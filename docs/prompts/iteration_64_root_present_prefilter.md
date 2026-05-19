# Iteration 64: Root-present pre-filter in candidate scoring loop

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=5, BIR=false=125. Jazz BIR=false=12.
(Commit af785da463 — Iter 65 Part A.)

Build fresh before every BIR measurement. Verify binary is newer than source.

**This is a performance and correctness-preservation iteration.** No BIR change
is expected or desired. If BIR changes in any direction, that is a bug in the
filter — revert and report.

---

## Background

The candidate scoring loop in `chordanalyzer.cpp` (lines ~1705–1724) evaluates
12 roots × 16 templates = 192 candidates per region unconditionally. For a
typical Bach triad region with 3–4 distinct pitch classes, 8–9 roots have
pcWeight ≈ 0 — yet all 16 templates are scored for each. Adding a single
`continue` before the inner loop eliminates all template scoring for absent
roots. No winner can ever have a root that contributes zero weight to the
region, so this is provably output-neutral.

Primary benefit: real-time bridge path (per-keypress `harmonicAnnotation` call,
no parallelism to hide behind). Secondary benefit: modest corpus regen speedup
(corpus regen now 204s; the pre-filter may trim this further).

---

## Step 1 — Confirm baselines (no corpus regen needed)

```bash
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

The corpus is current from Iter 65. Record BIR=true and BIR=false.

---

## Step 2 — Implement the filter

Add the pre-filter and elimination counter together in one build. In
`chordanalyzer.cpp`, immediately before the inner `tplIdx` loop:

```cpp
// Perf: skip all templates for roots not present in this region.
// Any winning root must have pcWeight > 0; absent roots cannot win.
static constexpr double kRootPresentThreshold = 0.0;

// TEMP counters — remove before commit
static std::atomic<long> s_skipped{0}, s_total{0};

for (int rootPc = 0; rootPc < 12; ++rootPc) {
    s_total.fetch_add(1, std::memory_order_relaxed);
    if (pcWeight[rootPc] <= kRootPresentThreshold) {
        s_skipped.fetch_add(1, std::memory_order_relaxed);
        continue;
    }
    for (size_t tplIdx = 0; tplIdx < templates.size(); ++tplIdx) {
        // existing code unchanged
    }
}
```

Use `<=` not `==` to handle floating-point accumulation that may leave a
near-zero residual (e.g. 1e-15) for a genuinely absent PC.

Print the counter totals once after a corpus run — add a file-scope struct
with a destructor, or print from a known single-call site.

---

## Step 3 — Build, run corpus once, check BIR and elimination fraction

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

**Required**: BIR=true and BIR=false must be identical to baseline (5/125).
If any BIR change: stop, revert, report — the filter is wrong.

Record the elimination fraction from the counter: skipped/total.
Expected: ~50–65% at threshold=0.

---

## Step 4 — Test extensionThreshold without an extra corpus regen

If threshold=0 is confirmed safe, change `kRootPresentThreshold` to
`prefs.extensionThreshold` and rebuild. Run test suites first:

```bash
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

If tests pass (407/407, 53/53), then regenerate corpus to confirm BIR:

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

If BIR unchanged at extensionThreshold: use it — eliminates more work and
is semantically consistent (same threshold already governs extension tone
presence). If BIR changes: revert to threshold=0, note which cases changed.

Jazz run: only needed if BIR changes at extensionThreshold, to understand
what shifted. If threshold=0 is the final choice with BIR unchanged, skip it.

---

## Step 5 — Confirm pipeline snapshots unchanged

```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected: 12/12, no golden refresh. This is a performance change only.

---

## Step 6 — Commit

Remove TEMP counters. Promote `kRootPresentThreshold` to a named constant
with a one-line comment:

```bash
git add src/composing/analysis/chord/chordanalyzer.cpp
git commit -m "Perf: skip candidate scoring for absent root PCs

Add pcWeight pre-filter before inner template loop in analyzeChord.
Roots with pcWeight <= kRootPresentThreshold skip all 16 template
evaluations. Threshold = [0.0 / prefs.extensionThreshold].

No change to BIR=true or BIR=false — confirmed over full Baroque corpus.
Eliminates ~N% of the 12×16 per-region candidate evaluations.
Primary benefit: real-time bridge path latency."

git push

---

## Step 7 — Report to Cowork

```
Threshold = 0.0:
  BIR unchanged: [yes / no — describe]
  Candidates eliminated: N%  (N skipped / N total)

Threshold = extensionThreshold:
  BIR unchanged: [yes / no — describe which cases changed if any]
  Candidates eliminated: N%

Threshold chosen: [0.0 / extensionThreshold]

Tests:
  composing: N/407
  notation: N/53
  pipeline snapshots: N/12

Committed: [yes — hash] / [not committed — reason]
```
