#!/usr/bin/env python3
"""Mode-grading adjudication probe (OI-132 / DISCOVERY D2, OI-145 wave 1) — READ-ONLY.

The measurement-chain hardening surfaced a music-theory disagreement between two graded key
parsers (compare_rn._our_key_tonic — the SHARED substrate every governing graded surface uses —
and oracle_root_metric.parse_our_key). They reduce our analyzer's DOMINANT-FAMILY exotic modes
(the modes whose TONIC TRIAD is major but whose PARENT COLLECTION is a minor scale) to
major-or-minor DIFFERENTLY for key-agreement grading. Consolidating to ONE shared rule moves a
graded figure whichever rule wins, so the USER rules on the rule. This probe produces the
evidence that ruling needs; it TOUCHES NO GRADED-PIPELINE CODE — both candidate rules are
computed side by side here only.

The two candidate rules (grading OUR emitted key/mode → (tonic_pc, is_major)):

  RULE A — TONIC-TRIAD QUALITY: a key is named by its tonic chord. The five dominant-family modes
    have a MAJOR (major-third) tonic triad, so a span our engine labels e.g. "E PhrygDom" grades
    as (E, major) — same tonic, major.  [= what oracle_root_metric.parse_our_key does for
    PhrygDom/alt.]

  RULE B — PARENT COLLECTION: the mode is a rotation of a minor (harmonic/melodic) parent scale,
    so the span grades as the minor key of that PARENT'S tonic — a DIFFERENT tonic. "E PhrygDom"
    is the 5th mode of A harmonic minor, so it grades as (A, minor) — the key it is the dominant
    OF, which is what a DCML annotator writes when keeping a dominant-heavy passage in the minor.

The five dominant-family conflict modes (major tonic triad, minor parent), with the parent
derivation cited (standard modes-of-the-scale theory):

  PhrygDom  5th mode of HARMONIC minor  → parent tonic = emitted − 7 semitones (P5 below), minor
  Mixb6     5th mode of MELODIC  minor  → parent tonic = emitted − 7 semitones (P5 below), minor
  Lydb7     4th mode of MELODIC  minor  → parent tonic = emitted − 5 semitones (P4 below), minor
  Lyd+      3rd mode of MELODIC  minor  → parent tonic = emitted − 3 semitones (m3 below), minor
  alt       7th mode of MELODIC  minor  → parent tonic = emitted + 1 semitone  (m2 above), minor

The two rules DIFFER only on these five modes (Rule A: emitted-tonic + major; Rule B: parent-tonic
+ minor). On EVERY other emitted mode both rules fall back to the current committed reduction
(compare_rn._our_key_tonic) verbatim — so, with the disagreeing population excluded, both rules
reproduce the committed key-agreement columns EXACTLY (proved by the establishment check below).

The grading harness (union-of-boundaries cells over ours ∪ DCML boundaries, duration-weighted,
DCML ground truth through the OI-142-corrected dcml.load_wir_regions) is REPLICATED from
a8_rebaseline_measure.build_piece_grid; the per-cell baseline key verdict reproduces
a8's committed tools/robust_stop/summary.json agg counters byte-for-byte (establishment (a)).

READ-ONLY: writes ONLY to --out — which defaults to a SCRATCH path (OI-151). It does NOT default
to tools/reports/mode_grading_adjudication_probe.json: that file is COMMITTED evidence, the record
the user's OI-132 ruling was made on, and a bare re-run silently overwriting it destroys the
pre-ruling evidence and breaks the figures cited in cc_mode_grading_adjudication_probe_report.md
(#12 information loss + #10 doc-sync). Writing that path is an explicit --out. The probe also
validates the committed corpus manifest before reading (characterise_bir_false.validate_corpus_dir)
and touches NOTHING under tools/robust_stop/ or tools/corpus/.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import compare_rn as crn                 # noqa: E402  (the shared graded substrate — reused verbatim)
import compare_analyses as cmp           # noqa: E402
import dcml_parser as dcml               # noqa: E402
from characterise_bir_false import validate_corpus_dir  # noqa: E402

WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"
CORPUS_ROOT = _ROOT / "tools" / "corpus"
COMMITTED_SUMMARY = _ROOT / "tools" / "robust_stop" / "summary.json"
PRESETS = ("baroque", "jazz", "default")
PC_NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def pcn(p):
    return PC_NAMES[p % 12] if p is not None and p >= 0 else "?"


def keystr(reduction):
    tc, maj = reduction
    if tc is None:
        return "KEYFAIL"
    return f"{pcn(tc)}{'maj' if maj else 'min'}"


# ── the five dominant-family conflict modes (major tonic triad, minor parent) ──
# suffix (ASCII-normalized) -> (parent_offset_semitones, parent_is_major)
# Rule A on these = (emitted_tonic, True). Rule B = ((emitted_tonic + off) % 12, parent_is_major).
CONFLICT_MODES = {
    "PhrygDom": (-7, False),   # 5th mode of harmonic minor
    "Mixb6":    (-7, False),   # 5th mode of melodic minor (Aeolian dominant)
    "Lydb7":    (-5, False),   # 4th mode of melodic minor (Lydian dominant)
    "Lyd+":     (-3, False),   # 3rd mode of melodic minor (Lydian augmented)
    "alt":      (+1, False),   # 7th mode of melodic minor (altered / super-Locrian)
}

_TONIC_RE = re.compile(r"^([A-G][#b]?)(.*)$")


def _split_key(k: str):
    """Emitted key string -> (tonic_pc | None, ascii_mode_suffix). ASCII-normalizes ♭/♯."""
    if not k:
        return None, ""
    k2 = k.replace("♯", "#").replace("♭", "b")
    m = _TONIC_RE.match(k2)
    if not m:
        return None, k2
    return dcml._key_to_tonic_pc(m.group(1)), m.group(2)


def is_conflict_key(k: str) -> bool:
    _, suf = _split_key(k)
    return suf in CONFLICT_MODES


def reduce_baseline(k: str):
    """The CURRENT committed reduction — the shared graded substrate, verbatim."""
    return crn._our_key_tonic(k)


def reduce_rule_a(k: str):
    """Rule A — tonic-triad quality. Conflict modes -> (emitted tonic, major); else baseline."""
    tonic, suf = _split_key(k)
    if suf in CONFLICT_MODES:
        return (tonic if tonic is None else tonic % 12, True)
    return crn._our_key_tonic(k)


def reduce_rule_b(k: str):
    """Rule B — parent collection. Conflict modes -> (parent tonic, parent mode); else baseline."""
    tonic, suf = _split_key(k)
    if suf in CONFLICT_MODES:
        off, parent_is_major = CONFLICT_MODES[suf]
        return (None if tonic is None else (tonic + off) % 12, parent_is_major)
    return crn._our_key_tonic(k)


def verdict(our_reduction, dcml_key_str):
    """Replicate a8's key verdict: keyfail if our reduction unparseable, dcml_keyfail if DCML
    unparseable, else agree/disagree on (tonic, is_major) equality. Same buckets as a8.add_cell."""
    otc, omaj = our_reduction
    dtc, dmaj = crn._dcml_key_tonic(dcml_key_str)
    if otc is None:
        return "keyfail"
    if dtc is None:
        return "dcml_keyfail"
    return "agree" if (otc, omaj) == (dtc, dmaj) else "disagree"


# ── the cell harness — replicated from a8_rebaseline_measure.build_piece_grid ──
def build_cells(stem, ours_regions, wir_regions):
    """Union-of-boundaries cells (ours ∪ DCML boundaries), each carrying the RAW key strings so the
    verdict can be recomputed under every candidate reduction. Construction identical to
    a8.build_piece_grid; self-validated against crn.grid_score_regions per piece."""
    cells = []
    if not ours_regions or not wir_regions:
        return cells
    ours_spans = [(r.start_tick, r.end_tick) for r in ours_regions]
    dcml_spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    bounds = set()
    for (s, e) in ours_spans:
        if e > s:
            bounds.add(s); bounds.add(e)
    for (s, e) in dcml_spans:
        if s >= 0 and e > s:
            bounds.add(s); bounds.add(e)
    if len(bounds) < 2:
        return cells
    grid = sorted(bounds)
    scored_dur = 0
    bucket_dur = Counter()
    for i in range(len(grid) - 1):
        t0, t1 = grid[i], grid[i + 1]
        if t1 - t0 <= 0:
            continue
        oi = crn._active_index_at(ours_spans, t0)
        di = crn._active_index_at(dcml_spans, t0)
        if oi is None or di is None:
            continue
        our_r = ours_regions[oi]
        dcml_r = wir_regions[di]
        pair = crn.classify_pair(our_r, dcml_r)
        if pair is None:
            continue
        w = t1 - t0
        scored_dur += w
        bucket_dur[pair.category] += w
        cells.append({
            "stem": stem, "t0": t0, "t1": t1, "w": w,
            "our_key": our_r.key,
            "our_sym": our_r.chord_symbol,
            "dcml_global": dcml_r.global_key,
            "dcml_local": dcml_r.local_key,
            "dcml_sym": dcml_r.chord_symbol,
        })
    # self-validation: the buckets/duration must match the pinned primitive exactly.
    oracle = crn.grid_score_regions(ours_regions, wir_regions)
    if dict(bucket_dur) != dict(oracle.bucket_dur) or scored_dur != oracle.scored_dur:
        raise AssertionError(
            f"{stem}: cell harness diverges from grid_score_regions "
            f"(mine={dict(bucket_dur)} scored={scored_dur} vs "
            f"oracle={dict(oracle.bucket_dur)} scored={oracle.scored_dur})")
    return cells


def measure_preset(preset):
    corpus_dir = CORPUS_ROOT / preset
    validate_corpus_dir(corpus_dir)   # OI-129/OI-35 discipline: manifest-gate the read

    # three reductions × two GT columns, duration-weighted; plus the population.
    RULES = {"baseline": reduce_baseline, "ruleA": reduce_rule_a, "ruleB": reduce_rule_b}
    COLS = {"home": "dcml_global", "local": "dcml_local"}
    # agg[rule][col] -> Counter of verdict -> duration
    agg = {r: {c: Counter() for c in COLS} for r in RULES}
    # same, but with the disagreeing population EXCLUDED (for establishment (b))
    agg_excl = {r: {c: Counter() for c in COLS} for r in RULES}
    scored_dur = 0

    pop_cells = []                       # the disagreeing population (conflict-mode cells)
    pop_by_mode = defaultdict(lambda: [0, 0])   # suffix -> [regions(cells), duration]
    pop_by_stem = defaultdict(lambda: [0, 0])   # stem   -> [cells, duration]

    for ours_path in sorted(corpus_dir.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours", "")
        wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
        if wir_path is None:
            continue                     # no human GT — the same legitimate exclusion a8 makes
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            print(f"[{preset}] DROPPED {stem} — ours load failed ({type(exc).__name__}: {exc})",
                  file=sys.stderr)
            continue
        wir_regions = dcml.load_wir_regions(str(WIR_DIR), stem)   # OI-142-corrected substrate
        if not wir_regions:
            continue

        for c in build_cells(stem, ours_regions, wir_regions):
            w = c["w"]
            scored_dur += w
            in_pop = is_conflict_key(c["our_key"])
            if in_pop:
                _, suf = _split_key(c["our_key"])
                pop_by_mode[suf][0] += 1
                pop_by_mode[suf][1] += w
                pop_by_stem[stem][0] += 1
                pop_by_stem[stem][1] += w
            for rname, rfn in RULES.items():
                red = rfn(c["our_key"])
                for cname, field in COLS.items():
                    v = verdict(red, c[field])
                    agg[rname][cname][v] += w
                    if not in_pop:
                        agg_excl[rname][cname][v] += w
            if in_pop:
                pop_cells.append({
                    "stem": stem, "t0": c["t0"], "t1": c["t1"], "w": w,
                    "our_key": c["our_key"], "our_sym": c["our_sym"],
                    "dcml_global": c["dcml_global"], "dcml_local": c["dcml_local"],
                    "dcml_sym": c["dcml_sym"],
                    "baseline": keystr(reduce_baseline(c["our_key"])),
                    "ruleA": keystr(reduce_rule_a(c["our_key"])),
                    "ruleB": keystr(reduce_rule_b(c["our_key"])),
                    "v_baseline_home": verdict(reduce_baseline(c["our_key"]), c["dcml_global"]),
                    "v_ruleA_home": verdict(reduce_rule_a(c["our_key"]), c["dcml_global"]),
                    "v_ruleB_home": verdict(reduce_rule_b(c["our_key"]), c["dcml_global"]),
                    "v_baseline_local": verdict(reduce_baseline(c["our_key"]), c["dcml_local"]),
                    "v_ruleA_local": verdict(reduce_rule_a(c["our_key"]), c["dcml_local"]),
                    "v_ruleB_local": verdict(reduce_rule_b(c["our_key"]), c["dcml_local"]),
                })

    def pct(rule, col):
        return 100.0 * agg[rule][col]["agree"] / scored_dur if scored_dur else 0.0

    figures = {}
    for col in COLS:
        figures[col] = {r: {
            "agree_dur": agg[r][col]["agree"],
            "disagree_dur": agg[r][col]["disagree"],
            "keyfail_dur": agg[r][col]["keyfail"],
            "dcml_keyfail_dur": agg[r][col]["dcml_keyfail"],
            "agree_pct": round(pct(r, col), 4),
        } for r in RULES}

    return {
        "preset": preset,
        "scored_dur": scored_dur,
        "figures": figures,
        "agg_excl": {r: {c: dict(agg_excl[r][c]) for c in COLS} for r in RULES},
        "population": {
            "cells": len(pop_cells),
            "duration": sum(pc_["w"] for pc_ in pop_cells),
            "pct_of_scored": round(100.0 * sum(pc_["w"] for pc_ in pop_cells) / scored_dur, 4)
                             if scored_dur else 0.0,
            "by_mode": {k: {"cells": v[0], "duration": v[1]} for k, v in sorted(pop_by_mode.items())},
            "by_stem": {k: {"cells": v[0], "duration": v[1]}
                        for k, v in sorted(pop_by_stem.items(), key=lambda x: -x[1][1])},
        },
        "population_cells": pop_cells,
    }


def establishment(results):
    """Prove (a) baseline reproduces the committed columns exactly, and (b) with the population
    excluded, ruleA and ruleB equal baseline exactly. Returns (ok, lines)."""
    committed = json.loads(COMMITTED_SUMMARY.read_text(encoding="utf-8"))
    ok = True
    lines = []
    for r in results:
        p = r["preset"]
        cagg = committed[p]["agg"]
        f = r["figures"]
        # (a) baseline home/local agree/dis/keyfail == committed a8 counters
        checks = [
            ("home.agree", f["home"]["baseline"]["agree_dur"], cagg["b_key_agree"]),
            ("home.disagree", f["home"]["baseline"]["disagree_dur"], cagg["b_key_dis"]),
            ("home.keyfail", f["home"]["baseline"]["keyfail_dur"], cagg["b_key_fail"]),
            ("home.dcml_keyfail", f["home"]["baseline"]["dcml_keyfail_dur"], cagg["b_dcml_keyfail"]),
            ("local.agree", f["local"]["baseline"]["agree_dur"], cagg["b_key_agree_local"]),
            ("local.disagree", f["local"]["baseline"]["disagree_dur"], cagg["b_key_dis_local"]),
            ("local.keyfail", f["local"]["baseline"]["keyfail_dur"], cagg["b_key_fail_local"]),
            ("local.dcml_keyfail", f["local"]["baseline"]["dcml_keyfail_dur"],
             cagg["b_dcml_keyfail_local"]),
            ("scored_dur", r["scored_dur"], cagg["scored_dur"]),
        ]
        for name, mine, theirs in checks:
            match = (mine == theirs)
            ok = ok and match
            if not match:
                lines.append(f"  [{p}] (a) MISMATCH {name}: probe={mine} committed={theirs}")
        # (b) population-excluded: ruleA == ruleB == baseline
        ex = r["agg_excl"]
        for col in ("home", "local"):
            b = ex["baseline"][col]
            for rule in ("ruleA", "ruleB"):
                match = (ex[rule][col] == b)
                ok = ok and match
                if not match:
                    lines.append(f"  [{p}] (b) MISMATCH {rule}.{col} excl-pop: "
                                 f"{ex[rule][col]} != baseline {b}")
        lines.append(f"  [{p}] (a) baseline reproduces committed columns: "
                     f"{'OK' if all(m == t for _, m, t in checks) else 'FAIL'}; "
                     f"(b) excl-population ruleA==ruleB==baseline: "
                     f"{'OK' if all(ex[rr][cc] == ex['baseline'][cc] for rr in ('ruleA','ruleB') for cc in ('home','local')) else 'FAIL'}")
    return ok, lines


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    # SCRATCH default (OI-151) — see the module docstring. The committed evidence path is written
    # only when it is asked for by name.
    ap.add_argument("--out", default="C:/tmp/mode_grading_adjudication_probe.json",
                    help="write the JSON report here (default: a scratch path; pass "
                         "tools/reports/mode_grading_adjudication_probe.json explicitly to "
                         "overwrite the committed OI-132 ruling evidence)")
    args = ap.parse_args()

    results = [measure_preset(p) for p in PRESETS]
    ok, est_lines = establishment(results)

    # ── printed report ──
    print("=" * 92)
    print("MODE-GRADING ADJUDICATION PROBE (OI-132 / D2) — READ-ONLY")
    print("=" * 92)
    print("\nDisagreeing population (conflict modes PhrygDom/Mixb6/Lydb7/Lyd+/alt):")
    for r in results:
        pop = r["population"]
        print(f"  {r['preset']:8}  cells={pop['cells']:4d}  dur={pop['duration']:7d}  "
              f"({pop['pct_of_scored']:.3f}% of scored)   by-mode: "
              + ", ".join(f"{k}={v['cells']}c/{v['duration']}d" for k, v in pop["by_mode"].items()))

    print("\nEight-figure key-agreement table (agree%, and Δ vs committed baseline):")
    for r in results:
        p = r["preset"]; f = r["figures"]
        print(f"\n  {p}:")
        for col in ("home", "local"):
            b = f[col]["baseline"]["agree_pct"]
            a = f[col]["ruleA"]["agree_pct"]
            bb = f[col]["ruleB"]["agree_pct"]
            print(f"    {col:5}  baseline={b:7.4f}   ruleA={a:7.4f} (Δ{a-b:+.4f})   "
                  f"ruleB={bb:7.4f} (Δ{bb-b:+.4f})   |A-B|={abs(a-bb):.4f}")

    print("\nEstablishment:")
    for ln in est_lines:
        print(ln)
    print(f"\nESTABLISHMENT {'PASS' if ok else 'FAIL'}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "probe": "mode_grading_adjudication_probe",
        "read_only": True,
        "corpus_root": str(CORPUS_ROOT),
        "committed_summary": str(COMMITTED_SUMMARY),
        "conflict_modes": {k: {"parent_offset": v[0], "parent_is_major": v[1]}
                           for k, v in CONFLICT_MODES.items()},
        "establishment_pass": ok,
        "establishment_lines": est_lines,
        "presets": [{k: v for k, v in r.items() if k != "population_cells"} for r in results],
        "population_cells": {r["preset"]: r["population_cells"] for r in results},
    }
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    print(f"\nwrote {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
