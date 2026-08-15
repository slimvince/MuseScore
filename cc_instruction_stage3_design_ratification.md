# CC Instruction: Stage 3 design ratification — one mandatory correction, all Q's decided

## Ratification verdict

`docs/decoder_design.md` is **ratified subject to ONE mandatory correction**. The
overall structure, the AWKWARD-1/2/3 analysis, the §4 byte-identity argument and
tripwires, the §5 NOT-PINNED boundary, the §7 retirement table, §8, and the §11
classifications are accepted as drafted. Cowork verified AWKWARD-1 against the code
and the Gate R replacement condition against the documented coupling.

## The mandatory correction — completeTriadInversionBonus is temporally GATED

Your honesty flag was right to raise it, but the conclusion is inverted. Cowork
verified in `chordanalyzer.cpp:1613–1622`: the bonus fires only under

```cpp
const bool hasStepwiseBassEvidence =
    context->bassIsStepwiseFromPrevious || context->bassIsStepwiseToNext;
if (hasStepwiseBassEvidence
        && qualifiesForCompleteTriadInversionBonus(...)) { ... }
```

The *qualifier* (`qualifiesForCompleteTriadInversionBonus`) is region-local — that's
what you read — but the **call-site gate is temporal** (either-neighbor bass-stepwise).
The 2026-06-09 layer audit (Finding 1) was correct. Leaving this term in the oracle as
"pure emission" would leave a temporal context read inside the post-3.3 oracle,
defeating the migration. Correct the design:

1. **§3 table row**: `completeTriadInversionBonus` → "**Transition-gated emission**:
   region-local quality test (complete triad, inverted, 3-PC) ACTIVATED by
   (back-edge bass-stepwise OR cold-lookahead forward-stepwise) — migrates in 3.3 with
   the bundle; at beam 1 the forward half stays cold-lookahead (AWKWARD-3 applies)."
2. **§6 migration table**: restore it to the migrating set (the roadmap's "4 inversion
   bonuses" bundle stands); its decoder home = an edge-gated term with the OR-of-edges
   condition stated explicitly; cite `chordanalyzer.cpp:1613–1622`.
3. Re-check §6's count language ("four are genuine transitions and one is region-local")
   and any downstream sentence built on the wrong split.
4. While there: re-verify the OTHER four signals' firing conditions at their call sites
   the same way (guard-at-call-site vs qualifier — make sure no second instance of this
   read-the-qualifier-miss-the-guard error exists; report what you find).

## Open Questions — all seven decided (recommendations accepted)

- **Q1**: whole-score decode, cached in the bridge, bounded-window invalidation.
- **Q2**: Level 1 promotes forward signals to true decoded-successor edges.
- **Q3**: (a) — identity-mutating gates are retired/folded BEFORE the beam widens past
  them; 3.4 leads 3.2 for those gates. Update §12's sequencing note accordingly.
- **Q4**: reproduce 1b-F4 artifacts at beam-1; fix-as-retire in 3.4 per-gate.
- **Q5**: emit the full path + per-node alternatives + margins (evidence-forwarding).
- **Q6**: Level-1 beam-in starts at K=8; Stage 5 tunes.
- **Q7**: 3.1 ships cache-READY without caching; decode-once lands as **3.1b** after
  the byte-identity gate passes (correctness and caching risks verified independently).

Record these in §13 as **DECIDED (Cowork ratification, 2026-06-12)** with one-line
rationales; keep the original recommendation text for the record.

## Commit

After applying the correction + the Q-decisions:
1. Commit `docs/decoder_design.md` as
   `docs: Stage 3 decoder design (ratified — beam-1 byte-identity plan)` —
   include in the same commit a `docs/implementation_roadmap.md` touch-up: 3.2/3.4
   ordering note per Q3, and a "design ratified `<hash>`" line on the Stage-3 header.
2. Report the hash + the §correction-4 re-verification results inline. STATUS is
   Cowork's (will record ratification + the completeTriad correction as the session's
   teaching example of qualifier-vs-call-site-guard).

Stop conditions: the §correction-4 sweep finds a second mis-classified signal (report
before re-drafting around it); anything in the Q-decisions that contradicts code you
re-read while applying them.
