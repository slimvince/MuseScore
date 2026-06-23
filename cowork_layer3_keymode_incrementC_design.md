# Layer 3 / Increment C — the KEY/MODE SEQUENCE DECODER — (⛔ SUPERSEDED → folded into the Layer-3 doc)

> **★ SUPERSEDED 2026-06-22.** "Increment C" is a unit of *delivery*, not architecture, and should not have its own
> architecture document. Its content — the decoder that implements the key/mode layer — now lives, increment-agnostic,
> in the formalized **Layer-3 layer document `cowork_layer3_keymode_design.md`** (the building-block / runtime / data
> / decisions sections). The build sequencing (the A/B/C steps) lives in the delivery plan
> `cowork_layer3_keymode_impl_design.md`. This file is retained only for history.

# (superseded) Layer 3 / Increment C — the KEY/MODE SEQUENCE DECODER

> *(original content below — see the Layer-3 doc for the live version)*

## 1. Introduction & purpose
**This component decides the key/mode of a passage as one coherent sequence over time, instead of guessing each
region's key in isolation.** Today the analyzer resolves a key/mode **per region**, locally, smoothed only by a
small anti-flip nudge — and that locality is the source of the two dominant key/mode errors we measured: confusing
**relative major and minor** (they share every note, so one region can't tell them apart) and **missing or
inventing modulations** (a brief borrowed chord looks like a key change to a region that can't see the music stay
home). Deciding the whole sequence together fixes that class. **Scope — in:** assign each slice a key/mode (+
alternatives + confidence). **Out:** chord symbol, function, cadence detection (Layer 4/5; cadences are
function-level, gated Stage 5).

## 2. Constraints
- **Key/mode only;** evidence = pitch-class content + tonic emphasis (cadence-free, no chord/function input —
  dependency order).
- **Output is a confidence-bearing path:** commit where decisive, **flag** the genuinely ambiguous (relative pairs,
  modulation) with ranked alternatives — never force-finalize (the gated Stage-5 joint step resolves the residual).
- **Frozen upstream** (L1/L2); **behavior changes** here (NOT byte-identical) — validated by metric, snapshot
  goldens refreshed after verified-correct.
- **Any score / size / style** (modal-complete); **incremental** (R2) and **scalable** (R1, uses indexed queries);
  **context-extensible** (R3 — the first layer to pull earlier-layer context on demand).

## 3. Context & scope (external view)
*Proposed; the read-only audit verifies the real call site / refines signatures.* New module
`composing/analysis/key/keymodesequence.{h,cpp}`.
**Imports:** `notemodel::NoteModel` (L1, emission windows via indexed `overlapping`); `slicing` slices (L2);
`KeyModeAnalyzer` (existing — the local-fit scorer, reused unchanged); `KeyModeSequencePreferences` (new tunables) +
`KeyModeAnalyzerPreferences`. **Does NOT import** chord/function/cadence or any resolved-key feedback.
**Exports (public API):**
```
struct SliceKeyMode {                 // one slice's decision
  int sliceIndex;
  KeyModeAnalysisResult chosen;             // decided key/mode (tonic, mode, score)
  std::vector<KeyModeAnalysisResult> alternatives;   // ranked runner-ups
  double confidence;                        // path-margin
  bool   uncertain;                         // low-confidence flag
};
class KeyModeSequenceDecoder {
  static std::vector<SliceKeyMode> decode(const std::vector<Slice>&, const NoteModel&,
                                          int keySigFifths, const KeyModeSequencePreferences&);
  static std::vector<SliceKeyMode> redecodeRange(/* …, */ int first, int last,
                                          const SliceKeyMode& leftPin, const SliceKeyMode& rightPin);
};
```
**Consumers:** `regionanalyzer` (replaces its per-region `resolveKeyAndModeRanked`); Layer 4 reads `chosen` as a
diatonic prior; the gated Stage-5 step reads `alternatives` + `uncertain`.

## 4. Solution strategy
Lay the slices left-to-right; at each, the existing scorer gives every candidate key/mode a **local-fit score**.
Choosing one key per slice traces a **sequence**; pick the single best one = max *total local-fit* − *total change
cost*. The change cost makes staying cheap and switching pay (more for distant keys, most for the relative pair) —
so a brief excursion stays home and a sustained one modulates, and the relative-major/minor choice is settled by
whole-stretch coherence. Compute it with **Viterbi** (the standard one-pass best-sequence algorithm). This is the
literature-standard HMM treatment of local key + modulation, on our slice grid, reusing our scorer.

## 5. Building-block view (static / internal structure)
A four-stage pipeline inside `decode()`:
1. **Emission** — per slice, build a small pitch-context window (slice ± a beat or two, via the note model) and call
   `KeyModeAnalyzer::analyzeKeyMode` → score per (tonic × mode). **Prune** to top-K ∪ the running incumbent key(s)
   (incumbent kept even when not top-K — so a transient slice can't drop the home key).
2. **Trellis** — (slice × surviving candidate); edges carry the change cost.
3. **Viterbi forward pass** — DP `best[i][s] = emission(i,s) + max_{s'}(best[i-1][s'] − changeCost(s'→s))`,
   backpointers; O(T·K²).
4. **Backtrace + outputs** — recover the sequence; per slice derive `alternatives`, `confidence` = margin of the
   best path vs the best path forced through a different key here, and `uncertain` when that margin is low.
**Change-cost function:** `0` if stay; else `baseSwitchPenalty + fifthsDistance·w + (relativePairBarrier if relative
major/minor)`. **Reach-back (R3):** an unsettled opening triggers a backward range-widen request to L1/L2.
**Sub-range re-decode (R2):** `redecodeRange` runs the same DP over `[first,last)` with the two boundary states
pinned.

## 6. Runtime view (scenarios)
- **Stable key:** emission favours one key; stay-cheap keeps it → one key throughout.
- **Relative-pair ambiguity:** per-slice scores near-tied; the whole-stretch tilt + the high relative barrier pick
  one consistently (low `confidence` ⇒ `uncertain` at the seam).
- **Brief tonicization:** a few slices score the dominant higher, but the switch cost isn't repaid over so few
  slices → stays home.
- **Real modulation:** the new key persists; the accumulated local-fit repays the switch → modulates.
- **Selection mid-passage:** the opening key area never stabilises → reach-back widens the range until the home key
  is in view.
- **Score edit:** `redecodeRange` re-decodes the dirty neighbourhood with pinned boundaries, not the whole piece.

## 7. Data design
`SliceKeyMode` (§3) is the output unit per slice. Internals: the **candidate set** per slice (≤ K + incumbent), the
**Viterbi DP table** `best[T][K]` + backpointers, and `KeyModeSequencePreferences` (pruning K, change-cost
magnitudes, emission-window size, flag threshold). `chosen`/`alternatives` reuse the existing `KeyModeAnalysisResult`.
Confidence is a path-margin (best vs best-different-key-here), not the per-slice emission sigmoid.

## 8. Crosscutting concepts
- **Confidence & uncertainty** — every slice carries a confidence + flag; ambiguity is recorded, not hidden (feeds
  Layer 4's prior and the gated joint step).
- **Annotate-don't-transform** — slices/notes unchanged; the path is an annotation; alternatives retained (revisable).
- **Performance / incrementality** — Viterbi is linear in slices; the indexed emission queries (Increment A) keep it
  scalable; `redecodeRange` bounds edit cost.
- **Determinism**; **the written key signature is a weak hint, not truth**.

## 9. Architecture decisions
- **Whole sequence vs per-region argmax.** Chosen: sequence — locality is the measured ceiling for relative-pairs +
  modulation.
- **Viterbi vs beam.** Chosen: Viterbi over a **pruned** lattice (global-optimal, linear); beam only if pruning is
  insufficient (it shouldn't be).
- **Dedicated decoder vs reuse `ChordPathDecoder`.** Chosen: dedicated — the chord decoder is chord-specific (audit).
- **Change cost = stay-cheap + fifths-distance + relative-pair barrier.** Alt: a flat hysteresis (today). Chosen:
  the literature HMM shape (key-distance + high self-transition); magnitudes start from today's hysteresis values.
- **Confidence = path margin vs per-slice emission gap.** Chosen: path margin — the path is the decision; near-tied
  paths are exactly the flagged residual.
- **Keep the incumbent in the candidate set always.** Rationale: lets a transient slice not drop the home key (the
  passing-key mechanism).

## 10. Quality & testing
- **Synthetic decoder unit tests** (hand-built emission/transition): single-key → one key; relative-pair tilt →
  correct + consistent; brief excursion → stays; sustained excursion → switches; near vs remote switch → near.
- **Note-model fixtures** — the §6 scenarios incl. reach-back.
- **Property tests** — `redecodeRange` (pinned) == the slice of a full `decode` (incremental consistency);
  determinism.
- **Directional corpus signal** — the Increment-B held-out harness, C-vs-pre-C (§11/grading): rotation/relative-pair
  defects down.
- **Coverage + safety** — full branch coverage; both suites; snapshot goldens refreshed only after verified-correct;
  **dual-preset BIR no-regression hard stop.**

## 11. Risks & technical debt
- **Grading is directional, against a moving "before."** The "before" = the current per-region resolver that
  Increment B baselined (held-out Baroque 87.3% / Jazz 61.5%); compare C-vs-pre-C on the same harness. Numbers + the
  metric definition are **provisional** — meaningful comparison is the finished pipeline.
- **Defect vs ground-truth limitation** — many Jazz "misses" are defensible **modal** readings (`G-mixolydian`) the
  major/minor GT can't represent; do NOT optimise those away.
- **Deferred tunables** — pruning K, change-cost magnitudes, emission window, flag threshold (audit / Stage-5 fit).
- **The relative/modulation residual is left flagged for the gated Stage-5 joint step** (key↔chord), not solved here.

## 12. Glossary
**Key/mode** — tonal centre + mode (`C-major`, `F-mixolydian`). **Sequence (path)** — the chosen key/mode per slice
across time, picked as a whole. **Emission** — a slice's local-fit score per candidate (the `KeyModeAnalyzer`
output). **Transition / change cost** — the penalty for switching key between slices. **Viterbi** — the standard
one-pass algorithm for the single best sequence given emissions + transition costs. **Path margin** — best path vs
best-different-key path = the confidence. **Directional grading** — judged by improvement vs the pre-C resolver, not
a fixed bar. **Reach-back (R3)** — pulling earlier-layer context beyond the selection on demand.
