# Scope — correcting the record to the language-model rulings of 2026-11-07 (Ruling 2's scope), 2026-11-07

> **STATUS: SCOPE DOCUMENT, NOT A RULING AND NOT A DISPATCH.** Cowork, 2026-11-07 (Stockholm), the sitting that booted
> on `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_four.md`. It says what conflicts with the
> language-model rulings, at which object, what rests on it, and what does not conflict. Nothing here is applied; no
> tracked document is edited by it. **The check (coherence, completeness, correctness, overstatement) has run, in the
> sitting booted on entry 565; it is §7, and its corrections stand at their sites with the former wordings kept.**
> **§8 (the open reads, and §5's open points tested against D-599) was added in the sitting booted on entry 566; its own
> check has run in that sitting and is §9.** *(Former wording: "its own check has NOT yet run.")*
> *(Former wording: "The check (coherence, completeness, correctness, overstatement) has NOT yet run on this document;
> it is a turn of its own, after this landing.")* **[checked]** means read at the object by this
> sitting; **[relayed]** means taken from another record and not read at its object by this sitting.

---

## 0. The rulings this scope serves

From `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` **[checked, read whole]**:

**Ruling 1** (the user's words):

> "The llm-integration is part of another workflow - to be used for comparing our (non LLM-based, procedural software
> solution) with a 2nd opinion for difficult cases (where there is no ground truth or otherwise not apparent from music
> theory community what is "right")."

> "LLM:S are only to be used during development of the software solution (in order to better it). Never at run-time in
> the finished product."

> "I repeat: llm-integration is NOT for finished shipped product. It might ONLY be used for getting an LLM:s second
> opinion when we test our product, and our product struggles with inference. LLM is NOT allowed anywhere near the
> finished product."

**Ruling 2** (the user's words): *"confliciting entries must be corrected - AND any down-stream effects of the
corrections too."*

**The test applied below:** a statement conflicts when it describes, decides or plans a language model used at
run-time, inside or shipped with the product, or used with a user present in the product. A statement does not conflict
when it describes a language model used during development to give a second opinion on the product's output.

## 1. Conflicts in the decisions register

### 1A. Live entries D-440 to D-448 (`decisions/group_N.md`, each read whole **[checked]**)

| Entry | What it decides, in plain words | Status | Home | Conflict |
|---|---|---|---|---|
| D-440 | The language-model module (`src/llm/`, "to be created") is built purpose-made, not waiting for the plugin-interface reform | DEFERRED | `ARCHITECTURE.md:8113-8116` | **In substance** — the module is an in-product bridge |
| D-441 | Asking about the music and changing it happen in one conversation; a fix re-uses the model's earlier reasoning | DEFERRED | `ARCHITECTURE.md:8135-8138` | **In substance** — a user conversing with the model in the product |
| D-442 | A rejected change goes back to the model as a tool-call error and is never shown to the user | NOT STATED | `docs/llm_integration.md:304-305` (§4.3) | **In substance** — the model changing the score in the product |
| D-443 | The user picks a model provider; tool use is the only requirement; a provider without it is read-only | NOT STATED | `docs/llm_integration.md:601-604` (§8.1) | **In substance** — a provider chosen in the product's preferences |
| D-444 | The core access layer is a facade over interfaces that already exist, not a redesign | NOT STATED | `docs/llm_integration.md:367-369` (§5.2) | **In its stated consumer only** — see below |
| D-445 | A musical address does not name one note, so a note carries its own identifier | NOT STATED | `docs/llm_integration.md:418-421` (§5.3) | **In its stated consumer only** — see below |
| D-446 | The model resolves how the user names a passage; no index is built | NOT STATED | `docs/llm_integration.md:518-521` (§6) | **In substance** — the model reading the user's words in the product |
| D-447 | The model's tool definitions are generated from the operation set | NOT STATED | `docs/llm_integration.md:613-615` (§8.2) | **In substance** — tools for the model to edit the score |
| D-448 | About forty editing operations, curated from observed use, are given to the model | NOT STATED | `docs/llm_integration.md:286-288` (§4.2) | **In substance** — the model editing the score |

All nine were entry-ratified on 2026-08-04 by the user, *"AS DRAFTED"*, with the register's own note that this
*"confirms that the register records the decision correctly; it is not a judgment that the decision is good"*
**[checked, at each entry's provenance]**. D-442 to D-448 each have a home section in `docs/llm_integration.md`, a
contract home reached by the delegation at `ARCHITECTURE.md:8096`; the section-level unit that decides each home is
D-430 **[checked, at each entry's Home section]**. *(Corrected at the check, §7 item 4; former wording: "D-442 to D-448
are homed under D-430 as a contract home reached by the delegation at `ARCHITECTURE.md:8096`".)*

**D-444 and D-445 — the distinction.** D-444's own plain words: *"The shared foundation the language-model bridge and
any future plugin interface both sit on is not new machinery"*. D-445 is a rule of that layer's information model. The
rule of each (a facade over existing interfaces; a note identifier) does not itself use a language model. What
conflicts is that the bridge is named as one of the layer's two consumers. Whether the layer is still wanted for the
other consumer, a future plugin interface, is not decided by Ruling 1 **[the writing side's reading of the two entries
against Ruling 1]**. *This narrows entry 564 §2 item 1, which says all nine conflict; entry 564 is not edited.*

### 1B. Retired entries D-139 to D-143 **[relayed from entry 564 §2 item 2, checked there at
`tools/audit/decisions/backbone_decisions.json` lines 21555–21702 and `tools/audit/framework_untrusted_candidates.json`
lines 79–132; not re-read by this sitting]**

All five are about the same integration (stateless tool calls; the model as search agent; intentional versus computed;
the analysis module as the model's context provider; the bridge confined to the core access layer). They were retired
on 2026-08-17 by the soft discard and carried into the framework phase as untrusted candidates. **The carry is the
downstream place:** an untrusted candidate that describes in-product use is a candidate Ruling 1 rules out. The
residue-sitting record's Ruling 1 **[checked, lines 28–37]** draws its membership from
`tools/audit/sole_carrier_subclass.json`, not by number; this sitting did not open that file.

## 2. Conflicts in documents

### 2A. `docs/llm_integration.md` (786 lines; read this sitting at §1, §2, §3.1 in part, §4.2 to §4.4, the lines homing
D-444, D-445, D-446, and §8 to §11 **[checked]**)

The document as a whole designs an in-product feature. Its own words: §1, *"make changes through conversation with an
LLM of the user's choice"* and *"**Claude Composer** is the working name for this capability"* (lines 28–37); §9, a
*"Basic chat panel UI in MuseScore"* (line 643), *"Diff preview UI"* and *"Accept / reject flow"* (lines 677–678);
§8.1, *"Users choose their LLM provider in MuseScore preferences"* and *"Supported at launch"* (lines 601–609); §11,
the bridge as a native module first and a plugin at the end state (lines 761–771). Banner: *"Design phase. No code
written yet."* (line 3).

**Sections that conflict in substance:** §1; §2.1 to §2.4; §3 (§3.1 read in part, §3.2 to §3.6 by heading only);
§4 (§4.1 not read, §4.2 to §4.4 read); §6; §7 (by heading and by the reading files' quotations of §7.3 only); §8; §9;
§10; §11.

**Sections that conflict in their stated consumer only:** §5 (the core access layer), as D-444 and D-445 above —
§5.1, §5.4, §5.5 not read.

**One passage that does not conflict:** §2.5, lines 117–118: *"The ambient layer uses the rule-based analysis from the
composing module, not the LLM, for latency reasons."* Its ambient features (lines 110–115) are listed under a heading
about what language models can do; the sentence itself puts no model in them.

### 2B. `ARCHITECTURE.md` §19, lines 8088–8185 **[relayed from entry 564 §2 item 3, read whole there; not re-read]**

*"LLM Integration — Claude Composer"*; §19.1 to §19.5 describe the in-product integration; §19.3 has the analysis
module feeding the model and driving its validation; lines 8094–8098 delegate §19's scope to
`docs/llm_integration.md`. All conflict. D-440 and D-441 are homed here.

## 3. What rests on the conflicting entries and passages (the downstream effects)

### 3A. Ruling records

1. **`records/cowork/rulings/cowork_document_route_rulings_2026_08_08.md`, route (i), third bullet** **[checked, lines
   33–37]**: the user ratified the delegation from `ARCHITECTURE.md` §19 to `docs/llm_integration.md` as *"The ONE
   detailed design for this section's scope"*, *"with the stated caveat resolved in its favour (the document is
   authoritative, not stale)"*. It is the act that makes D-442 to D-448 contract homes. It rests on the document being
   the authoritative design; Ruling 1 now rules that design out. **Reached.**
2. **Four records that name D-440 because its text carries the path `src/llm/`** and a leak check excludes it from a
   pack: `cowork_rulings_2026_08_22_withheld_family_sitting.md` Ruling 4 (line 92); `cowork_rulings_2026_08_24_sizing_leak_list_sitting.md`
   Ruling 1 (line 30); `cowork_rulings_2026_09_27_l2_leak_list_sitting.md` (line 52); `cowork_rulings_2026_10_17_l3_lists_sitting.md`
   (lines 73–74) **[each line checked; the records not read further]**. They treat D-440 as a string matched by a
   check, not as a decision in force. **Not a conflict.** If D-440 is retired, those exclusions may become moot — a
   bearing to note, not a correction.
3. **`cowork_rulings_2026_08_31_decision_surface_sitting.md`**: names `docs/llm_integration.md` Rows 20.2 to 20.4
   (§3.4, lines 4571–4572), Rows 20.7 to 20.9 (line 4192) and Row 20.10 (line 4901); lists the document in counts
   (lines 6446, 7123) and in the home-document list of L2's candidate criterion (line 7156); names D-440, D-441, D-442,
   D-443, D-444, D-447 and D-448 (not D-445 or D-446) as hits of the word *mode* inside *model* (line 6963) **[the
   lines checked; the rows' dispositions there not read]**. **Open:** the dispositions of the L0/L1 rows 20.x.
   *(Corrected at the check, §7 item 1; former wording: "names `docs/llm_integration.md` Rows 20.7 to 20.10 (lines 4192,
   4901) and lists the document in counts (lines 4571, 6446, 7123, 7156); names D-440 to D-448 as hits of the word
   *mode* inside *model* (line 6963)".)*
4. **`cowork_rulings_2026_08_17_rulings_sort_sitting.md`** line 42 lists D-443, D-444, D-447, D-448 among other entries
   **[the line checked; its context not read]**. **Open.**
5. **`cowork_rulings_2026_08_22_step_zero_return_sitting.md`** line 91 lists the document among others **[the line
   checked; its context not read]**. **Open.**

A search of the whole rulings folder for `llm_integration|Claude Composer|D-44[0-8]\b|D-1(39|4[0-3])\b` returned the
records above and the language-model ruling record itself, and no others **[checked by the sitting that wrote this
document, over the copies it had staged; at the check, the same pattern over the nine records the check staged
returned those nine and nothing else, which does not re-establish the folder-wide claim — see §7 item 3]**.
*(Former bracket: "[checked]".)*

### 3B. The reading files

1. **L2 reading file (`ratification_surfaces/cowork_comparison_l2_reading.md`)** **[checked at the lines named]**:
   - Row 36.1 (line 47766, `ARCHITECTURE.md` §19.3) and Rows 54.1 to 54.4 (lines 72487–72539, `docs/llm_integration.md`
     §7.3 and §10) — each **RULED RELOCATED to *L3 — The read-off facts*** by the L2 nothing-from-L3 Ruling 5, group
     *"Readers of the published record"*. Row 54.5 (voice-leading assessments handed to the model) — **proposed**
     RELOCATED to *the second axis — voice leading*, not ruled at the row.
   - The member's manifest describes the integration as *"a product tool outside the analysis"* (lines 72465–72469), and
     31 of its 34 *not a statement* items carry that label (lines 72557–72590); the other three are a label, a table's
     header row and a table's separator row (items 5, 11, 12). *(Corrected at the check, §7 item 2; former wording: "its
     34 *not a statement* items carry that label".)*
   - **Bearing:** the relocations were filing only (the ruling as quoted in the family-7 surface §1: *"filing only, no
     change to L2's algorithm as its statements define it"*). *(Corrected at the check, §7 item 5: the quotation
     completed; former wording ended it at "algorithm".)* Their ground, a reader of the published record, still holds for a test-time tool. The
     description *"a product tool"* is what conflicts **[the writing side's reading]**.
2. **L3 reading file (`ratification_surfaces/cowork_comparison_l3_reading.md`)** **[checked at the lines named]**:
   - §6.51, member 51, `docs/llm_integration.md` (from line 68265): 0 outgoing statements, 38 *not a statement*, by its
     manifest.
   - Rows 57.124 (i), (ii), 57.498 to 57.501 — family 7; see 3C.
   - **Row 21.102** (line 28935): the placeholder fields `useExistingChordSymbols`, `useRomanNumeralAnnotations`,
     `useNashvilleAnnotations`, **proposed QUARANTINED**. Its member's not-a-statement item 21 (line 30465) quotes the
     defense of keeping them: *"The LLM integration design (`docs/llm_integration.md`) and the Authoritative Chord
     Symbol Mode (§4.1f) depend on `useExistingChordSymbols`."* Half of that defense rests on the integration. **Reached,
     in part.**
3. **L0/L1 reading file (`ratification_surfaces/cowork_comparison_l0_l1_reading.md`)**: §6.20, document 20,
   `docs/llm_integration.md`, lines 10133–10576 **[the heading checked; the section not read]**. **Open.** *(Searched
   beyond entry 564's "both reading files", since the search was narrow.)*

### 3C. Work in hand — L3 family 7

`ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md` **[checked, read whole]**: describes the
six sentences as from *"a planned consumer outside the analysis — the language-model bridge, "whose module is to be
created""* (§2) and places them *"carried for the language-model bridge's own specification"* (§3A). Both rest on the
in-product bridge. Its check is entry 564 §3 step 5.

### 3D. Not searched by this sitting

`OPEN_ITEMS.md`; `DECISIONS.md` beyond D-599's row (entry 564 §2 item 5 records group-file searches); `src/`; tools
other than as relayed in 1B; the `docs` sub-folders (`old_docs`, `prompts`, `research_papers`, `apidocs_static`).

## 4. What does not conflict

1. **D-205** (group S): a human is the ground truth where none exists, and an automated (language-model) judge may only
   point the human at likely errors **[relayed from entry 564 §2 item 5]**.
2. **`docs/llm_triage_design.md`** **[checked, lines 1–40]**: *"LLM-Assisted Triage for Chord Inference Validation —
   Design Discussion"*, status *"Discussion only. No implementation committed."* Its problem: no mechanical comparator
   for scores without ground truth. Its core principle: *"When our inferrer, one or more LLMs, and any printed chord
   symbol differ within reason, flag that region for human inspection."* This is the test-time second opinion Ruling 1
   describes. **It is a source for family 7's re-test** (the description and the placement of a test-time tool).
3. Documents that refer to that triage **[each line checked; the documents not read further]**:
   `docs/quality_observations_iter76.md` §*LLM Triage as Quality Signal* (lines 190–215);
   `docs/nct_detection_design.md` (lines 4, 113–134, 216: deferred until LLM-triage data exists);
   `docs/unified_analysis_pipeline.md` line 94; `docs/score_inventory.md` lines 6, 34, 260 (the LLM-triage corpus);
   `CLAUDE.md` line 1385 (the only hit in `CLAUDE.md`).
4. `docs/decoder_design.md` line 518, a table cell *"LLM-assisted / academic"* **[the line checked; its context not
   read]** — not judged.
5. `FRAMEWORK.md` — no hit for the search terms **[checked]**.

## 5. What follows, and what goes to the user

**Documentation only. Algorithm: no change.** No language model is part of L2's or L3's method as decided. The method
that stands, as the family-7 surface §4 states it in its first part (its further clauses on presets, style labels, idiom
tags, the display and L3's own questions are not repeated here) *(corrected at the check, §7 item 6; former wording:
"as the family-7 surface §4 states it")*: L2 decides key and chord together and publishes the chord as a degree
in its tonality, and the tonality as tonic and mode; L3 publishes facts read off it (chord symbol, figured bass, harmonic
rhythm, cadence with type at each phrase end, phrase and section grouping, key areas, the pivot re-expression, the modal
counts per key area, and, once the application act amends `FRAMEWORK.md`, the catalog matches).

**What the register's own rules give, as far as read:** the register is generated from
`tools/audit/decisions/backbone_decisions.json` by `tools/audit/decisions/gen_decisions_register.py`, and an entry is
changed by editing the data and regenerating (`decisions/group_N.md` banner **[checked]**). One retiring form was found
by the sitting that wrote this document *(corrected at the check, §7 item 7; former wording: "One retiring form is on
the record")*: the soft discard, byte-preserving and revivable, with the statement standing at its home (residue-sitting
record, Ruling 1 **[checked]**). **Not read:** `DECISIONS.md`'s guide to its status words, which would say whether an
entry that a later ruling overrules is retired, superseded or re-statused. That read comes before any question is put.

**Open for the next step, each to be tested against the record (D-599) before it is put:**
1. The form for D-440, D-441, D-442, D-443, D-446, D-447, D-448 (conflict in substance).
2. Whether D-444 and D-445 stand with the bridge removed as a consumer, or go with the others.
3. The form for `docs/llm_integration.md` and `ARCHITECTURE.md` §19: rewritten to Ruling 1's purpose, or marked
   superseded with the former wording kept (#12).
4. The 2026-08-08 delegation (3A item 1), which follows from 3.
5. The reading files' descriptions (3B): corrected, annotated, or left as the record of what the documents said.
6. Row 21.102's defense (3B item 2): which half stands.
7. The open reads: 3A items 3 to 5, 3B item 3, 3D.

## 6. Departures, declared

No shell command, in the container or on the device. Every file staged by its path and read with the file tools;
searches with the Grep tool over staged copies, `count` mode first where the hit count was unknown. One search of the L3
reading file, for Row 21.102's heading, carried a second alternative that could have matched every ruled row
(`^\*RULED DISPOSITION`); it returned one line under a three-line limit. Declared as a breach of entry 564 §3 step 2's
rule in form, not in effect.

## 7. The check (coherence, completeness, correctness, overstatement)

Run in the sitting booted on entry 565, as a turn of its own, at the sources. **[checked]** at each object named.

**Held at the sources.** Ruling 1 and Ruling 2 as quoted in §0, word for word (the ruling record §1, §2). §1A: each of
D-440 to D-448 at `decisions/group_N.md` — status, home and home section as tabled; *"AS DRAFTED"* and the register's
note in each entry's provenance; D-440's entry ratification 2026-08-04 by the user; D-444's plain words; D-448's
*"forty"*. §2A: `docs/llm_integration.md` at lines 3, 26–46, 47–118, 328–369, 597–616, 755–786 — the quotations and line
numbers as given; §2.5's sentence and its bullets. §3A item 1: the route ruling at lines 33–37. §3A item 2: the four
records at the lines named. §3A item 4: `cowork_rulings_2026_08_17_rulings_sort_sitting.md` line 42, a list headed
*DESIGN-INTENT (24)*. §3A item 5: line 91. §3B item 1: Row 36.1 at line 47766 and Rows 54.1 to 54.5 at lines
72487–72553, the ruled and proposed dispositions as stated. §3B item 2: §6.51 at line 68265, its counts 0 and 38 at line
68324; Row 21.102 at line 28935, proposed QUARANTINED; item 21 at line 30465. §3C: the family-7 surface at lines
101–102 and the heading of §3A at line 108. §4 item 2: the triage document's title, status and core principle (lines 1,
3, 31–32). §4 item 3: hits at the lines named in the five documents and `CLAUDE.md` line 1385 (the only hit there).
§4 item 5: no hit in `FRAMEWORK.md`.

**Corrections, each made at its site with the former wording kept (#12):**

1. **§3A item 3, correctness.** Line 6963 names D-440 to D-444, D-447 and D-448 as *mode*-inside-*model* hits, not
   D-445 or D-446. Line 4571 names Rows 20.2 to 20.4 (§3.4), not a count; line 7156 is a home-document list, not a
   count.
2. **§3B item 1, overstatement.** 31 of the 34 *not a statement* items carry the *product tool* label, not all 34.
3. **§3A, the folder-wide search, overstatement of reach.** The claim rests on the copies the writing sitting had staged;
   its §6 does not say the whole rulings folder was staged. This check staged nine records and cannot re-establish the
   folder-wide claim. Marked as resting on that sitting's search. **Open:** a search over the whole rulings folder, if
   the correction act needs the list closed.
4. **§1A, precision.** *"Homed under D-430"* read as if D-430 were a home; D-430 is the rule that decides the home
   section.
5. **§3B item 1, a quotation cut short.** The quotation now ends where its sentence's clause ends.
6. **§5, a quotation cut short without saying so.** The method that stands is the first part of the family-7 surface's
   §4 statement; now said.
7. **§5, overstatement.** *"One retiring form is on the record"* asserted more than was searched; now stated as what
   that sitting found. `DECISIONS.md`'s guide to its status words remains the open read.

**Coherence.** §1A's narrowing of D-444 and D-445, §2A's §5 *"in its stated consumer only"*, and §5 item 2 agree.
§3B item 1 (Rows 54.2 to 54.4 at document lines 708–710) agrees with the document's headings: those lines lie in §10,
*Relationship to the Composing Module* (heading at line 695), though the L2 reading file's rows call them *"§8"*; this
document's *"§7.3 and §10"* is the right section reference. The reading file's own label is not corrected here.

**Completeness, not closed by this check.** §3D stands. §5 item 7's open reads stand. Not re-read: §1B and §4 item 1
(relayed in the document, still relayed); the triage-referring documents beyond their hit lines; D-445's and D-446's
own text beyond status and home.

**What this check does not change.** No finding in §1 to §5 moved: the conflicts, the downstream places, the open points
and *documentation only, algorithm: no change* stand as written.

## 8. The open reads of §5 item 7, and §5's open points tested against D-599

Written in the sitting booted on entry 566. **[checked]** at each object named. **Its check has run, in the same sitting
as a turn of its own; it is §9, and its corrections stand at their sites with the former wordings kept.** *(Former
wording: "This section has NOT yet been checked (coherence, completeness, correctness, overstatement); that check is a
turn of its own.")*

### 8A. What the open reads established

1. **`DECISIONS.md`'s guide to its status words** (lines 96–106) **[checked]**. There are seven status words: LIVE,
   SUPERSEDED BY, SUPERSEDED IN FACT, SHELVED WITH EVIDENCE, FALSIFIED, DEFERRED, NOT STATED. None of them is "retired".
   The three that bear here *(corrected at the check, §9 item 1; former wording: "The two that bear here:")*:
   - LIVE: *"In force. Nothing in the record supersedes, shelves or falsifies it."*
   - SUPERSEDED BY: *"A later ruling replaces it. The replacement is named."*
   - DEFERRED: *"Decided to be built later. The decision itself stands."*
2. **The L0/L1 reading file, §6.20** (lines 10133–10576, read whole) **[checked]**. There are 20 rows, 20.1 to 20.20.
   - Every row is derived from statements of the L0/L1 derivation (S-1, S-2, S-3 and others), and every disposition is
     argued from those statements.
   - The manifest describes the document as *"The design of a natural-language interface to the score — a consumer of
     the analysis rather than a part of it"* (line 10142).
   - Ruled at the rows: Rows 20.2 to 20.4 by Ruling 57 (§3bl); Rows 20.7 to 20.9 by Ruling 51 (§3bf); Rows 20.10 and
     20.12 by Ruling 62 (§3bq, items 10 and 11). The other rows carry no ruled disposition at the reading file; whether a
     ruling elsewhere reaches them was not searched *(corrected at the check, §9 item 2; former wording: "The other rows
     carry proposed dispositions only.")*.
   - Ruling 57 clause (ii), quoted at Row 20.3: *"S-2's bar binds every layer of the analysis and any consumer whose
     output feeds the analysis; a reader outside the analysis — D-522's explaining or editing consumer — may be handed
     annotation labelled as annotation for a purpose other than deciding the music, and may never feed it back in."*
     Ruling 62 item 11 (Row 20.12) rests on that clause and on D-522.
3. **D-522** (`decisions/group_C.md` lines 1000–1023, read whole) **[checked]**. LIVE. It says that explaining an
   inference to the end user is a late display consumer of facts already published. It names no language model.
4. **The decision-surface record** at lines 4186–4194, 4562–4575 and 4896–4903 **[checked]**. The rulings on Rows 20.2
   to 20.4, 20.7 to 20.9 and 20.10 cite `docs/llm_integration.md` as an outgoing text that reaches the derivation's own
   lists or tests from the other side. The grounds those passages give are the derivation's statements; Ruling 57's own
   paragraph was read only as the reading file quotes it, and at the record's facts paragraph (lines 4562–4575)
   *(corrected at the check, §9 item 3; former wording: "The ground of each ruling is the derivation's statements.")*.
   Lines 6446, 6963,
   7123 and 7156 were not re-read beyond what §3A item 3 records.
5. **The rulings-sort record**, line 42 in context (lines 27–54) **[checked]**. D-443, D-444, D-447 and D-448 are
   among the 24 returned entries Ruling 2 places DESIGN-INTENT (line 41). Ruling 1 calls the DESIGN-INTENT entries
   *"the framework phase's seed list"* (lines 29–30), and Ruling 2's placements join that total (line 51)
   *(corrected at the check, §9 item 4; former wording: "among the 24 entries placed DESIGN-INTENT: "the framework
   phase's seed list"")*. Lines 32–33: *"The seed list remains
   amendable when the framework phase consumes it; an amendment there is its own recorded act."*
6. **The step-zero-return record**, line 91 in context (lines 83–99) **[checked]**. `docs/llm_integration.md` is one
   of nine documents that have no changed passage in the screen's enumeration. Ruling 2 keeps all nine as members of
   the specification document set, read whole by the derivation.
7. **`OPEN_ITEMS.md`** **[checked, by search only]**. The pattern `llm_integration|Claude Composer|D-44[0-8]\b|D-1(39|4[0-3])\b|D-522\b`
   has no hit. The pattern `\bLLM|language[- ]model` has one hit, Row OI-205 (line 224). That row is about how much
   context a human or a language model can hold when reading `STATUS.md` and `ARCHITECTURE.md`; it does not conflict.
   This is a search for those terms, not a read of the file.

### 8B. §5's open points, tested against D-599 and the record

Each point below is put as **derived**, meaning the record decides it, or as **for the user**, meaning it does not.
The derivations are the writing side's reading of the objects named, and the user ratifies them.

1. **The form for D-440, D-441, D-442, D-443, D-446, D-447 and D-448 (§5 item 1). Derived: SUPERSEDED BY the
   2026-11-07 language-model record's Ruling 1.**
   - Ruling 1 is a later ruling, and it rules out what each of these entries decides: a language model in the shipped
     product.
   - Their present statuses are DEFERRED (D-440, D-441) and NOT STATED (D-442, D-443, D-446, D-447, D-448), per §1A.
   - NOT STATED no longer fits, because the record now speaks to them: Ruling 1 rules on their subject.
   - DEFERRED (D-440, D-441) no longer fits, because *"the decision itself stands"* is no longer true.
   - LIVE does not fit, because the record now supersedes them.
   *(Corrected at the check, §9 item 5; former first bullet: "LIVE no longer fits, because the record now supersedes
   them.", which read as if any of the seven were LIVE; none is.)*
   - SHELVED WITH EVIDENCE and FALSIFIED require a measurement, and none is involved.
   - The verbatim quotation and the 2026-08-04 entry ratification stay as they are. That ratification confirmed that
     the register recorded the decision correctly, and it still did.
   - The change is made in `tools/audit/decisions/backbone_decisions.json` and regenerated, per the banner of
     `decisions/group_N.md` (§5).
   - The soft discard (§1B) is not the form here. It was one ruled act over a defined population, not a standing form
     for correcting an entry **[the writing side's reading of §1B and §5, which relay the residue-sitting record; that
     record not opened by this sitting]** *(bracket added at the check, §9 item 6)*.
2. **D-444 and D-445 (§5 item 2). Derived: their status (NOT STATED, per §1A) is unchanged, with a provenance note that
   Ruling 1 removes the bridge as one of the core access layer's two consumers.** *(Corrected at the check, §9 item 7;
   former wording: "they stay LIVE, with a provenance note …"; neither is LIVE.)*
   - What conflicts is the stated consumer (§1A), not the rule.
   - Ruling 1 says nothing about the other consumer, a future plugin interface, so the record does not supersede the
     rule.
   - Ruling 2 asks for conflicting entries to be corrected. Superseding a rule that does not itself conflict would go
     beyond that.
3. **The form for `docs/llm_integration.md` and `ARCHITECTURE.md` §19 (§5 item 3). Derived: each marked superseded by
   Ruling 1, with its text kept (#12) and a pointer to `docs/llm_triage_design.md`. Neither is rewritten.**
   - Ruling 1's own words put the language-model use in *"another workflow"*, *"NOT for finished shipped product"*. So
     a section of the product's architecture should not describe that use as part of the product.
   - The record already holds the design of the test-time second opinion, in `docs/llm_triage_design.md` (§4 item 2).
     Rewriting the old document to that purpose would duplicate it.
   - `docs/llm_integration.md` §2.5, lines 117–118, does not conflict (§2A). It is kept under the same banner.
   - **The alternative, named so the user may take it:** rewrite §19 as a short section that states Ruling 1 and
     points to the triage design, with the former text kept beneath it.
4. **The 2026-08-08 delegation (§5 item 4). Derived: it follows from point 3.**
   - The route ruling made the document *"The ONE detailed design for this section's scope"* **[relayed from §3A item 1;
     not re-read by this sitting]**. Ruling 1 now rules that design out.
   - A note goes at the route record's bullet (lines 33–37), naming Ruling 1, with the bullet's wording kept.
   - The delegation lines in `ARCHITECTURE.md` (8094–8098 **[relayed from §2B]**) fall under point 3's banner.
5. **The reading files' descriptions (§5 item 5). Derived: each annotated, with the former wording kept. The
   dispositions are not changed.**
   - The descriptions are *"a product tool outside the analysis"* (L2 reading file, lines 72465–72469 and the 31 items
     at lines 72557–72590) and *"a natural-language interface to the score"* (L0/L1 reading file, line 10142).
   - Under Ruling 1 these descriptions are stale. The user's standing rule of 2026-09-22 has staleness fixed without
     asking **[the user's standing instruction to Cowork; not read at a repository object]** *(bracket added at the
     check, §9 item 8)*.
   - The dispositions rest on the derivation's statements (8A item 2) or on the ground *"a reader of the published
     record"* (§3B item 1). A test-time tool is still such a reader, so the dispositions stand.
6. **Row 21.102's defense (§5 item 6). Derived: the language-model half falls and the other half stands.**
   - The defense keeps the placeholder fields because of two things: the integration design, and the Authoritative
     Chord Symbol Mode.
   - Ruling 1 removes the first. The second is not touched.
   - An annotation goes at item 21 (L3 reading file, line 30465), with the former wording kept. Row 21.102's proposed
     QUARANTINED is not changed.
7. **New downstream places found by the reads, each derived:**
   - **Ruling 57 clause (ii) and Ruling 62 item 11 (8A item 2): not reached.** Both rule about any reader outside the
     analysis. That reader is still D-522's display consumer (8A item 3), and a test-time second opinion is such a
     reader too. The words *"editing consumer"* in clause (ii) may allude to the in-product bridge **[the writing
     side's reading; the ruling's surface not read]**, but the rule does not depend on them. No correction.
   - **The DESIGN-INTENT seed list (8A item 5): no act now.** Its own ruling makes an amendment a recorded act of the
     framework phase when it consumes the list. Points 1 and 2 travel to that act as the reason.
   - **Membership of the specification document set (8A item 6): unchanged.** The derivation reads the document whole
     as a source. Its rows' dispositions rest on the derivation's statements (point 5).
   - **The four leak-check records (§3A item 2): unchanged**, as §3A item 2 already finds.

**For the user:** no point of §5 is left as a genuine choice by this test. Point 3 names an alternative that the user
may take instead of the derivation.

**What this test does not settle:** §3D's places not searched (`src/`, the `docs` sub-folders, `DECISIONS.md` beyond
the rows read); §7 item 3's folder-wide rulings search; family 7's re-test (entry 565 §3 step 5).

## 9. The check of §8 (coherence, completeness, correctness, overstatement)

Run in the sitting booted on entry 566, as a turn of its own, at the objects §8 names. **[checked]** at each object.

**Held at the objects.** The status-word table at `DECISIONS.md` lines 98–106, word for word. §6.20's row count, the
rulings at Rows 20.2 to 20.4 (Ruling 57), 20.7 to 20.9 (Ruling 51), 20.10 and 20.12 (Ruling 62), the manifest's
description at line 10142, Ruling 57 clause (ii) at lines 10216–10219, and Ruling 62 item 11's reliance on clause (ii)
and D-522 at lines 10375–10377. D-522's status LIVE and its whole text without a language model (lines 1000–1023). The
decision-surface record at lines 4192–4194 and 4901–4903. The rulings-sort record's line 42 and lines 32–33. The
step-zero-return record's lines 83–99. `OPEN_ITEMS.md` line 224 (OI-205). The statuses of D-440 to D-448 at §1A's table.
Ruling 1's words at §0.

**Corrections, each made at its site with the former wording kept (#12):**

1. **§8A item 1, coherence.** It said "the two that bear here" and listed three.
2. **§8A item 2, overstatement.** "Proposed dispositions only" claimed more than the reading file shows; a ruling
   elsewhere was not searched for.
3. **§8A item 4, overstatement of reach.** Ruling 57's own paragraph in the decision-surface record was not read; its
   ground is stated as far as the reading file's quotation and the record's facts paragraph show it.
4. **§8A item 5, correctness.** The phrase *"the framework phase's seed list"* is Ruling 1's, about the DESIGN-INTENT
   entries; the 24 are Ruling 2's placements, which join that total (line 51). Now said with the lines.
5. **§8B point 1, correctness.** It argued that LIVE "no longer fits", but none of the seven is LIVE: two are DEFERRED
   and five NOT STATED. NOT STATED is now argued at its own definition. **The derivation (SUPERSEDED BY Ruling 1) does
   not move.**
6. **§8B point 1, a relay unmarked.** The reading of the soft discard rests on §1B and §5, not on the residue-sitting
   record; now marked.
7. **§8B point 2, correctness.** It said D-444 and D-445 "stay LIVE"; both are NOT STATED (§1A). **The derivation (no
   change of status; a provenance note) does not move.**
8. **§8B points 4 and 5, relays unmarked.** The route ruling's quotation and the `ARCHITECTURE.md` line numbers are
   §3A's and §2B's; the 2026-09-22 rule is the user's instruction to Cowork, not a repository object. Each now marked.

**Coherence.** §8B points 1 and 2 agree with §1A's split (conflict in substance; conflict in stated consumer only).
Point 3 agrees with §2A's finding that §2.5 does not conflict. Point 5 agrees with §3B item 1's bearing. Point 7's
reading of Ruling 57 (ii) agrees with 8A items 2 and 3.

**Completeness, not closed by this check.** §3D and §7 item 3 stand. Not read: Ruling 57's paragraph in the
decision-surface record; the residue-sitting record; `docs/llm_integration.md` and `ARCHITECTURE.md` §19 beyond what §2
records. None of these is needed to state the derivations, since each derivation names its ground; any of them may be
read before the correction act if a dispatch step turns on it.

**What this check does not change.** No derivation of §8B moved. *Documentation only; algorithm: no change* stands.

---

*Provenance: Cowork, 2026-11-07 (Stockholm), the sitting booted on entry 564. The user's words: the opening instruction;
"shortened". The check (§7) and its corrections: Cowork, 2026-11-07 (Stockholm), the sitting booted on entry 565; the
user's words: the opening instruction; "shortened". §8 and its check (§9): Cowork, 2026-11-07 (Stockholm), the sitting
booted on entry 566; the user's words: the opening instruction; "shortened"; "continue".*
