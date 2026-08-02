# Decisions group C — Cross-cutting analysis contracts

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-022 — The founding principle - analyse at the finest grain, coarser views are derived

> **The founding principle: analyze at the finest grain where harmony is well-defined, and make everything coarser a
> *derived view*.**

**In plain words.** The analysis works on the smallest stretch over which the sounding harmony does not change. Phrases, key areas and sections are then read off that, never analysed directly.

**Why.** Stated constraint, ARCHITECTURE.md:812-814: analysing at the finest grain is what makes segmentation a fact rather than a judgment (over-grab becomes structurally impossible), it aligns the architecture with the per-slice oracle measurement already built, and it matches the published state of the art - Contrapunctus labels every event.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:810-811`

**Provenance.** ARCHITECTURE.md:808 heading says '(ratified; full statements in cowork_target_architecture.md)'; the date and ratifier are not stated at this home

### D-023 — The atomic analysis unit is the constant-sonority slice, never the metric beat

> The atomic analysis unit is the **constant-sonority slice** (L2), never the metric beat

**In plain words.** The smallest thing analysed is a stretch during which exactly the same notes are sounding - not a beat of the bar.

**Why.** Same passage as D-022, ARCHITECTURE.md:810-814: the metric beat is not where harmony is well-defined; the constant-sonority slice is, and every coarser unit is derived from it.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:811`

**Provenance.** ARCHITECTURE.md:808-815. The joint estimator's own unit is the ONSET event (jointdecoder.h:67), not this slice - see OPEN_ITEMS OI-228

### D-024 — The fact layers are style-agnostic; style lives only in calibration

> L1 (notes) and L2 (slicing) are **style-agnostic and
>   lossless** — they carry facts, never style. Style-specificity lives **only** in the *calibration* of the judgment
>   layers (their priors/weights), **never in structure**.

**In plain words.** Reading the notes and cutting the music into constant-sound stretches works the same for every kind of music. Whether a piece is Baroque or jazz can change only the numbers the judging layers use, never the shape of the code.

**Why.** Stated constraint, ARCHITECTURE.md:817-820: confining style to the calibration of the judgment layers sharpens §2.1 - not merely data-driven style, but style kept out of the layers that carry facts, so the fact surface cannot silently differ between styles.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:817-820`

**Provenance.** ARCHITECTURE.md:808 ratified banner; sharpens §2.1 (D-070)

### D-025 — Forward-only, with two scoped escapes

> The **ratified** architecture (user-ratified;
> `cowork_target_architecture.md` §2) is **forward-only**:

**In plain words.** Each stage was to pass its answer forward and never reach back. A confident earlier answer could be overturned only by re-running that one stretch forwards, and the one genuinely tangled key-versus-chord case got a narrow, gated exception.

**Why.** Measurement, ARCHITECTURE.md:787-790: the investigation measured the full joint cross-layer search INERT, and located the realisable gain in soft-evidence quality carried forward (calibrated confidence + ranked alternatives) rather than global cycling.

**Status.** SUPERSEDED BY D-001 · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:790-791`

**Provenance.** The 2026-07-17 governing decision (D-001) replaces the mechanism with ONE joint decode - the mechanism this block had ruled out. No supersession banner was added to §2.14 - see OPEN_ITEMS OI-234 ★ USER RULING 2026-08-02 (OI-234, reading 3): forward-only as the architecture ruling is SUPERSEDED BY D-001 (the 2026-07-17 joint decision, adopted 2026-07-26); the supersession now has a ruling naming it (was superseded-in-fact). The §2.14 scoping annotation records the ruling.

### D-026 — The global joint-lattice decode was measured inert (2026-06-29)

> The subsequent investigation
> **measured the full joint cross-layer search INERT**

**In plain words.** An earlier plan to search all the possibilities at once was tested and found to add nothing, so the effort was redirected into better evidence flowing forwards.

**Why.** The measurement itself (ARCHITECTURE.md:787-788). What the record does NOT state is how it was reconciled with the 2026-07-17 joint estimator, which is one - see open_items/OI-234.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:787-788`

**Provenance.** The joint estimator (D-001) is a global joint decode and is in production on both surfaces. The record does not state how this measurement was reconciled with the later ruling - see OPEN_ITEMS OI-234 ★ USER RULING 2026-08-02 (OI-234, reading 3): the finding STANDS FOR WHAT IT TESTED — cycling/re-ranking over the per-layer pipeline's carried candidate lists adds nothing, binding on that design class — and does NOT bear on the fitted semi-Markov joint decode (a different mechanism class). Returned to LIVE, scoped; the §2.14 annotation records the scoping (was superseded-in-fact).

### D-027 — Every layer emits ranked candidates plus a confidence, never a forced point estimate

> each layer is feed-forward and emits **ranked candidates + a confidence**, never a forced point estimate;

**In plain words.** No stage is allowed to report only its single best answer. It reports the runners-up too, with a measure of how clear-cut the choice was.

**Why.** Stated constraint, ARCHITECTURE.md:733-735: irrevocable point estimates block iteration and provisional results with confidence metadata enable it, so every layer's output must carry the alternatives and the confidence a later layer would need to overturn it.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:792`

**Provenance.** The mechanism around it (D-025) is superseded in fact, but the ranked-alternatives requirement is carried forward by the joint estimator's published candidate lists (D-006)

### D-028 — The span typology - every layer names the span it operates on; bare 'region' is banned

> "Region" unqualified is **banned** as
>   ambiguous; every layer names the span it operates on.

**In plain words.** The word 'region' on its own is forbidden, because it hides which kind of stretch is meant. Each stretch has its own name: the chord-span, the key-span, the punctuation-span and so on.

**Why.** Research citation, ARCHITECTURE.md:865 - the span typology follows the GTTM premise of independent structures (Lerdahl & Jackendoff); the ban on the bare word is because a 'region' is a FAMILY of spans and the unqualified word names none of them (:765, :786-787).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:864-865`

**Provenance.** ARCHITECTURE.md:833-850 records the rename CONFIRMED (user, 2026-07-02) and EXECUTED 2026-07-03 'propagated through every layer spec'. ARCHITECTURE.md itself still uses the banned word 216 times including section headings - see OPEN_ITEMS OI-233

### D-029 — The verifiability contract

> prefer what we can verify against ground truth (it is how we catch our own theory
>   errors); for sound theory we cannot verify against the current corpus, build it with an explicit
>   **alternative-confidence path** *and* an **"empirically-unvalidated" mark**, rather than refusing it

**In plain words.** Prefer what we can check against annotated music. Where the theory is sound but we have nothing to check it against, build it anyway - but mark it as unchecked and give it its own confidence path.

**Why.** Stated constraint, ARCHITECTURE.md:872-875: checking against ground truth is how we catch our own theory errors, and refusing sound theory we cannot yet check would forfeit the jazz and pop reach, where the theory exists and the corpus does not.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:872-874`

**Provenance.** ARCHITECTURE.md:808 ratified banner

### D-030 — Bounded context - cost scales with the working span, not the whole score

> The binding scale requirements: **(R1)** cost scales with the working span, not the whole
>   score; **(R2)**
>   re-analysis is incremental over the dirty span plus a bounded margin; **(R3)** the working span is **extensible**

**In plain words.** Analysis runs on what the user has selected. The work must grow with the size of that selection, not with the size of the piece; re-analysis after an edit must only redo the changed part; and a layer that needs more music asks for it rather than reading everything.

**Why.** Stated constraint, ARCHITECTURE.md:876-880: the analysis runs on the user's selection, so a layer needing more must request an append-only extension from Layer 1 carrying a stop condition and a hard bound. The three binding scale requirements R1-R3 are stated there; the detailed cross-layer specification is `cowork_bounded_context_design.md`.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:878-880`

**Provenance.** ARCHITECTURE.md:880-884 names cowork_bounded_context_design.md as the ONE detailed cross-layer spec and records the 2026-07-02 user directive making it 'the hard gate before L6'. DIRECTLY CONTRADICTED by D-011 (whole-score decode per query, no caching) - see OPEN_ITEMS OI-210/OI-212

### D-031 — Whole-score analysis is the degenerate case, not the design

> Whole-score analysis is the degenerate case (selection = score).

**In plain words.** Analysing the whole piece is what happens when the user has selected the whole piece. It is not the normal mode of operation.

**Why.** Same passage, ARCHITECTURE.md:880: whole-score analysis is what the bounded-context rule produces when the selection happens to be the whole score - a case of the rule, not an exception to it.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:880`

**Provenance.** Same home as D-030. The record producer analyses the whole score regardless of the requested span (OI-212)

### D-032 — Every confidence crossing a layer boundary is in 0..1, class-declared, with its decision named

> **The cross-layer confidence contract — every confidence that crosses a layer boundary is bounded,
> class-declared, and named to its decision.** At a layer boundary — any value another layer may read — a
> confidence is **in [0,1], class-declared (a ranking margin or a calibrated probability), and stated

**In plain words.** Inside a stage, a confidence can be on any scale. The moment another stage can read it, it must be a 0-to-1 number, labelled with what kind of confidence it is and what decision it belongs to.

**Why.** Stated constraint, `cowork_confidence_contract.md:13-21` ('Why this contract exists'): the forward-override mechanism numerically compares a later layer's contradiction strength against an earlier layer's confidence, and those quantities are incommensurable by construction today - Layer 3 publishes a sequence margin, Layer 4 a three-part composite, Layer 5 an unbounded additive score. Fitting weights cannot repair a comparison between quantities with undefined semantics; it would bury the incoherence in fitted constants.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:910-912`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass, cc_instruction_spec_completion.md): the contract's own document `cowork_confidence_contract.md:39-40` (ratified there, user, 2026-07-02) remains the authoritative full statement; the rule is now stated in the cross-cutting contracts of the architecture document (§2.15), which is where a reader of the layers meets it. The stale 'ratification-gated' parenthetical in the §2.14 forward-override bullet of §2.15 is corrected in the same pass (OPEN_ITEMS OI-232, item 5). Contradicted by D-019 on the production record arm - see OPEN_ITEMS OI-231

### D-033 — Each layer owns one evidence-source-times-question contribution and uses all of L1's information

> each layer owns one *(evidence-source × question)*
>   contribution — stated as "owns the *[named evidence]* contribution to *X*", with what it does **not** own made
>   explicit — defers what needs later evidence (carried as ranked alternatives + an uncertain mark), and within its scope
>   uses *all* the information L1 carries losslessly (notated spelling, metric weight, voice).

**In plain words.** Each stage owns one contribution and says plainly what it does not own, handing unresolved cases forward as ranked options. Owning one contribution does not narrow what it may look at: within its scope it uses all the information the note reader carries - how the note is spelt, where it falls in the bar, and which voice it is in.

**Why.** Stated constraint, ARCHITECTURE.md:885-888: the single-responsibility half is what lets a layer say what it does NOT own, and the maximal-information half is what stops that ownership from being read as permission to ignore evidence Layer 1 already carries.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:885-888`

**Provenance.** ARCHITECTURE.md:808 ratified banner. The joint emission reads only struck notes (OI-228) and the shared tone surface is voice-blind (OI-74)

### D-034 — A new layer or axis is admitted only through three co-equal gates

> **A new layer or axis is admitted only when it clears three co-equal gates,
>   all required:**

**In plain words.** A new stage is added only if it carries one distinct responsibility, can be validated somehow, and buys something we can actually check. Carrying a distinct responsibility is enough on its own, even with no immediate accuracy gain.

**Why.** Stated constraint, ARCHITECTURE.md:902-909: gate (1) separation of concerns is a structural mandate sufficient on its own even at zero accuracy gain; gates (2) verifiability and (3) proportionality exist against the opposite error, and the record names the reminder - Contrapunctus is competitive with the state of the art with NO explicit grouping layer.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:902-903`

**Provenance.** ARCHITECTURE.md:902-909

### D-035 — The effort setting - every cost-driving choice is a setting, never a hardcoded constant

> **(a)** every cost-driving choice is an
> explicit *setting*, never a hardcoded constant; **(b)** every optional expensive refinement is a cleanly separable on/off
> stage.

**In plain words.** Anything that makes the analysis slower must be something the user or the caller can turn down, not a number baked into the code; and any expensive extra step must be separable so it can be switched off.

**Why.** Stated constraint, ARCHITECTURE.md:801-805: the effort dial is a calibration knob, not a structural one, so its two standing rules follow - every cost-driving choice is an explicit setting, and every optional expensive refinement is a cleanly separable stage.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:803-805`

**Provenance.** ARCHITECTURE.md:801-805. Not implemented: the effort setting does not exist and the decode's cost drivers (segment cap, key prune width) are compiled-in constants - tracked at OI-209/OI-210

### D-036 — Accumulating gates are a warning sign - add iteration, not more gates

> When a feedforward layer acquires many gates
> and guards to compensate for missing upstream feedback, that is a symptom of missing
> iteration — not a sign that the layer needs more gates.

**In plain words.** If a stage keeps needing new special cases, the problem is that it is missing information from elsewhere. Adding another special case makes it worse.

**Why.** Stated constraint, ARCHITECTURE.md:709-713: each gate is a heuristic patch on a structural limitation, so a rising gate count is a symptom of missing iteration rather than an argument for more gates.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:709-711`

**Provenance.** ARCHITECTURE.md:709-713; restated as an ongoing concern at :2131-2136

### D-099 — Negative evidence is information - a ruled-out possibility is carried, not dropped

> **Negative evidence is information — a ruled-out reading is carried, not dropped.** A layer that
> eliminates a reading publishes the elimination rather than discarding it: the ruled-out reading is
> carried on the output surface at low confidence, unless the elimination is recomputable from what that

**In plain words.** Knowing that something is not the case is itself useful. A reading that has been ruled out is kept at low confidence rather than thrown away, unless we could work out the exclusion again from what we did keep.

**Why.** Stated constraint, `CLAUDE.md` #12: a ruled-out possibility is evidence - finding by exclusion - so it is carried at low confidence unless the exclusion is recomputable from what is kept.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `ARCHITECTURE.md:926-928`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): CLAUDE.md guiding principle #12, ratified by the user 2026-07-06, remains the standing principle; the layer-facing rule is now stated in the cross-cutting analysis contracts it governs. OPEN_ITEMS OI-237 closes on this move

### D-100 — Every derived fact is published exactly once, on the producing layer's output surface

> **Every derived analytical fact is published exactly once, on the producing layer's output surface;
> consumers read it and never re-derive it.** For **evidence-class** facts — hints a later design could

**In plain words.** Whatever a stage works out, it publishes on its own output surface; every later stage reads that instead of working it out again. Facts that are hints a later stage might one day use are published broadly even when nothing reads them yet, each carrying whether it has been established, because a consumer may not rely on an unestablished fact. What to do with a fact nobody reads is decided case by case: keep it with a named future reader stated, or remove it - and a reader outside the analysis counts.

**Why.** Stated constraint, `CLAUDE.md` fact-publication corollary, with its evidence named there: `cowork_siloed_facts_audit.md` found 17 instances of facts being re-derived rather than read. The 2026-07-12 amendment's own recorded reason is the user's: a visible spread of published evidence lets a future design RECOGNIZE facts it would never have thought to ask for.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `ARCHITECTURE.md:934-935`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): CLAUDE.md's 'Fact-publication corollary to #6/#7/#12' (ratified 2026-07-10, amended 2026-07-12 - publish EVIDENCE-class facts broadly, each carrying its establishment status) remains the standing corollary; the layer-facing rule is now stated in the cross-cutting analysis contracts. OPEN_ITEMS OI-237 closes on this move

### D-115 — The regression stop is the granularity-robust unit; root governs, key and Roman numeral ride beside

> the **class-(b) (pitch-class-decidable-root) root-disagree DURATION
>   must be NON-INCREASING** vs the committed reference — the *meaningful* functional errors never grow.

**In plain words.** A change is allowed to ship only if the total amount of music on which we name the wrong chord root - counted where the root is decidable at all - does not grow. The key and the Roman numeral are watched alongside but do not govern.

**Why.** Measurement, `CLAUDE.md` gate block (C): the batch region gate it replaced under-counted the true per-onset root error by roughly 15 to 56 times - it measured a small music21-filtered corner in which pitch-class-undecidable rotations were about 53 % of the residual, against about 3.5 % on the robust unit - so the robust unit is governed by the meaningful errors and is segmentation-invariant by construction.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md gate block (A), ratified R10-b 2026-07-06; supersedes the batch case-identity stop preserved as block (C)

### D-191 — The two-tier regression class policy - functional regression stops, rotation churn is tracked

> **Two-tier refinement (user-ratified 2026-06-22) — class-(b) functional regression vs class-(a)
> symmetric-rotation churn.** A *new* BIR=false case is one of two classes:
> - **Class (b) — functional/key regression: UNCHANGED HARD STOP.** A new BIR=false case at a sonority
>   whose root is *pitch-class-decidable* (any non-symmetric chord — triads, dominant sevenths, etc.)
>   where the analysis now gets the root or key wrong. **Zero** new class-(b) cases on any preset, ever.
>   This is the gate's real intent and does not move.

**In plain words.** A newly wrong reading is one of two kinds. If the chord's root is decidable from the notes at all - any ordinary triad or seventh chord - and the analysis now gets the root or the key wrong, that is a functional regression and it is an absolute bar: never one more of them, on any style preset. The other kind is a sonority whose root the notes genuinely cannot decide - a symmetric diminished seventh, an augmented chord, a chord that shares all its notes with another - where no reading is more correct than another by pitch alone. Those are counted and watched, not barred.

**Why.** Stated constraint, CLAUDE.md:458-463: the pitch-class analyzer is spelling-blind and cannot pick the spelling-correct rotation of a symmetric chord, so counting a rotation flip as a regression would be counting a coin-flip. Measurement bounding the split: on the robust unit the decidable-root class is about 96.5 % of root-fail time (CLAUDE.md:428-431), so the hard stop governs almost all of it. Founding evidence, verified at the score against music21 ground truth: bwv272@4320, bwv289@20160, bwv291@17760, bwv387@10560 (CLAUDE.md:477-480).

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Home.** `CLAUDE.md:452`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:443-486, block (B), carried over unchanged to the robust unit at R10-b. Full provenance `cowork_gate_policy_amendment.md`. The four guardrails that make the tracked class conditional - verified at the score per case, default to the barred class on any doubt, the barred class non-increasing, case identities recorded - are at CLAUDE.md:464-473.

### D-210 — An exotic mode is graded against its parent collection's minor key, not its own tonic triad

> **An exotic mode is graded against its PARENT COLLECTION's minor key, not against its own tonic
> triad** (user-ruled 2026-07-13, OI-132; landed `800f1a12bf`). When our analysis emits one of the five
> dominant-family exotic modes, grading reduces it to the minor key of the collection it belongs to — an

**In plain words.** When the analysis emits one of the five dominant-family exotic modes, grading reduces it to the MINOR key of the collection it belongs to - an emitted C-sharp Phrygian dominant is graded as F-sharp minor, the key it is the dominant of - rather than to the key its own tonic triad would name.

**Why.** Measurement, CLAUDE.md:359-364: on the affected duration the parent-collection reading agrees with the published annotators on 67 % of the local key column, and the tonic-triad reading on 0 %. The consolidation moved only the key columns - root, Roman numeral, every root-failing run set and the hard-stop duration were byte-identical, run-difference +0/-0 on all presets.

**Status.** LIVE · decided 2026-07-13 · ratified by user

**Home.** `CLAUDE.md:378-380`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:239 (OI-132), ruled by the user 2026-07-13 and landed at 800f1a12bf. The adjudication probe is `cc_mode_grading_adjudication_probe_report.md`; the re-baseline record is `cc_key_grading_and_calibration_rebaseline_report.md`. It is implemented in ONE shared reduction, `compare_rn._our_key_tonic`, onto which the second key parser was folded (#6). OPEN_ITEMS OI-240 closes on this move

### D-211 — Key agreement is reported against both the global home key and the local key

> **Key agreement is reported against BOTH the global home key and the local key** (user-ratified
> 2026-07-12, OI-143; adopted `d9b52ba969`). Both columns are carried everywhere the key column appears;
> neither replaces the other. *Why:* measured — the local percentage is lower than the home percentage, and that

**In plain words.** There are two defensible questions about a key reading - does it match the key the piece is in, and does it match the key this passage is in - and the record carries both numbers everywhere the key column appears, rather than choosing one.

**Why.** Measurement, OPEN_ITEMS.md:253: the local figure is lower than the home figure, which is itself the finding - the analyzer tracks the tonal home more faithfully than it tracks momentary tonicizations - so keeping only one column would have hidden a real property of the system.

**Status.** LIVE · decided 2026-07-12 · ratified by user

**Home.** `CLAUDE.md:388-390`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:270 (OI-143), adopted at d9b52ba969. The current values are in the CLAUDE.md gate block (A): key-agree against the home key 56.14 %, against the local key 78.42 %. OPEN_ITEMS OI-240 closes on this move

### D-212 — The regression stop is abstain-aware: an abstention counts as disagreement on root

> **The stop is ABSTAIN-AWARE: on the root axis an abstention counts as a DISAGREEMENT** (ruled and
> mechanically enforced 2026-07-12, OI-33). A cell where our analysis carries no root pitch class is
> scored as a root disagreement; on the key axis abstained cells are instead **excluded from the

**In plain words.** If the analysis declines to name a chord root, that counts as getting it wrong, so declining more often can never look like improving. On the key axis the declined cells are excluded from the percentage instead, and a rise in declining trips a flag in the comparison tool.

**Why.** Stated constraint, OPEN_ITEMS.md:200: the metric is abstention-reducible - without the convention, a change that made the system decline more would raise the agreement figure without analysing anything better - and the convention was owed before any abstaining path could be gated on the stop at all.

**Status.** LIVE · decided 2026-07-12 · ratified by user

**Home.** `CLAUDE.md:393-395`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:217 (OI-33), resolved 2026-07-12 in the key-layer readiness wave 1. Its current reading on the production arm is D-114 - the decoder commits its best path, so the abstain counter reads zero. OPEN_ITEMS OI-240 closes on this move

### D-243 — The planning band for the vertical engine, and the corpora excluded from it

> For planning purposes, the current vertical tertian engine plus targeted texture
> fixes should be expected to plateau around 65–75% exact external root+quality
> agreement on **full-texture tonal corpora** (SATB choral, chamber, full piano
> accompaniment). This band applies specifically to region-centric DCML comparison
> methodology. Thin-texture corpora (Mozart piano sonatas, C.P.E. Bach keyboard,
> solo melody) are excluded from this target — they require a separate inference
> strategy and should not be compared against the same band. The When in Rome and
> music21-surface comparisons use different methodologies and are not directly
> comparable to this figure.

**In plain words.** For planning, the vertical engine plus texture fixes is expected to settle around 65-75 % exact root-and-quality agreement on full-texture tonal music, measured region-centrically against DCML annotations. Thin-texture corpora are outside that target and are not judged against it, and figures from other comparison methods are not comparable to it.

**Why.** The constraint stated in the record: the band is tied to one comparison methodology (region-centric DCML), and mixing methodologies is what makes a figure incomparable (ARCHITECTURE.md:3570-3575).

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3567-3575`

**Provenance.** The band is stated at ARCHITECTURE.md:3567-3575. The governing measurement surface is now the robust unit ratified at R10-b (CLAUDE.md gate block (A)), whose figures are reported per preset on a different unit; no ruling names this band as replaced. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

