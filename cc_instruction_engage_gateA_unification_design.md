# CC Instruction — Engage arc #3: Gate A promotion unification — design/scoping pass (read-only)

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** The engage arc's outstanding restructuring, taken first per the
> order-of-operations principle (restructuring → architectural design → algorithmic completion → then
> inference-fixing). The user ratified this ordering by principle: Gate A unification is the prerequisite
> that cleans the carried-alternatives surface Layer 5's engagement will build on, so it comes before the
> Layer 5 design; the fine-grain override's redesign lands later as a consumer of that same surface (and is
> deliberately NOT built now — building its own uncertainty mark ahead of the shared mechanism would
> duplicate it).
>
> **This is a DESIGN + SCOPING pass — read-only. NO `src/` change, NO corpus write, NO build, NO push of a
> behavior change.** The unification itself is a **user-ratified behavior change** (it moves the carried
> alternatives on ~36 Baroque scores — a load-bearing, user-visible output surface), so it is a *separate*
> ratified build event. This dispatch produces the characterization, the measured blast radius, the unified
> design, and the verification plan — the ratification surface.
>
> **Grounding (the established finding, re-confirmed at HEAD — build on this fact, not assumption):** Gate A
> is **winner-inert everywhere but alternatives-active on ~36 Baroque scores** — its `std::swap` promotion
> and the fallback `push_back(buildResult)` promotion produce the **same winner with different carried
> alternatives**. Because the carried alternatives are a **load-bearing output surface** (Layer 5's overrides
> select among them; they are user-visible), "same winner, different alternatives" **is** a behavior change —
> which is why Gate A's retirement was held pending exactly this "promotion machinery unifies (one path, one
> carry)" step. The **evidence-method rule** from that finding is binding here: inertness/impact is measured
> on the **FULL output surface (winner AND alternatives), never the winner alone.**
>
> **Read first (do NOT summarize from memory):**
> - The Gate A / promotion finding in `cowork_stage5_fitter_design.md` (the "GateA byte-identity ruling",
>   ~§ observation block near the family-2 closure) + the carried-alternatives carry contract it cites.
> - The two promotion sites + the duplicated builder, at HEAD:
>   `chordpostpasses.cpp` (the `std::swap(results[0], results.back())` promotion, ~L196-197; the
>   `buildResult` lambda ~L129 whose comment says it "mirrors the buildResult lambda in
>   applyPostScoringGates / analyzeChord"); `harmonicfunctionlayer.cpp` (the `push_back(buildResult(rc))`
>   promotion, ~L516/527/545); and `applyPostScoringGates` / `analyzeChord` in `chordanalyzer.cpp` (the
>   third `buildResult` mirror).
>
> **Current state:** HEAD `71c0be114a`, branch `master`, fork-only, ahead 0. Both stops green (batch
> 52/24/52; robust sandwich identity-PASS). Corpus `c50002fee1` (the pinned, non-stale corpus).
>
> **VS Code bash rules:** append `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read
> files** — use the file tools.

---

## Task 0 — state check
HEAD/branch/ahead-0; batch 52/24/52 set-diff empty; corpus fingerprint `c50002fee1`. Report.

## Task 1 — characterize the duplication at the source (build on knowledge)
Describe, code-grounded, the promotion machinery as built:
- The **two promotion idioms** — the `std::swap`-to-front promotion vs the `push_back`-then-rely-on-order
  promotion — where each runs, and what carried-alternatives ordering/content each produces.
- The **duplicated `buildResult` builder** across the three sites (`chordpostpasses.cpp`,
  `harmonicfunctionlayer.cpp`, `applyPostScoringGates`/`analyzeChord`): what each copy builds and where they
  diverge (if at all).
- **Why the alternatives differ** on the affected slices — the mechanical cause of the ~36-score divergence.

## Task 2 — measure the blast radius on the FULL output surface (the binding rule)
Read-only. Enumerate the **exact set of affected scores/slices** (expected ~36 Baroque) and, per affected
slice, the **carried-alternatives delta** (winner/root confirmed unchanged; the alternatives list before vs
after unifying onto a single path). Use the existing measurement from the Gate A finding if it is recorded;
otherwise a read-only comparison. Report:
- Confirmation that the **winner (and therefore the root) is unchanged on every score** — so both regression
  stops (root-based) stay green by construction.
- The **alternatives delta** characterized (which slices, what changes, and whether the change is
  cosmetic ordering or a content difference in the carried set).
- Whether the delta reaches the fullspine / dump surface (so the build event knows if any snapshot golden
  moves).

## Task 3 — design the single unified promotion path (total unification, in-layer)
Design **one promotion path producing one carry** that both call sites use — removing the duplicated
`buildResult` and the two idioms. Ground the choice of the **correct unified carry** in the carry's purpose
(Layer 5 selects among the carried readings, so the carry must be the correct/complete alternative set) — do
not pick an idiom arbitrarily; state which carry is correct and why, grounded at the code/contract. Keep the
change **in Layer 4** (the promotion/carry machinery's layer) — nothing cross-layer. State how Gate A
becomes truly inert (winner AND carry identical across both paths) and is therefore removable.

## Task 4 — the build-event plan + the ratification surface
State, for the *separate* ratified build event (not built here):
- What the refactor touches (the unified builder + the two call sites; Gate A removal), all in Layer 4.
- The **verification on the full output surface:** winner+alternatives byte-diff across **all** scores ×3
  presets (expected: identical except the ~36-score alternatives delta, explained per case); both stops
  green (roots unchanged); suites 1101/53+4skip/11; any snapshot golden that moves (with the intended-effect
  justification) or confirmation none moves.
- That the ~36-score **alternatives delta is the user-ratification surface** (every behavior change is
  user-ratified as one revertible, provenance-stamped commit) — enumerated and explained for the user to
  ratify at the build event.
- The reuse-vs-new + what-retires line (Gate A retires; the duplicated builder collapses to one).

## Task 5 — doc + report + fold + push
1. **Design doc** `cowork_gateA_unification_design.md` (force-add): Tasks 1–4.
2. **Report** `cc_engage_gateA_unification_design_report.md` (force-add): what landed, grounding sources,
   the affected-score enumeration, all SHAs.
3. **Sandwich (trivial — read-only):** no `src/` change; both stops untouched; suites unchanged (no build).
4. **Fold** (`docs(cowork):`): `STATUS.md` · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`
   (engage-arc observation) · this instruction (force-add).
5. **Push fork-only** (`git push origin master`) — the fork-only HARD STOP: never toward
   `upstream`/`musescore/MuseScore`.

## STOP conditions
- Any `src/` change, corpus write, build, or behavior change (the unification is the LATER ratified event).
- Measuring inertness on the winner alone instead of the full output surface (winner + alternatives) — the
  binding evidence-method rule.
- Choosing the unified carry by assumption rather than grounding which carried set is correct at the
  code/contract.
- Any push/PR/merge toward `upstream`/`musescore/MuseScore` (the `cfc7eb5e39` distribution HARD STOP).
- `characterise` ≠ 52/24/52 or the robust sandwich not identity-PASS at close.

## Acceptance
The two promotion idioms + the triplicated `buildResult` characterized at source ✓ · the affected scores
enumerated with the winner-unchanged confirmation and the alternatives delta on the full output surface ✓ ·
the single unified promotion path designed, in Layer 4, with the correct carry grounded (not assumed), and
Gate A's removal specified ✓ · the build-event verification plan + the ~36-score ratification surface ✓ ·
design doc + report + fold with SHAs ✓ · no src/corpus/build/push-of-behavior-change; both stops green;
pushed fork-only ✓.

*Cowork, 2026-07-06. Engage arc #3. Read-only restructuring design (the order-of-operations first step). On
CC's report: Cowork verifies at objects → presents the unification + ~36-score alternatives-delta ratification
surface to the user for the build event.*
