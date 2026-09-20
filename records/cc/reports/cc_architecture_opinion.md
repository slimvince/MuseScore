# Architectural Second Opinion — Deferred Commitment

**Read-and-reason pass. No code changes, no commits.**

## The decisive fact before the cases

The hypothesis — "defer commitment past functional context; have template
scoring produce a distribution that the functional layer resolves" — is **already
implemented for within-region commitment** by the E2d redesign. `analyzeChord()`
is now a vertical-only oracle that packs the entire `(bass, root, template)` cube
into a `ScoringSnapshot` and applies **no** progression signal and selects **no**
winner. `applyHarmonicFunction()` consumes that distribution, applies
`rootContinuity` / `w_seq` / `w_dim` / Pass-B step bonuses, runs the cross-bass
competition, and *only then* commits a winner
([harmonicfunctionlayer.cpp:230-329](src/composing/analysis/function/harmonicfunctionlayer.cpp#L230-L329)).

So inside a region, commitment is already deferred to after functional signals.
The interesting question is therefore not "should we defer" but "where does the
deferral stop helping" — and the answer is the **inter-region channel**:
`advanceTemporalContext()` forwards only `chosenResult.identity` (a scalar
`rootPc/bassPc/quality`), and `HarmonicFunctionContext` carries no confidence,
margin, or runner-up. The distribution is discarded at the region boundary
([chordanalyzer.h:692-730](src/composing/analysis/chord/chordanalyzer.h#L692-L730),
[harmonicfunctionlayer.h:59-68](src/composing/analysis/function/harmonicfunctionlayer.h#L59-L68)).

This reframes every case below: the within-region distribution exists; the
cross-region point-estimate is the actual bottleneck.

---

## Part 1 — Failure case analysis

### Case A — Iter 98 rootContinuityBonus mis-fires — *moves (becomes a state-forwarding problem)*
The predecessor *already* computed a full distribution; it is thrown away at
`advanceTemporalContext`, so the next region's `rootContinuityBonus` sees only
`previousRootPc` and adds a flat +0.40 regardless of how the predecessor was won.
Deferred commitment within the predecessor changes nothing — the predecessor
already deferred and still committed; the gap is that confidence never crosses the
boundary. **Falsifiable claim:** this dissolves *iff* predecessor **margin**
separates the wrong G6/E residual from the correct Alberti predecessor — a
different axis than the density (`distinctPcs`) proxy that failed in Iter 98. If
the wrong predecessor is *confidently* wrong (high margin), it remains.

### Case B — bwv301 G-absent winner — *remains (not commitment timing)*
The disambiguating fact is vertical: G major wins with `rootPc` pcWeight = 0 (root
absent), beating Bm7 (5th F# absent). The bass is B in both readings, so
"bass=B is a candidate root" is *already* available to the oracle via
`bassNoteRootBonus` — and Bm7 still lost the vertical competition. Deferred
commitment supplies no new signal; the fix is a vertical under-penalty for
root-absent/rootless triads (or template coverage), not later commitment.

### Case C — B1 MinorMajor7 leading-tone ambiguity — *moves (needs new infrastructure)*
With deferred commitment the functional layer would see both `i(maj7)` and
`{tonic + leading-tone-of-V}` in the distribution, but the signal that separates
them is whether the maj7/leading-tone **resolves** by semitone in the next region.
`HarmonicFunctionContext` has `nextRootPc` but not next-region voice content or
PC-resolution. So deferral is necessary but not sufficient: the failure relocates
from "template can't tell" to "functional layer lacks a voice-leading model"
(correctly the Phase-E deferral).

### Case D — B3 dim7 rotation selector — *unchanged (intrinsic; already resolved functionally)*
The four rotations are PC-identical, so there is no vertical distribution to defer —
deferral is orthogonal. Disambiguation is *already* functional and applied at two
points: the non-diatonic ♭♭7 key check (in the oracle) and `w_dim`'s
leading-tone-of-`nextRootPc` resolution target (in the function layer). The only
structural nicety is that the ♭♭7 check could move into the function layer beside
`w_dim`, but that is a code-location change with no behavior change, since key is
available in both.

### Case E — deduction-block guard — *supports the principle; already correctly placed*
The inversion-deduction block deliberately *speculates* — it promotes weak-root
first-inversion alternatives to test them. A hard absent-root veto placed inside a
speculative pass fights the pass's purpose; placed at the `applyHarmonicFunction`
commitment point it vetoes only the final winner. This is a micro-instance of the
hypothesis ("vetoes belong at the commitment boundary, not inside an exploratory
layer"), but it concerns *local* ordering, not the vertical-vs-functional
commitment, which is already deferred. The block is correctly placed as an
exploration layer.

---

## Part 2 — Implementation constraint audit

**2a — `applyIter8691Pedal`.** Runs at the production call sites *after*
`analyzeChord()` (which already ran `applyHarmonicFunction` internally) and
*before* `applyPostScoringGates`
([regionanalyzer.cpp:458-459](src/composing/analysis/region/regionanalyzer.cpp#L458-L459)).
It mutates an *already-committed* `results[]` (pedal Pass-2 can replace `results[0]`
via the captured region tones in `gateCtx`). It is a post-commitment corrector; if
`results[]` were an uncommitted distribution it would have no `results[0]` to test
the bass against — it presumes a winner.

**2b — Gate cascade on `results[0]`.** Essentially *every* gate in
`applyPostScoringGates` is written against a committed `results[0]`/`winner` live
reference and swaps alternatives into slot 0 (bias-correction, A–L, G-E…;
~30 references from [chordanalyzer.cpp:1911-2290+](src/composing/analysis/chord/chordanalyzer.cpp#L1911-L2290)).
They are *identity-correction* gates — they need a committed winner and a small
ranked alternative set, not a 12×17×|bass| distribution. They would all "break"
under a raw distribution, but that is by design: they are deliberately the
post-commitment layer. The distribution-consuming layer is `applyHarmonicFunction`;
the gates are downstream of it and should stay downstream.

**2c — `ScoringSnapshot` as distribution.** Yes — `ScoringSnapshot.cells` is the
full vertical-only `(bass, root, template)` distribution with decomposed score
terms (`basisIndep`, `basisDep`, `complexityFactor`, `augFactor`, `wCompleteBonus`,
`appliedBassBonus`) plus region metadata
([harmonicfunctionlayer.h:131-177](src/composing/analysis/function/harmonicfunctionlayer.h#L131-L177)).
It already *is* the pre-commitment distribution, and `applyHarmonicFunction`
already consumes it as such. The one thing it lacks for a *cross-region*
deferred scheme is any handle on the **predecessor's** snapshot — it is built
fresh per region and never retained.

**2d — `previousRootPc` propagation.** Set by `advanceTemporalContext` from
`chosenResult.identity` — i.e. from the **fully committed** winner, *after* the
function layer, pedal, and Gates A–L
([regionanalyzer.cpp:473-474](src/composing/analysis/region/regionanalyzer.cpp#L473-L474)).
`nextRootPc` is pre-computed by `inferNextRootPc()` (a committed scalar from a
throwaway analysis of the next region). If commitment were deferred across
regions, `previousRootPc` could not be a scalar — the next region's context would
need the predecessor's distribution (or at least its margin), which is exactly the
field that is missing today.

---

## Part 3 — Independent assessment

**Q1 — Which failures are genuinely about commitment timing?**
Strictly, **none of the five** are about *within-region* commitment timing, because
E2d already defers that. Re-binned by their actual layer:
- **Case A** — inter-region *state width* (scalar vs confidence). The only case a
  deferral-flavored change touches, and only if margin (not density) discriminates.
- **Case B** — vertical scoring (rootless-voicing under-penalty / template coverage).
- **Case C** — missing functional signal (voice-leading / resolution model).
- **Case D** — intrinsic enharmonic ambiguity; already resolved functionally.
- **Case E** — local guard-ordering; already at the commitment point.

The honest headline: the chord-identity layer the hypothesis targets is the layer
where deferred commitment is *already done*. The remaining failures are upstream
(key, segmentation — see Q4), lateral (vertical penalties), or need new functional
infrastructure.

**Q2 — Is `ScoringSnapshot` already the right foundation?**
Yes, and `applyHarmonicFunction` is already the deferred-commitment resolver the
hypothesis describes — for one region. The problem is *not* within-region: it is
that the snapshot is collapsed to `chosenResult.identity` at the boundary and the
**next** region inherits a point estimate. The right foundation exists; the missing
piece is carrying predecessor distribution metadata across `advanceTemporalContext`
into `HarmonicFunctionContext`.

**Q3 — Minimum change that moves commitment to the right place?**
Option (a). Add predecessor metadata to the temporal context — `previousWinnerMargin`
(winner score − best different-root alternative), `previousWasSparse`
(`distinctPcs <= 2`), and optionally `previousRootPcWeight` — populated in
`advanceTemporalContext` (which already has `chosenResult` and could read the
retained snapshot), and make `rootContinuityBonus` scale by predecessor confidence
instead of flat +0.40. This is a few struct fields plus one bonus signature change;
it directly targets Case A and is falsifiable on the bwv320 m27 / mozart_k280-1
pair. **Do not** reach for option (b) (forwarding the full predecessor distribution
into the next competition) until (a) is shown insufficient — (a) is the smallest
change that puts a confidence-aware decision at the inter-region boundary, and it is
the only one of the five cases that such a change can move.

**Q4 — The structural mismatch we have not discussed.**
**Key is committed before chord identity, with no feedback path — and that is a
strictly worse instance of the same early-commitment disease the hypothesis aims at,
one layer up.** In `regionanalyzer`, `resolveKeyAndModeRanked` fixes the key/mode
*before* `analyzeChord` runs
([regionanalyzer.cpp:411-416](src/composing/analysis/region/regionanalyzer.cpp#L411-L416)),
and the key is locked to the notated signature. **Named score: Corelli op01n08d** —
its Dorian partial signature (one flat over a C-minor tonic) is read as G minor, so
*every* downstream term that consumes the scale (`diatonicRootBonus`, `w_seq` P4
test, the dim7 ♭♭7 non-diatonic check, Gate I/K/L diatonic guards) is computed
against the wrong tonal frame for the whole piece. This is structural, not
parameter tuning: no gate threshold can recover a chord whose diatonic frame is
shifted a fifth, and there is no path for accumulated chord/progression evidence to
revise the committed key. The hypothesis correctly diagnoses "commit too early" —
but the most damaging early commitment is not template→winner (already deferred);
it is **key→everything** and, secondarily, **segmentation→everything**
(boundaries are committed in `explorationMode` with all progression signals
suppressed, and the functional layer can re-rank identities within a region but can
never split or merge a region — the documented zero-region cases are boundary
commitments no later layer can undo). If effort goes toward deferred commitment,
the highest-leverage target is a key layer that produces a *distribution over keys*
which chord/progression evidence can resolve — not further work on the
chord-identity layer, which is already the most deferred part of the pipeline.

---

### One-line summary
Deferred commitment is already the chord-identity architecture (E2d); of the five
cases only **Case A** would move under an enriched-commitment change, and only if
predecessor *margin* discriminates where *density* did not. The larger early-
commitment liabilities are **upstream** — key (op01n08d) and segmentation
boundaries — where no distribution exists and no deferral is possible today.
