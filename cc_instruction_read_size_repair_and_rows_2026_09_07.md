# CC dispatch — the session-start read measurement stops overstating its subject, and the three owed rows are opened

> **Dispatch (Cowork, 2026-09-07), on the user's ruling of this date.** He was put, in plain text
> across two turns and with no widget, a statement of what remains to be done about the boot cost and
> a recommendation with its alternatives and their costs: repair the measurement tool that reports
> this arc's savings, open the rows found yesterday that could not be written, and measure the yield
> of a restructure before committing to one. **His words: *"I agree with your recommendations"* and,
> when told what would be written, *"go ahead"*.**
>
> **Written at a verified stop.** The tip at writing is
> `1ac4059688aeab10a1132493a74972f395240009`, read at `.git/refs/heads/master`, with `.git/HEAD`
> reading `ref: refs/heads/master`. Nothing is running; no batch is out.
>
> **This is the FIRST batch to boot under the ruled membership** — six spans of `CLAUDE.md` at
> session start, eight read only on their condition (the user's ruling of 2026-09-07, written into
> the file itself). **This batch edits no span of `CLAUDE.md` and therefore does not read it whole.**
>
> **NOT in this batch:** the row-by-row extraction (PAUSED); the pruning pass (PAUSED); **the
> authored classification of `CLAUDE.md`'s passages into live rule and record-of-amendment** — that
> is authored judgment, not a mechanical instruction, and it is Cowork-side work; any move of any
> span to `CLAUDE_ARCHIVE.md`; any change to what any rule of `CLAUDE.md` says; any edit to
> `CLAUDE.md` at all; **the repair of OI-377**, whose own row reserves it for its own surface; the
> repair of the forward-bound trigger (OI-379); and the restructure of `CLAUDE.md` into satellite
> files, which stands with the user.
>
> **Read first, in full — the ordinary session-start read (`D-230`, P-1):** the six named spans of
> `CLAUDE.md`, `DECISIONS.md`, `STATUS.md`, and the derived gating answer
> (`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`). **A
> single-file opening instruction is not an exemption from that read.** **Then read, in full:**
> `tools/audit/gen_session_start_read_size.py` at its own source; `tools/audit/session_start_read_size.json`;
> and the `OPEN_ITEMS.md` rows OI-377, OI-378, OI-379 and OI-380 with their detail files.
>
> **The standing bars bind this batch whole:** no `src/` edit, no golden, no test changed, moved or
> run, no build, no measurement of the analysis, nothing under `tools/corpus/` or
> `tools/robust_stop/`, no design, no derivation of any specification, no document archived or
> deleted as a file, no decisions-register entry and no `D-NNN` allocated, and no edit to
> `CLAUDE.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `FRAMEWORK.md`, `CLAUDE_ARCHIVE.md`, any ruling
> record, or any governing document other than `OPEN_ITEMS.md` and `STATUS.md`. **The files this
> batch may write are exactly:** `tools/audit/gen_session_start_read_size.py`,
> `tools/audit/session_start_read_size.json`, `OPEN_ITEMS.md`, the new `open_items/OI-<n>.md` detail
> files, `STATUS.md`, `tools/audit/gen_status_batch_bound.py`, this dispatch, and this batch's report.
>
> **Run the FULL guard set BEFORE the first edit and again at the end; record both states.** Verify
> every commit at the object and record the SHAs in the close. **Commit and push per task.**

## Ruling ledger

- **The user's ruling, 2026-09-07.** Given in conversation against a recommendation stated in plain
  text: repair the measurement tool first; open the owed rows; and measure the yield of a restructure
  before doing one. **His words: "I agree with your recommendations" and "go ahead".** No choice
  question was manufactured, because the alternatives had collapsed and his own standing ruling of
  2026-08-28 forbids inventing one where the facts settle it.
- **What the agreement did NOT carry.** It did not authorise moving any text out of `CLAUDE.md`, and
  it did not authorise the satellite restructure. Those stand with him, together with the two
  questions OI-380 already puts to him.
- **The precedent for repairing a measurement tool that overstates its subject.** The finding was
  surfaced by `cc_instruction_claude_md_boot_membership_2026_09_07.md`'s own close and to the user,
  and left unrepaired only because that batch's bars forbade it. **No new licence is claimed.**

## Premise ledger

*(Each FACT established at the object named beside it by the writing side on 2026-09-07, reading
`tools/audit/gen_session_start_read_size.py` and `OPEN_ITEMS.md` through the file tools.)*

- **★ FACT — the tool measures `CLAUDE.md` WHOLE as an ordinary session's read.** Its authored
  `MEMBERS` table names `CLAUDE.md`, and `measure()` computes `len(claude_md)` for it. Read at the
  source.
- **★ FACT — that contradicts the tool's own stated convention.** Its docstring says, verbatim: *"A
  CONDITIONAL read (`BUILD_AND_TEST.md`, `docs/scoring_model.md`, the joint estimator's section) is
  NOT a member: it is read by the sessions its condition names and not by an ordinary one, which is
  what CONDITIONAL means."* On 2026-09-07 **eight spans of `CLAUDE.md` became conditional.** So the
  tool now counts into an ordinary session's read a quantity that includes eight conditional spans.
  **The measurement OVERSTATES its subject, and it is the measurement the whole pruning arc reports
  its savings with (#19).**
- **★ FACT — `--check` cannot see it.** `main()` re-derives the artifact and compares the rendered
  text against the committed artifact. The fault is in the DEFINITION of the measure, not a drift, so
  **the check passes while the measure overstates.** Read at the source.
- **FACT — the authored member row for `CLAUDE.md` cites no clause.** Its second field reads *"the
  project instructions themselves, which every clause below is written in"*, where the other two
  members each quote an actual clause of `CLAUDE.md`. **Since 2026-09-07 a clause exists.**
- **FACT — the repair follows the tool's OWN idiom and invents nothing.** `rule_a_pointer()` already
  parses rule (a)'s clause out of `CLAUDE.md` so that a later narrowing of that pointer moves the
  measurement **without anybody editing the tool**, and the docstring states that intent in terms.
  The membership is to be derived the same way.
- **FACT — a SECOND and DIFFERENT fault in the same file is already rowed, and this batch does NOT
  touch it.** OI-377 records a count typed by hand at three sites, two of them published into the
  artifact whose own opening field says every value is computed and none transcribed. **That row
  states in its own words that the right repair is a DESIGN question with real alternatives and gets
  its own surface.** So it is not repaired here. **The edit ordered below must not make it worse:**
  if any ordered change touches one of those three sites, that is **reported, not silently resolved.**
- **★ FACT — the earlier-commit readings need a stated regime rule.** `build()` calls `measure()` at
  two earlier commits through `git_show`. Both predate 2026-09-07 by the tool's own description of
  them, so **their `CLAUDE.md` carries no membership block.** A membership derived from that block
  therefore cannot resolve there, and the tool must say which regime each reading used rather than
  stop or silently fall back.
- **ASSUMPTION A1** — the working tree carries no tracked modification and this dispatch is among the
  untracked root files. **Check ordered (Task 0, first act, with the sanctioned enumeration tool):**
  any tracked difference is a STOP-and-report.
- **ASSUMPTION A2 — the guard set's start state is 80 run, 15 failing.** **RELAYED from the preceding
  handoff entry and NOT re-measured by the writing side.** **Check ordered (Task 0, before any
  edit).** A state matching neither that nor the previous batch's recorded end state is a
  STOP-and-report. **Nothing is adjusted to reach a number.**
- **★ ASSUMPTION A3 — no existing open-items row already covers the `CLAUDE.md`-edit coupling.**
  **EXPLICITLY NOT ESTABLISHED by the writing side:** six rows of `OPEN_ITEMS.md` mention
  `gen_phase1p_delegation_bar` or `gen_home_classification` and were not read. **Check ordered as a
  precondition of Task 3(c).** A row that already covers it means **no new row**, and the finding is
  recorded against the existing row instead.

## Task 0 — land the dispatch, and measure the start state

1. **A1's check**, over the whole tracked population with the sanctioned enumeration tool.
2. **A2's check:** the full guard set, run and read. Record it; do not act on it.
3. Commit this dispatch and this line's current handoff entry if it is not yet landed. Push; verify
   at the object. **Record the SHA.**

**Registered expectation E0:** A1 holds; the guard state is recorded as measured.

## Task 1 — the measurement stops counting the conditional spans

### 1a — derive the membership from `CLAUDE.md`'s own block, never from this dispatch

Locate the membership block by the text it opens with — *"★ AND THIS IS WHAT A SESSION READS OF"* —
**found exactly once, or STOP.** From that block, parse the SIX session-start span names and the
EIGHT conditional span names. **Do not take the names from this dispatch.**

Resolve each named span to its coordinates in `CLAUDE.md` **by its HEADING** (`D-307` — never by line
number), each heading found **exactly once in heading form, or STOP**. Two spans are not headings and
are located by quoted anchors, each found exactly once or STOP:

- **the session-start read block**, which has no heading: from *"Always read these two files at the
  start of every session:"* through the paragraph ending *"…NOT part of the session-start read."*
- **the Guiding principles span's close**, which the membership states as *"through the Delegation
  pointer paragraph"*: located by the opening text of that paragraph.

### 1b — what the measured value becomes

`CLAUDE.md`'s contribution to the ordinary session-start read is **the sum of the characters of the
six session-start spans**, not `len(claude_md)`. **State the counting convention in the artifact**,
in the same place and the same manner the tool already states how a key's span is counted, because a
convention nobody states is a convention nobody can check.

### 1c — the eight conditional spans are measured BESIDE and never summed in

Give them the treatment `FURTHER_SPANS` already has and for the tool's own stated reason: published
with what each is and the condition that calls for it, and **never added into `total_characters`**,
because counting them would report a read no ordinary session takes. **A named conditional span that
does not resolve is a STOP, on the same clause that stops the tool when rule (a)'s pointer stops
resolving — a silent zero is what a measurement may never publish.**

### 1d — the authored member row gains its real citation

Replace `CLAUDE.md`'s `MEMBERS` justification — *"the project instructions themselves, which every
clause below is written in"* — with a quotation of the clause that now makes it a member, taken from
the membership block itself and not from this dispatch.

### 1e — the two regimes, stated rather than inferred

At a commit whose `CLAUDE.md` carries **no** membership block, the whole file was the read: that was
the practice, and the file's own provenance sentence records that until 2026-09-07 the whole-file read
was practice and was mandated by no clause. So:

- **block ABSENT →** the reading is the whole file, and the artifact records that reading as
  `regime: "whole-file practice"` **in a field a reader cannot miss**, so a whole-file reading is
  never mistaken for a membership reading;
- **block PRESENT →** the reading is the six spans, recorded as `regime: "ruled membership"`;
- **block PRESENT but a span unresolvable → STOP.** The fallback exists for the ABSENCE of the block
  and for nothing else.

The movement rows this tool publishes must therefore **name the regime on both sides of each
comparison**, because a comparison across a regime boundary is comparing two different questions.

### 1f — the constraints on the edit

1. **NO other behaviour of the tool changes.** Not `BASELINES`, not `FURTHER_SPANS`, not the
   key-span counting, not the STOPs it already carries, not `--check`'s contract.
2. **OI-377's three hand-typed sites are NOT repaired.** If the ordered edit touches one, **report it
   with its ground; do not resolve it.**
3. **The self-check runs on the diff before the work is reported.**
4. Regenerate the artifact. ONE commit, push, verify at the object.

**Registered expectation E1:** the membership block found exactly once; all six session-start spans
and all eight conditional spans resolved, each anchor found exactly once; `total_characters` falls;
the conditional spans are published and not summed; both regimes appear in the artifact and every
movement row names the regime on each side.

## Task 2 — the repaired measurement is ESTABLISHED, not merely run (#19)

The tool is a measurement tool the pruning arc publishes figures from, so a changed measure is
established positively before anything relies on it. Four checks, all published in the artifact or
the report:

1. **The overstatement is MEASURED, not asserted.** Publish the old total and the new total at the
   SAME tree, and their difference. **That difference IS the overstatement**, and it is the finding
   OI-381 records.
2. **Reproduce-check.** Run twice at the same tree; the artifact must be byte-identical, and
   `--check` must pass afterwards.
3. **Reconciliation both ways.** Every span the derivation resolved is one the membership block
   names, and every span the block names was resolved — **none in both, none in neither.** A
   mismatch is a STOP.
4. **Falsification test, run on every run.** If the six spans' character sum is **greater than or
   equal to** `len(claude_md)`, the derivation is wrong and the tool **STOPs** — a membership that
   costs at least as much as the whole file has not been derived, it has been mis-parsed.

**Registered expectation E2:** all four hold, and no measured value was adjusted to reach a number.

## Task 3 — the three owed rows

**Derive the next free row identity AT THE INDEX**, not from this dispatch: read `OPEN_ITEMS.md` and
take the highest existing `OI-<n>`. **The writing side read it as OI-380; if the INDEX says
otherwise, that is a STOP-and-report.** Each row gets **an index row AND its detail file in this same
commit** (register rule (c)), six cells, **the status cell opening with one canonical token** (rule
(f)). **No apparatus declaration and no gating verdict is hand-added to any of them** — a verdict is
derived from a cut and never hand-written (`D-438`).

**(a) The read-size measurement overstated the ordinary session-start read.** Subject: the
measurement tool the pruning arc reports its savings with, and the fact that its own `--check` passed
while it overstated. **This row is created AND flipped to resolved in this same batch**, with Task 1's
commit as its provenance and Task 2's measured difference as its evidence — created because rule (c)
requires the discovery rowed, flipped because rule (d) requires a resolution to flip its row.

**(b) The forward-bound tool's prefix-adjustment defect.** As reported: its declared adjustment
searched the WHOLE entry for the literal `Last updated: ` and fired on an entry that quotes that
literal in its own prose; the tool's own STOP caught it; the test is now anchored to the entry's
opening. **THIS IS RELAYED and the writing side did NOT verify it at the tool's source.** **Read
`tools/audit/gen_status_batch_bound.py` and establish it at the object before rowing. If it does not
reproduce, STOP and report — do not row a claim.** Rowed and nothing else; no remedy proposed.

**(c) Every edit to `CLAUDE.md` reds two decisions-side checks.** As reported:
`gen_phase1p_delegation_bar.py` and `gen_home_classification.py` locate delegation anchors live and
record the located LINE NUMBER into committed artifacts, so an insertion above an anchor stales them.
**A3's precondition runs FIRST:** read the six `OPEN_ITEMS.md` rows that mention either generator. **If
any already covers this, create NO row** and record the finding against that row instead, saying so in
the report. Otherwise row it. Establish the mechanism at the two generators' sources before rowing;
**relayed is not established.** Rowed and nothing else; no remedy proposed.

**Registered expectation E3:** the row identities were derived at the INDEX; (b) and (c) were each
established at the object or stopped; A3's precondition was run and its answer reported either way;
every new row carries a detail file in the same commit and a canonical opening token.

## Task 4 — the close

One `STATUS.md` pointer entry per task under the OI-222 pointer convention, with no figure restated
(`D-431`), **and the forward-bound move performed on this batch itself** — `gen_status_batch_bound.py`
re-aimed at all six authored fields, the then-previous batch being the boot-membership batch, **this
batch's own entries written FIRST and `--apply` run second**, every previous aiming appended to rather
than replaced (#12). **Omitting it reproduces the defect OI-379 records and two batches were written
to clear.**

**Regenerate the read-size measurement in the end-state commit**, since `STATUS.md` is a member and
this batch moves it.

The report `cc_report_read_size_repair_and_rows_2026_09_07.md`: both guard states, every SHA, every
expectation graded, the resolved coordinates of all fourteen spans, the old and new totals with their
difference, the whole diff of the tool characterised, A3's answer, the self-check's output, and every
declared departure reported rather than absorbed.

**Registered expectation E4:** at the tree carrying the close, a fresh full guard run is run and read
rather than inferred, and every departure from A2's recorded start state is traced to this batch's own
ordered acts.

## What this batch does NOT do

- **It edits no governing document except `OPEN_ITEMS.md` and `STATUS.md`.** `CLAUDE.md` is not
  touched.
- **It repairs neither OI-377 nor OI-379**, and it proposes no remedy for the rows it opens.
- **It does not classify any passage of `CLAUDE.md`** as live rule or as record-of-amendment. That
  measurement is Cowork-side work and is not authorised here.
- **It does not restructure `CLAUDE.md` into satellite files**, and it answers neither of the two
  questions OI-380 already puts to the user.
- **It opens no paper, no extract and no companion; it runs no sweep; it moves no verdict; it lifts
  no gate.** The row-by-row extraction and the pruning pass stay paused.
