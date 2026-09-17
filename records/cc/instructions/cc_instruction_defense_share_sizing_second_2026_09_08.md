# CC INSTRUCTION — the defense-share sizing, SECOND ISSUE, 2026-09-08

**THIS SUPERSEDES `cc_instruction_defense_share_sizing_2026_09_08.md`, WHICH STOPPED AT ITS TASK 0(a)
AND IS NOT TO BE RUN AGAIN.** That dispatch's Task 0(a) expected zero tracked modifications. **The
expectation was FALSE at the objects and the error was the writing side's**, not the batch's: the
batch stopped exactly as instructed, established the finding at the git object rather than at the
status code, and answered both declared-unestablished premises anyway. Its report
`cc_report_defense_share_sizing_2026_09_08.md` was read in FULL by the writing side and every claim in
it was re-verified at the objects before this dispatch was written. **Nothing in it was taken on
trust and nothing in it was found wrong.**

**WHAT THIS IS.** A MEASUREMENT and a tracking act, unchanged in purpose. It measures how much of
`CLAUDE.md`'s six session-start spans is DEFENSE material behind an explicit marker, and it commits
the files this arc has left on disk. **IT MOVES NO TEXT, EDITS `CLAUDE.md` NOT AT ALL, CREATES NO
SATELLITE FILE, CREATES NO OPEN-ITEMS ROW, WRITES NO DECISIONS-REGISTER ENTRY, AND ALLOCATES NO
FINDING NUMBER.**

**WHY IT EXISTS.** The user ruled on 2026-09-08
(`cowork_rulings_2026_09_08_defense_satellite_sitting.md`, Ruling 1) that a rule's DEFENSE may live in
a satellite behind a pointer at the rule's home. Measure-before-build (**D-277**) and the user's own
2026-08-22 direction — that the surface be built from sizes MEASURED at the objects — require the size
of the prize derived rather than estimated. **Nothing here acts on the ruling; it sizes it.**

**THE BASE.** Tip `d2ebe3cc98a33affdb5ffa2b8faf993bff6f0a71`, read at `.git/refs/heads/master` with
the file tools by the writing side after the stopped batch, and unmoved — **that batch committed
nothing.**

---

## WHAT CHANGED FROM THE FIRST ISSUE, AND WHY

**(1) The Task 0(a) expectation is corrected.** ONE tracked modification is expected, named below with
its ground. It is `cowork_handoff_entry_one_hundred_and_forty_seven.md`, and the cause is structural
rather than an incident: **that entry was committed by its own batch's Task 0 partway through the
batch, and was then amended later in the same sitting when the batch returned** — its own declared
departure (xiii) states the amendment in its own words. So the committed blob is the pre-amendment
text and the working tree carries the amended one. **Verified at the objects by the writing side, by
explicit hash and not by a status code:** the committed blob at the declared base is 24,749 bytes and
the working-tree copy is 29,827.

**This will recur, and the next dispatch's author should expect it rather than rediscover it:** any
handoff entry committed by a batch and amended afterwards in the same sitting appears as a tracked
modification at the next batch's Task 0.

**(2) The commit list grows from five files to nine, and it now includes the amended entry.** The
first issue's own report, its ordered artifact and the superseded dispatch are on disk untracked and
belong in the record of what happened.

**(3) Task 1 gains a SECOND enrolment the first issue did not name.** The stopped batch found it by
reading and reported it rather than absorbing it, and **the writing side re-verified it at both
sources**: `tools/audit/gen_guard_classification.py` draws its population from
`gen_guard_state.AUTHORED` and declares as the first of its three STOPs that *"a tool in the
guard-state population with NO authored verdict is a STOP"*. **Enrolling in one table alone moves the
STOP instead of clearing it.**

---

## PREMISES — WHAT IS NOW ESTABLISHED, AND BY WHOM

**ESTABLISHED, read at the objects. None of these needs re-checking, and each names where it was
read:**

1. `tools/audit/gen_session_start_read_size.py` carries `claude_md_reading(claude_md)`, which parses
   `CLAUDE.md`'s own membership block and returns the resolved spans, each with `lo`, `hi` (line
   indices, `hi` exclusive) and `kind` taking the values `"session start"` and `"conditional"`; and
   `_paragraph_end(lines, at, hi)`; and a module-level `ITALIC` regex
   `re.compile(r'(?<!\*)\*([^*"][^*]*?)\*(?!\*)')` whose lookarounds keep a `**bold**` run out; and
   `at_tree(path)`; and `if __name__ == "__main__":` at its foot, so importing executes no work. It
   imports `use_utf8_output` from `output_encoding` after setting `sys.path`. *(Writing side, at that
   file.)*
2. `tools/audit/session_start_read_size.json` records the six session-start spans at **97,805**
   characters and the whole ordinary session-start read at **245,555**. *(Writing side, at that
   artifact.)*
3. **A new tool built to Task 1's specification MUST be enrolled in `tools/audit/gen_guard_state.py`'s
   `AUTHORED` table.** `MODE_TOKEN = re.compile(r"--(check|verify|establish)\b")`; `candidates()`
   admits every `tools/audit/*.py` whose source matches it, so a tool carrying `--check` enters the
   derived population by construction; `main()` computes
   `unclassified = sorted(p for p in derived if p not in authored_paths)` and a non-empty result
   prints `STOP: derived candidate(s) with no authored invocation` and returns 1. **That table's own
   comments state the standing new-tool rule repeatedly — a tool is classified "in the act that
   creates it rather than reaching a later pass's derived population unclassified".** *(Stopped batch,
   re-verified by the writing side at that source.)*
4. **AND IT MUST ALSO CARRY AN AUTHORED VERDICT IN `tools/audit/gen_guard_classification.py`**, whose
   population is taken from `gen_guard_state.AUTHORED` "so the two cannot disagree" and whose first
   declared STOP is a tool in that population with no authored verdict. *(Stopped batch, re-verified
   by the writing side at that source.)*
5. **All five files of the first issue's Task 0(c) are untracked**, established by the stopped batch
   with the sanctioned enumeration tool and visible at
   `tools/audit/changed_paths_defense_sizing_task0.json`, including
   `cowork_memory_pointer_cut_2026_09_07.md`, which had only been relayed. **That artifact carries
   exactly one record whose code is not the untracked one.** *(Stopped batch, re-verified by the
   writing side at that artifact.)*
6. `CLAUDE.md` carries no `**Why` bold form at this tree. *(Writing side, at that file.)*

**DECLARED UNESTABLISHED — check and report either way:**

7. **Whether any tracked modification other than the one named in Task 0(a) exists at the tree you
   actually run on.** The enumeration above was taken by the stopped batch; the tree may have moved
   since. **Re-run it; do not carry its result.**

---

## TASK 0 — the start state, and the tracking

**(a)** Run the sanctioned changed-paths enumeration over the whole tracked population and record it
at `tools/audit/changed_paths_defense_sizing_second_task0.json`.

**EXPECTED: EXACTLY ONE tracked modification —
`cowork_handoff_entry_one_hundred_and_forty_seven.md`, on the ground stated above — and no other.**
**Any other tracked modification, and any deletion or rename, is a STOP: report it and do not
proceed.** **Establish the one expected modification at the object as the stopped batch did — fetch
the committed text at the declared base by explicit hash — and STOP if the working-tree copy differs
from it in any way the amendment its own departure (xiii) declares does not account for.**

**(b)** Run the full guard set and record its state. **This is the START state, taken BEFORE the new
tool exists.** Any departure from the state the preceding batch's close recorded is **REPORTED, not
corrected here.**

**(c)** Commit these NINE paths in ONE commit:

- `cowork_handoff_entry_one_hundred_and_forty_seven.md` — **the amended entry; this is the tracked
  modification of (a), and committing it is an ORDERED act, named here with its ground, not a silent
  one**
- `cowork_claude_md_live_rule_classification_2026_09_08.md`
- `ratification_surfaces/cowork_pruning_and_satellites_surface_2026_09_08.md`
- `cowork_rulings_2026_09_08_defense_satellite_sitting.md`
- `cowork_handoff_entry_one_hundred_and_forty_eight.md`
- `cowork_memory_pointer_cut_2026_09_07.md`
- `cc_instruction_defense_share_sizing_2026_09_08.md` — the superseded first issue
- `cc_report_defense_share_sizing_2026_09_08.md` — its STOP report
- `tools/audit/changed_paths_defense_sizing_task0.json` — its ordered artifact

**Plus this dispatch itself and the artifact of (a), on the standing pattern that a batch commits the
instruction it runs.** **Commit every one VERBATIM — do not edit, reformat, re-wrap or normalise any
of them**, the ruling record landing here under the standing clause that a sitting record lands at the
next dispatch's Task 0. **If (a) shows any of these already tracked and unmodified, drop that one from
the commit and report it; that is not a STOP.**

---

## TASK 1 — build `tools/audit/gen_defense_share.py`, and enrol it in BOTH tables

**WHAT IT MEASURES.** For each of the six SESSION-START spans of `CLAUDE.md`, the characters standing
inside explicitly-marked defense clauses.

**HOW THE SPANS ARE OBTAINED — IMPORTED, NEVER REINVENTED (#6).** Import `claude_md_reading` from
`tools/audit/gen_session_start_read_size.py` and take the spans it resolves, with the same `sys.path`
handling that file uses, and **call `use_utf8_output`** — the standing remedy for the encoding
departure. **Do not re-parse the membership block, do not re-locate a heading, and do not carry a line
number for any span in this tool's own source.** Take only the spans whose `kind` is
`"session start"`. **If that yields other than six spans, STOP.**

**THE AUTHORED MARKER TABLE.** These are the phrasings the file itself uses to open a recorded
defense, matched by REUSING the imported `ITALIC` regex and never by a fresh pattern:

| Marker form | How it is matched |
|---|---|
| an italic run opening `Why` followed by a space or a colon | covers `*Why:*` and every `*Why <…>:*` variant |
| an italic run opening `Evidence:` | covers `*Evidence:*` |
| an italic run opening `Founding instance:` | covers `*Founding instance:*` |

**No other form is added on the strength of what a document might say.** Where the marker is preceded
by `**` bold emphasis on the same clause, the measured extent begins at the marker, not at the bold.

**THE EXTENT OF A MARKED CLAUSE, stated mechanically so it is not a judgment.** From the first
character of the marker through the end of the paragraph containing it, using the imported
`_paragraph_end`, bounded by the span's own `hi`. A marked clause never extends past its span.

**WHAT IS PUBLISHED**, at `tools/audit/defense_share.json`, every value computed and none transcribed
(**D-431**): per span, its name, its own character count, the number of marked clauses and the
characters they hold; the totals across the six spans, as a share of those spans and as a share of the
whole session-start read, **both denominators re-derived through the imported reader at this same
tree and never read out of the other artifact's JSON**; and per clause, its span, first and last line,
matched marker and character count.

**THE ESTABLISHMENT, TAKEN POSITIVELY ON EVERY RUN (#19) — each a STOP, not a reported field:** every
measured clause lies wholly inside the span it is attributed to; no two overlap; a span's clause
characters do not exceed that span's own count; the six spans' re-derived total equals the reader's;
and `--check` re-derives the artifact and compares rendered text.

**THE BOUND, DECLARED ON THE ARTIFACT ITSELF (D-673).** The artifact states in its own opening fields
that **the marker set's reach is UNMEASURED**: a defense written without one of these markers is not
counted, and the record demonstrably carries such defenses. **Two examples, both to be RE-LOCATED by
you before they are named in the artifact:** the plain non-italic clause opening *"Founding instances
of the gap:"* in the Conventions span — **it WRAPS across two lines, so a single-line search for the
whole phrase fails, which is how the writing side first missed it** — and the italic parenthetical
opening *"(This defense is stated as a DESCRIPTION rather than by line number"* in the
decisions-register span, which `ITALIC` matches as an italic run but which the marker table does not
admit. **If either cannot be re-located, say so and name only the one you found.** **The published
figure is a LOWER BOUND on the defense material in the six spans, and the artifact says so in those
words.**

**THE TWO ENROLMENTS, IN THE SAME COMMIT AS THE TOOL.** An `AUTHORED` entry in
`tools/audit/gen_guard_state.py` naming this tool and its invocation, and a verdict for it in
`tools/audit/gen_guard_classification.py`. **Neither table may be left for a later act.**

**THE GENERATED CONSEQUENCES OF THIS BATCH'S OWN ORDERED ACTS, NAMED HERE because a dispatch's file
list must name them:** `tools/audit/guard_state.json` and `tools/audit/guard_classification.json`
change when the two tables gain an entry. **Regenerate both and commit them with the tool.**

**WHAT THE ARTIFACT MUST NOT CLAIM:** that any marked clause is movable; that any unmarked passage is
not a defense; that `cowork_claude_md_live_rule_classification_2026_09_08.md` was consumed here — **it
was not, this measurement is independent of it**; or that the figure is what a satellite would remove,
since what moves is a later authored decision.

---

## TASK 2 — the close

**(a)** Write this batch's `STATUS.md` entries per the OI-222 pointer convention, restating no figure
(**D-431**).

**(b)** Perform the forward bound on `STATUS.md`: re-aim `tools/audit/gen_status_batch_bound.py` at
this batch, **this batch's own entries written FIRST and `--apply` run second**, appending to the
previous aimings rather than replacing them.

**(c)** Regenerate `tools/audit/session_start_read_size.json`, because `STATUS.md` is a member of the
read it measures and this batch moves it. **No measured value is adjusted to reach a number.**

**(d)** Re-run the FULL guard set at the closing tree and report it against the start state of Task
0(b), **with the new tool's membership expected and every other departure traced to this batch's own
ordered acts or REPORTED.**

**(e)** Run the standing self-check: re-read the actual diff of every touched file against the guiding
principles, the conventions and `DEFECT_TYPES.md`, and report every violation found.

**(f)** Write `cc_report_defense_share_sizing_second_2026_09_08.md` at the repository root: the commit
table, what each task did, premise (7)'s answer, the measured figures BY CITATION to the artifact
rather than by transcription, and every reading you took that this dispatch did not order.

---

## STOP CONDITIONS

- Any tracked modification at Task 0(a) other than the one named, or any deletion or rename.
- The expected modification differing from the committed blob in a way departure (xiii) does not
  account for.
- `claude_md_reading` yielding other than six session-start spans.
- Any of the establishment checks in Task 1 failing.
- The guard set departing from its recorded start state in a way this batch's own ordered acts do not
  explain — **report, do not correct.**
- Any instruction here found false at the objects. **A premise that does not hold is a STOP and a
  report, never something to work around.** *(The first issue failed exactly here, and the batch was
  right to stop.)*

## WHAT THIS BATCH MAY NOT DO

No edit to `CLAUDE.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md` or any ruling record. No
satellite file. No text moved from anywhere to anywhere. No open-items row created, flipped or
discarded. No decisions-register entry, no `D-NNN` allocated, no finding number. No `src/` change, no
build, no test, no golden, no corpus, nothing under `tools/robust_stop/` or `tools/corpus/`. No paper
opened, no extract, no sweep, no verdict moved, no gate lifted.
