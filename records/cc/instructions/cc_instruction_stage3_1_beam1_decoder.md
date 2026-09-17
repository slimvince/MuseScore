# CC Instruction: Stage 3.1 — the beam-1 decoder skeleton (byte-identical, the hard gate)

## Context

First implementation step of the ratified design (`docs/decoder_design.md`,
`e2bdef7e13`). Deliverable per roadmap 3.1 and design §12: the lattice/path-state
decoder lands **behind the quality-level knob with beam-1 (level 0) as the default**,
**byte-identical on every output**, cache-READY but with **no caching** (Q7: decode-once
is 3.1b), **no signal migration** (3.3), **no gate changes** (3.4). The oracle and
segmentation are untouched throughout.

**This is the strictest gate of the project: a single changed byte anywhere = stop.**
Not "investigate and refresh" — STOP, reconcile the decoder to the old behavior, or
report why it can't be. Golden refreshes are forbidden in this instruction.

Mandatory reads: `docs/decoder_design.md` §§2–5, 9, 12 (the ratified spec — deviations
from it require re-ratification, i.e. stop and report); `docs/scoring_model.md` §3
(FP tie policy — the tripwires); the Stage-5 path-state mapping table (design §5).
Standing rules (trust model 1–4) apply.

## Task 1 — Implementation plan (report §1; brief, then proceed)

The design leaves the concrete code shape to you within its constraints. Resolve and
write down (≤1 page) before coding:
1. Where the decoder type lives (suggest `analysis/function/` or a new
   `analysis/decode/` — justify) and its API: path-state struct (design §5 table),
   node/candidate representation at beam 1 (= the existing `results[]`), the
   quality-level knob on `ChordAnalyzerPreferences` (design §9; enum or int — justify;
   default = level 0).
2. **The interleaving reality**: the current Pass-1 loop interleaves analysis with the
   inline same-root merge, and Pass 2/2b/3 consume committed identities. At beam 1 the
   decoder must preserve this exactly — i.e. the beam-1 decoder is a *re-expression of
   the existing commit chain* (path-state object replacing the threaded
   `ChordTemporalContext` + `advanceTemporalContext` calls at all three commit sites),
   NOT a separate post-pass over a finished stream. Confirm this reading of design
   §1/§4(4) or stop and argue the alternative.
3. How cache-readiness is expressed WITHOUT caching (e.g. the decode entry is callable
   over a region range and returns the path object — nothing stores it yet).
4. The exact arithmetic-order guarantee: where in your structure the per-bass score is
   computed, and why it is the same expression in the same order
   (`(basisIndep + rcb + basisDep) × cf × af + wComplete + wSeq [+ wDim] [+ steps]`).

## Task 2 — Implement

Per the plan. Constraints restated: forward signals stay on the cold lookahead
(AWKWARD-3); rcb stays inside the multiply (AWKWARD-1); per-node sequence stays
`applyHarmonicFunction` → `applyIter8691Pedal` → `applyPostScoringGates` → commit
gate-corrected identity → inline merge; tie comparator untouched; the 1a-F2/F5
artifacts reproduced. `advanceTemporalContext` may be absorbed/wrapped — its OBSERVABLE
effect must be identical (the Step-1/2 fields keep being populated identically even
though nothing reads them).

## Task 3 — Tests

1. **Equivalence test** (the 2.3 agreement-invariant pattern): legacy-expression vs
   decoder on the catalog + musicxml fixtures — winner identity AND score, every
   region. If the legacy path is gone after the refactor, the equivalence test pins
   decoder-at-level-0 against the *recorded* pre-refactor outputs of those fixtures
   (state which form you used).
2. Quality-knob default pin (level 0 out of the box; levels >0 rejected/no-op for now
   — pin whichever you implement).
3. The existing FP canaries (1.7 near-tie, Δ=+7b, bwv320-class pins) are the tripwires
   — they must pass UNMODIFIED.

## Task 4 — The verification gate (design §4, all five items)

1. **Corpus A/B, three configs**: preserve the committed `tools/corpus/{baroque,jazz,default}`
   (pre-refactor binary outputs, manifest-fingerprinted); regenerate all three with the
   new binary into A/B dirs; **diff every `.ours.json`: 0/353 × 3 required.**
2. Pipeline snapshots **11/11 zero diffs**.
3. All suites green: composing (501 + new), notation 52, batch_analyze regression,
   Python 70.
4. BIR identity sets: Baroque 13 & 24/13, Jazz 7 & 35/7 (exact set), Default 14
   (Baroque-13 ∪ {bwv187.7}).
5. Perf sanity (not the full 5-sweep): one P3PerfBaseline run on chorale_001 +
   K279-1 — medians within noise of `docs/perf_p3_baseline.md` (no caching yet, so no
   improvement expected; a marked slowdown is a finding).

## Task 5 — Doc sync (same commit)

`docs/scoring_model.md` §11: a short addendum — winner selection + commit chain now
flow through the beam-1 decoder (byte-identical re-expression; design doc is the
authoritative structure reference; levels >0 not yet active). No other doc sprawl
(3.5 owns the big restructure docs).

## Commit

ONE commit, proposed and held for Cowork confirmation:
`refactor: beam-1 decoder skeleton behind quality-level knob (Stage 3.1, byte-identical)`
— with the A/B evidence summary in the message body (0/353 × 3, snapshots, identity
sets). Report: `cc_stage3_1_report.md` (§1 plan as built; §2 structure map old→new;
§3 equivalence-test form; §4 the full verification table; §5 deviations/unknowns —
expected: NONE, this is ratified-spec execution).

Stop conditions: ANY output byte differs anywhere (corpus, snapshot, fixture) — stop,
reconcile, report the differing case with its diagnose dump (you now have a trustworthy
one); any need to deviate from the ratified design; any FP canary failure; any
temptation to "improve" anything en route — beam-1 earns zero improvements by design.
