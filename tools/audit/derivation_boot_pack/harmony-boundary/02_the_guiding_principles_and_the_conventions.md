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
   *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 11 line(s), `preserved-former-wording`, opening "**★ WIDENED HERE 2026-08-04 ON THE USER'S RULING; THIS IS NO…"*
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
    *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 14 line(s), `preserved-former-wording`, opening "**★ #10 GAINED ITS SECOND HALF HERE, AND THIS IS THE RULE'S …"*
    **★ WHAT IT SUPERSEDES — A POINTER, NEVER A COPY (#6).** R3's clause that an apparatus
    finding's row is **mandatory** no longer holds for a finding the worth test above discards.
    **R3 is otherwise untouched** — it still decides whether a finding is surfaced or rowed, and
    its own #19 sentence is reinforced rather than weakened. R3's home is `cowork_audit_protocol.md`
    (register entry **D-641**), where the supersession is recorded at the clause itself and is not
    restated here.
    *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 8 line(s), `defense-and-declined-alternatives`, opening "**★ THE THREE ALTERNATIVES DECLINED, recorded because an exc…"*
    *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 5 line(s), `defense-and-declined-alternatives`, opening "**★ THE COSTS THE USER ACCEPTED, stated before the ruling an…"*
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
    Class A reaches a causal claim only where that claim is checkable, which is this
    principle's recorded ground. A claim about the conditions under which a session ran — its
    boot, its context, what reached it — is not checkable from outside that session, and is
    therefore declared, not established.
19. **Unestablished instruments are FORBIDDEN (Class B).** An instrument, corpus, gate, or
    recorded figure is trusted only after being *positively established* (oracle cross-check,
    derivation of what the measurement unit actually measures, reproduce-check) — never
    because it is merely unfalsified.
    The objects of this principle are the four it names and no others — a measurement tool, a
    corpus, a gate, a recorded figure — and each is an inspectable, re-runnable artifact,
    because each of the three establishment methods named here requires one. A session, a
    person or a conversation is never the object of a Class B demand.
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
    **★ AND THE CONTACT ROUTE CLOSED BY ANSWER, NOT BY SILENCE — WITH THE ANSWER THAT THE ONE
    LOCALLY HELD CANDIDATE CANNOT SUPPLY THE QUANTITY EITHER (user-ruled 2026-08-11).** Clause (a)
    provides for the laboratory contact closing by silence after a reasonable wait. **It closed by
    answer.** The laboratory states one annotator, named, PhD in musicology, who annotated the
    harmonic spines; weekly review with the corpus author and **no independent annotation**; and no
    duplicate or superseded readings. **So BCMH joins the class this principle already names for the
    Mozart-sonatas corpus — consensus-built, so agreement cannot be recovered after the fact** — and
    inter-annotator agreement inside it is not unpublished but nonexistent.
    **The consequence for this principle, stated at the width the D-474 block above uses.** What is
    absent is a **published** per-axis agreement value, and that absence is unchanged. What is **not**
    absent is computability: the block above already records two corpora whose duplicate or dual
    annotations exist and were never computed, and no corpus's standing is restated here (#6). **So
    the ceiling is not obtainable from inside any corpus of OUR GATE REPERTOIRE** — BCMH and the
    Mozart sonatas are consensus-built and can never yield it, and ABC has no overlap by design —
    **while within the wider enumerated set it is computable by us, off-repertoire or of unchecked
    domain.** OI-179's design surface — a Cowork reading surface, **not ratified** — classes TAVERN's
    duplicates as within-corpus, true inter-annotator and off-repertoire, and Dilemmadata's domain as
    still to be checked at the data; **neither computable route is established (#19)**, and neither
    has been checked at its data. **That is why OI-179's on-repertoire leg is a comparison BETWEEN
    annotation traditions and therefore a PROXY, and why the off-repertoire legs bracket it rather
    than replace it.** The choice this leaves — the right quantity on the wrong music against a proxy
    quantity on the right music — is a **phase-2 design decision and is not settled here.**
    *NOT claimed:* that no corpus anywhere could supply it; that either computable route will yield a
    usable value; or that the domain caveats have been discharged.
    **★ THAT PARAGRAPH REPLACED A NARROWER ONE, AND THE FORMER WORDING STANDS IN PLACE (#12;
    user-ruled 2026-08-11 on a surface carrying three alternatives with their principled costs — the
    ruling is KEEP THE WIDTH AND RESTATE WHAT IS ACTUALLY ABSENT; the defect it corrects is tracked at
    `OPEN_ITEMS.md` OI-375).** **THE FORMER WORDING WAS:** "**The consequence for this principle: the
    ceiling is not obtainable from inside any single corpus in this repertoire**, which is why
    OI-179's measurement is a comparison BETWEEN annotation traditions. *NOT claimed:* that no corpus
    anywhere could supply it — the claim is about the enumerated set the D-474 block names, and a
    corpus outside that set is a finding rather than a contradiction." *Why it was replaced:* its
    load-bearing word's argument — *this repertoire* — was unnamed, and this record already uses that
    phrase at two widths that give the sentence opposite truth values; read at the wider width, the
    one the D-474 block earlier in this same principle uses of itself, it is refuted by that block's
    own enumerated set and argues away two within-corpus legs OI-179's design surface holds open as
    an undecided question. *The two declined alternatives, recorded because an excluded alternative
    is evidence about the choice:* **narrowing the sentence to our gate repertoire**, declined
    because it would place a narrow reading of *this repertoire* below the same phrase used at a wide
    width in the same principle, which is the ambiguity that produced the defect; and **striking the
    consequence sentence**,
    declined because a reader of #21 would then still infer the ceiling might come from citation,
    which is exactly what D-474 exists to prevent. *The errata limb of the contact was RE-ASKED
    2026-08-11 and AWAITS REPLY; clause (a)'s reasonable-wait clock runs from that date.*
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
    Every reported result carries its uncertainty. Where a condition of a result's production
    cannot be established at an inspectable object, that condition is DECLARED as a bound and
    the result stands with the bound attached. A declared bound discharges an establishment
    demand that has no inspectable object. It does not discharge one that has.

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
  what the code does → the code. 

  [A PASSAGE IS WITHHELD FROM THIS PACK FOR THIS SUBJECT.]

  
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
  source is invention, and the never-work-from-memory rule forbids it). 

  [A PASSAGE IS WITHHELD FROM THIS PACK FOR THIS SUBJECT.]

  
- **ISSUE-EXHAUSTION AND SPECIFICATION COMPLETION BEFORE ANY FIX DESIGN (user-directed,
  2026-08-02; sharpens #8, which forbade inference-problem coding before layer completion — this
  forbids fix DESIGN before knowledge completion).**
  **★ THE THREE-PHASE STRUCTURE BELOW IS SUPERSEDED AND ITS TRUTH HALF IS REPLACED (user-ruled
  2026-08-15; the ruling record is `cowork_rulings_2026_08_15_phase_definition_sitting.md`; the ruled
  definitions' ONE home is `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3 —
  a pointer, never a copy, #6).** The governing structure is now SIX PHASES — preparation → the pilot
  (on `docs/scoring_model.md`) → the framework → the detail specifications → measurement design → the
  audit — with the fix plan after the audit unchanged: #8's three-clause gate and the
  one-prioritized-fix-plan rule stand exactly as below. Every phase closes with a recorded
  retrospective (lessons of any kind, with evidence, routed to their homes; amendments only by the
  user's ratification). **The rule that replaces the truth half, stated here because it must bind
  even a session that reads nothing else: A DISAGREEMENT BETWEEN SPECIFICATION AND CODE IS EVIDENCE,
  RESERVED FOR THE AUDIT; NO DOCUMENT IS CORRECTED ON THE GROUND THAT THE CODE SAYS OTHERWISE.** The
  COMPLETE half survives as a property, not a program: the detail-specification phase derives
  specifications that are born complete — every decision in its owning specification, with its
  defense. **The former three-phase text below is PRESERVED IN PLACE (#12) and is no longer the
  governing structure.** Its embedded sub-rulings keep their own recorded standing and none is edited
  by this supersession: old phase 2's exhaustion duty (measured coverage, every channel enumerated,
  the bounded trust statement) is inherited by the audit phase; old phase 3 and its family-gate
  qualification are the unchanged fix-plan territory; a sub-ruling whose subject was the superseded
  truth half (D-639's reach test) loses its subject with it, its record untouched and its register
  standing settled at the register's own discharge, not here. The abbreviation HEAD in the preserved
  text below is read under the ruled vocabulary: the current commit of everything, never the code
  alone.
  Three phases, strictly ordered. **Phase 1 —
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
