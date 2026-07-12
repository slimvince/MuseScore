#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_signature_sweep.py — protocol P8 pass-2 SIGNATURE SWEEP: apply every
# MECHANICAL DEFECT_TYPES.md rule across the ENTIRE inventory of the audited
# layer (all rows, not a sample) and write one hit table per catalog entry under
# tools/audit/<layer>/.
#
# ONE layer-selected instrument (OI-95 point (a); the gen_inventory.py --layer
# pattern): `--layer l1l2` (default) reproduces the original L1/L2 sweep
# byte-for-byte; `--layer l3` runs the same mechanical rules over the L3
# inventory with L3-appropriate inputs, plus a DT-5 dead-LOCAL-struct-field
# sub-check (the class the L3 pass-2 second reading surfaced — extraToneScore).
#
# Mechanical rules run here: DT-2, DT-3, DT-5, DT-12, DT-16, DT-19. The rest are
# review signatures, applied row-by-row in the report. Each rule either produces
# a hit list or raises — the script FAILS LOUDLY if any mechanical rule cannot
# run (no silent skip), per instruction Task 3 point 1.
#
# Read-only: greps the source tree via `git grep`, reads param_manifest.json and
# the frozen inventory CSVs. Writes only tools/audit/<layer>/sweep_*.{json,txt}.

import argparse
import csv
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))

# ── Per-layer configuration ───────────────────────────────────────────────────
LAYERS = {
    "l1l2": {
        "dir": "l1l2",
        "prefix": "l1l2_",
        "file_tags": ("L1", "L2"),
        # target_area -> the HIGHER layer it points to (an upward include).
        "dt19_upward": {"key": "L3", "chord": "L4"},
        "dt2_named_const": {
            "LOOKBACK_BEATS", "LOOKAHEAD_BEATS", "LOOKAHEAD_WEIGHT", "DECAY_RATE",
            "kMinRegionTicks", "kPass2bMinRegionTicks",
        },
        "dt2_inline": [
            ("repetitionBoost 0.3", "src/composing/analysis/engravingbridge/regiontonecollector.cpp", "297"),
            ("crossVoiceBoost 1.5", "src/composing/analysis/engravingbridge/regiontonecollector.cpp", "312"),
        ],
        "dt2_mode": "blocklist",
        "dt3_soft_copy": False,
        "dt5_symbols": [
            "changePointSlices", "weightedPcView", "collectRegionTones", "soundingAt",
            "collectSoundingAt", "buildTones", "pitchContextOverSpan", "collectPitchContext",
            "detectOnsetSubBoundaries", "detectBassMovementSubBoundaries", "findTemporalContext",
            "lineOfFifths", "sharpFlatSense", "spanSpelling", "SpanSpelling",
            "phraseBoundaryTicks", "computePhraseBoundaryProfile",
            "beatTypeToWeight", "regionMetricWeightForBeatType", "regionMetricWeightForOnsetTick",
            "beatTypeForOnsetTick", "safeBeatType", "timeDecay", "distinctPitchClasses",
            "buildPedalWindowIndex", "NoteModel", "NoteEvent",
        ],
        "dt5_struct_owner": {
            "NoteModel": "src/composing/analysis/notemodel/note_model.h",
            "NoteEvent": "src/composing/analysis/notemodel/note_model.h",
            "SpanSpelling": "src/composing/analysis/engravingbridge/spellingview.h",
        },
        "dt5_local_dead": False,
    },
    "l3": {
        "dir": "l3",
        "prefix": "l3_",
        "file_tags": ("L3", "L3-MIXED"),
        # For L3 the higher analysis layers are chord(L4)/function(L5)/progression(L5)/
        # grouping(L6)/voiceleading(L4)/vocabulary(L4)/decode(L4). region/section/harmony/
        # notemodel/slicing/engravingbridge/scoreharvest/types/key/external are peer-or-lower.
        "dt19_upward": {"chord": "L4", "function": "L5", "progression": "L5",
                        "grouping": "L6", "voiceleading": "L4", "vocabulary": "L4",
                        "decode": "L4"},
        "dt2_named_const": {
            "kEstablishmentMinChords", "kPitchTolerance", "kPervasiveFraction",
            "kDominanceRatio", "kWeightBase", "kWeightStructural", "kWeightChromatic",
            "kWeightFinality", "kSingleStateConfidence", "kJointModulationFallbackConfidence",
            "kAnnotateKeyConfidenceThreshold", "kMaxPivotLookaheadRegions",
        },
        "dt2_inline": [],
        # L3 inference tunables live in these config structs (whole surface = OI-91).
        "dt2_mode": "config_structs",
        "dt2_config_struct_suffixes": ("Preferences", "Preset", "Weights"),
        "dt3_soft_copy": True,
        "dt5_symbols": [
            "decode", "redecodeRange", "decodeLattice", "changeCost", "analyzeKeyMode",
            "resolveKeyAndModeRanked", "resolveKeySignatureContext",
            "detectAuthenticCadences", "aggregateGlobalAnchor", "detectLocalModulations",
            "decideJointKey", "setJointKeyWiringEnabled", "jointKeyWiringEnabled",
            "keyModeTonicName", "keyModeSuffix", "keyModeScaleIntervals",
            "ionianTonicPcForMode", "keySignatureFifthsForKey", "keyModeSignatureFifths",
            "modePriorPresets", "detectCadences", "detectPivotChords",
            "hasAssertiveKeyConfidence", "normalizedConfidenceSigmoid",
        ],
        "dt5_struct_owner": {},
        "dt5_local_dead": True,
    },
    "l4": {
        "dir": "l4",
        "prefix": "l4_",
        "file_tags": ("L4-SCORER", "L4-DECODER", "L4-MIXED"),
        # For L4 the higher analysis layers are function(L5)/progression(L5)/
        # grouping(L6). chord/decode = L4 peer; region/types/key(L3)/notemodel/
        # slicing/engravingbridge/scoreharvest/external = peer-or-lower.
        "dt19_upward": {"function": "L5", "progression": "L5", "grouping": "L6"},
        "dt2_named_const": set(),
        "dt2_inline": [],
        # L4: the override-registered file-scope scoring constants (registerDouble)
        # + the *Preferences/*Preset/*Weights config-struct members, each checked
        # against param_manifest.json. Mechanical: the registered names are read
        # from the source, not hardcoded (would-be-circular).
        "dt2_mode": "registered_config",
        "dt2_config_struct_suffixes": ("Preferences", "Preset", "Weights"),
        "dt3_soft_copy": True,
        "dt5_symbols": [
            "decode", "redecodeRange", "decodeSelection", "classifyMembership",
            "computeConfidence", "nameOpenQuestion", "deriveChordExtensions",
            "computeRawFanoutSummary", "formatSymbol", "formatRomanNumeral",
            "formatNashvilleNumber", "refineSparseChordQualityFromKeyContext",
            "applyTonicPriorToSparseChord", "forceChordTrackQualityFromKeyContext",
            "diatonicMaskFromFifths", "collectionMask", "recordNode",
        ],
        "dt5_struct_owner": {
            "ChordPathNode": "src/composing/analysis/decode/chordpathdecoder.h",
        },
        "dt5_local_dead": True,
    },
    "l5": {
        "dir": "l5",
        "prefix": "l5_",
        # L5 spans the dormant function/progression resolver (C++), the Python
        # instrument chain, and the shared C++ harness batch_analyze.cpp.
        "file_tags": ("L5-DORMANT", "INSTRUMENT", "INSTRUMENT-HARNESS"),
        # L5 is the TOP analysis layer; the only strictly-upward analysis target
        # is L6 (grouping/display). key/chord/region/etc. are peer-or-lower.
        "dt19_upward": {"grouping": "L6"},
        "dt2_named_const": set(),
        "dt2_inline": [],
        # The dormant resolver's firewall seeds live in the *Params config structs
        # (FunctionCadenceParams / ModulationParams / FunctionOutputParams /
        # FunctionResolverParams / RecognitionParams / ForwardOverrideParams);
        # each member checked against param_manifest.json (reproduces OI-120).
        "dt2_mode": "config_structs",
        "dt2_config_struct_suffixes": ("Params",),
        "dt3_soft_copy": True,
        "dt5_symbols": [
            "resolveCarriedReadings", "forwardRecompute", "classifyRelationalLabel",
            "degreeFunctionalBias", "recognizeProgressions", "deriveBaseRomanNumeral",
            "labelTonicizations", "cadenceTonicVote", "isLicensedProgression",
            "detectFunctionalCadences",
        ],
        "dt5_struct_owner": {},
        "dt5_local_dead": True,
        # L5-only extensions: the Python-aware instrument rules + the manifest
        # site-anchor check (gated so l1l2/l3/l4 sweeps stay byte-identical).
        "py_rules": True,
        "py_files": None,   # resolved at runtime = the .py layer_files
        "dt24_committed_prefixes": (
            "tools/corpus", "tools/robust_stop", "tools/calibration_maps",
            "tools/stage5_split_registry.json", "tools/param_manifest.json",
            "tools/corpus_registry.json", "tools/extra_scores_registry.json",
        ),
        "dt25_help_fn": "printHelp",
        "dt25_arg_file": "tools/batch_analyze.cpp",
        # manifest sites whose file basename matches one of these are L5-scoped
        "dt12_manifest_scope": ("function/", "progression/", "forwardoverride",
                                "batch_analyze.cpp"),
    },
}


def cfg(args):
    return LAYERS[args.layer]


def layer_dir(c):
    return os.path.join(HERE, c["dir"])


def layer_files(c):
    out = []
    with open(os.path.join(layer_dir(c), "file_table.csv"), newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["tag"] in c["file_tags"]:
                out.append(r["file"])
    return out


def read_csv(c, short):
    """short e.g. 'functions' -> <prefix>functions.csv"""
    with open(os.path.join(layer_dir(c), c["prefix"] + short + ".csv"),
              newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def git_grep_files(pattern, extra=None):
    cmd = ["git", "-C", REPO, "grep", "-l", "-F", pattern, "--"]
    cmd += (extra or ["src"])
    try:
        out = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as e:
        raise RuntimeError("git not available for DT-5/DT-16 sweep: %s" % e)
    if out.returncode not in (0, 1):
        raise RuntimeError("git grep failed (%d): %s" % (out.returncode, out.stderr))
    return set(l.replace("\\", "/") for l in out.stdout.splitlines() if l.strip())


# ── DT-19 — layer-boundary violation (upward include) ─────────────────────────
def sweep_dt19(c):
    upward = c["dt19_upward"]
    # file tag lookup so the report can tell a pure-layer file from a MIXED one.
    tag = {}
    with open(os.path.join(layer_dir(c), "file_table.csv"), newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            tag[r["file"]] = r["tag"]
    hits = []
    for r in read_csv(c, "crosslayer"):
        area = r["target_area"]
        if area in upward:
            ftag = tag.get(r["file"], "")
            hits.append({"file": r["file"], "line": r["line"], "include": r["include"],
                         "up_to": upward[area], "including_file_tag": ftag,
                         "note": "%s file includes a %s header (upward dependency%s)" % (
                             ftag, upward[area],
                             "; MIXED orchestrator — expected" if "MIXED" in ftag else "")})
    return hits


# ── DT-2 — unestablished / not-in-manifest inference constant ─────────────────
def manifest_param_names():
    m = json.load(open(os.path.join(REPO, "tools", "param_manifest.json"), encoding="utf-8"))
    names = set()
    for p in m["parameters"]:
        nm = p.get("name", "")
        names.add(nm)
        names.add(nm.split(" ")[0])
    return names


def sweep_dt2(c):
    names = manifest_param_names()
    hits = []
    seen = set()
    if c["dt2_mode"] == "config_structs":
        # L3: the inference tunables are the members of the *Preferences/*Preset/
        # *Weights structs (the whole L3 emission surface) + the named k-consts.
        suffixes = c["dt2_config_struct_suffixes"]
        for r in read_csv(c, "fields"):
            owner = r.get("type_owner", "")
            if not owner.endswith(suffixes):
                continue
            base = r["name"]
            key = (base, r["file"], r["line"])
            if key in seen:
                continue
            seen.add(key)
            if base not in names:
                hits.append({"name": base, "owner": owner, "file": r["file"],
                             "line": r["line"], "value": r["context"].strip()[:90],
                             "in_manifest": False})
        # named file-scope k-consts (surface via the literal table)
        named_const = c["dt2_named_const"]
        for r in read_csv(c, "literals"):
            ctx = r["context"]
            for nm in named_const:
                if nm in ctx:
                    key = (nm, r["file"], r["line"])
                    if key in seen:
                        continue
                    seen.add(key)
                    if nm not in names:
                        hits.append({"name": nm, "owner": "<file-scope>", "file": r["file"],
                                     "line": r["line"], "value": ctx.strip()[:90],
                                     "in_manifest": False})
        return hits

    if c["dt2_mode"] == "registered_config":
        # (a) override-registered file-scope scoring constants (registerDouble)
        #     absent from the manifest — read the registered NAMES from source.
        regre = re.compile(r'registerDouble\("([^"]+)"')
        for f in layer_files(c):
            path = os.path.join(REPO, f)
            if not os.path.exists(path):
                raise RuntimeError("DT-2: layer file missing on disk: " + f)
            for i, ln in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
                for m in regre.finditer(ln):
                    nm = m.group(1)
                    if nm in names or nm.split(" ")[0] in names:
                        continue
                    key = (nm, f, str(i))
                    if key in seen:
                        continue
                    seen.add(key)
                    hits.append({"name": nm, "owner": "<registerDouble>", "file": f,
                                 "line": str(i), "value": ln.strip()[:90],
                                 "in_manifest": False})
        # (b) config-struct members (Preferences/Preset/Weights) absent from manifest.
        suffixes = c["dt2_config_struct_suffixes"]
        for r in read_csv(c, "fields"):
            owner = r.get("type_owner", "")
            if not owner.endswith(suffixes):
                continue
            basen = r["name"]
            key = (basen, r["file"], r["line"])
            if key in seen:
                continue
            seen.add(key)
            if basen not in names:
                hits.append({"name": basen, "owner": owner, "file": r["file"],
                             "line": r["line"], "value": r["context"].strip()[:90],
                             "in_manifest": False})
        return hits

    # l1l2: original blocklist behavior (report every non-structural named const
    # not in the manifest), preserved byte-for-byte.
    candidates = []
    for r in read_csv(c, "fields"):
        candidates.append((r["name"], r["file"], r["line"], r["context"].strip()))
    named_const = c["dt2_named_const"]
    seen_cand = set((x[0], x[1], x[2]) for x in candidates)
    for r in read_csv(c, "literals"):
        ctx = r["context"]
        for nm in named_const:
            if nm in ctx and (nm, r["file"], r["line"]) not in seen_cand:
                candidates.append((nm, r["file"], r["line"], ctx.strip()))
                seen_cand.add((nm, r["file"], r["line"]))
    STRUCTURAL = {"count", "sharpCount", "flatCount", "naturalCount", "lofCentroid",
                  "staff", "voice", "onsets", "strength", "perVoice", "textureTicks",
                  "textureStrength", "pickedTicks", "pitch", "tpc", "onset", "release",
                  "duration", "isGrace", "plays", "visible", "staffEligible",
                  "start", "end", "startTick", "endTick", "tauTicks"}
    for nm, f, line, ctx in candidates:
        base = nm.split(" ")[0]
        if base in STRUCTURAL:
            continue
        in_man = base in names
        key = (base, f, line)
        if key in seen:
            continue
        seen.add(key)
        if not in_man:
            hits.append({"name": base, "file": f, "line": line, "value": ctx[:80],
                         "in_manifest": False})
    for label, f, line in c["dt2_inline"]:
        hits.append({"name": label, "file": f, "line": line,
                     "value": "inline weightedPcView weight", "in_manifest": False})
    return hits


# ── DT-3 — value-copied constant (agree by comment/history, not by reference) ──
def sweep_dt3(c):
    hits = []
    files = layer_files(c)
    eqre = re.compile(r"==?\s*([A-Za-z_][A-Za-z0-9_:.]*(?:\s+[A-Z][A-Z0-9_]{2,})?)")
    litdef = re.compile(r"=\s*([0-9]+\.?[0-9]*)\s*[;,]")
    idcopy = re.compile(r"=\s*([A-Za-z_][A-Za-z0-9_]{4,})\b")
    for f in files:
        path = os.path.join(REPO, f)
        if not os.path.exists(path):
            raise RuntimeError("DT-3: layer file missing on disk: " + f)
        for i, ln in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
            if "//" not in ln:
                continue
            code, comment = ln.split("//", 1)
            lit = litdef.search(code)
            if not lit:
                continue
            # comment asserts equality/identity to a NAMED symbol
            m = eqre.search(comment)
            named = m and (re.search(r"[A-Z]{3,}", m.group(1)) or "::" in m.group(1))
            # OR the comment says "= <identifier> by default" naming a same-scope field
            softcopy = idcopy.search(comment)
            if named:
                hits.append({"kind": "comment-coupled-value-copy", "file": f, "line": i,
                             "couples_to": m.group(1).strip(), "value": lit.group(1),
                             "text": ln.strip()[:130]})
            elif c["dt3_soft_copy"] and softcopy and ("default" in comment.lower() or "=" in comment):
                sym = softcopy.group(1)
                if sym.lower() not in ("true", "false", "nullptr", "default"):
                    hits.append({"kind": "comment-soft-value-copy", "file": f, "line": i,
                                 "couples_to": sym, "value": lit.group(1),
                                 "text": ln.strip()[:130]})
    return hits


# ── DT-5 — siloed / trapped derived fact (0–1 production consumers) ────────────
def _owner_files(c, sym):
    owners = set()
    for r in read_csv(c, "functions"):
        if r["name"] == sym:
            owners.add(r["file"])
    for r in read_csv(c, "decls"):
        if r["name"] == sym:
            owners.add(r["file"])
    for r in read_csv(c, "fields"):
        if r["type_owner"] == sym:
            owners.add(r["file"])
    pairs = set()
    for f in owners:
        stem, ext = os.path.splitext(f)
        pairs.add(stem + ".h")
        pairs.add(stem + ".cpp")
    return owners | pairs


def sweep_dt5(c):
    hits = []
    for sym in c["dt5_symbols"]:
        owners = _owner_files(c, sym)
        if not owners and sym in c["dt5_struct_owner"]:
            f = c["dt5_struct_owner"][sym]
            stem = os.path.splitext(f)[0]
            owners = {f, stem + ".h", stem + ".cpp"}
        if not owners:
            raise RuntimeError("DT-5: no owner file resolved for symbol " + sym)
        files = git_grep_files(sym)
        external = sorted(
            f for f in files
            if "/tests/" not in f
            and "test" not in os.path.basename(f).lower()
            and f not in owners)
        if len(external) <= 1:
            hits.append({"symbol": sym, "owner_files": sorted(owners),
                         "external_production_consumers": external,
                         "n_external": len(external),
                         "note": "0-1 production consumers outside its own module (siloed/dormant)"})
    return hits


# ── DT-5 (local) — a dead LOCAL struct field: assigned somewhere but never READ
# in its owning translation unit. Enumerates structs DEFINED inside each layer
# .cpp (their fields are confined to that TU) and flags any field with >=1 write
# and 0 reads. This is the class the L3 pass-2 reading surfaced (extraToneScore).
def sweep_dt5_local(c):
    hits = []
    field_decl = re.compile(r"^\s*(?:const\s+|static\s+|constexpr\s+|mutable\s+)*"
                            r"[A-Za-z_][\w:<>,\s\*&]*?\b([A-Za-z_]\w*)\s*(?:=[^=]|;|\{\})")
    for f in layer_files(c):
        if not f.endswith(".cpp"):
            continue
        path = os.path.join(REPO, f)
        text = open(path, encoding="utf-8", errors="replace").read()
        lines = text.splitlines()
        # find `struct <Name> { ... };` blocks by brace matching
        for sm in re.finditer(r"\bstruct\s+([A-Za-z_]\w*)\s*\{", text):
            name = sm.group(1)
            i = sm.end()  # just after '{'
            depth = 1
            body_start = i
            while i < len(text) and depth > 0:
                ch = text[i]
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                i += 1
            body = text[body_start:i-1]
            # only single-level (no nested struct) field lines
            fields = []
            for bl in body.splitlines():
                bl_nc = bl.split("//", 1)[0]
                if "(" in bl_nc:            # skip methods
                    continue
                m = field_decl.match(bl_nc)
                if m:
                    fld = m.group(1)
                    if fld and fld not in ("struct", "return"):
                        fields.append(fld)
            for fld in set(fields):
                # count reads vs writes across the owning TU
                tok = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(fld) + r"(?![A-Za-z0-9_])")
                total = 0
                writes = 0
                for ln in lines:
                    lnc = ln.split("//", 1)[0]
                    occ = tok.findall(lnc)
                    if not occ:
                        continue
                    total += len(occ)
                    # a write: `.<fld> =` or `<fld> =` (assignment, not ==) or a decl `= init`
                    if re.search(r"(?<![A-Za-z0-9_])" + re.escape(fld) + r"\s*=(?!=)", lnc):
                        writes += len(re.findall(
                            r"(?<![A-Za-z0-9_])" + re.escape(fld) + r"\s*=(?!=)", lnc))
                reads = total - writes
                # dead = at least one write, zero reads, appears at most a handful of
                # times (guards against very common short names used elsewhere).
                if writes >= 1 and reads == 0 and total <= 6:
                    hits.append({"struct": name, "field": fld, "file": f,
                                 "total_occurrences": total, "writes": writes, "reads": reads,
                                 "note": "assigned but never read in its owning TU — dead/vestigial local field (DT-5)"})
    return hits


# ── DT-12 — stale anchor / dangling reference ─────────────────────────────────
SWEEP_META = {}


def sweep_dt12(c):
    hits = []
    checked_md = 0
    checked_anchor = 0
    mdre = re.compile(r"([A-Za-z0-9_./-]+\.md)")
    anchorre = re.compile(r"([A-Za-z0-9_./]+\.(?:cpp|h)):(\d+)")
    for f in layer_files(c):
        path = os.path.join(REPO, f)
        for i, ln in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
            for md in set(mdre.findall(ln)):
                checked_md += 1
                found = (os.path.exists(os.path.join(REPO, md))
                         or os.path.exists(os.path.join(REPO, "docs", md)))
                if not found:
                    b = os.path.basename(md)
                    try:
                        ls = subprocess.run(["git", "-C", REPO, "ls-files", "*" + b],
                                            capture_output=True, text=True)
                        found = bool(ls.stdout.strip())
                    except Exception:
                        found = False
                if not found:
                    hits.append({"file": f, "line": i, "kind": "md-ref",
                                 "ref": md, "resolves": False})
            for m in anchorre.finditer(ln):
                tgt, tl = m.group(1), int(m.group(2))
                b = os.path.basename(tgt)
                if not b.endswith((".cpp", ".h")):
                    continue
                checked_anchor += 1
                try:
                    ls = subprocess.run(["git", "-C", REPO, "ls-files", "*" + b],
                                        capture_output=True, text=True)
                    cand = [c2 for c2 in ls.stdout.splitlines() if c2.endswith(b)]
                except Exception:
                    cand = []
                hint_syms = [h for h in re.findall(r"[A-Za-z_][A-Za-z0-9_:]{5,}",
                                                   ln.split(m.group(0), 1)[-1])
                             if not h.endswith(".cpp") and not h.endswith(".h")]
                exists = False
                content_ok = None
                for c2 in cand:
                    p = os.path.join(REPO, c2)
                    if not os.path.exists(p):
                        continue
                    tlines = open(p, encoding="utf-8", errors="replace").read().splitlines()
                    if len(tlines) < tl:
                        continue
                    exists = True
                    if hint_syms:
                        lo = max(0, tl - 7)
                        hi = min(len(tlines), tl + 6)
                        window = "\n".join(tlines[lo:hi])
                        content_ok = any(h.split("::")[-1] in window for h in hint_syms)
                    break
                if not exists:
                    hits.append({"file": f, "line": i, "kind": "file:line-anchor",
                                 "ref": "%s:%d" % (tgt, tl), "resolves": False,
                                 "why": "target file missing or too short"})
                elif content_ok is False:
                    hits.append({"file": f, "line": i, "kind": "file:line-anchor-stale-content",
                                 "ref": "%s:%d" % (tgt, tl), "resolves": False,
                                 "cited_symbol": hint_syms,
                                 "why": "cited symbol not near the cited line — line number drifted"})
    SWEEP_META["DT-12_refs_checked"] = {"md_refs": checked_md, "file_line_anchors": checked_anchor}
    if checked_md == 0 and checked_anchor == 0:
        raise RuntimeError("DT-12: found NO references to check — regex/scan broke, refusing silent 0")
    return hits


# ── DT-16 — raw-DOM interpretation outside the L1 note model ───────────────────
def sweep_dt16(c):
    NOTE_DOM = ["->notes()", "toChord(", "->ppitch()", "->cr("]
    BUILDER_DIR = "notemodel/"
    hits = []
    fns = read_csv(c, "functions")
    for f in layer_files(c):
        if not f.endswith(".cpp") or BUILDER_DIR in f:
            continue
        path = os.path.join(REPO, f)
        lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
        for r in fns:
            if r["file"] != f:
                continue
            s, e = int(r["start_line"]), int(r["end_line"])
            body_lines = [ln.split("//", 1)[0] for ln in lines[s-1:e]]
            body = "\n".join(body_lines)
            if any(tok in body for tok in NOTE_DOM):
                takes_model = "NoteModel" in body or "noteModel" in body or "model." in body
                hits.append({"function": r["name"], "file": f,
                             "start_line": s, "walks_dom_notes": True,
                             "also_uses_note_model": takes_model,
                             "note": "walks engraving-DOM notes directly (bypasses the L1 note model)"})
    return hits


# ── DT-23 — silent-failure / silent-drop path in a Python instrument ──────────
# A broad `except Exception` (or bare `except:`) whose handler only swallows
# (pass / continue / return None / return / <v> = [] / <v> = None / <v> = globalkey)
# with NO surfacing (print / raise / sys.stderr / logging) and NO skip-counter
# (`+= 1` / `.append(`) in the handler block. Reproduces OI-123 / OI-128.
def _py_layer_files(c):
    return [f for f in layer_files(c) if f.endswith(".py")]


def sweep_dt23(c):
    hits = []
    broad = re.compile(r"^(\s*)except\s*(Exception)?\s*(?:as\s+\w+)?\s*:")
    surfacing = ("print", "raise", "sys.stderr", "logging", "log.", "warn", "warnings")
    counter = ("+= 1", "+=1", ".append(", ".add(", "skipped", "errors.append")
    for f in _py_layer_files(c):
        lines = open(os.path.join(REPO, f), encoding="utf-8", errors="replace").read().splitlines()
        for i, ln in enumerate(lines):
            m = broad.match(ln)
            if not m:
                continue
            indent = len(m.group(1))
            # collect the handler block (more-indented following lines)
            body = []
            for j in range(i + 1, min(i + 12, len(lines))):
                bl = lines[j]
                if bl.strip() == "":
                    continue
                bind = len(bl) - len(bl.lstrip())
                if bind <= indent:
                    break
                body.append(bl)
            btext = "\n".join(body)
            swallow = bool(re.search(r"^\s*(pass|continue|return\b.*|[\w.\[\]]+\s*=\s*(\[\]|None|\{\}|globalkey|global_key))\s*$",
                                     btext.strip().splitlines()[0] if btext.strip() else "", re.M)) if body else False
            has_surface = any(s in btext for s in surfacing)
            has_counter = any(cc in btext for cc in counter)
            if body and swallow and not has_surface and not has_counter:
                hits.append({"file": f, "line": i + 1, "except": ln.strip(),
                             "handler_first": body[0].strip()[:80],
                             "note": "broad/bare except swallows with no surfacing/skip-counter (DT-23 silent-failure)"})
    return hits


# ── DT-24 — destructive default output path (argparse default under a committed ref)
def sweep_dt24(c):
    hits = []
    prefixes = c["dt24_committed_prefixes"]
    addarg = re.compile(r"add_argument\(([^)]*)\)", re.S)
    for f in _py_layer_files(c):
        text = open(os.path.join(REPO, f), encoding="utf-8", errors="replace").read()
        for m in addarg.finditer(text):
            call = m.group(1)
            if "default" not in call:
                continue
            dm = re.search(r"default\s*=\s*[\"']([^\"']+)[\"']", call)
            if not dm:
                continue
            dv = dm.group(1).replace("\\", "/")
            if any(dv == p or dv.startswith(p.rstrip("/") + "/") or dv == p for p in prefixes) or \
               any(dv.startswith(p) for p in prefixes):
                nm = re.search(r"[\"'](--?[\w-]+)[\"']", call)
                line = text[:m.start()].count("\n") + 1
                hits.append({"file": f, "line": line, "arg": nm.group(1) if nm else "?",
                             "default": dv,
                             "note": "argparse default resolves under a committed reference path (DT-24 destructive default)"})
    return hits


# ── DT-25 — undocumented mode: a flag the C++ arg parser matches but printHelp() omits
def sweep_dt25(c):
    argf = c["dt25_arg_file"]
    path = os.path.join(REPO, argf)
    if not os.path.exists(path):
        raise RuntimeError("DT-25: arg file missing: " + argf)
    text = open(path, encoding="utf-8", errors="replace").read()
    parsed = set(re.findall(r'==\s*"(--[\w-]+)"', text))
    parsed |= set(re.findall(r'a\s*==\s*"(--[\w-]+)"', text))
    # extract printHelp() body
    fn = c["dt25_help_fn"]
    hm = re.search(r"\b" + re.escape(fn) + r"\s*\([^)]*\)\s*\{", text)
    help_text = ""
    if hm:
        i = hm.end(); depth = 1; start = i
        while i < len(text) and depth > 0:
            if text[i] == "{": depth += 1
            elif text[i] == "}": depth -= 1
            i += 1
        help_text = text[start:i]
    documented = set(re.findall(r"(--[\w-]+)", help_text))
    if not parsed:
        raise RuntimeError("DT-25: no parsed flags found — regex broke, refusing silent 0")
    hits = []
    for flag in sorted(parsed - documented):
        line = text.find('"' + flag + '"')
        ln = text[:line].count("\n") + 1 if line >= 0 else 0
        hits.append({"file": argf, "line": ln, "flag": flag,
                     "note": "flag parsed by the arg parser but absent from printHelp() (DT-25 undocumented mode)"})
    return hits


# ── DT-12 (manifest sites) — param_manifest 'site' file:line anchors that no
# longer point at the named symbol (line drift). Scoped to the L5 files. This is
# the manifest→source direction (the source→doc direction is sweep_dt12).
def sweep_dt12_manifest_sites(c):
    # L5-scoped by file BASENAME (manifest 'site' values are basenames like
    # "functionresolver.h:197", not paths) — the set of L5 layer-file basenames.
    l5_basenames = {os.path.basename(f) for f in layer_files(c)}
    m = json.load(open(os.path.join(REPO, "tools", "param_manifest.json"), encoding="utf-8"))
    hits = []
    checked = 0
    for p in m["parameters"]:
        site = p.get("site", "")
        if ":" not in site:
            continue
        base, ln = site.rsplit(":", 1)
        if not ln.strip().isdigit():
            continue
        if os.path.basename(base) not in l5_basenames:
            continue
        # locate the source file
        try:
            ls = subprocess.run(["git", "-C", REPO, "ls-files", "*" + os.path.basename(base)],
                                capture_output=True, text=True)
            cand = [x for x in ls.stdout.splitlines() if x.endswith(os.path.basename(base))]
        except Exception:
            cand = []
        sym = p.get("name", "").split(" ")[0]
        checked += 1
        target = int(ln)
        resolved = False
        for c2 in cand:
            fp = os.path.join(REPO, c2)
            if not os.path.exists(fp):
                continue
            tl = open(fp, encoding="utf-8", errors="replace").read().splitlines()
            if len(tl) < target or not sym:
                continue
            lo, hi = max(0, target - 4), min(len(tl), target + 3)
            window = "\n".join(tl[lo:hi])
            if sym in window:
                resolved = True
            break
        if cand and not resolved and sym:
            hits.append({"param": p.get("name", ""), "site": site, "symbol": sym,
                         "note": "manifest 'site' line does not contain the named param — line drift (DT-12 manifest anchor)"})
    SWEEP_META["DT-12_manifest_sites_checked"] = checked
    return hits


def main():
    ap = argparse.ArgumentParser(description="P8 pass-2 mechanical DEFECT_TYPES sweep over a layer's inventory")
    ap.add_argument("--layer", choices=sorted(LAYERS.keys()), default="l1l2")
    args = ap.parse_args()
    c = cfg(args)

    runners = {
        "DT-2_unestablished_constant": lambda: sweep_dt2(c),
        "DT-3_value_copied_constant": lambda: sweep_dt3(c),
        "DT-5_siloed_fact": lambda: sweep_dt5(c),
        "DT-12_stale_anchor": lambda: sweep_dt12(c),
        "DT-16_raw_dom_outside_L1": lambda: sweep_dt16(c),
        "DT-19_layer_boundary": lambda: sweep_dt19(c),
    }
    if c["dt5_local_dead"]:
        runners["DT-5_local_dead_field"] = lambda: sweep_dt5_local(c)
    if c.get("py_rules"):
        runners["DT-23_silent_failure"] = lambda: sweep_dt23(c)
        runners["DT-24_destructive_default"] = lambda: sweep_dt24(c)
        runners["DT-25_undocumented_mode"] = lambda: sweep_dt25(c)
        runners["DT-12_manifest_site_drift"] = lambda: sweep_dt12_manifest_sites(c)

    results = {}
    errors = []
    for name, fn in runners.items():
        try:
            results[name] = fn()
        except Exception as e:
            errors.append("%s: %s" % (name, e))
    if errors:
        sys.stderr.write("FATAL: mechanical sweep rule(s) failed:\n  " + "\n  ".join(errors) + "\n")
        sys.exit(2)

    out = {"note": "P8 pass-2 mechanical DEFECT_TYPES sweep over the full %s inventory" % args.layer,
           "layer": args.layer,
           "results": results,
           "counts": {k: len(v) for k, v in results.items()},
           "sweep_meta": SWEEP_META}
    with open(os.path.join(layer_dir(c), "sweep_results.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)

    with open(os.path.join(layer_dir(c), "sweep_results.txt"), "w", encoding="utf-8") as fh:
        for name, hitlist in results.items():
            fh.write("=== %s : %d hit(s) ===\n" % (name, len(hitlist)))
            for h in hitlist:
                fh.write("  " + json.dumps(h) + "\n")
            fh.write("\n")

    print("mechanical sweep (%s) complete. counts:" % args.layer)
    for k, v in results.items():
        print("  %-32s %d" % (k, len(v)))


if __name__ == "__main__":
    main()
