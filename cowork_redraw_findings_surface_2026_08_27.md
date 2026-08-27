# Decision surface — what is done about the four findings the redraw returned

> **STATUS: DECISION SURFACE.** Cowork, 2026-08-27, the fifty-second session. One decision, the
> alternatives, what each costs towards the objective and the ruled principles, and a recommendation.
> **There is no question in the turn that delivers it.** The choice question is put in a later turn.
>
> **Taken at branch tip `93c154562083516ea41cf6d01bcb6ea6cf4eb859`**, read at `.git/refs/heads/master`
> with the file tool — the ref side. No shell command was run against the repository by this side.
>
> **★ EVERY FIGURE BELOW IS LABELLED EITHER *MEASURED HERE* OR *RELAYED*.** Measured here means this
> side opened the files and counted with the file tools, and §7 says exactly which files. Relayed
> means it comes from `cc_report_placement_sample_redraw.md` and **this side has no shell and cannot
> verify it.**
>
> **Not opened by this side, in any part:** `cowork_placement_sample_sealed_redraw_2026_08_27.md`,
> `cowork_placement_sample_sealed_2026_08_27.md`, `cowork_evidence_inventory.md`, `ARCHITECTURE.md`,
> `CLAUDE.md`, `DECISIONS.md`, any source file, any measurement output.

---

## 1. What has happened, and what this decision is about

The placement sample was redrawn and re-sealed. **Seven strata are drawn, one is recorded as not
enumerable, and no stratum remains STOPPED**, so the frame is no longer gated on any decision — only
on the sealed file, which now exists.

The batch also surfaced **four things that no ruling covers**. Three of them are readings the drawing
side had to take because the rule did not decide them; one is a count that came out other than
expected. None was hidden and none was adjusted quietly — which is the instruction working.

**This decision is what is done about the four.** It is put as one decision because all four share
one shape — *accept and declare, or correct and redraw* — and because the cost that dominates is the
number of further dispatch cycles, which is a single quantity.

---

## 2. Finding one — the unit forms for strata 1 and 2 admit ordinary section headings

**What was declared.** The dispatch declared, for stratum 1, that a *numbered ruling* is a markdown
heading whose text matches `Ruling <n>` **or** begins `<n>.` / `<n>)`; and for stratum 2, the same
shape with *Decision*. **That form was authored by this side and was never put to you** — it was
named in the handoff as a declared reading you could overturn.

**The defect, which is a property of the pattern and needs no measurement to see.** The second limb,
`<n>.`, matches **any** numbered section heading — `## 0. What was put`, `## 5. What this file does
NOT do`. So both strata enumerate section titles alongside the thing they are named for.

### 2.1 Stratum 1 — MEASURED HERE, and the report's headline overstates the damage

This side opened **22 of the 79 ruling records** — a sample, not a census — and counted with the file
tools:

| | |
|---|---|
| headings the declared form admits | **103** |
| of those, headings that are actually rulings — `<n>. Ruling <n> …` or `Ruling <n> …` | **69** |
| ordinary section headings | **34, or 33%** |
| files returning zero | **5** |

**★ THE REPORT'S TABLE SAYS 5 OF 25 DRAWN ITEMS MATCH "THE FIRST LIMB" AND 20 MATCH ONLY THE NUMBERED
LIMB. THAT IS NOT THE SAME STATEMENT AS "20 ARE NOT RULINGS", AND THE DIFFERENCE IS LARGE.** The
records' house style is `## 1. Ruling 1 — …`, which begins with a digit, so it matches **only** the
numbered limb while being a ruling in full. The report's own prose says as much; its table invites the
wrong reading. **Measured with a test that asks whether the heading is a ruling rather than which limb
fired, two thirds of what stratum 1 admits are rulings.**

**One independent corroboration, measured here.** The five files in this side's sample that return
zero are `cowork_rulings_2026_08_15_period_start.md`, `cowork_rulings_2026_08_15_session_length.md`,
`cowork_owner_rulings_2026_08_07.md`, `cowork_ruling_guard_family_2026_08_08.md`,
`cowork_document_route_rulings_2026_08_08.md` — **exactly the five the report names as
zero-returning across all 79.** Two enumerations, one list.

### 2.2 Stratum 2 — MEASURED HERE, and this one is as bad as the report says

This side opened **7 of the 35 listed decision surfaces** and counted:

| | |
|---|---|
| headings the declared form admits | **48** |
| of those, actual `Decision <n>` headings | **8, or 17%** |
| files carrying at least one numbered decision | **2 of 7** |
| files admitting nothing at all | **1** — `cowork_extent_decision_surface.md`, which numbers its sections `## §1`, `## §2`, so no heading begins with a digit |

**The eight are all in two files** — `cowork_placement_sample_surface_2026_08_27.md` (3) and
`cowork_framework_phase_opening_surface_2026_08_26.md` (5), both of which head their decisions
`### DECISION n`. **The other five surfaces carry their decision without numbering it**, because a
surface that argues one decision has nothing to number. The three surfaces of this sitting are among
them: each carries exactly one decision and none of their 22 admitted headings is it.

**So stratum 2, as drawn, is a sample of numbered section titles in decision surfaces.** Relayed and
consistent with that: the report states that **not one of stratum 2's 25 drawn items is a
`Decision <n>` heading.**

**What is NOT known, and will not be guessed here.** The corrected population over all 35 files is
**unmeasured**. Eight in seven files does not license an estimate over thirty-five, and this surface
does not make one.

---

## 3. Finding two — the list-item unit was pinned to bullets, and no decision said so

**RELAYED.** The confirmed reading for stratum 5 was *every markdown list item at any nesting depth*,
at `N = 33`. The drawing side reports that this returns 33 **only if list items are read as bullet
items** (`-`, `*`, `+`); admitting ordered items (`1.`, `1)`) returns **38**. Because the dispatch
carried a STOP forbidding any `N` other than 33 for that stratum, bullets-only is what the STOP
forced.

**So the reading was fixed by an instruction of this side's rather than by a decision of yours** —
and Ruling 1 requires stratum 3 to be read alike, so it binds there too. Relayed: over the ten
dossiers reachable at the git objects, the wider reading gives 251 items against 179.

**This side did not verify the 33-against-38 figure, deliberately.** Verifying it means opening
`cowork_evidence_inventory.md` — and opening the file in order to decide how its items should be
counted is precisely the sighted choice Ruling 1 of 2026-08-27 protects the sample against. **The
abstention is the discipline, not a gap in effort.**

---

## 4. Finding three — stratum 8 needs line-ending normalisation, which no ruling states

**RELAYED, and this side cannot verify any of it without a shell.** The unit compares heading text
between two versions of a file. Several member files changed from CRLF to LF in their history —
`ARCHITECTURE.md` at 26 commits. Without stripping the carriage return before comparing, **the single
commit at which a file's line endings change reads as every heading in that file being deleted at
once**, and the stratum returns **610 events instead of 59**, 580 of them from `ARCHITECTURE.md`
alone. Normalisation was applied and is what reproduces the confirmed 59 / 60.

**It is a real decision about the unit and the record does not contain it.**

---

## 5. Finding four — stratum 1 now contains this sitting's own ruling record

**MEASURED HERE.** The root holds **75** files matching `cowork_rulings_*.md`, counted at the
directory listing; with the four other admitted name shapes that is **79**. The 79th is
`cowork_rulings_2026_08_27_stopped_strata_sitting.md` — the record of the very sitting that declared
this stratum's membership.

**And the dispatch's stated ground for expecting 78 was wrong.** It said that file *"was already on
disk when that count was taken"*. It was not: this side took the count of 74 at the start of the
session, hours before that record existed. **The drawing side caught it at the objects and reported
it without adjusting the membership, which is exactly right.** It is counted as this side's error at
§8.

**The substance, separate from the error.** The sample may now carry, as statements to be placed, the
rulings that defined the sample.

---

## 6. The alternatives

Judged towards four things already ruled or stated by you: **(a)** the sample must not be shaped by a
side that can see what its choices admit; **(b)** a finding must be reportable per stratum with an
honest uncertainty range; **(c)** a statement that must be interpreted before it can be placed is not
a statement; **(d)** the standing bar against work pitched at too high a meta level.

### Alternative A — accept all seven strata as drawn, and rename two of them on the sealed file's face

No redraw. Strata 1 and 2 are relabelled for what they are — *numbered headings in ruling records* and
*numbered headings in decision surfaces* — so no successor reads a result from them as being about
rulings or decisions. Findings two, three and four are ratified as they stand.

**Towards the objective.** The frame can be authored today. Nothing is spent.

**Its cost.** Stratum 2's result would be a result about section titles. Measured here, **83% of what
it admits is not a decision, and five of the seven surfaces opened carry no numbered decision at
all.** *"The frame cannot hold decision-surface statements"* would not be supportable from it, and
that is one of the two strata the whole stratification exists to report separately.

### Alternative B — correct the unit form for strata 1 and 2 only; redraw those two; leave the rest as drawn

One further dispatch. Stratum 1's unit becomes a heading that is a ruling — `<n>. Ruling <n>` or
`Ruling <n>` — the test measured here, which returns 69 across 22 records. Stratum 2's becomes
`Decision <n>` alone, with the numbered limb dropped; a surface with no numbered decision contributes
zero and is reported as zero. Strata 3, 4, 5, 7 and 8 are untouched and carry across.

**Towards the objective.** The two governance strata become what they claim to be. Everything else is
already sound, so nothing sound is disturbed.

**Towards (b).** Stratum 2's corrected count is **unknown** and may fall at or below 25, in which case
it becomes a census and needs no uncertainty range at all. **That is a possibility, not a
prediction** — nobody has measured it.

**Its costs, both real.** One more dispatch, one more CC run, one more verification sitting. And
**the correction is made with stratum 1's and stratum 2's counts already visible — 382 and 236** — so
property (a) is spent for these two strata exactly as it was spent for the take rule. What partly
answers it is that the corrected forms are chosen by a test stated without reference to any count:
*does the heading say it is a ruling, or a decision*.

### Alternative C — correct and redraw the whole sample again

Nothing else is broken. Strata 3, 5, 7 and 8 reproduce the confirmed figures and their readings are
ruled. **Redrawing them would spend a cycle to change nothing**, and it is named only so it is not
proposed later as new.

### Alternative D — drop strata 1 and 2 from the sample

Cheapest of all, and it removes the two strata that overlap what the frame's author must read. **But
Ruling 1 of this sitting already refused the equivalent move** for a different reason: those two are
the project's governance records, and the frame is most likely to fail where the statement is a
governing one. Dropping them removes the half of the test most likely to produce a finding.

---

## 7. Recommendation

**Alternative B, with findings two, three and four ratified as they stand.**

**7.1 — Strata 1 and 2: corrected unit, redrawn.** Stratum 1's measured 33% mis-admission is not
fatal on its own; stratum 2's 83% is. They are corrected together because they share one form, one
dispatch and one defect, and correcting only the worse of the two would leave the record carrying two
different answers to the same question.

**7.2 — Finding two, the bullets-only reading: RATIFIED as it stands, not reopened.** It is what
returns the confirmed `N = 33`, and the alternative would reopen a ruling you took two turns ago and
move stratum 3 substantially. **Declared with it and to be written on the two strata's faces:** ordered
list items are excluded, they are plainly list items, and the exclusion was fixed by an instruction of
this side's rather than by a decision of yours.

**7.3 — Finding three, line-ending normalisation: RATIFIED.** Without it, one formatting commit reads
as 580 headings being deleted from `ARCHITECTURE.md` at once. **That is an artifact of how the file is
stored, not a deletion of anything**, and a stratum built on it would be measuring the repository's
whitespace history. This is the clearest of the four. It is ratified rather than left implicit
**because a successor re-implementing the enumeration will get 610 unless it makes the same
decision**, and nothing in the record currently tells it to.

**7.4 — Finding four, the self-inclusion: ACCEPTED, and declared on the stratum's face.** Excluding
the sitting's own record would need a rule about recency that nothing in this project supports, and
the placement test asks whether the frame can hold a statement — not where the statement came from.
**What is declared is the circularity**: stratum 1 contains rulings that defined stratum 1, and a
reader must be able to see that without reconstructing it.

---

## 8. This side's error, recorded here rather than left to the ruling record alone

**The dispatch asserted a relationship this side never checked** — that the ruling record was on disk
when the count of 74 was taken. It was not. **That is one of the named degradation tells of your
standing rule of 2026-08-15: asserting something never derived at the object.** It is the first such
error this session; the earlier one, the breach of the decision form, is not on that list. **One tell,
which is below the two your rule sets as the handover threshold** — reported rather than waited on.

---

## 9. What this surface does NOT decide

- **Whether the frame is authored now or after the redraw.** If Alternative B is ruled, the frame's
  author must wait for the new sealed file; if A is ruled, it may start immediately. That follows from
  the choice and is not a separate question.
- **Anything durable.** No class definition, no amendment to any tool, no register entry, no
  open-items row, no finding number. Nothing is landed in git by this session.
- **The register blocker**, untouched and still a decision act never put to you — the last dispatch
  was the sixth consecutive batch shaped to route around it.

---

## 10. Method

**Read whole:** `cc_report_placement_sample_redraw.md`.

**Measured here, with the file tools, on files opened for this purpose:**

- the branch tip at the ref;
- the count of root-level `cowork_rulings_*.md` at the directory listing — **75**, and 79 with the four
  further name shapes;
- **22 rulings-family files** — `2026_08_08_pre_away`, `08_09_fifth_stop`, `08_09_return`,
  `08_11_eleventh_stop`, `08_13_seventeenth_stop`, `08_15_inventory_sitting`, `08_15_period_start`,
  `08_15_session_length`, `08_17_residue_sitting`, `08_19_twelfth_return`,
  `08_21_successor_plan_sitting`, `08_22_step_zero_return_sitting`, `08_23_brief_validation_sitting`,
  `08_24_sizing_pilot_sitting`, `08_25_cascade_sitting`, `08_26_framework_opening_sitting`,
  `08_27_placement_sample_sitting`, `08_27_stopped_strata_sitting`, `oi345_oi342_2026_08_07`,
  `owner_rulings_2026_08_07`, `ruling_guard_family_2026_08_08`, `document_route_rulings_2026_08_08`;
- **7 decision surfaces** — `cowork_extent_decision_surface.md`,
  `cowork_phase1_commissioning_surface_2026_08_11.md`,
  `cowork_framework_phase_opening_surface_2026_08_26.md`,
  `cowork_placement_sample_surface_2026_08_27.md`, and the three surfaces of this sitting.

**One measurement caveat, declared.** The staged copy of
`cowork_rulings_2026_08_27_stopped_strata_sitting.md` predates Ruling 3 by one section, so it
contributes 5 admitted / 2 rulings where the file on disk carries 6 / 3. **The corrected totals are
104 admitted and 70 rulings**; the table at §2.1 gives the figures as measured.

**Not verified, and not verifiable by this side:** every commit hash; every stratum count `N`; the 610
figure and the CRLF history behind it; the drawn positions; the guard, candidate and tree counts.
**★ THE VERIFICATION LIMIT IS NOW NINE SESSIONS OLD AND IS THE LARGEST HOLE IN THIS RECORD.** A
session with a shell should be spent on it before the placement test's results are relied on.

**This session is barred from authoring the frame** on three grounds: it read the handoff, it
corrected the selection rule, and it has ruled on the sample's composition.
