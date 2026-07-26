# The notation-layer adoption increment — decision surface (★ USER-RATIFIED 2026-07-26)

**★ RATIFIED BY THE USER 2026-07-26, as asked in §9:** the §2 principles amendment (the
decision-neutrality corollary — lands in CLAUDE.md via the next dispatch's ratification commit)
and all five recommendations — **A2** (the joint-native record IS the surface), **B-full**
(the contract is the full posterior; the established slice is the first delivered step; the
marginal completion is rowed **OI-193**), **C1** (two-mode key + published un-rounded modal
reading), **D1** (tables embedded as provenance-stamped generated source), **E** (modal reading
inside the increment; ornament labels their own increment, rowed **OI-194**). Rows created at
ruling time per register rule (c). The first dispatch is the §8.1 read-only consumption-surface
audit (`cc_instruction_notation_consumption_audit.md`).

**Author:** Cowork, 2026-07-26, at the user's direction — the named successor increment of the
OI-178 staged-scope adoption (`cc_instruction_adoption_commit.md` header; CLAUDE.md gate block (A)
"STAGED SCOPE"). **Status: ratified, fourth writing.**

**The rulings this writing incorporates (user, 2026-07-26, in order):**
1. *(second writing)* Every pro and con names the principle/rule/gate it rests on; every option
   carries a two-axis rating — (a) principles/guardrails, (b) the ultimate objective,
   **enabling the best possible inference (#4)**.
2. *(third writing)* Whether a consumer needs to change is IRRELEVANT.
3. *(this writing)* **What already exists — what can be reused, and what would be made obsolete —
   is SECONDARY to the principles and the ultimate objective.** A design is chosen because the
   principles and the inference objective demand it; only then does the existing code either
   serve that design or retire. Reuse carries weight in exactly one way: an existing instrument
   carries its ESTABLISHMENT forward (#19) — sunk cost and implementation convenience carry
   none. **This changed the Decision-B recommendation** (previously the established local
   posterior slice with the full posterior as a someday-upgrade; the deferral leaned on what
   already existed, and is void).

Because these three rulings recur, §2 below proposes codifying them as a principles amendment for
ratification. Per the standing full-decision-surface rule, all ruling questions are asked in a
separate, later turn.

**What this increment is.** The 2026-07-26 adoption made the joint estimator the production
inference layer on the batch/corpus surface only. The in-app notation layer still runs the legacy
analysis — a declared, bounded migration state (#23, lawful transitions). This increment closes
that state: the in-app notation analysis is produced by the joint estimator's decode, through a
defined output surface, with the fitted tables delivered to the running application. Until it
lands, the dual path stays visible in the handoff every session (the OI-180 DT-13 guard).

**What this increment is NOT.** Not the legacy-code deletion (that is OI-180 §4's retirement map,
each item its own later dispatch). Not a re-fit, not a threshold change, not a corpus or
`tools/robust_stop/` event (the graded batch surface is already A's and does not move here).

---

## 1. The verified current state (all read at source this session)

**The notation seam.** The in-app analysis enters through ONE function:
`analyzeHarmonicRhythm(score, startTick, endTick, excludeStaves, granularity)`
(`src/notation/internal/notationharmonicrhythmbridge.cpp:69`), a thin wrapper that reads the
notation-side configuration (including 21 per-mode prior preferences, lines 92–113) and calls the
shared orchestrator `analyzeRegions(...)`, returning `std::vector<HarmonicRegion>`. Live
production callers: `notationcomposingbridge.cpp:321` (the main analysis unit — regions +
`analyzeSection`), `notationimplodebridge.cpp:1374`, `notationtuningbridge.cpp:762`. The pipeline
snapshot tests and the implode tests consume the same seam.

**The consumed record.** `HarmonicRegion` (`src/composing/analysis/region/harmonicrhythm.h:78`)
carries: `chordResult` (identity + function facts, e.g. `diatonicToKey`), ranked `alternatives`,
`hasAnalyzedChord`, `keyModeResult` (signature fifths, a 21-value `KeySigMode`, tonic, raw score,
the emission sigmoid), the sounding `tones`, `temporalExtensions`, two in-memory-only fields with
no production consumer (`keyAlternatives`, `fanout`), and `keyConfidence` (the Layer-3
sequence-margin confidence, D-L3a).

**What the joint module publishes today.** The C++ decoder's `DecodeResult`
(`src/composing/analysis/joint/jointdecoder.h:119`) is the MAP path only: per segment, ticks +
(tonic, major/minor) + the chord class (degree, quality, inversion, applied target) + the derived
root. **No alternatives, no confidence, no posterior field exists on the C++ surface.** The Python
probe publishes one posterior slice — per committed segment, the runner-up KEY and its
content-score gap (`probe_decoder._segment_posterior`, lines 1330–1363) — and no chord-axis
alternatives. The ratified decode plan (factorization §5) requires: "The full posterior (not only
the best path) is retained for the published alternatives and the uncertainty surface (#12; the
carry/abstention policies of the old architecture re-express as posterior mass)."

**The batch render is deliberately minimal.** `writeJointInferenceJson`
(`tools/batch_analyze.cpp:4414`) emits the a8 grading schema with `keyConfidence` hard-coded 1.0,
`diatonicToKey` null, `alternatives` empty — correct for grading, not a notation contract.

**Table delivery.** The module loads, from a directory path: `tables_all.json`,
`note_tables_all.json`, `factor_presence_all.json`, `fermata_boundary_addendum.json`
(`jointtables.cpp:116–172`), `mode_marginal.json` (`jointadapter.cpp:115`), and the selected
weight vector from `decode_parity_ref.json` (`batch_analyze.cpp:4512`). In tests the directory is
the compile-time define `JOINT_ARTIFACT_DIR` = the repo's `tools/joint_estimator`
(`src/composing/tests/CMakeLists.txt:101`); batch takes it as a command-line argument. **The
running application has no delivery mechanism — gap 2 of CC's two-gap STOP.** Measured sizes: the
five table artifacts total ≈158 KB; the weight vector is 13 numbers (`decode_parity_ref.json`
itself is a parity reference, not a delivery candidate).

**The fact adapter is app-ready.** `buildAdapterFacts(score, stem)` (`jointfactadapter.h:86`)
builds the decoder's inputs from the L1 published note surface plus the score's structural facts,
for any loaded score — not batch-specific. Its one accepted residual is the OI-184 reader-skew
class (10 corpus stems, metric-position bookkeeping; option 1 accepted-and-recorded; the repair is
bundled into the OI-184 unification event).

**The ratified presentation obligations.** Decision 1 (2026-07-19): the un-rounded modal reading
is PUBLISHED for the presentation layer. Decision 4: ornament labels (the non-chord-tone
categories) are derived post-decode and PUBLISHED. Neither exists yet in the C++ module; both are
PART of the ratified record and must not drop (handoff method reminder).

---

## 2. Proposed principles amendment (for ratification — the three recurring rulings, codified)

The three corrections to this document's writings are general decision rules, not
increment-specific ones. Proposed as a corollary to the guiding principles (provenance: the
user's rulings of 2026-07-26 at this increment's drafting), so no future decision surface repeats
the error:

> *Decision-neutrality of the existing implementation (corollary to #4/#6/#19).* Designs are
> chosen from the principles and the ultimate objective — enabling the best possible inference —
> alone. In that choice: **(a)** the value of reusing existing code, and the cost of making
> existing code obsolete, are SECONDARY — they may break ties between designs equal under the
> principles and the objective, and reuse counts only as carried-forward establishment (#19),
> never as sunk cost or saved effort; **(b)** downstream implementation impact — whether and how
> many consumers must change — carries NO weight; **(c)** end-user-visible behavior change
> carries NO weight (the 2026-07-26 unshipped-scoping ruling), while every behavior change
> remains ratification-gated (#14) and verification-gated (#15/#19) exactly as before. The
> best-possible-inference design is chosen first; what exists then either serves it or retires.

(Notes on fit with the standing list: this does not weaken #6 — one-path-per-concern is an
END-STATE structural principle, not a claim that the existing path deserves preservation; it does
not weaken #19 — establishment must still exist before trust, and an existing established
instrument legitimately carries that establishment; it does not weaken #14/#22 — gates and
ratification still govern every change event.)

---

## 3. Decision A — the shape of the output-surface contract

The question: on what record do the notation consumers read A's result? Derivation order per the
amendment: first, what surface do the principles and the inference objective demand? Then, what
existing code serves it or retires.

**What the principles demand of the surface, before any option is weighed:** every fact A computes
is published once, on the producing layer's own surface, in the producer's own terms, with
establishment status attached (the fact-publication corollary, #6/#7/#12; the evidence-publication
amendment); nothing computed is narrowed or reinterpreted at a boundary (#12/#19); the surface
carries what best-possible-inference consumers will need (#4) — the posterior, the derived chord
facts, the ratified presentation facts.

**Option A1 — render A into the existing `HarmonicRegion` stream; consumers keep reading the
legacy record permanently.**
- Pros:
  - The switch is verifiable like-for-like at one seam: the same record type before and after,
    diffed field-by-field on the full surface (#15). *(A verification convenience only —
    secondary under the amendment, since A2's staging achieves #15 by other declared
    instruments.)*
- Cons:
  - The legacy record's fields carry legacy semantics the joint decode does not natively have
    (the temporal-extensions snapshot; the emission sigmoid; the 21-value mode). Mapping A's
    facts into them loses or distorts information at the boundary (#12) and lets a consumer read
    a number whose meaning changed without its establishment changing (#19).
  - The posterior — A's genuinely new information — has no adequate home in the legacy record;
    squeezing it into `alternatives`/`keyConfidence` narrows it (#12).
  - The producing layer's own surface would permanently BE a legacy-shaped record — the
    fact-publication corollary met in letter only; the legacy shape survives the legacy path as
    permanent structural residue (#6/#7). This option's entire appeal is "the record already
    exists" — exactly the sunk-cost reasoning the amendment ranks secondary.
- Rating (a) principles: fails the surface requirements derived above (#12, fact-publication
  corollary) and rests on the demoted reuse value. Rating (b) #4: inference identical today; the
  narrowed posterior forecloses downstream precision uses — a standing #4 cost. **Not
  recommendable under the amendment.**

**Option A2 — the joint-native record IS the surface: A publishes its own record (segments, keys,
classes, derived chord facts, the posterior, the ratified presentation facts), and the notation
consumers read it; `HarmonicRegion` and its satellite shapes retire with the legacy path.**
- Pros:
  - Satisfies every derived surface requirement directly: publish once, producer's own terms,
    nothing narrowed, establishment status attached (#6/#7/#12/#19, the fact-publication and
    evidence-publication corollaries).
  - No transitional dual record shape exists at any point — no new #6 debt from the migration
    itself; the end-state (one record, one path) is reached within this increment.
  - Verification staging is fully available WITHIN the option (working method G): the record and
    decode land dormant behind the default-OFF driver; consumer outputs are diffed across the
    flip on the full output surface (#15); the behavior change is still ONE revertible ratified
    switch commit (#14/#22).
- Cons:
  - The old and new records differ in shape, so the switch cannot be verified as a same-type
    field diff; the #15 comparison moves one level up — to consumer outputs and the graded
    corpus equality (§8.3) — and those comparison instruments must be declared and established
    BEFORE the flip (#19). A real duty, fully answerable by the standing machinery.
  - Every legacy field with information not recomputable from A's surface must be individually
    dispositioned (republished, or retired-with-rationale) — the #12 no-information-loss check
    the §8.1 audit makes exhaustive.
- Rating (a) principles: the only option meeting the derived surface requirements with no
  permanent or transitional debt; its costs are verification-design duties the standing
  machinery covers. Rating (b) #4: the un-narrowed posterior and presentation publications give
  future precision consumers the full computed record — the best #4 posture.

**Option A3 — the joint-native record plus a thin `HarmonicRegion` compatibility view; consumers
migrate later.**
- Pros:
  - The native record exists from day one (as in A2); the flip is verifiable as a same-type diff
    (#15 convenience, as in A1).
- Cons:
  - The view exists only to defer consumer changes (ruled irrelevant) and to preserve the
    existing record shape (ruled secondary) — with both motivations void, it is a second
    publication shape of the same facts with no principled justification: an avoidable #6
    violation requiring its own #23 declaration, bound, and retirement bookkeeping.
  - The view inherits A1's boundary narrowing (#12) for everything it renders; consumers reading
    it sit on reinterpreted semantics (#19) for the life of the "transition".
  - Deferred migrations with no forcing function are the tracked-remainder pattern the register
    discipline exists to prevent (doc-sync rule (e)).
- Rating (a) principles: dominated by A2 — buys a verification convenience at the price of an
  avoidable #6/#12/#23 debt. Rating (b) #4: identical inference; no precision argument favors
  it.

**Recommendation: A2.** (Constrained-optimum ledger: A3 was the second writing's recommendation
on consumer-change grounds — voided by ruling 2; A1's excluded-alternative rationale: permanent
#12/#6 debt resting on sunk-cost value — voided by ruling 3. If the §8.1 audit surfaces a
consumed legacy fact that cannot yet be published correctly from A's surface — a genuine #19
blocker — that field's disposition returns as its own decision.)

## 4. Decision B — what the published posterior IS (the uncertainty surface)

**What the principles demand, before any option is weighed:** the ratified decode plan (§5)
already says it — "the full posterior (not only the best path) is retained for the published
alternatives and the uncertainty surface (#12)". The evidence-publication amendment says
evidence-class facts are published broadly EVEN WITHOUT a named consumer — the user's recorded
rationale being precisely that a visible spread of evidence lets a future design recognize facts
it would not have requested — with establishment status on the surface and no unvalidated fact
under load (#19). And #4 asks which surface enables the best possible inference downstream. All
three point the same way: the surface is the full posterior. The previous writing recommended the
LOCAL slice with the full posterior as a someday-upgrade "triggered by the first consumer that
needs it" — a deferral resting on what already existed (the slice's ready-made oracle) and on the
absence of a consumer; ruling 3 voids the first basis and the evidence-publication amendment
answers the second. The options are therefore re-derived:

**Option B-full — the contract's uncertainty surface is the full posterior: per-span/state
marginal mass from exact forward-backward over the decode lattice, published as model
probabilities with their establishment status attached (model-internal quantities, NOT calibrated
real-world confidences until a #20-gated calibration is ever measured); the ranked alternatives
and the key/chord uncertainty read off it.**
- Pros:
  - IS the ratified decode-plan clause, executed (#14 — the ratified record governs); complete
    #12: no posterior mass invisible anywhere, including the cross-segmentation mass every local
    slice hides; the carry/abstention re-expression is total, not partial.
  - The evidence-publication amendment's case exactly: published broadly, status-marked, so
    future designs (the OI-192 fifth-substitution refinement; any uncertainty display; the
    OI-179-ceiling-aware residual work) can recognize and use it — the best #4 substrate.
  - Establishment is achievable by the standing pattern (#19): forward logZ == backward logZ,
    marginals summing to 1 per span set, agreement with the Python fit-arc lattice arithmetic on
    synthetic cases, and the MAP path's mass dominating where the decode margin is large — a
    declarable oracle, built BEFORE trust, per the funnel.
- Cons:
  - A new production-path computation with a genuine establishment PRECONDITION (#19): the
    oracle above must be built and pass before the marginals are published as facts — this gates
    the increment's schedule, and per #13 any surprise in it is a STOP.
  - Decode-time cost grows by a constant factor over the same lattice; the declared guard: the
    cost is MEASURED (the OI-178 record's timing pattern), and if it ever pressures the prune,
    that is a measured #4 trade surfaced to the user — never silently taken (OI-188's lesson).
  - Model probabilities invite over-reading: the #19 guard (status on the surface; no consumer
    load-bears on calibration) must be explicit in the contract.
- Rating (a) principles: the ratified clause executed, with #12/#19 and the evidence amendment
  satisfied in full; the establishment precondition is the funnel working as designed, not a
  defect. Rating (b) #4: the maximum-information uncertainty surface — the best enabling
  substrate for every named future precision consumer.

**Option B-slice — the local slice only: per segment, runner-up key + score gap (the existing
Python form) and a chord-axis analogue, raw log-score gaps.**
- Pros:
  - Carried-forward establishment (#19, the amendment's one legitimate reuse value): the key-axis
    slice has a live parity oracle today.
  - No invented calibration (#1/#19/DT-2) — shared with B-full, which publishes model
    probabilities from the model's own arithmetic, equally calibration-free.
- Cons:
  - As the CONTRACT it under-delivers the ratified full-posterior clause — a narrowing of a
    ratified decision that would itself need ratification (#14/#22); the cross-segmentation
    blindness is a permanent, declared #12 loss (#17e names the false-negative path: a
    boundary-ambiguous passage looks artificially certain).
  - Waiting for "a consumer to name its need" before completing to the full posterior inverts
    the evidence-publication amendment's ratified direction.
- Rating (a) principles: sound as an ESTABLISHED STEP, unsound as the END-STATE contract (it
  re-ratifies away a ratified clause). Rating (b) #4: less enabling than B-full by exactly the
  hidden mass.

**Option B-none — MAP only.** Contradicts the ratified clause outright (#14/#22), regresses below
the legacy surface's published alternatives (#12), re-creates the carry/abstention vacuum.
Rating: fails on every axis; **excluded** (kept for the ledger).

**Recommendation: the contract IS B-full; B-slice is the first DELIVERED step (it is established
today and is a strict subset of B-full's surface), and the marginal completion is a NAMED, ROWED
step of this increment — not an indefinite upgrade.** Register row at ruling time (register rule
(c)); the slice's fields are defined as views of the posterior so nothing is published twice
(#6). If the marginal oracle's establishment surfaces a blocker, that is a #13 STOP returning to
the user — never a silent regression to B-slice-as-end-state.

## 5. Decision C — the mode field and the 21-value presentation question

A's key state is (tonic, major/minor) — ratified. The legacy record's mode field is a 21-value
`KeySigMode`; the bridge plumbs 21 hand-set mode priors (verified, bridge lines 92–113). Ratified
decision 1 publishes the UN-ROUNDED MODAL READING (the emission's modal color — how strongly a
passage's variable degrees behave, e.g., Dorian-ly) instead of a rounded exotic-mode label.

**Option C1 — the surface carries A's two-mode key; the un-rounded modal reading is published
beside it as its own fact; no 21-value mode label is ever inferred or published again.**
- Pros:
  - Faithful to the ratified mode decision (#14) and to the measured OI-174 lesson: the
    emitted-`Altered`-on-diatonic-material defect class becomes structurally unreachable — a #4
    gain on the key axis grounded in measurement (#1/#19).
  - The modal color survives UN-rounded — strictly more information than any 21-value label
    (#12) — with establishment status on the surface (#19, evidence-publication guardrail).
  - The 21 hand-set mode priors go dead: hand-set constant mass retires (the OI-23/#1
    direction), recorded for retirement-map item 2, docs moving with it (#10).
- Cons:
  - Every consumer reading exotic `KeySigMode` values must be dispositioned against #12: is any
    information they used NOT recomputable from the published modal reading? (The §8.1 audit
    makes this exhaustive; the disposition is the requirement.)
- Rating (a) principles: the only option consistent with the ratified decisions; positive on
  #1/#12/#19 simultaneously. Rating (b) #4: a measured defect class closes; nothing
  precision-relevant is lost (the un-rounded reading informationally dominates the label).

**Option C2 — round A's modal reading back onto the 21-value vocabulary for the published mode
field.**
- Pros:
  - None on the principle axes. (Presentation continuity and the existing vocabulary's survival
    are precisely the considerations rulings 2–3 demote.)
- Cons:
  - Contradicts a ratified decision (#14); publishes strictly less information than is computed
    (#12); imitates an emission never established as an instrument (#19; OI-174 measured it
    emitting modes the material does not contain); knowingly rebuilds a measured failure surface
    (#3).
- Rating (a) principles: fails #14/#12/#19/#3. Rating (b) #4: negative — re-attaches a measured
  error class to the published surface. **Excluded**; recorded per the constrained-optimum
  ledger corollary.

**Recommendation: C1.** The concrete form of the published modal reading (which quantities, on
which record fields) is contract detail the drafting step specifies from the ratified decision-1
text and the emission's fitted covariate cells, with establishment status on the surface (#19).

## 6. Decision D — delivering the fitted tables to the running application

**What the principles demand:** the running binary's inference values must be EXACTLY the
ratified fitted values — #16 (provenance), #19 (established instrument), #9 (no stale data), with
a direct #4 stake: silent table drift silently changes inference. The artifact set (§1): five
JSON files (≈158 KB measured) + the 13-number selected weight vector.

**Option D1 — embed as generated source: a provenance-stamped code-generation step turns the
committed artifacts into compiled-in constant data (one generated file in the joint module),
stamped with the source artifacts' hashes; regeneration mechanical and diffable.**
- Pros:
  - Provenance locked at BUILD time — a wrong/stale/foreign table is impossible at runtime: the
    strongest available #16/#19 guarantee, hence the strongest #4 protection.
  - No hand transcription (#17f); the generator's output is a reviewable diff (working method G;
    the self-check rule reads the actual diff).
  - No new file class outside the module (`src/composing/analysis/joint/`) — inside the OI-180
    sanction's touchable set as amended; no sanction widening (#22).
  - A per-case table edit (the DT-2 forbidden act) would require a reviewable code diff — the
    firewall structurally reinforced.
- Cons:
  - A table re-fit becomes regeneration + rebuild — one added step in the fit-event protocol,
    documented there (#10); re-fits are rare, gated events (#20), so no discipline changes.
  - The generator is one more instrument to establish (#19 — by byte-reproduction from the
    committed artifacts) and keep in doc-sync (#10/#11).
- Rating (a) principles: strongest on #16/#19/#17f/DT-2; sanction-clean (#22). Rating (b) #4:
  best protects inference values from silent drift; no runtime cost.

**Option D2 — ship the JSON artifacts as application resource files, loaded at startup through
`JointTables::load`.**
- Pros:
  - Carried-forward establishment (#19, the amendment's one legitimate reuse value): the loader
    is established by the module tests. *(Secondary by the amendment; decides nothing here.)*
- Cons:
  - New file classes outside every sanction to date (resource manifests, packaging) — its own
    sanction widening (#22) with no gain on any principle axis.
  - A runtime failure mode (missing/mismatched resource) that must fail loudly (#13).
  - Provenance becomes a runtime CHECK (hash vs a compiled-in fingerprint), strictly weaker than
    a build-time guarantee (#16/#19); with the check added, D2 carries D1's machinery anyway
    PLUS packaging — two mechanisms where one suffices (#6).
- Rating (a) principles: dominated — weaker #16/#19, wider #22 footprint, borderline #6.
  Rating (b) #4: equal when healthy; adds a path on which value drift becomes possible if the
  check is ever weakened.

**Option D3 — runtime read from a configured filesystem path (defaulting to the repo's
`tools/joint_estimator`).**
- Pros:
  - None beyond D2's demoted reuse value.
- Cons:
  - Production inference values depending on a MUTABLE working-tree path: the staleness class
    #9/#16/#19 forbid, sitting on the inference path — the worst provenance posture available.
  - The DT-2 firewall weakens materially: a per-case table tweak becomes a filesystem act
    invisible to code review — the audited defect class returns by the back door.
  - Acceptable at all only with the compiled-in fingerprint check — duplicating D1's guarantee
    at higher residual risk plus D2's runtime failure mode (#6).
- Rating (a) principles: fails the spirit of #9/#16/#19 unless fortified into a worse D1.
  Rating (b) #4: the only option under which inference values can silently drift — a structural
  #4 hazard. **Not recommended even as a temporary bridge.**

**Recommendation: D1.** Constrained-optimum ledger: no option outperforms another on inference
when healthy — the optimized constraint is provenance integrity, and D1 dominates it; D2/D3
recorded above for re-test if distribution packaging ever becomes mandatory.

## 7. Decision E — scheduling the two ratified presentation publications

Both are ratified record and must not drop: the un-rounded modal reading (decision 1) and the
post-decode ornament labels (decision 4). Under rulings 2–3, neither increment size nor what
exists is a scheduling argument; what remains are establishment availability (#19) and the
switch commit's verification cleanliness (#15/#22/#13).

**The modal reading: inside this increment** — a published fact computed from already-fitted,
already-established emission quantities (#19 satisfied by what exists — carried-forward
establishment, the amendment's legitimate sense); part of the ratified surface (decision 1); no
principled ground for deferral remains. **Proposed as settled unless drafting finds an
establishment blocker, which returns it here with the blocker named.**

**The ornament labels — two options:**

**Option E-orn-1 — inside this increment.**
- Pros:
  - The ratified surface arrives whole — zero tracked-remainder risk (register rule (e)).
- Cons:
  - The derivation's independent validation resource is BCMH (named in the ratified decision-4
    record; reserved off-CV by OI-176 §6), and the BCMH dataset is NOT on disk (verified at the
    OI-185/OI-179 rows). Publishing with validation incomplete is lawful only status-marked
    unvalidated (evidence-publication amendment), with no consumer load-bearing (#19).
  - Coupling an establishment-incomplete publication to the switch commit mixes an open
    establishment question into the one commit whose verification must be airtight (#22/#13).
- Rating (a) principles: whole-surface fidelity bought by weakening the switch commit's
  establishment cleanliness. Rating (b) #4: none — presentation publication of
  already-computed facts.

**Option E-orn-2 — its own named increment, register row created in the same commit as this
ruling.**
- Pros:
  - The publication gets its own establishment event sized to its actual open question (the BCMH
    resource, #19); the switch commit stays a closed, fully-established event (#22/#13/#15).
  - Drop-out risk neutralized by the register mechanism itself: row at RULING TIME (register
    rule (c)) + the handoff visibility line — a declared #23 gap with a named exit.
- Cons:
  - The notation surface runs, for the gap, without one ratified publication — a real, declared,
    bounded #23 state; the row and visibility line are a CONDITION of this option.
- Rating (a) principles: compliant staging; the anti-drop-out guardrail satisfied by the
  register discipline. Rating (b) #4: identical to E-orn-1.

**Recommendation: modal reading inside the increment; ornament labels as their own increment
(E-orn-2) with the row created at ruling time.**

## 8. The increment's verification plan (fixed by standing policy, not a decision)

1. **Investigation first (standing rule; investigate-by-default):** the FIRST dispatch is
   read-only — the notation consumption-surface audit: every field of `HarmonicRegion` (and its
   nested records) actually read by the live consumers (`notationcomposingbridge`,
   `notationimplodebridge`, `notationtuningbridge`, `sectionanalyzer` and the downstream
   function-labeling readers, the accessibility surface), each with file:line. Under Decision A2
   this is what makes the #12 check exhaustive: every consumed fact gets a declared source on
   A's surface OR a declared retirement-with-rationale — no silent drops. It also enumerates
   every consumer keyed to exotic `KeySigMode` values (Decision C's disposition list) and the
   OI-182 exposure-bucket constants' fate.
2. **Build under the OI-180 sanction pattern:** the native record + in-app decode + posterior
   publication (B-slice first, B-full's marginal oracle as its own established step) + table
   codegen land behind the default-OFF driver; production byte-identity proven per commit (both
   suites + pipeline snapshots untouched) until the switch commit (#23; working method B).
3. **Establishment before the switch (#19/#15):** (a) the in-app path's decode on the 326
   covered corpus scores equals the adopted batch decode (`adoption_decode.json`) — same tables,
   weights, tie-break, through the app seam; (b) A's published record is field-exact to that
   decode on the inference fields; (c) the posterior slice reproduces the Python probe's
   published slice, and the B-full marginals pass their declared oracle (forward/backward
   equality, per-span mass normalization, synthetic-case agreement with the fit-arc lattice
   arithmetic) BEFORE publication; (d) because the record shape changes (A2), the full-surface
   comparison instruments for consumer OUTPUTS (annotations, chord track, tuning decisions,
   accessibility text) across the flip are declared and established BEFORE the flip (#15/#19).
4. **The switch is ONE revertible, user-ratified commit (#14/#22):** the notation path flips to
   A's record; pipeline-snapshot goldens are refreshed — this increment DOES change notation
   output, and the refresh precondition is the establishment record above, cited in the commit
   body (working method B: a golden refresh is never a reflex); notation unit tests disposed per
   kind (snapshot-class refreshed, unit-class STOP); CLAUDE.md staged-scope block, STATUS,
   ARCHITECTURE, the OI-178/OI-175/OI-180 rows and the handoff dual-path line all move in the
   same commit (#10).
5. **After the switch:** the retirement map (OI-180 §4) is executable — first candidates the
   dead 21-mode-prior plumbing (item 2), the `HarmonicRegion`/legacy-record retirement, and the
   L2/L4 items; OI-192's fifth-substitution refinement proceeds independently on the
   fitted-transition factor.

## 9. The rulings (asked and answered)

**All six granted by the user, 2026-07-26:** (1) the §2 principles amendment ratified; (2)–(6)
Decisions A2, B-full (slice-first, completion rowed OI-193), C1, D1, and the E split (modal
reading in-increment; ornament labels rowed OI-194) — all as recommended. The verification plan
(§8) stands as standing policy. This document is now part of the ratified record; the
ratification commit rides the first dispatch (`cc_instruction_notation_consumption_audit.md`,
Task 0).
