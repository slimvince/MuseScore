# CC INSTRUCTION — C1 §2.1 explanation + the Cowork narrative fold (2026-07-04)

**Status: ACTIVE DISPATCH (the only open instruction). Docs/narrative only — NO `src/` changes, NO build, NO
tool changes, NO measurement re-runs beyond the cheap Task-1 inspection. C1 itself is RATIFIED (STATUS 22j);
this dispatch discharges its two loose ends.**

## Mandatory reads BEFORE any work

1. `CLAUDE.md` (bash rules; commit discipline) + `STATUS.md` header + the new 22j entry.
2. `cc_c1_reliability_report.md` §2.1 (the claim under question) + `cc_instruction_c1_reliability_instrumentation.md`
   (the context this closes out).

## Task 1 — the owed §2.1 explanation

Report §2.1 states the harness "reproduces the ratified A-8 variant-(b) key-agree baseline **exactly**" while
the numbers shown are near-equal, not equal: **68.18 vs 68.11 (Baroque) / 64.52 vs 64.43 (Jazz) / 67.77 vs
67.50 (Default)** — same-direction deltas up to 0.27 pp.

- **State the mechanism** for the delta, verified at the two code paths (`tools/c1_reliability.py` vs
  `tools/a8_rebaseline_measure.py`): candidate causes to check include the covered-cell set (key-covered vs
  root-covered cells), duration weighting scope, coverage denominator, or the keymargin-join substrate. Do NOT
  guess — read both aggregation paths. A cheap read-only scratch run to confirm the mechanism is authorized;
  no corpus regen, no `src/` touch.
- **Write the answer as an addendum section `§2.1a — baseline-delta mechanism`** appended to
  `cc_c1_reliability_report.md`, correcting the word "exactly" in §2.1 to an accurate statement (e.g.
  "reproduces to within X pp; mechanism: …"). Update the trailing line-count note.
- **STOP condition:** if the mechanism is a join or primitive DEFECT (cells mis-joined, wrong parser, wrong
  weighting) rather than a benign, nameable definition/coverage nuance — STOP and report before any commit;
  that would put the §2 curves in question and needs a Cowork ruling.

## Task 2 — the narrative fold commit (`docs(cowork):`)

One commit, exactly this list (the accumulated uncommitted Cowork narrative + this dispatch's records):

1. `STATUS.md` (the 22g close-out edit + 22h + 22i + 22j entries)
2. `cowork_handoff.md` (header + standing-record updates through 22j)
3. `cowork_score_census.md` (§8b/§8c governance additions)
4. `cowork_candidate_lever_register.md` (NEW file — R-1…R-13)
5. `cowork_product_tool_register.md` (NEW file — T-1…T-32 + E-1…E-14)
6. `cowork_polyphony_phrase_harmony_research.md` (§6b at-pin corrections)
7. `docs/implementation_roadmap.md` (the A-8-ratification block + wave-plan edits)
8. `cowork_voiceleading_axis_design.md` (§15-4/§5.4 at-pin notes)
9. `cc_c1_reliability_report.md` (the Task-1 §2.1a addendum — force-add, `/cc_*.md` is gitignored)
10. `cc_instruction_c1_reliability_instrumentation.md` + `cc_instruction_c1_fold_and_explanation.md`
    (instruction records — force-add, the established convention)

**Reconciliation before committing:** check `git status` against this list.
- A listed file with NO changes → surface it in the report (do not silently drop).
- An UNLISTED modified/untracked `cowork_*`/doc file beyond the known exclusions (the deliberately-untracked
  dumps/scratch, `/cc_*` non-listed items, the perpetually-dirty `muse` submodule — NEVER commit it) →
  surface it in the report and leave it OUT of the commit.
- Nothing under `src/` may appear in the commit at all.

## Task 3 — report (`cc_c1_fold_report.md`, force-added in the same commit)

Short: the §2.1a mechanism statement (with what was read/run to establish it); the reconciliation result
(exact file list committed, any surfaced discrepancies); **the commit SHA (mandatory)**; confirmation nothing
under `src/` was touched and the gate is untouched by construction (docs-only — state it, no re-measurement
needed).

## What this dispatch must NOT do

No `src/` edits, no tool-code edits (`c1_reliability.py` included — if Task 1 finds a defect, that is the STOP,
not a fix), no gate re-measurement, no golden refresh, no push (fork-only chain stays local; NEVER `upstream`).
