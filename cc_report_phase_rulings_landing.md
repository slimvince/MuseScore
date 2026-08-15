# CC report — the phase rulings landing

> **What this is.** The coding side's report on `cc_instruction_phase_rulings_landing.md`, performed
> 2026-08-15. The batch record beside it is the PHASE RULINGS LANDING section of
> `cowork_away_returns.md`; this file is the whole of what the coding side says back.
>
> **THE HEADLINE, BEFORE ANY DETAIL. Task 0 is done and pushed. Task 1 — the ruled D-231 rephrasing
> — is NOT LANDED and is STOP-reported.** The ordered insertion was made exactly as ordered, the
> guard set was run, and it turned SIX guards red where the dispatch sanctions only one class of
> red. Four of the six lie outside that class, two of those four are the gate-bearing derivations
> **D-436** reserves, and the dispatch's own words are *any other new red is a STOP-and-report*. The
> edit was therefore reverted, the working tree is byte-identical to the committed one, and the
> ruling awaits a user decision whose whole cost is measured in §2 below.
>
> *(Every guard count lives at `tools/audit/guard_state.json`; none is restated here beyond the few
> values this report is reporting ABOUT, each naming where it was read — **D-431**.)*

---

## 1. Task 0 — the writing-side records and the eighteenth handoff block. Commit `1c52098b64`, pushed

### 1.a What landed, and how it was verified

Exactly the four paths the dispatch names and no fifth:

- `cowork_handoff.md` (the eighteenth entry block)
- `cowork_rulings_2026_08_15_phase_definition_sitting.md` (new)
- `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` (new)
- `cc_instruction_phase_rulings_landing.md` (new — the dispatch itself)

Verified at the index through the sanctioned enumeration BEFORE the commit — four records, one `M`
and three `A` — and at the object AFTER it with `git diff-tree --no-commit-id --name-only -r`.
**The commit's parent is `b1a44ec046`**, which independently establishes that the blob every check
below was taken against was the current one, without trusting a branch-tip read.

**Registered expectation E0 — MET on both limbs.** Four paths at the object; and
`cc_instruction_phase_rulings_landing.md` was staged **plainly**, with no `-f` and no override of any
kind — the first dispatch ever landed that way, both ignore rules over the family having been
removed by the two preceding batches.

### 1.b ★ A1 IS FALSIFIED AS LITERALLY STATED, AND AN ORDERED STOP WAS REACHED AND NOT TAKEN

This is the one judgment call the batch made, and it is declared here, in the commit message and in
the `STATUS.md` pointer rather than left for a reader to notice.

**What A1 said.** *"`cowork_handoff.md`'s on-disk state differs from its committed blob ONLY by the
eighteenth entry block … any difference outside that one block is a STOP-and-report, never a
guess."*

**What was measured.** The check was performed FIRST and entirely at content-addressed objects: the
committed blob `98cd7aa118` (resolved from `b1a44ec046:cowork_handoff.md`) diffed against the
working blob `f64837573c` (produced by `git hash-object -w`). Neither side is a shell read of a
working-tree file, so D-253 is untouched. The result: **83 insertions and ONE deletion.** The
insertions are the eighteenth block. The deletion is **the seventeenth block's heading line**, whose
closing sentence changes:

- removed: `… THE ACTIVE DISPATCH IS \`cc_instruction_ruled_inventory_landing.md\`. THE CURRENT ENTRY POINT.`
- added:  `… THE ACTIVE DISPATCH IS \`cc_instruction_ruled_inventory_landing.md\`. (SUPERSEDED as the entry point by the eighteenth block above.)`

That line is **outside** the inserted block. On a strict reading the batch should have halted at its
first act.

**Why it was not taken as a halt.** Two grounds, both checked rather than assumed. First, the
demotion is this file's OWN established convention: reading the file's headings, every earlier block
down to the eleventh carries the identical marker — *(SUPERSEDED as the entry point by the Nth block
above.)* — so writing a new entry block and demoting the previous heading are two halves of one act,
not two acts. Second, the eighteenth block's own closing sentence announces it: *"(The seventeenth
block below remains binding in everything it states; it is superseded only as the entry point.)"*
And Task 0 commits the path WHOLE in either case, so the check's purpose — that nothing unauthored
rides into the commit — is met by the measurement itself.

**The cost, stated and not discharged.** A pre-registered STOP was judged past by the executing side.
That is precisely the act a pre-registered STOP exists to prevent, and the record's own reckoning is
that declared STOPs have caught every premise error this side has made. The finding is therefore
published in three places so it can be overruled cheaply. **Nothing about the landed content is at
risk**: the demoted heading is committed and readable, and reverting it is one edit.

*(One pre-existing inconsistency was noticed in passing and is NOT this batch's business and NOT
touched: the TWELFTH block's heading still reads `THE CURRENT ENTRY POINT.` in the committed file.
It was already so before this batch.)*

---

## 2. Task 1 — the ruled D-231 rephrasing. ★ STOP: NOT LANDED

### 2.a A2's check — CONFIRMED

The whole D-231 Conventions entry was read with the file tools (`CLAUDE.md:1597-1723` at the tree as
found). The truth-half sentence *"the specification text is corrected wherever it states something
false at HEAD"* occurs in the file **exactly once**, inside that entry — no second live occurrence,
no quotation of it elsewhere. No STOP was owed on A2, and the entry is the ONE home of the
three-phase text as A2 states.

### 2.b The edit, made exactly as ordered

The dispatch's block was inserted VERBATIM at the ordered position — immediately after the entry's
opening bold heading sentence ends and before `Three phases, strictly ordered.` begins — wrapped to
the file's own width at the bullet's two-space continuation indent. Nothing else in `CLAUDE.md`
moved. The whole-file change, measured blob against blob (`61ae1b484c` → `36ffe5e0b3`), is **one
hunk**: 24 lines added, 1 removed.

### 2.c The six new reds, each cause MEASURED

The full guard set went from ONE failing to SEVEN. Each cause was established by regenerating the
artifact, diffing it against its committed blob by explicit hash, and restoring it — never by
reading the tool and reasoning about what it would do.

| # | guard | what actually changed | class |
|---|---|---|---|
| 1 | `gen_cluster_dispositions.py --verify` | 11 register home anchors in `CLAUDE.md`, all below the insertion, all by exactly **+23**; all 677 verbatim quotes still found at their homes | **ANCHOR DRIFT** — the sanctioned class |
| 2 | `gen_phase3_gate_partition.py --check` | `found_lines` / `actual` coordinates 1661→1684 and 1666→1689, five times; nothing else | **ANCHOR DRIFT** — same class |
| 3 | `gen_phase1_completion_inventory.py --check` | ONE field: `clause_opening`, the span the tool derives from D-231's clause anchor to `**Phase 1 —` — the exact interval the block is ordered into — WIDENS to include it | NOT anchor drift |
| 4 | `gen_phase1_finish_line.py --check` | the same `clause_opening` field, inherited | NOT anchor drift |
| 5 | `gen_phase1p_delegation_bar.py --check` | `mentions_in_ratified_surfaces` for `docs/scoring_model.md` gains `CLAUDE.md:1604` — the ordered text NAMES that document | NOT anchor drift: a NEW MENTION |
| 6 | `gen_reads5_repack.py --check` | `read_documents_whose_naming_count_moved_since_registration` gains `docs/scoring_model.md` | NOT anchor drift: the same new mention |

**★ NO VERDICT, GATE, CUT OR POPULATION MOVES IN ANY OF THE SIX.** Reds 3 and 4 are one changed line
each. Red 5 leaves every verdict field untouched — `form`, `verdict`, `verdict_now`, `movement`,
`decided_by_the_bar` all identical. Red 6 moves the one field the artifact itself declares NOT
frozen: *"a statement about the surfaces as they stand today… still computed live on every run and
can still move"*, and the cause is exactly the mechanism its own `why_it_moved` paragraph describes
— a naming count incremented by a governing-surface edit.

### 2.d Why this is a STOP and not a remap

The dispatch sanctions ONE bounded exception — *"If a check reports an anchor drift caused solely by
this insertion, remap per the drift report's own per-citation practice"* — and states that **any
other new red is a STOP-and-report**. It repeats the bound at step 4 and in its own *what this batch
does NOT do*: no derivation, and no edit to any guard or generator beyond that one remap.

Reds 1 and 2 are inside the exception. Reds 3–6 are not, and the difference is not a technicality:

- **They are not anchor drift, so no per-citation remap addresses them.** A remap re-aims a line
  coordinate; these are a captured quote widening and a new mention.
- **Two of them are the gate-bearing derivations D-436 reserves.**
  `tools/audit/phase1_completion_inventory.json` and `tools/audit/phase1_finish_line.json` carry the
  phase-1 gate and its finish-line cut. Regenerating them under a dispatch that bars derivation
  would be the executing side moving a derived gate on its own judgment.
- **Red 5 writes a new naming into the record the delegation bar grades**, and rules (g) and (i) of
  the decisions-register section reserve delegation-writing to the user.

The governing precedent is the previous batch's own: the ordered [[OI-373]] flip was NOT performed,
because the coherent version of the act needed a mechanism change **D-436** reserves. This is the
same shape, and it is answered the same way.

### 2.e ★ THE STOP IS STRUCTURAL — and what the user is being asked to choose between

Reds 3 and 4 follow from the ordered **position**: any insertion between D-231's clause anchor and
`**Phase 1 —` widens that captured span, whatever it says. Reds 5 and 6 follow from the ordered
**words**: the block names `docs/scoring_model.md`, and it would do so wherever in a governing
surface it were placed. The text is ordered verbatim, so no session may reword it around this.

The candidates, with the batch's recommendation, taken by nobody here:

- **(a) RECOMMENDED — authorize the four non-anchor artifacts to be regenerated alongside the two
  anchor ones**, in the same commit as the `CLAUDE.md` edit. Its whole cost is measured in §2.c: one
  quote field, its inherited copy, one new mention, one live-list entry, and no verdict anywhere.
  This is the smallest act that lands the ruling at the ordered position with the ordered words.
- **(b) Move the insertion point** to after `Three phases, strictly ordered.` — removes reds 3 and 4,
  leaves 5 and 6, and departs from the ordered position.
- **(c) Leave the ruling unlanded** until the tools are amended — which no dispatch has authorized,
  and which leaves `CLAUDE.md` stating a superseded three-phase structure in a mandatory session-start
  read, the exposure eighteenth-stop Ruling 6 exists to close.

### 2.f The tree is left exactly as found

`CLAUDE.md` was restored from its committed blob and hashes identical to it — `61ae1b484c` on both
sides. The sanctioned enumeration then reported **no tracked modification anywhere** in the working
tree. Every artifact regenerated during the diagnosis was restored the same way, and every restore
was independently re-verified by the end-state guard run in §3. **Nothing is lost (#12):** the
ordered block's verbatim text is committed, in the dispatch itself, by this batch's own Task 0.

---

## 3. Both guard-set states

- **START, before the first edit:** `gen_guard_state.py --check` printed **"the guard state
  re-derives"** — 48 guards run, 47 passing, ONE failing (`gen_filing_convention_application.py
  --check`, which is [[OI-372]]), 4 not run, 10 historical records, **no STOP**.
  `gen_guard_classification.py --check` printed **"the guard classification re-derives"**. This is
  exactly the start state the dispatch declares as expected, stale report included by its absence.
- **MID, with the ordered edit in place:** 48 run, **7 failing**, no STOP; the runner reported the
  committed `guard_state.json` STALE against its own run. The six additions are §2.c.
- **END, after the revert:** identical to START in every value and in the runner's own words.
  **Registered expectation E2 — MET:** the batch introduces no red and works none around.

## 4. Every registered expectation, graded

- **E0 — MET.** Four paths at `git diff-tree`; no staging override of any kind.
- **E1 — one limb MET, one limb NOT MET AS WRITTEN.** *Met:* while the edit stood, the truth-half
  sentence occurred in the file exactly once, inside the preserved text, with the superseding block
  standing above it. *Not met as written:* the numstat was **24 insertions and 1 deletion**, not zero
  deletions. **The cause is the ordered position, not the edit:** the heading sentence ends and
  `Three phases, strictly ordered.` begins **on the same line**, so no line-boundary insertion exists
  there and a pure-insertion numstat is unobtainable at that position. Nothing was deleted in
  substance — the removed line's words are preserved verbatim across the first and last added lines,
  the only change being that the single space between `).**` and `Three` became a newline, which
  Markdown renders as that same space.
- **E2 — MET.** Start state and end state identical; no red introduced, none worked around.

## 5. Surfaced findings (D-641, #13, #19) — surfaced, not rowed

The dispatch forbids creating an open-items row, so each of these is stated here and nowhere else.

- **F1 — a zero-deletion expectation is unobtainable at that insertion point.** A future dispatch
  registering one should first establish that its insertion point is a line boundary.
- **F2 — four committed artifacts capture `CLAUDE.md`'s text or its naming counts, so ANY edit to the
  governing document turns them red.** This is a standing property of the record, not a defect of
  this edit, and the next governing-document edit will meet it again.
- **F3 — `reaim_home_anchors.py --check` exits 0 even while reporting drifted anchors** (its own
  `if args.check or not moves: return 0`). In the mid-run it PASSED while printing 11 drifted
  anchors; what caught the drift was `gen_cluster_dispositions.py --verify`. A reader taking the
  guard list at face value would read the anchor check as clean.

## 6. What this batch did NOT do

No `src/` change, no golden, **no test changed, moved or run**, nothing under `tools/corpus/` or
`tools/robust_stop/`, no measurement of the analysis, no design, no repair, no derivation, no
decisions-register entry. **No open-items row created, flipped or discarded.** No preparation-phase
act: no register filter, no rulings sort, no findings ledger, no fact-gate, no curated boot list, no
pruning, no caller-check, no archiving, no mining. No file landed beyond Task 0's four — the 284
newly visible instruction files and the remaining ignored files stay unlanded. No guard or generator
edited. [[OI-372]] and [[OI-374]] stay exactly as found; [[OI-179]] stays OPEN and GATES; D-231 as
it stands, and #8, are untouched.

*Provenance: CC, 2026-08-15, dispatch `cc_instruction_phase_rulings_landing.md`. Task 0 is commit
`1c52098b64`, pushed. **Task 1 has no commit, deliberately.** This report and the batch's full close
ride Task 2's commit, and the END-state guard run reported in §3 was taken TWICE — once immediately
after the revert, and once again at the tree carrying this report, the close and the `STATUS.md`
entries, with the same result both times.*
