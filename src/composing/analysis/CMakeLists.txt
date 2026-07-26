# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

muse_create_module(composing_analysis NO_QT)

target_sources(composing_analysis PRIVATE
    # types/ — LEAF cross-layer value types (Phase-5 audit-Q2 refactor). Depends on
    # nothing from chord/ or key/ (STL only), so the L1.5 engravingbridge and L3 key
    # headers compile without the L4 chord headers — killing the two type-only header
    # back-edges. Pure relocation, byte-identical. See cowork_types_header_design.md.
    ${CMAKE_CURRENT_LIST_DIR}/types/analysistypes.h

    # param/ — Stage-5 fitter: the OPTIONAL flag-gated parameter-override mechanism
    # (design D-6 / A-6). A by-name registry of the scoring pipeline's mutable global
    # constants + a strict line-based override loader, read once at analysis-binary
    # startup (batch_analyze --param-override). Byte-identical when no override is
    # loaded (the loader is the only writer). Depends only on the types leaf + STL.
    # See cowork_stage5_fitter_design.md + cc_stage5_phase1_report.md.
    ${CMAKE_CURRENT_LIST_DIR}/param/paramoverride.h
    ${CMAKE_CURRENT_LIST_DIR}/param/paramoverride.cpp

    # chord/ — chord analysis, formatting, voicing
    ${CMAKE_CURRENT_LIST_DIR}/chord/analysisutils.h
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordanalyzer.h
    # OI-168 measurement scaffolding — default-OFF counters + the signature-mask A/B variant.
    ${CMAKE_CURRENT_LIST_DIR}/chord/keycollectionprobe.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/keycollectionprobe.h
    # Refactor #1 — single-responsibility layer TUs split out of chordanalyzer.cpp
    # (byte-identical pure code movement). See cc_refactor1_split_design_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordsymbolformatter.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordvoicing.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/chorddiagnose.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordpostpasses.cpp
    ${CMAKE_CURRENT_LIST_DIR}/chord/postscoringgates.cpp
    # LAYER 4 (Increment A) — the per-slice CHORD-SYMBOL decoder: runs the existing
    # chord scorer over each Layer-2 slice's window and reads the complete candidate
    # cube it surfaces (the L3 pattern), producing one chord + ranked alternatives +
    # confidence + uncertain per slice. ISOLATED this increment: built + unit-tested
    # + graded against the held-out chord GT, NOT wired into the live pipeline —
    # production output byte-identical; it runs only under batch_analyze
    # --decode-chords. Membership / spelling-pin / new types are later increments.
    # See cowork_layer4_chordsymbol_design.md + cc_layer4_audit_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordslicedecoder.h
    ${CMAKE_CURRENT_LIST_DIR}/chord/chordslicedecoder.cpp

    # function/ — Phase E harmonic function layer (post-analysis pass between
    # analyzeChord() output and the final chord label). E1 is a pass-through
    # shell; E2/E3/E4 migrate progression signals, post-scoring gates, and
    # cadence detection out of chordanalyzer.cpp. See docs/scoring_model.md §10.
    ${CMAKE_CURRENT_LIST_DIR}/function/harmonicfunctionlayer.h
    ${CMAKE_CURRENT_LIST_DIR}/function/harmonicfunctionlayer.cpp

    # tonicizationlabeler — the functional layer's narrow first slice (Stage
    # 6-tonic-i; docs/stage6_functional_layer_design.md §3): a secondary-dominant
    # / applied-leading-tone labeling pass over the decoded chord+key path,
    # distinct from harmonicfunctionlayer (the chord-competition layer). Built +
    # MEASURED only; it PRODUCES a label and does NOT mutate chord/key or feed the
    # production RN output (wiring is 6-tonic-ii).
    ${CMAKE_CURRENT_LIST_DIR}/function/tonicizationlabeler.h
    ${CMAKE_CURRENT_LIST_DIR}/function/tonicizationlabeler.cpp

    # functionprogression + functionromannumeral — Architectural Layer 5 (FUNCTION),
    # Phase 5c Step 1: the progression model (the licensed-progression test +
    # prevailing-harmony / established-next-function queries over a region's
    # committed-chord stream, §5.0) and the base Roman-numeral derivation (wraps
    # diatonicDegreeForRootPc + ChordSymbolFormatter::formatRomanNumeral, §5.1).
    # DORMANT — no production consumer (exercised only by their unit tests), so
    # byte-identical on production by construction. Distinct from harmonicfunctionlayer
    # (the misnamed chord-COMPETITION pipeline). Spec: cowork_layer5_function_design.md.
    ${CMAKE_CURRENT_LIST_DIR}/function/functionprogression.h
    ${CMAKE_CURRENT_LIST_DIR}/function/functionprogression.cpp
    ${CMAKE_CURRENT_LIST_DIR}/function/functionromannumeral.h
    ${CMAKE_CURRENT_LIST_DIR}/function/functionromannumeral.cpp

    # functioncadence — Architectural Layer 5 (FUNCTION), Phase 5c Step 2: the
    # KEY-AGNOSTIC, EVENT-PAIR, feature-scored cadence detector (§5.2). Rebuilt on the
    # cadencekeyanchor key-agnostic frame + the Step-1 progression predicates, but with
    # the CORRECTED leading-tone RESOLUTION event (replacing the broken LT-presence
    # test that false-positives on I→IV) + the genuine-dominant gate + the inversion-
    # anchored typology + the cadential-6/4 collapse + the chorale phrase gate. DORMANT
    # — no production consumer (exercised only by its unit tests); the circular
    # production detectCadences() (section/sectioncadencedetection.cpp) is untouched
    # (its retirement is Phase 5d). Spec: cowork_layer5_function_design.md §5.2.
    ${CMAKE_CURRENT_LIST_DIR}/function/functioncadence.h
    ${CMAKE_CURRENT_LIST_DIR}/function/functioncadence.cpp

    # forwardoverride + functionresolver — Architectural Layer 5 (FUNCTION), Phase 5c
    # Step 3: the §8 confidence-weighted forward-override MECHANISM (the threshold +
    # the one-pass closure + the localized forward recompute — reusable; Step-4's
    # modulation recompute is its other instance) and the §5.5 RESOLVER (selects among
    # the L4-carried readings per ambiguity kind + the §5.7 bass-degree prior) + the
    # §5.5 case-4 FINE-GRAIN OVERRIDE (corrects a contradicted confident commit by
    # SELECTION, firing through forwardoverride). DORMANT — no production consumer
    # (exercised only by their unit tests). Spec: cowork_layer5_function_design.md
    # §5.5/§5.7/§8.
    ${CMAKE_CURRENT_LIST_DIR}/function/forwardoverride.h
    ${CMAKE_CURRENT_LIST_DIR}/function/forwardoverride.cpp
    ${CMAKE_CURRENT_LIST_DIR}/function/functionresolver.h
    ${CMAKE_CURRENT_LIST_DIR}/function/functionresolver.cpp

    # functionmodulation — Architectural Layer 5 (FUNCTION), Phase 5c Step 4: the
    # §5.3 TONICIZATION vs MODULATION arbiter (default-tonicize + the cadence-
    # confirmation gate + the persistence change-cost / hysteresis over duration +
    # accumulated cadential weight + the function-gated notated-spelling signal) and
    # the §5.4 CADENCE-CONFIRMED MODULATION RECOMPUTE (the §8 case-4 channel #1).
    # REUSES localmodulationdetector (the established + cadence-confirmed span
    # substrate), functioncadence (the §5.2 votes), and forwardoverride (the §8
    # mechanism — second instance). DORMANT — no production consumer (exercised only
    # by its unit tests). Spec: cowork_layer5_function_design.md §5.3/§5.4/§8.
    ${CMAKE_CURRENT_LIST_DIR}/function/functionmodulation.h
    ${CMAKE_CURRENT_LIST_DIR}/function/functionmodulation.cpp

    # functionrelationallabel — Architectural Layer 5 (FUNCTION), Phase 5c Step 5: the
    # §5.6 RELATIONAL LABELS (applied/secondary, Neapolitan, augmented sixth, modal
    # mixture) in the fixed precedence (aug6 → Neapolitan → applied → mixture, first
    # match wins; mixture is the residual), spelling-aware ONLY for the Ger6↔V7
    # distinction (engravingbridge::lineOfFifths), + the §3 UNIFIED tonicization emitter
    # (emitAppliedLabel — the ONE owned applied path subsuming the dormant
    # tonicizationlabeler [its chromatic-LT guard kept] and the inline formatRomanNumeral
    # applied path). REUSES formatRomanNumeral for the RN string (no second formatter).
    # DORMANT — no production consumer (exercised only by its unit tests); the existing
    # two paths are untouched until the joint engage (Phase 5d). Spec:
    # cowork_layer5_function_design.md §5.6/§8.
    ${CMAKE_CURRENT_LIST_DIR}/function/functionrelationallabel.h
    ${CMAKE_CURRENT_LIST_DIR}/function/functionrelationallabel.cpp

    # functionoutput — Architectural Layer 5 (FUNCTION), Phase 5c Step 6: the §7 OUTPUT
    # ASSEMBLY. Marshals the per-unit Step-1..5 products into the L5->L6 contract: the
    # full DCML Roman numeral (base RN + relational label, no simplification) + the
    # function confidence (its three fixed components — §5.2 cadence-vote weight / §5.0
    # licensed-progression fit / §5.5 margin — combined at default weights, the firewall)
    # + the open mark where unresolved; per region the local key (possibly modulated) +
    # the §5.2 cadence markers. ADDITIVE over Layer 4 (carries the committed identity, does
    # not replace it). The T/S/D read-out is NOT built (§9-D1, deferred). DORMANT — no
    # production consumer (exercised only by its unit tests). Spec:
    # cowork_layer5_function_design.md §7/§3/§9-D1.
    ${CMAKE_CURRENT_LIST_DIR}/function/functionoutput.h
    ${CMAKE_CURRENT_LIST_DIR}/function/functionoutput.cpp

    # vocabulary/ — THE HARMONIC VOCABULARY (v1): the curated reference catalog of harmonic
    # conventions (named chord PROGRESSIONS + chord SUBSTITUTIONS), queried by the analysis
    # tool (recognise/disambiguate) and a future composition tool (suggest). Holds the §5
    # in-code catalog and answers the four §4 queries — browse / recognise / suggest /
    # expand — each a ranked list of candidates carrying a structural match score; it
    # DECIDES nothing (the firewall — threshold/weighting/decision are the consumer's).
    # REUSES ChordQuality + Extension (no second quality vocabulary) and the licensed-
    # progression content (the multi-chord extension of functionprogression). DORMANT — no
    # production consumer (exercised only by its unit tests); the recognition consumer (the
    # L5 prior + L6 annotation) is a LATER step. Byte-identical on production by construction.
    # Spec: cowork_progression_schema_dictionary.md; design: cowork_progression_schema_design.md.
    ${CMAKE_CURRENT_LIST_DIR}/vocabulary/harmonicvocabulary.h
    ${CMAKE_CURRENT_LIST_DIR}/vocabulary/harmonicvocabulary.cpp

    # decode/ — chord-path decoder (Stage 3.1). Beam-1 re-expression of the greedy
    # left-to-right commit chain that analyzeRegions() threads by hand; lands behind
    # the quality-level knob with beam-1 (level 0) as the byte-identical default.
    # Header-only at 3.1. See docs/decoder_design.md and docs/scoring_model.md §11.
    ${CMAKE_CURRENT_LIST_DIR}/decode/chordpathdecoder.h

    # key/ — key and mode analysis
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodeanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodeanalyzer.h
    # Refactor — display formatters lifted out of keymodeanalyzer.cpp
    # (byte-identical pure code movement): keyModeTonicName / keyModeSuffix.
    # Both are header-declared (external linkage) and depend only on the
    # KeySigMode enum — no coupling to the anon-ns MODES/scorer cluster, which
    # stays in keymodeanalyzer.cpp. Declarations stay in the unchanged
    # keymodeanalyzer.h. See cc_refactor_keymodeanalyzer_report.md.
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodeformatting.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keyresolver.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/keyresolver.h
    ${CMAKE_CURRENT_LIST_DIR}/key/modepriorpresets.cpp
    ${CMAKE_CURRENT_LIST_DIR}/key/modepriorpresets.h
    # LAYER 3 — the key/mode SEQUENCE decoder (dedicated key-path Viterbi over the
    # Layer-2 slices; emission = KeyModeAnalyzer through the Layer-1 indexed query).
    # WIRED into the live pipeline (regionanalyzer.cpp:581): the whole-score decode
    # replaces the per-region key argmax at the Pass-1 seam. Still also runs as a
    # graded diagnostic under batch_analyze --decode-keymode. See
    # cowork_layer3_keymode_design.md + cc_layer3_decoder_audit_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodesequence.h
    ${CMAKE_CURRENT_LIST_DIR}/key/keymodesequence.cpp

    # section/ — unified section-level analysis: the analyzeSection() entry
    # point, key/mode stabilization, and cadence / pivot detection. Moved here
    # from notation/internal/notationcomposingbridgehelpers.cpp in Stage 2.1
    # (Phase 4c — Dependency Rule §3.3; docs/implementation_roadmap.md Stage 2.1).
    ${CMAKE_CURRENT_LIST_DIR}/section/sectionanalyzer.h
    ${CMAKE_CURRENT_LIST_DIR}/section/sectionanalyzer.cpp
    # Refactor — cadence/pivot detection lifted out of sectionanalyzer.cpp
    # (byte-identical pure code movement): detectCadences / detectPivotChords /
    # hasAssertiveKeyConfidence — independent of analyzeSection, driven by the
    # notation bridge. Declarations stay in the unchanged sectionanalyzer.h.
    ${CMAKE_CURRENT_LIST_DIR}/section/sectioncadencedetection.cpp
    # cadencekeyanchor — key-agnostic authentic-cadence → global tonic anchor
    # (Stage 4c-i; docs/stage4c_cadence_key_design.md §2). Built + measured only;
    # not yet wired into key scoring (that is 4c-ii).
    ${CMAKE_CURRENT_LIST_DIR}/section/cadencekeyanchor.h
    ${CMAKE_CURRENT_LIST_DIR}/section/cadencekeyanchor.cpp
    # localmodulationdetector — key-agnostic local-modulation detector (Stage
    # 4d-i; docs/stage4d_local_modulation_design.md §2): commits a candidate
    # local-key span when it is ESTABLISHED (sustained consistent run) AND
    # CONFIRMED (a V→I cadence inside it), consuming ONLY the key-agnostic cadence
    # instrument + raw region structure (no resolved key / KeyArea — the
    # no-circularity rule, design §3). Built + MEASURED only; not wired (4d-ii).
    ${CMAKE_CURRENT_LIST_DIR}/section/localmodulationdetector.h
    ${CMAKE_CURRENT_LIST_DIR}/section/localmodulationdetector.cpp
    # jointkeydecision — the scoped constrained-joint KEY decision (J-key-i;
    # docs/scoped_joint_design.md §6, the key-axis-first build): hard-fifths prune +
    # soft re-rank (cadence anchor / modulation / bass-is-root / declared-mode hint
    # / global key-path, all SOFT) + a scoped joint on the coupled core. Emits a
    # soft-only AND a soft+joint decision per region (the attribution toggle).
    # Consumes ONLY key-agnostic + local-candidate evidence (the production resolved
    # key is an echoed reference, never read). WIRED into the production resolver via
    # applyJointKeyWiring (J-key-iii, regionanalyzer.cpp:1369) but gated on
    # jointKeyWiringEnabled() (default OFF) — so production output is byte-identical by
    # default; also invoked from tools/batch_analyze --dump-joint-key.
    ${CMAKE_CURRENT_LIST_DIR}/section/jointkeydecision.h
    ${CMAKE_CURRENT_LIST_DIR}/section/jointkeydecision.cpp

    # region/ — harmonic region types and the shared analyzeRegions orchestrator.
    # Phase 4 of the duplication remediation (docs/duplication_audit.md §§2.14, 5.4)
    # moved the per-region pipeline body out of the notation bridge and
    # tools/batch_analyze.cpp into this module.
    ${CMAKE_CURRENT_LIST_DIR}/region/harmonicrhythm.h
    ${CMAKE_CURRENT_LIST_DIR}/region/regionanalyzer.h
    ${CMAKE_CURRENT_LIST_DIR}/region/regionanalyzer.cpp
    ${CMAKE_CURRENT_LIST_DIR}/region/sparsechordrefinement.h
    ${CMAKE_CURRENT_LIST_DIR}/region/sparsechordrefinement.cpp

    # harmony/ — region-level harmonic segmentation (greedy-expand, Iter 67)
    ${CMAKE_CURRENT_LIST_DIR}/harmony/harmonicsegmenter.h
    ${CMAKE_CURRENT_LIST_DIR}/harmony/harmonicsegmenter.cpp

    # scoreharvest/ — shared score-walking helpers used by both the notation
    # bridge and tools/batch_analyze.cpp. See docs/duplication_audit.md §5.8.
    ${CMAKE_CURRENT_LIST_DIR}/scoreharvest/metricweights.h
    ${CMAKE_CURRENT_LIST_DIR}/scoreharvest/metricweights.cpp

    # notemodel/ — LAYER 1: the lossless, annotated, tie-resolved note model
    # (the single source of truth for "what sounds"). Read once per score,
    # queryable by tick range via true-span overlap (no horizon). The
    # engravingbridge tone views derive over it. See
    # cowork_layer1_note_model_design.md + cc_layer1_audit_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/notemodel/note_model.h
    ${CMAKE_CURRENT_LIST_DIR}/notemodel/note_model.cpp

    # engravingbridge/ — single source of truth for the score-walking helpers
    # shared by the notation bridge and tools/batch_analyze.cpp. Replaces the
    # Step-3 using-declaration plumbing in batch_analyze.cpp. See
    # docs/duplication_audit.md §§2.1-2.13 and §5.1.
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/regiontonecollector.h
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/regiontonecollector.cpp
    # Refactor — tone/context primitives split out of regiontonecollector.cpp
    # (byte-identical pure code movement): collectSoundingAt, buildTones,
    # collectPitchContext, the two sub-boundary detectors, and findTemporalContext.
    # Residual regiontonecollector.cpp holds the collectRegionTones orchestrator.
    # Declarations stay in the unchanged regiontonecollector.h. See
    # cc_module_layering_assessment_dossier.md §5.
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/regiontoneprimitives.cpp
    # spellingview — the single shared tpc → line-of-fifths/sharp-flat spelling
    # primitive (Phase 4, the maximal-information capability). Interprets the
    # notated spelling Layer 1 carries (NoteEvent.tpc) into per-note line-of-fifths
    # + sharp/flat sense (the Layer-4 spelling-pin's input) and a signature-agnostic
    # span centroid/distribution (the Layer-3 key-spelling term's input, Phase B).
    # CAPABILITY ONLY — no production consumer yet, so output is byte-identical;
    # unit-tested as a pure function (spellingview_tests.cpp). See
    # cowork_tpc_capability_design.md + cc_tpc_capability_build_report.md.
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/spellingview.h
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/spellingview.cpp
    # phraseboundaryview — the single owned phrase-boundary primitive (Layer 1.5).
    # Reads, from the notated surface alone (key-/chord-/function-agnostic), where a
    # phrase ends. STEP A: the de-duplication of the two hand-synced fermata scans
    # (regionanalyzer jkdPhraseBoundaryTicks + batch_analyze collectPhraseBoundaryTicks)
    # into one owner — fermata-only, byte-identical. STEP B replaces the definition
    # with the graded surface-cue + marker model (design §4) without moving the
    # signature or its (dormant/gated) consumers. See cowork_phrase_boundary_design.md.
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/phraseboundaryview.h
    ${CMAKE_CURRENT_LIST_DIR}/engravingbridge/phraseboundaryview.cpp

    # slicing/ — LAYER 2: the deterministic CHANGE-POINT SLICER. Enumerates the
    # constant-tonal-sonority slices over the layer-1 note model as a covering,
    # lossless, zero-interpretation FACT (boundaries at every eligible onset AND
    # release; all-rest interior spans are explicit empty slices). WIRED into the live
    # analysis pipeline (changePointSlices @ regionanalyzer.cpp:579), consumed at
    # layer 3 by the key/mode sequence decoder. See
    # cowork_layer2_slicing_design.md + cc_layer2_audit_dossier.md.
    ${CMAKE_CURRENT_LIST_DIR}/slicing/slicer.h
    ${CMAKE_CURRENT_LIST_DIR}/slicing/slicer.cpp

    # grouping/ — ARCHITECTURAL LAYER 6 (GROUPING). The forward-only rebuild that
    # ASSEMBLES the upstream products (L1.5 boundaries, L5 cadences/RNs, L3 local
    # keys) into the flat grouping structure the ground truth annotates —
    # punctuation-spans, key-areas, cadence-to-span alignment (§5.1–§5.5). Detects
    # nothing (§6 proportionality bound). DORMANT: no production consumer; exercised
    # only by grouping_tests.cpp, byte-identical on production by construction. The
    # scattered live grouping paths it retires at engagement (detectCadences/
    # detectPivotChords in section/sectioncadencedetection.cpp, the KeyArea grouping
    # in analyzeSection/analyzed_section.h) are NAMED, touched nowhere. See
    # cowork_layer6_grouping_design.md (SIGNED) + cc_l6_build_report.md.
    ${CMAKE_CURRENT_LIST_DIR}/grouping/groupinglayer.h
    ${CMAKE_CURRENT_LIST_DIR}/grouping/groupinglayer.cpp

    # progression/ — THE PROGRESSION-RECOGNITION CONSUMER (the Layer-5/6 consumer of
    # the Harmonic Vocabulary). Recognises NAMED progressions (incl. substitutions) in
    # Layer 5's committed progression via HarmonicVocabulary::recognise (it owns no
    # second matcher), running the §4.5 three-phase idiom-mixture weighting, and emits:
    # the §4.4 progression-schema-spans (the L6 annotation), the §4.3 evidence
    # contributions (the §5.5 abstained feature + the §8/frame-F-B committed-override
    # contribution, both SELECTION-only), and the §4.6 harmonic sequences (always
    # emitted; the §5.3 key-channel CONSUMPTION is F-C-gated, NOT wired). NOT the
    # grammar owner (functionprogression, L5) nor the catalog owner (harmonicvocabulary)
    # — the D5 dependency map is cross-commented at both. DORMANT: no production consumer
    # (recognizeProgressions is called only by its tests + the default-OFF diagnostic
    # tools/batch_analyze --dump-progressions), byte-identical on production by
    # construction. Every numeric value is a declared precision-phase default (the
    # firewall — no θ, no tuning). Spec: cowork_progression_schema_design.md §3/§4;
    # component consumed: cowork_progression_schema_dictionary.md.
    ${CMAKE_CURRENT_LIST_DIR}/progression/progressionrecognizer.h
    ${CMAKE_CURRENT_LIST_DIR}/progression/progressionrecognizer.cpp

    # joint/ — THE JOINT KEY/MODE/CHORD ESTIMATOR (the OI-180 sanctioned dual path). The
    # C++ re-expression of the ratified factorization (cowork_joint_estimator_factorization.md),
    # built to decode byte-equivalently to the established Python probe (probe_corpus_decode.json).
    # Reads ONLY the L1/L1.5 published fact surface + the two dependency-free pitch primitives
    # (normalizePc, diatonicMaskFromFifths) — never the legacy L2/L3/L4/L5 analysis. Frozen tables
    # and weights are LOADED AT RUNTIME from the committed artifacts under tools/joint_estimator/.
    # DORMANT: no production consumer — nothing in src/ calls any joint symbol; it is exercised only
    # by the composing tests and (a later commit) a default-OFF tools/batch_analyze diagnostic flag.
    # Byte-identical on production by construction. Dispatch: the joint-estimator C++ module build.
    ${CMAKE_CURRENT_LIST_DIR}/joint/labelclass.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/labelclass.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointprimitives.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointprimitives.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointadapter.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointadapter.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointdecoder.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointdecoder.cpp
    # jointfactadapter — the "score -> facts" build step (Task C): builds the decoder's Piece inputs
    # from the L1 published notatedNotes() surface + the score's structural facts (measure/meter/
    # signature). The C++ counterpart of tools/joint_estimator/gen_note_events.py; input parity grades
    # it against note_events.json field by field. Still DORMANT (driven only by --joint-* diagnostics).
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointfactadapter.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointfactadapter.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointtables.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointtables.cpp
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointweights.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointweights.cpp
    # jointrender — the presentation-derivation primitives (chord-symbol / Roman-numeral / grading
    # quality strings) single-sourced from the batch render (the notation output-surface contract
    # §3.2 derived chord facts + §5.6 formatter continuity; #6 one path). Pure functions of a class +
    # bass role; read by BOTH tools/batch_analyze --joint-inference and the §3.2 notation record.
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointrender.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointrender.cpp
    # jointembeddedartifacts — GENERATED (tools/joint_estimator/gen_embedded_tables.py, Decision
    # D1): the five committed table artifacts + the SELECTED weight vector embedded VERBATIM as
    # compiled-in bytes, provenance-locked at build time. loadEmbedded() parses these through the
    # SAME parser as the filesystem path (#6). This is the PRODUCTION table/weight source; the
    # filesystem JointTables::load stays for the tests/diagnostics that establish it.
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointembeddedartifacts.h
    ${CMAKE_CURRENT_LIST_DIR}/joint/jointembeddedartifacts.cpp

    # voiceleading/ — AXIS 2 (VOICE LEADING), the dormant FOUNDATION build. The second,
    # orthogonal analysis dimension (cross-ARI(VL, harmonic) = 0.030, findings v2.0): the
    # linear reading of the same L1 notes. VL-A voicelinearview (the lossless per-voice
    # view; FACT) -> VL-B voiceleadingprofiles (motion & interval profiles + the per-sample
    # motion-event series; FACT, study-parity duty) -> VL-C textureclassifier (the ONE v1
    # judgment: texture-of-span, Class M, whole-selection granularity, nearest-centroid in
    # the measured winning feature space ABz) + its bounded-context extension requester.
    # The reference set is GENERATED (textureclassifierreference.h, run_vl_feature_space.py).
    # DORMANT: no production consumer — nothing in src/ calls any voiceleading symbol; it is
    # exercised only by voiceleading_tests.cpp and the default-OFF diagnostic
    # tools/batch_analyze --dump-vl. Byte-identical on production by construction; every
    # numeric value is a declared precision-phase default (the firewall). Spec:
    # cowork_voiceleading_axis_design.md (SIGNED) §5.1-§5.3, §7, §8; measurement +
    # feature-space decision: cc_vl_foundation_build_report.md.
    ${CMAKE_CURRENT_LIST_DIR}/voiceleading/voicelinearview.h
    ${CMAKE_CURRENT_LIST_DIR}/voiceleading/voicelinearview.cpp
    ${CMAKE_CURRENT_LIST_DIR}/voiceleading/voiceleadingprofiles.h
    ${CMAKE_CURRENT_LIST_DIR}/voiceleading/voiceleadingprofiles.cpp
    ${CMAKE_CURRENT_LIST_DIR}/voiceleading/textureclassifierreference.h
    ${CMAKE_CURRENT_LIST_DIR}/voiceleading/textureclassifier.h
    ${CMAKE_CURRENT_LIST_DIR}/voiceleading/textureclassifier.cpp
)
