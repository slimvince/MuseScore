# CC Instruction: Step 3 pre-investigation — key-as-distribution

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`,
`C:\s\MS\docs\redesign_plan.md` before starting.

**This is a read-and-diagnose pass only. No code changes. No commits.**

---

## Background

Step 3 of the redesign is "key-as-distribution" — using more than `.front()` of the
`resolveKeyAndModeRanked` output. Before writing the implementation instruction, three
things need to be confirmed:

1. Whether `fnCtx.keyFifths` / `fnCtx.keyMode` are ever read inside
   `harmonicfunctionlayer.cpp` (they appear unused — confirm or refute)
2. Where exactly `keyTonicPc` and `scale` are computed in `chordanalyzer.cpp`
   (these are the variables that feed all key-dependent scoring terms)
3. What `resolveKeyAndModeRanked` actually returns for the Corelli op01n08d failure
   case — specifically whether the correct key appears as a runner-up candidate

---

## Part A — Confirm fnCtx.keyFifths / fnCtx.keyMode usage

Search `harmonicfunctionlayer.cpp` for any read of `ctx.keyFifths` or `ctx.keyMode`.
Also check whether they are passed to any helper called from `applyHarmonicFunction`.

Report:
- Are they read at all in harmonicfunctionlayer.cpp?
- Are they passed to any function call (directly or indirectly) from within
  `applyHarmonicFunction`?
- If unused: note this is a dead field and should be documented

---

## Part B — Locate keyTonicPc and scale computation in chordanalyzer.cpp

In `analyzeChord`, find:
1. Where `keyTonicPc` is computed from `keySignatureFifths` / `keyMode`
2. Where `scale` (the 7-element diatonic array) is built
3. Show the exact lines and any intermediate variables

Then list every function in the oracle scoring loop that receives `keyTonicPc` or
`scale` as an argument. The known ones from Cowork's read pass are:
- `dim7CharacteristicBonus(tpl, rootPc, pcWeight, keyTonicPc, scale, ...)` — L2803
- `bassIndependentContextualBonuses(tpl, rootPc, keyTonicPc, scale, prefs, context)` — L2806

Confirm this is the complete list, or report any others.

---

## Part C — Corelli op01n08d key resolver diagnostic

Read `docs/score_inventory.md` to find the path for `corelli_op01n08a` or
`corelli_op01n08d` (check which is the failing one — it may be labelled as a
BIR=false case in `chord_mismatch_report.txt`).

Add a **temporary debug print** in `regionanalyzer.cpp` immediately after EACH call to
`kr::resolveKeyAndModeRanked` (both the initial one at ~L305 and the per-region one at
~L411). The print should output the top-3 candidates' key and confidence:

```cpp
// TEMPORARY DIAGNOSTIC — remove before reporting
for (size_t ri = 0; ri < std::min<size_t>(ranked.size(), 3); ++ri) {
    qDebug("[KEY-DIAG] tick=%d rank=%zu fifths=%d mode=%d tonicPc=%d "
           "score=%.4f normConf=%.4f",
           regionStart.ticks(),   // or startTick for the initial call
           ri,
           ranked[ri].keySignatureFifths,
           static_cast<int>(ranked[ri].mode),
           ranked[ri].tonicPc,
           ranked[ri].score,
           ranked[ri].normalizedConfidence);
}
```

For the initial call (L305), use `startTick.ticks()` instead of `regionStart.ticks()`.
For the per-region call (L411), use `regionStart.ticks()`.

Build, then run batch_analyze on the Corelli score:
```
cd C:\s\MS
ninja_build_rel/batch_analyze.exe <corelli_path> > /tmp/corelli_key.txt 2>&1; echo "exit:$?"
grep "\[KEY-DIAG\]" /tmp/corelli_key.txt | head -60
```

Report:
1. What does `initialRanked` return? Is rank=0 the wrong key (G minor)?
   What is rank=1 and its `normalizedConfidence`?
2. For the first few regions, what does the per-region ranked output look like?
   Is the correct key (C minor) ever appearing at rank=1 or rank=2?
3. Is G minor genuinely high-confidence (normalizedConfidence > 0.7)?
   Or is it only marginally ahead of C minor?

Remove the debug print before writing the report. Confirm working tree is clean.

---

## Report

Write findings to `C:\s\MS\cc_step3_key_investigation_report.md`.

Address:
1. Part A: fnCtx.keyFifths/keyMode — used or dead?
2. Part B: complete list of key-dependent functions in oracle, with line numbers
3. Part C: Corelli key resolver output
   - Is the wrong key confidently wrong (high normalizedConfidence, correct key not in top-3)?
   - Or is it ambiguously wrong (normalizedConfidence similar for wrong and correct)?
   - Does the correct key appear as a runner-up?
4. Implication for Step 3 implementation:
   - If wrong key is high-confidence: "key confidence scaling" (minimum viable form)
     will NOT fix Corelli — the double-run oracle (full form) would be needed
   - If correct key is a runner-up: minimum viable form (scale by key confidence, or
     run with ranked[1] as a fallback) may be sufficient
