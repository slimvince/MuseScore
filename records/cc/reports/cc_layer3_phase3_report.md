# CC report — Architectural Layer 3, Phase 3: reach-back as a tested capability

> Delivery notes for the Phase-3 build per `cowork_layer3_reachback_design.md` (corrected, §0) and the
> CC instruction. **Production `analyzeRegions` is untouched (whole-score); the capability is exercised
> only by partial-selection fixtures; every production gate is byte-identical.** Gitignored.

## §0 — Cowork docs committed (local-only)
Commit `2907e0c` — `docs(cowork): two-phase plan re-sequence (tpc capability early; tune-precision last) +
Phase-3 reach-back design (selection-aware capability, production untouched)`. `git show --stat` lists
**only** the two files (`cowork_l1l3_stabilization_plan.md`, `cowork_layer3_reachback_design.md`).

## The capability as built — form + reuse ledger

**Form chosen: a parameter on `analyzeRegions` (option B's unification, the lower-duplication choice).**
A default-constructed `ReachBackOptions reachBack` was added to `AnalyzeRegionsOptions`
(`regionanalyzer.h`). `enabled` defaults to `false`, so every existing caller (the notation bridge,
`batch_analyze`, the snapshot harness) is byte-identical — they pass the default. When `enabled`, the
SAME function:
1. builds Layer 1 over the **selection** `[startTick, endTick)` (`NoteModel::build(score, lo, hi)`) instead
   of whole-score — the only build-site change is a default-OFF ternary at `regionanalyzer.cpp:512`; the
   `false` branch is exactly the original `NoteModel::build(score)`;
2. runs the reach-back loop **between the existing decode (`:557`) and the `sliceEnds` lookup (`:561`)**;
3. applies the **output-filter** just before the return.

The entire downstream orchestration — seed/keySigCtx resolution, the slice + decode calls, `localKeyForRegion`,
Pass 1/2/2b, the merge passes, J-key wiring, hooks — is **reused verbatim** over the (possibly grown) model.
`noteModel` / `slices` / `sliceKeys` were de-`const`ed (semantically inert for their read-only uses) so the
loop can re-assign them.

**Reuse-vs-new ledger**
| Reused (unchanged) | New (this phase) |
|---|---|
| The whole `analyzeRegions` Pass-loop body + merges + emission scoping to `[startTick,endTick)` | `ReachBackOptions` struct + `reachBack` field (`regionanalyzer.h`) |
| `slc::changePointSlices` (Layer 2) — called again in the loop | `measureTicksBefore()` helper (one-measure increment from the score time sig) |
| `kms::KeyModeSequenceDecoder::decode` (Layer 3) — pure, called again in the loop | the reach-back loop block (`regionanalyzer.cpp`, guarded by `reachBack.enabled`) |
| `NoteModel::build(score, lo, hi)` / `extend` / `boundaryReached` (Phase 1a) | the output-filter block (drops `endTick <= selStart`) |
| The region→slice `upper_bound` idiom (mirrored for the leading-edge lookup) | `minOpeningConfidence` trigger (the design's "or low sequence-margin") |

**No new parallel path or logic duplication was introduced.** There is one orchestrator, one slicer call site
per pass, one decoder; the loop re-invokes the existing pure `decode()`. No second slicer/decoder, no
incremental `redecodeRange` (the deferred Phase-3b perf step — the loop re-decodes the enlarged span fresh,
as the design mandates for the interim).

## The reach-back loop (per design §2/§3)
- **Trigger** — the selection's leading-edge slice (first slice with `end > selStart`, the `upper_bound` idiom)
  is *unsettled*: `uncertain == true` OR `confidence < minOpeningConfidence`. `minOpeningConfidence` defaults
  to `0.0`, so the default trigger is exactly the decoder's own `uncertain` flag (design §3 primary criterion).
- **Extend** — `model.extend(Earlier, incTicks)`, `incTicks` = one measure via the score's time signature
  (`measureTicksBefore`), or a fixed `incrementTicks` override.
- **Re-slice + re-decode** — `changePointSlices` then `decode` over the enlarged span (a fresh decode; the
  interim, not the deferred incremental path).
- **Convergence** — see the measured correction below.
- **Hard bound / score start** — `maxReachSteps` (default 8) and `boundaryReached()` both terminate the loop.
- **Output-filter** — regions entirely before `selStart` are dropped. (In practice inert: the Pass loops
  already scope every region to `[startTick,endTick)`; the filter makes the selection-only contract explicit
  and robust, and only runs under reach-back.)

### Measured correction — convergence proxy → principled criterion
The design's **cheaper proxy** ("stop when a settled, `uncertain==false` key is in view in the reached-back
context") was implemented first and then **measured to stop prematurely**. On the fixture, one settled
context measure satisfies the proxy while the leading edge is still on the wrong (local) key — the
leading-edge key flips only once a *confident earlier key is established over a run* (a V–I), which is two
measures back:

```
step0 (iso,  loadedStart 11520): lead A minor, conf 1.300  (unsettled → fires)
step1 (+1,   loadedStart  9600): lead A minor, conf 3.020  (settled, but still A minor — 1 measure isn't enough)
step2 (+2,   loadedStart  7680): lead C major, conf 2.480  (flips — a V–I is now in view)
step3 (+3,   loadedStart  5760): lead C major, conf 2.480  (stable)
```

A single-settled-context-slice proxy would stop at step1 (lead = A minor, wrong). So the design's **headline**
criterion — *"extend until the leading-edge key stops changing"* — is implemented directly: track the
leading-edge SETTLED `(tonic, mode)` across iterations and stop when it repeats (more earlier context then
cannot move it). Verified to land on C major (step3), and to be increment-independent (test §3.2). This is a
faithful realization of the instruction's stated stop ("the leading-edge key stops changing"); the literal
single-slice proxy is documented here and in the code comment as insufficient.

## §3 — tests (`src/composing/tests/reachback_tests.cpp`, 4 tests, all pass)
Fixture `data/reachback_anchor.mscx` (authored as `.musicxml`, converted via `MuseScore5.exe`; MuseScore
session sidecars META-INF/Thumbnails/audiosettings.json/automation.json/score_style.mss/viewsettings.json
that the conversion dropped into `data/` were removed — not committed): 0 fifths, **declared A minor**;
bars 1–6 an unambiguous C-major head (I IV V I V I, G–B–D dominants carry the B leading tone, no G#), bars
7–9 a relative-pair A-minor/E-minor/A-minor tail. Selecting **only bar 7** (a single A-minor triad,
`[11520,13440)`) opens with a low-confidence A-minor reading (~1.3) that the C-major head settles to C major.

1. **FiresAndAnchorsToCarriedInContext** — iso reads A minor (tonic 9); reach-back reads C major (tonic 0)
   == the whole-score reading; reached ≠ iso (the extension fired and mattered).
2. **ConvergenceIsIncrementIndependent (determinism)** — 1-measure steps vs 2-measure steps give an
   identical in-selection analysis (both converge to C major) → the §3 proxy/criterion validated.
3. **SelectionAtScoreStart_TruncatesCleanly** — selection `[0, 1920)` with the trigger forced and a large
   increment: `extend` reports the boundary, the loop exits, and the result equals the no-reach baseline
   (graceful no-op, no error).
4. **OutputIsSelectionOnly** — every emitted region lies within the selection; the reached-back C-major head
   is context (evidence), never output.

## §4 — gate: production byte-identical (the hard gate)
- **composing_tests: 635 passed, 0 failed** (+4 reach-back; the 1 disabled is the pre-existing
  `DISABLED_IDX_PERF_ScalingIndexedVsLinear`).
- **notation_tests: 53 passed, 0 failed** (4 pre-existing skips) — matches baseline.
- **pipeline_snapshot_tests: 11/11 passed, no golden refresh** — P1–P4 byte-identical.
- **Corpus BIR (rebuilt `batch_analyze`, full 353×3 regen + `characterise_bir_false`):**
  **Baroque 53 / Jazz 24 / Default 53**, and **every `stem@tick` case-identity set is byte-identical** to the
  CLAUDE.md documented sets (diff empty for all three presets). Production `analyzeRegions` is untouched, so
  nothing on the live path moved. **No movement → no leak.**

## §5 — doc staleness corrected
`keymodesequence.h` ISOLATION block (`:74-80`) rewritten to the **as-built WIRING** reality: the decoder IS
the live key path (region analyzer, duration-majority over the slice run, replacing the per-region argmax),
with the ratified L3-wiring BIR delta, and a note that selection-aware reach-back wraps the same `decode()`
without touching the (pure/static) decoder.

## §6 — scope / unification / stops (confirmation)
- **The ENGAGEMENT was NOT done.** `regionanalyzer.cpp:512` still defaults to `NoteModel::build(score)`
  (whole-score); no production regions are dropped; `notationharmonicrhythmbridge.cpp:131` is untouched; no
  snapshot/notation delta was ratified or needed. Switching production to selection-scoped analysis remains
  the separate, deferred, behaviour-changing step.
- **No duplicate orchestration / second slicer / second decoder / incremental re-decode** (Phase-3b) was
  introduced.
- **`upstream` untouched; `origin` not pushed; local commit only.** No stop condition (§8) was triggered.

## Deliverables (local commits, unpushed)
- `2907e0c` — §0 Cowork docs.
- `<this commit>` — the capability + the 4 tests + fixture (+ source) + the §5 doc fix.
