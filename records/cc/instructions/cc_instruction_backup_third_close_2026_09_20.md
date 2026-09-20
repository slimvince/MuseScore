# CC INSTRUCTION — the third backup's CLOSE: commit the close's own edits and the records left beside them, by explicit path, and push, 2026-09-20

**What this is.** The third backup's task commit `4d248dd096f0960021e622160a962d48476b8eb5` is made and is
pushed. What is NOT done is the close. The batch that made the task commit ran its close's steps 1 to 3 —
the `STATUS.md` entry, the forward bound, the two measurements — and then stopped at its step 4, whose
condition is an EQUALITY between two guard-set captures
(`records/cc/reports/cc_report_backup_third_commit_and_push_2026_09_20.md` §8(b)). Two guards had moved FAIL
to PASS, which an equality forbids and a non-regression test allows. **So the close's edits stand in the
working tree, uncommitted, and this dispatch commits them.**

**The one thing this dispatch changes in how a close is done: its guard step is a NON-REGRESSION TEST.** No
guard that PASSED at this batch's opening capture may FAIL at its closing capture; a guard that moves to
passing is allowed and is reported. **This is written ahead of the batch, in a dispatch of its own, with
nothing staged and no diff live** — which is what principle **#22** requires of a gate written for a change
it did not anticipate. It is not an amendment made under the pressure of a live diff.

**The forward bound is NOT run and no new `STATUS.md` entry is written.** The entry standing at the top of
`STATUS.md` is this line's entry, the bound for it ran in that same act, and
`gen_status_batch_bound.py --check` exited 0 there. This batch commits that state; it does not repeat it.
The one `STATUS.md` edit this batch makes is at Task 1, and is the single sentence the close commit makes
false.

## THE ROUTE RULE

- Working-tree file content is read and written with the file tools, never through a shell (`D-253`).
- **Add no command of your own.** Any guard refusal → STOP.
- Run **no build, no test, no measurement of the analysis, no forward bound**, and no generator other than
  the two Task 2 names.
- **Never `git add -A`, `git add .`, `git add -u`, or any glob or directory pathspec.** Every path is staged
  by explicit path.
- **Repair nothing that is failing.** In particular, `tools/audit/gen_derivation_boot_pack.py --check` is
  expected to fail and **no record the writing side read establishes why**. It is reported and left exactly
  as it stands. Do not run it with any other argument, do not touch the frozen derivation boot pack, and do
  not touch `tools/audit/derivation_boot_pack.json`.
- The ordinary session-start read still binds you (P-1, `D-230`).
- **The writing side does not touch this dispatch, or any file named in it, while this batch runs** (`D-251`,
  and the measured failure behind it: a session that edited a live dispatch across four turns had CC observe
  three states of it). Task 0(a) pins this file to a git blob so that every later read of it is of one object.

## THE LIST — the stable members, each with the figure to check it by

These nine are on disk now and this batch's own orders do not touch their content. Sizes and modification
times were read by the writing side on 2026-09-20 at folder listings of `records/cowork/handoff/`,
`records/cc/instructions/`, `records/cc/reports/` and `tools/audit/`, and — for the two root files, the
repository root not being listed — at a staging call of each file.

| # | Member | Bytes | Modification time at the listing |
|---|---|---|---|
| 1 | `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixteen.md` | 8515 | 1789902200075 |
| 2 | `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventeen.md` | 8554 | 1789902750230 |
| 3 | `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_eighteen.md` | 14890 | 1789920242075 |
| 4 | `records/cc/instructions/cc_instruction_backup_third_push_only_2026_09_20.md` | 7428 | 1789919534816 |
| 5 | `records/cc/reports/cc_report_backup_third_commit_and_push_2026_09_20.md` | 32034 | 1789904966981 |
| 6 | `records/cc/reports/cc_report_backup_third_push_only_2026_09_20.md` | 5292 | 1789919737248 |
| 7 | `STATUS_ARCHIVE.md` | 1924957 | 1789904311662 |
| 8 | `tools/audit/gen_status_batch_bound.py` | 78109 | 1789904304216 |
| 9 | `tools/audit/status_batch_bound.json` | 20789 | 1789904311698 |

**Expected record kinds.** Members 1 to 6 untracked (`??`). Members 7, 8 and 9 modified (` M`). **A member
whose record is of the other kind is reported and is still staged. A member with NO record is reported,
Glob-checked for existence, and NOT staged** — a file that exists with no record is either already committed
as it stands or ignored, and this batch adds no command to tell which. **A member that does not exist on
disk → STOP.**

## THE MOVING MEMBERS — written by this batch's own orders, so no figure is given for them

| # | Member | Written by |
|---|---|---|
| 10 | `STATUS.md` | Task 1, at the one site named there |
| 11 | `tools/audit/session_start_read_size.json` | Task 2 |
| 12 | `tools/audit/defense_share.json` | Task 2 |
| 13 | `records/cc/instructions/cc_instruction_backup_third_close_2026_09_20.md` | this dispatch, landed by the writing side before hand-over |

**Expected record kinds.** Member 10 modified (` M`), the previous close having edited it. **Members 11 and
12 may carry a record or none**, and Task 2 rewrites them either way. Member 13 untracked (`??`).

**This batch's own report is NOT a member.** It is written at Task 6, after the close commit, so it cannot
be in it — which is the same position the two reports this batch commits were in when they were written.
**The next batch commits it.**

## THE ONE CONDITIONAL MEMBER

**`tools/audit/changed_paths_establishment.json`.** `tools/audit/gen_guard_state.py`'s authored invocation
list runs `tools/audit/changed_paths.py --establish`. That row of the list carries its own description
string, which reads *"the changed-path enumeration tool, measured against a known set; it has no verify-only
mode, and writes its establishment artifact on every run"* — read at `tools/audit/gen_guard_state.py` by the
writing side, and the ground for what follows. **On that description, each guard-set run rewrites this
file**, Task 0(g)'s and Task 3's among them. The writing side did not measure the rewrite; whether it
changes the file's CONTENT is unknown here, this side having no shell and resolving no git object. The
file's modification time at the `tools/audit/` listing (1789904348002) is about twelve seconds later than
`tools/audit/defense_share.json`'s (1789904336076), which the previous close's step 3 wrote — which fits the
description and does not establish it.

**So: it is staged if and only if it carries a record at Task 4's enumeration, and its absence from that
enumeration is equally correct.** Report which of the two happened. **Do not run `changed_paths.py
--establish` on its own to find out.**

## NOT IN THIS BATCH — named so an omission is not mistaken for a miss

- **The Cowork handoff entry this sitting is writing**, expected at
  `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nineteen.md`. **The writing side may land it
  before or after this dispatch is handed over**, so a record at that path may or may not appear. **If one
  appears in either enumeration, report it and do not stage it.** Its absence is equally correct. This is the
  shape the previous batch used for entry 216, at its own Task 0(d)(v).
- **This batch's own report**, `records/cc/reports/cc_report_backup_third_close_2026_09_20.md`, written at
  Task 6 after the close commit. It is reported as created and is not staged.
- Held back until the user says whether they belong in a public fork, **as the previous batch's dispatch
  holds them** — on handoff entry 188 §5 for the five directories, and on the third 2026-09-16 dispatch's own
  recorded ground for the `.mscx` (both relayed through that dispatch; this side read entry 188 §5 and did
  not open the 2026-09-16 dispatch): `Claude outputs/`, `Codex research inventory/`, `scratch_artifacts/`,
  `external resarch summary/`, `docs/research_papers/polyph9-release/`, and
  `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`.
- `tools/audit/claude_md_finer_archive.json`, whose modification's cause is unknown: the third backup left
  it unstaged, and the second backup's report records it as a ` M` record on 2026-09-19 (relayed through the
  third backup's report §2(iv)).
- Any root `cowork_*.md` document: the writing side listed no repository root.

## NEVER STAGED

`tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; `tools/audit/claude_md_finer_archive.json`;
`tools/audit/guard_state.json`; `tools/audit/guard_classification.json`;
`tools/audit/derivation_boot_pack.json`; anything under `tools/audit/derivation_boot_pack/`; anything under
`src/`; any `.pdf`; anything under `docs/research_papers/`; and any path not named in THE LIST, THE MOVING
MEMBERS or THE ONE CONDITIONAL MEMBER. **Open nothing under `docs/research_papers/`, and do not open the
`.mscx` file.**

## TASK 0 — the state

**(a)** `git hash-object -w` on this dispatch. Record the identity. Every later read of this dispatch is
`git cat-file blob <that identity>`.

**(b)** `git rev-parse --abbrev-ref HEAD` must print `master` and `git rev-parse HEAD` must print exactly

```
4d248dd096f0960021e622160a962d48476b8eb5
```

**Any other value → STOP**, and report the value printed. **This is both the task commit and this close's
own base**: nothing has been committed on `master` since it.

**(c)** `git rev-parse refs/remotes/origin/master` must print the same forty characters. **A different value
→ STOP**, and report it. *(Checked by the writing side at `.git/refs/heads/master` and
`.git/refs/remotes/origin/master` with the file tools on 2026-09-20: both read that value. That it was the
push-only batch that put it at the remote is that batch's own account, relayed.)*

**(d)** `git remote -v`. `origin` must be `https://github.com/slimvince/MuseScore` for **fetch** and for
**push**, and `upstream`'s push must be disabled, else STOP. *(Relayed: the previous two dispatches record
the writing side reading this at `.git/config` on 2026-09-20. **This side did not re-read `.git/config`**,
which is why it is a check CC runs rather than a figure carried.)*

**(e)** `python tools/audit/changed_paths.py --staged`, captured. It must list **no path record**, else
STOP, unstage nothing, and report the capture whole.

**(f)** `python tools/audit/changed_paths.py`, captured. Then, reading the capture with Read or Grep:

- Look up each of members 1 to 12 in the capture against the expected kinds above, and member 13 (this
  dispatch, expected `??`). **Members 11 and 12 may carry a record or none at this point; either is
  correct, and Task 2 rewrites them regardless.**
- **Every record under `records/cc/` must be `??`, and its path must be member 4, 5, 6 or 13.** Any other
  record under `records/cc/`, of any kind → STOP.
- **Every record under `records/cowork/handoff/` must be member 1, 2 or 3, or the entry named under NOT IN
  THIS BATCH.** Any other record there → STOP.
- **A modified, deleted or renamed record under `src/` → STOP.** An untracked record under `src/` is
  reported and is not a STOP.
- Every ` M` record not on THE LIST or among THE MOVING MEMBERS is named in the report.
  `tools/audit/claude_md_finer_archive.json` is expected among them and is not staged and not a STOP.
- Records elsewhere are not listed one by one; the capture's identity stands for them.

**(g) The opening guard capture — the reference for Task 3.** `python tools/audit/gen_guard_state.py
--check`, captured **whole**. The run may exit 1 when the failing set is not empty; **that exit code is not
a STOP.** Report its counts line. **Do not compare it to any earlier batch's counts line and do not act on
any difference**: this capture's only job is to be the reference Task 3 measures against.

## TASK 1 — the one sentence the close commit makes false in `STATUS.md`

`STATUS.md`'s topmost entry ends by saying that this file's entry, the forward bound, the two measurement
artifacts and both batches' reports **remain uncommitted**. That is true as this dispatch is written and
false at this batch's close commit, and #10 forbids the record stating something false about itself.
**ONE edit, with the file tools, and only this one.**

**Find this text, which the writing side read as standing exactly once in the file:**

```
the two measurement artifacts and both batches' reports remain uncommitted.
```

**Replace it with exactly:**

```
the two measurement artifacts and both batches' reports remain uncommitted. ★ **AND THE CLOSE IS TAKEN BY `records/cc/instructions/cc_instruction_backup_third_close_2026_09_20.md`, A DISPATCH OF ITS OWN** — written after the user's ruling of 2026-09-20 that the push is taken first and the close finished separately, and with its guard step written as a NON-REGRESSION test instead of the equality that stopped the first close (**#22**: the gate is written ahead of the batch, in a dispatch of its own, with nothing staged). **The sentence above stands as written of the state it described (#12)**, and that batch commits those files together with the handoff entries and the push-only dispatch standing uncommitted beside them. **It writes no entry of its own and runs no forward bound**: this entry is the latest batch's, and the bound for it ran in the act recorded above. Per the OI-222 pointer convention the whole of that batch is `records/cc/reports/cc_report_backup_third_close_2026_09_20.md`, and no value is restated here (**D-431**).
```

Nothing else in `STATUS.md` changes: **no entry is written, demoted, moved, archived or re-dated, the
`Last updated: ` prefix stays where it is, the two nameless 2026-09-02 entries stay where they are, and the
forward bound is NOT run.** **If that text is not found, or is found more than once → STOP**, edit nothing,
and report what was found.

## TASK 2 — the two measurements, in this order

`python tools/audit/gen_session_start_read_size.py`, then `python tools/audit/gen_defense_share.py`. **Any
STOP or FAIL printed → STOP, no commit.** No value either printed is restated in the report (`D-431`);
report that each exited 0 and wrote its artifact.

*Why these two and why after Task 1, stated so the order is not taken for habit:* `STATUS.md` is a member
of `gen_session_start_read_size.py`'s measured set — read by the writing side at that tool's `MEMBERS`
table — so Task 1's edit makes its artifact stale. **`gen_defense_share.py`'s text does not contain the
literal `STATUS.md` at all**, searched by the writing side, **and the writing side did not establish why
its `--check` guard was failing at the previous batch's opening capture**; it is run here because the
previous close's own step 3 ran it in this sequence and its `--check` passed afterwards, which is a
recorded act and not a causal claim of this side's.

## TASK 3 — the guard step, as a NON-REGRESSION TEST

`python tools/audit/gen_guard_state.py --check`, captured **whole**. The exit code is not by itself a STOP.
Compare this capture against Task 0(g)'s, **entry by entry, in the order each prints**:

1. **The set of guards named, and each one's position in the listing, must be identical in the two
   captures.** A guard named in one and not the other → **STOP**.
2. **The set of guards reported as not run must be identical.** Any difference → **STOP**.
3. **A guard that reads PASS at Task 0(g) must read PASS here.** Any PASS that is not PASS here →
   **STOP, no commit, no push.** This is the non-regression condition and it is the whole of the test.
4. **A guard that reads FAIL at Task 0(g) may read FAIL or PASS here.** Both are admitted. **Every guard
   that moves FAIL to PASS is named in the report**, with nothing inferred about why it moved.
5. Report both counts lines and every differing guard by name. **A difference in the counts line is not by
   itself a STOP**; conditions 1 to 3 are.

**`tools/audit/gen_derivation_boot_pack.py --check` is expected to read FAIL in both captures.** Under
condition 4 that is admitted. **Report it as still failing and change nothing about it.** Its cause is
established by no side, and handoff entry 218 §3 item 2 holds it as work of its own.

## TASK 4 — the enumeration, the checks, and the close commit

**(a)** `python tools/audit/changed_paths.py`, captured. **This capture, not Task 0(f)'s, is the one the
staging set is derived from**, both guard runs having rewritten
`tools/audit/changed_paths_establishment.json` since. Apply every STOP rule of Task 0(f) to it again, and
the missing-member STOP of THE LIST.

**THE STAGING SET** is: members 1 to 13 that this capture admits, **plus**
`tools/audit/changed_paths_establishment.json` if and only if it carries a record in this capture. **It
contains no fourteenth member: this batch's report does not exist yet.**

**(b) The size check, by git object and not by a shell read.** For members 1 to 9 only:
`git hash-object -w --no-filters <path>`, then `git cat-file -s <the identity it printed>`. **The size
printed must equal the figure on THE LIST. Any difference → STOP, stage nothing, and report every size
found.** The figures are of the bytes on disk, which is what `--no-filters` hashes; no member's line endings
were measured by the writing side. **Members 10 to 13 and the conditional member get no size check, because
this batch's own orders write them**, and that is a declared bound, not a check performed.

**(c) The tail check, with the Read file tool.** For members 1 to 6 only — the six untracked records. Four
of them (1 to 4) reached disk through the Cowork bridge, whose measured fault is why this check exists;
**members 5 and 6 were written by CC and are checked here anyway**, a check being no worse for being run
where the fault it guards against has not been shown. A Grep count of lines matching
`^` gives the line count; Read from five lines before it. **The last non-empty line must be ordinary text.
A file ending in NUL bytes, or an empty file → STOP.** Report the first 60 characters of each. **Members 7
to 13 get no tail check: 7 to 9 were written by tools in the previous batch's own recorded act, and 10 to
13 are written by this batch's orders.** A declared bound, not a check performed.

**(d) Stage by explicit path**, one `git add -- <path>` per member or one command naming them all. **No
directory pathspec, no glob, no `-A`, no `.`, no `-u`.** A line-ending warning printed by `git add` is
reported (the count as the tool printed it, and the first and last warning in full) and is not a STOP.

**(e)** `python tools/audit/changed_paths.py --staged`, captured. **It must show exactly THE STAGING SET
and nothing else.** Anything else → `git restore --staged -- <every staged path>` and **STOP**.

**(f) Commit** with this message, verbatim (the standing `Co-Authored-By` trailer may follow it):

```
Close: the third backup, with the guard step as a non-regression test

Commits the close's own edits left uncommitted when the first close stopped at
its equality guard - STATUS.md, STATUS_ARCHIVE.md, the forward bound's tool and
artifact, the two measurement artifacts - together with both batches' reports,
the push-only dispatch, handoff entries 216 to 218 and this dispatch. No file
content is changed by this batch except STATUS.md at one site, the two artifacts
its own orders regenerate, and the establishment artifact the guard set rewrites
on every run.
Dispatch: records/cc/instructions/cc_instruction_backup_third_close_2026_09_20.md
```

**(g)** Record the hash `git commit` printed, then run `git rev-parse HEAD` once. The forty characters it
prints must begin with the printed hash, else STOP. That value is the **CLOSE COMMIT**.

**(h)** `git diff --name-status 4d248dd096f0960021e622160a962d48476b8eb5 <CLOSE COMMIT>`. **It must name
exactly THE STAGING SET and nothing else.** Otherwise → **STOP, no push**, and report it whole.

## TASK 5 — the push

`git push origin master`. **Capture the whole output and report it verbatim.**

- Never `--force`, never `--force-with-lease`, never `upstream`, no other branch, no other refspec, no
  `--tags`.
- **If the push is rejected, or fails for any reason: report the output verbatim and STOP.** No pull, no
  fetch, no merge, no rebase, no retry with other options, and no second push.

Then `git rev-parse refs/remotes/origin/master` must print the CLOSE COMMIT. Report what it prints. **A
different value → report it and STOP.** *(The writing side verifies this independently at
`.git/refs/remotes/origin/master` with the file tools.)*

## TASK 6 — the report

Write with the Write file tool `records/cc/reports/cc_report_backup_third_close_2026_09_20.md`. Glob first;
**if it already exists → STOP.** It carries, in this order:

1. This dispatch's blob identity, from Task 0(a).
2. Task 0(b) to (e), each as the command printed it.
3. Task 0(f): the capture identity; each member's record kind against the expected kind; every record under
   `records/cc/` and `records/cowork/handoff/`; every ` M` record not staged; whether the entry named under
   NOT IN THIS BATCH appeared.
4. Task 0(g): the capture identity and its counts line.
5. Task 1: the text found, the text written, and that it stood exactly once.
6. Task 2: that each generator exited 0 and wrote its artifact, with no value restated.
7. **Task 3 in full**: both capture identities, both counts lines, the result of each of conditions 1 to 4,
   every guard that moved FAIL to PASS by name, and that
   `tools/audit/gen_derivation_boot_pack.py --check` still fails.
8. Task 4: the capture identity; whether `tools/audit/changed_paths_establishment.json` carried a record;
   every size from (b) against its figure; every tail line from (c); (d)'s warning count with its first and
   last warning; (e)'s capture; the CLOSE COMMIT; and (h)'s output.
9. Task 5's output verbatim, and the ref value.
10. What was not done: no forward bound, no `STATUS.md` entry written, no build, no test, no measurement of
    the analysis, no repair of any failing guard, nothing under NEVER STAGED touched.

**Write in the report, before the push, everything known before it**, so that an interrupted chat reply
loses only the push line. Name members; state a total only as a sum of named members or as a number a tool
printed (`D-431`).

**This report is itself uncommitted** — it is written after the close commit, and the NEXT batch commits it,
exactly as this batch commits the previous two reports.

At the foot of the chat reply: the report's path, this dispatch's blob identity, the CLOSE COMMIT, whether
any guard moved, and the push result verbatim.

## THE FOOTPRINT — what this batch's own orders touch, and nothing else

**Edited:** `STATUS.md`, at the one site Task 1 names. **Written by the two generators:**
`tools/audit/session_start_read_size.json` and `tools/audit/defense_share.json`. **Written by the guard set
on each of its two runs:** `tools/audit/changed_paths_establishment.json`. **Created:** this batch's report.
**Committed as they stand, content unchanged:** every other member of THE STAGING SET. **Pushed:** the close
commit.

**No tool source is edited by this batch.** `tools/audit/gen_status_batch_bound.py` is member 8: it is
COMMITTED as it stands, carrying the previous batch's own re-aiming, and nothing here touches its text. This
batch runs no forward bound, so the standing exception for that tool's per-batch re-aiming (Ruling 5 of
`records/cowork/rulings/cowork_rulings_2026_08_26_amendment_landing_sitting.md`) does not arise and is not
used. No `src/` file, no build, no test, no golden, no corpus, nothing under
`tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis, no paper opened, no extract edited,
no governing document amended beyond `STATUS.md` at one site, no open-items row created, flipped or
discarded, no decisions-register entry and no `D-NNN` allocated.

## DECLARED BY THE WRITING SIDE

- **Checked at the files on 2026-09-20, with the file tools and no shell:**
  - `.git/refs/heads/master` and `.git/refs/remotes/origin/master`, both reading
    `4d248dd096f0960021e622160a962d48476b8eb5`;
  - every figure on THE LIST, at folder listings of `records/cowork/handoff/`, `records/cc/reports/` and
    `tools/audit/`, and at a staging call for `STATUS_ARCHIVE.md`. **`records/cc/instructions/` was listed
    too, and its result exceeded the tool's inline limit, was saved to a file by the tool and was searched
    with Grep rather than read whole** — the same departure handoff entry 218 §6 declares for the same
    directory, and the ground for member 4's figure;
  - `STATUS.md` whole, and that Task 1's anchor text stands there exactly once;
  - `tools/audit/gen_status_batch_bound.py` at its six authored inputs and the comment block above
    `PREVIOUS_AIMINGS`: the aiming on disk is the third backup's own, `BASE_COMMIT` being the task commit;
  - `tools/audit/gen_guard_state.py` at its authored invocation list, for the `changed_paths.py --establish`
    row and that row's own comment;
  - `tools/audit/gen_session_start_read_size.py` at its `MEMBERS` table, where `STATUS.md` stands;
  - `tools/audit/gen_defense_share.py`, searched for `STATUS.md` with no match;
  - `tools/audit/changed_paths_establishment.json` whole;
  - the previous batch's dispatch at its Task 0 and Task 3, and its report whole;
  - the push-only dispatch and its report whole.
- **Relayed, not checked by this side:** everything the previous two reports state about their captures,
  their staged sets and the contents of the task commit; which members are tracked; and that the close's
  edits are uncommitted. **No git object was resolved by this side**, which has no shell — so every
  statement here about what is committed is the reports' and not this side's.
- **Not established by this side, and named rather than passed over:** why
  `tools/audit/gen_session_start_read_size.py --check`, `tools/audit/gen_defense_share.py --check` and
  `tools/audit/gen_derivation_boot_pack.py --check` began failing between the framework correction's close
  and the third backup's opening capture. The previous batch's report §3 records the same gap. **This
  dispatch repairs none of them and orders no investigation**; handoff entry 218 §3 item 2 holds the
  boot-pack one as work of its own.
- **A defect in handoff entry 218, found while writing this dispatch and named here because the dispatch
  departs from it.** That entry's §3 item 1 closes: *"The forward bound's `BASE_COMMIT` is then the close's
  own base, not `4d248dd096…`."* **The close's own base IS `4d248dd096…`** — nothing has been committed on
  `master` since the task commit, so this close commit sits directly on it, and the sentence sets two
  descriptions of one commit against each other. The bound is not re-run here for a different reason, stated
  at the head: this batch writes no entry of its own, so the forward clause — which moves *"the
  then-previous batch's entries, moved in the same act that writes this batch's own entries"*, as
  `tools/audit/gen_status_batch_bound.py`'s `MOVE_KIND` comment states it — has nothing to act on. The shape
  is the push-only dispatch's, one step earlier in the same line: it too edited `STATUS.md`, wrote no entry
  and ran no bound. **Whether a follow-on dispatch inside one line owes an entry of its own is a question
  this side did not find open anywhere in the record it read**; if the user reads it otherwise, that is a
  ruling and this dispatch is rewritten before it runs.
- **The `STATUS.md` anchor's uniqueness** was read at a staged copy of the file, which is a snapshot. Task 1
  re-checks it at the file and STOPs if it is absent or repeated.

## STOP CONDITIONS

- Any Task 0(b), (c), (d) or (e) mismatch.
- An unexpected record under `records/cc/`, `records/cowork/handoff/` or `src/`, at either enumeration.
- A member of THE LIST missing from disk.
- Task 1's anchor text absent, or present more than once.
- A STOP or FAIL printed by either generator at Task 2.
- **Task 3: a guard named in one capture and not the other; a change in the not-run set; or any guard that
  reads PASS at Task 0(g) and not PASS at Task 3.**
- Any size different from its figure, or any tail that is not ordinary text.
- Any staged path outside THE STAGING SET.
- `git diff --name-status` at Task 4(h) naming anything outside THE STAGING SET.
- The push rejected or failed, for any reason, or `refs/remotes/origin/master` not equal to the CLOSE COMMIT
  after it.
- The report's path already in use.
- Any guard refusal.
- **Any instruction here found false at the objects.**

On any STOP: undo nothing beyond the unstaging Task 4(e) orders, report every capture verbatim and every
value printed, and stop.
