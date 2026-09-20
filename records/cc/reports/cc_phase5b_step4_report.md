# CC Report — Phase 5b Step 4: G4 / C1 — the symmetric-root spelling-pin (LAST build increment)

**Status: BUILD COMPLETE — byte-identical production, both suites + snapshots green, no regression.**
One material finding flagged for Cowork's engage-step assessment (the pin's corpus footprint is far smaller
than Step-0's pre-G1 projection — see §5). NOT a STOP: the pin is correct, engages on its scope, and does not
regress; the dim7 cases it does not commit are *deferred by the already-built G1/G6 abstain* (the design's
"dissolve here, resolve at L5"), not mis-committed.

Commit (local, unpushed): **`1e74f21ea4`** — `feat(composing): L4 G4/C1 — symmetric-root spelling-pin (Phase-5b Step 4, dormant)`
Files changed (production-wise): `chordslicedecoder.cpp`, `chordslicedecoder.h`, `decode_chord_tests.cpp` **only**.
(`tools/batch_analyze.cpp` carried a TEMPORARY `--chord-no-spelling-pin` A/B measurement flag during §3; it was
reverted before commit — `git checkout`. Cowork can verify by sha that only the decoder + its tests changed.)

---

## §1 — INVESTIGATE-confirm (read-only, before building)

Confirmed against the spec (`cowork_layer4_chordsymbol_design.md` §5/§9), the Step-0 grounding
(`cc_phase5b_step0_report.md` §3 F-4), and the as-built code:

- **Spelling reaches the slice (the pin is real, not a fallback).** `NoteEvent::tpc` is the raw engraving
  `Note::tpc()` (`note_model.cpp:53`), carried losslessly through Layer 1; the decoder's per-note `FocalNote`
  is projected in `eligibleNotesInSpan`. The `tpc` was simply not *copied* into `FocalNote` yet — a one-line
  addition, not a structural gap. The shared `engravingbridge::lineOfFifths` primitive (`spellingview.h`)
  exists, is in the same `composing_analysis` lib the decoder links, and was **unconsumed** (Phase-4
  capability) — exactly the "next build" its header names.
- **Where it plugs in.** The symmetric (pitch-class-ambiguous) root is chosen KEY-dependently in the scorer:
  `dim7CharacteristicBonus` (`chordanalyzer.cpp:471`) adds +0.75 to the Diminished triad rotation whose `bb7`
  is non-diatonic in the current key — folded into `cell.basisIndep`, so the decoder inherits that
  key-dependent rotation. The pin OVERRIDES that choice for symmetric sonorities only, from the notated
  spelling; non-symmetric roots are untouched.
- **C2 is genuinely separable and OUT of scope (confirmed).** The catalogue has `Diminished` as a TRIAD
  `{0,3,6}` (tie 6) only — no four-note dim7 type. A fully-diminished seventh is scored as four dim-triad
  rotations (each covering 3 of the 4 pcs, the 4th the "extra"). The pin re-selects *among existing
  candidates* (no new template) — so it needs no C2. Augmented (`{0,4,8}`, tie 9) is symmetric by
  construction.
- **No structural change beyond the decoder is needed for the pin itself** (the §1 STOP condition did not
  trigger): the spelling is at the slice, and the re-root is a selection among already-surfaced cube cells.

## §2 — BUILD (in `chordslicedecoder`, dormant)

Decoder-local, behind a master switch `enableSpellingPin` (default true; OFF reproduces pre-G4 exactly).

1. **`FocalNote.tpc`** added and copied from `NoteEvent.tpc` in `eligibleNotesInSpan`.
2. **`spellingPinnedRoot(chosen, focal, prefs)`** — a pure public static, the deterministic spelling rule:
   - **Symmetric detection** from the chosen quality + the focal pcs present: a *full* dim7 (chosen
     `Diminished` AND `{r, r+3, r+6, r+9}` all sound — a plain 3-note dim triad is NOT symmetric and is
     left alone) or an augmented triad (`{r, r+4, r+8}`).
   - **Root from the line of fifths**, verified as a clean stack of thirds: gather each collection pc's
     line-of-fifths (`engravingbridge::lineOfFifths`); defer (-1) if a pc has no spelling, if one pc is
     spelled two ways (e.g. G♯ *and* A♭ sounding), or if the sorted positions do not rise by exactly the
     third's step (3 for the minor-third dim7 stack, 4 for the major-third augmented stack). The root is the
     **sharpest** (dim7) or **flattest** (aug) end — the bottom of the stack of thirds. `G♯–B–D–F → G♯`;
     `F–A♭–C♭–E𝄫 → F` (same four pcs, opposite spelling, opposite root).
3. **Integrated into `decideSlice`** (given the slice's focal): after ranking, if the chosen is a symmetric
   sonority whose spelling pins a root, the chosen ROTATION is re-selected to that root's cube cell (same
   quality, preferring the actual bass), and the **sibling rotations are dropped from the margin and the
   carried alternatives** — the spelling, not the score, resolved them, so they are no longer competing
   readings (this is what lets the pinned slice COMMIT instead of abstaining on the inter-rotation margin).
   Where the spelling is absent/contradicted the scorer's key-dependent choice stands (the existing
   behaviour — the design's "defer the unspelled-or-contradicted remainder").
4. **No new chord type** (C2 deferred). **No tuned bonus** — a hard, deterministic SELECTION from the score.
   `focal` was threaded to `decideSlice` at all call sites (`buildSliceWork` pass-1, `finalizeSlice` pass-2,
   the non-membership path); empty `focal` (the hand-injected ranking tests) disables the pin.
5. **Doc-comment block** in the header updated: G4/C1 moved to "WHAT IS BUILT"; "NOT YET BUILT" now lists only
   G5/C2 (the new four-note TYPES).

## §3 — RE-MEASURE (the assess checkpoint) + spelling spot-check

A/B over the canonical 353-stem Baroque corpus via the read-only `--decode-chords` path, pin-ON vs pin-OFF
(through a temporary `--chord-no-spelling-pin` flag, since reverted), graded by `cc_layer4_chord_baseline.py`
(held-out TEST split, vs the When-in-Rome GT). The decoder is preset-identical (Step-0 fact), so one run.

### Aggregate (held-out TEST split, Baroque)

| metric | before (G6, pin-OFF) | after (G4, pin-ON) |
|---|---|---|
| **dur-weighted root-pc match (decoder)** — the coverage-matched line | **77.8%** | **77.8%** |
| Δ dur-weighted vs per-region legacy baseline | +3.9 pts | **+4.0 pts** |
| region-count root match (decoder) | 1734 / 2307 | **1736 / 2309** |
| NCT precision / CT precision | 74.6% / 78.9% | 74.5% / 78.9% |

**Coverage-matched accuracy HOLDS (77.8% → 77.8%, +0.1pt on the Δ-vs-baseline).** The region-count moved
**+2 matches / +2 total** — the pin converted 2 test-split abstains into 2 commits, **both matching GT, zero
regressions** (every previously-matching region is unchanged; no match was lost). Correct abstention is
preserved everywhere else.

### The pin's exact corpus footprint (GT-independent diff, pin-ON vs pin-OFF)

Across **29,213 slices the pin changed exactly 3** — all **augmented**, all turning a pin-OFF **abstain** into a
pin-ON **commit**; **zero dim7 re-rotations.**

| stem@tick | m/beat | sounding pcs | pin-OFF | pin-ON | GT root (per-beat) |
|---|---|---|---|---|---|
| `bwv437@21120` (test) | m12 b1 | {C♯,E,F,A} | abstain | **F augmented** | **F — match** |
| `bwv40.3@16080` (test) | m9 b1.5 | {C,D,F♯,B♭} | abstain | B♭ augmented | None (off-beat; region-aligned GT counts it a match) |
| `bwv48.7@6600` (train) | m4 b1.75 | {D,F♯,A,B♭} | abstain | B♭ augmented | None (off-beat) |

**Spelling spot-check.** The instruction's exemplar `bwv272@4320` (G♯dim7) does **not** commit a dim under the
current decoder — its window-winner is a *phantom* G major (root absent), which G1 correctly abstains on (so
the pin, scoped to a symmetric *chosen*, does not fire — not a regression, an honest defer). The real spelling
spot-checks are therefore: (a) the oracle unit test `SpellingPin_Dim7_OverridesKeyBiasedRotation` — a notated
G♯–B–D–F with a key-biased Ddim top score is pinned **G♯**, not the key alternative; and (b) the live-corpus
`bwv437@21120` — a notated F-augmented is pinned **F**, GT = **F**, where it previously abstained.

## §4 — Gate

- **Production byte-identical — by construction + verified.** Only `chordslicedecoder.{h,cpp}` (+ `FocalNote`,
  a decoder-local struct) and `decode_chord_tests.cpp` changed. The decoder is invoked ONLY under
  `--decode-chords` (which returns before `analyzeScore`); the production analysis path
  (`regionanalyzer`/`analyzeChord`/…) is untouched, so the corpus `.ours.json` (gate 53/24/53) is
  byte-identical by construction. Direct corroboration: **pipeline_snapshot_tests 11/11, zero diffs, no golden
  refresh** (the real P1–P4 production pipeline on 11 scores is unchanged). The full 353×2 corpus regen was
  not re-run (no production file changed; disproportionate to re-prove an untouched path).
- **Both suites green:** **composing_tests 862/862** (`Composing_DecodeChord` 49 → **57**, +8 new), **notation_tests
  53/53**, **pipeline_snapshot_tests 11/11**.
- **New unit tests (8, oracle-asserted):** dim7 same-pcs-opposite-spelling-opposite-root (G♯ vs F); the
  key-bias override spot-check (notated G♯dim7 → G♯); an augmented case (C vs E by spelling + decideSlice
  re-select); a non-symmetric root untouched (major + the confidence is unchanged); a plain dim triad is not
  symmetric; absent-spelling defers; contradicted-spelling defers (broken stack + same-pc-two-ways); the
  master-switch-off no-op.

## §5 — ASSESS (closes the build)

**All Phase-5b build increments are complete: G1, G2/G3, the §4 two-reading inherit, G6, and now G4/C1.** The
spelling-pin is built per spec, deterministic (a selection from the notated spelling, not a tuned bonus),
byte-identical in production, and unit-proven. The coverage-matched accuracy holds (77.8%) and the pin is a
small net positive (+2 correct commits, zero regressions).

**FINDING — flagged for the engage-step assessment (an observation, not an inference-fix, not a STOP):**
the pin's *corpus* footprint is **3 slices**, not Step-0's projected ~87 (3.1%). The reason is an interaction
with the already-built G1/G6, not a defect in the pin:

- Step-0 measured the "87 spelling-fixable" cases on the **pre-G1** decoder, which *always committed* — so it
  committed *wrong dim7 rotations* the pin could re-root. After G1 (sufficiency + phantom-root guard) and G6,
  the decoder now **abstains** on essentially all symmetric dim7 slices: either the window-scored winner is a
  *phantom non-dim* (e.g. `bwv272@4320` → a rootless G major, abstained by the phantom-root guard), so the pin
  — correctly scoped to a symmetric *chosen* — never engages; or the symmetric chord is the winner but its
  inter-rotation margin is low, which G6 abstains on. Either way the dim7 **root is DEFERRED to Layer 5, not
  mis-committed** — which is exactly the design's intent (§11: "the symmetric-rotation churn is *dissolved*
  here (no arbitrary root committed) and *resolved* at Architectural Layer 5").
- So after G1/G6, the symmetric churn is already dissolved by *abstention*; the spelling-pin's remaining job is
  to *commit the spelled root where the decoder commits a symmetric chord* (the augmented cases) instead of
  deferring. That is real and correct (the 3 commits), just small.

**Implication for Cowork (engage step, not this increment):** if the goal is for L4 to *commit* the spelled
dim7 root (rather than defer it to L5), that requires either (a) the window/scoring to surface the dim triad as
the winner where it abstains as a phantom non-dim today (a window / G1-interaction question, not a C1 pin
matter), or (b) accept the design's defer-to-L5 for dim7 and let L5 read the same spelling. Both are engage /
Layer-5 decisions. The pin as built is the correct C1 deliverable; it is complete and does not block.

This is **not** a STOP: no regression, no class-(b) error, no structural need, no production movement, the pin
resolves the symmetric chords the decoder commits and defers the rest as designed.

## §6 — Stops honored
- No production `src/composing/` analysis-path edit; decoder-only + tests. ✓
- No C2 new types crept in. ✓
- No production movement (snapshots 11/11 zero-diff; corpus byte-identical by construction). ✓
- `upstream` untouched. ✓
