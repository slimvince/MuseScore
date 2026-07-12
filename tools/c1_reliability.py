#!/usr/bin/env python3
"""c1_reliability.py — Contract §6 C1 reliability instrumentation.

READ-ONLY / MEASUREMENT-ONLY. Measures **reliability** — empirical correctness as a
function of PUBLISHED confidence — per (layer × decision × preset), against human GT,
on the ratified A-8 unit (union-of-boundaries, duration-weighted, variant (b) DCML-only)
for the harmonic rows and on the 16 dev-bed TSV oracle for the phrase/cadence rows.

NOT delivered here: fitted Class-P maps, any squash-constant / θ change, any behaviour
change. Findings are RECORDED for the Stage-5 fitter (contract C1, NOT C2/Stage 5).

ORCHESTRATION ONLY over already-pinned primitives (the cc_stage1d basis). It imports and
REUSES VERBATIM:
  - a8_rebaseline_measure.build_piece_grid   (the ratified A-8 union-of-boundaries cell loop,
                                              self-validated byte-for-byte vs grid_score_regions)
  - a8_rebaseline_measure.WIR_DIR
  - compare_rn._active_index_at              (point membership in a span list)
  - compare_rn.classify_pair / _our_key_tonic / _dcml_key_tonic (via build_piece_grid)
  - compare_analyses.load_analysis / _dcml_time_spans
  - dcml_parser.find_wir_file / parse_rntxt_file / parse_cadence_phrase_markers
  - compare_l6_oracle.match_points / score_cadence / DEV_BEDS / _corpus_pieces / TOLERANCE_TICKS

The measured (layer × decision) rows (contract §3):
  L3 key-of-slice   : sequence margin (squashed) AND emission sigmoid — BOTH; key respect; gate corpus
  L4 chord-of-slice : composite (l4Composite); root respect (+ RN beside); gate corpus fullspine
  L5 fn-of-unit     : combinedBoundary (D-L5a); RN respect;               gate corpus fullspine
  L5 cadence        : vote weight (tonicVote, squashed); DCML cadence ±480; 16 dev beds
  L1.5 boundary     : graded texture strength (max-normalised); DCML phraseend ±480; 16 dev beds

Substrate inputs (generated read-only, standard corpus byte-identical by construction):
  - frozen gate corpus       tools/corpus/{preset}/{stem}.ours.json     (L3 key respect + sigmoid)
  - region-keymargin dumps   {km_dir}/{stem}.keymargin.json             (L3 sequence margin)
  - gate-corpus fullspine     {fs_dir}/{stem}.ours.json                 (L4/L5 + D-FS re-confirm)
  - dev-bed fullspine         tools/corpus_l6_oracle/{corpus}/{stem}.fullspine.json (cadence + L1.5)
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import a8_rebaseline_measure as a8       # noqa: E402  (the ratified A-8 cell loop)
import compare_analyses as cmp           # noqa: E402
import compare_rn as crn                 # noqa: E402
import dcml_parser as dcml               # noqa: E402
import compare_l6_oracle as l6           # noqa: E402
import characterise_bir_false as cbf     # noqa: E402  (validate_corpus_dir — OI-129 anti-contamination guard)

PRESETS = ["baroque", "jazz", "default"]

# ── Declared measurement-time squash maps (contract R5; constants precision-phase) ──
# s(x) = x/(x+k), monotone, [0,inf)->[0,1). RANKING is squash-invariant, so the
# monotonicity finding does NOT depend on k; only the [0,1] bin placement does. These
# are DECLARED here, NOT fitted (fitting is the Stage-5 job this dispatch does NOT do).
SQUASH_K_L3_MARGIN = 1.0    # = KeyModeSequencePreferences.uncertainThreshold (the layer's own bar)
SQUASH_K_CADENCE   = 3.5    # ~ the single-authentic-cadence tonicVote unit (declared; observed below)


def squash(x, k):
    x = max(0.0, float(x))
    return x / (x + k) if (x + k) > 0 else 0.0


# ── The generic reliability binner (10 equal-width bins on [0,1]; no fitting) ──────

def bin_curve(pairs, nbins=10):
    """pairs: iterable of (conf in [0,1], correct in {0.0,1.0}, weight>0).
    Returns per-bin rows with count, weight (=duration or count), duration-weighted
    empirical correctness, and the bin's weighted mean confidence."""
    bins = [dict(n=0, w=0.0, cw=0.0, confw=0.0) for _ in range(nbins)]
    tot_w = 0.0
    for conf, correct, w in pairs:
        c = min(max(conf, 0.0), 1.0)
        idx = min(int(c * nbins), nbins - 1)
        b = bins[idx]
        b["n"] += 1
        b["w"] += w
        b["cw"] += correct * w
        b["confw"] += c * w
        tot_w += w
    rows = []
    for i, b in enumerate(bins):
        emp = (b["cw"] / b["w"]) if b["w"] > 0 else None
        mconf = (b["confw"] / b["w"]) if b["w"] > 0 else None
        rows.append({
            "bin": i, "lo": i / nbins, "hi": (i + 1) / nbins,
            "n": b["n"], "w": b["w"],
            "mass": (b["w"] / tot_w) if tot_w > 0 else 0.0,
            "emp": emp, "mean_conf": mconf,
        })
    return rows, tot_w


def curve_diagnostics(rows, tot_w):
    """monotonicity violations (bins where empirical correctness FALLS as confidence
    rises, over consecutive non-empty bins), the weighted-mean calibration gap
    (ECE-style |emp - mean_conf|), and the confidence-mass distribution."""
    nonempty = [r for r in rows if r["emp"] is not None]
    viol = 0
    viol_bins = []
    prev = None
    for r in nonempty:
        if prev is not None and r["emp"] < prev["emp"] - 1e-9:
            viol += 1
            viol_bins.append((prev["bin"], r["bin"], round(prev["emp"], 3), round(r["emp"], 3)))
        prev = r
    ece = None
    if tot_w > 0:
        ece = sum(r["w"] * abs(r["emp"] - r["mean_conf"]) for r in nonempty) / tot_w
    # over/under-confidence sign: mean(emp - mean_conf) weighted
    signed = None
    if tot_w > 0:
        signed = sum(r["w"] * (r["emp"] - r["mean_conf"]) for r in nonempty) / tot_w
    return {
        "monotonicity_violations": viol,
        "violation_bins": viol_bins,
        "ece": ece,
        "signed_gap": signed,   # >0 underconfident (emp>conf); <0 overconfident
        "nonempty_bins": len(nonempty),
        "overall_correct": (sum(r["w"] * r["emp"] for r in nonempty) / tot_w) if tot_w > 0 else None,
    }


def fmt_curve(title, rows, diag, tot_w, weight_label):
    L = [f"  {title}"]
    L.append(f"    bins(conf)  {'n':>7} {weight_label:>12} {'mass':>6} {'emp.correct':>11} {'mean.conf':>9}")
    for r in rows:
        if r["n"] == 0:
            L.append(f"    [{r['lo']:.1f},{r['hi']:.1f})  {0:>7} {0.0:>12.0f} {'':>6} {'--':>11} {'--':>9}")
            continue
        L.append(f"    [{r['lo']:.1f},{r['hi']:.1f})  {r['n']:>7} {r['w']:>12.0f} "
                 f"{r['mass']:>6.3f} {r['emp']:>11.4f} {r['mean_conf']:>9.4f}")
    L.append(f"    -> overall correct={diag['overall_correct']:.4f}  "
             f"monotonicity_violations={diag['monotonicity_violations']}  "
             f"ECE={diag['ece']:.4f}  signed_gap={diag['signed_gap']:+.4f} "
             f"({'under' if diag['signed_gap'] and diag['signed_gap']>0 else 'over'}-confident)")
    if diag["violation_bins"]:
        L.append(f"    violations: {diag['violation_bins']}")
    return "\n".join(L)


# ── Per-stem cell join: A-8 cells + a per-region confidence lookup ─────────────────

def cells_with_region_conf(stem, ours_regions, wir_regions, m21_regions, conf_by_start):
    """Build the ratified A-8 cell grid (build_piece_grid, self-validated), then attach
    to each cell the confidence of the ACTIVE ours region at the cell start (join by the
    pinned _active_index_at + region.start_tick). Returns the PieceGrid + a parallel list
    of the active region's start tick per cell."""
    pg = a8.build_piece_grid(stem, ours_regions, wir_regions, m21_regions)
    ours_spans = [(r.start_tick, r.end_tick) for r in ours_regions]
    region_start = []
    for c in pg.cells:
        oi = crn._active_index_at(ours_spans, c["t0"])
        region_start.append(ours_regions[oi].start_tick if oi is not None else None)
    return pg, region_start


def _load_wir(stem):
    p = dcml.find_wir_file(str(a8.WIR_DIR), stem)
    if not p:
        return []
    try:
        return dcml.parse_rntxt_file(p)
    except (OSError, ValueError, KeyError, TypeError):
        return []


# ── ROW 1 — L3 key-of-slice (gate corpus): margin AND sigmoid vs A-8 key respect ──

def measure_l3(preset, km_dir):
    corpus_dir = _ROOT / "tools" / "corpus" / preset
    margin_pairs, sigmoid_pairs = [], []
    keyfail_w = 0.0
    stems = 0
    for ours_path in sorted(corpus_dir.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours", "")
        wir = _load_wir(stem)
        if not wir:
            continue
        try:
            _, ours = cmp.load_analysis(ours_path)
        except (OSError, ValueError, KeyError, TypeError):
            continue
        if not ours:
            continue
        m21_path = corpus_dir / f"{stem}.music21.json"
        m21 = []
        if m21_path.exists():
            try:
                _, m21 = cmp.load_analysis(m21_path)
            except (OSError, ValueError, KeyError, TypeError):
                m21 = []
        km_path = Path(km_dir) / f"{stem}.keymargin.json"
        if not km_path.exists():
            continue
        km = json.loads(km_path.read_text(encoding="utf-8"))
        conf_by_start = {r["startTick"]: (r["keySeqMargin"], r["keySigmoid"]) for r in km["regions"]}
        pg, region_start = cells_with_region_conf(stem, ours, wir, m21, conf_by_start)
        stems += 1
        for c, rs in zip(pg.cells, region_start):
            if rs is None or rs not in conf_by_start:
                continue
            kv = c["key_verdict"]
            if kv in ("keyfail", "dcml_keyfail"):
                keyfail_w += c["w"]
                continue
            correct = 1.0 if kv == "agree" else 0.0
            margin, sigmoid = conf_by_start[rs]
            margin_pairs.append((squash(margin, SQUASH_K_L3_MARGIN), correct, c["w"]))
            sigmoid_pairs.append((min(max(sigmoid, 0.0), 1.0), correct, c["w"]))
    return {"margin": margin_pairs, "sigmoid": sigmoid_pairs, "keyfail_w": keyfail_w, "stems": stems}


# ── ROWS 2/3 — L4 composite / L5 combinedBoundary (gate fullspine) ────────────────

def measure_l4_l5(preset, fs_dir):
    l4_pairs, l5_pairs = [], []
    stems = 0
    l5_zero_w = 0.0
    total_w = 0.0
    # D-FS re-confirm accumulators
    dfs = {"combinedBoundary": [], "overrideContradiction": [], "cadentialWeight": []}
    for fs_path in sorted(Path(fs_dir).glob("*.ours.json")):
        stem = fs_path.stem.replace(".ours", "")
        if stem == "corpus_manifest":
            continue
        wir = _load_wir(stem)
        if not wir:
            continue
        try:
            _, ours = cmp.load_analysis(fs_path)
        except (OSError, ValueError, KeyError, TypeError):
            continue
        if not ours:
            continue
        m21_path = (_ROOT / "tools" / "corpus" / preset / f"{stem}.music21.json")
        m21 = []
        if m21_path.exists():
            try:
                _, m21 = cmp.load_analysis(m21_path)
            except (OSError, ValueError, KeyError, TypeError):
                m21 = []
        raw = json.loads(fs_path.read_text(encoding="utf-8"))
        conf_by_start = {r["startTick"]: (r.get("l4Composite", 0.0), r.get("l5CombinedBoundary", 0.0))
                         for r in raw.get("regions", [])}
        # D-FS ranges (F-A/F-B contradiction quantities) — re-confirmed this run
        for r in raw.get("regions", []):
            dfs["combinedBoundary"].append(r.get("l5CombinedBoundary", 0.0))
            oc = r.get("l5OverrideContradiction", 0.0)
            if r.get("l5OverrodeCommit"):
                dfs["overrideContradiction"].append(oc)
        for m in raw.get("modulations", []):
            if m.get("isModulation") and m.get("cadenceConfirmed"):
                dfs["cadentialWeight"].append(m.get("cadentialWeight", 0.0))
        pg, region_start = cells_with_region_conf(stem, ours, wir, m21, conf_by_start)
        stems += 1
        for c, rs in zip(pg.cells, region_start):
            if rs is None or rs not in conf_by_start:
                continue
            comp, cb = conf_by_start[rs]
            l4_pairs.append((min(max(comp, 0.0), 1.0), 1.0 if c["root_agree"] else 0.0, c["w"]))
            l5_pairs.append((min(max(cb, 0.0), 1.0), 1.0 if c["rn_agree"] else 0.0, c["w"]))
            total_w += c["w"]
            if cb <= 0.0:
                l5_zero_w += c["w"]
    return {"l4": l4_pairs, "l5": l5_pairs, "stems": stems,
            "l5_zero_frac": (l5_zero_w / total_w) if total_w else 0.0, "dfs": dfs}


# ── ROW 4 — L5 cadence detection (dev beds): tonicVote vs DCML cadence ±480 ────────
# ── ROW 5 — L1.5 boundary-at-tick (dev beds): texture strength vs DCML phraseend ─

def measure_devbeds(l6_root):
    cad_pairs, l15_pairs = [], []
    all_votes = []
    cad_movements = l15_movements = 0
    for corpus in l6.DEV_BEDS:
        cdir = Path(l6_root) / corpus
        if not cdir.is_dir():
            continue
        for stem, mscx, tsv in l6._corpus_pieces(corpus):
            fj = cdir / f"{stem}.fullspine.json"
            if not fj.exists():
                continue
            try:
                fs = json.loads(fj.read_text(encoding="utf-8"))
            except (OSError, ValueError, KeyError, TypeError):
                continue
            # ROW 4 — cadence: reuse l6.score_cadence's matcher to know which OUR
            # cadences matched a GT cadence (±480), then bin each by tonicVote.
            cad_mk, phr_mk = dcml.parse_cadence_phrase_markers(str(tsv))
            gt_cad = sorted(set(m.abs_tick for m in cad_mk if m.abs_tick is not None))
            our_cads = fs.get("cadences", [])
            our_ticks = sorted(set(int(c["arrivalTick"]) for c in our_cads))
            if gt_cad and our_cads:
                m = l6.match_points(our_ticks, gt_cad)
                matched_our = set(p[0] for p in m.pairs)
                for c in our_cads:
                    t = int(c["arrivalTick"])
                    vote = float(c.get("tonicVote", 0.0))
                    all_votes.append(vote)
                    correct = 1.0 if t in matched_our else 0.0
                    cad_pairs.append((squash(vote, SQUASH_K_CADENCE), correct, 1.0))
                cad_movements += 1
            # ROW 5 — L1.5: every texture tick, strength max-normalised per profile,
            # correct iff within ±480 of a GT phraseend marker.
            tt = fs.get("phraseTextureTicks", [])
            ts = fs.get("phraseTextureStrength", [])
            gt_phr = sorted(set(m.abs_tick for m in phr_mk if m.abs_tick is not None))
            if tt and ts and len(tt) == len(ts) and gt_phr:
                mx = max(ts)
                if mx > 0:
                    tol = l6.TOLERANCE_TICKS
                    gt_sorted = gt_phr
                    for tick, s in zip(tt, ts):
                        norm = s / mx
                        near = any(abs(tick - g) <= tol for g in gt_sorted)
                        l15_pairs.append((min(max(norm, 0.0), 1.0), 1.0 if near else 0.0, 1.0))
                    l15_movements += 1
    return {"cadence": cad_pairs, "l15": l15_pairs, "votes": all_votes,
            "cad_movements": cad_movements, "l15_movements": l15_movements}


def _range(xs):
    if not xs:
        return "n=0"
    return f"n={len(xs)} min={min(xs):.4f} med={statistics.median(xs):.4f} max={max(xs):.4f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--km-root", default="C:/tmp/c1", help="dir holding km_{preset}/ region-keymargin dumps")
    ap.add_argument("--fs-root", default="C:/tmp/c1", help="dir holding fs_{preset}/ gate fullspine dumps")
    ap.add_argument("--l6-root", default=str(_ROOT / "tools" / "corpus_l6_oracle"),
                    help="dir holding {corpus}/{stem}.fullspine.json dev-bed dumps")
    ap.add_argument("--out", default="", help="write the full report JSON here")
    args = ap.parse_args()

    report = {"presets": {}, "squash": {"l3_margin_k": SQUASH_K_L3_MARGIN, "cadence_k": SQUASH_K_CADENCE},
              "dev_beds": {}}
    out_lines = []

    def emit(s=""):
        print(s)
        out_lines.append(s)

    emit("=" * 78)
    emit("C1 RELIABILITY — curves per (layer × decision × preset) on the ratified A-8 unit")
    emit("Read-only. No fitted maps, no θ change, no behaviour change. Findings recorded.")
    emit("=" * 78)

    # ── Harmonic rows (per preset) ──
    for preset in PRESETS:
        emit(f"\n########## PRESET = {preset} ##########")
        # OI-129: the harmonic reliability curves are measured off tools/corpus/{preset}; route the
        # read through the anti-contamination guard (manifest present, complete, .ours.json AND
        # .music21.json fingerprints match — OI-124) before measuring. (The km/fs scratch substrate
        # has no manifest — OI-129's second half; tracked, not closed here.)
        cbf.validate_corpus_dir(_ROOT / "tools" / "corpus" / preset)
        pr = {}
        # L3
        l3 = measure_l3(preset, Path(args.km_root) / f"km_{preset}")
        for name, pairs in (("L3 key — SEQUENCE MARGIN (squashed x/(x+%.1f))" % SQUASH_K_L3_MARGIN, l3["margin"]),
                            ("L3 key — EMISSION SIGMOID (native [0,1])", l3["sigmoid"])):
            rows, tw = bin_curve(pairs)
            diag = curve_diagnostics(rows, tw)
            emit(fmt_curve(name + "  [correctness = A-8 key respect]", rows, diag, tw, "dur(ticks)"))
            pr[name] = {"rows": rows, "diag": diag, "tot_w": tw}
        emit(f"    (L3 stems={l3['stems']}, key-parse-fail duration excluded={l3['keyfail_w']:.0f} ticks)")
        # L4 / L5
        ll = measure_l4_l5(preset, Path(args.fs_root) / f"fs_{preset}")
        for name, pairs, corr in (
                ("L4 chord — COMPOSITE (native [0,1])  [correctness = A-8 root respect]", ll["l4"], "root"),
                ("L5 fn — combinedBoundary (D-L5a [0,1))  [correctness = A-8 RN respect]", ll["l5"], "rn")):
            rows, tw = bin_curve(pairs)
            diag = curve_diagnostics(rows, tw)
            emit(fmt_curve(name, rows, diag, tw, "dur(ticks)"))
            pr[name] = {"rows": rows, "diag": diag, "tot_w": tw}
        emit(f"    (L4/L5 stems={ll['stems']}, L5 combinedBoundary==0 duration fraction={ll['l5_zero_frac']:.3f})")
        # D-FS re-confirm
        dfs = ll["dfs"]
        emit(f"    D-FS re-confirm (this run): l5CombinedBoundary {_range(dfs['combinedBoundary'])}")
        emit(f"                                F-B override contradiction (bestPlaus-committedPlaus) {_range(dfs['overrideContradiction'])}")
        emit(f"                                F-A cadentialWeight (confirmed modulations) {_range(dfs['cadentialWeight'])}")
        pr["dfs_ranges"] = {k: (_range(v)) for k, v in dfs.items()}
        report["presets"][preset] = {
            k: {"rows": v["rows"], "diag": v["diag"], "tot_w": v["tot_w"]}
            for k, v in pr.items() if isinstance(v, dict) and "rows" in v}
        report["presets"][preset]["dfs_ranges"] = pr["dfs_ranges"]
        report["presets"][preset]["l5_zero_frac"] = ll["l5_zero_frac"]

    # ── Dev-bed rows (preset-independent; the dormant chain runs one preset per dump) ──
    emit(f"\n########## DEV BEDS (16; L5 cadence + L1.5 boundary) ##########")
    db = measure_devbeds(args.l6_root)
    emit(f"    cadence movements={db['cad_movements']}  tonicVote {_range(db['votes'])}  (squash k={SQUASH_K_CADENCE})")
    for name, pairs, wl in (
            ("L5 CADENCE — tonicVote (squashed)  [correctness = matched DCML cadence ±480]", db["cadence"], "count"),
            ("L1.5 BOUNDARY — texture strength (max-norm)  [correct = within ±480 of DCML phraseend]", db["l15"], "count")):
        rows, tw = bin_curve(pairs)
        diag = curve_diagnostics(rows, tw)
        emit(fmt_curve(name, rows, diag, tw, wl))
        report["dev_beds"][name] = {"rows": rows, "diag": diag, "tot_w": tw}
    report["dev_beds"]["cad_movements"] = db["cad_movements"]
    report["dev_beds"]["l15_movements"] = db["l15_movements"]

    if args.out:
        Path(args.out).write_text(json.dumps(report, indent=1), encoding="utf-8")
        emit(f"\n[wrote {args.out}]")


if __name__ == "__main__":
    main()
