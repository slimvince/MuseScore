#!/usr/bin/env python3
"""
compare_progressions_oracle.py — the progression-recognition consumer's §7 dev-bed
validation (cowork_progression_schema_design.md §7).

READ-ONLY. Grades the DORMANT recognition consumer's --dump-progressions output over
the DCML dev beds against the `cadence` GT column. Nothing here moves a constant; the
consumer is dormant, so production is byte-identical. Descriptive only — a validation
bed, not a gate.

Measurements (per corpus + aggregate):
  1. Recognition census — positions, admitted schema-spans, span-name histogram,
     harmonic-sequence count, §4.3 abstained-feature / committed-override counts,
     and COVERAGE (fraction of committed positions under >=1 admitted recognition).
     This SIZES the exact-match v1 under-recognition (design §8).
  2. Cadence-span precision/recall — OUR recognised CADENCE schema-spans (Authentic /
     Plagal / Deceptive / Phrygian-half), whose arrival ~ the span endTick, vs the GT
     `cadence` rows, LOCATION-scoped, +/- one quarter-note beat (480t). Reuses the same
     tolerance basis as compare_l6_oracle.py; NOT tuned.
  3. Empirically-unvalidated mark — recognitions carrying a jazz/pop-family idiom
     (SeventhFunctional / TriadicModal / ChromaticColoristic without a common-practice
     idiom) are flagged: there is no score-aligned jazz/pop GT on these beds (design
     §7 / dictionary §8 — the census Tier-J want).

The evidence contribution measured as RN-accuracy CHANGE on covered positions (design
§7) is NOT produced here: the §5.5 feature / §8 override are DORMANT (not wired into
Layer 5), so an end-to-end RN-accuracy delta cannot be measured without engagement.
Coverage (#1) is the honest proxy — the surface on which that contribution would act.
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT / "tools"))
from dcml_parser import parse_cadence_phrase_markers, TICKS_PER_QUARTER  # noqa: E402

_DCML = _REPO_ROOT / "tools" / "dcml"
_OUT_ROOT = _REPO_ROOT / "tools" / "corpus_progressions_oracle"
TOLERANCE_TICKS = TICKS_PER_QUARTER   # +/- one beat, declared (not tuned)

# The dev beds (registry split=dev) — the same set compare_l6_oracle.py grades.
DEV_BEDS = [
    "ABC", "bach_en_fr_suites", "chopin_mazurkas", "corelli", "cpe_bach_keyboard",
    "dvorak_silhouettes", "grieg_lyric_pieces", "mozart_piano_sonatas",
    "schumann_kinderszenen", "tchaikovsky_seasons",
    "beethoven_piano_sonatas", "wagner_overtures", "liszt_pelerinage",
    "rachmaninoff_piano", "schulhoff_suite_dansante_en_jazz", "monteverdi_madrigals",
]

# The idiom bits (harmonicvocabulary.h enum Idiom): the recognition consumer's weights.
IDIOM_NAMES = ["Diatonic-fn", "Chromatic-fn", "Seventh-fn", "Triadic-modal", "Chromatic-col"]
# A recognition is "jazz/pop-family" (no score-aligned GT) when it carries a jazz/pop
# idiom (Seventh-fn=4 / Triadic-modal=8 / Chromatic-col=16) and NO common-practice
# idiom (Diatonic-fn=1 / Chromatic-fn=2).
_CP_IDIOMS = 1 | 2
_JP_IDIOMS = 4 | 8 | 16

# Our cadence schema-span names (the L5 §5.2 cadences the catalog also carries).
_CADENCE_PREFIXES = ("Authentic cadence", "Plagal cadence", "Deceptive cadence",
                     "Phrygian half cadence")


def _is_cadence_span(name: str) -> bool:
    return any(name.startswith(p) for p in _CADENCE_PREFIXES)


def _find_exe():
    for p in (_REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
              _REPO_ROOT / "ninja_build_rel" / "batch_analyze"):
        if p.exists():
            return p
    return None


def _find_bash():
    for p in (Path("C:/Program Files/Git/usr/bin/bash.exe"),
              Path("C:/Program Files (x86)/Git/usr/bin/bash.exe")):
        if p.exists():
            return p
    return None


def _to_unix(p: Path) -> str:
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ":":
        s = "/" + s[0].lower() + s[2:]
    return s.replace("\\", "/")


def _run_dump(exe, mscx, out, bash, timeout=180) -> bool:
    env = dict(os.environ)
    env.setdefault("QT_QPA_PLATFORM", "offscreen")
    try:
        if platform.system() == "Windows" and bash:
            cmd = f'{_to_unix(exe)} "{_to_unix(mscx)}" --dump-progressions > "{_to_unix(out)}"'
            r = subprocess.run([str(bash), "-c", cmd], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=timeout, env=env)
        else:
            with open(out, "wb") as fh:
                r = subprocess.run([str(exe), str(mscx), "--dump-progressions"],
                                   stdout=fh, stderr=subprocess.DEVNULL, timeout=timeout, env=env)
        return r.returncode == 0 and out.exists() and out.stat().st_size > 0
    except Exception:
        return False


def _corpus_pieces(corpus: str):
    ms3, harm = _DCML / corpus / "MS3", _DCML / corpus / "harmonies"
    if not ms3.is_dir() or not harm.is_dir():
        return []
    out = []
    for mscx in sorted(ms3.glob("*.mscx")):
        tsv = harm / f"{mscx.stem}.harmonies.tsv"
        if tsv.exists():
            out.append((mscx, tsv))
    return out


def _match_points(ours: list, gt: list) -> int:
    """Greedy nearest 1-1 match within TOLERANCE_TICKS. Returns #matched."""
    ours = sorted(ours)
    gt = sorted(gt)
    used = [False] * len(gt)
    matched = 0
    for t in ours:
        best, bestd = -1, TOLERANCE_TICKS + 1
        for j, g in enumerate(gt):
            if used[j]:
                continue
            d = abs(t - g)
            if d <= TOLERANCE_TICKS and d < bestd:
                best, bestd = j, d
        if best >= 0:
            used[best] = True
            matched += 1
    return matched


def _grade_corpus(corpus, exe, bash, limit):
    cdir = _OUT_ROOT / corpus
    cdir.mkdir(parents=True, exist_ok=True)
    pieces = _corpus_pieces(corpus)
    if limit:
        pieces = pieces[:limit]

    agg = dict(movements=0, positions=0, spans=0, seqs=0, abstained=0, overrides=0,
               covered=0, cad_spans=0, gt_cads=0, cad_matched=0, jp_spans=0)
    names = Counter()
    for mscx, tsv in pieces:
        outj = cdir / f"{mscx.stem}.progressions.json"
        if not outj.exists() or outj.stat().st_size == 0:
            if not _run_dump(exe, mscx, outj, bash):
                continue
        try:
            d = json.loads(outj.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        p = d.get("progressions")
        if not p:
            continue
        agg["movements"] += 1
        agg["positions"] += p.get("positions", 0)
        spans = p.get("schemaSpans", [])
        agg["spans"] += len(spans)
        agg["seqs"] += p.get("sequenceCount", 0)
        agg["abstained"] += p.get("abstainedFeatureCount", 0)
        agg["overrides"] += p.get("overrideCount", 0)

        covered = set()
        our_cad_ticks = []
        for s in spans:
            names[s["name"]] += 1
            for idx in range(s.get("startIndex", 0), s.get("endIndex", 0)):
                covered.add(idx)
            idioms = s.get("idioms", 0)
            if (idioms & _JP_IDIOMS) and not (idioms & _CP_IDIOMS):
                agg["jp_spans"] += 1
            if _is_cadence_span(s["name"]):
                our_cad_ticks.append(s.get("endTick", 0))
        agg["covered"] += len(covered)
        agg["cad_spans"] += len(our_cad_ticks)

        try:
            cad_markers, _ = parse_cadence_phrase_markers(str(tsv))
            gt_ticks = [m.abs_tick for m in cad_markers if m.abs_tick is not None]
        except Exception:
            gt_ticks = []
        agg["gt_cads"] += len(gt_ticks)
        agg["cad_matched"] += _match_points(our_cad_ticks, gt_ticks)

    return agg, names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpora", nargs="*", default=DEV_BEDS)
    ap.add_argument("--limit", type=int, default=0, help="max movements per corpus (0 = all)")
    ap.add_argument("--json-out", default="")
    args = ap.parse_args()

    exe, bash = _find_exe(), _find_bash()
    if not exe:
        print("ERROR: batch_analyze not found (build first)", file=sys.stderr)
        return 2

    total = Counter()
    all_names = Counter()
    rows = []
    hdr = f"{'corpus':32} {'mv':>3} {'pos':>5} {'span':>4} {'cov%':>5} {'seq':>3} {'abst':>4} {'ovr':>3} {'cadP':>5} {'cadR':>5} {'jp':>3}"
    print(hdr)
    print("-" * len(hdr))
    for corpus in args.corpora:
        agg, names = _grade_corpus(corpus, exe, bash, args.limit)
        all_names.update(names)
        for k, v in agg.items():
            total[k] += v
        cov = 100.0 * agg["covered"] / agg["positions"] if agg["positions"] else 0.0
        cadP = 100.0 * agg["cad_matched"] / agg["cad_spans"] if agg["cad_spans"] else 0.0
        cadR = 100.0 * agg["cad_matched"] / agg["gt_cads"] if agg["gt_cads"] else 0.0
        print(f"{corpus:32} {agg['movements']:3} {agg['positions']:5} {agg['spans']:4} "
              f"{cov:5.1f} {agg['seqs']:3} {agg['abstained']:4} {agg['overrides']:3} "
              f"{cadP:5.1f} {cadR:5.1f} {agg['jp_spans']:3}")
        rows.append(dict(corpus=corpus, **agg))

    cov = 100.0 * total["covered"] / total["positions"] if total["positions"] else 0.0
    cadP = 100.0 * total["cad_matched"] / total["cad_spans"] if total["cad_spans"] else 0.0
    cadR = 100.0 * total["cad_matched"] / total["gt_cads"] if total["gt_cads"] else 0.0
    print("-" * len(hdr))
    print(f"{'TOTAL':32} {total['movements']:3} {total['positions']:5} {total['spans']:4} "
          f"{cov:5.1f} {total['seqs']:3} {total['abstained']:4} {total['overrides']:3} "
          f"{cadP:5.1f} {cadR:5.1f} {total['jp_spans']:3}")
    print("\nAdmitted schema-span name histogram (all dev beds):")
    for n, k in all_names.most_common():
        print(f"  {k:4}  {n}")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(dict(rows=rows, total=dict(total),
                                       names=dict(all_names)), indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
