# Iteration 16: Snapshot originalWinnerQuality; document `winner` live-reference semantic

## ⚠ Critical behaviour rules

- Minimal targeted change — functionally equivalent in all known cases, but
  architecturally correct.
- Build + all tests + corpus BIR numbers must match Iteration 15 baselines exactly.
- If anything deviates: STOP and report verbatim.

---

## Background

`const ChordAnalysisResult& winner = results[0]` (line 1949) is a **live reference**:
after any `std::swap(results[0], ...)` in Gates A–F, `winner` silently refers to
the swapped-in element, not the original winner. Gate G (the new standalone block,
lines ~2157–2215) runs after all A–F gates and reads `winner.identity.quality` to
check for MinorAdd6. Today this is safe because a swapped-in element (Minor7 or a
re-sorted alt) does not carry `AddedSixth`, so Gate G does not misfire. But the
safety is implicit — it relies on an unstated assumption about what qualities
can appear at results[0] after A–F gates fire.

The fix is two-part:
1. Capture `originalWinnerQuality` once, before any gates can mutate results[0].
2. Use `originalWinnerQuality` instead of `winner.identity.quality` in Gate G's
   outer condition, making the intent explicit.
3. Add a comment at the `winner` declaration explaining the live-reference semantic
   so future developers understand the design.

The `winner` reference is still correct for Gates A–F (they intentionally read
the current top element), and for the re-sort path (which also reads the current
top). Only Gate G needs the snapshot because it is intended to act on the
original winner, not a post-swap element.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=100, BIR=false=788

---

## Step 2 — Read and confirm current state

Read `src/composing/analysis/chord/chordanalyzer.cpp` around lines 1949–1960 and
2157–2160. Confirm and report:

A. The exact line of `const ChordAnalysisResult& winner = results[0];`.
B. Whether there is already any comment explaining the live-reference semantic.
C. The exact line of the Gate G outer condition that reads
   `winner.identity.quality == ChordQuality::Minor`.
D. Confirm no other gate outside the `if (bestAlt... / if (winnerBassIsRoot ...)`
   block reads `winner.identity.quality` (Gate H reads it at line ~2229 — confirm
   its context: it only fires when no prior A–F/G gate fired, so the live-reference
   does not affect it).

Report before proceeding.

---

## Step 3 — Add `originalWinnerQuality` snapshot

Immediately after the `winner` declaration (confirmed in Step 2A), add one line:

```cpp
        const ChordQuality originalWinnerQuality = winner.identity.quality;
```

And add a comment on the `winner` declaration line itself, changing it from:

```cpp
        const ChordAnalysisResult& winner = results[0];
```

To:

```cpp
        // Live reference — winner tracks results[0] through any swap.
        // Use originalWinnerQuality (captured below) when you need the
        // pre-swap quality in gates that run after A–F.
        const ChordAnalysisResult& winner = results[0];
        const ChordQuality originalWinnerQuality = winner.identity.quality;
```

Report the exact lines inserted.

---

## Step 4 — Update Gate G outer condition

In the Gate G block, change the outer `if` condition from:

```cpp
        if (prefs.preferMinorOverMajorAdd6
            && winner.identity.quality == ChordQuality::Minor
            && hasExtension(winner.identity.extensions, Extension::AddedSixth)) {
```

To:

```cpp
        if (prefs.preferMinorOverMajorAdd6
            && originalWinnerQuality == ChordQuality::Minor
            && hasExtension(winner.identity.extensions, Extension::AddedSixth)) {
```

Note: `hasExtension(winner.identity.extensions, ...)` reads extensions from
`results[0]` at the time Gate G runs. This is intentional — if A–F swapped
results[0], the extension check on the new results[0] prevents a spurious fire.
Only the quality check needs the snapshot because quality is the primary
discriminator between gate families.

Report the exact line changed.

---

## Step 5 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected (must match exactly):
- Build: pass
- Composing tests: 407/407, RealDiff ≤ 4
- Notation tests: 53/53
- Pipeline snapshot tests: 11/11, no mismatches
- BIR=true: 100
- BIR=false: 788

Any deviation: STOP and report verbatim.

---

## Step 6 — Push

```
cd C:\s\MS && git add -A && git commit -m "Iter 16: snapshot originalWinnerQuality; document winner live-reference semantic" && git push
```

---

## Step 7 — Report

```
State (A–D confirmed):
  winner declared at:              line N
  Live-reference comment present:  no (added in this iteration)
  Gate G quality check at:         line N
  Gate H context:                  confirmed — no A–F/G swap possible before H

Changes:
  Comment + originalWinnerQuality added: lines N–N
  Gate G condition updated:              line N

Build:                    pass / fail
Composing tests:          407/407, RealDiff=N
Notation tests:           53/53
Pipeline snapshot tests:  11/11, no mismatches
BIR=true:                 100
BIR=false:                788
GitHub push:              done / commit hash
Unexpected findings:      none / <describe>
```
