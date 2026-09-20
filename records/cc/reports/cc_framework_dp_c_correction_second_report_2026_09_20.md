# `FRAMEWORK.md` DP-C — the ruled narrowing, WRITTEN (report, 2026-09-20)

> **STATUS: DONE, ON THE RULED STOP FORM. NO STOP WAS MET.** Written by the CC run of
> `records/cc/instructions/cc_instruction_framework_dp_c_correction_second_2026_09_20.md`, which
> executes the user's ruling of 2026-09-20 — his words, *"I agree: A"* — recorded at
> `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seven.md` §1 item 4. It supersedes
> the first writing, which ran and stopped at its Task 1 with nothing written.
>
> **★ THE HEADLINE. The sentence is narrowed in place, with the former wording preserved, and
> NOTHING ELSE OF `FRAMEWORK.md` IS TOUCHED** — proven blob to blob against the file's own pin, not
> asserted: **ONE HUNK**, three lines out and forty-six in, the corrected paragraph and its
> correction note. **APPENDIX B IS BYTE-IDENTICAL.**
>
> **★ THE START STATE WAS EXACTLY WHAT §1 ALLOWS.** The guard run's failing set is the committed
> `failing_tools` set plus `gen_derivation_boot_pack.py --check` and nothing else, and that check's
> whole output is the single drift line §1 permits — no pack member named, no frozen-subject
> verification raised.
>
> **★ THE INHERITED MANIFEST MISMATCH'S CAUSE IS ESTABLISHED AND COMMITTED ALONE**, before
> `FRAMEWORK.md` was touched, so the correction could not mask it (**D-669**). It is a reading-pass
> extract the writing side edited on 2026-09-20, proven changed at a blob comparison against the
> manifest's own last commit.
>
> **★ NO FILE UNDER `tools/audit/derivation_boot_pack/` MOVED AT ANY POINT.** All twenty-four
> re-hash to the blobs they were pinned at, after each of the two write-mode runs and at the close;
> the three frozen subjects verify at their recorded digests.
>
> **★ THE PAPER WAS NOT OPENED.** The replacement text was written verbatim from the dispatch, whose
> §3(b) the writing side checked at the page images (entry 209 §2). This run re-verified nothing at
> the paper and carries no value out of it.
>
> **★ NOTHING IS SETTLED HERE.** This report takes no decision and proposes no wording. One
> observation and five guard denials are surfaced below; none was worked around.

## 0. The boot

The ordinary session-start read was performed in full before the named file was acted on — a
single-file opening instruction is not an exemption (ratified 2026-08-29, P-1; **D-230**):

1. `CLAUDE.md` at its ruled membership; `DECISIONS.md` **whole** (three calls); `STATUS.md` whole;
   and the derived gating answer at `tools/audit/nongating_apparatus_rows.json` →
   `★_the_live_gating_answer` → `gating_ids`, read at its live section through the identity list.
   **No row of the open-items register is touched by this batch**, so no gating verdict decides
   anything here.
2. `BUILD_AND_TEST.md` — **the condition was RE-ESTABLISHED at the file, not relayed, and is NOT
   MET, so the file was not read.** `CLAUDE.md`'s condition is *a session that builds, tests, or
   runs a measurement tool **whose command lives there***. This batch builds nothing and tests
   nothing, and searches of that file for `gen_derivation_boot_pack`, `guard_state`,
   `gen_guard_state`, `gen_status_batch_bound` and `run_guards` returned **no match**; the tools
   whose commands that file does carry are the corpus, batch and inversion-error tools, none of
   which this batch runs. *(The divergence the first run reported against the 2026-08-31 batch's
   looser reading stands unresolved; this run applied the rule's own words, as that run did.)*
3. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seven.md` **§1 items 2 to 4**.
4. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nine.md` **whole**.
5. `records/cc/reports/cc_framework_dp_c_correction_report_2026_09_20.md` **whole** — the first run.
6. This batch's dispatch, whole.

## 1. Task 0 — the pins

**Thirty-eight files pinned with `git hash-object -w` before any other act**: this file's dispatch,
every file §0 names, `FRAMEWORK.md`, the boot-pack manifest, `tools/audit/guard_state.json`,
`tools/audit/gen_derivation_boot_pack.py`, `tools/audit/claude_md_finer_archive.json`, and **all
twenty-four files under `tools/audit/derivation_boot_pack/`** — seven in `harmony-boundary`, seven
in `scoring-model`, ten in `l0-l1`. The list is at `<scratchpad>/pins.txt`.

**No read disagreed with its pin at any point.** Two cross-checks worth stating, because each is a
claim this batch could have made from memory and did not:

- **The ten `l0-l1` pins reproduce the first run's table exactly**, and `FRAMEWORK.md` pins at
  `a6a6ca3352` — the value that run pinned it at. Nothing moved between the two runs.
- **At the close, exactly three pinned files differ from their pins**: `FRAMEWORK.md`,
  `tools/audit/derivation_boot_pack.json` and `STATUS.md` — this batch's own three edits. Every
  other pin holds, `tools/audit/claude_md_finer_archive.json` among them (§6).

## 2. Task 1 — the start state, established item by item

### (a) The guard set — **AS §1 ALLOWS. NO STOP.**

`python tools/audit/gen_guard_state.py --check` → **exit 1**, closing line **78 guard(s) run, 16
failing, 4 not run, 19 historical record(s)**, under the heading `STALE vs the run: guard_state.json
does not re-derive`. The full line-by-line output is at `<scratchpad>/guard_task1.txt`.

**The measure is the failing SET, and it is exactly what §1 permits.** The run's sixteen failing
invocations are the fifteen the committed record names at `tools/audit/guard_state.json` →
`summary` → `failing_tools`, **plus `tools/audit/gen_derivation_boot_pack.py --check` and nothing
else**. The committed list is not restated here (**D-431**); the comparison was made against that
artifact, member by member, not against memory.

**And the one addition's output is the single line §1 admits.** Run on its own:

```
STALE: the derivation boot pack does not re-derive
  - derivation_boot_pack.json does not re-derive
```

**One drift line, naming the manifest only** — no pack member of any subject, and no
frozen-subject verification raised (a frozen mismatch raises a `STOP:` line instead of joining the
drift list, read at `verify_frozen` and `check_all`). So the second limb of §1's allowance holds
too.

**Reported and acted on in nothing, as §1 directs:** `gen_guard_state.py --check` exits **1**, and
the only stale line it prints is the heading quoted above — it prints no itemised stale diff. Its
own run count (78 run, 4 not run, 19 historical) differs from the committed record's, which is the
inherited condition the first run also reported. **This batch did not touch
`tools/audit/guard_state.json`.**

### (b) How many sites in `FRAMEWORK.md` carry the target sentence — **exactly two. NO STOP.**

| Search string | Lines returned |
|---|---|
| `26%` | **700**, **1600** |
| `tie-breaking` | **699**, **1600** |
| `tie breaking` | *(no match)* |

**Two sites and no third:** the main text at DP-C (the sentence spanning **699–701**, under
`**DP-C — Is segmentation decided before, with, or after chord identity?**` inside
`## 9. Architecture decisions` → `### The design points`) and Appendix B's candidate decomposition
**(d)** at **1600**, under `## S4. The candidate decompositions, enumerated`. The third-site STOP
does not fire.

### (c) Does §3(a)'s quotation stand in the file exactly as quoted — **YES. NO STOP.**

**Matched as a SUBSTRING and mechanically, not by eye**: a multiline search for the quoted words
returns **exactly one occurrence**. The scope statement §3(a) makes is confirmed at the object —
line 699 reads `reported by the work named.] One further measurement is worth carrying: with
perfect tie-breaking`, so the closing words of the preceding label `[FACT — each reported by the
work named.]` stand before the quote on the same line and are not part of it, exactly as the
dispatch states.

### (d) The tracked-modification shape — **AS §7 EXPECTS. NO STOP.**

Enumerated with the sanctioned tool, `python tools/audit/changed_paths.py` (**D-253**'s permitted
route; the file tools were used for every content read). **591 changed-path records**, of which
**ten are tracked modifications**:

- **Nine under `reading_pass/`** — eight in `extracts/`, one in `extracts_second_pass/` — which is
  the population §7 expects there, and for which a third backup dispatch is owed.
- **One outside it: `tools/audit/claude_md_finer_archive.json`**, the single exception §7 names.
  **This batch did not modify it, did not touch it and did not commit it**, and **at the close it
  still stands at the blob it was pinned at** (§6).

**The handoff half of §7's expectation holds as the dispatch states it:** every changed path under
`records/cowork/handoff/` is an **untracked addition**, not a tracked modification.

**No other tracked modification exists**, so that STOP does not fire.

## 3. Task 2 — the inherited manifest mismatch, established and committed alone

**Commit `f1119a772e63e0144dd06b26739007ee3bb8454f`**, carrying
`tools/audit/derivation_boot_pack.json` and nothing else, staged by explicit path.

### (a) What write mode can write — established at the generator BEFORE it was run

Read at `build()` and `write_all`: `build()` builds every subject of the authored `WITHHELD` table,
and `write_all` writes `OUT` — `tools/audit/derivation_boot_pack.json` — and then, per subject,
**`continue`s past any subject in `FROZEN` before `os.makedirs` or any file write**. `WITHHELD` and
`FROZEN` carry **the same three subjects** — `harmony-boundary`, `scoring-model`, `l0-l1` — so **in
write mode with no `--subject` the generator can write exactly one path: the manifest.** No
directory under `tools/audit/derivation_boot_pack/` is reachable by it. (Write mode does not call
`verify_frozen`; only `--check` does.)

### (b) Proven at the objects after the run

**No file under `tools/audit/derivation_boot_pack/` moved.** All twenty-four re-hash to their pins;
the only object that differs is the manifest. The STOP does not fire and no restore was needed.

### (c) The difference, key path by key path, with each record's input named at the generator

**Five records changed, and every one of them is ONE member's.** All sit under
`subjects.l0-l1.the_members_as_rendered[7]` — which is **member (8)**,
`08_the_five_research_extracts.md`, not member (7); the list excludes `00_READ_THIS_FIRST.md`, so
its index 7 is the eighth member. All five sit under that member's **`parts[0]`**:

| Changed key path | Was → now |
|---|---|
| `…[7].characters` | 76722 → 85833 |
| `…[7].parts[0].characters` | 19434 → 28545 |
| `…[7].parts[0].filters_applied[0].characters_removed` | 1266 → 2111 |
| `…[7].parts[0].filters_applied[0].the_text_removed` | *(the filtered text itself)* |
| `…[7].parts[0].spans[0].lines_rendered` | 297 → 415 |

**The member-level delta equals the part-level delta exactly (+9111), so no other part moved.**

**The input is named at the generator, and it is a SOURCE DOCUMENT rather than an authored table.**
`EXTRAS["l0-l1"]`'s member (8) builds `parts[0]` from
`reading_pass/extracts/pardo-birmingham-2002-algorithms-for-chordal-analysis.md`.

**And that input has changed since the manifest's own last commit** — the question §2 item 2 makes a
STOP if answered no. The manifest's last commit by `git log` on its path is
`54804de49ac593b532e804bcfb881366e3a018b5` (2026-09-17). At that commit the extract's blob is
`d62eac3c29ac7baba0fde9767e56d55f6f93c5c7`; on disk it is
`9a0d685c6ff3ca047ad97b45b3f3c6f1f7b4a60d`. **They differ.** That is exactly the shape the
generator's own `frozen_block` describes — a frozen subject's member records are built *"from the
sources AS THEY STAND TODAY"*, so a changed source moves the manifest while no pack directory moves.

**The changed text names its own act**, which is corroboration at the object rather than inference:
the new `the_text_removed` carries *"★ CORRECTED 2026-09-20 UNDER THE USER'S RULING. FORMER
WORDING, PRESERVED (#12)"*, matching what
`records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seven.md` §1 item 4 records the writing
side doing to that extract on 2026-09-20.

**No record's input was unnameable, and none changed whose input had not changed.** Neither STOP
fires.

### (d) `--check` after the regeneration

```
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
```

**Exit 0, printing the three frozen subjects**, as §2 item 3 requires.

## 4. Task 3 — the one correction

**Commit `bfc1348c3bccfadd5b210c84c49d3c6ac6560d3e`**, carrying `FRAMEWORK.md` and
`tools/audit/derivation_boot_pack.json`, staged by explicit path.

### (a) What was written

The quoted sentence was replaced by §3(b)'s text **verbatim**, re-wrapped to the file's own line
width and to nothing else, and §3(c)'s correction note was written **verbatim** immediately beneath
the corrected paragraph, separated by one blank line — the placement the two existing correction
notes of this file use (the one beneath *"Why metric strength earns its place"* in §5, and
*"★ GROUND 2 WAS NARROWED HERE"* at DP-K). **No percentage was summed, rounded or re-expressed**,
and the label `[FACT — each reported by the work named.]` standing before the replaced sentence was
not touched.

**The paper was not opened.** §3(b)'s text was written as the dispatch carries it; the check at the
printed pages 31–35, at the page images, is the writing side's act of 2026-09-20 recorded at
`records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nine.md` §2, and this run neither
repeated it nor carried any value out of the paper.

### (b) Proven blob to blob against the pin

`FRAMEWORK.md` pin `a6a6ca3352` → `113a901c8e`. The blob-to-blob difference is **ONE HUNK**, at
`@@ -697,7 +697,50 @@`: **three lines deleted, forty-six added** — nineteen of the corrected
paragraph, one blank, twenty-six of the note. Nothing else in the file differs.

**Every deleted word either still stands in the corrected paragraph or is preserved verbatim inside
the note — measured, not read off:** on a whitespace-normalised comparison the former sentence
occurs **once in the pinned file and once in the new one**, and the lead words
`reported by the work named.] One further measurement is worth carrying` occur **once** in the new
file. **APPENDIX B IS BYTE-IDENTICAL**: no hunk reaches it, and its own copy of the sentence is
present in both blobs, unchanged. No note is added to it and no caveat is added at the appendix's
head, so §3t of `records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md`
leaves its question exactly as OWED AND NOT BLOCKING as it found it. **No other passage of
`FRAMEWORK.md` is touched**, §14.1's restatement included.

### (c) The rendered objects

**The expectation was written before the act (#17(b)), from the generator.** `FRAMEWORK.md` is the
source of exactly one member — `l0-l1`'s member **(7)**,
`07_the_charter_the_layers_and_the_decisions.md`, whose `parts[0]` takes two spans,
`## 5. Building-block view` and `## 9. Architecture decisions`. DP-C sits inside the second. So the
records predicted to move were that member's `characters`, its `parts[0].characters`, and
`parts[0].spans[1].lines_rendered` — and no others.

**Measured after the re-run, it is exactly those three and nothing else:**

| Changed key path | Was → now |
|---|---|
| `subjects.l0-l1.the_members_as_rendered[6].characters` | 29123 → 33067 |
| `…[6].parts[0].characters` | 29122 → 33066 |
| `…[6].parts[0].spans[1].lines_rendered` | 197 → 240 |

The span grew by **43** lines, which is the 46-for-3 replacement exactly. **No record built from any
other source moved**, so that STOP does not fire. **No file under
`tools/audit/derivation_boot_pack/` moved** — all twenty-four re-hash to their pins again. `--check`
**passes**, printing the same three frozen subjects at their recorded blobs.

### (d) The guard set after the edit — **exactly the committed failing set. NO STOP.**

The whole guard set was re-run: closing line **78 guard(s) run, 15 failing, 4 not run, 19 historical
record(s)**. **The failing set is exactly the committed `failing_tools` at
`tools/audit/guard_state.json` → `summary`, and nothing more** — `gen_derivation_boot_pack.py
--check` has left it, Task 2 having cured its cause. **No guard that passed at Task 1 fails now.**
`gen_guard_state.py --check` exits **1** again, printing the same single stale heading and the same
differing run count; both are reported and acted on in nothing, as §3(e) item 5 directs. Output at
`<scratchpad>/guard_task3.txt`.

## 5. Task 4 — the close

1. **`STATUS.md`** carries this batch's own entry as a **POINTER** to this report (the OI-222
   convention), written **before** the forward bound ran, so that the `Last updated: ` prefix had
   moved to it — the order the tool's own comment requires and whose reverse it STOPs on.
2. **The forward bound was re-aimed and applied.** All six authored inputs moved together:
   `BASE_COMMIT` to this batch's last task commit `bfc1348c3b`, `PREVIOUS_BATCH_DISPATCH` to
   `cc_instruction_backup_second_commit_and_push_2026_09_19.md`, `ACT_DATE` to 2026-09-20,
   `DISPATCH` and `TASK` to this dispatch and its Task 4, `MOVE_KIND` re-aimed to the same value it
   already carried — `ordinary`, which is what this move is — and `PREVIOUS_AIMINGS` **appended to
   rather than replaced** (#12), this batch's own row added once, the second backup's row left where
   that batch recorded it. `--apply` moved **one** entry, and its reconciliation is green in both
   limbs: byte-present in the archive exactly once, absent from the must-read. `--check` re-derives,
   exit 0. The archive header written is the ORDINARY form and names this dispatch's Task 4.
3. **`--apply` wrote exactly the three paths its own documentation names** — `STATUS.md`,
   `STATUS_ARCHIVE.md` and `tools/audit/status_batch_bound.json` — established at `apply_move()` and
   `main()` before it ran, and **measured after**: a changed-path enumeration taken before and after
   the run differs by exactly two new records, `STATUS_ARCHIVE.md` and the artifact, `STATUS.md`
   having already been modified by this batch's own entry. **No path outside that set was written**,
   so that STOP does not fire.
4. **The close commit** is `df76bbd7ac33ec06b8fe865556a99b64a12753b0`, carrying `STATUS.md`, the
   three paths `--apply` wrote, this dispatch, the first writing, the first run's report and this
   report — each staged by explicit path.
5. **The push succeeded.** `origin` is `https://github.com/slimvince/MuseScore`, the user's fork;
   `upstream` is push-disabled and stayed so. **One branch received commits this session —
   `master`** — and `git push origin master` reported `fe2c28b33a..df76bbd7ac  master -> master`,
   carrying all three of this batch's commits: **`f1119a772e63e0144dd06b26739007ee3bb8454f`**
   (Task 2), **`bfc1348c3bccfadd5b210c84c49d3c6ac6560d3e`** (Task 3) and
   **`df76bbd7ac33ec06b8fe865556a99b64a12753b0`** (the close). No `--force` was used and no push
   failed.

### The standing self-check

Run before this report was written, **at the diffs on disk and not from the memory of writing
them**: the `FRAMEWORK.md` blob-to-blob hunk; both manifest key diffs; the re-aimed tool blob to
blob; the forward-bound artifact key diff; the archive header at its own line; and the final
re-hash of all thirty-eight pins.

Checked against the guiding principles, the conventions, the gate and threshold policies and
`DEFECT_TYPES.md`. **One correction was made to this batch's own writing during the check**, and it
is reported rather than passed over: the re-aiming comment first read *"ALL SIX authored inputs
moved together"* with no qualification, which reads as a claim that six VALUES changed when
`MOVE_KIND`'s did not. The clause now says so in terms. A line the same edit left at 105 characters
was re-wrapped to the file's own width; **no line this batch wrote exceeds 100 characters**, against
that file's own 101–102 ceiling.

Three points stated positively, each a rule this batch could have broken and did not:

- **#17(b) / #17(f) / D-431** — the manifest's movement at Task 3 was **predicted before the act**
  and held exactly. The committed failing set is named by its artifact and not listed; no value of
  this project's own measurement is restated. Every figure above is this run's own establishment,
  named with the act that produced it.
- **D-669** — the inherited mismatch's cause was established at the objects and committed alone
  before the mechanism the correction touches; no fix was taken on a named-but-unasserted candidate.
- **D-646 / #12** — nothing was written into any frozen pack directory, and the former wording of
  the corrected sentence is preserved in place and proven present.

**One observation, surfaced and NOT acted on.** §3(b)'s ruled verbatim text and §3(c)'s note use
*figure* in the non-musical sense (*"the figure bears on labeling"*). `CLAUDE.md`'s disambiguation
convention reserves bare *figure* for figuration and asks for *number* / *value*. **The text was
written verbatim as ordered** — altering ruled text would be an act outside §7 — and the collision
already stands in this document's neighbouring correction note, which the convention's
do-not-rename-unilaterally clause covers. Recorded here so the choice is visible; nothing is
settled by it.

### Five shell commands were denied by the read guard

§0 asks that any denied command be quoted verbatim with the route taken instead. **None was retried
in another dialect to obtain the same forbidden read.**

1. `python -c "..."` reading `tools/audit/nongating_apparatus_rows.json` — denied as interpreter
   code carrying a literal repository path. **Route taken:** Grep and Read on that file.
2. `grep -v '^??' "$SP/changed_open.txt" | head -40; grep -vc '^??' "$SP/changed_open.txt"` — denied,
   the guard unable to resolve `$SP` and denying on indeterminate. **Route taken:** the Grep file
   tool on the scratchpad file by absolute path.
3. `git add -- tools/audit/derivation_boot_pack.json && git status --porcelain -- …` — denied for
   the `git status` limb. **Route taken:** `git add` alone, then
   `python tools/audit/changed_paths.py --staged`.
4. `git diff --unified=1 "$OLDT" "$NEWT"` — denied, the guard unable to resolve the variables to
   hashes. **Route taken:** the hashes were printed first and passed as literals.
5. `awk 'length>100 {print …}' tools/audit/gen_status_batch_bound.py` — denied as a shell read of
   working-tree content. **Route taken:** the Grep file tool with a length pattern.

## 6. The footprint

**Edited:** `FRAMEWORK.md` (the one correction of §3 and nothing else);
`tools/audit/derivation_boot_pack.json` (regenerated twice, Task 2 and Task 3(e)); `STATUS.md`;
`STATUS_ARCHIVE.md`, `tools/audit/status_batch_bound.json` and
`tools/audit/gen_status_batch_bound.py` — the three the forward bound's own re-aiming and `--apply`
account for, the tool source **excepted by name** by Ruling 5 of
`records/cowork/rulings/cowork_rulings_2026_08_26_amendment_landing_sitting.md`. **Created:** this
report, and — outside the repository, in the session scratchpad — the working files named above.

**Written into NO directory under `tools/audit/derivation_boot_pack/`**, frozen or otherwise.
**No file under it moved at any point**, proven by re-hash against the pins after each write-mode
run and at the close.

**Not done at all:** **no paper opened**; no build, no test, no golden, no measurement of the
analysis; nothing under `tools/corpus/`, `tools/robust_stop/` or `src/`; **no extract edited**; **no
other governing document amended**; **no open-items row created, flipped or discarded**; **no
decisions-register entry and no `D-NNN` allocated**; no score staged, no brief written, no session
booted; **`tools/audit/guard_state.json` NOT regenerated**.

**`tools/audit/claude_md_finer_archive.json` STILL STANDS AS PINNED** at
`1df4f20771b6782cbb965c293db4d445bc7ec892`. This batch did not touch it, did not commit it and does
not know what modified it.

**The close state, measured.** Fourteen tracked modifications remain: the **ten this batch
inherited** — nine under `reading_pass/`, plus `claude_md_finer_archive.json`, each unchanged — and
**four of this batch's own**, `STATUS.md`, `STATUS_ARCHIVE.md`,
`tools/audit/gen_status_batch_bound.py` and `tools/audit/status_batch_bound.json`, all of which the
close commits. `FRAMEWORK.md` and the manifest are no longer modified, having been committed.
**No tracked modification this batch did not make appeared**, so that STOP does not fire.

## 7. Done

**DONE.** The boot, in full, with the `BUILD_AND_TEST.md` condition re-established and found not
met. **Task 0**: thirty-eight files pinned, every pin re-hashed at the close, only this batch's own
three edits differing. **Task 1**: all four establishments — the guard set's failing set against the
committed one, the boot-pack check's single drift line, the two sentence sites, the §3(a) quotation
matched as a substring, and the tracked-modification shape. **Task 2**: the inherited mismatch's
cause established record by record and committed alone as `f1119a772e`. **Task 3**: the one
correction and nothing else, proven blob to blob, with Appendix B byte-identical, the manifest moving
exactly as predicted, `--check` passing and the closing failing set exactly the committed one —
committed as `bfc1348c3b`. **Task 4**: the `STATUS.md` pointer entry, the forward bound re-aimed and
applied with its three documented outputs and nothing else, the close commit `df76bbd7ac`, and the
push of `master` to `origin` carrying all three commits. The self-check. This report.

**★ ONE ERROR OF THIS RUN'S OWN, CAUGHT AT THE OBJECT AND CORRECTED, recorded rather than passed
over.** The close commit's full hash was first written into §5 from the abbreviation git printed,
with the remaining characters INVENTED rather than read. It was caught by verifying the hash at
`git rev-parse HEAD` and corrected to the value above before this report was committed. Nothing
else in this report carries a hash that was not read at its own command's output. *(The
report-amending commit below is what carries the correction; the three commits §5 names are
unchanged by it.)*

**NO STOP OF §6 WAS MET.** No read disagreed with its pin; no failing guard at Task 1 outside what
§1 allows and no boot-pack drift line other than the manifest's; no third site of the sentence;
§3(a)'s quoted words matched the file; no file under `tools/audit/derivation_boot_pack/` moved; at
Task 2 every changed manifest record's input was nameable at the generator and had changed since the
manifest's last commit; at Task 3 no moved manifest record was built from any source other than
`FRAMEWORK.md`; the blob-to-blob difference shows no deleted word neither standing nor preserved; no
change to Appendix B; no guard that passed at Task 1 failed after the edit; `--apply` wrote no path
its own documentation does not name; the paper was not opened; and no act outside §7 was taken.

---

*Provenance: written by the CC run of
`records/cc/instructions/cc_instruction_framework_dp_c_correction_second_2026_09_20.md`, 2026-09-20.
Every claim above was established at the object named beside it in this session: the guard set's
output at its own two runs; the committed failing set at `tools/audit/guard_state.json`'s `summary`;
the boot-pack check at its own three runs; `build()`, `write_all`, `check_all`, `verify_frozen`,
`frozen_block`, `FROZEN`, `WITHHELD` and `EXTRAS` at `tools/audit/gen_derivation_boot_pack.py`; the
two sentence sites, the §3(a) quotation and the corrected region at `FRAMEWORK.md` and at its own
blobs by explicit hash; the manifest's two differences at key-path comparisons of its blobs by
explicit hash; the extract's two blobs and the manifest's last commit at `git log` and `git rev-parse`
by path and hash; the tracked and untracked population at `tools/audit/changed_paths.py`, four times;
`apply_move()`, `moved_entries()`, `build()` and `main()` at `tools/audit/gen_status_batch_bound.py`.
The first run's report and both handoff entries were read whole. **The verification at the paper is
the writing side's and was not repeated here; no value of that paper is carried out of this run.** No
value of this project's own measurement is restated (#17f, **D-431**). No decisions-register identity
is allocated, and no open-items row was created or flipped.*
