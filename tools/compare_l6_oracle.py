#!/usr/bin/env python3
"""
compare_l6_oracle.py — the Layer-6 TSV-oracle validation metrics (design §10).

Two read-only measurements against the DCML `phraseend` / `cadence` GT columns
(now parsed by dcml_parser.parse_cadence_phrase_markers):

  1. Punctuation-span-boundary precision/recall — OUR L1.5 boundary ticks
     (batch_analyze --dump-fullspine "phraseBoundaryTicks") vs the GT `phraseend`
     bracket ticks, boundary-tolerant (± one beat).
  2. Cadence-location precision/recall — OUR dormant L5 detected cadences
     (--dump-fullspine "cadences[].arrivalTick", with "type") vs the GT `cadence`
     rows, LOCATION-scoped (design §10); cadence TYPE reported as a confusion
     matrix over {PAC, IAC, HC(+subtypes), DC, EC, PC} but NOT a gate.

Design choices (declared, per the CC dispatch):
  * A NEW compare_rn-adjacent module (not overloaded into compare_rn.py, whose
    align_dcml_regions is a *region-overlap* aligner — the wrong primitive for a
    point/boundary task).  Both metrics share ONE tolerance-based point matcher
    (match_points) — never a second matcher.
  * Tolerance = TOLERANCE_TICKS = one quarter-note beat (480 ticks): a DECLARED
    constant, not tuned.  (DCML onsets are quarter-based; ± one beat = ± 480.)
  * Tick basis is dcml_parser's (round(Fraction(quarterbeats)*480)) — the SAME
    basis OUR ticks use — so no second tick arithmetic is introduced.

This is a BASELINE measurement of the EXISTING dormant detectors; nothing here
moves a constant.  Descriptive only — a validation bed, not a gate.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT / "tools"))
from dcml_parser import parse_cadence_phrase_markers, TICKS_PER_QUARTER  # noqa: E402

# ± one beat, a declared constant (one quarter-note = 480 ticks).  Not tuned.
TOLERANCE_TICKS = TICKS_PER_QUARTER

# OUR fullspine cadence-type name (fsCadenceTypeName) -> GT cadence family.
_OUR_CAD_TO_GT = {
    "PerfectAuthentic":   "PAC",
    "ImperfectAuthentic": "IAC",
    "Half":               "HC",
    "PhrygianHalf":       "HC",   # HC.PHR family
    "Deceptive":          "DC",
    "Plagal":             "PC",
    "Evaded":             "EC",
    "None":               "None",
}

# The GT cadence-type axis for the confusion matrix (HC sub-types fold to HC).
_GT_CAD_FAMILIES = ["PAC", "IAC", "HC", "DC", "EC", "PC"]


def _gt_cadence_family(label: str) -> str:
    """Fold a GT cadence label ('PAC', 'HC.SIM', …) to its family axis."""
    base = label.split(".", 1)[0].strip()
    return base if base in _GT_CAD_FAMILIES else base


# ── The single shared point matcher ──────────────────────────────────────────

@dataclass
class MatchResult:
    matched: int                       # # of 1-1 matched pairs (within tol)
    ours_total: int
    gt_total: int
    ours_unmatched: list = field(default_factory=list)  # OUR ticks with no GT
    gt_unmatched: list = field(default_factory=list)     # GT ticks with no OUR
    pairs: list = field(default_factory=list)            # (our_tick, gt_tick, gt_idx)

    @property
    def precision(self) -> float:
        return self.matched / self.ours_total if self.ours_total else 0.0

    @property
    def recall(self) -> float:
        return self.matched / self.gt_total if self.gt_total else 0.0


def match_points(ours: list, gt: list, tol: int = TOLERANCE_TICKS) -> MatchResult:
    """Greedy 1-1 tolerance matching of two tick sequences.

    Deterministic: candidate pairs (|our-gt| <= tol) are sorted by (distance,
    our_tick, gt_tick) and consumed greedily, each tick used at most once — the
    standard boundary-tolerant P/R matcher.  `ours`/`gt` are lists of ints
    (duplicates de-duplicated first; a `}{` at one tick is one boundary).
    """
    ours_u = sorted(set(int(t) for t in ours))
    gt_u = sorted(set(int(t) for t in gt))
    cands = []
    for oi, ot in enumerate(ours_u):
        for gi, gt_t in enumerate(gt_u):
            d = abs(ot - gt_t)
            if d <= tol:
                cands.append((d, ot, gt_t, oi, gi))
    cands.sort()
    used_o, used_g = set(), set()
    pairs = []
    for d, ot, gt_t, oi, gi in cands:
        if oi in used_o or gi in used_g:
            continue
        used_o.add(oi)
        used_g.add(gi)
        pairs.append((ot, gt_t, gi))
    ours_unmatched = [t for i, t in enumerate(ours_u) if i not in used_o]
    gt_unmatched = [t for i, t in enumerate(gt_u) if i not in used_g]
    return MatchResult(matched=len(pairs), ours_total=len(ours_u), gt_total=len(gt_u),
                       ours_unmatched=ours_unmatched, gt_unmatched=gt_unmatched, pairs=pairs)


# ── Per-piece scoring ────────────────────────────────────────────────────────

@dataclass
class PieceBoundary:
    stem: str
    match: MatchResult
    gt_dropped_no_tick: int = 0   # GT phraseend markers with no abs_tick


@dataclass
class PieceCadence:
    stem: str
    match: MatchResult
    gt_dropped_no_tick: int = 0
    # confusion: (gt_family, our_family) -> count, over matched pairs only.
    confusion: dict = field(default_factory=dict)


def score_boundary(stem: str, fullspine: dict, tsv_path: Path) -> PieceBoundary:
    our_ticks = [int(t) for t in fullspine.get("phraseBoundaryTicks", [])]
    _cad, phrase_markers = parse_cadence_phrase_markers(str(tsv_path))
    gt_ticks = [m.abs_tick for m in phrase_markers if m.abs_tick is not None]
    dropped = sum(1 for m in phrase_markers if m.abs_tick is None)
    m = match_points(our_ticks, gt_ticks)
    return PieceBoundary(stem=stem, match=m, gt_dropped_no_tick=dropped)


def score_cadence(stem: str, fullspine: dict, tsv_path: Path) -> PieceCadence:
    our_cads = fullspine.get("cadences", [])
    our_ticks = [int(c["arrivalTick"]) for c in our_cads]
    our_type_by_tick = {}
    for c in our_cads:
        our_type_by_tick.setdefault(int(c["arrivalTick"]),
                                    _OUR_CAD_TO_GT.get(c.get("type", "None"), "None"))
    cad_markers, _phr = parse_cadence_phrase_markers(str(tsv_path))
    gt_ticks, gt_fam_by_tick = [], {}
    dropped = 0
    for mk in cad_markers:
        if mk.abs_tick is None:
            dropped += 1
            continue
        gt_ticks.append(mk.abs_tick)
        gt_fam_by_tick.setdefault(mk.abs_tick, _gt_cadence_family(mk.label))
    m = match_points(our_ticks, gt_ticks)
    confusion: dict = {}
    gt_u = sorted(set(gt_ticks))
    for our_tick, gt_tick, gi in m.pairs:
        gt_fam = gt_fam_by_tick.get(gt_u[gi], "?")
        our_fam = our_type_by_tick.get(our_tick, "None")
        confusion[(gt_fam, our_fam)] = confusion.get((gt_fam, our_fam), 0) + 1
    return PieceCadence(stem=stem, match=m, gt_dropped_no_tick=dropped, confusion=confusion)


# ── Aggregation ──────────────────────────────────────────────────────────────

def _agg_pr(pieces_matches: list) -> tuple:
    matched = sum(p.matched for p in pieces_matches)
    ours = sum(p.ours_total for p in pieces_matches)
    gt = sum(p.gt_total for p in pieces_matches)
    prec = matched / ours if ours else 0.0
    rec = matched / gt if gt else 0.0
    return matched, ours, gt, prec, rec


def _pct(x: float) -> str:
    return f"{100.0 * x:5.1f}%"


# ── Driver (batch_analyze --dump-fullspine over the dev beds) ─────────────────

import platform  # noqa: E402
import subprocess  # noqa: E402

_DCML = _REPO_ROOT / "tools" / "dcml"
_OUT_ROOT = _REPO_ROOT / "tools" / "corpus_l6_oracle"

# The L6 dev beds (registry split=dev): the 10 pre-wave-1 DLC members + 6 named.
DEV_BEDS = [
    "ABC", "bach_en_fr_suites", "chopin_mazurkas", "corelli", "cpe_bach_keyboard",
    "dvorak_silhouettes", "grieg_lyric_pieces", "mozart_piano_sonatas",
    "schumann_kinderszenen", "tchaikovsky_seasons",
    "beethoven_piano_sonatas", "wagner_overtures", "liszt_pelerinage",
    "rachmaninoff_piano", "schulhoff_suite_dansante_en_jazz", "monteverdi_madrigals",
]


def _find_batch_analyze() -> "Path | None":
    for p in (_REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
              _REPO_ROOT / "ninja_build_rel" / "batch_analyze"):
        if p.exists():
            return p
    return None


def _find_git_bash() -> "Path | None":
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


def _run_fullspine(exe: Path, mscx: Path, out: Path, bash: "Path | None", timeout: int,
                   dump_flag: str = "--dump-fullspine") -> bool:
    """Run batch_analyze with @p dump_flag (--dump-fullspine or --dump-l6), capturing
    stdout to `out`.  Launched via Git Bash on Windows (direct subprocess triggers a
    Qt access violation)."""
    try:
        if platform.system() == "Windows" and bash:
            cmd = f'{_to_unix(exe)} "{_to_unix(mscx)}" {dump_flag} > "{_to_unix(out)}"'
            r = subprocess.run([str(bash), "-c", cmd], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=timeout)
        else:
            with open(out, "wb") as fh:
                r = subprocess.run([str(exe), str(mscx), dump_flag],
                                   stdout=fh, stderr=subprocess.DEVNULL, timeout=timeout)
        return r.returncode == 0 and out.exists() and out.stat().st_size > 0
    except Exception:
        return False


# ── Task 3 — the §10 step-1 L6 validation (grades the --dump-l6 grouping structure) ─

# The §3.1 aggregate boundary baseline (cc_tsv_oracle_report.md): L6 adds NO detection,
# so its punctuation-span boundaries are the L1.5 picked set verbatim → the boundary
# oracle must stay within noise of this. A MATERIAL deviation ⇒ L6 leaked detection ⇒ STOP.
L6_BOUNDARY_BASELINE = {"precision": 0.348, "recall": 0.224}
L6_BOUNDARY_NOISE_PP = 3.0   # allowed |Δ| in percentage points before it is a STOP


def _key_tonic_minor(resolved: str) -> "tuple[int, bool]":
    from dcml_parser import _key_to_tonic_pc
    return _key_to_tonic_pc(resolved), (bool(resolved) and resolved[0].islower())


def gt_local_key_track(tsv_path: Path) -> list:
    """The GT local-key track: (abs_tick, tonicPc, minor) per region, the localkey
    resolved against globalkey (NOT the per-chord applied root)."""
    from dcml_parser import parse_abc_harmonies_file, _resolve_dcml_key
    track = []
    for r in parse_abc_harmonies_file(str(tsv_path)):
        if r.abs_tick is None:
            continue
        resolved = _resolve_dcml_key(r.local_key, r.global_key)
        tonic, minor = _key_tonic_minor(resolved)
        track.append((r.abs_tick, tonic, minor))
    track.sort()
    return track


def gt_key_change_ticks(track: list) -> list:
    """Ticks where the GT (tonic, minor) changes (excludes the first region)."""
    ticks, prev = [], None
    for tick, tonic, minor in track:
        if prev is not None and (tonic, minor) != prev:
            ticks.append(tick)
        prev = (tonic, minor)
    return ticks


def gt_key_at(track: list, tick: int) -> "tuple[int, bool] | None":
    """The GT (tonic, minor) active at @p tick (the last region starting at/before it)."""
    active = None
    for t, tonic, minor in track:
        if t <= tick:
            active = (tonic, minor)
        else:
            break
    return active


def score_l6(stem: str, fs: dict, tsv_path: Path) -> dict:
    """Grade the --dump-l6 grouping structure for one movement (§10 step 1)."""
    l6 = fs.get("l6", {})
    spans = l6.get("punctuationSpans", [])
    areas = l6.get("keyAreas", [])
    aligns = l6.get("cadenceAlignments", [])

    # 1) punctuation-span boundaries (interior span starts) vs GT phraseend.
    l6_boundaries = [s["startTick"] for s in spans[1:]]  # every span start except the first
    _cad, phrase_markers = parse_cadence_phrase_markers(str(tsv_path))
    gt_phrase = [m.abs_tick for m in phrase_markers if m.abs_tick is not None]
    bm = match_points(l6_boundaries, gt_phrase)

    # 1a) THE no-added-detection proof (§6 / the Task-3 STOP guard). L6 consumes the
    # L1.5 picked set as-is (§5.1 — no re-threshold, no re-detect); its punctuation-span
    # boundaries must be EXACTLY the interior of phraseBoundaryTicks. Any boundary L6
    # emits that is NOT in the L1.5 set is INVENTED detection ⇒ STOP. (The two edge ticks
    # at span start/end are legitimately dropped — an edge marker is not an interior cut.)
    pbt = set(int(t) for t in fs.get("phraseBoundaryTicks", []))
    span_start = spans[0]["startTick"] if spans else 0
    span_end = spans[-1]["endTick"] if spans else 0
    interior_pbt = {t for t in pbt if span_start < t < span_end}
    l6_set = set(l6_boundaries)
    added = l6_set - pbt                 # MUST be empty (L6 invented no boundary)
    dropped_edges = pbt - l6_set         # expected: the start/end edge markers

    # 2) key-area boundaries vs GT local-key change ticks + per-area tonic/mode match.
    track = gt_local_key_track(tsv_path)
    l6_ka_boundaries = [a["startTick"] for a in areas[1:]]
    km = match_points(l6_ka_boundaries, gt_key_change_ticks(track))
    tm_match = tm_total = 0
    for a in areas:
        gt = gt_key_at(track, a["startTick"])
        if gt is None:
            continue
        tm_total += 1
        if gt == (a["localTonicPc"], bool(a["localMinorMode"])):
            tm_match += 1

    # 3) cadence-to-span alignment counts + GT cadence-at-phrase-end rate.
    closes = sum(1 for a in aligns if a["kind"] == "ClosesSpan")
    internal = sum(1 for a in aligns if a["kind"] == "Internal")
    no_cadence_spans = sum(1 for s in spans if s["closingCadenceIndex"] < 0)

    return {
        "boundary": bm, "keyarea": km,
        "l6_added_boundaries": len(added),
        "l6_exact_interior": (l6_set == interior_pbt),
        "l6_dropped_edges": len(dropped_edges),
        "tonicmode_match": tm_match, "tonicmode_total": tm_total,
        "cad_closes": closes, "cad_internal": internal,
        "spans": len(spans), "no_cadence_spans": no_cadence_spans,
        "schema_count": l6.get("schemaSpanCount", 0),
    }


def _corpus_pieces(corpus: str) -> list:
    ms3 = _DCML / corpus / "MS3"
    harm = _DCML / corpus / "harmonies"
    out = []
    if not ms3.is_dir() or not harm.is_dir():
        return out
    for mscx in sorted(ms3.glob("*.mscx")):
        tsv = harm / f"{mscx.stem}.harmonies.tsv"
        if tsv.exists():
            out.append((mscx.stem, mscx, tsv))
    return out


def measure(corpora: list, timeout: int, limit: int, skip_cpp: bool) -> dict:
    exe = _find_batch_analyze()
    bash = _find_git_bash()
    if exe is None and not skip_cpp:
        print("ERROR: batch_analyze not found", file=sys.stderr)
        sys.exit(1)
    _OUT_ROOT.mkdir(parents=True, exist_ok=True)
    report: dict = {"corpora": {}, "tolerance_ticks": TOLERANCE_TICKS}

    for corpus in corpora:
        pieces = _corpus_pieces(corpus)
        if limit:
            pieces = pieces[:limit]
        cdir = _OUT_ROOT / corpus
        cdir.mkdir(parents=True, exist_ok=True)
        b_pieces, c_pieces = [], []
        ok = fail = 0
        gt_cad_total = 0
        for stem, mscx, tsv in pieces:
            fj = cdir / f"{stem}.fullspine.json"
            if not (skip_cpp and fj.exists()):
                if not _run_fullspine(exe, mscx, fj, bash, timeout):
                    fail += 1
                    continue
            try:
                fs = json.loads(fj.read_text(encoding="utf-8"))
            except Exception:
                fail += 1
                continue
            ok += 1
            b_pieces.append(score_boundary(stem, fs, tsv))
            pc = score_cadence(stem, fs, tsv)
            c_pieces.append(pc)
            gt_cad_total += pc.match.gt_total

        bm, bo, bg, bp, br = _agg_pr([p.match for p in b_pieces])
        cad_empty = (gt_cad_total == 0)
        cm, co, cg, cp, cr = _agg_pr([p.match for p in c_pieces]) if not cad_empty else (0, 0, 0, 0.0, 0.0)

        # confusion matrix (aggregate)
        conf: dict = {}
        for p in c_pieces:
            for k, v in p.confusion.items():
                conf[k] = conf.get(k, 0) + v

        # top-5 failure exemplars (stem@tick): boundary FN (GT unmatched) + FP (OUR unmatched)
        b_fn = [(p.stem, t) for p in b_pieces for t in p.match.gt_unmatched]
        b_fp = [(p.stem, t) for p in b_pieces for t in p.match.ours_unmatched]
        c_fn = [(p.stem, t) for p in c_pieces for t in p.match.gt_unmatched]
        c_fp = [(p.stem, t) for p in c_pieces for t in p.match.ours_unmatched]

        report["corpora"][corpus] = {
            "movements_ok": ok, "movements_fail": fail,
            "boundary": {"matched": bm, "ours": bo, "gt": bg,
                         "precision": bp, "recall": br,
                         "gt_dropped_no_tick": sum(p.gt_dropped_no_tick for p in b_pieces)},
            "cadence": ({"skipped": True, "reason": "0 GT cadence labels"} if cad_empty else
                        {"matched": cm, "ours": co, "gt": cg, "precision": cp, "recall": cr,
                         "gt_dropped_no_tick": sum(p.gt_dropped_no_tick for p in c_pieces)}),
            "confusion": {f"{g}->{o}": n for (g, o), n in sorted(conf.items())},
            "boundary_fn_top5": [f"{s}@{t}" for s, t in b_fn[:5]],   # GT boundary, no OUR pick
            "boundary_fp_top5": [f"{s}@{t}" for s, t in b_fp[:5]],   # OUR boundary, no GT
            "cadence_fn_top5": [f"{s}@{t}" for s, t in c_fn[:5]],    # GT cadence, no OUR detect
            "cadence_fp_top5": [f"{s}@{t}" for s, t in c_fp[:5]],    # OUR cadence, no GT
        }
        cad_str = ("cadence SKIP (0 GT)" if cad_empty
                   else f"cadence P={_pct(cp)} R={_pct(cr)} ({cm}/{co} | {cm}/{cg})")
        print(f"{corpus:34} ok={ok:3} fail={fail:2} | "
              f"boundary P={_pct(bp)} R={_pct(br)} ({bm}/{bo} | {bm}/{bg}) | {cad_str}")

    return report


def measure_l6(corpora: list, timeout: int, limit: int, skip_cpp: bool) -> dict:
    """Task 3 — grade the --dump-l6 grouping structure on the dev beds (§10 step 1).
    Boundary metric is asserted within noise of the L1.5 baseline (else a STOP)."""
    exe, bash = _find_batch_analyze(), _find_git_bash()
    (_OUT_ROOT / "_l6").mkdir(parents=True, exist_ok=True)
    report: dict = {"corpora": {}, "tolerance_ticks": TOLERANCE_TICKS,
                    "boundary_baseline": L6_BOUNDARY_BASELINE}
    for corpus in corpora:
        pieces = _corpus_pieces(corpus)
        if limit:
            pieces = pieces[:limit]
        cdir = _OUT_ROOT / "_l6" / corpus
        cdir.mkdir(parents=True, exist_ok=True)
        rows = []
        ok = fail = 0
        for stem, mscx, tsv in pieces:
            fj = cdir / f"{stem}.l6.json"
            if not (skip_cpp and fj.exists()):
                if not _run_fullspine(exe, mscx, fj, bash, timeout, "--dump-l6"):
                    fail += 1
                    continue
            try:
                fs = json.loads(fj.read_text(encoding="utf-8"))
            except Exception:
                fail += 1
                continue
            ok += 1
            r = score_l6(stem, fs, tsv)
            r["stem"] = stem
            rows.append(r)

        bm, bo, bg, bp, br = _agg_pr([r["boundary"] for r in rows])
        km, ko, kg, kp, kr = _agg_pr([r["keyarea"] for r in rows])
        added = sum(r["l6_added_boundaries"] for r in rows)
        exact = sum(1 for r in rows if r["l6_exact_interior"])
        tm_m = sum(r["tonicmode_match"] for r in rows)
        tm_t = sum(r["tonicmode_total"] for r in rows)
        closes = sum(r["cad_closes"] for r in rows)
        internal = sum(r["cad_internal"] for r in rows)
        no_cad = sum(r["no_cadence_spans"] for r in rows)
        spans = sum(r["spans"] for r in rows)
        schema = sum(r["schema_count"] for r in rows)

        # GT cadence-at-phrase-end rate (context for closes/internal): a GT cadence that
        # coincides (±tol) with a GT phraseend marker.
        gt_cad_at_phrase = gt_cad_total = 0
        for stem, mscx, tsv in pieces:
            cad_mk, phr_mk = parse_cadence_phrase_markers(str(tsv))
            cad_ticks = [m.abs_tick for m in cad_mk if m.abs_tick is not None]
            phr_ticks = [m.abs_tick for m in phr_mk if m.abs_tick is not None]
            if not cad_ticks:
                continue
            gt_cad_total += len(set(cad_ticks))
            gt_cad_at_phrase += match_points(cad_ticks, phr_ticks).matched

        report["corpora"][corpus] = {
            "movements_ok": ok, "movements_fail": fail,
            "boundary": {"matched": bm, "ours": bo, "gt": bg, "precision": bp, "recall": br},
            "keyarea": {"matched": km, "ours": ko, "gt": kg, "precision": kp, "recall": kr},
            "l6_added_boundaries": added, "l6_exact_interior_movements": exact,
            "tonicmode_match": tm_m, "tonicmode_total": tm_t,
            "cad_closes": closes, "cad_internal": internal,
            "no_cadence_spans": no_cad, "spans": spans, "schema_count": schema,
            "gt_cad_at_phrase": gt_cad_at_phrase, "gt_cad_total": gt_cad_total,
        }
        tmrate = (100.0 * tm_m / tm_t) if tm_t else 0.0
        print(f"{corpus:30} ok={ok:3} added={added:2} exact={exact}/{ok} | "
              f"bound P={_pct(bp)} R={_pct(br)} | keyarea P={_pct(kp)} R={_pct(kr)} "
              f"tonic/mode={tmrate:4.0f}% | cad closes={closes} internal={internal}")
    return report


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpora", default="", help="comma list; default = all 16 dev beds")
    ap.add_argument("--timeout", type=int, default=120)
    ap.add_argument("--limit", type=int, default=0, help="cap movements per corpus (0=all)")
    ap.add_argument("--skip-cpp", action="store_true", help="reuse cached fullspine JSON")
    ap.add_argument("--l6", action="store_true", help="Task 3: grade the --dump-l6 grouping structure")
    ap.add_argument("--out", default="", help="write full report JSON here")
    args = ap.parse_args()
    corpora = [c.strip() for c in args.corpora.split(",") if c.strip()] or DEV_BEDS

    if args.l6:
        report = measure_l6(corpora, args.timeout, args.limit, args.skip_cpp)
        # aggregate boundary + keyarea; assert boundary within noise of the L1.5 baseline.
        for name in ("boundary", "keyarea"):
            t = {"matched": 0, "ours": 0, "gt": 0}
            for c in report["corpora"].values():
                for kk in t:
                    t[kk] += c[name][kk]
            p = t["matched"] / t["ours"] if t["ours"] else 0.0
            r = t["matched"] / t["gt"] if t["gt"] else 0.0
            report[f"aggregate_{name}"] = {**t, "precision": p, "recall": r}
            print(f"AGGREGATE {name:9} P={_pct(p)} R={_pct(r)} ({t['matched']}/{t['ours']} | {t['matched']}/{t['gt']})")
        # THE no-added-detection STOP guard (exact + structural): L6's boundaries are
        # a SUBSET of the L1.5 picked set on every movement — it invents none. (This is
        # the faithful form of "L6 adds no detection"; the fuzzy P/R-vs-baseline band is
        # confounded by the legitimate edge-tick exclusion, so the exact set check is used.)
        total_added = sum(c["l6_added_boundaries"] for c in report["corpora"].values())
        total_exact = sum(c["l6_exact_interior_movements"] for c in report["corpora"].values())
        total_mv = sum(c["movements_ok"] for c in report["corpora"].values())
        report["no_added_detection"] = {"total_added_boundaries": total_added,
                                        "exact_interior_movements": total_exact,
                                        "movements": total_mv}
        agg_b = report["aggregate_boundary"]
        dP = 100.0 * (agg_b["precision"] - L6_BOUNDARY_BASELINE["precision"])
        dR = 100.0 * (agg_b["recall"] - L6_BOUNDARY_BASELINE["recall"])
        report["boundary_vs_baseline"] = {"dP_pp": round(dP, 2), "dR_pp": round(dR, 2),
                                          "note": "differs from the §3.1 baseline only by the "
                                                  "legitimate start/end edge-tick exclusion"}
        print(f"NO-ADDED-DETECTION: added boundaries={total_added} (MUST be 0) | "
              f"exact-interior movements={total_exact}/{total_mv} "
              f"-> {'PASS (L6 invented no boundary)' if total_added == 0 else 'STOP — L6 LEAKED DETECTION'}")
        print(f"BOUNDARY P/R vs §3.1 baseline: dP={dP:+.2f}pp dR={dR:+.2f}pp "
              f"(edge-tick exclusion only; descriptive)")
        tot_closes = sum(c["cad_closes"] for c in report["corpora"].values())
        tot_internal = sum(c["cad_internal"] for c in report["corpora"].values())
        gcap = sum(c["gt_cad_at_phrase"] for c in report["corpora"].values())
        gct = sum(c["gt_cad_total"] for c in report["corpora"].values())
        print(f"CADENCE alignment: closes={tot_closes} internal={tot_internal} | "
              f"GT cadence-at-phraseend rate={_pct(gcap/gct) if gct else 'n/a'} ({gcap}/{gct})")
        if args.out:
            Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")
            print(f"[wrote {args.out}]")
        return

    report = measure(corpora, args.timeout, args.limit, args.skip_cpp)

    # Aggregate across all measured corpora.
    def _sum(path_metric):
        tot = {"matched": 0, "ours": 0, "gt": 0}
        for c in report["corpora"].values():
            m = c[path_metric]
            if m.get("skipped"):
                continue
            tot["matched"] += m["matched"]; tot["ours"] += m["ours"]; tot["gt"] += m["gt"]
        return tot
    for name in ("boundary", "cadence"):
        t = _sum(name)
        p = t["matched"] / t["ours"] if t["ours"] else 0.0
        r = t["matched"] / t["gt"] if t["gt"] else 0.0
        report[f"aggregate_{name}"] = {**t, "precision": p, "recall": r}
        print(f"AGGREGATE {name:9} P={_pct(p)} R={_pct(r)} "
              f"({t['matched']}/{t['ours']} | {t['matched']}/{t['gt']})")

    if args.out:
        Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"[wrote {args.out}]")


if __name__ == "__main__":
    main()
