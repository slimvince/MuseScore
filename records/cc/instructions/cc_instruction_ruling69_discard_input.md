# CC dispatch — Ruling 69 recorded and applied: a discard verdict becomes an input to the cut, and the gate re-derives

> **Status: ACTIVE DISPATCH, written 2026-08-13 (Cowork), at a verified STOP** — the
> false-statements pass completed and reported no STOP. **One verification gap is declared rather
> than glossed: that report carried NO COMMIT HASHES, so Cowork has not verified the batch at the
> objects the way it has verified every previous one.** Its findings are cited to files and are
> readable; its commits are not checked. **Supply the four hashes with this dispatch's report.**
> Nothing is running.
>
> **Read IN FULL, and read FIRST:** `cowork_rulings_2026_08_13_seventeenth_stop.md` (Ruling 69,
> WHOLE, D-643); `CLAUDE.md`'s principle #10 as amended and the open-items register's non-gating
> declaration with D-676; `open_items/OI-90.md` and its INDEX row.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_ruling69_discard_input.md`. Acts dated
> from the clock; **no positional count anywhere** (D-307, D-432); **cite rulings by number, not by
> date** — the arc's date discrepancy is open and this dispatch does not settle it.
>
> **★ All standing rules as adopted.** D-253 in every dialect, including the path-mapping hazard.
> NO TRANSCRIBED VALUES (D-431). Hold-don't-guess. **Read-only on the analysis: no `src/` edit, no
> behaviour change, no golden, no corpus of scores, nothing under `tools/corpus/` or
> `tools/robust_stop/`, no measurement, no design.** D-231 and #8 stand. **Phase 1's completion
> statement is not written, not drafted and not partially written.** Commit and push per task
> boundary; `origin` only.

## 0a. THE PREMISE LEDGER (#17a)

**FACT — verified by Cowork at the objects.** That `cowork_handoff.md` carries an uncommitted
thirteenth block written by Cowork; CC correctly left it untouched.

**FACT — reported by CC and NOT verified by Cowork:** the four commits of the false-statements
pass, for want of their hashes; the A1–A4 findings and the two worth-test verdicts. **The verdicts
are consumed by Task 2 below, so OI-90's discard record is checked there before it moves anything.**

**ASSUMPTION — each checked BEFORE the act resting on it; a refutation is a STOP.**

- **A1.** OI-90's discard record **carries its finding, its date and its reason** — Ruling 69's
  guard, and amended #10's own requirement. *Check at the record. **If any of the three is absent,
  the verdict does not reach the cut and this is a STOP**, not something to complete by writing the
  missing part.*
- **A2.** The change is to **what the cut CONSUMES**, never to a verdict it publishes. *Check: no
  gating verdict is written, edited or removed by hand anywhere in this batch.*
- **A3.** The movement is reported **both ways** — the population recomputed with the discard input
  OFF must differ from the ON run **only** by rows carrying a conforming discard record. *Check:
  any other mover is a STOP.*
- **A4.** Ruling 65's falsification test runs over the result **in its own terms** — it grades a
  D-438 proposition, which is what a gating verdict asserts, so it transposes here where it did not
  onto a D-639 reach verdict. *Check: if a row the record elsewhere calls inference-bearing loses
  its gate, HALT.*

## 0b. THE TASKS, IN ORDER

**Task 1 — Ruling 69 recorded and entered. FIRST, atomic under the decisions register's rule (c).**
Commit the ruling record together with its register entry, written through the backbone data and
the generator, never by hand-editing a rendered file (rule (d)). **Derive and verify the home under
rules (g)–(k); if two candidates are equally supported, STOP and report both rather than choosing.**
Then `gen_decisions_register.py --check` and `gen_cluster_dispositions.py --verify`, re-aiming any
drifted citation per citation. Commit and push.

**Task 2 — the cut takes discard verdicts as an input (A1, A2, A3, A4).** Change the derivation so a
conforming discard record is consumed where it decides gating, and regenerate. **Report the
movement both ways** and run the falsification test. **Do not adjust anything to produce a
movement**, and **a result where nothing moves is a correct outcome** — it would mean OI-90's record
does not conform, which A1 catches first. Commit and push.

**Task 3 — commit the handoff block.** `cowork_handoff.md`'s uncommitted thirteenth block is
Cowork's; commit it **as it stands, altering nothing.** Commit and push.

**Task 4 — the close.** One `STATUS.md` pointer entry per task, nothing else in that file. Append
the close to `cowork_away_returns.md`. **Report at the objects, and include the four hashes of the
previous batch** so the verification gap is closed rather than carried.

## 0c. WHAT IS DELIBERATELY NOT DONE

**No sweep.** Ruling 69 says how a discard verdict is consumed; it does not say any row should be
discarded, and no row is tested here that was not already tested. **No row is closed** — a row that
stops gating stays open. OI-274's banner half came back WORTH FIXING and is **not** performed here;
it belongs to the ratified `docs/scoring_model.md` pass. **OI-150 is next in the ratified order and
is not started here.** OI-179 stays OPEN and GATES.

## 0d. STOP RULES

Halt with a STOP in `cowork_away_returns.md` if: OI-90's discard record lacks finding, date or
reason; any gating verdict would move by hand; the both-ways recomputation shows a mover carrying no
conforming discard record; the falsification test removes a gate from a row the record calls
inference-bearing; two homes are equally supported for the entry; or a guard goes red for a cause
that is neither this dispatch's own edits nor already recorded — the two standing reds are recorded
and are not that.

---

*Provenance: Cowork, 2026-08-13. Ruling 69 was taken on a surface carrying four mutually exclusive
options with their principled costs and objective ratings, and was ruled as a class rather than for
the row that forced it. Self-check run before release (D-434).*
