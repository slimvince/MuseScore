#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_signature_sweep.py — protocol P8 pass-2 SIGNATURE SWEEP: apply every
# MECHANICAL DEFECT_TYPES.md rule across the ENTIRE L1/L2 inventory (all rows,
# not a sample) and write one hit table per catalog entry under tools/audit/l1l2/.
#
# Mechanical rules run here (the rest are review signatures, applied row-by-row
# in the report): DT-2, DT-3, DT-5, DT-12, DT-16, DT-19. Each rule either
# produces a hit list or raises — the script FAILS LOUDLY if any mechanical rule
# cannot run (no silent skip), per instruction Task 3 point 1.
#
# Read-only: greps the source tree via `git grep`, reads param_manifest.json and
# the frozen inventory CSVs. Writes only tools/audit/l1l2/sweep_*.{json,txt}.

import csv
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
L1L2 = os.path.join(HERE, "l1l2")

# The 13 deep-audited L1/L2 files (from file_table.csv tags L1/L2).
def l1l2_files():
    out = []
    with open(os.path.join(L1L2, "file_table.csv"), newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["tag"] in ("L1", "L2"):
                out.append(r["file"])
    return out


def read_csv(name):
    with open(os.path.join(L1L2, name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def git_grep_files(pattern, extra=None):
    """Return the set of tracked files containing pattern (fixed-string, -l)."""
    cmd = ["git", "-C", REPO, "grep", "-l", "-F", pattern, "--"]
    cmd += (extra or ["src"])
    try:
        out = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as e:
        raise RuntimeError("git not available for DT-5/DT-16 sweep: %s" % e)
    if out.returncode not in (0, 1):   # 1 == no match, still fine
        raise RuntimeError("git grep failed (%d): %s" % (out.returncode, out.stderr))
    return set(l.replace("\\", "/") for l in out.stdout.splitlines() if l.strip())


# ── DT-19 — layer-boundary violation (upward include) ─────────────────────────
# Mechanical: a file in L1/L2 including a header whose target_area is a HIGHER
# analysis layer. Layer rank: engraving/std/types/notemodel/slicing/engravingbridge/
# scoreharvest are at/below L1.5; 'key' is L3, 'chord' is L4 — UPWARD from L1/L2.
def sweep_dt19():
    UPWARD = {"key": "L3", "chord": "L4"}
    hits = []
    for r in read_csv("l1l2_crosslayer.csv"):
        area = r["target_area"]
        if area in UPWARD:
            hits.append({"file": r["file"], "line": r["line"], "include": r["include"],
                         "up_to": UPWARD[area],
                         "note": "L1/L2 file includes a %s header (upward dependency)" % UPWARD[area]})
    return hits


# ── DT-2 — unestablished / not-in-manifest inference constant ─────────────────
# Mechanical: every NAMED L1/L2 constant/param default whose name is NOT one of
# the 78 manifest parameters. Structural literals (0/1/2/4/12 and pure inits) are
# excluded by only considering NAMED fields/file-scope consts with a non-trivial
# musical/weight meaning.
def manifest_param_names():
    m = json.load(open(os.path.join(REPO, "tools", "param_manifest.json"), encoding="utf-8"))
    names = set()
    for p in m["parameters"]:
        nm = p.get("name", "")
        names.add(nm)
        names.add(nm.split(" ")[0])   # strip trailing "(...)" annotations
    return names


def sweep_dt2():
    names = manifest_param_names()
    # Named inference constants/params declared in L1/L2 headers (fields + file-scope).
    # (name, file, line, value) — enumerated from the inventory fields + literal table.
    candidates = []
    for r in read_csv("l1l2_fields.csv"):
        candidates.append((r["name"], r["file"], r["line"], r["context"].strip()))
    # file-scope named constants that are not struct fields (LOOKBACK_BEATS etc.)
    NAMED_CONST = {
        "LOOKBACK_BEATS", "LOOKAHEAD_BEATS", "LOOKAHEAD_WEIGHT", "DECAY_RATE",
        "kMinRegionTicks", "kPass2bMinRegionTicks",
    }
    for r in read_csv("l1l2_literals.csv"):
        ctx = r["context"]
        for nm in NAMED_CONST:
            if nm in ctx and (nm, r["file"], r["line"]) not in [(c[0], c[1], c[2]) for c in candidates]:
                candidates.append((nm, r["file"], r["line"], ctx.strip()))
    # inline (un-named) inference weights the pass must not miss: the 0.3 / 1.5 boosts
    INLINE = [
        ("repetitionBoost 0.3", "regiontonecollector.cpp", "297"),
        ("crossVoiceBoost 1.5", "regiontonecollector.cpp", "312"),
    ]

    STRUCTURAL = {"count", "sharpCount", "flatCount", "naturalCount", "lofCentroid",
                  "staff", "voice", "onsets", "strength", "perVoice", "textureTicks",
                  "textureStrength", "pickedTicks", "pitch", "tpc", "onset", "release",
                  "duration", "isGrace", "plays", "visible", "staffEligible",
                  "start", "end", "startTick", "endTick", "tauTicks"}
    hits = []
    seen = set()
    for nm, f, line, ctx in candidates:
        base = nm.split(" ")[0]
        if base in STRUCTURAL:
            continue
        in_man = base in names
        key = (base, f, line)
        if key in seen:
            continue
        seen.add(key)
        # only report the tunable-looking ones (weights, factors, windows, thresholds, k)
        if not in_man:
            hits.append({"name": base, "file": f, "line": line, "value": ctx[:80],
                         "in_manifest": False})
    for label, f, line in INLINE:
        full = "src/composing/analysis/engravingbridge/" + f
        hits.append({"name": label, "file": full, "line": line,
                     "value": "inline weightedPcView weight", "in_manifest": False})
    return hits


# ── DT-3 — value-copied constant (agree by history/comment, not by reference) ──
# Mechanical: a DEFINITION line that sets a numeric literal AND whose comment
# asserts equality to a NAMED CONSTANT elsewhere ("== <CONST>" where <CONST> is an
# ALL-CAPS or ::-qualified symbol). This is the true value-copy signature: the two
# literals agree by comment/history, not by reference. Plain equality-invariant
# comments ("onset == release", "count == sharpCount") are excluded — they compare
# runtime values, not couple two stored constants.
def sweep_dt3():
    hits = []
    files = l1l2_files()
    # comment token "== SYMBOL" where SYMBOL has an ALL-CAPS run (>=3) or a "::"
    eqre = re.compile(r"==\s*([A-Za-z_][A-Za-z0-9_:.]*(?:\s+[A-Z][A-Z0-9_]{2,})?)")
    litdef = re.compile(r"=\s*([0-9]+\.?[0-9]*)\s*;")
    for f in files:
        path = os.path.join(REPO, f)
        if not os.path.exists(path):
            raise RuntimeError("DT-3: L1/L2 file missing on disk: " + f)
        for i, ln in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
            if "//" not in ln:
                continue
            code, comment = ln.split("//", 1)
            lit = litdef.search(code)
            if not lit:
                continue   # not a numeric-literal DEFINITION line
            m = eqre.search(comment)
            if not m:
                continue
            sym = m.group(1).strip()
            # require the coupled reference to be a NAMED constant (uppercase run / ::)
            if not (re.search(r"[A-Z]{3,}", sym) or "::" in sym):
                continue
            hits.append({"kind": "comment-coupled-value-copy", "file": f, "line": i,
                         "couples_to": sym, "value": lit.group(1),
                         "text": ln.strip()[:120]})
    return hits


# ── DT-5 — siloed / trapped derived fact (0–1 production consumers) ────────────
def _owner_files(sym):
    """The L1/L2 file(s) that DEFINE sym (its .h/.cpp pair), from the inventory."""
    owners = set()
    for r in read_csv("l1l2_functions.csv"):
        if r["name"] == sym:
            owners.add(r["file"])
    for r in read_csv("l1l2_decls.csv"):
        if r["name"] == sym:
            owners.add(r["file"])
    for r in read_csv("l1l2_fields.csv"):
        if r["type_owner"] == sym:      # struct name
            owners.add(r["file"])
    # add the .h/.cpp pair of every owner
    pairs = set()
    for f in owners:
        stem, ext = os.path.splitext(f)
        pairs.add(stem + ".h")
        pairs.add(stem + ".cpp")
    return owners | pairs


# Hard-coded struct owners (structs have no function/decl row keyed by their own name).
STRUCT_OWNER = {
    "NoteModel": "src/composing/analysis/notemodel/note_model.h",
    "NoteEvent": "src/composing/analysis/notemodel/note_model.h",
    "SpanSpelling": "src/composing/analysis/engravingbridge/spellingview.h",
}


def sweep_dt5():
    SYMBOLS = [
        "changePointSlices", "weightedPcView", "collectRegionTones", "soundingAt",
        "collectSoundingAt", "buildTones", "pitchContextOverSpan", "collectPitchContext",
        "detectOnsetSubBoundaries", "detectBassMovementSubBoundaries", "findTemporalContext",
        "lineOfFifths", "sharpFlatSense", "spanSpelling", "SpanSpelling",
        "phraseBoundaryTicks", "computePhraseBoundaryProfile",
        "beatTypeToWeight", "regionMetricWeightForBeatType", "regionMetricWeightForOnsetTick",
        "beatTypeForOnsetTick", "safeBeatType", "timeDecay", "distinctPitchClasses",
        "buildPedalWindowIndex", "NoteModel", "NoteEvent",
    ]
    hits = []
    for sym in SYMBOLS:
        owners = _owner_files(sym)
        if not owners and sym in STRUCT_OWNER:
            f = STRUCT_OWNER[sym]
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


# ── DT-12 — stale anchor / dangling reference ─────────────────────────────────
# Mechanical: resolve every *.md doc reference and every file:line anchor that
# appears in L1/L2 source comments.
SWEEP_META = {}


def sweep_dt12():
    hits = []
    checked_md = 0
    checked_anchor = 0
    mdre = re.compile(r"([A-Za-z0-9_./-]+\.md)")
    anchorre = re.compile(r"([A-Za-z0-9_./]+\.(?:cpp|h)):(\d+)")
    for f in l1l2_files():
        path = os.path.join(REPO, f)
        for i, ln in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
            for md in set(mdre.findall(ln)):
                checked_md += 1
                # search repo root + a couple of common dirs
                found = (os.path.exists(os.path.join(REPO, md))
                         or os.path.exists(os.path.join(REPO, "docs", md)))
                if not found:
                    # last-resort: git ls-files basename
                    b = os.path.basename(md)
                    g = git_grep_files  # reuse subprocess env
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
                # accept both full-path and bare-filename anchors (comments use both,
                # e.g. "regionanalyzer.cpp:579"); resolve the basename via git ls-files.
                b = os.path.basename(tgt)
                if not b.endswith((".cpp", ".h")):
                    continue
                checked_anchor += 1
                try:
                    ls = subprocess.run(["git", "-C", REPO, "ls-files", "*" + b],
                                        capture_output=True, text=True)
                    cand = [c for c in ls.stdout.splitlines() if c.endswith(b)]
                except Exception:
                    cand = []
                # CONTENT-aware check: the file must exist with >= tl lines AND the
                # symbol the comment cites alongside the anchor must appear within a
                # small window of the cited line (else the line number has drifted).
                hint_syms = [h for h in re.findall(r"[A-Za-z_][A-Za-z0-9_:]{5,}",
                                                   ln.split(m.group(0), 1)[-1])
                             if not h.endswith(".cpp") and not h.endswith(".h")]
                exists = False
                content_ok = None
                for c in cand:
                    p = os.path.join(REPO, c)
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
# Mechanical: L1/L2 functions that WALK notes from the engraving DOM directly
# (s->cr / toChord(...)->notes() / n->ppitch() / n->play()) instead of reading the
# note model. buildPedalWindowIndex reading spanner()/pedals is non-note DOM and
# is reported separately as a scoped read, not a note re-walk.
def sweep_dt16():
    NOTE_DOM = [ "->notes()", "toChord(", "->ppitch()", "->cr(" ]
    # The note model (notemodel/) IS the layer that reads the DOM to BUILD the single
    # note source — that is its job, not a re-read. Exclude it; a DT-16 hit is a
    # CONSUMER re-walking DOM notes instead of reading the built model.
    BUILDER_DIR = "notemodel/"
    hits = []
    fns = read_csv("l1l2_functions.csv")
    for f in l1l2_files():
        if not f.endswith(".cpp") or BUILDER_DIR in f:
            continue
        path = os.path.join(REPO, f)
        lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
        for r in fns:
            if r["file"] != f:
                continue
            s, e = int(r["start_line"]), int(r["end_line"])
            # strip // comments so a comment MENTION of ->ppitch() is not a hit
            body_lines = []
            for ln in lines[s-1:e]:
                body_lines.append(ln.split("//", 1)[0])
            body = "\n".join(body_lines)
            if any(tok in body for tok in NOTE_DOM):
                takes_model = "NoteModel" in body or "noteModel" in body or "model." in body
                hits.append({"function": r["name"], "file": f,
                             "start_line": s, "walks_dom_notes": True,
                             "also_uses_note_model": takes_model,
                             "note": "walks engraving-DOM notes directly (bypasses the L1 note model)"})
    return hits


def main():
    results = {}
    runners = {
        "DT-2_unestablished_constant": sweep_dt2,
        "DT-3_value_copied_constant": sweep_dt3,
        "DT-5_siloed_fact": sweep_dt5,
        "DT-12_stale_anchor": sweep_dt12,
        "DT-16_raw_dom_outside_L1": sweep_dt16,
        "DT-19_layer_boundary": sweep_dt19,
    }
    errors = []
    for name, fn in runners.items():
        try:
            results[name] = fn()
        except Exception as e:   # fail LOUDLY — no silent skip (Task 3 point 1)
            errors.append("%s: %s" % (name, e))
    if errors:
        sys.stderr.write("FATAL: mechanical sweep rule(s) failed:\n  " + "\n  ".join(errors) + "\n")
        sys.exit(2)

    out = {"note": "P8 pass-2 mechanical DEFECT_TYPES sweep over the full L1/L2 inventory",
           "results": results,
           "counts": {k: len(v) for k, v in results.items()},
           "sweep_meta": SWEEP_META}
    with open(os.path.join(L1L2, "sweep_results.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)

    with open(os.path.join(L1L2, "sweep_results.txt"), "w", encoding="utf-8") as fh:
        for name, hitlist in results.items():
            fh.write("=== %s : %d hit(s) ===\n" % (name, len(hitlist)))
            for h in hitlist:
                fh.write("  " + json.dumps(h) + "\n")
            fh.write("\n")

    print("mechanical sweep complete. counts:")
    for k, v in results.items():
        print("  %-32s %d" % (k, len(v)))


if __name__ == "__main__":
    main()
