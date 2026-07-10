#!/usr/bin/env python3
"""cc_eg2_probe.py — EG-2 rebuilt-vs-legacy read-only probe on the a8 robust unit.

READ-ONLY / MEASUREMENT-ONLY. No src/ change, no corpus mutation, no gate change, no
robust-stop reference re-baseline. Grades the REBUILT arm (the E0 --dump-fullspine
override-OFF dump) vs the LEGACY arm (the committed tools/corpus/<preset> production
.ours.json) against the DCML/WiR root ground truth on the A-8 granularity-robust
union-of-boundaries unit (variant-b, DCML-only), root axis.

ORCHESTRATION ONLY over already-pinned primitives (the a8 discipline):
  - compare_rn.classify_pair / grid_score_regions / _active_index_at / _our_key_tonic /
    _dcml_key_tonic
  - compare_analyses.load_analysis / _dcml_time_spans
  - characterise_bir_false.validate_corpus_dir      (manifest / no-contamination gate)
  - a8_rebaseline_measure.cell_class                (the two-tier class-(a)/(b) test)
  - dcml_parser.find_wir_file / parse_rntxt_file

The ONE thing this adds over a8_rebaseline_measure is ABSTAIN-AWARENESS: the rebuilt
per-slice arm ABSTAINS (rootPitchClass = -1) on ~63% of slices, and classify_pair scores
an abstain cell as root_err. But the two-tier policy + the E0 report §4-C define class-(b)
as a wrong COMMIT (chain COMMITTED a wrong root); an ABSTAIN is coverage-loss, NOT class-(b).
So a root-failing cell is bucketed:
   committed (our_root >= 0) & wrong  -> cell_class() -> class-(a) or class-(b)
   abstain   (our_root <  0)          -> coverage-loss (never class-(a)/(b))
For the legacy arm (commits everywhere, no our_root<0) this reduces EXACTLY to a8's
b_cls_b_dur — cross-checked against the committed tools/robust_stop reference.

Per-piece self-validation: the variant-(b) 5-bucket duration decomposition is asserted
byte-identical to compare_rn.grid_score_regions() (the a8 faithfulness proof).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import compare_analyses as cmp        # noqa: E402
import compare_rn as crn              # noqa: E402
import characterise_bir_false as cbf  # noqa: E402
import dcml_parser as dcml            # noqa: E402
import a8_rebaseline_measure as a8    # noqa: E402  (cell_class + the symmetric tests)

WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"


def merge_runs(cells):
    """Merge adjacent same-(stem,our_root,dcml_root) cells whose spans touch into runs
    (the re-slice-stable stem@runStartTick identity). Verbatim copy of the a8 nested
    merge_runs (which is not importable)."""
    runs = []
    cur = None
    for stem, c in sorted(cells, key=lambda x: (x[0], x[1]["t0"])):
        key = (stem, c["our_root"], c["dcml_root"])
        if cur and cur["key"] == key and cur["end"] == c["t0"]:
            cur["end"] = c["t1"]; cur["dur"] += c["w"]
        else:
            if cur:
                runs.append(cur)
            cur = {"key": key, "stem": stem, "start": c["t0"], "end": c["t1"],
                   "dur": c["w"], "our_root": c["our_root"], "dcml_root": c["dcml_root"],
                   "our_sym": c["our_sym"], "cls": c["cls"]}
    if cur:
        runs.append(cur)
    return runs


def grade_piece(stem, ours_regions, wir_regions, ref_spans=None):
    """Union-of-boundaries cell loop (ours ∪ DCML), abstain-aware root bucketing.
    Returns (cells, dcml_spans, scored_dur, unscored_dur).

    ref_spans: if None (default), the DCML tick spans are computed from THIS arm's own
    regions via the pinned cmp._dcml_time_spans (the a8-native mode) and the variant-b
    bucket decomposition is self-validated byte-identical to grid_score_regions(). If a
    span list is supplied (the COMMON-anchoring mode, EG-2 Task 1.5 / P4(c) fix), it is
    used verbatim for BOTH arms so the DCML ground truth is anchored to identical ticks
    regardless of the arm's segmentation granularity — removing the measure-anchor
    interpolation confound. Self-validation is skipped in that mode (grid_score_regions
    re-derives spans from the arm's own regions, so it is only an oracle for own-anchor)."""
    cells = []
    if not ours_regions or not wir_regions:
        return cells, [], 0, 0
    ours_spans = [(r.start_tick, r.end_tick) for r in ours_regions]
    dcml_spans = ref_spans if ref_spans is not None else cmp._dcml_time_spans(ours_regions, wir_regions)
    bounds = set()
    for (s, e) in ours_spans:
        if e > s:
            bounds.add(s); bounds.add(e)
    for (s, e) in dcml_spans:
        if s >= 0 and e > s:
            bounds.add(s); bounds.add(e)
    if len(bounds) < 2:
        return cells, dcml_spans, 0, 0
    grid = sorted(bounds)
    scored_dur = unscored_dur = 0
    bucket_dur = Counter()
    for i in range(len(grid) - 1):
        t0, t1 = grid[i], grid[i + 1]
        w = t1 - t0
        if w <= 0:
            continue
        oi = crn._active_index_at(ours_spans, t0)
        di = crn._active_index_at(dcml_spans, t0)
        if oi is None or di is None:
            unscored_dur += w
            continue
        our_r = ours_regions[oi]
        dcml_r = wir_regions[di]
        pair = crn.classify_pair(our_r, dcml_r)
        if pair is None:
            unscored_dur += w
            continue
        scored_dur += w
        bucket_dur[pair.category] += w
        our_root = our_r.root_pc
        committed = (our_root is not None and our_root >= 0)
        root_agree = committed and (our_root == dcml_r.root_pc)
        rn_agree = pair.category in ("exact", "partial")
        # key respect (global identity)
        otc, omaj = crn._our_key_tonic(getattr(our_r, "key", None))
        gtc, gmaj = crn._dcml_key_tonic(getattr(dcml_r, "global_key", None))
        if otc is None:
            key_verdict = "keyfail"
        elif gtc is None:
            key_verdict = "dcml_keyfail"
        elif (otc, omaj) == (gtc, gmaj):
            key_verdict = "agree"
        else:
            key_verdict = "disagree"
        # abstain-aware two-tier root bucket
        if root_agree:
            rbucket = "agree"
            cls = None
        elif not committed:
            rbucket = "coverage_loss"      # abstain where a decidable answer was owed
            cls = None
        else:
            cls = a8.cell_class(our_r)      # committed wrong: class (a) or (b)
            rbucket = "wrong_a" if cls == "a" else "wrong_b"
        cells.append({
            "stem": stem, "t0": t0, "t1": t1, "w": w,
            "our_root": our_root if our_root is not None else -1,
            "dcml_root": dcml_r.root_pc,
            "our_sym": our_r.chord_symbol, "dcml_sym": dcml_r.chord_symbol,
            "our_q": our_r.quality, "committed": committed,
            "root_agree": root_agree, "rn_agree": rn_agree,
            "key_verdict": key_verdict, "rbucket": rbucket, "cls": cls,
        })
    # a8 faithfulness self-validation (variant-b bucket decomposition) — ONLY valid in
    # own-anchor mode (grid_score_regions re-derives spans from THIS arm's own regions).
    if ref_spans is None:
        oracle = crn.grid_score_regions(ours_regions, wir_regions)
        if dict(bucket_dur) != dict(oracle.bucket_dur) or scored_dur != oracle.scored_dur:
            raise AssertionError(
                f"{stem}: cell loop diverges from grid_score_regions "
                f"(mine={dict(bucket_dur)} scored={scored_dur} vs "
                f"oracle={dict(oracle.bucket_dur)} scored={oracle.scored_dur})")
    return cells, dcml_spans, scored_dur, unscored_dur


def compute_ref_spans(corpus_dir: Path):
    """Per-stem DCML tick spans derived from THIS arm's regions — the common anchoring
    used to grade both arms coverage-equal (Task 1.5 / P4(c))."""
    out = {}
    for ours_path in sorted(corpus_dir.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours", "")
        try:
            _, ours = cmp.load_analysis(ours_path)
        except Exception:
            continue
        if not ours:
            continue
        wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
        if not wir_path:
            continue
        try:
            wir = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not wir:
            continue
        out[stem] = cmp._dcml_time_spans(ours, wir)
    return out


def grade_arm(corpus_dir: Path, label: str, ref_spans_by_stem=None):
    """Grade one arm (a manifest-stamped corpus dir). Returns a dict of aggregates +
    per-piece coverage + the class-(b)/(a) wrong-commit runs + all cells.

    ref_spans_by_stem: None => own-anchor (a8-native, self-validated). A dict => the
    common-anchoring mode (identical DCML tick spans for both arms)."""
    cbf.validate_corpus_dir(corpus_dir)   # manifest / no-contamination gate (raises on fail)
    ours_files = sorted(corpus_dir.glob("*.ours.json"))
    agg = Counter()
    per_piece = {}     # stem -> {scored_dur, unscored_dur, dcml_spans, covered_dcml_idx}
    b_wrong_cells = []  # (stem, cell) committed-wrong class-(b)
    a_wrong_cells = []  # committed-wrong class-(a)
    all_cells = []
    wir_covered = 0
    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
        except Exception:
            continue
        if not ours_regions:
            continue
        wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
        if not wir_path:
            continue
        try:
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not wir_regions:
            continue
        wir_covered += 1
        ref = ref_spans_by_stem.get(stem) if ref_spans_by_stem is not None else None
        if ref_spans_by_stem is not None and ref is None:
            continue   # no common anchor for this stem (should not happen; skip safely)
        cells, dcml_spans, scored, unscored = grade_piece(stem, ours_regions, wir_regions, ref_spans=ref)
        agg["scored_dur"] += scored
        agg["unscored_dur"] += unscored
        # committed duration + root/rn/key agreement over COMMITTED cells (E0 §2.1 convention)
        for c in cells:
            all_cells.append(c)
            if c["committed"]:
                agg["committed_dur"] += c["w"]
                if c["root_agree"]:
                    agg["c_root_agree_dur"] += c["w"]
                if c["rn_agree"]:
                    agg["c_rn_agree_dur"] += c["w"]
                if c["key_verdict"] == "agree":
                    agg["c_key_agree_dur"] += c["w"]
                elif c["key_verdict"] == "keyfail":
                    agg["c_key_fail_dur"] += c["w"]
                if c["rbucket"] == "wrong_b":
                    agg["b_cls_b_dur"] += c["w"]; agg["b_cls_b_cells"] += 1
                    b_wrong_cells.append((stem, c))
                elif c["rbucket"] == "wrong_a":
                    agg["b_cls_a_dur"] += c["w"]; agg["b_cls_a_cells"] += 1
                    a_wrong_cells.append((stem, c))
            else:
                if c["rbucket"] == "coverage_loss":
                    agg["coverage_loss_dur"] += c["w"]; agg["coverage_loss_cells"] += 1
        # per-piece coverage: the DCML span list + total DCML-covered scored duration
        dcml_covered_dur = sum(c["w"] for c in cells)   # every scored cell overlaps a DCML span by construction
        per_piece[stem] = {
            "scored_dur": scored, "unscored_dur": unscored,
            "dcml_spans": [(s, e) for (s, e) in dcml_spans if s >= 0 and e > s],
            "dcml_covered_dur": dcml_covered_dur,
            "n_cells": len(cells),
        }
    b_runs = merge_runs(b_wrong_cells)
    a_runs = merge_runs(a_wrong_cells)
    return {
        "label": label, "corpus_dir": str(corpus_dir), "wir_covered": wir_covered,
        "agg": dict(agg), "per_piece": per_piece,
        "b_runs": b_runs, "a_runs": a_runs,
        "b_wrong_cells": b_wrong_cells, "all_cells": all_cells,
    }


def _accumulate(cell, agg, b_wrong, a_wrong, all_cells):
    all_cells.append(cell)
    if cell["committed"]:
        agg["committed_dur"] += cell["w"]
        if cell["root_agree"]:
            agg["c_root_agree_dur"] += cell["w"]
        if cell["rn_agree"]:
            agg["c_rn_agree_dur"] += cell["w"]
        if cell["key_verdict"] == "agree":
            agg["c_key_agree_dur"] += cell["w"]
        elif cell["key_verdict"] == "keyfail":
            agg["c_key_fail_dur"] += cell["w"]
        if cell["rbucket"] == "wrong_b":
            agg["b_cls_b_dur"] += cell["w"]; agg["b_cls_b_cells"] += 1
            b_wrong.append((cell["stem"], cell))
        elif cell["rbucket"] == "wrong_a":
            agg["b_cls_a_dur"] += cell["w"]; agg["b_cls_a_cells"] += 1
            a_wrong.append((cell["stem"], cell))
    elif cell["rbucket"] == "coverage_loss":
        agg["coverage_loss_dur"] += cell["w"]; agg["coverage_loss_cells"] += 1


def _classify_cell(stem, t0, t1, our_r, dcml_r):
    """Build one abstain-aware cell for arm `our_r` against DCML `dcml_r`. Returns None
    if the pair is unscorable (dcml root None) — the caller skips it for BOTH arms."""
    pair = crn.classify_pair(our_r, dcml_r)
    if pair is None:
        return None
    our_root = our_r.root_pc
    committed = (our_root is not None and our_root >= 0)
    root_agree = committed and (our_root == dcml_r.root_pc)
    otc, omaj = crn._our_key_tonic(getattr(our_r, "key", None))
    gtc, gmaj = crn._dcml_key_tonic(getattr(dcml_r, "global_key", None))
    if otc is None:
        key_verdict = "keyfail"
    elif gtc is None:
        key_verdict = "dcml_keyfail"
    elif (otc, omaj) == (gtc, gmaj):
        key_verdict = "agree"
    else:
        key_verdict = "disagree"
    if root_agree:
        rbucket, cls = "agree", None
    elif not committed:
        rbucket, cls = "coverage_loss", None
    else:
        cls = a8.cell_class(our_r)
        rbucket = "wrong_a" if cls == "a" else "wrong_b"
    return {"stem": stem, "t0": t0, "t1": t1, "w": t1 - t0,
            "our_root": our_root if our_root is not None else -1, "dcml_root": dcml_r.root_pc,
            "our_sym": our_r.chord_symbol, "dcml_sym": dcml_r.chord_symbol, "our_q": our_r.quality,
            "committed": committed, "root_agree": root_agree,
            "rn_agree": pair.category in ("exact", "partial"),
            "key_verdict": key_verdict, "rbucket": rbucket, "cls": cls}


def grade_both_intersect(reb_dir: Path, leg_dir: Path, ref_spans_by_stem):
    """Grade BOTH arms on EXACTLY the same scored cells: a tick is scored iff BOTH arms
    have a region there AND the common DCML span covers it (the intersection of ours
    coverage ∩ DCML coverage). This makes scored coverage byte-exactly equal between the
    arms (Task 1.5 / P4(c)), so the class-(b) delta is confound-free. ref_spans_by_stem
    supplies the common DCML anchoring (rebuilt/fine by default)."""
    cbf.validate_corpus_dir(reb_dir); cbf.validate_corpus_dir(leg_dir)
    reb_agg, leg_agg = Counter(), Counter()
    reb_b, reb_a, leg_b, leg_a = [], [], [], []
    reb_cells, leg_cells = [], []
    reb_pp, leg_pp = {}, {}
    wir_covered = 0
    stems = sorted({p.stem.replace(".ours", "") for p in reb_dir.glob("*.ours.json")} &
                   {p.stem.replace(".ours", "") for p in leg_dir.glob("*.ours.json")})
    for stem in stems:
        wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
        if not wir_path:
            continue
        try:
            wir = dcml.parse_rntxt_file(wir_path)
            _, reb_reg = cmp.load_analysis(reb_dir / f"{stem}.ours.json")
            _, leg_reg = cmp.load_analysis(leg_dir / f"{stem}.ours.json")
        except Exception:
            continue
        if not wir or not reb_reg or not leg_reg:
            continue
        ref = ref_spans_by_stem.get(stem)
        if ref is None:
            continue
        wir_covered += 1
        reb_os = [(r.start_tick, r.end_tick) for r in reb_reg]
        leg_os = [(r.start_tick, r.end_tick) for r in leg_reg]
        bounds = set()
        for spans in (reb_os, leg_os, ref):
            for (s, e) in spans:
                if s >= 0 and e > s:
                    bounds.add(s); bounds.add(e)
        grid = sorted(bounds)
        pscored = 0
        for i in range(len(grid) - 1):
            t0, t1 = grid[i], grid[i + 1]
            if t1 <= t0:
                continue
            ri = crn._active_index_at(reb_os, t0)
            li = crn._active_index_at(leg_os, t0)
            di = crn._active_index_at(ref, t0)
            if ri is None or li is None or di is None:
                continue                                  # not in the ours∩ours∩DCML intersection
            dcml_r = wir[di]
            rc = _classify_cell(stem, t0, t1, reb_reg[ri], dcml_r)
            lc = _classify_cell(stem, t0, t1, leg_reg[li], dcml_r)
            if rc is None or lc is None:
                continue                                  # dcml root None ⇒ skip for BOTH (stays equal)
            pscored += (t1 - t0)
            _accumulate(rc, reb_agg, reb_b, reb_a, reb_cells)
            _accumulate(lc, leg_agg, leg_b, leg_a, leg_cells)
        reb_pp[stem] = {"scored_dur": pscored, "dcml_spans": ref, "n_cells": 0}
        leg_pp[stem] = {"scored_dur": pscored, "dcml_spans": ref, "n_cells": 0}
        reb_agg["scored_dur"] += pscored
        leg_agg["scored_dur"] += pscored
    def pack(label, agg, bcells, acells, cells, pp):
        return {"label": label, "wir_covered": wir_covered, "agg": dict(agg), "per_piece": pp,
                "b_runs": merge_runs(bcells), "a_runs": merge_runs(acells),
                "b_wrong_cells": bcells, "all_cells": cells}
    return (pack("rebuilt", reb_agg, reb_b, reb_a, reb_cells, reb_pp),
            pack("legacy", leg_agg, leg_b, leg_a, leg_cells, leg_pp))


def coverage_equality(reb, leg):
    """Per-piece DCML covered-span equality between arms (Task 1.5 / P4(c))."""
    stems = sorted(set(reb["per_piece"]) & set(leg["per_piece"]))
    mism = []
    for stem in stems:
        r = reb["per_piece"][stem]; l = leg["per_piece"][stem]
        rs = r["dcml_spans"]; ls = l["dcml_spans"]
        if rs != ls:
            mism.append((stem, "dcml_spans", len(rs), len(ls)))
        elif r["scored_dur"] != l["scored_dur"]:
            mism.append((stem, "scored_dur", r["scored_dur"], l["scored_dur"]))
    only_reb = sorted(set(reb["per_piece"]) - set(leg["per_piece"]))
    only_leg = sorted(set(leg["per_piece"]) - set(reb["per_piece"]))
    return {"n_common": len(stems), "mismatches": mism,
            "only_rebuilt": only_reb, "only_legacy": only_leg}


def pct(n, d):
    return 100.0 * n / d if d else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuilt-root", required=True, help="root holding <root>/<preset>/ fullspine dumps")
    ap.add_argument("--legacy-root", default="tools/corpus", help="root holding legacy <root>/<preset>/")
    ap.add_argument("--preset", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--anchor", choices=["own", "legacy", "rebuilt"], default="rebuilt",
                    help="DCML measure-anchoring for grading. 'own': each arm anchors DCML "
                         "from its own regions (a8-native, self-validated, but cross-arm "
                         "coverage differs — the P4(c) confound). 'legacy'/'rebuilt': a COMMON "
                         "anchoring from that arm's regions grades BOTH arms coverage-equal "
                         "(default 'rebuilt' = the finest/most-accurate DCML positions).")
    ap.add_argument("--intersect", action="store_true",
                    help="Grade both arms on EXACTLY the ours∩ours∩DCML intersection so "
                         "scored coverage is byte-exactly equal (the airtight Task-1.5 mode). "
                         "Uses the --anchor arm's DCML spans as the common anchoring.")
    args = ap.parse_args()
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    reb_dir = Path(args.rebuilt_root) / args.preset
    leg_dir = Path(args.legacy_root) / args.preset

    ref_spans = None
    if args.anchor == "legacy":
        ref_spans = compute_ref_spans(leg_dir)
    elif args.anchor == "rebuilt":
        ref_spans = compute_ref_spans(reb_dir)

    if args.intersect:
        if ref_spans is None:
            ref_spans = compute_ref_spans(reb_dir)   # intersect needs a common anchoring
        reb, leg = grade_both_intersect(reb_dir, leg_dir, ref_spans)
    else:
        reb = grade_arm(reb_dir, "rebuilt", ref_spans_by_stem=ref_spans)
        leg = grade_arm(leg_dir, "legacy", ref_spans_by_stem=ref_spans)

    cov = coverage_equality(reb, leg)

    # class-(b) run set-diff
    def run_key(r):
        return (r["stem"], r["start"])
    reb_runs = {run_key(r): r for r in reb["b_runs"]}
    leg_runs = {run_key(r): r for r in leg["b_runs"]}
    fixed = [leg_runs[k] for k in leg_runs.keys() - reb_runs.keys()]      # legacy-broken, rebuilt-not
    newbroke = [reb_runs[k] for k in reb_runs.keys() - leg_runs.keys()]   # rebuilt-broken, legacy-not

    ra, la = reb["agg"], leg["agg"]
    summary = {
        "preset": args.preset,
        "anchor": args.anchor,
        "rebuilt": {"b_cls_b_dur": ra.get("b_cls_b_dur", 0), "b_cls_b_cells": ra.get("b_cls_b_cells", 0),
                    "b_cls_a_dur": ra.get("b_cls_a_dur", 0), "coverage_loss_dur": ra.get("coverage_loss_dur", 0),
                    "coverage_loss_cells": ra.get("coverage_loss_cells", 0),
                    "committed_dur": ra.get("committed_dur", 0), "scored_dur": ra.get("scored_dur", 0),
                    "root_agree_committed_pct": pct(ra.get("c_root_agree_dur", 0), ra.get("committed_dur", 0)),
                    "rn_agree_committed_pct": pct(ra.get("c_rn_agree_dur", 0), ra.get("committed_dur", 0)),
                    "key_agree_committed_pct": pct(ra.get("c_key_agree_dur", 0), ra.get("committed_dur", 0)),
                    "committed_frac_of_scored": pct(ra.get("committed_dur", 0), ra.get("scored_dur", 0)),
                    "n_b_runs": len(reb["b_runs"])},
        "legacy": {"b_cls_b_dur": la.get("b_cls_b_dur", 0), "b_cls_b_cells": la.get("b_cls_b_cells", 0),
                   "b_cls_a_dur": la.get("b_cls_a_dur", 0), "coverage_loss_dur": la.get("coverage_loss_dur", 0),
                   "committed_dur": la.get("committed_dur", 0), "scored_dur": la.get("scored_dur", 0),
                   "root_agree_committed_pct": pct(la.get("c_root_agree_dur", 0), la.get("committed_dur", 0)),
                   "rn_agree_committed_pct": pct(la.get("c_rn_agree_dur", 0), la.get("committed_dur", 0)),
                   "key_agree_committed_pct": pct(la.get("c_key_agree_dur", 0), la.get("committed_dur", 0)),
                   "committed_frac_of_scored": pct(la.get("committed_dur", 0), la.get("scored_dur", 0)),
                   "n_b_runs": len(leg["b_runs"])},
        "delta_b_cls_b_dur": ra.get("b_cls_b_dur", 0) - la.get("b_cls_b_dur", 0),
        "delta_b_cls_b_pct": pct(ra.get("b_cls_b_dur", 0) - la.get("b_cls_b_dur", 0), la.get("b_cls_b_dur", 0)),
        "coverage_equality": {"n_common": cov["n_common"], "n_mismatch": len(cov["mismatches"]),
                              "only_rebuilt": cov["only_rebuilt"], "only_legacy": cov["only_legacy"]},
        "set_diff": {"n_fixed_by_rebuilt": len(fixed), "n_new_broken_by_rebuilt": len(newbroke)},
    }
    (out / f"{args.preset}_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    # full enumerations
    def dump_runs(path, runs):
        lines = [f"(count={len(runs)}; identity=stem@runStartTick)"]
        for r in sorted(runs, key=lambda r: -r["dur"]):
            lines.append(f"{r['stem']}@{r['start']} [{r['start']},{r['end']}) dur={r['dur']:>6} "
                         f"our={r['our_sym']}({r['our_root']}) -> dcml_root={r['dcml_root']} cls={r['cls']}")
        Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")
    dump_runs(out / f"{args.preset}_fixed_by_rebuilt.txt", fixed)
    dump_runs(out / f"{args.preset}_new_broken_by_rebuilt.txt", newbroke)
    dump_runs(out / f"{args.preset}_rebuilt_classb_runs.txt", reb["b_runs"])
    dump_runs(out / f"{args.preset}_legacy_classb_runs.txt", leg["b_runs"])
    if cov["mismatches"]:
        (out / f"{args.preset}_coverage_mismatch.txt").write_text(
            "\n".join(f"{m[0]} {m[1]} rebuilt={m[2]} legacy={m[3]}" for m in cov["mismatches"]) + "\n",
            encoding="utf-8")

    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
