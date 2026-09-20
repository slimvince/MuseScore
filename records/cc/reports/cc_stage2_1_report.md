# Stage 2.1 — Phase 4c: move `analyzeSection` + section-level analysis into composing

**Status: COMPLETE — all gates green, byte-identity proven. Two commits proposed
(below), awaiting Cowork confirmation. Nothing committed.**

HEAD at start: `bb48394b52` (Stage 1d). Decision on the Pass-0 reverse dependency:
**Option D (inject Pass-0 regions)** — chosen by the user.

---

## §1 — MOVE / STAY inventory, target home, caller strategy, test ledger

### MOVE → new `src/composing/analysis/section/sectionanalyzer.{h,cpp}` (namespace `mu::composing::analysis`)

| Symbol | Kind |
|---|---|
| `analyzeSection` | function (Passes 1–4 + key-area grouping; Pass 0 now injected) |
| `stabilizeHarmonicRegionsForDisplay` | file-local (anon ns) |
| `distinctPitchClassCount` | file-local (anon ns) |
| `detectCadences`, `detectPivotChords`, `hasAssertiveKeyConfidence` | functions |
| `CadenceMarker`, `PivotLabel` | result structs |
| `kAnnotateKeyConfidenceThreshold`, `kMaxPivotLookaheadRegions` | constants |

### STAY in `notationcomposingbridgehelpers.{cpp,h}`

`scoreNoteSpelling` (notation→composing display adapter, reads engraving style);
all thin pass-through shims (`diatonicDegreeForRootPc`, `refineSparseChordQuality…`,
`applyTonicPriorToSparseChord`, `forceChordTrackQualityFromKeyContext`,
`collectRegionTones`, `detectOnset/BassMovementSubBoundaries`, `findTemporalContext`,
`collectPitchContext`, the weight helpers), and `resolveKeyAndMode`.

**Re-derivations against the suggested MOVE list** (per "verify each, don't trust it"):
- `resolveKeyAndMode` → **STAY**. Sole caller is `notationcomposingbridge.cpp:410`
  (per-note path, which stays in notation); not used by `analyzeSection`. Moving it
  only churns its one notation caller for no functional gain — its real logic is
  already `kr::resolveKeyAndModeRanked`.
- The weight / pitch-context shims (`beatTypeToWeight`, `safeBeatType`,
  `regionMetricWeightForBeatType`, `timeDecay`, `distinctPitchClasses`,
  `collectPitchContext`) are **dead** (no live caller anywhere in `src/notation`).
  Left untouched — deleting dead shims is "tidying," out of scope. Flagged for a
  later cleanup pass.

### Target-home & Pass-0 resolution (Option D)

`analyzeSection`'s only cross-module dependency was its Pass-0 call to
`mu::notation::analyzeHarmonicRhythm` (notation). Option D removes that line and adds
a `const std::vector<HarmonicRegion>& rawRegions` parameter: the caller computes the
Pass-0 stream via the unchanged `analyzeHarmonicRhythm` (Smoothed) and injects it.
This keeps `composing_analysis` **config-agnostic and notation-agnostic** (matches the
deliberate Phase-4 `analyzeRegions(prefs, opts)` contract — `composing_analysis` does
not include `IComposingAnalysisConfiguration` or IoC), leaves `analyzeHarmonicRhythm`
+ debug-capture + batch entirely untouched, and keeps the moved body **byte-identical
from the region-conversion loop onward**.

### Caller strategy (no shim)

All 6 `analyzeSection` call sites are inside the notation module/tests; re-pointed to
`mu::composing::analysis::analyzeSection`, each preceded by one
`analyzeHarmonicRhythm(...)` line:
- `notationcomposingbridge.cpp:244, :1117` (+ `using`-decls for detectCadences /
  detectPivotChords / PivotLabel re-pointed; `kMaxPivotLookaheadRegions` re-pointed)
- `notationimplodebridge.cpp:1373` (+ `using`-decls hasAssertiveKeyConfidence /
  detectCadences re-pointed; `.h` doc-comment corrected)
- `pipeline_snapshot_tests.cpp:320, :716, :1059`

### Test ledger (no coverage drop)

| Suite | Before | After | Note |
|---|---|---|---|
| composing_tests | 498 | 498 | unchanged |
| notation_tests | 52 | 52 | `notationannotate_tests` (cadence/pivot) kept here, include re-pointed to the composing header; resolves moved symbols via its existing `using namespace mu::composing::analysis`. Lowest-risk; instruction explicitly permits leaving the tests in notation. |
| pipeline_snapshot | 11 | 11 | call re-pointed only |

The cadence/pivot tests build `AnalyzedRegion` vectors directly (no Score), so they
*could* relocate to `composing/tests`; keeping them in place avoids test-helper
portability churn with zero coverage change.

---

## §2 — File map (proposed ARCHITECTURE.md text, not yet applied)

- **NEW** `src/composing/analysis/section/sectionanalyzer.h` — declares
  `analyzeSection`, `detectCadences`, `detectPivotChords`, `hasAssertiveKeyConfidence`,
  `CadenceMarker`, `PivotLabel`, the two cadence/pivot constants. Namespace
  `mu::composing::analysis`.
- **NEW** `src/composing/analysis/section/sectionanalyzer.cpp` — definitions, including
  the file-local `stabilizeHarmonicRegionsForDisplay` / `distinctPitchClassCount`.
  Registered in `composing/analysis/CMakeLists.txt` (new `section/` group).
- `notationcomposingbridgehelpers.{cpp,h}` — shrank by ~900 lines; now only the
  notation-side adapter surface (`scoreNoteSpelling` + shims). File-top comment updated.
- `composing/CMakeLists.txt:39–42` — `analyzed_section.h` deferral comment updated
  (move resolved).

Proposed ARCHITECTURE.md sentence: *"Section-level unified analysis — `analyzeSection`,
key/mode stabilization, cadence and pivot detection — lives in
`composing/analysis/section/`. Pass-0 boundary detection (`analyzeHarmonicRhythm`)
remains the notation-side configuration adapter and injects its `HarmonicRegion`
stream into `analyzeSection`, keeping `composing_analysis` independent of the notation
and configuration layers."*

---

## §3 — Task-3 rider (chordanalyzer.h doc-comment)

Comment-only (`= 2.0` default unchanged). Verified the live signal list against
`bassDependentContextualBonuses()` (chordanalyzer.cpp:1701): the capped
`inversionContextBonus` sum has exactly four contributors —
`completeTriadInversionBonus`, `stepwiseBassInversionBonus` (stepwise-from-previous),
`stepwiseBassLookaheadBonus` (lookahead-to-next), `sameRootInversionBonus`. The
`nextRoot/consecutive/recentRoot/weakBeat` signals named in the old comment are not in
the sum at all. New comment (quoted):

```
/// Maximum total context bonus that can be applied to any single inversion
/// candidate across the inversion temporal signals combined — the four that
/// actually feed the sum in bassDependentContextualBonuses(): stepwise
/// (bassIsStepwiseFromPrevious), lookahead (bassIsStepwiseToNext), sameRoot
/// (previousRootPc == rootPc), and completeTriad.  The formerly-listed
/// nextRoot / consecutive / recentRoot / weakBeat signals were never wired
/// into this sum.
/// Prevents runaway stacking when multiple signals fire simultaneously.
/// Currently INERT on every code path: the cap is never overridden (both
/// presets inherit this 2.0 default) and the four bonuses sum to at most
/// 1.85 (Baroque/default) or 0.75 (Jazz), so std::min() never clamps.  See
/// docs/scoring_model.md §4 ("currently inert" paragraph) for the full story.
/// Range: 0.0–10.0.  Default: 2.0.
double maxTotalInversionContextBonus = 2.0;
```

No `scoring_model.md` change required — §4 already documents the "currently inert" cap
(per the doc pass `af39f28179`); this comment now points to it.

---

## §4 — Verification

| Gate | Result | Required |
|---|---|---|
| Build (composing + notation + tests + batch + GUI) | exit 0, clean | green |
| `composing_tests` | **498 / 498** | 498 ✓ |
| `notation_tests` | **52 / 52** | green ✓ |
| `pipeline_snapshot_tests` | **11 / 11, ZERO diffs** (no goldens refreshed) | 11/11 zero diffs ✓ — **decisive byte-identity proof** (the snapshot harness calls `analyzeSection`) |
| Python (`tools/tests`) | **54 OK** | 54 ✓ |
| BIR Baroque (`characterise_bir_false.py`) | **13** (stable across 2 runs) | 13 ✓ |
| BIR Jazz | **8, then 9** (run-to-run) | documented 7 — see below |

**BIR byte-identity proof (move + rider are batch-neutral):** `git diff --stat` shows
no batch-path behavioral source changed — `chordanalyzer.cpp`, `batch_analyze.cpp`,
`regionanalyzer.cpp`, `sparsechordrefinement.cpp`, `keyresolver/keymodeanalyzer/
harmonicsegmenter/metricweights/regiontonecollector` are all untouched; the only
edited `composing_analysis` file is `chordanalyzer.h` (**comment-only**, default
unchanged), and the new `sectionanalyzer.cpp` is never called by `batch_analyze`.
Therefore `batch_analyze.exe` is behaviorally identical to HEAD, so the batch/BIR
result is unchanged by this work. Baroque confirms it (13 = exact baseline match).

**Jazz nondeterminism finding (pre-existing, NOT move-induced):** consecutive Jazz
corpus runs at this same build produced BIR=false = **8** then **9**. Several Jazz
cases sit at `margin=0.000` (exact ties); the parallel batch path resolves them
nondeterministically, so the Jazz count varies run-to-run in a 7–9 band. The
documented "7" (last recorded at `90a52b5fee`) is one sample within that band. This is
a property of the Jazz batch path, independent of Stage 2.1 (proven above). Recommend
reconciling/pinning Jazz determinism in **Stage 2.2's single re-baseline** (STATUS
already defers metric reconciliation there). **Decision sought:** treat as a
pre-existing finding to log, not a Stage-2.1 blocker (the move is provably neutral).

`tools/corpus` left regenerated in **Baroque** state.

---

## §5 — Deviations / unknowns (never-guess ledger)

1. **Pass-0 dependency** — resolved by Option D (user decision), not silently.
2. **`resolveKeyAndMode` + dead weight shims** STAY (re-derived; deviate from the
   suggested MOVE list — justified in §1).
3. **`notationannotate_tests` kept in notation** (re-pointed include) rather than
   relocated — both permitted; chose lowest-risk. Ledger neutral.
4. **`analyzeSection` comment** "Inlines Passes 0–4" → "Inlines Passes 1–4" (Pass 0 is
   now injected — factual, not a logic change).
5. **Jazz BIR nondeterminism** — newly characterized here (8 vs 9 vs documented 7);
   pre-existing, flagged for Stage 2.2 (§4).
6. **Includes in trimmed `notationcomposingbridgehelpers.cpp`** left intact (a few are
   now unused, e.g. `<limits>`); not pruned — conservative relocate-only.

---

## §6 — Commit proposal (TWO commits — awaiting Cowork confirmation)

**Commit A (rider, separable):**
```
docs(code): correct stale maxTotalInversionContextBonus doc-comment (chordanalyzer.h)

Delete the never-implemented "Baroque: 2.5 / Jazz: 0.6" cap lines and the
incorrect eight-signal list. The capped inversionContextBonus sum has exactly
four contributors (stepwise, lookahead, sameRoot, completeTriad — verified
against bassDependentContextualBonuses); nextRoot/consecutive/recentRoot/weakBeat
were never wired in. Note the cap is currently inert (sums 1.85 Baroque / 0.75
Jazz < 2.0 default) and point to scoring_model.md §4. Comment-only; no behavior
change.
```

**Commit B (move):**
```
refactor: move analyzeSection + section-level analysis into composing module (Phase 4c / Stage 2.1)

Relocate analyzeSection(), key/mode stabilization, and cadence / pivot detection
out of notation/internal/notationcomposingbridgehelpers.cpp into the new
composing/analysis/section/sectionanalyzer.{h,cpp} (mu::composing::analysis), so
the analysis layer lives in the composing module (Dependency Rule §3.3). Unblocks
Stage 2.2 (batch must call the section-level pass without linking notation) and
Phase E/E4 (cadence layer co-located with the function layer).

Pass-0 boundary detection stays in the notation-side analyzeHarmonicRhythm wrapper
(config + debug-capture); analyzeSection now takes the HarmonicRegion stream as an
injected parameter, keeping composing_analysis independent of the notation and
configuration/IoC layers. The six call sites compute rawRegions via the unchanged
analyzeHarmonicRhythm and pass it in.

Byte-identical behavior: pipeline_snapshot_tests 11/11 with zero diffs (the harness
calls analyzeSection directly); composing 498/498; notation 52/52; 54 Python OK.
Batch/BIR unaffected — no batch-path source changed (Baroque BIR=false 13, exact
baseline match). Jazz BIR=false is nondeterministic (8–9 across runs, exact-tie
parallelism) independent of this change; flagged for the Stage 2.2 re-baseline.
```

Both await Cowork confirmation before `git commit`. STATUS.md / ARCHITECTURE.md
updates to follow at commit time (text proposed in §2).
