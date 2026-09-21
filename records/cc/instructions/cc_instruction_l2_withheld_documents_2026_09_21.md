# CC INSTRUCTION — L2's WITHHELD DOCUMENTS, DERIVED AND PRINTED (2026-09-21)

**This is the FIRST HALF of the pack-build dispatch** that Ruling 1 §11 item 3 of
`records/cowork/rulings/cowork_rulings_2026_09_05_l2_boot_list_sitting.md` orders. It runs the
derivation Ruling 6 of that record requires, prints its result, and **STOPS there**. **It authors
nothing into `WITHHELD`, `EXTRAS`, `VERDICTS` or `CRITERION`, renders no pack, and writes no pack
directory.**

**WHY THE PACK-BUILD DISPATCH IS IN TWO HALVES, declared on this dispatch's face rather than left to
be inferred.** Ruling 6 reads, in its own words: the dispatch *"derives, from the register's data
file (`tools/audit/decisions/backbone_decisions.json`) and the ruled verdict table, the set of home
documents of the 111 IN entries; prints it; and **STOPs for the user's confirmation before the set is
authored into `WITHHELD["l2"]["withheld_documents"]`**, each with its finding, date and reason."*
The tool's own structure makes that STOP a batch boundary and not a pause inside one:
`gen_derivation_boot_pack.build()` iterates `sorted(WITHHELD)`; `build_subject` raises
`Stop("no authored WITHHELD table for subject …")` when a subject is absent from `WITHHELD`, and the
same for `CRITERION` and `EXTRAS`; and `write_all` writes a pack directory for every non-frozen
subject the run covers — all of them on a bare run, the one named on a `--subject` run. **So
authoring `WITHHELD["l2"]` at all is the act that makes the tool build and write L2's pack** — and it would do so with the withheld documents still unconfirmed. Under **D-251**
a running dispatch is never steered mid-flight and every instruction is self-sufficient, so the
user's confirmation sits between two batches, not inside one. The second half authors
`WITHHELD["l2"]` and `EXTRAS["l2"]`, fixes the `DATE` mechanism, runs Ruling 8's two regenerations,
renders, and takes the leak list to the user. **It is not written yet and nothing here anticipates
it.**

**THE WRITING SIDE'S RESTRAINT, declared.** This dispatch is final at hand-over. The writing side
will not touch it, nor any file it names, while this batch runs.

**★ THIS DISPATCH WAS AMENDED 2026-09-21, AFTER IT WAS FIRST LANDED AND BEFORE IT RAN**, at the
writing side's own fact-check of it, in three places besides this note and no others: **0(f)**, which
gains handoff entry 224 as a conditional sixth member of the commit set; **Task 1's backbone
assembly**, which omitted the tool's own `e.get("id")` guard; and **§6's held-back list**, which
stated a relayed population as if this side had enumerated it. **No bar changed, no task changed, no
STOP changed.** Nothing has run against the earlier text.

---

## 1. Bars

**B1 — TWO TOOL SOURCES AND NO OTHERS ARE EDITED BY THIS BATCH, each named here because its own task
orders it:** `tools/audit/gen_guard_state.py` (Task 2, the enrolment the standing new-tool rule
requires) and `tools/audit/gen_status_batch_bound.py` (Task 3, the forward-bound re-aiming, which
this bar excepts BY NAME so that the bar cannot contradict 5(b)'s own task). **Every other tool
source is untouched.** If a task below seems to need a third tool edited, that is
a bar contradicting a task — **STOP and report it; do not resolve it.**

**B2 — `tools/audit/gen_derivation_boot_pack.py` IS NOT EDITED, IN ANY WAY.** Not its `WITHHELD`
table, not `EXTRAS`, not `VERDICTS`, not `CRITERION`, not `FROZEN`, not `DATE`, not one comment.
**It is run in `--check` mode only, and only where Task 3 runs the whole guard set.** Its bare
invocation rewrites its committed manifest and re-renders every non-frozen pack directory — the
OI-301 hazard, and that tool's own entry in the guard set says so. **A bare run of it is a STOP.**

**B3 — NOTHING under `tools/audit/derivation_boot_pack/` is read for content, written, deleted,
renamed or moved.**

**B4 — no `src/` file, no build, no test, no golden, no score corpus, nothing under `tools/corpus/`
or `tools/robust_stop/`, no measurement of the analysis, no paper, no reading-pass extract, no
score.**

**B5 — no governing document is amended except `STATUS.md`, and there only by the ONE new entry
5(a) orders. No existing sentence of `STATUS.md` is rewritten or removed (#12).** `STATUS_ARCHIVE.md`
changes only as the forward bound's own `--apply` writes it. Not `CLAUDE.md`, not `ARCHITECTURE.md`,
not `FRAMEWORK.md`, not `DECISIONS.md`, not `OPEN_ITEMS.md`. **No open-items row is created, flipped
or discarded. No decisions-register entry and no `D-NNN` is allocated.**

**B6 — `tools/audit/claude_md_finer_archive.json` is held back**: not staged, not reverted, not
investigated. Its modification's cause is still established by nobody and establishing it is not this
batch's work.

**B7 — NO FIGURE IS TRANSCRIBED INTO AN ARTIFACT FROM THIS DISPATCH (D-431).** Every count this
batch reports is measured by the tool that owns it and cited to its artifact. **The figures this
dispatch itself states are exactly these, and each is a START-STATE BAR rather than a value to be
written anywhere:** the tip at 0(b); the four interim-carrier sizes at 0(f), each measured at the
directory listing by the Cowork side; and **111**, a RULED figure taken from Ruling 6 and from §4 of
`records/cowork/rulings/cowork_rulings_2026_09_05_l2_withheld_family_sitting.md`, used at Task 1 as a
falsification bar. **None of them is written into any artifact by this batch.**

**THE FOOTPRINT ASSUMPTION, written from the paths this batch's own tasks touch and from nothing
wider.** This batch's own orders **modify** exactly these existing files: `tools/audit/gen_guard_state.py`
(Task 2), `tools/audit/gen_status_batch_bound.py` (5(b)), `STATUS.md` (5(a)), `STATUS_ARCHIVE.md`
(5(b), by the forward bound's `--apply`), and — as the ordinary consequence of running them —
`tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json`,
`tools/audit/status_batch_bound.json` and the guard set's own artifacts. It **creates** exactly three
new files: `tools/audit/gen_l2_withheld_documents.py`, `tools/audit/l2_withheld_documents.json`, and
your report. **Every other path §6 commits is already on disk from an earlier batch or from the
Cowork side and is committed unchanged**, and §6 orders each one's unchangedness proved.

**THE ORDER INSIDE TASK 3 IS A RULE, NOT A CONVENIENCE, and it is the rule the previous close was
written on.** `STATUS.md` is the second member of `tools/audit/gen_session_start_read_size.py`'s
`MEMBERS` table, and `tools/audit/gen_defense_share.py` carries
`import gen_session_start_read_size as reader`, so **any edit to `STATUS.md` moves both artifacts.**
*(Both facts are RELAYED here, not checked by the writing side: neither tool was opened. They are
established at handoff entry 222 §4, which records the `MEMBERS` table checked at that tool, and are
restated in `STATUS.md`'s own newest entry. **Confirm both at the two tools before you rely on the
ordering, and report what you found.**)* Therefore: **5(a) writes `STATUS.md` and is the LAST edit to
it in this batch; 5(c)'s generators run after it; 5(d)'s capture is taken after them; nothing between
5(c) and the commit may write to `STATUS.md`.**

---

## 2. Task 0 — the start state, proved before anything is written

**0(a) — pin this dispatch**, and take every later re-read of it from its blob:

```
git hash-object -w records/cc/instructions/cc_instruction_l2_withheld_documents_2026_09_21.md
```

Record the hash and report it.

**0(b) — the refs.** Read `.git/refs/heads/master` and `.git/refs/remotes/origin/master` **with the
file tools** (`D-253`; never `git rev-parse`). **Both must read
`ef4fad940d806edf8f84eb9a895f88d70a9bbcf2`.** If either has moved, **STOP**: something ran that this
dispatch does not know about, and the whole start state is void.

**0(c) — the four facts this dispatch is written on, proved at the objects with the file tools.**
Report what you found for each, as found:

1. `tools/audit/gen_derivation_boot_pack.py` carries the line `WITHHELD: dict[str, dict] = {`
   **exactly once**, and between that line and the next line beginning `KEYWORDS = (` it carries
   **no** key `"l2"`. *(What this establishes: L2 has no authored withheld family, which is the
   state this batch's whole shape assumes.)*
2. That same file carries the key `"l2": {` **exactly twice** in the whole file — once under
   `CRITERION = {` and once under `VERDICTS: dict[str, dict[str, tuple[str, str, str]]] = {`.
   **Neither is a withheld family.** *(This is stated because a bare search for `"l2"` in this file
   returns hits that read as a contradiction of item 1 and are not one.)*
3. That same file carries the line `EXTRAS: dict[str, list[dict]] = {` **exactly once**, and the
   subject keys inside it are exactly `"harmony-boundary"`, `"scoring-model"` and `"l0-l1"` — **no
   `"l2"`**.
4. `tools/audit/decisions/backbone_decisions.json` carries a top-level `"decisions"` array, and its
   first element carries the fields `"id"`, `"group"`, `"title"`, `"verbatim"`, `"plain"`, `"home"`
   and `"status"`. **Report the first element's `"id"` and its `"home"` verbatim.**

**Any one of these failing is a STOP.** Report which, and what you found instead. **Do not repair
it.**

**0(d) — the working tree.** Take the enumeration with `python tools/audit/changed_paths.py` — the
sanctioned route, the shell-read guard having refused a working-tree `git diff` to an earlier batch.
Report it whole. **Nothing may be staged when this batch opens**; if anything is, STOP.

**0(e) — the OPENING GUARD CAPTURE.** Run the guard set once and save the capture **outside** the
repository working tree; name the file in your report. Record every guard's verdict. **Two things are
expected and are to be reported as found rather than assumed:** `gen_derivation_boot_pack.py --check`
PASS, and a standing line `STALE vs the run: guard_state.json does not re-derive` at the head of the
capture. *(Both are RELAYED from handoff entry 222 §3, which records them of the captures of
2026-09-20; neither was checked by the writing side, which has no shell.)* **That standing line
predates this batch and is CARRIED, NOT CHASED** — do not investigate it, do not repair it, and write
no condition on it. **If either expectation is not what you find, report it and carry on** — neither
is a STOP, both being relays about a state this batch does not depend on.

**0(f) — the interim carriers, committed.** The standing interim-carrier clause says a sitting record
is written in the turn its ruling is given and lands in git at the next dispatch's Task 0. **This is
that task.** Commit, by explicit path and never a directory pathspec, exactly:

1. `records/cowork/rulings/cowork_rulings_2026_09_20_l2_gate_sitting.md`
2. `records/cowork/rulings/cowork_rulings_2026_09_20_first_pass_extracts_sitting.md`
3. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty_two.md`
4. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty_three.md`
5. `records/cc/reports/cc_report_boot_pack_frozen_manifest_close_2026_09_20.md`
6. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty_four.md` — **only if it exists
   on disk.** It is the handover entry of the Cowork sitting that wrote this dispatch, and it is
   written after this dispatch was landed, so this dispatch states **no size for it**: report the
   size you find. **If it does not exist, say so and commit the other five. Do not wait for it.**

**Establish each rather than asserting it**: take its size by the content-addressed route
(`git hash-object -w --no-filters <path>`, then `git cat-file -s <identity>`), read its last
non-empty line, and report both. **A tail that is not ordinary text, or a NUL byte, is a STOP** —
a Cowork session's landing can be truncated by an interrupted write. Members 1, 2, 3 and 4 must
measure **12,838**, **16,143**, **20,861** and **25,144** bytes; **a different figure at any of them
is a STOP**, because nothing in this batch may have changed them and those are the figures the Cowork
side measured at the directory listing. **Prove the staged set is exactly these five and nothing
else before committing.** Do not push yet.

---

## 3. Task 1 — the derivation tool

**Create `tools/audit/gen_l2_withheld_documents.py`.** It is a new tool; it is enrolled in Task 2, in
this same batch, which is the standing new-tool rule.

**What it derives.** The set of home documents of the entries the ruled L2 verdict table grades IN.

**Where it reads from, and from nowhere else:**

- **The verdict table:** `import gen_derivation_boot_pack as pack`, then `pack.VERDICTS["l2"]` and
  `pack.VERDICT_IN`. **The identity list is NOT re-authored here** — one path per concern (#6), and a
  copied list is a transcription (D-431). Importing that module executes its module level, which
  defines its tables and its functions; its `main()` sits under an `if __name__ == "__main__":` guard
  and does not run on import. **The import must not call `pack.build()`, `pack.build_subject()` or
  `pack.main()`** — doing so would render, and B2 forbids it. **If the import itself prints anything,
  writes anything, or takes any observable side effect, STOP and report what it did**: the writing
  side read that module at its tables and its entry point, not line by line, so an import-time side
  effect is possible and is not ruled out here.
- **The homes:** `tools/audit/decisions/backbone_decisions.json`. Assemble the backbone **exactly as
  `pack.build()` assembles it**, so the two derivations cannot disagree: `{d["id"]: d for d in
  data.get("decisions", [])}`, then for each `r` in `data.get("retired_entries", {}).get("entries",
  [])`, take `e = r.get("the_entry", {})` and add `e` under `e["id"]` **only where `e` carries a
  truthy `"id"` AND that id is not already present** — both guards, exactly as that loop has them.

**How a document is taken from a home, stated mechanically so no judgment enters:** the home is the
entry's `"home"` string. The document is the substring **before the first `:`**, with surrounding
whitespace stripped. **It must then match `^[^\s:]+\.md$`.** A home that is absent, empty, or whose
leading token does not match that pattern **STOPS the tool, naming the entry and its home string**.
Nothing is guessed and no home is repaired.

**What it writes:** `tools/audit/l2_withheld_documents.json`, carrying

- `what_this_is` — one sentence: the set of home documents of the entries the ruled L2 verdict table
  grades IN, derived under Ruling 6 of
  `records/cowork/rulings/cowork_rulings_2026_09_05_l2_boot_list_sitting.md`, **printed for the
  user's confirmation and authored into nothing**;
- `the_ruling_it_executes` — Ruling 6, quoted;
- `in_entries` — the IN identities, sorted by entry number;
- `documents` — one record per distinct document, sorted by path: the document, the IN identities
  homed there, and how many;
- `counted` — `in_entries`, `documents`, and the sum of the per-document identity counts;
- `★_the_reconciliation_taken_in_both_directions` — every IN identity accounted to **exactly one**
  document, and every listed document named by **at least one** IN identity. **A failure of either
  direction is a STOP, not a field.**
- `★_the_bound` — that this derivation reaches the entries of the verdict table and nothing wider,
  and that a document's presence here is not a judgment that it should be withheld: that is the
  user's, and Ruling 6 reserves it (D-661, #24).

**Its STOPs, each ending the run:**

1. An IN identity the backbone does not carry.
2. A home absent, empty, or not matching `^[^\s:]+\.md$` at its leading token.
3. Either direction of the reconciliation failing.
4. **The IN count is not 111.** Ruling 6 names *"the 111 IN entries"*, and §4 of
   `records/cowork/rulings/cowork_rulings_2026_09_05_l2_withheld_family_sitting.md` records the ruled
   family as 111 IN, 133 OUT, 0 UNPLACED. **A different count means the verdict table has moved since
   the user ruled it**, and the derivation must not run over a family he did not rule. Report both
   figures and stop.

**Its modes.** A bare run writes the artifact and prints the document list, one line per document with
its identity count. **`--check` re-derives and compares against the committed artifact, printing
`STALE: …` and exiting 1 on drift, and `the L2 withheld-document derivation re-derives` and exiting
0 otherwise.** This is the house shape and it is what Task 2 enrols.

**Run it in both modes and report all output and both exit codes verbatim:**

```
python tools/audit/gen_l2_withheld_documents.py
python tools/audit/gen_l2_withheld_documents.py --check
```

**Then take `python tools/audit/changed_paths.py` again and report it.** The only new path under
`tools/audit/` may be `l2_withheld_documents.json` and the tool itself. **A third is a STOP.**

---

## 4. Task 2 — enrol the new tool in the guard set

`tools/audit/gen_guard_state.py`'s own comment records the rule in its own words, at the boot pack's
entry: *"registered in the act that creates the tool — the standing new-tool rule."*

**Add exactly one entry to that file's `AUTHORED` list**, in the `tools/audit` block, in the form the
neighbouring entries use: the tool's path, `["--check"]`, and a `why` string saying what it guards —
that the L2 withheld-document derivation still re-derives from the ruled verdict table and the
register's data file, with its four STOPs riding with it. **`--check` and never the bare invocation**,
for the reason the boot pack's own entry gives: a bare run rewrites the artifact a ruling is taken
over.

**Nothing else in `gen_guard_state.py` changes.** No existing entry is edited, reordered or removed.
No other tool source is touched (B1).

---

## 5. Task 3 — `STATUS.md`, the forward bound, the two read-size generators, and the closing capture

**In this order and no other.**

**5(a) — the `STATUS.md` entry.** Write ONE new dated entry, at the head of the dated entries, in the
OI-222 pointer convention this file already uses: a POINTER whose whole is your report, restating
**no figure** (D-431). It says what this batch did — the derivation tool created, enrolled and run;
the document set printed for the user and **authored into nothing**; the pack generator untouched and
L2's pack unrendered — and that the batch **STOPPED at Ruling 6's own STOP**. **No existing sentence
of `STATUS.md` is rewritten or removed.** This is the last write to `STATUS.md` in this batch.

**5(b) — the forward bound.** Re-aim `tools/audit/gen_status_batch_bound.py` at
`ef4fad940d806edf8f84eb9a895f88d70a9bbcf2` and run its `--apply`, so the then-previous batch's
entries move to `STATUS_ARCHIVE.md` in the same act that writes this batch's own. **The bound as
`STATUS.md`'s own banner states it** — where the writing side read it, rather than at the ruling
record, which it did not open — is: *"an entry is SUPERSEDED the moment a later batch's close exists,
and this file keeps only the latest batch's entries"*, maintained forward at every batch close in the
same act that writes its own entries. Then run its `--check` and report the output. **If `--apply`
reports its already-in-the-archive STOP, report it whole and make no further change** — it means the
move has already happened and the bound is met.

**Do NOT read a green `--check` as proof the bound is met.** `OPEN_ITEMS.md` OI-379 is open on
exactly that: that tool is re-aimed by hand at every close and its `--check` reconciles only the
aiming currently authored, so a close that never re-aims it leaves the guard green and the bound
unmet. **Report the aiming you set and the entries the `--apply` actually moved, by name.** *(OI-379
is named here as `STATUS.md`'s own pointer paragraph states it; the row itself was not opened by the
writing side.)*

**The two 2026-09-02 entries do NOT move and are not to be moved by hand.** `STATUS.md`'s own
pointer records that they name no dispatch, so no aiming of that tool can identify them, and that
whether they ever move is a question standing with the user.

**5(c) — the two read-size generators, after 5(a) and 5(b) and not before:**

```
python tools/audit/gen_session_start_read_size.py
python tools/audit/gen_defense_share.py
python tools/audit/gen_session_start_read_size.py --check
python tools/audit/gen_defense_share.py --check
```

Report all four outputs and all four exit codes verbatim. **Both `--check` runs are expected to exit
0.** A `STOP:` line or a traceback from either is a STOP; **do not edit either tool** (B1).

**5(d) — the CLOSING GUARD CAPTURE**, taken after 5(c). Compare it against 0(e) **verdict by
verdict**.

> **THE CONDITION: no guard whose VERDICT was PASS at the opening capture may carry any other verdict
> at this capture.** A guard that moves FAIL → PASS is ALLOWED and REPORTED. **The newly enrolled
> guard has no verdict at the opening capture; its verdict here is expected PASS and is reported as
> found, not compared.** **No condition is written on any guard's printed output, on any count inside
> that text, or on the number of failing guards** — `gen_derivation_boot_pack.py --check` prints a
> line that moves whenever a source moves, and an equality over output would stop this batch for a
> green guard.

**One hazard, named rather than predicted.** `tools/audit/gen_guard_classification.py` reads the
artifact `gen_guard_state.py` writes. **`gen_guard_state.py`'s own comment** — not the
classification's — says of it: *"it refuses to re-derive while its verdicts and this file's
HISTORICAL table disagree"*, and that this is why it is run separately, after the guard set.
**Whether enrolling a new guard trips that refusal is not established by this dispatch**, the
classification's own source not having been opened by the writing side. Run the classification in its own stated order — after
the guard set — and **if it STOPS or goes red, report it whole and stop there. Do not repair it and
do not edit it** (B1).

---

## 6. The commit, and the push

**6(a) — the second commit, by explicit path, never a directory pathspec.** The candidate set is
exactly:

1. `tools/audit/gen_l2_withheld_documents.py`
2. `tools/audit/l2_withheld_documents.json`
3. `tools/audit/gen_guard_state.py`
4. `tools/audit/gen_status_batch_bound.py`
5. `tools/audit/status_batch_bound.json`
6. `tools/audit/session_start_read_size.json`
7. `tools/audit/defense_share.json`
8. `STATUS.md`
9. `STATUS_ARCHIVE.md`
10. `records/cc/instructions/cc_instruction_l2_withheld_documents_2026_09_21.md`
11. `records/cc/reports/cc_report_l2_withheld_documents_2026_09_21.md`
12. the guard set's own artifacts, **only those the enumeration actually reports as modified** —
    name each one in your report rather than assuming which moved.

**Prove the staged set is EXACTLY the candidate set and nothing else before committing.**

**HELD BACK, AND NAMED SO NOTHING SWEEPS THEM IN:** `tools/audit/claude_md_finer_archive.json`; and
the held-back population handoff entry 223 §0 names — the untracked `scratch_artifacts/` tree, the
two PDFs, `Claude outputs/`, `Codex research inventory/`, `docs/research_papers/polyph9-release/`
and the untracked `.mscx` under `tools/audit/derivation_exemplars/l0-l1/`. *(That population is
RELAYED: entry 223 §0 marks every member of it as relayed from CC's own §1(d) enumeration, and the
Cowork side has taken no enumeration of the working tree — it has no shell. **0(d)'s enumeration is
what establishes the actual untracked set; this list is a guide to it, not a statement of it.**)*
**Held back also: every other path the enumeration reports that the candidate set does not name.**
**Confirm in your report that each named path is absent from the staged set.** Report anything
unexpected and leave it.

**6(b) — push.** After both commits, push every branch that received them. `origin` is the fork;
`upstream`'s push is disabled and is not to be used. **If the push fails for any reason, REPORT IT;
do not skip it silently and never pass `--force`.** Name the pushed branches.

---

## 7. The report, and the STOP this batch ends on

`records/cc/reports/cc_report_l2_withheld_documents_2026_09_21.md`, carrying:

1. Task 0's pin; both refs; the four start-state proofs of 0(c) with what you found at each; the
   enumeration of 0(d); the opening capture with its path and every guard's verdict; and 0(f)'s five
   established members with each one's blob, size and last non-empty line, the staged set proved
   equal to the candidate set, and the first commit's hash.
2. **THE DERIVED DOCUMENT SET IN FULL** — every document, with the IN identities homed there and the
   count, exactly as the artifact carries it — together with the reconciliation's result in both
   directions and the IN count. **This is what goes to the user, and it is the point of the batch.**
3. Task 1's two invocations, their output and exit codes verbatim, and the enumeration taken after
   them.
4. Task 2's one added entry, quoted whole, and confirmation that nothing else in
   `tools/audit/gen_guard_state.py` changed.
5. Task 3's four parts: the `STATUS.md` entry quoted whole; the forward bound's `--apply` and
   `--check` output; the four generator outputs and exit codes; and the verdict-by-verdict comparison
   of the two captures, naming every guard that moved and in which direction, the newly enrolled
   guard's own verdict, and the statement that no PASS became anything else. Report the guard
   classification's result whatever it is.
6. The second commit's hash and the pushed branches.
7. **What you did NOT do**, named rather than counted — and in particular: that
   `tools/audit/gen_derivation_boot_pack.py` was not edited in any way and was never run bare; that
   nothing was authored into `WITHHELD`, `EXTRAS`, `VERDICTS`, `CRITERION` or `FROZEN`; that no pack
   directory was read for content, written or moved; that no governing document but `STATUS.md` was
   amended; and that no open-items row and no `D-NNN` was touched.

**THIS BATCH ENDS HERE.** The derived set is **printed and not authored**. Ruling 6 reserves its
confirmation to the user, and the second half of the pack-build dispatch is written only after he has
ruled on it.

**If any expected result does not appear, stop at that task and report it. Do not continue to the
next one, and do not resolve a bar that contradicts a task.**
