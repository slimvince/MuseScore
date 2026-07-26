#!/usr/bin/env python3
"""adoption_measure_b.py — the OI-178 adoption measurement's GRADE + DIFF + RECORD phase.

Consumes adoption_measure.py's cached decode (adoption_decode.json) + candidate corpus, runs the
pinned a8 + robust_stop_diff sandwich, computes the per-preset robust-unit comparison, the paired
piece-bootstrap CIs (A vs the current system), the ★R GT self-agreement ceiling and modulation-rate
band, evaluates every OI-178 PASS condition (as amended ★R=A1), and writes the adoption record.

★ MEASUREMENT ONLY — no adoption act, no re-baseline. Pinned instruments import-only; the firewall:
the only decoder input was the frozen selected weight vector; nothing here feeds a value back.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import probe_run as pr                # noqa: E402  grade_regions / WIR_DIR
import compare_analyses as cmp        # noqa: E402  load_analysis / _dcml_time_spans
import compare_rn as crn              # noqa: E402  _active_index_at / _dcml_key_tonic / _our_key_ident
import a8_rebaseline_measure as a8    # noqa: E402  build_piece_grid
import dcml_parser as dcml            # noqa: E402  load_wir_regions
import fit_run as fr                  # noqa: E402  pooled / _NUM / AXES / BOOTSTRAP_*
import robust_stop_diff as rsd        # noqa: E402  _RUN_RE / parse conventions (import-only)
import search_run as sr               # noqa: E402  decode_modulation_rate / gt_modulation_rate

import adoption_measure as am         # noqa: E402  paths + PRESETS + selected_weights

REF_DIR = _ROOT / "tools" / "robust_stop"
OUT_JSON = _HERE / "adoption_record.json"
OUT_SUMMARY = _HERE / "adoption_record_summary.txt"
OUT_SETDIFF = _HERE / "adoption_setdiff.json"
CORPUS_ROOT = _ROOT / "tools" / "corpus"

GT_MOD_RATE = 5.28          # the committed ground-truth local-key change rate (search report §3)
MOD_BAND = (0.75, 1.25)     # ★R (i-b): A's rate must sit within [0.75x, 1.25x] of the GT rate


def _git_head() -> str:
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def run_a8_and_diff():
    """Run the pinned a8 on A's candidate corpus and robust_stop_diff against the committed reference.
    Returns (a8_summary, diff_stdout, diff_returncode)."""
    am.CAND_A8.mkdir(parents=True, exist_ok=True)
    r1 = subprocess.run([sys.executable, str(_ROOT / "tools" / "a8_rebaseline_measure.py"),
                         "--corpus-root", str(am.CAND_CORPUS), "--out-dir", str(am.CAND_A8)],
                        capture_output=True, text=True)
    (am.CAND_A8 / "_a8_stdout.txt").write_text(r1.stdout + "\n" + r1.stderr, encoding="utf-8")
    if r1.returncode != 0:
        raise SystemExit(f"STOP: a8 on candidate corpus failed:\n{r1.stdout}\n{r1.stderr}")
    # --show-runs 6: a few examples per preset/direction — the COMPLETE set-diff is produced
    # programmatically by diagnose_setdiff below; robust_stop_diff is the AUTHORITATIVE gate verdict
    # (returncode + per-preset PASS lines), not the enumeration source.
    r2 = subprocess.run([sys.executable, str(_ROOT / "tools" / "robust_stop_diff.py"),
                         "--reference", str(REF_DIR), "--candidate", str(am.CAND_A8), "--show-runs", "6"],
                        capture_output=True, text=True)
    summary = json.loads((am.CAND_A8 / "summary.json").read_text(encoding="utf-8"))
    return summary, (r2.stdout + r2.stderr), r2.returncode


def parse_runs_spans(path: Path):
    """Parse an a8 variant-(b) run file into {(stem,start,our_root,dcml_root): {end,dur,cls}} — the
    same identity robust_stop_diff.parse_runs uses, plus the END tick (for span-overlap diagnosis).
    Fails loudly on an unparsed non-header line (the diff-base integrity guard, reused convention)."""
    runs = {}
    skipped = []
    for i, ln in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if i < 2 or not ln.strip():
            continue
        m = rsd._RUN_RE.match(ln)
        if not m:
            skipped.append(ln)
            continue
        stem, start, end = m.group(1), int(m.group(2)), int(m.group(4))
        dur, orr, dr, cls = int(m.group(5)), int(m.group(6)), int(m.group(7)), m.group(8)
        runs[(stem, start, orr, dr)] = {"end": end, "dur": dur, "cls": cls}
    if skipped:
        raise ValueError(f"{path.name}: {len(skipped)} run line(s) failed the parse: {skipped[0]!r}")
    return runs


def _key_at(regions, spans, tick):
    """(tonic, is_major) of the region active at tick, via the pinned _our_key_ident / active index."""
    i = crn._active_index_at(spans, tick)
    if i is None:
        return None
    return crn._our_key_ident(getattr(regions[i], "key", None))


def diagnose_setdiff(a8_summary, A_regions, wir_of):
    """Per preset: the complete run-level set-diff (A vs the committed reference), every added run
    classified (a)/(b), and every added class-(b) run individually diagnosed — root-interval class,
    A-local-key-correct?, and whether the current system ALSO failed at an overlapping span (churn) or
    was correct there (a GENUINE-NEW error, the surfacing subset). An added class-(b) run that lands
    on no diagnosable signature is flagged (none is expected — the signature is always computable)."""
    per_preset = {}
    a_spans_of = {s: [(r.start_tick, r.end_tick) for r in A_regions[s]] for s in A_regions}
    dcml_spans_of = {s: cmp._dcml_time_spans(A_regions[s], wir_of[s]) for s in A_regions if wir_of.get(s)}
    for preset in am.PRESETS:
        cand = parse_runs_spans(am.CAND_A8 / f"{preset}_variant_b_root_fail_runs.txt")
        ref = parse_runs_spans(REF_DIR / f"{preset}_variant_b_root_fail_runs.txt")
        added = sorted(set(cand) - set(ref))
        removed = sorted(set(ref) - set(cand))
        # committed class-(b) failing SPANS per stem (for the genuine-new overlap test)
        ref_b_spans = defaultdict(list)
        for (stem, start, orr, dr), v in ref.items():
            if v["cls"] == "b":
                ref_b_spans[stem].append((start, v["end"]))
        buckets = Counter()
        genuine_new = []
        n_added_b = 0
        for k in added:
            stem, start, orr, dr = k
            v = cand[k]
            if v["cls"] != "b":
                continue                 # class-(a) added runs counted separately (added_class_a)
            n_added_b += 1
            end = v["end"]
            interval = (dr - orr) % 12 if (dr >= 0 and orr >= 0) else None
            # A's local key vs GT local key at the run start
            akey = _key_at(A_regions[stem], a_spans_of[stem], start)
            di = crn._active_index_at(dcml_spans_of.get(stem, []), start) if dcml_spans_of.get(stem) else None
            gkey = None
            if di is not None:
                lt, lm = crn._dcml_key_tonic(getattr(wir_of[stem][di], "local_key", None))
                gkey = (lt, lm) if lt is not None else None
            key_ok = (akey is not None and gkey is not None and akey == gkey)
            # did the current system ALSO fail (class-b) at an overlapping span for this stem?
            overlaps_current = any(s < end and e > start for (s, e) in ref_b_spans.get(stem, []))
            interval_class = {0: "same-root(other-error)", 7: "fifth", 5: "fourth", 3: "minor-third",
                              9: "major-sixth", 4: "major-third", 8: "minor-sixth", 2: "whole-tone",
                              10: "minor-seventh", 1: "semitone", 11: "leading-tone", 6: "tritone"}.get(
                              interval, "other")
            kind = "churn(current also failed at overlapping span)" if overlaps_current else \
                   "GENUINE-NEW(current has no overlapping class-b failure)"
            factor_hint = ("key/prior (A's local key wrong here)" if not key_ok else
                           "chord-transition/bass (key right, root off by " + interval_class + ")")
            row = {"stem": stem, "start": start, "end": end, "dur": v["dur"],
                   "our_root": orr, "dcml_root": dr, "root_interval": interval,
                   "interval_class": interval_class, "a_local_key_correct": bool(key_ok),
                   "overlaps_current_failure": bool(overlaps_current),
                   "kind": kind, "factor_hint": factor_hint}
            buckets[(interval_class, "key_ok" if key_ok else "key_wrong",
                     "churn" if overlaps_current else "genuine_new")] += 1
            if not overlaps_current:
                genuine_new.append(row)
        # duration of added/removed class-(b)
        add_b_dur = sum(cand[k]["dur"] for k in added if cand[k]["cls"] == "b")
        rem_b_dur = sum(ref[k]["dur"] for k in removed if ref[k]["cls"] == "b")
        gn_dur = sum(r["dur"] for r in genuine_new)
        per_preset[preset] = {
            "runs_reference": len(ref), "runs_candidate": len(cand),
            "added": len(added), "removed": len(removed),
            "added_class_b": n_added_b, "added_class_a": len(added) - n_added_b,
            "added_class_b_dur": add_b_dur, "removed_class_b_dur": rem_b_dur,
            "genuine_new_class_b_runs": len(genuine_new),
            "genuine_new_class_b_dur": gn_dur,
            # every added class-(b) run is classified by its mechanical signature here
            # (interval_class | key correct? | churn-vs-genuine-new) — the "every run diagnosed" surface.
            "diagnosis_buckets": {f"{a}|{b}|{c}": n for (a, b, c), n in
                                  sorted(buckets.items(), key=lambda x: -x[1])},
            # the GENUINE-NEW subset (A wrong where the current system was root-correct) is enumerated
            # individually — the runs that actually warrant scrutiny; the churn runs (both systems fail,
            # only the boundary moved) are fully captured by the buckets and the a8 run files, and the
            # complete per-run list is deterministically regenerable from the decode cache.
            "genuine_new_runs": sorted(genuine_new, key=lambda r: -r["dur"]),
        }
    return per_preset


def gt_self_agreement_ceiling(A_regions, wir_of):
    """★R: the GT self-agreement ceiling — the fraction of A's GRADED duration where the ground
    truth's own LOCAL key equals its HOME (global) key. The maximum any correct local-following
    decoder can score on the key-HOME column. Computed over A's graded grid (build_piece_grid's
    scored cells) so the denominator matches A's key-home column exactly."""
    home_eq_local = home_ne_local = dcml_keyfail = 0
    for stem, regs in A_regions.items():
        wir = wir_of.get(stem)
        if not wir:
            continue
        pg = a8.build_piece_grid(stem, regs, wir, [])
        dcml_spans = cmp._dcml_time_spans(regs, wir)
        for c in pg.cells:
            di = crn._active_index_at(dcml_spans, c["t0"])
            if di is None:
                continue
            gt, gmaj = crn._dcml_key_tonic(getattr(wir[di], "global_key", None))
            lt, lmaj = crn._dcml_key_tonic(getattr(wir[di], "local_key", None))
            w = c["w"]
            if gt is None or lt is None:
                dcml_keyfail += w
            elif (gt, gmaj) == (lt, lmaj):
                home_eq_local += w
            else:
                home_ne_local += w
    scored = home_eq_local + home_ne_local
    return {
        "graded_dur_local_eq_home": home_eq_local,
        "graded_dur_local_ne_home": home_ne_local,
        "graded_dur_dcml_keyfail": dcml_keyfail,
        "ceiling_home_pct": round(100.0 * home_eq_local / scored, 2) if scored else None,
        "modulated_fraction_pct": round(100.0 * home_ne_local / scored, 2) if scored else None,
        "note": ("the maximum key-HOME agreement a PERFECT local-following decoder can reach; a system "
                 "scoring ABOVE this on key-home is achieving it by UNDER-following modulation (staying "
                 "in the home key where the music has left it)."),
    }


def paired_bootstrap(a_pp, cur_pp, b=fr.BOOTSTRAP_B, seed=fr.BOOTSTRAP_SEED):
    """Piece-level paired bootstrap of (A - current) per axis. Pairs on piece identity (the same
    resampled pieces enter both arms). Reuses fit_run._NUM / AXES / BOOTSTRAP constants."""
    stems = sorted(set(a_pp) & set(cur_pp))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(stems), size=(b, len(stems)))
    out = {"n_pieces": len(stems)}
    draws = {}
    for name, pp in (("A", a_pp), ("cur", cur_pp)):
        draws[name] = {}
        for axis, (ag, ds) in fr._NUM.items():
            m = np.array([[pp[s][ag], pp[s][ds]] for s in stems], dtype=np.float64)
            num = m[:, 0][idx].sum(axis=1)
            den = (m[:, 0] + m[:, 1])[idx].sum(axis=1)
            draws[name][axis] = 100.0 * num / np.maximum(1.0, den)
    for axis in fr.AXES:
        d = draws["A"][axis] - draws["cur"][axis]
        lo, hi = float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))
        out[axis] = {"mean": round(float(d.mean()), 2), "lo": round(lo, 2), "hi": round(hi, 2),
                     "excludes_zero": bool(lo > 0 or hi < 0)}
    return out


def main():
    t0 = time.perf_counter()
    dec = json.loads(am.DECODE_CACHE.read_text(encoding="utf-8"))
    stems = sorted(dec["decode"])
    est = dec["establishment_vs_cpp_production"]

    # A's regions from the candidate corpus (identical across presets; use default) + WiR GT
    A_regions = {s: cmp.load_analysis(am.CAND_CORPUS / "default" / f"{s}.ours.json")[1] for s in stems}
    wir_of = {s: dcml.load_wir_regions(pr.WIR_DIR, s) for s in stems}

    # ── the pinned a8 + robust_stop_diff sandwich ──
    a8_summary, diff_out, diff_rc = run_a8_and_diff()

    # ── the programmatic set-diff + per-added-class-(b) diagnosis ──
    setdiff = diagnose_setdiff(a8_summary, A_regions, wir_of)

    # ── A per-piece grade (reuse) + current-system per-piece grade per preset (reuse) ──
    a_pp = {s: pr.grade_regions(s, A_regions[s]) for s in stems}
    a_pp = {s: g for s, g in a_pp.items() if g is not None}
    cur_pp = {}
    cur_reproduces = {}
    ref_manifest = json.loads((REF_DIR / "manifest.json").read_text(encoding="utf-8"))
    for preset in am.PRESETS:
        pp = {}
        for s in stems:
            p = CORPUS_ROOT / preset / f"{s}.ours.json"
            if not p.exists():
                continue
            g = pr.grade_regions(s, cmp.load_analysis(p)[1])
            if g is not None:
                pp[s] = g
        cur_pp[preset] = pp
        pooled = fr.pooled(pp)
        man = ref_manifest["presets"][preset]
        cur_reproduces[preset] = {
            "root_pooled": pooled["root_agree_pct"], "root_manifest": man["root_agree_pct"],
            "reproduces_root": bool(pooled["root_agree_pct"] is not None
                                    and abs(pooled["root_agree_pct"] - man["root_agree_pct"]) < 0.02),
            "n_pieces": len(pp)}

    a_cols = fr.pooled(a_pp)

    # ── paired piece-bootstrap: A vs current, per preset ──
    ci = {preset: paired_bootstrap(a_pp, cur_pp[preset]) for preset in am.PRESETS}

    # ── ★R items ──
    ceiling = gt_self_agreement_ceiling(A_regions, wir_of)
    a_mod = sr.decode_modulation_rate({s: dec["decode"][s]["segments"] for s in stems})
    gt_mod = sr.gt_modulation_rate(stems)
    shared = sorted(set(a_mod) & set(gt_mod))
    a_rate = float(np.mean([a_mod[s] for s in shared]))
    gt_rate = float(np.mean([gt_mod[s] for s in shared]))
    band = (round(MOD_BAND[0] * gt_rate, 2), round(MOD_BAND[1] * gt_rate, 2))
    modulation = {
        "a_mean_key_changes_per_piece": round(a_rate, 2),
        "gt_mean_key_changes_per_piece_measured": round(gt_rate, 2),
        "gt_mean_committed": GT_MOD_RATE,
        "band_x0.75_1.25_of_gt": list(band),
        "a_pieces_with_zero_key_change": int(sum(1 for s in shared if a_mod[s] == 0)),
        "gt_pieces_with_zero_key_change": int(sum(1 for s in shared if gt_mod[s] == 0)),
        "within_band": bool(band[0] <= a_rate <= band[1]),
        "n_pieces": len(shared),
    }

    # ── the PASS-condition table (OI-178 as amended ★R=A1) ──
    # (ii) class-(b) duration net decrease per preset (A is preset-independent; cand agg equal per preset)
    classb = {}
    for preset in am.PRESETS:
        cand_cb = a8_summary[preset]["agg"]["b_cls_b_dur"]
        cand_ca = a8_summary[preset]["agg"]["b_cls_a_dur"]
        ref_cb = ref_manifest["presets"][preset]["class_b_root_disagree_dur"]
        ref_ca = ref_manifest["presets"][preset]["class_a_root_disagree_dur"]
        classb[preset] = {"cand_class_b_dur": cand_cb, "ref_class_b_dur": ref_cb,
                          "delta_class_b_dur": cand_cb - ref_cb,
                          "pct_change": round(100.0 * (cand_cb - ref_cb) / ref_cb, 2),
                          "net_decrease": bool(cand_cb - ref_cb < 0),
                          "cand_class_a_dur": cand_ca, "ref_class_a_dur": ref_ca,
                          "delta_class_a_dur": cand_ca - ref_ca,
                          "class_a_investigate": bool(cand_ca - ref_ca > rsd.CLASS_A_INVESTIGATE_TICKS),
                          # coverage context: the net decrease must not be an artifact of A grading
                          # LESS duration (robust_stop_diff separately fails on a wir_covered shrink).
                          "cand_scored_dur": a8_summary[preset]["agg"]["scored_dur"],
                          "ref_scored_dur": ref_manifest["presets"][preset]["scored_dur"],
                          "cand_wir_covered": a8_summary[preset]["coverage"]["wir_covered"],
                          "ref_wir_covered": ref_manifest["presets"][preset]["coverage"]["wir_covered"]}
    # (i) key-local exceeds baseline beyond CI; root/RN non-degrading; (i-b) modulation band
    cond_i = {}
    for preset in am.PRESETS:
        c = ci[preset]
        kl = c["key_local_agree_pct"]
        rt = c["root_agree_pct"]
        rn = c["rn_agree_pct"]
        cond_i[preset] = {
            "key_local_exceeds": bool(kl["mean"] > 0 and kl["excludes_zero"]),
            "key_local_delta": kl,
            "root_nondegrading": bool(not (rt["hi"] < 0)),   # not a CI-significant decrease
            "root_delta": rt,
            "rn_nondegrading": bool(not (rn["hi"] < 0)),
            "rn_delta": rn,
        }
    # (—) key abstain must read 0 (A commits MAP)
    key_abstain = {preset: {"b_key_fail": a8_summary[preset]["agg"].get("b_key_fail", 0),
                            "b_key_fail_local": a8_summary[preset]["agg"].get("b_key_fail_local", 0)}
                   for preset in am.PRESETS}
    abstain_zero = all(v["b_key_fail"] == 0 and v["b_key_fail_local"] == 0 for v in key_abstain.values())

    # PASS verdicts
    pass_ii = all(classb[p]["net_decrease"] for p in am.PRESETS)
    pass_i_kl = all(cond_i[p]["key_local_exceeds"] for p in am.PRESETS)
    pass_i_root = all(cond_i[p]["root_nondegrading"] for p in am.PRESETS)
    pass_i_rn = all(cond_i[p]["rn_nondegrading"] for p in am.PRESETS)
    pass_ib = modulation["within_band"]

    # ── the columns beside the current baselines ──
    columns = {"A_from_adapter": {a: a_cols[a] for a in fr.AXES},
               "current_baseline_committed": pr.BASELINES}

    record = {
        "provenance": {
            "generator": "tools/joint_estimator/adoption_measure.py (+ _b.py)",
            "instrument_commit": _git_head(),
            "dispatch": "cc_instruction_adoption_measurement.md (Cowork 2026-07-20; ★R=A1)",
            "kind": "MEASUREMENT ONLY — adoption record for the user's ratification; NO adoption act",
            "corpus_git_hash": dec["provenance"]["corpus_git_hash"],
            "decoder_input": dec["provenance"]["reader"],
            "selected_start": dec["provenance"]["selected_start"],
            "selected_R_train": dec["provenance"]["selected_R_train"],
            "config": {"seg_cap": dec["provenance"]["seg_cap"],
                       "leftover_rule": dec["provenance"]["leftover_rule"],
                       "table_set": dec["provenance"]["table_set"],
                       "tie_break": dec["provenance"]["tie_break"]},
            "reference": "tools/robust_stop/ (the committed OI-168 re-baseline)",
            "o12_snapshot": "tools/robust_stop/snapshot_2026-07-26_pre_oi178_adoption/",
            "reuse": ("decode=probe_decoder.decode_piece; regions=probe_run.decode_to_regions; "
                      "grading=probe_run.grade_regions->a8.build_piece_grid; run enumeration + class "
                      "split + set-diff=a8_rebaseline_measure.py + robust_stop_diff.py (the R10 "
                      "sandwich); pooled+bootstrap=fit_run; modulation=search_run"),
        },
        "establishment": {
            "reproduces_cpp_from_adapter_decode": est["reproduces_cpp_from_adapter"],
            "divergent_vs_note_events_oracle": est["my_divergent_vs_note_events_oracle"],
            "cpp_from_adapter_divergent": est["cpp_from_adapter_divergent_vs_oracle"],
            "current_system_reproduces_manifest_root": cur_reproduces,
            "note": est["note"],
        },
        "predictions_vs_measured": {
            "class_b_duration": {"predicted": "NET DECREASE every preset, 10-30% smaller",
                                 "measured_pct_change": {p: classb[p]["pct_change"] for p in am.PRESETS}},
            "set_diff": {"predicted": "LARGE in both directions",
                         "measured": {p: {"added": setdiff[p]["added"], "removed": setdiff[p]["removed"]}
                                      for p in am.PRESETS}},
            "key_local": {"predicted": "+8 to +13 pts over every preset baseline",
                          "measured_delta": {p: ci[p]["key_local_agree_pct"]["mean"] for p in am.PRESETS}},
            "key_home": {"predicted": "12-18 pts BELOW the baselines (explained by the GT ceiling)",
                         "measured_delta": {p: ci[p]["key_home_agree_pct"]["mean"] for p in am.PRESETS}},
            "rn": {"predicted": "+12 to +16",
                   "measured_delta": {p: ci[p]["rn_agree_pct"]["mean"] for p in am.PRESETS}},
            "modulation": {"predicted": "within the ★R band", "measured": modulation["a_mean_key_changes_per_piece"],
                           "band": modulation["band_x0.75_1.25_of_gt"], "within": modulation["within_band"]},
            "root": {"predicted": "large improvement (expected, carried as known — the architecture's "
                                  "asymmetric expectation)",
                     "measured_delta": {p: ci[p]["root_agree_pct"]["mean"] for p in am.PRESETS}},
        },
        "columns": columns,
        "pass_conditions": {
            "amended_ruling": "★R=A1 (user 2026-07-20): key-LOCAL is the PASS axis; key-HOME tracked "
                              "with the GT-ceiling decomposition; modulation-rate is a PASS condition.",
            "i_key_local_exceeds_beyond_CI": {"pass": pass_i_kl, "per_preset": cond_i},
            "i_root_nondegrading": {"pass": pass_i_root},
            "i_rn_nondegrading": {"pass": pass_i_rn},
            "ib_modulation_band": {"pass": pass_ib, "detail": modulation},
            "ii_class_b_duration_net_decrease": {"pass": pass_ii, "per_preset": classb,
                                                 "robust_stop_diff_returncode": diff_rc,
                                                 "robust_stop_diff_pass": bool(diff_rc == 0)},
            "iii_class_a_tracked": {p: {"delta": classb[p]["delta_class_a_dur"],
                                        "investigate": classb[p]["class_a_investigate"]} for p in am.PRESETS},
            "key_abstain_zero": {"pass": abstain_zero, "detail": key_abstain},
            "iv_user_ratification": "PENDING — this record is the input to that ruling (no adoption act here)",
        },
        "R_ceiling_decomposition": ceiling,
        "modulation_rate": modulation,
        "confidence_intervals_A_minus_current": ci,
        "set_diff_summary": {p: {k: v for k, v in setdiff[p].items()
                                 if k not in ("genuine_new_runs", "all_added_class_b_diagnoses")}
                             for p in am.PRESETS},
        "timing": {**dec["timing"], "measure_wall_s": round(time.perf_counter() - t0, 1)},
        "robust_stop_diff_stdout": diff_out,
        "what_the_adoption_commit_would_contain": _adoption_commit_plan(),
    }
    OUT_JSON.write_text(json.dumps(record, indent=1), encoding="utf-8")
    # the full per-run diagnosis (kept separate — the complete set-diff enumeration)
    OUT_SETDIFF.write_text(json.dumps(setdiff, indent=1), encoding="utf-8")
    write_summary(record, setdiff)
    print(f"\nwrote {OUT_JSON.name}, {OUT_SETDIFF.name}, {OUT_SUMMARY.name}", flush=True)
    return record


def _adoption_commit_plan():
    return {
        "note": "For the user's ratification — NOT executed in this dispatch.",
        "would_contain": [
            "the wiring point: A becomes the inference-layer key/mode/chord estimator; the analysis is "
            "PRESET-INDEPENDENT at the inference layer (the ratified mode decision) — presets remain "
            "presentation concerns only",
            "the re-baselined tools/robust_stop/ reference (a8 re-run over A's decode; the set-diff "
            "explained and ratified; the manifest re-stamped via robust_stop_restamp.py; the O-12 "
            "snapshot at snapshot_2026-07-26_pre_oi178_adoption/ is the outgoing preservation)",
            "the OI-180 retirement map's first steps (each its own later verified increment)",
            "one revertible, provenance-stamped commit; suites + pipeline snapshots refreshed only if "
            "A's adoption changes committed output",
        ],
    }


def write_summary(g, setdiff):
    L = []
    A = ("key_local_agree_pct", "key_home_agree_pct", "root_agree_pct", "rn_agree_pct")
    SH = {"key_local_agree_pct": "key-LOCAL", "key_home_agree_pct": "key-HOME",
          "root_agree_pct": "root", "rn_agree_pct": "RN"}
    L.append("OI-178 ADOPTION MEASUREMENT — the adoption record (MEASUREMENT ONLY; no adoption act)")
    L.append(f"instrument {g['provenance']['instrument_commit']}   corpus {g['provenance']['corpus_git_hash']}")
    L.append(f"decoder input: {g['provenance']['decoder_input']}")
    L.append(f"selected weights: {g['provenance']['selected_start']} "
             f"(R_train {g['provenance']['selected_R_train']:.6f}); {g['provenance']['config']}")
    L.append("")
    e = g["establishment"]
    L.append(f"ESTABLISHMENT — Python-from-adapter reproduces the C++ production decode: "
             f"{e['reproduces_cpp_from_adapter_decode']}")
    L.append(f"  divergent vs note_events oracle: {e['divergent_vs_note_events_oracle']}")
    L.append(f"  (C++ from-adapter divergent:      {e['cpp_from_adapter_divergent']})")
    L.append(f"  current-system grading reproduces manifest ROOT: "
             + ", ".join(f"{p} {r['reproduces_root']}({r['root_pooled']} vs {r['root_manifest']})"
                         for p, r in e["current_system_reproduces_manifest_root"].items()))
    L.append("")
    L.append("COLUMNS — A (from adapter, all-326 selected) vs current committed baselines (B/J/D)")
    ac = g["columns"]["A_from_adapter"]
    base = g["columns"]["current_baseline_committed"]
    bk = {"key_local_agree_pct": "key_local", "key_home_agree_pct": "key_home",
          "root_agree_pct": "root", "rn_agree_pct": "rn"}
    L.append(f"{'axis':14s} {'A(all326)':>10s}   current B / J / D")
    for a in A:
        b = base[bk[a]]
        L.append(f"{SH[a]:14s} {ac[a]:10.2f}   {b['Baroque']} / {b['Jazz']} / {b['Default']}")
    L.append("")
    L.append("PASS CONDITIONS (OI-178 as amended ★R=A1)")
    pc = g["pass_conditions"]
    L.append(f"  (i)  key-LOCAL exceeds baseline beyond CI on every preset: "
             f"{'PASS' if pc['i_key_local_exceeds_beyond_CI']['pass'] else 'FAIL'}")
    for p in am.PRESETS:
        d = pc["i_key_local_exceeds_beyond_CI"]["per_preset"][p]["key_local_delta"]
        L.append(f"         {p:8s} A-current key-local {d['mean']:+6.2f} [{d['lo']:+.2f},{d['hi']:+.2f}]"
                 f"{'  *excludes 0' if d['excludes_zero'] else '  (spans 0)'}")
    L.append(f"  (i)  root non-degrading: {'PASS' if pc['i_root_nondegrading']['pass'] else 'FAIL'}   "
             f"RN non-degrading: {'PASS' if pc['i_rn_nondegrading']['pass'] else 'FAIL'}")
    L.append(f"  (i-b) modulation-rate band {g['modulation_rate']['band_x0.75_1.25_of_gt']}: "
             f"A={g['modulation_rate']['a_mean_key_changes_per_piece']} "
             f"(GT {g['modulation_rate']['gt_mean_key_changes_per_piece_measured']}) -> "
             f"{'PASS' if pc['ib_modulation_band']['pass'] else 'FAIL'}")
    L.append(f"  (ii) class-(b) root-disagree DURATION net decrease every preset: "
             f"{'PASS' if pc['ii_class_b_duration_net_decrease']['pass'] else 'FAIL'}   "
             f"(robust_stop_diff rc={pc['ii_class_b_duration_net_decrease']['robust_stop_diff_returncode']})")
    for p in am.PRESETS:
        cb = pc["ii_class_b_duration_net_decrease"]["per_preset"][p]
        L.append(f"         {p:8s} class-b dur {cb['ref_class_b_dur']} -> {cb['cand_class_b_dur']} "
                 f"({cb['delta_class_b_dur']:+d}, {cb['pct_change']:+.1f}%)   class-a delta "
                 f"{cb['delta_class_a_dur']:+d}{'  **INVESTIGATE' if cb['class_a_investigate'] else ''}")
    L.append(f"  (—)  key-abstain reads zero (A commits MAP): "
             f"{'PASS' if pc['key_abstain_zero']['pass'] else 'FAIL'}")
    L.append("")
    L.append("★R  GT SELF-AGREEMENT CEILING (key-HOME decomposition)")
    ce = g["R_ceiling_decomposition"]
    L.append(f"  ceiling (GT local==home over A's graded dur): {ce['ceiling_home_pct']}%   "
             f"modulated (local!=home): {ce['modulated_fraction_pct']}%")
    L.append(f"  A key-home {ac['key_home_agree_pct']}  vs current home "
             f"{base['key_home']['Baroque']}/{base['key_home']['Jazz']}/{base['key_home']['Default']}  "
             f"-> a system above the ceiling under-follows modulation")
    L.append("")
    L.append("SET-DIFF (per preset; A vs the committed reference)")
    for p in am.PRESETS:
        s = setdiff[p]
        L.append(f"  {p:8s} runs ref={s['runs_reference']} cand={s['runs_candidate']}  "
                 f"(+{s['added']} / -{s['removed']}); added class-b={s['added_class_b']} "
                 f"(dur {s['added_class_b_dur']}), removed class-b dur {s['removed_class_b_dur']}; "
                 f"GENUINE-NEW class-b runs={s['genuine_new_class_b_runs']} (dur {s['genuine_new_class_b_dur']})")
    L.append("")
    L.append("PREDICTIONS vs MEASURED")
    pm = g["predictions_vs_measured"]
    L.append(f"  class-b duration: predicted NET DECREASE 10-30%; measured "
             + ", ".join(f"{p} {pm['class_b_duration']['measured_pct_change'][p]:+.1f}%" for p in am.PRESETS))
    L.append(f"  key-local delta:  predicted +8..+13; measured "
             + ", ".join(f"{p} {pm['key_local']['measured_delta'][p]:+.1f}" for p in am.PRESETS))
    L.append(f"  key-home delta:   predicted -12..-18; measured "
             + ", ".join(f"{p} {pm['key_home']['measured_delta'][p]:+.1f}" for p in am.PRESETS))
    L.append(f"  RN delta:         predicted +12..+16; measured "
             + ", ".join(f"{p} {pm['rn']['measured_delta'][p]:+.1f}" for p in am.PRESETS))
    L.append(f"  root delta:       predicted large (known); measured "
             + ", ".join(f"{p} {pm['root']['measured_delta'][p]:+.1f}" for p in am.PRESETS))
    L.append(f"  modulation:       predicted in-band; measured {pm['modulation']['measured']} "
             f"band {pm['modulation']['band']} -> {'in' if pm['modulation']['within'] else 'OUT'}")
    L.append("")
    L.append(f"TIMING: decode mean {g['timing']['decode_mean_s']}s max {g['timing']['decode_max_s']}s "
             f"total {g['timing']['decode_total_s']}s (production scale, 326 pieces)")
    L.append("")
    L.append("robust_stop_diff.py verdict (authoritative gate output):")
    L.append(g["robust_stop_diff_stdout"].strip())
    OUT_SUMMARY.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:40]))


if __name__ == "__main__":
    main()
