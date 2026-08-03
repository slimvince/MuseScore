# Decisions group H — Layer 5 and Layer 6 — function, cadence, grouping

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-079 — The function layer annotates and resolves; it never rewrites the committed chord

> additive over L4 (it annotates and resolves; it never
> rewrites the committed chord identity)

**In plain words.** The stage that works out a chord's role in the key may label it and settle open questions, but it may not change which chord was identified.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1477-1478`

**Provenance.** ARCHITECTURE.md:1389-1398 (Layer 5 - Built+Dormant, design ratified)

### D-080 — Carried abstentions are resolved by selecting among the carried readings, never re-derived

> the carried L4 abstentions are resolved by **selecting** among the carried readings (never re-derived)

**In plain words.** Where the chord stage could not decide, the function stage picks from the options it was handed. It does not work the chord out again from the notes.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1481-1482`

**Provenance.** ARCHITECTURE.md:1389-1398

### D-081 — The cadence detector is key-agnostic

> The cadence
> detector is **key-agnostic** (it votes for the key; it does not read a resolved key).

**In plain words.** The part that spots cadences must not be told what key it is in - it is one of the things that decides the key, so reading the answer first would be circular.

**Why.** Both rejected alternatives are named with their defect at the layer's own design document (`cowork_layer5_function_design.md` §9-D2, the same decision entered as **D-336**): the earlier key-dependent detector is circular and conflates the perfect with the imperfect cadence, and a single-chord interval test false-positives on tonic-to-subdominant and tonic-to-dominant because it tests whether the leading tone is *present* rather than whether it *resolves*. The same document records the approach's ratified limit (§5.2): a plain V-to-I and a plain I-to-IV are exact transpositions, so the resolution event alone cannot separate them — which is why the phrase gate, the dominant seventh, and the key layer's aggregation of the tonic votes carry the discrimination rather than the detector.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1481-1482`

**Provenance.** ARCHITECTURE.md:1397. open_items/OI-166 records that the built detector is key-agnostic but CHORD-derived, not the bass-driven pre-scan specified. Defense filled 2026-08-02 by the phase-1g triage wave from `cowork_layer5_function_design.md` §9-D2/§5.2 — the act the phase-1f note named and left for the wave that reads that document; the register entry for the same decision at its design-document home is D-336

### D-082 — The grouping layer is additive, read-only, with no feedback

> additive, read-only, no feedback into L5.

**In plain words.** The stage that assembles phrases and key areas only organises what earlier stages decided. It never changes their answers.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1491`

**Provenance.** ARCHITECTURE.md:1400-1407 (Layer 6 - Design-only, v1 spec)

### D-083 — Hierarchy, periods and prolongation are out of the validatable core

> Hierarchy,
> periods/sentences, and prolongation are out of the validatable core (verifiability contract, §2.15).

**In plain words.** Deeper structural theory - nested hierarchy, periods, prolongation - is deliberately left out, because we have no annotated music to check it against.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1492-1493`

**Provenance.** ARCHITECTURE.md:1400-1407, deriving from D-029

### D-084 — The progression-schema recognizer is a consumer of the function layer, not a new layer

> an L5 *consumer* (a prior + an annotation), not a new layer

**In plain words.** Recognising well-known chord patterns is something that reads the finished analysis and annotates it. It is not another stage in the chain.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1498`

**Provenance.** ARCHITECTURE.md:1409-1414 'Scaffolding-first, deferred'

### D-085 — The voice-leading axis is a separate axis with its own layers

> the **orthogonal voice-leading axis** with its own layers (where melodic phrases [MT] and
>   chord **voicing / arrangement** are analysed)

**In plain words.** How the individual voices move is a second, independent line of analysis alongside the harmonic one, with its own stages.

**Why.** Argued in the axis's own design document against the three co-equal admission gates the architecture requires of any new axis (`cowork_voiceleading_axis_design.md:510-518`, decision D1). (1) Separation of concerns: linear structure is a distinct responsibility no harmonic layer may absorb, and the grouping layer's own specification excludes it explicitly. (2) Verifiability: the motion and interval statistics are facts, an oracle by construction; the texture classification validates under the discovery protocol; stream separation validates against the notated voices. (3) Proportionality: the axis buys a second style coordinate MEASURED orthogonal to the harmonic one — cross-agreement 0.030 over 1,283 dual-view pieces — plus an owner for the melodic phrase, the galant patterns and chord voicing, which are otherwise homeless, and the evidence base for the non-chord-tone lever the dormant full-spine measurement sized at about 45 % of the exact-match ceiling. The alternative weighed and rejected: folding the motion features into the harmonic spine's half-tier as another derived view, which would leave the judgment components (texture, phrases) with no home and mix this axis's concerns into that tier.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Home.** `ARCHITECTURE.md:926-927`

**Provenance.** ARCHITECTURE.md:896-899 records the foundation BUILT (dormant). ARCHITECTURE.md:1415-1415 still says the voice-leading layer is 'not built' - see OPEN_ITEMS OI-232 ★ 2026-08-02 (the phase-1h continuation wave): the recorded defense is FILLED from `cowork_voiceleading_axis_design.md` section 9 decision D1 and section 1, read IN FULL — the entry previously read 'derivation not recorded'. Written from the document, not from memory.

### D-248 — Tonicization labels are not implemented and are deferred

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - Tonicization labels (V/V, V/ii, V/IV etc.) — **NOT YET IMPLEMENTED**
>   (deferred; no `relativeRoot`/secondary-dominant field in
>   `ChordFunction`; requires standalone implementation first)

**In plain words.** On the LEGACY function layer, applied-chord labels such as V/V are not produced: `ChordFunction` (`src/composing/analysis/chord/chordanalyzer.h:287`) has no field for the relative root, so the annotate path's tonicization layer waits on a standalone implementation. SCOPE CORRECTED 2026-08-02 — this describes the legacy structure ONLY. The production joint estimator's renderer DOES emit applied labels: `jointRenderRn` adds the applied "/target" suffix (`src/composing/analysis/joint/jointrender.h:62-63`), and on the committed corpus 8.62 % of scored duration carries an applied label in our Roman numeral, including 50,280 ticks of EXACT matches against applied ground truth.

**Why.** The constraint is stated in the record: `ChordFunction` carries no `relativeRoot` or secondary-dominant field, so the label has nowhere to live (ARCHITECTURE.md:6013-6014).

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:6166-6168`

**Provenance.** ARCHITECTURE.md:6012-6014. Section 5.10 (ARCHITECTURE.md:3860) is the tonicization section; the memory-held backlog item is recorded in the same terms. ★ RATIFIED (user, 2026-08-02) with the revisit to be PLANNED: for the ultimate objective (maximum-precision inference) the feature may be needed — the ground truth annotates applied chords, so not producing them costs Roman-numeral agreement wherever the annotator wrote one. Row OI-267 carries the planning obligation, including the OI-53 tension (a live classifier emitting V7/x was found on the legacy path while this entry's home says not implemented). ★ SCOPE CORRECTED 2026-08-02 (CC, at the phase-1i delivery acts, on Cowork's measured probe finding B-1, user-reviewed): the entry's verbatim is a statement about the LEGACY `ChordFunction` structure, and its plain restatement wrongly generalized it to the whole system. The production joint estimator — the inference layer on both surfaces since the OI-178 adoption — DOES emit applied labels (`src/composing/analysis/joint/jointrender.h:62-63`; measured 8.62 % of scored duration, with exact matches against applied ground truth: `tools/joint_estimator/applied_chord_stake_2026_08_02/`). The OI-53 tension named above is therefore substantially ANSWERED: the joint surface emits applied labels, the legacy `ChordFunction` structure does not carry them. The decision itself is unchanged and stays DEFERRED for the surface it governs; what changed is the recorded scope.

### D-291 — The tonicization labeller is NOT wired, and the metric is NOT changed to credit it - both would hide a real key error

> - **★ HEADROOM CORRECTION (load-bearing — propagate to docs):** the biggest precision slice relocates **Stage 6 → Stage 4** (local-modulation
>   detection). **Do NOT wire 6-tonic-i** (games rn_agree, degrades correctness). Real lever = a **LOCAL-MODULATION / KeyArea detector
>   (Stage 4)**, ~95% of S1, signal = sustained span + local cadence (consumes the committed CADENCE INSTRUMENT + KeyArea); 6-tonic-i's

**In plain words.** A working labeller for applied chords was deliberately left unwired, and the proposal to make the accuracy measurement treat its labels as equivalent to the annotator's was rejected. Both would have raised the reported Roman-numeral agreement while the underlying reading stayed wrong: the annotator has changed key, and labelling the chord relative to the old key hides that.

**Why.** Measured: of the affected cases 92.7 % are cadence-confirmed local keys in the ground truth and 79.2 % last five chords or more, so the annotator's modulation is correct for about 97 % of them; only 2.7 % are brief enough for either reading to be defensible. The comparison already credits the label by root and quality, so it does not over-penalise - it MASKS. Recorded as the clearest win of the measure-before-building rule: without the check the labeller would have shipped and improved the number while worsening the output.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_handoff_archive.md:3833`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 metric-check block), citing `cc_tonicization_modulation_metric_dossier.md`. The same block relocates the largest accuracy slice from the function layer to the key layer. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-335 — The function layer outputs the Roman numeral; the tonic/subdominant/dominant summary is a derived read-out, never a stored output

> - **D1 — Output the Roman numeral; the three-role summary is a derived read-out (decided, user, 2026-06-26).** The Roman
>   numeral is the complete, precise analysis and is what the reference corpora evaluate; the three-role summary
>   (tonic/subdominant/dominant) is deterministically derivable from it and therefore lossy to store as a primary output.
>   *Rejected:* a first-class three-role analysis — it would have to resolve the few context-dependent role cases, which no
>   reference data can verify, violating the build-only-what-we-can-verify discipline. The read-out, if built for
>   accessibility, defaults those cases to their tonic-side bucket. (Full reasoning: methods catalog §1.)

**In plain words.** The layer's answer is the Roman numeral — the complete, precise reading. The coarse three-role label can be worked out from it whenever a display needs it, so it is never stored or used to drive the analysis.

**Why.** Measured against the field: every published autonomous Roman-numeral system represents and evaluates the analysis as the numeral's components and none emits a three-role head. A first-class three-role analysis is rejected because it would have to resolve context-dependent role cases no reference data can verify.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:612-617`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 611). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-336 — Cadence detection is key-agnostic and votes for the key rather than reading one

> - **D2 — Cadence detection is key-agnostic and votes for the key; it does not read a resolved key.** *Rejected:* the prior
>   key-dependent detector, which is circular and conflates the perfect with the imperfect cadence; and the single-chord
>   interval test, which false-positives on tonic-to-subdominant and tonic-to-dominant because it tests leading-tone
>   presence (the major third of any major triad) rather than leading-tone resolution. The event-pair feature test with the
>   phrase gate is the corrected design.

**In plain words.** Points of harmonic closure are found without being told the key, and each one casts a vote for what the key is. Reading a key that a cadence is supposed to help decide would be circular.

**Why.** Both rejected alternatives are named with their defect: the earlier key-dependent detector is circular and conflates the perfect with the imperfect cadence, and a single-chord interval test false-positives on tonic-to-subdominant and tonic-to-dominant because it tests whether the leading tone is present rather than whether it resolves. The layer's own recorded limit is that a plain V-to-I and a plain I-to-IV are exact transpositions, so the resolution event alone cannot separate them — which is why the phrase gate, the seventh, and the key layer's aggregation carry the discrimination.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:618-622`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 611). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-337 — A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost

> - **D3 — Tonicization is the default; modulation requires cadence confirmation plus persistence, as a change-cost.**
>   *Rejected:* a fixed-duration rule (no published threshold exists and the boundary is a continuum); and resolving the
>   distinction in the key layer (it needs function). The hysteresis over the local-key decision matches the ground-truth

**In plain words.** When the music leans toward a note other than the home tonic, the home key holds and the chord is written as an applied chord. The key changes only when a cadence confirms the new key and the music stays in it; how long it must stay is a cost that falls as the candidate area grows, not a fixed number of bars.

**Why.** Both alternatives are rejected with reasons: a fixed-duration rule has no published threshold and the boundary is a genuine continuum, and resolving the distinction in the key layer cannot work because it needs function. The hysteresis form is chosen because it matches the ground-truth annotation convention.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:623-625`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 611). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-338 — The function layer selects among the chord layer's carried readings and never re-derives a chord from the notes

> - **D4 — The layer selects among Layer 4's carried readings; it never re-derives.** *Rejected:* re-scoring the slice from
>   the notes (that is Layer 4's job and would duplicate it) — the structural content of the ratified resolution-by-
>   selection: a case separable by a note cue is a lower-layer case, a case separable only by function is this layer's,
>   leaving no third box.

**In plain words.** Where the chord layer left a stretch open, this layer picks one of the readings that layer carried. It never goes back to the notes and works out a chord of its own.

**Why.** Structural, and stated as such: a case separable by a note cue is a lower-layer case and a case separable only by function is this layer's, which leaves no third box — so re-scoring from the notes would duplicate the layer below.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:627-630`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 611). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-340 — The reading the function layer emits IS the selected source's committed identity, carried whole — never rebuilt field by field

> **The carried chord identity is emitted VERBATIM (carry-fix 2, 2026-07-02).** "Additive, does not replace" is literal at
> the struct level: the reading this layer emits for a slice is the *selected source's committed identity carried whole*
> (root + quality + committed **bass/inversion** + the Layer-4-carried **extensions** with their natural-fifth and
> extensions-known flags),
> never a reconstruction from the §5.0 `{root, quality}` progression projection. A standing commit emits its own `chosen`;
> a neighbour-selected override emits that neighbour's identity as-is; an abstain resolution emits the selected carried
> reading — honest-carry `extensionsKnown=false` (unknown, not asserted-absent) states included. This is what lets the
> downstream base Roman numeral render the figured-bass inversion (65/43/42) and the applied-seventh (`V7/x`) from the

**In plain words.** When this layer keeps, overrides or resolves a reading, it passes on the chosen reading's own record intact — its bass, its inversion, its added notes. It never reassembles a reading from the root and quality alone, which would silently drop the rest.

**Why.** Stated with the loss it prevents: rebuilding from the progression's root-and-quality projection would flatten the committed bass and inversion and the carried added notes, so the figured-bass inversion and the applied seventh could no longer be rendered from what the chord layer actually committed. A neighbour-root with this stretch's bass is not a carried candidate, so it is not synthesized.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:547-554`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§7** — `## 7. Data design` (heading at line 537). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-341 — The licensed root-motion set is completed by theory — the ascending fifth, the descending second and the diatonic diminished fifth are added

> 12. **★ §5.0 grammar completion (found 2026-07-02 by the D5 consistency check — ★ RATIFIED by the user 2026-07-03;
>     the §5.0 enumeration is amended, the code increment is pending).** The licensed
>     root-motion set descended from the old scoring-bonus signals and omitted three theory-licensed motions the
>     catalog's
>     own musically-correct entries exercise: **ascending fifth / plagal motion** (IV→I, I→V — tonic-to-dominant!),
>     **descending second** (the Phrygian/Andalusian step), and the **diatonic diminished fifth** (the IV→viiᵒ link of
>     the full circle). The amendment: extend `isLicensedProgression` (+ this §5.0's enumeration, now done) accordingly
>     — algorithmic
>     completion per theory, NOT tuning; its own small dormant increment with tests; the consumer's consistency test
>     then tightens to the clean assert. Evidence: the 6-entry/**11-motion** failure table, measured, enumerated and

**In plain words.** The list of chord-to-chord root motions the analysis treats as real functional progressions was inherited from an older scoring mechanism and left out three motions that standard theory licenses and the project's own catalogue uses. They are added. This is completing an algorithm against theory, not tuning it.

**Why.** Measured by the catalogue-versus-grammar consistency check: six catalogue entries exercising eleven motions failed against the grammar as coded, and the eleven are enumerated and pinned in the consumer's own test. The three missing motions are tonic-to-dominant and plagal motion, the Phrygian step, and the diminished fifth that closes the circle of fifths.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:888-897`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§15** — `## 15. Open items & deferred refinements` (heading at line 782). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-342 — Putting the function layer into production is DEFERRED INDEFINITELY — the posture is a dormant build with ground-truth validation

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Engagement framing.** References to an "engagement hard-stop" / "before any production switch" (§5/§10) remain true
>   *conditionally* — engagement (Phase 5d) is **deferred indefinitely** (production out of scope; the posture is dormant
>   build + ground-truth validation). The hard-stops apply *if* a switch is ever made; they are not pending work.

**In plain words.** Switching the function layer on in the product is not scheduled. It is built and checked against published human analyses, and stays inactive; the conditions written for a switch apply if one is ever made, and are not outstanding work. THIS IS NOT THE INFERENCE-ENGINE SWITCH - that happened (D-010): the joint estimator is production and the legacy pipeline is dormant. This entry concerns the separate Layer-5 function-annotation module, built and validated but never in production in either era. Its concerns are handled by the LIVE implementation natively or by schedule: degree-in-key Roman numerals are the estimator's own state; key changes are decided inside the decode; applied-chord labels are emitted by the live renderer (the D-248/OI-267 revisit covers the remainder); cadence is a fitted factor inside the model and a marker on the presentation surface; carried-abstention resolution is obviated by the full-posterior publication (D-006); the ornament labels are the ratified OI-194 increment; and the complete concern-by-concern mapping of the legacy layer's remaining scope is the OI-259 phase-3 re-disposition.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:696-698`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 669). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02) after the live-handling question was answered (the concern mapping now in the plain restatement); LEGACY-subject marked.

### D-382 — The function layer selects by JOINT CONSISTENCY across tonality, root, inversion and bass — not by maximizing any one score — and every ambiguity kind reasons over the full carried distribution

> The decisive published lesson `[research]` §2: **select by joint consistency across key / root / inversion /
> bass**, not by maximizing any single score. ChordGNN wins the full Roman-numeral label while scoring *lower* on
> the individual heads — the payoff is the mutually-consistent reading, not a stronger vertical or progression
> score; AnalysisGNN's logit-fusion confirms it. This is the direct analog of our selection problem and the steer
> for the L5 objective.
>
> So engaged Layer 5's selection, for each slice, reasons over the **graded distinct-root distribution including the
> exclusion tail** (§2, #12) and picks the reading that is **maximally consistent across the evidence channels**,
> carrying the rest at graded confidence and open-marking where no reading dominates. This **generalizes**
> `resolveAbstained` (§1.2): today only the SymmetricRotation arm reasons over the full pool; the other arms decide
> on the readingA/readingB pair. Engaged selection lifts *all* kinds to reason over the full distinct-root carry —
> the SymmetricRotation arm is the structural precedent.

**In plain words.** Choosing among the readings handed forward is done by picking the one that agrees best across all the evidence at once — the tonality, the root, the inversion and the bass — rather than the one that scores highest on any one kind of evidence alone. Everything else is carried on at graded confidence, and where nothing dominates the stretch is marked open. This generalizes what was built: only the symmetric-rotation case already reasoned over the whole set of alternatives, while every other case decided between just two readings.

**Why.** Grounded in the published result the record cites: the leading joint model wins the full Roman-numeral label while scoring LOWER on the individual heads — the payoff is the mutually consistent reading rather than a stronger vertical or progression score — and a second system's logit fusion confirms it. The record names this the direct analogue of the project's own selection problem.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_engagement_design.md:187-198`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§3.1 The objective: select by JOINT CONSISTENCY, not by strengthening one score”** — `### §3.1 The objective: select by JOINT CONSISTENCY, not by strengthening one score` (heading at line 186). A delegation at ARCHITECTURE.md:1485 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer5_engagement_design.md` IN FULL. The document's banner records `Status: DESIGN (CC, 2026-07-07)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-CLASSIFIED contract-home 2026-08-02 (CC, phase 1j, under the TRANSITIVE-AUTHORITY refinement of the fifth home case, user 2026-08-02): `cowork_layer5_engagement_design.md` carries a status banner and its authority is the user's transitively — the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arc #9 to it by name (`:41`), arc #11 to it by name (`:46`), and states that the Stage-3 build inventory 'is enumerated at `cowork_layer5_engagement_design.md` §9.2' (`:53-55`). The missing `ARCHITECTURE.md` delegation pointer — the gap the ruling says a missing delegation owes — was written into the Layer-5 section in the same commit.

### D-383 — Bass, spelling and tonality-consistency DECIDE; a licensed progression is only a tie-break among already-consistent readings and may never override a committed root

> The **re-ordering vs the as-built resolver** is the load-bearing structural change: the built `resolveAbstained`
> leads with `isLicensedProgression` (the weak channel) as its *primary* separator (Transition/ShareTone arms). The
> research says bass/inversion + spelling + key-consistency are the primary channels and progression is the
> tie-break. Engaged selection **re-orders** so the load-bearing channels decide and progression only breaks ties
> among mutually-consistent readings. *(The channel weights and the deciding margin are precision-phase, R5 — only
> the ordering/direction is fixed here.)*

**In plain words.** The built resolver leads with whether one chord progresses plausibly into the next, and that is the wrong lead. The evidence that actually carries root correctness is the bass and inversion, the written spelling, and how well a root fits the tonality of the passage. Whether the progression is a licensed one is a tidy signal that turns out to be uncorrelated with getting the root right, so it is demoted: it may separate readings that are already equally consistent, and it may never overturn a root the vertical evidence committed to. Only the ordering is fixed here; the weights are left to the fitting phase.

**Why.** Two independent grounds, both cited: published work dissociating the bass from pitch-class content, showing both independently drive expectation, and work on spelling disambiguation — against the project's own measurement, in which the progression-driven override fired 1,043 times for 53 corrections and 809 harms, moving a correct root to a wrong one on about 78 % of its fires. The demotion is therefore the structural form of a measured finding, not a preference.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_engagement_design.md:212-217`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§3.2 The evidence channels, ranked by the research”** — `### §3.2 The evidence channels, ranked by the research (load-bearing first) [research]` (heading at line 200). A delegation at ARCHITECTURE.md:1485 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer5_engagement_design.md` IN FULL. The document's banner records `Status: DESIGN (CC, 2026-07-07)`; the measured basis it consumes is the separately-ratified fine-grain-override finding. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-CLASSIFIED contract-home 2026-08-02 (CC, phase 1j, under the TRANSITIVE-AUTHORITY refinement of the fifth home case, user 2026-08-02): `cowork_layer5_engagement_design.md` carries a status banner and its authority is the user's transitively — the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arc #9 to it by name (`:41`), arc #11 to it by name (`:46`), and states that the Stage-3 build inventory 'is enumerated at `cowork_layer5_engagement_design.md` §9.2' (`:53-55`). The missing `ARCHITECTURE.md` delegation pointer — the gap the ruling says a missing delegation owes — was written into the Layer-5 section in the same commit.

### D-384 — Re-ranking the tonality under chord evidence is a SEPARATE step, never part of the function layer's selection — the function layer reasons inside a tonality already fixed

> - **The joint key↔chord step (O-18 / contract C3)** is a **distinct step, not L5 selection.** L5 selection reasons
>   within a *fixed* region key; the joint step is the coupled machinery that **re-ranks the key under chord
>   evidence** (and vice versa) — the "carry a beam of (key, chord) hypotheses and let downstream chord evidence
>   re-rank the key" of `[research]` §3. It is the home of the C3 "genuinely-coupled key↔chord minority."

**In plain words.** The function stage chooses among readings within a tonality that has already been settled; it never re-opens which tonality that is. Anything that re-ranks the tonality in the light of the chords, or the chords in the light of the tonality, is a distinct piece of machinery upstream of it, and that piece owns the small population of places where the two genuinely depend on each other.

**Why.** The boundary is drawn so that the forward-only control-flow contract is kept: the function stage reads the chord layer's carry forward and never re-derives, and any coupling machinery is a bounded instance of the same forward discipline — a declared exception with its own closure — rather than a free search back across stages.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_engagement_design.md:263-266`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§4.1 Layer boundaries”** — `### §4.1 Layer boundaries (#7) — what belongs where` (heading at line 255). A delegation at ARCHITECTURE.md:1485 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer5_engagement_design.md` IN FULL. The separate step this boundary reserves a place for was afterwards shelved against measurement (**D-278**); the boundary itself is a statement about what the function layer does not own and is unaffected by that shelving. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-CLASSIFIED contract-home 2026-08-02 (CC, phase 1j, under the TRANSITIVE-AUTHORITY refinement of the fifth home case, user 2026-08-02): `cowork_layer5_engagement_design.md` carries a status banner and its authority is the user's transitively — the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arc #9 to it by name (`:41`), arc #11 to it by name (`:46`), and states that the Stage-3 build inventory 'is enumerated at `cowork_layer5_engagement_design.md` §9.2' (`:53-55`). The missing `ARCHITECTURE.md` delegation pointer — the gap the ruling says a missing delegation owes — was written into the Layer-5 section in the same commit.

### D-387 — A contradiction between the function context and a committed chord is surfaced on the ONE open mark, enriched with a reason — not on a second parallel flag, and not by overloading the plain undecided mark

> **The #6-clean vehicle: UNIFY into one structured open-mark carrying its REASON/KIND.** Promote the boolean
> `openMark` (across the three structs and their assembly) to a small open-mark annotation that names *why* the slice
> is marked — one channel, distinct kinds:
> - **`Undecided`** — the case-3 abstain / §15-13 both-licensed honest-carry (today's `openMark = true` semantics,
>   preserved exactly);
> - **`FunctionContextContradiction`** — the F-B case: **the reading stays the L4 commit** (`overrodeCommit` stays
>   **false**, `reading` = the committed chord — the additive-not-replace contract `ResolvedReading` already declares,
>   `functionresolver.h:160-165` `[code]`), and the annotation carries the contradiction as calibrated uncertainty
>   (§7.3).
>
> This **reuses the existing open-mark carry path** (no new field threaded through three structs) and **dissolves
> `[fb §4.2]`'s "new advisory field" into "the existing open-mark, enriched with a reason"** — a unification, not a
> parallel channel, exactly the instruction's licensed outcome ("a *unified* advisory, not a duplicate"). It composes
> with the existing `ResolutionBasis` transparency enum (`functionresolver.h:151-158`): the demoted
> `ResolutionBasis::FineGrainOverride` value becomes an **annotation basis** (renamed/re-valued to
> `FineGrainContradiction` — an owed spec edit, §8.2), never an override basis.

**In plain words.** When the functional context disagrees with a chord the earlier stage committed to confidently, that disagreement is recorded as a reason on the single existing open mark, alongside the genuinely-undecided reason it already carries. Two shapes were rejected. Setting the plain undecided mark would be wrong in meaning: the chord stage was not undecided, it committed, and the reading is carried unchanged. Adding a second flag beside the open mark would be two fields on the same object meaning the same thing, threaded through the same three places.

**Why.** Both rejections are argued at the code and the argument is recorded with them: the plain mark's declared meaning is 'no decided answer — genuinely undecidable', so using it here would tell the display that nothing was decided when something was, which is an information loss; and a parallel flag duplicates a channel, which principle #6 forbids. The unification also composes with the existing transparency enumeration, whose override value is re-valued to a contradiction value in the same act.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_engagement_design.md:490-505`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§7.2 The vehicle”** — `### §7.2 The vehicle (#6, the load-bearing decision): unify the open-mark, do NOT add a parallel channel` (heading at line 468). A delegation at ARCHITECTURE.md:1485 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_layer5_engagement_design.md` IN FULL. The record notes it dissolves an earlier proposal for a new advisory field into an enrichment of the existing one. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-CLASSIFIED contract-home 2026-08-02 (CC, phase 1j, under the TRANSITIVE-AUTHORITY refinement of the fifth home case, user 2026-08-02): `cowork_layer5_engagement_design.md` carries a status banner and its authority is the user's transitively — the user-ratified `cowork_engage_arc_plan.md` (RATIFIED by the user, 2026-07-07) delegates arc #9 to it by name (`:41`), arc #11 to it by name (`:46`), and states that the Stage-3 build inventory 'is enumerated at `cowork_layer5_engagement_design.md` §9.2' (`:53-55`). The missing `ARCHITECTURE.md` delegation pointer — the gap the ruling says a missing delegation owes — was written into the Layer-5 section in the same commit.

### D-388 — Texture is read primarily from HOW VOICES MOVE TOGETHER, not from how far each line leaps — the interval-led alternative was measured weaker and partly an encoding artifact

> - **D2 — motion-type-led features.** Measured (§4): the ablation is decisive, and the motion view is the
>   extraction-robust one (it never explodes chords; it grouped exploded chamber corpora with the chorales, ruling
>   out an encoding artifact). *Alternative rejected:* interval-profile-led (the pilot's view) — weaker (≤0.20) and
>   partly a chordal-density artifact by the study's own caveat.

**In plain words.** What separates one texture from another is the pattern of parallel, similar, contrary and oblique motion between pairs of lines. The rates of those four motion types alone recover the texture structure; the statistics of how far each single line moves do not, and are used only as a secondary description of melodic complexity.

**Why.** Measured, and decisively: motion-type rates alone recover the texture structure at an agreement index of 0.37 to 0.46 where interval profiles alone reach at most 0.20. The motion view is also the extraction-robust one — it never explodes chords, and it grouped chamber corpora encoded with exploded chords together with the chorales, which rules out an encoding artifact. The rejected alternative carries the study's own caveat that its signal is partly an artifact of how densely chords are written.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:519-522`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 508). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-07-03 — asks A1–A8 ratified in full)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-389 — A notated voice is a FACT and an inferred perceptual line is a JUDGMENT — the two are separate types and are never conflated

> - **D3 — two-tier voice model: notated voice = fact; stream = inference.** Never conflated; enforced by the §0
>   one-sense rule and the type system (VoiceLine vs Stream). *Alternative rejected:* a single "voice" concept with
>   a quality flag — exactly the silent fact/judgment mixing the universality principle forbids.

**In plain words.** The line the score actually writes and the line a listener hears are different things and are kept apart, in the words used and in the types the code carries. The written one is a fact taken from the score; the heard one is always called a stream, is always marked inferred, and carries its own confidence. Merging them into one idea with a quality flag was considered and rejected.

**Why.** The rejection has a principled ground: one idea with a quality flag is exactly the silent mixing of fact with judgment that the universality principle forbids — the fact layers must stay style-agnostic and free of inference, so a value that is sometimes read and sometimes guessed cannot live in one field. The separation is enforced twice over, by the document's one-sense vocabulary rule and by the type system.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:523-525`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 508). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A3, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-390 — The first version classifies the WHOLE selection as one texture — classifying within a piece is deferred behind a measurement, because the evidence is per-piece

> - **D4 — texture classification is v1's only judgment, at whole-selection granularity.** The evidence is
>   per-piece; a per-span claim would be assumption-based code. The refinement is a named cheap measurement first
>   (§15-1). *Alternative rejected:* shipping windowed per-span classification now — knowledge-based-coding
>   violation.

**In plain words.** The study that established the texture classes measured whole pieces. Whether the same statistics, computed over a moving window, would find the places where the texture changes inside a piece has not been measured. So the first version gives the whole selection one texture, and finding several within it waits on that measurement. Shipping the windowed version now was considered and rejected as building on an assumption.

**Why.** The rejection cites the project's own rule that a component's build is earned by the measurement behind it: a per-stretch claim on per-piece evidence would be assumption-based code. The record also notes what the deferral does and does not cost — the output type is already a series of texture stretches, so the refinement changes how many there are, not the shape of anything.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:526-529`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 508). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A4, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-391 — Reads between the two analysis dimensions are admissible only where the combined dependency graph stays acyclic — harmonic layers may take voice-leading FACTS freely; a voice-leading component may take a committed harmonic result only if nothing that result depends on consumes it back

> - **D6 — the cross-axis dependency rule (acyclicity by declaration).** Cross-axis reads are admissible only where
>   the combined two-axis dependency graph stays acyclic, checked at each wiring: (a) harmonic layers may consume
>   axis-2 **facts** (VL-A/B, L1-derived only) freely — e.g. the future L4 non-chord-tone filter — because facts
>   depend on no harmonic inference; (b) an axis-2 component may consume a **committed harmonic output** (VL-F
>   reads L3's key) provided nothing that harmonic layer depends on, directly or transitively, consumes that
>   axis-2 component. VL-F→L3 is safe (L3 consumes no axis-2 output; the planned L4 filter consumes only VL-A/B,
>   which don't depend on VL-F). Each future wiring re-states this check in its instruction. *Alternative
>   rejected:* a blanket "axis 2 reads nothing harmonic" — it would make schema recognition impossible for no
>   structural gain.

**In plain words.** The harmonic analysis and the voice-leading analysis may read each other, under one rule checked at every wiring. A harmonic stage may freely use the voice-leading facts derived straight from the notes, because those depend on no harmonic decision. A voice-leading component may use a harmonic result that has already been committed — recognizing a stock pattern needs scale degrees, and scale degrees need the tonality — but only if nothing that harmonic stage depends on, directly or through others, reads that component back. A blanket ban on reading anything harmonic was considered and rejected.

**Why.** The rejection is argued on what it would cost against what it would buy: forbidding every harmonic read would make pattern recognition impossible for no structural gain, since the one planned read is safe under the rule and is shown to be — the tonality stage consumes nothing from this dimension, and the planned non-chord-tone filter consumes only the facts, which do not depend on the pattern recognizer. Each future wiring re-states the check rather than inheriting this one.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:533-541`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 508). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A8, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-392 — The later voice-leading components are CLAIMS WITH OWNERS, not builds — each clears its own design document and its own evidence before any instruction exists

> - **D5 — staged components behind design gates.** VL-D/E/F/G/H are claims with owners, not builds; each clears its
>   own design + footing before an instruction exists. This is the proportionality gate applied *inside* the axis —
>   no slot-filling (the Contrapunctus reminder). *Alternative rejected:* one monolithic axis build.

**In plain words.** Stream separation, phrase segmentation, pattern recognition, voicing analysis and part-writing advice are all named and assigned, but none is built. Each first needs its own design document and the evidence to stand on. Building the whole dimension in one go was considered and rejected.

**Why.** The record names the principle and the failure it guards against: this is the proportionality admission gate applied inside the dimension rather than only at its border, and the guard is against slot-filling — building a component because a slot exists for it rather than because evidence earned it.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:530-532`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 508). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A2's second half, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-393 — Every voice-leading inference publishes the committed answer AND the FULL ranked list of all alternatives with their weights — nothing below the top is discarded

> - **Output — the committed class PLUS the full ranked alternative list (zero information loss; ratification
>   clarification, user 2026-07-03):** the span's voice-leading idiom from the four-class taxonomy (§0) is the
>   TOP of a **fully ranked list of ALL class fits, each carried with its weight** — nothing below the top is
>   discarded; a downstream consumer (and Stage-5 calibration) sees everything VL-C saw. This is the ARCH §2.15
>   minimality-plus-maximal-information contract applied here (the same carried-alternatives discipline as L4's
>   ranked chord readings).

**In plain words.** The texture stage does not publish only the class it chose. It publishes every class it considered, ranked, each with the weight it earned, so that anything reading it later — including the calibration step — sees exactly what the stage saw. Nothing below the winner is thrown away.

**Why.** It is the carried-alternatives contract the architecture already states, applied here rather than restated: the same discipline the chord layer's ranked readings follow. The record notes the clarification it rode: facts carry no alternatives by construction, but a choice made at the fact level — which reduction rule was applied — is a declared parameter of the query, recoverable at zero loss from the lossless note model.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:346-351`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.3** — `### 5.3 VL-C — texture classification (inference; the first judgment component)` (heading at line 338). A delegation at ARCHITECTURE.md:901 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. The document's banner records that this clarification was folded in BEFORE signing and that the signing ratified asks A1–A8 in full. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-394 — Reducing a chord-bearing voice to one line is a DECLARED parameter of the request, uniform across sources — never silent, never chosen per source; the first version offers exactly one rule

> - **Reduction is declared, uniform, and per-query — never silent, never per-source.** A consumer needing one line
>   from a chordal voice names a reduction rule (v1 provides exactly one: **top-note** — the highest sounding pitch
>   per event, the study's curated-branch rule). The rule is a parameter of the *query*, carried in the output's
>   provenance. This single uniform rule is what retires the study's per-source explosion asymmetry (its View-A
>   caveat) when the production extractor is built.

**In plain words.** Where a written voice carries chords rather than single notes, anything needing one line from it must name the rule that picks that line, and the rule travels with the answer as provenance. There is one rule in the first version: take the highest sounding pitch. It is applied the same way everywhere, which is what removes the uneven treatment the exploratory study had between its sources.

**Why.** The record ties it to a measured problem in the study it inherits from: the study reduced differently per source, which is recorded as a caveat on its own results, and one uniform declared rule is what retires that asymmetry when the production extractor is built. Declaring the rule per request rather than fixing it globally also keeps it inspectable — the record's standing complaint against the alternative is that a silent reduction makes its effects invisible rather than absent.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:304-308`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§5.1** — `### 5.1 VL-A — the voice-linear view (representation; facts)` (heading at line 289). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-07-03 — asks A1–A8 ratified in full)` and, separately, that the top-note default is closed as-built. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-395 — Three named floors govern abstention, and the FIT floor is the one that lets a passage resembling NO known texture decline rather than be forced to its nearest

> - **Honest marks — the three declared floors (named once here, used by these names everywhere):** the
>   **evidential floor** (minimum motion-sample count for a profile to support a decision), the **margin floor**
>   (minimum best-vs-second-best margin), and the **fit floor** (minimum absolute fit of the best class).
>   Abstention (uniform semantics, contract U5) fires when the margin is below the margin floor **or** the best fit
>   is below the fit floor — the second clause is what makes a span resembling *no* reference class abstain rather
>   than be forced to its nearest class (a relative margin alone cannot deliver that).

**In plain words.** The texture stage declines to answer under three named conditions: too few motion samples to support any decision, too small a lead of the best class over the second, or too poor an absolute fit of the best class. The third is the one that matters for music the taxonomy does not cover: without it, a passage unlike every known class would still be assigned to whichever class it least resembled, because a lead over the second-best says nothing about whether either fits.

**Why.** The reason is stated with the rule and is a logical one rather than a measured one: a relative margin alone cannot deliver off-taxonomy abstention. The record also notes that the floor was added in response to an independent adversarial audit, as one of that audit's three high-severity findings — the abstention the design promised was not deliverable by the mechanism it specified until this floor existed.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:376-381`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.3** — `### 5.3 VL-C — texture classification (inference; the first judgment component)` (heading at line 338). A delegation at ARCHITECTURE.md:901 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. All three floor values are recorded as precision-phase constants, not fixed here. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-396 — The voice-leading dimension covers NOTATED music only, and its style coordinate is UNDEFINED — not zero — for sources that carry no voices

> - **Coverage declaration (honest, structural).** The axis analyses **notated music only** — lead-sheet sources
>   carry no voices, so the voice-leading coordinate of the 2-D style structure is simply *undefined* for them
>   (undefined, not zero, in every consumer). This is a representational fact, not a corpus accident.

**In plain words.** This dimension reads the lines a score writes, so a source that carries no lines at all, such as a lead sheet, has no voice-leading character to read. Every consumer must treat that coordinate as undefined rather than as zero, because a missing measurement is not a measurement of nothing.

**Why.** The record grounds it as a property of the representation rather than of the corpora held: a lead sheet does not fail to have voices for want of a better encoding, it has none by what it is. The distinction between undefined and zero is what stops a downstream consumer from reading absence as a low score.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:502-504`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§8** — `## 8. Crosscutting concepts` (heading at line 484). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A6, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-397 — The homeless analysis objects are ASSIGNED to named owners on the voice-leading dimension — the stock patterns, the melodic phrase, chord voicing, and part-writing advice — as claims, discharged only at each owner's own ratified design

> - **A7 — the claims registry:** VL-F claims the six voice-leading-defined Vocabulary entries; VL-E claims the
>   melodic phrase [MT]; VL-G claims voicing/arrangement (the dictionary §5.3 exclusion); VL-H claims part-writing
>   checking & suggestion (the advisory consumer, incl. the VL-B per-sample motion-event export that serves it).
>   Recorded as claims with owners, discharged only at each component's own ratified design.

**In plain words.** Four kinds of analysis object that previously had no owner are assigned here: the stock eighteenth-century patterns and the chromatic line cliché, which the chord dictionary already flags as belonging to this dimension; the melodic phrase; chord voicing and arrangement, which the dictionary explicitly excludes from its own scope; and checking and advising on part-writing. Each is recorded as a claim with an owner, not as work started, and the claim is settled only when that owner's own design is ratified.

**Why.** The assignment is grounded in what defines each object: the stock patterns are defined primarily by a paired outer-voice scale-degree skeleton — that is, by voice leading — which the built chord catalogue already records with a voice-leading-defined flag on six entries, verified at that catalogue. The phrase assignment is the other side of a ruling already made on the harmonic side, where the grouping layer deliberately does not segment the melodic phrase.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:693-696`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§16** — `## 16. Ratification asks` (heading at line 680). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A7, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-398 — Parallel motion is judged SEMITONE-EXACT, not by generic diatonic size — a same-direction move whose semitone interval changes counts as similar motion

> 2. **The "parallel" interval-preservation convention** (semitone-exact vs generic-diatonic) — ✅ **CLOSED at build
>    (AS-BUILT, 2026-07-03): SEMITONE-EXACT.** Verified at `voiceleading2.py` `_motion`: `parallel` iff both voices
>    move the same direction AND `(pu1−pv1)==(pu0−pv0)` on signed MIDI pitches (a same-direction move whose semitone
>    interval changes is `similar`). Replicated exactly in `voiceleadingprofiles.cpp classifyMotion` (oracle-tested).

**In plain words.** Two lines count as moving in parallel only when they move the same way and the distance between them in semitones is unchanged. A pair moving the same way from a major third to a minor third is therefore similar motion, not parallel, even though both are thirds. The alternative — counting by the size of the interval as written on the staff, so that any third to any third is parallel — was the open question, and this is the answer.

**Why.** Settled by replication rather than by choice: the convention was read off the exploratory study's own motion classifier at source and reproduced exactly in the production code, which is oracle-tested against it. Fixing it this way is what makes the production implementation reproduce the study's features, which the design requires of it.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:632-635`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§15** — `## 15. Open items & deferred refinements` (heading at line 624). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. The document records this as one of two build declarations the design owed and the build closed; the closure names no ratifier. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-399 — The texture feature space was decided BY MEASUREMENT among three named candidates — the standardized combination of both views won; the unstandardized combination was rejected before testing for a measured dilution

> **★ AS-BUILT: the winner is the z-scored
>   concatenation (ABz)** — measured by `run_vl_feature_space.py` (nearest-centroid reproduction of the ratified AB K=4
>   partition, cap=80/source, seed 0): **ABz ARI 0.791 / accuracy 0.918**, two-stage 0.716, motion-only 0.258 (raw
>   concatenation rejected a priori).

**In plain words.** Which numbers the texture decision is made from was not chosen by argument. Three candidates were tested against one criterion: reproduce the classes the earlier study established. Putting both kinds of statistic together after standardizing them reproduced those classes best. Putting them together without standardizing was ruled out in advance, because the sixteen interval numbers would simply outvote the four motion numbers.

**Why.** Measured, with the numbers recorded: nearest-centroid classification in the standardized combined space reproduces the ratified four-class partition at an agreement index of 0.791 and an accuracy of 0.918, against 0.716 for the two-stage alternative and 0.258 for motion alone. The declared tolerance was met with margin, so no stop fired. The resulting reference set ships as generated code with its full provenance — the run, the corpus state, the number of classes, the seed and the library version — and is refit at corpus waves under the same protocol as the harmonic taxonomy.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:368-371`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.3** — `### 5.3 VL-C — texture classification (inference; the first judgment component)` (heading at line 338). A delegation at ARCHITECTURE.md:901 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. The document records this as the second of two build declarations the design owed and the build closed, decided at build by measurement rather than at design time; the closure names no ratifier. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-400 — A PER-VOICE span kind is admitted to the span typology — melodic phrases overlap across voices by construction and tile only within one voice

> - **A5 — the typology extension:** admit the **per-voice span kind** (phrase-spans: overlapping across voices by
>   construction, tiling within one voice) into ARCHITECTURE §2.15 — needed before VL-E's design can be written
>   against the typology.

**In plain words.** Until now every kind of span the analysis produces cuts across all the music at once. The melodic phrase does not: in contrapuntal writing the voices' phrases run concurrently and out of step with one another, as a fugue's staggered entries do. So a per-voice kind of span is admitted to the catalogue of span kinds, which is what a phrase-segmentation design can then be written against.

**Why.** Grounded in the musical fact it has to represent: phrases in contrapuntal textures are concurrent, overlapping and out of phase across voices, so they cannot be expressed as a partition of the music into successive stretches. The record also states what is deliberately not asserted — that consecutive phrases within one voice tile it exactly — because phrase elision makes a shared boundary note a real case, recorded as an open question for the segmentation design rather than assumed away.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:688-690`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§16** — `## 16. Ratification asks` (heading at line 680). The delegation names sections, and no delegation names this one. Decided by **D-430, the section-level unit — the delegation reaches named sections only, and no delegation names this section**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A5, recorded ratified in full at the banner. The propagation into the architecture document's span typology is recorded as riding the build. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-419 — Until the recognition consumer is built, the function layer does not touch the harmonic vocabulary

> 3. **Recognition consumer** — build + wire: the encyclopedia becomes L5's multi-chord disambiguation prior (the §5.5
>    resolver + the §8 forward-override) and L6's sequence-span annotation. **This is the step where L5 takes advantage of
>    the encyclopedia AND the five idioms** (the active idiom-mixture weights the matches). Until this exists, L5 does not
>    touch the encyclopedia.

**In plain words.** The reference catalog of named progressions and the function layer are connected by a separate piece of work that has not been built. Until it is, the function layer makes no use of the catalog at all — it is not a partial or optional connection, it is absent. That piece is also where the five idioms first do any work, by weighting which catalog entries count.

**Why.** It follows from the ratified build order stated at `:54` — encyclopedia, then the grouping layer, then wire the consumer — and from the catalog's own contract that it supplies ranked candidates and decides nothing (register entry D-407): with no consumer, there is nothing to receive the candidates, so a partial connection would be a consumer built by accident and unratified. Register entry D-084 records the same shape from the other side: the progression-schema recognizer is a CONSUMER of the function layer, not a new layer.

**Status.** LIVE · decided 2026-06-30 · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/implementation_roadmap.md:101`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **the opening block (above the first section heading)** — `# Consolidated Implementation Roadmap — Reviews → Plan` (heading at line 1). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `docs/implementation_roadmap.md`:59-62, inside the forward increment sequence whose header (`:54`) calls the order "ratified" — encyclopedia, then L6, then wire the consumer — without naming who ratified it or when; the surrounding block is dated 2026-06-30 at `:36`. The date recorded here is that block's date and the ratifier is NOT STATED, because the text asserts ratification without attributing it. The constraint governs Layer 5 and is recorded in a plan rather than in the Layer-5 specification, hence the documentation-gap flag. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

