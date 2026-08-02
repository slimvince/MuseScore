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

**Home.** `ARCHITECTURE.md:1392-1393`

**Provenance.** ARCHITECTURE.md:1389-1398 (Layer 5 - Built+Dormant, design ratified)

### D-080 — Carried abstentions are resolved by selecting among the carried readings, never re-derived

> the carried L4 abstentions are resolved by **selecting** among the carried readings (never re-derived)

**In plain words.** Where the chord stage could not decide, the function stage picks from the options it was handed. It does not work the chord out again from the notes.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1396-1397`

**Provenance.** ARCHITECTURE.md:1389-1398

### D-081 — The cadence detector is key-agnostic

> The cadence
> detector is **key-agnostic** (it votes for the key; it does not read a resolved key).

**In plain words.** The part that spots cadences must not be told what key it is in - it is one of the things that decides the key, so reading the answer first would be circular.

**Why.** Both rejected alternatives are named with their defect at the layer's own design document (`cowork_layer5_function_design.md` §9-D2, the same decision entered as **D-336**): the earlier key-dependent detector is circular and conflates the perfect with the imperfect cadence, and a single-chord interval test false-positives on tonic-to-subdominant and tonic-to-dominant because it tests whether the leading tone is *present* rather than whether it *resolves*. The same document records the approach's ratified limit (§5.2): a plain V-to-I and a plain I-to-IV are exact transpositions, so the resolution event alone cannot separate them — which is why the phrase gate, the dominant seventh, and the key layer's aggregation of the tonic votes carry the discrimination rather than the detector.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1396-1397`

**Provenance.** ARCHITECTURE.md:1397. open_items/OI-166 records that the built detector is key-agnostic but CHORD-derived, not the bass-driven pre-scan specified. Defense filled 2026-08-02 by the phase-1g triage wave from `cowork_layer5_function_design.md` §9-D2/§5.2 — the act the phase-1f note named and left for the wave that reads that document; the register entry for the same decision at its design-document home is D-336

### D-082 — The grouping layer is additive, read-only, with no feedback

> additive, read-only, no feedback into L5.

**In plain words.** The stage that assembles phrases and key areas only organises what earlier stages decided. It never changes their answers.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1404`

**Provenance.** ARCHITECTURE.md:1400-1407 (Layer 6 - Design-only, v1 spec)

### D-083 — Hierarchy, periods and prolongation are out of the validatable core

> Hierarchy,
> periods/sentences, and prolongation are out of the validatable core (verifiability contract, §2.15).

**In plain words.** Deeper structural theory - nested hierarchy, periods, prolongation - is deliberately left out, because we have no annotated music to check it against.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1405-1406`

**Provenance.** ARCHITECTURE.md:1400-1407, deriving from D-029

### D-084 — The progression-schema recognizer is a consumer of the function layer, not a new layer

> an L5 *consumer* (a prior + an annotation), not a new layer

**In plain words.** Recognising well-known chord patterns is something that reads the finished analysis and annotates it. It is not another stage in the chain.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1411`

**Provenance.** ARCHITECTURE.md:1409-1414 'Scaffolding-first, deferred'

### D-085 — The voice-leading axis is a separate axis with its own layers

> the **orthogonal voice-leading axis** with its own layers (where melodic phrases [MT] and
>   chord **voicing / arrangement** are analysed)

**In plain words.** How the individual voices move is a second, independent line of analysis alongside the harmonic one, with its own stages.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-03 · ratifier not stated

**Home.** `ARCHITECTURE.md:895-896`

**Provenance.** ARCHITECTURE.md:896-899 records the foundation BUILT (dormant). ARCHITECTURE.md:1415-1415 still says the voice-leading layer is 'not built' - see OPEN_ITEMS OI-232

### D-248 — Tonicization labels are not implemented and are deferred

> - Tonicization labels (V/V, V/ii, V/IV etc.) — **NOT YET IMPLEMENTED**
>   (deferred; no `relativeRoot`/secondary-dominant field in
>   `ChordFunction`; requires standalone implementation first)

**In plain words.** Applied-chord labels such as V/V are not produced. The data structure has no field for the relative root, and the feature waits on a standalone implementation.

**Why.** The constraint is stated in the record: `ChordFunction` carries no `relativeRoot` or secondary-dominant field, so the label has nowhere to live (ARCHITECTURE.md:6013-6014).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6012-6014`

**Provenance.** ARCHITECTURE.md:6012-6014. Section 5.10 (ARCHITECTURE.md:3860) is the tonicization section; the memory-held backlog item is recorded in the same terms. ★ RATIFIED (user, 2026-08-02) with the revisit to be PLANNED: for the ultimate objective (maximum-precision inference) the feature may be needed — the ground truth annotates applied chords, so not producing them costs Roman-numeral agreement wherever the annotator wrote one. Row OI-267 carries the planning obligation, including the OI-53 tension (a live classifier emitting V7/x was found on the legacy path while this entry's home says not implemented).

### D-291 — The tonicization labeller is NOT wired, and the metric is NOT changed to credit it - both would hide a real key error

> - **★ HEADROOM CORRECTION (load-bearing — propagate to docs):** the biggest precision slice relocates **Stage 6 → Stage 4** (local-modulation
>   detection). **Do NOT wire 6-tonic-i** (games rn_agree, degrades correctness). Real lever = a **LOCAL-MODULATION / KeyArea detector
>   (Stage 4)**, ~95% of S1, signal = sustained span + local cadence (consumes the committed CADENCE INSTRUMENT + KeyArea); 6-tonic-i's

**In plain words.** A working labeller for applied chords was deliberately left unwired, and the proposal to make the accuracy measurement treat its labels as equivalent to the annotator's was rejected. Both would have raised the reported Roman-numeral agreement while the underlying reading stayed wrong: the annotator has changed key, and labelling the chord relative to the old key hides that.

**Why.** Measured: of the affected cases 92.7 % are cadence-confirmed local keys in the ground truth and 79.2 % last five chords or more, so the annotator's modulation is correct for about 97 % of them; only 2.7 % are brief enough for either reading to be defensible. The comparison already credits the label by root and quality, so it does not over-penalise - it MASKS. Recorded as the clearest win of the measure-before-building rule: without the check the labeller would have shipped and improved the number while worsening the output.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

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

**Home.** `cowork_layer5_function_design.md:612-617`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-336 — Cadence detection is key-agnostic and votes for the key rather than reading one

> - **D2 — Cadence detection is key-agnostic and votes for the key; it does not read a resolved key.** *Rejected:* the prior
>   key-dependent detector, which is circular and conflates the perfect with the imperfect cadence; and the single-chord
>   interval test, which false-positives on tonic-to-subdominant and tonic-to-dominant because it tests leading-tone
>   presence (the major third of any major triad) rather than leading-tone resolution. The event-pair feature test with the
>   phrase gate is the corrected design.

**In plain words.** Points of harmonic closure are found without being told the key, and each one casts a vote for what the key is. Reading a key that a cadence is supposed to help decide would be circular.

**Why.** Both rejected alternatives are named with their defect: the earlier key-dependent detector is circular and conflates the perfect with the imperfect cadence, and a single-chord interval test false-positives on tonic-to-subdominant and tonic-to-dominant because it tests whether the leading tone is present rather than whether it resolves. The layer's own recorded limit is that a plain V-to-I and a plain I-to-IV are exact transpositions, so the resolution event alone cannot separate them — which is why the phrase gate, the seventh, and the key layer's aggregation carry the discrimination.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:618-622`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-337 — A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost

> - **D3 — Tonicization is the default; modulation requires cadence confirmation plus persistence, as a change-cost.**
>   *Rejected:* a fixed-duration rule (no published threshold exists and the boundary is a continuum); and resolving the
>   distinction in the key layer (it needs function). The hysteresis over the local-key decision matches the ground-truth

**In plain words.** When the music leans toward a note other than the home tonic, the home key holds and the chord is written as an applied chord. The key changes only when a cadence confirms the new key and the music stays in it; how long it must stay is a cost that falls as the candidate area grows, not a fixed number of bars.

**Why.** Both alternatives are rejected with reasons: a fixed-duration rule has no published threshold and the boundary is a genuine continuum, and resolving the distinction in the key layer cannot work because it needs function. The hysteresis form is chosen because it matches the ground-truth annotation convention.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:623-625`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-338 — The function layer selects among the chord layer's carried readings and never re-derives a chord from the notes

> - **D4 — The layer selects among Layer 4's carried readings; it never re-derives.** *Rejected:* re-scoring the slice from
>   the notes (that is Layer 4's job and would duplicate it) — the structural content of the ratified resolution-by-
>   selection: a case separable by a note cue is a lower-layer case, a case separable only by function is this layer's,
>   leaving no third box.

**In plain words.** Where the chord layer left a stretch open, this layer picks one of the readings that layer carried. It never goes back to the notes and works out a chord of its own.

**Why.** Structural, and stated as such: a case separable by a note cue is a lower-layer case and a case separable only by function is this layer's, which leaves no third box — so re-scoring from the notes would duplicate the layer below.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:627-630`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

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

**Home.** `cowork_layer5_function_design.md:547-554`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

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

**Home.** `cowork_layer5_function_design.md:888-897`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-342 — Putting the function layer into production is DEFERRED INDEFINITELY — the posture is a dormant build with ground-truth validation

> - **Engagement framing.** References to an "engagement hard-stop" / "before any production switch" (§5/§10) remain true
>   *conditionally* — engagement (Phase 5d) is **deferred indefinitely** (production out of scope; the posture is dormant
>   build + ground-truth validation). The hard-stops apply *if* a switch is ever made; they are not pending work.

**In plain words.** Switching the function layer on in the product is not scheduled. It is built and checked against published human analyses, and stays inactive; the conditions written for a switch apply if one is ever made, and are not outstanding work.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `cowork_layer5_function_design.md:696-698`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

