# CC REPORT — THE L2 PACK BUILD, SECOND HALF (2026-09-27) — STOPPED AT §12(c)

> **STATUS: STOPPED AT §12(c), BEFORE §12(d). NOT COMMITTED BEYOND TASK 0. NOT PUSHED.**
> **CLOSED 2026-09-27 by `records/cc/instructions/cc_instruction_l2_pack_build_close_2026_09_27.md`** — §12(d), §12(e), §13(a) and §13(b) run under it; see §12 below.
> Dispatch: `records/cc/instructions/cc_instruction_l2_pack_build_second_half_2026_09_27.md`, pinned at
> blob `7d5267c5c60f6380dd87d151e0ebc4c4a2eec234` (326,577 bytes). Written by Claude Code on
> 2026-09-27. Every figure below is read out of the tool output, artifact or git object named beside it;
> the captures are in this session's scratchpad, outside the working tree, at
> `C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\4be43c84-f33e-4ed4-ba31-5011217eded4\scratchpad\`
> (referred to below as `scratchpad/`).

## ★★ THE HEADLINE, STATED FIRST

**Tasks 0 to 9 ran and every expected result appeared.** The L2 subject is built and rendered. The
render gives `l2` exactly `IN 111 / OUT 133 / UNPLACED 0`, all fifty-six extracts passed the tool's own
two-direction STOPs with their 280 cuts, 28 runs-to-end cuts and 101 removals, the six withheld
passages matched, and the three frozen subjects were proved unmoved record by record.

**The batch STOPPED at §12(c), because one expected result did not appear.** The dispatch states that
Ruling 8's first regeneration publishes `tools/audit/gen_withheld_family_reading.py` as a
pinned-evidence member **UNRESOLVED**, for the user to resolve. **It did not.** The regenerated
`tools/audit/evidence_pin_membership.json` carries the same seven members as before, `UNRESOLVED 0`,
and files the 2026-09-05 reading document under *"named in a ruling record but not generated"*
instead. **The cause is established at the two tool sources (§8 below) and is a detection limit of
`gen_evidence_pin_membership.py`, not a change in the record.** Neither tool may be edited by this batch
(B1), and whether the pin tool should see that generator is the user's question. Under the dispatch's
closing rule — *"If any expected result does not appear, stop at that task and report it. Do not
continue to the next one"* — and principle #13, §12(d), §12(e), §13 and the push were **not** run.

**What is on disk and uncommitted** is listed at §10. **What goes to the user** is the leak list (§7)
and the STOP (§8).

---

## 1. Task 0 — the start state, and the previous sittings' work committed

**0(a).** `git hash-object -w` of the dispatch: **`7d5267c5c60f6380dd87d151e0ebc4c4a2eec234`**;
`git cat-file -s` of it: **326,577** bytes.

**0(b).** Read with the file tools: `.git/refs/heads/master` = `9909492ff02b19e4163eaed73ce163e7c62f742c`;
`.git/refs/remotes/origin/master` = `9909492ff02b19e4163eaed73ce163e7c62f742c`. **Both agree with the
expected value.**

**0(c).** `python tools/audit/changed_paths.py` reported **462 changed path records** (captured whole at
`scratchpad/cp_open.txt`): 38 modified — the 36 extracts, `records/cc/reports/cc_report_decision_rules_close_2026_09_21.md`
and `tools/audit/claude_md_finer_archive.json` — and the untracked population. **Nothing was staged**
(every record's index column was blank or `??`). The last byte of every text file 0(d) and 0(e) commit
was read from its blob (`scratchpad/t0_sizes.py`, output `scratchpad/t0_sizes.txt`): every one ends in
`0a`, no trailing NUL in any last 16 bytes, and no final line breaks off mid-word.

**0(d) — COMMIT ONE.** The close report was reported **modified** (it was committed in `9909492ff0` and
then extended after the push by a 110-line closing note — the diff against `9909492ff0` by object hash
is additions only). Size by the content-addressed route: **37,351** — equal to the figure given. Last
non-empty line: *"Nothing else. Nothing is staged."* Staged alone; `changed_paths.py --staged` reported
exactly `M records/cc/reports/cc_report_decision_rules_close_2026_09_21.md`, one record.
**Commit one: `42cbfa676fe03c974fd7f98571c3ea15949b0355`.** `tools/audit/claude_md_finer_archive.json`
held back (B9).

**0(e) — COMMIT TWO.** Every size given by the dispatch was re-taken by `git hash-object -w --no-filters`
then `git cat-file -s` and **every one matched** — the dispatch, the cut list (71,991), the three
ruling records (20,158 / 26,012 / 31,519), handoff entries 226 to 250 (all twenty-five figures), and the
thirty-six extracts (all thirty-six figures). **Entry 251 exists: 6,001 bytes** (the dispatch states no
size for it). Every path the list names was reported by the enumeration and every path committed is
named in the list. `changed_paths.py --staged` reported **exactly 67 records** — 36 `M` (the extracts)
and 31 `A` — and nothing else. **Commit two: `a84e2375301973b48cb2a0cc5a0fb13e6ec41c24`**, 67 files.
`git ls-tree` of it carries the dispatch at **`7d5267c5c60f6380dd87d151e0ebc4c4a2eec234`** — the
pinned blob.

**0(f) — THE OPENING GUARD CAPTURE**, taken after both commits: `python tools/audit/gen_guard_state.py`,
captured at **`scratchpad/guard_open.txt`**. Result line:

```
79 guard(s) run, 14 failing, 4 not run, 19 historical record(s)
```

The fourteen FAIL verdicts: `gen_phase3_gate_partition.py --check`, `gen_filing_convention_application.py --check`,
`gen_l0_l1_outgoing_population.py --check`, `gen_artifact_inventory.py --check`,
`gen_artifact_inventory_surface.py --check`, `gen_test_construction_evidence.py --check`,
`gen_retirement_caller_check.py --check`, `decisions/apply_soft_discard.py --check`,
`decisions/apply_residue_discard.py --check`, `gen_evidence_pin_membership.py --check`,
`gen_epoch_write_path.py --check`, `gen_recognizer_establishment_sort.py --check`,
`decisions/gen_home_classification.py --check`, `decisions/gen_phase1p_delegation_bar.py --check`.
Every other run guard PASSED; the four NOT RUN and nineteen HISTORICAL are as the capture lists.
**As expected and found:** `gen_derivation_boot_pack.py --check` **PASS**.
`python tools/audit/gen_guard_classification.py` (run separately after it, `scratchpad/guardclass_open.txt`):

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
exit:2
```

**As expected (B8): carried, not chased.** The opening capture left `tools/audit/guard_state.json`
byte-unchanged (it is not in the enumeration at the stop).

## 2. Task 1 — the pack re-derives at the untouched tree (THE BASELINE)

**(a)** `python tools/audit/gen_derivation_boot_pack.py --check`, verbatim (`scratchpad/t1_check.txt`):

```
FROZEN SOURCES: 15 of 21 frozen pack file(s) would render at a different length from the sources as they stand today. NOT COMPARED; sets no exit code.
  - harmony-boundary/02_the_guiding_principles_and_the_conventions.md: the directory holds 59762 characters; today's sources would render 66702
  - harmony-boundary/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - harmony-boundary/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - harmony-boundary/05_the_ratified_design_intent.md: the directory holds 252572 characters; today's sources would render 252641
  - l0-l1/02_the_guiding_principles_and_the_conventions.md: the directory holds 61113 characters; today's sources would render 67476
  - l0-l1/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - l0-l1/04_the_dispatch_protocol.md: the directory holds 103431 characters; today's sources would render 108389
  - l0-l1/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
  - l0-l1/07_the_charter_the_layers_and_the_decisions.md: the directory holds 29031 characters; today's sources would render 33067
  - l0-l1/08_the_five_research_extracts.md: the directory holds 76722 characters; today's sources would render 99171
  - l0-l1/09_the_empirical_findings_ledger.md: the directory holds 50666 characters; today's sources would render 50963
  - scoring-model/02_the_guiding_principles_and_the_conventions.md: the directory holds 60536 characters; today's sources would render 67476
  - scoring-model/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - scoring-model/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - scoring-model/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
exit:0
```

**(b)** The line naming `l0-l1/08_the_five_research_extracts.md`:
`  - l0-l1/08_the_five_research_extracts.md: the directory holds 76722 characters; today's sources would render 99171`

**(c)** `git hash-object tools/audit/gen_derivation_boot_pack.py` = **`e01f7bf369f3797b109ffc8317bf04f5ba5ce64b`**;
`git hash-object tools/audit/derivation_boot_pack.json` = **`fafcda4b368a6606e8c5bb0281a15988bb1fd601`**.
Both equal their HEAD blobs, and both agree with `--no-filters`.

## 3. Task 2 — `_cut_spans` may declare `runs_to_end`: the four D-657 proofs

The function read exactly as §4(a) quotes it; the replacement of §4(b) and the one docstring sentence
were applied and nothing else.

1. `--check` printed **byte-identical** output to Task 1(a) (`cmp` of `scratchpad/t1_check.txt` and
   `scratchpad/t2_check.txt`: identical), exit 0.
2. The `l0-l1/08` line is therefore identical to Task 1(b).
3. `git hash-object tools/audit/derivation_boot_pack.json` = `fafcda4b368a6606e8c5bb0281a15988bb1fd601`
   — unchanged.
4. `git diff e01f7bf369f3797b109ffc8317bf04f5ba5ce64b 1b7ea9bebdca7cc40b7b2bd48733ab0d1914a471`,
   verbatim:

```diff
@@ -2983,7 +2983,12 @@ def _removal_spans(text: str, removals: list[dict], rel: str) -> list[dict]:
 
 
 def _cut_spans(text: str, cuts: list[dict], rel: str) -> list[dict]:
-    """The offsets of each authored section cut, located by what its HEADING contains."""
+    """The offsets of each authored section cut, located by what its HEADING contains.
+
+    A cut that declares `runs_to_end` may be the file's last section at its level, and runs to
+    the end of the text; an undeclared unterminated section is a STOP, and a declared one that is
+    terminated is a STOP too.
+    """
     lines = text.split("\n")
     starts, pos = [], 0
     for ln in lines:
@@ -2998,14 +3003,26 @@ def _cut_spans(text: str, cuts: list[dict], rel: str) -> list[dict]:
                        f"one")
         h = hits[0]
         nxt = next((j for j in range(h + 1, len(lines)) if lines[j].startswith(level)), None)
-        if nxt is None:
+        runs_to_end = bool(cut.get("runs_to_end", False))
+        if nxt is None and not runs_to_end:
             raise Stop(f"{rel}: the section {lines[h]!r} is not terminated by a further {level!r} "
-                       f"heading")
-        a, b = starts[h], starts[nxt]
-        spans.append({"kind": "cut", "heading": lines[h], "heading_contains": needle,
-                      "closes_before": lines[nxt], "why": cut["why"],
-                      "start": a, "end": b, "the_text_removed": text[a:b],
-                      "characters_removed": b - a})
+                       f"heading, and the cut does not declare runs_to_end")
+        if nxt is not None and runs_to_end:
+            raise Stop(f"{rel}: the section {lines[h]!r} declares runs_to_end, but a further "
+                       f"{level!r} heading follows it: {lines[nxt]!r}")
+        a = starts[h]
+        b = starts[nxt] if nxt is not None else len(text)
+        record = {"kind": "cut", "heading": lines[h], "heading_contains": needle,
+                  "closes_before": lines[nxt] if nxt is not None else "<the end of the text>",
+                  "why": cut["why"],
+                  "start": a, "end": b, "the_text_removed": text[a:b],
+                  "characters_removed": b - a}
+        if runs_to_end:
+            # Written into the record ONLY when declared, so that every cut authored before this
+            # key existed re-derives byte-identical (D-657: no member the defect's shape does not
+            # name may move).
+            record["runs_to_end"] = True
+        spans.append(record)
     return spans
```

Changes inside `_cut_spans` only. **All four proofs hold.** Tool blob after Task 2:
`1b7ea9bebdca7cc40b7b2bd48733ab0d1914a471`.

## 4. Tasks 3 and 5 — member (8), and members (7) and (9) as shared objects

**How the table entered the tool, so nothing was retyped.** The §5.1 literal and the §5.2 fifty-six
parts were taken **verbatim from the pinned dispatch blob** by `scratchpad/extract_52.py` (which reads
only `git cat-file -p 7d5267c5…`), and inserted by `scratchpad/apply_7.py`, which asserts every anchor
exactly once. Parsed back as a Python literal before insertion: **56 parts, 280 cuts, 28 `runs_to_end`
cuts in 28 distinct files, 101 removals, no part without a removal, 56 distinct sources** — the
dispatch's expected values. The one line of the §5.1 literal that is a placeholder comment
(`# ── §5.2 — the fifty-six parts, verbatim ──…`) was replaced by the parts rather than kept above them.

**The move of (7) and (9), proved exact rather than asserted** (`scratchpad/verify_move.py`, over the
Task-2 blob `1b7ea9be…` and the post-move blob `ceccb970…`): `CHARTER_MEMBER_7`'s 62 body lines and
`LEDGER_MEMBER_9`'s 16, re-indented by the 8 spaces the change in nesting takes, are **byte-identical**
to the original dict bodies; `l0-l1`'s member (8) (38 lines) is untouched; and every line of the file
before the moved region and after `EXTRAS` is identical. *Placement, as §7(b) orders it literally:* the
constants stand **immediately above** the `EXTRAS:` line, which puts them below the `EXTRAS` banner
comment that describes the extras table — recorded so a reader is not surprised by it.

**§7(e) THE PROOF.** `--check` output **byte-identical** to Task 1(a) (`scratchpad/t7_check.txt`),
exit 0; `derivation_boot_pack.json` still `fafcda4b368a6606e8c5bb0281a15988bb1fd601`. **Tool blob after
§7: `ceccb9708617a34ac100e0de9075cba4d3ca243c`.**

## 5. Task 6 — `WITHHELD["l2"]`

**§8(a).** `python tools/audit/gen_l2_withheld_documents.py --check`, verbatim:

```
the L2 withheld-document derivation re-derives
exit:0
```

`tools/audit/l2_withheld_documents.json` → `documents`: the twenty-one `document` values, in order,
**equal the §8(b) tuple name for name**; `counted` → `documents` reads **21**.

**§8(b)–(d)** inserted verbatim from the pinned blob by `scratchpad/apply_8.py` (30, 148 and 11 lines).
*A defect of my own script, recorded because it happened:* its first run STOPPED on its own assertion —
the anchor `    "l0-l1": {` also opens entries in `FROZEN` and `CRITERION` — **before writing anything**
(the tool blob was confirmed unchanged at `ceccb970…` before the second run); the anchor was narrowed to
the key lying between `WITHHELD:` and the framework comment. The `l2` entry sits after the `l0-l1`
entry's closing `},` and its blank line, and before the framework comment.

**§8(e)** — the first run in which `build_subject("l2")` executes, verbatim (`scratchpad/t8_check.txt`):
the `FROZEN SOURCES` block as in Task 1(a), line for line, then

```
STALE: the derivation boot pack does not re-derive
  - derivation_boot_pack.json does not re-derive
  - l2: the pack directory is missing
exit:1
```

**No `STOP:` line, exit 1, exactly the two expected STALE lines, `FROZEN SOURCES` identical.** So every
candidate against `VERDICTS["l2"]`, the six passages against member (2), and all fifty-six parts through
`filter_part` passed the tool's own STOPs. **Tool blob after §8: `8486b08d4d2d975fd583ccc54438e01fe88ff178`.**

## 6. Tasks 7 and 8 — limb B, and the verdict date

**§9(a)** — the extras block read exactly as quoted; replaced as §9(a) gives, the comment line above it
kept. **§9(b)** inserted between the record's close and `return record, files`. **§9(c)** output
**byte-identical to §8(e)** (`scratchpad/t9_check.txt`). **Tool blob: `a09fc71485763bc2aa1d0fcc623d038ff54c4650`.**

**§10(a)–(d)** — `VERDICT_DATE` below `DATE = "2026-08-22"`; the stamp in `build_subject` replaced
exactly; the head comment's `# THE DATE.` paragraph (c) and its heading run (c2) replaced, every line read
first and each first/last line found once; the two `the_STOPS` changes (d), each located line found once.
**§10(e)** output **byte-identical to §9(c)** (`scratchpad/t10_check.txt`). **Tool blob:
`9c3c78fcbd89dcf34f303881451610049cbdb6e9`** — the tool as it stands at the stop.

## 7. Task 9 — the render, the frozen subjects, and THE LEAK LIST

**§11(a) — the render**, verbatim (`scratchpad/t11_render.txt`):

```
wrote tools\audit\derivation_boot_pack.json
  harmony-boundary: design-intent 244 · candidates 75 · IN 16 / OUT 59 / UNPLACED 0
    withheld 33 (16 authored + 17 derived) · documents 1 · passages 2 · leaks 3
    rendered: 208 design-intent entries, 25 defect-type rows, 7 files
  l0-l1: design-intent 244 · candidates 0 · IN 0 / OUT 0 / UNPLACED 0
    withheld 0 (0 authored + 0 derived) · documents 0 · passages 0 · leaks 3
    rendered: 241 design-intent entries, 25 defect-type rows, 10 files
  l2: design-intent 244 · candidates 244 · IN 111 / OUT 133 / UNPLACED 0
    withheld 202 (111 authored + 91 derived) · documents 21 · passages 6 · leaks 0
    rendered: 42 design-intent entries, 25 defect-type rows, 10 files
  scoring-model: design-intent 244 · candidates 0 · IN 0 / OUT 0 / UNPLACED 0
    withheld 0 (0 authored + 0 derived) · documents 0 · passages 0 · leaks 3
    rendered: 241 design-intent entries, 25 defect-type rows, 7 files
exit:0
```

**The `l2` line reads `IN 111 / OUT 133 / UNPLACED 0`, as expected.** The other printed figures are
reported as printed; the dispatch expected none of them.

**§11(b)** `--check` (`scratchpad/t11_check.txt`): the `FROZEN SOURCES` block **identical to Task 1(a)**
(`cmp` of the first sixteen lines: identical), then `the derivation boot pack re-derives` and the three
`FROZEN — N file(s) at their recorded blobs` lines, **exit 0**. Manifest blob after the render:
`3fa7d30c67f63f3efd660dfd4f6c0e7dc3cf881a`.

**§11(c) — THE THREE FROZEN SUBJECTS DID NOT MOVE.** The script, outside the working tree, is
`scratchpad/t11c_compare.py`; it loads the manifest at Task 1(c)'s blob by `git cat-file -p fafcda4b…`
and the manifest on disk. Its output, verbatim (the `§` shows as `�` on the console only):

```
PASS  subjects['harmony-boundary'] equal
PASS  subjects['scoring-model'] equal
PASS  subjects['l0-l1'] equal
PASS  top-level keys the same set
top-level keys whose values differ: ['subjects', 'the_STOPS', 'the_pack_files_in_order', 'the_rulings_it_executes']
PASS  only the four named keys differ
PASS  the_rulings_it_executes = old + the four §8(d) strings
PASS  old STOP string present once
PASS  the_STOPS = old with §10(d)'s two changes
PASS  the_pack_files_in_order: new keys = old keys + ['l2']
PASS  the_pack_files_in_order: every old key's value equal
PASS  subjects: new keys = old keys + ['l2']
PASS  subjects: every old key's value equal
OVERALL: PASS
```

**§11(d) — member (8) at the manifest** (`scratchpad/t11def.py`, output `scratchpad/t11def.txt`):
**56 parts, 280 cuts, 28 `runs_to_end` cuts, 101 removals**; all 28 `runs_to_end` cuts close before
`<the end of the text>` and no other cut does; the parts are in §5.2's order; **per-file differences
from §5.2: none** (counts, cut needles and removal anchors compared per file). `filter_part`'s
two-direction verification **passed for all fifty-six** (no STOP at §8(e) or at the render).
*The opening and closing removals, read:* 56 openings and 28 closing-provenance removals. All 28
closings begin `---` and end `*`. 55 openings are whole blockquotes beginning `> `, ending at the
block's last line (the next character is not a further quote line). **The one that does not begin
`> ` is `granrothwilding-2013-…`**, the file §6.2(5) names as two plain paragraphs: read against the
file, it takes lines 3 to 14 exactly — the STATUS paragraph and the provenance paragraph, ending
`"PDF has 183 pages".*` — and leaves the `---` rule at line 16. **It fits its stated disposition.**

**§11(e) — `tools/audit/derivation_boot_pack/l2/`**: `00_READ_THIS_FIRST.md`,
`01_the_phase_definitions.md`, `02_the_guiding_principles_and_the_conventions.md`,
`03_the_writing_standards.md`, `04_the_dispatch_protocol.md`, `05_the_ratified_design_intent.md`,
`06_the_defect_type_catalog.md`, `07_the_charter_the_layers_and_the_decisions.md`,
`08_the_fifty_six_research_extracts.md`, `09_the_empirical_findings_ledger.md`. **The listing and
`the_pack_files_in_order` → `l2` agree.**

### ★ THE LEAK LIST (§11(f)) — written for the user. This batch decides none of it.

Everything below is read out of `tools/audit/derivation_boot_pack.json` as rendered, and out of the
rendered files in `tools/audit/derivation_boot_pack/l2/`. **Every line listed here IS in the pack as
rendered.** No session boots from this pack before you rule on it (D-655).

**1. How far the confirmed documents widened the withheld family — measured.** You confirmed 21
withheld documents. The tool then withholds, beyond the 111 identities the verdicts grade IN, every
design-intent entry whose own text names a withheld identity or a withheld document. **That added 91
entries** (`THE_WITHHELD_FAMILY.derived_cross_reference_additions.additions`), so **202 are withheld and
only 42 of the 244 design-intent entries reach the pack.** The largest single cause is that
`ARCHITECTURE.md` is one of the 21 documents, and many entries name it in their rationale or status
source. The 91, with the field and string that pulled each in (`rationale`/`status_source`/`verbatim`
: matched string):

- D-002 — The fitted tables and weights are compiled into the binary verbatim — rationale:ARCHITECTURE.md; status_source:ARCHITECTURE.md
- D-028 — The span typology - every layer names the span it operates on; bare 'region' is banned — rationale:ARCHITECTURE.md; status_source:ARCHITECTURE.md
- D-029 — The verifiability contract — rationale:ARCHITECTURE.md; status_source:ARCHITECTURE.md
- D-030 — Bounded context - cost scales with the working span, not the whole score — rationale:ARCHITECTURE.md; status_source:ARCHITECTURE.md
- D-031 — Whole-score analysis is the degenerate case, not the design — rationale:ARCHITECTURE.md
- D-034 — A new layer or axis is admitted only through three co-equal gates — rationale:ARCHITECTURE.md; status_source:ARCHITECTURE.md
- D-035 — The effort setting - every cost-driving choice is a setting, never a hardcoded constant — rationale:ARCHITECTURE.md; status_source:ARCHITECTURE.md
- D-072 — The dependency rule - the analysis library knows nothing about the score format — status_source:ARCHITECTURE.md
- D-095 — The dual path during the joint-estimator build is a declared, bounded, pre-ratified migration state — status_source:ARCHITECTURE.md
- D-131 — One shared style taxonomy, not two parallel vocabularies — status_source:ARCHITECTURE.md
- D-132 — The remaining empirical grounding is the per-preset WEIGHTS alone; the clusters half is delivered by the ratified five-idiom set — status_source:ARCHITECTURE.md
- D-190 — The decision-neutrality corollary - what exists carries no weight in choosing a design — status_source:cowork_notation_adoption_increment.md
- D-202 — The effort control is one setting with several dials, and it must bound the time taken — status_source:ARCHITECTURE.md
- D-206 — Intonation is held as a future feature, and is a declared future consumer of the analysis — status_source:ARCHITECTURE.md
- D-223 — A gate that judges the pre-correction winner reads a snapshot, not the live result — status_source:docs/scoring_model.md
- D-229 — The MuseScore-dependency rule - one general rule for what our code may depend on — rationale:ARCHITECTURE.md; status_source:ARCHITECTURE.md
- D-260 — Analysis output covers exactly the selection; everything loaded beyond it is evidence, never a result — status_source:ARCHITECTURE.md
- D-261 — A layer never guesses how much context it needs - the amount is discovered by convergence — rationale:D-622; status_source:D-622
- D-265 — Asking a lower layer for more notes is a data-supply call, not a backward inference edge — status_source:D-025
- D-268 — A confidence attaches to a named decision, is compared only within its class and a declared frame, and keeps its identity downstream — status_source:ARCHITECTURE.md
- D-275 — Every published record carries its own instrument provenance; a provenance-less analysis cannot exist — status_source:cowork_notation_output_contract.md
- D-279 — The Stage-3 entry gate - seven conditions before any engagement wiring reaches production — rationale:cowork_engage_arc_plan.md; status_source:cowork_engage_arc_plan.md
- D-282 — Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy — status_source:cowork_architecture_reassessment.md
- D-286 — Whole-score interactive analysis was SHELVED WITH EVIDENCE; the bounded window is the ratified reading — status_source:ARCHITECTURE.md
- D-295 — Zero information loss to the end user - every inferred object must be displayable — rationale:D-099; status_source:ARCHITECTURE.md
- D-296 — READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits — status_source:ARCHITECTURE.md
- D-322 — Any change to optimization flags or to the order of the scoring arithmetic requires a full corpus A/B on both presets — status_source:docs/scoring_model.md
- D-324 — Retirement of a post-scoring rule is global — a rule still doing work on any one preset is retained for all — status_source:docs/scoring_model.md
- D-352 — The key/mode grading bar splits the cases first … — rationale:cowork_layer3_keymode_design.md; status_source:cowork_layer3_keymode_design.md
- D-353 — The key/mode layer is graded on two goals kept apart … — status_source:cowork_layer3_keymode_design.md
- D-388, D-389, D-390, D-392, D-393, D-394, D-395, D-396 — the voice-leading axis entries — status_source:cowork_voiceleading_axis_design.md
- D-397, D-398, D-400 — status_source:ARCHITECTURE.md; status_source:cowork_voiceleading_axis_design.md
- D-406 — The catalog owns the NAMED progressions … — verbatim:cowork_progression_schema_design.md; status_source:D-341; status_source:ARCHITECTURE.md; status_source:cowork_progression_schema_design.md
- D-421 — Idiom re-discovery rides every corpus wave … — status_source:ARCHITECTURE.md
- D-423 — The gate-retirement stage is the only sanctioned way the post-scoring gates change … — status_source:docs/scoring_model.md
- D-440, D-441, D-443, D-444, D-445, D-448 — the language-model integration entries — status_source:ARCHITECTURE.md
- D-451, D-452 — the desk-simulation entries — status_source:cowork_factorization_desk_simulation.md
- D-469, D-470, D-471, D-472, D-474, D-475, D-476, D-477, D-478, D-479, D-480, D-481, D-482, D-484, D-485, D-498 — status_source:D-501
- D-495, D-496, D-500 — status_source:D-501; status_source:cowork_architecture_review_2026_07.md
- D-497 — status_source:D-501; status_source:ARCHITECTURE.md; status_source:cowork_architecture_review_2026_07.md
- D-502 — The span a recognised named progression covers is called the progression-schema-span … — status_source:ARCHITECTURE.md
- D-503 — The idiom mixture is DISCOVERED from the score … — status_source:D-293
- D-508 — The catalog/grammar consistency test ships scoped to the MEASURED containment … — status_source:D-341
- D-512 — Gate A becomes removable only once the unified promotion reproduces its carry byte-for-byte … — status_source:D-510; status_source:D-511; status_source:docs/scoring_model.md
- D-535 — The checking stage's verdict … — status_source:D-453
- D-569 — Collecting, filtering and weighting are THREE separate responsibilities … — status_source:ARCHITECTURE.md
- D-576 — The corpus root-agreement measurement UNDERSTATES … a wrong key … — status_source:D-575
- D-584 — The perfect/imperfect cadence call is made on the BASS-DERIVED inversion … — status_source:D-336
- D-587, D-588, D-589, D-590, D-591, D-598, D-625 — status_source:ARCHITECTURE.md
- D-601 — Before any constant that would make two differently-scaled confidences comparable is fitted … — status_source:D-600; status_source:ARCHITECTURE.md; status_source:cowork_engage_arc_plan.md; status_source:docs/scoring_model.md
- D-613 — Ground truth for IMPLIED polyphony is confirmed ABSENT … — status_source:D-291
- D-656 — The crediting rule is NOT amended … — verbatim:D-291; status_source:D-291
- D-665 — What a voice/stream label set actually MEASURES is said at intake … — status_source:D-291

*(Grouped rows share one reason and are listed together to keep this readable; the full per-entry title
and reason for every one of the 91 is in the manifest at the path above, and at
`scratchpad/t11def.txt` lines 30–120.)*

**2. Leaks in the generated members (5) and (6):** `LEAKS.entries` is **empty** — no withheld identity,
withheld document name, `ARCHITECTURE.md` or `docs/`/`src/` path in a rendered design-intent entry or
defect-type row.

**3. Limb B — lines of the quoted extras that carry a withheld string: 66 lines**
(`LEAKS_IN_THE_EXTRAS.entries`; `counted.extras_lines_with_a_leak_hit` = 66). **None in member (7).**
The lines, grouped by member, with their line number in the rendered file:

*Member (8), `08_the_fifty_six_research_extracts.md` — 54 lines.* Two kinds:

- **Withheld decision identities named in the extracts' own kept text (5 lines):** line 5014 (D-525 —
  *"specification beside D-525 and DP-P."*); line 8954 (D-526 — *"It takes **no** verdict on D-526,"*);
  line 8955 (D-532, D-533 — *"D-532, D-533, DP-E, R-5 or the L2 candidate-admission clause …"*);
  line 10137 (D-474 — *"It asserts no contradiction with D-474"*); line 10581 (D-474 — *"… principle
  #21's D-474 block already refuses as a …"*).
- **`docs/` paths (49 lines):** the held-paper file paths (`**File:** docs/research_papers/<paper>.pdf`
  — lines 12, 217, 420, 596, 1027, 1655, 1888, 2273, 2548, 6688, 9258) and references to
  `docs/research_papers/BIBLIOGRAPHY.md` or its folder (lines 399, 598, 1004, 1022, 1211, 1228, 1393,
  1414, 1630, 1648, 1859, 2248, 2514, 2536, 2855, 3168, 4531, 4755, 5071, 5341, 6405, 6660, 6702,
  6828, 7145, 7369, 7648, 7895, 7916, 8291, 8980, 9141, 9268, 9477, 9630, 9837, 10014, 10032). These
  are what the leak check's `docs/…` string rule catches; many sit in `## Identity` bibliography
  comparisons that §6.4 names as not reached by the removals, or in kept sections' provenance-like
  sentences.

*Member (9), `09_the_empirical_findings_ledger.md` — 12 lines.* `docs/scoring_model.md` (a withheld
document, and a `docs/` path) at lines 94, 145, 156, 217, 318, 644; withheld identities D-490 and
D-491 (lines 166, 167), D-575 (351), D-474 (568, 572), D-190 (602). *(Member (9) enters "whole and
unfiltered" by Ruling 4 — so these can be struck only by a ruling that widens that member's filter.)*

Every one of the 66 lines is quoted whole in the manifest (`the_line`) and at `scratchpad/t11def.txt`
lines 127–259.

**4. Member (2)'s named residues, located in the rendered `l2/02_the_guiding_principles_and_the_conventions.md`**
— §8(f)'s reading, marked as a reading: each names the document as a pointer and carries no IN entry's
content.

- `cowork_evidence_inventory.md` — line 254 (the fact-publication corollary's amendment).
- `cowork_joint_estimator_architecture.md` — line 294 (the principles' provenance paragraph).
- `cowork_notation_adoption_increment.md` — lines 296 (provenance paragraph) and 677 (the decision-surface block, as D-424's home).
- `cowork_engage_arc_plan.md` — lines 298 (provenance paragraph) and 303 (the delegation-pointer paragraph).
- `docs/scoring_model.md` — line 433 (the phase-structure supersession note).
- `ARCHITECTURE.md` — lines 260, 322, 402, 413, 416, 582 — **six places, the by-design naming** the
  tool's own `LEAKS` scope note declares for this member (the three further `CLAUDE.md` lines §8(f)
  counted fall inside withheld passages (a) and (d) and are gone).
- The sentence *"an item that cannot touch what the model reads or how candidates are admitted"* —
  line 534, which restates in general words the two subjects passage (f) withholds.

**5. Member (8)'s title lines — the first line of each first-pass part, as rendered (all fifteen are in
the pack):** `CENTRAL` in eight (`mcleod-rohrmeier-2021`, `dehaas-…-2013`, `mcleod-rohrmeier-2024`,
`sapp-2005`, `viaccoz-…-2023`, `humphrey-bello-2015`, `hentschel-…-2021`, `hamanaka-…-2013`);
`CENTRAL-adjacent` in one (`lazzari-2023`); `not central` in five (`bachi-2026`, `hu-arthur-2021`,
`napoleslopez-…-2020`, `eerola-schutz-2025`, `navarrocaceres-…-2024-2025`); none in
`feisthauer-2021`. This matches §6.2(7) exactly. Each title line is quoted at `scratchpad/t11def.txt`
lines 286–315.

**6. The bound on the handoff archive's name, as §8(f) states it:** *"the confirmed name
`records/cowork/handoff/cowork_handoff_archive.md` is matched by `leaks_in` and
`cross_reference_additions` as that whole string, so a text naming the archive by its file name alone is
not caught by it."*

## 8. Task 10 — as far as it ran, and ★ THE STOP

**12(a) — the `STATUS.md` entry.** Ruling 9's "ELEVEN FAILING" entry: **absent from `STATUS.md`** —
found at `STATUS_ARCHIVE.md` line 5633 — so nothing was done about it. The entry written, quoted whole:

> *Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_pack_build_second_half_2026_09_27.md`. **★★ THE L2 SUBJECT IS ADDED TO THE DERIVATION BOOT PACK AND ITS PACK IS RENDERED**, under Rulings 1 to 6 of `records/cowork/rulings/cowork_rulings_2026_09_05_l2_boot_list_sitting.md`, the withheld family of `records/cowork/rulings/cowork_rulings_2026_09_05_l2_withheld_family_sitting.md`, the withheld documents the user confirmed whole on 2026-09-21, and Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_21_l2_extracts_member_cutting_sitting.md` — the withheld table with its two prose fields, its confirmed documents and its six passages of member (2); the extracts member over the fifty-six files with their authored per-file cuts and removals; and the charter and ledger members as ONE shared object each with `l0-l1` rather than a copy (#6). ★ **THE THREE FROZEN SUBJECTS WERE PROVED UNMOVED**, record by record against the manifest at its pre-batch blob, and nothing under their directories was written. ★ **THE SECTION-CUT FILTER MAY NOW DECLARE THAT A CUT RUNS TO THE END OF THE TEXT**, the NARROW amendment — an undeclared unterminated section and a declared terminated one both still STOP — proved under **D-657** before any member was added: every existing subject re-derived byte-identical. ★ **THE VERDICT DATE IS MADE PER SUBJECT**, so the L2 verdicts carry the date they were ruled rather than the pilot's. ★ **LIMB B's LEAK CHECK NOW RUNS OVER THE RENDERED EXTRAS** of every subject that is not frozen, LISTING its hits rather than stopping on them. ★ **RULING 8's TWO NAMED REGENERATIONS WERE RUN.** ★★ **WHAT THIS BATCH DID NOT DO: no session was booted, no brief written, no score staged, and THE LEAK LIST WAS NOT ACTED ON — it goes to the user, who rules on it before any session boots from this pack (D-655)**, together with the pinned-evidence members the regeneration published. No open-items row created, flipped or discarded; no decisions-register identity allocated and no `D-NNN` created; no extract edited; no tool source edited but the boot-pack generator and the forward bound's authored aiming; no `src/` file, build, test, golden, score corpus or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md` — and no figure is restated here (**D-431**).)*

**★ ONE CHANGE TO AN EXISTING LINE, DECLARED.** The consolidation batch's entry lost its leading
`Last updated: ` prefix when this entry was written above it. It is not an editorial rewrite. It is
`gen_status_batch_bound.py`'s own declared `PREFIX_ADJUSTMENT`: `moved_entries()` strips that prefix from
the base-commit text and requires the stripped form in the live file exactly once. The previous batch
declared the same act (its report §6.1), and `STATUS_ARCHIVE.md` at `9909492ff0` carries its moved
entry in the stripped form. **My first `--apply` STOPPED on exactly this** — verbatim: `STOP: the entry
at base line 8 occurs 0 time(s) in the live STATUS.md — the file has changed under the act and the move
is not byte-faithful` (exit 2; `--check` then FAIL) — **because I had written the new entry without
moving the prefix. Nothing was written by that run**; the prefix was moved and `--apply` re-run. The
entry it touched has since moved to the archive whole, so no rewritten sentence remains in `STATUS.md`.
*Caveat on the entry itself:* written before 12(c) ran, it says Ruling 8's regenerations "were run" —
true — and speaks of "the pinned-evidence members the regeneration published", which the STOP below
qualifies. It was not re-edited, 12(a) being the last write to `STATUS.md`.

**12(b) — the forward bound.** `tools/audit/gen_status_batch_bound.py` re-aimed at its authored inputs,
their comments and one appended `PREVIOUS_AIMINGS` row, and nowhere else. The diff, by explicit blobs
`98ce226641a00cc79c44eb03c27eb6d050498c67` → `3a5ae0ed27e95f1926f0fb777e9b25e274e1b6dc`, is at
`scratchpad/bound_diff.txt`. It sets `BASE_COMMIT` = `a84e2375301973b48cb2a0cc5a0fb13e6ec41c24`
(commit two), `PREVIOUS_BATCH_DISPATCH` =
`cc_instruction_decision_rules_consolidation_2026_09_21.md`, `DISPATCH` =
`cc_instruction_l2_pack_build_second_half_2026_09_27.md`, `TASK` = `Task 10`, `ACT_DATE` =
`2026-09-27`, `MOVE_KIND` `ordinary` and `RULINGS` unchanged, with every former value named in its
comment. Established before relying on it: `STATUS.md` at commit two is blob
`af9eb2a6e6fa7843c88ed38597ff9e246634c6a5`, the same as at `9909492ff0`. The comment's claim that
the consolidation batch's close wrote no entry of its own was checked at that commit's `STATUS.md`
diff: its one changed line is the consolidation entry itself.

`--apply` (second run), verbatim:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 3,545 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
exit:0
```

`--check`: the same three lines, exit 0. **The entry actually moved, by name:** the consolidation
batch's entry, `*2026-09-21 (CC — \`records/cc/instructions/cc_instruction_decision_rules_consolidation_2026_09_21.md\`. **★★ THE DECISION-SURFACE RULES ARE CONSOLIDATE…`
(base line 8, membership "names the dispatch", the declared adjustment applied). **The two 2026-09-02
entries did not move** and were not moved by hand. (A green `--check` is not read as proof the bound is
met, `OPEN_ITEMS.md` OI-379; the moved entry is named above.)

**12(c) — Ruling 8's two regenerations**, all four outputs verbatim:

```
$ python tools/audit/gen_evidence_pin_membership.py
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 97
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
exit:0

$ python tools/audit/gen_evidence_pin_membership.py --check
the evidence pin's class membership re-derives
  (the same six further lines)
exit:0

$ python tools/audit/gen_l0_l1_outgoing_population.py
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
exit:0

$ python tools/audit/gen_l0_l1_outgoing_population.py --check
l0_l1_outgoing_population.json re-derives
exit:0
```

**The pinned-evidence members, compared against the blob at commit two** (`fb3a00be268401e5386954cc3c410c9c827539df`
→ `92f4522642d88f1ef754c1cdb3843c17d0749e7b`, diff at `scratchpad/t12c_pin_diff.txt`): **no member
added, none removed, none changed in state.** The same seven generators, five pinned and two not pinned,
and zero unresolved. What moved: `ruling_records_read` 85 → 97 (twelve ruling records landed since, the
2026-09-05 to 2026-09-21 ones); every record name now carries its `records/cowork/rulings/` path; and
**two documents joined the list of documents *named in a ruling record but not generated***:
`cowork_pruning_and_satellites_surface_2026_09_08.md` (from the 2026-09-08 defense-satellite sitting)
and **`cowork_withheld_family_l2_reading.md` (from the 2026-09-05 L2 withheld-family sitting)**.

**`l0_l1_outgoing_population.json`** (`ae7de9f679cd15d6f446985961ff2d8278743f9b` →
`e310fb57ac53f9a06f8a9295d70c17ec143e3ce3`, diff at `scratchpad/t12c_pop_diff.txt`): the changes are
line-number shifts in `CLAUDE.md`'s hit records, from the 2026-09-21 insertion, plus one added
recorded `repeat` hit there, and report paths rewritten to `records/cc/reports/…` in other governing
documents' hit lines. **None comes from this batch's `STATUS.md` entry.** This guard was already FAIL at
the opening capture, for these inherited reasons.

### ★ THE STOP — the expected UNRESOLVED member did not appear

**What the dispatch expected (§12(c)):** *"Ruling 8 … orders both regenerated here, **the first publishing
the 2026-09-05 withheld-family record's surface generator (`tools/audit/gen_withheld_family_reading.py`)
as a pinned-evidence member UNRESOLVED**, for the user to resolve at that artifact."* It relies on §5 of
`records/cc/reports/cc_report_l2_ruling_writeback_2026_09_05.md`, which predicted that the ruling
record, once landed, would make that generator a member and publish it UNRESOLVED.

**What happened:** the regeneration **read** that ruling record and found the document it names. It
classified the document as **not generated**, so no member was created.

**The cause, established at the two tool sources:**

- `gen_evidence_pin_membership.py` recognises a generated document ONLY by a **module-level constant**
  that joins `ROOT`/`REPO` with `"ratification_surfaces"` and a `.md` name (its regex `NAMES_SURFACE`),
  **and** a write through that same constant (`writes_it`). Its docstring: *"taken by scanning the tools
  for a module-level assignment composing that directory with a `.md` filename."*
- `gen_withheld_family_reading.py` declares its target as a **dictionary value** inside a per-subject
  table — line 50: `"out": "ratification_surfaces/cowork_withheld_family_l2_reading.md",` — and writes
  it with `open(out, "w", …)` at line 468. That shape is outside the pin tool's pattern, so the document
  never enters the generated-document map (still 7), and Route A cannot make its generator a member.

So the 2026-09-05 prediction was right about the **fact** — that tool does write the document — and
wrong about what the pin tool **detects**. That is a detection limit of the pin derivation: a generated
ratification document it cannot see is silently classed as hand-written, and its generator is left out
of the pinned class (#19 — the membership is complete only relative to what the pattern recognises).

**Why this is a STOP and not a report-and-carry-on:** §12(c)'s own carry-on clause covers a tool that
STOPs, and neither tool did. The expected publication is the thing that puts the question to you, and it
is missing, so the question does not reach you through the artifact. The dispatch's closing rule and
principle #13 both say stop. **Resolving it would mean editing either tool, which B1 forbids** (and B8
reserves `gen_withheld_family_reading.py` to its own act). **Nothing was edited to make it appear.**

**What remains undone because of the STOP:** §12(d) (the two read-size generators), §12(e) (the closing
guard capture and its verdict-by-verdict comparison), §13(a) (the batch commit), §13(b) (the push).
*Expected movement at the closing capture, stated as a prediction and not a measurement:*
`gen_evidence_pin_membership.py --check` and `gen_l0_l1_outgoing_population.py --check`, both FAIL at
the opening, now pass when run directly (FAIL → PASS, which is allowed). The read-size guards have not
been run since `STATUS.md` changed.

## 9. The commits and the push

- Commit one: **`42cbfa676fe03c974fd7f98571c3ea15949b0355`** — the previous batch's close report.
- Commit two: **`a84e2375301973b48cb2a0cc5a0fb13e6ec41c24`** — the 67 interim carriers.
- **No batch commit. No push.** `master` is two commits ahead of `origin/master`
  (`9909492ff02b19e4163eaed73ce163e7c62f742c`). Pushing is left to the close of this batch.

## 10. The working tree at the stop

`python tools/audit/changed_paths.py` at the stop (`scratchpad/cp_stop.txt`, 403 records). Modified:
`STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/derivation_boot_pack.json`,
`tools/audit/evidence_pin_membership.json`, `tools/audit/gen_derivation_boot_pack.py`,
`tools/audit/gen_status_batch_bound.py`, `tools/audit/l0_l1_outgoing_population.json`,
`tools/audit/status_batch_bound.json` — and the held-back `tools/audit/claude_md_finer_archive.json`
(B9, untouched). New: `tools/audit/derivation_boot_pack/l2/` (ten files) and this report. The rest is
the standing untracked population, unchanged. **All of it lies inside the footprint assumption.**
**Nothing is staged. Nothing under `tools/audit/derivation_boot_pack/harmony-boundary/`, `…/scoring-model/`
or `…/l0-l1/` changed.** `tools/audit/guard_state.json` is unchanged. Current blobs: boot-pack tool
`9c3c78fcbd89dcf34f303881451610049cbdb6e9`; manifest `3fa7d30c67f63f3efd660dfd4f6c0e7dc3cf881a`;
`STATUS.md` `2c8ace0d624cbe9fcb902b4aabcba9eb542f2809`; `STATUS_ARCHIVE.md`
`160ece0f9274a0669bd2a52ec601a0cb08a4df78` (four lines appended — the forward-bound header and the moved
entry); `status_batch_bound.json` `a29df6799a5962747c8980e16e69994ea229c842`.

## 11. What was NOT done

- No tool source edited other than `tools/audit/gen_derivation_boot_pack.py` and the authored aiming
  inputs of `tools/audit/gen_status_batch_bound.py` (B1). `gen_evidence_pin_membership.py` and
  `gen_withheld_family_reading.py` were read, not edited.
- No extract edited, and nothing under `reading_pass/` was written (B2).
- Nothing was written under the three frozen pack directories (B3).
- No governing document other than `STATUS.md` was amended (B7).
- No session booted, no brief written, no score staged. The leak list was not acted on.
- No open-items row created, flipped or discarded. No `D-NNN` created, and no register identity
  allocated (B5).
- No `src/` file, build, test, golden, score corpus, `tools/corpus/`, `tools/robust_stop/`,
  measurement of the analysis, or paper (B4).
- `tools/audit/claude_md_finer_archive.json` held back (B9). `gen_guard_classification.py`'s STOP
  carried, not chased (B8).
- §12(d), §12(e), §13 and the push not run — **the STOP**.

**What goes to the user:** the leak list (§7), the pinned-evidence comparison (no member added, removed
or changed) and **the STOP (§8)**, whose question is whether the pin tool should recognise a generator
that declares its target in a table rather than a module constant — a question about a measurement tool,
which this batch may not answer by editing it.

---

*Provenance: Claude Code, 2026-09-27. Dispatch pinned at `7d5267c5c60f6380dd87d151e0ebc4c4a2eec234`.
Every figure is cited to the tool output, artifact or git object it was read from; the captures and the
helper scripts are in this session's scratchpad, outside the working tree, and are named in place.*

---

## 12. The close, resumed under cc_instruction_l2_pack_build_close_2026_09_27.md

*Written by Claude Code on 2026-09-27, in a new session. The pinned dispatch's §12(d), §12(e) and §13
were read from its blob `7d5267c5c60f6380dd87d151e0ebc4c4a2eec234` (`git cat-file -p`, saved to this
session's scratchpad). This session's captures are at
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\d4dc3f6a-ab87-4f9a-91a8-99465bd89307\scratchpad\`
(called `scratchpad2/` below); the stopped session's `scratchpad/` is the one named at the head of this
report. **Every expected result of R0 to R5 appeared; no STOP.** No tool source was edited.*

### 12.1 R0 — the start state

1. Read with the file tools: `.git/refs/heads/master` = `a84e2375301973b48cb2a0cc5a0fb13e6ec41c24`;
   `.git/refs/remotes/origin/master` = `9909492ff02b19e4163eaed73ce163e7c62f742c`. **Both as expected.**
2. `python tools/audit/changed_paths.py` (exit 0, `scratchpad2/cp_r0.txt`, 406 records). **Nothing
   staged.** Modified tracked paths, exactly: `STATUS.md`, `STATUS_ARCHIVE.md`,
   `tools/audit/claude_md_finer_archive.json` (held back), `tools/audit/derivation_boot_pack.json`,
   `tools/audit/evidence_pin_membership.json`, `tools/audit/gen_derivation_boot_pack.py`,
   `tools/audit/gen_status_batch_bound.py`, `tools/audit/l0_l1_outgoing_population.json`,
   `tools/audit/status_batch_bound.json`. `tools/audit/derivation_boot_pack/l2/` is reported as one
   untracked directory; its listing by the file tools is the ten files of §7 (§11(e)). A `diff` of this
   enumeration against the stop's (`scratchpad/cp_stop.txt`) shows only three added records —
   `records/cc/instructions/cc_instruction_l2_pack_build_close_2026_09_27.md`,
   `records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md` (written after the stop's
   capture) and `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_two.md` — and the
   count line. **As expected.**
3. `git hash-object`, all seven equal to §10: boot-pack tool `9c3c78fcbd89dcf34f303881451610049cbdb6e9`;
   manifest `3fa7d30c67f63f3efd660dfd4f6c0e7dc3cf881a`; `STATUS.md`
   `2c8ace0d624cbe9fcb902b4aabcba9eb542f2809`; `STATUS_ARCHIVE.md`
   `160ece0f9274a0669bd2a52ec601a0cb08a4df78`; `tools/audit/status_batch_bound.json`
   `a29df6799a5962747c8980e16e69994ea229c842`; `tools/audit/evidence_pin_membership.json`
   `92f4522642d88f1ef754c1cdb3843c17d0749e7b`; `tools/audit/l0_l1_outgoing_population.json`
   `e310fb57ac53f9a06f8a9295d70c17ec143e3ce3`. **No mismatch.**
4. `python tools/audit/gen_derivation_boot_pack.py --check`, exit 0 (`scratchpad2/r0_check.txt`): the
   same sixteen-line `FROZEN SOURCES` block as Task 1(a), then

```
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
```

### 12.2 R1 — the one correction to this batch's own `STATUS.md` entry

The string `together with the pinned-evidence members the regeneration published.` occurred **exactly
once** in `STATUS.md` (line 8, this batch's own entry), and was replaced by the dispatch's text,
verbatim. `STATUS.md` `2c8ace0d624cbe9fcb902b4aabcba9eb542f2809` → `d390a3103918b039489e1a5b08484d7cd18bc302`;
`git diff --word-diff=porcelain` of the two blobs shows that phrase as the only change. **This was the
last write to `STATUS.md` in this batch.**

### 12.3 R2 — the two regenerations re-checked after R1

```
$ python tools/audit/gen_l0_l1_outgoing_population.py --check
l0_l1_outgoing_population.json re-derives
exit:0
```

It re-derived, so it was **not** regenerated. Then:

```
$ python tools/audit/gen_evidence_pin_membership.py --check
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 97
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
exit:0
```

No `STOP:` line, no traceback. Both artifacts stand at their R0 blobs.

### 12.4 R3 — the pinned dispatch's §12(d)

```
$ python tools/audit/gen_session_start_read_size.py
wrote tools/audit/session_start_read_size.json
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              39804
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 168350, the six session-start spans 104609, overstated by 63741
    CLAUDE.md                                                                104609
    STATUS.md                                                                 11984
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 247146
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 247146 [ruled membership]  (-119975, -32.68%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 247146 [ruled membership]  (-49686, -16.74%)  <- CROSSES A REGIME BOUNDARY
exit:0

$ python tools/audit/gen_defense_share.py
wrote tools/audit/defense_share.json
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   39804  ( 8.72%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (104609): 12.39%
    of the whole session-start read (247146): 5.24%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
exit:0

$ python tools/audit/gen_session_start_read_size.py --check
the session-start read measurement re-derives
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              39804
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 168350, the six session-start spans 104609, overstated by 63741
    CLAUDE.md                                                                104609
    STATUS.md                                                                 11984
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 247146
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 247146 [ruled membership]  (-119975, -32.68%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 247146 [ruled membership]  (-49686, -16.74%)  <- CROSSES A REGIME BOUNDARY
exit:0

$ python tools/audit/gen_defense_share.py --check
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   39804  ( 8.72%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (104609): 12.39%
    of the whole session-start read (247146): 5.24%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
exit:0
```

**Both `--check` runs exit 0. No `STOP:` line, no traceback.** Neither tool was edited.

### 12.5 R4 — the closing guard capture, verdict by verdict

The opening capture was found at the stopped session's `scratchpad/guard_open.txt` (not reconstructed).
`python tools/audit/gen_guard_state.py`, captured at `scratchpad2/guard_close.txt`, exit 0; its result line:

```
79 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

A line-by-line `diff` of the two captures — the same guards, in the same order — returns exactly:

```
27c27
<   [FAIL] tools/audit/gen_l0_l1_outgoing_population.py --check
---
>   [PASS] tools/audit/gen_l0_l1_outgoing_population.py --check
59c59
<   [FAIL] tools/audit/gen_evidence_pin_membership.py --check
---
>   [PASS] tools/audit/gen_evidence_pin_membership.py --check
104c104
< 79 guard(s) run, 14 failing, 4 not run, 19 historical record(s)
---
> 79 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

**The guards that moved:** `gen_l0_l1_outgoing_population.py --check` **FAIL → PASS** and
`gen_evidence_pin_membership.py --check` **FAIL → PASS** — both allowed, and both as §8 predicted.
**No guard that was PASS at the opening carries any other verdict now.** Every other verdict,
including the twelve remaining FAILs, the four NOT RUN and the nineteen HISTORICAL, is identical.

`python tools/audit/gen_guard_classification.py`, as expected (B8), carried and not chased:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
exit:2
```

It is identical to the opening's (`scratchpad/guardclass_open.txt`).

### 12.6 R5 — the batch commit

`python tools/audit/changed_paths.py` after R4 (`scratchpad2/cp_r5.txt`, 409 records), compared by `diff`
with R0's: three records were added, all modified tracked paths — `tools/audit/defense_share.json` and
`tools/audit/session_start_read_size.json` (R3), and **`tools/audit/guard_state.json`, the one guard-set
artifact the enumeration reports as modified** (written by R4's capture). Nothing else moved.

**The candidate set, as the close dispatch's R5 restates it:** `tools/audit/gen_derivation_boot_pack.py`;
`tools/audit/derivation_boot_pack.json`; the ten `tools/audit/derivation_boot_pack/l2/` files, each by
its own path; `STATUS.md`; `STATUS_ARCHIVE.md`; `tools/audit/gen_status_batch_bound.py`;
`tools/audit/status_batch_bound.json`; `tools/audit/evidence_pin_membership.json`;
`tools/audit/l0_l1_outgoing_population.json`; `tools/audit/session_start_read_size.json`;
`tools/audit/defense_share.json`; this report; the close dispatch; and, from the guard set,
`tools/audit/guard_state.json` — **23 paths.**

**Held back and confirmed absent from the staged set:** `tools/audit/claude_md_finer_archive.json` (B9);
`records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_two.md` (it lands at the next batch's
Task 0); and every other path the enumeration reports — the standing untracked population.

**The staged set, proved.** All 23 paths were staged by one `git add --` naming each path (no directory
pathspec). `python tools/audit/changed_paths.py --staged`, verbatim, exit 0:

```
M	STATUS.md
M	STATUS_ARCHIVE.md
A	records/cc/instructions/cc_instruction_l2_pack_build_close_2026_09_27.md
A	records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md
M	tools/audit/defense_share.json
M	tools/audit/derivation_boot_pack.json
A	tools/audit/derivation_boot_pack/l2/00_READ_THIS_FIRST.md
A	tools/audit/derivation_boot_pack/l2/01_the_phase_definitions.md
A	tools/audit/derivation_boot_pack/l2/02_the_guiding_principles_and_the_conventions.md
A	tools/audit/derivation_boot_pack/l2/03_the_writing_standards.md
A	tools/audit/derivation_boot_pack/l2/04_the_dispatch_protocol.md
A	tools/audit/derivation_boot_pack/l2/05_the_ratified_design_intent.md
A	tools/audit/derivation_boot_pack/l2/06_the_defect_type_catalog.md
A	tools/audit/derivation_boot_pack/l2/07_the_charter_the_layers_and_the_decisions.md
A	tools/audit/derivation_boot_pack/l2/08_the_fifty_six_research_extracts.md
A	tools/audit/derivation_boot_pack/l2/09_the_empirical_findings_ledger.md
M	tools/audit/evidence_pin_membership.json
M	tools/audit/gen_derivation_boot_pack.py
M	tools/audit/gen_status_batch_bound.py
M	tools/audit/guard_state.json
M	tools/audit/l0_l1_outgoing_population.json
M	tools/audit/session_start_read_size.json
M	tools/audit/status_batch_bound.json
23 changed path record(s) [staged]
```

**It is exactly the candidate set: every candidate staged, nothing else.** Nothing under
`tools/audit/derivation_boot_pack/harmony-boundary/`, `…/scoring-model/` or `…/l0-l1/` is staged (B3).
`tools/audit/claude_md_finer_archive.json` and entry 252 are **absent** from the staged set. This report
was staged, then this paragraph was written, and then the report was staged again. The listing was
re-run after that second staging, and it must be identical before the commit is made (§12.7 records it).

### 12.7 The commit and the push — written AFTER the commit, and not inside it

*A report cannot carry the hash of the commit that contains it. Everything above this subsection is in
the batch commit. This subsection was appended after that commit and the push, so it is additions only,
it is uncommitted, and it lands at the next batch's Task 0. That is the shape this batch's own commit
one used for the previous close report (§1, 0(d)).*

- The re-run of `changed_paths.py --staged` after the report's second staging was **identical to the
  listing in §12.6**: 23 records (`scratchpad2/staged2.txt`). The worktree enumeration just before the
  commit (`scratchpad2/cp_precommit.txt`) showed every one of the 23 as staged with a clean worktree
  column. The only other tracked modification was ` M tools/audit/claude_md_finer_archive.json`, which
  is held back.
- **The batch commit: `84ab3a5c404bf9953a568df7c0c57022dba06f8f`**, parent
  `a84e2375301973b48cb2a0cc5a0fb13e6ec41c24` (commit two). `git show --stat` of it: `23 files changed`,
  the 23 paths of §12.6 and no other.
- **Push:** `git push origin master` (no `--force`), verbatim:

```
To https://github.com/slimvince/MuseScore
   9909492ff0..84ab3a5c40  master -> master
exit:0
```

- **The pushed branch: `master`**. The push carried three commits: `42cbfa676f` and `a84e237530` (the two
  Task 0 commits) and `84ab3a5c40`. `upstream` was not used.
- **`origin/master` after the push**, read with the file tools at `.git/refs/remotes/origin/master`:
  `84ab3a5c404bf9953a568df7c0c57022dba06f8f`. **It equals `master`** (`.git/refs/heads/master`, read the
  same way).

### 12.8 What the close did NOT do

- **No tool source was edited** — not `gen_derivation_boot_pack.py`, not `gen_status_batch_bound.py`, not
  `gen_evidence_pin_membership.py`, not `gen_withheld_family_reading.py`, not any other. The tool edits
  the stopped batch made were committed as they stood at R0's blobs.
- No extract was edited, and nothing was written under the three frozen pack directories.
- No governing document was amended except `STATUS.md`, at R1's one phrase.
- No session was booted, no brief was written and no score was staged. The leak list was not acted on.
- No open-items row was created, flipped or discarded. No `D-NNN` was created and no register identity
  was allocated.
- No `src/` file, build, test, golden, score corpus or measurement of the analysis was touched.
- `gen_l0_l1_outgoing_population.py` was not regenerated at R2, because it re-derived.
- `tools/audit/claude_md_finer_archive.json` and handoff entry 252 were held back.
  `gen_guard_classification.py`'s STOP was carried, not chased.

### 12.9 What goes to the user

1. **The leak list**, §7 above, unchanged by the close.
2. **The pin tool's blind spot.** The first problem is that `tools/audit/gen_evidence_pin_membership.py`
   recognises a generated ratification document only when two things hold:
   - a module-level constant composes `ratification_surfaces` with a `.md` name;
   - the file is written through that constant.

   A generator that declares its output in a table does not meet that shape, and neither does one that
   writes through a local variable. `tools/audit/gen_withheld_family_reading.py` does both, so the tool
   does not see it.

   The consequence is that its document (`cowork_withheld_family_l2_reading.md`) is filed as *"named in
   a ruling record but not generated"*, and its generator is **not** a pinned-evidence member, resolved
   or unresolved. The membership is therefore complete only relative to the pattern the tool
   recognises. This is reported, not repaired (D-436), and whether the tool should see such a generator
   is the user's question.
3. **The STOP** at §12(c) of the stopped batch (§8). The close dispatch resolved it by no longer
   expecting the member. **No new STOP arose in R0 to R5.**
