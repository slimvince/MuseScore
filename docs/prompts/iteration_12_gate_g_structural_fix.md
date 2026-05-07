# Iteration 12: Structural fix + Gate G-E (MinorAdd6 → HalfDim7)

## ⚠ Critical behaviour rules

- **Read first, report exact lines, then implement.**
- Make only the changes listed. Nothing else.
- Do NOT run `--update-goldens` until every pipeline snapshot change is verified correct.
- Stop conditions apply at both the pipeline snapshot step and corpus step.
  If BIR=false increases > 50 above 788: STOP before committing.
- If the build fails or any test regresses: STOP and report verbatim.

---

## Background — two problems identified in Iteration 11

### Problem 1: Structural — G block is unreachable for MinorAdd6 winners

The outer guard at chordanalyzer.cpp line 1960 is:

```cpp
if (winnerBassIsRoot && winnerQualityTargeted) {
```

`winnerQualityTargeted` is `{Major, Minor}` — MinorAdd6 passes this check.
But inside, `kCleanQualities = {Major, Minor}` excludes HalfDiminished, so
`bestAlt == nullptr` for every MinorAdd6 winner. The `if (bestAlt != nullptr)`
block at line 1988 is never entered. The G block (currently lines 2073–2131)
is structurally unreachable.

**Fix**: Move the entire G block to a new location between the closing `}`
of `if (bestAlt != nullptr)` (line 2202) and the closing `}` of the outer
`if (winnerBassIsRoot && winnerQualityTargeted)` block (line 2203). The
new block runs for any winner inside the outer guard — no dependency on
bestAlt.

### Problem 2: Conditional — leading-tone condition matches only 7 of 48 cases

Iteration 11's condition `altRoot == (keyTonicPc + 11) % 12` (viiø7) fires
for only 7 of the 48 MinorAdd6 errors. The dominant pattern (21 cases) is
`altRoot == (keyTonicPc + 2) % 12` — the HalfDim7 is the supertonic seventh
(iiø7), the standard pre-dominant in minor keys (e.g. Cm6 in G minor → Aø7).

Both are musically unambiguous readings in tonal/Baroque harmony. The remaining
20 cases need separate investigation and are NOT addressed in this iteration.

**Fix**: Gate G-E condition becomes:
```
altRoot == (keyTonicPc + 11) % 12   // viiø7 — leading tone  (7 cases)
|| altRoot == (keyTonicPc + 2) % 12  // iiø7  — supertonic   (21 cases)
```

Expected: 28 of 48 MinorAdd6 errors fixed; BIR=true ≤ 81.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=109, BIR=false=788

---

## Step 2 — Read and confirm current state

Read `src/composing/analysis/chord/chordanalyzer.cpp` at the following
line ranges and confirm each item:

A. **Line 1960** — confirm the outer guard is exactly:
   `if (winnerBassIsRoot && winnerQualityTargeted) {`

B. **Line 1988** — confirm `if (bestAlt != nullptr) {` opens here.

C. **Line 1998** — confirm `bool didEnharmonicFlip = false;` is declared
   INSIDE `if (bestAlt != nullptr)`.

D. **Lines 2073–2131** — confirm this is the G block. Report:
   - The exact opening line of the G block comment (should be
     `// ── Gates G-B / G-C / G-D ...`).
   - The exact line where `const bool winnerIsMinor = !winnerIsMajor;` appears.
   - The exact closing `}` of the `if (winnerIsMinor && winnerHasAddedSixth)`
     sub-block.
   - The exact line where the `if (winnerIsMinor && winnerHasAddedSixth)` outer
     closes (one `}`) and where `}` closes `if (prefs.preferMinorOverMajorAdd6)`
     on line 2132.

E. **Line 2202** — confirm `}` closes `if (bestAlt != nullptr)`.

F. **Line 2203** — confirm `}` closes `if (winnerBassIsRoot && winnerQualityTargeted)`.

G. **Line 2205** — confirm Gate H comment begins here (after a blank line at 2204).

H. **Line 1664** — confirm `keyTonicPc` is in scope:
   `const int keyTonicPc = (ionianTonicPc + keyModeTonicOffset(keyMode)) % 12;`
   Confirm this is at function scope, visible at the insertion point (between
   lines 2202 and 2203).

Report all line numbers and confirm each item before proceeding.

---

## Step 3 — Remove the old G block

In `src/composing/analysis/chord/chordanalyzer.cpp`, remove the entire old G
block from inside the `if (prefs.preferMinorOverMajorAdd6)` block.

The block to remove starts at the G block comment line (approx line 2073,
`// ── Gates G-B / G-C / G-D: Minor-add6 ↔ HalfDim7 (temporal context required)`)
and ends at the closing `}` of `if (winnerIsMinor && winnerHasAddedSixth)` on
approximately line 2131.

Do NOT remove `}` that closes `if (prefs.preferMinorOverMajorAdd6)` at line 2132
or `}` that closes `if (bestAlt != nullptr)` at line 2202.

Report the exact lines removed.

---

## Step 4 — Insert the new standalone G block

Immediately BEFORE the closing `}` of `if (winnerBassIsRoot && winnerQualityTargeted)`
(which after Step 3 is the line directly following the closing `}` of
`if (bestAlt != nullptr)`), insert the following block. Use the same indentation
level as Gate H (one level inside the outer function body — same as the
`if (winnerBassIsRoot && ...` line itself):

```cpp
        // ── Gates G-E / G-B / G-C / G-D: Minor-add6 ↔ HalfDim7 ─────────────────────
        //
        // MinorAdd6 and HalfDim7 share identical pitch classes.
        // kCleanQualities excludes HalfDiminished, so this block runs independently
        // of the bestAlt path above.
        //
        // Gate G-E (key-context): fires when the HalfDim7 alt is a functional chord
        // of the current key — either the leading-tone seventh (viiø7, alt root at
        // tonicPc+11) or the supertonic seventh (iiø7, alt root at tonicPc+2).
        // No temporal signals required.
        //
        // Gates G-B/C/D: temporal fallbacks for the remaining cases.
        if (prefs.preferMinorOverMajorAdd6
            && winner.identity.quality == ChordQuality::Minor
            && hasExtension(winner.identity.extensions, Extension::AddedSixth)) {
            const int gExpectedAltRoot = (winner.identity.rootPc + 9) % 12;
            // Find the HalfDim7 alt in results[].
            size_t halfDimAltIdx = results.size();
            for (size_t i = 1; i < results.size(); ++i) {
                if (results[i].identity.quality == ChordQuality::HalfDiminished
                    && results[i].identity.rootPc == gExpectedAltRoot) {
                    halfDimAltIdx = i;
                    break;
                }
            }
            if (halfDimAltIdx != results.size()) {
                bool didGFlip = false;
                // Gate G-E: leading-tone key-context gate.
                // The half-diminished seventh is the standard functional reading when
                // it is rooted on the leading tone (viiø7) or supertonic (iiø7) of
                // the current key.  No temporal signals required.
                const int gLeadingTonePc  = (keyTonicPc + 11) % 12;
                const int gSupersonicPc   = (keyTonicPc + 2) % 12;
                if (!didGFlip
                    && (results[halfDimAltIdx].identity.rootPc == gLeadingTonePc
                        || results[halfDimAltIdx].identity.rootPc == gSupersonicPc)) {
                    std::swap(results[0], results[halfDimAltIdx]);
                    didGFlip = true;
                }
                // Gate G-B: next region's inferred root matches the HalfDim root.
                // Strong forward evidence the harmony continues on that root.
                if (!didGFlip
                    && context != nullptr
                    && context->nextRootPc != -1
                    && context->nextRootPc == gExpectedAltRoot
                    && context->bassIsStepwiseToNext) {
                    std::swap(results[0], results[halfDimAltIdx]);
                    didGFlip = true;
                }
                // Gate G-C: HalfDim root appears in the 3-region window AND bass
                // is moving stepwise from the previous region.
                if (!didGFlip
                    && context != nullptr
                    && context->bassIsStepwiseFromPrevious) {
                    const auto& rpc = context->recentRootPcs;
                    if (rpc[0] == gExpectedAltRoot
                        || rpc[1] == gExpectedAltRoot
                        || rpc[2] == gExpectedAltRoot) {
                        std::swap(results[0], results[halfDimAltIdx]);
                        didGFlip = true;
                    }
                }
                // Gate G-D: two or more consecutive stepwise bass moves ending here.
                if (!didGFlip
                    && context != nullptr
                    && context->consecutiveBassStepwiseCount >= 2) {
                    std::swap(results[0], results[halfDimAltIdx]);
                    didGFlip = true;
                }
            }
        }
```

Report the exact line range inserted.

---

## Step 5 — Build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Build must pass with no errors. Report any warnings.

---

## Step 6 — Composing and notation tests

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407, 53/53. Any regression: STOP.

---

## Step 7 — Pipeline snapshot tests

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Gate G-E is categorical (no temporal signals) so it fires on the bridge path
too. Golden mismatches are expected if any of the 11 snapshot scores contain
MinorAdd6 chords where the HalfDim7 alt is rooted on (keyTonicPc+11)%12 or
(keyTonicPc+2)%12.

**If mismatches occur:**
1. Do NOT run `--update-goldens` yet.
2. For each changed score: identify the measure, the before/after chord symbols,
   and the key context. Verify the new symbol is the correct viiø7 or iiø7
   reading in the current key.
3. Report all changes and verification before updating goldens.

**If no mismatches:** report that and proceed to Step 8.

---

## Step 8 — Update goldens if needed

Only after verifying all changes are correct:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 9 — Corpus run

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected:
- BIR=true: ≤ 81 (109 − 28 minimum; ideally closer to 61 if all 48 fire)
- BIR=false: ≤ 838 (788 + 50 stop threshold)

**If BIR=false > 838: STOP immediately. Do not commit. Report:**
- The exact new BIR=false count
- Run the following diagnostic inline (do not save) to identify which chords
  are being wrongly promoted:

```python
import json, glob, os

corpus_dir = r'C:\s\MS\tools\corpus'
new_fp = []
for f in glob.glob(os.path.join(corpus_dir, '*.json')):
    data = json.load(open(f))
    for region in data.get('regions', []):
        if region.get('bassIsRoot') is False and region.get('referenceIsRoot') is True:
            w = region.get('winner', {})
            alts = region.get('alternatives', [])
            new_fp.append({
                'file': os.path.basename(f),
                'measure': region.get('measure'),
                'winnerQuality': w.get('quality'),
                'winnerRoot': w.get('rootPc'),
                'alts': [(a.get('quality'), a.get('rootPc')) for a in alts[:3]],
            })

from collections import Counter
print(f"Total new FP: {len(new_fp)}")
q = Counter(x['winnerQuality'] for x in new_fp)
print("By winner quality:", q.most_common())
```

**If BIR=true is unchanged (0 of 48 fixed):** the HalfDim7 alt is not present
in results[] for these cases. Report the first 5 error cases with their
key signatures and computed (keyTonicPc+11)%12 and (keyTonicPc+2)%12 values.

**If BIR=false ≤ 838 and BIR=true has improved:** record new baselines.

---

## Step 10 — Update baselines and push

Update `build_and_test.md`:
- Replace BIR=true baseline with the new number
- Replace BIR=false ceiling with the new number (if it changed)
- Update the attribution line

Update `STATUS.md` with a 2026-05-06 entry:
- Gate G-E added: MinorAdd6 → HalfDim7 via leading-tone/supertonic key context (viiø7 + iiø7)
- Structural fix: G block moved outside `if (bestAlt != nullptr)` (was unreachable)
- New BIR=true and BIR=false baselines
- Commit hash

```
cd C:\s\MS && git add -A && git commit -m "Iter 12: Gate G-E — MinorAdd6→HalfDim7 key-context gate (viiø7+iiø7), structural fix" && git push
```

---

## Step 11 — Report

```
State verification (A–H confirmed):
  Outer guard line:                   N (winnerBassIsRoot && winnerQualityTargeted)
  if (bestAlt != nullptr) opens:      line N
  didEnharmonicFlip declared inside:  yes (line N)
  Old G block:                        lines N–N
  if (bestAlt != nullptr) closes:     line N
  Outer block closes:                 line N
  Gate H begins:                      line N
  keyTonicPc in scope at insertion:   yes (line N)

Changes:
  Old G block removed:                lines N–N (N lines)
  New G block inserted:               lines N–N
  Gate G-E condition:                 altRoot == (keyTonicPc+11)%12 || (keyTonicPc+2)%12

Build:                        pass / fail
Composing tests:              407/407, RealDiff=N
Notation tests:               53/53
Pipeline snapshot tests (before update):  N/N pass / N mismatches
  Changed scores:             <list or "none">
  Changes verified correct:   yes / n/a
Pipeline snapshot tests (after update):   N/N pass

Corpus:
  BIR=true:                   N (was 109 — MinorAdd6 fixed: N of 48)
  BIR=false:                  N (was 788)
  Gate G-E BIR=false impact:  N new false positives (expected: ≤ 50)

build_and_test.md updated:    yes
STATUS.md updated:            yes
GitHub push:                  done / commit hash
Unexpected findings:          none / <describe>
```
