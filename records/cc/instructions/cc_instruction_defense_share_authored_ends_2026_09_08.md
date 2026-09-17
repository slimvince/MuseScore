# CC INSTRUCTION — the defense-share measurement's clause ENDS become AUTHORED, 2026-09-08

**THE BASE.** Tip `cdd7ff4aca948156291725c76535bedfd84d9be5`.

**WHY THIS EXISTS, IN ONE PARAGRAPH.** `tools/audit/gen_defense_share.py` ends a marked defense clause at *the end of the paragraph containing it*, using the imported `_paragraph_end`, **which walks forward only until a BLANK LINE.** In `CLAUDE.md` the guiding principles are one numbered list with no blank lines between items and the two register sections are single unbroken blocks, **so a marked clause runs from its marker to the next marker and swallows every rule standing between them.** Twenty-four of the thirty-four clauses over-run that way and thirteen carry at least one whole live rule. **The published value is therefore not a LOWER BOUND on defense material, as its own artifact declares, and not a bound in either direction.** This dispatch replaces the mechanical end with an AUTHORED one, read at the file marker by marker.

**THIS IS A MEASUREMENT-DEFINITION REPAIR AND NOTHING ELSE.** No text moves out of `CLAUDE.md`, no satellite is created, and `CLAUDE.md` is not edited. **The measured value WILL move, downward, and that is the point of the act rather than a regression** — the previous value measured the wrong thing.

**★ THIS DISPATCH WAS FACT-CHECKED AT THE OBJECTS BEFORE IT WAS WRITTEN.** Read for it: `tools/audit/gen_defense_share.py` **whole**; `tools/audit/gen_session_start_read_size.py` at `claude_md_reading`, `_paragraph_end`, `ITALIC`, `BOLD` and `at_tree`; `tools/audit/defense_share.json` whole; `tools/audit/guard_state.json` at its counts; `STATUS.md` whole; `.git/refs/heads/master`; and `CLAUDE.md` at every one of the thirty-four clause regions. **All thirty-four end anchors below were verified present and locatable exactly once. THREE OF THEM WRAP ACROSS A LINE BREAK** — anchors 2, 17 and 30 — **which is why §2 requires whitespace-flexible compilation and why a plain single-line search for them finds nothing.**

---

## PREMISES

**ESTABLISHED, each read at the object named:**

1. `gen_defense_share.py` finds clauses in `clauses_in()`, setting `_ends` and `_paragraph_ends` from `reader._paragraph_end(lines, start_line, hi)`; `close_at_the_next_clause()` then truncates `_ends` where a later clause opens inside an earlier one, and sets `characters`, `last_line`, `it_was_closed_at_the_next_marked_clause` and `characters_had_it_run_to_the_paragraph_end`. **Both functions are in that one file and nothing else computes an extent.**
2. `reader._paragraph_end(lines, at, hi)` advances while `lines[end].strip() != ""` — **a blank line and nothing else ends a paragraph for it.**
3. The tool already imports `reader.ITALIC`, `reader.BOLD`, `reader.at_tree` and `reader.claude_md_reading(claude_md, with_coordinates=True)`, and takes both denominators through the reader. **None of that changes here.**
4. The tool is ALREADY enrolled: an invocation `["--check"]` in `tools/audit/gen_guard_state.py` and a `LIVE` verdict in `tools/audit/gen_guard_classification.py`. **No new enrolment is owed. Do not add one.**
5. `tools/audit/guard_classification.json` **cannot be regenerated at this tree** — that tool STOPs on `gen_l0_l1_outgoing_population.py` and `gen_withheld_family_reading.py`, neither of which is ours. **Pre-existing and already standing with the user. REPORT IT, do not correct it, and do not author a verdict for either.**
6. The user ruled on 2026-09-08 that a marked clause ends at its paragraph end **or the next marked clause, whichever comes first** — `cowork_rulings_2026_09_08_extent_rule_sitting.md`. **That ruling stands and is not re-opened here.** It settled a double-counting question between two readings; **this act replaces the paragraph unit both of those readings rested on**, which the ruling record does not reach and does not forbid.

**DECLARED UNESTABLISHED — check and report either way:**

7. Whether any tracked modification exists at the tree you run on. **EXPECTED: ZERO.** The hundred-and-forty-ninth entry was committed by the previous batch and never amended; this sitting's three files are UNTRACKED. **Re-run the enumeration; carry no earlier result. Any tracked modification is a STOP.**
8. Whether the guard set still stands at 81 run, 66 passing, 15 failing, 4 not run, 16 historical, with the failing set unchanged member for member. **Any departure is REPORTED, not corrected.**

---

## TASK 0 — the start state

**(a)** Run the sanctioned changed-paths enumeration over the whole tracked population and record it at `tools/audit/changed_paths_defense_authored_ends_task0.json`. **EXPECTED: ZERO tracked modifications, no deletion, no rename.** Any tracked modification is a STOP.

**(b)** Run the full guard set with `--check` and **not bare**, for the standing reason: a bare run rewrites the committed `tools/audit/guard_state.json` and folds the tree's current state into a committed record before this batch's own commit. Record the state; report any departure from premise 8.

**(c)** Commit, in ONE commit, and **verbatim — edit, reformat, re-wrap and normalise nothing**: this dispatch; the artifact of (a); `cowork_handoff_entry_one_hundred_and_fifty.md`; `cowork_rulings_2026_09_08_extent_rule_sitting.md`; and `cowork_defense_clause_ends_2026_09_08.md`. **Five paths. If any is absent at your tree, STOP and report rather than committing four.**

---

## TASK 1 — the authored ends

### 1.1 What replaces what

`clauses_in()` keeps finding clauses exactly as it does — same imported patterns, same marker table, same emphasis handling. **What changes is only where each found clause ENDS.**

- **The paragraph end stops being the measurement.** It is computed still, and published still, as a comparison column only.
- **`close_at_the_next_clause()` is KEPT and is no longer the measurement either.** Run it over a COPY of the extents so that its result is published as the second comparison column — the reading the 2026-09-08 ruling settled — and nothing is lost (#12).
- **The measurement becomes: from the first character of the marker through the end of that clause's AUTHORED END ANCHOR.**

### 1.2 How an anchor is compiled — and why it is not a plain search

Each anchor is a phrase of `CLAUDE.md`'s own text. **Compile it by splitting on whitespace, `re.escape`-ing each word, and joining the words with `\s+`.** Two reasons, both established:

- **Three of the anchors WRAP across a line break** (2, 17 and 30). A single-line search for them finds nothing. **This arc has now made that mistake four times; the tool already uses exactly this technique for `KNOWN_MISS` and this reuses it (#6).**
- Several anchors contain regex-special characters — parentheses in 18 and 33, a backtick in 17. **Escaping is not optional.**

### 1.3 The AUTHORED table, verbatim

Thirty-four anchors, in file order, one per marked clause. **Each is the last words of that clause's defense.**

| # | Span | End anchor |
|---|---|---|
| 1 | Guiding principles | `which is the defect the catalog names DT-2.` |
| 2 | Guiding principles | `would confound a structural verdict with a weighting one.` |
| 3 | Guiding principles | `however convenient the invariant they share.` |
| 4 | Guiding principles | `would go on reading as work outstanding rather than as an answer.` |
| 5 | Guiding principles | `the condition under which that route is finished.` |
| 6 | Guiding principles | `which is exactly what D-474 exists to prevent.` |
| 7 | Guiding principles | `they bind on the reading of the literature rather than on the ledger.` |
| 8 | The open-items register | `the establishment being the thing that made the narrower pointer admissible at all.` |
| 9 | The open-items register | `#19 exists because a thing merely unfalsified is not established.` |
| 10 | The open-items register | `the cost of the error in the other direction is bounded by the default above.` |
| 11 | The open-items register | `so a false resolution propagates mechanically.` |
| 12 | The open-items register | `forbidding the mark in prose, which is one symptom of three.` |
| 13 | The open-items register | `and answers the objection rather than overriding it.` |
| 14 | The decisions register | `it was never ruled to require every delegation to name sections.` |
| 15 | The decisions register | `each of which produced the evidence locating its own error.` |
| 16 | The decisions register | `and a status banner does not change that.` |
| 17 | The decisions register | ``The distinction is `ARCHITECTURE.md`'s own, not a preference.`` |
| 18 | The decisions register | `what keeps (i) a mechanical test rather than one with a case-by-case exception.` |
| 19 | The decisions register | `and an ellipsis by anything at all.` |
| 20 | The decisions register | `without the register standing in for the specification.` |
| 21 | The decisions register | `which is what shows it is real rather than notional.` |
| 22 | The decisions register | `what the mechanism's own output already carries, which is what #6 forbids.` |
| 23 | The decisions register | `already carried at the table the adoption happened in.` |
| 24 | The decisions register | `the rule the verdict bears on is elsewhere and is unmoved by it.` |
| 25 | Conventions | `which is the general case, not the exception.` |
| 26 | Conventions | `the reader who meets the term at its fiftieth use never meets the introduction site.` |
| 27 | Conventions | `a single tree-wide pass would take every one of those decisions silently and at once.` |
| 28 | Conventions | `already forbids citing code by line number in the first place.` |
| 29 | Conventions | `and from probes, not from apparatus repair.` |
| 30 | Conventions | `buys no protection and spends the time the fix plan is owed.` |
| 31 | Conventions | `ratifications were re-presented and re-confirmed.` |
| 32 | Conventions | `erroring loudly rather than returning silently-wrong content.` |
| 33 | Conventions | `and it operationalizes principle #5 (investigate when facts may be scarce).` |
| 34 | Conventions | `the fifty-ninth performed it and counted one.` |

**The span column is authored context for a reader and MUST be checked, not trusted: an anchor resolving inside a different span than the one named here is a STOP.**

### 1.4 The STOPs this table earns — every one an establishment, none a reported field

- **The number of anchors must equal the number of clauses found.** A marker added to or removed from `CLAUDE.md` invalidates an authored table, and the table must then be re-authored by the writing side, never patched by a batch. **A mismatch is a STOP naming both counts.**
- **Each anchor must be locatable EXACTLY ONCE inside its own clause's span.** Zero or more than one is a STOP naming the anchor.
- **Anchor *i* must begin at or after clause *i*'s marker start** and **must end at or before clause *i*'s paragraph end**. Either violated is a STOP.
- **Anchor *i* must end strictly before clause *i+1*'s marker begins.** A STOP otherwise.
- **The anchors must resolve in strictly increasing file order.** A STOP otherwise.
- **The span each anchor resolves inside must be the span this table names for it.** A STOP otherwise.
- **Every existing STOP in the tool stays in force**, including the six-span check, the dead-row check, the clause-inside-its-span check, the no-overlap check, the per-span-not-exceeded check, the total-equals-the-reader's check, the known-miss check and `--check`.

### 1.5 What is published per clause, after this

Per clause, three lengths and never fewer (#12): **`characters`** — the authored measurement; **`characters_had_it_been_closed_at_the_next_marked_clause`** — the reading the 2026-09-08 ruling settled; and **`characters_had_it_run_to_its_paragraph_end`** — the literal reading of the original dispatch. Plus the anchor as written and the line it resolves on. **The per-span and total columns carry the same three.**

### 1.6 The bound wording, which is false as it stands and must be corrected in this act

The artifact declares the value a **LOWER BOUND on defense material**. That is false of the value it currently publishes, because the extents carry live rule text. **Rewrite that block to say, in the artifact's own voice and computed where a value is involved:**

- that the value **is** now a lower bound on marked defense material, the marker set's reach being UNMEASURED, so a defense written without one of the three markers is not counted;
- **that it was NOT a bound in either direction before this act**, the paragraph unit having carried live rule text into the extents, and that the correction is recorded rather than the old wording quietly replaced (#12);
- that the ends are **AUTHORED**, published in `cowork_defense_clause_ends_2026_09_08.md`, and challengeable at their anchor;
- **and that the classification `cowork_claude_md_live_rule_classification_2026_09_08.md` is STILL not consumed** — it is not read by this tool.

### 1.7 The module docstring

Amend it to state the authored-end definition, the compilation rule and its two reasons, and the anchor STOPs. **The declared-departure block about the closing rule is REPLACED by a pointer to `cowork_rulings_2026_09_08_extent_rule_sitting.md`, which ruled it** — the departure is no longer outstanding and the docstring must not go on saying it is. **Carry no line number into the docstring** (**D-307**); this arc has already had to repair one for that reason.

---

## TASK 2 — re-banner the spent dispatch, and do not rewrite it

`cc_instruction_defense_share_sizing_third_2026_09_08.md` has run and is committed. **Under D-674 a dated instruction the record has overtaken is RE-BANNERED and never rewritten**: its body stands exactly as the batch executed it. **Add a banner at its head only**, recording that its extent sentence was defective as written; that the executing batch declared and resolved the conflict; that the resolution was ruled on 2026-09-08; and that the paragraph unit both readings rested on was replaced by this dispatch. **Change no other character of that file.**

---

## TASK 3 — the close

**(a)** `STATUS.md` entries for this batch, per the OI-222 pointer convention, restating no value (**D-431**).

**(b)** The forward bound ONCE: re-aim `tools/audit/gen_status_batch_bound.py` at this batch, **this batch's own entries written FIRST and `--apply` run second**, appending to the previous aimings rather than replacing them (#12). **Write no count of entries into the re-aiming comment** — the previous batch wrote four where five moved, and a comment asserting a count the tool's own run contradicts is the defect #10 forbids.

**(c)** **REGENERATE IN THIS ORDER AND STATE THAT YOU DID:** first `tools/audit/session_start_read_size.json`, because (a) and (b) move `STATUS.md`, a member of the read it measures; **then `tools/audit/defense_share.json`, because it re-derives the whole-read denominator through that same reader and would otherwise go stale the moment `STATUS.md` moves.** The previous batch met this and it is named here so it is not rediscovered. **No measured value is adjusted to reach a number.**

**(d)** Re-run the FULL guard set with `--check` at the closing tree and report it against Task 0(b). **The defense-share member's captured output moves by construction; every other departure is traced to this batch's own ordered acts or REPORTED.**

**(e)** The standing self-check: re-read the actual diff of every touched file against the guiding principles, the conventions and `DEFECT_TYPES.md`; report every violation found. **Scan your own new text for reserved-word breaches before reporting** — the previous batch shipped eight.

**(f)** Write `cc_report_defense_share_authored_ends_2026_09_08.md`: the commit table, what each task did, premises 7 and 8 answered, **the measured values BY CITATION to the artifact and never by transcription**, the movement against the previous measurement stated as a movement and not as a correction of a number, and every reading taken that this dispatch did not order. **Assert no count of your own acts anywhere in it; name the members.**

---

## STOP CONDITIONS

- Any tracked modification at Task 0(a); any deletion or rename.
- Any of the five Task 0(c) paths absent.
- The anchor count not equalling the clause count.
- Any anchor not locatable exactly once inside its clause's own span.
- Any anchor before its own marker, after its own paragraph end, at or after the next marker, out of file order, or in a span other than the one the table names.
- Any pre-existing STOP in the tool firing.
- The guard set departing from its start state in a way this batch's own acts do not explain — **report, do not correct.**
- **Any instruction here found false at the objects. A premise that does not hold is a STOP and a report, never something to work around.**

## WHAT THIS BATCH MAY NOT DO

No edit to `CLAUDE.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md`, any ruling record, or `cowork_defense_clause_ends_2026_09_08.md`. **No change to the marker table, to the span source, to the denominators, or to which clauses are found.** No satellite file. No text moved out of any governing document. No open-items row created, flipped or discarded. No decisions-register entry, no `D-NNN`, no finding number. No `src/` change, no build, no test, no golden, no corpus, nothing under `tools/robust_stop/` or `tools/corpus/`. No paper opened, no extract, no sweep, no verdict moved, no gate lifted. **No new guard enrolment — the tool is already enrolled. No verdict authored for the two unclassified guard-set members. And no hunt for anything the guard set reports.**
