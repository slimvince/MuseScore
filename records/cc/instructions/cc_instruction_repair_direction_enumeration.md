# CC dispatch — enumerate every document correction this arc made TOWARD the code, and whether the code's correctness was ever assessed

> **Status: ACTIVE DISPATCH, written 2026-08-13 (Cowork), at a verified STOP.** The scoring-model
> pass completed; Cowork verified its three commits at the objects by explicit hash, no forbidden
> path, OI-45 and OI-183 flipped. Nothing is running.
>
> **★ WHY THIS RUNS, AND THE FAULT IS TIMING RATHER THAN DIRECTION (user, 2026-08-13).** A
> code-versus-documentation comparison is what the **audit step exists to do**. This arc performed
> those comparisons **during restructuring** — so the audit was run early, out of sequence, on an
> instrument not yet fit for it. **That is the fault, and it holds however carefully each act was
> done.** Direction is a second and smaller matter: the comparisons also moved the document toward
> the code every time, treating the code as the standard, and **whether the code was right was
> never asked** — but even had it been asked, the acts would still have been premature.
> **A specification grounded in published research (#1, #2) or carrying a ratified decision (#14)
> may therefore have been displaced by a description of what the implementation happens to do.**
> The audit method surface already names that class — *the specification is correct, the code is
> wrong* — and none of this arc's comparisons went through it.
>
> **★ TWO EARLIER FRAMINGS ARE WITHDRAWN, so nothing here rests on them.** That #10's *"in sync with
> code"* makes the code the reference — **it does not**; *in sync* is symmetric and states a
> required agreement, not which side moves. And that *at HEAD* means *against the code* — **it does
> not**; HEAD is the current commit of everything. Both were the writing side's glosses, and the
> one-directionality that does exist enters at **D-231's truth half**, where the specification is
> the grammatical object of the repair verb.
>
> **★ THIS DISPATCH ENUMERATES. IT CORRECTS NOTHING.** Deciding what is correct is the user's, and
> repairing in the same act would repeat the error in the opposite direction.
>
> **★ AMENDED BEFORE DISPATCH — the model sharpened after this file was drafted, and the change is
> the point of the enumeration rather than a detail of it (user, 2026-08-13).**
> **RESTRUCTURING IS NOT CORRECTING.** The current phase's output is documentation that is
> **internally consistent, findable, one home per concern** — an instrument fit to audit with. It
> may be internally perfect and still wrong about the world, and still wholly at odds with the
> code; **we do not know yet, and finding out is a later act.** **The audit that follows is an
> audit OF THE CODE, with the documentation as the instrument** — not an audit of documentation —
> and it is **two-directional**: any combination of code wrong, specification wrong, both wrong,
> both right differently, or something missing entirely.
> **So the test this enumeration turns on is: was the inconsistency between TWO DOCUMENTS —
> restructuring, and legitimate now — or between a document and something else the repository holds
> — a DELTA, which waits?** That cut is added as field 0 below and is answered first.
> **AND `HEAD` IS NOT THE CODE.** It is the current commit of everything — code, specification,
> tools, corpora, goldens — so *false at HEAD* is **direction-neutral**: it names a disagreement as
> of now and says nothing about which side is wrong. Where the implementation is meant, this
> dispatch says **the code**.
>
> **Read IN FULL, and read FIRST:** `cowork_spec_code_audit_adjudication_method.md`, whose seven
> gap classes and three adjudication standards are the vocabulary this enumeration uses;
> `CLAUDE.md` principles #1, #2, #14 and #10 as amended.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_repair_direction_enumeration.md`. Acts
> dated from the clock; **no positional count anywhere**; cite rulings by number, not by date.
>
> **★ All standing rules as adopted.** D-253 in every dialect; git object queries by explicit hash
> are the admitted route and the working-tree is read with the file tools. NO TRANSCRIBED VALUES
> (D-431). Hold-don't-guess. **NO EDIT OF ANY KIND to a document, a comment, a row, a register entry
> or the code. No `src/`, no golden, no corpus, no measurement, no design, no flip, no row, no
> discard.** D-231 and #8 stand. **Phase 1's completion statement is not written, not drafted and
> not partially written.** One commit at the end carrying the enumeration; `origin` only.

## 0a. THE POPULATION, AND HOW IT IS DERIVED

**Every commit of this arc that changed what a document says about the system**, where a document
means anything read as specification or record: `docs/`, `ARCHITECTURE.md`, `CLAUDE.md`,
`BUILD_AND_TEST.md`, and **comments under `src/`**, which are documentation living in code and were
corrected on the same reasoning.

**Derived from git**, not from any list — including this dispatch's own account. **The arc's
starting point is established at the record, not assumed**; if it cannot be established, STOP and
report what bound is available.

## 0b. WHAT IS RECORDED PER ITEM

Five fields, each answered at an object and none inferred. **Field 0 is answered FIRST, because it
decides whether the act should have happened in this phase at all.**

0. **RESTRUCTURING OR DELTA.** Was the inconsistency **between two documents** — which is
   restructuring and belongs to the current phase — or between a document and **the code, a tool, a
   corpus, a golden, or a measurement**, which is a DELTA and waits? *Record which two objects
   disagreed, by name. An item may be BOTH — a statement false against another document and against
   the code — and where it is, say so and split it, because only one half was legitimate.*
1. **DIRECTION.** Did the edit move the **document toward the other object**, the **other object
   toward the document**, or neither — a measurement re-stamp, a filing act, a banner?
2. **WAS THE CODE'S CORRECTNESS ASSESSED?** Not *was the code read* — every one of these read the
   code. **Did anything ask whether what the code does is RIGHT?** Quote the assessment if there is
   one; **record its absence plainly if there is not**, which is expected to be the common answer
   and is not a fault of the session that made the edit.
3. **WHAT THE FORMER WORDING CARRIED.** Every correction preserved it under #12, so this is
   recoverable. Does it carry, or cite, a **ratified decision** (#14), a **register entry**, or a
   **published-research citation** (#1, #2)? Quote what it carried.
4. **THE GAP CLASS**, from the method surface's seven — including *the specification is correct,
   the code is wrong*, *the specification is silent*, and *both correct about different arms*.
   **Assign a class only where the evidence settles it; otherwise record NOT ADJUDICABLE**, which
   that surface makes a first-class outcome.

## 0c. THE PREMISE LEDGER (#17a)

**FACT — verified by Cowork at the objects.** This arc's commits and their changed paths, by
explicit hash, across the batches Cowork verified.

**ASSUMPTION — checked before the act resting on it; a refutation is a STOP.**

- **A1.** Every former wording is recoverable, from the preserved text in the file or from the
  commit object. *Check per item. **If any is unrecoverable, that is a STOP and a loss** — say
  which.*
- **A2.** Field 2 is answered from the **dispatch and the batch record**, not from the diff. A diff
  cannot show whether a question was asked. *Check: quote the instruction or the report where an
  assessment appears; where neither carries one, record absence.*
- **A3.** Field 4 assigns a class **only where the evidence settles it.** *Check: no item is
  classed by resemblance. NOT ADJUDICABLE is the correct answer wherever the three adjudication
  standards — a ratified decision, a public algorithm or published research, or the music itself —
  do not decide.*
- **A4.** **The enumeration is published WHOLE** (D-671). *Check: if capacity runs short, publish
  the members covered **by name** and state the remainder as untouched; do not publish a partial
  set as though complete.*

## 0d. THE TASKS

**Task 1 — the enumeration.** Derive the population, answer the four fields per item, and publish it
as a generated artifact under `tools/audit/` with its own reproduce check. **Report separately and
prominently: every item where field 3 shows a ratified decision or a research citation on the
document side AND field 2 shows no assessment of the code.** That set is the exposure this dispatch
exists to size.

**Task 2 — one Conventions line in `CLAUDE.md`, on the user's direction.** Written verbatim as
below; the wording is the writing side's and the user may change any of it, but **nothing is
paraphrased or improved in the writing.** Former text is untouched — this is an addition, not a
correction.

> **`HEAD` IS THE CURRENT COMMIT OF EVERYTHING — CODE, SPECIFICATION, TOOLS, CORPORA AND GOLDENS —
> AND IS NEVER USED TO MEAN THE IMPLEMENTATION (user-directed, 2026-08-13).** Where the
> implementation is meant, say **the code** or **the implementation**; where the current state of
> the repository is meant, say HEAD and mean that. **The phrase *false at HEAD* is therefore
> DIRECTION-NEUTRAL: it names a disagreement as of now and says nothing about which side is
> wrong.** This is the same family as the reserved-word rule and the no-self-invented-labels rule —
> a term with an established precise meaning is used only in that meaning, and where the narrower
> thing is meant the narrower thing is named. *Why:* measured — a session glossed *at HEAD* as
> *against the code*, built an argument about D-231's truth half on the gloss, and it took three
> exchanges to unwind; a later session reading the doc-sync clause the same way makes the same
> error against the same sentence.

**Task 3 — the close.** One `STATUS.md` pointer entry per task, the close appended to
`cowork_away_returns.md`. Report at the objects with commit hashes.

## 0e. WHAT IS DELIBERATELY NOT DONE

**Nothing is corrected, in either direction.** No document is moved back, no code is changed, no row
is flipped, opened or discarded, no register entry is written. **No verdict is offered on what is
correct** — that is the user's, on the enumeration. The remaining ratified acts are not started.
OI-179 stays OPEN and GATES.

## 0f. STOP RULES

Halt with a STOP in `cowork_away_returns.md` if: a former wording is unrecoverable; the arc's
starting point cannot be established at the record; an item cannot be classed and NOT ADJUDICABLE
would misdescribe it; or the enumeration cannot be published whole and the covered members cannot be
named.

---

*Provenance: Cowork, 2026-08-13, on the user's ruling that phase 1's truth half has been running in
one direction only and that the specification may have been demoted to a description of the code.
The error is Cowork's: it wrote the dispatches that instructed these corrections and never once
instructed an assessment of the code. Self-check run before release (D-434).*
