# CC REPORT — L2's withheld-family reading file rendered from the verdict table, with two small repairs at the front (2026-09-05)

> **STATUS: REPORT.** Written by CC executing `cc_instruction_l2_reading_file_2026_09_05.md`, Tasks 0
> to 5, after the ordinary session-start read in full — `CLAUDE.md`, the `DECISIONS.md` INDEX,
> `STATUS.md`, and the derived gating answer at
> `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids` — which
> binds even when the opening instruction names a single file (Ruling 5 of
> `cowork_rulings_2026_08_29_ratification_sitting.md`, P-1). `BUILD_AND_TEST.md` was **NOT** read and
> the ground is recorded: its read is conditional on a build, a test, or a measurement tool whose
> command lives there, and **none of this batch's commands is one** — established rather than
> assumed, by searching that file for every tool this batch runs and finding no match.
>
> **NO STOP CONDITION FIRED. Nothing was withheld, no verdict moved, no pack was rendered and no
> session was booted.** This report recommends nothing and takes no position on any list or any
> candidate.

---

## 1. The tip at boot and the tip at close

| | commit | read where |
|---|---|---|
| **at boot** | `8457c97445ff9a6c506fe999128681b80969e9ba` | `.git/refs/heads/master` and `.git/refs/remotes/origin/master`, both with the file tools — equal, and equal to the hash the dispatch declares, so STOP condition 1 did not fire |
| **at close** | *written into this cell by the end-state commit* | the tip after the Task 5 commit, read at both ref files with the file tools and **written into the end-state commit**, on the convention the two preceding reports state at their own tables: a commit cannot carry its own hash, so naming the Task 3 tip here would leave the row stale. **This cell is left empty of any value until that hash has been read** — no provisional or stand-in hash is written into it at any point |

**Every commit of this batch**, each hash read at **both** ref files with the file tools immediately
after its push — never from a push's own output:

| task | commit | what it carries |
|---|---|---|
| Task 0 | `03abbdec0fa825e04b1e6854d5bdbd1c4bf2a80a` | the dispatch and the Task 0 enumeration artifact — **two paths** |
| Task 1(a) | `02f28d1cbad9d279efcc4cfd6e8c25dd29970bc5` | the two regenerated artifacts — **two paths** |
| Task 1(b) | `3cd4bf4e7b71eeab70adc54b9b41e5419398720c` | `open_items/OI-378.md` — **one path**, `12 insertions(+)`, **zero deletions** |
| Task 2 | `1fb0a97a72f6155a1436c85f8a1d4c8892b00bab` | the new tool, its guard enrolment, the rendered reading file — **three paths** |
| Task 3 | `9a124b77d2a5772c32fc9cc00e53e96e0aff3d18` | the Task 3 enumeration artifact alone |
| Task 5 | *written into this cell by the end-state commit* | `STATUS.md` and this report — **two paths** |
| the end state | *the commit that carries this table's close-tip cells* | the regenerated guard artifact, the close section in `cowork_away_returns.md`, and this table's two close-tip cells |

**On the close test.** Following the practice of the preceding batch, the close section and the
end-state guard artifact go in the **same** commit, not one apart. The preceding batch recorded that
the written test asks for one further commit after the close section while the last several batches
have used the single-commit form; this batch uses the single-commit form and says so, as that batch
did. Whether the wording should be amended is the user's and is not urgent.

---

## 2. Task 0 — the dispatch landed, and the tree it was landed into

`python tools/audit/changed_paths.py --json tools/audit/changed_paths_l2_reading_file_task0.json`
reported **848 changed path records, EVERY ONE of them untracked (`??`) — ZERO tracked
modifications.** **STOP condition 2 did not fire.**

The count of untracked records was not read off the listing by eye: the artifact was searched for
`"code": "??"` and returned **848 occurrences against 848 records**, so the all-untracked claim is a
measurement over the whole population rather than an impression of a long list.

The dispatch was present as an untracked addition, and the standing untracked historical `cc_*` root
population was present and correctly not landed. The dispatch is explicit that the clean tree was an
**expectation and not a measured start state** — the writing side has no enumeration tool — and the
expectation held.

Two paths were committed, exactly as the fenced list and the heading both name.

---

## 3. Task 1(a) — the two staled artifacts regenerated, and the proof that only positions moved

**`BEFORE` = `03abbdec0fa825e04b1e6854d5bdbd1c4bf2a80a`** and
**`AFTER` = `02f28d1cbad9d279efcc4cfd6e8c25dd29970bc5`**, each read at both ref files with the file
tools.

**Both regenerations ran without a STOP and both `--check` runs exit 0 afterwards:**

| run | output | exit |
|---|---|---|
| `gen_phase3_gate_partition.py` | `wrote C:\s\MS\tools\audit\phase3_gate_partition.json` / `items 17: GATING 14, NON-GATING 3 ['P2-C4', 'P2-TRUST', 'P2-OI288a']` / `quotes located 20/20; anchor drift 4` | 0 |
| `gen_phase3_gate_partition.py --check` | `PASS: phase3_gate_partition.json re-derives byte-identically (14 gating / 3 non-gating of 17; 20/20 quotes located)` | 0 |
| `gen_l0_l1_outgoing_population.py` | `named members: 11` / `specification set members as read: 26` / `files with an admitting hit: 112 (outside the named members: 103)` / `of those IN the specification set: 18; residue: 85` / `population in comparison order: 29 entries (before the cut: 114)` / `size stop reached: False (threshold 40, evaluated on the IN-set count)` / `wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json` | 0 |
| `gen_l0_l1_outgoing_population.py --check` | `l0_l1_outgoing_population.json re-derives` | 0 |

**NO TOOL WAS EDITED AND NO `expected_line` WAS RE-AIMED.** Neither
`gen_phase3_gate_partition.py` nor `gen_l0_l1_outgoing_population.py` was opened for writing; the
only act was running each in its ordinary write mode and then in `--check`. A tool edit is a separate
act and the dispatch forbids it here.

### The object comparison, IN FULL

The four committed versions were taken as git objects **by explicit hash** (D-253's licence) and
compared by the dispatch's read-only script, which never touches the repository:

```
== phase3_gate_partition.json: 12 differing leaf path(s)
   ok   items/[15]/source_verification/drift/actual/[0] | 321 -> 322
   ok   items/[15]/source_verification/found_lines/[0] | 321 -> 322
   ok   items/[16]/source_verification/drift/actual/[0] | 327 -> 328
   ok   items/[16]/source_verification/found_lines/[0] | 327 -> 328
   ok   quote_verification/anchor_drift/[2]/drift/actual/[0] | 321 -> 322
   ok   quote_verification/anchor_drift/[2]/found_lines/[0] | 321 -> 322
   ok   quote_verification/anchor_drift/[3]/drift/actual/[0] | 327 -> 328
   ok   quote_verification/anchor_drift/[3]/found_lines/[0] | 327 -> 328
   ok   quote_verification/records/[18]/drift/actual/[0] | 321 -> 322
   ok   quote_verification/records/[18]/found_lines/[0] | 321 -> 322
   ok   quote_verification/records/[19]/drift/actual/[0] | 327 -> 328
   ok   quote_verification/records/[19]/found_lines/[0] | 327 -> 328
== phase3_gate_partition.json: ALL PERMITTED
== l0_l1_outgoing_population.json: 11 differing leaf path(s)
   ok   the_term_search/per_file/OPEN_ITEMS.md/admitting_hits/[9]/line_number | 395 -> 396
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[25]/line_number | 314 -> 315
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[26]/line_number | 315 -> 316
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[27]/line_number | 330 -> 331
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[28]/line_number | 330 -> 331
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[29]/line_number | 355 -> 356
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[30]/line_number | 359 -> 360
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[31]/line_number | 361 -> 362
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[32]/line_number | 366 -> 367
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[33]/line_number | 410 -> 411
   ok   the_term_search/per_file/OPEN_ITEMS.md/recorded_hits/[34]/line_number | 451 -> 452
== l0_l1_outgoing_population.json: ALL PERMITTED
RESULT: POSITIONS ONLY
```

**Twenty-three differing leaves in all, and EVERY ONE printed `ok`.** **STOP condition 5 did not
fire.**

**No leaf printed `BAD`, so the two reportable-but-permitted kinds did not arise at all**: there was
**no run stamp** among the differences — no time, no HEAD hash — and **no summary count** moved. That
is a stronger outcome than the dispatch anticipated, and it is stated as a fact rather than as a
success: the dispatch names run stamps and position-derived counts as things that MAY move and must
then be named; none did, so there is nothing to name.

**Three properties of the difference set, each a check on the stated cause rather than a restatement
of it:**

1. **Every value moved by exactly +1** — 321→322, 327→328, 395→396, and so on — which is the
   signature of a single inserted row, not of content moving.
2. **Every moved value sits at or below its file's OI-378 insertion point.** The dispatch states the
   OI-378 row was inserted at line 278 of `OPEN_ITEMS.md`; every shifted position is above 278 in
   value and therefore below it in the file.
3. **No hit was ADDED to `l0_l1_outgoing_population.json`.** The dispatch's own third-pass note
   records this as the live risk — that tool searches `OPEN_ITEMS.md` for its admitting and recorded
   terms, so a new row could add a HIT and not merely shift positions, and a hit would be content and
   would fire condition 5. **The comparison settles it: every difference in that file is a
   `line_number` of an EXISTING hit record; no record was added, removed or re-indexed, and the
   `admitting_hits` and `recorded_hits` arrays are the same length before and after.** The risk was
   real and did not materialise.

**What this batch deliberately did NOT do here**, named so it is not mistaken for an oversight: the
`expected_line` values in `gen_phase3_gate_partition.py` are **not** re-aimed. That artifact
therefore still carries `anchor_ok: false` and a `drift` record for the `OPEN_ITEMS.md` quotes below
the insertion point — `anchor drift 4`, as the regeneration's own output says — exactly as it already
did for the re-aimings of 2026-08-03. Re-aiming is a tool edit and is the user's to call for.

---

## 4. Task 1(b) — the fourth guard observation appended to OI-378's detail file

The note was appended **after** the file's own closing line
*"Resolution belongs in the INDEX row; dated notes may be appended here."*, which is what that line
permits. **No existing line of the detail file changed, and the `OPEN_ITEMS.md` INDEX was not
touched.**

Before writing, the file's line endings were established rather than assumed — a search for a
carriage return returned **zero matches**, so the file is LF-terminated and the appended note is LF
too, leaving no mixed-ending artifact.

The appended text, re-read at the file after the edit (lines 101–112):

```

---

**Dated note, 2026-09-05 (CC, `cc_instruction_l2_reading_file_2026_09_05.md` Task 1(b)) — a FOURTH
observation, relayed from `cc_report_l2_verdict_pass_2026_09_05.md` §7 departure 3 and not
re-measured.** A `python -c` that opened `cc_report_l2_candidate_list_2026_09_05.md` and
`cowork_away_returns.md` — two plain RELATIVE repository paths inside interpreter code — was
**DENIED** by the guard, the denial naming `CLAUDE.md`'s conventions, D-253 and the guard-family
ruling of 2026-08-08. It differs from observation (3) above in the paths being relative rather than
absolute, and in the utility from observation (1), which was not denied. **As before: no cause is
asserted, none may be read in, no remedy is proposed, and the INDEX row is unchanged** — a fourth
data point is recorded, not a conclusion drawn.
```

**The two checks, both PASSING as expected — the INDEX did not change:**

| check | output | exit |
|---|---|---|
| `tools/audit/index_status_lint.py` | `INDEX STATUS LINT: OPEN_ITEMS.md` / `INDEX STATUS LINT: PASS — every status cell opens with one canonical token, and every row splits.` | 0 |
| `tools/open_items_split_check.py` | `living mode: index=378 detail=378 baseline=200 post-baseline=178` / `OVERALL PASS — bijection holds, no detail file carries a status of its own, and all 200 original items stay byte-verbatim` | 0 |

**The zero-deletion proof at the commit object** (`git show --stat 3cd4bf4e7b`):

```
 open_items/OI-378.md | 12 ++++++++++++
 1 file changed, 12 insertions(+)
```

**Twelve insertions, zero deletions, ONE path.**

**A difference from the preceding batch, stated rather than absorbed.** The dispatch anticipates that
the split check may rewrite `open_items/register_check.json`, "as it did last batch". **It did not
this time.** That path was staged alongside the detail file, and the commit object shows one file
changed — so the staging was a no-op and the artifact was already at the state a fresh run produces.
Nothing was forced either way.

---

## 5. Task 2 — the generator, its enrolment, and the rendered reading file

### 5.1 The two object checks the dispatch requires before running the tool

**(1) `tools/audit/output_encoding.py` exists.** Confirmed with `Glob`, which returned
`tools\audit\output_encoding.py`. The import in the new tool is the same one the boot-pack generator
already makes from the same directory.

**(2) The charter string needed NO correction.** Read at `FRAMEWORK.md` with the file tools:

- the heading `### L2 — The tonal reading. The one entangled decision.` occurs at **line 386**, and an
  anchored search for it returns **exactly one** match;
- the bold-labelled question occupies **lines 388–390**, wrapped across three lines with two-space
  continuation indents, byte-for-byte as the tool's `charter_label` + `charter_sentence` strings
  spell it;
- the sentence is restated at **lines 1699–1701** under an *italic* label, which the needle
  deliberately does not match — so the labelled form the tool searches for occurs **once**, which is
  what its `locate_once` demands.

**The tool STOPPED on neither anchor, and no string in the tool was corrected.** The dispatch's
contingency — correct the tool's string to the file's exact bytes and declare it — was not needed and
was not exercised. The dispatch's own fact-check of this point reproduces exactly.

### 5.2 The tool and its enrolment

`tools/audit/gen_withheld_family_reading.py` was written with the dispatch's content. It imports
`VERDICTS`, `CRITERION`, the keyword tuple and `group_title()` from the boot-pack generator rather
than copying any of them (#6), and locates the charter sentence at its home on every run.

The guard-set entry was inserted in `tools/audit/gen_guard_state.py` **immediately after** the entry
ending `moving the population silently"),` and **before** the comment line
`# ---- AUTHORED 2026-08-15, cc_instruction_artifact_inventory.md`, both anchors located at the file
before the edit. **Nothing else in that file changed.**

### 5.3 The render, and the two checks around it

| run | output | exit |
|---|---|---|
| `gen_withheld_family_reading.py --subject l2` | `wrote ratification_surfaces/cowork_withheld_family_l2_reading.md (125866 bytes)` | 0 |
| `gen_withheld_family_reading.py --subject l2 --check` | `PASS: ratification_surfaces/cowork_withheld_family_l2_reading.md re-renders byte-identically` | 0 |
| `gen_derivation_boot_pack.py --check` | `the derivation boot pack re-derives` / `harmony-boundary: FROZEN — 7 file(s) at their recorded blobs` / `l0-l1: FROZEN — 10 file(s) at their recorded blobs` / `scoring-model: FROZEN — 7 file(s) at their recorded blobs` | 0 |

**No `STOP:` line was emitted on any run, so STOP condition 6 did not fire.** The boot-pack
generator's `--check` exits 0 with all three built subjects re-deriving FROZEN at their recorded
blobs, so **STOP condition 3 did not fire** — and no committed manifest was adjusted to make it pass.

### 5.4 The counts read at the rendered file

| where | figure |
|---|---|
| LIST ONE heading | `**110 entries.**` |
| LIST TWO heading | `**132 entries.**` |
| LIST THREE heading | `**2 entries.**` |
| summary table's last row | `\| **all** \| \| **244** \| \| \| \| **110** \| **132** \| **2** \|` |
| table rows matching `^\| D-\d+ \|` | **244** |

**IN 110 / OUT 132 / UNPLACED 2, total 244, and 244 table rows in all — the figures the dispatch
names. STOP condition 7 did not fire.**

Two independent consistency properties, checked rather than assumed: the three list counts sum to
244, and the summary table's per-group IN/OUT/UNPLACED cells sum to that group's candidate count in
every one of the eighteen rows.

### 5.5 The rendered file, read

The banner, §1 to §5, the head of each of the three lists, and §6 to §8 were read with the file
tools. The file carries, in order: the STATUS banner declaring every verdict a PROPOSAL and naming
Ruling 81; the generated-file warning; §1's vocabulary including the explicit note that register
group **E** (*Layer 2 — the slicer*) and the subject **L2** are different units in two numbering
schemes; §2's charter question with the located heading quoted; §3's statement that **no ruling names
an oracle passage for L2**, sourced rather than asserted; §4's derivation with its eighteen-row
sizing table and its UNMEASURED-reach bound; §5's three-way test with the default-nothing rule; the
three lists; §6's four not-yet items including the `DATE` gap; §7's what-you-are-asked-to-rule; §8's
what-the-ruling-does-not-do; and the provenance line.

**The file makes no recommendation on any list or any UNPLACED entry** — §5 states the
default-nothing rule, LIST THREE's own gloss states that no recommendation is made on any of them
(D-658), and §7 says in terms that the file recommends neither IN nor OUT for either UNPLACED entry.

---

## 6. Task 3 — nothing else moved, and the guard set

`python tools/audit/changed_paths.py --json tools/audit/changed_paths_l2_reading_file_task3.json`
reported **847 changed path records, EVERY ONE untracked (`??`) — ZERO tracked modifications**, the
all-untracked claim again measured over the whole population (847 `"code": "??"` occurrences against
847 records) rather than read by eye.

**A search of the Task 3 artifact for `derivation_boot_pack` returned NO matches at all** — nothing
under `tools/audit/derivation_boot_pack/` and not `tools/audit/derivation_boot_pack.json` appears as
modified, or in any state. **STOP condition 4 did not fire.**

**The record count reconciles exactly, which is itself a check that nothing unexpected appeared.**
Task 0 saw 848 untracked records; the dispatch became tracked at Task 0's commit, removing one; each
enumeration artifact is written by the run that lists, so neither appears in its own listing, and
both are tracked once committed; the new tool and the rendered reading file were committed and are
therefore tracked, not untracked. 848 − 1 = **847**, which is what Task 3 measured.

### The standing guard set

`python tools/audit/gen_guard_state.py --check` — **exit 1, and the first line is
`STALE vs the run: guard_state.json does not re-derive`.** **That is DRIFT, not a HALT**, which is
what the dispatch expects: the population grew by one and two artifacts were regenerated, so the
committed `guard_state.json` no longer re-derives.

```
77 guard(s) run, 10 failing, 4 not run, 16 historical record(s)
```

**The three verdicts this batch's own acts bear on:**

| guard | verdict |
|---|---|
| `tools/audit/gen_withheld_family_reading.py --subject l2 --check` | **PASS** |
| `tools/audit/gen_phase3_gate_partition.py --check` | **PASS** |
| `tools/audit/gen_l0_l1_outgoing_population.py --check` | **PASS** |

**The new tool appears in the run as a PASSING guard, not as a HALT naming it a candidate without an
authored invocation — so the enrolment in Task 2(b) landed as written, and STOP condition 6 did not
fire.**

**The ten failing are EXACTLY the ten inherited, established by comparison against the committed
artifact rather than recalled.** The committed `guard_state.json` recorded `run 76, passing 64,
failing 12` — the ten inherited plus the two the previous batch caused and deliberately left. Those
two now pass. The ten that remain:

1. `tools/audit/gen_filing_convention_application.py --check`
2. `tools/audit/gen_artifact_inventory.py --check`
3. `tools/audit/gen_artifact_inventory_surface.py --check`
4. `tools/audit/gen_test_construction_evidence.py --check`
5. `tools/audit/gen_retirement_caller_check.py --check`
6. `tools/audit/decisions/apply_soft_discard.py --check`
7. `tools/audit/decisions/apply_residue_discard.py --check`
8. `tools/audit/gen_epoch_write_path.py --check`
9. `tools/audit/gen_recognizer_establishment_sort.py --check`
10. `tools/audit/decisions/gen_cluster_dispositions.py --verify`

**None is this batch's, and this batch added no eleventh.** Nothing was regenerated at Task 3, as the
dispatch orders; the end state regenerates the guard artifact.

**`gen_session_start_read_size.py --check` PASSES.** The dispatch provides for regenerating the
read-size measurement "where this batch's own acts staled it" — **this batch's acts did not stale
it**, so it is not regenerated and nothing is touched to make a number come out. This differs from
the preceding batch, whose regenerated gating answer did stale it.

**The new tool's `--check` was run once more on its own after the guard set: `PASS: … re-renders
byte-identically`, exit 0.**

---

## 7. Any STOP reached

**NONE.** All seven STOP conditions were tested rather than assumed:

1. **The tip at boot** was `8457c97445ff9a6c506fe999128681b80969e9ba` at both ref files, the declared
   hash. Did not fire; `cowork_away_returns.md` was not opened as a stop response.
2. **The enumeration reported ZERO tracked modifications** at boot, measured over all 848 records.
   Did not fire.
3. **`gen_derivation_boot_pack.py --check` exits 0**, all three subjects FROZEN at their recorded
   blobs. Did not fire.
4. **Nothing under the pack directory or the manifest appears in the Task 3 enumeration in any
   state.** Did not fire.
5. **The object comparison returned `POSITIONS ONLY`** with all 23 differing leaves permitted and no
   `BAD` leaf of any kind. Did not fire, so no revert was taken and Task 1(a)'s commit stands.
6. **The new tool emitted no `STOP:` line, its `--check` exits 0 immediately after the render, and
   the guard runner reported drift rather than halting.** Did not fire.
7. **The three list counts read IN 110 / OUT 132 / UNPLACED 2, total 244**, with 244 table rows. Did
   not fire.

---

## 8. Declared departures — stated rather than absorbed

**(i) A shell command that read a repository file was DENIED by the shell-read guard, and was routed
to the file tools rather than worked around (D-253).** Performing the session-start read of the
gating answer, a `python -c` was issued that opened
`tools/audit/nongating_apparatus_rows.json` — a plain **relative** repository path inside interpreter
code. The guard **DENIED** it, the denial naming `CLAUDE.md`'s conventions, D-253 and the
guard-family ruling of 2026-08-08. **The denied form was not retried**; the artifact was located with
`Grep` and read with `Read`. **This is a FIFTH observation of the guard's denial behaviour and it is
of the same shape as the fourth** — interpreter code carrying a relative repository path — **so it
adds no new respect in which the observations differ. No cause is asserted, none may be read in, no
remedy is proposed, and OI-378 was NOT amended to carry it**: the dispatch's Task 1(b) names the
fourth observation and this batch does not widen its own licence. It is stated here and nothing more.

**(ii) The commit trailer differs from the dispatch's, exactly as the dispatch anticipates.** A
system-level attribution instruction in force for this session mandates
`Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`; the dispatch's blocks write
`Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` and instruct that the system instruction be
followed and the difference declared. **The system-mandated form was used in all six commits. Every
commit subject and body is the dispatch's, verbatim.**

**(iii) Four read-only shell commands were run beyond those the dispatch names, all of them git
object queries by explicit hash and all inside D-253's licence.** `git show --stat` was run against
three commits — `15b553b90d` and `8457c97445`, the preceding batch's Task 5 and end-state commits, to
establish which form of the close test that batch actually used rather than assuming it, and
`3cd4bf4e7b`, this batch's own Task 1(b) commit, which the dispatch does order. Each was redirected
to scratch and read with the file tools. **No working-tree file was read through a shell at any point
by this session, and nothing rests on a branch-tip read** — every tip in this report was read at both
ref files with the file tools.

**(iv) `open_items/register_check.json` was staged and turned out to be unchanged**, as §4 records.
Staging a path that the dispatch makes conditional was the cheapest way to avoid a working-tree read
through a shell to decide whether to stage it; the commit object proves it was a no-op.

**(v) The guard set was run as a background command and took roughly twenty minutes**, exceeding the
foreground timeout. It was **not** killed and no subset was substituted; the batch waited for it. Its
full 98-line output was read from the redirect with the file tools.

**(vi) The committed `guard_state.json` was read before the end state** to establish the inherited
failing set at an object rather than recalling it from the preceding batch's prose. This is a read,
not a write, and the artifact was not touched.

**(vii) ★ AN INVENTED HASH WAS WRITTEN INTO THIS REPORT'S TWO CLOSE-TIP CELLS AT FIRST DRAFTING AND
WAS CAUGHT AND REMOVED BEFORE ANYTHING WAS STAGED.** Writing §1 before the Task 5 commit existed, the
executing side put a forty-character value into the *at close* row and the Task 5 row that **no
commit bore and that had been read from nothing**. It was caught on re-reading the draft, and both
cells now say *written into this cell by the end-state commit* and carry no value until that hash has
been read at both ref files. **The invented value never reached the tree**: it existed only in the
untracked working copy of this file, and the first commit to carry this report is Task 5's, taken
after the correction.

**It is disclosed here, in the report itself, and not only in chat — which is the point.** The
preceding batch made the same error, disclosed it in a closing chat message, and its own report and
close section carried no trace of it; the hundred-and-eighth handoff entry named that gap as its
headline finding, and the verdict-pass batch wrote the disclosure into the record additively. **This
is the second occurrence of the same error by the next session, which is itself the finding**, and
the countermeasure applied here is stated so it can be judged: the close-tip cells are written with a
named marker rather than left to be filled from expectation, and no hash is written into this report
that was not first read at both ref files with the file tools. No cause is asserted beyond the
observable one, and no remedy is proposed for the class.

**Nothing in this report is a recommendation, and no position is taken on which list any candidate
should end on.**

---

## 9. What this batch did NOT do

- **No verdict was authored and no verdict was changed.** `VERDICTS` was read by the new tool and
  written by nothing. Not one tuple moved.
- **Nothing was withheld.** `WITHHELD` was not touched and gained no `l2` key.
- **No pack was rendered and no session was booted.** No file under
  `tools/audit/derivation_boot_pack/` was created, edited, deleted or read for writing;
  `tools/audit/derivation_boot_pack.json` was not regenerated; `write_all` was never reached; the only
  mode of that generator run was `--check`.
- **`EXTRAS`, `FROZEN`, the `CRITERION` table, `KEYWORDS`, `L2_KEYWORDS` and `DATE` stand exactly as
  they stood.**
- **Neither `gen_phase3_gate_partition.py` nor `gen_l0_l1_outgoing_population.py` was edited**, and no
  `expected_line` was re-aimed.
- **The `OPEN_ITEMS.md` INDEX was not edited.**
- **No open-items row was created, flipped or discarded; no `D-NNN` was allocated**; and nothing was
  written into `DECISIONS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `FRAMEWORK.md` or any ruling record.
- **No choice question was put to the user and nothing was recommended** about any list or any
  UNPLACED entry (D-658).
- **The reading file was not taken to the user in any form.** It is landed; the Cowork side puts it to
  him, one list per turn.
- **No `src/` change, no golden, no test changed, moved or run, no build, no measurement of the
  analysis, and nothing under `tools/corpus/` or `tools/robust_stop/`.**

---

## 10. The standing self-check (D-434, `CLAUDE.md`) over this batch's own work

The diff of every touched file was re-read on disk, not from the memory of writing it.

1. **#6 — one path per concern.** The reading file has ONE source: the generator's own table. The new
   tool imports `VERDICTS`, `CRITERION`, the keyword tuple and `group_title()` rather than copying
   them, and locates the charter sentence at its home instead of copying it as truth. No second copy
   of any verdict, criterion term or group title now exists.
2. **#17f / D-431 — no transcribed figures.** Every count in the reading file is computed on the run.
   Every figure in this report is quoted from a run's own output or from a git object, and the three
   list counts were read at the rendered file rather than carried from the dispatch.
3. **#12 — no information loss.** Nothing was deleted anywhere. The OI-378 note and the rendered file
   are additions; the regenerated artifacts preserve their authored `expected_line` values and record
   drift beside them rather than overwriting it.
4. **#18 / #19 — nothing assumed that could be established.** The claim that only positions moved is
   not asserted: it is proved at four git objects by explicit hash. The inherited failing set was read
   at the committed artifact. The charter anchors were located at the file. The clean tree was
   measured over the whole population, twice.
5. **#24 / #13 — bounds and surprises.** The dispatch's own named risk — that a new row could add a
   HIT to the L0/L1 population rather than only shift positions — was checked at the objects and did
   not materialise; that is recorded as a checked risk, not as a silent pass. Nothing surprising arose
   that was built around.
6. **Conventions.** American English throughout. No self-invented label: *the reading file*, *the
   guard set*, *a stale artifact* are the dispatch's own plain-word terms. Music-theory words are
   reserved — *measurement tool* and *check*, never *instrument*; *the open-items register* in full;
   bare *score* nowhere in a numerical sense.
7. **The bars.** No verdict moved; nothing withheld; no pack; no session; no INDEX edit; no tool edit
   beyond the one creation and the one enrolment; no choice question anywhere.

*Provenance: CC, 2026-09-05, at boot tip `8457c97445ff9a6c506fe999128681b80969e9ba`, under
`cc_instruction_l2_reading_file_2026_09_05.md`. Every commit identifier above was read from both ref
files with the file tools at the time each commit was taken; the object comparison from git objects by
explicit hash; the guard verdicts from this batch's own run; the inherited failing set from the
committed `guard_state.json`. No figure of the verdict distribution is derived here — the three counts
are quoted as read at the rendered file, which computes them.*
