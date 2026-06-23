# Cowork independent audit — chordanalyzer (the vertical oracle) — to reconcile with CC

> Second-opinion pass from the committed-object source (HEAD) + the functional-residual investigation.
> Correctness vs the true chord (DCML/music21), not the gate.

## Responsibility
`analyzeChord` — the **vertical chord oracle**: from sounding pitch content (+ bass, + key context for the
diatonic-root tiebreak), score against the **17-template vocabulary**, build a `ScoringSnapshot`, hand it to
the competition/function layer. Output: vertical chord candidates + the snapshot. Foundational vertical
identification. One responsibility.

## Correctness (vs the true chord)
1. **[HIGH correctness — the oracle is SOLID] ~95% vertically correct.** The functional-residual investigation
   established **95.2% of root errors are FUNCTIONAL, only 4.8% vertical**, and music21's vertical RN analyzer
   fails the *same* functional roots → a functional-LAYER problem, not a vertical ceiling. So the oracle
   correctly identifies root+quality from pitch content the large majority of the time. **Few obligations
   here** (contrast: the key axis).
2. **[correctness FLOOR — inherent, the reserved B-slice] Symmetric chords are pc-root-undefined.** A
   fully-diminished 7th {0,3,6,9} has four equally-valid roots; augmented {0,4,8} three. The root is undefined
   *by construction* from pitch alone (~53% of Baroque carries a symmetric dim7). This is the inherent vertical
   floor — the ~111 pc-irreducible cases reserved for a learned emission. Not hand-buildable away.
3. **[correctness — share-tone] viio7↔V7 share-tone collisions** → ambiguous root, partly resolved downstream
   (gates/function layer).
4. **[correctness — key coupling] The diatonic-root tiebreak reads the key** (`diatonicRootContribution`) → the
   chord depends on the key for ambiguous roots (the re-emission-bug coupling; the "vertical" oracle isn't
   purely vertical on ambiguous sonorities). Phase-2 dependency note.

## Completeness (vs the chord vocabulary)
5. **[completeness · chord-axis · jazz] Vocabulary = 17 tertian/sus/power templates** (maj/min/dim/aug
   triads, dom7/maj7/min7/halfdim7/dom7b5/aug7, sus2/sus4 variants, power). Covers tonal/Baroque well, but
   **no extended/altered jazz harmony (9/11/13, alt)** → for the Jazz preset, extended chords are
   mis-identified as the nearest 7th + extra notes. (Verify whether explicit fully-dim7 {0,3,6,9} is a
   template or handled via the dim triad + `dim7CharacteristicBonus`.)

## Phase-2 carry-forward — the chord axis is HEALTHY; obligations are DOWNSTREAM
- Unlike the key axis, the vertical oracle is **high-correctness** — its only real gaps are the *inherent*
  symmetric floor (reserved slice) and the jazz-vocabulary completeness hole.
- **95% of root errors are FUNCTIONAL** → the real chord-axis obligations live in the **competition/function
  layer (`harmonicfunctionlayer`, audited next)**, not the oracle.
- The diatonic-root key coupling = the chord↔key circularity (phase-2): the oracle is "mostly vertical" but
  leaks a key dependency on ambiguous roots.

## Reconciliation targets (for CC)
- Confirm the 95.2/4.8 functional/vertical split holds at the current HEAD + the symmetric-floor size.
- Confirm the jazz-vocabulary completeness gap (extended chords on the Jazz corpus).
- Confirm whether fully-dim7 is an explicit template or derived.
