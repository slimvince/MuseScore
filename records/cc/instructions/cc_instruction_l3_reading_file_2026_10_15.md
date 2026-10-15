# CC dispatch — L3's WITHHELD-FAMILY READING FILE: the reading-file tool gains an `l3` subject and renders L3's three verdict lists for the user to rule, with one wording repair to the verdict table at the front — NOTHING withheld, NO pack, NO algorithm change, NO register entry, NO session booted

> **★★ RELEASED 2026-10-15** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_nine.md`, which wrote it, after the check at
> the sources recorded at the end of this file. It is executed by Claude Code when the user hands it over (D-252);
> the Cowork writing side never runs it. *(The banner this replaces read, preserved (#12): "**★★ DRAFT UNDER
> CONSTRUCTION BY THE COWORK WRITING SIDE — NOT TO BE HANDED TO CLAUDE CODE.** Claude Code: if you are reading this
> banner, STOP at once, do nothing, and report that you were handed an unfinished draft.")*

## What this batch is, in plain words

On 2026-10-14 the user ruled that L3's boot pack carries a withheld family and that every design-intent entry is a
candidate for it (Rulings 1 and 2 of `records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`).
The last batch published L3's 244 candidates at `tools/audit/l3_candidate_list.json` and wrote one verdict PROPOSAL
per candidate into `VERDICTS["l3"]` of `tools/audit/gen_derivation_boot_pack.py`. The writing side then checked those
verdicts at the published text (entry 400) and found them complete and coherent, with ONE wording defect: the last
batch's own reserved-word correction dropped a space in fifteen reason strings ("tohow", "towhich",
"thebounded-context", "theconfidence").

This batch **(1)** repairs those fifteen spaces, and **(2)** gives the existing reading-file tool,
`tools/audit/gen_withheld_family_reading.py`, an `l3` subject, renders
`ratification_surfaces/cowork_withheld_family_l3_reading.md` from the verdict table, and enrols the new run in the
guard set — the shape `records/cc/instructions/cc_instruction_l2_reading_file_2026_09_05.md` used for L2. The user
then rules the three lists one per turn. **Nothing here changes the algorithm as any specification defines it.**

## Words used in this dispatch, explained first

- **Boot pack, withheld family, candidate, verdict (IN / OUT / UNPLACED), finding, reason, guard set, red,
  historical record** — as defined in `records/cc/instructions/cc_instruction_l3_candidate_list_and_verdict_pass_2026_10_14.md`,
  "Words used in this dispatch". A verdict in `VERDICTS["l3"]` is a PROPOSAL and withholds nothing.
- **The reading file** — a generated markdown surface the user reads to rule the three lists. It is rendered by the
  reading-file tool from the verdict table and the candidate list, never hand-written, and its `--check` re-renders
  and compares.
- **The subject-specific prose** — the sentences in the reading-file tool's `render()` that are true of L2 only
  ("L2's pack does not exist yet", "it asks FOUR things at once", the sizing table's keyword and home-document
  columns, and so on). Task 2 moves them, unchanged, into the tool's `SUBJECTS["l2"]` entry, and gives `SUBJECTS["l3"]`
  its own.
- **Register group** — the letter under which `DECISIONS.md` lists an entry. ★ Register group **F** is titled
  *"Layer 3 — key and mode"* (the old `ARCHITECTURE.md` Layer 1–6 numbering), while the subject `l3` is the
  framework's **L3 — the read-off facts**. The two are different units; the reading file says so to the user.

## The ruling ledger

| | Record or rule | What it orders | Task |
|---|---|---|---|
| L.1 | `records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`, Ruling 2 | *"the verdicts are ruled by the user list by list, one list per turn, as for L2 … No identity is withheld that the user has not ruled."* — the lists need a surface to be ruled from. | 2 |
| L.2 | The user's standing rule of 2026-09-22 | Staleness and apparent errors in the record are fixed without asking him. | 1, 2(e) |
| L.3 | `CLAUDE.md`, Conventions, *"HOW A DECISION SURFACE IS WRITTEN, AND IN WHAT ORDER ITS RULES APPLY"*, step 8 | *"D-658's fourth requirement — no recommendation at all — is SUPERSEDED by step 5 above … and is dead."* The tool's UNPLACED heading cites D-658 for its no-recommendation sentence; L3's file carries a corrected heading. | 2(e) |

The user's standing rule: **every commit is pushed, and the push is verified at `.git/refs/remotes/origin/master`.**

## Premise ledger (written 2026-10-15 by the writing side from staged copies read with the file tools; no shell command and no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/HEAD` → `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both `44b22bee63b7ecdd1e6496d15f73ea570216fbf2`. `.git/logs/HEAD` names that
  commit *"End state: the L3 candidate list and verdict pass's guard run at the close's tree, with the two artifacts
  regenerated under A2"*, its parent the close `e95282f9f5cd3938d7d93fcfe2f4d519eac26631`, and the last task commit
  before the close `e47daa17bc7d7e1f0c190a1932283435964bca2b`. **Re-read both ref files yourself before Task 0.**
- **FACT — the guard start state, at `tools/audit/guard_state.json` → `summary`:** run 79, failing 14 — the same
  fourteen the last dispatch's premise ledger names (`gen_phase3_gate_partition.py`, `gen_filing_convention_application.py`,
  `gen_artifact_inventory.py`, `gen_artifact_inventory_surface.py`, `gen_test_construction_evidence.py`,
  `gen_retirement_caller_check.py`, `decisions/apply_soft_discard.py`, `decisions/apply_residue_discard.py`,
  `gen_epoch_write_path.py`, `gen_derivation_boot_pack.py`, `gen_recognizer_establishment_sort.py`,
  `decisions/gen_cluster_dispositions.py --verify`, `decisions/gen_home_classification.py`,
  `decisions/gen_phase1p_delegation_bar.py`) per the last batch's close, end-state part. The writing side read
  `summary`'s run and failing counts and the first failing name only; **the other names are relayed from the last
  report — your start run is the proof.** The classification tool `gen_guard_classification.py` ends on its
  standing STOP naming `gen_l0_l1_outgoing_population.py`, `gen_l2_withheld_documents.py`,
  `gen_withheld_family_reading.py` (the last close, end-state part).
- **FACT — the reading-file tool runs in the guard set ONCE today**, as `--subject l2 --check`, exit 0
  (`guard_state.json`; `gen_guard_state.py` `AUTHORED`, the entry headed *"AUTHORED 2026-09-05,
  cc_instruction_l2_reading_file_2026_09_05.md Task 2"*). **One tool may carry more than one authored run:**
  `gen_guard_state.py` already registers `tools/audit/gen_governing_surface_split.py` once per pair, by a list
  comprehension inside `AUTHORED`.
- **FACT — the reading-file tool** (`tools/audit/gen_withheld_family_reading.py`, 28,765 bytes at its staging, read
  WHOLE): `SUBJECTS` carries `l2` alone. `render()` writes L2-only sentences in §1 (the boot-pack and register-group
  bullets), §2 (*"That is L2's charter question … it asks FOUR things at once"*), §3 (*"what is not ruled for L2"*),
  §4 (three criterion-term bullets, a population paragraph about the keyword term, and a sizing table that reads
  `art["the_sizing"]["by_register_group_and_term"]`), §5 (*"with L2's four-limbed question"*), §6 (four bullets naming
  L2), §7 and §8 (*"L2's pack members"*, *"L2's boot-list members"*), and in the ruled-status banner (*"only after
  L2's"*). Its lists render in `GROUP_ORDER` (L2's verdict-pass order, A C D E F G B H …). **Run on `l3` as it stands,
  it raises a `KeyError` at the sizing table**: L3's candidate list carries `the_sizing` → `by_register_group` only.
- **FACT — L3's candidate list** (`tools/audit/l3_candidate_list.json`): `the_population` 244 of 411; `the_sizing` →
  `by_register_group`, eighteen groups; nine checks, all `"passed": true`; `the_writing_side_s_expectation_disagreements`
  empty; both identity lists of the comparison with L2's list empty.
- **FACT — `CRITERION["l3"]`** in the generator: `groups` names the twenty groups A to U without R (O and P among
  them), `home_documents`, `architecture_spans`, `keywords` and `always` all empty. `group_title()` reads every title
  from the backbone's own `groups` table and STOPs on a group it lacks.
- **FACT — L3's charter at its home.** `FRAMEWORK.md`, heading `### L3 — The read-off facts` (once in the file); the
  line `- **Question:** given a settled tonal reading, what else does a harmonic analysis of this music say?` — the
  bold-labelled form occurs once; an italic restatement (`- *Question:* …`) occurs later and does not match the bold
  needle. The block's **Publishes** line names the five facts: the cadence at each phrase end with its type; the
  phrase and section grouping; the chord symbol (root pitch class, quality, bass note); the figured bass; the harmonic
  rhythm.
- **FACT — the fifteen fused words (Task 1)**, at `tools/audit/gen_derivation_boot_pack.py`, all inside
  `VERDICTS["l3"]`'s reason strings and found by a whole-file search that returned no other site:
  `answer tohow` — **11** occurrences; `answer towhich` — **1**; `belongs to thebounded-context` — **1**;
  `belongs to theconfidence` — **2**. A second, wider search over the whole file for a short word fused to
  *the / how / which / what / where / whether / its* returned only the twelve `to…` sites above.
- **FACT — `gen_derivation_boot_pack.py --check` IS ALREADY RED**, and nothing in the generator reads `VERDICTS["l3"]`
  (`build()` iterates `WITHHELD`, which carries no `l3`). Inertness of Task 1 is proven by the `--check` OUTPUT being
  byte-identical before and after, as in the last two batches.
- **FACT — the untracked population Task 0 lands:** this dispatch; handoff entry 400 (written by the writing side at
  its close — if absent at boot, report the absence, not a STOP). At the handoff folder's listing of 2026-10-15 the
  newest entry was 399. `ratification_surfaces/` was not listed — A1's enumeration settles it.

- **ASSUMPTION A1 — the working tree, by content.** Tracked modifications at boot: **none expected**, except the
  line-ending-only marking of `tools/audit/claude_md_finer_archive.json` the last three reports record (re-establish
  it; leave it untouched; never stage it). Any other tracked modification at boot or during the run is a
  STOP-and-report, except a path this batch writes, after the task that writes it and until its commit. A further
  untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` appearing during the run is the writing side's and is
  NOT landed and NOT a STOP. **Check (Task 0, first act):** per tracked input this batch edits
  (`tools/audit/gen_derivation_boot_pack.py`, `tools/audit/gen_withheld_family_reading.py`,
  `tools/audit/gen_guard_state.py`, `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`)
  `git diff --stat 44b22bee63b7ecdd1e6496d15f73ea570216fbf2 -- <path>; echo "exit:$?"`; per path of Task 0's list
  `git ls-files --others --exclude-standard -- <path>; echo "exit:$?"`; the whole tracked population with
  `tools/audit/changed_paths.py`.
- **ASSUMPTION A2 — the guard run before the first edit:** the fourteen, exactly, and the classification tool's
  standing STOP naming the three tools above. **Predicted at the end state: run 80 (the 79 plus the one run Task 2(f)
  enrols), historical 20, not run 4, failing the same fourteen**; the new run `--subject l3 --check` PASSES and the
  existing `--subject l2 --check` PASSES. Reds this batch's own acts may cause, classed by cause and NOT a STOP:
  `gen_l0_l1_outgoing_population.py --check` and `gen_defense_share.py --check` if Task 3's `STATUS.md` entries move
  their inputs — regenerate, compare against the committed blob by explicit hash, commit with the end state, report
  that no member moved (a member moving IS a STOP-and-report); `gen_session_start_read_size.py --check` if
  regenerated before the last `STATUS.md` edit; `gen_guard_state.py`'s own artifact between Task 2's commit and the
  end-state run. A red outside these is a STOP-and-report.
- **ASSUMPTION A3 — byte-unchanged by this batch, verified at the objects after the last commit:** every governing
  document except `STATUS.md` and `STATUS_ARCHIVE.md`; `tools/audit/gen_derivation_boot_pack.py` except Task 1's
  fifteen one-space insertions; `tools/audit/gen_guard_state.py` except Task 2(f)'s one insertion;
  **`ratification_surfaces/cowork_withheld_family_l2_reading.md`** (the ruled L2 surface); `tools/audit/l3_candidate_list.json`
  and `tools/audit/l2_candidate_list.json`; every rendered decisions-register file; everything under
  `tools/audit/derivation_boot_pack/` and `tools/audit/derivation_boot_pack.json`; every ruling record, surface,
  extract, `FRAMEWORK.md` and the suspension file. Any other difference is a STOP-and-report.

## The standing bars, and the commit-and-push discipline

No `src/` edit, no golden, no test changed or run, no build, nothing under `tools/corpus/` or `tools/robust_stop/`,
**no measurement of the analysis built, designed, scoped or run**, no derivation of any specification statement,
**NO SESSION BOOTED, no pack rendered** (the generator runs in `--check` only), **no `WITHHELD`, `EXTRAS`, `FROZEN` or
`VERDICT_DATE` entry for `l3`, no edit to `CRITERION`, to any verdict word, finding or to any reason except Task 1's
fifteen spaces, and no edit to any other `VERDICTS` entry**, no open-items row created, flipped or discarded, **no
decisions-register entry and no `D-NNN` allocated, nothing written into the suspension file**, no edit to any
governing document except `STATUS.md`/`STATUS_ARCHIVE.md` in Task 3, **no re-render of the L2 reading file**, **no
ruling taken, and no recommendation about which list any candidate should end on**.

**Commit-and-push per task. Run the FULL guard set BEFORE the first edit (`python tools/audit/gen_guard_state.py
--check`) and again at the end (write mode, committed as the artifact of a real run). After every commit: push, then
read `.git/refs/remotes/origin/master` with the file tools and confirm it names the commit just made.** Verify every
commit at the object by explicit hash. Every shell command carries `; echo "exit:$?"`. `git status` and `git diff`
over the working tree are denied by the armed guard — use the explicit-hash forms of A1. Plain single-quoted
`git commit -m '…'` subjects. Every working-tree read through the file tools (D-253); a run's output is redirected
to a file in your session's scratch folder outside the repository and read with the file tools; every script this
dispatch orders is written there too. Edit files with your file-editing tool, never by retyping a whole file. **If
an old text quoted below does not occur EXACTLY the number of times stated (once, unless a count is given) in its
file, that edit is a STOP-and-report for that edit alone**: make nothing for it, report what you found, and — because
Task 2's edits depend on one another — a STOP on any Task 2 edit restores the tool by explicit hash and ends Task 2.
The reserved-word rule binds every line you write: *score*, *key*, *note*, *figure*, *register*, *measure*, *part*,
*scale*, *tie* only in their musical senses, or qualified.

## The ordered first reads

**(1)** `records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` WHOLE. **(2)** `CLAUDE.md`
at its six ruled spans (the membership at its "Build and test commands" block), `STATUS.md` whole, `DECISIONS.md`
whole; rule (a)'s `gating_ids` at `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`. **(3)**
`records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_nine.md` whole, and `…four_hundred.md` whole if
present (the current entry point). **(4)** `cowork_audit_protocol.md`'s dispatch-protocol section. **(5)** The last
batch: its dispatch `records/cc/instructions/cc_instruction_l3_candidate_list_and_verdict_pass_2026_10_14.md` whole,
its report `records/cc/reports/cc_report_l3_candidate_list_and_verdict_pass_2026_10_14.md` whole, its close (the
last section of `records/cowork/handoff/cowork_away_returns.md`). **(6)** The L2 model:
`records/cc/instructions/cc_instruction_l2_reading_file_2026_09_05.md` at Task 2. **(7)** `tools/audit/gen_withheld_family_reading.py`
WHOLE. **(8)** `FRAMEWORK.md` from the heading `### L3 — The read-off facts` through the line before
`### The second axis — voice leading`. **(9)** The generator at `VERDICT_DATE`, `CRITERION["l3"]`, `group_title()`,
and `VERDICTS["l3"]` whole. **(10)** `gen_guard_state.py` at `AUTHORED` (its head, the reading-file entry, and the
`gen_governing_surface_split.py` entries). **(11)** `tools/audit/gen_status_batch_bound.py` whole at the object
`44b22bee63b7ecdd1e6496d15f73ea570216fbf2:tools/audit/gen_status_batch_bound.py` before Task 3.

## Task 0 — land this dispatch and entry 400, and PUSH

To be landed (the standing clause): `records/cc/instructions/cc_instruction_l3_reading_file_2026_10_15.md` and
`records/cowork/handoff/cowork_handoff_entry_four_hundred.md`. **Each path's standing at the tip is yours to take
under A1** (expected: both UNTRACKED).

**The acts, in order:** **(1)** A1's check. A path already tracked is reported and not re-landed; entry 400 absent is
reported, not a STOP; the dispatch absent is a STOP. Report any other untracked path the enumeration shows under
`records/`, `reading_pass/` or `ratification_surfaces/` — NOT landed, not a STOP. **(2)** If
`tools/audit/gen_evidence_pin_membership.py --check` is red, regenerate `tools/audit/evidence_pin_membership.json`
and measure it against the committed blob: the only permitted change is its list of ruling records read; any other
movement is a STOP-and-report. **(3)** Commit the paths that exist and are untracked, plus the membership artifact
only if it moved. Subject, exactly:
`record: the L3 reading-file dispatch and entry 400 landed`
(if entry 400 is absent, the subject ends `…dispatch landed`). **(4)** PUSH; verify `origin/master` at the ref file.

**Under standing clause P-2 this dispatch is PINNED at Task 0:** record its blob, and prove it unmoved immediately
before staging it.

**E0:** the named paths in one commit; `origin/master` at the commit; every path accounted for.

## Task 1 — the fifteen missing spaces in `VERDICTS["l3"]`'s reasons; ONE commit, before anything else

It cannot be stopped partway, so it goes first with nothing large in front (D-670).

**(a)** Run, and keep the output: `cd C:\s\MS && python tools/audit/gen_derivation_boot_pack.py --check > <scratch>\dbp_before.txt 2>&1; echo "exit:$?"`.

**(b)** In `tools/audit/gen_derivation_boot_pack.py`, confirm each old text's count FIRST, then replace every
occurrence:

| Old text | Count that must hold | New text |
|---|---|---|
| `answer tohow` | 11 | `answer to how` |
| `answer towhich` | 1 | `answer to which` |
| `belongs to thebounded-context` | 1 | `belongs to the bounded-context` |
| `belongs to theconfidence` | 2 | `belongs to the confidence` |

Every occurrence lies inside `VERDICTS["l3"]` (the block opened by the comment
`# ── L3, the deriving subject after L2 — PROPOSALS, NOT A WITHHELD FAMILY`); an occurrence outside it is a
STOP-and-report. No other character of the file changes.

**(c)** Re-run (a) to `<scratch>\dbp_after.txt`: **the output byte-identical to the before file and the same exit
code** (compare by `cmp` and report it). Any difference: restore the generator to `44b22bee…` by explicit hash, make no
commit, report, and go to Task 2 (whose `l3` lists then render with the fused words, which the report says).

**(d)** Commit the generator alone:
`audit(l3): fifteen missing spaces restored in the verdict reasons (former: "tohow", "towhich", "thebounded-context", "theconfidence")`.
Push; verify.

**E1:** the four counts confirmed; the byte-identity reported; the commit pushed.

## Task 2 — the reading-file tool gains an `l3` subject; L3's reading file rendered; the run enrolled in the guard set: ONE commit

### (a) Before the first edit

Run, and keep: `cd C:\s\MS && python tools/audit/gen_withheld_family_reading.py --subject l2 --check > <scratch>\rf_l2_before.txt 2>&1; echo "exit:$?"`.
**Expected: `PASS: ratification_surfaces/cowork_withheld_family_l2_reading.md re-renders byte-identically`, exit 0.**
Anything else is a STOP-and-report before any edit.

### (b) The edits to `tools/audit/gen_withheld_family_reading.py`, in this order

**THE PRINCIPLE OF EVERY EDIT BELOW:** each L2-only sentence moves out of `render()`, unchanged, into
`SUBJECTS["l2"]`, and `render()` writes it from there. For `l2` the rendered file must stay byte-identical — (d) proves
it. `SUBJECTS["l3"]` carries L3's own text.

**Edit 1 — the `l2` entry gains its subject-specific prose.** Old text (once):

```python
        "title": "The WITHHELD FAMILY for the L2 subject — put to the user for a ruling",
```

New text:

```python
        "title": "The WITHHELD FAMILY for the L2 subject — put to the user for a ruling",
        "subject_name": "L2",
        # ── THE SUBJECT-SPECIFIC PROSE.  Moved here from render() on 2026-10-15 by
        #    `cc_instruction_l3_reading_file_2026_10_15.md` Task 2, so that a second subject can carry
        #    its own.  Every string below is the text render() wrote for L2 before the move, byte for
        #    byte; the proof is that `--subject l2 --check` passes before and after the move.
        "words_boot_pack": (
            "- **The boot pack** — the self-contained directory such a session opens at boot, and nothing",
            "  else.  L2's pack does not exist yet; its members are a later ruling.",
        ),
        "words_register_group": (
            "- **The register group** — the letter under which `DECISIONS.md` lists an entry.  It is a",
            "  property of the entry and decided no verdict.  Note that register group **E** is titled",
            "  *Layer 2 — the slicer* while this subject is called **L2**: they are different units in two",
            "  different numbering schemes (`ARCHITECTURE.md`'s Layer 1–6 and the framework's L0/L1/L2).",
        ),
        "charter_gloss": (
            "and it asks FOUR things at once: the",
            "tonality at each moment; where one harmony ends and the next begins; which sounding notes are",
            "chord tones and which elaborate; and what chord is read over each span.  The pilot subject asked",
            "only the second of these.  A verdict here is IN if the entry discloses the ruled answer to ANY of",
            "the four, in whole or in part.",
        ),
        "section_3": (
            "## 3. What this family protects, and what is not ruled for L2",
            "",
            "For the pilot, a separate ruling named one oracle passage the family protected.  **No ruling",
            "names an oracle passage for L2.** Ruling 81's own record states that the record was searched",
            "before it was taken and that no ruling reached L2's family; Ruling 81 rules that the pack",
            "carries a family derived over a criterion built from the charter, and stops there; and none of",
            "Rulings 82 to 89, which fix the criterion's terms, names one.  What the family protects is",
            "therefore the entries themselves: the recorded current answers to the four limbs, which are the",
            "IN rows below.  This file does not restate any of those answers beyond the one-sentence finding",
            "each row carries, and it does not invent an oracle.",
        ),
        "empty_terms_line": (
            "- the `ARCHITECTURE.md` passage term is **EMPTY** by ruling, and no identity is named by any "
            "ruling for this subject, so the named-identity term is **EMPTY**."),
        "bound_tail": (
            "  The keyword term is a plain substring match whose reach is UNMEASURED; an entry bearing on this "
            "subject in words none of the terms carry does not appear here at all, and the candidate list "
            "says so on itself.  A keyword can match inside a longer word; every such match is published "
            "with its context at `tools/audit/l2_candidate_list.json` → `the_candidates` → `matched_by`, and no "
            "keyword match was treated as a reason for IN."),
        "sizing_by_term": True,
        "test_intro": "From the pilot's own dispatch, with L2's four-limbed question in place of the pilot's one:",
        "test_in": (
            "- **IN** — a deriving session that read this entry would know, in whole or in part, what the",
            "  ruled answer to the charter question is.",
        ),
        "not_yet": (
            "- **No leak list.** The pilot's fourth list named entries the pack's generated members could not",
            "  render because their text pointed into the implementation.  A leak is found when a pack is",
            "  rendered, and L2's pack is not rendered until the family is ruled and its members are ruled.",
            "- **No derived cross-reference additions.** When a pack is built, every entry whose own text",
            "  quotes or cross-references a withheld identity is withheld with it, derived and published whole",
            "  and not ruled.  Ruling 84 (§3cm) bounds that derivation: it may ADD a withholding to an entry",
            "  you have not ruled on, and may NOT overturn a verdict you have ruled.  None exists for L2 yet.",
            "- **No withheld passages.** A passage is a cut inside a member the boot list quotes WHOLE.  L2's",
            "  boot list is not ruled, so there is no member to cut.",
            "- **The date each verdict carries.** Ruling 81 requires it.  The generator stamps every verdict",
            "  with one module constant at render time, which is the pilot's authoring date and would be false",
            "  for these; the gap is recorded as owed to the batch that builds L2's pack, and the authoring date",
            "  of every group block stands in the table's own heading comments meanwhile.",
        ),
```

**Edit 2 — the `l3` entry.** Old text (once):

```python
                "being stated in full by the withheld D-525.",
            ),
        },
    },
}
```

New text:

```python
                "being stated in full by the withheld D-525.",
            ),
        },
    },
    # ── L3, added 2026-10-15 by `cc_instruction_l3_reading_file_2026_10_15.md` Task 2 ─────────────
    # Ruling 2 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`: the lists are ruled one
    # per turn, as for L2, from a surface rendered from the table.  No `ruling` block: the lists are
    # not ruled, so the file renders as a reading surface FOR RULING.
    "l3": {
        "candidate_list": "tools/audit/l3_candidate_list.json",
        "out": "ratification_surfaces/cowork_withheld_family_l3_reading.md",
        "title": "The WITHHELD FAMILY for the L3 subject — put to the user for a ruling",
        "subject_name": "L3",
        "subject_in_plain_words": (
            "The read-off facts: given a settled tonal reading, where does each phrase end and how do "
            "phrases group into sections, what cadence stands at each phrase end and of what type, what "
            "is the chord symbol, what is the figured bass, and what is the harmonic rhythm?"),
        # Located on every run, as for L2.  L3's block labels its question `**Question:**` (L2's
        # carries `**Question, in one sentence:**`); the bold form occurs once, an italic restatement
        # later in the file does not match it.
        "charter_file": "FRAMEWORK.md",
        "charter_label": "**Question:** ",
        "charter_sentence": "given a settled tonal reading, what else does a harmonic analysis of this music say?",
        "charter_heading": "### L3 — The read-off facts",
        "criterion_rulings": (
            "Ruling 2 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` ruled that it reaches "
            "the whole design-intent class, and `cc_instruction_l3_criterion_write_2026_10_14.md` wrote it "
            "as a group term naming every group of the decisions register's own table."),
        "verdicts_authored": (
            "by Claude Code on 2026-10-14 under "
            "`cc_instruction_l3_candidate_list_and_verdict_pass_2026_10_14.md` Task 3, at each entry's own "
            "published verbatim and plain restatement in the candidate list, in the decisions register's "
            "own group order"),
        # The verdict pass wrote L3's groups in the register's own order; the lists keep it.
        "group_order": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Q", "S",
                        "T", "U"],
        "words_boot_pack": (
            "- **The boot pack** — the self-contained directory such a session opens at boot, and nothing",
            "  else.  L3's pack does not exist yet; its members are a later ruling.",
        ),
        "words_register_group": (
            "- **The register group** — the letter under which `DECISIONS.md` lists an entry.  It is a",
            "  property of the entry and decided no verdict.  Note that register group **F** is titled",
            "  *Layer 3 — key and mode* while this subject is called **L3**, and that register group **H**,",
            "  *Layer 5 and Layer 6 — function, cadence, grouping*, carries much of what the framework puts",
            "  at L3: they are different units in two different numbering schemes (`ARCHITECTURE.md`'s",
            "  Layer 1–6 and the framework's L0 to L3).",
        ),
        "charter_gloss": (
            "and the same block's **Publishes** line names the FIVE",
            "facts this layer reads off that settled reading: the cadence at each phrase end, with its type;",
            "the phrase and section grouping; the chord symbol — root pitch class, quality and bass note; the",
            "figured bass; and the harmonic rhythm.  L3 may not revise L2: the tonality, where one harmony",
            "gives way to the next, which sounding notes are chord tones, and the chord read over each span",
            "reach it settled.  A verdict here is IN if the entry discloses the ruled answer to how L3 reads",
            "off ANY of the five, in whole or in part.",
        ),
        "section_3": (
            "## 3. What this family protects, and what is not ruled for L3",
            "",
            "For the pilot, a separate ruling named one oracle passage the family protected.  **No ruling",
            "names an oracle passage for L3.** Ruling 1 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`",
            "rules that L3's pack carries a withheld family, and Ruling 2 that every design-intent entry is a",
            "candidate; neither names one.  What the family protects is therefore the entries themselves: the",
            "recorded current answers to how L3 reads off its five facts, which are the IN rows below.  This",
            "file does not restate any of those answers beyond the one-sentence finding each row carries, and",
            "it does not invent an oracle.",
        ),
        "empty_terms_line": (
            "- the home-document, keyword and `ARCHITECTURE.md` passage terms are **EMPTY**, and no identity "
            "is named by any ruling for this subject, so the named-identity term is **EMPTY**: the group term "
            "names every group of the decisions register's own table, so it alone reaches the whole "
            "design-intent class (Ruling 2)."),
        "bound_tail": (
            "  Every design-intent entry of the sort is a candidate, so none of that class is missing here; "
            "the rulings recorded only in a ruling record since the register's rule (c) was suspended are "
            "outside the sort as well, and the candidate list states that bound on itself."),
        "sizing_by_term": False,
        "test_intro": "From the pilot's own dispatch, with L3's five published facts (§2) in place of the pilot's one question:",
        "test_in": (
            "- **IN** — a deriving session that read this entry would know, in whole or in part, the ruled",
            "  answer to how L3 reads off ANY of its five facts (§2).",
        ),
        "not_yet": (
            "- **No leak list.** The pilot's fourth list named entries the pack's generated members could not",
            "  render because their text pointed into the implementation.  A leak is found when a pack is",
            "  rendered, and L3's pack is not rendered until the family is ruled and its members are ruled.",
            "- **No derived cross-reference additions.** When a pack is built, every entry whose own text",
            "  quotes or cross-references a withheld identity is withheld with it, derived and published whole",
            "  and not ruled.  Ruling 84 (§3cm of `cowork_rulings_2026_08_31_decision_surface_sitting.md`)",
            "  binds L3 as written (§2 of the L3 sitting record): an addition that would withhold an entry you",
            "  have ruled admitted is put to you as its own list rather than standing.  None exists for L3 yet.",
            "- **No withheld passages.** A passage is a cut inside a member the boot list quotes WHOLE.  L3's",
            "  boot list is not ruled, so there is no member to cut.",
            "- **The date each verdict carries.** Ruling 2 of the L3 sitting record requires it.  The",
            "  generator's per-subject verdict-date table carries no `l3` entry, and the generator STOPs when",
            "  it builds a subject with graded candidates and no date there; the date is owed to the batch that",
            "  builds L3's pack, and the authoring date of every group block (2026-10-14) stands in the table's",
            "  own heading comments meanwhile.",
        ),
        # The UNPLACED list's heading, corrected for this subject.  The shared heading cites D-658 for
        # making no recommendation; that requirement of D-658 is superseded (`CLAUDE.md`, Conventions,
        # the order of a decision surface's rules, step 8).  L2's ruled file keeps the shared heading.
        "unplaced_gloss": (
            "These could not be defended either way in one sentence at the entry's own verbatim, so "
            "they were not guessed.  Each row says what was read.  This file makes no recommendation on "
            "any of them; a recommendation, with its grounds, comes on the decision surface that puts this "
            "list to you (`CLAUDE.md`, Conventions, the order in which a decision surface's rules apply, "
            "step 5)."),
    },
}
```

**Edit 3 — the ruled-status banner names the subject.** Old text (once):

```python
        w("> withheld yet and no pack exists**: the withheld family is authored from LIST ONE only after L2's")
```

New text:

```python
        w(f"> withheld yet and no pack exists**: the withheld family is authored from LIST ONE only after {spec['subject_name']}'s")
```

**Edit 4 — §1's boot-pack bullet.** Old text (once):

```python
    w("- **The boot pack** — the self-contained directory such a session opens at boot, and nothing")
    w("  else.  L2's pack does not exist yet; its members are a later ruling.")
```

New text:

```python
    for line in spec["words_boot_pack"]:
        w(line)
```

**Edit 5 — §1's register-group bullet.** Old text (once):

```python
    w("- **The register group** — the letter under which `DECISIONS.md` lists an entry.  It is a")
    w("  property of the entry and decided no verdict.  Note that register group **E** is titled")
    w("  *Layer 2 — the slicer* while this subject is called **L2**: they are different units in two")
    w("  different numbering schemes (`ARCHITECTURE.md`'s Layer 1–6 and the framework's L0/L1/L2).")
```

New text:

```python
    for line in spec["words_register_group"]:
        w(line)
```

**Edit 6 — §2 after the charter sentence.** Old text (once):

```python
    w(f"That is L2's charter question, located on this run at `{spec['charter_file']}` under the heading")
    w(f"`{spec['charter_heading']}` — *\"{charter_one_line}\"* — and it asks FOUR things at once: the")
    w("tonality at each moment; where one harmony ends and the next begins; which sounding notes are")
    w("chord tones and which elaborate; and what chord is read over each span.  The pilot subject asked")
    w("only the second of these.  A verdict here is IN if the entry discloses the ruled answer to ANY of")
    w("the four, in whole or in part.")
```

New text:

```python
    w(f"That is {spec['subject_name']}'s charter question, located on this run at `{spec['charter_file']}` under the heading")
    w(f"`{spec['charter_heading']}` — *\"{charter_one_line}\"* — {spec['charter_gloss'][0]}")
    for line in spec["charter_gloss"][1:]:
        w(line)
```

**Edit 7 — §3.** Old text (once):

```python
    w("## 3. What this family protects, and what is not ruled for L2")
    w("")
    w("For the pilot, a separate ruling named one oracle passage the family protected.  **No ruling")
    w("names an oracle passage for L2.** Ruling 81's own record states that the record was searched")
    w("before it was taken and that no ruling reached L2's family; Ruling 81 rules that the pack")
    w("carries a family derived over a criterion built from the charter, and stops there; and none of")
    w("Rulings 82 to 89, which fix the criterion's terms, names one.  What the family protects is")
    w("therefore the entries themselves: the recorded current answers to the four limbs, which are the")
    w("IN rows below.  This file does not restate any of those answers beyond the one-sentence finding")
    w("each row carries, and it does not invent an oracle.")
```

New text:

```python
    for line in spec["section_3"]:
        w(line)
```

**Edit 8 — §4's criterion terms.** Old text (once):

```python
    w("- **its recorded home is one of these documents:** " + ", ".join(
        f"`{d}`" for d in criterion["home_documents"]) + ";")
    w("- **any of its title, verbatim, plain restatement or search patterns contains one of these "
      f"{len(criterion['keywords'])} words or phrases:** " + ", ".join(
        f"*{k}*" for k in criterion["keywords"]) + ";")
    w("- the `ARCHITECTURE.md` passage term is **EMPTY** by ruling, and no identity is named by any "
      "ruling for this subject, so the named-identity term is **EMPTY**.")
```

New text:

```python
    if criterion["home_documents"]:
        w("- **its recorded home is one of these documents:** " + ", ".join(
            f"`{d}`" for d in criterion["home_documents"]) + ";")
    if criterion["keywords"]:
        w("- **any of its title, verbatim, plain restatement or search patterns contains one of these "
          f"{len(criterion['keywords'])} words or phrases:** " + ", ".join(
            f"*{k}*" for k in criterion["keywords"]) + ";")
    # The authored line below states the passage and named-identity terms EMPTY; a criterion that
    # carries either would make it false, so that is a STOP rather than a silently wrong sentence.
    if criterion["architecture_spans"] or criterion["always"]:
        raise Stop(f"CRITERION[{subject!r}] carries a passage or a named-identity term, which the "
                   f"authored empty-terms line does not describe")
    w(spec["empty_terms_line"])
```

**Edit 9 — §4's population paragraph.** Old text (once):

```python
      f"returned **{pop['candidates']}** candidates.  The population is the sort artifact's and NOT the "
      "decisions register's, so register entries outside it are reached by no term (D-661, #24).  The "
      "keyword term is a plain substring match whose reach is UNMEASURED; an entry bearing on this "
      "subject in words none of the terms carry does not appear here at all, and the candidate list "
      "says so on itself.  A keyword can match inside a longer word; every such match is published "
      f"with its context at `{spec['candidate_list']}` → `the_candidates` → `matched_by`, and no "
      "keyword match was treated as a reason for IN.")
```

New text:

```python
      f"returned **{pop['candidates']}** candidates.  The population is the sort artifact's and NOT the "
      "decisions register's, so register entries outside it are reached by no term (D-661, #24)."
      + spec["bound_tail"])
```

**Edit 10 — §4's sizing table.** Old text (once):

```python
    sizing = art["the_sizing"]["by_register_group_and_term"]
    w("**The candidates by register group, and the verdicts proposed in each:**")
    w("")
    w("| group | register-group title | candidates | reached by the group term | by a keyword | by a home document | IN | OUT | UNPLACED |")
    w("|---|---|---|---|---|---|---|---|---|")
    for g in groups_present:
        s = sizing.get(g, {})
        n = sum(per_group[g].values())
        w(f"| {g} | {cell(boot_pack.group_title(g))} | {n} | {s.get('group', 0)} | {s.get('keyword', 0)} | "
          f"{s.get('home-document', 0)} | {per_group[g][boot_pack.VERDICT_IN]} | "
          f"{per_group[g][boot_pack.VERDICT_OUT]} | {per_group[g][boot_pack.VERDICT_UNPLACED]} |")
    total = sum(counted.values())
    w(f"| **all** | | **{total}** | | | | **{counted[boot_pack.VERDICT_IN]}** | "
      f"**{counted[boot_pack.VERDICT_OUT]}** | **{counted[boot_pack.VERDICT_UNPLACED]}** |")
```

New text:

```python
    total = sum(counted.values())
    w("**The candidates by register group, and the verdicts proposed in each:**")
    w("")
    if spec["sizing_by_term"]:
        sizing = art["the_sizing"]["by_register_group_and_term"]
        w("| group | register-group title | candidates | reached by the group term | by a keyword | by a home document | IN | OUT | UNPLACED |")
        w("|---|---|---|---|---|---|---|---|---|")
        for g in groups_present:
            s = sizing.get(g, {})
            n = sum(per_group[g].values())
            w(f"| {g} | {cell(boot_pack.group_title(g))} | {n} | {s.get('group', 0)} | {s.get('keyword', 0)} | "
              f"{s.get('home-document', 0)} | {per_group[g][boot_pack.VERDICT_IN]} | "
              f"{per_group[g][boot_pack.VERDICT_OUT]} | {per_group[g][boot_pack.VERDICT_UNPLACED]} |")
        w(f"| **all** | | **{total}** | | | | **{counted[boot_pack.VERDICT_IN]}** | "
          f"**{counted[boot_pack.VERDICT_OUT]}** | **{counted[boot_pack.VERDICT_UNPLACED]}** |")
    else:
        # One term only, so the candidate list sizes by group alone; its count must equal the
        # table's own, group by group, or the file would show the user two numbers for one thing.
        sizing = art["the_sizing"]["by_register_group"]
        if set(sizing) != set(per_group):
            raise Stop(f"the candidate list sizes groups {sorted(sizing)}, the verdict table grades "
                       f"groups {sorted(per_group)}")
        w("| group | register-group title | candidates | IN | OUT | UNPLACED |")
        w("|---|---|---|---|---|---|")
        for g in groups_present:
            n = sum(per_group[g].values())
            if sizing[g] != n:
                raise Stop(f"register group {g}: the candidate list's sizing says {sizing[g]}, the "
                           f"verdict table grades {n}")
            w(f"| {g} | {cell(boot_pack.group_title(g))} | {n} | {per_group[g][boot_pack.VERDICT_IN]} | "
              f"{per_group[g][boot_pack.VERDICT_OUT]} | {per_group[g][boot_pack.VERDICT_UNPLACED]} |")
        w(f"| **all** | | **{total}** | **{counted[boot_pack.VERDICT_IN]}** | "
          f"**{counted[boot_pack.VERDICT_OUT]}** | **{counted[boot_pack.VERDICT_UNPLACED]}** |")
```

**Edit 11 — the group order.** Old text (once):

```python
    groups_present = [g for g in GROUP_ORDER if g in per_group]
    unknown_groups = sorted(set(per_group) - set(GROUP_ORDER))
```

New text:

```python
    order = spec.get("group_order", GROUP_ORDER)
    groups_present = [g for g in order if g in per_group]
    unknown_groups = sorted(set(per_group) - set(order))
```

**Edit 12 — §5's opening and IN bullet.** Old text (once):

```python
    w("From the pilot's own dispatch, with L2's four-limbed question in place of the pilot's one:")
    w("")
    w("- **IN** — a deriving session that read this entry would know, in whole or in part, what the")
    w("  ruled answer to the charter question is.")
```

New text:

```python
    w(spec["test_intro"])
    w("")
    for line in spec["test_in"]:
        w(line)
```

**Edit 13 — the UNPLACED heading, per subject.** Old text (once):

```python
        heading, gloss = LIST_HEADINGS[verdict]
```

New text:

```python
        heading, gloss = LIST_HEADINGS[verdict]
        if verdict == boot_pack.VERDICT_UNPLACED and "unplaced_gloss" in spec:
            gloss = spec["unplaced_gloss"]
```

**Edit 14 — §6.** Old text (once):

```python
    w("- **No leak list.** The pilot's fourth list named entries the pack's generated members could not")
    w("  render because their text pointed into the implementation.  A leak is found when a pack is")
    w("  rendered, and L2's pack is not rendered until the family is ruled and its members are ruled.")
    w("- **No derived cross-reference additions.** When a pack is built, every entry whose own text")
    w("  quotes or cross-references a withheld identity is withheld with it, derived and published whole")
    w("  and not ruled.  Ruling 84 (§3cm) bounds that derivation: it may ADD a withholding to an entry")
    w("  you have not ruled on, and may NOT overturn a verdict you have ruled.  None exists for L2 yet.")
    w("- **No withheld passages.** A passage is a cut inside a member the boot list quotes WHOLE.  L2's")
    w("  boot list is not ruled, so there is no member to cut.")
    w("- **The date each verdict carries.** Ruling 81 requires it.  The generator stamps every verdict")
    w("  with one module constant at render time, which is the pilot's authoring date and would be false")
    w("  for these; the gap is recorded as owed to the batch that builds L2's pack, and the authoring date")
    w("  of every group block stands in the table's own heading comments meanwhile.")
```

New text:

```python
    for line in spec["not_yet"]:
        w(line)
```

**Edit 15 — §7, the ruled branch.** Old text (once):

```python
        w("**The withheld family itself is authored from LIST ONE in a later act**, together with L2's")
```

New text:

```python
        w(f"**The withheld family itself is authored from LIST ONE in a later act**, together with {spec['subject_name']}'s")
```

**Edit 16 — §7, the unruled branch.** Old text (once):

```python
        w("together with L2's pack members, which are a separate ruling.")
```

New text:

```python
        w(f"together with {spec['subject_name']}'s pack members, which are a separate ruling.")
```

**Edit 17 — §8.** Old text (once):

```python
    w("- **It does not settle who derives**, nor L2's boot-list members, nor the date mechanism.")
```

New text:

```python
    w(f"- **It does not settle who derives**, nor {spec['subject_name']}'s boot-list members, nor the date mechanism.")
```

### (c) The self-check of the edits, before any run

Re-read the tool's whole change against the tip: copy the tip's object to scratch with
`git show 44b22bee63b7ecdd1e6496d15f73ea570216fbf2:tools/audit/gen_withheld_family_reading.py > <scratch>\rf_tool_tip.py; echo "exit:$?"`
and compare it with the edited working-tree file using the file tools (a working-tree `git diff` is denied by the
armed guard). Every removed line must be one of the old texts above; every added
line one of the new texts. Anything else is a STOP-and-report (restore by explicit hash; end Task 2).

### (d) L2 is untouched — the proof

Run `--subject l2 --check` to `<scratch>\rf_l2_after.txt`. **Expected: byte-identical to `rf_l2_before.txt`, exit 0.**
A FAIL means one moved L2 string differs from what `render()` wrote: **do not re-render the L2 file**; restore the
tool by explicit hash, report which edit's string differs if you can find it, and end Task 2.

### (e) Render L3's file and check it

Run `python tools/audit/gen_withheld_family_reading.py --subject l3` (it prints `wrote … (N bytes)`), then
`--subject l3 --check` (expected `PASS`, exit 0). A `STOP:` from either run is a STOP-and-report: delete nothing by
hand, restore the tool by explicit hash, leave the rendered file uncommitted, report the message, end Task 2.

**Then READ the rendered file WHOLE** and confirm, reporting each: the STATUS banner reads *"READING SURFACE — FOR
RULING"*; §2 quotes L3's question and names the five facts; §4 shows ONE term bullet (the group term naming twenty
groups) followed by the empty-terms line, and the six-column table; the three lists appear in the order IN, OUT,
UNPLACED with group A first inside each; the UNPLACED heading carries the corrected sentence (no D-658); no row
contains `tohow`, `towhich`, `thebounded` or `theconfidence` (if Task 1 was not done, say so instead); and the words
*L2's pack* do not occur anywhere in it. **Do not paste the file or its counts into the report; cite it (D-431).**

### (f) Enrol the new run in the guard set, in the same act

In `tools/audit/gen_guard_state.py`, old text (once):

```python
     "candidate list that no longer matches the table turns this red rather than leaving the user "
     "reading a surface that has drifted from its source"),
```

New text:

```python
     "candidate list that no longer matches the table turns this red rather than leaving the user "
     "reading a surface that has drifted from its source"),
    # ---- AUTHORED 2026-10-15, cc_instruction_l3_reading_file_2026_10_15.md Task 2 ---------------
    # The same tool's second subject, registered in the act that gives the tool that subject.  One
    # run per rendered surface, on the precedent of the per-pair runs of
    # `gen_governing_surface_split.py` below, so each surface the user rules from is guarded.
    ("tools/audit/gen_withheld_family_reading.py", ["--subject", "l3", "--check"],
     "L3's withheld-family reading file re-renders from the boot-pack generator's own authored "
     "verdict table and L3's published candidate list, with L3's charter sentence located at "
     "FRAMEWORK.md and the candidate list's per-group sizing required to equal the table's own "
     "counts. What it guards is that the file the user rules L3's lists from is what the table says, "
     "so an edit to the table without a re-render, a hand edit to the file, or a candidate list that "
     "no longer matches the table turns this red"),
```

Then run `python tools/audit/gen_guard_state.py --check` to scratch and read it: **expected 80 run, the same fourteen
failing, `--subject l3 --check` among the passing**, plus the runner's own *"STALE vs the run"* line for its artifact
(expected until the end-state run). Run `gen_guard_classification.py --check`: **expected the standing STOP naming the
same three tools**; a different message is reported and is not a STOP for this batch.

### (g) Commit the three paths together

`tools/audit/gen_withheld_family_reading.py`, `tools/audit/gen_guard_state.py`,
`ratification_surfaces/cowork_withheld_family_l3_reading.md` — and nothing else (three paths; the guard artifact
waits for the end state). Subject:
`audit(l3): the withheld-family reading file, rendered from the verdict table; the tool's L2 prose moved into its subject entry, L2's file byte-unchanged`.
Push; verify.

**E2:** (a) PASS; (c) clean; (d) byte-identical; (e) PASS and every confirmation reported; (f) the counts as
expected; the commit pushed.

## Task 3 — the close

1. **The `STATUS.md` entries and the forward-bound move, IN THIS ORDER** (read `gen_status_batch_bound.py` whole at
   the object first, ordered first read (11)). **(a)** Write this batch's entries at the top of `STATUS.md`: one pointer
   entry per task that did work — the close entry FIRST, NAMING THIS DISPATCH BY ITS FILE NAME
   (`records/cc/instructions/cc_instruction_l3_reading_file_2026_10_15.md`), each earlier task's entry below it saying
   `Same dispatch`; no figure restated (D-431); **the `Last updated: ` prefix moved from the last batch's close entry
   (the topmost at the tip, naming `cc_instruction_l3_candidate_list_and_verdict_pass_2026_10_14.md`) to your newest
   entry.** **(b)** Re-aim the five authored constants of `gen_status_batch_bound.py`: `BASE_COMMIT` (this batch's last
   task commit before the close), `PREVIOUS_BATCH_DISPATCH` (`cc_instruction_l3_candidate_list_and_verdict_pass_2026_10_14.md`),
   `ACT_DATE` (the day the move runs), `DISPATCH` (`cc_instruction_l3_reading_file_2026_10_15.md`), `TASK` (`Task 3`);
   append your own aiming to `PREVIOUS_AIMINGS` on the convention its comments state (every aiming exactly once; the
   last batch's aiming is already its last row). **(c)** Run `gen_status_batch_bound.py --apply`. **Prediction:** it
   moves **exactly the last batch's five entries** (its close entry and the four `Same dispatch` entries for Tasks 3
   to 0, read at `STATUS.md` at the tip); the two 2026-09-02 entries stay. If it STOPs, restore its passing aim, re-run
   green, report, move nothing by hand. **(d) LAST**, after the final `STATUS.md` edit, regenerate
   `gen_session_start_read_size.py` and confirm its `--check` green. Commit the re-aimed tool,
   `tools/audit/status_batch_bound.json`, `STATUS.md`, `STATUS_ARCHIVE.md` and the read-size artifact together in the
   close.
2. **The report**, `records/cc/reports/cc_report_l3_reading_file_2026_10_15.md`, which decides nothing and recommends
   nothing about any list: both guard states; every commit hash (or a pointer to the git log where it cannot contain
   one); E0 to E2 and A1 to A3 graded; Task 1's four counts and byte-identity; Task 2's (a), (c), (d), (e) and (f)
   results; declared departures; and the plan's tell in one sentence — did this batch produce anything other than the
   landed paths, the fifteen spaces, the tool's edits, the guard enrolment, L3's reading file, the Task 3 files and
   the report? If yes, name it.
3. **The full close appended to `records/cowork/handoff/cowork_away_returns.md`** as a section headed **THE L3
   READING FILE: RENDERED FROM THE VERDICT TABLE FOR THE USER TO RULE, NOTHING WITHHELD, NO PACK, NO ALGORITHM
   CHANGED** (if Task 2 stopped, the heading says so) — the report's content as pointers, and the plan line: **the
   next act is the writing side's — the check of the rendered file, then the three lists put to the user one per
   turn.**
4. **The close does not assert the end state**; one further commit carries it. Commit the close, push, verify; then
   the full guard run in write mode at that tree, the A2 exceptions handled as A2 says, and the one further commit
   with its artifacts, pushed and verified. Re-run `gen_guard_classification.py --check` after it and report the
   message (expected: the standing STOP naming the same three tools).

**E3:** at the tree carrying the close, a fresh full guard run — the A2 prediction (80 run, 20 historical, failing the
fourteen named) — committed only after the run that produced it.

## What this batch does NOT do

- **No withheld identity, no pack, no session, no ruling.** The reading file is a surface for the user's ruling; it
  applies nothing.
- **No change to what any layer computes** as its specification defines it. Every edit is a wording repair inside a
  dormant table of proposals, a reading-tool refactor proven inert for L2, a new rendered surface, or one guard run.
- **No re-render of L2's ruled reading file.** Its UNPLACED heading still cites D-658 for its no-recommendation
  sentence (L.3); it stands as the ruled surface, and this batch neither re-renders nor edits it.
- **No decisions-register entry, no `D-NNN`, nothing in the suspension file.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **`VERDICT_DATE["l3"]`** — owed to the batch that builds L3's pack; `build_subject` STOPs without it.
- **`criterion_block()`'s fixed bullet** (*"its `group` is E — Layer 2, the slicer"*) — owed before an `l3` pack is
  rendered (carried from the last two dispatches).
- **The six drifted register anchors and the eight stale derived `home_section` blocks** — register maintenance;
  cause first (D-669).
- **The ruling write-back** — after the user rules the lists, a dispatch writes any moved verdicts back to
  `VERDICTS["l3"]` and gives `SUBJECTS["l3"]` its `ruling` block, as `cc_instruction_l2_ruling_writeback_2026_09_05.md`
  did for L2.

## The writing side's self-check, run before this dispatch was released (D-434)

1. *Principles.* #6 — one reading-file tool for both subjects, no second renderer; L2's prose moved, not copied (it no
   longer exists in `render()`); one verdict table, one candidate list. #12 — the four fused words' former spellings
   in Task 1's commit subject; L2's ruled file untouched. #13/#18 — every inertness claim proven by a before/after
   comparison (Task 1(c), Task 2(d)); the two new STOPs (criterion terms, sizing equality) turn a silent wrong
   sentence or number into a halt. #19 — the new surface is guarded in the act that creates it. #17f/D-431 — counts
   are rendered from the table and cited, never transcribed.
2. *Conventions.* American English; the vocabulary block precedes first use; the group-F / L3 numbering collision is
   stated where it can mislead, in the dispatch and in the rendered file; *check*, *script*, *generator*, never
   *instrument*.
3. *The bars.* Nothing withheld; no `WITHHELD`, `EXTRAS`, `FROZEN` or `VERDICT_DATE` entry for `l3`; no pack, no
   session; no register entry; no choice question to the user anywhere.
4. *Documentation and algorithm.* Nothing here changes the algorithm as any specification defines it.

*Provenance: Cowork writing side, 2026-10-15 (Stockholm), the sitting booted on entry 399, at tip
`44b22bee63b7ecdd1e6496d15f73ea570216fbf2` read as files; no shell command was run. **Read by the writing side, at the
extent named:** the boot read of entry 291 §4 step 3; entries 291, 398 and 399 whole; the last batch's report whole,
its close whole, and its dispatch at its head (through Task 0), Tasks 1 to 3 and its tail; the L3 ruling record
whole; `.git/HEAD`, both ref files and `.git/logs/HEAD` at the batch's lines; `VERDICTS["l3"]` whole; the generator
at `CRITERION["l3"]`, the table heads (`VERDICT_DATE`, `FROZEN`, `EXTRAS`, `WITHHELD`, `CRITERION`, `VERDICTS`),
`group_title()`, `candidates()`' head and `build_subject()`'s head; `l3_candidate_list.json` at its head and checks and
at the IN, UNPLACED and nearest-OUT candidates; `gen_withheld_family_reading.py` WHOLE; `gen_guard_state.py` at the
reading-file entry, `AUTHORED`'s head and by search; `guard_state.json` at `summary`'s head and the reading-file run;
`FRAMEWORK.md` at the L3 block and by search for the question lines; the L2 reading-file dispatch by its headings.
**NOT read:** the L2 reading file itself, `gen_guard_classification.py`, `gen_status_batch_bound.py`,
`cowork_audit_protocol.md`, and the `ratification_surfaces/` listing.*

## The writing side's check of this dispatch at its sources (recorded per the standing clause and D-434; run 2026-10-15 in a turn of its own, after the user's "continue")

**The objects were current.** At the `tools/audit` listing of 2026-10-15 the reading-file tool, the generator and
`gen_guard_state.py` carried the same modification times as the staged copies the dispatch was written from.

**Checked at the objects and holding:** every single-line anchor of Task 2's seventeen tool edits occurs exactly
once in the tool (the title line, the D-525 line, the group-order line, the ruled-banner line, the first line of §1's
two bullets, §2's first line, §3's heading, the home-document bullet, the population paragraph's `returned` line, the
sizing line, §5's opening, the `LIST_HEADINGS` lookup, §6's first bullet, the two §7 lines and the §8 line). **Every
L2 string Edit 1 moves equals the tool's line character for character**: the §1, §2, §3 and §6 lines were searched
as literals in both files — each tool line once in the tool, and twice in the dispatch (in Edit 1 and in the old
text), the dispatch's surplus being exactly the four lines L3's own prose shares with L2's. The two concatenated
strings (`empty_terms_line`, `bound_tail`) split at the same places as the tool's source and, for `bound_tail`, the
f-string's value (`tools/audit/l2_candidate_list.json`, `SUBJECTS["l2"]["candidate_list"]`) is written in literally.
Task 1's counts — `answer tohow` 11, `answer towhich` 1, `belongs to thebounded-context` 1,
`belongs to theconfidence` 2 — all inside `VERDICTS["l3"]`. Task 2(f)'s two-line anchor occurs once.
`FRAMEWORK.md`'s bold L3 question needle occurs once. `CRITERION["l3"]`'s twenty groups omit R. The
`gen_governing_surface_split.py` runs stand below the reading-file entry in `AUTHORED`. The last batch's five
`STATUS.md` entries. The L3 ruling record names no oracle passage, and its §2 carries Ruling 84's
own-list rule as quoted. `CLAUDE.md` Conventions' decision-surface order: step 5 requires a recommendation, step 8
records D-658's fourth requirement superseded.

**Corrected at its site:** Task 2(c) quoted a working-tree `git diff` command and called it denied in the same
breath; it now orders only the `git show` copy and a file-tools comparison.

**Not established by this check:** that the multi-line old texts match beyond their anchor lines (they were copied
from the tool's own text as read, and the exactly-once rule turns any mismatch into a STOP); that
`gen_guard_classification.py`'s message is unchanged by a second run of the same tool (Task 2(f) reports it, not a
STOP); the A2 failing names after the first (relayed from the last report).
