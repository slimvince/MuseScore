#!/usr/bin/env python3
"""E0 — the dormant FULL-SPINE (L1→L5) read-only measurement grader.

Grades the full-spine side files emitted by `batch_analyze --dump-fullspine` (the
L1→L2→L3(live)→L4-decoder→L5 chain — see runFullSpine in tools/batch_analyze.cpp)
against BOTH frozen references: the DCML/WiR ground truth AND the legacy spine (the
flag-OFF corpus). Produces the nine E0 measures per cowork_engage_criteria.md §3, with
the Cowork-ratified riders (2026-07-02): RN accuracy at THREE levels (root / triad-
normalized / raw-full-diagnostic), and measure #7 split into the firable vs
structurally-non-firable relational-label sets.

REUSE, NOT RE-IMPLEMENT: every metric primitive is the committed tooling —
compare_rn.score_regions / grid_score_regions / classify_pair / normalise_rn /
PieceStats / GridStats (the SAME region-count + granularity-robust units used for the
production RN and the gate), compare_analyses.load_analysis / align_dcml_regions, and
dcml_parser (oracle-correct WiR roots). This script only marshals the two graded
streams, triad-normalizes for the fair capped RN comparison, and reads the E0-specific
fields the standard loaders ignore (l4Decision / l4RootPc / l5OverrodeCommit / openMark
/ ambiguityKind / l5Role / l4Composite / l5Combined / wallTime*).

Read-only. The base RN is TRIAD-LEVEL by construction (the L4→L5 carry drops the
seventh/extensions — report §4 carry-contract finding); the raw-full-RN level is a
CAPPED diagnostic, never a verdict (rider 1).
"""
import argparse
import dataclasses
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp
import compare_rn as C
import dcml_parser as dcml

_RN_AGREE = {"exact", "partial"}
# Symmetric / pitch-class-undecidable qualities (two-tier policy class-(a) seed).
_SYM_QUALITIES = {"Diminished", "Augmented", "HalfDiminished"}
_SYM_AMBIG = {"SymmetricRotation", "ShareTone", "RelativePair"}
# An APPLIED target = '/' + roman degree (not a figured-bass '/'+digit).
_APPLIED_RE = re.compile(r"/[#b]?[ivIVN]")
# A DCML applied DOMINANT-SEVENTH (V7/x, V65/x, V43/x, V42/x) — the non-firable class.
_DCML_V7_APPLIED_RE = re.compile(r"\bV(7|65|43|42|6/5|4/3|4/2)/[#b]?[ivIVN]", re.I)
_GER6_RE = re.compile(r"Ger", re.I)


def triad_norm(rn: str) -> str:
    """Strip figured-bass digits + seventh/extension markers to a triad-level RN,
    preserving the degree (case = triad quality), any accidental, the o/ø/+ triad
    quality marker (ø→o: a half-diminished's TRIAD is diminished), and any applied
    target. The fair capped unit (rider 1): both sides + DCML normalized before
    comparison so V==V7, viio==viio7, I==I6."""
    s = C.normalise_rn(rn or "")
    if not s:
        return s
    target = ""
    if _APPLIED_RE.search(s):
        idx = s.rfind("/")
        if idx >= 0:
            target = s[idx:]
            s = s[:idx]
    def strip(x: str) -> str:
        x = re.sub(r"\d", "", x)          # drop all figured-bass / seventh digits
        x = x.replace("ø", "o")           # half-dim triad == dim
        x = re.sub(r"(maj|M|Δ)", "", x)   # drop major-seventh markers
        return x
    return strip(s) + (("/" + strip(target[1:])) if target else "")


def _norm_ours(regions, tn: bool):
    if not tn:
        return regions
    return [dataclasses.replace(r, roman_numeral=triad_norm(r.roman_numeral)) for r in regions]


def _norm_wir(regions, tn: bool):
    if not tn:
        return regions
    return [dataclasses.replace(r, chord_symbol=triad_norm(r.chord_symbol)) for r in regions]


def _rn_agree(s: C.PieceStats) -> int:
    return s.exact + s.partial


def _grid_agree(g: C.GridStats) -> int:
    return g.bucket_dur.get("exact", 0) + g.bucket_dur.get("partial", 0)


def _pct(n, d):
    return 100.0 * n / d if d else 0.0


def _pctl(xs, q):
    if not xs:
        return 0.0
    xs = sorted(xs)
    k = max(0, min(len(xs) - 1, int(round(q * (len(xs) - 1)))))
    return xs[k]


def measure_preset(preset, fs_dir: Path, legacy_dir: Path, wir_base: Path):
    fs_files = sorted(fs_dir.glob("*.ours.json"))

    # region-count PieceStats + granularity-robust GridStats, per level, per stream
    acc = {k: C.PieceStats() for k in ("chain_raw", "chain_triad", "leg_raw", "leg_triad")}
    grid = {k: C.GridStats() for k in ("chain_raw", "chain_triad", "leg_raw", "leg_triad")}

    covered = no_wir = no_legacy = 0

    # E0-specific accumulators
    l4_wrong_root = 0            # L4 committed a (non-symmetric) decidable root != DCML
    l4_wrong_sym = 0            # ditto but symmetric quality/ambiguity (class-(a) seed)
    override_fired = 0
    override_corrected = []      # (stem, tick, l4Decision, l4Root, finalRoot, dcmlRoot)
    override_residual = []       # L4 wrong (decidable) + NOT corrected by override
    override_regressed = []      # L4 root WAS right, override moved it wrong (safety)
    by_decision_wrong = Counter()      # l4Decision -> count of decidable L4-wrong
    by_decision_corrected = Counter()  # l4Decision -> count corrected by override
    by_decision_residual = Counter()   # l4Decision -> count NOT corrected (the extend-to-Inherit question)

    classb_moves = []            # chain moves root vs legacy: NEW class-(b) (chain worse)
    classb_fixes = []            # chain fixes a legacy root error (decidable)
    classa_moves = []            # symmetric root churn (either direction)

    abst_total = 0
    abst_defensible = []         # openMark where the best-guess root != DCML (abstain avoided a wrong commit)
    abst_costly = []             # openMark where the best-guess root == DCML (abstained on a gettable one)

    role_counts = Counter()      # chain relational roles emitted
    firable_by_dcml = 0          # DCML units whose (triad-normed) label is a FIRABLE relational role
    dcml_v7_applied = 0          # DCML applied dominant-SEVENTH occurrences (non-firable cap component)
    dcml_ger6 = 0                # DCML Ger+6 occurrences (non-firable cap component)

    l4_composite, l5_combined = [], []
    wall_decode, wall_legacy = [], []
    tot_slices = tot_committed = tot_abstain = tot_openmark = tot_overrode = 0

    over_trigger = Counter()     # #7: chain emits AppliedSecondary but DCML has a plain diatonic (target degree)

    for p in fs_files:
        stem = p.name.replace(".ours.json", "")
        try:
            data, chain_regions = cmp.load_analysis(p)
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
        if not chain_regions or not wir_regions:
            continue

        legacy_regions = None
        lp = legacy_dir / p.name
        if lp.exists():
            try:
                _, legacy_regions = cmp.load_analysis(lp)
            except Exception:
                legacy_regions = None
        if not legacy_regions:
            no_legacy += 1

        covered += 1

        # ── #1 RN at three levels (region-count + granularity-robust) ──
        # Score over CHORDED units only (root_pc >= 0): a final open mark is an
        # honest abstention, scored separately in #4 — never as a root_err here
        # (an openMark's thin duration falls to the grid's unscored bucket). The
        # legacy stream commits everywhere, so its filter is inert.
        chain_chorded = [r for r in chain_regions if r.root_pc is not None and r.root_pc >= 0]
        legacy_chorded = ([r for r in legacy_regions if r.root_pc is not None and r.root_pc >= 0]
                          if legacy_regions else None)
        for tn, key in ((False, "raw"), (True, "triad")):
            ow = _norm_ours(chain_chorded, tn)
            dw = _norm_wir(wir_regions, tn)
            acc[f"chain_{key}"].add(C.score_regions(ow, dw))
            grid[f"chain_{key}"].add(C.grid_score_regions(ow, dw))
            if legacy_chorded:
                low = _norm_ours(legacy_chorded, tn)
                acc[f"leg_{key}"].add(C.score_regions(low, dw))
                grid[f"leg_{key}"].add(C.grid_score_regions(low, dw))

        # top-level fields
        wall_decode.append(float(data.get("wallTimeDecodeMs", 0.0)))
        wall_legacy.append(float(data.get("wallTimeLegacyMs", 0.0)))
        tot_slices += int(data.get("slicesTotal", 0))
        tot_committed += int(data.get("committedUnits", 0))
        tot_abstain += int(data.get("abstainUnits", 0))
        tot_openmark += int(data.get("openMarkUnits", 0))
        tot_overrode += int(data.get("overrodeCommits", 0))

        # ── align chain units to DCML (per-unit E0 measures) ──
        matches = cmp.align_dcml_regions(chain_regions, wir_regions,
                                         mode=cmp.DEFAULT_DCML_MATCH_MODE)
        raw_by_tick = {int(r.get("startTick", -1)): r for r in data.get("regions", [])}
        for cr, dr in zip(chain_regions, matches):
            raw = raw_by_tick.get(cr.start_tick, {})
            l4root = int(raw.get("l4RootPc", -1))
            l4dec = raw.get("l4Decision", "Commit")
            overrode = bool(raw.get("l5OverrodeCommit", False))
            openmark = bool(raw.get("openMark", False))
            ambig = raw.get("ambiguityKind", "None")
            role = raw.get("l5Role", "None")
            qual = raw.get("quality", "Unknown")
            comp = float(raw.get("l4Composite", 0.0))
            comb = float(raw.get("l5Combined", 0.0))
            if cr.root_pc is not None and cr.root_pc >= 0:
                l4_composite.append(comp)
                l5_combined.append(comb)
            if role != "None":
                role_counts[role] += 1

            if dr is None or dr.root_pc is None:
                continue
            symmetric = (qual in _SYM_QUALITIES) or (ambig in _SYM_AMBIG)

            # ── #6 override-duty: L4 committed a DECIDABLE root wrong; did the
            #     §5.5 case-4 override correct it? split by Commit / Inherit ──
            if l4dec in ("Commit", "Inherit") and l4root >= 0 and l4root != dr.root_pc:
                if symmetric:
                    l4_wrong_sym += 1
                else:
                    l4_wrong_root += 1
                    by_decision_wrong[l4dec] += 1
                    final = cr.root_pc
                    if overrode and final == dr.root_pc:
                        override_corrected.append((stem, cr.start_tick, l4dec, l4root, final, dr.root_pc))
                        by_decision_corrected[l4dec] += 1
                    else:
                        override_residual.append((stem, cr.start_tick, l4dec, l4root, cr.root_pc, dr.root_pc))
                        by_decision_residual[l4dec] += 1
            elif l4dec in ("Commit", "Inherit") and l4root >= 0 and l4root == dr.root_pc:
                # L4 root was CORRECT; did the override move it wrong? (safety)
                if overrode and cr.root_pc != dr.root_pc:
                    override_regressed.append((stem, cr.start_tick, l4dec, l4root, cr.root_pc, dr.root_pc))
            if overrode:
                override_fired += 1

            # ── #4 abstention ──
            if openmark:
                abst_total += 1
                guess = l4root if l4root >= 0 else cr.root_pc
                if guess >= 0 and guess != dr.root_pc:
                    abst_defensible.append((stem, cr.start_tick, guess, dr.root_pc))
                elif guess == dr.root_pc:
                    abst_costly.append((stem, cr.start_tick, guess, dr.root_pc))

            # ── #7 relational: over-trigger (chain applied where DCML diatonic) ──
            if role == "AppliedSecondary":
                d_applied = bool(_APPLIED_RE.search(C.normalise_rn(dr.chord_symbol or "")))
                if not d_applied:
                    over_trigger[stem] += 1

        # ── #7 DCML non-firable-label census (the cap's 2nd component) ──
        for d in wir_regions:
            csym = d.chord_symbol or ""
            if _DCML_V7_APPLIED_RE.search(csym):
                dcml_v7_applied += 1
            if _GER6_RE.search(csym):
                dcml_ger6 += 1
            tnl = triad_norm(csym)
            if _APPLIED_RE.search(tnl) or tnl.startswith("N") or tnl.lower().startswith("b"):
                firable_by_dcml += 1

        # ── #5 class-(b)/(a): chain root vs legacy root vs DCML, per DCML region ──
        if legacy_regions:
            leg_match = cmp.align_dcml_regions(legacy_regions, wir_regions,
                                               mode=cmp.DEFAULT_DCML_MATCH_MODE)
            # legacy root per DCML region (by identity of the matched dcml region)
            leg_root_for = {}
            for lr, ld in zip(legacy_regions, leg_match):
                if ld is not None:
                    leg_root_for[id(ld)] = lr.root_pc
            for cr, dr in zip(chain_regions, matches):
                if dr is None or dr.root_pc is None:
                    continue
                lroot = leg_root_for.get(id(dr))
                if lroot is None:
                    continue
                croot = cr.root_pc
                if croot == lroot:
                    continue
                raw = raw_by_tick.get(cr.start_tick, {})
                qual = raw.get("quality", "Unknown")
                ambig = raw.get("ambiguityKind", "None")
                symmetric = (qual in _SYM_QUALITIES) or (ambig in _SYM_AMBIG)
                chain_ok = (croot == dr.root_pc)
                leg_ok = (lroot == dr.root_pc)
                rec = (stem, cr.start_tick, lroot, croot, dr.root_pc, qual, ambig)
                if symmetric:
                    classa_moves.append(rec)
                elif leg_ok and not chain_ok:
                    classb_moves.append(rec)       # NEW class-(b): chain worse than legacy
                elif chain_ok and not leg_ok:
                    classb_fixes.append(rec)       # chain fixes a legacy decidable error

    return dict(
        preset=preset, covered=covered, no_wir=no_wir, no_legacy=no_legacy,
        acc=acc, grid=grid,
        l4_wrong_root=l4_wrong_root, l4_wrong_sym=l4_wrong_sym,
        override_fired=override_fired, override_corrected=override_corrected,
        override_residual=override_residual, override_regressed=override_regressed,
        by_decision_wrong=by_decision_wrong, by_decision_corrected=by_decision_corrected,
        by_decision_residual=by_decision_residual,
        classb_moves=classb_moves, classb_fixes=classb_fixes, classa_moves=classa_moves,
        abst_total=abst_total, abst_defensible=abst_defensible, abst_costly=abst_costly,
        role_counts=role_counts, firable_by_dcml=firable_by_dcml,
        dcml_v7_applied=dcml_v7_applied, dcml_ger6=dcml_ger6,
        l4_composite=l4_composite, l5_combined=l5_combined,
        wall_decode=wall_decode, wall_legacy=wall_legacy,
        over_trigger=over_trigger,
        tot_slices=tot_slices, tot_committed=tot_committed, tot_abstain=tot_abstain,
        tot_openmark=tot_openmark, tot_overrode=tot_overrode,
    )


def report(R):
    L = []
    P = R["preset"].upper()
    L.append("=" * 92)
    L.append(f"PRESET {P}   ({R['covered']} stems w/ WiR GT; {R['no_wir']} without; "
             f"{R['no_legacy']} without legacy)")
    L.append("=" * 92)

    def rn_line(tag, key):
        s = R["acc"][key]; g = R["grid"][key]
        m = s.matched; sd = g.scored_dur
        return (f"    {tag:14s} region rn_agree {_pct(_rn_agree(s), m):5.1f}% ({_rn_agree(s)}/{m})"
                f"   robust(dur) {_pct(_grid_agree(g), sd):5.1f}%   root_agree {_pct(s.root_agree, s.root_aligned):5.1f}%")

    L.append("  #1 RN ACCURACY (rider 1 — three levels):")
    L.append("   ROOT-LEVEL (uncapped, verdict):")
    L.append(rn_line("chain", "chain_raw"))
    L.append(rn_line("legacy", "leg_raw"))
    L.append("   TRIAD-NORMALIZED RN (fair capped, verdict):")
    L.append(rn_line("chain", "chain_triad"))
    L.append(rn_line("legacy", "leg_triad"))
    L.append("   RAW FULL-RN (carry-capped DIAGNOSTIC — artifact: seventh/extension drop; NOT a verdict):")
    L.append(rn_line("chain", "chain_raw"))
    cap_region = _pct(_rn_agree(R["acc"]["chain_triad"]), R["acc"]["chain_triad"].matched) \
               - _pct(_rn_agree(R["acc"]["chain_raw"]), R["acc"]["chain_raw"].matched)
    L.append(f"     → cap size (triad − raw, chain, region): {cap_region:+.1f} pts")
    L.append("")

    L.append("  #2 KEY (S1/S2 split — within key_disagree):")
    for tag, key in (("chain", "chain_triad"), ("legacy", "leg_triad")):
        s = R["acc"][key]
        L.append(f"    {tag:7s} key_disagree {s.key_disagree}  (S1 eq-global {s.kd_eq_global} / "
                 f"S2 ne-global {s.kd_ne_global}; keyfail {s.kd_keyfail})  keyparse_fail {s.keyparse_fail}")
    L.append("")

    L.append("  ★#6 OVERRIDE-DUTY (the headline — §5.5 case-4 on the decoder substrate):")
    L.append(f"    L4 committed a DECIDABLE root WRONG (non-symmetric)   : {R['l4_wrong_root']}")
    L.append(f"       by decision: " + ", ".join(f"{k}:{v}" for k, v in R["by_decision_wrong"].most_common()))
    L.append(f"    corrected by the §5.5 override                        : {len(R['override_corrected'])}")
    L.append(f"       by decision: " + ", ".join(f"{k}:{v}" for k, v in R["by_decision_corrected"].most_common()))
    L.append(f"    RESIDUAL (decidable L4-wrong NOT corrected)           : {len(R['override_residual'])}")
    L.append(f"       residual by decision (extend-to-Inherit?): "
             + ", ".join(f"{k}:{v}" for k, v in R["by_decision_residual"].most_common()))
    L.append(f"    ⚠ override REGRESSED a correct L4 commit (safety)     : {len(R['override_regressed'])}")
    for c in R["override_regressed"][:20]:
        L.append(f"        regressed {c[0]}@{c[1]} [{c[2]}]: L4root={c[3]}(=DCML) → final={c[4]} DCML={c[5]}")
    L.append(f"    (symmetric/undecidable L4-wrong, class-(a) seed)      : {R['l4_wrong_sym']}")
    L.append(f"    overrides fired total                                 : {R['override_fired']}")
    for c in R["override_residual"][:40]:
        L.append(f"        residual {c[0]}@{c[1]} [{c[2]}]: L4root={c[3]} final={c[4]} DCML={c[5]}")
    if len(R["override_residual"]) > 40:
        L.append(f"        ... +{len(R['override_residual'])-40} more")
    L.append("")

    L.append("  #5 TWO-TIER CASE DELTAS (chain root vs legacy root vs DCML; identity sets):")
    L.append(f"    NEW class-(b)  (legacy right → chain wrong, decidable): {len(R['classb_moves'])}")
    for c in R["classb_moves"]:
        L.append(f"        !! classb {c[0]}@{c[1]}: leg={c[2]} chain={c[3]} DCML={c[4]} q={c[5]}")
    L.append(f"    class-(b) FIXES (chain right → legacy wrong, decidable): {len(R['classb_fixes'])}")
    for c in R["classb_fixes"][:20]:
        L.append(f"        fix {c[0]}@{c[1]}: leg={c[2]} chain={c[3]} DCML={c[4]} q={c[5]}")
    if len(R["classb_fixes"]) > 20:
        L.append(f"        ... +{len(R['classb_fixes'])-20} more")
    L.append(f"    class-(a) symmetric churn (either direction)          : {len(R['classa_moves'])}")
    L.append("")

    L.append("  #4 ABSTENTION (correct-abstention scored separately):")
    ts, tc, ta, to, tv = (R["tot_slices"], R["tot_committed"], R["tot_abstain"],
                          R["tot_openmark"], R["tot_overrode"])
    L.append(f"    slices {ts}  committed {tc} ({_pct(tc,ts):.1f}%)  L4-abstain {ta} ({_pct(ta,ts):.1f}%)")
    L.append(f"    FINAL open marks (L5 unresolved) {to} ({_pct(to,ts):.1f}% of slices)  "
             f"→ resolver resolved {ta-to} of {ta} L4 abstains")
    L.append(f"    override commits fired (top-level) {tv}")
    L.append(f"    open-mark cases aligned to GT            : {R['abst_total']}")
    L.append(f"    defensible (best-guess root != DCML)     : {len(R['abst_defensible'])}")
    L.append(f"    costly (best-guess root == DCML)         : {len(R['abst_costly'])}")
    L.append("")

    L.append("  #7 RELATIONAL LABELS (rider 2 — firable vs structurally non-firable):")
    L.append(f"    chain roles emitted: " + (", ".join(f"{k}:{v}" for k, v in R["role_counts"].most_common()) or "none"))
    L.append(f"    FIRABLE set (viio/x, Neapolitan, modal-mixture) — scoreable")
    L.append(f"    NON-FIRABLE on this substrate (seventh-dependent): V7/x applied dominants, Ger+6")
    L.append(f"       DCML V7-applied occurrences (cap component 1): {R['dcml_v7_applied']}")
    L.append(f"       DCML Ger+6 occurrences       (cap component 2): {R['dcml_ger6']}")
    L.append(f"    applied OVER-TRIGGER (chain applied, DCML diatonic), stems: {sum(R['over_trigger'].values())}"
             f"  ({len(R['over_trigger'])} stems)")
    L.append("")

    L.append("  #8 WALL-TIME (per-stem, ms):")
    wd, wl = R["wall_decode"], R["wall_legacy"]
    L.append(f"    decode(L1-L4) proxy: median {_pctl(wd,0.5):.1f}  p95 {_pctl(wd,0.95):.1f}  (n={len(wd)})")
    L.append(f"    legacy analyzeScore: median {_pctl(wl,0.5):.1f}  p95 {_pctl(wl,0.95):.1f}")
    L.append("")

    L.append("  #9 CONFIDENCE READOUT (contract §3 terms):")
    c4, c5 = R["l4_composite"], R["l5_combined"]
    if c4:
        L.append(f"    L4 composite [Class M, squashed→[0,1]]: min {min(c4):.3f} median {statistics.median(c4):.3f} max {max(c4):.3f}")
    if c5:
        L.append(f"    L5 combined  [Class M, UNBOUNDED — D-L5a]: min {min(c5):.3f} median {statistics.median(c5):.3f} max {max(c5):.3f}")
    L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fullspine-root", default="tools/corpus",
                    help="dir holding per-preset fullspine subdirs (fullspine_<preset>)")
    ap.add_argument("--legacy-root", default="tools/corpus",
                    help="dir holding the flag-OFF legacy per-preset subdirs (<preset>)")
    ap.add_argument("--presets", nargs="+", default=["baroque", "jazz", "default"])
    ap.add_argument("--wir-base", default=str(C.WIR_BASE_DEFAULT))
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    fsroot, legroot = Path(args.fullspine_root), Path(args.legacy_root)
    for preset in args.presets:
        fs_dir = fsroot / f"fullspine_{preset}"
        leg_dir = legroot / preset
        if not fs_dir.is_dir():
            print(f"[skip] {fs_dir} not found"); continue
        R = measure_preset(preset, fs_dir, leg_dir, Path(args.wir_base))
        print(report(R))


if __name__ == "__main__":
    main()
