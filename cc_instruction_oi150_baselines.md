# CC dispatch — OI-150: build at HEAD, run both suites, and re-stamp the baselines from those runs

> **Status: ACTIVE DISPATCH, written 2026-08-13 (Cowork), at a verified STOP** — the previous batch
> completed and its four commits, together with the four whose hashes it supplied, are verified by
> Cowork at the objects: no `src/`, no golden, nothing under `tools/corpus/` or
> `tools/robust_stop/`, tip on `origin/master`. **The declared verification gap is closed.** Nothing
> is running.
>
> **★ SECOND OF THE FIVE RATIFIED ACTS.** The user ratified the ordering: the false-statements pass
> first (done), **OI-150 second**, the `docs/scoring_model.md` pass third, the apparatus pair split,
> OI-207 alone and last. **OI-150's ground for second place is #13** — it is the only act on the list
> that can return a surprise, and a surprise found early has room while one found last does not —
> and **#19**, since a stale baseline is currently trusted rather than established.
>
> **Read IN FULL, and read FIRST:** `open_items/OI-150.md` END TO END; `BUILD_AND_TEST.md`'s
> baseline lines; `CLAUDE.md`'s build-and-test section.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_oi150_baselines.md`. Acts dated from the
> clock; **no positional count anywhere** (D-307, D-432); cite rulings by number, not by date.
>
> **★ All standing rules as adopted.** D-253 in every dialect. Hold-don't-guess. **This dispatch
> BUILDS and RUNS TESTS, which the standing commands authorize — and it changes nothing they
> measure: no `src/` edit, no golden refreshed, no corpus of scores touched, nothing under
> `tools/corpus/` or `tools/robust_stop/`, no behaviour change, no fix to inference, no design.**
> D-231 and #8 stand. **Phase 1's completion statement is not written, not drafted and not partially
> written.** Commit and push per task boundary; `origin` only.

## 0a. THE PREMISE LEDGER (#17a)

**FACT — verified by Cowork at the objects.** The eight commits above and their changed paths.
OI-150's act in the sizing artifact's own words: *"Build at HEAD, run both suites, re-stamp both
`BUILD_AND_TEST.md` baselines from those runs, and make the notation line name the four
key-emission cases that fail by design."*

**FACT — asserted by the ROW and NOT verified by anyone:** that exactly four key-emission cases
fail by design. **Checked at A2 before it is written anywhere.**

**ASSUMPTION — each checked BEFORE the act resting on it; a refutation is a STOP.**

- **A1.** **THE VALUES ARE MEASURED, NEVER CARRIED.** Every number written into
  `BUILD_AND_TEST.md` comes from **this batch's own runs**. *Check: no value is taken from the row,
  from a previous report, or from the file's existing text. **A wave declined this act once already
  precisely because copying figures forward would be the transcription D-431 forbids** — that
  refusal was correct and must not be undone by this one.*
- **A2.** The expected-failure set is **established at the run**, not taken from the row. *Check:
  name each failing case from this batch's own output. **If the count or the identities differ from
  the row's, that is a finding and a STOP**, not a discrepancy to smooth.*
- **A3.** **A FAILING SUITE IS A STOP (#13).** *Check: any failure that is not in the
  established-by-design set halts the batch and is reported with its output. It is not worked
  around, not re-stamped around, and not diagnosed — surfacing it is the whole of what is owed.*
- **A4.** The build and the runs **change nothing they measure**. *Check: the working tree carries
  no `src/`, golden, `tools/corpus/` or `tools/robust_stop/` modification at any point; if a run
  writes into any of those, STOP.*

## 0b. THE TASKS, IN ORDER

**Task 1 — build at HEAD and run both suites (A1, A2, A3, A4). FIRST, with nothing in front of
it.** It cannot be stopped partway and it is the only act here that can surprise, which is D-670's
ordering and #13's reason together. Record each run's outcome and the identity of every failing
case. **Do not edit anything in this task.** Commit nothing yet; if a STOP fires, write it to
`cowork_away_returns.md` and halt.

**Task 2 — re-stamp the baselines from those runs.** Both `BUILD_AND_TEST.md` baselines, written
from Task 1's own output, and the notation line made to name the by-design failing cases
established at A2. **Former wording preserved in place (#12).** Then flip **OI-150** with
provenance if and only if its own closing conditions are met, and report which condition each
half met; if any is unmet, leave it open and say which. Commit and push.

**Task 3 — one read-only report, no act.** After the false-statements pass performed OI-315's and
OI-321's acts, **were those two rows flipped?** Read their INDEX rows and report the state.
**Flip neither here** — if an act is complete and its row still open, that is a finding for the
user, not a correction to make inside a dispatch sent for something else.

**Task 4 — the close.** One `STATUS.md` pointer entry per task, nothing else in that file. Append
the close to `cowork_away_returns.md`. **Report at the objects, with commit hashes.**

## 0c. WHAT IS DELIBERATELY NOT DONE

**No golden is refreshed**, whatever the runs show — a golden refresh is a separate ratified act and
its own gate. **No test is changed, skipped or marked.** **No diagnosis of any failure** — surfacing
is the whole of the obligation. The `docs/scoring_model.md` pass, OI-274's banner half and OI-207
are ratified for later and are not started. **CC's two declared findings — the stale triage clauses
and the two discard-record routes — are held, not acted on**; the second is with the user because
Ruling 69 made discard records load-bearing for the gate. OI-179 stays OPEN and GATES.

## 0d. STOP RULES

Halt with a STOP in `cowork_away_returns.md` if: the build fails; any suite reports a failure
outside the by-design set established at A2; the by-design count or identities differ from the
row's; a run modifies `src/`, a golden, `tools/corpus/` or `tools/robust_stop/`; a value would have
to be carried rather than measured; or a guard goes red for a cause that is neither this dispatch's
own edits nor already recorded — the two standing reds are recorded and are not that.

---

*Provenance: Cowork, 2026-08-13. Second of five acts the user ratified on a surface carrying five
mutually exclusive first-acts, each pro and con naming its principle and each rated against the
ultimate objective. Self-check run before release (D-434).*
