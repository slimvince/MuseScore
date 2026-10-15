# CC report — L3's PACK BUILD, FIRST HALF: L3's withheld documents DERIVED AND PRINTED, the two input-contract copies cut — TASK 1 (the freeze of L2's pack) STOPPED with nothing committed, TASK 2 not performed; nothing withheld, no pack, no algorithm changed

> **This report decides nothing and recommends nothing.** It records what was done, what was measured, and where
> the act departed from what the dispatch predicted. **No ruling was taken, no question or recommendation was put
> to the user, nothing was withheld, no pack was rendered, no pack directory was written, no session was booted, and
> no decisions-register entry was written.** Where this report would name a hash it cannot contain — its own commit,
> and the end-state commit that follows — it points at the git log. Guard counts are this batch's own runs; the
> end-state run's values are carried by `tools/audit/guard_state.json` → `summary` in the end-state commit.

**Dispatch:** `records/cc/instructions/cc_instruction_l3_pack_build_first_half_2026_10_15.md`, pinned at Task 0 to
blob `53145d47647a8b4080e2605385589da033895476`, proven unmoved immediately before staging; the committed blob at
Task 0's commit equals the pin.
**Full close:** `records/cowork/handoff/cowork_away_returns.md`, the section **THE L3 PACK BUILD, FIRST HALF: …**,
which carries the plan line and points here.

---

## THE DERIVED DOCUMENT SET — FOR THE USER'S CONFIRMATION UNDER RULING 5

Derived by `python tools/audit/gen_l2_withheld_documents.py --subject l3` (exit 0), from the register's data file
`tools/audit/decisions/backbone_decisions.json` and the ruled `VERDICTS["l3"]` of
`tools/audit/gen_derivation_boot_pack.py`, under Ruling 5 of
`records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md`. **Exactly as the run printed it:**

```
wrote tools\audit\l3_withheld_documents.json
  ARCHITECTURE.md  (5)
  cowork_joint_estimator_architecture.md  (1)
  cowork_layer5_function_design.md  (1)
  cowork_layer6_grouping_design.md  (8)
  cowork_phrase_boundary_design.md  (7)
22 IN entr(ies) homed in 5 document(s)
```

*(The figures above are the run's own printed output, reproduced because the dispatch orders the set printed
exactly as the run printed it; their home is `tools/audit/l3_withheld_documents.json`.)*

**For each document, the IN identities homed there, as the artifact lists them**
(`tools/audit/l3_withheld_documents.json` → `documents`):

| Document | IN identities homed there |
|---|---|
| `ARCHITECTURE.md` | D-022, D-472, D-495, D-584, D-605 |
| `cowork_joint_estimator_architecture.md` | D-526 |
| `cowork_layer5_function_design.md` | D-336 |
| `cowork_layer6_grouping_design.md` | D-454, D-455, D-456, D-457, D-459, D-460, D-461, D-462 |
| `cowork_phrase_boundary_design.md` | D-476, D-477, D-478, D-479, D-480, D-481, D-485 |

**Compared with Ruling 5's stated expectation** (read by the writing side at the decisions-register INDEX's home
column, not at the data file): `ARCHITECTURE.md` (D-022, D-605, D-472, D-495, D-584);
`cowork_joint_estimator_architecture.md` (D-526); `cowork_layer5_function_design.md` (D-336);
`cowork_layer6_grouping_design.md` (D-454 to D-462 except D-458); `cowork_phrase_boundary_design.md` (D-476 to D-481,
D-485). **They AGREE in full** — the same five documents, and the same identities homed in each. No difference.

The artifact's reconciliation holds in both directions (every IN identity accounted to exactly one document, every
listed document named by at least one), and `--subject l3 --check` passes. **Nothing is authored into
`WITHHELD["l3"]`**; Ruling 5 reserves that to after the user's confirmation, and nothing in this batch moves towards
it.

---

## 1. The commits, by explicit hash

| Act | Commit | What it carries |
|---|---|---|
| the tree met | `5499f3e2521c2bf4478469f30f3b9fb18f0af655` | `master` and `origin/master`, both read at the ref files |
| Task 0 | `4d7b8dd16e633f2f2ca8e01237b42a8b714b469a` | this dispatch, handoff entries 402–409, the four 2026-10-15 L3 ruling records, the cut-list document, rows 36 and 39's second extractions, the two corrected first extracts, and `tools/audit/evidence_pin_membership.json` (§4) |
| Task 1 | **none** | STOPPED at its own condition (§5) |
| Task 2 | **none** | not performed (§6) |
| Task 3 | `0ad45e7f09c054fa082f7540a855ac1b31fd35ae` | `tools/audit/gen_l2_withheld_documents.py`, `tools/audit/l3_withheld_documents.json`, `tools/audit/gen_guard_state.py` |
| Task 4 | `a753601449d5642f4cd2734c2f07f9406a213fbf` | the two cut copies under `tools/audit/derivation_exemplars/l3/` |
| the close | see the git log | `STATUS.md`, `STATUS_ARCHIVE.md`, the re-aimed `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`, `tools/audit/session_start_read_size.json`, this report, the close section |
| the end state | see the git log | the full guard run at the close's tree, with the artifacts A2 orders regenerated |

After every push, `.git/refs/remotes/origin/master` was read with the file tools and named the commit just made.
Every commit was verified at the object by explicit hash (`git show --stat <hash>`).

## 2. The guard states

**THE START STATE, a `--check` run before the first edit:** 80 run, **15 failing**, 4 not run, 20 historical — A2's
fourteen by name, plus `gen_evidence_pin_membership.py --check`, which A2 predicts for exactly this cause (the four
untracked 2026-10-15 ruling records) and Task 0 act (2) cleared. `gen_guard_classification.py --check` (exit 2) gave
the standing STOP: *"STOP: tool(s) in the guard-state population with no authored verdict:
['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py',
'tools/audit/gen_withheld_family_reading.py']"*. **What turns `gen_derivation_boot_pack.py --check` red at the
start, measured** (the dispatch did not establish it): *"derivation_boot_pack.json does not re-derive"*,
*"l2/02_the_guiding_principles_and_the_conventions.md does not re-render"* and
*"l2/07_the_charter_the_layers_and_the_decisions.md does not re-render"* — `l2` being live, its pack is compared
against a re-render of today's sources.

**AFTER TASK 3's ENROLMENT:** **81 run, exactly A2's fourteen failing**, 4 not run, 20 historical;
`gen_l2_withheld_documents.py --check` and `--subject l3 --check` both PASS; the runner's own *"STALE vs the run"* line.

**AT THE CLOSE'S TREE, a `--check` run after the last `STATUS.md` edit and before this report was written:** 81 run,
**16 failing**: A2's fourteen plus `gen_l0_l1_outgoing_population.py --check` and `gen_defense_share.py --check` — the
two A2 names as caused by Task 5's `STATUS.md` entries, handled in the end-state commit as A2 orders. The runner's own
stale-artifact line again. `gen_session_start_read_size.py --check` and `gen_status_batch_bound.py --check` passed.
**`gen_derivation_boot_pack.py --check` stays red, `l2` not having been frozen.**

**THE END STATE IS NOT ASSERTED HERE.** The one further commit carries it.

## 3. A1 to A3, and E0 to E5, graded

- **A1 — HELD, BY CONTENT.** The seven tracked inputs each diffed empty against `5499f3e2…`. The tracked population
  through `tools/audit/changed_paths.py` showed exactly three tracked modifications: the two corrected first extracts
  (both TRACKED and modified at the tip, 21 and 61 lines changed) and `tools/audit/claude_md_finer_archive.json`,
  whose hash through git's filters equals the tip's blob (`1df4f20771b6782cbb965c293db4d445bc7ec892`) —
  re-established, left untouched, never staged. Entry 409 was present. **Untracked paths outside Task 0's list, NOT
  landed:** none under `records/`, `reading_pass/` or `ratification_surfaces/`; elsewhere `Claude outputs/`,
  `Codex research inventory/`, `docs/research_papers/polyph9-release/`, two files under `external resarch summary/`,
  the `scratch_artifacts/` population and `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. No
  further handoff entry or ruling record appeared during the run.
- **A2 — HELD AT THE START; NOT REACHED AT THE END AS PREDICTED, BECAUSE TASK 1 DID NOT RUN.** Start: the fourteen
  plus the predicted evidence-pin red, and the standing classification STOP. A2's end prediction (run 81, failing the
  fourteen or thirteen) assumed Task 1's freeze; with Task 1 stopped, `gen_derivation_boot_pack.py` stays red, so the
  end state is the fourteen plus whatever A2's own `STATUS.md` exceptions leave after their regeneration — carried by
  the end-state commit.
- **A3 — verified at the objects after the last commit**, stated in the close section's end-state part. Up to Task 4,
  `git diff --name-status 5499f3e2… a7536014…` names exactly the nineteen Task 0 paths and the five paths Tasks 3 and 4
  wrote, and nothing under `tools/audit/derivation_boot_pack/`, not `tools/audit/derivation_boot_pack.json`, not
  `tools/audit/gen_derivation_boot_pack.py`, not `tools/audit/l2_withheld_documents.json`, neither source
  specification, no ruling record after landing, no extract after landing, not `FRAMEWORK.md`, no rendered
  decisions-register file and neither reading file.
- **E0 — MET.** The nineteen paths in one commit; `origin/master` at it; every path accounted for.
- **E1 — NOT MET: TASK 1 STOPPED.** Its measurement half holds — the ten files proven equal to their committed blobs
  and the ten digests taken twice and agreeing (§5) — and no entry was written, no manifest regenerated and nothing
  committed.
- **E2 — NOT MET: TASK 2 NOT PERFORMED** (§6).
- **E3 — MET.** L2's printed output and artifact byte-identical; L3's set derived, printed and committed as an
  artifact; the enrolment in place; `WITHHELD` untouched.
- **E4 — MET.** Both copies written, every quote found once and removed, both reconstructions byte-exact, every
  expected end confirmed; the search reported whole; both sources unchanged.
- **E5** — carried by the end-state commit, not asserted here.

## 4. Task 0 — the landing

A1's check as above. `gen_evidence_pin_membership.py --check` was red (*"STALE vs the derivation:
evidence_pin_membership.json does not re-derive"*); regenerated, and measured against the tip's blob by
`git diff 5499f3e2… -- tools/audit/evidence_pin_membership.json`: **the only movement is its list of ruling records
read**, which gains the four 2026-10-15 L3 records of Task 0's item 3, with the count of records read derived from that
list; no member, pin or route moved. Committed with the eighteen landed paths. The dispatch was proven at its pinned
blob immediately before staging; the nineteen staged paths were enumerated with `tools/audit/changed_paths.py --staged`
before the commit, under the ordered subject (entry 409 present, so the subject reads `entries 402-409`).

## 5. Task 1 — STOPPED AT ITS OWN CONDITION, NOTHING COMMITTED

**(a) and (b) — HELD.** The directory listing (by the file tools) and the tip's tree both name the same ten files. For
each, `git hash-object` (through git's filters), `git hash-object --no-filters` and
`git rev-parse 5499f3e2…:<path>` agree:

| File | Digest (all three forms agree) |
|---|---|
| `00_READ_THIS_FIRST.md` | `fd27dee7a4b6bca3454d12c659aa34a96cd1abc1` |
| `01_the_phase_definitions.md` | `518b1e50d60af2b4e2ddcd8978623832eb071899` |
| `02_the_guiding_principles_and_the_conventions.md` | `41288e7375faca980c566ca0367fca1c7de760e8` |
| `03_the_writing_standards.md` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` |
| `04_the_dispatch_protocol.md` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` |
| `05_the_ratified_design_intent.md` | `6ae0b1d8c9a830cfc3f2021f37460f05fad23547` |
| `06_the_defect_type_catalog.md` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` |
| `07_the_charter_the_layers_and_the_decisions.md` | `5796c2d1bda0520b067ccde300e25336b9606884` |
| `08_the_fifty_six_research_extracts.md` | `69404bace220b25589e78edc7c89c513ae5a0e2e` |
| `09_the_empirical_findings_ledger.md` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` |

**THE SURPRISE, found at the ordered first read (7) and measured before any edit (#13).** The dispatch's writing side
did not read `build_subject` or `build()` (its provenance says so). Read whole, `build_subject` branches on
`subject in FROZEN` in two places that are NOT about the freeze's hash STOP:

1. the cross-reference additions search `XREF_FIELDS_FROZEN` (`title`, `verbatim`, `plain`, `rationale`,
   `status_source`) for a frozen subject and `XREF_FIELDS` (the first three) otherwise — the comment above them
   states the ground: Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md` scopes
   the three-field search to every subject NOT frozen, *"A FROZEN subject keeps the five-field search its pack was
   built under"*;
2. the extras' leak check (limb B) runs *"only for a subject that is NOT FROZEN — a frozen subject's record describes
   a directory rendered before this check existed (D-657)"*, and the `★_what_these_are` text of the additions block
   switches to the five-field wording for a frozen subject.

Both comments are true of the three subjects frozen until now, whose packs predate those rulings. **They are false of
`l2`, whose pack was rendered UNDER them** (the 2026-09-27 pack build). So "is in `FROZEN`" is doing two jobs — *spent*
and *rendered before the 2026-09-21/2026-09-27 rulings* — and for `l2` the two come apart.

**THE EFFECT, MEASURED WITHOUT EDITING ANY FILE.** Two scripts, outside the repository (texts in §8), imported the
generator: the first compared `l2`'s additions under both field sets against the committed manifest; the second added
`FROZEN["l2"]` with the ten digests **in memory only**, ran `build()`, verified every frozen subject's hash STOP in both
directions, and compared the manifest `write_all` would write against the committed one. Results:

- `harmony-boundary`, `scoring-model` and `l0-l1`: **UNCHANGED**; no top-level field moved.
- `l2`: moved in `LEAKS`, `LEAKS_IN_THE_EXTRAS` (**REMOVED**), `THE_WITHHELD_FAMILY`, `counted`,
  `the_members_as_rendered`, and `★_FROZEN` (added). The committed manifest's `l2` additions equal the three-field
  derivation exactly; the five-field derivation adds every one of them and more — the identities are listed in the
  first script's output — so `withheld_identities_derived`, `withheld_identities_total`, `leaks` and
  `design_intent_entries_rendered` all move, the `★_what_these_are` text states that `rationale` and `status_source`
  were searched, and the extras leak list that went to the user disappears from the record. *(The values are in the
  committed manifest and the scratch outputs; none is restated here, D-431.)*

**WHY THIS IS THE DISPATCH'S OWN STOP.** Task 1(d) expects *"the diff is confined to `l2`'s record (the frozen-subject
shape `frozen_from_disk` writes)"*. This movement is not `frozen_from_disk`'s shape — it is `build_subject`'s FROZEN
branches re-deriving `l2`'s withheld set under a rule its pack was not built under — and the result would make the
record of what L2's session was given state a withheld set and a leak list that session's pack never carried, which is
the falsification the freeze exists to prevent (#12; D-646's own ground). **The cause is established at the code; a
fix — for instance keying those two branches on something other than `FROZEN` membership — is a change to the
generator's mechanism, which is the user's (D-657, D-669), and is not taken here.** No `FROZEN` entry was written, the
generator is byte-unchanged, the manifest was not regenerated, and nothing was committed.

**(e) — reported as ordered, read at the code.** `write_all`, quoted: *"if subject in FROZEN: # THE FREEZE, at the one
place that could break it. Nothing is written into a spent subject's directory — not the whole pack, not one file of
it. continue"*. `build()` builds every subject of `WITHHELD`: today `harmony-boundary`, `scoring-model`, `l0-l1` and
`l2` — none of them `l3`. **Because `l2` stayed live, the write path into `l2`'s directory is NOT shut.**

## 6. Task 2 — NOT PERFORMED

Its ordered regeneration of the manifest *"naming the mode"* is a write run, and `write_all` writes every subject not in
`FROZEN` — so with `l2` live it would re-render `tools/audit/derivation_boot_pack/l2/` from today's sources, which this
dispatch's bars forbid (*"NO PACK DIRECTORY WRITTEN"*) and which Task 1 exists to prevent. Restricting the write with
`--subject` to a frozen subject would build around the surprise and would still move `l2`'s manifest record beyond the
one bullet line Task 2(e) admits, `l2`'s record not re-deriving today (§2). **Neither the three generator edits nor
`VERDICT_DATE["l3"]` were written; both stay owed to a later batch, after the user rules on §5.** No `--check` before/
after outputs or manifest diffs exist for this task.

## 7. Task 3 — L3's withheld documents derived and printed; the tool gains `--subject`

**(a)** Before any edit, `--check`: *"the L2 withheld-document derivation re-derives"*, exit 0.

**(b)** The four module constants `SUBJECT`, `RULED_IN_COUNT`, `RULING_6` and `OUT` are replaced by one table
`SUBJECTS`, keyed `l2` and `l3`. `SUBJECTS["l2"]` carries the four values and every L2 sentence the tool wrote or
printed — `what_this_is`, the ruling and its verbatim, the verdict-table sentence, both bound sentences, STOP 4's
message, both `--check` messages and the closing line — moved unchanged. `SUBJECTS["l3"]` carries `l3`, 22,
`tools/audit/l3_withheld_documents.json`, Ruling 5 of the 2026-10-15 boot-list record with the dispatch's quotation
of it as its verbatim, each sentence with L2 read as L3 and Ruling 6 as Ruling 5, and STOP 4's message citing the
2026-10-15 lists record as ordered. `main()` gains `--subject` (`l2` or `l3`, default `l2`); any other value, or the
flag with no value, STOPs — shown by `--subject l4 --check`: *"STOP: --subject takes one of ['l2', 'l3']; given
'l4'"*, exit 2. The docstring gains one paragraph after its first; no other docstring line changed. **A slip of my own,
caught by the self-check and corrected before the commit:** the first edit to the `BACKBONE` line dropped the space
after `=`; the explicit-hash diff showed it, it was restored, and the final diff deletes only the lines named above.

**(c)** After the edits, `--check` output **byte-identical** to (a)'s (`cmp` exit 0, run again after the correction),
and `tools/audit/l2_withheld_documents.json` hashes `82ff8abcb877eaacab3a04dcb54e681e5a9cf729`, equal to its committed
blob.

**(d)** `--subject l3`: the printed set at the head of this report, exit 0; `--subject l3 --check`: *"the L3
withheld-document derivation re-derives"*, exit 0. No STOP fired.

**(e)** One entry added to `AUTHORED` in `tools/audit/gen_guard_state.py`, directly after the `gen_l2_withheld_documents.py
--check` entry, in the shape of the reading-file tool's `--subject l3` entry (a dated `AUTHORED` comment header, the
args `["--subject", "l3", "--check"]`), with the ordered `what_it_checks` text. The full guard set: 81 run, the
fourteen failing (§2).

## 8. Task 4 — the two cut copies, and the search that cut nothing

**(a)** Results, as the script printed them (`EOL` LF for both sources):

- **Job 1** — source `cowork_derived_specification_l0_l1_2026_09_03.md`, 142,523 bytes (as expected), `git hash-object`
  `8148e8d34b0f2dd061589240e4d8448ad5447771`. Cuts 1–5 each matched once in the source and zero times in the result;
  re-insertion reproduces the source byte for byte. Each removed span included exactly one space before its quote.
  Written `tools/audit/derivation_exemplars/l3/the_l0_l1_specification_the_input_contract.md`, 142,104 bytes,
  `git hash-object` `4602b98dcddc7c612d0c716d042ff1e226379d86`; with the HEAD and its blank line removed it equals the
  result byte for byte.
- **Job 2** — source `cowork_derived_specification_l2_2026_10_10.md`, 218,121 bytes (as expected), `git hash-object`
  `bba490c50a9b1e963b59ed971b960fc648c5fd68`. Cuts 6–7 each matched once and then zero times; re-insertion byte-exact;
  one space removed before each quote. Written
  `tools/audit/derivation_exemplars/l3/the_l2_specification_the_input_contract.md`, 218,151 bytes, `git hash-object`
  `05d7ee00dc746ef4a0e2b1811a6c8a82bfdb2b14`; the HEAD check as for Job 1.

**Every expected end, confirmed** (the result's 80 characters before and after each cut; `⏎` is `EOL`):

| Cut | Result before the cut ends with | Result after the cut begins with | Both |
|---|---|---|---|
| 1 | `…bounded by harmony change;` | ` any further span is named by what bounds it and never by *slice* or bare *regio…` | MATCH |
| 2 | `…L1 publishing notated punctuation⏎  evidence and not phrases;` | `"* *(The ruling's own sentence uses* bar *in its prohibiting sense…` | MATCH |
| 3 | `…the partition of Row 10.53 is a published fact."*` | `⏎- *Beside S-39 (Ruling 48, §3bc) — what an absent flag does not mean.*…` | MATCH |
| 4 | `…the class of⏎  every change point (Ruling 47)"*` | `⏎⏎**S-40. Several marks at one change point…` | MATCH |
| 5 | `…the series is the slice list, already published;` | `"*⏎⏎**S-30. No slice has zero length.…` | MATCH |
| 6 | `…before jazz ground truth⏎  exists;` | ` **L2-S4 stands as derived.**"⏎- *Beside L2-S4 (…` | MATCH |
| 7 | `…- *Status.* Settled.⏎- *Premise.* L3 needs nothing intermediate.` | `⏎- *Falsifier.* CODE. **Observable:** L2's output schema.…` | MATCH |

The residues the dispatch records for the user stand as it predicts: Cut 4's sentence loses its full stop; Cuts 2 and 5
leave a semicolon before a closing quotation.

**(b) The search, reported whole.** Over the two copies, for the 22 IN identities of `VERDICTS["l3"]` (read by import,
through `VERDICT_IN`; nothing called `build()` or `main()`), the five documents of
`tools/audit/l3_withheld_documents.json`, the string `ARCHITECTURE.md` and the generator's `PATH_LIKE`
(`\b(?:docs|src)/[A-Za-z0-9_./+-]+`):

- `…/the_l0_l1_specification_the_input_contract.md`: **no hit of any kind.**
- `…/the_l2_specification_the_input_contract.md`: **one hit, of kind (3):** line 2234, `PATH_LIKE` matched
  `docs/research_papers/BIBLIOGRAPHY.md`, the line verbatim:
  `  the Rule of the Octave is held (`docs/research_papers/BIBLIOGRAPHY.md`); a published form entering under`

Counts per kind per copy: L0/L1 copy (1) 0, (2) 0, (3) 0; L2 copy (1) 0, (2) 0, (3) 1. **The prediction holds** — no
hit of kind (1), and no hit of kind (2) for the five documents, which here are the whole derived set. The kind (3) hit
is not a STOP and goes to the user through the writing side; nothing was cut.

**(c)** After both scripts, both sources hash as at (a)1 and equal their committed blobs at `0ad45e7f…`.

**THE SCRIPTS, whole.** All are kept in this session's scratch folder, outside the repository.

`t4_cut_copies.py` — Task 4(a):

```python
"""Task 4(a) of cc_instruction_l3_pack_build_first_half_2026_10_15.md — write the two cut
input-contract copies.  Kept outside the repository working tree; its text goes into the report.

Per job: read the SOURCE as bytes, decode UTF-8, record size and `git hash-object`; take EOL; build
one whitespace-tolerant pattern per QUOTE and require EXACTLY ONE match; extend each span left over
the run of U+0020 before it on the same line; require disjoint spans; remove them; verify (i) every
pattern matches the result zero times, (ii) re-inserting every removed span reproduces the source
byte for byte, (iii) each cut's 80 characters before and after against the expected ends; and only
if every check holds, prepend the HEAD and write the TARGET, then verify the written file.  A
failed check is a STOP for that job: nothing is written for it.
"""
import os
import re
import subprocess
import sys

ROOT = r"C:\s\MS"
SHOW_EOL = "⏎"


def git_hash_object(rel: str) -> str:
    return subprocess.run(["git", "hash-object", rel], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout.strip()


JOBS = [
    {
        "name": "Job 1",
        "source": "cowork_derived_specification_l0_l1_2026_09_03.md",
        "target": "tools/audit/derivation_exemplars/l3/the_l0_l1_specification_the_input_contract.md",
        "expected_size": 142523,
        "head": [
            "> **THE INPUT CONTRACT — the ratified specification of L0 and L1, cut for the L3 deriving session.**",
            "> Its source is `cowork_derived_specification_l0_l1_2026_09_03.md`; this file is a cut copy of that source and not a",
            "> second version of it. Below this block the source stands verbatim, except that passages stating the L3 layer's own",
            "> ruled or current design have been removed where they stood, with no mark. Do not try to reconstruct them, and do",
            "> not treat a gap as a hint.",
        ],
        "cuts": [
            ("Cut 1",
             "the grouping layer's unit is the punctuation span, bounded by notated punctuation, as Row 13.1's own convention says;",
             "bounded by harmony change;",
             " any further span is named by what bounds it"),
            ("Cut 2",
             "the grouping object is the punctuation span; the phrase-boundary primitive's code name is an inherited collision for OI-229, that primitive being L3's under Ruling 48.",
             "evidence and not phrases;",
             "\"* *(The ruling's own sentence uses* bar"),
            ("Cut 3",
             "The graded profile, its gap-dominant weights, the marker spikes, the max-normalisation, the adaptive threshold, the peak-picking, the picked set and the *\"ends a phrase\"* flag are **RELOCATED to the consumer that decides the phrase boundary** — the phrase read-off at L3 under the L1 → L3 contract — *\"with D-476 to D-485 re-homed there and D4 (D-478) remaining that consumer's ruled rule\"*.",
             "is a published fact.\"*",
             "⏎- *Beside S-39 (Ruling 48, §3bc) — what an absent flag"),
            ("Cut 4",
             "— and relating them is L2's cadence-factor covariate and L3's alignment window, to which Rows 11.12 and 13.14 are relocated.",
             "every change point (Ruling 47)\"*",
             "⏎"),
            ("Cut 5",
             "the harmonic rhythm is over decided harmonic spans, the charter's L3.",
             "the series is the slice list, already published;",
             "\"*⏎"),
        ],
    },
    {
        "name": "Job 2",
        "source": "cowork_derived_specification_l2_2026_10_10.md",
        "target": "tools/audit/derivation_exemplars/l3/the_l2_specification_the_input_contract.md",
        "expected_size": 218121,
        "head": [
            "> **THE INPUT CONTRACT — the ratified specification of L2, cut for the L3 deriving session.**",
            "> Its source is `cowork_derived_specification_l2_2026_10_10.md`; this file is a cut copy of that source and not a",
            "> second version of it. Below this block the source stands verbatim, except that passages stating the L3 layer's own",
            "> ruled or current design have been removed where they stood, with no mark. Do not try to reconstruct them, and do",
            "> not treat a gap as a hint.",
        ],
        "cuts": [
            ("Cut 6",
             "D-526's \"jazz-specific classes enter only under the OI-7 jazz-ground-truth gate\" is read as gating the increment's measurement rather than its landing (the surface's reading, put with the position and not separately ruled).",
             "before jazz ground truth⏎  exists;",
             " **L2-S4 stands as derived.**\""),
            ("Cut 7",
             "**False-negative path:** L3's cadence-type reading wanting \"how strongly V→I was scored here\". It reads the masses of the readings with and without the cadence, which are published, rather than a term value.",
             "- *Premise.* L3 needs nothing intermediate.",
             "⏎- *Falsifier.* CODE."),
        ],
    },
]


def run_job(job: dict) -> bool:
    print(f"=================== {job['name']} ===================")
    src_rel = job["source"]
    raw = open(os.path.join(ROOT, src_rel), "rb").read()
    text = raw.decode("utf-8")
    print(f"SOURCE {src_rel}: {len(raw)} bytes (expected {job['expected_size']}"
          f"{'' if len(raw) == job['expected_size'] else ' — DIFFERENT, reported, not a STOP'}); "
          f"git hash-object {git_hash_object(src_rel)}")
    eol = "\r\n" if "\r\n" in text else "\n"
    print(f"EOL: {'CRLF' if eol == chr(13) + chr(10) else 'LF'}")

    patterns, spans = [], []
    ok = True
    for name, quote, _, _ in job["cuts"]:
        pat = re.compile(r"\s+".join(re.escape(w) for w in quote.split()))
        found = list(pat.finditer(text))
        print(f"{name}: pattern matches {len(found)} time(s) in the source")
        if len(found) != 1:
            ok = False
            continue
        m = found[0]
        start = m.start()
        while start > 0 and text[start - 1] == " ":
            start -= 1
        patterns.append((name, pat))
        spans.append((name, start, m.end()))
    if not ok:
        print(f"STOP — {job['name']}: a quote is not found exactly once; nothing is written.")
        return False

    ordered = sorted(spans, key=lambda s: s[1])
    for (n1, a1, b1), (n2, a2, b2) in zip(ordered, ordered[1:]):
        if a2 < b1:
            print(f"STOP — {job['name']}: {n1} and {n2} overlap; nothing is written.")
            return False

    # Build the result, and remember where each cut now sits in it.
    pieces, cursor, at_in_result = [], 0, {}
    removed_len = 0
    for name, a, b in ordered:
        pieces.append(text[cursor:a])
        at_in_result[name] = a - removed_len
        removed_len += b - a
        cursor = b
    pieces.append(text[cursor:])
    result = "".join(pieces)

    # (i) every quote's pattern matches the result zero times.
    for name, pat in patterns:
        n = len(pat.findall(result))
        print(f"(i) {name}: pattern matches the result {n} time(s)")
        if n != 0:
            ok = False
    # (ii) re-inserting each removed span at its offset reproduces the source byte for byte.
    rebuilt = result
    for name, a, b in sorted(ordered, key=lambda s: at_in_result[s[0]], reverse=True):
        p = at_in_result[name]
        rebuilt = rebuilt[:p] + text[a:b] + rebuilt[p:]
    same = rebuilt.encode("utf-8") == raw
    print(f"(ii) re-inserting every removed span reproduces the source byte for byte: {same}")
    if not same:
        ok = False
    # (iii) the 80 characters before and after each cut, against the expected ends.
    for name, quote, exp_before, exp_after in job["cuts"]:
        p = at_in_result[name]
        before = result[max(0, p - 80):p]
        after = result[p:p + 80]
        eb = exp_before.replace(SHOW_EOL, eol)
        ea = exp_after.replace(SHOW_EOL, eol)
        good_b, good_a = before.endswith(eb), after.startswith(ea)
        removed = [text[a:b] for n, a, b in ordered if n == name][0]
        print(f"(iii) {name}: removed {len(removed)} characters, "
              f"{len(removed) - len(removed.lstrip(' '))} of them the space run before the quote")
        print(f"      result BEFORE (80): {before.replace(eol, SHOW_EOL)!r}")
        print(f"      expected to end:    {exp_before!r}  -> {'MATCHES' if good_b else 'DIFFERS'}")
        print(f"      result AFTER  (80): {after.replace(eol, SHOW_EOL)!r}")
        print(f"      expected to begin:  {exp_after!r}  -> {'MATCHES' if good_a else 'DIFFERS'}")
        if not (good_b and good_a):
            ok = False
    if not ok:
        print(f"STOP — {job['name']}: a check failed; nothing is written.")
        return False

    head = eol.join(job["head"]) + eol + eol
    out = head + result
    tgt = os.path.join(ROOT, job["target"])
    os.makedirs(os.path.dirname(tgt), exist_ok=True)
    with open(tgt, "wb") as fh:
        fh.write(out.encode("utf-8"))
    written = open(tgt, "rb").read()
    hb = head.encode("utf-8")
    print(f"WRITTEN {job['target']}: {len(written)} bytes; git hash-object "
          f"{git_hash_object(job['target'])}")
    print(f"  the written file begins with the HEAD and its blank line: {written.startswith(hb)}")
    print(f"  with them removed it equals the result byte for byte: "
          f"{written[len(hb):] == result.encode('utf-8')}")
    print(f"  the source's git hash-object after the job: {git_hash_object(src_rel)}")
    return True


if __name__ == "__main__":
    results = [run_job(j) for j in JOBS]
    print("RESULT:", ["written" if r else "STOPPED" for r in results])
    sys.exit(0 if all(results) else 3)
```

`t4_search.py` — Task 4(b):

```python
"""Task 4(b) of cc_instruction_l3_pack_build_first_half_2026_10_15.md — the search over the two cut
copies.  Its hits are REPORTED; nothing is cut.  Kept outside the repository working tree.

Reads the two copies; `VERDICTS["l3"]` by import of the generator (its IN entries, with that
module's `VERDICT_IN` token — nothing calls `build()` or `main()`); and
`tools/audit/l3_withheld_documents.json`.  For every line of each copy (numbered from 1 in the
copy) it prints every hit of: (1) each IN identity, as `re.escape(id) + r"(?!\\d)"`; (2) each
document of the derived set, as a plain substring; (3) the string `ARCHITECTURE.md`, and every
match of the generator's own `PATH_LIKE`.
"""
import json
import os
import re
import sys

ROOT = r"C:\s\MS"
sys.path.insert(0, os.path.join(ROOT, "tools", "audit"))
import gen_derivation_boot_pack as pack  # noqa: E402

COPIES = [
    "tools/audit/derivation_exemplars/l3/the_l0_l1_specification_the_input_contract.md",
    "tools/audit/derivation_exemplars/l3/the_l2_specification_the_input_contract.md",
]

in_ids = sorted((i for i, v in pack.VERDICTS["l3"].items() if v[0] == pack.VERDICT_IN),
                key=lambda s: int(s.split("-")[1]))
derived = json.load(open(os.path.join(ROOT, "tools", "audit", "l3_withheld_documents.json"),
                         encoding="utf-8"))
docs = [d["document"] for d in derived["documents"]]
print(f"IN identities ({len(in_ids)}): {in_ids}")
print(f"derived documents ({len(docs)}): {docs}")
print(f"PATH_LIKE: {pack.PATH_LIKE.pattern}")
id_pats = [(i, re.compile(re.escape(i) + r"(?!\d)")) for i in in_ids]

for copy in COPIES:
    print(f"==================== {copy}")
    lines = open(os.path.join(ROOT, copy), encoding="utf-8", newline="").read().split("\n")
    counts = {1: 0, 2: 0, 3: 0}
    for n, ln in enumerate(lines, start=1):
        shown = ln.rstrip("\r")
        hits = []
        for i, p in id_pats:
            for m in p.finditer(ln):
                hits.append((1, m.group(0)))
        for d in docs:
            if d in ln:
                hits.append((2, d))
        if "ARCHITECTURE.md" in ln:
            hits.append((3, "ARCHITECTURE.md"))
        for m in pack.PATH_LIKE.finditer(ln):
            hits.append((3, m.group(0)))
        for kind, what in hits:
            counts[kind] += 1
            print(f"{copy} | line {n} | kind ({kind}) | {what} | {shown}")
    print(f"COUNTS for {copy}: kind (1) {counts[1]}, kind (2) {counts[2]}, kind (3) {counts[3]}")
```

`diag_l2_xref.py` — Task 1's diagnosis, NOT ordered by the dispatch (§9 item 2):

```python
"""Diagnose, without editing the tool, what freezing `l2` changes in its build.

Imports the generator from the repository's tools/audit, computes `l2`'s cross-reference additions
under the three-field search (live subject) and under the five-field search (frozen subject), and
compares both with the additions the committed manifest records for `l2`.
"""
import json
import os
import sys

ROOT = r"C:\s\MS"
sys.path.insert(0, os.path.join(ROOT, "tools", "audit"))
import gen_derivation_boot_pack as pack  # noqa: E402

sort = pack.read_json(pack.SORT)
bb_data = pack.read_json(pack.BACKBONE)
backbone = {d["id"]: d for d in bb_data.get("decisions", [])}
for r in bb_data.get("retired_entries", {}).get("entries", []):
    e = r.get("the_entry", {})
    if e.get("id") and e["id"] not in backbone:
        backbone[e["id"]] = e

design_intent = [e for e in sort["entries"] if e.get("proposed_class") == "DESIGN-INTENT"]
authored_ids = {i for i, v in pack.VERDICTS["l2"].items() if v[0] == pack.VERDICT_IN}
docs = set(pack.WITHHELD["l2"].get("withheld_documents", {}))

three = pack.cross_reference_additions(authored_ids, docs, design_intent, backbone, pack.XREF_FIELDS)
five = pack.cross_reference_additions(authored_ids, docs, design_intent, backbone,
                                      pack.XREF_FIELDS_FROZEN)
ids3 = sorted(a["id"] for a in three)
ids5 = sorted(a["id"] for a in five)

manifest = json.load(open(pack.OUT, encoding="utf-8"))
rec = manifest["subjects"]["l2"]
ids_m = sorted(a["id"] for a in rec["THE_WITHHELD_FAMILY"]["derived_cross_reference_additions"]["additions"])

print("authored IN:", len(authored_ids), " withheld documents:", len(docs))
print("three-field additions:", len(ids3))
print("five-field additions: ", len(ids5))
print("committed manifest additions:", len(ids_m))
print("three == manifest:", ids3 == ids_m)
print("five == manifest: ", ids5 == ids_m)
print("in five, not in three:", sorted(set(ids5) - set(ids3)))
print("in three, not in five:", sorted(set(ids3) - set(ids5)))
print("manifest l2 carries LEAKS_IN_THE_EXTRAS:", "LEAKS_IN_THE_EXTRAS" in rec,
      " entries:", len(rec.get("LEAKS_IN_THE_EXTRAS", {}).get("entries", [])))
print("manifest l2 counted.extras_lines_with_a_leak_hit:",
      rec["counted"].get("extras_lines_with_a_leak_hit"))
print("manifest l2 counted.withheld_identities_total:", rec["counted"]["withheld_identities_total"])
```

`sim_freeze_l2.py` — Task 1(c)–(d) simulated in memory, NOT ordered by the dispatch (§9 item 2); it writes its
manifest to the scratch folder only:

```python
"""Simulate Task 1 IN MEMORY: add FROZEN["l2"] to the imported generator, build, and compare the
manifest that `write_all` would write against the committed manifest.  Writes nothing into the
repository: the manifest it would write goes to this scratch folder only.
"""
import json
import os
import sys

ROOT = r"C:\s\MS"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "tools", "audit"))
import gen_derivation_boot_pack as pack  # noqa: E402

DIGESTS = {
    "00_READ_THIS_FIRST.md": "fd27dee7a4b6bca3454d12c659aa34a96cd1abc1",
    "01_the_phase_definitions.md": "518b1e50d60af2b4e2ddcd8978623832eb071899",
    "02_the_guiding_principles_and_the_conventions.md": "41288e7375faca980c566ca0367fca1c7de760e8",
    "03_the_writing_standards.md": "a41983018cb27ed4a47d24ff8bb9e95181ed0572",
    "04_the_dispatch_protocol.md": "72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da",
    "05_the_ratified_design_intent.md": "6ae0b1d8c9a830cfc3f2021f37460f05fad23547",
    "06_the_defect_type_catalog.md": "1dec7621dc48d89242cacaf79b3048cd965d6a19",
    "07_the_charter_the_layers_and_the_decisions.md": "5796c2d1bda0520b067ccde300e25336b9606884",
    "08_the_fifty_six_research_extracts.md": "69404bace220b25589e78edc7c89c513ae5a0e2e",
    "09_the_empirical_findings_ledger.md": "925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6",
}

before = json.load(open(pack.OUT, encoding="utf-8"))

pack.FROZEN["l2"] = {"finding": "simulated", "date": "2026-10-15", "reason": "simulated",
                     "digests": DIGESTS}
manifest, packs, displaced = pack.build()
for s in sorted(pack.FROZEN):
    pack.verify_frozen(s)   # the hash STOP, both directions
with open(os.path.join(HERE, "sim_manifest_after_freeze.json"), "w", encoding="utf-8",
          newline="") as fh:
    fh.write(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

print("top-level keys equal:", sorted(before) == sorted(manifest))
for k in sorted(set(before) | set(manifest)):
    if k == "subjects":
        continue
    if before.get(k) != manifest.get(k):
        print("TOP-LEVEL FIELD MOVED:", k)
for s in sorted(set(before["subjects"]) | set(manifest["subjects"])):
    a, b = before["subjects"].get(s), manifest["subjects"].get(s)
    print(f"subject {s}: {'UNCHANGED' if a == b else 'MOVED'}")
    if a != b and a and b:
        for k in sorted(set(a) | set(b)):
            if a.get(k) != b.get(k):
                print(f"    field moved: {k}"
                      + ("" if k in a else "   [ADDED]") + ("" if k in b else "   [REMOVED]"))

l2a, l2b = before["subjects"]["l2"], manifest["subjects"]["l2"]
print("l2 counted before:", json.dumps(l2a["counted"], ensure_ascii=False))
print("l2 counted after: ", json.dumps(l2b["counted"], ensure_ascii=False))
xa = l2a["THE_WITHHELD_FAMILY"]["derived_cross_reference_additions"]
xb = l2b["THE_WITHHELD_FAMILY"]["derived_cross_reference_additions"]
print("l2 additions before:", len(xa["additions"]), " after:", len(xb["additions"]))
print("l2 additions ★_what_these_are AFTER:", xb["★_what_these_are"])
print("l2 LEAKS entries before:", len(l2a["LEAKS"]["entries"]), " after:", len(l2b["LEAKS"]["entries"]))
print("l2 LEAKS_IN_THE_EXTRAS before:", "LEAKS_IN_THE_EXTRAS" in l2a, " after:", "LEAKS_IN_THE_EXTRAS" in l2b)
print("frozen subjects verified:", sorted(pack.FROZEN))
```

## 9. Declared departures

1. **The dispatch was read from the working tree before it was pinned** — standing clause P-2's fallback route, the
   user's opening line naming only the file. Pinned at Task 0; the blob proven unmoved before staging.
2. **Task 1 STOPPED and Task 2 was not performed** (§5, §6), and **two unordered diagnosis scripts were run** to
   establish the cause before stopping (D-669: a tool can be diagnosed without being edited). Both import the
   generator and write nothing into the repository; their texts are in §8.
3. **The batch continued through Tasks 3 to 5 after Task 1's STOP.** Task 1(d)'s STOP is stated for that task
   (*"nothing is committed"*), not for the batch; Tasks 3 and 4 read nothing Task 1 or Task 2 writes, and Task 3's
   printed set is what Ruling 5's STOP for the user needs.
4. **Task 5's `STATUS.md` close entry says what happened, not what the dispatch scripted** — the dispatch orders it to
   say *"that L2's pack is frozen"*; it says L2's pack is NOT frozen and why (#10).
5. **Ruling 5's verbatim in `SUBJECTS["l3"]` is the dispatch's quotation of it, as ordered**; see §10 item 2.
6. **Scratch files went to this session's scratch folder** (a subfolder of `%TEMP%`); every run output and script is
   there.
7. **Each commit message carries one trailer line after the ordered subject** — the co-author attribution line this
   session's instructions require — as a second paragraph; the subject lines are exactly the ordered ones.
8. **`git hash-object` was run on working-tree files** — the dispatch, for P-2; `claude_md_finer_archive.json`, for A1;
   the ten `l2` pack files, as Task 1(a)–(b) orders; and, inside the Task 4 script, the two sources and the two
   copies, as Task 4(a) orders. A first attempt at Task 1(a) also listed the `l2` directory with `ls` and was denied by
   the armed guard; the listing was taken with the file tools instead.
9. **Task 3's guard enrolment sits directly after its sibling `gen_l2_withheld_documents.py --check` entry**, not
   beside the reading-file tool's `l3` entry: "the same convention" was read as *the next subject of the same tool,
   placed after that tool's existing entry*, which is what the reading-file tool's `l3` entry itself does.

## 10. Observations, recorded and not acted on

1. **The freeze's two scoping branches key on `FROZEN` membership** (§5). Any later freeze of a subject rendered
   after the 2026-09-21 and 2026-09-27 rulings — `l2` now, and `l3` when its session has run — meets the same shape.
2. **Ruling 5's full sentence opens with a clause the dispatch's quotation omits** — the record reads *"As Ruling 6
   of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` did for L2: the pack-build dispatch derives, …"*; the
   artifact carries the dispatch's quotation, which begins at *"the pack-build dispatch derives"*. Recorded against
   D-643 (a ruling invoked as an application is quoted in full), not corrected, the dispatch ordering that text.
3. **A2's end prediction depended on Task 1** and so does not apply as written (§3).
4. **The dispatch's read-first block names handoff entries 408 and 409 rather than a block of
   `records/cowork/handoff/cowork_handoff.md`**; the handoff now lives in per-entry files, which is the reading taken.

## 11. What this batch did not do

No identity withheld; no `WITHHELD`, `EXTRAS`, `FROZEN` or `VERDICT_DATE` entry for `l3`, and no `FROZEN` entry for
`l2`; no edit to `tools/audit/gen_derivation_boot_pack.py` at all, so none to `CRITERION`, `MEMBERS`,
`CHARTER_MEMBER_7`, `LEDGER_MEMBER_9`, any `VERDICTS` entry or `criterion_block()`; no pack rendered and no pack
directory written; no session booted; no edit to either source specification, the cut-list document, any ruling
record or any extract after landing; no score file copied, staged or written; no ruling taken and no question or
recommendation put to the user; no open-items row created, flipped or discarded; no decisions-register entry and no
`D-NNN`; nothing in the suspension file; no `src/` file, build, test, golden, corpus of scores, or anything under
`tools/corpus/` or `tools/robust_stop/`; no measurement of the analysis; no governing document edited except
`STATUS.md` and `STATUS_ARCHIVE.md`.

## 12. The plan's tell, in one sentence

**Did this batch produce anything other than the landed paths, the freeze, the three generator edits, the derivation
tool's parameter and artifact, the enrolment, the two copies, the Task 5 files and the report?** **Yes, by absence and
by addition:** the freeze and the three generator edits were NOT produced (Task 1 stopped; Task 2 not performed);
Task 0 carries the regenerated `tools/audit/evidence_pin_membership.json`, as its act (2) orders; the end-state commit
carries the artifacts A2's classing regenerates beside `tools/audit/guard_state.json`; and two diagnosis scripts were
run outside the repository (§9 item 2). Nothing else.

## 13. The standing self-check (D-434) over this batch's own work

1. *Principles touched.* **#13/#3** — the surprise was surfaced as a STOP before anything was built around it, its
   cause established at the code first (D-669). **#12** — the record of what L2's session was given is untouched,
   precisely because the act that would have rewritten it was stopped; L2's derivation output and artifact proven
   byte-identical. **#6/D-623** — one derivation tool with a parameter, not a sibling. **#19** — the new derivation is
   guarded on its first commit. **#17(f)/D-431** — counts left in the artifacts and cited, except the printed set the
   dispatch orders reproduced, which is labelled as such. Conforms.
2. *Conventions.* American English in this side's prose; no self-invented label; reserved words in their musical
   senses or qualified (*decisions-register*, *open-items*, *corpus of scores*).
3. *Figures and premises.* Every commit read from its own object and the ref files; every comparison against an
   explicit hash or a whole-file `cmp`; the derived set read back at the artifact.
4. *File-tools rule.* Repository content read with the file tools, save the git object queries, the sanctioned
   scripts and the declared items of §9.
5. *Uncertainty.* No check rests on a sample; each is a whole-file comparison or a full run.

*Provenance: CC, 2026-10-15, at boot tip `5499f3e2521c2bf4478469f30f3b9fb18f0af655`, under
`cc_instruction_l3_pack_build_first_half_2026_10_15.md`, after its ordered first reads — the four 2026-10-15 L3 ruling
records and the cut-list document whole; `CLAUDE.md` at its session-start spans; `STATUS.md` and `DECISIONS.md` whole;
the gating answer located; handoff entries 408 and 409 whole; the dispatch-protocol section of
`cowork_audit_protocol.md`; the last batch's dispatch and report whole and its close; the four model dispatches at the
named tasks; the generator at its docstring, `VERDICT_DATE`, `FROZEN` whole, `CRITERION`, `criterion_is_empty`,
`criterion_block`, `group_title`, `build_subject`, `build`, `write_all`, `check_all`, `frozen_from_disk`, `main` and
`VERDICTS["l3"]`'s opening comment; `gen_l2_withheld_documents.py` and `l2_withheld_documents.json` whole;
`gen_guard_state.py` at its authored list; and `gen_status_batch_bound.py` whole at the tip's object.*
