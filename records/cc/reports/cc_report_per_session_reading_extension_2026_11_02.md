# CC report — the pruning iteration, step 4's second dispatch: the per-session reading measurement extended and re-run, before and after side by side; one stale tool comment corrected (2026-11-02)

> **STATUS: SESSION REPORT.** Claude Code, 2026-11-02, executing
> `records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md` (pinned at Task 0 as blob
> `20968a55882b17b5a75fc84882ff2647dc6a063c`, 64,133 bytes). **This report decides nothing and interprets no value.** It
> is the REPORT PROPER of Ruling 4's two-file form; its APPENDIX is named in §11. **Measurement and documentation only;
> no algorithm change.**

## 0. The outcome in one paragraph

Task 0 landed this dispatch and handoff entry 476 (`dd06b5fea97a0f7e1fee4ffa35b7aebdc704ebd5`, pushed); the opening
capture was exactly A2's. **Task 1 corrected the stale comment** in `tools/audit/gen_derivation_boot_pack.py`'s `build()`
(`db25a104f8aa1c7c75903f68a2f905ecd9f88ce7`, pushed): the tool's `--check` printed byte-identical output before and after,
and the full capture was identical to the opening one. **Task 2 extended `tools/audit/gen_per_session_reading.py`** by
edits 1 to 9 and nothing else (`37d8ebb68f60a62f01b1f618288fd95a8a9a6512`, pushed): P1 to P8 PASS; the regenerated
artifact against a run of the unextended tool at the same tree is EXACTLY as predicted — additions and `generated_for`,
nothing removed, both arithmetic checks true; the capture differed from Task 1's in the one predicted verdict. **The close
ran in full**, the before-and-after table is §8. **No ★ case fired in any task.**

## 1. The ordered first read

- **First tool call, exactly:** one `Read` of `c:\s\MS\records\cc\instructions\cc_instruction_per_session_reading_extension_2026_11_02.md`,
  nothing else in the call and nothing in parallel. It returned the whole file (879 lines) in one view.
- **The two cited texts**, each command in its own call, each hash literal, each into a scratch file outside the
  repository:

  | Text | Blob | Size (`git cat-file -s`) | Scratch file |
  |---|---|---|---|
  | the fourth dispatch | `50edaf8582a3748089caffe03641a3629ed68c62` (`git rev-parse 08274008…:<path>`, as expected) | 51,166 (as expected) | `C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad\fourth_dispatch.md` |
  | the third dispatch | `6d59532fff7f64280e4daf3bc8cc588fd68d2acc` | 41,161 (as expected) | `C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad\third_dispatch.md` |

- **What reached my context as injected context at boot, each by name:** the whole of `CLAUDE.md` (as project
  instructions); the memory index `MEMORY.md`; the user's e-mail address; a git status snapshot (branch, the one standing
  modification, untracked paths, five recent commits); the commit-attribution reminder; the environment block; the skills
  list; the deferred-tools list; the Claude Docs connector's instructions and tool list; a notice of two connectors needing
  authorization.
- **Ruling 2's eight-line check — PASSED; the six-span read was NOT performed.** Each line located by search and read at
  the tree with the file tools, compared with the injected copy:

  | Line | As read at the tree | As injected |
  |---|---|---|
  | 1 (first) | `# Claude Code — Standing Instructions for This Repository` | identical |
  | 3 | `## Guiding principles` | identical |
  | 313 | `## The open-items register (user-directed, 2026-07-10; split into index + detail files, user-ratified 2026-07-26)` | identical |
  | 488 | `## The decisions register (shape user-ratified 2026-07-28; content + living surface 2026-08-02)` | identical |
  | 704 | `**Always read these two files at the start of every session:**` | identical |
  | 1536 | `## Conventions` | identical |
  | 1985 | `## The self-check after every coding exercise (user-directed, 2026-07-11)` | identical |
  | 1994 (last carrying text) | `memory of writing it. This applies to CC sessions and Cowork sessions alike.` | identical |

  *(The ruling's bound holds: an omission inside a span would pass this check. The last two line numbers are four lower
  than the fourth run's, the two pointers of Ruling 1 having replaced longer text.)*
- **Then, in order:** `STATUS.md` whole; `DECISIONS.md` whole (773 lines, three ranges); `BUILD_AND_TEST.md` whole;
  `gating_ids` at `tools/audit/nongating_apparatus_rows.json` (lines 186–409); `cowork_audit_protocol.md` lines 180–1606,
  the dispatch-protocol section to the file's end, in four ranges; the ruling record whole; entries 475 and 476 whole (476
  is the current handover block); the fourth report whole; the fourth dispatch whole (616 lines); the third dispatch at
  its lines 380–433; the tool whole (868 lines); the boot-pack tool at lines 9040–9051, located by search for *"all
  three subjects being spent"* (9046), *"EVERY SUBJECT IS STILL BUILT IN FULL"* (9043) and `for subject in
  sorted(WITHHELD):` (9049).
- **Further reads, declared** (§10, departure 1): the second dispatch (blob `abb7ef061d9f0ab922c935dfaa0157324eee8b14`,
  55,136 bytes, into `…\scratchpad\second_dispatch.md`) at its lines 460–549, and the first dispatch's text (blob
  `17d9d39c487079ba18fb6ba1380b8ad8750ca822`, 102,666 bytes, into `…\scratchpad\first_dispatch.md`) at its lines
  855–994 — the close and the end state the citation chain reaches (this dispatch's Task 3 → the fourth's → the third's
  → the second's → the first's text's Task 3, and the same for Task 4); `cowork_away_returns.md` at 30260–30364 (the
  fourth run's section, for the form of 3(e)); the fourth report's appendix by search for the one untracked `.mscx`; the
  forward-bound tool at the start tip object (by `git show` into scratch, searched for its constants) and at its head
  comments in the tree (lines 2415–2454, 2640–2676, 2915–2954, 3195–3234, and 3872–3880 by search); the L3 population
  tool's `L3_KEYWORDS` (lines 155–166) for 3(a)'s search.
- **Not read:** the L3 reading file, the derivation, `FRAMEWORK.md`, `CLAUDE.md` beyond the eight lines.

## 2. The capacity judgment

*No step of this dispatch orders a capacity judgment at a fixed point; 3(d) names one among the report's contents, so it is
written here, at 3(d), after Task 2's commit and the close's regenerations (§10, departure 2).*

```
CAPACITY JUDGMENT, written at 3(d) — after <T2> 37d8ebb6 and the close's regenerations, before the
report and its appendix are final.

What remained after it: the report proper (this file), 3(c′)'s last regeneration, the away-returns
section, the close commit, and the end state (a full guard run, the classification check, the
end-state portion, its commit).

What the ordered reads took, by my own account: the largest were DECISIONS.md whole, the
dispatch-protocol section (lines 180 to 1606), the fourth dispatch whole, the fourth report whole,
the tool whole and the ruling record whole. The eight-line check replaced the six-span read. Three
full guard captures were taken, each about eight and a half minutes, their printouts kept in scratch
files and only their comparisons read whole.

Whether a summary of my context has fallen: no.

Judgment: the remainder is mechanical and small in reading; I judge I can finish it whole.
```

**No summary of this session's context fell** at any point up to the writing of this report.

## 3. Task 0 — landed, pushed

- **0(a)** pin: `git hash-object --no-filters` blob `20968a55882b17b5a75fc84882ff2647dc6a063c`; `git cat-file -s` 64,133;
  re-hashed immediately before staging, equal; the committed blob at `<T0>` is the same object.
- **0(b)** both ref files `08274008…`. `git cat-file -p` of the start tip: parent `ac25ae01d9a06eec1fc6be1e9e1c3c7dcb6558da`;
  of that: parent `fbf6485ff6fd02dafa3b64c5fa4382acf15d7d09`. **The chain is the expected one.** `git cat-file -t
  d17a84af…`: `commit`. **The before-artifact:** `git rev-parse d17a84afdbfbf78c16ff4514df63185fad114a5c:tools/audit/per_session_reading.json`
  = **`cfdbb22d3eda609cd51fe8ddf478804ecea04087`**.
- **0(c)** A1 by `changed_paths.py` (appendix A1): exactly the one standing modification
  (`tools/audit/claude_md_finer_archive.json`); the two landing paths untracked; every other untracked path the standing
  population — the one untracked path under `tools/audit/`, `derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`, stands in
  the fourth run's enumeration too (its appendix, line 1334). 396 records (the fourth run's 394 standing + 2).
- **0(d)** last bytes at blobs written `--no-filters` (appendix A2): dispatch 64,133 bytes (`20968a55…`); entry 476 8,632
  bytes (`adae534aa0369663b06fb48f71d651ae59294e62`). Each ends with a newline after a complete line; zero zero-bytes in each.
- **0(e)** evidence pin `--check` GREEN (*"ruling records read 171"*; members 7, pinned 5, unresolved 0) — nothing
  regenerated. Staged set proved (2 paths). Commit `dd06b5fea97a0f7e1fee4ffa35b7aebdc704ebd5`, parent the start tip,
  subject `record: entry 476 and the step-4 second dispatch (the per-session reading extension)` (entry 476 existed).
  Push line `08274008d0..dd06b5fea9  master -> master`; `origin/master` read equal at the ref file. **This is `<T0>`.**
- **0(f)** opening capture (appendix A4): header *"STALE vs the run: guard_state.json does not re-derive"*; **83 run, 14
  failing, 4 not run, 20 historical; zero STOPs**; failing set = the thirteen + `gen_per_session_reading.py --check` —
  **exactly A2** (A5: read against the start tip's `summary.failing_tools` with their arguments); `gen_derivation_boot_pack.py
  --check` PASS. The start tip's `guard_state.json` → `summary`, read at its object: run 83, passing 70, failing 13, not run
  4, historical 20. Classification `--check`: exit 2, STOP naming exactly five tools — `tools/audit/gen_l0_l1_outgoing_population.py`,
  `tools/audit/gen_l2_withheld_documents.py`, `tools/audit/gen_l3_outgoing_population.py`,
  `tools/audit/gen_per_session_reading.py`, `tools/audit/gen_withheld_family_reading.py` (A6).

## 4. Task 1 — the stale comment corrected, COMMITTED

- **1(a)** `gen_derivation_boot_pack.py --check`: exit 0, *"the derivation boot pack re-derives"* and the five lines
  *"<subject>: FROZEN — <n> file(s) at their recorded blobs"* (A8). As expected.
- **1(b)** the two lines replaced by the five, with the file-editing tool, `<ACT_DATE>` 2026-11-02. The indentation at
  the object was four spaces, as the dispatch states. Nothing else in the tool.
- **1(c)** `--check` again, no writing run: **byte-identical to 1(a)** (`cmp` of the two saved files: *IDENTICAL*; A9).
  `changed_paths.py`: modified are the tool and the standing `claude_md_finer_archive.json`, nothing else. **The full
  capture against the opening capture (A10, A11):**

  ```
A: cap0_opening.txt
B: cap1_after_task1.txt
header A: STALE vs the run: guard_state.json does not re-derive
header B: STALE vs the run: guard_state.json does not re-derive
tally A: 83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
tally B: 83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
verdicts compared 107, differing 0; header same True; tally same True
  ```
- **1(d)** staged set proved (the tool). Commit `db25a104f8aa1c7c75903f68a2f905ecd9f88ce7`, parent `<T0>`, subject
  `Correct a stale comment in the derivation boot pack tool: all five built subjects are frozen`. Committed blob of the
  tool: `c115ab7559c96e83b188342ddde5111d9f4d6494` (the start tip's) → `b92021db9505ddd3d81fed1e34047fde82e0081a`. Push line
  `dd06b5fea9..db25a104f8  master -> master`; `origin/master` read equal. **This is `<T1>`.**

## 5. Task 2 — the measurement tool extended, proved, re-run, COMMITTED

- **2(a)** the tool as it stood (`<T1>` blob `851f98ec4c1a01be133731e56bc01e5f43acf56f`), a writing run then `--check`
  GREEN (A12, A13); the artifact copied to `…\scratchpad\baseline_at_this_tree.json` — **the baseline at this tree**. Its
  `the_cowork_boot_chain`'s three latest entries: **473, 472 and 476**, in that order (see observation (b)).
- **2(b)** edits 1 to 9 made with the file-editing tool in order, each anchor located by search first and found exactly
  once (`import sys` 126; `REPORT_PREFIX` 193; the prefix test 348; the table-2 comment 375; the `latest_entries` loop
  627; the two `population_summary` calls 641 and 650; `"the_injected_copy_added_in_with_it"` 717; `"generated_for"` 748;
  `"the_arc_reports": the_reports,` 774; the bound 809; the non-assertion 819; `WHY IT EXISTS.` 26; the add-commit STOP
  line 104; the `print` call's last line 848). **One spacing choice declared (§10, departure 3)**: edit 4's block stands
  with two blank lines before it and two after it, the convention between the tool's other functions. **The tool's new
  size: 1,012 lines, 59,464 characters (60,974 bytes, blob `6d3f308c889e7ec6a1ab58b98f4eef0acee8bea4`).** **The diff of the
  tool against its `<T1>` blob, whole (A14):**

  ```diff
diff --git a/851f98ec4c1a01be133731e56bc01e5f43acf56f b/6d3f308c889e7ec6a1ab58b98f4eef0acee8bea4
index 851f98ec4c..6d3f308c88 100644
--- a/851f98ec4c1a01be133731e56bc01e5f43acf56f
+++ b/6d3f308c889e7ec6a1ab58b98f4eef0acee8bea4
@@ -23,6 +23,16 @@ WHAT IT IS.  One artifact, `per_session_reading.json`, carrying two tables.
   the IMPORTED defense-share measurement; and, by text hash, the sub-blocks earlier sittings
   already settled, so that nobody re-proposes them.
 
+AND, SINCE 2026-11-02, THREE ADDITIONS (`cc_instruction_per_session_reading_extension_2026_11_02.md`,
+Task 2 — step 4's second dispatch).  (1) THE INVARIANT SHARE: for each dispatch and each report of the
+arc, the characters on lines it shares with its predecessor (the member before it in the population's
+own order), matched line for line with line endings, order ignored, whitespace-only lines apart — the
+figure the dispatch-form question waits for (handoff entry 464 §1).  (2) THE APPENDIX FILE BESIDE A
+REPORT: under Ruling 4 of the 2026-11-01 record a report's raw printouts stand in `<stem>_appendix.md`
+beside it; appendix files leave the populations, are sized beside their reports, and every report of
+the folder with one is listed with both sizes.  (3) RULING 2's AFTER-FIGURE: the Claude Code side's
+per-batch total with the six spans' file-tool read replaced by the injected copy.
+
 WHY IT EXISTS.  The user's instruction of 2026-10-31, in his words: *"After group 5, together with
 the member's feet and closing sections is a natural break: plan a pruning iteration (shrink the
 context occupied every session by mandatory reading ), then continue."*  The plan the writing side
@@ -102,6 +112,7 @@ THE STOPS — each raised as `Stop`, printed as `STOP: …`, exit 2:
   * a boot-chain anchor found other than exactly once, or the closing opener standing before the
     opening one;
   * a dispatch, a report or a handoff entry of a derived population with no add-commit;
+  * an appendix file of the reports folder with no report beside it;
   * the imported measurement's total disagreeing with its own committed artifact at the tree;
   * the defense-share denominator disagreeing with the reader's six-span total.
 
@@ -124,6 +135,7 @@ import os
 import re
 import subprocess
 import sys
+from collections import Counter
 
 HERE = os.path.dirname(os.path.abspath(__file__))
 ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
@@ -191,6 +203,7 @@ DISPATCH_FOLDER = "records/cc/instructions"
 DISPATCH_PREFIX = "cc_instruction_l3_comparison_tabulation_"
 REPORT_FOLDER = "records/cc/reports"
 REPORT_PREFIX = "cc_report_l3_comparison_tabulation_"
+APPENDIX_SUFFIX = "_appendix.md"      # Ruling 4 of the 2026-11-01 record: `<stem>_appendix.md` beside `<stem>.md`
 
 DERIVATION_PATH = "cowork_blind_derivation_l3_2026_10_17.md"
 SETTLED_SOURCES = (
@@ -345,7 +358,7 @@ def population_rows(folder: str, prefix: str, commits: dict, sized: bool = True)
     is a STOP. Ordered by (time, name)."""
     rows = []
     for name in sorted(os.listdir(os.path.join(ROOT, folder))):
-        if not name.startswith(prefix):
+        if not name.startswith(prefix) or name.endswith(APPENDIX_SUFFIX):
             continue
         path = folder + "/" + name
         if path not in commits:
@@ -372,6 +385,74 @@ def population_summary(rows: list[dict], latest: int, latest_field: str) -> dict
     }
 
 
+# ── the appendix beside a report (Ruling 4 of the 2026-11-01 record) ────────────────────────────
+def pair_appendices(names: list[str]) -> dict[str, str]:
+    """Every appendix file among `names`, keyed by the report it stands beside: the report of
+    `<stem>_appendix.md` is `<stem>.md`. An appendix with no report beside it is a STOP."""
+    present = set(names)
+    pairs = {}
+    for name in sorted(names):
+        if not name.endswith(APPENDIX_SUFFIX):
+            continue
+        report = name[:-len(APPENDIX_SUFFIX)] + ".md"
+        if report not in present:
+            raise Stop("an appendix file has no report beside it: %s" % name)
+        pairs[report] = name
+    return pairs
+
+
+# ── the invariant share: what a member shares line for line with its predecessor ───────────────
+def shared_with_predecessor(text: str, previous: str) -> dict:
+    """The characters of `text` on lines that also stand in `previous`, matched line for line with
+    their line endings, each line of `previous` matched at most once, order ignored.
+    Whitespace-only lines are counted apart and are not in the share."""
+    available = Counter(previous.splitlines(keepends=True))
+    shared = blank = 0
+    for line in text.splitlines(keepends=True):
+        if available[line] > 0:
+            available[line] -= 1
+            if line.strip():
+                shared += len(line)
+            else:
+                blank += len(line)
+    return {
+        "characters": len(text),
+        "characters_on_lines_shared_with_the_predecessor": shared,
+        "characters_on_whitespace_only_lines_shared_and_not_counted_above": blank,
+        "share_percent": round(100.0 * shared / len(text), 2) if text else 0.0,
+    }
+
+
+def invariant_shares(folder: str, rows: list[dict]) -> dict:
+    """Each member of a derived population against the member before it in the population's own
+    order (add-commit time, then name). The first member has no predecessor."""
+    previous_name = previous_text = None
+    shared_total = own_total = 0
+    for row in rows:
+        text = read(folder + "/" + row["name"])
+        if previous_text is None:
+            row["the_predecessor"] = None
+            row["shared_with_the_predecessor"] = None
+        else:
+            s = shared_with_predecessor(text, previous_text)
+            row["the_predecessor"] = previous_name
+            row["shared_with_the_predecessor"] = s
+            shared_total += s["characters_on_lines_shared_with_the_predecessor"]
+            own_total += s["characters"]
+        previous_name, previous_text = row["name"], text
+    return {
+        "members_with_a_predecessor": max(len(rows) - 1, 0),
+        "their_characters": own_total,
+        "their_characters_on_lines_shared_with_the_predecessor": shared_total,
+        "share_percent": round(100.0 * shared_total / own_total, 2) if own_total else 0.0,
+        "how_a_line_is_shared": "a line of the member, with its line ending, counts as shared when "
+                                "the predecessor holds the same line not already matched; the order "
+                                "of lines is ignored; whitespace-only lines are counted apart and are "
+                                "not in the share. A line changed by one character counts as not "
+                                "shared, and a short common line counts as shared wherever it stands.",
+    }
+
+
 # ── table 2: the six spans, partitioned ─────────────────────────────────────────────────────────
 def normalized_opening(text: str) -> str:
     """The whitespace-collapsed opening the settled-span artifacts publish — the same normalization
@@ -627,6 +708,25 @@ def build() -> dict:
     for r in latest_entries:
         r["characters"] = len(read(HANDOFF_FOLDER + "/" + r["name"]))
 
+    dispatch_shares = invariant_shares(DISPATCH_FOLDER, dispatch_rows)
+    report_shares = invariant_shares(REPORT_FOLDER, report_rows)
+    appendix_pairs = pair_appendices(sorted(os.listdir(os.path.join(ROOT, REPORT_FOLDER))))
+    for row in report_rows:
+        beside = appendix_pairs.get(row["name"])
+        row["the_appendix_beside_it"] = (
+            {"name": beside, "characters": len(read(REPORT_FOLDER + "/" + beside))} if beside else None)
+    reports_with_an_appendix = []
+    for report, beside in sorted(appendix_pairs.items()):
+        proper = len(read(REPORT_FOLDER + "/" + report))
+        appendix = len(read(REPORT_FOLDER + "/" + beside))
+        reports_with_an_appendix.append({
+            "the_report": report,
+            "characters_of_the_report_proper": proper,
+            "the_appendix": beside, "characters_of_the_appendix": appendix,
+            "the_appendix_share_of_the_two_percent":
+                round(100.0 * appendix / (proper + appendix), 2) if proper + appendix else 0.0,
+        })
+
     the_dispatches = {
         "the_folder": DISPATCH_FOLDER, "the_name_prefix": DISPATCH_PREFIX,
         "read_by": "Claude Code, per batch (its own dispatch, whole); Cowork, per sitting that "
@@ -639,6 +739,7 @@ def build() -> dict:
                                        "previous dispatch",
     }
     the_dispatches.update(population_summary(dispatch_rows, 5, "the_last_five"))
+    the_dispatches["the_invariant_share"] = dispatch_shares
     the_reports = {
         "the_folder": REPORT_FOLDER, "the_name_prefix": REPORT_PREFIX,
         "read_by": "Cowork, per sitting (whole); Claude Code, per batch (at the portions its "
@@ -648,6 +749,16 @@ def build() -> dict:
                                        "read in full — carried in the handoff entries (entry 461 §4)",
     }
     the_reports.update(population_summary(report_rows, 3, "the_last_three"))
+    the_reports["the_invariant_share"] = report_shares
+    the_reports["the_appendices_beside_them"] = {
+        "count": sum(1 for r in report_rows if r["the_appendix_beside_it"]),
+        "characters_total": sum(r["the_appendix_beside_it"]["characters"]
+                                for r in report_rows if r["the_appendix_beside_it"]),
+        "how_these_relate_to_the_sizes_above": "every size above is of the report proper only; an "
+                                               "appendix file is sized here and in "
+                                               "`the_reports_with_an_appendix_beside_them`, never "
+                                               "added to the report's own size",
+    }
 
     chain_record = ("the writing side's own boot instruction — entry 291 §4 step 3 and entry 169's "
                     "Boot block; no user ruling names these reads")
@@ -715,6 +826,12 @@ def build() -> dict:
             "without_the_injected_copy_of_CLAUDE_md": cc_without,
             "with_it": cc_without + whole,
             "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, %d characters" % whole,
+            "under_ruling_2_of_2026_11_01": cc_without + whole - six,
+            "how_ruling_2_moves_it": "Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_"
+                                     "pruning_iteration_sitting.md`: the injected copy is the read of "
+                                     "the six spans, so their file-tool read (%d characters) leaves the "
+                                     "sum and the injected copy stays; the eight-line check's own reads "
+                                     "are not sized here" % six,
             "left_out_and_said_so": "the previous report at the portions a dispatch orders, the "
                                     "reading file at its ordered portions, the ruling records a "
                                     "dispatch orders — varies per dispatch and is not sized here",
@@ -745,8 +862,10 @@ def build() -> dict:
             "text, gives no span a fate, proposes nothing and decides nothing. Every value is "
             "computed; none is transcribed (D-431).",
         "generated_by": "tools/audit/gen_per_session_reading.py",
-        "generated_for": "cc_instruction_per_session_reading_measurement_2026_11_01.md, Task 1 — "
-                         "step 1 of the pruning iteration the user ordered on 2026-10-31",
+        "generated_for": "cc_instruction_per_session_reading_extension_2026_11_02.md, Task 2 — step 4's "
+                         "second dispatch of the pruning iteration the user ordered on 2026-10-31; "
+                         "first built for step 1 (cc_instruction_per_session_reading_measurement_"
+                         "2026_11_01.md, Task 1)",
         "the_four_mandate_classes": MANDATE_CLASSES,
         "how_a_size_is_counted":
             "a whole file is `len(text)` of the file read by the imported `at_tree` (UTF-8, universal "
@@ -772,6 +891,20 @@ def build() -> dict:
             "the_further_members": further,
             "the_arc_dispatches": the_dispatches,
             "the_arc_reports": the_reports,
+            "the_reports_with_an_appendix_beside_them": {
+                "the_folder": REPORT_FOLDER,
+                "how_a_pair_is_found": "every file of the folder whose name ends `%s`, beside the report "
+                                       "named by its stem; an appendix with no report beside it is a "
+                                       "STOP" % APPENDIX_SUFFIX,
+                "read_by": "Cowork: the report proper in full under the user's rule of 2026-09-03, the "
+                           "appendix at need (Ruling 4 of the 2026-11-01 record)",
+                "count": len(reports_with_an_appendix),
+                "characters_of_the_reports_proper": sum(r["characters_of_the_report_proper"]
+                                                        for r in reports_with_an_appendix),
+                "characters_of_the_appendices": sum(r["characters_of_the_appendix"]
+                                                    for r in reports_with_an_appendix),
+                "the_pairs": reports_with_an_appendix,
+            },
             "the_cowork_boot_chain": boot_chain,
             "totals_by_side": totals_by_side,
         },
@@ -807,6 +940,10 @@ def build() -> dict:
             "The injected copy of `CLAUDE.md` is DECLARED by the executing sessions; this tool "
             "measures the file, not the copy.",
             "The dispatch and report populations are complete only relative to their name prefixes.",
+            "The invariant share is a LINE measure, not a judgement of copying: a line changed by one "
+            "character counts as not shared, and a short common line counts as shared wherever it "
+            "stands. It compares each member with its predecessor only.",
+            "An appendix file is found by its name alone (`<stem>_appendix.md` beside `<stem>.md`).",
             "The imported recognizers are patterns over prose whose reach is UNMEASURED (D-673 "
             "applies: no analysis decision consumes this enumeration); the doubt default places "
             "what no recognizer places; and a sub-block cut at a ★ marker may carry a sentence that "
@@ -817,6 +954,8 @@ def build() -> dict:
             "That any mandate class is right.",
             "That the injected copy of `CLAUDE.md` exists or has the size of the file.",
             "That the dispatch and report populations are complete beyond the name prefixes.",
+            "That a line shared with the predecessor was copied from it, or that a line not shared "
+            "was newly written.",
             "That any sub-block's class is right.",
             "That any size is small or large enough — that is the user's question at step 3.",
             "That any text should move — this tool proposes nothing.",
@@ -846,6 +985,12 @@ def main(argv: list[str]) -> int:
     print("  arc dispatches %d, %d characters; arc reports %d, %d characters"
           % (t1["the_arc_dispatches"]["count"], t1["the_arc_dispatches"]["characters_total"],
              t1["the_arc_reports"]["count"], t1["the_arc_reports"]["characters_total"]))
+    print("  invariant share: dispatches %.2f %%, reports %.2f %%"
+          % (t1["the_arc_dispatches"]["the_invariant_share"]["share_percent"],
+             t1["the_arc_reports"]["the_invariant_share"]["share_percent"]))
+    ap = t1["the_reports_with_an_appendix_beside_them"]
+    print("  reports with an appendix beside them %d: reports proper %d, appendices %d characters"
+          % (ap["count"], ap["characters_of_the_reports_proper"], ap["characters_of_the_appendices"]))
     for name, side in t1["totals_by_side"].items():
         value = side.get("without_the_injected_copy_of_CLAUDE_md", side.get("characters"))
         print("  %s: %d" % (name, value))
  ```
- **2(c) the planted-fault proofs — ALL PASS** (the scratch script `t2c_proofs.py`, quoted whole at A15; P7 and P8 run
  after 2(d)). Its output, whole:

  ```
P1 PASS — {'characters': 8, 'characters_on_lines_shared_with_the_predecessor': 4, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 1, 'share_percent': 50.0}
P2 PASS — {'characters': 4, 'characters_on_lines_shared_with_the_predecessor': 4, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 0, 'share_percent': 100.0}
P3 PASS — {'first': {'characters': 4, 'characters_on_lines_shared_with_the_predecessor': 0, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 0, 'share_percent': 0.0}, 'second': {'characters': 0, 'characters_on_lines_shared_with_the_predecessor': 0, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 0, 'share_percent': 0.0}}
P4 PASS — {'characters': 8, 'characters_on_lines_shared_with_the_predecessor': 4, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 0, 'share_percent': 50.0}
P5 PASS — Stop: an appendix file has no report beside it: r_y_appendix.md
P6 PASS — {'r_x.md': 'r_x_appendix.md'}
P7 PASS — {'the_arc_dispatches': {'members': 30, 'appendix_names': [], 'first_has_no_predecessor': True, 'every_other_predecessor_is_the_member_before': True, 'every_other_carries_a_share': True}, 'the_arc_reports': {'members': 30, 'appendix_names': [], 'first_has_no_predecessor': True, 'every_other_predecessor_is_the_member_before': True, 'every_other_carries_a_share': True}}
P8 PASS — {'count': 4, 'the_pairs': {'cc_report_pruning_rulings_execution_2026_11_01.md': 'cc_report_pruning_rulings_execution_2026_11_01_appendix.md', 'cc_report_pruning_rulings_fourth_execution_2026_11_02.md': 'cc_report_pruning_rulings_fourth_execution_2026_11_02_appendix.md', 'cc_report_pruning_rulings_reexecution_2026_11_01.md': 'cc_report_pruning_rulings_reexecution_2026_11_01_appendix.md', 'cc_report_pruning_rulings_third_execution_2026_11_01.md': 'cc_report_pruning_rulings_third_execution_2026_11_01_appendix.md'}, 'above_four_reported_not_a_failure': False}
ALL PASS
  ```

  P8's count is exactly four, so *"a count above 4"* did not arise.
- **2(d)** the writing run, then `--check` GREEN (A16, A17), the new printout lines included. **The `--check` run's wall
  time: 3.0 seconds** (`real 0m3.017s`, A17) — the first NOT KNOWN item of the premise ledger.
- **2(e) THE COMPARISON WITH THE BASELINE AT THIS TREE — AS PREDICTED** (the scratch script `t2e_compare.py`, A18; every
  per-path record at A19). Its classed summary and both arithmetic checks, verbatim:

  ```
== differences: 179
      2  added: an edit 8 (iii) bound sentence, after the populations bound
      1  added: how_ruling_2_moves_it under the Claude Code side
     35  added: shared_with_the_predecessor in a member record of the_arc_dispatches
     33  added: shared_with_the_predecessor in a member record of the_arc_reports
      1  added: the edit 8 (iv) non-assertion, after the populations one
      1  added: the_appendices_beside_them under the_arc_reports
     33  added: the_appendix_beside_it in a member record of the_arc_reports
      1  added: the_invariant_share under the_arc_dispatches
      1  added: the_invariant_share under the_arc_reports
     35  added: the_predecessor in a member record of the_arc_dispatches
     33  added: the_predecessor in a member record of the_arc_reports
      1  added: the_reports_with_an_appendix_beside_them under table 1
      1  added: under_ruling_2_of_2026_11_01 under the Claude Code side
      1  changed: generated_for
generated_for former: cc_instruction_per_session_reading_measurement_2026_11_01.md, Task 1 — step 1 of the pruning iteration the user ordered on 2026-10-31
generated_for new:    cc_instruction_per_session_reading_extension_2026_11_02.md, Task 2 — step 4's second dispatch of the pruning iteration the user ordered on 2026-10-31; first built for step 1 (cc_instruction_per_session_reading_measurement_2026_11_01.md, Task 1)
changed values other than generated_for: 0
removed: 0
member records lacking a predicted added field: 0
ARITH 1: under_ruling_2_of_2026_11_01 738504 == with_it 843945 - six spans 105441 = 738504 : True
ARITH 2: characters_of_the_appendices 578857 == sum of pairs 578857 : True
predicted single additions present in the predicted number: True
2(e) COMPARISON: AS PREDICTED
  ```

  The member-record counts are the population and the latest subset: 35 = 30 dispatches + the last five; 33 = 30 reports
  + the last three. The two lists of edit 8 (iii) and (iv) were compared as lists of strings; the three bound sentences
  stand in two list elements, as edit 8 (iii) writes them.
- **2(f) the full capture against Task 1's (A20, A21):**

  ```
A: cap1_after_task1.txt
B: cap2_after_task2.txt
header A: STALE vs the run: guard_state.json does not re-derive
header B: STALE vs the run: guard_state.json does not re-derive
tally A: 83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
tally B: 83 guard(s) run, 13 failing, 4 not run, 20 historical record(s)
DIFFERS: tools/audit/gen_per_session_reading.py --check : FAIL -> PASS
verdicts compared 107, differing 1; header same True; tally same False
  ```

  **Exactly one verdict differs, `gen_per_session_reading.py --check` FAIL → PASS. The risk the dispatch named — a guard
  pinning either tool's own blob — did not materialize** at Task 1 or here.
- **2(g)** staged set proved (the tool and the artifact). Commit `37d8ebb68f60a62f01b1f618288fd95a8a9a6512`, parent `<T1>`,
  subject `Extend the per-session reading measurement: the invariant share, the appendix beside a report, Ruling 2's
  after-figure`. Committed blobs: tool `6d3f308c…`, artifact `2b652810b2e21268b382e53dadee38f0f7391acc`. Push line
  `db25a104f8..37d8ebb68f  master -> master`; `origin/master` read equal. **This is `<T2>`.**

## 6. Task 3 — the close

- **3(a)** four entries written at the top of `STATUS.md`: the close entry (naming this dispatch, carrying `Last updated: `),
  then Task 2's, Task 1's and Task 0's, each `Same dispatch`. The prefix was MOVED off the fourth dispatch's close entry in
  the same edit; one line carries it (searched: one occurrence). **The search:** case-insensitive, the 26 `L3_KEYWORDS`
  (the L3 population tool's lines 155–164) plus *repeat* and *tie* as substrings, over `STATUS.md` — **one hit, line 30,
  `phrase`** (inside the standing *paraphrase* line, at that moment eight lines lower than its usual place).
- **3(b)** the tool read at the `08274008…` object first; its authored constants were the relayed ones — `BASE_COMMIT`
  `fbf6485ff6fd02dafa3b64c5fa4382acf15d7d09`, `PREVIOUS_BATCH_DISPATCH` the third dispatch, `DISPATCH` the fourth dispatch,
  `TASK` `Task 3`, `MOVE_KIND` `ordinary`, `ACT_DATE` 2026-11-02. `STATUS.md` blob at `37d8ebb6…` = at `08274008…` =
  `990cfeb244cd1e5de76cae57a5d0c0a9e8b052ce` (each `git rev-parse` in its own command). Re-aimed: `BASE_COMMIT` → `<T2>`
  (the last task commit), `PREVIOUS_BATCH_DISPATCH` → the fourth dispatch, `DISPATCH` → this dispatch, `ACT_DATE`,
  `TASK` and `MOVE_KIND` kept; one aiming appended; the former values named in the head comments. `--apply`: *"entries
  moved: 4, 2,639 characters"*, present in the archive once, absent from the must-read; `the_moved` = the base's lines 8
  (the fourth dispatch's close entry, the declared adjustment applied), 10, 12 and 14 (its Task 2, Task 1 and Task 0
  entries) — **exactly the prediction; no STOP**; the two 2026-09-02 entries stay. `--check` and the other three archive
  checks (`--pair STATUS.md`, `gen_status_residue_move.py`, `gen_status_archive_pass.py`) exit 0 (A22, A23).
- **3(c)** evidence pin GREEN (never regenerated). Read size and defense share RED, regenerated, `--check` green.
  **L0/L1 GREEN and L3 GREEN** — not regenerated: the four entries 3(a) added and the four 3(b) moved out leave the
  *paraphrase* residue record's line where it stood. The boot-pack manifest not regenerated; its `--check` exit 0. Then
  LAST `gen_per_session_reading.py` (its `--check` red before), `--check` green. All re-run whole at A25. **Each artifact
  against its base blob** (the scratch script `t3c_diffs.py`, A26; each diff whole there):
  - `session_start_read_size.json` (`5b4a3465…` → `f86a3fe2…`, against the start tip): the `STATUS.md` member and the
    total, and the two regime comparisons built on the total (`to_total`, `change_in_characters`, `change_percent`).
    Nothing else.
  - `defense_share.json` (`15f65041…` → `a0ba4c07…`, against the start tip): the whole-read denominator and the share
    against it. Nothing else.
  - `l0_l1_outgoing_population.json` and `l3_outgoing_population.json`: **unchanged** at their start-tip blobs
    (`d4a7a548…`, `8aac2cfc…`).
  - `per_session_reading.json` (`2b652810…` → `5a927584…`, against `<T2>`): the ordinary read's `STATUS.md` member and
    `total_characters`; its mirrors in both sides' member lists of `totals_by_side` and the sums that include it
    (`without_the_injected_copy_of_CLAUDE_md`, `with_it`, `under_ruling_2_of_2026_11_01`, the Cowork side's
    `characters`); the imported `the_two_denominators` → `the_whole_ordinary_session_start_read`; **and** the imported
    `the_totals` → `share_of_the_whole_ordinary_session_start_read`, a value computed from that same denominator
    (observation (a)). Nothing of the arc populations, the invariant shares, the appendix pairs, the boot chain or table
    2's spans moved.
- **3(c′)** the last regeneration runs after this report and its appendix are final; its output and its diff are in the
  away-returns section, not here.
- **3(d)** this report and its appendix (§11). **3(e)** the close section appended to
  `records/cowork/handoff/cowork_away_returns.md`. **3(f)** the close commit (named in the away-returns end-state portion).

## 7. The commits

| Task | Commit | Parent | Committed blobs |
|---|---|---|---|
| 0 | `dd06b5fea97a0f7e1fee4ffa35b7aebdc704ebd5` | `08274008…` | dispatch `20968a55…`, entry 476 `adae534a…` |
| 1 | `db25a104f8aa1c7c75903f68a2f905ecd9f88ce7` | `dd06b5fe…` | `gen_derivation_boot_pack.py` `b92021db…` |
| 2 | `37d8ebb68f60a62f01b1f618288fd95a8a9a6512` | `db25a104…` | `gen_per_session_reading.py` `6d3f308c…`, `per_session_reading.json` `2b652810…` |
| close | named in the away-returns end-state portion (written after the commit exists) | `37d8ebb6…` | |

## 8. THE BEFORE AND AFTER TABLE

The scratch script `t3d_before_after.py` (quoted whole at A28) reads the before-artifact — the artifact at
`d17a84afdbfbf78c16ff4514df63185fad114a5c`, blob `cfdbb22d…`, the close of the step-1 measurement's remainder batch — and
the after-artifact, the working-tree file as 3(c) left it, and prints every value below from the two objects; none is
typed. **The appendix pairs are as 3(c) left them, so without this batch's own pair, which 3(c′) adds.**

**Which rulings the moved values belong to, where the record says so:** the `CLAUDE.md` values (the six spans, the
whole file, table 2's archive-class characters) belong to **Ruling 1** (the two former wordings moved, the fourth report);
the `DECISIONS.md` member to **Ruling 3** (the four classes of history text moved, the third run); and
`under_ruling_2_of_2026_11_01` is **Ruling 2**'s total. The `STATUS.md` member and the three latest handoff entries are
not attributed to any ruling by the record, and this report attributes them to none.

**1. The ordinary session-start read (imported)**

| Value | Before | After | Difference |
|---|---|---|---|
| total_characters | 248,426 | 237,414 | -11,012 |
| characters_per_member → CLAUDE.md | 105,876 | 105,441 | -435 |
| characters_per_member → STATUS.md | 11,997 | 11,657 | -340 |
| characters_per_member → DECISIONS.md | 127,727 | 117,490 | -10,237 |
| characters_per_member → tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids | 2,826 | 2,826 | +0 |

**2. The reading of CLAUDE.md (the six spans)**

| Value | Before | After | Difference |
|---|---|---|---|
| the_reading_of_claude_md → characters | 105,876 | 105,441 | -435 |

**3. The further members**

| Value | Before | After | Difference |
|---|---|---|---|
| CLAUDE.md, the whole file as the executing sessions report it injected at boot | 169,617 | 169,182 | -435 |
| BUILD_AND_TEST.md | 27,236 | 27,236 | +0 |
| cowork_audit_protocol.md, the dispatch-protocol section | 108,389 | 108,389 | +0 |
| the blind derivation of L3, whole | 126,702 | 126,702 | +0 |

**4. The arc dispatches and the arc reports**

| Value | Before | After | Difference |
|---|---|---|---|
| the_arc_dispatches → count | 30 | 30 | +0 |
| the_arc_dispatches → characters_total | 4,982,224 | 4,982,224 | +0 |
| the_arc_dispatches → characters_mean | 166,074 | 166,074 | +0 |
| the_arc_dispatches → characters_max | 259,912 | 259,912 | +0 |
| the_arc_reports → count | 30 | 30 | +0 |
| the_arc_reports → characters_total | 3,741,155 | 3,741,155 | +0 |
| the_arc_reports → characters_mean | 124,705 | 124,705 | +0 |
| the_arc_reports → characters_max | 520,923 | 520,923 | +0 |

**5. The Cowork boot chain**

| Value | Before | After | Difference |
|---|---|---|---|
| entry 118, the bridge-fault section | 2,075 | 2,075 | +0 |
| entry 152, items (v) to (x) | 3,580 | 3,580 | +0 |
| entry 169, whole | 24,913 | 24,913 | +0 |
| entry 291, whole | 9,655 | 9,655 | +0 |
| the three handoff entry files with the latest add-commits | 46,985 | 22,955 | -24,030 |

The three latest entries — before: cowork_handoff_entry_four_hundred_and_sixty_one.md (15,962), cowork_handoff_entry_four_hundred_and_sixty_two.md (14,669), cowork_handoff_entry_four_hundred_and_sixty_three.md (16,354); after: cowork_handoff_entry_four_hundred_and_seventy_three.md (7,122), cowork_handoff_entry_four_hundred_and_seventy_two.md (7,261), cowork_handoff_entry_four_hundred_and_seventy_six.md (8,572).

**6. Totals by side**

| Value | Before | After | Difference |
|---|---|---|---|
| Claude Code → without_the_injected_copy_of_CLAUDE_md | 709,543 | 674,501 | -35,042 |
| Claude Code → with_it | 879,160 | 843,683 | -35,477 |
| Cowork → characters | 1,008,362 | 973,320 | -35,042 |

**7. Table 2, the six spans partitioned — totals**

| Value | Before | After | Difference |
|---|---|---|---|
| characters_of_the_six_spans | 105,876 | 105,441 | -435 |
| sub_block_count | 106 | 106 | +0 |
| archive_class_characters | 14,269 | 13,834 | -435 |
| doubt_defaulted_characters | 90,909 | 90,909 | +0 |

**After only — values that did not exist before**

- `under_ruling_2_of_2026_11_01`: 738,242 (with_it 843,683 less the six spans 105,441)
- `the_arc_dispatches` → `the_invariant_share`, whole:

```json
{
 "members_with_a_predecessor": 29,
 "their_characters": 4883215,
 "their_characters_on_lines_shared_with_the_predecessor": 1579730,
 "share_percent": 32.35,
 "how_a_line_is_shared": "a line of the member, with its line ending, counts as shared when the predecessor holds the same line not already matched; the order of lines is ignored; whitespace-only lines are counted apart and are not in the share. A line changed by one character counts as not shared, and a short common line counts as shared wherever it stands."
}
```

- `the_arc_reports` → `the_invariant_share`, whole:

```json
{
 "members_with_a_predecessor": 29,
 "their_characters": 3680373,
 "their_characters_on_lines_shared_with_the_predecessor": 699415,
 "share_percent": 19.0,
 "how_a_line_is_shared": "a line of the member, with its line ending, counts as shared when the predecessor holds the same line not already matched; the order of lines is ignored; whitespace-only lines are counted apart and are not in the share. A line changed by one character counts as not shared, and a short common line counts as shared wherever it stands."
}
```

- `the_arc_reports` → `the_appendices_beside_them`, whole:

```json
{
 "count": 0,
 "characters_total": 0,
 "how_these_relate_to_the_sizes_above": "every size above is of the report proper only; an appendix file is sized here and in `the_reports_with_an_appendix_beside_them`, never added to the report's own size"
}
```

- `the_reports_with_an_appendix_beside_them`, without `the_pairs`:

```json
{
 "the_folder": "records/cc/reports",
 "how_a_pair_is_found": "every file of the folder whose name ends `_appendix.md`, beside the report named by its stem; an appendix with no report beside it is a STOP",
 "read_by": "Cowork: the report proper in full under the user's rule of 2026-09-03, the appendix at need (Ruling 4 of the 2026-11-01 record)",
 "count": 4,
 "characters_of_the_reports_proper": 131829,
 "characters_of_the_appendices": 578857
}
```

| The report | Report proper (characters) | Appendix (characters) | Appendix share of the two |
|---|---|---|---|
| `cc_report_pruning_rulings_execution_2026_11_01.md` | 25,664 | 88,629 | 77.55 % |
| `cc_report_pruning_rulings_fourth_execution_2026_11_02.md` | 42,897 | 261,900 | 85.93 % |
| `cc_report_pruning_rulings_reexecution_2026_11_01.md` | 30,008 | 73,269 | 70.94 % |
| `cc_report_pruning_rulings_third_execution_2026_11_01.md` | 33,260 | 155,059 | 82.34 % |

**The second table — per arc member, after only**

*the_arc_dispatches*

| # | Name | Characters | Predecessor | Share % |
|---|---|---|---|---|
| 1 | `cc_instruction_l3_comparison_tabulation_2026_10_18.md` | 99,009 | — | — |
| 2 | `cc_instruction_l3_comparison_tabulation_second_2026_10_18.md` | 80,466 | `cc_instruction_l3_comparison_tabulation_2026_10_18.md` | 34.45 |
| 3 | `cc_instruction_l3_comparison_tabulation_third_2026_10_19.md` | 84,717 | `cc_instruction_l3_comparison_tabulation_second_2026_10_18.md` | 51.52 |
| 4 | `cc_instruction_l3_comparison_tabulation_fourth_2026_10_19.md` | 92,356 | `cc_instruction_l3_comparison_tabulation_third_2026_10_19.md` | 54.89 |
| 5 | `cc_instruction_l3_comparison_tabulation_fifth_2026_10_19.md` | 98,630 | `cc_instruction_l3_comparison_tabulation_fourth_2026_10_19.md` | 54.37 |
| 6 | `cc_instruction_l3_comparison_tabulation_sixth_2026_10_19.md` | 111,310 | `cc_instruction_l3_comparison_tabulation_fifth_2026_10_19.md` | 49.58 |
| 7 | `cc_instruction_l3_comparison_tabulation_seventh_2026_10_19.md` | 126,198 | `cc_instruction_l3_comparison_tabulation_sixth_2026_10_19.md` | 43.83 |
| 8 | `cc_instruction_l3_comparison_tabulation_eighth_2026_10_19.md` | 136,728 | `cc_instruction_l3_comparison_tabulation_seventh_2026_10_19.md` | 46.98 |
| 9 | `cc_instruction_l3_comparison_tabulation_ninth_2026_10_20.md` | 153,800 | `cc_instruction_l3_comparison_tabulation_eighth_2026_10_19.md` | 36.61 |
| 10 | `cc_instruction_l3_comparison_tabulation_tenth_2026_10_20.md` | 172,851 | `cc_instruction_l3_comparison_tabulation_ninth_2026_10_20.md` | 37.21 |
| 11 | `cc_instruction_l3_comparison_tabulation_eleventh_2026_10_20.md` | 156,452 | `cc_instruction_l3_comparison_tabulation_tenth_2026_10_20.md` | 34.20 |
| 12 | `cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md` | 153,985 | `cc_instruction_l3_comparison_tabulation_eleventh_2026_10_20.md` | 43.63 |
| 13 | `cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md` | 171,675 | `cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md` | 38.78 |
| 14 | `cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md` | 185,731 | `cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md` | 39.69 |
| 15 | `cc_instruction_l3_comparison_tabulation_fifteenth_2026_10_24.md` | 181,526 | `cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md` | 30.31 |
| 16 | `cc_instruction_l3_comparison_tabulation_sixteenth_2026_10_24.md` | 169,864 | `cc_instruction_l3_comparison_tabulation_fifteenth_2026_10_24.md` | 30.15 |
| 17 | `cc_instruction_l3_comparison_tabulation_seventeenth_2026_10_24.md` | 177,296 | `cc_instruction_l3_comparison_tabulation_sixteenth_2026_10_24.md` | 28.01 |
| 18 | `cc_instruction_l3_comparison_tabulation_eighteenth_2026_10_25.md` | 190,948 | `cc_instruction_l3_comparison_tabulation_seventeenth_2026_10_24.md` | 27.84 |
| 19 | `cc_instruction_l3_comparison_tabulation_nineteenth_2026_10_26.md` | 205,990 | `cc_instruction_l3_comparison_tabulation_eighteenth_2026_10_25.md` | 28.44 |
| 20 | `cc_instruction_l3_comparison_tabulation_twentieth_2026_10_26.md` | 224,366 | `cc_instruction_l3_comparison_tabulation_nineteenth_2026_10_26.md` | 27.30 |
| 21 | `cc_instruction_l3_comparison_tabulation_twenty_first_2026_10_26.md` | 210,734 | `cc_instruction_l3_comparison_tabulation_twentieth_2026_10_26.md` | 26.49 |
| 22 | `cc_instruction_l3_comparison_tabulation_twenty_second_2026_10_26.md` | 166,056 | `cc_instruction_l3_comparison_tabulation_twenty_first_2026_10_26.md` | 26.30 |
| 23 | `cc_instruction_l3_comparison_tabulation_twenty_third_2026_10_26.md` | 164,756 | `cc_instruction_l3_comparison_tabulation_twenty_second_2026_10_26.md` | 21.72 |
| 24 | `cc_instruction_l3_comparison_tabulation_twenty_fourth_2026_10_27.md` | 188,439 | `cc_instruction_l3_comparison_tabulation_twenty_third_2026_10_26.md` | 21.85 |
| 25 | `cc_instruction_l3_comparison_tabulation_twenty_fifth_2026_10_27.md` | 212,059 | `cc_instruction_l3_comparison_tabulation_twenty_fourth_2026_10_27.md` | 30.72 |
| 26 | `cc_instruction_l3_comparison_tabulation_twenty_sixth_2026_10_27.md` | 239,614 | `cc_instruction_l3_comparison_tabulation_twenty_fifth_2026_10_27.md` | 30.13 |
| 27 | `cc_instruction_l3_comparison_tabulation_twenty_seventh_2026_10_28.md` | 259,912 | `cc_instruction_l3_comparison_tabulation_twenty_sixth_2026_10_27.md` | 29.35 |
| 28 | `cc_instruction_l3_comparison_tabulation_twenty_eighth_2026_10_30.md` | 233,425 | `cc_instruction_l3_comparison_tabulation_twenty_seventh_2026_10_28.md` | 24.08 |
| 29 | `cc_instruction_l3_comparison_tabulation_twenty_ninth_2026_10_31.md` | 181,526 | `cc_instruction_l3_comparison_tabulation_twenty_eighth_2026_10_30.md` | 15.90 |
| 30 | `cc_instruction_l3_comparison_tabulation_thirtieth_2026_10_31.md` | 151,805 | `cc_instruction_l3_comparison_tabulation_twenty_ninth_2026_10_31.md` | 28.75 |

*the_arc_reports*

| # | Name | Characters | Predecessor | Share % |
|---|---|---|---|---|
| 1 | `cc_report_l3_comparison_tabulation_2026_10_18.md` | 60,782 | — | — |
| 2 | `cc_report_l3_comparison_tabulation_second_2026_10_18.md` | 46,542 | `cc_report_l3_comparison_tabulation_2026_10_18.md` | 28.33 |
| 3 | `cc_report_l3_comparison_tabulation_third_2026_10_19.md` | 54,986 | `cc_report_l3_comparison_tabulation_second_2026_10_18.md` | 35.53 |
| 4 | `cc_report_l3_comparison_tabulation_fourth_2026_10_19.md` | 61,723 | `cc_report_l3_comparison_tabulation_third_2026_10_19.md` | 50.21 |
| 5 | `cc_report_l3_comparison_tabulation_fifth_2026_10_19.md` | 69,767 | `cc_report_l3_comparison_tabulation_fourth_2026_10_19.md` | 43.10 |
| 6 | `cc_report_l3_comparison_tabulation_sixth_2026_10_19.md` | 56,766 | `cc_report_l3_comparison_tabulation_fifth_2026_10_19.md` | 41.57 |
| 7 | `cc_report_l3_comparison_tabulation_seventh_2026_10_19.md` | 57,458 | `cc_report_l3_comparison_tabulation_sixth_2026_10_19.md` | 33.40 |
| 8 | `cc_report_l3_comparison_tabulation_eighth_2026_10_19.md` | 72,330 | `cc_report_l3_comparison_tabulation_seventh_2026_10_19.md` | 20.31 |
| 9 | `cc_report_l3_comparison_tabulation_ninth_2026_10_20.md` | 62,175 | `cc_report_l3_comparison_tabulation_eighth_2026_10_19.md` | 33.98 |
| 10 | `cc_report_l3_comparison_tabulation_tenth_2026_10_20.md` | 74,764 | `cc_report_l3_comparison_tabulation_ninth_2026_10_20.md` | 20.89 |
| 11 | `cc_report_l3_comparison_tabulation_eleventh_2026_10_20.md` | 79,270 | `cc_report_l3_comparison_tabulation_tenth_2026_10_20.md` | 29.01 |
| 12 | `cc_report_l3_comparison_tabulation_twelfth_2026_10_20.md` | 134,126 | `cc_report_l3_comparison_tabulation_eleventh_2026_10_20.md` | 21.69 |
| 13 | `cc_report_l3_comparison_tabulation_thirteenth_2026_10_21.md` | 117,568 | `cc_report_l3_comparison_tabulation_twelfth_2026_10_20.md` | 23.11 |
| 14 | `cc_report_l3_comparison_tabulation_fourteenth_2026_10_23.md` | 63,286 | `cc_report_l3_comparison_tabulation_thirteenth_2026_10_21.md` | 28.04 |
| 15 | `cc_report_l3_comparison_tabulation_fifteenth_2026_10_24.md` | 71,420 | `cc_report_l3_comparison_tabulation_fourteenth_2026_10_23.md` | 30.46 |
| 16 | `cc_report_l3_comparison_tabulation_sixteenth_2026_10_24.md` | 73,117 | `cc_report_l3_comparison_tabulation_fifteenth_2026_10_24.md` | 37.06 |
| 17 | `cc_report_l3_comparison_tabulation_seventeenth_2026_10_24.md` | 89,385 | `cc_report_l3_comparison_tabulation_sixteenth_2026_10_24.md` | 31.95 |
| 18 | `cc_report_l3_comparison_tabulation_eighteenth_2026_10_25.md` | 114,017 | `cc_report_l3_comparison_tabulation_seventeenth_2026_10_24.md` | 25.82 |
| 19 | `cc_report_l3_comparison_tabulation_nineteenth_2026_10_26.md` | 79,766 | `cc_report_l3_comparison_tabulation_eighteenth_2026_10_25.md` | 24.78 |
| 20 | `cc_report_l3_comparison_tabulation_twentieth_2026_10_26.md` | 139,118 | `cc_report_l3_comparison_tabulation_nineteenth_2026_10_26.md` | 13.56 |
| 21 | `cc_report_l3_comparison_tabulation_twenty_first_2026_10_26.md` | 221,926 | `cc_report_l3_comparison_tabulation_twentieth_2026_10_26.md` | 11.54 |
| 22 | `cc_report_l3_comparison_tabulation_twenty_second_2026_10_26.md` | 152,663 | `cc_report_l3_comparison_tabulation_twenty_first_2026_10_26.md` | 23.34 |
| 23 | `cc_report_l3_comparison_tabulation_twenty_third_2026_10_26.md` | 167,250 | `cc_report_l3_comparison_tabulation_twenty_second_2026_10_26.md` | 9.30 |
| 24 | `cc_report_l3_comparison_tabulation_twenty_fourth_2026_10_27.md` | 132,154 | `cc_report_l3_comparison_tabulation_twenty_third_2026_10_26.md` | 11.90 |
| 25 | `cc_report_l3_comparison_tabulation_twenty_fifth_2026_10_27.md` | 228,900 | `cc_report_l3_comparison_tabulation_twenty_fourth_2026_10_27.md` | 7.74 |
| 26 | `cc_report_l3_comparison_tabulation_twenty_sixth_2026_10_27.md` | 246,250 | `cc_report_l3_comparison_tabulation_twenty_fifth_2026_10_27.md` | 15.18 |
| 27 | `cc_report_l3_comparison_tabulation_twenty_seventh_2026_10_28.md` | 260,055 | `cc_report_l3_comparison_tabulation_twenty_sixth_2026_10_27.md` | 16.72 |
| 28 | `cc_report_l3_comparison_tabulation_twenty_eighth_2026_10_30.md` | 142,049 | `cc_report_l3_comparison_tabulation_twenty_seventh_2026_10_28.md` | 28.81 |
| 29 | `cc_report_l3_comparison_tabulation_twenty_ninth_2026_10_31.md` | 90,619 | `cc_report_l3_comparison_tabulation_twenty_eighth_2026_10_30.md` | 20.66 |
| 30 | `cc_report_l3_comparison_tabulation_thirtieth_2026_10_31.md` | 520,923 | `cc_report_l3_comparison_tabulation_twenty_ninth_2026_10_31.md` | 3.49 |

## 9. Grades

- **E0 — MET.** **E1 — MET:** the comment corrected; the boot-pack check's output byte-identical; the capture identical to
  the opening one; one commit, pushed. **E2 — MET:** the tool extended by edits 1 to 9 and nothing else (the diff, §5); P1
  to P8 PASS; the comparison exactly as predicted; the capture differing in the one predicted verdict; one commit, pushed.
  **E3** — asserted at Task 4, not here.
- **A1 — HELD** (`changed_paths.py`: the one standing modification; the two landing paths untracked; the standing
  population). **A2 — HELD in every limb:** the opening failing set; Task 1's capture identical and the boot-pack check's
  output unchanged; at Task 2 the per-session check green after 2(a) and after 2(d), and exactly one verdict differing,
  FAIL → PASS; at 3(c) L0/L1 and L3 green, both allowed. **A3 — HELD** (no `src/` file, build, test, golden, corpus of
  scores or measurement of the analysis touched). **A4/A5** — verified at Task 4.

## 10. Declared departures and observations

**Departures.**

1. **Reads beyond the ordered list**, each named in §1: the second dispatch and the first dispatch's text at their close
   and end-state tasks — the citation chain of this dispatch's Task 3 and Task 4 reaches them, and their steps (the
   prefix move, the search, the archive checks, the end-state condition) could not be executed by citation without them
   — the fourth run's away-returns section, the fourth appendix by search, the forward-bound tool's object and head
   comments, and the L3 keyword list.
2. **The capacity judgment is written at 3(d)**, not at a step before a task: this dispatch orders it only among the
   report's contents (§2).
3. **Edit 4's spacing.** The dispatch puts the block after `population_summary`'s two following blank lines and ends it
   with one blank line, *"together with the existing blank line before the table-2 comment there are then two"* — but
   at that anchor no blank line remains before the comment, so the dispatch's text would leave one. Following its own
   instruction to *"follow the object's spacing and report it"*, the block stands with two blank lines on each side,
   the tool's convention between functions. The diff (§5) shows it.
4. **The shell-read guard denied one call**: a `grep` over a scratch file named through a shell variable, which the
   guard cannot expand and so denies by its standing policy. Nothing ran; the call was made again without the search,
   and the file read with the file tools.
5. **The first outputs of two scratch scripts run under `python -I`** printed an em dash in the console's legacy
   encoding (`-I` ignores `PYTHONIOENCODING`). The scripts were set to write UTF-8 and re-run on the same inputs; every
   verdict and value is unchanged, and the appendix holds the UTF-8 output.
6. **The read-only checks of 3(b) and 3(c) were re-run at the close tree** into files (A23, A25), the first runs having
   been read on the console only in part; every re-run exits 0 as the first run did.
7. **The appendix was written into the repository by a scratch Python script** (`assemble_appendix.py`, quoted at A30)
   from the saved printouts, so every printout is verbatim; this report proper was filled the same way from a template,
   so that no printed value is copied by hand.
8. **Shell use:** the repository's own tools, `git add`, `git commit` and `git push` ran with the repository as working
   directory; git object queries by explicit hash; `| head` and `| tail` only on command output; `cmp` over two scratch
   files; scratch scripts for the last-bytes check, the 3(c) diffs and the checks' re-runs (each hash inside them
   written literally or computed there). `git hash-object -w` left loose blob objects.

**Observations, not acted on.**

- **(a)** At 3(c) the per-session artifact's imported defense totals moved `share_of_the_whole_ordinary_session_start_read`
  (5.45 → 5.46, A26). 3(c)'s list names the denominator, not this share; the share is computed from that denominator, so
  it has no second cause.
- **(b)** The boot chain's three latest entries are 473, 472 and 476. Entries 472 to 475 share one add-commit time and
  the tool orders a shared time by name, so 474 and 475 fall outside the three although they landed with 472 and 473 —
  the shape the third and fourth reports met for their own shared times.
- **(c)** The arc's own appendix count is zero (`the_arc_reports` → `the_appendices_beside_them` → `count` 0): the arc's
  reports predate Ruling 4. Ruling 4's share has a value now only through the folder-wide pairs, as the premise ledger
  states.
- **(d)** The fourth report's observation (a) stands unchanged (table 2 still classes the decision-surface block as
  carrying a former wording) — carried, not acted on, as the dispatch's closing list names.

## 11. The appendix

`records/cc/reports/cc_report_per_session_reading_extension_2026_11_02_appendix.md`, **195,762 bytes**. It holds thirty
printout sections, verbatim, each under a heading naming its command and step (A1–A30): A1's enumeration whole; the
last-bytes script and output; the evidence-pin check; **the opening capture whole**; the start-tip summary comparison;
the classification STOP; the capture-comparison script; the boot-pack check before and after the edit; **the capture
after Task 1 whole** and its comparison; the unextended tool's writing run and check; **the tool diff**; the proofs'
script and output; the extended tool's writing run and timed check; **the 2(e) script and its every per-path record**;
**the capture after Task 2 whole** and its comparison; the 3(b) apply and the four archive checks; the 3(c) writing runs
and every 3(c) check; **the 3(c) diffs whole**; the re-run script; **the before-and-after script and its output**; the
assembler itself.

## 12. The ordered reads against the work, and the tell

**What took most:** `DECISIONS.md` whole and the protocol section, then the fourth dispatch, the fourth report and the
tool. **A summary of context did not fall.** **What the eight-line check saved, by my own account:** the six-span
file-tool read was replaced by eight single-line reads; `under_ruling_2_of_2026_11_01` is the measured total under that
change.

**The tell.** This batch produced nothing beyond the landed records, the edits A4 names (the boot-pack tool's one comment;
the measurement tool's edits 1 to 9 and its artifact), the regenerated artifacts, the Task 3 files (`STATUS.md`,
`STATUS_ARCHIVE.md`, the forward-bound tool and its artifact), this report and its appendix, the away-returns section,
the end state's guard artifact — and, outside the repository, scratch files and loose blob objects from `git hash-object
-w`.

## 13. The self-check

Re-read at the diffs of every touched file. **Principles:** #6 — the extension imports nothing twice and reuses the
tool's own `read`, `population_rows` and `Stop`; #12 — the comment's former wording kept at its site, every former
constant value named in the forward-bound tool's comments, `generated_for`'s former value in §5; #13/#3 — no unpredicted
result met in a build act; #14 — no behavior change of the analysis; #15/#19 — every check at the objects, the extension
proved on planted cases and against the unextended tool both ways (additions and removals); #17(f)/D-431 — every value
here is a printout of a named tool or script, filled from the printout. **Conventions:** American spelling; no invented
labels; the musical words only in their musical sense in my wording (the code and its quoted identifiers excepted).
**File tools:** working-tree reads with the file tools; shell for git object queries by explicit hash, the sanctioned
tools and scratch scripts. **Uncertainty:** no difference between measured quantities is asserted or interpreted; the
tables state values only.
