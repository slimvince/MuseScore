#!/usr/bin/env python3
"""Phase-5c Step M — the read-only L5 (FUNCTION) would-be-engage measurement.

Reads the dormant Layer-5 would-be labels emitted by `batch_analyze --dump-l5` (the
`l5` array appended to each .ours.json — see writeL5Json in tools/batch_analyze.cpp)
and grades them against the DCML ground truth, per case, signed, two-tier — the
GO/NO-GO input for engaging L5 (Phase 5d).

REUSE, NOT RE-IMPLEMENT (cc_instruction Step M §1): the RN comparison is the committed
`compare_rn.classify_pair` / `score_regions` (the same equivalence/credit logic used for
the production RN), the ground truth is `dcml_parser` (oracle-correct When-in-Rome roots),
the alignment is `compare_analyses.align_dcml_regions`. This script only marshals the L5
RN into the SAME Region shape (dataclasses.replace) and diffs the two graded streams.

L5 is ADDITIVE over L4 (§7): the committed root is UNCHANGED on this (legacy region)
substrate — the relational label only changes the RN STRING. So the per-case diff is a
RN-string category change (exact/partial/key_disagree/quality_disagree), NEVER a root_pc
flip → class-(b)-NEUTRAL by construction. The script VERIFIES that (asserts root unchanged;
counts any legacy→L5 transition INTO root_err — must be 0).

Read-only: reads the .ours.json `l5`/`regions` + the WiR GT. Touches no production code.
"""
import argparse
import dataclasses
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp
import compare_rn as C
import dcml_parser as dcml

# Category quality rank (higher == closer to the DCML RN). rn_agree = exact|partial.
_RANK = {"exact": 4, "partial": 3, "key_disagree": 2, "quality_disagree": 2,
         "root_err": 0, None: -1}
_RN_AGREE = {"exact", "partial"}


# An APPLIED/secondary label is a '/' followed by a ROMAN-NUMERAL degree (V/V, viio/ii,
# V7/IV, vii%7/V, /N, /bVI). It must NOT match a figured-bass slash (V6/5, V4/3, V6/4,
# V4/2) where the '/' is followed by a DIGIT — those are inversion figures, not applied
# targets. (The earlier naive "/" test false-positived DCML's V6/5 as "applied".)
_APPLIED_RE = re.compile(r"/[#b]?[ivIVN]")


def _has_applied(rn: str) -> bool:
    return bool(_APPLIED_RE.search(C.normalise_rn(rn or "")))


def measure_preset(preset: str, corpus_dir: Path, wir_base: Path):
    files = sorted(corpus_dir.glob("*.ours.json"))
    legacy_agg = C.PieceStats()
    l5_agg = C.PieceStats()

    changed = []          # (stem, tick, legacyRN, l5RN, dclRN, leg_cat, l5_cat, sign, root, role)
    new_class_b = []      # legacy NOT root_err but L5 == root_err (must be empty)
    root_moved = []       # ours_r.root_pc != l5_r.root_pc (must be empty — additivity)
    applied_div = []      # §4: inline emits applied, L5 guard rejects → (stem,tick,inline,l5,dcl,verdict)
    role_counts = Counter()
    covered = 0
    no_wir = 0

    for p in files:
        stem = p.name.replace(".ours.json", "")
        try:
            data, ours_regions = cmp.load_analysis(p)
        except Exception:
            continue
        wir_path = dcml.find_wir_file(str(wir_base), stem)
        if not wir_path:
            no_wir += 1
            continue
        try:
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not ours_regions or not wir_regions:
            continue

        l5_arr = data.get("l5", [])
        if not l5_arr:
            continue
        l5_by_tick = {int(e["startTick"]): e for e in l5_arr}
        for e in l5_arr:
            role_counts[e.get("role", "None")] += 1

        # The parallel L5-RN stream: the SAME regions, roman_numeral replaced by the L5 RN.
        l5_regions = []
        for r in ours_regions:
            e = l5_by_tick.get(r.start_tick)
            l5rn = e["l5RomanNumeral"] if e else r.roman_numeral
            l5_regions.append(dataclasses.replace(r, roman_numeral=l5rn))

        covered += 1
        legacy_agg.add(C.score_regions(ours_regions, wir_regions))
        l5_agg.add(C.score_regions(l5_regions, wir_regions))

        # ── per-case diff (aligned to the GT) ─────────────────────────────────
        matches = cmp.align_dcml_regions(ours_regions, wir_regions,
                                         mode=cmp.DEFAULT_DCML_MATCH_MODE)
        for ours_r, l5_r, dr in zip(ours_regions, l5_regions, matches):
            if dr is None:
                continue
            # additivity guard: the L5 relational label never moves the root pc.
            if ours_r.root_pc != l5_r.root_pc:
                root_moved.append((stem, ours_r.start_tick, ours_r.root_pc, l5_r.root_pc))

            leg_pair = C.classify_pair(ours_r, dr)
            l5_pair = C.classify_pair(l5_r, dr)
            leg_cat = leg_pair.category if leg_pair else None
            l5_cat = l5_pair.category if l5_pair else None

            if C.normalise_rn(ours_r.roman_numeral) == C.normalise_rn(l5_r.roman_numeral):
                continue  # the RN string did not change → no L5 delta at this unit

            sign = _RANK[l5_cat] - _RANK[leg_cat]
            e = l5_by_tick.get(ours_r.start_tick, {})
            changed.append((stem, ours_r.start_tick, ours_r.roman_numeral,
                            l5_r.roman_numeral, dr.chord_symbol, leg_cat, l5_cat,
                            sign, ours_r.root_pc, e.get("role", "None")))
            if leg_cat != "root_err" and l5_cat == "root_err":
                new_class_b.append((stem, ours_r.start_tick, ours_r.roman_numeral,
                                    l5_r.roman_numeral, dr.chord_symbol))

        # ── §4 applied-divergence (inline emits applied, the L5 guard rejects) ─
        for e in l5_arr:
            inl, l5rn = e.get("inlineRomanNumeral", ""), e.get("l5RomanNumeral", "")
            if _has_applied(inl) and not _has_applied(l5rn):
                # the guard fired → L5 keeps the diatonic numeral. Which does DCML back?
                tick = int(e["startTick"])
                dcl = None
                for ours_r, dr in zip(ours_regions, matches):
                    if ours_r.start_tick == tick and dr is not None:
                        dcl = dr.chord_symbol
                        break
                verdict = "no_gt"
                if dcl is not None:
                    verdict = "dcml_applied(inline)" if _has_applied(dcl) else "dcml_diatonic(guard)"
                applied_div.append((stem, tick, inl, l5rn, dcl, verdict))

    return dict(preset=preset, covered=covered, no_wir=no_wir,
                legacy=legacy_agg, l5=l5_agg, changed=changed,
                new_class_b=new_class_b, root_moved=root_moved,
                applied_div=applied_div, role_counts=role_counts)


def _rn_agree(s):
    return s.exact + s.partial


def report(R):
    L = []
    leg, l5 = R["legacy"], R["l5"]
    m = leg.matched
    L.append("=" * 88)
    L.append(f"PRESET {R['preset'].upper()}   ({R['covered']} stems w/ WiR GT; {R['no_wir']} without)")
    L.append("=" * 88)
    L.append(f"  matched GT regions               : {m}")
    L.append(f"  rn_agree  LEGACY (production RN)  : {C._pct(_rn_agree(leg), m):5.1f}%  ({_rn_agree(leg)}/{m})")
    L.append(f"  rn_agree  L5     (would-be RN)    : {C._pct(_rn_agree(l5), m):5.1f}%  ({_rn_agree(l5)}/{m})")
    L.append(f"     --> would-be-engage rn_agree delta: {C._pct(_rn_agree(l5),m)-C._pct(_rn_agree(leg),m):+.2f} pts "
             f"({_rn_agree(l5)-_rn_agree(leg):+d} regions)")
    L.append(f"  exact     LEGACY / L5            : {leg.exact} / {l5.exact}   ({l5.exact-leg.exact:+d})")
    L.append(f"  root_agree (UNCHANGED — additive): {C._pct(leg.root_agree,leg.root_aligned):5.1f}% legacy"
             f"  vs {C._pct(l5.root_agree,l5.root_aligned):5.1f}% L5  ({l5.root_agree-leg.root_agree:+d})")
    L.append("")
    ch = R["changed"]
    improves = [c for c in ch if c[7] > 0]
    regresses = [c for c in ch if c[7] < 0]
    neutral = [c for c in ch if c[7] == 0]
    L.append(f"  L5 changed the RN string at {len(ch)} aligned units (signed vs DCML):")
    L.append(f"     improves : {len(improves)}   by role: "
             + ", ".join(f"{k}:{v}" for k, v in Counter(c[9] for c in improves).most_common()))
    L.append(f"     regresses: {len(regresses)}   by role: "
             + ", ".join(f"{k}:{v}" for k, v in Counter(c[9] for c in regresses).most_common()))
    L.append(f"     neutral  : {len(neutral)}  (same category rank; RN string differs)")
    # Applied OVER-TRIGGER (a regression where L5 emits an applied label but legacy was exact):
    overtrig = [c for c in regresses if c[9] == "AppliedSecondary" and c[5] == "exact"]
    L.append(f"     ↳ applied OVER-TRIGGER (legacy exact → L5 applied, root unchanged): {len(overtrig)}")
    for c in overtrig:
        L.append(f"          {c[0]}@{c[1]}: legacy={c[2]} -> L5={c[3]}  DCML={c[4]}")
    L.append("")
    L.append(f"  ★ CLASS-(b) gate (the GO criterion — pitch-class-decidable root read wrong):")
    L.append(f"     root pc MOVED by L5 (must be 0 — additive)         : {len(R['root_moved'])}")
    L.append(f"     NEW root_err (legacy ok → L5 root_err; must be 0)  : {len(R['new_class_b'])}")
    if R["new_class_b"]:
        for c in R["new_class_b"]:
            L.append(f"        !! {c[0]}@{c[1]}: legacy={c[2]} L5={c[3]} DCML={c[4]}")
    if R["root_moved"]:
        for c in R["root_moved"][:10]:
            L.append(f"        !! root moved {c[0]}@{c[1]}: {c[2]}->{c[3]}")
    L.append("")
    L.append(f"  L5 relational roles emitted (per-unit census): "
             + ", ".join(f"{k}:{v}" for k, v in R["role_counts"].most_common()))
    L.append("")
    # regressions + improvements detail
    if regresses:
        L.append(f"  REGRESSIONS (L5 RN further from DCML than legacy) — all {len(regresses)}:")
        for c in regresses:
            L.append(f"     {c[0]}@{c[1]} [{c[9]}]: legacy={c[2]}({c[5]}) -> L5={c[3]}({c[6]})  DCML={c[4]}")
        L.append("")
    if improves:
        L.append(f"  IMPROVEMENTS (L5 RN closer to DCML) — first 25 of {len(improves)}:")
        for c in improves[:25]:
            L.append(f"     {c[0]}@{c[1]} [{c[9]}]: legacy={c[2]}({c[5]}) -> L5={c[3]}({c[6]})  DCML={c[4]}")
        L.append("")
    # §4 applied divergences
    ad = R["applied_div"]
    L.append(f"  §4 APPLIED-DIVERGENCE (inline emits applied, the §5.6 guard rejects → L5 diatonic): {len(ad)} cases")
    vc = Counter(x[5] for x in ad)
    for k, v in vc.most_common():
        L.append(f"     {k:26s}: {v}")
    for x in ad[:30]:
        L.append(f"     {x[0]}@{x[1]}: inline={x[2]}  L5={x[3]}  DCML={x[4]}  -> {x[5]}")
    if len(ad) > 30:
        L.append(f"     ... +{len(ad)-30} more")
    L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus-root", default="tools/corpus",
                    help="dir holding per-preset subdirs with --dump-l5 .ours.json")
    ap.add_argument("--presets", nargs="+", default=["baroque", "jazz", "default"])
    ap.add_argument("--wir-base", default=str(C.WIR_BASE_DEFAULT))
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    root = Path(args.corpus_root)
    for preset in args.presets:
        cdir = root / preset
        if not cdir.is_dir():
            print(f"[skip] {cdir} not found"); continue
        R = measure_preset(preset, cdir, Path(args.wir_base))
        print(report(R))


if __name__ == "__main__":
    main()
