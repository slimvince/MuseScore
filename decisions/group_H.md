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

**Why.** SEARCHED 2026-08-09 and the record holds NO derivation for the prohibition itself, though it states the rule sharply and in a form that shows what it protects. The home says the function layer *"reads the L4 chord **in** the L3 key"* and is *"additive over L4"*, and it names the two things the layer MAY do — annotate, and resolve carried abstentions by selecting among readings already handed to it (**D-080**). No reason is given for the boundary: nothing says why an annotating layer must not overturn the chord identity, no alternative is recorded as considered, and no measurement is attached. The general grounds that would supply one — #7's layer adherence, and the fact that a downstream rewrite would make the committed chord unfalsifiable at the layer that committed it — are nowhere stated as THIS decision's ground, and are not written in as one. Recorded as an established gap. Its live counterpart, which is a DIFFERENT decision and does carry a defense, is the confidence-weighted forward-override the same section names: where a later layer may move an earlier commitment, the record says so explicitly and bounds it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2078-2079`

**Provenance.** ARCHITECTURE.md:1389-1398 (Layer 5 - Built+Dormant, design ratified)

### D-080 — Carried abstentions are resolved by selecting among the carried readings, never re-derived

> the carried L4 abstentions are resolved by **selecting** among the carried readings (never re-derived)

**In plain words.** Where the chord stage could not decide, the function stage picks from the options it was handed. It does not work the chord out again from the notes.

**Why.** SEARCHED 2026-08-09. The record holds NO derivation as a stated reason, and it holds one STRUCTURAL fact that the rule follows from and that the home makes visible: the layer *"reads the L4 chord **in** the L3 key"* and is *"additive over L4"* (**D-079**), so re-deriving a reading from the notes would be the chord analysis run a second time, in a layer whose whole contract is that it does not do that. That is the rule restated at the boundary rather than a reason for drawing the boundary there, and the two are not conflated here. Nothing in the record says why SELECTING among carried readings is the right resolution rather than, say, re-deciding with the key now known; no alternative is recorded as considered and no measurement is attached. Recorded as an established gap. **What the record DOES establish, elsewhere and as a separate finding, is that this layer is the right OWNER of the resolution** — the same section states that the resolver of carried uncertain readings is this layer itself and not a distinct gated box, which answers WHERE and not WHY-BY-SELECTION.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2082-2083`

**Provenance.** ARCHITECTURE.md:1389-1398

### D-081 — The cadence detector is key-agnostic

> The cadence
> detector is **key-agnostic** (it votes for the key; it does not read a resolved key).

**In plain words.** The part that spots cadences must not be told what key it is in - it is one of the things that decides the key, so reading the answer first would be circular.

**Why.** Both rejected alternatives are named with their defect at the layer's own design document (`cowork_layer5_function_design.md` §9-D2, the same decision entered as **D-336**): the earlier key-dependent detector is circular and conflates the perfect with the imperfect cadence, and a single-chord interval test false-positives on tonic-to-subdominant and tonic-to-dominant because it tests whether the leading tone is *present* rather than whether it *resolves*. The same document records the approach's ratified limit (§5.2): a plain V-to-I and a plain I-to-IV are exact transpositions, so the resolution event alone cannot separate them — which is why the phrase gate, the dominant seventh, and the key layer's aggregation of the tonic votes carry the discrimination rather than the detector.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2082-2083`

**Provenance.** ARCHITECTURE.md:1397. open_items/OI-166 records that the built detector is key-agnostic but CHORD-derived, not the bass-driven pre-scan specified. Defense filled 2026-08-02 by the phase-1g triage wave from `cowork_layer5_function_design.md` §9-D2/§5.2 — the act the phase-1f note named and left for the wave that reads that document; the register entry for the same decision at its design-document home is D-336

### D-082 — The grouping layer is additive, read-only, with no feedback

> additive, read-only, no feedback into L5.

**In plain words.** The stage that assembles phrases and key areas only organises what earlier stages decided. It never changes their answers.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The record holds no reason for the additive, read-only, no-feedback constraint. The home states the rule and, in the same sentence, WHAT IT REPLACES — the forward-only rebuild of the scattered live cadence, pivot-chord and key-area machinery — which is a description of the change rather than a ground for the constraint. NOTHING IS BORROWED FROM THE NEAREST THING TO A REASON, and it is named so a later reader does not mistake it for this entry's: the key-area grouping rule further down the same section carries its own defense — that it is a grouping rule and not a second key analysis, reading the key fields the earlier layers already published rather than re-deciding them — and attributes that reasoning to "this layer's contract ... for grouping generally", i.e. to the delegated contract document rather than to this section. Whether that contract states a derivation for THIS constraint was not read by this fill and is not asserted.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2197`

**Provenance.** ARCHITECTURE.md:1400-1407 (Layer 6 - Design-only, v1 spec)

### D-083 — Hierarchy, periods and prolongation are out of the validatable core

> Hierarchy,
> periods/sentences, and prolongation are out of the validatable core (verifiability contract, §2.15).

**In plain words.** Deeper structural theory - nested hierarchy, periods, prolongation - is deliberately left out, because we have no annotated music to check it against.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The home NAMES A GROUND rather than stating a derivation, and that is more than an empty field but less than a reason: the exclusion is given as following from the "verifiability contract" (§2.15), in a parenthetical inside the decision's own sentence. So the defense is BY REFERENCE — the contract is what decides what sits inside the validatable core, and these three are outside it. Checked rather than assumed: the phrase "validatable core" occurs nowhere else in the document, so §2.15 is named as the governing contract rather than restating this exclusion, and no derivation is stated at the home itself.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2202-2203`

**Provenance.** ARCHITECTURE.md:1400-1407, deriving from D-029

### D-084 — The progression-schema recognizer is a consumer of the function layer, not a new layer

> an L5 *consumer* (a prior + an annotation), not a new layer

**In plain words.** Recognising well-known chord patterns is something that reads the finished analysis and annotates it. It is not another stage in the chain.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The record holds no reason for the classification. What stands in its place is a DESCRIPTION THAT ENTAILS IT, and it is recorded as that rather than upgraded: the home says the recognizer works over the COMMITTED progression, disambiguates through the forward-override and annotates the result as a grouping-layer span — which is what makes it a consumer of the finished analysis rather than a stage inside it. No alternative is weighed and no ground is given for preferring the consumer shape over a further layer. "Scaffolding-first, deferred" is a status, not a reason.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2259`

**Provenance.** ARCHITECTURE.md:1409-1414 'Scaffolding-first, deferred'

### D-085 — The voice-leading axis is a separate axis with its own layers

> the **orthogonal voice-leading axis** with its own layers (where melodic phrases [MT] and
>   chord **voicing / arrangement** are analysed)

**In plain words.** How the individual voices move is a second, independent line of analysis alongside the harmonic one, with its own stages.

**Why.** Argued in the axis's own design document against the three co-equal admission gates the architecture requires of any new axis (`cowork_voiceleading_axis_design.md:510-518`, decision D1). (1) Separation of concerns: linear structure is a distinct responsibility no harmonic layer may absorb, and the grouping layer's own specification excludes it explicitly. (2) Verifiability: the motion and interval statistics are facts, an oracle by construction; the texture classification validates under the discovery protocol; stream separation validates against the notated voices. (3) Proportionality: the axis buys a second style coordinate MEASURED orthogonal to the harmonic one — cross-agreement 0.030 over 1,283 dual-view pieces — plus an owner for the melodic phrase, the galant patterns and chord voicing, which are otherwise homeless, and the evidence base for the non-chord-tone lever the dormant full-spine measurement sized at about 45 % of the exact-match ceiling. The alternative weighed and rejected: folding the motion features into the harmonic spine's half-tier as another derived view, which would leave the judgment components (texture, phrases) with no home and mix this axis's concerns into that tier.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Home.** `ARCHITECTURE.md:1190-1191`

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

**Home.** `ARCHITECTURE.md:7294-7296`

**Provenance.** ARCHITECTURE.md:6012-6014. Section 5.10 (ARCHITECTURE.md:3860) is the tonicization section; the memory-held backlog item is recorded in the same terms. ★ RATIFIED (user, 2026-08-02) with the revisit to be PLANNED: for the ultimate objective (maximum-precision inference) the feature may be needed — the ground truth annotates applied chords, so not producing them costs Roman-numeral agreement wherever the annotator wrote one. Row OI-267 carries the planning obligation, including the OI-53 tension (a live classifier emitting V7/x was found on the legacy path while this entry's home says not implemented). ★ SCOPE CORRECTED 2026-08-02 (CC, at the phase-1i delivery acts, on Cowork's measured probe finding B-1, user-reviewed): the entry's verbatim is a statement about the LEGACY `ChordFunction` structure, and its plain restatement wrongly generalized it to the whole system. The production joint estimator — the inference layer on both surfaces since the OI-178 adoption — DOES emit applied labels (`src/composing/analysis/joint/jointrender.h:62-63`; measured 8.62 % of scored duration, with exact matches against applied ground truth: `tools/joint_estimator/applied_chord_stake_2026_08_02/`). The OI-53 tension named above is therefore substantially ANSWERED: the joint surface emits applied labels, the legacy `ChordFunction` structure does not carry them. The decision itself is unchanged and stays DEFERRED for the surface it governs; what changed is the recorded scope.

### D-291 — The tonicization labeller is NOT wired - wiring it would raise the reported agreement while hiding a real key error

> **★ THE TONICIZATION LABELLER IS DELIBERATELY LEFT UNWIRED, AND THE REAL LEVER IS AT THE KEY LAYER
> (2026-06-14; the record states no ratifier for the decision itself. Written into this section
> 2026-08-09 on the user's ruling — the BUILD half of register entry **D-291**, whose measurement half
> belongs to the grading conventions and is not restated here, #6).** A working labeller for applied
> chords exists and **must not be wired on the ground that it raises Roman-numeral agreement**.

**In plain words.** A working labeller for applied chords was deliberately left unwired, and the proposal to make the accuracy measurement treat its labels as equivalent to the annotator's was rejected. Both would have raised the reported Roman-numeral agreement while the underlying reading stayed wrong: the annotator has changed key, and labelling the chord relative to the old key hides that.

**Why.** Measured: of the affected cases 92.7 % are cadence-confirmed local keys in the ground truth and 79.2 % last five chords or more, so the annotator's modulation is correct for about 97 % of them; only 2.7 % are brief enough for either reading to be defensible. The comparison already credits the label by root and quality, so it does not over-penalise - it MASKS. Recorded as the clearest win of the measure-before-building rule: without the check the labeller would have shipped and improved the number while worsening the output.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:2164-2168`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 metric-check block), citing `cc_tonicization_modulation_metric_dossier.md`. The same block relocates the largest accuracy slice from the function layer to the key layer. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ SPLIT 2026-08-09 ON THE USER'S RULING 7 OF 2026-08-09 (`cowork_rulings_2026_08_09_return.md`; CC, `cc_instruction_return_continuation.md` Task 2) — TWO DECISIONS, TWO OWNERS (#7), AND ONLY ONE HALF LANDED. The 2026-08-08 hold's own text is kept below, unedited (#12). **THE BUILD HALF IS HOMED**, at `ARCHITECTURE.md`'s Layer-5 function section — the layer that would have consumed the labeller — in that section's own voice, with its defense: that the comparison scores by root and quality rather than against the Roman numeral's reference key, so an applied-chord label in the home key is ALREADY partially credited and the comparison MASKS rather than over-penalises; that the affected cases are overwhelmingly cadence-confirmed local keys of substantial length; and that the lever therefore sits at the KEY layer as a local-modulation / key-area detector. The verbatim above is RE-TAKEN from that home. NO MEASURED VALUE IS CARRIED INTO THE SPECIFICATION (**D-431**) — every percentage stays in `cc_tonicization_modulation_metric_dossier.md`, which the home text cites. FORMER HOME, PRESERVED (#12): `cowork_handoff_archive.md:3833`; the archive is UNTOUCHED. FORMER CLASS, PRESERVED (#12): `unhomed`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **★ HEADROOM CORRECTION (load-bearing — propagate to docs):** the biggest precision slice relocates **Stage 6 → Stage 4** (local-modulation\n  detection). **Do NOT wire 6-tonic-i** (games rn_agree, degrades correctness). Real lever = a **LOCAL-MODULATION / KeyArea detector\n  (Stage 4)**, ~95% of S1, signal = sustained span + local cadence (consumes the committed CADENCE INSTRUMENT + KeyArea); 6-tonic-i's" ★ **AND THE MEASUREMENT HALF IS A STOP BACK TO THE USER — THE RULING'S OWN CONDITION IS NOT MET (2026-08-09).** Ruling 7 rules the measurement half ONE DECISION RECORDED TWICE, with `CLAUDE.md` gate block (A)'s same-date convention standing as its single home, **on the condition that the two texts are the same binding statement, compared verbatim before the act; any binding difference is a STOP.** The comparison was made verbatim at both texts and **they are not the same binding statement.** THIS half, at its source, reads *"Crediting rule NOT warranted (harmful — masks the 95% real error); only a DIAGNOSTIC partial-sub-split (expose the masking) is defensible"* — it forbids AMENDING THE GRADING CONVENTION so that a tonicization label counts as agreeing with the annotator's modulated numeral. The gate-block-(A) convention reads *"THE BINDING METRIC FOR A MODULATION DETECTOR IS MODULATION CORRECTNESS — explicitly NOT the agreement percentage … A change that decides where the music changes key is judged on whether the key changes it commits are real ones (precision) and whether it finds the real ones (recall) — the track rate together with the de-masked partial split — and never on the overall agreement percentage"* — it fixes WHICH BAR a modulation-detecting change is graded against. **The two overlap in date, in source dossier, in the masking argument and in naming the de-masking diagnostic as the honesty measurement — and they still forbid different acts.** A session could obey the gate-block convention, grading a new detector on precision and recall, and still amend the crediting rule, which THIS half forbids and which would corrupt the Roman-numeral column for every measurement rather than for that change alone; conversely a session could leave the comparison untouched and grade a detector on the agreement percentage, which the gate-block convention forbids and this half does not address. Collapsing the two would therefore LOSE the more specific and more easily violated prohibition (#12). **So the measurement half is NOT recorded as one decision recorded twice, it is NOT homed, and NOTHING was written for it** — it returns to the user with this comparison as the evidence, which is the ruling's own stated outcome for a binding difference. ★ **AND THE USER ANSWERED IT: THE MEASUREMENT HALF IS NOW HOMED, SIDE BY SIDE (user, 2026-08-09, Ruling 11 of `cowork_rulings_2026_08_09_second_stop.md`; CC, `cc_instruction_return_continuation_2.md` Task 0).** The two are ruled TWO DECISIONS sharing a date and an argument, and the measurement half is written into `CLAUDE.md` gate block (A) BESIDE the modulation-correctness convention rather than into it, each of the two cross-referencing the other, with the specific prohibition — *"Crediting rule NOT warranted (harmful — masks the 95% real error); only a DIAGNOSTIC partial-sub-split (expose the masking) is defensible"* — carried in the words it was recorded in (#12) and no already-ruled text reworded (#14). The percentage inside that quotation is the source's own wording and the home says so; every value of the measurement stays in `cc_tonicization_modulation_metric_dossier.md` (#17f, **D-431**). THE EXCLUDED ALTERNATIVE, RECORDED: widening the existing convention and retiring this half into it — a merge of two differently-binding rules, editing a user-homed text, with paraphrase risk to the more specific prohibition (#12); #6 does not demand it, since #6 forbids two homes for ONE rule and these are demonstrably two. **THE `home` FIELD ABOVE IS UNMOVED AND STILL NAMES THE BUILD HALF'S HOME**, which is where this entry's `verbatim` is located and verified; whether the measurement half now warrants its own register identifier is a question about register CONTENT, not a filing act, and it is put to the user in the ratification queue `ratification_surfaces/cowork_ruling_registration_queue_2026_08_09.md` rather than decided by a session. ★ HELD, NOT HOMED, 2026-08-08 (CC, `cc_instruction_away_execution.md` Task 2), on assumption A3's owner-determinacy test — **and it fails that test for an unusual reason: the entry is TWO decisions with two different owners.** Its first half is a BUILD decision — a working labeller for applied chords is deliberately left unwired — whose owner is the layer that would have consumed it. Its second half is a MEASUREMENT CONVENTION — the accuracy measurement is NOT changed to treat the labeller's output as equivalent to the annotator's — whose owner is `CLAUDE.md` gate block (A), where the grading conventions live. Homing the entry whole would put a measurement convention into a layer specification or a build decision into the gate block; splitting it is a register act, not a filing one. **AND THE SECOND HALF LOOKS ALREADY HOMED, which is why this is reported rather than merely deferred.** Gate block (A) carries a grading convention dated 2026-06-14 — the same date as this entry — stating that the binding metric for a modulation detector is modulation correctness and explicitly NOT the agreement percentage, and naming the de-masking diagnostic as the honesty measurement beside it. That is this entry's masking argument, in the same words and from the same day. Whether the two are one decision recorded twice, or two decisions that happen to share a date and an argument, is a question about the record's own content and is the user's to settle; asserting either would be a session deciding a supersession. The archive is untouched (#12) and nothing was written. ★ **AND THE REGISTER-CONTENT QUESTION THAT RODE WITH IT IS ANSWERED: THIS ENTRY IS SPLIT INTO TWO IDENTIFIERS (user, 2026-08-09, Ruling 21 of `cowork_rulings_2026_08_09_fourth_stop.md`; CC, `cc_instruction_return_continuation_4.md` Task 0).** The queue the previous continuation put the question to — whether the measurement half now warrants its own register identifier — is ruled YES, on the ground that an ENTRY is the register's findability unit, which is the same reasoning as Ruling 11 one level up. **THIS ENTRY KEEPS THE BUILD HALF** — the tonicization labeller deliberately left unwired, homed at the Layer-5 function section, which is where this entry's `verbatim` is located and verified — and **the MEASUREMENT half is now D-656**, homed in `CLAUDE.md` gate block (A) beside the modulation-correctness convention, exactly where Ruling 11 put it. Neither text was reworded (#14) and no field of this entry was deleted (#12); what changed here is the title, and the FORMER TITLE IS PRESERVED WHOLE: "The tonicization labeller is NOT wired, and the metric is NOT changed to credit it - both would hide a real key error". The `rationale` field above still states the defense of BOTH halves as the record gives it, which is accurate — the two halves share one measured ground — and D-656 carries its own statement of it. Cross-ref **D-656** (the measurement half), **D-650** (the verbatim-comparison condition and the side-by-side remedy under which both halves were homed).

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

**Home.** `cowork_layer5_function_design.md:621-626`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 620). A delegation at ARCHITECTURE.md:2086 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer5_function_design.md:627-631`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 620). A delegation at ARCHITECTURE.md:2086 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-337 — A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost

> - **D3 — Tonicization is the default; modulation requires cadence confirmation plus persistence, as a change-cost.**
>   *Rejected:* a fixed-duration rule (no published threshold exists and the boundary is a continuum); and resolving the
>   distinction in the key layer (it needs function). The hysteresis over the local-key decision matches the ground-truth

**In plain words.** When the music leans toward a note other than the home tonic, the home key holds and the chord is written as an applied chord. The key changes only when a cadence confirms the new key and the music stays in it; how long it must stay is a cost that falls as the candidate area grows, not a fixed number of bars.

**Why.** Both alternatives are rejected with reasons: a fixed-duration rule has no published threshold and the boundary is a genuine continuum, and resolving the distinction in the key layer cannot work because it needs function. The hysteresis form is chosen because it matches the ground-truth annotation convention.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:632-634`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 620). A delegation at ARCHITECTURE.md:2086 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer5_function_design.md:636-639`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 620). A delegation at ARCHITECTURE.md:2086 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_layer5_function_design.md:556-563`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§7** — `## 7. Data design` (heading at line 546). A delegation at ARCHITECTURE.md:2086 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-341 — The licensed root-motion set is completed by theory — the ascending fifth, the descending second and the diatonic diminished fifth are added

>   **(★ THE GRAMMAR-COMPLETION AMENDMENT — found 2026-07-02 by the D5 consistency check; ★ RATIFIED by the user
>   2026-07-03; in force in this spec, not yet in code — the code increment is pending):** the pre-amendment
>   set descended from the old scoring-bonus signals and omitted three theory-licensed motions the catalog's
>   musically-correct
>   entries exercise; the licensed set now **also includes**: **the ascending fifth** (tonic→dominant and plagal
>   motion — I→V, IV→I), **the descending second** (the Phrygian/Andalusian step — i→♭VII, ♭VII→♭VI, ♭VI→V), and **the
>   diatonic diminished fifth** (the IV→viiᵒ link of the full circle of fifths). This is **algorithmic completion per
>   theory, NOT tuning**. Implementation = its own small dormant
>   increment (`isLicensedProgression` + tests, instruction pending dispatch); the consumer's D5 consistency test then
>   empties its 11-motion known-gap list and tightens to the clean assert. Until that increment lands, the code
>   implements the pre-amendment set — a known, ruled spec-ahead-of-code state.
>   **Evidence:** the 6-entry/**11-motion** failure table, measured, enumerated and
>   pinned in the consumer's consistency test (`EXPECT_EQ(failing.size(), 11u)`) — the earlier "12" was a Cowork
>   arithmetic error, corrected 2026-07-02 (U2); the measured 11 is authoritative.

**In plain words.** The list of chord-to-chord root motions the analysis treats as real functional progressions was inherited from an older scoring mechanism and left out three motions that standard theory licenses and the project's own catalogue uses. They are added. This is completing an algorithm against theory, not tuning it.

**Why.** Measured by the catalogue-versus-grammar consistency check: six catalogue entries exercising eleven motions failed against the grammar as coded, and the eleven are enumerated and pinned in the consumer's own test. The three missing motions are tonic-to-dominant and plagal motion, the Phrygian step, and the diminished fifth that closes the circle of fifths.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:203-216`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.0** — `### 5.0 Shared definitions (the terms the rules below stand on)` (heading at line 158). A delegation at ARCHITECTURE.md:2086 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping). **HOMED IN A SECTION THAT RECORDS FINDINGS (2026-08-03, phase 1r).** The delegation the user wrote for `cowork_layer5_function_design.md` names the whole document and so reaches §15, but §15 is an open-items list and fails D-430's rule-stating half, so this entry stays `gap` while the document's other seven move. The kind judgment follows the user's own adjacent ruling of the same day, which excludes the identically-titled §15 of the sibling voice-leading design as "ratification asks, not rule-stating sections". Because this decision IS a ratified rule, the mismatch is a finding about the DOCUMENT, not about the entry: rowed at `OPEN_ITEMS.md` OI-295, the `OPEN_ITEMS.md` OI-290 shape at a second document. The remedy is to move the amendment into §5.0, the section it amends. **THE REMEDY IS EXECUTED (2026-08-03, phase 1s, on the user's ruling Y3 — fix it at the DOCUMENT, not at the classification).** The amendment now lives in §5.0's licensed-progression definition, the section its own verbatim says it amends, and §15 item 12 keeps a dated note recording that it moved and where — the tracking history preserved, the rule not duplicated (#6). **One thing the dispatch did not predict, and it changed what "move the rule text" meant:** §5.0 ALREADY carried the amendment's enumeration, inserted when the amendment was ratified ("+ this §5.0's enumeration, now done", the former verbatim). Moving the §15 text wholesale would therefore have DUPLICATED it. What moved instead is the part §15 alone carried — the ratification marker with its finding date, the completion-not-tuning characterization, and the 6-entry/11-motion evidence — moved unchanged (#12), so the section now states the rule AND carries its defense at its home. The former verbatim (the §15 item-12 text) is preserved here: "12. **★ §5.0 grammar completion (found 2026-07-02 by the D5 consistency check — ★ RATIFIED by the user 2026-07-03; the §5.0 enumeration is amended, the code increment is pending).** The licensed root-motion set descended from the old scoring-bonus signals and omitted three theory-licensed motions the catalog's own musically-correct entries exercise: **ascending fifth / plagal motion** (IV→I, I→V — tonic-to-dominant!), **descending second** (the Phrygian/Andalusian step), and the **diatonic diminished fifth** (the IV→viiᵒ link of the full circle). The amendment: extend `isLicensedProgression` (+ this §5.0's enumeration, now done) accordingly — algorithmic completion per theory, NOT tuning; its own small dormant increment with tests; the consumer's consistency test then tightens to the clean assert. Evidence: the 6-entry/**11-motion** failure table, measured, enumerated and", and the former home was `cowork_layer5_function_design.md:888-897`. The §15 kind judgment that produced this row's `gap` — that §15 RECORDS FINDINGS, on the user's own adjacent ruling of the same day about the identically-titled §15 of the sibling voice-leading design — is retired from the authored block because it now decides no entry, and is preserved here instead of being deleted. `OPEN_ITEMS.md` OI-295 flips.

### D-342 — Putting the function layer into production is DEFERRED INDEFINITELY — the posture is a dormant build with ground-truth validation

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Engagement framing.** References to an "engagement hard-stop" / "before any production switch" (§5/§10) remain true
>   *conditionally* — engagement (Phase 5d) is **deferred indefinitely** (production out of scope; the posture is dormant
>   build + ground-truth validation). The hard-stops apply *if* a switch is ever made; they are not pending work.

**In plain words.** Switching the function layer on in the product is not scheduled. It is built and checked against published human analyses, and stays inactive; the conditions written for a switch apply if one is ever made, and are not outstanding work. THIS IS NOT THE INFERENCE-ENGINE SWITCH - that happened (D-010): the joint estimator is production and the legacy pipeline is dormant. This entry concerns the separate Layer-5 function-annotation module, built and validated but never in production in either era. Its concerns are handled by the LIVE implementation natively or by schedule: degree-in-key Roman numerals are the estimator's own state; key changes are decided inside the decode; applied-chord labels are emitted by the live renderer (the D-248/OI-267 revisit covers the remainder); cadence is a fitted factor inside the model and a marker on the presentation surface; carried-abstention resolution is obviated by the full-posterior publication (D-006); the ornament labels are the ratified OI-194 increment; and the complete concern-by-concern mapping of the legacy layer's remaining scope is the OI-259 phase-3 re-disposition.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The home states a GROUND in a parenthetical rather than a derivation, and it is recorded as that: engagement is deferred indefinitely "(production out of scope; the posture is dormant build + ground-truth validation)". So the reason given is a SCOPE DECISION taken elsewhere and applied here, together with the posture it leaves in place — built, validated against published human analyses, and inactive. What the record does NOT hold at this entry is any argument for that scope decision, and no alternative is weighed. The entry's plain restatement carries a concern-by-concern mapping of how the live implementation handles what this layer would have done — which is a statement about the live system rather than a defense of the deferral, and is not read as one. ⚠ Legacy subject; the hard-stops written for a switch apply IF one is ever made and are not pending work, which the decision itself says.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:705-707`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 678). A delegation at ARCHITECTURE.md:2086 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home section.** **“§3.1 The objective: select by JOINT CONSISTENCY, not by strengthening one score”** — `### §3.1 The objective: select by JOINT CONSISTENCY, not by strengthening one score` (heading at line 186). A delegation at ARCHITECTURE.md:2106 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home section.** **“§3.2 The evidence channels, ranked by the research”** — `### §3.2 The evidence channels, ranked by the research (load-bearing first) [research]` (heading at line 200). A delegation at ARCHITECTURE.md:2106 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home section.** **“§4.1 Layer boundaries”** — `### §4.1 Layer boundaries (#7) — what belongs where` (heading at line 255). A delegation at ARCHITECTURE.md:2106 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home section.** **“§7.2 The vehicle”** — `### §7.2 The vehicle (#6, the load-bearing decision): unify the open-mark, do NOT add a parallel channel` (heading at line 468). A delegation at ARCHITECTURE.md:2106 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_voiceleading_axis_design.md:545-548`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 534). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. The document's banner records `Status: SIGNED (user, 2026-07-03 — asks A1–A8 ratified in full)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-389 — A notated voice is a FACT and an inferred perceptual line is a JUDGMENT — the two are separate types and are never conflated

> - **D3 — two-tier voice model: notated voice = fact; stream = inference.** Never conflated; enforced by the §0
>   one-sense rule and the type system (VoiceLine vs Stream). *Alternative rejected:* a single "voice" concept with
>   a quality flag — exactly the silent fact/judgment mixing the universality principle forbids.

**In plain words.** The line the score actually writes and the line a listener hears are different things and are kept apart, in the words used and in the types the code carries. The written one is a fact taken from the score; the heard one is always called a stream, is always marked inferred, and carries its own confidence. Merging them into one idea with a quality flag was considered and rejected.

**Why.** The rejection has a principled ground: one idea with a quality flag is exactly the silent mixing of fact with judgment that the universality principle forbids — the fact layers must stay style-agnostic and free of inference, so a value that is sometimes read and sometimes guessed cannot live in one field. The separation is enforced twice over, by the document's one-sense vocabulary rule and by the type system.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:549-551`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 534). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_voiceleading_axis_design.md:552-555`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 534). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_voiceleading_axis_design.md:559-567`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 534). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A8, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-392 — The later voice-leading components are CLAIMS WITH OWNERS, not builds — each clears its own design document and its own evidence before any instruction exists

> - **D5 — staged components behind design gates.** VL-D/E/F/G/H are claims with owners, not builds; each clears its
>   own design + footing before an instruction exists. This is the proportionality gate applied *inside* the axis —
>   no slot-filling (the Contrapunctus reminder). *Alternative rejected:* one monolithic axis build.

**In plain words.** Stream separation, phrase segmentation, pattern recognition, voicing analysis and part-writing advice are all named and assigned, but none is built. Each first needs its own design document and the evidence to stand on. Building the whole dimension in one go was considered and rejected.

**Why.** The record names the principle and the failure it guards against: this is the proportionality admission gate applied inside the dimension rather than only at its border, and the guard is against slot-filling — building a component because a slot exists for it rather than because evidence earned it.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:556-558`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (alternatives weighed)` (heading at line 534). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_voiceleading_axis_design.md:372-377`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.3** — `### 5.3 VL-C — texture classification (inference; the first judgment component)` (heading at line 364). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_voiceleading_axis_design.md:330-334`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.1** — `### 5.1 VL-A — the voice-linear view (representation; facts)` (heading at line 315). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_voiceleading_axis_design.md:402-407`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.3** — `### 5.3 VL-C — texture classification (inference; the first judgment component)` (heading at line 364). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. All three floor values are recorded as precision-phase constants, not fixed here. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-396 — The voice-leading dimension covers NOTATED music only, and its style coordinate is UNDEFINED — not zero — for sources that carry no voices

> - **Coverage declaration (honest, structural).** The axis analyses **notated music only** — lead-sheet sources
>   carry no voices, so the voice-leading coordinate of the 2-D style structure is simply *undefined* for them
>   (undefined, not zero, in every consumer). This is a representational fact, not a corpus accident.

**In plain words.** This dimension reads the lines a score writes, so a source that carries no lines at all, such as a lead sheet, has no voice-leading character to read. Every consumer must treat that coordinate as undefined rather than as zero, because a missing measurement is not a measurement of nothing.

**Why.** The record grounds it as a property of the representation rather than of the corpora held: a lead sheet does not fail to have voices for want of a better encoding, it has none by what it is. The distinction between undefined and zero is what stops a downstream consumer from reading absence as a low score.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:528-530`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8** — `## 8. Crosscutting concepts` (heading at line 510). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A6, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-397 — The homeless analysis objects are ASSIGNED to named owners on the voice-leading dimension — the stock patterns, the melodic phrase, chord voicing, and part-writing advice — as claims, discharged only at each owner's own ratified design

> **★ FOUR ANALYSIS OBJECTS THAT HAD NO OWNER ARE OWNED BY THE VOICE-LEADING AXIS, AS CLAIMS (user-ratified
>   2026-07-03; written here 2026-08-09).** Growth by axis only works if every analysis object has a named owner, and
>   four did not. They are assigned here, and each is recorded **as a CLAIM with an owner rather than as work
>   started** — a claim is discharged only when that component's own design is ratified, never by this line.

**In plain words.** Four kinds of analysis object that previously had no owner are assigned here: the stock eighteenth-century patterns and the chromatic line cliché, which the chord dictionary already flags as belonging to this dimension; the melodic phrase; chord voicing and arrangement, which the dictionary explicitly excludes from its own scope; and checking and advising on part-writing. Each is recorded as a claim with an owner, not as work started, and the claim is settled only when that owner's own design is ratified.

**Why.** The assignment is grounded in what defines each object: the stock patterns are defined primarily by a paired outer-voice scale-degree skeleton — that is, by voice leading — which the built chord catalogue already records with a voice-leading-defined flag on six entries, verified at that catalogue. The phrase assignment is the other side of a ruling already made on the harmonic side, where the grouping layer deliberately does not segment the melodic phrase.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1197-1200`

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A7, recorded ratified in full at the banner. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-HOMED 2026-08-09 under the user's Ruling 38 of `cowork_rulings_2026_08_09_sixth_stop.md`, by `cc_instruction_return_continuation_6.md` Task 1. The owning section is the `ARCHITECTURE.md` §2.15 paragraph that states GROWTH BY AXIS AND BY COMPONENT and names the orthogonal voice-leading axis with its components — an ownership assignment belongs where the ownership map is stated, and that paragraph already names the axis as the place melodic phrases and chord voicing are analysed. The homing keeps the entry's own form: each object is written in AS A CLAIM with its owner, with the record's own condition that a claim is discharged only at that component's ratified design and never by the architecture line. THE COMPONENT CODE NAMES ARE DELIBERATELY NOT CARRIED into the specification text — the objects are named in plain words, because a reader of the architecture meets an object rather than a component identifier, and the identifiers live in the axis design this section delegates to (#6, and the code-mechanics-in-prose rule of the writing standards). The verbatim is RE-TAKEN from the new home. FORMER HOME, PRESERVED (#12): `cowork_voiceleading_axis_design.md:693-696`, §16. FORMER CLASS, PRESERVED (#12): `gap`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **A7 — the claims registry:** VL-F claims the six voice-leading-defined Vocabulary entries; VL-E claims the\n  melodic phrase [MT]; VL-G claims voicing/arrangement (the dictionary §5.3 exclusion); VL-H claims part-writing\n  checking & suggestion (the advisory consumer, incl. the VL-B per-sample motion-event export that serves it).\n  Recorded as claims with owners, discharged only at each component's own ratified design." THE FORMER HOME-CLASS RULING, PRESERVED (#12) AND NOT WITHDRAWN — it settled the DELEGATION question for §16 and this act settles the ENTRY, the split the finish line's own gate note draws: "★ THE HOME CLASS IS SETTLED BY RULING AND IS NOT OWED WORK (user, 2026-08-04, ruling R2, dispatch `cc_instruction_census_delegation_and_commit.md`): the `ARCHITECTURE.md` delegation is NOT widened to reach §16, so this entry stays `gap` deliberately. §16 holds the ratification asks put TO the user — this entry is ask A7 — and an ask is not a rule, so forcing it a contract home would misdescribe what it is; D-430's kind half would exclude the section at the next run in any case. THIS IS A RULING, NOT A DEFERRAL: no later wave owes a delegation act here." §16's ask is left standing where it is (#12). No count is carried into the specification (#17f, D-431): the catalogue's voice-leading-defined entries are named as a class rather than by number.

### D-398 — Parallel motion is judged SEMITONE-EXACT, not by generic diatonic size — a same-direction move whose semitone interval changes counts as similar motion

> **★ "INTERVAL PRESERVED" IS SEMITONE-EXACT, NOT GENERIC DIATONIC SIZE — CLOSED AT BUILD, 2026-07-03.** Two lines
>   count as **parallel** only when they move the same direction AND the SIGNED SEMITONE distance between them is
>   unchanged; a same-direction move whose semitone interval changes is **similar**. So a pair moving from a major
>   third to a minor third is similar motion, not parallel, although both are thirds on the staff.

**In plain words.** Two lines count as moving in parallel only when they move the same way and the distance between them in semitones is unchanged. A pair moving the same way from a major third to a minor third is therefore similar motion, not parallel, even though both are thirds. The alternative — counting by the size of the interval as written on the staff, so that any third to any third is parallel — was the open question, and this is the answer.

**Why.** Settled by replication rather than by choice: the convention was read off the exploratory study's own motion classifier at source and reproduced exactly in the production code, which is oracle-tested against it. Fixing it this way is what makes the production implementation reproduce the study's features, which the design requires of it.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:109-112`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“Accepted music-theory terms [MT]”** — `### Accepted music-theory terms [MT]` (heading at line 99). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. The document records this as one of two build declarations the design owed and the build closed; the closure names no ratifier. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-HOMED 2026-08-09 under the user's Ruling 38 of `cowork_rulings_2026_08_09_sixth_stop.md` (re-homing is the DEFAULT closing route for finish-line item 1 and no document is excepted), by `cc_instruction_return_continuation_6.md` Task 1. The rule is written into §0, the delegated TERMINOLOGY section, at the very bullet that defines the motion types — because that bullet is where the ambiguity lives: it says 'harmonic interval preserved' and a reader meets the undecided word there. The homing is ALSO a doc-sync correction (C3): that bullet closed by calling the reading 'an implementation declaration owed at build', which is FALSE at HEAD, and the former wording is preserved in place (#12). The §15 tracking line is untouched and the verbatim is RE-TAKEN from the new home rather than transcribed. FORMER HOME, PRESERVED (#12): `cowork_voiceleading_axis_design.md:632-635`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "2. **The \"parallel\" interval-preservation convention** (semitone-exact vs generic-diatonic) — ✅ **CLOSED at build\n   (AS-BUILT, 2026-07-03): SEMITONE-EXACT.** Verified at `voiceleading2.py` `_motion`: `parallel` iff both voices\n   move the same direction AND `(pu1−pv1)==(pu0−pv0)` on signed MIDI pitches (a same-direction move whose semitone\n   interval changes is `similar`). Replicated exactly in `voiceleadingprofiles.cpp classifyMotion` (oracle-tested)." THE FORMER HOME-CLASS RULING, PRESERVED (#12) AND NOT WITHDRAWN — it settled the DELEGATION question and this act settles the ENTRY, which is the split the finish line's own gate note draws: "★ THE HOME CLASS IS SETTLED BY RULING AND IS NOT OWED WORK (user, 2026-08-04, ruling R2, dispatch `cc_instruction_census_delegation_and_commit.md`): the `ARCHITECTURE.md` delegation is NOT widened to reach §15, so this entry stays `gap` deliberately. §15 is 'Open items & deferred refinements', a tracking list of what is owed or since closed — the shape the record has declined as a home elsewhere — and D-430's kind half would exclude it at the next run in any case. THIS IS A RULING, NOT A DEFERRAL: no later wave owes a delegation act here." No code identifier or commit is carried into the specification text (#17f, D-431); the implementation evidence stays in this field and in §15's closure line.

### D-399 — The texture feature space was decided BY MEASUREMENT among three named candidates — the standardized combination of both views won; the unstandardized combination was rejected before testing for a measured dilution

> **★ AS-BUILT: the winner is the z-scored
>   concatenation (ABz)** — measured by `run_vl_feature_space.py` (nearest-centroid reproduction of the ratified AB K=4
>   partition, cap=80/source, seed 0): **ABz ARI 0.791 / accuracy 0.918**, two-stage 0.716, motion-only 0.258 (raw
>   concatenation rejected a priori).

**In plain words.** Which numbers the texture decision is made from was not chosen by argument. Three candidates were tested against one criterion: reproduce the classes the earlier study established. Putting both kinds of statistic together after standardizing them reproduced those classes best. Putting them together without standardizing was ruled out in advance, because the sixteen interval numbers would simply outvote the four motion numbers.

**Why.** Measured, with the numbers recorded: nearest-centroid classification in the standardized combined space reproduces the ratified four-class partition at an agreement index of 0.791 and an accuracy of 0.918, against 0.716 for the two-stage alternative and 0.258 for motion alone. The declared tolerance was met with margin, so no stop fired. The resulting reference set ships as generated code with its full provenance — the run, the corpus state, the number of classes, the seed and the library version — and is refit at corpus waves under the same protocol as the harmonic taxonomy.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_voiceleading_axis_design.md:394-397`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.3** — `### 5.3 VL-C — texture classification (inference; the first judgment component)` (heading at line 364). A delegation at ARCHITECTURE.md:1147 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL. The document records this as the second of two build declarations the design owed and the build closed, decided at build by measurement rather than at design time; the closure names no ratifier. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-400 — A PER-VOICE span kind is admitted to the span typology — melodic phrases overlap across voices by construction and tile only within one voice

> **★ THE TYPOLOGY ADMITS A PER-VOICE SPAN KIND (user-ratified 2026-07-03; written here 2026-08-09).** Every span
>   kind listed above cuts across the whole texture at once — it is a segmentation of the music, and the members of
>   one kind tile it. **A MELODIC PHRASE DOES NOT.** In contrapuntal writing the voices' phrases run concurrently and
>   out of step with one another, as a fugue's staggered entries do, so phrase-spans **overlap across voices by
>   construction and tile only WITHIN one voice**. The typology therefore carries a second kind of member: a
>   **per-voice span**, whose tiling law is stated per voice rather than over the texture.

**In plain words.** Until now every kind of span the analysis produces cuts across all the music at once. The melodic phrase does not: in contrapuntal writing the voices' phrases run concurrently and out of step with one another, as a fugue's staggered entries do. So a per-voice kind of span is admitted to the catalogue of span kinds, which is what a phrase-segmentation design can then be written against.

**Why.** Grounded in the musical fact it has to represent: phrases in contrapuntal textures are concurrent, overlapping and out of phase across voices, so they cannot be expressed as a partition of the music into successive stretches. The record also states what is deliberately not asserted — that consecutive phrases within one voice tile it exactly — because phrase elision makes a shared boundary note a real case, recorded as an open question for the segmentation design rather than assumed away.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1153-1158`

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_voiceleading_axis_design.md` IN FULL; it is ratification ask A5, recorded ratified in full at the banner. The propagation into the architecture document's span typology is recorded as riding the build. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue). ★ RE-HOMED 2026-08-09 under the user's Ruling 38 of `cowork_rulings_2026_08_09_sixth_stop.md`, by `cc_instruction_return_continuation_6.md` Task 1, INTO THE SECTION THE ENTRY'S OWN TEXT NAMES — the ask says in terms that the per-voice span kind is admitted 'into ARCHITECTURE §2.15', so the owning section is determinate from the record and nothing is sited by judgment. The propagation this ask recorded as riding the build had never been performed: §2.15's typology carried no per-voice member, so a design written against the catalogue would have found every kind tiling the whole texture. The home text carries the rule, its defense (the musical fact of concurrent, out-of-phase phrases in contrapuntal writing) and the thing the record deliberately does NOT assert (that consecutive phrases within one voice tile it exactly — phrase elision makes a shared boundary note a real case, recorded as an open question for the segmentation design). The verbatim is RE-TAKEN from the new home. FORMER HOME, PRESERVED (#12): `cowork_voiceleading_axis_design.md:688-690`, §16. FORMER CLASS, PRESERVED (#12): `gap`. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **A5 — the typology extension:** admit the **per-voice span kind** (phrase-spans: overlapping across voices by\n  construction, tiling within one voice) into ARCHITECTURE §2.15 — needed before VL-E's design can be written\n  against the typology." THE FORMER HOME-CLASS RULING, PRESERVED (#12) AND NOT WITHDRAWN — it settled the DELEGATION question for §16 and this act settles the ENTRY, which is the split the finish line's own gate note draws: "★ THE HOME CLASS IS SETTLED BY RULING AND IS NOT OWED WORK (user, 2026-08-04, ruling R2, dispatch `cc_instruction_census_delegation_and_commit.md`): the `ARCHITECTURE.md` delegation is NOT widened to reach §16, so this entry stays `gap` deliberately. §16 holds the ratification asks put TO the user — this entry is ask A5 — and an ask is not a rule, so forcing it a contract home would misdescribe what it is; D-430's kind half would exclude the section at the next run in any case. THIS IS A RULING, NOT A DEFERRAL: no later wave owes a delegation act here." §16's ask is left standing where it is (#12).

### D-419 — Until the recognition consumer is built, the function layer does not touch the harmonic vocabulary

> - **Until the RECOGNITION CONSUMER is built, the function layer does not touch this vocabulary —
>   and the connection is absent, not partial.** The consumer is the separate, named piece of work
>   that makes this catalog the function layer's multi-chord disambiguation prior and the grouping
>   layer's sequence-span annotation; it is also where the §6.7 idioms first do any work, by
>   weighting which entries count. Until it exists the function layer makes **no** use of the catalog
>   at all. *Why:* it follows from the ratified build order — vocabulary, then the grouping layer,
>   then wire the consumer — and from this component's own contract that it supplies **ranked
>   candidates and decides nothing**: with no consumer there is nothing to receive the candidates, so
>   a partial connection would be a consumer built by accident and unratified. This is the
>   declared-dormancy form the fact-publication corollary requires: the component is published with
>   its future consumer **named**, rather than left to look like waste.

**In plain words.** The reference catalog of named progressions and the function layer are connected by a separate piece of work that has not been built. Until it is, the function layer makes no use of the catalog at all — it is not a partial or optional connection, it is absent. That piece is also where the five idioms first do any work, by weighting which catalog entries count.

**Why.** It follows from the ratified build order stated at `:54` — encyclopedia, then the grouping layer, then wire the consumer — and from the catalog's own contract that it supplies ranked candidates and decides nothing (register entry D-407): with no consumer, there is nothing to receive the candidates, so a partial connection would be a consumer built by accident and unratified. Register entry D-084 records the same shape from the other side: the progression-schema recognizer is a CONSUMER of the function layer, not a new layer.

**Status.** LIVE · decided 2026-06-30 · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `ARCHITECTURE.md:5705-5715`

**Provenance.** `docs/implementation_roadmap.md`:59-62, inside the forward increment sequence whose header (`:54`) calls the order "ratified" — encyclopedia, then L6, then wire the consumer — without naming who ratified it or when; the surrounding block is dated 2026-06-30 at `:36`. The date recorded here is that block's date and the ratifier is NOT STATED, because the text asserts ratification without attributing it. The constraint governs Layer 5 and is recorded in a plan rather than in the Layer-5 specification, hence the documentation-gap flag. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that a build-ORDER rule is not a statement either section makes. The user ruled it a DECLARED-DORMANCY CONSTRAINT WITH ITS FUTURE CONSUMER NAMED — the shape the fact-publication corollary requires — which homes at §7, where the component and its planned consumers are specified. Written into §7 in that section's own voice, with its defense and with the absence stated as absolute rather than partial. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/implementation_roadmap.md:101`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 1, "section": "# Consolidated Implementation Roadmap — Reviews → Plan", "label": "the opening block (above the first section heading)", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "3. **Recognition consumer** — build + wire: the encyclopedia becomes L5's multi-chord disambiguation prior (the §5.5
   resolver + the §8 forward-override) and L6's sequence-span annotation. **This is the step where L5 takes advantage of
   the encyclopedia AND the five idioms** (the active idiom-mixture weights the matches). Until this exists, L5 does not
   touch the encyclopedia." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-454 — The grouping layer detects nothing — it assembles what earlier layers decided, and pressure to add detection means the work belongs elsewhere

> Layer 6 defines **no detection of its own**: it assembles §5.1–§5.3 (punctuation-span segmentation, key-area grouping,
> cadence alignment) and hosts the **read-through carries** — §5.4 the Layer-5 residual and §5.5 the consumer's schema
> annotations, both carried verbatim, neither *detected* here. There is no additional *detection* rule and no hierarchy.
> Pressure to add detection is a signal to check whether the work belongs in an **earlier** layer (a detection that should be
> a primitive) or is an **out-of-scope extension** (§9-D3) — not a new Layer-6 mechanism.

**In plain words.** The grouping stage adds no detector of its own. It puts together the boundaries, cadences, keys and unresolved marks the earlier stages produced. If it starts to feel as though grouping needs to detect something, that is a sign the work belongs to an earlier stage or is out of scope — not that grouping needs a new mechanism.

**Why.** Stated with the rule, and it is the same reasoning as the rebuild itself: a second detector here would duplicate the boundary, cadence and key machinery the layers already own and reintroduce exactly the divergence the rebuild exists to remove (the document's decision D2). D-082 carries the additive-and-read-only half from the canonical specification; the no-detection prohibition and its warning sign are recorded only here.

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:307-311`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. The layer is exactly its assembly rules + read-through carries (the proportionality bound)` (heading at line 306). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` §6, in a document whose banner reads "AS-BUILT (2026-07-02) — built dormant + oracle-validated" and records the Cowork ratification of the build report. Entered by the phase-1 reads wave 1. NOT user-ratified: the banner names Cowork as the ratifier of this document's sign-off, and only the items the banner marks user-ratified carry the user's authority. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-455 — A cadence away from a grouping boundary is surfaced as internal, never snapped to the nearest boundary and never discarded

> - **D4 — Cadences align to punctuation-spans, asymmetrically; an off-boundary cadence is surfaced, not snapped (§5.3).**
>   *Rejected:* forcing every punctuation-span to end with a cadence (contradicts the ground truth) and snapping a stray
>   cadence to the nearest boundary (hides a real tension signal and would be a covert upstream override).

**In plain words.** A cadence usually lands where a grouping span ends, but a span may end with no cadence at all, so the relation runs one way only. A cadence that lands nowhere near a boundary is marked as falling inside a span and shown as such. It is not dragged to the nearest boundary and it is not thrown away.

**Why.** Stated with the decision, both alternatives rejected for named reasons: requiring every span to close with a cadence contradicts the ground truth, and snapping a stray cadence hides a real signal — an off-boundary cadence means either a missed boundary or an over-eager cadence — and would amount to overriding an upstream decision from the grouping stage, which the forward-only contract forbids.

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:355-357`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 340). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` §9 decision D4, with the rule stated at §5.3, in the AS-BUILT document signed off by Cowork 2026-07-02. Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-456 — Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle

> - **D3 — Sections / periods / sentences are out of L6's *core* for PROPORTIONALITY — NOT disqualified for lack of an
>   oracle (user-ratified verifiability contract, 2026-06-29).** They are sound theory and *do* lack an oracle in our
>   corpus, but the contract is explicit that **lack of ground truth is not a disqualifier.** They stay out of the thin core
>   because L6 is the *flat-grouping assembly* layer and forms/sections are a larger, *higher*-layer structure — and they are
>   **buildable via a chosen alternative-confidence path** (a form-annotated corpus, or theory-rules-as-oracle) with an
>   "empirically-unvalidated" mark, when a need arises. The core is punctuation-spans + key-areas + cadence alignment + the
>   hosted schema spans.

**In plain words.** Larger formal structures — sections, periods, sentences — are left out of the grouping stage's core because that stage assembles the flat grouping and formal structure is a bigger thing belonging higher up. They are NOT rejected for being uncheckable against our annotated music: the standing contract says that alone never disqualifies sound theory. They may be built when a need arises, with a chosen way of gaining confidence in them and an explicit mark that they are empirically unchecked.

**Why.** Stated with the decision and grounded in the user-ratified verifiability contract of 2026-06-29 (D-029), which this entry is the layer-level application of. It matters that the two grounds are kept apart: D-083 records these structures as out of the validatable core, which reads as the oracle-absence ground the contract explicitly rejects as a disqualifier — this entry records the ground the design document actually gives.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:348-354`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 340). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` §9 decision D3, which names its ground as the "user-ratified verifiability contract, 2026-06-29". The verifiability contract's own user ratification is what the entry's date and ratifier record; the application to this layer sits in a document signed off by Cowork 2026-07-02. Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-457 — A group truncated by the selection edge is marked as truncated, and a group that runs off the edge unclosed carries an extension cue the grouping layer only surfaces

> An edge group whose opening/closing tick is the **selection edge rather than a musical boundary** carries the provenance
> `clipped-by-selection-edge` (the same principle as the §3 marker-scope provenance and L2's artificial-clip-boundary
> distinction) — a truncated group is never presented as a complete one; the same mark applies to an edge **key-area**
> (§5.2). And an edge span that reaches the selection edge with **no closing boundary and no cadence** is surfaced with an
> `extension-cue` tag — the signal that widening the selection would complete it. Per the forward-only contract L6 only
> **surfaces** the cue (like the §5.3 internal-cadence tension tag); acting on it — invoking L1's `extend` and re-running —
> is the decision of the **orchestrator** (the pipeline driver that sequences the layers — the region analyzer of the
> bounded-context contract, `cowork_bounded_context_design.md` §6) under the §2.15 bounded-context contract (stop
> condition + hard bound), never L6's.

**In plain words.** When a group begins or ends only because the user's selection stops there, it is marked as clipped by the selection edge, so a cut-off group is never presented as a complete one; the same mark applies to a key area at the edge. When a group reaches the edge with neither a closing boundary nor a cadence, it carries a cue saying that widening the selection would complete it. The grouping stage only shows the cue — deciding to act on it, by asking for more music and re-running, belongs to whatever drives the pipeline.

**Why.** Stated with the amendment: it applies the same principle as the boundary-scope provenance and the slicer's artificial-clip-boundary distinction — a truncated thing is never presented as complete — and the division of labour follows from the forward-only contract, since acting on the cue means invoking the extension machinery and re-running, which is the orchestrator's call under the bounded-context contract's stop condition and hard bound.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:214-222`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.1** — `### 5.1 Punctuation-span segmentation` (heading at line 209). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` §5.1, marked in the document as a "Post-sign-off amendment, user-ratified 2026-07-02". Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-458 — The codetta refinement is read as the as-built tiling: keep the strong cut, drop the weak one, and record the codetta end as an annexe

> **(§5.1-a, the reading that is CANONICAL — ruled at ratification, Cowork, 2026-07-02.)** The refinement above admits
>     more than one reading of what to do with the second boundary, and one of them is fixed: **keep the strong-peak cut,
>     drop the weak cut, and record the codetta's end as an ANNEXE** — the `codettaEndTick` field — rather than as a span
>     boundary.

**In plain words.** Where a strong grouping cut is followed closely by a weak one, the span ends at the strong cut and the stretch after it is recorded as a trailing annexe rather than opening a group of its own. This reading was ruled canonical at ratification.

**Why.** Stated with the ruling: it is the only reading that preserves the rule that groups tile the analysed stretch completely and without nesting — a second cut opening its own group would break the partition the layer is defined by. The ruling also records that it is inert under default settings, changing no output unless explicitly enabled.

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:234-237`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.1** — `### 5.1 Punctuation-span segmentation` (heading at line 209). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` status banner, which records the ruling as made by Cowork at ratification. Entered by the phase-1 reads wave 1. The banner is a status surface, which OI-240 establishes is not a home for a standing decision — recorded here so the ruling is findable, with the documentation-gap flag standing. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ RE-HOMED 2026-08-11 (CC, `cc_instruction_return_continuation_12.md` Task 2), under D-664's re-homing default and by D-668's procedure. STEP 1 WAS CHECKED FIRST AND DECLINED: §5.1-a already states the strong-peak/weak-peak rule, but it does NOT state the annexe field, that the reading is ruled canonical, or the partition-law ground — so a pointer move onto it would have admitted the rule by stretch, which the procedure forbids. STEP 2 was taken: the missing halves are written into §5.1-a in that section's own voice, and the home and verbatim are re-taken from the new text. THE KIND HALF WAS JUDGED BEFORE THE WRITE: §5.1 states the partition law and its refinement in the imperative, which is a rule-stating section; the document's opening block, which the classification grades as recording findings, is where this entry sat. FORMER HOME, PRESERVED (#12): `cowork_layer6_grouping_design.md:12-15`, the status banner. FORMER VERBATIM, PRESERVED (#12): "**§5.1-a codetta interpretation RULED (Cowork, at ratification):** the\n> as-built tiling reading (keep the strong-peak cut, drop the weak cut, record `codettaEndTick` as an annexe) is\n> canonical — it is the only reading preserving the §5.1 flat/total partition law; inert under default settings\n> (changes no output unless explicitly enabled)." WHAT THE HOME TEXT DELIBERATELY DOES NOT CARRY: no measured value and no build figure from the banner — the oracle counts, the recall value and the corpus-gate figures stay in the banner and in the build report that measured them (D-431); the section states the rule and its ground. THE BANNER IS UNTOUCHED, so a reader comparing the two sees what moved.

### D-459 — The key-area confidence is a declared margin-class boundary confidence, and its input is the declared key confidence — never the grading diagnostics' sigmoid

> *(Contract compliance, added at sign-off review 2026-07-02: any confidence L6 publishes — the key-area
> confidence, a span-level aggregate — is a **boundary confidence under the cross-layer confidence contract**
> (`cowork_confidence_contract.md` U2): [0,1], declared in the contract's **Class M** (a margin-family quantity, not a
> calibrated probability), with its combiner and inputs named; and its **input** is
> each unit's DECLARED boundary key confidence per that contract — i.e. once the **D-L3a close-out** (the Layer-3
> boundary-confidence declaration item of `cowork_confidence_contract.md` §3) lands, the one declared
> L3/L5 number, not the **diagnostic sigmoid** (the Layer-3 emission-scale confidence squash used by the grading
> diagnostics, named in the Layer-3 spec banner as the C1 fidelity fix).)*

**In plain words.** The confidence the grouping stage publishes for a key area is a quantity crossing a stage boundary, so it obeys the cross-layer confidence rules: it sits between zero and one, it is declared as a margin rather than a calibrated probability, and it names how it was combined and from what. What it is combined FROM is the declared key confidence, not the squashed number the grading diagnostics use.

**Why.** Stated with the rule and grounded in the ratified cross-layer confidence contract (D-032): a boundary quantity must declare its class, and feeding an aggregate from the diagnostic squash instead of the declared number would compare quantities from two different frames, which the contract forbids. The entry also carries the direction fixed here — the area's confidence is non-increasing in its weakest unit's — while the exact combiner is left to the precision phase.

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:254-261`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.2** — `### 5.2 Key-area grouping` (heading at line 245). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` §5.2, added at the sign-off review of 2026-07-02. Entered by the phase-1 reads wave 1. The rule is stated as conditional on a Layer-3 close-out item landing; whether that item has landed was NOT checked by this wave and nothing here asserts it. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-460 — A group counts as fully resolved exactly when no unit in it carries an unresolved mark — no confidence threshold enters the test

> A Layer-5 open mark on a unit is surfaced on the punctuation-span and key-area that contain that unit (the group is
> reported as carrying an unresolved reading at that location). L6 **never** resolves an open mark — it has no evidence Layer
> 5 lacked. A punctuation-span composed entirely of units carrying **no open mark** (that is the whole test — no
> confidence threshold is involved) is reported as fully resolved; one containing an
> open mark is reported with the residual visible.

**In plain words.** Where an earlier stage left a reading unresolved, that mark is shown on the group and the key area containing it. The grouping stage never resolves it — it has no evidence the earlier stage lacked. A group is reported as fully resolved when, and only when, none of its units carries such a mark; no confidence number is consulted.

**Why.** Stated with the rule, and the parenthesis is doing the work: naming the test as the whole test forecloses a threshold creeping in, which would turn an honest carried residual into a judgment the grouping stage is not entitled to make. It is #12 (no information loss) at the assembly stage — the residual stays visible rather than being averaged away.

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:292-296`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5.4** — `### 5.4 Carrying the residual` (heading at line 291). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` §5.4, in the AS-BUILT document signed off by Cowork 2026-07-02. Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-461 — The grouping layer is an explainability layer, not an accuracy requirement, and is deliberately kept thin

> - **Proportionality.** The SOTA reaches competitive Roman-numeral accuracy with **no** explicit grouping layer (grouping
>   falls out of stable key runs — `contrapunctus_findings.md`). L6 is a deliberate **explainability** layer, not an
>   accuracy requirement; it stays the thin assembly layer specified here and does not grow detection of its own.

**In plain words.** The best published systems reach competitive Roman-numeral accuracy with no grouping stage at all — grouping falls out of stable key runs. Ours exists to make the analysis explainable, not to make it more accurate, and it is held to the thin assembly job on that basis.

**Why.** Measured against the published state of the art and cited to the research findings the claim rests on: since the accuracy case for the layer does not exist, the layer's justification is explainability, and that is exactly what bounds how much it may grow. This is the reasoning behind the no-detection prohibition rather than a restatement of it.

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:324-326`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§7** — `## 7. Crosscutting concepts` (heading at line 314). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` §7, in the AS-BUILT document signed off by Cowork 2026-07-02. Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-462 — Cadence validation is scoped to LOCATION; cadence TYPE is only partially attributable and is never a clean gate

> - **Cadence alignment → the DCML-TSV `|cadence` oracle, scoped to LOCATION** (robust to Roman-numeral errors; cadence
>   *type* is harmony-dependent and only partially attributable on the harder repertoire — measured, caveated, not a clean
>   gate).

**In plain words.** Cadences are checked against the annotated corpus for WHERE they fall, because that check survives a wrong Roman numeral. WHAT KIND of cadence it is depends on the harmony being right, so on the harder repertoire that can only partly be attributed — it is measured and reported with that caveat, and it never becomes a pass-or-fail gate.

**Why.** Stated with the rule: cadence type is harmony-dependent, so a type mismatch cannot be attributed to the cadence detector rather than to the chord reading upstream — which is what disqualifies it as a gate, while location remains attributable and therefore gate-worthy. This is #19 applied to an oracle: the measurement unit is trusted only for what it can actually be shown to measure.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer6_grouping_design.md:369-371`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§10** — `## 10. Quality & testing — the validation strategy (the two-step oracle, user-ratified 2026-06-29)` (heading at line 362). A delegation at ARCHITECTURE.md:2206 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_layer6_grouping_design.md` §10, whose heading records the two-step validation strategy as "user-ratified 2026-06-29". Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-472 — Key areas are grouped by a smoothing pass over regions whose key sequence has already been smoothed, and a region that disagrees without clearing the confidence test keeps its own key while being grouped into the enclosing area

> **★ KEY AREAS ARE GROUPED BY A SMOOTHING PASS OVER REGIONS WHOSE KEY SEQUENCE HAS ALREADY BEEN
> SMOOTHED, AND A REGION THAT DISAGREES WITHOUT CLEARING THE CONFIDENCE TEST KEEPS ITS OWN KEY WHILE
> BEING GROUPED INTO THE ENCLOSING AREA (re-homed into this specification 2026-08-08 on the user's
> ruling — the owning layer in the target architecture, with §11.5 pointing; the PRECONDITION half of
> the wording corrected 2026-08-09 on the user's ruling, immediately below).** Neighbouring regions in
> the same key are collected into one key area. A key area opens at the first region and closes when
> the next region's key differs from the current area's **and** that region clears a confidence test; a
> region whose key disagrees but does not clear the test **keeps its own key reading** — so the status
> bar stays accurate for that region — while being grouped into the enclosing area, so the annotation
> emitter writes Roman numerals against the key that actually governs the passage rather than against a
> momentary wobble. *Why:* it is a grouping rule and not a second key analysis — it reads the key
> fields the earlier layers already published rather than re-deciding them, which is the same
> not-a-new-detector reasoning this layer's contract states for grouping generally.

**In plain words.** Neighbouring stretches in the same key are collected into one key area. A stretch that reads a different key but is not confident enough to open a new area keeps its own reading for display, yet is counted inside the surrounding area — so the Roman numerals are written against the key that actually governs the passage rather than against a momentary wobble.

**Why.** Stated with the design: it reads the key/mode fields an earlier smoothing step has already settled, so it adds a grouping rule rather than a second key analysis — the same not-a-new-detector reasoning **D-454** later states for the grouping layer. **THE PRECONDITION HALF OF THIS DEFENSE WAS CORRECTED 2026-08-09** (user, Ruling 15 of `cowork_rulings_2026_08_09_second_stop.md`), after the read-only probe ruled at Ruling 9 of `cowork_rulings_2026_08_09_return.md` established at the code that the arm which SHIPS meets the precondition by a different design: the joint decoder's global dynamic program, whose state carries the tonality and whose key transitions carry separate stay and change branches. The former wording, preserved (#12), named the legacy arm's own step — *"it leverages the key/mode fields and the stabilization Pass 4 already performed"* — which is true of the legacy arm and false of the production one. The not-a-new-detector ground is unchanged and is what survives. The corrected home states the non-equivalence between the two designs (island erased versus island made expensive, unmeasured, #24); the probe's citations are located rather than transcribed at `tools/audit/oi349_record_arm_precondition_probe.json` (**D-431**).

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:2208-2220`

**Provenance.** Stated as the key-area detection design of the unification document. The mechanism is live at HEAD in `groupKeyAreas` (`src/composing/analysis/section/sectionanalyzer.cpp`), where the confidence test reads the stored per-region assertive-exposure flag rather than re-thresholding the confidence field. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ HELD 2026-08-07 BY THE ARM CHECK ITS OWN RULING ORDERED, THEN HOMED 2026-08-08 IN THE FORM THE USER RULED (Option A). The 2026-08-07 homing wave ran the arm check before writing any home text and it came back MIXED: the grouping rule is shared and is reached on the PRODUCTION record arm (`sectionrecordadapter.cpp:360`), while the Pass-4 stabilization this entry's own text names as the grouping's precondition has ONE call site, inside the LEGACY arm (`sectionanalyzer.cpp:750`). A mixed arm was that dispatch's stated outcome for holding an entry, so it was held and returned to the user. **THE USER RULED OPTION A on 2026-08-08:** home it in the Layer-6 section WITH THE ARM SPLIT STATED — the grouping rule specified as live, the stabilization precondition beside it marked ⚠ LEGACY, each end carrying its citation — one home, both halves visible (#12). That is what was written. **AND THE CONFORMANCE QUESTION IS ROWED as its own open item** (`OPEN_ITEMS.md` OI-349): whether the record arm satisfies the stated stabilization precondition by other means, or the live path runs the grouping on input its own specification says must be stabilized first. That row's subject BEARS ON THE ANALYSIS; whether its read-only probe runs before phase 2 or inside it is the user's timing call and is not settled by this homing. THE ALGORITHM'S FIELD NAMES AND THE PROPOSED THRESHOLD VALUE ARE NOT CARRIED ACROSS (D-307 / D-431) — the rule is, and the two code citations appear only in the arm-split note, where they are what makes the split checkable. FORMER HOME, PRESERVED (#12): `docs/unified_analysis_pipeline.md:149-165`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 147, "section": "### Key-area detection", "label": "“Key-area detection”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "Runs after Pass 4 (`stabilizeHarmonicRegionsForDisplay`) on the smoothed
region list. Algorithm:

1. Walk regions in order. A key area opens at the first region.
2. Close the current key area and open a new one when the next region's
   `(keyFifths, mode)` differs from the current key area's key AND the
   next region's `keyModeResult.normalizedConfidence` meets a threshold
   (initial proposal: 0.8, reusing the assertive-confidence constant).
3. Regions whose key disagrees with the enclosing area but don't clear
   the threshold retain their own `keyModeResult` (status-bar display
   still accurate) but are grouped into the enclosing area via
   `keyAreaId` (so the annotation emitter writes Roman numerals
   relative to the enclosing area's key, not the transient local
   disagreement).

This is a smoothing pass, not a new analyzer. It leverages existing
`keyModeResult` fields and the stabilization already done in Pass 4." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-476 — The phrase-boundary primitive is owned by the notation-derived view layer — not by the note model, and not by the function layer that consumes it

> - **D1 — Owner: Architectural Layer 1.5 (the notation-derived views).** The primitive is a notation-derived view, the same
>   kind as the bass, top-voice, and spelling views, reading the same notated surface. *Rejected:* the Layer-1 note model
>   (deliberately narrow — it records notes, it does not derive phrase structure) and the function layer (it consumes phrase
>   boundaries; it cannot own them).

**In plain words.** Working out where a musical phrase ends is done by the same kind of component that reads the bass line or the written spelling off the page. It is not part of the plain record of the notes, and it is not part of the stage that detects cadences — because that stage uses phrase ends as input and cannot also produce them.

**Why.** Stated with the decision, and both alternatives are named with their reason: the note model is deliberately narrow — it records notes and derives no phrase structure — and the function layer consumes phrase boundaries, so owning them would be circular.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:250-253`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Architecture decisions (with the alternatives weighed)` (heading at line 249). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Decision D1 of a design document whose banner reads SIGNED (user, 2026-06-26). Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-477 — Phrase boundaries are read from the written surface alone — never from a resolved key, chord or cadence — and the boundaries this misses are accepted, not recovered here

> - **Notation-only — key-, chord-, and function-agnostic.** A phrase boundary is read from the written surface (rests,
>   durations, pitch intervals, metric position, annotations, barlines), never from a resolved key, a chord reading, or a
>   cadence. This is structural: the function layer's cadence detection *consumes* phrase boundaries, so a boundary that
>   depended on cadence would be circular. Cadence-based phrase refinement therefore stays a **function-layer** concern,
>   downstream of this primitive (§6-D3). A known consequence (accepted): a surface-only primitive **systematically misses
>   boundaries marked only harmonically** — a cadence with no surface gap — which the function layer recovers downstream.

**In plain words.** Phrase ends are found from what is printed: rests, note lengths, leaps, metric position, marks and barlines. Nothing about the key or the chords may enter, because the stage that detects cadences uses phrase ends, so a phrase end that depended on a cadence would be circular. The cost is accepted and stated: a phrase that is marked only by its harmony, with no gap in the surface, is missed here and picked up later.

**Why.** Stated with the constraint: the dependency must stay acyclic because the function layer's cadence detection consumes phrase boundaries. The accepted consequence is stated in the same breath rather than left for a reader to discover — a surface-only primitive systematically misses harmonically-marked boundaries.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:64-69`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. Constraints` (heading at line 63). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The first constraint of a design document whose banner reads SIGNED (user, 2026-06-26); its decision D3 states the same rule from the architecture side, and the banner records that the acyclicity argument was independently verified airtight. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-478 — A phrase boundary is a peak in a continuous boundary-strength profile, not the OR of a few binary signals

> - **D4 — A graded boundary-strength model, not a binary union (user-ratified 2026-06-26).** The boundary is a peak in a
>   continuous strength profile, not the OR of a few binary signals. *Rejected:* the binary union — a degenerate special
>   case that cannot express "a gap larger than its neighbours," inflates recall, and wrecks precision (per the research: a
>   weighted combination measurably beats any single cue and beats a naive union; the leading harmony-free models all
>   compute graded strength + peaks). The cost — per-cue normalisation, the weight vector, the peak threshold — is modest
>   and the constants are precision-phase.

**In plain words.** Rather than declaring a phrase end wherever any one signal fires, the program computes how strongly each moment is marked as an ending and then picks the peaks. The all-or-nothing version is the special case that cannot express 'a bigger gap than its neighbours', and it finds too many endings.

**Why.** Published research, cited with the decision: the leading harmony-free segmentation models all compute a continuous boundary strength and pick peaks, a weighted combination measurably beats any single cue and beats a naive union, and the binary union is a degenerate lower-precision special case of the graded form. The cost is named and accepted — per-cue normalisation, a weight vector and a peak threshold, all deferred to the precision phase.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:260-265`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Architecture decisions (with the alternatives weighed)` (heading at line 249). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Decision D4 of a design document whose banner reads SIGNED (user, 2026-06-26) and records the graded model as revision 2, adopted on the research in `cowork_phrase_boundary_methods.md` (user-ratified 2026-06-26). Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-479 — The boundary cues run per eligible voice and aggregate to the texture, and BOTH the per-voice and the texture boundaries are published

> - **D5 — Per-voice cues aggregated to the texture (both per-voice and polyphonic), not a top-voice/whole-texture
>   reduction.** The cues run **per eligible voice** and aggregate by **voice-coincidence** into the texture strength,
>   exposing **both** the per-voice boundaries and the texture boundaries (§4.3). *Rejected:* (a) a whole-texture reduction
>   with **top-voice-only pitch** — it discards every inner voice's pitch cue and yields no per-voice phrasing; (b) running
>   the cues on one arbitrary voice — ill-defined in polyphony. Per-voice-then-aggregate is the principled form (the
>   local-change cues are defined per line) and produces both outputs. Since the literature's cues are validated only
>   monophonically, the aggregation is validated on our own corpus (§7).

**In plain words.** The signals that mark a phrase end are properties of a single melodic line, so they are computed for every voice separately and then added up across the voices. Where many voices phrase together the total is high; where one inner voice alone pauses it is low. Both answers are published: each voice's own phrasing and the whole texture's.

**Why.** Stated with the decision: the local-change cues are defined per melodic line, so per-voice-then-aggregate is the principled form, and it is the only form that produces the per-voice output at all. Both rejected alternatives are named — a whole-texture reduction with top-voice-only pitch discards every inner voice's pitch cue, and running the cues on one arbitrary voice is ill-defined in polyphony. The honesty clause is stated with it: the literature validates these cues monophonically only, so the aggregation is validated on this project's own corpus.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:266-272`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Architecture decisions (with the alternatives weighed)` (heading at line 249). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Decision D5 of a design document whose banner reads SIGNED (user, 2026-06-26); the banner records this as the revision-3 change made at the user's direction, and that the rev-3 changes were independently re-reviewed with a blocking fix applied. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-480 — The phrase-boundary primitive is NOT an accuracy requirement — a competitive reference engine does no phrase segmentation at all — so it is built right but kept proportionate

> - **★ Proportionality (scope discipline, user-ratified 2026-06-26).** The state-of-the-art-competitive reference
>   engine (Contrapunctus) does **no** explicit phrase segmentation or cadence detection and is still competitive at Roman-numeral
>   analysis (it captures phrase structure implicitly via stable key runs). So this primitive is **not** an accuracy
>   requirement — it is load-bearing for *our* cadence mechanism (a means to key/function), a deliberate bet for an
>   explainable, decomposed pipeline. **Build the graded model right, but keep it proportionate — do not let it balloon.**
>   If the explicit phrase/cadence path proves hard, there is a proven implicit fallback (phrase-alignment via stable key
>   runs). See `contrapunctus_findings.md` addendum and `cowork_phrase_boundary_methods.md`.

**In plain words.** A comparable system that performs as well as ours at Roman-numeral analysis has no phrase detection whatsoever; it picks up phrase structure indirectly. So this component is not what accuracy depends on. It is a deliberate bet on an explainable, decomposed design — worth building properly, not worth letting grow without limit, and there is a proven fallback if the explicit route proves hard.

**Why.** Evidence cited with the ruling: the state-of-the-art-competitive reference engine (Contrapunctus) does no explicit phrase segmentation or cadence detection and is still competitive at Roman-numeral analysis, capturing phrase structure implicitly via stable key runs — recorded in `contrapunctus_findings.md` and the methods catalog. That same finding supplies the named fallback if the explicit path proves hard.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:303-309`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8** — `## 8. Risks & technical debt` (heading at line 293). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** A user-ratified scope ruling recorded in the risks section of a design document whose banner reads SIGNED (user, 2026-06-26). Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) It is the same proportionality reasoning **D-456** records for the grouping layer, reached independently and earlier.

### D-481 — The notated markers are emitted as boundaries unconditionally; only the surface-cue strength is peak-picked

> The picked-boundary set is **the surface-cue peaks UNION every notated marker** — because the §4.2 markers are
> **deterministic facts** (a fermata/barline/etc. *is* a phrase boundary), they are emitted **unconditionally**, not
> subjected to the threshold; only the **surface-cue** strength is peak-picked. *(As-built realisation, ratified 2026-06-26:
> the earlier wording "peak-pick the combined profile" put the markers through the local-maximum test, which a strict
> greater-than rule drops for two **adjacent equal-height markers** — e.g. a final fermata abutting the closing barline.
> Emitting markers directly is the faithful reading of their "deterministic / dominate wherever they occur" status.)*

**In plain words.** A fermata, a breath mark, a structural barline and the other written signs are facts, not evidence to be weighed — so each one is reported as a phrase end directly. Only the computed strength has to clear a local-maximum test and a threshold.

**Why.** Measured against the rule it replaces, and the case is stated: putting the markers through the local-maximum test drops two adjacent equal-height markers under a strict greater-than rule — a final fermata abutting the closing barline. Emitting them directly is the faithful reading of the deterministic status the markers already carry.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:188-193`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4.4** — `### 4.4 Peak-picking` (heading at line 187). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The as-built realisation recorded in §4.4 of a design document whose banner reads SIGNED (user, 2026-06-26); the parenthetical records it as ratified on that date and preserves the earlier wording it replaces. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-482 — The two hand-synchronised copies of the fermata scan retire into one owned primitive, and that retirement changes no output

> - **D2 — One unified primitive replaces the two duplicated fermata scans.** The fermata logic exists today in two
>   hand-synchronised copies; they are retired into the single owned primitive and every consumer re-points at it. The
>   retirement is byte-identical.

**In plain words.** The same fermata-finding code existed twice, kept in step by hand. Both copies are replaced by the single owned component and every consumer re-pointed at it. Because the marker-only behaviour is unchanged, the swap produces identical results — the new behaviour is a separate, measured step.

**Why.** Stated with the decision and required by #6 (one path per concern): two hand-synchronised copies drift independently. Splitting the change into a byte-identical unification and a separately-gated behaviour change is the project's standing discipline, applied here so the unification cannot hide an output movement.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:254-256`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§6** — `## 6. Architecture decisions (with the alternatives weighed)` (heading at line 249). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Decision D2 of a design document whose banner reads SIGNED (user, 2026-06-26); the same document's constraints state the split explicitly — the marker-only path is byte-identical, the graded model is gated on the corpus regression stop. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-483 — The picked boundaries are validated against the analysts' own phrase marks; a fermata-derived phrase list is inadmissible as ground truth because the primitive reads fermatas

> - **Validation on the chorale corpus** (the per-voice aggregation, D5) — the picked texture boundaries are checked
>   against the corpus's **analyst-annotated phrase markers** (the DCML corpora's `{}` / `phraseend` annotations, parsed
>   corpus-wide since the TSV-oracle infrastructure landed) — an **independent** ground truth: the markers are supplied
>   by the human analyst, not derived from fermatas, so validating the fermata marker against them is not circular. A
>   fermata-derived phrase list would be inadmissible as ground truth here, for exactly that circularity. A per-voice

**In plain words.** To check whether the phrase ends are right, they are compared with the phrase marks the human analysts wrote in the annotated corpora. A list of phrases derived from fermatas could not be used, because the program reads fermatas itself — it would be marking its own homework.

**Why.** Stated with the rule: the markers are supplied by the human analyst and are not derived from fermatas, so validating the fermata marker against them is not circular — and the document states the converse in the same sentence rather than leaving it implied.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:281-285`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§7** — `## 7. Quality & testing` (heading at line 277). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The validation rule of a design document whose banner reads SIGNED (user, 2026-06-26), naming the corpus columns it uses. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) It is the phrase-axis instance of the standing rule **D-294** — the only ground truth is the human annotation, and no self-annotation ever enters a measurement.

### D-484 — The phrase-boundary primitive is a derived view: it inherits the loaded span, requests no extension of its own, and publishes a per-profile max-normalised boundary confidence

> - **A DERIVED VIEW: it inherits the loaded span and requests no extension of its own.** Where only a stretch of the
>   score is loaded, this primitive does **not** ask for more music. Its profile simply **ends where the loaded span
>   ends**. A consumer that wants boundary evidence beyond that stretch extends the span through **its own**
>   bounded-context obligation, and this primitive then **recomputes over the enlarged span** — the standard re-run.
>   *Why:* a derived view that reached for its own context would hold a second, independent extension policy beside its
>   consumers' (#6), and its answer would then depend on which consumer asked.
> - **Its published boundary strength is a per-profile MAX-NORMALISED confidence, comparable within ONE score's profile
>   only, and it participates in NO override frame.** The number on the wire is a boundary confidence in the cross-layer
>   contract's Class-M sense: it ranks ticks inside one score's own profile and says nothing across scores, and it never
>   overrides another layer's answer. *Why:* the strength is a max-normalised salience rather than a probability, so two
>   scores' values are not on one scale, and a quantity that cannot be compared across scores must not be given the
>   authority to overrule one that can.

**In plain words.** When only part of a score is loaded, this component does not ask for more music. Its profile simply ends where the loaded stretch ends; a consumer that wants boundary evidence further out asks for the extension itself and this component recomputes. Its published strength is comparable only within one score's own profile — it never overrides another layer's answer.

**Why.** Stated with the stance and derived from the two contracts it cites: the bounded-context design's standard re-run rule for derived views, and the cross-layer confidence contract's Class-M boundary confidence, which fixes the range, the comparability and the fact that it participates in no override frame.

**Status.** LIVE · decided 2026-07-02 · ratified by Cowork

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:83-94`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. Constraints` (heading at line 63). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** ★ RE-HOMED 2026-08-09 into `cowork_phrase_boundary_design.md` §2 (Constraints) by `cc_instruction_return_continuation_8.md` Task 2, under the user's Ruling 38 — the finish-line item for entries the delegation REACHES in a section that RECORDS FINDINGS, whose closing act is rule (e)'s preferred route: write the rule into a section that STATES it, in the specification that owns the concern. The concern is owned by this same specification, so the move is within the document. THE KIND HALF WAS CHECKED BEFORE THE WRITE: §2 is a list of binding constraints on the primitive, which is what a rule-stating section is; the former home was the document's OPENING BLOCK, which the classification records as recording findings. FORMER HOME, PRESERVED (#12): `cowork_phrase_boundary_design.md:23-31`. FORMER VERBATIM, PRESERVED (#12): '> **Bounded-context stance (added 2026-07-02, closing gap-analysis v2 finding A-2, `cc_gap_analysis_v2_report.md` — ruled by Cowork):** this primitive is a **derived view** over the Layer-1/Layer-2 outputs: it **inherits the loaded span and requests no extension of its own** (its profile simply ends where the loaded span ends; a consumer wanting boundary evidence beyond the loaded span extends via ITS own bounded-context obligation, and this primitive recomputes over the enlarged span — the standard re-run, per `cowork_bounded_context_design.md` §4). Its published boundary strength is a **Class-M boundary confidence** under the cross-layer confidence contract (`cowork_confidence_contract.md`: [0,1] per-profile max-normalised salience, comparable within one score's profile only; it participates in no override frame) — closing gap A-3 of the same v2 report for this spec.' ★ WHAT THE CONSTRAINT TEXT DELIBERATELY DOES NOT CARRY: the two gap-analysis finding identifiers and the report that raised them, which are provenance and stay in the entry's own fields; and the Class-M label itself, whose home is the confidence contract — §2 states what the number MEANS and what it may not do, and the class name stays where it is defined (#6). The opening block's stance text is untouched (#12). The original entry: a stance added to the design document on 2026-07-02, closing two findings of the gap-analysis v2 report; the document records it as ruled by Cowork, not by the user. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-485 — Each picked boundary should carry which cue fired and at what scope; the picked set is scope-blind today and the refinement waits for the inference phase

> **★ EVERY PICKED BOUNDARY CARRIES WHICH CUE OR MARKER FIRED, AND AT WHAT SCOPE — A REQUIREMENT ON THIS SECTION'S OUTPUT,
> STATED AS OWED AND EXPLICITLY NOT BUILT.** A picked boundary — texture **and** per-voice — carries its **provenance**:
> which cue or marker produced it, and whether it fired **globally** or **per voice** (and if per voice, which voices, and
> how many coincided). **The picked set is SCOPE-BLIND today**, which is the defect this requirement names: a marker
> written on one voice — a breath mark — is spiked onto the texture profile and thereafter reads exactly like a marker
> that applies to the whole ensemble, so a downstream consumer (the punctuation-span annotation) cannot tell a **local
> breath** from a **global barline**.

**In plain words.** The markers that produce a phrase end are of two kinds: some apply to the whole ensemble by notation (a structural barline), and some are written on one instrument (a breath mark). Today both are treated as whole-texture endings, so a local breath is promoted to a global boundary and the fact that it was local is lost. A boundary should record which signal produced it and at what scope — recorded as owed, and deliberately not built yet.

**Why.** Stated with the item and grounded in #12 (no information loss): spiking a per-part marker onto the texture profile discards the locality, and the principled form is for it to reach a texture boundary only through the same voice-coincidence aggregation as the graded cues. The refinement is chorale-inert by construction — in the chorale convention all voices hold together — so it changes nothing on the gate repertoire and matters only for orchestral and contrapuntal textures.

**Status.** LIVE · decided 2026-07-01 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phrase_boundary_design.md:205-218`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4.4** — `### 4.4 Peak-picking` (heading at line 187). A delegation at ARCHITECTURE.md:1571 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** ★ RE-HOMED 2026-08-09 into `cowork_phrase_boundary_design.md` §4.4 (Peak-picking) — the section whose OUTPUT the requirement is about — by `cc_instruction_return_continuation_8.md` Task 2, under the user's Ruling 38, by the same finish-line item and the same rule (e) route as D-484. THE KIND HALF WAS CHECKED BEFORE THE WRITE: §4 is headed 'The model (the rules)' and §4.4 states the picking mechanism, so it states rules; the former home was §11 'Open items', which records what is owed. **THE FORM IS THE D-472 PATTERN**: the requirement is written in AS a requirement, marked OWED and EXPLICITLY NOT BUILT, with the standing rule that a proper-layer refinement waits for the inference phase named beside it — so the specification does not read as describing behaviour the implementation has. §11's own open item is untouched (#12) and now has a requirement to point at. FORMER HOME, PRESERVED (#12): `cowork_phrase_boundary_design.md:382-386`. FORMER VERBATIM, PRESERVED (#12): '   - **Provenance (the information-loss fix).** Each picked boundary — texture *and* per-voice — should carry **which cue/marker fired and at what scope** (global, or per-voice with which / how-many voices coincided), so a downstream consumer (Layer 6's punctuation-span annotation) does not lose that a boundary was a *local breath* versus a *global barline*. The picked set is scope-blind today. Recorded as a proper-layer refinement; per the standing rule, not built until the inference phase opens; validate on a non-chorale corpus (§8).' The original entry: open item 5 of the design document, recorded 2026-07-01 and attributed there to the user raising it. The document records the whole item as a proper-layer refinement not built until the inference phase opens; the register carries it because a recorded refinement with a stated shape binds what a future build may do. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.)

### D-490 — FALSIFIED: no threshold can make the fine-grain function override net-positive — the harm rate is flat against both quantities the threshold is built from

> - **FALSIFIED — no threshold can make the override net-positive.** Whether a fire helps or hurts is
>   unrelated to either quantity its trigger is built from: the incumbent reading's confidence and
>   the strength of the progression contradiction. Since the only tunable knob scales the bar by that
>   confidence, **no setting separates the cases it fixes from the cases it breaks**, and the best
>   measurable setting simply switches the pass off. *Why:* measured and stratified rather than
>   argued, on a ground-truth-aligned population of fires — the harm rate is essentially flat across
>   the contradiction value and **rises** with the incumbent's confidence, so the one available lever
>   pushes the wrong way; the mechanism of the harm is named too, the fourth- and fifth-related root
>   moves the progression score rewards accounting for most of both the fires and the harms.

**In plain words.** A late correction pass overturns a committed chord when the surrounding progression argues against it. Whether it helps or hurts turns out to be unrelated to either quantity its trigger is made of — how confident the earlier reading was, and how strongly the progression contradicts it. So no setting of the trigger separates the cases it fixes from the cases it breaks, and the best available setting simply switches the pass off.

**Why.** Measured and stratified rather than argued: the harm rate is about 78 % at the weaker contradiction value and about 76 % at the stronger, and it RISES with the earlier reading's confidence — about 81 % in the highest confidence band against about 72 % in the lowest — so the one available lever, scaling the bar by that confidence, pushes the wrong way. The mechanism of the harm is named too: fourth- and fifth-related root moves, exactly what the progression score rewards, are 55 % of the fires and 58 % of the harms.

**Status.** LIVE · decided 2026-07-06 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1148-1156`

**Provenance.** The measured verdict of the F-B redesign design pass, on 1043 ground-truth-aligned fires from the dormant decode chain, reproducing the fitting ledger's own split to the unit. It refutes the premise the confidence contract and the code comment both assert — that a fitted threshold accounts for the incumbent's missing progression term. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ The mechanism's reachability at HEAD was checked on 2026-08-04 (dispatch cc_instruction_reads_3.md §4.2) and is recorded once, at D-492: it is dormant — no production surface, and not the legacy production path either — so this falsified mechanism is not running today. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed under the scoring-surface rule to `docs/scoring_model.md`, and the ruling requires THE FAMILY (D-490, D-491, D-492, D-493) TO STAY IN ONE PLACE: all four are written into one §8 subsection, which is one evidence record about one mechanism. Written in that document's own voice and with its defense. The reachability check this entry's record already carries is restated at the subsection's head rather than in this entry alone, so a reader meets it with the findings: the mechanism is not reachable on any production surface and not on the plain legacy batch path either. The edit is ADD-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_fb_redesign_design.md:104-108`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 91, "section": "### §2.1 Test of the documented root-cause hypothesis — CONFIRMED `[data]`", "label": "“§2.1 Test of the documented root-cause hypothesis”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "The incumbent-confidence band and the contradiction value are **both** flat against correctness. Because the
override's *only* tunable knob is `bar = baseBar + confidenceScale·C`, and harm does not fall as `C` falls,
**no θ can carve corrections from harms** — the code-grounded proof of Phase 3's "best measurable θ disables
it" (theta_fit: the corr−harm-maximizing measurable bar drops fires to 0 at corr−harm 0, vs −571 on the
fitting split at the current bar). `[data]`" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-491 — REFUTED: making the override's comparison vertically fair does not repair it — even where the alternative fits the notes at least as well, it is still about 71 % harmful

> - **REFUTED — making the comparison vertically fair does not repair it.** The obvious repair is to
>   let the pass overturn a reading only when the replacement fits the sounding notes at least as
>   well. Measured, that band is still overwhelmingly harmful. The problem is not that the comparison
>   was unfair; it is that **the progression contradiction does not predict which root is correct at
>   these moments**. *Why:* measured across bands of the vertical gap, every one net-negative, with
>   the count and harm rate per band; the conclusion drawn is the one the numbers support and no more
>   — the earlier layer's vertical commit is a better predictor of the annotated root than the
>   progression re-pick, even where the alternative is its vertical equal.

**In plain words.** The obvious repair was to let the pass overturn a chord only when the replacement fits the sounding notes at least as well as the reading it displaces. Measured, that band is still wrong about seven times in ten. The problem is not that the comparison was unfair; it is that the progression argument does not predict which root is correct at these moments.

**Why.** Measured across five bands of the vertical gap, every one of them net-negative, with the count and the harm rate per band; the conclusion drawn is the one the numbers support and no more — the earlier layer's vertical commit is a better predictor of the annotated root than the progression re-pick, even when the alternative is its vertical equal.

**Status.** LIVE · decided 2026-07-06 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1157-1164`

**Provenance.** The direct test of the documented root-cause's natural repair, measured on the same 1043-fire population. It is what removes the large-surface repair option (§3.C) from the redesign, and it is stated with its own caveat — the vertical gap uses a proxy for the committed reading's own score, and the conclusion is stated to be independent of the proxy's precision because no band drops below about 71 % harm. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Written into the same §8 subsection as D-490, per the ruling that the family stays in one place, in that document's own voice and with its defense. The edit is ADD-ONLY. FORMER HOME, PRESERVED (#12): `cowork_fb_redesign_design.md:160-165`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 144, "section": "### §2.4 The incumbent-repair premise, tested directly — REFUTED `[data]`", "label": "“§2.4 The incumbent-repair premise, tested directly”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "Even in the **vertically-fair** band (`g ≤ 0` — the alternative is at least as vertically supported as the
committed reading) the override is still **70.8 %** harm (corr−harm −163). So repairing the vertical
asymmetry does **not** reach net-positive: the problem is not merely that the incumbent lacks a progression
term; it is that the progression contradiction is **uncorrelated with root-correctness** at these committed
slices. L4's vertical commit is a far better predictor of the DCML root than F-B's progression re-pick, even
when the alternative is vertically its equal. `[data]`" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-492 — The recommended redesign is to demote the override to an annotation — carrying the earlier reading unchanged and surfacing the contradiction — floored by simply disabling it

> - **RECOMMENDED AND NOT ADOPTED — demote the override to an ANNOTATION.** The recommendation on the
>   evidence above is to stop overturning the committed chord and instead **record that the
>   surrounding progression disagrees**, leaving the chord alone — accuracy-equivalent to simply
>   disabling the pass, while keeping the disagreement as calibrated uncertainty a later stage can
>   use. Tightening the trigger and repairing the comparison are both rejected as measured
>   net-negative. **This is a PROPOSAL, not a specification of this document: it is NOT adopted, and
>   no reader may implement it from this paragraph.** It is recorded as an INPUT to the one
>   prioritized fix plan, and the row that owns the demotion carries the cross-reference on the
>   plan's side. *Why:* every clause of the recommendation is measured and cited in the bullets
>   above; the loss it accepts — a modest number of genuine corrections given up — is stated and kept
>   in view rather than netted away.

**In plain words.** Instead of overturning the committed chord, the pass should record that the surrounding progression disagrees and leave the chord alone. That matches simply switching the pass off on accuracy, while keeping the disagreement as information a later stage can use. Tightening the trigger and repairing the comparison are both rejected: they were measured and both lose.

**Why.** Every clause is measured and cited: the override is net-harmful by 756 root decisions and no threshold repairs it; no structural gate on the available features beats disabling it, the best carve still losing by 163; the vertically-fair repair is refuted; and disabling and annotating tie on accuracy while annotating additionally preserves 1043 contradiction signals as calibrated uncertainty. The stated loss is 53 corrections, kept in view rather than netted away.

**Status.** LIVE · decided 2026-07-06 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1174-1184`

**Provenance.** The recommendation of a document whose banner records it as a DESIGN + DECISION SURFACE and states that the implementation is a separately-ratified build event. **D-387** (2026-07-07, `cowork_layer5_engagement_design.md`) records the open-mark vehicle the recommendation calls for, one day later; whether that constitutes the build event's ratification is not settled by either document and is not decided here. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ PHASE-3 FIX-PLAN INPUT, NOT AN AUTHORIZATION (user, 2026-08-04, dispatch cc_instruction_reads_3.md §4.1): the recommendation — demote the override to an annotation carrying the earlier reading unchanged, floored by disabling it — is recorded as an INPUT to the ONE prioritized fix plan D-231's phase 3 assembles, and is NOT acted on. D-231 forbids the fix design and D-490's falsification does not change that sequencing; the row that owns the demotion, and carries this cross-reference on the plan's side, is OPEN_ITEMS.md OI-2. ★ AND THE ARM IS CHECKED RATHER THAN ASSUMED (dispatch §4.2; read with the file tools at HEAD, 2026-08-04): the override is NOT reachable on any production surface, and NOT on the legacy production path either. attemptFineGrainOverride has exactly one caller, resolveCarriedReadings (src/composing/analysis/function/functionresolver.cpp:530); that function's only non-test caller in the whole tree is tools/batch_analyze.cpp:3321, inside runFullSpine, which is reached only from the --dump-fullspine block at :5506 and returns at :5519 before analyzeScore or analyzeRegions runs; and functionresolver.h is included by that one tool, by its own .cpp, and by src/composing/tests/functionresolver_tests.cpp, and by nothing else. So the measured-harmful mechanism is dormant behind a return-early diagnostic dump flag and the test suites — NARROWER than the dispatch's assumption A2, which supposed the legacy production path, and narrower than 'legacy' reads: plain flag-less batch_analyze, the reachability path OI-289 established for the legacy arm generally, does NOT reach it. There is no STOP. The document's own 2026-07-06 dormancy finding (§1.1) therefore still holds at HEAD, re-established rather than carried forward. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Written into the same §8 subsection as D-490, per the ruling that the family stays in one place. ★ THE RULING'S OWN CONDITION IS CARRIED INTO THE HOME TEXT: its NOT-ADOPTED status is stated in terms, so no reader takes a proposal for a specification, and the text says explicitly that no reader may implement it from that paragraph. The phase-3 fix-plan input marking this entry already carries is unchanged and is named in the home text without restating the plan-side row's content. The edit is ADD-ONLY. FORMER HOME, PRESERVED (#12): `cowork_fb_redesign_design.md:284-285`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 283, "section": "### §4.1 CC's evidence-based recommendation", "label": "“§4.1 CC's evidence-based recommendation”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Adopt §3.D‑1 (demote to annotation) as the redesign, with §3.A (disable the override action) as its
accuracy-equivalent floor; reject §3.B and §3.C as measured net-negative.** Rationale, all `[data]`-grounded:" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). ★ ONE STATED ESCAPE INSIDE THE PRESERVED VERBATIM ABOVE, recorded so the alteration is visible rather than silent (#12). The source document's own option label is written there with a NON-BREAKING hyphen — "§3.D‑1" — where the source uses an ordinary one. Why: the register's cross-reference guard scans this field for register identifiers, and with an ordinary hyphen that label is indistinguishable from a reference to a single-digit register entry, which does not exist — so moving the quote into this field would have manufactured a dangling reference that did not exist while the same characters sat in the verbatim field, which the guard does not scan. Nothing is lost and nothing else in the quote is touched; the label is recoverable by replacing that one character.

### D-493 — Restricting the override to the genuinely-coupled key-and-chord minority is UN-COMPUTABLE, not merely unmeasured: its trigger is not computed anywhere and building it is the still-owed joint step

> - **UN-COMPUTABLE, not merely unmeasured — the principled restriction cannot be built today.**
>   Restricting the override to the genuinely coupled key-and-chord minority is the principled form,
>   and its trigger **is not computed anywhere**. The binding blocker is the component that asks
>   whether a different carried KEY alternative flips the chord reading: that needs a per-key chord
>   re-decode, which **is** the joint key-and-chord step the record says is still owed, and the
>   closest existing mechanism explicitly leaves the chord unchanged. *Why:* established at the code,
>   both components separately; surfacing the trigger would mean **building** the joint step, which
>   the standing sequencing rules forbid at this stage. So the verdict is un-computable rather than
>   unmeasured, and this option is a long-run successor rather than a near-term choice.

**In plain words.** The principled home for this correction is the small set of moments where the key and the chord genuinely depend on each other. That set cannot be measured today, and not for want of a dump: half of the trigger requires re-deciding the chord under a different candidate key, which is precisely the joint step the project has not built. So this option is a long-run successor, not a near-term choice.

**Why.** Established at the code, both components separately: the binding blocker is the per-key chord re-decode, which the confidence contract itself says is still owed at Stage 5, and the closest existing mechanism — the joint re-key pass — explicitly leaves the chord unchanged; the other component is absent from this chain, which uses a score-global confidence rather than the per-slice sequence margin. Surfacing the trigger would therefore mean BUILDING the joint step, which #6/#7/#8 forbid at this stage — so the verdict is un-computable rather than unmeasured.

**Status.** LIVE · decided 2026-07-06 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1165-1173`

**Provenance.** The measured verdict of engage arc #2, recorded in the F-B redesign document as a correction of its own earlier UNKNOWN, with the measurement report named. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Written into the same §8 subsection as D-490, per the ruling that the family stays in one place, in that document's own voice and with its defense — the restriction is UN-COMPUTABLE today, and the home text states why that is a code fact rather than a missing measurement. The edit is ADD-ONLY. FORMER HOME, PRESERVED (#12): `cowork_fb_redesign_design.md:251-262`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 230, "section": "### §3.D — (re-frame) two theory-aligned alternatives to *overriding*", "label": "“§3.D”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **Projected split:** ~~UNKNOWN~~ → **UN-COMPUTABLE (engage arc #2 measured, 2026-07-06;
  `cc_engage_c3_measurement_report.md`).** The C3 trigger is **not computed anywhere** — VERDICT 3 (not
  read-only measurable, not surfaceable by additive default-off telemetry). The binding blocker is component
  **(b)** ("a different carried KEY alternative flips the chord reading"): the per-key chord re-decode it
  requires **is the gated joint key-and-chord step the contract §6-C3 says is "still owed at Stage 5"**
  ([keymodesequence.h:70-72](src/composing/analysis/key/keymodesequence.h#L70)), and even the closest
  mechanism — the J-key-iii joint re-key pass — **explicitly leaves the chord unchanged** ("the chord-axis
  side-effect … is DEFERRED to a faithful mechanism", [regionanalyzer.cpp:369-375](src/composing/analysis/region/regionanalyzer.cpp#L369)).
  Component (a) is likewise absent from the F-B fullspine chain (which uses `inferLocalKey(...)[0]` + a
  score-global `homeConf` sigmoid, not the per-slice L3 sequence margin; D-L3a's "no sequence-margin
  substrate on that path"). Surfacing (b) would mean **building** the joint step (forbidden by #6/#7/#8) —
  there is no already-computed signal to dump. `[code]` `[flag]`" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-495 — RATIFIED AMENDMENT A-5: when the phrase-boundary profile is flat, cadence admission relaxes with vote-weight scaling instead of starving

> - **Cadence admission needs a stated FALLBACK for a FEATURELESS phrase-boundary profile: relax admission
>   and scale the vote weight down, rather than starve.** Cadences are looked for at phrase ends,
>   which this layer reads as a published L1.5 fact — the graded phrase-boundary profile. In music
>   with almost no surface punctuation that profile goes featureless and everything gated on it gets nothing
>   to work with. The required fallback admits cadences more freely there and weights their votes
>   down by the graded strength the profile already carries. *Why:* derived from the review's stress
>   simulation — in a punctuation-poor texture the fermatas, rests and structural barlines are
>   deliberately absent, so the profile loses its contour and every phrase-gated consumer starves, while the
>   graded profile still carries the relative signal a scaled admission needs. **The obligation is
>   cadence admission's and therefore this layer's**; the profile it reads is the primitive's
>   published output and the primitive's own contract is unchanged by it.

**In plain words.** Cadences are only looked for at phrase ends. In music with almost no surface punctuation the phrase-end signal goes flat, and everything that depends on it gets nothing to work with. The amendment requires a specified fallback: admit cadences more freely there but weight their votes down, using the graded strength that is already computed.

**Why.** Derived from the review's stress simulation: in a punctuation-poor texture the fermatas, rests and structural barlines are deliberately absent, the graded profile goes flat, and everything gated on phrase boundaries starves — while the graded profile the design already produces still carries the relative signal the fallback needs.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:2143-2153`

**Provenance.** Amendment A-5 of the external architecture review, in a document whose banner records amendments A-1…A-10 as RATIFIED by the user on 2026-07-02. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ NOT A FRESH DECISION, stated so that nothing is counted twice (dispatch cc_instruction_reads_3.md §1.3): the amendment itself was ratified by the user at the 2026-07-02 architecture review, which is what this entry's Status line already records. Ratifying the ENTRY records only that the register transcribes that ratification correctly — it neither re-makes the decision nor adds a second ratification event to it. It binds on the phrase-boundary primitive's consumer; the primitive's own specification (`cowork_phrase_boundary_design.md`) does not carry it. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was whether the obligation or its trigger carries a fallback rule spanning both. The user ruled it WHOLE TO LAYER 5: the obligation is cadence admission's, and the flat phrase-boundary profile is a PUBLISHED L1.5 FACT the layer reads — so the primitive's own contract is untouched by it. Written into the Layer-5 section in that section's own voice, with its defense, and marked DESIGN-ONLY. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_architecture_review_2026_07.md:324-325`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 307, "section": "## 9. Proposed amendments (ranked; each ratification-gated; none is code)", "label": "§9", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **A-5 (from F-11). Specify the phrase-gate fallback** for flat boundary profiles (relax admission with vote-weight
  scaling instead of starving; the graded profile already carries the needed signal)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-629 — The resolver of carried uncertain readings IS the function layer itself — there is no distinct gated box between the note layers and it

> **★ THE RESOLVER OF CARRIED UNCERTAIN READINGS IS THIS LAYER ITSELF — THERE IS NO DISTINCT GATED BOX
> BETWEEN THE NOTE LAYERS AND IT (re-homed into this specification 2026-08-08 on the user's ruling).**
> When the earlier layers cannot decide between two readings they carry both forward with an
> uncertainty mark. **What resolves them is this layer, as part of assigning function**: it reads the
> carried alternatives and the marks at its gated entry, assigns function under each carried
> key/chord reading, and keeps the reading whose functional and cadential analysis is coherent. The
> "gated step" language elsewhere in the specifications describes **this layer's gated entry**, not a
> separate layer.

**In plain words.** When the earlier stages cannot decide between two readings they hand both forward with a mark. The thing that then picks one is not a separate component: it is the function stage, choosing as part of naming the harmony. The wording elsewhere about a gated step describes the point at which that stage begins, not another stage.

**Why.** Derived from the project's own layer-identity test and then confirmed by measurement. Every carried-ambiguity class was enumerated and each resolves on functional or cadential evidence — the share-tone pairs decisively, since naming the numeral IS choosing the reading — and the key-side classes form a circle that no fixed order discharges, which forces one joint computation. The corpus measurement then confirmed it: every separable cue the residual exposes belongs to an earlier layer, and the function-only remainder is small and structural. Two literature lineages agree, including one measured case where a standalone re-ranking layer was built and found saturated.

**Status.** LIVE · decided 2026-06-24 · ratified by user

**Home.** `ARCHITECTURE.md:2088-2104`

**Provenance.** `cowork_uncertain_resolver_investigation.md`, the open-item O1 investigation, RESOLVED and user-ratified 2026-06-24; the document's own status block records that the corpus measurement confirmed the verdict and that the three competing names were collapsed across the Layer-3 and Layer-4 specifications. Read in full by READ WAVE 6, 2026-08-04. The verdict's cross-layer consequence — that a failing case is a work budget spread over Layers 1-5 rather than the function layer's residual — is carried at `CLAUDE.md` gate block (D) and is not re-entered here (#6). This is the applied instance of **D-033**, the one-contribution-per-layer invariant. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii), which routes this document PER ENTRY to the subject's owning section). The subject is which component resolves the carried uncertainty, and the verdict is that it is the function layer itself — so the owning section is the Layer-5 section of `ARCHITECTURE.md`, written there in that section's own voice with the derivation and the corpus confirmation, and with the three tests it satisfies named. THE CROSS-LAYER-BUDGET CONSEQUENCE IS NOT COPIED (#6): it is homed at `CLAUDE.md` gate block (D) and stays there. FORMER HOME, PRESERVED (#12): `cowork_uncertain_resolver_investigation.md:96-102`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 94, "section": "## Provisional verdict (gated on part 3)", "label": "“Provisional verdict”", "delegated": null, "delegation": "CLAUDE.md:871", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**The resolver is Architectural Layer 5 (function) itself — there is no distinct gated box between the note-layers and
Layer 5.** Layer 5 reads the carried alternatives and the \"uncertain\" marks at its **gated entry**, and resolves them
**as part of** assigning function: it assigns function under the carried key/chord readings and keeps the reading whose
functional/cadential analysis is coherent. The \"gated step\" language in the specs describes *Layer 5's gated entry*,
not a separate layer. This satisfies minimality (no new box), the `(evidence × question)` invariant (same evidence,
same question), and the forward-only contract (Layer 5 selects among carried alternatives; it does not re-enter L3 or
L4)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

