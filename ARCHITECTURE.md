# MuseScore Arranger — Architecture Document

> **★★ GOVERNING DECISION (user-ratified 2026-07-17): the key/mode/chord estimator is JOINT — see
> `cowork_joint_estimator_architecture.md`.** Key, mode, and chord are inferred by ONE probabilistic decode
> over `(tonic, mode, chord)` with segmentation as a modeled (semi-Markov) variable and every enumerated clue
> as a theory-grounded factor — NOT the feed-forward, per-layer pipeline the layer sections below still
> describe. Those layer sections (L1–L6) remain the accurate description of the CURRENT code and its
> retirements, but the TARGET architecture is the joint estimator; the layer specs are updated to it as the
> design pass proceeds. Theory basis: `cowork_key_chord_joint_inference_grounding.md`.

> **★★ AS-BUILT (the OI-178 adoption, user-ratified 2026-07-26, option 1 — STAGED SCOPE): the joint estimator
> is now the PRODUCTION inference layer on the batch/corpus surface.** As-built module `src/composing/analysis/joint/`:
> the **L1 fact adapter** (`jointfactadapter` — score → `Piece` from the published `notemodel::notatedNotes()`
> tie-unresolved surface + the score's structural facts, per the OI-180 sanction: no module-private raw-note walk);
> the **event lattice + exact block-factorized semi-Markov Viterbi decoder** (`jointdecoder`) with the ratified
> **§5 total-order tie-break**; the **factor log-probability provider** (`jointadapter` — the ten-factor
> log-linear score, Katz leftover option 2a); the frozen generative **tables** (`jointtables` — the committed
> all-326 `tables_all.json` / `note_tables_all.json` / `factor_presence_all.json` / `fermata_boundary_addendum.json`);
> and the **weight vector** (`jointweights` — the direct-metric SELECTED vector, identity `random07`).
> **Table/weight delivery — EMBEDDED (ratified Decision D1):** a provenance-stamped code-generation step
> (`tools/joint_estimator/gen_embedded_tables.py`) compiles the five committed artifacts + the selected weight vector
> VERBATIM (JSON bytes, not a parsed-structure codegen) into the generated `jointembeddedartifacts.{h,cpp}`, so the
> running binary's fitted values are **provenance-locked at BUILD time** (#16/#19) and cannot silently drift.
> `JointTables::loadEmbedded` / `FittedAdapter::loadEmbedded` / `selectedWeights()` are the PRODUCTION source; they
> parse the embedded bytes through the SAME parser as the filesystem loaders (#6, one parse path). The filesystem
> `JointTables::load` / `FittedAdapter::load` stay for the tests/diagnostics that establish the embedded data.
> Regenerating the embedded source is the **new mechanical step of any table re-fit**; the `joint_embedded_tests`
> drift guard (embedded bytes byte-identical to the committed files; the weight vector value-exact to
> `decode_parity_ref.json`) is the standing guard against divergence. The generated file publishes the §2
> output-surface-contract provenance constants (artifact sha256s, the weight-vector identity, a decoder-version
> string) as declared dormancy — consumer: the notation record build. State = `24 keys × a ground-truth-derived Roman-numeral
> vocabulary`, chord = scale-degree-valued (the chord symbol is the derived published fact from (key, degree)),
> segmentation is a modeled semi-Markov variable, seg_cap 4. Inference is **preset-independent** (presets are
> presentation concerns). **Wiring:** `tools/batch_analyze.cpp --joint-inference <dir>` (default-OFF) produces
> each `.ours.json` from the decode at the EMBEDDED tables/weights (the `<dir>` is no longer read for fitted
> values) instead of the legacy `analyzeScore` pipeline; `tools/run_bach_preset.py
> --joint-inference` regenerates the corpus; the committed regression reference `tools/robust_stop/` is graded on
> it (root 77.03 / RN 64.12 / key-home 56.14 / key-local 78.42 %, class-(b) hard-stop 1,817,280 ticks per preset).
> **STAGED SCOPE — CLOSED AT THE NOTATION SWITCH, 2026-07-27 (corrected 2026-08-02, `OPEN_ITEMS.md` OI-232 item 1;
> the sentence this replaces said the notation layer stays on the legacy pipeline, which the switch made false).** The
> adoption above put the joint estimator on the batch/corpus surface only; **the notation switch put it on the in-app
> NOTATION surface too** (`useJointNotationRecord` defaults ON — `composingconfiguration.cpp:178`). The declared
> migration state (#23) is therefore CLOSED on both surfaces, and the legacy `region::analyzeRegions` →
> `analyzeSection` path is compiled and dormant, awaiting deletion at the OI-180 retirement map. The first
> increment named here — carrying the notation output-surface contract (from A's posterior — alternatives,
> exposure/confidence, cadences, key areas) and the fitted-table packaging to the in-app runtime — is DELIVERED;
> see "THE RECORD PATH" below, subsections (1)–(6). Full
> spec: `cowork_joint_estimator_architecture.md`, `cowork_joint_estimator_factorization.md`; pre-fit gates
> `cowork_prefit_gates.md`; adoption record `cc_adoption_measurement_report.md` / `tools/joint_estimator/adoption_record.json`.
>
> **POSTERIOR SLICE — the notation output-surface contract §3.3 GROUP (i) (as-built, ADDITIVE; the decode is
> unchanged).** `jointdecoder::computePosteriorSlice(piece, segments, adapter, vocab, cache)` publishes, per
> committed segment, the ESTABLISHED content-score uncertainty surface as two full candidate lists (no truncation
> constant): a **KEY axis** — the committed chord class re-scored under every scoreable candidate key (all 24,
> KEYS_24 order: tonic 0..11, major before minor) — and a **CHORD axis** — every scoreable vocabulary class
> re-scored under the committed key (sorted class-key order); each entry is (label, weighted within-segment content
> score) with the committed reading flagged by index. It is computed POST-decode by re-scoring the held span with
> `segmentContentScore`, so it inherits the established Neumaier bit-parity; "scoreable" = root defined AND finite
> content score (probe_decoder._segment_posterior's filter). The scores are LOG-scores, NOT probabilities, and gaps
> are score differences; **GROUP (ii) forward-backward marginals are NOT delivered here — OI-193's later step.** The
> batch `.ours.json` render is UNCHANGED (the a8 grading schema keeps `"alternatives": []`, the pinned grading form);
> the slice's consumer is the later notation record build. **Reference oracle + parity:** the Python
> `tools/joint_estimator/gen_posterior_slice.py` writes `posterior_slice_ref.json` — the SELECTED-arm slice, full
> precision, in shared-label form (the scoreable sets are span-INDEPENDENT on this corpus: exactly one 24-key list
> and one 104-class list across all 13,063 committed segments, so the labels are published once at top level and each
> segment stores only its scores + committed index; lossless, not truncation). It is established two-halved:
> (a) the identity-arm key-axis runner-up/gap reproduces the committed `probe_corpus_decode.json` EXACTLY on the 325
> §5-unaffected pieces (bwv362 the sole §5 equal-score exception, enumerated), (b) the selected-arm committed
> segments equal `decode_parity_ref.json` on all 326. The default-OFF `batch_analyze --joint-posterior-slice <dir>`
> driver verifies the C++ slice BIT-IDENTICALLY against it (every piece × segment × candidate × both axes; a
> near-miss is a defect, not a tolerance).
>
> **NOTATION OUTPUT-SURFACE RECORD — the A-native record (as-built, DORMANT; contract `cowork_notation_output_contract.md`
> §3.1–§3.4).** `joint::assembleNotationRecord(piece, result, sigFifths, declaredMode, adapter, vocab, cache)`
> (`jointnotationrecord`) assembles the ONE surface the in-app notation path will read (Decision A2), from the
> decode outputs + the decode's prior inputs + the compiled-in provenance — it NEVER re-decodes and never reads the
> score. **§3.1** the piece block: analyzed span, the signature-fifths/declared-mode INPUT ECHO (the adapter exposes
> only the initial signature — no mid-piece re-anchor points, so that list is empty), and the §2 provenance block
> read from the D1 embedded constants (`kTableArtifacts` hashes, `kWeightVectorIdentity`, `kDecoderVersion`,
> `kCorpusGitHash` — **their declared dormancy is discharged**: the record is their consumer). **§3.2** per committed
> segment: the native fields verbatim + the derived chord facts computed ONCE (the render primitives are
> single-sourced in `jointrender` — `jointOursQuality`/`jointChordSymbol`/`jointRenderRn`, shared with the batch
> render for §5.6 formatter continuity, #6): `keySignatureFifths`, root/bass tonal **spellings** (line-of-fifths;
> `jointprimitives::rootSpellingLof`/`factorSpellingLof`), member pcs with factor roles, the class-native
> `diatonicToKey` (a structural read, not a collection recompute — OI-173's lesson), the per-event bass factor role,
> and the augmented-sixth Italian/German/French sub-type derived from the SOUNDING content (the vocabulary collapsed
> the family to Italian). **§3.3** the established posterior slice attached. **§3.4** the un-rounded modal reading
> (`computeModalReading`) per key run: for each scale degree 1..7, the sounding duration + onset count of every
> chromatic inflection (degree from the notated spelling, inflection by pc offset) — counted, un-rounded, no label
> (C1). **§3.5** ornament fields RESERVED-absent (OI-194's own increment); **§3.6** excluded fields simply absent.
> **Establishment:** the key-signature-fifths mapping duplicates the legacy `keymodeanalyzer::keySignatureFifthsForKey`
> module-locally (L1-only isolation, #7/OI-180 — unifies at the legacy retirement); the spelling derivation is
> established by `tools/joint_estimator/gen_spelling_establishment.py` → `spelling_establishment.json` (root
> 13061/13063 = 99.985 % agreement with the notated tpc where the root sounds, 0 unmappable/pc-mismatch; the four
> divergences are enharmonic re-spellings, the OI-168 convention class); **the C++ spelling mapping
> (`jointprimitives::rootSpellingLof`/`factorSpellingLof` — the one the switch publishes) is established lof-EXACT
> against that Python derivation on all 13,063 committed segments — 0 divergences, root 13,063 + bass 11,182 cells
> reconciling to the establishment (OI-197 RESOLVED; the default-OFF `batch_analyze --joint-spelling-parity` dump +
> `gen_spelling_establishment.py --cpp-parity` → the generated `cpp_parity` block, with a negative-control check
> that a perturbed lof STOPs)**; the modal counter by the bwv254 hand-check
> (D-minor degree-6 all ♭6, degree-7 ♭7+leading-tone). Consumers: the RECORD PRODUCER + the two seam VIEWS (next
> paragraph) read this record — DORMANT (no src/ consumer yet). Suites: unit coverage in
> `joint_record_tests` / `joint_spelling_tests` / `joint_modal_tests`.
>
> **THE RECORD PATH — the notation output-surface contract as-built (the PRODUCTION notation path since THE SWITCH,
> user-ratified 2026-07-27; `useJointNotationRecord` defaults ON).** This is the consolidated, forward end-to-end record
> of the joint estimator's A-native notation record and the re-plumbed notation consumers that read it (delivered by the
> seams partition P0-P7; per-unit provenance in STATUS.md / `cowork_handoff.md`). At the switch the migration posture
> **CLOSED**: the record path is now THE in-app notation analysis; the legacy `analyzeHarmonicRhythm`/`analyzeChord`
> path remains COMPILED and DORMANT, selected only by an explicit `useJointNotationRecord = false`, awaiting deletion at
> the **OI-180 retirement map (now fully live)**. Through the whole P0-P7 build the flag stayed OFF and the legacy path
> ran byte-identically (proven per delivery unit); the switch flipped the default and refreshed the pipeline-snapshot
> goldens against the record arm, every diff reconciled to the P6 classified evidence (see **(6) the switch**, below).
>
> **(1) The producer + the two seam views (contract §1 seams, PRODUCER side; `jointnotationproducer`).**
> `joint::produceNotationRecord(score, stem)` is the ONE-call score->record
> entry: `buildAdapterFacts` (the L1 published-fact surface — the only score read, no raw-DOM walk) -> the compiled-in
> EMBEDDED tables/adapter + the SELECTED weight vector (Decision D1) -> `decodePiece` (§5 total order, seg_cap 4) ->
> `assembleNotationRecord` (which attaches the §3.3 slice). WHOLE-score decode ONCE; deterministic; NO caching (a
> later, measured concern — #17's funnel, not built speculatively). It returns a `NotationRecordResult` — either the
> full record or an UNAMBIGUOUS failure (`ok=false`, `error` set, empty record) when the fact adapter cannot extract
> the score (`AdapterFacts.ok == false`, e.g. a null score): never a partial record, never a silent fallback (#13).
> **Input-scoping (OI-204):** `produceNotationRecord(score, stem, excludeStaves = {})` forwards `excludeStaves` to
> `buildAdapterFacts`, which skips any notated note whose owning staff is in the set — INPUT selection at the fact
> adapter (the layer that owns its input surface, #7), before the note enters the L1 fact view the decode reads; NOT a
> consumer-side post-filter, NOT an inference change (the empty default skips nothing → byte-identical extraction). Each
> record-arm seam threads the SAME chord-track exclude set its legacy arm passes (arm-for-arm input parity), so a
> populated chord track's own notes are never fed back into a re-analysis (the self-feedback hazard). A
> `produceNotationRecord(piece, sigFifths, declaredMode)` core (the same minus `buildAdapterFacts`) is the
> establishment seam. The two §1 seams READ this record as pure VIEWS (#6, no recompute): **the span view**
> `spanViewSegments(rec, startTick, endTick)` returns the segment indices OVERLAPPING [startTick, endTick)
> (`seg.startTick < endTick && seg.endTick > startTick`; an empty/inverted span selects nothing); **the note view**
> `noteView(rec, tick)` returns the segment CONTAINING `tick` (`seg.startTick <= tick < seg.endTick` — a boundary
> tick belongs to the segment it STARTS), resolving the committed reading + derived facts (`segment`) + the §3.3
> slice (`slice`), or `found=false` outside the analyzed span (the §3.1 piece block is the record's own fields).
> Consumers: the record-arm branches of the re-plumbed notation seams — subsections (2)-(5) below (behind the
> default-OFF flag; DORMANT on production until the switch). It composes only already-established parts; no inference,
> no new derivation.
> Coverage: `joint_producer_tests` (the producer core vs the parts-assembled record + a `decode_parity_ref` spot-check
> on bwv324/bwv362; the score wrapper == `buildAdapterFacts` + core on `pb_chorale.mscx`; the null-score failure
> path; the span-view overlap incl. span-splitting; the note-view boundary rule; the empty-span / out-of-span edge
> duties).
> The layer sections (L1–L6) below remain the accurate description of the LEGACY pipeline, which since the notation
> switch is **dormant-compiled on BOTH surfaces** — the batch/corpus surface and the in-app notation surface alike.
> (Corrected 2026-08-02, `OPEN_ITEMS.md` OI-232 item 2; the sentence this replaces had the two surfaces the wrong
> way round, saying the legacy pipeline was still live on the notation path.)

> **(2) The section adapter + the span-annotation consumer + the inference↔presentation boundary.**
> The section layer's record path `analyzeSectionFromRecord` (`sectionrecordadapter`) derives the shared
> `AnalyzedSection` from the record (1:1 segment→region) via the ONE record-segment→`ChordAnalysisResult` converter
> `chordResultFromRecordSegment` (#6; the section layer and the presentation layer both read its result). The
> span-path emitter's record arm (`emitHarmonicAnnotations`, `notationcomposingbridge`) writes, per region: the
> **Roman numeral** as the record's PUBLISHED derived fact (`rs->romanNumeral`, the jointRender form); and the
> **display chord symbol** + **Nashville number** as PRESENTATION DERIVATIONS (Decision D2 + the contract §3.3
> amendment — display renderings are presentation, facts are published) rendered by the REUSED `ChordSymbolFormatter`
> (`formatSymbol` / `formatNashvilleNumber`, via the shared `formatChordResultForStatusBar`) from the record's
> committed reading — NOT the record's grading-form `chordSymbol` ("GDom7"), which stays on the record for batch/a8
> continuity. The carriage is COMPLETE: the converter carries the FINE class quality's seventh-ness into
> `ChordIdentity.extensions` (the coarse `ChordQuality` drops it), so the formatter renders "G7"/"Am7"/"Bdim7"; a
> rootless chromatic class renders no symbol (matching the batch rootless "" from `jointChordSymbol`). **THE BOUNDARY
> IS PERMANENTLY GUARDED both ways** by a mechanical include-closure test (`inference_presentation_boundary_tests`):
> the joint estimator's inference module (every file under `analysis/joint/`) includes NO presentation formatter
> (`chordanalyzer.h` / `chordsymbolformatter`; the shared pitch leaf `analysisutils.h` is exempt), and the
> presentation formatter (`chordsymbolformatter.cpp`) includes NO joint inference internal — it consumes only the
> published record/adapter output surface (a `ChordAnalysisResult`). The guard carries a negative control (it fires
> on a perturbed include, both directions). No inference change on this path; the display renderings are the only
> additions, and they are presentation.

> **(3) The implode + tuning span-seam consumers + the exposure-bucket unification.**
> The last two span-seam consumers are re-plumbed
> onto the record path. **The key-exposure BUCKET is unified (the P2a pattern completed):** the tentative/assertive
> bucket the implode formerly re-thresholded at 0.5/0.8 is now a STORED per-arm result on `AnalyzedRegion`
> (`keyExposureBucket`, 0=below-tentative / 1=tentative / 2=assertive), set ONCE at the section-layer set site beside
> `hasAssertiveExposure` — legacy arm from `normalizedConfidence >= 0.5/0.8` (`sectionanalyzer.cpp::legacyKeyExposureBucket`,
> legacy-arm-only), record arm from the raw §3.3 key-axis gap (nats) at `kTentativeKeyExposureGap=0.975911` /
> `kAssertiveKeyExposureGap=1.055757` (`sectionrecordadapter.cpp`, the P1 constants from
> `tools/notation_seams/exposure_constants.json`; the record's confidence field carries nats, never compared to the
> [0,1] literals). The implode reads the stored bucket (#6 — one thresholding site per gate). **The implode chord-track
> record path** (`notationimplodebridge.cpp`, `populateChordTrack` behind the flag → `produceNotationRecord` →
> `analyzeSectionFromRecord` → the SAME `emitImplodedChordTrack` with the record) writes, per region: the **Roman
> numeral** as the record's PUBLISHED `romanNumeral` (a fact, looked up by `noteView` at the region's start tick, NOT
> re-formatted from `ChordIdentity`); the **display chord symbol** + **Nashville** as PRESENTATION derivations
> (`ChordSymbolFormatter::formatSymbol`/`formatNashvilleNumber`; a rootless class writes no symbol); exposure gates read
> the stored bucket; the borrowed-key source-key search is restricted to the C1 two modes (the exotic-mode enumeration
> + the 0.35 mode-suffix gate are legacy-arm-only, inert on the record arm by two-mode construction);
> `kSameChordReannotationGap` (960) is a declared presentation-timing constant. **The tuning region record path**
> (`notationtuningbridge.cpp`, `applyRegionTuning` behind the flag) derives the tuning regions from the record and maps
> each to the `(span, chordResult, keyModeResult)` the tuning loop reads — the inputs are FACTS the record carries
> (`rootPc`, `quality`, and `keyModeResult.tonicPc`, the only `KeyModeAnalysisResult` field any `TuningSystem` reads —
> `JustIntonation::rootOffset`); no consumed fact the record lacks. A produce failure writes/tunes NOTHING on either
> path (the record IS the surface, A2/#13 — no legacy fallback). Flag OFF → both paths byte-identical. **OI-182 EXECUTED
> at the record surface** (the §4.1 presentation-gate disposition — every exposure/annotation constant's declared site).

> **(4) The note-seam re-plumb (status bar + harmony write + right-click menu) on `noteView`.**
> The single-note surface
> (`analyzeNoteHarmonicContext[Details]`, and through them `harmonicAnnotation`) gains its record arm at the ONE funnel
> `analyzeHarmonicContextAtTick` (`notationcomposingbridge`): flag ON → `produceNotationRecord` (whole-score, once) →
> `noteView(rec, tick)` → the ONE builder `buildNoteContextFromRecord` fills `NoteHarmonicContext` from the record's
> published facts (contract §1 **seam 2** — a VIEW into the record, NOT a second computation, #6). The builder reuses the
> SHARED per-segment mapping `regionFromRecordSegment` (`sectionrecordadapter`, EXTRACTED so the span seam
> `analyzeSectionFromRecord` and the note seam derive the committed reading + two-mode key + §3.3 alternatives in ONE
> place — the span loop then adds only `tones`, which the note view carries none of). Per note: `chordResults[0]` = the
> committed reading via `chordResultFromRecordSegment`; `chordResults[1..]` = the §3.3 chord-axis alternatives
> (`recordAlternatives`), committed-first then descending content score, each carrying its §3.3 content score as
> `identity.score` (the "(%.2f)" suffix); `keyFifths`/`keyMode` = the C1 two-mode key; `keyConfidence` = the RAW §3.3
> key-axis gap in nats (a model-internal quantity, NO [0,1] remap); the pedal fields stay false/-1 (suspended, OI-194);
> `temporalExtensions` default (audited: no in-tree reader); `enclosingKeyArea` nullopt (the single-segment view has no
> section key-area grouping). The THREE audited note-seam consumers — the **status bar** (`harmonicAnnotation` → the
> accessibility chain), the **harmony write** (`notationinteraction`), and the **right-click menu**
> (`notationcontextmenumodel`) — all route through `analyzeNoteHarmonicContext[Details]`, so the ONE builder carries all
> three; each renders via the SAME shared P-strings formatters (`formatChordResultForStatusBar` / `ChordSymbolFormatter`)
> reading the carriage — **NO consumer code change**. An out-of-span tick or a produce failure yields an EMPTY context
> (nothing written, no partial output, no legacy fallback — the record IS the surface, A2/#13). The bounded-window decode
> cache is BYPASSED on the record arm (a whole-score produce per invocation, the P3a/P4 pattern; a record cache is a later
> measured concern — the interactive-frequency cost is noted, not a structural incompatibility). Flag OFF → the legacy
> expanding-window path byte-identical. After this unit the whole audited note seam is dual-arm.

> **(5) The dual-arm classified-comparison instrument (measurement-only, opt-in; the switch evidence).**
> The §8.4 switch-ratification evidence: what the switch actually changes on the notation output surface,
> and why. A CAPTURE (`pipeline_snapshot_tests` `DISABLED_DualArmClassifiedCapture`, opt-in — the golden sweep and
> byte-identity untouched) runs the FULL notation output surface TWICE per snapshot-corpus score over the 16-measure
> window — arm "legacy" (`useJointNotationRecord` OFF) and arm "record" (ON) — and serializes both:
> `annotation` (the span-seam write: display symbols / Roman / key brackets / Nashville / pedal + cadence StaffText),
> `implode` (the chord-track write: treble symbols, bass Roman/Nashville, imploded voicing pitches, key/cadence text),
> `tuning` (per-note offsets under a fixed Just-Intonation tonic-anchored config — a downstream read of the committed
> root+key), and `noteSeam` (the committed reading + rendered symbol/roman/nashville + §3.3 alternatives at EVERY
> measure downbeat). It calls only public production entry points; the flag is restored OFF by RAII per surface; each
> surface array is sorted by a stable key so the artifact `tools/notation_seams/dualarm_capture.json` is deterministic
> run-to-run. A CLASSIFIER (`tools/notation_seams/classify_dualarm.py`, #17f) aligns the two arms per surface and
> classifies EVERY non-identical item into: **inference-driven** (the record's committed reading differs — the
> adoption's expected differences, both readings cited); **presentation-rule** (a ratified rule accounts for it, cited:
> C1 two-mode display / the §4.1 exposure gates / OI-194 pedal suspension / §3.3 alternatives ordering / D2
> grading-vs-display / OI-201 aug-sixth coarseness / the applied-chord Nashville "?" convention); **input-scoping** (the
> OI-204 class — structurally ZERO on this chord-track-free corpus); and **UNEXPLAINED** (the headline — every entry
> investigated to a mechanism before delivery, else a STOP). It emits `dualarm_classified_report.json` +
> `dualarm_classified_summary.txt`. The instrument invents no value and bends nothing toward either arm — a difference
> is CLASSIFIED, never patched.
>
> **(6) THE SWITCH — the migration posture is CLOSED (user-ratified 2026-07-27).** The seams partition (P0-P7) was
> closed out and completeness-verified (`tools/notation_seams/partition_completeness.json` — every consumer's record
> branch cited, every ruling checked, every seams-era register row in state, the flag OFF everywhere, the three suites
> green; NO finding), and the switch — ONE revertible, user-ratified commit (dispatch `cc_instruction_notation_switch.md`)
> — flipped `useJointNotationRecord`'s default to **ON**. The batch/corpus output is A's (the OI-178 adoption); the in-app
> notation analysis is now **A's record path** too. The switch refreshed the pipeline-snapshot goldens against the
> established record arm (cited preconditions: the P6 classified report `dualarm_classified_report.json` + the OI-178
> adoption record), and every legacy→record golden diff was reconciled to the P6 taxonomy by
> `tools/notation_seams/reconcile_switch_goldens.py` → `switch_golden_reconciliation.json`: **0 unexplained, 0
> input-scoping, the non-flag-gated surfaces (implode / keyAreas / tickLocal) byte-identical** — the diff is
> inference-driven (the record's committed-reading / segmentation / voicing moves), §3.3 alternatives-ordering
> presentation, and a production-INERT auxiliary class (the note-seam carriage's `temporalExtensions`/`wasRegional`,
> which no consumer reads). The batch/corpus surface and `tools/robust_stop/` did not move (the flag is notation-side;
> `test_batch_analyze_regressions` passes). The legacy `ChordAnalysisResult`/`NoteHarmonicContext`/`HarmonicRegion` path
> and the per-arm legacy branches now RETIRE on the **OI-180 retirement map** (post-switch, fully live); the post-switch
> agenda includes OI-193 (the marginal-posterior completion), OI-194 (the ornament-label / voice-independent pedal-class
> publication), OI-203 (the record-cache increment — the latency is now on the default path), and OI-201 (the aug-sixth
> display-symbol completeness gap).

> **★★ THE JOINT ESTIMATOR'S STANDING RULES — fitting, held-out evaluation, the search, the key axis, and
> what the fitting pool may contain.**
> Six rules govern the estimator described above. Each was ratified on the date given; all six were until
> 2026-08-02 recorded only on tracking surfaces or in `CLAUDE.md`, which is why they are stated here — this
> specification is where a reader looks for how the estimator must behave.
>
> **(a) Factor FORMS come from theory; factor VALUES are fit ONCE against ground truth and are never tuned
> per case.** Every factor's shape is derived from established music theory before any number is attached to
> it, and the numbers are then estimated in one fit event against the DCML ground truth — never adjusted
> afterwards to make a particular passage come out right. *Why:* a value tuned to one passage is fitted to
> that passage and measures nothing on the next one (`CLAUDE.md` #8; `DEFECT_TYPES.md` DT-2). Ratified by the
> user 2026-07-17, with the governing decision at the head of this document (`OPEN_ITEMS.md:24-25`).
>
> **(b) The held-out split and the capacity budget are declared BEFORE any value is fit, and the headline
> number is the held-out one.** The ratified protocol is five-fold cross-validation grouped by the shared
> *When in Rome* analysis file, with every fitted object — vocabulary threshold, smoothing, regularization
> strength included — estimated on training folds only; the headline is the pooled cross-validation number
> with a piece-bootstrap 95 % uncertainty range. The capacity budget is a pre-fit parameter inventory: a cell
> receives its own maximum-likelihood estimate only at a count of at least 20 and otherwise pools to a
> declared parent, free parameters stay at or below one tenth of the token count, and the weight vector holds
> at most 12 weights. *Why:* `CLAUDE.md` #20 — no value is graded on data that helped fit it, so a
> fitted-and-self-measured number is not established (#19). Protocols ratified 2026-07-19
> (`cowork_prefit_gates.md`; tracked at `open_items/OI-176.md` and `open_items/OI-177.md`); the ratifier of
> that event is not named in the record.
>
> *Delegation pointer (the fifth home case, user-ratified 2026-08-02): the fitting event's own design contract is `cowork_stage5_fitter_design.md` (SIGNED, user, 2026-07-04) — D-312…D-314 — which this specification points at and does not restate.*
>
> **(c) The decode is EXACT; the declared reserve prune was never adopted, and what the decoder does narrow
> has no specified form.** Exact semi-Markov Viterbi over the joint state is the ratified search. A prune was
> declared in reserve — restricting key-change candidates to a fitted-mass neighborhood on the circle of
> fifths — to be used only if measurement showed exact decode intractable, and only with its own
> established-loss measurement, never as a silent heuristic
> (`cowork_joint_estimator_factorization.md:170-173`). It was never adopted: measured at the fitted weights
> its cost is worse than exact decode. What the shipped decoder DOES narrow — the candidate-admission rule
> that decides which chord classes a segment may even consider — has no specified form anywhere in this
> architecture and no recorded basis. Both facts are open and are tracked at `OPEN_ITEMS.md` OI-188 (the
> reachability bound on every ceiling claim) and OI-226 (admission has no ratified basis); neither is settled
> here.
>
> *Tried and closed on the search — do not retry; the register carries each with its measurement: D-288 (beam widening, shelved), D-328 (a wider search over the same scoring, refuted), D-278 (the joint key-and-chord step over the two legacy decoders, shelved).*
>
> **(d) On the key axis the decoder commits its maximum-a-posteriori path; it never abstains.** The estimator
> always names a key for every committed segment, so the abstention counter the regression stop reads is
> zero on the production arm. Recorded at the OI-178 adoption, user-ratified 2026-07-26 (`CLAUDE.md` gate
> block (A)); **derivation not recorded** — the record gives no reason for committing rather than abstaining.
> **This sits in tension with the abstention rule at §5.7a** ("calibrated
> abstention when evidence is weak", an item in the high-precision-before-coverage target), which admits
> declining to answer. The two statements are both in force in the record: §5.7a states the product target,
> this rule states what the shipped decoder does on the key axis. Which governs is **not settled here**.
>
> **(e) A value that SHIPS may be fitted only on freely-licensed music.** The pool a ship-intended weight or
> table is estimated on is restricted to public-domain, CC0 and CC-BY sources. Music carrying a
> non-commercial licence or no stated licence — the record names the DCML corpora, MCMA and Essen — may be
> used to validate and to check, never to fit a value that is distributed. The fitting design states its
> objective-source and its validation-source split explicitly, so which pool produced which number is
> readable rather than reconstructed. *Why:* a fitted value inherits the licence terms of the corpus it was
> estimated on, and this project ships under GPL v3 (§1.3), so a value fitted on a non-commercial pool
> cannot lawfully be distributed with the product. Ratified by the user 2026-07-04 as binding on the fitter
> design; reaffirmed as written by the user 2026-08-02 at the `OPEN_ITEMS.md` OI-271 ruling. The constraint's
> own detailed block, with the per-licence-class pool table, is `cowork_score_census.md` §8c. **Which class
> the 326-chorale ground truth actually falls in is NOT settled:** the licence-class verification of
> 2026-08-02 established that the *When in Rome* analyses this fit reads are not a DCML-lab corpus and are
> therefore not the non-commercial class the constraint assumed, and did not establish CC-BY-SA either; the
> narrowed question is open at OI-271.
>
> **(f) Values are fitted per IDIOM, never for a user preset.** One fit event per musical idiom — a body of
> repertoire sharing a practice — and no value is ever adjusted to make a named preset come out right. A
> preset is a regression surface and a carrier for delivering a fitted set; which presets an end user should
> see is a separate product question, decided later and not by the fitting event. The Bach fit is an idiom
> fit delivered through more than one carrier. *Why:* a user mandate, recorded as constraint 4c of the
> fitting design; it is the fitting-side statement of the same separation the adopted estimator makes on the
> inference side (inference is preset-independent, presets are presentation concerns — stated at the head of
> this document). Ratified by the user; the record does not date the mandate.

> **Living design document.** Read this AND STATUS.md at the start of every development
> session. ARCHITECTURE.md contains stable design decisions. STATUS.md contains current
> implementation status and immediate next steps. Update STATUS.md as your last act when
> anything changes. Update ARCHITECTURE.md only when architectural decisions change.

> **Doc governance (2026-06-29) — the hierarchy.** This is **THE canonical architecture doc**. The **per-layer /
> per-component design docs** (`cowork_layer*_design.md`, `cowork_progression_schema_dictionary.md`,
> `cowork_progression_schema_design.md`, the phrase-boundary design, …) are the **authoritative detail** for their own
> scope — the rules, the mechanisms, the per-layer decisions-with-alternatives — and are **referenced** from here. They
> are **not** rival architecture docs: a **cross-cutting contract is stated once, here (§2.15), and never redefined in a
> layer doc** (a layer doc may *use* the span typology or the verifiability contract, not *redefine* it).
> `cowork_target_architecture.md` is **demoted** to the detailed-rationale reference for those contracts (the historical
> north-star, the full statements, the supporting evidence) — not a second canonical doc. **When any doc disagrees with
> this one, this one wins, and a new ratified decision lands here first.**

> **★★ ARCHITECTURE NOTE (updated 2026-06-29 — the 2026-06-15 joint-inference investigation has LANDED).**
> The "constrained joint inference" investigation concluded: a **full joint cross-layer decode was measured
> INERT** — the realisable gain is soft-evidence *quality* carried forward (calibrated confidence + ranked
> alternatives), not global cycling. The ratified back-half architecture is therefore **forward-only**: a
> feed-forward stack of single-responsibility layers (**L1** notes → **L2** slicing → **L3** key/mode → **L4**
> chord → **L5** function → **L6** grouping), each carrying **ranked alternatives + a confidence**, with two
> scoped escapes from pure feed-forward — a **gated, constrained joint step (Stage 5)** for the residual
> key↔chord coupling only, and the **confidence-weighted forward-override mechanism** (a confident inference
> overturned by decisive later evidence via a *localized forward recompute* — no back-edge, no global decode).
> See §2.14 (the superseding reconciliation) and §2.15 (the cross-cutting contracts); full ratified statements:
> `cowork_target_architecture.md` §2.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Architectural Principles](#2-architectural-principles)
3. [Directory Structure](#3-directory-structure)
   - §3.3 [Module Boundaries and Bridge Architecture](#33-module-boundaries-and-bridge-architecture) ← **read this if touching any bridge or cross-module code**
4. [Existing Components — The Analysis Foundation](#4-existing-components--the-analysis-foundation) (incl. §4.6 User Preferences)
5. [Planned Analysis Extensions](#5-planned-analysis-extensions)
6. [The Style System](#6-the-style-system)
7. [The Knowledge Base](#7-the-knowledge-base)
8. [Planned Generation Components](#8-planned-generation-components)
9. [The Constraint System](#9-the-constraint-system)
10. [Visualization](#10-visualization)
11. [Intonation](#11-intonation)
12. [User Interface](#12-user-interface)
13. [File Persistence](#13-file-persistence)
14. [ML Readiness](#14-ml-readiness)
15. [Development Phases](#15-development-phases)
16. [Scope Reference](#16-scope-reference)
17. [Coding Standards](#17-coding-standards)
18. [Contributing](#18-contributing)
19. [LLM Integration — Claude Composer](#19-llm-integration--claude-composer)

---

## 1. Project Overview

### 1.1 Vision and Purpose

MuseScore Arranger is a harmonic analysis and arranging assistance system integrated
directly into MuseScore Studio's C++ core. It helps composers, arrangers, and musicians
working across the western music tradition by:

- Analyzing harmony, key, and mode in existing scores
- Suggesting chord voicings and progressions
- Assisting with voice leading optimization
- Supporting multiple musical styles from baroque to contemporary
- Providing intonation guidance for performed music

The primary users are musically literate MuseScore Studio users — arrangers, composers,
and musicians with some theoretical knowledge — ranging from students to professionals.

### 1.2 Relationship to MuseScore Studio

This system is implemented as a new module (`composing`) within MuseScore Studio's
existing C++ codebase. It is not a plugin. It integrates directly with MuseScore's
score model, rendering pipeline, playback engine, and UI infrastructure.

The long-term intent is for this to become an official contribution to MuseScore Studio.
All code follows MuseScore's coding standards, licensing requirements, and contribution
guidelines.

### 1.3 Licensing

All code is licensed under **GPL v3** — consistent with MuseScore Studio's open source
license. All external libraries used must be GPL v3 compatible.

The Contributor License Agreement (CLA) with MuseScore must be signed before any
pull requests are submitted.

### 1.4 Implemented Components

- **ChordAnalyzer** — identifies chord quality, extensions, inversions, diatonic
  degree, and chromatic (borrowed) Roman numerals from a set of simultaneously
  sounding notes
- **KeyModeAnalyzer** — infers the most likely key and mode from a temporal window
  of pitch contexts with duration, beat, and bass weighting
- **ChordSymbolFormatter** — formats analysis results as chord symbols and Roman
  numerals; non-diatonic chords produce chromatic numerals (♭VII, ♭III, ♭VI etc.)
  rather than returning empty
- **HarmonicRhythm** — detects harmonic boundaries across a score range, drives chord
  staff population
- **Chord staff** (also called the **chord track** elsewhere in this doc — the same object) — a grand-staff part added by
  the user that is populated on demand (an action called **implode**: write the harmonic reduction to the chord staff)
  with a harmonic reduction: chord symbols, Roman numerals, canonical or collected
  voicings, key/mode annotations, borrowed chord labels, pivot detection, and cadence
  markers. Notes on the chord staff have `play = false` (annotation-only; they do not
  double the source staves in playback)
- **Status bar integration** — displays chord, key/mode, and Roman numeral information
  when a note is selected
- **Intonation** — per-note and region tuning via split-and-slur; tonic-anchored JI
  places each chord root at its scale-degree position above the mode tonic rather than
  always at 0¢; optional minimize-retune shift and per-note cent annotation in score;
  sustained-event rewriting is controlled by user preference, existing tie boundaries
  may be converted to slurs when independent retuning is needed, and anchors protect
  the full written duration from segmentation
- **User preferences** — `IComposingAnalysisConfiguration` and
  `IComposingChordStaffConfiguration` expose analysis and output settings; preferences
  page in Edit → Preferences → Composing

The bridge layer (`src/notation/internal/notation*bridge*.cpp`) connects the
`composing` module to MuseScore's engraving model. All bridge functions are declared
in notation-side headers and live in the `mu::notation` namespace. The `composing`
module itself has **no engraving dependency** — it is pure music theory. See §3.3 for
the full bridge architecture.

*For current implementation status, test counts, known gaps, and immediate next steps
see STATUS.md.*

---

## 2. Architectural Principles

These principles apply to every line of code in this project. Claude Code should
treat them as hard constraints, not guidelines.

### 2.1 Style Behavior Is Fully Data-Driven

The C++ implementation contains no conditional logic based on style identity. All
behavioral differences between musical styles are expressed as parameter values in
style JSON files. Adding, renaming, or modifying a style never requires C++ code changes.

```cpp
// WRONG — never do this
if (style.id == "jazz_vocal") {
    applyJazzVocalSpecialCase();
}

// CORRECT — behavior driven by parameters
if (style.voicing.leadVoicePosition == LeadVoicePosition::SecondFromTop) {
    applyLeadVoiceLogic();
}
```

### 2.2 Interface-Based Design for ML Substitutability

Every component that may eventually be replaced or augmented by a machine learning
model must be defined behind a pure abstract interface. The rest of the system
depends only on the interface, never on a specific implementation.

```cpp
// Every major analytical and generative component follows this pattern
class IHarmonizer {
public:
    virtual ~IHarmonizer() = default;
    virtual std::vector<RankedChord> suggestChords(
        const MelodicContext& melody,
        const HarmonicContext& context,
        const StyleContext& style,
        const ConstraintStore& constraints
    ) = 0;
    virtual std::string explainSuggestion(
        const RankedChord& chord,
        const MelodicContext& melody,
        const HarmonicContext& context
    ) = 0;
};
```

### 2.3 Analysis Layer Is Display-Agnostic

Analysis components produce structured data — they never produce display strings.
Formatting is handled by separate formatter classes. This separation is already
established by `ChordSymbolFormatter` and must be maintained throughout.

### 2.4 No Conditional Logic Based on Style Identity

Closely related to 2.1. No `if (styleName == "...")` anywhere in the codebase.
Style-specific behavior flows entirely through the parameters in `StyleContext`.

### 2.5 American English Throughout

All identifiers, comments, and documentation use American English spelling.

```cpp
// CORRECT
HarmonicAnalyzer, VoiceLeadingOptimizer, visualize, behavior, color

// WRONG
HarmonicAnalyser, VoiceLeadingOptimiser, visualise, behaviour, colour
```

### 2.6 Musically Legible Documentation

Every class, method, and non-obvious data structure must be documented in terms
a person with reasonable musical knowledge and basic C++ familiarity can understand.
Comments explain the musical concept being implemented, not just the code mechanics.

See Section 17 for the full documentation standard with examples.

### 2.7 Low-Stability Decisions Are Refactorable

Directory structure, file naming, and internal organization can be refactored
efficiently with Claude Code assistance. Do not spend design energy on these.
Spend design energy on interfaces, data formats, and algorithms — things that
are genuinely expensive to change.

### 2.8 Follow MuseScore's Existing Patterns

Before implementing anything that touches MuseScore's existing infrastructure —
UI panels, score traversal, playback, settings, localization — read how MuseScore
already does it and follow the same pattern. Do not invent parallel infrastructure.

### 2.9 Analyze and Suggest — Never Modify Without Explicit User Action

The system presents analytical findings and suggestions. It never modifies the main score
automatically. All score modifications require explicit user action. The chord track, status
bar display, and visualization panels are informational — they show what the system has
inferred without changing anything. When the user wants to act on a suggestion — inserting a
key signature, adding a chord symbol, applying tuning — they do so explicitly through
standard MuseScore editing.

### 2.10 Single Implementation for Shared Logic

Any algorithm that must produce identical results in both the notation bridge and
`batch_analyze` belongs in the `composing` module (`src/composing/`), not in either
consumer. The bridge and `batch_analyze` are both consumers of composing-layer logic —
they should not contain their own copies of it.

Before implementing any new note collection, boundary detection, key/mode resolution,
or chord scoring logic:

1. First ask: does this belong in the `composing` module where both the bridge and
  `batch_analyze` can call it directly?
2. If yes: implement it there first, then wire both consumers to call it.
3. If a composing-layer implementation is not immediately feasible (dependency
  constraints, interface not yet designed), implement in one place only and
  immediately file a technical debt note. Do not copy-paste.
4. Mirroring (duplicating logic across the bridge and `batch_analyze`) is a last
  resort, used only when a shared implementation is blocked by dependency
  constraints that cannot be resolved in the current session. Any mirrored code
  must be marked with a TODO comment referencing this rule and the technical debt
  note.

**RESOLVED (Iter 97, commits `16b5bdfa57` Phases 2+3 / `045cb54e0d` Phase 4).** The two
duplicate regional collectors that previously lived in `notationcomposingbridgehelpers.cpp`
and `batch_analyze.cpp` have been unified into the `composing` module. `collectRegionTones()`
and friends now live in `composing/analysis/engravingbridge/regiontonecollector.{h,cpp}`,
`resolveKeyAndModeRanked()` in `composing/analysis/key/keyresolver.{h,cpp}`, and the entire
region-orchestration algorithm (segmentation → per-region scoring → absorb/merge → sparse
refinement) in `composing/analysis/region/regionanalyzer.{h,cpp}` +
`sparsechordrefinement.{h,cpp}`. Both consumers — the notation bridge
(`analyzeHarmonicRhythm`) and `batch_analyze` (`analyzeScore`) — are now **thin wrappers**
over `region::analyzeRegions()`; neither contains its own copy of the orchestration logic.
`detectHarmonicBoundariesJaccard()` was deleted (dead since the Iter 77 greedy-expand switch,
removed in Iter 81). See §3.3 "Region Analysis — Canonical Modules" for the full module map.

### 2.11 Score Inspection Before Diagnosis

When a corpus result is unexpected — agreement rate significantly above or below
neighboring corpora, high unmatched rate, zero-region files, or a suspected failure
mode — open a representative score in MuseScore Studio before running any diagnostic
scripts or changing any code.

Score inspection takes 2 minutes and answers questions that corpus statistics cannot:

- What is the actual texture? (SATB, Alberti bass, walking bass, running passages,
  pedal notation, arpeggiation)
- What does the chord track show? (over-segmentation, missing regions, wrong roots,
  empty spans)
- Is the key detection correct at the opening?
- Are pedal markings present and where?
- Is the harmonic rhythm fast or slow relative to what our region count implies?

Specific triggers that require score inspection before any other action:

- Any corpus with >20% drop or rise vs similar repertoire
- Any corpus with >30% unmatched annotation rate
- Any corpus with >10% zero-region files
- Any proposed scoring change that would affect a specific texture type
- Any new corpus being added to the validation suite — inspect at least 3
  representative scores before running `batch_analyze`

The developer (Vincent) performs score inspection in MuseScore Studio and reports
findings. Claude Code does not have direct score access and must not substitute
statistical inference for visual score inspection.

### 2.12 Benchmark Score Set

> *The "Rule N" labels in §2.11–§2.12 are a legacy flat numbering of the coding/process rules and do not align with the
> §-numbers (and appear out of order); the **§-numbers are authoritative**. Read each "Rule N" as a local name for the
> rule stated beside it, not a cross-reference to a numbered list.*

**Rule 12 — Benchmark score set**

Any change to the analyzer, bridge, or chord-track output must be evaluated visually against
the following three scores before committing:

| Score | File | Key passages |
|-------|------|-------------|
| Bach BWV 227.7 | `tools/corpus/bwv227.7.xml` | Bars 1-2, 8-10, final cadence |
| Chopin BI16-1 | `tools/dcml/chopin_mazurkas/MS3/BI16-1.mscx` | Bars 1-5, 10-16, trio |
| Dvořák op08n06 | `tools/dcml/dvorak_silhouettes/MS3/op08n06.mscx` | Early slow section, chromatic middle |


This is Rule 11 (score inspection before diagnosis) operationalized for the current
development phase. Open the score in MuseScore Studio, implode to chord track, and
confirm the key passages look reasonable before accepting any change. If a change
improves corpus numbers but worsens any benchmark passage visually, treat it as a red
flag and report before committing.

**Rule 14 — Shell discipline for long-running commands**

All build and test commands must run synchronously (foreground). Never use background jobs or split output.

Correct patterns:
```bash
# Build
cmake --build ninja_build_rel --target notation_tests --parallel 2>&1 | tail -20

# Tests — run once, capture tail
./ninja_build_rel/notation_tests.exe 2>&1 | tail -10

# Python scripts
python tools/test_batch_analyze_regressions.py 2>&1 | tail -5

# Long corpus runs — use tee
python tools/run_corpus.py 2>&1 | tee /tmp/corpus_run.txt | tail -5
# Then after completion:
cat /tmp/corpus_run.txt
```

Never do:
- `command &` (background job)
- Run, decide too slow, kill and re-run differently
- Check background task output more than once

One run, one result. If output is unexpected, report it and ask for instructions. Do not silently re-run.

**Rule 13 — Commit before session end**

Every development session must end with a git commit of all working tree changes, even if changes are incomplete or tests are partially failing. An uncommitted working tree that spans multiple sessions makes it impossible to identify what changed between sessions and prevents reliable diagnosis of regressions.

If tests are failing at session end:
- Commit with a clear message noting the failing test names
- Record the failing tests in STATUS.md current state summary
- Do not leave uncommitted changes

A commit with known failing tests is better than no commit. The commit history is the only reliable record of what changed and when.

Corollary: at session start (Rule 9 stale binary checklist), if the working tree is dirty, stash or commit before doing anything else. Never diagnose test failures in a dirty working tree without first knowing what changed.

**Rule 16 — Do not rely on chords.xml**

MuseScore has two chord description files:
- `share/chords/chords_std.xml` — the active standard chord list used by default in all scores
- `share/chords/chords.xml` — legacy file, likely deprecated, contains known bugs and inconsistencies with the parser

When our formatter produces a chord symbol string, it must be valid according to `chords_std.xml` only. Do not add chord symbol strings that exist only in `chords.xml` — they will fail to parse correctly under the Standard chord style and may produce corrupted output.

Confirmed example: `9sus` exists in `chords.xml` (id=134) but not in `chords_std.xml`. When used with Standard chord style, it triggers `generateDescription()` which produces a corrupted render list causing `Fsussus9` in the display. Fix: use `sus(add9)` instead which is correctly handled by the parser.

When adding new chord symbol formats, always verify against `chords_std.xml` first, not `chords.xml`.

### 2.13 Cross-Platform by Default

All code must run on every platform officially supported by MuseScore Studio: Windows,
macOS, and Linux. Platform-specific code is permitted only when absolutely necessary,
must be clearly documented, and must be abstracted so that the rest of the module
remains platform-agnostic. All build scripts, dependencies, and runtime logic must
be verified on all supported platforms before merging.

### 2.14 Layered AND Iterative Inference

Clean layer separation (§2.3, §4.1 design boundary) is necessary but not sufficient.
The inference problem has intrinsic circular dependencies that a purely feedforward
pipeline cannot resolve correctly:

- **Key ↔ chord**: the key affects how each chord is scored; the chords confirm or
  refute the key. Committing the key before chord analysis means the chord scorer
  operates under a hypothesis, not a fact.
- **Segmentation ↔ chord**: where a region boundary falls affects which pitch classes
  land in each region's oracle input; chord identity is a signal for where boundaries
  should be. `greedyExpandSegmentation` already acknowledges this by running its
  exploratory passes in `ScoringPhase::Segmentation` (progression signals withheld).
- **Non-harmonic tone classification ↔ chord**: whether a sounding pitch is structural
  or ornamental depends on knowing the chord; knowing the chord depends on which pitches
  are structural.
- **Functional role ↔ chord identity**: resolving B1 (mMaj7 leading-tone ambiguity),
  A2 (dominant in minor), and the Δ=+7b voice-leading cluster requires knowing functional
  role (is the leading tone resolving?), which requires knowing chord identities, which
  requires knowing functional role.

**The correct architecture is layers WITH iteration between them.** Layers define what
each component is *responsible for*; iteration defines how information flows *between*
them over multiple passes. These are complementary, not in tension.

**Accumulating gates are a warning sign.** When a feedforward layer acquires many gates
and guards to compensate for missing upstream feedback, that is a symptom of missing
iteration — not a sign that the layer needs more gates. Each gate is a heuristic patch
on a structural limitation. When the gate count becomes hard to reason about holistically
(see §4.1i), add iteration rather than more gates.

**Quality/ambition setting governs iteration depth.** Iteration is not unconditionally
expensive — for well-tonal music most loops converge in 1–2 passes. Computational cost
is managed by an explicit user-facing quality setting:

| Level | Name | Iteration | Use case |
|---|---|---|---|
| 0 | Fast / Real-time | None (single forward pass) | Cursor annotation, playback display |
| 1 | Normal | Key ↔ chord (1–2 passes); segmentation revision | Background analysis, default export |
| 2 | Deep / Publication | Full convergence; all feedback loops active | LLM-assisted annotation, academic output |

At Level 0 the system promises a fast plausible reading. At Level 2 it promises the most
self-consistent reading achievable. The quality setting makes this tradeoff explicit and
honest rather than silently failing on hard cases.

**Design implication for data structures:** Each layer's output must carry a confidence
estimate (the **winner margin** — the rank-1 minus rank-2 score gap, §5.7; the key confidence gap; segmentation
stability) so downstream layers
know whether to treat a result as a solid commitment or a tentative hypothesis worth
revisiting. Irrevocable point estimates block iteration. Provisional results with
confidence metadata enable it. Infrastructure already started: winner margin
(`previousWinnerMargin`), key ranked list (`resolveKeyAndModeRanked`).

**Phase D resolves the NHT/arpeggio circularity before Phase E iterates.** The current
system infers a chord at every tick boundary and then tries to filter out "passing-note
anomalies" retroactively. This is circular: identifying a note as passing requires knowing
the chord; knowing the chord requires knowing which notes are structural. The correct
resolution is duration-weighted aggregation: collect all tones within a rhythmic window
(beat-level or bass-motion boundary) weighted by duration, then run a single chord
inference on the aggregate. A brief passing tone contributes low weight; a sustained
structural tone (or an arpeggiated root that sounds across the beat) contributes high
weight. This is a prerequisite for Phase E — the feedback loop requires stable,
arpeggio-resolved chord identities as input. Design reference: `docs/redesign_plan.md`
Step 4 (Phase D).

**Phase E is the first iteration loop**, not just a new layer. Cadence detection creates
a feedback signal from functional labels back into chord identities (a confirmed V→I
cadence revises the chord identities participating in it and confirms the key). Design
Phase E as a bidirectional interface, not a unidirectional gate addition.

> **⚠ SUPERSEDED 2026-06-29 — read the next block first.** The 2026-06-10 reconciliation immediately below proposed a
> *global joint-lattice decode*; that mechanism was later measured **inert** and the ratified architecture is
> **forward-only** (the 2026-06-29 reconciliation that follows). The 2026-06-10 block is **retained only as history** — do
> not build to it.

**Reconciliation (2026-06-10) — SUPERSEDED; see the 2026-06-29 reconciliation below.** This
section and `docs/redesign_plan.md` ("single comprehensive pass; iteration is not a design
premise") name the same target imprecisely. The standard resolution of the circular
dependencies listed above is **joint inference over a hypothesis lattice**: each layer emits
ranked candidates with scores (chord cells per region, key candidates per window,
segmentation hypotheses), and a global decode (Viterbi / beam search) selects the jointly
best path. This *is* the single comprehensive pass, and it equals the fixpoint that
iteration between layers would converge to — computed exactly, with "revise an earlier
commitment on later evidence" arising automatically from backtracking rather than from
bespoke revision machinery. The quality levels above map onto beam width (Level 0 = beam 1
≈ current greedy behavior; Level 2 = exact DP). Full rationale and literature comparison:
`cowork_target_architecture_review.md`; adopted Phase E direction:
`docs/redesign_plan.md` "Architecture review addendum (2026-06-10)".

**★ Reconciliation (2026-06-29) — SUPERSEDED: the joint-lattice decode gave way to forward-only + a gated step.**

**★ Scoping annotation (user ruling, 2026-08-02, at the OI-234 decision-conflict adjudication — reading 3).**
The finding below STANDS FOR WHAT IT TESTED and is not withdrawn: global cycling / re-ranking over
the per-layer pipeline's carried candidate lists adds nothing, and that remains binding on any
future cycling-style design (#12 — an exclusion is information). It DOES NOT BEAR ON the fitted
semi-Markov joint decode ratified 2026-07-17 (the governing banner at the top of this document)
and adopted 2026-07-26 — a different mechanism class (ONE generative decode over a joint
(tonality, mode, chord) state space with fitted factors), whose gain was measured at the adoption
(root agreement 66.0 → 77.0 on the robust unit). The "not by a joint decode" conclusion below is
therefore scoped to lattice/beam cycling over per-layer candidates. Register entries D-025/D-026
carry the scoped statuses.

The 2026-06-10 "joint inference over a hypothesis lattice / global Viterbi–beam decode" above named the right
*goal* (revise an earlier commitment on later evidence) but the wrong *mechanism*. The subsequent investigation
**measured the full joint cross-layer search INERT** — the realisable gain is soft-evidence *quality* carried
forward (calibrated confidence + ranked alternatives), not the global cycling — so the architecture spends its
effort on good forward evidence, not on a beam search. The **ratified** architecture (user-ratified;
`cowork_target_architecture.md` §2) is **forward-only**:
- each layer is feed-forward and emits **ranked candidates + a confidence**, never a forced point estimate;
- "revise on later evidence" is the **confidence-weighted forward-override** — a confident commit is overturned
  only when contradicting later evidence crosses a threshold scaled to its confidence, firing a **localized
  forward recompute** (one pass, region-scoped, no back-edge), *not* a global backtrack;
- the one residual genuinely-coupled decision (key↔chord on the relative-pair / short-modulation cases) is a
  **gated, constrained joint step (Stage 5)** that fires only on the flagged minority, leaving the clean majority
  feed-forward.
So the circular dependencies listed above are real, but resolved **forward** (the slicer owns segmentation; L4
owns chord + non-chord-tone together; the cadence-confirmed key override and the function→chord override are
forward recomputes), not by a joint decode. The quality-levels table still holds as the *cost* dial but no longer
maps to beam width — it is the **effort preset** (quick / normal / ambitious), a *calibration* knob (not a structural
one), added after profiling. Its two standing design rules hold from the start: **(a)** every cost-driving choice is an
explicit *setting*, never a hardcoded constant; **(b)** every optional expensive refinement is a cleanly separable on/off
stage. The `docs/architecture_joint_inference.md` joint-decode synthesis is **superseded** by this, retained only as
history.

### 2.15 The core principle and the cross-cutting analysis contracts (ratified; full statements in `cowork_target_architecture.md`)

**The founding principle: analyze at the finest grain where harmony is well-defined, and make everything coarser a
*derived view*.** The atomic analysis unit is the **constant-sonority slice** (L2), never the metric beat; phrases,
key-areas, and sections are *groupings* derived from the per-slice analysis, not primary objects. This is what makes
segmentation a fact rather than a judgment (over-grab becomes structurally impossible, §3.3 L2), aligns the architecture
with the per-slice oracle metric we already built, and matches the SOTA shape (Contrapunctus labels every event). The
contracts below all serve this principle. Their detailed statements live in the target-architecture doc.

- **Universality in the fact layers; style only in calibration.** L1 (notes) and L2 (slicing) are **style-agnostic and
  lossless** — they carry facts, never style. Style-specificity lives **only** in the *calibration* of the judgment
  layers (their priors/weights), **never in structure**. (This sharpens §2.1: not merely *data-driven* style, but style
  confined to the layers that may carry it at all.)
- **The confidence-weighted forward-override** (§2.14) — any layer's confident inference is overturnable by decisive
  later evidence via a localized forward recompute; its instances are the cadence-confirmed key modulation and the
  fine-grain chord override. **Forward-only is a strong *default*, not dogma:** a sanctioned backward edge is admissible
  only as a deliberate, surfaced, measured, documented exception (justified by a plateau, scoped, gated,
  convergence-bounded, recorded). *The quantities this mechanism compares are governed by the **cross-layer confidence
  & calibration contract** (`cowork_confidence_contract.md`, review amendment A-1, **RATIFIED by the user
  2026-07-02** — corrected 2026-08-02, `OPEN_ITEMS.md` OI-232 item 5: this parenthetical read
  "ratification-gated", so a reader of the canonical document alone would have concluded the contract does not
  yet bind, which is the precise reading under which the production record path departs from it, OI-231):
  every boundary confidence is [0,1], class-declared (margin vs calibrated probability), and cross-layer comparisons
  happen only in the contract's declared frames. The contract's own rule and its defense are stated as a
  cross-cutting contract in the list below.*
- **The span typology** — a "region" is a *family* of spans, each named by its bounding criterion. *(★ FAMILY RENAME
  ✅ CONFIRMED (user, 2026-07-02) — ✅ EXECUTED at the merged Cowork doc pass (2026-07-03) across the **Cowork design
  documents and the schema dictionary**. **Scope correction, 2026-08-02 (`OPEN_ITEMS.md` OI-233): this clause
  claimed the rename was "propagated through every layer spec", and in THIS document — the canonical layer
  specification — it was not. The bare word is still used throughout, including in four section headings a reader
  navigates by (§3.3 "Region Analysis — Canonical Modules", §4.1 "Region identity modes", §11.5 "Region Analysis
  and the Chord Track", §11.6 "Region Intonation") and in the load-bearing Layer-3 prose, where the reader must
  work out unaided that "region" means the chord-span.** Bringing this document into line is a scoped terminology
  pass and is NOT executed here: it must be sequenced against the standing music-theory-terminology convention
  (`OPEN_ITEMS.md` OI-229), under which existing names are not renamed unilaterally, and it is a judgment call in
  §11.5/§11.6, where "region" sometimes names a user-selected stretch rather than an analytical one. The ban itself
  is unaffected and stands for all NEW text. The renames the 2026-07-03 pass did carry out:
  **harmonic region → chord-span** (the typology bans "region" unqualified, yet its
  own atomic member carried the banned word; "the span one committed chord prevails over" is the criterion) ·
  latent **sequence-span → progression-schema-span** (D6, ratified) · latent **pedal span → pedal-point-span**
  (pedal point ≠ the piano's pedal) · **section-span / voice-leading-span** (suffix-consistent) · key-span /
  punctuation-span / decision-context span KEEP · **cadential scope** KEEP as the deliberate non-"span" exception —
  it names a relation (the span a cadence closes AND confirms), not a segmentation.)* The current names: the
  **chord-span** (chord-rhythm — the span one committed chord prevails over, a maximal run of same-chord
  constant-sonority slices; the atomic member, formerly "harmonic region") · the **key-span** · the
  **punctuation-span** (the flat,
  surface-punctuation-delimited grouping span — the DCML `{}` unit Layer 6 owns; **renamed from "phrase" 2026-07-01** so
  that "phrase [MT]" denotes *only* the accepted **melodic** phrase, which is a voice-leading-axis object, not this one —
  see `cowork_layer6_grouping_design.md` §0) · the **decision-context span** (the
  bounded look-ahead a deferred decision integrates over — bounded by the deferring layer's stop condition and hard bound,
  per the Bounded-context contract below) · the **cadential scope** (the span a cadence closes *and*
  confirms — where a punctuation-span and a key-span are *jointly* articulated, which is why one cadence detector feeds both
  grouping and key) · the **progression-schema-span** (emitted by the recognition consumer, hosted by Layer 6) · the
  latent **section-span / pedal-point-span / voice-leading-span**. They relate by **nesting**
  (chord-spans ⊂ key-spans; chord-spans ⊂ punctuation-spans; punctuation-spans ⊂ section-spans) **or cross-cutting**
  (key-spans and punctuation-spans cross-cut — a key change may fall mid-span; progression-schema-spans cross-cut
  both). "Region" unqualified is **banned** as
  ambiguous; every layer names the span it operates on. (After the GTTM premise of independent structures.) *(The **cue
  that delimits** a punctuation-span is still supplied by the Layer-1.5 **phrase-boundary primitive** — that upstream
  primitive keeps its code name; only the grouping-**span** term changed.)*
  **★ voice-leading-span — criterion given (2026-07-03):** the span **one texture classification prevails over** — a
  maximal run carrying one voice-leading idiom; owner = the axis-2 texture classifier **VL-C**; v1 = the whole selection
  (one span) until the §15-1 per-span measurement refines it. Criterion + build home:
  `cowork_voiceleading_axis_design.md` §0/§5.3 (AS-BUILT). *(section-span / pedal-point-span remain latent.)*
- **The verifiability contract** — prefer what we can verify against ground truth (it is how we catch our own theory
  errors); for sound theory we cannot verify against the current corpus, build it with an explicit
  **alternative-confidence path** *and* an **"empirically-unvalidated" mark**, rather than refusing it (this governs the
  jazz/pop reach, where we have theory but no corpus).
- **Bounded context** — analysis runs on the user's *selection*; a layer needing more requests an **append-only**
  extension from L1 (a data-supply call down the stack, not an analysis back-edge), carrying a stop condition and a hard
  bound. The binding scale requirements: **(R1)** cost scales with the working span, not the whole score; **(R2)**
  re-analysis is incremental over the dirty span plus a bounded margin; **(R3)** the working span is **extensible** (a
  fixed margin plus lazy extension). Whole-score analysis is the degenerate case (selection = score). *(The ONE
  detailed cross-layer spec for this contract is **`cowork_bounded_context_design.md`** — the request→supply→bounded-
  recompute protocol, the per-layer discovery rules incl. the pinned L5 decision-context extent, denial provenance,
  and the §11 acceptance list. Per the 2026-07-02 user directive it is the **hard gate before L6**: ratify → code →
  regression-test L1–L5, then L6 resumes. A short-lived duplicate contract doc was killed into it same day.)*
- **Single-responsibility / minimality + maximal information** — each layer owns one *(evidence-source × question)*
  contribution — stated as "owns the *[named evidence]* contribution to *X*", with what it does **not** own made
  explicit — defers what needs later evidence (carried as ranked alternatives + an uncertain mark), and within its scope
  uses *all* the information L1 carries losslessly (notated spelling, metric weight, voice).
- **Layers are not one homogeneous stack, and the count is not a cap.** The numbered layers span **three kinds of
  work**: **representation** (L1 lossless notes, L1.5 derived views, L2 mechanical slicing — facts and segmentation, *no*
  harmonic decision), **inference** (L3 key, L4 chord, L5 function — the only *decision* layers), and **assembly** (L6
  grouping — organizes the finished decisions into a view; decides nothing new, read-only, downstream). "Six" is the
  *current* decomposition of the **harmonic spine**, not a ceiling: the architecture already carries more than six named
  elements — the **L1.5** half-tier, the **Harmonic Vocabulary** (a separate queried component, off the spine), the
  **recognition consumer**, and the **orthogonal voice-leading axis** with its own layers (where melodic phrases [MT] and
  chord **voicing / arrangement** are analysed) — **★ axis-2 status (2026-07-03): the foundation is BUILT (dormant) —
  VL-A voice-linear view + VL-B motion/interval profiles (facts) + VL-C texture classification (the one v1 judgment:
  texture-of-span, Class M) + its bounded-context requester; measured orthogonal to the harmonic spine (cross-ARI 0.030);
  VL-D/E/F/G/H named + design-gated (`cowork_voiceleading_axis_design.md`)** — and higher grouping structure (sections /
  periods / form) is explicitly
  anticipated *above* L6 (`cowork_layer6_grouping_design.md` §9-D3), deferred, not forbidden. Growth is **by axis and by
  component**, not by climbing a fixed tower. **A new layer or axis is admitted only when it clears three co-equal gates,
  all required:** **(1) separation of concerns** — it carries *one* responsibility that must not sit mixed into another;
  this is a **structural mandate, sufficient on its own** to justify a split even at *zero* immediate accuracy gain, and
  the primary reason the stack is decomposed at all. **(2) verifiability** — there is a way to validate it (or an explicit
  alternative-confidence path + "empirically-unvalidated" mark). **(3) proportionality** — it buys explainability or
  accuracy we can *actually check*, never a slot filled for symmetry (the Contrapunctus reminder: SOTA-competitive with
  **no** explicit grouping layer — do not multiply layers for their own sake). Gate (1) is **not** subordinate to (2)–(3):
  a genuine second concern earns its own component regardless of the immediate metric.
- **The cross-layer confidence contract — every confidence that crosses a layer boundary is bounded,
  class-declared, and named to its decision.** At a layer boundary — any value another layer may read — a
  confidence is **in [0,1], class-declared (a ranking margin or a calibrated probability), and stated
  together with the decision it is the confidence of**. Unbounded content scores are permitted *inside* a
  layer and must be squashed at the boundary. *Why:* the §2.14 confidence-weighted forward-override compares a
  later layer's contradiction strength numerically against an earlier layer's confidence, and those two
  quantities are incommensurable as published today — Layer 3 publishes a sequence margin, Layer 4 a
  three-part composite, Layer 5 an unbounded additive content score — so the comparison has no defined
  meaning, and fitting weights over it would bury the incoherence in fitted constants instead of repairing
  it (`cowork_confidence_contract.md:13-21`). Ratified by the user 2026-07-02; the class vocabulary, the
  squashing rules and the declared comparison frames are stated in full in `cowork_confidence_contract.md`,
  which this contract points at rather than restates. **The production notation record path departs from
  this contract**: it publishes the key-axis gap raw, in nats, with no remapping to [0,1] (the record path,
  subsection (4) at the head of this document). The departure is recorded and unresolved at
  `OPEN_ITEMS.md` OI-231; this contract is the standard that departure is measured against, not a
  description of the shipped record path.
- **Negative evidence is information — a ruled-out reading is carried, not dropped.** A layer that
  eliminates a reading publishes the elimination rather than discarding it: the ruled-out reading is
  carried on the output surface at low confidence, unless the elimination is recomputable from what that
  surface does keep. *Why:* guiding principle #12 (`CLAUDE.md`), ratified by the user 2026-07-06 — finding
  by exclusion is a result, and a surface that keeps only survivors cannot tell a later layer the
  difference between a reading never considered and a reading considered and rejected. The
  recomputable-exclusion exemption is what stops the rule from forcing every layer to publish its entire
  candidate space.
  **The rule's boundary, stated because an earlier framing got it wrong: NEVER COMPUTING a possibility is
  not information loss; only DISCARDING a computed one is.** A layer that decides, on measured evidence,
  not to work out a particular alternative at all has lost nothing — you cannot lose what you never had.
  What the rule forbids is computing a reading and then dropping it off the output surface. *Why:*
  recorded as an explicit correction of a framing that had called the same situation a violation of this
  principle. The worked case is the shelved joint key-and-chord step: the chord under an alternative
  tonality is never computed on that path, the tonality alternatives themselves ARE carried, and the
  roughly 1.4 % of slices where the alternative would have differed was measured to be an even split —
  that is, noise. Decided 2026-07-07; the record does not name the ratifier.
- **Every derived analytical fact is published exactly once, on the producing layer's output surface;
  consumers read it and never re-derive it.** For **evidence-class** facts — hints a later design could
  conceivably use — publication is broad even where no consumer is named yet, and each published evidence
  fact carries its **establishment status** on the surface, because a consumer may not put an unestablished
  fact under load (#19). A published fact that no one reads is either **declared dormant**, with its future
  consumer named, or removed. *Why:* `cowork_siloed_facts_audit.md` found 17 instances of a fact being
  re-derived by a consumer instead of read from its producer. Ratified by the user 2026-07-10 and amended
  2026-07-12 (`CLAUDE.md`, the fact-publication corollary); the user's recorded reason for the broad-
  publication amendment is that a visible spread of published evidence lets a future design recognize facts
  it would never have thought to ask for. The catalog of what each layer discovers is
  `cowork_evidence_inventory.md`, kept in step with these layer specifications as facts are adopted.
- **The analysis always emits its FULLEST reading; simplifying a reading is a comparison-side act and
  never a product one.** When a layer names a chord it states everything it found, the added notes above
  the basic triad included. Cutting a name back to a plainer one — dropping an extension so that two
  differently-notated readings can be compared — belongs only to the machinery that grades us against a
  published corpus, and must not exist on any path a user's result travels. *Why:* measured — applying
  the comparison-side simplification reduced a pinned baseline from 135 differences to 10, which is the
  size of the pure notation-convention difference the rule keeps out of the analysis; without the rule
  that difference would be counted as analytical disagreement. Implemented as a test-only utility
  (`stripSymbol`, `classifyComparison`) with the design memo `docs/extension_stripping_policy.md`; the
  record states neither a date nor a ratifier for the rule itself.

### 2.16 Standing design requirements — very large scores, and the effort control

Two requirements the user stated on 2026-07-28 at the analysis-cost review. They are **requirements, not
defect reports**: every later inference and notation design is judged against them. Both were until
2026-08-02 recorded only on an open-item row, which tracks work rather than housing a standing decision.

- **Very large scores MUST be handled, and are expected to be a MORE COMMON use than our corpora.** A
  Wagner act or a symphony has to produce an analysis; the user expects such music to be a more common
  use of this system than the chorales it was fitted on. *Why:* stated by the user as a standing
  requirement, and recorded together with the collision it creates — the joint estimator's ratified
  tractability envelope is chorale size (roughly 60–150 events at exact decode) and its fitted material
  is 326 Bach chorales by one composer, so the requirement names music the estimator was neither fitted
  nor established on. Tracked at `OPEN_ITEMS.md` OI-209; the measured collision is OI-215 and OI-227 —
  the decode returns an empty analysis on 13 of the 23 committed large scores.
- **The effort control is ONE setting with several dials behind it, and among the quantities it must
  bound is the TIME the analysis takes. DEFERRED.** How hard the analysis works is a single user-facing
  setting, not several; several dials sit behind it; and a temporal bound is one of the things it must be
  able to impose. *Why:* it is too early to build, because which parts of the analysis have to be
  switchable is not yet known factually, and establishing that is a measurement rather than a design
  choice. The user's prediction recorded beside the requirement, verbatim: *"always read the entire score
  will VERY likely not survive (maybe only under some effort setting = EXTREME)."* The two older standing
  design rules this control must satisfy are already stated in §2.14: every cost-driving choice is an
  explicit setting, never a hardcoded constant; and every optional expensive refinement is a cleanly
  separable on/off stage. Tracked at `OPEN_ITEMS.md` OI-209.

---

## 3. Directory Structure

### 3.1 Module Layout

The new code lives in `src/composing/` within MuseScore's source tree. This
namespace and directory are already established by the existing chord and key/mode
analyzers.

```
src/
  composing/                        ← NEW module — pure music theory, NO engraving dependency
    CMakeLists.txt
    composingmodule.cpp/.h          ← registers IComposingAnalysisConfiguration +
    composingconfiguration.cpp/.h      IComposingChordStaffConfiguration in IoC
    icomposinganalysisconfiguration.h  ← analysis+tuning prefs; IoC-registered
    icomposingchordstaffconfiguration.h← chord staff prefs; IoC-registered
    icomposingconfiguration.h          ← composite base (NOT IoC-registered; see §3.3)

    analysis/                    ← existing, fully working
      chord/
        ichordanalyzer.h          ← IChordAnalyzer interface
        chordanalyzerfactory.h/.cpp ← ChordAnalyzerFactory
        chordanalyzer.h/.cpp      ← RuleBasedChordAnalyzer implementation
        keycollectionprobe.h/.cpp ← OI-168 measurement scaffolding: default-OFF branch
                                    counters + the default-OFF signature-mask A/B variant
                                    of the two key-consuming scoring terms. Reads nothing
                                    the analyzer consumes; removable in one revert.
      key/
        keymodeanalyzer.h/.cpp    ← KeyModeAnalyzer, all 21 modes
      region/
        harmonicrhythm.h          ← HarmonicRegion struct (types only)
      analysisutils.h             ← pitch-class helpers shared across subdirectories

    intonation/                  ← existing, fully working
      tuning_system.h            ← TuningSystem abstract base, TuningRegistry
                                    (no bridge decls — those are in notation/)
      tuning_keys.h
      tuning_utils.h
      equal_temperament.h/.cpp
      just_intonation.h/.cpp
      pythagorean.h/.cpp
      quarter_comma_meantone.h/.cpp
      werckmeister.h/.cpp
      kirnberger.h/.cpp

    tests/
      chordanalyzer_tests.cpp
      chordanalyzer_musicxml_tests.cpp
      keymodeanalyzer_tests.cpp
      synthetic_tests.cpp            ← P6 parametrized suite (root coverage, inversions, modes, round-trip)
      tuning_tests.cpp
      chord_mismatch_report.txt      ← written by catalog test run

  notation/
    internal/
      notationanalysisinternal.h     ← internal helpers shared between bridges:
                                        isChordTrackStaff(), staffIsEligible()
      notationcomposingbridge.h/.cpp ← BRIDGE: analyzeNoteHarmonicContext(),
                                        analyzeHarmonicRhythm(), harmonicAnnotation()
                                        Declared AND defined in mu::notation namespace.
      notationimplodebridge.h/.cpp   ← BRIDGE: populateChordTrack()
      notationtuningbridge.h/.cpp    ← BRIDGE: applyTuningAtNote(), applyRegionTuning()
      notationinteraction.cpp        ← NotationInteraction methods incl. composing ops
                                        (implodeToChordTrack, tuneSelection,
                                         addAnalyzedTuning, addAnalyzedHarmony*)
      notationaccessibility.cpp      ← status bar; calls harmonicAnnotation()

  notationscene/
    qml/MuseScore/NotationScene/
      notationcontextmenumodel.cpp   ← right-click menu; calls mu::notation::
                                        analyzeNoteHarmonicContext() via bridge header

  appshell/
    qml/MuseScore/AppShell/
      appmenumodel.cpp/.h            ← top bar "Tune as" and chord track menus;
                                        injects IComposingAnalysisConfiguration

  preferences/
    qml/MuseScore/Preferences/
      composingpreferencesmodel.cpp/.h ← injects BOTH IComposingAnalysisConfiguration
                                          AND IComposingChordStaffConfiguration

  composing/
    resources/
      styles/                    — style JSON files (planned)
      knowledge/                 — knowledge base JSON files (planned)
```

**Planned but not yet present:** `generation/`, `knowledge/`, `visualization/`, `ui/`, `constraints/` subdirectories and their contents (see §§6–10).

### 3.2 Namespace

| Namespace | Where it lives | What goes here |
|-----------|---------------|----------------|
| `mu::composing::analysis` | `src/composing/analysis/` | Pure analysis types and algorithms (ChordAnalyzer, KeyModeAnalyzer, ChordSymbolFormatter, HarmonicRegion struct, …) |
| `mu::composing::intonation` | `src/composing/intonation/` | Tuning systems (TuningSystem, TuningRegistry, concrete systems) |
| `mu::composing` | `src/composing/` | Configuration interfaces (IComposingAnalysisConfiguration, IComposingChordStaffConfiguration) |
| `mu::notation` | `src/notation/` | **All bridge functions** — functions that require engraving access but produce composing-domain results live here, not in `mu::composing`. This is the primary rule of the bridge layer. See §3.3. |
| `mu::notation::internal` | `src/notation/internal/` | Internal notation helpers (isChordTrackStaff, staffIsEligible) |

**Critical rule:** If a free function requires `mu::engraving` types as parameters, it belongs in `mu::notation` regardless of what it returns. The `composing` module must not forward-declare or depend on engraving types.

### 3.3 Module Boundaries and Bridge Architecture

> **Read this section before touching any code that crosses the composing ↔ notation boundary.**

#### The Dependency Rule

```
engraving     ← knows nothing about composing or notation
    ↓
composing     ← pure music theory; NO engraving dependency whatsoever
    ↓              (no forward declarations, no includes of engraving headers)
notation      ← bridges both; owns all bridge function declarations and definitions
    ↓
notationscene ← calls notation bridge API; does NOT include composing headers directly
appshell      ← calls notation API; injects composing config interfaces
preferences   ← injects both composing config interfaces
```

This dependency order is **enforced**. Any code that would invert it (e.g. a composing header forward-declaring `mu::engraving::Note`) must be moved to the notation bridge layer.

#### The MuseScore-Dependency Rule (user-ratified 2026-08-02, at the OI-241 adjudication)

Which existing MuseScore code our code may depend on, stated once — the general rule the scoped
forms in this document instantiate:

1. **The analysis library (`composing`) depends on no MuseScore or engraving types** — the
   Dependency Rule above, unchanged.
2. **The bridge layer reads the score model only through the established bridge pattern, and
   never layout-derived state as analysis input.** The Layer-1 note model is the single
   sanctioned reading surface for analysis facts; positions, spacing and other layout products
   are presentation outputs, readable only for placing presentation artifacts, never as
   inference evidence (a layout read entering analysis is the OI-98 class, judged against this
   rule).
3. **Editing MuseScore's own code is admissible only for a defect blocking our feature.** Each
   instance is recorded in `CLAUDE.md`'s local-patches section with a do-not-revert note and an
   explicit per-instance distribution disposition (upstreamable or fork-local), ratified by the
   user. The recorded contribution intent (§1.2) governs our module as a whole; distribution is
   decided per patch — the fork-local constraint on the MusicXML mode-import patch is such an
   instance, not a contradiction of the intent.
4. **READING and CALLING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING
   the notation and engraving source is off limits.** Clause 3's prohibition is on changing
   `src/notation` and `src/engraving` code, not on consulting it: any code we are entitled to write may
   read from and call into MuseScore's score and engraving model. *Why:* a user correction, 2026-06-14,
   of an over-statement that had conflated the two, with its worked consequence recorded beside it — a
   measurement that needed fermatas read them in the batch tool, which already loads the score, and
   passed them into our own analysis through our own input structure, so nothing outside our area was
   edited. Clause 2 above is the narrower rule that still governs what such a read may be used FOR: the
   Layer-1 note model is the only sanctioned reading surface for analysis facts, and layout-derived
   state is never inference evidence.

*Why this rule: derived from the already-ratified scoped forms (the Dependency Rule, the bridge
pattern, the local-patches constraints) rather than invented (#1); one rule where
practice-by-example governed (#6/#7); the layout exclusion because layout is presentation
downstream of the facts, and analysis consuming it is a layer inversion and the self-feedback
class the input-scoping work guarded against; the per-instance patch ratification preserves #14
and reconciles the §1.2 contribution intent with the fork-local patch constraint.*

#### Why This Matters

The `composing` module is a pure C++ music theory library. It can be unit-tested in complete isolation from MuseScore's engraving model — no score, no staves, no UI, just pitch classes and algorithms. This isolation is what makes the test suite (`composing_tests.exe`) fast and reliable.

If `composing` headers imported engraving types, the unit tests would need to link against the full engraving library. More fundamentally, it would mean the music theory library had knowledge of a specific score representation format — a structural coupling that makes the algorithms harder to reuse or replace.

#### The Bridge Pattern

A "bridge function" is a free function that:
- Takes engraving types as input (Note*, Score*, Fraction, …)
- Produces composing-domain results (ChordAnalysisResult, HarmonicRegion, …)
- Lives in `mu::notation` namespace
- Is declared in a `notation/internal/notation*bridge.h` header
- Is defined in the corresponding `notation/internal/notation*bridge.cpp`

**Callers** of bridge functions include only the notation-side bridge header, not composing headers, for the function itself. They may still include composing headers for the composing types in the function signature.

#### Bridge File Inventory

| File | Declares/defines | Called by |
|------|-----------------|-----------|
| `notationcomposingbridge.h` | Declares `harmonicAnnotation()`, `analyzeNoteHarmonicContext()`, `analyzeHarmonicRhythm()`, and `HarmonicRegionGranularity` | `notationaccessibility.cpp`, `notationinteraction.cpp`, `notationcontextmenumodel.cpp`, `notationimplodebridge.cpp`, `notationtuningbridge.cpp` |
| `notationcomposingbridge.cpp` | `harmonicAnnotation()` — status bar string<br>`analyzeNoteHarmonicContext()` — single-note analysis | (implements declarations above) |
| `notationharmonicrhythmbridge.cpp` | `analyzeHarmonicRhythm()` — time-range harmonic scanner | (implements declaration above) |
| `notationcomposingbridgehelpers.h/.cpp` | Shared bridge helpers: `collectSoundingAt()`, `buildTones()`, `collectPitchContext()`, `resolveKeyAndMode()`, `findTemporalContext()`, … | `notationcomposingbridge.cpp`, `notationharmonicrhythmbridge.cpp` |
| `notationimplodebridge.h/.cpp` | `populateChordTrack()` — write harmonic reduction to chord staff | `notationinteraction.cpp` (via `implodeToChordTrack()`) |
| `notationtuningbridge.h/.cpp` | `applyTuningAtNote()` — tune a single note's chord<br>`applyRegionTuning()` — tune a time range | `notationinteraction.cpp` (via `addAnalyzedTuning()`, `tuneSelection()`) |
| `notationanalysisinternal.h` | `isChordTrackStaff()` — name-based chord staff detection<br>`staffIsEligible()` — exclude drums/hidden/chord-staff staves | `notationcomposingbridgehelpers.cpp`, `notationtuningbridge.cpp`, `notationimplodebridge.cpp` |

**Layer status legend.** Each layer below is tagged with exactly one build state: **Built+Live** (wired into the
production pipeline), **Built+Dormant** (built and tested but not wired — reachable only via diagnostics, byte-identical on
production), or **Design-only** (specified, not yet built). Per-date and per-commit provenance lives in STATUS.md and the
`cc_*` reports, not here.

**Two terms used throughout these layer docs.** **L1.5** is the thin *derived-view* layer over the L1 note model — the
spelling / `engravingbridge` views (the shared `lineOfFifths` spelling interpreter, the phrase-boundary primitive); it is
a view, not a judgment layer, which is why it is numbered 1.5. **BIR** (bass-is-root) is the corpus gate metric: a
BIR=false case is a *pitch-class-decidable* root the analysis got wrong, and the gate is quoted as `Baroque/Jazz/Default`
case counts (e.g. `53/24/53`); the "class-(a)/(b)" split and the full definition live in the gate policy (CLAUDE.md).

#### Layer 1 — the lossless note model (Built+Live)

The analysis pipeline is being rebuilt **upstream-first** onto the ratified 4-layer target
(`cowork_target_architecture.md`): **note model (L1, DONE) → change-point slicing (L2, BUILT —
wired, consumed by L3) → per-slice analysis with context (L3) → grouping for display (LN).** Layer 1 is built
and ratified (commits `edd33901ed` standing oracle-root metric tool, `e30bb45a4f` the note model,
`4055f89082` its coverage; pushed to the fork). Layer 2 is built as a fully-covered
module (below) and is now **wired — L3 consumes the slicer** (`regionanalyzer.cpp:579`).

| Module | Responsibility |
|--------|----------------|
| `composing/analysis/notemodel/note_model.{h,cpp}` | **The lossless, tie-resolved NOTE MODEL — the single source of truth for "what sounds."** `NoteModel::build(score)` reads the score **once** into an annotated, tick-range-queryable set of sounding notes. Each `NoteEvent` carries 11 fields: `pitch, tpc, staff, voice, onset, release, duration, isGrace, plays, visible, staffEligible`. Tied groups are merged into **one** span/onset (via the DOM `firstTiedNote`/`lastTiedNote`/`playTicksFraction`); spans are true `[onset,release)` answered by **overlap with no horizon** (the old 4-whole-note backward cap is gone). Grace / non-playing / invisible / staff-ineligible notes are **kept and flagged, never dropped**. **Additive fact-surface extension (joint-estimator dual path, OI-180):** `notatedNotes()` republishes the tie-UNRESOLVED atoms — EVERY notated note incl. tie continuations, each with its OWN notated span, a `tieContinuation` flag, a `hasFermata` flag, and `resolvedIndex` linking to its tie-resolved `NoteEvent` — the facts the tie-resolved surface discards that the joint module's event lattice + emission covariates need. Purely additive: `notes()` and every existing consumer are byte-identical. |

**Derived views over the model (in `engravingbridge`).** The old note-reading is replaced by
the model; the old *weighting* survives as a derived view:
- `weightedPcView(noteModel, range, …)` — the recomputed `collectRegionTones` weighting
  (duration×beat, repetition, cross-voice, pedal, PC aggregation, bass pick), now counting
  **one onset per tied group** (tie **de-inflation**) and finding sustains by overlap.
  `collectRegionTones`/`collectSoundingAt` are retained as thin **build-once Score wrappers**.
- `soundingAt(noteModel, tick, …)` — the point-in-time per-note view (replaces `collectSoundingAt`'s
  reading half); `buildTones` is now a trivial adapter; `findTemporalContext` takes the model.

**Transitional, by design.** The segment-first analysis spine described below
(`greedyExpandSegmentation`, the Pass-1/2/2b sub/merge machinery, `analyzeHarmonicRhythm`)
**still runs and still drives all analysis** — it now consumes `weightedPcView` (unchanged
weighting) instead of reading notes directly. It retires only when **layer 2** (change-point
slicing) and **layer 3** (per-slice analysis) are built. The note-reading *ownership* has moved
to the note model; the slicing/scoring *logic* is frozen until its layers.

**Ratified trade-off on record.** Layer 1 is a **behavior change**, not byte-identical: the
faithful tie de-inflation moved the per-event oracle-root metric **+3/+1/+1 charged**
(Baroque/Jazz/Default), with the KEY tier flat, FLOOR byte-flat, and BIR **−2/+1/−2** (mostly
improved). This is a correct-**upstream** / frozen-**downstream** wobble (the old
repetition-inflation happened to nudge a few borderline chords toward the oracle); it re-tunes at
layer 3 and is **not** an unexplained regression (proven: a legacy reproduction mode reproduced
the prior oracle set byte-exactly). **Next: layer 3 (per-slice analysis).** See
`cc_layer1_impl_report.md` / `cc_layer1_coverage_report.md` (HELD).

#### Layer 2 — the deterministic change-point slicer (Built+Live — consumed by L3)

The **constant-(tonal-)sonority slicer** — layer 2 of the rebuild. A pure, deterministic FACT
read off the layer-1 note model, **not** a judgment. It **is** now wired into the live analysis
pipeline: layer 3 consumes the slicer (`regionanalyzer.cpp:579` → `KeyModeSequenceDecoder`). The
slicer's own output stays **byte-identical** on the whole-score live path (the clip is inert there);
the analysis movement came from **L3's consumption** of the slices, not from the slicer.

| Module | Responsibility |
|--------|----------------|
| `composing/analysis/slicing/slicer.{h,cpp}` | **Enumerate the change-point slices of a score from the note model.** `changePointSlices(noteModel)` returns an ordered, **covering, lossless** list of half-open `[start,end)` spans that **tile the domain with no gaps and no overlaps**. Boundaries = the sorted-unique union of every **onset AND every release** of the **eligible** notes; consecutive boundaries form the slices. O(n log n). |

**Boundaries over layer-1's eligibility annotation — never re-decided.** A note participates in
boundary generation iff layer 1 flagged it `plays && visible && staffEligible`. The slicer
**reads** those flags; it does not re-filter. A muted / invisible / non-tonal-staff note opens
**no** boundary, yet still rides along in each slice's `overlapping()` set (passed through, not
dropped). A slice is therefore "constant **tonal** sonority"; non-eligible notes are passenger
metadata. **Slice identity is the eligible sounding-NOTE set** (not the octave-folded PC set — a
unison/octave shrink is a real boundary though the PC set is unchanged).

**Covering / empty slices, clipped to the loaded span (bounded context).** The tiled domain is the
intersection of the eligible-notes span with the model's **loaded span**:
`[max(loadedStart, firstEligibleOnset), min(loadedEnd, lastEligibleRelease))`. Every tick in that
domain lands in exactly one slice. A **sustained-in** note (onset `< loadedStart`) is clipped to
start at `loadedStart`, a **sustained-out** note (release `> loadedEnd`) to end at `loadedEnd` —
slicing never drags outside the loaded span (Phase 2; `cowork_layer2_reslice_design.md` §2). On a
**whole-score** model `loadedStart ≤ firstEligibleOnset` and `loadedEnd ≥ lastEligibleRelease`, so
the clip is **inert** and the domain is exactly `[firstEligibleOnset, lastEligibleRelease)` —
byte-identical to before the clip. An interior span where all eligible voices rest is an **explicit
EMPTY slice** (empty eligible overlap set), not a gap — it falls out of the consecutive-boundary
construction for free. Leading/trailing silence within the loaded span is not sliced; silence
outside the domain is not invented. **Re-slice on extend** = re-call `changePointSlices` on the
enlarged model (the slicer is a pure function of (notes, loaded span)): interior real change-points
are stable, the edge slice abutting an *artificial* clip boundary extends into the new context, and
the result equals a fresh slice over the enlarged span (re-slice equivalence). Incremental
re-slice is Phase 2b (deferred, byte-identical).

**Zero interpretation.** No thresholds, min-gap, merge, or snapping; no notion of
"ornamental/passing/structural". **No special-casing of any note kind** — grace and tuplet
outcomes fall out of the note-model spans as facts (verified at source: a grace event carries
onset = parent-chord tick and duration = `playTicksFraction()` = its nominal written value, so a
grace genuinely opens/closes a boundary by its span; tuplet ticks are the model's real, un-snapped
ticks). The slicer needs no grace/tuplet code. Boundaries are **necessary but not sufficient** for
a chord change (the exhaustive candidate grid): a real chord change can never be missed
(over-grab is structurally impossible), and the slicer never asserts a change — layer 3 decides
which boundaries are real, layer N groups equal analyses.

**Fully covered + byte-identical on the live path.** Built with `slicer_tests.cpp` (20 tests: the
audit §3 functional set + edge/eligibility cases + the Phase-2 bounded-context set CP1–CP7 —
degenerate clip-inertness, sustained-in/out clip correctness, seam-aware stability on extend,
re-slice equivalence). `changePointSlices` is consumed by L3 on a **whole-score** model
(`regionanalyzer.cpp` → `KeyModeSequenceDecoder`; `batch_analyze` key/chord decode), where the
Phase-2 clip is inert — so composing / notation / pipeline-snapshot / BIR / oracle are
byte-identical (composing 631/631, notation 53/53, snapshots 11/11 with no golden refresh; corpus
0/353 `.ours.json` byte-diffs on Baroque/Jazz/Default, gate unchanged at 53/24/53). See `cc_layer2_impl_report.md` (HELD), `cowork_layer2_slicing_design.md`,
`cc_layer2_audit_dossier.md`.

#### Layer 3 — key/mode is the sequence decoder (Built+Dormant)

**Build-state correction, 2026-08-02 (`OPEN_ITEMS.md` OI-232 item 3; the tag read "Built+Live", which the
two adoptions made false).** Layer 3's decoder no longer decides the key on either surface: the
batch/corpus surface runs the joint estimator since the OI-178 adoption (2026-07-26) and the in-app
notation surface since the notation switch (2026-07-27). Verified at the code: every production call site
of this pipeline — `notationcomposingbridge.cpp:324-328` (the bounded-window section build behind the
note-seam funnel's flag check at `:729-738`), `notationcomposingbridge.cpp:1509-1513` (the span emitter's
legacy arm), `notationimplodebridge.cpp:1434-1441` (implode's legacy arm) and
`notationtuningbridge.cpp:794` (the tuning region path's legacy arm) — sits in the `false` branch of
`useJointNotationRecord`, whose default is `true` (`composingconfiguration.cpp:178`). The remaining
callers are the `batch_analyze` diagnostics, which are development tools and are not shipped (§15). **The description below remains accurate for the dormant pipeline** and is retained as
the record of what that pipeline does; it is no longer a description of what runs.

**Delegation pointer (the fifth home case, user-ratified 2026-08-02).** The ratified contract for this layer is `cowork_layer3_keymode_design.md` (SIGNED, user, 2026-06-22) — D-343…D-358 — which this section points at and does not restate.

**Tried and closed on this layer — do not retry; the register carries each with its evidence: D-287 (key-as-distribution, shelved), D-290 (the key-agnostic local cadence approach, falsified).**

**The backward re-reading facility stays SWITCHED OFF in the shipped configuration.** This layer carries a
facility for returning to an earlier stretch and re-reading it once later evidence has arrived
(`ReachBackOptions`). It is built, and `enabled = false` is the shipped default; turning it on is reopened
only on a named evidence follow-up, not on judgment. *Why:* measured and judged insufficient — an A/B run
showed the designed effect is material (roughly 35–45 % of interior range queries change, almost all of
them anchoring the leading key), but the timing comparison was confounded, one arm cold and the other
warm, so the evidence needed to justify switching it on — interleaved timing plus an adjudicated sample of
the changed outputs — was named and has not been gathered. Decided by the user 2026-07-02.

**The production region key/mode path is the decoder, not the per-region resolver.** Step-1 wiring
replaced the per-region `resolveKeyAndModeRanked` call with a single whole-score decode of
`KeyModeSequenceDecoder` (`composing/analysis/key/keymodesequence.{h,cpp}`, the Layer-3
key/mode design — `cowork_layer3_keymode_design.md`). This is the first rebuilt analysis **decision** layer to go **live** in the
pipeline — and this wiring is what connected Layer 2: it consumes Layer 1's note model and Layer 2's
slicer (`changePointSlices(noteModel)`), so neither is isolated any longer.

**As-wired data flow (the seam in `regionanalyzer::analyzeRegions`).** Reusing the whole-score
`noteModel`, the path computes the signature context **once**
(`keySigCtx = resolveKeySignatureContext(...)`), runs `decode(changePointSlices(noteModel), …,
keySigCtx.correctedFifths, keySigCtx.declaredMode, …, excludeStaves)` **once** before Pass-1, and
then serves each region via `localKeyForRegion(rs, re)`:
- **Intra-region rule (b) — duration-majority** over the region's overlapping slice run (ties →
  lower representative slice index, deterministic), returning the representative slice's `chosen`
  key/mode (carrying its C1 `normalizedConfidence`).
- **Seed S2** — a region overlapping no decoded slice falls back to the segmentation seed (@521,
  unchanged). The coarse grid (`greedyExpandSegmentation` boundaries) is therefore **byte-stable**;
  the only new sub-region ticks are Pass-2/2b sub-boundaries that ride on the (legitimately changed)
  chord analysis, not a coarse-grid change.

**Three fidelity fixes, no duplication.** (1) `excludeStaves` is threaded
`decode()/redecodeRange() → buildLattice → buildSliceContext → pitchContextOverSpan` (was hardcoded
`{}`); the default keeps every existing caller byte-identical. (2) The signature read + declared-mode
mapping + declared-gated Baroque `partialSignatureCorrection` was lifted verbatim into a shared
public `resolveKeySignatureContext`, **called by both** the resolver and the wiring — so no
signature/partial-correction logic is duplicated. (3) C1 emission confidence
(`populateEmissionConfidence`) stamps each `SliceKeyMode.chosen.normalizedConfidence` with the
`analyzeKeyMode` winner sigmoid re-expressed over the lattice's per-slice emission scores (≈0 when
sequence smoothing overrode the local argmax — the safe direction).

**Retired from the production region path:** the per-region `resolveKeyAndModeRanked` call at the
seam, its hysteresis, and the `prevKeyResult` threading (declaration + per-region update);
`collectPitchContext` as the region builder. The end-state on the production region path is **one
key path (the decoder) + one builder (`pitchContextOverSpan`)**.

**Surfaced residuals (pre-existing, not introduced; named follow-ups):**
- **P4 tick-local still uses `resolveKeyAndModeRanked` + `collectPitchContext`** (the ratified
  P4-defer). Verified **byte-identical** this increment (the `tickLocal` snapshot section is
  unchanged in all 11 goldens) — no leak. The named follow-up is **P4-redecode**.
- The resolver and `collectPitchContext` remain compiled **only** as the segmentation seed (@521,
  S2) and the diagnostic/grading baseline (e.g. `batch_analyze --decode-keymode`); they no longer
  drive the production region key/mode.

**Gate trade-off on record.** BIR (case-identity): Baroque **53** (net −4), Jazz **24** (net +1),
Default **53** (net −4); zero new class-(b) (functional) regressions — every new case is a
class-(a) symmetric-dim7 / share-tone **rotation** ambiguity (root pitch-class-undecidable by
construction). The Jazz +1 is accepted under the two-tier BIR-gate amendment (CLAUDE.md, "Gate
threshold and preset policy"); it retires when Layer 4 (function/cadence) pins the rotation.
`composing_tests` 596/596; the P1/P2/P3/keyAreas snapshot goldens were refreshed for the ratified
key moves with **P4 untouched**. Full provenance: `cc_layer3_wiring_report.md` (HELD),
`cowork_layer3_keymode_design.md`.

#### Layer 4 — the per-slice chord-symbol decoder (Built+Dormant — not wired)

**Plan correction, 2026-08-02 (`OPEN_ITEMS.md` OI-232 item 3; the heading read "engages with L5", which
no longer describes anything scheduled).** The "joint with Layer 5" production switch described below was
the plan ratified 2026-06-26. It was overtaken by the joint estimator, which became the production
inference layer on the batch/corpus surface (2026-07-26) and on the notation surface (2026-07-27) without
any ruling that names the engage-with-L5 plan — a supersession in fact, not by decision (register entry
D-051 records the same shape on Layer 3). The build state itself is unchanged and correct: Built+Dormant.
**What becomes of this decoder is OPEN** — it is neither retired by a ruling nor scheduled; see the
OI-180 retirement map.

**Delegation pointer (the fifth home case, user-ratified 2026-08-02).** The ratified contract for this layer is `cowork_layer4_chordsymbol_design.md` (SIGNED, user, 2026-06-24) — D-329…D-334 — which this section points at and does not restate.

**Tried and closed on the chord layer — do not retry; the register carries each with its measurement: D-215, D-299, D-300, D-301, D-302, D-317, D-318, D-319, D-320, D-328.**

**Deciding which sounding notes do not belong to the chord is DEFERRED — and when it is built, the
knowledge enters the chord decision itself, never a removal afterwards.** Non-chord-tone detection waits
for the annotated material it needs. Its shape is constrained in advance: chord identification that knows
about non-chord tones, not a pass that names a chord and then strips notes out of the answer. *Why:*
**derivation not recorded** — the record states the constraint without giving the reason for it. It is
load-bearing now: the non-chord-tone filter is the named lever at `OPEN_ITEMS.md` OI-55 and OI-68, and
`docs/nct_detection_design.md` exists. The record states neither a date nor a ratifier.

**Scope of the description below, 2026-08-02 (`OPEN_ITEMS.md` OI-265).** As on Layer 3, **the
description below remains accurate for the dormant decoder** and is retained as the record of what
that decoder does; it is not a description of what runs. It carries one sentence about what runs —
that production chord analysis still runs the legacy `analyzeChord` + post-scoring gates (§4.1) —
which was true when written and is **false at HEAD**: the joint estimator produces the committed
chord reading on the batch/corpus surface since the OI-178 adoption (2026-07-26) and on the in-app
notation surface since the notation switch (2026-07-27), where `useJointNotationRecord` defaults to
`true` (`composingconfiguration.cpp:178`). The legacy `analyzeChord` path is compiled and dormant
beside this decoder, and retires with it at the OI-180 map. Read that sentence as the legacy
pipeline's own frame at the time the decoder was built, not as a statement about today.

**Built, unit-tested, and graded — but NOT wired into the live pipeline.** Layer 4 of the rebuild is
`ChordSliceDecoder` (`composing/analysis/chord/chordslicedecoder.{h,cpp}`): a per-slice chord-symbol
decoder over the Layer-2 slices, mirroring the Layer-3 key/mode decoder's shape. Production chord
analysis still runs the **legacy** `analyzeChord` + post-scoring gates (§4.1); the decoder runs only
under the read-only `batch_analyze --decode-chords` diagnostic (which returns before `analyzeScore`),
so production output is **byte-identical**. The production switch, legacy retirement, and coverage
seal are **joint with Layer 5** (engage-with-L5, ratified 2026-06-26).

| Module | Responsibility |
|--------|----------------|
| `composing/analysis/chord/chordslicedecoder.{h,cpp}` | **Decode a chord symbol per Layer-2 slice.** `decideSlice` (scorer-independent) selects from a candidate cube, computes the confidence margin to the best DIFFERENT chord, ranks/caps the alternatives, carries the prevailing (∪) union, and marks "uncertain". `decode` runs the full pipeline over a Layer-1 note model + `changePointSlices`; `redecodeRange` re-decodes a sub-range under the same incremental contract. |

**The decision ladder (G1–G6 + spelling-pin), built incrementally, all dormant:**
- **G1 — commit / inherit / abstain + sufficiency gate** (`f21273ce3b`): per slice, commit a chord,
  inherit the prevailing chain, or abstain when the slice is insufficient.
- **G2/G3 — three-tier membership ladder + plausibility check** (`1b7fee1cd5`; the ladder is kept by
  the Step-2 correction `d52cfd0847`).
- **Two-reading both-sides inherit — continuation vs transition** (`4aa88452cd`): a slice's look-ahead
  consumes `nextChord` (a Layer-4 result) but explicitly disclaims any transition *cost* ("that is
  Layer 5") — the forward-only contract holds, no back-edge.
- **G6 — confidence model + open-question label (the L4→L5 abstain contract)** (`c74fe98ff5`):
  `OpenQuestionLabel` *declares* the open question + the competing readings; Layer 4 does **not**
  resolve it (representational only — the `SliceDecision` is unchanged by G6).
- **G4/C1 — symmetric-root spelling-pin** (`1e74f21ea4`): for a pitch-class-undecidable symmetric root
  (dim7 / augmented / share-tone), pins the spelling-correct rotation from each focal note's notated
  `tpc`, read through the **shared** `engravingbridge::lineOfFifths` primitive (the Layer-1.5 spelling
  view) — one interpreter, not a per-layer tpc copy.

**Proven where it commits; abstains where function decides.** Per the L4-build grading reported in the
engage-with-L5 ratification (`cowork_l1l4_review_charter.md`): the decoder is materially better than
legacy where it commits (+5.5 / +5.8 in the graded measure), and ≈**85%** of its abstention is
genuinely function-dependent → resolvable only by Layer 5 (function/cadence). That is the evidence for
opening L5 on a clean L1–L4 foundation.

**Unification residual (scheduled for engage-with-L5).** The spelling-pin reads the shared spelling
primitive, but the live legacy scorer (`chordanalyzer.cpp`) still interprets `tpc` through its own
inline cluster (`tpcForPc` / `tpcConsistencyBonus` / `tpcSpellsAsSharp` / `countTpcMatches`), so a
**second tpc reader coexists** until the legacy path retires (the tpc-fold the tpc-capability spec §3
owes — deferred, not done). Likewise `redecodeRange`, `tonicizationlabeler`, and
`DecodeQualityLevel::Normal/Deep` are built-but-inert staging, each comment-accurate about its
dormancy. Built with `decode_chord_tests.cpp` (scorer-independent + note-model tiers). Full provenance:
`cowork_layer4_chordsymbol_design.md`, `cowork_phase5b_l4_build_plan.md`, the Phase-5b commits
`f21273ce3b`..`1e74f21ea4`.

#### Layer 5 — the function/cadence layer (Built+Dormant — design ratified; consumed by L6)

The function layer reads the L4 chord **in** the L3 key and produces the **Roman numeral** (the precise superset of a
T/S/D summary) plus **cadence** and **local-key** markers — additive over L4 (it annotates and resolves; it never
rewrites the committed chord identity). Built dormant + byte-identical (Phase 5c, Steps 0–6 + the A-D2 follow-up,
2026-06-29); the joint L4+L5 production switch is deferred. L5 is where the **confidence-weighted forward-override**
(§2.14) fires its two instances — the cadence-confirmed modulation recompute and the fine-grain chord override — and
where the carried L4 abstentions are resolved by **selecting** among the carried readings (never re-derived). The cadence
detector is **key-agnostic** (it votes for the key; it does not read a resolved key). Full spec:
`cowork_layer5_function_design.md`.

**Delegation pointer (the fifth home case, user-ratified 2026-08-02).** The ratified contract for how this layer ENGAGES with the chord layer's carry — the carry's distinct-root axis, selection by joint consistency, pedal detection's home, and the open-mark — is `cowork_layer5_engagement_design.md` (Part 1 §1–§5, Part 2 §6–§10) — D-380…D-387 — which this section points at and does not restate. Its authority is TRANSITIVE: the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arcs #9 and #11 to it by name (`:41`, `:46`) and states that the Stage-3 build inventory "is enumerated at `cowork_layer5_engagement_design.md` §9.2" (`:53-55`).

#### Layer 6 — the grouping layer (Design-only — v1 spec)

The grouping layer assembles the L5-labelled stream into the **flat** structure the ground truth annotates: **phrases**
(from the L1.5 phrase-boundary primitive), **key-areas** (grouping the local-key track, which **cross-cuts** phrases —
§2.15 span typology), and the **alignment of cadences to phrase ends** — additive, read-only, no feedback into L5. It is
the forward-only rebuild of the scattered live `detectCadences`/`detectPivotChords`/`KeyArea` machinery. Hierarchy,
periods/sentences, and prolongation are out of the validatable core (verifiability contract, §2.15). Full spec:
`cowork_layer6_grouping_design.md`.

#### Planned analysis consumers beyond the layer stack

- **The progression-schema recognizer** — an L5 *consumer* (a prior + an annotation), not a new layer: it recognises
  multi-chord patterns and substitutions from the **Harmonic Vocabulary** (§7) over the committed progression,
  disambiguates via the §2.14 forward-override, and annotates the recognised schema as an **L6 sequence-span**.
  Scaffolding-first, deferred. Spec: `cowork_progression_schema_design.md`.
- **The voice-leading layer** — the *horizontal* dimension (linear progressions, suspension chains, the
  voice-leading skeletons that complete the galant schemata); named so the dependency is explicit (the
  functional-harmonic schemas are L5-reachable without it; the voice-leading-complete ones require it). It reads the
  per-voice motion the L1 note model already carries losslessly. **Corrected 2026-08-02 (`OPEN_ITEMS.md` OI-232
  item 4; this entry said "not built", contradicting §2.15 in the same document):** the axis-2 FOUNDATION is
  **BUILT and dormant** as of 2026-07-03 — VL-A the voice-linear view, VL-B motion and interval profiles (facts),
  VL-C texture classification — with VL-D…VL-H named and design-gated. The full status and the design are in §2.15
  and `cowork_voiceleading_axis_design.md`.

#### Region Analysis — Canonical Modules (Iter 97, complete; note-reading half superseded by Layer 1; region key/mode path superseded by Layer 3)

The harmonic-rhythm region pipeline used to exist as two near-duplicate copies (one in
the notation bridge, one in `batch_analyze.cpp`). Iter 97's duplication-remediation work
collapsed both into a single canonical implementation inside the `composing` module. Four
new modules carry it, all with **zero engraving dependency** (they consume a tone/region
abstraction the callers populate):

| Module | Responsibility |
|--------|----------------|
| `composing/analysis/engravingbridge/regiontonecollector.{h,cpp}` (+ `regiontoneprimitives.cpp`) | The derived tone **views over the Layer-1 note model** — `weightedPcView` (recomputed `collectRegionTones` weighting, tie-de-inflated), `soundingAt`, `buildTones`, plus the retained build-once `collectRegionTones`/`collectSoundingAt` Score wrappers, `findTemporalContext`, and the still-live `detectOnsetSubBoundaries`/`detectBassMovementSubBoundaries`/`collectPitchContext` (slated for Layer 2/3). Note **reading** moved to `notemodel/` (above); this layer now derives over it. |
| `composing/analysis/key/keyresolver.{h,cpp}` | `resolveKeyAndModeRanked` — supersedes the old `inferLocalKey` + `resolveKeyAndMode` pair. **No longer the production region key/mode path** (replaced by the Layer-3 decoder, above); it now serves only the segmentation seed (S2), P4 tick-local (P4-defer), and the diagnostic/grading baseline. The shared `resolveKeySignatureContext` (signature read + declared-mode + Baroque `partialSignatureCorrection`) is called by both it and the wiring. |
| `composing/analysis/region/regionanalyzer.{h,cpp}` | `region::analyzeRegions()` — the whole orchestration: greedy-expand segmentation (Pass 1) → per-region `analyzeChord` → `absorbShortRegions` → Pass 2 / Pass 2b sub-region splitting → merge. The single source of truth for region output. |
| `composing/analysis/region/sparsechordrefinement.{h,cpp}` | Sparse-region post-refinement (tonic/diatonic priors on thin ≤2-PC slices) factored out of the orchestrator. |
| `composing/analysis/section/sectionanalyzer.{h,cpp}` | Section-level unified analysis — `analyzeSection`, key/mode stabilization, cadence and pivot detection (`detectCadences`, `detectPivotChords`). Moved here in Stage 2.1 (Phase 4c). |
| `composing/analysis/types/analysistypes.h` | **The cross-layer value-types LEAF** — a dependency-free header (STL only; no `chord/`, `key/`, or engraving includes) holding the value types that cross the L1.5 / L3 / L4 boundaries: `ChordQuality`, `ChordAnalysisTone`, `ChordAnalyzerPreferences` (+ `kDefault`), `ChordTemporalContext`, `DecodeQualityLevel`, `function::ScoringPhase`, `ParameterBound`/`ParameterBoundsMap`, `KeySigMode`, `KeyModeAnalyzerPreferences` (+ `kDefault`), and the un-nested `PitchContext`. Each is a **pure relocation** from its former home (same name/namespace/layout). `chord/chordanalyzer.h` and `key/keymodeanalyzer.h` now `#include` this leaf, so every existing includer gets the types transitively, unchanged. |

**Cross-layer types leaf removed two header back-edges (layering audit Q2).** Introducing
`analysis/types/analysistypes.h` lets the L1.5 (`engravingbridge`) and L3 (`key`) headers compile
**without** including the L4 (`chord`) headers, killing the two type-only header back-edges the
audit found: `regiontonecollector.h → {chordanalyzer.h, keymodeanalyzer.h}` (now includes only the
leaf) and `keymodeanalyzer.h → chord/analysisutils.h` (now includes only the leaf). `PitchContext`
was **un-nested** out of `class KeyModeAnalyzer` into the leaf; that class keeps a member alias
`using PitchContext = analysis::PitchContext;` so all call sites are unchanged.

**Section-level analysis and the Pass-0 injection contract (Stage 2.1).** Section-level
unified analysis — `analyzeSection`, key/mode stabilization, cadence and pivot detection —
lives in `composing/analysis/section/`. Pass-0 boundary detection (`analyzeHarmonicRhythm`)
remains the notation-side configuration adapter and **injects** its `HarmonicRegion` stream
into `analyzeSection` as a parameter, keeping `composing_analysis` independent of the
notation and configuration layers.

**Bridge and batch are thin wrappers.** `analyzeHarmonicRhythm()` (notation bridge) and
`analyzeScore()` (`batch_analyze.cpp`) now contain only the engraving→tone adaptation and a
single call to `region::analyzeRegions()`. The −968 / −399 line deletions in those two files
(Phase 4) removed the duplicated orchestration. All orchestration logic — and therefore the
behavior that BIR and the pipeline snapshots measure — lives in `regionanalyzer`.

**Two configuration divergences between the two call paths were audited (`AnalyzeRegionsOptions`):**

- **D1 — `excludeLookAheadOnDenseStart`** is **intentionally divergent and load-bearing.**
  The 4 batch call sites pass `true`; the bridge defaults to `false`. This is not an oversight:
  unifying it regresses the bridge/Corelli trio-sonata dominants. It stays divergent by design;
  the flag's contract is documented in `regionanalyzer.h`.
- **D2 — `pass1MinDistinctPcsForCandidate`** is **unified at `1`** on both paths
  (commit `4d881e7418`). This was the last remaining batch/bridge parameter divergence; the
  batch path now admits sparse 1–2 PC Pass-1 slices exactly as the bridge always did.

With D1 confirmed intentional and D2 unified, the bridge and batch are fully unified thin
wrappers — there are no remaining unexplained asymmetries between the two paths.

### Path divergence decisions (Stage 2.4)

Four analysis-path divergences accumulated across the part-2 implementation review, the corpus
audit (Findings 3/4), and the 2.2-i section-level dossier (§2/§7). They are decided here so they
are not rediscovered. The unifying theme: the **batch BIR-measurement path** and the **live
notation path** are not the same configuration, and the **greedy feed-forward pipeline** builds
temporal context per-commit rather than from a global decode. Stage 3 (the lattice decoder) is
where accumulated context becomes a decode product; decisions that would be torn up by Stage 3
are deferred to it rather than pre-built now.

#### D-P4 — tick-local path builds temporal context cold

**Facts.** The P4 tick-local fallback (`analyzeHarmonicContextLocallyAtTick`) builds its
`ChordTemporalContext` via `findTemporalContext`, which cold-analyzes the backward and forward
neighbours with `nullptr` context and no accumulated rolling state [code]. It fires only when
the P3 regional path returns no region for the surrounding window — structurally rare; exact
live frequency unmeasured [code]. The same chord can therefore in principle answer differently
on P4 vs P3.

**Decision.** Cold context on P4 is the **current contract**, documented and accepted (the same
precedent as the Stage 2.3 diagnose context banner: a path may legitimately analyze with less
context, provided that is stated, not silent). No pre-pass is built now: Stage 3's lattice makes
accumulated context a decode product, and any context pre-pass built against the greedy pipeline
would be discarded at Stage 3.

**Revisit trigger.** Stage 3 design **must** state explicitly what P4 (and the bridge) consume
from the decode. If P4's empty-window fallback rate is ever shown to be non-trivial (requires
instrumenting the per-tick API), revisit earlier.

#### D-BRIDGE — bridge predecessor analyzed with null context; Step-1/2 fields inert

**Facts.** `findTemporalContext` analyzes the backward predecessor (and forward successor) with
`nullptr` context [code]. The Step-1/2 confidence fields
(`previousWinnerScore/Margin/RootPcWeight`, `previousDistinctPcs`) are default-initialized
(`-1.0`/`0.0`/`0`) and never written on the bridge path — only `advanceTemporalContext` (region
commit sites) writes them [code]. So predecessor-confidence progression signals are inert on the
bridge path; the bridge populates only the root/quality/bass neighbour fields the downstream
gates need.

**Decision.** Same as D-P4: this is the **current contract**, documented. The forward-lookahead
gap that previously left `nextRootPc=-1` was already closed (`90a52b5fee`); the residual
(Step-1/2 confidence fields) genuinely requires a committed competition result from the
neighbour, i.e. a forward pre-pass over the score — exactly the global-decode product Stage 3
provides. Do not build a bespoke pre-pass now.

**Revisit trigger.** Stage 3 design must state what the bridge consumes. The decoder's path
state supersedes `findTemporalContext`'s cold walk.

#### D-PASS0 — notation Pass-0 uses default prefs + `excludeLookAheadOnDenseStart=false`; batch uses preset prefs + `true`

This divergence has **two independent halves**; Stage 2.4 investigation (§1.1) decides them
separately.

**Half A — chord-scoring preferences (the headline). Facts.** The Jazz/Baroque
`ChordAnalyzerPreferences` are constructed only in `tools/batch_analyze.cpp` and never reach the
product; every live chord-scoring site uses `kDefaultChordAnalyzerPreferences` [code]. The
app's "Jazz/Baroque/…" Preferences buttons set only the 21 mode priors (key detection), not
chord-scoring prefs [code]. The BIR Jazz/Baroque gate therefore measures a chord-scoring
configuration **no user can produce in the app**. Sharper still: the struct default
(`preferMinorOverMajorAdd6=false`) matches NO batch preset — even "Standard" sets it true — so
the configuration the live product actually runs has, as of Stage 2.4, never been corpus-measured.
The `--preset Default` measurement (below) closes that. **Measured (Stage 2.4 V4,
`tools/corpus/default`, informational — no gate):** the user-default config yields **30/14**
three-way genuine errors (`bassIsRoot` true/false) — its BIR=false set is the canonical
Baroque-13 set **in full plus `bwv187.7`** (every gate case is experienced by users; one extra),
and it shares 5 of the canonical Jazz-7 (`bwv245.17/245.40/422/432/45.7`), while Jazz's
`bwv244.15/74.8` are preset-specific. So the live-product configuration is closest to Baroque
(a 13-of-13 superset, +1), not to batch "Standard".

> **Re-baselined 2026-06-13 (corrected GT parser).** The figures in this paragraph are the
> pre-re-baseline Stage-2.4 values. The corrected `tools/dcml_parser.py` (applied-`/X` +
> minor-key leading-tone rooting) moves the gate to **Baroque 57 / Jazz 23 / Default 57**
> *(Superseded 2026-06-26: the live gate is now **53 / 24 / 53** — the L3-wiring delta moved
> 57/23/57 → 53/24/53; CLAUDE.md is authoritative for the current integers and `stem@tick`
> identity sets, which this paragraph's pre-delta figures and Default-swap detail do not reflect)* — a
> **strict superset** of the old 13/7/14 (0 lost, 100% oracle-correct roots; ~95% of the
> additions are legitimate ambiguity). The `30/14` `analyze_inversion_errors` three-way figure
> is **stale pending re-measurement**. The qualitative finding is unchanged: the live config is
> closest to Baroque (Default-57 = Baroque-57 with `{bwv227.7@18120, bwv60.5@30960}` ↔
> `{bwv187.7@19200, bwv227.7@18000}`), the preset chord-scoring system is measurement-only. See
> the CLAUDE.md gate section for the authoritative identity sets.

**Decision (Half A).** Record this as a **product-level finding**, not a code change. The
chord-scoring preset system is currently a **measurement-only artifact** of `batch_analyze`. Do
**not** silently flip the live product onto preset chordPrefs — whether the product should expose
a chord-scoring style is a deliberate **product decision**, deferred. Until then, all docs that
imply Jazz/Baroque chord tuning ships to users must be corrected to "batch-measurement only."
The live product analyzes chords with struct defaults (not even batch "Standard").

**Decision (Half B — `excludeLookAheadOnDenseStart`).** Unchanged and intentional. Batch passes
`true`, the bridge defaults `false`; this is the **D1 / Iter-97 load-bearing divergence**
(unifying it regresses the Corelli trio-sonata dominants on the bridge). Keep diverged;
keep documented.

**Revisit trigger (Half A).** Any product initiative to expose a chord-scoring "style" to users;
any Stage-5 metric work that wants the gate to measure the *user* configuration (note: that would
mean re-tuning against `kDefaultChordAnalyzerPreferences`, not the batch preset). Until one of
those, the gate stays as-is and is **described accurately** (batch-measurement configuration).

#### D-GAP — `inferGapRegion` analyzed gap slices with default prefs regardless of caller

**Facts.** `analyzeSection`'s gap inference hardcoded `kDefaultChordAnalyzerPreferences`
(`sectionanalyzer.cpp:607/614/617`) [code]. Under a preset, the section diagnostic mixed
**preset Pass-0 + default gap analysis** — internally inconsistent. The 2.2-i dossier (§7.2)
hypothesized this leak as the likely cause of all 3 genuine Baroque A/B regressions.

**Decision.** **Fixed now** (Stage 2.4 surgical fix — §3): the caller's `ChordAnalyzerPreferences`
are threaded through `analyzeSection → inferGapRegion`. Proven user-neutral + gate-neutral
(snapshots 11/11 zero diffs; flag-off BIR path byte-identical) — the live path passes default and
is unaffected; only the batch `--section-level` diagnostic now measures a consistent preset
pipeline. **Causal note:** the fix does **not** heal the 3 Baroque regressions — under
Baroque the chordPrefs delta from default is only `preferMinorOverMajorAdd6`, so the leak was
nearly inert there; the 3 regressions are structural (measure-split / gap-insertion), not
gap-pref-caused. So the dossier's §7.2 hypothesis is **not supported** for the Baroque cases.
The fix is justified on consistency + user/gate-neutrality, which was the stated bar (healing was
"expected, not required").

**Revisit trigger.** None for the fix itself. The 3 structural regressions and the section-vs-batch
granularity question fold into the Stage-5 granularity-robust metric (already mandated).

#### The `IComposingConfiguration` Split

Configuration is exposed through **two narrow interfaces**, both IoC-registered:

| Interface | IoC-registered? | Used by |
|-----------|----------------|---------|
| `IComposingAnalysisConfiguration` | ✓ | Analysis bridge, tuning bridge, status bar, context menu, app menu, preferences model |
| `IComposingChordStaffConfiguration` | ✓ | Implode bridge, preferences model |
| `IComposingConfiguration` | ✗ | Only `ComposingConfiguration` concrete class inherits this (as a plain base, not IoC-registered) |

**Why split?** The implode bridge has no business knowing about status-bar display preferences; the analysis bridge has no business knowing about chord-staff output settings. Narrow interfaces make the dependency of each component explicit and keep the IoC registrations clean.

`IComposingConfiguration` is not registered because it inherits from both sub-interfaces, and the IoC `modularity_interfaceInfo` static member would be ambiguous with two `MODULE_GLOBAL_INTERFACE` bases. Only the two leaf interfaces are registered; `ComposingConfiguration` (the one concrete class) inherits from `IComposingConfiguration` and thereby implements both.

#### `KeySigMode` Disambiguation

`mu::engraving` defines `KeyMode` (key signature mode: MAJOR, MINOR, DORIAN, …).
`mu::composing::analysis` defines `KeySigMode` (21-mode analysis enum: Ionian, Dorian, …).

The two enums have different names, so no explicit disambiguation is needed. However,
bridge files that use `using mu::composing::analysis::KeySigMode;` alongside
`using namespace mu::engraving` should add a comment for clarity:

```cpp
using mu::composing::analysis::KeySigMode;  // disambiguate from mu::engraving::KeyMode
```

This pattern appears in `notationcomposingbridgehelpers.cpp`, `notationimplodebridge.cpp`,
and `notationtuningbridge.cpp`.

#### Adding New Bridge Functions — Checklist

1. Implement the logic in the appropriate `notation*bridge.cpp`
2. Declare in the corresponding `notation*bridge.h` in `mu::notation` namespace
3. Do **not** add declarations to any `composing/` header
4. Do **not** forward-declare engraving types in any `composing/` header
5. Add the new header to `src/notation/CMakeLists.txt`
6. Callers include the notation-side header, not the composing header

---

## 4. Existing Components — The Analysis Foundation

### 4.1 ChordAnalyzer

**File:** `src/composing/analysis/chord/chordanalyzer.h` and `chord/chordanalyzer.cpp`

**Purpose:** Identifies the chord quality, extensions, inversions, and diatonic
degree from a set of simultaneously sounding notes. Returns up to three ranked
candidates, allowing downstream consumers to consider alternatives.

**Algorithm:** Hybrid — template matching for common chord types combined with
procedural extension detection for the combinatorial space of extensions and
alterations. Template matching uses a scoring system that weights root notes most
heavily (1.8×), thirds next (1.2×), and other chord tones equally (1.0×).
TPC (Tonal Pitch Class) data is used for enharmonic disambiguation when available.

#### Input — `ChordAnalysisTone`

```cpp
struct ChordAnalysisTone {
    int pitch = 0;      // MIDI playback pitch (ppitch — honours ottavas and transpositions)
    int tpc = -1;       // MuseScore TPC (0-34, circle-of-fifths spelling). -1 = not provided.
    double weight = 1;  // Relative evidence weight. TODO: populate from duration/beat position.
    bool isBass = false;
};
```

**Important:** `weight` currently defaults to 1.0 for all notes — it is not yet
populated from duration or metric position. This is a planned improvement (see
Section 5.1). Populating weight will improve analysis quality without any changes
to the analyzer itself.

#### Output — `ChordAnalysisResult`

`ChordAnalysisResult` is split into two orthogonal sub-structs (P8a):

- **`ChordIdentity`** — pitch-content properties: what notes make up the chord.
  Stable across different harmonic readings of the same voicing.
- **`ChordFunction`** — tonal-function properties: how the chord relates to the
  key. Changes when the key context changes even if the voicing is identical.

```cpp
// Extension bitmask (P8b) — replaces 17 individual boolean fields.
// Use hasExtension() / setExtension() / hasAnyNinth() / hasAnyThirteenth() helpers.
// Bit order corrected 2026-08-02 (OPEN_ITEMS.md OI-107(b)): bits 4/5, 9/10 and 14/15
// were listed swapped against chordanalyzer.h:213-230.  In-memory only — no serialized
// form depends on it — but a reader deriving a mask from this listing would be wrong.
enum class Extension : uint32_t {
    MinorSeventh      = 1u << 0,
    MajorSeventh      = 1u << 1,
    DiminishedSeventh = 1u << 2,
    AddedSixth        = 1u << 3,
    FlatNinth         = 1u << 4,
    NaturalNinth      = 1u << 5,
    SharpNinth        = 1u << 6,
    NaturalEleventh   = 1u << 7,
    SharpEleventh     = 1u << 8,
    FlatThirteenth    = 1u << 9,
    NaturalThirteenth = 1u << 10,
    SharpThirteenth   = 1u << 11,
    FlatFifth         = 1u << 12,
    SharpFifth        = 1u << 13,
    OmitsThird        = 1u << 14,
    SixNine           = 1u << 15,
};

// Field list re-synced 2026-08-02 (OPEN_ITEMS.md OI-107(d)): naturalFifthPresent,
// tiePriority, isPedalPoint and pedalBassPc were missing from this listing.
struct ChordIdentity {
    double score = 0.0;           // Raw template-match score. Higher is better. Ranking only.
    int rootPc = 0;               // Root pitch class (0-11, C=0)
    int rootTpc = -1;             // Root TPC for enharmonic display (-1 if unknown). See §5.14.
    int bassPc = 0;               // Bass pitch class (0-11)
    int bassTpc = -1;             // Bass TPC for enharmonic display (-1 if unknown)
    bool naturalFifthPresent = false;  // P5 above root sounds; separates Ger+6 from It+6 (§5.11)
    ChordQuality quality = ChordQuality::Unknown;
    int tiePriority = -1;         // Template index; matches snapshot cells back to candidates (E2c)
    uint32_t extensions = 0;      // Bitmask of Extension flags
    bool isPedalPoint = false;    // Bass is a structural pedal point (§5.12; empty on the record
                                  //   path — see §7.4's voice-independent successor)
    int pedalBassPc = -1;         // Pedal bass pitch class; -1 when isPedalPoint is false
};

struct ChordFunction {
    int degree = -1;              // Diatonic degree 0-6; -1 if non-diatonic
    bool diatonicToKey = false;   // True if all sounding pitches are diatonic
    int keyTonicPc = 0;           // Pitch class of mode tonic (0=C)
    KeySigMode keyMode = KeySigMode::Ionian;
};

struct ChordAnalysisResult {
    ChordIdentity identity;
    ChordFunction function;
};
```

#### Chord Quality Enum

```cpp
enum class ChordQuality {
    Unknown,
    Major,
    Minor,
    Diminished,
    Augmented,
    HalfDiminished,
    Suspended2,
    Suspended4,
    Power
};
```

#### Tunable Parameters — `ChordAnalyzerPreferences`

```cpp
struct ChordAnalyzerPreferences {
    double bassNoteRootBonus = 0.70;          // Bonus when candidate root == bass note
                                              // (corrected 2026-08-02, OPEN_ITEMS.md OI-107(a):
                                              //  documented 0.65, code default 0.70 at
                                              //  analysis/types/analysistypes.h:196)
    double diatonicRootBonus = 0.30;          // Bonus when root is in the current key
    double tpcConsistencyBonusPerTone = 0.20; // Bonus per correctly-spelled chord tone
    double rootContinuityBonus = 0.40;        // Bonus for same root as preceding chord
    double resolutionBonus = 0.35;            // Bonus for typical harmonic resolution target

    // Planned — not yet implemented
    bool useExistingChordSymbols = false;
    bool useRomanNumeralAnnotations = false;
    bool useNashvilleAnnotations = false;

    // Planned style prior — not yet implemented
    // enum class StylePrior { General, Classical, Jazz, Pop, Blues, Folk };
    // StylePrior stylePrior = StylePrior::General;

    // Extension detection threshold
    // Jazz preset uses 0.12 (= kSeventhThreshold) to detect lightly-voiced ninths
    // (pcWeight 0.12–0.19).  Standard and Baroque keep 0.20 to suppress ornamental
    // passing tones in counterpoint textures.  Range: 0.10–0.30.
    double extensionThreshold = 0.20;

    // P8c: optimization readiness
    ParameterBoundsMap bounds() const;   // parameter name → {min, max, isManual}
};

inline constexpr ChordAnalyzerPreferences kDefaultChordAnalyzerPreferences{};
```

The `StylePrior` commented-out code is the planned connection between
`ChordAnalyzerPreferences` and the style system (Section 6). When the style system
is implemented, the active style will populate the analyzer's preferences.

**Gate threshold policy**: the inversion-preference gate thresholds in
`postscoringgates.cpp` (Gate I: 0.45, Gate L: 0.35, etc.) are empirically
calibrated against the Baroque corpus and are Baroque-specific. They must not be
loosened to accommodate other styles. When a gate causes regressions in a non-Baroque
preset, the fix is either (a) a tighter structural entry condition that excludes the
problematic chord type in all styles, or (b) a preset-specific threshold value passed
through `ChordAnalyzerPreferences` — leaving the Baroque-tuned default unchanged.
Both corpus presets (Baroque and Jazz) must pass BIR=false regression checks before
any gate change is committed.

**Two corrections, 2026-08-02 (`OPEN_ITEMS.md` OI-107(d)).** (1) The gates do not live in
`chordanalyzer.cpp`: refactor-1 moved the post-scoring gate cluster to
`analysis/chord/postscoringgates.cpp`, where the two surviving margin constants are declared
(`:46` `kGateIMargin = 0.45`, `:47` `kGateLMargin = 0.35`). (2) **Gate K was RETIRED** at Stage 5
on 2026-07-05 (design item D-7; `postscoringgates.cpp:49` records the constant's retirement and
`:523` the gate's), so listing "Gate K: 0.20" as a live calibrated threshold was false. The same
retired threshold is still listed in the `CLAUDE.md` gate-threshold policy; correcting a governing
document is outside this pass's scope and is recorded as owed on OI-107.

#### Public Interface

```cpp
class IChordAnalyzer {
public:
    virtual ~IChordAnalyzer() = default;
    virtual std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,                         // -7 to +7
        KeySigMode keyMode,                             // detected mode (all 21 modes)
        const ChordTemporalContext* context = nullptr,  // optional preceding-chord context
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences
    ) const = 0;
};

/// Default implementation: template-matching rule-based approach.
class RuleBasedChordAnalyzer : public IChordAnalyzer {
public:
    std::vector<ChordAnalysisResult> analyzeChord(...) const override;
};
```

Minimum 3 distinct pitch classes required. Returns empty vector if insufficient data.
Callers instantiate `RuleBasedChordAnalyzer{}` or hold an `IChordAnalyzer*` for
dependency injection (e.g. future ML-based analyzer).

#### Factory — `ChordAnalyzerFactory` (P4b)

```cpp
enum class ChordAnalyzerType { RuleBased };

class ChordAnalyzerFactory {
public:
    static std::unique_ptr<IChordAnalyzer> create(
        ChordAnalyzerType type = ChordAnalyzerType::RuleBased);
};
```

All notation bridge files (`notationcomposingbridge.cpp`, `notationcomposingbridgehelpers.cpp`, `notationharmonicrhythmbridge.cpp`) use `ChordAnalyzerFactory::create()` so the analyzer type is resolved through the factory rather than hard-coded at each call site. Tests that need a direct instance may use `RuleBasedChordAnalyzer{}` on the stack.

#### §4.1b — Contextual Inversion Resolution

**Problem:** The `bassNoteRootBonus` (0.70 — corrected 2026-08-02, OI-107(a); this read 0.65)
biases vertical analysis toward choosing the
bass note as the chord root. For inverted chords (e.g. `Gm/Bb` with Bb in bass) this
produces correct bass-root readings that disagree with music21's functional notation.
74.3% of corpus disagreements have `bassIsRoot=true`. Local scoring fixes for 3-note
inversions consistently regress (see three-attempt history in Section 6).

**Solution:** Contextual bonuses applied only to non-bass-root Major/Minor candidates,
using information from neighbouring chords. Three bonuses were added (historically via a
`contextualBonuses()` helper — removed in Stage 2.3 `18dc9e1829` when `diagnoseChord`
became a view into the production pipeline; the bonuses now live in the competition
pipeline / function layer):

| Bonus | Condition | Default |
|-------|-----------|---------|
| `stepwiseBassInversionBonus` | Bass moves by diatonic step FROM previous region | 0.5 |
| `stepwiseBassLookaheadBonus` | Bass moves by diatonic step TO next region (deferred) | 0.5 |
| `sameRootInversionBonus` | Candidate root matches previous chord's root | 0.4 |

**Safety constraints (lesson from three-attempt history) — ⚠ SUPERSEDED BY ITER 46, see §4.1g.** As
originally written: bonuses never fire for Diminished, HalfDiminished, Augmented, or Suspended
candidates — only Major and Minor. The existing `inversionSuspicionMargin` /
`inversionBonusReduction` mechanism is left unchanged.

**Correction, 2026-08-02 (`OPEN_ITEMS.md` OI-236; the prohibition above carried no supersession note,
so a reader met a hard-won safety constraint that the same document reverses later, in §4.1g).** Iter 46
relaxed it, because keeping it made correct inverted readings unreachable — `C+/E`, `Yø7/X` and their
kind fell below the `results[]` cutoff entirely — and relaxing it produced the largest single
improvement of iteration path 1 (§4.1g). **The constraint that actually survives at HEAD, read off the
code, differs between the two predicates:**

- `supportsContextualInversionBonuses` (`chordanalyzer.cpp:855-870`) admits **Major, Minor, Augmented,
  HalfDiminished**; **Diminished and Suspended candidates still never receive** the three contextual
  inversion bonuses.
- `qualifiesForCompleteTriadInversionBonus` (`chordanalyzer.cpp:829-853`) admits **Major, Minor,
  Diminished, Augmented, HalfDiminished**; only **Suspended** is still excluded.

No code change is owed — the code is the later behaviour and is correct; what was owed was saying so
here.

**`ChordTemporalContext` fields (§4.1b additions):**

| Field | Populated by | Status |
|-------|-------------|--------|
| `previousRootPc` | Both bridges | ✅ Active |
| `previousQuality` | Both bridges | ✅ Active |
| `previousChordAge` | — | Reserved (not yet populated) |
| `previousBassPc` | Both bridges | ✅ Active |
| `bassIsStepwiseFromPrevious` | Both bridges | ✅ Active |
| `nextRootPc` | batch (Iter 92); bridge parent-scope (Iter 95 Step 1); bridge sub-region (Iter 95 Step 2) | ✅ Active |
| `nextBassPc` | batch + bridge parent-scope (Iter 92) | ✅ Active |
| `bassIsStepwiseToNext` | — | Deferred |
| `jazzMode` | Retired (69716deead) | Removed — no remaining callers after tool-side Jazz path deletion |

`isDiatonicStep(pc1, pc2)` helper declared in `notationcomposingbridgehelpers.h` (inline).
Both bridges (`notationcomposingbridge.cpp` and `notationharmonicrhythmbridge.cpp`) populate
`previousBassPc` and compute `bassIsStepwiseFromPrevious` before each analysis call.

**Validation (20260406_122004, git `bcc0811f67`; retired Bach reference methodology):**

| Metric | Baseline | §4.1b |
|--------|----------|-------|
| Chord identity | 83.4% (3383/4058) | **50.0% (WIR structural, 2026-04-09; supersedes 83.7% onset-only/music21 figure)** |
| chord_disagree | 673 | **661** (−12) |
| bassIsRoot fraction (est.) | 74.3% | ~72.9% |
| Catalog regressions | 0 | 0 |

#### §4.1c — Regional Note Accumulation (Classical Mode)

**Problem:** Per-tick pitch-class snapshots treat all notes as equal regardless of
duration, metric position, or repetition across a region. Short passing tones receive
the same weight as sustained structural pitches.

**Solution:** Replace per-tick evidence with pitch evidence accumulated across the
entire harmonic region, weighted by three factors:

1. **Beat weight** (Pass 1): `(durationInRegion / regionDuration) × beatWeight`
   — DOWNBEAT 1.0, STRESSED 0.85, UNSTRESSED 0.75, SUBBEAT 0.5
2. **Repetition boost** (Pass 2): `weight × (1.0 + 0.3 × (distinctMetricPositions − 1))`
   for pitch classes appearing at more than one distinct metric position
3. **Cross-voice boost** (Pass 3): `weight × 1.5` for pitch classes sounding in more
   than one voice simultaneously

Harmonic boundaries are detected via **Jaccard distance** between consecutive
quarter-note window PC bitsets: `distance = 1 − |A∩B| / |A∪B|`. Threshold 0.6
(`harmonicBoundaryJaccardThreshold` in `ChordAnalyzerPreferences`).

**Sustained notes:** Notes that attack before `startTick` and are held into the
region are captured by a backward walk (matching the `collectSoundingAt` pattern).
This carry-in collection runs even when there is already a `ChordRest` segment exactly
at `startTick`, so region analysis keeps pedal/support tones that continue across beat
boundaries.

**Known gap — piano pedal sustain:** The carry-in walk intentionally preserves held
support tones, but §4.1c still treats a long sustain-pedal sonority as structurally
active for the whole region. In Romantic piano textures this can smear the evidence for
later harmonies instead of letting stale pedal support decay, so the remaining gap is a
pedal-role/decay model rather than missing note collection.

#### Duplicate note collection paths — RESOLVED (Iter 97)

This Rule 10 violation (two separate `collectRegionTones()` copies — one in
`notationcomposingbridgehelpers.cpp`, one in `tools/batch_analyze.cpp`) has been resolved
exactly as the original resolution note predicted. The shared logic now lives in
`src/composing/analysis/engravingbridge/regiontonecollector.{h,cpp}` (note collection /
sub-boundary detection) and `src/composing/analysis/region/regionanalyzer.{h,cpp}` (the
whole region-orchestration algorithm), both consumed through a tone abstraction with no
notation dependency. The notation bridge and `batch_analyze` are now thin wrappers over
`region::analyzeRegions()` — there is a single implementation, so note-collection or
boundary-detection changes are made once and both paths pick them up automatically. (The
former Jaccard boundary detector was replaced by greedy-expand in Iter 77 and deleted in
Iter 81; greedy-expand is the single segmentation algorithm on both paths.) See §3.3
"Region Analysis — Canonical Modules" for the module map and the D1/D2 divergence audit.

#### Region identity modes (decided 2026-04-11)

Preserve-all harmonic regions use different identity keys depending on the output mode:

**Harmonic summary mode** (status bar, analysis, tuning): region identity = root pitch
class + quality. Adjacent regions with the same root and quality are merged. Extensions,
inversions, and slash chord bass notes are secondary metadata, not identity keys.

**As-written mode** (chord track "as written"): region identity = full sonority including
extensions and bass note. Octave doublings are preserved. Adjacent regions are merged
only when the full sonority matches.

Current implementation: harmonic summary mode only. As-written mode is deferred —
requires a mode flag in the implode bridge and a separate merge pass. The chord track
octave deduplication limitation (§5.8) is the primary consequence of this deferral.

**New API:**
- `collectRegionTones(score, startTick, endTick, excludeStaves)` — implemented in
  `notationcomposingbridgehelpers.cpp`; declared in `notationcomposingbridgehelpers.h`
- `detectHarmonicBoundariesJaccard(score, startTick, endTick, excludeStaves, threshold)`
  — returns sorted vector of boundary `Fraction` ticks; first = `startTick`
- `ChordAnalysisTone` extended with 3 fields: `durationInRegion`, `distinctMetricPositions`,
  `simultaneousVoiceCount` (all initialize to 0 for backward compatibility)
- `useRegionalAccumulation()` / `setUseRegionalAccumulation()` in `IComposingAnalysisConfiguration`
  (default `true`; settings key `composing/useRegionalAccumulation`)

**Bridge wiring:** `notationharmonicrhythmbridge.cpp` branches on `useRegionalAccumulation`:
- Regional path: `detectHarmonicBoundariesJaccard` → `collectRegionTones` → `analyzeChord`
- Legacy path: per-tick PC bitset comparison (unchanged)

**Validation (20260406_151131; Bach baseline corrected 2026-04-09):**

| Metric | §4.1b | §4.1c |
|--------|-------|-------|
| Chord identity (Bach 352 chorales) | 50.0% (WIR structural, 2026-04-09; supersedes 83.7% onset-only/music21 figure) | **50.0% (WIR structural, 2026-04-09; supersedes 83.7% onset-only/music21 figure)** |
| chord_disagree | 661 | **661** (unchanged) |
| Beethoven BIR% of disagreements | 59.4% | **57.3%** (−2.1 pp) |
| Catalog regressions | 0 | 0 |

#### Temporal context — `ChordTemporalContext` vs future `TemporalContext` (P4b)

`ChordTemporalContext` carries the **immediately preceding chord's** root, quality, and
bass, plus stepwise-motion flags — sufficient for root-continuity, resolution-bias, and
contextual inversion scoring (§4.1b). It is **not** a full progression context. A future
`TemporalContext` will carry the full recent progression (chord sequence, cadence history,
secondary dominants) once secondary dominant analysis (§5.6) is implemented. Keep the
names distinct.

#### §4.1d — Joint (bass, chord) scoring bonuses (Iters 92–96)

The core scoring loop in `RuleBasedChordAnalyzer::analyzeChord` enumerates
`(bass candidate, root, template)` triples and applies a set of contextual
bonuses layered on top of the base template score. All bonuses share three
common gates: `jointScoringEnabled` (false on single-tick / unit-test path),
`prefs.scoringPhase == ScoringPhase::Final` (the progression signals are withheld
during `greedyExpandSegmentation`'s internal boundary-exploration calls, which run in
`ScoringPhase::Segmentation` — prevents the bonus from biasing segmentation
before the final per-region pass), and a populated `context` pointer.

| Bonus | Lambda | Value | Quality gate | Extra gates | Iter |
|-------|--------|-------|--------------|-------------|------|
| `w_complete` | `wCompleteBonus` | +0.50 | root-position only (`bassPc == rootPc`) | `distinctPcs >= 3`, all three triad tones present above `extensionThreshold` | 92 |
| `w_stepIn` | `wStepInBonus` | +0.10 | root-position only | `previousBassPc` moves ≤2 semitones to bass; not Power quality; m7-family guard | 94 |
| `w_stepOut` | `wStepOutBonus` | +0.10 | root-position only | bass moves ≤2 semitones to `nextBassPc`; same guards as `w_stepIn` | 94 |
| `w_seq` | `wSeqBonus` | +0.20 | any inversion | `nextRootPc >= 0`; `((nextRootPc - rootPc + 12) % 12) == 5` (P4-below = descending-fifth); `distinctPcs >= 4` | 95 |
| `w_dim` | `wDimBonus` | +0.15 | Diminished or HalfDiminished only | `nextRootPc >= 0`; `((nextRootPc - rootPc + 12) % 12) == 1` (semitone resolution = leading-tone); `distinctPcs >= 4` | 96 |

**`w_stepIn` / `w_stepOut` surgical guards (Iter 94):**

Two additional guards beyond the root-position and Power exclusions:

1. *First-inversion-m7-family guard* — if any competitor in the same `perBass`
   block with quality in {HalfDiminished, Diminished, Minor7} sits at
   `(candBassPc − 3) mod 12` (minor third below our bass = first-inversion
   shape) AND scores within `kStepBudget = kWStepIn + kWStepOut + 0.01` of the
   candidate's unbonused score, both step bonuses are suppressed. Prevents
   `w_stepIn`/`w_stepOut` from tipping a fragile m6 root-position reading
   (e.g. Dm6) over an equally viable first-inversion m7-family reading (e.g.
   Bø7/D) on identical pitch evidence.

2. *Power exclusion* — root+fifth-only templates are excluded outright.
   Extending the exclusion to Suspended2/4 regressed Jazz BIR=false, so the
   current cut is Power-only.

**Parent-scope context plumbing (Iter 94):**

Bridge Pass 2 / Pass 2b in `notationharmonicrhythmbridge.cpp` and the main
analysis loop in `tools/batch_analyze.cpp` compute the predecessor / successor
PARENT region's bass PC and override `subCtx.previousBassPc` / `subCtx.nextBassPc`
for each sub-region call. The override happens AFTER the stepwise booleans
(which remain sub-region-scope for passing-tone/inversion signals) and BEFORE the
`analyzeChord` call; a post-call restore keeps the next iteration's stepwise
boolean correct. The same pattern was applied to `nextRootPc` in Iter 95 Step 2.

**`ScoringPhase` (Iter 94 as `explorationMode`; reworked to the enum in `e7d4ba2b1a`):**

`ChordAnalyzerPreferences::scoringPhase` (default `ScoringPhase::Final`) is set to
`ScoringPhase::Segmentation` by `greedyExpandSegmentation` on every internal
boundary-exploration call. This prevents the contextual bonuses from biasing sub-region
bass selection during segmentation, before the final per-region scoring pass. (Replaced
the former `bool explorationMode` flag — see `docs/scoring_model.md` §"ScoringPhase".)

**`w_dim` gate note (Iter 96):**

The `distinctPcs >= 4` gate confines `w_dim` to fully-stated dim7 chords (4 PCs)
and rules out 3-PC sparse regions where dim-triad vs Major/Minor is a quality
contest rather than a rotation contest. A future variant may add a rotation-only
condition (require the current winner to also be Dim/HalfDim) to recover
improvements on the sparse-region tier (e.g. `schumann bvo7→viio7/V`,
`chorale_003 Am→G#dim`) that the `distinctPcs >= 4` gate currently suppresses.

**STEP 1 — dim7-completeness guard + Gate J (Iter 97, commit `3d80d0a91d`):**

Two coupled changes to the diminished/dominant family in `chordanalyzer.cpp`:

1. *dim7-completeness requirement.* The dim7 characteristic bonus now fires only when the
   full diminished triad is present (root + ♭3 + ♭5). An incomplete diminished sonority no
   longer earns the dim7 bonus, so it stops out-scoring the dominant-seventh reading that
   the same pitch evidence actually supports. This is what fixes the incomplete-dim-vs-
   dominant confusions (Jazz: bwv282, bwv60.5, bwv65.2; Baroque BIR=false 25→23).

2. *Gate J — vii° → V7 completion.* A **root-position diminished triad whose dominant root
   (a major third below the diminished root) is present** is treated as an **inverted V7**
   rather than a root-position vii°. Canonical case: bwv110.7 m10 `C#dim7 → F#7` — the C#
   diminished triad over a sounding F# is the leading-tone chord functioning as the dominant,
   so the analyzer promotes it to the dominant-seventh reading. Gate J requires the **complete
   diminished triad** to be present before the promotion fires, so it never triggers on a thin
   2-PC dyad. 5 pipeline-snapshot goldens were refreshed and DCML-verified for this change.

---

#### Design boundary — vertical sonority vs functional/contextual harmony

`RuleBasedChordAnalyzer` is a **vertical sonority analyzer**: it identifies what chord
is implied by the set of simultaneously sounding notes at a single point in time. It
does not perform functional harmonic analysis (Roman-numeral reductions, cadence
detection, tonicization, secondary dominants) or contextual annotation (what role this
chord plays in the surrounding progression).

This boundary is intentional and has been validated empirically. Corpus analysis against
DCML annotations (four corpora, 2026-04-06) established a retired onset-only/music21
comparison ceiling of ~83–84% for Bach chorales; the official Bach structural baseline is now
50.0% against local When in Rome RomanText annotations (2026-04-09). The remaining divergence is not
an analyzer defect — it represents legitimate cases where:

- **3-note triads in inversion** (bass ≠ functional root): DCML annotates the
  functional root; vertical analysis defaults to bass=root. For bare triads this
  cannot be resolved from local note content alone. 95.8% of all disagreements
  with BIR (bass-is-root) errors are 3-note triads.
- **Functional prolongation**: DCML may annotate a passing or neighboring chord as
  part of a broader harmonic region (e.g. a cadential 6-4 as dominant), while vertical
  analysis identifies the sounding notes independently.

Improving beyond ~84% requires a **contextual harmony layer** (Phase 2) that consumes
a sequence of `ChordAnalysisResult` outputs and applies voice-leading, cadence, and
harmonic-sequence reasoning. That layer is explicitly out of Phase 1 scope. Do not
attempt to improve corpus agreement by adding heuristics to `RuleBasedChordAnalyzer`
that embed contextual assumptions — keep the vertical/contextual boundary clean.

#### §4.1g — Iteration Path 1 Close (final state)

Iteration path 1 — incremental gate additions and scoring tweaks on the existing
`RuleBasedChordAnalyzer` — is complete as of commit `5df8421114` (2026-05-10).
The remaining residual is fully characterised and not further reducible without
architectural changes (boundary-detection replacement, contextual harmony layer).

**Final BIR baselines (Iteration Path 1 close):**

| Metric | Value | Source |
|---|---|---|
| Three-way genuine BIR=true | **21** | Baroque corpus, 353 chorales |
| Three-way genuine BIR=false | **128** | Baroque corpus, 353 chorales |
| Jazz BIR=false (hard-stop reference) | **20** | ≤ 75 hard-stop |
| Two-way chord_disagree | 1575 | Baroque corpus |

"Three-way genuine" = our analysis disagrees with **both** music21 and the
DCML-annotated reference (When-in-Rome). Two-way `chord_disagree` is our vs music21;
the gap between two-way and three-way is the `near_agree` reclassification — regions
where music21 matches our 2nd or 3rd alternative (genuine partial successes, not
uncounted failures).

**Active gates (chordanalyzer.cpp):**

Gates fire in `analyzeChord()` after the initial scoring pass, before results
are returned. Each operates on **structured fields only** (rootPc, bassPc, quality,
extensions, key tonic, scale, score margin) — no chord-symbol string parsing,
no Roman-numeral inference. Conditions are pre-conditions on `winner` and a
candidate runner-up `inv`/`alt`. Iteration number is the path-1 iteration in which
the gate was introduced or last modified.

| Gate | Iter | Condition (winner → preferred alt) | Effect at introduction |
|---|---|---|---|
| **A** (winnerCorrection enharmonic flip) | 2–3 | MajorAdd6 ↔ Minor7 inversion enharmonic pair; bestAlt at expectedAltRoot in results[] | Foundational; pre-path-1 |
| **B** | 3 | + context.nextRootPc == altRoot && bassIsStepwiseToNext | Foundational |
| **C** | 3 | + altRoot in recentRootPcs && bassIsStepwiseFromPrevious | Foundational |
| **D** | 3 | + consecutiveBassStepwiseCount ≥ 2 | Foundational |
| **E** (first-inversion) | 4 | Minor winner; bestAlt.rootPc == (winner.rootPc + 8) % 12; stepwise bass | Foundational |
| **F** (second-inversion) | 4 | Major bestAlt; altRoot == (winner.rootPc + 5) % 12; stepwise bass | Foundational |
| **G-E** (key-context) | 12, 21 | Minor+Add6 winner; HalfDim7 alt rooted on leading-tone, supertonic, or mediant of key; rawCandidates fallback (Iter 21) when HalfDim suppressed by temporal context | 27 BIR=true |
| **G-B / G-C / G-D** | 12 | Temporal fallbacks for MinorAdd6 → HalfDim7 (analogous to B/C/D) | (part of Iter 12 / 21) |
| **H** | 7C | Augmented winner; alt rooted at winner.rootPc + 4 or +8 (root-symmetry); + temporal evidence (H-B/H-C/H-D) | Augmented root-disambiguation |
| **I** | 25 | Minor winner, bassIsRoot=true; alt with same bass, non-root-position, root a major-third below bass (I4 interval), diatonic; score margin ≤ 0.45 | 18 BIR=true |
| **K** | 30 | Augmented winner, bassIsRoot=true; alt same bass, non-root-position, root a major-third below bass; quality Augmented or Major+SharpFifth; diatonic; margin ≤ 0.20 | 1 BIR=true |
| **L** | 32 | Plain Augmented winner (no 7th), bassIsRoot=true; alt has same root AND same bass (root-position), Major quality, diatonic; margin ≤ 0.35 | 4 BIR=true |
| **kCleanQualities guard** | 60 (`381b401add`) | Minor or Minor+AddedSixth winner; HalfDim alt where all 4 tones confirmed (root, root+3, root+6, root+10 mod 12); bass is m3/b5/m7 of HalfDim alt root; gate: `preferMinorOverMajorAdd6` → deduction on winner score | Enables HalfDim inversion bonus to fire; part of Iter 60+61 composite fix |
| **HalfDim first-inversion bonus** | 61 (`a34dba041e`), 65 (`af785da463`) | Same structural check as kCleanQualities; bass PC exempt from `extensionThreshold` in `allTonesPresent` (Iter 65: bass is sounding by definition); score bonus applied to HalfDim candidate, gated on `preferMinorOverMajorAdd6` | BIR=true 7→6; BIR=false 132→125 (bonus eliminated 7 false-positive Power/Minor inversions) |

**Active scoring extensions — Iter 46 (`36bf4738a8`):**

`supportsContextualInversionBonuses()` and `qualifiesForCompleteTriadInversionBonus()`
in `chordanalyzer.cpp` were extended to include `Augmented` and `HalfDiminished` in
addition to the original `Major`/`Minor` (and `Diminished` for the latter). Before
Iter 46, Augmented and HalfDiminished inversion candidates received neither
`stepwiseBassInversionBonus` (+0.50), `stepwiseBassLookaheadBonus` (+0.50),
`sameRootInversionBonus` (+0.40), nor `completeTriadInversionBonus` (+0.45) — so
correct inverted readings (e.g. `C+/E`, `Yø7/X`) fell below the `results[]` cutoff
entirely and were unreachable by Gate H/Q. Extending these gates put Augmented and
HalfDiminished inversion candidates on equal footing with Major/Minor.

**Effect of Iter 46 scoring extension:** BIR=true 32→21 (Δ −11), BIR=false 177→128
(Δ −49). Largest single improvement of iteration path 1.

**Active counting methodology — Iter 36 (`5df8421114`, recovered 2026-05-10):**

`tools/batch_analyze.cpp` emits `rootPitchClass`, `bassPitchClass`, `quality`, and
`bassIsRoot` on each alternative entry in `.ours.json`. This activates the
`_matches_alternative` reclassification in `tools/compare_analyses.py`, which moves
chord_disagree regions where music21 matches our 2nd or 3rd alternative into the
`near_agree` bucket. Without these fields the comparison reverts to pre-Iter-36
counts (~700 BIR=false). The change was originally Iter 36 but the commit was lost
to a git reset on 2026-05-09; recovered and re-committed at `5df8421114`.

**Deprecated algorithm — `detectHarmonicBoundariesJaccard`:**

The Jaccard-based boundary detector
([notationcomposingbridgehelpers.cpp](src/notation/internal/notationcomposingbridgehelpers.cpp);
duplicate in [tools/batch_analyze.cpp](tools/batch_analyze.cpp), see Task #58 below)
is deprecated and slated for replacement by **Task #62**. Reasons:

- **Fixed quarter-note window** (`Constants::DIVISION`) — wrong for non-4/4
  meters, swing-eighth feel, or any meter where the harmonic rhythm does not
  align with the quarter-note grid.
- **Jaccard measures pitch-class overlap, not harmonic function** — two regions
  sharing 70 % of their pitch classes can still be functionally distinct (a IV–V
  motion has high pitch overlap if the bass moves diatonically), and two regions
  with low overlap can be the same chord under embellishment.
- **Running accumulation** suppresses subsequent boundaries within a region
  (`prevBits = unionBits` on non-boundary windows), so a gradual harmonic shift
  never fires a boundary even when the shift is complete.
- **Single-pass with no revision** — once a boundary is missed or spuriously
  fired, there is no later pass that re-evaluates segmentation in light of the
  inferred chord identities.

Parameter tuning was exhausted in Iter 48/48b/48c: threshold 0.50 regresses
(BIR=true 21→29, BIR=false 128→154); threshold 0.60 is the local optimum and
the documented quality ceiling for this algorithm.

**Replacement (Task #62): IMPLEMENTED on batch path** — iterative greedy-expand
algorithm with preset-controlled stopping threshold, activated in Iter 54
(commit `f92a4f1a3b`). `tools/batch_analyze.cpp` now uses greedy-expand for all
Baroque-preset analysis. The bridge path (`notationcomposingbridgehelpers.cpp`)
still uses Jaccard; Task #58 (consolidation into `src/composing/`, §2.10) remains
open and is a prerequisite for unifying both paths.

**Genuine-21 residual — Path 1 floor (for historical reference):**

At the close of Iteration Path 1, 21 BIR=true cases remained. That count has
since been reduced in Iteration Path 2 (see §4.1h). The clusters listed here
are the original Path-1 characterization; individual cases have been resolved
or re-characterized since.

| Cluster | Count (Path 1) | Pattern | Why blocked at Path 1 close |
|---|---|---|---|
| **Gate M cluster** | 7 | Winner = Minor (root-position); correct = Diminished or HalfDiminished at same bass | No temporal signal reliably separates genuine from false-positive at any viable threshold. |
| **Cluster A** (Minor6 ↔ HalfDim 1st-inv) | 7 | Winner = Minor6 root-position; correct = HalfDiminished 1st inversion at same bass (`Xm6 ≡ Yø7/X`) | 5/7: correct alternative absent from `results[]` — candidate-generation gap. 2/7: FP rate 9:2. |
| **Power / Suspended** | 4 | Winner = Power or Suspended quality at root-position | Not fully diagnosed at Path 1 close. |
| **Edge cases** | 2–3 | Individually examined; no shared pattern | No viable gate. |

**Current residual — see §4.1h for the live Genuine-5 breakdown.**

The 128 BIR=false residual was not separately re-characterised in path 1;
remediation is expected from the Task #62 replacement algorithm, which will
change the region boundaries on which inversion analysis runs.

**Pending tasks (carried into iteration path 2):**

- **Task #36** — Move gate thresholds (`0.45`, `0.20`, `0.35`, etc.) from
  inline literals in `chordanalyzer.cpp` into `ChordAnalyzerPreferences`.
  Required before any preset-specific calibration is attempted.
- **Task #50** — Build verified BWV→DCML MSCX mapping registry. Current
  mapping is implicit in `tools/dcml/when_in_rome` directory layout and is
  not verified score-by-score.
- **Task #58** — Consolidate duplicate `detectHarmonicBoundariesJaccard`
  implementations (§2.10 violation). Prerequisite for Task #62.
- **Task #62** — ~~Design and implement replacement segmentation algorithm~~ **IMPLEMENTED**
  on batch path (Iter 54, commit `f92a4f1a3b`). Bridge path consolidation (Task #58)
  still open.
- **Task #63** — Iteration-path-1 wrap-up — **DONE** (commit `c0d06d3965`).

#### §4.1h — Iteration Path 2 — Current State (May 2026)

Iteration Path 2 continues active scoring and segmentation improvement on top
of the greedy-expand batch path. No architectural changes relative to Path 1;
all fixes are targeted scoring bonus / guard additions in `chordanalyzer.cpp`.

**Current BIR baselines (as of Iter 65, commit `af785da463`):**

| Metric | Value | Commits producing this baseline |
|---|---|---|
| Three-way genuine BIR=true | **5** | `a34dba041e` (Iter 61), `af785da463` (Iter 65) |
| Three-way genuine BIR=false | **125** | `a34dba041e` (Iter 61) |
| Jazz BIR=false (hard-stop reference) | **12** | unchanged since Iter 46 |
| Composing tests | **407/407** | |
| Notation tests | **53/53** | |

**Path 2 fixes applied (Iters 55–65):**

- **Iter 55** — Baseline update + pipeline snapshot goldens refresh after greedy-expand switch.
- **Iter 56/57** — Re-characterize genuine-14; identify 4 BIR=false regressions from Jaccard→greedy-expand.
- **Iter 58–59** — Blocker C investigation: HalfDim candidates are enumerated for all 12×16 root×template combinations; real issue is scoring/penalty imbalance.
- **Iter 60** (`381b401add`) — kCleanQualities guard (HalfDim inversion deduction on Minor/Minor6 winner) + alternative cap raised 2→3. BIR=true 14→7.
- **Iter 61** (`a34dba041e`) — HalfDim first-inversion score bonus (Option B), gated on `preferMinorOverMajorAdd6`. BIR=true 7→6, BIR=false 132→125.
- **Iter 62** (`ee337aeca4`) — Parallel corpus regen: `run_bach_preset.py` now uses `ProcessPoolExecutor(max_workers=24)`. 353 chorales in ~204 s on Ryzen 9 3900X.
- **Iter 63** (`cd6a61e6a0`) — Baseline enumeration (BIR=true=6, BIR=false=125); fresh characterization of all 6 genuine cases saved to `tools/iter63_genuine6_characterization.txt`.
- **Iter 65** (`af785da463`) — Bass-PC exemption in `allTonesPresent` for HalfDim inversion check (bass is sounding by definition; was falsely failing threshold). BIR=true 6→5.

**Genuine-5 residual — Iter 63 characterization (bwv187.7 fixed in Iter 65):**

| Case | Cluster | Pattern | Status |
|---|---|---|---|
| bwv184.5 m=13 b=3.0 | Scoring gap | Winner A5 (2.05) vs Dsus2/A (1.98); gap 0.07 | Target of Iter 66 sus2 P5-inversion bonus |
| bwv184.5 m=13 b=4.0 | Hypothesis A | 6 PCs: over-merged A7→D cadence; boundary split | Segmentation fix needed; deferred to Iter 66+ |
| bwv371 m=35 b=2.5 | Correct | Annotation disagreement; our analysis likely correct | No fix needed |
| bwv372 m=10 b=1.5 | Hypothesis A | {C,G,A}: Bb missing from region; adjacent regions Bb-rooted | Segmentation fix needed; deferred to Iter 66+ |
| bwv43.11 m=3 b=2.0 | Scoring gap / absent | {D,E,A}=Dsus2; Dsus2 not in results[] (cap-3 A-rooted); results-cap issue | Target of Iter 66 sus2 P5-inversion bonus |

**Pending performance work:**

- **Iter 64 (not yet committed)** — Root-present pre-filter: `if (pcWeight[rootPc] <= 0.0) continue` before inner template loop in the 12×16 candidate scoring loop. Output-neutral; expected ~50–65% candidate elimination. Primary benefit: real-time bridge path latency. Instruction at `docs/prompts/iteration_64_root_present_prefilter.md`.

**Pending tasks (active):**

- **Task #36** — Move gate thresholds into `ChordAnalyzerPreferences`.
- **Task #50** — Build verified BWV→DCML MSCX mapping registry (`tools/dcml_bwv_map.json`).
- **Task #58** — Consolidate duplicate `detectHarmonicBoundariesJaccard` (§2.10). Prerequisite for bridge-path greedy-expand unification.

**Sub-beat boundaries and DCML alignment (noted 2026-05-15):** Sub-beat boundaries
from Iters 72/73/83 (note-end tick collection, head/tail-gap synthesis) do not align
with music21's beat-anchored DCML annotation positions. This creates alignment
measurement noise but does not affect chord accuracy. The time-overlap comparator
(`tools/compare_analyses.py`, `mode='time-overlap'`) handles this correctly via the
lenient-OR-50% overlap threshold.

---

#### §4.1i — Technical Debt and Refactor Backlog (reviewed 2026-05-22)

An external code review of `src/composing/` was conducted and assessed against
project context. Findings are categorised below by priority and actionability.

**Act now — real risk or low-risk cleanup:**

- **`pitchClassName()` / `pitchClassNameFromTpc()` duplication** — both functions
  maintain nearly-identical static name arrays for Standard / German spelling.
  This is the highest-priority item: Iters 84, 88, and 89 each touched
  `pitchClassNameFromTpc()`'s TPC-disambiguation block and had to carefully *not*
  touch `pitchClassName()`. One careless edit to either without mirroring the other
  is a latent mis-spelling bug. **Fix:** extract shared `static const char*` arrays
  into a small central helper used by both functions. Moderate effort, real risk.

- **`ChordSymbolFormatter` in `chordanalyzer.h`** — a display-layer class declared
  alongside analysis types. Violates the analysis-is-display-agnostic principle
  (§2.3). **Fix:** move to its own `chordsymbolformatter.{h,cpp}` pair. Low risk,
  low effort — a file move with no logic change. **PARTLY DONE — status corrected 2026-08-02
  (`OPEN_ITEMS.md` OI-112(a)).** Refactor-1 moved the IMPLEMENTATION to
  `analysis/chord/chordsymbolformatter.cpp`; the DECLARATIONS were intentionally left in
  `chordanalyzer.h` and no `chordsymbolformatter.h` exists. The header half is the residue; it is
  tracked as OI-108(b), and the boundary the item was written to protect is now enforced
  mechanically both ways by `inference_presentation_boundary_tests` (see the record-path section
  at the head of this document).

**Defer until scoring stabilises:**

- **Split `ChordAnalyzerPreferences`** — the struct conflates chord-scoring weights,
  inversion heuristics, harmonic-boundary thresholds, and pedal-tail weight.
  Valid technical debt (several fields are self-described as such). However,
  splitting the struct mid-iteration requires updating all callers twice. Revisit
  after a scoring stabilisation phase, not during active iteration.

- **Segmentation ↔ scorer phase coupling** — `greedyExpandSegmentation` sets
  `scoringPhase = ScoringPhase::Segmentation` on every internal `analyzeChord` call,
  creating a dependency from the segmentation algorithm into chord-scorer internals
  (introduced Iter 94 as the `explorationMode` flag; reworked into the `ScoringPhase`
  enum in `e7d4ba2b1a`, which removed the per-function dual-path and left a single
  control point in `applyHarmonicFunction`). The residual coupling — segmentation telling
  the scorer which phase it is in — remains; a clean separation of segmentation vs.
  final-analysis concerns would remove it entirely. Major refactor — defer.

- **Data-driven mode definition table** — `keyModeTonicName()` and
  `keyModeTonicOffset()` use separate static arrays per mode family and share
  comment patterns that repeat the same "mode family / parent key signature" logic.
  Consolidating into a single mode-metadata table would improve maintainability.
  Correct-as-is; defer.

**Do not remove:**

- **`useExistingChordSymbols`, `useRomanNumeralAnnotations`,
  `useNashvilleAnnotations`** in `ChordAnalyzerPreferences` — these are placeholder
  fields for planned features, not dead code. The LLM integration design
  (`docs/llm_integration.md`) and the Authoritative Chord Symbol Mode (§4.1f)
  depend on `useExistingChordSymbols`. Removing them would require an explicit
  feature-abandonment decision.

**Ongoing concern (no immediate fix):**

- **Accumulating scoring heuristics in `chordanalyzer.cpp`** — each iteration adds
  well-justified gates, bonuses, and lambdas (`wSeqBonus`, `wDimBonus`, `wComplete`,
  `wStepIn/Out`, Gate J, Gate K/L, etc.). Individually each is correct; collectively
  they are becoming harder to reason about holistically. No structural fix is obvious
  without a broader redesign, but new bonuses should be scrutinised carefully for
  interaction effects with existing ones before committing.

---

### 4.2 KeyModeAnalyzer

**File:** `src/composing/analysis/key/keymodeanalyzer.h` and `key/keymodeanalyzer.cpp`

**Purpose:** Infers the most likely key and mode from a temporal window of pitch
contexts. Uses duration weight, metric weight, and bass status to give more
influence to harmonically significant notes. Returns up to three ranked candidates.

**Algorithm:** Scores all 12 possible tonics against all **21 modes** (7 diatonic +
7 melodic minor family + 7 harmonic minor family = 252 candidates) using six orthogonal
helper functions:
- `scoreScaleMembership` — how well the pitch classes fit the candidate scale,
  cross-referenced against the notated key-signature scale
- `scoreTriadEvidence` — how strongly the tonic triad is present (tonic 1.6×,
  third 0.7×, fifth 0.5×, leading tone 0.4×; complete triad bonus 2.5)
- `scoreCharacteristicPitch` — boost/penalty for the characteristic pitch(es) that
  most distinguish each mode from its closest neighbor (e.g. Dorian's raised 6th vs
  Aeolian; harmonic minor's raised 7th; multiple compound conditions for non-diatonic modes)
- `scoreTrueLeadingTone` — bonus when the semitone below the tonic is present,
  regardless of diatonicism (chromatic leading tones still signal the tonic strongly)
- `scoreKeySignatureProximity` — preference for keys close to the notated key
  signature (−0.6 per fifth of distance)
- `scoreModePrior` — **21 independent additive priors**, one per mode, user-configurable
  via `IComposingAnalysisConfiguration::modePrior{ModeName}()`; defaults reflect Western
  tonal frequency (Ionian=+1.20, Aeolian=+1.00, down to Altered=−3.50)
- `applyRelativePairDisambiguation` — post-hoc score mutations for the relative
  major/minor pair sharing a key signature (four documented cases; see implementation)

The key-signature path uses a separate focussed `tonalCenterScore` formula for the
final same-key-signature family decision, independent of the main scoring weights so
both can be tuned without cross-interference. For diatonic family decisions, tonal-
centre disambiguation is now guarded by the raw candidate score: it may break close
same-key-signature ties, but it must not overturn a materially stronger raw winner.

All scoring weights are named constants in `KeyModeAnalyzerPreferences`.

#### Input — `PitchContext`

```cpp
struct PitchContext {
    int pitch = 0;               // MIDI pitch number
    double durationWeight = 1.0; // Duration in quarter notes — longer notes have more influence
    double beatWeight = 1.0;     // 1.0 = downbeat, ~0.2 = offbeat
    bool isBass = false;         // Bass notes weighted 2× in analysis
};
```

**Relocation (types-leaf, as-built).** `PitchContext` was **un-nested** out of `class KeyModeAnalyzer`
and now lives in the cross-layer value-types leaf header `composing/analysis/types/analysistypes.h`
(pure relocation — same name, namespace `mu::composing::analysis`, layout, and definition).
`KeyModeAnalyzer` keeps a member alias `using PitchContext = analysis::PitchContext;`, so existing
call sites (`KeyModeAnalyzer::PitchContext`) are unchanged. See the types-leaf note under
"Region Analysis — Canonical Modules" above.

**Important:** In the current calling code, `durationWeight`, `beatWeight`, and
`isBass` are populated from the score. The bridge collects a 16-beat lookback +
8-beat lookahead window with exponential time decay (0.7× per measure) and
beat-type weights from MuseScore's `BeatType` enum.

#### Output — `KeyModeAnalysisResult`

```cpp
enum class KeySigMode {
    // Diatonic family (7)
    Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian,
    // Melodic minor family (7)
    MelodicMinor, DorianB2, LydianAugmented, LydianDominant,
    MixolydianB6, AeolianB5, Altered,
    // Harmonic minor family (7)
    HarmonicMinor, LocrianSharp6, IonianSharp5, DorianSharp4,
    PhrygianDominant, LydianSharp2, AlteredDomBB7,
};  // 21 modes total

**Harmonic major modes — deferred:** The harmonic major scale and its 7 modes were
considered for inclusion in this expansion but deferred. Harmonic major modes are
significantly rarer as tonal centers than melodic and harmonic minor modes, and the
validation corpus is unlikely to calibrate them well. They can be added as a future
extension following the same pattern as the melodic and harmonic minor families.

struct KeyModeAnalysisResult {
    int keySignatureFifths = 0;             // Resolved key signature (-7..+7, Ionian convention)
    KeySigMode mode = KeySigMode::Ionian;   // Detected mode
    int tonicPc = 0;                        // Pitch class of the mode's tonic (0=C, 2=D, etc.)
    double score = 0.0;                     // Raw confidence score; higher is better
    double normalizedConfidence = 0.0;      // 0.0–1.0 via sigmoid on score gap to runner-up
};
```

All 21 modes are active. `normalizedConfidence` is computed via sigmoid on the score
gap between rank-1 and rank-2 candidates (midpoint 2.0, steepness 1.5). The chord
staff uses this to annotate uncertain detections with "?" or "(?)".

#### Tunable Parameters — `KeyModeAnalyzerPreferences`

All scoring weights and thresholds are collected in `KeyModeAnalyzerPreferences`.
See `keymodeanalyzer.h` for the full struct with documentation. Key groups:

- **Note weight caps** — `noteWeightCap`, `bassMultiplier`
- **Scale membership** — four case weights (`scaleScoreInBoth`, etc.)
- **Tonal centre** — per-tone weights and bonus/penalty for complete triad
- **Characteristic pitch** — `characteristicPitchBoost`, `characteristicPitchPenalty`
- **True leading tone** — `trueLeadingToneBoost`
- **Mode priors** — `modePriorIonian` through `modePriorAlteredDomBB7` (21 independent
  priors); populated from user preferences via `IComposingAnalysisConfiguration::modePrior*()`
  in the bridge; replaces former 4-tier grouping
- **Tonal-centre comparison** — independent weights for the same-key-signature
  family decision (`tonalCenter*`); diatonic family selection also applies a
  raw-score guard before tonal-centre can overturn the current raw winner
- **Key-signature proximity** — `keySignatureDistancePenalty`
- **Disambiguation** — `disambiguationTriadBonus`, `disambiguationTriadCost`,
  `disambiguationTonicBonus`
- **Confidence sigmoid** — `confidenceSigmoidMidpoint`, `confidenceSigmoidSteepness`
- **Beat-type weights** — `beatWeightDownbeat` through `beatWeightSubbeat`

#### Public Interface

```cpp
class KeyModeAnalyzer {
public:
    static std::vector<KeyModeAnalysisResult> analyzeKeyMode(
        const std::vector<PitchContext>& pitches,
        int keySignatureFifths,
        const KeyModeAnalyzerPreferences& prefs = kDefaultKeyModeAnalyzerPreferences
    );
};
```

#### §4.1c Part 2 — Jazz Mode (chord-symbol-driven boundaries)

**Status: Retired** — production analysis paths in commit 02e3733afb, tool-side surfaces in 69716deead. Chord symbols are no longer read by any analysis or tool path. See §4.1f for the future per-symbol trust-mode design.

**2026-04-08 follow-up:** Temporary jazz-specific scoring experiments were evaluated
and then reverted. `ChordTemporalContext::jazzMode` is retained only as a context
flag for chord-symbol-driven analysis paths and future diagnostics; no accepted
jazz-only scoring adjustments remain in the analyzer.

##### Jazz validation findings (2026-04-08)

A synthetic bass injection experiment confirmed that the vertical analyzer identifies
jazz chords correctly at near-perfect rates when given complete tonal material.

Experiment: `batch_analyze --inject-written-root` adds a synthetic bass tone at the
written chord symbol root before calling `analyzeChord()`. This simulates the bass
player's root note that is present in performance but absent from lead-sheet and
horn-section scores.

Results:

- Rampageswing (horn-only): 39.8% → 98.3%
- Omnibook (melody-only): 18.0% → 99.9%

Conclusion: the 40–60% agreement gap on available jazz corpora is explained by
missing bass/root material in the scores, not by a scoring-model deficiency. The
vertical analyzer requires complete tonal material (bass + harmony voices) to identify
chords reliably.

Jazz validation therefore requires scores with written-out bass and piano voicings.
Lead sheets, horn arrangements, and solo transcriptions are incomplete for this
purpose and should not be treated as analyzer accuracy benchmarks.

The `--inject-written-root` flag in `batch_analyze` provides a diagnostic upper bound.
It is not a production path: chord symbols must never be used as analyzer input in
production because they are user content and may be incorrect.

**The ban is decided by WHAT AN ANNOTATION SAYS, not by how the score stores it.** No harmonic
annotation already written in a score may be read as analyzer input — not a chord symbol, not a
Roman numeral, not a function, cadence or key label — whatever kind of score object happens to
carry it. Ordinary notational metadata that states no harmonic reading, the key signature among
it, remains admissible. *Why:* **derivation not recorded** — the record states the
generalization without giving the reason for widening it. It sharpens the chord-symbol ban above
from one annotation kind to a content test over all of them, and it is what makes that ban
proof against a rewording: an analysis of ours cannot be laundered back in as evidence by being
stored in a different element type. The record states neither a date nor a ratifier.

Known gap: no freely available corpus of jazz scores with complete written-out bass
and piano voicings has yet been found. This is an open corpus-availability problem,
not an analyzer design problem.

**The standing consequence: jazz accuracy is NOT MEASURABLE on the corpora we hold, and no
jazz-specific scoring work is planned on them.** The low agreement on the jazz material in the
project is a property of the material — melody-and-chord-symbol transcriptions with the bass and
the piano chords left out — not of the scoring model. No accepted jazz-specific scoring change
remains in the analyzer, and none is planned until scores carrying the missing parts are
available. *Why:* measured, by the bass-injection experiment above — supplying the missing root
before analysis moved one jazz corpus from 39.8 % to 98.3 % and another from 18.0 % to 99.9 %,
which is what identifies the shortfall as absent material rather than mis-scoring. Decided
2026-04-08; the record does not name the ratifier. This is the standing evidence behind
`OPEN_ITEMS.md` OI-7 (establish a jazz ground-truth corpus or de-scope the Jazz correctness
claims) and behind the empirically-unvalidated mark the verifiability contract (§2.15) requires
in exactly this situation.

##### Original problem statement (historical record)

The Jazz mode was motivated by three structural claims about note-based analysis of
jazz scores:

1. Jazz scores already contain explicit harmonic annotations — the written chord symbols
   (e.g. `Dm7`, `G7`, `CMaj7`) are useful boundary hints and comparison metadata.
   They are not the analysis result. Inferring region boundaries from pitch-class
   Jaccard distance is often redundant and error-prone when explicit chord-symbol
   boundaries are already present.
2. Jazz harmony uses voicings where the written root is frequently absent from the
   sounding notes (shell voicings: root + 3rd + 7th only; rootless voicings). The
   vertical note-set approach systematically misidentifies these.
3. Monophonic melodic lines (saxophone, bass) cannot produce the 3 simultaneous pitch
   classes required by the current 3-PC minimum.

##### Retirement rationale

- **Reason 1 (redundancy)** was a value judgment, not structural. Jaccard boundaries
  can still be computed; the question is whether symbol-boundary output is *better*
  than note-boundary output, not whether it is *possible*.
- **Reason 2 (rootless voicings)** concerned identity, not boundaries, so it does not
  justify symbol-driven boundaries. The vertical analyzer's identity problem on
  rootless voicings exists regardless of how regions are delimited.
- **Reason 3 (monophonic / sparse voicings)** was load-bearing only if identity
  inference from sparse notes also succeeded — it does not. Boundaries without usable
  identity produce symbol-echoed output, not analysis.
- **Core principle:** chord symbols are user-written instructions, not analysis
  results. Analyzer output is a pure function of notes + key signature + preferences.
- **Tool-side retirement** (`analyzeScoreJazz`, `--inject-written-root`, `jazzMode`
  flag) completed the principle — tools may read symbols only to compare against
  analyzer output produced from notes.

### §4.1f — Future: Authoritative Chord Symbol Mode

**Status:** Designed, not implemented. No current timeline.

#### Motivation

Chord symbols, Roman numerals, and Nashville numbers already present in a score may
carry different levels of authority depending on context:

- **As-is analysis:** The current analyzer reads notes and infers what chord they
  imply. Written chord symbols are comparison metadata only.
- **To-be annotation:** A composer or arranger may enter chord symbols representing
  the intended harmony, which the written notes may only partially realize (e.g. a
  lead sheet where the pianist improvises the voicing, or an arrangement where the
  bass is tacet).

In the to-be case, the written chord symbol is the ground truth — not the notes.
The analyzer's job shifts from "identify what the notes imply" to "confirm or
annotate what the composer declared."

#### Design

**Per-symbol trust, not per-score preference.** A per-score toggle is explicitly
rejected — too coarse-grained, since a single score may contain both trusted
lead-sheet-style annotations and untrusted draft symbols.

**Storage:** A boolean `trusted` property on the `Harmony` engraving element,
stored as a new MSCX attribute. Default `false`. Survives save/load roundtrip.

**UX:** A context-menu action "Mark symbol as authoritative" toggles the `trusted`
flag on selected `Harmony` elements. Trusted symbols receive a distinct visual cue
(color or small icon) to make authority status visible in the score editor.

**Analyzer semantics:** Only when a `Harmony` element has `trusted = true` does it
become boundary AND identity input for the harmonic region it opens. The analyzed
root and quality are taken from the written symbol, not from note-based inference.
Untrusted symbols remain comparison metadata only and are never read by the analysis
pipeline.

#### Diagnostic evidence

The synthetic bass injection experiment (2026-04-08) demonstrated that treating
written roots as authoritative (injecting the written root as a synthetic bass tone)
raises Rampageswing agreement from 39.8% to 98.3% and Omnibook from 18.0% to 99.9%.
This confirms the authoritative mode would be highly effective when the written chord
symbols are correct — and shows the risk when they are not. The injection tool
(`--inject-written-root`) was retired in 69716deead; the experiment data stands as
calibration evidence.

#### §4.1d Monophonic Chord Inference — Provisional Phased Plan

**Status:** provisional design note, updated after Phase 1a validation.
Phase 1a validation completed 2026-04-07, git `0587ec27e1`, on the Charlie
Parker Omnibook (50 public LORIA MusicXML solos with embedded chord symbols).
Result: **4454/4454 comparable regions = 100.0% root agreement**.

This validates the existing §4.1c chord-symbol-driven path, not independent
monophonic inference. In Phase 1a the written root is read directly from the
embedded chord symbols, not inferred from melody notes. The result confirms:
- chord-symbol boundaries are detected correctly in all 50 solos
- `Harmony` elements are parsed correctly from the MusicXML files
- jazz mode fires reliably on monophonic saxophone scores

Critical Phase 1a finding from the `noteCount` distribution:
- `noteCount = 0`: 1581 regions (35.4%)
- `noteCount = 1`: 2873 regions (64.4%)
- `noteCount >= 2`: 0 regions

Implication for Phase 1b: saxophone solos in this validation set provide at
most one sounded note per chord-symbol region. Independent chord inference from
isolated single-note regions is therefore not viable. Phase 1b must use bounded
group expansion across multiple consecutive regions, rather than attempting to
resolve chords from one-note local windows. This makes the bounded-expansion
design necessary, not optional.

The remaining monophonic problem is now narrowed to inference without chord
symbols: e.g. C.P.E. Bach keyboard, Bach suites, and arpeggiated piano or other
thin-texture repertories.

**End-state architecture:**
Monophonic and arpeggiated chord inference should use a separate internal engine
from the current vertical chord analyzer, but both should be hidden behind one
unified orchestration layer.

This separation is necessary because the two engines use different evidence
models:
- the vertical engine reasons from simultaneous pitch-class evidence, bass-root
  relations, and sonority-template matching
- the monophonic engine must reason from temporal accumulation, structural-note
  weighting, subset matching, and implied rather than explicit simultaneity

The unified orchestration layer should expose one harmonic-analysis entry point
to the rest of the system. Status-bar analysis, chord-staff population, tuning,
and validation tooling should not need to know which internal engine produced
the result.

**Shared context:**
Key/mode inference remains shared. The existing key/mode analyzer already
provides a broader temporal prior than chord identity and should be reused by
both vertical and monophonic chord inference. A separate monophonic mode
analyzer is not planned for the initial implementation.

**Score metadata:**
Fields such as `fromChordSymbol` and `writtenRootPc` are score metadata rather
than engine metadata. The unified orchestration layer must preserve them
regardless of which analysis engine produced the winning harmonic result.

### Phase 1a — Validate Existing Chord-Symbol-Driven Path

Phase 1a is now complete.

Corpus: Charlie Parker Omnibook (50 solos, public LORIA MusicXML).

Run result:
- 50/50 files loaded successfully
- 4464 total regions
- 3361 comparable `fromChordSymbol` regions with an analyzed chord
- 605/3361 written-root vs analyzed-root agreement = **18.0%**
- 1103 `fromChordSymbol` regions produced no analyzed chord (`hasAnalyzedChord=false`)
- 0 zero-region solos

Interpretation:
- the previous 100% Omnibook result was invalid because the old jazz path copied
  the written chord-symbol root into the analysis result
- with the corrected non-circular path, the current vertical chord analyzer does
  **not** solve the annotated monophonic jazz case, even when the written chord
  symbols supply exact region boundaries
- this run validates `Harmony` parsing and regionization, but it falsifies the
  assumption that boundary-correct regional accumulation is enough on its own

The corrected Phase 1a note-count evidence is:
- all `fromChordSymbol` regions: `0: 268`, `1: 349`, `2: 476`, `3: 691`, `4: 1088`,
  `5: 610`, `6: 496`, `7: 341`, `8: 110`, `9: 25`, `10: 5`, `11: 5`
- 1103 regions (24.7%) remain unanalyzable by the current vertical analyzer
  because they produce fewer than 3 distinct pitch classes
- the comparable subset is not especially sparse: most analyzable regions contain
  3-6 distinct pitch classes, yet agreement is still only 18.0%

The dominant mismatch pattern is functional reinterpretation rather than total
absence of evidence: written `F` is often analyzed as `C`, `Am`, or `Gm`; written
`Bb` as `F`, `Gm`, `Dm`, or `C`; written `C` as `G` or `Am`.

Therefore the next monophonic step cannot be framed merely as bounded expansion
to overcome 0-1 note sparsity. The current vertical analyzer's evidence model is
itself a poor fit for monophonic jazz melody, even when region boundaries are
supplied correctly. Bounded expansion may still help the 1103 sparse regions, but
it is not sufficient to explain or solve the remaining disagreement.

### Phase 1b — Minimal Monophonic Fallback Without Chord Symbols

If Phase 1a shows that annotated monophonic material is largely handled, the
next step is a minimal monophonic fallback for unannotated single-line or
arpeggiated passages.

This phase should remain intentionally modest:
- simple boundary sources first
- subset-based chord matching rather than full simultaneity requirements
- bounded local-context expansion only when confidence is weak
- lightweight smoothing heuristics rather than full sequence decoding

**Boundary-source selection in Phase 1b:**
Boundary choice should be repertoire- and texture-aware rather than globally
ordered.

Use:
1. written chord symbols when present
2. fine-grained Jaccard-style harmonic-boundary detection for faster harmonic
   rhythm or classical material
3. beat- or bar-quantized boundaries only as a simpler fallback for slower
   harmonic-rhythm contexts

Bar-quantized boundaries are intentionally not the default fallback for
classical keyboard material, where within-bar harmony changes are common.

**Subset-based matching in Phase 1b:**
Phase 1b does not require three simultaneous pitch classes, but it also must not
treat arbitrary one-note fragments as sufficient chord evidence.

Initial rule:
- 2 distinct pitch classes may nominate a candidate set
- 2-PC evidence alone must not finalize a chord without contextual support
- 1-PC evidence is insufficient for independent chord resolution and may only
  participate in continuity-preserving abstention logic

This keeps Phase 1b permissive enough to analyze broken-chord passages while
avoiding over-interpretation of isolated tones.

**Bounded expansion in Phase 1b:**
Chord identity should remain local. When a local group is too weak to resolve,
the analyzer may expand by one neighboring region and re-score. Expansion is
bounded and should stop when:
- confidence crosses threshold
- top-vs-second margin crosses threshold
- the same winner survives repeated expansion
- the hard expansion cap is reached

**Lightweight smoothing in Phase 1b:**
Phase 1b should not implement full dynamic-programming or Viterbi decoding.
Instead, it should use a simple continuity heuristic.

Example intent:
if the same chord wins strongly in adjacent groups, do not let one weak middle
group overturn it unless the competing candidate wins by a substantial margin.

These terms must be implemented as tunable parameters rather than prose-only
rules.

**Initial Phase 1b calibration parameters:**
- `monoMinSubsetDistinctPcs` — initial default: 2
- `monoWeakGroupConfidenceMax` — upper bound below which a local group is
  treated as weak
- `monoAdjacentAgreementMinConfidence` — minimum confidence required for the
  neighboring groups to count as strong agreement
- `monoWeakGroupOverrideMargin` — minimum margin required for a weak middle
  group to overturn adjacent agreement
- `monoExpansionMaxGroups` — hard cap on neighboring-group expansion

As with other analyzer parameters, these should follow the existing
preferences-and-`bounds()` pattern and remain explicitly calibratable.

### Phase 2 — Full Monophonic Engine

The full monophonic engine is still the intended long-term design, but it
should follow Phase 1 validation rather than precede it.

The full engine should add:
- dedicated harmonic grouping from melodic structure
- boundary scoring from duration, metric stress, rests, leaps, register shifts,
  and pitch-class novelty
- chord inference from weighted subsets rather than vertical simultaneity
- sequence-level smoothing across neighboring groups
- compound-melody handling for implied multiple voices in one line
- explicit confidence calibration against the vertical engine

The local grouping problem is intentionally deferred to Phase 2 because it is
the hardest part of monophonic inference.

### Unified Orchestration Layer

The outer harmonic-analysis pipeline remains unified and selects among internal
strategies.

The orchestration layer should:
1. gather texture facts for the requested span
2. resolve shared key/mode prior
3. run vertical analysis on the full texture where appropriate
4. run monophonic analysis on individual staves or voices where appropriate
5. compare calibrated confidence rather than raw internal scores
6. return one ranked harmonic result list
7. abstain when neither engine is sufficiently reliable

**Mixed texture — explicit Phase 2 open question:**
The most common unresolved orchestration problem is staff-level or voice-level
mixed texture. A single passage may contain vertical evidence on one staff and
arpeggiated or single-line evidence on another. The orchestrator must therefore
eventually decide which staves or voices receive which analysis treatment.

This is not required for Phase 1, but it is an explicit Phase 2 design question
and should not be treated as solved by piece-level texture classification.

### Confidence and Abstention

The unified layer must not compare vertical and monophonic raw scores directly.
The two engines use different evidence models and therefore require explicit
confidence calibration.

This remains an open design problem. Acceptable solutions include:
- held-out corpus-based calibration
- normalized confidence derived from score margin, coverage, and texture facts
- a combination of both

Abstention is a first-class outcome. It is preferable to emit no chord result
than to emit a low-confidence result that later drives annotation or tuning
incorrectly.

### Interaction with Existing Temporal Context

The monophonic path should reuse the same broad contextual ideas already used by
the vertical path:
- harmonic continuation
- local stability versus change
- cadence-like expectation
- key/mode compatibility
- continuity bonuses where musically justified

This does not imply identical scoring formulas, but it does mean both engines
should live inside one coherent harmonic-analysis framework rather than evolve
as unrelated systems.

### Implementation Priority

**Immediate priority:**
Run Phase 1a validation on annotated monophonic jazz material and let the corpus
results determine whether a dedicated Phase 1b fallback is necessary.

**Next priority:**
If Phase 1a leaves clear failures on unannotated single-line passages, implement
a minimal Phase 1b monophonic fallback with explicit thresholds and bounded
behavior.

**Later priority:**
Implement the full monophonic engine for non-annotated and compound-melody
repertoires.

This ordering is intentional: it targets the fastest corpus-quality gains first
while preserving the correct long-term architecture.

#### Known limitation — dominant seventh / Mixolydian ambiguity

A dominant seventh chord (major triad + minor seventh) is the characteristic chord of
Mixolydian mode. When such a chord appears in isolation or without sufficient surrounding
diatonic context, the key analyzer may briefly declare Mixolydian even in a major-key
passage. This produces false-positive Mixolydian detections (observed in Grieg corpus
validation 2026-04-06: 32 cases / ~7% of disagreements).

This is **not a prior calibration problem**. Adjusting the Mixolydian prior would either
suppress genuine Mixolydian detection (lower prior) or increase false positives (higher
prior). The correct fix is requiring more sustained evidence of the lowered 7th scale
degree before declaring Mixolydian — an evidence-threshold improvement in `KeyModeAnalyzer`
scoring, deferred to a future session.

The same structural ambiguity applies to the Lydian raised 4th (an augmented fourth
interval may appear briefly in major passages) but at much lower false-positive rates
(12 cases in Grieg vs 32 for Mixolydian) because the raised 4th is less common in
incidental voice leading than the dominant seventh.

**Validated correct behaviour:** Lydian detection in Chopin (4.2% of regions) and
Grieg (11.9%) reflects genuine raised-4th passages. Dorian detection (5.2% Grieg,
5.9% Chopin) similarly reflects real modal content. The Mixolydian false-positive
rate (7%) is a known, bounded limitation — not evidence of a miscalibrated prior.

### 4.3 ChordSymbolFormatter

**Files:** declared in `src/composing/analysis/chord/chordanalyzer.h` (namespace within);
implemented in `src/composing/analysis/chord/chordsymbolformatter.cpp`. (Corrected 2026-08-02,
`OPEN_ITEMS.md` OI-112(a): the single "File:" line predated refactor-1, which split the
IMPLEMENTATION into its own translation unit while INTENTIONALLY keeping the declarations in
`chordanalyzer.h` — there is no `chordsymbolformatter.h`. The backlog item in §4.1i that proposes
creating one is annotated there.)

**Purpose:** Formats `ChordAnalysisResult` into display strings. Kept separate from
`ChordAnalyzer` so the analysis layer remains display-agnostic. This separation must
be maintained throughout the codebase — analysis produces data, formatters produce strings.

```cpp
namespace ChordSymbolFormatter {

    // Note spelling convention for chord symbol root and bass names.
    // Mirrors NoteSpellingType in src/engraving/types/types.h.
    enum class NoteSpelling { Standard, German, GermanPure };

    // Display options — locale/notation-style concerns kept separate from analysis.
    struct Options {
        NoteSpelling spelling = NoteSpelling::Standard;
    };
    inline constexpr Options kDefaultOptions{};

    // "Cmaj7", "Fm7/Ab", "Bdim7" etc.
    std::string formatSymbol(const ChordAnalysisResult& result, int keySignatureFifths,
                             const Options& opts = kDefaultOptions);

    // "IM7", "ii7", "V7/3", "viiø7" etc.
    // Non-diatonic roots generate chromatic numerals: "♭VII", "♭III7", "♭VIM7" etc.
    // Returns "" only when the root cannot be mapped at all (should not occur in
    // standard 12-tone music).  The result stores keyTonicPc and keyMode so no
    // extra parameters are needed.
    std::string formatRomanNumeral(const ChordAnalysisResult& result);
}
```

Display options (`Options`) live in `ChordSymbolFormatter`, not in
`ChordAnalyzerPreferences`, enforcing the analysis/display separation (principle 2.3).

**Note naming convention:** Root and bass note names in chord symbol output
respect the score's chord symbol spelling preference (Format → Style → Chord
Symbols). The analysis layer implements a self-contained `NoteSpelling` enum
`{Standard, German, GermanPure}` — defined in `chordanalyzer.h`, mirroring
`NoteSpellingType` in `src/engraving/types/types.h`. The bridge reads
`Sid::chordSymbolSpelling` from the score style via `scoreNoteSpelling()`
(defined in `notationcomposingbridgehelpers.cpp`) and maps it to
`ChordSymbolFormatter::Options::spelling`. German mapping mirrors
`tpc2name()` GERMAN case (`pitchspelling.cpp:343-356`): B natural → "H",
Bb → "B". All other note names are unchanged. Solfeggio and French map to
Standard (not yet supported in chord symbol output). Roman numerals and
Nashville numbers do not use note names — they use degree integers and
accidental tokens — so the spelling setting does not affect them.

**Roman numeral scope (corrected 2026-08-02, `OPEN_ITEMS.md` OI-112(b) — this paragraph said
extensions beyond the 7th are "not yet emitted", which the corpus contradicts):** the formatter
emits Roman numerals at the 7th level (e.g. `I7`, `IM7`, `iø7`) **and above** — `csfDiatonicRoman`
appends `b9`/`#9`/`#11`/`b13` alterations when a seventh is present, and the `(add9)` / `(add11)` /
`(add13)` forms when none is (`chordsymbolformatter.cpp:590-616`); the corpus counts are in the
OI-112 row. Non-diatonic roots produce chromatic numerals by computing semitone
distance from the mode tonic and prefixing with ♭ or ♯ as appropriate (preferring
flat names). The quality/extension suffix is reused from the diatonic path. The
test catalog covers the 7th level only; extending it is a natural future increment.

#### Planned Trajectory — IChordSymbolFormatter

`ChordSymbolFormatter` will eventually become a substitutable interface, orthogonal
to `IChordAnalyzer` (Section 14.1). The two axes vary independently:

```
IChordAnalyzer          IChordSymbolFormatter
      ↓                         ↓
ChordAnalysisResult  →  formatted string
```

**Planned substitution points for IChordSymbolFormatter:**

- *Notation convention:* lead sheet ("Cmaj7"), Nashville ("1maj7"), Roman numeral
  ("IM7"), figured bass (for baroque contexts — see note below)
- *Spelling conventions:* American ("maj7", "m7b5"), German/Nordic (H/B naming),
  Berklee/jazz ("Δ7", "ø7"), classical (augmented sixth notation)
- *Symbol vocabulary:* half-diminished ø vs "m7b5" vs "ø7"; major seventh Δ vs
  "maj7" vs "M7"; augmented "+" vs "aug"

When `IChordSymbolFormatter` is introduced, `ChordSymbolFormatter::Options` becomes
its configuration struct — the migration path is already established.

#### Note on figured bass

Figured bass (basso continuo) is interval notation above a bass note rather than a
chord name — e.g. "6" = first inversion triad, "6/4" = second inversion, "7" = root
position seventh.  It is architecturally simpler than chord symbols in one critical
respect: **it requires no root detection**.  The algorithm is:

1. Identify the bass note (lowest sounding pitch — already `ChordAnalysisTone::isBass`).
2. Compute each upper tone's interval above the bass, reduced to within one octave.
3. Convert to diatonic scale degrees using TPC spelling and `keySignatureFifths`.
4. Apply the standard omission table (root position triad → nothing; first inversion →
   "6"; second inversion → "6/4"; root position seventh → "7"; etc.).
5. Prefix accidentals (♭ ♯ ♮) where a tone deviates from the key signature.

This can be derived directly from the raw `ChordAnalysisTone` input — `ChordAnalysisResult`
is not required.  Importantly, figured bass annotates *all* sounding pitches including
suspensions and passing tones, which is actually easier than chord symbol analysis (no
need to distinguish chord tones from non-chord tones).  The only tricky parts are the
omission convention table and enharmonically-correct accidental spelling, both of which
are straightforward given TPC data and `keySignatureFifths`.

Figured bass generation is feasible with the current analysis infrastructure and would
work even for sonorities with fewer than 3 distinct pitch classes (where chord symbol
analysis returns empty).  It is not currently planned but is noted here because the
prerequisite data is already present.

### 4.3a Voicing Helpers

**File:** `src/composing/analysis/chordanalyzer.h` (declared) and `chordanalyzer.cpp`
(defined)

Two helpers support chord track population (§11.5):

```cpp
struct ClosePositionVoicing {
    int bassPitch = -1;              // Root MIDI pitch in C2–C3 range (-1 = empty)
    std::vector<int> treblePitches;  // Upper chord tones in C4–C5 close position
};

ClosePositionVoicing closePositionVoicing(const ChordAnalysisResult& result);
std::vector<int> chordTonePitchClasses(const ChordAnalysisResult& result);
```

`closePositionVoicing()` produces a keyboard-reduction voicing: root in bass
register (C2–C3), remaining chord tones stacked ascending above C4 within one
octave.  Returns empty voicing for `ChordQuality::Unknown`.

`chordTonePitchClasses()` derives the canonical pitch-class set from an analysis
result — root first, then remaining tones ascending.  Reflects the idealized chord
(quality + extensions), not a transcription of what was sounding.  Used when the
chord track is set to show canonical tones rather than collected sounding tones.

### 4.3b HarmonicRhythm

**Files:**
- `src/composing/analysis/region/harmonicrhythm.h` — `HarmonicRegion` struct (pure composing type, no engraving dependency)
- `src/notation/internal/notationharmonicrhythmbridge.h/.cpp` — `analyzeHarmonicRhythm()` declaration and definition
- `src/notation/internal/notationcomposingbridgehelpers.h/.cpp` — shared bridge helpers used by both bridges
- `src/notation/internal/notationimplodebridge.h/.cpp` — `populateChordTrack()` declaration and definition

The `HarmonicRegion` struct lives in the composing module (no engraving include needed); the functions that consume `Score*` / `Fraction` are bridge functions in `mu::notation`:

```cpp
// composing/analysis/harmonicrhythm.h
namespace mu::composing::analysis {
struct HarmonicRegion {
    int startTick = 0;                    // Raw tick integer (first tick of region)
    int endTick = 0;                      // First tick of next region (exclusive)
    ChordAnalysisResult chordResult;      // Root, quality, extensions, degree
    KeyModeAnalysisResult keyModeResult;  // Key and mode context
    std::vector<ChordAnalysisTone> tones; // Sounding tones that produced the analysis
};
} // namespace mu::composing::analysis

// notation/internal/notationcomposingbridge.h
namespace mu::notation {
std::vector<mu::composing::analysis::HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves = {});
} // namespace mu::notation

// notation/internal/notationimplodebridge.h
namespace mu::notation {
bool populateChordTrack(
    mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones = false);
} // namespace mu::notation
```

`analyzeHarmonicRhythm()` scans all eligible staves, detects harmonic boundaries
(ticks where the sounding pitch-class set changes), and runs chord analysis at each
boundary. In its default smoothed mode it collapses consecutive same-chord regions and
absorbs short regions; callers may instead request `HarmonicRegionGranularity::PreserveAllChanges`
when every detected harmonic event must survive into output (the chord-staff populate
path now does this). Declared and defined in `mu::notation` (bridge pattern — requires
engraving types `Score*`, `Fraction`).

`populateChordTrack()` clears the target grand-staff region and writes a harmonic
reduction with the following layout:

Before writing notes, the populate path normalizes measure-local gaps between analyzed
regions: if sparse spans inside a measure produced no chord result, the first and last
written region in that measure are extended to the measure boundaries and any internal
gap is absorbed into the preceding written region. This keeps the chord track from
serializing mixed chord/rest measures when the analyzer intentionally skips thin-texture
subspans.

| Position | Content |
|----------|---------|
| Above first stave | Key/mode label (e.g. "C maj", "D Dor?") only when key confidence is at least 0.5; confidence 0.5–0.8 appends "?" |
| Below first stave | Key relationship annotation (e.g. "(→ relative min)", "(→ dominant key)") only on assertive key changes (confidence at least 0.8) |
| Above second stave | Borrowed chord star ★ + source key (e.g. "Bb min") when a non-diatonic chord has an identifiable diatonic source, plus pivot label (e.g. "pivot: IV → I in G maj") at modulation boundaries and cadence marker (PAC, HC, DC, PC); these are written only when key confidence is at least 0.8 |
| Below second stave | Roman numeral (e.g. "IM7", "V7") only when key confidence is at least 0.5 |
| Treble stave notes | Upper chord tones (canonical or collected) |
| Bass stave notes | Root |
| Above treble stave | Chord symbol (e.g. "Cmaj7", "F#m7/A") |

**Borrowed chord rule:** The star ★ and source key are written only when a source
key is found (chord tones all diatonic to some other key within ±7 fifths). Purely
chromatic chords that fit no diatonic scale receive no marker.

The `useCollectedTones` flag controls whether the treble staff uses the original
sounding tones (preserving voicing color) or canonical chord tones.

Tick values in `HarmonicRegion` are raw integers rather than `Fraction` objects,
keeping the header free of the engraving module's `Fraction` include and
preserving `composing_analysis`'s module independence.

### 4.4 AnalysisUtils

**File:** `src/composing/analysis/chord/analysisutils.h` (path and contents corrected 2026-08-02,
`OPEN_ITEMS.md` OI-107(c): the path was given without the `chord/` component and three functions
were missing.)

Shared utilities used by both analyzers and the formatter — the dependency-free pitch leaf, exempt
from the inference/presentation include guard:

- `normalizePc(int pitch)` — reduces any MIDI pitch to pitch class 0–11
- `ionianTonicPcFromFifths(int fifths)` — converts circle-of-fifths position to
  the pitch class of the Ionian (major) tonic for that key signature
- `endsWith(const std::string&, const char*)` — generic string suffix test
- `diatonicMaskFromFifths(int fifths)` — the 12-bit mask of the pitch classes the key
  signature's own collection contains (no tonic, no mode scale — see the OI-168 correction)
- `collectionMask(int tonicPc, bool isMajor)` — the 12-bit mask of a major or minor collection
  rooted at `tonicPc`
- `pcInMask(uint16_t mask, int pc)` — membership test against either mask

### 4.5 Current Status Bar Integration

**Files:**
- `src/notation/internal/notationaccessibility.cpp` — entry point; calls `harmonicAnnotation()`
- `src/notation/internal/notationcomposingbridge.cpp` — `harmonicAnnotation()` bridge function

The analysis is invoked from `NotationAccessibility::singleElementAccessibilityInfo()`.
This method triggers on every selection change and calls `mu::notation::harmonicAnnotation(note)`
(defined in `notationcomposingbridge.cpp`), which runs `analyzeNoteHarmonicContext()` and formats
the result for display in the status bar.

#### Score Traversal Pattern

This is the established pattern for collecting notes at a tick. All future components
that need to collect notes at a specific moment should follow this pattern:

```cpp
// 1. Find the ChordRest segment at the target tick
const Segment* seg = sc->tick2segment(tick, true, SegmentType::ChordRest);

// 2. Iterate all staves and voices — collect from every voice simultaneously
for (size_t si = 0; si < sc->nstaves(); ++si) {
    for (int v = 0; v < VOICES; ++v) {
        const ChordRest* cr = seg->cr(static_cast<track_idx_t>(si) * VOICES + v);

        // Grace notes are ornamental, not harmonic — always exclude from analysis
        if (!cr || !cr->isChord() || cr->isGrace()) {
            continue;
        }

        for (const Note* n : toChord(cr)->notes()) {
            // Use ppitch() not pitch() — honours ottavas and transposing instruments
            // Use tpc() for enharmonic spelling information
        }
    }
}
```

#### Key Decision Logic

The key/mode inferrer always runs. The notated key signature provides `keySignatureFifths`
as a scoring prior — it biases the inferrer toward nearby keys without overriding note
evidence. The `KeyMode` enum from the key signature is used only as a fallback when pitch
context is genuinely insufficient (fewer than 3 distinct pitch classes). See §5.2 for the
full revised priority logic.

#### Temporal Window for Key/Mode Analysis

16-beat lookback + 8-beat lookahead, with exponential time decay (0.7× per measure).
Dynamic expansion to 24 beats when confidence is below 0.60. Mode-switching hysteresis
prevents spurious mode switches on transient evidence. All `PitchContext` fields
(`durationWeight`, `beatWeight`, `isBass`) are fully populated.

#### Current Status Bar Output Format

```
[Note name]; [bar and beat]; Staff N (Part name); [C maj] Cmaj7 (IM7)
```

Chord symbol, key/mode, and Roman numeral are all appended.

### 4.6 User Preferences — Configuration Interface Split

**Files:**
- `src/composing/icomposinganalysisconfiguration.h` — IoC-registered interface for analysis settings
- `src/composing/icomposingchordstaffconfiguration.h` — IoC-registered interface for chord-staff output settings
- `src/composing/icomposingconfiguration.h` — non-IoC aggregate base (inherits both above; not registered)
- `src/composing/composingconfiguration.h/.cpp` — concrete implementation (registered under both sub-interfaces)
- `src/preferences/qml/MuseScore/Preferences/ComposingPreferencesPage.qml` — preferences UI

The configuration is split into two separately-registered IoC interfaces:

| Interface | Registered? | Inject when... |
|-----------|-------------|----------------|
| `IComposingAnalysisConfiguration` | Yes | Code needs analysis toggles, status-bar flags, mode tier weights |
| `IComposingChordStaffConfiguration` | Yes | Code needs chord-staff output preferences |
| `IComposingConfiguration` | **No** | Not used for injection; plain C++ base uniting both |

`IComposingConfiguration` is **not** registered because `MODULE_GLOBAL_INTERFACE` injects a
`modularity_interfaceInfo` static member, and multiple inheritance would make that member ambiguous.
`ComposingConfiguration` inherits from both sub-interfaces (and therefore from `IComposingConfiguration`
transitively) and is registered under each sub-interface separately.

Callers inject the narrowest interface they need.  The bridge functions in
`notationcomposingbridge.cpp`, `notationtuningbridge.cpp`, and `notationimplodebridge.cpp`
inject `IComposingAnalysisConfiguration` via `muse::GlobalInject`.

The UI is a dedicated preferences page under Edit → Preferences → Composing.

The preferences are organised into three sections: Analysis, Status bar, and Chord staff.

**Analysis section:**
- `analyzeForChordSymbols` (bool, default true) — pitch-structure analysis only;
  does not require key/mode inference
- `analyzeForChordFunction` (bool, default false) — key/mode-aware degree analysis;
  single toggle that feeds both Roman-numeral and Nashville-number display.
  Replaces the former separate `analyzeForRomanNumerals` / `analyzeForNashvilleNumbers`
  toggles.  Roman numerals and Nashville numbers are **presentation choices**, not
  separate analyses — they are alternative formatters on the same `ChordAnalysisResult`.
- `inferKeyMode` (bool, forced on when `analyzeForChordFunction` is active)
- `analysisAlternatives` (int 1–3, default 3) — single universal count applied to
  both the status bar and the context menu (replaces former per-type counts)

**Intonation section** (grouped under a labelled heading in the UI):
- `tuningSystemKey` (string, default "equal") — tuning system for "tune as" action
- `tonicAnchoredTuning` (bool, default true) — anchor each chord root to its JI
  scale-degree position above the mode tonic (§11.2a)
- `tuningMode` (int, default 0 = TonicAnchored) — high-level drift behavior:
  0 = Tonic-anchored (current behavior), 1 = Free drift (see §11.3f)
- `allowSplitSlurOfSustainedEvents` (bool, default true) — allows region retuning
  to rewrite sustained events into independent playback events when a continuation
  needs different tuning; applies to both single sustained notes and tied chains at
  existing tie boundaries in both TonicAnchored and FreeDrift, but anchors still
  protect the full written duration
- `minimizeTuningDeviation` (bool, default false) — subtract the mean offset per
  chord so the chord hovers near 0¢ while preserving internal JI ratios
- `annotateTuningOffsets` (bool, default false) — add a staff text showing the cent
  offset of each tuned note (e.g. "+15 −2 +3") below the chord in the score
- `annotateDriftAtBoundaries` (bool, default false) — in Free drift mode, insert a
  StaffText above the first eligible staff at each harmonic region boundary showing
  the accumulated pitch drift, e.g. "d=+3" or "d=-2" (only emitted when
  |driftAdjustment| ≥ 0.5 ¢; independent of `annotateTuningOffsets`)

**Mode detection weights** (21 independent sliders, one per mode, range −5.0 to +5.0, step 0.5):

Diatonic family:
- `modePriorIonian` (default +1.20)
- `modePriorDorian` (default −0.50)
- `modePriorPhrygian` (default −1.50)
- `modePriorLydian` (default −1.50)
- `modePriorMixolydian` (default −0.50)
- `modePriorAeolian` (default +1.00)
- `modePriorLocrian` (default −3.00)

Melodic minor family:
- `modePriorMelodicMinor` (default −0.50)
- `modePriorDorianB2` (default −1.50)
- `modePriorLydianAugmented` (default −2.00)
- `modePriorLydianDominant` (default −1.00)
- `modePriorMixolydianB6` (default −1.50)
- `modePriorAeolianB5` (default −2.50)
- `modePriorAltered` (default −3.50)

Harmonic minor family:
- `modePriorHarmonicMinor` (default −0.30)
- `modePriorLocrianSharp6` (default −2.50)
- `modePriorIonianSharp5` (default −2.00)
- `modePriorDorianSharp4` (default −2.00)
- `modePriorPhrygianDominant` (default −0.80)
- `modePriorLydianSharp2` (default −2.50)
- `modePriorAlteredDomBB7` (default −3.50)

Five named presets populate all 21 sliders:

| Preset | Character |
|--------|-----------|
| Standard | Classical/baroque defaults as above |
| Jazz | LydianDominant=−0.20, Altered=−0.50, MelodicMinor=−0.50, DorianB2=−1.00, PhrygianDominant=−0.80, HarmonicMinor=−0.50; diatonic at standard weights |
| Modal | All 7 diatonic modes equal at 0.0; melodic and harmonic minor at high penalty |
| Baroque | HarmonicMinor=−0.20, PhrygianDominant=−0.50; all non-diatonic modes at maximum penalty |
| Contemporary | All 21 modes at moderate penalty; optimizer determines final weights from corpus |

Presets are represented by `ModePriorPreset` (a plain struct with 21 `double` fields and a
`std::string name`) declared in `icomposinganalysisconfiguration.h`.  The free function
`mu::composing::modePriorPresets()` returns `std::vector<ModePriorPreset>` with all five.
The interface exposes two extra methods:
- `applyModePriorPreset(const std::string& name)` — writes all 21 priors in one call
- `currentModePriorPreset() const` — returns the name of the active preset, or `""` when
  the current values do not match any preset (epsilon = 1e-6)

The QML preferences page exposes these via `ComposingPreferencesPage.qml` →
`ComposingAnalysisSection.qml` as five `FlatButton` widgets (`accentButton` when active);
the current preset name is tracked in `currentModePriorPreset` Q_PROPERTY.

The bridge reads these at analysis time and populates `KeyModeAnalyzerPreferences`
before calling `analyzeKeyMode()`. The former 4-tier grouping (`modeTierWeight1`–`modeTierWeight4`)
and the internal +0.2 Ionian offset are replaced by these 21 independent priors.

**Status bar section** (boolean checkboxes; each enabled only when its analysis is on):
- `showChordSymbolsInStatusBar` (bool, default true) — requires `analyzeForChordSymbols`
- `showRomanNumeralsInStatusBar` (bool, default false) — requires `analyzeForChordFunction`
- `showNashvilleNumbersInStatusBar` (bool, default false) — requires `analyzeForChordFunction`
- `showKeyModeInStatusBar` (bool, default true) — requires `inferKeyMode`

Status bar format: `Chord: Bmaj / II / 2 (0.65) | Cmin / iv / 4 (0.43) in key: C major`.
Parts within a candidate joined by ` / ` (only active formats included); candidates
separated by ` | `; key appended as ` in key: X` when shown.  When no chord results
are shown but key/mode is on: `key: C major` (no "in" prefix).

**Chord staff section** (controls what "Implode to chord staff" writes — planned):
- `chordStaffWriteChordSymbols` (bool, default true) — write `HarmonyType::STANDARD`
  annotations above the treble staff; requires `analyzeForChordSymbols`
- `chordStaffFunctionNotation` (enum: None / Roman numerals / Nashville numbers,
  default Roman numerals) — write either `HarmonyType::ROMAN` or
  `HarmonyType::NASHVILLE` below the treble staff; requires `analyzeForChordFunction`.
  Roman and Nashville are mutually exclusive here — they encode the same information
  and displaying both would clutter the staff with redundant text.
- `chordStaffWriteKeyAnnotations` (bool, default true) — write key/mode staff text at
  region boundaries; requires `inferKeyMode`

---

## 5. Planned Analysis Extensions

> *The per-feature "Implemented / Pending / Planned" tags in the §5 sub-headings are **status**, not design, and are
> kept here only for orientation; the **authoritative, current** implemented/planned state lives in STATUS.md. Where a
> heading's status and STATUS.md disagree, STATUS.md wins. This section describes the **designs**.*

### 5.1 Weight Population — Implemented for KeyModeAnalyzer, Pending for ChordAnalyzer

**KeyModeAnalyzer calling code** (in `NotationComposingBridge`) fully populates all
`PitchContext` fields: duration in quarter notes, beat-type weight from MuseScore's
`BeatType` enum, bass identification via two-pass per-segment scan, and exponential
time decay (0.7× per measure).

**ChordAnalyzer calling code** — `ChordAnalysisTone.weight` is still not populated
from duration or metric position. Populating it is a planned improvement that requires
no analyzer changes — only calling code changes.

### 5.2 Key/Mode Inference — Revised Priority and Expanded Temporal Window

**Notes Always Win — Implemented**

The key/mode inferrer always runs. The notated key signature's `KeyMode` enum
(`MAJOR`, `MINOR`, etc.) is no longer a bypass gate — it is passed as a weak hint
(`declaredMode`) to `analyzeKeyMode()` and influences the scoring prior but does not
skip the inferrer.

The only exception is a **piece-start shortcut** in `resolveKeyAndMode()`: when the
analysis tick is within the first 16 quarter-note beats (a separate constant from the 16-beat lookback window below —
they coincide in value, not by design), no prior result exists (`prevResult == nullptr`),
and the key signature carries an explicit mode, the function returns the declared mode
immediately (confidence 0.5) rather than waiting for pitch evidence that cannot yet exist.
This is a deliberate pragmatic choice for the score opening, not a general bypass.

Outside the piece-start shortcut, the priority of evidence is:

**Priority of evidence:**

| Priority | Source | Description |
|---|---|---|
| Strongest | Actual sounding notes | what is literally happening now |
| Strong | Temporal context | surrounding measures |
| Weak | Notated key signature | `keySignatureFifths` (circle of fifths position) |
| Weakest | `KeyMode` enum | explicit major/minor tag (rare, only when user sets it) |

**Implemented logic — `resolveKeyAndMode()` in `notationcomposingbridgehelpers.cpp`:**

The key signature's `keySignatureFifths` remains a scoring prior inside the inferrer
(`keySignatureScore` biases toward nearby keys without overriding note evidence).
The `declaredMode` from the key signature is passed to `analyzeKeyMode()` as an optional
hint — it shifts the prior weight for that mode but does not prevent other modes from
winning.

The inferrer output is used for all but two narrow fallback cases:
- **Piece-start shortcut:** tick < 16 beats, no prior result, explicit key-sig mode →
  return declared mode at confidence 0.5 (no pitch evidence to analyze yet)
- **Insufficient data:** `modeResults.empty() || distinctPitchClasses(ctx) < 3` →
  fall back to key signature enum (Aeolian for MINOR, Ionian for all other explicit or
  unknown modes)

The `KeyMode` enum (`MAJOR`, `MINOR`, `IONIAN`, `AEOLIAN` etc.) is only a factor in
these two fallback paths — when pitch data is genuinely insufficient.

**Expanded Temporal Window — Implemented**

The bridge uses a 16-beat lookback + 8-beat lookahead window:

```cpp
const int LOOKBACK_BEATS  = 16;  // ~4 measures in 4/4
const int LOOKAHEAD_BEATS =  8;  // ~2 measures ahead
```

Notes are weighted by `durationWeight × beatWeight × timeDecay`, where time decay
applies an exponential factor of 0.7× per measure of distance from the analysis tick.
Beat-type weights are mapped from MuseScore's `BeatType` enum (downbeat 1.0,
stressed 0.7, unstressed 0.4, subbeat 0.2).

**Normalized Confidence — Implemented**

`KeyModeAnalysisResult::normalizedConfidence` is 0.0–1.0 via sigmoid on the score
gap between rank-1 and rank-2 candidates. The chord staff uses this to add "?" or
"(?)" to key/mode labels when confidence is below 0.8 or 0.5 respectively.

### 5.3 TemporalContext — Full Specification

> *Naming: this spec's `TemporalContext` is realised in the as-built as **`ChordTemporalContext`** (the `analysistypes.h`
> cross-layer leaf, §3.3) — the same struct under its current name. Read `TemporalContext` below as `ChordTemporalContext`.*

`TemporalContext` is an optional parameter that will be added to `analyzeChord()`.
The analyzer functions correctly without it (current behavior). When provided,
it improves analysis quality significantly.

```cpp
struct TemporalContext {
    // Previous harmonic position
    std::optional<std::vector<ChordAnalysisResult>> previousChord;
    float distanceFromPreviousBeats = 0.0f;

    // Next harmonic position (look-ahead)
    std::optional<std::vector<ChordAnalysisTone>> nextTones;
    float distanceToNextBeats = 0.0f;

    // Key/mode inference at this position — from KeyModeAnalyzer
    std::optional<KeyModeAnalysisResult> keyModeContext;

    // Metric context
    float metricWeight = 1.0f;         // Strength of this beat
    bool isOnDownbeat = false;
    bool isAtPhraseBeginning = false;
    bool isAtPhraseCadence = false;

    // Duration of current harmonic event
    float durationBeats = 1.0f;

    // Recognized progression pattern if any
    std::optional<ProgressionPattern> ongoingPattern;
};
```

**How temporal context modifies scoring:**

- Previous chord continuation bonus — V7 → I, ii7 → V7 get score bonuses
- Key/mode confidence weighting — high-confidence key inference strengthens
  the diatonic root bonus beyond its flat default value
- Duration sensitivity — events shorter than half a beat get higher extension
  detection thresholds (passing chords flagged conservatively)
- Pattern completion — ii7 at previous position reinforces V7 at current position

**Implementation sequence:**
1. Define `TemporalContext` struct — optional parameter, existing tests unaffected
2. Add key/mode confidence weighting — simplest, uses already-computed data
3. Add previous chord continuation scoring
4. Add duration sensitivity for short events
5. Add pattern recognition — most complex, built on 1-4 being stable

### 5.4 Modal Extension — Implemented

All 7 diatonic modes (Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian,
Locrian) are now evaluated. Each mode has a characteristic pitch boost/penalty and
a frequency prior configurable via user preferences (mode tier weights).

Mode suffixes are abbreviated: "maj", "min", "Dor", "Phryg", "Lyd", "Mixolyd", "Loc".

**Melodic minor modes** — still planned for jazz style support:
- Lydian Dominant (mode 4 of melodic minor) — #11 and b7 together
- Altered/Superlocrian (mode 7 of melodic minor) — maximum tension

### 5.5 Monophonic and Arpeggiated Input

Monophonic and arpeggiated chord inference is now tracked under
§4.1d. That section contains the current provisional phased plan,
including the separate-engine / unified-orchestrator design,
Phase 1a validation-first workflow, and the deferred full monophonic
engine for unannotated material.

### 5.6 Extended Harmonic Functions — Planned

Currently, non-diatonic chords show a borrowed source key label (e.g. "Bb min") when
an identifiable source is found. Explicit labeling of harmonic functions is backlogged:

**Classical chromatic vocabulary:**
- Augmented sixth chords (Italian, French, German +6): approach chords to V
- Neapolitan chord (♭II, N6): flat-supertonic major
- Common-tone diminished seventh

**Secondary function:**
- Secondary dominants / leading-tone chords (V/V, vii°/V, etc.)
- Tritone substitutions (subV/x): dom7 whose root is a tritone from the expected dominant
- Backdoor dominant (♭VII7 as V7 substitute) — jazz-specific

**Structural distinctions:**
- Tonicization vs. modulation: brief secondary dominant vs. genuine key change
- Chromatic mediants: major-third key relationships

**Implementation prerequisite:** resolution-target tracking (look-ahead to next chord
region) is required for secondary dominant and tritone sub detection.

### 5.7 Normalized Confidence Scores — Implemented for KeyModeAnalyzer

`KeyModeAnalysisResult::normalizedConfidence` is 0.0–1.0 via sigmoid on the score
gap (midpoint 2.0, steepness 1.5). Usage thresholds:

- Above 0.8 — display without qualifier
- 0.5–0.8 — append "?" to key/mode label
- Below 0.5 — suppress key-dependent chord-track annotations rather than exposing a low-confidence key

`ChordAnalysisResult` still returns only raw scores. Normalized confidence for
chord analysis is a planned extension.

### 5.7a Confidence Interpretation and "Good Enough" Plateau

The current confidence signals must be interpreted as heuristic ranking
stability, not calibrated probability of correctness.

- `KeyModeAnalysisResult::normalizedConfidence` is derived from an internal
  score-gap sigmoid and is suitable for tentative vs assertive UI exposure.
- `ChordAnalysisResult` still exposes raw scores only.
- Current corpus benchmark tables are mostly root-pitch-class agreement metrics,
  not full harmonic-correctness metrics.

Therefore the product target is not "always emit a label". The target is:

- high precision on exposed results
- calibrated abstention when evidence is weak
- strong internal consistency across all entry points
- coverage gains only after precision is acceptable

For planning purposes, the current vertical tertian engine plus targeted texture
fixes should be expected to plateau around 65–75% exact external root+quality
agreement on **full-texture tonal corpora** (SATB choral, chamber, full piano
accompaniment). This band applies specifically to region-centric DCML comparison
methodology. Thin-texture corpora (Mozart piano sonatas, C.P.E. Bach keyboard,
solo melody) are excluded from this target — they require a separate inference
strategy and should not be compared against the same band. The When in Rome and
music21-surface comparisons use different methodologies and are not directly
comparable to this figure.

Exact Roman/function agreement will remain lower because it compounds chord
identity, key/mode, analytical granularity, and reference-philosophy
differences. Beyond that band, diminishing returns should be expected unless
the system adds a second inference family or richer musical representation.

Highest-return work before that plateau:

1. remaining recurring texture fixes: broken-chord/pedal boundary handling,
  Baroque passing-bass handling, and phrase-aware key look-ahead. These address
  primary failure modes that confidence calibration cannot fix.
2. evaluation tier separation: split published quality reporting into
  internal consistency, root-only/root+quality external agreement on
  full-texture corpora, and full harmonic correctness. Baselines must be
  stable before held-out calibration is meaningful.
3. normalized chord confidence plus held-out calibration on stable baselines.
  This becomes useful only after the primary texture failure modes are reduced.
4. mixed-texture orchestration: add a lightweight second strategy for
  obviously arpeggiated or single-line spans. "Obviously arpeggiated" is
  defined as maximum simultaneous pitch-class count in any beat window <= 2.
  Compare calibrated confidence across strategies and treat abstention as a
  valid outcome.
5. an explicit region-identity decision: preserve-all regions must be keyed to
  either `root + quality` (harmonic summary mode) or full sonority identity
  (as-written mode). Fold the deferred chord-track octave-deduplication item
  into this decision. Both modes are needed; neither should remain undecided.

The following should be treated as post-plateau scope expansion rather than
immediate blockers:

- quartal/quintal language detection
- rootless ensemble awareness
- polychordal / upper-structure detection
- register-sensitive add2 vs add9
- the full Phase 2 monophonic engine

### 5.8 Known Analyzer Limitations

These are known cases where the current tertian template-matching approach produces
incorrect or misleading results. Each has a planned resolution noted.

**Quartal and quintal chords**

The analyzer is built entirely on tertian templates — chords built from stacked thirds.
Chords built from stacked fourths or fifths are force-fitted into the nearest tertian
interpretation. The four open strings of a guitar (E-A-D-G) — three stacked perfect
fourths — are analyzed as Em11, which is technically defensible but musically wrong.
The chord has no tertian root in the meaningful sense. The planned resolution is a
musical language detector that switches the analyzer into a quartal/quintal mode before
attempting tertian analysis. Quartal and quintal support is in Prepared scope.

**The add2/add9 distinction**

Cadd2 and Cadd9 contain identical pitch classes — the distinction is registral, not
harmonic. The added D appears within the root's octave (add2) or above it (add9). The
current analyzer discards register information immediately by reducing all pitches to
pitch classes. Distinguishing add2 from add9 requires preserving full MIDI pitch through
the analysis pipeline and running a register-aware second pass after chord identification.
This is a planned extension — not a minor change — and is deferred until the generation
engine requires it.

**Rootless voicings**

When no root is present — common in jazz ensemble writing where the bass instrument
provides the root — the analyzer's bass-note-root bonus misfires. The lowest sounding
note gets promoted to root status incorrectly. Correct handling requires knowing that a
bass instrument is providing the root, which is context the current analyzer does not
have. Planned resolution: the `TemporalContext` struct will carry ensemble awareness,
suppressing the bass root bonus when appropriate.

**Polychordal and upper structure voicings**

Two distinct chords superimposed produce a pitch class set the analyzer interprets as a
single complex tertian chord. The two-chord structure is lost. Planned resolution: a
polychordal detection pass that identifies superimposed triadic structures before tertian
analysis runs.

**Piano left-hand beat-1 pattern over-segmentation**

In piano music with a single bass note on beat 1 followed by a chord block on beats 2–3
(mazurka, waltz, and march accompaniment patterns), the Jaccard boundary detector fires
between beat 1 `{bass pc}` and beats 2–3 `{chord pcs}` because these are completely
different pitch-class sets. Under a pedal marking, all three beats should accumulate to
one pitch-class set. Fix required: include pedal-sustained notes when computing per-beat
pitch-class sets for Jaccard boundary detection. Confirmed on Chopin BI16-1 measure 1.

**bassNoteRootBonus miscalibration — confirmed by score inspection (2026-04-09):**

Score inspection across four corpora confirms a single root cause:
`bassNoteRootBonus` fires unconditionally on the lowest sounding note,
regardless of whether that note is actually the chord root.

Confirmed failure patterns:

- Chopin mazurka: single bass note on beat 1 (root) isolated from chord block on beats
  2-3 — bass correctly identifies root but creates spurious boundary vs chord beats
- Mozart sonata: arpeggiated left hand (C→E→G) — each successive lowest note promoted
  to root, producing Em / Dm7 / Bdim instead of C
- Corelli trio sonata: walking/stepping bass line — each bass step promoted to root,
  producing one chord per bass note instead of recognizing the underlying harmony
- Beethoven string quartet: cello moving in inversions and stepwise motion — same
  pattern as Corelli

All four cases share the same mechanism: the bass voice moves at a faster rate than the
harmonic rhythm, and each bass note independently receives `bassNoteRootBonus`,
overriding the correct root identification from the chord tones above.

**Implemented fix (2026-04-09):**

`bassNoteRootBonus` is now conditioned on corroborating root-position support in the
accumulated tones:

- Full bonus: the candidate's fifth slot is present, and third-bearing templates also
  retain their own matching third
- Reduced bonus: a major/minor third above the bass is present, but the fifth support
  is absent or contradictory
- Minimal bonus: no third or fifth support above the bass is present

Two new preferences expose the reduced tiers in `ChordAnalyzerPreferences`:

- `bassRootThirdOnlyMultiplier = 0.3`
- `bassRootAloneMultiplier = 0.1`

This preserves the bonus for clear root-position chords while materially reducing the
cross-corpus bass-root failure signal. Validation on 2026-04-09:

- Bach WIR structural improved from 50.0% to 52.3%
- Bach music21 surface re-run now reports 39.3% average agreement
- Beethoven 59.9%, Mozart direct DCML 26.7% root agreement with 59.5%
  `bassIsRoot` in disagreements (not directly comparable to the full-texture
  corpora because only 32.5% of our regions align), Corelli 63.3%, Chopin 57.5%,
  Grieg 50.3%,
  Schumann 58.7%, Tchaikovsky 58.9%, Dvorak 66.2%
- Weighted non-Bach `bassIsRoot` in disagreements dropped from 73.0% to 58.0%
  (piano 58.5%, chamber 57.5%)

The remaining Chopin BI16-1 notation mismatch turned out to be separate from scoring:
the batch path already collapsed adjacent same-root/same-quality regions, but
`analyzeHarmonicRhythm(..., PreserveAllChanges)` did not. The notation bridge now uses
the same collapse rule, so repeated slices that analyze to the same chord merge into one
region even in preserve-all mode. A dedicated notation regression now checks that BI16-1
opening collapses to a single G-major region. A follow-up BI16 regression on the full
populate path also guards against mixed chord/rest measures: sparse unanalysable spans
within a measure are now absorbed into neighboring written chord regions in
`populateChordTrack()` instead of being left behind as visible rests.

Post-fix score inspection isolated three remaining categories, none of which revive the
original unconditional bass-root promotion bug:

- **Dvorak op08n06: accepted ambiguity ceiling.** The chord-track output is musically
  plausible and the disagreement with DCML reflects genuine harmonic ambiguity in
  chromatic Romantic writing. No follow-up scoring change is planned for this movement.
- **Corelli op01n08d: deferred Baroque passing-bass limitation.** Walking bass passing
  tones can still pull the output toward sus/slash-chord spellings rather than the
  underlying triadic harmony. This is now documented as a known limitation of the
  current vertical scorer in Baroque stepwise bass textures.
- **Schumann Kinderszenen: not a comparison artifact.** `tools/compare_analyses.py`
  classifies chord identity from root pitch class and quality, and the direct DCML
  runners compare root pitch class only. Slash-chord spellings such as `D7/C` already
  match inversional DCML spellings when the underlying root pitch class agrees, so the
  58.7% Schumann baseline is accepted as genuine rather than a notation-mapping error.
- **Chord track octave deduplication: deferred.** When imploding to chord track,
  octave duplicates are currently collapsed to a single pitch class. That is correct
  for harmonic-summary analysis but incorrect for "as written" chord-track generation,
  where the original voicing should be preserved. Fixing this requires a separate
  implode-bridge mode flag to distinguish harmonic summary from as-written output.

#### Background — resolved-issue history (not needed to understand the current design)

> *The following is a dated record of fixes and a 2026-04 follow-up roadmap, retained for provenance. It is **history**,
> not current status: the current open limitations are the named items above, and live status / next steps live in
> STATUS.md.*

The post-fix score-review roadmap (2026-04-10) ran under a gated Milestone A before any
later score-review work was allowed to proceed:

- **A1 — shared same-chord merge semantics.** Batch and notation now collapse
  adjacent same-root/same-quality slices by unioning tone sets and recomputing
  the bass from the merged tones. Acceptance is complete: `composing_tests.exe`
  passed 295/295, `notation_tests.exe` passed 19/19, `batch_analyze_regressions`
  passed, Bach WIR structural remains 52.3%, and Chopin remains 57.5%.
- **A2 — mechanical batch/notation parity.** `batch_analyze` now supports
  `--dump-regions batch|notation|notation-premerge`, the notation bridge exposes
  pre/post-merge debug capture, and `tools/check_parity.py` compares both paths on
  one score. Acceptance is complete: BWV 227.7 and Chopin BI16-1 now match exactly
  on region starts, spans, roots, qualities, and tone sets.
- **A3 — confidence/exposure cleanup.** Complete. Key-dependent chord-track output
  is now confidence-gated: below 0.5 it is suppressed, from 0.5 to 0.8 only the
  tentative key label survives, and at 0.8 or above the full key-dependent annotation
  set is allowed. A Dvorak `op08n06` notation regression verifies that low-confidence
  regions do not emit key labels or Roman numerals while confident regions still do.

Use the following benchmark passages for any follow-up score inspection or UI
validation:

- Bach BWV 227.7: bars 1–2, 8–10, final cadence
- Chopin BI16-1: bars 1–5, 10–16, trio
- Dvorak op08n06: early slow section, chromatic middle, late modal stretch

**Formatter: double quality prefix (confirmed 2026-04-13):**
Chord symbol formatter produces unreadable strings when quality and extension share
a prefix: `Csussus2` (suspended + sus extension), `G#aussus5` (augmented + sus
extension), `Dsussus5D+` (worst case).
Confirmed in 7+ scores across all styles.
Fix: sanitize `sussus`→`sus`, `aussus`→`aug(sus...)` in formatSymbol.
**Fixed 2026-04-13** — commit `4c35da17`.

**Formatter: invalid bass note name `/p` (confirmed 2026-04-13):**
TPC resolution failure produces `p` as a bass note name, e.g. `BbMaj7/p`. Occurs
when bassTpc is TPC_INVALID. Fix: guard against invalid TPC before appending
slash bass suffix. Confirmed in Dvořák Silhouettes.
**Fixed 2026-04-13** — commit `4c35da17`.

**Key detection: relative major/minor ambiguity (confirmed 2026-04-13):**
When opening chord is in first inversion, the bass note matches the tonic of the
relative key, causing the inferrer to lock onto the wrong member of the relative pair:
- BWV 227/7 (E minor, 1♯): was reading as G major throughout
- BWV 66.6 (F# minor, 3♯): was reading as A major (BWV 66.6 was already correct per
  music21 ground truth — STATUS.md expectation corrected 2026-04-13)

**Fixed 2026-04-13** — complete-triad bonus + piece-start hysteresis, commit `3ba80cb7`.

**Preset misuse degrades output (confirmed 2026-04-13):**
Jazz preset causes key context drift on Classical scores. Mozart K279 with Jazz preset
reads C major as D Dorian in multiple passages. Standard preset on same score produces
output close to DCML reference. Preset selection is user responsibility — document
clearly in UI and help text. Standard preset is correct default for all non-jazz
repertoire.

**Modulation tracking — philosophy difference (confirmed 2026-04-13):**
Our analyzer stays in the home key and labels borrowed chords with chromatic scale
degrees (e.g. `♭VII`, `II` in C major). DCML reference uses tonicization notation
(e.g. `V/IV`, `IV/III`). Both are valid analytical approaches. Our approach is more
accessible for general users. Not a bug — design choice.

**Third-inversion dominant seventh ambiguity (confirmed 2026-04-13):**
G7/C (G dominant seventh, C in bass) is sometimes identified as Gm/C (G minor over C).
Occurs when B natural evidence is weak and Bb reading is slightly preferred. Confirmed
in Mozart K279 and Chopin Mazurkas. Known limitation of vertical template matching on
passing-bass textures.

**Roman numeral quality at minor tonic cadences (confirmed 2026-04-13):**
At minor key cadences, analyzer occasionally writes major `I` where minor `i` is
correct. Confirmed in Corelli. Likely a chord quality threshold issue at cadential
points.

**Over-segmentation on dense piano texture (confirmed 2026-04-13):**
Dvořák Silhouettes and Chopin Mazurkas show repeated identical chord labels
(e.g. `Bb×8`, `Fsus×20`) from Jaccard boundary firing on dense arpeggiated texture.
Same-chord merge logic is working but the merge threshold may be too fine. Known
limitation — mixed texture orchestration would address this post-plateau.

**`do` abstention in jazz context is correct behavior (confirmed 2026-04-13):**
In "You Must Believe in Spring" (jazz ballad, 5 flats), the analyzer correctly abstains
on highly chromatic passages, writing `do` (no label) rather than guessing wrong. This
is confidence gating working as intended. More trustworthy than wrong labels.

**Campania font rendering artifact (`Dsdim`, `Fsdim` etc.) — MuseScore core issue, not our bug (confirmed 2026-04-17):**
Certain chord symbol strings containing diminished chords on specific roots (D, F, C, A)
render with a spurious `s` prefix in MuseScore's Campania chord symbol font — e.g.
`Ddim7/A` renders visually as `Dsdim7/A`. The internal string produced by our formatter
is correct: confirmed by clicking the element to edit it, which shows the correct string
without the `s`. The same artifact affects other chord symbol tools including third-party
plugins. This is a MuseScore core font rendering issue, not a bug in the composing module.
The same artifact appears in chord symbol plugins used for comparison QA. Fix requires
changes to the Campania font or MuseScore's chord symbol rendering pipeline — outside the
scope of this module.

**iii/III triad confusion is non-local (confirmed 2026-05-15, Iter 90 characterization):**
iii/III triad confusion ({C,E,G} = C major vs Em/C) is non-local — cannot be resolved
with a local gate in `chordanalyzer.cpp`. 84% of the Baroque BIR=false=118 residual is
this pattern. Fix belongs in a bridge-level adjacent-context pass (see
`docs/iter90_bass_as_root_promotion_shelved.md` for characterization and Iter 91 design).

### 5.9 Key Signature Injection — Not Planned

An earlier design considered automatically suggesting key signature insertions in the main
score when the key/mode inferrer detected extended passages in a different key. This was
superseded by the key/mode annotation feature in the chord track (§11.5). The chord track
provides the same analytical information — inferred key regions with confidence indicators —
without modifying the main score. The user reads the chord track annotations and decides
independently whether to add key signatures to the main score. No automatic key signature
injection is planned.

### §5.10 Tonicization Labels

Secondary dominant and other tonicization labels (V/V, vii°/V, V/ii etc.)
exposed in the annotate path Roman numeral layer. The analyzer already
detects tonicizations internally; this exposes the conclusion as an
annotation. Universal across all presets.

### §5.11 Augmented Sixth Chord Labels

Explicit It+6, Fr+6, Ger+6 labels in the annotate path Roman numeral layer.
These replace the generic chromatic Roman numeral (e.g. ♭VI) when the
analyzer detects the specific augmented sixth interval pattern.

**Preset gating is NOT implemented — corrected 2026-08-02 (`OPEN_ITEMS.md` OI-112(c); this section
asserted "Gated to Standard and Baroque presets only", and the code defers exactly that).**
`formatRomanNumeral()` has no preset context, so the gate is explicitly deferred at the site
(`chordsymbolformatter.cpp:882-883`) and the labels are emitted for every preset. The corpus shows
no augmented-sixth label under the Jazz preset, but that is an upstream-analysis coincidence — the
`SharpThirteenth` extension the classifier requires is not set there — and not the documented gate.
**Whether the gate should exist at all is OPEN** and is not settled here; if it is wanted, the
preset must first be threaded through the formatter.

### §5.12 Pedal Point Detection — Two-Pass Analysis

**Status: Implemented (Session 18, master `fb9a27ce9a`).** **Superseded as a design by the
voice-independent pedal-point class of the ornament vocabulary (§7.4, user-ratified 2026-07-26):** the
two-pass detector described below can only see the lowest voice, and it retires with the legacy analysis
path. The ornament class that replaces it is DEFERRED to its own increment (`OPEN_ITEMS.md` OI-194), so the
two-pass detector below is still the code on the legacy arm; on the production record path the pedal fields
are left empty.

When the lowest-pitched tone in a window is structurally lighter than the upper
voices — as in a dominant or tonic organ point — it may not belong to the chord
formed by the upper voices. A single-pass template match will either (a) force a
bass-root reading and suppress the upper-voice harmony, or (b) return a slash chord
with the wrong root identity if the template accidentally fits. Two-pass analysis
resolves this.

#### Algorithm

**Pass 1** runs normally on all voices. If the winning result's root is a chord
tone of the detected quality (checked by `isBassChordTone()`), the bass is part of
the chord (e.g. an inversion) and no pedal detection occurs.

**Pass 2** is triggered only when the Pass 1 bass PC is NOT a chord tone of the
winner. It re-runs `analyzeChord()` on the upper voices only (the bass PC is removed
from the tone list). Two conditions must both be met before the pedal reading is
accepted:

1. The upper voices produce at least 2 distinct pitch classes (prevents triggering
   on a unison or single-note passage).
2. The normalized confidence of the Pass 2 winner — computed as the score gap
   between the winner and the best **different-root** competitor — reaches or
   exceeds `pedalConfidenceThreshold` (default 0.65).

When both conditions are met, the Pass 2 result replaces the full-pass result, and
`ChordIdentity::isPedalPoint = true` / `pedalBassPc` are set on the returned
`ChordAnalysisResult`.

#### Why "different-root competitor"

Multiple chord templates share the same root (e.g. Major triad, Maj7, and Dom7 all
score identically when extension tones are absent). If the gap is computed against
`results[1]` — which may be the same root — the gap is ~0 and confidence collapses
to ~0.047, blocking pedal detection for bare major triads. Computing the gap against
the first result whose `rootPc` differs from the winner gives a meaningful separation
signal regardless of how many same-root templates appear in the candidate list.

#### `isBassChordTone()` helper

Checks whether a pitch class is a structural member of the chord (root, triad tone,
or any detected extension). Quality-specific triadic intervals are checked first.
Extensions are checked from the `extensions` bitmask (min7, maj7, dim7, b9, 9, #9,
11, #11, b13, 13). Two additional rules handle borderline cases:

- **Any extension (9th–13th) listed in the bitmask:** the corresponding interval
  also marks the bass as a chord tone.
- **P4 with any seventh present:** if the chord has a min7, maj7, or dim7 detected
  (even at the lower `kSeventhThreshold = 0.12`) and the bass is a P4 above the
  root, it is treated as a chord tone. This handles slash chords like Cm7/F where
  the bass F is at exactly `kExtensionThreshold = 0.20` and therefore NOT detected
  as `NaturalEleventh` by the extension scanner, yet is structurally part of the
  chord.

#### `pedalConfidenceThreshold` parameter

Default 0.65. Appears in `ChordAnalyzerPreferences::bounds()` with range [0.30, 0.95].
Set to 0.0 to disable pedal detection entirely (the `pedalConfidenceThreshold > 0.0`
guard short-circuits Pass 2 before any analysis is attempted).

#### Bridge annotation

When `isPedalPoint = true`, the annotate path (`addHarmonicAnnotationsToSelection`)
writes an additional `StaffText` at the same segment in the format `"X ped."` where
`X` is the chord symbol of the pedal bass pitch class formatted as a simple major
root name (e.g. `"G ped."`, `"C ped."`). This is placed only when Roman numeral
annotations are enabled.

---

### §5.13 Analyze-at-Tick Path Table

Every entry point that runs harmonic analysis against a tick position is listed here.
There is no Jazz path and no symbol reading anywhere in the analysis pipeline.

**★ Table re-synced 2026-08-02 (`OPEN_ITEMS.md` OI-238 and its dated note).** The paragraph above
also said "no path-selection flag", and the table below described only the legacy arm. Both were
false at HEAD. **There IS a path-selection flag, and it is the production default:** the single
funnel `analyzeHarmonicContextAtTick` branches on `prefs->useJointNotationRecord()`
(`notationcomposingbridge.cpp:728-738`) and returns from the record arm before any legacy code is
reached; the flag's default is `true` (`composingconfiguration.cpp:178`). Three further corrections
are folded in below: `prepareUserFacingHarmonicRegions()` no longer exists in the production tree
(only a test comment and a corpus README still name it); the implode bridge contains **zero**
references to `analyzeHarmonicContextAtTick`, and the tuning bridge calls
`analyzeNoteHarmonicContext` (`:190`, `:547`) and `analyzeHarmonicRhythm` (`:794`) instead; and
`populateChordTrack` does **not** re-analyze each stretch through `analyzeHarmonicContextAtTick`.

#### Entry points

Every row is what runs at HEAD. "Record arm" means `useJointNotationRecord == true`, the default;
"legacy arm" means the explicit `false` branch, which is dormant.

| Entry point | File | Caller | Notes |
|---|---|---|---|
| `harmonicAnnotation(note)` | `notationcomposingbridge.cpp` | `notationaccessibility.cpp` (status bar) | Calls `analyzeNoteHarmonicContextDetails()` → `analyzeHarmonicContextAtTick()`. |
| `analyzeNoteHarmonicContext(note, …)` | `notationcomposingbridge.cpp` | `notationcontextmenumodel.cpp` (right-click), `notationtuningbridge.cpp:190/:547` (tune at a note) | Same funnel; returns ranked candidates. |
| `analyzeRestHarmonicContextDetails(rest)` | `notationcomposingbridge.cpp:967-981` | `notationcontextmenumodel.cpp` (right-click on a rest) | Same funnel, anchored at the rest's tick. |
| `analyzeHarmonicContextAtTick(score, tick, …)` | `notationcomposingbridge.cpp:703` | the three entries above — it has no other production caller | **THE funnel, and the path-selection site.** Record arm: `produceNotationRecord` (whole score, once) → `noteView(rec, tick)` → `buildNoteContextFromRecord`. Legacy arm: the bounded expanding-window path (`analyzeHarmonicContextRegionallyAtTick`), then the tick-local fallback. |
| `analyzeHarmonicContextLocallyAtTick(…)` | `notationcomposingbridge.cpp:621` | **no production caller** — the record arm returns first (`:738`); reached only from the legacy arm's fallback (`:753`) and directly from `pipeline_snapshot_tests.cpp:569` | The P4 tick-local fallback. See the reachability entry below. |
| `analyzeHarmonicRhythm(score, start, end, …)` | declared `notationcomposingbridge.h:161`, defined `notationharmonicrhythmbridge.cpp:69` | the legacy arms of the span emitter, implode and tuning; `batch_analyze` | Time-range scanner over `region::analyzeRegions()`. **The only entry that takes a time range** — and it is legacy-arm only. |
| `addHarmonicAnnotationsToSelection(score, …)` | `notationcomposingbridge.cpp:1385` | `notationinteraction.cpp` (menu action) | Annotation write path. Record arm: `produceNotationRecord` → `analyzeSectionFromRecord` → `emitHarmonicAnnotations` (`:1491-1507`). Legacy arm: `analyzeHarmonicRhythm` → `analyzeSection` (`:1509-1519`). |
| `populateChordTrack(score, …)` | `notationimplodebridge.cpp` | `notationinteraction.cpp` (implode action) | Chord track write path. Record arm: `produceNotationRecord` → `analyzeSectionFromRecord` → `emitImplodedChordTrack` (`:1409-1431`). Legacy arm: `analyzeHarmonicRhythm` → `analyzeSection` (`:1434-1441`). |
| `applyRegionTuning(…)` | `notationtuningbridge.cpp` | `notationinteraction.cpp` (tune-selection action) | Record arm derives the tuning stretches from the record; legacy arm calls `analyzeHarmonicRhythm` (`:794`). |

**What a tick query reads, and what it costs.** On the legacy arm a tick query analysed a bounded
window around the tick. **On the record arm there is no such narrowing:** the funnel produces a
WHOLE-SCORE record and looks the tick up in it (the producer decodes the whole score once and does
not cache — see the record-path section at the head of this document). A reader consulting this
table to learn what music a tick query reads, or what it costs, must read the record-arm row, not
the `analyzeHarmonicRhythm` row. The input-scope consequence is the same question `OPEN_ITEMS.md`
OI-212 tracks on the span seams; the cost consequence is OI-203/OI-206 and the §12.1a correction.

**The P4 tick-local fallback's reachability (recorded 2026-08-02, OI-238).** §3.3's "D-P4" entry
makes the tick-local cold-context fallback the current accepted contract, with a stated revisit
trigger: the Stage-3 design must state explicitly what P4 and the bridge consume from the decode.
Two things are now true and neither was written down. The joint/record design never stated it; and
on the switched build `analyzeHarmonicContextLocallyAtTick` is **unreachable from the production
funnel**, surviving as a direct call from the pipeline-snapshot suite alone. So that contract
governs nothing on the shipped product, and the `tickLocal` golden section — which the switch
reconciliation reported byte-identical — is measuring a path production no longer takes. Its
coverage must not be over-read. **What to do about either fact is OPEN** and is not settled here.

#### Order-of-annotation safety

Because there is no Jazz path and no symbol-reading gate, order of annotation has no
effect on region boundaries. Writing chord symbols to the score via one path does not
change what any other path produces from the same notes.

The `forceClassicalPath` flag that previously short-circuited Jazz boundary detection
has been removed (02e3733afb). The classical §4.1c Jaccard path is now the only path.

#### Unknown-quality Roman numeral fallback

`ChordSymbolFormatter::formatRomanNumeral()` returns `""` when
`ChordQuality::Unknown` — this occurs for bare fifths (no third detected) in
Aeolian passages where the chord analyzer cannot determine major vs. minor quality
from the available tones.

Both the annotation path (`addHarmonicAnnotationsToSelection`) and the chord-track
path (`populateChordTrack`) apply `forceChordTrackQualityFromKeyContext()` as a
post-analysis fallback: when `formatRomanNumeral` returns empty and quality is
Unknown, the diatonic triad shape for the current degree+mode is substituted.
This ensures Roman numeral annotations are written even for bare-fifth regions.

### §5.14 Enharmonic Root Spelling — TPC-Guided Disambiguation

**Status: Implemented (2026-04-20, Session 24).**

#### Problem

`pitchClassName(pc, keyFifths)` converts a pitch class to a note name using key
signature direction. When `keyFifths ≥ 0` (sharp keys or C major) it returns sharp
names. In C major (`keyFifths = 0`) this means pitch class 10 (Bb/A#) is returned
as "A#" — wrong for any score written in C major.

The original implementation had no access to TPC (Tonal Pitch Class), which encodes
the composer's actual spelling intention as written in the score.

#### TPC encoding (MuseScore circle-of-fifths)

| TPC range | Names | Examples |
|-----------|-------|---------|
| 7–13 | Flat spellings | Fb(7) … Bb(13) |
| 14–20 | Natural notes | F(14) C(15) G(16) D(17) A(18) E(19) B(20) |
| 21–27 | Sharp spellings | F#(21) … B#(27) |

Key notes: TPC 11 = Ab, 12 = Eb, 13 = Bb, 23 = G#, 24 = D#, 25 = A#.

#### Fix: `pitchClassNameFromTpc(pc, tpc, keyFifths, spelling)`

TPC is consulted **only when `keyFifths == 0`** (C major / A minor). That is the
only context where the key signature alone does not resolve the flat-vs-sharp
ambiguity. For all other keys the key signature already determines the correct
accidental direction, and TPC is ignored — this prevents score-data misspellings
(e.g., a note stored as D# TPC=24 in a C Dorian passage where Eb is correct) from
corrupting the output.

```cpp
const char* pitchClassNameFromTpc(int pc, int tpc, int keySignatureFifths,
                                  ChordSymbolFormatter::NoteSpelling spelling)
{
    // TPC consulted only for C major / A minor (keyFifths == 0)
    if (tpc >= 0 && keySignatureFifths == 0) {
        const bool preferFlat = (tpc >= 7 && tpc <= 13);
        const size_t idx = static_cast<size_t>(normalizePc(pc));
        if (preferFlat)
            return isGerman ? FLAT_NAMES_GERMAN[idx] : FLAT_NAMES[idx];
        return isGerman ? SHARP_NAMES_GERMAN[idx] : SHARP_NAMES[idx];
    }
    return pitchClassName(pc, keySignatureFifths, spelling);
}
```

#### `ChordIdentity.rootTpc`

To make the root TPC available to `formatSymbol()` (which was previously called
with only `rootPc`), a new field `int rootTpc = -1` was added to `ChordIdentity`.
The chord analyzer populates it from the highest-scoring root candidate's TPC.
`formatSymbol()` and `formatRomanNumeral()` pass `rootTpc` through to
`pitchClassNameFromTpc`. `bassTpc` was already present; the pattern is now uniform.

#### Before / after on affected scores

| Score | Sharp roots before | Sharp roots after |
|-------|--------------------|-------------------|
| sun-bear-osaka (C major passages) | 65 wrong | 18 (all legitimate) |
| take-five (Eb major) | 6 wrong | 0 |
| pinocchio (mixed flat keys) | 3 wrong | 3 (pre-existing score data misspellings, not formatter errors) |

Corpus baselines (Corelli, Bach, Beethoven) unchanged — fix affects chord symbol
display strings only, not rootPc detection used by corpus comparators.

#### Unit tests

7 tests in `Composing_EnharmonicSpellingTests` in `chordanalyzer_tests.cpp`:

| Test | Scenario |
|------|---------|
| `BbRootInCMajorSpellsAsBb` | TPC=13 (Bb), keyFifths=0 → "Bb" not "A#" |
| `EbRootInCMajorSpellsAsEb` | TPC=12 (Eb), keyFifths=0 → "Eb" not "D#" |
| `AbRootInCMajorSpellsAsAb` | TPC=11 (Ab), keyFifths=0 → "Ab" not "G#" |
| `BbSus4InCMajorSpellsAsBbsus` | {Bb,Eb,F}, keyFifths=0 → starts "Bb" |
| `GsharpRootInSharpKeyStaysGsharp` | TPC=23 (G#), keyFifths=4 → key sig wins → "G#m" |
| `NoTpcFallsBackToKeySignatureFlat` | tpc=-1, keyFifths=-5 → key sig → "Bb" |
| `SharpTpcInFlatKeyUsesKeySignature` | TPC=24 (D#), keyFifths=-2 → key sig wins → "Eb" |

### §5.15 Sus4 Structural Penalty — Requiring the Defining Perfect Fourth

**Status: Implemented (2026-04-21, Session 25).**

#### Problem

Sus4 templates (`ChordQuality::Suspended4`, intervals containing `5` = P4) were
winning in regions where the perfect fourth was barely present — a weak passing tone
or absent — yielding false Sus4 labels on chords that should be power, major, or minor.
The perfect fourth *is* the defining suspension tone of Sus4; without it the chord is
not convincingly sus4.

#### Fix: `kSus4MissingFourth = 0.70` penalty in `structuralPenalties()`

Applied when **all** of the following hold:
1. Template quality is `Suspended4` with interval `5` (P4) in `tpl.intervals`.
2. `pcWeight[fourthPc] < extThreshold` (0.20 Standard / 0.12 Jazz).
3. Template is **not** Sus4b5 (`intervals[2] == 6`): Sus4b5 uses the tritone as the
   identifying interval, not the P4. Penalising it would incorrectly push the root
   toward D when the correct analysis has C as root.

Sus4♯5 and standard Sus4 are penalised; Sus4b5 is excluded.

```cpp
static constexpr double kSus4MissingFourth = 0.70;

const bool sus4HasPerfectFourth = (tpl.quality == ChordQuality::Suspended4)
    && std::any_of(tpl.intervals.begin(), tpl.intervals.end(),
                   [](int i) { return i == 5; });
const bool isSus4FlatFive = (tpl.quality == ChordQuality::Suspended4)
    && tpl.intervals.size() >= 3 && tpl.intervals[2] == 6;
if (sus4HasPerfectFourth && !isSus4FlatFive) {
    const int fourthPc = static_cast<int>((rootPc + 5) % 12);
    if (pcWeight[static_cast<size_t>(fourthPc)] < extThreshold) {
        score -= kSus4MissingFourth;
    }
}
```

#### Root-only single-note gap carry fix (notationcomposingbridgehelpers.cpp)

The Sus4 penalty produced a secondary cascade in Corelli op01n08d m.13: Gsus4/7
(intervals `{0,5,7,10}`) lost 0.70 points, allowing G-power chord (score 3.775) to
win the region `[19200,19680)`. The adjacent sparse region `[18240,18720)` had a
single note G (1 PC). `regionSupportsGapTones({G}, G-power)` returned TRUE (G is in
`{G,D}` and matches root), so the gap was carried as "G5" instead of inferring "Gm"
from key context.

**Fix in `inferGapRegion`:** a `supportsCarry` lambda blocks carry when the gap has
exactly 1 pitch class AND that pitch class equals the adjacent region's root. A root-
alone gap carries no quality information; the diatonic key context is more reliable.
Non-root chord tones (e.g. G as the **third** of Em) continue to carry correctly,
because they confirm the chord quality through interval relationship.

#### Corpus impact

| Corpus | Before | After | Δ |
|--------|--------|-------|---|
| Corelli 149 mvts | 69.54% | 70.9% | +1.36% |
| Bach chorales chord-identity 352 | 74.8% | 75.2% | +0.4% |
| Beethoven 70 mvts | 64.94% | 65.18% | +0.24% |

All three corpora improved. The Corelli gain is the largest because Sus4 is rare in
Baroque music — penalising false Sus4 wins redirects to the correct major/minor/power
analysis.

#### Unit tests

2 tests in `Composing_Sus4RequiresFourthTests`:

| Test | Scenario |
|------|---------|
| `Sus4SharpFiveNonBassRoot_SubThresholdFourth_NotSus4` | Sus4♯5/C: P4=F weight 0.04 < 0.20; non-bass root — Sus4 must not win |
| `FourthAboveJazzThreshold_JazzPreset_CanBeSus4` | P4 weight 0.13 ≥ Jazz threshold 0.12 — no penalty, Sus4 may win |

---

### §5.16 Session 26 — Declared-Mode Override, Pass2b Iterative, Enharmonic Normalization

**Status: Implemented (2026-04-21, Session 26).**

#### §5.16.1 Declared Key-Signature Mode Override

**File:** `notationcomposingbridgehelpers.cpp` — `resolveKeyAndMode()`

When the score's key signature has an explicit Mode property (MAJOR → Ionian, MINOR →
Aeolian), a strong prior block at the end of `resolveKeyAndMode` overrides the top-voted
mode if it is incompatible with the declared mode:

```cpp
if (declaredMode.has_value()) {
    const bool topIsCompatible = ...;
    if (!topIsCompatible) {
        for (const auto& r : modeResults) {
            if (rCompatible) { outKeyFifths = r.keySignatureFifths; ...; return; }
        }
    }
}
```

Root cause: Oak and the Lark m.14 has key signature Mode=Major; the analyzer voted G#
Dorian (close in fifths to F# Ionian), overriding the explicit Major declaration.

#### §5.16.2 Pass2b Iterative Bass-Movement Detection

**File:** `notationharmonicrhythmbridge.cpp` — Pass2b loop in `prepareUserFacingHarmonicRegions()`

Pass2b (bass-movement sub-boundary detection) is now iterative with `kMaxBassMovementPasses=8`:

```cpp
static constexpr int kMaxBassMovementPasses = 8;
bool anyNewSplit = true;
int passCount = 0;
while (anyNewSplit && passCount < kMaxBassMovementPasses) {
    anyNewSplit = false; ++passCount;
    // ... pass2b split logic; sets anyNewSplit = true when splits occur ...
}
```

Validation: Eye of Hurricane m.14 and m.15 each now produce 2 regions (beat 1 and beat 3)
instead of one wide 21-beat region.

#### §5.16.3 D#/G#/A# → Eb/Ab/Bb Enharmonic Normalization

**File:** `chordanalyzer.cpp` — `pitchClassNameFromTpc()`

Sharp-spelled chromatic notes (TPC ≥ 20, covering both MuseScore-internal and +1-offset
encodings) are normalized to their conventional flat chord-symbol spelling in keys where
the sharp is not yet diatonic:

```cpp
if (tpc >= 20) {
    if ((pc == 3  && keySignatureFifths < 4)   // D# → Eb (diatonic at E major)
     || (pc == 8  && keySignatureFifths < 3)   // G# → Ab (diatonic at A major)
     || (pc == 10 && keySignatureFifths < 5))  // A# → Bb (diatonic at B major)
        return FLAT_NAMES[idx];
}
```

The block fires before the `keySignatureFifths == 0` TPC-range check so it also
normalizes sharp-spelled notes in neutral-key (C major) contexts.

Root cause: Billy Boy Red Garland score had D# TPC (sharp accidental) written in G
Mixolydian context, producing `Em7add11/D#` and `D#Maj7` instead of `Em7add11/Eb`
and `EbMaj7`.

#### §5.16.4 Track-Specific Annotation Removal

**File:** `notationinteraction.cpp` — `addAnalyzedHarmony()`

The existing Harmony element removal loop now checks `ann->track() == cr->track()` before
deleting. Prevents removing chord symbols from wrong staves when annotating with multiple
staves selected.

#### §5.16.5 REST Context-Menu Harmonic Inference

**Files:** `notationcomposingbridge.cpp/h`, `notationcontextmenumodel.cpp/h`

New bridge function `analyzeRestHarmonicContextDetails(const Rest*)` mirrors
`analyzeNoteHarmonicContextDetails` for rest elements. The context menu now shows chord
analysis when right-clicking a rest. `appendNoteAnalysisItems` body extracted to
`appendAnalysisItemsForContext(items, NoteHarmonicContext)` shared by both paths.

#### §5.16.6 Status-Bar Alternatives Sorted by Confidence

**File:** `notationcomposingbridge.cpp` — `harmonicAnnotation()`

Alternative candidates (positions 1+) are sorted descending by `normalizedConfidence`
before formatting. Position 0 (region winner) is preserved at the top to maintain correct
harmonic-annotation text. A working copy is sorted; the original `chordResults` is
unchanged to avoid side-effects on callers.

---

## 6. The Style System

### 6.1 Overview

Musical styles are defined entirely in JSON files. The C++ code implements mechanisms —
voice leading optimization, chord generation, voicing rules — while JSON files define
parameters. Adding a new style never requires C++ changes.

### 6.2 Mixin Architecture

A style is not a monolithic entity but an assembly of independent dimensions. Each
dimension can be inherited from a different source:

```json
{
  "metadata": {
    "id": "bossa_nova",
    "name": "Bossa Nova"
  },
  "mixins": {
    "harmonic_language": "jazz/jazz_vocal",
    "rhythmic_feel": "dimensions/rhythm/samba_pattern",
    "bass_line": "dimensions/bass/samba_bass",
    "voicing": "dimensions/vocal/close_harmony",
    "form": "jazz/jazz_vocal"
  },
  "overrides": {
    "harmonic_language": {
      "substitution_frequency": 0.5
    }
  }
}
```

**Dimensions:**
- `harmonic_language` — available chords, progressions, substitutions
- `voice_leading` — motion type preferences, parallel interval tolerance
- `voicing` — drop voicing technique, lead voice position, spread constraints
- `rhythmic_feel` — meter, groove, harmonic rhythm patterns
- `form` — phrase structure, cadence types, section characteristics
- `bass_line` — walking bass, funk bass, melodic bass character
- `melodic` — scales, ornaments, approach notes
- `idiomatic_material` — fills, riffs, characteristic textures
- `ensemble` — voice count, ranges, blend characteristics
- `tuning` — which tuning system applies
- `generation` — creativity level, substitution frequency, complexity target
- `analysis` — what the analyzer flags as problems vs features

**Conflict resolution priority:**
1. System defaults — lowest priority
2. Mixin sources — in declared order, later overrides earlier
3. Explicit `overrides` in the style file — highest priority, always wins

### 6.3 Style File Naming and Location

```
src/composing/resources/styles/
  builtin/
    baroque/
      bach_chorale.json
    jazz/
      jazz_vocal.json
    blues/
      blues.json
    funk/
      funk.json
    rock/
      progressive_rock.json
  user/
    (user-contributed styles — not shipped with MuseScore)
  dimensions/
    harmonic/
    rhythm/
    bass/
    vocal/
  schema/
    style_schema.json          — JSON Schema — formal validation
    STYLE_AUTHORING_GUIDE.md   — Human-readable guide for style authors
    example_minimal.json       — Simplest possible valid style
    example_inherited.json     — Demonstrates mixin inheritance
```

### 6.4 Style Loader

The style loader scans the styles directory recursively and loads all valid JSON files.
It never references specific style IDs in code — it simply loads whatever it finds.

```cpp
class StyleLoader {
public:
    // Load all styles from the given root directory
    std::vector<StyleContext> loadAll(
        const std::filesystem::path& stylesRoot
    );

    // Load a single style file, resolving mixin inheritance
    StyleContext load(const std::filesystem::path& styleFile);

private:
    // Merge parent dimension into child, child overrides parent
    template<typename T>
    T mergeDimension(const T& parent, const T& child);
};
```

### 6.5 Initial Styles

*Terminology: these are **style instances** (individual JSON style files), distinct from the **style families** of the
§6.7 taxonomy (Baroque, swing, bebop, …). A style file is a leaf; a family is a taxonomy node a preset selects on.*

The five initial styles are chosen for maximum architectural diversity — they stress-test
the schema by requiring different parameter sets:

| Style | Primary challenge |
|-------|------------------|
| Bach Chorale | Strict voice leading rules, SATB ranges, functional harmony |
| Jazz Vocal | Extended harmony, drop voicings, lead voice concept |
| Blues | Non-functional dominant harmony, major/minor ambiguity |
| Funk | Static harmony, rhythmic primacy, horn section |
| Progressive Rock | Odd meter, modal harmony, extended form |

### 6.6 Connection to ChordAnalyzerPreferences

A `StylePrior` connection point is planned in `ChordAnalyzerPreferences`
(today a commented-out enum stub). When the style system is active, the current style populates
the analyzer's preferences — affecting which chord types are considered idiomatic,
what extensions are expected, and how scoring weights are adjusted.

### 6.7 The canonical style taxonomy (shared with the Harmonic Vocabulary)

The style vocabulary the presets select on is **one shared, hierarchical taxonomy** (common-practice / jazz / vernacular
families — Baroque, Classical/galant, Romantic; trad, swing/songbook, bebop, hard-bop, cool, modal; blues, ragtime,
gospel-soul, rock, pop, folk, barbershop) — the **same** set the Harmonic Vocabulary (§7) tags its entries with, not two
parallel vocabularies. Inclusion rule: a style is listed iff it has a **distinct functional-harmonic vocabulary** (free
jazz / atonal excluded). It is a **theory-based v1**; **empirically grounding** it — deriving the clusters *and* the
per-style weights by clustering corpora — is committed future work (`cowork_style_clustering_plan.md`): the clusters and
their feature distributions are one data-derived object, reachable for jazz/pop from **lead-sheet** corpora even where
note-level analysis ground truth is scarce. Full proposal + the surveyed corpora:
`cowork_progression_schema_dictionary.md` §6/§12, `cowork_style_clustering_plan.md`.

---

## 7. The Knowledge Base

The knowledge base contains musical theory encoded as structured data. It is shared
across all styles — styles reference knowledge base entries rather than duplicating them.

**The Harmonic Vocabulary — the queried progression & substitution component.** The Substitution Network (§7.3) and the
recurring progressions are formalised as an **independent knowledge-base component** with its own spec
(`cowork_progression_schema_dictionary.md`): a static, curated, **style-tagged** catalog of progressions, schemas, and
substitutions, with a **read-only query interface** (recognise = match a written progression to a pattern; suggest = propose a
continuation, approach, or substitution; expand = instantiate the per-degree generative slots) returning **ranked**
candidates, and
**bidirectional** by design — read forward it serves analysis (the L5 progression-schema recognizer above), read
predictively it serves a future chord-suggestion tool (§8). It is reference knowledge **queried** by the layers and by
future tools, **not a pipeline layer**. Entries carry **provenance** (established theory), not a ground-truth-validation
status — validation is the *consumer's* concern (verifiability contract, §2.15). The **voice-leading** dimension of
voice-leading-defined schemata is **out of this component** (the separate future voice-leading layer). Substitution is
not dominant-only — it operates on every functional family (tonic, pre-dominant, dominant); only the tritone substitution
is dominant-specific. **Relationship to §7.1–§7.3:** those dictionaries are the static *data*; the Harmonic Vocabulary is
the *queried component* over the progression-and-substitution part of it — it subsumes §7.3's Substitution Network as the
query surface, drawing on it as the underlying dictionary.

### 7.1 Chord Dictionary

`resources/knowledge/chord_dictionary.json`

For every chord type — all roots, all qualities, all extensions — defines:
- Interval structure (semitones from root)
- Guide tones (3rd and 7th — most harmonically essential)
- Essential tones (must include in voicing)
- Omissible tones (fifth is usually omissible)
- Color tones (extensions and alterations)
- Implied scale (chord-scale relationship from Berklee/Nettles tradition)
- Tendency tones (which notes want to resolve and where)
- TPC deltas (for enharmonic spelling — already used in ChordAnalyzer)

### 7.2 Scale and Mode Dictionary

`resources/knowledge/scale_mode_dictionary.json`

For every scale and mode — defines:
- Interval structure
- Available tensions (can be added without clashing)
- Avoid notes (create unresolvable dissonance)
- Characteristic chord types
- Connection to chord types (chord-scale relationships)
- Historical period and style associations

### 7.3 Substitution Network

`resources/knowledge/substitution_network.json`

For every chord type — defines available substitutions:
- Tritone substitution (dominant chords — root moves tritone, guide tones exchange)
- Secondary dominant (V7 of any diatonic chord)
- Backdoor dominant (bVII7 → I)
- Modal interchange (borrowed from parallel mode)
- Relative substitution (relative major/minor)
- Each substitution includes voice leading implications and style weights

### 7.4 Ornament Vocabulary

`resources/knowledge/ornament_vocabulary.json`

Style-specific ornament types:
- Baroque: trill, mordent, turn, appoggiatura, acciaccatura, Schleifer
- Jazz: approach notes, encirclement, blues bend notation
- Classical: ornament table per period

**The pedal-point class is defined VOICE-INDEPENDENTLY (user-ratified 2026-07-26; DEFERRED to its own
increment).** The ornament vocabulary carries a **pedal-point** class: a tone sustained — or continuously
restruck — against changing harmony in **any** voice, sub-labeled by position as **bass**, **internal**, or
**inverted**. This class supersedes the legacy bass-only pair of published facts, `isPedalPoint` and
`pedalBassPc`. *Why:* the legacy facts are produced by an unestablished post-pass
(`chordpostpasses.cpp:275`, the Iter-86/91 second pass specified at §5.12) that can only see the lowest
voice, and it retires with the legacy analysis path; the voice-independent class instead comes from the
joint estimator's own non-chord-tone emission categories, which do not privilege the bass. Ratified at the
pedal-point ruling of the notation-adoption increment (`cowork_notation_adoption_increment.md` §7 + §10).
**Status: DEFERRED.** It lands with the ornament-label publication, an increment of its own after the
notation switch; until then the record path leaves the pedal fields empty and the `"X ped."` annotation is a
declared gap. Tracked at `OPEN_ITEMS.md` OI-194.

---

## 8. Planned Generation Components

All generation components are behind abstract interfaces (Principle 2.2).
No generation is implemented yet — this section documents the planned design.

### 8.1 IHarmonizer

The primary generation interface. Both rule-based and future ML implementations
satisfy this interface.

```cpp
class IHarmonizer {
public:
    virtual ~IHarmonizer() = default;

    virtual std::vector<RankedChord> suggestChords(
        const MelodicContext& melody,
        const HarmonicContext& context,
        const StyleContext& style,
        const ConstraintStore& constraints
    ) = 0;

    // Every implementation must explain its suggestions in musical terms
    virtual std::string explainSuggestion(
        const RankedChord& chord,
        const MelodicContext& melody,
        const HarmonicContext& context
    ) = 0;
};

class RuleBasedHarmonizer : public IHarmonizer { ... };  // First implementation
class MLHarmonizer : public IHarmonizer { ... };          // Future ML implementation
class HybridHarmonizer : public IHarmonizer { ... };      // Rule-generated, ML-ranked
```

### 8.2 VoicingGenerator

Given a chord symbol and context, generates specific voicings appropriate to the
style and ensemble profile. The generator interface is voicing-type agnostic — the
caller specifies a style and the generator selects and applies appropriate voicing
types from the style parameters. The style JSON determines which voicing types are
used and in what proportion. Adding a new voicing type means adding it to the
generator implementation and making it available as a style parameter — the interface
does not change.

```cpp
class VoicingGenerator {
public:
    // Style determines which voicing types are used and in what proportion.
    // Never call with a specific voicing type directly — encode that in the style.
    std::vector<Voicing> generateCandidates(
        const ChordSymbol& chord,
        const StyleContext& style,
        const EnsembleProfile& ensemble,
        const Voicing& previousVoicing,    // for voice leading continuity
        const ConstraintStore& constraints
    );
};
```

**Voicing type taxonomy:**

*Tertian family — close position variants:*
- **Close position** — all voices within one octave, chord tones ascending. Baseline
  for all drop transformations.
- **Drop 2** — second voice from top dropped an octave. Primary jazz vocal voicing.
  Puerling's main tool.
- **Drop 3** — third voice from top dropped an octave. Less common, more open sound.
- **Drop 2 and 4** — second and fourth voices from top both dropped. Very open.
  Puerling's more elaborate arrangements.

*Tertian family — special cases:*
- **Shell voicings** — root, third, seventh only. Fifth omitted. Essential for jazz
  when bass instrument is present.
- **Rootless voicings** — third, seventh, and extensions only. No root. Common in jazz
  ensemble writing where the bass provides the root. Requires ensemble awareness before
  applying.
- **Chorale style** — SATB with specific doubling rules: root doubled in root position,
  leading tone not doubled, seventh not doubled. Bach chorale style. Strict and
  well-defined.
- **Spread triads** — middle note of triad displaced by an octave. Open, resonant.
  Some contemporary choral writing.

*Non-tertian family:*
- **Quartal** — stacked perfect fourths. Modal jazz, contemporary. Generated by
  stacking fourths from a starting pitch, not from a root+quality template. Requires
  quartal mode in the analyzer and musical language detector. In Prepared scope.
- **Quintal** — stacked fifths. Similar generation logic to quartal. In Prepared scope.
- **Mixed quartal/quintal** — alternating fourths and fifths. McCoy Tyner's
  characteristic sound. In Prepared scope.
- **Cluster** — adjacent semitones and seconds. Contemporary choral, avant-garde jazz.
  In Prepared scope.

*Extended tertian:*
- **Upper structure triads** — guide tones (3rd and 7th) in lower voices, a complete
  foreign triad in upper voices. The upper structure triad is selected from the
  knowledge base based on which tensions are available over the chord symbol. Requires
  chord-scale knowledge base. In Important scope.
- **Polychordal** — two complete chords superimposed. Used as a specific compositional
  effect. In Prepared scope.

**Initial implementation scope per style:**

| Style | Primary voicing | Secondary | Notes |
|---|---|---|---|
| Bach Chorale | Chorale style | — | Strict doubling rules throughout |
| Jazz Vocal | Drop 2 | Drop 2+4, close | Shell and rootless when accompanied |
| Blues | Close position | — | Simple voicings appropriate to style |
| Funk | Shell voicings | Close position | Rootless when bass is active |
| Progressive Rock | Close position | Open position | Quartal prepared but not initial |

**Style JSON voicing parameters:**

```json
{
  "voicing": {
    "close": 0.3,
    "drop2": 0.9,
    "drop2and4": 0.6,
    "shell": 0.4,
    "rootless": 0.7,
    "chorale": 0.0,
    "quartal": 0.0,
    "upper_structure": 0.4
  }
}
```

### 8.3 VoiceLeadingOptimizer

Finds the optimal sequence of voicings through a chord progression using dynamic
programming (Viterbi algorithm). Minimizes total voice leading cost subject to
hard constraints (fixed elements) and style-specific soft constraints.

**Cost function:**
```
cost = Σ(semitone distance per voice)
     + penalty for voice crossing
     + penalty for large leaps
     + bonus for common tone retention (negative cost)
     + bonus for half-step motion in inner voices (negative cost)
     + penalty for parallel octaves/fifths (style-weighted)
     + penalty for melody note not in lead voice
```

### 8.4 RuleBasedHarmonizer

The first implementation of `IHarmonizer`. Works in four stages:

1. **Melodic analysis** — phrase structure, scale degrees, climax, chromatic notes
2. **Harmonic rhythm planning** — where chord changes occur
3. **Initial chord suggestion** — most natural chord for each melody note given
   style context and key
4. **Progression coherence** — ensure functional logic, complete ii-V-I patterns,
   appropriate cadences

Chord suggestions include a creativity/temperature parameter (0.0-1.0). At 0.0,
always takes the highest-scored candidate. At higher values, samples from the
distribution — producing more surprising but still stylistically grounded choices.

### 8.5 BassLineGenerator

Generates melodically interesting bass lines appropriate to the style. Walking bass
for jazz, syncopated funk bass, melodic gospel bass, etc. The bass line has its own
melodic logic — not merely root movement through chord changes.

### 8.6 IdiomaticMaterialGenerator

Generates style-idiomatic fills and decorative material:
- Brass fills and riffs (jazz big band, funk, soul)
- Guitar riffs (rock, funk)
- Chord animation — voices moving through chord tones (Poulenc technique)

Requires gap detection — identifying structural spaces where fills are appropriate.

---

## 9. The Constraint System

### 9.1 Fix Levels

Any element of the score can be placed on a spectrum from fixed to free:

```cpp
enum class FixLevel {
    Locked,     // System never modifies this — hard constraint in optimizer
    Preferred,  // System keeps this unless strong voice leading reason to change
    Suggested,  // System's starting point, considered negotiable
    Open        // Fully available for optimization
};
```

Fixing can be applied at multiple granularities:
- Single note (specific pitch in specific voice at specific moment)
- Voice line (entire voice fixed throughout or for a passage)
- Chord (specific chord symbol fixed, voicing free — or both fixed)
- Progression (passage of bars fixed harmonically)
- Parameter (fix a characteristic rather than specific notes)

### 9.2 ConstraintStore

```cpp
class ConstraintStore {
public:
    void fix(const ScoreElement* element, FixLevel level);
    void release(const ScoreElement* element);
    bool isFixed(const ScoreElement* element) const;
    FixLevel fixLevel(const ScoreElement* element) const;

    // Fixed elements propagate influence — compute what fixing X implies
    std::vector<Constraint> propagate(const ScoreElement* element) const;

private:
    std::map<int, FixLevel> fixedElements;  // keyed by MuseScore element ID
};
```

Fixed elements are hard constraints in the voice leading optimizer — they anchor
the dynamic programming search. The optimizer guarantees never modifying them.

### 9.3 Persistence

Constraint data persists with the score as a separate file within the MSCZ archive
(see Section 13). Constraints are keyed by MuseScore element IDs which are stable
within a score. Fixed elements are visually indicated in the score view.

---

## 10. Visualization

### 10.0 Inference Demo Mode (Developer Tool)

A step-through visualization of the inference pipeline, for use by developers
during quality assurance and algorithmic development. Not shipped to end users.

**Purpose:** Allow the developer to walk through `greedyExpandSegmentation()` one
step at a time on a live score, observing every decision the algorithm makes. This
makes it possible to verify musical correctness by ear and eye rather than purely
through automated BIR metrics.

**What is shown at each step — overlaid directly on the score:**

The visualization lives on the score itself. Demo mode shows what the inferrers are doing — that is its sole purpose.

Note highlighting is painted directly on the score canvas by Qt without touching
the document.

- **Notes under consideration** — notes in the current candidate window are
  highlighted (e.g. amber). Notes excluded by staff eligibility or the non-chord-tone
  filter are highlighted in a distinct color (e.g. grey) with a small "why" label:
  "passing — duration < floor", "excluded staff", "tied continuation", etc.

- **Live chord symbols** — as each region is tentatively placed, a chord symbol
  (e.g. "G7") and Roman numeral (e.g. "V7") appear above the staff at the region's
  start tick, rendered in a distinct color (e.g. blue = tentative). These are the
  actual output of `analyzeChord` for that candidate.

- **Revisions are visible** — if a later step overrides or removes a tentative
  region (Round 2 gap-fill replaces an R1 anchor, or a region is consumed by a
  neighbor), the chord symbol on the score changes or fades out in place. The
  observer sees the algorithm "change its mind."

- **Anchor promotion** — when a region is promoted to anchor status (Round 1,
  score ≥ threshold), its chord symbol changes color (e.g. green = confirmed anchor).
  When rejected, it briefly appears in red then disappears.

- **Inline reasoning labels** — small text annotations on or near each note or
  region explain the inference: "root: G (score 1.87)", "threshold: 1.34 (PC×2)",
  "bilateral: D7 ← | → Cm", "complexity penalty ×0.75 → Gm preferred over Gmadd9",
  "head-gap: tonic prior → Cm". These labels are unobtrusive but readable on hover
  or at high zoom.

- **Temporal extension animation** — as the greedy window expands, the highlighted
  region boundary moves rightward on the score, making the "greedy" nature of the
  expansion directly visible.

- **Placed regions summary strip** — a narrow timeline strip below the score shows
  all placed regions as colored bands (green = anchor, blue = R2 fill, yellow =
  synthesized). Clicking a band jumps to that region.

**Interaction model:**

- Demo mode is triggered from a developer menu or keyboard shortcut (not exposed
  in production UI)
- "Step" button advances one candidate tick; the score updates live
- "Run to next decision" advances until the next accept/reject verdict
- "Run all" completes the full pass at adjustable speed (slider)
- All ephemeral overlays are cleared when demo mode exits
- Clicking any placed-region band in the summary strip rewinds and replays from
  that region's start tick

**Implementation approach:**

`greedyExpandSegmentation()` is refactored to accept an optional
`SegmentationStepCallback` — called after each candidate evaluation with the full
decision state. In normal (non-demo) operation the callback is null and incurs no
overhead. In demo mode, the callback updates the panel UI and blocks until the user
clicks "Step".

```cpp
struct SegmentationStepEvent {
    int candidateTick;
    int round;                          // 1 or 2
    std::vector<int> pitchClasses;      // PCs collected in window
    int winnerRoot;
    double winnerScore;
    double effectiveThreshold;
    bool passed;                        // accepted as placed region
    std::string rejectReason;           // if !passed
    std::vector<PlacedRegion> placedSoFar;
};

using SegmentationStepCallback
    = std::function<void(const SegmentationStepEvent&)>;
```

**Prerequisites:** Bridge switch (§2.10) must be complete so the live annotation
path uses `greedyExpandSegmentation()`. Demo mode drives the same code path that
produces live annotations.

**Status:** Not yet started. Planned after §2.10 bridge unification is complete.

**Premise correction, 2026-08-02 (`OPEN_ITEMS.md` OI-232, dated-note item 1).** The prerequisite and
the whole premise above are false at HEAD: the production annotation path is the joint estimator's
record path, which never calls `greedyExpandSegmentation()` (OI-175 records exactly that). So this
section specifies a developer tool for a code path that no longer runs, and "the same code path that
produces live annotations" no longer names anything live. **What the demo view should step through
instead is OPEN** — it is a design question for the joint decoder, not a documentation fix, and it is
not settled here.

---

### 10.1 IHarmonicMap Interface

All harmonic space visualizations implement this interface. Adding a new map type
means implementing the interface — the preview engine works automatically.

```cpp
class IHarmonicMap {
public:
    virtual ~IHarmonicMap() = default;

    // What chord does this position on the map represent?
    virtual std::optional<ChordSymbol> chordAt(
        const MapPosition& position
    ) const = 0;

    // What chords are harmonically adjacent to this chord on this map?
    virtual std::vector<ChordSymbol> neighboringChords(
        const ChordSymbol& chord
    ) const = 0;

    // Where on the map does this chord appear?
    virtual std::optional<MapPosition> positionOf(
        const ChordSymbol& chord
    ) const = 0;

    // Highlight these chords (substitutes, smooth voice leading targets, etc.)
    virtual void highlight(
        const std::vector<ChordSymbol>& chords,
        HighlightType type
    ) = 0;

    // Show the current score position on the map
    virtual void showCurrentPosition(
        const ChordSymbol& currentChord
    ) = 0;
};
```

### 10.2 Initial Implementation — Circle of Fifths

First harmonic map implementation. Shows key relationships and chord relationships
by fifth. Familiar to all musicians. No IP concerns. Implemented as a QML component
following MuseScore's existing UI patterns.

The circle shows:
- Current key highlighted
- Current chord highlighted
- Harmonically adjacent chords available for preview
- Clicking a chord triggers the preview engine

### 10.3 Planned — Tonnetz

Two-dimensional lattice where horizontal = perfect fifths, diagonals = major/minor
thirds. Every major and minor triad is a triangle. Adjacent triangles share two
common tones — minimum voice leading cost. Geometric distance represents harmonic
distance. No IP concerns — 19th century mathematical structure.

### 10.4 Planned — Functional Harmony Map

MTH Pro-style map based on Berklee chord-scale theory (Nettles, Levine). Positions
chords by functional region (tonic, subdominant, dominant) and shows available
tensions. Our own visual design — not a reproduction of MTH Pro's specific layout.

### 10.5 The Preview Engine

Enables clicking any chord on any map and hearing it immediately in context.

```cpp
class HarmonicPreviewEngine {
public:
    // Play a chord immediately — triggered by map interaction
    // Uses MuseScore's existing note-input preview infrastructure (low latency)
    void previewChord(
        const ChordSymbol& chord,
        const Voicing& voicing,
        const PreviewContext& context
    );

    // Play context chord — preview chord — optional resolution
    void previewProgression(
        const std::vector<ChordSymbol>& chords,
        const StyleContext& style,
        const EnsembleProfile& ensemble
    );

    void stopPreview();
    bool isPlaying() const;
};
```

**Implementation note:** Use MuseScore's note-input preview pathway (same as hearing
a note when clicking in input mode) — not the full score playback pipeline. The
full pipeline has too much latency for interactive map exploration. Inference runs
on a background thread via `QtConcurrent` to keep the UI responsive.

---

## 11. Intonation

**Status of this whole section — HELD, and a declared future CONSUMER of the analysis (user-decided
2026-07-13).** Intonation **is** a future feature: the six unbuilt items specified in §11.3a–g, together
with the tie limitation recorded there, stay on the books as a deliberate long-horizon hold, revisited at a
natural pause in the analysis work — not dropped, not scheduled. *Why the hold is strategic rather than
neglect:* the user stated the dependency that makes it so — **the intonation feature will consume the
analysis facts.** Knowing the mode, the chord, the chord's function and the progression is what lets a
just-intonation decision be made, particularly the decision in the TIME dimension between staying in tune
over time and allowing drift. Intonation is therefore a **named future consumer** of the published analysis
surfaces, and a concrete instance of the rule in §2.15 that evidence-class facts are published broadly so a
later design can recognize facts it would never have thought to ask for. Tracked at `OPEN_ITEMS.md` OI-62.

### 11.1 Tuning Systems

The intonation module supports multiple western tuning systems for playback:

| System | Description | Primary use |
|--------|-------------|-------------|
| Equal temperament | All semitones equal — modern standard | Default |
| Just intonation | Pure mathematical ratios — maximum acoustic purity | A cappella choral |
| Adaptive just | Pure intervals with managed pitch drift correction | A cappella with modulation |
| Pythagorean | Pure fifths throughout — impure thirds | Medieval, Renaissance |
| Quarter-comma meantone | Pure major thirds, slightly impure fifths | Renaissance, early Baroque |
| Well temperament | All keys usable, each slightly different — Kirnberger, Werckmeister | Bach period |

### 11.2 Per-Instrument Configuration

```cpp
enum class IntonationCapability {
    FullyFlexible,      // Can adjust pitch continuously (voices, bowed strings, trombone)
    PartiallyFlexible,  // Limited adjustment (valved brass, woodwinds)
    Fixed,              // Equal temperament — cannot adjust (piano, organ, guitar)
    Excluded            // Not relevant (unpitched percussion)
};

struct InstrumentIntonationConfig {
    IntonationCapability capability;
    bool includeInAnalysis;   // Contributes to chord identification
    bool includeInTuning;     // Receives tuning offsets
    bool anchorPitch;         // Other instruments tune to this one
    float maxAdjustmentCents; // For partially flexible instruments
};
```

Percussion instruments are excluded from both harmonic analysis and intonation.
Fixed-pitch instruments (piano) serve as intonation anchors when present.

### 11.2a Tuning System Preference

A single user preference (`composing/tuningSystemKey`) controls which tuning system
is applied across **all** tuning workflows:

- Per-note tuning from the context menu ("Tune as")
- Chord track population ("Implode to chord track")
- Region tuning ("Tune selection")

The preference is set in Preferences → Composing → Analysis ("Tuning system"
dropdown, enabled only when Roman-numeral analysis is active).  Valid keys:
`"equal"`, `"just"`, `"pythagorean"`, `"quarter_comma_meantone"`.  Default: `"equal"`.

All tuning code paths read the preference at call time via `preferredTuningSystem()`
(defined in `notationtuningbridge.cpp`), which resolves the key through
`TuningRegistry::byKey()` with a `JustIntonation` fallback if the key is unset or
unknown.  No tuning code hardcodes a specific system.

**Tonic-anchored tuning** (`tonicAnchoredTuning`, default on): when enabled, each chord
root is placed at its pure JI scale-degree position above the mode tonic rather than always
at 0¢.  This prevents syntonic-comma drift across a piece.  Implemented as a virtual
`rootOffset(keyMode, rootPc)` method on `TuningSystem` (default: 0.0¢; JI override uses
the mode-relative dev[] table).  `KeyModeAnalysisResult.tonicPc` and `.mode` are populated
by the bridge from `keyFifths` + `keyMode` using `keyModeTonicOffset()`.

**Minimize retune** (`minimizeTuningDeviation`, default off): subtracts the mean of all
attacking-note offsets per chord so the chord hovers near 0¢ while preserving internal
JI ratios.

**Annotate tuning offsets** (`annotateTuningOffsets`, default off): adds a `StaffText`
element below the chord in the score (one per chord voice, space-separated rounded cent
values) for each chord processed in Phase 2 and Phase 3 of the tuning algorithm.

**Allow split/slurring of sustained events for retuning**
(`allowSplitSlurOfSustainedEvents`, default on): lets region tuning rewrite sustained
events when a later harmonic region needs an independent playback event with a
different tuning. In TonicAnchored mode this is the region-local retuning behavior
already described above. In FreeDrift mode it means that a sustained event may be
rewritten only when the continuation's target tuning differs meaningfully from the
carried tuning. For an untied sustained note this uses split-and-slur at the region
boundary. For a tied chain, the bridge may reuse an existing tie boundary: the tie
that crosses the region boundary is removed and replaced with a slur so the later
segment can carry its own tuning. If the preference is off, the whole sustained event
remains one tuning event in both modes.

**Anchor override:** anchor expressions (`alt. rif.` and the other Italian forms)
protect the full written duration of the sustained event. An anchored sustained note is
never split, and an anchored tied chain is never segmented at a tie boundary even when
`allowSplitSlurOfSustainedEvents` is enabled. If the anchor appears on any note in the
tie chain, the chain remains one protected written-duration event.

### 11.2b Adaptive Tuning — Future Exploration

The current tuning implementation computes offsets independently per note against
a fixed interval table.  A more sophisticated approach would solve for optimal
tuning offsets *simultaneously* across all sounding voices, balancing three
competing goals: harmonic purity (intervals close to JI), ET anchoring (notes
not straying too far from equal temperament), and temporal continuity (minimizing
pitch movement between successive chords).

Several algorithmic methods exist in the literature:

- **Spring model** (deLaubenfels, ~2000–2004) — models each note as a node with
  interval springs (rest length = JI ratio) and anchor springs (pulling toward
  ET).  Anchor stiffness per voice controls how much each voice moves.  Solving
  for equilibrium is a linear system.
- **Hermode Tuning** (Mohrlok, 1990s–present; shipped in Logic Pro) — hierarchical
  interval priority (fifths first, then thirds), with a tracked center pitch to
  prevent drift.  Bass and melody receive less movement by design.
- **Weighted least-squares optimization** — generalizes the spring model as a
  cost function with per-voice weights for harmonic purity, ET anchoring, and
  temporal continuity.  Minimizing the quadratic cost yields a linear system.
- **Iterative relaxation** — a real-time-friendly variant that starts at ET and
  iteratively moves notes toward pure intervals scaled by per-voice flexibility,
  converging in 3–5 iterations.

The key design concept across all methods is **per-voice anchor weight**: outer
voices (bass, melody) get high anchor stiffness so they stay close to ET, while
inner voices absorb more of the harmonic adjustment.  Temporal anchoring adds a
penalty for pitch movement at chord boundaries, referencing the previous chord's
solved pitches — tying naturally into the harmonic rhythm regions.

This would evolve the `TuningSystem` interface from independent per-note offsets
to a simultaneous solve across all voices at each harmonic region boundary.  The
`anchorPitch` flag in `InstrumentIntonationConfig` would become a continuous
weight rather than a binary.  No implementation is planned yet — this section
records the design space for future exploration.

Another deferred design question is **which interval family to prefer for
ambiguous sonorities**.  The current shipped tuning systems use fixed lookup
tables (for example, 5-limit just intonation uses 9/5 for a minor seventh and
15/8 for a major seventh) rather than a style-aware policy that can choose
between alternatives such as 5-limit dominant sevenths versus septimal
"harmonic sevenths" (7/4), or other competing targets for altered/extended
sonorities.  This is not specific to seventh chords — similar ambiguity also
appears in tritones, minor sonorities, diminished/augmented chords, and larger
extensions.  This choice architecture should be explored later, but it is not a
current implementation target.

### 11.2c Scoring Parameter Optimization Readiness (P8c)

Both `ChordAnalyzerPreferences` and `KeyModeAnalyzerPreferences` expose a `bounds()` method that returns a `ParameterBoundsMap` — a `std::map<std::string, ParameterBound>` where each entry describes the valid range for one tunable parameter:

```cpp
struct ParameterBound {
    double min;
    double max;
    bool   isManual = false;  // true = skip during automated optimization
};
using ParameterBoundsMap = std::map<std::string, ParameterBound>;
```

`isManual = false` parameters are safe for gradient-based, grid-search, or Bayesian optimization. `isManual = true` parameters are either wired to user-visible preferences (mode priors, hysteresis margins, declared-mode penalty) or have narrow hand-tuned sweet-spots.

**Purpose:** makes the parameter space machine-readable. An optimizer can call `bounds()` to discover all tunable parameters, their valid ranges, and which are off-limits for automated tuning. This is sufficient to wire up a simple grid-search or parameter-sweep runner without manually hardcoding parameter names.

**Not yet implemented:** serialization of `ChordAnalyzerPreferences` and `KeyModeAnalyzerPreferences` to/from JSON. When the settings store is wired in, this is the next step: map each struct field to a settings key, use the `bounds()` method to enforce valid ranges.

### 11.3 Drift Management

Just intonation creates pitch drift — stacking pure intervals doesn't form a closed
system (the Pythagorean comma: 12 pure fifths overshoot the octave by 23.46 cents).

The drift manager:
- Tracks accumulated pitch drift continuously
- Identifies correction opportunities (repeated notes, unisons, rests, section boundaries)
- Distributes corrections across multiple voices to minimize audibility
- Respects a configurable drift budget per section

When a fixed-pitch instrument is present, it serves as an automatic drift correction
anchor — the choir tunes to it at every piano chord, resetting drift.

### 11.3a Zero-Sum Centering

The current tuning implementation applies fixed offsets relative to a single reference
pitch. A more musically effective approach — used by Hermode Tuning — centers the
deviations so that the sum of all tuning offsets across simultaneously sounding voices
equals zero.

**Why this matters:** When all voices are offset in the same direction, the entire chord
drifts away from equal temperament. This creates compatibility problems with fixed-pitch
instruments and with an audience's sense of absolute pitch. Zero-sum centering ensures the
chord is tuned purely internally while its average pitch matches equal temperament.

**Example — C major chord in just intonation:**

```
Raw just offsets:     C=0,   E=-14,  G=+2    sum=-12
Equal centering:      C=+4,  E=-10,  G=+6    sum=0
```

The chord is equally pure in both cases — the intervals between notes are identical. But
the centered version has zero net deviation from equal temperament.

**Implementation:** After computing raw just intonation offsets for all sounding voices,
compute the mean offset and subtract it from each voice's offset. The result is a set of
offsets that sum to zero.

**Status:** Basic (unweighted) zero-sum centering is implemented and ships as the
`minimizeTuningDeviation` user preference in `applyTuningAtNote()` and `applyRegionTuning()`.
When enabled, the arithmetic mean of all note offsets in the chord/region is subtracted from
each note's offset before it is applied. This is the §11.3a definition — "compute the mean
offset and subtract it from each voice's offset." The voice-role-weighted variant (§11.3b)
is not yet implemented; the current implementation weights all voices equally.

### 11.3b Weighted Centering by Voice Role

Pure zero-sum centering distributes the correction equally across all voices. This is
musically too democratic — the melody and bass are more perceptually prominent than inner
voices, and pitch changes in these voices are more audible.

Weighted centering distributes the centering correction inversely proportional to each
voice's musical importance. More important voices receive less correction — they stay
closer to their raw just intonation position. Less important voices absorb more correction.
The zero-sum property is preserved regardless of the weighting.

Voice role weights are defined in the style JSON:

```json
{
  "tuning": {
    "centeringWeights": {
      "melody": 3.0,
      "bass": 2.5,
      "inner": 1.0
    }
  }
}
```

Higher weight = more important = less correction applied to that voice.

**Bass weight by inversion:** The bass voice weight is further modified by the chord's
inversion, since the acoustic anchor role of the bass depends on whether it is playing the
harmonic root:

| Inversion | Bass note | Anchor strength | Weight (example) |
|---|---|---|---|
| Root position | root in bass | strong anchor | high (e.g. 2.5) |
| First inversion | third in bass | moderate anchor | medium (e.g. 1.5) |
| Second inversion | fifth in bass | weak anchor | low (e.g. 1.0) |
| Third inversion | seventh in bass | very weak | very low (e.g. 0.8) |

In inverted chords, the acoustic anchor is the harmonic root even if it is not the lowest
sounding note. The tuning system anchors to the implied root when computing centering, not
just the bass note.

**Pedal points** — a bass note sustained while harmony changes above it — receive maximum
anchor weight regardless of inversion, since they are explicitly the fixed reference in the
musical context.

Automatic melody detection is deferred. For now, voice role is determined by staff position
or explicit user assignment — not automatic detection. Per-staff override of voice role is
a future extension.

### 11.3c Note Retuning Susceptibility

Not all notes should be retuned equally freely. The system must respect that notes which
have been sounding for some time have established a pitch in the listener's ear, and
retuning them mid-sustain is audible as a wobble or portamento.

Rather than discrete protection classes, the system uses a **maximum adjustment budget** —
a continuous value in cents — that caps how much any note can be retuned at a harmonic
boundary. This budget is determined by how long the note has been sounding, modified by
musical context.

**Duration-based maximum adjustment budget:**

| Duration sounded | Maximum adjustment |
|---|---|
| < 30ms | Unlimited — ear has not registered the pitch |
| 30ms – 200ms | Up to 8–10 cents |
| 200ms – 500ms | Up to 4–5 cents |
| 500ms – 1000ms | Up to 2–3 cents |
| > 1000ms | Up to 1–2 cents |

The 30ms threshold corresponds to the minimum time for the ear to register a pitch. Below
this threshold, retuning is inaudible and the note can be placed optimally. Above it, the
budget shrinks as duration increases.

**Harmonic context modifiers** applied to the duration-based budget:

- Note is an **avoid note** in the new harmony → increase budget by 50% (the dissonance
  justifies more movement)
- Note is a **leading tone or chordal seventh** in the new harmony → increase budget by
  30% (tendency tone, movement is musically expected)
- Note is still a **consonant chord tone** in the new harmony → decrease budget by 50%
  (no musical reason to move)
- Note forms a **pure interval with another sustained note** (e.g. a perfect fifth) →
  decrease budget by 70% (breaking a locked resonance is very audible)

**Special cases:**

**Sustained perfect fifth or octave pairs:** Two notes a perfect fifth or octave apart
that have been sounding together for more than ~200ms have established a locked acoustic
resonance — their overtones are interlaced and beats have disappeared. Both notes receive
near-zero budget and effectively become anchors for the new harmony to tune around. Neither
note should be split; the new voices tune to them.

**Tied notes:** A non-partial tie chain explicitly carries a compositional instruction of
continuity. For region tuning, the entire non-partial tie chain is treated as one tuning
event. The chain must not be split. Its tuning is set from a single authority note and
protected thereafter; later harmonic regions tune around that established pitch.

The authority note is chosen as follows:

- If any note in the non-partial tie chain carries an `alt. rif.`-style anchor
  expression, the earliest such note in the chain is authoritative.
- Otherwise, the first note in the chain (the actual attack) is authoritative.

The tuning offset is computed once from that authority note's harmonic context and applied
unchanged to every note in the chain. If a user wants a sustained sound to be retuned when
the harmony changes, they should replace the tie with a slur.

**Unisons and octaves across voices:** Two or more notes sounding the same pitch class
simultaneously (in unison or octave relationship) must receive identical tuning offsets.
They are treated as a linked pair — the offset is computed once for the pair and applied to
both. Neither can be tuned independently.

**Repeated notes:** A note that was just heard in the previous beat and is now repeated —
same pitch class, adjacent position — is compared against the listener's memory of the
previous instance. Even 3–4 cents difference is audible as inconsistency. Repeated notes
receive a reduced budget until sufficient time has elapsed.

**Register sensitivity:** Notes between approximately 500Hz and 4000Hz are most sensitive
to retuning — the ear discriminates pitch most precisely in this range. Notes above or
below this range receive a slightly increased budget. The register modifier is applied as a
multiplier on the duration-based budget.

**Instrument sensitivity:** MuseScore's instrument ID system (e.g. `wind.flutes.flute`,
`voice.soprano`, `strings.violin`) is used to look up a per-instrument sensitivity value
from the knowledge base. This value scales the protection budget — more sensitive
instruments (flute, soprano) receive smaller budgets, less sensitive instruments (brass
with vibrato, electric guitar) receive larger budgets. Family-level fallbacks apply when
specific instrument IDs are not found.

```json
{
  "instrumentTuningSensitivity": {
    "wind.flutes": 0.90,
    "wind.reeds": 0.80,
    "voice": 0.85,
    "strings.bowed": 0.70,
    "brass": 0.55,
    "strings.plucked": 0.40
  },
  "defaultSensitivity": 0.60
}
```

Higher sensitivity = smaller maximum adjustment budget = more protection from retuning.

Fixed-pitch instruments (piano, organ, fretted guitar) are deferred — their handling is not
yet implemented. When implemented, they will serve as absolute anchors that other
instruments tune to, and will never receive tuning offsets themselves.

#### User-defined tuning anchors

A user can mark any note as a **tuning anchor** by attaching a MuseScore
Expression element with any of the accepted Italian forms:

| Form | Context |
|------|---------|
| `altezza di riferimento` | Full form — for performance notes and program text |
| `alt. rif.` | Standard score abbreviation (space after first dot) |
| `alt.rif.` | Compact abbreviation (no space after first dot) |
| `altezza rif.` | Semi-abbreviated form |

Italian: *altezza* = pitch, *riferimento* = reference.

**Rules for anchor notes:**
- **Zero tuning offset** — the note is left exactly at 12-TET.
- **Never split** — anchor notes are not divided at harmonic boundaries.
- **Not a FreeDrift reference** — in FreeDrift mode the anchor note is
  excluded from the drift reference hierarchy (P1/P2/P3); it sits at 0 ¢
  and other notes accumulate drift around it.
- **Excluded from zero-sum centering** — other voices in the harmonic region
  absorb the full centering correction; the anchor contributes zero.
- Applies to the specific note carrying the Expression only — subsequent notes
  on the same staff are not automatically anchored.

**Priority:** Highest. Overrides all duration-based, context-based, and
FreeDrift reference hierarchy rules.

**Keyword matching:** Case-insensitive, leading/trailing whitespace trimmed.
Exact match only — prefix/suffix text does not count.
`"ALT. RIF."`, `"Alt. Rif."`, `"  alt. rif.  "` all match `alt. rif.`.

**Implementation:**
- `kTuningAnchorKeywords` array (`std::array<const char*, 4>`) in
  `composing/intonation/tuning_system.h`
- `trimAndLowercase(std::string_view)` — inline helper for normalization
- `isTuningAnchorText(std::string_view)` — pure function for testable keyword
  matching; iterates `kTuningAnchorKeywords`
- `RetuningSusceptibility` enum in `tuning_system.h` with values
  `AbsolutelyProtected`, `Adjustable`, `Free`
- `hasTuningAnchorExpression(const Note*)` — bridge function in
  `notationtuningbridge.cpp`; scans the note's segment annotations for a
  matching Expression element on the same track
- `computeSusceptibility(const Note*)` — returns `AbsolutelyProtected` for
  anchor notes; `Free` for all others (duration-based classification is a
  future addition)

### 11.3d Tuning Session State

The tuning system maintains session-only state that is not persisted to the MSCZ file and
resets when the score is closed.

**Global session parameters:**

```cpp
class TuningSessionState {
public:
    // Global sensitivity — scales maximum adjustment budget across all voices
    // 1.0 = default, < 1.0 = more aggressive, > 1.0 = more conservative
    float globalSensitivity = 1.0f;

    // Global depth — scales tuning offsets between ET and full just intonation
    // 0.0 = equal temperament, 1.0 = full just intonation offsets
    // 0.6–0.7 recommended when mixing with fixed-pitch instruments (HMT guideline)
    float globalDepth = 1.0f;
};
```

**Sensitivity** scales the maximum adjustment budget. Higher sensitivity means smaller
budgets across all protection tiers — more conservative retuning.

**Depth** scales the final tuning offsets linearly between equal temperament (0%) and the
computed just intonation values (100%). Useful when performing alongside a piano — HMT
recommends 60–70% depth in mixed ensembles to reduce the mismatch between adapted and
fixed-pitch instruments.

Both parameters are exposed as sliders in the tuning preferences panel. They are
session-only — not persisted.

**Future extension:** Per-staff sensitivity and depth overrides, accessible via right-click
on the staff name. This will also be session-only when implemented. Visual indicator on the
staff label when an override is active.

### 11.3e The Complete Tuning Algorithm

Putting the above together, the tuning algorithm for a harmonic region boundary proceeds as
follows:

**Step 1 — Classify all sounding notes by susceptibility**
For each sounding note, compute its maximum adjustment budget from: duration sounded,
harmonic context in the new chord, register, instrument sensitivity, and special cases
(tied, unison pair, sustained fifth/octave pair).

**Step 2 — Identify anchors**
Notes with near-zero budget — sustained perfect fifth/octave pairs, tied notes, very long
sustained notes — become anchors. They do not move. The new harmony must tune around them.

**Step 3 — Compute raw just intonation offsets**
For all non-anchor notes, compute the ideal just intonation offset given the new chord and
the voice's role within it. Apply the depth scalar.

**Step 4 — Apply weighted zero-sum centering**
Compute the weighted centering correction for the non-anchor notes. Voice role weights and
bass inversion weight determine the distribution. Anchors are excluded from the centering
calculation. Apply the correction so the sum of all non-anchor offsets equals zero.

**Step 5 — Clamp to susceptibility budget**
Clamp each note's final offset to its maximum adjustment budget. If a note's ideal offset
exceeds its budget, it moves only as far as its budget allows. The zero-sum property may be
slightly violated by clamping — this is acceptable; the priority is avoiding audible
retuning artifacts.

**Step 6 — Apply sensitivity scalar**
Multiply all offsets by the global sensitivity parameter.

**Step 7 — Determine which notes need splits**
Notes with offsets exceeding `kEpsilonCents` (0.5 cents) and not protected by anchor
semantics may need independent playback events. Untied sustained notes use the normal
split-and-slur mechanism. For tied sustained events, existing tie boundaries may be reused
as segmentation points when preference and harmonic context allow; otherwise the tie chain
remains one event and receives one chain-level tuning. Anchors override both cases and
protect the full written duration from segmentation. Apply the split-and-slur mechanism
(§11.4) for all notes requiring independent playback events.

**Step 8 — Apply tuning offsets**
Write final cent values to all notes via `undoChangeProperty(Pid::TUNING, ...)`.

### 11.3f FreeDrift Mode

The `tuningMode` preference selects one of two high-level drift behaviors:

**TonicAnchored (default):** Each harmonic region independently computes offsets
relative to the mode tonic. The chord root is placed at its JI scale-degree
position; individual chord tones are offset relative to that root. Sustained
notes crossing region boundaries are split-and-slurred so each segment receives
the correct offset for its region. Drift does not accumulate across regions.

**FreeDrift:** Tuning offsets accumulate naturally across harmonic regions.
The reference pitch for each region is determined by a priority hierarchy:

| Priority | Source | Meaning |
|----------|--------|---------|
| P1 | Held note from previous region | Drift reference: existing tuning of the held note |
| P2/P3 | Bass note / analyzer root | No prior drift — fresh baseline (adjustment = 0) |

When a held note bridges regions (P1), the drift adjustment is:
```
driftAdjustment = heldNote.tuning() − desiredOffset(heldNote.ppitch())
```
All notes in the new region receive `desiredOffset(pitch) + driftAdjustment`.

**`alt. rif.` anchor notes in FreeDrift:** Unlike in TonicAnchored mode (where
an anchor forces all notes back to a 0 ¢ reference), in FreeDrift an anchor note
is pitched *at the current drift level* — i.e. it receives `finalOffset(pitch)`
exactly like any other note. It "confirms where we have drifted to" without
pulling other notes back to 12-TET. Anchor notes are excluded from P1 held-note
selection and annotated with a `*` suffix in cent annotations.

**Key differences from TonicAnchored:**
- Held notes carry their existing tuning into the new region first, providing the
  drift baseline for other voices.
- If `allowSplitSlurOfSustainedEvents` is off, sustained events remain whole.
- If `allowSplitSlurOfSustainedEvents` is on, a sustained event may be rewritten
  only when the continuation target differs from the carried tuning. This applies
  to both untied sustained notes and tied chains at existing tie boundaries.
- When no held note exists (no P1 candidate), drift resets to 0.0 (same
  as a fresh TonicAnchored computation without the rootOffset term).

**Drift boundary annotation (`annotateDriftAtBoundaries`, default off):**
When enabled together with FreeDrift, a `StaffText` is inserted above the first
eligible staff at each harmonic region boundary whenever |driftAdjustment| ≥ 0.5 ¢,
showing the accumulated pitch drift, e.g. `d=+3` or `d=-2`. This is independent of
the per-note `annotateTuningOffsets` toggle. A future drift-reset marker
(see `backlog_drift_reset.md`) will allow composers to insert deliberate
intonation resets at structural boundaries.

**Implementation:** `applyRegionTuning()` in `notationtuningbridge.cpp`,
controlled by `cfg->tuningMode()`. The drift computation happens between
the minimizeRetune (meanShift) calculation and the Phase 2 note-assignment loop.

### 11.3g Harmonic Priority (Just Intonation Only)

**Status: Design note.** The `HarmonicPriority` enum and `harmonicPriority()`
preference are not yet implemented. The current JI implementation uses a fixed
5-limit lookup table throughout.

#### Scope

Harmonic priority is only meaningful for just intonation family tuning systems.
For all other implemented systems the interval sizes are uniquely determined by
the system definition and no choice is available:

| Tuning system | Interval sizes | Harmonic priority |
|---------------|----------------|-------------------|
| Equal temperament | Fixed by definition | Not applicable |
| Pythagorean | Uniquely determined by stacking 3/2 fifths | Not applicable — equivalent to "Fifths first" JI |
| Quarter-comma meantone | Uniquely determined by tempering fifths for pure 5/4 thirds | Not applicable |
| Werckmeister / Kirnberger | Uniquely determined by their fixed compromises | Not applicable |
| Just intonation | Multiple legitimate pure ratio interpretations per interval | Applies |
| Adaptive JI (future) | JI ratios simultaneously optimized — same ambiguity | Applies |

Note that Pythagorean tuning is mathematically equivalent to the "Fifths first"
harmonic priority choice in just intonation — both derive all intervals by
stacking pure 3/2 fifths. They are the same system under different names.

The `HarmonicPriority` preference control must be hidden or disabled in the UI
whenever a non-JI tuning system is active.

#### Why the Choice Exists in JI

In just intonation, every interval has multiple legitimate pure ratio
interpretations derived from different prime factors. The choice of which primes
to include as primary consonances determines the character of the tuning:

| Interval | 3-limit (Pythagorean) | 5-limit (classical JI) | 7-limit (harmonic series) |
|----------|-----------------------|------------------------|---------------------------|
| Major third | 81/64 (+8¢) | 5/4 (-14¢) | 5/4 (-14¢) |
| Minor third | 32/27 (-6¢) | 6/5 (+16¢) | 6/5 (+16¢) |
| Perfect fifth | 3/2 (+2¢) | 3/2 (+2¢) | 3/2 (+2¢) |
| Minor seventh | 16/9 (-4¢) | 9/5 (+18¢) | 7/4 (-31¢) |
| Tritone | 729/512 (+12¢) | 45/32 (-10¢) | 7/5 (-17¢) |
| Augmented sixth | — | 225/128 (+41¢) | 7/4 (-31¢) |

Moving from 3-limit to 5-limit: thirds and sixths change dramatically (major
third drops 22¢). The fifth is unchanged.

Moving from 5-limit to 7-limit: sevenths and tritones change dramatically
(minor seventh drops 49¢). Thirds and fifths are unchanged.

The prime-limit choice implicitly sets the priority when simultaneous pure
intervals conflict — four-note chords cannot have all intervals pure
simultaneously, so the system must decide which intervals to prioritize:

- **5-limit:** fifths and thirds are primary; sevenths are derived and end up
  slightly impure.
- **7-limit:** fifths, thirds, and sevenths are all primary; other
  relationships absorb the remaining impurity.

#### The Preference

A single preference controls which prime limit is used as the primary
consonance target:

```cpp
enum class HarmonicPriority {
    /// Pure fifths only — Pythagorean ratios for all intervals.
    /// Bright, tense thirds. Historically appropriate for medieval
    /// and Renaissance music. Mathematically equivalent to the
    /// Pythagorean tuning system.
    FifthsFirst,

    /// Pure fifths and thirds — 5-limit just intonation.
    /// Warm, consonant triads. Standard for classical choral
    /// and orchestral JI. Default.
    ThirdsAndFifths,

    /// Full chord purity — 7-limit harmonic series.
    /// All chord tones (including sevenths) derived from pure
    /// harmonic partials. Seventh chords lock into zero-beat
    /// resonance. Appropriate for barbershop, close vocal harmony,
    /// natural brass ensemble, some jazz vocal.
    FullChordPurity,

    /// Context-dependent — follows the active style preset.
    /// The style preset maps chord function to prime limit:
    /// dominant seventh chords may use 7-limit while triads
    /// use 5-limit, etc.
    Automatic,
};
```

**Default:** `ThirdsAndFifths` — preserves current behavior (5-limit lookup
table) for all existing users.

#### UI Presentation

Exposed in **Preferences → Composing → Intonation** as a radio button group,
visible only when the active tuning system is Just intonation or Adaptive JI:

```text
Harmonic priority:  (only shown for Just intonation)
  ○ Fifths first       — pure fifths, Pythagorean thirds
  ● Thirds and fifths  — pure triads (standard)
  ○ Full chord purity  — harmonic series, all chord tones pure
  ○ Automatic          — follows style preset
```

#### Dominant Seventh Character

When `FullChordPurity` or `Automatic` is active, a second sub-preference becomes
relevant. The minor seventh in a dominant seventh chord has a unique musical
function — it is both a primary consonance (7-limit) and a functional dissonance
(resolution pull toward the tonic). The user may want to control this tension
independently:

```cpp
enum class DominantSeventhCharacter {
    /// Wide seventh (9/5, +18¢) — maximum tension, strong
    /// resolution pull toward tonic. Appropriate for functional
    /// harmony where V7 → I resolution is the goal.
    Tense,

    /// Pure harmonic seventh (7/4, -31¢) — zero-beat resonance,
    /// floating quality. Appropriate for static dominant color,
    /// barbershop tag chords, natural brass sonority.
    Natural,

    /// Pythagorean seventh (16/9, -4¢) — close to equal temperament.
    /// Neutral character, minimal deviation from 12-TET.
    Neutral,
};
```

**Default:** `Natural` when `FullChordPurity` is active.

This control only affects the minor seventh of dominant seventh chords — not the
minor seventh in minor seventh chords (`Dm7`), half-diminished chords, or other
contexts where the seventh does not carry dominant function. Other intervals
(thirds, fifths, extensions) are not affected by this preference.

UI: shown as a sub-option beneath `FullChordPurity` and `Automatic` in the
harmonic priority group, enabled only when those options are selected.

#### Relationship to the Generalized Tuning Algorithm

The `HarmonicPriority` preference is the user-facing control for a deeper
architectural choice: which prime limit to use when computing just intonation
ratios.

The full generalized algorithm (§11.2b, deferred) would:

- Identify each note's harmonic function within the chord.
- Select the prime limit based on `HarmonicPriority` and chord function.
- Compute the canonical ratio via shortest lattice path (minimum Tenney height
  within the chosen prime limit).
- Resolve conflicts between simultaneously sounding notes via the simultaneous
  optimizer.
- Apply context modifiers (dominant tension, leading-tone pull, resolution
  target).

The current fixed 5-limit lookup table is a degenerate case of this algorithm —
it hardcodes `ThirdsAndFifths` with no context modifiers and no simultaneous
optimization. The `HarmonicPriority` preference adds the first degree of freedom
without requiring the full algorithm to be implemented.

#### Implementation Sequence

- Add `HarmonicPriority` and `DominantSeventhCharacter` enums to
  `tuning_system.h`.
- Add `harmonicPriority()` and `dominantSeventhCharacter()` to
  `IComposingAnalysisConfiguration`.
- Wire through `ComposingConfiguration` → `composingpreferencesmodel` → QML
  (same pattern as `TuningMode`).
- In `applyRegionTuning()` and `applyTuningAtNote()`, branch on
  `harmonicPriority()` when selecting the ratio for each interval:
  - `FifthsFirst`: use Pythagorean ratios throughout.
  - `ThirdsAndFifths`: use the current 5-limit table (no change).
  - `FullChordPurity`: use 7-limit ratios for sevenths and tritones, 5-limit
    for thirds and fifths, and apply `DominantSeventhCharacter` for dominant
    seventh context.
  - `Automatic`: consult the style preset for chord-type → prime-limit mapping.
- UI: radio group in `ComposingAnalysisSection.qml`, visible only when tuning
  system is JI or Adaptive JI.
- Validate on a cappella choral scores with known tuning practice (barbershop
  corpus when available).

### 11.4 Score Mutation for Tuning Application

Applying a non-equal temperament writes cent deviations to individual notes via
`Note::undoChangeProperty(Pid::TUNING, cents)`.  For notes that attack exactly at
the target tick this is a direct property change.  Sustained notes — notes that
started before the target tick but are still sounding — require score mutation
because tuning is a single value per note and the note's harmonic role may differ
from when it first attacked.

#### Split-and-slur approach

A sustained note that needs a different tuning at the target tick is split there
into two notes connected by a slur.  The first half (note_A) keeps its existing
tuning.  The second half (note_B) receives the offset for its role in the current
chord.

A **slur** (not a tie) connects the two halves.  This is a deliberate choice:
MuseScore's playback engine treats tied notes as one continuous sound with a single
tuning value, so a tie would silently discard note_B's tuning.  A slur produces two
independent playback events with legato articulation, allowing each half to carry
its own tuning offset.

The split is **visible** — the score shows two shorter notes connected by a slur.
This is the simplest correct approach and is fully undoable via MuseScore's standard
undo system.

**Backlog:** An alternative invisible-voice strategy (silent original + invisible
playing pair in a spare voice) was designed and prototyped but deferred.  It requires
a UI indicator for tuning-applied notes before it is practical.  See
`backlog_invisible_split.md`.

#### Split threshold

A split is only performed when the difference between the note's current tuning and
the desired tuning exceeds `kEpsilonCents` (0.5 cents).  This avoids unnecessary
score mutations for inaudible differences.

#### Slur chain management

When successive splits are applied to the same note (e.g. a whole note in 4/4 with
quarter-note chord changes), existing forward slurs are transferred from the
shortened original to the end of the new note_B chain.  This produces a sequential
slur chain (1→2→3→4) rather than a fan pattern (1→2, 1→3, 1→4).

#### Note collection filter

Chord analysis filters notes with `visible = true` and `play = true`, excluding
both silent notes and any future invisible tuning artifacts from the pitch-class
collection.

#### Idempotency

After a split, note_A ends exactly at the target tick (`noteEnd == anchorTick`),
which is excluded by the `noteEnd <= anchorTick` guard in the lookback loop.
Re-running the operation on the same target tick does not produce additional splits.
Phase 2 (attack-note tuning) handles re-tuning of notes at the anchor tick,
including note_B from a previous split.

#### Bridge function

Declared and defined in `mu::notation` (not in the composing module — requires `Note*`):

```cpp
// notation/internal/notationtuningbridge.h
namespace mu::notation {
bool applyTuningAtNote(const mu::engraving::Note* selectedNote,
                       const mu::composing::intonation::TuningSystem& system);
} // namespace mu::notation
// defined in src/notation/internal/notationtuningbridge.cpp
```

The context menu path passes the tuning system explicitly (resolved from the user
preference at menu-build time).  Other callers (chord track population, region
tuning) use `preferredTuningSystem()` to read the preference at call time.

The caller is responsible for undo grouping (`startCmd`/`endCmd` or the
`NotationInteraction::startEdit`/`apply` pattern).  The function does not manage
its own undo scope.

Returns `false` when the selected note is invisible (no-op) or when fewer than 3
distinct pitch classes are sounding (insufficient data for chord identification).

### 11.5 Region Analysis and the Chord Track

**Status: Implemented, and running the RECORD path since the notation switch (2026-07-27).**
`populateChordTrack()` is declared and defined in
`notation/internal/notationimplodebridge.h/.cpp` (`mu::notation` namespace) and is exposed as the
"Implode to chord track" action in the Tools menu (see §12.1b). **Corrected 2026-08-02
(`OPEN_ITEMS.md` OI-232, dated-note item 2):** what the action runs is the joint estimator's record
path — `produceNotationRecord` → `analyzeSectionFromRecord` → `emitImplodedChordTrack`
(`notationimplodebridge.cpp:1409-1431`) — not `analyzeHarmonicRhythm()`, which is now the legacy
arm's boundary source behind `useJointNotationRecord == false` (`:1434-1441`). A second, smaller
correction of the same date: `analyzeHarmonicRhythm()` is DECLARED in
`notation/internal/notationcomposingbridge.h:161` but DEFINED in
`notation/internal/notationharmonicrhythmbridge.cpp:69`, not in `notationcomposingbridge.cpp`. **The
description of the region machinery below remains accurate for the legacy arm** and is retained as the
record of what that arm does.

Single-note analysis (status bar display, single-chord tuning) is the foundation.
Region analysis extends this to a time range, producing a complete harmonic analysis
with chord symbols, roman numerals, and an optional note reduction across an entire
passage.

#### User interaction — selection-based targeting

There is no dedicated staff type or property for the chord track.  The user's
**selection determines the target**:

1. **Select a range on any staff** and invoke "Implode to chord track."
2. The system analyzes all **other** non-hidden tonal staves within that time range.
3. The selected region is cleared and populated with the harmonic reduction.

The target staff is excluded from the analysis input — it is the output, not a
source.  This prevents feedback loops when re-running the analysis.

**Any existing content in the selected region is overwritten.**  Re-analysis after
score edits simply selects the same range and runs again.  If the user wants to
preserve a previous analysis, they can undo or copy it elsewhere first.

#### On-demand staff creation

If no suitable target staff exists yet, the action offers to **create one**:

1. Opens MuseScore's standard Add Instruments dialog — the user picks whatever
   instrument they want (piano, organ, a single-line sketch staff, etc.).
2. The new part is inserted (e.g., at the bottom of the score).
3. A default name like "Chord Track" is suggested (soft hint for future automation,
   not enforced).
4. The selected tick range is applied to the new staff and population proceeds.

The instrument choice is the user's.  The system adapts its output to what the
staff supports (see below).

#### Adaptive output by staff type

- **Grand staff** (e.g., piano, organ): root on the bass staff, upper-structure
  chord tones on the treble staff, chord symbols above, roman numerals below.
  This is the richest output — a full keyboard reduction.
- **Single staff** (e.g., treble clef sketch): chord symbols and roman numerals
  only (no note reduction), or a single-staff reduction with root and upper
  structure combined.  The user's instrument choice drives the output.

#### Harmonic rhythm detection

The region analysis scans **all non-hidden tonal staves** (excluding the target
staff) within the selected time range, left to right, to identify every tick
where the sounding pitch-class set changes — i.e. where any instrument starts or
stops a note.  Each such tick is a potential chord boundary.

Chord analysis runs at each boundary tick. In the default smoothed mode,
consecutive boundaries that produce the **same root and quality** are collapsed into a
single harmonic region, and sub-quarter-note fragments are absorbed so tuning and other
range operations do not overreact to ornaments. Chord-staff population uses the
preserve-all mode instead: every detected harmonic event is kept, even when adjacent
events share root and quality, and sustained carry-in notes still contribute at the new
region start.

The result is a sequence of harmonic regions, each with:
- Start tick and end tick (duration = harmonic rhythm)
- Chord analysis result (root, quality, extensions)
- Key/mode analysis result

#### Chord track population (grand staff)

The selected region is cleared and populated from the region sequence:

**Treble clef (staff 1):** Upper-structure chord tones in close position, placed
in the C4–C5 range.  Duration matches the harmonic region.  When voicing analysis
is available (future), the inferred voicing (drop 2, spread, etc.) replaces the
close-position default.

**Bass clef (staff 2):** Root note only, showing bass motion.  Placed in a
natural bass register (C2–C3 range).

**Chord symbols** (`HarmonyType::STANDARD`) attached above the treble staff —
controlled by the "Write chord symbols to staff" preference.

**Chord function notation** attached below the treble staff — either
`HarmonyType::ROMAN` (Roman numerals) or `HarmonyType::NASHVILLE` (Nashville
numbers), selected by the "Chord function notation" preference (None / Roman
numerals / Nashville numbers).  Roman and Nashville are mutually exclusive on
the staff because they encode identical information; displaying both would be
redundant and legibility-destroying.

**Key/mode annotations** written as staff text at key region boundaries —
controlled by the "Write key/mode annotations" preference.

The instrument's sound makes the harmonic reduction audible on playback — the
composer can audition the harmonic progression independent of the orchestration.

#### Close-position reduction algorithm

Given a chord analysis result with root pitch class and chord tones:

1. Sort pitch classes ascending from the root.
2. Place the root in the bass clef at C2–C3 (nearest octave to middle of range).
3. Stack remaining pitch classes above C4, each ascending from the previous, within
   one octave.  This produces close-position voicing.
4. When voicing inference is implemented (Phase 3), the inferred voicing replaces
   step 3.  The algorithm becomes: "given these pitch classes and the detected
   voicing type, produce the appropriate spacing."

This mirrors how arrangers think — the chord track is a **keyboard reduction** of
the full score, showing harmony and rhythm stripped of orchestration.

#### Relationship to MuseScore's chord symbol realization

MuseScore's existing `Score::cmdRealizeChordSymbols()` converts `Harmony` elements
into notes on a single track.  It supports voicing types (close, drop 2, 3-note,
4-note, 6-note) but places all notes including the bass on one staff.

Our approach differs in two ways:

1. **Grand staff separation** — root on the bass staff, upper structure on treble.
   This matches standard lead-sheet layout and is more readable.
2. **Analysis-derived** — their flow is symbol → notes (user typed the chord,
   system voices it).  Ours is notes → symbol → reduction-notes (system infers the
   chord from sounding notes, then produces the reduction).  The existing
   `RealizedHarmony` and `Voicing` infrastructure may be useful when building our
   voicing generator, but the analysis-first workflow is new.

#### Rest analysis

Single-note analysis requires a selected note as the anchor.  Region analysis does
not — it analyzes at arbitrary ticks based on the harmonic rhythm.  A new entry
point `analyzeHarmonicContextAtTick(Score*, Fraction tick, ...)` provides analysis
without requiring a note anchor.  It uses the same collection and analysis logic,
just without the "selected note" starting point.  This also enables annotation at
ticks where the target staff has a rest.

#### Relationship to intonation

The chord track and intonation are **independent workflows** that share the chord
analysis engine but have no other coupling:

| | Chord track ("Implode to chord track") | Intonation |
|---|---|---|
| **Purpose** | Composition and analysis tool | Playback quality |
| **Output** | Visible: notes, chord symbols, chord function notation (Roman or Nashville), key annotations | Invisible: cent offsets on existing notes |
| **Target** | Any staff the user selects (or creates on demand) | Any staff the user selects |
| **Requires** | Range selection on the target staff | Any note or range selection |
| **Score impact** | Overwrites target region with reduction | Split-and-slur on sustained notes only |

Neither workflow depends on the other.  A user can intonate without a chord track,
and can populate the chord track without applying tuning.  Both use the same
`analyzeHarmonicContextAtTick` entry point internally and the same user-preferred
tuning system (§11.2a).

#### Additional Chord Track Annotations — Planned

The following annotations are planned for the chord track. All derive from data already
computed or planned in the analysis engine — no new analytical components are required
beyond what is already described in this document.

**Non-diatonic chord highlighting** (ready to implement)

Chords where `ChordAnalysisResult.diatonicToKey` is `false` receive distinct visual
treatment — a different color or border on the chord block. Makes borrowed chords,
secondary dominants, and chromatic passing chords immediately visible without requiring
the user to read each Roman numeral. No additional analysis required — the flag is already
computed.

**Relative and parallel key relationships** (ready to implement)

When the inferred key changes, the key label annotation includes the relationship to the
previous key:

- Same `keySignatureFifths`, different `isMajor` → "→ relative minor" / "→ relative major"
- Same `tonicPc`, different `isMajor` → "→ parallel minor" / "→ parallel major"
- `keySignatureFifths` differs by ±1 → "→ dominant key" / "→ subdominant key"
- Other differences → circle of fifths distance stated: "→ mediant (E major)"

All relationships are pure arithmetic on `keySignatureFifths`, `tonicPc`, and `isMajor` —
no additional analysis required.

**Key stability indicator** (depends on §5.7 normalized confidence)

The confidence of the key/mode inference is indicated through staff text annotation:

- Confidence above 0.8 — no annotation (confident, label stands alone)
- Confidence 0.5–0.8 — question mark appended to key label: "D Dorian?"
- Confidence below 0.5 — suppress key-dependent chord-track annotations rather than printing a tentative label

The chord-track writer uses the same thresholds to reduce misleading downstream output:

- Roman/Nashville function labels are written only when confidence is at least 0.5
- Key signatures, modulation relationship labels, pivot labels, borrowed-chord markers,
  and cadence markers are written only when confidence is at least 0.8

Requires normalized confidence scores (§5.7) to be implemented first. Until then, raw
scores from `KeyModeAnalysisResult` can be used with approximate thresholds as a temporary
measure.

**Key distance / borrowed chord annotation** (ready — basic version)

When a chord is non-diatonic to the current inferred key, a small annotation identifies
which nearby key it belongs to — making the borrowing relationship explicit.
Implementation: for each non-diatonic chord, compute which keys contain it as a diatonic
chord, then select the closest key by circle-of-fifths distance to the current inferred
key. Requires the chord dictionary and scale/mode dictionary (§7.1, §7.2) to be populated.

**Cadence markers** (basic version ready, improved with phrase analysis)

Detected cadences annotated above the chord track staff at phrase boundaries:

- Authentic (V→I): Roman numeral sequence in the inferred key
- Half cadence (→V): ending on dominant
- Deceptive (V→vi): dominant resolving to submediant
- Plagal (IV→I): subdominant to tonic

Basic detection uses a heuristic: cadential chord pairs followed by a significant harmonic
change (new key region, long held chord, or rest). Full accuracy requires phrase structure
analysis (planned but not yet implemented). Basic version is implementable now from the
harmonic rhythm regions already computed.

**Modulation path annotation** (basic version ready)

At key region boundaries, annotate the pivot chord when one exists:

"pivot: IV in G → ii in D"

Implementation: the last chord before the key boundary that is diatonic to both the old
and new key is the pivot. `formatRomanNumeral()` is called twice — once with the old key
context, once with the new — to produce both Roman numerals. When no pivot chord exists
(direct chromatic modulation), annotate as "direct modulation". Enharmonic reinterpretation
detection is a future refinement.

### Annotate path annotation layers (Roman numeral mode)

When the user selects a region and runs "Annotate to chord track" in Roman
numeral mode, the following layers are written as StaffText annotations:

- Chord symbols
- Roman numerals (with chromatic/borrowed labels: ♭VII, ♭III etc.)
- Cadence markers (PAC, HC, DC, PC) — **implemented** (Session 14);
  uses `detectCadences()` in `notationcomposingbridgehelpers.cpp`
- Pivot chord labels — **implemented** (Session 14); uses
  `detectPivotChords()` in `notationcomposingbridgehelpers.cpp`
- Tonicization labels (V/V, V/ii, V/IV etc.) — **NOT YET IMPLEMENTED**
  (deferred; no `relativeRoot`/secondary-dominant field in
  `ChordFunction`; requires standalone implementation first)
- Augmented sixth chord labels (It+6, Fr+6, Ger+6) — **NOT YET
  IMPLEMENTED** (deferred; no aug-sixth classifier in composing module;
  requires standalone implementation first)

Nashville annotation mode emits chord symbols and Nashville numbers only.
No cadence markers, no pivot labels, no tonicization labels.

**Cadence detection** (`detectCadences`): pairs of consecutive in-selection
regions are examined. PAC = V→I or viio→I with assertive key confidence
(≥ 0.8) on both. PC = IV→I. DC = V→vi. HC = last in-selection region is
a dominant (degree V or viio). Label is placed at the resolution tick; if
the resolution region is in lookahead (past `selectionEndTick`), the label
is placed at the preparatory chord's tick instead. One harmonic region of
read-only lookahead is used.

**Pivot detection** (`detectPivotChords`): scans for assertive key
transitions (consecutive regions with different `keyTonicPc` or `keyMode`).
The new key is confirmed by finding at least one additional assertive region
within `kMaxPivotLookaheadRegions = 8` regions past the boundary. The pivot
chord is the last in-selection chord diatonic to both the old and new key.
The pivot label format is `vi → ii` (U+2192 RIGHT ARROW, no "pivot:" prefix,
no key-name context). Analysis window extended by up to
`kMaxPivotLookaheadRegions × 1 whole note` past `selectionEndTick` in Roman
numeral mode; no annotations written outside the selection boundary.

**Annotation color policy:**

Interactive annotate path (human use): annotations written in score default
color (black). Publication-ready, indistinguishable from manually entered
symbols. No user preference exposed.

Automated pipeline (`batch_analyze` headless): annotations written in red,
hardcoded in `tools/batch_analyze.cpp`. Never exposed to human user. Used by
`auto_review.py` to filter our inferred annotations from pre-existing score
content by color comparison.

#### Future Extensions — Chord Track

The following are possible future extensions. No implementation is planned.

**Tension curve strip** — a small graph below the chord track staff showing harmonic
tension over time, derived from voice leading complexity and distance from tonic. Connects
to the tension curve editor (§12.4) when implemented.

**Phrase structure markers** — bracket notation showing detected phrase beginnings and
endings. Requires phrase structure analysis component.

**Harmonic rhythm emphasis** — visual weight on chord blocks proportional to harmonic
rhythm density, making acceleration toward cadences immediately visible.

**Actual bass line overlay** — optional display of the original score's bass voice rather
than just the chord root, revealing bass line character (walking bass, pedal point, chromatic
descent).

### 11.6 Region Intonation

Intonation over a region extends the single-note tuning workflow (§11.4) to a
time range. No dedicated staff is needed — intonation is a playback-only concern
that does not add visible notation beyond the split-and-slur artifacts.

For ordinary untied notes, the user selection defines exactly what gets retuned.
For non-partial tie chains, the chain is treated as an indivisible tuning event:
if any note in the chain intersects the selected region, the tuning offset is
applied to the entire chain, including members outside the selected span.

#### Selection-based scoping

The selection determines the scope:

- **Single note** — tune that note using the harmonic context at its tick (the
  existing single-note workflow from §11.4).
- **Range on one or more staves** — detect harmonic rhythm within the range,
  compute a tuning plan per region, split and tune all notes accordingly.
- **Whole staff or Ctrl+A** — same as range, applied to the full extent.

In every case the user selects what they want tuned; the tuning system is read from
the user preference (§11.2a).  The analysis engine figures out the harmonic context
at each tick, and the tuning logic handles the rest.

For non-partial tie chains, the tuning annotation is placed at the first note in the
chain even when that note lies outside the visible selection. This makes the one-event
semantics explicit in the score.

#### Algorithm

1. **Harmonic rhythm detection** — same scan as §11.5: identify every tick in the
   selected time range where the sounding pitch-class set changes across all
   non-hidden tonal staves.  Run chord analysis at each boundary.  Collapse
   consecutive same-chord regions.
2. **Compute tuning plan** — for each harmonic region and each sounding note in the
  selected staves, compute the desired tuning offset. For non-partial tie chains,
  choose the chain authority note (earliest anchor-marked note, otherwise first note
  in the chain), compute the offset once from that authority note's harmonic context,
  and reuse that same offset for every note in the chain. Compare against each note's
  current tuning. Record which notes need changes and which sustained untied notes
  need splits.
3. **Execute splits** — because all boundaries are known upfront, the complete
   split plan is computed before any mutations.  Each sustained note crossing a
   region boundary is split-and-slurred once (§11.4 mechanics).  No cascading
   splits.
4. **Apply tuning** — set cent offsets on all notes (attack and newly-split)
  via `undoChangeProperty(Pid::TUNING, ...)`. If a non-partial tie chain intersects
  the selected range, the final chain offset is written to every note in that chain,
  even when some members lie outside the selection.

The entire operation is one undo group.

#### Entry points

```cpp
// notation/internal/notationtuningbridge.h
namespace mu::notation {
bool applyRegionTuning(mu::engraving::Score* score,
                       const mu::engraving::Fraction& startTick,
                       const mu::engraving::Fraction& endTick);
} // namespace mu::notation
// defined in src/notation/internal/notationtuningbridge.cpp
```

Called from `NotationInteraction::tuneSelection()`, which determines the tick range
from the current selection (range, single note → note span, or full score fallback).
Exposed as the `"tune-selection"` action in the Tools menu.

#### Shared split helper

The split-and-slur logic used by both single-note tuning (§11.4 Phase 3) and region
tuning is factored into a template helper:

```cpp
template<typename TuningFn>
bool splitAndTuneChord(Score* sc, Chord* chordMut,
                       const Fraction& splitTick, TuningFn tuningFn);
```

This shortens the original chord at the split tick, creates a continuation chord
bridged by a slur, and applies the caller-supplied tuning function to the
continuation's notes.  Both `applyTuningAtNote` and `applyRegionTuning` use this
helper, eliminating duplicated mutation logic.

---

## 12. User Interface

**The governing requirement over everything in this section: ZERO INFORMATION LOSS TO THE END USER — every
inferred object must be displayable.** Anything the analysis works out has to be capable of being shown.
Revealing it gradually, so that a display is not overwhelming, is the intended design; leaving something the
analysis produced permanently unreachable because no part of the interface has a place for it is not
permitted. *Why:* a user-stated principle. It is the display-side counterpart of the no-information-loss
principle (§2.15, guiding principle #12), which governs what the analysis may discard internally — this
governs what the interface may withhold. Ratified by the user; the record does not date it.

### 12.1 MuseScore Panel Integration

New panels follow MuseScore's existing panel architecture — KDDockWidgets for
panel management, QML for UI components. Do not create parallel infrastructure.
Read how existing MuseScore panels are implemented before creating new ones.

All user-visible strings use MuseScore's existing Qt localization infrastructure
(`.ts` files, Qt Linguist). English and Swedish translations provided for all new strings.

Accessibility follows MuseScore's existing Qt accessibility patterns — focus
management, keyboard navigation, screen reader hooks.

### 12.1a Harmonic Analysis Display Preference

A user preference controls whether harmonic analysis is shown in the status bar. This
preference exists for UI clarity — some users find the chord and key information
distracting, particularly when doing work unrelated to harmony.

**Corrected 2026-08-02 (`OPEN_ITEMS.md` OI-242).** This paragraph continued: *"It is not a
performance control: analysis cost is negligible (well under 1ms) and suppressing the display does
not require skipping the analysis."* **Both clauses are false on the production path since the
notation switch (2026-07-27).**

- **The cost is not negligible.** The note-seam funnel runs `produceNotationRecord` — a WHOLE-SCORE
  decode — synchronously, once per single-note selection, with the legacy bounded-window cache
  bypassed by construction. The measured latency is in the seconds range on the corpus and in the
  seconds-to-tens-of-seconds range on the committed large scores (`OPEN_ITEMS.md` OI-206 for the
  mechanism and the reproduced field pattern; OI-203 for the measurement,
  `tools/joint_estimator/noteseam_latency.json`). The "well under 1 ms" number described the LEGACY
  bounded-window path with its decode cache.
- **Suppressing the display WOULD skip the analysis.** The note-seam status bar is the sole
  per-selection payer: the other consumers (implode, tuning, annotate, the context menu) are
  action-scoped, not selection-scoped (OI-206 Task 1). So on the production arm, suppressing the
  display is precisely what would skip the per-selection analysis.

The preference's stated PURPOSE — clarity, not cost — is untouched by this correction. **Whether it
should also become a performance control is OPEN**: that depends on the OI-203/OI-206 remedy and is
not settled here.

The preference follows MuseScore's existing preferences infrastructure. Toggling it
takes effect immediately on the next selection change without requiring a restart. When
disabled, the status bar reverts to standard MuseScore accessibility information.

### 12.1b Menu Actions (Implemented)

**Completed 2026-08-02 (`OPEN_ITEMS.md` OI-257): this table listed two actions; the code registers
nine that consume the harmonic analysis.** The two Tools-menu actions below are wired through
`notationuiactions.cpp` → `notationactioncontroller.cpp` → `appmenumodel.cpp`; the other seven are
listed beneath them.

| Action ID | Menu label | Trigger |
|-----------|-----------|---------|
| `implode-to-chord-track` | Implode to chord track | Requires a range selection on a grand-staff part; analyzes all other staves and populates the selected part with a harmonic reduction |
| `tune-selection` | Tune selection | Tunes the selected note or range using the user-preferred tuning system (§11.2a) |

Both are gated by `canReceiveAction(actionCode)` in `NotationActionController`, which checks that a
score is open and the required selection exists.

**The seven further harmonic-analysis actions.** Six are registered in `notationuiactions.cpp` and
one is built by the context-menu model:

| Action ID | Label | Registered at | What it writes |
|---|---|---|---|
| `add-chord-symbol-from-analysis` | Add chord symbol | `notationuiactions.cpp:1402` | the analyzed chord symbol at the selected element |
| `add-roman-numeral-from-analysis` | Add Roman numeral | `:1408` | the analyzed Roman numeral at the selected element |
| `add-nashville-number-from-analysis` | Add Nashville number | `:1414` | the analyzed Nashville number at the selected element |
| `add-chord-symbols-to-selection` | Add chord symbols to selection | `:1420` | chord symbols across the whole selection |
| `add-roman-numerals-to-selection` | Add Roman numerals to selection | `:1426` | Roman numerals across the whole selection |
| `add-nashville-numbers-to-selection` | Add Nashville numbers to selection | `:1432` | Nashville numbers across the whole selection |
| `compose-tune-as` | *(one entry per analyzed reading, under a "Tune as ⟨system⟩" submenu)* | built in `notationcontextmenumodel.cpp:174`, handled at `notationactioncontroller.cpp:387` | retunes the selected note's chord as the chosen reading |

**The right-click chord anchor.** When the right-clicked element is a CHORD rather than a single
note, the analysis is anchored on `chord->notes().front()` — the first note of the chord's note
list (`notationcontextmenumodel.cpp:210-214`). **Derivation not recorded:** nothing in the record
says why the first note is the right representative, and the list order is an engraving-model order,
not a musical one. Recorded here so the choice is at least visible; **whether it is the right rule
is OPEN** (`OPEN_ITEMS.md` OI-257) and is not settled here.

The **"Implode to chord track"** submenu is rebuilt dynamically whenever:
- A different score is opened (`currentNotationChanged`)
- A part is added or removed in the current score (`partsChanged`)

This ensures the submenu is enabled as soon as a valid chord staff is added and
disabled immediately when one is removed, without requiring the user to reopen the
menu.  Implemented via `rebuildChordTrackMenu()` called from both notification paths
in `AppMenuModel::setupConnections()`.

### 12.2 Harmony Navigator

Primary temporal view — shows the chord progression over time as a sequence of
colored blocks. Block width proportional to duration. Current position highlighted.
Clicking any block selects it in the score and opens the chord detail panel.

### 12.3 Voicing Alternatives Panel

When a chord is selected, shows ranked alternative voicings. Each alternative displays:
- Notes in each voice with chord function labels
- Voice leading cost indicator
- Tendency tone status
- Brief description of what makes it distinctive

Hover over any alternative to hear it immediately (uses preview engine).

### 12.4 Tension Curve Editor

Shows harmonic tension as a continuous curve over time. The arranger can draw
a desired tension curve and the system suggests reharmonizations that approximate it.

### 12.5 Style Editor

GUI editor for creating and modifying style JSON files — making the style system
accessible to musicians without JSON expertise. A natural second-phase UI component
that doesn't affect the core architecture.

---

## 13. File Persistence

### 13.1 Separate Files in MSCZ Archive

MuseScore's MSCZ format is a ZIP archive. Our metadata lives as additional files
within the archive alongside `score.mscx`:

```
score.mscz (ZIP)
  └── score.mscx              (standard MuseScore — untouched by our code)
  └── arranger_constraints.xml (constraint data — keyed by element ID)
  └── arranger_branches.xml   (version branches)
  └── arranger_analysis.xml   (cached harmonic analysis)
  └── arranger_preferences.json (user preference model)
```

**Advantages:** Zero interference with MuseScore's standard score read/write.
The score is always valid standard MuseScore. Our data travels with the file.

**Limitation:** Exporting to MusicXML, PDF, or MIDI loses our metadata. This is
acceptable — the arranging workflow is MuseScore-native.

### 13.2 Format Versioning

All our custom files include a format version field. When the format changes,
migration code handles existing files. The score.mscx is never modified by our
persistence layer.

---

## 14. ML Readiness

### 14.1 Interface-Based Substitution Points

Every component that may eventually be replaced or augmented by ML is behind a
pure abstract interface. The factory pattern enables runtime selection:

```cpp
class HarmonizerFactory {
public:
    static std::unique_ptr<IHarmonizer> create(const SystemConfig& config) {
        switch (config.harmonizerType) {
            case HarmonizerType::RuleBased:
                return std::make_unique<RuleBasedHarmonizer>(config.knowledgeBase);
            case HarmonizerType::ML:
                return std::make_unique<MLHarmonizer>(config.modelPath);
            case HarmonizerType::Hybrid:
                return std::make_unique<HybridHarmonizer>(
                    config.knowledgeBase, config.modelPath);
        }
    }
};
```

Components with ML substitution interfaces planned:
- `IChordAnalyzer` — chord quality and extension identification from sounding notes.
  `ChordAnalyzer` is currently a static class; when ML substitutability is needed,
  it will be placed behind this interface alongside `RuleBasedChordAnalyzer`.
  Note: `ChordSymbolFormatter` is **not** part of this interface — it operates on
  `ChordAnalysisResult` regardless of which implementation produced it (see Section 4.3).
- `IKeyModeInferrer` — key/mode inference ranking
- `IHarmonizer` — initial chord suggestions
- `IHarmonicRhythmPlanner` — where chord changes occur
- `IVoicingRanker` — ranking voicing alternatives

### 14.2 Data Collection Infrastructure

The system logs arranger interactions from the start — with user consent — as
future ML training data. Every suggestion accepted, modified, or rejected is a
labeled training example specific to vocal jazz arranging, filling the corpus gap
identified in the design phase.

```cpp
struct ArrangerInteraction {
    MelodicContext melody;
    HarmonicContext context;
    StyleContext style;
    RankedChord suggested;       // What the system offered
    ChordSymbol actual;          // What the arranger used
    InteractionType type;        // Accepted, modified, rejected
    float timeToDecision;        // How long the arranger considered it
};
```

### Automated annotation review (planned, post-RFC)

`tools/auto_review.py` — headless pipeline that loads a directory of scores
via `batch_analyze`, runs the annotation path, and passes structured output
to an LLM judge (Anthropic API) for music-theory-correctness evaluation
without corpus ground truth dependency. Produces per-score judgment reports
and aggregate quality summaries. Calibration requires a small hand-verified
set of 10–15 scores. Intended as a scalable complement to corpus validation
for repertoire not covered by DCML/WiR/Bach chorale annotations.

**Three-mode design:**

Mode 1 — No pre-existing symbols: judge evaluates our output against music
theory rules only.

Mode 2 — Pre-existing symbols present: treated as a second analyst's opinion,
not ground truth. Judge comments on agreements and disagreements without
scoring disagreements as errors. Framing: "two analysts may reach different
but equally valid conclusions."

Mode 3 — Known ground truth corpus (DCML/WiR/Bach chorales): judge scores
errors directly against reference annotations.

Mode detection is automatic: if Harmony elements exist in the score before
annotation, use Mode 2. If the score is in the DCML registry, use Mode 3.
Otherwise use Mode 1.

**LLM triage pipeline (implemented, `llm-triage` branch):**
A complementary pipeline exists on the `llm-triage` branch that submits
scores directly to an LLM for chord inference and compares the result
three ways: LLM vs DCML ground truth, LLM vs our analyzer, our analyzer
vs DCML. This is particularly useful during pipeline snapshot diff reviews
as a structured musical reference point, reducing reliance on manual
inspection alone. See `docs/quality_observations_iter76.md` for the
recommended workflow. The branch needs periodic re-merging with master
to stay compatible with the current analyzer output format.

**Report format:**
Designed as input to a Claude conversation, not a standalone verdict.
Requirements:
- Compact enough for many scores in a single context window
- Structured to make cross-score patterns visible
- Flags specific measure locations for drill-down
- Separates formatter artifacts (actionable) from analytical disagreements
  (judgment call) from expected limitations (ignore)
- Includes score metadata per entry: title, composer, key, time signature,
  texture type, preset used

**Pipeline boundary:**
Entire `auto_review.py` pipeline lives in `tools/` — no MuseScore core
involvement. Operates on JSON output from `batch_analyze`. Pre-existing
chord symbols read from score as `writtenSymbols` field in JSON, our
inferred symbols as `inferredSymbols` field. Color (red) used as filter
criterion when both are present in the same score file.

---

## 15. Development Phases

*Current implementation status, remaining items, and immediate next steps are in STATUS.md.*

### Development Tools

The following tools live in `tools/` and are **not part of the shipping product**.
They are compiled/run only in development builds (`MUE_BUILD_ENGRAVING_DEVTOOLS=ON`).

**`tools/batch_analyze.cpp`** — headless C++ analysis tool.
Loads a MusicXML (or MSCZ/MSCX) file, runs our harmonic analysis pipeline
(boundary detection, ChordAnalyzer, KeyModeAnalyzer) without any UI, outputs JSON.
Uses the same module-initialization pattern as MuseScore's existing test
infrastructure (DrawModule + EngravingModule + MusicXmlModule, `MScore::noGui = true`).
Compiled as a separate executable; linked against `engraving`, `composing_analysis`,
and `iex_musicxml` — no notation module required. Because the tool only consumes
logical score structure, it deliberately skips forced post-load layout; this avoids
legacy native MSCX cache-overflow crashes (for example Mozart `K533-3`) without
changing the emitted harmonic-analysis JSON.

**`tools/music21_batch.py`** — exports scores from music21's corpus to MusicXML
and produces a JSON harmonic analysis per score.  Supports any composer via
`--composer NAME` (default: `bach`).  The music21 corpus directory is resolved
automatically from the installed library — no hardcoded path required.
Working copies (XML + JSON) are written to `tools/corpus/` using short names
(`bwv1.6.xml`, `beethoven_opus132.xml`, `beethoven_opus59no1_movement1.xml`).
Note: music21's `romanNumeralFromChord()` is stateless and local — it does not
use temporal context.  Key detection uses Krumhansl-Schmuckler (global, stored as
`detectedKey`) and FloatingKey sliding window (local, stored as `keyLocal` per
region).  Both are stored for comparison.

**`tools/inject_m21_rn.py`** — injects music21's Roman numeral labels into an
exported MusicXML file as `<direction type="words">` elements above the first staff.
Source XMLs are read from `tools/corpus/`; annotated output is written to
`tools/corpus_m21_xml/` (default).  Open the result in MuseScore alongside the
chord staff output to compare music21's analysis with ours visually.

**`tools/compare_analyses.py`** — three-level comparison of our analysis against
music21's.  Levels: chord identity (key-independent), key context, Roman numeral
string.  Classifies disagreements into `full_agree`, `near_agree`,
`chord_agree_rn_differs`, `chord_agree_key_differs`, `chord_disagree`, `unaligned`.
Also checks music21's chord against our top-2 alternatives before declaring
`chord_disagree`, classifying such cases as `near_agree`.
The script reports all six comparison categories.  Chord identity agreement rate —
the most diagnostically meaningful figure, counting cases where root pitch class and
quality match regardless of key context — must currently be computed manually as
(full_agree + chord_agree_rn_differs + chord_agree_key_differs) / total aligned
regions.  Adding this as an explicit script output is a planned improvement.

**`tools/run_validation.py`** — orchestrates the full pipeline across all chorales.
Produces an HTML validation report.  Works with any composer supported by
`music21_batch.py`.

```bash
# Full Bach corpus
python tools/run_validation.py --output tools/

# Single chorale for spot-checking
python tools/run_validation.py --single bach/bwv66.6
```

---

### Submission Roadmap (pre-PR phases)

Short-term milestones tracking readiness for MuseScore contribution.

#### Phase 1 — Analysis foundation *(complete)*

The Phase 1 analysis engine, status bar integration, and basic chord staff are
implemented and passing all targeted tests. See STATUS.md for test counts.

#### Phase 2 — Inferrer stabilization **COMPLETE — `bc6f2edb`**

2a — Key annotation display: confirmed working. `minKeyStabilityBeats=8.0`
  suppresses transient key changes. Mode name threshold correctly applied.

2b — Corpus re-run: 64.6% weighted direct DCML confirmed stable after
  formatter and key-detection fixes (Corelli 70.3%, Dvorak 79.2% spot-checked).

2b2 — Complete-voicing jazz transcription QA (2026-04-17): My Funny Valentine
  (Bill Evans, Some Other Time 1968, Felix B. transcription) — 185-measure
  three-layer comparison (our annotations vs human analyst transcription vs
  third-party plugin). Agreement with human transcription: approximately 75–80%
  exact or near-exact chord symbol match. Extended runs of perfect
  measure-by-measure agreement: m.82–102, m.151–185, Coda (m.179–185). Complex
  extended chords correctly identified: AbΔ7#11, F-13, G7(#9b13), EbMaj7add13/Ab,
  AbMaj7add13(no3)/Gm7/F, GbMaj7b9b5, GbMaj7add13, FmMaj7, CmMaj9, Asus(add9b5),
  Eb7sus#5/B, G7sus#5#11, and many others. Bass solo ostinato (F13/Eb, m.106–142):
  correctly held across 36 measures. Pedal point (Bb pedal, m.106): correctly labelled.
  The 75–80% figure on complete voicings vs 64.6% weighted corpus figure reflects the
  sparse-voicing limitation: the vertical analyzer performs substantially better when
  bass notes and complete chord voicings are present. Both figures are cited in the RFC
  with this context. Note: `Dsdim`/`Fsdim` visual artifacts in screenshots are Campania
  font rendering artifacts (§5.8), not formatter output bugs. Internal strings confirmed
  correct via edit dialog.

2c — Benchmark set Rule 12 sign-off: PASSED 2026-04-14.
  BWV 227/7: E minor key annotation, correct Roman numerals ✓
  Chopin BI16-1: single G major region at measure 1 ✓
  Dvořák op08n06: Bb major context, cadence detection, confident opening ✓

2d — Known limitations documented: see §5.8 (updated 2026-04-13 with 10-score
  inspection findings).

2e — Pre-submission backlog items fixed: formatter sussus/bassIsRoot bugs
  (commit `4c35da17`), relative major/minor key ambiguity (commit `3ba80cb7`).

#### Phase 3 — Submission fork preparation *(not started; NOT the next thing)*

- Create submission scope document (`docs/submission_scope.md`)
- Identify files in scope vs out of scope for the PR
- Create fork branch containing only submittable code
- Final PR readiness review

**Corrected 2026-08-02 (`OPEN_ITEMS.md` OI-232, dated-note item 3):** this phase was marked *(next)*,
which no session since 2026-04 has treated as the next thing — the whole intervening arc is the layer
rebuild, the joint estimator, and the certification audits. It is recorded here as **not started**;
**when it becomes next is OPEN** and is not settled here. `STATUS.md` is the authority on what the
current next action actually is (§doc governance: `STATUS.md` wins on current state).

---

### Long-term project phases (post-submission)

### Phase 1 — Analysis Foundation

- `TemporalContext` struct — previous chord continuation scoring
- Duration sensitivity for passing events
- Modal extension — melodic minor and harmonic minor families (21 modes total)
- `KeyModeAnalysisResult` extended with `modeIndex` and `tonicPc`
- Normalized confidence scores in both result structs
- Monophonic/arpeggiated chord inference
- Secondary dominant Roman numeral notation
- Validation pipeline against Bach chorale corpus; DCML and ABC Beethoven corpora

### Phase 2 — Knowledge Base and Style System

- `ChordDictionary` — complete chord-scale relationships from Nettles/Levine
- `ScaleModeDictionary` — all western scales and modes
- `SubstitutionNetwork` — complete substitution types with voice leading implications
- Style JSON schema defined and documented
- `StyleLoader` implemented
- Five initial styles authored: Bach chorale, jazz vocal, blues, funk, progressive rock
- `StylePrior` connection in `ChordAnalyzerPreferences` implemented

### Phase 3 — Generation Engine

- `VoicingGenerator` — style-aware voicing from chord symbols
- `VoiceLeadingOptimizer` — Viterbi algorithm over voicing graph
- `RuleBasedHarmonizer` — complete harmonization from melody
- `ConstraintStore` — full fixing system
- `BassLineGenerator` — walking bass for jazz style

### Phase 4 — UI Panels

- Harmony Navigator panel
- Voicing Alternatives panel
- Chord detail panel
- Style selector
- Tension curve editor

### Phase 5 — Visualization and Preview

- Circle of fifths map (first `IHarmonicMap` implementation)
- `HarmonicPreviewEngine` — low-latency chord audition
- Map interaction — click to preview, path exploration
- Tonnetz map (second implementation)

### Phase 6 — Intonation Module

- `TuningCalculator` — tuning systems in `composing/intonation/` (JI, Pythagorean, meantone, well temperaments)
- Per-instrument configuration
- `DriftManager` — drift prediction and correction
- Tuning system selector (equal, just, meantone, well temperament, Pythagorean) — user preference in Preferences → Composing
- Region tuning — "Tune selection" in Tools menu; harmonic rhythm analysis + split-and-slur

---

## 16. Scope Reference

### Ground truth where none is published

**A HUMAN acts as ground truth where no formal ground truth exists (user-decided 2026-07-13).** For
repertoire nobody has published an analysis of, the reference answer is a person's judgment. That person
may reach it by any method they choose, **including** letting an automated triage judge point them at the
passages most likely to be wrong. Such a judge is therefore admitted as **guidance for the human**, never
as a grader and never as the source of a reported number. *Why:* a language-model judge is not ground
truth (#9, and the standing rule that music21 corroborates but never adjudicates), so it could not grade
this system; the most it can do is triage. **When** this workflow starts is tied to the corpus-onboarding
event and is itself open (`OPEN_ITEMS.md` OI-38; the deciding row is OI-56).

### Core — Must Be Implemented

Harmonic analysis (functional, modal, extended tonal, jazz), monophonic chord
inference, analysis correction and ground truth override, voice leading analysis
and optimization, tendency tone tracking, tuning system support, per-instrument
tuning configuration, percussion exclusion, ornamentation (analysis and generation),
variable voice count, transposing instruments, chord symbol input, MSCZ file
persistence, undo/redo integration, incremental analysis cache, enharmonic spelling,
score error detection, musical language detector and graceful degradation, extensible
style system, initial five styles, ML interface design throughout, unified temporal
representation, pickup bars and anacrusis, localization (English and Swedish via
MuseScore infrastructure), accessibility (via MuseScore infrastructure).

### Important — Planned for Later Phases

Full generative support for pop, rock, funk, soul, metal, progressive rock (phased
by style), bass line generation, brass fills and idiomatic material, chord animation
(Poulenc model), non-chord tone generation, doubling rules per style, variation
generation, version branching, arrangement comparison, multiple expertise levels in
UI, natural language instruction, education mode, figured bass input and output,
performance markup suggestions, meter changes and mixed meter, drift prediction and
management, comma pumping, historical tuning for fixed instruments, copyright and
attribution metadata.

### Prepared — Architecture Ready, Implementation Deferred

Imitative counterpoint (fugue, canon), motivic tracking, through-composed large-scale
planning, quartal and quintal harmony, polytonality, sacred and liturgical music,
music theatre and opera, headless operation and batch processing, API access for
external tools, community knowledge base.

### Out of Scope

Live and real-time operation, film synchronization, adaptive game music, non-Western
traditions (graceful degradation at boundary), post-tonal and serial music (graceful
degradation at boundary), audio transcription from recording, spatial music, extended
techniques as primary language.

---

## 17. Coding Standards

### 17.1 Follow MuseScore Practice — With Higher Documentation Standard

Follow MuseScore's existing coding style throughout:
- Formatting defined in `.clang-format` — run clang-format before every commit
- Naming conventions — consistent with existing MuseScore code
- File headers — GPL v3 license header on every file (see existing files for template)
- Include ordering — follow MuseScore's convention

Where MuseScore's documentation practice is minimal, use good practice instead.

### 17.2 The Documentation Standard for This Project

Every public class must have a documentation comment explaining:
- What musical concept it implements
- What it receives as input (in musical terms)
- What it produces as output (in musical terms)
- What it does not handle (important for setting expectations)

Every public method must document:
- The musical operation being performed
- All parameters in musical terms
- Return value in musical terms
- Preconditions and postconditions

Every non-obvious scoring weight or threshold must explain its musical reasoning.

**Example — poor documentation (do not write this):**
```cpp
// Calculate x for each element in v
float calcX(std::vector<int>& v) { ... }
```

**Example — good documentation (write this):**
```cpp
/**
 * Calculates the voice leading cost between two chord voicings.
 *
 * Voice leading cost measures the total pitch motion when moving from one
 * voicing to the next. Smaller values indicate smoother voice leading —
 * the goal in most tonal styles.
 *
 * Cost is the average semitone distance moved per voice:
 *   0.0 = all voices hold common tones (maximally smooth)
 *   1.0 = each voice moves an average of one semitone
 *   3.0+ = typically indicates problematic voice leading
 *
 * Style-specific acceptable thresholds are in each style's JSON file.
 *
 * @param fromVoicing  Current chord voicing (one MIDI pitch per voice)
 * @param toVoicing    Target chord voicing (must match voice count)
 * @return             Average semitone distance per voice
 */
float calculateVoiceLeadingCost(
    const Voicing& fromVoicing,
    const Voicing& toVoicing
);
```

### 17.3 The Harmony Analyzer Documentation Rule

The chord and key/mode analyzers are the most complex components in the codebase.
Every scoring weight, threshold, and heuristic must be documented with its musical
rationale. A musician with reasonable theoretical knowledge must be able to read the
analyzer code and understand why each decision was made.

Example of the standard required (from existing code — maintain this quality):
```cpp
// TPC delta = circle-of-fifths distance for each interval, derived from music theory:
//   perfect 5th  = +1,  major 3rd = +4,  minor 3rd  = -3,  perfect 4th = -1,
//   augmented 5th = +8,  dim 5th  = -6,  minor 7th  = -2,  major 2nd   = +2.
```

### 17.4 Test Documentation Standard

Every test must document:
- What musical situation is being tested
- What the expected result is and why it is musically correct
- What a failure would indicate about the system's behavior

Tests should be readable by MuseScore open source contributors without deep
familiarity with this codebase.

---

## 18. Contributing

### 18.1 Before Writing Code

1. Read this document — especially Sections 2 (Principles) and 4 (Existing Components)
2. Read the relevant existing source files
3. For new components — confirm the interface design matches Section 8's patterns
4. For MuseScore integration — read how existing MuseScore code does it first

### 18.2 Pull Request Strategy

Each pull request should implement one coherent piece of functionality. Large
pull requests are hard to review. The phased plan in Section 15 defines natural
PR boundaries.

### 18.3 The MuseScore CLA

Before submitting any pull request to the official MuseScore repository, the
Contributor License Agreement must be signed. See MuseScore's contribution
guidelines on GitHub.

### 18.4 Updating This Document

When an architectural decision changes — update this document in the same commit.
Stale documentation is worse than no documentation because it actively misleads.
Claude Code should update relevant sections of this document as its last act when
a session changes an architectural decision.

---

## 19. LLM Integration — Claude Composer

> **Full design document:** `docs/llm_integration.md`  
> This section is a summary and entry point. Read the full document before
> working on any LLM integration code.

### 19.1 Vision

MuseScore Studio will support natural-language interaction with scores through
an embedded LLM bridge — provisionally called **Claude Composer**. Users choose
their LLM provider (Anthropic, OpenAI, Ollama, others). The system supports:

- Asking questions about the score (*"where is the climax and why?"*)
- QA and comparison (*"find differences between the oboe in sections C–D vs. G–H"*)
- Targeted modification (*"make the fixes you suggested"*)
- Creative generation (*"reharmonize the second verse, preserving voice leading"*)

### 19.2 Key architectural decisions

**Purpose-built, not part of the plugin API reform.** The LLM integration is
a focused module (`src/llm/`, to be created) that taps the existing
`INotationInteraction` and DOM layers directly. It does not wait for the general
plugin API redesign.

**Stateless tool-call model.** The LLM does not hold object references. Each
tool call carries its own musical address. No proxy objects, no EID handles,
no lifecycle management. This is the right model for LLM interaction and the
simpler one to implement.

**LLM as search agent.** The LLM is never given a full score dump. It has
search tools (`find_notes`, `get_part`, `get_measure`, `search_harmony`) and
fetches what it needs iteratively — exactly as Claude Code uses Grep and Read
in a large codebase. Serialization quality is the critical foundation: clean,
hierarchical, beat-aligned, free of layout noise.

**Intentional vs. computed.** The LLM sees everything the user deliberately
set (pitch, dynamics, articulation, note color, lyrics formatting, visibility).
It does not see what the engraving engine derived (positions, beam geometry,
stem lengths, `LayoutData`). The `Pid` property system is the practical
boundary.

**Conversational continuity.** Analysis and modification occur in one
conversation thread. When the LLM identifies problems in a QA query, "make
the fixes you suggested" executes without re-analysis — the LLM reasons from
its own conversation history.

### 19.3 Relationship to the composing module

The composing module (`src/composing/`) is the LLM's context provider. Its
harmonic analysis output (chord symbols, Roman numerals, key inference,
harmonic rhythm) is included in every score section sent to the LLM. The LLM
does not re-derive harmony from raw pitch data — it receives pre-digested
musical context.

The composing module's analysis also drives the **validation layer**: after
the LLM generates score modifications, voice leading and harmonic consistency
are checked before changes reach the score.

Note: `src/composing/` is not part of official MuseScore Studio upstream. It
is a module under active development by this project, intended as a future
contribution.

### 19.4 The LLM integration as a plugin — the end state

With a properly designed plugin API sitting on top of the Core Access Layer
(including network access and UI extension points), the LLM bridge does not
need to live in MuseScore core. It becomes a plugin — optional, independently
updatable, provider-agnostic, open to community alternatives.

**Build strategy:** Implement the LLM bridge as a native module initially for
speed, but strictly constrained to the Core Access Layer only (never bypassing
it to the DOM). When the plugin API matures, migration to a plugin is then
straightforward. See `docs/llm_integration.md §11` for the full argument.

### 19.4 Implementation phases

| Phase | Scope | Estimate |
|-------|-------|----------|
| 1 | Read-only analysis — score serializer, LLM client, chat panel | ~2 weeks |
| 2 | Search tools, structural addressing, QA/comparison queries | ~1–2 weeks |
| 3 | ~40 curated operations, undo integration, diff preview UI | ~4–6 weeks |
| 4 | Creative generation (reharmonization, new sections, arrangement) | Ongoing |

Estimates assume vibe-coding with Claude Code. See `docs/llm_integration.md §8`
for detail.

---

## Appendix A — Key Musical Concepts

Brief definitions for developers who may be less familiar with music theory terms
used throughout the codebase.

**Pitch class (pc):** A pitch regardless of octave. C in any octave = pitch class 0.
Range 0-11. C=0, C#/Db=1, D=2, D#/Eb=3, E=4, F=5, F#/Gb=6, G=7, G#/Ab=8, A=9,
A#/Bb=10, B=11.

**TPC (Tonal Pitch Class):** MuseScore's representation of enharmonic spelling.
Distinguishes F# from Gb even though they are the same pitch class. Range 0-34 on
the circle of fifths. Used for correct chord naming.

**Circle of fifths:** Arrangement of the 12 pitch classes by perfect fifth.
C-G-D-A-E-B-F#/Gb-Db-Ab-Eb-Bb-F-C. Keys close on the circle are harmonically
related. Key signatures are measured in fifths from C (0 = C major, +1 = G major,
-1 = F major, etc.).

**Guide tones:** The 3rd and 7th of a chord — they define the chord's quality most
essentially and create the strongest tendency to resolve. In G7 the guide tones are
B (major 3rd) and F (minor 7th) — they form a tritone that resolves to C major.

**Tendency tone:** A pitch that has a strong gravitational pull toward a specific
resolution. The leading tone (major 7th of the scale) pulls upward to the tonic.
The chordal 7th pulls downward by step.

**Voice leading:** How individual melodic voices move from one chord to the next.
Good voice leading minimizes motion, prefers stepwise movement, avoids parallel
perfect intervals, and resolves tendency tones appropriately.

**Drop 2 voicing:** Take a close-position four-note chord and drop the second voice
from the top down an octave. Opens the spacing while maintaining smooth voice leading
connections. Characteristic of jazz vocal arranging (Puerling style).

**Roman numeral analysis:** Labeling chords by their scale degree in a key. I = tonic,
IV = subdominant, V = dominant, ii = supertonic, etc. Upper case = major, lower case
= minor. Superscripts indicate extensions: V7 = dominant seventh.

**ii-V-I:** The most fundamental jazz chord progression — minor seventh chord on
scale degree 2, dominant seventh on scale degree 5, major seventh on scale degree 1.
The guide tones resolve by half step: the 7th of ii becomes the 3rd of V, the 7th
of V resolves to the 3rd of I.

---

## Appendix B — MuseScore Score Model Quick Reference

Key classes used in score traversal. Read MuseScore source for full interfaces.

```cpp
Score*        // The complete score
Measure*      // A single measure — score->tick2measure(tick)
Segment*      // A moment in time within a measure — seg->tick(), seg->next1()
ChordRest*    // Either a Chord or a Rest — seg->cr(track)
Chord*        // A chord (collection of notes) — toChord(cr)
Note*         // A single note — n->ppitch(), n->tpc(), n->tick()
Staff*        // A staff — score->staff(staffIdx)
KeySigEvent   // Key signature — staff->keySigEvent(tick)

// Segment types used in analysis
SegmentType::ChordRest  // Notes and rests — what we analyze
SegmentType::KeySig     // Key signature changes

// Traversal
score->tick2segment(tick, true, SegmentType::ChordRest)
score->tick2measure(tick)
measure->first(SegmentType::ChordRest)
segment->next1(SegmentType::ChordRest)

// Always use ppitch() not pitch() — honours ottavas and transposing instruments
// Always exclude grace notes — cr->isGrace()
// Tracks = staffIndex * VOICES + voiceIndex (VOICES = 4)
```

---

*Document version: 3.34 — May 2026: §4.1g gate table extended with kCleanQualities guard (Iter 60) and HalfDim first-inversion bonus (Iters 61/65); Task #62 segmentation replacement marked IMPLEMENTED (batch path, Iter 54); Genuine-21 residual section updated to reflect Path 1 history only; §4.1h added with Path 2 current state (BIR=true=5, BIR=false=125, Jazz=12, tests 407/407 + 53/53), Genuine-5 breakdown, Path 2 fix log, and pending Iter 64 performance work. previous: 3.33 — Session 26: D#/G#/A#→Eb/Ab/Bb enharmonic normalization in `pitchClassNameFromTpc()` for sharp TPC (≥20) in keys below diatonic threshold (block placed before `keySignatureFifths==0` early-return); status-bar alternatives sorted by `normalizedConfidence` (positions 1+ only, position 0 fixed); declared-mode hard override in `resolveKeyAndMode()` from key-signature Mode property; Pass2b iterative bass-movement detection (`kMaxBassMovementPasses=8`); track-specific annotation removal in `addAnalyzedHarmony`; REST context-menu harmonic inference (`analyzeRestHarmonicContextDetails`); §5.16 added; 3 new `Composing_EnharmonicSpellingTests`; corpus: Corelli 70.9%, Bach 75.2%, Beethoven 65.2%. Composing tests: 381/381 (master). Notation tests: 51/51 (master). previous: 3.32 — Session 25: `kSus4MissingFourth = 0.70` penalty added to `structuralPenalties()` in `chordanalyzer.cpp`; fires when Sus4 template lacks detectable P4 (pcWeight < extThreshold), excludes Sus4b5; root-only single-note gap carry blocked in `inferGapRegion` (notationcomposingbridgehelpers.cpp); §5.15 "Sus4 Structural Penalty" added; 2 new `Composing_Sus4RequiresFourthTests` + 3 new `Composing_EnharmonicSpellingTests`; corpus: Corelli 70.9%, Bach 75.2%, Beethoven 65.18% (all improved). Composing tests: 378/378 (master), 320/320 (submission-phase1). Notation tests: 51/51 (master). previous: 3.31 — Session 24: `pitchClassNameFromTpc()` added to `chordanalyzer.cpp`; TPC consulted only when `keyFifths==0` (C major/A minor); `ChordIdentity.rootTpc` field added; `formatSymbol()`/`formatRomanNumeral()` pass rootTpc through; 7 new `Composing_EnharmonicSpellingTests` unit tests; §5.14 "Enharmonic Root Spelling" added. Composing tests: 373/373 (master), 315/315 (submission-phase1). Notation tests: 51/51 (master). previous: 3.30 — Session 20: `ChordAnalyzerPreferences` gains `extensionThreshold = 0.20`; Jazz preset uses 0.12 (`kSeventhThreshold`) to detect lightly-voiced ninths; Standard/Baroque keep 0.20 to suppress counterpoint passing tones; documented in §4.6 `ChordAnalyzerPreferences`. previous: 3.29 — Session 19 (continued): order-of-annotation violation fix (`forceClassicalPath=true` in `addHarmonicAnnotationsToSelection`); Unknown quality Roman numeral fallback added to annotation path (`notationcomposingbridge.cpp`); §5.13 "Analyze-at-Tick Path Table" added; new test `AnnotationOrderDoesNotAffectRomanNumeralOutput`; notation test count 50/50 (all passing). previous: 3.28 — Session 19 (continued): two further chord-track annotation fixes bringing notation tests to 49/49 (all passing): (1) `forceChordTrackQualityFromKeyContext()` helper (in `notationcomposingbridgehelpers.cpp`) re-derives diatonic quality from degree+mode when `formatRomanNumeral` returns empty because quality is `ChordQuality::Unknown` — occurs for lone Aeolian tonic/dominant bare fifths; (2) `kSameChordReannotationGap = 2 * Constants::DIVISION` (960 ticks = 2 quarter notes) threshold in the coalescing pass: consecutive same-chord sub-regions are re-annotated when their gap from the previous annotation equals or exceeds the threshold, enabling the Corelli m24 beat-3 Fm re-annotation (gap=960 ≥ 960 → keep) while preserving the sustained-support merge (gap=480 < 960 → merge). previous: 3.27 — Session 19: two §5.12 regressions resolved: (1) `populateChordTrack()` now runs a post-populate cleanup pass that removes Rest segments sitting inside a Chord's stored time span (artefact of `makeGap`'s "removed too much" restore path on triplet Fractions); (2) `populateChordTrack()` now coalesces consecutive regions with the same user-facing chord identity before the populate loop, preventing over-segmentation when tied-note continuations create extra inference ticks within a single display region. Notation test count: 47/49 (up from 45/49). previous: 3.26 — Campania font rendering artifact (`Dsdim`/`Fsdim`) documented as MuseScore core issue in §5.8; complete-voicing jazz QA evidence added (MFV 185-measure three-layer comparison, 75–80% agreement); `isValidBassNoteName` guard added to `formatSymbol` suppressing slash chord when bass name is not a plain note name; chord name in bass field bug documented and fixed; RFC draft at `docs/rfc_musescore_forum_post.md`; chordlist.cpp upstream bug report draft at `docs/chordlist_bug_report.md`; previous: 3.25 — cadence markers (PAC/HC/DC/PC) and pivot chord labels (vi → ii format, U+2192) wired into annotate path via `detectCadences()`/`detectPivotChords()` helpers; tonicization and augmented sixth labels deferred (no classifier implemented); pivot annotation format updated from verbose "pivot: vi in C → ii in G" to concise "vi → ii"; `kMaxPivotLookaheadRegions = 8` lookahead for pivot confirmation; 13 new notation unit tests (45/49 passing, 4 deferred); previous: 3.24 — B/H naming convention fix for German locale chord names in jazz path; previous: 3.23 — annotation color policy documented (black for human use, red for headless pipeline); auto_review.py three-mode design and report format requirements added; previous: 3.22 — annotate path Roman numeral layer extended to include cadence markers, pivot labels, tonicization labels, and augmented sixth chord labels (Standard/Baroque presets only); automated annotation review tool design recorded; Session 5 jazz QA outcomes documented; previous: 3.21 — the plateau target is now qualified for full-texture tonal corpora only, the highest-ROI roadmap is reordered so texture fixes precede evaluation separation and confidence calibration, Rule 12 adds a permanent benchmark score set for visual review, region identity modes are now decided conceptually (harmonic summary vs as-written), and the Mozart 26.7% direct-DCML figure is explicitly marked as a thin-texture/non-comparable case; previous: 3.20 — confidence interpretation is now documented explicitly as heuristic rather than probabilistic, a reasonable "good enough" plateau is defined for the current vertical tertian engine, the highest-ROI pre-plateau roadmap is recorded, and the stale Mozart `59.4%` agreement reference is corrected to the current 26.7% direct-DCML root-agreement figure; previous: 3.19 — `batch_analyze` now skips forced post-load layout in headless mode because analysis uses logical score data only; this avoids the legacy native MSCX cache-overflow crash on Mozart `K533-3` while preserving JSON output parity with the mirrored `score.mxl` path; previous: 3.18 — same-key-signature key-mode selection now uses tonal-center comparison with a diatonic raw-score guard, preventing the Mozart `K279-1` opening from flipping to spurious `F Lydian`, while Roman/Nashville analysis annotations are excluded from chord-symbol-driven path activation; previous: 3.17 — Milestone A3 confidence gating is implemented for chord-track exposure, the key-confidence thresholds now suppress low-confidence key-dependent annotations, and the Dvorak `op08n06` regression locks that behavior in; previous: 3.16 — Milestone A benchmark passages are recorded, the reusable batch/notation parity harness is documented, and BWV 227.7 plus Chopin BI16-1 now pass exact parity gates; previous: 3.15 — final post-`bassNoteRootBonus` corpus baselines are recorded, Schumann slash-chord spellings are confirmed not to be a comparator artifact, Dvorak op08n06 is accepted as genuine ambiguity, and Corelli walking-bass sus/slash artifacts are documented as a deferred limitation; previous: 3.14 — `populateChordTrack()` now absorbs sparse intra-measure gaps into neighboring written regions so BI16-style chord-track generation does not leave mixed chord/rest measures; previous: 3.13 — `bassNoteRootBonus` conditioning is now implemented with tiered support checks, corpus validation results are recorded, and the Chopin BI16-1 notation mismatch is resolved by aligning `PreserveAllChanges` collapse semantics with the batch path; previous: 3.12 — `bassNoteRootBonus` conditioning is now implemented with tiered support checks, corpus validation results are recorded, and the remaining Chopin BI16-1 boundary issue is separated from the root-scoring fix; previous: 3.11 — four-corpus score inspection now documents the shared `bassNoteRootBonus` failure mechanism and a concrete conditioning strategy for the fix; previous: 3.10 — 2026-04-09 score inspection confirms `bassNoteRootBonus` as the primary cross-corpus failure mode and the highest-priority next action; previous: 3.9 — removed the false pedal-marking analyzer limitation after Rule 11 score inspection confirmed sparse texture rather than analyzer failure; previous: 3.8 — Rule 11 added: representative MuseScore Studio score inspection is required before diagnosis when corpus statistics are anomalous or a texture-specific failure mode is suspected; previous: 3.6 — §5.8 now records two next-session analyzer limitations: pedal-aware Jaccard boundary detection for piano beat-1 accompaniment patterns and the cross-corpus `bassNoteRootBonus` miscalibration signal; previous: 3.5 — Rule 10 added: shared note collection, boundary detection, key/mode resolution, and chord-scoring logic must live in `src/composing/` whenever bridge and batch_analyze must agree; §4.1c duplicate-path technical debt now references Rule 10 explicitly; Bach baseline corrected to 50.0% WIR structural (2026-04-09), superseding the older 83.7% onset-only/music21 figure; previous: 3.4 — §4.1c batch classical path now uses Jaccard boundaries plus smoothed regional accumulation, reducing note-collection divergence from three active paths to two duplicate regional collectors; previous: 3.3 — §4.1c duplicate note-collection-path technical debt documented, including the batch_analyze jazz-path duplicate regional collector and the onset-only classical batch path that bypasses regional accumulation; previous: 3.2 — §4.1c piano pedal-sustain gap documented as the remaining Romantic-piano accumulator limitation; previous: 3.1 — §4.1c Part 2 Jazz Mode implemented: status updated from "design complete" to "implemented"; `analyzeHarmonicRhythmJazz()` / `analyzeScoreJazz()` / `scoreHasChordSymbols()` / `collectChordSymbolBoundaries()` documented; `HarmonicRegion` `fromChordSymbol` + `writtenRootPc` fields noted; FiloSax/FiloBass unblocked; previous: 3.0 — §4.1c Part 2 Jazz Mode design added (chord-symbol-driven boundaries, Harmony element traversal, quality mapping, integration point, open questions); corpus roadmap updated with deferred status for C.P.E. Bach/Handel/Bach Suites/Debussy/Liszt/Bartók; previous: 2.9 — §4.1c Regional Note Accumulation added: collectRegionTones() + detectHarmonicBoundariesJaccard() + useRegionalAccumulation preference documented; §4.2 KeyModeAnalyzer known limitation (dominant seventh / Mixolydian ambiguity) added from Grieg corpus modal diagnostic; previous: 2.8 — §4.1b Contextual Inversion Resolution added: ChordTemporalContext extended with previousBassPc/previousChordAge/nextRootPc/nextBassPc/bassIsStepwiseFromPrevious/bassIsStepwiseToNext; three new scoring parameters (stepwiseBassInversionBonus, stepwiseBassLookaheadBonus, sameRootInversionBonus) added to ChordAnalyzerPreferences; isDiatonicStep() helper added to bridge helpers header; §4.1b temporal context section updated; validation: 83.7% chord identity (up from 83.4%), 661 disagree (down from 673) in the now-retired onset-only/music21 Bach workflow; previous: 2.6 — §4.2 harmonic major modes deferred note added after KeySigMode enum; §15 compare_analyses.py description extended with chord identity agreement rate note; previous: 2.5 — §4.5 "Remaining Gap" subsection removed (bypass no longer exists); §5.2 rewritten to reflect actual piece-start shortcut instead of claimed full bypass; §11.3a status note added (basic zero-sum centering implemented as minimizeTuningDeviation; weighted variant still planned); §3.1 file tree updated with synthetic_tests.cpp; factory/direct-use guidance updated; preset system (ModePriorPreset, modePriorPresets(), applyModePriorPreset, currentModePriorPreset) documented under §4.6 mode detection weights; previous: 2.4 — §4.6 mode detection weights updated to 21 independent priors with 5 presets; §4.5 key decision logic updated; §4.3b bridge location corrected; §3.1 analysis/ subdirectory structure updated*
*Last updated: May 2026*
*Maintainer: Update this document whenever architectural decisions change*
