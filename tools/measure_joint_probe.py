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

KEY-AXIS DESK-SIM extension (OI-43, mode/key + chord inference discussion, 2026-07-12):
An additive read-only summary answering the desk-simulation's "does the joint chord->key
coupling FIRE?" over the full corpus. Per key-disagree region (argmax region key != DCML
GLOBAL key, the ratified key-agreement target):
  * menu-containment    (PREDICTION 3) — GT global key present in the carried keyAlternatives
  * chord-flip-under-GT  (PREDICTION 1's mechanism) — re-decoding under the carried GT key
                         flips the region root vs the argmax key
  * alt keyConf populated (PREDICTION 2 support) — is a per-alternative key confidence carried?
This is the mechanism-fire check, NOT the key-agreement ceiling/floor grader — the desk-sim
HARD GATE (chord must differ under a carried key) decides whether that grader is worth
building. See cc_mode_key_chord_probe_report.md.

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

# ── The KEY-axis desk-simulation measurement (OI-43, read-only) ──────────────
# Added for the mode/key + chord inference discussion (cowork_mode_key_chord_
# inference_discussion.md). This is the desk-simulation's "does the mechanism FIRE"
# check at full-corpus scale — NOT the key-agreement ceiling/floor grader. The
# desk-sim HARD GATE (the chord must differ under a carried key) decides whether the
# ceiling/floor grader is worth building. Two read-only rates, per key-disagree region
# (argmax region key != DCML GLOBAL key, the ratified key-agreement target):
#   * menu-containment    — the DCML global key present in the carried keyAlternatives
#                           (the PREDICTION-3 quantity; needs no ranking)
#   * chord-flip-under-GT  — re-decoding the chord under the carried GT key flips the
#                           region root vs the argmax key (the joint chord->key coupling
#                           the user's question turns on; PREDICTION-1's mechanism)
#
# KeySigMode enum index -> is_major, derived from keymodeformatting.cpp keyModeSuffix()
# + compare_rn._mode_is_major (major iff suffix prefix in {maj,ion,lyd,mix}). Verified
# faithful per row against crn._our_key_tonic(region key string) — the _selfcheck below.
_MAJOR_MODE_IDX = frozenset({0, 3, 4, 9, 10, 11, 16, 19})
#   0 Ionian, 3 Lydian, 4 Mixolydian, 9 LydianAugmented, 10 LydianDominant,
#   11 MixolydianB6, 16 IonianSharp5, 19 LydianSharp2   (all other modes -> minor)


def _mode_is_major(mode_idx):
    return mode_idx in _MAJOR_MODE_IDX


def _key_ident(tonic_pc, mode_idx):
    """(tonic_pc%12, is_major) for a carried/argmax key from its tonicPc + KeySigMode int."""
    if tonic_pc is None or tonic_pc < 0:
        return None
    return (tonic_pc % 12, _mode_is_major(mode_idx))


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


def _dcml_localkey_by_region(ours_regions, wir_regions):
    """Return, for each of our regions (index-aligned), the DCML LOCAL key (tonic_pc, is_major)
    active at the region's start tick — the key IN EFFECT (tracks tonicization/modulation).
    Same shared tick alignment as _dcml_root_by_region. (OI-143 local-key column.)"""
    if not wir_regions or not ours_regions:
        return [(None, None)] * len(ours_regions)
    dcml_spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    out = []
    for r in ours_regions:
        di = crn._active_index_at(dcml_spans, r.start_tick)
        out.append(crn._dcml_key_tonic(wir_regions[di].local_key) if di is not None else (None, None))
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

    try:
        # THE shared WiR loading substrate (applies the OI-142 transposition correction).
        wir_regions = dcml.load_wir_regions(str(WIR_DIR), stem)
    except Exception:
        wir_regions = []
    if not wir_regions:
        return (stem, None, "NO_WIR")

    dcml_roots = _dcml_root_by_region(ours_regions, wir_regions)
    dcml_localkeys = _dcml_localkey_by_region(ours_regions, wir_regions)  # OI-143
    probe_regions = raw.get("regions", [])
    # The DCML GLOBAL key (constant per piece; the ratified key-agreement target — a8
    # grades our region key vs dcml_r.global_key). Parsed once with the ratified substrate.
    gt_key = crn._dcml_key_tonic(wir_regions[0].global_key) if wir_regions else (None, None)
    rows = []
    for reg, dcml_root, l_key in zip(probe_regions, dcml_roots, dcml_localkeys):
        p = reg.get("probe", {})
        ak = p.get("argmaxKey", {})
        rows.append({
            "stem": stem,
            "startTick": reg.get("startTick"),
            "dur": (reg.get("endTick", 0) - reg.get("startTick", 0)),
            "dcmlRoot": dcml_root,
            "argmaxRoot": p.get("argmaxRoot", -1),
            "keySeqMargin": p.get("keySeqMargin", 0.0),
            "alts": p.get("alternatives", []),        # [{fifths,mode,tonicPc,keyConf,root}]
            "isPedalPoint": bool(p.get("isPedalPoint", False)),
            "prodRoot": p.get("prodRoot", -1),
            "bassPc": p.get("bassPc", -1),
            "carryRoots": p.get("argmaxCarryRoots", []),
            # ── KEY-axis desk-sim fields (OI-43) ──
            "argmaxKeyIdent": _key_ident(ak.get("tonicPc"), ak.get("mode")),
            "gtGlobalKey": (gt_key if gt_key[0] is not None else None),
            "gtLocalKey": (l_key if l_key[0] is not None else None),   # OI-143 local-key column
            "ourKeyStr": reg.get("key"),              # for the enum-table self-check
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
    # ── KEY-axis desk-sim (OI-43); region-level over committed regions ──
    ka_keyagree = 0; ka_keyagree_dur = 0        # region key == DCML global key
    ka_keydis = 0;   ka_keydis_dur = 0          # region key != DCML global key
    ka_keyfail = 0                              # argmax/GT key unparseable
    # OI-143 — the LOCAL-key column beside the home column (region key vs DCML LOCAL key)
    ka_keyagree_local = 0; ka_keyagree_local_dur = 0
    ka_keydis_local = 0;   ka_keydis_local_dur = 0
    ka_keyfail_local = 0
    ka_menu = 0;     ka_menu_dur = 0            # key-disagree AND GT key in carried menu
    ka_flip_gt = 0;  ka_flip_gt_dur = 0         # key-disagree AND chord flips under carried GT key
    ka_flip_gt_coupled = 0                      #   + key-uncertain (keySeqMargin < bar)
    ka_flip_any = 0                             # key-disagree AND chord flips under ANY carried key
    ka_alt_total = 0                            # carried alternatives seen (committed regions)
    ka_alt_keyconf_nonzero = 0                  # carried alts with a populated (>0) keyConf
    ka_selfcheck_total = 0; ka_selfcheck_mismatch = 0   # enum-table vs key-string faithfulness

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

        # ── KEY-axis desk-sim (OI-43): region-level menu-containment + chord-flip-under-GT ──
        # NOTE: region-level counts over COMMITTED regions — NOT the robust-unit
        # key-agreement (union-of-boundaries cells) that produces the ratified column.
        ak_ident = r.get("argmaxKeyIdent")
        gt = r.get("gtGlobalKey")
        gt_local = r.get("gtLocalKey")            # OI-143
        dur = r.get("dur", 0)
        # OI-143 — region key vs the DCML LOCAL key (the key in effect), beside the home column
        if ak_ident is None or gt_local is None or gt_local[0] is None:
            ka_keyfail_local += 1
        elif ak_ident == (gt_local[0] % 12, gt_local[1]):
            ka_keyagree_local += 1
            ka_keyagree_local_dur += dur
        else:
            ka_keydis_local += 1
            ka_keydis_local_dur += dur
        # enum-table faithfulness self-check: is_major from tonicPc+mode must equal
        # crn._our_key_tonic(region key string) — proves the alt grading is faithful.
        if ak_ident is not None and r.get("ourKeyStr"):
            sc = crn._our_key_tonic(r["ourKeyStr"])
            if sc[0] is not None:
                ka_selfcheck_total += 1
                if (sc[0] % 12, sc[1]) != ak_ident:
                    ka_selfcheck_mismatch += 1
        for a in alts:
            ka_alt_total += 1
            kc = a.get("keyConf", 0.0)
            if kc is not None and kc > 0.0:
                ka_alt_keyconf_nonzero += 1
        if ak_ident is None or gt is None or gt[0] is None:
            ka_keyfail += 1
        elif ak_ident == (gt[0] % 12, gt[1]):
            ka_keyagree += 1
            ka_keyagree_dur += dur
        else:
            ka_keydis += 1
            ka_keydis_dur += dur
            gt_in_menu = False
            gt_flip = False
            any_flip = False
            for a in alts:
                a_ident = _key_ident(a.get("tonicPc"), a.get("mode"))
                rt = a.get("root", -1)
                if rt is not None and rt >= 0 and am >= 0 and rt != am:
                    any_flip = True
                if a_ident is not None and a_ident == (gt[0] % 12, gt[1]):
                    gt_in_menu = True
                    if rt is not None and rt >= 0 and am >= 0 and rt != am:
                        gt_flip = True
            if gt_in_menu:
                ka_menu += 1
                ka_menu_dur += dur
            if gt_flip:
                ka_flip_gt += 1
                ka_flip_gt_dur += dur
                if r["keySeqMargin"] < KEY_UNCERTAIN_BAR:
                    ka_flip_gt_coupled += 1
            if any_flip:
                ka_flip_any += 1

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
        # ── KEY-axis desk-sim (OI-43): does the joint chord->key coupling FIRE? ──
        # Region-level over committed regions; NOT the robust-unit key-agreement column.
        "key_axis_desksim": {
            "n_key_agree_regions": ka_keyagree,
            "n_key_disagree_regions": ka_keydis,
            "n_key_unparseable_regions": ka_keyfail,
            "key_agree_dur": ka_keyagree_dur,
            "key_disagree_dur": ka_keydis_dur,
            # OI-143 — the LOCAL-key column beside the home column (region key vs DCML LOCAL key)
            "vs_local_key": {
                "n_key_agree_regions": ka_keyagree_local,
                "n_key_disagree_regions": ka_keydis_local,
                "n_key_unparseable_regions": ka_keyfail_local,
                "key_agree_dur": ka_keyagree_local_dur,
                "key_disagree_dur": ka_keydis_local_dur,
            },
            # PREDICTION 3 — menu-containment (GT global key present in carried menu)
            "menu_containment": {
                "n": ka_menu,
                "frac_of_keydisagree": round(ka_menu / ka_keydis, 4) if ka_keydis else None,
                "frac_of_keydisagree_dur": round(ka_menu_dur / ka_keydis_dur, 4) if ka_keydis_dur else None,
            },
            # PREDICTION 1 — the coupling mechanism: chord flips under the carried GT key
            "chord_flip_under_gt": {
                "n": ka_flip_gt,
                "frac_of_keydisagree": round(ka_flip_gt / ka_keydis, 4) if ka_keydis else None,
                "n_coupled": ka_flip_gt_coupled,
                "dur": ka_flip_gt_dur,
            },
            "chord_flip_under_any_carried": {
                "n": ka_flip_any,
                "frac_of_keydisagree": round(ka_flip_any / ka_keydis, 4) if ka_keydis else None,
            },
            # PREDICTION 2 support — the per-alternative key confidence populated?
            "alt_keyconf_populated": {
                "n_alts": ka_alt_total,
                "n_nonzero": ka_alt_keyconf_nonzero,
                "frac_nonzero": round(ka_alt_keyconf_nonzero / ka_alt_total, 4) if ka_alt_total else None,
            },
            "enum_table_selfcheck": {
                "n_checked": ka_selfcheck_total,
                "n_mismatch": ka_selfcheck_mismatch,
            },
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
            ka = summ["key_axis_desksim"]
            mc = ka["menu_containment"]; cf = ka["chord_flip_under_gt"]
            sc = ka["enum_table_selfcheck"]; kc = ka["alt_keyconf_populated"]
            kl = ka["vs_local_key"]
            print(f"  ★ KEY-AXIS desk-sim (OI-43): key-disagree regions vs HOME={ka['n_key_disagree_regions']} "
                  f"(dur {ka['key_disagree_dur']}); keyfail={ka['n_key_unparseable_regions']}")
            print(f"     OI-143 vs LOCAL key: agree={kl['n_key_agree_regions']} "
                  f"disagree={kl['n_key_disagree_regions']} (dur {kl['key_disagree_dur']}); "
                  f"keyfail={kl['n_key_unparseable_regions']}")
            print(f"     PRED-3 menu-containment (GT key in menu): {mc['n']} "
                  f"({mc['frac_of_keydisagree']} by count, {mc['frac_of_keydisagree_dur']} by dur)")
            print(f"     PRED-1 chord-flip-under-GT (coupling fires): {cf['n']} "
                  f"({cf['frac_of_keydisagree']}); coupled={cf['n_coupled']}; any-carried-flip={ka['chord_flip_under_any_carried']['n']}")
            print(f"     PRED-2 alt keyConf populated: {kc['n_nonzero']}/{kc['n_alts']} ({kc['frac_nonzero']}); "
                  f"enum-table selfcheck mismatch={sc['n_mismatch']}/{sc['n_checked']}")
            if failed:
                print(f"  FAILED {len(failed)}: {failed[:5]}")

    out = args.out or str(_REPO_ROOT / "tools" / "reports" / "joint_probe_measure.json")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nReport → {out}")


if __name__ == "__main__":
    main()
