# CC REPORT — THE L2 COMPARISON, THE THIRTEENTH TABULATION BATCH: POSITIONS 53 TO 61 TABULATED, EACH WHOLE; STOPPED AT THE MEMBER BOUNDARY AFTER POSITION 61 BECAUSE THE DISPATCH BOUNDED THE BATCH THERE; NOTHING DECIDED (2026-10-04)

> **STATUS: SESSION REPORT.** Claude Code, 2026-10-04 (the session opened late on 2026-10-03 and its work ran on
> 2026-10-04), executing `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`
> (pinned at Task 0 to blob `cee54d127030ca408e8d57bce9ac0920385c9a58`, 150,042 bytes). **This report decides nothing**:
> every disposition in the reading file is a proposal, nothing is applied anywhere, no recommendation is made about the
> derivation, the method or any open question, and the five questions the derivation marks for the user — OQ-L2-2, 4, 5,
> 8 and 16 — are not put. **Shape**: the user's ruling of 2026-10-03 — the check outputs that prove something are kept
> verbatim in Appendices A to C; there is no log of shell calls; every other result is stated in the body.

---

## 0. The ordered first read, and the session-start read

- **The opening instruction named only the dispatch**, so the dispatch was read first, from its working-tree path, before
  anything else (as the third to twelfth batches recorded). `CLAUDE.md` and the auto-memory index reached the context at
  boot as injected context before any tool call. **Then the derivation, `cowork_blind_derivation_l2_2026_09_27.md`, was
  read before any other file: §5 first, then §6, then §7, then the whole file.** Counted at its own structure: **49
  statements (L2-S1 to L2-S49), 18 open questions (OQ-L2-1 to OQ-L2-18), 5 of them marked ★ (OQ-L2-2, 4, 5, 8, 16)** —
  the counts of record, no difference.
- **Then, in the dispatch's order, reads (1) to (10)**: `CLAUDE.md`'s session-start spans (injected), `STATUS.md`,
  `DECISIONS.md`, `BUILD_AND_TEST.md` (its condition met: this batch runs the guard set), the gating identities, and the
  remaining reads the dispatch lists, through read (10), the targeted reads of §6.1 to §6.52 (named at §6). **The
  departures in these reads are at §5.**

## 1. Task 0 — the records landed and pushed

- **0(a) the pin.** The dispatch's blob **`cee54d127030ca408e8d57bce9ac0920385c9a58`, 150,042 bytes**; entry 275's blob
  **`5cf72cd67dee64aefd3f0fe7677e3c1bafe016c4`, 11,337 bytes** (Appendix C.2).
- **0(b) the refs and the chain.** Both ref files read **`5fa68913cbbbd421072d8384338cc623ccc7dafc`**. The chain, by `git
  show --stat` of each explicit hash (Appendix C.8): `5fa68913` (the twelfth close; parent `096b6cde`; tree `85fd48e1`; it
  carries `STATUS.md`, `STATUS_ARCHIVE.md`, the twelfth report, `tools/audit/defense_share.json`,
  `tools/audit/gen_status_batch_bound.py`, `tools/audit/guard_state.json`, `tools/audit/l2_outgoing_population.json`,
  `tools/audit/session_start_read_size.json` and `tools/audit/status_batch_bound.json`) → `096b6cde` (member 52; parent
  `7736090f`) → `7736090f` (member 51; parent `cc8acd05`) → `cc8acd05` (Task 0; parent `3d218b1c`). **The chain is the
  one the premise ledger relays.**
- **0(c) A1.** `python tools/audit/changed_paths.py` (Appendix C.1): exactly one tracked modification,
  `tools/audit/claude_md_finer_archive.json`; the two records to land untracked; the standing untracked population
  otherwise. The index tree equalled the tip's tree, `85fd48e1e15bdedf467f3e7464c7dc546aed592e`.
- **0(d) the last bytes** (Appendix C.2): both blobs end in the newline byte and carry no zero byte and no carriage return.
- **0(e) the commit.** Exactly the two paths, staged by explicit path. Commit
  **`986ada4a41b7fcdac6ba0be93b8382160afe4cc8`**, subject *"record: entry 275 and the thirteenth L2 tabulation dispatch"*,
  parent `5fa68913`, tree `33745aac87ccd01928e1ba3fbf20ca9ba076c43a`; pushed; `origin/master` read equal at the ref file.
- **0(f) the opening capture** (Appendix C.3), by the writing invocation, under **Git Bash 5.2.37(1)-release,
  `PYTHONIOENCODING` not set, `PYTHONUTF8` not set, Python 3.14.3**: population 80, **exactly A2's twelve failing**,
  `gen_evidence_pin_membership.py --check` passing. The classification exits 2 with its STOP naming exactly the four tools
  of the FACT.
- **0(g) the two blobs.** At `986ada4a` and in its tree: the derivation **`d78ac530992860d38d1f605a77a2961d5440a2f6`
  (125,549 bytes)** and the brief **`c5ff83dcad2107ac8c05ead21724cbab0d9471fd` (35,952 bytes)** — as the FACT relays.

**E0: met.**

## 2. Task 1 — the tabulation continued: positions 53 to 61

### 2.1 The capacity judgments, quoted from the capacity log (Appendix A)

Each was written out in the session as a message of its own, before any read of that member's text, and appended verbatim
to the capacity log by a scratch script. Every judgment opened its member; none stopped the batch. **The batch stopped
at the member boundary after position 61 because the dispatch bounded it there**, and position 61's own judgment says
so: *"It is the last position this batch may write; I stop at the member boundary after it."*

- **Position 53** (logged 00:24:26): *"… 232 lines, 23,317 bytes, 9 ranges, four WITHHELD homes … Judgment: I can finish
  position 53 whole and still leave room for the whole close. I open it."*
- **Position 54** (00:47:23): *"… 44 lines, 2,511 bytes, 7 ranges, no WITHHELD home … Judgment: I can finish position 54
  whole and still leave room for the close. I open it."*
- **Position 55** (00:52:20): *"… 35 lines, 2,613 bytes, 4 ranges, no WITHHELD home … I open it."*
- **Position 56** (00:58:58): *"… 7 lines, 638 bytes, 1 range, three WITHHELD homes … I open it."*
- **Position 57** (01:03:39): *"… 30 lines, 2,887 bytes, 1 range, one WITHHELD home (D-499 at 336–338) … I open it."*
- **Position 58** (01:12:07): *"… 11 lines, 973 bytes, 1 range, one WITHHELD home (D-453 at 590–591) … I open it."* — **and
  a CORRECTION logged at 01:14:11, before any read of the member's text**: the judgment's sentence *"there has been no
  compaction"* was false (§2.2); the judgment itself stood.
- **Position 59** (01:20:13): *"… 20 lines, 1,908 bytes, 1 range … One WITHHELD home: D-376 at 87–106, the whole range …
  I open it."*
- **Position 60** (01:26:42): *"… 12 lines, 1,085 bytes, 1 range, one WITHHELD home (D-571 at 69–73) … I open it."*
- **Position 61** (01:32:24): *"… 10 lines, 873 bytes, 1 range, one WITHHELD home (D-289 at line 3082) … I open it. It is
  the last position this batch may write; I stop at the member boundary after it."*

### 2.2 Compaction

**The context was compacted once: at the member boundary after position 57** — after member 57's commit
`ae7f91c21af6fcd0e16998b3cd6ebe80a1ef6bd0` was pushed and verified, and after position 58's entry had been read at the
artifact, but **before position 58's capacity judgment was written and before any of position 58's text was read**. No
member was begun before it and finished after it. The work after it continued only from the scratch files and the committed objects.
**The first judgment written after it (position 58's) wrongly said there had been no compaction**; a correction was
appended to the log before the member's text was opened (§2.1, §5).

### 2.3 The commits

| Member | Commit | Parent | Tree | Reading-file blob | Subject |
|---|---|---|---|---|---|
| 53 | `e5e5c5cf937700381b5d2ab0e50af425d42aab26` | `986ada4a` | `95177bae…` | `ddc1c29902fc4e6bbaafcb3fa1a0ca5426dd206a` | *comparison L2: member 53 tabulated - 96 outgoing statements placed, proposals only* |
| 54 | `e101c17eb415abd29af8629926f0865cc1e294dc` | `e5e5c5cf` | `43ed276d…` | `a8c3c283f206dc6d62faa2980f701b8752b1f6d5` | *comparison L2: member 54 tabulated - 5 outgoing statements placed, proposals only* |
| 55 | `202fe6e7b940d345a575baa0a8d62c0081160d4b` | `e101c17e` | `6df2333e…` | `7d79711163eeaa0c4e38c002a38a467c57709b4d` | *comparison L2: member 55 tabulated - 23 outgoing statements placed, proposals only* |
| 56 | `f2ff5aef2c559a9f54fdf90c70ee42e209f030f6` | `202fe6e7` | `d65c16af…` | `3b2bad9213ed35d6e28af5218db6ac1fd6f6a060` | *comparison L2: member 56 tabulated - 9 outgoing statements placed, proposals only* |
| 57 | `ae7f91c21af6fcd0e16998b3cd6ebe80a1ef6bd0` | `f2ff5aef` | `4b749741…` | `5269b7ed0e6d3dde72de3092d69ed0b37fb69827` | *comparison L2: member 57 tabulated - 21 outgoing statements placed, proposals only* |
| 58 | `806edbc3f5bf16a547e4de5b8920bde231af11a1` | `ae7f91c2` | `c64cb50e…` | `badc3fded1458e97636edcb877726e4cadeffe9f` | *comparison L2: member 58 tabulated - 12 outgoing statements placed, proposals only* |
| 59 | `fa2309b7e8b6f2c8d7fb32219fd504e068ee93c5` | `806edbc3` | `32cee3e1…` | `8745c0b4b75d135f112afef92582cc8f3b5468ba` | *comparison L2: member 59 tabulated - 6 outgoing statements placed, proposals only* |
| 60 | `a50b183e13e9b593029acf28f50aa978d9c73f42` | `fa2309b7` | `f59ed12c…` | `fb1bd97676c607adabef553a6efe38fc7b0f8edb` | *comparison L2: member 60 tabulated - 8 outgoing statements placed, proposals only* |
| 61 | `2f1bde426aa6fe60be6bde5a92a89a7fd7caec00` | `a50b183e` | `5370e65c…` | `e06ef1a4220f8ea5a93a9ba9138ec352bc59f33b` | *comparison L2: member 61 tabulated - 8 outgoing statements placed, proposals only* |

Each staged set was proved by the tree difference between the parent's tree and the index tree, by literal hashes (one
modified path, the reading file); each commit was verified at its object; each push was followed by `origin/master` read
equal at the ref file. The members' whole footprint, `986ada4a` to `2f1bde42`, is the reading file alone (Appendix
C.8). The banner edit rode position 53's commit, once. §0, §10, §11, §12, §13 and the §16 progress clause were updated
in each member's commit; the counts are at each member's own manifest and foot and are not restated here (D-431).

### 2.4 The seven checks, and what changed in the scripts

All seven checks ran before each member's commit, over scratch copies taken from git objects by explicit hash; the final
run before each commit is Appendix B.1 to B.9. **What the checks caught, each corrected before the commit:**

- **Member 53:** a quotation anchor not found (two locators one line off — *Ruled grammar gaps* is lines 238–240 and
  *Deriving the predicate* 240–242); the word scan found non-musical *scaled* and *flat* and two row labels carrying
  non-musical *score* in my locators. Reworded (*growing with*, *span*, *the functional-plausibility row*, *the match
  row*).
- **Member 55:** the word scan found non-musical *notes* (*remarks*); a manifest phrasing broke the draft-manifest check's
  pattern and was rewritten.
- **Member 57:** the word scan found non-musical *bar* (*criterion*); the count check found Row 57.10 without per-claim
  derived statements and axis, which were added.
- **Member 61:** the word scan found the British *labelling* twice and non-musical *rest* and *part* in my titles
  (reworded *labeling*, *remainder*, *portion*); **the build check showed the §16 clause written as *"positions 62 to 62
  are untouched"***, which the scratch build script produced when one position remained. The script was corrected to
  write *"position 62 is untouched"* and the member was rebuilt; the second run is B.9.
- **Members 58, 59 and 60:** their first runs were clean. **Members 54 and 56:** no correction is recorded in what
  survived the compaction; their final runs (B.2, B.4) are clean, the word-scan hits being the permitted forms below.
- **What the remaining word-scan hits are, read by eye:** *key*, *mode*, *notes* and *key state* in their musical
  sense; *candidate score*, *decisions register*, *open-items register* and *tie-break*, the qualified forms; and hits inside
  quotations the scan's quotation removal does not reach across a wrapped line, each a quotation of the source or of the
  derivation.

**The consistency script's FIRST run over the committed reading file (at the Task 0 commit) flagged nothing** — *"rows
parsed: 4434; travelling refs checked: 2316; as-at refs checked: 805; flags: 0"* (Appendix B.10a); it was proved on two
planted faults, both flagged (B.10b). **The coverage check was proved by deleting a quotation** (B.10c: three residue
lines reported). **The consistency script was not changed during the batch.**

**Script changes, each stated:** the twelfth batch's scripts were copied with their scratch-path constant rewritten
(`adopt_scripts.py`); **`build_member.py`'s one banner edit was re-aimed** from the twelfth dispatch's wording to this
dispatch's, before its first use, and applied in member 53's commit only; **`build_member.py`'s §16 clause gained the
one-position form** at member 61 (§2.4 above); `a5span.py`, `nextsizes.py`, `cmp_artifacts.py` and `gcompare.py` were
re-aimed to this batch's commits and capture files before their use at the close.

### 2.5 A5's span: §6.1 to §6.52 untouched

The span from `### 6.1 — ` to the line before `## 7.` at `5fa68913` against the span from `### 6.1 — ` to the separator
before `### 6.53 — ` at `2f1bde42`, both read by explicit hash, trailing newlines trimmed: **byte-identical**, 3,762,297
characters each (Appendix C.9). The build check of each member also proved the done span identical to its parent's. A
verification at the object of `2f1bde42` (Appendix C.10) finds **the twelfth batch's §0 sentence present verbatim —
nothing struck** — the thirteenth's sentence ending with its stop reason and no clause about where the writing stands,
the banner clause, §0's rows 53 to 61 DONE and 62 NOT YET TABULATED, the stop paragraph and resume pointer at position 62,
the §16 clause, and the nine new headings each after one separator.

### 2.6 The readings applied, and where they met

**No placement reading was taken new.** Where earlier readings met:

- **Position 53, the progression-schema design.** The named progression, its catalog and the recognizing consumer go to
  *L3 — The read-off facts*, travelling with Row 5.91 and the member-50 rows; descriptions of the dormant layers travel
  QUARANTINED with Rows 5.81, 6.16, 6.22(iv), 5.158 and 5.149(i); a recognizer's output fed back into the decision travels
  UNPLACED with Row 4.20(ii), L2-S49 DIFFERS as at that row; the idiom taxonomy travels UNPLACED with Row 9.30. Four
  WITHHELD homes, D-504 with D-505 nested in it, D-506 and D-509; Row 53.51 opens inside D-505's home and runs past it and
  carries a boundary mark.
- **Position 54, the language-model integration.** Four statements go to *L3* with Row 17.23(ii), one to *the second axis
  — voice leading*; the homes in the document (D-442 to D-448) lie outside the ranges.
- **Position 55, the idiom entry mapping.** The idiom statements travel UNPLACED with Row 9.30; three go to *the second
  axis — voice leading*; one is HISTORICAL.
- **Position 56, the architecture reassessment** — the first member of the kind *item 4 alone*. Every statement is a
  meta-finding whose standing was read at `DECISIONS.md` as superseded, and is HISTORICAL; the further reading below.
- **Position 57, the architecture review.** Plans to write, define or decide are HISTORICAL; content already carried
  travels with Rows 4.19, 4.20(i), 4.20(ii), 2.50(i), 7.179, 7.180, 9.20, 4.15, 4.21, 5.347, 9.5, 23.33 and 6.198(ii).
- **Position 58, the factorization's desk simulation.** The verdict, the request for ratification, the findings' plan
  and the row closure are HISTORICAL; the factor granularity is carried with Rows 1.33 to 1.36; the initial-state-only
  prior travels UNPLACED with Row 1.37 and its re-anchoring at a notated signature change is carried with Row 1.38(ii).
- **Position 59, the joint design over tonality and chord.** The bounded coupling travels UNPLACED with Row 9.323 and the
  coupled minority with Row 8.98; the forward-only contract is carried with Row 8.99(i) and quarantined with Rows 8.99(ii)
  and 8.100(i); defenses and the rejected alternative are listed.
- **Position 60, the legacy key analyzer's declared-mode change.** The small declared hint travels UNPLACED with Row 24.4;
  the code as it stood and the plans for the code are HISTORICAL; Row 60.2 opens before D-571's home and runs into it, and
  carries a boundary mark.
- **Position 61, an archived handoff entry.** The meta-principle is HISTORICAL as superseded, member 56's reading; the
  recorded measurement of the legacy tonality path is QUARANTINED with its audit questions; the status, assessment,
  decision of order and deferral are HISTORICAL.

**The further readings taken — the decisions register's standing of a decision homed in an item-4 document, read at
`DECISIONS.md`'s index:** at member 56, D-282 to D-285, each superseded (D-282 by D-115 and D-191, D-283 by D-001 and
D-096, D-284 by D-036 with D-001 and D-010, D-285 by the ratified factorization's emission design); at member 59, D-376
**SHELVED WITH EVIDENCE**, beside D-384 **LIVE**; at member 60, D-571 **SUPERSEDED IN FACT**; at member 61, D-289
**SUPERSEDED BY D-284** (and through it D-036 with D-001 and D-010, with D-288 and D-287). **Where no earlier row carries
the content** (members 56 and 61), the superseded statement is HISTORICAL. **Where an earlier row does** (members 59 and
60), the row travels with that row as the cross-member reading requires, and the decisions register's standing is stated at the row
and the manifest without moving the disposition (§7, observation 2).

**SEEN rows: none** — none of the eight homes lies in any document of positions 53 to 61, checked at the backbone. The
manifests name the decisions homed in each document that are not L2's own.

### 2.7 The members done and not done, and what the next member's size suggests

**Done: positions 53 to 61, each whole in its own commit. Not done: position 62 — UNTOUCHED**, not read for
tabulation, quoted, counted or placed. **The next writing resumes at position 62**, the L0/L1 transfer input —
`ratification_surfaces/cowork_comparison_l0_l1_reading.md` §10. Its size at the artifact is Appendix C.11: 287 lines,
21,436 bytes, one range, no item-4 identity. **That is a little under position 53, which this batch finished whole as its
first member before any compaction**, so there is no reason here to doubt that a fresh session can finish position 62
whole, opening with it. After it the population is complete, and the sections written once after the last member — §7,
§8, §9 and §14 — are what remains; their size is not measured here.

**E1: met** — for each member done: its manifest; every outgoing statement with exactly one disposition or UNPLACED with
what was read; every DIFFERS with its one-sentence difference and nothing chosen; the marks of 1(c) where they apply, the
WITHHELD homes marked and the SEEN check made at the homes; the transfer list, audit questions and proposals gathered; §0
and the §16 clause true of the file; the capacity judgment written out before each member and quoted from the log; the
seven checks run before each commit; no recommendation anywhere; position 53 committed first; no member beyond position 61
opened; A5 intact.

## 3. Task 2 — the close

- **2(a)** The `STATUS.md` entry was written first, at the top, the `Last updated: ` prefix moved to it from the twelfth
  batch's entry; it names this dispatch, names positions 53 to 61 by their documents, states that every disposition is a
  proposal and nothing is applied, that §6.1 to §6.52 were not edited, and where and why the batch stopped, and points at
  this report; no count is restated. Its word scan (Appendix C.5a): *decisions register*, the qualified name, and
  *scores* in its musical sense; nothing to change.
- **2(b)** `STATUS.md`'s object is the same blob, `c4dc0c77cdb26818a4e80db347a398e7edee745d`, at `986ada4a` and at
  `5fa68913`. The forward bound was re-aimed — `BASE_COMMIT` `986ada4a…` (was `cc8acd05…`), `PREVIOUS_BATCH_DISPATCH` the
  twelfth dispatch (was the eleventh), `ACT_DATE` **2026-10-04** (was 2026-10-03; the dispatch is dated 2026-10-03 and the
  move ran on 2026-10-04, which the head comment states), `DISPATCH` this dispatch (was the twelfth), `TASK` `"Task 2"`
  (unchanged); `MOVE_KIND` stays `"ordinary"`, `RULINGS` unchanged; this aiming appended to `PREVIOUS_AIMINGS`; the head
  comments amended, each former value named. **All five constants were read back at the source before `--apply`.**
  `--apply` and `--check` (Appendix C.5b, C.5c): **one entry moved, as predicted — the twelfth batch's**
  (`*2026-10-03 (CC — `…twelfth_2026_10_03.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 51…`), now in
  `STATUS_ARCHIVE.md` under the forward bound's header dated 2026-10-04 naming the twelfth dispatch as the previous batch
  and this dispatch's Task 2 as the act, with its prefix removed, and gone from `STATUS.md`, read at both files with the
  file tools; the two 2026-09-02 entries stay. No STOP.
- **2(c)** The five regenerations and their `--check`s, run without `PYTHONUTF8` (`PYTHONUTF8` and `PYTHONIOENCODING` both
  unset, recorded), all exit 0 (Appendix C.6). Against their blobs at `2f1bde42` (Appendix C.7):
  `evidence_pin_membership.json` and `l0_l1_outgoing_population.json` **identical**; `defense_share.json` and
  `session_start_read_size.json` moved **only in what `STATUS.md`'s new size moves**; `status_batch_bound.json` moved
  with the re-aim and the move; `l2_outgoing_population.json` moved **only in the text of `STATUS.md`'s two residue hit
  lines**, which now carry this batch's entry. **A3's tally check** (Appendix C.7): **no term's tally moved** — every
  term's tally change equals its change in `STATUS.md`'s residue hit records (none), the residue record's hits 3 → 3 and
  distinct hit lines 2 → 2; every other field outside that residue record and the tally identical;
  **`the_tabulation_population` → `the_members` identical by that path (62 and 62)**; the residue file list identical.
  **A3 holds term by term.**
- **2(d)** The closing capture ran by the writing invocation, `python tools/audit/gen_guard_state.py`, under the
  environment 0(f) recorded — Git Bash 5.2.37(1)-release, `PYTHONIOENCODING` not set, `PYTHONUTF8` not set, Python 3.14.3.
  **The two captures are identical verdict for verdict**: every PASS still PASS, the same twelve FAIL, the NOT RUN and
  HISTORICAL lines identical, population 80. **The per-tool verdicts read out of `guard_state.json` at `runs`: 80 and 80,
  identical.** `python tools/audit/gen_guard_classification.py` exits 2 with its STOP naming exactly the four tools of the
  FACT. `tools/audit/guard_state.json`'s summary at `5fa68913` and in the new file are equal, and the file moved, by
  explicit blobs `f7982ee9…` → `c242fb04…`, only inside the captured outputs of this batch's own acts: the forward bound's
  moved-entry size, and the session-start read values `STATUS.md`'s new size moves (Appendix C.4).

**E2: met**, derived from the declared start state plus this batch's footprint (P-3): at the tree carrying the close,
population 80; zero STOPs in the runner; the failing set exactly the twelve named, plus none; the classification STOP
unchanged, naming the same four tools.

## 4. The assumptions, graded

- **A1 — held.** Established by the enumeration (Appendix C.1): one tracked modification, `claude_md_finer_archive.json`,
  standing and held back; the two records landed by Task 0.
- **A2 — held.** The opening capture's failing set is exactly the twelve, `gen_evidence_pin_membership.py --check` passing.
- **A3 — held** (§3, 2(c)).
- **A4 — held.** No tool added or enrolled; the one tool source touched is the forward bound's authored aiming; population
  80 throughout.
- **A5 — held.** The derivation and the brief at the blobs `d78ac530…` and `c5ff83dc…`; and, by the tree difference
  between the boot tip's tree and the staged close set (Appendix C.12), **no path changed** in the pack directory, the boot
  pack, the input contract, the L0/L1 reading file, any outgoing text, any tool source but
  `tools/audit/gen_status_batch_bound.py`, any governing document but `STATUS.md` and `STATUS_ARCHIVE.md`, any source of
  the decisions register or the open-items register, or the twelfth report; and inside the reading file, §6.1 to §6.52 byte-identical (§2.5).

## 5. Declared departures

1. **The dispatch was read from its working-tree path before it was pinned**, because the opening instruction named only
   the dispatch; it was pinned at Task 0.
2. **Read (9) overran.** Locating position 53's entry, the read started at position 52's tail (the artifact's lines
   77306–77308) and ran on into position 54's entry (lines 77392–77409). Position 54's entry was read again, whole, at its
   own capacity judgment.
3. **Two shell commands were denied by the guard and not retried in the same form:** an `ls` aimed at a repository path
   (replaced by the file tools), and a `grep -c` over a scratch file named through a shell variable (read with the file
   tools instead). **At the close a third was denied**: a `git diff` of two blobs whose hashes were passed through shell
   variables; it was redone with the two hashes written literally (Appendix C.4d).
4. **One command carried a stray `cat > /dev/null`**, which did nothing.
5. **The coverage check's deletion proof (B.10c) ran after the first provisional run of the check on member 53's draft**,
   not before the check's first use.
6. **Position 58's capacity judgment, as first logged, said "there has been no compaction", which was false**; a
   correction was appended to the capacity log before any of the member's text was read (§2.1, §2.2). The judgment's
   conclusion did not change.
7. **One scratch script was edited through a Python heredoc that names a scratch path** (the member-61 rewording of
   `gen61.py`) — a form the dispatch excludes; the guard did not deny it. Every other scratch file was written with the
   file tools.
8. **Lines outside a member's range were seen while reading the member's text** (the reads ran across a few lines for
   sentence and section boundaries): position 58's lines 575–589 and 601–607, position 59's lines 80–86 and 107–109,
   position 60's lines 58–63 and 76–77, and position 61's lines 3076–3077 and 3088–3089. None was tabulated, quoted or
   listed.

No branch-tip query was used for a new commit's hash: each was read from the ref file. Every repository tool ran without
`PYTHONUTF8`; scratch scripts ran with it where they print text outside the console's code page. Commit messages were
passed to `git commit -F -` through a heredoc that names no path.

## 6. The targeted reads of §6.1 to §6.52, by row

On scratch copies of the reading file taken by explicit hash at each member's parent commit, by search and a short read
at the hit. **The rows the nine new members cite** — each read before it was cited, the list generated at the object of
`2f1bde42` (Appendix C.13): **1.33 to 1.38**; **2.50**; **4.15, 4.19 to 4.21**; **5.81, 5.83, 5.84, 5.90, 5.91, 5.149,
5.158, 5.243, 5.347**; **6.8, 6.16, 6.22, 6.127, 6.198**; **7.179, 7.180**; **8.96, 8.98 to 8.100**; **9.5, 9.20, 9.30,
9.323**; **10.55, 10.56**; **17.23**; **21.48, 21.49, 21.65, 21.67**; **22.98, 22.100**; **23.33**; **24.4**; **36.1**;
**43.35, 43.97**; **48.37, 48.53**; **50.2, 50.6, 50.8, 50.9, 50.15, 50.32, 50.41, 50.62, 50.70, 50.76**. **Read and not
cited**, after the compaction: Rows 1.29, 8.97, 10.2, 10.17, 10.37, 15.30, 21.31, 24.2, 24.3, 44.63, and 5.226 (reached
through Row 8.99(ii)). Searches for row titles naming the declared mode, the prior, ratification, a bounded coupling, a
unified state and a shelved step returned title lines only, among them Rows 1.39, 10.3, 10.36, 10.54 and 24.1 to 24.12. The reads
made before the compaction are not all recoverable from what survived it beyond the rows cited above; that is stated
rather than reconstructed.

## 7. Findings of the run

**None under 1(h) or the Findings section.** Three observations, no act of their own:

1. **A home cited at a single line split the sentence carrying its decision.** D-289's home is cited at line 3082 of the
   archived handoff. The sentence stating the meta-principle opens on that line and runs to line 3084, so the mark
   follows the line to claim (i) — *a second structural fix falsified* — while the decisions register's own statement of
   D-289 is claim (ii)'s content. Row 61.3's boundary mark records this and the mark was not moved.
2. **Two readings meet at rows of members 59 and 60.** The decisions register records D-376 SHELVED WITH EVIDENCE and
   D-571 SUPERSEDED IN FACT, while the earliest rows carrying the same content (Rows 9.323, 8.98 and 24.4) are UNPLACED.
   Under the cross-member reading the new rows travel with those rows; under member 56's reading a superseded statement is
   HISTORICAL. The rows travel, and state the decisions register's standing; nothing is chosen between the two.
3. **The scratch build script had no form for the last remaining position** and wrote *"positions 62 to 62"* on member
   61's first build; the build check's changed-passage listing showed it, and it was corrected before the commit (§2.4).

## 8. What this batch did not do, and the plan's tell

It booted no session, built and ran no measurement of the analysis, derived no specification statement, froze nothing,
created, flipped or discarded no open-items row, allocated no decisions-register identity, and edited no `src/` file,
test, golden, corpus, outgoing text, derivation, brief, pack, input contract, L0/L1 reading file, source of the decisions
register or the open-items register, governing document but `STATUS.md` and `STATUS_ARCHIVE.md`, or tool source but the
forward bound's authored aiming. Rows §6.1 to §6.52 were not edited, and §0's sentence on the twelfth batch stands
unchanged by the first member commit — nothing struck (§2.5). No member beyond position 61 was opened. **The plan's
tell: this batch produced nothing other than the landed records, the reading file's nine new member subsections with
their updates to §0, §10 to §13 and the §16 progress clause and the one banner edit, the Task 2 files and this report.**
This report cannot contain its own close commit's hash; see the git log.

## 9. The self-check over this batch

**Principles:** #19 — every row is an authored reading, re-placeable at the quoted texts, establishing nothing; #12 —
nothing struck in §0, §6.1 to §6.52 proven byte-identical, the former forward-bound values named in its comments, the
false capacity-log sentence corrected by an appended entry rather than edited; #6 — one row per statement, each later
statement travelling with the earliest row carrying its content; #13 — no surprise met that needed a STOP; #17(f)/D-431 —
no population count restated in `STATUS.md`, the counts living at each manifest and foot and in the generated artifacts.
**Conventions:** American English in my own prose (British spellings appear only inside quotations of the source or the
derivation); the reserved words in their musical sense or qualified, as §2.4 records. **File-tools rule:** working-tree
content read with the file tools; shell for git object queries by explicit hash, the named tools and scratch scripts,
with the departures at §5. **Uncertainty:** no difference between measured quantities is asserted.

---

# APPENDICES — the check outputs, verbatim

## Appendix A — the capacity log, whole

### A — capacity_log.txt

*Saved to the scratch file `capacity_log.txt`.*


```text
=== 2026-10-04T00:24:26 ===
Capacity judgment — position 53 (Task 1(h)), written before any read of the member's text.
Position 53: `cowork_progression_schema_design.md` passages, kind "items 3 and 4 — passages of a specification-set member", 232 lines, 23,317 bytes, 9 ranges, four WITHHELD homes (D-504 161–178, D-505 162–166 nested inside D-504's, D-506 193–194, D-509 121–128), read at the artifact. It is the first member of this batch, opened with nothing in front of it but Task 0 (D-670). The context has not been compacted. The session-start reads, Task 0, the opening guard capture (running), the blob checks and the consistency proof are done. What remains after position 53 is the whole close: the STATUS.md entry, the forward-bound re-aim and move, five regenerations with the A3 tally check, the closing guard capture and comparison, the report quoting every member's check outputs verbatim, and the close commit. The member is under half of position 46, which the tenth batch finished whole as its first member, and the twelfth batch's reusable build and check scripts are already in my scratch, re-aimed. Judgment: I can finish position 53 whole and still leave room for the whole close. I open it.
=== 2026-10-04T00:47:23 ===
Capacity judgment — position 54 (Task 1(h)), written before any read of the member's text.
Position 54: `docs/llm_integration.md` passages, kind "items 3 and 4 — passages of a specification-set member", 44 lines, 2,511 bytes, 7 ranges, no WITHHELD home (item_4_identities_inside empty), read at the artifact. Position 53 (232 lines, 23,317 bytes) was finished whole and committed without a compaction; the context has not been compacted at any point. Position 54 is about a tenth of position 53 by bytes, and the build and check scripts are in place and proved. The whole close is still owed after it (the STATUS.md entry, the forward bound, five regenerations with the A3 tally check, the closing guard capture and comparison, the report quoting every member's check outputs verbatim, the close commit), and a member this size adds little to what the report must carry. Judgment: I can finish position 54 whole and still leave room for the close. I open it.
=== 2026-10-04T00:52:20 ===
Capacity judgment — position 55 (Task 1(h)), written before any read of the member's text.
Position 55: `cowork_idiom_entry_mapping.md` passages, kind "items 3 and 4 — passages of a specification-set member", 35 lines, 2,613 bytes, 4 ranges, no WITHHELD home, read at the artifact. Positions 53 and 54 were each finished whole and committed. No compaction has occurred, and the scripts are proved and in place. A member of this size costs little, and the whole close is still owed after it (STATUS.md entry, forward bound, regenerations with the A3 check, closing capture and comparison, the report quoting every member's check outputs, the close commit). Judgment: I can finish position 55 whole and still leave room for the close. I open it.
=== 2026-10-04T00:58:58 ===
Capacity judgment — position 56 (Task 1(h)), written before any read of the member's text.
Position 56: `cowork_architecture_reassessment.md` passages, kind "item 4 — passages reached by item 4 alone" (the first member of that kind), 7 lines, 638 bytes, 1 range, three WITHHELD homes (D-283 at 107, D-284 at 108–109, D-285 at 110), read at the artifact. Positions 53 to 55 were each finished whole without a compaction. This member is tiny, but it carries three homes, and every row in it must be marked. The whole close is still owed after it. Judgment: I can finish position 56 whole and still leave room for the close. I open it.
=== 2026-10-04T01:03:39 ===
Capacity judgment — position 57 (Task 1(h)), written before any read of the member's text.
Position 57: `cowork_architecture_review_2026_07.md` passages, kind "item 4 — passages reached by item 4 alone", 30 lines, 2,887 bytes, 1 range, one WITHHELD home (D-499 at 336–338), read at the artifact. Positions 53 to 56 were finished whole with no compaction. This member is small, and the whole close is still owed after it. That close includes a report quoting every member's check outputs verbatim, which now covers five members, but each further member of this size adds little to it. Judgment: I can finish position 57 whole and still leave room for the close. I open it.
=== 2026-10-04T01:12:07 ===
Capacity judgment — position 58 (Task 1(h)), written before any read of the member's text.
Position 58: `cowork_factorization_desk_simulation.md` passages, kind "item 4 — passages reached by item 4 alone", 11 lines, 973 bytes, 1 range, one WITHHELD home (D-453 at 590–591), read at the artifact. Five members (53–57) are finished whole and there has been no compaction. My context has now grown large over five members, so I am weighing the close more heavily: I will assemble the report's verbatim check outputs from the saved check files by script rather than reading them back, which keeps the close's cost low. A member of under a kilobyte costs little. Judgment: I can finish position 58 whole and still leave room for the close. I open it.
=== 2026-10-04T01:14:11 ===
CORRECTION to the position-58 judgment above, written before any read of the member's text: its sentence "there has been no compaction" is FALSE. The context was compacted at the member boundary after position 57 (commit ae7f91c21af6fcd0e16998b3cd6ebe80a1ef6bd0), after position 58's entry was read at the artifact and before that judgment was written. I continue only from the scratch files and the committed objects. The judgment itself stands: position 58 is under a kilobyte, compaction freed room, and I can finish it whole and still leave room for the close. I open it.
=== 2026-10-04T01:20:13 ===
Capacity judgment — position 59 (Task 1(h)), written before any read of the member's text.
Position 59: `cowork_joint_key_chord_design.md` passages, kind "item 4 — passages reached by item 4 alone", 20 lines, 1,908 bytes, 1 range, read at the artifact. One WITHHELD home: D-376 at 87–106, the whole range, so every row is marked WITHHELD — D-376. Members 53–58 are finished whole. One compaction has occurred, at the member boundary after position 57; I continue from the scratch files and the committed objects, and the room it freed is ample. A two-kilobyte member costs little, and the close has room after it. Judgment: I can finish position 59 whole. I open it.
=== 2026-10-04T01:26:42 ===
Capacity judgment — position 60 (Task 1(h)), written before any read of the member's text.
Position 60: `docs/stage4b_design.md` passages, kind "item 4 — passages reached by item 4 alone", 12 lines, 1,085 bytes, 1 range, one WITHHELD home (D-571 at 69–73), read at the artifact. Members 53–59 are finished whole; one compaction has occurred, at the member boundary after position 57, and I continue from the scratch files and the committed objects. My room is ample. A member of about a kilobyte costs little, and the close has room after it. Judgment: I can finish position 60 whole. I open it.
=== 2026-10-04T01:32:24 ===
Capacity judgment — position 61 (Task 1(h)), written before any read of the member's text.
Position 61: `records/cowork/handoff/cowork_handoff_archive.md` passages, kind "item 4 — passages reached by item 4 alone", 10 lines, 873 bytes, 1 range, one WITHHELD home (D-289 at line 3082), read at the artifact. Members 53–60 are finished whole; one compaction has occurred, at the member boundary after position 57, and I continue from the scratch files and the committed objects. My room is ample. A member under a kilobyte costs little, and the close has room after it. Judgment: I can finish position 61 whole. I open it. It is the last position this batch may write; I stop at the member boundary after it.
```

## Appendix B — every member's check outputs (Task 1(g))

### B.1 — member 53: the seven checks, the final run before its commit

*Saved to the scratch file `checks_53.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_53.md disp totals [5381, 658, 111, 1307, 1538, 0, 1365, 402, 2282] axis totals [989, 845, 3603, 5437]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 119
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 9; mismatches: 0
draft manifest texts checked: 18; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 19; problems 0

===== count check (foot.py) (exit 0) =====
rows: 83 statements: 96 multi-claim rows by claim count: {2: 13}
| ADOPTED — carried | 0 | — |
| ADOPTED — proposed | 0 | — |
| RELOCATED | 56 | 53.1, 53.2, 53.3, 53.4, 53.10(i), 53.12, 53.13, 53.14, 53.15, 53.16, 53.17, 53.19(i), 53.19(ii), 53.20, 53.21, 53.22(i), 53.22(ii), 53.23, 53.26, 53.27, 53.28, 53.32, 53.33, 53.34, 53.35, 53.36, 53.37, 53.38, 53.39, 53.40, 53.43, 53.44, 53.45, 53.47(i), 53.47(ii), 53.49, 53.50(i), 53.51(i), 53.51(ii), 53.54, 53.56(ii), 53.57, 53.58(i), 53.59, 53.61, 53.62, 53.63, 53.64, 53.65, 53.67, 53.71, 53.72, 53.73(i), 53.79(i), 53.79(ii), 53.81 |
| QUARANTINED | 10 | 53.5, 53.6, 53.7, 53.8, 53.9, 53.10(ii), 53.29(ii), 53.60, 53.66, 53.68 |
| DISCARDED | 0 | — |
| HISTORICAL | 15 | 53.41, 53.42, 53.46, 53.55, 53.58(ii), 53.69, 53.73(ii), 53.74, 53.75, 53.76, 53.77, 53.78, 53.80, 53.82, 53.83 |
| UNPLACED | 15 | 53.11, 53.18(i), 53.18(ii), 53.24, 53.25, 53.29(i), 53.30, 53.31, 53.48, 53.50(ii), 53.52, 53.53(i), 53.53(ii), 53.56(i), 53.70 |
sum dispositions: 96
verdicts: {'AGREES': 12, 'DIFFERS': 17, 'SILENT': 67} total 96 rows/claims naming two or more: 0
DIFFERS: 53.5, 53.6, 53.8, 53.18(i), 53.18(ii), 53.24, 53.25, 53.29(i), 53.30, 53.31, 53.48, 53.50(ii), 53.52, 53.53(i), 53.53(ii), 53.56(i), 53.70
WITHHELD rows: ['53.30', '53.31', '53.32', '53.48', '53.49', '53.50', '53.51', '53.52', '53.53', '53.54', '53.55', '53.59']
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3762297 3762297
--- changed passage 1: replace base lines 11-11 -> new lines 11-11
  - > `records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md` Task 1, and furth
  + > `records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md` Task 1, and furth
--- changed passage 2: replace base lines 97-97 -> new lines 97-97
  - | 53 | `cowork_progression_schema_design.md` passages | NOT YET TABULATED |
  + | 53 | `cowork_progression_schema_design.md` passages | **DONE** (§6.53) |
--- changed passage 3: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 52 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 53 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 4: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 5: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 52 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 53 (D-672).** The first batch, under
--- changed passage 6: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 53**, `cowork_progression_schema_design.md` passages. §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 54**, `docs/llm_integration.md` passages. §7, §8,
--- changed passage 7: insert base lines 67979-67978 -> new lines 67979-68013
  + - Rows 53.1, 53.20, 53.26, 53.51(ii), 53.58(i), 53.62, 53.67 and 53.79(ii) — travelling with Row 5.91: a named
  +   progression and its catalog entry, the catalog queried and not owned, nothing emitted where nothing is recognized,
  +   an internally sequential entry's tonality motion carried by its schema-span, exact matches only for now, the
  +   catalog the one place a named progression is added or edited and its owner, and frequent corpus pairs the catalog
  +   lacks the evidence for growing it.
  + - Rows 53.21, 53.35, 53.49 and 53.56(ii) — travelling with Row 5.91: the consumer reading the committed progression,
  +   running its recognition over it, exposing each sequence as a typed output, and adding no layer. *(L2-S49 travels
  +   with them; Row 53.49 lies inside D-504's and D-505's homes.)*
  + - Row 53.2 — travelling with Row 50.2: a member, one chord position of an entry, by scale degree and quality.
  + - Row 53.3 — travelling with Row 50.6: the Prinner, a galant schema.
  + - Row 53.4 — travelling with Row 50.62: a substitution, one chord standing in for another of the same function.
  + - Row 53.10(i) — travelling with Row 50.70: the match, the catalog's value for a stretch realizing an entry.
  + - Rows 53.12, 53.13, 53.14, 53.33, 53.34, 53.36 to 53.40, 53.43 to 53.45 and 53.47(ii) — travelling with Row
  +   50.76(ii): the consumer's weighting of its recognitions — prior strength, admission and its threshold, the seed, the
  +   weight vector discovered from the music in three forward-only phases, the histogram and the blend, the mode cue
  +   and the factor for entries defined by their lines.
  + - Row 53.15 — travelling with Row 6.8: the punctuation-span, the grouping layer's span. *(L2-S49 travels with it.)*
  + - Rows 53.16, 53.23 and 53.72 — travelling with Row 21.48(v): the progression-schema-span, one per recognized
  +   progression, and its name. *(L2-S49 travels with Rows 53.16 and 53.23.)*
  + - Rows 53.17, 53.50(i) and 53.51(i) — travelling with Row 50.32: the harmonic sequence, at least two transposed
  +   statements of one entry, and none emitted for a single recognition of an internally sequential entry. *(Rows
  +   53.50 and 53.51 lie inside D-504's home, and claim (i) of each inside D-505's.)*
  + - Row 53.19(i) — travelling with Row 21.49(iii): the schema-span cutting across the punctuation-spans.
  + - Rows 53.19(ii) and 53.22(i) — travelling with Row 43.97(i): the recognition read-only and additive over the function
  +   layer. *(L2-S49 travels with them.)*
  + - Rows 53.22(ii), 53.28 and 53.59 — the literal Roman numeral never changed by the recognition, a substitution
  +   recorded only in the annotation. *(Rows 53.28 and 53.59 travel with Row 53.22(ii); L2-S49 travels with all three;
  +   Row 53.59 lies inside D-506's home.)*
  + - Row 53.27 — travelling with Row 50.41(i): a member filled by a substitution recorded with what the chord stands in
  +   for.
  + - Rows 53.47(i), 53.57 and 53.73(i) — travelling with Row 43.35(i): an entry defined by its lines recognized by its
  +   chord skeleton alone and marked chords-only, the scope chords only.
  + - Rows 53.61, 53.63, 53.64 and 53.79(i) — travelling with Row 50.9: the licensing grammar and the catalog not derived
  +   from each other, coupled one way by the consistency test, and a licensed pair in no entry not a gap of the catalog.
  + - Row 53.65 — travelling with Row 50.8(i): one owner per item.
--- changed passage 8: insert base lines 68056-68055 -> new lines 68091-68092
  + - Row 53.81 — travelling with Row 22.100: the voice-leading layer, a prerequisite for the half of the line-defined
  +   entries their chords do not carry.
--- changed passage 9: insert base lines 68106-68105 -> new lines 68143-68145
  + - Rows 53.32 and 53.54 — travelling with Row 6.127(iii): no new comparison frame for a recognized progression's
  +   correction, and the comparison of sequence evidence against the home-tonality confidence a new frame, declared
  +   before its wiring. *(Row 53.32 lies inside D-509's home and Row 53.54 inside D-504's.)*
--- changed passage 10: insert base lines 68373-68372 -> new lines 68413-68414
  + - Row 53.71 — the consistency test between the catalog and the licensing grammar scoped to the measured containment,
  +   a known-gap list until the amendment lands.
--- changed passage 11: replace base lines 68383-68383 -> new lines 68425-68425
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 12: insert base lines 69484-69483 -> new lines 69526-69541
  + - Row 53.5 — travelling with Row 5.81: does the dormant function layer read the progression as the dormant Layer 4's
  +   committed chord stream?
  + - Row 53.6 — travelling with Row 6.16: when does the dormant decoder abstain, on what test, and what does it hand
  +   forward?
  + - Row 53.7 — travelling with Row 6.22(iv): what confidence does the dormant decoder attach to a slice, and from which
  +   components is it computed?
  + - Row 53.8 — travelling with Row 5.158: does the dormant function layer override a confident Layer 4 commit through
  +   the selection machinery, and does it run?
  + - Rows 53.9 and 53.29(ii) — travelling with Row 5.149(i): does the dormant resolver settle a close tie-break case by
  +   functional plausibility over the stated features, with its selection rule otherwise unchanged?
  + - Row 53.10(ii) — travelling with Row 50.15(i): does the built recognizer of the catalog match only exact and whole
  +   realizations at the current commit?
  + - Rows 53.60 and 53.66 — travelling with Row 5.90: is the named licensing test the only place in the code that
  +   decides which root motions are licensed?
  + - Row 53.68 — is the built licensing test held as predicates on root motion computed from the two roots and
  +   qualities, with no table and no constants, at the current commit?
--- changed passage 13: insert base lines 70474-70473 -> new lines 70532-70548
  + - Row 53.5 — as at Row 5.81: the outgoing committed progression is *"the ordered chords the layers COMMITTED"*;
  +   L2-S34's progression term is on *"the pair of adjacent chords read as degrees in their tonalities"*.
  + - Row 53.6 — as at Row 6.16: the outgoing chord layer either *"committed"* one reading or *"abstained"*; L2-S44
  +   leaves to the charter's open DP-Q whether a sounding span may be published with no chord.
  + - Row 53.8 — as at Row 5.158: the outgoing mechanism is for *"correcting a committed reading on later evidence"*;
  +   L2-S35 normalizes *"over whole readings"*.
  + - Rows 53.18(i), 53.24, 53.25, 53.29(i), 53.48, 53.50(ii), 53.52, 53.53(i), 53.53(ii) and 53.56(i) — as at Row
  +   4.20(ii): the outgoing feeds a recognition back into the chord or tonality decision — *"the evidence
  +   contribution"* to the function layer's selection and override, the *"harmonic-sequence output"* for its
  +   tonality arbitration, *"corroboration, always"* and *"the substitute confirming channel"*; L2-S49 says *"L2
  +   consumes nothing L3 publishes"* and *"The dependency is one-way: L3 reads L2."*
  + - Rows 53.18(ii) and 53.31 — as at Row 5.243: the outgoing *"Layer 5 is the re-ranker"*, its correction
  +   *"selects"* an existing reading; L2-S11 decides the chord *"in the one decision"*.
  + - Row 53.30 — as at Row 22.98(iii): the outgoing *"the committed reading is overridden"* when the contradiction
  +   exceeds the threshold; L2-S35 normalizes *"over whole readings"*.
  + - Row 53.70 — as at Row 5.83: the outgoing amendment would *"license ascending-fifth/plagal, descending-second, the
  +   diatonic diminished-fifth"*; L2-S34 says *"Each family's weights are fitted."*
--- changed passage 14: replace base lines 70537-70537 -> new lines 70612-70613
  - | **Total** | **5285** | **658** | **111** | **1251** | **1528** | **0** | **1350** | **387** | **2246** |
  + | 53 | 96 | 0 | 0 | 56 | 10 | 0 | 15 | 15 | 36 |
  + | **Total** | **5381** | **658** | **111** | **1307** | **1538** | **0** | **1365** | **402** | **2282** |
--- changed passage 15: replace base lines 70539-70539 -> new lines 70615-70615
  - **The arithmetic check:** 658 + 111 + 1251 + 1528 + 0 + 1350 + 387 = 5285, against 5285 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 658 + 111 + 1307 + 1538 + 0 + 1365 + 402 = 5381, against 5381 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 16: replace base lines 70597-70597 -> new lines 70673-70674
  - | **Total** | **977** | **828** | **3536** | **5341** |
  + | 53 | 12 | 17 | 67 | 96 |
  + | **Total** | **989** | **845** | **3603** | **5437** |
--- changed passage 17: replace base lines 70599-70599 -> new lines 70676-70676
  - **The arithmetic check:** 977 + 828 + 3536 = 5341 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
  + **The arithmetic check:** 989 + 845 + 3603 = 5437 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
--- changed passage 18: replace base lines 70630-70630 -> new lines 70707-70707
  -   untouched: positions 1 to 52 are done, positions 53 to 62 are untouched.
  +   untouched: positions 1 to 53 are done, positions 54 to 62 are untouched.
changed passages outside the member: 18
member lines: 1176
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
BRITISH realises | oing statement.*  this stretch of the committed progression realises this entry  — §0, the terms, the match row (locator: lines 
BRITISH recognised |  candidate reading fills the member position of an admitted recognised progression  — §4.3, the evidence contribution (locator: li
RESERVED scale |  — a member: one chord position of an entry, specifying the scale degree and quality a chord must realize.**  *Outgoing state
RESERVED tie | eshold growing with its confidence; the incumbent kept on a tie-break; one override per pass.**  *Outgoing statement.*   — 
RESERVED notes | ction selects an existing reading, never one built from the notes.** *WITHHELD — D-509.*  *Outgoing statement.*   — §4.3, the
RESERVED mode | ts*, travelling with Row 50.76(ii).  ---  **Row 53.45 — the mode cue: a contradicting mode tag lowers prior strength by a de
RESERVED mode | 0.76(ii).  ---  **Row 53.45 — the mode cue: a contradicting mode tag lowers prior strength by a declared factor, never to ze
RESERVED key | ality.** *WITHHELD — D-504, D-505.*  *Outgoing statement.*  key  — §4.6, harmonic sequences as tonality evidence (locator: 
RESERVED root | ---  **Row 53.68 — the licensing test held as predicates on root motion, with no table and no constants.**  *Outgoing statem
RESERVED root | uestion:* is the built licensing test held as predicates on root motion computed from the two roots and qualities, with no t
RESERVED roots | est held as predicates on root motion computed from the two roots and qualities, with no table and no constants, at the curre

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4517; travelling refs checked: 2397; as-at refs checked: 833; flags: 0
```

### B.2 — member 54: the seven checks, the final run before its commit

*Saved to the scratch file `checks_54.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_54.md disp totals [5386, 658, 111, 1312, 1538, 0, 1365, 402, 2316] axis totals [993, 845, 3604, 5442]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 39
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 7; mismatches: 0
draft manifest texts checked: 14; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 0; problems 0

===== count check (foot.py) (exit 0) =====
rows: 5 statements: 5 multi-claim rows by claim count: {}
| ADOPTED — carried | 0 | — |
| ADOPTED — proposed | 0 | — |
| RELOCATED | 5 | 54.1, 54.2, 54.3, 54.4, 54.5 |
| QUARANTINED | 0 | — |
| DISCARDED | 0 | — |
| HISTORICAL | 0 | — |
| UNPLACED | 0 | — |
sum dispositions: 5
verdicts: {'AGREES': 4, 'DIFFERS': 0, 'SILENT': 1} total 5 rows/claims naming two or more: 0
DIFFERS: none
WITHHELD rows: []
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3835104 3835104
--- changed passage 1: replace base lines 98-98 -> new lines 98-98
  - | 54 | `docs/llm_integration.md` passages | NOT YET TABULATED |
  + | 54 | `docs/llm_integration.md` passages | **DONE** (§6.54) |
--- changed passage 2: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 53 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 54 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 3: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 4: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 53 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 54 (D-672).** The first batch, under
--- changed passage 5: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 54**, `docs/llm_integration.md` passages. §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 55**, `cowork_idiom_entry_mapping.md` passages. §7, §8,
--- changed passage 6: insert base lines 69193-69192 -> new lines 69193-69195
  + - Rows 54.1, 54.2, 54.3 and 54.4 — travelling with Row 17.23(ii): the analysis the language-model integration is
  +   handed — the chord symbols and the Roman-numeral analysis, the tonality and mode, and where the chords change.
  +   *(L2-S49 travels with them.)*
--- changed passage 7: insert base lines 69272-69271 -> new lines 69275-69275
  + - Row 54.5 — the voice-leading assessments the language-model integration is handed.
--- changed passage 8: replace base lines 69604-69604 -> new lines 69608-69608
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 9: replace base lines 71792-71792 -> new lines 71796-71797
  - | **Total** | **5381** | **658** | **111** | **1307** | **1538** | **0** | **1365** | **402** | **2282** |
  + | 54 | 5 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 34 |
  + | **Total** | **5386** | **658** | **111** | **1312** | **1538** | **0** | **1365** | **402** | **2316** |
--- changed passage 10: replace base lines 71794-71794 -> new lines 71799-71799
  - **The arithmetic check:** 658 + 111 + 1307 + 1538 + 0 + 1365 + 402 = 5381, against 5381 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 658 + 111 + 1312 + 1538 + 0 + 1365 + 402 = 5386, against 5386 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 11: replace base lines 71853-71853 -> new lines 71858-71859
  - | **Total** | **989** | **845** | **3603** | **5437** |
  + | 54 | 4 | 0 | 1 | 5 |
  + | **Total** | **993** | **845** | **3604** | **5442** |
--- changed passage 12: replace base lines 71855-71855 -> new lines 71861-71861
  - **The arithmetic check:** 989 + 845 + 3603 = 5437 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
  + **The arithmetic check:** 993 + 845 + 3604 = 5442 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
--- changed passage 13: replace base lines 71886-71886 -> new lines 71892-71892
  -   untouched: positions 1 to 53 are done, positions 54 to 62 are untouched.
  +   untouched: positions 1 to 54 are done, positions 55 to 62 are untouched.
changed passages outside the member: 13
member lines: 182
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
RESERVED mode | ord symbols, the > Roman-numeral analysis, the tonality and mode, where the chords change — it is a consumer reading the dec
RESERVED mode | els with it.)*  ---  **Row 54.3 — the inferred tonality and mode handed to the language model.**  *Outgoing statement.*   — 
RESERVED note | oins its records. 4.  What chord symbol is sounding at this note?  (415–416) — *a statement about a product tool outside the

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4522; travelling refs checked: 2401; as-at refs checked: 837; flags: 0
```

### B.3 — member 55: the seven checks, the final run before its commit

*Saved to the scratch file `checks_55.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_55.md disp totals [5409, 658, 111, 1315, 1538, 0, 1366, 421, 2322] axis totals [993, 845, 3627, 5465]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 28
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 4; mismatches: 0
draft manifest texts checked: 8; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 0; problems 0

===== count check (foot.py) (exit 0) =====
rows: 22 statements: 23 multi-claim rows by claim count: {2: 1}
| ADOPTED — carried | 0 | — |
| ADOPTED — proposed | 0 | — |
| RELOCATED | 3 | 55.18, 55.20, 55.21(ii) |
| QUARANTINED | 0 | — |
| DISCARDED | 0 | — |
| HISTORICAL | 1 | 55.21(i) |
| UNPLACED | 19 | 55.1, 55.2, 55.3, 55.4, 55.5, 55.6, 55.7, 55.8, 55.9, 55.10, 55.11, 55.12, 55.13, 55.14, 55.15, 55.16, 55.17, 55.19, 55.22 |
sum dispositions: 23
verdicts: {'AGREES': 0, 'DIFFERS': 0, 'SILENT': 23} total 23 rows/claims naming two or more: 0
DIFFERS: none
WITHHELD rows: []
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3849165 3849165
--- changed passage 1: replace base lines 99-99 -> new lines 99-99
  - | 55 | `cowork_idiom_entry_mapping.md` passages | NOT YET TABULATED |
  + | 55 | `cowork_idiom_entry_mapping.md` passages | **DONE** (§6.55) |
--- changed passage 2: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 54 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 55 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 3: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 4: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 54 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 55 (D-672).** The first batch, under
--- changed passage 5: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 55**, `cowork_idiom_entry_mapping.md` passages. §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 56**, `cowork_architecture_reassessment.md` passages (item 4 alone). §7, §8,
--- changed passage 6: insert base lines 69461-69460 -> new lines 69461-69463
  + - Rows 55.18, 55.20 and 55.21(ii) — a voicing substitution outside the idioms, and the galant schemata and the line
  +   cliché defined by their voice leading, their identity the voice-leading axis's. *(Row 55.18 travels with Row
  +   21.67, Rows 55.20 and 55.21(ii) with Row 21.65.)*
--- changed passage 7: replace base lines 69793-69793 -> new lines 69796-69796
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 8: replace base lines 71982-71982 -> new lines 71985-71986
  - | **Total** | **5386** | **658** | **111** | **1312** | **1538** | **0** | **1365** | **402** | **2316** |
  + | 55 | 23 | 0 | 0 | 3 | 0 | 0 | 1 | 19 | 6 |
  + | **Total** | **5409** | **658** | **111** | **1315** | **1538** | **0** | **1366** | **421** | **2322** |
--- changed passage 9: replace base lines 71984-71984 -> new lines 71988-71988
  - **The arithmetic check:** 658 + 111 + 1312 + 1538 + 0 + 1365 + 402 = 5386, against 5386 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 658 + 111 + 1315 + 1538 + 0 + 1366 + 421 = 5409, against 5409 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 10: replace base lines 72044-72044 -> new lines 72048-72049
  - | **Total** | **993** | **845** | **3604** | **5442** |
  + | 55 | 0 | 0 | 23 | 23 |
  + | **Total** | **993** | **845** | **3627** | **5465** |
--- changed passage 11: replace base lines 72046-72046 -> new lines 72051-72051
  - **The arithmetic check:** 993 + 845 + 3604 = 5442 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
  + **The arithmetic check:** 993 + 845 + 3627 = 5465 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
--- changed passage 12: replace base lines 72077-72077 -> new lines 72082-72082
  -   untouched: positions 1 to 54 are done, positions 55 to 62 are untouched.
  +   untouched: positions 1 to 55 are done, positions 56 to 62 are untouched.
changed passages outside the member: 12
member lines: 352
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
RESERVED mode | s at Row 9.30.  ---  **Row 55.4 — the two cross-attributes, mode and chromaticism, tagged separately per entry.**  *Outgoing
RESERVED resolution | as read:* as at Row 9.30.  ---  **Row 55.16 — the deceptive resolution tagged with the second idiom.**  *Outgoing statement.*   — 
RESERVED mode |  Row 21.65.  ---  **Row 55.22 — each entry also tagged with mode and chromaticism, independently of the idiom.**  *Outgoing 

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4544; travelling refs checked: 2423; as-at refs checked: 837; flags: 0
```

### B.4 — member 56: the seven checks, the final run before its commit

*Saved to the scratch file `checks_56.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_56.md disp totals [5418, 658, 111, 1315, 1538, 0, 1375, 421, 2323] axis totals [993, 848, 3633, 5474]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 7
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 1; mismatches: 0
draft manifest texts checked: 2; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 7; problems 0

===== count check (foot.py) (exit 0) =====
rows: 6 statements: 9 multi-claim rows by claim count: {2: 3}
| ADOPTED — carried | 0 | — |
| ADOPTED — proposed | 0 | — |
| RELOCATED | 0 | — |
| QUARANTINED | 0 | — |
| DISCARDED | 0 | — |
| HISTORICAL | 9 | 56.1, 56.2, 56.3(i), 56.3(ii), 56.4(i), 56.4(ii), 56.5(i), 56.5(ii), 56.6 |
| UNPLACED | 0 | — |
sum dispositions: 9
verdicts: {'AGREES': 0, 'DIFFERS': 3, 'SILENT': 6} total 9 rows/claims naming two or more: 0
DIFFERS: 56.3(i), 56.3(ii), 56.5(i)
NEAREST L2-S38 56.3
WITHHELD rows: ['56.3', '56.4', '56.5']
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3864943 3864943
--- changed passage 1: replace base lines 100-100 -> new lines 100-100
  - | 56 | `cowork_architecture_reassessment.md` passages (item 4 alone) | NOT YET TABULATED |
  + | 56 | `cowork_architecture_reassessment.md` passages (item 4 alone) | **DONE** (§6.56) |
--- changed passage 2: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 55 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 56 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 3: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 4: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 55 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 56 (D-672).** The first batch, under
--- changed passage 5: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 56**, `cowork_architecture_reassessment.md` passages (item 4 alone). §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 57**, `cowork_architecture_review_2026_07.md` passages (item 4 alone). §7, §8,
--- changed passage 6: replace base lines 70151-70151 -> new lines 70151-70151
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 7: insert base lines 72275-72274 -> new lines 72275-72280
  + - Row 56.3(i) — the outgoing says *"Never learn keys"*; L2-S38 says *"Every weight of the candidate score is fitted
  +   from annotated music, not set by hand."*
  + - Row 56.3(ii) — the outgoing lever is *"keychain structure (cadence precision)"*; L2-S34 says *"confirmation is
  +   carried by the progression term over proposed chords, not by a separate detector"*.
  + - Row 56.5(i) — the outgoing embellishment is *"chord-first"*, with a *"post-process"*; L2-S23 says *"The
  +   assignments are part of the one decision."*
--- changed passage 8: replace base lines 72341-72341 -> new lines 72347-72348
  - | **Total** | **5409** | **658** | **111** | **1315** | **1538** | **0** | **1366** | **421** | **2322** |
  + | 56 | 9 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 1 |
  + | **Total** | **5418** | **658** | **111** | **1315** | **1538** | **0** | **1375** | **421** | **2323** |
--- changed passage 9: replace base lines 72343-72343 -> new lines 72350-72350
  - **The arithmetic check:** 658 + 111 + 1315 + 1538 + 0 + 1366 + 421 = 5409, against 5409 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 658 + 111 + 1315 + 1538 + 0 + 1375 + 421 = 5418, against 5418 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 10: replace base lines 72404-72404 -> new lines 72411-72412
  - | **Total** | **993** | **845** | **3627** | **5465** |
  + | 56 | 0 | 3 | 6 | 9 |
  + | **Total** | **993** | **848** | **3633** | **5474** |
--- changed passage 11: replace base lines 72406-72406 -> new lines 72414-72414
  - **The arithmetic check:** 993 + 845 + 3627 = 5465 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
  + **The arithmetic check:** 993 + 848 + 3633 = 5474 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
--- changed passage 12: replace base lines 72437-72437 -> new lines 72445-72445
  -   untouched: positions 1 to 55 are done, positions 56 to 62 are untouched.
  +   untouched: positions 1 to 56 are done, positions 57 to 62 are untouched.
changed passages outside the member: 12
member lines: 164
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
RESERVED register | a meta-finding of a dated reassessment, which the decisions register records as superseded (D-282, by D-115 and D-191).  ---  **
RESERVED register | a meta-finding of a dated reassessment, which the decisions register records as superseded (D-282, by D-115 and D-191).  ---  **
RESERVED register | a meta-finding of a dated reassessment, which the decisions register records as superseded (D-283, by D-001 and D-096). (ii) **H
RESERVED register | a meta-finding of a dated reassessment, which the decisions register records as superseded (D-284, by D-036 with D-001 and D-010
RESERVED notes | hord tones; (ii) never by re-deriving the chord from pooled notes, and never by a wider chord vocabulary.  *Derived statement
RESERVED register | a meta-finding of a dated reassessment, which the decisions register records as superseded (D-285, by the ratified factorization

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====
RESERVED keys | EW =   S11 = [] S12_PROP = [] S12_DIFF = [      Never learn keys\ Every weight of the candidate score is fitted   from annot
RESERVED score | FF = [      Never learn keys\ Every weight of the candidate score is fitted   from annotated music, not set by hand.\ ,      
RESERVED part | or\ ,      chord-first\ post-process\ The   assignments are part of the one decision.\ , ] S13_DISP = [9, 0, 0, 0, 0, 0, 9, 

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4550; travelling refs checked: 2423; as-at refs checked: 837; flags: 0
```

### B.5 — member 57: the seven checks, the final run before its commit

*Saved to the scratch file `checks_57.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_57.md disp totals [5439, 661, 112, 1320, 1538, 0, 1385, 423, 2325] axis totals [998, 849, 3649, 5496]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 15
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 1; mismatches: 0
draft manifest texts checked: 2; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 3; problems 0

===== count check (foot.py) (exit 0) =====
rows: 13 statements: 21 multi-claim rows by claim count: {2: 5, 4: 1}
| ADOPTED — carried | 3 | 57.6(i), 57.6(ii), 57.13(i) |
| ADOPTED — proposed | 1 | 57.6(iv) |
| RELOCATED | 5 | 57.7(ii), 57.8, 57.10(ii), 57.11(i), 57.11(ii) |
| QUARANTINED | 0 | — |
| DISCARDED | 0 | — |
| HISTORICAL | 10 | 57.1, 57.2, 57.3, 57.4, 57.5(i), 57.5(ii), 57.7(i), 57.9, 57.10(i), 57.12 |
| UNPLACED | 2 | 57.6(iii), 57.13(ii) |
sum dispositions: 21
verdicts: {'AGREES': 5, 'DIFFERS': 1, 'SILENT': 16} total 22 rows/claims naming two or more: 1
DIFFERS: 57.6(iii)
WITHHELD rows: ['57.13']
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3874963 3874963
--- changed passage 1: replace base lines 101-101 -> new lines 101-101
  - | 57 | `cowork_architecture_review_2026_07.md` passages (item 4 alone) | NOT YET TABULATED |
  + | 57 | `cowork_architecture_review_2026_07.md` passages (item 4 alone) | **DONE** (§6.57) |
--- changed passage 2: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 56 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 57 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 3: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 4: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 56 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 57 (D-672).** The first batch, under
--- changed passage 5: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 57**, `cowork_architecture_review_2026_07.md` passages (item 4 alone). §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 58**, `cowork_factorization_desk_simulation.md` passages (item 4 alone). §7, §8,
--- changed passage 6: insert base lines 69903-69902 -> new lines 69903-69904
  + - Row 57.8 — travelling with Row 4.15: the fallback admitting cadences at a featureless phrase-boundary profile.
  +   *(L2-S49 travels with it.)*
--- changed passage 7: insert base lines 70308-70307 -> new lines 70310-70313
  + - Rows 57.7(ii), 57.10(ii), 57.11(i) and 57.11(ii) — a chromatic repertoire as the measurement bed for the channels
  +   that need no cadence, the validation path for the Jazz preset's values, the regression stop on the robust unit,
  +   and a chromatic stress corpus as research material. *(Row 57.7(ii) travels with Row 4.21, Row 57.10(ii) with Row
  +   23.33, Row 57.11(i) with Row 9.5 and Row 57.11(ii) with Row 5.347.)*
--- changed passage 8: replace base lines 70318-70318 -> new lines 70324-70324
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 9: insert base lines 71577-71576 -> new lines 71583-71584
  + - Row 57.6(iv) — travelling with Row 2.50(i): that L2 carry a rule deciding whether a tonality span is read in one
  +   spelling of a tonality or in its enharmonic twin.
--- changed passage 10: insert base lines 72448-72447 -> new lines 72456-72457
  + - Row 57.6(iii) — as at Row 4.20(ii): the outgoing has *"the recognition consumer as a §5.3 input"*; L2-S49 says *"L2
  +   consumes nothing L3 publishes"* and *"The dependency is one-way: L3 reads L2."*
--- changed passage 11: replace base lines 72515-72515 -> new lines 72525-72526
  - | **Total** | **5418** | **658** | **111** | **1315** | **1538** | **0** | **1375** | **421** | **2323** |
  + | 57 | 21 | 3 | 1 | 5 | 0 | 0 | 10 | 2 | 2 |
  + | **Total** | **5439** | **661** | **112** | **1320** | **1538** | **0** | **1385** | **423** | **2325** |
--- changed passage 12: replace base lines 72517-72517 -> new lines 72528-72528
  - **The arithmetic check:** 658 + 111 + 1315 + 1538 + 0 + 1375 + 421 = 5418, against 5418 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 661 + 112 + 1320 + 1538 + 0 + 1385 + 423 = 5439, against 5439 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 13: replace base lines 72579-72579 -> new lines 72590-72591
  - | **Total** | **993** | **848** | **3633** | **5474** |
  + | 57 | 5 | 1 | 16 | 22 |
  + | **Total** | **998** | **849** | **3649** | **5496** |
--- changed passage 14: replace base lines 72581-72581 -> new lines 72593-72593
  - **The arithmetic check:** 993 + 848 + 3633 = 5474 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
  + **The arithmetic check:** 998 + 849 + 3649 = 5496 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
--- changed passage 15: replace base lines 72612-72612 -> new lines 72624-72624
  -   untouched: positions 1 to 56 are done, positions 57 to 62 are untouched.
  +   untouched: positions 1 to 57 are done, positions 58 to 62 are untouched.
changed passages outside the member: 15
member lines: 247
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
RESERVED tie | .5, the validation path with Row > 23.33 and the membership tie-breaker with Row 6.198(ii) — the claim travels with the ear
RESERVED tie | ed review, a plan.  ---  **Row 57.13 — A-10: the membership tie-breaker recorded as an idiom-calibrated constant; the swap 
RESERVED tie | a rule of the development process, and not counted: (i) the tie-breaker deciding whether a sounding note belongs to the cho
RESERVED note | ot counted: (i) the tie-breaker deciding whether a sounding note belongs to the chord is recorded as an idiom-calibrated con

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4563; travelling refs checked: 2437; as-at refs checked: 843; flags: 0
```

### B.6 — member 58: the seven checks, the final run before its commit

*Saved to the scratch file `checks_58.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_58.md disp totals [5451, 666, 112, 1320, 1538, 0, 1391, 424, 2325] axis totals [1004, 850, 3655, 5509]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 5
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 1; mismatches: 0
draft manifest texts checked: 2; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 3; problems 0

===== count check (foot.py) (exit 0) =====
rows: 5 statements: 12 multi-claim rows by claim count: {2: 1, 5: 1, 3: 1}
| ADOPTED — carried | 5 | 58.2(i), 58.2(ii), 58.2(iii), 58.2(iv), 58.3(ii) |
| ADOPTED — proposed | 0 | — |
| RELOCATED | 0 | — |
| QUARANTINED | 0 | — |
| DISCARDED | 0 | — |
| HISTORICAL | 6 | 58.1(i), 58.1(ii), 58.2(v), 58.3(iii), 58.4, 58.5 |
| UNPLACED | 1 | 58.3(i) |
sum dispositions: 12
verdicts: {'AGREES': 6, 'DIFFERS': 1, 'SILENT': 6} total 13 rows/claims naming two or more: 1
DIFFERS: 58.3(i)
NEAREST L2-S31 58.2
NEAREST L2-S17 58.3
WITHHELD rows: ['58.1']
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3891271 3891271
--- changed passage 1: replace base lines 102-102 -> new lines 102-102
  - | 58 | `cowork_factorization_desk_simulation.md` passages (item 4 alone) | NOT YET TABULATED |
  + | 58 | `cowork_factorization_desk_simulation.md` passages (item 4 alone) | **DONE** (§6.58) |
--- changed passage 2: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 57 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 58 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 3: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 4: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 57 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 58 (D-672).** The first batch, under
--- changed passage 5: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 58**, `cowork_factorization_desk_simulation.md` passages (item 4 alone). §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 59**, `cowork_joint_key_chord_design.md` passages (item 4 alone). §7, §8,
--- changed passage 6: replace base lines 70574-70574 -> new lines 70574-70574
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 7: insert base lines 72708-72707 -> new lines 72708-72710
  + - Row 58.3(i) — as at Row 1.37: the outgoing has *"the signature/declared-mode prior is initial-state-only"*; L2-S17
  +   says the signature enters as *"a weak prior over the spans' tonalities"* and that *"A tonality or mode tag the record
  +   file declares is not read at all."*
--- changed passage 8: replace base lines 72776-72776 -> new lines 72779-72780
  - | **Total** | **5439** | **661** | **112** | **1320** | **1538** | **0** | **1385** | **423** | **2325** |
  + | 58 | 12 | 5 | 0 | 0 | 0 | 0 | 6 | 1 | 0 |
  + | **Total** | **5451** | **666** | **112** | **1320** | **1538** | **0** | **1391** | **424** | **2325** |
--- changed passage 9: replace base lines 72778-72778 -> new lines 72782-72782
  - **The arithmetic check:** 661 + 112 + 1320 + 1538 + 0 + 1385 + 423 = 5439, against 5439 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 666 + 112 + 1320 + 1538 + 0 + 1391 + 424 = 5451, against 5451 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 10: replace base lines 72841-72841 -> new lines 72845-72846
  - | **Total** | **998** | **849** | **3649** | **5496** |
  + | 58 | 6 | 1 | 6 | 13 |
  + | **Total** | **1004** | **850** | **3655** | **5509** |
--- changed passage 11: replace base lines 72843-72843 -> new lines 72848-72848
  - **The arithmetic check:** 998 + 849 + 3649 = 5496 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 20
  + **The arithmetic check:** 1004 + 850 + 3655 = 5509 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 2
--- changed passage 12: replace base lines 72874-72874 -> new lines 72879-72879
  -   untouched: positions 1 to 57 are done, positions 58 to 62 are untouched.
  +   untouched: positions 1 to 58 are done, positions 59 to 62 are untouched.
changed passages outside the member: 12
member lines: 144
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
RESERVED mode | ines 596–597). Three claims: (i) the signature and declared-mode prior conditions the initial key state only; (ii) it is re-
RESERVED key | he signature and declared-mode prior conditions the initial key state only; (ii) it is re-anchored at a notated signature c
RESERVED register | dispositions: one rides an open item, two become open-items register rows, an erratum left to the user.**  *Outgoing statement.*

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====
RESERVED mode | = [] S12_PROP = [] S12_DIFF = [      the signature/declared-mode prior is initial-state-only\ ,      a weak prior over the s
RESERVED mode |      a weak prior over the spans' tonalities\ A tonality or mode tag the record   file declares is not read at all.\ , ] S13

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4568; travelling refs checked: 2445; as-at refs checked: 850; flags: 0
```

### B.7 — member 59: the seven checks, the final run before its commit

*Saved to the scratch file `checks_59.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_59.md disp totals [5457, 667, 112, 1320, 1540, 0, 1391, 427, 2331] axis totals [1005, 854, 3656, 5515]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 11
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 1; mismatches: 0
draft manifest texts checked: 2; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 8; problems 0

===== count check (foot.py) (exit 0) =====
rows: 5 statements: 6 multi-claim rows by claim count: {2: 1}
| ADOPTED — carried | 1 | 59.4(i) |
| ADOPTED — proposed | 0 | — |
| RELOCATED | 0 | — |
| QUARANTINED | 2 | 59.4(ii), 59.5 |
| DISCARDED | 0 | — |
| HISTORICAL | 0 | — |
| UNPLACED | 3 | 59.1, 59.2, 59.3 |
sum dispositions: 6
verdicts: {'AGREES': 1, 'DIFFERS': 4, 'SILENT': 1} total 6 rows/claims naming two or more: 0
DIFFERS: 59.1, 59.2, 59.3, 59.5
WITHHELD rows: ['59.1', '59.2', '59.3', '59.4', '59.5']
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3901202 3901202
--- changed passage 1: replace base lines 103-103 -> new lines 103-103
  - | 59 | `cowork_joint_key_chord_design.md` passages (item 4 alone) | NOT YET TABULATED |
  + | 59 | `cowork_joint_key_chord_design.md` passages (item 4 alone) | **DONE** (§6.59) |
--- changed passage 2: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 58 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 59 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 3: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 4: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 58 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 59 (D-672).** The first batch, under
--- changed passage 5: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 59**, `cowork_joint_key_chord_design.md` passages (item 4 alone). §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 60**, `docs/stage4b_design.md` passages (item 4 alone). §7, §8,
--- changed passage 6: replace base lines 70721-70721 -> new lines 70721-70721
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 7: insert base lines 71838-71837 -> new lines 71838-71840
  + - Row 59.4(ii) — travelling with Row 8.99(ii), and through it with Row 5.226: are the modulation recompute and the
  +   fine-grain override built as instances of one mechanism, and does either run?
  + - Row 59.5 — travelling with Row 8.100(i), and through it with Row 5.226: as at Row 59.4(ii).
--- changed passage 8: insert base lines 72858-72857 -> new lines 72861-72868
  + - Row 59.1 — as at Row 9.323: the outgoing decision is *"(B) — a bounded coupling step"*; L2-S11 decides the
  +   boundaries together with the tonality, the chord and the assignments *"in the one decision"*.
  + - Row 59.2 — as at Row 59.1: the outgoing coupling runs *"over the two existing decoders"*; L2-S11 decides the
  +   tonality and the chord *"in the one decision"*.
  + - Row 59.3 — as at Row 8.98: the outgoing coupling *"fires only on the coupled minority"*; L2-S11 decides every
  +   boundary, tonality and chord *"in the one decision"*.
  + - Row 59.5 — as at Row 8.100(i): the outgoing coupling *"must be designed to respect"* the acyclicity between two
  +   layers; L2-S11 decides the tonality and the chord *"in the one decision"*.
--- changed passage 9: replace base lines 72927-72927 -> new lines 72938-72939
  - | **Total** | **5451** | **666** | **112** | **1320** | **1538** | **0** | **1391** | **424** | **2325** |
  + | 59 | 6 | 1 | 0 | 0 | 2 | 0 | 0 | 3 | 6 |
  + | **Total** | **5457** | **667** | **112** | **1320** | **1540** | **0** | **1391** | **427** | **2331** |
--- changed passage 10: replace base lines 72929-72929 -> new lines 72941-72941
  - **The arithmetic check:** 666 + 112 + 1320 + 1538 + 0 + 1391 + 424 = 5451, against 5451 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 667 + 112 + 1320 + 1540 + 0 + 1391 + 427 = 5457, against 5457 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 11: replace base lines 72993-72993 -> new lines 73005-73006
  - | **Total** | **1004** | **850** | **3655** | **5509** |
  + | 59 | 1 | 4 | 1 | 6 |
  + | **Total** | **1005** | **854** | **3656** | **5515** |
--- changed passage 12: replace base lines 72995-72995 -> new lines 73008-73008
  - **The arithmetic check:** 1004 + 850 + 3655 = 5509 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 2
  + **The arithmetic check:** 1005 + 854 + 3656 = 5515 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 2
--- changed passage 13: replace base lines 73026-73026 -> new lines 73039-73039
  -   untouched: positions 1 to 58 are done, positions 59 to 62 are untouched.
  +   untouched: positions 1 to 59 are done, positions 60 to 62 are untouched.
changed passages outside the member: 13
member lines: 159
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
RESERVED register | t was read:* as at Row 9.323, and further, at the decisions register's index, D-376 — the decision homed here — recorded SHELVED

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4573; travelling refs checked: 2451; as-at refs checked: 855; flags: 0
```

### B.8 — member 60: the seven checks, the final run before its commit

*Saved to the scratch file `checks_60.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_60.md disp totals [5465, 667, 112, 1320, 1540, 0, 1394, 432, 2331] axis totals [1006, 858, 3659, 5523]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 7
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 1; mismatches: 0
draft manifest texts checked: 2; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 4; problems 0

===== count check (foot.py) (exit 0) =====
rows: 7 statements: 8 multi-claim rows by claim count: {2: 1}
| ADOPTED — carried | 0 | — |
| ADOPTED — proposed | 0 | — |
| RELOCATED | 0 | — |
| QUARANTINED | 0 | — |
| DISCARDED | 0 | — |
| HISTORICAL | 3 | 60.1, 60.5, 60.6 |
| UNPLACED | 5 | 60.2(i), 60.2(ii), 60.3, 60.4, 60.7 |
sum dispositions: 8
verdicts: {'AGREES': 1, 'DIFFERS': 4, 'SILENT': 3} total 8 rows/claims naming two or more: 0
DIFFERS: 60.2(i), 60.2(ii), 60.3, 60.4
NEAREST L2-S17 60.2, 60.3, 60.4, 60.7
WITHHELD rows: ['60.2', '60.3', '60.4', '60.5', '60.6']
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3912715 3912715
--- changed passage 1: replace base lines 104-104 -> new lines 104-104
  - | 60 | `docs/stage4b_design.md` passages (item 4 alone) | NOT YET TABULATED |
  + | 60 | `docs/stage4b_design.md` passages (item 4 alone) | **DONE** (§6.60) |
--- changed passage 2: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 59 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 60 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 3: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 4: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 59 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 60 (D-672).** The first batch, under
--- changed passage 5: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 60**, `docs/stage4b_design.md` passages (item 4 alone). §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 61**, `records/cowork/handoff/cowork_handoff_archive.md` passages (item 4 alone). §7, §8,
--- changed passage 6: replace base lines 70883-70883 -> new lines 70883-70883
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 7: insert base lines 73031-73030 -> new lines 73031-73035
  + - Row 60.2(i) and (ii) — as at Row 24.4: the outgoing keeps a declared value *"as the only declared influence on the
  +   252-candidate score"*; L2-S17 says *"A tonality or mode tag the record file declares is not read at all."*
  + - Row 60.3 — as at Row 24.4: the outgoing hint *"can only flip the winner when the raw note-based gap is already
  +   within ~1.0"*; L2-S17, as above.
  + - Row 60.4 — as at Row 24.4: the outgoing gate is the hint's own size, *"smallness *is* the gate"*; L2-S17, as above.
--- changed passage 8: replace base lines 73101-73101 -> new lines 73106-73107
  - | **Total** | **5457** | **667** | **112** | **1320** | **1540** | **0** | **1391** | **427** | **2331** |
  + | 60 | 8 | 0 | 0 | 0 | 0 | 0 | 3 | 5 | 0 |
  + | **Total** | **5465** | **667** | **112** | **1320** | **1540** | **0** | **1394** | **432** | **2331** |
--- changed passage 9: replace base lines 73103-73103 -> new lines 73109-73109
  - **The arithmetic check:** 667 + 112 + 1320 + 1540 + 0 + 1391 + 427 = 5457, against 5457 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 667 + 112 + 1320 + 1540 + 0 + 1394 + 432 = 5465, against 5465 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 10: replace base lines 73168-73168 -> new lines 73174-73175
  - | **Total** | **1005** | **854** | **3656** | **5515** |
  + | 60 | 1 | 4 | 3 | 8 |
  + | **Total** | **1006** | **858** | **3659** | **5523** |
--- changed passage 11: replace base lines 73170-73170 -> new lines 73177-73177
  - **The arithmetic check:** 1005 + 854 + 3656 = 5515 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 2
  + **The arithmetic check:** 1006 + 858 + 3659 = 5523 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 2
--- changed passage 12: replace base lines 73201-73201 -> new lines 73208-73208
  -   untouched: positions 1 to 59 are done, positions 60 to 62 are untouched.
  +   untouched: positions 1 to 60 are done, positions 61 to 62 are untouched.
changed passages outside the member: 12
member lines: 178
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
RESERVED key | adings apply.** Passages of a dated design for the legacy > key analyzer: the code as it stood, and the change demoting the
RESERVED mode |  the code as it stood, and the change demoting the declared mode's penalty to a small additive hint. > **The placement readi
RESERVED score | itted, kept as the only declared influence on the candidate score.** *WITHHELD — D-571, claim (ii).*  *Outgoing statement.*  
RESERVED score |  it is kept as the only declared influence on the candidate score. *Boundary mark:* the sentence opens on line 68, before D-5
RESERVED register | at was read:* as at Row 24.4, and further, at the decisions register's index, D-571 — the decision homed here — recorded SUPERSE
RESERVED tie |  was read:* as at (i).  ---  **Row 60.3 — the small value a tie-break: it flips the winner only within a gap of about one, 
RESERVED notes | n a gap of about one, never against clear evidence from the notes.** *WITHHELD — D-571.*  *Outgoing statement.*  when genuine
RESERVED register | at was read:* as at Row 24.4, and further, at the decisions register's index, D-571 — the decision homed here — recorded SUPERSE
RESERVED register | at was read:* as at Row 24.4, and further, at the decisions register's index, D-571 — the decision homed here — recorded SUPERSE
RESERVED mode | onal plan for the code.  ---  **Row 60.7 — with no declared mode the hint is not applied, and the candidate score comes from
RESERVED score | no declared mode the hint is not applied, and the candidate score comes from the notes alone.**  *Outgoing statement.*   — §2
RESERVED notes | hint is not applied, and the candidate score comes from the notes alone.**  *Outgoing statement.*   — §2.1, *The −7 penalty →
RESERVED mode | 17: **AGREES** — on the case it names, where no tonality or mode is declared and nothing but the notes is read; L2-S17 says 
RESERVED notes | , where no tonality or mode is declared and nothing but the notes is read; L2-S17 says    *PROPOSED DISPOSITION.* **UNPLACED*
RESERVED mode | s at Row 24.4; the AGREES is on the case without a declared mode alone, and does not decide the hint whose property the sent

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====
RESERVED score |       as the only declared influence on the   252-candidate score\ A tonality or mode tag the record file declares is not rea
RESERVED mode | lared influence on the   252-candidate score\ A tonality or mode tag the record file declares is not read at all.\ ,      ca
RESERVED note |  read at all.\ ,      can only flip the winner when the raw note-based gap is already   within ~1.0\ ,      smallness *is* t

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4580; travelling refs checked: 2456; as-at refs checked: 859; flags: 0
```

### B.9 — member 61: the seven checks, the final run before its commit

*Saved to the scratch file `checks_61.txt`.*


```text
===== build (build_member.py) (exit 0) =====
built C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/054efb45-1683-45ab-9d54-3a2629537b4b/scratchpad/reading_61.md disp totals [5473, 667, 112, 1320, 1542, 0, 1400, 432, 2331] axis totals [1006, 858, 3667, 5531]

===== quotation + coverage + short-quotation + manifest checks (qcheck.py) (exit 0) =====
quotations checked: 6
problems: 0
coverage residue pieces: 0
short quotations not found in either text: 0
manifest ranges checked: 1; mismatches: 0
draft manifest texts checked: 2; mismatches: 0
doc has CR: False

===== short-quotation check over the §10-§12 entries added (speccheck.py) (exit 0) =====
§10-§12 added entries: short quotations checked 0; problems 0

===== count check (foot.py) (exit 0) =====
rows: 6 statements: 8 multi-claim rows by claim count: {2: 2}
| ADOPTED — carried | 0 | — |
| ADOPTED — proposed | 0 | — |
| RELOCATED | 0 | — |
| QUARANTINED | 2 | 61.2(i), 61.2(ii) |
| DISCARDED | 0 | — |
| HISTORICAL | 6 | 61.1, 61.3(i), 61.3(ii), 61.4, 61.5, 61.6 |
| UNPLACED | 0 | — |
sum dispositions: 8
verdicts: {'AGREES': 0, 'DIFFERS': 0, 'SILENT': 8} total 8 rows/claims naming two or more: 0
DIFFERS: none
WITHHELD rows: ['61.2', '61.3']
problems: 0

===== build check (build_check.py) (exit 0) =====
done span identical: True 3924132 3924132
--- changed passage 1: replace base lines 105-105 -> new lines 105-105
  - | 61 | `records/cowork/handoff/cowork_handoff_archive.md` passages (item 4 alone) | NOT YET TABULATED |
  + | 61 | `records/cowork/handoff/cowork_handoff_archive.md` passages (item 4 alone) | **DONE** (§6.61) |
--- changed passage 2: replace base lines 110-110 -> new lines 110-110
  - each. **Done: positions 1 to 60 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
  + each. **Done: positions 1 to 61 — the four `ARCHITECTURE.md` sections of the ruling's item 1, whole,
--- changed passage 3: replace base lines 116-116 -> new lines 116-116
  - `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
  + `cowork_engage_arc_plan.md`, whole, `cowork_l1l4_review_charter.md`, whole, the `ARCHITECTURE.md` passages of the opening block, above the first `## ` heading, the `ARCHITECTURE.md` passages under *Document governance an
--- changed passage 4: replace base lines 118-118 -> new lines 118-118
  - **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 60 (D-672).** The first batch, under
  + **★ THE WRITING STANDS AT THE MEMBER BOUNDARY AFTER POSITION 61 (D-672).** The first batch, under
--- changed passage 5: replace base lines 146-147 -> new lines 146-147
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  - quoted, not counted and not placed, and nothing in them is partly worked. **The next writing resumes at position 61**, `records/cowork/handoff/cowork_handoff_archive.md` passages (item 4 alone). §7, §8,
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 a
  + quoted, not counted and not placed, and nothing in it is partly worked. **The next writing resumes at position 62**, the L0/L1 transfer input — `ratification_surfaces/cowork_comparison_l0_l1_reading.md` §10. §7, §8,
--- changed passage 6: replace base lines 71064-71064 -> new lines 71064-71064
  - above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
  + above. Member 34 relocates no row. Member 35 relocates no row. Member 36 relocates one, Row 36.1, above. Member 37 relocates no row. Member 38 relocates no row. Member 39's relocations are the rows numbered 39.n above, m
--- changed passage 7: insert base lines 72184-72183 -> new lines 72184-72187
  + - Row 61.2(i) — does the recorded share of the legacy tonality path's disagreement set that the path itself recovers
  +   reproduce, and on which retired path and corpus was it taken?
  + - Row 61.2(ii) — as at Row 61.2(i), for the share recorded as emission error, and for the recorded share in which the
  +   correct tonality is never ranked second.
--- changed passage 8: replace base lines 73288-73288 -> new lines 73292-73293
  - | **Total** | **5465** | **667** | **112** | **1320** | **1540** | **0** | **1394** | **432** | **2331** |
  + | 61 | 8 | 0 | 0 | 0 | 2 | 0 | 6 | 0 | 0 |
  + | **Total** | **5473** | **667** | **112** | **1320** | **1542** | **0** | **1400** | **432** | **2331** |
--- changed passage 9: replace base lines 73290-73290 -> new lines 73295-73295
  - **The arithmetic check:** 667 + 112 + 1320 + 1540 + 0 + 1394 + 432 = 5465, against 5465 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
  + **The arithmetic check:** 667 + 112 + 1320 + 1542 + 0 + 1400 + 432 = 5473, against 5473 statements placed (72 + 65 + 40 + 36 + 417 + 272 + 224 + 212 + 471 + 96 + 104 + 71 + 50 + 47 + 45 + 10 + 124 + 4 + 0 + 6 + 111 + 156
--- changed passage 10: replace base lines 73356-73356 -> new lines 73361-73362
  - | **Total** | **1006** | **858** | **3659** | **5523** |
  + | 61 | 0 | 0 | 8 | 8 |
  + | **Total** | **1006** | **858** | **3667** | **5531** |
--- changed passage 11: replace base lines 73358-73358 -> new lines 73364-73364
  - **The arithmetic check:** 1006 + 858 + 3659 = 5523 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 2
  + **The arithmetic check:** 1006 + 858 + 3667 = 5531 (78 + 65 + 40 + 38 + 430 + 273 + 225 + 219 + 472 + 105 + 104 + 71 + 50 + 47 + 45 + 10 + 129 + 4 + 0 + 6 + 112 + 156 + 373 + 132 + 53 + 24 + 18 + 2 + 31 + 87 + 0 + 12 + 2
--- changed passage 12: replace base lines 73389-73389 -> new lines 73395-73395
  -   untouched: positions 1 to 60 are done, positions 61 to 62 are untouched.
  +   untouched: positions 1 to 61 are done, position 62 is untouched.
changed passages outside the member: 12
member lines: 159
ends with newline: True no CR: True

===== word scan (wordscan.py, member subsection, quotations removed) (exit 0) =====
RESERVED register | y mark. Row 61.3's boundary mark records that the decisions register's own > statement of D-289 is the content of that row's cla
RESERVED register | claim (ii) lies past it and does not — though the decisions register's own statement of D-289 is claim (ii)'s content. The mark 
RESERVED register | eta-principle of a dated handoff entry, which the decisions register records as superseded (D-289, by D-284 and through it D-036

===== word scan (wordscan.py, the spec's §0/§10-§12 text, quotations removed) (exit 0) =====

===== consistency check (consistency.py, whole built file) (exit 0) =====
rows parsed: 4586; travelling refs checked: 2456; as-at refs checked: 859; flags: 0
```

### B.10a — the consistency script's FIRST run over the committed reading file (at the Task 0 commit)

*Saved to the scratch file `cons_first.txt`.*


```text
rows parsed: 4434; travelling refs checked: 2316; as-at refs checked: 805; flags: 0
```

### B.10b — the consistency script on two planted faults

*Saved to the scratch files `plant_out.txt`, `cons_planted.txt`.*

`plant_out.txt`:
```text
planted 2
```

`cons_planted.txt`:
```text
rows parsed: 4434; travelling refs checked: 2316; as-at refs checked: 805; flags: 2
FLAG Row 48.1(i) [ADOPTED — carried]: travelling with Row 48.2(ii) whose disposition(s) are ['HISTORICAL']
FLAG Row 48.11: L2-S34 DIFFERS as at Row 10.14(v), which carries [('L2-S34', 'AGREES')]
```

### B.10c — the coverage check's deletion proof on member 53's draft

*Saved to the scratch file `q53_delproof.txt`.*


```text
quotations checked: 118
problems: 0
coverage residue pieces: 3
RESIDUE 21 'Named progression — a chord progression with a conventional name and a catalog entry in the Harmonic'
RESIDUE 22 'Vocabulary (cowork_progression_schema_dictionary.md §5): cadence formulas, ii–V–I, turnarounds, the galant'
RESIDUE 23 'schemata, bass-line patterns, substitution operations.'
short quotations not found in either text: 0
manifest ranges checked: 9; mismatches: 0
draft manifest texts checked: 0; mismatches: 0
doc has CR: False
```

### B.11 — the backbone homes located for each member's document (the SEEN check at the homes, and the decisions homed in each document)

*Saved to the scratch files `homes53.txt`, `homes54.txt`, `homes55.txt`, `homes56.txt`, `homes57.txt`, `homes58.txt`, `homes59.txt`, `homes60.txt`, `homes61.txt`.*

`homes53.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
HOMED-IN-DOC D-502 cowork_progression_schema_design.md:245-247
HOMED-IN-DOC D-503 cowork_progression_schema_design.md:135-136
HOMED-IN-DOC D-504 cowork_progression_schema_design.md:161-178
HOMED-IN-DOC D-505 cowork_progression_schema_design.md:162-166
HOMED-IN-DOC D-506 cowork_progression_schema_design.md:193-194
HOMED-IN-DOC D-507 cowork_progression_schema_design.md:272-273
HOMED-IN-DOC D-508 cowork_progression_schema_design.md:242-244
HOMED-IN-DOC D-509 cowork_progression_schema_design.md:121-128
```

`homes54.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
HOMED-IN-DOC D-442 docs/llm_integration.md:304-305
HOMED-IN-DOC D-443 docs/llm_integration.md:601-604
HOMED-IN-DOC D-444 docs/llm_integration.md:367-369
HOMED-IN-DOC D-445 docs/llm_integration.md:418-421
HOMED-IN-DOC D-446 docs/llm_integration.md:518-521
HOMED-IN-DOC D-447 docs/llm_integration.md:613-615
HOMED-IN-DOC D-448 docs/llm_integration.md:286-288
```

`homes55.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
```

`homes56.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
HOMED-IN-DOC D-282 cowork_architecture_reassessment.md:106
HOMED-IN-DOC D-283 cowork_architecture_reassessment.md:107
HOMED-IN-DOC D-284 cowork_architecture_reassessment.md:108-109
HOMED-IN-DOC D-285 cowork_architecture_reassessment.md:110
```

`homes57.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
HOMED-IN-DOC D-498 cowork_architecture_review_2026_07.md:333-335
HOMED-IN-DOC D-499 cowork_architecture_review_2026_07.md:336-338
```

`homes58.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
HOMED-IN-DOC D-453 cowork_factorization_desk_simulation.md:590-591
```

`homes59.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
HOMED-IN-DOC D-376 cowork_joint_key_chord_design.md:87-106
HOMED-IN-DOC D-377 cowork_joint_key_chord_design.md:146-150
HOMED-IN-DOC D-378 cowork_joint_key_chord_design.md:183-190
HOMED-IN-DOC D-379 cowork_joint_key_chord_design.md:276-282
```

`homes60.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
HOMED-IN-DOC D-571 docs/stage4b_design.md:69-73
HOMED-IN-DOC D-573 docs/stage4b_design.md:217-218
HOMED-IN-DOC D-574 docs/stage4b_design.md:167
```

`homes61.txt`:
```text
entries with a home: 680
SEEN-HOME D-002 ARCHITECTURE.md:21-22
SEEN-HOME D-095 ARCHITECTURE.md:43-44
SEEN-HOME D-223 docs/scoring_model.md:1184-1186
SEEN-HOME D-261 cowork_bounded_context_design.md:57-71
SEEN-HOME D-275 cowork_notation_output_contract.md:54-57
SEEN-HOME D-279 cowork_engage_arc_plan.md:69-72
SEEN-HOME D-322 docs/scoring_model.md:286-291
SEEN-HOME D-393 cowork_voiceleading_axis_design.md:372-377
HOMED-IN-DOC D-289 records/cowork/handoff/cowork_handoff_archive.md:3082
```

## Appendix C — the close and Task 0

### C.1 — A1's enumeration, `python tools/audit/changed_paths.py` (0(c))

*Saved to the scratch file `t0c_changed.txt`.*


```text
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventy_five.md
??	scratch_artifacts/baseline_composing.txt
??	scratch_artifacts/baseline_notation.txt
??	scratch_artifacts/baseline_snapshot.txt
??	scratch_artifacts/baseline_table.md
??	scratch_artifacts/batch_analyze.both.bak
??	scratch_artifacts/batchreg.log
??	scratch_artifacts/bir_after_baroque.txt
??	scratch_artifacts/bir_after_default.txt
??	scratch_artifacts/bir_after_jazz.txt
??	scratch_artifacts/bir_baroque.log
??	scratch_artifacts/bir_baroque.txt
??	scratch_artifacts/bir_default.log
??	scratch_artifacts/bir_default.txt
??	scratch_artifacts/bir_jazz.log
??	scratch_artifacts/bir_jazz.txt
??	scratch_artifacts/build_backfill.txt
??	scratch_artifacts/build_backfill2.txt
??	scratch_artifacts/build_backfill2_err.txt
??	scratch_artifacts/build_backfill_err.txt
??	scratch_artifacts/build_dbg.log
??	scratch_artifacts/build_final.log
??	scratch_artifacts/build_g1.log
??	scratch_artifacts/build_g2.log
??	scratch_artifacts/build_g2b.log
??	scratch_artifacts/build_iso.log
??	scratch_artifacts/build_out.txt
??	scratch_artifacts/build_revert.log
??	scratch_artifacts/build_revert_err.log
??	scratch_artifacts/build_step1.log
??	scratch_artifacts/build_step1b.log
??	scratch_artifacts/build_step1c.log
??	scratch_artifacts/build_step2.log
??	scratch_artifacts/build_stepM.log
??	scratch_artifacts/build_stepM2.log
??	scratch_artifacts/build_stepM_err.log
??	scratch_artifacts/build_task1.log
??	scratch_artifacts/build_task2.log
??	scratch_artifacts/c5_guardhelp.txt
??	scratch_artifacts/c5_p1w.txt
??	scratch_artifacts/c5_triage.txt
??	scratch_artifacts/c5_triage2.txt
??	scratch_artifacts/c8_bar.txt
??	scratch_artifacts/c8_bar2.txt
??	scratch_artifacts/c8_build.log
??	scratch_artifacts/c8_class.txt
??	scratch_artifacts/c8_classchk.txt
??	scratch_artifacts/c8_ct.txt
??	scratch_artifacts/c8_disp.txt
??	scratch_artifacts/c8_dispv.txt
??	scratch_artifacts/c8_gc_t0.txt
??	scratch_artifacts/c8_gc_t1.txt
??	scratch_artifacts/c8_gc_t2.txt
??	scratch_artifacts/c8_gc_t4.txt
??	scratch_artifacts/c8_gc_t4b.txt
??	scratch_artifacts/c8_gp.txt
??	scratch_artifacts/c8_guard_final.txt
??	scratch_artifacts/c8_guard_final2.txt
??	scratch_artifacts/c8_guard_start.txt
??	scratch_artifacts/c8_guard_t0.txt
??	scratch_artifacts/c8_guard_t0b.txt
??	scratch_artifacts/c8_guard_t0c.txt
??	scratch_artifacts/c8_guard_t1.txt
??	scratch_artifacts/c8_guard_t1b.txt
??	scratch_artifacts/c8_guard_t1c.txt
??	scratch_artifacts/c8_guard_t2.txt
??	scratch_artifacts/c8_guard_t2b.txt
??	scratch_artifacts/c8_guard_t4.txt
??	scratch_artifacts/c8_guard_t4b.txt
??	scratch_artifacts/c8_guard_t4c.txt
??	scratch_artifacts/c8_guardclass_start.txt
??	scratch_artifacts/c8_inv.txt
??	scratch_artifacts/c8_lint.txt
??	scratch_artifacts/c8_nt.txt
??	scratch_artifacts/c8_oi357_a.txt
??	scratch_artifacts/c8_oi357_b.txt
??	scratch_artifacts/c8_oi357_c.txt
??	scratch_artifacts/c8_ps.txt
??	scratch_artifacts/c8_r1.txt
??	scratch_artifacts/c8_r12.txt
??	scratch_artifacts/c8_reaim.txt
??	scratch_artifacts/c8_reaimhelp.txt
??	scratch_artifacts/c8_reg.txt
??	scratch_artifacts/c8_regchk.txt
??	scratch_artifacts/c8_routes.txt
??	scratch_artifacts/c8_split.txt
??	scratch_artifacts/c8_sweep.txt
??	scratch_artifacts/c8_sweep2.txt
??	scratch_artifacts/c8_sweep3.txt
??	scratch_artifacts/c8_sweep4.txt
??	scratch_artifacts/c8_sweep5.txt
??	scratch_artifacts/c8_sweep6.txt
??	scratch_artifacts/c8_sweep_list.txt
??	scratch_artifacts/c8_t1_bar.txt
??	scratch_artifacts/c8_t1_bar2.txt
??	scratch_artifacts/c8_t1_blk.txt
??	scratch_artifacts/c8_t1_class.txt
??	scratch_artifacts/c8_t1_class2.txt
??	scratch_artifacts/c8_t1_class3.txt
??	scratch_artifacts/c8_t1_disp.txt
??	scratch_artifacts/c8_t1_disp2.txt
??	scratch_artifacts/c8_t1_fl.txt
??	scratch_artifacts/c8_t1_inv.txt
??	scratch_artifacts/c8_t1_outd.txt
??	scratch_artifacts/c8_t1_reaim.txt
??	scratch_artifacts/c8_t1_reg.txt
??	scratch_artifacts/c8_t1_reg2.txt
??	scratch_artifacts/c8_t1_routes.txt
??	scratch_artifacts/c8_t1_routes2.txt
??	scratch_artifacts/c8_t1_routes3.txt
??	scratch_artifacts/c8_t1_routes4.txt
??	scratch_artifacts/c8_t2_blk.txt
??	scratch_artifacts/c8_t2_class.txt
??	scratch_artifacts/c8_t2_class2.txt
??	scratch_artifacts/c8_t2_class3.txt
??	scratch_artifacts/c8_t2_class4.txt
??	scratch_artifacts/c8_t2_class5.txt
??	scratch_artifacts/c8_t2_disp.txt
??	scratch_artifacts/c8_t2_fl.txt
??	scratch_artifacts/c8_t2_inv.txt
??	scratch_artifacts/c8_t2_outd.txt
??	scratch_artifacts/c8_t2_r1.txt
??	scratch_artifacts/c8_t2_reaim.txt
??	scratch_artifacts/c8_t2_reg.txt
??	scratch_artifacts/c8_t2_routes.txt
??	scratch_artifacts/c8_t4_blk.txt
??	scratch_artifacts/c8_t4_cp.txt
??	scratch_artifacts/c8_t4_cp2.txt
??	scratch_artifacts/c8_t4_cp3.txt
??	scratch_artifacts/c8_t4_cphelp.txt
??	scratch_artifacts/c8_t4_fl.txt
??	scratch_artifacts/c8_t4_fl2.txt
??	scratch_artifacts/c8_t4_inv.txt
??	scratch_artifacts/c8_t4_inv2.txt
??	scratch_artifacts/c8_t4_ng.txt
??	scratch_artifacts/c8_t4_ng2.txt
??	scratch_artifacts/c8_t4_p1w.txt
??	scratch_artifacts/c8_t4_p1w2.txt
??	scratch_artifacts/c8_t4_p1w3.txt
??	scratch_artifacts/c8_t4_r1.txt
??	scratch_artifacts/c8_t4_routes.txt
??	scratch_artifacts/c8_triage.txt
??	scratch_artifacts/c8_triage2.txt
??	scratch_artifacts/c9_changed.txt
??	scratch_artifacts/c9_class.txt
??	scratch_artifacts/c9_classchk.txt
??	scratch_artifacts/c9_guard_start.txt
??	scratch_artifacts/c9_guards1.txt
??	scratch_artifacts/c9_guards2.txt
??	scratch_artifacts/c9_p1w.txt
??	scratch_artifacts/c9_r1.txt
??	scratch_artifacts/c9_reaim.txt
??	scratch_artifacts/c9_regen1.txt
??	scratch_artifacts/c9_regen2.txt
??	scratch_artifacts/c9_regen3.txt
??	scratch_artifacts/c9_routes.txt
??	scratch_artifacts/c9_shellguard_1.txt
??	scratch_artifacts/c9_shellguard_rep.txt
??	scratch_artifacts/c9_split.txt
??	scratch_artifacts/c9_verify1.txt
??	scratch_artifacts/c9_verify2.txt
??	scratch_artifacts/cadence_tests.txt
??	scratch_artifacts/cc_collect.txt
??	scratch_artifacts/ccc_collect2.txt
??	scratch_artifacts/ccc_log.txt
??	scratch_artifacts/ccc_notation.txt
??	scratch_artifacts/ccc_path.txt
??	scratch_artifacts/char_baroque.txt
??	scratch_artifacts/char_baroque_l5m.txt
??	scratch_artifacts/char_default.txt
??	scratch_artifacts/char_default_l5m.txt
??	scratch_artifacts/char_jazz.txt
??	scratch_artifacts/char_jazz_l5m.txt
??	scratch_artifacts/claude_baroque.txt
??	scratch_artifacts/claude_baroque_sorted.txt
??	scratch_artifacts/claude_default.txt
??	scratch_artifacts/claude_default_sorted.txt
??	scratch_artifacts/claude_jazz.txt
??	scratch_artifacts/claude_jazz_sorted.txt
??	scratch_artifacts/clone_algomusdata.txt
??	scratch_artifacts/clone_asap.txt
??	scratch_artifacts/clone_batch1.log
??	scratch_artifacts/clone_batch2.log
??	scratch_artifacts/clone_batch3.log
??	scratch_artifacts/clone_batik.log
??	scratch_artifacts/clone_bcfb.txt
??	scratch_artifacts/clone_cocopops.txt
??	scratch_artifacts/clone_figbass.txt
??	scratch_artifacts/clone_lieder.txt
??	scratch_artifacts/clone_mcma.log
??	scratch_artifacts/clone_mikrokosmos.log
??	scratch_artifacts/clone_openewld.txt
??	scratch_artifacts/clone_piano_svsep.log
??	scratch_artifacts/clone_protovoice.txt
??	scratch_artifacts/clone_schenker41.txt
??	scratch_artifacts/clone_sq.txt
??	scratch_artifacts/clone_vocsep.log
??	scratch_artifacts/cmp_manifest_sha.py
??	scratch_artifacts/commit1_msg.txt
??	scratch_artifacts/commit1_out.txt
??	scratch_artifacts/commit2_msg.txt
??	scratch_artifacts/commit2_out.txt
??	scratch_artifacts/commit_msg_step2.txt
??	scratch_artifacts/comp_run.txt
??	scratch_artifacts/comp_run2.txt
??	scratch_artifacts/comp_run3.txt
??	scratch_artifacts/comp_run4.txt
??	scratch_artifacts/comp_step1.txt
??	scratch_artifacts/comp_step1c.txt
??	scratch_artifacts/composing.cobertura.xml
??	scratch_artifacts/composing_final_out.txt
??	scratch_artifacts/composing_full.txt
??	scratch_artifacts/composing_new_out.txt
??	scratch_artifacts/composing_test.log
??	scratch_artifacts/composing_test2.log
??	scratch_artifacts/composing_tests_out.txt
??	scratch_artifacts/corpus_decode_chord_g1/
??	scratch_artifacts/corpus_decode_chord_g2/
??	scratch_artifacts/corpus_decode_chord_g2iso/
??	scratch_artifacts/corpus_decode_chord_g6/
??	scratch_artifacts/corpus_decode_chord_step2final_A/
??	scratch_artifacts/corpus_decode_chord_step2final_B/
??	scratch_artifacts/corpus_decode_chord_stepM/
??	scratch_artifacts/corpus_ours_check/
??	scratch_artifacts/corpus_ours_check_g2/
??	scratch_artifacts/cov_after.log
??	scratch_artifacts/cov_after2.log
??	scratch_artifacts/cov_final.log
??	scratch_artifacts/cov_final2.log
??	scratch_artifacts/coverage/
??	scratch_artifacts/coverage_merged.txt
??	scratch_artifacts/coverage_report.txt
??	scratch_artifacts/curation_worksheet.txt
??	scratch_artifacts/decode_baroque_step0.log
??	scratch_artifacts/decode_default_step0.log
??	scratch_artifacts/decode_g1_baroque.log
??	scratch_artifacts/decode_g1_baroque2.log
??	scratch_artifacts/decode_g1_default2.log
??	scratch_artifacts/decode_g1_driver.py
??	scratch_artifacts/decode_g2_baroque.log
??	scratch_artifacts/decode_g2_default.log
??	scratch_artifacts/decode_g2iso.log
??	scratch_artifacts/decode_step0_run.log
??	scratch_artifacts/decode_stepM_baroque.log
??	scratch_artifacts/decode_stepM_default.log
??	scratch_artifacts/decompose_g1_after.log
??	scratch_artifacts/decompose_g1_before.log
??	scratch_artifacts/decompose_g2_after.log
??	scratch_artifacts/decompose_g2_before.log
??	scratch_artifacts/decompose_g2iso.log
??	scratch_artifacts/decompose_step0.log
??	scratch_artifacts/dlc_baseline_run.log
??	scratch_artifacts/dlc_pins.json
??	scratch_artifacts/driver_smoke.err
??	scratch_artifacts/e0dp_cap_decomp.py
??	scratch_artifacts/e0prime_grader.log
??	scratch_artifacts/e0prime_supp.log
??	scratch_artifacts/e0prime_supp.py
??	scratch_artifacts/filter_hunks.py
??	scratch_artifacts/fs_regen_baroque.log
??	scratch_artifacts/fs_regen_default.log
??	scratch_artifacts/fs_regen_driver.log
??	scratch_artifacts/fs_regen_jazz.log
??	scratch_artifacts/g1_composing.log
??	scratch_artifacts/g1_decode_tests.log
??	scratch_artifacts/g1_notation.log
??	scratch_artifacts/g1_one_decode.err
??	scratch_artifacts/g1_one_decode.json
??	scratch_artifacts/g1_snapshots.log
??	scratch_artifacts/g2_composing.log
??	scratch_artifacts/g2_decode_tests.log
??	scratch_artifacts/g2_notation.log
??	scratch_artifacts/g2_snap.log
??	scratch_artifacts/gate_after_baroque.txt
??	scratch_artifacts/gate_after_default.txt
??	scratch_artifacts/gate_after_jazz.txt
??	scratch_artifacts/gate_baroque.txt
??	scratch_artifacts/gate_before_baroque.txt
??	scratch_artifacts/gate_before_default.txt
??	scratch_artifacts/gate_before_jazz.txt
??	scratch_artifacts/gate_check.py
??	scratch_artifacts/gate_setdiff.py
??	scratch_artifacts/grade_g1_after.log
??	scratch_artifacts/grade_g1_before.log
??	scratch_artifacts/grade_g2_after.log
??	scratch_artifacts/grade_g2_before.log
??	scratch_artifacts/grade_g2iso.log
??	scratch_artifacts/grade_step0.log
??	scratch_artifacts/guitarset_curl_err.txt
??	scratch_artifacts/guitarset_dl_err.txt
??	scratch_artifacts/guitarset_zenodo.json
??	scratch_artifacts/harvest_final.txt
??	scratch_artifacts/harvest_final2.txt
??	scratch_artifacts/harvest_final3.txt
??	scratch_artifacts/harvest_run1.txt
??	scratch_artifacts/harvest_run2.txt
??	scratch_artifacts/harvest_run3.txt
??	scratch_artifacts/hd_LIST.txt
??	scratch_artifacts/hd_branch.txt
??	scratch_artifacts/hd_dl.txt
??	scratch_artifacts/hd_err.txt
??	scratch_artifacts/hd_lists.json
??	scratch_artifacts/hd_repo.json
??	scratch_artifacts/hd_repos.txt
??	scratch_artifacts/hd_repos_final.txt
??	scratch_artifacts/hd_root.json
??	scratch_artifacts/hd_tree.json
??	scratch_artifacts/humdrum_data_closure_71repos.txt
??	scratch_artifacts/humdrum_gitmodules.txt
??	scratch_artifacts/humdrum_gitmodules2.txt
??	scratch_artifacts/keyparse_probe.log
??	scratch_artifacts/l4.err
??	scratch_artifacts/l4.patch
??	scratch_artifacts/l5.err
??	scratch_artifacts/l5.patch
??	scratch_artifacts/l5_smoke.err
??	scratch_artifacts/l5_smoke.json
??	scratch_artifacts/line_hits.py
??	scratch_artifacts/ninja_direct.txt
??	scratch_artifacts/notation.cobertura.xml
??	scratch_artifacts/notation_after.txt
??	scratch_artifacts/notation_final.txt
??	scratch_artifacts/notation_full.txt
??	scratch_artifacts/notation_run.txt
??	scratch_artifacts/notation_step1.txt
??	scratch_artifacts/notation_test.log
??	scratch_artifacts/notation_test2.log
??	scratch_artifacts/notation_tests_out.txt
??	scratch_artifacts/oi357_production_arm/
??	scratch_artifacts/oi357_production_arm_legacy_control/
??	scratch_artifacts/ours_A/
??	scratch_artifacts/ours_B/
??	scratch_artifacts/ours_check_baroque.log
??	scratch_artifacts/parse_cov.py
??	scratch_artifacts/parse_merge.py
??	scratch_artifacts/pdmx_inspect.py
??	scratch_artifacts/pipeline_snapshot_tests_out.txt
??	scratch_artifacts/quote_verify.txt
??	scratch_artifacts/quote_verify2.txt
??	scratch_artifacts/reg_A.json
??	scratch_artifacts/reg_B.json
??	scratch_artifacts/reg_pre_acq.json
??	scratch_artifacts/reg_run1.json
??	scratch_artifacts/reg_run1.txt
??	scratch_artifacts/reg_run2.txt
??	scratch_artifacts/regen_baroque.log
??	scratch_artifacts/regen_baroque_l5.log
??	scratch_artifacts/regen_default.log
??	scratch_artifacts/regen_default_l5.log
??	scratch_artifacts/regen_driver.log
??	scratch_artifacts/regen_g2_baroque.log
??	scratch_artifacts/regen_jazz.log
??	scratch_artifacts/regen_jazz_l5.log
??	scratch_artifacts/rel_tests.txt
??	scratch_artifacts/repro30.txt
??	scratch_artifacts/repro_block.txt
??	scratch_artifacts/repro_check/
??	scratch_artifacts/s5_2b_task1_tables.txt
??	scratch_artifacts/set_baroque.txt
??	scratch_artifacts/set_default.txt
??	scratch_artifacts/set_jazz.txt
??	scratch_artifacts/setdiff.py
??	scratch_artifacts/sm_comp.txt
??	scratch_artifacts/sm_notation.txt
??	scratch_artifacts/sm_snap.txt
??	scratch_artifacts/smoke.err
??	scratch_artifacts/smoke.json
??	scratch_artifacts/smoke_and_cadence.py
??	scratch_artifacts/snap_after.txt
??	scratch_artifacts/snap_final.txt
??	scratch_artifacts/snap_full.txt
??	scratch_artifacts/snap_run.txt
??	scratch_artifacts/snap_step1.txt
??	scratch_artifacts/snap_test.log
??	scratch_artifacts/snap_test2.log
??	scratch_artifacts/snapshot_full.txt
??	scratch_artifacts/stepM_analysis_all.txt
??	scratch_artifacts/stepM_analysis_test.txt
??	scratch_artifacts/stepM_analyze.py
??	scratch_artifacts/stepM_l5_measure.txt
??	scratch_artifacts/taskB_run.sh
??	scratch_artifacts/u1_byteid/
??	scratch_artifacts/u1_composing_tests.txt
??	scratch_artifacts/u1_pipeline_snap.txt
??	scratch_artifacts/v2_composing.txt
??	scratch_artifacts/v2_notation.txt
??	scratch_artifacts/v2_snap.txt
??	scratch_artifacts/wjd_curl_err.txt
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
396 changed path record(s) [worktree]
```

### C.2 — the last-bytes check (0(d)), with the pinned blobs

*Saved to the scratch file `t0_lastbytes.txt`.*


```text
records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md
  blob cee54d127030ca408e8d57bce9ac0920385c9a58 size 150042
  zero bytes: 0
  carriage returns: 0
  last byte is newline: True
  last 70 bytes: b'. TOWARDS the ultimate objective and TOWARDS the guiding principles.*\n'
records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventy_five.md
  blob 5cf72cd67dee64aefd3f0fe7677e3c1bafe016c4 size 11337
  zero bytes: 0
  carriage returns: 0
  last byte is newline: True
  last 70 bytes: b'ce: Cowork, 2026-10-03 (Stockholm), the sitting booted on entry 274.*\n'
```

### C.3a — the opening guard capture (0(f))

*Saved to the scratch file `guard_open.txt`.*


```text
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

### C.3b — the classification after the opening capture (exit 2)

*Saved to the scratch file `gclass_open.txt`.*


```text
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

### C.4a — the closing guard capture (2(d)), with its environment

*Saved to the scratch files `t2d_env.txt`, `guard_close.txt`.*

`t2d_env.txt`:
```text
bash=5.2.37(1)-release PYTHONUTF8=[unset] PYTHONIOENCODING=[unset] Python 3.14.3
guard exit:0
classification exit:2
```

`guard_close.txt`:
```text
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

### C.4b — the classification after the closing capture (exit 2)

*Saved to the scratch file `gclass_close.txt`.*


```text
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

### C.4c — the two captures compared, and guard_state.json's summary and per-tool verdicts under `runs`

*Saved to the scratch file `t2d_compare.txt`.*


```text
opening verdict lines: 104 ; closing verdict lines: 104
IDENTICAL VERDICT FOR VERDICT: True
closing FAIL set:
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
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
closing summary: 80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
guard_state.json summary at 5fa68913: {'run': 80, 'passing': 68, 'failing': 12, 'failing_tools': [{'tool': 'tools/audit/gen_phase3_gate_partition.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_filing_convention_application.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_artifact_inventory.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_artifact_inventory_surface.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_test_construction_evidence.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_retirement_caller_check.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/apply_soft_discard.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/apply_residue_discard.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_epoch_write_path.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_recognizer_establishment_sort.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/gen_home_classification.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/gen_phase1p_delegation_bar.py', 'args': ['--check']}], 'not_run': 4, 'historical_records': 19}
guard_state.json summary, new:        {'run': 80, 'passing': 68, 'failing': 12, 'failing_tools': [{'tool': 'tools/audit/gen_phase3_gate_partition.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_filing_convention_application.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_artifact_inventory.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_artifact_inventory_surface.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_test_construction_evidence.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_retirement_caller_check.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/apply_soft_discard.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/apply_residue_discard.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_epoch_write_path.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_recognizer_establishment_sort.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/gen_home_classification.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/gen_phase1p_delegation_bar.py', 'args': ['--check']}], 'not_run': 4, 'historical_records': 19}
per-tool verdicts read from the artifact's `runs`: 80 and 80 ; identical: True
FAIL in the new artifact: ['tools/audit/decisions/apply_residue_discard.py --check', 'tools/audit/decisions/apply_soft_discard.py --check', 'tools/audit/decisions/gen_home_classification.py --check', 'tools/audit/decisions/gen_phase1p_delegation_bar.py --check', 'tools/audit/gen_artifact_inventory.py --check', 'tools/audit/gen_artifact_inventory_surface.py --check', 'tools/audit/gen_epoch_write_path.py --check', 'tools/audit/gen_filing_convention_application.py --check', 'tools/audit/gen_phase3_gate_partition.py --check', 'tools/audit/gen_recognizer_establishment_sort.py --check', 'tools/audit/gen_retirement_caller_check.py --check', 'tools/audit/gen_test_construction_evidence.py --check']
```

### C.4d — guard_state.json between the boot tip's blob and the new blob, by explicit hashes

*Saved to the scratch file `c4d_guardstate.txt`.*


```text
diff --git a/f7982ee9f24286291309a46b18a081e1b57f476a b/c242fb0488149e9005ceedc54f257865d250b390
index f7982ee9f2..c242fb0488 100644
--- a/f7982ee9f24286291309a46b18a081e1b57f476a
+++ b/c242fb0488149e9005ceedc54f257865d250b390
@@ -1041,7 +1041,7 @@
       "exit_code": 0,
       "verdict": "PASS",
       "stdout": [
-        "  entries moved: 1, 2,271 characters",
+        "  entries moved: 1, 2,287 characters",
         "  byte-present in the archive exactly once: True",
         "  absent from the must-read:                True"
       ],
@@ -1161,15 +1161,15 @@
         "    [conditional  ] VS Code extension — bash command rules                    3013",
         "  whole file 168350, the six session-start spans 104609, overstated by 63741",
         "    CLAUDE.md                                                                104609",
-        "    STATUS.md                                                                 11564",
+        "    STATUS.md                                                                 11812",
         "    DECISIONS.md                                                             127727",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826",
-        "  total at the tree 246726",
+        "  total at the tree 246974",
         "  further spans of the same artifact, NOT counted into the read:",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951",
-        "  vs 1760d9a4a8: 367121 [whole-file practice] -> 246726 [ruled membership]  (-120395, -32.79%)  <- CROSSES A REGIME BOUNDARY",
-        "  vs 594074e1e1: 296832 [whole-file practice] -> 246726 [ruled membership]  (-50106, -16.88%)  <- CROSSES A REGIME BOUNDARY"
+        "  vs 1760d9a4a8: 367121 [whole-file practice] -> 246974 [ruled membership]  (-120147, -32.73%)  <- CROSSES A REGIME BOUNDARY",
+        "  vs 594074e1e1: 296832 [whole-file practice] -> 246974 [ruled membership]  (-49858, -16.80%)  <- CROSSES A REGIME BOUNDARY"
       ],
       "stderr": [],
       "what_it_checks": "what an ordinary session reads at session start, in characters, measured at the tree and at the recorded earlier commit's git object. It is the arc's own subject made checkable: the pruning direction of 2026-08-16 is about this number, and every act in the arc has had to state what it saved. Its load-bearing STOP is a demand about the tree AS IT STANDS — rule (a)'s artifact-and-key pointer is PARSED FROM THE CLAUSE ITSELF and must RESOLVE in the artifact it names, so a pointer that has stopped resolving fails on the day it stops rather than being hidden inside a number. It goes red when a governing surface changes, which is the point: the session-start read moved and the record does not yet say so. ★ WHAT IT DOES NOT ASSERT: that the membership is complete — it is AUTHORED, and each member carries the clause that makes it one so the authored half is checkable by reading three clauses; and nothing about whether the read is small enough, which is [[OI-370]]'s own subject"
@@ -1195,7 +1195,7 @@
         "  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends",
         "    the ruled closing reading would attribute 51684; the literal paragraph reading 160906",
         "    of the six session-start spans (104609): 12.39%",
-        "    of the whole session-start read (246726): 5.25%",
+        "    of the whole session-start read (246974): 5.25%",
         "  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,",
         "  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md)."
       ],
```

### C.5a — the `STATUS.md` entry extracted and word-scanned (2(a))

*Saved to the scratch file `t2a_entry.txt`.*


```text
entry chars: 2548 ; 'Last updated' lines: 1
names the thirteenth dispatch: True
twelfth entry no longer carries the prefix: True
RESERVED register | no outgoing text, derivation, brief, boot pack or decisions register was edited; the five questions the derivation marks for the
RESERVED register |  open-items row created, flipped or discarded; no decisions-register identity allocated; no tool source edited but the forward b
RESERVED scores |  and its archive; no   file, build, test, golden, corpus of scores or measurement of the analysis. Per the OI-222 pointer conv
```

### C.5b — the forward bound's `--apply` (2(b))

*Saved to the scratch file `t2b_apply.txt`.*


```text
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 2,287 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

### C.5c — the forward bound's `--check` (2(b))

*Saved to the scratch file `t2b_check.txt`.*


```text
  entries moved: 1, 2,287 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

### C.6 — the five regenerations and their `--check`s (2(c))

*Saved to the scratch files `t2c_env.txt`, `t2c_exits.txt`, `t2c_gen_evidence_pin_membership.txt`, `t2c_gen_evidence_pin_membership_check.txt`, `t2c_gen_l0_l1_outgoing_population.txt`, `t2c_gen_l0_l1_outgoing_population_check.txt`, `t2c_gen_l2_outgoing_population.txt`, `t2c_gen_l2_outgoing_population_check.txt`, `t2c_gen_defense_share.txt`, `t2c_gen_defense_share_check.txt`, `t2c_gen_session_start_read_size.txt`, `t2c_gen_session_start_read_size_check.txt`.*

`t2c_env.txt`:
```text
PYTHONUTF8=[unset] PYTHONIOENCODING=[unset]
```

`t2c_exits.txt`:
```text
gen_evidence_pin_membership run exit:0
gen_evidence_pin_membership check exit:0
gen_l0_l1_outgoing_population run exit:0
gen_l0_l1_outgoing_population check exit:0
gen_l2_outgoing_population run exit:0
gen_l2_outgoing_population check exit:0
gen_defense_share run exit:0
gen_defense_share check exit:0
gen_session_start_read_size run exit:0
gen_session_start_read_size check exit:0
```

`t2c_gen_evidence_pin_membership.txt`:
```text
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

`t2c_gen_evidence_pin_membership_check.txt`:
```text
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

`t2c_gen_l0_l1_outgoing_population.txt`:
```text
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
```

`t2c_gen_l0_l1_outgoing_population_check.txt`:
```text
l0_l1_outgoing_population.json re-derives
```

`t2c_gen_l2_outgoing_population.txt`:
```text
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

`t2c_gen_l2_outgoing_population_check.txt`:
```text
l2_outgoing_population.json re-derives
```

`t2c_gen_defense_share.txt`:
```text
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
    of the whole session-start read (246974): 5.25%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

`t2c_gen_defense_share_check.txt`:
```text
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
    of the whole session-start read (246974): 5.25%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

`t2c_gen_session_start_read_size.txt`:
```text
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
    STATUS.md                                                                 11812
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 246974
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 246974 [ruled membership]  (-120147, -32.73%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 246974 [ruled membership]  (-49858, -16.80%)  <- CROSSES A REGIME BOUNDARY
```

`t2c_gen_session_start_read_size_check.txt`:
```text
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
    STATUS.md                                                                 11812
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 246974
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 246974 [ruled membership]  (-120147, -32.73%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 246974 [ruled membership]  (-49858, -16.80%)  <- CROSSES A REGIME BOUNDARY
```

### C.7 — the artifact comparisons line by line, and the A3 tally check with the members compared by path (2(c))

*Saved to the scratch file `t2c_compare.txt`.*


```text
===== tools/audit/evidence_pin_membership.json: committed blob 54f774d82a2d2e5a9ec99b13666bd83d63ac5257 -> new blob 54f774d82a2d2e5a9ec99b13666bd83d63ac5257: IDENTICAL
===== tools/audit/l0_l1_outgoing_population.json: committed blob e310fb57ac53f9a06f8a9295d70c17ec143e3ce3 -> new blob e310fb57ac53f9a06f8a9295d70c17ec143e3ce3: IDENTICAL
===== tools/audit/l2_outgoing_population.json: committed blob b0e9e747cb0c44dfdba09c80c7860332546f4732 -> new blob aedc6b1914783190cc6dcd40a6168a81403ee829: MOVED
  --- committed
  +++ new
  @@ -40141 +40141 @@
  -       "line": "*Last updated: 2026-10-03 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 51: POSITIONS 51 AND 52 — THE `cowork_layer1_note_model_design.md` PASSAGES
  +       "line": "*Last updated: 2026-10-04 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 53: POSITIONS 53 TO 61 ARE NOW TABULATED, EACH WHOLE, AND POSITION 62 IS
  @@ -40147 +40147 @@
  -       "line": "*Last updated: 2026-10-03 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 51: POSITIONS 51 AND 52 — THE `cowork_layer1_note_model_design.md` PASSAGES
  +       "line": "*Last updated: 2026-10-04 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 53: POSITIONS 53 TO 61 ARE NOW TABULATED, EACH WHOLE, AND POSITION 62 IS
===== tools/audit/defense_share.json: committed blob 20c5f404d70f7691e7fd3aca02935507251b6476 -> new blob 889156e05a325af4c484f1ef5c7afd10cf8f6a20: MOVED
  --- committed
  +++ new
  @@ -80 +80 @@
  -  "the_whole_ordinary_session_start_read": 246726,
  +  "the_whole_ordinary_session_start_read": 246974,
===== tools/audit/session_start_read_size.json: committed blob 576f1e44f0d55631782a7025959d7fa90ae5155b -> new blob 0577d359c5d88413eacced669e4af87f5ef9b9fb: MOVED
  --- committed
  +++ new
  @@ -179 +179 @@
  -   "STATUS.md": 11564,
  +   "STATUS.md": 11812,
  @@ -183 +183 @@
  -  "total_characters": 246726,
  +  "total_characters": 246974,
  @@ -279 +279 @@
  -   "to_total": 246726,
  +   "to_total": 246974,
  @@ -281,2 +281,2 @@
  -   "change_in_characters": -120395,
  -   "change_percent": -32.79,
  +   "change_in_characters": -120147,
  +   "change_percent": -32.73,
  @@ -290 +290 @@
  -   "to_total": 246726,
  +   "to_total": 246974,
  @@ -292,2 +292,2 @@
  -   "change_in_characters": -50106,
  -   "change_percent": -16.88,
  +   "change_in_characters": -49858,
  +   "change_percent": -16.8,
===== tools/audit/status_batch_bound.json: committed blob 1def782a6d870577a87f1ea91318348ae2ba2d66 -> new blob 3a482f544996e216351b556f6f0b38823cb92e00: MOVED
  --- committed
  +++ new
  @@ -4 +4 @@
  - "dispatch": "cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md, Task 2",
  + "dispatch": "cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md, Task 2",
  @@ -479,0 +480,6 @@
  +  },
  +  {
  +   "executing_act": "cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md, Task 2",
  +   "base_commit": "986ada4a41b7fcdac6ba0be93b8382160afe4cc8",
  +   "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md",
  +   "the_kind_of_move": "ordinary"
  @@ -483,2 +489,2 @@
  - "base_commit": "cc8acd05a1ad1ba56870513e0e95d89f98789081",
  - "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md",
  + "base_commit": "986ada4a41b7fcdac6ba0be93b8382160afe4cc8",
  + "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md",
  @@ -487 +493 @@
  - "characters_moved": 2271,
  + "characters_moved": 2287,
  @@ -491,2 +497,2 @@
  -   "characters": 2271,
  -   "sha256": "35903917f897f5500e5fc3986d8077140173c346f7b8f4c88290ca59522d21f8",
  +   "characters": 2287,
  +   "sha256": "71e5070d6ee4e68282a2b0f459a354b976bba1f16297bf7bf43da7e1bd147820",
  @@ -495 +501 @@
  -   "opening": "*2026-10-03 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`. **★★ THE L2 TABULATION CONTINUED FROM POSI"
  +   "opening": "*2026-10-03 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`. **★★ THE L2 TABULATION CONTINUED FROM POSIT"
===== A3 tally check
term | tally committed | tally new | tally change | STATUS.md residue hit_records committed | new | change | equal
every term's tally change equals its change in STATUS.md's residue hit records: True
terms whose tally moved: 0
every other field outside STATUS.md's residue record and the tally identical: True
the_tabulation_population -> the_members identical by that path: True (62 and 62 members)
residue file list identical: True
STATUS.md residue record: hits 3 -> 3 ; hit_lines_distinct 2 -> 2
```

### C.8 — the chain of commits at 0(b), the batch's own commits, and the members' footprint

*Saved to the scratch files `t0_chain.txt`, `chain_members.txt`, `members_footprint.txt`.*

`t0_chain.txt`:
```text
commit 5fa68913cbbbd421072d8384338cc623ccc7dafc
parent 096b6cde83575de10e31a6e5bae350092792e9c2
tree 85fd48e1e15bdedf467f3e7464c7dc546aed592e
subject Close: the L2 tabulation continued from position 51, under its dispatch

 STATUS.md                                          |    2 +-
 STATUS_ARCHIVE.md                                  |    4 +
 ..._l2_comparison_tabulation_twelfth_2026_10_03.md | 1951 ++++++++++++++++++++
 tools/audit/defense_share.json                     |    2 +-
 tools/audit/gen_status_batch_bound.py              |   51 +-
 tools/audit/guard_state.json                       |   12 +-
 tools/audit/l2_outgoing_population.json            |   12 +-
 tools/audit/session_start_read_size.json           |   16 +-
 tools/audit/status_batch_bound.json                |   20 +-
 9 files changed, 2040 insertions(+), 30 deletions(-)
----
commit 096b6cde83575de10e31a6e5bae350092792e9c2
parent 7736090ffeea37cda2eb892a3524361f810b8c57
tree cf6f96fdd23685c0b683dfbc9094b4b436b52a37
subject comparison L2: member 52 tabulated - 60 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 704 ++++++++++++++++++++-
 1 file changed, 692 insertions(+), 12 deletions(-)
----
commit 7736090ffeea37cda2eb892a3524361f810b8c57
parent cc8acd05a1ad1ba56870513e0e95d89f98789081
tree e869a6d23923cc339e0f485e05c29713c58d5440
subject comparison L2: member 51 tabulated - 91 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 1084 +++++++++++++++++++-
 1 file changed, 1071 insertions(+), 13 deletions(-)
----
commit cc8acd05a1ad1ba56870513e0e95d89f98789081
parent 3d218b1c427724bb313306f8fc4afc422e6ff528
tree d8045e97e67e04b7072e4bd546028b9a33e79998
subject record: entry 274 and the twelfth L2 tabulation dispatch

 ..._l2_comparison_tabulation_twelfth_2026_10_03.md | 1449 ++++++++++++++++++++
 ...k_handoff_entry_two_hundred_and_seventy_four.md |  109 ++
 2 files changed, 1558 insertions(+)
----
```

`chain_members.txt`:
```text
2f1bde426aa6fe60be6bde5a92a89a7fd7caec00 a50b183e13e9b593029acf28f50aa978d9c73f42 5370e65c125980cc2d6f3e0d94e112aebae9b7d6 comparison L2: member 61 tabulated - 8 outgoing statements placed, proposals only
a50b183e13e9b593029acf28f50aa978d9c73f42 fa2309b7e8b6f2c8d7fb32219fd504e068ee93c5 f59ed12c9548e48a6351a50943440ec53a0dcfb4 comparison L2: member 60 tabulated - 8 outgoing statements placed, proposals only
fa2309b7e8b6f2c8d7fb32219fd504e068ee93c5 806edbc3f5bf16a547e4de5b8920bde231af11a1 32cee3e1a750f73b8d71a22ba9b7e072cd6cfe75 comparison L2: member 59 tabulated - 6 outgoing statements placed, proposals only
806edbc3f5bf16a547e4de5b8920bde231af11a1 ae7f91c21af6fcd0e16998b3cd6ebe80a1ef6bd0 c64cb50e213097c1a11bf1772d59005f1759de6c comparison L2: member 58 tabulated - 12 outgoing statements placed, proposals only
ae7f91c21af6fcd0e16998b3cd6ebe80a1ef6bd0 f2ff5aef2c559a9f54fdf90c70ee42e209f030f6 4b7497414985d9e5a961854cde1d1771c1a2f8b5 comparison L2: member 57 tabulated - 21 outgoing statements placed, proposals only
f2ff5aef2c559a9f54fdf90c70ee42e209f030f6 202fe6e7b940d345a575baa0a8d62c0081160d4b d65c16af91a5a1afaa6b21fd7888e9b126e2500d comparison L2: member 56 tabulated - 9 outgoing statements placed, proposals only
202fe6e7b940d345a575baa0a8d62c0081160d4b e101c17eb415abd29af8629926f0865cc1e294dc 6df2333e3c5af1ec26897b239e9208594571cfce comparison L2: member 55 tabulated - 23 outgoing statements placed, proposals only
e101c17eb415abd29af8629926f0865cc1e294dc e5e5c5cf937700381b5d2ab0e50af425d42aab26 43ed276db4b157ee016bf083d94d42f8705c4ffa comparison L2: member 54 tabulated - 5 outgoing statements placed, proposals only
e5e5c5cf937700381b5d2ab0e50af425d42aab26 986ada4a41b7fcdac6ba0be93b8382160afe4cc8 95177baeef0da83689e66399f91769c6617e9d40 comparison L2: member 53 tabulated - 96 outgoing statements placed, proposals only
986ada4a41b7fcdac6ba0be93b8382160afe4cc8 5fa68913cbbbd421072d8384338cc623ccc7dafc 33745aac87ccd01928e1ba3fbf20ca9ba076c43a record: entry 275 and the thirteenth L2 tabulation dispatch
```

`members_footprint.txt`:
```text
M	ratification_surfaces/cowork_comparison_l2_reading.md
```

### C.9 — A5's span (§6.1 to §6.52)

*Saved to the scratch file `a5_out.txt`.*


```text
span at 5fa68913 (to the line before '## 7.'): 3762297 chars
span at 2f1bde42 (to the separator before '### 6.53 — '): 3762297 chars
BYTE-IDENTICAL: True
```

### C.10 — the reading file's ordered updates verified at the object of the last member commit

*Saved to the scratch file `c10_verify.txt`.*


```text
twelfth batch sentence at 5fa68913 (to the stop clause): 'The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch order' ... 'wn commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close.'
twelfth batch sentence present verbatim at 2f1bde42: True (374 and 374 chars)
thirteenth batch sentence: The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there.
  ends with its stop reason, no clause on where the writing stands: True
header: True
resume pointer: **The next writing resumes at position 62**, the L0/L1 transfer input — `ratification_surfaces/cowork_comparison_l0_l1_reading.md` §10.
§0 row 53 DONE: True
§0 row 54 DONE: True
§0 row 55 DONE: True
§0 row 56 DONE: True
§0 row 57 DONE: True
§0 row 58 DONE: True
§0 row 59 DONE: True
§0 row 60 DONE: True
§0 row 61 DONE: True
§0 row 62 NOT YET TABULATED: True
§16 clause: True
heading 6.53 after one separator: True
heading 6.54 after one separator: True
heading 6.55 after one separator: True
heading 6.56 after one separator: True
heading 6.57 after one separator: True
heading 6.58 after one separator: True
heading 6.59 after one separator: True
heading 6.60 after one separator: True
heading 6.61 after one separator: True
banner clause (thirteenth dispatch named, Task 1): True
no heading 6.62: True
```

### C.11 — the next member's size at the artifact (1(h))

*Saved to the scratch file `next62.txt`.*


```text
position 62 | ratification_surfaces/cowork_comparison_l0_l1_reading.md | lines 287 | bytes 21436 | ranges 1 | item-4 identities 0 | the L0/L1 transfer input
  label: ## 10. The TRANSFER LIST — every RELOCATED row, by target charter | ranges: [{'first_line_as_a_locator_only': 14856, 'last_line_as_a_locator_only': 15142, 'first_line_text': '## 10. The TRANSFER LIST — every RELOCATED row, by target charter', 'last_line_text': ''}]
```

### C.12 — the staged close set before the report was added, and the whole batch's tree difference

*Saved to the scratch file `c12_staged.txt`.*


```text
== staged close set (before the report): tree 5370e65c125980cc2d6f3e0d94e112aebae9b7d6 (last member commit 2f1bde42) -> index tree 230ec36a63c62a09e5b7958f7ddfbeb5fb54a9dd
:100644 100644 c4dc0c77cd 836746bebc M	STATUS.md
:100644 100644 92e2117821 54bf70ca90 M	STATUS_ARCHIVE.md
:100644 100644 20c5f404d7 889156e05a M	tools/audit/defense_share.json
:100644 100644 f061da2775 225cbbbd58 M	tools/audit/gen_status_batch_bound.py
:100644 100644 f7982ee9f2 c242fb0488 M	tools/audit/guard_state.json
:100644 100644 b0e9e747cb aedc6b1914 M	tools/audit/l2_outgoing_population.json
:100644 100644 576f1e44f0 0577d359c5 M	tools/audit/session_start_read_size.json
:100644 100644 1def782a6d 3a482f5449 M	tools/audit/status_batch_bound.json
== the whole batch: tree 85fd48e1e15bdedf467f3e7464c7dc546aed592e (the boot tip 5fa68913) -> index tree 230ec36a63c62a09e5b7958f7ddfbeb5fb54a9dd
M	STATUS.md
M	STATUS_ARCHIVE.md
M	ratification_surfaces/cowork_comparison_l2_reading.md
A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventy_five.md
M	tools/audit/defense_share.json
M	tools/audit/gen_status_batch_bound.py
M	tools/audit/guard_state.json
M	tools/audit/l2_outgoing_population.json
M	tools/audit/session_start_read_size.json
M	tools/audit/status_batch_bound.json
```

### C.13 — the rows of §6.1 to §6.52 the nine new members cite, at the object of the last member commit

*Saved to the scratch file `cited_rows.txt`.*


```text
member 1: 1.33, 1.34, 1.35, 1.36, 1.37, 1.38(ii)
member 2: 2.50(i)
member 4: 4.15, 4.19, 4.20(i), 4.20(ii), 4.21
member 5: 5.81, 5.83, 5.84(i), 5.90, 5.91, 5.149(i), 5.158, 5.243, 5.347
member 6: 6.8, 6.16, 6.22(iv), 6.127(iii), 6.198(ii)
member 7: 7.179, 7.180
member 8: 8.96, 8.98, 8.99(i), 8.99(ii), 8.100(i)
member 9: 9.5, 9.20, 9.30, 9.323
member 10: 10.55, 10.56
member 17: 17.23(ii)
member 21: 21.48(v), 21.49(iii), 21.65, 21.67
member 22: 22.98(iii), 22.100
member 23: 23.33
member 24: 24.4
member 36: 36.1
member 43: 43.35(i), 43.97(i)
member 48: 48.37, 48.53
member 50: 50.2, 50.6, 50.8(i), 50.9, 50.15(i), 50.15(ii), 50.32, 50.41(i), 50.62, 50.70, 50.76(ii)
rows cited: 64
```

### C.14 — the word scan of this report's own prose (the body above the appendices)

*Saved to the scratch file `report_wordscan.txt`.* Every remaining hit is a word the scans found, named as found, or a qualified or musical form.


```text
BRITISH labelling | re added. - **Member 61:** the word scan found the British *labelling* twice and non-musical *rest* and *part* in my titles   (re
RESERVED scaled | g the predicate* 240–242); the word scan found non-musical *scaled* and *flat* and two row labels carrying   non-musical *scor
RESERVED flat | te* 240–242); the word scan found non-musical *scaled* and *flat* and two row labels carrying   non-musical *score* in my lo
RESERVED score | aled* and *flat* and two row labels carrying   non-musical *score* in my locators. Reworded (*growing with*, *span*, *the fun
RESERVED notes |    row*). - **Member 55:** the word scan found non-musical *notes* (*remarks*); a manifest phrasing broke the draft-manifest 
RESERVED bar | ewritten. - **Member 57:** the word scan found non-musical *bar* (*criterion*); the count check found Row 57.10 without per
RESERVED rest | d scan found the British *labelling* twice and non-musical *rest* and *part* in my titles   (reworded *labeling*, *remainder
RESERVED part | d the British *labelling* twice and non-musical *rest* and *part* in my titles   (reworded *labeling*, *remainder*, *portion
RESERVED key |  - **What the remaining word-scan hits are, read by eye:** *key*, *mode*, *notes* and *key state* in their musical   sense;
RESERVED mode | at the remaining word-scan hits are, read by eye:** *key*, *mode*, *notes* and *key state* in their musical   sense; *candid
RESERVED notes | emaining word-scan hits are, read by eye:** *key*, *mode*, *notes* and *key state* in their musical   sense; *candidate score
RESERVED key | d-scan hits are, read by eye:** *key*, *mode*, *notes* and *key state* in their musical   sense; *candidate score*, *decisi
RESERVED score | notes* and *key state* in their musical   sense; *candidate score*, *decisions register*, *open-items register* and *tie-brea
RESERVED register | te* in their musical   sense; *candidate score*, *decisions register*, *open-items register* and *tie-break*, the qualified form
RESERVED register | sense; *candidate score*, *decisions register*, *open-items register* and *tie-break*, the qualified forms; and hits inside   qu
RESERVED tie | te score*, *decisions register*, *open-items register* and *tie-break*, the qualified forms; and hits inside   quotations t
RESERVED key | ejected alternative are listed. - **Position 60, the legacy key analyzer's declared-mode change.** The small declared hint 
RESERVED mode | listed. - **Position 60, the legacy key analyzer's declared-mode change.** The small declared hint travels UNPLACED with Row
RESERVED register | e HISTORICAL.  **The further readings taken — the decisions register's standing of a decision homed in an item-4 document, read 
RESERVED register | row as the cross-member reading requires, and the decisions register's standing is stated at the row and the manifest without mo
RESERVED register | ount is restated. Its word scan (Appendix C.5a): *decisions register*, the qualified name, and   *scores* in its musical sense; 
RESERVED scores | dix C.5a): *decisions register*, the qualified name, and   *scores* in its musical sense; nothing to change. - **2(b)**  's ob
RESERVED graded | hanged, naming the same four tools.  ## 4. The assumptions, graded  - **A1 — held.** Established by the enumeration (Appendix 
RESERVED register | verning document but   and  , any source of   the decisions register or the open-items register, or the twelfth report; and insi
RESERVED register |  , any source of   the decisions register or the open-items register, or the twelfth report; and inside the reading file, §6.1 t
RESERVED mode |  Row 8.99(ii)). Searches for row titles naming the declared mode, the prior, ratification, a bounded coupling, a unified sta
RESERVED register | — *a second structural fix falsified* — while the decisions register's own statement of    D-289 is claim (ii)'s content. Row 61
RESERVED register | readings meet at rows of members 59 and 60.** The decisions register records D-376 SHELVED WITH EVIDENCE and    D-571 SUPERSEDED
RESERVED register |  is    HISTORICAL. The rows travel, and state the decisions register's standing; nothing is chosen between the two. 3. **The scr
RESERVED register | pped or discarded no open-items row, allocated no decisions-register identity, and edited no   file, test, golden, corpus, outgo
RESERVED register | input contract, L0/L1 reading file, source of the decisions register or the open-items register, governing document but   and  ,
RESERVED register | ng file, source of the decisions register or the open-items register, governing document but   and  , or tool source but the for
```
