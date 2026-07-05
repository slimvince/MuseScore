#!/usr/bin/env python3
"""stage5_2_2b_evidence.py — Stage-5 Phase-2.2b Task-1 evidence completion.

READ-ONLY / MEASUREMENT-ONLY. No src/ change, no frozen-corpus mutation, no gate change.
All regen goes to a manifest-stamped scratch root; the frozen tools/corpus is never touched.

Produces, per CARRIER (Baroque/Jazz/Default) at CURRENT weights, on the FULL corpus:
  (Task 1.1) the per-rule disable AUDIT table: root/RN/key deltas, batch-stop subset-diff
             (added/removed/class-changed, each with its two-tier class), class-(b)/(a)
             root-disagree DURATION deltas.  -> tools/fit_ledgers/stage5_rule_disable_fullcorpus.jsonl
  (Task 1.2) the per-rule FIRING SITES: diff the full-corpus regen (rule OFF vs baseline ON)
             at the union-of-region-boundaries cell grid; a cell whose chosen root_pc OR
             chord_symbol differs is an effective site.  Merged into runs; each site records
             stem@tick, our-root-ON, our-root-OFF, WiR root + WiR roman numeral (where covered),
             duration, two-tier class.  -> tools/fit_ledgers/stage5_rule_firing_sites.jsonl
  (Task 1.4) the Gate-J / BiasCorrection / GateE / GateH per-case tables are the firing sites
             of those four rules restricted to WiR-covered sites, with the WiR RN family
             (viio-family vs V-family vs other) tag — emitted inline in the firing-site rows.

Reuses verbatim: stage5_fit_driver (PARAMS / POST_SCORING_RULES / regen / measure /
write_override), compare_analyses (load_analysis / _dcml_time_spans / Region),
compare_rn (_active_index_at), dcml_parser (find_wir_file / parse_rntxt_file).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import stage5_fit_driver as drv     # noqa: E402
import compare_analyses as cmp      # noqa: E402
import compare_rn as crn            # noqa: E402
import dcml_parser as dcml          # noqa: E402

WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"
FIT_LEDGER_DIR = _ROOT / "tools" / "fit_ledgers"
AUDIT_LEDGER = FIT_LEDGER_DIR / "stage5_rule_disable_fullcorpus.jsonl"
FIRING_LEDGER = FIT_LEDGER_DIR / "stage5_rule_firing_sites.jsonl"
CARRIERS = ["Baroque", "Jazz", "Default"]
RULES = drv.POST_SCORING_RULES


# ── two-tier class of a region (reuse a8's exact test) ──────────────────────────────────
import a8_rebaseline_measure as a8  # noqa: E402


def region_class(region):
    return a8.cell_class(region)   # 'a' (pc-undecidable) or 'b' (pc-decidable)


# ── WiR (DCML) root + roman numeral at a tick, aligned to the ours regions ──────────────
def wir_context(stem, ours_regions):
    wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
    if not wir_path:
        return None, None
    try:
        wir = dcml.parse_rntxt_file(wir_path)
    except Exception:
        return None, None
    if not wir:
        return None, None
    spans = cmp._dcml_time_spans(ours_regions, wir)
    return wir, spans


def wir_at(wir, spans, tick):
    if wir is None or spans is None:
        return None, None
    di = crn._active_index_at(spans, tick)
    if di is None or di >= len(wir):
        return None, None
    r = wir[di]
    return r.root_pc, r.roman_numeral


def rn_family(numeral):
    """viio-family vs V-family vs other (Task 1.4 tension classifier)."""
    if not numeral:
        return "none"
    n = numeral.strip()
    low = n.lower()
    # strip a leading applied '/'-free numeral core
    core = low.lstrip("#b")
    if core.startswith("vii"):
        return "viio-family"
    if core.startswith("v") and not core.startswith("vi"):
        return "V-family"
    return "other"


# ── the per-cell firing-site diff (rule OFF vs baseline ON), union-of-boundaries grid ──
def firing_sites(base_regions, off_regions, wir, spans):
    """Cells where root_pc OR chord_symbol differ between baseline(ON) and rule-off(OFF).
    Merged into adjacent same-(on_root,off_root) runs. Boundaries are identical for a
    post-scoring gate, so the grid degrades to exact region alignment; the union grid is
    defensive against any boundary shift."""
    if not base_regions:
        return []
    bspans = [(r.start_tick, r.end_tick) for r in base_regions]
    ospans = [(r.start_tick, r.end_tick) for r in off_regions]
    bounds = set()
    for s, e in bspans + ospans:
        if e > s:
            bounds.add(s)
            bounds.add(e)
    grid = sorted(bounds)
    cells = []
    for i in range(len(grid) - 1):
        t0, t1 = grid[i], grid[i + 1]
        if t1 <= t0:
            continue
        bi = crn._active_index_at(bspans, t0)
        oi = crn._active_index_at(ospans, t0)
        br = base_regions[bi] if bi is not None else None
        orr = off_regions[oi] if oi is not None else None
        b_root = br.root_pc if br is not None else None
        o_root = orr.root_pc if orr is not None else None
        b_sym = br.chord_symbol if br is not None else None
        o_sym = orr.chord_symbol if orr is not None else None
        if b_root != o_root or b_sym != o_sym:
            cells.append((t0, t1, b_root, o_root, b_sym, o_sym, br))
    # merge adjacent cells with same (b_root,o_root,b_sym,o_sym)
    runs = []
    cur = None
    for t0, t1, b_root, o_root, b_sym, o_sym, br in cells:
        key = (b_root, o_root, b_sym, o_sym)
        if cur and cur["key"] == key and cur["end"] == t0:
            cur["end"] = t1
            cur["dur"] += (t1 - t0)
        else:
            if cur:
                runs.append(cur)
            cur = {"key": key, "start": t0, "end": t1, "dur": t1 - t0,
                   "on_root": b_root, "off_root": o_root,
                   "on_sym": b_sym, "off_sym": o_sym, "br": br}
        # keep the region ref of the run's first cell for class/pcs
    if cur:
        runs.append(cur)
    out = []
    for r in runs:
        wir_root, wir_num = wir_at(wir, spans, r["start"])
        out.append({
            "tick": r["start"], "end": r["end"], "dur": r["dur"],
            "on_root": r["on_root"], "off_root": r["off_root"],
            "on_sym": r["on_sym"], "off_sym": r["off_sym"],
            "wir_root": wir_root, "wir_rn": wir_num,
            "wir_family": rn_family(wir_num),
            "wir_covered": wir_root is not None,
            "cls": region_class(r["br"]) if r["br"] is not None else "b",
            "on_matches_wir": (r["on_root"] == wir_root) if wir_root is not None else None,
            "off_matches_wir": (r["off_root"] == wir_root) if wir_root is not None else None,
        })
    return out


def load_regions(path):
    _, regs = cmp.load_analysis(path)
    return regs


def audit_row(carrier, rule, base_m, m):
    added = sorted(c for c in m["cases"] if c not in base_m["cases"])
    removed = sorted(c for c in base_m["cases"] if c not in m["cases"])
    changed = sorted(c for c in m["cases"]
                     if c in base_m["cases"] and m["cases"][c] != base_m["cases"][c])
    return {
        "record": "audit", "carrier": carrier, "rule": rule, "split": "full",
        "root_pct": round(m["root_pct"], 4),
        "root_delta": round(m["root_pct"] - base_m["root_pct"], 4),
        "rn_pct": round(m["rn_pct"], 4),
        "rn_delta": round(m["rn_pct"] - base_m["rn_pct"], 4),
        "key_pct": round(m["key_pct"], 4),
        "key_delta": round(m["key_pct"] - base_m["key_pct"], 4),
        "batch_gate": m["batch_gate"],
        "batch_delta": m["batch_gate"] - base_m["batch_gate"],
        "batch_added": [{"case": c, "cls": m["cases"][c]} for c in added],
        "batch_removed": [{"case": c, "cls": base_m["cases"][c]} for c in removed],
        "batch_class_changed": [{"case": c, "from": base_m["cases"][c], "to": m["cases"][c]}
                                for c in changed],
        "cls_b_dur_delta": m["cls_b_dur"] - base_m["cls_b_dur"],
        "cls_a_dur_delta": m["cls_a_dur"] - base_m["cls_a_dur"],
    }


def done_keys(path, record):
    done = set()
    if path.exists():
        for ln in path.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(ln)
                if d.get("record") == record:
                    done.add((d["carrier"], d["rule"]))
            except Exception:
                pass
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scratch", default="C:/tmp/s5_2b")
    ap.add_argument("--carriers", default=",".join(CARRIERS))
    ap.add_argument("--rules", default=",".join(RULES))
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    scratch = Path(args.scratch)
    scratch.mkdir(parents=True, exist_ok=True)
    FIT_LEDGER_DIR.mkdir(parents=True, exist_ok=True)
    carriers = [c for c in args.carriers.split(",") if c]
    rules = [r for r in args.rules.split(",") if r]

    if not args.resume:
        for p in (AUDIT_LEDGER, FIRING_LEDGER):
            if p.exists():
                p.unlink()
    audit_done = done_keys(AUDIT_LEDGER, "audit")
    fire_done = done_keys(FIRING_LEDGER, "firing")

    for carrier in carriers:
        plower = carrier.lower()
        base_root_dir = scratch / carrier / "baseline"
        off_root_dir = scratch / carrier / "off"
        a8_base = scratch / carrier / "a8_base"
        a8_off = scratch / carrier / "a8_off"

        t0 = time.time()
        # baseline regen (kept for the region diff) — no override
        drv.regen(carrier, None, base_root_dir)
        base_m = drv.measure(carrier, base_root_dir, a8_base)
        base_regions_cache = {}
        for bp in sorted((base_root_dir / plower).glob("*.ours.json")):
            stem = bp.stem.replace(".ours", "")
            base_regions_cache[stem] = load_regions(bp)
        # write baseline audit record once (per carrier)
        if (carrier, "__baseline__") not in audit_done:
            with open(AUDIT_LEDGER, "a", encoding="utf-8") as f:
                f.write(json.dumps({
                    "record": "audit", "carrier": carrier, "rule": "__baseline__",
                    "split": "full", "root_pct": round(base_m["root_pct"], 4),
                    "rn_pct": round(base_m["rn_pct"], 4), "key_pct": round(base_m["key_pct"], 4),
                    "batch_gate": base_m["batch_gate"],
                    "cls_b_dur": base_m["cls_b_dur"], "cls_a_dur": base_m["cls_a_dur"],
                }, sort_keys=True) + "\n")
        print(f"[{carrier}] baseline root={base_m['root_pct']:.4f} rn={base_m['rn_pct']:.4f} "
              f"key={base_m['key_pct']:.4f} batch={base_m['batch_gate']} "
              f"({time.time()-t0:.0f}s)", flush=True)

        for rule in rules:
            if args.resume and (carrier, rule) in audit_done and (carrier, rule) in fire_done:
                continue
            tr = time.time()
            ov = off_root_dir / f"override_{plower}.txt"
            off_root_dir.mkdir(parents=True, exist_ok=True)
            drv.write_override({}, carrier, ov, disable_rules=[rule])
            drv.regen(carrier, str(ov).replace("\\", "/"), off_root_dir)
            m = drv.measure(carrier, off_root_dir, a8_off)

            # Task 1.1 audit row
            ar = audit_row(carrier, rule, base_m, m)
            with open(AUDIT_LEDGER, "a", encoding="utf-8") as f:
                f.write(json.dumps(ar, sort_keys=True) + "\n")

            # Task 1.2/1.4 firing sites
            n_sites = 0
            n_cov = 0
            with open(FIRING_LEDGER, "a", encoding="utf-8") as f:
                for op in sorted((off_root_dir / plower).glob("*.ours.json")):
                    stem = op.stem.replace(".ours", "")
                    base_regions = base_regions_cache.get(stem)
                    if base_regions is None:
                        continue
                    off_regions = load_regions(op)
                    wir, spans = wir_context(stem, base_regions)
                    sites = firing_sites(base_regions, off_regions, wir, spans)
                    for s in sites:
                        n_sites += 1
                        if s["wir_covered"]:
                            n_cov += 1
                        rec = {"record": "firing", "carrier": carrier, "rule": rule,
                               "stem": stem, **s}
                        f.write(json.dumps(rec, sort_keys=True) + "\n")
            print(f"  [{carrier}] {rule:<16} root_d={ar['root_delta']:+.4f} "
                  f"rn_d={ar['rn_delta']:+.4f} key_d={ar['key_delta']:+.4f} "
                  f"batch={ar['batch_gate']}({ar['batch_delta']:+d}) "
                  f"+{len(ar['batch_added'])}/-{len(ar['batch_removed'])}/~{len(ar['batch_class_changed'])} "
                  f"clsBd={ar['cls_b_dur_delta']:+g} clsAd={ar['cls_a_dur_delta']:+g} "
                  f"sites={n_sites}(cov={n_cov}) ({time.time()-tr:.0f}s)", flush=True)

    print("EVIDENCE DONE", flush=True)


if __name__ == "__main__":
    main()
