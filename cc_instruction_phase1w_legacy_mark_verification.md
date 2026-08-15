# CC dispatch — phase 1w (STAGE 2): verify the LEGACY-marked set against live reachability

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork).** Stage 2 of the user's sequencing ruling —
> *facts before action* — and the first gathering act, placed first because its output can **redirect
> where the family fix has to live**, not merely inform.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1w_legacy_mark_verification.md`.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).**
>
> **★ QUEUE.** Runs after `cc_instruction_phase1t_restatement_and_pruning.md`, whose recording rule
> governs how this wave's findings are written.
>
> **★ THIS IS A GATHERING WAVE.** No `src/`, no goldens, no `tools/corpus/`, no `tools/robust_stop/`,
> no behaviour change, no fix, no design, no inference change. It reads and it measures.

## 0. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork in the session that wrote this dispatch:**

- **F1.** OI-289 states the test this row calls for: *"for each marked entry, is its subject reachable
  on either production surface at HEAD, and does any ruling carry its principle across to the live
  design?"* — `open_items/OI-289.md:49-51`.
- **F2.** The set size is **derived from the data, and no figure in the record matches it**. Three
  recorded figures disagree with each other and with the derived count — the row names them and says
  *"a reader should re-derive rather than quote"* — `open_items/OI-289.md:43-49`.
- **F3.** Reachability on the notation arm is decided by **a runtime flag whose default is `true`**
  and by four branch points, **not by compilation**, so "dormant" is a statement about a default with
  an enumerated false-negative path: an explicit flag flip, `batch_analyze` without
  `--joint-inference`, the test suites, and the declared non-production uncached path. **Any per-entry
  verdict has to say which of those it means** — `open_items/OI-289.md:53-58`.
- **F4.** The flag's default is set at `composingconfiguration.cpp:178`, and
  `notationcomposingbridge.cpp:729-737` returns the record view whenever it is true, with the legacy
  paths below that return — read at the code.
- **F5.** Two marks are already established wrong: **D-329** (its principle carried across to the live
  family design at the OI-275 ruling) and **D-311** (its subject produced `chordsymbolformatter.cpp`,
  which the record arm runs at `notationimplodebridge.cpp:1170`). D-311's mark was removed on that
  established evidence and is **the only per-entry change made without this verification**.
- **F6.** The marking convention itself is user-ratified (`CLAUDE.md` decisions-register rule (f)) and
  is **not** in question — what was withdrawn is the unchecked clause that rode along with it
  (`open_items/OI-289.md:60-65`).

**ASSUMPTION — checked before the act it licenses:**

- **A1.** That the marker is generated text, one wording emitted from the register generator for every
  marked entry, so the set is derivable from the data rather than by searching prose. → **Task 1.1**.

## 1. Task 1 — Derive the set

**1.1** Establish A1 at the generator, then **derive the marked set from the backbone data**. **Do not
quote any recorded figure** (F2) — three exist, they disagree, and sizing this work from one of them
under-counts it. Publish the derived set and its count as a generated artifact; every later figure in
this wave cites that artifact.

**1.2** Report the discrepancy between the derived count and each recorded figure, and **where each
recorded figure lives**, so the stale ones can be corrected as a separate act. Do not correct them
here — that is action on surfaces, and it belongs after the gathering.

## 2. Task 2 — Define the test before applying it

The test is F1's, and F3 makes it two questions per entry, not one. **Write the test down before
running it**, in the artifact:

- **(a) Reachability.** Is the entry's subject reachable on **either** production surface at HEAD? And
  because F3/F4 make "dormant" a claim about a **default** rather than about compilation, **each
  verdict must name which sense it means** — unreachable at any setting, unreachable only while the
  flag holds its default, reachable via one of the four enumerated false-negative paths, or reachable
  on a production path outright.
- **(b) Transfer.** Does any ruling carry the decision's **principle** across to the live design, as
  the OI-275 ruling did for D-329? A mark that is correct about the subject can still be wrong about
  the effect, and F5 is the precedent.

**Register a prediction before measuring** (#17b): how many entries you expect to fail each half, and
on what grounds. State it in the artifact. A refuted band is a result, not a failure.

## 3. Task 3 — Verify every entry

Apply the test to the whole derived set. Per entry record: the subject, the reachability verdict **in
the sense named at 2(a)**, the transfer verdict, the evidence cited to the object, and — where the
evidence does not settle it — **UNDETERMINED**, which is a permitted and expected value.

**Do not guess to fill a cell.** An UNDETERMINED with its reason is worth more than a verdict with
nothing behind it, and #19 is the whole point of this row.

**Where a verdict rests on a code path, cite the code**; where it rests on a ruling, cite the ruling.
A row or a register entry is a secondary source for both (D-431's premise clause).

## 4. Task 4 — Correct only what this wave establishes

A mark this wave **establishes** as wrong may be corrected, in the same act, on the D-311 precedent
(F5): a correction of a demonstrated error is not a sweep. Report the count and enumerate them.

**Everything else stands.** An UNDETERMINED entry keeps its mark and is reported. Do **not** re-mark
the set on a general conclusion — that would be a second sweep, which is the thing this row exists to
undo.

**If the failure rate is high enough to put the convention itself in question, say so and STOP there.**
F6 makes the convention the user's, and a session may not withdraw it. Report the rate and the ground
for the concern.

## 5. Task 5 — Report what this bears on

State plainly, from the results:

- **whether any wrong mark's subject is code the family design may have to live in** — this is why the
  wave is sequenced first, and it is the finding the design needs before it is drafted;
- whether OI-288's class hypothesis holds — that the P4 finding bears on a whole class of these
  entries rather than on D-311 alone;
- what remains UNDETERMINED and what would settle it.

Flip or update **OI-289** with the derived count, the verdicts, and the corrections made.

## 6. Task 6 — Guards, notes, close

Run every guard at the committed tree; **derive the list from what exists** and report rather than
substitute if one this dispatch names is absent. Read each output separately. Verify what is being
committed through `tools/audit/changed_paths.py`. Run `tools/audit/process_check.py` over **this
dispatch** and report what it finds against Cowork.

`STATUS.md` gains one POINTER entry, written to the standard phase 1t installs.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's remedy and OI-300 (the other two
gating establishments, stage 2), OI-274's body-tense half, OI-288 half (a), OI-290's document-side
remedy, OI-296's sweep, OI-299, OI-301, the `CLAUDE.md` mechanism-coverage measurement (stage 2), the
owed reads (stage 2), and every stage-4 action.

## 7. Accepted outcomes

**A high UNDETERMINED rate is a result, not a shortfall** — it would mean the marks were made on
grounds the record cannot reconstruct, which is exactly what #19 says about a swept population.
**A refuted prediction is a result.** **Stopping at Task 4's last clause is a success** if the failure
rate puts the convention in question — that is the user's to rule, not a session's.

## 8. Self-check (D-434) — run by Cowork before release

- **#17(a).** Six facts, each cited to the object — the code facts at the code, the row's own
  statements at the row. One assumption, checked before the derivation rests on it.
- **Sequencing.** This wave is pure gathering. Task 4's narrow licence to correct is action on facts
  established **in the same act**, which is what "acting on facts" permits; everything wider waits.
- **Principles.** #19 — the whole wave. #17(b) — a prediction registered before measuring. #12 —
  nothing deleted, UNDETERMINED preserved rather than resolved. #13 — the convention-in-question case
  is a STOP. #7 — no amendment to any specification here; this wave reads.
- **D-431.** No bare quantity anywhere; F2 explicitly forbids quoting a recorded figure and orders
  re-derivation, and every later figure cites the artifact this wave generates.
