#!/usr/bin/env python3
"""l15_split.py — Stage-5 Phase 3 Task B: the L1.5 spike-vs-surface reliability split.

MEASUREMENT / VERDICT MATERIAL ONLY. Splits the L1.5 candidate ticks (phraseTextureTicks)
into two populations — deterministic MARKER SPIKES vs SURFACE CUES — and re-measures the
reliability curve per population. The C1 pooled curve put 97.7 % of ticks in one bin
because per-profile max-normalization is spike-dominated; this split asks whether either
population ALONE has usable spread + monotonicity (→ a per-population map could later be
fitted) or the deferral stands.

The split is code-truth: a spike adds spikeCeilingFactor*numVoices*sumWeights (=1.5*nV*1.0
default) which STRICTLY exceeds the max possible surface strength (numVoices*sumWeights),
phraseboundaryview.h §4.2. So a tick is a spike iff raw strength > numVoices*sumWeights.
`phraseNumVoices` is the additive dump field (Task B); sumWeights defaults to 1.0.

Reuses compare_l6_oracle's dev-bed machinery + dcml_parser verbatim.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_l6_oracle as l6
import dcml_parser as dcml

_ROOT = Path(__file__).resolve().parent.parent
SUM_WEIGHTS = 1.0   # wGap + wInterOnset + wPitch (phraseboundaryview.h defaults)


def bin_curve(pairs, nbins=10):
    bins = [dict(n=0, cw=0.0, confw=0.0) for _ in range(nbins)]
    for conf, correct in pairs:
        c = min(max(conf, 0.0), 1.0)
        idx = min(int(c * nbins), nbins - 1)
        b = bins[idx]
        b["n"] += 1; b["cw"] += correct; b["confw"] += c
    rows = []
    for i, b in enumerate(bins):
        emp = (b["cw"] / b["n"]) if b["n"] else None
        mconf = (b["confw"] / b["n"]) if b["n"] else None
        rows.append({"bin": i, "n": b["n"], "emp": emp, "mean_conf": mconf})
    return rows


def diagnostics(rows, n_total):
    ne = [r for r in rows if r["emp"] is not None]
    viol = 0
    prev = None
    for r in ne:
        if prev is not None and r["emp"] < prev["emp"] - 1e-9:
            viol += 1
        prev = r
    emps = [r["emp"] for r in ne]
    spread = (max(emps) - min(emps)) if emps else 0.0
    overall = (sum(r["emp"] * r["n"] for r in ne) / sum(r["n"] for r in ne)) if ne else None
    return {"monotonicity_violations": viol, "spread": spread,
            "overall_precision": overall, "nonempty_bins": len(ne)}


def measure(l6_root):
    spike_pairs, surf_pairs = [], []          # (norm strength within pop-per-profile, correct)
    spike_raw_ratio = []                       # min-spike-strength / numVoices (invariant check)
    n_movements = 0
    n_profiles_with_nv = 0
    tot_ticks = spike_ticks = surf_ticks = 0
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
            except Exception:
                continue
            tt = fs.get("phraseTextureTicks", [])
            ts = fs.get("phraseTextureStrength", [])
            nv = fs.get("phraseNumVoices", None)
            if not (tt and ts and len(tt) == len(ts)) or nv is None or nv <= 0:
                continue
            _cad, phr_mk = dcml.parse_cadence_phrase_markers(str(tsv))
            gt_phr = sorted(set(m.abs_tick for m in phr_mk if m.abs_tick is not None))
            if not gt_phr:
                continue
            n_profiles_with_nv += 1
            thr = nv * SUM_WEIGHTS
            tol = l6.TOLERANCE_TICKS
            spikes = [(t, s) for t, s in zip(tt, ts) if s > thr]
            surfs = [(t, s) for t, s in zip(tt, ts) if s <= thr]
            tot_ticks += len(tt); spike_ticks += len(spikes); surf_ticks += len(surfs)
            if spikes:
                spike_raw_ratio.append(min(s for _, s in spikes) / nv)
            # normalize WITHIN each population per profile (un-compress the surface cues)
            def add(pop, dest):
                if not pop:
                    return
                mx = max(s for _, s in pop)
                if mx <= 0:
                    return
                for t, s in pop:
                    near = any(abs(t - g) <= tol for g in gt_phr)
                    dest.append((s / mx, 1.0 if near else 0.0))
            add(spikes, spike_pairs)
            add(surfs, surf_pairs)
            n_movements += 1
    return {"spike": spike_pairs, "surf": surf_pairs, "spike_raw_ratio": spike_raw_ratio,
            "n_movements": n_movements, "n_profiles_with_nv": n_profiles_with_nv,
            "tot_ticks": tot_ticks, "spike_ticks": spike_ticks, "surf_ticks": surf_ticks}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--l6-root", default=str(_ROOT / "tools" / "corpus_l6_oracle"))
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    d = measure(args.l6_root)
    print("=" * 78)
    print("l15_split — Task B: L1.5 spike-vs-surface reliability (verdict material)")
    print("=" * 78)
    if d["n_profiles_with_nv"] == 0:
        print("NO profiles with phraseNumVoices — dev-bed fullspine not regenerated with the additive field.")
        return
    print(f"movements={d['n_movements']}  profiles_with_numVoices={d['n_profiles_with_nv']}")
    print(f"ticks total={d['tot_ticks']}  spike={d['spike_ticks']} ({d['spike_ticks']/d['tot_ticks']:.3f})  "
          f"surface={d['surf_ticks']} ({d['surf_ticks']/d['tot_ticks']:.3f})")
    if d["spike_raw_ratio"]:
        rr = d["spike_raw_ratio"]
        print(f"spike-floor invariant: min(spikeStrength)/numVoices  median={statistics.median(rr):.3f} "
              f"min={min(rr):.3f} (expect >= 1.5 = spikeCeilingFactor)")
    report = {"counts": {"movements": d["n_movements"], "tot_ticks": d["tot_ticks"],
                         "spike_ticks": d["spike_ticks"], "surf_ticks": d["surf_ticks"]},
              "spike_floor_ratio_median": (statistics.median(d["spike_raw_ratio"]) if d["spike_raw_ratio"] else None),
              "populations": {}}
    for name, pairs in (("SPIKE", d["spike"]), ("SURFACE", d["surf"])):
        rows = bin_curve(pairs)
        diag = diagnostics(rows, len(pairs))
        print(f"\n  {name} population (strength max-normalized WITHIN population, per profile):")
        print(f"    n={len(pairs)}  overall_precision={diag['overall_precision']}  "
              f"spread={diag['spread']:.3f}  monotonicity_violations={diag['monotonicity_violations']}  "
              f"nonempty_bins={diag['nonempty_bins']}")
        for r in rows:
            if r["n"]:
                print(f"      bin[{r['bin']/10:.1f},{(r['bin']+1)/10:.1f})  n={r['n']:>6}  "
                      f"emp={r['emp']:.3f}  mean_conf={r['mean_conf']:.3f}")
        report["populations"][name] = {"n": len(pairs), "diag": diag,
                                       "rows": [{k: r[k] for k in ('bin', 'n', 'emp', 'mean_conf')} for r in rows]}
    if args.out:
        Path(args.out).write_text(json.dumps(report, indent=1), encoding="utf-8")
        print(f"\n[wrote {args.out}]")


if __name__ == "__main__":
    main()
