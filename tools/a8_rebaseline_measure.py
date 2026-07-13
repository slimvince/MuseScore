#!/usr/bin/env python3
"""a8_rebaseline_measure.py — A-8 granularity-robust re-baseline MEASUREMENT driver.

READ-ONLY / MEASUREMENT-ONLY. No src/ change, no corpus mutation, no gate change.
This is the measurement instrument for the A-8 candidate re-baselined gate (roadmap
Stage 5.2 / A-8): it measures the candidate metric at the granularity-robust
**union-of-boundaries** unit on the frozen gate corpus, for all three presets, both
adjudication variants, and all three respects, and produces the mapping / undercount /
class-split evidence the ratification needs.

ORCHESTRATION ONLY over already-pinned functions (the cc_stage1d "orchestration is not a
metric definition" basis). It imports and reuses verbatim:
  - compare_rn.classify_pair          (the per-cell RN verdict — 5 buckets)
  - compare_rn._active_index_at        (point membership in a span list)
  - compare_rn._our_key_tonic / _dcml_key_tonic  (key identity parsers)
  - compare_rn.grid_score_regions      (the pinned union-of-boundaries primitive —
                                        used ONLY as a self-validation oracle)
  - compare_analyses._dcml_time_spans  (DCML tick spans; same as grid_score_regions)
  - compare_analyses.three_way_classify (the legacy music21 root filter)
  - compare_analyses.load_analysis / align_* (loading + the legacy region gate)
  - characterise_bir_false.validate_corpus_dir (manifest / no-contamination check)
  - dcml_parser.find_wir_file / parse_rntxt_file (WiR reference)

The driver re-runs the union-of-boundaries cell loop itself (so it can attach the KEY
respect and the music21 leg, which grid_score_regions does not compute) and ASSERTS its
variant-(b) 5-bucket duration decomposition equals grid_score_regions() byte-for-byte on
every piece — that assertion is the proof the re-run loop is a faithful reuse of the
pinned primitive, not a re-definition.

THE ABSTAIN-AWARE CONVENTION (OI-33; before any abstaining path is adoption-gated).
Every reported agreement-% is published WITH its abstain/coverage figure so a metric can
never be flattered by opting out of the hard slices:
  - ROOT respect (the governing hard stop): an abstained cell — OUR region carries no root_pc —
    is counted a DISAGREEMENT, so the root metric is NOT abstention-reducible. The
    scored/unscored duration is published. The comparison itself is compare_analyses.roots_agree,
    the ONE root-equality decision every graded site routes through (OI-52), so this convention
    is encoded once instead of being re-implemented at each `==`.
  - KEY respect: an abstained cell — OUR key is unparseable/absent — becomes `keyfail` and is
    EXCLUDED from the key-agree denominator (agree+disagree). So the key-agree-% IS abstention-
    reducible: raising the key-abstain rate can lift key-agree without better inference. The
    summary publishes b_key_fail (the abstain duration) and the manifest key_parse_fail_pct;
    robust_stop_diff reports the key-abstain BESIDE key-agree and FLAGS a candidate abstain
    above the reference. Mechanical enforcement, not just prose.

Usage:
    python tools/a8_rebaseline_measure.py --out-dir <scratch>
"""
from __future__ import annotations

import argparse
import hashlib
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

WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"

PRESETS = ["baroque", "jazz", "default"]

RN_CATEGORIES = crn.RN_CATEGORIES  # (exact, partial, key_disagree, quality_disagree, root_err)


# ── structural class-(a)/(b) test at cell granularity (two-tier policy) ──────
# Class (a) = pitch-class-UNDECIDABLE root by construction (the "coin-flip" churn):
#   (i)  transposition-invariant sonorities — the root is undefined by symmetry:
#        fully-diminished 7th (T3-invariant), augmented triad (T4-invariant),
#        whole-tone subset (T2-invariant).  These are the ~53%-of-Baroque symmetric
#        dim7 majority named in CLAUDE.md.
#   (ii) the half-diminished-7th / minor-6th SHARE-TONE collection {r,r+3,r+6,r+10}
#        — a ø7 and an m6 a minor third apart are the SAME pc-set (Eø7 == Gm6), so the
#        root is pc-undecidable between the two spellings (CLAUDE.md's bwv291/bwv352 class).
# Class (b) = everything else (pitch-class-DECIDABLE root — triads, dom7, etc.).
# Guardrail (2) of the policy: DEFAULT TO CLASS (b) ON ANY DOUBT.  This test is therefore
# deliberately CONSERVATIVE — it fires class (a) only on pc-sets that are provably
# root-ambiguous from OUR pitch-class set alone (WiR gives no DCML pc-set, so a share-tone
# case whose pc-set is not one of the two templates above is counted class (b), the safe
# direction for a gate).  Stated, not left to the reader (per the A-8 instruction Task 1).

def _pcs(bitmap):
    if bitmap is None:
        return frozenset()
    return frozenset(i for i in range(12) if bitmap & (1 << i))


def _t_invariant(pcs, k):
    """True iff pcs is invariant under transposition by k semitones (symmetry)."""
    if not pcs:
        return False
    return frozenset((p + k) % 12 for p in pcs) == pcs


def _is_halfdim_or_min6_set(pcs):
    """True iff pcs == {r, r+3, r+6, r+10} for some r (the ø7 / m6 share-tone set)."""
    if len(pcs) != 4:
        return False
    for r in pcs:
        if frozenset((r + d) % 12 for d in (0, 3, 6, 10)) == pcs:
            return True
    return False


def cell_class(our_region):
    """Return 'a' (pc-undecidable / symmetric-share-tone) or 'b' (pc-decidable root)."""
    pcs = _pcs(our_region.pitch_class_set)
    if len(pcs) >= 3 and _t_invariant(pcs, 3):      # dim7 (fully-diminished)
        return 'a'
    if len(pcs) >= 3 and _t_invariant(pcs, 4):      # augmented triad
        return 'a'
    if len(pcs) >= 4 and _t_invariant(pcs, 2):      # whole-tone
        return 'a'
    if _is_halfdim_or_min6_set(pcs):                # ø7 <-> m6 share-tone
        return 'a'
    return 'b'


# ── the candidate metric: union-of-boundaries cells, 3 respects, 2 variants ──

class PieceGrid:
    """Per-cell candidate-metric result for one (ours, wir, m21) triple."""

    def __init__(self, stem):
        self.stem = stem
        self.cells = []          # list of dict per scored cell
        self.scored_dur = 0
        self.unscored_dur = 0
        self.bucket_dur = Counter()   # variant-(b) RN decomposition (validation oracle)

    def add_cell(self, t0, t1, our_r, dcml_r, m21_root):
        w = t1 - t0
        pair = crn.classify_pair(our_r, dcml_r)
        if pair is None:
            self.unscored_dur += w
            return
        self.scored_dur += w
        bucket = pair.category
        self.bucket_dur[bucket] += w

        # respect 1 — root. The one shared comparison (OI-52); the abstain convention
        # stated below in THE ABSTAIN-AWARE CONVENTION is encoded there, once, rather
        # than re-implemented at each graded site. classify_pair has already dropped any
        # cell whose DCML root did not resolve, so an abstain here is OURS, and it counts
        # as a disagreement.
        root_agree = cmp.roots_agree(our_r.root_pc, dcml_r.root_pc)
        # respect 2 — RN (exact+partial == agree, per design doc rn_agree)
        rn_agree = bucket in ("exact", "partial")
        # respect 3 — key vs the DCML GLOBAL (home) key (keyfail reported separately)
        otc, omaj = crn._our_key_tonic(getattr(our_r, "key", None))
        gtc, gmaj = crn._dcml_key_tonic(getattr(dcml_r, "global_key", None))
        if otc is None:
            key_verdict = "keyfail"          # our key unparseable
        elif gtc is None:
            key_verdict = "dcml_keyfail"     # dcml global_key unparseable (rare)
        elif (otc, omaj) == (gtc, gmaj):
            key_verdict = "agree"
        else:
            key_verdict = "disagree"

        # respect 3b — key vs the DCML LOCAL key (the key IN EFFECT; OI-143). Carried BESIDE
        # the home-key column; the local column counts correct modulation-following as agreement.
        ltc, lmaj = crn._dcml_key_tonic(getattr(dcml_r, "local_key", None))
        if otc is None:
            key_verdict_local = "keyfail"
        elif ltc is None:
            key_verdict_local = "dcml_keyfail"
        elif (otc, omaj) == (ltc, lmaj):
            key_verdict_local = "agree"
        else:
            key_verdict_local = "disagree"

        # variant-(a) legacy music21 genuine filter (root-defined) + BIR=false
        three_way = cmp.three_way_classify(our_r.root_pc, m21_root, dcml_r.root_pc)
        bir_false = not bool(our_r.bass_is_root)   # matches gate: `if bass_is_root: continue`
        m21_genuine = (three_way == "music21_dcml_agree") and bir_false

        self.cells.append({
            "t0": t0, "t1": t1, "w": w,
            "our_root": our_r.root_pc, "dcml_root": dcml_r.root_pc,
            "our_sym": our_r.chord_symbol, "our_q": our_r.quality,
            "dcml_sym": dcml_r.chord_symbol,
            "bucket": bucket,
            "root_agree": root_agree,
            "rn_agree": rn_agree,
            "key_verdict": key_verdict,
            "key_verdict_local": key_verdict_local,
            "three_way": three_way,
            "bir_false": bir_false,
            "m21_genuine": m21_genuine,
            "cls": cell_class(our_r),
        })


def build_piece_grid(stem, ours_regions, wir_regions, m21_regions):
    """Re-run the union-of-boundaries loop (ours ∪ DCML boundaries) attaching the
    key respect + music21 leg.  Then self-validate the variant-(b) buckets against
    the pinned grid_score_regions()."""
    pg = PieceGrid(stem)
    if not ours_regions or not wir_regions:
        return pg
    ours_spans = [(r.start_tick, r.end_tick) for r in ours_regions]
    dcml_spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    m21_spans = [(r.start_tick, r.end_tick) for r in m21_regions] if m21_regions else []

    bounds = set()
    for (s, e) in ours_spans:
        if e > s:
            bounds.add(s); bounds.add(e)
    for (s, e) in dcml_spans:
        if s >= 0 and e > s:
            bounds.add(s); bounds.add(e)
    if len(bounds) < 2:
        return pg
    grid = sorted(bounds)
    for i in range(len(grid) - 1):
        t0, t1 = grid[i], grid[i + 1]
        if t1 - t0 <= 0:
            continue
        oi = crn._active_index_at(ours_spans, t0)
        di = crn._active_index_at(dcml_spans, t0)
        if oi is None or di is None:
            pg.unscored_dur += (t1 - t0)
            continue
        mi = crn._active_index_at(m21_spans, t0) if m21_spans else None
        m21_root = m21_regions[mi].root_pc if mi is not None else None
        pg.add_cell(t0, t1, ours_regions[oi], wir_regions[di], m21_root)

    # ── self-validation: variant-(b) buckets must equal the pinned primitive ──
    oracle = crn.grid_score_regions(ours_regions, wir_regions)
    if dict(pg.bucket_dur) != dict(oracle.bucket_dur) or pg.scored_dur != oracle.scored_dur:
        raise AssertionError(
            f"{stem}: re-run grid diverges from grid_score_regions "
            f"(mine={dict(pg.bucket_dur)} scored={pg.scored_dur} vs "
            f"oracle={dict(oracle.bucket_dur)} scored={oracle.scored_dur})")
    return pg


# ── the legacy batch gate on the same corpus (the anchor, for the mapping) ──

def batch_gate_cases(ours_regions, m21_regions, wir_regions):
    """Reproduce characterise_bir_false's per-region BIR=false gate.  Returns the
    set of (stem-less) region cases as dicts {tick, our_root, dcml_root, start, end}."""
    aligned = cmp.align_regions(ours_regions, m21_regions)
    wir_aligned = (cmp.align_dcml_regions(ours_regions, wir_regions)
                   if wir_regions else [None] * len(ours_regions))
    cases = []
    for i, (our_r, their_r) in enumerate(aligned):
        if cmp.classify(our_r, their_r).category != "chord_disagree":
            continue
        if our_r.bass_is_root:
            continue
        if not wir_regions or i >= len(wir_aligned):
            continue
        wir_r = wir_aligned[i]
        wir_pc = wir_r.root_pc if wir_r is not None else None
        cat = cmp.three_way_classify(our_r.root_pc, their_r.root_pc if their_r else None, wir_pc)
        if cat != "music21_dcml_agree":
            continue
        cases.append({
            "tick": our_r.start_tick, "start": our_r.start_tick, "end": our_r.end_tick,
            "our_root": our_r.root_pc, "dcml_root": wir_pc,
            "our_sym": our_r.chord_symbol, "cls": cell_class(our_r),
        })
    return cases


def measure_preset(preset, out_dir, corpus_root=None, scores=None):
    # corpus_root: the dir holding the per-preset corpus subdirs (<root>/<preset>).
    # Default = tools/corpus (the frozen corpus). The Stage-5 fitter passes a scratch
    # root so a fitted regen is measured WITHOUT touching the frozen corpus. Default
    # (None) is byte-identical to the historical hardcoded path.
    corpus_root = Path(corpus_root) if corpus_root else (_ROOT / "tools" / "corpus")
    corpus_dir = corpus_root / preset
    cbf.validate_corpus_dir(corpus_dir)   # manifest / no-contamination gate (raises on fail)

    ours_files = sorted(corpus_dir.glob("*.ours.json"))
    # Stage-5 fitter: optional stem filter (the fitting/held-out split). None => all
    # scores (byte-identical to the historical run). A set of stems restricts the
    # measured objective to exactly those scores (the fitting-split objective).
    if scores is not None:
        ours_files = [p for p in ours_files if p.stem.replace(".ours", "") in scores]
    total_files = len(ours_files)
    wir_covered = 0
    wir_no_annotation = 0            # OI-140: stem has no WiR reference (a legitimate exclusion)
    wir_parse_fail_stems = []        # OI-140: WiR file present but load failed / yielded 0 regions
    ours_load_fail_stems = []        # OI-123: corrupt/unreadable .ours.json (NOT folded into no_wir)
    m21_load_fail_stems = []         # OI-123: corrupt/unreadable .music21.json (variant-(a) leg only)
    empty_ours = 0                   # OI-123: .ours.json loaded but yielded 0 regions
    # OI-124: identity of the WiR SOURCE graded against (offset-file pattern). Deterministic
    # (ours_files sorted); the in-memory OI-142 transposition is separately pinned by the
    # committed offsets file — this hashes the raw analysis.txt content per covered stem.
    wir_source_hasher = hashlib.sha256()
    m21_and_wir = 0

    # aggregates
    agg = {
        "scored_dur": 0, "unscored_dur": 0,
        "bucket_dur": Counter(),
        # respect duration tallies (variant b = DCML-only)
        "b_root_agree": 0, "b_root_dis": 0,
        "b_rn_agree": 0, "b_rn_dis": 0,
        "b_key_agree": 0, "b_key_dis": 0, "b_key_fail": 0, "b_dcml_keyfail": 0,
        # key vs the DCML LOCAL key (OI-143) — the same four buckets, graded vs local_key
        "b_key_agree_local": 0, "b_key_dis_local": 0, "b_key_fail_local": 0, "b_dcml_keyfail_local": 0,
        # variant a = music21-filtered (root-defined genuine filter)
        "a_root_dis_dur": 0,   # duration of genuine (music21-filtered) root failures
        "a_root_dis_cells": 0,
        "a_rn_dis_dur": 0,     # rn-fail AND genuine filter (⊆ root failures structurally)
        "a_key_dis_dur": 0,
        # class split of root-failing cells
        "b_root_dis_cells": 0,
        "b_cls_a_dur": 0, "b_cls_b_dur": 0, "b_cls_a_cells": 0, "b_cls_b_cells": 0,
        "a_cls_a_dur": 0, "a_cls_b_dur": 0, "a_cls_a_cells": 0, "a_cls_b_cells": 0,
    }
    # full failing-cell enumerations
    b_root_fail_cells = []   # variant b root failures (DCML-only)
    a_root_fail_cells = []   # variant a root failures (music21-filtered)
    # mapping: batch gate cases and their grid disposition
    batch_cases = []         # list of (stem, case)
    grid_by_stem = {}        # stem -> PieceGrid

    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        m21_path = corpus_dir / f"{stem}.music21.json"
        # OI-123: a corrupt .ours.json must NOT silently fold into the no_wir bucket (which conflates
        # a parse failure with a missing WiR annotation). Narrow the catch to the load-failure types
        # and count it in its own named bucket, surfaced below.
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            ours_load_fail_stems.append((stem, f"{type(exc).__name__}: {exc}"))
            continue
        if not ours_regions:
            empty_ours += 1
            continue
        m21_regions = []
        if m21_path.exists():
            try:
                _, m21_regions = cmp.load_analysis(m21_path)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                m21_load_fail_stems.append((stem, f"{type(exc).__name__}: {exc}"))
                m21_regions = []
        # ── WiR ground truth (OI-140: distinguish a MISSING annotation from a PARSE FAILURE) ──
        # The governing hard stop is a class-(b) root-disagree DURATION non-increase; a WiR-parse
        # failure that silently became an empty list would DROP the piece from the class-(b)
        # population and could PASS the non-increase gate by shrinking coverage. So a present-but-
        # unparseable WiR file is NAMED (never folded into the no-annotation bucket), and the
        # wir_covered figure the summary exports lets robust_stop_diff reconcile coverage and fail
        # loudly on a systematic break.
        wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
        if wir_path is None:
            wir_no_annotation += 1
            continue    # no human GT for this stem — a legitimate exclusion, not a failure
        wir_regions = []
        try:
            # THE shared WiR loading substrate (applies the OI-142 transposition correction).
            wir_regions = dcml.load_wir_regions(str(WIR_DIR), stem)
        except Exception as exc:
            wir_parse_fail_stems.append((stem, f"{type(exc).__name__}: {exc}"))
            continue
        if not wir_regions:
            # a present WiR file that yields no scoreable region is a parse anomaly, not a
            # missing annotation — name it so it cannot silently shrink the class-(b) population.
            wir_parse_fail_stems.append((stem, "present WiR file yielded 0 scoreable regions"))
            continue
        wir_covered += 1
        # OI-124: fold this covered stem's WiR SOURCE identity into the running fingerprint.
        try:
            wir_bytes = Path(wir_path).read_bytes()
        except OSError:
            wir_bytes = b""
        wir_source_hasher.update(stem.encode("utf-8") + b"\0" + hashlib.sha256(wir_bytes).digest())
        if m21_regions:
            m21_and_wir += 1

        pg = build_piece_grid(stem, ours_regions, wir_regions, m21_regions)
        grid_by_stem[stem] = pg

        agg["scored_dur"] += pg.scored_dur
        agg["unscored_dur"] += pg.unscored_dur
        agg["bucket_dur"] += pg.bucket_dur

        for c in pg.cells:
            w = c["w"]
            # respect 1 root (variant b)
            if c["root_agree"]:
                agg["b_root_agree"] += w
            else:
                agg["b_root_dis"] += w
                agg["b_root_dis_cells"] += 1
                b_root_fail_cells.append((stem, c))
                if c["cls"] == "a":
                    agg["b_cls_a_dur"] += w; agg["b_cls_a_cells"] += 1
                else:
                    agg["b_cls_b_dur"] += w; agg["b_cls_b_cells"] += 1
            # respect 2 rn (variant b)
            if c["rn_agree"]:
                agg["b_rn_agree"] += w
            else:
                agg["b_rn_dis"] += w
            # respect 3 key vs GLOBAL/home (variant b)
            kv = c["key_verdict"]
            if kv == "agree":
                agg["b_key_agree"] += w
            elif kv == "disagree":
                agg["b_key_dis"] += w
            elif kv == "keyfail":
                agg["b_key_fail"] += w
            else:
                agg["b_dcml_keyfail"] += w
            # respect 3 key vs LOCAL (variant b; OI-143)
            kvl = c["key_verdict_local"]
            if kvl == "agree":
                agg["b_key_agree_local"] += w
            elif kvl == "disagree":
                agg["b_key_dis_local"] += w
            elif kvl == "keyfail":
                agg["b_key_fail_local"] += w
            else:
                agg["b_dcml_keyfail_local"] += w
            # variant a (music21-filtered genuine failures)
            if c["m21_genuine"]:
                agg["a_root_dis_dur"] += w
                agg["a_root_dis_cells"] += 1
                a_root_fail_cells.append((stem, c))
                if c["cls"] == "a":
                    agg["a_cls_a_dur"] += w; agg["a_cls_a_cells"] += 1
                else:
                    agg["a_cls_b_dur"] += w; agg["a_cls_b_cells"] += 1
                if not c["rn_agree"]:
                    agg["a_rn_dis_dur"] += w
                if c["key_verdict"] == "disagree":
                    agg["a_key_dis_dur"] += w

        # batch gate (region granularity) for the mapping
        for case in batch_gate_cases(ours_regions, m21_regions, wir_regions):
            batch_cases.append((stem, case))

    # ── run-merge the root-failing cells into segmentation-stable failing runs ──
    def merge_runs(cells):
        """cells: list of (stem, celldict). Merge adjacent same-(stem,our_root,dcml_root)
        cells whose spans touch (c.t1 == next.t0) into runs → the re-slice-stable id."""
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

    b_runs = merge_runs(b_root_fail_cells)
    a_runs = merge_runs(a_root_fail_cells)

    result = {
        "preset": preset,
        "coverage": {
            "total_ours_files": total_files,
            "wir_covered": wir_covered,           # variant (b) denominator (scores)
            "m21_and_wir": m21_and_wir,           # variant (a) denominator (scores)
            "no_wir": total_files - wir_covered,
            # OI-140: the no_wir total split into its WiR causes so a systematic WiR-parse
            # breakage surfaces as a NAMED failure rather than a silent coverage shrink.
            "wir_no_annotation": wir_no_annotation,
            "wir_parse_fail": len(wir_parse_fail_stems),
            "wir_parse_fail_stems": [s for s, _ in wir_parse_fail_stems],
            # OI-123: the .ours.json load failures are their OWN bucket, not folded into no_wir.
            "ours_load_fail": len(ours_load_fail_stems),
            "ours_load_fail_stems": [s for s, _ in ours_load_fail_stems],
            "m21_load_fail": len(m21_load_fail_stems),
            "empty_ours": empty_ours,
            # OI-124: identity of the WiR source content graded against (paired with the
            # separately-pinned offsets file), so a foreign/drifted WiR clone is detectable.
            "wir_source_sha256": wir_source_hasher.hexdigest(),
        },
        "agg": {k: (dict(v) if isinstance(v, Counter) else v) for k, v in agg.items()},
        "batch_gate_count": len(batch_cases),
        "grid_b_root_fail_cells": len(b_root_fail_cells),
        "grid_a_root_fail_cells": len(a_root_fail_cells),
        "grid_b_root_fail_runs": len(b_runs),
        "grid_a_root_fail_runs": len(a_runs),
    }

    # write enumerations
    _write_cells(out_dir / f"{preset}_variant_b_root_fail_cells.txt",
                 preset, "VARIANT B (DCML-only) — root-respect failing cells", b_root_fail_cells)
    _write_cells(out_dir / f"{preset}_variant_a_root_fail_cells.txt",
                 preset, "VARIANT A (music21-filtered) — root-respect failing cells (genuine)",
                 a_root_fail_cells)
    _write_runs(out_dir / f"{preset}_variant_a_root_fail_runs.txt",
                preset, "VARIANT A — root-failing RUNS (re-slice-stable identity)", a_runs)
    _write_runs(out_dir / f"{preset}_variant_b_root_fail_runs.txt",
                preset, "VARIANT B — root-failing RUNS (re-slice-stable identity)", b_runs)

    # mapping table data
    mapping = build_mapping(batch_cases, grid_by_stem)
    (out_dir / f"{preset}_mapping.json").write_text(
        json.dumps(mapping, indent=1), encoding="utf-8")
    result["mapping_summary"] = mapping["summary"]

    # OI-140: a WiR-parse failure must never be silent — it shrinks the class-(b) population.
    if wir_parse_fail_stems:
        print(f"[{preset}] !! WiR PARSE FAILURE on {len(wir_parse_fail_stems)} stem(s) — "
              f"class-(b) coverage is REDUCED (would silently pass the non-increase gate):",
              file=sys.stderr)
        for stem, reason in wir_parse_fail_stems:
            print(f"    {stem}: {reason}", file=sys.stderr)
    # OI-123: surface the .ours.json / .music21.json load failures (no longer folded into no_wir).
    for label, stems in (("OURS LOAD", ours_load_fail_stems), ("MUSIC21 LOAD", m21_load_fail_stems)):
        if stems:
            print(f"[{preset}] !! {label} FAILURE on {len(stems)} stem(s):", file=sys.stderr)
            for stem, reason in stems:
                print(f"    {stem}: {reason}", file=sys.stderr)

    return result, a_runs, b_runs, batch_cases


def _write_cells(path, preset, title, cells):
    lines = [f"=== {preset}: {title} ===",
             f"(count = {len(cells)}; identity = stem@cellStartTick)"]
    for stem, c in sorted(cells, key=lambda x: (x[0], x[1]["t0"])):
        lines.append(
            f"{stem}@{c['t0']}  [{c['t0']},{c['t1']}) w={c['w']:>5}  "
            f"our={c['our_sym']}({c['our_root']}) -> dcml={c['dcml_sym']}({c['dcml_root']})  "
            f"bucket={c['bucket']} key={c['key_verdict']} cls={c['cls']} 3way={c['three_way']}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_runs(path, preset, title, runs):
    lines = [f"=== {preset}: {title} ===",
             f"(count = {len(runs)}; identity = stem@runStartTick)"]
    for r in sorted(runs, key=lambda r: (r["stem"], r["start"])):
        lines.append(
            f"{r['stem']}@{r['start']}  [{r['start']},{r['end']}) dur={r['dur']:>6}  "
            f"our={r['our_sym']}({r['our_root']}) -> dcml_root={r['dcml_root']}  cls={r['cls']}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_mapping(batch_cases, grid_by_stem):
    """For each batch-gate region case, find the overlapping grid cells and record
    whether the case remains failing under variant (a) and variant (b) on the root
    respect."""
    rows = []
    a_hit = b_hit = disappeared_a = disappeared_b = 0
    for stem, case in batch_cases:
        pg = grid_by_stem.get(stem)
        s, e = case["start"], case["end"]
        cells = [c for c in (pg.cells if pg else []) if c["t0"] < e and c["t1"] > s]
        # does any overlapping cell show a root failure under each variant?
        b_fail = any(not c["root_agree"] for c in cells)
        a_fail = any(c["m21_genuine"] for c in cells)
        if b_fail:
            b_hit += 1
        else:
            disappeared_b += 1
        if a_fail:
            a_hit += 1
        else:
            disappeared_a += 1
        rows.append({
            "stem": stem, "tick": case["tick"], "our_root": case["our_root"],
            "dcml_root": case["dcml_root"], "our_sym": case["our_sym"], "cls": case["cls"],
            "n_overlap_cells": len(cells),
            "b_root_fail": b_fail, "a_root_fail": a_fail,
        })
    return {
        "rows": rows,
        "summary": {
            "batch_cases": len(batch_cases),
            "still_failing_variant_b": b_hit,
            "still_failing_variant_a": a_hit,
            "disappeared_variant_b": disappeared_b,
            "disappeared_variant_a": disappeared_a,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    # Stage-5 fitter additive flags (byte-identical to the historical run when unused).
    ap.add_argument("--corpus-root", default=None,
                    help="Root dir holding the per-preset corpus subdirs (<root>/<preset>). "
                         "Default: tools/corpus. Pass a manifest-stamped scratch root to "
                         "measure a fitted regen without touching the frozen corpus.")
    ap.add_argument("--preset", default=None, choices=PRESETS,
                    help="Measure only this preset (default: all three). The single-preset "
                         "run is byte-identical to the full run for the preset it covers.")
    ap.add_argument("--scores", default=None,
                    help="Path to a newline-separated stem list; restrict the measured "
                         "objective to exactly those scores (the fitting/held-out split). "
                         "Default: all scores (byte-identical to the historical run).")
    args = ap.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    scores = None
    if args.scores:
        scores = {s.strip() for s in Path(args.scores).read_text().splitlines() if s.strip()}

    presets = [args.preset] if args.preset else PRESETS
    summary = {}
    for preset in presets:
        res, a_runs, b_runs, batch_cases = measure_preset(preset, out_dir,
                                                          corpus_root=args.corpus_root,
                                                          scores=scores)
        summary[preset] = res
        print(f"[{preset}] validated grid==oracle OK; "
              f"batch_gate={res['batch_gate_count']} "
              f"grid_a_cells={res['grid_a_root_fail_cells']} "
              f"grid_a_runs={res['grid_a_root_fail_runs']} "
              f"grid_b_cells={res['grid_b_root_fail_cells']}")

    (out_dir / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(f"\nWrote summary.json + per-preset enumerations to {out_dir}")


if __name__ == "__main__":
    main()
