# CC Instruction — Layer 3 key/mode: WIRING §2 (CODE) — ratified low-risk choices

> The wiring design dossier (`cc_layer3_wiring_design_dossier.md`) is Cowork-verified at source and **user-ratified**.
> Implement the §2 wiring code to the **ratified, low-risk** choices below. This is **Step 1** (decoder replaces the
> per-region resolver, **BASELINE scorer**); the `scaleMembership` reweight is **Step 2** (separate, NOT here).
>
> **★ Low-risk posture (user directive):** when a gate moves the wrong way, **STOP and surface** — do not force it,
> do not refresh goldens to mask it, do not pull Step 2's reweight in to rescue Step 1 without surfacing first.

## §1 — Ratified design choices (locked)
1. **Intra-region rule = (b) duration-majority.** Per Pass-1 coarse region `[startTick,endTick)`, the region's key is
   the decoder key holding the most ticks in that span. Re-split (c) is **deferred** (it changes the grid).
2. **Seed = S2 (segmentation-stable).** Keep `resolveKeyAndModeRanked` at @521 for the **seed only** (coarse grid
   byte-stable); replace **only** the per-region seam @633. Full seed-retire (S1) is a **tracked follow-up**.
3. **P4 tick-local path = defer.** Leave P4 on `resolveKeyAndModeRanked`; do not touch it. Tracked follow-up =
   **P4-redecode** (P4 indexes a cached whole-score decode) — the eventual "one key path" end-state.
4. **Confidence = C1.** Populate `keyModeResult.normalizedConfidence` from the chosen state's **emission**
   `normalizedConfidence` (the `analyzeKeyMode` sigmoid @ `keymodeanalyzer.cpp:771-774`), NOT the sequence margin —
   it is the scale the 0.8 downstream gate is calibrated for. (Sequence-margin-as-downstream-confidence = a later
   confidence-redesign follow-up.)
5. **Single-signature decode = accept (baseline).** Report the count of stems with notated mid-piece key-signature
   changes (the affected set). Per-notated-segment re-anchor = deferred.

## §2 — The wiring (data flow, per dossier §2.1)
In `analyzeRegions` (`regionanalyzer.cpp`):
1. Reuse the existing whole-score `noteModel` (@508).
2. Compute `correctedFifths` **once** via `partialSignatureCorrection(...)` exactly as the resolver does
   (`keyresolver.cpp:260-263`, mode-gated on `declaredMode.has_value()`) — the load-bearing Baroque partial-signature
   fix (fidelity gap #2). Read `declaredMode` as the resolver does.
3. Add `slices = changePointSlices(noteModel)` (Layer-2 grid; not currently called here).
4. Run `KeyModeSequenceDecoder::decode(slices, noteModel, correctedFifths, declaredMode, keyPrefs, seqPrefs,
   excludeStaves)` **once**, before the Pass-1 loop. **Thread `excludeStaves`** through
   `decode()` → `buildLattice` → `buildSliceContext` → `pitchContextOverSpan` (the view already accepts it) — fidelity
   gap #1. This is a decoder signature addition; production excludes staves, so the decode must too.
5. Build a tick→slice index (slices are ordered/covering/non-overlapping) for O(log N) region→slice-run lookup.
6. **Replace @633:** per Pass-1 coarse region, derive `localKey` (+ fifths + mode) by **duration-majority** over the
   region's slice run, and feed it to the existing consumers (`analyzeChord` @668, `inferNextRootPc` @653,
   `refineSparseChordQualityFromKeyContext` @684, `applyTonicPriorToSparseChord` @686, `keyModeResult` @740). Map the
   **C1** confidence into `keyModeResult.normalizedConfidence`.
7. **Pass-2/2b untouched** — they inherit `parentRegion.keyModeResult` (no re-resolution).
8. **Retire** from the region production path: the @633 resolver call + its hysteresis + the `prevKeyResult`
   threading; `collectPitchContext` as the region builder. Leave @521 (seed, S2), @393 (joint, OFF), and P4 untouched.

## §3 — Gates (MANDATORY, both presets — production-changing)
- **BIR case-identity, NO regression:** Baroque **57** / Jazz **23** / Default **57**, byte-or-better
  (`run_bach_preset.py` + `characterise_bir_false.py`, both presets). **Any BIR=false increase on ANY preset = HARD
  STOP, surface — do not proceed, do not pull in Step 2 to rescue without surfacing.**
- **Both suites pass:** `composing_tests` + `notation_tests` (incl. `pipeline_snapshot_tests`).
- **Pipeline snapshots:** produce the diff; confirm each change is the decoder being *correct*; **surface for
  ratification before any `--update-goldens`.** Under P4-defer the **P4 goldens must be byte-identical** (P4 still on
  the resolver) — if a P4 golden moves, something leaked; STOP.
- **S2 segmentation check:** confirm the coarse grid is byte-stable (the S2 seed is unchanged ⇒ `greedyExpandSegmentation`
  input unchanged ⇒ same regions). If the grid moves, the S2 assumption is violated — STOP and surface.
- **Held-out direct metric:** report the wired decoder's production key vs held-out GT per preset; confirm it tracks
  the build-report grading direction. A divergence implicates the §2 fidelity fixes (excludeStaves / correctedFifths /
  C1) — they are the prime suspects.
- **S2 key-inference:** report the move.

## §4 — Unification ledger (standing rule)
State **reused / newly-written / retired**. End-state: **on the production region path, one key path (decoder) + one
builder (`pitchContextOverSpan`).** Surface the residuals honestly (not silent): P4 still on the resolver (tracked
follow-up), and the resolver + `collectPitchContext` remain compiled as the diagnostic/grading baseline. End with:
*"No NEW parallel path or logic duplication was introduced; the P4 residual is pre-existing and surfaced with a named
follow-up."* Cowork verifies at source.

## §5 — Commit + push
- Commit **locally (unpushed)**. **Do NOT push** until Cowork verifies the wiring at source and the user ratifies
  (first production-moving change). Leave held WIP (B2 trio, `STATUS.md`, WIP docs) unstaged; `cc_*` report gitignored.
- When approved: **`origin` only. NEVER `upstream`** (disabled; hard stop).
- Report `cc_layer3_wiring_report.md`: the as-wired data flow, the three fidelity fixes, the gate results (BIR both
  presets, suites, the surfaced snapshot diff, S2 grid-stability, held-out re-measure), the §4 ledger, and the
  single-signature affected-stem count.

## §6 — Stop conditions
- BIR=false increases on any preset, a suite fails, a P4 golden moves, or the coarse grid shifts → STOP, surface.
- Tempted to apply the `scaleMembership` reweight (Step 2) or to refresh goldens to mask a move → STOP.
- The held-out re-measure diverges from the build-report grading → STOP, check the fidelity fixes before proceeding.
- A push would target `upstream` → STOP (fork-only).
