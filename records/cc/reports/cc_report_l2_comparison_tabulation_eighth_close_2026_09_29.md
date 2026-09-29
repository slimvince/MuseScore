# CC REPORT — THE L2 COMPARISON, THE EIGHTH BATCH'S CLOSE COMPLETED UNDER ITS CLOSE DISPATCH: A3′ HELD TERM BY TERM, THE CLOSING CAPTURE IDENTICAL VERDICT FOR VERDICT, NO MEMBER OPENED (2026-09-29)

> **Executes** `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_close_2026_09_29.md`, pinned at
> blob `e011f15719bb463b2338afbbe36ea9a0e6c3a1b6` (26,605 bytes). **No STOP fired.** The halted close of the eighth
> batch was established at its objects, the one `STATUS.md` sentence was inserted and proved the only change, the five
> regenerations ran green, **A3′ held and its tally clause was checked term by term at the artifact**, and the closing
> guard capture came back **identical verdict for verdict** to the eighth batch's opening capture. **One expectation of
> the dispatch did not match the tree, and it is reported rather than built around (§1, 0(c); §5, A1′):** the dispatch
> expected nine tracked modifications at boot and there were eight, because `tools/audit/guard_state.json` — which the
> eighth report's §4.6 lists as modified — was at its committed blob. A1′'s own STOP condition (a modification at any
> OTHER tracked path) did not fire; the cause is established at the objects. **This report decides nothing**: no
> disposition, verdict, row or open question of the reading file is touched, and no recommendation is made. The eighth
> report is committed exactly as it stood (D-674). No count the population tool produces is restated in prose beyond
> what A3′'s check requires (D-431); the tool outputs are quoted verbatim at Appendix A.

---

## 0. The session-start read, and the order of work

The opening instruction named only this dispatch. The ordinary session-start read was performed before any act, as
the Conventions rule of 2026-08-29 requires: the dispatch was read first, to learn what to do; then `STATUS.md`
whole; `DECISIONS.md`'s preamble, reading guide, status table, terms table and counts (its lines 1 to 229 — **the
entry rows below line 229 were not read**, a declared departure at §6, item 1); the gating answer's location at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`. `CLAUDE.md` and the
auto-memory index reached the session's context at boot. `BUILD_AND_TEST.md` was read at the one block whose command
the guard runner executes (`corpus_arm_stamp.py --check`). Entry 270 was read whole before it was landed, and the
eighth report was read at its §4.3 to §5 and at its Appendix D sections for 0(f) and 2(c).

---

## 1. Task 0 — the records landed, and pushed

**0(a) — the pin.** `git hash-object -w`:

```
e011f15719bb463b2338afbbe36ea9a0e6c3a1b6   (this dispatch, 26,605 bytes)
c04b4e548aaa2bf68106fcf21020224d33f4857c   (entry 270, 6,572 bytes)
```

Re-hashed immediately before staging: both identical.

**0(b) — the refs**, read with the file tools: `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
`33ecea8069ae2281fb7df6c13c0e40edfe901331`; `.git/COMMIT_EDITMSG` first line *"comparison L2: row 7.168 as-at wording
corrected, no row re-tabulated"*. **Matches the FACT.**

**0(c) — A1′'s check.** `python tools/audit/changed_paths.py`, saved to scratch; its tracked lines verbatim (the
untracked lines are the standing population A1′ names — `Claude outputs/`, `Codex research inventory/`,
`docs/research_papers/polyph9-release/`, the two PDFs under `external resarch summary/`, everything under
`scratch_artifacts/`, `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` — plus the three records named
below; the full listing ends `404 changed path record(s) [worktree]`):

```
 M	STATUS.md
 M	STATUS_ARCHIVE.md
 M	tools/audit/claude_md_finer_archive.json
 M	tools/audit/defense_share.json
 M	tools/audit/gen_status_batch_bound.py
 M	tools/audit/l2_outgoing_population.json
 M	tools/audit/session_start_read_size.json
 M	tools/audit/status_batch_bound.json
```

**Eight tracked modifications, not nine.** `tools/audit/guard_state.json` is absent. Checked at the objects:

```
git hash-object tools/audit/guard_state.json                                   -> 5ba6375f905dfd6fb808669b06b3714660a44794
git rev-parse 33ecea8069ae2281fb7df6c13c0e40edfe901331:tools/audit/guard_state.json -> 5ba6375f905dfd6fb808669b06b3714660a44794
```

So the eighth batch's opening capture (its 0(f)) rewrote `guard_state.json` byte-identically to the blob committed at
the seventh batch's close (`f289884e…`, the last commit touching that path). The eighth report's §4.6 lists the file as
"Modified and uncommitted"; at the objects it was written but not modified. **This is a finding about the eighth
report's §4.6, left at its site** — the eighth report is not edited. **A modification at any other tracked path: none.**
A1′'s STOP did not fire.

Per named untracked path, `git ls-files --others --exclude-standard -- <path>` printed the path back for each of: the
eighth report, this dispatch, entry 270, and the `.mscx` — all four untracked. **Nothing staged:** `git write-tree` →
`355ca376ee3f8b898a4a4334459b7f6f05762968`; `git rev-parse 33ecea8069ae2281fb7df6c13c0e40edfe901331^{tree}` →
`355ca376ee3f8b898a4a4334459b7f6f05762968`. Equal.

**0(d) — the last bytes**, at the blob from `git hash-object -w --no-filters` (the same blob hashes as 0(a)):

```
blob e011f15719bb463b2338afbbe36ea9a0e6c3a1b6
  size bytes: 26605
  zero bytes: 0
  last 70 bytes: b'. TOWARDS the ultimate objective and TOWARDS the guiding principles.*\n'
  ends with newline byte: True
blob c04b4e548aaa2bf68106fcf21020224d33f4857c
  size bytes: 6572
  zero bytes: 0
  last 70 bytes: b'ce: Cowork, 2026-09-29 (Stockholm), the sitting booted on entry 269.*\n'
  ends with newline byte: True
```

**0(e) — the commit.** The two paths staged by explicit path; `git write-tree` → `e6fa12fbace0ccf116c9272a145a19058e3e9ae9`;
`git diff --name-status 355ca376ee3f8b898a4a4334459b7f6f05762968 e6fa12fbace0ccf116c9272a145a19058e3e9ae9`:

```
A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_close_2026_09_29.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventy.md
```

The halted close's files stayed unstaged. Commit and push:

```
[master e062715f0d] record: entry 270 and the eighth L2 tabulation close dispatch
 2 files changed, 427 insertions(+)
 create mode 100644 records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_close_2026_09_29.md
 create mode 100644 records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventy.md
```
```
To https://github.com/slimvince/MuseScore
   33ecea8069..e062715f0d  master -> master
```

Both ref files then read `e062715f0d37aa462bce056980999d73137212ce`.

**E0 — MET.** Two paths in one commit; `origin/master` at the commit; the pin proved; A1′ reported with its
enumeration, its count off by one as stated above.

---

## 2. Task 1 — the halted close, established, and the one `STATUS.md` sentence

**1(a)1 — the six artifacts against the relayed blobs:**

| Path | Working-tree blob | Relayed | Equal |
|---|---|---|---|
| `tools/audit/l2_outgoing_population.json` | `b85122cb4cdd0d7f169dca5a292f469c0a847cc0` | `b85122cb…` | yes |
| `tools/audit/defense_share.json` | `5737e5f57d9a017fbf18429d6b1b0572b8228a98` | `5737e5f5…` | yes |
| `tools/audit/session_start_read_size.json` | `2f935b25e22b54d5f507eed3db48163787247d12` | `2f935b25…` | yes |
| `tools/audit/status_batch_bound.json` | `1470dd352aefcadde722a9480821d506995d0460` | `1470dd35…` | yes |
| `tools/audit/evidence_pin_membership.json` | `54f774d82a2d2e5a9ec99b13666bd83d63ac5257` | `54f774d8…` | yes |
| `tools/audit/l0_l1_outgoing_population.json` | `e310fb57ac53f9a06f8a9295d70c17ec143e3ce3` | `e310fb57…` | yes |

(Each relayed hash was compared at its full 40 characters as the premise ledger prints it; the table shortens the
right-hand column only.)

**1(a)2 — the other five, blob and size:**

| Path | Blob | Bytes |
|---|---|---|
| `STATUS.md` | `2b6dc6f43420457a685ff7c1102c3ac02c95e407` | 12,256 |
| `STATUS_ARCHIVE.md` | `19bbaf87959469ab3b12a20584ddf979af3d5119` | 1,979,640 |
| `tools/audit/gen_status_batch_bound.py` | `3c8ae8096ba0518e1d2d1471c38828feb25ab5bc` | 132,604 |
| `tools/audit/guard_state.json` | `5ba6375f905dfd6fb808669b06b3714660a44794` | 128,360 |
| the eighth report | `7623aa0467080f2cd78971ce61134ef36c9f4f75` | 256,350 |

The eighth report's size matches the premise ledger's FACT (256,350).

**1(a)3 — read with the file tools.** `STATUS.md` line 8 begins `*Last updated: 2026-09-29 (CC —
\`records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md\``; a search for `Last updated: `
over `STATUS.md` finds line 8 alone; a search for `tabulation_seventh_2026_09_29` over `STATUS.md` finds nothing. In
`STATUS_ARCHIVE.md` the last header (its line 5773) reads *"The entries below are the PREVIOUS batch's
(`cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md`), moved verbatim out of `STATUS.md` by
`cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md` Task 2"*, and the seventh batch's entry stands under it
at line 5775, the file's last entry. The two 2026-09-02 entries stand at `STATUS.md` lines 10 and 12.
`python tools/audit/gen_status_batch_bound.py --check` — exit 0:

```
  entries moved: 1, 2,953 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**1(a)4 — the eighth report's last bytes** (`git hash-object -w --no-filters` gave the same blob):

```
blob 7623aa0467080f2cd78971ce61134ef36c9f4f75
  size bytes: 256350
  zero bytes: 0
  last 70 bytes: b' TABULATION CONTINUED FROM POSIT"\n   }\n  ],\n  "reconciliation": {\n```\n'
  ends with newline byte: True
```

The final line is a closing code fence with its newline, and there is no zero byte. The line before it,
`"reconciliation": {`, is the last line of a diff the eighth report prints in its Appendix D, which is shown there only
up to that line — that is how the diff was printed, not the file breaking off.

**1(b) — the one sentence.** A scratch script (Appendix B) read `STATUS.md` as bytes, asserted the anchor occurs
exactly once and on line 8, and inserted the text immediately before it:

```
bytes before: 12256; CRLF pairs before: 0; LF count before: 20
anchor occurrences in file: 1
anchor on line(s): [8]
bytes after: 12594; delta: 338; inserted bytes: 338
CRLF pairs after: 0; LF count after: 20
inserted text words: 50; reserved words found as whole words: []
```

New blob `fb4eae21907ae4e07eab1d9370bd33f3b4a46d23`. `git diff --stat 2b6dc6f43420457a685ff7c1102c3ac02c95e407
fb4eae21907ae4e07eab1d9370bd33f3b4a46d23` → `1 file changed, 1 insertion(+), 1 deletion(-)`; the only hunk header is
`@@ -8 +8 @@` — **one changed passage, line 8.** A second scratch script over the two blobs by explicit hash:

```
line counts: 21 -> 21
changed lines: [8]
removed bytes on line 8: 0 ''
added bytes on line 8: 338
added text: "★ **THE CLOSE HALTED AT A STOP UNDER THE DISPATCH'S OWN ASSUMPTION A3 AND WAS COMPLETED UNDER A SECOND DISPATCH**, `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_close_2026_09_29.md`, whose report `records/cc/reports/cc_report_l2_comparison_tabulation_eighth_close_2026_09_29.md` says what it accepted and why. "
text following the insertion begins: 'Per the OI-222 pointer convention this entry is a **POINTER*'
```

*How to read that output:* the script takes the longest common beginning of the two lines, and the inserted text's
leading space matches the space already standing before the anchor, so the 338 added bytes print with the space at
their end rather than their start. It is the same 338 bytes: nothing was removed, and the text as a whole is the
dispatch's fenced text. Line feeds preserved (no carriage return before or after); word-scanned, no reserved word.

**1(c) — the five regenerations, each then `--check`:**

```
gen_evidence_pin_membership regen exit:0
gen_evidence_pin_membership check exit:0
gen_l0_l1_outgoing_population regen exit:0
gen_l0_l1_outgoing_population check exit:0
gen_l2_outgoing_population regen exit:0
gen_l2_outgoing_population check exit:0
gen_defense_share regen exit:0
gen_defense_share check exit:0
gen_session_start_read_size regen exit:0
gen_session_start_read_size check exit:0
```

`gen_session_start_read_size.py` ran last. Each output is verbatim at Appendix A. The blobs against `33ecea80…`:

| Artifact | New blob | Blob at `33ecea8069ae2281fb7df6c13c0e40edfe901331` | Moved |
|---|---|---|---|
| `evidence_pin_membership.json` | `54f774d82a2d2e5a9ec99b13666bd83d63ac5257` | `54f774d82a2d2e5a9ec99b13666bd83d63ac5257` | no |
| `l0_l1_outgoing_population.json` | `e310fb57ac53f9a06f8a9295d70c17ec143e3ce3` | `e310fb57ac53f9a06f8a9295d70c17ec143e3ce3` | no |
| `l2_outgoing_population.json` | `3d6c37bc1eae7ecb8de0b10ca2a3497773caeabf` | `8d88bab3ecc78bd60249430a218eafeaadb580c0` | yes |
| `defense_share.json` | `d2d151a1112daf8a80ab44c4026c1893a3c7e7ca` | `d9be5534e2d31961de19e8b119f58d97c8f5cad0` | yes |
| `session_start_read_size.json` | `9d812c2a785b684ce662aa9690c9aad00eddc2b8` | `160d6673dba6336eb6188a66ec3f1f7eb5013fe5` | yes |

(`status_batch_bound.json` is not among the five and was not regenerated; it stands at `1470dd35…` as the eighth batch
wrote it.)

**What moved, against A3′.**

- **`l2_outgoing_population.json`** — `git diff --stat 8d88bab3ecc78bd60249430a218eafeaadb580c0
  3d6c37bc1eae7ecb8de0b10ca2a3497773caeabf` → `9 insertions(+), 3 deletions(-)`, in the two places the eighth report's
  diff shows: the tally entry for *slicing*, and the residue record of `STATUS.md` (its `hits`, one added hit record —
  line 8, term *slicing*, tier *admitting* — and the stored line text of its existing line-8 record, which is now the
  line as 1(b) left it). The zero-context diff's hunk headers and changed fields are at Appendix A.
- **`defense_share.json`** — two changed passages: `the_whole_ordinary_session_start_read` 247392 → 247644, and
  `share_of_the_whole_ordinary_session_start_read` 5.24 → 5.23. The second is the first's quotient, so both are what
  `STATUS.md`'s new size moves. (The eighth batch's regeneration left that share at 5.24 because its denominator moved
  less; the rounding changes here.)
- **`session_start_read_size.json`** — `STATUS.md` 12230 → 12482 characters (the 338 inserted bytes are 336
  characters, the ★ being three bytes), `total_characters` and the two comparisons' `to_total`,
  `change_in_characters` and `change_percent` — all what `STATUS.md`'s new size moves.

**A3′'s tally clause, checked by a scratch script over the two blobs by explicit hash** (Appendix B), which also
compares every field outside the tally and `STATUS.md`'s residue record:

```
terms in tally: old 42, new 42; key sets equal: True

term                         tally old tally new tally chg  STATUS.md old  STATUS.md new  STATUS.md chg  equal
slicing                             71        72        +1              0              1             +1  True
(terms with any change: 1)
TALLY CLAUSE HOLDS FOR EVERY TERM: True

STATUS.md residue record hits: 2 -> 3
STATUS.md residue record hit_lines_distinct: 2 -> 2
STATUS.md residue record in_the_specification_document_set: False -> False
STATUS.md residue record inventory_class: 'governing-documents' -> 'governing-documents'
STATUS.md residue hit_records: 2 -> 3

fields differing outside the tally and STATUS.md's residue record: 0
EVERY OTHER FIELD IDENTICAL: True
residue files: 168 -> 168; entered []; left []
```

So no member of the outgoing population or the tabulation population moved, and no file entered or left the
population or the residue — every other field of the artifact, the member lists among them, is identical. The inserted
sentence of 1(b) names no document carrying an admitting term and added no hit; the movement is exactly the eighth
batch's.

**A3′'s further prediction:** the eighth report, this dispatch and entry 270 were all on disk when
`gen_l2_outgoing_population.py` regenerated, and they moved nothing — the check above finds no field changed but the
two A3′ names. **Held.**

**E1 — MET.** The halted close's files established at their blobs; the one sentence inserted and proved the only
change; five regenerations green; A3′ held, its tally clause checked term by term.

---

## 3. Task 2 — the close, completed

**2(a) — the closing guard capture.** Run under the eighth batch's opening capture's environment, recorded at the
invocation: `PYTHONIOENCODING=[unset] PYTHONUTF8=[unset] Python 3.14.3`, Git Bash. The invocation that writes:
`python tools/audit/gen_guard_state.py`, exit 0, output saved to scratch and quoted whole at Appendix A. Its last line:

```
80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

**Against the eighth report's Appendix D, 0(f)**, by a scratch script that extracted the opening capture from the
eighth report's blob `7623aa04…` and compared (Appendix B):

```
opening verdict lines: 103; closing verdict lines: 103
same invocations in the same order: True
verdicts differing: 0
opening counts: {'PASS': 68, 'FAIL': 12, 'NOT RUN': 4, 'HISTORICAL': 19}
closing counts: {'PASS': 68, 'FAIL': 12, 'NOT RUN': 4, 'HISTORICAL': 19}
closing FAIL set:
  tools/audit/gen_phase3_gate_partition.py --check
  tools/audit/gen_filing_convention_application.py --check
  tools/audit/gen_artifact_inventory.py --check
  tools/audit/gen_artifact_inventory_surface.py --check
  tools/audit/gen_test_construction_evidence.py --check
  tools/audit/gen_retirement_caller_check.py --check
  tools/audit/decisions/apply_soft_discard.py --check
  tools/audit/decisions/apply_residue_discard.py --check
  tools/audit/gen_epoch_write_path.py --check
  tools/audit/gen_recognizer_establishment_sort.py --check
  tools/audit/decisions/gen_home_classification.py --check
  tools/audit/decisions/gen_phase1p_delegation_bar.py --check
opening summary: ['80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)']
closing summary: ['80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)']
closing lines that are neither a verdict nor the summary: ['wrote tools\\audit\\guard_state.json']
```

**Identical verdict for verdict.** `python tools/audit/gen_guard_classification.py` — exit 2:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

Exactly the four names A2′ predicts.

**What moved in `guard_state.json`.** New blob `c343eb2544ddb3d191a22d33a958d4ed7db79f25` against
`5ba6375f905dfd6fb808669b06b3714660a44794`: three changed passages, all inside captured tool output and none in a
verdict — the forward-bound check's `entries moved: 1, 2,908 characters` → `2,953 characters` (the eighth batch moved
a different entry than the seventh did), and the session-start read size and defense-share lines that follow
`STATUS.md`'s size. The diff is at Appendix A. This file therefore differs from its committed blob now, where after the
eighth batch's opening capture it did not; it is committed at Task 3.

**2(b) — this report.** Written; the eighth report is not edited.

**E2 — MET at the working tree that the close commit carries**: population 80; zero STOPs in the runner; the failing
set exactly the twelve, plus none; the classification STOP unchanged. *Bound, declared:* the capture was taken at the
working tree before the commit. For every tracked path the close commit carries, the working tree and the commit hold
the same blob, and the only other tracked modification in the tree at the capture, `tools/audit/claude_md_finer_archive.json`,
is held back from the commit as it was from every earlier close; this report itself did not exist when the capture ran.

---

## 4. Task 3 — commit and push

Carried out after this report is written; its staged-set proof, the commit, the push and A5′'s proof are reported in
the session's closing message, because a commit cannot contain the proof of its own contents (§6, item 4). **The
staged set planned**, by explicit path: `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`,
`tools/audit/status_batch_bound.json`, `tools/audit/l2_outgoing_population.json`, `tools/audit/defense_share.json`,
`tools/audit/session_start_read_size.json`, `tools/audit/guard_state.json`, the eighth report, and this report.
`evidence_pin_membership.json` and `l0_l1_outgoing_population.json` are not in it — their blobs equal those at
`33ecea80…`. **Held back:** `tools/audit/claude_md_finer_archive.json`, the untracked research paths, the untracked
`.mscx`, everything under `scratch_artifacts/`.

---

## 5. The assumptions and expected results, graded

- **A1′ — HELD in its STOP condition, WRONG in its count.** No modification at any tracked path outside the nine it
  names. But eight of the nine were modified, not nine: `tools/audit/guard_state.json` was at its committed blob
  (§1, 0(c)). The count came from the eighth report's §4.6, which calls that file modified; A1′ says it rests on that
  section. The untracked population matched.
- **A2′ — HELD.** Population 80; the same twelve FAIL; the four NOT RUN and nineteen HISTORICAL identical; every PASS
  still PASS; the classification STOP naming exactly the four tools.
- **A3′ — HELD.** `evidence_pin_membership.json` and `l0_l1_outgoing_population.json` did not move;
  `l2_outgoing_population.json` moved only in `STATUS.md`'s residue record and in `hits_per_term`, the one changed
  term's tally change equal to its change in that record's hit records; `defense_share.json` and
  `session_start_read_size.json` moved only in what `STATUS.md`'s new size moves. The further prediction (the three
  records on disk move nothing) held.
- **A4′ — HELD.** No tool source was touched in this dispatch; the forward bound was not re-aimed; no tool added or
  enrolled; population 80.
- **A5′ — graded in the closing message**, by `git diff --name-status` between
  `33ecea8069ae2281fb7df6c13c0e40edfe901331` and the close commit (§4). The paths this dispatch wrote are exactly those
  §4 lists plus the two records of Task 0; nothing else in the tree was written by it — the reading file, every tool
  source, every governing document other than `STATUS.md`, and the eighth report (blob `7623aa04…`, committed as
  hashed at 1(a)2) were not edited.
- **E0, E1, E2 — MET** (§1, §2, §3).

---

## 6. Declared departures

1. **`DECISIONS.md` was read at its lines 1 to 229, not whole.** The preamble, the reading guide, the status and
   terms tables and the counts were read; the entry rows were not. The entries this dispatch cites (D-431, D-643,
   D-672, D-674) were not opened. Nothing in this dispatch applies or changes a decision.
2. **One `python -c` over a pipe.** At 1(b), the hunk headers of `git diff -U0` between the two `STATUS.md` blobs
   (literal hashes) were printed by `| python -c "…"` reading standard input. It was aimed at no repository or scratch
   path, but it is a `python -c` code string, which the shell rules otherwise keep to script files; its output
   (`['@@ -8 +8 @@']`) was then confirmed by the script-file proof quoted at 1(b).
3. **One `git log`, over one path, for history only.** At 0(c), `git log --format="%H %s" -3 -- tools/audit/guard_state.json`
   was run to find which commit last wrote that file, while establishing why it was not modified. It was not used
   to decide what is current; that was decided by the two blob hashes quoted at 0(c).
4. **Task 3's proofs are not in this report**, as §4 says: this report is itself one of the files the close commit
   carries, so the commit's hash, its staged-set proof and A5′'s `git diff --name-status` exist only after the report
   is written. They are reported in the session's closing message.
5. **One shell call refused by the repository's shell-read guard:** an `ls -l` over the regeneration output files in
   scratch, written with a relative pattern. It returned nothing and was not retried; the files were read with the
   file tools instead.

---

## 7. The plan's tell

**Did this dispatch produce anything other than the two landed records, the one `STATUS.md` sentence, the
regenerated artifacts, the closing capture and this report?** No — beyond those, it produced only scratch files
outside the repository, and it commits the files the halted close had already written, as Task 3 orders.

---

## 8. What this report does NOT do

It opens no member: position 43 onward stays UNTOUCHED, and the reading file is not edited. It edits neither the
eighth report nor any tool source, source of the open-items register or the decisions register, derivation, brief, boot pack, input contract or outgoing text. It
creates, flips or discards no open-items row, allocates no decisions-register identity, re-aims no forward bound,
enrolls no tool, and freezes no pack. The eighth report's findings stay at their sites; the finding about its §4.6 above
is reported, not repaired. No `src/` file, build, test, golden, corpus of scores or measurement of the analysis.

---

## Appendix A — tool outputs, verbatim

### 1(c), `gen_evidence_pin_membership.py`

```
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 102
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
```

### 1(c), `gen_evidence_pin_membership.py --check`

```
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 102
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
```

### 1(c), `gen_l0_l1_outgoing_population.py`

```
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
```

### 1(c), `gen_l0_l1_outgoing_population.py --check`

```
l0_l1_outgoing_population.json re-derives
```

### 1(c), `gen_l2_outgoing_population.py`

```
item 1: ## The joint estimator — the standing rules of the production inference layer — 286 lines
item 1: #### Layer 3 — key/mode is the sequence decoder — 207 lines
item 1: #### Layer 4 — the per-slice chord-symbol decoder — 140 lines
item 1: #### Layer 5 — the function/cadence layer — 117 lines
item 2: 20 distinct names, 20 resolve (1123671 bytes), 8 in the specification set
item 3: 26 in-set files with a hit, 2664 distinct hit lines over them (ARCHITECTURE.md inside the four spans: 87, outside: 683); residue files: 168
item 4: in a specification-set member — 56
item 4: in an item-2 document that resolves — 28
item 4: inside item 1 — 19
item 4: reached by item 4 alone — 8
transfer span: 287 lines
tabulation population: 62 members, 14232 lines, 1317940 bytes
wrote C:\s\MS\tools\audit\l2_outgoing_population.json
```

### 1(c), `gen_l2_outgoing_population.py --check`

```
l2_outgoing_population.json re-derives
```

### 1(c), `gen_defense_share.py`

```
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
    of the whole session-start read (247644): 5.23%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

### 1(c), `gen_defense_share.py --check`

```
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
    of the whole session-start read (247644): 5.23%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

### 1(c), `gen_session_start_read_size.py`

```
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
    STATUS.md                                                                 12482
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 247644
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 247644 [ruled membership]  (-119477, -32.54%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 247644 [ruled membership]  (-49188, -16.57%)  <- CROSSES A REGIME BOUNDARY
```

### 1(c), `gen_session_start_read_size.py --check`

```
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
    STATUS.md                                                                 12482
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 247644
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 247644 [ruled membership]  (-119477, -32.54%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 247644 [ruled membership]  (-49188, -16.57%)  <- CROSSES A REGIME BOUNDARY
```

### 1(c), `defense_share.json` diff

```
diff --git a/d9be5534e2d31961de19e8b119f58d97c8f5cad0 b/d2d151a1112daf8a80ab44c4026c1893a3c7e7ca
index d9be5534e2..d2d151a111 100644
--- a/d9be5534e2d31961de19e8b119f58d97c8f5cad0
+++ b/d2d151a1112daf8a80ab44c4026c1893a3c7e7ca
@@ -77,7 +77,7 @@
  ],
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
   "the_six_session_start_spans": 104609,
-  "the_whole_ordinary_session_start_read": 247392,
+  "the_whole_ordinary_session_start_read": 247644,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
  "per_span": [
@@ -142,7 +142,7 @@
   "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
   "characters_had_every_clause_run_to_its_paragraph_end": 160906,
   "share_of_the_six_session_start_spans": 12.39,
-  "share_of_the_whole_ordinary_session_start_read": 5.24
+  "share_of_the_whole_ordinary_session_start_read": 5.23
  },
  "every_clause_published_so_the_tables_reach_is_inspectable_rather_than_asserted": [
   {
```

### 1(c), `session_start_read_size.json` diff

```
diff --git a/160d6673dba6336eb6188a66ec3f1f7eb5013fe5 b/9d812c2a785b684ce662aa9690c9aad00eddc2b8
index 160d6673db..9d812c2a78 100644
--- a/160d6673dba6336eb6188a66ec3f1f7eb5013fe5
+++ b/9d812c2a785b684ce662aa9690c9aad00eddc2b8
@@ -176,11 +176,11 @@
   },
   "characters_per_member": {
    "CLAUDE.md": 104609,
-   "STATUS.md": 12230,
+   "STATUS.md": 12482,
    "DECISIONS.md": 127727,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 247392,
+  "total_characters": 247644,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
     "characters": 62498,
@@ -276,10 +276,10 @@
    "from_commit": "1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 247392,
+   "to_total": 247644,
    "to_regime": "ruled membership",
-   "change_in_characters": -119729,
-   "change_percent": -32.61,
+   "change_in_characters": -119477,
+   "change_percent": -32.54,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   },
@@ -287,10 +287,10 @@
    "from_commit": "594074e1e1900079e449d2b79a38920d21bca6e6",
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 247392,
+   "to_total": 247644,
    "to_regime": "ruled membership",
-   "change_in_characters": -49440,
-   "change_percent": -16.66,
+   "change_in_characters": -49188,
+   "change_percent": -16.57,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   }
```

### 1(c), `l2_outgoing_population.json` diff, zero context — the hunk headers and the short changed lines

`git diff -U0 8d88bab3ecc78bd60249430a218eafeaadb580c0 3d6c37bc1eae7ecb8de0b10ca2a3497773caeabf`, searched for its hunk
headers and its short changed fields; the three long changed lines — the added record's stored line text, and the
existing line-8 record's stored line text before and after — are each one whole `STATUS.md` line 8, the "after" being
the line as 1(b) left it, and are not repeated here:

```
@@ -775 +775 @@
-    "slicing": 71,
+    "slicing": 72,
@@ -40134 +40134 @@
-     "hits": 2,
+     "hits": 3,
@@ -40136,0 +40137,6 @@
+       "line_number": 8,
+       "term": "slicing",
+       "tier": "admitting",
@@ -40141 +40147 @@
```

### 2(a), the closing guard capture — `python tools/audit/gen_guard_state.py`

```
wrote tools\audit\guard_state.json
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
  [PASS] tools/audit/gen_l0_l1_outgoing_population.py --check
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
  [PASS] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [PASS] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
  [PASS] tools/audit/gen_l2_outgoing_population.py --check
  [PASS] tools/audit/decisions/gen_decisions_register.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --verify
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
  [HISTORICAL] tools/audit/gen_claude_md_finer_archive.py
  [HISTORICAL] tools/audit/gen_post_split_archive.py
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
  [HISTORICAL] tools/audit/gen_claude_md_prune_backlog.py
80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

### 2(a), `guard_state.json` diff

```
diff --git a/5ba6375f905dfd6fb808669b06b3714660a44794 b/c343eb2544ddb3d191a22d33a958d4ed7db79f25
index 5ba6375f90..c343eb2544 100644
--- a/5ba6375f905dfd6fb808669b06b3714660a44794
+++ b/c343eb2544ddb3d191a22d33a958d4ed7db79f25
@@ -1041,7 +1041,7 @@
       "exit_code": 0,
       "verdict": "PASS",
       "stdout": [
-        "  entries moved: 1, 2,908 characters",
+        "  entries moved: 1, 2,953 characters",
         "  byte-present in the archive exactly once: True",
         "  absent from the must-read:                True"
       ],
@@ -1161,15 +1161,15 @@
         "    [conditional  ] VS Code extension — bash command rules                    3013",
         "  whole file 168350, the six session-start spans 104609, overstated by 63741",
         "    CLAUDE.md                                                                104609",
-        "    STATUS.md                                                                 12230",
+        "    STATUS.md                                                                 12482",
         "    DECISIONS.md                                                             127727",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826",
-        "  total at the tree 247392",
+        "  total at the tree 247644",
         "  further spans of the same artifact, NOT counted into the read:",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951",
-        "  vs 1760d9a4a8: 367121 [whole-file practice] -> 247392 [ruled membership]  (-119729, -32.61%)  <- CROSSES A REGIME BOUNDARY",
-        "  vs 594074e1e1: 296832 [whole-file practice] -> 247392 [ruled membership]  (-49440, -16.66%)  <- CROSSES A REGIME BOUNDARY"
+        "  vs 1760d9a4a8: 367121 [whole-file practice] -> 247644 [ruled membership]  (-119477, -32.54%)  <- CROSSES A REGIME BOUNDARY",
+        "  vs 594074e1e1: 296832 [whole-file practice] -> 247644 [ruled membership]  (-49188, -16.57%)  <- CROSSES A REGIME BOUNDARY"
       ],
       "stderr": [],
       "what_it_checks": "what an ordinary session reads at session start, in characters, measured at the tree and at the recorded earlier commit's git object. It is the arc's own subject made checkable: the pruning direction of 2026-08-16 is about this number, and every act in the arc has had to state what it saved. Its load-bearing STOP is a demand about the tree AS IT STANDS — rule (a)'s artifact-and-key pointer is PARSED FROM THE CLAUSE ITSELF and must RESOLVE in the artifact it names, so a pointer that has stopped resolving fails on the day it stops rather than being hidden inside a number. It goes red when a governing surface changes, which is the point: the session-start read moved and the record does not yet say so. ★ WHAT IT DOES NOT ASSERT: that the membership is complete — it is AUTHORED, and each member carries the clause that makes it one so the authored half is checkable by reading three clauses; and nothing about whether the read is small enough, which is [[OI-370]]'s own subject"
@@ -1195,7 +1195,7 @@
         "  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends",
         "    the ruled closing reading would attribute 51684; the literal paragraph reading 160906",
         "    of the six session-start spans (104609): 12.39%",
-        "    of the whole session-start read (247392): 5.24%",
+        "    of the whole session-start read (247644): 5.23%",
         "  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,",
         "  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md)."
       ],
```

---

## Appendix B — the scratch scripts, by name and purpose

All run from the session's scratch directory with absolute paths, reading git objects by explicit hash unless stated;
none was aimed at a repository file through a shell text utility.

- `blob_tail.py` — per blob: size, count of zero bytes, last 70 bytes, final newline (0(d), 1(a)2, 1(a)4).
- `t1b_insert.py` — 1(b)'s insertion: reads `STATUS.md` as bytes, asserts the anchor once and on line 8, inserts,
  writes bytes, word-scans the inserted text against the Conventions' reserved-word inventory.
- `t1b_prove.py` — 1(b)'s proof over the two `STATUS.md` blobs: changed lines, removed and added bytes.
- `c_struct.py` — locates `hits_per_term` and `STATUS.md`'s residue record in the population artifact.
- `c_a3prime.py` — A3′'s tally clause and the every-other-field comparison over the two population blobs.
- `cmp_capture.py` — extracts the opening capture from the eighth report's blob and compares it verdict by verdict
  with the closing capture's saved output.

*Provenance: Claude Code, 2026-09-29, the session that ran the eighth batch's close dispatch, at tip `e062715f…`
(after Task 0) with `origin/master` equal.*
