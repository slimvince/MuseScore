# CC report — the session-start read measurement stops overstating its subject, and the three owed rows are opened

**Dispatch:** `cc_instruction_read_size_repair_and_rows_2026_09_07.md` (Cowork, 2026-09-07, on the
user's ruling of that date).
**Executed by CC, 2026-09-07.** Base tip at session start `1ac4059688aeab10a1132493a74972f395240009`.

*Per the OI-222 pointer convention, `STATUS.md` carries POINTERS and the arithmetic is here.*

---

## 0. The ordinary session-start read was performed in full

`D-230` and the standing convention P-1 — a single-file opening instruction is not an exemption
from the session-start read — were both honoured before the dispatch was acted on.

- **`CLAUDE.md` at its ruled membership.** The file arrived whole in this session's project-instructions
  context block, and the six session-start spans were read there. *(Recorded in one line as the
  handoff entry asks: the harness delivered `CLAUDE.md` whole. This is a second observation of the
  same kind [[OI-376]] records, at this session.)*
- **`DECISIONS.md` whole** — the INDEX, all 862 lines, in three reads with no gap.
- **`STATUS.md` whole.**
- **The derived gating answer** — `tools/audit/nongating_apparatus_rows.json` →
  `★_the_live_gating_answer` → `gating_ids`, its header and all its identities.

**Then, as the dispatch orders:** `tools/audit/gen_session_start_read_size.py` at its own source,
whole; `tools/audit/session_start_read_size.json`; and rows OI-377, OI-378, OI-379 and OI-380 with
their four detail files.

---

## 1. The commits, verified at the objects

| Task | SHA | Paths | Shape |
|---|---|---|---|
| Task 0 | `dc43e265b46efe35c92a6347dd26cc3f46863717` | 2 | 372 insertions, **0 deletions** — all additions |
| Tasks 1 and 2 | `61e9e6e54d4bf3eead07927db830829091915f2e` | 2 | 622 insertions, 29 deletions |
| Task 3 | `5ec1f97cb956488717af7f4cbfde6ffc4eb70a51` | 6 | 423 insertions, 8 deletions |
| Task 4, the close | *filled in by the end-state commit* | — | — |

Every hash was verified with `git show --stat <sha>` by explicit hash after the commit, and each was
pushed; each push exited 0. **No value was invented at any point.**

**One commit was amended before it was pushed** — the Tasks 1 and 2 commit, after the standing
self-check found a convention breach in this batch's own new text (§7). The amend is stated rather
than absorbed; nothing was rewritten after a push.

---

## 2. Task 0 — the start state, measured and not relayed

**A1, over the whole tracked population** with the sanctioned enumeration tool
(`tools/audit/changed_paths.py`): **920 changed-path records, every one untracked, ZERO tracked
modifications**, the dispatch present among them. Verified mechanically rather than by eye — a
search for any record not opening with the untracked marker returns only the tool's own summary
line. **A1 HOLDS as declared.**

**A2, the full guard set run and read:** **80 run, 65 passing, 15 failing, 4 not run, 16 historical
records** — matching the relayed start state at every count and matching the preceding batch's own
recorded end state.

**The failing set matches member for member, and that was established rather than compared by eye.**
The run rewrote `tools/audit/guard_state.json` **byte-identically to the committed artifact**, which
the changed-path enumeration taken immediately afterwards confirms by reporting **no tracked
modification at all**. A byte-identical artifact carries a byte-identical failing set, so no second
comparison is needed. **Nothing was adjusted to reach a number.**

**No encoding departure this time.** The preceding batch recorded one — a child tool emitting a dash
in the console codepage — and established its remedy at the bytes. Every run of this batch was made
with the interpreter's output encoding set to UTF-8, and the artifact came back byte-faithful.

**The handoff entry needed landing and got it.** This line's hundred-and-forty-seventh entry appeared
**untracked during Task 0**, between two enumerations minutes apart, having been written while this
batch was already running. It was committed with the dispatch, as Task 0.3 orders. A second file from
the same sitting — `cowork_memory_pointer_cut_2026_09_07.md` — was left untracked: it is neither
ordered by this dispatch nor within this batch's file list.

**Registered expectation E0 — GRADED PASS.**

---

## 3. Task 1 — the measurement stops counting the conditional spans

### 3.1 The membership was DERIVED at the tree, never taken from the dispatch

The block was located by the text it opens with, **found exactly once**. From it the tool parses the
six session-start span names and the eight conditional ones, and **no span name, heading or anchor is
carried in the tool at all** — which is the idiom `rule_a_pointer()` already used, and the reason its
own comment gives: a later amendment of the membership moves this measurement without anybody editing
the tool.

**The block's own declared counts are used as a CHECK on the parse.** Six bullets against a header
saying six, eight rows against a header saying eight; a disagreement is a STOP. A written-out number
is a word, not a transcribed value.

### 3.2 The resolved coordinates of all fourteen spans

Every span is named by its **heading** and never by a line number (**D-307**); each heading was found
exactly once in heading form or the run would have stopped. Sizes are in the artifact and are not
restated here (#17f, **D-431**).

| | Span, as the membership names it | How it resolved |
|---|---|---|
| 1 | **Guiding principles** | the heading `## Guiding principles`, closed at the paragraph the membership names — the one opening `**Delegation pointer` |
| 2 | **The open-items register** | the heading `## The open-items register (user-directed, 2026-07-10; split into index + detail files, user-ratified 2026-07-26)` |
| 3 | **The decisions register** | the heading `## The decisions register (shape user-ratified 2026-07-28; content + living surface 2026-08-02)` |
| 4 | **This block** | the two anchors the membership itself quotes — from *"Always read these two files at the start of every session:"* through the paragraph ending *"…NOT part of the session-start read."* |
| 5 | **Conventions** | the heading `## Conventions` |
| 6 | **The self-check after every coding exercise** | the heading `## The self-check after every coding exercise (user-directed, 2026-07-11)` |
| 7 | **Project context** | the heading `## Project context` |
| 8 | **Autonomous operation — composing module** | the heading `## Autonomous operation — composing module` |
| 9 | **Build and test commands** | the heading `## Build and test commands` |
| 10 | **Gate threshold and preset policy** | the heading `## Gate threshold and preset policy` |
| 11 | **Scoring model** | the heading ``## Scoring model — `docs/scoring_model.md` (MANDATORY for scoring sessions)`` |
| 12 | **Score corpora** | the heading `## Score corpora` |
| 13 | **Local patches — do not revert** | the heading `## Local patches — do not revert` |
| 14 | **VS Code extension — bash command rules** | the heading `## VS Code extension — bash command rules (MANDATORY for any session that runs bash commands)` |

**The Guiding principles span's close coincides with the end of its section**, and the artifact
records that as a derived field rather than leaving a reader to assume it.

### 3.3 ★ One thing the dispatch did not anticipate, found at the tree and solved without widening anything

**The membership block QUOTES the anchors it names spans by, so a whole-file search finds each of
them TWICE** — once as the naming, once as the named. A naive search would have stopped on an
ambiguity the record does not have.

**The resolution is stated at the site and is narrow: an anchor is sought OUTSIDE the block**, the
block's own extent being derived (from its opening text to the line after its last table row). *The
naming is not the thing named.* Nothing about heading resolution changed, and the ambiguity STOP is
untouched for every anchor outside the block.

### 3.4 What the measured value became, and what is published beside it

`CLAUDE.md`'s contribution is now **the sum of the six session-start spans**. The counting convention
is stated in the artifact in the same place and manner the tool already states how a key's span is
counted: a span runs from its heading through the line before the next heading at the same or a
higher level, trailing blank lines dropped, sized as those lines joined by newlines.

**The eight conditional spans are published beside the read and never summed into it**, each with
what it is and the condition that calls for it — the treatment `FURTHER_SPANS` already had.

**And one thing the dispatch did not ask for is published because leaving it silent would mislead.**
The conditional *Build and test commands* span CONTAINS the session-start read block, which is one of
the six. Resolving it by its heading, as the membership's own rule requires, therefore double-counts
that block inside the conditional column. Rather than authoring a special case, **every overlap
between a conditional span and a session-start span is DERIVED from the resolved ranges and
published**, so a reader sees it. No total is affected: conditional spans are never summed in.

### 3.5 The member row's citation

`CLAUDE.md`'s `MEMBERS` justification read *"the project instructions themselves, which every clause
below is written in"* — citing no clause, where the other two rows each quote a real one, and written
when no clause existed to cite. **It now carries the clause, DERIVED and quoted out of the membership
block itself** rather than retyped into the tool. Retyping it would have added one more transcription
site to a file that already carries [[OI-377]]'s three.

### 3.6 The two regimes — and the check the dispatch ordered because the writing side had inferred it

Stated rather than inferred: block **absent** → whole-file practice; block **present** → ruled
membership; block present with an unresolvable span → **STOP**. The fallback exists for the absence of
the block and nothing else. **Every movement row names the regime on both sides**, and where the two
differ the row says so in terms and says what it means — that the change is not a saving any act made.

**Both recorded earlier commits resolve to `whole-file practice`, MEASURED at their git objects.**
The handoff entry declared this INFERRED from how the tool describes those commits and asked for it to
be checked. It is checked, and it holds.

### 3.7 The constraints on the edit

- **No other behaviour changed.** `BASELINES`, `FURTHER_SPANS`, the key-span counting, every STOP the
  tool already carried, and `--check`'s contract are untouched.
- **[[OI-377]]'s three hand-transcribed sites were NOT repaired and NOT touched.** Verified at the
  source after the edit: all three still stand, unchanged in text; none was removed, none replaced by
  a citation, and no check, marker or fallback was added to any of them. **The row is not made worse
  and not made better.**
- The self-check ran on the diff before the work was reported (§7).

**Registered expectation E1 — GRADED PASS.** The block was found exactly once; all fourteen spans
resolved, each anchor found exactly once under the stated scoping; `total_characters` falls; the
conditional spans are published and not summed; both regimes appear; every movement row names the
regime on each side.

---

## 4. Task 2 — the repaired measurement is ESTABLISHED, not merely run (#19)

**(1) The overstatement is MEASURED, not asserted.** The former whole-file value and the repaired
six-span value are computed at the **same tree**, and their difference published at
`session_start_read_size.json` → `at_the_tree` → `the_reading_of_claude_md` →
`★_the_overstatement_this_repair_removes`. That difference **is** the overstatement, and it is the
finding [[OI-381]] records. No figure restated here (#17f, **D-431**).

**(2) Reproduce-check.** The artifact was written, then **two further independent derivations** were
each compared byte-for-byte against it by `--check`; both passed. After the §7 correction the same
three-derivation check was run again from scratch, and every published value was unchanged.

**(3) Reconciliation in both directions, on every run.** Every span resolved is one the block names;
every span the block names was resolved; none in both, none in neither; and no two spans share a name.
**A mismatch in any direction is a STOP, not a reported field.** What it does not establish is stated
in the artifact: that any span's *bounds* are the ones the membership intends.

**(4) The falsification test, run on every run.** If the six spans' sum is greater than or equal to
`len(CLAUDE.md)`, the tool STOPs — a membership costing at least the whole file has not been derived,
it has been mis-parsed.

**★ One bound is DECLARED rather than left unstated (#24).** The falsification test **runs** and did
not fire. Its **firing** was not exercised on a synthetic input: doing so needs either an edit to
`CLAUDE.md` or a new probe file, and this batch's bars admit neither. **What is established is that
it runs and passes, not that it has been seen to fire.** Both regime branches, by contrast, ARE
exercised by the ordinary run — the tree in one, both baselines in the other.

**Registered expectation E2 — GRADED PASS.** All four hold, and no measured value was adjusted to
reach a number.

---

## 5. Task 3 — the three owed rows

**The identities were derived AT THE INDEX**, not from the dispatch: `OI-380` is the highest
`OPEN_ITEMS.md` carries, and a directory search of `open_items/` holds nothing above it — which is
what the dispatch said to expect, so **no STOP**. The new rows are **OI-381, OI-382, OI-383**, each
with its index row and its detail file **in the same commit** (rule (c)) and each opening with one
canonical token (rule (f)).

### 5.1 OI-381 — created and flipped resolved in this batch

The read-size measurement overstated the ordinary session-start read, and its own `--check` passed
while it did. **Created** because rule (c) requires the discovery rowed — the discovery was the
preceding batch's, whose bars forbade the row — and **flipped** because rule (d) requires a resolution
to flip its row, the repair being this batch's Task 1 at `61e9e6e54d`, with Task 2's measured
difference as its evidence.

### 5.2 OI-382 — established at four objects before it was rowed

The dispatch declared the claim RELAYED and unverified by the writing side, and ordered: establish it
at the tool's source, and **if it does not reproduce, STOP and report — do not row a claim.**

**It reproduces in every clause.**

| What was claimed | Where it was established |
|---|---|
| the test searched the WHOLE entry | the `-` side of `f7d6d7c391`'s diff of the tool: `if PREFIX_ADJUSTMENT in text:` |
| it is now anchored to the entry's opening | the tool's source at HEAD: `if text.lstrip("*").startswith(PREFIX_ADJUSTMENT):` |
| an entry quotes the literal in its own prose | `31dc1e5d88`'s `STATUS.md`: the literal occurs **three times over two entries**, and the entry the next move had to find opens `*2026-09-07 (CC — Same dispatch, Task 1.` — carrying the literal without carrying the prefix |
| the tool's own STOP caught it | `apply_move()`'s occurrence check at HEAD, which refuses unless each entry occurs exactly once in the live file |

**★ THE RESOLVED TOKEN IS THIS BATCH'S OWN READING AND IS DECLARED AS ONE.** The dispatch ordered the
defect *"rowed and nothing else; no remedy proposed"* and named no status. The defect **is repaired at
HEAD**, by another batch. Rowing it OPEN would put a false state on the open-items register's
authoritative status surface, which three separate derivations read — a doc-sync violation (#10) with
mechanical consequences. Rowing it RESOLVED with the repairing commit as its provenance records what
is true, and what the row discharges is rule (c), which the repairing batch left undischarged. **The
reading is reported here, in the commit message and in the row itself; the user can overrule it in one
word.** *"Rowed and nothing else"* is satisfied either way: **this batch did nothing to the defect.**

### 5.3 OI-383 — A3's precondition run first, and its answer recorded either way

**A3's precondition:** six `OPEN_ITEMS.md` rows mention `gen_phase1p_delegation_bar` or
`gen_home_classification`, and the writing side had explicitly NOT read them. **All six were read
before the row was written**, and **none covers the finding**:

| Row | Why it does not cover it |
|---|---|
| [[OI-305]] | RESOLVED. A specific, since-fixed staleness of the classification check; names no coupling to `CLAUDE.md` edits |
| [[OI-309]] | OPEN. Four decisions-chain artifacts not re-deriving; does **not** carry `gen_home_classification.py` at all, and its own text establishes a different cause class |
| [[OI-316]] | OPEN. The reading regime refitting its own predictions; names both generators only as an example of an epoch pattern |
| [[OI-319]] | RESOLVED. Read waves widening the classification check's stale report while [[OI-305]] stood |
| [[OI-327]] | OPEN. Which documents the user's delegations reach; mentions the apply mode only to record it stayed unrun |
| [[OI-330]] | OPEN, and the nearest — but a DIFFERENT tool, a DIFFERENT surface, and an **ambiguity** rather than a moved coordinate; its own text records the delegation bar as **passing** when it was written |

**So a row was created**, and all six are cross-referenced in it rather than duplicated.

**The mechanism was established at both generators' own sources.** `gen_phase1p_delegation_bar.py`
names `CLAUDE.md` among three `RATIFIED_SURFACES`, its docstring lists *"each anchor's current line
number and text"* among what it DERIVES, and `locate()` returns the located line by number.
`gen_home_classification.py` **imports** that tool's `locate` and `FORMS` and writes
`citation = f"{surface}:{ln}"` into every entry's `delegation_at`.

**And its firing was measured at this tree, not named as a likely cause.** The committed
`phase1p_delegation_bar.json` records the scoring-model delegation at `CLAUDE.md:1290`; that line now
stands at **1329**, located by its own text and **found exactly once**. The anchor still resolves
uniquely, which is exactly what separates this from [[OI-330]]'s ambiguity.

### 5.4 Two generated artifacts ride with the rows — a declared reading

The dispatch's file list does not name `open_items/register_check.json` or
`tools/audit/nongating_apparatus_rows.json`. **Creating a row necessarily moves both**, and the list
also omits `guard_state.json`, which the dispatch itself orders written twice. **The list is read as
naming the files this batch AUTHORS**, generated artifacts moving as a consequence of the ordered
acts — which is the shape [[OI-379]]'s own rowing commit used, touching exactly these two beside the
index and the detail file. Both were regenerated, never hand-edited.

**The gating answer moves by exactly one open row** — OI-381 and OI-382 being resolved and so outside
the open population. **The generator did not STOP**, so no new candidate lacked a verdict and **none
was authored**: no apparatus declaration and no gating verdict is hand-added to any of the three rows
(**D-438**).

### 5.5 The register's own checks, after the edit

`register_lint` **PASS** — every row ID unique, at 383 rows.
`index_status_lint --check` **PASS** — every status cell opens with one canonical token, every row
splits into six cells.
`open_items_split_check` **OVERALL PASS** — the bijection holds at 383 index rows and 383 detail
files, no detail file carries a status of its own, and all 200 original items stay byte-verbatim.

**Registered expectation E3 — GRADED PASS.**

---

## 6. Task 4 — the close

**The forward-bound move was performed on this batch itself, as an ORDINARY move.**
`tools/audit/gen_status_batch_bound.py` was re-aimed at **all six** authored fields — `BASE_COMMIT` to
this batch's last task commit pushed before the close began, `PREVIOUS_BATCH_DISPATCH` to the
boot-membership batch, `ACT_DATE`, `DISPATCH`, `TASK` and `MOVE_KIND` — with **one row appended** to
`PREVIOUS_AIMINGS` rather than replacing it (#12). **None of the six was left naming the previous
aiming**, which is the check the recorded 2026-09-02 incomplete re-aiming exists to force.

**The order was mechanical, not preferred.** This batch's own entries were written into `STATUS.md`
**first** and `--apply` was run **second**: the declared prefix adjustment fires on the then-previous
batch's newest entry, and running the two in the other order matches nothing and STOPs. **It fired as
predicted**, under the anchored test [[OI-382]] records.

**Four entries moved**, both reconciliation limbs green — each byte-present in `STATUS_ARCHIVE.md`
exactly once and absent from the must-read. No entry was retyped.

**The read-size measurement was regenerated in the end-state commit**, because `STATUS.md` is a member
of the read it measures and this batch moves it.

**The two nameless 2026-09-02 `STATUS.md` entries are untouched**, as every aiming of this tool
records: they name no dispatch, so no aiming can identify them. That is a declared standing state and
a question standing with the user, not a STOP.

---

## 7. The self-check — what it found, and what was done about it

The standing self-check ran on the actual diff of every touched file, read at the git object rather
than from the memory of writing it.

**It found one class of breach in this batch's own new text, and every instance was corrected before
the work was reported.**

**Reserved music-theory words used in their non-musical senses** — `CLAUDE.md`'s disambiguation
convention reserves the bare word for the musical meaning:

- bare **measure** (noun) in the gauging sense, where the convention reserves it for the bar — at two
  sites in the tool's docstring, two in a published artifact field, and **three artifact key names**.
  All corrected to *measurement* or to *what is measured*; the key names were renamed and the printing
  that reads them updated.
- bare **note** meaning a remark — at two sites. Corrected to *statement*.
- bare **figure** meaning a number — at two sites. Corrected to *value*.
- bare **register** meaning the open-items register, and bare **part** meaning a portion — one each,
  in the row text and a detail file. Corrected.

**The Tasks 1 and 2 commit was amended** (before pushing) to carry the corrections and a corrected
message. The reproduce-check was then re-run from scratch and every published value was unchanged.

**No inherited use was renamed.** The register's own template lines — *"dated notes may be appended
here"*, *"no figure is restated here"* — are the record's standing idiom, and the convention makes the
tree-wide cleanup a scoped decision surface rather than a sweep.

**Other checks made:** American English throughout; every span named by heading and never by line
number in any artifact (**D-307**); no self-invented label, abbreviation or numbering scheme; no
figure transcribed into this report that a generated artifact produces (**D-431**); the file tools
used for every working-tree read, with shell access confined to git object queries by explicit hash
taken from a session's own commit report (**D-253**).

---

## 8. The guard set at the closing tree

*(Run and read at the tree carrying this close, never inferred; recorded by the run itself in
`tools/audit/guard_state.json` and committed only after the run.)*

| | Start (Task 0) | End (this close) |
|---|---|---|
| Guards run | 80 | **80** |
| Passing | 65 | **65** |
| Failing | 15 | **15** |
| Not run | 4 | 4 |
| Historical records | 16 | 16 |

**The fifteen failures are unchanged, member for member: none cleared, none added.** Thirteen were
inherited before the preceding batch; **two were added by that batch's own act and are the subject of
[[OI-383]]**, opened here.

### Why the two were not regenerated

The remedy for a governing-surface-derived check is regeneration — which is what §6 did for the
read-size measurement. **It was not done for these two, on the same ground the preceding close gave
and this batch's own bars repeat.** `gen_home_classification.py`'s write mode writes
`tools/audit/decisions/backbone_decisions.json`, the decisions register's source of record, from which
`DECISIONS.md` is generated; this batch is barred from any decisions-register write and from editing
`DECISIONS.md`. Regenerating the delegation-bar artifact alone would leave it inconsistent with the
classification that imports from it.

**What changed since the preceding close is not the state but the record of it:** the coupling is now
**rowed**, with its mechanism established at both sources and its firing measured, rather than
surfaced in prose alone.

**Registered expectation E4 — GRADED PASS.** The end state was run and read rather than inferred, and
**every departure from A2's measured start state is traced to this batch's own ordered acts** — of
which, on the counts, there are none.

---

## 9. Declared departures and readings — stated rather than absorbed

1. **The resolved token on [[OI-382]]** — §5.2. This batch's reading, not the dispatch's word.
2. **Two generated artifacts committed that the dispatch's file list does not name** — §5.4, with the
   ground and the precedent.
3. **The falsification test's firing was not exercised** — §4, a bound declared under #24 rather than
   left unstated.
4. **One commit was amended before being pushed** — §1 and §7.
5. **A second untracked file from the Cowork sitting was left untracked** —
   `cowork_memory_pointer_cut_2026_09_07.md`, neither ordered by this dispatch nor in its file list.
6. **A conditional span's published size includes a session-start span it contains** — §3.4, with the
   overlap derived and published so it is visible rather than silent.

**No D-253 departure occurred.** Every working-tree read went through the file tools; the guard denied
nothing, and three attempts that would have been denied were not made — two shell reads aimed at
repository paths were refused by the guard at the moment of issue and were replaced with file-tool
reads rather than retried in another dialect. *(Recorded as data for [[OI-378]], which collects
observations about that guard: two denials, both on interpreter code and a listing carrying a literal
repository path, both routed to the file tools. No cause is asserted and none may be read in.)*

---

## 10. What this batch did NOT do

- **It edited no governing document except `OPEN_ITEMS.md` and `STATUS.md`.** `CLAUDE.md` is
  untouched — verified at the enumeration.
- **It repaired neither [[OI-377]] nor [[OI-379]]**, and it proposes no remedy for the rows it opens.
- **It classified no passage of `CLAUDE.md`** as live rule or record-of-amendment.
- **It restructured nothing into satellite files**, and it answers neither of [[OI-380]]'s two
  questions.
- **It opened no paper, no extract and no companion; it ran no sweep; it moved no verdict; it lifted
  no gate.** The row-by-row extraction and the pruning pass stay paused.
- **No `src/` change, no golden, no test changed, moved or run, no build, no measurement of the
  analysis, nothing under `tools/corpus/` or `tools/robust_stop/`, no decisions-register entry and no
  `D-NNN` allocated.**
