# CC REPORT — the group gloss repaired, and L2's candidate list published whole (2026-09-05)

> **STATUS: REPORT.** Written by CC under `cc_instruction_l2_candidate_list_2026_09_05.md`, Tasks 0
> to 5. **No verdict was authored for any subject, nothing was withheld, no pack was rendered, no
> session was booted, no reading file was written, and no position is taken on any candidate.
> Nothing is recommended anywhere in this report.**

---

## 1. The tip at boot and the tip at close

Both read at **both ref files with the file tools** — `.git/refs/heads/master` and
`.git/refs/remotes/origin/master` — never through a shell and never from a push's own output.

| | `.git/refs/heads/master` | `.git/refs/remotes/origin/master` |
|---|---|---|
| **At boot** | `87fd4dea5c9e07a92ca7e3327a68e97a9e05f93e` | `87fd4dea5c9e07a92ca7e3327a68e97a9e05f93e` |
| **After Task 0** | `111a60ce63431f208c80a3d922811c252764cfd6` | `111a60ce63431f208c80a3d922811c252764cfd6` |
| **After Task 3** | `7564a73e62d0821cc652e08924d031b3b718b507` | `7564a73e62d0821cc652e08924d031b3b718b507` |
| **At close, after the Task 5 commit** | `1c567a8dcb6322059b7d89758e9f572ef2571fa4` | `1c567a8dcb6322059b7d89758e9f572ef2571fa4` |

The boot tip is the hash the dispatch names, at both files, so **STOP condition 1 did not fire** and
`cowork_away_returns.md` was not consulted as a blocker.

**★ WHY THE CLOSE ROW NAMES THE TIP AFTER THE TASK 5 COMMIT AND NOT AFTER THE BATCH'S LAST COMMIT,
STATED RATHER THAN LEFT AS THE STALENESS THE DISPATCH WARNS AGAINST.** Task 4(1) orders the close tip
written after the LAST commit of the batch. The batch's last commit is the **end-state commit**, which
carries the end-state guard artifact, this file's completed close row and the `cowork_away_returns.md`
close section — and **a commit cannot carry its own hash**. The row above is therefore the tip
immediately before that commit, written INTO the end-state commit rather than left at the Task 3 tip,
which is the two-commits-stale defect the dispatch names. The end-state commit's own hash is reported
in this session's closing message and in the close section's commit table, where it is named as
*this commit* on that file's established convention. **This is declared as departure 5 below.**

---

## 2. Task 0 — the dispatch landed, and the tree it was landed into

**Commit `111a60ce63431f208c80a3d922811c252764cfd6`**, pushed. Two paths, exactly as Task 0 names
them: `cc_instruction_l2_candidate_list_2026_09_05.md` and
`tools/audit/changed_paths_l2_candidate_list_task0.json`. The commit reports `2 files changed, 4046
insertions(+)` and **zero deletions**.

**The enumeration was taken with the sanctioned enumeration tool** — `tools/audit/changed_paths.py`,
never `git status` — over the whole tracked population, its output redirected to a scratch file
outside the repository and read with the file tools. Its artifact is
`tools/audit/changed_paths_l2_candidate_list_task0.json`.

- **ZERO tracked modifications.** Every one of the 848 records carries the untracked code `??`; no
  record carries a modification, addition, deletion, rename or copy code in either the index or the
  working-tree column. **STOP condition 2 did not fire.**
- This dispatch was present as an untracked addition, and the standing untracked `cc_*` root
  population was present and correctly not landed, exactly as Task 0 names in advance.
- The Task 0 enumeration artifact does not appear in its own listing, because the tool enumerates and
  then writes. That is mechanical and the dispatch says so for Task 3; it holds identically here.

---

## 3. Task 1 — the group gloss reads the register's own group title

### What was inserted, and what was changed

**One inserted helper and one changed expression, and nothing else.** No other line of
`tools/audit/gen_derivation_boot_pack.py` was edited, moved or deleted.

1. **The helper `group_title(group)` with its module-level cache `_GROUP_TITLES`**, inserted
   immediately before `def candidates(` and after the blank lines following `haystack()`, verbatim as
   Task 1(c) prints it — including the docstring that preserves the former hardcoded wording in place
   rather than deleting it (#12), and the two `Stop` raises that make an unknown group a STOP rather
   than a silently-degrading fallback.
2. **The gloss expression inside `candidates()`**, changed from the hardcoded string to
   `group_title(e.get("group"))`. The two surrounding lines of that `why.append` are unchanged.

The helper reads the group titles from `tools/audit/decisions/backbone_decisions.json`'s own `groups`
table through the generator's existing `read_json` and `BACKBONE`, so no second copy of those titles
is created (#6).

### The proof it is a repair and not a behaviour change

`python tools/audit/gen_derivation_boot_pack.py --check` → **exit 0**, with all three built subjects
re-deriving FROZEN at their recorded blobs. **STOP condition 3 did not fire.** The committed manifest
was not adjusted to make it pass, and nothing under `tools/audit/derivation_boot_pack/` was touched.

**★ WHAT THAT EXIT-0 ACTUALLY ESTABLISHES WAS CHECKED AT THE TOOL'S SOURCE RATHER THAN ASSUMED (#19),
because all three subjects are FROZEN and a reader could take the run for a digest comparison only.**
`check_all` compares the freshly built manifest against the committed
`tools/audit/derivation_boot_pack.json` **byte for byte** before it reaches the frozen-digest branch,
and `build()` calls `build_subject()` for **every** subject in `WITHHELD` including the frozen ones —
so `candidates()`, and with it the group gloss, is re-derived on this run for `harmony-boundary`, the
one built subject whose criterion carries a group term. **The exit-0 is therefore a byte-identity
proof of the rendered gloss and not merely a hash check of pinned pack files.** The frozen branch is
what leaves the pack DIRECTORIES verified against their recorded blobs rather than re-rendered.

### The value the repair returns

`group_title("E")` returns exactly **`Layer 2 — the slicer`** — the same string the removed hardcode
carried, which is why the `harmony-boundary` subject renders byte-identically. **STOP condition 5 did
not fire.** The value was taken from the function itself inside Task 2's check (check 14 below), not
by eye and not from the backbone by transcription.

**The repair is visible in the published data**, which is the other half of the point: a group-A match
in `tools/audit/l2_candidate_list.json` is now glossed `The estimator architecture — the joint
estimator`, and no group match anywhere in that artifact carries the string `Layer 2 — the slicer`
unless its matched group is E (checks 15 and 16 below).

---

## 4. Task 2 — L2's candidate list, published whole

The script was written into this session's scratch directory **outside the repository**, ran
read-only, never called `build()`, `write_all()` or `check_all()`, injected nothing, and wrote exactly
one file into the tree: **`tools/audit/l2_candidate_list.json`**, which is the ONE home of the
candidate list and its sizing. It calls the generator's **own** `candidates()` over the **committed**
criterion table, so no second matcher exists to disagree with the first (#6).

### Every check, stated as passed or failed with its own numbers

**`FAILED CHECKS: 0` — all sixteen passed.**

| # | Check | Result | What it saw |
|---|---|---|---|
| 1 | the design-intent population is 244 | **PASS** | 244 |
| 2 | the criterion returns 244 candidates | **PASS** | 244 |
| 3 | the group term picks 130 | **PASS** | 130 |
| 4 | the keyword list adds 47 | **PASS** | 47 |
| 5 | the home-document list adds 67 | **PASS** | 67 |
| 6 | the three parts sum to 244 | **PASS** | 244 |
| 7 | the three parts partition the candidates with none left over | **PASS** | remainder 0 |
| 8 | every candidate falls in exactly one of the three parts | **PASS** | unpartitioned: none |
| 9 | the per-register-group counts sum to 244 | **PASS** | 244 |
| 10 | the published rows are the whole candidate set | **PASS** | 244 rows |
| 11 | every row carries the entry's own verbatim | **PASS** | 0 rows missing it |
| 12 | every row carries the entry's own plain restatement | **PASS** | 0 rows missing it |
| 13 | the sixty-seven by home document agree with the preceding batch's artifact | **PASS** | the two dictionaries equal |
| 14 | `group_title('E')` is the register's own title for group E | **PASS** | `Layer 2 — the slicer` |
| 15 | every group match is glossed with that group's own register title | **PASS** | no counter-example |
| 16 | no group match is glossed `Layer 2 — the slicer` unless its group is E | **PASS** | no counter-example |

**Check 13 is a CHECK and not a transcription** (D-431): the sixty-seven-by-home-document mapping was
derived here by this script and compared against
`tools/audit/l2_criterion_written_check.json`'s independently written one from the preceding batch.
They agree.

**Two ways the script could have died instead of reporting were caught rather than left**, exactly as
the dispatch's own fact check records: a candidate outside the three parts is named at check 8 rather
than raising a `KeyError` mid-render, and a register group of `None` is ordered by `gkey` rather than
raising a `TypeError` in a sort. Neither condition arose.

**Any failure would have been STOP condition 6.** None occurred, and nothing was adjusted to make a
number come out.

### The sizing by register group — the figure the next dispatch will be scoped on

Task 4(4) orders this figure into the report by name. Its **one home** is
`tools/audit/l2_candidate_list.json` → `the_sizing`; the table below is a citation of that generated
artifact and not a hand-taken measurement (#17f, D-431).

| Register group | Candidates | first reached by the group term | by the keyword list | by the home-document list |
|---|---|---|---|---|
| A | 27 | 27 | 0 | 0 |
| B | 4 | 0 | 2 | 2 |
| C | 43 | 43 | 0 | 0 |
| D | 2 | 2 | 0 | 0 |
| E | 1 | 1 | 0 | 0 |
| F | 24 | 24 | 0 | 0 |
| G | 33 | 33 | 0 | 0 |
| H | 47 | 0 | 33 | 14 |
| I | 6 | 0 | 1 | 5 |
| J | 4 | 0 | 1 | 3 |
| K | 3 | 0 | 1 | 2 |
| L | 2 | 0 | 0 | 2 |
| M | 17 | 0 | 6 | 11 |
| N | 8 | 0 | 0 | 8 |
| Q | 5 | 0 | 1 | 4 |
| S | 12 | 0 | 0 | 12 |
| T | 1 | 0 | 0 | 1 |
| U | 5 | 0 | 2 | 3 |
| **total** | **244** | **130** | **47** | **67** |

**How the three columns are to be read, in the artifact's own words:** they record which term FIRST
reached each candidate, in the criterion's own order — the group term, then the keyword list on what
the group term leaves, then the home-document list on what both leave. They are a partition and not a
statement that no other term also reached an entry; each row's `matched_by` carries every term that
did. **The six groups the group term names are A, C, D, E, F and G**, which is why every candidate in
those groups is reached by it and none in any other group is.

### The bound the artifact carries on itself

Written into the artifact rather than only here (#19): it is a pattern match and **its reach is
UNMEASURED** — an entry bearing on L2's subject in words none of the criterion's terms carry does not
appear, and an empty match would be evidence of nothing. It counts **CANDIDATES and not withheld
entries**: a candidate carries an authored verdict, and a candidate ruled OUT is still rendered into
the pack. **No verdict exists for this subject.** And the population is the sort artifact's 411, not
the decisions register's 477 — sixty-six register entries lie outside the criterion's reach and no
term of it can reach them (#24, **D-661**).

---

## 5. Task 3 — the three results

### (a) The enumeration

`tools/audit/changed_paths_l2_candidate_list_task3.json`, 849 records over the whole tracked
population.

- **Exactly one tracked modification: `tools/audit/gen_derivation_boot_pack.py`, code `" M"`.** Every
  other record is untracked.
- **`tools/audit/l2_candidate_list.json` present as an untracked addition**, code `"??"`.
- **Nothing under `tools/audit/derivation_boot_pack/` and not `tools/audit/derivation_boot_pack.json`
  appears in the enumeration at all**, so both are unchanged against the commit. **STOP condition 4
  did not fire.**
- The Task 3 enumeration artifact does not appear in its own listing, for the mechanical reason the
  dispatch names in advance: it enumerates and then writes.

### (b) The standing guard set

`python tools/audit/gen_guard_state.py --check` → **exit 0**, *the guard state re-derives*: **76
guard(s) run, 10 failing, 4 not run, 16 historical record(s)**.

**The exit-0 is the identity proof and not merely a matching count.** `--check` re-derives the guard
state and compares it against the committed artifact, so exiting 0 means the state measured after this
batch's edit EQUALS the state recorded at the boot tip — the failing set is the same SET as the ten
inherited, not merely the same size, and there is no eleventh. **The edited generator's own guard,
`tools/audit/gen_derivation_boot_pack.py --check`, PASSES.** There was no drift, so the dispatch's
do-not-regenerate branch was not reached at Task 3 and nothing was regenerated there.

### (c) The commit

**Commit `7564a73e62d0821cc652e08924d031b3b718b507`**, pushed. Three paths:
`tools/audit/gen_derivation_boot_pack.py`, `tools/audit/l2_candidate_list.json` and
`tools/audit/changed_paths_l2_candidate_list_task3.json`. The commit reports `3 files changed, 10383
insertions(+), 1 deletion(-)` — the single deletion being the one replaced gloss line, which is the
whole of the change to existing text.

---

## 6. Any STOP reached

**None. All six STOP conditions were tested rather than assumed, and none fired.**

1. **The tip at boot** — `87fd4dea5c9e07a92ca7e3327a68e97a9e05f93e` at both ref files, the hash the
   dispatch declares. Did not fire.
2. **Tracked modifications at boot** — the sanctioned enumeration tool reported **zero** over 848
   records. Did not fire.
3. **`--check` after the repair** — exit 0. Did not fire.
4. **`tools/audit/derivation_boot_pack/` and `derivation_boot_pack.json`** — absent from the Task 3
   enumeration entirely, so unchanged against their committed blobs. Did not fire.
5. **`group_title("E")`** — returns exactly `Layer 2 — the slicer`. Did not fire.
6. **Task 2(f)** — `FAILED CHECKS: 0`; all sixteen checks passed, with 244 candidates over a
   244-entry population, the three parts at 130 / 47 / 67 partitioning them with nothing left over,
   every row carrying the entry's own verbatim and plain restatement, the sixty-seven agreeing with
   the preceding batch's independently written artifact, and every group gloss carrying its own
   group's register title. Did not fire.

---

## 7. Declared departures — stated rather than absorbed

1. **The commit trailer differs from the one the dispatch prints.** The dispatch specifies
   `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. All commits of this batch carry
   **`Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`**, because a system-level
   attribution instruction in force for this session states that form and states that it replaces
   earlier attribution guidance — which is exactly the case Task 0 anticipates and asks to have
   declared. **Every commit SUBJECT and BODY is the dispatch's own, verbatim.**

2. **A shell command read a repository state at session start: `git rev-parse HEAD`.** It is a branch
   tip read through the shell, and **`CLAUDE.md`'s D-253 conventions say a branch-tip or index read is
   never trusted for what is current.** It is reported rather than absorbed, on the rule that being
   right is not the defence. **Nothing rests on it:** both ref files were then read with the file
   tools, and every tip in this report and in the close section comes from those reads.

3. **One shell command was DENIED by the shell-read guard and was routed to the file tools rather than
   worked around.** A `python -c` that opened `C:\s\MS\cowork_away_returns.md` to count its lines was
   denied by policy — interpreter code carrying a literal repository path. The denied form was not
   retried; the file's structure was located with `Grep` and read with `Read`. **This is a data point
   about a finding the preceding batch already recorded and is stated as one below.**

4. **The temporary files are in this session's scratchpad, not `%TEMP%`.** The dispatch's Task 2(b)
   orders the script written outside the repository and warns that `%TEMP%` does not expand in this
   shell. Everything — the script and every redirected run output — went to a directory outside the
   repository; the Task 3 enumeration confirms no scratch file reached the tree.

5. **This report's close-tip row is written in the batch's LAST commit rather than in the commit that
   first carries the report.** Task 4(1) requires the close tip taken after the last commit; the last
   commit is the end-state commit and cannot carry its own hash. The row therefore names the tip after
   the Task 5 commit, written into the end-state commit, with the reason stated at the table itself
   rather than left to be inferred. **The alternative was available and is recorded:** naming the Task
   3 tip and leaving it two commits stale, which is the defect the dispatch's own Task 4(1) names.
   This adds one path — this file — to the end-state commit that Task 5 describes as carrying the
   end-state guard artifact.

6. **The end-state commit regenerates one measurement and the guard artifact.** Task 5 orders this
   explicitly where the `STATUS.md` entry it also orders stales the read-size measurement, on the
   settled practice of the two preceding batches. It is named here so the act is on the record and
   not merely inside the guard's own output.

   **The cause was established at the object rather than assumed.**
   `tools/audit/session_start_read_size.json` records `STATUS.md`'s character count at the tree, and
   the entry Task 5 orders grew that file. The three guard states of this batch:

   | When | Result |
   |---|---|
   | after Task 3's edit, before the `STATUS.md` entry | **exit 0** — the artifact re-derives; population 76, **ten failing**, 4 not run, 16 historical |
   | at the tree carrying the close, before the end state | **exit 1** — STALE; population 76, **eleven failing**, the eleventh being `gen_session_start_read_size.py --check` |
   | the end state, after the regeneration | **exit 0** — population 76, **ten failing**, the failing set the ten inherited with **no eleventh** |

   The eleventh red appeared only after Task 5's own ordered act, and the regeneration repairs a red
   this batch itself caused. **The alternative was available and is recorded:** committing a guard
   state carrying an eleventh red of this batch's own making, which the next batch would inherit and
   have to diagnose.

---

## ★ ONE OBSERVATION ABOUT THE APPARATUS, CARRYING NO VERDICT, NO CAUSE AND NO RECOMMENDATION

The preceding batch recorded a finding about the shell-read guard: it denied one command whose path it
could not resolve, and did **not** deny a `wc -l` at a plain relative repository path, `wc` being one
of the utilities the rule's own sentence names. That finding is carried in this dispatch's own
closing section as an owed open-items row, deliberately not created here.

**This batch adds a third observation and nothing more.** A `python -c` opening a plain **absolute**
repository path was **DENIED**, with the denial naming the guard-family ruling of 2026-08-08 in its own
words. That is a third data point beside the preceding batch's two.

**No cause is asserted and none may be read in** (**D-641**, **D-658**). The guard's source was not
opened, the three observations differ in more than one respect at once — the utility, the redirection
form, the path's absoluteness — and this batch established none of them as the operative difference.
**No `OPEN_ITEMS.md` row was created**, this dispatch forbidding it, and the row the preceding batch
declared owed remains owed and is carried, not dropped.

---

## What this batch did NOT do

**No verdict was authored for any subject and no `l2` verdict table was created** — an empty one would
be a claim that the subject has been graded. **Nothing was withheld and no `l2` withheld family was
authored.** **No pack was rendered and no session was booted:** no file under
`tools/audit/derivation_boot_pack/` was created, edited, deleted or read for writing,
`tools/audit/derivation_boot_pack.json` was not regenerated, `write_all` was never reached, and the
only operating state of the generator this batch ran is `--check`. **`EXTRAS` and `FROZEN` gained no
`l2` key.** **The `CRITERION` table was not touched, and `KEYWORDS` and `L2_KEYWORDS` both stand
exactly as they stood** — the enumeration's single tracked modification is the generator file, whose
only changes are the inserted helper and the one gloss expression. **No reading file was written.**
**No `D-NNN` was allocated**, no `OPEN_ITEMS.md` row was created, flipped or discarded, and nothing
was written into `DECISIONS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `FRAMEWORK.md` or any ruling record
— only the one `STATUS.md` entry Task 5 orders. **No `src/` change, no golden, no test changed, moved
or run, no build, no measurement of the analysis, and nothing under `tools/corpus/` or
`tools/robust_stop/`.** **No position is taken on any candidate: publishing a candidate is not judging
it, and no sentence of the artifact or of this report says or implies whether any entry should be
withheld.** **Nothing is recommended.**

---

## The standing self-check over this batch's own diff (D-434, D-196)

1. *Principles touched.* **#6** — the gloss reads the group titles from the table that already defines
   them rather than making a second copy, and the publication calls the generator's own `candidates()`
   rather than reimplementing the match. **#12** — the former hardcoded wording is preserved in the
   helper's own docstring rather than deleted, and the pre-repair state of every artifact is recorded
   rather than overwritten in silence. **#13** — the two ways the check script could have died instead
   of reporting were caught and named; the guard observation is stated without a cause being asserted.
   **#19** — the repair's inertness is proved at `--check` and at the value `group_title("E")`
   returns, and what that exit-0 establishes was itself checked at `check_all`'s and `build()`'s
   source rather than assumed; the publication's reach is stated as UNMEASURED on the artifact itself.
   **#17f / D-431** — every figure lands in the generated artifact; the one table this report
   reproduces is reproduced under Task 4(4)'s explicit order and is cited to that artifact as its one
   home, and the one place the preceding batch's figures reappear is a comparison between two
   independently written scripts, which is a check and not a transcription. **#24 / D-661** — the
   population bound, 411 and not 477, is carried on the artifact. **#15** — every property is verified
   at the objects, the enumerations taken over the whole tracked population twice. **D-249** — no
   question is put to the user and no position is taken on any candidate. **D-672** — nothing was
   stopped partway. Conforms, with departure 2 recorded as a breach of **D-253** rather than defended.
2. *Conventions.* American English; no self-invented label — *the group term*, *the keyword list*, *the
   home-document list*, *the withheld family*, *a candidate*, *the group gloss* are the dispatch's and
   the record's own; *measurement tool*, *check*, *script*, *generator*, never *instrument*; *the
   open-items register* and *the decisions register* in full; *register group* rather than bare
   *group* where the sense is the decisions register's; music-theory words in their musical sense.
3. *Numbers and premises.* Both tips at the two ref files with the file tools at every commit; the
   generator's three quoted sites, the backbone's `groups` table and group E's title with the file
   tools; the enumerations with the sanctioned enumeration tool over the whole tracked population,
   twice; every check value from this batch's own run of the Task 2 script; the guard verdict from
   this batch's own run; what `--check` establishes from `check_all` and `build()` read at their
   source.
4. *File-tools rule.* Every intended repository read went through the file tools, with **one breach
   declared as departure 2** and **one denial routed as departure 3**. The shell was otherwise used
   only for the sanctioned tool invocations, for reads of scratch files outside the repository, and
   for `git add` / `git commit` / `git push`.
5. *Uncertainty.* **What this batch establishes is that the group gloss now reads the decisions
   register's own title for every group the ruled criterion names, byte-inert for every built subject,
   and that L2's 244 candidates are published whole with the entry's own words and the criterion terms
   that reached each of them.** It does **NOT** establish what any candidate's verdict would be, that
   the criterion is the right one, that the criterion's reach is adequate — the artifact states in
   terms that its reach is unmeasured — or that the sixty-six register entries outside the population
   do not matter. **The ten inherited guard reds were carried as a SET, established identical by the
   run's exit-0, and their individual causes were not established here.**

*Provenance: CC, 2026-09-05, at boot tip `87fd4dea5c9e07a92ca7e3327a68e97a9e05f93e`, under
`cc_instruction_l2_candidate_list_2026_09_05.md`, after the ordinary session-start read in full —
`CLAUDE.md`, the `DECISIONS.md` INDEX, `STATUS.md` and the derived gating answer — which binds even
when the opening instruction names a single file (Ruling 5 of
`cowork_rulings_2026_08_29_ratification_sitting.md`, the framework phase retrospective, P-1).
`BUILD_AND_TEST.md` was NOT read and the ground is recorded: its read is conditional on a build, a
test, or a measurement tool whose command lives there, and none of this batch's three commands does —
they are the sanctioned enumeration tool, the boot-pack generator's `--check`, and the standing guard
set, each named in this dispatch itself. Every commit identifier above was read from the ref files by
the file tools at the time each commit was taken. No figure of the candidate list is restated in this
report beyond the sizing table Task 4(4) orders by name, which is cited to its one home (D-431).*

---

## ★ ADDENDUM 2026-09-05 — a disclosure made in chat and absent from this report, written in by the next batch

**Written by the L2 verdict-pass batch (`cc_instruction_l2_verdict_pass_2026_09_05.md`, Task 1(c)) on
the account of `cowork_handoff_entry_one_hundred_and_eight.md`, first paragraph. No existing line of
this report is changed** — a dated report is re-bannered and never rewritten (**D-674**), and an
appended, dated, attributed addendum is the additive form.

**What the entry records.** That the executing side of this batch **told the user in its closing chat
message that it had written an invented placeholder hash into this report's close-tip cell and caught
it before committing**. The entry states that it searched **this report's declared departures** and
**this batch's close section in `cowork_away_returns.md`** and found the disclosure in **neither**,
and calls it *"the one instance this line has produced of the failure the whole apparatus exists to
prevent"* being *"the one thing not written down"*.

**The bound on this addendum (#24).** It carries **the entry's account and not the executing side's
own words.** That chat message does not survive and the batch writing this addendum has no access to
it. Nothing here is a quotation of the executing side, and no cause, motive or further fact about
what happened is asserted.

**What this batch established about the committed close-tip row, by the one cheap check D-253
permits** — a git OBJECT query by explicit hash, under D-254, investigate by default. §1's table of
this report names `1c567a8dcb6322059b7d89758e9f572ef2571fa4` as the tip after the Task 5 commit. Two
queries were run:

- `git cat-file -p 73d27c15e887b4d1063fc15af6d2beadaac1b24a` — the tip the hundred-and-eighth entry
  read at both ref files after this batch closed. **Its `parent` line reads
  `parent 1c567a8dcb6322059b7d89758e9f572ef2571fa4`.**
- `git show --stat 1c567a8dcb6322059b7d89758e9f572ef2571fa4` — **the commit exists**, is subjected
  `docs(status): record the group-gloss repair and L2's published candidate list`, and its stat
  carries exactly two paths: **`STATUS.md`** and **`cc_report_l2_candidate_list_2026_09_05.md`**.

**Outcome, stated as what was checked and what was seen: the committed close-tip row names a real
commit, and the right one.** The invented value the entry describes did not reach the tree. Neither
query returned a `bad object`, so no staleness signal arose.

**What this addendum does NOT do.** It asserts no cause, proposes no remedy, allocates no finding
number, creates no open-items row, and takes no position on whether the disclosure should have been
declared in the departures section rather than only in chat. It changes nothing about this batch's
results.
