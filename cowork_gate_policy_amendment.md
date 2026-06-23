# Proposed CLAUDE.md amendment — two-tier BIR gate (class-(a) symmetric-rotation churn vs class-(b) functional regression)

> **Status: DRAFT for user ratification.** On ratification this folds into CLAUDE.md's "Gate threshold and preset
> policy" section, refining (not removing) the BIR case-identity gate. Until ratified, the existing strict gate stands.
>
> **Why:** the Architectural-Layer-3 decoder wiring (Step 1) is faithful and functionally net-positive, but trips the
> strict case-identity gate purely on **symmetric-diminished-seventh / share-tone rotation churn** — sonorities whose
> root is **pitch-class-undecidable by construction**, key-orthogonal, and beyond the spelling-blind pitch-class
> pipeline's reach. Cowork verified this at the score (music21 ground truth) on the four cases below.

## The amendment (proposed gate wording)

The existing rule — *"Any BIR=false increase in either preset is a hard stop … the gate is the case-identity set,
not a bare integer"* — is refined to distinguish **two classes** of new BIR=false case:

**Class (b) — functional / key regression. UNCHANGED HARD STOP.** A new BIR=false case at a sonority whose root is
**pitch-class-decidable** (any non-symmetric chord: triads, dominant sevenths, etc.) where the analysis now gets the
root or key wrong. **Zero** new class-(b) cases on any preset, ever. This is the gate's real intent; it does not move.

**Class (a) — symmetric-rotation churn. TRACKED, CONDITIONAL — not an automatic hard stop.** A new BIR=false case at
a sonority whose root is **pitch-class-undecidable by construction** — a symmetric diminished-seventh, augmented
triad, whole-tone collection, or a share-tone tetrad (half-diminished ↔ minor-sixth; diminished-seventh subset of a
dominant ♭9; major-seventh ↔ relative-minor triad). The analyzer is spelling-blind (it works in pitch class), so it
cannot pick the spelling-correct rotation, and **no rotation is more correct by pitch class**. Such a case is
acceptable **only when ALL** of:
1. **Verified at the score, per case.** Each new case is shown — against the actual notes (e.g. the music21 GT
   region) — to be a genuinely symmetric / share-tone sonority with a pitch-class-undecidable root. Assertion alone
   does not qualify.
2. **Default to class (b) on any doubt.** If a case cannot be *proven* class-(a), it **is** class-(b) (hard stop).
   The burden of proof is on class-(a).
3. **Net BIR=false count non-increasing** on every preset. Class-(a) churn *swaps* structurally-equivalent cases; it
   must not raise the total false count.
4. **Recorded** — the specific case identities (stem@tick + sonority) listed in the change's report.
5. **Interim only.** This is a bridge pending the **Stage-5/6 spelling-aware (two-tier) gate**, which adjudicates
   symmetric sonorities by spelling / voice-leading. When that gate exists, these cases are decided properly and this
   exception retires.

The exception applies **only** to the symmetric / share-tone structural class. No other source of a new BIR=false case
qualifies.

## Founding evidence (Cowork-verified at the score, music21 GT, 2026-06-22)
The four Step-1 Architectural-Layer-3 wiring cases, independently confirmed symmetric / share-tone (root
pitch-class-undecidable):

| case | preset(s) | GT sonority | root reading |
|---|---|---|---|
| bwv272@4320  | Baroque/Jazz/Default | diminished seventh chord (G♯-B-D-F) | GT G♯ (spelled) vs decoder pc-equivalent rotation |
| bwv289@20160 | Baroque/Default      | diminished seventh chord (A♯dim7)   | same — rotation |
| bwv291@17760 | Jazz                 | half-diminished seventh (Eø7 ↔ Gm6) | share-tone, same 4 pcs |
| bwv387@10560 | Default              | diminished seventh chord (G♯dim7, subset of E7♭9) | dim7 subset |

In every case the GT root is the **spelling-aware** rotation; the spelling-blind decoder picks a
pitch-class-equivalent rotation. **Zero functional or key regressions.** (The fifth case, bwv282@12000, was
*Step-2-introduced* and is removed by reverting Step 2; the GT reads it as a plain A-minor triad — so it would **not**
qualify as class-(a), and is correctly excluded.)

## Root-cause attribution (proper layer)
The rotation churn is a **chord-layer (Architectural Layer 4) ambiguity** — *which note is the root* — **surfaced, not
caused,** by the Layer-3 key change (the key context is the chord analyzer's tiebreaker for symmetric chords). The
proper fix is **spelling / voice-leading-aware chord-root selection (Layer 4 / Stage 5–6)**, not any key-layer change.
This amendment is the interim gate policy until that layer exists.

## On ratification
1. Fold the "Class (a) / Class (b)" wording above into CLAUDE.md's "Gate threshold and preset policy" (the gate's
   home), keeping the existing case-identity sets as the class-(b) baseline.
2. CC reverts Step 2 (chord/BIR-flat; deferred to a separate KEY-metric-gated increment) and commits the faithful
   Step-1 wiring under the amended gate, with the four class-(a) cases recorded and the snapshot diff **surfaced for
   ratification before any golden refresh** (the legitimate key/RN improvements + the class-(a) relabels).
