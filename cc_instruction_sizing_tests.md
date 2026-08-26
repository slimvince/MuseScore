# CC DISPATCH — THE SIZING UNIT'S TESTS (a) AND (b), AND THE SIZING RECORD

*Written by the Cowork writing side, 2026-08-26, against tip
`c4a2563515fa6e6a46c06f036b06677b713a9852`. Executes Rulings 1 and 2 of
`cowork_rulings_2026_08_26_sizing_tests_sitting.md`, which un-held the tests batch of Ruling 3 of
`cowork_rulings_2026_08_24_sizing_pilot_sitting.md`. This dispatch performs NO ratification and
orders NO register entry.*

---

## 0. What this batch is, and the one thing that makes it delicate

The sizing unit of the pilot produced one file. Two tests were ordered over it and then held, because
that file's deriving session booted with the uncut standing instruction file in its context and its
blinding failed. The hold is now lifted on the merits of the two tests taken separately: one of them
judges the FORM of a statement, which the contamination plausibly does not reach, and the other yields
a harvest of pre-existing facts whose soundness does not depend on the session having been blind.

**The delicacy is that both tests produce something that must NOT be used, alongside something that
must.** Getting the labels onto the right products, at the point they are produced, is as much the job
as running the tests.

**You grade. You neither refute nor confirm.** No recommendation on the method, on the sizing unit, or
on what should happen next appears anywhere in your output.

---

## Task 0 — start state and landings

**(a) The tip.** Read `.git/refs/heads/master` with the file tool. It must read
`c4a2563515fa6e6a46c06f036b06677b713a9852`. **If it does not, STOP and report.** Name the side you
measured (ref, worktree or blob) wherever you state a hash, here and everywhere below.

**(b) Do NOT run `git status`** (D-253). Run `python tools/audit/changed_paths.py` and record the
population. Do not commit any of the standing untracked population.

**(c) Land, in one commit:** `cowork_rulings_2026_08_26_sizing_tests_sitting.md` (untracked at the
root, the ruling record this dispatch executes, written under the standing clause that a record lands
at the next dispatch's Task 0); this dispatch; and `cowork_handoff.md`, which stands **tracked-modified
against the tip** — the previous batch declared it at its §1(c) and correctly left it, and it is this
batch's to land. Then regenerate the evidence-pin membership with
`python tools/audit/gen_evidence_pin_membership.py`.

**(d) The session-start read comes AFTER Task 1(a). See the reading-order departure below.**

---

## Task 1 — the reading order, which is a ruled departure and is stated in terms

**(a) Read `cowork_blind_derivation_scoring_model_2026_08_24.md` WHOLE, FIRST, before you take your
session-start read.**

This follows the precedent of Ruling 2 of `cowork_rulings_2026_08_24_comparison_design_sitting.md`,
which put the blind output before the session-start read so the grader forms its understanding of what
the session claimed before another frame exists to map it onto — generous mis-mapping being the known
failure of frame-first grading. **The read SET is unchanged; only its ORDER is.**

**The ground differs from the precedent's and is stated so you do not mis-apply it.** That unit had a
withheld oracle inside `CLAUDE.md`. **This unit has none** — its withheld family is ruled EMPTY and it
is not held out (Ruling 1 of the sizing-pilot sitting; re-measured at 0 identities, 0 documents,
0 passages by the previous batch). The anchoring risk here is different: `CLAUDE.md` carries an entire
section on this unit's own subject document — *"Scoring model — `docs/scoring_model.md` (MANDATORY for
scoring sessions)"*, relayed as lines 1276–1329 from
`cowork_rulings_2026_08_24_blinding_failure_sitting.md` and not re-measured by the writing side — and
reading it first would frame your view of statements before you have seen them.

**(b) Verify the file is the one this dispatch means, before you read further than its banner.**

- Its banner must read *DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED*.
- Its size must be **125,529 bytes** and its sha256 must be
  `4887a9ab4dd16494cd7799b18babbfede83e51a40e11205920f1137a84a9861b` — the receipt taken at the
  working-tree file on 2026-08-24 and committed byte-identical under Ruling 2 of the blinding-failure
  sitting. **Say which side you measured.**
- **If the banner, the size or the hash differs, STOP and report.**

**(c) Then take the session-start read** (#6): `CLAUDE.md`, `STATUS.md`, `DECISIONS.md` in full;
`BUILD_AND_TEST.md` conditional; rule (a)'s `gating_ids`.

---

## Task 2 — the sizing record, reported before either test

Locate the sizing record inside that file. **Do not assume it is at a section numbered §5** — §5 is the
brief's numbering, not necessarily the output's. Find it by its content and report where it sits.

Report each field it carries **against the ruled list at §5 of `cowork_blind_session_brief_scoring_model.md`**,
which is six bullets: time per statement and the number of statements; the share marked *open* and the
share the session would put to the user for a ruling; the share whose sixth field could not be written;
the share resting on a *measured* source class; the noise measurement — which pack files and which
fetched sources were consulted per statement, with a pack file consulted by no statement listed as
such; and the reading time before the first statement, separately from writing time.

**Report every share with its denominator. Report a missing measurement as missing.** The brief
instructed the session to report missing rather than reconstruct; if it reconstructed anything, say so.

**★ Label the whole record, at the point it appears in your reading file: NOT A BUDGET.** Its three
defects are named beside it, all three, every time it is presented:

1. the failed blinding of its deriving session;
2. **18 % input coverage** — the session's stop-on-meeting fired correctly at `05_the_ratified_design_intent.md`
   and it rested on 44 of 241 design-intent entries, 197 unread;
3. its own session's declaration that **the clock is a model session's generation time, not an
   analyst's hours**, and its per-statement value a batch mean reported as a shortfall.

**Do not draw a budget from it, do not annualise it, do not extrapolate it to any later unit, and do
not compare it to any estimate.**

---

## Task 3 — test (a), the record check

**(a) Identify the corpus of recorded dead ends first, and prove you found it.**

§6.4 of `cowork_specification_reconstruction_plan_successor_2026_08_21.md` and Ruling 8 of
`cowork_rulings_2026_08_21_successor_plan_sitting.md` govern this. **The writing side has NOT opened
the dead-end corpus and this dispatch therefore names no path for it — deliberately.** Locate it,
report exactly what you identified and where, and quote the text that establishes it as the
authoritative source.

**If you cannot identify a single authoritative source, STOP and report. Do not assemble one.**

**(b) Apply the admission test by hand**, per Ruling 8, to each dead end that bears on a statement. The
test, in the plan's own words: a recorded dead end may withdraw a derived statement **only if** it
passes the fact-gate's ruled test — *does the fact survive the implementation being thrown away?* — and
is **approach-level**. A prohibition on re-attempting a specific mechanism of the dormant scorer does
not pass. A fact about the music or the corpus does.

**(c) The two products, and their labels.**

**Product one — the withdrawal rate.** How many of the session's statements a passing dead end
withdraws, with its denominator.

> **★ LABEL IT `UNCITABLE` AT THE POINT IT APPEARS, IN THE SAME SENTENCE, WITH THE REASON NAMED: it is
> a measurement over statements produced by a session whose blinding failed.** Not in a footnote, not
> at the head of the file, not left to the handoff. Anyone who reads that number reads its bound in the
> same breath. This project has had a figure travel out of its bounds within three days, more than
> once; the label is the whole of this product's containment.

**Product two — the admitted facts.** Every fact admitted at (b), written **in the ledger's ruled entry
shape**.

**Find and quote that shape before you write a single entry.** It is ruled; it is not yours to design.
**If you cannot find it, STOP and report — do not invent an entry shape.**

> **These entries SEED the ledger. They are not admissions to it.** The empirical findings ledger is
> **not built**, and this batch does not build it, does not create it, and admits nothing to it. Each
> entry is re-checked at the ledger's own gate when the ledger is built.
>
> **Their bound, stated with them:** the facts themselves are pre-existing records about the music and
> the corpus and do not depend on the deriving session having been blind — but **which** dead ends came
> up for examination was driven by which statements they collided with, so the harvest carries a
> **COVERAGE** bound from the contamination. Say so where the entries appear.

---

## Task 4 — test (b), the format test

**(a) The sample: five statements.** It **must** include a **probabilistic factor form** and a
**conditional-independence premise**. The ground, from §6.1 of the successor plan: the predecessors'
five chosen kinds omitted the two dominant kinds in the production layer's ratified specification, so a
test over the tractable kinds alone would pass and leave the hard kind untested. This subject's content
supplies both. **If either kind is absent from the output, STOP and report** — do not substitute a
third tractable kind and do not proceed on four.

State how you chose the other three.

**(b) What is judged.** Whether the statement's **sixth field — what would falsify it** — is returnable
without interpretation.

For the behavioural half, §7 of the successor plan carries five sub-fields as **UNESTABLISHED input**:
the **ARM** (joint / legacy-live / legacy-dormant), a named **SITE**, the **OBSERVABLE** read, the
**DECISION RULE** over it, and the named **near-miss it is NOT falsified by**. The plan's own words:
*"the format test of §6.1 (b) is where they are tested, not assumed."* Judge each of the five
sub-fields separately per statement — this is the only test they get, and every framework-phase and
detail-phase statement will be written in this form.

For a statement that is a modelling premise rather than behavioural, field six falsifies **in the
residual**, because a premise has no code site to check. Judge it on that footing, not the behavioural
one.

A statement that cannot carry field six should be marked **unverifiable** by the session itself; report
whether it was.

**(c) ★ THE SEPARABILITY DETERMINATION — this is Ruling 2 of the record and it is not optional.**

The open question three records left undecided is whether (b) survives the contamination **on its own
ground** — form being judged, not content. This batch measures that instead of assuming it.

**For each of the five statements, state explicitly whether your form verdict rested on the statement's
content**, and how you established that it did or did not.

**The stop rule, in operational terms:** grade all five and record all five separability
determinations. **If ANY one of the five returns *cannot separate*, the format test delivers NO overall
verdict.** The five rows stand as data; the question *does (b) survive the contamination* returns
**NOT SETTLED**, with the count and the reasons. Do not average it, do not call it a partial pass, and
do not decide the question yourself.

---

## Task 5 — the reading file

One file delivers all of it: `ratification_surfaces/cowork_sizing_tests_reading.md`, following the
precedent of `ratification_surfaces/cowork_comparison_harmony_boundary_reading.md`.

It carries, in this order: the sizing record with its NOT A BUDGET label and three defects; test (a)'s
withdrawal rate with its UNCITABLE label; test (a)'s admitted facts in the ledger's ruled entry shape
with their COVERAGE bound; test (b)'s five rows with their sub-field judgements; and the five
separability determinations with the overall verdict or the words NOT SETTLED.

**Every row carries the statement's own words**, so the user can re-grade any row at the text.

**Default nothing.** A verdict you cannot defend in one sentence at the text is delivered **UNGRADED**,
with what you read.

**The file makes no recommendation** — not about the method, not about the sizing unit, not about the
next act.

---

## Task 6 — bounds that bind this batch

**No measurement of the analysis is built, designed, scoped or run.** These tests are TEXTUAL.

The three ruled annotated pairs — chorales 001 and 003 with their `analysis.txt` and
`analysis_BCMH.txt`, and the BWV 301 score (`tools/dcml/bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx`)
with *When in Rome* folder **134**'s `analysis.txt`, paired by content and never by number — **may be
OPENED and CITED where a statement's own text names them, and nothing is run over them.** They are
**exemplars, not a corpus**; a published reading is one human reading, never a specification.

Do not open the harmony-boundary blind output. Do not touch either pack, the generator, the manifest,
any withheld family, or either brief.

---

## Task 7 — report and commit

Write `cc_report_sizing_tests.md` at the root, then commit.

State separately: the Task 1(b) verification with the side measured; where the sizing record was found
and how; what you identified as the dead-end corpus and the text establishing it; where you found the
ledger's entry shape, quoted; the five sample statements and how the two required kinds were located;
the five separability determinations; the sweep with every red named and classified; and **every
departure and every instruction you could not obey.**

---

## §8 THE FENCE

Writes permitted at **exactly** these paths and nowhere else:

- `ratification_surfaces/cowork_sizing_tests_reading.md` — new
- `cc_report_sizing_tests.md` — new
- `STATUS.md` — one POINTER entry (OI-222 remedy; **D-431**: no count, no identity, no rendered value)
- `tools/audit/gen_status_batch_bound.py` — the **five** aiming constants and the appended
  `PREVIOUS_AIMINGS` row, under its named carve-out; the append is part of the act the carve-out names.
  **Write the `STATUS.md` entry BEFORE running `--apply`** — the previous batch established that the
  reverse order makes the tool's occurrence test find zero and STOP.
- the three Task 0(c) landings and `tools/audit/evidence_pin_membership.json`
- **any file a tool this dispatch orders you to run writes as its own output.** Name each in the report.

**Explicitly forbidden.** No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md` edit. **No register
entry** — see below. **No ledger built, created or admitted to.** No `src/` change, no test changed,
moved or run, no golden. Nothing under `tools/corpus/` or `tools/robust_stop/`. No open-items row
created, flipped or discarded. No finding number allocated. No other `.py` source edited. Do not cure
`apply_soft_discard.py --check` or `apply_residue_discard.py --check`; do not regenerate `[[OI-372]]`.

**Why no register entry, stated so it is not read as an oversight.** Ruling 1 of the record changes a
hold status, which is register business of the same kind as the phase-status change entered as D-680.
**That entry is OWED and is named here so it is not rediscovered** — it joins the five already owed
from the sixty-sixth handoff entry. It is not ordered here because the register cannot presently accept
a new entry without turning two guards red, and those two checks are mutually unsatisfiable with
register rule (c) from the first addition after 2026-08-17 onward. **Curing that is a decision act and
is not this batch's.**

**The sweep.** Run it as ruled. Three reds are standing and are not yours to cure: `[[OI-372]]`'s
guard, `apply_soft_discard.py --check`, `apply_residue_discard.py --check`. A staleness red caused by
this batch's own writes is cured under the standing sweep rule. **For any other red: if you cannot tell
whether it is a decision red or a regeneration red, treat it as a DECISION red and STOP.**

**★ AND THE STANDING CLAUSE.** **If obeying any instruction in this dispatch would require a write
outside this fence, STOP and report the conflict. Do not choose a route, do not widen the fence, and do
not substitute a weaker form of the instruction to stay inside it.** Two dispatches before last ordered
writes their own fences forbade; the previous one did not, and reported that it did not. Stopping and
reporting is the correct outcome, not a failed batch.
