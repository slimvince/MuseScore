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

### D-172 — #8 - no inference-problem-driven coding until the refactoring, the architectural design and the algorithmic completion are done

> 8. **No inference-problem-driven coding until the refactoring, the architectural design and the
>    algorithmic completion are done.** Build-it-right comes BEFORE tune-precision, strictly. All
>    three must be finished, not the last alone: every method and algorithm implemented in its
>    correct layer, the architecture designed, and the refactoring carried out.

**In plain words.** Work is not steered by whichever analysis error is currently visible. Until the system is built right - the refactoring carried out, the architecture designed, and every method and algorithm finished in its correct layer - no fix is made because an analysis result is wrong. All three must be done, not the last alone.

**Why.** Derivation not recorded as a separate defense. The related recorded position is that a fix at its #8-correct stage is 'never a knob-turn' - the phrase carried on the open-item rows that defer a fix for this reason (for example open_items/OI-192, OI-216, OI-217).

**Status.** LIVE · date not stated · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:23-26`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:23-26, the user's standing list. ★ WIDENED 2026-08-04 on the user's ruling (READ WAVE 5, dispatch `cc_instruction_reads_5.md` §0a ruling R2), which homed the build-it-right-before-tune-precision rule here in the fuller form **D-557** carried. The verbatim above is re-taken at the widened text. **THE FORMER VERBATIM, PRESERVED (#12):** "8. **No inference-problem-driven coding until all methods and algorithms are implemented    in their correct layer.**" **★ THE WIDENED RULE WAS NOT DECIDED ON 2026-08-04 — IT WAS USER-RATIFIED 2026-06-25 AND WAS LIVING IN THE WRONG DOCUMENT (carried here 2026-08-04 on the user's ruling R3, READ WAVE 6, dispatch `cc_instruction_reads_6.md` Task 3).** The date is verified at this entry's own home rather than taken from the dispatch: CLAUDE.md:30-32 states that `cowork_l1l3_stabilization_plan.md` "has carried the fuller three-clause form — refactoring + architectural design + algorithmic completion — user-ratified 2026-06-25". The 2026-08-04 act moved that already-ratified form into the governing document and widened the narrower statement standing here; it decided nothing about the rule's content. The `date` field stays "not stated" because it dates THE PRINCIPLE, which CLAUDE.md:120-132 records as part of the user's undated standing list 1-11 — the 2026-06-25 ratification is of the widened WIDTH and is recorded here, where the record can carry it without asserting a date the principle does not have. **★ THE DUPLICATION IS RESOLVED (user's ruling R3, same act; `OPEN_ITEMS.md` OI-329):** D-557 was re-homed to this same principle on 2026-08-04, so two live entries recorded one rule at one home — the duplication #6 forbids. **D-172 SURVIVES as #8's entry and D-557 is `superseded-by D-172`**, with D-557's former home (`cowork_l1l3_stabilization_plan.md:14-22`) and its former verbatim preserved in its own provenance (#12). Nothing about either DECISION changed. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review. **★ #8 POINTS at D-592 (what FINISHED means for a layer) and D-593 (the line inside the build-it-right firewall) as of 2026-08-04, ruling R2 — a pointer, never a copy (#6): the principle states WHEN inference work may start, D-592 states what "done" means per layer, and D-593 states what may still be fixed while the gate holds.**

### D-173 — #9 - measure only on corpora known to be non-stale and accurate

> 9. **Test and measure only on corpora known to be non-stale and accurate.**

**In plain words.** A measurement is only run against music whose annotations are current and correct.

**Why.** Sharpened by #21 (CLAUDE.md:61-65): the accuracy of ground truth is itself a measured quantity rather than an assumed one, so 'accurate' means measured per-axis annotator agreement, not an assumption.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:50`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:25, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-174 — #10 - documentation always in sync with code

> 10. **Documentation always in sync with code.**

**In plain words.** The documents describing the system never lag behind the system.

**Why.** Stated constraint, ARCHITECTURE.md:6757: stale documentation is worse than no documentation because it actively misleads. The same-commit rule that operationalizes it is at ARCHITECTURE.md:6756-6759.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:51`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:26, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-175 — #11 - regression tests in sync with code, and run between iterations

> 11. **Regression test cases always in sync with code; regression-test between iterations.**

**In plain words.** The tests that guard against going backwards are kept current with the code, and they are run between each step of work rather than at the end.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:52`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:27, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-176 — #13 - surface a surprise as a stop before building around it

> 13. **Surface a surprise as a STOP before building around it** (the operational form of #3).

**In plain words.** When something unexpected turns up, work halts and it is reported. It is never quietly worked around.

**Why.** Stated constraint, CLAUDE.md:31: this is the operational form of #3 - if surprise means the fact basis was incomplete, then building on top of the surprise builds on the same incomplete basis.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:66`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:31; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-177 — #14 - every behavior change is one user-ratified, revertible, provenance-stamped commit

> 14. **Every behavior change is user-ratified as one revertible, provenance-stamped commit.**

**In plain words.** Anything that changes what the system does is ratified by the user first, lands as a single commit that can be undone whole, and carries the record of where it came from.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:67`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:32; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-178 — #15 - verify at the objects on the full output surface, never at an assertion

> 15. **Verify at objects/data on the full output surface, never at assertion** (winner *and*
>     carry, not the winner alone).

**In plain words.** A result is confirmed by looking at the actual data it produced, across everything it produced - the chosen reading and the alternatives carried beside it - not by a test that asserts what was expected.

**Why.** Stated constraint, CLAUDE.md:33-34: checking the winner alone would miss a change in the carried alternatives, which are part of the published surface (#12).

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:68`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:33-34; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-179 — #16 - every measurement is stamped to its corpus and its tooling, and the outgoing reference is snapshotted

> 16. **Reproducibility.** Every measurement is stamped to corpus-hash + instrument-commit;
>     snapshot the outgoing reference before any re-baseline.

**In plain words.** A measurement records which music it was run on and which version of the measuring code produced it, and the previous reference numbers are saved before new ones replace them.

**Why.** Stated constraint, CLAUDE.md:75-78 (#24): reproducibility bounds the error the measuring tools introduce, as the companion of the sampling error #24 bounds - so a number without both is not interpretable.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:70`  — a project-wide convention with no owning layer; this is its correct home.

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

**Home.** `CLAUDE.md:72`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:37-50; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-181 — #18 - an unverified causal premise is forbidden (Class A)

> 18. **Unverified causal premises are FORBIDDEN (Class A).** No design may carry load on a
>     causal claim about our own system or data that is checkable but unchecked.

**In plain words.** No design may rest on a claim about how our own system or data behaves when that claim could be checked and has not been.

**Why.** Stated constraint, CLAUDE.md:51-52: the prohibition is specifically about claims that are CHECKABLE - the cost of checking is what makes leaving them unchecked indefensible.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:102`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:51-52; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-182 — #19 - an unestablished measurement tool is forbidden (Class B)

> 19. **Unestablished instruments are FORBIDDEN (Class B).** An instrument, corpus, gate, or
>     recorded figure is trusted only after being *positively established* (oracle cross-check,
>     derivation of what the measurement unit actually measures, reproduce-check) — never
>     because it is merely unfalsified.

**In plain words.** A measuring script, a corpus, a gate or a recorded figure is trusted only once it has been positively shown to be right - checked against an independent oracle, with a derivation of what its unit actually measures, and a reproduce-check. Never merely because nothing has contradicted it.

**Why.** Stated constraint, CLAUDE.md:55-56: 'never because it is merely unfalsified' - absence of contradiction is not evidence, so establishment has to be a positive act.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:104`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:53-56; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-183 — #20 - fit and evaluation are separated

> 20. **Fit/evaluation separation.** No value is graded on data that helped fit it. Every fit
>     event declares its held-out data (split or k-fold) and its capacity budget (parameter
>     count, regularization, justified against corpus size) BEFORE fitting; the headline claim
>     is the held-out figure. A fitted-and-self-measured number is not established (#19).

**In plain words.** No number is graded on the same music that helped choose it. Before any fitting, the held-back music and the budget of how many free values may be fitted are declared; the headline figure is always the one measured on the held-back music.

**Why.** Stated constraint, CLAUDE.md:60: a value fitted and then measured on its own fitting data is not established at all (#19) - the figure describes the fitting, not the system.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:108`  — a project-wide convention with no owning layer; this is its correct home.

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

**Home.** `CLAUDE.md:112`  — a project-wide convention with no owning layer; this is its correct home.

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

**Home.** `CLAUDE.md:135`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:66-70; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-186 — #23 - an end-state principle needs a lawful transition

> 23. **End-state principles need lawful transitions.** When a planned change must temporarily
>     violate an end-state principle (e.g. #6, one path per concern, during a parallel build),
>     the violation is declared, bounded, and pre-ratified with a retirement map — migration is
>     a first-class state, never an undeclared exception.

**In plain words.** When a planned piece of work must temporarily break a principle that describes the finished state - such as building a second analysis path beside the first - the breach is declared, bounded, and approved in advance together with the plan for removing it.

**Why.** Stated constraint, CLAUDE.md:73-74: migration is a first-class state, never an undeclared exception - the alternative being a temporary duplicate that nobody is obliged to remove. The instance is open_items/OI-180, the sanctioned dual path.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:140`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:71-74; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-187 — #24 - every reported figure carries its uncertainty

> 24. **Every reported figure carries its uncertainty.** Sampling noise on the measurement
>     corpus is quantified; a difference within the uncertainty is not a finding, and no
>     decision rests on one. (The companion of #16: reproducibility bounds instrument error,
>     this bounds sampling error.)

**In plain words.** How much a measured number could move by chance, given how much music it was measured on, is quantified and reported with it. A difference inside that range is not a finding and no decision may rest on one.

**Why.** Stated constraint, CLAUDE.md:77-78: this is the companion of #16 - reproducibility bounds the error the measuring tools introduce, and this bounds the error the sample introduces.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:144`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:75-78; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-188 — The constrained-optimum ledger corollary

> *Ledger corollary to #17 (ratified with #20–#24):* when a decision selects a **constrained
> optimum** (a design chosen for methodology-compliance rather than raw measured performance),
> the ledger records what the unconstrained best known alternative is and why it is excluded —
> so a future reader can re-test whether the constraint still binds.

**In plain words.** When a design is chosen because it complies with the method rather than because it measured best, the record must name what the best-performing alternative actually was and why it is ruled out.

**Why.** Stated constraint, CLAUDE.md:82-83: so that a future reader can re-test whether the constraint still binds - without the excluded alternative on record, a constraint that has since been lifted is invisible.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:149`  — a project-wide convention with no owning layer; this is its correct home.

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

**Home.** `CLAUDE.md:154`  — a project-wide convention with no owning layer; this is its correct home.

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

**Home.** `CLAUDE.md:175`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:106-118; user-ratified 2026-07-26 at the notation-layer adoption increment's decision surface, analysis `cowork_notation_adoption_increment.md` §2 (CLAUDE.md:129-131).

### D-200 — Make it work first; compromise on performance only if performance proves a problem

> **MAKE IT WORK FIRST; COMPROMISE ON PERFORMANCE ONLY IF PERFORMANCE PROVES TO BE A PROBLEM
> (user-directed, 2026-07-28, at the analysis-cost session).** Getting the inference right comes
> first. Runtime speed is traded against it only once slowness has actually turned out to be a

**In plain words.** Getting the analysis right comes first. Speed is traded against it only once slowness has actually turned out to be a problem. That does not make speed unimportant - it puts it second: anything that makes the same computation faster is free on every principle and is done first, and the settings that buy speed by giving up precision are the last resort, not the first.

**Why.** Stated constraint, cowork_handoff.md:361-364: work that makes the same computation faster costs nothing on any principle axis, so it must be exhausted BEFORE anything that trades precision for speed - which is what sequences the effort dial and the analysis-extent question last rather than demoting them.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md:1327-1329`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at cowork_handoff.md (the user's rulings at the analysis-cost session, 2026-07-28), a session handoff block that ages into an archive outside the session-start read. It corrects a Cowork misreading of 'implementation efficiency is not very relevant', which meant BUILD effort, not runtime. OPEN_ITEMS OI-240 closes on this move

### D-201 — Very large scores must be handled, and are expected to be more common than our corpora

> **Very large scores MUST be handled, and are expected to be a MORE COMMON use than our corpora.** A
> Wagner act or a symphony has to produce an analysis; the user expects such music to be a more common

**In plain words.** A Wagner act or a symphony must work. The user expects such scores to be a more common use than the chorales the system was fitted on. This is a standing requirement every later design is judged against, not a defect report.

**Why.** Stated constraint, OPEN_ITEMS.md:157: the requirement is recorded together with the collision it creates - the joint estimator's ratified tractability envelope is chorale size (60-150 events), and the fitted corpus is 326 Bach chorales by one composer.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `ARCHITECTURE.md:1180-1181`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:157 (OI-209) with open_items/OI-209.md, which tracks the requirement rather than housing it. Consumed by the analysis-extent question (OI-210), the corpus onboarding (OI-38), and the architecture step-back (OI-200). The measured collision is OI-215/OI-227 - the decode returns nothing on 13 of 23 committed large scores. OPEN_ITEMS OI-240 closes on this move

### D-202 — The effort control is one setting with several dials, and it must bound the time taken

> **The effort control is ONE setting with several dials behind it, and among the quantities it must
> bound is the TIME the analysis takes. DEFERRED.** How hard the analysis works is a single user-facing

**In plain words.** How hard the analysis works is a single setting the user turns, not several. Behind it sit several dials, and among the things it must be able to bound is how long the analysis takes. It is too early to build: which pieces of the analysis have to be switchable is not yet known.

**Why.** Stated constraint, OPEN_ITEMS.md:157: it is too early to implement until we know FACTUALLY which pieces must be switchable - which is a measurement, and the measurement is what the analysis-cost dispatch was for. The user's recorded prediction beside it: 'always read the entire score will VERY likely not survive (maybe only under some effort setting = EXTREME)'.

**Status.** DEFERRED · decided 2026-07-28 · ratified by user

**Home.** `ARCHITECTURE.md:1188-1189`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:157 (OI-209). The two standing design rules the effort control must satisfy are older and are stated in ARCHITECTURE.md §2.14 (D-035). OPEN_ITEMS OI-240 closes on this move

### D-203 — Candidate admission is completion, not refinement - so #8 permits fixing it now

> **CANDIDATE ADMISSION IS COMPLETION, NOT REFINEMENT — so #8 permits fixing it now (user-ruled
> 2026-07-28, at the OI-199 pass-2 session).** The rule that decides which chord classes the joint
> decoder will even consider is a piece that was never finished, not a refinement of something already

**In plain words.** The rule that decides which chords the decoder will even consider is not a refinement of something already built - it is a piece that was never finished. So the principle that forbids chasing visible analysis errors before the structure is complete does not block fixing it.

**Why.** Stated constraint, cowork_handoff.md:31-32: the design happens ONCE over the whole family, never per symptom (#6/#7) - which is why the fix is deferred until the family is enumerated even though #8 permits it. The measured family: OI-215 (the sparse member-overlap gate), OI-227 (the dense fit gate), OI-226 (admission has no ratified basis), OI-228 (the emission reads struck rather than sounding notes).

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md:1337-1339`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at cowork_handoff.md, the user's ruling at the OI-199 pass-2 session, 2026-07-28. Homed beside #8 in CLAUDE.md because it is a ruling about what #8 permits; what the admission rule IS, and that it has no specified form, is in the estimator's own specification (D-098) and at OPEN_ITEMS OI-226. Cross-read with STATUS.md's earlier note that the classification 'is the user's to settle' - this row records that it was settled. OPEN_ITEMS OI-240 closes on this move

### D-204 — One fix is designed once over the whole enumerated family, never per symptom

> **ONE FIX IS DESIGNED ONCE OVER THE WHOLE ENUMERATED FAMILY, NEVER PER SYMPTOM (user-ruled
> 2026-07-28, at the OI-199 pass-2 session).** When several observed faults turn out to share a cause,
> the remedy is designed once for all of them together, at the layer that owns the cause; fixing

**In plain words.** When several observed faults turn out to share a cause, the remedy is designed once for all of them together. Fixing whichever one is currently visible, on its own, is the error the one-path-per-concern and layer principles exist to prevent.

**Why.** Stated constraint, cowork_handoff.md:28-29 and #3: the fix is deferred BY DESIGN until the whole family is known, because designing over part of a family is the patch-per-symptom error. The instance that produced the rule: the empty-decode cliff turned out to have a sibling at the opposite end of the density spectrum (OI-227) and an emission-side twin (OI-228), neither visible from the first symptom.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `CLAUDE.md:1348-1350`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at cowork_handoff.md, recorded at the OI-199 pass-2 session, 2026-07-28. OPEN_ITEMS OI-240 closes on this move

### D-205 — A human acts as ground truth where no formal ground truth exists

> **A HUMAN acts as ground truth where no formal ground truth exists (user-decided 2026-07-13).** For
> repertoire nobody has published an analysis of, the reference answer is a person's judgment. That person
> may reach it by any method they choose, **including** letting an automated triage judge point them at the

**In plain words.** For music nobody has published an analysis of, the reference answer is a person's judgment. They may reach it however they like, including by letting an automated judge point them at the passages most likely to be wrong. That judge is guidance for the human, never a grader and never a number we report.

**Why.** Stated constraint, open_items/OI-56.md:7: a language-model judge is not ground truth (#9, and the standing rule that music21 corroborates but does not adjudicate), so it could never grade us - at most it can triage, by pointing a human at the scores most likely wrong.

**Status.** LIVE · decided 2026-07-13 · ratified by user

**Home.** `ARCHITECTURE.md:7641-7643`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at open_items/OI-56.md:7, decided by the user 2026-07-13. The when-question is tied to the corpus-onboarding event (OI-38) and the timing is itself open. OPEN_ITEMS OI-240 closes on this move

### D-206 — Intonation is held as a future feature, and is a declared future consumer of the analysis

> **Status of this whole section — HELD, and a declared future CONSUMER of the analysis (user-decided
> 2026-07-13).** Intonation **is** a future feature: the six unbuilt items specified in §11.3a–g, together
> with the tie limitation recorded there, stay on the books as a deliberate long-horizon hold, revisited at a

**In plain words.** The six unbuilt pieces of the tuning design stay on the books as a deliberate long-horizon hold, revisited at a natural pause in the analysis work. The reason the hold is strategic rather than neglect: tuning will read the analysis - knowing the mode, the chord, its function and the progression is what lets a just-intonation decision be made, particularly the decision about staying in tune over time versus letting the pitch drift.

**Why.** Stated constraint, open_items/OI-62.md:7: intonation is a named future CONSUMER of the published analysis surfaces - a concrete instance of the rule that evidence is published broadly so a future design can recognize facts it would never have thought to ask for (D-100's 2026-07-12 amendment).

**Status.** DEFERRED · decided 2026-07-13 · ratified by user

**Home.** `ARCHITECTURE.md:5938-5940`

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

### D-586 — "Function" in the machine-learning literature names the Roman-numeral components, not Riemann's function theory — and this project's own function layer is misnamed for the same confusion

> - **"Function" in the machine-learning literature names the ROMAN-NUMERAL COMPONENTS, not Riemann's
>   function theory — and this project's own component named after this layer does neither (D-586).**
>   When published research says a system predicts "function" it means the Roman numeral's parts (the
>   degree, the quality, the applied relation), not the three-role tonic/subdominant/dominant scheme;
>   the two senses are routinely confused, and the legacy component carrying the name compares
>   candidate chords instead. *Why:* established by survey — every published autonomous Roman-numeral
>   system the catalog names represents and evaluates the analysis as the Roman-numeral component
>   tuple and none emits a three-role head, one of them listing the three-role labels explicitly as
>   unimplemented future work; where the three-role labels exist at all they are a deterministic lookup
>   from the Roman numeral. This is why the layer's output is specified above as the Roman numeral (the
>   precise superset of a T/S/D summary) rather than as a function label.

**In plain words.** When published research says a system predicts "function", it means the Roman numeral's parts — the degree, the quality, the applied relation — and not the three-role tonic/subdominant/dominant scheme of German function theory. The two senses are routinely confused. This project's own component named after the function layer does neither: it compares candidate chords.

**Why.** Established by survey: every published autonomous Roman-numeral system the catalog names represents and evaluates the analysis as the Roman-numeral component tuple and none emits a three-role head, and one of them explicitly lists the three-role labels as future work it did not implement. The three-role labels, where they exist at all, are a deterministic lookup from the Roman numeral.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1970-1980`

**Provenance.** ★ RE-HOMED 2026-08-04 (CC, dispatch `cc_instruction_finish_line_item1.md`, Task 3.3, ruling R3): written into the OWNING LAYER SPECIFICATION in that section's own voice, with its defense. Register rule (e) prefers this route in terms, and D-231's purposive clause (criterion C4) is why it is preferred over a delegation: at completion the specifications must suffice to measure conformance against WITHOUT consulting the register, and a decision reachable only by following a pointer satisfies C1's letter and defeats C4. The classification that selected this entry, with its reason and the whole 94-entry population, is `tools/audit/decisions/finish_line_item1_routes.json`. Its former home class was `gap` — a decision governing a layer but not findable from that layer's section — which is precisely what the re-homing discharges; the field is cleared because a layer-specification home is not a non-specification home. **THE FORMER HOME, CLASS AND VERBATIM, PRESERVED (#12)** — former home `cowork_layer5_function_methods.md:16-20`; former verbatim: “friend: it means the generalized RN components, **not Riemann's *Funktionstheorie***. T/S/D, where it exists (music21's
`analysis.harmonicFunction`), is a **deterministic lookup from the RN**, not a prediction. This matches our own world
exactly: our ground truth (DCML/music21) and our output (`formatRomanNumeral`) already treat "function" as the RN
itself (scale-degree + quality + applied/secondary), and our `harmonicfunctionlayer` is **misnamed** — it does chord-
identity competition, with cadence + functional labeling marked "E4 (planned)" = L5.” — `cowork_layer5_function_methods.md`, the research-first methods catalog that grounds the Layer-5 specification (2026-06-26). Read in full by READ WAVE 5, 2026-08-04. This is the vocabulary finding behind **D-335** (the function layer outputs the Roman numeral; the three-role summary is a derived read-out). It is entered separately because it carries a second thing D-335 does not: a NAMING defect in this repository's own code, which the catalog's §9 lists as a structural step to schedule. The record states no ratifier for the naming half. The rename is unscheduled at HEAD and this entry does not schedule it; it also sits against `CLAUDE.md`'s reserved-word convention, under which a collision already in the tree is not renamed unilaterally.

### D-610 — The value-type relocation is ZERO-CHURN by construction: the leaf spans both namespaces and the un-nested type keeps a member alias, so no call site changes and the move is byte-identical

> - **Holds the closure, EACH IN ITS EXISTING NAMESPACE** (so every qualified name — `analysis::KeySigMode`,
>   `function::ScoringPhase`, … — is *unchanged* → zero call-site churn):

**In plain words.** When the shared value types were moved into their own dependency-free file, none of them was renamed or moved to a different namespace — the new file deliberately spans both namespaces so that every name spelled anywhere in the code still resolves. The one type that was lifted out of a class keeps an alias in its old place. So the move touches no call site and cannot change behaviour.

**Why.** The constraint that forced it is the gate the refactor was held to: a pure relocation must be byte-identical, and the only way to move a type without touching its users is to leave its qualified name unchanged. The document states the cost this accepts — a value-types leaf spanning two namespaces — and accepts it explicitly as required to keep the names unchanged.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_types_header_design.md:16-17`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“The leaf header”** — `## The leaf header` (heading at line 13). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_types_header_design.md`, BUILT / AS-BUILT 2026-06-26. Read in full by READ WAVE 5, 2026-08-04. **D-078** already carries the decision that the cross-layer value types live in a dependency-free leaf header; this carries the separate rule about HOW they got there, which is what made the move byte-identical. The document's two ratification items — relocate only the parameter-bound types and defer the rest, and give the un-nested type a member alias rather than renaming its forty-odd uses — are both instances of it. The record states no ratifier.

### D-639 — Phase 1's doc-sync half reaches a document's account of ITSELF only where that account changes how its analysis content is read — with three worked examples that are the test, and a fallback ruled with it

>   **★ HOW FAR THE DOC-SYNC HALF REACHES INTO A DOCUMENT'S ACCOUNT OF ITSELF (user-ruled 2026-08-04;
>   D-639).** The sentence above says *"states something false at HEAD"*, and a document states things
>   about ITSELF as well as about the analysis — a status banner, an as-built marker, a code anchor, a
>   missing supersession note. **The doc-sync half reaches a document's account of itself ONLY WHERE
>   THAT ACCOUNT CHANGES HOW THE DOCUMENT'S ANALYSIS CONTENT IS READ.** The ruling's own three worked
>   examples, which are the test rather than illustrations of it: an **as-built banner over a dormant
>   mechanism — IN**; a **missing supersession note on a superseded plan — IN**; a **stale anchor or a
>   formatting artifact — OUT**. *Why the line falls there:* the clause states its own reason two lines
>   up — *because a specification cannot be the compliance standard while it misdescribes the code* —
>   so what the half exists to catch is a document that would make a reader believe something false
>   about the system; a coordinate that has drifted misleads nobody about the analysis, and D-307
>   already forbids citing code by line number in the first place. **THE FALLBACK, RULED WITH THE TEST
>   AND NOT LEFT TO A LATER SESSION:** if the test needs judgment on the first rows it meets, that is
>   the *"stable enough to be cited"* failure repeating — a criterion that reads as mechanical and
>   resolves case by case — and the fallback is **option (1A): the doc-sync half reaches only the
>   account of the ANALYSIS.** A session that finds itself arguing a case applies the fallback and says
>   so; it does not stretch the test to reach a verdict. *(First application, 2026-08-04, at
>   `OPEN_ITEMS.md` OI-332: three documents, one matching each worked example, decided without reaching
>   the fallback — the enumeration and the per-document reason are generated at
>   `tools/audit/decisions/true_half_reach.json` and no verdict is restated here, #17f, D-431.)*

**In plain words.** D-231's phase-1 rule says the specifications must be corrected wherever they state something false at HEAD. Documents also state things about themselves — a status banner, an as-built marker, a code line number, a missing note that a plan was superseded — and the user ruled how far that obligation reaches into those: only where the document's account of itself changes how a reader reads its analysis content. Three worked examples settle it rather than illustrate it: an as-built banner over a mechanism that is dormant is IN; a superseded plan with no note saying so is IN; a code anchor that has drifted, or a formatting artifact, is OUT. And if a session finds the test needs argument on the first cases it meets, it falls back to the narrow reading — the obligation covers only what a document says about the analysis — and says that it did so.

**Why.** Stated with the ruling, and it is the clause's own reason two lines above it: the doc-sync half exists 'because a specification cannot be the compliance standard while it misdescribes the code', so what it catches is a document that would make a reader believe something false about the system. A drifted coordinate misleads nobody about the analysis, and D-307 already forbids citing code by line number. The FALLBACK carries its own reason: a criterion that reads as mechanical and then resolves case by case is the 'stable enough to be cited' failure, which the record has already had to retire once, so the answer for that case is ruled in advance rather than left to the session that meets it. First application at `OPEN_ITEMS.md` OI-332 — three documents, one matching each worked example, decided without reaching the fallback; the per-document reasoning is generated at `tools/audit/decisions/true_half_reach.json`.

**Status.** LIVE · decided 2026-08-04 · ratified by user

**Home.** `CLAUDE.md:1236-1255`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** User ruling of 2026-08-04, transmitted in the dispatch `cc_instruction_phase1_delegations_and_corrections.md` §0a as R1, which states both the test and its fallback. Homed at the D-231 phase-1 clause in `CLAUDE.md`, which is where the obligation it bounds is defined — the dispatch's own instruction was to record it 'where the TRUE half is defined, so a later row is classifiable without a fresh ruling'. The ruling ALSO moves a gate verdict (OI-332 classes itself apparatus on one half of D-438's line, whose other half makes a correction to a statement about the build state gating); that consequence is REPORTED at `tools/audit/decisions/true_half_reach.json` and rowed at `OPEN_ITEMS.md` OI-336, not applied here, because a non-gating verdict is derived from a cut and never hand-added.

