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

**Home.** `ARCHITECTURE.md:1015-1016`

**Provenance.** ARCHITECTURE.md:808 heading says '(ratified; full statements in cowork_target_architecture.md)'; the date and ratifier are not stated at this home

### D-023 — The atomic analysis unit is the constant-sonority slice, never the metric beat

> The atomic analysis unit is the **constant-sonority slice** (L2), never the metric beat

**In plain words.** The smallest thing analysed is a stretch during which exactly the same notes are sounding - not a beat of the bar.

**Why.** Same passage as D-022, ARCHITECTURE.md:810-814: the metric beat is not where harmony is well-defined; the constant-sonority slice is, and every coarser unit is derived from it.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:1016`

**Provenance.** ARCHITECTURE.md:808-815. The joint estimator's own unit is the ONSET event (jointdecoder.h:67), not this slice - see OPEN_ITEMS OI-228

### D-024 — The fact layers are style-agnostic; style lives only in calibration

> L1 (notes) and L2 (slicing) are **style-agnostic and
>   lossless** — they carry facts, never style. Style-specificity lives **only** in the *calibration* of the judgment
>   layers (their priors/weights), **never in structure**.

**In plain words.** Reading the notes and cutting the music into constant-sound stretches works the same for every kind of music. Whether a piece is Baroque or jazz can change only the numbers the judging layers use, never the shape of the code.

**Why.** Stated constraint, ARCHITECTURE.md:817-820: confining style to the calibration of the judgment layers sharpens §2.1 - not merely data-driven style, but style kept out of the layers that carry facts, so the fact surface cannot silently differ between styles.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:1022-1025`

**Provenance.** ARCHITECTURE.md:808 ratified banner; sharpens §2.1 (D-070)

### D-025 — Forward-only, with two scoped escapes

> The **ratified** architecture (user-ratified;
> `cowork_target_architecture.md` §2) is **forward-only**:

**In plain words.** Each stage was to pass its answer forward and never reach back. A confident earlier answer could be overturned only by re-running that one stretch forwards, and the one genuinely tangled key-versus-chord case got a narrow, gated exception.

**Why.** Measurement, ARCHITECTURE.md:787-790: the investigation measured the full joint cross-layer search INERT, and located the realisable gain in soft-evidence quality carried forward (calibrated confidence + ranked alternatives) rather than global cycling.

**Status.** SUPERSEDED BY D-001 · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:995-996`

**Provenance.** The 2026-07-17 governing decision (D-001) replaces the mechanism with ONE joint decode - the mechanism this block had ruled out. No supersession banner was added to §2.14 - see OPEN_ITEMS OI-234 ★ USER RULING 2026-08-02 (OI-234, reading 3): forward-only as the architecture ruling is SUPERSEDED BY D-001 (the 2026-07-17 joint decision, adopted 2026-07-26); the supersession now has a ruling naming it (was superseded-in-fact). The §2.14 scoping annotation records the ruling.

### D-026 — The global joint-lattice decode was measured inert (2026-06-29)

> The subsequent investigation
> **measured the full joint cross-layer search INERT**

**In plain words.** An earlier plan to search all the possibilities at once was tested and found to add nothing, so the effort was redirected into better evidence flowing forwards.

**Why.** The measurement itself (ARCHITECTURE.md:787-788). What the record does NOT state is how it was reconciled with the 2026-07-17 joint estimator, which is one - see open_items/OI-234.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:992-993`

**Provenance.** The joint estimator (D-001) is a global joint decode and is in production on both surfaces. The record does not state how this measurement was reconciled with the later ruling - see OPEN_ITEMS OI-234 ★ USER RULING 2026-08-02 (OI-234, reading 3): the finding STANDS FOR WHAT IT TESTED — cycling/re-ranking over the per-layer pipeline's carried candidate lists adds nothing, binding on that design class — and does NOT bear on the fitted semi-Markov joint decode (a different mechanism class). Returned to LIVE, scoped; the §2.14 annotation records the scoping (was superseded-in-fact).

### D-027 — Every layer emits ranked candidates plus a confidence, never a forced point estimate

> each layer is feed-forward and emits **ranked candidates + a confidence**, never a forced point estimate;

**In plain words.** No stage is allowed to report only its single best answer. It reports the runners-up too, with a measure of how clear-cut the choice was.

**Why.** Stated constraint, ARCHITECTURE.md:733-735: irrevocable point estimates block iteration and provisional results with confidence metadata enable it, so every layer's output must carry the alternatives and the confidence a later layer would need to overturn it.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:997`

**Provenance.** The mechanism around it (D-025) is superseded in fact, but the ranked-alternatives requirement is carried forward by the joint estimator's published candidate lists (D-006)

### D-028 — The span typology - every layer names the span it operates on; bare 'region' is banned

> "Region" unqualified is **banned** as
>   ambiguous; every layer names the span it operates on.

**In plain words.** The word 'region' on its own is forbidden, because it hides which kind of stretch is meant. Each stretch has its own name: the chord-span, the key-span, the punctuation-span and so on.

**Why.** Research citation, ARCHITECTURE.md:865 - the span typology follows the GTTM premise of independent structures (Lerdahl & Jackendoff); the ban on the bare word is because a 'region' is a FAMILY of spans and the unqualified word names none of them (:765, :786-787).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:1069-1070`

**Provenance.** ARCHITECTURE.md:833-850 records the rename CONFIRMED (user, 2026-07-02) and EXECUTED 2026-07-03 'propagated through every layer spec'. ARCHITECTURE.md itself still uses the banned word 216 times including section headings - see OPEN_ITEMS OI-233

### D-029 — The verifiability contract

> prefer what we can verify against ground truth (it is how we catch our own theory
>   errors); for sound theory we cannot verify against the current corpus, build it with an explicit
>   **alternative-confidence path** *and* an **"empirically-unvalidated" mark**, rather than refusing it

**In plain words.** Prefer what we can check against annotated music. Where the theory is sound but we have nothing to check it against, build it anyway - but mark it as unchecked and give it its own confidence path.

**Why.** Stated constraint, ARCHITECTURE.md:872-875: checking against ground truth is how we catch our own theory errors, and refusing sound theory we cannot yet check would forfeit the jazz and pop reach, where the theory exists and the corpus does not.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:1081-1083`

**Provenance.** ARCHITECTURE.md:808 ratified banner

### D-030 — Bounded context - cost scales with the working span, not the whole score

> The binding scale requirements: **(R1)** cost scales with the working span, not the whole
>   score; **(R2)**
>   re-analysis is incremental over the dirty span plus a bounded margin; **(R3)** the working span is **extensible**

**In plain words.** Analysis runs on what the user has selected. The work must grow with the size of that selection, not with the size of the piece; re-analysis after an edit must only redo the changed part; and a layer that needs more music asks for it rather than reading everything.

**Why.** Stated constraint, ARCHITECTURE.md:876-880: the analysis runs on the user's selection, so a layer needing more must request an append-only extension from Layer 1 carrying a stop condition and a hard bound. The three binding scale requirements R1-R3 are stated there; the detailed cross-layer specification is `cowork_bounded_context_design.md`.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:1087-1089`

**Provenance.** ARCHITECTURE.md:880-884 names cowork_bounded_context_design.md as the ONE detailed cross-layer spec and records the 2026-07-02 user directive making it 'the hard gate before L6'. DIRECTLY CONTRADICTED by D-011 (whole-score decode per query, no caching) - see OPEN_ITEMS OI-210/OI-212

### D-031 — Whole-score analysis is the degenerate case, not the design

> Whole-score analysis is the degenerate case (selection = score).

**In plain words.** Analysing the whole piece is what happens when the user has selected the whole piece. It is not the normal mode of operation.

**Why.** Same passage, ARCHITECTURE.md:880: whole-score analysis is what the bounded-context rule produces when the selection happens to be the whole score - a case of the rule, not an exception to it.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:1089`

**Provenance.** Same home as D-030. The record producer analyses the whole score regardless of the requested span (OI-212)

### D-032 — Every confidence crossing a layer boundary is in 0..1, class-declared, with its decision named

> **The cross-layer confidence contract — every confidence that crosses a layer boundary is bounded,
> class-declared, and named to its decision.** At a layer boundary — any value another layer may read — a
> confidence is **in [0,1], class-declared (a ranking margin or a calibrated probability), and stated

**In plain words.** Inside a stage, a confidence can be on any scale. The moment another stage can read it, it must be a 0-to-1 number, labelled with what kind of confidence it is and what decision it belongs to.

**Why.** Stated constraint, `cowork_confidence_contract.md:13-21` ('Why this contract exists'): the forward-override mechanism numerically compares a later layer's contradiction strength against an earlier layer's confidence, and those quantities are incommensurable by construction today - Layer 3 publishes a sequence margin, Layer 4 a three-part composite, Layer 5 an unbounded additive score. Fitting weights cannot repair a comparison between quantities with undefined semantics; it would bury the incoherence in fitted constants.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `ARCHITECTURE.md:1119-1121`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass, cc_instruction_spec_completion.md): the contract's own document `cowork_confidence_contract.md:39-40` (ratified there, user, 2026-07-02) remains the authoritative full statement; the rule is now stated in the cross-cutting contracts of the architecture document (§2.15), which is where a reader of the layers meets it. The stale 'ratification-gated' parenthetical in the §2.14 forward-override bullet of §2.15 is corrected in the same pass (OPEN_ITEMS OI-232, item 5). Contradicted by D-019 on the production record arm - see OPEN_ITEMS OI-231

### D-033 — Each layer owns one evidence-source-times-question contribution and uses all of L1's information

> each layer owns one *(evidence-source × question)*
>   contribution — stated as "owns the *[named evidence]* contribution to *X*", with what it does **not** own made
>   explicit — defers what needs later evidence (carried as ranked alternatives + an uncertain mark), and within its scope
>   uses *all* the information L1 carries losslessly (notated spelling, metric weight, voice).

**In plain words.** Each stage owns one contribution and says plainly what it does not own, handing unresolved cases forward as ranked options. Owning one contribution does not narrow what it may look at: within its scope it uses all the information the note reader carries - how the note is spelt, where it falls in the bar, and which voice it is in.

**Why.** Stated constraint, ARCHITECTURE.md:885-888: the single-responsibility half is what lets a layer say what it does NOT own, and the maximal-information half is what stops that ownership from being read as permission to ignore evidence Layer 1 already carries.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:1094-1097`

**Provenance.** ARCHITECTURE.md:808 ratified banner. The joint emission reads only struck notes (OI-228) and the shared tone surface is voice-blind (OI-74)

### D-034 — A new layer or axis is admitted only through three co-equal gates

> **A new layer or axis is admitted only when it clears three co-equal gates,
>   all required:**

**In plain words.** A new stage is added only if it carries one distinct responsibility, can be validated somehow, and buys something we can actually check. Carrying a distinct responsibility is enough on its own, even with no immediate accuracy gain.

**Why.** Stated constraint, ARCHITECTURE.md:902-909: gate (1) separation of concerns is a structural mandate sufficient on its own even at zero accuracy gain; gates (2) verifiability and (3) proportionality exist against the opposite error, and the record names the reminder - Contrapunctus is competitive with the state of the art with NO explicit grouping layer.

**Status.** LIVE · date not stated · ratified by user

**Home.** `ARCHITECTURE.md:1111-1112`

**Provenance.** ARCHITECTURE.md:902-909

### D-035 — The effort setting - every cost-driving choice is a setting, never a hardcoded constant

> **(a)** every cost-driving choice is an
> explicit *setting*, never a hardcoded constant; **(b)** every optional expensive refinement is a cleanly separable on/off
> stage.

**In plain words.** Anything that makes the analysis slower must be something the user or the caller can turn down, not a number baked into the code; and any expensive extra step must be separable so it can be switched off.

**Why.** Stated constraint, ARCHITECTURE.md:801-805: the effort dial is a calibration knob, not a structural one, so its two standing rules follow - every cost-driving choice is an explicit setting, and every optional expensive refinement is a cleanly separable stage.

**Status.** LIVE · decided 2026-06-29 · ratified by user

**Home.** `ARCHITECTURE.md:1008-1010`

**Provenance.** ARCHITECTURE.md:801-805. Not implemented: the effort setting does not exist and the decode's cost drivers (segment cap, key prune width) are compiled-in constants - tracked at OI-209/OI-210

### D-036 — Accumulating gates are a warning sign - add iteration, not more gates

> When a feedforward layer acquires many gates
> and guards to compensate for missing upstream feedback, that is a symptom of missing
> iteration — not a sign that the layer needs more gates.

**In plain words.** If a stage keeps needing new special cases, the problem is that it is missing information from elsewhere. Adding another special case makes it worse.

**Why.** Stated constraint, ARCHITECTURE.md:709-713: each gate is a heuristic patch on a structural limitation, so a rising gate count is a symptom of missing iteration rather than an argument for more gates.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:914-916`

**Provenance.** ARCHITECTURE.md:709-713; restated as an ongoing concern at :2131-2136

### D-099 — Negative evidence is information - a ruled-out possibility is carried, not dropped

> **Negative evidence is information — a ruled-out reading is carried, not dropped.** A layer that
> eliminates a reading publishes the elimination rather than discarding it: the ruled-out reading is
> carried on the output surface at low confidence, unless the elimination is recomputable from what that

**In plain words.** Knowing that something is not the case is itself useful. A reading that has been ruled out is kept at low confidence rather than thrown away, unless we could work out the exclusion again from what we did keep.

**Why.** Stated constraint, `CLAUDE.md` #12: a ruled-out possibility is evidence - finding by exclusion - so it is carried at low confidence unless the exclusion is recomputable from what is kept.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `ARCHITECTURE.md:1135-1137`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): CLAUDE.md guiding principle #12, ratified by the user 2026-07-06, remains the standing principle; the layer-facing rule is now stated in the cross-cutting analysis contracts it governs. OPEN_ITEMS OI-237 closes on this move

### D-100 — Every derived fact is published exactly once, on the producing layer's output surface

> **Every derived analytical fact is published exactly once, on the producing layer's output surface;
> consumers read it and never re-derive it.** For **evidence-class** facts — hints a later design could

**In plain words.** Whatever a stage works out, it publishes on its own output surface; every later stage reads that instead of working it out again. Facts that are hints a later stage might one day use are published broadly even when nothing reads them yet, each carrying whether it has been established, because a consumer may not rely on an unestablished fact. What to do with a fact nobody reads is decided case by case: keep it with a named future reader stated, or remove it - and a reader outside the analysis counts.

**Why.** Stated constraint, `CLAUDE.md` fact-publication corollary, with its evidence named there: `cowork_siloed_facts_audit.md` found 17 instances of facts being re-derived rather than read. The 2026-07-12 amendment's own recorded reason is the user's: a visible spread of published evidence lets a future design RECOGNIZE facts it would never have thought to ask for.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `ARCHITECTURE.md:1152-1153`

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

**Why.** Stated constraint, CLAUDE.md:461-463: the pitch-class analyzer is spelling-blind and cannot pick the spelling-correct rotation of a symmetric chord, so counting a rotation flip as a regression would be counting a coin-flip. Measurement bounding the split: on the robust unit the decidable-root class is about 96.5 % of root-fail time (CLAUDE.md:428-431), so the hard stop governs almost all of it. Founding evidence, verified at the score against music21 ground truth: bwv272@4320, bwv289@20160, bwv291@17760, bwv387@10560 (CLAUDE.md:477-480).

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Home.** `CLAUDE.md:776`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:443-486, block (B), carried over unchanged to the robust unit at R10-b. Full provenance `cowork_gate_policy_amendment.md`. The four guardrails that make the tracked class conditional - verified at the score per case, default to the barred class on any doubt, the barred class non-increasing, case identities recorded - are at CLAUDE.md:464-473.

### D-210 — An exotic mode is graded against its parent collection's minor key, not its own tonic triad

> **An exotic mode is graded against its PARENT COLLECTION's minor key, not against its own tonic
> triad** (user-ruled 2026-07-13, OI-132; landed `800f1a12bf`). When our analysis emits one of the five
> dominant-family exotic modes, grading reduces it to the minor key of the collection it belongs to — an

**In plain words.** When the analysis emits one of the five dominant-family exotic modes, grading reduces it to the MINOR key of the collection it belongs to - an emitted C-sharp Phrygian dominant is graded as F-sharp minor, the key it is the dominant of - rather than to the key its own tonic triad would name.

**Why.** Measurement, CLAUDE.md:359-364: on the affected duration the parent-collection reading agrees with the published annotators on 67 % of the local key column, and the tonic-triad reading on 0 %. The consolidation moved only the key columns - root, Roman numeral, every root-failing run set and the hard-stop duration were byte-identical, run-difference +0/-0 on all presets.

**Status.** LIVE · decided 2026-07-13 · ratified by user

**Home.** `CLAUDE.md:639-641`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:239 (OI-132), ruled by the user 2026-07-13 and landed at 800f1a12bf. The adjudication probe is `cc_mode_grading_adjudication_probe_report.md`; the re-baseline record is `cc_key_grading_and_calibration_rebaseline_report.md`. It is implemented in ONE shared reduction, `compare_rn._our_key_tonic`, onto which the second key parser was folded (#6). OPEN_ITEMS OI-240 closes on this move

### D-211 — Key agreement is reported against both the global home key and the local key

> **Key agreement is reported against BOTH the global home key and the local key** (user-ratified
> 2026-07-12, OI-143; adopted `d9b52ba969`). Both columns are carried everywhere the key column appears;
> neither replaces the other. *Why:* measured — the local percentage is lower than the home percentage, and that

**In plain words.** There are two defensible questions about a key reading - does it match the key the piece is in, and does it match the key this passage is in - and the record carries both numbers everywhere the key column appears, rather than choosing one.

**Why.** Measurement, OPEN_ITEMS.md:253: the local figure is lower than the home figure, which is itself the finding - the analyzer tracks the tonal home more faithfully than it tracks momentary tonicizations - so keeping only one column would have hidden a real property of the system.

**Status.** LIVE · decided 2026-07-12 · ratified by user

**Home.** `CLAUDE.md:649-651`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:270 (OI-143), adopted at d9b52ba969. The current values are in the CLAUDE.md gate block (A): key-agree against the home key 56.14 %, against the local key 78.42 %. OPEN_ITEMS OI-240 closes on this move

### D-212 — The regression stop is abstain-aware: an abstention counts as disagreement on root

> **The stop is ABSTAIN-AWARE: on the root axis an abstention counts as a DISAGREEMENT** (ruled and
> mechanically enforced 2026-07-12, OI-33). A cell where our analysis carries no root pitch class is
> scored as a root disagreement; on the key axis abstained cells are instead **excluded from the

**In plain words.** If the analysis declines to name a chord root, that counts as getting it wrong, so declining more often can never look like improving. On the key axis the declined cells are excluded from the percentage instead, and a rise in declining trips a flag in the comparison tool.

**Why.** Stated constraint, OPEN_ITEMS.md:200: the metric is abstention-reducible - without the convention, a change that made the system decline more would raise the agreement figure without analysing anything better - and the convention was owed before any abstaining path could be gated on the stop at all.

**Status.** LIVE · decided 2026-07-12 · ratified by user

**Home.** `CLAUDE.md:654-656`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:217 (OI-33), resolved 2026-07-12 in the key-layer readiness wave 1. Its current reading on the production arm is D-114 - the decoder commits its best path, so the abstain counter reads zero. OPEN_ITEMS OI-240 closes on this move

### D-243 — The planning band for the vertical engine, and the corpora excluded from it

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:4290-4298`

**Provenance.** The band is stated at ARCHITECTURE.md:3567-3575. The governing measurement surface is now the robust unit ratified at R10-b (CLAUDE.md gate block (A)), whose figures are reported per preset on a different unit; no ruling names this band as replaced. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-260 — Analysis output covers exactly the selection; everything loaded beyond it is evidence, never a result

> **Invariant.** The analysis output covers **exactly the selection**; everything outside it is evidence, never a
> result.

**In plain words.** The user's selection is the output span: labels are emitted only for it. Music loaded from outside the selection is pulled in as evidence for judging the selection's edges and is never itself labelled.

**Why.** Stated with the rule (cowork_bounded_context_design.md:21-26): the shipped product analyses the part of the score the user selected, and a layer often needs evidence from outside it to judge its edges. Separating the output span from the loaded span is what lets a layer read more music without changing what the user asked to have analysed.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_bounded_context_design.md:43-44`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. The three spans (the core distinction)` (heading at line 33). A delegation at ARCHITECTURE.md:1090 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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
>    answer — and it is what keeps the result independent of the extension step size (the equivalence invariant, §4).
>    **A layer applies that criterion DIRECTLY, on the in-selection quantity the extension was requested for**: it
>    re-infers over the enlarged span, compares that quantity step against step, and stops when it repeats. The
>    as-built Architectural Layer 3 reach-back does exactly this — it tracks the **leading-edge settled key across
>    iterations and stops when it repeats**, which is the criterion itself and not a stand-in for it (the convergence
>    note above the reach-back loop in `regionanalyzer.cpp` states it in the code's own words). §7's safety caps are
>    the only other way out of the loop, and a cap that fired is never the discovered amount.

**In plain words.** A layer knows what evidence it needs but not how far away it is, so it never picks an amount. It extends the loaded span incrementally and stops on a principled condition: convergence, meaning its in-selection output stops changing as more context arrives. The layer applies that test directly, on the quantity it asked for more context about, and stops when that quantity repeats.

**Why.** The reason is stated with the rule, in item 5 and item 6 of the contract itself: guessing an amount is the un-knowledge-based move the contract exists to forbid, and convergence is self-validating - you have enough context exactly when adding more does not change the answer - which is also what makes the result independent of the extension step size. Since 2026-08-07 the item also states WHY the criterion is applied directly rather than through a stand-in, and that defense is a measurement: the one domain proxy the clause licensed was disproved at build (D-622).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_bounded_context_design.md:57-71`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§3** — `## 3. The bounded-context contract (what every layer obeys)` (heading at line 51). A delegation at ARCHITECTURE.md:1090 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; the rule is items 5 and 6 of the bounded-context contract. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue). ★ THE VERBATIM IS RE-TAKEN FROM THE EDITED HOME, 2026-08-07, on the user's ruling (dispatch `cc_instruction_five_rulings.md` §0a R3; `OPEN_ITEMS.md` OI-331). The item-6 clause licensing a DOMAIN PROXY in place of the convergence test is STRUCK from the contract document and recorded there as tried and closed, with D-622 — the measurement that disproved it — named as superseding it. THE HEADLINE RULE IS UNCHANGED and so is this entry's status and its ratification: what was removed is the substitution clause and its worked example, not the rule that the amount of context is discovered by convergence. THE FORMER VERBATIM, PRESERVED WHOLE (#12): '3. A layer must distinguish **"unavailable because not loaded"** (→ request extension) from **"unavailable because the score starts/ends here"** (→ proceed, truncated). Architectural Layer 1 reports which. 4. A layer **outputs analysis only for the selection**; extended context is evidence, never labelled. 5. A layer **never guesses how much** more context it needs — guessing an amount is the un-knowledge-based move this contract forbids. It knows *what* it needs, not how far away that is, so it **extends incrementally and stops on a principled condition**; the amount is **discovered, not chosen**. 6. The principled stop is **convergence**: extend until the layer's **in-selection output stops changing** with further context. This is self-validating — you have enough context exactly when adding more does not change the answer — and it is what keeps the result independent of the extension step size (the equivalence invariant, §4). In practice a layer uses a **domain proxy that *implies* convergence** rather than re-checking its whole output each step (Architectural Layer 3 reach-back: *"a settled, stable prevailing key is in view"* — once a confident earlier key is established, the change-cost/decay means reaching further back will not move the selection's leading-edge key). The proxy is validated **once, in design**, to imply convergence.' The former home was `cowork_bounded_context_design.md:57-69`. Two further restatements of the struck example — the §5 Architectural Layer 3 bullet and the §10 spec-propagation bullet, both of which stated the reach-back's stop as the proxy — were corrected in the same act under the dispatch's own assumption check (A4), each with its former wording preserved in place.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_bounded_context_design.md:94-102`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§3** — `## 3. The bounded-context contract (what every layer obeys)` (heading at line 51). A delegation at ARCHITECTURE.md:1090 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_bounded_context_design.md:103-107`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§3** — `## 3. The bounded-context contract (what every layer obeys)` (heading at line 51). A delegation at ARCHITECTURE.md:1090 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_bounded_context_design.md:142-147`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. The protocol — request → supply → bounded recompute` (heading at line 117). A delegation at ARCHITECTURE.md:1090 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_bounded_context_design.md:136-141`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. The protocol — request → supply → bounded recompute` (heading at line 117). A delegation at ARCHITECTURE.md:1090 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_bounded_context_design.md:238-242`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8** — `## 8. Risks & the non-trivial parts` (heading at line 218). A delegation at ARCHITECTURE.md:1090 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_confidence_contract.md:25-34`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. Definitions — the two admissible confidence classes` (heading at line 23). A delegation at ARCHITECTURE.md:1129 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_confidence_contract.md:36-48`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§2** — `## 2. Definitions — the two admissible confidence classes` (heading at line 23). A delegation at ARCHITECTURE.md:1129 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** cowork_confidence_contract.md:3, status banner 'RATIFIED (user, 2026-07-02)'; rules U1 to U5 at :36-48. Rule U2 is the one already registered, as D-032, at its ARCHITECTURE.md home; U1, U3, U4 and U5 were not in the register. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-269 — The frame table is the one home of the override arithmetic; a new override site declares its frame before it is built

> **New frames require declaration here.** Any future override site (e.g. the A-4 cadence-less confirmation channels;
> the recognition consumer's schema-contradiction override, `cowork_progression_schema_design.md` §2) must add its
> frame row to this section before build — an undeclared cross-layer comparison is a contract violation.

**In plain words.** Every place where one layer's contradiction strength is compared against another layer's confidence is a declared frame - a triple of incumbent confidence, contradiction measure, and the conversion that makes them comparable - and all of them live in one section. Any future override site must add its frame row there before it is built; an undeclared cross-layer comparison is a contract violation.

**Why.** It is principle #6 (one path per concern) applied to the override arithmetic: the contract exists because the same comparison was being re-stated with different semantics at each site. Stating it once, with each instance's conversion declared, is what makes the threshold interpretable rather than an arbitrary scale factor.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_confidence_contract.md:83-85`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§4** — `## 4. The comparison frames (the §8 override arithmetic, stated once)` (heading at line 63). A delegation at ARCHITECTURE.md:1129 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** cowork_confidence_contract.md:3, status banner 'RATIFIED (user, 2026-07-02)'; the rule at :83-85, over the frame definition and the two built instances at :63-81. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-278 — The joint key-and-chord step is SHELVED - measured not to pay

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_engage_arc_plan.md:108-117`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“The stages”** — `## The stages (in principle order)` (heading at line 19). A delegation at CLAUDE.md:215 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** cowork_engage_arc_plan.md:3 records the user's ratification of this plan, dated 2026-07-07; the shelving at :103-112, with the measurement cited to its report and the no-information-loss reconciliation stated in place. Found by the phase-1d enumeration wave, 2026-08-02 - the class this audit exists for: a shelving with evidence, recorded only in a design document. ★ RATIFIED (user, 2026-08-02, option (a) with the deprecation made extremely clear) — the scoping annotation is at the home (the dated annotation beneath the shelving); the subject is legacy-era, will be entirely discarded at the OI-180 retirement map, and the shelving does not bear on D-001.

### D-282 — Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy

> - **Oracle/tier metric, never a bare proxy** (BIR rewards wrong-root=bass). Make the dual metric standing.

**In plain words.** Never grade the analysis on the bare bass-is-root number, which rewards a wrong chord root that happens to be the bass; use the oracle-checked, tiered measurement. Its content became standing through the robust-unit regression stop and the two-tier class policy.

**Why.** The stated reason is in the finding itself (the bare proxy rewards wrong-root-equals-bass); the successors carry their own measured defenses (D-115: the batch proxy under-counted the true per-onset error ~15-56x; D-191: decidable vs undecidable roots graded differently).

**Status.** SUPERSEDED BY D-115 and D-191 · date not stated · ratifier not stated

**Home.** `cowork_architecture_reassessment.md:106`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§4** — `## 4. Meta-findings to institutionalize (cross-cutting)` (heading at line 104). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Stated 2026-06-20 in cowork_architecture_reassessment.md §4 ('Meta-findings to institutionalize'); put to the user in §5 ('Ratify: …') with NO recorded answer (open_items/OI-270.md, the phase-1d wave's remainder). ★ RULED by the user 2026-08-02 (the OI-270 split, all four recommendations adopted): SUPERSEDED BY the named later ratified decisions — the governing status derives from the record's dates and explicitness, not from resolving the original statement's ambiguity. The second-partition read of the archives is instructed to flag anything refining these. ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

### D-286 — Whole-score interactive analysis was SHELVED WITH EVIDENCE; the bounded window is the ratified reading

>   self-consistent. **Decision (Cowork): bounded-window cache (CC's recommendation);
>   whole-score SHELVED with evidence; P3↔P1 consistency PARKED as a product/Stage-5
>   question; D-P4/D-BRIDGE closure rolled back to the 2.4 contract; the A/B data
>   promoted to committed Stage-5 evidence.** Revision instruction:

**In plain words.** At Stage 3.1b a measured A/B put a whole-score interactive analysis against a bounded-window one and the window won against the published annotations; the whole-score variant was withdrawn against that measurement and the bounded window adopted. The question of whether a per-note answer must match the whole-piece answer was parked, not settled.

**Why.** Measured: the A/B changed 32-40 % of ticks on contrapuntal music and the published annotations preferred the window path 59/41 overall and 65/35 on Mozart (`docs/p3_granularity_ab_3_1b.md`, the committed evidence). The shelving is the founding case of the decision-conformance audit: it lived only in an archive outside the session-start read, and a later build specified whole-score interactive analysis without meeting it (`OPEN_ITEMS.md` OI-210, OI-212).

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_handoff_archive.md:2964`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in the 2026-06-12 Stage-3.1b block of `cowork_handoff_archive.md` and in `docs/p3_granularity_ab_3_1b.md`. NOT superseded by any later ruling: `OPEN_ITEMS.md` OI-210 records that the extent question was then PARKED pending the granularity-robust metric (which has existed since 2026-07-06) and is now implemented as whole-piece by dispatch specification with no ruling — so the shelving stands on the record and the implementation departs from it. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-288 — Beam widening is SHELVED - a wider search cannot fix the failure class it was proposed for

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **⚠ STRATEGIC PIVOT (2026-06-13, Cowork-verified + user-directed): beam-widening
>   SHELVED; the back half of the roadmap is being re-grounded on measured precision
>   headroom.** The 3.2 design's §3 derivation (Cowork-verified against the independent

**In plain words.** Searching more candidate readings in parallel was withdrawn. The failure it was meant to fix is not a search failure: the wrong reading is the highest-scoring one, so looking at more readings finds the same wrong answer. Only changing how readings are scored, or cutting the music differently, can fix it.

**Why.** Derived, then cross-checked: the design's own arithmetic (verified against the independent earlier figures - AbMaj7 2.55 over 2.33, F#7 2.85 over 2.825) shows the wrong continued-root path is the genuine global optimum, which a decode finds exactly as a greedy walk does. The consequence recorded with it is that a wider beam is substitutable by the width-one beam for every other motivated use, so nothing else justified building it.

**Status.** LIVE · decided 2026-06-13 · ratified by the user (directive), on Cowork's verification

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_handoff_archive.md:3029`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-13 strategic-pivot block); `docs/beam_widening_design.md` was banner-shelved and retained for its derivation. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the search (at line 306 on 2026-08-03), under *"Tried and closed on the search — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-289 — Meta-principle: precision lives in the evidence and the functional labelling, not in the search

>   correct key never rank-2 in 51.6% of S2) — unrecoverable by any path. **SECOND
>   falsified structural fix → META-PRINCIPLE recorded in roadmap: precision lives in
>   emission + functional labeling, NOT search/path.** The HMM path is the least valuable
>   part of Stage 4 (~10%); KeyArea spans + the key-EMISSION fix are what deliver.

**In plain words.** Three independent investigations converged on one rule: accuracy is gained by improving what evidence each reading is judged on and by labelling harmonic function better - not by searching harder over the readings already on the table.

**Why.** Converged from three separate falsified structural fixes, each measured: the wider beam (the wrong reading is the top-scoring one), the key path (it reaches about 10 % of the key errors because the correct key is usually not even ranked second), and the algorithmic ground-truth filter. Recorded in `docs/implementation_roadmap.md` as a meta-principle.

**Status.** LIVE · decided 2026-06-13 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_handoff_archive.md:3082`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-13 Stage-4 design-investigation block) and `docs/implementation_roadmap.md`. ★ FLAGGED against the OI-270 meta-findings (D-282…D-285): this is an EARLIER and independently-derived statement of the same insight as D-284 (selection and competition are saturated). It does not change D-284's ruled status; it dates and corroborates it. It was itself later RECONCILED rather than overturned: `cowork_handoff_archive.md:3920-3921` records that the joint decode's value is broad-evidence integration, NOT search — "search is about zero" having been measured over a FIXED NARROW evidence surface. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue).

### D-293 — Fitted values are fitted per IDIOM, never for a user preset; presets are regression surfaces and delivery carriers

> **(f) Values are fitted per IDIOM, never for a user preset.** One fit event per musical idiom — a body of
> repertoire sharing a practice — and no value is ever adjusted to make a named preset come out right. A
> preset is a regression surface and a carrier for delivering a fitted set; which presets an end user should

**In plain words.** Numbers are fitted once per musical idiom - a body of repertoire that shares a practice - and never tuned to match one of the program's named presets. A preset is a way of delivering a set of values and a surface to check for regressions; which presets a user should see is a separate product question, decided later.

**Why.** A user mandate, recorded as constraint 4c of the fitting design. Its consequence is stated with it: ONE fit per idiom, and the Bach fit is an idiom fit delivered through two carriers.

**Status.** LIVE · date not stated · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:356-358`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the Stage-5 fitter block) as design constraint 4c of `cowork_stage5_fitter_design.md`. Consistent with, and earlier than, D-003 (inference is preset-independent; presets are presentation concerns) — this states the FITTING side of the same separation. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): stated as standing rule (f) of the joint estimator's specification. Former home preserved (#12): `cowork_handoff_archive.md:2363`, the Stage-5 fitter block, as design constraint 4c.

### D-294 — The only ground truth is the human annotation; the algorithmic analysis is a filter, and no self-annotation ever enters a measurement

> - **THE ONLY GROUND TRUTH IS THE HUMAN ANNOTATION. The algorithmic analysis is a noise filter, never a
>   standard of correctness** (user mandate 2026-06-10; homed here 2026-08-02 from `cowork_handoff_archive.md`,
>   `OPEN_ITEMS.md` OI-272). Accuracy is measured against the published human analyses — *When in Rome* /

**In plain words.** Accuracy is measured against published human analyses only. The second, computer-generated analysis is a noise filter, not a standard of correctness, so a measurement that uses it reports a lower bound rather than an agreement rate - and must never be described as agreement with ground truth. Our own outputs and our own test fixtures are never used as a standard of correctness; they pin behaviour against change and nothing more.

**Why.** A user mandate, sharpening what counts as ground truth. Its reason is stated with it: where the algorithmic analysis sides with us against the human annotator, the case is excluded by an algorithm's opinion, so the count understates the human-adjudicated error. The mandate produced the requirement for a human-annotation-only measurement, which is the unit now governing (D-115).

**Status.** LIVE · decided 2026-06-10 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `CLAUDE.md:626-628`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the corpus-audit block, as the ground-truth verdict). The human-annotation-only requirement it names was delivered as the granularity-robust unit (D-115), whose own text carries the clause "music21 is NOT ground truth"; the two further clauses — never describe a measurement as ground-truth agreement, and no self-annotation in any measurement — are recorded ONLY here. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]] — measurement conventions go to the gate block): written into `CLAUDE.md` gate block (A) as the FIRST of the four grading conventions the robust unit is measured under, carrying all three clauses the archive held alone. Former home preserved (#12): `cowork_handoff_archive.md:2844`, the corpus-audit block.

### D-297 — Correction of record: never computing a possibility is not information loss; only discarding a computed one is

>   **The rule's boundary, stated because an earlier framing got it wrong: NEVER COMPUTING a possibility is
>   not information loss; only DISCARDING a computed one is.** A layer that decides, on measured evidence,
>   not to work out a particular alternative at all has lost nothing — you cannot lose what you never had.

**In plain words.** The no-information-loss principle forbids throwing away something the analysis has worked out. It does not require working out everything that could be worked out. Deciding, on measured evidence, not to compute a possibility is an ordinary design decision - you cannot lose what you never had.

**Why.** Recorded as an explicit correction of an earlier, wrong framing that had called the same situation a principle violation. The worked case is the shelved joint key-and-chord step: the chord under an alternative key is never computed on that path, the key alternatives themselves ARE carried, and the roughly 1.4 % of cases where the alternative would differ were measured to be an even split, i.e. noise.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:1143-1145`

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-07-07 entry-point block) as a dated correction. It scopes D-099 / principle #12 and is recorded nowhere that a reader of #12 would find. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]]): written into `ARCHITECTURE.md` §2.15 as the boundary clause of the negative-evidence contract, beside D-099 — the home this row's own text named. Former home preserved (#12): `cowork_handoff_archive.md:1532`, the 2026-07-07 entry-point block.

### D-313 — A confidence map is monotone or it is not fitted — a non-monotone curve is an upstream finding, not a mapping target

> **D-8 Calibration maps are monotone or deferred.** A non-monotone empirical curve (L5 combinedBoundary) is
> an upstream finding, not a mapping target — fitting a non-monotone map would launder an inference defect
> into the confidence semantics. (Contract R4/R5 monotonicity carries this.)

**In plain words.** Turning a layer's internal confidence number into a statement about how often it is right is only done when a higher number really does mean more often right. Where the measured curve goes the wrong way in places, that is reported as a fault in the layer, not smoothed over by the map.

**Why.** Stated with the rule: fitting a non-monotone map would launder an inference defect into the confidence semantics — the map would make a mis-ordered confidence read as a well-ordered probability. The confidence contract's monotonicity rules carry the same requirement.

**Status.** LIVE · decided 2026-07-04 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_stage5_fitter_design.md:684`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions` (heading at line 623). A delegation at ARCHITECTURE.md:301 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_layer5_function_design.md:646-657`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives weighed)` (heading at line 620). A delegation at ARCHITECTURE.md:1929 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_joint_key_chord_design.md:136-140`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§1.3 How it avoids re-introducing a cross-layer cycle”** — `### §1.3 How it avoids re-introducing a cross-layer cycle (#7)` (heading at line 118). A delegation at cowork_engage_arc_plan.md:44 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_joint_key_chord_design.md` IN FULL. The step the document designs is shelved (**D-278**); this prohibition is not about that step — it is stated as what any placement must avoid, and is flagged in the record as written so the build does not drift there. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-422 — The jazz fit is deferred to the jazz ground-truth conversion; only the classical common-practice idiom is fitted now

> **Stage-5 design SIGNED 2026-07-04:** `cowork_stage5_fitter_design.md`; A-3 ruled = Jazz fit deferred to the
> jazz-GT conversion (the idiom-#2 Baroque/Default target is fitted now).

**In plain words.** Fitting the analysis constants for jazz waits until jazz music with published human analyses can be converted into a form the fitter can use. What is fitted now is the one idiom the held annotated music covers — the classical common-practice one, which is what the two non-jazz presets deliver.

**Why.** It follows from a measured constraint recorded elsewhere in the register: jazz accuracy is not measurable on the corpora held, because the jazz material is melody-and-chord-symbol transcription with the bass and piano voicings absent (D-310, whose defense is a bass-injection experiment moving agreement from 39.8 % to 98.3 % on one corpus and 18.0 % to 99.9 % on another). Fitting against material that cannot measure the result would be fitting without evaluation, which guiding principle #20 forbids.

**Status.** DEFERRED · decided 2026-07-04 · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/implementation_roadmap.md:549`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“Stage 5”** — `## Stage 5 — Fit the weights *(stop hand-tuning)*` (heading at line 532). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `docs/implementation_roadmap.md`:460-461, recorded at the Stage-5 fitter design's signing: "Stage-5 design SIGNED 2026-07-04 … A-3 ruled = Jazz fit deferred to the jazz-GT conversion". The document states the DESIGN was signed that day but does not say who ruled A-3, so the ratifier is NOT STATED. A-3 is one of the ten external-review amendments the record marks user-ratified 2026-07-02 at `:148-151`, but that ratification is of the amendment, not of this later disposition of it. Beside D-310 (jazz accuracy not measurable) and `OPEN_ITEMS.md` OI-7 (establish a jazz ground truth or de-scope the jazz claims). Recorded in a plan rather than in the fitter's own specification, hence the documentation-gap flag. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-466 — Forward-only is a strong DEFAULT, not dogma — a backward edge is admissible only as a deliberate, surfaced, measured, documented exception

> **Forward-only is a strong *default*, not dogma:** a sanctioned backward edge is admissible
>   only as a deliberate, surfaced, measured, documented exception (justified by a plateau, scoped, gated,
>   convergence-bounded, recorded).

**In plain words.** The rule that each stage passes its work forward and never reaches back may be relaxed if it genuinely gets in the way of being right. But only deliberately and in the open: the case must be justified by evidence that the forward-only path has stopped improving, confined to the cases that need it, gated so it does not fire on the ordinary majority, bounded so an iterative one cannot run away, and recorded as an architecture decision. A silent cycle is never admissible.

**Why.** Stated with the rule in the target-architecture document read in full this wave: the bar is high precisely because a backward edge trades away the acyclic guarantee — which is what makes the pipeline deterministic and removes any convergence question — but the rule exists so that the guarantee is a chosen default rather than an unexaminable commitment.

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1028-1030`

**Provenance.** Carried in ARCHITECTURE.md §2.15's confidence-weighted-override bullet, whose full statement is `cowork_target_architecture.md` §2, read in full by the phase-1 reads wave 1 — where the clause is marked "user, 2026-06-22" and states the five conditions in full. D-025 carries the forward-only rule itself and its two scoped escapes; the revision clause is entered here because no register entry carried it. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-468 — The pinned block-(A) instrument declares which inference arm its baselines were measured on, and refuses a corpus whose stamp disagrees

> **★ THE PINNED INSTRUMENT NOW DECLARES WHICH INFERENCE ARM ITS BASELINES WERE MEASURED ON, AND REFUSES
> A CORPUS WHOSE STAMP DISAGREES

**In plain words.** The measurement tool that produces every baseline in the hard-stop block now says out loud which of the two analysis pipelines those baselines came from, and it declines to measure a corpus whose own record says it came from the other one. It cannot change any measured value; it can only decline.

**Why.** Stated with the decision at its home: the defect being closed is that --joint-inference is opt-in, so a regeneration that omits it silently fills the directory this instrument reads with the other pipeline's output, and an opt-in DETECTOR would reproduce that hole's shape exactly — absent from precisely the invocation that most needs it. Hence a declared default rather than a flag. The instrument is one CLAUDE.md gate block (A) calls pinned, so the narrow claim that it can only refuse and can move no measured value is itself measured rather than asserted (#19).

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:476-477`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Built 2026-08-03 (CC, phase 1y, dispatch cc_instruction_phase1y_corpus_arm_stamping.md) as the manifest half of OPEN_ITEMS.md OI-307, and flagged there as a judgment call for the user rather than buried; recorded at gate block (A) 2026-08-04 (phase 1z, dispatch cc_instruction_phase1z_commit_and_instrument_record.md Task 2.3), the block that pins the instrument being where a change to it belongs (#7). ★ RATIFIED BY THE USER, 2026-08-03, in session — presented as three options with the third recommended, ratify AND record, and agreed. The ruling is transmitted in the read-wave-2 dispatch cc_instruction_reads_2.md §0a, whose ruling ledger records why this field read otherwise for a day: the phase-1z re-issue dropped the sentence carrying the ratification, so phase 1z executed the recording half of the ruling and not the ratifying half, and this entry stated 'ratifier not stated' about a decision the user had made. ★ The former provenance sentence — 'THE USER HAS NOT RULED ON IT: recording is not ratifying, and no ratifier is inferred from the dispatch that ordered the record.' — is preserved here rather than deleted (#12), and it was the correct thing to write on what phase 1z was given: what was missing was the transmission, not the ruling, and inferring a ratifier from a dispatch that named none would have been the worse error. The two measurements it rests on are generated, and no value of either is restated in the record (#17f, D-431): that the declaration moves nothing is at tools/audit/instrument_arm_declaration_effect.json, which runs gate block (A)'s own two commands at HEAD over the production corpus and diffs against the committed tools/robust_stop/ reference; that it detects a wrong-arm corpus, admits a right-arm one and leaves an undeclared caller alone is at tools/audit/corpus_arm_establishment.json, probes 2, 3 and 4. Reversal is one default (EXPECT_ARM_DEFAULT set to 'any').

### D-474 — No published study reports per-axis inter-annotator agreement for Roman-numeral analysis of Baroque/classical symbolic music — the ground-truth ceiling principle #21 demands is unmeasured by the entire field

>     **★ THE CEILING CANNOT BE CITED FROM THE LITERATURE; MEASURING IT HERE IS THE ONLY ROUTE
>     (recorded 2026-08-04 on the user's ruling with the read-wave-3 ratification; D-474).** A
>     dedicated search established a FACT-of-absence: no published study reports per-axis
>     inter-annotator agreement for Roman-numeral or key annotation of Baroque/classical symbolic
>     music. TAVERN released duplicate annotations but published no such number; ABC split its pieces
>     between annotators with no overlap by design; the Mozart-sonatas corpus is consensus-built, so
>     agreement cannot be recovered after the fact; *When in Rome* states in its own words that the
>     variance is unmeasured; Dilemmadata (2026) identifies dual-annotated pieces and computes
>     nothing. **So a session may not satisfy this principle by citation — there is nothing to cite.**
>     The obligation is tracked at `OPEN_ITEMS.md` OI-179, which is therefore not "a measurement not
>     yet built" among others but **the only available route to the quantity this principle demands**.

**In plain words.** Principle #21 says the accuracy of the human annotation is itself something to measure, so that an error we cannot fix is told apart from two experts simply disagreeing. Searching the literature found that nobody has published such a figure for this repertoire — so the ceiling cannot be cited from anywhere and would have to be measured here.

**Why.** Measured by search rather than asserted: each candidate corpus is named with the reason it yields no figure — duplicate annotations published without a number, pieces split between annotators by design, consensus-built annotation whose agreement cannot be recovered after the fact. The quantified bounds that DO exist are recorded beside it, from other domains (rock symbolic by ear; pop audio), together with the invariant they share — root and key agree far better than the full label, inversion always costs about five points, quality is the most subjective axis.

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:117-127`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** The central finding of the theory-grounding audit's ground-truth section, reached by a dedicated search and recorded with the corpora checked (TAVERN, ABC, the Mozart sonatas, When in Rome, Dilemmadata). Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) It is the literature half of the obligation **D-184** (principle #21) creates and is tracked at `OPEN_ITEMS.md` OI-179. ★ HOME FIELD RE-AIMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). ★ THIS IS A FIELD CORRECTION AND NOT A PIECE OF WRITING, and the ruling says so in terms: the content is ALREADY WRITTEN into `CLAUDE.md` principle #21, which carries the fact-of-absence and names this entry in terms, and what was outstanding was only the register's HOME field, which still pointed at the findings document. NO FILE WAS EDITED FOR THIS ENTRY. The home now points at principle #21's own block, and the verbatim is re-taken from there. It is the one member of finish-line item 1 for which criterion C1 was substantively satisfied and only the bookkeeping was not. FORMER HOME, PRESERVED (#12): `cowork_term_theory_grounding.md:258-262`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 256, "section": "## 2. The ground-truth ceiling (OI-179, literature half) — and the BCMH verdict", "label": "§2", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**FACT-of-absence (the central finding):** no published study reports per-axis inter-annotator agreement
for RN/key annotation of Baroque/classical symbolic music. TAVERN has duplicate annotations but
published no number; ABC split pieces between annotators (no overlap by design); the Mozart sonatas
corpus is consensus-built (agreement unmeasurable post hoc); When in Rome 2020/2023 states the variance
is unmeasured; Dilemmadata (2026) identifies 84 dual-annotated pieces and computes nothing yet." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-475 — The BCMH chorale annotations are NOT established as an instrument: the annotator is unknown, the annotations sit on a reduction, and they reached the repository through a machine translation

> content to any existing analysis). **Unestablished as an instrument (#19):** annotator count/identity
> and validation are UNKNOWN (the JEP:HPP Method section and the dataset zip's headers are the two places
> that would settle it — the zip is fetch-blocked in this environment but downloadable on the user's
> machine); the annotations sit on a homorhythmic REDUCTION (unit mismatch with our full-texture grading
> must be handled in the measurement design); they reached the repo through a machine translation into
> rntxt (Nápoles López), whose noise would be part of any measured disagreement. **Consequence:** the

**In plain words.** A second set of human chorale analyses is held, and it would be the natural way to measure how far two annotators disagree. It cannot be trusted yet: nothing in the dataset says who made the annotations or whether they were checked, the analyses describe a simplified version of the music rather than the full texture, and they were converted automatically into our format, so the conversion's own errors would show up as disagreement.

**Why.** Measured at the objects, not assumed: the dataset was downloaded and read file by file, and the only editor records found are the note-encoding provenance of the underlying score collection. The independence half is a FACT the source states in its own words ('we encoded'), which is what makes the corpus worth establishing rather than discarding.

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_term_theory_grounding.md:274-279`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§2** — `## 2. The ground-truth ceiling (OI-179, literature half) — and the BCMH verdict` (heading at line 256). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** The theory-grounding audit's verdict on the BCMH corpus, with the three establishment steps it names. The audit's own dated update of 2026-07-19 records that the first step came back NEGATIVE at the files — no annotator record in any of them — and its source register adds that the 2023 Method section names no annotator and no validation either. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ This is an ESTABLISHMENT statement under #19: a consumer may not put this corpus under load while it stands.

### D-486 — A measurement publishes its coverage denominator and its per-corpus breakdown; a single aggregate number that hides which corpus moved is not reported

> - **A measurement publishes its COVERAGE DENOMINATOR and its PER-CORPUS breakdown; a single aggregate
>   number that hides which corpus moved is not reported** (2026-06-13; the record states no ratifier).
>   The denominator published is the number of pieces the measurement actually resolved to a human

**In plain words.** When accuracy is reported, the number of pieces it was actually measured on is stated, never the number of pieces held. And the corpora are reported separately, because one combined figure lets an improvement on one repertoire pay for a loss on another without anyone seeing it.

**Why.** Stated with the rule and evidenced in the same sentence: only 326 of the 353 gate chorales resolve to a human annotation at all, so dividing by 353 reports an accuracy the measurement never had; and the cross-corpus root-error rate ranges from about 41 % to about 55 % across corpora, so a scalar objective would let a fit win on chorales while losing on Corelli.

**Status.** LIVE · decided 2026-06-13 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:671-673`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** A rule of the Stage-5 objective section of a metric design document whose banner reads DRAFT — UNCOMMITTED and which closes 'awaiting Cowork/user ratification before any metric is built'. The metric it designs WAS subsequently built and ratified — the granularity-robust unit of `CLAUDE.md` gate block (A), R10-b, 2026-07-06 — and that block reports its coverage as 326/352 in exactly this form, so the rule is honoured at HEAD while the document that states it still presents itself as an unratified draft (see `OPEN_ITEMS.md`). Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ HOMED 2026-08-07 (CC, the licensed homing wave, executing the user's ruling R2 of 2026-08-07, dispatch `cc_instruction_licensed_homing_and_oi344.md` §0a — the LICENSING class of finish-line item 1's re-home set, homed under the edit-surface licence the user ruled on the same date). Written into `CLAUDE.md` gate block (A), as the first of the three further measurement conventions homed beside the four grading conventions, in that section's own voice and with its defense. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. FORMER HOME, PRESERVED (#12): `docs/precision_metric_design.md:291-293`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `process` entry (the register's own home rule): section "### 3.3 The Stage-5 objective function", label "§3.3", verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **Coverage honesty:** report the 326/353 WiR denominator and per-corpus breakdown; never aggregate a\n  single number that hides which corpus moved (the cross-corpus root_err ranges corelli 55%→dvorak 41%\n  [doc, dossier §1.4] — a scalar would let a fit win on chorales while losing on Corelli).". Provenance is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, its date and its ratifier where the record states one, and its defense.

### D-497 — RATIFIED AMENDMENT A-7: the empirically-unvalidated mark must be APPLIED to the Jazz preset constants and the unvalidated idioms, with the validation path named

> **Every style constant and every idiom that no ground truth has calibrated CARRIES THE
> EMPIRICALLY-UNVALIDATED MARK, and the corpus that would validate it is named beside it (re-homed
> into this specification 2026-08-07 on the user's ruling).** The verifiability contract already
> defines that mark; this states where it must appear and what must accompany it. It applies to the
> **Jazz preset constants** and to the **idioms of the §6.7 taxonomy for which no gate-grade ground
> truth exists**, and the mark is not decorative: beside each marked value the record names **the
> validation path** — the corpus class that would establish it. **Maintenance is part of the rule:**
> a value keeps the mark until an established corpus measures it, and it loses the mark only in the
> act that records that measurement, never by a value being changed or a preset being renamed.
> *Why:* measured by the architecture review — calibration and validation are Baroque- and
> Bach-heavy, the jazz preset and the non-classical idioms have no gate-grade ground truth, and the
> mark defined in the specification was found absent from exactly those constants and presets. The
> gap is therefore between a stated rule and its application, not in the rule, which is why what is
> written here is the rule and its maintenance rather than a new criterion. **What this clause does
> NOT claim:** that the mark is applied at HEAD. It is not; applying it, constant by constant and
> idiom by idiom with the validating corpus named, is owed work and is tracked in the open-items

**In plain words.** The rule that says an unvalidated value must be marked as such already exists. The review found it was not actually applied to the constants only Baroque data has ever calibrated. The amendment requires the mark to be put on them, and the corpus that would validate each to be named alongside.

**Why.** Measured by the review: calibration and validation are Baroque- and Bach-heavy, the jazz preset and the non-classical idioms have no gate-grade ground truth, and the contract's own mark is present in the specification but absent from the affected constants and presets — so the gap is between a stated rule and its application, not in the rule.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:5157-5172`

**Provenance.** Amendment A-7 of the external architecture review, in a document whose banner records amendments A-1…A-10 as RATIFIED by the user on 2026-07-02. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ NOT A FRESH DECISION, stated so that nothing is counted twice (dispatch cc_instruction_reads_3.md §1.3): the amendment itself was ratified by the user at the 2026-07-02 architecture review, which is what this entry's Status line already records. Ratifying the ENTRY records only that the register transcribes that ratification correctly — it neither re-makes the decision nor adds a second ratification event to it. It is the APPLICATION half of the verifiability contract **D-029** — the mark exists in the specification and the review found it unapplied — and it is adjacent to **D-310**, which records that jazz accuracy is not measurable on the corpora held. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The ruling SPLITS the amendment: THE RULE — the mark and its maintenance — goes to `ARCHITECTURE.md` §6 beside the preset constants, and THE APPLICATION is owed work that must be tracked by an open-items row. Both halves are done. The rule is written into §6 in that section's own voice, with its defense and with an explicit statement that it does NOT claim the mark is applied at HEAD. ★ THE ROW CHECK THE RULING ORDERS WAS RUN: `OPEN_ITEMS.md` OI-7 was the named candidate and is NOT the same obligation — it asks for a jazz ground-truth corpus to be established or the Jazz claims de-scoped and it gates the Stage-3 entry gate, while the application half asks for the absence of that evidence to be DECLARED where a reader meets the values and gates nothing; either could be discharged without the other. No other open row names the mark's application, so a row was created in this commit under register rule (c): `OPEN_ITEMS.md` OI-346, index row and detail file together. FORMER HOME, PRESERVED (#12): `cowork_architecture_review_2026_07.md:328-329`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 307, "section": "## 9. Proposed amendments (ranked; each ratification-gated; none is code)", "label": "§9", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **A-7 (from F-7). Apply the "empirically-unvalidated" mark** to the Jazz preset constants and idioms 3–5 in the
  affected docs; name the validation path (JHT/McGill-class corpora already inventoried by the idiom study)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-500 — The user ratified CORPUS EXPANSION at the architecture review: gate-grade jazz ground truth, chromatic material of the Wagner class, and more non-Bach, non-Baroque annotation generally

> additionally ratified **corpus expansion** — gate-grade jazz GT and Wagner-class (and similar) DCML material; in
> general more non-Bach, non-Baroque ground truth (folded into A-7/A-8; recorded in `docs/implementation_roadmap.md`).

**In plain words.** At the same review the user approved widening the material the program is measured against: real ground truth for jazz, hard chromatic repertoire, and in general more annotated music that is neither Bach nor Baroque.

**Why.** Derived from the review's own findings F-7 and F-8: calibration and validation are Baroque- and Bach-heavy with no gate-grade ground truth for the jazz preset or the non-classical idioms, and the review names a chromatic stress corpus as the measurement bed for the capability amendments.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_architecture_review_2026_07.md:4-5`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **the opening block (above the first section heading)** — `# Comprehensive architecture review — the layered inference architecture (external Cowork review)` (heading at line 1). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** Recorded in the banner of the external architecture review as a user ratification additional to amendments A-1…A-10, folded into A-7/A-8 and recorded in the implementation roadmap. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) ★ NOT A FRESH DECISION, stated so that nothing is counted twice (dispatch cc_instruction_reads_3.md §1.3): the amendment itself was ratified by the user at the 2026-07-02 architecture review, which is what this entry's Status line already records. Ratifying the ENTRY records only that the register transcribes that ratification correctly — it neither re-makes the decision nor adds a second ratification event to it. It is the ratification the corpus waves that follow it execute; the standing rule on the other side — a newly acquired corpus enters as research material and the frozen corpus stays the gate until a deliberate re-baseline — is `CLAUDE.md` gate block (A) and is not weakened by it.

### D-521 — The general law of the circularity map: an abstract circle becomes acyclic in the concrete by one of four named conditions — and every alleged circle in this system fell to one of them

> **The general law all five instances obey:** a circle in the ABSTRACT ("A needs B,
> B needs A") becomes acyclic in the CONCRETE when one of: the score already contains
> one side (spelling, signatures, fermatas, annotations); a key-agnostic form of the
> evidence exists (tonic votes, dominant shapes, bass skeletons); the dependency is on
> a COARSER fact that is already stable (the collection, not the tonic); or the
> ratified forward-override/joint-minority patterns cover the measured-rare remainder.
> Every alleged circle above fell to one of these. None survived as a true blocker —
> which is the answer to the user's worry: the circularity challenge, named
> completely, stops nothing.

**In plain words.** The worry that key, chord, cadence and non-chord tones each need one another turns out not to block anything once the cases are named. A circle dissolves when the score already contains one side of it, when a form of the evidence exists that does not need the other side, when the real dependency is on a coarser fact that is already settled, or when the rare remainder is covered by the ratified forward-recompute pattern.

**Why.** Established case by case rather than argued in general: the five alleged circles are each named, and each is shown to fall to one of the four conditions — spelling is input because we read notated scores; the cadence machinery votes for a tonic without reading one; the chord layer needs the collection far more than the tonic, which our own measurement shows; grammaticality is scored per candidate key, so the key is a hypothesis index rather than an input.

**Status.** LIVE · decided 2026-07-12 · ratifier not stated

**Home.** `cowork_evidence_inventory.md:196-204`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§8** — `## 8. Which of it the KEY layer wants — and the circularity map, faced honestly` (heading at line 149). A delegation at ARCHITECTURE.md:1161 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it RECORDS FINDINGS**.

**Provenance.** The conclusion of the evidence inventory the user directed, and the answer to a worry the user raised. It is the general form of the standing forward-only rule (**D-025**, **D-466**) and of the forbidden back-edge (**D-377**): those say what is not allowed, this says why the prohibition is affordable. The one measured premise it leans on — chord roots are key-invariant under collection siblings — is the reason the collection/tonic split is named the inventory's headline unpublished fact. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-522 — Explaining an inference to the end user is a late-bound DISPLAY consumer of facts that already exist — not a new analysis

> **Explainability (user, 2026-07-13): the end user may want to know HOW a mode, chord,
> or function was inferred.** If the evidence trail behind every inference is published
> — which pitch classes drove the key, which cadence vote confirmed the modulation,
> which margin separated the winner from the runner-up, why the analyzer abstained —
> then "show me why" is a late-bound DISPLAY consumer of facts that already exist, not
> a new analysis. Much of the raw material exists today as internal diagnostics (the
> chord-diagnosis replay, the dormant function machinery's structured open marks and
> ambiguity kinds, the ranked-candidates-plus-margins confidence contract); the gap is
> publication, which is wave 3's job anyway. A register row for the feature follows at
> the next free number (numbers are in flight in the current CC session).

**In plain words.** If the evidence behind each inference is published — which pitch classes drove the key, which cadence confirmed the change, how far ahead the winner was, why the analyzer declined to decide — then answering 'show me why' is a matter of displaying what is already there, not of analysing anything again.

**Why.** Grounded in an inventory of what already exists: most of the raw material is present today as internal diagnostics — the chord-diagnosis replay, the structured open marks and ambiguity kinds of the dormant function machinery, and the ranked-candidates-plus-margins confidence contract — so the gap is publication rather than computation.

**Status.** LIVE · decided 2026-07-13 · ratified by user

**Home.** `cowork_evidence_inventory.md:215-224`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§8b** — `## 8b. Declared future consumers, named by the user (2026-07-13)` (heading at line 206). A delegation at ARCHITECTURE.md:1161 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it RECORDS FINDINGS**.

**Provenance.** Named by the user at the evidence-inventory discussion, in the same conversation that produced the publish-broadly amendment to the fact-publication corollary in `CLAUDE.md`. It is the second declared future consumer recorded there, beside the intonation feature; both are instances of the rationale for publishing evidence without a named consumer — a visible menu lets a future design recognise facts it would never have thought to request. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-523 — If the algorithmic second opinion's LOCAL key is ever adopted it enters UNVALIDATED, and adopting it is a corroborator re-baseline under user ratification — not a refresh

> **Status if it is ever adopted:** it enters as an **unvalidated** field and stays
> unvalidated until positively established (#19 — a consumer may not put it under load
> before then), and music21 is **not** ground truth (DCML/When-in-Rome is; music21 only
> corroborates). Activating it changes the committed `.music21.json`, so adoption is a
> **corroborator re-baseline** under the user's ratification (#16), not a refresh.
>
> **Gate:** the key-layer design conversation. Carried on **OI-158**; the dead-code half
> of that row is closed, this half stays open.

**In plain words.** Whether to consult the second-opinion library for a local, moving key rather than only a single key for the whole piece is left open. If it is ever taken up, the field arrives explicitly unvalidated and no consumer may lean on it until it is established. Turning it on changes the committed second-opinion files, so it is a deliberate re-baseline the user ratifies.

**Why.** Both halves are grounded in standing rules rather than chosen here: a fact is trusted only after being positively established (#19), and the algorithmic analysis is a corroborator and never ground truth, so its output is a pinned artifact whose regeneration is a re-baseline (#16). The document also records that the machinery which appeared to do this never ran at all — the class it named does not exist in the pinned version — and that removing the dead code was proven byte-identical and deliberately does not decide the question.

**Status.** DEFERRED · decided 2026-07-13 · ratifier not stated

**Home.** `cowork_evidence_inventory.md:241-248`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§8c** — `## 8c. An external evidence source, filed OPEN — music21's local key (OI-158)` (heading at line 226). A delegation at ARCHITECTURE.md:1161 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it RECORDS FINDINGS**.

**Provenance.** Filed OPEN in the inventory and carried on `OPEN_ITEMS.md` OI-158, whose dead-code half is closed and whose question half stays open, gated on the key-layer design conversation. The pinning rule it invokes is **D-226**; the ground-truth rule is **D-294**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-531 — The hand-built emission is CONFIRMED and the learned replacement is NOT triggered — retained as an explicit fallback with a concrete trigger, and scoped to one repertoire with a named re-check gate

> **The standing verdict on this principle's own live case: the hand-built analysis is CONFIRMED and
> the learned replacement is NOT TRIGGERED — it is retained behind this interface as the explicit
> fallback, with a concrete trigger.** The substitution this section exists to keep possible was put
> to a measured test on the analysis front — go on improving the hand-built scorer, or replace it
> with a trained model. The measured answer is to keep the hand-built one: the error mass decomposes
> into causes reachable within it, and the bucket that would genuinely need a learned model came back
> empty on the sample. The learned option is **not withdrawn**; it stays a drop-in behind the
> interface, and it re-opens for **any slice later established as a genuine ceiling**. *Why:* decided
> on measurement, with the measurement's own limits stated as part of the decision — the corrected
> metric showed the residual had been inflated by already-correct artifacts and by mis-attributed
> cases, the empty bucket is a sample carrying a stated corpus upper bound, and the algorithmic
> second opinion fails the same functional roots, which makes it a missing-layer problem rather than
> a ceiling of the vertical scorer. **Two limits ride with the verdict and are part of it:** the
> decomposition covers one repertoire only, and the fallback's advantage is concentrated on the
> harder chromatic material that was not decomposed; and the corrected metric must be **committed
> before any fitting**, or the fitter optimises against cases that do not exist.

**In plain words.** The open question was whether to keep improving the hand-written scorer or replace it with a trained model. The measured answer is to keep the hand-written one: the error mass decomposes into causes that are fixable within it, and the bucket that would need a learned model came back empty on the sample. The learned option is kept as a stated fallback, to be reconsidered for any slice later shown to be a genuine ceiling.

**Why.** Decided on measurement, and the measurement's own limits are stated with it: the corrected metric showed the residual had been inflated by already-correct artifacts and mis-attributed cases, the empty bucket is a sample with a stated corpus upper bound, and the algorithmic second opinion fails the same functional roots — which makes it a missing-layer problem rather than a scorer ceiling. The scope limit is explicit: the decomposition is one repertoire only, the fallback's advantage is concentrated on harder chromatic music that was not decomposed, and the question is formally re-openable at a named gate.

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Home.** `ARCHITECTURE.md:669-684`

**Provenance.** The ratified answer to the back-half re-grounding's first open question. The prerequisite recorded with it — the corrected metric must be COMMITTED before any fitting, or the fitter optimises against phantom cases — is part of the ruling. The measurement-substitutability interface that keeps the fallback a drop-in is **D-075**. The convergent finding this document derives the whole back half from is registered as **D-289**, whose only recorded home is a session-handoff archive while its full derivation is here. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was whether §2.2, which owns the substitutability property, also owns a standing not-yet-triggered verdict. The user ruled that it does: the standing verdict and its concrete trigger ARE the current state of the substitutability contract, so they belong at the section that states that contract. Written into §2.2 in that section's own voice, with its defense and with the two limits the record states as part of the decision (one repertoire only; the corrected metric committed before any fitting). Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/back_half_design.md:108-116`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 79, "section": "## §3 — The design-goals fork, resolved on the evidence: A (hand-built) confirmed; B (learned) NOT triggered, kept as the explicit fallback", "label": "“§3”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**OQ-1 RATIFIED 2026-06-14 — A confirmed, scoped to Bach (user decision).** The functional
root-error mass — the one slice §3 left undecomposed — is now decomposed on the *corrected*
metric (`cc_functional_residual_dossier.md`): the buggy parser had inflated the "functional"
residual with 365 already-correct artifacts + 75 mis-attributed vertical cases; the cleaner
2153-region residual splits into rule-reachable + ambiguity/noise with an **empty
needs-a-learned-model bucket (B2 = 0/44 sampled; corpus upper bound ~7%)**. music21's vertical
RN analyzer fails the same functional roots (0/4) → it is a functional-*layer* problem (= A),
not a vertical-scorer ceiling. So **A is confirmed on the functional axis too, B is not
triggered.**" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-539 — The standing method for every error slice: decompose it into structural, fitted and ceiling BEFORE building anything — derive, never assert

> **★ AND AN ERROR SLICE IS DECOMPOSED BEFORE ANYTHING IS BUILT FOR IT — STRUCTURAL / FITTED /
> CEILING (homed here 2026-08-07 on the user's ruling; decided 2026-06-13, the record states no
> ratifier).**
> MEASURE-BEFORE-BUILD above says that a precision claim is measured before it is built. This says
> what the measurement is OF, and it is the standing method for every error slice: **decompose the
> slice three ways — what a STRUCTURAL lever reaches, what belongs to the FITTED step, and what is a
> genuine CEILING — before anything is built for it.**

**In plain words.** Before work is done on a class of errors, the class is broken into three parts: what a structural fix reaches, what belongs to the fitting step, and what is a genuine ceiling. The structural part is built, the fitted part is routed to the fitter, and the ceiling is either accepted as ambiguity or flagged as evidence for the fallback.

**Why.** Presented as the lesson that had already paid three times in one session: three separate investigations each tested a structural fix on a different slice and each falsified it for the same reason, and the one probe that decomposed its slice found the bulk specific and recoverable. The method is what turned a pessimistic reading into an actionable one.

**Status.** LIVE · decided 2026-06-13 · ratifier not stated

**Home.** `cowork_engage_arc_plan.md:131-137`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The standing method of the back-half re-grounding, stated for every slice. It is the ancestor of the MEASURE-BEFORE-BUILD gate (**D-277**) and of the #17 funnel's staging — desk-simulate, then probe read-only, then build — and the reason the document gives for re-deriving the plan rather than amending it is the accumulating-amendment smell the architecture principles name. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the three-owner-rulings wave, executing the user's ruling R3 of 2026-08-07). This is one of the three entries the licensed homing wave of the same date did NOT home: its recorded owner named 'the principles' and no section, assumption A1 came back refuted for it, and it was returned to the user with the owner question rather than written into a guessed section. The user answered it. Written into `cowork_engage_arc_plan.md` BESIDE THE MEASURE-BEFORE-BUILD GATE — the ratified, delegated contract for the ORDER OF WORK, which this entry's method is a rule of, and where D-277, the method's recorded descendant, already lives — in the contract's own voice and with its defense. Assumption A3 was discharged before the edit by reading the section: it STATES RULES rather than recording findings, which is D-430's kind half. THE EXCLUDED ALTERNATIVE, RECORDED WITH THE RULING (#12): `CLAUDE.md` beside the #17 funnel, which would begin restating what the governing file delegates (#6) — the delegation written into `CLAUDE.md`'s principles section points at the arc plan and does not restate it. THE ONE-EDIT AUTHORIZATION: `cowork_engage_arc_plan.md` is a ratified contract document outside every standing licence, and the user's ruling is itself the authorization for this single edit, which is the homing act and nothing else; the standing edit surface is NOT widened by it. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. The edit is ADD-ONLY: no existing line of the arc plan is modified or deleted. WHAT THE RULING DID NOT DO: it settled the OWNER and did not ratify the entry as correctly recorded, so the 'NOT ratified' sentence above still stands and the entry stays in the ratification queue. FORMER HOME, PRESERVED (#12): `docs/back_half_design.md:147-150`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `process` entry (the register's own home rule): heading line 129, section "## §4 — The re-grounded back half (derived order)", label "“§4”", delegated null, delegation "named in no user-ratified surface", states_rules null, verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Method, standing for every slice (the lesson that paid off thrice): scope the cause\nbefore building.** Decompose the slice structural / fitted / ceiling (the key-emission\nprobe is the template); build the structural lever; route fitted to Stage 5; route\nceiling to accepted-ambiguity or flag it as a possible B-trigger. Derive, don't assert." Provenance — the wave and its dispatch — is recorded in this field and NOT in the contract text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-564 — Correction of record: the 'function-only' share of the legacy residual was overstated, because over-grabbed segmentation corrupts the BASS and not only the pitch-class window

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **★ CORRECTION OF RECORD TO THE CAVEAT ABOVE — THE FUNCTION-ONLY SHARE IS OVERSTATED, BECAUSE
> OVER-GRABBED SEGMENTATION CORRUPTS THE BASS AND NOT ONLY THE PITCH-CLASS WINDOW (2026-07-10; the
> record states no ratifier).** The apportionment above books a share-tone class as function-only on

**In plain words.** An earlier classification held that a particular family of errors could not be fixed by better segmentation, because the two competing readings contain the same pitch classes. The paper simulation refuted that on its own test case: a stretch that reaches too far picks up a bass note that does not sound where the error is, and the bass is what separates the two readings. So part of what had been booked as needing a later layer is resolvable earlier.

**Why.** Found by the desk simulation before any measurement was built, which the record states is exactly what that stage exists for: the prior was written down, traced by hand at the score, and refuted cheaply. The magnitude of the separating term on the named case is in the document's own trace (**D-431**).

**Status.** LIVE · decided 2026-07-10 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:910-912`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_eg2_scoping.md`, the first work item opened under the Premise Gate (Cowork, 2026-07-10, session 36). Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's *ledger update from the desk sim*, marked evidence rather than a surprise-at-build because the explorational stage admits surprises (`CLAUDE.md`, the scope clause under #17–#19). Sharpens the failure-population premise the same document carries. **Its subject is the LEGACY path's residual**, which is why the entry is marked. The record states no ratifier. ★ HOMED 2026-08-07 (CC, the licensed homing wave, executing the user's ruling R2 of 2026-08-07, dispatch `cc_instruction_licensed_homing_and_oi344.md` §0a — the LICENSING class of finish-line item 1's re-home set, homed under the edit-surface licence the user ruled on the same date). Written into `CLAUDE.md` gate block (D), as the correction of record to the cross-layer-budget caveat it corrects, in that section's own voice and with its defense. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. FORMER HOME, PRESERVED (#12): `cowork_eg2_scoping.md:138-143`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `process` entry (the register's own home rule): section "## §5 Written predictions — ★ RECORDED at the desk sim (2026-07-10, BEFORE any probe exists)", label "“§5 Written predictions”", verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Ledger update from the desk sim (recorded as evidence, not surprise-at-build):** the §4 prior\nfor `bwv352@1440` (\"share-tone cannot move without the intended selection\") was WRONG — the O1\n\"function-only residual\" classification partially conflates legacy segmentation artifacts:\nover-grab corrupts not only the pc window but the BASS, so part of the presumed-L5 residual is\nL2-resolvable. This sharpens P5 and is exactly the class of discovery the desk-sim stage exists\nto make cheaply (explorational scope).". Provenance is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, its date and its ratifier where the record states one, and its defense.

### D-568 — The two-track remedy: the chord axis is completed by hand-built rules, the key axis by soft-evidence quality and calibration — and NOT by a wider search on either

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **★ AND WHEN THAT PRECISION WORK OPENS, THE TWO AXES TAKE DIFFERENT MEDICINE — AND NEITHER TAKES A
> WIDER SEARCH (homed here 2026-08-07 on the user's ruling; decided 2026-06-20, the record states no
> ratifier). ⚠ LEGACY subject — the two-axis pipeline this was derived on is superseded on both axes by
> the joint estimator; the rule is recorded as the work-programme statement it is, not as a description
> of what runs.**
> The stages above fix the ORDER of work. This fixes what KIND of work each axis gets when the order
> reaches it. **The CHORD axis is hand-buildable:** finish the competition rules that decide between
> competing readings, and dissolve the compensation gates into that competition. **The KEY axis is
> soft-evidence QUALITY plus CALIBRATION, and is not hand-buildable:** raise the precision of the
> evidence fed in — the cadence channel first, because it is the highest-leverage input and feeds
> several layers — then let the joint combination's SOFT integration resolve what remains, with
> calibration and possibly a learned emission for the residual floors. **Neither axis is improved by a
> fancier lattice or a wider search.** *Why:* measured on both sides. On the key side the scoped joint
> search was measured to move a fraction of a percent of stretches and to come out slightly negative
> overall, which is what located the value of the joint combination in its evidence integration rather
> than in its search — the same finding the shelving above records, from its other end. On the chord
> side the residual was re-attributed by measurement and most of it turned out to need a candidate that
> was never surfaced at all, which is a rules problem and not a re-weighting one. The structural and
> cross-cutting findings that sat beside this verdict fed the architecture review rather than this plan.

**In plain words.** The two halves of the problem need different medicine. Getting the chord right is a matter of finishing the rules that decide between competing readings. Getting the tonality right is a matter of the quality of the evidence fed in and how well its confidence is calibrated. Neither is improved by searching harder over more candidate readings.

**Why.** Measured on both sides. On the key side the scoped joint search was measured to move a fraction of a percent of stretches and to be slightly negative overall, so the value of the joint combination was located in its evidence integration rather than its search. On the chord side the residual was re-attributed by measurement, and most of it turned out to need a candidate that was never surfaced at all — a rules problem, not a re-weighting one.

**Status.** LIVE · decided 2026-06-20 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_engage_arc_plan.md:155-173`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_audit_obligation_map.md`, the phase-1 synthesis of the per-layer audits. Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's own §E, *the two-track remedy*. The search half is carried independently at **D-026** (the global joint-lattice decode measured inert, 2026-06-29) and this is its antecedent on the scoped search, with the chord half beside it. The figures are the document's own (**D-431**). The record states no ratifier. **Its subject is the LEGACY two-axis pipeline**, superseded on both axes by the joint estimator; the entry is marked accordingly. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that this governs no single layer and that §2.14 states the inference shape rather than a work programme. The user ruled it A WORK-PROGRAMME RULE, and the arc plan owns the ORDER OF WORK — the same ground as the D-539 ruling — so it is written into `cowork_engage_arc_plan.md`, beside the Stage-5 paragraph that opens the precision work this rule governs. ★ THE USER'S RULING IS ITSELF THE AUTHORIZATION FOR THIS ONE EDIT of that contract document, exactly as it was for D-539; `cowork_engage_arc_plan.md` remains outside every standing licence and NO standing edit surface is widened by it. Written in the contract's own voice, with its defense and with the ⚠ LEGACY subject stated — the two-axis pipeline the verdict was derived on is superseded on both axes — so the rule is read as the work-programme statement it is and not as a description of what runs. The edit is ADD-ONLY: no existing line of the arc plan is modified or deleted. FORMER HOME, PRESERVED (#12): `cowork_audit_obligation_map.md:171-179`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 161, "section": "## D. CROSS-CUTTING findings (architecture-level, for phase-2)", "label": "“D. CROSS-CUTTING findings”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "## E. The two-track remedy (the actionable verdict for the eventual inference work)
- **Chord-axis track = hand-buildable:** competition-rule completion (C1) + gate-dissolution (C2); floor → B.
- **Key-axis track = SOFT-EVIDENCE QUALITY + CALIBRATION (NOT a joint search — measured inert, K3):** fix K1
  (cadence precision) FIRST (highest leverage, feeds 3 layers; clears ~42% of modulation FPs + the K1b
  in-layer over-extension covers more) → then the joint combination's SOFT integration (K3) resolves K2;
  calibration + possibly a learned emission for the partial-sig / dim7 floors. **NOT hand-buildable rules,
  and NOT a fancier lattice/search** (the scoped joint moves <0.3% of regions, net negative — CC-measured).
- Structural (S1–S3) + cross-cutting (X1–X3) feed the **phase-2 architecture review** (decomposition +
  interactions), which uses this map." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-576 — The corpus root-agreement measurement UNDERSTATES the real-world quality impact of a wrong key, because root and bass are largely key-independent

> A chord's root and its bass note are **largely
> key-independent**: both can be named correctly while the key label is wrong. So the root-agreement
> percentage barely moves when the tonality is misread — while the chord's **quality**, its **Roman
> numeral** and some of its **inversions** are all corrupted by that same misreading. The corpus
> measurement therefore reports **less damage than a reader or listener would see**

**In plain words.** A chord's root and its lowest note can both be named correctly while the key is wrong. So a measurement built on root agreement barely moves when the tonality is misread — but the quality of the chord, its Roman numeral and some of its inversions are all corrupted. The measurement therefore reports less damage than a listener or reader would see.

**Why.** Measured at the case that shows it: the anchor piece was systematically mis-keyed while the root-agreement baseline did not expose it, and the failures that did expose it were the notation tests asserting chord symbols and Roman numerals. The document draws the general conclusion from that contrast.

**Status.** LIVE · decided 2026-05-23 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:511-515`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** ★ RE-HOMED 2026-08-04 on the user's ruling (READ WAVE 5, dispatch `cc_instruction_reads_5.md` §0a ruling R3): the caveat is recorded BESIDE THE FIGURES IT QUALIFIES, in `CLAUDE.md` gate block (A), which is the surface that publishes them — the same act phase 1j performed for the four grading conventions in the same block. The verbatim and home above are re-taken there; the entry's class moves from `gap` to `project-convention`, because the concern is how ANY root-governed figure is read and gate block (A) is where that is owned. **THE FORMER VERBATIM, PRESERVED (#12)** — quoted from `docs/key_detection_baroque_partial_signature.md:121-127` as it stood: "**Why the Baroque BIR baseline (27/23) doesn't expose it:** BIR measures root-pc / bass-is-root agreement, which is largely **key-independent** — a chord's root/bass can be right while the key label is wrong. The wrong key corrupts **quality** (F vs Fm), **Roman numerals**, and some **inversions** — exactly what the Corelli *notation* tests assert (chord symbols + romans), which is why they catch it while BIR does not. So the corpus metric understates the real-world quality impact for Baroque material." **THE FORMER HOME, PRESERVED:** docs/key_detection_baroque_partial_signature.md:121-127. **THE FORMER PROVENANCE SENTENCE, PRESERVED:** `docs/key_detection_baroque_partial_signature.md`, the 2026-05-23 read-only investigation and its resolution banner. Read in full by READ WAVE 4, 2026-08-04. Recorded in the document's own scope section. Unlike **D-575** this is a statement about a MEASUREMENT and not about the legacy key path, so it is not legacy-scoped: it bears on how any root-governed figure is read, including the granularity-robust unit, whose Roman-numeral and key columns are tracked beside the root for a related reason (**D-115**, **D-211**). The record states no ratifier. *(The original 2026-05-23 investigation document is unchanged and remains the evidence the block now cites; what moved is where the RULE is recorded, not where the measurement that produced it lives. The record still states no ratifier for the DECISION, and the 2026-08-04 act supplies none — what the user ruled is where it is written down.)*

### D-579 — The anchor obligation: compute the chord ONCE against its region's FINAL notes, with the tonality as an explicit input rather than frozen mid-pipeline

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> 3. **★ ANCHOR — compute the chord ONCE against final region tones, with the key as an explicit input [BS, DEEP]**
>    `[CC sixth issue, VERIFIED]`. This composes the old S2 (chord-identity ≠ final-region) and the frozen-key
>    half of X2 into the single highest-leverage structural obligation. Re-layer so: segmentation → final tones →
>    chord(key) — the chord is a clean function of its final region AND the key is an explicit variable, not
>    frozen into `basisIndep` mid-pipeline. This is what makes a joint fixpoint *possible*; it unblocks BOTH steps
>    5 and the eventual joint-key activation. The deepest structural fix; measure-gated.

**In plain words.** The old pipeline named the chord before its stretch of music was finished being assembled, and it baked in the tonality before the competition between readings ran. The fix is to order it properly — settle the stretch, then its notes, then decide the chord with the tonality passed in as an ordinary input. Only then is the chord a clean function of what it is a chord of.

**Why.** Its position in the order is argued rather than asserted: the review places it first among the deep fixes because both of the other structural obligations depend on it — readings cannot be folded into a competition whose stretches are still being mutated underneath it, and no joint settling is possible while the tonality is frozen before the chord is chosen. The two halves were verified verbatim at the committed object, including the source's own comment that the joint re-key runs once with no fixpoint and cannot re-emit the chord.

**Status.** SUPERSEDED IN FACT · decided 2026-06-20 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phase2_architecture_review.md:127-132`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“§5”** — `## §5 — The structural fix-first ORDER (the phase-2 deliverable)` (heading at line 108). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_phase2_architecture_review.md`, the phase-2 architecture review (Cowork-led, reconciled against CC's empirical pass at committed HEAD `a03c2493bb`). Read in full by READ WAVE 4, 2026-08-04. **Its subject is the LEGACY multi-pass pipeline**, which the joint estimator replaced on both surfaces. Recorded as step 3 of the review's fix-first order, marked its anchor. **The obligation was met by replacement rather than by repair**: the production arm is now one joint decode over key, mode, chord and segmentation together (**D-001**), which is the ordering this step asked for arrived at by a different route. Recorded *superseded in fact* — no ruling names it. The record states no ratifier.

### D-581 — Information not yet consumed is NOT automatically a defect: every site is classified preserved-awaiting-consumer, lost, should-already, or unclear — and unclear is recorded for adjudication, never guessed

> Not-yet-consumed information is **NOT automatically a defect.** Every site is classified as one of:
>
> - **OK — PRESERVED, awaiting a future/dormant consumer.** Intact and carried; simply not consumed *yet* because
>   its consumer (e.g. Layer 5) is not built yet. Correct forward-provisioning — records the engage-ready substrate.
> - **DEFECT — LOST.** Destroyed / overwritten / collapsed / dropped so **no** consumer — present OR the
>   architecture-intended future one — can recover it. (The Gate A case: a distinct alternative overwritten by a
>   near-duplicate.)
> - **DEFECT — SHOULD-ALREADY.** Preserved/available, but a consumer that **already exists and should be using it now**
>   does not receive it (a routing/wiring gap).
> - **UNCLEAR — consumer-status ambiguous.** Not guessed (#1); recorded for user adjudication.

**In plain words.** A fact the analysis produces and nothing currently reads is not by itself a fault. It may be correctly held for a stage not yet built. So each such site gets one of four verdicts: it is intact and waiting; it has been destroyed so that nothing could ever recover it; it is intact but a reader that exists today is not being given it; or which of those it is cannot be told, in which case that is what gets written down.

**Why.** It is the user's binding rule for the sweep, and its work is to stop a proactive audit manufacturing findings: without it every forward-provisioned fact reads as waste. The fourth verdict is what keeps it honest in the other direction — guiding principle #1 forbids guessing, so an ambiguous consumer status is recorded as ambiguous rather than resolved by the auditor.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_information_loss_audit.md:15-24`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“The central classification axis”** — `## The central classification axis (the user's binding rule)` (heading at line 13). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_information_loss_audit.md`, the engage-arc-#4 information-loss catalogue (Cowork, 2026-07-06; every hit verified at code by CC). Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's own central classification axis, marked *the user's binding rule*. It is the operational form of principle #12 turned from accidental into a systematic sweep, which the document states as its purpose.

### D-582 — A collapse that is RECOMPUTABLE from what is kept is not information loss — not every collapse is a defect

>     **★ THE RECOMPUTABLE CLAUSE ABOVE REACHES EVERY COLLAPSE, NOT ONLY AN EXCLUSION (2026-07-06;
>     the record states no ratifier).** The *unless* is written for exclusion evidence; it holds for
>     **any** collapse of several values into one. A collapse is a loss only when the several cannot

**In plain words.** Reducing several numbers to one is only a loss if the several cannot be got back. Where the reduced value is derived deterministically from something that is still carried, nothing has gone: it can be recomputed on demand. This is the guard that stops the audit flagging every summary as a fault.

**Why.** Stated with the two cases that establish it: a confidence squashed through a fixed function whose input is carried, and a boolean that is exactly a comparison of a carried number against a threshold. The document names its own purpose — guarding against over-flagging — and it is the qualification `CLAUDE.md` principle #12 already carries in its own text (*unless the exclusion is recomputable from what is kept*).

**Status.** LIVE · decided 2026-07-06 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:56-58`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** `cowork_information_loss_audit.md`, the engage-arc-#4 information-loss catalogue (Cowork, 2026-07-06; every hit verified at code by CC). Read in full by READ WAVE 4, 2026-08-04. Recorded as form (+2) of the document's taxonomy, one of three forms the sweep's own evidence added to the a–i list it started from. The record states no ratifier. ★ HOMED 2026-08-07 (CC, the licensed homing wave, executing the user's ruling R2 of 2026-08-07, dispatch `cc_instruction_licensed_homing_and_oi344.md` §0a — the LICENSING class of finish-line item 1's re-home set, homed under the edit-surface licence the user ruled on the same date). Written into `CLAUDE.md` principle #12, as the clause that generalizes the recomputable-collapse `unless` beyond exclusion evidence to every collapse, in that section's own voice and with its defense. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. FORMER HOME, PRESERVED (#12): `cowork_information_loss_audit.md:127`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `project-convention` entry (the register's own home rule): section "## Taxonomy coverage (the a–i forms swept + the new forms the code revealed)", label "“Taxonomy coverage”", verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "| **(+2) recomputable-collapse** *(new — a collapse that is NOT a loss)* | ✓ | **K5** (sigmoid), **K6** (`uncertain` flag) — a hard value derived from a **carried** source (or deterministically regenerable) is lossless; not every collapse is a defect. Guards against over-flagging. |". Provenance is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, its date and its ratifier where the record states one, and its defense.

### D-600 — The quality-overwrite information-loss violation is TOLERATED until the gate-dissolution step and stays VISIBLE in the open-items register — tolerated is not forgotten

> Two post-scoring passes change the chord quality the scorer committed and keep no record of what
> they replaced, which is an information-loss violation (#12). **The verdict is to TOLERATE it until
> the gate-dissolution step, with the violation kept VISIBLE in the open-items register — tolerated is
> not forgotten.** *Why, as a derivation from three principles rather than a preference:* removing the
> overwrites now would be a production behaviour change with no replacement owner, since no component
> yet owns deciding quality from the key — which is the cross-layer patch layer adherence forbids
> (#7); and #8 puts the structural work first. Deferring to the step that gives the concern a single
> home makes the removal ONE ratified, revertible change under the regression stop (#14/#15). The
> alternative — ripping the overwrites out now — was considered and rejected on exactly that ground.
> **The open-items register row is the mechanism that makes this an acceptance rather than an
> oversight**, and it gates the dissolution.

**In plain words.** Two later passes change the chord quality the chord stage committed and keep no record of what they replaced, which is information loss. It is left in place for now rather than ripped out, because there is no other component yet that owns deciding quality from the key, and removing it now would be a patch across stages. The violation is kept on the open-items list so that leaving it is a decision and not an oversight.

**Why.** Stated as a derivation from three principles and recorded as such: removing the overwrites now would be a production behaviour change with no replacement owner, which is the cross-layer patch layer adherence forbids; tolerating it until the step that gives the concern a single home makes it one ratified, revertible change under the regression stop. The alternative considered and rejected is recorded with it.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1227-1237`

**Provenance.** `cowork_adjudication_dossier.md`, the 2026-07-10 user-directed adjudication of the structural audit's open rows and the siloed-fact findings. Read in full by READ WAVE 5, 2026-08-04. The dossier records this as the ONE genuine acceptance among the seven rows — the six others were pure rule applications — RATIFIED by the user 2026-07-10. ⚠ The subject is the LEGACY chord path's post-scoring passes; the joint estimator that now produces the committed reading does not run them. Whether the acceptance still has a subject at HEAD is NOT stated here and is not asserted. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii), whose table routes this document PER ENTRY to the subject's owning section). The subject is this surface's own post-scoring passes, so the standing scoring-surface family rule sites it at `docs/scoring_model.md` §8, the section that exists to collect this surface's constraints and dead ends, with the ⚠ LEGACY subject and the not-asserted clause both stated at the new home. THE OPEN-ITEMS ROW IDENTIFIER IS NOT WRITTEN INTO THE SPECIFICATION TEXT — the rule states that a register row is what makes the toleration an acceptance, and the row's identity stays in this field, because a row identifier written into a governing document goes stale silently. FORMER HOME, PRESERVED (#12): `cowork_adjudication_dossier.md:59-60`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 14, "section": "## Part A — the seven audit adjudications, in plain language", "label": "“Part A”", "delegated": null, "delegation": "CLAUDE.md:164", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12), AND IT IS WHERE THE ROW IDENTIFIER REMAINS ON THE RECORD: "**⚖ Verdict (#7/#8/#14):** (ii). The violation stays VISIBLE in the register (OI-10, gating
the dissolution) — tolerated is not forgotten." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-601 — Before any constant that would make two differently-scaled confidences comparable is fitted, the premise that a fitted constant CAN do so must itself pass a premise ledger and a desk simulation

> **A5. S19 — two confidence numbers on different scales compared as if equal.** One number is
> bounded 0–1, the other is an unbounded sum (observed up to ~25); the override bar compares
> them directly — like comparing meters with feet. This is the already-registered T1-3, and it
> is now HARD-GATED (EG-4): before anyone fits the conversion constants, the premise "a fitted
> constant CAN make these scales commensurable" must itself pass a #17 ledger + desk sim —
> because the one calibration attempted so far failed (non-monotone).

**In plain words.** Two confidence numbers in the program are on different scales — one runs from zero to one, the other is an unbounded total — and a comparison between them treats them as the same kind of quantity. Fitting a conversion factor is not allowed to be the first move: the assumption that any single factor could make the two comparable has to be written down as a premise and traced by hand first, because the one attempt at such a calibration did not behave monotonically.

**Why.** Measured: the one calibration attempted failed, and it failed non-monotonically — which is evidence against the premise itself rather than against the particular constant, since a monotone relationship is what a single conversion factor would have to express. That is why the gate is on the PREMISE and not on the fit.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_adjudication_dossier.md:69-74`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“Part A”** — `## Part A — the seven audit adjudications, in plain language` (heading at line 14). Not reached: the document's delegation is graded before any section question arises. Decided by **D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit**.

**Provenance.** `cowork_adjudication_dossier.md`, the 2026-07-10 user-directed adjudication of the structural audit's open rows and the siloed-fact findings. Read in full by READ WAVE 5, 2026-08-04. Recorded as adjudication A5, whose verdict is that the audit's own question is superseded by this gate, which is stricter than either alternative the audit offered. It is the specific instance of **D-267**/**D-268** (two admissible confidence classes; a confidence is compared only within its class and a declared frame) that the audit found violated, and of **D-269** (the frame table is the one home of the override arithmetic). The record states the gate but no ratifier for it by name. ★ HELD, NOT HOMED, 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii), which routes this document PER ENTRY to the subject's owning section). ITS SIBLING D-600 WAS HOMED IN THE SAME ACT; this one is held, and the reason is a LICENCE rather than a judgment. **THE OWNER IS DETERMINATE:** the subject is a comparison between two confidence quantities on different scales and the gate placed on fitting a conversion between them, and **D-269** — which this entry is an instance of — records that the frame table in `cowork_confidence_contract.md` is the ONE home of the override arithmetic, with each frame declared before its site is built. That document is a contract home and the concern is squarely its section's. **BUT IT IS OUTSIDE EVERY STANDING EDIT AUTHORIZATION** — the autonomous-operation block licenses `src/composing/`, one notation bridge file and `ARCHITECTURE.md`; this wave's own ruling additionally names `docs/scoring_model.md` as a destination; no ruling in force names `cowork_confidence_contract.md`. Widening an edit surface is the act the record reserves to the user (`tools/audit/decisions/item1_rehome_blocker.json` states it in those words — *"widening is a scope question and it goes back to the user"*), so writing into that contract on a session's own reading would take a surface the user has not granted. **THE SECOND CANDIDATE WAS CHECKED AND IS OUTSIDE THE SAME LINE:** the gate is recorded as a Stage-3 entry gate, whose home is `cowork_engage_arc_plan.md` — a ratified contract document the user has licensed for ONE named edit before (D-568, D-539) and which no ruling licenses here. So the entry stays where it is and comes back to the user with the owner named, which is the dispatch's stated outcome for a held entry. Its document is therefore NOT retired from the classifier's authored set. NOTHING WAS WRITTEN for this entry: no home text, no class change, no status change.

### D-604 — A defensible modal reading the major/minor ground truth cannot represent is a GROUND-TRUTH LIMITATION, not a defect to optimise away

> - **A DEFENSIBLE MODAL READING THE MAJOR/MINOR GROUND TRUTH CANNOT REPRESENT IS A GROUND-TRUTH
>   LIMITATION, NOT A DEFECT TO OPTIMIZE AWAY** (user, 2026-06-22). Where our analysis emits a mode
>   the published human annotation has no way of writing down — the annotation records major and
>   minor only — a resulting disagreement is a limit of the ground truth, not an error of the analysis.
>   **Do not chase the major/minor ground truth on a modal reading**, and do not tune such a case
>   away: doing so makes the analysis worse in order to match a notation limit. *Why:* measured on
>   the affected population — the large majority of the jazz key misses are perfect-fifth
>   displacements where our reading is a defensible modal one, which places them inside the layer's
>   own done-criterion (defensible-or-flagged on an ambiguous case) and inside the stated scope
>   caveat that the ground truth is major/minor only. **Distinct from the exotic-mode convention
>   above**, which decides how a modal emission is SCORED; this decides what a REMAINING disagreement
>   means. Distinct also from the separate rule governing what the key layer may EMIT. It is
>   principle #21 applied at the point of reading: the ground truth is an instrument, and a
>   disagreement it cannot represent is not evidence about us.

**In plain words.** Most of the apparent key errors on jazz material are not errors: the program reads a mode the published human annotation has no way of writing down, because that annotation records only major and minor. Reading such a case as a mistake and tuning it away would make the analysis worse in order to match a notation limit.

**Why.** Measured on the affected population: roughly sixty-nine per cent of the jazz misses are perfect-fifth displacements where the reading is a defensible modal one. That places them inside the layer's own done-criterion, which admits a defensible-or-flagged answer on an ambiguous case, and inside the stated scope caveat that the ground truth is major/minor only.

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:704-717`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_layer3_keymode_impl_design.md`, the Layer-3 key/mode implementation design. Read in full by READ WAVE 5, 2026-08-04. Recorded inside the same *user, 2026-06-22* metric block. It is a ground-truth-capacity statement of exactly the kind `CLAUDE.md` #21 governs — ground truth is an instrument too — and it bears on how any key-axis residual is read. Distinct from **D-210**, the ratified grading convention that reduces an exotic mode to its parent collection's minor key: that convention decides how a modal emission is SCORED; this decides what a remaining disagreement MEANS. Distinct also from **D-344**, which governs what the layer may EMIT. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Ruled a GRADING CONVENTION and homed in `CLAUDE.md` gate block (A), beside the conventions already homed there — the same treatment D-486, D-602 and D-603 received. Written in the gate block's own voice, with its defense, and with the two distinctions the record insists on: from the exotic-mode grading convention, which decides how a modal emission is SCORED, and from the separate rule governing what the key layer may EMIT. The D-645 licence covers `CLAUDE.md` for homing acts, so no new authorization was needed. The edit is ADD-ONLY: no existing line of `CLAUDE.md` is modified or deleted. FORMER HOME, PRESERVED (#12): `cowork_layer3_keymode_impl_design.md:88-92`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 82, "section": "## §4 — Metric / gates (Increment C — the behavior-changing one)", "label": "“§4”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "Crucially, **distinguish a rotation DEFECT from a
modal-GT LIMITATION**: ~69% of Jazz "misses" are perfect-fifth displacements where our reading is a *defensible
modal* one (e.g. `G-mixolydian`) the major/minor ground truth cannot represent — those are NOT defects to optimize
away (the done-criterion's "defensible-or-flagged on ambiguous", + the major/minor-GT scope caveat). Do not chase
the major/minor GT on modal readings." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-608 — The symmetric-root spelling pin's entry premise was measured FALSE — it is unreachable because the scorer rarely chooses the diminished quality; the remedy is enumerated and NOT decided

> - **The G4/C1 symmetric-root spelling-pin's ENTRY PREMISE is false — it is effectively unreachable,
>   and the remedy is enumerated and NOT decided (D-608).** The pin only runs once the scorer has
>   already called the sonority diminished. On the great majority of diminished-seventh sonorities it
>   has not: the scorer either declines to commit or names the chord something else, so the mechanism
>   almost never fires. That it would fire was an assumption and was never written down as one.
>   *Why:* measured at the probe and traced at the code — of the diminished-seventh sonorities in the
>   primary corpus most abstain, and of those that commit the scorer chooses major or minor far more
>   often than diminished. A contributing fact is recorded with it: the four-note diminished-seventh
>   type is deferred, so the diminished reading competes as a triad-plus-bonus against complete triads

**In plain words.** The mechanism that picks the correctly-spelled rotation of a symmetric diminished-seventh chord only runs if the scorer has already called the chord diminished. It usually has not — on the great majority of such sonorities the scorer either declines to commit or calls the chord something else — so the mechanism almost never runs. The assumption that it would was never written down as one.

**Why.** Measured at the probe and traced at the code: of the diminished-seventh sonorities in the primary corpus most abstain, and of those that commit the scorer chooses major or minor far more often than diminished. A contributing fact is recorded with it — the four-note diminished-seventh type is deferred, so the diminished reading competes as a triad-plus-bonus against complete triads with bass support and usually loses. The second gate was separately desk-verified sound where it is reached.

**Status.** LIVE · decided 2026-07-10 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1873-1881`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_eg1_premise_checks.md:21-22`; former verbatim: “**Gate 1 is the blocker.** The design premise — *"on a symmetric dim7 sonority the scorer's
chosen quality is Diminished"* — was an unlabeled ASSUMPTION, and the probe measured it FALSE:” — `cowork_eg1_premise_checks.md`, the read-only at-code premise checks written before the EG-1 build (2026-07-10). Read in full by READ WAVE 5, 2026-08-04. Recorded as premise check PC-1. Its own text marks the remedy ENUMERATED, NOT DECIDED and assigns it to the owning layer, with three named options each owing its own premise ledger and desk simulation. ⚠ The mechanism is in the dormant Layer-4 decoder, not in the joint estimator that now runs; whether the production arm has the same shape is NOT stated here and is not asserted. The record states no ratifier. This is a founding case for `CLAUDE.md` #17(a): the premise was load-bearing, checkable and unlabelled.

### D-609 — The abstention rate rides on an arbitrary, never-fitted seed constant — a whole probe's metric-moving behaviour sat downstream of an unestablished value

> - **The abstention rate rides on an arbitrary, never-fitted SEED CONSTANT (D-609).** How often G1
>   declines to commit is governed by one number set by hand as a starting value and never fitted, so
>   every quantity measured downstream of the ladder depends on an unestablished value (#19). *Why:*
>   established at the code — the constant is a seed in the decoder's own header, and the control flow
>   was traced to show that everything not committed and not inherited abstains, including a case that
>   is sufficient but falls under the margin; the consequence was then measured, a substantial share of
>   scored duration abstaining under it.

**In plain words.** How often the chord stage declines to commit is governed by one number that was set by hand as a starting value and never fitted to anything. Everything the probe measured therefore depends on a value nobody has established.

**Why.** Established at the code: the constant is a seed in the decoder's own header, and the control flow was traced to show that everything not committed and not inherited abstains — including a case that is sufficient but falls under the margin. The consequence was then measured: a substantial share of scored duration abstains under it.

**Status.** LIVE · decided 2026-07-10 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1883-1889`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_eg1_premise_checks.md:55-57`; former verbatim: “1. The abstain rate rides on **`uncertaintyMargin` = 0.5 — an arbitrary, never-fit Tier-3 seed**
   (`chordslicedecoder.h:174`). The metric-moving behavior of the whole EG-2 probe sits
   downstream of an unestablished constant.” — `cowork_eg1_premise_checks.md`, the read-only at-code premise checks written before the EG-1 build (2026-07-10). Read in full by READ WAVE 5, 2026-08-04. Recorded as the first of three ledger facts under premise check PC-2. ⚠ The constant is in the DORMANT Layer-4 decoder. The third fact recorded beside it — that a ratified abstain-aware stop convention was owed before any abstaining path could be adoption-gated — is **D-212**, ruled and enforced two days later, and is not re-entered here (#6). The record states no ratifier.

### D-615 — Under #19 the validation basis of every Iter-era hand-set scoring magnitude is retroactively VOID — the values are unfalsified, not established

> **Nearly every live scoring magnitude on this surface was hand-set, and the only check that ever
> validated it was a regression gate later proven to under-count true per-onset root error by a large
> factor and to have been reading a then-buggy ground-truth parser. Under #19 the validation basis of
> these values is therefore retroactively void: they are UNFALSIFIED, NOT ESTABLISHED.** *Why the
> reading is "unestablished" rather than "wrong", which is a different claim and the record supports
> only the first:* the same audit measured a third of the reachable constants inert at the root
> objective, and both high-leverage re-fit candidates regressed held out. So nothing here says the
> values are bad; what it says is that nothing in the record shows they are good. The under-count
> factor and the inert fraction are in the audit that measured them and are not restated (D-431).

**In plain words.** Almost every number in the chord scorer was set by hand, and the only thing that ever checked those numbers was a measurement later shown to miss most of the real error and to have been reading a faulty reference. So the check they passed does not establish them. They may still be good values — nothing here says they are bad — but nothing in the record shows that they are.

**Why.** It follows from the establishment principle applied backwards, and the audit states the mechanism rather than asserting the conclusion: the only instrument that ever graded these values was later measured to under-count the true per-onset root error by a factor of fifteen to fifty-six and to have been reading a ground-truth parser since fixed. The audit also records what bounds the alarm — one third of the reachable constants were measured inert at the root objective, and both high-leverage re-fit candidates regressed held-out — so the reading is 'unestablished', not 'wrong'.

**Status.** LIVE · decided 2026-07-10 · ratifier not stated

**Home.** `docs/scoring_model.md:1279-1287`

**Provenance.** `cowork_l1_l5_premise_debt_audit.md` Tier 2, the retroactive premise ledger commissioned by the user immediately after ratifying `CLAUDE.md` #17-#19 (2026-07-10). Read in full by READ WAVE 6, 2026-08-04. The audit's Tier-1 and Tier-3 findings are already tracked as the Stage-3 entry-gate rows `OPEN_ITEMS.md` OI-1 through OI-7 and are not re-entered here (#6); this Tier-2 statement is the one that no row carries as a standing consequence. The record states no ratifier. ⚠ The magnitudes it describes are the LEGACY chord scorer's; the joint estimator is the production inference layer (**D-001**), and whether its fitted tables inherit the same standing is NOT stated here and is not asserted. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii), which routes this document PER ENTRY to the subject's owning section). The subject is the standing of the magnitudes ON THIS SCORING SURFACE, so the standing scoring-surface family rule sites it at `docs/scoring_model.md` §8 — the document that specifies those magnitudes and whose §8 collects its standing constraints. The ⚠ LEGACY subject and the not-asserted clause about the estimator's fitted tables are both written into the home text. THE PARAMETER-LOCATION LIST IS NOT CARRIED ACROSS: it is a pointer into a manifest and into this document itself, so restating it at the new home would be a second copy of a list the file already is (#6). THE UNDER-COUNT FACTOR AND THE INERT FRACTION ARE NOT RESTATED (D-431). FORMER HOME, PRESERVED (#12): `cowork_l1_l5_premise_debt_audit.md:63-67`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 61, "section": "## Tier 2 — the Class-B MASS: live constants tuned against instruments later proven broken", "label": "“Tier 2”", "delegated": null, "delegation": "cowork_engage_arc_plan.md:69", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12), AND IT IS WHERE THE UNDER-COUNT FACTOR REMAINS ON THE RECORD: "**Nearly every live scoring magnitude was hand-set in the Iter/B-era (pre-2026-06-13), and its
only validation instrument was the batch BIR gate + catalog/snapshot pins — the gate later
proven to under-count true per-onset root error ~15–56× and to sit on a then-buggy GT parser.**
Under #19 the validation basis of these values is retroactively void: they are *unfalsified,
not established*. The set (locations per `tools/param_manifest.json` + `docs/scoring_model.md`):" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-619 — Over-claiming a constraint as HARD re-creates the override failure in reverse — and a sounding note is not automatically a chord tone

> - **Over-claiming a constraint as HARD re-creates the override failure in reverse, and a sounding
>   tone is not automatically a chord tone.** Evidence splits into constraints that disqualify
>   readings outright and scores that only lean. A hard constraint is safe precisely because no amount
>   of soft evidence can overturn it — which is exactly what makes a mis-declared one unrecoverable, a
>   wrong certainty forcing a wrong answer. Whether a sounding pitch belongs to the chord is therefore
>   never a raw fact: the same four sounding pitches may be one chord with an added fourth or a chord
>   with a suspension that resolves away, so chord membership is decided inside the analysis rather
>   than before it. *Why:* it follows from what the split is FOR, and the worked case is the defense —
>   a sounding set that admits two readings cannot be a constraint on either.

**In plain words.** Treating a judgment as if it were a fact is as damaging as letting a global guess overrule the notes — it just fails in the other direction, with a wrong certainty forcing a wrong answer. Which notes belong to the chord is one of those judgments: the same four sounding pitches can be one chord with an added note or a chord with a note that resolves away.

**Why.** The reason is derived from what the hard/soft split is FOR, and stated with the rule: a hard constraint is safe precisely because no amount of soft evidence can overturn it, which is exactly what makes a mis-declared one unrecoverable. The worked case is the defense — the same sounding set admits two readings, so chord membership cannot be a raw fact.

**Status.** LIVE · decided 2026-06-15 · ratifier not stated

**Home.** `ARCHITECTURE.md:450-458`

**Provenance.** `docs/architecture_joint_inference.md` §5, the calibration precondition. Read in full by READ WAVE 6, 2026-08-04. ⚠ The document is superseded as an architecture proposal (`ARCHITECTURE.md` §2.14; the ratified estimator is **D-001**), and this clause is not a proposal but a constraint on how any evidence is classified — it is the general form of the demotion **D-618** records for one specific candidate. The record states no ratifier. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). ★ ASSUMPTION A4 DISCHARGED BY READING: the supersession was read at `ARCHITECTURE.md:960-961` and reaches the proposal's SHAPE, not this classification rule, which is therefore LIVE. Routed to the joint-estimator section of `ARCHITECTURE.md`, where it leads the subsection because the two measurements beside it are instances of it. FORMER HOME, PRESERVED (#12): `docs/architecture_joint_inference.md:83-89`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 81, "section": "## §5 — The calibration precondition (the load-bearing skill)", "label": "“§5”", "delegated": null, "delegation": "ARCHITECTURE.md:858", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "Getting \"hard\" right is the whole game. **A sounding note is not automatically a chord tone** — a C-E-G
with an F may be an added-fourth chord or an F suspension to be explained away. So the truly hard
constraints are the **raw facts** + the genuinely-unambiguous analyses; chord-tone-vs-non-chord-tone is
itself part of the soft/joint analysis operating *within* those facts. **Over-claiming \"hard\" on a soft
case re-creates the override problem in reverse** — a wrong constraint pinning a wrong answer." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-620 — The reading-shaped evidence producers were each measured to pin WRONG and must stay SOFT — a cadence anchor, a modulation detector and a bass-is-root rule are scores, never constraints

> - **Three reading-shaped producers were each measured to pin WRONG and must stay SOFT: a
>   cadence-based tonic anchor, a modulation detector, and the rule that the lowest sounding pitch is
>   the chord's root.** Each was tested for how often the reading it would force is the wrong one, and
>   all three came back with error rates that disqualify them from ruling anything out. *Why:* the
>   classification of an evidence source as decisive or merely suggestive is measured against the
>   ground truth rather than assumed from how authoritative the source sounds — which is the rule
>   above run over the candidate set. The rates are in the record that measured them (D-431).
>   **⚠ LEGACY SCOPE:** the three producers named are legacy-era mechanisms, so the measurements are
>   of those producers and are not claims about the estimator specified above; what carries forward is
>   the verdict that a reading-shaped producer is a score and never a constraint.

**In plain words.** Three mechanisms that each produce a candidate reading were tested for how often the reading they force is wrong: a cadence-based tonic anchor about two times in five, a modulation detector about half the time, and the rule that the lowest note is the chord's root about one time in five. None of them may rule a reading out; all three may only lean.

**Why.** Measured per producer, which is the whole point of the check: the classification of each evidence source as decisive or merely suggestive was tested against the ground truth rather than assumed from how authoritative the source sounds, and all three reading-shaped producers came back with error rates that disqualify them from ruling anything out. This is the safety measurement **D-619** demands, run over the candidate set.

**Status.** LIVE · decided 2026-06-15 · ratifier not stated

**Home.** `ARCHITECTURE.md:469-478`

**Provenance.** `docs/architecture_joint_inference.md`, the status block's investigation findings. Read in full by READ WAVE 6, 2026-08-04. ⚠ The document is superseded as an architecture proposal (`ARCHITECTURE.md` §2.14; **D-001**), but these are measured error rates rather than a proposal, and no other home carries them. The bass-is-root value is the measured counterpart of **D-585**, which admits the bass prior as a tie-break only; the cadence value sits beside **D-290**, the falsification of the local key-agnostic cadence approach. The record states no ratifier. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). ★ ASSUMPTION A4 DISCHARGED BY READING: the supersession at `ARCHITECTURE.md:960-961` reaches the proposal's shape, not these measurements, which are LIVE and homed. Routed to the joint-estimator section of `ARCHITECTURE.md` beside the rule they instantiate. TWO THINGS ARE STATED AT THE NEW HOME RATHER THAN LEFT IMPLICIT: the three RATES ARE NOT CARRIED ACROSS (D-431) — the verdict is, the numbers stay in the record — and a **⚠ LEGACY SCOPE** mark rides along, because the three producers named are legacy-era mechanisms and the measurements are of them, not of the production estimator. FORMER HOME, PRESERVED (#12): `docs/architecture_joint_inference.md:16-17`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 1, "section": "# Architecture — Constrained Joint Inference (the back-half target)", "label": "the opening block (above the first section heading)", "delegated": null, "delegation": "ARCHITECTURE.md:858", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12), AND IT IS WHERE THE THREE RATES REMAIN ON THE RECORD: "> - **The reading-shaped producers are correctly SOFT** — measured to pin WRONG: cadence anchor 44%,
>   modulation detector 53%, bass-is-root 17–23%. They must be soft scores, never hard constraints." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-624 — The hard bound and the score start are SAFETY CAPS for a loop that never settles — never the amount of context a layer needs

> **The hard bound and the score start are SAFETY CAPS for a loop that never settles — never the
> amount of context this layer needed (D-624; re-homed into this specification 2026-08-04 from the
> design document that formerly carried it — the register records which).** The backward loop has two stops that are not answers: a
> maximum distance, and the beginning of the piece. Neither reports how much context the analysis
> required; each only terminates a loop that would otherwise not terminate, and a cap that fired may
> never be read as the discovered amount. *Why:* the amount of context a layer needs is **discovered
> by convergence and never chosen**, so this distinction is what keeps that rule intact — without it a
> cap would silently become the answer in exactly the cases where the loop failed to settle.

**In plain words.** The loop that reads backwards for context has two stops that are not answers: a maximum distance, and the beginning of the piece. Neither of them says how much context the analysis needed — they only stop a loop that would otherwise not stop.

**Why.** It follows from the rule the caps sit beside and is stated as the distinction that keeps that rule intact: the amount of context is discovered by convergence and never chosen, so a cap that terminated the loop cannot be read as the discovered amount. Without the distinction the cap would silently become the answer whenever it fired.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1623-1630`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_layer3_reachback_design.md:83-84`; former verbatim: “- **Hard bound + score start:** a maximum reach (a small number of measures — a setting) and the score's first tick
  both terminate the loop. These are **safety caps for "never settles," not the needed amount.**” — `cowork_layer3_reachback_design.md` §3. Read in full by READ WAVE 6, 2026-08-04. It guards **D-261**'s no-guessing rule at the one place a guess could re-enter — a terminating cap read as the needed amount — and it is why the loop reports the boundary rather than silently truncating (the L1 contract's `boundaryReached`). The record states no ratifier.

### D-628 — The finest meaningful extension step is the change-point — within a slice the sounding set is constant, so a finer request loads no note and changes no answer

> **The finest meaningful extension step is the CHANGE-POINT — a finer request loads no note and can
> move no answer (D-628; re-homed into this specification 2026-08-04 from the design document that formerly
> carried it — the register records which).** When a consumer asks this model to reach further into the
> score, the smallest request worth making is one that reaches the next change-point. *Why:* it
> follows from what a Layer-2 slice **is** — the stretch over which the eligible sounding-note set is
> constant — so a request that ends inside a slice is *provably* a no-op rather than merely a small
> one: no note enters the model and no downstream answer can differ. That makes the granularity bound
> a **fact about the representation**, not a tuning choice, and it is what bounds the step-size
> question the requesting layer owns.

**In plain words.** Between two points where the sounding notes change, nothing about the music changes, so asking to load a little more music that stops inside such a stretch brings in no new notes and can move no answer. The smallest request worth making therefore reaches the next point of change.

**Why.** It follows from what a slice IS — the stretch over which the set of sounding notes is constant — so a request ending inside one is provably a no-op rather than merely a small one. That is what makes the granularity bound a fact about the representation rather than a tuning choice, and it bounds the step-size question the requesting layer owns.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1470-1478`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_layer1_extend_design.md:32-34`; former verbatim: “The **finest meaningful step is the change-point/slice**: within a slice the sounding set is
  constant, so a sub-change-point (beat/tick) extension loads no new note and changes no analysis — requesters never
  ask finer than that.” — `cowork_layer1_extend_design.md` §2. Read in full by READ WAVE 6, 2026-08-04. It bounds **D-262**, which puts the increment size in the requesting layer's hands in its own natural scale: this says the scale has a floor below which no request can matter. The record states neither a date nor a ratifier.

### D-630 — Minimality sets the default and the burden — do not add a component; a new one is earned only by exhibiting a residual class a separable criterion resolves

> **Minimality sets the default and the burden.** Do not add a box. The resolver is presumed to be Layer 5 unless part 1
> or part 3 exhibits a residual class resolved by a separable, non-function criterion. The burden is on finding that
> class; absent it, no new box.

**In plain words.** When it is unclear whether a job needs a component of its own, the answer is no until somebody shows a class of cases that some other kind of evidence settles on its own. The proof obligation sits with adding the component, never with declining to.

**Why.** It follows from the layer-identity invariant, which the document applies as its decisive test: a component exists to own one pairing of evidence source and question, so a proposed component with no evidence source of its own has nothing to own. Placing the burden on the addition is what makes the test decidable rather than a matter of taste, and the investigation records what would have discharged it and did not.

**Status.** LIVE · decided 2026-06-24 · ratified by user

**Home.** `cowork_uncertain_resolver_investigation.md:31-33`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_uncertain_resolver_investigation.md`, the O1 investigation, RESOLVED and user-ratified 2026-06-24. Read in full by READ WAVE 6, 2026-08-04. Stated as the lens the investigation applies before its own evidence, so the verdict **D-629** is the rule's first application rather than its source. It is the structural companion of **D-033**: that says what a layer owns, this says what it takes to create one.

### D-635 — Reach-back is a REAL product requirement, currently MASKED by the whole-score load — it must land WITH selection-based loading or selection-edge key inference breaks

> **Reach-back is a REAL product requirement, currently MASKED by the whole-score load — it must land
> WITH selection-based loading (D-635; re-homed into this specification 2026-08-04 from the
> disposition record that formerly carried it).** The shipped program analyses the stretch a user has
> selected; the whole-score path exists for offline measurement. Reading backwards before the
> selection begins is therefore genuinely needed, and the only reason its absence costs nothing today
> is that the note model still loads the whole score anyway. **Narrowing Layer 1 to load only the
> selection WITHOUT also engaging this facility would break key inference at the start of every
> selection** — the two changes are one change. *Why:* derived rather than asserted — a selection is a
> subset in time, so the evidence establishing the key at its opening lies *before* it, and the
> efficiency fix removes exactly that evidence. This corrects an earlier reading that called the
> requirement moot; that reading described the current whole-score stopgap rather than the design.

**In plain words.** The shipped program analyses the stretch of music a user has selected, not the whole piece; the whole-piece path exists only for offline measurement. Reading backwards before the selection begins is therefore genuinely needed, and the only reason its absence causes no trouble today is that the note reader still loads everything anyway. Making the note reader load only the selection without also building the backwards read would break key inference at the start of every selection.

**Why.** Corrected against an earlier reading that called the requirement moot, and the correction is what makes the entry load-bearing: the earlier framing described the current whole-score stopgap rather than the design. The dependency is derived rather than asserted — a selection is a subset in time, so the evidence establishing the key at its opening lies before it, and the efficiency fix removes exactly the accident that supplies that evidence today. The document also states the bound: chord identity is local, so nothing here gates the chord layer's build.

**Status.** LIVE · decided 2026-06-24 · ratifier not stated

**Home.** `ARCHITECTURE.md:1632-1642`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_delta_check_dispositions.md:74-83`; former verbatim: “- **Widen / reach-back — a REAL product requirement, currently unbuilt and currently masked (corrected
  2026-06-24).** The shipped product is **selection-based**: it analyses the user's selected range, never the whole
  score (the whole-score path is only the offline batch-testing harness). A selection is a temporal **subset**, so L3
  genuinely needs to **reach back before the selection's start** to read the established key at the leading edge
  (analyse measures 20–40 and the key at m.20 needs the context before m.20). So widen is **needed by design**, not
  speculative. It is currently **unbuilt**, and currently **masked** only because L1 still loads the whole score (the
  §11 inefficiency) — so the pre-selection context happens to be in memory and reach-back is not yet exercised. When
  L1 is fixed to load only the selection (the §11 efficiency fix / selection-based working model), **reach-back must
  land with it**, or selection-edge key inference breaks.” — `cowork_delta_check_dispositions.md`, the Layer-1 disposition, verified at the source by Cowork directly. Read in full by READ WAVE 6, 2026-08-04. The capability has since been BUILT and gated off by default (**D-623**), so what remains owed is the coupling this entry names: the two must be switched together. ⚠ Whether the joint estimator's own production path carries the same dependency is NOT stated here and is not asserted. The record states no ratifier.

