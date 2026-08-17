#!/usr/bin/env python3
"""Phase 1w — verify the LEGACY-marked register entries against live reachability (OI-289).

WHAT THIS IS.  `OPEN_ITEMS.md` OI-289 carries the full re-verification of the LEGACY-marked
decision set against a live-reachability test, after the marker's "no effect on the live
solution" clause was withdrawn by the user on 2026-08-03 as an unchecked assertion (#19).
This generator publishes that verification.  It does four things:

  1. DERIVES the marked set from `backbone_decisions.json` — never from a recorded figure.
     OI-289 states in terms that no figure in the record matches the set size and that a
     reader should re-derive rather than quote; three recorded figures disagree with each
     other.  The derivation also ESTABLISHES the dispatch's assumption A1 (the marker is
     generated text emitted from one data field), by reading the generator that emits it.

  2. LOCATES every recorded figure this wave reports as stale, in the file that carries it.
     A quote that cannot be found is a STOP, not a warning.

  3. Carries the TEST, the registered PREDICTION, and the authored PER-ENTRY VERDICTS.
     The verdicts are AUTHORED — the tool refuses to guess one, and an entry without a
     verdict is a STOP.  Every code citation an entry rests on is an evidence ANCHOR that
     this tool locates and quotes at the object; an anchor whose quote is not at the cited
     line is a STOP, so the evidence cannot go stale silently.

  4. Computes the counts and compares them against the registered prediction.

WHAT IT DOES NOT DO.  It changes no mark.  Task 4 of the dispatch licenses correcting a mark
this wave ESTABLISHES wrong; this wave establishes none wrong, and the one candidate is
reported with the reason it is not settled rather than acted on.

Run:  python tools/audit/decisions/gen_phase1w_legacy_verification.py
      python tools/audit/decisions/gen_phase1w_legacy_verification.py --check   (re-derive only)

Output (ASCII only on stdout — `OPEN_ITEMS.md` OI-297, the Windows console encoding limit;
the artifact itself is UTF-8):
      tools/audit/decisions/phase1w_legacy_verification.json
"""

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

BACKBONE = ROOT / 'tools' / 'audit' / 'decisions' / 'backbone_decisions.json'
GENERATOR = ROOT / 'tools' / 'audit' / 'decisions' / 'gen_decisions_register.py'
OUT = ROOT / 'tools' / 'audit' / 'decisions' / 'phase1w_legacy_verification.json'


class Stop(Exception):
    """A premise this artifact rests on is not true at the tree. Never a warning."""


# ── A1: the marker is generated text, emitted from ONE data field ────────────────────────
# The dispatch's declared assumption. Checked here, at the generator that emits the mark,
# BEFORE the derivation below rests on it.
A1_GENERATOR_QUOTES = [
    (70, 'LEGACY_MARK = ('),
    (81, 'LEGACY_TRANSFER_MARK = ('),
    # Re-aimed 2026-08-04 (phase 1z) from this generator's own STOP message (447 -> 455), per
    # citation: the phase-1z ratification event added lines to the register generator's PREAMBLE,
    # above these two and below the first two, which is why only these two move.
    # Re-aimed AGAIN 2026-08-09 (455 -> 514, 457 -> 516) under Ruling 14 of
    # `cowork_rulings_2026_08_09_second_stop.md`, from this tool's own STOP message, which named
    # the line the first quote is at now. Same cause as the 2026-08-04 re-aim and the same
    # signature: the two quotes above are unmoved, so what grew is the register generator's own
    # preamble between them and `render_entry`, not the emission site. This is the
    # authored-input maintenance class Ruling 4(b) of `cowork_rulings_2026_08_09_return.md`
    # legitimised — a citation follows its quote; the premise itself is unchanged.
    (514, "if d.get(\"legacy_subject\"):"),
    (516, 'else LEGACY_MARK)'),
]

# ── The recorded figures this wave reports as not matching the derived count ─────────────
# Task 1.2. Each is LOCATED in the file that carries it; none is corrected here (that is
# action on surfaces, and it belongs after the gathering).
RECORDED_FIGURES = [
    {
        'figure': 80,
        'where': 'open_items/OI-289.md',
        'line': 39,
        'quote': 'the set is **80 entries**',
        'note': 'The row that owns this verification. TRUE WHEN WRITTEN (phase 1m); it first went '
                'stale at phase 1n (see when_the_set_last_changed) and the set has GROWN AGAIN '
                'since — which is the OPEN_ITEMS.md OI-354 finding, and why the discrepancy field '
                'beside this note is computed from the derived set rather than read off any '
                'recorded figure. This tool records WHEN the set last changed only up to phase 1n; '
                'the later growth is dated on OI-354\'s own row and is not re-measured here.',
    },
    {
        'figure': 80,
        # ★ TAUGHT WHERE THE ROW NOW LIVES, 2026-08-17, on the user's Ruling 1 of
        # `cowork_rulings_2026_08_17_sixth_return.md` (the user's word: "A."). The ruled
        # governing-surface split archived OI-289's resolved INDEX row, and this citation halted:
        # *"recorded figure 80: quote not at OPEN_ITEMS.md:327. It is nowhere in the file — the
        # premise has changed."* The row is byte-present in the companion, so nothing was lost and
        # the remedy is the pointer-follows-the-move discipline the split itself rests on. THE
        # QUOTE IS UNTOUCHED; only where it is looked for moves.
        'where': 'OPEN_ITEMS_ARCHIVE.md',
        # Re-aimed 2026-08-09 (318 -> 319 -> 327) per this tool's own reported line, twice in one
        # session: the OI-365 row inserted above it by `cc_instruction_return_continuation_5.md`
        # Task 0 shifted it by one, and that dispatch's Task 1 added eight lines to the INDEX
        # preamble. Authored-input maintenance (D-648), not a mechanism change. Re-aimed AGAIN
        # 2026-08-17 (327 -> 333) with the move above, at the companion's own line.
        'line': 333,
        'quote': 'Set size **80**, counted from the data',
        'note': 'The INDEX row, which the register\'s own rule makes the authoritative status '
                'surface. Same staleness as the detail file.',
    },
    {
        'figure': 79,
        'where': 'DECISIONS.md',
        'line': None,
        'quote': 'the 79-entry LEGACY-marked set confirmed',
        'note': 'The register\'s own ratified preamble (eighth ratification event, 2026-08-02). '
                'Rendered from the generator\'s PREAMBLE constant, so correcting it means '
                'editing ratified text — reported, not touched.',
    },
    {
        'figure': 75,
        # ★ THE SAME ACT BROKE THIS CITATION IN THE SAME WAY, and it is taught the same lesson.
        # Ruling 1 names the OI-289 figure; the split archived the phase-1i STATUS entry too, and
        # `--check` cannot pass while a second citation points at a file the quote left. The
        # remedy is identical and is the ruling's own stated discipline — the pointer follows the
        # move — so it is applied here and DECLARED in the report rather than taken silently. THE
        # QUOTE IS UNTOUCHED.
        'where': 'STATUS_ARCHIVE.md',
        'line': None,
        'quote': 'the 75-entry LEGACY',
        'note': 'The phase-1i entry, moved verbatim to `STATUS_ARCHIVE.md` by the ruled '
                'governing-surface split of 2026-08-17; this citation follows it. *(Former '
                'wording, preserved in place (#12): "The phase-1i entry. Still in the live STATUS '
                'entries, not archived." — true when written, and made untrue by that act.)*',
    },
    {
        'figure': 75,
        'where': 'cc_instruction_phase1m_dispositions_and_measurements.md',
        'line': 132,
        'quote': 'LEGACY-marked entries',
        'note': 'The phase-1m dispatch that opened OI-289 — so the row was sized from a figure that '
                'was already wrong by five when the row was written, which is why the row says to '
                're-derive.',
    },
]

# ── The evidence anchors ─────────────────────────────────────────────────────────────────
# Every per-entry verdict cites anchors by key. The tool reads each file and checks the quote
# is at the cited line; a miss is a STOP. Nothing here is transcribed from memory or from a
# report — each was read at the object in the session that wrote this file.
ANCHORS = {
    'FLAG_DEFAULT': {
        'file': 'src/composing/composingconfiguration.cpp', 'line': 178,
        'quote': 'settings()->setDefaultValue(USE_JOINT_NOTATION_RECORD, Val(true));',
        'says': 'The notation record arm is the DEFAULT. "Dormant" on the notation surface is a '
                'statement about this default, not about compilation.',
    },
    'NOTE_SEAM_RECORD': {
        'file': 'src/notation/internal/notationcomposingbridge.cpp', 'line': 738,
        'quote': 'return buildNoteContextFromRecord(rec.record, tick);',
        'says': 'Branch point 1 of 4. With the flag at its default the note seam returns the '
                'record view and never reaches the legacy funnel below.',
    },
    'NOTE_SEAM_LEGACY': {
        'file': 'src/notation/internal/notationcomposingbridge.cpp', 'line': 656,
        'quote': 'context.chordResults = bridgeAnalyzer->analyzeChord(analysisTones,',
        'says': 'The legacy chord scorer on the note seam, inside analyzeHarmonicContextLocallyAtTick '
                '— called at :753, BELOW the record return at :737.',
    },
    'SPAN_RECORD': {
        'file': 'src/notation/internal/notationcomposingbridge.cpp', 'line': 1502,
        'quote': 'const auto section = mu::composing::analysis::analyzeSectionFromRecord(',
        'says': 'Branch point 2 of 4 — the span annotation emitter.',
    },
    'IMPLODE_RECORD': {
        'file': 'src/notation/internal/notationimplodebridge.cpp', 'line': 1426,
        'quote': 'const auto section = mu::composing::analysis::analyzeSectionFromRecord(',
        'says': 'Branch point 3 of 4 — the implode chord track.',
    },
    'TUNING_RECORD': {
        'file': 'src/notation/internal/notationtuningbridge.cpp', 'line': 783,
        'quote': 'const auto section = mu::composing::analysis::analyzeSectionFromRecord(',
        'says': 'Branch point 4 of 4 — the tuning region path.',
    },
    'RECORD_SECTION': {
        'file': 'src/composing/analysis/section/sectionrecordadapter.cpp', 'line': 310,
        'quote': 'AnalyzedSection analyzeSectionFromRecord(const mu::engraving::Score* sc,',
        'says': 'The record arm\'s whole section derivation. Read in full (:309-362): it calls '
                'NoteModel::build, weightedPcView, regionFromRecordSegment and groupKeyAreas, and '
                'calls NEITHER analyzeChord, NOR resolveKeyAndModeRanked, NOR KeyModeSequenceDecoder, '
                'NOR the post-scoring gates. That is why the legacy scorer and the legacy key layer '
                'are off the production notation path.',
    },
    'RECORD_GROUPKEYAREAS': {
        'file': 'src/composing/analysis/section/sectionrecordadapter.cpp', 'line': 361,
        'quote': 'groupKeyAreas(out.regions, out.keyAreas);',
        'says': 'The one piece of sectionanalyzer.cpp the record arm DOES run — the shared '
                'confidence-gated key-area grouping.',
    },
    'RECORD_EXPOSURE': {
        'file': 'src/composing/analysis/section/sectionrecordadapter.cpp', 'line': 70,
        'quote': 'constexpr double kAssertiveKeyExposureGap = 1.055757;',
        'says': 'The record arm declares its OWN exposure constant on the record gap scale; it does '
                'not read the legacy 0.5/0.8 confidence gates.',
    },
    'BATCH_JOINT': {
        'file': 'tools/batch_analyze.cpp', 'line': 4805,
        'quote': 'r = joint::decodePiece(fx.piece, adapter, vocab, cache, 4, fx.sigFifths, fx.declaredMode);',
        'says': 'The production batch/corpus surface: --joint-inference decodes through the joint '
                'module alone.',
    },
    'BATCH_LEGACY_DEFAULT': {
        'file': 'tools/batch_analyze.cpp', 'line': 4926,
        'quote': 'the legacy analyzeScore pipeline. Default OFF',
        'says': 'ENUMERATED FALSE-NEGATIVE PATH: --joint-inference defaults OFF, so plain '
                'batch_analyze runs the legacy pipeline. The corpus instrument reaches the legacy '
                'scorer every time it is run without the flag.',
    },
    'TESTS_CHORD': {
        'file': 'src/composing/tests/test_helpers.h', 'line': 119,
        'quote': 'auto results = analyzer.analyzeChord(tones, keySignatureFifths, keyMode,',
        'says': 'ENUMERATED FALSE-NEGATIVE PATH: the composing test suite drives the legacy chord '
                'scorer directly, through the shared helper every chord test calls.',
    },
    'TESTS_KEY': {
        'file': 'src/composing/tests/l3_coverage_tests.cpp', 'line': 158,
        'quote': 'const auto full = kr::resolveKeyAndModeRanked(',
        'says': 'ENUMERATED FALSE-NEGATIVE PATH: the test suite drives the legacy key resolver.',
    },
    'L3_LEGACY_ENTRY': {
        'file': 'src/composing/analysis/region/regionanalyzer.cpp', 'line': 636,
        'quote': 'kms::KeyModeSequenceDecoder::decode(',
        'says': 'The legacy Layer-3 sequence decoder\'s production entry, on the legacy region path.',
    },
    # Re-aimed 2026-08-09 from this tool's own STOP message, per citation (the authored-input
    # maintenance class, D-648). These ARCHITECTURE.md anchors had drifted behind the uncovered-entry
    # STOP, which fires before the anchor loop — the same layered shape that hid the coverage check
    # itself behind the A1 citation (OPEN_ITEMS.md OI-354).
    'L3_SPEC_DORMANT': {
        # Re-aimed 2026-08-09 from 1643, per the tool's own reported line, after the Task-1 homings
        # of D-397 and D-400 inserted above it in ARCHITECTURE.md (D-648, authored-input maintenance).
        # Re-aimed again 2026-08-09 from 1673, same way and same class, after Ruling 39's delegation
        # was written into the joint-estimator section above it.
        # Re-aimed again 2026-08-11 from 1679, same way and same class, after Ruling 63's
        # evidential-priority section was written into the joint-estimator section above it.
        # Re-aimed again 2026-08-11 from 1721, same way, after the OI-318 scope-correction clause.
        'file': 'ARCHITECTURE.md', 'line': 1731,
        'quote': "Layer 3's decoder no longer decides the key on either surface",
        'says': 'The layer specification\'s own build-state correction, which enumerates the same four '
                'branch points this wave read and adds the remaining callers: "the batch_analyze '
                'diagnostics, which are development tools and are not shipped".',
    },
    'L4_SPEC_DORMANT': {
        # Re-aimed 2026-08-09 from 1854, then from 1884, each per this tool's own reported line
        # (D-648) — the second after Ruling 39's delegation was written above it. Re-aimed again
        # 2026-08-11 from 1890, same way, after Ruling 63's evidential-priority section.
        'file': 'ARCHITECTURE.md', 'line': 1942,
        'quote': 'The build state itself is unchanged and correct: Built+Dormant.',
        'says': 'The Layer-4 section\'s own build state. What becomes of that decoder is recorded OPEN.',
    },
    'SPEC_DONOTRETRY_CHORD': {
        # Re-aimed 2026-08-09 from 1860, then from 1890, each per this tool's own reported line
        # (D-648) — the second after Ruling 39's delegation was written above it.
        # Re-aimed again 2026-08-11 from 1896, same way, after Ruling 63's evidential-priority
        # section was written into the joint-estimator section above it.
        'file': 'ARCHITECTURE.md', 'line': 1948,
        'quote': 'Tried and closed on the chord layer',
        'says': 'A LIVE do-not-retry list in the layer specification naming ten marked entries. The '
                'mark is right about the SUBJECT and the entry still binds what a future designer '
                'may attempt.',
    },
    'SPEC_DONOTRETRY_KEY': {
        # Re-aimed 2026-08-09 from 1656, then from 1686, each per this tool's own reported line
        # (D-648) — the second after Ruling 39's delegation was written above it.
        # Re-aimed again 2026-08-11 from 1692, same way, after Ruling 63's evidential-priority
        # section was written into the joint-estimator section above it.
        'file': 'ARCHITECTURE.md', 'line': 1744,
        'quote': 'Tried and closed on this layer',
        'says': 'The same construction on the key layer, naming D-287 and D-290.',
    },
    'SPEC_DONOTRETRY_SEARCH': {
        'file': 'ARCHITECTURE.md', 'line': 315,
        'quote': 'Tried and closed on the search',
        'says': 'The same construction on the search, naming D-288, D-328 and D-278.',
    },
    # ADDED 2026-08-09 with the OI-354 verdict set (user, Ruling 23 of
    # `cowork_rulings_2026_08_09_fourth_stop.md`). The fourth instance of the do-not-retry
    # construction the pass already anchors on the chord layer, the key layer and the search.
    'SPEC_DONOTRETRY_DECLARED_MODE': {
        # Re-aimed 2026-08-09 from 4198, then from 4228, each per this tool's own reported line
        # (D-648) — the second after Ruling 39's delegation was written above it.
        # Re-aimed again 2026-08-11 from 4234, same way, after Ruling 63's evidential-priority
        # section and the §5.2 annotation were written above it.
        # Re-aimed again 2026-08-11 from 4294, same way, after the OI-346 marks were written into
        # §4.6's preset table above it.
        'file': 'ARCHITECTURE.md', 'line': 4339,
        'quote': "Tried and closed on the declared mode's weight",
        'says': 'The same construction on the declared mode\'s weight, naming D-572 with its '
                'evidence — a LIVE specification line whose subject is a removed legacy promotion '
                'and whose prohibition binds now.',
    },
    'ARCH_BATCH_DIAGNOSTICS': {
        # Re-aimed 2026-08-09 from 1651, then from 1681, each per this tool's own reported line
        # (D-648) — the second after Ruling 39's delegation was written above it.
        # Re-aimed again 2026-08-11 from 1687, same way, after Ruling 63's evidential-priority
        # section was written into the joint-estimator section above it.
        'file': 'ARCHITECTURE.md', 'line': 1739,
        'quote': 'callers are the `batch_analyze` diagnostics, which are development tools and are not shipped',
        'says': 'The layer specification already names the fifth false-negative path — the batch '
                'diagnostics — which OI-289\'s four-item enumeration does not. Located here rather '
                'than quoted as a line number in prose, which is the failure D-432\'s own defense '
                'was re-written to avoid.',
    },
    'ARCH_D429_POINTER': {
        'file': 'ARCHITECTURE.md', 'line': 287,
        'quote': 'register entry **D-429**',
        'says': 'The pointer that carries D-429\'s transferred principle into the live design\'s '
                'own specification.',
    },
    'ARCH_L3_DELEGATION': {
        # Re-aimed 2026-08-09 from 1654, then from 1684, each per this tool's own reported line
        # (D-648) — the second after Ruling 39's delegation was written above it.
        # Re-aimed again 2026-08-11 from 1690, same way, after Ruling 63's evidential-priority
        # section was written into the joint-estimator section above it.
        'file': 'ARCHITECTURE.md', 'line': 1742,
        'quote': 'The ratified contract for this layer is `cowork_layer3_keymode_design.md`',
        'says': 'The delegation that makes the Layer-3 design document a contract home. It sits '
                'immediately below the build-state correction declaring that layer dormant, which '
                'is why the marks on its decisions are consistent rather than contradictory.',
    },
    'ARCH_L5_ENGAGEMENT_DELEGATION': {
        # Re-aimed 2026-08-09 from 2018, then from 2048, each per this tool's own reported line
        # (D-648) — the second after Ruling 39's delegation was written above it.
        # Re-aimed again 2026-08-11 from 2054, same way, after Ruling 63's evidential-priority
        # section was written into the joint-estimator section above it.
        'file': 'ARCHITECTURE.md', 'line': 2106,
        'quote': 'The ratified contract for how this layer ENGAGES with the chord layer',
        'says': 'The delegation behind D-380/D-381\'s home — the reason their transfer half is '
                'undetermined rather than none-found.',
    },
    'REDESIGN_LIVE_PROHIBITION': {
        'file': 'docs/redesign_plan.md', 'line': 4,
        'quote': 'are LIVE prohibitions about the legacy chord path',
        'says': 'The document that homes D-317-D-320 says the distinction in its own words: the '
                'prohibition is LIVE, its subject is the legacy path.',
    },
    'CSF_RECORD_ARM': {
        'file': 'src/notation/internal/notationimplodebridge.cpp', 'line': 1170,
        'quote': 'ChordSymbolFormatter::formatSymbol(chord, localKeyFifths, fmtOpts))',
        'says': 'The chord-symbol formatter runs on the RECORD arm. This is the established evidence '
                'on which D-311\'s mark was removed at phase 1m.',
    },
    'JOINT_SIG_READ': {
        'file': 'src/composing/analysis/joint/jointfactadapter.cpp', 'line': 359,
        'quote': 'const KeySigEvent kse = score->staff(0)->keySigEvent(Fraction(0, 1));',
        'says': 'The joint fact adapter performs its OWN signature and declared-mode read rather than '
                'calling the shared resolveKeySignatureContext D-052 is about.',
    },
    'MODE_PRIOR_SETTING': {
        'file': 'src/composing/composingconfiguration.cpp', 'line': 63,
        'quote': 'MODE_PRIOR_IONIAN',
        'says': 'The twenty-one mode-prior preferences are registered in the module configuration, '
                'which runs unconditionally. Their CONSUMER is the legacy key scorer.',
    },
    'FM2_FLIP': {
        'file': 'src/composing/analysis/chord/postscoringgates.cpp', 'line': 270,
        'quote': 'The surviving rule name for the whole flip is FM2',
        'says': 'The enharmonic flip D-219 constrains survives at HEAD as FM2, so D-219\'s standing '
                'half governs code that exists.',
    },
    'JKEY_WIRING_FLAG': {
        'file': 'src/composing/analysis/region/regionanalyzer.cpp', 'line': 1484,
        'quote': 'if (analysis::jointKeyWiringEnabled()) {',
        'says': 'A SECOND runtime flag, default OFF, gating the built half of the shelved joint '
                'key-and-chord step. Reachability on the legacy arm is not decided by '
                'useJointNotationRecord alone.',
    },
    'JKEY_NO_REEMIT': {
        'file': 'src/composing/analysis/region/regionanalyzer.cpp', 'line': 390,
        'quote': 'The CHORD is left as the production chord R0 (NOT re-emitted)',
        'says': 'The chord half of the shelved step is not built, which is what D-378 is about.',
    },
    'SLICE_DECODER_DORMANT': {
        'file': 'tools/batch_analyze.cpp', 'line': 2964,
        'quote': 'the dormant per-slice chord decoder',
        'says': 'The Layer-4 slice decoder is reached only by batch_analyze diagnostic flags and the '
                'test suites. The batch diagnostic flags are a false-negative path OI-289\'s '
                'four-item enumeration does not name; ARCHITECTURE.md:1339 does name them.',
    },
    'L5_DIAG_ONLY': {
        'file': 'tools/batch_analyze.cpp', 'line': 107,
        'quote': '#include "composing/analysis/function/functionresolver.h"',
        'says': 'The Layer-5 function module is reached only by batch_analyze diagnostic dumps '
                '(--dump-l5, --dump-fullspine) and the test suites — no production caller.',
    },
    'FIND_TEMPORAL_LEGACY': {
        'file': 'src/composing/analysis/engravingbridge/regiontoneprimitives.cpp', 'line': 507,
        'quote': 'chordAnalyzer->analyzeChord(prevTones, keyFifths, keyMode, nullptr,',
        'says': 'The Layer-1.5 primitive that runs the whole chord decision to obtain neighbour '
                'identities — the violation D-404 defers, still at HEAD on the legacy arm.',
    },
    'JOINT_APPLIED_RN': {
        'file': 'src/composing/analysis/joint/jointrender.h', 'line': 62,
        'quote': 'applied',
        'says': 'The production renderer emits applied-chord labels, which is why D-248\'s scope was '
                'corrected on 2026-08-02.',
    },
}

# ── The test, stated before it is applied (dispatch section 2) ───────────────────────────
THE_TEST = {
    'source': {
        'file': 'open_items/OI-289.md', 'line': 50,
        'quote': 'for each marked entry, is its subject reachable on either production surface at HEAD, and',
    },
    'half_a_reachability': (
        'Is the entry\'s subject reachable on EITHER production surface at HEAD? Because the notation '
        'arm turns on a runtime flag whose default is true rather than on compilation, a bare '
        '"dormant" is not an answer: each verdict names WHICH SENSE it means, from the four below.'
    ),
    'half_b_transfer': (
        'Does any ruling carry the decision\'s PRINCIPLE across to the live design, as the OI-275 '
        'ruling did for D-329? A mark correct about the subject can still be wrong about the effect.'
    ),
    'reachability_senses': {
        'production': 'The subject\'s code runs on a DEFAULT production path — the in-app record arm, '
                      'or batch_analyze --joint-inference.',
        'false-negative-path': 'Not on any default production path, but reached by an enumerated '
                               'non-default path: an explicit flag flip, plain batch_analyze (the '
                               '--joint-inference flag defaults OFF), a batch_analyze diagnostic dump '
                               'flag, the test suites, or the declared non-production uncached path.',
        'flag-default-only': 'Unreachable only while useJointNotationRecord holds its default, and by '
                             'no other path. (No entry received this verdict — see '
                             'what_this_found.the_dormancy_is_weaker_than_it_sounds.)',
        'none': 'Unreachable at any setting: no code at HEAD implements the subject. A decision whose '
                'subject is a prohibition, a closure or a design never built.',
        'undetermined': 'The evidence read does not settle it.',
    },
    'transfer_values': {
        'ruling-transferred': 'A later ruling explicitly carried the principle to the live design.',
        'live-prohibition-in-spec': 'A LIVE specification section restates the decision as a standing '
                                    'do-not-retry. The subject stays legacy; the prohibition binds now.',
        'carried-elsewhere': 'The record states the doctrine lives on in another, live entry or rule.',
        'assigns-live-work': 'The decision\'s OWN text assigns work, ownership or a property to the '
                             'live design. Not a later ruling — which is why it is a separate value.',
        'explicitly-not-transferred': 'A ruling states in terms that the decision does NOT bear on the '
                                      'live design.',
        'none-found': 'The citation scan over every .md/.cpp/.h/.py/.txt surface found no ruling '
                      'carrying it, and the surfaces that do cite it are register mechanics.',
        'scoped-to-an-act-that-never-ran': 'A USER RULING settles, on the two records\' own words, '
                                           'that the decision\'s constraint was scoped to an act '
                                           'that was never performed — so no ruling carried it '
                                           'across, and any live-design question that survives is '
                                           'a separate ROWED input rather than a transfer. ADDED '
                                           '2026-08-09 for Ruling 34; used by one entry. It is a '
                                           'distinct value because the three that could otherwise '
                                           'carry it each say something the ruling declined to '
                                           'say: `none-found` reports a SEARCH result where this '
                                           'is a ruling, `explicitly-not-transferred` asserts the '
                                           'decision does not bear on the live design where the '
                                           'ruling leaves exactly that open, and `undetermined` '
                                           'says the evidence does not settle it where it now '
                                           'does.',
        'undetermined': 'The evidence read does not settle it.',
    },
    'how_the_transfer_half_was_searched': (
        'Every occurrence of each marked entry\'s ID was collected across the repository '
        '(.md/.cpp/.h/.py/.txt, register-internal data files excluded), and the hits outside the '
        'register\'s own mechanics were read. TWO PROPERTIES OF THE SEARCH, stated because they bound '
        'what a "none-found" verdict is worth: (i) it finds a transfer only where the transferring '
        'ruling NAMES THE ENTRY — a ruling that carries a principle without citing the decision is '
        'invisible to it; (ii) NO marked ID is cited anywhere under src/, so no verdict rests on a '
        'code comment.'
    ),
}

# ── The prediction, registered before the per-entry pass (#17b) ──────────────────────────
THE_PREDICTION = {
    'registered': 'Before the per-entry verdicts were assigned, and AFTER the structural code facts '
                  'above were established. Stated plainly because it changes what the prediction is '
                  'worth: the anchors were read first, so the reachability bands are informed rather '
                  'than blind. The transfer bands were not — the citation scan had been run but its '
                  'hits had not been read when these were written.',
    'reachability': {
        'production': '0 — the two production paths were traced and neither enters the legacy scorer '
                      'or the legacy key layer.',
        'false-negative-path': 'the large majority — plain batch_analyze and the test suites both '
                               'drive the legacy scorer.',
        'none': 'a minority — the shelved, reverted and never-built subjects.',
        'undetermined': '0 to 3.',
    },
    'transfer': {
        'ruling-transferred': 'exactly 2 (D-329, D-329\'s sibling D-429 — the two the data already '
                              'flags with the transfer variant).',
        'own-text-assigns-live': '3 to 8.',
        'undetermined': '5 or more.',
    },
    'marks_established_wrong': '0 — the weakening removed the clause that failed, so the surviving '
                               'mark claims only what the decision is ABOUT, and that is what the '
                               'marking pass actually checked.',
}

# ── The authored per-entry verdicts ─────────────────────────────────────────────────────
# (id, subject, reachability sense, anchor keys, transfer value, note)
# Every row is authored. The tool refuses to emit if a derived entry has no row, or a row
# names an entry that is not in the derived set.
VERDICTS = [
    ('D-053', 'The P4 tick-local path keeping the older resolver',
     'false-negative-path', ['FLAG_DEFAULT', 'NOTE_SEAM_RECORD', 'NOTE_SEAM_LEGACY', 'TESTS_KEY'],
     'none-found',
     'The clearest flag-default case in the set: the subject sits directly below the record return.'),
    ('D-054', 'The legacy key scorer\'s 21-mode x 12-tonic grid; harmonic major deferred',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-055', 'The 21 mode priors as independent, user-configurable values',
     'production', ['MODE_PRIOR_SETTING', 'L3_SPEC_DORMANT', 'TESTS_KEY'],
     'none-found',
     'THE ONE CANDIDATE WRONG MARK, AND IT IS NOT CORRECTED. The preference registration runs '
     'unconditionally in the module configuration — production code — while the consumer that reads '
     'the priors is the legacy key scorer. Whether the SETTINGS are themselves legacy-scoped (and so '
     'retire with the scorer) is a scoping judgment, not a code fact this wave can settle, so the '
     'mark stands and the finding is reported. Task 4 licenses correcting an ESTABLISHED error only.'),
    ('D-058', 'The legacy key resolver\'s piece-start shortcut',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-068', 'The legacy analyzer\'s three-distinct-pitch-class minimum',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'undetermined',
     'A minimum-content admission rule is the same KIND of rule the live family design is about '
     '(OI-226 records the joint decoder\'s admission as having no ratified basis). No ruling names '
     'D-068, so a transfer cannot be asserted — but a reader designing admission should see it.'),
    ('D-069', 'Merged-stretch identity: the harmonic-summary mode built, the as-written mode not',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found',
     'Split subject: the built half is legacy code on the false-negative paths; the second mode is not '
     'built at all.'),
    ('D-103', 'The pedal-point second pass and its two acceptance conditions',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-215', 'Gating the root-continuity bonus on a sparse predecessor',
     'none', ['SPEC_DONOTRETRY_CHORD', 'BATCH_LEGACY_DEFAULT'],
     'live-prohibition-in-spec',
     'The GATING was tried in two forms and abandoned, so nothing at HEAD implements the subject; the '
     'bonus it would have gated is legacy code. ARCHITECTURE.md:1420 lists it as a live do-not-retry, '
     'and D-423 names it as one of three programme-wide prohibitions.'),
    ('D-220', 'The augmented-seventh guard requiring both intervals',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-221', 'Denying inversion bonuses to a sparse upper-register lowest note',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-222', 'Falling back when the diminished bonus rotates the winner off diminished',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-223', 'A gate judging the pre-correction winner reads a snapshot',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-224', 'Joint bass-and-chord scoring gated on accumulated regional evidence',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-248', 'The legacy ChordFunction structure carrying no relative-root field',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'L5_DIAG_ONLY', 'JOINT_APPLIED_RN'],
     'assigns-live-work',
     'The entry\'s own scope correction of 2026-08-02 records that the production renderer DOES emit '
     'applied labels. So the mark is right about the subject and the entry already carries the live '
     'statement — the inverse of a transfer, and the reason OI-267 exists.'),
    ('D-278', 'The shelved joint key-and-chord step',
     'false-negative-path', ['JKEY_WIRING_FLAG', 'JKEY_NO_REEMIT', 'BATCH_LEGACY_DEFAULT'],
     'explicitly-not-transferred',
     'Split subject, and the split matters: the KEY half IS built (jointkeydecision.cpp) and is called '
     'behind a SECOND default-OFF flag on the legacy region path; the chord half is not built. The '
     'user\'s 2026-08-02 scoping states in terms that the shelving does not bear on the joint '
     'estimator.'),
    ('D-284', 'The saturation meta-finding on the legacy selection surface',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'L4_SPEC_DORMANT'],
     'carried-elsewhere',
     'cowork_architecture_reassessment.md records the successor mapping D-284 -> D-036 with '
     'D-001/D-010: the doctrine lives on generalized in a live entry.'),
    ('D-287', 'Carrying a ranked key distribution forward instead of one committed key',
     'none', ['SPEC_DONOTRETRY_KEY'],
     'live-prohibition-in-spec',
     'Shelved before building; nothing at HEAD implements it. The key layer\'s specification lists it '
     'as a live do-not-retry.'),
    ('D-288', 'Widening the beam of the chord search',
     'none', ['SPEC_DONOTRETRY_SEARCH'],
     'live-prohibition-in-spec', ''),
    ('D-290', 'The key-agnostic local cadence approach',
     'none', ['SPEC_DONOTRETRY_KEY'],
     'live-prohibition-in-spec',
     'Falsified against a byte-matched reimplementation; never shipped.'),
    ('D-299', 'A negative-margin guard over the correction steps',
     'none', ['SPEC_DONOTRETRY_CHORD'],
     'live-prohibition-in-spec',
     'A prohibition on a guard that was never added — so there is no code, and the correction steps it '
     'would have disabled are legacy.'),
    ('D-300', 'Gate M — re-reading a minor chord as diminished on the same root',
     'none', ['SPEC_DONOTRETRY_CHORD'],
     'live-prohibition-in-spec', ''),
    ('D-301', 'Gate N — re-reading a root-position major as an inverted minor',
     'none', ['SPEC_DONOTRETRY_CHORD'],
     'live-prohibition-in-spec', ''),
    ('D-302', 'The closure of local scoring fixes for inversions',
     'none', ['SPEC_DONOTRETRY_CHORD'],
     'live-prohibition-in-spec',
     'A closure of a line of work, not a mechanism; nothing implements it.'),
    ('D-306', 'The key layer\'s backward re-reading facility, shipped switched off',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found',
     'ARCHITECTURE.md:1346-1349 restates it in the live-specification voice ("stays SWITCHED OFF in '
     'the shipped configuration") INSIDE the section whose own build-state correction declares the '
     'layer dormant. Both statements are in the record; a reader meeting the second first would read '
     'a shipped-configuration claim about a dormant layer.'),
    ('D-317', 'The one-tick backward-walk boundary change',
     'none', ['SPEC_DONOTRETRY_CHORD', 'REDESIGN_LIVE_PROHIBITION'],
     'live-prohibition-in-spec',
     'Tried and closed; not in the code. Its home says the distinction in its own words.'),
    ('D-318', 'A short-region external merger pass',
     'none', ['SPEC_DONOTRETRY_CHORD', 'REDESIGN_LIVE_PROHIBITION'],
     'live-prohibition-in-spec', ''),
    ('D-319', 'Re-analysing the merged tone aggregate',
     'none', ['SPEC_DONOTRETRY_CHORD', 'REDESIGN_LIVE_PROHIBITION'],
     'live-prohibition-in-spec',
     'Implemented, measured and reverted; not in the code.'),
    ('D-320', 'The absent-root guard',
     'none', ['SPEC_DONOTRETRY_CHORD', 'REDESIGN_LIVE_PROHIBITION'],
     'live-prohibition-in-spec',
     'Built, measured and removed entirely; not in the code.'),
    ('D-321', 'Exact candidate-score comparison with no epsilon in the ranking',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'undetermined',
     'A no-tolerance ranking convention is a decoder-wide property; the live decoder\'s own tie and '
     'comparison convention was not read this wave, so whether the same rule holds there is open.'),
    ('D-322', 'Requiring a full corpus A/B for any change to optimization flags or arithmetic order',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'undetermined',
     'Same ground as D-321 — and the phase-1o probe re-run measured a ~1e-14 C-library difference on '
     'the live joint path, which is the same hazard class this decision is about.'),
    ('D-324', 'Global retirement of a post-scoring rule',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-325', 'Retiring or folding in a committing correction before widening the search',
     'false-negative-path', ['SLICE_DECODER_DORMANT', 'BATCH_LEGACY_DEFAULT'],
     'undetermined',
     'Adjacent to the rule D-429\'s transfer already carries (a correction belongs in a fitted value, '
     'never in a layer over the decode). Whether D-429\'s transfer subsumes this one is a question for '
     'the ruling, not for this wave.'),
    ('D-326', 'The chord-path search emitting the whole path with alternatives and margins',
     'false-negative-path', ['SLICE_DECODER_DORMANT', 'BATCH_LEGACY_DEFAULT'],
     'undetermined',
     'The live record publishes a section 3.3 chord-axis alternative list per segment, which is the '
     'same property; no ruling names D-326, so the transfer cannot be asserted from the record.'),
    ('D-327', 'The root-continuity guard reading reconstructed inversion credit',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-328', 'A wider search over the same scoring as a fix for the arpeggio root failure',
     'none', ['SPEC_DONOTRETRY_CHORD', 'SPEC_DONOTRETRY_SEARCH'],
     'live-prohibition-in-spec',
     'A refutation, not a mechanism. Listed twice in the live specification — on the chord layer and '
     'on the search.'),
    ('D-329', 'The legacy Layer-4 decoder\'s complete-candidate-listing step',
     'false-negative-path', ['SLICE_DECODER_DORMANT', 'L4_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'ARCH_BATCH_DIAGNOSTICS'],
     'ruling-transferred',
     'The known case. The user\'s OI-275 ruling of 2026-08-02 (reading 1-with-transfer) carried the '
     'principle to the live family design; the entry already carries the transfer variant of the mark.'),
    ('D-342', 'Putting the Layer-5 function layer into production',
     'false-negative-path', ['L5_DIAG_ONLY', 'BATCH_LEGACY_DEFAULT', 'ARCH_BATCH_DIAGNOSTICS'],
     'carried-elsewhere',
     'The module is built and reached only by batch_analyze diagnostic dumps and the test suites. The '
     'entry\'s own text enumerates where each of its concerns is handled on the live implementation.'),
    ('D-344', 'Reporting an unrecognized scale as the best-fitting recognized mode',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'undetermined',
     'The live estimator\'s label class set is a different mechanism and was not read this wave. The '
     'question the entry raises — what happens to music outside the recognized set — is live '
     'regardless of which engine answers it.'),
    ('D-345', 'The style preset entering the analysis first at the key/mode layer',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT'],
     'none-found',
     'Production inference is preset-independent (CLAUDE.md gate block (A)), so on the live arm the '
     'preset has no entry point at all — the decision describes an arrangement the live system does '
     'not have, which is what the mark is for.'),
    ('D-347', 'The change-cost shape: cheap-to-stay plus distance plus a relative-pair penalty',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-348', 'Circle-of-fifths distance in the change cost, and no duration threshold',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-349', 'Whole-reading key confidence rather than a per-stretch top-two gap',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-351', 'The key/mode search as its own decoder, not the chord decoder reused',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found',
     'OBSERVATION: the live estimator decides key and chord inside ONE decode, which is the opposite '
     'arrangement. The mark is right — the decision is about the legacy pair — and a reader should not '
     'read it as describing what runs.'),
    ('D-358', 'Dominant-shaped sonority as note-level tonality evidence',
     'none', ['L3_SPEC_DORMANT', 'ARCH_L3_DELEGATION'],
     'undetermined',
     'Deferred and not built. The question it raises — under-modulation where tonics are withheld — is '
     'live for whatever engine decides key, and ARCHITECTURE.md:1342 delegates this layer\'s contract '
     'to the document holding it; no ruling carries it across.'),
    ('D-376', 'The bounded-coupling shape chosen over a unified single state',
     'none', ['JKEY_WIRING_FLAG', 'JKEY_NO_REEMIT'],
     'assigns-live-work',
     'Neither shape exists as described — the coupling was shelved. The entry\'s own title records that '
     'the REJECTED option is the shape the production engine now has, which is a statement about the '
     'live design inside a LEGACY-marked entry.'),
    ('D-380', 'The carry\'s distinct-root axis and graded confidence',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'L4_SPEC_DORMANT', 'ARCH_L5_ENGAGEMENT_DELEGATION'],
     'undetermined',
     'Its home is the engagement design ARCHITECTURE.md:1498 delegates as a ratified contract. Whether '
     'that contract binds the live estimator\'s carry was not established this wave.'),
    ('D-381', 'Capping the carry on distinct roots rather than voicings',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'L4_SPEC_DORMANT', 'ARCH_L5_ENGAGEMENT_DELEGATION'],
     'assigns-live-work',
     'The owed shape is not built; the existing voicing-keyed cap is legacy code. The entry leaves the '
     'limit\'s value "to the fitting phase", which is live work.'),
    ('D-403', 'The four best-different-root scans as four decisions, not one',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-404', 'The deferred relocation of the neighbour-chord temporal-context computation',
     'false-negative-path', ['FIND_TEMPORAL_LEGACY', 'BATCH_LEGACY_DEFAULT'],
     'assigns-live-work',
     'The violating primitive is at HEAD on the legacy arm. The decision names the replacement decoder '
     'as the owner of regional temporal context — an assignment to the live design, made in the '
     'decision itself rather than by a later ruling. OI-165 puts it the same way: D-404 defers rather '
     'than forbids.'),
    ('D-428', 'The owed iteration-vocabulary API renames',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'FIND_TEMPORAL_LEGACY', 'BATCH_LEGACY_DEFAULT'],
     'none-found',
     'FINDING, reported not fixed: two dated annotations still assert the OPPOSITE of this entry as '
     'corrected at phase 1n — cowork_stage5_fitter_design.md:116 and '
     'cowork_structural_integrity_audit.md:323 both say the subject "includes live Layer-1.5 code", '
     'while the entry says every use sits on the legacy arm and deleting that path discharges it.'),
    ('D-429', 'Dissolving the post-hoc gate-correction layer into fitted weights',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD', 'ARCH_D429_POINTER'],
     'ruling-transferred',
     'The second known case. The rule itself was carried to the live estimator by the user\'s ruling '
     'of 2026-08-03; the entry carries the transfer variant, ARCHITECTURE.md:278 carries the pointer, '
     'and all eight struck-versus-sounding family rows cite it.'),
    ('D-423', 'The gate-retirement stage as the only sanctioned way the post-scoring gates change',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'undetermined',
     'THE SHARPEST UNDETERMINED IN THE SET. The entry says its three prohibitions hold "for the whole '
     'programme" while being LEGACY-marked, and one of the three is the rule D-429\'s transfer already '
     'carries to the live design. Either the programme-wide claim is a transfer the record has not '
     'ruled, or it is scoped to the legacy path and the wording overstates it. A session may not '
     'decide which.'),

    # ── THE ELEVEN ENTRIES MARKED SINCE THE PHASE-1W PASS ────────────────────────────────────
    # AUTHORED 2026-08-09 by `cc_instruction_return_continuation_3.md` Task 1 on the user's
    # Ruling 18 of `cowork_rulings_2026_08_09_third_stop.md`, delivered for review at
    # `ratification_surfaces/cowork_oi354_legacy_mark_establishment_2026_08_09.md`, and APPLIED
    # HERE 2026-08-09 on the user's Ruling 23 of `cowork_rulings_2026_08_09_fourth_stop.md`,
    # which ratifies ten of the eleven whole and holds D-580's TRANSFER cell UNDETERMINED
    # pending Ruling 27's fact-gathering pass.
    #
    # THE AUTHORING SESSION CLEARED NO GUARD (D-655): these verdicts were written into a reading
    # file, the standing check was carried red across that session, and it clears here — in the
    # commit that cites the user's ruling on the reviewed set. `OPEN_ITEMS.md` OI-354 is the
    # event's row; OI-289's own VERIFIED status is untouched, being true of the population it
    # covered.
    #
    # The METHOD is this pass's own, read in full before the first verdict and not invented:
    # half A is reachability at the code with the five senses declared in THE_TEST, half B is
    # the citation-transfer scan with the two bounds THE_TEST states on it. Where a case needed
    # a judgment this pass had already faced, the pass's own precedent is named in the note.
    ('D-536', 'The bass and the chord chosen TOGETHER as one bass-root-template triple',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'carried-elsewhere',
     'The legacy chord scorer, reached by plain batch_analyze and by the composing test suite, and '
     'sitting below the record return on the note seam. The transfer is the record\'s own statement, '
     'in this entry\'s home text AND its provenance: the principle it embodies — deciding coupled '
     'quantities together rather than committing one early — is the one D-001 carries for the live '
     'design ("Key, mode and chord are inferred by ONE joint decode"). The MECHANISM is legacy; the '
     'doctrine is live and named.'),
    ('D-537', 'The completeness bonus firing only for a root-position reading — the guard against '
     'demoting genuine slash chords',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'carried-elsewhere',
     'Same arm as D-536. The home text states the kinship in its own words: it is "an early instance '
     'of the standing rule that a correction is given a structural entry condition rather than a '
     'widened threshold" (CLAUDE.md, the gate and preset policy), which is live and binds now. '
     'STATED PRECISELY SO IT IS NOT OVER-CREDITED: what is carried is the general rule, not this '
     'guard; the guard itself is legacy code.'),
    ('D-538', 'A multi-signal change lands one signal at a time, the corpus re-run after each, any '
     'rise a hard stop',
     'none', [],
     'carried-elsewhere',
     'Reach `none` on this pass\'s own D-302 precedent ("a closure of a line of work, not a '
     'mechanism; nothing implements it"): the subject is a LANDING PROCEDURE for one past change, so '
     'there is no code at HEAD to reach at any setting and no code anchor can bear on it — which is '
     'why the anchor list is empty rather than padded with an anchor that would not be evidence for '
     'the verdict. Transfer is the clearest in the set and is already RULED: the user ruled this '
     'entry\'s content superseded by D-177 (one revertible provenance-stamped commit per behaviour '
     'change) and D-115 (the measured non-increase of gate block (A)), both homed in CLAUDE.md, with '
     'the obligation moved to them under D-642.'),
    ('D-564', 'Correction of record: the function-only share of the legacy residual was overstated — '
     'over-grab corrupts the BASS',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found',
     'Reach follows this pass\'s D-284 and D-243 precedent — a FINDING about the legacy surface takes '
     'the reachability of the surface it is about, not of the prose that records it. Transfer: the '
     'citation scan finds only homing and triage hits and no ruling carries it. ONE OBSERVATION, '
     'RECORDED RATHER THAN PROMOTED TO A VERDICT: its home is CLAUDE.md gate block (D), and the '
     'caveat it corrects is stated there as applying equally to the robust unit — the live '
     'measurement — so a reader of the live block meets the corrected apportionment. That is the '
     'entry\'s HOME being live, not a ruling carrying its principle, and under bound (i) it is not a '
     'transfer.'),
    ('D-568', 'The two-track remedy: chord axis by hand-built rules, key axis by evidence quality and '
     'calibration — neither by a wider search',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD', 'TESTS_KEY'],
     'assigns-live-work',
     'The two-axis pipeline it was derived on is reachable only off the default paths. The transfer '
     'half is `assigns-live-work` on that value\'s own definition — the decision\'s OWN text assigns '
     'work to the live design rather than a later ruling — and the record says so twice: the home '
     'text calls it "the work-programme statement it is, not a description of what runs", and its '
     'key-axis half assigns the residual to the joint combination\'s SOFT integration, which is the '
     'live estimator. Its home is the arc plan\'s Stage-5 paragraph, the precision work it governs.'),
    ('D-571', 'The declared-mode influence becomes a small additive hint, and SMALLNESS IS THE GATE',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'carried-elsewhere',
     'A scoring term of the legacy key emission. The transfer is unusually exact and the record names '
     'it: this entry\'s provenance states that the joint estimator takes the signature and declared '
     'mode as "a weak fitted soft prior with no conditional gate anywhere" (D-528) and conditions the '
     'initial key state only (D-450) — and "no conditional gate anywhere" is this decision\'s own "no '
     'separate confidence test is added", on the live arm.'),
    ('D-572', 'The hard post-hoc declared-mode promotion REMOVED OUTRIGHT rather than kept in a gated '
     'form',
     'none', ['SPEC_DONOTRETRY_DECLARED_MODE'],
     'live-prohibition-in-spec',
     'Reach `none`: the promotion was removed, so nothing at HEAD implements the subject. This is the '
     'ONE entry of the eleven cited in a LIVE specification section, and the citation is a standing '
     'do-not-retry naming the entry with its evidence. The subject stays legacy; the prohibition '
     'binds now. (D-528\'s own title additionally records that the hard declared-mode wall is '
     'formally retired on the live arm — noted, but the do-not-retry line is the more specific and is '
     'what the verdict rests on.)'),
    ('D-575', 'The Baroque partial-signature convention handled by DETECTING it and reinterpreting '
     'the signature one step',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found',
     'The correction is applied inside the legacy resolver, which the production arm does not run. '
     'DELIBERATELY NOT `explicitly-not-transferred`, and the distinction matters: that value requires '
     'a ruling stating the decision does not bear on the live design, and what the record actually '
     'says is that the question is UNSETTLED — the home text\'s own words are "Whether the joint '
     'estimator handles the convention AT ALL is NOT settled by this entry and is not asserted here." '
     'Unsettled is not the same as not-transferred, so the weaker verdict is the honest one. The live '
     'open question this exposes is rowed at OPEN_ITEMS.md OI-357.'),
    ('D-580', 'Two of the twelve post-scoring gates are purely-local and MUST survive the '
     'dissolution; the other ten dissolve',
     'false-negative-path', ['FM2_FLIP', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'scoped-to-an-act-that-never-ran',
     'The gates are legacy code at HEAD, and the entry\'s own home text says the surviving rule name '
     'for one of the two is FM2, which is the anchor. THE TRANSFER HALF IS SETTLED BY THE USER\'S '
     'RULING 34 of `cowork_rulings_2026_08_09_fifth_stop.md`, taken on the facts gathered under '
     'Ruling 27 and delivered at '
     '`ratification_surfaces/cowork_d580_transfer_fact_gathering_2026_08_09.md`. THE RULING, in its '
     'own terms: reading (ii) — DIFFERENT ACTS, BOTH RECORDS TRUE. D-580\'s carve-out is about a '
     'DISSOLUTION into the competition that never ran; the retirement map\'s R1 performs a DELETION '
     'of the legacy path; both stand, and R1 is NOT qualified. The carve-out is therefore recorded '
     'as scoped to the unrun dissolution, which is what this transfer value states. THE EXCLUDED '
     'READING IS RECORDED (#12): reading (i), that R1 overlooked the carve-out — it would qualify a '
     'ratified map on an assumption about intent, the unestablished-premise class the user\'s own '
     'verbatim rule forbids. WHAT THE RULING DELIBERATELY DOES NOT DECIDE, and what is therefore '
     'ROWED rather than folded in here: whether the live competition design owes the two gates\' '
     'CONCERNS is a phase-3 fix-plan input (D-231), at OPEN_ITEMS.md OI-365. FORMER VERDICT, '
     'PRESERVED (#12): `undetermined`, on the ground that the rule this constrains — dissolving the '
     'post-hoc correction layer into the competition — is D-429, whose principle a user ruling DID '
     'carry to the live design, and that whether the carve-out rides across with it or was scoped to '
     'a legacy dissolution that never ran was a ruling and not a session\'s call; the user held the '
     'cell explicitly at Ruling 23 of `cowork_rulings_2026_08_09_fourth_stop.md` pending Ruling 27\'s '
     'fact-gathering pass, so that state was a RULED one and not an unfinished one. THE FACT THAT '
     'DECIDED IT, located in that pass rather than assumed: D-429\'s carrying ruling states its own '
     'scope as the phase-3 candidate-admission and emission family, and the gate layer is not a '
     'member of it.'),
    ('D-583', 'A known deferred loss is KEPT only while it stays characterized EXACTLY, and '
     're-adjudicated when its form changes',
     'false-negative-path', ['JKEY_WIRING_FLAG', 'JKEY_NO_REEMIT', 'BATCH_LEGACY_DEFAULT'],
     'none-found',
     'The characterized loss sits on the legacy region path behind a SECOND default-OFF flag — the '
     'same anchors this pass gives D-278, the shelved step it defers to. ONE THING THE RECORD STATES '
     'AND THE VERDICT DOES NOT CREDIT: its provenance says "the CONDITION it states is general", '
     'while the behaviour it characterizes is legacy. Under bound (i) a general condition no ruling '
     'carries is `none-found` — but a reader should not take the condition itself for legacy-scoped, '
     'and that is said here rather than folded into a verdict.'),
]

# ── RETIRED SUBJECTS — verdicts whose subject entry has left the LIVE register ───────────
#
# WHY THIS SECTION EXISTS (user, 2026-08-16, §6 kind 2 of
# `cowork_rulings_2026_08_16_preparation_return.md`).  The ruled soft-discard retires a
# register entry from the LIVE record into the data file's retired-entries block — retired,
# never destroyed (#12), and individually revivable.  A verdict whose subject entry is retired
# is no longer a verdict about the derived marked set, and this tool STOPS on authored verdicts
# for entries that are NOT in that set, which is that guard working.  The ruled treatment is
# neither to delete the verdict (#12 forbids it) nor to switch the check off (#19's
# silent-failure direction): it MOVES here, verbatim, with the subject reference it was
# authored against, and the check keeps watching the live marked set.
#
# NOTHING HERE IS RE-AUTHORED, RE-READ OR RE-GRADED.  Each row is the six-part tuple exactly as
# it stood in VERDICTS.  Nothing counts it: no tally, no anchor-use check and no comparison
# against the registered prediction reads this list.
#
# MEMBERSHIP IS DERIVED, NOT AUTHORED: `gen_retired_subject_moves.py` derives which verdicts
# belong here from the data file's own retired block and re-verifies this section in BOTH
# directions on every run.  A subject in both sections, in neither, or on the wrong side halts
# that derivation.
RETIRED_VERDICTS_RETIREMENT = (
    "CC, dispatch `cc_instruction_preparation_fifth.md` Task 1, executing the user's rulings "
    "of 2026-08-16 — §3 the soft-discard, §4 its reach, §6 the STANDING checks' treatment. "
    "Every subject entry below was SOFT-DISCARDED into the decisions register's "
    "retired-entries block: a provenance verdict, not a judgment on soundness or usefulness. "
    "Each verdict is moved here whole; if an entry is ever revived, its verdict is read back "
    "into VERDICTS deliberately rather than resurrected by this copy."
)

RETIRED_VERDICTS = [
    ('D-051', 'The legacy Layer-3 sequence decoder as the production key path',
     'false-negative-path', ['L3_LEGACY_ENTRY', 'L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found',
     'ARCHITECTURE.md:1414 cites it only as the precedent SHAPE for a supersession in fact, not as a '
     'principle carried across.'),
    ('D-052', 'The shared signature-read + declared-mode function (resolveKeySignatureContext)',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found',
     'OBSERVATION, not a mark error: the joint fact adapter performs its OWN signature and '
     'declared-mode read (JOINT_SIG_READ), so the "ONE shared function" property D-052 records does '
     'not extend across the live path. Whether that is a #6 duplication of concern or two different '
     'concerns is not settled here.'),
    ('D-059', 'The legacy key window — 16 beats back, 8 forward, decayed',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-060', 'The legacy chord analyzer\'s vertical-only boundary',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'undetermined',
     'The boundary rule is #7 applied to the legacy analyzer. Whether the live estimator inherits a '
     'boundary statement of the same kind was not established this wave; no ruling names D-060.'),
    ('D-061', 'The Baroque-calibrated gate thresholds and the never-widen rule',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'undetermined',
     'CLAUDE.md\'s gate-threshold policy states the same prohibition as a STANDING instruction, and '
     'D-423 names it as one of three holding "for the whole programme" — while D-423 is itself '
     'LEGACY-marked. Whether the prohibition reaches the live design is a ruling the record does not '
     'contain.'),
    ('D-062', 'Withholding progression signals during segmentation',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-063', 'The tick-local path\'s cold-context contract',
     'false-negative-path', ['FLAG_DEFAULT', 'NOTE_SEAM_RECORD', 'NOTE_SEAM_LEGACY', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-064', 'The chord-scoring presets as a measurement-tool-only artifact',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT'],
     'none-found',
     'Production inference is preset-independent (CLAUDE.md gate block (A)), so the presets have no '
     'production consumer at all — which is the same conclusion the entry\'s superseded-in-fact status '
     'already records.'),
    ('D-065', 'The deliberate look-ahead divergence between the measurement tool and the app',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'NOTE_SEAM_LEGACY'],
     'none-found', ''),
    ('D-089', 'The legacy 0.5 / 0.8 confidence exposure gates',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'RECORD_EXPOSURE', 'BATCH_LEGACY_DEFAULT'],
     'none-found',
     'The record arm declares its own constant on its own gap scale (RECORD_EXPOSURE) rather than '
     'reusing these, which is why the entry is superseded-by rather than transferred.'),
    ('D-101', 'Restricting contextual inversion bonuses to major and minor candidates',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-102', 'Extending the inversion bonuses to augmented and half-diminished candidates',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-104', 'Conditioning the bass-is-root bonus on corroborating support',
     'false-negative-path', ['NOTE_SEAM_LEGACY', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-214', 'The dim7 characteristic bonus as the rotation selector',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-216', 'The stepwise-bass bonus\'s four load-bearing gates',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-217', 'Suppressing every context-dependent bonus during segmentation',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found',
     'The same rule as D-062 at a second home; its specification home is D-062 by the entry\'s own text.'),
    ('D-218', 'Deriving every template-sized array extent from one constant',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-219', 'The removal of Gates B/C/D and the standing bar on a temporal condition in the flip',
     'false-negative-path', ['FM2_FLIP', 'BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found',
     'Split subject: the three removed gates are gone, but the flip the standing half constrains '
     'survives at HEAD as FM2, so the prohibition governs code that exists.'),
    ('D-235', 'The bound on what tonal-centre disambiguation may overturn',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-243', 'The planning band for the vertical engine and the corpora excluded from it',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'L4_SPEC_DORMANT'],
     'none-found',
     'The subject is the engine the band bands. Status superseded-in-fact — the production surface is '
     'measured on the robust unit, not this band.'),
    ('D-346', 'The union-of-stretch-bests candidate set for the whole-run tonality decision',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-350', 'The whole-run margin as the published key confidence',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found',
     'Its citations outside the register mechanics are all tooling discussions of home classification, '
     'not rulings about its content.'),
    ('D-354', 'The exhaustion of the key/mode decoder\'s private settings',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT'],
     'none-found', ''),
    ('D-355', 'The scale-membership term as the identified key/mode lever',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found',
     'The lever is a term in the legacy shared key scorer, and the wiring step it was to be applied at '
     'is the legacy one.'),
    ('D-356', 'The brittleness of the leading-note presence gate',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT', 'TESTS_KEY'],
     'none-found', ''),
    ('D-357', 'Reading notated spelling as tonality evidence at the function layer',
     'none', ['L5_DIAG_ONLY', 'L3_SPEC_DORMANT'],
     'none-found',
     'Not built on either layer — the decision places the evidence at a layer that is itself dormant.'),
    ('D-378', 'Re-deciding a chord under a different tonality, well-defined only on the decoder path',
     'none', ['JKEY_NO_REEMIT', 'JKEY_WIRING_FLAG'],
     'assigns-live-work',
     'The naive re-emit is not built — the wiring leaves the chord as the production chord. The entry '
     'names the decoder path as where the question IS well defined.'),
    ('D-402', 'The inversion-append as a cap artifact, and the surviving bass promotion',
     'false-negative-path', ['BATCH_LEGACY_DEFAULT', 'TESTS_CHORD'],
     'none-found', ''),
    ('D-405', 'Keeping the full ranked key resolve as a segmentation seed',
     'false-negative-path', ['L3_SPEC_DORMANT', 'BATCH_LEGACY_DEFAULT'],
     'none-found', ''),
    ('D-579', 'The anchor obligation: compute the chord ONCE against its region\'s FINAL notes, with '
     'tonality an explicit input',
     'none', ['BATCH_JOINT', 'RECORD_SECTION'],
     'carried-elsewhere',
     'Reach `none` on this pass\'s own D-215 precedent — the obligation was never executed on the path '
     'it was written for, so nothing at HEAD implements the subject. Its two anchors are the '
     'production-path anchors, and they are the evidence for the transfer as much as for the reach: '
     'the record states the obligation "was met by replacement rather than by repair" — the live arm '
     'is one joint decode over key, mode, chord and segmentation together (D-001), which is the '
     'ordering this step asked for, reached by a different route.'),
]

# ── A side finding this wave met while tracing the two production surfaces ───────────────
# Comments that still describe the record arm as OFF or uncalled, contradicting the default
# at composingconfiguration.cpp:178 and their own call sites. Located, never hand-counted
# (#17f); the count is derived from this list's length.
# ★ THIS SIDE FINDING IS DISCHARGED IN `src/`, AND ITS TABLE IS RETIRED RATHER THAN DELETED (#12,
# D-648) — CC, `cc_instruction_return_continuation_8.md` Task 4, on the user's Ruling 16 of
# 2026-08-09.  Five of the six sites below were CORRECTED by that ruling's one comment-only commit,
# so their quotes are gone and this tool STOPPED on the first of them with "the premise has
# changed" — that guard working.  The former table is kept whole here as the record of what the
# finding named; the LIVE table below carries only what still stands.
#
# ★ THE SIXTH WAS NOT DISCHARGED BY THAT ACT, AND IT IS NOW.  FORMER TEXT OF THIS PARAGRAPH,
# PRESERVED (#12) — true when it was written, and made false by the user's Ruling 48 rather than
# wrong: "★ THE SIXTH IS NOT DISCHARGED AND IS NOT SILENTLY DROPPED: `tools/batch_analyze.cpp` still
# says the notation layer stays on the legacy analysis, which the 2026-07-27 notation switch made
# false.  It is OUTSIDE Ruling 16's stated scope — that ruling licenses ONE comment-only `src/`
# commit, and a measurement tool is neither `src/` nor a build file — so it is left standing and
# surfaced, not edited.  It is also outside the enumerated family the Ruling-16 sweep derives
# (`tools/audit/arm_comment_sweep.json`), whose scan is `src/` by the same scope."
STALE_RECORD_ARM_COMMENTS_RETIRED_2026_08_09 = [
    ('src/notation/internal/notationcomposingbridge.cpp', 719,
     'Record arm (default OFF, useJointNotationRecord)'),
    ('src/notation/internal/notationcomposingbridge.cpp', 1485,
     'Record path (default OFF, useJointNotationRecord)'),
    ('src/notation/internal/notationimplodebridge.cpp', 1408,
     'Record path (default OFF, useJointNotationRecord)'),
    ('src/notation/internal/notationtuningbridge.cpp', 765,
     'record path default OFF, useJointNotationRecord'),
    ('src/composing/analysis/section/sectionrecordadapter.cpp', 26,
     'DORMANT'),
]

# ★ THE SIXTH SITE, RETIRED 2026-08-11 — its own table, one per act, as the five above are (#12,
# D-648).  CC, `cc_instruction_return_continuation_9.md` Task 0, on the user's RULING 48 of
# `cowork_rulings_2026_08_09_ninth_stop.md`, which licenses exactly this one comment-only edit: the
# stale claim is the OI-353 falsity class and sat outside Ruling 16's enumerated family ONLY by
# living under `tools/`.  The comment now says the staging is CLOSED on both production surfaces and
# keeps apart the thing that is NOT closed — this flag's own default, which is still OFF.  The quote
# below is therefore gone from the file, and this tool STOPPED on it with "the premise has changed",
# which is the same guard working that found the sweep's own missed member one act earlier.
STALE_RECORD_ARM_COMMENTS_RETIRED_2026_08_11 = [
    ('tools/batch_analyze.cpp', 4916,
     'notation layer stays on the legacy analysis'),
]

# ★ A SEVENTH SITE THIS ENUMERATION NEVER HELD, FOUND 2026-08-11 AND CORRECTED THE SAME DAY — and it
# is recorded as a MISS rather than as a retirement, because it never entered the live table and so
# never left it.  CC, `cc_instruction_return_continuation_12.md` Task 3 found it by VERIFYING
# OPEN_ITEMS.md OI-303's six named sites AT THE FILES, which is the only way it becomes visible; the
# correction is `cc_instruction_return_continuation_13.md` Task 0, on the user's RULING 59 of
# `cowork_rulings_2026_08_11_thirteenth_stop.md`.  THE SAME CLAIM stood at a SECOND block of the SAME
# file the Ruling-48 act had just corrected, so for two days that one file said both that the in-app
# notation layer stays on the legacy analysis and that the staging is closed on both production
# surfaces — worse for a reader than the single false claim the finding was opened for.  Rowed at
# OPEN_ITEMS.md OI-368.
STALE_RECORD_ARM_COMMENTS_MISSED_AND_CORRECTED_2026_08_11 = [
    ('tools/batch_analyze.cpp', 4657,
     'the in-app NOTATION layer stays on the legacy analysis'),
]

STALE_RECORD_ARM_COMMENTS: list[tuple[str, int, str]] = []

# The two dated annotations that still assert the opposite of D-428 as corrected at phase 1n.
D428_CONTRADICTIONS = [
    ('cowork_stage5_fitter_design.md', 116, 'their subject includes live Layer-1.5 code'),
    ('cowork_structural_integrity_audit.md', 323, 'whose subject includes live Layer-1.5 code'),
]

# ── When the set last changed (Task 1.2, the reason the recorded 80 is stale) ────────────
SET_HISTORY = {
    'how_this_was_established': 'Read-only git OBJECT queries by explicit commit hash, walking parents '
                               'from the hashes in this session\'s own start-of-session commit report '
                               '(CLAUDE.md, the working-tree-files rule). Content-addressed reads only '
                               '— no branch-tip or index read was trusted.',
    'phase_1m_self_check_correction': {'sha': 'd5f3181beaf2425ab42c1ca66c3a1a34acd41b19',
                                       'decisions': 429, 'marked': 80},
    'phase_1n': {'sha': 'db119807f1020869fe683039f0f3f3c42605f064', 'decisions': 431, 'marked': 81},
    'what_changed': 'D-428 gained the mark at phase 1n, when its classification was corrected against '
                    'the OI-165 premise. Nothing lost the mark.',
    'so': 'OI-289\'s "80" was TRUE when it was written and has been stale by one since the next wave. '
          'The row is not wrong about its method — it says to re-derive — it is stale about its number, '
          'which is the failure shape it names.',
}


def read_lines(rel):
    p = ROOT / rel
    if not p.exists():
        raise Stop('cited file does not exist: %s' % rel)
    return p.read_text(encoding='utf-8', errors='strict').splitlines()


def locate(rel, line, quote, what):
    """Verify `quote` sits at `line` of `rel` (1-indexed). Returns the located line text."""
    lines = read_lines(rel)
    if line is not None:
        if line < 1 or line > len(lines):
            raise Stop('%s: cited line %s is outside %s (%d lines)' % (what, line, rel, len(lines)))
        if quote in lines[line - 1]:
            return {'file': rel, 'line': line, 'line_text': lines[line - 1].strip()}
        # A quote that has MOVED is reported with where it now is, so the fix is one edit.
        found = [i + 1 for i, t in enumerate(lines) if quote in t]
        raise Stop('%s: quote not at %s:%d. %s' % (
            what, rel, line,
            ('It is now at line(s) %s — re-aim the citation.' % found) if found
            else 'It is nowhere in the file — the premise has changed.'))
    found = [i + 1 for i, t in enumerate(lines) if quote in t]
    if not found:
        raise Stop('%s: quote not found anywhere in %s' % (what, rel))
    return {'file': rel, 'line': found[0], 'line_text': lines[found[0] - 1].strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='re-derive and verify every citation; do not write the artifact')
    args = ap.parse_args()

    # ── A1, checked before the derivation rests on it ────────────────────────────────────
    a1 = []
    for line, quote in A1_GENERATOR_QUOTES:
        a1.append(locate('tools/audit/decisions/gen_decisions_register.py', line, quote,
                         'A1 (the marker is generated text)'))

    # ── Task 1.1 — DERIVE the set ────────────────────────────────────────────────────────
    data = json.loads(BACKBONE.read_text(encoding='utf-8'))
    decisions = data['decisions']
    marked = [d for d in decisions if d.get('legacy_subject')]
    marked_ids = [d['id'] for d in marked]
    transfer_variant = [d['id'] for d in marked if d.get('legacy_principle_transferred')]

    # ── The authored table must cover the derived set exactly ────────────────────────────
    verdict_ids = [v[0] for v in VERDICTS]
    retired_verdict_ids = [v[0] for v in RETIRED_VERDICTS]
    retired_entry_ids = {r['the_entry']['id']
                         for r in data.get('retired_entries', {}).get('entries', [])}
    if len(verdict_ids) != len(set(verdict_ids)):
        raise Stop('the authored verdict table has a duplicate id')
    if len(retired_verdict_ids) != len(set(retired_verdict_ids)):
        raise Stop('the RETIRED verdict table has a duplicate id')
    # A verdict in BOTH sections would be two copies free to drift apart; a verdict in NEITHER is
    # the ruled STOP — the check must not be able to lose a judgment because its subject went away.
    both = sorted(set(verdict_ids) & set(retired_verdict_ids))
    if both:
        raise Stop('verdicts carried in BOTH the live table and RETIRED_VERDICTS: %s'
                   % ', '.join(both))
    missing = [i for i in marked_ids if i not in set(verdict_ids)]
    if missing:
        raise Stop('derived entries with NO authored verdict (the tool will not guess one): %s'
                   % ', '.join(missing))
    extra = [i for i in verdict_ids if i not in set(marked_ids)]
    if extra:
        raise Stop('authored verdicts for entries that are NOT in the derived marked set: %s'
                   % ', '.join(extra))
    # The retirement STOP in the OTHER direction, on the delegation bar's established pattern.
    resurrected = [i for i in retired_verdict_ids if i in set(marked_ids)]
    if resurrected:
        raise Stop('RETIRED verdicts for entries that are in the derived marked set again: %s — '
                   'read the verdict back into VERDICTS rather than relying on the retired copy'
                   % ', '.join(resurrected))
    orphaned = [i for i in retired_verdict_ids if i not in retired_entry_ids]
    if orphaned:
        raise Stop('RETIRED verdicts for entries the decisions register carries neither live nor '
                   'retired, so the subject cannot be placed at all: %s' % ', '.join(orphaned))

    # ── Every anchor located at the object ───────────────────────────────────────────────
    anchors_out = {}
    for key, a in ANCHORS.items():
        loc = locate(a['file'], a['line'], a['quote'], 'anchor %s' % key)
        anchors_out[key] = {**loc, 'says': a['says']}

    used = set()
    for v in VERDICTS:
        for k in v[3]:
            if k not in ANCHORS:
                raise Stop('verdict %s cites unknown anchor %s' % (v[0], k))
            used.add(k)
    unused = sorted(set(ANCHORS) - used)

    # ── Recorded figures located ─────────────────────────────────────────────────────────
    figures = []
    for f in RECORDED_FIGURES:
        loc = locate(f['where'], f['line'], f['quote'], 'recorded figure %s' % f['figure'])
        figures.append({'recorded_figure': f['figure'], 'located_at': loc, 'note': f['note'],
                        'derived_count': len(marked_ids),
                        'discrepancy': len(marked_ids) - f['figure']})

    # ── The two side findings, located ───────────────────────────────────────────────────
    stale = [locate(f, ln, q, 'stale record-arm comment')
             for f, ln, q in STALE_RECORD_ARM_COMMENTS]
    d428 = [locate(f, ln, q, 'D-428 contradiction')
            for f, ln, q in D428_CONTRADICTIONS]

    the_test = dict(THE_TEST)
    the_test['source_located'] = locate(THE_TEST['source']['file'], THE_TEST['source']['line'],
                                       THE_TEST['source']['quote'], 'the test')

    # ── Counts ───────────────────────────────────────────────────────────────────────────
    def tally(idx):
        out = {}
        for v in VERDICTS:
            out[v[idx]] = out.get(v[idx], 0) + 1
        return dict(sorted(out.items(), key=lambda kv: -kv[1]))

    reach = tally(2)
    transfer = tally(4)
    bears_on_live = sum(c for k, c in transfer.items()
                        if k in ('ruling-transferred', 'live-prohibition-in-spec',
                                 'carried-elsewhere', 'assigns-live-work'))

    entries = [{'id': v[0], 'subject': v[1], 'reachability': v[2], 'anchors': v[3],
                'transfer': v[4], 'note': v[5],
                'carries_transfer_variant_in_the_data': v[0] in transfer_variant}
               for v in VERDICTS]

    artifact = {
        'what_this_is': __doc__.strip().split('\n\n')[1].replace('\n', ' '),
        'generated_by': 'tools/audit/decisions/gen_phase1w_legacy_verification.py',
        'row': 'OPEN_ITEMS.md OI-289',
        'dispatch': 'cc_instruction_phase1w_legacy_mark_verification.md',
        'assumption_A1_the_marker_is_generated_text': {
            'claim': 'The LEGACY marker is one generated wording emitted for every entry carrying the '
                     'data field `legacy_subject`, with a second variant for '
                     '`legacy_principle_transferred` — so the set is DERIVABLE from the data rather '
                     'than findable by searching prose.',
            'verdict': 'HELD — established at the generator that emits it, before the derivation below '
                       'rested on it.',
            'located': a1,
        },
        'derived_set': {
            'count': len(marked_ids),
            'ids': marked_ids,
            'carrying_the_transfer_variant': transfer_variant,
            'register_size_at_this_tree': len(decisions),
            'derivation': "every decision in backbone_decisions.json whose `legacy_subject` field is "
                          "truthy; no figure in the record is used or quoted (D-431, and OI-289's own "
                          "instruction to re-derive).",
        },
        'retired_subjects': {
            'what_this_is': 'Verdicts whose subject entry was SOFT-DISCARDED out of the LIVE '
                            'record on 2026-08-16 (the user\'s ruling §3, its reach §4, the '
                            'STANDING checks\' treatment §6). Each is carried WHOLE, in the words '
                            'it was authored in, and is neither re-read nor re-graded (#12). '
                            'NOTHING COUNTS IT: the derived set, the tallies, the anchor-use '
                            'check and the comparison against the registered prediction are the '
                            'LIVE marked set\'s.',
            'the_retirement': RETIRED_VERDICTS_RETIREMENT,
            'membership_is_derived': 'tools/audit/decisions/gen_retired_subject_moves.py derives '
                                     'which verdicts belong here from the data file\'s own '
                                     'retired block and re-verifies this section in both '
                                     'directions.',
            'the_stop_in_the_other_direction': 'A retired subject that is in the derived marked '
                                               'set again halts this tool until the verdict is '
                                               'read back into VERDICTS deliberately.',
            'count': len(retired_verdict_ids),
            'verdicts': [{'id': v[0], 'subject': v[1], 'reachability': v[2], 'anchors': v[3],
                          'transfer': v[4], 'note': v[5]} for v in RETIRED_VERDICTS],
        },
        'recorded_figures_that_do_not_match': figures,
        'when_the_set_last_changed': SET_HISTORY,
        'the_test': the_test,
        'the_prediction': THE_PREDICTION,
        'evidence_anchors': anchors_out,
        'anchors_declared_but_unused': {
            'why_they_exist': 'These anchors establish the two PRODUCTION paths themselves — what the '
                              'record arm and --joint-inference actually call — rather than any one '
                              'entry\'s subject. Every per-entry verdict rests on them collectively: '
                              'the reason no marked subject is reachable on a production path is that '
                              'these paths were traced and none of them enters the legacy scorer or '
                              'the legacy key layer. They are listed separately rather than attached '
                              'to every row of derived_set.ids, and they are located at the object '
                              'exactly like the cited ones, so a change to any of them stops this '
                              'tool. (The former wording named a row count, which the 2026-08-09 '
                              'application of the OI-354 verdict set made stale; it is replaced by a '
                              'pointer to the derived list rather than re-typed, D-431.)',
            'keys': unused,
        },
        'entries': entries,
        'counts': {
            'reachability': reach,
            'transfer': transfer,
            'entries_whose_transfer_half_bears_on_live_work': bears_on_live,
        },
        'prediction_outcome': {
            'reachability': 'HELD in shape. 0 entries reachable on a default production path except '
                            'the single partial case D-055 (a preference registration, not an '
                            'inference path); the large majority reached only by an enumerated '
                            'non-default path; a minority with no code at all; and 0 UNDETERMINED, at '
                            'the bottom of the predicted 0-3 band.',
            'transfer': 'PARTLY REFUTED, and the refutation is the finding. The prediction expected 2 '
                        'ruling-transfers (correct) and 3-8 entries whose own text assigns live work '
                        '(correct — the count is in counts.transfer above). It did NOT predict the '
                        'largest class: entries the LIVE layer specification restates as standing '
                        'do-not-retry prohibitions. That class was not in the prediction at all, and '
                        'it is several times the size of the ruling-transfer class the row was opened '
                        'on. (The two figures formerly typed into this sentence were true of the '
                        'population as it stood at phase 1w and were made stale by the 2026-08-09 '
                        'application of the OI-354 verdict set; they are replaced by pointers to the '
                        'computed tally rather than re-typed, D-431.)',
            'marks_established_wrong': 'HELD — 0. See corrections_made.',
        },
        'corrections_made': {
            'count': 0,
            'why': 'Task 4 licenses correcting a mark this wave ESTABLISHES wrong, on the D-311 '
                   'precedent. This wave establishes none wrong: on the test the surviving mark '
                   'actually makes — what the decision is ABOUT — every one of the derived entries is '
                   'about the dormant pipeline. The one candidate, D-055, turns on a scoping judgment '
                   '(are the mode-prior preferences themselves legacy-scoped?) that is not a code '
                   'fact, so it is reported and the mark stands.',
            'convention_in_question': 'NO. Task 4\'s last clause fires if the failure rate puts the '
                                      'marking convention in question; the failure rate is zero. What '
                                      'the wave found instead is about what a mark does NOT say, which '
                                      'is the thing the 2026-08-03 weakening already ruled.',
        },
        'what_this_found': {
            'the_dormancy_is_weaker_than_it_sounds': (
                'No entry earned the "unreachable at any setting" verdict for the notation flag alone, '
                'and none earned "flag-default-only". Every marked subject that HAS code at HEAD is '
                'reached by something: plain batch_analyze (the --joint-inference flag defaults OFF, '
                'so the corpus instrument runs the legacy pipeline unless told otherwise), a '
                'batch_analyze diagnostic dump flag, or the test suites. A change to any of these '
                'subjects still breaks tests and still moves what an untagged batch_analyze run '
                'produces. "Dormant" means "not what the product runs", not "nothing runs it".'
            ),
            'the_false_negative_enumeration_is_short_by_one': (
                'OI-289 enumerates four false-negative paths: an explicit flag flip, batch_analyze '
                'without --joint-inference, the test suites, and the declared non-production uncached '
                'path. A fifth is load-bearing here: batch_analyze\'s DIAGNOSTIC DUMP FLAGS, which '
                'reach code neither production surface reaches and plain batch_analyze does not '
                'either — the Layer-4 slice decoder (--decode-chords) and the whole Layer-5 function '
                'module (--dump-l5, --dump-fullspine). ARCHITECTURE.md:1339 already names this path '
                'for Layer 3 ("the remaining callers are the batch_analyze diagnostics"); OI-289\'s '
                'list does not.'
            ),
            'a_second_flag_gates_reachability': (
                'The reachability picture is not one flag. jointKeyWiringEnabled() '
                '(regionanalyzer.cpp:1484) is a second runtime flag, default OFF, gating the built '
                'half of the shelved joint key-and-chord step INSIDE the legacy arm. A verdict of the '
                'form "reachable when the notation flag is flipped" would be wrong for those subjects '
                'without also naming this one.'
            ),
            'the_largest_transfer_class_was_not_the_predicted_one': (
                'The largest transfer class — its size is counts.transfer["live-prohibition-in-spec"] '
                'above, not typed here (D-431) — is entries restated by a LIVE specification section '
                'as standing do-not-retry prohibitions, on the chord layer, the key layer, the search '
                'and, since 2026-08-09, the declared mode\'s weight; docs/redesign_plan.md:4 '
                'states the distinction in its own words: "LIVE prohibitions about the legacy chord '
                'path". The mark is RIGHT about the subject and the entry still binds what a future '
                'designer may attempt. That is a third thing a mark can be, beside "about live code" '
                'and "about dead code", and the register has no field for it.'
            ),
            'entries_that_describe_an_arrangement_the_live_system_does_not_have': (
                'Three cases where a reader could take a marked entry for a description of what runs: '
                'D-345 (the style preset enters at the key/mode layer — production inference is '
                'preset-independent, so on the live arm the preset has no entry point at all), D-351 '
                '(the key search is its own decoder — the live estimator decides key and chord in ONE '
                'decode), and D-052 (the signature read lives in one shared function — the joint fact '
                'adapter does its own). None is a wrong mark. All three are why the mark exists.'
            ),
            'no_marked_id_is_cited_anywhere_under_src': (
                'The citation scan found not one occurrence of a marked decision ID in any .cpp or .h '
                'file. Nothing in the code points back at the decisions that govern it, in either '
                'direction, so the transfer half could only ever be searched in prose.'
            ),
        },
        'findings_rowed_elsewhere': {
            'stale_record_arm_comments': {
                'what': 'Comments in src/ and tools/ that still describe the record arm as "default '
                        'OFF", or the record section adapter as having no src/ caller, contradicting '
                        'the default at composingconfiguration.cpp:178 and their own call sites. Each '
                        'still standing is located below.',
                'the_former_wording_preserved_12': (
                    'Its last clause read "Each is located below; correcting them is a src/ change, '
                    'which this wave forbids." True of the wave that wrote it and false now: the '
                    'user licensed the corrections in two acts, Ruling 16 for the five under src/ '
                    'and Ruling 48 for the sixth under tools/.'),
                '★_this_side_finding_is_DISCHARGED_WHOLE': (
                    'All six sites are corrected and the live list is EMPTY. The five under `src/` '
                    'were corrected 2026-08-09 under the user\'s Ruling 16 (one comment-only `src/` '
                    'commit); the sixth, under `tools/`, was corrected 2026-08-11 under the user\'s '
                    'Ruling 48, which licensed exactly that edit because the site sat outside '
                    'Ruling 16\'s enumerated family ONLY by living under `tools/`. Both retired '
                    'tables are kept whole in this file\'s source rather than deleted (#12, D-648), '
                    'one per act, so what the finding named survives the act that closed it. An '
                    'EMPTY count here is therefore a discharge and not a search that found '
                    'nothing.'),
                '★_ADVISORY_WITH_UNMEASURED_REACH_—_a_bound_STATED_not_a_claim_withdrawn': {
                    'the_ruling': (
                        'User, 2026-08-11, Ruling 59 of '
                        '`cowork_rulings_2026_08_11_thirteenth_stop.md`. Nothing above is '
                        'withdrawn: the discharge is true of the sites this enumeration HOLDS, '
                        'and what follows bounds what that is worth.'),
                    'the_bound': (
                        'This enumeration is an AUTHORED table whose members were found by a '
                        'session reading, and its REACH against the text it scans has never been '
                        'measured. It re-locates each member it holds on every run, which is the '
                        'right construction for the members it holds — and it looks for no new '
                        'ones. So an EMPTY live table bounds nothing about the class, and this '
                        'block is ADVISORY. That is D-436\'s detection condition and D-661\'s '
                        'completeness rule both unmet for this pattern, stated rather than left '
                        'to be discovered.'),
                    'the_instance_that_proves_it': (
                        'While this block read empty, a SEVENTH site carrying the same claim stood '
                        'at a second block of the very file the sixth\'s correction had touched — '
                        'so one file stated both readings for two days. It was found by VERIFYING '
                        'OI-303\'s named sites at the FILES rather than at the record of them, and '
                        'is at STALE_RECORD_ARM_COMMENTS_MISSED_AND_CORRECTED_2026_08_11 in this '
                        'file\'s source. It is corrected under the same ruling, so the class is '
                        'empty at HEAD by act as well as by table.'),
                    'why_no_detection_measurement_is_SEEDED_for_it': (
                        'The ruling\'s own ground: establishment is spent where an ANALYSIS '
                        'DECISION consumes it, and no analysis decision consumes a comment sweep. '
                        'Measuring this pattern\'s reach would buy a bound on a class of '
                        'statements ABOUT the build state, which no measurement of the analysis '
                        'reads and no gate depends on. The obligation is therefore DISCHARGED BY '
                        'STATING THE BOUND, not by leaving a measurement owed forever.'),
                    'the_sibling_shape': (
                        'OPEN_ITEMS.md OI-367 is the same shape one measurement tool over — a '
                        'family enumerated by a pattern nobody measured, found because a later act '
                        'derived or verified its own population. OI-368 carries this one.'),
                },
                'count': len(stale),
                'located': stale,
            },
            'two_annotations_contradict_the_corrected_D_428': {
                'what': 'Both were written 2026-08-03 at phase 1m and both assert that the owed '
                        'iteration-API renames have a subject including LIVE Layer-1.5 code. D-428 was '
                        'corrected later the same day (phase 1n) against the OI-165 premise and now '
                        'says every use sits on the legacy arm, so deleting that path discharges it. '
                        'The correction reached the register and not these two documents.',
                'count': len(d428),
                'located': d428,
            },
        },
    }

    if args.check:
        print('phase1w: A1 held; %d entries derived; %d anchors located; %d recorded figures located'
              % (len(marked_ids), len(anchors_out), len(figures)))
        return 0

    OUT.write_text(json.dumps(artifact, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('phase1w: wrote %s' % OUT.relative_to(ROOT).as_posix())
    print('  derived marked set: %d (register %d)' % (len(marked_ids), len(decisions)))
    print('  reachability: %s' % ', '.join('%s=%d' % kv for kv in reach.items()))
    print('  transfer:     %s' % ', '.join('%s=%d' % kv for kv in transfer.items()))
    print('  entries whose transfer half bears on live work: %d' % bears_on_live)
    print('  marks corrected: 0')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Stop as e:
        print('STOP: %s' % e)
        sys.exit(2)
