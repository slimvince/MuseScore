# CC INSTRUCTION — the defense-share sizing, THIRD ISSUE, 2026-09-08

> **★ RE-BANNERED 2026-09-09, AND NOT REWRITTEN — THIS DISPATCH HAS RUN AND IS COMMITTED, AND ITS
> BODY BELOW STANDS EXACTLY AS THE EXECUTING BATCH RAN AGAINST IT (`D-674`).** The banner is added
> at the head; not one other character of this file is changed. Rewriting the body would falsify
> what that batch actually executed.
>
> **WHAT WAS DEFECTIVE, IN ONE SENTENCE.** §2's extent sentence fixed a marked clause's reach as
> *"From the first character of the marker through the end of the paragraph containing it"* and, in
> the same task, made two establishment STOPs — that no two clauses overlap, and that a span's
> clause characters do not exceed that span's own count. **At the tree it ran on, those could not
> all hold**, because `CLAUDE.md` routinely writes two marked defenses inside one paragraph, so
> under the literal wording both run to that paragraph's end and overlap.
>
> **THE EXECUTING BATCH DECLARED THE CONFLICT AND RESOLVED IT, AND DID NOT TAKE IT SILENTLY.** It
> measured the conflict before deciding anything, closed a clause at the next marked one where one
> opens before the paragraph ends, published both readings per clause (#12), and declared the
> departure at the tool, on the artifact, in `STATUS.md` and in its report.
>
> **THE RESOLUTION WAS RULED ON 2026-09-08** — `cowork_rulings_2026_09_08_extent_rule_sitting.md`,
> §1: the closing rule IS the definition, and the literal wording above is a drafting defect in a
> bar the writing side wrote, corrected rather than ratified.
>
> **AND THE PARAGRAPH UNIT BOTH READINGS WERE BUILT ON HAS SINCE BEEN REPLACED**, by
> `cc_instruction_defense_share_authored_ends_2026_09_08.md`, which the ruling record does not reach
> and does not forbid: the imported paragraph-end function walks forward only until a blank line,
> and `CLAUDE.md` carries no blank line between its numbered principles and none inside its sections
> for the open-items register and for the decisions register, so an extent ran from its marker to
> the next marker and carried live rule text.
> The measurement now ends each clause at an AUTHORED anchor, published in
> `cowork_defense_clause_ends_2026_09_08.md`, and keeps both earlier readings as comparison columns.
> **The measured value moved DOWNWARD, which is the point of that act and not a regression against
> this one.**

**THIS SUPERSEDES `cc_instruction_defense_share_sizing_second_2026_09_08.md`. DO NOT RE-RUN IT.** Its
Task 0 completed and committed at `45a0527b90e895bee735cf9aa57c4d8e2a640478`; **nothing of that Task 0
is repeated here.** Its Task 1 stopped on a premise the dispatch declared ESTABLISHED and which was
false at the object. **That was the writing side's error, and it is the SECOND of the same shape in
this arc** — the first issue's zero-tracked-modifications expectation was the first. The batch was
right to stop both times, and its report `cc_report_defense_share_sizing_second_2026_09_08.md` was
read in FULL by the writing side, with every load-bearing claim re-verified at the objects before this
dispatch was written. **Nothing in it was found wrong.**

**THE ERROR, NAMED SO IT IS NOT REPEATED.** The second issue's premise (1) said
`claude_md_reading(claude_md)` returns spans carrying `lo` and `hi`. **It does not.** It builds span
records with those keys, uses them to compute each span's characters and lines, and then strips both
from everything it returns — read at `tools/audit/gen_session_start_read_size.py`, the two return
lists, each a dict comprehension filtering `("lo", "hi")`. The writing side had read `_resolve_span`,
which does return them, and inferred the rest without reading the function that consumes it. **An
inference was published under an ESTABLISHED marker, which is what #19 forbids.**

**AND THE STRIP IS DELIBERATE, WHICH DECIDES THE REPAIR.** That artifact is published, and **D-307**
holds that a span is named by its HEADING and never by a line number. Keeping `lo`/`hi` out of the
rendered artifact is that rule working. **So the repair must preserve the strip in what is PUBLISHED
and expose the coordinates only to a caller, in memory.**

**THE BASE.** Tip `45a0527b90e895bee735cf9aa57c4d8e2a640478`.

**★ THIS DISPATCH WAS FACT-CHECKED AT THE OBJECTS BY A LATER SITTING BEFORE IT WAS RUN, AND AMENDED
IN THREE PLACES. 2026-09-08, the fourth sitting of this arc.** The tip was unmoved and nothing had
run. What was read to check it: `gen_session_start_read_size.py` at `claude_md_reading` and at both
of its return lists; `gen_guard_classification.py` at its population and at all three of its STOPs;
`gen_guard_state.py` at `AUTHORED` and at `HISTORICAL`; `session_start_read_size.json` whole;
`CLAUDE.md` at every emphasised occurrence of the three marker words, each placed against the six
span bounds; and the base commit's own shape at `git show --stat` by explicit hash — **eleven paths,
ten files entering git and `cowork_handoff_entry_one_hundred_and_forty_seven.md` the one
modification, which is what makes Task 0(a)'s expectation sound rather than assumed.** **Every
premise below held at its object.** The three amendments are each marked ★ at their site: a third
cross-check named in premise (3); the `Why` marker row widened in premise (4) and in the Task 2
table; and a fifth path added to Task 0(c). **Nothing else was changed, and no task was reordered.**

**A STANDING EXPECTATION, STATED ONCE SO IT IS NOT REDISCOVERED A THIRD TIME.** A handoff entry
committed by a batch and then amended later in the same sitting appears as a tracked modification at
the next batch's Task 0. It happened to entry 147 and it has now happened to entry 148. **Task 0(a)
below expects exactly that one file and no other.**

---

## PREMISES

**ESTABLISHED, each read at the object named, by the writing side unless stated:**

1. `tools/audit/gen_session_start_read_size.py` carries `claude_md_reading(claude_md)`. Under the
   membership regime it builds `session_start` and `conditional` span records carrying `name`, `kind`,
   `lo`, `hi`, `located_by`, then sets `characters` and `lines` on each from `lo`/`hi`, and **returns
   the two lists with `lo` and `hi` filtered out**. Under the whole-file regime it returns no spans at
   all. It also carries module-level `ITALIC` and `BOLD` regular expressions, `_paragraph_end`,
   `at_tree`, a `__main__` guard, and a `use_utf8_output` import after a `sys.path` insert.
2. `tools/audit/session_start_read_size.json` records the six session-start spans at **97,805**
   characters and the whole ordinary session-start read at **245,555**.
3. A new tool carrying `--check` enters `gen_guard_state.py`'s derived population by construction and
   **must** be enrolled in its `AUTHORED` table, **and must also carry a verdict in
   `gen_guard_classification.py`**, whose population is drawn from that same table and whose first
   STOP is a tool in it with no authored verdict. *(Established by the stopped batch, re-verified by
   the writing side at both sources.)*
   **★ AND THERE IS A THIRD CROSS-CHECK IN THAT SAME FILE THAT THE SECOND ISSUE DID NOT NAME, ADDED
   HERE BY THE FOURTH SITTING OF THIS ARC AFTER READING THE CHECK ITSELF.**
   `gen_guard_classification.py` also requires that the set of tools whose authored verdict is
   `POINT` — *records-a-point-in-time-measurement* — be EQUAL, in both directions, to
   `gen_guard_state.HISTORICAL`, and STOPS otherwise. `HISTORICAL` is the table of tools whose
   subject is a SUPERSEDED program and which are therefore NOT RUN. **So a `POINT` verdict on the
   new tool would halt the run.** The verdict this tool takes is `LIVE`
   (*re-derives-a-live-invariant*) on the ground its nearest sibling already carries:
   `tools/audit/gen_session_start_read_size.py` is enrolled `["--check"]` and verdicted `LIVE`
   because every character count is re-measured on every run and its inputs are parsed from
   `CLAUDE.md` itself rather than listed. The new tool has exactly that shape. **If, having read
   the check, you judge the verdict to be other than `LIVE`, STOP and report — do not author a
   `POINT` verdict and do not add anything to `HISTORICAL`.**
4. **The authored marker table of the second issue was DEFECTIVE and is corrected in Task 2.** At this
   tree `CLAUDE.md` carries, in the six session-start spans: a **bold** `**Founding instance:**` in
   Conventions, which the `ITALIC` lookarounds exclude by construction; an **italic** run opening
   `Founding instance,` **with a comma** in the decisions-register span; and a **plain, unemphasised**
   clause opening `Founding instances of the gap:` in Conventions, which wraps across two lines.
   **The second issue's row for an italic `Founding instance:` matches NOTHING.** *(Found by the
   stopped batch; re-verified by the writing side at the file, distinguishing bold from italic.)*
   **★ AND THE SAME DEFECT IS PRESENT IN THE `Why` ROW, IN THE OTHER DIRECTION — FOUND BY THE FOURTH
   SITTING OF THIS ARC AND CORRECTED IN TASK 2.** Every emphasised occurrence of the three marker
   words in `CLAUDE.md` was located and each was placed against the six span bounds. Inside the six
   session-start spans there is an emphasised run opening `Why` **followed by a comma** — the
   *"Why, in the user's own recorded ground:"* clause of the phase-1 finish-line ruling in
   Conventions — and the second issue's row, which admitted only a space or a colon after `Why`,
   does not reach it. **This one does NOT produce a STOP; it silently lowers the figure**, which is
   why it is corrected here rather than left to be discovered by a dead row. Row 1 below is widened
   to a space, a colon **or a comma**, on exactly the ground row 3 was widened.
   **★ AND ONE FIGURE ABOUT THE TABLE ITSELF, MEASURED SO THAT A STOP IS NOT MISREAD WHEN IT COMES.**
   The `Evidence` row matches **exactly one** clause inside the six session-start spans — the
   *"Evidence:"* clause of the single-file-opening rule at the end of Conventions. Its only other
   occurrence in the file sits inside the CONDITIONAL gate-and-preset span, which an ordinary
   session does not read and which this measurement does not count. **The row is therefore one
   rewording away from being a dead row**, and if the zero-match STOP below ever fires on it, that
   is the reason to look at first.

**DECLARED UNESTABLISHED — check and report either way:**

5. Whether any tracked modification other than the one named in Task 0(a) exists at the tree you run
   on. **Re-run the enumeration; do not carry any earlier result.**
6. Whether `tools/audit/guard_state.json`'s reported `--check` staleness — the previous batch found
   `--check` saying it does not re-derive, with every verdict and every failing member matching, and
   did not locate the cause — is still present. **REPORT IT, do not correct it, and do not spend the
   batch hunting it.**

---

## TASK 0 — the start state

**(a)** Run the sanctioned changed-paths enumeration over the whole tracked population and record it
at `tools/audit/changed_paths_defense_sizing_third_task0.json`.

**EXPECTED: EXACTLY ONE tracked modification —
`cowork_handoff_entry_one_hundred_and_forty_eight.md`, on the standing ground above — and no other,
with no deletion and no rename.** **Establish it at the object**: fetch the committed text at the base
by explicit hash, read both copies whole, and **STOP if the working-tree copy differs in any way the
entry's own declared amendment does not account for.** Any other tracked modification is a STOP.

**(b)** Run the full guard set with `--check` at this tree and record its state. **Run it with
`--check` and not bare**, for the reason the previous batch gave and which stands: a bare run rewrites
the committed `tools/audit/guard_state.json` and would fold the tree's current state into a committed
record before this batch's own commit. **Any departure from the state that batch recorded — 80 run,
65 passing, 15 failing, 4 not run, 16 historical, the failing set member for member — is REPORTED, not
corrected**, premise (6) included.

**(c)** Commit, in ONE commit, this dispatch, the artifact of (a), the amended
`cowork_handoff_entry_one_hundred_and_forty_eight.md`,
`cc_report_defense_share_sizing_second_2026_09_08.md`, and
`cowork_handoff_entry_one_hundred_and_forty_nine.md`. **Verbatim; edit, reformat, re-wrap and
normalise nothing.** Committing the amended entry is an ORDERED act named here with its ground.
**The hundred-and-forty-ninth entry is the writing side's own close of the sitting that corrected
this dispatch; it is UNTRACKED at your base and entering git is all that happens to it here.** If
any of these five paths is absent at your tree, STOP and report rather than committing four.

---

## TASK 1 — make the span coordinates reachable, WITHOUT changing what is published

**THE CONTRACT, stated as a requirement rather than as code the writing side has not run.**

- A caller of `tools/audit/gen_session_start_read_size.py` must be able to obtain, in memory, the
  resolved spans **carrying their `lo` and `hi`**, for the membership regime.
- **The rendered artifact must not change.** `tools/audit/session_start_read_size.json` regenerated
  after this amendment must be **BYTE-IDENTICAL** to the blob committed at the base, and
  `gen_session_start_read_size.py --check` must pass. **Prove both, by comparing against the committed
  blob by explicit hash — not by eye.** **A difference of any kind is a STOP.**
- **No line number reaches the artifact.** The strip stays in force for everything rendered; the
  coordinates are available to a caller and to nothing else. **D-307** is the ground and the amendment
  records it in a comment at the site.
- **The amendment is ADDITIVE.** Existing callers keep today's behaviour without being edited — an
  optional parameter defaulting to the present shape is the obvious form, but the form is yours; the
  contract above is what binds.
- **This is not a behaviour change under #14**: no measured value moves and no output differs. The
  byte-identity proof is what establishes that, and it is why it is demanded rather than assumed.

**If the contract cannot be met without changing the artifact, STOP and report** — do not trade the
artifact for the coordinates.

---

## TASK 2 — build `tools/audit/gen_defense_share.py`, and enrol it in BOTH tables

**WHAT IT MEASURES.** For each of the six SESSION-START spans of `CLAUDE.md`, the characters standing
inside explicitly-marked defense clauses.

**HOW THE SPANS ARE OBTAINED.** Import from `tools/audit/gen_session_start_read_size.py`, using
Task 1's amendment, with that file's own `sys.path` handling, and **call `use_utf8_output`**. **Do not
re-implement the membership parse, do not re-locate a heading, and carry no line number for any span in
this tool's own source.** Take only spans whose `kind` is `"session start"`. **Other than six is a
STOP.**

**THE CORRECTED MARKER TABLE.** Matched by reusing the imported `ITALIC` **and `BOLD`** regular
expressions — never a fresh pattern:

| # | Emphasis | The run opens with |
|---|---|---|
| 1 | italic or bold | `Why` followed by a space, a colon **or a comma** |
| 2 | italic or bold | `Evidence` followed by a colon |
| 3 | italic or bold | `Founding instance` followed by a colon **or a comma** |

**A MARKER FORM MATCHING NOTHING IS A STOP.** Report the match count for each of the three rows, and
**halt if any is zero** — a dead row is a defect in the authored table, and the second issue shipped
one. **Publish every match per clause**, so the table's reach is inspectable rather than asserted.

**WHAT REMAINS UNMATCHED, AND IS DECLARED RATHER THAN CHASED.** The plain, unemphasised clause opening
`Founding instances of the gap:` is a defense the table does not admit, and **it is deliberately left
unadmitted**: a pattern over unemphasised prose would match ordinary text, and the doubt default keeps
the table narrow. **Re-locate it and name it on the artifact as a known miss** — it wraps across two
lines, so a single-line search for the whole phrase fails.

**THE EXTENT OF A MARKED CLAUSE.** From the first character of the marker through the end of the
paragraph containing it, using the imported `_paragraph_end`, bounded by the span's own `hi`. A marked
clause never extends past its span.

**WHAT IS PUBLISHED**, at `tools/audit/defense_share.json`, every value computed and none transcribed
(**D-431**): per span — name, its own character count, marked-clause count, and the characters those
clauses hold; the totals across the six spans, as a share of those spans and of the whole
session-start read, **both denominators re-derived through the imported reader at this same tree**;
per clause — its span, first and last line, the matched marker, its emphasis, and its character count;
and per marker row — its match count.

**THE ESTABLISHMENT, POSITIVE ON EVERY RUN (#19), each a STOP and not a reported field:** every
measured clause lies wholly inside its attributed span; no two overlap; a span's clause characters do
not exceed that span's own count; the six spans' re-derived total equals the reader's; every marker row
matches at least once; and `--check` re-derives the artifact and compares rendered text.

**THE BOUND, DECLARED ON THE ARTIFACT (D-673).** The marker set's reach is **UNMEASURED**; a defense
written without one of these markers is not counted; the published figure is a **LOWER BOUND** and the
artifact says so in those words, naming the unemphasised form above as a known miss.

**THE TWO ENROLMENTS, IN THE SAME COMMIT AS THE TOOL** — an `AUTHORED` entry in
`tools/audit/gen_guard_state.py` and a verdict in `tools/audit/gen_guard_classification.py`. **Neither
may be left for a later act.** **The generated consequences, named because a dispatch's file list must
name its own:** `tools/audit/guard_state.json` and `tools/audit/guard_classification.json` change and
are regenerated and committed with the tool.

**WHAT THE ARTIFACT MUST NOT CLAIM:** that any marked clause is movable; that any unmarked passage is
not a defense; that `cowork_claude_md_live_rule_classification_2026_09_08.md` was consumed — **it was
not**; or that the figure is what a satellite would remove.

---

## TASK 3 — the close

**(a)** Write `STATUS.md` entries **covering BOTH commits** — the eleven-path tracking commit
`45a0527b90e895bee735cf9aa57c4d8e2a640478`, which no `STATUS.md` entry records, and this batch's own —
per the OI-222 pointer convention, restating no figure (**D-431**). **The previous batch left that
commit unrecorded and named the cost; this discharges it, and the record's own rule decides it — the
file is updated as the last act when anything changes.**

**(b)** Perform the forward bound ONCE: re-aim `tools/audit/gen_status_batch_bound.py` at this batch,
**this batch's own entries written FIRST and `--apply` run second**, appending to the previous aimings
rather than replacing them. **Once, not twice — covering both commits in one set of entries is what
avoids a second archiving act.**

**(c)** Regenerate `tools/audit/session_start_read_size.json`, which **does** have a subject here
because (a) moves `STATUS.md`, a member of the read it measures. **No measured value is adjusted to
reach a number.** *(The previous batch was right that it had no subject then.)*

**(d)** Re-run the FULL guard set with `--check` at the closing tree and report it against Task 0(b),
with the new tool's membership expected and every other departure traced to this batch's own ordered
acts or REPORTED.

**(e)** The standing self-check: re-read the actual diff of every touched file against the guiding
principles, the conventions and `DEFECT_TYPES.md`; report every violation found.

**(f)** Write `cc_report_defense_share_sizing_third_2026_09_08.md`: the commit table, what each task
did, premises (5) and (6) answered, the measured values BY CITATION to the artifact and never by
transcription, and every reading taken that this dispatch did not order.

---

## STOP CONDITIONS

- Any tracked modification at Task 0(a) other than the one named, or any deletion or rename.
- The expected modification differing in a way the entry's own declared amendment does not account for.
- Task 1's byte-identity proof failing in any respect.
- `claude_md_reading` yielding other than six session-start spans.
- **Any marker row matching zero clauses.**
- Any establishment check in Task 2 failing.
- The guard set departing from its recorded start state in a way this batch's own acts do not explain
  — **report, do not correct.**
- Any instruction here found false at the objects. **A premise that does not hold is a STOP and a
  report, never something to work around.** *(Two issues of this arc have failed exactly here and the
  batch was right to stop both times.)*

## WHAT THIS BATCH MAY NOT DO

No edit to `CLAUDE.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md` or any ruling record. No
satellite file. No text moved from anywhere to anywhere. No open-items row created, flipped or
discarded. No decisions-register entry, no `D-NNN` allocated, no finding number. No `src/` change, no
build, no test, no golden, no corpus, nothing under `tools/robust_stop/` or `tools/corpus/`. No paper
opened, no extract, no sweep, no verdict moved, no gate lifted. **And no hunt for the
`guard_state.json` staleness — it is reported and left.**
