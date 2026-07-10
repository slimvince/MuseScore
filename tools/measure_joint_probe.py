#!/usr/bin/env python3
"""measure_joint_probe.py — Engage arc #12 read-only measurement.

Runs batch_analyze --dump-joint-probe over the pinned Bach corpus (tools/corpus/*.xml)
for each of the three presets and answers the DECISIVE joint-step question
(cowork_joint_key_chord_design.md §5): does re-deciding the chord under an alternative
CARRIED key measurably improve root-correctness, or not?

--dump-joint-probe exercises the EXISTING ChordSliceDecoder as a PURE re-decode function
under L3's already-carried per-region key alternatives (keyModeResult ∪ keyAlternatives).
It returns before the standard writeJson, so the standard .ours.json corpus is untouched;
this script writes only throwaway *.joint.json side files into a scratch dir. Read-only,
no behavior change, no re-baseline, no fit.

The benefit is measured the SAME way the robust stop is (#1): root-agreement vs the DCML
(When-in-Rome) ground truth, aligned to our region ticks by the SHARED compare_analyses /
compare_rn / dcml_parser substrate the a8 driver reuses — no proxy, no new tick matcher.

Reports, per preset:
  * fire-rate       [owed-1] — fraction of regions where the chord root FLIPS under some
                    carried alternative key (overall + on the key-uncertain coupled minority)
  * ★ the benefit   [owed-2/3 go/no-go] — on the flipped regions, corr / harm / neutral vs
                    DCML, in the net-(corr−harm) framing that exposed the F-B override
  * beam width      [owed-4] — the distribution of carried-key-alternative counts per region
  * pedal owed-P1   — whether the decoder carry under the argmax key already holds the
                    production in-place pedal (upper-voice) root

Reuses run_bach_preset's Git-Bash invocation helpers (no duplication, #6).
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import multiprocessing
import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))

import run_bach_preset as rbp          # noqa: E402
import compare_analyses as cmp         # noqa: E402
import compare_rn as crn               # noqa: E402
import dcml_parser as dcml             # noqa: E402

_REPO_ROOT = Path(__file__).resolve().parent.parent
WIR_DIR = _REPO_ROOT / "tools" / "dcml" / "when_in_rome"
PRESETS = ["Baroque", "Jazz", "Default"]

# The coupled-minority bar (a): the D-L3a sequence-margin abstention threshold
# (keymodesequence.h uncertainThreshold, default 1.0). CLAUDE.md-verified at source;
# NOT fitted here (R5). Reported both overall and on keySeqMargin < this bar.
KEY_UNCERTAIN_BAR = 1.0


def _dcml_root_by_region(ours_regions, wir_regions):
    """Return, for each of our regions (index-aligned), the DCML root_pc active at the
    region's start tick — via the SHARED tick alignment (compare_analyses._dcml_time_spans
    + compare_rn._active_index_at), the same substrate the a8 robust-stop driver reuses."""
    if not wir_regions or not ours_regions:
        return [None] * len(ours_regions)
    dcml_spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    out = []
    for r in ours_regions:
        di = crn._active_index_at(dcml_spans, r.start_tick)
        out.append(wir_regions[di].root_pc if di is not None else None)
    return out


def _collect_one(args_tuple):
    exe, xml_path, preset, scratch = args_tuple
    stem = xml_path.stem
    out_path = Path(scratch) / f"{preset}_{stem}.joint.json"
    ok = rbp._run_batch_analyze(exe, xml_path, out_path, preset,
                                diag_fh=None, extra_args="--dump-joint-probe")
    if not ok or not out_path.exists():
        return (stem, None, "FAILED")
    try:
        _, ours_regions = cmp.load_analysis(out_path)
        raw = json.loads(out_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return (stem, None, f"PARSE_ERR:{exc}")
    finally:
        try:
            out_path.unlink()
        except OSError:
            pass

    wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
    if not wir_path:
        return (stem, None, "NO_WIR")
    try:
        wir_regions = dcml.parse_rntxt_file(wir_path)
    except Exception:
        wir_regions = []
    if not wir_regions:
        return (stem, None, "NO_WIR")

    dcml_roots = _dcml_root_by_region(ours_regions, wir_regions)
    probe_regions = raw.get("regions", [])
    rows = []
    for reg, dcml_root in zip(probe_regions, dcml_roots):
        p = reg.get("probe", {})
        rows.append({
            "stem": stem,
            "startTick": reg.get("startTick"),
            "dcmlRoot": dcml_root,
            "argmaxRoot": p.get("argmaxRoot", -1),
            "keySeqMargin": p.get("keySeqMargin", 0.0),
            "alts": p.get("alternatives", []),        # [{fifths,mode,tonicPc,keyConf,root}]
            "isPedalPoint": bool(p.get("isPedalPoint", False)),
            "prodRoot": p.get("prodRoot", -1),
            "bassPc": p.get("bassPc", -1),
            "carryRoots": p.get("argmaxCarryRoots", []),
        })
    return (stem, rows, "OK")


def _classify_flip(argmax_root, alt_root, dcml_root):
    """A root-changing flip (argmax != alt, both defined) vs the DCML root:
       corr = alt agrees, argmax did not; harm = argmax agreed, alt does not;
       neutral = neither agrees (a root move that changes nothing correctness-wise)."""
    a_ok = (argmax_root == dcml_root)
    x_ok = (alt_root == dcml_root)
    if x_ok and not a_ok:
        return "corr"
    if a_ok and not x_ok:
        return "harm"
    return "neutral"


def _summarize(all_rows):
    n_regions = len(all_rows)
    n_committed = 0            # regions with an argmax-key committed decode (argmaxRoot >= 0)
    n_with_alts = 0
    beam_hist = Counter()      # carried-key count = 1 (argmax) + len(alts)
    # fire-rate
    n_flip = 0                 # >=1 carried alt with a DIFFERENT committed root
    n_flip_coupled = 0
    n_coupled = 0
    # benefit — per-region TOP-alternative flip (the key the beam most likely surfaces:
    # the highest-keyConf carried alt that flips), scored only where the DCML root is known
    top_flip = Counter()       # corr/harm/neutral over regions whose top flipping alt is defined
    top_flip_coupled = Counter()
    # benefit — per-flip (region,alt) pairs (the raw flip surface)
    pair_flip = Counter()
    # benefit — optimistic ANY-alt bound + harm exposure (over DCML-known regions)
    n_scored = 0               # argmaxRoot>=0 and dcmlRoot is not None
    corr_available = 0         # argmax wrong, SOME carried alt flips to the DCML root
    harm_exposed = 0           # argmax right, SOME carried alt flips AWAY from the DCML root
    # pedal owed-P1
    n_pedal = 0
    n_pedal_carry_agree = 0

    for r in all_rows:
        am = r["argmaxRoot"]
        alts = r["alts"]
        beam = 1 + len(alts)
        beam_hist[beam if beam <= 6 else ">6"] += 1
        if alts:
            n_with_alts += 1
        coupled = (r["keySeqMargin"] < KEY_UNCERTAIN_BAR)
        if coupled:
            n_coupled += 1
        if am is None or am < 0:
            continue
        n_committed += 1

        # flips = carried alts with a defined, DIFFERENT root
        flips = [a for a in alts if a.get("root", -1) >= 0 and a["root"] != am]
        if flips:
            n_flip += 1
            if coupled:
                n_flip_coupled += 1

        dcml_root = r["dcmlRoot"]
        if dcml_root is not None:
            n_scored += 1
            # per-flip pairs
            for a in flips:
                pair_flip[_classify_flip(am, a["root"], dcml_root)] += 1
            # optimistic bound / harm exposure
            if flips:
                any_to_dcml = any(a["root"] == dcml_root for a in flips)
                any_away = any(a["root"] != dcml_root for a in flips)
                if am != dcml_root and any_to_dcml:
                    corr_available += 1
                if am == dcml_root and any_away:
                    harm_exposed += 1
                # top-keyConf flipping alt
                top = max(flips, key=lambda a: a.get("keyConf", 0.0))
                v = _classify_flip(am, top["root"], dcml_root)
                top_flip[v] += 1
                if coupled:
                    top_flip_coupled[v] += 1

        # pedal owed-P1: production flagged a pedal (upper-voice chord is prodRoot != bass);
        # does the decoder carry under the argmax key already hold that upper-voice root?
        if r["isPedalPoint"]:
            n_pedal += 1
            pr = r["prodRoot"]
            bass = r["bassPc"]
            carry = set(x for x in r["carryRoots"] if x is not None and x >= 0)
            if pr is not None and pr >= 0 and pr != bass and pr in carry:
                n_pedal_carry_agree += 1

    def _net(c):
        return c.get("corr", 0) - c.get("harm", 0)

    return {
        "n_regions": n_regions,
        "n_committed": n_committed,
        "n_regions_with_carried_alts": n_with_alts,
        "beam_width_carried_keys": dict(beam_hist),
        "fire_rate": {
            "n_flip_regions": n_flip,
            "frac_of_committed": round(n_flip / n_committed, 4) if n_committed else 0.0,
            "n_coupled_regions": n_coupled,
            "n_flip_coupled": n_flip_coupled,
            "frac_of_coupled": round(n_flip_coupled / n_coupled, 4) if n_coupled else 0.0,
        },
        "benefit_top_alt_flip": {
            **dict(top_flip),
            "net_corr_minus_harm": _net(top_flip),
            "n": sum(top_flip.values()),
        },
        "benefit_top_alt_flip_coupled": {
            **dict(top_flip_coupled),
            "net_corr_minus_harm": _net(top_flip_coupled),
            "n": sum(top_flip_coupled.values()),
        },
        "benefit_per_flip_pairs": {
            **dict(pair_flip),
            "net_corr_minus_harm": _net(pair_flip),
            "n": sum(pair_flip.values()),
        },
        "benefit_any_alt_bound": {
            "n_scored_regions": n_scored,
            "corrections_available": corr_available,
            "harms_exposed": harm_exposed,
            "net_available": corr_available - harm_exposed,
        },
        "pedal_owed_p1": {
            "n_production_pedal_regions": n_pedal,
            "n_carry_already_holds_pedal_root": n_pedal_carry_agree,
            "agreement_frac": round(n_pedal_carry_agree / n_pedal, 4) if n_pedal else None,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-analyze", metavar="PATH")
    ap.add_argument("--corpus-dir", default="tools/corpus")
    ap.add_argument("--out", metavar="FILE", help="write the JSON report here")
    args = ap.parse_args()

    exe = rbp._find_batch_analyze(args.batch_analyze)
    if exe is None:
        print("ERROR: batch_analyze not found", file=sys.stderr)
        sys.exit(1)
    print(f"Using batch_analyze: {exe}")

    corpus_dir = Path(args.corpus_dir)
    xml_files = sorted(f for f in corpus_dir.glob("*.xml") if not f.stem.endswith("_m21"))
    if not xml_files:
        print(f"ERROR: no .xml in {corpus_dir}", file=sys.stderr)
        sys.exit(1)
    print(f"Corpus: {len(xml_files)} scores × {len(PRESETS)} presets")

    report = {
        "git_hash": rbp._get_git_hash(),
        "corpus_git_hash": None,
        "key_uncertain_bar": KEY_UNCERTAIN_BAR,
        "n_scores": len(xml_files),
        "presets": {},
    }
    mp = corpus_dir / "baroque" / "corpus_manifest.json"
    if mp.exists():
        report["corpus_git_hash"] = json.loads(mp.read_text())["git_hash"]

    workers = min(multiprocessing.cpu_count(), len(xml_files))
    with tempfile.TemporaryDirectory() as scratch:
        for preset in PRESETS:
            print(f"\n=== preset {preset} ===")
            work = [(exe, xml, preset, scratch) for xml in xml_files]
            all_rows = []
            failed = []
            no_wir = 0
            done = 0
            with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
                futs = {pool.submit(_collect_one, w): w[1].stem for w in work}
                for fut in concurrent.futures.as_completed(futs):
                    stem, rows, status = fut.result()
                    done += 1
                    if status == "OK":
                        all_rows.extend(rows)
                    elif status == "NO_WIR":
                        no_wir += 1
                    else:
                        failed.append((stem, status))
                    if done % 50 == 0:
                        print(f"  {done}/{len(work)} ...")
            summ = _summarize(all_rows)
            summ["scores_no_wir"] = no_wir
            summ["scores_failed"] = failed
            report["presets"][preset] = summ

            fr = summ["fire_rate"]
            bt = summ["benefit_top_alt_flip"]
            ba = summ["benefit_any_alt_bound"]
            pp = summ["pedal_owed_p1"]
            print(f"  regions={summ['n_regions']} committed={summ['n_committed']} "
                  f"no_wir_scores={no_wir}")
            print(f"  FIRE-RATE: flips={fr['n_flip_regions']} "
                  f"({fr['frac_of_committed']:.1%} of committed); "
                  f"coupled flips={fr['n_flip_coupled']} ({fr['frac_of_coupled']:.1%} of coupled)")
            print(f"  ★ BENEFIT (top-alt flip): corr={bt.get('corr',0)} harm={bt.get('harm',0)} "
                  f"neutral={bt.get('neutral',0)}  NET={bt['net_corr_minus_harm']}  (n={bt['n']})")
            print(f"  BENEFIT (any-alt bound over {ba['n_scored_regions']} DCML-scored): "
                  f"corrections_available={ba['corrections_available']} "
                  f"harms_exposed={ba['harms_exposed']} net={ba['net_available']}")
            print(f"  PEDAL owed-P1: pedal_regions={pp['n_production_pedal_regions']} "
                  f"carry_holds_root={pp['n_carry_already_holds_pedal_root']} "
                  f"agree={pp['agreement_frac']}")
            if failed:
                print(f"  FAILED {len(failed)}: {failed[:5]}")

    out = args.out or str(_REPO_ROOT / "tools" / "reports" / "joint_probe_measure.json")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nReport → {out}")


if __name__ == "__main__":
    main()
