# CC Instruction — ANCHOR (architecture fix): READ-ONLY design investigation

> The architecture-fix order's deepest item (`cowork_phase2_architecture_review.md` §5 step 3 / the sixth
> issue): the chord is finalized **before** its region's tones are final AND against a **frozen** key →
> a one-shot pipeline with **no fixpoint**. **This is ARCHITECTURE, not inference tuning** (user principles:
> architecture FIRST; better inference only once the architecture is correct, known, tested). **This step is
> READ-ONLY: investigate + DESIGN only. NO code/behavior/inference change. Produce a dossier; the user ratifies
> the actual change before any implementation.** North star: best = CORRECT inference vs the DCML/music21
> oracle.

## §0 — Why read-only first (user principles 2 + 4: investigate, never guess; no surprises)
This is the first output-moving change and the deepest re-layering. We do NOT touch code until the mechanism is
mapped at source and the design + measurement plan are ratified. Guessing the data-flow here would be the exact
"assume" failure the user forbids. Map it, don't assume it.

## §1 — The defect, restated (verified at HEAD `dd418ecfed` by Cowork — confirm at source)
- The chord is emitted **mid-pipeline**: `analyzeChord` at Pass-1 `:627`, Pass-2 `:858`, Pass-2b `:1064`,
  against the tones present *at that pass*.
- Pass-3 then **mutates region tones AFTER** the chord exists: `coalesceShortSameRootRuns` folds in other
  sub-regions' tones (`mergeChordAnalysisTones` ~`:138`) and recomputes **only the bass**;
  `absorbShortRegions` extends spans — neither recomputes root/quality/extensions.
- The key is **frozen into `cell.basisIndep` pre-competition** (`chordanalyzer.cpp` ~`:1436`), via the oracle's
  `dim7CharacteristicBonus` + `diatonicRootContribution`.
- Net: `segment → chord(key₀, partial-tones) → merge → key₁`, **no fixpoint** — the source itself says the
  joint re-key "calls decideJointKey ONCE (frozen — no fixpoint)" and cannot re-emit the chord
  (`regionanalyzer.cpp` ~`:309-316`).

## §2 — ★ THE decisive question to resolve (the design hinges entirely on this)
**Does segmentation CONSUME the chord result, or only the tones?** `analyzeChord` is called *inside* the
Pass-2/2b sub-boundary detectors. Trace precisely:
- Do `detectOnsetSubBoundaries` (Pass-2) and `detectBassMovementSubBoundaries` (Pass-2b) use the
  **`ChordAnalysisResult`** (root/quality/identity) to DECIDE where to split — or do they split on raw
  tone/onset/bass features and merely *attach* the chord to each resulting sub-region?
- Same for the inline same-root collapse (now `tryCollapseSameChordRegion`, step 2): it reads
  `chordResult.identity.rootPc/quality` to decide merges — so the **merge already depends on the chord**.

Two worlds, two designs:
- **(A) Segmentation does NOT need the chord to choose boundaries** (chord is only attached) → the fix is a
  **clean re-order**: run all segmentation (incl. Pass-3 merges) on tones first → FINAL region tones → compute
  the chord ONCE per final region, with the key as an explicit input. Feed-forward, no iteration.
- **(B) Segmentation DOES consume the chord** (boundaries/merges depend on root/quality) → a clean re-order is
  impossible; the honest fix is an **iterative fixpoint** (compute chord → segment → recompute chord against
  final tones → re-segment until stable), i.e. the constrained-joint formulation. Heavier, but it's what the
  "no fixpoint" diagnosis implies.

**Report which world we are in, with source evidence (call-sites + what they read).** This single finding
determines whether the anchor is a re-order or a joint loop — do not guess; trace it.

## §3 — What to investigate + deliver (all read-only)
1. **Data-flow map:** tones → (Pass-1/2/2b boundary decisions + analyzeChord) → Pass-3 tone mutation → key.
   For each chord call-site, list exactly what consumes its output (the §2 question), with file:line.
2. **The key-freeze seam:** confirm the two oracle key-reads + where `basisIndep` is frozen, and assess how
   hard it is to thread the key as an **explicit oracle parameter** (the byte-identical-plumbing sub-step:
   pass the *current* key value explicitly → byte-identical; the behavior change only arrives when a
   *different* (final-region) key/tone set is passed).
3. **Design options** (A vs B from §2, plus any hybrid). For the recommended one: the new layer ordering, what
   moves where, the seams/signatures that change, and an honest complexity/risk estimate. Flag whether a
   byte-identical plumbing sub-step can land first (principle 1: smallest correct architectural step first).
4. **Measurement plan** (how we'll know the eventual change is CORRECT, not just different):
   - Expected output movement (which regions/chords change) and WHY.
   - **Correctness vs the oracle** — the change must move root/chord output *toward* DCML/music21, measured on
     the corpus (this is the 37.7%/~38–42% held-harmony residual the anchor targets). Define the before/after
     metric.
   - **BIR gate:** Baroque 57 / Jazz 23 / Default 57 must HOLD or improve on all three presets (case-identity),
     no regression — a hard gate.
   - **Snapshots:** `pipeline_snapshot_tests` goldens WILL move (expected). The plan: inspect each golden diff,
     verify it is correct vs the oracle, THEN `--update-goldens` — never update blind.
5. **Risks / unknowns / stop-points.** Where could this regress? What can't be measured read-only? What would
   make us abandon design A for B (or defer)?

## §4 — Deliver
`cc_anchor_design_dossier.md`: the §2 verdict (A vs B, with evidence), the data-flow map, the key-freeze
assessment, the recommended design + the byte-identical-plumbing-first sub-step if one exists, the measurement
plan, and the risks. **READ-ONLY — no code change, HEAD stays `dd418ecfed`.** Cowork reconciles at the
committed object + the bigger architecture context; **the user ratifies the design before any implementation.**

## §5 — Stop conditions
- Any code/behavior/inference change → STOP (this is design-only).
- The §2 question cannot be answered cleanly from source (genuinely ambiguous call-site) → say so explicitly,
  give what you found, do NOT force an A/B verdict.
- The design appears to require touching the catalog/ground-truth or anything outside the chord/region/key
  pipeline → note it, do not assume authorization.
