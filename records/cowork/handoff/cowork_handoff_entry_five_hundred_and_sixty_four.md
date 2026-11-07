# Cowork handoff entry 564 — 2026-11-07 — LANGUAGE-MODEL CORRECTION: SCOPING BEGUN, FINDINGS RECORDED, NO DOCUMENT WRITTEN

**The current entry point.** Entry 563 is superseded as entry point and stands otherwise. **[checked]** means read at the
object by this sitting; **[relayed]** means not.

## 1. State

- **At boot [checked]:** entry 563 at 7,014 bytes in the handoff folder's listing, no later entry listed; the three files
  of its §1 at 7,264, 12,389 and 5,626 bytes when staged. The start-up chain read at the sections the 2026-11-02
  amendment to entry 291 §4 step 3 names; §3 of entries 529 to 562.
- **Session-start read shortened on the user's word ("shortened"):** `STATUS.md` whole (latest entry still the
  boot-chain landing of 2026-11-02); the gating answer at its counts (247 open, 222 gating, 25 non-gating); D-599 at its
  `DECISIONS.md` row.
- **The order, on the user's word ("continue" after the proposal):** the correction's scoping first, family 7's check
  after it.
- **Changed on disk:** this entry only.
- **Nothing is running; no dispatch is out; nothing is awaited.**
- **Not in git:** everything entry 563 §1 lists, plus this entry; the next dispatch's Task 0 lands them.

## 2. What this sitting established for the scope (language-model Ruling 2)

1. **D-440 to D-448, each read whole at `decisions/group_N.md` [checked]:** all nine record the in-product integration
   (a chat bridge in MuseScore, provider chosen by the user, model-driven score modification, editing operations, the
   model resolving the user's references). All nine conflict with Ruling 1, not only D-441, D-442 and D-446. Statuses:
   D-440, D-441 DEFERRED; D-442 to D-448 NOT STATED; all entry-ratified 2026-08-04. Homes: `ARCHITECTURE.md` (D-440,
   D-441); `docs/llm_integration.md` §4.2, §4.3, §5.2, §5.3, §6, §8.1, §8.2 (D-448, D-442, D-444, D-445, D-446, D-443,
   D-447), each as a contract home under D-430.
2. **D-139 to D-143 [checked at `tools/audit/decisions/backbone_decisions.json`, lines 21555–21702]:** group N, all
   five about the same integration (stateless tool calls; search agent; intentional vs computed; the analysis module as
   the model's context provider; the bridge confined to the core access layer). Retired 2026-08-17 by Ruling 1 of
   `cowork_rulings_2026_08_17_residue_sitting.md` (soft discard), and carried as untrusted candidates in
   `tools/audit/framework_untrusted_candidates.json` (lines 79–132 name them **[checked]**). That carry is a
   downstream place the correction reaches. They are absent from `DECISIONS.md` and the group files **[checked]**.
3. **`ARCHITECTURE.md` §19, lines 8088–8185, read whole [checked]:** "LLM Integration — Claude Composer"; §19.1 to
   §19.5 all describe the in-product integration (user's provider, chat panel, modification, generation; §19.3 the
   analysis module feeding the model and driving its validation). All conflict. The delegation at 8094–8098 makes
   `docs/llm_integration.md` the one detailed design for §19's scope.
4. **`docs/llm_integration.md`, read at its banner, §1 and its heading list only [checked]:** banner "Design phase. No
   code written yet."; §1 states natural-language interaction with scores through *"an LLM of the user's choice"*. Its
   headings (§2 capabilities, §4 architecture, §8 client, §9 phases, §10 composing module, §11 plugin API) all name
   in-product use. **Its passages beyond §1 were not read.**
5. **Not conflicting, found by narrow searches [checked]:** D-205 (group S): a human is ground truth where none exists,
   and an automated (language-model) judge may only point the human at likely errors — consistent with Ruling 1, and a
   possible precedent for family 7's test-time tool. D-037's provenance quotes OI-241 naming D-143 (a quotation of a
   past record). OI-241 and OI-268: RULED 2026-08-02 and ARCHIVED, neither in the gating answer. OI-207's §19 mention
   is a reading history; OI-205's mention concerns context size. In the decisions group files other than N, the only
   hits for the integration's terms were D-205 and D-037.

## 3. What the next session does

As entry 529 §3, with entries 530 §3, 531 §3 steps 3–4, 532 §3 and 533 to 563 §3 kept as they still apply, and these:

1. **Prove one size:** this entry at the handoff folder's listing.
2. **Finish the scoping searches, narrow patterns only, `count` mode first, then content limited by `-o` with a short
   context:** (a) the rulings folder's records for `llm_integration|Claude Composer|D-44[0-8]\b|D-1(39|4[0-3])\b`;
   (b) both reading files for `llm_integration\.md` and `§ ?19\.[1-5]` — **never `^\| OI-` or any alternation that
   matches every row** (this sitting broke the rule three times); (c) `CLAUDE.md`, `FRAMEWORK.md` and the `docs` folder
   for the same terms; (d) the family-7 surface read whole. An `OPEN_ITEMS.md` row is read only by its exact heading,
   `^\| OI-NNN \| [^|]*\|`.
3. **Read `docs/llm_integration.md` at the passages that state run-time or shipped use** (§2, §4.4, §8, §9, §10 at
   least), and its sections homing D-442 to D-448.
4. **Judge capacity out loud; then write the scope document** (what conflicts, at which object; what rests on it;
   what does not conflict), **check it as a turn of its own**, then the dispatch for Claude Code with the push to the
   central repository. Whether an entry is amended, retired or replaced follows the register's own rules (note the
   retired-and-carried form of D-139 to D-143); where they do not decide, it goes to the user. Documentation only: the
   analysis method is not changed.
5. **Then family 7's check**, as entry 563 §3 step 4.
6. **Write narrowly;** mark a fact checked only at the object read; no counts of the sitting's own reads.
7. **The session-start read:** full or shortened is the user's; ask.

## 4. Who does what, in this order

1. **Nothing is given to Claude Code now.** No dispatch was written; nothing is running; nothing is awaited.
2. **THE USER opens a NEW Cowork session** and gives it exactly this:
   > Read and follow `C:\s\MS\records\cowork\handoff\cowork_handoff_entry_five_hundred_and_sixty_four.md`. Make the device-info call first. Use no shell at any point, not even to read that file or to prove a landing: stage it and use the file tools.
3. **That session boots** as entry 529 §4 step 3 says, reading this entry whole and §3 of entries 529 to 563, proves
   the size of §3 step 1, reports the boot with a capacity judgment, then does §3.
4. **If that session writes a dispatch, that session, not this one, tells the user what to hand to Claude Code.**

**If the user overrules any of this or changes the order, the session follows him.** **This session is now read-only**
(the user's rule of 2026-10-14).

## 5. Departures, declared

- No shell command, in the container or on the device. No memory tool, git, widget, task list, subagent or web access.
  `C:\s\MS` was not connected at boot and was requested after the device-info call. Folders listed: the handoff folder
  and `decisions` (once each). Never the repository root.
- **Three over-broad searches of `OPEN_ITEMS.md`** (patterns that matched every row) — a breach of entry 530 §3 step 3,
  and the degradation tell on which this sitting handed over.

*Provenance: Cowork, 2026-11-07 (Stockholm), the sitting booted on entry 563. The user's words: the opening instruction;
"shortened"; "continue"; "yes".*
