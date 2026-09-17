# CC REPORT — the root record files moved into `records/`; references fixed; STOPPED at Task 5(c) on a guard refusal, 2026-09-17

**Dispatch executed:** `records/cc/instructions/cc_instruction_root_records_move_2026_09_17.md` (second issue),
blob **`ce2290509e905ae41d3422c06c937b3d3cbe9f98`**.

## 0. THE STOP — read this first

**The batch STOPPED during Task 5(c), before any commit, on a guard refusal.** The dispatch makes any guard refusal a
STOP ("If a guard refuses anything, STOP and report the refusal text verbatim."). The refused command was an
auxiliary one this session added. The dispatch did not order it, and no task needed it: a `git diff --no-index
--stat` over the scratch files holding the nine captured guard messages, meant only to size them before reading
them. The refusal text, verbatim:

```
`git diff` with no commit hash is aimed at a working-tree path ("$S/c_$t.txt", 2>/dev/null). D-253 permits git only for read-only OBJECT queries named by an explicit hash, because a content-addressed read errors loudly rather than returning silently-wrong content; a working-tree diff is not one. Use `python tools/audit/changed_paths.py`, or name the commits.
```

**State at the stop.** The dispatch says: do not undo the moves; report the state; the user decides.

- **No commit was made and nothing was pushed.** `git rev-parse HEAD` → `5d24edb565b2e0e9efc92e082c163112bd97087f`
  (the base). Commits 1, 2 and 3 do not exist.
- **Staged:** `python tools/audit/changed_paths.py --staged` printed `978 changed path record(s) [staged]`. Every
  record is a rename (`R`), and nothing else is staged. The capture is blob
  `4e959e003bbdd5b51e336ee669bd761eba00d7fc`. That is **the same blob** as the Task 2 capture, so the staged area
  has not changed since Task 2.
- **Working tree:** `python tools/audit/changed_paths.py` printed `1607 changed path record(s) [worktree]`. The
  capture is blob `fd3a25f41083e97d29ea6a5da0f9ae3b9d7dba1b`. Its records other than renames and untracked paths
  are the Task 3/4/5(a) edits listed in §4–§6, plus the two pre-existing modifications
  (`docs/research_papers/BIBLIOGRAPHY.md` and `docs/research_papers/README.md`, both ` M` at Task 0). Two records
  read `RM` (renamed in the index, modified in the working tree):
  - `cowork_handoff.md -> records/cowork/handoff/cowork_handoff.md` — this batch's Task 4 edits;
  - `cowork_handoff_entry_one_hundred_and_eighty_eight.md -> records/cowork/handoff/…` — its working-tree
    modification existed before this batch (` M` at Task 0). It is not this batch's work.
- **Not done:** Task 5(c) (no guard write mode was run), Task 5(d), Task 6 (Commits 1–3, content proof, STATUS.md
  entry, forward bound, push).

**What resuming would involve, for the user to decide.** The index holds exactly Commit 1's content. §7 below
predicts that the Task 6 content proof would STOP anyway: several newly failing guards measure sizes or hashes,
so their rewrites would not be pure name-to-path changes.

---

## 1. TASK 0 — start state

- **(a)** `git hash-object -w records/cc/instructions/cc_instruction_root_records_move_2026_09_17.md` →
  **`ce2290509e905ae41d3422c06c937b3d3cbe9f98`**. Git warned that LF will be replaced by CRLF. The dispatch was read
  once with the Read tool, just before this; it was not re-read from the blob.
- **(b)** `git rev-parse --abbrev-ref HEAD` → `master`; `git rev-parse HEAD` →
  `5d24edb565b2e0e9efc92e082c163112bd97087f`. This is the base, so there was no STOP.
- **(c)** `python tools/audit/changed_paths.py` → printed `566 changed path record(s) [worktree]`. The whole output
  is in Appendix A (blob `1e6a70be54df1850f40a55f5fae6a086abe5acd9`).
- **(d)** `python tools/audit/gen_guard_state.py --check` → exit 1, printed
  `81 guard(s) run, 15 failing, 4 not run, 16 historical record(s)`, and its first line was
  `STALE vs the run: guard_state.json does not re-derive`. That was reported and not corrected. The whole output is
  in Appendix B (blob `0c5a2086a0e1ba158c655323e5e14331a5b9bbad`).

## 2. TASK 1 — the population and its destinations

**(a) The mapped files.** The population is the map's §1.1–§1.4 lists (map blob
`aafb7591f7e0bbcde89c97e5f8baf89985693bdb`), and those lists are the per-member enumeration with T / U marks. The
map's own summary gives 110 + 91 + 571 + 372 members, and the check batch
(`tools/audit/reference_map_check.json`, check 4) found every list and mark equal to the repository. This batch
re-confirmed each pattern with one Glob (Glob recursed, as the map records, and returned no root file outside the
lists):

| Pattern | Glob total | Minus non-root matches | = root |
|---|---|---|---|
| `cowork_handoff*.md` | 112 | `records/cowork/handoff/` entries 189 and 190 | 110 |
| `cowork_ruling*.md` | 93 | the two `ratification_surfaces/` files the map names | 91 |
| `cc_instruction_*.md` | 574 | the three dispatches already under `records/cc/instructions/` | 571 |
| `cc_*.md` | 948 | those three, plus the two reports under `records/cc/reports/` | 943 = 571 + 372 |

The shell loop that moved the tracked files counted them at the time (§3). The untracked members are the 171 `U`
lines of the map (§1.3: 3; §1.4: 168). Those same 171 names were passed to the move loop.

**(b) The five added files** all exist at the root and are all tracked (`git ls-files` returned all five):
`cowork_owner_rulings_2026_08_07.md`, `cowork_pending_rulings_2026_08_02.md`,
`cowork_document_route_rulings_2026_08_08.md`, `cowork_instruction_return_session.md`, `cowork_away_returns.md`.
One brace-Glob over `cowork_owner_rulings_*.md`, `cowork_pending_rulings_*.md`,
`cowork_document_route_rulings_*.md`, `cowork_instruction_*.md` and `cowork_away_returns.md` returned exactly those
five, so no unnamed file was found.

**(c) Destinations** are as the dispatch's table sets them. The folders `records/cowork/rulings/` and
`records/cowork/instructions/` were created (`mkdir -p`; declared in §9).

**Collision check.** Before the move, `records/` held seven files:
- `records/cc/instructions/`: `cc_instruction_root_records_reference_map_2026_09_16.md`,
  `cc_instruction_reference_map_check_2026_09_17.md`, `cc_instruction_root_records_move_2026_09_17.md`;
- `records/cc/reports/`: `cc_report_root_records_reference_map_2026_09_16.md`,
  `cc_report_reference_map_check_2026_09_17.md`;
- `records/cowork/handoff/`: `cowork_handoff_entry_one_hundred_and_eighty_nine.md`,
  `cowork_handoff_entry_one_hundred_and_ninety.md`.

A Glob for those seven names found them only under `records/`, so none collides with a population member. The move
loop for untracked files also tested each destination before moving, and reported no collision.

## 3. TASK 2 — the move and its proof

**Tracked files.** `git mv` was run in chunks of 80, over lists taken from `git ls-files -z` with root-only glob
pathspecs. The loop printed:
- `records/cowork/handoff/` 111 (the 110 of §1.1, plus `cowork_away_returns.md`);
- `records/cowork/rulings/` 94 (the 91 of §1.2, plus three);
- `records/cowork/instructions/` 1;
- `records/cc/instructions/` 568;
- `records/cc/reports/` 204.

111 + 94 + 1 + 568 + 204 = **978**.

**Untracked files.** `mv -n` was run over the map's 171 `U` names (the loop printed `moved 171 fail 0`):
- the three `cc_instruction_*` files went to `records/cc/instructions/`;
- the other 168 went to `records/cc/reports/`.

None was added to git.

**Proof.**
- `changed_paths.py --staged` printed `978 changed path record(s) [staged]`, and every record is an `R` from a root
  name to its destination (blob `4e959e003bbdd5b51e336ee669bd761eba00d7fc`). Nothing else is staged.
- The untracked files are at their destinations. Glob `records/cc/reports/*.md` returned 374 = 204 tracked + 168
  moved + 2 pre-existing. `git ls-files` over the root patterns returned nothing. The Task 2 working-tree capture
  lists no root `cc_` or record file other than the rename records.
- **Working-tree difference from Task 0(c).** The Task 2 capture (blob `dfdf41675d56fab90ce075739b0d57fee27b48fe`)
  printed `1552 changed path record(s) [worktree]`. That total is made of:
  - 2 ` M` (the two `docs/research_papers/` files);
  - 978 rename records (one of them `RM`, the pre-modified handoff entry 188);
  - 177 untracked records under `records/`;
  - 395 other untracked records, the same set Task 0(c) listed besides the root `cc_` files and `records/`.

  The untracked records under `records/` are:
  - 167 moved untracked files that git shows;
  - the 7 pre-existing `records/` files, which now appear one by one because `records/` is partly tracked;
  - **three `cc_e2d_*` reports that are newly visible.** `.gitignore` line 116 (`/cc_e2d_*.md`) was anchored to the
    root, so once they moved it no longer covered them. Task 4 changes that line. After the change the three are
    hidden again: the stop capture no longer lists them.

  167 + 7 + 3 = 177. `cc_foundation_stage0_report.md` stays hidden by another ignore rule: it was absent from
  Task 0(c) and is absent now. This difference is the class the dispatch allows, so there was no STOP.

## 4. TASK 3 — code

Each changed line is given before → after. The rule-case is **P** for a path, **S** for a scan directory, **A** for a
prefix rule's directory anchor, and **K** for a table key.

**Group A (live opens of a moved file):**

1. `tools/audit/decisions/apply_soft_discard.py:68` (P)
   `RULING = ROOT / "cowork_rulings_2026_08_16_preparation_return.md"` →
   `RULING = ROOT / "records" / "cowork" / "rulings" / "cowork_rulings_2026_08_16_preparation_return.md"`
2. `tools/audit/decisions/apply_residue_discard.py:83` (P)
   the same form, for `cowork_rulings_2026_08_17_residue_sitting.md`
3. `tools/audit/decisions/gen_retired_subject_moves.py:70` (P)
   the same form, for `cowork_rulings_2026_08_16_preparation_return.md`
4. `tools/audit/decisions/gen_phase1w_legacy_verification.py:142` (P)
   `'where': 'cc_instruction_phase1m_dispositions_and_measurements.md',` →
   `'where': 'records/cc/instructions/cc_instruction_phase1m_dispositions_and_measurements.md',`
5. `tools/audit/gen_phase1_gate_readers.py:198` (P)
   `path = os.path.join(ROOT, RULING)` → `path = os.path.join(ROOT, "records", "cowork", "rulings", RULING)`
   - `RULING` stays a bare name, because it is also written into the tool's output as a label (line 441).
   - The regular expression at line 126 matches **base names**, so it is not a root anchor, and it was not edited.
6. `tools/audit/gen_ratified_document_check.py:98` (P)
   the same form as item 1.
   - `RULING_PATH` (line 99), which is read at `RULING_PINNED_AT`, is a fixed-commit read and was not edited.
7. `tools/audit/gen_retirement_caller_check.py:153–155` (P)
   `RULING`, `READING_RULING` and `CALLERS_RULING` each gained `"records" / "cowork" / "rulings" /` after `ROOT /`.
8. `tools/audit/gen_rulings_sort.py:111` and `:118` (P)
   `RULING` and `SORT_RULING` gained the same prefix. The output records `path.name`, which is unchanged.
9. `tools/audit/gen_sole_carrier_subclass.py:106` (P)
   the same form as item 1.
10. `tools/audit/gen_deciding_act_recovery.py:83` (P)
    the same form as item 1.
    - The filter at line 358 runs over `ls-tree` at `PINNED_COMMIT`, a fixed-commit read, and was not edited.
11. `tools/audit/gen_discard_reach_split.py:130` (P)
    `path = os.path.join(ROOT, RULING)` → `path = os.path.join(ROOT, "records", "cowork", "rulings", RULING)`
    - `RULING` is also an output label (line 433).
    - **`REPORT = "cc_report_preparation_third.md"` (line 86) was NOT edited.** It is read from git at the recorded
      commit in `--check` (map group F). Declared consequence: once the move is committed, a plain write run at a
      new HEAD will STOP, because the report is not at its root path at that commit. Making it follow the commit
      would need more than a path.

**Group B (root scans):**

12. `tools/audit/decisions/gen_decision_harvest.py`
    - line 105 (K):
      `"cowork_handoff.md", "cowork_handoff_archive.md", "OPEN_ITEMS.md",` →
      `"records/cowork/handoff/cowork_handoff.md", "records/cowork/handoff/cowork_handoff_archive.md", "OPEN_ITEMS.md",`
    - lines 152–153 → 152–156 (S): the root `cowork_*.md` glob with its exclude became a sorted union of:
      - the root glob;
      - `records/cowork/handoff` (excluding the two governing handoff paths);
      - `records/cowork/rulings`;
      - `records/cowork/instructions`.
    - line 166 (S): `cc = md_glob("", "cc_*.md")` became a sorted union of `records/cc/instructions` and
      `records/cc/reports`.
    - **Declared:** the scanned folders also hold the seven files that were never at the root, and this report, so
      a future harvest's population includes them.
13. `tools/audit/gen_artifact_inventory.py`
    - line 231 (K): `"cowork_handoff_archive.md"` → `"records/cowork/handoff/cowork_handoff_archive.md"`
    - lines 248–249 (A): `at_root_prefixed(<five ruling prefixes>)` became a lambda:
      `posixpath.dirname(p) == "records/cowork/rulings"` and one of the same five prefixes.
    - lines 254–255 (K, A): the names became `"records/cowork/handoff/cowork_handoff.md"` and
      `"records/cowork/handoff/cowork_away_returns.md"`. `at_root_prefixed("cowork_instruction_")` became an anchor
      on `records/cowork/instructions`.
    - line 259 (A): `at_root_prefixed("cowork_")` became `any_of(` that rule and an anchor on
      `records/cowork/handoff` with the `cowork_` prefix `)`. That keeps the handoff entries in the class they had at
      the root.
    - line 268 (A): `at_root_prefixed("cc_instruction_")` became an anchor on `records/cc/instructions`.
    - line 272 (A): `at_root_prefixed("cc_")` became an anchor on `records/cc/reports`.
    - **Declared, not edited:** the class descriptions still read "repository-root files …". Changing that prose
      is beyond the allowed rule-cases.
14. `tools/audit/gen_filing_convention_application.py`
    - line 67 (S): the five `records/…/*.md` globs were added after `"*.md"`.
    - lines 145, 150, 153, 158, 162, 166, 170 (K): the seven `VERDICTS` keys gained their `records/cc/…/` prefix.
15. `tools/audit/gen_evidence_pin_membership.py:186–188` (S)
    `ruling_records()` now lists `records/cowork/rulings` and returns `"records/cowork/rulings/" + fn`. The output
    therefore carries the path where it carried the bare name.
16. `tools/audit/gen_ratification_surface_set.py:109` (S)
    `for base in ("", RATIFICATION_DIR):` → `for base in ("", RATIFICATION_DIR, "records/cowork/rulings"):`
    - Reason: `cowork_pending_rulings_2026_08_02.md` is a class member (`ratification_surface_set.json:31`).
    - **Declared:** on a re-run its `"filed"` field becomes true (`bool(base)`), because the file no longer sits at
      the root.
17. `tools/audit/decisions/gen_reads4_oi326_application.py:228` (S)
    `repo_matches("*phrase*boundary*.md")` became a sorted union with
    `repo_matches("records/cc/*/*phrase*boundary*.md")`. The added glob finds exactly the two moved files.

**Group D:**

18. `tools/audit/reaim_ratification_surface_paths.py`
    - line 100 (K): `"cowork_handoff.md": {` → `"records/cowork/handoff/cowork_handoff.md": {`
    - line 149 (A): `f.startswith("cc_instruction_")` → `f.startswith("records/cc/instructions/cc_instruction_")`
    - **Declared latent:** `f in _MEMBERS` (line 144) compares bare member names, so a re-taken census naming
      `records/cowork/rulings/cowork_pending_rulings_2026_08_02.md` as a citing file would get no verdict.
19. `tools/audit/gen_specification_document_set.py` (K)
    The eleven `GRADES` keys naming a moved file each gained their `records/…/` prefix, because `ARCHITECTURE.md`
    changed (§5). The keys:
    - `cc_adoption_measurement_report.md`
    - `cowork_handoff.md`
    - `cc_instruction_notation_switch.md`
    - `cowork_rulings_2026_08_11_fourteenth_stop.md`
    - `cc_layer1_impl_report.md`
    - `cc_layer1_coverage_report.md`
    - `cc_layer2_impl_report.md`
    - `cc_layer2_audit_dossier.md`
    - `cc_layer3_wiring_report.md`
    - `cc_tonicization_modulation_metric_dossier.md`
    - `cowork_rulings_2026_08_09_second_stop.md`

    **Declared, not edited:** the grade reason at line 412 still quotes "`cowork_handoff.md`".
- **Not edited, per the map's own reading:**
  - `gen_status_batch_bound.py` (substring match still holds);
  - `process_check.py`;
  - `shell_read_guard.py`;
  - `gen_recognizer_establishment_sort.py`;
  - `gen_status_archive_pass.py` (`RETURNS` is a text match).
- **Group C:** none was edited.

**Group E:**

20. `tools/audit/gen_discard_records.py:118` (P)
    `"surface": "cowork_away_returns.md",` → `"surface": "records/cowork/handoff/cowork_away_returns.md",`

**Grep for the five added names** over code under `tools/`, `src/`, `idiom_discovery/` and `hooks/`.
- `src/`, `idiom_discovery/` and `hooks/` gave no hit.
- In `tools/`, the only openers were items 13 and 20.
- Every other hit is a comment or a message string:
  - `gen_finish_line_item1_routes.py`
  - `gen_artifact_inventory_surface.py`
  - `gen_home_classification.py`
  - `gen_gating_row_sizing.py`
  - `gen_governing_surface_split.py`
  - `gen_oi357_partial_signature_establishment.py`
  - `gen_july_screen.py`
  - `gen_phase1_gate_readers.py:126`, a base-name regular expression
  - `gen_phase1_completion_inventory.py`
  - `gen_status_batch_bound.py`
  - `gen_status_archive_pass.py`
  - `apply_soft_discard.py:330`

`buildscripts/` was not searched for the five names, and that is declared.

**No `src/` file was edited.** The `src/` string literals the map names at §2(b).4 are labels, not openers.

**Existence.** One Glob over all 16 new path literals of items 1–20 returned exactly those 16 files. The Glob in
item 17 returned the two phrase-boundary files.

## 5. TASK 4 — documents

**The rule applied.** In each LIVE document, every bare mention of a moved file became its destination path.
**Nothing else on any line was changed.**

**Which names count as moved.** A name counts as moved only if `git ls-files -c -o` found it at its destination
after the move:
- 95 of the cowork names checked and 265 of the `cc_` names checked were found;
- the rest — `cowork_handoff_entry_66_pending.md`, `cowork_rulings_2026_08_27_ledger_precondition_sitting.md`,
  `cc_instruction_X.md`, and the two `ratification_surfaces/` names — are not moved files, and were left alone.

**How the replacement was done.** Each replacement used the Edit tool with `replace_all` for one name in one file.
That departs from "one changed passage at a time", and is declared in §9.

**Checks before editing.**
- A Grep for occurrences preceded by a path or name character found only the prefixed occurrences handled below.
- After editing, a Grep for any bare mention left in the LIVE set returned only the intended exceptions.
- A Grep for a doubled `records/…records/` prefix returned nothing.

**The LIVE documents edited:** `ARCHITECTURE.md`, `CLAUDE.md`, `BUILD_AND_TEST.md`, `STATUS.md`, `OPEN_ITEMS.md`,
`DEFECT_TYPES.md`, `EMPIRICAL_FINDINGS_LEDGER.md`, `FRAMEWORK.md`, `PHASE_CONSTRAINTS_AND_STOP_RULES.md`,
`cowork_audit_protocol.md`, `cowork_confidence_contract.md`, `cowork_derived_specification_l0_l1_2026_09_03.md`,
`cowork_design_doc_template.md`, `cowork_engage_arc_plan.md`, `cowork_joint_estimator_architecture.md`,
`cowork_layer3_keymode_design.md`, `cowork_layer4_chordsymbol_design.md`, `cowork_layer5_engagement_design.md`,
`cowork_layer5_function_design.md`, `cowork_layer6_grouping_design.md`, `cowork_notation_adoption_increment.md`,
`cowork_notation_output_contract.md`, `cowork_phrase_boundary_design.md`, `cowork_score_census.md`,
`cowork_stage5_fitter_design.md`, `cowork_target_architecture.md`, `cowork_voiceleading_axis_design.md`,
`docs/implementation_roadmap.md`, `docs/scoring_model.md`, `docs/score_inventory.md`,
`docs/unified_analysis_pipeline.md`, `tools/REPRODUCIBILITY.md`, `tools/extra_scores_registry.json`,
`records/cowork/handoff/cowork_handoff.md`.

LIVE documents with no bare mention of a moved file, and therefore unedited: `cowork_bounded_context_design.md`,
`cowork_oi200_perspective_inventory.md`, `cowork_prefit_gates.md`, `cowork_joint_estimator_factorization.md`,
`cowork_evidence_inventory.md`, `cowork_progression_schema_dictionary.md`, `cowork_layer2_slicing_design.md`,
`cowork_layer1_note_model_design.md`, `cowork_progression_schema_design.md`, `cowork_idiom_entry_mapping.md`,
`cowork_prune_pass_checklist.md`, `docs/research_papers/README.md`.

**The names each document carried** are listed per line by the pre-edit Grep. The edit rule maps each name to a
fixed path, so every changed line equals its old line once `records/<folder>/` is removed from before each moved
name. The per-line before/after is therefore the Grep listing together with that rule. **No exact before/after
listing per line was produced, because the batch stopped before the Task 6 diff that would show it.**

**`ARCHITECTURE.md`.** Eleven names were replaced, each inside an existing sentence. No delegation was added,
removed or reworded.

**Exceptions, each a judgment, declared:**
1. **Quoted past commands left as written.** Rewriting these would make a true record of a past act false. This
   applies to fixed-commit reads the principle Task 3 states for code, and the per-citation constraint OI-287
   states.
   - `records/cowork/handoff/cowork_handoff.md` line 7572: `git hash-object cowork_handoff.md`.
   - Line 7723: `git show dcbfa5fe32:cowork_handoff.md`.
   - Line 8336: `git show 3cfb220b1d:cowork_handoff.md`.
   - `OPEN_ITEMS.md` line 278: the quoted denied command path `` `C:\s\MS\cowork_away_returns.md` ``.

   Each was replaced with the rest of its file and then restored, so its net change is zero.
2. **`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` (LIVE in the map) was NOT edited.**
   - `open_items/OI-285.md:108–109` records that such surfaces "are the text the user read, and a ratification
     surface that has been tidied is no longer the surface that was ratified (**D-249**)".
   - Its nine mentions of moved files stay as root names. **For the user:** keep it as written, or authorize the
     path change.
3. **`docs/research_papers/BIBLIOGRAPHY.md` (LIVE) was NOT edited.**
   - Its only mention (line 136, `cowork_handoff_entry_one_hundred_and_sixty_two.md`) is absent from the file at
     the base commit.
   - So the mention exists only in the file's pre-existing **uncommitted** modification, which is another session's
     work in progress. Editing and committing it would commit that work.

**The decisions register data.** `tools/audit/decisions/backbone_decisions.json` had four `home` values, and only
the `home` value changed on each line:
- line 5581: `cowork_handoff_archive.md:3082` → `records/cowork/handoff/cowork_handoff_archive.md:3082`;
- lines 14651, 14669, 14687: `cowork_rulings_2026_08_25_v1_sufficiency_sitting.md:<range>` →
  `records/cowork/rulings/cowork_rulings_2026_08_25_v1_sufficiency_sitting.md:<range>`.

**`.gitignore` line 116:** `/cc_e2d_*.md` → `/records/cc/reports/cc_e2d_*.md`.

**DATED, GENERATED and FROZEN documents:** none was hand-edited.

## 6. The UNDECIDED list — UNDECIDED files that mention a moved file by its root name

**How it was taken.** A Grep ran over the map's UNDECIDED files for a bare name matching the moved families
(`cowork_handoff*`, `cowork_ruling(s)_*`, the three other ruling prefixes, `cowork_instruction_return_session`,
`cowork_away_returns`, `cc_*`). **The list is by that pattern.** A file is listed if a name of those families
appears in it; whether each such name is itself a moved file was not checked file by file.

**Root, and the moved `records/cowork/handoff/cowork_away_returns.md`** (34 files; Grep printed "501 total
occurrences across 34 files"):
`cowork_joint_key_chord_design.md`, `cowork_framework_phase_opening_surface_2026_08_26.md`,
`cowork_l2_boot_list_surface_2026_09_05.md`, `cowork_curated_boot_list_draft_2026_08_19.md`,
`cowork_l1l3_stabilization_plan.md`, `cowork_gateA_unification_design.md`, `cowork_fb_redesign_design.md`,
`cowork_cross_layer_transfer_list.md`, `cowork_defense_clause_ends_2026_09_08.md`,
`cowork_key_drift_research_grounding.md`, `cowork_declared_readings_surface_2026_08_27.md`,
`cowork_l1l4_review_charter.md`, `cowork_factorization_desk_simulation.md`,
`cowork_claude_md_live_rule_classification_2026_09_08.md`, `cowork_l2_task_b_slice_derivation_2026_09_05.md`,
`cowork_layer3_keymode_impl_design.md`, `cowork_phase1_commissioning_surface_2026_08_11.md`,
`cowork_layer3_reachback_design.md`, `cowork_l2_score_set_read_2026_09_05.md`,
`cowork_placement_sample_surface_2026_08_27.md`, `cowork_l2_first_pass_extracts_derivation_2026_09_05.md`,
`cowork_redraw_findings_surface_2026_08_27.md`, `cowork_register_blocker_surface_2026_08_28.md`,
`cowork_register_rule_c_suspension_2026_08_28.md`, `cowork_research_list_disposition_surface_2026_08_29.md`,
`cowork_specification_reconstruction_plan_successor_2026_08_21.md`, `cowork_stopped_strata_surface_2026_08_27.md`,
`cowork_running_order_2026_09_01.md`, `cowork_take_rule_surface_2026_08_27.md`, `cowork_term_theory_grounding.md`,
`cowork_types_header_design.md`, `cowork_tpc_capability_design.md`, `cowork_unit_question_surface_2026_08_28.md`,
`records/cowork/handoff/cowork_away_returns.md`.

**`ratification_surfaces/`** (11 files):
`cowork_d580_transfer_fact_gathering_2026_08_09.md`, `cowork_standing_treatment_surface_2026_08_16.md`,
`cowork_sizing_tests_reading.md`, `cowork_sizing_pack_leak_list_reading.md`, `cowork_comparison_l0_l1_reading.md`,
`cowork_pruning_and_satellites_surface_2026_09_08.md`, `cowork_reserved_word_inventory_2026_08_09.md`,
`cowork_restructuring_period_start_decision_surface.md`, `cowork_comparison_harmony_boundary_reading.md`,
`cowork_discard_reach_surface_2026_08_16.md`, `cowork_first_deriving_subject_surface_2026_08_31.md`.

**`docs/`** (8 files):
`stage4d_local_modulation_design.md`, `scoped_joint_design.md`, `beam_widening_design.md`, `decoder_design.md`,
`architecture_joint_inference.md`, `key_path_design.md`, `precision_metric_design.md`, `back_half_design.md`.

**`reading_pass/`** (5 files):
`population.md`, `l2_slice_reading_progress_companion.md`, `l2_slice_reading_progress.md`, `continuation.md`,
`candidacy_upgrades.md`.

**`open_items/`.** Grep printed "670 total occurrences across 280 files". The per-file listing was truncated at 250
in this session's output, **so the 280 files are not named here.** The same Grep, without truncation, names them.

**`tools/notation_seams/README.md` and `tools/robust_stop/README.md`:** no match.

## 7. TASK 5 — as far as it ran

**(a)**
- `python tools/audit/decisions/gen_decisions_register.py` → `wrote 20 files: DECISIONS.md (the index, 861 lines)
  + 19 group files under decisions/ (477 decisions)`. The files it changed on disk are `DECISIONS.md`,
  `decisions/group_C.md` and `decisions/group_T.md`, per the stop capture.
- `--check` → `the register matches the data (20 files: the index + 19 group files)`.
- `gen_cluster_dispositions.py` was located by Glob at `tools/audit/decisions/`. Its `--verify` exited 1, as it
  also did at Task 0 (FAIL), and its full output is blob `9cfcddcbc553da8f804aafe0748025ebdcf229e4`.
  - **43 of its `verbatim NOT FOUND` lines are attributable to this batch:** D-199, D-249, D-252, D-253, D-254,
    D-294, D-416, D-640 to D-658, D-660 to D-664, and D-666 to D-677.
  - A Grep of `backbone_decisions.json` shows that every one of those entries has a `verbatim` field quoting a
    moved file by its root name. Task 4 changed those names to paths at the homes, but the dispatch limited the
    data edit to `home` values.
  - Its `LINE DRIFT` lines were not caused by this batch, because no edit added or removed a line.
  - The guard's result is unchanged (FAIL), but its content widened.

**(b)** `python tools/audit/gen_guard_state.py --check` (blob `d3774d3735639fcf8a604ee5d357a94933f2305f`) printed
`81 guard(s) run, 24 failing, 4 not run, 16 historical record(s)`, again with the `STALE vs the run` first line.

- **The 15 guards that failed at Task 0 still fail.**
- **9 guards passed at Task 0 and fail now.** Each check was run once more on its own, with the message given here:

| Guard | Message |
|---|---|
| `gen_discard_records.py --check` | `STALE: tools/audit/discard_records.json does not re-derive from the record` |
| `gen_specification_document_set.py --check` | `STALE: specification_document_set.json does not re-derive` |
| `gen_rulings_sort.py --check` | `FAIL: the rulings sort does not re-derive: …rulings_sort_classification.json`, and the same for `ratification_surfaces\cowork_rulings_sort_surface_2026_08_16.md` |
| `gen_claude_md_finer_archive.py --check` | `FAIL: the finer archive record does not re-derive: tools\audit\claude_md_finer_archive.json` |
| `gen_post_split_archive.py --check` | `FAIL: the post-split archiving record does not re-derive: tools\audit\post_split_archive.json` |
| `gen_session_start_read_size.py --check` | `STALE vs the measurement: session_start_read_size.json does not re-derive` |
| `gen_defense_share.py --check` | `STALE vs the measurement: defense_share.json does not re-derive` |
| `gen_derivation_boot_pack.py --check` | `STALE: the derivation boot pack does not re-derive` / `derivation_boot_pack.json does not re-derive` |
| `gen_claude_md_prune_backlog.py --check` | `FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json` |

**(c) Not run, because of the STOP.** Prediction for the user, labeled as a PREDICTION and not measured:
- `gen_session_start_read_size.py` and `gen_defense_share.py` measure the sizes of `CLAUDE.md` and `STATUS.md`,
  which Task 4 lengthened. Their rewrites would change measured values, not only names, which fails the Task 6
  proof.
- `gen_derivation_boot_pack.py` covers two boot-pack members that Task 4 edited (`cowork_design_doc_template.md`
  and `cowork_audit_protocol.md`). Its packs are FROZEN under a hash check.
- `gen_rulings_sort.py` would rewrite a ratification surface, `cowork_rulings_sort_surface_2026_08_16.md`.

## 8. What was not done

- No commit, stage (beyond the Task 2 `git mv`) or push.
- No `STATUS.md` entry, and no forward bound. The bound would take `BASE_COMMIT` = Commit 2. Because it would read
  the entries as edited at that commit, the Task 4 edit to `STATUS.md` line 8 would not break its verbatim match.
- No `src/` file, build or test was touched or run.
- No DATED, UNDECIDED or FROZEN document was edited.
- No file was renamed. No moved untracked file was added to git.

## 9. Declared departures and bounds

1. **The guard refusal (§0).**
2. **Edit with `replace_all`**, one name per call per file. The dispatch says one changed passage at a time.
3. **`mkdir -p`** of the destination folders before `git mv`.
4. **Several Greps and Globs ran from the repository root with a file-name filter.** ripgrep and Glob still walk the
   tree to apply such a filter, so they may have entered the excluded folders:
   - the LIVE-set and UNDECIDED-set Greps;
   - the doubled-prefix Grep over `*.{md,json,py}`;
   - the recursive root Globs of Task 1.

   No path under an excluded folder appears in any result used here.
5. **`git show 5d24edb565:docs/research_papers/BIBLIOGRAPHY.md`** was written to a scratch file and read there, to
   check whether that one mention existed at the base.
6. **`git hash-object -w`** was run on nineteen scratch captures, to give them the blob identities cited here.
7. **`DECISIONS.md` was read only to line 60** at session start. `STATUS.md` was read whole.
8. **The first Task 0(c) command failed** on a bad temporary path, before writing anything (the shell refused the
   path). It was re-run into the scratchpad.
9. **Report totals.** Every total above is a tool's printed figure or a sum of named members, except these, which
   are counted from this session's own command output: the 111 / 94 / 1 / 568 / 204 printed by the move loop, and
   the 95 and 265 printed by the existence loops.

**Rows the self-check would ask for.** These were not written: the dispatch authorizes no row, and the batch
stopped.
- (i) the 43 `verbatim` quotes in the decisions register that no longer match their homes;
- (ii) the stale "repository-root files" class descriptions in `gen_artifact_inventory.py`;
- (iii) the `gen_discard_reach_split.py` write-mode STOP once the move is committed;
- (iv) the unedited phase-definition surface's nine root-name pointers;
- (v) `BIBLIOGRAPHY.md`'s uncommitted mention.

---

## Appendix A — Task 0(c), `python tools/audit/changed_paths.py`, whole (blob `1e6a70be54df1850f40a55f5fae6a086abe5acd9`)

The capture is 567 lines: 566 path records followed by the tool's summary line,
`566 changed path record(s) [worktree]`. **It is kept in the object store rather than retyped here**, because a
hand transcription of 567 lines is exactly the risk #17(f) names. `git cat-file blob
1e6a70be54df1850f40a55f5fae6a086abe5acd9` prints it byte for byte. Its non-`scratch_artifacts/` records:

```
 M	cowork_handoff_entry_one_hundred_and_eighty_eight.md
 M	docs/research_papers/BIBLIOGRAPHY.md
 M	docs/research_papers/README.md
??	Claude outputs/
??	Codex research inventory/
??	<164 root cc_*.md report files and the 3 cc_instruction_second_backup_* dispatches — the U members of map §1.3/§1.4 less the four ignored ones>
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/
??	<387 scratch_artifacts/ records — capture lines 177–563>
??	tools/audit/check_reference_map.py
??	tools/audit/derivation_exemplars/
??	tools/audit/reference_map_check.json
566 changed path record(s) [worktree]
```

(The two `<…>` lines summarize runs of records; they are not tool output. The four ignored U members are
`cc_foundation_stage0_report.md` and the three `cc_e2d_*` reports.)

## Appendix B — Task 0(d), `python tools/audit/gen_guard_state.py --check`, whole (blob `0c5a2086a0e1ba158c655323e5e14331a5b9bbad`)

```
STALE vs the run: guard_state.json does not re-derive
  [PASS] tools/audit/register_lint.py 
  [PASS] tools/audit/index_status_lint.py --check
  [PASS] tools/audit/gen_arm_comment_sweep.py --check
  [PASS] tools/audit/local_patches_check.py 
  [PASS] tools/audit/local_patches_check.py --establish --check
  [PASS] tools/audit/guard_armed_check.py 
  [PASS] tools/audit/process_check.py --establish --check
  [PASS] tools/audit/shell_read_guard.py --establish --check
  [PASS] tools/audit/output_encoding.py --establish --check
  [PASS] tools/audit/changed_paths.py --establish
  [PASS] tools/audit/claude_md_rule_triage.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --establish --check
  [PASS] tools/audit/instrument_arm_declaration_effect.py --check
  [FAIL] tools/audit/gen_phase3_gate_partition.py --check
  [PASS] tools/audit/gen_nongating_apparatus_rows.py --check
  [PASS] tools/audit/gen_discard_records.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach_rows.py --check
  [PASS] tools/audit/gen_gating_row_sizing.py --check
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [PASS] tools/audit/decisions/gen_phase1q_snapshot_establishment.py --check
  [PASS] tools/audit/gen_period_stratum_split.py --check
  [PASS] tools/audit/gen_july_screen.py --check
  [PASS] tools/audit/gen_specification_document_set.py --check
  [FAIL] tools/audit/gen_l0_l1_outgoing_population.py --check
  [PASS] tools/audit/gen_withheld_family_reading.py --subject l2 --check
  [FAIL] tools/audit/gen_artifact_inventory.py --check
  [FAIL] tools/audit/gen_artifact_inventory_surface.py --check
  [PASS] tools/audit/gen_status_archive_pass.py --check
  [PASS] tools/audit/gen_doc_change_candidates.py --check
  [FAIL] tools/audit/gen_test_construction_evidence.py --check
  [PASS] tools/audit/gen_decisions_filter.py --check
  [FAIL] tools/audit/gen_retirement_caller_check.py --check
  [PASS] tools/audit/gen_deciding_act_recovery.py --check
  [PASS] tools/audit/gen_rulings_sort.py --check
  [PASS] tools/audit/gen_sole_carrier_subclass.py --check
  [PASS] tools/audit/gen_ratified_document_check.py --check
  [FAIL] tools/audit/decisions/apply_soft_discard.py --check
  [FAIL] tools/audit/decisions/apply_residue_discard.py --check
  [PASS] tools/audit/gen_framework_untrusted_candidates.py --check
  [PASS] tools/audit/gen_phase1_gate_readers.py --check
  [PASS] tools/audit/gen_discard_reach_split.py --check
  [PASS] tools/audit/decisions/gen_retired_subject_moves.py --check
  [PASS] tools/audit/gen_census_movement_classification.py --check
  [PASS] tools/audit/gen_governing_surface_spans.py --check
  [PASS] tools/audit/gen_governing_surface_readers.py --check
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair CLAUDE.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair OPEN_ITEMS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair DECISIONS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair BUILD_AND_TEST.md
  [PASS] tools/audit/gen_status_batch_bound.py --check
  [PASS] tools/audit/gen_status_residue_move.py --check
  [PASS] tools/audit/gen_retirement_census_movement.py --check
  [PASS] tools/audit/gen_claude_md_finer_spans.py --check
  [PASS] tools/audit/gen_claude_md_finer_surface.py --check
  [PASS] tools/audit/gen_claude_md_finer_archive.py --check
  [PASS] tools/audit/gen_post_split_archive.py --check
  [FAIL] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [PASS] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/decisions/gen_decisions_register.py --check
  [FAIL] tools/audit/decisions/gen_cluster_dispositions.py --verify
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --producible
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
  [PASS] tools/audit/decisions/gen_reads5_repack.py --check
  [PASS] tools/audit/decisions/gen_decision_clusters.py --check
  [PASS] tools/audit/decisions/gen_phase1w_legacy_verification.py --check
  [PASS] tools/audit/decisions/reaim_home_anchors.py --check
  [PASS] tools/audit/decisions/gen_live_prohibition_pointers.py --check
  [PASS] tools/audit/gen_claude_md_growth.py --check
  [PASS] tools/audit/gen_claude_md_prune_backlog.py --check
  [PASS] tools/audit/prune_at_amendment_lint.py --check
  [PASS] tools/open_items_split_check.py 
  [PASS] tools/notation_seams/gen_callpath_facts.py --check
  [NOT RUN] tools/audit/gen_ratification_surface_set.py
  [NOT RUN] tools/audit/reaim_ratification_surface_paths.py
  [NOT RUN] tools/audit/decisions/gen_verbatim_subject_consistency.py
  [NOT RUN] tools/audit/gen_reserved_word_scanner.py
  [HISTORICAL] tools/audit/gen_phase1_completion_inventory.py
  [HISTORICAL] tools/audit/gen_phase1_finish_line.py
  [HISTORICAL] tools/audit/decisions/gen_outstanding_delegations.py
  [HISTORICAL] tools/audit/decisions/gen_phase1n_reading_regime.py
  [HISTORICAL] tools/audit/decisions/gen_reads5_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads6_yield.py
  [HISTORICAL] tools/audit/decisions/gen_phase1m_measurements.py
  [HISTORICAL] tools/audit/decisions/gen_phase1g_triage.py
  [HISTORICAL] tools/audit/decisions/gen_reads1_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads2_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads3_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_yield.py
  [HISTORICAL] tools/audit/decisions/gen_finish_line_item1_routes.py
  [HISTORICAL] tools/audit/decisions/gen_item1_rehome_blocker.py
  [HISTORICAL] tools/audit/decisions/gen_r1_superseded_reach.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_oi326_application.py
81 guard(s) run, 15 failing, 4 not run, 16 historical record(s)
```

## Appendix C — other capture identities

| Capture | Blob |
|---|---|
| Task 2 `--staged` | `4e959e003bbdd5b51e336ee669bd761eba00d7fc` |
| Task 2 working tree | `dfdf41675d56fab90ce075739b0d57fee27b48fe` |
| Task 5(a) generate | `cb789fc6b747ba528f9d2e117aab39d625217ef3` |
| Task 5(a) `--check` | `574a9d240e29f9099a09c6bce8d4f5d2d658204e` |
| Task 5(a) `--verify` | `9cfcddcbc553da8f804aafe0748025ebdcf229e4` |
| Task 5(b) guard set | `d3774d3735639fcf8a604ee5d357a94933f2305f` |
| Stop `--staged` | `4e959e003bbdd5b51e336ee669bd761eba00d7fc` |
| Stop working tree | `fd3a25f41083e97d29ea6a5da0f9ae3b9d7dba1b` |
| the nine single-guard checks | `d78a28b0…`, `40f82e74…`, `9a81bc8a…`, `a99e4ab0…`, `e4d3e573…`, `7c5cb727…`, `882843dc…`, `96643717…`, `845cc32d…` (in the order of the §7 table) |
