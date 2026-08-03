# The 27 decisions pending ratification (D-255…D-281) — complete entries

> **GENERATED REVIEW AID (Cowork, 2026-08-02).** Found by the phase-1d enumeration wave (21 of
> 145 documents read in full; the measured remainder is the second partition). Entered with
> status from the record only — RATIFICATION IS YOURS. Rendered by the register's own entry
> renderer. Highest-stakes entries: D-278 (the joint key-and-chord step SHELVED WITH EVIDENCE,
> recorded only in a design document — the 3.1b failure shape) and D-266 (a live prohibition on
> resuming Layer 6, sitting where no session-start read opens).


## Group K — Documentation governance

### D-255 — Every design document follows one fourteen-section structure, synthesized from three published standards

> **Standing convention (user, 2026-06-22):** every architecture/design document in this project follows the
> section structure below — a synthesis of **arc42** (the 12-section architecture template) and **IEEE 1016**
> (Software Design Descriptions) + the viewpoints idea of **ISO/IEC/IEEE 42010**. Two arc42 sections —
> **Deployment view** and **Human-interface design** — are **N/A** for our backend analysis modules (no separate
> hardware/runtime deployment; no UI); each doc states that omission once rather than padding.

**In plain words.** Every architecture or design document in this project uses the same section order, taken from arc42, IEEE 1016 and ISO/IEC/IEEE 42010. The two arc42 sections that do not apply to a backend analysis module - deployment view and human-interface design - are declared not applicable once per document instead of being padded out.

**Why.** The sources are cited with the decision: arc42 (the 12-section architecture template), IEEE 1016 (Software Design Descriptions) and the viewpoints idea of ISO/IEC/IEEE 42010 (cowork_design_doc_template.md:4-9) - published standards rather than an invented house style, which is principle #1 applied to documentation.

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Home.** `cowork_design_doc_template.md:3-7`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** cowork_design_doc_template.md:3 states it as a standing convention with the ratifier and date in the text. CLAUDE.md's Conventions entry names this file as the ONE home for writing standards and names this structure among what it carries, so the decision is correctly homed and was simply never in the register. Found by the phase-1d enumeration wave, 2026-08-02.

### D-256 — Every design document opens with one of four declared status banners

> ## Status-banner convention
> Each doc opens with a one-line status: **DRAFT for sign-off** / **SIGNED (date)** / **AS-BUILT (date + commits)** /
> **SUPERSEDED (→ pointer)**. The all-documentation-in-sync standing rule applies: when the code or a decision
> changes, the doc moves with it.

**In plain words.** A design document states its status in one line at the top: draft for sign-off, signed with a date, as-built with a date and commits, or superseded with a pointer to what replaced it. When the code or a decision moves, the document moves with it.

**Why.** Stated with the rule: it binds the all-documentation-in-sync standing rule (#10) to a visible per-document marker, so a reader can tell at a glance whether what they are reading is a proposal, a ratified contract, or a superseded record.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_design_doc_template.md:75-78`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** cowork_design_doc_template.md:75-78, stated as a convention in the file CLAUDE.md's Conventions entry names as the ONE home for writing standards; no date or ratifier is stated at this home. Found by the phase-1d enumeration wave, 2026-08-02.

### D-257 — A specification carries a locator to its code and tests; code mechanics never do the explaining

> straight from the architecture to the code and to the tests that protect it. The locator **stays** (user, 2026-06-24).
> What is *not* allowed is code **mechanics** doing explanatory work in the prose — function/type/variable names used to
> *explain the algorithm*, code formulas, or commit hashes woven into the reasoning. The line: the algorithm is
> described in plain architect/music-theory language; the *pointer to where it lives* is a short, clearly-marked
> reference, not prose.
> - **Implementation locator** — the headers and `.cpp` files — in Section 3 (Context & scope), as a labelled pointer.
> - **Test locator** — the unit-test file(s) and any corpus/property validation tool — in Section 10 (Quality &
>   testing).
> (Deferred for layers not yet built; added when they are. A layer mid-rebuild names its current location, marked as
> such. User mandate 2026-06-22, refined 2026-06-24.)

**In plain words.** A specification names the files that hold its implementation and the files that hold its tests, as a short labelled pointer, so a reader can go from the architecture straight to the code. What is not allowed is code mechanics doing the explanatory work: function, type and variable names used to explain the algorithm, code formulas, or commit hashes woven into the reasoning. The algorithm is described in plain architectural and music-theory language.

**Why.** The line is drawn in the rule itself (cowork_design_doc_template.md:84-86): a pointer to where something lives is a reference, while naming code to explain the algorithm makes the prose unreadable to the musician the documentation standard requires it to serve (register entry D-124, the readable-by-a-musician rule).

**Status.** LIVE · decided 2026-06-24 · ratified by user

**Home.** `cowork_design_doc_template.md:82-91`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** cowork_design_doc_template.md:82 ('The locator stays (user, 2026-06-24)') and :91 ('User mandate 2026-06-22, refined 2026-06-24'). Homed in the file CLAUDE.md's Conventions entry names as the ONE home for writing standards, which names the implementation/test locator rule among what it carries. Found by the phase-1d enumeration wave, 2026-08-02.


## Group T — Standing process rules and local patches

### D-258 — A prune and tidy pass runs before any publish of the fork, and nothing on its list is acted on before it

> **Standing deferral (user, 2026-06-22):** "back up now, tidy up files we don't want to publish later." This is the
> running list of prune/tidy decisions to make **before any publish** of the fork (`origin = slimvince/MuseScore`).
> Nothing here is to be acted on now — it is the to-do for the prune pass. Keep appending as items arise.

**In plain words.** Files that should not be published are listed as they are found and dealt with in one pass before the fork is published; the list is appended to as items arise, and nothing on it is acted on in the meantime.

**Why.** The reason is stated with the deferral: backing the work up to the fork now is worth more than keeping the fork publishable at every moment, so the publishability question is batched into one pass rather than paid per commit. Related: register entry D-197, the distribution constraint.

**Status.** DEFERRED · decided 2026-06-22 · ratified by user

**Home.** `cowork_prune_pass_checklist.md:3-5`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** cowork_prune_pass_checklist.md:3 records it as a standing deferral in the user's own words ('back up now, tidy up files we don't want to publish later'), with the date and ratifier stated. Status is DEFERRED because the record says the pass has not run (:5 - 'Nothing here is to be acted on now - it is the to-do for the prune pass'). Found by the phase-1d enumeration wave, 2026-08-02.

### D-259 — Every upstream contribution is checked against the distribution constraint before it is posted

> ## 6. Standing guard (not a prune item — a permanent rule)
> - **Any** upstream GitHub comment / PR / contribution must be checked against the CLAUDE.md distribution constraint
>   **before** posting. A draft carrying a fork-local-constrained patch (`cfc7eb5e39`, #9444) is a **HARD STOP** — never
>   post. Non-constrained reports (e.g. #24673) are the user's normal call.

**In plain words.** Any comment, pull request or contribution aimed at the upstream MuseScore project is checked against the distribution constraint first. A draft carrying the fork-local import-fix patch is a hard stop and is never posted; a contribution carrying none of it is an ordinary decision for the user.

**Why.** The instance that produced it is recorded in the same file (cowork_prune_pass_checklist.md:7-18): a draft comment for the upstream issue was written carrying the constrained patch's content, before the constraint existed, and survives in the fork's history. The rule generalizes the one-patch prohibition into a pre-post check on every upstream contribution.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_prune_pass_checklist.md:43-46`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** cowork_prune_pass_checklist.md:43 states it as 'a permanent rule' explicitly distinguished from the prune items around it; no date or ratifier is stated at this home. It operationalizes register entry D-197, the ratified distribution constraint, by naming the check that has to happen and when. Found by the phase-1d enumeration wave, 2026-08-02.


## Group C — Cross-cutting analysis contracts

### D-260 — Analysis output covers exactly the selection; everything loaded beyond it is evidence, never a result

> **Invariant.** The analysis output covers **exactly the selection**; everything outside it is evidence, never a
> result.

**In plain words.** The user's selection is the output span: labels are emitted only for it. Music loaded from outside the selection is pulled in as evidence for judging the selection's edges and is never itself labelled.

**Why.** Stated with the rule (cowork_bounded_context_design.md:21-26): the shipped product analyses the part of the score the user selected, and a layer often needs evidence from outside it to judge its edges. Separating the output span from the loaded span is what lets a layer read more music without changing what the user asked to have analysed.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:43-44`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3 carries the status banner 'SIGNED (user, 2026-07-02)'; the invariant is stated at :43-44. The cross-cutting bounded-context bullet of ARCHITECTURE.md points at this document as the ONE cross-layer extension spec (:10). Found by the phase-1d enumeration wave, 2026-08-02.

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

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; the rule is items 5 and 6 of the bounded-context contract at :57-69. Found by the phase-1d enumeration wave, 2026-08-02.

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

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; item 8 of the bounded-context contract at :73-81. Found by the phase-1d enumeration wave, 2026-08-02.

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

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; item 10 of the bounded-context contract at :82-86, marked '(merged 2026-07-02)' from the killed duplicate contract document. Found by the phase-1d enumeration wave, 2026-08-02.

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

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; the equivalence invariant at :121-126, with the step-size independence obligation restated as a required test at :202-204. Found by the phase-1d enumeration wave, 2026-08-02.

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

**Provenance.** cowork_bounded_context_design.md:3, status banner 'SIGNED (user, 2026-07-02)'; stated at :115-120 and again as an architecture decision at :188-189 ('recorded so the forward-only contract is not read as forbidding extension'). Bears on register entry D-025, the forward-only rule with two scoped escapes. Found by the phase-1d enumeration wave, 2026-08-02.

### D-266 — Layer 6 is prohibited until the bounded-context design is coded and regression-tested for Layers 1 to 5

> ## §11 Acceptance (the L6 gate — user directive 2026-07-02)
>
> 1. This design **ratified** (it was never signed; sign-off is now the first step).
> 2. **Coded, L1–L5:** L1 build-selection + extend seam (interim rebuild allowed, §8); L2 re-slice-on-extend (done);
>    L3 reach-back activated as this design's request (from gated-off) ; L4's request-or-truncate path (uncoded today,

**In plain words.** The grouping layer's track does not resume until this cross-layer design is ratified, implemented across Layers 1 to 5, and regression-tested against the listed acceptance conditions - including the equivalence invariant, step-size independence, denial provenance, termination, and byte-identity of the whole-score degenerate case against the corpus gate.

**Why.** The reason is the design's own opening argument (cowork_bounded_context_design.md:14-16): the whole-score assumption is foundational, so building more layers on it bakes it deeper and unwinding it afterward is a cross-cutting, expensive retrofit. Gating the next layer on the contract being real, not merely written, is what stops that.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_bounded_context_design.md:213-217`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_bounded_context_design.md:3-4 records it in the status banner as 'THE GATE (user directive, same day)', and the acceptance list is the numbered section at :213-223. Found by the phase-1d enumeration wave, 2026-08-02.

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

**Provenance.** cowork_confidence_contract.md:3, status banner 'RATIFIED (user, 2026-07-02)'; the two classes at :25-34. The contract names its architecture home as the cross-cutting contracts section (:6), where register entry D-032 records the boundary rule this classification underpins. Found by the phase-1d enumeration wave, 2026-08-02.

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

**Provenance.** cowork_confidence_contract.md:3, status banner 'RATIFIED (user, 2026-07-02)'; rules U1 to U5 at :36-48. Rule U2 is the one already registered, as D-032, at its ARCHITECTURE.md home; U1, U3, U4 and U5 were not in the register. Found by the phase-1d enumeration wave, 2026-08-02.

### D-269 — The frame table is the one home of the override arithmetic; a new override site declares its frame before it is built

> **New frames require declaration here.** Any future override site (e.g. the A-4 cadence-less confirmation channels;
> the recognition consumer's schema-contradiction override, `cowork_progression_schema_design.md` §2) must add its
> frame row to this section before build — an undeclared cross-layer comparison is a contract violation.

**In plain words.** Every place where one layer's contradiction strength is compared against another layer's confidence is a declared frame - a triple of incumbent confidence, contradiction measure, and the conversion that makes them comparable - and all of them live in one section. Any future override site must add its frame row there before it is built; an undeclared cross-layer comparison is a contract violation.

**Why.** It is principle #6 (one path per concern) applied to the override arithmetic: the contract exists because the same comparison was being re-stated with different semantics at each site. Stating it once, with each instance's conversion declared, is what makes the threshold interpretable rather than an arbitrary scale factor.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `cowork_confidence_contract.md:83-85`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_confidence_contract.md:3, status banner 'RATIFIED (user, 2026-07-02)'; the rule at :83-85, over the frame definition and the two built instances at :63-81. Found by the phase-1d enumeration wave, 2026-08-02.


## Group A — The estimator architecture — the joint estimator

### D-270 — The held-out evaluation protocol - five-fold cross-validation grouped by ground-truth analysis file

> 2. **The split: 5-fold cross-validation [prov-ratify] over the 326 WiR-covered pieces, grouped by
>    WiR analysis file.** The 326 pieces resolve to 324 distinct analysis files (`docs/score_inventory.md`
>    — some chorales share an analysis); pieces sharing an analysis file share a fold (leakage guard).
>    Fold assignment is generated once with a fixed, committed seed and committed as a stamped artifact
>    (`tools/` + manifest, the #17f pattern); it never changes across fit events (a re-split is a
>    protocol amendment).
> 3. **Everything fitted is fitted inside the training folds only** — the generative tables, the
>    combination weights, AND the fitted structure choices: the degree vocabulary's count threshold and
>    pooling, the smoothing constants, the L2 penalty. Model selection (λ, thresholds) uses inner
>    validation within the training folds; the held-out fold is touched exactly once, by the final
>    fitted model of that fold.

**In plain words.** Evaluation splits the 326 ground-truth-covered pieces into five folds, grouped so that pieces sharing one ground-truth analysis file share a fold. Fold assignment is generated once from a fixed committed seed and never changes. Everything fitted - the tables, the weights, and the fitted structure choices such as the vocabulary threshold, the smoothing constants and the penalty - is fitted inside the training folds only; the held-out fold is touched exactly once, by that fold's final model.

**Why.** The protocol names what it prevents (cowork_prefit_gates.md:25-28): a headline figure graded on data that helped fit it, including the subtle forms - a vocabulary derived from all-corpus counts, a smoothing constant chosen on the grading data, a threshold checked against the final metric. The grouping rule is a stated leakage guard: some chorales share an analysis file.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:32-42`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols including the marked constants, dated 2026-07-19; the held-out protocol at :23-60. It is the protocol form of register entry D-097, which states the general rule at its ARCHITECTURE.md home. Found by the phase-1d enumeration wave, 2026-08-02.

### D-271 — The capacity budget - a cell keeps its own estimate only above a stated count, and free parameters are bounded against the training tokens

>    table, its dimensions, its raw cell-count histogram from the training data, and the resulting free
>    parameter count. No prose-only budget.
> 2. **Budget rule:** a table cell keeps its own maximum-likelihood estimate iff its training count
>    ≥ 20 [prov-ratify]; below that it is pooled to its declared parent class (the pooling hierarchy
>    declared per table in the artifact) under additive smoothing with a single declared α per table.
>    The degree vocabulary's rare-class pooling (factorization §1) is the same rule applied to the state
>    space itself.
> 3. **Global sanity bound:** total effective free parameters ≤ training tokens / 10 [prov-ratify],
>    verified in the artifact. The combination-weight vector stays ≤ 14 weights, L2-penalized, per the
>    ratified staged-fitting decision. *(Amended ≤ 12 → ≤ 14 by user ratification 2026-07-19 at the
>    weight-fit dispatch: the ratified factorization gives the four cadence features their own fitted
>    weights, putting the enumerated vector at 12–13; the amendment is the lawful #22 path — capacity
>    impact nil, thousands of training tokens per weight either way. Original text: "≤ 12 weights (one
>    per factor plus the declared-mode strength)".)*

**In plain words.** Before any fit, the parameter inventory is published as a generated artifact: every table, its dimensions, its raw cell-count histogram and its resulting free-parameter count. A table cell keeps its own maximum-likelihood estimate only if its training count reaches twenty; below that it is pooled into its declared parent class under smoothing. Total effective free parameters stay at or below one tenth of the training tokens, and the combination-weight vector stays at or below fourteen weights with a penalty.

**Why.** The protocol names what it prevents (cowork_prefit_gates.md:64-65): overfitting in one shot on a 326-piece single-composer corpus, and hand-picking hidden inside the words 'derived from counts'. Publishing the inventory as a generated artifact before fitting is principle #17(f) applied to the fit itself - the budget cannot be asserted in prose after the fact.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:68-81`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols including the marked constants, dated 2026-07-19; the capacity budget at :62-96, with the twelve-to-fourteen weight amendment recorded in place at :77-81 as a lawful protocol amendment. Found by the phase-1d enumeration wave, 2026-08-02.

### D-272 — The protocol constants are protocol, not tuning - changing one is an amendment, never a fitting act

> Provisional numeric choices inside the protocols (fold count, cell-count threshold, confidence level)
> are marked **[prov-ratify]** — they become binding at ratification but remain protocol constants, not
> fitted values; changing one later is a protocol amendment (#22), not a tuning act.

**In plain words.** The numeric choices inside the pre-fit protocols - the fold count, the cell-count threshold, the confidence level - become binding when the protocols are ratified but remain protocol constants rather than fitted values. Changing one later is a governance amendment, not an act of tuning.

**Why.** It closes the route by which a governance constant becomes a knob: without the distinction, a fold count or a pooling threshold could be moved in response to a disappointing measurement and the move would look like ordinary calibration. The document states the same rule twice (cowork_prefit_gates.md:5-6 and :17-19), once for the ratification and once for the constants themselves.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:17-19`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:17-19 states the rule and :3-6 records its ratification, dated 2026-07-19. It applies principle #22 (a hard gate declares in advance how it handles the largest change it will meet), registered as D-185, to the pre-fit protocols. Found by the phase-1d enumeration wave, 2026-08-02.

### D-273 — The architecture-adoption variant of the hard regression stop, written before any diff existed

> 3. **Adoption PASS requires ALL of:**
>    - **(i) Held-out:** A's key-agree vs the LOCAL key exceeds the current baseline beyond the
>      piece-bootstrap CI on every preset; root-agree and RN-agree do not degrade beyond the CI (#24 —
>      a difference within the CI is not a finding, in either direction). **(i-b) The modulation-rate
>      guard:** A's key changes per piece sit within 0.75×–1.25× of the ground truth's rate. **The
>      key-HOME column is TRACKED with a mandatory explained decomposition** against the computed GT

**In plain words.** Adopting an architecture replacement in place of the incremental hard stop requires all of: the held-out key agreement against the local key beating the baseline beyond the stated confidence interval on every preset with root and Roman-numeral agreement not degrading beyond it; a modulation-rate guard keeping key changes per piece within a quarter of the ground truth's rate; a net decrease in the class-(b) root-disagree duration on every preset with every added failing run enumerated, classified and individually diagnosed; class-(a) tracked; and user ratification of the whole record as one revertible commit that re-baselines the reference.

**Why.** The protocol names what it prevents (cowork_prefit_gates.md:100-103): negotiating the hard stop on a live diff. The incremental non-increase ratchet was written for incremental change, and an architecture replacement moves runs in both directions by design - so the exceptional-event variant is written while no diff exists, which is principle #22's requirement (register entry D-185).

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:116-121`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols, dated 2026-07-19; the adoption protocol at :98-145, with the home-column amendment recorded in place at :123-129 as a lawful pre-measurement amendment. The event it governed is the OI-178 adoption, whose outcome is in the CLAUDE.md gate block. Found by the phase-1d enumeration wave, 2026-08-02.

### D-274 — The reverse map - if the new estimator is not adopted it is removed whole, and the retirement map is void

> 5. **The reverse map (if A is not adopted):** A's module is removed whole (one revertible commit), the
>    fold/fit artifacts are kept as measurement history, and the retirement map is void — declared now
>    so non-adoption has a lawful exit too.

**In plain words.** Non-adoption has a declared lawful exit, written at the same time as the adoption path: the new module is removed in one revertible commit, the fold and fit artifacts are kept as measurement history, and the retirement map that would have deleted the superseded code never executes.

**Why.** It is principle #23 (an end-state principle needs a lawful transition) applied in both directions: the sanction that permits two paths for one concern must say how the duplication ends whichever way the decision goes, so that a declared migration state cannot quietly become a permanent one.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:189-191`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols, dated 2026-07-19; the reverse map is item 5 of the dual-path sanction at :189-191. Register entry D-095 records the sanctioned dual path itself at its ARCHITECTURE.md home. Found by the phase-1d enumeration wave, 2026-08-02.


## Group B — The notation output surface and the record path

### D-275 — Every published record carries its own instrument provenance; a provenance-less analysis cannot exist

> Every published record carries its instrument provenance: the embedded table set's source-artifact
> hashes and the selected weight-vector identity (both compiled in per Decision D1), plus the
> decoder's version. A consumer — and any future measurement — can always answer "which fitted
> values produced this analysis" from the record itself; a provenance-less analysis cannot exist.

**In plain words.** Each record published for the notation path carries the source-artifact hashes of the fitted table set, the identity of the selected weight vector, and the decoder's version. A consumer, or any later measurement, can always answer which fitted values produced a given analysis from the analysis itself.

**Why.** It is principle #16 (every measurement stamped to its corpus and its tooling) applied at the record level rather than at the measurement level: an analysis that has left the module can otherwise no longer be attributed to the values that produced it, which makes any later reproduction check impossible.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `cowork_notation_output_contract.md:54-57`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_notation_output_contract.md:3 records the user's ratification, dated 2026-07-26, as specified and without amendments; the provenance rule at :52-57. Found by the phase-1d enumeration wave, 2026-08-02.

### D-276 — Modal colour is published as un-rounded per-degree counts; no mode label is inferred or published anywhere

> For each key run and each scale degree 1..7 of its key: the sounding duration and onset count of
> EVERY chromatic inflection of that degree actually observed in the run (computed from the
> published L1 note facts relative to (tonic, mode)). This is the whole publication — counted,
> un-rounded, nothing hand-set: minor's variable 6̂/7̂ (Dorian color, subtonic-vs-leading-tone),
> major's lowered 7̂ (Mixolydian color) or raised 4̂ (Lydian color), and every borrowing appear as
> their actual counts. The presentation layer may FORMAT a reading from it ("Dorian-leaning"); the
> published fact is the counts, with establishment status (§5.4). No 21-value mode label is
> inferred or published anywhere (C1); the two-mode key plus this table informationally dominates
> the retired labels (#12).

**In plain words.** For each key run and each scale degree, the record publishes the sounding duration and onset count of every chromatic inflection of that degree actually observed. That is the whole publication - counted, un-rounded, nothing hand-set - so minor's variable sixth and seventh, major's lowered seventh or raised fourth, and every borrowing appear as their actual counts. A presentation layer may format a reading from it; no twenty-one-value mode label is inferred or published.

**Why.** The reason is stated with the decision (cowork_notation_output_contract.md:146-147): the two-mode key plus the count table informationally dominates the retired mode labels, so publishing counts rather than a label loses nothing (#12) while removing an inference nobody had established. Register entry D-054 records the twenty-one-mode vocabulary this supersedes on the record surface.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `cowork_notation_output_contract.md:139-147`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_notation_output_contract.md:3 records the user's ratification, dated 2026-07-26, as specified and without amendments; the modal reading at :137-147. Found by the phase-1d enumeration wave, 2026-08-02.


## Group S — The guiding principles

### D-277 — Measure before build - and a byte-identical structural refactor is exempt, because byte-identity is its prediction

> **★ MEASURE-BEFORE-BUILD (ratified 2026-07-07, arc #12 lesson) — since 2026-07-10 the MIDDLE stage of the
> #17 Premise-Gate funnel: desk-simulate (hours) → read-only probe (a session) → build (an arc).** Every
> Stage-3+ item additionally owes a #17 premise ledger (FACT/THEORY/ASSUMPTION), a written quantitative
> prediction per assumption, and a desk simulation over known failing cases BEFORE its probe or build is opened
> (see CLAUDE.md #17–#19 + `cowork_premise_gate_reflection.md`). Byte-identical structural refactors are exempt
> from the prediction requirement — byte-identity IS their prediction. A build whose case rests on an *anticipated*

**In plain words.** A build whose case rests on an anticipated precision gain is measured read-only before it is built. The gate applies to precision claims - will building this make the analysis more correct - and not to structural refactors, which are justified by cleanliness and verified byte-identical, owing no precision measurement. A byte-identical structural refactor is exempt from the written-prediction requirement because byte-identity is its prediction.

**Why.** The exemption's reason is stated with the rule (cowork_engage_arc_plan.md:101-113): the requirement exists to stop a precision claim being built before it is checked, and a refactor that must come out byte-identical has already stated its falsifiable prediction. The instance that produced the gate is recorded beside it - the joint key-and-chord step, measured not to pay before it was built.

**Status.** LIVE · decided 2026-07-07 · ratified by user

**Home.** `cowork_engage_arc_plan.md:97-102`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** cowork_engage_arc_plan.md:3 records the user's ratification of this plan, dated 2026-07-07; the gate at :97-102, amended 2026-07-10 to become the middle stage of the Premise-Gate funnel (:128-130). The CLAUDE.md principles provenance paragraph names this gate, in this file, as a companion standing rule; register entry D-189 records the funnel it sits in. Found by the phase-1d enumeration wave, 2026-08-02.


## Group C — Cross-cutting analysis contracts

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

**In plain words.** The separate joint key-and-chord decision was measured before being built and does not pay: about a tenth of a percentage point net over roughly 6200 stretches, with harm at three quarters to nine tenths of the correction, an oracle ceiling under a percentage point, and a firing rate of 1.4 per cent. The cause is that the carried alternative keys are siblings within one collection, so the chord is almost always stable across them. It drops off the build inventory.

**Why.** The measurement is stated with the shelving, and so is the principle #12 reconciliation: the key alternatives ARE carried, so the key discovery is not discarded; the chord under an alternative key is never computed in this path, so nothing computed is discarded; and the measured 1.4 per cent where it would differ is even-odds noise. Choosing not to compute a measured-worthless possibility is an evidence-based decision, not information loss.

**Status.** SHELVED WITH EVIDENCE · decided 2026-07-07 · ratified by user

**Home.** `cowork_engage_arc_plan.md:103-112`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_engage_arc_plan.md:3 records the user's ratification of this plan, dated 2026-07-07; the shelving at :103-112, with the measurement cited to its report and the no-information-loss reconciliation stated in place. Found by the phase-1d enumeration wave, 2026-08-02 - the class this audit exists for: a shelving with evidence, recorded only in a design document.


## Group T — Standing process rules and local patches

### D-279 — The Stage-3 entry gate - seven conditions before any engagement wiring reaches production

> **★ STAGE-3 ENTRY GATE (ratified 2026-07-10 with #17–#19; evidence `cowork_l1_l5_premise_debt_audit.md`).**
> Before any E4/L5 engagement wiring can reach production:
> - **(EG-1) Tier-1 defusal is a PREREQUISITE, not an inventory item:** the resolver selection re-ordering
>   (arc #9 — the as-built `resolveAbstained` still selects progression-first at confidence 1.0, the channel

**In plain words.** Before the rebuilt path's wiring can reach production, seven conditions hold: the two measured-harmful mechanisms are defused or provably bypassed; the go/no-go measurement runs under the full Premise Gate with its measurement tool established first; the pedal reader waits on its underpowered premise being settled; the confidence-commensurability premise owes a ledger and a desk simulation before any threshold is fitted; the fit surface is completed; the Jazz preset's validation status is declared honestly; and no step opens until every layer it depends on has passed its audit.

**Why.** Each condition names the measurement or the absence that produced it (cowork_engage_arc_plan.md:66-92): the override measured at minus 756, the missing establishment record for the decode chain, the pedal premise at agreement 0.20 to 0.50 on two to five cases, and the failed calibration that stands as the warning against assuming a fit will repair an incoherent quantity. It is principle #18 at architecture scale - new construction may not carry load on unaudited foundations.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `cowork_engage_arc_plan.md:64-67`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_engage_arc_plan.md:64 states the gate as 'ratified 2026-07-10 with #17-#19', with its evidence document cited; the conditions at :64-92 and the amendment note at :128-130. The last condition is registered separately as D-209, the retiring-code audit rule, at its cowork_audit_protocol.md home. Found by the phase-1d enumeration wave, 2026-08-02.


## Group G — Layer 4 — chord identity

### D-280 — Gates read structured fields only - never a chord symbol string and never a Roman numeral

> 4. **Gates operate on structured fields only**: no chord-symbol string parsing,
>    no Roman-numeral inference. This is now a standing rule for any future gate
>    or scoring change. Symbol- and Roman-numeral-derived signals are too lossy
>    and too entangled with the formatter to be reliable inputs to chord
>    classification.

**In plain words.** Any gate or scoring rule reads structured analysis fields. It never parses a chord-symbol string and never infers from a Roman numeral. Signals derived from symbols or Roman numerals are too lossy and too entangled with the formatter to be reliable inputs to chord classification.

**Why.** The reason is stated with the rule: symbol- and Roman-numeral-derived signals are lossy and entangled with the formatter. It is the inference/presentation boundary (register entries D-016 and D-017) stated as an input restriction - reading the rendered form back in would make an analysis depend on its own presentation layer.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/iteration_path1_summary.md:74-78`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** docs/iteration_path1_summary.md:74-78, recorded among the architecture decisions of the completed iteration path and stated there as 'now a standing rule for any future gate or scoring change'; no date or ratifier is stated at this home. Distinct from register entry D-066, which forbids chord symbols written in the SCORE as analyzer input; this forbids re-reading our own rendered output. Found by the phase-1d enumeration wave, 2026-08-02.


## Group U — The standing decision-bearing surfaces

### D-281 — The batch measurement tool must emit the structured fields on every alternative, or the corpus figures silently revert

> 3. **batch_analyze output schema**: `batch_analyze.cpp` must emit
>    `rootPitchClass`, `bassPitchClass`, `quality`, `bassIsRoot` on every
>    alternative entry. This activates the previously-dormant
>    `_matches_alternative` reclassification in `compare_analyses.py` and is the
>    floor below which corpus measurements revert to pre-Iter-36 counts (~700
>    BIR=false). Committed in Iter 36 (recovered in `5df8421114` after a git
>    reset lost the original commit).

**In plain words.** The batch analysis tool emits root pitch class, bass pitch class, quality and bass-is-root on every alternative entry, not only on the winner. Those fields activate the comparison script's reclassification of readings where the corroborating source matches our second or third candidate; without them the corpus measurement silently reverts to its earlier counts.

**Why.** The failure that produced it is recorded with it: the change was lost to a hard reset and went undetected for three weeks, and only a stale binary holding the documented baseline made the loss visible at all. It is principle #19 applied to a measurement tool - a figure produced without these fields is not the figure it claims to be.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/iteration_path1_summary.md:66-72`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** docs/iteration_path1_summary.md:66-72, recorded among the architecture decisions of the completed iteration path; no date or ratifier is stated at this home. A decision about a MEASUREMENT TOOL and its floor, reported separately by the phase-1d enumeration wave (2026-08-02) so that the sealed measurement-tools partition can account for it.

