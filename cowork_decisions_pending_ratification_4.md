# The 14 decisions pending ratification (D-286…D-299) — complete entries

> **GENERATED REVIEW AID (Cowork, 2026-08-02).** Found by the phase-1e archive partition
> (`cowork_handoff_archive.md` read in full; `STATUS_ARCHIVE.md` in part, remainder measured).
> Entered with status from the record only — RATIFICATION IS YOURS. All enter LIVE (no later
> ruling names any of them — itself the finding). Headline: D-286, the Stage-3.1b shelving —
> the audit's founding case, never registered until now. D-292 (the fitting-pool licence
> constraint) carries the OI-271 conflict — see the decision surface in chat.


## Group C — Cross-cutting analysis contracts

### D-286 — Whole-score interactive analysis was SHELVED WITH EVIDENCE; the bounded window is the ratified reading

>   self-consistent. **Decision (Cowork): bounded-window cache (CC's recommendation);
>   whole-score SHELVED with evidence; P3↔P1 consistency PARKED as a product/Stage-5
>   question; D-P4/D-BRIDGE closure rolled back to the 2.4 contract; the A/B data
>   promoted to committed Stage-5 evidence.** Revision instruction:

**In plain words.** At Stage 3.1b a measured A/B put a whole-score interactive analysis against a bounded-window one and the window won against the published annotations; the whole-score variant was withdrawn against that measurement and the bounded window adopted. The question of whether a per-note answer must match the whole-piece answer was parked, not settled.

**Why.** Measured: the A/B changed 32-40 % of ticks on contrapuntal music and the published annotations preferred the window path 59/41 overall and 65/35 on Mozart (`docs/p3_granularity_ab_3_1b.md`, the committed evidence). The shelving is the founding case of the decision-conformance audit: it lived only in an archive outside the session-start read, and a later build specified whole-score interactive analysis without meeting it (`OPEN_ITEMS.md` OI-210, OI-212).

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Home.** `cowork_handoff_archive.md:2964`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in the 2026-06-12 Stage-3.1b block of `cowork_handoff_archive.md` and in `docs/p3_granularity_ab_3_1b.md`. NOT superseded by any later ruling: `OPEN_ITEMS.md` OI-210 records that the extent question was then PARKED pending the granularity-robust metric (which has existed since 2026-07-06) and is now implemented as whole-piece by dispatch specification with no ruling — so the shelving stands on the record and the implementation departs from it. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group F — Layer 3 — key and mode

### D-287 — Key-as-distribution is SHELVED - its motivating case was already fixed and no live target was found

> 3. **Key-as-distribution — ⛔ SHELVED.** Motivating case (Corelli op01n08d) already
>    fixed by `81978321e3`. No confirmed live target in corpus. `normalizedConfidence`
>    structurally unreliable as scaling signal. See `docs/redesign_plan.md` §Step 3.

**In plain words.** Carrying a ranked distribution of key candidates forward, instead of one committed key, was withdrawn: the one failure it was designed to fix had already been fixed another way, no other case in the corpus needed it, and the confidence number it would have been weighted by is not trustworthy.

**Why.** Measured and cited in the record: the motivating case (Corelli op01n08d read in G minor instead of C minor) was already fixed by the partial-signature correction `81978321e3`, the resolver returns C minor at rank 0 for every stretch, and no case was found where the correct key sits at rank 1 or 2 (`cc_step3_key_investigation_report.md`). A second reason is recorded beside it: the confidence field is re-ranked without being recomputed, so it reads anywhere from 0.025 to 1.00 on one correctly-keyed piece and cannot scale anything.

**Status.** LIVE · decided 2026-06-08 · ratifier not stated

**Home.** `cowork_handoff_archive.md:5272`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the redesign-sequence block) and in the 2026-06-08 `STATUS_ARCHIVE.md` entry, both pointing at `docs/redesign_plan.md` Step 3. The shelving names its own re-open condition — a confirmed case where the correct key sits at rank 1 or 2 — so it is a shelving with a stated trigger, not a permanent exclusion. Found by the phase-1e second-partition archive read, 2026-08-02. Note for a future reader: the joint estimator (D-001) carries a full posterior by construction, so the concern this shelving withdrew is met by a different design, not by reviving this one.


## Group C — Cross-cutting analysis contracts

### D-288 — Beam widening is SHELVED - a wider search cannot fix the failure class it was proposed for

> - **⚠ STRATEGIC PIVOT (2026-06-13, Cowork-verified + user-directed): beam-widening
>   SHELVED; the back half of the roadmap is being re-grounded on measured precision
>   headroom.** The 3.2 design's §3 derivation (Cowork-verified against the independent

**In plain words.** Searching more candidate readings in parallel was withdrawn. The failure it was meant to fix is not a search failure: the wrong reading is the highest-scoring one, so looking at more readings finds the same wrong answer. Only changing how readings are scored, or cutting the music differently, can fix it.

**Why.** Derived, then cross-checked: the design's own arithmetic (verified against the independent earlier figures - AbMaj7 2.55 over 2.33, F#7 2.85 over 2.825) shows the wrong continued-root path is the genuine global optimum, which a decode finds exactly as a greedy walk does. The consequence recorded with it is that a wider beam is substitutable by the width-one beam for every other motivated use, so nothing else justified building it.

**Status.** LIVE · decided 2026-06-13 · ratified by the user (directive), on Cowork's verification

**Home.** `cowork_handoff_archive.md:3029`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-13 strategic-pivot block); `docs/beam_widening_design.md` was banner-shelved and retained for its derivation. Found by the phase-1e second-partition archive read, 2026-08-02.

### D-289 — Meta-principle: precision lives in the evidence and the functional labelling, not in the search

>   correct key never rank-2 in 51.6% of S2) — unrecoverable by any path. **SECOND
>   falsified structural fix → META-PRINCIPLE recorded in roadmap: precision lives in
>   emission + functional labeling, NOT search/path.** The HMM path is the least valuable
>   part of Stage 4 (~10%); KeyArea spans + the key-EMISSION fix are what deliver.

**In plain words.** Three independent investigations converged on one rule: accuracy is gained by improving what evidence each reading is judged on and by labelling harmonic function better - not by searching harder over the readings already on the table.

**Why.** Converged from three separate falsified structural fixes, each measured: the wider beam (the wrong reading is the top-scoring one), the key path (it reaches about 10 % of the key errors because the correct key is usually not even ranked second), and the algorithmic ground-truth filter. Recorded in `docs/implementation_roadmap.md` as a meta-principle.

**Status.** LIVE · decided 2026-06-13 · ratifier not stated

**Home.** `cowork_handoff_archive.md:3082`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-13 Stage-4 design-investigation block) and `docs/implementation_roadmap.md`. ★ FLAGGED against the OI-270 meta-findings (D-282…D-285): this is an EARLIER and independently-derived statement of the same insight as D-284 (selection and competition are saturated). It does not change D-284's ruled status; it dates and corroborates it. It was itself later RECONCILED rather than overturned: `cowork_handoff_archive.md:3920-3921` records that the joint decode's value is broad-evidence integration, NOT search — "search is about zero" having been measured over a FIXED NARROW evidence surface. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group F — Layer 3 — key and mode

### D-290 — The key-agnostic local cadence approach is FALSIFIED at its precision ceiling

> - **★★ CADENCE-PRECISION INVESTIGATION: NEGATIVE — the key-agnostic LOCAL cadence approach has HIT ITS PRECISION CEILING (2026-06-15).**

**In plain words.** Deciding the key from cadences found without knowing the key, one cadence at a time, was tested to its limit and cannot be made accurate enough to use. The remaining errors need either a long-range key decision or a different kind of model - not a better local cadence rule.

**Why.** Measured with a byte-matched reimplementation (the Python re-implementation reproduced the committed analysis exactly on all 326 pieces, so the simulation is trustworthy): the chromatic-leading-tone gate is orthogonal to correctness (about 45 % of true modulations and about 50 % of false ones carry a diatonic leading tone), and the relative-pair signals were already spent by the existing aggregation. Ceiling approximately 50-58 % precision at 18-22 % recall, below the bar the wiring step required.

**Status.** LIVE · decided 2026-06-15 · ratifier not stated

**Home.** `cowork_handoff_archive.md:3896`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-15 cadence-precision-investigation block), citing `cc_cadence_precision_investigation_dossier.md`. Its scope is stated with it: measured on the Bach ground-truth corpus, non-Bach unmeasured. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group H — Layer 5 and Layer 6 — function, cadence, grouping

### D-291 — The tonicization labeller is NOT wired, and the metric is NOT changed to credit it - both would hide a real key error

> - **★ HEADROOM CORRECTION (load-bearing — propagate to docs):** the biggest precision slice relocates **Stage 6 → Stage 4** (local-modulation
>   detection). **Do NOT wire 6-tonic-i** (games rn_agree, degrades correctness). Real lever = a **LOCAL-MODULATION / KeyArea detector
>   (Stage 4)**, ~95% of S1, signal = sustained span + local cadence (consumes the committed CADENCE INSTRUMENT + KeyArea); 6-tonic-i's

**In plain words.** A working labeller for applied chords was deliberately left unwired, and the proposal to make the accuracy measurement treat its labels as equivalent to the annotator's was rejected. Both would have raised the reported Roman-numeral agreement while the underlying reading stayed wrong: the annotator has changed key, and labelling the chord relative to the old key hides that.

**Why.** Measured: of the affected cases 92.7 % are cadence-confirmed local keys in the ground truth and 79.2 % last five chords or more, so the annotator's modulation is correct for about 97 % of them; only 2.7 % are brief enough for either reading to be defensible. The comparison already credits the label by root and quality, so it does not over-penalise - it MASKS. Recorded as the clearest win of the measure-before-building rule: without the check the labeller would have shipped and improved the number while worsening the output.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Home.** `cowork_handoff_archive.md:3833`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 metric-check block), citing `cc_tonicization_modulation_metric_dossier.md`. The same block relocates the largest accuracy slice from the function layer to the key layer. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group L — Licensing, contribution, and coding standards

### D-292 — The fitting-pool licence constraint - values that ship are fitted only on freely-licensed music

>    **★ BINDING on the fitter design (user-ratified 2026-07-04): the FITTING-POOL LICENSE CONSTRAINT** —
>    census §8c block: ship-intended weights fit only on the PD/CC0/CC-BY pool; NC-class (all DCML, MCMA,
>    Essen…) + no-license sources = validation/QA only; the design doc declares the objective-vs-validation
>    source split explicitly; the constraint also enters the roadmap Stage-5 block at the next CC docs commit.

**In plain words.** Any number that is fitted and then shipped may be fitted only on public-domain or permissively-licensed music. Music under a non-commercial or unstated licence may be used to check and validate, never to fit a shipped value.

**Why.** A licensing constraint, not a measurement one: fitted values derived from a corpus inherit that corpus's licence terms, and this project ships under GPL v3 (D-118). The record requires the fitting design to state its objective-source versus validation-source split explicitly.

**Status.** LIVE · decided 2026-07-04 · ratified by the user

**Home.** `cowork_handoff_archive.md:2478`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the queue block, marked BINDING on the fitter design), naming `cowork_score_census.md` §8c as the constraint's own block and `cowork_stage5_fitter_design.md` §2/§3a as where it binds. ★ Load-bearing at HEAD and NOT reconciled anywhere in the record this pass read: the joint estimator's tables and weights are fitted on the DCML ground truth, which this constraint names as non-commercial-class and therefore validation-only. Whether the constraint was amended, scoped, or simply not carried forward is not stated. Found by the phase-1e second-partition archive read, 2026-08-02; rowed.


## Group C — Cross-cutting analysis contracts

### D-293 — Fitted values are fitted per IDIOM, never for a user preset; presets are regression surfaces and delivery carriers

> **★ NEW USER MANDATE (recorded as design constraint 4c): OPTIMIZE FOR IDIOMS ONLY — never for the current
> user presets;** presets = regression surfaces + delivery carriers; ONE fit per idiom; the end-user-facing
> preset question is a separate later product decision. **★ CHECKPOINT P0 RATIFIED (user): 61 tunable / 17

**In plain words.** Numbers are fitted once per musical idiom - a body of repertoire that shares a practice - and never tuned to match one of the program's named presets. A preset is a way of delivering a set of values and a surface to check for regressions; which presets a user should see is a separate product question, decided later.

**Why.** A user mandate, recorded as constraint 4c of the fitting design. Its consequence is stated with it: ONE fit per idiom, and the Bach fit is an idiom fit delivered through two carriers.

**Status.** LIVE · date not stated · ratified by the user

**Home.** `cowork_handoff_archive.md:2363`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the Stage-5 fitter block) as design constraint 4c of `cowork_stage5_fitter_design.md`. Consistent with, and earlier than, D-003 (inference is preset-independent; presets are presentation concerns) — this states the FITTING side of the same separation. Found by the phase-1e second-partition archive read, 2026-08-02.

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

**Provenance.** Recorded in `cowork_handoff_archive.md` (the corpus-audit block, as the ground-truth verdict). The human-annotation-only requirement it names was delivered as the granularity-robust unit (D-115), whose own text carries the clause "music21 is NOT ground truth"; the two further clauses — never describe a measurement as ground-truth agreement, and no self-annotation in any measurement — are recorded ONLY here. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group J — Presentation and output conventions

### D-295 — Zero information loss to the end user - every inferred object must be displayable

>   R-map at its next edit) and **E-14** (user-stated principle: ZERO INFORMATION LOSS TO THE END USER — every
>   inferred object displayable; progressive disclosure yes, structural hiding no; ARCH pointer rides ARCH's next
>   edit). Market probe recorded: no comparable engine anywhere in the MuseScore GitHub space; plugins hand-annotate
>   what our layers infer.

**In plain words.** Anything the analysis works out must be capable of being shown to the user. Showing it gradually, so the display is not overwhelming, is fine; leaving something permanently unreachable because the interface has no place for it is not.

**Why.** A user-stated principle. It is the display-side counterpart of the no-information-loss principle (D-099, principle #12), which governs what the analysis may discard internally; this governs what the interface may withhold.

**Status.** LIVE · date not stated · ratified by the user

**Home.** `cowork_handoff_archive.md:2507`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the standing-records block) as item E-14 of `cowork_product_tool_register.md`, with a note that a pointer into the architecture document was owed at its next edit. This pass found no such pointer in the register's own home census, so the owed act appears undischarged. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group I — Module boundaries and code structure

### D-296 — READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits

> - **★ FERMATA/OFF-LIMITS CLARIFICATION (user, 2026-06-14) — corrects a Cowork over-statement:** *reading/calling*
>   engraving is ALLOWED from any code we may edit; only *editing* `src/notation`/`src/engraving` CODE is off-limits.

**In plain words.** Our code may call into and read from MuseScore's own score and engraving code wherever we are allowed to write. What is out of bounds is changing MuseScore's notation and engraving source itself.

**Why.** A user correction of an over-statement that had conflated the two. Its worked consequence is recorded with it: a measurement that needed fermatas read them in the batch tool, which already loads the score, and passed them into our own analysis through our own input structure - zero edits outside our area.

**Status.** LIVE · decided 2026-06-14 · ratified by the user

**Home.** `cowork_handoff_archive.md:3732`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 Stage-4c block) as a standing lesson. Bears directly on D-229, the general MuseScore-dependency rule the user adopted 2026-08-02: this is the EDIT-versus-READ half, stated a month and a half earlier and consistent with it. D-229 adds what the bridge may read (the score model through the bridge pattern, never layout-derived state) and when an edit to MuseScore's own code is admissible. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group C — Cross-cutting analysis contracts

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

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-07-07 entry-point block) as a dated correction. It scopes D-099 / principle #12 and is recorded nowhere that a reader of #12 would find. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group T — Standing process rules and local patches

### D-298 — The layer-by-layer audit - each layer is audited once its pieces are in place

> - **★ NEW STANDING METHOD recorded (user): layer-by-layer audit once pieces are in place** (handoff top standing block +
>   roadmap). The back-half verification model.

**In plain words.** Verification is organised by layer: when a layer's pieces are built, that layer is audited as a whole before the work moves on, rather than checking each change in isolation.

**Why.** A user-recorded standing method, adopted as the verification model for the second half of the programme. It is the method the later per-layer certification plan realised.

**Status.** LIVE · decided 2026-06-14 · ratified by the user

**Home.** `cowork_handoff_archive.md:3771`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 option-C block) as a new standing method, pointing at the handoff's standing block and the roadmap. Realised as the dependency-ordered per-layer certification plan (`OPEN_ITEMS.md` OI-84, complete 2026-07-12) and as the audit protocol's pass ordering. Found by the phase-1e second-partition archive read, 2026-08-02.


## Group G — Layer 4 — chord identity

### D-299 — No negative-margin guard may be added - it would break every intentional backward-swap gate

> **Do NOT add a negative-margin guard** — would break Gate J and all other
> intentional backward-swap gates (B/C/D/E/F/G/H/I/K/L, Iter 91).

**In plain words.** A rule that refuses to let a later correction step overturn the leading reading when the margin against it is negative must not be added. Several correction steps exist precisely to overturn a leading reading, and such a rule would disable all of them.

**Why.** A structural prohibition, stated with the mechanism: the named correction steps promote a reading that was behind on the raw score, so a guard keyed on that margin removes their reason to exist.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_handoff_archive.md:4967`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the failure-cluster block). This is the statement the 2026-08-02 residual pass cited as its worked example of a real ruling sitting inside the unresolved residual (`open_items/OI-207.md`, the residual-pass note), now entered. Found by the phase-1e second-partition archive read, 2026-08-02.

