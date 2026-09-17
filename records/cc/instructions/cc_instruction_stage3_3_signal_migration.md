# CC Instruction: Stage 3.3 — oracle temporal-signal migration + Gate R redesign (ATOMIC)

## Context

Roadmap 3.3, design §6 as corrected at ratification: the FIVE oracle-side temporal
signals migrate into the competition pipeline, and Gate R's `basisDep ≤ 0` proxy is
redesigned to read the sounding third directly — **one commit, indivisible** (splitting
opens the documented silent-regression window). Base: `4f1754c26c`.

**Why this is the hardest byte-identity gate yet:** 3.1/3.1b never moved arithmetic
("the decoder computes no score"). 3.3 MOVES five score terms between layers. The same
values must be composed in the same arithmetic order at the same position in the score
expression, or the FP near-ties (Δ=+7b 0.02 class, the margin=0.000 Jazz set) flip.
The E2d precedent proves it's achievable ("basisIndep (clean) + rootContinuity
reconstructs the historical value" — scoring_model §11); this is the same maneuver ×5
plus a cap.

Working method A–H (handoff) applies in full. Mandatory reads: design §3/§6 (the
corrected table — completeTriad = edge-gated emission, OR-of-edges), scoring_model §4
(the five terms + the cap + Gate R), `chordanalyzer.cpp` `bassIndependentContextualBonuses`
+ `bassDependentContextualBonuses` (the code being moved — read CALL SITES, not just
helpers; the completeTriad lesson), `harmonicfunctionlayer.cpp` Pass A,
audit Findings 1/2a/6 (this clears them), the Stage-1a/1b test files (re-pin candidates).

---

## Task 1 — Survey + FP-preservation plan (report §1; this is the load-bearing task —
do not write production code until the plan is complete and internally verified)

1. **The exact current composition**, documented to the addition: where each of the five
   lands today — `resolutionBonus` into `basisIndep` (at what position among its other
   terms?); the four inversion bonuses summed into `inversionContextBonus` in WHAT
   order, then `min(sum, maxTotalInversionContextBonus)`, then added to `basisDep`
   (where, relative to `appliedBassBonus`?). Quote the code. The migrated computation
   must replicate THIS composition: same per-term order inside the capped sum, same
   `min`, same insertion points relative to the `(basisIndep + rcb + basisDep) × cf × af`
   expression in Pass A.
2. **What the pipeline needs that it doesn't have.** The temporal CONDITIONS are in
   ctx (prevQuality, bassIsStepwiseFromPrevious/ToNext, previousRootPc — verify each,
   incl. on the bridge path). The VERTICAL predicates gating the bonuses
   (`isInvertedMajMin` / `supportsContextualInversionBonuses`,
   `qualifiesForCompleteTriadInversionBonus`, `hasStructuralBass`) are oracle facts:
   the clean split is **vertical predicates stay oracle-side as per-cell FLAGS on
   `ScoringCell`** (they are pitch facts — legitimately oracle); the temporal gating +
   bonus values + cap move to Pass A. Enumerate the new cell fields and verify each is
   a pure vertical fact.
3. **Gate R replacement condition** (design §6): direct sounding-third test —
   `pcWeight[(rootPc + thirdInterval) % 12] > presenceThreshold`, third interval from
   the candidate's quality. Resolve precisely: which threshold (the §4 kPresenceThreshold
   0.05 vs extensionThreshold — what does the CURRENT basisDep>0 outcome actually
   correspond to? Derive, don't pick); what happens for qualities without a defining
   third (Sus, Power, Dim?) — the old proxy's behavior on those must be matched, case
   by case. The new predicate must produce THE SAME GATE/NO-GATE decision on every
   reachable input as the old one does today — argue it in the plan, then prove it by
   the corpus A/B.
4. **Re-pin inventory.** Stage-1a/1b/3.1 unit tests that encode the OLD slot semantics
   (fixtures setting `basisDep` to mean "sounding third"; the formula test's term
   composition; Gate R fixtures) — list every test that must be DELIBERATELY re-pinned
   (2.2-ii precedent: marked re-pins) vs every test that must stay green untouched.
   The end-to-end pins (Δ=+7b, bwv110.7, the corpus) are NOT re-pinnable — they are
   the proof obligations.
5. **diagnoseChord**: the COMPETITION layer must now display the migrated signals
   (resolution + the four inversion edges incl. Gate R's new reasoning); the agreement
   invariant stays green by construction — confirm.

## Task 2 — Implement (per plan, atomic)

The oracle stops adding the five terms (its `basisIndep`/`basisDep` become genuinely
vertical — audit Finding 1 debt clears); Pass A reconstitutes them in the planned
composition; Gate R reads the new condition; `chordanalyzer.h:329` TODO and the
Finding 2a/6 comments updated; scoring_model §4/§11 + harmonicfunctionlayer.h comments
synced (the oracle's "applies no progression signal" finally becomes TRUE — say so).

## Task 3 — Verify (the full gate, maximum strictness)

1. **0/353 × 3 configs corpus A/B** (the 3.1 protocol; manifests as second proof).
2. Snapshots **11/11 zero diffs**; composing (505 ± documented re-pins) / notation 57 /
   Python 70 / batch regression.
3. BIR identity sets ×3 (Baroque-13 ticks now pinned in CLAUDE.md — compare against).
4. FP canaries + Δ=+7b/bwv320 pins UNMODIFIED and green.
5. One diagnose dump on a Δ=+7b shape showing the NEW Gate R reasoning fields.
6. Perf sanity: one P3PerfBaseline spot (no change expected — same arithmetic, moved).

## Commit — ONE, held for Cowork ratification

`refactor: migrate oracle temporal signals to the competition pipeline; Gate R reads
the sounding third directly (Stage 3.3, byte-identical)` — message carries the A/B
evidence + the re-pin ledger + the audit-debt closure note.

## Report — `cc_stage3_3_report.md`

§1 THE PLAN (composition quotes, new cell flags, Gate R derivation incl. the
no-third-quality cases, re-pin inventory); §2 implementation map; §3 verification;
§4 re-pin ledger (each marked test, old→new meaning); §5 deviations/unknowns.

Stop conditions: ANY corpus/snapshot diff or canary failure (reconcile, never refresh);
the FP composition proving unreplicable in the new home (STOP with the specific
expression — options come to Cowork, e.g. replicating the sum structure verbatim);
the Gate R equivalence derivation finding a reachable input where old and new disagree
(that's a design question, not an implementation detail); any second
qualifier-vs-call-site surprise in the five signals (Method D).
