# CC dispatch — remove the second ignore rule, perform the [[OI-373]] clearing act, fix the guard-staleness cause at its printing side, and land the return rulings

> **Dispatch (Cowork, 2026-08-15).** Executes the rulings of
> `cowork_rulings_2026_08_15_batch_return.md` §2, §3 and §4 (§1 orders no act of the coding
> side). Written at a verified STOP; nothing else is running.
> **Read first, in full:** that ruling record; then `cowork_rulings_2026_08_15_inventory_sitting.md`;
> then your own `cc_report_ruled_inventory_landing.md`; then `cowork_handoff.md`'s seventeenth
> entry block. The standing bars are unchanged and bind this batch whole: **no `src/` edit, no
> golden, no test changed, moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`,
> no measurement of the analysis, no design, no repair, no decisions-register entry** (the
> filtering ruling stands), **no open-items row created or flipped except exactly where Task 2
> orders it.**
>
> **Commit-and-push per task. Run the FULL guard set BEFORE the first edit and again at the
> end; record both states.** The expected start state is the previous batch's end state — one
> FAIL ([[OI-372]]'s tool), zero STOPs, the committed `guard_state.json` reported STALE for the
> diagnosed reason — **a different start state is a STOP-and-report.** Verify every commit after
> the fact at the object (`git diff-tree --no-commit-id --name-only -r <sha>`) and record the
> SHAs in the close. Reserved-word conventions bind all new prose.

## Ruling ledger (what this batch may rest on — quoted at the record, not paraphrased)

- **§2:** the coherent one-act version of the [[OI-373]] clearing is permitted under D-436 for
  this act alone: the authored discard pointer retired WHOLE into a retired block (added if the
  mechanism does not yet carry one) with reason, date and dispatch name — nothing destroyed
  (#12) — and the INDEX row flipped RESOLVED with provenance in the same act; the refusal logic
  not otherwise changed; after the act the standing reds are ONE ([[OI-372]]).
- **§3:** `.gitignore`'s `/cc_instruction_*.md` line is removed; **no other line moves**;
  `/cc_e2d_*.md` and `ai-assistant/CC_INSTRUCTION_*.md` are NOT ruled on; the newly visible
  untracked files are NOT landed.
- **§4:** `gen_artifact_inventory.py`'s live half changes what it prints so its commit-hash
  line carries the exact shape the runner's EXISTING normalization reaches, the pattern read at
  the runner before the edit; **the runner's normalization is NOT widened.**

## Premise ledger

- **FACT** — `/cc_instruction_*.md` stands at `.gitignore` line 116 in the tree at `91ea25b20d`
  (verified at the object 2026-08-15, Cowork).
- **FACT** — `guard_state.json` at `4a65a40e03` reads run 48, passing 47, failing 1, the failing
  tool being [[OI-372]]'s; its `not_run` set of four is standing, present identically in the
  pre-batch committed state with authored reasons (verified at the objects 2026-08-15, Cowork).
- **ASSUMPTION A1** — `gen_discard_records.py`'s authored table carries exactly ONE discard
  pointer naming [[OI-373]], and no other row's pointer is touched by the act. **Check ordered
  before the act (Task 2 step 1); a different count is a STOP-and-report, never a guess.**
- **ASSUMPTION A2** — the runner's normalization reaches a line carrying the literal word `HEAD`
  followed by a sha (the shape the previous report's §4.a names). **Check ordered: READ the
  pattern at `gen_guard_state.py` before editing; the printed shape is matched to the pattern AS
  READ, never to this assumption. Record the pattern verbatim in the close.**
- **ASSUMPTION A3** — the commit-hash line is the ONLY cross-commit staleness cause. The
  previous report's §4.a names a second candidate: the untracked-appendix line, which varies
  with the working tree. **If staleness persists after the fix, STOP-and-report the differing
  lines verbatim; never regenerate in a loop to make the check pass.**

## Task 0 — land the writing-side records

Commit, in ONE commit whose message names its own act, exactly these TWO paths and no third:

1. `cowork_rulings_2026_08_15_batch_return.md` (new)
2. `cc_instruction_batch_return_rulings.md` (this file; staged with `-f` — genuinely the last
   time: Task 1 removes the rule that requires it)

**`cowork_handoff.md` is NOT part of this landing** — its next entry block is written at the
writing side's session close, not now. If it shows as modified on disk, STOP-and-report. Verify
at the index through the sanctioned enumeration, then after the fact at the object. Push.

**Registered expectation E0:** `git diff-tree` on the Task 0 commit lists exactly 2 paths.

## Task 1 — the second ignore rule (ruling §3)

1. Edit `.gitignore`: delete the line whose entire content is `/cc_instruction_*.md`. **No other
   line moves.**
2. Commit as ONE commit naming its own act and citing ruling §3 — exactly one path. Push. Verify
   at the object.
3. Record IN THE CLOSE (not in any commit): how many previously ignored `cc_instruction_*.md` /
   `cc_e2d_*.md`-family files now show untracked, **none of which this batch lands.**

**Registered expectation E1:** path count 1; the commit's diff to `.gitignore` deletes exactly
one line and adds none; afterwards `git check-ignore -q cc_instruction_hypothetical_future.md`
exits non-matching (a hypothetical name — the test is the rule's absence, not any file).

## Task 2 — the [[OI-373]] clearing act (ruling §2)

1. Read `tools/audit/gen_discard_records.py` IN FULL with the file tools. **A1's check:** exactly
   one authored discard pointer names [[OI-373]]. Otherwise STOP-and-report.
2. In ONE act: move that pointer WHOLE into a retired block (adding the block if the mechanism
   does not carry one), with the reason it leaves — the row's substance discharged 2026-08-15 by
   the ruled invocations; the discard verdict superseded by the ruled resolution — the date, and
   this dispatch's name. The refusal logic that caught the incoherence is not otherwise changed.
3. Flip [[OI-373]]'s INDEX row to RESOLVED with provenance (this dispatch, this date, ruling
   §2); its detail file gains the dated remark and never a status. **No other row is touched.**
4. Run `gen_discard_records.py --check`: MUST pass. Run the full guard set: MUST report exactly
   one FAIL ([[OI-372]]'s tool) and zero STOPs. **STOP on any difference.**
5. Commit as ONE commit naming its own act and citing ruling §2. Push. Verify at the object.

**Registered expectation E2:** step 4's end state exactly as stated, and [[OI-373]]'s INDEX row's
leading status token is RESOLVED.

## Task 3 — the staleness fix at the printing side (ruling §4)

1. Read IN FULL with the file tools: `gen_guard_state.py`'s normalization (the pattern and the
   comment beside it) and `tools/audit/gen_artifact_inventory.py`'s live half. **A2's check
   applies; record the pattern verbatim in the close.**
2. Edit `gen_artifact_inventory.py` so the line printing the resolved commit hash carries the
   exact shape that pattern reaches. Nothing else about the tool's behaviour changes. **The
   runner is NOT edited.**
3. Run the inventory tool's `--check` and the full guard set. Regenerate `guard_state.json` and
   `guard_classification.json` by their own generators; confirm each re-derives on a second run.
4. Commit as ONE commit naming its own act and citing ruling §4. Push. Verify at the object.

**Registered expectation E3, two limbs:** *(hard)* after this batch's FINAL commit, a fresh
runner `--check` no longer shows the commit-hash line as a difference — demonstrated by running
it and reading what it prints, not inferred; *(report)* whether ANY staleness remains at that
tree, and if so which line, quoted verbatim (A3's check).

## Task 4 — the close

One `STATUS.md` pointer entry per task and nothing else in that file. The FULL close appended to
`cowork_away_returns.md` — both guard-set states, every SHA, every expectation graded, every
problem declared. The report file `cc_report_batch_return_rulings.md` — **the first report to
land without `-f`.** Commit, push, verify at the object.

## What this batch does NOT do

- **No file archived, retired, renamed or deleted** — beyond the one authored pointer's move to
  its retired block, which destroys nothing. The newly visible untracked instruction files are
  NOT landed; the remaining ignored files are NOT landed; **the caller-check is NOT started.**
- **No mining, no findings ledger, no register filter, no phase drafting, no pilot, no
  write-back of ruled verdicts onto the generated surface.**
- **No edit to `gen_guard_state.py`**, no edit to `OPEN_ITEMS.md` beyond the one row Task 2
  orders, **no verdict or change authored for any tool this batch did not read in full.**
- **[[OI-372]] stays exactly as found. [[OI-179]] stays OPEN and GATES. D-231 and #8 stand.**
