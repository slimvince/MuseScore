# Rulings — the landing-return sitting, 2026-08-25 — THE TWO OWED REGENERATIONS RUN, AND ONE LANDED CITATION IS CORRECTED

> **STATUS: RULING RECORD.** Cowork, 2026-08-25 (the forty-fifth Cowork session, its fourteenth
> sitting). An interim carrier under the standing clause that a sitting record is written in the
> turn its ruling is given and lands in git at the next dispatch's Task 0.
>
> **Taken at branch tip `64d640317fd652d1192350f0eafe4ef83abca680`** — the method-voiding landing
> batch's second commit — **after that batch's return was verified at the objects by this session**,
> not taken from its report.
>
> **★ THIS RECORD ORDERS ONE DISPATCH** and decides nothing about the derivation method, the
> re-run, or the plan's phases. **It is hygiene and one correction.**

---

## 0. The return, verified at the objects

**Verified, not relayed.** Both commits exist as reported — **`2dfe0ba485f438817f60385b4f6ea9fc0e6e4432`**
carrying **exactly six** paths, then **`64d640317fd652d1192350f0eafe4ef83abca680`** carrying
**exactly four**, its parent the first. **All four landing files are byte-identical at the committed
objects** to the hashes this side measured before the dispatch was written. **`OI-376`'s INDEX row
splits into six cells and opens with the bare canonical `OPEN` token**, carries no apparatus claim,
no gating verdict, no finding number and no remedy; its detail file is 6,797 bytes. **The guard
summary at the tip reads `{run 75, passing 72, failing 3, not_run 4, historical_records 16}`** with
the three tools named.

**And the batch's one inference was checked rather than accepted.** Its claim that
`gen_evidence_pin_membership --check` was **already red at the tree as found** is well grounded: at
the old tip the committed artifact carries entries for `…_08_21`, `…_08_22`, `…_08_23` and
`…_08_24` and **none** for `…_08_25`, while all three 2026-08-25 ruling records were already sitting
in the tree. **The batch did not cause that red.**

**★ AND A1 WAS WRONG A THIRD TIME, BY THREE ENTRIES.** Measured: the old tip's handoff carried
**44** entry headings, the new commit's **48** — the fifty-seventh, fifty-eighth, fifty-ninth and
sixtieth all landed together, and the superseded-marker went onto the fifty-**sixth** heading, not
the fifty-ninth. **This side's own handoff had said entries 57–59 were uncommitted, and this side
then wrote "one new entry" into the dispatch anyway.** The rule that orders this MEASURED is what
made the error free; **the error is that the assertion keeps reappearing in prose beside the rule
that forbids it.** *Recorded here rather than in a report, because it is this side's and not CC's.*

## 1. The finding this session made, at the objects — A LANDED ROW CARRIES ONE WRONG CITATION

`OI-376`'s INDEX row withholds a gating verdict and justifies it with *"a verdict is derived from a
cut and never hand-added ([[OI-319]], [[OI-336]], **D-436**)"*.

**At `DECISIONS.md`, at the tip:**

> *"| D-436 | A mechanism is judged on three measured conditions — automatic, detection rate,
> false-positive rate — and a failing one is REPORTED, not automatically removed | LIVE |"*

> *"| D-438 | Open-items register rows whose subject is this project's own tracking and
> documentation apparatus gate nothing — but an establishment obligation always gates | LIVE |"*

**D-436 is the wrong number. D-438 is the decision that actually states the register's gating cut**
— and is the one [[OI-336]] itself turns on. **[[OI-319]] and [[OI-336]] are same-class and
defensible by analogy** and are not disturbed. **So this is a transposition, not a fabrication** —
but it sits on the **authoritative status surface**, pointing a later reader at a decision about
mechanism judging.

**Why it is corrected rather than left to stand under #12.** #12 protects a **ruled text** from
being rewritten by a later reader. **A cross-reference is not a ruled text; it is a pointer, and a
pointer that leads somewhere false makes the record state something untrue about itself (#10).**
**The correction is therefore made IN PLACE and is ANNOTATED where it is made**, so that nothing is
silently rewritten and a later reader sees both the corrected pointer and the fact that it was
corrected.

## 2. Ruling 1 — the two OWED regenerations run, and the citation is corrected, in ONE dispatch (Alternative A)

**Ruled.** One small correction dispatch runs now:

- **(a) `gen_nongating_apparatus_rows.py` is regenerated.** Its `--check` red is **caused by this
  project's own act** — A5 of the last dispatch was falsified, and correctly so: the row is indeed
  outside the tool's first cut and needed no authored verdict, **but the same artifact also
  publishes `gating_ids` over every open row, so adding ANY open row moves it by construction.** The
  artifact is **out of date, not wrong**, and regenerating it is the ordinary discharge.
- **(b) `gen_evidence_pin_membership.py` is regenerated.** Its red predates the batch (§0) and its
  cause is discharged: the three 2026-08-25 ruling records are now committed, so the derivation and
  the artifact can agree.
- **(c) The `OI-376` citation is corrected in place, D-436 → D-438, with an inline note recording
  that it was corrected and when.** Nothing else in the row changes.

**★ AND ONE THING THIS RULING SETTLES THAT THE LAST ONE PROMISED AS A SURFACE.** The method-voiding
record said the row's gating verdict would be **put to the user on its own surface**. **At the tool's
source that verdict is DERIVED FROM A CUT, not chosen** — the register's own discipline is that a
verdict is never hand-added. **So there is nothing to put.** Ruled instead: **the regeneration's
derived answer is ACCEPTED as it falls**, whatever it is, and the landing batch **reports** it.
**This side's expectation — that a row outside the first cut takes the gating side by the ruled
default — is a READING OF THE SOURCE, not a measurement**, and the regeneration is what will replace
it with one. **If the derived answer differs from that expectation, that is a finding and is
reported, NOT corrected by re-wording the row's subject cell** — re-wording a row to move a derived
verdict would be gaming the cut, and is forbidden here in terms.

**The alternatives declined, by their ratings.** **B** — regenerate only, leave the citation under
#12: declined, #12 protects rulings and not pointers, and the row would keep sending readers to the
wrong decision. **C** — correct the citation only: declined, it leaves three reds including one this
project caused, which is the state in which a later session cannot read the guard set as a signal.
**D** — defer all of it into the re-run's landing: declined, the re-run is the user's to open and its
duration is unknown; a red guard set held open across it is the state the record cannot cite, and
the argument that landed the records this morning applies with more force to a red we caused.

## 3. Ruling 2 — the dispatch's own defect is corrected on the WRITING SIDE, with no repository act

**Ruled, recorded rather than dispatched.** The last dispatch's §4 ordered `git status --porcelain
-uall`. **That command is refused by this repository's own `PreToolUse` guard, citing D-253**, which
names `tools/audit/changed_paths.py` as the sanctioned enumeration. **CC used the sanctioned tool and
obtained the enumeration in full, so nothing was lost** — but the wording would have recurred in
every future dispatch. **It is struck from this side's dispatch form from here on; no repository act
is owed and none is ordered.** *(This is the same error class as the citation of §1: a form recalled
rather than measured against the rule that governs it.)*

## 4. What is HELD, and what this sitting does NOT do

**HELD, unchanged from the method-voiding sitting:** the method ruling stands **VOIDED**; the
framework phase and the detail-specification phase do not open; the tests batch (a)+(b) stays held,
and whether **(b)** survives on its own ground is still not decided. **The empirical findings ledger
remains owed before the framework phase.**

**★ THE RE-RUN IS UNBLOCKED AND IS THE USER'S TO OPEN AT ANY TIME.** It does not wait on this
dispatch and this dispatch does not wait on it.

**Not done:** no session is booted by this side; no derivation, no comparison, no oracle opened; no
blind output read beyond its bounded receipt; **no pack, generator, manifest, withheld family, brief
or governing document is touched — `CLAUDE.md` above all**; **no register row is created, flipped,
closed or re-scoped**, and `OI-376`'s status cell is not altered; no finding number is allocated
(**and none exists — Ruling 9 opens no series**); [[OI-179]] stays OPEN and GATES; [[OI-372]] stands
as the standing red and is **not** touched; [[OI-374]] stands as found. **The three deferred
apparatus items stay deferred.** **No remedy for `OI-376`'s hazard is proposed, and the row stays a
finding.**

---

*Provenance: Cowork, 2026-08-25, the forty-fifth session's fourteenth sitting, at tip
`64d640317f`. The batch's return was verified at content-addressed git objects — both commits and
their path lists, the four landing blobs' hashes, the row's cell count and status token, the guard
summary, the evidence-pin artifact's record population, and the handoff's entry counts on both
sides. §1's finding was measured at `DECISIONS.md` at the tip and is quoted from it. The batch's one
inference was checked and stands. The user's word: "A".*
