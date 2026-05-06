# Fix: results[] cap exhaustion blocking inversion correction

## ⚠️ Status: code edits already applied — build and test only

The `chordanalyzer.cpp` edits described below have already been made. **Do not
re-apply them.** Verify they are present (grep for "Guaranteed inversion
alternative" and confirm the `buildResult` lambda exists above the filling
loop), then go directly to the Verification section: build, run tests, run
`analyze_inversion_errors.py`, and return the report.

---

## Context loading — do this first

1. `CLAUDE.md` — standing instructions, build/test commands, autonomous-operation scope.
2. `STATUS.md` — top summary line and the `2026-05-04` entries only.
3. `src/composing/analysis/chord/chordanalyzer.cpp` — specifically:
   - The `RawCandidate` struct, scoring loop, and results-filling loop (~lines 1668–1740)
   - The post-ranking inversion correction (~lines 1859–1938)

---

## What was diagnosed

After commit `31ea993f46` (threshold de-inflation + sus structural fourth), inversion
confusion sits at **8.1%** of GT-paired cells. The threshold fix was successful: the
correct chord (e.g. Gm when Bb6 wins) now clears the admission threshold. But the
post-ranking inversion correction still cannot fire because `results[]` is capped at 3
entries and all 3 slots are consumed by same-rootPc variants (Bb, Bb7, BbMaj7, …)
before the correct different-rootPc chord can enter.

Diagnostic numbers (151 genuine three-way-confirmed bassIsRoot errors, post-fix corpus):
- 88.1% have `margin < 0.25` — winner barely beats competitors
- 100% have a clean Major/Minor alternative somewhere in rawCandidates
- 80.1% (121 cases): all 3 results[] slots exhausted by same-rootPc candidates; correct
  chord never admitted despite clearing the threshold
- Blockers A (seventh exemption) and B (margin ≥ 0.70): 1 case each — negligible

The post-ranking correction at lines ~1859–1938 searches `results[1]` and `results[2]`
for a Major/Minor candidate with `rootPc != results[0].rootPc`. It never finds one
because Bb, Bb7, and BbMaj7 all have the same rootPc as the Bb6 winner.

---

## The fix

**Goal:** when the winner is a bass-root candidate (`rootPc == bassPc`), guarantee that
`results[]` contains at least one entry with a different rootPc, so the post-ranking
correction has something to evaluate.

**Mechanism:** after the normal results-filling loop, if the winner has `rootPc == bassPc`
and every entry in `results[]` shares the winner's rootPc, find the highest-scoring
different-rootPc `RawCandidate` that clears the threshold and build it into a
`ChordAnalysisResult`, appending it to `results[]` as an extra slot. The post-ranking
correction then finds it at `results[1]` or later.

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`

### Where to add the code

After the existing results-filling loop (which ends around line 1740, just before the
`// ── Inversion / bass-root bias correction ──` comment), insert a new block:

```cpp
// ── Guaranteed inversion alternative ─────────────────────────────────────────
//
// When the winner is a bass-root candidate (rootPc == bassPc), the results[]
// cap of 3 is routinely exhausted by same-rootPc extensions/variants (e.g.
// Bb, Bb7, BbMaj7) before the correct enharmonic alternative (e.g. Gm7) can
// enter.  The post-ranking inversion correction requires a different-rootPc
// Major/Minor candidate in results[] to function.
//
// If every entry in results[] shares the winner's rootPc, scan rawCandidates
// for the highest-scoring different-rootPc candidate that clears the threshold
// and append it.  The correction then has a target to evaluate and potentially
// promote.
//
// This append only fires when:
//   (a) the winner is a bass-root candidate (rootPc == bassPc), AND
//   (b) no different-rootPc candidate already made it into results[].
// It is a no-op for all other cases.
if (!results.empty()
    && bassPc >= 0
    && results.front().identity.rootPc == static_cast<int>(bassPc))
{
    const int winnerRootPc = results.front().identity.rootPc;
    const bool hasDiffRoot = std::any_of(results.begin(), results.end(),
        [winnerRootPc](const ChordAnalysisResult& r) {
            return r.identity.rootPc != winnerRootPc;
        });

    if (!hasDiffRoot) {
        for (const RawCandidate& rc : rawCandidates) {
            if (rc.score < threshold)        { break; }
            if (rc.rootPc == winnerRootPc)   { continue; }

            // Build this candidate into a ChordAnalysisResult using the same
            // logic as the main filling loop above.  Duplicate only what is
            // needed: quality normalisation, extension detection, degree
            // assignment, and result construction.
            // [See implementation note below.]
            break;
        }
    }
}
```

### Implementation note — avoiding code duplication

The `ChordAnalysisResult`-building logic inside the main filling loop (post-scoring
quality normalisation, `detectExtensions`, degree assignment, etc.) is non-trivial.
Rather than duplicating it verbatim, **extract it into a private helper function** first:

```cpp
// In the anonymous namespace or as a static helper:
// ChordAnalysisResult buildResult(const RawCandidate& rc,
//                                 const std::array<double,12>& pcWeight,
//                                 const std::array<int,12>& tpcForPc,
//                                 int bassPc, int bassTpc,
//                                 int keyTonicPc,
//                                 const std::array<int,7>& scale);
```

Refactor the main filling loop to call `buildResult(...)`, then call the same helper
in the guaranteed-inversion-alternative block. This keeps the logic in one place and
makes both sites easier to maintain.

If extracting the helper turns out to be unexpectedly complex in this session, an
acceptable short-term alternative is to duplicate the building logic verbatim inside
the new block with a `// TODO: deduplicate into helper` comment — but the helper
extraction is strongly preferred.

---

## Constraints

- The extra append must only fire for **bass-root winners with no existing diff-rootPc
  entry** — the guard conditions above enforce this.
- Do **not** change `kScoreThresholdRatio`, `inversionSuspicionMargin`,
  `inversionBonusReduction`, or any other scoring constants.
- Do **not** touch `chordanalyzer_catalog.musicxml`.
- Do **not** commit — report results and wait for sign-off.

---

## Verification

### Build and test

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.
**Pass criterion:** 407/407 tests pass, RealDiff ≤ 4.

### Spot-check

Run `tools/analyze_inversion_errors.py` on the post-fix corpus data. The
"no diff-rootPc Major/Minor alt in results[] cap of 3" count (currently 121) should
drop substantially. The "should-have-fired" count should increase (more cases now have
a diff-rootPc alt to evaluate) and the remaining blocker breakdown should shift.

### Report format

```
Build:              pass / fail
Tests:              N/N pass
RealDiff:           before=4, after=N
Helper extracted:   yes / no (duplicated with TODO)
analyze_inversion_errors.py delta:
  cap-exhaustion cases before: 121
  cap-exhaustion cases after:  N
  should-have-fired before:    6
  should-have-fired after:     N
Regressions:        none / <description>
```
