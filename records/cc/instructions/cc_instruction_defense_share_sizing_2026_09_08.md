# CC INSTRUCTION — the defense-share sizing, 2026-09-08

**WHAT THIS IS.** A MEASUREMENT and a tracking act. It measures how much of `CLAUDE.md`'s six
session-start spans is DEFENSE material behind an explicit marker, and it tracks four files that are
on disk and outside git. **IT MOVES NO TEXT, EDITS `CLAUDE.md` NOT AT ALL, CREATES NO SATELLITE FILE,
CREATES NO OPEN-ITEMS ROW, WRITES NO DECISIONS-REGISTER ENTRY, AND ALLOCATES NO FINDING NUMBER.**

**WHY IT EXISTS.** The user ruled on 2026-09-08 (`cowork_rulings_2026_09_08_defense_satellite_sitting.md`,
Ruling 1) that a rule's DEFENSE may live in a satellite behind a pointer at the rule's home. Before
any text moves, measure-before-build (**D-277**) and the user's own 2026-08-22 direction — that the
surface be built from sizes MEASURED at the objects — require the size of the prize to be derived
rather than estimated. **Nothing in this dispatch acts on the ruling; it sizes it.**

**THE BASE.** Tip `d2ebe3cc98a33affdb5ffa2b8faf993bff6f0a71`. **Nothing is running.**

---

## PREMISES THIS SIDE DECLARES, AND WHICH OF THEM ARE ESTABLISHED

**ESTABLISHED, read at the objects by the writing side this session:**

1. `tools/audit/gen_session_start_read_size.py` carries `claude_md_reading(claude_md)`, which parses
   `CLAUDE.md`'s own membership block and returns the resolved spans, each carrying `lo`, `hi`
   (line indices, `hi` exclusive) and `kind` with the values `"session start"` and `"conditional"`.
   Read at that file, definition at `def claude_md_reading`, span construction at `def _resolve_span`.
2. The same file carries `def _paragraph_end(lines, at, hi)` returning the line after the last line
   of the paragraph containing `at`; a module-level `ITALIC` regex,
   `re.compile(r'(?<!\*)\*([^*"][^*]*?)\*(?!\*)')`, which matches an italic run and by its
   lookarounds does NOT match a `**bold**` run; a module-level `at_tree(path)` reading a file at the
   working tree; and `if __name__ == "__main__":` at its foot, so importing it executes no work.
   **It imports `use_utf8_output` from `output_encoding` after setting `sys.path`; the new tool does
   the same and CALLS it**, which is the standing remedy for the encoding departure.
2a. **`CLAUDE.md` carries no `**Why` bold form** — the writing side searched for one and found none —
   so an italic-only match loses nothing at this tree. **Re-establish that at the file; if a bold
   form has appeared, STOP and report rather than widening the pattern.**
3. `tools/audit/session_start_read_size.json` records the six session-start spans at **97,805**
   characters and the whole ordinary session-start read at **245,555**.
4. The marker openings listed in Task 1's table occur in `CLAUDE.md` at this tree; the writing side
   enumerated them at the file.

**DECLARED UNESTABLISHED — CHECK EACH AND REPORT THE ANSWER EITHER WAY. DO NOT ASSUME:**

5. **Whether a new tool must be enrolled in the guard runner's authored invocation list.** The record
   states a standing new-tool rule and a guard-runner STOP that a previous batch cleared by
   enrolling a tool in the act that added it. **Read the guard runner's own source and its invocation
   list, and answer whether this tool must be enrolled. If it must, enroll it in this batch. If it
   must not, say so with the ground read at the source.** This side did not open that source.
6. **Whether the five files named in Task 0(c) are in fact untracked at this tree.** Four were
   written this sitting and `cowork_memory_pointer_cut_2026_09_07.md` is RELAYED as untracked from
   the hundred-and-forty-seventh entry and was not checked by this side. **Establish it with the
   sanctioned enumeration tool; do not take it from this dispatch.**

---

## TASK 0 — the start state, and the tracking

**(a)** Run the sanctioned changed-paths enumeration over the whole tracked population and record it
at `tools/audit/changed_paths_defense_sizing_task0.json`. **Expected: zero tracked modifications**,
with the untracked files of (c) present among the untracked records. **A tracked modification is a
STOP — report it and do not proceed.**

**(b)** Run the full guard set and record its state. **Expected: the counts the preceding batch's
close recorded. Any departure is REPORTED, not corrected here.**

**(c)** Commit these FIVE files, which are on disk and outside git, in ONE commit, after (6) above is
established:

- `cowork_claude_md_live_rule_classification_2026_09_08.md`
- `ratification_surfaces/cowork_pruning_and_satellites_surface_2026_09_08.md`
- `cowork_rulings_2026_09_08_defense_satellite_sitting.md`
- `cowork_handoff_entry_one_hundred_and_forty_eight.md`
- `cowork_memory_pointer_cut_2026_09_07.md`

**Commit them VERBATIM. Do not edit, reformat, re-wrap or normalise any of them.** The ruling record
lands here under the standing clause that a sitting record lands at the next dispatch's Task 0, and
the handoff entry lands here for the same reason the preceding batch's Task 0 landed its own.
**If the enumeration at (a) shows a file of this list already tracked and unmodified, that file is
simply dropped from the commit and the fact reported — it is not a STOP.**

---

## TASK 1 — build `tools/audit/gen_defense_share.py`

**WHAT IT MEASURES.** For each of the six SESSION-START spans of `CLAUDE.md`, the characters standing
inside explicitly-marked defense clauses.

**HOW THE SPANS ARE OBTAINED — IMPORTED, NEVER REINVENTED (#6).** Import `claude_md_reading` from
`tools/audit/gen_session_start_read_size.py` and take the spans it resolves. **Do not re-parse the
membership block, do not re-locate a heading, and do not carry a line number for any span in this
tool's own source.** Take only the spans whose `kind` is `"session start"`. **If that yields other
than six spans, STOP.**

**THE AUTHORED MARKER TABLE.** These are the phrasings the file itself uses to open a recorded
defense. They are authored input, listed here so the authored half is checkable by reading one table,
and they are matched as they appear at the start of an italic run:

| Marker form | How it is matched |
|---|---|
| an italic run opening `Why` followed by a space or a colon | covers `*Why:*` and every `*Why <…>:*` variant |
| an italic run opening `Evidence:` | covers `*Evidence:*` |
| an italic run opening `Founding instance:` | covers `*Founding instance:*` |

**Matched by REUSING the imported `ITALIC` regex, never by a fresh pattern** — its lookarounds are
what keep a `**bold**` run out, and duplicating the pattern would put one concern in two places (#6).
**No other form is added on the strength of what a document might say.** Where the marker is preceded
by `**` bold emphasis on the same clause (`**★ ... .** *Why:* ...`), the measured extent begins at
the marker, not at the bold.

**THE EXTENT OF A MARKED CLAUSE, stated mechanically so it is not a judgment.** From the first
character of the marker through the end of the paragraph containing it, using the imported
`_paragraph_end`, bounded by the span's own `hi`. **A marked clause never extends past its span.**

**WHAT IS PUBLISHED**, at `tools/audit/defense_share.json`, every value computed and none
transcribed (**D-431**):

- per span: its name, its own character count, the number of marked clauses in it, and the characters
  those clauses hold;
- the totals across the six spans, and that total as a share of the six spans' own character count
  and as a share of the whole session-start read — **both denominators taken by re-deriving them
  through the imported reader at this same tree, never read out of the other artifact's JSON**;
- per clause: its span, its first and last line, its marker as matched, and its character count.

**THE ESTABLISHMENT, TAKEN POSITIVELY ON EVERY RUN (#19) — each of these is a STOP, not a reported
field:**

- every measured clause lies wholly inside the span it is attributed to;
- no two measured clauses overlap;
- the sum of a span's clause characters does not exceed that span's own character count;
- the six spans' re-derived total equals the total the reader gives for them;
- `--check` re-derives the artifact and compares rendered text.

**THE BOUND, DECLARED ON THE ARTIFACT ITSELF (D-673).** The artifact states, in its own opening
fields, that **the marker set's reach is UNMEASURED**: a defense written without one of these markers
is not counted, and the record demonstrably carries such defenses. **Two examples, both
located at the file by the writing side and both to be RE-LOCATED by you before they are named in
the artifact:** the plain (non-italic) clause opening *"Founding instances of the gap:"* in the
Conventions span — **note that it WRAPS across two lines, so a single-line search for the whole
phrase fails, which is how the writing side first missed it** — and the italic parenthetical opening
*"(This defense is stated as a DESCRIPTION rather than by line number"* in the decisions-register
span, which the imported `ITALIC` matches as an italic run but which the marker table does not admit.
**If either cannot be re-located, say so and name only the one you found.** **The published figure is
therefore a LOWER BOUND on the defense material in the six spans, and the artifact says so in those
words.** D-673 admits this because no analysis decision consumes
the figure: it sizes a restructure and nothing else.

**WHAT THE ARTIFACT MUST NOT CLAIM**, stated so it is not written by accident: that any marked clause
is movable; that any unmarked passage is not a defense; that the classification of
`cowork_claude_md_live_rule_classification_2026_09_08.md` was consumed here — **it was not, this
measurement is independent of it**; or that the figure is what a satellite would remove, since what
moves is a later authored decision.

---

## TASK 2 — the close

**(a)** Write this batch's `STATUS.md` entries, per the OI-222 pointer convention, restating no
figure (**D-431**).

**(b)** Perform the forward bound on `STATUS.md`: re-aim `tools/audit/gen_status_batch_bound.py` at
this batch, **this batch's own entries written FIRST and `--apply` run second**, appending to the
previous aimings rather than replacing them.

**(c)** Regenerate `tools/audit/session_start_read_size.json`, because `STATUS.md` is a member of the
read it measures and this batch moves it. **No measured value is adjusted to reach a number.**

**(d)** Run the standing self-check: re-read the actual diff of every touched file against the
guiding principles, the conventions and `DEFECT_TYPES.md`, and report every violation found.

**(e)** Write `cc_report_defense_share_sizing_2026_09_08.md` at the repository root: the commit table,
what each task did, every declared premise's answer including (5) and (6), the measured figures by
citation to the artifact rather than by transcription, and every reading you took that this dispatch
did not order.

---

## STOP CONDITIONS

- Any tracked modification at Task 0(a).
- `claude_md_reading` yielding other than six session-start spans.
- Any of the four establishment checks in Task 1 failing.
- The guard set departing from its recorded start state in a way this batch's own ordered acts do not
  explain — **report, do not correct.**
- Any instruction here that you find to be false at the objects. **A premise of this dispatch that
  does not hold is a STOP and a report, never something to work around.**

## WHAT THIS BATCH MAY NOT DO

No edit to `CLAUDE.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md` or any ruling record. No
satellite file. No text moved from anywhere to anywhere. No open-items row created, flipped or
discarded. No decisions-register entry, no `D-NNN` allocated, no finding number. No `src/` change, no
build, no test, no golden, no corpus, nothing under `tools/robust_stop/` or `tools/corpus/`. No paper
opened, no extract, no sweep, no verdict moved, no gate lifted.
