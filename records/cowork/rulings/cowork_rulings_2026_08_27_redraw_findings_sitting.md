# Rulings — the redraw-findings sitting, 2026-08-27

> **STATUS: RULING RECORD.** Cowork, 2026-08-27, the fifty-second session, second sitting. An interim
> carrier under the standing clause that a sitting record is written in the turn its ruling is given
> and lands in git at the next dispatch's Task 0.
>
> **Taken at branch tip `93c154562083516ea41cf6d01bcb6ea6cf4eb859`, read by this side at
> `.git/refs/heads/master` with the file tool** — the ref side. No shell command was run against the
> repository by this side. No document ruled here is generated, so no generated-document commit clause
> is engaged.
>
> **★ THE SITTING IS CLOSED. It carries ONE ruling with four named settlements.** The object ruled on
> is `cowork_redraw_findings_surface_2026_08_27.md`, delivered with no question in its turn; the choice
> question was put in the following turn, in the ruled form. **The form was observed on both sides this
> time.**

---

## 0. What was put, and how it was answered

His words, verbatim: *"i have read it"*, and then, to the question: *"Agree with recommendation"*.

**The single-limb test was applied before this was recorded as ruled.** The recommendation reads
*"Alternative B, with findings two, three and four ratified as they stand"* and then names one
settlement for each of the four findings. It carries no conditional and no fork; the three rejected
alternatives are named on their face as rejected. An agreement admits of one reading only.

---

## 1. Ruling 1 — the unit form for strata 1 and 2 is corrected and those two strata alone are redrawn; findings two, three and four are ratified as they stand (Alternative B)

### 1.1 Stratum 1 — ruling records — corrected unit

**Ruled.** A *numbered ruling* is a fence-aware markdown heading whose text, after the leading `#`
characters and after stripping leading `*`, `_`, `★` and whitespace, matches **EITHER**
`^(Ruling|RULING)\s+\d+` **OR** `^\d+\s*[.)]\s+\**\s*(Ruling|RULING)\b`.

**The bare numbered limb `^\d+\s*[.)]\s` is VOID for this stratum.** It admitted every ordinary
numbered section heading.

**The ground, measured by the writing side at the objects before the surface was written.** Across
**22 of the 79 ruling records**, opened and counted with the file tools: **103 headings admitted by
the void form, of which 69 are actual rulings — 34, or 33%, were ordinary section headings.** The
corrected form is the test that separates them, and it was chosen by a criterion stated without
reference to any count: *does the heading say it is a ruling.*

**★ A CORRECTION OF RECORD TO THE DRAWING SIDE'S REPORT, AND IT MATTERS.** That report's table splits
the 25 drawn items **5 against 20 by which limb of the pattern fired**. That is not the same statement
as *20 are not rulings*: the records' house style is `## 1. Ruling 1 — …`, which begins with a digit
and therefore matches only the numbered limb **while being a ruling in full**. The report's own prose
says so; its table invites the wrong reading. **Stratum 1 was materially less damaged than the
headline suggested, and this ruling corrects it rather than inheriting it.**

**A record matching zero contributes ZERO and is reported as zero, never construed.** Measured by this
side: five of the 22 opened return zero, and they are **exactly the five the report names as
zero-returning across all 79** — two enumerations, one list.

### 1.2 Stratum 2 — decision surfaces — corrected unit

**Ruled.** A *numbered decision* is a fence-aware markdown heading whose stripped text matches
`^(Decision|DECISION)\s+\d+`, **and nothing else. The numbered limb is dropped entirely.**

**The ground, measured by the writing side.** Across **7 of the 35 listed surfaces**: **48 headings
admitted by the void form, of which 8 are actual `Decision <n>` headings — 17%.** All eight stand in
two files. **Five of the seven carry no numbered decision at all**, because a surface that argues one
decision has nothing to number; the three surfaces of the previous sitting are among them, and none
of their 22 admitted headings is the decision each carries. One of the seven,
`cowork_extent_decision_surface.md`, admitted nothing even under the void form, because it numbers its
sections `## §1`.

**A listed file matching zero contributes ZERO and is reported as zero.** Under the corrected form
this is expected to be common, and the list of zero-returning files is a deliverable, not a defect.

**★ NO EXPECTED COUNT IS DECLARED FOR EITHER STRATUM, AND THAT IS DELIBERATE.** Eight matches in seven
files licenses no estimate over thirty-five. **If the corrected count falls at or below the threshold
of 25, the stratum becomes a census under the standing rule and no uncertainty range is needed** —
that is a possibility, not a prediction, and nobody has measured it.

### 1.3 What is NOT redrawn

**Strata 3, 4, 5, 7 and 8 stand as drawn.** Their readings are ruled, their figures reproduce, and
redrawing them would spend a cycle to change nothing. Alternative C, which redraws everything, was put
and rejected on that ground. Alternative D, which drops strata 1 and 2 altogether, was rejected on the
ground Ruling 1 of the previous sitting already gave: those two are the project's governance records
and the frame is most likely to fail where the statement is a governing one.

### 1.4 Finding two — the bullets-only list-item reading — **RATIFIED as it stands**

A *markdown list item* is a **bullet** item — a line whose first non-whitespace character is `-`, `*`
or `+` followed by whitespace — at any nesting depth. Ordered items (`1.`, `1)`) are **excluded**.

**Declared with the ruling, and to be written on the faces of strata 3 and 5:** ordered items are
plainly list items, and the exclusion was fixed by a **STOP in the writing side's own dispatch** —
which forbade any `N` other than the confirmed 33 — rather than by a decision of the user's. It is
ratified now so that it is a ruling rather than an artifact of an instruction.

**The writing side did not verify the 33-against-38 figure, deliberately.** Verifying it means opening
`cowork_evidence_inventory.md`, and opening a file in order to decide how its items should be counted
is the sighted choice Ruling 1 of 2026-08-27 protects the sample against.

### 1.5 Finding three — line-ending normalisation for stratum 8 — **RATIFIED**

**Ruled: heading text is compared with line endings normalised — the carriage return stripped —
before two versions are compared.**

**The ground.** Relayed and unverifiable by this side without a shell: several member files changed
from CRLF to LF in their history, `ARCHITECTURE.md` at 26 commits. Without normalisation the single
commit at which a file's line endings change reads as **every heading in that file being deleted at
once**, and the stratum returns **610 events instead of 59**, 580 of them from `ARCHITECTURE.md`
alone. **That is an artifact of how the file is stored, not a deletion of anything.**

**It is ratified rather than left implicit because a successor re-implementing the enumeration will
get 610 unless it makes the same decision, and nothing in the record currently tells it to.**

### 1.6 Finding four — stratum 1 contains this sitting's own predecessor record — **ACCEPTED, declared on the stratum's face**

**Ruled: accepted.** Excluding a ruling record for its recency would need a rule nothing in this
project supports, and the placement test asks whether the frame can hold a statement, not where the
statement came from.

**What is declared on the stratum's face: the circularity.** Stratum 1 contains rulings that defined
stratum 1, and a reader must be able to see that without reconstructing it.

### 1.7 Two hazards carried by this ruling, declared on its face

**(i) The correction is made with the counts visible.** Stratum 1 was reported at `N = 382` and
stratum 2 at `N = 236` before this correction was chosen. **Property (a) of Ruling 1 of 2026-08-27 —
that the selection is fixed before the numbers are visible — is spent for these two strata**, exactly
as it was spent for the take rule. What partly answers it: the corrected forms are chosen by a
criterion stated without reference to any count.

**(ii) The two strata's memberships behave differently and it is not cured.** Stratum 1's membership
is a **signature**, so it grows as this project writes ruling records — including the record of this
sitting. Stratum 2's is a **frozen list of 35 paths**, ruled at the previous sitting, and it is **not
extended** to admit `cowork_redraw_findings_surface_2026_08_27.md` or any other surface written since.
**The asymmetry is declared, not cured**; extending a ruled list without a ruling is the larger fault.

---

## 2. What this ruling does NOT do

No frame text is authored and no part of the frame is written. The two conflicting ruling-record
definitions are still not reconciled. No decision-surface class and no dossier class is created. No
dormancy marker convention is built. Strata 3, 4, 5, 7 and 8 are not reopened, and neither is any
ruling of the stopped-strata sitting other than the two unit forms this one voids. No finding number
is allocated. No open-items row is created, flipped or discarded; `[[OI-179]]` stays OPEN and GATES,
`[[OI-372]]` remains the one standing DECISION red with a five-member STOP list, `[[OI-377]]` stays
OPEN and deliberately unfixed. Nothing is landed in git by this session. No `src/` change, no build,
no test, no measurement tool of the analysis, no guard run.

**The register blocker is untouched and remains a decision act never put to the user.** The last
dispatch was the sixth consecutive batch shaped to route around it, and the dispatch this sitting
produces will be the seventh.

**Still owed and unchanged:** which side performs the ARM/SITE fill-in and when; the homeless routed
content; whether the class-24 record repeats the two-files slip; the register blocker; the incoming
external input the user is assembling elsewhere, whose timing Ruling 6 of 2026-08-26 bears on.

---

## 3. This session's counted errors — two

**(1) The ruled decision form was breached, twice in one message.** After the second surface of the
first sitting was delivered, this side restated its recommendations in conversation and re-put the
choice question in the same message. **The user stopped the sitting over it.** Recorded at
`cowork_rulings_2026_08_27_stopped_strata_sitting.md` §2. Not one of the named degradation tells; not
self-caught.

**(2) ★ A RELATIONSHIP ASSERTED THAT THIS SIDE NEVER DERIVED — one of the named degradation tells of
the standing rule of 2026-08-15.** `cc_instruction_placement_sample_redraw.md` §1.1 stated that
`cowork_rulings_2026_08_27_stopped_strata_sitting.md` *"was already on disk when that count was
taken and is included in it."* **It was not.** The count of 74 was taken at the start of the session,
hours before that record was written. The correct figures are 75 and 79, since re-established at the
directory listing by this side. **The drawing side caught it at the objects, reported it, and did not
adjust the membership — which is exactly right.**

**Per the standing rule: ONE of the named degradation tells has occurred, which is below the two the
rule sets as the handover threshold.** It is reported unprompted rather than waited on. The ratio of
*checked at this object* to *recalled* was deliberately moved in this sitting's favour: every figure
in the surface that governs the recommendation was measured here, and §10 of the surface names the
files.

---

*Provenance: Cowork, 2026-08-27, the fifty-second session, at tip
`93c154562083516ea41cf6d01bcb6ea6cf4eb859`, read at the ref with the file tool. Every governing
document read from a bridge-staged snapshot with the file tools; no shell command was run against the
repository by this side, which therefore cannot resolve a commit or a blob and relays every git-object
figure. Read whole: `cc_report_placement_sample_redraw.md`. Measured at the objects by this side: the
tip; 75 root-level `cowork_rulings_*.md`; 22 rulings-family files; 7 decision surfaces. Not opened, in
any part: either sealed sample, `cowork_evidence_inventory.md`, `ARCHITECTURE.md`, `CLAUDE.md`,
`DECISIONS.md`, any source file, any measurement output, any dossier, any boot pack. This side is
barred from authoring the frame. The user's words: "i have read it" / "Agree with recommendation".*
