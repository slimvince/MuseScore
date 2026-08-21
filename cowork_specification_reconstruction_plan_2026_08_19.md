# PLAN — reconstructing the specifications, question by question

> **STATUS: DRAFT FOR THE USER'S RATIFICATION. NO WORK BEGINS UNTIL THIS PLAN IS RULED.**
> Drafted by Cowork, 2026-08-19, at branch tip `891bacc5d2`. Nothing in this file is executed by
> anything in it. It orders no act, opens no question, touches no document and moves no candidacy.
>
> **★ IT IS WRITTEN TO BE RULED IN ONE SITTING, AND TO BE THE LAST PLANNING ACT.** Every decision the
> work needs is settled here or is listed at §14 as a question for the user. A session executing this
> plan makes no further planning decisions of its own.

---

## 0. What this plan is for

**To produce a first new version of the specifications** — reconstructed from everything the project
knows, salvaging what is worth keeping and deriving the rest — ratified as the best obtainable from a
named set of sources, and written in a form that can then be compared against the implementation.

It serves the ultimate objective, maximum-precision inference (`CLAUDE.md` #4), indirectly and
deliberately: a specification that is defensible is what makes a precision change checkable rather
than a guess.

---

## 1. The diagnosis this plan rests on, stated so it is not re-litigated

Four facts, each established at the objects or at the file during the sitting that produced this
plan.

**(a) The specifications are polluted by the implementation, and the instruction that did it is
dead.** Until 2026-08-15, `D-231`'s phase 1 ordered *"the specification text is corrected wherever it
states something false at HEAD."* That instruction is how code enters a specification. It was
superseded on 2026-08-15 and `CLAUDE.md` now carries the replacement: *a disagreement between
specification and code is evidence, reserved for the audit; no document is corrected on the ground
that the code says otherwise.* **The cause is stopped. The damage is not repaired.**

**(b) The extent of the damage is unmeasured, and the measuring effort went to the wrong surface.**
`tools/audit/decisions_filter_classification.json` measures the decisions register — 677 entries, 411
with a nameable deciding act, 182 with none found, 84 evidence-ambiguous. That is an index of
decisions. The pollution is in `ARCHITECTURE.md` (532,289 bytes) and `docs/scoring_model.md` (127,593
bytes), and **no artifact in `tools/audit/` takes either specification's provenance as its subject.**

**(c) Provenance cannot be recovered where it was never recorded, so the repair must not depend on
it.** A statement's history is not obtainable by reading harder. What a statement can be asked for is
a **defense** — a musical, research-based or measured reason — which `CLAUDE.md` already requires of
every design decision. This plan therefore repairs by defensibility and never by archaeology.

**(d) The previous programme did not fail on effort; it failed on shape.** Every batch's return
produced rulings, every ruling produced the next dispatch, and every dispatch produced a report whose
open questions produced the next return. The unit of work generated more units. Fourteen preparation
batches produced no specification text, and the act that would produce some — the pilot — never
opened, its one prerequisite excluded by name from every dispatch.

---

## 2. Scope

**In scope:** the specification of the analysis — what the analysis should do and why — reconstructed
question by question, ratified per question, and written so each statement can be compared against
the code.

**Out of scope, and named so a session does not drift into them:** repairing the existing documents
in place; recovering provenance; classifying the decisions register; building any measurement tool;
changing any code; running any build, test or guard; the archiving wave; the open-items register; the
findings series; and the phase-1 finish line, which describes a programme the record superseded on
2026-08-15.

---

## 3. The unit of work — ten questions, and their order

The unit is **one question the analysis must answer**, not one section of an existing document. The
existing structure is part of what is being replaced, so inheriting it would inherit the problem.

**The ten questions (AUTHORED — see §14, question 1):**

1. **Segmentation** — where one harmony ends and the next begins.
2. **Chord tones** — which sounding pitches belong to the harmony and which do not.
3. **Root** — which pitch class is the root.
4. **Quality** — what kind of chord it is.
5. **Bass and inversion** — what is in the bass and whether the chord is inverted.
6. **Key** — what key is in force.
7. **Key change** — when the key has changed rather than been momentarily tonicised.
8. **Function** — what the harmony does in its key.
9. **Spelling** — how pitches and chords are spelled.
10. **Emission** — what is written out: symbols, Roman numerals, annotations.

**The order is dependency, not importance**, so each question is derived against inputs already
settled. **Segmentation is first**, and three measured facts agree rather than one preference: it
consumes none of the others; `docs/scoring_model.md` §8 records that only re-weighting **or a
different segmentation** can reach the arpeggio root failure, because the wrong reading there is the
global optimum; and the cross-layer caveat in `CLAUDE.md` records that an over-grabbed segment picks
up a bass note that does not sound where the error is, and the bass is what separates the share-tone
readings.

**The list is closed at ten.** An eleventh question is a matter for the user (§14), never a unit a
session takes on its own.

---

## 4. Roles

**Cowork (the writing side) derives, harvests, reconciles and drafts.** This is prose and judgment; it
needs no dispatch, no build and no code change, so it cannot be starved by the batch cycle.

**The user ratifies, per question**, and answers the open questions that question raised.

**CC (the executing side) does nothing under this plan.** Its work begins at the delta analysis (§12),
which is a separate act under a separate ruling.

---

## 5. What is read

**Read once, and standing for all ten questions. Three of the four are already done.**

| source | state |
|---|---|
| `CLAUDE.md` — the guiding principles and the Conventions | **read in full**, 2026-08-19 |
| `CLAUDE.md` — the gate block: measured baselines, grading conventions, the caveats on how they are read | **read in full**, 2026-08-19 |
| `DEFECT_TYPES.md` — 26 defect types with founding instances and detection signatures | **read in full**, 2026-08-19 |
| `docs/scoring_model.md` §8 — the constraints and dead ends | **read to line 1328**; about 130 lines remain |

**Found per question, and this is the only recurring reading act.** For each question, the documents
that cover it are located by searching for the subject — not by classifying the corpus — and the list
is written down and shown to the user **before it is read**, so a missing source is named while it is
still cheap. For a typical question that list is expected to be:

- the passages of `ARCHITECTURE.md` that specify it;
- any `docs/` design document whose subject it is;
- every deletion ever made from those passages (`git log` over the region — the only place history is
  consulted, because what still stands is already in the current text and only removals are invisible);
- the register entries whose subject it is;
- the `docs/scoring_model.md` §8 constraints specific to it;
- the code sites that implement it;
- the failing runs in the corpus that turn on it.

**Honest statement of what is not known yet:** which documents cover question 1 has not been
established. That search is the first step of the first pass, and its result is shown before it is
read.

---

## 6. The steps, per question

Executed in this order and no other.

**Step 1 — Locate and declare the sources.** Search for the documents covering the question. Write the
list. **Show it to the user before reading any of it.** The user may add or remove members. The list
is then fixed for the pass and is not extended mid-pass (guardrail 4).

**Step 2 — Derive blind.** Write what the analysis should do about this question, from music theory,
the published research, and the annotated corpus. **The current specification and the code stay
closed.** Every statement carries its defense in the same breath; a statement with no defense is not
written. Where the derivation cannot settle something, it is written as an open question rather than
filled with the most plausible reading.

**Step 3 — Open the declared sources and grade the derivation against them.** Four outcomes, a closed
set, each with a different consequence:

| outcome | consequence |
|---|---|
| **confirms** a derived statement | the statement stands, with the confirmation cited |
| **contradicts** it | an **open question**, both readings stated, never resolved silently |
| **adds** something the derivation missed | **salvage** — admitted, with its own defense recorded |
| **records a dead end the derivation walked into** | the derived statement is withdrawn, and this is also the measurement of whether the derivation method can be trusted |

The order of steps 2 and 3 is load-bearing. Reading the record first would anchor the derivation on
the existing framing; reading it after turns it into a test of the derivation.

**Step 4 — Reconcile into a statement set** in the form of §7.

**Step 5 — Put it to the user for ratification**, as one surface carrying the statement set, the open
questions, the sources read, and what was excluded and why. No question is asked in the same turn the
surface is delivered.

**Step 6 — Land it.** The ratified section is written as its own document. The corresponding passages
of `ARCHITECTURE.md` are re-bannered as reference once covered — **nothing is deleted and no former
wording is lost.**

---

## 7. The form of the output

Every statement is atomic — **one rule per statement**, because a paragraph cannot be compared against
code — and carries five fields:

1. **The statement.** What the analysis must do.
2. **The defense.** The music theory, the published research, or the measurement that decides it.
   *"Because the implementation does this"* is not a defense, and a statement supported only by the
   code is marked **UNSUPPORTED** rather than admitted.
3. **The source class.** **derived** (from theory, research or the corpus) · **salvaged** (found in the
   record and admitted with its defense) · **measured** (established on the annotated corpus).
4. **The status.** **settled** or **open**.
5. **What would falsify it in code.** The observable behaviour that decides conformance. This field is
   what makes the delta analysis mechanical rather than interpretive, and a statement that cannot
   carry it is marked as unverifiable rather than left to look checkable.

---

## 8. The guardrails

Each is aimed at a failure observed in this project, and the failure is named so the guardrail cannot
be softened into general advice.

1. **A pass produces specification statements, an open-questions list and a findings note — nothing
   else.** No new tool, artifact, register row, rule or numbered finding. *Stops:* fourteen batches
   whose outputs were machinery for the next batch.
2. **Findings attach to their question and never get numbers or rows.** They are read at that
   question's ratification and closed with it. *Stops:* a findings series that reached F88, each
   member acquiring an owner, a lifecycle and a place in every future handover.
3. **No mechanism is built during a pass. Zero.** What can only be checked by a tool is recorded as
   unchecked, with its reason. *Stops:* the establishment recursion — establishing the tool that
   establishes the tool.
4. **The sources are declared before reading and never extended mid-pass.** Anything found outside them
   is written down as an input to a later question. *Stops:* the rabbit hole, every instance of which
   was individually justified.
5. **A declared budget per question; overrun is a stop, not a continue.** *Stops:* the absence of any
   cost ceiling on any act in this project's history.
6. **The done condition is written before the work starts.** *Stops:* a finish line open since August
   that now describes a superseded programme.
7. **No ruling is taken during a pass.** Open questions accumulate to one ratification at the end.
   *Stops:* the engine itself — return, rulings, dispatch, return.
8. **One file per question, and no record about the record.** No close, no chain table, no correction
   commit about a correction. *Stops:* a batch of 77 written lines that generated about 1,500 lines
   describing itself.
9. **A ratified question is closed.** A later question that bears on it produces a note; re-opening
   takes the user's word. *Stops:* the same subjects re-litigated across four sittings.
10. **The question list is closed at ten.** *Stops:* a unit of work that generates more units.
11. **One tell, checked at the end of every pass, in one sentence:** *did this pass produce anything
    other than specification statements, an open-questions list and a findings note? If yes — name
    it.* Checked by the user reading one short thing, not by a guard. **If a session proposes building
    something to check these guardrails, that proposal is itself the tell firing.**

---

## 9. Stop conditions

A pass halts and reports, rather than continuing, when any of these holds:

- the declared sources cannot be located, or a named source does not exist;
- the derivation and the record contradict each other on a point the pass cannot leave open;
- the budget is reached;
- the pass finds that the question is not separable from another question in the list;
- the pass would have to build something, change code, or take a ruling to continue.

A stop records what was done, what was not, and that the remainder is untouched rather than
half-worked.

---

## 10. Budget and cadence

**Question 1 is done alone and measured**: elapsed effort, statements produced, salvage found, open
questions raised, and how much of the declared reading turned out to matter. **Those numbers set the
budget for the remaining nine**, which is not fixed in advance here because no honest basis for it
exists yet.

One question at a time. No question begins before the previous one is ratified.

---

## 11. Done conditions

**Per question:** the statement set covers every decision the question names; every statement carries
its five fields; every open question is listed rather than filled; the sources read and the exclusions
are recorded; and the user has ratified.

**For the plan as a whole:** all ten questions ratified, and the resulting statement set is the first
new version of the specifications — described as *the best reconstruction obtainable from the named
sources, with these open questions*, and never as *correct*.

---

## 12. What happens after — the delta analysis, described and NOT authorized here

Once a question is ratified, each of its statements can be compared against the implementation under a
closed verdict set: **conforms · diverges · not implemented · present in code but in no statement.**
Every divergence is **evidence reserved for the audit**, and a licence to change neither side.

**This plan does not authorize that comparison.** It is a separate act needing its own ruling, and it
is described here only so that §7's fifth field is understood as serving it.

---

## 13. What this plan does NOT do

No `src/` change, no build, no test, no measurement tool, no guard run. No document is deleted,
archived or moved. No open-items row is created, flipped or discarded. No finding number is allocated.
No pin is taken. No existing specification text is edited — the old passages are re-bannered as
reference only after a ratified section covers their subject. It does not measure how polluted the
specifications are, and does not need to. It does not recover provenance. It does not repair the
decisions register. It does not re-open any ruling.

---

## 14. Open questions in this plan itself — for the user, at its ratification

1. **Are the ten questions the right ten?** The list is authored from the domain, not derived from any
   document. An eleventh, a merge or a split is the user's call.
2. **Is segmentation the right first question?** The three reasons given are measured, but the user may
   have a reason to start elsewhere.
3. **Where do the new sections live?** One document per question, or one assembled specification? This
   plan assumes one document per question and no edit to `ARCHITECTURE.md` until a subject is covered.
4. **Does this replace the ruled PILOT phase, or execute it?** The six-phase structure ruled on
   2026-08-15 defines a pilot whose subject is `docs/scoring_model.md`, derived blind, with the current
   text opened afterwards — the same shape as §6 here, but aimed at a document rather than a question,
   and at a document whose own ratified banner says its mechanism content describes a scorer **dormant
   on both production surfaces.** This plan aims at questions instead. **That difference is the user's
   to rule**, and nothing here should be read as having settled it.
5. **Is the curated boot list needed at all under this plan?** It was drafted on 2026-08-19 as the
   pilot's prerequisite. If this plan replaces the pilot's shape, that prerequisite may fall away.

---

*Provenance: Cowork, 2026-08-19, drafted at branch tip `891bacc5d2` in the remote Cowork environment.
Every establishment in §1 was taken by git OBJECT read at an explicit hash or by opening a snapshot
staged through the device bridge with the file tools; `CLAUDE.md` was read in full by the drafting
session, lines 1 to 1844. `DECISIONS.md` was read in full BY DELEGATION and that is a departure rather
than a discharge. `git status` was not run — it is measured to time out on this mount. No count in this
file is transcribed from a surface that repeats it; each is derived at the artifact named beside it.*
