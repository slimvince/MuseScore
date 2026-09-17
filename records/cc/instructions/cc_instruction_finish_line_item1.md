# CC dispatch — move the stray dumps, row the guard, and start the finish line at item 1

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_finish_line_item1.md`.
>
> **★ THREE ACTS AND NOTHING ELSE.** D-641 governs: a finding that bears on the analysis, its inputs
> or an instrument a measurement depends on is **surfaced**; anything else is **rowed and left — no
> wave, no fix.** Do not repair what you find.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/`, no goldens, no corpus, no
> behaviour change, no fix to inference, no design. Phase 1 under D-231.
>
> **★ THE FINISH LINE IS THE SCOPE.** Nothing outside `tools/audit/phase1_finish_line.json` gets work
> here, and adding to it needs a user ruling.

## 0a. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04.** The six `*_root_fail_cells.txt` dumps are **moved out of
  `tools/robust_stop/`** to a scratch location — not deleted (#12), not committed as reference. The
  directory then holds only what gate block (A) names. **The move is measurement-neutral and the
  reason is recorded, not asserted:** the consumer reads the reference **by explicit filename**.
- **R2 — RULED, same act.** The intermittently-failing guard is **rowed and left** — apparatus under
  D-641, no fix, not surfaced. **This corrects a false statement in Cowork's previous dispatch**,
  which described it as already rowed when no row existed.
- **R3 — RULED, same act.** Work the finish line, **starting at item 1**: classify its entries by the
  route that would close each, execute the unambiguous re-homings, and report the residue. **Item 1
  only.** Do not start item 2.

**None of R1–R3 authorizes a fix to the analysis, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session:**

- **F1.** `tools/robust_stop_diff.py:189-190` reads the reference by explicit filename —
  `f"{preset}_variant_b_root_fail_runs.txt"` — with no glob. The `_cells.txt` dumps cannot be read by
  it.
- **F2.** `tools/robust_stop/` currently holds the six `*_root_fail_cells.txt` files beside the
  committed reference (`*_root_fail_runs.txt`, `*_mapping.json`, `summary.json`, `manifest.json`).
- **F3.** D-231's clause carries **C4**: *"so that conformance is thereafter measured against the
  specifications themselves — the decisions register remains the status ledger … never the
  conformance reference"* (`CLAUDE.md:1117-1119`).

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That `tools/a8_rebaseline_measure.py` — the other consumer of that directory — also reads by
  explicit filename. **Cowork checked one consumer, not both.** → **Task 1.1**; if it globs, **STOP**
  and do not move anything.
- **A2.** That finish-line item 1 is *"home document named in no user-ratified surface"* at the size
  the report gives. Cowork has this from the report table, **not from the artifact.** → **Task 3.1**.

## 1. Task 1 — Move the dumps (R1)

**1.1 Discharge A1.** Establish how **every** consumer of `tools/robust_stop/` reads it — by name or
by pattern. **If any reads by pattern, STOP and report**; the move would then not be neutral and the
question changes.

**1.2** Move the six `*_root_fail_cells.txt` files out of the directory, preserving them. Record at
the destination what they are and which measurement produced them.

**1.3** Record on OI-337 that the move happened and **why it is measurement-neutral** — F1 plus A1's
result, not an assertion. Re-run `robust_stop_diff.py` against the committed reference and report that
it is unaffected.

## 2. Task 2 — Row the guard (R2)

Open a row for the guard that failed once and passed on every later run with no intervening write,
cause not established. **Classify it apparatus under D-641, and leave it.** Record that Cowork's
previous dispatch asserted it was already rowed and that this was false.

## 3. Task 3 — Finish-line item 1 (R3)

**3.1 Discharge A2** at `tools/audit/phase1_finish_line.json`: report item 1's actual definition and
population.

**3.2 Classify every entry in item 1 by the route that would close it**, from the entry and its
document:

- **RE-HOME** — an owning specification exists and the decision belongs in it. **This is the preferred
  route and C4 is why (F3):** a delegation makes a document a home, but re-homing puts the decision
  *in* the specification, which is what "conformance measured against the specifications themselves"
  requires. A decision reachable only by following a pointer satisfies the letter and defeats the
  purpose.
- **NEEDS A DELEGATION** — the decision genuinely belongs to a contract document rather than to a
  layer specification. **Only the user may write one**; collect these and do not draft wordings unless
  the document is already a home for a related concern.
- **NO HOME EXISTS** — neither route is available. Report; propose nothing.

Publish the classification as a generated artifact with the reason per entry.

**3.3 Execute the RE-HOME class**, where the owning specification is unambiguous. Each homing writes
the decision into the specification **in that specification's own voice, with its defense**, and
re-takes the entry's verbatim and home, former preserved (#12).

**Where the owning specification is not unambiguous, do not guess — report it in the residue.**

**3.4** Report the residue by class. **Do not start item 2.**

## 4. Task 4 — Close

Guards at the committed tree with the list `gen_guard_state.py` derives; report and **fix none**.
Re-aim any anchor this wave's edits drift, per citation. Verify what is committed through
`tools/audit/changed_paths.py`. Run `tools/audit/process_check.py` over this dispatch. `STATUS.md`
gains one POINTER entry.

**Anything found outside these three acts is rowed and left under D-641**, unless it bears on the
analysis, its inputs or a measurement instrument — in which case it is **surfaced, not acted on.**

## 5. Accepted outcomes

**A1 finding a pattern-reading consumer is a STOP** and nothing moves. **Item 1's RE-HOME class being
small is a result** — it would mean most of the 94 need a delegation and the route is the user's.
**Reporting an ambiguous owning specification is correct**; guessing one is the failure.

## 6. Self-check (D-434) — run by Cowork before release

- **Ruling ledger.** Three rulings; R2 records a false statement in Cowork's previous dispatch rather
  than quietly correcting it.
- **#17(a).** Three facts read at the objects. Two assumptions — A1 because Cowork checked one
  consumer of two, A2 because the item-1 figure came from a report table rather than the artifact.
- **D-641 applied.** Task 2 rows an apparatus finding and leaves it; Task 4 states the rule for
  anything else this wave meets.
- **Principles.** C4 — the re-home route is preferred and the reason is stated. #12 — dumps moved, not
  deleted; former verbatims preserved. #19 — the move's neutrality is established, not asserted.
