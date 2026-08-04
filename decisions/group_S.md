# Decisions group S — The guiding principles

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-165 — #1 - build only on established fact and theory

> 1. **Fact- and theory-based coding only.** Build only on established fact and theory —
>    published research, public algorithms, public software. Fact-finding (investigative)
>    coding is allowed.

**In plain words.** Nothing is built on a hunch. Every method comes from published research, a public algorithm, or public software. Investigating to find out what the facts are is a separate, permitted activity.

**Why.** Derivation not recorded as a separate defense - this is the founding premise the other principles are stated against. Its operational consequence is recorded: #3 makes an unexpected finding a failure of this principle rather than a curiosity (CLAUDE.md:14-16).

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:9`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:9-11, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-166 — #2 - target the specific open question, not the general topic

> 2. **Specific research over general.** Most research so far has been general or on
>    already-handled topics; target the specific open question.

**In plain words.** Research effort goes to the exact question in front of us, not to the surrounding subject generally or to something already handled.

**Why.** Stated constraint, CLAUDE.md:12-13: most research done so far has been general or on already-handled topics - the observation that motivates the rule.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:12`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:12-13, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-167 — #3 - an unexpected finding is a failure to diagnose, not a curiosity

> 3. **An unexpected finding means we have failed #1** (and possibly #2, #4, #6). Surprise
>    signals that the fact/theory basis was incomplete — treat it as a failure to diagnose,
>    not a curiosity.

**In plain words.** Being surprised means the facts and theory we built on were incomplete. Surprise is treated as a defect in our own understanding, not as an interesting result.

**Why.** Stated constraint, CLAUDE.md:14-15: surprise signals that the fact and theory basis was incomplete, which is a failure of #1. Its operational form is #13 - surface it as a stop before building around it.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:14`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:14-16, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-168 — #4 - the long-term goal is maximum-precision inference

> 4. **Long-term goal: maximum-precision inference.**

**In plain words.** The objective the whole project is measured against is getting the analysis as accurate as it can be made.

**Why.** Derivation not recorded - this is the stated objective, not a decision derived from something else. It is what the decision-neutrality corollary (CLAUDE.md:106-118) means by 'the ultimate objective'.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:17`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:17, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-169 — #5 - when facts may be scarce, investigate

> 5. **Investigate when facts may be scarce.** If we are unsure whether facts are scarce,
>    gather more facts.

**In plain words.** If it is unclear whether we know enough about something, the answer is to go and find out, not to proceed on what we have.

**Why.** Stated constraint, CLAUDE.md:85-89 (the scope-of-surprise rule): explorational runs whose purpose is to eliminate ignorance are exactly where surprises are permitted - so fact-finding is the cheap stage that keeps surprises out of the expensive one.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:18`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:18-19, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-170 — #6 - total unification: one path per concern

> 6. **Total unification — no duplication of any code.** One path per concern.

**In plain words.** There is exactly one implementation of any given concern. No duplicated code, no second place the same question is answered.

**Why.** Measurement named elsewhere in the record: `cowork_siloed_facts_audit.md` found 17 instances of facts being re-derived rather than read (CLAUDE.md:94-95), and open_items/OI-173 records four inequivalent definitions of one predicate as the cost of a second path. The end-state reading is fixed by #23 and by the decision-neutrality corollary (CLAUDE.md:116-118): #6 is a structural end-state principle, not a preservation claim for whatever exists now.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:20`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:20, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-171 — #7 - a layer is enhanced only with what belongs to it

> 7. **Adhere to layers.** Enhance a layer only with algorithms/methods that belong to it,
>    nothing else. Worst case, this forces a layer redesign rather than a cross-layer patch.

**In plain words.** A stage of the analysis gets only the methods that are properly its own. If the right method does not belong there, the layers are redesigned rather than the method smuggled across.

**Why.** Stated constraint, CLAUDE.md:22: the worst case is a layer redesign, which is explicitly preferred to a cross-layer patch.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:21`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:21-22, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-172 — #8 - no inference-problem-driven coding until every method sits in its correct layer

> 8. **No inference-problem-driven coding until all methods and algorithms are implemented
>    in their correct layer.**

**In plain words.** Work is not steered by whichever analysis error is currently visible. Until the structure is built out, a fix is made at the stage that owns it, at the time that stage is being built.

**Why.** Derivation not recorded as a separate defense. The related recorded position is that a fix at its #8-correct stage is 'never a knob-turn' - the phrase carried on the open-item rows that defer a fix for this reason (for example open_items/OI-192, OI-216, OI-217).

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:23`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:23-24, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-173 — #9 - measure only on corpora known to be non-stale and accurate

> 9. **Test and measure only on corpora known to be non-stale and accurate.**

**In plain words.** A measurement is only run against music whose annotations are current and correct.

**Why.** Sharpened by #21 (CLAUDE.md:61-65): the accuracy of ground truth is itself a measured quantity rather than an assumed one, so 'accurate' means measured per-axis annotator agreement, not an assumption.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:25`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:25, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-174 — #10 - documentation always in sync with code

> 10. **Documentation always in sync with code.**

**In plain words.** The documents describing the system never lag behind the system.

**Why.** Stated constraint, ARCHITECTURE.md:6757: stale documentation is worse than no documentation because it actively misleads. The same-commit rule that operationalizes it is at ARCHITECTURE.md:6756-6759.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:26`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:26, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-175 — #11 - regression tests in sync with code, and run between iterations

> 11. **Regression test cases always in sync with code; regression-test between iterations.**

**In plain words.** The tests that guard against going backwards are kept current with the code, and they are run between each step of work rather than at the end.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:27`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:27, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-176 — #13 - surface a surprise as a stop before building around it

> 13. **Surface a surprise as a STOP before building around it** (the operational form of #3).

**In plain words.** When something unexpected turns up, work halts and it is reported. It is never quietly worked around.

**Why.** Stated constraint, CLAUDE.md:31: this is the operational form of #3 - if surprise means the fact basis was incomplete, then building on top of the surprise builds on the same incomplete basis.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:31`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:31; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-177 — #14 - every behavior change is one user-ratified, revertible, provenance-stamped commit

> 14. **Every behavior change is user-ratified as one revertible, provenance-stamped commit.**

**In plain words.** Anything that changes what the system does is ratified by the user first, lands as a single commit that can be undone whole, and carries the record of where it came from.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:32`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:32; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-178 — #15 - verify at the objects on the full output surface, never at an assertion

> 15. **Verify at objects/data on the full output surface, never at assertion** (winner *and*
>     carry, not the winner alone).

**In plain words.** A result is confirmed by looking at the actual data it produced, across everything it produced - the chosen reading and the alternatives carried beside it - not by a test that asserts what was expected.

**Why.** Stated constraint, CLAUDE.md:33-34: checking the winner alone would miss a change in the carried alternatives, which are part of the published surface (#12).

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:33`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:33-34; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-179 — #16 - every measurement is stamped to its corpus and its tooling, and the outgoing reference is snapshotted

> 16. **Reproducibility.** Every measurement is stamped to corpus-hash + instrument-commit;
>     snapshot the outgoing reference before any re-baseline.

**In plain words.** A measurement records which music it was run on and which version of the measuring code produced it, and the previous reference numbers are saved before new ones replace them.

**Why.** Stated constraint, CLAUDE.md:75-78 (#24): reproducibility bounds the error the measuring tools introduce, as the companion of the sampling error #24 bounds - so a number without both is not interpretable.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:35`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:35-36; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-180 — #17 - the Premise Gate

> 17. **The Premise Gate.** Before any inference-affecting design is built or probed:
>     (a) a **premise ledger** — every load-bearing causal claim explicitly labeled **FACT**
>     (citation to code/measurement), **THEORY** (citation to published research answering the
>     *specific* question, #2), or **ASSUMPTION**; (b) a **written quantitative prediction per
>     assumption** (fire-rate, magnitude, direction, population) recorded *before* measuring —
>     no prediction, no build; (c) a **desk simulation** — trace the mechanism by hand through
>     the intended architecture on 3–5 real corpus cases drawn from the known failing sets,
>     answering FIRST "does the mechanism FIRE on this case?" (control flow — ratified sharpening
>     2026-07-10, the EG-2 desk-sim lesson), THEN "which term moves, by how much?" (arithmetic);
>     (d) every **proxy→target
>     link is itself a ledger premise** (a structural proxy never stands in for a behavioral
>     quantity unvalidated); (e) every **insulation claim** ("X cannot affect Y") must enumerate
>     the false-negative path explicitly; (f) **no hand-transcribed measurement numbers** —
>     figures enter docs only via generated artifacts (the `manifest.json` pattern).

**In plain words.** Before anything that affects the analysis is built or even probed: every load-bearing causal claim is written down and labelled as an established fact, a published theory, or an assumption; every assumption gets a written numerical prediction BEFORE anything is measured; the mechanism is traced by hand through three to five real failing cases, asking first whether it fires at all and only then what it changes; any stand-in quantity must itself be justified; any claim that one thing cannot affect another must name how it could; and no number enters a document by being typed in by hand.

**Why.** Measurement, CLAUDE.md:44-45: part (c)'s fire-first ordering is a ratified sharpening from a specific failure - the desk simulation that traced arithmetic through a mechanism which, on the real case, never fired. Part (f)'s reason is recorded across the decisions register as the generated-artifact pattern: a hand-transcribed figure cannot be re-derived, and the harvest's own counts drifted one regeneration stale exactly that way.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:37`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:37-50; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-181 — #18 - an unverified causal premise is forbidden (Class A)

> 18. **Unverified causal premises are FORBIDDEN (Class A).** No design may carry load on a
>     causal claim about our own system or data that is checkable but unchecked.

**In plain words.** No design may rest on a claim about how our own system or data behaves when that claim could be checked and has not been.

**Why.** Stated constraint, CLAUDE.md:51-52: the prohibition is specifically about claims that are CHECKABLE - the cost of checking is what makes leaving them unchecked indefensible.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:51`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:51-52; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-182 — #19 - an unestablished measurement tool is forbidden (Class B)

> 19. **Unestablished instruments are FORBIDDEN (Class B).** An instrument, corpus, gate, or
>     recorded figure is trusted only after being *positively established* (oracle cross-check,
>     derivation of what the measurement unit actually measures, reproduce-check) — never
>     because it is merely unfalsified.

**In plain words.** A measuring script, a corpus, a gate or a recorded figure is trusted only once it has been positively shown to be right - checked against an independent oracle, with a derivation of what its unit actually measures, and a reproduce-check. Never merely because nothing has contradicted it.

**Why.** Stated constraint, CLAUDE.md:55-56: 'never because it is merely unfalsified' - absence of contradiction is not evidence, so establishment has to be a positive act.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:53`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:53-56; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-183 — #20 - fit and evaluation are separated

> 20. **Fit/evaluation separation.** No value is graded on data that helped fit it. Every fit
>     event declares its held-out data (split or k-fold) and its capacity budget (parameter
>     count, regularization, justified against corpus size) BEFORE fitting; the headline claim
>     is the held-out figure. A fitted-and-self-measured number is not established (#19).

**In plain words.** No number is graded on the same music that helped choose it. Before any fitting, the held-back music and the budget of how many free values may be fitted are declared; the headline figure is always the one measured on the held-back music.

**Why.** Stated constraint, CLAUDE.md:60: a value fitted and then measured on its own fitting data is not established at all (#19) - the figure describes the fitting, not the system.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:57`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:57-60; ratified by the user 2026-07-18 at the joint-estimator plan review, analysis `cowork_joint_estimator_architecture.md` §6/§7 (CLAUDE.md:125-129). The ratified protocols are open_items/OI-176 and OI-177.

### D-184 — #21 - ground truth is a measurement tool too, and its accuracy is measured

> 21. **Ground truth is an instrument too.** The accuracy of ground truth is itself a measured
>     quantity — per-axis annotator agreement, not an assumed binary (sharpens #9's "accurate").
>     Every precision target and every "irreducible residual" verdict is interpreted against
>     that measured ceiling; without it, structural error and annotator disagreement are
>     indistinguishable in the residual.

**In plain words.** How right the reference annotations are is itself something to be measured - how far annotators agree with each other, axis by axis - not assumed. Every precision target and every claim that a remaining error is irreducible is read against that measured ceiling.

**Why.** Stated constraint, CLAUDE.md:63-65: without the measured ceiling, our own structural error and disagreement between annotators are indistinguishable in what is left over - so an 'irreducible residual' verdict cannot be made at all.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:61`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:61-65; ratified by the user 2026-07-18 (CLAUDE.md:125-129). Sharpens #9.

### D-185 — #22 - every hard gate declares in advance how it handles the largest change it will meet

> 22. **Every hard gate carries a pre-declared protocol for the largest change it will face.**
>     A gate written only for incremental change must not be amended under the pressure of a
>     live diff — the exceptional-event variant (e.g. architecture-scale adoption: aggregate
>     criterion + explained diff + snapshot + ratification) is written and ratified before such
>     a change is on the table.

**In plain words.** A rule that decides whether a change may ship must say, before the fact, what it does when the change is far bigger than the incremental ones it was written for. It must never be rewritten while such a change is sitting in front of it.

**Why.** Stated constraint, CLAUDE.md:67-68: a gate amended under the pressure of a live difference is no longer a gate. The exceptional-event variant this required was written and ratified as open_items/OI-178 before the joint estimator's first decode was measured against the stop.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:66`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:66-70; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-186 — #23 - an end-state principle needs a lawful transition

> 23. **End-state principles need lawful transitions.** When a planned change must temporarily
>     violate an end-state principle (e.g. #6, one path per concern, during a parallel build),
>     the violation is declared, bounded, and pre-ratified with a retirement map — migration is
>     a first-class state, never an undeclared exception.

**In plain words.** When a planned piece of work must temporarily break a principle that describes the finished state - such as building a second analysis path beside the first - the breach is declared, bounded, and approved in advance together with the plan for removing it.

**Why.** Stated constraint, CLAUDE.md:73-74: migration is a first-class state, never an undeclared exception - the alternative being a temporary duplicate that nobody is obliged to remove. The instance is open_items/OI-180, the sanctioned dual path.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:71`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:71-74; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-187 — #24 - every reported figure carries its uncertainty

> 24. **Every reported figure carries its uncertainty.** Sampling noise on the measurement
>     corpus is quantified; a difference within the uncertainty is not a finding, and no
>     decision rests on one. (The companion of #16: reproducibility bounds instrument error,
>     this bounds sampling error.)

**In plain words.** How much a measured number could move by chance, given how much music it was measured on, is quantified and reported with it. A difference inside that range is not a finding and no decision may rest on one.

**Why.** Stated constraint, CLAUDE.md:77-78: this is the companion of #16 - reproducibility bounds the error the measuring tools introduce, and this bounds the error the sample introduces.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:75`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:75-78; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-188 — The constrained-optimum ledger corollary

> *Ledger corollary to #17 (ratified with #20–#24):* when a decision selects a **constrained
> optimum** (a design chosen for methodology-compliance rather than raw measured performance),
> the ledger records what the unconstrained best known alternative is and why it is excluded —
> so a future reader can re-test whether the constraint still binds.

**In plain words.** When a design is chosen because it complies with the method rather than because it measured best, the record must name what the best-performing alternative actually was and why it is ruled out.

**Why.** Stated constraint, CLAUDE.md:82-83: so that a future reader can re-test whether the constraint still binds - without the excluded alternative on record, a constraint that has since been lifted is invisible.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:80`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:80-83; ratified with #20-#24 by the user 2026-07-18 (CLAUDE.md:125-129).

### D-189 — The scope of surprise, and the three-stage funnel

> *Scope of surprise (ratified with #17–19):* surprises are **allowed in explorational runs**
> whose purpose is to eliminate ignorance (#5 fact-finding); they are **NOT allowed when building
> actual inference code** — there, a surprise is a STOP (#13) and evidence the Premise Gate was
> not satisfied. The stage funnel: **desk-simulate (hours) → read-only probe (a session) → build
> (an arc)** — each stage kills bad premises before the next pays for them.

**In plain words.** Being surprised is allowed - expected, even - in exploratory work whose whole purpose is to remove ignorance. It is not allowed while building the analysis itself: there a surprise stops the work and shows the Premise Gate was not satisfied. The order of work is: trace it by hand for hours, then probe it read-only for a session, then build it.

**Why.** Stated constraint, CLAUDE.md:89: each stage kills bad premises before the next one pays for them - the funnel is ordered by what a wrong premise costs at that stage.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:85`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:85-89; ratified with #17-#19 by the user 2026-07-10 (CLAUDE.md:122-125).

### D-190 — The decision-neutrality corollary - what exists carries no weight in choosing a design

> *Decision-neutrality of the existing implementation (corollary to #4/#6/#19; user-ratified
> 2026-07-26):* Designs are chosen from the principles and the ultimate objective — enabling the
> best possible inference — alone. In that choice: **(a)** the value of reusing existing code, and
> the cost of making existing code obsolete, are SECONDARY — they may break ties between designs
> equal under the principles and the objective, and reuse counts only as carried-forward
> establishment (#19), never as sunk cost or saved effort; **(b)** downstream implementation
> impact — whether and how many consumers must change — carries NO weight; **(c)**
> end-user-visible behavior change carries NO weight (the 2026-07-26 unshipped-scoping ruling),
> while every behavior change remains ratification-gated (#14) and verification-gated (#15/#19)
> exactly as before. The best-possible-inference design is chosen first; what exists then either
> serves it or retires. (This does not weaken #6 — one path per concern is an END-STATE structural
> principle, not a preservation claim for the existing path; nor #19 — establishment must still
> exist before trust.)

**In plain words.** A design is chosen on the principles and the goal of the best possible analysis, and on nothing else. What it would cost to make existing code obsolete is a secondary consideration that can only break a tie between designs already equal; how many places downstream would have to change counts for nothing; and a change in what the user sees counts for nothing either - though every such change still needs ratifying and verifying exactly as before. The best design is chosen first, and what exists then either serves it or is retired.

**Why.** Stated constraint, CLAUDE.md:110-111 and :116-118: reusing existing code counts only as establishment already carried forward (#19), never as effort saved or cost sunk; and the corollary is explicitly said not to weaken #6 - one path per concern is an end-state structural principle, not a claim that the existing path is the one to preserve.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `CLAUDE.md:106`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:106-118; user-ratified 2026-07-26 at the notation-layer adoption increment's decision surface, analysis `cowork_notation_adoption_increment.md` §2 (CLAUDE.md:129-131).

### D-200 — Make it work first; compromise on performance only if performance proves a problem

> **MAKE IT WORK FIRST; COMPROMISE ON PERFORMANCE ONLY IF PERFORMANCE PROVES TO BE A PROBLEM
> (user-directed, 2026-07-28, at the analysis-cost session).** Getting the inference right comes
> first. Runtime speed is traded against it only once slowness has actually turned out to be a

**In plain words.** Getting the analysis right comes first. Speed is traded against it only once slowness has actually turned out to be a problem. That does not make speed unimportant - it puts it second: anything that makes the same computation faster is free on every principle and is done first, and the settings that buy speed by giving up precision are the last resort, not the first.

**Why.** Stated constraint, cowork_handoff.md:361-364: work that makes the same computation faster costs nothing on any principle axis, so it must be exhausted BEFORE anything that trades precision for speed - which is what sequences the effort dial and the analysis-extent question last rather than demoting them.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md:1108-1110`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at cowork_handoff.md (the user's rulings at the analysis-cost session, 2026-07-28), a session handoff block that ages into an archive outside the session-start read. It corrects a Cowork misreading of 'implementation efficiency is not very relevant', which meant BUILD effort, not runtime. OPEN_ITEMS OI-240 closes on this move

### D-201 — Very large scores must be handled, and are expected to be more common than our corpora

> **Very large scores MUST be handled, and are expected to be a MORE COMMON use than our corpora.** A
> Wagner act or a symphony has to produce an analysis; the user expects such music to be a more common

**In plain words.** A Wagner act or a symphony must work. The user expects such scores to be a more common use than the chorales the system was fitted on. This is a standing requirement every later design is judged against, not a defect report.

**Why.** Stated constraint, OPEN_ITEMS.md:157: the requirement is recorded together with the collision it creates - the joint estimator's ratified tractability envelope is chorale size (60-150 events), and the fitted corpus is 326 Bach chorales by one composer.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `ARCHITECTURE.md:1013-1014`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:157 (OI-209) with open_items/OI-209.md, which tracks the requirement rather than housing it. Consumed by the analysis-extent question (OI-210), the corpus onboarding (OI-38), and the architecture step-back (OI-200). The measured collision is OI-215/OI-227 - the decode returns nothing on 13 of 23 committed large scores. OPEN_ITEMS OI-240 closes on this move

### D-202 — The effort control is one setting with several dials, and it must bound the time taken

> **The effort control is ONE setting with several dials behind it, and among the quantities it must
> bound is the TIME the analysis takes. DEFERRED.** How hard the analysis works is a single user-facing

**In plain words.** How hard the analysis works is a single setting the user turns, not several. Behind it sit several dials, and among the things it must be able to bound is how long the analysis takes. It is too early to build: which pieces of the analysis have to be switchable is not yet known.

**Why.** Stated constraint, OPEN_ITEMS.md:157: it is too early to implement until we know FACTUALLY which pieces must be switchable - which is a measurement, and the measurement is what the analysis-cost dispatch was for. The user's recorded prediction beside it: 'always read the entire score will VERY likely not survive (maybe only under some effort setting = EXTREME)'.

**Status.** DEFERRED · decided 2026-07-28 · ratified by user

**Home.** `ARCHITECTURE.md:1021-1022`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:157 (OI-209). The two standing design rules the effort control must satisfy are older and are stated in ARCHITECTURE.md §2.14 (D-035). OPEN_ITEMS OI-240 closes on this move

### D-203 — Candidate admission is completion, not refinement - so #8 permits fixing it now

> **CANDIDATE ADMISSION IS COMPLETION, NOT REFINEMENT — so #8 permits fixing it now (user-ruled
> 2026-07-28, at the OI-199 pass-2 session).** The rule that decides which chord classes the joint
> decoder will even consider is a piece that was never finished, not a refinement of something already

**In plain words.** The rule that decides which chords the decoder will even consider is not a refinement of something already built - it is a piece that was never finished. So the principle that forbids chasing visible analysis errors before the structure is complete does not block fixing it.

**Why.** Stated constraint, cowork_handoff.md:31-32: the design happens ONCE over the whole family, never per symptom (#6/#7) - which is why the fix is deferred until the family is enumerated even though #8 permits it. The measured family: OI-215 (the sparse member-overlap gate), OI-227 (the dense fit gate), OI-226 (admission has no ratified basis), OI-228 (the emission reads struck rather than sounding notes).

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md:1118-1120`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at cowork_handoff.md, the user's ruling at the OI-199 pass-2 session, 2026-07-28. Homed beside #8 in CLAUDE.md because it is a ruling about what #8 permits; what the admission rule IS, and that it has no specified form, is in the estimator's own specification (D-098) and at OPEN_ITEMS OI-226. Cross-read with STATUS.md's earlier note that the classification 'is the user's to settle' - this row records that it was settled. OPEN_ITEMS OI-240 closes on this move

### D-204 — One fix is designed once over the whole enumerated family, never per symptom

> **ONE FIX IS DESIGNED ONCE OVER THE WHOLE ENUMERATED FAMILY, NEVER PER SYMPTOM (user-ruled
> 2026-07-28, at the OI-199 pass-2 session).** When several observed faults turn out to share a cause,
> the remedy is designed once for all of them together, at the layer that owns the cause; fixing

**In plain words.** When several observed faults turn out to share a cause, the remedy is designed once for all of them together. Fixing whichever one is currently visible, on its own, is the error the one-path-per-concern and layer principles exist to prevent.

**Why.** Stated constraint, cowork_handoff.md:28-29 and #3: the fix is deferred BY DESIGN until the whole family is known, because designing over part of a family is the patch-per-symptom error. The instance that produced the rule: the empty-decode cliff turned out to have a sibling at the opposite end of the density spectrum (OI-227) and an emission-side twin (OI-228), neither visible from the first symptom.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md:1129-1131`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at cowork_handoff.md, recorded at the OI-199 pass-2 session, 2026-07-28. OPEN_ITEMS OI-240 closes on this move

### D-205 — A human acts as ground truth where no formal ground truth exists

> **A HUMAN acts as ground truth where no formal ground truth exists (user-decided 2026-07-13).** For
> repertoire nobody has published an analysis of, the reference answer is a person's judgment. That person
> may reach it by any method they choose, **including** letting an automated triage judge point them at the

**In plain words.** For music nobody has published an analysis of, the reference answer is a person's judgment. They may reach it however they like, including by letting an automated judge point them at the passages most likely to be wrong. That judge is guidance for the human, never a grader and never a number we report.

**Why.** Stated constraint, open_items/OI-56.md:7: a language-model judge is not ground truth (#9, and the standing rule that music21 corroborates but does not adjudicate), so it could never grade us - at most it can triage, by pointing a human at the scores most likely wrong.

**Status.** LIVE · decided 2026-07-13 · ratified by user

**Home.** `ARCHITECTURE.md:6802-6804`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at open_items/OI-56.md:7, decided by the user 2026-07-13. The when-question is tied to the corpus-onboarding event (OI-38) and the timing is itself open. OPEN_ITEMS OI-240 closes on this move

### D-206 — Intonation is held as a future feature, and is a declared future consumer of the analysis

> **Status of this whole section — HELD, and a declared future CONSUMER of the analysis (user-decided
> 2026-07-13).** Intonation **is** a future feature: the six unbuilt items specified in §11.3a–g, together
> with the tie limitation recorded there, stay on the books as a deliberate long-horizon hold, revisited at a

**In plain words.** The six unbuilt pieces of the tuning design stay on the books as a deliberate long-horizon hold, revisited at a natural pause in the analysis work. The reason the hold is strategic rather than neglect: tuning will read the analysis - knowing the mode, the chord, its function and the progression is what lets a just-intonation decision be made, particularly the decision about staying in tune over time versus letting the pitch drift.

**Why.** Stated constraint, open_items/OI-62.md:7: intonation is a named future CONSUMER of the published analysis surfaces - a concrete instance of the rule that evidence is published broadly so a future design can recognize facts it would never have thought to ask for (D-100's 2026-07-12 amendment).

**Status.** DEFERRED · decided 2026-07-13 · ratified by user

**Home.** `ARCHITECTURE.md:5142-5144`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at open_items/OI-62.md:7, decided by the user 2026-07-13. The six unbuilt items are specified at ARCHITECTURE.md §11.3a-g and confirmed absent from the code in that row. OPEN_ITEMS OI-240 closes on this move

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_engage_arc_plan.md:102-107`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** cowork_engage_arc_plan.md:3 records the user's ratification of this plan, dated 2026-07-07; the gate at :97-102, amended 2026-07-10 to become the middle stage of the Premise-Gate funnel (:128-130). The CLAUDE.md principles provenance paragraph names this gate, in this file, as a companion standing rule; register entry D-189 records the funnel it sits in. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

