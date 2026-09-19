# Cowork handoff entry 194 — 2026-09-17

**The current entry point.** Entry 193 is superseded as entry point and stands otherwise; its §3 list carries
forward except where §3 below settles an item. Grades: **[checked]** = opened or measured at the file by this sitting;
**[relayed]** = taken from CC's report or chat reply, or from another record, and not checked here.

## 0. State at close

- **The passage-guards batch is finished and pushed.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master`
  both read `5c95032de157aff105c2c2abefce2c87cbb95cab` **[checked]** — the close commit. Task commit `ec86e53b7a`,
  push line `49c6364242..5c95032de1 master -> master` **[relayed, CC's chat reply]**.
- **The three checks are historical** (`gen_claude_md_finer_archive.py`, `gen_post_split_archive.py`,
  `gen_claude_md_prune_backlog.py`); their three LIVE verdicts are reversed with the former wording preserved.
  Edits read at both tools before the commit **[checked]**. Guard counts now `78 run, 15 failing, 4 not run,
  19 historical` **[relayed]**.
- **The forward bound is met**: two moves ran (catch-up on the authored-ends batch, ordinary on the root-move
  close). `STATUS.md` went from 19,082 to 12,068 bytes and now heads with this batch's entry; the three 2026-09-09
  entries and the root-move close entry are gone from it **[checked at the file]**.
- **`tools/audit/claude_md_finer_archive.json` stays modified and uncommitted**, and the cause is now measured:
  committed blob 0 CR-terminated lines of 122, working-tree copy 122 of 122, `git diff --ignore-cr-at-eol` between
  the two blobs empty **[relayed, the report §3]**. CC's first-run guess (CRLF in the blob) was the reverse of the
  fact. Why the working-tree copy carries CRLF was not traced.
- **Nothing is running. No dispatch is out.** No decisions-register entry was written; whether the reclassification
  owes one is still the open point of entry 193 §1.

## 1. What happened this sitting, in order

1. Boot per entry 192 §4.1, whole, at the objects; entries 193 and 192 whole; the dispatch whole.
2. CC's first run STOPPED at Task 2(c): after `git restore`, git still reported the finer-archive artifact
   modified. **Writing-side defect** — the original dispatch assumed a restore clears the record. Checked at the
   tools: the tool writes LF (`gen_claude_md_finer_archive.py` line 592), `.gitattributes` has `* text=auto`,
   `changed_paths.py` wraps `git status --porcelain`, so the ` M` is git's own. CC wrote no report for that run.
3. The resume dispatch `records/cc/instructions/cc_instruction_passage_guards_historical_resume_2026_09_17.md`
   was written with the cause MEASURED first (blob by explicit hash, CR counts, `--ignore-cr-at-eol` diff,
   `ls-files --eol`) and the branch ruled before the measurement. No user decision was put: the ruling already keeps
   the file out of every commit, and the commits are by explicit path.
4. The resume run completed everything. Report read whole; refs checked; `STATUS.md` checked.

**Two items the report leaves unfilled, filled here from CC's FIRST chat reply, which the second run never saw
[relayed from that reply]:** capture `5a4aa7039fa711b490fa786ec22912ffdc94c0e8` is the first run's Task 0(d)
(566 records) and `98d16ef898cab4eda00215bff85070c7459d6491` its Task 2(b); the Task 2(b) STOP read, verbatim:
`STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_withheld_family_reading.py']`.

**One inconsistency in the report, not corrected (a dated report is re-bannered, never rewritten, D-674):** its
§8 says "no command was added" while its §5 declares the one added command (`git rev-parse HEAD` after the task
commit). The §5 declaration is the true one.

## 2. What comes next — the root clean-up, then the analysis work behind it

Entry 193 §3.2 stands: one question per turn, full self-contained surfaces, choice question in a later turn.

1. **(a) The `cowork_*.md` design and working documents at root** (173 by CC's earlier check report **[relayed through entry
   193 §2]**, not counted here) — where they go, and how the next move avoids the quote-and-line-number breakage the root records move met
   (35 `LINE DRIFT` lines after that move's Task 1 **[relayed, entry 192 §4]**; the three word-for-word checks
   that turned red are now historical, but the decisions register's quote check — `gen_cluster_dispositions.py
   --verify`, named at `CLAUDE.md` register rule (d) **[checked]** — was untouched by this batch and is what
   reported the drift at the last move **[relayed, entry 192 §1 item 2]**). *(★ CORRECTED AT THE USER-ORDERED
   CHECK. FORMER WORDING, PRESERVED (#12): "but the decisions register's quote and line checks still run and
   would meet a move the same way" — whether it is in the guard runner was not checked.)*
2. **(b) The loose leftovers at root** (old test JSON, logs, echo files, a file named `--output-json`, `.bat`
   scripts, an `.mp3`, scratch folders) — whether anything quotes them is to be checked, not assumed.
3. **(c) Entry 191 §3's remainder:** the 24 unclassified files, CC's five self-check rows, entry 189 decision 4;
   the `CLAUDE.md` line drift; the stray `…_eighty_two-1.md`.
4. **Keep the perspective:** all of the above is record-keeping. The analysis work waiting behind it is the owed
   second extractions (entry 186's count, fourteen). Say so when putting each question.

**Dispatch rules learned this sitting:** (i) a `git restore` did not make `git status` clean for
`tools/audit/claude_md_finer_archive.json` (committed LF, checked out CRLF under `core.autocrlf=true` and
`* text=auto`) — do not write a dispatch expectation that a restore clears a ` M` record; whether other files
behave the same was not measured *(★ CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING, PRESERVED (#12): "a
`git restore` of a text file does not make `git status` clean" — one file was measured, not the class)*;
(ii) when a dispatch allows the writing side to land a new file while it runs, EVERY later enumeration in that
dispatch must carry the same allowance — the resume's Task 1(b) required identity with Task 0(d), so a file landed
between the two would have been a STOP (this side held entry 194 back until the batch closed, so it did not fire);
(iii) a report written by a later run cannot carry what only an earlier run's chat reply holds — paste the earlier
reply's captures into the resume dispatch, or the report will say "not assigned".

## 3. Declared departures of this side

- **FOUR SHELL COMMANDS ON THE DEVICE, AGAINST THE USER'S OPENING INSTRUCTION ("NOT bash")**, all before any
  repository content had been read through the file tools: a search for the entry's file name at the root with a
  root listing; a repository-wide `grep` for the entry's title that timed out; a time-sorted root listing with a
  `grep` over the root `.md` files and over `CLAUDE.md` for "handoff"; a listing of `records/cowork/handoff/` with a
  heading search over `cowork_handoff.md`. All read-only; no file changed; **listing the root breaks cadence 0 of
  entry 169**. No claim in this entry rests on their output — every fact graded [checked] above was read afterwards
  through Read, Grep, a staging call or a bridge listing. Declared to the user in the same turn, after they had happened *(★ CORRECTED AT THE USER-ORDERED CHECK.
  FORMER WORDING, PRESERVED (#12): "in the turn after they happened")*. No shell
  command after that, in the container or on the device.
- One folder-access grant (`C:\s\MS`); one bridge listing of `records/cc/reports/`.
- No project memory read or written. No popup, subagent, web access or task list. Two files sent into the
  conversation — the resume dispatch and this entry — to obtain the identifiers their commits need *(★ CORRECTED
  AT THE USER-ORDERED CHECK. FORMER WORDING, PRESERVED (#12): "One file sent … (the resume dispatch)" — written
  before this entry's own landing)*.
- **Landings:** the resume dispatch, 12,835 bytes, committed twice (unguarded then forced), staged back, proved at
  its last edit and at its last paragraph; this entry, landed after the batch closed, first at 7,700 bytes, then
  re-landed after the user-ordered check below — the closing size is at the closing staging result and in the
  conversation's closing report.
- **★ The user-ordered check, run on this entry as landed (7,700 bytes, 92 lines, one call).** Five corrections,
  each at its site with the former wording preserved: an unmarked relay (the 173 count); a claim about the register's
  checks wider than what was read; a rule generalised from one measured file to a class; a wrong turn reference for
  the shell-command declaration; a count of files sent that this entry's own landing made false. What the check
  confirmed at its objects: both ref values; the `STATUS.md` sizes and the entries moved out of it; the edit lines in
  both tools; the two capture identities and the STOP text against CC's first reply; the report's §5/§8
  inconsistency at its lines. It did not re-open the report whole or any earlier entry.
- **Degradation:** the four shell commands are one lapse of attention at boot, not a listed tell. One writing-side
  defect cost a CC run (§1 item 2); a second (rule (ii) above) was caught before it fired. No listed tell counted;
  that is a statement about what was looked for. Handover is at a verified stop: the batch is pushed and this entry
  is landed with nothing running.
