#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
"""Generate the joint estimator's EMBEDDED table artifacts (ratified Decision D1).

Turns the committed fitted artifacts under tools/joint_estimator/ into ONE compiled-in
C++ source (header + .cpp) under src/composing/analysis/joint/, so the running binary's
inference values are the ratified fitted values with provenance locked at BUILD time
(#16/#19). The JSON bytes are embedded VERBATIM (not a parsed-structure codegen): the bytes
ARE the artifact, they are parsed at load time through the SAME established parser as the
filesystem path (#6, one parse path), and the establishment check is byte equality.

Design (from cowork_notation_adoption_increment.md §5 Decision D1 +
cowork_notation_output_contract.md §2):
  * each of the five committed table artifacts -> its verbatim bytes as C-escaped
    string-literal chunks (concatenated at load into the exact file bytes) + its sha256;
  * the SELECTED weight vector -> extracted from decode_parity_ref.json's selected_weights
    (13 named weights, probe_decoder.WEIGHT_NAMES order), embedded as a verbatim JSON
    snippet (parsed at load into a WeightVector), with its provenance identity 'random07';
  * the §2 provenance constants published on the notation record (artifact hashes, the
    weight-vector identity, a decoder version) — DECLARED DORMANCY: their consumer is the
    notation record build (a later dispatch); nothing reads them yet.

This is the #17f mechanism: the figures enter source only through this generator, never by
hand. Regenerate (deterministic given the committed artifacts) with:
    python tools/joint_estimator/gen_embedded_tables.py
"""

import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(REPO, "src", "composing", "analysis", "joint")

# The five committed table artifacts, each with its generated C++ symbol base name.
FILE_ARTIFACTS = [
    ("tables_all.json", "kTablesAll"),
    ("note_tables_all.json", "kNoteTablesAll"),
    ("factor_presence_all.json", "kFactorPresenceAll"),
    ("fermata_boundary_addendum.json", "kFermataBoundaryAddendum"),
    ("mode_marginal.json", "kModeMarginal"),
]

# probe_decoder.WEIGHT_NAMES order — MUST match jointweights.cpp kWeightNames.
WEIGHT_NAMES = [
    "prior", "declared_mode", "emission", "spelling", "bass", "boundary",
    "chord_trans", "key_trans", "entry",
    "cad_leading_tone", "cad_tritone_pair", "cad_dominant_tonic_bass", "cad_fermata_location",
]

# The joint decoder's OWN version string (the module's own; defined here per the contract §2).
# Pins the decode CODE for the record's provenance; bump on any change to the decode
# arithmetic. The fitted-value provenance is the artifact hashes + weight identity below.
DECODER_VERSION = "1.0"

# Break the verbatim bytes into chunks of this many ORIGINAL bytes; the escaped literal is at
# most ~4x this, well under the MSVC 65535-byte single-string-literal limit.
CHUNK_BYTES = 2048

CHUNK_ESCAPE = {
    0x22: '\\"',    # "
    0x5c: '\\\\',   # backslash
    0x0a: '\\n',    # LF
    0x0d: '\\r',    # CR
    0x09: '\\t',    # HT
    0x3f: '\\?',    # ? — escaped to make trigraph sequences impossible
}


def escape_byte(b):
    """One C string-literal token for a single byte (unambiguous; 3-digit octal for
    everything non-printable, so a following digit can never extend the escape)."""
    e = CHUNK_ESCAPE.get(b)
    if e is not None:
        return e
    if 0x20 <= b <= 0x7e:
        return chr(b)
    return "\\%03o" % b


def chunk_literals(data):
    """Return the list of escaped string-literal chunk bodies for `data` (bytes)."""
    chunks = []
    for i in range(0, len(data), CHUNK_BYTES):
        chunks.append("".join(escape_byte(b) for b in data[i:i + CHUNK_BYTES]))
    if not chunks:
        chunks.append("")  # an empty artifact -> one empty chunk
    return chunks


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


LICENSE = """/*
 * SPDX-License-Identifier: GPL-3.0-only
 * MuseScore-Studio-CLA-applies
 *
 * MuseScore Studio
 * Music Composition & Notation
 *
 * Copyright (C) 2026 MuseScore Limited
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 3 as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
"""


def gen_header(blobs, weight_blob, corpus_git_hash):
    lines = [LICENSE.rstrip("\n"), ""]
    lines.append("// ★ GENERATED FILE — DO NOT EDIT BY HAND.")
    lines.append("// Produced by tools/joint_estimator/gen_embedded_tables.py from the committed fitted")
    lines.append("// artifacts under tools/joint_estimator/ (ratified Decision D1). Regenerate with:")
    lines.append("//     python tools/joint_estimator/gen_embedded_tables.py")
    lines.append("//")
    lines.append("// The five table artifacts + the SELECTED weight vector are embedded VERBATIM (JSON")
    lines.append("// bytes, not a parsed-structure codegen) and parsed at load through the SAME parser as")
    lines.append("// the filesystem path (#6). Establishment = byte equality vs the committed artifacts")
    lines.append("// (the joint_embedded_tests drift guard). Source corpus: %s." % corpus_git_hash)
    lines.append("")
    lines.append("#ifndef MU_COMPOSING_ANALYSIS_JOINT_JOINTEMBEDDEDARTIFACTS_H")
    lines.append("#define MU_COMPOSING_ANALYSIS_JOINT_JOINTEMBEDDEDARTIFACTS_H")
    lines.append("")
    lines.append("#include <array>")
    lines.append("#include <cstddef>")
    lines.append("#include <string>")
    lines.append("")
    lines.append("namespace mu::composing::analysis::joint::embedded {")
    lines.append("/// One embedded artifact: the committed file's bytes stored VERBATIM as compiled-in")
    lines.append("/// C-string chunks (JSON text carries no NUL byte, so each chunk is NUL-terminated and")
    lines.append("/// its length is strlen; bytes() concatenates them into the exact file bytes). `sha256`")
    lines.append("/// is the lowercase-hex digest of those verbatim bytes (== the committed file's digest).")
    lines.append("struct EmbeddedBlob {")
    lines.append("    const char* const* chunks;")
    lines.append("    std::size_t chunkCount;")
    lines.append("    std::size_t byteLen;   ///< total verbatim byte length")
    lines.append("    const char* sha256;    ///< lowercase-hex sha256 of the verbatim bytes")
    lines.append("    const char* name;      ///< source artifact name")
    lines.append("")
    lines.append("    std::string bytes() const;   ///< reconstruct the verbatim file bytes")
    lines.append("};")
    lines.append("")
    lines.append("// ── the five committed table artifacts (verbatim) ────────────────────────────────────")
    for _, base in FILE_ARTIFACTS:
        lines.append("extern const EmbeddedBlob %s;" % base)
    lines.append("")
    lines.append("/// The five table artifacts, for the drift guard.")
    lines.append("extern const std::array<const EmbeddedBlob*, %d> kTableArtifacts;" % len(FILE_ARTIFACTS))
    lines.append("")
    lines.append("/// The direct-metric SELECTED weight vector (probe_decoder selected_start 'random07'),")
    lines.append("/// extracted from decode_parity_ref.json's selected_weights and embedded VERBATIM as a")
    lines.append("/// JSON snippet in WEIGHT_NAMES order; parsed at load by joint::selectedWeights().")
    lines.append("extern const EmbeddedBlob kSelectedWeightsJson;")
    lines.append("")
    lines.append("// ── §2 provenance constants (published on the notation output-surface record). ────────")
    lines.append("// DECLARED DORMANCY (fact-publication corollary): their named consumer is the notation")
    lines.append("// record build (a later dispatch); nothing reads them yet.")
    lines.append('extern const char* const kWeightVectorIdentity;   ///< "random07"')
    lines.append("extern const char* const kDecoderVersion;         ///< the joint decoder's own version")
    lines.append("extern const char* const kCorpusGitHash;          ///< source corpus (tables_all provenance)")
    lines.append("extern const char* const kGeneratedBy;            ///< the generating instrument")
    lines.append("} // namespace mu::composing::analysis::joint::embedded")
    lines.append("")
    lines.append("#endif // MU_COMPOSING_ANALYSIS_JOINT_JOINTEMBEDDEDARTIFACTS_H")
    lines.append("")
    return "\n".join(lines)


def emit_chunk_array(base, chunks):
    out = ["const char* const %s_chunks[] = {" % base]
    for c in chunks:
        out.append('    "%s",' % c)
    out.append("};")
    return out


def gen_source(blobs, weight_blob, corpus_git_hash):
    lines = [LICENSE.rstrip("\n"), ""]
    lines.append("// ★ GENERATED FILE — DO NOT EDIT BY HAND.")
    lines.append("// Produced by tools/joint_estimator/gen_embedded_tables.py. See the header for the")
    lines.append("// design and the regeneration command. Source corpus: %s." % corpus_git_hash)
    lines.append("//")
    lines.append("// Embedded artifacts and their sha256 (== the committed tools/joint_estimator/ files):")
    for name, base, digest, blen, nchunks, _chunks in blobs:
        lines.append("//   %-32s %s  (%d bytes, %d chunks)" % (name, digest, blen, nchunks))
    lines.append("//   %-32s %s  (%d bytes; 'random07', value-exact vs decode_parity_ref.json)"
                 % (weight_blob[0], weight_blob[2], weight_blob[3]))
    lines.append("")
    lines.append('#include "jointembeddedartifacts.h"')
    lines.append("")
    lines.append("namespace mu::composing::analysis::joint::embedded {")
    lines.append("std::string EmbeddedBlob::bytes() const")
    lines.append("{")
    lines.append("    std::string s;")
    lines.append("    s.reserve(byteLen);")
    lines.append("    for (std::size_t i = 0; i < chunkCount; ++i) {")
    lines.append("        s.append(chunks[i]);   // NUL-terminated (JSON carries no NUL byte)")
    lines.append("    }")
    lines.append("    return s;")
    lines.append("}")
    lines.append("")
    lines.append("namespace {")
    # chunk arrays for each file artifact
    for (name, base), chunks in zip(FILE_ARTIFACTS, [b[5] for b in blobs]):
        lines += emit_chunk_array(base, chunks)
    # weight snippet chunk array
    lines += emit_chunk_array("kSelectedWeightsJson", weight_blob[4])
    lines.append("} // namespace")
    lines.append("")
    for name, base, digest, blen, nchunks, _chunks in blobs:
        lines.append('const EmbeddedBlob %s = { %s_chunks, %du, %du, "%s", "%s" };'
                     % (base, base, nchunks, blen, digest, name))
    wname, wbase, wdigest, wlen, wchunks = weight_blob
    lines.append('const EmbeddedBlob kSelectedWeightsJson = { kSelectedWeightsJson_chunks, %du, %du, "%s", "%s" };'
                 % (len(wchunks), wlen, wdigest, wname))
    lines.append("")
    lines.append("const std::array<const EmbeddedBlob*, %d> kTableArtifacts = {{" % len(FILE_ARTIFACTS))
    lines.append("    " + ", ".join("&%s" % base for _, base in FILE_ARTIFACTS))
    lines.append("}};")
    lines.append("")
    lines.append('const char* const kWeightVectorIdentity = "random07";')
    lines.append('const char* const kDecoderVersion = "%s";' % DECODER_VERSION)
    lines.append('const char* const kCorpusGitHash = "%s";' % corpus_git_hash)
    lines.append('const char* const kGeneratedBy = "tools/joint_estimator/gen_embedded_tables.py";')
    lines.append("} // namespace mu::composing::analysis::joint::embedded")
    lines.append("")
    return "\n".join(lines)


def main():
    # File artifacts.
    blobs = []            # (name, base, sha256, byteLen, nChunks, chunks)
    corpus_git_hash = None
    for name, base in FILE_ARTIFACTS:
        path = os.path.join(HERE, name)
        data = read_bytes(path)
        digest = hashlib.sha256(data).hexdigest()
        chunks = chunk_literals(data)
        blobs.append((name, base, digest, len(data), len(chunks), chunks))
        if name == "tables_all.json":
            corpus_git_hash = json.loads(data.decode("utf-8")).get("provenance", {}).get("corpus_git_hash", "")

    # The SELECTED weight vector, extracted from decode_parity_ref.json.
    parity = json.loads(read_bytes(os.path.join(HERE, "decode_parity_ref.json")).decode("utf-8"))
    sel = parity["selected_weights"]
    start = parity.get("provenance", {}).get("selected_start", "")
    if start != "random07":
        print("WARNING: decode_parity_ref.json selected_start is %r, not 'random07'" % start, file=sys.stderr)
    ordered = {n: sel[n] for n in WEIGHT_NAMES}      # WEIGHT_NAMES order, all 13 present
    snippet = json.dumps(ordered).encode("utf-8")     # verbatim embedded snippet bytes
    wdigest = hashlib.sha256(snippet).hexdigest()
    wchunks = chunk_literals(snippet)
    weight_blob = ("selected_weights@decode_parity_ref.json", "kSelectedWeightsJson",
                   wdigest, len(snippet), wchunks)

    header = gen_header(blobs, weight_blob, corpus_git_hash)
    source = gen_source(blobs, weight_blob, corpus_git_hash)

    hdr_path = os.path.join(OUT_DIR, "jointembeddedartifacts.h")
    src_path = os.path.join(OUT_DIR, "jointembeddedartifacts.cpp")
    with open(hdr_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(header)
    with open(src_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(source)

    # Report (for the operator; the source itself is the deliverable).
    print("corpus_git_hash: %s" % corpus_git_hash)
    print("wrote %s" % hdr_path)
    print("wrote %s (%d bytes)" % (src_path, len(source.encode("utf-8"))))
    for name, base, digest, blen, nchunks, _c in blobs:
        print("  %-32s %s  %7d bytes  %3d chunks" % (name, digest, blen, nchunks))
    print("  %-32s %s  %7d bytes  %3d chunks  ('%s')"
          % ("selected_weights", wdigest, len(snippet), len(wchunks), start))


if __name__ == "__main__":
    main()
