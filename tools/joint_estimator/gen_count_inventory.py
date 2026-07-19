#!/usr/bin/env python3
"""gen_count_inventory.py — the OI-177 count-inventory instrument.

READ-ONLY / MEASUREMENT-LAYER. No src/ change, no corpus mutation, no gate change, no value
fitted, NO decision made. This aggregates RAW ground-truth counts — the count basis the OI-177
capacity budget will be checked against at the fit event (`cowork_prefit_gates.md`, user-ratified
2026-07-19). It decides NOTHING: no threshold applied, no vocabulary pooled — that happens at fit
time inside training folds per the ratified protocol. This instrument only COUNTS.

GROUND TRUTH is read ONLY through dcml_parser.load_wir_regions (the OI-142-corrected substrate)
for the 326 covered stems. Roman-numeral labels are normalized ONLY through the existing compare_rn
parsing/normalization (crn.normalise_rn / crn.split_rn / crn.extract_quality) and the applied-target
split through dcml_parser._split_rntxt_applied (the producer's own splitter that already produced
DcmlRegion.roman_numeral). NO second RN parser is written (#6). Where compare_rn's normalization
cannot express something Task B needs, the label is counted under a `raw_unnormalized` bucket and the
gap is reported — nothing is invented.

Fold keying comes from the committed Task-A artifact (fold_assignment.json).

TABLES (each keyed by fold AND totaled), per the ratified OI-177 protocol:
  (a) raw GT label histogram + normalized-class histogram (degree, quality, inversion-figure,
      applied-target), normalization rule stated in the artifact;
  (b) same-key adjacent-label transition-pair counts, per mode (major/minor of the local key);
      key-change boundaries excluded from (b), counted in (c);
  (c) key-change counts by (circle-of-fifths tonic distance, mode pair), with relative/parallel
      identifications;
  (d) entry-chord counts (the first label after each key change);
  (e) the desk-sim §4.3 sensitive cells' raw counts, by name, each with its stated label mapping;
  (f) total token counts (labels, transition pairs, key changes) per fold and overall.
EXCLUDED (deliberately): any boundary/metric-position table — gated on OI-184 (the WiR anacrusis
alignment establishment). Written into the artifact.

Usage:
    python tools/joint_estimator/gen_count_inventory.py
    python tools/joint_estimator/gen_count_inventory.py --out-json <p> --out-summary <p>
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import dcml_parser as dcml              # noqa: E402
import compare_rn as crn               # noqa: E402

WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")
FOLD_ARTIFACT = Path(__file__).resolve().parent / "fold_assignment.json"

UNPARSEABLE_STOP_PCT = 2.0             # ratified establishment check (ii)

# WiR seventh-inversion figured-bass tokens (slash-spelled) + root-position 7th.
_SEVENTH_TOKENS = ("7", "6/5", "4/3", "4/2")


def _git_head() -> str:
    out = subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                         capture_output=True, text=True, check=True)
    return out.stdout.strip()


def _rel(p) -> str:
    return Path(p).resolve().relative_to(_ROOT).as_posix()


# ── label component extraction (STATED normalization; pure reuse) ────────────

def label_components(region):
    """Extract the normalized components of one WiR region's label. Returns a dict, or None
    if the primary numeral is unparseable by compare_rn.split_rn (the `raw_unnormalized` case).

    Reuse only:
      - dcml._split_rntxt_applied : separates the applied tonicization target (V6/5/V -> V6/5, V)
                                    — the producer's own splitter (already made DcmlRegion.roman_numeral).
      - crn.normalise_rn / crn.split_rn : degree token (case = mode color) + verbatim suffix.
      - crn.extract_quality : the pinned coarse quality token (Maj/Min/Dom7/HalfDim7/Dim/... /?).

    figure = the VERBATIM suffix compare_rn.split_rn returns (the remainder after the degree
    token), NOT further parsed — so WiR's slashed figured bass ('6/5', '4/3') and the half-dim
    sigil ('/o7') are preserved here and never wrongly merged. quality is compare_rn's pinned
    coarse token, which is coarse on WiR's slashed notation (reads 'V6/5' as Maj, 'ii/o6/5' as
    Min); reported as-is per the reuse mandate, with the gap quantified in normalization_gaps."""
    raw = region.chord_symbol or ""
    primary, target = dcml._split_rntxt_applied(raw)
    norm = crn.normalise_rn(primary)
    parts = crn.split_rn(norm)
    if parts is None:
        return None
    acc, deg, suffix = parts
    return {
        "raw": raw,
        "degree": acc + deg,                        # case-preserving (mode color)
        "deg_base": deg.upper(),                     # I..VII, case-folded
        "minor_color": deg[0].islower(),
        "quality": crn.extract_quality(norm),        # pinned coarse quality
        "figure": suffix,                            # verbatim suffix (inversion / sigil)
        "target": target,                            # applied tonicization target (raw)
        "target_base": _deg_base(target),            # I..VII of the target, or ""
        "halfdim_sigil": ("/o" in primary),          # WiR half-dim spelling
    }


def _deg_base(tok: str) -> str:
    """The degree letter (I..VII, case-folded) of a bare applied-target token, via the SAME
    compare_rn parser (no second RN parser, #6). '' if the token is empty/unparseable."""
    if not tok:
        return ""
    parts = crn.split_rn(crn.normalise_rn(tok))
    return parts[1].upper() if parts else ""


def class_key(c) -> str:
    """The normalized-class key string: degree | quality | figure | target."""
    return f"{c['degree']} | {c['quality']} | {c['figure']} | {c['target']}"


def _is_seventh_figure(figure: str) -> bool:
    """True iff the verbatim figure denotes a seventh chord (root-pos '7' or a slashed
    seventh inversion). Used ONLY to quantify the extract_quality coarseness gap."""
    f = figure.replace("/o", "")   # drop the half-dim sigil before figure inspection
    if any(tok in f for tok in _SEVENTH_TOKENS):
        return True
    return f.strip() == "2"


# ── circle-of-fifths / relative-parallel helpers ────────────────────────────

def _cof_distance(a: int, b: int) -> int:
    """Circular distance on the circle of fifths between two tonic pitch classes (0..6)."""
    ca, cb = (a * 7) % 12, (b * 7) % 12
    d = abs(ca - cb)
    return min(d, 12 - d)


def _key_change_kind(ft, fmaj, tt, tmaj) -> str:
    """'parallel' | 'relative' | 'other' for a key change (from_tonic,from_major)->(to_...)."""
    if ft == tt and fmaj != tmaj:
        return "parallel"
    if fmaj and not tmaj and tt == (ft + 9) % 12:      # major -> its relative minor
        return "relative"
    if (not fmaj) and tmaj and tt == (ft + 3) % 12:    # minor -> its relative major
        return "relative"
    return "other"


# ── the count run ────────────────────────────────────────────────────────────

def run(check_stems):
    fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
    stem_index = fa["stem_index"]
    covered = sorted(stem_index.keys())
    stem_fold = {s: stem_index[s]["fold"] for s in covered}
    n_folds = fa["provenance"]["n_folds"]
    folds = list(range(n_folds))

    # per-fold + overall accumulators
    def fold_ctr():
        return {f: Counter() for f in folds}

    raw_hist = fold_ctr()
    norm_hist = fold_ctr()
    raw_unnorm = fold_ctr()
    trans_major = fold_ctr()            # same-key transitions in a major local key
    trans_minor = fold_ctr()
    trans_indeterminate = {f: 0 for f in folds}
    keychg = fold_ctr()                 # "(cofN | from->to)" histogram
    keychg_kind = {f: Counter() for f in folds}
    entry_hist = fold_ctr()

    tot_labels = {f: 0 for f in folds}
    tot_trans = {f: 0 for f in folds}
    tot_keychg = {f: 0 for f in folds}

    # sensitive cells (e): name -> {fold: count}
    sens_names = ["V6_to_vihalfdim", "vihalfdim_to_IV", "i_to_IVraised6",
                  "vi_to_appliedTo_vi", "applied_not_resolving_to_target", "V_to_vi"]
    sens = {name: {f: 0 for f in folds} for name in sens_names}

    # normalization-gap accounting
    gap_halfdim = Counter()            # '/o' labels read as non-half-dim -> raw label counts
    gap_seventh_as_triad = Counter()   # seventh-figure labels read as a triad quality

    # establishment-check region excerpts
    region_reconcile = {}

    total_labels_all = 0
    total_unparse_all = 0

    for stem in covered:
        f = stem_fold[stem]
        regs = dcml.load_wir_regions(WIR_DIR, stem)
        comps = []           # per-region: components dict OR None (unparseable)
        keys = []            # per-region: (tonic_pc, is_major) or (None, None)
        for r in regs:
            total_labels_all += 1
            tot_labels[f] += 1
            raw = r.chord_symbol or ""
            raw_hist[f][raw] += 1
            c = label_components(r)
            comps.append(c)
            keys.append(crn._dcml_key_tonic(getattr(r, "local_key", None)))
            if c is None:
                total_unparse_all += 1
                raw_unnorm[f][raw] += 1
                continue
            norm_hist[f][class_key(c)] += 1
            if c["halfdim_sigil"] and c["quality"] not in ("HalfDim", "HalfDim7"):
                gap_halfdim[raw] += 1
            if _is_seventh_figure(c["figure"]) and c["quality"] in (
                    "Maj", "Min", "Aug", "Dim", "?"):
                gap_seventh_as_triad[raw] += 1

        # transitions (b), key changes (c), entry chords (d), sensitive cells (e)
        for i in range(len(regs) - 1):
            ca, cb = comps[i], comps[i + 1]
            (ta, ma), (tb, mb) = keys[i], keys[i + 1]
            same_key = (ta is not None and tb is not None and ta == tb and ma == mb)
            if same_key:
                tot_trans[f] += 1
                if ca is not None and cb is not None:
                    pairkey = f"{class_key(ca)}  =>  {class_key(cb)}"
                    (trans_major if ma else trans_minor)[f][pairkey] += 1
                else:
                    trans_indeterminate[f] += 1
                # sensitive cells — same-key adjacent pairs only
                _score_sensitive(sens, f, ca, cb, ma)
            else:
                # key change (c) + entry chord (d)
                if ta is None or tb is None:
                    keychg[f]["(indeterminate)"] += 1
                    keychg_kind[f]["indeterminate"] += 1
                else:
                    cof = _cof_distance(ta, tb)
                    mp = f"{'major' if ma else 'minor'}->{'major' if mb else 'minor'}"
                    keychg[f][f"cof{cof} | {mp}"] += 1
                    keychg_kind[f][_key_change_kind(ta, ma, tb, mb)] += 1
                tot_keychg[f] += 1
                if cb is not None:
                    entry_hist[f][class_key(cb)] += 1
                else:
                    entry_hist[f]["(raw_unnormalized)"] += 1

        # establishment-check excerpt
        if stem in check_stems:
            seq = [(c["degree"] + c["figure"] + (("/" + c["target"]) if c["target"] else ""))
                   if c is not None else f"(raw:{regs[j].chord_symbol})"
                   for j, c in enumerate(comps)]
            region_reconcile[stem] = {
                "my_region_count": len(regs),
                "load_wir_regions_count": len(dcml.load_wir_regions(WIR_DIR, stem)),
                "fold": f,
                "first_labels": seq[:14],
                "analysis_txt_excerpt": _analysis_excerpt(stem),
            }

    unparse_pct = 100.0 * total_unparse_all / total_labels_all if total_labels_all else 0.0
    if unparse_pct > UNPARSEABLE_STOP_PCT:
        sys.exit(f"STOP: unparseable/unnormalizable label rate {unparse_pct:.3f}% exceeds "
                 f"{UNPARSEABLE_STOP_PCT}% — the count basis would be undermined. "
                 f"({total_unparse_all}/{total_labels_all} labels)")

    # ── assemble the artifact (overall = sum across folds) ──
    def overall(fc):
        agg = Counter()
        for f in folds:
            agg += fc[f]
        return agg

    def hist_block(fc, top_n=None):
        ov = overall(fc)
        blk = {
            "overall": dict(ov.most_common()),
            "by_fold": {str(f): dict(fc[f].most_common()) for f in folds},
            "distinct_overall": len(ov),
        }
        if top_n:
            blk["top"] = ov.most_common(top_n)
            blk["tail_size"] = max(0, len(ov) - top_n)
        return blk

    norm_ov = overall(norm_hist)

    artifact = {
        "provenance": {
            "generator": _rel(__file__),
            "corpus_git_hash": _git_head(),
            "fold_artifact": _rel(FOLD_ARTIFACT),
            "fold_artifact_git_hash": fa["provenance"]["corpus_git_hash"],
            "wir_dir": _rel(WIR_DIR),
            "ground_truth_substrate": "dcml_parser.load_wir_regions (OI-142-corrected)",
            "rn_normalization": (
                "primary/target split: dcml_parser._split_rntxt_applied; degree+suffix: "
                "compare_rn.normalise_rn + split_rn (degree case = mode color, suffix verbatim); "
                "quality: compare_rn.extract_quality (pinned, coarse on WiR slashed figures). "
                "normalized class = 'degree | quality | figure | target'."),
            "protocol": "cowork_prefit_gates.md (OI-177), user-ratified 2026-07-19",
        },
        "coverage_count": len(covered),
        "n_folds": n_folds,
        # (f) totals — the denominator basis for params <= tokens/10
        "totals": {
            "overall": {
                "labels": sum(tot_labels.values()),
                "transition_pairs": sum(tot_trans.values()),
                "key_changes": sum(tot_keychg.values()),
            },
            "by_fold": {str(f): {"labels": tot_labels[f],
                                 "transition_pairs": tot_trans[f],
                                 "key_changes": tot_keychg[f]} for f in folds},
        },
        # (a) raw + normalized histograms
        "raw_label_histogram": hist_block(raw_hist, top_n=15),
        "normalized_class_histogram": {
            **hist_block(norm_hist, top_n=15),
            "class_key_format": "degree | quality | figure | target",
        },
        "raw_unnormalized": {
            "rule": "compare_rn.split_rn returned None (degree unparseable, e.g. It6/Ger/Fr/N/Cad).",
            **hist_block(raw_unnorm),
            "count": total_unparse_all,
            "rate_pct": round(unparse_pct, 4),
        },
        # normalization gaps (surfaced, not fixed — #3/#12)
        "normalization_gaps": {
            "note": ("compare_rn.extract_quality is coarse on WiR's slash-spelled notation "
                     "(the pinned instrument, reused as-is). Figure info is preserved verbatim "
                     "in the class 'figure' field, so classes do NOT wrongly merge; only the "
                     "coarse 'quality' token is affected. Surfaced for Cowork; not built around."),
            "halfdim_sigil_read_as_non_halfdim": {
                "count": int(sum(gap_halfdim.values())),
                "distinct_labels": len(gap_halfdim),
                "examples": gap_halfdim.most_common(12),
            },
            "seventh_figure_read_as_triad_quality": {
                "count": int(sum(gap_seventh_as_triad.values())),
                "distinct_labels": len(gap_seventh_as_triad),
                "examples": gap_seventh_as_triad.most_common(12),
            },
        },
        # (b) transitions
        "transitions_same_key": {
            "rule": ("adjacent regions with an identical resolved local key (tonic_pc, mode); "
                     "key-change boundaries excluded (counted in key_changes). Label = the "
                     "normalized class; pair = 'from  =>  to'."),
            "major": hist_block(trans_major, top_n=15),
            "minor": hist_block(trans_minor, top_n=15),
            "indeterminate_local_key_pairs": {str(f): trans_indeterminate[f] for f in folds},
        },
        # (c) key changes
        "key_changes": {
            "rule": ("adjacent regions whose resolved local key (tonic_pc, mode) differs; "
                     "keyed by (circle-of-fifths tonic distance, from_mode->to_mode)."),
            **hist_block(keychg),
            "kind": {
                "overall": dict(overall(keychg_kind).most_common()),
                "by_fold": {str(f): dict(keychg_kind[f].most_common()) for f in folds},
            },
        },
        # (d) entry chords
        "entry_chords": {
            "rule": "the first label after each key change (the region entering the new key).",
            **hist_block(entry_hist, top_n=15),
        },
        # (e) sensitive cells
        "sensitive_cells": _sensitive_block(sens, folds),
        # excluded
        "excluded": {
            "boundary_metric_position_tables": (
                "gated on OI-184 (the WiR anacrusis beat-alignment convention must be positively "
                "established before per-beat/boundary counts are drawn); NOT counted here."),
        },
        # establishment checks
        "establishment_checks": {
            "region_reconcile": region_reconcile,
            "unparseable_rate": {
                "rate_pct": round(unparse_pct, 4),
                "stop_threshold_pct": UNPARSEABLE_STOP_PCT,
                "pass": unparse_pct <= UNPARSEABLE_STOP_PCT,
                "count": total_unparse_all,
                "labels": total_labels_all,
            },
        },
    }
    return artifact


def _score_sensitive(sens, f, ca, cb, ma):
    """Increment the desk-sim §4.3 sensitive-cell counts for a same-key adjacent (ca -> cb)
    pair (ma = local key is_major). Stated label mappings (raw label space):
      V6_to_vihalfdim  : from V (major color) figure exactly '6'; to VI (minor color) with '/o' sigil.
      vihalfdim_to_IV  : from VI (minor color) '/o' sigil; to IV (major color).
      i_to_IVraised6   : minor local key; from I (minor color = i); to IV (major color = raised 6th).
      vi_to_appliedTo_vi: from VI (minor color = vi); to any chord applied to VI (target base VI).
      applied_not_resolving_to_target: from any applied chord (target present); to a chord whose
                          degree base != that target base.
      V_to_vi          : from V (major color), not applied; to VI (any color), not applied (deceptive)."""
    if ca is None or cb is None:
        return
    # 1
    if (ca["deg_base"] == "V" and not ca["minor_color"] and ca["figure"] == "6"
            and not ca["target"] and cb["deg_base"] == "VI" and cb["minor_color"]
            and cb["halfdim_sigil"] and not cb["target"]):
        sens["V6_to_vihalfdim"][f] += 1
    # 2
    if (ca["deg_base"] == "VI" and ca["minor_color"] and ca["halfdim_sigil"] and not ca["target"]
            and cb["deg_base"] == "IV" and not cb["minor_color"] and not cb["target"]):
        sens["vihalfdim_to_IV"][f] += 1
    # 3
    if (not ma and ca["deg_base"] == "I" and ca["minor_color"] and not ca["target"]
            and cb["deg_base"] == "IV" and not cb["minor_color"] and not cb["target"]):
        sens["i_to_IVraised6"][f] += 1
    # 4
    if (ca["deg_base"] == "VI" and ca["minor_color"] and not ca["target"]
            and cb["target_base"] == "VI"):
        sens["vi_to_appliedTo_vi"][f] += 1
    # 5
    if ca["target_base"] and cb["deg_base"] and cb["deg_base"] != ca["target_base"]:
        sens["applied_not_resolving_to_target"][f] += 1
    # 6
    if (ca["deg_base"] == "V" and not ca["minor_color"] and not ca["target"]
            and cb["deg_base"] == "VI" and not cb["target"]):
        sens["V_to_vi"][f] += 1


_SENS_PREDICATES = {
    "V6_to_vihalfdim": "from V (maj color) figure exactly '6'; to VI (min color) with '/o' half-dim sigil",
    "vihalfdim_to_IV": "from VI (min color) with '/o' sigil; to IV (maj color)",
    "i_to_IVraised6": "minor local key; from i (I min color); to IV (maj color = raised 6th degree)",
    "vi_to_appliedTo_vi": "from vi (VI min color); to any chord applied to VI (target base == VI)",
    "applied_not_resolving_to_target": "from an applied chord (target present); to a chord whose degree base != target base",
    "V_to_vi": "from V (maj color), not applied; to VI (any color), not applied (deceptive)",
}


def _sensitive_block(sens, folds):
    out = {"rule": ("desk-sim §4.3 named cells; same-key adjacent raw-label pairs; each "
                    "predicate stated below (raw label space).")}
    for name, per_fold in sens.items():
        out[name] = {
            "predicate": _SENS_PREDICATES[name],
            "count_overall": sum(per_fold.values()),
            "by_fold": {str(f): per_fold[f] for f in folds},
        }
    return out


def _analysis_excerpt(stem):
    """First few measure lines of the stem's analysis.txt (eyeball check, read-only)."""
    path = dcml.find_wir_file(WIR_DIR, stem)
    if not path:
        return []
    lines = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if s.startswith("m") and not s.startswith("Note:"):
            lines.append(s)
        if len(lines) >= 6:
            break
    return lines


def main():
    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    ap.add_argument("--out-json", default=str(here / "count_inventory.json"))
    ap.add_argument("--out-summary", default=str(here / "count_inventory_summary.txt"))
    args = ap.parse_args()

    if not FOLD_ARTIFACT.exists():
        sys.exit(f"STOP: fold artifact not found ({FOLD_ARTIFACT}); run gen_fold_assignment.py first.")

    fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
    covered = sorted(fa["stem_index"].keys())
    check_stems = ["bwv110.7"] + [s for s in ("bwv10.7", "bwv40.3", "bwv244.3") if s in covered]
    check_stems = [s for s in check_stems if s in covered][:4]

    artifact = run(check_stems)

    Path(args.out_json).write_text(json.dumps(artifact, indent=1, ensure_ascii=False) + "\n",
                                   encoding="utf-8")
    _write_summary(Path(args.out_summary), artifact)
    print(f"Wrote {args.out_json} and {args.out_summary}")
    t = artifact["totals"]["overall"]
    print(f"  labels={t['labels']} transition_pairs={t['transition_pairs']} "
          f"key_changes={t['key_changes']}")
    print(f"  normalized classes distinct={artifact['normalized_class_histogram']['distinct_overall']}; "
          f"unparseable={artifact['raw_unnormalized']['rate_pct']}%")


def _write_summary(path, a):
    L = []
    L.append("=== OI-177 count inventory — generated summary ===")
    L.append(f"corpus git_hash: {a['provenance']['corpus_git_hash']}")
    L.append(f"coverage: {a['coverage_count']} stems, {a['n_folds']} folds")
    t = a["totals"]["overall"]
    L.append(f"TOTALS  labels={t['labels']}  transition_pairs={t['transition_pairs']}  "
             f"key_changes={t['key_changes']}")
    L.append("  per fold: " + ", ".join(
        f"f{f}(lab={v['labels']},tr={v['transition_pairs']},kc={v['key_changes']})"
        for f, v in a["totals"]["by_fold"].items()))
    L.append("")
    L.append(f"(a) normalized classes distinct = {a['normalized_class_histogram']['distinct_overall']}; "
             f"raw labels distinct = {a['raw_label_histogram']['distinct_overall']}")
    L.append("    top 15 normalized classes:")
    for k, n in a["normalized_class_histogram"]["top"]:
        L.append(f"      {n:6d}  {k}")
    L.append(f"    tail (classes beyond top 15): {a['normalized_class_histogram']['tail_size']}")
    L.append("")
    L.append(f"raw_unnormalized: {a['raw_unnormalized']['count']} labels "
             f"({a['raw_unnormalized']['rate_pct']}%)  {dict(list(a['raw_unnormalized']['overall'].items()))}")
    g = a["normalization_gaps"]
    L.append(f"normalization gaps: halfdim-sigil-coarse={g['halfdim_sigil_read_as_non_halfdim']['count']}, "
             f"seventh-as-triad={g['seventh_figure_read_as_triad_quality']['count']}")
    L.append("")
    L.append("(b) transitions same-key: "
             f"major distinct={a['transitions_same_key']['major']['distinct_overall']}, "
             f"minor distinct={a['transitions_same_key']['minor']['distinct_overall']}")
    L.append("(c) key changes by kind (overall): " + str(a["key_changes"]["kind"]["overall"]))
    L.append("(d) entry chords distinct = " + str(a["entry_chords"]["distinct_overall"]))
    L.append("")
    L.append("(e) sensitive cells (desk-sim §4.3) — raw counts:")
    for name, pred in _SENS_PREDICATES.items():
        cell = a["sensitive_cells"][name]
        L.append(f"    {name:34s} count={cell['count_overall']:5d}   [{pred}]")
    L.append("")
    L.append(f"(ii) unparseable rate {a['establishment_checks']['unparseable_rate']['rate_pct']}% "
             f"(threshold {a['establishment_checks']['unparseable_rate']['stop_threshold_pct']}%) "
             f"-> {'PASS' if a['establishment_checks']['unparseable_rate']['pass'] else 'FAIL'}")
    L.append("EXCLUDED: boundary/metric-position tables (gated on OI-184).")
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
