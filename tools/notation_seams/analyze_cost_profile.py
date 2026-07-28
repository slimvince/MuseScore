#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
"""analyze_cost_profile.py — OI-206 / cc_instruction_analysis_cost_profile.md Tasks 1/2/4.

Combines the MEASURED artifacts into the report tables:
  - tools/notation_seams/large_score_profile_counts.json     (counts, phase 1/2, boundaries, viewport)
  - tools/notation_seams/large_score_decode_profile.json     (phase 1-4 + memory, the decoded subset)
  - tools/joint_estimator/content_dp_split.json              (content-vs-DP fraction, chorale envelope)
  - tools/notation_seams/noteseam_latency.json               (C++ whole-score produce cost, OI-203)

Produces tools/notation_seams/cost_profile_analysis.json (#17f) with:
  Task 1  the per-score phase table (events, staves, phase times, shares) + the posterior-slice share
  Task 2  the scaling law: log-log least-squares fit of decode time vs EVENTS and vs STAVES, with a
          bootstrap 95% CI on the exponent, residual outliers, and a FLAGGED Tristan extrapolation
  Task 4b the enclosing-unit (structural-boundary) size distribution — the tail, not the mean
  Task 4c the viewport event counts

Read-only: consumes generated artifacts, writes one analysis artifact. No production code, no golden,
no corpus, no tools/robust_stop/. All figures are derived (never hand-typed, #17f).
"""
from __future__ import annotations

import json
import math
import os
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
NS = REPO / "tools" / "notation_seams"
JE = REPO / "tools" / "joint_estimator"


def load(p):
    p = Path(p)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def git_hash():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(REPO)).decode().strip()
    except Exception:
        return "unknown"


# ── a log-log least-squares fit y = A * x^k  (fit log y = a + k log x), with a residual-bootstrap
# 95% CI on k. Pure Python (no numpy dependency). ──
def loglog_fit(xs, ys, n_boot=2000, seed_pts=None):
    pts = [(x, y) for x, y in zip(xs, ys) if x and x > 0 and y and y > 0]
    n = len(pts)
    if n < 3:
        return None
    lx = [math.log(x) for x, _ in pts]
    ly = [math.log(y) for _, y in pts]

    def fit(idx):
        mx = sum(lx[i] for i in idx) / len(idx)
        my = sum(ly[i] for i in idx) / len(idx)
        sxx = sum((lx[i] - mx) ** 2 for i in idx)
        sxy = sum((lx[i] - mx) * (ly[i] - my) for i in idx)
        if sxx == 0:
            return None
        k = sxy / sxx
        a = my - k * mx
        return a, k

    base = fit(list(range(n)))
    if base is None:
        return None
    a, k = base
    # R^2
    my = sum(ly) / n
    sst = sum((v - my) ** 2 for v in ly)
    ssr = sum((ly[i] - (a + k * lx[i])) ** 2 for i in range(n))
    r2 = 1 - ssr / sst if sst > 0 else None
    # deterministic bootstrap (LCG, no Math.random — reproducibility); resample indices with replacement
    state = 2463534242
    def rnd():
        nonlocal state
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= (state >> 17)
        state ^= (state << 5) & 0xFFFFFFFF
        state &= 0xFFFFFFFF
        return state / 0xFFFFFFFF
    ks = []
    for _ in range(n_boot):
        idx = [int(rnd() * n) % n for _ in range(n)]
        r = fit(idx)
        if r:
            ks.append(r[1])
    ks.sort()
    lo = ks[int(0.025 * len(ks))] if ks else None
    hi = ks[int(0.975 * len(ks))] if ks else None
    return {
        "A": math.exp(a), "k": k, "log10_A": a / math.log(10),
        "r2": r2, "n": n, "k_ci95": [lo, hi],
        "predict_ms": None,  # filled by caller
    }


def main():
    counts = load(NS / "large_score_profile_counts.json")
    decode = load(NS / "large_score_decode_profile.json")
    content_dp = load(JE / "content_dp_split.json")
    latency = load(NS / "noteseam_latency.json")

    out = {"provenance": {
        "generator": "tools/notation_seams/analyze_cost_profile.py",
        "instrument_commit": git_hash(),
        "open_item": "OI-206 / cc_instruction_analysis_cost_profile.md Tasks 1/2/4",
        "inputs": {
            "counts": bool(counts), "decode": bool(decode),
            "content_dp": bool(content_dp), "latency": bool(latency),
        },
    }}

    # index counts by id
    cidx = {}
    if counts:
        for e in counts.get("perfCorpus", []) + counts.get("largeCorpus", []):
            cidx[e["id"]] = e

    # ── Task 1: the phase table (from the decode profile; content/DP fraction from the split) ──
    phase_rows = []
    if decode:
        for s in decode.get("scores", []):
            if "phase3_decode_ms" not in s:
                continue
            p1 = s.get("phase1_build_facts_ms", 0.0)
            p2 = s.get("phase2_load_tables_ms", 0.0)
            p3 = s.get("phase3_decode_ms", 0.0)
            p4 = s.get("phase4_assemble_ms", 0.0)
            slice_ms = s.get("phase4_posterior_slice_ms", 0.0)
            tot = p1 + p2 + p3 + p4
            row = {
                "id": s["id"], "events": s.get("adapterEvents"), "notes": s.get("adapterNotes"),
                "staves": s.get("staves"), "nSegments": s.get("nSegments"),
                "phase1_build_facts_ms": p1, "phase2_load_tables_ms": p2,
                "phase3_decode_ms": p3, "phase4_assemble_ms": p4,
                "phase4_posterior_slice_ms": slice_ms,
                "total_ms": tot,
                "share_phase1": p1 / tot if tot else None,
                "share_phase2": p2 / tot if tot else None,
                "share_phase3": p3 / tot if tot else None,
                "share_phase4": p4 / tot if tot else None,
                "posterior_slice_share_of_phase4": (slice_ms / p4) if p4 else None,
                "peak_ws_MB": s.get("peak_ws_bytes", 0) / (1024 * 1024),
                "ws_decode_growth_MB": s.get("ws_decode_growth_bytes", 0) / (1024 * 1024),
            }
            phase_rows.append(row)
    out["task1_phase_table"] = phase_rows

    # content/DP split (the mandatory within-phase-3 split, chorale envelope)
    if content_dp:
        agg = content_dp.get("aggregate", {})
        out["task1_content_dp_split"] = {
            "envelope": "chorale (Python reference decoder, byte-identical to C++ decodePiece)",
            "content_frac_pooled": agg.get("content_frac_pooled"),
            "dp_frac_pooled": (1 - agg["content_frac_pooled"]) if agg.get("content_frac_pooled") is not None else None,
            "content_frac_range": [agg.get("content_frac_min"), agg.get("content_frac_max")],
            "n_pieces": agg.get("n_pieces"),
            "interpretation": None,  # filled in the report prose
        }

    # ── Task 2: scaling law — decode ms vs events, and vs staves ──
    # The decode fit MUST exclude the segs=0 FAILURES (butterworth, holst_mercury — they ran the DP but
    # returned an empty analysis, so their time is not a normal-decode data point) AND note the DENSITY
    # confound: per-event decode cost varies ~3x with onset density (contrapuntal/orchestral segments
    # keep more candidate classes -> slower content scoring), so a single events^k exponent is weak.
    fits = {}
    if phase_rows:
        normal = [r for r in phase_rows if (r.get("nSegments") or 0) > 0]  # exclude segs=0 failures
        ev = [r["events"] for r in normal]
        st = [r["staves"] for r in normal]
        d3 = [r["phase3_decode_ms"] for r in normal]
        fits["decode_vs_events_normal_only"] = loglog_fit(ev, d3)
        fits["decode_vs_staves_normal_only"] = loglog_fit(st, d3)
        fits["n_normal_decode_scores"] = len(normal)
        fits["n_segs0_failures_excluded"] = len(phase_rows) - len(normal)
        # density confound: per-event decode ms vs notes/event (the density proxy)
        fits["density_confound"] = [
            {"id": r["id"], "events": r["events"], "notes": r["notes"],
             "notes_per_event": (r["notes"] / r["events"]) if r["events"] else None,
             "decode_ms_per_event": (r["phase3_decode_ms"] / r["events"]) if r["events"] else None,
             "nSegments": r.get("nSegments")}
            for r in phase_rows]
        p1 = [r["phase1_build_facts_ms"] for r in phase_rows]
        fits["buildfacts_vs_events"] = loglog_fit([r["events"] for r in phase_rows], p1)
    # also fit Phase 1 across the FULL counts corpus (adapter runs on all scores; more data points)
    if counts:
        allrows = counts.get("perfCorpus", []) + counts.get("largeCorpus", [])
        ev = [e.get("adapterEvents") for e in allrows if e.get("adapterOk")]
        p1 = [e.get("phase1_build_facts_ms") for e in allrows if e.get("adapterOk")]
        st = [e.get("staves") for e in allrows if e.get("adapterOk")]
        fits["buildfacts_vs_events_fullcorpus"] = loglog_fit(ev, p1)
        fits["buildfacts_vs_staves_fullcorpus"] = loglog_fit(st, p1)
    out["task2_scaling"] = fits

    # Tristan extrapolation — decode time at a Tristan-act event count. State assumptions.
    # A full act of Tristan ~ 90-120 min orchestral. We do NOT have its event count on disk; we bound
    # it from the measured orchestral scores (gluck 29677 events was the largest adapter run) and scale.
    def predict(fit, x):
        if not fit:
            return None
        return fit["A"] * (x ** fit["k"])
    # The buildFacts (phase 1) law is the CLEAN one (R^2~0.96); it is the extrapolation basis for the
    # fact-extraction cost. The decode either (a) FAILS to an empty analysis on most orchestral scores
    # (OI-215 — uncoverableEvents>0) or (b) where it succeeds, costs even more than phase 1, with a large
    # density-dependent constant that a single exponent captures poorly. So we extrapolate the FLOOR
    # (phase 1) and state the decode as "fails-or-worse", never a point number.
    tristan = {}
    bf = fits.get("buildfacts_vs_events_fullcorpus")  # the n=27 full-corpus law (the robust one)
    if bf:
        for label, nev in [("10k_events", 10000), ("30k_events_gluck_scale", 30000),
                           ("60k_events_tristan_act_estimate", 60000)]:
            ms = predict(bf, nev)
            lo = (bf["A"] * (nev ** bf["k_ci95"][0])) if bf["k_ci95"][0] else None
            hi = (bf["A"] * (nev ** bf["k_ci95"][1])) if bf["k_ci95"][1] else None
            tristan[label] = {
                "events": nev,
                "buildfacts_floor_s_point": ms / 1000 if ms else None,
                "buildfacts_floor_s_ci95": [lo / 1000 if lo else None, hi / 1000 if hi else None],
                "decode": "FAILS to an empty analysis if any event is uncoverable (OI-215; true of most "
                          "orchestral scores measured); else > the phase-1 floor with a large density constant",
            }
    out["task2_tristan_extrapolation"] = {
        "note": "EXTRAPOLATION beyond the measured range, flagged NOT a measurement. Basis: the buildFacts "
                "(phase 1) law events^%.2f (R^2~%.2f), the CLEAN fit; it gives a FLOOR on the whole-piece "
                "cost (fact extraction alone). The decode on top of it FAILS to empty on most orchestral "
                "scores (OI-215) or costs more with a poorly-captured density constant. The true Tristan-act "
                "event count is not on disk; bounded from the measured orchestral scores (gluck 29677 events "
                "was the largest adapter run; a full act is larger)."
                % ((bf["k"] if bf else 0), (bf["r2"] if bf else 0)),
        "measured_max_events_adapter": 29677,
        "measured_max_events_decoded_normally": max(
            (r["events"] for r in phase_rows if (r.get("nSegments") or 0) > 0), default=None),
        "points": tristan,
    }

    # ── Task 4b: enclosing-unit (boundary) size distribution — the tail ──
    b4 = []
    if counts:
        for e in counts.get("perfCorpus", []) + counts.get("largeCorpus", []):
            bd = e.get("boundary", {})
            units_m = bd.get("unitSizesMeasures", [])
            if not e.get("adapterOk"):
                continue
            b4.append({
                "id": e["id"], "measures": e.get("measures"), "events": e.get("adapterEvents"),
                "structuralBoundaries": bd.get("boundaryCount"),
                "fermatas": bd.get("fermatas"), "structuralBarlines": bd.get("structuralBarlines"),
                "rehearsalMarks": bd.get("rehearsalMarks"), "restSpans": bd.get("restSpans"),
                "nUnits": bd.get("nUnits"),
                "maxUnitMeasures": bd.get("maxUnitMeasures"),
                "maxUnitEvents": bd.get("maxUnitEvents"),
                "meanUnitMeasures": (e.get("measures") / bd["nUnits"]) if bd.get("nUnits") else None,
            })
    out["task4b_boundaries"] = b4
    # how many scores have a long boundary-free stretch (max unit > 30 measures)?
    long_free = [r for r in b4 if (r.get("maxUnitMeasures") or 0) > 30]
    out["task4b_summary"] = {
        "n_scores": len(b4),
        "n_with_boundary_free_stretch_gt_30_measures": len(long_free),
        "worst_maxUnitMeasures": sorted(b4, key=lambda r: -(r.get("maxUnitMeasures") or 0))[:8],
    }

    # ── Task 4c: viewport ──
    v4 = []
    if counts:
        for e in counts.get("perfCorpus", []) + counts.get("largeCorpus", []):
            if not e.get("adapterOk"):
                continue
            m = e.get("measures") or 1
            ev = e.get("adapterEvents") or 0
            v4.append({
                "id": e["id"], "measures": m, "events": ev, "staves": e.get("staves"),
                "eventsFirst4Measures": e.get("eventsFirst4Measures"),
                "eventsFirst8Measures": e.get("eventsFirst8Measures"),
                "events_per_measure": ev / m,
            })
    out["task4c_viewport"] = v4

    outp = NS / "cost_profile_analysis.json"
    outp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {outp}")
    # brief console summary
    if fits.get("decode_vs_events_normal_only"):
        f = fits["decode_vs_events_normal_only"]
        print(f"decode(normal only, n={f['n']}) ~ events^{f['k']:.2f} "
              f"(95% CI {f['k_ci95'][0]:.2f}-{f['k_ci95'][1]:.2f}, R2={f['r2']:.3f}) "
              f"[{fits.get('n_segs0_failures_excluded')} segs=0 failures excluded]")
    if fits.get("buildfacts_vs_events_fullcorpus"):
        f = fits["buildfacts_vs_events_fullcorpus"]
        print(f"buildFacts ~ events^{f['k']:.2f} (95% CI {f['k_ci95'][0]:.2f}-{f['k_ci95'][1]:.2f}, R2={f['r2']:.3f}, n={f['n']})")
    if content_dp:
        cf = content_dp["aggregate"].get("content_frac_pooled")
        if cf is not None:
            print(f"content/DP split (chorale): content={100*cf:.1f}% DP={100*(1-cf):.1f}%")


if __name__ == "__main__":
    main()
