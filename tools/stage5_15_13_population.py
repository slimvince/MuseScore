#!/usr/bin/env python3
"""stage5_15_13_population.py — the §15-13 both-licensed fall-through population count.

Stage-5 fitter design §4.4 family 4 (the commissioned L5 preference-among-licensed
weight) is GATED on this measurement: count the both-licensed fall-through population on
the reference corpus (decode-only). If the population is too small for an evidence-based
fit, the item returns to the user with the number and stays a recorded §15-13 open item.

DECODE-ONLY, READ-ONLY. This reads the DEFAULT-OFF --dump-fullspine measurement dumps
(runFullSpine in tools/batch_analyze.cpp), which run the DORMANT L5 resolver over the
frozen corpus. It reads the additive `l5BothLicensed` field (functionresolver.cpp sets it
at the §5.5 Transition/ShareTone licensing arms when aIn && bIn) plus the pre-existing
per-region fields (ambiguityKind / l5Resolved / l5OpenMark / l5Basis / duration). No GT is
needed — this is a population census of the resolver's own decisions, not an accuracy run.

The both-licensed OUTCOME (design §5.5): a both-licensed case falls to the structural
tie-breaks (Transition's NeighbourHarmony arm, then the §5.7 BassDegreePrior) or, where
those do not separate it, to the honest open mark. So per case:
  - TIE-BREAK  == l5Resolved && !l5OpenMark  (basis NeighbourHarmony or BassDegreePrior)
  - OPEN MARK  == l5OpenMark                 (basis None)

Usage:
  python tools/stage5_15_13_population.py --fs-root C:/tmp/s5_scratch --presets baroque jazz default
    expects  {fs-root}/fullspine_{preset}/{stem}.ours.json
"""
import argparse
import json
import statistics
import sys
from collections import Counter
from pathlib import Path


def measure(fs_dir: Path):
    files = sorted(fs_dir.glob("*.ours.json"))
    covered = 0
    tot_slices = tot_abstain = tot_openmark = tot_committed = 0
    tot_regions = 0
    bl_total = 0
    bl_by_ambig = Counter()          # ambiguityKind -> count of both-licensed
    bl_by_basis = Counter()          # l5Basis -> count of both-licensed (the outcome)
    bl_tiebreak = 0                  # both-licensed resolved by a structural tie-break
    bl_openmark = 0                  # both-licensed fell to the honest open mark
    bl_dur = 0.0                     # duration of both-licensed regions
    all_dur = 0.0                    # duration of ALL regions
    abstain_dur = 0.0                # duration of L4-abstain regions (context denominator)
    per_score = []                   # both-licensed count per score
    # a fall-through census for context: any Transition/ShareTone slice reaching a
    # structural tie-break / open mark (basis not Progression), split both-lic vs not.
    ft_transition_sharetone = 0      # Transition/ShareTone slices NOT resolved by Progression
    ft_bl = 0                        # of those, both-licensed
    examples = []                    # (stem, tick, ambig, basis, openmark, dur)

    for p in files:
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        stem = p.name.replace(".ours.json", "")
        covered += 1
        tot_slices += int(data.get("slicesTotal", 0))
        tot_committed += int(data.get("committedUnits", 0))
        tot_abstain += int(data.get("abstainUnits", 0))
        tot_openmark += int(data.get("openMarkUnits", 0))
        score_bl = 0
        for r in data.get("regions", []):
            tot_regions += 1
            dur = float(r.get("duration", 0.0))
            all_dur += dur
            ambig = r.get("ambiguityKind", "None")
            basis = r.get("l5Basis", "None")
            resolved = bool(r.get("l5Resolved", False))
            openmark = bool(r.get("l5OpenMark", r.get("openMark", False)))
            l4dec = r.get("l4Decision", "Commit")
            if l4dec == "Abstain":
                abstain_dur += dur
            if ambig in ("TransitionVsContinuation", "ShareTone") and basis != "Progression":
                ft_transition_sharetone += 1
            if r.get("l5BothLicensed", False):
                bl_total += 1
                score_bl += 1
                bl_by_ambig[ambig] += 1
                bl_by_basis[basis] += 1
                bl_dur += dur
                ft_bl += 1
                if openmark:
                    bl_openmark += 1
                else:
                    bl_tiebreak += 1
                if len(examples) < 60:
                    examples.append((stem, int(r.get("startTick", -1)), ambig, basis,
                                     openmark, round(dur, 3)))
        per_score.append(score_bl)
    return dict(
        covered=covered, tot_slices=tot_slices, tot_committed=tot_committed,
        tot_abstain=tot_abstain, tot_openmark=tot_openmark, tot_regions=tot_regions,
        bl_total=bl_total, bl_by_ambig=bl_by_ambig, bl_by_basis=bl_by_basis,
        bl_tiebreak=bl_tiebreak, bl_openmark=bl_openmark,
        bl_dur=bl_dur, all_dur=all_dur, abstain_dur=abstain_dur,
        per_score=per_score, ft_transition_sharetone=ft_transition_sharetone, ft_bl=ft_bl,
        examples=examples,
    )


def report(preset, R):
    L = []
    L.append("=" * 78)
    L.append(f"PRESET {preset.upper()}  ({R['covered']} fullspine dumps)")
    L.append("=" * 78)
    ps = R["per_score"]
    nz = [x for x in ps if x > 0]
    L.append(f"  DENOMINATORS:")
    L.append(f"    slices total .......... {R['tot_slices']}")
    L.append(f"    committed units ....... {R['tot_committed']}")
    L.append(f"    L4-abstain units ...... {R['tot_abstain']}   (the resolveAbstained population)")
    L.append(f"    final open marks ...... {R['tot_openmark']}")
    L.append(f"    emitted regions ....... {R['tot_regions']}")
    L.append(f"    Transition/ShareTone fall-throughs (basis != Progression): {R['ft_transition_sharetone']}")
    L.append("")
    L.append(f"  ★ §15-13 BOTH-LICENSED FALL-THROUGH POPULATION: {R['bl_total']}")
    L.append(f"    by ambiguity kind : " + (", ".join(f"{k}:{v}" for k, v in R['bl_by_ambig'].most_common()) or "—"))
    L.append(f"    OUTCOME breakdown : tie-break {R['bl_tiebreak']}  |  open mark {R['bl_openmark']}")
    L.append(f"    by resolution basis: " + (", ".join(f"{k}:{v}" for k, v in R['bl_by_basis'].most_common()) or "—"))
    ad = R["all_dur"]
    L.append(f"    duration share    : {R['bl_dur']:.1f} / {ad:.1f} q = "
             f"{(100.0*R['bl_dur']/ad if ad else 0.0):.3f}% of scored duration"
             f"  ({(100.0*R['bl_dur']/R['abstain_dur'] if R['abstain_dur'] else 0.0):.2f}% of abstain duration)")
    L.append(f"    per-score distrib : scores with >=1 = {len(nz)}/{len(ps)};  "
             f"max/score = {max(ps) if ps else 0};  "
             f"median (over nonzero) = {statistics.median(nz) if nz else 0}")
    if R["examples"]:
        L.append(f"    examples (up to 60): ")
        for e in R["examples"]:
            L.append(f"      {e[0]}@{e[1]}  {e[2]:<24} basis={e[3]:<16} "
                     f"{'OPEN' if e[4] else 'tie-break'}  dur={e[5]}")
    L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fs-root", default="C:/tmp/s5_scratch",
                    help="dir holding fullspine_{preset}/ subdirs of {stem}.ours.json dumps")
    ap.add_argument("--presets", nargs="+", default=["baroque", "jazz", "default"])
    ap.add_argument("--json-out", default=None, help="optional path to write the compact per-preset totals")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    root = Path(args.fs_root)
    compact = {}
    for preset in args.presets:
        fs_dir = root / f"fullspine_{preset}"
        if not fs_dir.is_dir():
            print(f"[skip] {fs_dir} not found")
            continue
        R = measure(fs_dir)
        print(report(preset, R))
        compact[preset] = {
            "covered": R["covered"], "slices": R["tot_slices"],
            "abstain_units": R["tot_abstain"], "open_marks": R["tot_openmark"],
            "both_licensed": R["bl_total"], "tie_break": R["bl_tiebreak"],
            "open_mark": R["bl_openmark"],
            "by_ambig": dict(R["bl_by_ambig"]), "by_basis": dict(R["bl_by_basis"]),
            "dur_share_pct": round(100.0 * R["bl_dur"] / R["all_dur"], 4) if R["all_dur"] else 0.0,
            "scores_with_ge1": sum(1 for x in R["per_score"] if x > 0),
            "max_per_score": max(R["per_score"]) if R["per_score"] else 0,
        }
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(compact, indent=1, sort_keys=True), encoding="utf-8")
        print(f"compact totals -> {args.json_out}")


if __name__ == "__main__":
    main()
