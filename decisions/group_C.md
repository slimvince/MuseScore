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

### D-260 — Analysis output covers exactly the selection; everything loaded beyond it is evidence, never a result

> **Invariant.** The analysis output covers **exactly the selection**; everything outside it is evidence, never a
> result.

**In plain words.** The user's selection is the output span: labels are emitted only for it. Music loaded from outside the selection is pulled in as evidence for judging the selection's edges and is never itself labelled.

**Why.** Stated with the rule (cowork_bounded_context_design.md:21-26): the shipped product analyses the part of the score the user selected, and a layer often needs evidence from outside it to judge its edges. Separating the output span from the loaded span is what lets a layer read more music without changing what the user asked to have analysed.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:43-44`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3 carries the status banner 'SIGNED (user, 2026-07-02)'; the invariant is stated at :43-44. The cross-cutting bounded-context bullet of ARCHITECTURE.md points at this document as the ONE cross-layer extension spec (:10). Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-261 — A layer never guesses how much context it needs - the amount is discovered by convergence

> 3. A layer must distinguish **"unavailable because not loaded"** (→ request extension) from **"unavailable because the
>    score starts/ends here"** (→ proceed, truncated). Architectural Layer 1 reports which.
> 4. A layer **outputs analysis only for the selection**; extended context is evidence, never labelled.
> 5. A layer **never guesses how much** more context it needs — guessing an amount is the un-knowledge-based move this
>    contract forbids. It knows *what* it needs, not how far away that is, so it **extends incrementally and stops on a
>    principled condition**; the amount is **discovered, not chosen**.
> 6. The principled stop is **convergence**: extend until the layer's **in-selection output stops changing** with
>    further context. This is self-validating — you have enough context exactly when adding more does not change the
>    answer — and it is what keeps the result independent of the extension step size (the equivalence invariant, §4). In
>    practice a layer uses a **domain proxy that *implies* convergence** rather than re-checking its whole output each
>    step (Architectural Layer 3 reach-back: *"a settled, stable prevailing key is in view"* — once a confident earlier
>    key is established, the change-cost/decay means reaching further back will not move the selection's leading-edge
>    key). The proxy is validated **once, in design**, to imply convergence.

**In plain words.** A layer knows what evidence it needs but not how far away it is, so it never picks an amount. It extends the loaded span incrementally and stops on a principled condition: convergence, meaning its in-selection output stops changing as more context arrives. In practice it uses a domain proxy that implies convergence, and the proxy is validated once, at design time.

**Why.** The reason is stated with the rule (cowork_bounded_context_design.md:61-68): guessing an amount is the un-knowledge-based move the contract exists to forbid, and convergence is self-validating - you have enough context exactly when adding more does not change the answer - which is also what makes the result independent of the extension step size.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:57-69`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; the rule is items 5 and 6 of the bounded-context contract at :57-69. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-262 — The extension increment is chosen by the requesting layer, not by the layer that supplies the notes

>    layer; it is not fixed and not Architectural Layer 1's to decide.** Architectural Layer 1 is domain-blind, and no
>    single size fits every layer (Architectural Layer 3 probes at phrase/measure scale, Architectural Layer 4 at
>    harmony/slice scale), so the requester sets it to **its own natural inference scale** — the smallest step that
>    could plausibly change its output (knowledge, not a guess). It is an **efficiency knob only**: a larger increment
>    means fewer round-trips (and perhaps a slightly larger final loaded span), never a different answer, because
>    convergence (item 6) fixes the result. Mechanically this is forced — the requester owns the *extend → re-infer →
>    re-check* loop, and Architectural Layer 1's *extend* executes **exactly the one requested step and never evaluates
>    convergence** (that would be inference, which it does not do), so the increment can only be a per-call parameter
>    from the requester.

**In plain words.** How much music to load per extension step is set by the layer asking for it, in its own natural inference scale, because the note supplier is domain-blind and no single step size fits every layer. The increment is an efficiency knob only - a larger step means fewer round trips, never a different answer, because convergence fixes the result.

**Why.** Two reasons are stated with the rule (cowork_bounded_context_design.md:74-81): the supplying layer holds no analysis knowledge, so it cannot know the smallest step that could plausibly change an answer; and it is mechanically forced anyway, because the supplier executes exactly one requested step and never evaluates convergence, which would be inference it does not do.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:73-81`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; item 8 of the bounded-context contract at :73-81. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-263 — A refused or truncated extension is marked on the output, never silently absorbed

> 10. **Denial/truncation is honest, never silent (merged 2026-07-02).** When an extension is refused (hard bound,
>    score boundary at a *selection* edge with the stop condition unmet, or a driver-level safety cap), the layer
>    proceeds on truncated evidence AND the affected output carries **`clipped-by-selection-edge`** provenance
>    (+ `cue-denied` where a request was actually refused) — a truncated result is never presented as a complete one.
>    Layer 6 (when resumed) surfaces these marks and the `extension-cue` tag (its §5.1 amendment); it never acts on them.

**In plain words.** When an extension is refused - by a hard bound, by the score's own start or end at a selection edge with the stop condition unmet, or by a safety cap - the layer proceeds on truncated evidence AND the affected output carries provenance saying so. A truncated result is never presented as a complete one.

**Why.** It is principle #12 (no information loss) applied to the extension protocol: the fact that a layer wanted more evidence and could not get it is itself information a consumer needs, and dropping it would make a truncated reading indistinguishable from a fully-evidenced one.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:82-86`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; item 10 of the bounded-context contract at :82-86, marked '(merged 2026-07-02)' from the killed duplicate contract document. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-264 — Extension is an optimisation of load-more-then-rerun: any sequence of extensions equals one fresh run

> - **Equivalence invariant (the correctness guard).** The result after **any** sequence of extensions must equal a
>   **single fresh run over the final loaded span** — extension is an optimisation of *"load more, then run from
>   scratch,"* never a different computation. In practice the forward cascade is **bounded**: the new context changes
>   inference only where it actually reaches (a carried-in key affects the leading-edge slices and decays inward), so
>   only the affected slices re-infer — the same locality that makes the stop condition terminate, and which composes
>   with the existing *"re-analyse a sub-range"* capability.

**In plain words.** The result after any sequence of extensions must equal a single fresh run over the final loaded span. Extension exists to avoid recomputing from scratch; it is never allowed to be a different computation, and the analysis must not depend on how many steps reached a given span.

**Why.** Stated as the correctness guard for the whole protocol: without it, incremental extension could silently produce an answer no single run would produce, and the result would depend on the extension granularity rather than on the music. It is the same guarantee re-slice equivalence gives Layer 2 (register entry D-050).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:121-126`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; the equivalence invariant at :121-126, with the step-size independence obligation restated as a required test at :202-204. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-265 — Asking a lower layer for more notes is a data-supply call, not a backward inference edge

> - **The re-inference cascade IS the forward-only contract, not an exception to it.** The extension **request** is a
>   data-supply call **down** to Architectural Layer 1 (a higher layer using a lower layer's service — control, not
>   inference). The new notes and every re-inference then flow **forward** (Architectural Layer 1 → 2 → 3 → …), exactly
>   as on a first run. **Inference never flows backward** — a later layer re-inferring cannot alter an earlier layer's
>   result. So an extension is precisely *"ask down for more raw material, then infer forward again,"* with no backward
>   inference edge anywhere; this is what makes it consistent with the project's forward-only analysis contract.

**In plain words.** An extension request travels down the stack to the note supplier, and the new notes and every re-inference then flow forward through the layers exactly as on a first run. Inference never flows backward: a later layer re-inferring cannot alter an earlier layer's result. So extension is consistent with the forward-only contract rather than an exception to it.

**Why.** The distinction is drawn in the rule itself (cowork_bounded_context_design.md:115-118): a higher layer using a lower layer's service is control, not inference. It is recorded precisely because a reader could otherwise read the forward-only contract as forbidding extension, which would block the whole bounded-context design.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:115-120`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; stated at :115-120 and again as an architecture decision at :188-189 ('recorded so the forward-only contract is not read as forbidding extension'). Bears on register entry D-025, the forward-only rule with two scoped escapes. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-266 — Layer 6 is prohibited until the bounded-context design is coded and regression-tested for Layers 1 to 5

> ## §11 Acceptance (the L6 gate — user directive 2026-07-02)
>
> 1. This design **ratified** (it was never signed; sign-off is now the first step).
> 2. **Coded, L1–L5:** L1 build-selection + extend seam (interim rebuild allowed, §8); L2 re-slice-on-extend (done);
>    L3 reach-back activated as this design's request (from gated-off) ; L4's request-or-truncate path (uncoded today,

**In plain words.** The grouping layer's track does not resume until this cross-layer design is ratified, implemented across Layers 1 to 5, and regression-tested against the listed acceptance conditions - including the equivalence invariant, step-size independence, denial provenance, termination, and byte-identity of the whole-score degenerate case against the corpus gate. RULING (user, 2026-08-02): the gate itself STANDS and transfers to the current architecture; the design's §11 acceptance list is DEPRECATED — not to be used, not even relevant — and the acceptance conditions are restated against the current stack in the phase-3 plan (with OI-259).

**Why.** The reason is the design's own opening argument (cowork_bounded_context_design.md:14-16): the whole-score assumption is foundational, so building more layers on it bakes it deeper and unwinding it afterward is a cross-cutting, expensive retrofit. Gating the next layer on the contract being real, not merely written, is what stops that.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:213-217`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3-4 records it in the status banner as 'THE GATE (user directive, same day)', and the acceptance list is the numbered section at :213-223. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, option (b) with the acceptance list explicitly deprecated) — the dated annotation at the home records it; the restatement obligation joins the phase-3 plan via OI-259.

### D-267 — There are exactly two admissible confidence classes, and no layer may claim a calibrated probability until one is fitted

> Every published confidence declares exactly one **class**:
>
> - **Class M — decision margin.** "How much better is the chosen reading than the best *different* reading, under this
>   layer's own scoring?" A margin is a **rank statement**, not a probability. Raw margins are unbounded and
>   scorer-scale-dependent, so a Class-M confidence is published only **squashed to [0,1]** by a fixed monotone map
>   (the map's constants are precision-phase; the map itself is declared per layer). Class M is what every layer can
>   compute today.
> - **Class P — calibrated probability.** "With what empirical frequency is a decision at this confidence correct,
>   measured against ground truth?" Class P is the **Stage-5 target**: a fitted reliability map per (layer × decision
>   type) converts the Class-M value into Class P. Until fitted, no layer may claim Class P.

**In plain words.** Every published confidence declares one of two classes. A decision margin says how much better the chosen reading is than the best different one under that layer's own scoring - a rank statement, not a probability, published only after being squashed into the zero-to-one range. A calibrated probability says with what measured frequency a decision at this confidence is correct; it is the later target, and until its reliability map is fitted no layer may claim it.

**Why.** Stated with the contract (cowork_confidence_contract.md:14-21): the architecture's forward-override mechanism numerically compares confidences across layers, and those quantities were incommensurable by construction - one layer publishing a sequence margin, another a composite, another an unbounded additive score against a clamped comparison. Weight fitting cannot repair a comparison between quantities with undefined semantics; it would only bury the incoherence in fitted constants.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_confidence_contract.md:25-34`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_confidence_contract.md:3, status banner 'RATIFIED (user, 2026-07-02)'; the two classes at :25-34. The contract names its architecture home as the cross-cutting contracts section (:6), where register entry D-032 records the boundary rule this classification underpins. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-268 — A confidence attaches to a named decision, is compared only within its class and a declared frame, and keeps its identity downstream

> **Rules of use:**
> - **U1.** A confidence attaches to a **named decision** (key-of-slice, chord-of-slice, membership-of-note,
>   cadence-vote, boundary-strength, function-of-unit) — never to "the layer" in general.
> - **U2.** At a **layer boundary** (any value another layer may read), a confidence is **[0,1], class-declared, with
>   its decision named**. Unbounded internal scores are permitted *inside* a layer but must be squashed at the boundary.
> - **U3.** A consumer may compare two confidences **only within one class and one declared frame** (§4). Treating a
>   Class-M margin as a probability (or comparing two Class-M values produced by different scorers without a declared
>   conversion) is a contract violation.
> - **U4. Provenance.** A carried-forward confidence keeps its (source layer, decision, class) identity; no silent
>   re-interpretation downstream.
> - **U5. Abstention.** The "uncertain" mark ≡ the decision's confidence is below the layer's declared bar (a
>   precision-phase constant). Abstention semantics are therefore uniform: *low confidence in the declared class*, not
>   a separate ad-hoc judgment.

**In plain words.** Five rules of use. A confidence belongs to a named decision, never to a layer in general. At a layer boundary it is zero-to-one, class-declared and decision-named. A consumer may compare two confidences only within one class and one declared comparison frame. A carried-forward confidence keeps its source layer, decision and class, with no silent reinterpretation. An abstention means the decision's confidence is below that layer's declared bar - the same meaning everywhere, not a separate ad-hoc judgment.

**Why.** Each rule names the failure it prevents (cowork_confidence_contract.md:41-48): treating a margin as a probability, comparing two margins from different scorers without a declared conversion, and re-interpreting a carried confidence downstream are all named as contract violations. The abstention rule exists so that 'uncertain' means one thing across layers rather than being re-invented per layer.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_confidence_contract.md:36-48`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_confidence_contract.md:3, status banner 'RATIFIED (user, 2026-07-02)'; rules U1 to U5 at :36-48. Rule U2 is the one already registered, as D-032, at its ARCHITECTURE.md home; U1, U3, U4 and U5 were not in the register. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-269 — The frame table is the one home of the override arithmetic; a new override site declares its frame before it is built

> **New frames require declaration here.** Any future override site (e.g. the A-4 cadence-less confirmation channels;
> the recognition consumer's schema-contradiction override, `cowork_progression_schema_design.md` §2) must add its
> frame row to this section before build — an undeclared cross-layer comparison is a contract violation.

**In plain words.** Every place where one layer's contradiction strength is compared against another layer's confidence is a declared frame - a triple of incumbent confidence, contradiction measure, and the conversion that makes them comparable - and all of them live in one section. Any future override site must add its frame row there before it is built; an undeclared cross-layer comparison is a contract violation.

**Why.** It is principle #6 (one path per concern) applied to the override arithmetic: the contract exists because the same comparison was being re-stated with different semantics at each site. Stating it once, with each instance's conversion declared, is what makes the threshold interpretable rather than an arbitrary scale factor.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_confidence_contract.md:83-85`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_confidence_contract.md:3, status banner 'RATIFIED (user, 2026-07-02)'; the rule at :83-85, over the frame definition and the two built instances at :63-81. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-278 — The joint key-and-chord step is SHELVED - measured not to pay

> precision gain is measured read-only **before** it is built, exactly as the joint step was. **The joint key↔chord
> step is SHELVED — measured NOT to pay** (arc #12: net +0.05–0.16 pp over ~6200 regions, harm 75–90 % of
> correction, oracle ceiling +0.6 pp, coupled-minority net ~0, fire-rate only 1.4 % — the carried alternative
> keys are diatonic-collection siblings so the chord is almost always key-stable). It **drops off the Stage-3
> build inventory.** The #12 reconciliation (no loss): the key alternatives ARE carried (the key discovery is not
> discarded); the chord under an alternative key is **never computed** in this path (so nothing computed is
> discarded), and the measurement shows the ~1.4 % where it would differ is 50/50 noise — choosing not to compute
> a *measured-worthless* possibility is an evidence-based decision, not information loss. **Distinction:** this
> gate applies to **precision claims** ("will building X make analysis more correct?" — measure first); the
> **structural refactors** (decoder-replaces-tangle, the migrations) are justified by cleanliness and verified

**In plain words.** The separate joint key-and-chord decision was measured before being built and does not pay: about a tenth of a percentage point net over roughly 6200 stretches, with harm at three quarters to nine tenths of the correction, an oracle ceiling under a percentage point, and a firing rate of 1.4 per cent. The cause is that the carried alternative keys are siblings within one collection, so the chord is almost always stable across them. It drops off the build inventory. DEPRECATION MADE EXPLICIT (user, 2026-08-02): the shelved step's subject is deprecated legacy-era machinery, to be entirely discarded with the legacy path at the retirement map; the shelving binds that class only and does not bear on the joint estimator (D-001), a different mechanism class.

**Why.** The measurement is stated with the shelving, and so is the principle #12 reconciliation: the key alternatives ARE carried, so the key discovery is not discarded; the chord under an alternative key is never computed in this path, so nothing computed is discarded; and the measured 1.4 per cent where it would differ is even-odds noise. Choosing not to compute a measured-worthless possibility is an evidence-based decision, not information loss.

**Status.** SHELVED WITH EVIDENCE · decided 2026-07-07 · ratified by user

**Home.** `cowork_engage_arc_plan.md:103-112`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_engage_arc_plan.md:3 records the user's ratification of this plan, dated 2026-07-07; the shelving at :103-112, with the measurement cited to its report and the no-information-loss reconciliation stated in place. Found by the phase-1d enumeration wave, 2026-08-02 - the class this audit exists for: a shelving with evidence, recorded only in a design document. ★ RATIFIED (user, 2026-08-02, option (a) with the deprecation made extremely clear) — the scoping annotation is at the home (the dated annotation beneath the shelving); the subject is legacy-era, will be entirely discarded at the OI-180 retirement map, and the shelving does not bear on D-001.

### D-282 — Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy

> - **Oracle/tier metric, never a bare proxy** (BIR rewards wrong-root=bass). Make the dual metric standing.

**In plain words.** Never grade the analysis on the bare bass-is-root number, which rewards a wrong chord root that happens to be the bass; use the oracle-checked, tiered measurement. Its content became standing through the robust-unit regression stop and the two-tier class policy.

**Why.** The stated reason is in the finding itself (the bare proxy rewards wrong-root-equals-bass); the successors carry their own measured defenses (D-115: the batch proxy under-counted the true per-onset error ~15-56x; D-191: decidable vs undecidable roots graded differently).

**Status.** SUPERSEDED BY D-115 and D-191 · date not stated · ratifier not stated

**Home.** `cowork_architecture_reassessment.md:97`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Stated 2026-06-20 in cowork_architecture_reassessment.md §4 ('Meta-findings to institutionalize'); put to the user in §5 ('Ratify: …') with NO recorded answer (open_items/OI-270.md, the phase-1d wave's remainder). ★ RULED by the user 2026-08-02 (the OI-270 split, all four recommendations adopted): SUPERSEDED BY the named later ratified decisions — the governing status derives from the record's dates and explicitness, not from resolving the original statement's ambiguity. The second-partition read of the archives is instructed to flag anything refining these.

### D-286 — Whole-score interactive analysis was SHELVED WITH EVIDENCE; the bounded window is the ratified reading

>   self-consistent. **Decision (Cowork): bounded-window cache (CC's recommendation);
>   whole-score SHELVED with evidence; P3↔P1 consistency PARKED as a product/Stage-5
>   question; D-P4/D-BRIDGE closure rolled back to the 2.4 contract; the A/B data
>   promoted to committed Stage-5 evidence.** Revision instruction:

**In plain words.** At Stage 3.1b a measured A/B put a whole-score interactive analysis against a bounded-window one and the window won against the published annotations; the whole-score variant was withdrawn against that measurement and the bounded window adopted. The question of whether a per-note answer must match the whole-piece answer was parked, not settled.

**Why.** Measured: the A/B changed 32-40 % of ticks on contrapuntal music and the published annotations preferred the window path 59/41 overall and 65/35 on Mozart (`docs/p3_granularity_ab_3_1b.md`, the committed evidence). The shelving is the founding case of the decision-conformance audit: it lived only in an archive outside the session-start read, and a later build specified whole-score interactive analysis without meeting it (`OPEN_ITEMS.md` OI-210, OI-212).

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Home.** `cowork_handoff_archive.md:2964`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in the 2026-06-12 Stage-3.1b block of `cowork_handoff_archive.md` and in `docs/p3_granularity_ab_3_1b.md`. NOT superseded by any later ruling: `OPEN_ITEMS.md` OI-210 records that the extent question was then PARKED pending the granularity-robust metric (which has existed since 2026-07-06) and is now implemented as whole-piece by dispatch specification with no ruling — so the shelving stands on the record and the implementation departs from it. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-288 — Beam widening is SHELVED - a wider search cannot fix the failure class it was proposed for

> - **⚠ STRATEGIC PIVOT (2026-06-13, Cowork-verified + user-directed): beam-widening
>   SHELVED; the back half of the roadmap is being re-grounded on measured precision
>   headroom.** The 3.2 design's §3 derivation (Cowork-verified against the independent

**In plain words.** Searching more candidate readings in parallel was withdrawn. The failure it was meant to fix is not a search failure: the wrong reading is the highest-scoring one, so looking at more readings finds the same wrong answer. Only changing how readings are scored, or cutting the music differently, can fix it.

**Why.** Derived, then cross-checked: the design's own arithmetic (verified against the independent earlier figures - AbMaj7 2.55 over 2.33, F#7 2.85 over 2.825) shows the wrong continued-root path is the genuine global optimum, which a decode finds exactly as a greedy walk does. The consequence recorded with it is that a wider beam is substitutable by the width-one beam for every other motivated use, so nothing else justified building it.

**Status.** LIVE · decided 2026-06-13 · ratified by the user (directive), on Cowork's verification

**Home.** `cowork_handoff_archive.md:3029`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-13 strategic-pivot block); `docs/beam_widening_design.md` was banner-shelved and retained for its derivation. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-289 — Meta-principle: precision lives in the evidence and the functional labelling, not in the search

>   correct key never rank-2 in 51.6% of S2) — unrecoverable by any path. **SECOND
>   falsified structural fix → META-PRINCIPLE recorded in roadmap: precision lives in
>   emission + functional labeling, NOT search/path.** The HMM path is the least valuable
>   part of Stage 4 (~10%); KeyArea spans + the key-EMISSION fix are what deliver.

**In plain words.** Three independent investigations converged on one rule: accuracy is gained by improving what evidence each reading is judged on and by labelling harmonic function better - not by searching harder over the readings already on the table.

**Why.** Converged from three separate falsified structural fixes, each measured: the wider beam (the wrong reading is the top-scoring one), the key path (it reaches about 10 % of the key errors because the correct key is usually not even ranked second), and the algorithmic ground-truth filter. Recorded in `docs/implementation_roadmap.md` as a meta-principle.

**Status.** LIVE · decided 2026-06-13 · ratifier not stated

**Home.** `cowork_handoff_archive.md:3082`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-13 Stage-4 design-investigation block) and `docs/implementation_roadmap.md`. ★ FLAGGED against the OI-270 meta-findings (D-282…D-285): this is an EARLIER and independently-derived statement of the same insight as D-284 (selection and competition are saturated). It does not change D-284's ruled status; it dates and corroborates it. It was itself later RECONCILED rather than overturned: `cowork_handoff_archive.md:3920-3921` records that the joint decode's value is broad-evidence integration, NOT search — "search is about zero" having been measured over a FIXED NARROW evidence surface. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-293 — Fitted values are fitted per IDIOM, never for a user preset; presets are regression surfaces and delivery carriers

> **★ NEW USER MANDATE (recorded as design constraint 4c): OPTIMIZE FOR IDIOMS ONLY — never for the current
> user presets;** presets = regression surfaces + delivery carriers; ONE fit per idiom; the end-user-facing
> preset question is a separate later product decision. **★ CHECKPOINT P0 RATIFIED (user): 61 tunable / 17

**In plain words.** Numbers are fitted once per musical idiom - a body of repertoire that shares a practice - and never tuned to match one of the program's named presets. A preset is a way of delivering a set of values and a surface to check for regressions; which presets a user should see is a separate product question, decided later.

**Why.** A user mandate, recorded as constraint 4c of the fitting design. Its consequence is stated with it: ONE fit per idiom, and the Bach fit is an idiom fit delivered through two carriers.

**Status.** LIVE · date not stated · ratified by the user

**Home.** `cowork_handoff_archive.md:2363`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the Stage-5 fitter block) as design constraint 4c of `cowork_stage5_fitter_design.md`. Consistent with, and earlier than, D-003 (inference is preset-independent; presets are presentation concerns) — this states the FITTING side of the same separation. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-294 — The only ground truth is the human annotation; the algorithmic analysis is a filter, and no self-annotation ever enters a measurement

>   Ground-truth verdict (sharpened by user mandate 2026-06-10): **the ONLY ground truth
>   is the human annotation (WiR/DCML); music21 is NOT ground truth** — it is an
>   algorithmic noise filter, and the 13/7 "genuine" counts are a music21-filtered LOWER
>   BOUND on human-adjudicated errors (cases where music21 sides with us against DCML are
>   excluded by an algorithm's opinion). Never describe the gate as "ground-truth
>   agreement." Stage 5 must evaluate a DCML-only gate variant (roadmap 5.2). No
>   self-annotations in any gate; catalog/goldens correctly used as regression pins only.

**In plain words.** Accuracy is measured against published human analyses only. The second, computer-generated analysis is a noise filter, not a standard of correctness, so a measurement that uses it reports a lower bound rather than an agreement rate - and must never be described as agreement with ground truth. Our own outputs and our own test fixtures are never used as a standard of correctness; they pin behaviour against change and nothing more.

**Why.** A user mandate, sharpening what counts as ground truth. Its reason is stated with it: where the algorithmic analysis sides with us against the human annotator, the case is excluded by an algorithm's opinion, so the count understates the human-adjudicated error. The mandate produced the requirement for a human-annotation-only measurement, which is the unit now governing (D-115).

**Status.** LIVE · decided 2026-06-10 · ratified by the user

**Home.** `cowork_handoff_archive.md:2844`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the corpus-audit block, as the ground-truth verdict). The human-annotation-only requirement it names was delivered as the granularity-robust unit (D-115), whose own text carries the clause "music21 is NOT ground truth"; the two further clauses — never describe a measurement as ground-truth agreement, and no self-annotation in any measurement — are recorded ONLY here. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-297 — Correction of record: never computing a possibility is not information loss; only discarding a computed one is

> **★ #12 CORRECTION (recorded — the earlier "recomputable" framing was WRONG):** on the shelved joint step,
> the chord under an alternative key is **NEVER COMPUTED** in this path — so nothing computed is discarded (no
> #12 violation). The key alternatives ARE carried (the key discovery is preserved). Not computing a
> *measured-worthless* possibility (the ~1.4 % where it differs is 50/50 noise) is an **evidence-based
> decision, not information loss** — you cannot lose what you never had. ("Recompute a discarded thing" WOULD
> be a #12 violation; that is not what happens here.)

**In plain words.** The no-information-loss principle forbids throwing away something the analysis has worked out. It does not require working out everything that could be worked out. Deciding, on measured evidence, not to compute a possibility is an ordinary design decision - you cannot lose what you never had.

**Why.** Recorded as an explicit correction of an earlier, wrong framing that had called the same situation a principle violation. The worked case is the shelved joint key-and-chord step: the chord under an alternative key is never computed on that path, the key alternatives themselves ARE carried, and the roughly 1.4 % of cases where the alternative would differ were measured to be an even split, i.e. noise.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Home.** `cowork_handoff_archive.md:1532`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-07-07 entry-point block) as a dated correction. It scopes D-099 / principle #12 and is recorded nowhere that a reader of #12 would find. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-313 — A confidence map is monotone or it is not fitted — a non-monotone curve is an upstream finding, not a mapping target

> **D-8 Calibration maps are monotone or deferred.** A non-monotone empirical curve (L5 combinedBoundary) is
> an upstream finding, not a mapping target — fitting a non-monotone map would launder an inference defect
> into the confidence semantics. (Contract R4/R5 monotonicity carries this.)

**In plain words.** Turning a layer's internal confidence number into a statement about how often it is right is only done when a higher number really does mean more often right. Where the measured curve goes the wrong way in places, that is reported as a fault in the layer, not smoothed over by the map.

**Why.** Stated with the rule: fitting a non-monotone map would launder an inference defect into the confidence semantics — the map would make a mis-ordered confidence read as a well-ordered probability. The confidence contract's monotonicity rules carry the same requirement.

**Status.** LIVE · decided 2026-07-04 · ratified by the user

**Home.** `cowork_stage5_fitter_design.md:673`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_stage5_fitter_design.md` (SIGNED, user, 2026-07-04) as the eighth of its numbered architecture decisions, and applied in the same document at §4.5: the one measured non-monotone row was deferred and declared rather than mapped. Found by the phase-1f final-partition wave, 2026-08-02, reading `cowork_stage5_fitter_design.md` in full (SIGNED, user, 2026-07-04). NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue).

### D-339 — A confident earlier decision can be overturned by decisive later evidence, through ONE confidence-weighted forward-recompute mechanism — architecture-wide

> - **D7 — A confident earlier inference can be overturned by decisive later evidence, via one general
>   confidence-weighted forward-recompute mechanism (decided, user, 2026-06-26; see §8).** Every later layer brings its
>   independent evidence to bear on every earlier inference; agreement reinforces, and a *confident* commit is overturned
>   only when the contradicting evidence crosses a threshold scaled to the earlier layer's confidence — firing a localized,
>   forward, convergence-bounded recompute. The two channels this layer needs (the modulation recompute §5.4 and the
>   fine-grain chord override §5.5/§10) are **instances** of this one mechanism. *Rejected:* (a) treating each override as a
>   bespoke one-off (it hides that they are the same mechanism and makes generalizing a rewrite); (b) a hard
>   confidence-gate that locks confident commits permanently (a confidently-wrong commit must stay recoverable — this is
>   what gives the precision phase tunable per-channel thresholds); (c) a backward re-derivation or full joint cross-layer
>   search (measured inert — the gain is soft-evidence quality carried forward, not cycling). The mechanism and its
>   direction are fixed here; the thresholds are precision-phase. **This decision is architecture-wide** (it generalizes the
>   forward-only control-flow contract for all layers, not just this one) — to be promoted into the target-architecture

**In plain words.** Every later stage brings its own evidence to bear on every earlier decision. Agreement strengthens it; disagreement overturns it only when the contradicting evidence is strong enough, and how strong depends on how sure the earlier stage was. When that happens the affected passage is re-read forward once, and the overturned decision is then closed for the rest of the pass.

**Why.** Three alternatives are rejected with reasons: treating each override as a one-off hides that they are the same mechanism; a hard gate that locks confident decisions permanently makes a confidently-wrong decision unrecoverable; and a backward re-derivation or full joint cross-layer search was measured inert, the gain being soft-evidence quality carried forward rather than cycling. Confidence is what sets the bar to overturn, which is what gives the later calibration phase a tunable lever instead of an absolute veto.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:637-648`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1g queue — the ratification is of the RULE itself; home and provenance are bookkeeping).

### D-377 — The forbidden back-edge, stated concretely: a chord decision may NOT write into the committed tonality and re-run the tonality decode — a coupled decision is OWNED by its own bounded box, never patched backward

> **A placement that WOULD violate acyclicity** (flagged so the build does not drift there): letting L4's chord
> decision write back into L3's *committed* region key as a side effect and then re-running L3's whole-score
> Viterbi — that is the back-edge #7 forbids. The design avoids it by making the joint step the **owner** of the
> coupled (key,chord) decision (it does the re-rank locally, in its own bounded beam) rather than a **feedback
> patch** on L3.

**In plain words.** There is one shape that would break the rule against a later stage feeding an earlier one, and it is named so that no build drifts into it: letting the chord decision alter the tonality that has already been committed, and then re-running the whole tonality search over the piece. The permitted shape is the opposite — whatever owns the coupled decision makes it locally, inside its own bounded search, and publishes one settled answer forward. A new decision box, never a feedback patch on an existing stage.

**Why.** It is the concrete form of the forward-only control-flow contract the architecture already carries, written down at the one place a design could plausibly have violated it. The record states why the permitted shape is safe: the coupled box reads only what the earlier stage has already emitted and carried — the ranked alternatives it published as its exclusion tail — and drives the later decoder forward as a pure function, so neither direction is a cycle.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Home.** `cowork_joint_key_chord_design.md:136-140`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_joint_key_chord_design.md` IN FULL. The step the document designs is shelved (**D-278**); this prohibition is not about that step — it is stated as what any placement must avoid, and is flagged in the record as written so the build does not drift there. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue.

