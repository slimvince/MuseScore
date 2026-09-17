# CC report — the ordinary session-start read of `CLAUDE.md` written as a named membership

> **Executing dispatch:** `cc_instruction_claude_md_boot_membership_2026_09_07.md` (Cowork,
> 2026-09-07), on the user's ruling of that date. **Status: COMPLETE.** Every task of the dispatch
> was performed. **Four things are reported rather than absorbed:** two declared departures (an
> environment artifact in the Task-0 guard capture, §3; and where the membership block was placed,
> §4), and **two FINDINGS the batch's own closing acts surfaced** — the read-size measurement now
> overstating the ordinary session-start read (§8), and every `CLAUDE.md` edit reding two
> decisions-side checks (§11). **Neither finding is repaired here**, and §10 states why. **Two guards
> went red at the close**, both traced to this batch's own ordered act with the cause established at
> the object.
>
> **What this batch did NOT do**, restated from the dispatch and true of the tree it leaves: no
> `src/` edit; no golden; no test changed, moved or run; no build; no measurement of the analysis;
> nothing under `tools/corpus/` or `tools/robust_stop/`; no design; no derivation of any
> specification; no document archived or deleted as a file; no decisions-register entry and no
> `D-NNN` allocated; no open-items row created, flipped or discarded; and no edit to `DECISIONS.md`,
> `ARCHITECTURE.md`, `FRAMEWORK.md`, `OPEN_ITEMS.md`, `CLAUDE_ARCHIVE.md`, any ruling record, or any
> governing document other than `CLAUDE.md` and `STATUS.md`. The row-by-row extraction and the
> pruning pass stay paused; the forward-bound trigger's repair (`OPEN_ITEMS.md` OI-379) and the
> restructure of `CLAUDE.md` into satellite files stay with the user.

---

## 1. The commits

| Task | What it landed | SHA |
|---|---|---|
| 0 | The dispatch landed; A1 and A2 measured | `b679e4f6b528aa16bc1b67bc06194a32eb203f95` |
| 1 | The membership written into `CLAUDE.md`; the one heading amended | `da693541c65ca67d10ed5bec811a04b40c4c0a9c` |
| 2 | *(deliberately nothing — see §6)* | — |
| 3 | The close — this report, the `STATUS.md` entries, the forward-bound move | *below* |

Each commit was pushed and then verified at its own object. **`CLAUDE_ARCHIVE.md` was not edited by
any task of this batch**, and neither was any archiving tool.

---

## 2. The reads performed before anything was touched

The ordinary session-start read (`D-230`, and the 2026-08-29 convention that it binds even when the
opening instruction names a single file) was performed in full and first: `CLAUDE.md`,
`DECISIONS.md`, `STATUS.md`, and the derived gating answer at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`. This batch
is the last one that reads `CLAUDE.md` whole under the old practice, and it had to, because it edits
it.

Then, as the dispatch orders: `cowork_rulings_2026_08_17_session_start_read_sitting.md` in full at
its own object (`D-643` — a ruling invoked as precedent is quoted whole, not in the branch that
supports the claim), and §5 of `cowork_rulings_2026_08_16_preparation_return.md`, which carries
rule (D), the continuous-pruning rule that clause 5 of Task 1 orders tested.

---

## 3. Task 0 — the start state, measured and not relayed

**A1**, over the whole tracked population with the sanctioned enumeration tool
(`tools/audit/changed_paths.py`): **every changed-path record untracked, zero tracked
modifications**, the dispatch present among them. **A1 HOLDS as declared.**

**A2**, the full guard set run and read: the run, passing, failing, not-run and historical-record
counts all matching the relayed start state, **and the failing set identical member for member** to
the artifact committed at `f7d6d7c391`, verified at that object by explicit hash. **A2 HOLDS.**
Nothing was adjusted to reach a number. The values are in `tools/audit/guard_state.json` (D-431).

**The handoff entry needed no landing:** `cowork_away_returns.md` carries no tracked modification.

**Registered expectation E0 — GRADED PASS.**

### Departure (i) — an environment artifact in the capture, established at the bytes and not committed

The Task-0 guard run rewrote `tools/audit/guard_state.json`, and the rewrite differed from the
committed artifact in **exactly one captured line, in character encoding alone**: the open-items
split check emits a dash, and under this session's shell it emitted it in the console codepage
rather than UTF-8, so the runner's UTF-8 decode replaced it. **The cause was established at the
bytes** — the child's raw output inspected under both environments — **before anything was decided**,
and the fix confirmed the same way: with the interpreter's output encoding set to UTF-8 the child
emits the UTF-8 dash and the capture is byte-faithful again.

The committed artifact was **RESTORED rather than a degraded one committed**, and every later run of
this batch was made with the encoding aligned. **No measured value moved**: the summary and the
failing set were identical in both captures, which is what the A2 check turns on. This is reported
rather than absorbed because a session that silently commits a mojibake into a guard artifact
degrades the record without saying so.

---

## 4. Task 1 — the fourteen spans, derived at the tree

**The coordinates were DERIVED at the tree at the Task-0 commit and not taken from the dispatch**, as
clause 4 requires. Every `##` and `###` heading of `CLAUDE.md` was enumerated with the file tools, and
each of the thirteen headings the membership names was then checked to occur **exactly once in heading
form**. Three of the thirteen also occur as ordinary prose elsewhere in the file — a cross-reference
to *Conventions*, a body mention of the *VS Code extension*, and a prose mention of *the decisions
register* — and none of those is a heading, so no heading is ambiguous and none needed a guess.

**The one block anchor** — the session-start read block, which has no heading of its own — was located
by the two texts the dispatch quotes: the opening *"Always read these two files at the start of every
session:"* and the closing *"…NOT part of the session-start read."* **Both occur exactly once.**

### The membership as written

| | Span, by heading | When it is read |
|---|---|---|
| 1 | **Guiding principles**, through the *Delegation pointer* paragraph that closes it | session start |
| 2 | **The open-items register**, whole | session start |
| 3 | **The decisions register**, whole | session start |
| 4 | **The session-start read block itself** (the block the membership sits in) | session start |
| 5 | **Conventions**, whole | session start |
| 6 | **The self-check after every coding exercise**, whole | session start |
| 7 | **Project context** | touches the composing module, or needs the full project-context pointer |
| 8 | **Autonomous operation — composing module** | edits code under the composing module, or runs the standard loop for mismatch reduction work |
| 9 | **Build and test commands** — the command blocks below the read block | builds, tests, or runs a measurement tool whose command lives there |
| 10 | **Gate threshold and preset policy**, including blocks (A) to (D) | measures the analysis, changes a gate or threshold, re-baselines, or needs a ratified baseline |
| 11 | **Scoring model** | unchanged — touches scoring logic (that section's own standing condition) |
| 12 | **Score corpora** | any task involving scores |
| 13 | **Local patches — do not revert** | edits MuseScore's own code, or runs or reviews a dependency update |
| 14 | **VS Code extension — bash command rules** | any session that runs bash commands |

**Six at session start, eight conditional. Nothing beyond the fourteen is named, and no span is named
by a line number** (`D-307`).

### The premise was verified at the object rather than relayed

The dispatch's load-bearing FACT — that nothing in `CLAUDE.md` mandates reading `CLAUDE.md`, so this
act writes a rule rather than amending one — was **re-established here at the file**, not carried from
the dispatch. The session-start mandates the file actually carries are four, and they name: the
derived gating answer (the open-items register's rule (a)); the decisions register's INDEX (that
register's rule (a)); `STATUS.md` and `DECISIONS.md` (the build-and-test section's opening list); and
the binding of those reads against a single-file opening instruction (Conventions, 2026-08-29).
**None of them names `CLAUDE.md` itself.**

Two consequences, and both are written into the file: this act does **not loosen a rule** — it
replaces an unwritten habit with a stated one — and **the membership is narrower than the habit**.

### The three things the ruling carried

1. **The bash-rules section moved to the conditional list and its heading now names its real
   condition** — see §5, where the test the dispatch ordered is answered.
2. **The one split that does not fall on a heading is the build-and-test section**: its session-start
   read block stays at boot, its command blocks become conditional. **No other section is split.**
3. **The conditional list is announced in the kept half** — the table above sits inside span 4, so a
   session that never opens a conditional span still learns it exists and when to read it.

### Departure (ii) — where the membership block was placed, and why

**The dispatch places the membership "immediately after the existing conditional-read sentence for
`BUILD_AND_TEST.md` and its 2026-08-17 provenance note." It was placed one paragraph later**, after
the note recording that `DECISIONS.md` was considered for the same treatment and ruled out, and
before the block's closing paragraph. It is still inside the session-start read block, which is the
placement the dispatch's own stated ground requires.

**The ground.** That note opens *"★ AND `DECISIONS.md` WAS CONSIDERED FOR THE SAME TREATMENT AND
RULED OUT"*, and *the same treatment* points back at the `BUILD_AND_TEST.md` demotion immediately
above it. Inserting between them a block about a new conditionality ruling would make the nearest
antecedent of *the same treatment* this act instead — **changing what an existing sentence says
without changing one of its characters**, which is what constraint 6 forbids and what a session
cannot do silently. The two provenance notes are also about the same two-file list they sit under,
while the membership is about the whole file, so the later placement groups like with like.

**Registered expectation E1 — GRADED PASS**, with departure (ii) declared. Every heading found
exactly once; both block anchors found exactly once; the diff touches the session-start read block
and the bash-rules heading and nothing else; no rule text changed; the membership names the fourteen
spans and nothing beyond them; and clause 5's test is answered below with its ground rather than
assumed.

---

## 5. Clause 5 — the prune-at-amendment rule TESTED, and the reading taken with its ground

Clause 5 orders rule (D) tested here rather than assumed either way, offers exactly two readings for
the one wording this act changes, forbids taking either silently, and makes a third a STOP.

**The reading taken: the former parenthetical stated something FALSE about its own scope, so the
amendment is a DOC-SYNC CORRECTION and rule (D) does not fire.** Nothing moved to
`CLAUDE_ARCHIVE.md`. `#12` is satisfied by the former parenthetical — *"(MANDATORY, every session)"* —
being quoted verbatim at the site and here.

**The ground, established at the object and not argued from the batch's own bars:**

1. **The section's body carries no read-mandate at all.** Its only scope statement is the sentence
   *"Two rules that apply to every bash command, no exceptions"*, so *every session* widened the body
   rather than summarizing it.
2. **The parallel that would make the parenthetical a read-mandate does not hold.** The adjacent
   scoring-model heading's *"(MANDATORY for scoring sessions)"* IS a summary of an explicit
   read-mandate its body states in its first sentence. The bash-rules body has no such sentence.
3. **A session that runs no bash command is bound by nothing in the section** — Rule 1 governs a
   command that may return non-zero, Rule 2 a single bash call. So the parenthetical was not a rule
   that was true and has now been narrowed.
4. **Contrast the precedent this act repeats.** The `BUILD_AND_TEST.md` demotion superseded a wording
   that was TRUE of a live obligation, which is why rule (D) fired there and the superseded wording
   moved to `CLAUDE_ARCHIVE.md` — as that section's own provenance note records. The difference is
   exactly that this heading's claim was not true when it was made.

**The reading is written at the heading itself**, so a later reader meets it where the amendment is
rather than only in this report. **No third reading was needed and no STOP was reached.**

**Clause 5's second limb** — *if any other wording this act touches turns out to be superseded, rule
(D) fires on it* — was checked and is empty: the only other change is an addition where the file
previously carried no statement, which supersedes nothing.

---

## 6. Task 2 — what was deliberately not done

**No open-items row was created.** This batch carried out a ruled change; it did not find a defect in
what it was ordered to do. A row would put a non-issue in the register. *(A defect the batch's own
closing acts surfaced is reported in §8, and the reason no row was opened for it is given there.)*

**No decisions-register entry was written and no `D-NNN` was allocated**, although rule (c) asks for
one in the commit that records a ratification. The reason is the writing side's reading, carried out
as the dispatch states it and reported as such: `CLAUDE.md`'s own clause on discharging rule (c) once
it has already been missed requires an accumulated run of rulings to be **CLASSIFIED first, put to
the user as a reading file, and landed in ONE commit**, with no entry written before the user rules on
the classification. That debt exists and is unclassified. Writing this one entry alone would leave the
register partly current and partly not, with nothing to tell a reader which. **So this ruling joins
the debt.** The user can overrule this in one word.

---

## 7. Task 3 — the close

**The `STATUS.md` entries**: one per task — Task 0, Task 1, Task 2 and the close — each a POINTER
under the OI-222 convention, with no figure restated (`D-431`).

**The forward-bound move, performed on this batch itself as an ORDINARY move.**
`tools/audit/gen_status_batch_bound.py` was re-aimed at **all six authored fields** —
`BASE_COMMIT` at this batch's last task commit before the close, `PREVIOUS_BATCH_DISPATCH` at the
prune-at-amendment batch, `ACT_DATE`, `DISPATCH`, `TASK`, and `MOVE_KIND` at `"ordinary"` — with
`PREVIOUS_AIMINGS` **appended to rather than replaced** (`#12`), this batch's own row recorded in the
same act that makes it. **None of the six was left naming the previous aiming**, which is the check
the recorded 2026-09-02 incomplete re-aiming exists to force.

**The order was mechanical, not preferred:** this batch's own entries were written into `STATUS.md`
**first** and `--apply` was run **second**. The declared prefix adjustment fires on the then-previous
batch's newest entry, whose `Last updated: ` prefix moves up to the newest of this batch's own
entries; running the two in the other order matches nothing and STOPs. **It fired as predicted.**

The move ran and **both reconciliation limbs came back green** — every moved entry byte-present in
`STATUS_ARCHIVE.md` exactly once, and absent from the must-read. The entry count, the character
count and the per-entry records are in `tools/audit/status_batch_bound.json` and are not restated
here (`D-431`).

**The read-size measurement was regenerated**, and the ground is stated rather than assumed: two
members of the session-start read — `CLAUDE.md` and `STATUS.md` — moved in this batch, which is that
check's own sanctioned cause and remedy, the same one the previous batch applied for `STATUS.md`
alone. **No measured value was adjusted to reach a number**: the artifact was re-derived and its
`--check` re-run afterwards. The values are in `tools/audit/session_start_read_size.json`.

---

## 8. A FINDING the closing acts surfaced, reported and not repaired here

**The read-size measurement now overstates the ordinary session-start read, and its guard is green
while it does so.**

`tools/audit/gen_session_start_read_size.py` authors the membership of the ordinary session-start
read as three WHOLE documents, and counts `CLAUDE.md` at its full length. Its own docstring states
the rule it works to: *"A CONDITIONAL read … is NOT a member: it is read by the sessions its
condition names and not by an ordinary one."* **After this batch's ruling, eight spans of
`CLAUDE.md` are exactly that** — conditional, read only by the sessions their conditions name — so by
the tool's own rule they are no longer part of the ordinary read, and the measurement counts them
anyway.

**Why it matters, and it is not bookkeeping.** This measurement is the instrument the whole pruning
arc reports its savings with, in an arc the user opened because the session-start reads are too
large. An instrument that overstates the quantity a decision is taken on is the `#19` case exactly:
its `--check` passes, so nothing flags it, which is the silent-failure direction. Its own docstring
already anticipates the shape — *"a mandatory read added to `CLAUDE.md` without being added here
would not appear"* — but the case that has actually arrived is the mirror of it: a mandatory read
**narrowed** in `CLAUDE.md` without being narrowed here.

**Why no row was opened.** This batch's standing bars say in terms that no open-items row is created,
flipped or discarded. The finding is therefore **surfaced** — here, in the `STATUS.md` close entry,
and to the user — rather than rowed, and it is **not repaired**: changing what that tool measures
would change a published measurement, which is not this batch's to do. **The row is owed.**

*What the finding does NOT say:* that any figure this batch published is wrong. The regenerated
measurement re-derives exactly what the tool is written to measure, and it is reported as that. What
is wrong is the fit between what the tool measures and what the ordinary session-start read now is.

---

## 9. The self-check on the diff (the standing rule, run before this was reported)

The actual diff of every touched file was re-read at the object — not the memory of writing it — and
checked against the guiding principles, the conventions, the gate and threshold policies, and
`DEFECT_TYPES.md`.

- **`CLAUDE.md`** — two hunks and nothing else: the membership block, and the heading plus its
  provenance note. **No principle, register rule, convention, gate value or patch record changed.**
  `#6`: the membership sits in the one block that states what is read at start, so no second home.
  `D-307`: no line number anywhere in the added text. `#12`: the former parenthetical preserved at
  the site. American English checked and one British spelling corrected before the commit. The
  reserved-word convention checked term by term over the added text: *score* used only of music,
  *measurement tool* never *instrument*, *register* never bare, and no bare use of *note*, *mode*,
  *key*, *part*, *figure* or *scale* in a non-musical sense.
- **`STATUS.md`** — four added entries and the `Last updated: ` prefix moved down one entry, which
  is the mechanism's own declared adjustment; the five moved entries left by the tool, byte-faithful,
  never retyped.
- **`STATUS_ARCHIVE.md`** — written only by the forward-bound tool, never by hand.
- **`tools/audit/gen_status_batch_bound.py`** — six authored fields re-aimed, `PREVIOUS_AIMINGS`
  appended to rather than replaced, and the new ★-block states what the move is and what is expected
  to fire, so the aiming is readable rather than a value that changed for no stated reason.
- **`tools/audit/session_start_read_size.json`** and **`tools/audit/guard_state.json`** — generated,
  never hand-edited.

**One violation-shaped thing was found and it is §8**, surfaced rather than silently shipped. The two
departures are §3 and §4, both declared.

---

## 10. The guard set at the closing tree

*(Run and read at the tree carrying this close, never inferred; recorded by the run itself in
`tools/audit/guard_state.json` and committed only after the run. The interpreter's output encoding
was set to UTF-8 for every run of this batch after the cause in §3 was established, so the captures
are byte-faithful.)*

| | Start (Task 0) | End (this close) |
|---|---|---|
| Guards run | 80 | **80** |
| Passing | 67 | **65** |
| Failing | 13 | **15** |
| Not run | 4 | 4 |
| Historical records | 16 | 16 |

**The thirteen inherited failures are unchanged, member for member: none cleared, none of them
touched by this batch. TWO WERE ADDED, both by this batch's own ordered act, and the cause of each is
ESTABLISHED AT THE OBJECT rather than named as a likely candidate (`D-669`).**

- `tools/audit/decisions/gen_phase1p_delegation_bar.py --check`
- `tools/audit/decisions/gen_home_classification.py --check`

**The cause, one cause for both.** Both derivations LOCATE their delegation anchors live in the
user-ratified surfaces — `CLAUDE.md` among them — and record the located **line number** into their
committed artifacts. `tools/audit/decisions/phase1p_delegation_bar.json` carries a series of
`CLAUDE.md:<line>` citations, and `home_classification.json` carries one per entry, for example
D-321's `"delegation_at": "CLAUDE.md:1290"`, which is the scoring-model section's delegating
sentence. **This batch inserted lines into `CLAUDE.md` above every one of those anchors, so each
citation's line number moved and the artifacts no longer re-derive.**

That also accounts for the four fields the home-classification check names — D-321, D-322, D-323 and
D-324. They are `docs/scoring_model.md` entries, and this batch did not touch that file; **what moved
is not their home but the position of the clause in `CLAUDE.md` that delegates to it.** The
established cause is the same one, and no second cause was assumed.

### Why they were NOT regenerated

The remedy for a governing-surface-derived check is regeneration — that is what §7 did for the
read-size measurement, on the dispatch's own instruction. **It was not done for these two, and the
ground is the dispatch's own standing bars.** `gen_home_classification.py`'s write mode writes
`tools/audit/decisions/backbone_decisions.json`, the decisions register's source of record, from
which `DECISIONS.md` is generated. This batch is barred from any decisions-register write and from
editing `DECISIONS.md`. Regenerating the delegation-bar artifact alone would leave it inconsistent
with the classification that imports from it, which is worse than leaving both red and saying so.

**Registered expectation E2 — GRADED PASS.** The end state was run and read rather than inferred,
and **every addition beyond the recorded start state is traced to this batch's own ordered act**,
with its cause established at the object.

---

## 11. A SECOND FINDING, surfaced with the first

**Every edit to `CLAUDE.md` reds these two decisions-side checks, and nothing in the record says
so.**

The coupling is a standing property, not a defect this batch introduced: the two derivations record
live-located line numbers into committed artifacts, so any insertion above an anchor stales them. It
has been dormant because the batches since 2026-08-18 either did not edit `CLAUDE.md` or did not
reach these checks — the immediately preceding batch states in terms that it edited neither
`CLAUDE.md` nor `CLAUDE_ARCHIVE.md`.

**Why it is worth stating.** A dispatch that edits `CLAUDE.md` currently learns about this by turning
the guard set red at its close, after the edit is committed — and the remedy needs a decisions-register
write, which several dispatch shapes bar. The record already anticipates the class: `D-307` forbids a
SPECIFICATION citing by raw line number precisely because the anchor machinery cannot maintain it. Here
the citation is generated and re-located on every run, which is the right design; what is missing is
that the two artifacts are **not named among the things a `CLAUDE.md`-editing act regenerates**, the way
the read-size measurement now is.

**No row was opened**, for the same reason as §8: this batch's standing bars forbid it. **The row is
owed**, and the finding is surfaced here, in the `STATUS.md` close entry, and to the user.

*What this finding does NOT say:* that either check is wrong, or that any classification in the
decisions register has changed. Nothing about any decision's home, section or class moved — only the
line at which the delegating sentence sits in `CLAUDE.md`.
