#!/usr/bin/env python3
"""calibration_fit.py — Stage-5 Phase 3 Task A: fit Class-M -> Class-P reliability maps.

MEASUREMENT + ARTIFACT ONLY. No behaviour change: reads the C1 substrate (regenerated on
the current corpus) and fits monotone maps from a layer's PUBLISHED Class-M boundary
confidence to empirical correctness, per (layer x decision x carrier). Maps are FITTED on
the fitting split (registry), VALIDATED on the held-out split. The held-out post-map ECE is
the honesty number.

Scope (constraint 4c / A-7): fitted for the idiom-#2 target, delivered via the Baroque and
Default carriers. The Jazz carrier gets NO map (fitting a Jazz map on Bach data would
mislabel the style axis) — it stays Class M with the A-7 "empirically-unvalidated" mark.

Rows (design §4.5 dispositions):
  L3 key sequence margin (squashed x/(x+1))  — correctness = A-8 key respect   [FIT]
  L4 chord composite (native [0,1])          — correctness = A-8 root respect  [FIT]
  (L5 combinedBoundary / cadence tonicVote / L1.5 texture — DEFERRED, re-verified elsewhere)

Shape rule (design §4.5.1): isotonic regression is the default; a Platt sigmoid ONLY where
the isotonic fit is near-logistic (smooth) AND the sigmoid does not generalize worse. The
choice is recorded per row.

Reuses c1_reliability.py primitives verbatim (which reuse the ratified A-8 cell loop).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import c1_reliability as c1        # noqa: E402  (reuse cell-join primitives + squash + PRESETS)
import compare_analyses as cmp     # noqa: E402
import characterise_bir_false as cbf  # noqa: E402  (validate_corpus_dir — OI-129 anti-contamination guard)

CARRIERS = ["baroque", "default"]  # idiom-#2 carriers; Jazz excluded (A-7)
SPLIT_REGISTRY = _ROOT / "tools" / "stage5_split_registry.json"

IDIOM2_LABEL = "idiom-#2 (Baroque common-practice); WiR/DCML-adjudicated fitting pool"
LICENSE_LINE = ("C1 substrate is WiR-adjudicated (DCML When-in-Rome) = the licensed fitting pool; "
                "music21 is corroboration only, never GT (contract C1 / feedback_ground_truth).")


def _load_splits():
    reg = json.loads(SPLIT_REGISTRY.read_text(encoding="utf-8"))
    return {stem: v["split"] for stem, v in reg["scores"].items()}


def _corpus_git_hash(preset):
    mani = _ROOT / "tools" / "corpus" / preset / "corpus_manifest.json"
    try:
        return json.loads(mani.read_text(encoding="utf-8")).get("git_hash", "?")
    except (OSError, ValueError, KeyError, TypeError):
        return "?"


# ── per-cell collectors (mirror c1_reliability's measure_l3 / measure_l4_l5, split-tagged) ──

def collect_l3(preset, km_dir, splits):
    """-> list of (squashed_margin, key_correct, w, split)."""
    corpus_dir = _ROOT / "tools" / "corpus" / preset
    out = []
    for ours_path in sorted(corpus_dir.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours", "")
        split = splits.get(stem)
        if split is None:
            continue
        wir = c1._load_wir(stem)
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
        pg, region_start = c1.cells_with_region_conf(stem, ours, wir, m21, conf_by_start)
        for cell, rs in zip(pg.cells, region_start):
            if rs is None or rs not in conf_by_start:
                continue
            kv = cell["key_verdict"]
            if kv in ("keyfail", "dcml_keyfail"):
                continue
            correct = 1.0 if kv == "agree" else 0.0
            margin, _sig = conf_by_start[rs]
            out.append((c1.squash(margin, c1.SQUASH_K_L3_MARGIN), correct, cell["w"], split))
    return out


def collect_l4(preset, fs_dir, splits):
    """-> list of (composite, root_correct, w, split)."""
    corpus_dir = _ROOT / "tools" / "corpus" / preset
    out = []
    for fs_path in sorted(Path(fs_dir).glob("*.ours.json")):
        stem = fs_path.stem.replace(".ours", "")
        if stem == "corpus_manifest":
            continue
        split = splits.get(stem)
        if split is None:
            continue
        wir = c1._load_wir(stem)
        if not wir:
            continue
        try:
            _, ours = cmp.load_analysis(fs_path)
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
        raw = json.loads(fs_path.read_text(encoding="utf-8"))
        conf_by_start = {r["startTick"]: r.get("l4Composite", 0.0) for r in raw.get("regions", [])}
        pg, region_start = c1.cells_with_region_conf(stem, ours, wir, m21, conf_by_start)
        for cell, rs in zip(pg.cells, region_start):
            if rs is None or rs not in conf_by_start:
                continue
            comp = min(max(conf_by_start[rs], 0.0), 1.0)
            out.append((comp, 1.0 if cell["root_agree"] else 0.0, cell["w"], split))
    return out


# ── ECE / curve diagnostics on a pair list (reuse c1's binner) ─────────────────────

def diag_of(pairs3):
    """pairs3: (conf, correct, w). Returns c1 curve diagnostics dict."""
    rows, tw = c1.bin_curve(pairs3)
    return c1.curve_diagnostics(rows, tw), rows, tw


def split_pairs(cells, split):
    return [(c, y, w) for (c, y, w, s) in cells if s == split]


# ── fitters ────────────────────────────────────────────────────────────────────────

def fit_isotonic(fit_pairs):
    X = np.array([p[0] for p in fit_pairs], float)
    y = np.array([p[1] for p in fit_pairs], float)
    w = np.array([p[2] for p in fit_pairs], float)
    iso = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip", increasing=True)
    iso.fit(X, y, sample_weight=w)
    return iso


def fit_platt(fit_pairs):
    X = np.array([[p[0]] for p in fit_pairs], float)
    y = np.array([p[1] for p in fit_pairs], float)
    w = np.array([p[2] for p in fit_pairs], float)
    # near-unregularized logistic == Platt scaling P=sigmoid(a*x+b)
    lr = LogisticRegression(C=1e6, solver="lbfgs", max_iter=10000)
    lr.fit(X, y, sample_weight=w)
    a = float(lr.coef_[0][0]); b = float(lr.intercept_[0])
    return lr, a, b


def apply_map(mapper, pairs3):
    X = np.array([p[0] for p in pairs3], float).reshape(-1, 1)
    if isinstance(mapper, IsotonicRegression):
        pred = mapper.predict(X.ravel())
    else:
        pred = mapper.predict_proba(X)[:, 1]
    return [(float(pv), y, w) for pv, (_, y, w) in zip(pred, pairs3)]


def curve_at(mapper, grid):
    X = np.array(grid, float).reshape(-1, 1)
    if isinstance(mapper, IsotonicRegression):
        return list(map(float, mapper.predict(X.ravel())))
    return list(map(float, mapper.predict_proba(X)[:, 1]))


# ── OI-133(c) / #19 — the two genuinely LOAD-BEARING fitting gates in this instrument. ──────────
# Unlike the bucket edges in analyze_inversion_errors (which grade nothing), these two DECIDE the
# committed calibration maps: MIN_* decides whether a row is fitted AT ALL, and NEAR_LOGISTIC_TOL
# decides whether that row ships a Platt curve or an isotonic one. They are hand-set, and the
# hygiene sweep of 2026-07-13 did NOT establish them — saying so plainly rather than inventing a
# derivation after the fact.
#
# WHAT AN ESTABLISHMENT WOULD TAKE (the concrete gate on the OI-133(c) row; neither is a desk
# exercise, which is why neither was forced here):
#   MIN_FITTING_CELLS / MIN_HELD_OUT_CELLS — a minimum-sample-size question. Establish by sweeping
#     the two counts and measuring held-out ECE variance across resamples: the right floor is where
#     the fitted curve stops moving under resampling. Today's 50/20 is a rule of thumb.
#   NEAR_LOGISTIC_TOL — "the isotonic and Platt curves agree closely enough that the smoother,
#     lower-variance parametric fit is preferred." 0.05 is a probability distance (5 points), of
#     the same order as the ECE it is protecting, but it was not derived FROM it. Establish by
#     showing the held-out ECE is insensitive to the choice across the band where the two curves
#     are within tolerance — i.e. that the tie-break cannot cost calibration quality.
# Both are RECORDED as unestablished (#19: an instrument constant is trusted only once positively
# established, never merely because it has not misbehaved). Changing either re-fits the committed
# maps, so any change is a re-baseline event, not a sweep.
MIN_FITTING_CELLS = 50      # [hand-set; NOT established — see above]
MIN_HELD_OUT_CELLS = 20     # [hand-set; NOT established — see above]
NEAR_LOGISTIC_TOL = 0.05    # [hand-set; NOT established — see above]


def fit_row(name, layer, decision, conf_name, carrier, cells, squash_note):
    fit_pairs = split_pairs(cells, "fitting")
    hel_pairs = split_pairs(cells, "held_out")
    if len(fit_pairs) < MIN_FITTING_CELLS or len(hel_pairs) < MIN_HELD_OUT_CELLS:
        return None, f"  [{name} / {carrier}] INSUFFICIENT cells (fit={len(fit_pairs)} hel={len(hel_pairs)})"

    # pre-map diagnostics
    pre_fit_d, _, _ = diag_of(fit_pairs)
    pre_hel_d, _, _ = diag_of(hel_pairs)

    iso = fit_isotonic(fit_pairs)
    lr, a, b = fit_platt(fit_pairs)

    iso_post_fit = diag_of(apply_map(iso, fit_pairs))[0]
    iso_post_hel = diag_of(apply_map(iso, hel_pairs))[0]
    pl_post_fit = diag_of(apply_map(lr, fit_pairs))[0]
    pl_post_hel = diag_of(apply_map(lr, hel_pairs))[0]

    # near-logistic test: max |isotonic - platt| over a fine grid on [0,1]
    grid = [i / 100.0 for i in range(101)]
    iso_g = curve_at(iso, grid)
    pl_g = curve_at(lr, grid)
    max_abs_diff = max(abs(i - p) for i, p in zip(iso_g, pl_g))
    near_logistic = max_abs_diff < NEAR_LOGISTIC_TOL
    platt_not_worse = pl_post_hel["ece"] is not None and iso_post_hel["ece"] is not None \
        and pl_post_hel["ece"] <= iso_post_hel["ece"] + 1e-6
    chosen = "platt" if (near_logistic and platt_not_worse) else "isotonic"

    # flat-band assertion: over the low band [0,0.5), the fitted map's spread should not
    # exceed the empirical spread (no invented resolution). Report the map's low-band range.
    low_grid = [i / 100.0 for i in range(0, 50)]
    chosen_map = iso if chosen == "isotonic" else lr
    low_vals = curve_at(chosen_map, low_grid)
    low_range = (min(low_vals), max(low_vals))

    if chosen == "isotonic":
        knots = {"type": "isotonic-piecewise-linear",
                 "x_thresholds": list(map(float, iso.X_thresholds_)),
                 "y_thresholds": list(map(float, iso.y_thresholds_))}
        post_fit_ece = iso_post_fit["ece"]; post_hel_ece = iso_post_hel["ece"]
        mono_ok = True  # isotonic monotone by construction
    else:
        knots = {"type": "platt-sigmoid", "a": a, "b": b, "form": "P = 1/(1+exp(-(a*x+b)))"}
        post_fit_ece = pl_post_fit["ece"]; post_hel_ece = pl_post_hel["ece"]
        mono_ok = a >= 0.0

    artifact = {
        "schema": "stage5_classP_reliability_map/v1",
        "layer": layer, "decision": decision,
        "published_confidence": conf_name,
        "confidence_class_in": "M", "confidence_class_out": "P",
        "carrier": carrier,
        "idiom_target": IDIOM2_LABEL,
        "license_provenance": LICENSE_LINE,
        "empirically_unvalidated_note": "Jazz carrier deliberately UNMAPPED (A-7): stays Class M.",
        "squash_note": squash_note,
        "map_type": chosen,
        "map": knots,
        "monotone": mono_ok,
        "fit_substrate": {
            "corpus_git_hash": _corpus_git_hash(carrier),
            "split_registry": "tools/stage5_split_registry.json",
            "fit_split": "fitting", "validation_split": "held_out",
            "n_cells_fit": len(fit_pairs), "n_cells_held_out": len(hel_pairs),
        },
        "ece": {
            "pre_map_fitting": pre_fit_d["ece"], "pre_map_held_out": pre_hel_d["ece"],
            "post_map_fitting": post_fit_ece, "post_map_held_out": post_hel_ece,
        },
        "signed_gap_pre": {"fitting": pre_fit_d["signed_gap"], "held_out": pre_hel_d["signed_gap"]},
        "overall_correct": {"fitting": pre_fit_d["overall_correct"], "held_out": pre_hel_d["overall_correct"]},
        "raw_monotonicity_violations": {"fitting": pre_fit_d["monotonicity_violations"],
                                        "held_out": pre_hel_d["monotonicity_violations"]},
        "shape_selection": {
            "chosen": chosen, "rule": "isotonic default; Platt only if near-logistic AND not worse held-out",
            "isotonic_vs_platt_max_abs_diff": max_abs_diff,
            "near_logistic": near_logistic,
            "platt": {"a": a, "b": b, "post_map_fitting_ece": pl_post_fit["ece"],
                      "post_map_held_out_ece": pl_post_hel["ece"]},
            "isotonic": {"post_map_fitting_ece": iso_post_fit["ece"],
                         "post_map_held_out_ece": iso_post_hel["ece"]},
        },
        "flat_band_assertion": {
            "band": "[0,0.5)",
            "map_low_band_range": [low_range[0], low_range[1]],
            "note": "isotonic pools the flat low band to its mean; does not invent resolution.",
        },
    }
    summary = (f"  [{name} / {carrier}] chosen={chosen}  "
               f"ECE pre(fit/hel)={pre_fit_d['ece']:.3f}/{pre_hel_d['ece']:.3f}  "
               f"post(fit/hel)={post_fit_ece:.3f}/{post_hel_ece:.3f}  "
               f"overall(fit/hel)={pre_fit_d['overall_correct']:.3f}/{pre_hel_d['overall_correct']:.3f}  "
               f"n(fit/hel)={len(fit_pairs)}/{len(hel_pairs)}  "
               f"iso-platt maxdiff={max_abs_diff:.3f}  low-band={low_range[0]:.2f}..{low_range[1]:.2f}")
    return artifact, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--km-root", default="C:/tmp/c1")
    ap.add_argument("--fs-root", default="C:/tmp/c1")
    # OI-130 (DT-24): default out-dir is SCRATCH, never the committed tools/calibration_maps.
    # Re-fitting the committed maps must name that dir EXPLICITLY, so a bare run cannot overwrite them.
    ap.add_argument("--out-dir", default="C:/tmp/calibration_maps_out",
                    help="Output dir for the fitted maps (default: a scratch dir; pass "
                         "tools/calibration_maps EXPLICITLY to re-fit the committed maps)")
    args = ap.parse_args()

    splits = _load_splits()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # OI-35: the km/fs dump substrate has NO manifest to validate (OI-129's km/fs residual), so the
    # generalized "validate-or-re-manifest at the read site" rule is applied as far as possible here —
    # the substrate's per-carrier stem COVERAGE is checked against the validated corpus and surfaced,
    # so a stale/partial/missing dump substrate cannot silently shrink the fit pool with no signal.
    # (A full manifest-based validate waits on the km/fs producer stamping a manifest — OI-129.)
    for carrier in CARRIERS:
        corpus_stems = {p.stem.replace(".ours", "")
                        for p in (_ROOT / "tools" / "corpus" / carrier).glob("*.ours.json")}
        km_dir = Path(args.km_root) / f"km_{carrier}"
        fs_dir = Path(args.fs_root) / f"fs_{carrier}"
        km_have = ({p.stem.replace(".keymargin", "") for p in km_dir.glob("*.keymargin.json")}
                   if km_dir.is_dir() else set())
        fs_have = ({p.stem.replace(".ours", "") for p in fs_dir.glob("*.ours.json")}
                   if fs_dir.is_dir() else set())
        km_missing, fs_missing = corpus_stems - km_have, corpus_stems - fs_have
        if km_missing or fs_missing:
            print(f"[OI-35] {carrier} DUMP-SUBSTRATE PARTIAL: km {len(km_have & corpus_stems)}/"
                  f"{len(corpus_stems)} (missing {len(km_missing)}), fs "
                  f"{len(fs_have & corpus_stems)}/{len(corpus_stems)} (missing {len(fs_missing)}) "
                  f"— fit pool silently reduced; regenerate the km/fs dumps.", file=sys.stderr)

    print("=" * 78)
    print("calibration_fit — Stage-5 Phase 3 Task A: Class-P reliability maps (L3 margin, L4 composite)")
    print("Fit=fitting split; validate=held_out split. Jazz UNMAPPED (A-7). No behaviour change.")
    print("=" * 78)

    written = []
    for carrier in CARRIERS:
        print(f"\n########## CARRIER = {carrier} ##########")
        # OI-129: the committed calibration maps are fit off tools/corpus/{carrier}; route the
        # read through the anti-contamination guard (manifest present, complete, .ours.json AND
        # .music21.json fingerprints match — OI-124) so a stale/foreign/preset-crossed corpus
        # cannot silently poison a map. (The km/fs dump substrate itself is a bare scratch dir with
        # no manifest — OI-129's second half; tracked, not closed here.)
        cbf.validate_corpus_dir(_ROOT / "tools" / "corpus" / carrier)
        km_dir = Path(args.km_root) / f"km_{carrier}"
        fs_dir = Path(args.fs_root) / f"fs_{carrier}"

        l3_cells = collect_l3(carrier, km_dir, splits)
        art, summ = fit_row("L3 key margin", "L3", "key-of-slice",
                            "sequence margin (squashed x/(x+1); D-L3a boundary confidence)",
                            carrier, l3_cells,
                            "squash s(x)=x/(x+1), k=uncertainThreshold; monotone, ranking-invariant")
        print(summ)
        if art:
            p = out_dir / f"stage5_classP_l3_key_margin_{carrier}.json"
            p.write_text(json.dumps(art, indent=1), encoding="utf-8")
            written.append(p)

        l4_cells = collect_l4(carrier, fs_dir, splits)
        art, summ = fit_row("L4 chord composite", "L4", "chord-of-slice",
                            "composite (min(margin,sufficiency,cleanliness); native [0,1])",
                            carrier, l4_cells, "native [0,1] composite; no squash")
        print(summ)
        if art:
            p = out_dir / f"stage5_classP_l4_chord_composite_{carrier}.json"
            p.write_text(json.dumps(art, indent=1), encoding="utf-8")
            written.append(p)

    print("\n=== WROTE ===")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
