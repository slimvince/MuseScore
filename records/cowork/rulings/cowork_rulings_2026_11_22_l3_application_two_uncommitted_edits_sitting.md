# Ruling record — 2026-11-22 — the two uncommitted edits Claude Code met at Task 0 of the L3 application dispatch

*The Cowork sitting booted on `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_one.md`.
**[checked]** means read at the object by this sitting; **[relayed]** means not.*

## 0. What happened

The L3 application dispatch (`records/cc/instructions/cc_instruction_l3_application_2026_11_08.md`), released on
2026-11-22, was handed to Claude Code. Claude Code stopped at Task 0's first act, before any commit, push or edit, and
reported to the user, who brought the report to this sitting. Its reason: assumption A1 makes a change at any committed
path a stop, except the families file and `docs/research_papers/BIBLIOGRAPHY.md`, and two other committed files carry
changes never committed.

## 1. The facts the ruling rests on

- **[checked]** `.git/HEAD` names `refs/heads/master`; `refs/heads/master` and `refs/remotes/origin/master` both read
  `e855ff2a38883bc453b3f1c83cb20b9fd89cda05`, modification times unmoved since entry 1181. The index's modification time
  is that of the commit (1794137605012).
- **[checked]** `docs/research_papers/README.md` is in the index, and its content on disk does not match the content
  fingerprint the index holds for it (index `352d9a8f3ec56d2a66ce83778c8a84e582f2e31a`; disk
  `fb2b3c1c598aa41edfe08f5f6ab2da72a6623165`; no carriage returns in the file). It carries rows for `A10383.pdf`,
  `Camb_MusPerc2006.pdf`, `CMA2016.pdf` and `20068.pdf` (its lines 33–36) and was last modified 2026-11-03 13:29,
  before the current commit (2026-11-08 12:33).
- **[checked]** `ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md` is in the index, and its
  content on disk does not match the index's fingerprint (index `ccfc164cf7fba596ec3673cc735f6e6225aecde2`; disk
  `4cf3fa722cb576b6bbd683f283ce06d9b7ec4ce6`; no carriage returns). It carries *"## 7. The check — 2026-11-08"* and was
  last modified 2026-11-08 12:44, after the current commit.
- **[checked]** `records/cowork/rulings/cowork_rulings_2026_11_08_l3_language_model_family_sitting.md`, which Task 0
  item 1 lands, gives the surface's §7 as the ground of its Ruling 1 (family 7 placed HISTORICAL).
- **[checked]** `records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md` §6: *"`BIBLIOGRAPHY.md`
  updated under its rules 1 and 2 (entry 497 §3 item 2) and `README.md` indexed"*.
- **[checked]** Task 0 item 5's sentence *"No other file of `docs/research_papers/` is named or landed"* is the wording
  of Ruling 8 of `records/cowork/rulings/cowork_rulings_2026_11_11_l3_application_release_part2_sitting.md`, whose list of
  what it read does not mention `README.md` and says the sections record's §6 was relayed, not opened.
- **[checked]** The dispatch names the current commit's identity on 13 lines, among them the boot checks.
- **[relayed, from Claude Code's report]** the size of the two changes ("four rows", "119 lines"); that the surface was
  first committed in `113b2ce680`; that the other 19 committed inputs are unchanged.

## 2. What was put

The full decision surface in the chat in its own turn: the two files and the facts above; five alternatives (A: amend
Task 0 so both land in its commit; B: commit them separately first, through a dispatch of their own, and rewrite the
13 lines naming the current commit; C: land the surface only; D: land neither, A1 amended to report them; E: put the
stored versions back on disk), each weighed towards the ultimate objective, towards the guiding principles and for its
meta level; the recommendation A in those three terms. Documentation only, no algorithm change. The user's word
*"continue"*; the choice question alone in a later turn, plain text, no widget.

## 3. Ruling 1 — alternative A (the user's word: "A")

**Task 0 of the L3 application dispatch is amended so that both edits land in its commit**: the language-model family
surface as a modified committed path under item 2 and act (1), as the families file is; `README.md` beside
`BIBLIOGRAPHY.md` under item 5, by the same act per file. Ruling 8's sentence *"No other file of `docs/research_papers/`
is named or landed"* stands, now true with both files named. The ruling record and handoff entry 1182, written after the
amendment and before the second hand-over, are added to Task 0 items 1 and 3.

**Documentation only. Algorithm: no change.** The currently decided method stands as ruled: family 7's six rows are
HISTORICAL, a superseded plan, and add nothing to L3; the rest of L3 as the ratified records and the dispatch's later
Tasks state it.

## 4. Applied by this sitting

The twelve changes, shown whole to the user before landing and landed on his word *"yes"*: the banner's paragraph
*"AMENDED AFTER CLAUDE CODE'S STOP, 2026-11-22, AND RELEASED AGAIN"*; the committed-inputs note; the untracked-population
expectation; A1's exceptions; Task 0's opening expectation; item 1; item 2 (two places); item 3; item 5; act (1);
act (3) and its subject; E0. Every changed site keeps its former wording (#12). Proved by staging back: the dispatch at
941,330 bytes, 7,157 lines, modification time 1795371843765.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1181. The user's words: the opening instruction;
"try again" (after the folder was added); "shortened"; "continue" (taken first as leave to draft, corrected by the user:
"No, As ALWAYS, write a PROPER decision surface as we have defined and decided."); "continue" (to the choice question);
"A"; "yes" (to land the twelve changes).*
