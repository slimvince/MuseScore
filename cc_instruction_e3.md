# CC Instruction: E3 Gate Decoupling + G-E Phantom Fix

## Pre-reading (mandatory)

Read `C:\s\MS\STATUS.md` (header only) and `C:\s\MS\build_and_test.md` before starting.
Read `C:\s\MS\cc_e3_investigation_report.md` — Q1 gate inventory and Q6 anomalies are
the direct input to this instruction.

Also read `src/composing/analysis/chord/chordanalyzer.cpp`
`applyPostScoringGates` (full, lines ~1885–2458) before making any changes.

Current HEAD: `a693b6ba82`. Working tree clean.
Baseline: 407/407 composing, 52/52 notation, 11/11 pipeline snapshots.

---

## Background

The E3 investigation (cc_e3_investigation_report.md) found that E3's original
architectural goal is already done: Gates A–L live in a standalone
`applyPostScoringGates()` called after `analyzeChord`. The two actionable
findings from Q6 are:

**Q6 item 1 — Structural gate coupling (highest concern)**
Gates H, I, J, K, L are nested inside the outer
`inversionSuspicionMargin > 0 && inversionBonusReduction < 1.0 && results.size() >= 2 && distinctPcs >= 3`
guard block. These gates are logically independent of the bias correction and
should not inherit its preconditions. All active presets have
`inversionSuspicionMargin = 0.70 > 0` and `inversionBonusReduction = 0.0 < 1.0`,
so this fix is **byte-identical** for all current corpus runs.

**Q6 item 3 — G-E phantom HalfDim**
Gate G-E pulls a HalfDim from `rawCandidates` and appends it to `results[]`
even when none of the G sub-gates fire, leaving a phantom alternative in the
ranked list. The phantom does not change `results[0]` (the winner), but it
pollutes the alternatives list beyond the "top-3 + diff-root" cap. Fix: remove
the appended HalfDim if no G sub-gate fires.

**Q6 item 4 — Float literals → named constants**
Gates I, K, L use `0.45f`, `0.20f`, `0.35f` margin guards; these should be
named constants matching the rest of the file's double-precision style.

This instruction covers all three items in one commit.

---

## Task 1 — Decouple structural gates from outer guard

### 1a — Move winner captures to the function top

At the very top of `applyPostScoringGates` (after the `buildResult` lambda,
before any `if` block), add an early-return guard and move the winner captures:

```cpp
if (results.empty()) { return; }

const ChordAnalysisResult& winner         = results[0];
const ChordQuality originalWinnerQuality  = winner.identity.quality;
const int originalWinnerRootPc            = winner.identity.rootPc;
const bool originalWinnerHasAddedSixth    =
    hasExtension(winner.identity.extensions, Extension::AddedSixth);
const bool winnerBassIsRoot               = (winner.identity.rootPc == winner.identity.bassPc);
```

Add the following comment immediately before these captures:
```cpp
// Pre-sort winner captures.  Defined here (before any gate block) so both the
// inversion-correction block (A–G) and the independent structural gates (H, I,
// J, K, L) can use them without repeating the capture.
// IMPORTANT: winner is a live reference — tracks results[0] through any swap
// or re-sort.  Use originalWinner* when pre-swap state is needed (Sub-9a fix).
```

### 1b — Remove the duplicate captures from inside the outer guard

Inside the outer `if (prefs.inversionSuspicionMargin > 0.0 && ...)` block,
delete the four lines that currently define `winner`, `originalWinnerQuality`,
`originalWinnerRootPc`, `originalWinnerHasAddedSixth`, and `winnerBassIsRoot`
(they are now defined above). Do not remove the comment block that explains the
Sub-9a capture rationale — keep it, just remove the capture statements
themselves.

### 1c — Move Gates H, I, K, L, J outside the outer guard

The outer guard currently closes just before Gate H (there is a `}` that ends
the `if (inversionSuspicionMargin > 0.0 && ...)` block). Gates H, I, K, L, J
currently sit inside that outer guard.

Move the gate blocks for **Gate H** (lines ~2276–2317), **Gate I** (~2328–2352),
**Gate K** (~2364–2388), **Gate L** (~2401–2422), and **Gate J** (~2435–2455)
to **after** the closing `}` of the outer guard, maintaining their existing
relative order (H, I, K, L, J). Each gate already has its own appropriate
preconditions (`winnerBassIsRoot`, quality checks, `results.size() >= 2`,
`gateCtx.keyTonicPc >= 0`), which now serve as their sole guards.

Update the in-code comment for the outer guard block to read:
```
// ── Inversion / bass-root bias correction + enharmonic gates (A–G) ─────────
//
// Gated on inversionSuspicionMargin and inversionBonusReduction because all
// these blocks depend on the margin-based winner re-sort or on the
// preferMinorOverMajorAdd6 setting. Structural gates H–L are independent
// and appear below.
```

---

## Task 2 — Fix the G-E phantom HalfDim

In the G-E/G-B/G-C/G-D block, Gate G-E conditionally appends a HalfDim from
`rawCandidates` when it is absent from `results[]`:

```cpp
if (halfDimAltIdx >= results.size()) {
    for (const auto& rc : gateCtx.rawCandidates) {
        if (rc.quality == ChordQuality::HalfDiminished && rc.rootPc == gExpectedAltRoot) {
            results.push_back(buildResult(rc));
            halfDimAltIdx = results.size() - 1;
            break;
        }
    }
}
```

If none of the four sub-gates (G-E, G-B, G-C, G-D) swap the appended entry to
`results[0]`, the phantom remains. To fix this, record whether the HalfDim was
pulled from `rawCandidates` and remove it if no swap occurred:

```cpp
bool halfDimPulledFromRaw = false;
if (halfDimAltIdx >= results.size()) {
    for (const auto& rc : gateCtx.rawCandidates) {
        if (rc.quality == ChordQuality::HalfDiminished && rc.rootPc == gExpectedAltRoot) {
            results.push_back(buildResult(rc));
            halfDimAltIdx = results.size() - 1;
            halfDimPulledFromRaw = true;
            break;
        }
    }
}
```

After the `if (halfDimAltIdx != results.size())` block (after all four sub-gates
have had their chance to fire via `didGFlip`), add:

```cpp
if (halfDimPulledFromRaw && !didGFlip) {
    // No sub-gate fired — remove the phantom alternative.
    results.pop_back();
}
```

This must go at the end of the `if (halfDimAltIdx != results.size())` block,
after the `didGFlip` checks, before the closing `}`.

---

## Task 3 — Named constants for Gate I/K/L margin guards

Add named constants near the top of `applyPostScoringGates`, after the
`buildResult` lambda and before the winner captures:

```cpp
// Gate margin guards (corpus-tuned).  All reachable corpus targets have
// margins well within these bounds.
static constexpr double kGateIMargin = 0.45;   // Gate I: first-inversion Min→Maj
static constexpr double kGateKMargin = 0.20;   // Gate K: first-inversion Aug
static constexpr double kGateLMargin = 0.35;   // Gate L: same-root Aug→Maj
```

Replace:
- `> 0.45f` in Gate I with `> kGateIMargin`
- `> 0.20f` in Gate K with `> kGateKMargin`
- `> 0.35f` in Gate L with `> kGateLMargin`

---

## Task 4 — Build and verify

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Then run all three suites:

```
cd C:\s\MS\ninja_build_rel

./composing_tests.exe > /tmp/comp_e3.txt 2>&1; echo "exit:$?"
head -20 /tmp/comp_e3.txt
tail -5 /tmp/comp_e3.txt

./notation_tests.exe > /tmp/nota_e3.txt 2>&1; echo "exit:$?"
head -20 /tmp/nota_e3.txt

./pipeline_snapshot_tests.exe > /tmp/snap_e3.txt 2>&1; echo "exit:$?"
head -20 /tmp/snap_e3.txt
```

Expected: 407/407, 52/52, 11/11. Task 1 (gate decoupling) and Task 3 (float
literals) must be byte-identical. Task 2 (G-E phantom) may change `results[]`
but must not change `results[0]`, so snapshot goldens should be unchanged.

If `pipeline_snapshot_tests` fails, do NOT update goldens — stop and report.

Run BIR for both presets:
```
cd C:\s\MS
python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
python tools/analyze_inversion_errors.py
python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
python tools/analyze_inversion_errors.py
```

Hard stops: Baroque BIR=false ≤ 25, Jazz BIR=false ≤ 13.
If either hard stop is hit, **do not commit** — report the regression.

---

## Task 5 — Update docs/scoring_model.md

The scoring model doc §6 (or wherever `applyPostScoringGates` is described)
should be updated to note:

- The pre-sort winner captures now occur at the top of the function, before the
  outer guard, so structural gates can access them.
- Gates H, I, J, K, L now run independently of the inversion-correction guard.
- The G-E phantom fix: the appended HalfDim is removed if no sub-gate fires.

Keep the update concise (2–4 sentences; no need to re-document each gate).

---

## Task 6 — Commit

If all acceptance criteria are met:

```
git add src/composing/analysis/chord/chordanalyzer.cpp docs/scoring_model.md
git commit -m "fix: decouple structural gates H–L from inversion-correction guard; fix G-E phantom (E3)"
```

---

## Acceptance criteria

| Check | Required |
|---|---|
| composing_tests | 407/407 |
| notation_tests | 52/52 |
| pipeline_snapshot_tests | 11/11 (no goldens updated) |
| Baroque BIR=false | ≤ 25 |
| Jazz BIR=false | ≤ 13 |
| Gates H/I/J/K/L inside outer guard | Removed |
| G-E phantom HalfDim removed when no sub-gate fires | Yes |
| `0.45f`/`0.20f`/`0.35f` replaced with named constants | Yes |

---

## Output

Report:
1. Build outcome.
2. All three test suite results.
3. BIR for both presets (did G-E phantom fix change anything?).
4. Confirmation of the three structural changes (decoupling, phantom fix, literals).
5. New HEAD commit hash.
