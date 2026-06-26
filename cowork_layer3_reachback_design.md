# Architectural Layer 3 — reach-back (request extension for opening context) — detail design (Phase 3)

> **Status: DRAFT for sign-off. Read-only design — no code.** Phase 3 of the L1–L3 stabilization plan, completing the
> bounded-context model: when the **opening of the user's selection has no settled key**, Architectural Layer 3 asks
> Architectural Layer 1 to **extend earlier** until the prevailing key is in view, then re-slices and re-decodes over
> the enlarged span. This is **algorithmic completion of the designed bounded-context contract**
> (`cowork_bounded_context_design.md`) — *not* inference-problem-fixing. It is **byte-identical on the corpus**, because
> a whole-score stem has nothing before its start to reach back to (the extend hits the score boundary immediately), so
> reach-back **never fires** there; the new behaviour is exercised only by partial-selection tests.

## 0. CORRECTION after §7 verification (production is whole-score today — read this first)
The §7 read-only verification (CC, cited in `cc_layer3_reachback_verify_report.md`) found that the production
orchestrator `analyzeRegions` (`regionanalyzer.cpp:488`) **builds whole-score on every path** (`build(score)`,
1-arg) **regardless of the `[startTick, endTick)` range** — the range only drives which regions are *emitted*, not
what is analysed. So **none of the bounded-context model is engaged in production**; the decode is always whole-score.
This corrects two things below: §2 step 1's "as today" is wrong (there is no selection-scoped decode today), and
reach-back can only fire once *something* builds over the selection.

**Phase-3 scope (user-ratified, option A):** build reach-back **as a tested capability** — a **selection-aware
orchestration path** (build over the selection → slice → decode → reach-back loop → output-filter) — with the
**production `analyzeRegions` left untouched at whole-score**, so the build is **byte-identical on every gate** and the
new behaviour is exercised only by partial-selection fixtures. The capability must not **duplicate** the orchestration
(unification): either a parameter on `analyzeRegions` defaulting to whole-score (production path unchanged) or a thin
sibling that shares the build/slice/decode calls — the build decides, gated on byte-identity + the unification ledger.
**The decoder is key-only: `keymodeseq::KeyModeSequenceDecoder::decode`** (chord is production-R0/diagnostic; a
separate `ChordPathDecoder` exists — do not confuse).

**The ENGAGEMENT is a separate, deferred, behaviour-changing step — NOT Phase 3.** Actually switching production to
selection-scoped analysis (build over the selection, drop context regions) is byte-identical on the corpus (whole-score
range = degenerate) but **not automatically** on the live bridge / snapshots if a live caller passes a sub-range
(`notationharmonicrhythmbridge.cpp:131` must be checked first). That switch + its snapshot/notation ratification is the
"selection-based working model", deferred.

## 1. Where reach-back lives (single responsibility)
The reach-back loop spans three layers — Architectural Layer 1 (`extend`), Architectural Layer 2 (re-slice),
Architectural Layer 3 (re-decode) — so it lives in the **selection-aware orchestration path** (§0), which drives all
three (the analysis
driver that builds the model, slices it, and calls the decoder), **not inside the decoder**. The decoder stays a pure
function of the slice sequence it is given (`decode(slices, model, …)`); the orchestrator decides *whether to extend*
and re-invokes the pipeline. This keeps the decoder single-responsibility and matches the bounded-context contract:
*the requesting layer owns the extend → re-infer → re-check loop; Architectural Layer 1 supplies; the decoder infers.*

## 2. The loop (extend → re-slice → re-decode → converge) — on the selection-aware path (§0), production untouched
1. **Build over the selection** (`build(score, selStart, selEnd)`), slice, and **decode once** over the selection's
   slices. (This is the new selection-aware path — *not* today's whole-score production decode, which stays as-is.)
2. **Trigger:** if the **opening** of the selection has **no settled key** (Section 3), enter the loop.
3. **Extend earlier** by one increment — `model.extend(Earlier, incrementTicks)` (Phase 1a) — the increment is
   Architectural Layer 3's natural unit: **a measure**, converted to ticks via the score's time signature
   (`cowork_bounded_context_design.md` §3.8/§3.9; ticks at the L1 boundary).
4. **Re-slice** the enlarged loaded span (Phase 2 — pure; the new earlier region gains slices, the seam edge extends).
5. **Re-decode** the enlarged slice sequence (a **fresh** decode — the bounded-recompute is "as if first run", forward
   only: the request went *down* to L1, inference flows *up/forward* L1→L2→L3).
6. **Re-check convergence** (Section 3). If converged → stop. Else if the **hard bound** or the **score start** is
   reached → stop. Else → extend again (step 3).
7. **Output only the selection's slices.** The reached-back context slices anchor the carried-in key but are **not**
   emitted (`cowork_bounded_context_design.md` §2: output = selection; context = evidence).

## 3. The trigger and the convergence stop (no amount-guessing)
Per the contract (§3.5–§3.7), Architectural Layer 3 never guesses *how far* to reach — it extends until its **own
output converges**.
- **Trigger (enter the loop):** the selection's **leading-edge slice(s)** carry **no settled key** — i.e. the
  decoder marks them "uncertain" / low sequence-margin at the opening (it had no earlier context to establish a key).
- **Convergence stop (the principled criterion):** extend until the **key assigned to the selection's leading-edge
  slices stops changing** as more earlier context is added. That is self-validating — once a confident earlier key is
  established, the change-cost/decay means reaching further back will not move the leading-edge key.
- **Domain proxy (cheaper than re-checking the whole opening each step):** *a settled, stable prevailing key is in view
  in the reached-back region* (a committed, non-"uncertain" key for a run of context slices). Validated **once, in
  design**, to imply leading-edge convergence; the loop uses the proxy, the equivalence test (Section 5) confirms it.
- **Hard bound + score start:** a maximum reach (a small number of measures — a setting) and the score's first tick
  both terminate the loop. These are **safety caps for "never settles," not the needed amount.**

## 4. Byte-identity on every gate (why it stays green)
**Production `analyzeRegions` is untouched (whole-score), so the corpus, snapshots, and notation are all byte-identical
— the reach-back capability is not on the production path** (§0). Two independent reasons it cannot perturb production:
(a) the selection-aware path is exercised only by partial-selection fixtures; and (b) even if invoked on a whole-score
span, the selection *is* the whole score, so its opening is the score start, `extend(Earlier, …)` clamps on the first
call (`boundaryReached`), the loop exits with **no extension**, and the decode is over exactly today's slices —
reach-back **cannot fire on whole-score**. Byte-identity (any corpus/snapshot/notation movement) is the hard gate; the
engagement that would actually change production output is the deferred step (§0), not this.

## 5. Invariants & tests (the gate)
1. **Degenerate byte-identity:** whole-score corpus + both suites + snapshots **unchanged** (reach-back never fires).
2. **Reach-back fires and terminates:** on a partial selection whose opening is unsettled, the loop extends, the
   leading-edge key gets anchored by the carried-in context, and it stops (convergence, or hard bound, or score start
   with `boundaryReached`).
3. **Convergence / equivalence (determinism):** the final analysis of the selection is **independent of the increment
   size** — reaching the same converged span in one big step or several small ones gives the same in-selection result
   (this is also the check that the Section-3 proxy really implies convergence).
4. **Selection at the score start:** opening = score start → reach-back requests, L1 reports the boundary, L3 proceeds
   with what exists (no earlier context to want) — no error, graceful truncation.
5. **Output = selection only:** context slices are evidence, never emitted as results.

## 6. What is deferred
- **Incremental re-decode** (only re-running the affected leading-edge slices instead of a full re-decode) is a
  performance optimisation — **deferred**, like the L1 incremental index and the L2 incremental re-slice. The interim
  re-decodes the enlarged sequence fresh (pure; correct).
- The convergence **proxy tuning** (how stable is "stable") is a setting; its *calibration* is Phase-B precision work,
  not built here — here it is set to a safe default that the equivalence test (Section 5.3) validates.

## 7. What CC verifies read-only BEFORE building (ground the design — do not assume)
- **The current decode orchestration:** where the model is built, sliced, and the decoder invoked (the analysis driver
  / region analyzer path), and that the decoder is a pure function of the slice sequence (so the loop can wrap it
  without touching the decoder). Confirm the exact seam.
- **The Phase-1a `extend(Earlier, ticks)` + `boundaryReached`** behave as Section 2 assumes (verified at build of
  Phase 1a; re-confirm the signatures).
- **That no production path currently feeds the decoder a partial span** (so reach-back is genuinely new behaviour,
  inert on every existing caller — as Phases 1–2 established).
- **The leading-edge "no settled key" signal** the decoder already exposes (the "uncertain"/sequence-margin at the
  opening) — confirm what is available to use as the trigger, so the trigger reads an existing signal, not a new one.
- Report findings; if any seam differs from this design, surface before building (as the Phase-2 verification did).

## 8. Spec & delivery
- The Architectural Layer 3 spec already frames reach-back as an extension request (stop = prevailing key in view,
  hard bound); on build it gains the as-built loop location and the convergence proxy; build state to the delivery
  notes.
- **Phase 3 (the interim full-re-decode loop)** is the buildable unit; the incremental re-decode is a separate,
  deferred perf step. Each is its own gated Claude-Code instruction; the §7 read-only verification precedes the build.
