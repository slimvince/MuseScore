#!/usr/bin/env python3
"""gen_factor_presence.py — the chord-factor presence table (option 3a; the fitted-table probe
finding 3). Dispatch: `cc_instruction_secondary_dominant_refit.md` (Cowork 2026-07-19), executing
`cowork_sensitive_cell_probe.md` finding 3 (user-ratified 2026-07-19).

READ-ONLY / FIT-LAYER-OWNED. No src/ change, no corpus mutation, no gate change, NO DECODING, NO
EVALUATION, no accuracy metric consulted (the DT-2 firewall — grep-provable: no import of
a8_rebaseline_measure / compare_analyses grading / robust_stop_diff / any decoder). It counts, over
the committed note-event data + the SAME ground-truth segment alignment and exclusions as the part-2
note-side fit, how often each factor of a humanly-labeled chord actually SOUNDS in its segment.

THE TABLE:  P(factor sounds | factor role, chord family)
  factor role  = root | third | fifth | seventh   (seventh only for seventh chords)
  chord family = triad | seventh                   (triad has 3 factor roles, seventh 4)
So 7 cells: (root|triad)(third|triad)(fifth|triad) + (root|seventh)(third|seventh)(fifth|seventh)
(seventh|seventh). Per training fold + all-326, exactly as the other tables.

WHY it exists (finding 3): when the estimator weighs a candidate chord for a segment, a chord tone
that FAILS to sound (an incomplete chord — e.g. a dominant seventh whose third is silent) needs a
counted penalty. The desk simulation used an INVENTED placeholder (0.35). This replaces it with the
corpus frequency, per factor. Per-factor counting encodes the asymmetry automatically: a silent
seventh nearly never earns a seventh-chord label (so its penalty is near-prohibitive), while the
fifth is the factor four-part writing routinely omits (so its penalty is mild).

GENRE SCOPE (dispatch / probe §3, verbatim intent): all counted values are Bach-chorale values —
the only repertoire we hold ground truth for. For jazz, where omitting the fifth or even the root
from a voicing is normal practice, these frequencies would be wrong and no jazz values can be counted
because no jazz ground truth exists (register item 7 — jazz correctness claims stay de-scoped; the
style-adaptation pattern is: same table STRUCTURE, values re-counted per style, only when that gate
is passed). The reliability claim is scoped to the chorale corpus and claims nothing beyond it.

REUSE (#6): gen_note_tables.gt_segments (the part-2 GT-segment alignment — one reader),
gen_note_tables.chord_factor_pcs (the ordered factor pcs, sharing member_pcs's framework/root
derivation), gen_note_tables.{FLAGGED,MULTIMETER,COUNTED_METERS} (the part-2 exclusion gate),
gen_label_tables.{THRESHOLD,ALPHA,N_FOLDS,_git_head,_rel}, the committed note_events.json substrate,
fold_assignment.json. No new normalizer, no new template, no new key reduction.

Usage:
    python tools/joint_estimator/gen_factor_presence.py
    python tools/joint_estimator/gen_factor_presence.py --out-dir <scratch>   # reproducibility check
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_ROOT / "tools" / "joint_estimator"))

import gen_note_tables as gnt            # noqa: E402  (gt_segments, chord_factor_pcs, exclusion gate)
import gen_label_tables as glt           # noqa: E402  (THRESHOLD, ALPHA, N_FOLDS, _git_head, _rel)

NOTE_EVENTS = _ROOT / "tools" / "joint_estimator" / "note_events" / "note_events.json"
FOLD_ARTIFACT = _ROOT / "tools" / "joint_estimator" / "fold_assignment.json"
OUT_DIR_DEFAULT = _ROOT / "tools" / "joint_estimator"

THRESHOLD = glt.THRESHOLD
ALPHA = glt.ALPHA
N_FOLDS = glt.N_FOLDS
FIT_VERSION = "factor-presence-v1 (option 3a; P(factor sounds | role, family))"

# The two note->segment membership definitions, both reported (like part-2's exact vs robust
# boundary). PRIMARY = 'overlap' ("sounds during the segment": a factor held over from the previous
# chord still sounds and counts). CROSS-CHECK = 'onset' (part-2's onset-in-segment assignment).
MODES = ("overlap", "onset")
PRIMARY_MODE = "overlap"

ROLES = ("root", "third", "fifth", "seventh")

GENRE_SCOPE = (
    "Bach-chorale values only. These are counts over the 326 annotated Bach chorales (When-in-Rome "
    "ground truth), the only repertoire we hold ground truth for. For jazz — where omitting the fifth "
    "or even the root from a voicing is normal practice — these frequencies would be wrong, and no "
    "jazz values can be counted because no jazz ground truth exists (register item 7; the "
    "style-adaptation pattern is: same table STRUCTURE, values re-counted per style, only when a jazz "
    "ground-truth gate is passed). The reliability claim is scoped to this corpus and claims nothing "
    "beyond it.")


def sounding_pcs(piece, start, end, mode):
    """The set of pitch classes sounding in segment [start,end). 'overlap': notes whose sounding
    interval [onset, onset+dur) overlaps the segment (a held-over factor still sounds). 'onset':
    notes whose onset falls in the segment (part-2's onset-in-span assignment). Measure-0 (anacrusis)
    notes are excluded in both — the same exclusion as part 2."""
    pcs = set()
    for n in piece["notes"]:
        onset, dur, pc = n[0], n[1], n[2]
        if n[6] == 0:                       # OI-184 (a): anacrusis notes excluded (part-2 convention)
            continue
        if mode == "overlap":
            if onset < end and onset + dur > start:
                pcs.add(pc)
        else:                               # onset-in-segment
            if start <= onset < end:
                pcs.add(pc)
    return pcs


def per_stem_counts(stem, piece):
    """Per-segment factor-presence counts for one stem, or (None, reason) for an excluded stem. The
    exclusion gate is IDENTICAL to gen_note_tables.per_stem_counts (flagged / multi-meter / meter not
    in {4/4,3/4}); m0 segments are already dropped by gt_segments."""
    if stem in gnt.FLAGGED:
        return None, "flagged"
    if stem in gnt.MULTIMETER or piece["multi_meter"]:
        return None, "multi_meter"
    meter = tuple(piece["meter"]) if piece["meter"] else None
    if meter not in gnt.COUNTED_METERS:
        return None, "meter_not_counted"

    segs = gnt.gt_segments(stem)
    # counts[mode][(role, family)] = [present, total]
    counts = {m: defaultdict(lambda: [0, 0]) for m in MODES}
    diag = Counter()
    # alignment diagnostic (PRIMARY mode): #-factors-present distribution per family (a segment with
    # ZERO factors present is a GT-tick MISALIGNMENT signature — the span holds a different chord; the
    # OI-184 / part-2 anomaly-1 jitter), and the seventh's presence conditioned on the triad being
    # complete (a well-aligned segment). Reported beside the raw table, never used to adjust it.
    factor_dist = {"triad": Counter(), "seventh": Counter()}     # #present -> segment count
    seventh_align = {"any": [0, 0], "triad_complete": [0, 0]}    # [seventh_absent, total]
    for s in segs:
        if s["tonic"] is None or s["is_major"] is None:
            diag["seg_indeterminate_key"] += 1
            continue
        factors = gnt.chord_factor_pcs(s["cls"], s["tonic"], s["is_major"])
        if factors is None:
            cls = s["cls"]
            if cls.raw_unnormalized:
                diag["seg_raw_unnormalized"] += 1
            elif cls.quality in ("AugSixth", "Neapolitan"):
                diag["seg_chromatic_class"] += 1
            elif cls.target and "/" in cls.target:
                diag["seg_multilevel_applied"] += 1
            else:
                diag["seg_unmapped_quality"] += 1
            continue
        family = "seventh" if len(factors) == 4 else "triad"
        diag[f"seg_{family}"] += 1
        snd = {m: sounding_pcs(piece, s["start"], s["end"], m) for m in MODES}
        for role, pc in factors:
            cell = f"{role}|{family}"
            for m in MODES:
                counts[m][cell][1] += 1
                if pc in snd[m]:
                    counts[m][cell][0] += 1
        # alignment diagnostic on the PRIMARY mode
        po = snd[PRIMARY_MODE]
        present_roles = [r for r, pc in factors if pc in po]
        factor_dist[family][len(present_roles)] += 1
        if family == "seventh":
            others = sum(1 for r, pc in factors if r != "seventh" and pc in po)
            sev_present = any(pc in po for r, pc in factors if r == "seventh")
            seventh_align["any"][1] += 1
            seventh_align["any"][0] += (0 if sev_present else 1)
            if others == 3:                                     # root+third+fifth all present
                seventh_align["triad_complete"][1] += 1
                seventh_align["triad_complete"][0] += (0 if sev_present else 1)
    return {"counts": {m: dict(counts[m]) for m in MODES}, "diag": diag,
            "factor_dist": {f: dict(factor_dist[f]) for f in factor_dist},
            "seventh_align": seventh_align}, None


def _cell_stat(present, total):
    """Bernoulli presence for one (role, family) cell. Raw MLE reported; the STORED probability is
    additive-alpha smoothed over {present, absent} (the ratified alpha=1) so P(absent) — the
    missing-tone penalty basis — is never zero (finding-2 option-2c is fatal). reliable = total>=20
    (the unchanged reliability rule; a Bernoulli has no pooling parent, so a <20 cell is REPORTED)."""
    p_mle = present / total if total else None
    p_pres = (present + ALPHA) / (total + 2 * ALPHA) if total else None
    return {
        "present": present, "total": total,
        "p_present_mle": p_mle,
        "p_present_smoothed": p_pres,
        "p_absent_smoothed": (1.0 - p_pres) if p_pres is not None else None,
        "reliable": total >= THRESHOLD,
    }


def fit_presence(stem_counts):
    """Aggregate per-stem counts and build the presence table (per mode) + the alignment diagnostic."""
    agg = {m: defaultdict(lambda: [0, 0]) for m in MODES}
    diag = Counter()
    factor_dist = {"triad": Counter(), "seventh": Counter()}
    seventh_align = {"any": [0, 0], "triad_complete": [0, 0]}
    for sc in stem_counts:
        for m in MODES:
            for cell, (p, t) in sc["counts"][m].items():
                agg[m][cell][0] += p
                agg[m][cell][1] += t
        diag.update(sc["diag"])
        for f in factor_dist:
            for k, v in sc["factor_dist"][f].items():
                factor_dist[f][k] += v
        for k in seventh_align:
            seventh_align[k][0] += sc["seventh_align"][k][0]
            seventh_align[k][1] += sc["seventh_align"][k][1]
    table = {}
    for m in MODES:
        table[m] = {cell: _cell_stat(agg[m][cell][0], agg[m][cell][1])
                    for cell in sorted(agg[m])}

    def _rate(pair):
        absent, total = pair
        return {"seventh_absent": absent, "total": total,
                "P_seventh_present": (1 - absent / total) if total else None}
    zero_present = {f: factor_dist[f].get(0, 0) for f in factor_dist}
    fam_tot = {f: sum(factor_dist[f].values()) for f in factor_dist}
    alignment = {
        "factors_present_distribution": {f: dict(sorted(factor_dist[f].items())) for f in factor_dist},
        "zero_factors_present_misalignment": {
            f: {"count": zero_present[f], "total": fam_tot[f],
                "frac": (zero_present[f] / fam_tot[f]) if fam_tot[f] else None} for f in factor_dist},
        "seventh_presence_any": _rate(seventh_align["any"]),
        "seventh_presence_when_triad_complete": _rate(seventh_align["triad_complete"]),
        "note": ("a segment with ZERO of its factors sounding is a GT-tick MISALIGNMENT signature "
                 "(the span holds a different chord — the OI-184 / part-2 anomaly-1 jitter), NOT a "
                 "musical incomplete chord. The raw table counts every kept segment (the fact, "
                 "unadjusted); this diagnostic quantifies the alignment floor so the raw rates are "
                 "interpreted correctly. 'seventh_presence_when_triad_complete' is the seventh's "
                 "presence among well-aligned seventh segments (root+third+fifth all sounding)."),
    }
    return {"table": table, "diagnostics": dict(diag), "alignment_diagnostic": alignment}


def sanity(table_primary):
    """The two user-stated expectations (dispatch): the seventh's presence in seventh-chord segments
    is near 1; the fifth is the most-omitted factor. Reported, never used to adjust anything."""
    def mle(cell):
        v = table_primary.get(cell)
        return v["p_present_mle"] if v else None

    seventh = mle("seventh|seventh")
    per_family = {}
    for fam in ("triad", "seventh"):
        pres = {r: mle(f"{r}|{fam}") for r in ("root", "third", "fifth")}
        omitted = min((v for v in pres.values() if v is not None), default=None)
        most_omitted_role = min((r for r in pres if pres[r] is not None),
                                key=lambda r: pres[r], default=None)
        per_family[fam] = {"presence": pres, "most_omitted_role": most_omitted_role,
                           "fifth_is_most_omitted": most_omitted_role == "fifth"}
    return {
        "seventh_presence_in_seventh_chords": seventh,
        "seventh_near_one": (seventh is not None and seventh >= 0.95),
        "per_family_omission": per_family,
        "fifth_is_most_omitted_triad": per_family["triad"]["fifth_is_most_omitted"],
        "fifth_is_most_omitted_seventh": per_family["seventh"]["fifth_is_most_omitted"],
    }


def _write(path, obj):
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n",
                    encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(OUT_DIR_DEFAULT))
    args = ap.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
    covered = sorted(fa["stem_index"].keys())
    fold_of = {s: fa["stem_index"][s]["fold"] for s in covered}
    note_events = json.loads(NOTE_EVENTS.read_text(encoding="utf-8"))

    per_stem = {}
    excluded = defaultdict(list)
    for stem in covered:
        res, reason = per_stem_counts(stem, note_events["pieces"][stem])
        if res is None:
            excluded[reason].append(stem)
        else:
            per_stem[stem] = res
    counted_stems = sorted(per_stem)

    def stem_set(name):
        if name == "all":
            return counted_stems
        f = int(name[4:])
        return [s for s in counted_stems if fold_of[s] != f]

    fits = {}
    for name in ["all"] + [f"fold{i}" for i in range(N_FOLDS)]:
        stems = stem_set(name)
        fits[name] = {"fit": fit_presence([per_stem[s] for s in stems]), "n_stems": len(stems)}

    # reliability: every cell must clear the count>=20 rule; a sub-threshold cell is a reportable
    # finding (the unchanged reliability rule). None expected — all cells carry thousands.
    sub_threshold = {}
    for name, fd in fits.items():
        bad = [(m, cell) for m in MODES for cell, v in fd["fit"]["table"][m].items()
               if not v["reliable"]]
        if bad:
            sub_threshold[name] = bad

    san = sanity(fits["all"]["fit"]["table"][PRIMARY_MODE])

    prov = {
        "generator": glt._rel(Path(__file__)),
        "corpus_git_hash": glt._git_head(),
        "fit_version": FIT_VERSION,
        "protocol": "cowork_prefit_gates.md (OI-176/OI-177), user-ratified 2026-07-19",
        "ratified_probe_finding": "cowork_sensitive_cell_probe.md finding 3, option 3a (2026-07-19)",
        "note_events_artifact": glt._rel(NOTE_EVENTS),
        "gt_segment_alignment": "gen_note_tables.gt_segments (compare_analyses._dcml_time_spans, part-2, untouched)",
        "factor_pcs": "gen_note_tables.chord_factor_pcs (shares member_pcs framework/root derivation)",
        "constants": {"threshold": THRESHOLD, "alpha": ALPHA, "n_folds": N_FOLDS},
        "membership_definitions": {
            "overlap": "PRIMARY — a factor sounds if a note's [onset,onset+dur) overlaps the segment "
                       "(a factor held over from the previous chord still sounds).",
            "onset": "CROSS-CHECK — part-2's onset-in-segment assignment.",
        },
        "smoothing_note": ("stored p_present_smoothed = (present+alpha)/(total+2*alpha) with the "
                           "ratified alpha=1, so P(absent) — the missing-tone penalty basis — is never "
                           "zero (finding-2 option-2c, a zero probability, is fatal to the decode). "
                           "p_present_mle is the raw corpus frequency, reported beside it."),
        "exclusions_same_as_part2": "flagged (7) + multi-meter (bwv304,bwv362) + meter not in {4/4,3/4}; m0 segments dropped",
        "GENRE_SCOPE": GENRE_SCOPE,
    }

    for name in ["all"] + [f"fold{i}" for i in range(N_FOLDS)]:
        obj = {"provenance": dict(prov, fit_scope=name, n_training_stems=fits[name]["n_stems"]),
               "factor_presence_table": fits[name]["fit"]["table"],
               "primary_mode": PRIMARY_MODE}
        _write(out_dir / f"factor_presence_{name}.json", obj)

    inventory = {
        "purpose": ("the chord-factor presence table (option 3a): P(factor sounds | role, family) "
                    "per training fold + all-326; the counted replacement for the desk-sim missing-"
                    "tone placeholder. Bach-chorale scope (declared)."),
        "provenance": prov,
        "counted_population": {
            "counted_stems": len(counted_stems),
            "excluded_counts": {k: len(v) for k, v in excluded.items()},
            "excluded": {k: sorted(v) for k, v in excluded.items()},
            "all326_segment_diagnostics": fits["all"]["fit"]["diagnostics"],
        },
        "primary_mode": PRIMARY_MODE,
        "reliability_all_cells_pass": not sub_threshold,
        "sub_threshold_cells": sub_threshold,
        "all326_table": fits["all"]["fit"]["table"],
        "per_fold_table": {name: fits[name]["fit"]["table"]
                           for name in [f"fold{i}" for i in range(N_FOLDS)]},
        "alignment_diagnostic_all326": fits["all"]["fit"]["alignment_diagnostic"],
        "sanity_expectations": san,
    }
    _write(out_dir / "factor_presence_inventory.json", inventory)
    _write_summary(out_dir / "factor_presence_inventory_summary.txt", inventory, fits, san)

    print(f"wrote factor_presence_*.json (6 fits) + inventory (+summary) to {out_dir}")
    print(f"counted stems: {len(counted_stems)}  excluded: "
          + "{" + ", ".join(f"{k}:{len(v)}" for k, v in excluded.items()) + "}")
    print(f"reliability all cells pass (>=20): {not sub_threshold}")
    print(f"seventh presence (seventh chords): {san['seventh_presence_in_seventh_chords']}  "
          f"near_one={san['seventh_near_one']}")
    print(f"fifth most-omitted: triad={san['fifth_is_most_omitted_triad']} "
          f"seventh={san['fifth_is_most_omitted_seventh']}")


def _write_summary(path, inv, fits, san):
    L = ["=== chord-factor presence table (option 3a) — summary ===",
         f"corpus git_hash: {inv['provenance']['corpus_git_hash']}",
         f"GENRE SCOPE: {inv['provenance']['GENRE_SCOPE']}",
         f"counted stems: {inv['counted_population']['counted_stems']}  "
         f"excluded: {inv['counted_population']['excluded_counts']}",
         f"reliability all cells >=20: {inv['reliability_all_cells_pass']}",
         "",
         f"-- P(factor sounds | role, family), all-326, PRIMARY mode '{inv['primary_mode']}' --",
         f"  {'cell':18s} {'present':>8s} {'total':>7s} {'P(mle)':>8s} {'P(smoothed)':>12s} {'P(absent)':>10s}"]
    tbl = fits["all"]["fit"]["table"][inv["primary_mode"]]
    order = ["root|triad", "third|triad", "fifth|triad",
             "root|seventh", "third|seventh", "fifth|seventh", "seventh|seventh"]
    for cell in order:
        if cell not in tbl:
            continue
        v = tbl[cell]
        L.append(f"  {cell:18s} {v['present']:8d} {v['total']:7d} {v['p_present_mle']:8.4f} "
                 f"{v['p_present_smoothed']:12.4f} {v['p_absent_smoothed']:10.4f}")
    L += ["",
          "-- cross-check mode 'onset' (part-2 onset-in-segment) --",
          f"  {'cell':18s} {'P(mle)':>8s}"]
    tbl2 = fits["all"]["fit"]["table"]["onset"]
    for cell in order:
        if cell in tbl2:
            L.append(f"  {cell:18s} {tbl2[cell]['p_present_mle']:8.4f}")
    L += ["",
          "-- sanity (user expectations; reported, never adjusted) --",
          f"  seventh presence in seventh chords = {san['seventh_presence_in_seventh_chords']:.4f}  "
          f"(near 1: {san['seventh_near_one']})"]
    for fam in ("triad", "seventh"):
        pf = san["per_family_omission"][fam]
        pres = "  ".join(f"{r}={pf['presence'][r]:.4f}" for r in ("root", "third", "fifth")
                         if pf["presence"][r] is not None)
        L.append(f"  {fam:8s}: {pres}  -> most-omitted={pf['most_omitted_role']} "
                 f"(fifth_is_most_omitted={pf['fifth_is_most_omitted']})")
    ad = fits["all"]["fit"]["alignment_diagnostic"]
    L += ["",
          "-- alignment diagnostic (interprets the raw rates; NOT an adjustment) --",
          f"  zero-factors-present (misalignment signature): "
          f"triad {ad['zero_factors_present_misalignment']['triad']['count']}"
          f"/{ad['zero_factors_present_misalignment']['triad']['total']} "
          f"({ad['zero_factors_present_misalignment']['triad']['frac']:.4f}), "
          f"seventh {ad['zero_factors_present_misalignment']['seventh']['count']}"
          f"/{ad['zero_factors_present_misalignment']['seventh']['total']} "
          f"({ad['zero_factors_present_misalignment']['seventh']['frac']:.4f})",
          f"  factors-present distribution triad:  {ad['factors_present_distribution']['triad']}",
          f"  factors-present distribution seventh:{ad['factors_present_distribution']['seventh']}",
          f"  P(seventh present | any seventh seg)          = {ad['seventh_presence_any']['P_seventh_present']:.4f}",
          f"  P(seventh present | triad complete/aligned)   = {ad['seventh_presence_when_triad_complete']['P_seventh_present']:.4f}"]
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
