# Claude Code — Standing Instructions for This Repository

## Guiding principles

The standing decision guides for all work in this repository. Every design, build, and
measurement choice is checked against them; they are the guide for making decisions and
override convenience.

1. **Fact- and theory-based coding only.** Build only on established fact and theory —
   published research, public algorithms, public software. Fact-finding (investigative)
   coding is allowed.
2. **Specific research over general.** Most research so far has been general or on
   already-handled topics; target the specific open question.
3. **An unexpected finding means we have failed #1** (and possibly #2, #4, #6). Surprise
   signals that the fact/theory basis was incomplete — treat it as a failure to diagnose,
   not a curiosity.
4. **Long-term goal: maximum-precision inference.**
5. **Investigate when facts may be scarce.** If we are unsure whether facts are scarce,
   gather more facts.
6. **Total unification — no duplication of any code.** One path per concern.
7. **Adhere to layers.** Enhance a layer only with algorithms/methods that belong to it,
   nothing else. Worst case, this forces a layer redesign rather than a cross-layer patch.
8. **No inference-problem-driven coding until the refactoring, the architectural design and the
   algorithmic completion are done.** Build-it-right comes BEFORE tune-precision, strictly. All
   three must be finished, not the last alone: every method and algorithm implemented in its
   correct layer, the architecture designed, and the refactoring carried out.
   **★ WIDENED HERE 2026-08-04 ON THE USER'S RULING; THIS IS NOW THE RULE'S ONE HOME (#6).** The
   former wording, preserved verbatim (#12), was *"No inference-problem-driven coding until all
   methods and algorithms are implemented in their correct layer."* It was narrower than the
   statement being applied in practice: `cowork_l1l3_stabilization_plan.md` has carried the fuller
   three-clause form — refactoring + architectural design + algorithmic completion — user-ratified
   2026-06-25, and that plan is **D-557**'s home no longer; it now POINTS here and does not restate
   (#6). *Why it was widened rather than left standing beside the fuller statement:* a session
   reading only this file would have applied the narrow width and concluded that refactoring and
   architectural design were not among the things that must finish first — so the governing
   document and the practice disagreed about the size of the gate, which is the one disagreement a
   governing document may not carry.
   **★ THIS PRINCIPLE POINTS AT ITS OPERATIONAL HALF — D-592 AND D-593 (written 2026-08-04 on the
   user's ruling; a POINTER, never a copy, because both are already homed, #6).** The three clauses
   above say WHEN inference work may start. They do not say when a layer counts as FINISHED, and
   they do not say what may still be fixed while the gate holds — so the principle is not readable
   without the two entries that do. **D-592** is the standing bar for what finished means for a
   layer. **D-593** is the line inside the build-it-right firewall: which work is allowed now and
   which is not. Read both at their homes; neither is restated here.
   **★ AND THE ENTRY IS D-172, ONCE (user's ruling, 2026-08-04, `OPEN_ITEMS.md` OI-329).** The
   widening above briefly gave this one principle two live register entries; **D-172** survives as
   its entry and **D-557** is recorded superseded into it, its former home and text preserved (#12).
   The widened three-clause width is not a 2026-08-04 decision — it was **user-ratified 2026-06-25**,
   as the paragraph above records, and had been living in the wrong document until that date.
9. **Test and measure only on corpora known to be non-stale and accurate.**
10. Documentation is kept in sync with code **so that code can always be compared against its
    specification, and so that the specification is as correct and complete as possible — in order
    that the code may be as correct and complete as possible.** That purpose is the test of what is
    worth fixing. **An issue is WORTH FIXING when leaving it unfixed risks either (a) something
    being built that does not serve maximum-precision inference, or (b) code no longer being
    comparable against a correct and complete specification. An issue bearing on neither is
    recorded as DISCARDED — the finding, its date, and the reason — and is not an open obligation:
    no row, no gate, no capacity.** Two carve-outs: **an establishment obligation (#19) is never
    discarded, whatever its subject**; and where the consequence can neither be named nor cheaply
    established, **it is looked at once, cheaply (#5)** — being unable to imagine a consumer is not
    evidence there is none.
    **★ #10 GAINED ITS SECOND HALF HERE, AND THIS IS THE RULE'S ONE HOME (user-ruled 2026-08-11;
    the ruling record is `cowork_rulings_2026_08_11_sixteenth_stop.md`, Ruling 68; register entry
    D-174, whose verbatim is re-taken at the text above).** The ruled text is the user's own and
    stands verbatim. **THE FORMER WORDING, PRESERVED IN PLACE (#12), WAS:** *"Documentation always
    in sync with code."* — five words with no purpose attached. *Why the amendment was made at the
    principle rather than at a process rule beside it (#6):* because nothing in those five words
    said what being in sync is FOR, **every discrepancy read as owed, and a session that rowed a
    stale banner was obeying the principle exactly as written** — so the unbounded documentation
    stream is #10 working as written, and a remedy anywhere else would leave the principle still
    demanding it. *The user's own statement of the objective, recorded verbatim because it is the
    ground of the rule:* **"The objective is NOT to create to ultimate documentation. The objective
    with fixing documentation is to make sure we always can compare code with specification, and
    that the spec should always be as correct and complete as possible - in order to facilitate the
    code to be as complete and correct as possible."**
    **★ WHAT IT SUPERSEDES — A POINTER, NEVER A COPY (#6).** R3's clause that an apparatus
    finding's row is **mandatory** no longer holds for a finding the worth test above discards.
    **R3 is otherwise untouched** — it still decides whether a finding is surfaced or rowed, and
    its own #19 sentence is reinforced rather than weakened. R3's home is `cowork_audit_protocol.md`
    (register entry **D-641**), where the supersession is recorded at the clause itself and is not
    restated here.
    **★ THE THREE ALTERNATIVES DECLINED, recorded because an excluded alternative is evidence about
    the choice.** *Keeping rows for the discarded class* was declined as achieving nothing **D-676**
    had not already achieved — every row of the batch that prompted this would still exist.
    *Placing the test at R3 instead of here* was declined on #6: the test would live at the process
    rule while the purpose it serves lived nowhere, so a session reading the principle would still
    meet an unbounded demand — the same disagreement between a governing document and practice that
    forced #8's widening. *Doing nothing and letting **D-675** and **D-676** drain* was declined
    because it changes the backlog and not the rate.
    **★ THE COSTS THE USER ACCEPTED, stated before the ruling and recorded because an accepted cost
    is not a discharged one.** **#12 is weakened:** a discarded finding is harder to retrieve than a
    row, and the finding-by-exclusion clause holds that negative evidence is information — mitigated,
    not erased, by the discard record carrying the finding and its reason. And it **amends a standing
    principle**, which is the heaviest change available.
    **★ WHAT IT DOES NOT DO.** It authorizes no fix, no design and no inference change. It moves
    neither **D-231**'s phases nor #8's three-clause gate. It touches no measured value, no golden,
    no corpus of scores and nothing under `tools/robust_stop/`. And **it does not retroactively
    discard the open population** — it states the test; what the test does to rows already on the
    books is a separate act.
11. **Regression test cases always in sync with code; regression-test between iterations.**
12. **No information loss.** Negative/exclusion evidence is information ("finding by exclusion") —
    carry a ruled-out possibility at low confidence rather than dropping it, unless the exclusion is
    recomputable from what is kept.
    **★ THE RECOMPUTABLE CLAUSE ABOVE REACHES EVERY COLLAPSE, NOT ONLY AN EXCLUSION (2026-07-06;
    the record states no ratifier).** The *unless* is written for exclusion evidence; it holds for
    **any** collapse of several values into one. A collapse is a loss only when the several cannot
    be got back: where the collapsed value is derived deterministically from something still
    carried, or is regenerable from it, nothing has gone and the collapse is not a defect. *Why
    this is stated rather than left to the reader:* it is the guard against over-flagging, and
    without it a sweep conducted under this principle reports every summary as a fault, which is
    the opposite of what the principle is for. It was established on two cases of exactly that
    shape — a confidence squashed through a fixed function whose input is carried, and a boolean
    that is exactly a comparison of a carried number against a threshold.
13. **Surface a surprise as a STOP before building around it** (the operational form of #3).
14. **Every behavior change is user-ratified as one revertible, provenance-stamped commit.**
15. **Verify at objects/data on the full output surface, never at assertion** (winner *and*
    carry, not the winner alone).
16. **Reproducibility.** Every measurement is stamped to corpus-hash + instrument-commit;
    snapshot the outgoing reference before any re-baseline.
17. **The Premise Gate.** Before any inference-affecting design is built or probed:
    (a) a **premise ledger** — every load-bearing causal claim explicitly labeled **FACT**
    (citation to code/measurement), **THEORY** (citation to published research answering the
    *specific* question, #2), or **ASSUMPTION**; (b) a **written quantitative prediction per
    assumption** (fire-rate, magnitude, direction, population) recorded *before* measuring —
    no prediction, no build; (c) a **desk simulation** — trace the mechanism by hand through
    the intended architecture on 3–5 real corpus cases drawn from the known failing sets,
    answering FIRST "does the mechanism FIRE on this case?" (control flow — ratified sharpening
    2026-07-10, the EG-2 desk-sim lesson), THEN "which term moves, by how much?" (arithmetic);
    (d) every **proxy→target
    link is itself a ledger premise** (a structural proxy never stands in for a behavioral
    quantity unvalidated); (e) every **insulation claim** ("X cannot affect Y") must enumerate
    the false-negative path explicitly; (f) **no hand-transcribed measurement numbers** —
    figures enter docs only via generated artifacts (the `manifest.json` pattern).
    **★ WHAT A DESK SIMULATION'S TABLE VALUES ARE, AND WHAT THEY MAY NEVER BECOME (user-ratified
    2026-07-19).** Every table value a desk simulation under (c) uses is **PROVISIONAL** — declared
    before use, each labeled with its provenance class, and hand-declared stand-ins whose only job
    is to let the mechanism be traced. **No value declared that way survives into any fit**;
    fitting happens only under the fit gates, which are a separate act. And a verdict that would
    flip within the plausible range of a provisional value is reported as a **NEAR-TIE with the
    sensitive cell named**, never as a win. *Why:* visible in the traces the rule governs — several
    verdicts are reported with their sensitive cells named rather than as wins, and those cells are
    carried forward to the capacity and pooling gate. Without the rule a hand-declared number
    silently becomes a measurement tool, which is the defect the catalog names DT-2.
    **★ EVERY DESK-SIMULATION TRACE RUNS AT IDENTITY WEIGHTS (user-ratified 2026-07-19).** A trace
    under (c) runs the generative product with every weight at one — exactly the mandatory ablation
    baseline the design already carries. The desk simulation therefore tests the structure and the
    tables, not the weight layer. *Why:* identity weights ARE that ablation baseline, so the choice
    imports no new premise, and running at anything else would confound a structural verdict with a
    weighting one.
18. **Unverified causal premises are FORBIDDEN (Class A).** No design may carry load on a
    causal claim about our own system or data that is checkable but unchecked.
19. **Unestablished instruments are FORBIDDEN (Class B).** An instrument, corpus, gate, or
    recorded figure is trusted only after being *positively established* (oracle cross-check,
    derivation of what the measurement unit actually measures, reproduce-check) — never
    because it is merely unfalsified.
20. **Fit/evaluation separation.** No value is graded on data that helped fit it. Every fit
    event declares its held-out data (split or k-fold) and its capacity budget (parameter
    count, regularization, justified against corpus size) BEFORE fitting; the headline claim
    is the held-out figure. A fitted-and-self-measured number is not established (#19).
21. **Ground truth is an instrument too.** The accuracy of ground truth is itself a measured
    quantity — per-axis annotator agreement, not an assumed binary (sharpens #9's "accurate").
    Every precision target and every "irreducible residual" verdict is interpreted against
    that measured ceiling; without it, structural error and annotator disagreement are
    indistinguishable in the residual.
    **★ THE CEILING CANNOT BE CITED FROM THE LITERATURE; MEASURING IT HERE IS THE ONLY ROUTE
    (recorded 2026-08-04 on the user's ruling with the read-wave-3 ratification; D-474).** A
    dedicated search established a FACT-of-absence: no published study reports per-axis
    inter-annotator agreement for Roman-numeral or key annotation of Baroque/classical symbolic
    music. TAVERN released duplicate annotations but published no such number; ABC split its pieces
    between annotators with no overlap by design; the Mozart-sonatas corpus is consensus-built, so
    agreement cannot be recovered after the fact; *When in Rome* states in its own words that the
    variance is unmeasured; Dilemmadata (2026) identifies dual-annotated pieces and computes
    nothing. **So a session may not satisfy this principle by citation — there is nothing to cite.**
    The obligation is tracked at `OPEN_ITEMS.md` OI-179, which is therefore not "a measurement not
    yet built" among others but **the only available route to the quantity this principle demands**.
    *Why this belongs at the principle rather than only on that row:* the principle's own sentence
    above is that without the ceiling, structural error and annotator disagreement are
    indistinguishable in the residual — so the absence of a citable number bears on what may be
    claimed about ANY residual, on any axis, not on one open item. The quantified agreement bounds
    that do exist are off-domain (rock symbolic-by-ear; pop audio) and are recorded with D-474; they
    are **not** a ceiling for this repertoire and may not be used as one, however convenient the
    invariant they share.
    **★ AND THE MEASUREMENT IS NOW COMMISSIONED, IN TWO HALVES, WITH THE RULE THAT ENDS THE CONTACT
    ROUTE (user-ruled 2026-08-09; the ruling record is `cowork_rulings_2026_08_09_return.md`,
    Ruling 10).** The block above establishes that this principle cannot be satisfied by citation.
    What follows is the route to satisfying it, and both halves are recorded here because each
    settles something a later session would otherwise re-decide. **(a) THE LABORATORY CONTACT IS THE
    USER'S ACT** — the one act no session can perform, and the longest lead — **and it is
    PERFORMED**: a public issue on the annotating laboratory's own repository, asking annotator count
    and background, the validation and review procedure, any unpublished duplicate or superseded
    readings, and errata. **A reply is recorded on the tracking row when it arrives; SILENCE AFTER A
    REASONABLE WAIT IS RECORDED AS THE ROUTE EXHAUSTED**, which makes the declared status of what the
    published record holds FINAL rather than provisional — #19 closed by exhaustion rather than left
    open forever. *Why the exhaustion clause is part of the commissioning:* without it a contact
    route never ends, and an obligation that cannot end is one that never closes, so the absence of a
    reply would go on reading as work outstanding rather than as an answer. **(b) THE CEILING
    MEASUREMENT ITSELF IS COMMISSIONED AND OPENS WITH PHASE 2, DESK SIMULATION FIRST (#17c).** No
    measurement tool is built before phase 2 opens: the standing scope rule is that an addition to
    the phase-1 finish line is a user ruling, and this is that ruling for this addition — it
    commissions the measurement and it does not pull the work forward. *Why the commissioning is
    recorded at the principle rather than only on the row:* the principle DEMANDS a quantity the
    literature does not hold, so a reader meeting the demand must also meet the route to it and the
    condition under which that route is finished.
22. **Every hard gate carries a pre-declared protocol for the largest change it will face.**
    A gate written only for incremental change must not be amended under the pressure of a
    live diff — the exceptional-event variant (e.g. architecture-scale adoption: aggregate
    criterion + explained diff + snapshot + ratification) is written and ratified before such
    a change is on the table.
23. **End-state principles need lawful transitions.** When a planned change must temporarily
    violate an end-state principle (e.g. #6, one path per concern, during a parallel build),
    the violation is declared, bounded, and pre-ratified with a retirement map — migration is
    a first-class state, never an undeclared exception.
24. **Every reported figure carries its uncertainty.** Sampling noise on the measurement
    corpus is quantified; a difference within the uncertainty is not a finding, and no
    decision rests on one. (The companion of #16: reproducibility bounds instrument error,
    this bounds sampling error.)

*Ledger corollary to #17 (ratified with #20–#24):* when a decision selects a **constrained
optimum** (a design chosen for methodology-compliance rather than raw measured performance),
the ledger records what the unconstrained best known alternative is and why it is excluded —
so a future reader can re-test whether the constraint still binds.

*Scope of surprise (ratified with #17–19):* surprises are **allowed in explorational runs**
whose purpose is to eliminate ignorance (#5 fact-finding); they are **NOT allowed when building
actual inference code** — there, a surprise is a STOP (#13) and evidence the Premise Gate was
not satisfied. The stage funnel: **desk-simulate (hours) → read-only probe (a session) → build
(an arc)** — each stage kills bad premises before the next pays for them.

*Fact-publication corollary to #6/#7/#12 (ratified by the user, 2026-07-10):* every derived
analytical fact is **published exactly once, on the producing layer's output surface;
consumers read, never re-derive.** A fact consumed by no one is either **declared dormancy**
(its future consumer named) or **waste** (removed). Evidence for why this needs stating:
`cowork_siloed_facts_audit.md` (17 findings) + `cowork_adjudication_dossier.md` Part B.
*Amendment (user, 2026-07-12, at the evidence-inventory discussion):* for EVIDENCE-class
facts (hints/clues a layer discovers that downstream inference could conceivably use —
the `cowork_evidence_inventory.md` catalog), **publish broadly even without a named
consumer** — the user's rationale: a visible smörgåsbord of evidence lets a future design
RECOGNIZE useful facts it would never have thought to request. Guardrails: each published
evidence fact carries its **establishment status** on the surface (established vs
unvalidated — a consumer may not put an unvalidated fact under load, #19); publication is
the in-memory surface (serialization stays selective); and the inventory + the
`ARCHITECTURE.md` layer specifications are kept in sync as facts are adopted (OI-146).

*Decision-neutrality of the existing implementation (corollary to #4/#6/#19; user-ratified
2026-07-26):* Designs are chosen from the principles and the ultimate objective — enabling the
best possible inference — alone. In that choice: **(a)** the value of reusing existing code, and
the cost of making existing code obsolete, are SECONDARY — they may break ties between designs
equal under the principles and the objective, and reuse counts only as carried-forward
establishment (#19), never as sunk cost or saved effort; **(b)** downstream implementation
impact — whether and how many consumers must change — carries NO weight; **(c)**
end-user-visible behavior change carries NO weight (the 2026-07-26 unshipped-scoping ruling),
while every behavior change remains ratification-gated (#14) and verification-gated (#15/#19)
exactly as before. The best-possible-inference design is chosen first; what exists then either
serves it or retires. (This does not weaken #6 — one path per concern is an END-STATE structural
principle, not a preservation claim for the existing path; nor #19 — establishment must still
exist before trust.)

*Theory-grounding corollary to #1/#2 (2026-07-19; the record states no ratifier):* where published
research is used to justify a design, **every load-bearing claim is labeled FACT** (stated or
measured in a paper actually fetched and read), **THEORY** (established published theory), or
**CONJECTURE**. The central sources are extracted **independently by two or three passes each and
cross-checked** for agreement, and **a source that could not be fetched is flagged with no equation
carried out of it** — the gap is stated instead of filled. *Why:* it follows from #1 itself. A
citation to a paper nobody read is not a fact basis, and an equation reconstructed from a snippet is
an assumption wearing a citation. This SHARPENS #17(a) rather than restating it: #17(a) requires the
FACT / THEORY / ASSUMPTION labels on a design's own premises; the unfetched-source rule and the
independent cross-extraction are what this adds, and they bind on the reading of the literature
rather than on the ledger.

*Provenance: principles 1–11 are the user's standing list; #12 (no information loss) and
#13–16 were ratified by the user on 2026-07-06; #17–19 (the Premise Gate + the Class-A/Class-B
prohibitions) and the surprise-scope rule were ratified by the user on 2026-07-10 — analysis
and evidence in `cowork_premise_gate_reflection.md`; #20–#24 (evaluation statistics, the
ground-truth ceiling, gate/transition governance) and the constrained-optimum ledger corollary
were ratified by the user on 2026-07-18 at the joint-estimator plan review — analysis in
`cowork_joint_estimator_architecture.md` §6/§7, operational rows OI-176…OI-181; the
decision-neutrality corollary was ratified by the user on 2026-07-26 at the notation-layer
adoption increment's decision surface — analysis in `cowork_notation_adoption_increment.md` §2. Companion standing rules elsewhere: the
⛔ TOTAL UNIFICATION rule (`cowork_handoff.md`), the MEASURE-BEFORE-BUILD gate
(`cowork_engage_arc_plan.md`, now the middle stage of the #17 funnel), and the doc-sync,
layer, and gate policies below.*

**Delegation pointer (the fifth home case; written 2026-08-03 on the user's direction, the OI-293
write list).** The ratified contract for the ORDER OF WORK from here to the precision phase — the
arc sequence, the MEASURE-BEFORE-BUILD gate, and the Stage-4 rules — is `cowork_engage_arc_plan.md`
(RATIFIED by the user, 2026-07-07) — D-278, D-279, D-311 — which this file points at and does not
restate. *(The naming in the paragraph above is a citation inside a list, which rule (i) does not
admit as a delegation; and rule (j) records that a document being a SOURCE of delegations does not
make it a delegation TARGET. This paragraph is what makes it one.)*

## The open-items register (user-directed, 2026-07-10; split into index + detail files, user-ratified 2026-07-26)

**The register is `OPEN_ITEMS.md` (the lean INDEX) + `open_items/OI-<n>.md` (one detail file per
item).** The INDEX `OPEN_ITEMS.md` is the ONE home for every discovered-but-unresolved issue and the
**authoritative status surface** (#6 applied to tracking itself — created after a full-repo sweep
found 91 open items scattered across 12 surfaces with 11 status contradictions; split into
index + per-item detail files on 2026-07-26, user-ratified option 1, when the single file grew too
large to render). Each item's full original row (text + source + status) lives verbatim in its
detail file `open_items/OI-<n>.md`, which carries narrative and provenance only and **never a status
of record**. Rules: (a) **read the INDEX `OPEN_ITEMS.md` at session start** (open detail files as
needed); (b) **a stage may not open while a register item gating it is open**; (c) every newly
discovered issue gets an **index row AND its detail file** **in the same commit** that records the
discovery; (d) every resolution **flips the INDEX row** with provenance (the detail file gains a
dated resolution note, never a status of its own); (e) tracking an owed/deferred/TODO item in
prose only, without a register row, is a doc-sync violation (#10). "Deal with everything
discovered" means: every item has ONE index row, an owning layer, and a blocking gate — fixed at its
#8-correct stage, never silently forgotten. (The byte-level split reconciliation instrument is
`tools/open_items_split_check.py` → `open_items/split_reconciliation.json`.)

**★ QUALIFICATION OF RULE (b) — THE APPARATUS ROWS ARE DECLARED NON-GATING (user-ruled
2026-08-03).** Rule (b) says a stage may not open while a register item gating it is open; it does
not say every open row gates. **A row whose subject is this project's own tracking and
documentation apparatus gates nothing** — it stays open, it stays owed, and it is worked in
leftover capacity. **The test, so a future row is classifiable without a fresh ruling: does the
row's subject bear on the analysis, its inputs, or an instrument a measurement depends on? IF YES
IT GATES.** The line inside the documentation rows, stated once so the test is mechanical rather
than a matter of taste: **what is owed decides it** — a pointer, an anchor, a label, a banner, a
filing decision or a section boundary is apparatus; a correction to a statement about the analysis
or its build state, or the completion of a specification, GATES, because the phase-1 rule in
Conventions makes specifications COMPLETE and TRUE the thing that precedes everything else. **A row
that is not apparatus, or whose subject its own text does not settle, GATES** — the declaration
only ever removes a wait where the row supports removing it. **★ AN ESTABLISHMENT OBLIGATION (#19)
ALWAYS GATES, WHATEVER ITS SUBJECT** — including one whose subject is the open-items register
itself. *Why that clause is not discretionary:* backgrounding an establishment obligation is how it
never happens, and #19 exists because a thing merely unfalsified is not established. *Why the
qualification at all:* the open-items register is this project's own record-keeping, and a rule that
lets its housekeeping block the work it exists to track inverts what it was created for; the cost of
the error in the other direction is bounded by the default above. The derived set is generated, never
hand-listed — `tools/audit/nongating_apparatus_rows.json` from
`tools/audit/gen_nongating_apparatus_rows.py`, which parses the INDEX itself and stops if any
candidate row lacks a verdict or any verdict names a row the INDEX no longer carries open; no
row identity or count is restated here (#17f, D-431).

**★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH A PER-ROW LAPSE RECORD (user-ruled
2026-08-11; the ruling record is `cowork_rulings_2026_08_11_fifteenth_stop.md`, Ruling 66).** The
declaration above says an apparatus row gates nothing, and then says three things about what such a
row IS: *it stays open, it stays owed, and it is worked in leftover capacity.* **THE SECOND AND
THIRD ARE SUPERSEDED HERE. An apparatus row STAYS OPEN in the open-items register, STOPS GATING ANY
STAGE, and STOPS BEING OWED — it no longer draws leftover capacity.** The first clause is untouched, and so is the
row's status cell: a lapse is not a resolution. **EACH LAPSE IS RECORDED PER ROW, NAMING THE
DERIVATION THAT GRADED IT**, so a later reader sees why the row stopped being owed and can re-open
it by challenging a recorded derivation rather than by rediscovering the issue; **a row with no
named grading DOES NOT LAPSE.** **THE #19 CLAUSE ABOVE IS UNTOUCHED AND IS WHAT BOUNDS THIS ONE:**
an establishment obligation always gates whatever its subject, so it never lapses. *(The former
wording stands in place above (#12) — "it stays open, it stays owed, and it is worked in leftover
capacity" — and was the rule until this date.)* *Why:* stated with the ruling — the apparatus is now
large enough to generate its own defect stream indefinitely, and *stays owed, worked in leftover
capacity* is precisely the mechanism **D-641**'s own recorded ground names as the cause of the
backlog it describes (`OPEN_ITEMS.md` OI-337; no figure is restated here, #17f, **D-431**), so the
alternative reading — the row unblocked but still owed — was declined as changing almost nothing.
**THE COSTS THE USER
ACCEPTED, recorded because an accepted cost is not a discharged one:** a residual #19 exposure,
mitigated only as well as the cut encodes the carve-out; a motion against #5, since this decides to
stop investigating a population; and practical irreversibility, which the per-row lapse record is
what softens. **RESOLVING THE ROWS OUTRIGHT WAS NOT AVAILABLE AND THE EXCLUSION IS RECORDED:** rule
(d) flips a row with provenance and there is none, because nothing was done; #19 forbids converting
*merely unfalsified* into *established*; #10 forbids the record stating something false about
itself; and three separate derivations read this INDEX's status token, so a false resolution
propagates mechanically. **NO NEW CANONICAL STATUS TOKEN IS CREATED, AND THAT WAS ESTABLISHED
RATHER THAN ASSUMED:** rule (f) below carries a row's OPEN-or-RESOLVED bit and nothing else — its
vocabulary maps every canonical opening to exactly those two values — and a lapsed row is still
OPEN, so *owed* is a DERIVED field of the same cut that already derives gating, and a token would
put one state in two places (#6). The lapse population and every lapse record are derived, never
hand-listed; no row identity or count is restated here (#17f, D-431).

**★ RULE (f) — EVERY INDEX STATUS CELL BEGINS WITH ONE CANONICAL TOKEN (user-ruled 2026-08-09; the
ruling record is `cowork_rulings_2026_08_09_fifth_stop.md`, Ruling 33).** Rules (a)–(e) above say
how the register is kept. This is the sixth, and it is about the one cell three separate derivations
read. **A row's STATE is carried by the first token of its status cell — the resolved mark at the
head of the cell, or one of the open-state words — and by nothing else.** Two consequences follow
immediately and both are the point of the rule: a cell may **name any other row's resolution
freely**, in words or with the mark, because a mention anywhere after the opening is inert; and a
resolution spelled **only in prose**, with no canonical opening, **is not a state** and will be
counted open until the opening is written.

**The two STOPs that make it a mechanism rather than a convention.** A **lint** reports every
non-canonical opening, and **the ONE index parser** — the single reader every derivation over this
INDEX imports (#6) — **STOPS on a row that does not split into six cells** instead of skipping it.
The vocabulary, the row split and the leading-token test have exactly one home,
`tools/audit/index_status_lint.py`; the vocabulary is **DERIVED from the openings the INDEX
actually uses** rather than invented, and no token or count is restated here (#17f, D-431).

*Why the rule is worth a lettered place beside the others.* It is one cause with three faces, and
each face was found separately: a cell that mentioned another row's mark made its OWN row read
resolved to every derivation; a cell stating its resolution in words read OPEN although its text
said otherwise; and a malformed row was **dropped silently — in no population at all**, which is
worse than either mis-reading, because a mis-read row is at least counted somewhere and a moving
count can be noticed. The silent drop is why the parser STOPs rather than skips (#12, #19). *The
two excluded alternatives are recorded at the ruling:* recognising a resolution token anywhere in a
bounded opening — a hand-picked threshold over varying prose, which fixes neither sibling — and
forbidding the mark in prose, which is one symptom of three. **`OPEN_ITEMS.md`'s own preamble
carries a POINTER to this rule and is explicitly not its home** (#6).

## The decisions register (shape user-ratified 2026-07-28; content + living surface 2026-08-02)

**The register is `DECISIONS.md` (the lean INDEX) + `decisions/group_<X>.md` (full entries: the
verbatim decision, plain restatement, why, status, home, provenance).** It records WHAT WAS
DECIDED and its STATUS, nothing else — non-conformance is tracked in `OPEN_ITEMS.md` as ordinary
rows pointing back at the decision violated. Rules: (a) **read the INDEX `DECISIONS.md` at
session start** (open group files as needed); (b) a dispatch, design or report touching a
decision's subject CITES its register entry; (c) **a new ratification, shelving or falsification
gets its register entry (data + regenerated files) IN the commit that records it**; (d) the
register is a GENERATED surface — change `tools/audit/decisions/backbone_decisions.json` and
regenerate (`gen_decisions_register.py`; its `--check` and `gen_cluster_dispositions.py
--verify` guard drift, quote fidelity and reference resolution), never hand-edit the rendered
files; (e) a decision belongs, wherever possible, in the OWNING LAYER'S SPECIFICATION — the
register is the index and pointer, never a substitute home; (f) an entry whose subject is the
LEGACY surface (the dormant pipeline awaiting deletion) is explicitly marked LEGACY — a reader
must never mistake a ruling about soon-deleted code for one about the live solution (user,
2026-08-02); (g) a RATIFIED CONTRACT DOCUMENT the owning `ARCHITECTURE.md` section points to is
a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268 — the pointer, never a
copy, is what a missing delegation owes); the document's ratification is the user's directly OR
TRANSITIVE — a user-ratified surface explicitly delegating to the document carries the user's
authority to it (user, 2026-08-02, at the phase-1i banner/authority review) — an assistant's
stamp alone never confers contract-home status; **(h) THE UNIT OF (g) IS A SECTION, NOT A
DOCUMENT (user, 2026-08-03): a home is a SECTION of a document, admitted when a user-ratified
surface delegates a stated concern to that section BY NAME and that section STATES RULES rather
than recording findings.** The surrounding document's kind and its status banner are not the
test. **GRANULARITY — stated explicitly so it is not re-interpreted (user, 2026-08-03, at the
phase-1q whole-document reading): a delegation naming a DOCUMENT reaches ALL of its sections; a
delegation naming SECTIONS reaches only those; and the rule-stating half is judged PER SECTION in
both cases.** *Why the granularity clause:* the strict reading — that a delegation must name a
section or it admits nothing — would evict every document delegated as a whole, signed layer
specifications among them, on the accident of how a pointer happens to be phrased, and would make (h) retroactively destructive
rather than refining. (h) was ruled to let a SECTION be a home where the surrounding document is
not; it was never ruled to require every delegation to name sections. *Why (h) itself:* measured, at the case that refutes the document-level form — `ARCHITECTURE.md:319`
delegates the shipped-parameter licence-pool constraint to `cowork_score_census.md` **§8c**, a
block that states three binding rules, inside a document whose kind is a census; a test applied
to the document excludes the block along with it. **(h) subsumes the two tests that preceded it
rather than replacing them** — the delegation-specificity criterion (2026-08-03, measured at
`OPEN_ITEMS.md` OI-281) and the document-kind test (2026-08-03, same row) — each of which was a
proxy for it and each of which produced the evidence locating its own error. (g)'s guard is
untouched: the delegation confers, and only the user writes a delegation into `ARCHITECTURE.md`.
Applied **in full 2026-08-03** — first staged to the entries where section granularity decided
something, then, on the user's ruling below, to the whole home population in one pass.
**A SHELVED SECTION CAN BE A HOME — SHELVING IS A STATUS, NOT A KIND (user, 2026-08-03).** A
section whose rules are shelved still STATES rules, and the register records shelvings with their
evidence, so a shelved decision needs a home exactly as a live one does (#12). *Why:* stated with
the ruling — the kind half of (h) asks what a section DOES, and a status banner does not change
that. This also retires the phrase *"stable enough to be cited"* wherever it survives: it is a
clause of the superseded delegation-specificity criterion, and leaving it in the tracking prose
invites a fourth criterion. **(i) WHAT COUNTS AS A DELEGATION, GRADED BY FORM (user, 2026-08-03).**
(h) turns on a user-ratified surface DELEGATING a stated concern to a section; (i) fixes which
wordings do that, and it is the clause (h) deliberately did not touch. **ADMITTED:** an **explicit
delegation clause** — *"The ratified contract for this layer is X"*, *"The ONE detailed cross-layer
spec for this contract is X"*, *"formalised as an independent knowledge-base component with its own
spec (X)"* — or **a named home with sections** — *"Criterion + build home: X §0/§5.3"*. **NOT
ADMITTED:** a **bare appended citation** — *"Full spec: X."* — or a **provenance attribution**,
meaning a naming inside a list of citations, or a parenthetical recording where something was
ratified. *Why:* the canonical document distinguishes the two acts in ADJACENT LINES — one line ends
*"Full spec:"* and names its target on the next, and the delegation clause immediately beneath it
names its target AND the sections it owns. The distinction is `ARCHITECTURE.md`'s own, not a
preference. *(This defense is stated as a DESCRIPTION rather than by line number on the user's ruling
of 2026-08-03. A line number quoted inside a rule's prose is not a register anchor, so the anchor
machinery cannot maintain it and it goes stale on the next insertion above it — as the two numbers
formerly quoted here did, on the very act rule (i) asked for. Both lines are located and quoted from
the file at `tools/audit/decisions/phase1p_delegation_bar.json` → `the_defense`, which is generated
and therefore does not go stale silently. The former wording is preserved in D-432's provenance,
#12.)* **(i) IS APPLIED (user, 2026-08-03, at OI-291):** the
check ordered before applying it — does the bar change the verdict for any document the register
currently classifies `contract-home`? — came back yes, and the user ruled **ONE re-classification
pass over the whole home population**, with a **write list** for the homes the record means to keep,
rather than a forward-only migration or a revision of the bar. The pass is generated, never
hand-classified, and every entry keeps the class it carried before it (#12).
**(j) DELEGATING TO A DOCUMENT AND BEING A HOME ARE DIFFERENT TESTS WITH DIFFERENT SUBJECTS (user,
2026-08-03).** To DELEGATE, a surface must itself be user-ratified; to BE a home, a section must be
delegated to. A document may satisfy one and fail the other, and neither role implies the other. So
`cowork_engage_arc_plan.md` — a user-ratified surface the criterion USES as a source of delegations
— is not a delegation TARGET BY THAT FACT: whether any section of it is a home turns on the separate
question of whether some user-ratified surface delegates a concern to it in a form (i) admits, which
is answered by reading the delegations that exist and never by the document's standing as a source.
*Why:* the question was asked in exactly that form, and the two roles had been running together in
the tracking prose; stating them apart is what keeps (i) a mechanical test rather than one with a
case-by-case exception. *(Corrected on the user's ruling of 2026-08-03. The clause that formerly
closed the sentence asserted in the present tense that no such delegation existed — true when the
ruling was made, and made untrue by the OI-293 write list, which on the user's direction wrote one
into this very file, so a reader arriving here first read a false statement about the file in their
hands. What is struck is the factual claim, not the rule: the arc plan became a home by BEING
DELEGATED TO, which is (j) working rather than an exception to it. The former wording is preserved
in D-435's provenance, #12.)*
**(k) A DELEGATION REACHES ONLY THE MEMBERS IT NAMES EXPLICITLY — AND TWO CONFIRMATIONS THAT CLOSE
THE QUESTIONS ASKED WITH IT (user, 2026-08-04, at `OPEN_ITEMS.md` OI-326).** `ARCHITECTURE.md`'s
doc-governance hierarchy clause — the one naming the per-layer and per-component design documents as
the authoritative detail for their own scope — **IS a delegation under (i), but it delegates only to
the members it names EXPLICITLY. A glob pattern and a trailing ellipsis CONFER NOTHING.** *Why:* a
delegation whose membership is indeterminate could be extended by a session, and extending a
delegation is the authority (g) reserves to the user; a glob is satisfied by any file a later commit
happens to name that way, and an ellipsis by anything at all. **This APPLIES (i)'s logic rather than
amending it — (i) is unchanged, and so is D-432.** Two confirmations, ruled in the same act and
written here so that neither is asked again. **(k1) WHERE A DOCUMENT IS NAMED IN BOTH AN ADMITTING
AND AN EXCLUDED FORM, THE STRONGEST NAMING GOVERNS**; being cited elsewhere in a weaker form does not
undo a delegation. **(k2) (h) REQUIRES BOTH HALVES AND THE KIND HALF IS DECISIVE**: a well-formed
delegation to a section that RECORDS FINDINGS rather than STATES RULES admits nothing, and the halves
are applied in that order — form first, kind second and last. **What (k) leaves out is settled
through the OI-293 WRITE LIST, never by reading the clause more generously:** a delegation the user
writes settles that document without touching the bar. *Measured before it was applied, on the
user's own condition:* how much of the population the split moves was measured first, and the split
moves nothing — the enumeration, the reasoning and every count are generated at
`tools/audit/decisions/reads4_oi326_application.json`, and no figure is restated here (#17f, D-431).
**(l) WHERE NO DELEGATION ADMITS AN ENTRY'S HOME, RE-HOMING IS THE DEFAULT CLOSING ROUTE — AND WHO
MAY EXCEPT A DOCUMENT FROM IT, AND WHEN (user-ruled 2026-08-09; the ruling record is
`cowork_rulings_2026_08_09_sixth_stop.md`, Ruling 38).** Rules (g)–(k) decide which documents and
sections are homes. This is the rule they lack: what closes an entry whose home is a home under
none of them. **For every register entry whose home document is named in NO user-ratified surface,
or only in a form the delegation bar excludes, the closing act is RE-HOMING into the owning layer's
specification** — rule (e)'s own stated preference, made a rule rather than a preference. **AND THE
EXCEPTION MECHANISM IS THE HALF THAT BINDS HARDER. A SESSION MAY NOT EXCEPT A DOCUMENT.** An
exception — a document the user wants kept as a contract home by delegation instead — is a **NEW
USER RULING NAMING THE DOCUMENT, TAKEN BEFORE THAT DOCUMENT'S ENTRIES ARE RE-HOMED, never after**;
taken after, it is void, because the entries it would have covered are already gone. **The exception
list was EMPTY when the rule was made, and that is a ruled state rather than an unfilled field.**
*Why the default falls this way:* the alternative — delegation as the default — grows the
contract-home class, requires the user's own writing per document under rule (g), and runs against
both concrete declinations already on the record; re-homing is what makes a decision findable
without the register standing in for the specification. *Why the timing clause is not decorative:*
it is the only thing that stops an exception being read back onto work already done, and the
mechanism has been exercised once, which is what shows it is real rather than notional. **What (l)
does NOT settle:** it chooses between two AVAILABLE routes and creates neither where the record says
there is none — an entry whose live content is already carried by a homed successor is not re-homed,
because that would put a second copy of a homed rule (#6), and an entry with no decision content to
write has nothing to re-home. That class stays dispositioned where it already was.
**(m) AN EVENT A MECHANISM EXISTS TO PRODUCE IS NOT A RULE NEEDING A HOME (user-ruled 2026-08-11;
the ruling record is `cowork_rulings_2026_08_11_tenth_stop.md`, Ruling 49, taking Ruling 44 of
`cowork_rulings_2026_08_09_ninth_stop.md`).** Rule (l) chooses between two available closing routes.
This is the neighbouring case it does not reach: an entry for which **neither route is owed, because
there is no rule to write at all.** **Where a register entry's whole content is an EVENT that a
standing mechanism exists to produce and has produced — an adoption, an admission, a membership
gained — the entry is CLOSED as that event, its register record standing as the event's index with
its evidence POINTED at the surface where the mechanism recorded it. No specification home is owed,
and inventing one is forbidden.** *Why:* writing such an entry into a rule-stating section produces
text nothing consumes, and it restates on a second surface what the mechanism's own output already
carries, which is what #6 forbids. The test is the one the words above state — **does a mechanism
exist whose ordinary operation produces this, and did it?** — so the class is recognised rather than
argued: an adoption event has an adopting mechanism and a table it wrote to, and an entry with
neither is not in this class. **What (m) does NOT reach:** an entry whose content is a RULE the
mechanism operates under, which is a rule and is homed like any other; and an entry whose content is
SUPERSEDED, which the supersession route already disposes. *Founding instance, and the reason the
clause is general rather than one entry's treatment:* three separate waves held entries they could
not place, and one of them turned out to have nothing to write — the needs vector's membership,
already carried at the table the adoption happened in.
**(n) A PER-CORPUS ESTABLISHMENT VERDICT IS A STATUS, SO THE DECISIONS REGISTER IS ITS HOME
(user-ruled 2026-08-11; the ruling record is `cowork_rulings_2026_08_11_tenth_stop.md`, Ruling 49,
taking Ruling 46 of `cowork_rulings_2026_08_09_ninth_stop.md`).** The phase-1 rule assigns STATUS to
this register and CONFORMANCE to the specifications; it does not say which of the two an
establishment verdict is, and this fixes it. **An establishment verdict (#19) about ONE corpus, one
measurement tool or one gate — that it is established, or that it is not, or that the route to
establishing it is exhausted — is the same KIND as supersession and shelving: register business.
Its home is this register itself, its evidence pointed at the record that measured it. No
specification home is owed.** **The converse binds equally and is the half worth reading:** writing
a one-corpus verdict INTO a rule-stating section is the mirror of the error the homing procedure's
findings-table STOP prevents — a section that states what shall be would then carry a dated finding
about one held collection, and a later reader would take the finding for the rule. *Why the line
falls at the KIND rather than at the subject:* a verdict about a corpus and a supersession about an
entry are both statements about the STANDING of something the record holds, which is what this
register is for; the rule the verdict bears on is elsewhere and is unmoved by it.

**★ HOW RULE (c) IS DISCHARGED ONCE IT HAS ALREADY BEEN MISSED (user-ruled 2026-08-09; the ruling
record is `cowork_rulings_2026_08_09_second_stop.md`, Ruling 12).** Rule (c) says a new ratification,
shelving or falsification gets its register entry IN the commit that records it. It does not say what
happens when a run of rulings has accumulated OUTSIDE the register — which is the state the rule is
meant to prevent and, once reached, a state the rule alone does not resolve. **The discharge is: the
accumulated rulings are CLASSIFIED first — per ruling, is this a DECISION the register carries, or
the exercise of one it already holds — the classification is put to the user as a reading file, and
the entries then land in ONE COMMIT, late but by the same pattern every on-time register event uses.
No entry is written before the user rules on the classification.** Two things this forbids, and they
are the reason it is written rather than left to be improvised: retro-fitting the entries ruling by
ruling as later dispatches happen to touch them, which leaves the register's completeness depending
on what came up next; and abandoning the debt on the ground that every ruling's CONTENT is already on
disk in a ratified record — which is true, and beside the point. **What is at risk when rulings sit
outside the register is not the rulings. It is the register's claim to be the ONE place a session
learns what was decided**, which is what rule (a) makes a session rely on.

## Project context

This is MuseScore Studio. The active development area is the `composing` module
(`src/composing/`), which implements harmonic analysis. See
`C:\Users\vince\.claude\projects\c--s-MS\memory\project_chord_analyzer.md` for
full project context.

## Autonomous operation — composing module

When working on the `src/composing/` module you are **pre-authorized** to:

- Edit any file under `src/composing/` without asking for confirmation
- Edit `src/notation/internal/notationaccessibility.cpp` without asking
- Edit `ARCHITECTURE.md` (project root) without asking
- Run the build: `powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`
- Run the tests: `./composing_tests.exe` from `ninja_build_rel/`
- Read `src/composing/tests/chord_mismatch_report.txt` after each test run

**Standard loop for mismatch reduction work** — do all of the following without
stopping for confirmation:
1. Analyse the mismatch(es)
2. Implement the fix in `chordanalyzer.cpp`
3. Build
4. Run tests and read the mismatch report
5. Report results (mismatches before → after, any regressions)

Only stop and ask if:
- A regression is introduced (mismatch count goes up or a previously passing
  test fails)
- A change would touch files **outside** `src/composing/` and
  `notationaccessibility.cpp`
- The catalog XML (`chordanalyzer_catalog.musicxml`) needs to be modified
  (ground-truth changes require explicit approval)
- You are uncertain whether a fix is correct and want a second opinion

## Build and test commands

**Always read these three files at the start of every session:**
- `C:\s\MS\BUILD_AND_TEST.md` — authoritative commands for all build variants, both test suites, and all Python tools
- `C:\s\MS\STATUS.md` — lean since the 2026-07-18 doc split: the current entries, active iteration/next
  action, and pointers to the ratified baselines (gate block (A) below)
- `C:\s\MS\DECISIONS.md` — the decisions register's INDEX (see the register section above); rulings
  bind mechanically only if every session reads them

Do not rely on memory of previous sessions for baseline numbers or iteration state — read STATUS.md.
`STATUS_ARCHIVE.md` and `cowork_handoff_archive.md` hold the superseded historical entries moved out
by the doc split (`cc_instruction_doc_split.md`) — reference-only, NOT part of the session-start read.

```
# Build — use PowerShell Start-Process (cmd.exe //c fails in MSYS2/Git Bash)
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Run composing tests (must be in ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe

# Run notation tests — includes P1/P2/P3/P4 pipeline regression test
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check (always --preset Baroque unless iteration says otherwise)
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report written to:
src/composing/tests/chord_mismatch_report.txt
```

**Both test suites must pass after every code change.** The notation tests include
`pipeline_snapshot_tests` which pins P1/P2/P3/P4 output against golden JSON files.
If a change intentionally alters chord output (e.g. a new inversion gate fires),
the pipeline snapshot goldens need refreshing. Note: `pipeline_snapshot_tests.exe`
is a SEPARATE binary from `notation_tests.exe` — pass `--update-goldens` to it:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
```
Then re-run `./pipeline_snapshot_tests.exe` to confirm all pass.
Only run `--update-goldens` when the output change is verified correct.

## Gate threshold and preset policy

Gate thresholds (e.g. Gate I: 0.45, Gate L: 0.35; Gate K is retired — removed from this list
by user ruling 2026-08-02, OI-260) are **calibrated
against the Baroque corpus** and are intentionally Baroque-specific. Do NOT adjust
them to accommodate other musical styles.

### (A) THE ROBUST-UNIT REGRESSION STOP (ratified R10-b, 2026-07-06)

**★ The governing hard regression stop** is the **granularity-robust union-of-boundaries unit,
variant (b) DCML-only** (music21 is NOT ground truth), duration-weighted and
**segmentation-invariant**. **Root governs; RN and key are always tracked beside it.** This is the
granularity-robust metric mandated at Stage 5; it **supersedes the batch 52/24/52 case-identity stop**
(now historical — see block (C)). Ratified at **R10-b (2026-07-06)**; handover provenance
`cc_stage5_r10b_ratification_report.md` (assembly surface: `cc_stage5_r10_assembly_report.md`).

**Committed reference (the diff base): `tools/robust_stop/`** — per-preset `stem@runStartTick`
variant-(b) root-failing run enumerations (**4547 runs on every preset** since the OI-178 adoption
2026-07-26 — identical across presets because inference is preset-independent; was ≈6506 / 6688 / 6522
Baroque/Jazz/Default under the superseded OI-168 legacy-analysis reference), the
`summary.json` aggregates, and `manifest.json` (corpus `git_hash` + instrument provenance + the offsets-
file hash + per-preset summary block + reproduce-status). Generated by the pinned instrument
`tools/a8_rebaseline_measure.py`, which self-validates its variant-(b) duration decomposition byte-
identical to `compare_rn.grid_score_regions()` on all 326×3 covered pieces. The manifest is **derived,
never hand-typed** (#17f): `tools/robust_stop_restamp.py` regenerates every recorded figure from the
candidate `summary.json`, and is established by reproducing the outgoing manifest exactly. A frozen
snapshot of the superseded batch sets lives at `tools/robust_stop/batch_stop_frozen_history.json` (block (C)).

**★ THE PINNED INSTRUMENT NOW DECLARES WHICH INFERENCE ARM ITS BASELINES WERE MEASURED ON, AND REFUSES
A CORPUS WHOSE STAMP DISAGREES (2026-08-03, phase 1y; recorded here 2026-08-04, phase 1z; `OPEN_ITEMS.md`
OI-307, D-468).** `tools/a8_rebaseline_measure.py` carries an expected arm, **defaulting to the joint arm
— the one every baseline in this block was measured on** — and a corpus whose `corpus_manifest.json`
records the other pipeline is refused rather than measured. `--expect-arm` states a different intent
explicitly. **It cannot move a measured value; it can only refuse** — run at HEAD over the production
corpus by this block's own two commands and diffed against the committed reference, the candidate is
indistinguishable from that reference on every preset and at every value the diff reports, in both
directions of the run-level set-diff (`tools/audit/instrument_arm_declaration_effect.json`; the refusal
half — a wrong-arm corpus detected, a right-arm one admitted, a caller declaring nothing unaffected —
at `tools/audit/corpus_arm_establishment.json`, probes 2, 3 and 4). *Why the default rather than an
opt-in:* **the defect was that an opt-in flag created an undetectable hole** — `--joint-inference` is
opt-in, so a regeneration that omits it silently fills the directory this instrument reads with the
other pipeline's output — **and an opt-in detector would reproduce that hole's shape exactly**, being
absent from precisely the invocation that most needs it. **Reversal is one default:** set
`EXPECT_ARM_DEFAULT` to `"any"` and the field is inert again. This is a change to a PINNED instrument
and is recorded here because this block is what pins it (#7).

**★ Ratified baselines — RE-BASELINED AT THE OI-178 JOINT-ESTIMATOR ADOPTION, 2026-07-26 (user-ratified,
option 1; measurement provenance `d615152c51`; report `cc_adoption_measurement_report.md`, record
`tools/joint_estimator/adoption_record.json`).** The joint estimator is now the **PRODUCTION inference
layer on the batch/corpus surface**: `batch_analyze --joint-inference <dir>` produces each `.ours.json`
from the joint module's decode (the L1 fact adapter → the ratified §5 decoder at the committed all-326
tables + the direct-metric SELECTED weight vector, seg_cap 4, leftover 2a); `run_bach_preset.py
--joint-inference` regenerates the corpus through it. **Inference is PRESET-INDEPENDENT** (the ratified
mode decision — presets are presentation concerns; the three preset dirs are identical at the inference
fields, so every column below is ONE value, not three): **root-agree 77.03 %, RN-agree 64.12 %, key-agree
vs HOME/global 56.14 %, key-agree vs LOCAL 78.42 %** (variant b, at 326/352 coverage; the OI-143 dual key
column both tracked; **key-abstain 0** — A commits its MAP path, the OI-33 flag reads zero). **The
hard-stop class-(b) root-disagree duration is 1,817,280 ticks per preset** (−33.0 / −34.7 / −33.1 % vs the
superseded OI-168 reference's 2 714 000 / 2 783 680 / 2 718 080; `robust_stop_diff` OVERALL PASS, the
run-level set-diff large in both directions by design, every added class-(b) run enumerated/diagnosed —
the genuine-new fifth-substitution subset is OI-192, the accepted cost side of the net trade).

**★ HOW THE ROOT COLUMN MUST BE READ — IT UNDERSTATES WHAT A WRONG KEY COSTS (D-576; recorded here
2026-08-04 on the user's ruling, READ WAVE 5).** A chord's root and its bass note are **largely
key-independent**: both can be named correctly while the key label is wrong. So the root-agreement
percentage barely moves when the tonality is misread — while the chord's **quality**, its **Roman
numeral** and some of its **inversions** are all corrupted by that same misreading. The corpus
measurement therefore reports **less damage than a reader or listener would see**, and a root figure
above must never be read as a statement about how good the analysis looks in the score. *Evidence:*
measured at the case that shows it — an anchor piece was systematically mis-keyed while the
root-governed baseline did not expose it, and what did expose it were the notation tests asserting
chord symbols and Roman numerals (`docs/key_detection_baroque_partial_signature.md`). *Why it is
written HERE rather than only at its own home:* this block is where the figures it qualifies are
published, and the same act was performed for the four grading conventions below — a figure and the
thing that bounds its meaning belong together. It is also **why the RN and key columns are tracked
beside the root** rather than instead of it (**D-115**, **D-211**): the root axis alone cannot see
this class of error. The caveat is about how the MEASUREMENT is read; it moves no value in it.

**STAGED SCOPE — CLOSED AT THE NOTATION SWITCH (user-ratified 2026-07-27).** The OI-178 adoption put the
joint estimator on the batch/committed surface only; **THE NOTATION SWITCH now puts it on the in-app
NOTATION surface too.** `useJointNotationRecord` defaults **ON**, so the in-app notation analysis — the
span-annotation emit, the implode chord-track, the tuning region path, and the note-seam (status-bar /
harmony-write / right-click-menu) — is produced by the joint estimator's A-native notation record (the
seams P0–P7 record path), NOT the legacy `analyzeHarmonicRhythm`/`analyzeChord` path. **The migration state
is now CLOSED on BOTH surfaces.** The legacy notation path remains **COMPILED and DORMANT** (selected only by
an explicit `useJointNotationRecord = false`), awaiting deletion at the **OI-180 retirement map, now fully
live**. The switch is ONE revertible commit: the pipeline-snapshot goldens were refreshed against the record
arm and every diff reconciled against the P6 classified evidence — **0 unexplained, 0 input-scoping, the
non-flag-gated surfaces byte-identical** (`tools/notation_seams/switch_golden_reconciliation.json`; the
inference/§3.3-presentation/inert-auxiliary split is the record arm's expected notation differences). **The
batch/corpus surface and `tools/robust_stop/` are UNMOVED** (the flag is notation-side; `test_batch_analyze_
regressions` passes, no `tools/corpus/` or `tools/robust_stop/` diff). Provenance: dispatch
`cc_instruction_notation_switch.md`; the P6 report `tools/notation_seams/dualarm_classified_report.json`; the
OI-178 adoption record `tools/joint_estimator/adoption_record.json`.

**Superseded columns preserved (#12):** the OI-168 LEGACY-ANALYSIS baselines (root 66.04 / 64.98 / 65.93,
RN 46.33 / 44.10 / 46.23, key-home 71.42 / 67.83 / 70.65, key-local 65.99 / 62.98 / 65.71) live in the
manifest's `reproduce_status.superseded_oi168` and the O-12 snapshot
`tools/robust_stop/snapshot_2026-07-26_pre_oi178_adoption/`. **The OI-168 narrative below is now HISTORICAL
(the superseded legacy-analysis reference), retained for provenance.**

*★ [SUPERSEDED by the OI-178 adoption 2026-07-26 — historical] THE OI-168 RE-BASELINE (2026-07-14; report `cc_oi168_fix_report.md`; outgoing reference preserved at
`tools/robust_stop/snapshot_2026-07-13_pre_oi168/`, O-12). **Every published column above is UNCHANGED at
the two decimals reported here** — what moved is the hard stop itself and the Jazz run count.
`analyzeChord`'s two key-consuming scoring terms (`dim7CharacteristicBonus`, `diatonicRootContribution`)
stopped testing membership in the mode-tonic-anchored set `{(keyTonicPc + scale[i]) mod 12}` and now test the
key SIGNATURE's own collection, `pcInMask(diatonicMaskFromFifths(fifths), pc)` — no tonic, no mode scale.
The two sets are provably identical for 19 of the 21 `KeySigMode` values and differ by a semitone
transposition for `Altered`/`AlteredDomBB7`. **Baroque and Default are BYTE-IDENTICAL** (352/352 `.ours.json`
each; every column and every run set unmoved — the δ=0 derivation verified at runtime, not on paper).
**Jazz: 9 `.ours.json` change and exactly ONE committed chord flips** — `bwv145.5@12960` (local key `D#alt`):
`Ebm` (root 3) → `B/Eb` (root 11), which is the DCML ground-truth root AND the music21 root (the sounding
D♯–F♯–B is a B-major triad; the old reading named a chord the notes do not contain). **The run-level set-diff
is REMOVAL-ONLY: one run, zero additions on any preset.** Class-(b) root-disagree duration **Jazz −480**
(2 784 160 → 2 783 680), Baroque/Default **+0**; class-(a) unmoved; the key columns unmoved (the key layer is
upstream of the corrected terms). Jazz variant-(b) runs 6689 → **6688**; Jazz root-agree 64.9772 → **64.9830 %**
(+0.0058 pp — below the reported precision, hence no column edit above). `robust_stop_diff.py`: **OVERALL
PASS** — the hard stop strictly DECREASES. No pipeline-snapshot golden was refreshed (the suite runs the
Default configuration, which is byte-identical). **Caveat carried forward (OI-170):** this fixed the two
SCORING terms, not the layer — `buildChordResult`'s `diatonicToKey` and the Gate I / Gate L
`invRootIsDiatonic` checks still answer a collection question through the tonic and still carry the same
defect. **L4 is NOT tonic-independent; no design may assume it is.**

*The KEY columns above supersede the OI-142/OI-143 column (key home 71.29/67.49/70.52, key local
65.72/62.49/65.39), preserved in `tools/robust_stop/snapshot_2026-07-13_pre_oi132_oi144/`. **Root and RN did
NOT move** (the mode reduction touches only the key axis): every root-failing run set is byte-identical, the
class-(b) root-disagree duration is unchanged on all presets, and the run-level set-diff is (+0 / −0). What
changed: the five dominant-family exotic modes (Phrygian dominant, altered, Lydian dominant, Lydian augmented,
Mixolydian ♭6) now reduce to the MINOR key of their PARENT COLLECTION — an emitted "C♯PhrygDom" grades as F♯
minor, the key it is the dominant of — in the ONE shared reduction `compare_rn._our_key_tonic`, onto which the
second key parser (`oracle_root_metric`) was folded. Key-abstain also drops (7680/10800/33120 → 0/4080/2400
ticks). The user's ruling and the evidence: `cc_mode_grading_adjudication_probe_report.md` (the parent-collection
reading matches the DCML annotators on 67 % of the affected duration on the local column; the tonic-triad
reading on 0 %). Provenance: `cc_key_grading_and_calibration_rebaseline_report.md`.*

*Earlier columns, for the record: the OI-142/OI-143 re-baseline (user-ratified 2026-07-12) applied the 12
transposed editions' constant offsets to the WiR ground truth at the shared substrate
`dcml_parser.load_wir_regions` (OI-142) and split the key column into home/local (OI-143); its run-level
set-diff was confined to the 12 corrected stems and the class-(b) root-disagree duration DECREASED on all
presets (`cc_key_grading_rebaseline_report.md`; offsets in `tools/robust_stop/corpus_transposition_offsets.json`).
It in turn superseded the R10-b column (root 63.36/62.37/63.25, RN 44.58/42.40/44.41, key 68.13/64.43/67.50),
preserved in `tools/robust_stop/snapshot_2026-07-12_pre_oi142_oi143/`.*

- **The hard stop (per preset):** the **class-(b) (pitch-class-decidable-root) root-disagree DURATION
  must be NON-INCREASING** vs the committed reference — the *meaningful* functional errors never grow.
  Any preset increasing ⟹ FAIL. Run (≈6 s total):
  ```
  python tools/a8_rebaseline_measure.py --out-dir <cand> [--corpus-root <scratch>]   # self-validates grid==oracle per piece
  python tools/robust_stop_diff.py --candidate <cand>                                # exit 0 iff every preset passes
  ```
- **The mandatory explained diff:** every run lists the **run-level set-diff** vs the reference
  (added/removed `stem@runStartTick` runs, each tagged with its two-tier class). Zero-new-case cannot
  scale to ~7k runs, so the gate is a **duration non-increase + an explained per-run diff**, NOT a
  set-identity.
- **Class-(a) duration is TRACKED** (a large net increase trips the `robust_stop_diff.py` INVESTIGATE
  flag — advisory threshold `CLASS_A_INVESTIGATE_TICKS = 9600`, the guardrail-(3) "many symmetric
  sonorities destabilized" carry-over), never an automatic stop; class-(b) is the hard stop above. On
  this unit class-(b) is **~96.5 %** of root-fail time (vs ≈53 % class-(a) on the old batch residual) —
  the robust stop is governed by the meaningful count.
- **Re-baseline discipline for future adoptions (the 2.2e pattern, generalized):** an adoption that
  changes a fitted value **re-baselines the `tools/robust_stop/` reference artifacts** in the adoption
  commit — the run-level set-diff (removals/additions, each with class) **explained per case and
  ratified**, the class-(b) duration non-increase **proven per preset**, the manifest re-stamped with
  the new corpus `git_hash`, and the **outgoing reference snapshotted first (O-12)**.
- **A NEWLY ACQUIRED CORPUS ENTERS AS RESEARCH MATERIAL; the frozen corpus above stays the gate until a
  deliberate re-baseline** (user-ratified 2026-07-02; homed here 2026-08-02 from `STATUS_ARCHIVE.md`,
  `OPEN_ITEMS.md` OI-272). Music brought into the project for study does not become part of the pass/fail
  check by arriving. Promoting any of it into the gate is the separate, deliberate re-baseline act the
  bullet above describes, with its snapshot and its ratification. *Why:* **derivation not recorded** — the
  record states the rule without giving a reason for it. Distinct from the regenerate-before-restamp rule
  (`BUILD_AND_TEST.md`), which governs the order of operations once a corpus is already the gate; the same
  research-tier-on-entry rule is stated on the corpus side at `cowork_score_census.md`'s decision-tier block.

**★ THE FOUR GRADING CONVENTIONS THE ROBUST UNIT IS MEASURED UNDER (each ruled earlier; written into
this block 2026-08-02 because until then they were recorded only on the open-items rows that tracked
building them, or on a session-handoff archive — surfaces that track work and are not a home for a
standing convention).** Every number in this block depends on all four.

- **THE ONLY GROUND TRUTH IS THE HUMAN ANNOTATION. The algorithmic analysis is a noise filter, never a
  standard of correctness** (user mandate 2026-06-10; homed here 2026-08-02 from `cowork_handoff_archive.md`,
  `OPEN_ITEMS.md` OI-272). Accuracy is measured against the published human analyses — *When in Rome* /
  DCML — and against nothing else. music21 is an algorithmic second opinion used to filter noise, so a
  count taken through it is a LOWER BOUND on human-adjudicated error, not an agreement rate. Three clauses
  follow from that and are part of the convention: **(i)** a measurement filtered through the algorithmic
  analysis is never described as "ground-truth agreement"; **(ii)** the human-annotation-only variant is
  the one that governs — delivered as the variant-(b) DCML-only unit above; **(iii)** **no self-annotation
  ever enters a measurement** — our own outputs, the catalog and the goldens are regression pins that hold
  behaviour against change, never a standard of correctness. *Why:* stated with the mandate — where the
  algorithmic analysis sides with us against the human annotator the case is excluded by an algorithm's
  opinion, so the count understates the human-adjudicated error; and a system graded against its own
  output measures only that it has not changed.
- **An exotic mode is graded against its PARENT COLLECTION's minor key, not against its own tonic
  triad** (user-ruled 2026-07-13, OI-132; landed `800f1a12bf`). When our analysis emits one of the five
  dominant-family exotic modes, grading reduces it to the minor key of the collection it belongs to — an
  emitted C♯ Phrygian dominant grades as F♯ minor, the key it is the dominant of. *Why:* measured — on
  the affected duration the parent-collection reading agrees with the DCML annotators on **67 %** of the
  local key column and the tonic-triad reading on **0 %** (`cc_mode_grading_adjudication_probe_report.md`).
  The consolidation moved the key columns only: root, Roman numeral, every root-failing run set and the
  class-(b) hard-stop duration were byte-identical, run-difference +0/−0 on all presets
  (`cc_key_grading_and_calibration_rebaseline_report.md`). It is implemented in ONE shared reduction,
  `compare_rn._our_key_tonic` (#6), onto which the second key parser was folded.
- **Key agreement is reported against BOTH the global home key and the local key** (user-ratified
  2026-07-12, OI-143; adopted `d9b52ba969`). Both columns are carried everywhere the key column appears;
  neither replaces the other. *Why:* measured — the local percentage is lower than the home percentage, and that
  difference is itself the finding (the analysis tracks the tonal home more faithfully than it tracks
  momentary tonicizations), so keeping one column would have hidden a real property of the system.
- **The stop is ABSTAIN-AWARE: on the root axis an abstention counts as a DISAGREEMENT** (ruled and
  mechanically enforced 2026-07-12, OI-33). A cell where our analysis carries no root pitch class is
  scored as a root disagreement; on the key axis abstained cells are instead **excluded from the
  agreement denominator** and the abstain duration is published beside the percentage, with
  `robust_stop_diff.py` flagging any rise in the candidate's abstain rate. *Why:* an agreement
  percentage is abstention-reducible — without the convention a change that made the system decline more
  often would raise the percentage without analysing anything better — and the convention was owed before any
  abstaining path could be gated on this stop at all. The one abstain decision on the key axis is
  `compare_rn._our_key_ident`; every graded surface routes through it rather than re-deciding what counts
  as an abstention. On the production arm the decoder never abstains on the key axis, so the counter reads
  zero (the joint estimator's standing rules (d), `ARCHITECTURE.md`).

**★ THREE FURTHER MEASUREMENT CONVENTIONS, HOMED HERE 2026-08-07 ON THE USER'S HOMING RULING.** They
sit BESIDE the four above and not among them: the four were ruled together as the set the robust unit
is measured under, and each of these three was ruled separately and earlier. Every one of them binds
on any measurement this block publishes.

- **A measurement publishes its COVERAGE DENOMINATOR and its PER-CORPUS breakdown; a single aggregate
  number that hides which corpus moved is not reported** (2026-06-13; the record states no ratifier).
  The denominator published is the number of pieces the measurement actually resolved to a human
  annotation, never the number of pieces held — which is why every baseline above is stated at its
  coverage rather than over the whole corpus. *Why:* stated with the rule and evidenced in the same
  sentence — only some of the gate chorales resolve to a human annotation at all, so dividing by the
  whole set reports an accuracy the measurement never had; and the root-error rate ranges widely
  across corpora, so a single scalar objective would let a fit win on chorales while losing on another
  repertoire, with nothing in the reported number showing it.
- **A layer's measurement is judged on COVERAGE-MATCHED ACCURACY and CORRECT ABSTENTION, never on raw
  coverage** (2026-06-26; the record states no ratifier). Two things are reported together: how
  accurate the layer is over the cases it answered, and whether the cases it declined were ones it
  should have declined. Abstaining on a genuinely undecidable case is a RIGHT outcome, not a gap.
  *Why:* recorded as the lesson of a completed layer build, where the decoder measured materially
  better than the path it replaced WHERE IT COMMITS and most of its abstention was established as
  genuinely undecidable at that layer — which raw coverage would have read as a failure. It is also
  the reason the stop above is abstain-aware: an agreement percentage that ignores abstention is
  reducible by declining more often.
- **While the pipeline is being rebuilt, a behaviour-changing increment is graded DIRECTIONALLY and
  not against a fixed bar** (user, 2026-06-22). Both the baseline numbers AND the metric definitions
  move as the layers around an increment are reconstructed, so a rebuild step is judged on whether it
  moved the specific defects it was meant to move, in the right direction; the comparison that means
  something is against the fully reconstructed pipeline, not increment by increment. *Why:* stated
  with the decision — a fixed bar set during a rebuild is a bar against a measurement that no longer
  exists by the time it is tested. It is the reasoning #16 and #24 apply to reproducibility and to
  sampling noise, applied to a measurement whose definition is still in motion. It settles WHETHER a
  fixed bar is admissible during a rebuild; how a bar is set once one is set at all is the separate
  standing rule that a pass-bar is fixed only after the baseline is measured.

**★ TWO MORE GRADING CONVENTIONS, HOMED HERE 2026-08-07 ON THE USER'S HOMING RULING.** They sit
beside the seven above and were each ruled separately. Both bind on how a disagreement this block's
figures contain is READ; neither moves a value in them.

- **A DEFENSIBLE MODAL READING THE MAJOR/MINOR GROUND TRUTH CANNOT REPRESENT IS A GROUND-TRUTH
  LIMITATION, NOT A DEFECT TO OPTIMIZE AWAY** (user, 2026-06-22). Where our analysis emits a mode
  the published human annotation has no way of writing down — the annotation records major and
  minor only — a resulting disagreement is a limit of the ground truth, not an error of the analysis.
  **Do not chase the major/minor ground truth on a modal reading**, and do not tune such a case
  away: doing so makes the analysis worse in order to match a notation limit. *Why:* measured on
  the affected population — the large majority of the jazz key misses are perfect-fifth
  displacements where our reading is a defensible modal one, which places them inside the layer's
  own done-criterion (defensible-or-flagged on an ambiguous case) and inside the stated scope
  caveat that the ground truth is major/minor only. **Distinct from the exotic-mode convention
  above**, which decides how a modal emission is SCORED; this decides what a REMAINING disagreement
  means. Distinct also from the separate rule governing what the key layer may EMIT. It is
  principle #21 applied at the point of reading: the ground truth is an instrument, and a
  disagreement it cannot represent is not evidence about us.
- **THE BINDING METRIC FOR A MODULATION DETECTOR IS MODULATION CORRECTNESS — explicitly NOT the
  agreement percentage** (2026-06-14; the record states no ratifier). A change that decides where
  the music changes key is judged on whether the key changes it commits are real ones (precision)
  and whether it finds the real ones (recall) — the track rate together with the de-masked partial
  split — and never on the overall agreement percentage. *Why:* stated with the decision — the
  agreement percentage is **gameable by the change under test**, so it cannot be that change's own
  bar. It is the same defect the abstain-aware convention above exists against on the root axis: an
  agreement percentage a behaviour change can move without analysing anything better is not a
  measurement of that change. The honesty measurement named with it is the de-masking diagnostic,
  which exposes a committed home-key label being credited against a ground-truth local key.
  **★ READ IT BESIDE THE CREDITING-RULE PROHIBITION IMMEDIATELY BELOW, WHICH IS A DIFFERENT
  BINDING STATEMENT OF THE SAME DATE.** This convention fixes WHICH BAR a modulation-detecting
  change is graded against; the one below forbids AMENDING the comparison itself. A session can
  obey either while breaching the other, which is why they are two entries and not one.

**★ THE CREDITING RULE IS NOT AMENDED TO COUNT A TONICIZATION LABEL AS AGREEING WITH THE
ANNOTATOR'S MODULATED NUMERAL; ONLY A DIAGNOSTIC PARTIAL-SUB-SPLIT IS DEFENSIBLE** (2026-06-14; the
record states no ratifier for the decision itself. Homed here 2026-08-09 on the user's ruling —
Ruling 11 of `cowork_rulings_2026_08_09_second_stop.md` — as the MEASUREMENT half of register entry
**D-291**, whose BUILD half belongs to the Layer-5 function specification and is not restated here,
#6. **SPLIT INTO TWO REGISTER IDENTIFIERS 2026-08-09** on the user's Ruling 21 of
`cowork_rulings_2026_08_09_fourth_stop.md`: this half now carries its own entry, **D-656**, and
**D-291** keeps the build half; the two cross-reference each other, and neither text changed).
Where our analysis labels an applied chord relative to the home key and the human annotator
has changed key, the comparison is **not** to be changed so that the label counts as agreement. The
prohibition survives in the words it was recorded in: *"Crediting rule NOT warranted (harmful —
masks the 95% real error); only a DIAGNOSTIC partial-sub-split (expose the masking) is
defensible."* *(The percentage inside that sentence is the source's own wording, quoted rather than
reported: every value of that measurement lives in `cc_tonicization_modulation_metric_dossier.md`
and none is restated here, #17f, **D-431**.)* *Why:* measured before it was decided — the
comparison already credits such a label by root and quality, so it does not over-penalise, it
**MASKS**; and the affected cases are overwhelmingly cadence-confirmed local keys of substantial
length, so the annotator's modulation is the correct reading for nearly all of them. Amending the
crediting rule would therefore raise the reported Roman-numeral agreement while the underlying key
reading stayed wrong — and, unlike a bar set for one change, it would corrupt the Roman-numeral
column for **every** measurement this block publishes. **★ READ IT BESIDE THE
MODULATION-CORRECTNESS CONVENTION IMMEDIATELY ABOVE** — same date, same source dossier, same masking
argument, and both name the de-masking diagnostic as the honesty measurement. They are nonetheless
**two decisions**, established by a verbatim comparison of the two texts on 2026-08-09: this one
governs the comparison itself and binds on every measurement; that one governs the bar a
modulation-detecting change is judged at. Collapsing them would lose this, the more specific and
more easily violated prohibition (#12).

**★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; `cc_a8_rebaseline_measure_report.md`).** The
**primary reported metric AND the Stage-5 fitting-objective basis** is the robust unit above: root
governs, RN + key(home,local) tracked beside. **★ Ratified baselines — RE-BASELINED AT THE OI-178
JOINT-ESTIMATOR ADOPTION, 2026-07-26 (user-ratified, option 1; the joint estimator IS the production
inference layer on the batch/corpus surface, PRESET-INDEPENDENT — full detail in block (A) above):
root-agree 77.03 %, RN-agree 64.12 %, key-agree vs HOME/global 56.14 %, key-agree vs LOCAL 78.42 %**
(one value per column, all three presets; class-(b) hard-stop duration 1,817,280 per preset;
`robust_stop_diff` OVERALL PASS; measurement provenance `d615152c51`, `cc_adoption_measurement_report.md`).
**The recitation that follows is HISTORICAL — the superseded OI-168/OI-132 legacy-analysis lineage,
retained for provenance.** *The superseded OI-168 columns (variant b, 326/352 coverage; re-baselined at
the signature-mask fix, 2026-07-14, `cc_oi168_fix_report.md`; the movement then was Jazz root-agree
+0.0058 pp, the Jazz run count 6689→6688 and class-(b) −480 vs the OI-132 mode-grading consolidation,
user-ratified 2026-07-13, `cc_key_grading_and_calibration_rebaseline_report.md`): **root-agree Baroque
66.04 % / Jazz 64.98 % / Default 65.93 %**, RN-agree 46.33/44.10/46.23 %, **key-agree vs HOME/global
71.42/67.83/70.65 %** + **vs LOCAL 65.99/62.98/65.71 %** (the OI-143 dual column, both tracked). That consolidation reduces the five
dominant-family exotic modes to their PARENT COLLECTION's minor key in the one shared reduction
`compare_rn._our_key_tonic`; it moved the KEY columns only — root, RN, every root-failing run set and the
class-(b) hard-stop duration are byte-identical (run-diff +0/−0 on all presets). The key columns it superseded
(home 71.29/67.49/70.52, local 65.72/62.49/65.39) came from the OI-142/OI-143 re-baseline (user-ratified
2026-07-12, `cc_key_grading_rebaseline_report.md`), which applied the 12 transposed editions' offsets to the
WiR ground truth at `dcml_parser.load_wir_regions` (OI-142) and split the key column (OI-143); its run-diff was
confined to the 12 corrected stems (the other 314 byte-identical) and class-(b) root-disagree duration
DECREASED on all presets. *The superseded R10-b column (root
63.36/62.37/63.25, RN 44.58/42.40/44.41, key 68.13/64.43/67.50), preserved in
`tools/robust_stop/snapshot_2026-07-12_pre_oi142_oi143/`, was itself re-baselined at the 2.2e kWStepIn
adoption, 2026-07-05; its key-column establishment history: Jazz is byte-identical to the pre-adoption
corpus — proven by an explicit-override
reconstruction — so its root/RN reproduce the prior 62.37/42.40 exactly, and by that **same
byte-identity its key reproduces the prior 64.43 exactly** (measured 64.4321): identical `.ours.json` +
WiR + git-unchanged key-path code cannot move the figure. The earlier-recorded 2.2e key column
**68.19/64.52/67.77 was a non-reproducible measurement-entry error**, corrected at R10-b (2026-07-06) to
the reproducible **68.13/64.43/67.50**; Baroque shows a tiny +0.015 pp shift vs the prior 68.11 from the
kWStepIn re-segmentation, Jazz/Default reproduce the prior 64.43/67.50 to the digit. Prior baselines:
63.32/62.37/63.22, RN 44.56/42.40/44.40, key 68.11/64.43/67.50.)* When it governs, the **hard stop is
the class-(b) root-disagree DURATION non-increase per preset** + the **mandatory explained per-run
set-diff** (zero-new-case cannot scale to ~7,000 runs; class-(b) dominates ~96.5 % at this unit). C1
reliability curves on this unit: `cc_c1_reliability_report.md`.

### (B) The two-tier per-cell class policy — CARRIED OVER, LIVE

**This policy is UNCHANGED at R10-b and now governs the robust unit's per-cell classification** (the
class-(a)/(b) split on the robust unit's failing runs, and the block-(A) class-(b) duration hard stop).
It was authored against the batch BIR=false gate (block (C)); every guardrail, definition, and founding
case below carries over verbatim to the robust unit. (The "BIR=false case" phrasing below is the batch
framing under which it was ratified; on the robust unit the same classification applies per failing
run/cell.)

**Two-tier refinement (user-ratified 2026-06-22) — class-(b) functional regression vs class-(a)
symmetric-rotation churn.** A *new* BIR=false case is one of two classes:
- **Class (b) — functional/key regression: UNCHANGED HARD STOP.** A new BIR=false case at a sonority
  whose root is *pitch-class-decidable* (any non-symmetric chord — triads, dominant sevenths, etc.)
  where the analysis now gets the root or key wrong. **Zero** new class-(b) cases on any preset, ever.
  This is the gate's real intent and does not move.
- **Class (a) — symmetric-rotation churn: TRACKED, CONDITIONAL (not an automatic hard stop).** A new
  BIR=false case at a sonority whose root is *pitch-class-undecidable by construction* — symmetric
  diminished-seventh, augmented, whole-tone, or a share-tone tetrad (half-dim↔m6; dim7-subset-of-V7♭9;
  Maj7↔relative-minor triad). The pitch-class analyzer is spelling-blind and cannot pick the
  spelling-correct rotation; no rotation is more correct by pitch class. Acceptable **only when ALL** of:
  (1) **verified at the score per case** against the actual notes (e.g. the music21 GT region) —
  assertion is not enough; (2) **default to class (b) on any doubt** — if not *proven* class-(a), it
  IS class-(b); (3) **the class-(b) (pitch-class-decidable-root) BIR=false count is non-increasing** on every preset —
  the *meaningful* errors never grow; the class-(a) total may wobble by a **small, every-case-verified**
  amount (the rotation count is a coin-flip, not a quality measure), but a **large class-(a) net
  increase trips mandatory investigation** (a change destabilizing many symmetric sonorities is a
  signal even when each case is individually class-(a)); (4) **case identities recorded** (stem@tick +
  sonority); (5) **interim only** — a
  bridge pending the Stage-5/6 spelling-aware (two-tier) gate, which retires this exception. Applies
  **only** to the symmetric/share-tone structural class; no other source of a new BIR=false case
  qualifies. Root cause: the rotation churn is a **chord-layer (Layer-4) root ambiguity** *surfaced,
  not caused,* by a key change; the proper fix is spelling/voice-leading-aware chord-root selection
  (Layer 4 / Stage 5–6). Founding evidence (Cowork-verified at the score, music21 GT, 2026-06-22):
  `bwv272@4320` (G♯dim7), `bwv289@20160` (A♯dim7), `bwv291@17760` (Eø7↔Gm6), `bwv387@10560`
  (G♯dim7/E7♭9) — all symmetric/share-tone, zero functional regressions; the Layer-3 decoder-wiring
  increment. Full provenance: `cowork_gate_policy_amendment.md`.
- **First accepted class-(a) interim case (Layer-3 wiring, 2026-06-22):** Baroque/Default net **−4** (all new
  cases class-(a)); **Jazz net +1** — accepted under guardrail (3): new `bwv272@4320` (G♯dim7 coin-flip) +
  `bwv291@17760` (Eø7↔Gm6 same-collection center), `bwv244.15@10080` fixed; both new verified class-(a) at the
  score, zero new class-(b), and the L3 reduction-rule lever measured byte-identically inert (a≡b on all presets) —
  so the +1 is irreducible at Layer 3. **Retires when Layer 4 (function/cadence) pins the rotation/center** —
  rotation-pinning is a named early Layer-4 job. Investigation: `cc_layer3_jazz_churn_investigation.md`.

### (C) RETROSPECTIVE — the batch 52/24/52 stop (superseded at R10-b, 2026-07-06 — historical reference)

> The `52/24/52` `stem@tick` case-identity sets below and their full L3-wiring / 2.2e / corrected-parser
> history were **THE hard regression stop through Stages 2–5**. They are **superseded** by the robust-unit
> stop (block (A)) at R10-b and are preserved here as historical reference only. Machine-readable snapshot:
> `tools/robust_stop/batch_stop_frozen_history.json`. Full handover provenance:
> `cc_stage5_r10b_ratification_report.md` (+ assembly `cc_stage5_r10_assembly_report.md`). **Why it was
> replaced:** the batch (cross-barline) region gate under-counted the true per-onset root error **~15–56×**
> — it measured a small music21-filtered reachable corner (class-(a) was ≈53 % of that residual vs ~3.5 % on
> the robust unit) — so the robust-unit stop replaced it at R10-b.

**The batch stop's diagnostic form — KEPT (no longer the stop).** `characterise_bir_false.py` remains a
runnable per-region diagnostic (useful for triage and for cross-checking the robust unit); it is no longer
the regression gate. Its corpus-integrity mechanism is **shared by the robust stop** — the block-(A) a8
instrument imports `characterise_bir_false.validate_corpus_dir`, so this guard cannot bit-rot into
uselessness. Since Stage 2.2a (M3 fix) each preset writes to its **own** dir under `tools/corpus/` and stamps
a `corpus_manifest.json`; `run_bach_preset.py` clean-slates the dir at the start of a regen and **exits
nonzero** unless the corpus is complete (**352/352** at current HEAD — the expected count is derived from the
source `.xml` files, not hard-coded); `characterise_bir_false.py` **refuses** to measure a dir whose manifest
is missing, incomplete, or whose `.ours.json` fingerprints do not match (preset contamination — the old
shared-`tools/corpus` failure mode). Re-run the batch diagnostic with:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz
```

**Re-baselined 2026-06-13 (corrected GT parser).** The prior **13/7/14** gate was an
**undercount**: GT-parser bugs (applied-chord `/X` rooting + minor-key
leading-tone/submediant rooting, fixed in `tools/dcml_parser.py`) corrupted the WiR roots
of applied and `viio`/`vio` chords, pushing genuine candidate cases into the discarded
`all_differ` bucket. With the roots now oracle-correct (music21 `RomanNumeral`, **100% on
all gate cases**), those cases surface. The new gate is a **strict superset** of the old
(every old case preserved, **0 lost** — verified through the canonical tool with an A/B
parser revert). **~95% of the added mass is legitimate ambiguity** — chiefly **symmetric
fully-diminished-7th** sonorities (root pitch-class-undefined by construction; ≈53% of
Baroque) and **viio↔V7 share-tone** readings; the genuinely-new *actionable* error count
is only ~1–3 per preset (net ≈9–10 Baroque / ~4 Jazz). The symmetric-dim7 members are
structurally unresolvable by pitch class and are the seed of a future **two-tier /
spelling-aware** gate (Stage 5/6 — noted, not built). Full provenance:
`cc_metric_rebaseline_report.md` + `cc_gate_rebaseline_verify_report.md`.

**★ (Historical — the batch stop's FINAL frozen state before R10-b) `52 / 24 / 52` (re-baselined at the
ratified 2.2e kWStepIn adoption, 2026-07-05, commit `c50002fee1` + the corpus chore below; frozen as history
at R10-b, 2026-07-06 — machine-readable at `tools/robust_stop/batch_stop_frozen_history.json`).** The 2.2e
delta vs the prior `53 / 24 / 53`: **removal-only
`{bwv244.32@5760}`** on Baroque + Default (the class-(b) case the kWStepIn 0.10→0.125 adoption fixed); Jazz
unchanged (byte-identical). The identity sets below are the 52/24/52 form; the history that produced the
prior 53/24/53 is preserved in the following paragraph.

**★ (History) Corrected to the ratified post-L3-wiring state `53 / 24 / 53` (Stage-0 measurement, commit `b57dbfa7a8`,
2026-06-25).** The `57/23/57` sets previously listed here predated the **already-ratified L3-wiring delta**
(`−4 / +1 / −4`) — the two-tier-gate prose above describes that delta, but these integer tables were never updated.
They are now. The delta, verified by diffing the measured sets against the prior `57/23/57` sets: **Baroque**
`− {bwv102.7@17520, bwv122.6@6720, bwv227.7@18120, bwv301@960, bwv336@8640, bwv381@4800}` (six fixed)
`+ {bwv272@4320, bwv289@20160}` (two class-(a) symmetric dim7) = net **−4**; **Jazz** `− {bwv244.15@10080}`
`+ {bwv272@4320, bwv291@17760}` = net **+1**. (Baroque and Jazz deltas Cowork-verified against the prior sets;
Default measured at `53`.) The **case-identity set, not the integer, is the gate** — re-measure with
`characterise_bir_false.py` after any change.

- **Baroque = 52** with identities (stem@tick):
  `{bwv10.7@36000, bwv14.5@8160, bwv144.6@15360, bwv144.6@16320, bwv151.5@13440, bwv153.1@18240, bwv16.6@16800,
  bwv169.7@24960, bwv17.7@46080, bwv174.5@6240, bwv20.11@13440, bwv244.46@960, bwv245.15@13920,
  bwv245.17@4800, bwv245.37@13920, bwv245.3@12480, bwv245.40@51360, bwv258@10560, bwv261@33840, bwv269@20640,
  bwv272@4320, bwv272@4800, bwv272@8160, bwv282@9120, bwv289@20160, bwv289@21600, bwv300@13440, bwv309@8640,
  bwv320@31680, bwv334@5280, bwv334@6720, bwv342@25440, bwv352@1440, bwv358@6000, bwv364@2880, bwv392@14400,
  bwv40.3@2400, bwv402@22080, bwv416@10080, bwv421@2880, bwv422@23040, bwv423@28320, bwv429@24240, bwv432@5520,
  bwv45.7@20160, bwv48.3@2880, bwv57.8@15360, bwv60.5@30960, bwv64.8@5280, bwv77.6@22080, bwv94.8@24960,
  bwv96.6@13440}` (= prior Baroque-53 − `{bwv244.32@5760}`, the class-(b) case the 2.2e kWStepIn adoption fixed;
  `characterise_bir_false.py --corpus-dir tools/corpus/baroque`, re-baselined at the ratified 2.2e adoption, removal-only).
- **Jazz = 24** with identities (stem@tick):
  `{bwv144.6@15360, bwv144.6@16320, bwv245.15@13920, bwv245.17@4800, bwv245.37@13920, bwv245.40@51360, bwv272@4320,
  bwv272@8160, bwv280@17280, bwv282@9120, bwv291@17760, bwv301@1440, bwv313@14880, bwv334@5280, bwv342@25440,
  bwv392@14400, bwv422@23040, bwv429@24240, bwv432@5520, bwv45.7@20160, bwv48.3@2880, bwv64.8@5280, bwv74.8@13440,
  bwv74.8@13920}` (= prior Jazz-23 − {bwv244.15@10080} + {bwv272@4320, bwv291@17760}).
- **Default (the user-run config) = 52.** Per the `characterise_bir_false.py --corpus-dir tools/corpus/default`
  measurement, Default = Baroque-52 with `{bwv352@1440, bwv60.5@30960}` replaced by `{bwv227.7@18000, bwv387@10560}`
  (the rest identical to Baroque-52). Re-baselined at the ratified 2.2e adoption: removal-only `{bwv244.32@5760}`
  vs the prior Default-53 (the same class-(b) case the kWStepIn adoption fixed on Baroque). *(✅ RE-CONFIRMED by measurement at the 2026-07-03 grammar-completion regen
  (`cc_grammar_completion_report.md`, commit `ce509b0961`): all three presets' case-identity sets matched this
  document exactly, set-diff empty both directions — the earlier Stage-0 prose-inconsistency caveat is discharged and
  the Default identities above may be relied on.)*

### (D) Caveats

**Cross-layer-budget caveat (2026-06-24, O1 measurement) — LIVE (an interpretation caveat, not a granularity
one; it applies equally to the robust unit).** the BIR=false set is **not** the Layer-5 resolver
residual — it is a **work budget distributed across Layers 1–5**, and it overstates the function-only remainder
several-fold. Measured during the O1 investigation (`cowork_uncertain_resolver_investigation.md` +
`cc_uncertain_resolver_measurement_report.md`): ≈60% Baroque / ≈42% Jazz are **spelling-resolvable** (the Layer-4
notated-spelling root pin), and most of the rest is **bass/inversion**, **local voice-leading**, or plain
**segmentation over-grab** the change-point slicer (Layer 2) removes by construction (e.g. `bwv10.7@36000` — a 5-note
scale `C-D-E♭-F-G` over-grabbed across two GT chords `i43`/`iv532`, Cowork-verified at the score). The genuinely
**function-only** remainder reaching Architectural Layer 5 is small: pitch-class-identical share-tone chords
(`bwv352` Am6↔F♯ø7; Jazz `bwv291` Eø7↔Gm6) on the chord side, and the **note-identical** key-disagreement class
(relative major/minor, tonicization-vs-modulation) on the key side. So a BIR=false count is read as cross-layer work,
not as any one layer's accuracy. (O1 resolved: the resolver of "uncertain" is Layer 5 itself, no separate box.)

**★ CORRECTION OF RECORD TO THE CAVEAT ABOVE — THE FUNCTION-ONLY SHARE IS OVERSTATED, BECAUSE
OVER-GRABBED SEGMENTATION CORRUPTS THE BASS AND NOT ONLY THE PITCH-CLASS WINDOW (2026-07-10; the
record states no ratifier).** The apportionment above books a share-tone class as function-only on
the ground that the competing readings contain the same pitch classes and so cannot be separated
earlier. A desk simulation refuted that on its own named case: an over-grabbed stretch picks up a
**bass** note that does not sound where the error is, and the bass is exactly what separates the two
readings — so some of what this caveat books as reaching Architectural Layer 5 is resolvable at the
segmentation layer. *Why it is recorded here:* this block is where the apportionment is published,
and a reader of the apportionment must meet its correction. *Why it is evidence and not a
surprise-at-build (#13):* it was found at the desk-simulation stage, before any measurement was
built — the prior was written down, traced by hand at the score and refuted cheaply, which is what
the explorational stage exists for under the scope clause at #17–#19.

**Granularity caveat (Stage 2.2-i) — ✅ RESOLVED at R10-b (2026-07-06).** The mandate this caveat raised — "a
granularity-robust metric is mandatory at Stage 5" — is **delivered**: the block-(A) robust-unit stop is the
granularity-robust (segmentation-invariant, duration-weighted, union-of-boundaries) metric, and it now governs
as the hard stop. *(Historical statement of the resolved problem, kept for provenance:)* the former batch
`53/24`→`52/24/52` gate was measured at **batch (cross-barline) region** granularity; the user-visible
**per-beat** root-error rate is ~7× higher when the same scores are scored at measure-aligned (section)
granularity — the block-(A) unit closes that gap. Inspect the per-beat view with `batch_analyze
--section-level` (diagnostic flag, default OFF). See `cc_stage2_2_ab_dossier.md` for the A/B that quantified
the granularity gap.

(`tools/analyze_inversion_errors.py` is a *separate* secondary metric: its three-way
`music21_dcml_agree` genuine split is `bassIsRoot` true/false. **Re-measured under the
corrected parser** (`cc_functional_residual_dossier.md`, 2026-06-14): **Baroque 24/13→47/57,
Jazz 35/7→81/23** — the `bassIsRoot`=false halves (**57 / 23**) independently match the
re-baselined gate. `characterise_bir_false.py` reproduces that BIR=false half (57/23, Default 57).
Since Stage 2.2-ii (Rider 1) it takes `--corpus-dir` and reads BOTH `.ours.json` and
`.music21.json` from the validated per-preset dir — `--ours-dir` is a deprecated,
unvalidated alias.)

If a gate causes BIR=false regressions in a non-Baroque preset, the correct fix is:
1. A tighter **structural entry condition** that excludes the problematic chord type
   regardless of preset (preferred — e.g. an extension guard blocks augmented+seventh
   chords in all styles), OR
2. A **preset-specific threshold override** that leaves the Baroque-tuned value unchanged.

Never widen a Baroque-tuned threshold to cover a non-Baroque edge case.

**Preset scoring caps — corrected 2026-06-10:** `maxTotalInversionContextBonus` is
**never set on any code path** — both presets inherit the 2.0 default, and the cap is
currently non-binding (the four inversion bonuses sum to 1.85 Baroque/default, 0.75
Jazz). The formerly documented "Baroque=2.5 / Jazz=0.6" values were aspirational and
never implemented. Jazz's inversion behavior comes from its **reduced individual
inversion bonuses** (0.20/0.20/0.15/0.20 in `batch_analyze.cpp`), not the cap. Full
story in `docs/scoring_model.md` §4 (note below the "Other terms" table).

## Scoring model — `docs/scoring_model.md` (MANDATORY for scoring sessions)

**Read `docs/scoring_model.md` at the start of any session that touches scoring
logic in `chordanalyzer.cpp`** — this includes adding or modifying templates,
bonuses, guards, gates, score matrices, or post-scoring passes.

**★ THE SAME FORM, FOR THE PRODUCTION INFERENCE LAYER (user-ruled 2026-08-11; the ruling record is
`cowork_rulings_2026_08_11_fourteenth_stop.md`, Ruling 64).** **Read the joint estimator's section of
`ARCHITECTURE.md` — its standing rules and the factorization contract that section delegates to — at
the start of any session that touches the joint estimator's behaviour.** *Why:* the
never-work-from-memory rule's founding instance is measured evidence that routing a session to a
specification on demand fails under load — a session reasoned about note collection from two
neighbouring documents without opening the layer specification and reported the position as
ambiguous, where the specification states it explicitly and twice. Phase 3's sessions live in this
specification, so the risk concentrates exactly where the record is least able to absorb it. *The
excluded alternatives are recorded at the ruling:* an unconditional read, which spends capacity —
this arc's measured scarcest resource — on every session the condition excludes; and declining, which
leaves the failed route as the only route.

The document is the authoritative reference for how the scoring pipeline works,
why each term exists, and what invariants must not be broken. Violating these
invariants without reading the doc first has caused multiple failed attempts
(B1 leading-tone ambiguity, B2 ×4, B3 rotation-selector bypass).

**Sync rule — mandatory:** Any commit that adds or modifies a template, bonus,
guard, gate, or other scoring term in `chordanalyzer.cpp` **must** include a
corresponding update to `docs/scoring_model.md` in the same commit. The two
must never drift apart. Specifically:

- Adding a template: update the Templates section (§2), increment the template
  count in the array-size comment, add the guard description if applicable
- Adding or changing a bonus/gate: update the relevant §4 or §6 entry
- Adding a new constraint or dead end: add it to §8

**Staleness check:** The template count in `docs/scoring_model.md` §2 must
always match the `array<TemplateDef, N>` declaration in `chordanalyzer.cpp`.
If they differ, the doc is stale — update it before proceeding.

**Template additions — the `kTemplateCount` model (since `a236a0ff21`):** All
template-related array extents (the `analyzeChord` template array, the three score
matrices, `kMasks` in `harmonicfunctionlayer.cpp`) are derived from
`analysis::kTemplateCount` in `chordanalyzer.h`, so the compiler enforces size
consistency — the old silent stack-buffer-overrun failure mode (a missed matrix
resize, caught in the B1 attempt 2026-06-04) is closed. (Since Stage 2.3
`18dc9e1829` the duplicate `kDiagTemplates` array is gone — `diagnoseChord` replays
the production pipeline, so there is **one** template array, not two.) Adding a
template means:
1. Bump `analysis::kTemplateCount` N→N+1 (auto-resizes the matrices and `kMasks`)
2. Add the new `TemplateDef` entry in `analyzeChord`
3. Add the interval bitmask to `kMasks` (a zero mask silently disables Gate R)

Remaining trap: bumping the constant **without** adding the `TemplateDef` entry
value-initializes a trailing all-zero template (silent) — always do both in the
same edit. The authoritative checklist is `docs/scoring_model.md` §9.

## Score corpora

For any task involving scores (validation, snapshot tests, manual QA,
LLM-triage, qualitative review), read `docs/score_inventory.md` first. It
maps every score location to its intended use and lists the do-not-touch
files. Companion references: `tools/REPRODUCIBILITY.md` (how to recreate
corpora) and the JSON registries (`tools/corpus_registry.json`,
`tools/extra_scores_registry.json`).

## Local patches — do not revert

The following changes have been made intentionally to fix bugs unrelated to the
composing module. Do **not** revert them, and do not let build scripts or
dependency updates overwrite them without explicit approval.

**★ THIS SECTION IS A CHECK'S INPUT (2026-08-03).** `tools/audit/local_patches_check.py` derives
its patch list from the `###` subsections below and their `**File:**` lines, and verifies each
patch is still present at HEAD — the silent failure a dependency update produces, which nothing
else here would catch. Two things follow for whoever edits this section. **(1) A new patch needs a
`###` subsection with a `**File:**` line**, and the check then STOPS until a presence marker for
it is added to the tool: a recorded patch that is not tested must never read as a clean run.
**(2) A patch upstream later fixes is RETIRED by one line in its own subsection**, in this form —
`**★ SUPERSEDED UPSTREAM (YYYY-MM-DD):** <what upstream did>; upstream <commit-or-release>.` The
marking must name the upstream commit or release that supersedes the patch; a marking without one
is a STOP, so a patch cannot be retired by assertion. A retired patch is reported RETIRED and its
marker is no longer tested.

### Windows Snap fix — `muse` submodule (applied 2026-05-14)

**File:** `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`  
**Function:** `calculateWindowSize()`

Two lines were removed that set `ptMinTrackSize` equal to the full monitor work
area inside the `WM_GETMINMAXINFO` handler. This told Windows the minimum
allowed window size was the entire screen, which prevented Windows Snap from
resizing a maximised MuseScore window into a chosen snap zone (the window
stayed full-screen and lost its title-bar controls).

The fix: `ptMaxSize` and `ptMaxPosition` are kept (they correctly constrain the
maximised position); `ptMinTrackSize` is intentionally left unset.

Upstream issue: musescore/MuseScore#25823 (related cousins: #21344, #16794).  
Introduced by upstream commit `4ad218709` (5 Aug 2025).  
**Do not restore the `ptMinTrackSize` lines.**

### MusicXML declared-mode import fix (Stage 4a, applied 2026-06-14)

**File:** `src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp`  
**Function:** `addKey()` (the `KeySig`-dedup guard, ~line 5976)

The dedup guarded the `KeySig` creation on **fifths only**:
`if (oldkey != key.key() || key.custom() || key.isAtonal())`. At score start the
prevailing key defaults to `{C, KeyMode::UNKNOWN}` (`KeyList::key()` →
`setConcertKey(Key::C)`), so a **0-fifths** key signature carrying an explicit
`<mode>` (e.g. `<fifths>0</fifths><mode>minor</mode>`) matched the prevailing fifths,
the whole `KeySig` was dropped, and the declared `<mode>` went with it →
`KeyMode::UNKNOWN` downstream. Export *does* write `<mode>`
(`exportmusicxml.cpp:2473`), so this broke export/import round-trip of `<mode>` and,
in our pipeline, dropped the declared-mode anchor on ~79 zero-signature Bach stems
(`cc_key_emission_headroom_dossier.md` — `declaredModeOrdinal=-1`). The maintainers'
own `// TODO only if different custom key ?` flags the dedup as known-incomplete.

The fix: fetch the prevailing `KeySigEvent` (not just the `Key` fifths) and add an
`oldKeySig.mode() != key.mode()` term to the guard, so a mode-bearing key at matching
fifths is retained. A key matching the prevailing one in **both** fifths and mode (and
not custom/atonal) still produces **no** `KeySig`, so plain mode-less C-major scores are
unaffected. Verified isolated to empty-signature scores (exactly 79 zero-sig `.ours.json`
changed, 0 non-empty-signature stems); BIR gate byte-identical on all three presets
(Baroque 57 / Jazz 23 / Default 57); key-inference S2 −378 (Default). Round-trip of
`bwv254` (0-fifths `<mode>minor</mode>`) now preserves `<mode>`.

Upstream issue: musescore/MuseScore#9444. The buggy fifths-only dedup is upstream-unchanged
code (the `// TODO only if different custom key ?` line). Stage-4a discrete step; the
graded-prior / KeyArea work that softens the resolver's −7 declared-mode wall is a later
Stage-4 step (see `cc_stage4a_mode_import_report.md`).
**Do not revert; do not let dependency updates overwrite without approval.**

**★ DISTRIBUTION CONSTRAINT (user, 2026-06-15): FORK-LOCAL ONLY — NEVER merge upstream / to the
MuseScore community.** This patch (`cfc7eb5e39`) is fine to have in the **central repo = the user's
fork** (`origin` = `slimvince/MuseScore`) and may be pushed there, but it must **NEVER** be pushed or
merged to `upstream` (`musescore/MuseScore`) or otherwise contributed to the MuseScore community.
`upstream` push is disabled in this repo; keep it so. Any future push/PR/merge that would carry
`cfc7eb5e39` (or its content) toward `musescore/MuseScore` is a HARD STOP — surface, do not proceed.
(The #9444 reference above is the upstream *bug report*; it does NOT authorize contributing THIS patch.)

### Chord-symbol parser "sussus" fix — `ParsedChord::parse` (applied 2026-04-15; recorded 2026-08-02)

**File:** `src/engraving/dom/chordlist.cpp`
**Function:** `ParsedChord::parse()` (~line 990)
**Commit:** `b1ba7464`

One line removed: the redundant case-sensitive `tok1 = u"sus"` assignment beside the correct
lowercase `tok1L = u"sus"` path. The redundant assignment was the underlying cause of the
"sussus" double-rendering defect in chord-symbol display. Found unrecorded by the phase-1f
enumeration (`OPEN_ITEMS.md` OI-273) and recorded here under the MuseScore-dependency rule
(`ARCHITECTURE.md` §3.3, D-229: every edit to MuseScore's own code recorded with a per-instance
distribution disposition).

**★ DISTRIBUTION DISPOSITION (user-ratified 2026-08-02): UPSTREAMABLE** — a general parser
defect fix with no fork-specific content; contributing it to `musescore/MuseScore` is permitted
and consistent with the §1.2 contribution intent (contrast the MusicXML mode-import patch above,
which stays fork-local). **Do not revert; do not let dependency updates overwrite without
approval.** Register entries **D-315** — the fix itself, that it was made and is live in this fork
— and **D-316**, its distribution disposition. *(D-315 homed here 2026-08-08: until then it was
recorded ONLY in `STATUS_ARCHIVE.md`, which is reference-only and not among the session-start
reads, while the record that a live edit to MuseScore's own code exists is exactly what this section
is for. Its own provenance said this section carried two subsections and not this one — true when
written, and closed by the subsection above, which was added the same day it was found. The archive
is untouched.)*

## VS Code extension — bash command rules (MANDATORY, every session)

The Claude Code VS Code extension (v2.1.141+) has a 15-second stall detector. If the
API stream is silent for >15 seconds — which happens any time a bash command is running
— the extension marks the session `idle` and hands control back to the user, even though
CC is still running. This causes silent disconnects that are hard to detect.

**Two rules that apply to every bash command, no exceptions:**

**Rule 1 — Always append `; echo "exit:$?"` to any command that may return non-zero.**
A non-zero exit code also triggers an immediate idle transition. The echo always returns 0.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Rule 2 — Never let a single bash call produce large output.**
Large output (thousands of lines) takes >15 seconds to process and triggers the stall
detector. Redirect to a file and read separately.
- BAD:  `./pipeline_snapshot_tests.exe`  (many failing tests = large output)
- GOOD: `./pipeline_snapshot_tests.exe > /tmp/snap_out.txt 2>&1; echo "exit:$?"`
         then `head -50 /tmp/snap_out.txt`
- BAD:  `batch_analyze <score> --dump-regions notation`
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

Build commands via `Start-Process` are isolated from these rules (exit code not exposed).

## Conventions

- American English throughout — "analyzer" not "analyser"
- No confirmation prompts between analyse → implement → build → test steps
- Commit only when explicitly asked
- never hallucinate or guess, verified facts only - better ask first if unsure.
- **NEVER WORK FROM MEMORY INSTEAD OF DOCUMENTED FACTS (user-directed, 2026-07-28; binds Cowork
  and CC equally).** No assertion, design, decision, dispatch or report may rest on recalled or
  inferred content when a documented source exists. Open the primary source and cite it
  (file:line). This is STRONGER than the no-guessing rule above and is not satisfied by being
  right: correct memory is indistinguishable from incorrect memory without checking, so "I was
  probably right" is not a defence — and the check is what surfaces the parts the memory did not
  contain. **Where the primary source is:** how a layer *should* work → **that layer's section in
  `ARCHITECTURE.md`** (the primary place such decisions are recorded — not exclusively, but
  first); a ruling → the ratified `cowork_*` decision document and its dated amendments (and, once
  it exists, the decisions register, OI-208); current state and baselines → `STATUS.md` and
  `CLAUDE.md` gate block (A); an open issue → the `OPEN_ITEMS.md` INDEX and its detail file;
  what the code does → the code. **Founding instance:** on 2026-07-28 Cowork reasoned about note
  collection from `ARCHITECTURE.md` §2.15 and the factorization document without opening the
  Layer-2 specification, and reported the position as ambiguous; the specification states it
  explicitly and twice (`ARCHITECTURE.md:1045-1053`, slice identity IS the eligible sounding-note
  set with releases as boundaries; `:3134-3141`, actual sounding notes ranked the STRONGEST
  evidence), which turned an "ambiguous spec, narrowed in implementation" reading into a
  documented decision the implementation contradicts. The primary source was more specific than
  the memory of it, which is the general case, not the exception.
- **No self-invented labels, abbreviations, numbering schemes, or jargon** — in documents,
  register rows, commit messages, and conversation alike. Use the name a thing already has
  in the repository; if it has none, describe it in plain words. (User-directed, repeatedly;
  recorded 2026-07-11.)
- **THE WRITING STANDARDS LIVE IN `cowork_design_doc_template.md` — read it before writing any
  specification, design document, decision surface, or anything presented to the user.** Two
  standards: **predicates must be qualified** (user, 2026-06-24 — every two-place word names its
  argument; the mechanical check is to force the word to be followed by the thing it points at,
  and a phrase the prose cannot supply is a hole), and **defined terms, plain vocabulary, no
  shorthand** (user, 2026-07-02 — a terms table with nothing used before its row; no invented
  synonyms; no insider compression, a jargon handle only after its rule has been stated; inherited
  prose audited as hard as new). That file also carries the fourteen-section document structure,
  the status-banner convention, and the implementation/test locator rule. It is the ONE home for
  writing standards; the entry below sharpens its rule 5 and does not replace it (#6).
- **MUSIC-THEORY WORDS ARE RESERVED FOR THEIR MUSIC-THEORY MEANING (user-directed, 2026-07-28;
  sharpens `cowork_design_doc_template.md` rule 5 of 2026-07-02, whose own examples were *key*,
  *bar* and *measure* — that rule said one declared sense per document; this makes the choice
  mechanical rather than per-document. Binds Cowork and CC equally.)** Any term that coincides even slightly with music theory is used
  ONLY in its musical sense. This is a music-analysis system: an ambiguous domain vocabulary makes
  every document harder to read and every specification easier to misapply. The generalization of
  the "instrument" case — that word means a violin, not a measurement script; say *measurement
  tool*, *check*, *script*, or *generator*. Where a collision already exists in the tree it is NOT
  renamed unilaterally: the pass is scoped and ratified as its own work item (some names carry
  correspondence to the published research the design is grounded in, #1/#2, so the rename is a
  decision surface, not a sweep). But **no NEW collision is introduced**, and **anything written
  for the user avoids the collided sense entirely.** Known collisions in current use, as the
  starting inventory: *instrument*, *score* (numerical vs musical), *key* (map key vs tonality),
  *measure* (to measure vs the bar), *stem* (filename stem vs note stem), *note* (annotation vs
  pitch event), *mode* (operating mode vs musical mode), *tie* (score tie-break vs notated tie),
  *dynamic* (dynamic programming vs dynamics), *register* (issue register vs pitch register),
  *beat* (to defeat vs the pulse), *scale* (to scale vs the collection), *figure* (a reported
  figure vs figuration), *interval* (confidence interval vs pitch interval), *resolution* (of
  detail vs of a dissonance), *sharpen* (to refine vs to raise a pitch), *flat* (a flat profile vs
  the accidental), *root* (root cause vs chord root), *part* (a portion vs a musical part), *rest*
  (the remainder vs the silence).
  **THE DISAMBIGUATION CONVENTION (user-directed, 2026-07-28) — one rule covering every case:
  THE BARE WORD ALWAYS CARRIES THE MUSICAL MEANING; EVERY NON-MUSICAL USE IS EXPLICITLY
  QUALIFIED.** Bare *score* is the music — the numerical sense is always *candidate score* /
  *content score* / *total score*, never bare. Bare *key* is tonality — the other is *map key* /
  *cache key* / *lookup key*. Bare *measure* (noun) is the bar — the gauging sense is
  *measurement* (the verb "to measure" is unambiguous and stays). Bare *note* is a pitch event —
  the other is a *remark* / *annotation* / *entry*. Bare *mode* is the musical mode — the other is
  *operating mode*. Bare *register* is pitch register — the other is *the open-items register*, in
  full. Bare *tie* is the notated tie — the other is *tie-break*, always compound. Bare *dynamics*
  is the musical marking — the other is *dynamic programming*, always in full. Likewise *stem*
  (note stem; the other is *file name* / *piece identifier*), *interval* (pitch; the other is
  *uncertainty range*), *figure* (figuration; the other is *number* / *value*), *resolution*
  (harmonic; the other is *level of detail*), *scale* (the collection; the other is *grows with*),
  *beat* (the pulse; never a verb for "outperformed"), *root* (chord root; the other is
  *underlying cause*), *rest* (the silence; the other is *remainder*), *part* (musical part; the
  other is *portion* / *component*), *flat* (the accidental; the other is *featureless*),
  *instrument* (a violin; the other is *measurement tool* / *check* / *script*). This makes the
  eventual cleanup a BOUNDED job rather than a rename: much of the tree already complies by
  accident (`totalScore`, `content score`, `segmentContentScore` are qualified already), so only
  the BARE uses in a non-musical sense need touching.
  **★ WHAT HAPPENS TO A NAME BORROWED FROM THE PUBLISHED RESEARCH, AND IN WHAT ORDER THE CLEANUP
  RUNS (user-ruled 2026-08-09; the ruling record is `cowork_rulings_2026_08_09_fifth_stop.md`,
  Ruling 30).** The block above says the existing tree is not renamed unilaterally and that the
  pass is a decision surface rather than a sweep. It does not say what a session does with a term
  that carries correspondence to the research the design is grounded in, and it does not fix the
  order — both are settled here. **A RESEARCH-TIED NAME IS NOT RENAMED (#1/#2), AND IS GOVERNED BY
  TWO TIERS.** *(i)* At the **INTRODUCTION SITE** — where the public research is actually
  discussed, which is expected to be one or very few places — the collision is EXPLAINED and our
  decided synonym STATED; the term standing there with that statement is conformant. *(ii)* **Every
  subsequent use** of the research term outside our own vocabulary carries a **compact inline
  annotation referencing the research**; such a use is conformant if and only if it is annotated,
  and an **unannotated repeat use is a flag**. *Why the second tier is the load-bearing one:* a
  rule stated as *research terms are not renamed* and nothing else reads as a licence to leave them
  bare, which reproduces the ambiguity the whole convention exists against — the reader who meets
  the term at its fiftieth use never meets the introduction site. **AND THE ORDER OF THE CLEANUP IS
  FIXED: NO TREE-WIDE RENAME.** The derived inventory comes first; the user then rules **per-word
  batches**, **governing surfaces first** (`CLAUDE.md`, `ARCHITECTURE.md`, the signed
  specifications), with **code identifiers** and **research-tied names** each a named LATER
  decision. *Why the order rather than a sweep:* it is what makes the pass a scoped decision
  surface, which is the thing the block above already ruled it must be; a single tree-wide pass
  would take every one of those decisions silently and at once. The tracking row is
  `OPEN_ITEMS.md` OI-229, which stays open because the cleanup itself is not done, and the derived
  inventory and its measured limits are at `tools/audit/reserved_word_scanner.json` — no count or
  word list is restated here (#17f, D-431).

- **EVERY DESIGN DECISION CARRIES ITS DEFENSE AT ITS HOME (user-directed, 2026-08-01, at the
  decisions-register ratification review).** Wherever a design decision is recorded — the owning
  layer's specification in `ARCHITECTURE.md` first — the record states WHY the decision was made:
  the published research or algorithm adopted (#1/#2), the measurement that decided it, or the
  constraint that forced it. Every design decision must be defendable, and its defense documented
  where the decision lives. This generalizes `ARCHITECTURE.md` §17.2 (every non-obvious scoring
  weight or threshold must explain its musical reasoning) from scoring values to design decisions
  as a class. The decisions register (`DECISIONS.md`) points at the defense; where a decision's
  derivation is not in the record, the register says **"derivation not recorded"** — the gap is
  stated, never filled in retroactively from memory (a defense written after the fact without a
  source is invention, and the never-work-from-memory rule forbids it). Founding instances of the
  gap: the decode segment cap's value (4), the legacy 16-beats-back/8-forward window, the
  boundary-tick-belongs-to-the-segment-it-starts convention — each recorded with no derivation.

- **ISSUE-EXHAUSTION AND SPECIFICATION COMPLETION BEFORE ANY FIX DESIGN (user-directed,
  2026-08-02; sharpens #8, which forbade inference-problem coding before layer completion — this
  forbids fix DESIGN before knowledge completion).** Three phases, strictly ordered. **Phase 1 —
  the specifications are made COMPLETE and TRUE:** every recorded decision is written into its
  owning specification (the homing acts), with its defense, so that conformance is thereafter
  measured against the specifications themselves — the decisions register remains the status
  ledger (supersession, shelving, the same-commit rule), never the conformance reference; and the
  specification text is corrected wherever it states something false at HEAD (the doc-sync debt),
  because a specification cannot be the compliance standard while it misdescribes the code.
  **★ HOW FAR THE DOC-SYNC HALF REACHES INTO A DOCUMENT'S ACCOUNT OF ITSELF (user-ruled 2026-08-04;
  D-639).** The sentence above says *"states something false at HEAD"*, and a document states things
  about ITSELF as well as about the analysis — a status banner, an as-built marker, a code anchor, a
  missing supersession note. **The doc-sync half reaches a document's account of itself ONLY WHERE
  THAT ACCOUNT CHANGES HOW THE DOCUMENT'S ANALYSIS CONTENT IS READ.** The ruling's own three worked
  examples, which are the test rather than illustrations of it: an **as-built banner over a dormant
  mechanism — IN**; a **missing supersession note on a superseded plan — IN**; a **stale anchor or a
  formatting artifact — OUT**. *Why the line falls there:* the clause states its own reason two lines
  up — *because a specification cannot be the compliance standard while it misdescribes the code* —
  so what the half exists to catch is a document that would make a reader believe something false
  about the system; a coordinate that has drifted misleads nobody about the analysis, and D-307
  already forbids citing code by line number in the first place. **THE FALLBACK, RULED WITH THE TEST
  AND NOT LEFT TO A LATER SESSION:** if the test needs judgment on the first rows it meets, that is
  the *"stable enough to be cited"* failure repeating — a criterion that reads as mechanical and
  resolves case by case — and the fallback is **option (1A): the doc-sync half reaches only the
  account of the ANALYSIS.** A session that finds itself arguing a case applies the fallback and says
  so; it does not stretch the test to reach a verdict. *(First application, 2026-08-04, at
  `OPEN_ITEMS.md` OI-332: three documents, one matching each worked example, decided without reaching
  the fallback — the enumeration and the per-document reason are generated at
  `tools/audit/decisions/true_half_reach.json` and no verdict is restated here, #17f, D-431.)*
  **★ AND IT BEARS ON A GATE VERDICT — A POINTER, NOT A RULING (the question is open at
  `OPEN_ITEMS.md` OI-336).** THIS rule decides what PHASE 1 OWES; the non-gating declaration above
  decides what A STAGE WAITS ON. They are different tests with different subjects and neither
  overrides the other. Applying this one at OI-332 surfaced a question about the OTHER: whether that
  row's apparatus classification survives reading the whole of D-438's line rather than its first
  half. **That is not settled here and nothing above settles it** — a non-gating verdict is derived
  from a cut and never hand-added, so it is the user's. Stated and left at OI-336.
  **★ WHEN PHASE 1 IS COMPLETE — THE FINISH LINE IS CUT BY D-438'S TEST, AND THE APPARATUS RESIDUE
  DOES NOT GATE THE COMPLETION (user-ruled 2026-08-11; the ruling record is
  `cowork_rulings_2026_08_11_fifteenth_stop.md`, Ruling 65).** The clause above says WHAT phase 1
  requires; it does not say which of those requirements the completion WAITS ON, and until this
  ruling the derived finish line waited on all of them. **The finish line is cut by D-438's own
  test — does the item's subject bear on the analysis, on the analysis's inputs, or on a measurement
  tool something depends on — and PHASE 1 COMPLETES WHEN THE INFERENCE-BEARING OBLIGATIONS ARE
  DISCHARGED. The apparatus residue does not gate phase 1's completion.** **THE #19 EXCEPTION STANDS
  INTACT AND IS ENCODED IN THE CUT RATHER THAN REMEMBERED:** an establishment obligation gates
  whatever its subject, because trust in a measurement is trust in the analysis. **THE CUT IS DERIVED
  AND REGENERATED, NEVER HAND-CLASSIFIED** — a gating verdict comes from a cut and is never
  hand-added (**D-436**; the recorded lesson is `OPEN_ITEMS.md` OI-336) — and **the pre-cut
  population is preserved beside the post-cut one (#12)**. **THE FALSIFICATION TEST THE RULING IS
  OWED, RUN ON EVERY REGENERATION: if the cut places into the apparatus class any item or row the
  record elsewhere calls inference-bearing, THE CUT IS WRONG AND HALTS** — without it a declaration
  cannot be told apart from wishful filing. *What it changes, mechanically:* it applies to the finish
  line the non-gating declaration the open-items register section already carries — the one surface
  the record had never applied it to. That declaration governs what a STAGE waits on, and the block
  immediately above says in terms that what PHASE 1 OWES is a different test with a different
  subject; so the finish line's items carried their gate separately, and one of them was explicitly
  the class whose place had not been decided. **That class is now decided.** *Why, in the user's own
  recorded ground:* the documentation work was genuinely valuable and its marginal value has fallen —
  the findings that bear on the objective came from reading specification against code and from
  probes, not from apparatus repair. **What it does NOT move:** the three phases and their strict
  order, #8's three-clause gate, the #19 exception, and D-639 immediately above, which still decides
  what the doc-sync half REACHES. It adds nothing to the finish line — it changes how the finish line
  is CUT. No item, verdict or count is restated here (#17f, **D-431**); the cut is derived at
  `tools/audit/phase1_finish_line.json`.
  **Phase 2 — issue-finding is EXHAUSTED with measured coverage:** the remaining audit partitions
  and the blind second pass with its seeded error rate, plus the enumerated discovery channels —
  **enumerated at `cowork_oi200_perspective_inventory.md` §4, which is the ONE home for that list
  (user-ratified 2026-08-03, D-439); that section's own scope ruling states which of its channels
  this clause reaches, and this clause lists none of them itself (#6)** —
  each search reporting its detection power, ending in the bounded trust statement — every
  channel enumerated, every miss rate measured, every finding rowed. **Phase 3 — ONE prioritized
  fix plan over the complete list** — where each fix lives (its proper layer), what it groups
  with (its family), in what order, and what refits it forces — and only then does design begin.
  Rationale: #3/#5/#13 generalized from one defect family to the whole system, and the product is
  unshipped, so carrying known defects while knowledge completes costs no user anything.
  **★ QUALIFICATION — PHASE 3 WAITS ON THE PHASE-2 ITEMS THAT COULD FIND ANOTHER MEMBER OF THE
  FAMILY BEING DESIGNED FOR, NOT ON ALL OF PHASE 2 (user-ruled 2026-08-03).** For a given family
  design, the phase-2 items it waits on are those whose SEARCH SPACE could contain a statement,
  measurement or code fact about the thing that family is about. For the struck-versus-sounding
  family (`OPEN_ITEMS.md` OI-215, OI-226, OI-227, OI-228, OI-243, OI-244, OI-246, OI-277) that
  question is: **could this item's search space contain a fact about (a) what the decoder or the
  emission READS — struck versus sounding tones, note counting, pitch representation — or (b) how
  candidates are ADMITTED?** Where an item's scope does not settle it, it GATES: the default on
  doubt is to keep waiting. *Why the qualification:* the rule above was ratified so that a family
  is KNOWN before it is designed for — the standing one-fix-per-family rule of 2026-07-28 is what
  it protects — and an item that cannot touch what the model reads or how candidates are admitted
  cannot change what the family is; making the design wait on it buys no protection and spends the
  time the fix plan is owed. **NARROWING THE GATE DOES NOT OPEN IT:** the qualification authorizes
  no fix, no design and no inference change, and phase 1 is not complete. **The partition is a
  PREDICTION and is recorded as one, before the items it classifies run** — the criterion verbatim,
  the per-item verdict with its reason, the per-item check filled in as each item runs, and the
  STOP: **a NON-GATING item that yields a family member falsifies the partition, and the gate
  widens.** It lives at `tools/audit/phase3_gate_partition.json` (generated by
  `tools/audit/gen_phase3_gate_partition.py`, which locates every source quote in the file it
  cites); no verdict or count is restated here (#17f, D-431). **An establishment obligation (#19)
  always gates, whatever its subject** — see the open-items register section's non-gating
  declaration, where that clause is stated once and is not repeated here (#6).
  **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT IS RATIFIED (user, 2026-08-03;
  D-439).** `cowork_oi200_perspective_inventory.md` §4 is the ONE home for the enumerated discovery
  channels, and that section carries the user's ruling of which of its channels this clause reaches:
  channel 9 (history mining) is IN; channels 4 and 8 are ALREADY REACHED by what this clause names
  elsewhere (channel 4 is an obligation carried by the other probes and not a search of its own;
  channel 8 is the audit passes and the blind second pass, which the phase-2 clause above names in
  the words immediately preceding its channel half); channel 10 is NOT a discovery channel on its
  own account, its catalog-feeding role noted
  rather than dropped. **What the ratification did NOT do:** the inventory's §6 program is NOT
  adopted, `OPEN_ITEMS.md` OI-200 is not pulled forward, that document's own §9 request stays open
  and untaken, no probe/fix/design/inference change is authorized, and phase 1 is not complete.
  The reading surface the ruling was taken from is
  `ratification_surfaces/cowork_perspective_inventory_ratification.md`; the gap it closed was
  tracked at `OPEN_ITEMS.md` OI-298.
  *(Former text, preserved under #12 — recorded 2026-08-03 at phase 1u, one wave before the
  ratification, when this clause still listed six subjects of its own:* "★ NOTE ON PHASE 2 — THE
  ENUMERATION THIS CLAUSE RELIES ON IS NOT RATIFIED (recorded 2026-08-03; the clause itself is
  unchanged). Phase 2 above names *"the enumerated discovery channels"* and then lists six
  subjects. The only place in the record where those channels are actually enumerated is
  `cowork_oi200_perspective_inventory.md`, whose own banner reads *"STATUS: DRAFT for discussion"*
  and whose §9 records that its one requested decision has not been taken. So a user-directed rule
  leans on an unratified draft, and the six subjects under-name what that draft holds. The gap is
  stated here, not filled: the six subjects bind on this clause's own authority and nothing else is
  imported from the draft; the phase-3 gate partition therefore states each verdict against the
  SUBJECT this clause names, using the draft's channel numbers as locators only. The ratification
  is owed, its reading surface is
  `ratification_surfaces/cowork_perspective_inventory_ratification.md`, and until the user rules,
  no claim about phase 2's coverage rests on the draft's structure. Tracked at `OPEN_ITEMS.md`
  OI-298 — an apparatus row under the non-gating declaration above, so it blocks nothing and stays
  owed."*)*

- **MAKE IT WORK FIRST; COMPROMISE ON PERFORMANCE ONLY IF PERFORMANCE PROVES TO BE A PROBLEM
  (user-directed, 2026-07-28, at the analysis-cost session).** Getting the inference right comes
  first. Runtime speed is traded against it only once slowness has actually turned out to be a
  problem. This does not demote runtime speed, it **sequences** it: work that makes the *same*
  computation faster costs nothing on any principle axis and must therefore be exhausted BEFORE
  anything that trades precision for speed — which puts the effort control (`ARCHITECTURE.md` §2.16)
  and the analysis-extent question **last**, not first. The rule was stated to correct a misreading of
  an earlier remark that "implementation efficiency is not very relevant": that remark meant BUILD
  effort, not runtime.

- **CANDIDATE ADMISSION IS COMPLETION, NOT REFINEMENT — so #8 permits fixing it now (user-ruled
  2026-07-28, at the OI-199 pass-2 session).** The rule that decides which chord classes the joint
  decoder will even consider is a piece that was never finished, not a refinement of something already
  built. #8 — no inference-problem-driven coding until every method sits in its correct layer — therefore
  does NOT block fixing it. The classification is recorded here because it is a ruling about what #8
  permits, and #8 lives here; what the admission rule actually is, and that it has no specified form, is
  in the estimator's own specification (`ARCHITECTURE.md`, the joint estimator's standing rules, (c)) and
  at `OPEN_ITEMS.md` OI-226. The licence is narrow: it permits deriving the correct admission rule from
  the model, NOT loosening a threshold until orchestral scores pass, which is per-case tuning and DT-2
  forbids it.

- **ONE FIX IS DESIGNED ONCE OVER THE WHOLE ENUMERATED FAMILY, NEVER PER SYMPTOM (user-ruled
  2026-07-28, at the OI-199 pass-2 session).** When several observed faults turn out to share a cause,
  the remedy is designed once for all of them together, at the layer that owns the cause; fixing
  whichever fault is currently visible, on its own, is the patch-per-symptom error that #6 (one path per
  concern) and #7 (layer adherence) exist to prevent. A fix is therefore **deferred by design** until
  the family is enumerated. The instance that produced the rule: the empty-decode cliff turned out to
  have a sibling at the opposite end of the density spectrum (`OPEN_ITEMS.md` OI-227) and an
  emission-side twin (OI-228), neither visible from the first symptom (OI-215).

- **THE WHOLE DECISION SURFACE IS DELIVERED AS USER-VISIBLE TEXT BEFORE ANY CHOICE QUESTION (user
  mandate 2026-07-05; homed here 2026-08-02 from `cowork_handoff.md`, `OPEN_ITEMS.md` OI-266).**
  Never present the user with options before the entire situation has been explained in a message the
  user has actually seen. The decision surface — what is being decided, the background, what each
  option means, the risks both ways, and the recommendation with its reason — is delivered as
  user-visible text FIRST, via the verbatim message channel or as the turn's final response. For a
  **consequential** decision (a ratification, an adoption, a retirement, a checkpoint ruling) the
  choice question goes in a SEPARATE, LATER turn: the user reads first, then is asked. **A decision
  answered blind is voidable** — re-present the surface and re-confirm. *Why:* the mechanism is
  stated with the rule — prose written between tool calls is summarized rather than shown verbatim,
  so an explanation placed "just before" a question widget may never reach the user and the question
  arrives blind. Its first application is on the record: the 2026-07-05 verdict-14 and 2.2c
  ratifications were re-presented and re-confirmed.

- **WORKING-TREE FILES ARE READ WITH THE FILE TOOLS; SHELL ACCESS IS LIMITED TO GIT OBJECT QUERIES BY
  EXPLICIT HASH (user mandate 2026-06-21; homed here 2026-08-02 from `cowork_handoff.md`,
  `OPEN_ITEMS.md` OI-266).** Local file content, existence, line counts and searches always go
  through the file tools (Read / Grep / Glob), never through shell text utilities — no `cat`, `wc`,
  `grep`, `sed`, `head`, `tail`, `git status` or `git diff` on working-tree files. Shell access is
  permitted **only** for read-only git OBJECT queries named by an explicit commit hash taken from a
  session's own commit report (`git show <sha>:path`, `git show --stat <sha>`, `git cat-file`,
  `git diff <shaA> <shaB>`). A branch tip or index read — `git rev-parse HEAD`, `git status`,
  `git log` — is never trusted for what is current. A `bad object` or missing-object error is a
  **staleness signal: surface it, never guess around it.** *Why:* measured failure — a stale mount
  made the shell path return wrong content and raise a false corruption alarm while the file tools
  read the live disk correctly; the git-object exception survives because content-addressed reads are
  self-verifying, erroring loudly rather than returning silently-wrong content. **Scope, as the
  record states it:** this is a standing rule for the PLANNING side — it is stated under the heading
  "COWORK MUST NOT HALLUCINATE OR ASSUME — VERIFY AT SOURCE", and the role-separation rule beside it
  spells out the same restriction as one of the things "Cowork MAY" do. It is homed here because
  `CLAUDE.md` is where this project's shared standing rules live, not because its scope widens: the
  build, test and measurement commands `BUILD_AND_TEST.md` and the sections above mandate are
  unaffected, and nothing in the record extends the file-tools restriction to them.
  **★ THE RULE COVERS EVERY READ MECHANISM AND EVERY DIALECT (recorded 2026-08-08 on the user's
  direction, at the third measured instance family).** The restriction is on WHAT is read —
  working-tree content through a shell — not on which utility spells the read. A PowerShell
  `Get-Content` / `Select-String` / `Get-ChildItem` aimed at a repository path (the OI-345
  family, CC, 2026-08-07) and a `python -c "open(...)"` in the Cowork sandbox (Cowork,
  2026-08-07/08, self-reported at the user's challenge after repeated use for row statuses,
  guard summaries and artifact fields) are the same violation as `cat`. **THE GUARD WATCHES
  BOTH SPELLINGS WHERE THE HOOK RUNS, AND THE COWORK SANDBOX IS NOT THAT PLACE (corrected
  2026-08-09 on the user's ruling; the former wording, preserved under #12, was *"No guard
  watches either surface"*).** The PowerShell reading family came inside the guard at the
  2026-08-07/08 dialect widening, and interpreter code — `python -c`, `perl -e`, and a heredoc
  body fed to one — at the 2026-08-08 guard-family act, to that act's own stated ceiling:
  interpreter code whose path is COMPUTED carries no literal for the policy to see and is
  admitted. **The correction is a NARROWING and not a discharge**, because the clause's point
  is unchanged: the guard is armed as a hook in THIS project directory, it says nothing about
  any other execution surface, and **its silence on an unwatched surface is not compliance
  (#19)**. The sandbox instance carries the
  rule's own founding hazard undiminished: sandbox reads go through the same mount whose
  measured stale-content failure created this rule, so a sandbox read can be stale in exactly
  the way the rule exists to prevent. The Cowork instance's reads were re-verified through the
  file tools on 2026-08-08 and all reproduced — recorded so the outcome is not mistaken for
  the defense; "it happened to be right" is the argument the never-work-from-memory rule
  already rejects.

- **INVESTIGATE BY DEFAULT; NEVER ASK THE USER WHETHER TO INVESTIGATE OR PROCEED (user mandate
  2026-06-14; homed here 2026-08-02 from `cowork_handoff.md`, `OPEN_ITEMS.md` OI-266).** Wherever a
  step could be investigated or measured BEFORE it is committed to, it is measured first — and that
  is not put to the user as a choice. When such a fork is reached, the read-only investigation or
  measurement is written and run directly, byte-identical where possible. *Why:* the user's standing
  answer to "investigate, or go in some direction" is always *investigate*, so asking spends a turn
  to learn nothing; this is the never-guess rule's logical end — gather the cheap evidence before any
  commitment — and it operationalizes principle #5 (investigate when facts may be scarce).

## The self-check after every coding exercise (user-directed, 2026-07-11)

After EVERY coding exercise — code, scripts, instruments, and document edits alike —
and BEFORE reporting the work done: take a step back, re-read the actual diff of every
touched file, and check it against the guiding principles, the conventions, the gate and
threshold policies in this file, and the known problem types in `DEFECT_TYPES.md`. Any
violation found is surfaced immediately (its own `OPEN_ITEMS.md` row if it cannot be
corrected on the spot within the session's authorized scope), never silently shipped.
The check is of the work actually on disk, not of the intention — read the diff, not the
memory of writing it. This applies to CC sessions and Cowork sessions alike.
