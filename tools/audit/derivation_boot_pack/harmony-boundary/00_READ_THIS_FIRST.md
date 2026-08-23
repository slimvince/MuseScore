# READ THIS FIRST — the whole of what this session opens

You are an **implementation-blind deriving session**. Your work is to write what the analysis
**should** do for one unit, from the domain and from the ruled design intent — **not** to describe
what any existing code or specification says it currently **does**.

**The unit for this session is: How the analysis should decide where one chord ends and the next begins, and what evidence decides it.**

## The six files of this pack, in order

1. `01_the_phase_definitions.md` — The six phases and the standing constraints over every one of them
2. `02_the_guiding_principles_and_the_conventions.md` — The guiding principles and the conventions
3. `03_the_writing_standards.md` — The writing standards every derived specification is written to
4. `04_the_dispatch_protocol.md` — The dispatch protocol a deriving session is dispatched under
5. `05_the_ratified_design_intent.md` — The ratified design intent, CUT for this subject
6. `06_the_defect_type_catalog.md` — The defect-type catalog — type and definition only

Read them in that order. Together with this file they are **the whole of your read**.

## The boundary, stated once and binding

**This directory replaces the ordinary session-start read for you.** `cowork_handoff.md`,
`STATUS.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `docs/scoring_model.md`, the open-items register
and its derived gating answer, and every `cc_*` and `cowork_*` file outside this directory are
**NOT opened**. No branch rule is taken. Nothing outside this directory is opened at all.

**If you nonetheless meet a statement about how THIS project's analysis currently works — in any
file, including one of these six — STOP READING THAT FILE AT THAT POINT and record WHERE you were
and HOW MUCH you had seen.** That record is part of your output. It is not a failure; an unrecorded
one is.

## What has been cut out of this pack, and why you are told

Material has been withheld from this pack **for this subject**, so that what you derive can be
compared against a ruled answer you have not read. Two kinds:

* entries of the design-intent file that were not rendered — you will see identifier gaps, and
  those gaps are **not** evidence of anything;
* 2 passages inside `02_the_guiding_principles_and_the_conventions.md`, each marked in place where it was removed.

**Do not try to reconstruct any of it, and do not treat a gap as a hint.** Derive the unit from the
domain and from what this pack does carry.

## What your output is

A specification of the unit named above, in the six-field form the writing standards and the phase
definitions in this pack describe, plus your source declaration — which files you actually
consulted — and any stop-and-record notes from the clause above.
