#!/usr/bin/env python3
"""gen_wir_alignment_probe.py — the OI-184 WiR anacrusis-alignment establishment probe.

READ-ONLY / MEASURE-ONLY. No src/ change, no corpus mutation, no gate change, no value
fitted, NO decision made, NO re-baseline, NO alignment "fix". This instrument answers the
OI-184 establishment question POSITIVELY, either way (#19): what convention maps a WiR
`(measure, beat)` chorale annotation to OUR tick grid, and is it correct on anacrusis-bearing
pieces? If a systematic offset is found it is a FINDING for Cowork/user disposition (an
alignment correction would move the ratified grading columns — a ratified re-baseline event of
its own, the OI-142 pattern — NOT started here).

Dispatch: `cc_instruction_wir_alignment_probe.md` (Cowork 2026-07-19). Register row OI-184;
source finding `cowork_factorization_desk_simulation.md` §4.5.

ORCHESTRATION ONLY over already-pinned functions (the cc_stage1d "orchestration is not a metric
definition" basis). It imports and reuses verbatim — modifying NONE of them (the dispatch's hard
stop):
  - a8_rebaseline_measure.build_piece_grid  (the pinned root-respect grid; the OFFSET-0 ORACLE —
                                             self-validates its variant-(b) buckets against
                                             compare_rn.grid_score_regions on every piece)
  - a8_rebaseline_measure.measure_preset coverage logic (mirrored, not called — same skip
                                             conditions, same order, so wir_covered reproduces 326)
  - compare_analyses._dcml_time_spans        (the ONE (measure,beat)->tick span primitive)
  - compare_analyses.load_analysis / roots_agree
  - compare_analyses._infer_ticks_per_beat / _build_measure_anchors / _derive_ticks_per_measure
                                             (used ONLY to corroborate the anacrusis flag, read-only)
  - compare_rn.classify_pair / _active_index_at   (the per-cell scoreability + membership)
  - characterise_bir_false.validate_corpus_dir    (manifest / no-contamination gate)
  - dcml_parser.find_wir_file / load_wir_regions  (the OI-142-corrected WiR substrate)

THE OFFSET SWEEP. For each covered stem the DCML-side tick spans (produced by the pinned
_dcml_time_spans) are translated by a GLOBAL candidate offset in {-960,-480,0,+480,+960} ticks and
the duration-weighted root-agreement is recomputed on the union-of-boundaries grid. A translation
is a pure constant shift of the GT stream's already-resolved spans; the OURS side and the
measure->tick anchoring (which comes from OUR regions) are untouched. Root-agreement is the
established alignment signal (block (A)); a systematically better nonzero offset means the mapping,
not the analysis, is off.

ESTABLISHMENT (#19). Two locks, both mechanical, both fail as a STOP:
  (1) PER-PIECE: at offset 0 the probe's (agree, scored) durations must equal
      build_piece_grid's on every covered stem (the probe reuses the pinned metric, it does not
      redefine it). Asserted per piece.
  (2) AGGREGATE: at offset 0 the summed (agree, scored) must equal the COMMITTED block-(A)
      Default reference, read (not hand-typed, #17f) from tools/robust_stop/summary.json. A
      discrepancy means the probe is mis-built — STOP.
Plus byte-reproducibility: the artifact is deterministic (sorted stems, fixed offset order, no
timestamp/random) and reproduces on a second run.

Usage:
    python tools/joint_estimator/gen_wir_alignment_probe.py
    python tools/joint_estimator/gen_wir_alignment_probe.py --out-json <p> --out-summary <p>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import a8_rebaseline_measure as arb      # noqa: E402  (offset-0 oracle + coverage logic)
import compare_analyses as cmp           # noqa: E402
import compare_rn as crn                 # noqa: E402
import characterise_bir_false as cbf     # noqa: E402
import dcml_parser as dcml               # noqa: E402

WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")
CORPUS_DIR = _ROOT / "tools" / "corpus" / "default"   # Default corpus (block (A) Default = 65.93 %)
A8_SUMMARY = _ROOT / "tools" / "robust_stop" / "summary.json"
OFFSETS_FILE = _ROOT / "tools" / "robust_stop" / "corpus_transposition_offsets.json"

OFFSETS = [-960, -480, 0, 480, 960]      # candidate GLOBAL tick offsets of the GT stream
HIGH_MARGIN_PP = 2.0                      # dispatch item 3: margin over offset 0 exceeding 2 %


def _git_head() -> str:
    out = subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                         capture_output=True, text=True, check=True)
    return out.stdout.strip()


def _sha256_file(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


# ── the offset-shifted root scorer (offset 0 provably == build_piece_grid) ───

def root_score_at_offset(ours_regions, wir_regions, ours_spans, base_dcml_spans, off):
    """Duration-weighted root agreement with the GT stream translated by `off` ticks.

    Reuses the pinned per-cell verdict (crn.classify_pair) and membership (crn._active_index_at)
    and the ONE root-equality decision (cmp.roots_agree, OI-52). At off=0 the shifted spans equal
    the base spans and this loop is byte-identical in outcome to a8_rebaseline_measure.build_piece_grid's
    root respect (asserted per piece by the caller). Returns (agree_dur, scored_dur)."""
    # Shift only the RESOLVED spans; the (-1,-1) unresolved sentinel stays unresolved. A resolved
    # span that shifts negative keeps e>s and is still scored (harmless: no OURS span covers
    # negative ticks, so such cells drop out as oi=None) — this matches build_piece_grid's guard at
    # off=0 exactly, where resolved <=> (s>=0 and e>s).
    dspans = [(s + off, e + off) if (s >= 0 and e > s) else (-1, -1) for (s, e) in base_dcml_spans]
    bounds = set()
    for (s, e) in ours_spans:
        if e > s:
            bounds.add(s); bounds.add(e)
    for (s, e) in dspans:
        if e > s:
            bounds.add(s); bounds.add(e)
    if len(bounds) < 2:
        return (0, 0)
    grid = sorted(bounds)
    agree = 0
    scored = 0
    for i in range(len(grid) - 1):
        t0, t1 = grid[i], grid[i + 1]
        w = t1 - t0
        if w <= 0:
            continue
        oi = crn._active_index_at(ours_spans, t0)
        di = crn._active_index_at(dspans, t0)
        if oi is None or di is None:
            continue
        pair = crn.classify_pair(ours_regions[oi], wir_regions[di])
        if pair is None:
            continue
        scored += w
        if cmp.roots_agree(ours_regions[oi].root_pc, wir_regions[di].root_pc):
            agree += w
    return (agree, scored)


def build_piece_grid_root(stem, ours_regions, wir_regions):
    """The offset-0 ORACLE: the pinned build_piece_grid (which self-validates against
    grid_score_regions), reduced to (agree_dur, scored_dur) on the root respect."""
    pg = arb.build_piece_grid(stem, ours_regions, wir_regions, [])   # m21 not needed for root
    agree = sum(c["w"] for c in pg.cells if c["root_agree"])
    return (agree, pg.scored_dur)


# ── anacrusis classification (flag + cheap measure-tick corroboration) ───────

def anacrusis_facts(ours_regions, wir_regions):
    """Return the anacrusis facts for one piece: the pickup flag from OUR first measure, the
    WiR-m0 flag, and a cheap measure-tick corroboration of the pickup (read-only)."""
    ours_min_m = min(r.measure_number for r in ours_regions)
    wir_min_m = min(r.measure_number for r in wir_regions)
    ours_pickup = (ours_min_m == 0)
    wir_m0 = (wir_min_m == 0)

    # cheap corroboration: measure 0's own length vs the piece's derived measure length.
    tpb = cmp._infer_ticks_per_beat(ours_regions)
    measure_starts = cmp._build_measure_anchors(ours_regions, tpb)
    derived_mlen = cmp._derive_ticks_per_measure(measure_starts)
    m0_len = None
    corroborates = None
    if 0 in measure_starts and 1 in measure_starts:
        m0_len = measure_starts[1] - measure_starts[0]
    if m0_len is not None and derived_mlen:
        # a genuine pickup measure is materially shorter than a full measure
        corroborates = bool(m0_len < 0.9 * derived_mlen)
    return {
        "ours_min_measure": ours_min_m,
        "wir_min_measure": wir_min_m,
        "ours_pickup": ours_pickup,
        "wir_m0": wir_m0,
        "class": _contingency_class(ours_pickup, wir_m0),
        "m0_span_ticks": (int(m0_len) if m0_len is not None else None),
        "derived_measure_ticks": (round(derived_mlen, 1) if derived_mlen else None),
        "pickup_length_corroborates": corroborates,
    }


def _contingency_class(ours_pickup, wir_m0):
    if ours_pickup and wir_m0:
        return "both"
    if ours_pickup and not wir_m0:
        return "ours_pickup_only"
    if wir_m0 and not ours_pickup:
        return "wir_m0_only"
    return "neither"


def pickup_mapping_facts(ours_regions, wir_regions):
    """The SHARPEST form of the OI-184 question, which the global-offset sweep MASKS: does the
    WiR m0 (pickup) chord land ON our pickup region, or is it displaced by the measure-anchor
    arithmetic? Returns None when either side lacks an m0 (not an anacrusis-mapping case).

    A single short pickup region is duration-negligible against the body, so a per-piece
    displacement does NOT move the global offset — it must be measured on its own. Read-only:
    reuses the same _dcml_time_spans mapping the grading uses."""
    ours_m0 = [r for r in ours_regions if r.measure_number == 0]
    wir_m0 = [r for r in wir_regions if r.measure_number == 0]
    if not ours_m0 or not wir_m0:
        return None
    o_start = min(r.start_tick for r in ours_m0)
    o_end = max(r.end_tick for r in ours_m0)
    spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    m0_mapped = [(r, s) for r, (s, e) in zip(wir_regions, spans)
                 if r.measure_number == 0 and s >= 0]
    if not m0_mapped:
        return None
    first_r, first_s = min(m0_mapped, key=lambda rs: rs[1])
    if o_start <= first_s < o_end:
        rel = "inside"          # WiR pickup chord lands on our pickup region — aligned
    elif first_s >= o_end:
        rel = "overshoot"       # placed AFTER our pickup region (the beat-renumber displacement)
    else:
        rel = "before"          # placed before our pickup region
    return {
        "ours_pickup_span": [o_start, o_end],
        "wir_m0_first_beat": first_r.beat,
        "wir_m0_first_mapped_tick": first_s,
        "displacement_ticks": first_s - o_start,
        "relation": rel,
    }


# ── per-piece argmax / margin over the offset sweep ──────────────────────────

def _pct(agree, scored):
    return round(100.0 * agree / scored, 4) if scored else None


def piece_offset_profile(ours_regions, wir_regions):
    """Compute (agree, scored, pct) for every candidate offset, and the argmax + margin over
    offset 0. Returns the per-offset dict plus argmax facts."""
    ours_spans = [(r.start_tick, r.end_tick) for r in ours_regions]
    base_dcml_spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    per_offset = {}
    for off in OFFSETS:
        agree, scored = root_score_at_offset(ours_regions, wir_regions,
                                             ours_spans, base_dcml_spans, off)
        per_offset[str(off)] = {"agree": agree, "scored": scored, "pct": _pct(agree, scored)}

    # argmax over offsets with a defined pct; tie-break toward the smallest |offset| (conservative:
    # only a strict win over the zero-shift is evidence of a convention error).
    defined = [(off, per_offset[str(off)]["pct"]) for off in OFFSETS
               if per_offset[str(off)]["pct"] is not None]
    argmax_off = None
    argmax_pct = None
    if defined:
        best = max(p for _, p in defined)
        cands = sorted((off for off, p in defined if p == best), key=lambda o: (abs(o), o))
        argmax_off = cands[0]
        argmax_pct = best
    pct0 = per_offset["0"]["pct"]
    margin_pp = (round(argmax_pct - pct0, 4)
                 if (argmax_pct is not None and pct0 is not None) else None)
    return per_offset, argmax_off, argmax_pct, margin_pp


# ── the covered-stem iteration (mirrors a8 measure_preset skip conditions) ───

def iter_covered_stems():
    """Yield (stem, ours_regions, wir_regions) for each covered stem, applying the SAME coverage
    filter as a8_rebaseline_measure.measure_preset (same skip order), so wir_covered == 326."""
    cbf.validate_corpus_dir(CORPUS_DIR)   # manifest / no-contamination gate (raises on fail)
    coverage = {"total_ours_files": 0, "wir_covered": 0,
                "no_annotation": 0, "wir_parse_fail": 0,
                "ours_load_fail": 0, "empty_ours": 0}
    src_hasher = hashlib.sha256()
    for ours_path in sorted(CORPUS_DIR.glob("*.ours.json")):
        coverage["total_ours_files"] += 1
        stem = ours_path.stem.replace(".ours", "")
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
        except (OSError, ValueError, KeyError, TypeError):
            coverage["ours_load_fail"] += 1
            continue
        if not ours_regions:
            coverage["empty_ours"] += 1
            continue
        wir_path = dcml.find_wir_file(WIR_DIR, stem)
        if wir_path is None:
            coverage["no_annotation"] += 1
            continue
        try:
            wir_regions = dcml.load_wir_regions(WIR_DIR, stem)
        except Exception:
            coverage["wir_parse_fail"] += 1
            continue
        if not wir_regions:
            coverage["wir_parse_fail"] += 1
            continue
        coverage["wir_covered"] += 1
        try:
            wb = Path(wir_path).read_bytes()
        except OSError:
            wb = b""
        src_hasher.update(stem.encode("utf-8") + b"\0" + hashlib.sha256(wb).digest())
        yield stem, ours_regions, wir_regions
    coverage["wir_source_sha256"] = src_hasher.hexdigest()
    iter_covered_stems.coverage = coverage   # stashed for the caller


def measure():
    pieces = []
    agg_agree0 = 0
    agg_scored0 = 0
    oracle_mismatch = []
    for stem, ours_regions, wir_regions in iter_covered_stems():
        facts = anacrusis_facts(ours_regions, wir_regions)
        per_offset, argmax_off, argmax_pct, margin_pp = piece_offset_profile(ours_regions, wir_regions)

        # ── establishment lock (1): offset 0 must equal the pinned build_piece_grid ──
        o_agree, o_scored = build_piece_grid_root(stem, ours_regions, wir_regions)
        p_agree = per_offset["0"]["agree"]
        p_scored = per_offset["0"]["scored"]
        if (o_agree, o_scored) != (p_agree, p_scored):
            oracle_mismatch.append(
                {"stem": stem, "oracle": [o_agree, o_scored], "probe": [p_agree, p_scored]})
        agg_agree0 += o_agree
        agg_scored0 += o_scored

        pieces.append({
            "stem": stem,
            **facts,
            "pickup_mapping": pickup_mapping_facts(ours_regions, wir_regions),
            "per_offset": per_offset,
            "argmax_offset": argmax_off,
            "argmax_pct": argmax_pct,
            "margin_pp": margin_pp,
        })

    pieces.sort(key=lambda p: p["stem"])
    coverage = iter_covered_stems.coverage
    return pieces, coverage, agg_agree0, agg_scored0, oracle_mismatch


# ── aggregation into the artifact ────────────────────────────────────────────

def build_artifact():
    pieces, coverage, agg_agree0, agg_scored0, oracle_mismatch = measure()

    # ── establishment lock (2): reconcile offset-0 aggregate to the committed a8 Default ──
    a8 = json.loads(A8_SUMMARY.read_text(encoding="utf-8"))
    a8_def = a8["default"]["agg"]
    a8_agree = a8_def["b_root_agree"]
    a8_scored = a8_def["scored_dur"]
    reconciles = (agg_agree0 == a8_agree and agg_scored0 == a8_scored)
    if oracle_mismatch:
        raise SystemExit(f"STOP (#13): offset-0 per-piece oracle mismatch on "
                         f"{len(oracle_mismatch)} stem(s): {oracle_mismatch[:3]}")
    if not reconciles:
        raise SystemExit(
            f"STOP (#13): offset-0 aggregate does not reconcile to the committed block-(A) Default. "
            f"probe=(agree={agg_agree0}, scored={agg_scored0}) "
            f"a8=(agree={a8_agree}, scored={a8_scored}). The probe is mis-built.")

    # ── 2x2 anacrusis contingency ──
    cont = Counter(p["class"] for p in pieces)
    mismatched = sorted(p["stem"] for p in pieces if p["ours_pickup"] != p["wir_m0"])
    # cheap-corroboration disagreements (pickup flag vs measure-length) — surfaced as findings
    corrob_disagree = sorted(
        p["stem"] for p in pieces
        if p["ours_pickup"] and p["pickup_length_corroborates"] is False)

    # ── argmax-offset distribution: overall, by contingency class, by pickup ──
    def _dist(subset):
        d = Counter(str(p["argmax_offset"]) for p in subset if p["argmax_offset"] is not None)
        return {str(off): d.get(str(off), 0) for off in OFFSETS}

    by_class = {cls: _dist([p for p in pieces if p["class"] == cls])
                for cls in ("both", "ours_pickup_only", "wir_m0_only", "neither")}
    by_pickup = {
        "ours_pickup": _dist([p for p in pieces if p["ours_pickup"]]),
        "no_ours_pickup": _dist([p for p in pieces if not p["ours_pickup"]]),
    }

    # ── high-margin pieces (candidates for systematic vs local misalignment) ──
    high_margin = sorted(
        ({"stem": p["stem"], "class": p["class"], "argmax_offset": p["argmax_offset"],
          "margin_pp": p["margin_pp"], "per_offset": p["per_offset"]}
         for p in pieces
         if p["margin_pp"] is not None and p["margin_pp"] > HIGH_MARGIN_PP),
        key=lambda r: (-r["margin_pp"], r["stem"]))

    # ── pickup-chord mapping across the anacrusis class (the sharpest form of OI-184) ──
    pm_pieces = [p for p in pieces if p["pickup_mapping"] is not None]
    pm_rel = Counter(p["pickup_mapping"]["relation"] for p in pm_pieces)
    pm_beat = Counter(p["pickup_mapping"]["wir_m0_first_beat"] for p in pm_pieces)
    pm_disp = Counter(p["pickup_mapping"]["displacement_ticks"] for p in pm_pieces)
    pickup_section = {
        "note": ("For pieces where BOTH our score has a pickup (m0) and WiR carries an m0 line, does "
                 "the WiR m0 (pickup) chord land ON our pickup region? A displacement here is the "
                 "beat-numbering mismatch at the anacrusis (our pipeline renumbers the pickup content "
                 "as m0 beat 1; WiR numbers it as its true metric beat, e.g. beat 4 of the incomplete "
                 "bar). It is duration-negligible (one short region per piece) so it does NOT move the "
                 "global offset — hence measured separately. A FINDING for disposition before per-beat "
                 "/ boundary fitting counts are drawn from pickup measures; NOT fixed here."),
        "pieces_with_both_m0": len(pm_pieces),
        "relation_counts": {"inside": pm_rel.get("inside", 0),
                            "overshoot": pm_rel.get("overshoot", 0),
                            "before": pm_rel.get("before", 0)},
        "wir_m0_first_beat_distribution": {str(k): v for k, v in sorted(pm_beat.items())},
        "displacement_ticks_distribution": {str(k): v for k, v in sorted(pm_disp.items())},
    }

    # ── named case: bwv110.7 full profile ──
    named = next((p for p in pieces if p["stem"] == "bwv110.7"), None)

    artifact = {
        "instrument": "tools/joint_estimator/gen_wir_alignment_probe.py",
        "purpose": ("OI-184 WiR anacrusis-alignment establishment probe (read-only, measure-only). "
                    "Whether a systematic nonzero GT-stream offset better aligns the WiR "
                    "(measure,beat) annotations to our tick grid, split by anacrusis class."),
        "provenance": {
            "corpus_git_hash": _git_head(),
            "corpus_dir": "tools/corpus/default",
            "wir_dir": "tools/dcml/when_in_rome",
            "wir_source_sha256": coverage.pop("wir_source_sha256"),
            "transposition_offsets_file": "tools/robust_stop/corpus_transposition_offsets.json",
            "transposition_offsets_sha256": _sha256_file(OFFSETS_FILE),
            "offsets_tested_ticks": OFFSETS,
            "a8_summary_read": "tools/robust_stop/summary.json",
            "pinned_instruments_reused_unmodified": [
                "a8_rebaseline_measure.build_piece_grid",
                "compare_analyses._dcml_time_spans / load_analysis / roots_agree",
                "compare_rn.classify_pair / _active_index_at",
                "characterise_bir_false.validate_corpus_dir",
                "dcml_parser.find_wir_file / load_wir_regions",
            ],
        },
        "coverage": coverage,
        "establishment": {
            "offset0_agree_dur": agg_agree0,
            "offset0_scored_dur": agg_scored0,
            "offset0_root_agree_pct": _pct(agg_agree0, agg_scored0),
            "a8_committed_default_agree_dur": a8_agree,
            "a8_committed_default_scored_dur": a8_scored,
            "reconciles_to_block_A_default": reconciles,
            "per_piece_oracle_matches_build_piece_grid": (len(oracle_mismatch) == 0),
            "note": ("offset-0 aggregate equals the committed block-(A) Default b_root_agree/scored_dur "
                     "exactly (the same computation); and every covered stem's offset-0 (agree,scored) "
                     "equals the pinned build_piece_grid, which self-validates against grid_score_regions."),
        },
        "anacrusis_contingency_2x2": {
            "both": cont.get("both", 0),
            "ours_pickup_only": cont.get("ours_pickup_only", 0),
            "wir_m0_only": cont.get("wir_m0_only", 0),
            "neither": cont.get("neither", 0),
            "total": sum(cont.values()),
            "mismatched_pair_stems": mismatched,
            "pickup_flag_vs_measure_length_disagree_stems": corrob_disagree,
        },
        "argmax_offset_distribution": {
            "overall": _dist(pieces),
            "by_contingency_class": by_class,
            "by_ours_pickup": by_pickup,
        },
        "high_margin_pieces": {
            "threshold_pp": HIGH_MARGIN_PP,
            "count": len(high_margin),
            "pieces": high_margin,
        },
        "pickup_chord_mapping": pickup_section,
        "named_case_bwv110_7": named,
        "pieces": pieces,
    }
    return artifact


# ── summary txt ──────────────────────────────────────────────────────────────

def write_summary(artifact, path: Path):
    L = []
    L.append("=== OI-184 WiR anacrusis-alignment probe — summary ===")
    L.append(f"corpus git_hash: {artifact['provenance']['corpus_git_hash']}")
    cov = artifact["coverage"]
    L.append(f"coverage: {cov['wir_covered']} covered / {cov['total_ours_files']} ours-files "
             f"(no_annotation={cov['no_annotation']}, wir_parse_fail={cov['wir_parse_fail']})")
    est = artifact["establishment"]
    L.append("")
    L.append("-- establishment (#19) --")
    L.append(f"offset-0 aggregate root-agree: {est['offset0_agree_dur']}/{est['offset0_scored_dur']} "
             f"= {est['offset0_root_agree_pct']}%")
    L.append(f"reconciles to committed block-(A) Default "
             f"({est['a8_committed_default_agree_dur']}/{est['a8_committed_default_scored_dur']}): "
             f"{est['reconciles_to_block_A_default']}")
    L.append(f"per-piece offset-0 == pinned build_piece_grid on all covered stems: "
             f"{est['per_piece_oracle_matches_build_piece_grid']}")
    c = artifact["anacrusis_contingency_2x2"]
    L.append("")
    L.append("-- anacrusis 2x2 (ours_pickup x wir_m0) --")
    L.append(f"both={c['both']}  ours_pickup_only={c['ours_pickup_only']}  "
             f"wir_m0_only={c['wir_m0_only']}  neither={c['neither']}  total={c['total']}")
    L.append(f"mismatched pairs ({len(c['mismatched_pair_stems'])}): "
             f"{', '.join(c['mismatched_pair_stems']) or '(none)'}")
    if c["pickup_flag_vs_measure_length_disagree_stems"]:
        L.append(f"pickup-flag vs measure-length disagree: "
                 f"{', '.join(c['pickup_flag_vs_measure_length_disagree_stems'])}")
    d = artifact["argmax_offset_distribution"]
    L.append("")
    L.append("-- argmax offset distribution (count of pieces best at each offset) --")
    L.append(f"{'offset':>8} " + " ".join(f"{str(o):>7}" for o in OFFSETS))
    L.append(f"{'overall':>8} " + " ".join(f"{d['overall'][str(o)]:>7}" for o in OFFSETS))
    for cls in ("both", "ours_pickup_only", "wir_m0_only", "neither"):
        L.append(f"{cls:>8} " + " ".join(f"{d['by_contingency_class'][cls][str(o)]:>7}" for o in OFFSETS))
    L.append("-- by ours_pickup --")
    for k in ("ours_pickup", "no_ours_pickup"):
        L.append(f"{k:>15} " + " ".join(f"{d['by_ours_pickup'][k][str(o)]:>7}" for o in OFFSETS))
    hm = artifact["high_margin_pieces"]
    L.append("")
    L.append(f"-- pieces with argmax margin over offset 0 > {hm['threshold_pp']} pp: {hm['count']} --")
    for r in hm["pieces"]:
        L.append(f"  {r['stem']:>12}  class={r['class']:<16} argmax={str(r['argmax_offset']):>5} "
                 f"margin={r['margin_pp']}pp")
    pm = artifact["pickup_chord_mapping"]
    L.append("")
    L.append("-- pickup-chord mapping (sharpest form; MASKED by the global sweep) --")
    L.append(f"pieces with both m0: {pm['pieces_with_both_m0']}  "
             f"| WiR m0 chord lands: inside={pm['relation_counts']['inside']} "
             f"overshoot={pm['relation_counts']['overshoot']} before={pm['relation_counts']['before']}")
    L.append(f"WiR m0 first-beat distribution: {pm['wir_m0_first_beat_distribution']}")
    L.append(f"displacement (ticks) distribution: {pm['displacement_ticks_distribution']}")

    n = artifact["named_case_bwv110_7"]
    L.append("")
    L.append("-- named case bwv110.7 (desk-sim §4.5) --")
    if n:
        L.append(f"  class={n['class']}  ours_min_m={n['ours_min_measure']}  wir_min_m={n['wir_min_measure']}  "
                 f"m0_span={n['m0_span_ticks']}  derived_measure={n['derived_measure_ticks']}")
        L.append(f"  {'offset':>8} {'agree':>8} {'scored':>8} {'pct':>8}")
        for o in OFFSETS:
            po = n["per_offset"][str(o)]
            L.append(f"  {str(o):>8} {po['agree']:>8} {po['scored']:>8} {str(po['pct']):>8}")
        L.append(f"  argmax offset = {n['argmax_offset']}  (margin over 0 = {n['margin_pp']} pp)")
    else:
        L.append("  (bwv110.7 not in covered set)")
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    ap.add_argument("--out-json", default=str(here / "wir_alignment_probe.json"))
    ap.add_argument("--out-summary", default=str(here / "wir_alignment_probe_summary.txt"))
    args = ap.parse_args()

    artifact = build_artifact()
    Path(args.out_json).write_text(json.dumps(artifact, indent=1, ensure_ascii=False) + "\n",
                                   encoding="utf-8")
    write_summary(artifact, Path(args.out_summary))
    print(f"Wrote {args.out_json} and {args.out_summary}")
    est = artifact["establishment"]
    print(f"offset-0 reconciles to block-(A) Default: {est['reconciles_to_block_A_default']} "
          f"({est['offset0_root_agree_pct']}%); per-piece oracle match: "
          f"{est['per_piece_oracle_matches_build_piece_grid']}")


if __name__ == "__main__":
    main()
