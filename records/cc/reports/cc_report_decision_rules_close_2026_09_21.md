# CC REPORT — THE CLOSE OF THE DECISION-RULES BATCH: THE THREE STALED ARTIFACTS RE-DERIVED, NO RULED VERDICT MOVED, COMMITTED AND PUSHED (2026-09-21)

**Dispatch:** `records/cc/instructions/cc_instruction_decision_rules_close_2026_09_21.md`,
pinned at `3cfbfdf43f124add50b1d2b4975c7f05d4262d82`.

**★★ THE HEADLINE, STATED FIRST.** Every task ran and every expected result appeared. The three
guards that stood red at the opening capture — `claude_md_rule_triage.py --check`,
`gen_rulings_sort.py --check` and `decisions/gen_reads5_repack.py --check` — moved **FAIL → PASS**,
**no guard that was PASS at the opening capture carries any other verdict at the closing one**, and
**no entry's class moved in the user-ruled rulings sort**. The dispatch's correction to the previous
report is **CONFIRMED at the tool source**: `claude_md_rule_triage.py` opens exactly two files and
neither is `CLAUDE.md`. The batch this one closes left nineteen tracked paths plus its two untracked
records, and the enumeration found **exactly** those and nothing else.

**★ ONE THING THE PREVIOUS REPORT RECORDS THAT DID NOT REPRODUCE, ESTABLISHED RATHER THAN PASSED
OVER.** The backbone's blob hash on disk is **not** the post-edit hash that report's §5.4 names. The
cause was established at the git objects, not assumed: that hash is the state **before** the same
batch's §5.5 anchor re-aim, and the two blobs differ by exactly 41 lines, **every one of them a
`"home"` field**. §3.2 carries the proof. Nothing here is a STOP; the backbone is in the state the
previous batch left it in, which is what 1(b) tests and what it reports.

---

## 1. Task 0 — the start state

### 1.1 The pin (0(a))

```
git hash-object -w records/cc/instructions/cc_instruction_decision_rules_close_2026_09_21.md
3cfbfdf43f124add50b1d2b4975c7f05d4262d82
```

### 1.2 The two refs, read at the ref FILES with the file tools (0(b), D-253)

| Ref file | Value found | Barred value | Held |
|---|---|---|---|
| `.git/refs/heads/master` | `6b5bdfc38145befd865feab9436e6ff0dc32cea0` | same | ✅ |
| `.git/refs/remotes/origin/master` | `ef4fad940d806edf8f84eb9a895f88d70a9bbcf2` | same | ✅ |

**They disagree, which is the state the dispatch was written knowing.** Neither has moved since the
previous batch left them. Both were read at the loose ref files with the Read tool; neither was taken
from `git rev-parse`.

### 1.3 The working tree (0(c))

`python tools/audit/changed_paths.py` reported **416 changed path records**. The enumeration is
outside the working tree at `scratchpad/wt_0c.txt` (this session's scratchpad); no path list beyond
the tracked records below is restated here (**D-431**).

**NOTHING IS STAGED.** Every tracked record carries the code ` M` — a space in the index column — and
every other record carries `??`.

**THE TWENTY TRACKED RECORDS FOUND, compared member by member against the previous batch's §7 list:**

```
 M CLAUDE.md
 M DECISIONS.md
 M STATUS.md
 M STATUS_ARCHIVE.md
 M cowork_audit_protocol.md
 M decisions/group_C.md
 M decisions/group_D.md
 M decisions/group_G.md
 M decisions/group_K.md
 M decisions/group_L.md
 M decisions/group_Q.md
 M decisions/group_S.md
 M decisions/group_T.md
 M tools/audit/claude_md_finer_archive.json      (HELD BACK by B7)
 M tools/audit/decisions/backbone_decisions.json
 M tools/audit/defense_share.json
 M tools/audit/gen_status_batch_bound.py
 M tools/audit/guard_state.json
 M tools/audit/session_start_read_size.json
 M tools/audit/status_batch_bound.json
```

**THE COMPARISON CLOSES IN BOTH DIRECTIONS WITH NO DIFFERENCE.** Every path that report named is
here; no path is here that it did not name. The count reconciles with the dispatch's own warning
about that report's internal disagreement: its prose says nineteen and its block lists twenty,
`claude_md_finer_archive.json` being in the block and outside the count — and twenty is what the tree
carries.

**The untracked side, accounted for whole so that nothing is left unexplained:** 396 records, being
`scratch_artifacts/` **387**, the six standing entries (`Claude outputs/`, `Codex research
inventory/`, `docs/research_papers/polyph9-release/`, the two PDFs under `external resarch summary/`,
and the untracked `.mscx` under `tools/audit/derivation_exemplars/l0-l1/`), and **three** under
`records/cc/` — the previous batch's two, plus **this dispatch**, which is this batch's own and is
the only addition. 20 + 396 = 416, which is the whole enumeration.

**A route substitution, declared.** The grouping of the untracked records by prefix was first
attempted with a Python one-liner; **the shell-read guard refused it** (D-253, the 2026-08-08
interpreter-code widening) because the code string carried a repository path literal. The counts
above were taken with **Grep over the enumeration file** instead. This is the guard working, and the
sanctioned route was used rather than worked around.

### 1.4 The corruption check (0(d))

**All twenty-six text files this batch will commit were checked, and every one ends in ordinary
text.** No trailing NUL byte; no final line broken off mid-word. Each file's length was taken with
Grep and its tail read **with the Read tool** — every JSON ends on its closing `}`, the one Python
source on a complete statement, and every Markdown file on a complete sentence or its generated-by
line.

The twenty-six: `CLAUDE.md` · `DECISIONS.md` · `STATUS.md` · `STATUS_ARCHIVE.md` ·
`cowork_audit_protocol.md` · the eight `decisions/group_*.md` · the rulings-sort ratification surface
· `backbone_decisions.json` · `reads5_repack.json` · `gen_status_batch_bound.py` ·
`status_batch_bound.json` · `session_start_read_size.json` · `defense_share.json` ·
`guard_state.json` · `claude_md_rule_triage.json` · `rulings_sort_classification.json` · the two
dispatches · the previous batch's report.

**No binary was read, and nothing in the held-back untracked population was read**, exactly as 0(c)
directs. The twenty-seventh committed file is this report, which did not exist when the check ran.

### 1.5 The opening guard capture (0(e))

**Path: `scratchpad/guard_open.txt`, outside the working tree.** Result line:

```
79 guard(s) run, 17 failing, 4 not run, 19 historical record(s)
```

**EVERY EXPECTATION WAS MET, AND EACH IS REPORTED AS FOUND RATHER THAN ASSUMED:**

| Guard | Expected | Found |
|---|---|---|
| `tools/audit/claude_md_rule_triage.py --check` | FAIL | **FAIL** |
| `tools/audit/gen_rulings_sort.py --check` | FAIL | **FAIL** |
| `tools/audit/decisions/gen_reads5_repack.py --check` | FAIL | **FAIL** |
| `tools/audit/decisions/gen_cluster_dispositions.py --verify` | PASS | **PASS** |

The failing set is the same seventeen the previous batch's closing capture named, which is what makes
this capture the continuation of that one rather than a fresh state. The other fourteen failures are
inherited debt and are named at §6.2, where they are carried.

---

## 2. Task 1(a) — the three tools' inputs, read at their own sources

### 2.1 `tools/audit/claude_md_rule_triage.py` — **THE CORRECTION IS CONFIRMED AT THE OBJECT**

**It opens exactly two files, and NEITHER is `CLAUDE.md`.**

| Line | What it opens |
|---|---|
| 42 | `BACKBONE = os.path.join(HERE, "decisions", "backbone_decisions.json")` |
| 43 | `OUT = os.path.join(HERE, "claude_md_rule_triage.json")` |
| 646 | `b = json.loads(open(BACKBONE, encoding="utf-8").read())` |
| 753 | `have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""` |
| 759 | `open(OUT, "w", encoding="utf-8", newline="").write(text)` |

Every other occurrence of the string `CLAUDE.md` in that file is a docstring, a comment, or authored
prose inside a verdict. The one that could be mistaken for a read is **line 648**:

```python
rules = [e for e in b["decisions"]
         if e["home"].split(":")[0].replace("\\", "/") == "CLAUDE.md"]
```

— which compares a **register entry's `home` FIELD** against that string. It is a filter over the
backbone, not a file read. **So the previous report's §6.4 attribution of this guard's move to Task
2's `CLAUDE.md` insertion is wrong**, and the dispatch's correction stands.

**AND THE ACTUAL CAUSE IS ESTABLISHED IN THE SAME READING, not merely asserted by elimination.** Line
**685** builds each output row as `{"id": …, "title": …, "home": e["home"], …}` — the row carries the
backbone's `home` anchor **verbatim**. The previous batch's Task 4 re-aimed 41 `home` anchors, 35 of
them on entries homed in `CLAUDE.md`, so every one of those rows changed and the committed artifact
stopped re-deriving. The staling act was the **backbone edit**, exactly as the dispatch says.

### 2.2 `tools/audit/gen_rulings_sort.py` — confirmed as the dispatch states

| Line | Constant |
|---|---|
| 110 | `BACKBONE = ROOT / "tools" / "audit" / "decisions" / "backbone_decisions.json"` |
| 114 | `OUT = ROOT / "tools" / "audit" / "rulings_sort_classification.json"` |
| 115–116 | `SURFACE = (ROOT / "ratification_surfaces" / "cowork_rulings_sort_surface_2026_08_16.md")` |

**`main()` writes BOTH on a bare run, and there is no mode that writes one without the other:** line
**934** `OUT.write_text(...)`, line **936** `SURFACE.write_text(...)`, both unconditional after the
`--check` branch returns at line 932. The `--check` branch reads both (924, 927) and fails on either.

*Reported because it is read and not asked for: the tool has four further inputs it reads and never
writes — `FILTER` (109), `RULING` (111), `PHASES` (112–113) and `SORT_RULING` (118). None was touched
by the previous batch, which is why the backbone is the whole cause.*

### 2.3 `tools/audit/decisions/gen_reads5_repack.py` — confirmed as the dispatch states

| Line | Constant |
|---|---|
| 94 | `BACKBONE = os.path.join(HERE, "backbone_decisions.json")` |
| 95 | `OUT = os.path.join(HERE, "reads5_repack.json")` |

It loads the backbone at line 145 and writes `OUT` at line 385. *Also read and never written:
`REGIME` (line 93, `phase1n_reading_regime.json`), untouched by the previous batch.*

---

## 3. Task 1(b) — the backbone is final and has not moved

### 3.1 Its identity, by the content-addressed route

```
git hash-object -w --no-filters tools/audit/decisions/backbone_decisions.json
73e243773bbe1ec1a2b130b2440bce947adc4a01

git cat-file -s 73e243773bbe1ec1a2b130b2440bce947adc4a01
2753303
```

**`git hash-object -w` WITHOUT `--no-filters` returns the same hash**, so no line-ending filter is in
play and the two routes agree.

### 3.2 ★ WHY THAT IS NOT THE HASH THE PREVIOUS REPORT NAMES — ESTABLISHED, NOT ASSUMED

That report's §5.4 names `dcfee15e86e1f3ea7d7cce6a321f6aa9f035b7a1` as the post-edit blob. The tree
carries `73e2437…`. **The difference is the anchor re-aim that report's own §5.5 records as
happening afterwards**, and it was proved at the git objects rather than argued:

```
git diff --numstat dcfee15e86e1f3ea7d7cce6a321f6aa9f035b7a1 73e243773bbe1ec1a2b130b2440bce947adc4a01
41      41
```

and of the 82 changed lines (41 removed, 41 added), **82 match `^[+-] *"home"`** — that is, **every
single one is a `"home"` field and nothing else differs**. `dcfee15e…` is the state after the D-658
field edit and **before** the 41-anchor re-aim; `73e2437…` is the state the previous batch left. The
discrepancy is fully accounted for and is not a STOP.

### 3.3 The drift check

```
python tools/audit/decisions/reaim_home_anchors.py --check
anchors drifted: 0                                                      [exit 0]
```

**`anchors drifted: 0`, and `REFUSED` was NOT printed.** Both conditions hold: the backbone is in the
state the previous batch left it in, and it is in the serialization that tool requires.

---

## 4. Task 1(c) and 2(a) — THE VERDICT PROOF

### 4.1 The baseline, taken before anything was re-derived

**The field the class is read from is `proposed_class`**, one per entry in the artifact's `entries`
array. The totals are at `the_distribution`.

| | Baseline, from `the_distribution` | Baseline, counted at the per-entry `proposed_class` |
|---|---|---|
| `DESIGN-INTENT` | 244 | 244 |
| `IMPLEMENTATION-MANAGEMENT` | 167 | 167 |
| `NEEDS-THE-USER` | 0 | 0 |

The two agree, which is itself a cross-check: the published totals are the per-entry verdicts counted,
not a separately authored figure. **411 entries.**

**★ AND THE BASELINE WAS PRESERVED WHOLE, NOT TRANSCRIBED (#12, D-431).** Before the run, the file
was written into the git object store by the content-addressed route, so the complete per-entry
baseline survives the regeneration instead of being reduced to the three numbers above:

| Artifact | Pre-run blob |
|---|---|
| `tools/audit/rulings_sort_classification.json` | `13e67ece02c0c63c532ee7f1fe37ebecfc1ba0cc` |
| `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md` | `04b899222d0ffdb58f35a7fc6d43725b4fa610c4` |
| `tools/audit/claude_md_rule_triage.json` | `813e7e7a432f3bab83290fcf1bba47605afb816c` |
| `tools/audit/decisions/reads5_repack.json` | `a0548d76038a4be574d30dc943cf4bba24a46a2e` |

This makes 2(a)'s comparison an **entry-by-entry byte comparison of the whole file**, rather than a
comparison of the values a session happened to write down.

### 4.2 The three bare runs, in the ordered sequence — all exit 0

```
python tools/audit/claude_md_rule_triage.py                                          [exit 0]
wrote tools\audit\claude_md_rule_triage.json: 87 rules
  MECHANISM-EXISTS: 32
  MECHANISABLE-AND-NOT: 9
  KNOWLEDGE: 46
  the defect set (9): D-113, D-187, D-193, D-194, D-230, D-253, D-308, D-486, D-546

python tools/audit/decisions/gen_reads5_repack.py                                    [exit 0]
remaining owed: 27 documents / 87346 est tokens; terciles still owed: medium, short
  wave 5: 14 docs, 45418 tok, terciles {'medium': 5, 'short': 9}
  wave 6: 13 docs, 41928 tok, terciles {'medium': 5, 'short': 8}
ordering key flips if the regime is regenerated: True (document_length_lines -> named_in_a_user_ratified_surface_count)

python tools/audit/gen_rulings_sort.py                                               [exit 0]
wrote tools\audit\rulings_sort_classification.json
wrote ratification_surfaces\cowork_rulings_sort_surface_2026_08_16.md
  DESIGN-INTENT: 244
  IMPLEMENTATION-MANAGEMENT: 167
  NEEDS-THE-USER: 0
```

*The middle tool prints no `wrote` line; that is its own bare-run behaviour — it writes `OUT` at line
385 and prints the remainder summary instead. Confirmed at the source rather than inferred from the
absence.*

### 4.3 ★★ NO ENTRY'S CLASS MOVED, AND THE TOTALS DID NOT MOVE

**Regenerated totals: `DESIGN-INTENT` 244 · `IMPLEMENTATION-MANAGEMENT` 167 · `NEEDS-THE-USER` 0 —
identical to the baseline in every cell.**

The entry-by-entry proof, against the preserved pre-run blob:

```
new blob: 21b2adb8cb73f1a852ee323e54220618ab247688
git diff --numstat 13e67ece… 21b2adb8…   →   78  78
```

**Seventy-eight lines changed, and every one of them is one of four fields.** Measured over the diff
itself, not read off by eye:

| Pattern searched in the diff | Matches |
|---|---|
| `^[+-].*(proposed_class\|decided_by\|DESIGN-INTENT\|IMPLEMENTATION-MANAGEMENT\|NEEDS-THE-USER\|the_distribution)` | **0** |
| `^[+-] *"(home\|the_home_it_names\|title\|what_the_entry_says_the_decision_is_quoted_from_the_register)"` | **156** (= 78 removed + 78 added) |

**So: not one `proposed_class` line changed, not one `decided_by` line changed, and not one line of
`the_distribution` changed — while every changed line is accounted for.** The 78 are the re-aimed
`home` anchors and their `the_home_it_names` echoes, plus **two prose fields on D-658 alone** — its
`title` and its quoted restatement, which is exactly the rendered-text change the dispatch predicted.

**This is the condition on the whole batch and it HOLDS.** The expected diff was rendered text only,
D-658's among it, with every verdict standing — and that is what the objects show.

---

## 5. Task 2(b) — what the surface's diff actually contains

```
new blob: 7344d7e624005c913f137d179bb085f101b2aed8
git diff --numstat 04b89922… 7344d7e6…   →   4  4
```

**FOUR LINES, in three hunks, and nothing else in the file moved.** Named:

| Where | What moved |
|---|---|
| D-576's entry | `**Recorded at:** CLAUDE.md:826-830` → `CLAUDE.md:865-869` |
| D-656's entry | `**Recorded at:** CLAUDE.md:1044-1053` → `CLAUDE.md:1083-1092` |
| D-660's entry | `**Recorded at:** CLAUDE.md:1561-1572` → `CLAUDE.md:1616-1627` |
| the standing-rules list | **D-658's rendered title**, replaced by the corrected one |

Three re-aimed anchors and one corrected title. **Every one of the four lines keeps its
*decided by* clause unchanged** — D-658 still *the decisions register's own `nonspec_kind`*, the other
three still *the authored word recognizers* — so no verdict moved on the surface either.

**THE BANNER, THE THREE RULING PARAGRAPHS AND THE TOTALS ARE UNCHANGED.** This is proved twice: they
lie outside all three diff hunks, so at byte level they did not move; and the banner was read at the
file afterwards and still opens **`STATUS: RULED, 2026-08-17. NOTHING IS EXECUTED BY IT.`**, with the
three numbered ruling paragraphs and the *A MANAGEMENT PLACEMENT REMOVES NOTHING* block standing
exactly as before. **No STOP condition fired.**

---

## 6. Task 2(c) and 2(d) — the three checks and the closing capture

### 6.1 The three checks — all exit 0

```
python tools/audit/claude_md_rule_triage.py --check        →  the CLAUDE.md rule triage re-derives   [exit 0]
python tools/audit/decisions/gen_reads5_repack.py --check  →  reads5_repack.json re-derives          [exit 0]
python tools/audit/gen_rulings_sort.py --check             →  the rulings sort re-derives            [exit 0]
```

The third prints the single re-derives line, which means **both** its artifacts matched: its check
fails separately on `OUT` and on `SURFACE`, and the clean line is printed only when neither drifted.

### 6.2 The closing guard capture (2(d))

**Path: `scratchpad/guard_close.txt`, outside the working tree.** Result line:

```
79 guard(s) run, 14 failing, 4 not run, 19 historical record(s)
```

**COMPARED VERDICT BY VERDICT IN BOTH DIRECTIONS, MECHANICALLY.** The two captures were diffed
against each other rather than read side by side, and the entire difference is:

```
12c12   [FAIL] → [PASS]  tools/audit/claude_md_rule_triage.py --check
37c37   [FAIL] → [PASS]  tools/audit/gen_rulings_sort.py --check
72c72   [FAIL] → [PASS]  tools/audit/decisions/gen_reads5_repack.py --check
104c104 79 guard(s) run, 17 failing → 14 failing, 4 not run, 19 historical record(s)
```

**THE CONDITION HOLDS ON BOTH LIMBS.** The three named guards moved FAIL → PASS. **No guard that was
PASS at 0(e) carries any other verdict** — not one line outside those four differs, the NOT-RUN set
is the same four tools and the HISTORICAL set the same nineteen. No condition was written on any
printed output or on any count inside a guard, and none was read.

**THE FOURTEEN GUARDS STILL RED ARE CARRIED AND NOT CHASED**, every one of them red at 0(e) for a
reason unrelated to this batch: `gen_phase3_gate_partition.py` · `gen_filing_convention_application.py`
· `gen_l0_l1_outgoing_population.py` · `gen_artifact_inventory.py` · `gen_artifact_inventory_surface.py`
· `gen_test_construction_evidence.py` · `gen_retirement_caller_check.py` ·
`decisions/apply_soft_discard.py` · `decisions/apply_residue_discard.py` ·
`gen_evidence_pin_membership.py` · `gen_epoch_write_path.py` · `gen_recognizer_establishment_sort.py`
· `decisions/gen_home_classification.py` · `decisions/gen_phase1p_delegation_bar.py` — each `--check`.
**Nothing here repairs any of them.**

### 6.3 The guard classification, run in its own order and CARRIED

```
python tools/audit/gen_guard_classification.py --check                                    [exit 2]
STOP: tool(s) in the guard-state population with no authored verdict:
['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py',
 'tools/audit/gen_withheld_family_reading.py']
```

**Exactly the three tools the dispatch predicted**, two of them older debt. Reported whole and
carried on, as ordered. It is not a STOP for this batch and it is not repaired here.

---

## 7. Task 3(a) — the candidate set, and the proof that items 1 to 11 are unchanged

### 7.1 The enumeration after the runs

`python tools/audit/changed_paths.py` now reports **420 changed path records** — four more than at
0(c), and **exactly the four this batch's own orders modify**:

```
 M ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md
 M tools/audit/claude_md_rule_triage.json
 M tools/audit/decisions/reads5_repack.json
 M tools/audit/rulings_sort_classification.json
```

**THE FOOTPRINT ASSUMPTION HELD EXACTLY.** Those four plus `tools/audit/guard_state.json` — already
modified at 0(c) and written again by both captures — are the whole of what this batch moved, and
this report is the one file it creates. **`tools/audit/changed_paths_establishment.json` is NOT
modified**: the guard set invokes `changed_paths.py --establish` on every run and its output was
byte-identical, so it appears in no enumeration. That is the same outcome the previous batch measured
and it is reported because the footprint assumption is the dispatch's while the measurement is this
side's.

### 7.2 ★ ITEMS 1 TO 11, PROVED UNCHANGED RATHER THAN ASSERTED

**Item 3, `backbone_decisions.json`, is proved byte-identical outright**: re-hashed after every run
of this batch, it is still `73e243773bbe1ec1a2b130b2440bce947adc4a01` — the same blob §3.1 recorded
before Task 2 ran. **B3 holds at the object.**

**The other ten are proved two ways, neither of them a memory of not having edited them.**

*(a) Their landing points were read at the objects and match the previous report's own record of
where it left them:*

| Item | What the previous report records | Found now |
|---|---|---|
| `CLAUDE.md` | file length 1986 | **1986** |
| `cowork_audit_protocol.md` | 1605 lines; heading at 1306; THE FORM's fourth requirement at 1316–1317; the standing-clause note at 1304 | **all four, read in place** |
| `DECISIONS.md` | index 861 lines; D-658's corrected row at line 823 | **both** |
| `decisions/group_T.md` | D-658's entry at 1469–1492 | **heading at 1469** |
| `STATUS.md` | three dated entries, at lines 8, 10 and 12 | **exactly three, at 8, 10 and 12** |
| `STATUS_ARCHIVE.md` | forward-bound header at 5721, moved entry at 5723 | **both** |

*(b) Six guards re-derive from precisely these files and are GREEN at the closing capture, so a
change to any of them would have shown as a verdict move — and §6.2 proves no verdict moved but the
three intended ones:*

- `decisions/gen_decisions_register.py --check` — `DECISIONS.md` and every `decisions/group_*.md`
  match the backbone exactly (items 4 and 5).
- `decisions/gen_cluster_dispositions.py --verify` — all 477 verbatim quotes found at their cited
  homes with their cited line numbers correct, which is a byte-level statement about `CLAUDE.md` and
  `cowork_audit_protocol.md` at every cited anchor (items 1, 2, 3).
- `decisions/reaim_home_anchors.py --check` — zero anchor drift over the same two documents.
- `gen_status_batch_bound.py --check` — the moved entry byte-present in the archive exactly once and
  absent from the must-read (items 6, 7, 8, 9).
- `gen_session_start_read_size.py --check` — re-derives from `CLAUDE.md`, `STATUS.md` and
  `DECISIONS.md` as they now stand (items 1, 4, 6, 10).
- `gen_defense_share.py --check` — re-derives through that same reader (item 11).

**No item differs. Nothing here is a STOP.**

**Item 12, `tools/audit/guard_state.json`, IS moved by this batch** — the two guard captures at 0(e)
and 2(d) each write it, which the footprint assumption names — and it is committed as this batch
changed it, not as unchanged.

### 7.3 The candidate set as it stands

Twenty-seven paths: items 1 to 4 and 6 to 20 of §3(a), the eight `decisions/group_*.md` the
enumeration reports as modified (**C, D, G, K, L, Q, S, T** — named rather than assumed), and this
report. **Item 21 is EMPTY**: the enumeration reports no further modified guard artifact. The only
other modified tracked path is `tools/audit/claude_md_finer_archive.json`, which B7 holds back.

---

## 8. What this batch did NOT do — named rather than counted

- **NO TOOL SOURCE WAS EDITED, AT ALL** (B1). Not one. Every tool named in this report was RUN.
- **NO GOVERNING DOCUMENT WAS AMENDED** (B2): not `CLAUDE.md`, `cowork_audit_protocol.md`,
  `STATUS.md`, `STATUS_ARCHIVE.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `FRAMEWORK.md` or
  `OPEN_ITEMS.md`. The previous batch's edits to them went in unchanged, proved at §7.2.
- **`tools/audit/decisions/backbone_decisions.json` WAS NOT EDITED** (B3) — proved by the identical
  blob hash before and after every run.
- **NO REGISTER REGENERATION** (B4). `gen_decisions_register.py` and `gen_cluster_dispositions.py`
  ran only inside the guard set, in their check and verify modes. Neither was run bare.
- **`tools/audit/gen_derivation_boot_pack.py` WAS NOT EDITED AND WAS NEVER RUN BARE** (B5): it ran
  only inside the guard set, in `--check`, in both captures. **Nothing was authored into `WITHHELD`,
  `EXTRAS`, `VERDICTS`, `CRITERION` or `FROZEN`, and no path under
  `tools/audit/derivation_boot_pack/` was read for content, written, deleted, renamed or moved.**
- **`tools/audit/gen_withheld_family_reading.py` WAS NEITHER EDITED NOR RUN** (B6). The live finding
  the previous batch reported at its lines 146–147 — the superseded no-recommendation clause asserted
  by D-658's own identity into a generated reading surface — **stands with the user and is NOT
  repaired here.** *(The guard set runs that tool's own `--subject l2 --check`, which is the guard
  set's invocation and not this batch's; it is `[PASS]` in both captures.)*
- **`tools/audit/claude_md_finer_archive.json` WAS HELD BACK** (B7): not staged, not reverted, not
  investigated.
- **NO OPEN-ITEMS ROW was created, flipped or discarded, and NO `D-NNN` was allocated** (B8). The
  register's rule (c) suspension and its owed-entries list are left exactly as they stand.
- **No `src/` file, no build, no test, no golden, no score corpus, nothing under `tools/corpus/` or
  `tools/robust_stop/`, no measurement of the analysis, no paper, no reading-pass extract, no score**
  (B9).
- **No figure from the dispatch was transcribed into any artifact** (B10). The four figures it
  states — the two ref hashes and the two commit hashes — are start-state bars, and none of them is
  written anywhere by this batch.
- **No new file was created under `tools/`**, and no helper script was written anywhere.

---

## 9. WHAT GOES TO THE USER

1. **NO VERDICT MOVED IN THE RULED SORT.** The user ruled that sort on 2026-08-17. Every one of the
   411 entries carries the same class it carried before, and the totals are unchanged in every cell —
   proved by a whole-file byte comparison against a preserved pre-run snapshot, in which **not one
   `proposed_class` line and not one line of `the_distribution` appears**. The surface moved by four
   lines: three stale line anchors and D-658's corrected title. Its **STATUS banner and its three
   ruling paragraphs are untouched.**
2. **`claude_md_rule_triage.py` DOES NOT READ `CLAUDE.md`, which corrects the previous report.** It
   opens exactly two files — the decisions register's data file and its own artifact. Its population
   is the register entries whose home is `CLAUDE.md`, filtered on a field. The previous report
   attributed its failure to the `CLAUDE.md` insertion; **the real cause is the backbone edit**, and
   this was established at the tool source, including the line that copies the `home` anchor into
   every output row.
3. **THE TWO REFS NOW AGREE** — recorded in the closing note below, written after the push.

---

## 10. The self-check after the coding exercise

The work actually on disk was re-read before this report was written, not recalled.

**What the check caught, all reported above rather than shipped silently:**

1. **The backbone hash does not match the previous report's §5.4 value.** Rather than assume the
   obvious explanation, it was established at the git objects — the 41 differing lines are all `home`
   fields, so the hash gap is that report's own §5.5 re-aim. §3.2.
2. **The shell-read guard refused one command** (D-253, the interpreter-code widening) and the
   sanctioned file-tool route was used instead. Declared at §1.3 rather than passed over.
3. **The baseline was preserved as a git blob rather than transcribed.** The dispatch asks for the
   per-entry classes to be recorded; recording 411 values by hand would be the transcription D-431
   forbids and a weaker proof besides, so the whole file was preserved by the content-addressed route
   and the comparison made byte-for-byte. The field compared is **named** (`proposed_class`) and the
   totals **are** stated, so nothing the dispatch asks for is missing. Declared at §4.1.

**Against the bars:** no tool source edited (B1); no governing document amended (B2); the backbone
proved unmoved by hash (B3); no bare register regeneration (B4); the boot pack untouched and never
run bare (B5); `gen_withheld_family_reading.py` neither edited nor run by this batch (B6);
`claude_md_finer_archive.json` held back (B7); no row and no `D-NNN` (B8); nothing in B9's list
touched; no dispatch figure transcribed (B10).

**The reserved-word check.** Every bare *score* above is the musical sense (*"no score corpus"*, *"no
score"*); the numerical sense does not occur. *Register* is never bare — each use reads *the decisions
register* or *the open-items register*. *Measure* appears only as the verb and as *measurement*, never
for the bar. *Note* is used for a written remark only in the compound *closing note*, which names a
section of this file rather than a pitch event.

---

## 11. The commit and the push

**★ WHY THIS SECTION IS IN TWO PARTS, stated before the values rather than after them.** This report
is a member of the staged set, so the commit that carries it cannot name itself inside it. Everything
above was written before the commit; **the commit hash and the push result are in the closing note
below, appended to this file after the push, which leaves this file standing as an uncommitted
modification for a later batch to pick up.** That is the shape the previous close's report already
has in this batch's own candidate set, and it is declared here so that no reader takes the committed
text for a claim that the push had happened when it was written.

*Provenance: CC, 2026-09-21. Dispatch pinned at `3cfbfdf43f124add50b1d2b4975c7f05d4262d82`. Every
figure above is cited to the object, the artifact or the capture that produced it; the two guard
captures are at `scratchpad/guard_open.txt` and `scratchpad/guard_close.txt` outside the working
tree, and the per-task outputs at the `scratchpad/t1b_*`, `t2_*` and `t2a_*`/`t2b_*` files named in
place.*
