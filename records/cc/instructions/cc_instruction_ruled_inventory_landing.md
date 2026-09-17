# CC dispatch — land the sitting's records, land the 122 cited files with the `.gitignore` rule removal, clear two guard reds, and run the class-1 construction-evidence check

> **Dispatch (Cowork, 2026-08-15).** Executes the rulings of
> `cowork_rulings_2026_08_15_inventory_sitting.md` §1 (the landing), §3.1 (the class-1 check)
> and §5 (the guard clearing). Written at a verified STOP; nothing else is running.
> **Read first, in full:** that ruling record; then `cowork_rulings_2026_08_15_method_directions.md`;
> then `cowork_handoff.md`'s seventeenth entry block. The standing bars are unchanged and bind
> this batch whole: **no `src/` edit, no golden, no test changed, nothing under `tools/corpus/`
> or `tools/robust_stop/`, no measurement of the analysis, no design, no repair, no
> decisions-register entry** (the filtering ruling stands), no open-items row created or flipped
> except exactly where Task 2 orders it.
>
> **Commit-and-push per task. Run the FULL guard set BEFORE the first edit** (the inventory
> batch's declared departure is not repeated) **and again at the end.** Record both states.
> Verify every commit after the fact at the object (`git diff-tree --no-commit-id --name-only -r
> <sha>`) and record the SHAs in the close. Reserved-word conventions bind all new prose.

## Ruling ledger (what this batch may rest on — quoted at the record, not paraphrased)

- §1: the 122 cited files land as one commit naming its own act, list taken from the ruling
  surface's *The cited-and-ignored files (DERIVED)* section; `/cc_*.md` removed from
  `.gitignore` in the same act; the remaining ignored files are NOT landed.
- §5: the third red's clearing is ordered, WITH the extension to [[OI-373]]'s two
  run-instructions and that row's resolution with provenance.
- §3.1: the class-1 check is ordered; SPEC-DERIVED findings return to the user; unestablished
  construction defaults to code-built.

## Premise ledger

- **FACT** — `.gitignore` line 118 carries `/cc_*.md` (verified at the file 2026-08-15, Cowork).
- **FACT** — the ruling surface's cited-and-ignored list counts exactly 122 entries (verified by
  derivation over the file 2026-08-15, Cowork).
- **FACT** — `git log --all` shows zero commits for `cc_adoption_measurement_report.md` and
  `cc_tonicization_modulation_metric_dossier.md` (verified 2026-08-15, Cowork).
- **ASSUMPTION A1** — `gen_guard_classification.py`'s STOP names exactly ONE tool, the
  2026-08-13 entrant. **Check ordered before the act (Task 2 step 1); a different count is a
  STOP-and-report, never a guess.**
- **ASSUMPTION A2** — the runner's STOP names exactly the TWO tools the inventory batch's close
  names. **Check ordered before the act (Task 2 step 4); a different set is a STOP-and-report.**
- **ASSUMPTION A3** — every listed cited-and-ignored file still exists on disk unmodified since
  the inventory run. **Check: a listed file missing from disk is a STOP-and-report, never
  silently skipped.**

## Task 0 — land the writing-side records

Commit, in ONE commit whose message names its own act, exactly these FOUR paths and no fifth:

1. `cowork_rulings_2026_08_15_inventory_sitting.md` (new)
2. `cowork_handoff.md` (modified — the seventeenth entry block)
3. `cc_instruction_ruled_inventory_landing.md` (this file; still ignored at this point — stage
   with `-f`, the repository's own recorded practice, for the last time)
4. `ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` **only if modified on
   disk — expected NOT modified; if unmodified it is already tracked and this line is a no-op.**

Verify at the index through the sanctioned index-verification step the inventory batch's Task 0
used, then after the fact at the object: the commit's path count MUST be 3 (or 4 per the line
above). Push.

**Registered expectation E0:** `git diff-tree` on the Task 0 commit lists exactly 3 paths.

## Task 1 — the ruled landing (ruling §1)

1. Edit `.gitignore`: delete the line whose entire content is `/cc_*.md`. No other line moves.
2. Derive the landing list: parse
   `ratification_surfaces/cowork_artifact_inventory_ruling_surface.md`, section *The
   cited-and-ignored files (DERIVED)* (between that summary line and its closing
   `</details>`), extracting the backticked file name from each list line. **STOP if the count
   is not exactly 122.**
3. Stage `.gitignore` plus every listed file (A3's check applies per file). Commit as ONE
   commit whose message names its own act and cites ruling §1. Push.
4. Verify after the fact at the object: the commit's path list counts **exactly 123** and every
   listed name is among the 122 plus `.gitignore`. **STOP on any difference.**

**Registered expectation E1:** path count 123; `git log --all -- cc_adoption_measurement_report.md`
afterwards shows exactly one commit — this one.

## Task 2 — the guard clearing (ruling §5)

1. Run `python tools/audit/gen_guard_classification.py --check`. Record the STOP text verbatim.
   **A1's check:** exactly one named tool, entered 2026-08-13. Otherwise STOP-and-report.
2. Read the named tool IN FULL with the file tools. Author its classification verdict in the
   authored table that file's own rule maintains — the verdict written from the reading, its
   ground stated in the entry. Re-run `--check`; it MUST pass. **STOP if still red.**
3. Re-run the guard runner. **A2's check:** its STOP names exactly the two tools the inventory
   batch's close names. Otherwise STOP-and-report.
4. Read EACH of the two tools in full; author each one's invocation in the runner's authored
   invocation table, from the reading. Re-run the runner: it MUST now report **exactly one red —
   the [[OI-372]] FAIL — and no STOP.** Regenerate `tools/audit/guard_state.json` by its own
   generator and confirm it re-derives on a second run.
5. Flip [[OI-372]]? **NO — untouched.** Flip [[OI-373]]'s INDEX row to resolved with provenance
   (this task, this date, this dispatch); its detail file gains the dated resolution note and
   never a status. No other row is touched.
6. Commit as one commit naming its own act and citing ruling §5. Push. Verify at the object.

**Registered expectation E2:** the end-state guard run reports one FAIL ([[OI-372]]), zero
STOPs, and both runs of the state generator derive line-identical artifacts.

## Task 3 — the class-1 construction-evidence check (ruling §3.1)

Build `tools/audit/gen_test_construction_evidence.py` →
`tools/audit/test_construction_evidence.json`. Population: exactly the members of class
`our-analysis-tests-and-fixtures` read from `tools/audit/artifact_inventory.json` — never a
hand list. Per file, collect DERIVED evidence only:

- text references to specification documents (`ARCHITECTURE.md`, `docs/*.md` names, section
  marks) found in the file;
- the file's own commit history subjects (`git log --follow --format=%H %s -- <path>`), each
  commit's subject recorded verbatim;
- whether any history subject or in-file comment states derivation from a specification.

Classify per file, the vocabulary fixed by the ruling: **SPEC-DERIVED-EVIDENCE** (positive
evidence a specification was the source of expectations), **CODE-BUILT** (positive evidence of
construction beside/from the code, or — per the ruling's default — no establishable
construction evidence at all; the two sub-cases recorded distinctly in the artifact), and
nothing else. **The tool STOPs if any population member is unclassified.** No test is edited,
moved or run. Report the distribution and list every SPEC-DERIVED-EVIDENCE member BY NAME for
the user's follow-up ruling. Commit the tool and artifact; push.

**Registered expectation E3 (falsifiable, not load-bearing):** the large majority classify
CODE-BUILT; any SPEC-DERIVED-EVIDENCE member is a finding for the user, not a defect.

## Task 4 — the close

One `STATUS.md` pointer entry per task and nothing else in that file. The FULL close appended
to `cowork_away_returns.md` — including both guard-set states, every SHA, every expectation
graded, and every problem declared. The report file `cc_report_ruled_inventory_landing.md`
(trackable after Task 1 — no `-f`). Commit, push, verify at the object.

## What this batch does NOT do

No file is archived or retired (every flag awaits the caller-check, which is NOT this batch).
No mining, no findings ledger, no register filter, no phase drafting, no pilot. The remaining
449 ignored files are not landed. No verdict is authored for any tool this batch did not read.
[[OI-179]] stays OPEN and GATES. D-231 and #8 stand.
