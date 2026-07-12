#!/usr/bin/env python3
"""classify_key_disagreement.py — the OI-141 key/mode-inference diagnosis classifier.

READ-ONLY. No src/ change, no constant tuned, no golden refresh; no write to
tools/robust_stop/ or tools/corpus/. Executes cc_instruction_key_mode_inference_
diagnosis.md (Cowork, 2026-07-12) whose Premise-Gate opening (cause classes +
written predictions) is cowork_key_mode_inference_diagnosis.md.

WHAT IT DOES
------------
Labels EVERY key-disagreeing run of duration with exactly ONE primary cause from
the opening document's closed list, on the SAME unit that produces the ratified
key-agreement column (a8_rebaseline_measure.py: union-of-boundaries cells, our
region key vs the DCML GLOBAL key, duration-weighted). Establishment (#19) FIRST:
the classified failing duration must reconcile EXACTLY with a8's b_key_dis + b_key_fail
per preset before any share is read.

ONE loading substrate, no second parser — reuses:
  * compare_analyses.load_analysis / _dcml_time_spans   (region + DCML tick spans)
  * compare_rn.classify_pair / _active_index_at          (the a8 cell scoring + membership)
  * compare_rn._our_key_tonic / _dcml_key_tonic          (the ratified key identity parsers)
  * dcml_parser.find_wir_file / parse_rntxt_file         (WiR reference; carries global_key + local_key)
  * run_bach_preset._run_batch_analyze                   (the --dump-joint-probe invocation)
  * measure_joint_probe._key_ident                       (the carried-menu KeySigMode->(pc,is_major) table)

The failing MASS and its per-cause duration are computed over the FROZEN corpus
(tools/corpus/<preset>/*.ours.json, corpus c50002fee1) so reconciliation to a8 is
guaranteed by construction. The carried KEY menu (keyAlternatives) — needed only
for the carried/outranked flags and the wrong-neighborhood cause — comes from a
--dump-joint-probe run, joined to the frozen regions by start tick; the join match
rate is reported (a coverage caveat, OI-33), and the standard .ours.json does NOT
carry the key menu (only keyModeRunnerUp), which is why the probe is run.

THE CAUSE CLASSES (mechanical; each rule is stated + justified in the report)
Let  K = our region key as (tonic_pc, is_major) via crn._our_key_tonic
     G = DCML GLOBAL key (piece constant, the a8 grading target) via crn._dcml_key_tonic
     L = DCML LOCAL key at the cell (the key IN EFFECT — tracks tonicization/modulation)
A run is failing iff K != G at pitch-class identity (== a8 key_verdict 'disagree'),
or our key is unparseable (== a8 'keyfail', a distinct reconciled bucket).
collection(pc,maj) = pc if maj else (pc+3)%12   (the relative-major tonic = the diatonic
                     collection's identifying pitch class).

Each failing run gets ONE primary cause under BOTH anchorings of the closed list:
  * GLOBAL-anchored (doc-literal): relative/parallel/wrong-neighborhood measured vs G.
  * LOCAL-anchored (diagnostic): measured vs L (the in-effect key = what "true" means
    musically and what our analyzer tracks). This separates the tonicization label-gap
    (K == L) from genuine local errors and is the primary explanatory view.
Precedence (first match wins), justified in the report:
  1 enharmonic          K == G at pc but spelled differently — impossible at this unit
                        (a8 compares pc identity), reported as structurally 0.
  2 tonicization/modul. K == L and L != G — we match the DCML LOCAL key; the disagreement
                        is only against the global-key grading (the label-gap; anchor-free).
  3 relative-key        collection(K) == collection(ref) and K != ref (relative maj/min).
  4 parallel-mode       tonic(K) == tonic(ref), mode differs.
  5 segmentation-edge   run.dur < one measure AND both temporal neighbors key-agree AND
                        a DCML local-key change lies within +/- one measure (a real GT
                        boundary we placed at a different tick — WHERE not WHETHER).
  6 wrong-neighborhood  ref absent from the carried menu AND ref is not a collection-sibling
                        of any carried key (the true key area was never even offered).
  else UNCLASSIFIED     counted, never forced; characterized by K's relationship to L
                        (dominant/subdominant, distant).
(ref = G for the global-anchored pass, L for the local-anchored pass.)

Per run also: G carried/absent flag, outranked flag (carried ⟹ outranked within the
failing set, since argmax != G), and — for relative-key runs whose true key (G or L) is
the MINOR sibling — the leading-tone presence test (is (tonic + 11) % 12 present among the
run's sounding pitch classes, unioned from our regions' pitchClassSet).

CORPUS INTEGRITY (#9/#19): pieces whose SCORE is transposed vs the WiR reference edition
(constant whole-piece root offset) are detected and reported separately — they are ~100%
key- AND root-disagree by construction, NOT key-inference error. Included in the
a8-reconciling tables; a clean-corpus companion view excludes them.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import multiprocessing
import statistics
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))

import run_bach_preset as rbp          # noqa: E402
import compare_analyses as cmp         # noqa: E402
import compare_rn as crn               # noqa: E402
import dcml_parser as dcml             # noqa: E402
import measure_joint_probe as mjp      # noqa: E402  (reuse _key_ident + _MAJOR_MODE_IDX; #6)

_REPO_ROOT = Path(__file__).resolve().parent.parent
WIR_DIR = _REPO_ROOT / "tools" / "dcml" / "when_in_rome"
PRESETS = ["Baroque", "Jazz", "Default"]
PRESET_DIR = {"Baroque": "baroque", "Jazz": "jazz", "Default": "default"}

CAUSES = [
    "enharmonic",
    "tonicization_vs_modulation",
    "relative_key",
    "parallel_mode",
    "segmentation_edge",
    "wrong_neighborhood",
    "unclassified",
    "unparseable_our_key",   # the a8 keyfail bucket (distinct; reconciles b_key_fail)
]


def collection_id(ident):
    """(tonic_pc, is_major) -> the identifying pc of its diatonic collection
    (the relative-major tonic). Major C and minor A both map to 0."""
    pc, maj = ident
    return pc if maj else (pc + 3) % 12


def is_relative(a, b):
    """Share a diatonic collection but differ (relative major/minor)."""
    return a is not None and b is not None and a != b and collection_id(a) == collection_id(b)


def is_parallel(a, b):
    """Same tonic, different mode (C major vs C minor)."""
    return a is not None and b is not None and a[0] == b[0] and a[1] != b[1]


def is_sibling_or_same(a, b):
    """a is b, its relative, or its parallel — 'a collection sibling of b'."""
    return a is not None and b is not None and (a == b or is_relative(a, b) or is_parallel(a, b))


# ── corpus-integrity: transposition-mismatched pieces (#9/#19) ────────────────
# A piece is transposition-mismatched iff the modal (our_root - dcml_root) mod 12
# offset over aligned root-defined regions is NONZERO and covers >= TRANSPOSE_FRAC of
# them. That constant whole-piece offset is the unmistakable signature of a differently-
# transposed SCORE edition (same progressions, shifted) — our reading follows the notated
# signature, the WiR reference edition is in another key — NOT a key-inference error. Such
# a piece is ~100% key-disagree AND ~100% root-disagree by construction; it contaminates
# BOTH the a8 key-agree and root-agree columns. Detected + reported (not silently dropped);
# the primary classification still INCLUDES them (to reconcile with the a8 column, which
# also includes them), with a clean-corpus companion view that excludes them.
TRANSPOSE_FRAC = 0.7


def _piece_transposition(ours_regions, wir_regions):
    """Return (is_transposed, modal_offset, frac, n_aligned)."""
    if not ours_regions or not wir_regions:
        return (False, 0, 0.0, 0)
    spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    off = Counter()
    n = 0
    for r in ours_regions:
        di = crn._active_index_at(spans, r.start_tick)
        if di is None:
            continue
        dr = wir_regions[di]
        if dr.root_pc is None or r.root_pc is None or r.root_pc < 0:
            continue
        off[(r.root_pc - dr.root_pc) % 12] += 1
        n += 1
    if n < 5:
        return (False, 0, 0.0, n)
    modal, cnt = off.most_common(1)[0]
    frac = cnt / n
    return (modal != 0 and frac >= TRANSPOSE_FRAC, modal, round(frac, 3), n)


# ── per-piece measure length (ticks), for the segmentation-edge rule ──────────
def _measure_ticks(ours_regions):
    """Median inter-measure tick gap: for each measureNumber take its first region's
    startTick, then the median positive gap between consecutive distinct measures.
    Bach chorales are 480 ticks/quarter -> 1920 (4/4) or 1440 (3/4). Falls back to
    1920 if under-determined."""
    first_tick = {}
    for r in ours_regions:
        mn = r.measure_number
        if mn not in first_tick or r.start_tick < first_tick[mn]:
            first_tick[mn] = r.start_tick
    if len(first_tick) < 2:
        return 1920
    items = sorted(first_tick.items())
    gaps = []
    for (m0, t0), (m1, t1) in zip(items, items[1:]):
        dm = m1 - m0
        if dm > 0 and t1 > t0:
            gaps.append((t1 - t0) / dm)
    if not gaps:
        return 1920
    return statistics.median(gaps)


def _run_probe_menus(exe, xml_path, preset, scratch):
    """Run --dump-joint-probe for one score; return {startTick: (menu_idents, keyconf_pop)}
    where menu_idents is the frozenset of (pc,is_major) for argmaxKey ∪ alternatives, and
    keyconf_pop is True iff any carried alt has keyConf>0. Also returns the probe region
    (startTick,endTick,key) tuples for the region-stream match check."""
    stem = xml_path.stem
    out_path = Path(scratch) / f"{preset}_{stem}.joint.json"
    ok = rbp._run_batch_analyze(exe, xml_path, out_path, preset,
                                diag_fh=None, extra_args="--dump-joint-probe")
    menus = {}
    probe_regions = []
    if not ok or not out_path.exists():
        return menus, probe_regions, "PROBE_FAILED"
    try:
        raw = json.loads(out_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return menus, probe_regions, f"PROBE_PARSE_ERR:{exc}"
    finally:
        try:
            out_path.unlink()
        except OSError:
            pass
    for reg in raw.get("regions", []):
        st = reg.get("startTick")
        probe_regions.append((st, reg.get("endTick"), reg.get("key")))
        p = reg.get("probe", {})
        ak = p.get("argmaxKey", {})
        idents = set()
        ai = mjp._key_ident(ak.get("tonicPc"), ak.get("mode"))
        if ai is not None:
            idents.add(ai)
        keyconf_pop = False
        for a in p.get("alternatives", []):
            xi = mjp._key_ident(a.get("tonicPc"), a.get("mode"))
            if xi is not None:
                idents.add(xi)
            kc = a.get("keyConf", 0.0)
            if kc is not None and kc > 0.0:
                keyconf_pop = True
        menus[st] = (frozenset(idents), keyconf_pop)
    return menus, probe_regions, "OK"


def _build_cells(stem, ours_regions, wir_regions):
    """Re-run the a8 union-of-boundaries loop, attaching the key strings/idents, the
    local key, the pcs, and the a8 key_verdict per SCORED cell. Reuses the exact a8
    substrate (crn._active_index_at, cmp._dcml_time_spans, crn.classify_pair,
    crn._our_key_tonic/_dcml_key_tonic) so the scored set and key_verdict reconcile
    to a8 by construction."""
    cells = []
    if not ours_regions or not wir_regions:
        return cells
    ours_spans = [(r.start_tick, r.end_tick) for r in ours_regions]
    dcml_spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    bounds = set()
    for (s, e) in ours_spans:
        if e > s:
            bounds.add(s); bounds.add(e)
    for (s, e) in dcml_spans:
        if s >= 0 and e > s:
            bounds.add(s); bounds.add(e)
    if len(bounds) < 2:
        return cells
    grid = sorted(bounds)
    for i in range(len(grid) - 1):
        t0, t1 = grid[i], grid[i + 1]
        if t1 - t0 <= 0:
            continue
        oi = crn._active_index_at(ours_spans, t0)
        di = crn._active_index_at(dcml_spans, t0)
        if oi is None or di is None:
            continue                      # unscored (a8 counts as unscored_dur)
        our_r = ours_regions[oi]
        dcml_r = wir_regions[di]
        pair = crn.classify_pair(our_r, dcml_r)
        if pair is None:
            continue                      # unscored (a8 skips)
        k = crn._our_key_tonic(getattr(our_r, "key", None))
        g = crn._dcml_key_tonic(getattr(dcml_r, "global_key", None))
        l = crn._dcml_key_tonic(getattr(dcml_r, "local_key", None))
        our_ident = k if k[0] is not None else None
        g_ident = g if g[0] is not None else None
        l_ident = l if l[0] is not None else None
        if our_ident is None:
            verdict = "keyfail"
        elif g_ident is None:
            verdict = "dcml_keyfail"
        elif our_ident == g_ident:
            verdict = "agree"
        else:
            verdict = "disagree"
        cells.append({
            "t0": t0, "t1": t1, "w": t1 - t0,
            "our_ident": our_ident, "g_ident": g_ident, "l_ident": l_ident,
            "our_key": getattr(our_r, "key", None),
            "g_key": getattr(dcml_r, "global_key", None),
            "l_key": getattr(dcml_r, "local_key", None),
            "pcs": our_r.pitch_class_set or 0,
            "our_start": our_r.start_tick,
            "verdict": verdict,
        })
    return cells


def _pcs_list(bitmap):
    return [i for i in range(12) if bitmap & (1 << i)]


def _merge_failing_runs(cells):
    """Merge adjacent failing cells (verdict in disagree/keyfail/dcml_keyfail) sharing
    (our_key, g_key, l_key) whose spans touch, into runs. Non-failing cells are kept in
    `cells` order for neighbor lookup by the caller."""
    runs = []
    cur = None
    for idx, c in enumerate(cells):
        if c["verdict"] not in ("disagree", "keyfail", "dcml_keyfail"):
            if cur:
                runs.append(cur); cur = None
            continue
        key = (c["our_key"], c["g_key"], c["l_key"], c["verdict"])
        if cur and cur["mkey"] == key and cur["end"] == c["t0"]:
            cur["end"] = c["t1"]; cur["dur"] += c["w"]
            cur["pcs"] |= c["pcs"]
            cur["cell_idxs"].append(idx)
        else:
            if cur:
                runs.append(cur)
            cur = {"mkey": key, "start": c["t0"], "end": c["t1"], "dur": c["w"],
                   "verdict": c["verdict"], "our_ident": c["our_ident"],
                   "g_ident": c["g_ident"], "l_ident": c["l_ident"],
                   "our_key": c["our_key"], "g_key": c["g_key"], "l_key": c["l_key"],
                   "pcs": c["pcs"], "cell_idxs": [idx],
                   "our_starts": set()}
        cur["our_starts"].add(c["our_start"])
    if cur:
        runs.append(cur)
    return runs


def _rel_kind(a, b):
    """Plain-word relationship of our key `a` to reference key `b` (both (pc,is_major)):
    equal / relative / parallel / dominant_or_subdominant (tonic a perfect fifth from b) /
    distant / na."""
    if a is None or b is None:
        return "na"
    if a == b:
        return "equal"
    if is_relative(a, b):
        return "relative"
    if is_parallel(a, b):
        return "parallel"
    if a[0] == (b[0] + 7) % 12 or a[0] == (b[0] + 5) % 12:
        return "dominant_or_subdominant"
    return "distant"


def _classify_one(stem, cells, wir_regions, ours_regions, menus, measure_ticks):
    """Classify each failing run of one piece under BOTH anchorings:
      * cause_global — the opening document's literal classes, ground-truth key = the
        piece GLOBAL key (the a8 grading target). relative/parallel are vs global.
      * cause_local  — the diagnostic refinement, ground-truth key = the DCML LOCAL key
        (the key IN EFFECT — what "true" means musically and what our analyzer tracks).
        Separates the tonicization label-gap (our == local) from genuine local errors.
    Also records our-key relationships to local and to global, the carried/outranked
    flags, and the leading-tone test under both anchorings.
    """
    runs = _merge_failing_runs(cells)
    out = []
    for run in runs:
        i0 = run["cell_idxs"][0]
        i1 = run["cell_idxs"][-1]
        prev_agree = (i0 - 1 >= 0 and cells[i0 - 1]["verdict"] == "agree")
        next_agree = (i1 + 1 < len(cells) and cells[i1 + 1]["verdict"] == "agree")
        short = run["dur"] < measure_ticks
        # menu union over the run's ours-regions (carried key menu, from the probe join)
        menu_idents = set()
        menu_join = 0
        menu_total = 0
        keyconf_pop = False
        for st in run["our_starts"]:
            menu_total += 1
            m = menus.get(st)
            if m is not None:
                menu_join += 1
                menu_idents |= set(m[0])
                keyconf_pop = keyconf_pop or m[1]
        menu_available = (menu_join == menu_total and menu_total > 0)
        g_ident = run["g_ident"]
        our_ident = run["our_ident"]
        l_ident = run["l_ident"]
        g_carried = (g_ident is not None and g_ident in menu_idents) if menu_idents else False
        g_sibling_of_carried = any(is_sibling_or_same(g_ident, c) for c in menu_idents) if (menu_idents and g_ident) else False
        l_carried = (l_ident is not None and l_ident in menu_idents) if menu_idents else False
        l_sibling_of_carried = any(is_sibling_or_same(l_ident, c) for c in menu_idents) if (menu_idents and l_ident) else False

        seg_gt_boundary = _has_gt_boundary_near(run, cells, wir_regions, ours_regions,
                                                measure_ticks)

        rel_to_local = _rel_kind(our_ident, l_ident)
        rel_to_global = _rel_kind(our_ident, g_ident)

        cause_global = _primary_cause(run, our_ident, g_ident, l_ident, prev_agree,
                                      next_agree, short, seg_gt_boundary, menu_available,
                                      g_carried, g_sibling_of_carried, anchor="global")
        cause_local = _primary_cause(run, our_ident, g_ident, l_ident, prev_agree,
                                     next_agree, short, seg_gt_boundary, menu_available,
                                     l_carried, l_sibling_of_carried, anchor="local")

        # ── leading-tone test (relative-key runs whose TRUE key is the MINOR sibling) ──
        # under each anchoring the "true key" is that anchoring's reference key.
        def _lt(ref_ident, cause):
            if cause != "relative_key" or ref_ident is None or ref_ident[1]:
                return (False, None)
            lt_pc = (ref_ident[0] + 11) % 12
            return (True, bool(run["pcs"] & (1 << lt_pc)))

        lt_g_appl, lt_g_present = _lt(g_ident, cause_global)
        lt_l_appl, lt_l_present = _lt(l_ident, cause_local)

        out.append({
            "stem": stem, "start": run["start"], "end": run["end"], "dur": run["dur"],
            "verdict": run["verdict"],
            "cause_global": cause_global, "cause_local": cause_local,
            "rel_to_local": rel_to_local, "rel_to_global": rel_to_global,
            "local_eq_global": (l_ident == g_ident),
            "our_key": run["our_key"], "g_key": run["g_key"], "l_key": run["l_key"],
            "our_ident": our_ident, "g_ident": g_ident, "l_ident": l_ident,
            "short": short, "prev_agree": prev_agree, "next_agree": next_agree,
            "seg_gt_boundary": seg_gt_boundary,
            "menu_available": menu_available, "menu_join": menu_join, "menu_total": menu_total,
            "g_carried": g_carried, "l_carried": l_carried, "keyconf_pop": keyconf_pop,
            "lt_g_appl": lt_g_appl, "lt_g_present": lt_g_present,
            "lt_l_appl": lt_l_appl, "lt_l_present": lt_l_present,
            "pcs": _pcs_list(run["pcs"]),
        })
    return out


def _has_gt_boundary_near(run, cells, wir_regions, ours_regions, measure_ticks):
    """True iff a DCML LOCAL key change falls within +/- one measure of the run's tick
    span. WiR regions have no abs_tick, so we map each WiR region to its ours-tick via
    the same DCML span mapping used to build the grid, then test for a local-key change
    among WiR regions whose mapped tick lies within [start-measure, end+measure]."""
    if not wir_regions or not ours_regions:
        return False
    dcml_spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    lo = run["start"] - measure_ticks
    hi = run["end"] + measure_ticks
    prev_lk = None
    for r, (s, e) in zip(wir_regions, dcml_spans):
        if s < 0 or e <= s:
            continue
        lk = crn._dcml_key_tonic(r.local_key)
        if prev_lk is not None and lk != prev_lk:
            # this WiR region starts a new local key at tick s
            if lo <= s <= hi:
                return True
        prev_lk = lk
    return False


def _primary_cause(run, our_ident, g_ident, l_ident, prev_agree, next_agree, short,
                   seg_gt_boundary, menu_available, ref_carried, ref_sibling_of_carried,
                   anchor):
    """One primary cause per failing run (opening-document closed list). `anchor`
    selects the ground-truth reference for the IDENTITY classes:
      anchor='global' -> reference = g_ident (the a8 grading target; doc-literal).
      anchor='local'  -> reference = l_ident (the key in effect; the diagnostic view).
    Precedence: enharmonic -> tonicization/modulation (our==local!=global, the label-gap,
    identical under both anchorings) -> relative -> parallel -> segmentation-edge ->
    wrong-neighborhood -> UNCLASSIFIED (counted, never forced)."""
    if run["verdict"] in ("keyfail", "dcml_keyfail"):
        return "unparseable_our_key"
    ref = g_ident if anchor == "global" else l_ident
    # 1 enharmonic — impossible at the pc unit (a8 compares pc identity); kept for completeness.
    if our_ident is not None and g_ident is not None and our_ident == g_ident:
        return "enharmonic"
    # 2 tonicization vs modulation — we match the DCML LOCAL key while it differs from the
    #   global (would-agree-against-local; the label-gap). Anchor-independent.
    if l_ident is not None and our_ident == l_ident and l_ident != g_ident:
        return "tonicization_vs_modulation"
    # 3 relative-key confusion (vs the anchor's reference key)
    if is_relative(our_ident, ref):
        return "relative_key"
    # 4 parallel-mode confusion (vs the anchor's reference key)
    if is_parallel(our_ident, ref):
        return "parallel_mode"
    # 5 segmentation-edge — short, flanked by agreement, near a real GT local-key change.
    if short and prev_agree and next_agree and seg_gt_boundary:
        return "segmentation_edge"
    # 6 wrong-neighborhood — the anchor's reference key absent from the carried menu AND not
    #   a collection-sibling of anything carried (the true key area was never offered).
    if menu_available and not ref_carried and not ref_sibling_of_carried:
        return "wrong_neighborhood"
    return "unclassified"


def _collect_one(args_tuple):
    exe, xml_path, preset, scratch = args_tuple
    stem = xml_path.stem
    corpus_dir = _REPO_ROOT / "tools" / "corpus" / PRESET_DIR[preset]
    ours_path = corpus_dir / f"{stem}.ours.json"
    if not ours_path.exists():
        return (stem, "NO_OURS", None)
    try:
        _, ours_regions = cmp.load_analysis(ours_path)
    except Exception as exc:
        return (stem, f"OURS_ERR:{exc}", None)
    if not ours_regions:
        return (stem, "EMPTY_OURS", None)
    wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
    if not wir_path:
        return (stem, "NO_WIR", None)
    try:
        wir_regions = dcml.parse_rntxt_file(wir_path)
    except Exception:
        wir_regions = []
    if not wir_regions:
        return (stem, "NO_WIR", None)

    menus, probe_regions, pstatus = _run_probe_menus(exe, xml_path, preset, scratch)
    # region-stream match check (establishment of the join): frozen vs probe (startTick,endTick,key)
    frozen_tuples = [(r.start_tick, r.end_tick, r.key) for r in ours_regions]
    probe_by_tick = {t[0]: t for t in probe_regions}
    match = sum(1 for (s, e, k) in frozen_tuples if probe_by_tick.get(s) == (s, e, k))
    stream_stats = {"frozen_n": len(frozen_tuples), "probe_n": len(probe_regions),
                    "matched": match, "probe_status": pstatus}

    cells = _build_cells(stem, ours_regions, wir_regions)
    measure_ticks = _measure_ticks(ours_regions)
    is_transposed, tr_off, tr_frac, tr_n = _piece_transposition(ours_regions, wir_regions)

    # a8 reconciliation aggregate (per-verdict scored duration)
    verd_dur = Counter()
    for c in cells:
        verd_dur[c["verdict"]] += c["w"]

    runs = _classify_one(stem, cells, wir_regions, ours_regions, menus, measure_ticks)
    return (stem, "OK", {
        "verd_dur": dict(verd_dur),
        "runs": runs,
        "stream_stats": stream_stats,
        "measure_ticks": measure_ticks,
        "transposed": is_transposed, "tr_offset": tr_off, "tr_frac": tr_frac, "tr_n": tr_n,
    })


def _summarize(preset, results, a8_ref):
    verd = Counter()
    stream = {"frozen_n": 0, "probe_n": 0, "matched": 0, "probe_failed": 0}
    cause_dur_g = Counter(); cause_n_g = Counter()      # global-anchored (doc-literal)
    cause_dur_l = Counter(); cause_n_l = Counter()      # local-anchored (diagnostic)
    rel_local_dur = Counter()                           # our-key relationship to LOCAL
    rel_global_dur = Counter()                          # our-key relationship to GLOBAL
    # cross-cutting
    carried_dur = 0; absent_dur = 0; menu_unavail_dur = 0
    # leading-tone (both anchorings)
    ltg = {"dur_tot": 0, "dur_pres": 0, "n_tot": 0, "n_pres": 0}
    ltl = {"dur_tot": 0, "dur_pres": 0, "n_tot": 0, "n_pres": 0}
    # unclassified (local-anchored) characterization by our-to-local relationship
    uncl_local_by_rel = Counter()
    per_cause_examples = defaultdict(list)              # keyed by local-anchored cause
    absent_runs = []                                    # G absent from menu (desk-sim seed)
    # corpus-integrity: transposition-mismatched pieces (#9/#19)
    transposed_pieces = []                              # (stem, offset, frac, scored, fail)
    tr_fail_dur = 0
    # clean-corpus companion (excluding transposed pieces)
    clean_cause_dur_l = Counter(); clean_cause_n_l = Counter()
    clean_rel_local_dur = Counter()
    clean_failing_mass = 0
    clean_scored = 0
    cltl = {"dur_tot": 0, "dur_pres": 0, "n_tot": 0, "n_pres": 0}   # clean leading-tone (local)

    for stem, status, data in results:
        if status != "OK":
            continue
        verd.update(data["verd_dur"])
        ss = data["stream_stats"]
        stream["frozen_n"] += ss["frozen_n"]; stream["probe_n"] += ss["probe_n"]
        stream["matched"] += ss["matched"]
        if ss["probe_status"] != "OK":
            stream["probe_failed"] += 1
        piece_scored = sum(data["verd_dur"].values())
        piece_fail = (data["verd_dur"].get("disagree", 0) + data["verd_dur"].get("keyfail", 0)
                      + data["verd_dur"].get("dcml_keyfail", 0))
        is_tr = data.get("transposed", False)
        if is_tr:
            transposed_pieces.append({"stem": stem, "offset": data["tr_offset"],
                                      "frac": data["tr_frac"], "scored": piece_scored,
                                      "fail": piece_fail})
            tr_fail_dur += piece_fail
        else:
            clean_scored += piece_scored
        for run in data["runs"]:
            cg, cl = run["cause_global"], run["cause_local"]
            cause_dur_g[cg] += run["dur"]; cause_n_g[cg] += 1
            cause_dur_l[cl] += run["dur"]; cause_n_l[cl] += 1
            if not is_tr:
                clean_cause_dur_l[cl] += run["dur"]; clean_cause_n_l[cl] += 1
                clean_failing_mass += run["dur"]        # ALL failing runs (incl. keyfail)
                if run["verdict"] not in ("keyfail", "dcml_keyfail"):
                    clean_rel_local_dur[run["rel_to_local"]] += run["dur"]
                    if run["lt_l_appl"]:
                        cltl["dur_tot"] += run["dur"]; cltl["n_tot"] += 1
                        if run["lt_l_present"]:
                            cltl["dur_pres"] += run["dur"]; cltl["n_pres"] += 1
            if run["verdict"] in ("keyfail", "dcml_keyfail"):
                continue
            rel_local_dur[run["rel_to_local"]] += run["dur"]
            rel_global_dur[run["rel_to_global"]] += run["dur"]
            if run["menu_available"]:
                if run["g_carried"]:
                    carried_dur += run["dur"]
                else:
                    absent_dur += run["dur"]
                    absent_runs.append(run)
            else:
                menu_unavail_dur += run["dur"]
            if run["lt_g_appl"]:
                ltg["dur_tot"] += run["dur"]; ltg["n_tot"] += 1
                if run["lt_g_present"]:
                    ltg["dur_pres"] += run["dur"]; ltg["n_pres"] += 1
            if run["lt_l_appl"]:
                ltl["dur_tot"] += run["dur"]; ltl["n_tot"] += 1
                if run["lt_l_present"]:
                    ltl["dur_pres"] += run["dur"]; ltl["n_pres"] += 1
            if cl == "unclassified":
                uncl_local_by_rel[run["rel_to_local"]] += run["dur"]
            if len(per_cause_examples[cl]) < 10:
                per_cause_examples[cl].append(
                    {"stem": run["stem"], "start": run["start"], "dur": run["dur"],
                     "our_key": run["our_key"], "g_key": run["g_key"], "l_key": run["l_key"],
                     "rel_to_local": run["rel_to_local"], "rel_to_global": run["rel_to_global"]})

    scored = sum(verd.values())
    failing_mass = verd.get("disagree", 0) + verd.get("keyfail", 0) + verd.get("dcml_keyfail", 0)
    recon = {
        "my_agree": verd.get("agree", 0), "a8_agree": a8_ref["b_key_agree"],
        "my_disagree": verd.get("disagree", 0), "a8_disagree": a8_ref["b_key_dis"],
        "my_keyfail": verd.get("keyfail", 0), "a8_keyfail": a8_ref["b_key_fail"],
        "my_dcml_keyfail": verd.get("dcml_keyfail", 0), "a8_dcml_keyfail": a8_ref["b_dcml_keyfail"],
        "my_scored": scored, "a8_scored": a8_ref["scored_dur"],
        "agree_ok": verd.get("agree", 0) == a8_ref["b_key_agree"],
        "disagree_ok": verd.get("disagree", 0) == a8_ref["b_key_dis"],
        "keyfail_ok": verd.get("keyfail", 0) == a8_ref["b_key_fail"],
        "scored_ok": scored == a8_ref["scored_dur"],
        "classified_global_total": sum(cause_dur_g.values()),
        "classified_local_total": sum(cause_dur_l.values()),
        "failing_mass": failing_mass,
    }
    recon["classified_eq_failing_global"] = (sum(cause_dur_g.values()) == failing_mass)
    recon["classified_eq_failing_local"] = (sum(cause_dur_l.values()) == failing_mass)

    def share(d):
        return round(100.0 * d / failing_mass, 2) if failing_mass else 0.0

    def table(cd, cn):
        return {c: {"dur": cd.get(c, 0), "n": cn.get(c, 0),
                    "share_of_failing_pct": share(cd.get(c, 0))} for c in CAUSES}

    def lt_block(x):
        return {"n_runs": x["n_tot"], "n_runs_lt_present": x["n_pres"],
                "dur_total": x["dur_tot"], "dur_lt_present": x["dur_pres"],
                "lt_present_frac_dur": round(x["dur_pres"] / x["dur_tot"], 4) if x["dur_tot"] else None,
                "lt_present_frac_n": round(x["n_pres"] / x["n_tot"], 4) if x["n_tot"] else None}

    def cshare(d, denom):
        return round(100.0 * d / denom, 2) if denom else 0.0

    clean_table = {c: {"dur": clean_cause_dur_l.get(c, 0), "n": clean_cause_n_l.get(c, 0),
                       "share_of_clean_failing_pct": cshare(clean_cause_dur_l.get(c, 0), clean_failing_mass)}
                   for c in CAUSES}

    return {
        "scored_dur": scored,
        "failing_mass_dur": failing_mass,
        "failing_share_of_scored_pct": round(100.0 * failing_mass / scored, 4) if scored else 0.0,
        "key_agree_pct_vs_global": round(100.0 * verd.get("agree", 0) / scored, 4) if scored else 0.0,
        "reconciliation": recon,
        "region_stream_match": {
            "frozen_regions": stream["frozen_n"], "probe_regions": stream["probe_n"],
            "matched_start_end_key": stream["matched"],
            "match_frac": round(stream["matched"] / stream["frozen_n"], 4) if stream["frozen_n"] else None,
            "scores_probe_failed": stream["probe_failed"],
        },
        "cause_table_local_anchored": table(cause_dur_l, cause_n_l),
        "cause_table_global_anchored": table(cause_dur_g, cause_n_g),
        "transposition_contamination": {
            "note": ("pieces whose SCORE is transposed vs the WiR reference edition "
                     "(constant whole-piece root offset >= %.0f%% coverage): ~100%% key- AND "
                     "root-disagree by construction, NOT key-inference error (#9/#19). "
                     "Included in the a8-reconciling tables; excluded in the clean-corpus view."
                     % (100 * TRANSPOSE_FRAC)),
            "n_transposed_pieces": len(transposed_pieces),
            "transposed_pieces": sorted(transposed_pieces, key=lambda p: -p["fail"]),
            "transposed_failing_dur": tr_fail_dur,
            "transposed_share_of_failing_pct": share(tr_fail_dur),
            "clean_failing_mass_dur": clean_failing_mass,
            "clean_scored_dur": clean_scored,
            "clean_key_agree_pct_vs_global": round(100.0 * (clean_scored - clean_failing_mass) / clean_scored, 4) if clean_scored else None,
        },
        "cause_table_local_anchored_clean_corpus": clean_table,
        "our_key_relationship_to_local_key_clean_corpus": {
            k: {"dur": v, "share_of_clean_failing_pct": cshare(v, clean_failing_mass)}
            for k, v in clean_rel_local_dur.items()},
        "leading_tone_test_local_anchored_clean_corpus": lt_block(cltl),
        "our_key_relationship_to_local_key": {k: {"dur": v, "share_of_failing_pct": share(v)}
                                              for k, v in rel_local_dur.items()},
        "our_key_relationship_to_global_key": {k: {"dur": v, "share_of_failing_pct": share(v)}
                                               for k, v in rel_global_dur.items()},
        "unclassified_local_by_our_to_local_rel": {k: {"dur": v, "share_of_failing_pct": share(v)}
                                                   for k, v in uncl_local_by_rel.items()},
        "present_but_outranked": {
            "carried_dur": carried_dur, "absent_dur": absent_dur,
            "menu_unavailable_dur": menu_unavail_dur,
            "carried_share_of_failing_pct": share(carried_dur),
            "absent_share_of_failing_pct": share(absent_dur),
            "menu_unavailable_share_pct": share(menu_unavail_dur),
        },
        "leading_tone_test_global_anchored": lt_block(ltg),
        "leading_tone_test_local_anchored": lt_block(ltl),
        "examples_per_local_cause": {k: v for k, v in per_cause_examples.items()},
        "absent_from_menu_runs": [
            {"stem": r["stem"], "start": r["start"], "dur": r["dur"], "our_key": r["our_key"],
             "g_key": r["g_key"], "l_key": r["l_key"], "cause_local": r["cause_local"],
             "rel_to_local": r["rel_to_local"], "rel_to_global": r["rel_to_global"]}
            for r in sorted(absent_runs, key=lambda r: -r["dur"])[:60]],
    }


def _load_a8_ref(a8_summary_path):
    d = json.loads(Path(a8_summary_path).read_text())
    ref = {}
    for p in PRESETS:
        a = d[PRESET_DIR[p]]["agg"]
        ref[p] = {"b_key_agree": a["b_key_agree"], "b_key_dis": a["b_key_dis"],
                  "b_key_fail": a["b_key_fail"], "b_dcml_keyfail": a["b_dcml_keyfail"],
                  "scored_dur": a["scored_dur"]}
    return ref


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-analyze", metavar="PATH")
    ap.add_argument("--corpus-dir", default="tools/corpus")
    ap.add_argument("--a8-summary", required=True,
                    help="Path to a8_rebaseline_measure.py summary.json (the reconciliation reference).")
    ap.add_argument("--out", metavar="FILE", required=True)
    ap.add_argument("--presets", default=",".join(PRESETS))
    args = ap.parse_args()

    exe = rbp._find_batch_analyze(args.batch_analyze)
    if exe is None:
        print("ERROR: batch_analyze not found", file=sys.stderr)
        sys.exit(1)
    print(f"Using batch_analyze: {exe}")
    a8_ref = _load_a8_ref(args.a8_summary)

    corpus_dir = Path(args.corpus_dir)
    xml_files = sorted(f for f in corpus_dir.glob("*.xml") if not f.stem.endswith("_m21"))
    if not xml_files:
        print(f"ERROR: no .xml in {corpus_dir}", file=sys.stderr)
        sys.exit(1)
    print(f"Corpus: {len(xml_files)} scores")
    presets = [p.strip() for p in args.presets.split(",") if p.strip()]

    report = {
        "git_hash": rbp._get_git_hash(),
        "corpus_git_hash": None,
        "n_scores": len(xml_files),
        "measure_edge_rule": "run.dur < median inter-measure tick gap (per piece)",
        "presets": {},
    }
    mp = corpus_dir / "baroque" / "corpus_manifest.json"
    if mp.exists():
        report["corpus_git_hash"] = json.loads(mp.read_text())["git_hash"]

    workers = min(multiprocessing.cpu_count(), len(xml_files))
    with tempfile.TemporaryDirectory() as scratch:
        for preset in presets:
            print(f"\n=== preset {preset} ===")
            work = [(exe, xml, preset, scratch) for xml in xml_files]
            results = []
            done = 0
            with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
                futs = {pool.submit(_collect_one, w): w[1].stem for w in work}
                for fut in concurrent.futures.as_completed(futs):
                    results.append(fut.result())
                    done += 1
                    if done % 50 == 0:
                        print(f"  {done}/{len(work)} ...")
            summ = _summarize(preset, results, a8_ref[preset])
            report["presets"][preset] = summ
            rc = summ["reconciliation"]
            print(f"  RECONCILE: agree_ok={rc['agree_ok']} disagree_ok={rc['disagree_ok']} "
                  f"keyfail_ok={rc['keyfail_ok']} scored_ok={rc['scored_ok']} "
                  f"class==fail global={rc['classified_eq_failing_global']} local={rc['classified_eq_failing_local']}")
            print(f"    my_disagree={rc['my_disagree']} a8_disagree={rc['a8_disagree']}  "
                  f"my_keyfail={rc['my_keyfail']} a8_keyfail={rc['a8_keyfail']}")
            print(f"  key_agree(vs global)={summ['key_agree_pct_vs_global']}%  "
                  f"failing_mass={summ['failing_mass_dur']} ({summ['failing_share_of_scored_pct']}% of scored)")
            print(f"  region-stream match: {summ['region_stream_match']['matched_start_end_key']}"
                  f"/{summ['region_stream_match']['frozen_regions']} "
                  f"({summ['region_stream_match']['match_frac']}); probe_failed_scores="
                  f"{summ['region_stream_match']['scores_probe_failed']}")
            print("  CAUSE SHARES — local-anchored (true key = LOCAL, diagnostic):")
            for c in CAUSES:
                ct = summ["cause_table_local_anchored"][c]
                print(f"    {c:<28} {ct['share_of_failing_pct']:>6}%  (dur {ct['dur']}, n {ct['n']})")
            print("  CAUSE SHARES — global-anchored (true key = GLOBAL, doc-literal):")
            for c in CAUSES:
                ct = summ["cause_table_global_anchored"][c]
                print(f"    {c:<28} {ct['share_of_failing_pct']:>6}%  (dur {ct['dur']}, n {ct['n']})")
            print("  our-key relationship to LOCAL key:")
            for k, v in sorted(summ["our_key_relationship_to_local_key"].items(),
                               key=lambda kv: -kv[1]["dur"]):
                print(f"    {k:<26} {v['share_of_failing_pct']:>6}%  (dur {v['dur']})")
            po = summ["present_but_outranked"]
            print(f"  present-but-outranked: carried={po['carried_share_of_failing_pct']}%  "
                  f"absent={po['absent_share_of_failing_pct']}%  "
                  f"menu_unavail={po['menu_unavailable_share_pct']}%")
            ltg = summ["leading_tone_test_global_anchored"]
            ltl = summ["leading_tone_test_local_anchored"]
            print(f"  leading-tone GLOBAL-anchored relative-minor runs: present "
                  f"{ltg['lt_present_frac_dur']} of dur ({ltg['dur_lt_present']}/{ltg['dur_total']})")
            print(f"  leading-tone LOCAL-anchored relative-minor runs: present "
                  f"{ltl['lt_present_frac_dur']} of dur ({ltl['dur_lt_present']}/{ltl['dur_total']})")
            tc = summ["transposition_contamination"]
            print(f"  ★ TRANSPOSITION-mismatched pieces (score transposed vs WiR): "
                  f"{tc['n_transposed_pieces']} pieces = {tc['transposed_share_of_failing_pct']}% of failing mass")
            print(f"    clean-corpus key-agree(vs global) = {tc['clean_key_agree_pct_vs_global']}% "
                  f"(vs {summ['key_agree_pct_vs_global']}% with them included)")
            cltl = summ["leading_tone_test_local_anchored_clean_corpus"]
            print(f"    clean-corpus leading-tone LOCAL relative-minor present: {cltl['lt_present_frac_dur']}")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nReport -> {args.out}")


if __name__ == "__main__":
    main()
