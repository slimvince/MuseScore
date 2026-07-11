#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# gen_blind_rerun_sample.py — draw AND record the two row samples for the
# FULLY-BLIND re-run of the L1/L2 certification audit (EG-7 / OI-84 / OI-89).
#
# Why this script exists (distinct from tools/audit/gen_pass2_sample.py): the
# earlier pass-2 second reading was only PARTIALLY blind — the instruction it
# followed made it read STATUS.md, which carried pass 1's headline verdict. The
# user withheld certification of layers 1 and 2 until an independent reading that
# never saw any prior conclusion. This script draws two NEW samples with NEW fixed
# seeds (both different from pass 2's 20260711), and the auditor's own from-scratch
# verdicts are embedded below (READING_VERDICTS / ERRORRATE_VERDICTS) so the two
# committed artifacts regenerate byte-identically from this one script.
#
# Two samples, two new fixed recorded seeds:
#   (1) READING sample (protocol P5 / instruction Task 1): >= 110 rows, stratified
#       over the FIVE row kinds (function, literal, field, branch, crosslayer) in
#       proportion to their counts, every L1/L2 file represented. The independent
#       second reading. seed = SEED_READING.
#   (2) ERROR-RATE sample (protocol P6 / instruction Task 1): 40 rows, uniform over
#       the FULL disposition domain (all six inventory kinds PLUS the file rows).
#       Judged blind too (verdict recorded first; pass-1 comparison is Task 2).
#       seed = SEED_ERROR.
#
# The domain is rebuilt from the NON-VERDICT inventory files only (file_table.csv +
# l1l2_*.csv) — running this reads none of pass 1's dispositions and cannot leak
# them. Load order is identical to gen_pass2_sample.py's load_rows(), so the global
# row index (the row_id tail) aligns row-for-row with pass 1's 688-row domain.
#
# Determinism: every input list is sorted by a stable key before sampling; the draw
# depends only on the seed and the frozen inventory, not filesystem order.

import copy
import csv
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1L2 = os.path.join(HERE, "l1l2")

SEED_READING = 20260712      # Task 1 fully-blind second reading (NEW; != pass-2's 20260711)
SEED_ERROR   = 20260713      # Task 1 fully-blind error-rate sample (NEW; != pass-2's 424242)
READING_TARGET = 110         # proportional base target (coverage top-ups may add a few)
ERROR_N = 40                 # error-rate sample size (matches the pass-2 design)

# The five row kinds the reading sample is stratified over (Task 1, point 1).
READING_KINDS = ["function", "literal", "field", "branch", "crosslayer"]


def _read_csv(name):
    path = os.path.join(L1L2, name)
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def load_rows():
    """Rebuild the full disposition domain from the non-verdict inventory files.

    Load order MATCHES gen_pass2_sample.py exactly (file, function, literal, field,
    branch, decl, crosslayer), so the global index in each row_id lines up with
    pass 1's domain for row-for-row comparison in Task 2.
    """
    rows = []

    def add(kind, file, line, label, extra=None):
        rid = "{}|{}|{}|{}".format(kind, file, line, len(rows))
        r = {"row_id": rid, "kind": kind, "file": file, "line": str(line),
             "label": label}
        if extra:
            r.update(extra)
        rows.append(r)

    for r in _read_csv("file_table.csv"):
        add("file", r["file"], "", r.get("tag", ""),
            {"tag": r.get("tag", ""), "reason": r.get("reason", "")})

    for r in _read_csv("l1l2_functions.csv"):
        add("function", r["file"], r["start_line"],
            "{}()".format(r["name"]),
            {"name": r["name"], "end_line": r.get("end_line", "")})

    for r in _read_csv("l1l2_literals.csv"):
        add("literal", r["file"], r["line"],
            "{} in {}".format(r["value"], r.get("func", "")),
            {"value": r["value"], "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l1l2_fields.csv"):
        add("field", r["file"], r["line"],
            "{}::{}".format(r.get("type_owner", ""), r["name"]),
            {"type_owner": r.get("type_owner", ""), "field_type": r.get("field_type", ""),
             "name": r["name"], "context": r.get("context", "")})

    for r in _read_csv("l1l2_branches.csv"):
        add("branch", r["file"], r["line"],
            "{} in {}".format(r.get("kind", ""), r.get("func", "")),
            {"branch_kind": r.get("kind", ""), "func": r.get("func", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l1l2_decls.csv"):
        add("decl", r["file"], r["line"],
            "{}".format(r.get("name", "")),
            {"type_owner": r.get("type_owner", ""), "name": r.get("name", ""),
             "context": r.get("context", "")})

    for r in _read_csv("l1l2_crosslayer.csv"):
        add("crosslayer", r["file"], r["line"],
            "include {} -> {}".format(r.get("include", ""), r.get("target_area", "")),
            {"include": r.get("include", ""), "resolved": r.get("resolved", ""),
             "target_area": r.get("target_area", "")})

    return rows


def stable_key(r):
    line = r["line"]
    lnum = int(line) if line.isdigit() else -1
    return (r["kind"], r["file"], lnum, r["row_id"])


def largest_remainder(counts, target):
    total = sum(counts.values())
    raw = {k: target * c / total for k, c in counts.items()}
    floor = {k: int(v) for k, v in raw.items()}
    used = sum(floor.values())
    rem = sorted(counts.keys(), key=lambda k: raw[k] - floor[k], reverse=True)
    i = 0
    while used < target:
        floor[rem[i % len(rem)]] += 1
        used += 1
        i += 1
    return floor


def l1l2_files(rows):
    out = set()
    for r in rows:
        if r["kind"] == "file" and r.get("tag") in ("L1", "L2"):
            out.add(r["file"])
    return out


def draw_reading(rows):
    pool = [r for r in rows if r["kind"] in READING_KINDS]
    by_kind = {k: sorted([r for r in pool if r["kind"] == k], key=stable_key)
               for k in READING_KINDS}
    counts = {k: len(v) for k, v in by_kind.items()}
    alloc = largest_remainder(counts, READING_TARGET)

    rng = random.Random(SEED_READING)
    selected = {}
    for k in READING_KINDS:
        picks = rng.sample(by_kind[k], alloc[k])
        for r in picks:
            selected[r["row_id"]] = r

    covered_files = {selected[i]["file"] for i in selected}
    need = l1l2_files(rows)
    topups = []
    for f in sorted(need - covered_files):
        cand = sorted([r for r in pool if r["file"] == f and r["row_id"] not in selected],
                      key=stable_key)
        if not cand:
            cand = sorted([r for r in rows if r["file"] == f and r["row_id"] not in selected],
                          key=stable_key)
        if cand:
            pick = rng.choice(cand)
            selected[pick["row_id"]] = pick
            topups.append(pick["row_id"])

    ordered = [copy.deepcopy(selected[i]) for i in selected]
    rng.shuffle(ordered)
    for i, r in enumerate(ordered):
        r["process_order"] = i + 1

    meta = {
        "seed": SEED_READING,
        "target_base": READING_TARGET,
        "kind_counts": counts,
        "kind_allocation": alloc,
        "coverage_topups": topups,
        "n_selected": len(ordered),
        "l1l2_files": sorted(need),
        "files_covered": sorted({r["file"] for r in ordered}),
    }
    return ordered, meta


def draw_error(rows):
    pool = sorted(rows, key=stable_key)
    rng = random.Random(SEED_ERROR)
    picks = rng.sample(pool, ERROR_N)
    picks_sorted = [copy.deepcopy(r) for r in sorted(picks, key=stable_key)]
    for i, r in enumerate(picks_sorted):
        r["process_order"] = i + 1
    meta = {
        "seed": SEED_ERROR,
        "n": ERROR_N,
        "domain_size": len(pool),
        "kind_breakdown": {k: sum(1 for r in picks if r["kind"] == k)
                           for k in sorted({r["kind"] for r in picks})},
    }
    return picks_sorted, meta


# ── The auditor's from-scratch verdicts (Task 1, point 2) ─────────────────────
# Filled in by hand at the code, BLIND to every prior pass. Keyed by the stable
# process_order the draw assigned (1..N per sample). Each value = (verdict, flag,
# reason).
# Verdict vocabulary = cowork_audit_protocol.md P2 (kind-appropriate):
#   code (function/branch): SURVIVES / RETIRES
#   constant (literal):     ESTABLISHED / UNFIT / DEAD
#   field (derived fact/struct field): PUBLISHED / SILOED / TRAPPED / DUPLICATED
#   crosslayer (include):   SURVIVES (layer-adheres) / RETIRES (back-edge)
#   file:                   the tag verdict (L1 / L2 / L3+ / RETIRES) confirmed or not
#   decl:                   SURVIVES / RETIRES (declaration matches a live definition)
# flag = "issue" (a defect/finding worth attention) or "clean" (no issue).
READING_VERDICTS = {
    1:  ("SURVIVES", "clean", "weightedPcView forward-onset: `if (ne->pitch < a.lowestPitch)` tracks the pc's lowest pitch+tpc for bass selection — correct."),
    2:  ("SURVIVES", "clean", "collectVoiceLines `if (!isEligible(n))` — reads L1 plays&&visible&&staffEligible flags, does not re-decide eligibility. Layer-2/1.5 correct."),
    3:  ("PUBLISHED", "clean", "PhraseBoundaryParams::minSilenceTicks=240 — precision-phase config field consumed by collectMarkerTicks all-rest-span guard; dormant primitive, dormancy declared."),
    4:  ("SURVIVES", "clean", "regionMetricWeightForBeatType `case SIMPLE_STRESSED:` falls through to 0.85 — correct beat-weight mapping."),
    5:  ("SURVIVES", "clean", "detectBassMovementSubBoundaries `if (cr->tick()!=segTick)` skips notes not onsetting at the segment tick — correct onset-only scan."),
    6:  ("SURVIVES", "clean", "slicer.cpp self-include of slicer.h — external/self, layer-adherent."),
    7:  ("SURVIVES", "clean", "isChordTrackStaff() — inline predicate re-implemented in the bridge to avoid a notation-layer include (documented); consumed by staffIsEligible. Correct."),
    8:  ("SURVIVES", "clean", "weightedPcView dense-start `if (!passes(*ne) || ne->onset>=startTickInt)` — filters to sustained-in eligible notes. Correct."),
    9:  ("SURVIVES", "clean", "collectVoiceLines `if (!ev.empty() && ev.back().onset==n.onset)` — collapses same-onset chord notes into one monophonic line event. Correct."),
    10: ("SURVIVES", "clean", "NoteQueryIndex::collect `if (nodeHi-nodeLo==1)` — segment-tree leaf detection; qualifies unconditionally per the two prior guards. Correct."),
    11: ("ESTABLISHED", "clean", "0.0 in `if (params.coincidenceWeight > 0.0)` — guard to apply coincidence weighting only when enabled. Correct."),
    12: ("SURVIVES", "clean", "weightedPcView ternary `fs ? metricWeight : bwAtRegionStart` — fallback beat weight when no ChordRest segment. Correct."),
    13: ("PUBLISHED", "clean", "SpanSpelling::flatCount — published field of the spanSpelling aggregate; consumer dormant (Phase B key-spelling term), dormancy declared."),
    14: ("SURVIVES", "clean", "phraseBoundaryTicks() — consumer-facing owned API = computePhraseBoundaryProfile(score).pickedTicks; consumers dormant/gated-off (declared)."),
    15: ("SURVIVES", "clean", "findTemporalContext `if (currentBassPc!=-1 && nextBassPc!=-1)` — computes bassIsStepwiseToNext only when both known. Correct."),
    16: ("SURVIVES", "clean", "weightedPcView main-loop `if (!passes(*ne))` — the view keep/drop filter (staffEligible,plays,visible,!grace,!excluded). Correct."),
    17: ("SURVIVES", "clean", "isChordTrackStaff `if (si >= sc->nstaves())` — out-of-range staff guard. Correct."),
    18: ("ESTABLISHED", "clean", "0.7 DECAY_RATE — documented per-measure decay multiplier; the design constant, single-owned here."),
    19: ("SURVIVES", "clean", "regiontonecollector.cpp self-include of regiontonecollector.h — external/self, layer-adherent."),
    20: ("SURVIVES", "clean", "findTemporalContext() — bridge temporal-context builder; legitimately CALLS L4 chord analyzer (analyzeChord/applyPostScoringGates) to cold-analyze neighbours. Intrinsic bridge->L4 dependency (relevant to owning-layer review), not a defect in isolation."),
    21: ("ESTABLISHED", "clean", "0.0 in `double sum=0.0, sumSq=0.0` — pickPeaks accumulator init. Correct."),
    22: ("SURVIVES", "clean", "weightedPcView `if (excludeLookAhead && ne->onset>startTickInt)` — dense-start look-ahead exclusion. Correct (reproduces legacy)."),
    23: ("SURVIVES", "clean", "spanSpelling `if (agg.count > 0)` — guards the centroid division against count==0. Correct."),
    24: ("SURVIVES", "clean", "detectBassMovementSubBoundaries `if (!firstSeg)` — null first-segment guard. Correct."),
    25: ("PUBLISHED", "clean", "SpanWindowWeights::decayRate=0.7 — settings-struct default the L3 decoder caller overrides; documented value-mirror of scoreharvest DECAY_RATE (in-line comment, not silent). Note: literal mirror, drift-risk if DECAY_RATE moves, but declared."),
    26: ("SURVIVES", "clean", "makeEvent() — builds NoteEvent (ppitch, tpc, tie-resolved duration via playTicksFraction, flags). Core L1, correct."),
    27: ("SURVIVES", "clean", "scoreEnd() — accessor returning m_scoreEnd. Correct."),
    28: ("ESTABLISHED", "clean", "1.5 spikeCeilingFactor — precision-phase default (>1 so a marker strictly exceeds the max surface strength). Documented."),
    29: ("SURVIVES", "clean", "phraseboundaryview.cpp include engraving/dom/staff.h — external DOM (downward); Staff used via score->staff(0)->keySigEvent. Layer-adherent."),
    30: ("SURVIVES", "clean", "note_model.cpp include engraving/dom/staff.h — external DOM (downward). Legitimate L1->engraving substrate; not an upward back-edge."),
    31: ("SURVIVES", "clean", "detectOnsetSubBoundaries ternary `(uniCount>0) ? jaccard : 0.0` — div-by-zero guard. Correct."),
    32: ("ESTABLISHED", "clean", "0.0 coincidenceWeight default — plain per-voice sum (feature off by default). Correct."),
    33: ("SURVIVES", "clean", "maxNormalizeInPlace `if (mx <= 0.0)` — all-zero/empty leaves profile unchanged. Correct."),
    34: ("SURVIVES", "clean", "pickPeaks() — local-maximum + (mean + k*SD) threshold peak-picking. Matches design §4.4. Correct."),
    35: ("ESTABLISHED", "clean", "2 in `minGapTicks = 2 * DIVISION` (detectBassMovementSubBoundaries default) — 2 quarter-notes min gap. Documented."),
    36: ("ESTABLISHED", "clean", "0.75 in `if (!s0) return 0.75` — fallback beat weight (unstressed) when the region-start segment is null. Correct."),
    37: ("SURVIVES", "clean", "beatTypeToWeight `case SIMPLE_UNSTRESSED:` returns prefs.beatWeightSimpleUnstressed. Correct."),
    38: ("SURVIVES", "clean", "detectOnsetSubBoundaries `if (excludeStaves.count(si) || !staffIsEligible(...))` — eligibility filter. Correct."),
    39: ("SURVIVES", "clean", "regionMetricWeightForBeatType `case SIMPLE_UNSTRESSED:` falls through to 0.75. Correct."),
    40: ("SURVIVES", "clean", "detectOnsetSubBoundaries `if (bits != 0)` — record only non-empty onset windows. Correct."),
    41: ("SURVIVES", "clean", "beatTypeForOnsetTick `if (num<=0 || den<=0)` — invalid time-signature guard, returns SUBBEAT. Correct."),
    42: ("SURVIVES", "clean", "regiontonecollector.h include types/analysistypes.h — leaf value-types header (the intended way to get value types without L3/L4 analyzer headers). Layer-adherent."),
    43: ("SURVIVES", "clean", "spellingview.cpp include engraving/dom/pitchspelling.h — external DOM; tpcIsValid/Tpc used. Layer-adherent."),
    44: ("SURVIVES", "clean", "NoteQueryIndex::build() — perfect-binary max-release segment tree over onset-sorted notes. Correct (padded leaves INT_MIN pruned)."),
    45: ("ESTABLISHED", "clean", "12 in `(bassPitch % 12)` — pitch-class modulus. Structural, correct."),
    46: ("SURVIVES", "clean", "findTemporalContext forward `if (!nextSounding.empty())` — analyze next chord only if notes sound. Correct."),
    47: ("SURVIVES", "clean", "findTemporalContext forward hasAttacks scan eligibility filter. Correct."),
    48: ("PUBLISHED", "clean", "VoiceBoundaryProfile::voice — published per-voice profile field; dormant primitive, dormancy declared."),
    49: ("ESTABLISHED", "clean", "0.0 in `if (a.totalWeight == 0.0) continue` — skip empty pitch classes in tone emission. Correct."),
    50: ("ESTABLISHED", "clean", "0.0 lofCentroid default — 0 when count==0 (documented invariant). Correct."),
    51: ("ESTABLISHED", "clean", "12 in Pass-2 `for (int pc=0; pc<12; ++pc)` — 12 pitch classes. Correct."),
    52: ("ESTABLISHED", "clean", "1.5 in `a.totalWeight *= 1.5` — Pass-3 cross-voice boost; documented legacy coefficient."),
    53: ("PUBLISHED", "clean", "NoteEvent::release — core published L1 fact (tie-resolved release tick); consumed by slicer, views, index. PUBLISHED."),
    54: ("SURVIVES", "clean", "safeBeatType() — null/invalid-timesig-safe BeatType; falls back to SUBBEAT. Correct."),
    55: ("SURVIVES", "clean", "detectBassMovementSubBoundaries eligibility filter `if (excludeStaves.count(si) || !staffIsEligible(...))`. Correct."),
    56: ("SURVIVES", "clean", "rebuildForLoadedSpan `if (!sc)` — null-score path builds an empty index. Correct."),
    57: ("SURVIVES", "clean", "spanSpelling `else if (lof < 0)` — flat-side count branch. Correct."),
    58: ("ESTABLISHED", "clean", "2 in `collect(2*node+1, ...)` — segment-tree right-child index. Structural, correct."),
    59: ("ESTABLISHED", "clean", "0.0 in `if (accum[pc].totalWeight > 0.0 && ...)` — bass-fallback loop (any weighted pc). Correct."),
    60: ("SURVIVES", "clean", "beatWeightForOnsetTick() — anon-namespace prefs-weighted wrapper over the shared indexed beatTypeForOnsetTick. Correct (single tick->beat-type source)."),
    61: ("SURVIVES", "clean", "spellingview.cpp self-include of spellingview.h — external/self. Layer-adherent."),
    62: ("PUBLISHED", "clean", "VoiceBoundaryProfile::strength — published per-onset surface strength; dormant primitive, dormancy declared."),
    63: ("SURVIVES", "clean", "beatTypeToWeight `case SUBBEAT:` returns prefs.beatWeightSubbeat. Correct."),
    64: ("SURVIVES", "issue", "regiontonecollector.cpp:37 includes composing/analysis/chord/analysisutils.h (an L1.5->L4 edge) but uses NONE of its 6 exported symbols (endsWith/ionianTonicPcFromFifths/normalizePc/pcInMask/diatonicMaskFromFifths/collectionMask) — verified by grep. Candidate unnecessary cross-layer include (removability needs a build-confirm; regiontoneprimitives.cpp is the sibling that actually uses chord utils). Include hygiene / minor layer back-edge, not a correctness defect."),
    65: ("SURVIVES", "clean", "soundingAt `if (!passes(*ne))` — point-in-time view filter. Correct."),
    66: ("SURVIVES", "clean", "scoreStart() — accessor returning m_scoreStart. Correct."),
    67: ("SURVIVES", "clean", "collectPitchContext `if (pp < lowestPitch)` — per-segment lowest-pitch (bass) tracking. Correct."),
    68: ("SURVIVES", "issue", "extend() impl is correct (single append-only step, clamps at score bounds, no-op guards). BUT its consumer docstring at note_model.h:161-163 says 'no layer calls it yet'; grep shows production call sites regionanalyzer.cpp:702, chordslicedecoder.cpp:1387/1393, textureclassifier.cpp:183/187 (gated off by default). The 'who consumes it?' question exposes a stale/inaccurate doc-sync claim (#10). Code SURVIVES; the docstring is wrong as worded."),
    69: ("PUBLISHED", "clean", "PhraseBoundaryProfile::textureStrength — published texture-strength output (parallel to textureTicks); dormant primitive, dormancy declared."),
    70: ("SURVIVES", "clean", "collectMarkerTicks `case Smorzando:` — member of the ritardando-family slowing-into-arrival list; spikes at spanner end. Correct."),
    71: ("SURVIVES", "clean", "note_model.cpp include engraving/dom/chord.h — external DOM; Chord/graceNotes used. Layer-adherent."),
    72: ("SURVIVES", "clean", "findTemporalContext backward `if (!hasAttacks) continue` — skip rest-only prior segments. Correct."),
    73: ("ESTABLISHED", "clean", "0.20 wPitch — precision-phase surface-cue weight (gap>ioi>pitch ordering). Documented default."),
    74: ("ESTABLISHED", "clean", "12 in Pass-3 pc loop. Correct."),
    75: ("SURVIVES", "clean", "buildPedalWindowIndex `if (pedalEndTick<=pedalStartTick || ... || pedalStartTick>=endTickInt)` — reject empty/out-of-window pedals. Correct."),
    76: ("ESTABLISHED", "clean", "1.0 in `laMul = lookahead ? weights.lookaheadWeight : 1.0` — non-lookahead multiplier. Correct."),
    77: ("SURVIVES", "clean", "beatTypeToWeight `case COMPOUND_STRESSED:`. Correct."),
    78: ("SURVIVES", "clean", "isChordTrackStaff `if (!part)` — null-part guard. Correct."),
    79: ("SURVIVES", "clean", "collectMarkerTicks `if (!firstMeasure)` — empty-score guard. Correct."),
    80: ("SURVIVES", "clean", "spanSpelling() — line-of-fifths centroid + sharp/flat/natural distribution; skips invalid tpc. Correct, single tpc interpreter."),
    81: ("SURVIVES", "clean", "detectOnsetSubBoundaries `if (onsets.size() < 2)` — need >=2 onset windows. Correct."),
    82: ("SURVIVES", "clean", "note_model.cpp include engraving/dom/score.h — external DOM; Score used. Layer-adherent."),
    83: ("SURVIVES", "clean", "weightedPcView dense-start `if (!backwardPc[ne->pitch % 12])` — distinct-pc sustaining-in count. Correct."),
    84: ("SURVIVES", "clean", "metricweights.h include engraving/types/constants.h — external types; Constants::DIVISION used. Layer-adherent."),
    85: ("ESTABLISHED", "clean", "0.0 in `if (totalWeight == 0.0) return {}` — empty-region guard. Correct."),
    86: ("SURVIVES", "clean", "weightedPcView ternary `(bassPitch < max) ? (bassPitch % 12) : -1` — bassPC or -1. Correct."),
    87: ("SURVIVES", "clean", "pitchContextOverSpan `else if (ne->onset >= anchorEnd)` — look-ahead distance classification. Correct."),
    88: ("SURVIVES", "clean", "collectMarkerTicks `if (!anyEligible)` — spike an all-eligible-voice-rest span at its onset. Correct."),
    89: ("SURVIVES", "clean", "pickPeaks `if (m == 0)` — empty-profile guard. Correct."),
    90: ("ESTABLISHED", "clean", "0.0 in PedalTailCandidate attackBeatWeight init. Correct."),
    91: ("PUBLISHED", "clean", "SpanSpelling::lofCentroid — published centroid field; consumer dormant (Phase B), dormancy declared."),
    92: ("SURVIVES", "clean", "collectMarkerTicks `if (score->nstaves()>0 && score->staff(0))` — prevailing-key init guard. Correct."),
    93: ("PUBLISHED", "clean", "VoiceBoundaryProfile::staff — published profile field; dormant primitive, dormancy declared."),
    94: ("SURVIVES", "clean", "regiontonecollector.cpp include engraving/dom/chord.h — external DOM; Chord used. Layer-adherent."),
    95: ("SURVIVES", "clean", "regiontoneprimitives.cpp include engraving/dom/chord.h — external DOM; toChord/Chord used. Layer-adherent."),
    96: ("SURVIVES", "clean", "collectPitchContext ternary `isLookahead ? LOOKAHEAD_WEIGHT : 1.0` — look-ahead weight. Correct."),
    97: ("SURVIVES", "clean", "regiontoneprimitives.cpp include engraving/dom/segment.h — external DOM; Segment used. Layer-adherent."),
    98: ("SURVIVES", "clean", "collectPitchContext() — LEGACY DOM-walk point-anchored pitch-context builder; documented as the live resolver's builder, coexisting with the indexed successor pitchContextOverSpan (declared dual-existence, retires with the L3 wiring). Correct."),
    99: ("SURVIVES", "clean", "weightedPcView `if (excludeLookAheadOnDenseStart)` — the dense-start exclusion block entry. Correct."),
    100: ("ESTABLISHED", "clean", "0.3 in `(1.0 + 0.3 * (distinct-1))` — Pass-2 repetition-boost coefficient; documented legacy value."),
    101: ("SURVIVES", "clean", "phraseboundaryview.cpp include engraving/dom/segment.h — external DOM; Segment used. Layer-adherent."),
    102: ("ESTABLISHED", "clean", "4 in `(startTick - Fraction(4,1)).ticks()` — 4-whole-note backward pedal-candidate window; documented legacy coverage."),
    103: ("PUBLISHED", "clean", "Slice::end — published L2 fact (exclusive upper bound); consumed by slice consumers. PUBLISHED."),
    104: ("SURVIVES", "clean", "collectMarkerTicks `else if (key != prevKey && tick > 0)` — mid-score key-signature CHANGE spike (engraved event, not inferred key). Correct."),
    105: ("ESTABLISHED", "clean", "0.0 in `double distBeats = 0.0` (pitchContextOverSpan). Correct."),
    106: ("SURVIVES", "clean", "regiontonecollector.h include engraving/dom/score.h — external DOM; Score used. Layer-adherent."),
    107: ("SURVIVES", "clean", "computePhraseBoundaryProfile normalizeAcrossVoices `if (mx <= 0.0)` — all-zero guard. Correct."),
    108: ("PUBLISHED", "clean", "NoteEvent::isGrace — published L1 annotation (kept-and-flagged, not dropped); consumed by the view filters. PUBLISHED."),
    109: ("ESTABLISHED", "clean", "0.0 in `double strength = 0.0` (texture-grid accumulation). Correct."),
    110: ("SURVIVES", "clean", "lineOfFifths `if (!tpcIsValid(tpc))` — the sole tpc presence test (returns kNoLineOfFifths); documented as NOT `>=0` to keep flat-side spellings. Correct."),
    111: ("SURVIVES", "clean", "beatTypeToWeight() — BeatType -> prefs weight switch; default returns prefs.beatWeightSubbeat. Correct."),
}
ERRORRATE_VERDICTS = {
    1:  ("SURVIVES", "clean", "computePhraseBoundaryProfile tau-cluster `if (rep==min || s.first-rep > tauTicks)` — start a new coincidence cluster. Correct."),
    2:  ("SURVIVES", "clean", "weightedPcView `if (!s0) return 0.75` — region-start beat-weight fallback. Correct."),
    3:  ("SURVIVES", "clean", "weightedPcView Pass-2 `if (a.totalWeight == 0.0) continue`. Correct."),
    4:  ("SURVIVES", "clean", "buildTones `if (sn.ppitch < lowestPpitch)` — lowest-pitch (bass) tracking. Correct."),
    5:  ("SURVIVES", "clean", "collectPitchContext ternary `isLookahead ? LOOKAHEAD_WEIGHT : 1.0`. Correct."),
    6:  ("SURVIVES", "clean", "findTemporalContext `if (currentBassPc!=-1 && previousBassPc!=-1)` — bassIsStepwiseFromPrevious. Correct."),
    7:  ("SURVIVES", "clean", "beatTypeToWeight `case SIMPLE_UNSTRESSED:`. Correct."),
    8:  ("SURVIVES", "clean", "regionMetricWeightForBeatType `case SIMPLE_UNSTRESSED:` -> 0.75. Correct."),
    9:  ("SURVIVES", "clean", "changePointSlices post-clip `if (boundaries.size() < 2) return slices` — degenerate single-tick loaded span -> empty partition. Correct (documented)."),
    10: ("SURVIVES", "clean", "phraseboundaryview.cpp include engraving/dom/gradualtempochange.h — external DOM; GradualTempoChange used. Layer-adherent."),
    11: ("SURVIVES", "clean", "regiontonecollector.cpp self-include of regiontonecollector.h — external/self. Layer-adherent."),
    12: ("SURVIVES", "clean", "metricweights.h include ../key/keymodeanalyzer.h — used for KeyModeAnalyzer::PitchContext / KeyModeAnalyzerPreferences (distinctPitchClasses, beatTypeToWeight). Intrinsic type dependency of the shared key-path helpers; a scoreharvest->key coupling worth an owning-layer note, but a real used include, not a dangling back-edge."),
    13: ("SURVIVES", "clean", "slicer.h include composing/analysis/notemodel/note_model.h — proper L2->L1 downward dependency. Layer-adherent."),
    14: ("SURVIVES", "clean", "regiontonecollector.h:87 `trackName` — this 'decl' inventory row is an extractor over-capture (a method-call token `instrument->trackName()`, not a declaration; manifest notes the extractor is over-capture-biased). The underlying isChordTrackStaff track-name check is correct."),
    15: ("SURVIVES", "clean", "note_model.h:215 `overlapping` decl — declares NoteModel::overlapping(t0,t1); matches the definition at note_model.cpp:307. Correct."),
    16: ("PUBLISHED", "clean", "VoiceBoundaryProfile::onsets — published per-voice onset vector; dormant primitive, dormancy declared."),
    17: ("PUBLISHED", "clean", "SpanSpelling::naturalCount — published field; consumer dormant (Phase B), dormancy declared. Invariant count==sharp+flat+natural."),
    18: ("PUBLISHED", "clean", "NoteEvent::release — core published L1 fact (same as reading-sample row 53). PUBLISHED."),
    19: ("L3+", "clean", "chordvoicing.cpp — chord/decode (L4); correctly deferred to the L4 audit, out of L1/L2 scope. Tag confirmed."),
    20: ("L3+", "clean", "decode/chordpathdecoder.h — L3 key-mode decoder scaffolding; correctly deferred to the L3 audit. Tag confirmed."),
    21: ("L3+", "clean", "function/functionmodulation.h — function (L5); correctly deferred to the L5 audit. Tag confirmed."),
    22: ("L3+", "clean", "function/functionprogression.h — function (L5); correctly deferred. Tag confirmed."),
    23: ("L3+", "clean", "function/functionresolver.h — function (L5); correctly deferred. Tag confirmed."),
    24: ("L3+", "clean", "tests/data/nm_slice_rest.mscx — test fixture data; out of L1/L2 source scope. Tag confirmed."),
    25: ("L3+", "clean", "tests/data/nm_two_staff.mscx — test fixture data; out of scope. Tag confirmed."),
    26: ("L3+", "clean", "tests/data/reachback_anchor.musicxml — test fixture data; out of scope. Tag confirmed."),
    27: ("L3+", "clean", "tests/data/s1c_unison_c.mscx — test fixture data; out of scope. Tag confirmed."),
    28: ("L3+", "clean", "tests/functionprogression_tests.cpp — test source; out of L1/L2 source scope. Tag confirmed."),
    29: ("L3+", "clean", "tests/grouping_tests.cpp — test source; out of L1/L2 source scope. Tag confirmed."),
    30: ("SURVIVES", "clean", "collectMarkerTicks() — deterministic notated-marker scan (fermata/breath/keysig-change/barline/ritardando/all-rest); notation only, no key/function. Correct."),
    31: ("SURVIVES", "clean", "soundingAt() — point-in-time note view (onset<=tick<release) reproducing legacy collectSoundingAt order. Correct."),
    32: ("SURVIVES", "clean", "collectPitchContext() — legacy DOM-walk pitch-context builder (same as reading-sample row 98). Correct, declared dual-existence."),
    33: ("SURVIVES", "clean", "NoteQueryIndex::collect() — segment-tree descent collecting overlappers in ascending index order. Correct."),
    34: ("ESTABLISHED", "clean", "0.30 wInterOnset — precision-phase surface-cue weight. Documented default."),
    35: ("ESTABLISHED", "clean", "12 in `voiceCountAtTick[12]` — one map per pitch class. Correct."),
    36: ("ESTABLISHED", "clean", "0.0 in `if (accum[pc].totalWeight > 0.0 && ...)` bass fallback (same as reading row 59). Correct."),
    37: ("ESTABLISHED", "clean", "12 in `1u << (n->ppitch() % 12)` — pitch-class bit in the onset bitmask. Correct."),
    38: ("ESTABLISHED", "clean", "2 in `m_segMaxRel[2*v]` — segment-tree child index. Structural, correct."),
    39: ("ESTABLISHED", "clean", "2 in `collect(2*node+1, ...)` — segment-tree right child (same as reading row 58). Correct."),
    40: ("ESTABLISHED", "clean", "8 LOOKAHEAD_BEATS — documented sliding-window look-ahead length constant. Established."),
}


def write_sample(basename, rows, meta, verdicts):
    verdict_fields = ["verdict", "flag", "reason"]
    for r in rows:
        v = verdicts.get(r["process_order"])
        if v:
            r["verdict"], r["flag"], r["reason"] = v
        else:
            for f in verdict_fields:
                r[f] = ""
    cols = ["process_order", "row_id", "kind", "file", "line", "label"] + verdict_fields
    csv_path = os.path.join(L1L2, basename + ".csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["process_order"]):
            w.writerow(r)
    json_path = os.path.join(L1L2, basename + ".json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump({"meta": meta, "rows": rows}, fh, indent=1, sort_keys=True)
    return csv_path, json_path


def main():
    rows = load_rows()
    total = len(rows)
    if total != 688:
        sys.stderr.write(
            "FATAL: rebuilt domain = {} rows, expected 688. "
            "Inventory drift — do not sample.\n".format(total))
        sys.exit(2)

    reading, reading_meta = draw_reading(rows)
    err, err_meta = draw_error(rows)

    write_sample("blind_rerun_reading", reading, reading_meta, READING_VERDICTS)
    write_sample("blind_rerun_errorrate", err, err_meta, ERRORRATE_VERDICTS)

    print("domain rows: {}".format(total))
    print("reading sample: {} rows (seed {}), files covered {}/{}".format(
        reading_meta["n_selected"], reading_meta["seed"],
        len(reading_meta["files_covered"]), len(reading_meta["l1l2_files"])))
    print("  kind allocation: {}".format(reading_meta["kind_allocation"]))
    print("  coverage top-ups: {}".format(reading_meta["coverage_topups"]))
    print("  reading verdicts filled: {}/{}".format(
        sum(1 for r in reading if r.get("verdict")), len(reading)))
    print("error-rate sample: {} rows (seed {}), kinds {}".format(
        err_meta["n"], err_meta["seed"], err_meta["kind_breakdown"]))
    print("  errorrate verdicts filled: {}/{}".format(
        sum(1 for r in err if r.get("verdict")), len(err)))


if __name__ == "__main__":
    main()
