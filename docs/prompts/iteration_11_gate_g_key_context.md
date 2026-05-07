# Iteration 11: Gate G-E — MinorAdd6 → HalfDim7 via leading-tone key context

## ⚠ Critical behaviour rules

- **Read first, report exact lines, then implement.**
- Make only the changes listed. Nothing else.
- Do NOT run `--update-goldens` until every pipeline snapshot change is verified correct.
- Stop conditions apply at both the pipeline snapshot step and corpus step.
  If BIR=false increases > 50 above 788: STOP before committing.
- If the build fails or any test regresses: STOP and report verbatim.

---

## Background

The 48 MinorAdd6 enharmonic-pair errors are the largest remaining BIR=true class.
They have been unchanged since Iteration 6b. Gates G-B/C/D (temporal, stepwise-bass)
never fire on them because the bass always arrives by leap in these passages.

The reference corpus (DCML) consistently labels these chords as the leading-tone
half-diminished seventh (viiø7) rather than a supertonic minor-add-six. The reason is
functional harmony: in tonal music (major or minor), the half-diminished seventh rooted
on the leading tone is an extremely common pre-dominant or pre-tonic chord; the
supertonic minor-add-six with the same pitch classes is rare as a root-position reading
in Bach's style.

The leading tone of any key is always (tonicPc + 11) % 12. The supertonic (the winner's
root when this situation arises) is always (tonicPc + 2) % 12. The condition is therefore:

  winner quality = MinorAdd6
  AND a HalfDim7 alt exists at (winnerRootPc + 9) % 12  ← already checked in G block
  AND that alt's rootPc == (tonicPc + 11) % 12            ← the leading tone

This is Gate G-E: categorical but key-conditioned — no temporal signals required.
Unlike the reverted categorical Gate G (which fired unconditionally, producing 96%
false positives), Gate G-E is restricted to the specific case where the HalfDim7
interpretation is functionally the leading-tone chord of the current key.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=109, BIR=false=788

---

## Step 2 — Read and confirm current state

### A. Gate G block in chordanalyzer.cpp

Read the `if (prefs.preferMinorOverMajorAdd6)` block. Confirm and report:

1. The exact opening line of the block and its closing line.
2. The line where `halfDimAltIdx` is initialised (sentinel value and type).
3. The loop that searches for the HalfDim7 alt — confirm it searches for quality
   `HalfDiminished7` (or whatever `ChordQuality` enum value is used) at
   `expectedAltRoot = (winnerRootPc + 9) % 12`.
4. The exact conditions of Gates G-B, G-C, G-D (one line each) — confirm each
   requires `context != nullptr` (or equivalent).
5. The `didEnharmonicFlip` variable — confirm it is shared across all G-B/C/D gates
   and prevents double-firing.
6. Where `winnerIsMinor` and `winnerHasAddedSixth` are declared and confirmed true
   before this block. (Gate G-E needs both in scope.)

### B. KeySigMode enum and tonicPc computation

Read `chordanalyzer.h` (or wherever `KeySigMode` is defined). Report:
1. All enum values of `KeySigMode`.
2. Which values correspond to major-type keys (tonicPc computed from kSF directly).
3. Which values correspond to minor-type keys (tonicPc is a minor third below the
   relative major tonic, i.e. (majorTonicPc + 9) % 12).

Also search the codebase for any existing utility function that computes tonicPc
from `keySignatureFifths` and `KeySigMode`. If one exists, report its name, location,
and signature. If none exists, confirm this.

### C. Parameters in scope at the Gate G block

Confirm that `keySignatureFifths` (int) and `keyMode` (KeySigMode) are in scope
as named variables at the Gate G block location (they are parameters to `analyzeChord`).

Report all findings from A, B, C before proceeding.

---

## Step 3 — Implement Gate G-E

### Location

Inside the `if (prefs.preferMinorOverMajorAdd6)` block, immediately BEFORE the
existing Gate G-B check (i.e., before the `if (!didEnharmonicFlip && context != nullptr
&& context->nextRootPc ...` line). Gate G-E fires first because it uses a stronger
categorical condition; if it fires, `didEnharmonicFlip = true` prevents G-B/C/D
from also firing.

### tonicPc computation

If an existing utility function was found in Step 2B, use it. Otherwise, compute
inline using:

```cpp
// Tonic pitch class of the current key.
const int majorTonicPc = ((keySignatureFifths * 7) % 12 + 12) % 12;
const bool isMinorKey = /* true for all minor-type KeySigMode values identified in Step 2B */;
const int tonicPc     = isMinorKey ? (majorTonicPc + 9) % 12 : majorTonicPc;
const int leadingTonePc = (tonicPc + 11) % 12;
```

(Replace `isMinorKey` with the correct check for the `keyMode` variable based on
the enum values confirmed in Step 2B.)

### Gate G-E code

```cpp
        // ── Gate G-E: leading-tone key-context gate ────────────────────────────────
        //
        // The half-diminished seventh on the leading tone (viiø7) is the standard
        // functional reading in tonal music when the pitch-class set is shared with
        // a MinorAdd6 on the supertonic.  No temporal signals are required — the key
        // context alone is sufficient evidence.
        //
        // Fires when: winner is MinorAdd6 AND the HalfDim7 alt is rooted on the
        // leading tone of the current key.  Placed before G-B/C/D so temporal gates
        // do not double-fire.
        if (!didEnharmonicFlip
            && winnerIsMinor && winnerHasAddedSixth
            && halfDimAltIdx < results.size()
            && results[halfDimAltIdx].identity.rootPc == leadingTonePc) {
            std::swap(results[0], results[halfDimAltIdx]);
            didEnharmonicFlip = true;
        }
```

Use the same indentation level as the surrounding G-B/C/D gates.
The `tonicPc` / `leadingTonePc` computation should appear immediately before this
`if` block, still inside the `if (prefs.preferMinorOverMajorAdd6)` block.

Report the exact line range inserted.

---

## Step 4 — Build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Build must pass with no errors. Report any warnings.

---

## Step 5 — Composing and notation tests

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407, 53/53. Any regression: STOP.

---

## Step 6 — Pipeline snapshot tests

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Gate G-E requires no temporal context, so it fires on the bridge path too.
Golden mismatches are expected if any of the 11 snapshot scores contain
MinorAdd6 chords in the supertonic position.

**If mismatches occur:**
1. Do NOT run `--update-goldens` yet.
2. For each changed score: identify the measure, the before/after chord symbols,
   and the key context. Verify the new symbol is the leading-tone half-diminished
   reading in the correct key.
3. Report all changes and verification before updating goldens.

**If no mismatches:** report that too and proceed to Step 7.

---

## Step 7 — Update goldens if needed

Only after verifying all changes are correct:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 8 — Corpus run

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected:
- BIR=true: < 109 (some or all of the 48 MinorAdd6 errors fixed)
- BIR=false: ≤ 838 (788 + 50 stop threshold)

**If BIR=false > 838: STOP immediately. Do not commit. Report:**
- The exact new BIR=false count
- Run the diagnostic from Iteration 10's script pattern to identify which chords
  are now being wrongly promoted to inversions by Gate G-E

**If BIR=false ≤ 838 and BIR=true has improved:** record new baselines and proceed.

**If BIR=true is unchanged (0 of 48 fixed):** the leading-tone condition is not
matching these specific errors. Report the key signatures of the 48 error cases
and the computed leading tones — there may be a bug in the tonicPc formula or
the mode detection.

---

## Step 9 — Update baselines and push

Update `build_and_test.md`:
- Replace BIR=true baseline with the new number
- Replace BIR=false ceiling with the new number (if it changed)
- Update the attribution line

Update `STATUS.md` with a 2026-05-06 entry:
- Gate G-E added: MinorAdd6 → HalfDim7 via leading-tone key context
- New BIR=true and BIR=false baselines
- Commit hash

```
cd C:\s\MS && git add -A && git commit -m "Iter 11: Gate G-E — MinorAdd6→HalfDim7 leading-tone key-context gate" && git push
```

---

## Step 10 — Report

```
State verification (A–C):
  halfDimAltIdx sentinel:           <type and value>
  HalfDim7 quality enum value:      <name>
  didEnharmonicFlip shared:         yes
  winnerIsMinor / winnerHasAddedSixth in scope: yes
  KeySigMode minor values:          <list>
  Existing tonicPc utility:         <name and location> / not found
  keySignatureFifths / keyMode in scope: yes

Gate G-E inserted:
  Insertion point (before Gate G-B at line): N
  Inserted block lines:              N–N
  leadingTonePc computation:         inline / utility function <name>
  isMinorKey check:                  <exact condition used>

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
