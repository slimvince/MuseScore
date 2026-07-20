#!/usr/bin/env python3
"""gen_fermata_boundary.py — the fermata-conditioned boundary cells (algorithm-completion step 1;
Cowork dispatch 2026-07-19, Task 1). READ-ONLY / FIT-LAYER-OWNED. No src/ change, no corpus mutation,
no gate change, NO DECODING, NO EVALUATION.

★ STEP-2 ADDITION (the weight fit): the same counted population is ALSO tabulated CROSSED with the beat
class — `exact_tick_by_beat_class` — which is the form the ratified factorization's boundary factor
actually names (§3 items 7+8: the boundary probability conditioned on beat-strength class AND the
fermata). That crossed table is what the decoder's boundary factor consumes; a cell below the count
threshold pools to the beat-class-only cell in `note_tables_*.json`. The step-1 marginal cells are
untouched and still reported (they reproduce byte-identically).

WHAT IT PRODUCES — a SMALL ADDENDUM artifact beside the boundary table (the dispatch's wording): the
ONE counted addition the ratified boundary factor names, **P(segment boundary | fermata at or adjacent
to the event)**. It does NOT re-count any existing table — the existing note-side tables
(`note_tables_*.json`) are untouched; this is a separate covariate on the SAME event population.

THE PROTOCOL (identical to every note-side table, dispatch Task 1): the 5-fold grouped split
(fold_assignment.json), the count>=20 reliability rule (gen_label_tables.THRESHOLD), the same
exclusions (7 OI-184-flagged + 2 multi-meter pieces excluded entirely; anacrusis m0 events skipped),
and the OI-184 interim measured-misaligned (zero-factor) span leave-out. Both boundary variants are
reported (exact-tick and first-event-of-kept-segment robust), mirroring the boundary table's dual.

REUSE (#6): gen_note_tables' own primitives — gt_segments, excluded_zero_factor_segments,
_seg_idx_for_tick, FLAGGED / MULTIMETER / COUNTED_METERS, the fold machinery, the THRESHOLD. This
module writes NO second GT parser, segment resolver, or exclusion rule.

THE COVARIATE — "fermata at or adjacent to the event" is defined mechanically (below):
  ferm_ctx(event) = the event's own fermata flag (a sounding note carries a fermata; the "at" case)
                    OR a fermata note ENDS at the event's start tick (the phrase-end boundary right
                       after a fermata — the "adjacent" case that carries the boundary signal)
                    OR a fermata note BEGINS at the event's end tick (the approach immediately before
                       a fermata).
This is the boundary-factor reading of factorization §3.8 (the fermata as a boundary prior + the de
Clercq weak-beat displacement, where the arrival may sit one strong beat before a metrically weak
fermata; the offset/onset adjacency captures both the at-fermata and the displaced-approach sites).
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import gen_note_tables as gnt        # noqa: E402  the note-side counting primitives (reused, #6)
import gen_label_tables as glt       # noqa: E402  THRESHOLD / N_FOLDS / _git_head / _rel

NOTE_EVENTS = _HERE / "note_events" / "note_events.json"
FOLD_ARTIFACT = _HERE / "fold_assignment.json"
OUT_JSON = _HERE / "fermata_boundary_addendum.json"
OUT_SUMMARY = _HERE / "fermata_boundary_addendum_summary.txt"

VERSION = "fermata-boundary-addendum-v1 (P(boundary | fermata at/adjacent); step-1 counted addition)"

# note/event field indices (note_events provenance) — the fermata flags this addendum adds.
N_ONSET, N_DUR, N_MEAS, N_FERM = 0, 1, 6, 12
EV_START, EV_END, EV_MEAS, EV_MC, EV_FERM = 0, 1, 2, 4, 5


def _ferm_ctx_ticks(notes):
    """Ticks where a (non-anacrusis) fermata note ENDS (offset) and BEGINS (onset) — the 'adjacent'
    part of the covariate. Measure-0 (anacrusis) notes are excluded, matching the counting population."""
    offs, ons = set(), set()
    for n in notes:
        if n[N_MEAS] == 0 or len(n) <= N_FERM or not n[N_FERM]:
            continue
        ons.add(n[N_ONSET])
        offs.add(n[N_ONSET] + n[N_DUR])
    return offs, ons


def event_ferm_ctx(ev, ferm_off, ferm_on):
    """THE fermata boundary-covariate rule for one event (the single definition, #6): the event's own
    fermata flag, OR a fermata note ends at its start tick, OR a fermata note begins at its end tick."""
    return bool(len(ev) > EV_FERM and ev[EV_FERM]) or (ev[EV_START] in ferm_off) or (ev[EV_END] in ferm_on)


def event_ferm_ctx_flags(events, notes):
    """The per-event fermata-context flags for a whole piece — the SAME rule the counted cells were fit
    under, so the decoder's boundary factor reads its covariate from this one definition."""
    ferm_off, ferm_on = _ferm_ctx_ticks(notes)
    return [event_ferm_ctx(ev, ferm_off, ferm_on) for ev in events]


def per_stem(stem: str, piece: dict):
    """Fermata-conditioned boundary counts for one stem, mirroring gnt.per_stem_counts' boundary block
    exactly (same exclusions, same numerator). Returns None + reason for an excluded stem."""
    if stem in gnt.FLAGGED:
        return None, "flagged"
    if stem in gnt.MULTIMETER or piece["multi_meter"]:
        return None, "multi_meter"
    meter = tuple(piece["meter"]) if piece["meter"] else None
    if meter not in gnt.COUNTED_METERS:
        return None, "meter_not_counted"

    segs = gnt.gt_segments(stem)
    starts = [s["start"] for s in segs]
    excluded = gnt.excluded_zero_factor_segments(segs, piece)   # OI-184 interim leave-out (shared rule)
    excluded_idx = {sp["idx"] for sp in excluded}

    # the boundary numerator sets (KEPT GT segments only) — identical to gnt.per_stem_counts
    gt_start_set = {segs[i]["start"] for i in range(len(segs)) if i not in excluded_idx}
    first_event_of_seg = {}
    for ev in piece["events"]:
        start, measure = ev[EV_START], ev[EV_MEAS]
        if measure == 0:
            continue
        si = gnt._seg_idx_for_tick(segs, starts, start)
        if si >= 0 and si not in excluded_idx:
            seg_start = segs[si]["start"]
            fe = first_event_of_seg.get(seg_start)
            if fe is None or start < fe:
                first_event_of_seg[seg_start] = start
    robust_boundary_ticks = set(first_event_of_seg.values())

    ferm_off, ferm_on = _ferm_ctx_ticks(piece["notes"])

    # cell -> [boundaries, events], both boundary variants; keyed by fermata context (True/False), and
    # (step 2, the weight fit) CROSSED with the beat class — the form the ratified factorization's
    # boundary factor names (§3 items 7+8: boundary probability conditioned on beat-strength class AND
    # the fermata). The marginal (fermata-only) cells stay exactly as step 1 counted them.
    exact = {True: [0, 0], False: [0, 0]}
    robust = {True: [0, 0], False: [0, 0]}
    exact_bc = defaultdict(lambda: [0, 0])          # (beat_class, ferm_ctx) -> [boundaries, events]
    for ev in piece["events"]:
        start, end, measure = ev[EV_START], ev[EV_END], ev[EV_MEAS]
        if measure == 0:
            continue
        si = gnt._seg_idx_for_tick(segs, starts, start)
        if si >= 0 and si in excluded_idx:
            continue                                    # OI-184 interim: left-out span event dropped
        ferm_ctx = event_ferm_ctx(ev, ferm_off, ferm_on)
        bc = gnt._MC_INV[ev[EV_MC]]
        exact[ferm_ctx][1] += 1
        exact_bc[(bc, ferm_ctx)][1] += 1
        if start in gt_start_set:
            exact[ferm_ctx][0] += 1
            exact_bc[(bc, ferm_ctx)][0] += 1
        robust[ferm_ctx][1] += 1
        if start in robust_boundary_ticks:
            robust[ferm_ctx][0] += 1
    return {"exact": exact, "robust": robust,
            "exact_bc": {f"{bc}|{int(fc)}": v for (bc, fc), v in exact_bc.items()}}, None


def _fit(stem_counts):
    """Aggregate the 2-cell Bernoulli table with the reliability flag (count>=THRESHOLD), plus the
    beat-class-CROSSED table the decoder's boundary factor consumes (step 2)."""
    exact = {True: [0, 0], False: [0, 0]}
    robust = {True: [0, 0], False: [0, 0]}
    exact_bc = defaultdict(lambda: [0, 0])
    for sc in stem_counts:
        for cell in (True, False):
            for k in (0, 1):
                exact[cell][k] += sc["exact"][cell][k]
                robust[cell][k] += sc["robust"][cell][k]
        for key, v in sc.get("exact_bc", {}).items():
            exact_bc[key][0] += v[0]
            exact_bc[key][1] += v[1]

    def cells(tab):
        out = {}
        tot_b = tot_e = 0
        for cell, (b, e) in tab.items():
            key = "fermata_at_or_adjacent" if cell else "no_fermata_context"
            out[key] = {"boundaries": b, "events": e,
                        "prob": (b / e if e else None),
                        "reliable": e >= glt.THRESHOLD}      # count>=20 rule (gen_label_tables)
            tot_b += b
            tot_e += e
        out["_marginal"] = {"boundaries": tot_b, "events": tot_e,
                            "prob": (tot_b / tot_e if tot_e else None)}
        return out

    # the crossed table, keyed beat_class -> {fermata cell -> row}. A cell is `reliable` iff its own
    # event count >= THRESHOLD; the decoder's declared pooling parent for an unreliable cell is the
    # beat-class-only cell of note_tables_*.json (the same count>=20 rule as every other table).
    bc_out = {}
    for key, (b, e) in sorted(exact_bc.items()):
        bc, fc = key.rsplit("|", 1)
        name = "fermata_at_or_adjacent" if fc == "1" else "no_fermata_context"
        bc_out.setdefault(bc, {})[name] = {"boundaries": b, "events": e,
                                           "prob": (b / e if e else None),
                                           "reliable": e >= glt.THRESHOLD}
    return {"exact_tick": cells(exact), "robust_first_event": cells(robust),
            "exact_tick_by_beat_class": bc_out}


def main():
    fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
    covered = sorted(fa["stem_index"].keys())
    fold_of = {s: fa["stem_index"][s]["fold"] for s in covered}
    note_events = json.loads(NOTE_EVENTS.read_text(encoding="utf-8"))

    per = {}
    excluded_stems = Counter()
    for stem in covered:
        res, reason = per_stem(stem, note_events["pieces"][stem])
        if res is None:
            excluded_stems[reason] += 1
        else:
            per[stem] = res
    counted = sorted(per)

    def stem_set(name):
        if name == "all":
            return counted
        f = int(name[4:])
        return [s for s in counted if fold_of[s] != f]

    fits = {name: _fit([per[s] for s in stem_set(name)])
            for name in ["all"] + [f"fold{i}" for i in range(glt.N_FOLDS)]}

    prov = {
        "generator": glt._rel(Path(__file__)), "corpus_git_hash": glt._git_head(),
        "version": VERSION,
        "protocol": ("cowork_prefit_gates.md (OI-176/OI-177) — 5-fold grouped split, count>=20 "
                     "reliability, OI-184 exclusions + interim zero-factor span leave-out"),
        "threshold": glt.THRESHOLD, "n_folds": glt.N_FOLDS,
        "note_events_artifact": glt._rel(NOTE_EVENTS),
        "counted_stems": len(counted),
        "excluded_stems": dict(excluded_stems),
        "covariate_definition": (
            "ferm_ctx(event) = the event's own fermata flag (a sounding note carries a fermata) OR a "
            "fermata note ends at the event's start tick (the phrase-end boundary) OR a fermata note "
            "begins at the event's end tick (the approach). The boundary-factor reading of §3.8."),
        "boundary_numerator": ("exact_tick: a KEPT GT label starts at the event's start tick; "
                               "robust_first_event: the event is the first (min-start) event of a KEPT "
                               "GT segment — the same dual the note-side boundary table reports."),
        "relation_to_existing_tables": ("ADDENDUM ONLY — note_tables_*.json are NOT re-counted or "
                                        "modified; this is a separate covariate on the same events."),
        "crossed_table": ("exact_tick_by_beat_class (added at the weight fit, step 2): P(boundary | "
                          "beat class x fermata context) — the form the ratified factorization's "
                          "boundary factor names (§3 items 7+8). A cell is used by the decoder iff its "
                          "own training count >= threshold; the declared pooling parent is the "
                          "beat-class-only cell in note_tables_*.json."),
    }
    obj = {"provenance": prov, "fits": fits}
    OUT_JSON.write_text(json.dumps(obj, indent=1, sort_keys=True) + "\n", encoding="utf-8")

    a = fits["all"]
    L = ["=== fermata-conditioned boundary cells (algorithm-completion step 1) — summary ===",
         f"corpus git_hash: {prov['corpus_git_hash']}",
         f"counted stems: {len(counted)}  (excluded: {dict(excluded_stems)})",
         "",
         "P(segment boundary | fermata at/adjacent) — the ONE counted addition (all-326 fold):",
         ""]
    for variant in ("exact_tick", "robust_first_event"):
        c = a[variant]
        L.append(f"-- {variant} --")
        for key in ("fermata_at_or_adjacent", "no_fermata_context", "_marginal"):
            cc = c[key]
            p = f"{cc['prob']:.4f}" if cc["prob"] is not None else "None"
            rel = "" if key == "_marginal" else ("  [reliable]" if cc["reliable"] else "  [UNRELIABLE <20]")
            L.append(f"  {key:24s} P={p}  ({cc['boundaries']}/{cc['events']}){rel}")
        L.append("")
    L.append("P(boundary | beat class x fermata context) — the CROSSED table the decoder consumes")
    L.append("  (step 2; unreliable cell pools to the beat-class-only cell of note_tables_*.json):")
    for bc in sorted(a["exact_tick_by_beat_class"]):
        for name in ("fermata_at_or_adjacent", "no_fermata_context"):
            cc = a["exact_tick_by_beat_class"][bc].get(name)
            if cc is None:
                continue
            rel = "reliable" if cc["reliable"] else "UNRELIABLE <20 -> pooled"
            L.append(f"  {bc:13s} {name:24s} P={cc['prob']:.4f}  ({cc['boundaries']}/{cc['events']})  [{rel}]")
    L.append("")
    # per-fold P(boundary|fermata) for the exact variant (the headline cell), reproducibility view
    L.append("per training fold — P(boundary | fermata at/adjacent), exact_tick:")
    for i in range(glt.N_FOLDS):
        cc = fits[f"fold{i}"]["exact_tick"]["fermata_at_or_adjacent"]
        p = f"{cc['prob']:.4f}" if cc["prob"] is not None else "None"
        L.append(f"  fold{i}: P={p}  ({cc['boundaries']}/{cc['events']})")
    OUT_SUMMARY.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    print(f"\nwrote {glt._rel(OUT_JSON)}")


if __name__ == "__main__":
    main()
