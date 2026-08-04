# OI-2 — EG-1: T1-2 F-B override demotion

> STATUS IS AUTHORITATIVE IN THE INDEX (OPEN_ITEMS.md) — this file carries narrative and provenance only and is NEVER the status of record

**Section A — STAGE-3 ENTRY GATE — blocks E4/L5 engagement (from `cowork_engage_arc_plan.md`)**

| OI-2 | EG-1: T1-2 F-B override demotion (arc-#11 design; `attemptFineGrainOverride` unconditional, −756) | arc plan; premise-debt T1-2; `functionresolver.cpp:529-531` | OPEN — prerequisite |

*Resolution belongs in the INDEX row; dated notes may be appended here.*

---

**Dated note — 2026-08-04 (CC, READ WAVE 3, dispatch `cc_instruction_reads_3.md` Task 4, on the
user's ruling R4). The redesign this row asks for now has a register identity, and the state of the
mechanism it acts on is established rather than assumed.**

## What is registered

Read wave 2 read `cowork_fb_redesign_design.md` in full and entered four decisions, all ratified as
drafted on 2026-08-04:

- **D-490** — FALSIFIED: no threshold can make the override net-positive; the harm rate is flat
  against both quantities the threshold is built from, so no setting separates corrections from
  harms and the best measurable bar disables it.
- **D-491** — REFUTED: making the comparison vertically fair does not repair it either.
- **D-492** — the recommendation: demote the override to an **annotation** that carries the earlier
  reading unchanged and surfaces the contradiction, with simply disabling it as the accuracy-
  equivalent floor.
- **D-493** — the principled restriction (the genuinely coupled key-and-chord minority) is
  **un-computable** today, not merely unmeasured: its trigger requires the joint step.

Together they are the evidence base for this row's demotion, and D-492 is the shape of it.

## Why this note marks and does not act

**D-231** sequences all work: no fix design until phase 1 (specifications complete and true) and
phase 2 (issue-finding exhausted with measured coverage) close. A falsification does not create an
exception — it makes the eventual fix better evidenced, not earlier. The user's ruling R4 says the
same in terms: mark it as a phase-3 input, do not act on it. So this row is the place the phase-3
fix plan picks the F-B redesign up, and nothing here authorizes a build event.

The standing one-fix-per-family rule of 2026-07-28 also bears: whether the demotion is designed on
its own or with the resolver re-ordering ([[OI-1]]), the lost corrections ([[OI-24]]) and the
class-(b) movement obligation ([[OI-22]]) is a phase-3 grouping decision, not this row's.

## The arm check — established at the code, 2026-08-04

The dispatch declared as an assumption that the override sits on the **legacy** path, and asked for
it to be checked rather than carried, because a measured-harmful mechanism running on a production
surface would be a different situation entirely. Read with the file tools at HEAD:

- `attemptFineGrainOverride` is called from exactly one place —
  `resolveCarriedReadings` (`src/composing/analysis/function/functionresolver.cpp:530`);
- `resolveCarriedReadings`'s only non-test caller in the whole tree is
  `tools/batch_analyze.cpp:3321`, inside `runFullSpine`;
- `runFullSpine` is reached only from the `--dump-fullspine` block at `tools/batch_analyze.cpp:5506`,
  which writes its side file and `return 0`s at `:5519` — before `analyzeScore` or `analyzeRegions`
  is called;
- `functionresolver.h` is included by that one tool, by its own `.cpp`, and by
  `src/composing/tests/functionresolver_tests.cpp` — and by nothing else. No `src/notation/` or
  joint-module consumer exists.

**Verdict: dormant, and NARROWER than "legacy".** It is not on the production record arm, and it is
not on the legacy production path either — plain flag-less `batch_analyze`, which [[OI-289]] and
phase 1w established as a real reachability path for the legacy arm generally, does **not** reach it,
because the joint/legacy fork is downstream of a dump flag that returns first. So the answer to the
dispatch's STOP condition is **no STOP**.

Two things this does not license. It does not weaken the row: a mechanism that is dormant is still a
prerequisite the engage step must discharge before it can run at all. And it does not re-open the
LEGACY-mark question the register settled — a mark states what a decision is ABOUT, and dormancy is
never evidence a design may put load on ([[OI-289]], the weakened marking convention).

*Provenance: CC, READ WAVE 3, 2026-08-04, dispatch `cc_instruction_reads_3.md` Tasks 4.1 and 4.2.
Cross-ref [[OI-1]], [[OI-3]], [[OI-22]], [[OI-24]], [[OI-289]]; register D-490, D-491, D-492, D-493,
D-231.*
