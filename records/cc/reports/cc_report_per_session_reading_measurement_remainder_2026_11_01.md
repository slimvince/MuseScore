# CC report — the per-session reading measurement, the remainder: ONE TOOL RECOVERED, AMENDED AT THREE SITES, PROVED ON SEVEN PLANTED FAULTS, RUN, ENROLLED AND COMMITTED; THE TWO TABLES PUBLISHED; NOTHING MOVED, NOTHING DECIDED (2026-11-01)

**Dispatch:** `records/cc/instructions/cc_instruction_per_session_reading_measurement_remainder_2026_11_01.md`, pinned at
Task 0 as blob `27f6099a391cea20bcc9c3c858e51e8a51b19912` (70,347 bytes by `git cat-file -s`). It amends, and is otherwise
bound by, `records/cc/instructions/cc_instruction_per_session_reading_measurement_2026_11_01.md` ("the previous dispatch").
**This report decides nothing.** It proposes no fate for any span, makes no recommendation about any member, any span or the
pruning iteration, and authors no class or verdict.

**In one paragraph.** Task 0 landed this dispatch and entry 463 (`023353b2…`); the opening guard capture matched the
declared start state exactly. Task 1 found the kept blob `b909c71e…` present, recovered it into a scratch file proved equal
to it by hash, amended it at the ordered sites — (A) the entry-152 end anchor `**(x)**` → `**(x) ★`, (B) `normalised_opening`
→ `normalized_opening`, (C) the three derivation choices written into the docstring's account of what is derived, (D) the
provenance line — wrote the amended source into the object store as H2 = `851f98ec4c1a01be133731e56bc01e5f43acf56f`, and
placed it in `tools/audit/` by that hash with the git commands (no fallback needed). **All seven proofs passed at their first
run with no change to the tool between any proof and the run**; P1 to P5 printed exactly the values the previous report
quotes. The tool's write-mode run and its `--check` both exit 0; it is enrolled; the classification's STOP names five tools.
Committed as `91e45d62…`, the committed tool's blob equal to H2. Task 2 closed in the standing form; Task 3 carries the end
state.

---

## 0. The ordered first read, and what reached me as injected context

**My first tool call was exactly one read of this dispatch, and nothing else.** It returned a **PARTIAL view** (lines 1 to
615 of 767, at the tool's page limit); before any other read I read the remaining range, 616 to 767.

**Injected context at boot, before any tool call:** (1) `CLAUDE.md`; (2) the memory index `MEMORY.md` from my user memory
folder; (3) a git status snapshot, truncated by the harness at 2,000 characters, with five recent commits (tip `aa0b81558d`);
(4) the user's email address line; (5) an attribution reminder for commit messages; (6) a harness list of deferred tools.
**The injected `CLAUDE.md` was, by my account, the WHOLE FILE:** its first line as injected was `# Claude Code — Standing
Instructions for This Repository` and its last line `…This applies to CC sessions and Cowork sessions alike.`; read later
with the file tool, line 1 and line 1998 (the last) are those same lines, and the injected copy carried every `##` section of
the file in the file's order, the eight conditional spans among them. This is DECLARED, not established (#18): I compared the
first and last lines and the section order, not every byte.

**Then, in the dispatch's order:**

- **(0)** The previous dispatch whole, in four ranges (1–300, 300–619, 619–918, 918–1204).
- **(1)** `CLAUDE.md` with the file tool, located by a heading search: lines 1–312 and 313–666, 704–773, 1536–1999 — the six
  spans' windows. `STATUS.md` whole. `DECISIONS.md` whole in four reads (1–400, 400–599, 600–799, 800–862).
  `BUILD_AND_TEST.md` whole. Rule (a)'s `gating_ids` at `tools/audit/nongating_apparatus_rows.json` lines 186–409 — my read
  range ran on to line 637 and so also took in the field `gating_rows_by_how_they_were_placed` (declared, §6). The
  open-items index was not read.
- **(2)** `cowork_audit_protocol.md`'s dispatch-protocol section, located by a heading search, read at 180–1606 in four reads.
- **(3)** `gen_session_start_read_size.py`, `gen_defense_share.py` and `gen_claude_md_finer_spans.py` whole;
  `gen_governing_surface_spans.py` at its constants by one search (lines 127–134, 140, 165, 177, 197, 198, 201);
  `output_encoding.py` whole.
- **(4)** `session_start_read_size.json`, `defense_share.json`, `claude_md_finer_archive.json`, `claude_md_prune_backlog.json`,
  each whole.
- **(5)** `gen_guard_state.py` at 1–60, 60–259 and 700–929 (the docstring, the `AUTHORED` list's governing comment at
  72–74, its first entries, and the session-start-read, defense-share, L2/L3 entries). Not read whole.
- **(6)** Entries 463, 462 and 461 whole. Entry 464 does not exist (a Glob of the folder for `…_sixty*` returned 460 to 463).
- **(7)** The previous report whole.
- **(8)** Not read, as ordered.

---

## The capacity-judgment file, quoted whole

`capacity_judgment_task1_remainder.txt`, written with the file tools in my session's scratch folder, after the ordered first
read and Task 0 and before the kept blob was touched:

```
CAPACITY JUDGMENT BEFORE TASK 1 (THE REMAINDER) — written 2026-11-01, after the ordered first read and Task 0's commit and push, before the kept blob is touched.

WHAT TASK 1 DOES. Recover tools/audit/gen_per_session_reading.py from the kept loose blob
b909c71ea47ef8c62f9bd74e06c634fb217f517b into a scratch file and prove the recovery by hash equality;
amend it at the dispatch's sites (A) the entry-152 end anchor `**(x)**` -> `**(x) ★` as a prefix test,
(B) normalised_opening -> normalized_opening, (C) the three derivation choices written into the
docstring, (D) the provenance line; write the amended source into the object store (H2) and place it
in the tree by that hash; re-run the five proofs P1 to P5 and the two new ones P6 (the folder-level
add-commit lookup against the per-path one) and P7 (the old wrong anchor planted); the write-mode run
and --check; the self-check and word scan; the enrolment in gen_guard_state.py's authored list with
its two checks; one commit, pushed.

WHAT THE ORDERED READS TOOK, by my own account. This dispatch (two ranges), the previous dispatch whole
(four ranges, 1,204 lines), the six CLAUDE.md spans read with the file tool on top of the whole file
injected at boot, STATUS.md, DECISIONS.md whole (four ranges), BUILD_AND_TEST.md whole, the gating
identities, the dispatch-protocol section of cowork_audit_protocol.md (lines 180 to 1606, four reads),
the three imported tools whole, the coarse constants and output_encoding.py, the four artifacts whole,
gen_guard_state.py at three windows, entries 463, 462 and 461 whole, and the previous report whole.
Most context went to the previous dispatch, DECISIONS.md, the protocol section and the three imported
tools, in that rough order.

HAS A SUMMARY OF MY CONTEXT FALLEN? No. No summary has fallen at the time of writing; everything from
the first read of this dispatch is in my context.

WHAT THE BATCH STILL OWES AFTER TASK 1. The whole close (Task 2: the STATUS.md entries and the prefix
move, the forward-bound re-aim with --apply and --check and the four archive checks, the regenerations
of session_start_read_size, defense_share and then this tool last, the evidence-pin and the two
population checks, the report, the appended close, the close commit) and the end state (Task 3: the
full guard run in write mode, the classification check, the end-state section with A3 to A5 verified at
the objects, the commit).

MY JUDGMENT. The tool is not written in this batch: it is recovered and amended at a handful of sites,
and its derivations were proved by the previous batch. The seven proofs are short scratch scripts over
functions whose code I will read whole at 1(b). The context already spent on the reads is large, so the
residual risk is that a summary falls during the close; if one falls I will say so plainly in the
report and in the STATUS.md close entry. I judge I can finish Task 1 whole — recovered, amended, proved,
run, enrolled, committed — and still close and reach the end state. If the kept blob is absent, if an
imported function raises its own STOP on this tree, if a proof fails and resists a correction of my
amendments, or if a second authored anchor does not hold at the file, I stop under the first-unit rule,
commit nothing of Task 1, clear the index of the tool, and go to Task 2.
```

---

## 1. Task 0

**0(a) — the pin.** `git hash-object -w` of this dispatch → `27f6099a391cea20bcc9c3c858e51e8a51b19912`; `git cat-file -s` →
`70347`. Immediately before staging, `git hash-object` of the working copy → `27f6099a…` again: unmoved. The committed blob,
`git rev-parse 023353b2…:<this dispatch>`, is `27f6099a…`. The dispatch had been read from the working tree first (the user's
opening line orders that read), so the pin follows the standing clause P-2's declared-departure route (§6).

**0(b) — the refs**, read with the file tools: `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
`aa0b81558da334b755f0f93cb2fe11794a3129d5`. `git show --stat`, one command per commit, hash written literally:

```
aa0b81558da334b755f0f93cb2fe11794a3129d5 6b970e0715c3a9aeae2cd505232e0cbd9c7836e0  End state: the per-session reading measurement - ...  (2 files: cowork_away_returns.md, guard_state.json)
6b970e0715c3a9aeae2cd505232e0cbd9c7836e0 6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65  Close: the per-session reading measurement - nothing measured, under its dispatch  (10 files)
6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65 63163e31560a2bb663f32dcfae34290f0871026b  record: entries 461 and 462 and the per-session reading measurement dispatch  (3 files)
63163e31560a2bb663f32dcfae34290f0871026b 3300e3d6513e586d99a08208340139f65c6903ae  End state: the L3 comparison - sections 8, 9 and 14 written, ...  (2 files)
```

The chain is exactly the one the premise ledger states.

**0(c) — A1.** `python tools/audit/changed_paths.py` (repository as the working directory): **396 change records**; exactly
ONE tracked modification, ` M tools/audit/claude_md_finer_archive.json` (the standing one). The untracked population is given
**by its count with every path outside `scratch_artifacts/` named** (387 records are under `scratch_artifacts/`): `Claude
outputs/`, `Codex research inventory/`, `docs/research_papers/polyph9-release/`, `external resarch summary/Computational Music
Theory and Its.pdf`, `external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf`, this dispatch,
`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_three.md`, and
`tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. No other untracked path under `records/`, `tools/audit/` or
the repository's top folder. `git ls-files --others --exclude-standard --` printed this dispatch and entry 463 (each
`exit:0`) and nothing for entry 464. `git diff --stat aa0b8155… -- <path>` for `STATUS.md`, `STATUS_ARCHIVE.md`,
`gen_status_batch_bound.py`, `status_batch_bound.json`, `gen_guard_state.py`, the four imported tools, `CLAUDE.md`,
`DECISIONS.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, the previous dispatch, the previous report, entries 448 to 462
each named (their existence confirmed by a Glob), and `cowork_blind_derivation_l3_2026_10_17.md`: **empty for every one**,
`exit:0` each. **A1 holds.**

**0(d) — the last bytes**, each landed file at its blob (`git hash-object -w --no-filters`), the object written to a scratch
file and read by a scratch script:

```
== blob_dispatch.bin   (27f6099a391cea20bcc9c3c858e51e8a51b19912)
  size 70347
  zero bytes 0
  last 70 bytes b'h named one at its ordered first read and holds the quotations to it.\n'
== blob_e463.bin       (00a77280b3f17747c31b9594177a3014a304c8d5)
  size 16460
  zero bytes 0
  last 70 bytes b'on entry 462. The user\'s words: the opening instruction;\n"continue".*\n'
```

No final line broken off, no zero byte. Entry 463 is 16,460 bytes.

**0(e) — the commit.** Staged by explicit path; `changed_paths.py --staged`:

```
A	records/cc/instructions/cc_instruction_per_session_reading_measurement_remainder_2026_11_01.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_three.md
2 changed path record(s) [staged]
```

Committed with the subject `record: entry 463 and the per-session reading measurement remainder dispatch` →
`023353b20cd77c31552a354fc512c879c7974348` (parent `aa0b8155…`, 2 files, 928 insertions), read at `.git/refs/heads/master`
and at its own object. Push: `   aa0b81558d..023353b20c  master -> master`; `.git/refs/remotes/origin/master` reads
`023353b20cd77c31552a354fc512c879c7974348`.

**0(f) — the opening guard capture**, `python tools/audit/gen_guard_state.py --check` (read-only operating mode, named), run in
the background, its output in a scratch file, read with the file tools. Its header line was *"the guard state re-derives"*;
its last two lines *"82 guard(s) run, 13 failing, 4 not run, 20 historical record(s)"* and `exit:0`. **Every verdict line is
identical to the previous report's §1, 0(f) listing**, line for line (the same 106 verdict lines in the same order); the FAIL
lines, verbatim:

```
  [FAIL] tools/audit/gen_phase3_gate_partition.py --check
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [FAIL] tools/audit/gen_artifact_inventory.py --check
  [FAIL] tools/audit/gen_artifact_inventory_surface.py --check
  [FAIL] tools/audit/gen_test_construction_evidence.py --check
  [FAIL] tools/audit/gen_retirement_caller_check.py --check
  [FAIL] tools/audit/decisions/apply_soft_discard.py --check
  [FAIL] tools/audit/decisions/apply_residue_discard.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [FAIL] tools/audit/decisions/gen_cluster_dispositions.py --verify
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
```

The whole output stands in the scratch file `t0f_guard.txt`; it is not retyped here beyond the lines quoted, every other line
being a PASS, NOT RUN or HISTORICAL line identical to the previous report's quotation. Against A2: header *"the guard state
re-derives"* (exit 0), run 82, the thirteen and nothing else, zero STOPs. `python tools/audit/gen_guard_classification.py
--check` → exit 2:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_withheld_family_reading.py']
```

exactly the four relayed names.

**0(g) — at the Task 0 commit**, each in its own call, each exit 0: *"the session-start read measurement re-derives"*, *"the
defense-share measurement re-derives"*, *"l0_l1_outgoing_population.json re-derives"*, *"l3_outgoing_population.json
re-derives"*. **The precondition for Task 1 held.**

---

## 2. Task 1 — recovered, amended, proved, run, enrolled, committed

**1(a).** The capacity file is quoted above; it judged Task 1 finishable whole.

**1(b) — the recovery.** `git cat-file -e b909c71ea47ef8c62f9bd74e06c634fb217f517b` → `exit:0`: present. `git cat-file blob
b909c71e…` → the scratch file `gen_per_session_reading_recovered.py`; `git hash-object --no-filters` of that file →
`b909c71ea47ef8c62f9bd74e06c634fb217f517b`. **The recovery is proved by that equality.** Read whole with the file tools:
**847 lines**, newline-terminated. **The locator of row (ii), `roman_items_portion`, already tests each anchor against the
line's OPENING** — `line.lstrip().startswith(opener)` — so amendment (A) needed no change to the test, only to the anchor.

**1(c) — the amendments, in the scratch copy, with the file tools**, each site found by a Grep over the scratch file (line
numbers in the recovered source):

- **(A)** `**(x)**` occurred at **166** (`OPENER_X`, the locator's anchor, which the published `the_portion_read` of row (ii)
  formats in) and **287** (`roman_items_portion`'s docstring) — both now `**(x) ★`. Line 642's member name `"entry 152, items
  (v) to (x)"` carries no anchor and stands. The module docstring's account of row (ii) names "the two openers of entry 152"
  with no literal, and stands.
- **(B)** `normalised_opening` at **356** (definition), **408** and **420** (calls) → `normalized_opening`; the private field
  `_normalised_opening` on the same two lines → `_normalized_opening` (declared, §6).
- **(C)** the three derivation choices written into the docstring's `derived :` account, each as a bullet, after its existing
  last sentence (recovered lines 43–46). The lists of what is authored, the STOPs and what the tool does not assert stand as
  written; the existing paragraphs *HOW A SIZE IS COUNTED* and *HOW AN ADD-COMMIT IS FOUND* stand as written.
- **(D)** the provenance sentence at **31–32** replaced by the ordered line.

`git hash-object -w --no-filters` of the amended scratch file → **H2 = `851f98ec4c1a01be133731e56bc01e5f43acf56f`**.
`git diff b909c71ea47ef8c62f9bd74e06c634fb217f517b 851f98ec4c1a01be133731e56bc01e5f43acf56f`, whole:

```
diff --git a/b909c71ea47ef8c62f9bd74e06c634fb217f517b b/851f98ec4c1a01be133731e56bc01e5f43acf56f
index b909c71ea4..851f98ec4c 100644
--- a/b909c71ea47ef8c62f9bd74e06c634fb217f517b
+++ b/851f98ec4c1a01be133731e56bc01e5f43acf56f
@@ -28,8 +28,11 @@ the member's feet and closing sections is a natural break: plan a pruning iterat
 context occupied every session by mandatory reading ), then continue."*  The plan the writing side
 put to him and he answered *"continue"* to is at `records/cowork/handoff/
 cowork_handoff_entry_four_hundred_and_sixty_one.md` §2, and its STEP 1 is to measure before
-anything moves (D-277, measure before build).  Built by
-`cc_instruction_per_session_reading_measurement_2026_11_01.md` Task 1.
+anything moves (D-277, measure before build).  Built under
+`cc_instruction_per_session_reading_measurement_2026_11_01.md` Task 1, whose first write-mode run
+STOPPED on an authored anchor the file does not carry, the source kept as a loose blob; recovered,
+amended at three sites and completed under
+`cc_instruction_per_session_reading_measurement_remainder_2026_11_01.md` Task 1.
 
 WHAT IS AUTHORED AND WHAT IS DERIVED
 ------------------------------------
@@ -43,7 +46,24 @@ authored : the MEMBERSHIP of the further members — each row with the side that
 derived  : every size, every count, every population, every partition and every hash match.  The
            ordinary read, the six spans, the finer cut, the classes, the shape and the marked
            defense are each IMPORTED and called as written, never re-implemented (#6).  No value
-           is transcribed (D-431).
+           is transcribed (D-431).  Three choices in how these are derived, each AUTHORED by the
+           remainder dispatch named under WHY IT EXISTS above:
+             * THE PROTOCOL PARTITION'S ACCOUNTING.  A located portion is its lines joined by
+               newlines, so the opening prose, the marked and the unmarked sections sum to the
+               section LESS the newline joining each portion to the next.  Those joining newlines
+               are counted explicitly, and the run STOPs unless opening + marked + unmarked +
+               joining newlines = the section; the equality is exact and is published.
+             * THE SETTLED-SPAN OPENING MATCH, OVER WHITESPACE-COLLAPSED TEXT.  The two settled-span
+               artifacts write `the_opening` as `" ".join(span["text"].split())[:160]`, which is
+               `gen_claude_md_finer_spans.build()`'s own form.  A raw comparison would fail at the
+               first line break of every multi-line sub-block, so whitespace is collapsed on both
+               sides before the first 120 characters are compared, as the producing tool does.
+             * THE ADD-COMMIT LOOKUP, ONE `git log` PER FOLDER.  A per-path call costs about a
+               second here and the handoff folder holds several hundred entries, so ONE
+               `git log --no-renames --diff-filter=A --format=@@%H %ct --name-only -- <folder>`
+               runs per folder, and each path takes the first (newest) commit naming it — what a
+               per-path call's first line gives.  That equality was proved against the per-path
+               call by that dispatch's proof P6.
 
 WHY A SIBLING AND NOT AN EXTENSION of `gen_session_start_read_size.py`.  That tool's subject is the
 ORDINARY session-start read: its own docstring states that a conditional read is not a member and
@@ -163,7 +183,7 @@ ENTRY_118 = HANDOFF_FOLDER + "/cowork_handoff_entry_one_hundred_and_eighteen.md"
 BRIDGE_HEADING = "### ★★ THE BRIDGE FAULT — READ THIS BEFORE YOU WRITE ANYTHING"
 ENTRY_152 = HANDOFF_FOLDER + "/cowork_handoff_entry_one_hundred_and_fifty_two.md"
 OPENER_V = "**(v)**"
-OPENER_X = "**(x)**"
+OPENER_X = "**(x) ★"
 ENTRY_169 = HANDOFF_FOLDER + "/cowork_handoff_entry_one_hundred_and_sixty_nine.md"
 ENTRY_291 = HANDOFF_FOLDER + "/cowork_handoff_entry_two_hundred_and_ninety_one.md"
 
@@ -284,7 +304,7 @@ def bridge_fault_portion(text: str) -> dict:
 
 
 def roman_items_portion(text: str) -> dict:
-    """Entry 152 from the line opening `**(v)**` through the end of the paragraph opening `**(x)**`."""
+    """Entry 152 from the line opening `**(v)**` through the end of the paragraph opening `**(x) ★`."""
     lines = text.split("\n")
     found = {}
     for opener in (OPENER_V, OPENER_X):
@@ -353,7 +373,7 @@ def population_summary(rows: list[dict], latest: int, latest_field: str) -> dict
 
 
 # ── table 2: the six spans, partitioned ─────────────────────────────────────────────────────────
-def normalised_opening(text: str) -> str:
+def normalized_opening(text: str) -> str:
     """The whitespace-collapsed opening the settled-span artifacts publish — the same normalization
     the finer tool applies when it writes `the_opening`."""
     return " ".join(text.split())[:OPENING_WIDTH]
@@ -405,7 +425,7 @@ def partition_the_six_spans(claude_md: str, settled: list[dict]) -> dict:
                 "text_sha256": hashlib.sha256(s["text"].encode("utf-8")).hexdigest(),
                 "the_opening": s["text"][:160],
                 "settled_at_an_earlier_sitting": [],
-                "_normalised_opening": normalised_opening(s["text"]),
+                "_normalized_opening": normalized_opening(s["text"]),
                 "_span": span["name"],
             }
             rows.append(row)
@@ -417,7 +437,7 @@ def partition_the_six_spans(claude_md: str, settled: list[dict]) -> dict:
     for entry in settled:
         by_hash = [r for r in every if r["text_sha256"] == entry["text_sha256"]]
         by_opening = [r for r in every
-                      if r["_normalised_opening"] == normalised_opening(entry["the_opening"])]
+                      if r["_normalized_opening"] == normalized_opening(entry["the_opening"])]
         if by_hash:
             how, matched = "by hash — the sub-block stands unchanged", by_hash
         elif by_opening:
```

**Every changed passage is at one of the sites (A) to (D), and nowhere else.**

**1(d) — placing the tool in the tree, by hash**, the repository as the working directory: `git update-index --add
--cacheinfo 100644,851f98ec4c1a01be133731e56bc01e5f43acf56f,tools/audit/gen_per_session_reading.py` → `exit:0`; `git
checkout-index -f -- tools/audit/gen_per_session_reading.py` → `exit:0`; `git hash-object --
tools/audit/gen_per_session_reading.py` → **`851f98ec4c1a01be133731e56bc01e5f43acf56f`**. **The guard denied neither git
command; the fallback was not taken.** The tool was placed only after the opening guard capture had finished, so the capture
measured the tree as declared.

**1(e) — the proofs, before the first run**, each a scratch script importing the tool from `tools/audit/` and calling its
functions on an altered copy held in memory, run with `python -I -X utf8` from the scratch folder with `tools/audit` inserted
on the import path, each output in a scratch file read with the file tools. Quoted whole:

**P1** (`proof_p1.py`):
```
the marker line deleted, at line 235 : "*★ STANDING CLAUSE — a dispatch's read-first block requires the clause below to be met.*"
the_marked_sections count 38 -> 37  characters 101700 -> 100817
the_unmarked_sections count 1 -> 2  characters 2157 -> 2950
section characters 108389 -> 108300  fall 89  expected 89
the sums still account: yes (protocol_section raised no Stop on the altered copy)
P1 PASS
```

**P2** (`proof_p2.py`):
```
the marker inserted directly above line 896 : '### When a shell-read policy cannot decide, it DENIES — and the ceiling it cannot see is published in the measured rate'
the_marked_sections count 38 -> 39  characters 101700 -> 103946
the_unmarked_sections count 1 -> 0  characters 2157 -> 0
section characters 108389 -> 108478  rise 89  (the line and its newline: 89 )
the sums still account: yes (protocol_section raised no Stop on the altered copy)
P2 PASS
```

**P3** (`proof_p3.py`; the star-marked sub-block chosen is the one opening `**★ WHAT HAPPENS TO A NAME BORROWED FROM THE
PUBLISHED RESEARCH…`, inside Conventions):
```
the ★ removed at line 1616 : '  **★ WHAT HAPPENS TO A NAME BORROWED FROM THE PUBLISHED RESEARCH, AND IN WHAT ORDER THE CLEANUP'
  Guiding principles                            sub-blocks   44 ->   44  characters  26908 ->  26908
  The open-items register                       sub-blocks   17 ->   17  characters  14816 ->  14816
  The decisions register                        sub-blocks    3 ->    3  characters  17109 ->  17109
  This block                                    sub-blocks   20 ->   20  characters   5213 ->   5213
  Conventions                                   sub-blocks   20 ->   19  characters  41071 ->  41070
  The self-check after every coding exercise    sub-blocks    2 ->    2  characters    759 ->    759
six spans 105876 -> 105875  fall 1
the accounting still sums: yes (partition_the_six_spans raised no Stop on the altered copy)
P3 PASS
```

**P4** (`proof_p4.py`; the settled span chosen is the one found by hash at line 1775, *"NOTE ON PHASE 2"*):
```
by hash 4 by opening only 2 not found 2
tools/audit/claude_md_finer_archive.json the_left_at_site_by_the_reading by hash — the sub-block stands unchanged [202]
    **★ THAT PARAGRAPH REPLACED A NARROWER ONE, AND THE FORMER WORDING STANDS IN PLACE (#12; user-ruled 
tools/audit/claude_md_finer_archive.json the_left_at_site_by_the_reading by hash — the sub-block stands unchanged [53]
    **★ WHAT IT SUPERSEDES — A POINTER, NEVER A COPY (#6).** R3's clause that an apparatus finding's row
tools/audit/claude_md_finer_archive.json the_refused_by_the_ruling by its opening only — the same sub-block, amended since [388]
    **★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH A PER-ROW LAPSE RECORD (user-ruled 2026-
tools/audit/claude_md_finer_archive.json the_refused_by_the_ruling not found []
    *★ [SUPERSEDED by the OI-178 adoption 2026-07-26 — historical] THE OI-168 RE-BASELINE (2026-07-14; r
tools/audit/claude_md_finer_archive.json the_refused_by_the_ruling not found []
    **★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; `cc_a8_rebaseline_measure_report.md`).** 
tools/audit/claude_md_finer_archive.json the_refused_by_the_ruling by hash — the sub-block stands unchanged [1949]
    **★ THE RULE COVERS EVERY READ MECHANISM AND EVERY DIALECT (recorded 2026-08-08 on the user's direct
tools/audit/claude_md_prune_backlog.json the_left_at_site_by_the_reading by its opening only — the same sub-block, amended since [1658]
    **★ THE THREE-PHASE STRUCTURE BELOW IS SUPERSEDED AND ITS TRUTH HALF IS REPLACED (user-ruled 2026-08
tools/audit/claude_md_prune_backlog.json the_left_at_site_by_the_reading by hash — the sub-block stands unchanged [1775]
    **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT IS RATIFIED (user, 2026-08-03; D-439).**

the sub-block: 1775 to 1804 ; changed at line 1804 : '  owed."*)*' -> '  Owed."*)*'
  **★ THAT PARAGRAPH REPLACED A NARROWER ONE, AND THE FORMER W | by hash — the sub-block stands unchanged -> by hash — the sub-block stands unchanged 
  **★ WHAT IT SUPERSEDES — A POINTER, NEVER A COPY (#6).** R3' | by hash — the sub-block stands unchanged -> by hash — the sub-block stands unchanged 
  **★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH  | by its opening only — the same sub-block, amended since -> by its opening only — the same sub-block, amended since 
  *★ [SUPERSEDED by the OI-178 adoption 2026-07-26 — historica | not found -> not found 
  **★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; ` | not found -> not found 
  **★ THE RULE COVERS EVERY READ MECHANISM AND EVERY DIALECT ( | by hash — the sub-block stands unchanged -> by hash — the sub-block stands unchanged 
  **★ THE THREE-PHASE STRUCTURE BELOW IS SUPERSEDED AND ITS TR | by its opening only — the same sub-block, amended since -> by its opening only — the same sub-block, amended since 
  **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT  | by hash — the sub-block stands unchanged -> by its opening only — the same sub-block, amended since     <- MOVED
found_by_hash 4 -> 3
found_by_opening_only 2 -> 3
not_found 2 -> 2
P4 PASS
```

**P5** (`proof_p5.py`):
```
unaltered: {'first_line_at_the_tree': 27, 'last_line_at_the_tree': 51, 'characters': 2075}
Stop raised: the boot-chain anchor '### ★★ THE BRIDGE FAULT — READ THIS BEFORE YOU WRITE ANYTHING' is found 2 time(s) and must be found exactly once
P5 PASS
```

**P6** (`proof_p6.py` — for every arc dispatch, every arc report, entries 118, 152, 169 and 291 and the three handoff entries
with the latest add-commits, the per-path `git log --diff-filter=A --format=%H %ct -- <path>` first line against the tool's
folder-level `add_commits`):
```
the three latest handoff entries: ['cowork_handoff_entry_four_hundred_and_sixty_one.md', 'cowork_handoff_entry_four_hundred_and_sixty_two.md', 'cowork_handoff_entry_four_hundred_and_sixty_three.md']
checked 67 mismatched 0
ADD-COMMIT CHECK PASS
```

**P7** (`proof_p7.py`):
```
the corrected anchor's line at the tree: 66 : '**(x) ★ A CORRECTION TO THE HUNDRED-AND-FIFTY-FIRST ENTRY, F'
unaltered: {'first_line_at_the_tree': 61, 'last_line_at_the_tree': 66, 'characters': 3580}
planted: line 66 now opens '**(x)** A CORRECTION TO THE HUNDRED-AND-'
Stop raised: the boot-chain anchor '**(x) ★' is found 0 time(s) and must be found exactly once
P7 PASS
```

`roman_items_portion` publishes its portion under `first_line_at_the_tree`, `last_line_at_the_tree` and `characters` — the
same field names as the bridge-fault portion (read at the function, 1(b)). **P1 to P5 printed exactly the verdicts and values
the previous report §2, 1(c) quotes.** **No change was made to the tool between any proof and the run**; every proof passed at
its first run.

**1(f) — the run.** `python tools/audit/gen_per_session_reading.py` (write mode, named), the repository as the working
directory, exit 0 — verbatim:

```
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 247953
    CLAUDE.md, the whole file as the executing sessions report it injected   169617
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 709070
  Cowork, per sitting, in the shape of the sitting of entry 461: 1007889
  six spans 105876 characters, 106 sub-blocks, archive-class 14269, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
```

`python tools/audit/gen_per_session_reading.py --check` (own call) → exit 0, *"the per-session reading measurement
re-derives"*. **The artifact's values at the Task 1 commit** (`tools/audit/per_session_reading.json`, blob
`c221ad8eb1e66e4b39d3722f023ac2b0bf709dad`), quoted from it. The fields that moved at the close are listed at 2(c).

- `the_ordinary_session_start_read_imported` → `total_characters`: `247953` (members: `CLAUDE.md` 105876, `STATUS.md`
  11524, `DECISIONS.md` 127727, the gating identities 2826).
- `the_further_members` → `characters`: the injected `CLAUDE.md` `169617` (with
  `characters_the_six_spans_read_with_the_file_tool_add_on_top_of_it` `105876` and
  `characters_of_the_file_outside_the_six_spans` `63741`); `BUILD_AND_TEST.md` `27236`; the protocol section `108389`; the
  blind derivation `126702`.
- The protocol row: `the_opening_prose` → `characters` `4493`; `the_marked_sections` → `count` `38`, `characters` `101700`;
  `the_unmarked_sections` → `count` `1`, `characters` `2157` (the one section headed *"When a shell-read policy cannot decide,
  it DENIES — …"*, heading at line 896); `newlines_joining_one_portion_to_the_next` `39`;
  `paragraphs_opening_STANDING_CLAUSE_ratified_inside_the_last_section` `4`; `all_of_those_paragraphs_lie_inside_the_last_section`
  `true`.
- `the_arc_dispatches`: `count` 30, `characters_total` 4982224, `characters_mean` 166074, `characters_min` 80466,
  `characters_max` 259912; `the_last_five`: `…_twenty_sixth_2026_10_27.md` 239614, `…_twenty_seventh_2026_10_28.md` 259912,
  `…_twenty_eighth_2026_10_30.md` 233425, `…_twenty_ninth_2026_10_31.md` 181526, `…_thirtieth_2026_10_31.md` 151805.
- `the_arc_reports`: `count` 30, `characters_total` 3741155, `characters_mean` 124705, `characters_min` 46542,
  `characters_max` 520923; `the_last_three`: `…_twenty_eighth_2026_10_30.md` 142049, `…_twenty_ninth_2026_10_31.md` 90619,
  `…_thirtieth_2026_10_31.md` 520923.
- `the_cowork_boot_chain`: (i) entry 118, the bridge-fault section, lines 27–51, `2075`; (ii) entry 152, `the_portion_read`
  *"from the line opening `**(v)**` through the end of the paragraph whose first line opens `**(x) ★`"*, lines 61–66,
  `3580`; (iii) entry 169 whole `24913`; (iv) entry 291 whole `9655`; (v) the three latest handoff entries
  (`the_population_count` 383) — entries 461 `15962`, 462 `14669`, 463 `16354` — `46985`.
- `totals_by_side`: *"Claude Code, per batch, in the thirtieth dispatch's shape"* → `without_the_injected_copy_of_CLAUDE_md`
  `709070`, `with_it` `878687`; *"Cowork, per sitting, in the shape of the sitting of entry 461"* → `characters` `1007889`.
- Table 2's `totals`, whole: `characters_of_the_six_spans` 105876; `characters_given_to_the_finer_cut` 105882;
  `characters_of_the_blank_lines_between_sub_blocks` 49; `sub_block_count` 106; `by_kind` — `block` 44 / 55420,
  `numbered-principle sub-block` 24 / 8024, `star-marked sub-block` 28 / 41318, `table-row` 10 / 1071; `by_class` —
  `operative-rule-text` 102 / 91564, `preserved-former-wording` 3 / 11316, `defense-and-declined-alternatives` 1 / 2953;
  `by_shape_element` — `archive_pointer_lines_inside_this_span` 5 / 2863, `ruled_date_header` 39 / 56976,
  `accepted_costs_paragraph_REFUSED_as_pointer_carried` 2 / 1012, `declined_alternatives_paragraph_REFUSED_as_pointer_carried`
  2 / 1012, `former_wording_marker` 4 / 26826, `accepted_costs_paragraph` 1 / 2953, `declined_alternatives_paragraph`
  1 / 2953; `star_marked_sub_blocks` 28 / 41318; `sub_blocks_carrying_a_ruled_date_header` 39 / 56976;
  `archive_class_characters` 14269; `doubt_defaulted_characters` 90909; `settled_sub_blocks` 6 / 12997 (each pair is
  `sub_blocks` / `characters`).
- `the_settled_spans`: `found_by_hash` 4, `found_by_opening_only` 2, `not_found` 2.
- `the_marked_defense_clauses_imported` → `the_totals`: `marked_clauses` 34, `characters_those_clauses_hold` 12957,
  `characters_had_every_clause_been_closed_at_the_next_marked_clause` 51684,
  `characters_had_every_clause_run_to_its_paragraph_end` 160906, `share_of_the_six_session_start_spans` 12.24,
  `share_of_the_whole_ordinary_session_start_read` 5.23.

Then `python tools/audit/gen_session_start_read_size.py --check` and `python tools/audit/gen_defense_share.py --check` → both
exit 0, *"the session-start read measurement re-derives"*, *"the defense-share measurement re-derives"* (run in one shell
call, §6).

**1(g) — the self-check and the word scan** over the tool's own text: one case-insensitive Grep for *note(s)*, *key(s)*,
*part(s)*, *figure(s)*, *rest*, *root*, *scale*, *bar(s)*, *flat*, *stem*, *instrument*, *period*, *phrase*, *measure(s)*,
*tie*, *register*, *mode(s)*, *score*, *beat*, *resolution* as whole words, and *colour*, *centre*, *judgement*, *recognis-*,
*normalis-*, *summaris-*, *organis-*, *behaviour*, *favour*, *whilst*, *analyse*, *catalogue*, *programme* as substrings.
**What stands, each read:** `measure` as the imported function's name and the verb *to measure* (lines 9, 30, 31, 544, 547,
763, 808); `ROOT` as code (129, 209, 328, 347, 831, 840); `key=` as code (358); `shape.keys()` as code (423); *write-mode* as
the operating mode (32). **No British spelling remains.** No hit of my own needed rewording, so the tool was not re-run for
this step. The artifact's authored strings are the tool's own strings and were covered by the same scan.

**1(h) — the enrolment.** `tools/audit/gen_guard_state.py`'s `AUTHORED` list gained the entry
`("tools/audit/gen_per_session_reading.py", ["--check"], …)` directly after the entry for `gen_defense_share.py` (which follows
the entry for `gen_session_start_read_size.py`), in their shape: a dated comment block naming this dispatch and Task 1, then
the invocation and its reason. **The governing head comment at lines 72–74 was not amended**: the earlier enrolments I read —
the session-start read size, the defense share, the L0/L1 and L3 populations — each carry their own dated comment block above
their entry and none amended that head comment, so there was no former wording to name (§6). **No classification verdict was
authored.** `python tools/audit/gen_guard_state.py --check` (read-only operating mode, named), in the background: header line
*"STALE vs the run: guard_state.json does not re-derive"* (A2's named exception); the new tool's verdict line `  [PASS]
tools/audit/gen_per_session_reading.py --check`; last line *"83 guard(s) run, 13 failing, 4 not run, 20 historical
record(s)"*; the same thirteen FAIL lines; `exit:1`. `python tools/audit/gen_guard_classification.py --check` → exit 2:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_per_session_reading.py', 'tools/audit/gen_withheld_family_reading.py']
```

Five names: the four and the new one.

**1(i) — the commit.** Staged by explicit path; `changed_paths.py --staged`:

```
M	tools/audit/gen_guard_state.py
A	tools/audit/gen_per_session_reading.py
A	tools/audit/per_session_reading.json
3 changed path record(s) [staged]
```

Committed with the subject `measurement: the per-session reading table and the CLAUDE.md span partition - a tool added and
enrolled, nothing moved` → `91e45d621aa4a387271f8a4e89e9742c958c38c6` (parent `023353b2…`, 3 files, 4,234 insertions). Push:
`   023353b20c..91e45d621a  master -> master`; `.git/refs/remotes/origin/master` reads `91e45d62…`. **The committed tool's blob,
`git rev-parse 91e45d62…:tools/audit/gen_per_session_reading.py`, is `851f98ec4c1a01be133731e56bc01e5f43acf56f` — equal to
H2**; no change was made after 1(c).

---

## 3. Task 2 — the close

**2(a) — the `STATUS.md` entries.** In one edit: the close entry naming this dispatch and carrying the `Last updated: `
prefix, the Task 1 and Task 0 entries (`Same dispatch`) below it, and the prefix removed — and nothing else — from the previous
batch's close entry. Read after the edit: **exactly one line carries `Last updated: `**. The case-insensitive substring search
of `STATUS.md` for all 26 ruled terms returned exactly one hit, `24:phrase`, the standing *paraphrase* line; a search for
*repeat* and *tie* returned none.

**2(b) — the forward bound.** `gen_status_batch_bound.py` read at the object `aa0b8155…` (written to a scratch file, read
there): `BASE_COMMIT = "6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65"` (2374), `PREVIOUS_BATCH_DISPATCH =
"cc_instruction_l3_comparison_tabulation_thirtieth_2026_10_31.md"` (2582), `ACT_DATE = "2026-11-01"` and `DISPATCH =
"cc_instruction_per_session_reading_measurement_2026_11_01.md"` (2839–2840), `TASK = "Task 2"` (3096), `MOVE_KIND =
"ordinary"` (3103), `PREVIOUS_AIMINGS` ending at the previous batch's row — **every constant as the premise ledger relays it**.
`git rev-parse 91e45d62…:STATUS.md` → `e09f1904379414f66cb48f883fa58090df117251`; `git rev-parse aa0b8155…:STATUS.md` →
`e09f1904379414f66cb48f883fa58090df117251`, one command each: equal. Re-aimed: `BASE_COMMIT` →
`91e45d621aa4a387271f8a4e89e9742c958c38c6` (the Task 1 commit); `PREVIOUS_BATCH_DISPATCH` →
`cc_instruction_per_session_reading_measurement_2026_11_01.md`; `ACT_DATE` stays `2026-11-01` (the day the move ran);
`DISPATCH` → `cc_instruction_per_session_reading_measurement_remainder_2026_11_01.md`; `TASK` stays `Task 2`; `MOVE_KIND`
stays `ordinary`; this batch's aiming appended as the last row of `PREVIOUS_AIMINGS`; each head comment amended in the shape
of the rows above it, the former values named. `--apply`:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 2, 2,246 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The prediction held**: `status_batch_bound.json` → `the_moved` names the previous batch's close entry (`line_at_base` 8,
`"the_one_declared_adjustment_applied": true`) and its Task 0 `Same dispatch` entry (10); the two 2026-09-02 entries stayed;
no STOP. **No correction line was inserted in `STATUS_ARCHIVE.md`.** The four archive checks, each in its own call, each
exit 0:

```
python tools/audit/gen_status_batch_bound.py --check
  entries moved: 2, 2,246 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True

python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
  STATUS.md / STATUS_ARCHIVE.md: moved 131 span(s), 457,949 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters

python tools/audit/gen_status_residue_move.py --check
  candidates: 17, moved 16, left at site by the reading 1
  characters moved: 46,105
  byte-present in the companion exactly once: True
  absent from the must-read:                  True
  every flagged entry still at site:          True

python tools/audit/gen_status_archive_pass.py --check
  dated entries moved: 52
  at the pass commit, the live file was exactly base-minus-range: True
  the moved block is verbatim in the archive at HEAD:             True
  the moved block is absent from the live file at HEAD:           True
```

**2(c) — the regenerations.** Each check first, in its own call:

- `gen_evidence_pin_membership.py --check` → exit 0, GREEN as predicted: *"the evidence pin's class membership re-derives"*,
  *"generated ratification documents 7; ruling records read 170"*, *"members 7 — pinned 5, UNRESOLVED 0"*.
- `gen_session_start_read_size.py --check` → exit 1, *"STALE vs the measurement: session_start_read_size.json does not
  re-derive"*; `gen_defense_share.py --check` → exit 1, *"STALE vs the measurement: defense_share.json does not re-derive"* —
  both red as A2 provides.
- `gen_l0_l1_outgoing_population.py --check` → exit 0, *"l0_l1_outgoing_population.json re-derives"* — **GREEN, as A2
  predicts.**
- `gen_l3_outgoing_population.py --check` → exit 1, *"STALE vs the derivation: l3_outgoing_population.json does not
  re-derive"* — **RED, as A2 predicts where Task 1 committed.**
- `gen_per_session_reading.py --check`, taken here before the read size had been regenerated → exit 2, *"STOP: the imported
  ordinary read measures 248426 characters and its committed artifact says 247953 at the same tree"*. **Cause, at the tool's
  own STOP:** the imported total is compared with `session_start_read_size.json`, which was not yet regenerated — the
  ordering the dispatch itself gives for running this tool LAST. Not a defect; nothing was changed for it (§6).

Then regenerated in order — the read size, the defense share, the L3 population, and **last** the new tool — each exit 0, and
each `--check` again → exit 0: *"the session-start read measurement re-derives"*, *"the defense-share measurement
re-derives"*, *"l3_outgoing_population.json re-derives"*, *"the per-session reading measurement re-derives"*.

**What moved, named at the blob diffs** (each regenerated file written with `git hash-object -w`; each old blob by `git
rev-parse aa0b8155…:<path>`, one command each, or the Task 1 blob; `git diff <old> <new>` between explicit blob hashes):

- `session_start_read_size.json` (`c6019963…` → `bd65f9f3…`): `at_the_tree` → `characters_per_member` → `STATUS.md`,
  `total_characters`, and both rows of `movement_against_each_earlier_reading` (`to_total`, `change_in_characters`,
  `change_percent`). Nothing else.
- `defense_share.json` (`a69ea370…` → `371d7932…`): `the_denominators_…` → `the_whole_ordinary_session_start_read`, and
  `the_totals` → `share_of_the_whole_ordinary_session_start_read`. Nothing else.
- `l3_outgoing_population.json` (`7b4f925f…` → `13d1750b…`): one RESIDUE record's `line_number` 18 → 20 — the standing
  *paraphrase* line of `STATUS.md`, moved down by the net two lines this close added above it (two entries left, three
  arrived). The new blob is the one the file carried before the previous close. **No member of `the_population`, no item-4
  passage and no member of `the_tabulation_population` moved.**
- `per_session_reading.json`, against its own Task 1 blob (`c221ad8e…` → `cfdbb22d…`): table 1's imported `STATUS.md` and
  `total_characters`; both totals-by-side (the imported read's row in each, `without_the_injected_copy_of_CLAUDE_md`,
  `with_it`, and the Cowork side's `characters`) — **the expected movement**. **Reported by field, as the dispatch orders for
  any other movement:** inside table 2's `the_marked_defense_clauses_imported`, `the_totals` →
  `share_of_the_whole_ordinary_session_start_read` and `the_two_denominators` → `the_whole_ordinary_session_start_read`
  moved — both imported from the defense share and built on `STATUS.md`'s size. **Nothing of table 2's partition, nothing of
  the populations, nothing of the boot chain moved.**
- `l0_l1_outgoing_population.json` was not regenerated (green).

Every moved value is `STATUS.md`'s size or a sum or share built on it; the values themselves are at the artifacts (D-431).

**2(d) — this report. 2(e) — the close section appended to `records/cowork/handoff/cowork_away_returns.md`. 2(f) — the
close commit**: see §4.

---

## 4. The commits

| Task | Commit | Parent | What it carries |
|---|---|---|---|
| 0 | `023353b20cd77c31552a354fc512c879c7974348` | `aa0b81558da334b755f0f93cb2fe11794a3129d5` | this dispatch and entry 463 |
| 1 | `91e45d621aa4a387271f8a4e89e9742c958c38c6` | `023353b2…` | the tool (blob `851f98ec4c1a01be133731e56bc01e5f43acf56f` = H2), its artifact (blob `c221ad8eb1e66e4b39d3722f023ac2b0bf709dad`, 141,263 bytes), the enrolment edit |
| 2 | see `git log` (the close commit cannot name its own hash) | `91e45d62…` | `STATUS.md`, `STATUS_ARCHIVE.md`, the forward-bound tool and its artifact, the four regenerated artifacts (the artifact at blob `cfdbb22d3eda609cd51fe8ddf478804ecea04087`), this report, the away-returns close |
| 3 | see `git log` | the close commit | the guard state and the end-state portion |

---

## 5. Grades

- **E0 — MET.** The named paths in one commit; `origin/master` at it; the pin proved; A1 reported with its enumeration; the
  opening capture the thirteen and nothing else; the four-name STOP; the four checks of 0(g) green.
- **E1 — MET.** The tool in the tree, hash-proved against its amended source, in the imported idiom with its docstring, bounds
  and STOPs; the seven proofs run and quoted, no change between a proof and the run; the artifact written and re-deriving; the
  two imported measurements still green; the enrolment made and the classification's five names quoted; one commit, pushed.
  No value authored into the artifact beyond the member table, the mandate column, the class definitions and the two
  compositions; no fate, no recommendation, no text moved.
- **E2 — at the tree carrying the close:** every `--check` A2 names green after regeneration, the four archive checks green;
  the failing set and the classification's STOP are taken at Task 3's run.
- **A1 — HOLDS** (§1, 0(c)).
- **A2 — HOLDS, every prediction as stated**: the evidence pin and the L0/L1 population green throughout; the read size, the
  defense share, the L3 population and the new tool red after Task 2's edits and regenerated; the guard population 83 and
  the classification naming five after the enrolment.
- **A3 — HOLDS:** `gen_l2_outgoing_population.py` was not run in any operating mode.
- **A4 — HOLDS:** exactly one tool added and enrolled; `gen_guard_state.py` edited at its authored list only;
  `gen_guard_classification.py` unedited; `gen_status_batch_bound.py` edited at its authored aiming only.
- **A5 — verified at Task 3** at the objects.

---

## 6. Declared departures

1. **The first read was partial** (1–615 of 767) and was completed in one further range before any other read.
2. **The dispatch was read from the working tree before it was pinned** — the user's opening line orders that read — so the
   pin took P-2's declared-departure route: pinned at Task 0 and proved unmoved immediately before staging.
3. **(B) reached the private field `_normalised_opening` too** (two sites, beside the two calls), renamed
   `_normalized_opening`. It is the same identifier string in the same function, and leaving it would leave a British
   spelling of the previous session's own that 1(g)'s scan must clear. The field starts with `_` and is never published.
4. **The (C) bullets restate in brief what two existing docstring paragraphs** (*HOW A SIZE IS COUNTED*, *HOW AN ADD-COMMIT
   IS FOUND*) already say; those paragraphs stand as written, the dispatch ordering nothing else changed. The (C3) bullet's
   last sentence names proof P6 and was written before P6 ran; P6 then passed with no change to the tool.
5. **The artifact's `generated_for` still names the previous dispatch's Task 1** — not one of the sites (A) to (D), so
   unchanged; the docstring's provenance line (D) names both dispatches.
6. **The governing head comment of `gen_guard_state.py`'s list (lines 72–74) was not amended** (§2, 1(h)); the enrolment
   carries its own dated comment block, as every earlier enrolment I read does. That block's opening line wraps onto a second
   comment line, where the earlier blocks fit on one.
7. **The read range for the gating identities ran past `gating_ids`** to line 637, taking in
   `gating_rows_by_how_they_were_placed`.
8. **1(f)'s two re-checks ran in one shell call**, two commands each printing its first line, rather than each in its own
   call; both exit 0.
9. **At 2(c) the new tool's `--check` was taken before the read size was regenerated** and STOPPED on the comparison the
   dispatch names as the reason it runs last; the regenerations then ran in the ordered order and it is green.
10. **Commands run with the repository as the working directory**: `changed_paths.py` (whole and `--staged`), the guard runs
    and the classification, the imported measurements, the forward-bound tool, the regenerations, the population checks, the
    new tool's runs, `git update-index`, `git checkout-index`, `git hash-object` of the tree copy, `git add`, `git commit`,
    `git push`. The `git -C /c/s/MS …` object queries and the scratch scripts ran from the scratch folder; two `cat` loops
    printed scratch output files there.
11. **`python -I -X utf8` scratch scripts inserted `tools/audit` on their own import path**, since `-I` does not.
12. **No mandate class was found named otherwise by the record I read** — the ruling records behind the mandate column were
    not opened by this batch, so that is a bound, not a check.

---

## 7. The file's state, and the ordered reads against the task

**The artifact `tools/audit/per_session_reading.json` is written, enrolled and re-deriving**, at the close tree after its own
regeneration.

**The ordered reads against the task.** The reads took most of this context before any unit was opened: the previous dispatch
whole, `DECISIONS.md` whole, the protocol section and the three imported tools were the largest, then `defense_share.json`,
the six `CLAUDE.md` spans (on top of the whole file injected at boot) and the previous report. The task itself — a recovery,
five small edits, seven short proofs — took little. **No summary of my context fell** at any point of this session up to the
writing of this report.

---

## 8. Findings of the run

None. A2's predictions all held, the corrected anchor holds at the object, and no imported function behaved otherwise than the
premise ledgers say.

---

## 9. Observations met and not acted on

- **The boot chain's "three latest handoff entries" now include entry 463**, which this batch's own Task 0 landed; the member
  is derived from add-commits, so whichever entries a dispatch lands become the three.
- **"The latest dispatch of the arc" is the thirtieth L3 tabulation dispatch** in both totals-by-side: the pruning
  iteration's own dispatches do not carry the arc's name prefix, so they are not in the population — as authored.
- **Members the table does not carry that a session of this batch read before its work:** the memory index `MEMORY.md` and the
  git status snapshot, injected at boot beside `CLAUDE.md` (also named by the previous report). Named, not added.
- **Settled spans:** two of the eight not found in the six spans — the two the 2026-08-17 ruling refused that sit in the gate
  policy block, a conditional span — and two matched by opening only, as the previous report found.

---

## 10. The plan's tell

**Did this batch produce anything other than the landed records, the tool and its artifact, the enrolment edit, the Task 2
files and the report — and, outside the repository, the scratch files, the seven proof scripts and the loose blob objects the
hash checks write?** No, apart from what those imply: the loose objects include H2 (later reached by the Task 1 commit) and the
regenerated artifacts' blobs written for the diffs; the proofs' and runs' imports wrote bytecode under
`tools/audit/__pycache__/`, which git ignores and no enumeration listed. The proof copies were held in memory inside the
scratch scripts, not written as files.

---

## 11. The self-check

Re-read the diff of every file this batch wrote: the tool (the whole H2 diff above, every passage at a site), the enrolment
entry in `gen_guard_state.py`, `STATUS.md` (three entries added, one prefix removed — read back, one `Last updated: ` line),
`tools/audit/gen_status_batch_bound.py` (five aiming edits, comments in the earlier rows' shape, former values named), this
report and the away-returns section. Against the principles: nothing touches the analysis, no `src/`, no measurement of the
analysis, no governing document beyond the two of the close; every value in this report is a tool's verbatim output or quoted
from its artifact (D-431); the anchor correction was the writing side's, applied as authored and proved at the object (#18,
#19); nothing was resolved by stretching an anchor. **Word scan of my own wording** (this report, the three `STATUS.md`
entries, the away-returns section, the enrolment entry), searched for *note*, *notes*, *key*, *part* as a word, *the rest*,
*figure(s)*, *measure* as a noun, *register* bare, *root*, *scale*, *bar*, *flat*, *stem*, *instrument*, *period*, *phrase*,
*tie*, *take part*, *status bar*, *recorded figure*, *colour*, *centre*, *judgement*, *recognise*, *normalise*, *summarise*: the
hits that stand are quoted text (tool output, the dispatch's and the old anchor, the *paraphrase* line, file names carrying
*thirtieth*, `normalised_opening` as the corrected identifier), *portion* used for the other sense, *measurement* as the
gauging noun, and *write mode* / *read-only operating mode*. No numeric grade anywhere.
