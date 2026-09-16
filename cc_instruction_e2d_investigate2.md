# CC Instruction — E2d Investigation 2 (read-only)

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**Current HEAD:** `de418dea5f` (E2d-infra). Working tree must be clean
(E2d-enable changes reverted). Confirm with `git status`.

**This is a READ-ONLY investigation. Make zero code changes. Report findings only.**

---

## Context

E2d-enable was attempted and reverted. Four snapshot tests show winner
identity changes (root + quality), not just alternative reordering:

- `bach_bwv806_prelude` — multiple regions: sus2→major, major→minor, etc.
- `bach_bwv806_gigue` — Esus→E
- `mozart_k280_1` — C7/E→F
- `bach_chorale_137` — Em7b5/Db→Dm (+ tick shift 24000→24960)

The hypothesis is that the scorer's post-scoring gates (A–L, Sub-9a) process
the suppressed-signal winner and transform its identity AFTER the snapshot is
captured, so the function layer's snapshot cell has a different identity than
the final gate-processed result.

This investigation must confirm or refute that hypothesis — and identify the
true root cause — before a fix is designed.

---

## Question 1 — Trace one failing case end-to-end

Focus on `bach_chorale_137`, the simplest case (one region: Em7b5/Db→Dm,
tick shift 24000→24960).

### Q1a — What is the golden output for this region?

Read the golden file for `bach_chorale_137` in
`src/notation/tests/pipeline_snapshot_tests/snapshots/`. Find the region
near tick 24000 (or 24960). Report:
- The tick value
- `candidates[0]`: rootPc, quality, bassPc, bassTpc, tiePriority, score
- `candidates[1]`, `candidates[2]` if present

### Q1b — What does the function layer pick?

In the working tree (E2d-enable reverted), the function layer is a no-op
(suppression still false). The golden was written before E2c. So the golden
represents the with-signal scorer output.

When E2d-enable was active (suppression true), the function layer picked Dm
instead of Em7b5/Db. Read `harmonicfunctionlayer.cpp` as it stands now
(no-op body after E2c). This tells you what the function layer DOES NOT yet do.

The question is: what is the snapshot cell that corresponds to the Dm result
the function layer was selecting?

In the snapshot, a Dm cell has:
- `rootPc = 2` (D)
- `bassPc = 2` (D, root position)
- `quality = Minor`

The golden Em7b5/Db has:
- `rootPc = 4` (E)
- `bassPc = 1` (Db/C#)
- `quality = HalfDiminished`

These are different rootPcs. How does the function layer select rootPc=2 (Dm)
when the snapshot's highest-scoring cell should be rootPc=4 (Em7b5)?

Read `chordanalyzer.cpp` around the `buildResult` lambda. Report:
- Does `buildResult` change `rootPc` or `quality` from the raw cell values?
  (i.e., does `result.identity.rootPc` ever differ from `rawCandidate.rootPc`?)
- Does `buildResult` change `bassPc` or `bassTpc`?
- Is there any transformation that could convert a raw `rootPc=4, quality=HalfDim,
  bassPc=1` cell into the final `Em7b5/Db` label?

### Q1c — Identify which gate fires

Read all gates and sub-gates in `analyzeChord()` between the initial
winner-selection and the final `candidates` population. For each gate/sub-gate,
report:
- Its line number and brief description
- Whether it is gated on `!prefs.suppressProgressionSignals` or runs unconditionally
- Whether it can change `candidates[0]`'s rootPc, quality, or bassPc

Specifically look for:
- Sub-9a (mentioned in the E2d-enable report)
- Any gate that could produce a `HalfDiminished` result from a `Minor` cell
- Any gate that could change `bassPc` from root-position to a non-root value

### Q1d — Tick shift: 24000 → 24960

The tick value also changed. This suggests a different REGION is being
selected as the winner, not just a different chord label within the same
region. Or the region boundary itself moved.

Read `regionanalyzer.cpp` around the tick-to-region assignment. Is the tick
stored in the `ChordAnalysisResult` derived from the region boundary, from
the beat position, or from another source? Could the function layer's
winner swap cause a tick change?

---

## Question 2 — Does `buildResult` change cell identity?

Read the `buildResult` lambda in `analyzeChord()` in full.

Report:
- Every field of `ChordAnalysisResult::identity` that `buildResult` sets
- Whether any of them can differ from the `RawCandidate`'s raw rootPc / quality /
  bassPc / bassTpc
- Specifically: is there any enharmonic spelling correction, inversion
  detection, or quality reclassification inside `buildResult`?

---

## Question 3 — What does the snapshot capture vs. what `buildResult` produces?

The D1 snapshot capture records `cell.rootPc`, `cell.quality`, `cell.bassPc`,
`cell.bassTpc`, `cell.tiePriority` directly from the raw scoring loop.
`buildResult` runs later and may transform these.

For the `Em7b5/Db` case:
- The raw scoring loop would have a cell with `rootPc=4, quality=HalfDim,
  bassPc=1` (or whatever the raw values are).
- The snapshot captures THOSE raw values.
- `buildResult` produces `Em7b5/Db` from them.

If `buildResult` does NOT transform rootPc/quality/bassPc, then the snapshot
cell and the final result identity should match. If it DOES transform them,
the function layer's `(tiePriority, rootPc)` lookup will find the snapshot
cell but the cell has different identity fields than `candidates[0]`.

Report: for the `Em7b5/Db` candidate, do the snapshot cell's identity fields
match `candidates[0].identity` exactly?

---

## Question 4 — What is the function layer actually selecting?

In the E2d-enable implementation (which you have reverted), the function layer
selected a winner using `(tiePriority, rootPc)` lookup in `candidates[]`.

For the `bach_chorale_137` failing region:
- What `tiePriority` and `rootPc` does the function layer's winner cell have
  in the snapshot?
- Is there a `candidates[]` entry with that exact `(tiePriority, rootPc)`?
- If yes: what is that candidate's full identity (rootPc, quality, bassPc)?
  Is it Dm (rootPc=2, Minor) or Em7b5/Db (rootPc=4, HalfDim, bassPc=1)?

This will reveal whether the function layer is:
(a) Correctly finding the Em7b5/Db candidate and something downstream changes it, OR
(b) Mistakenly selecting a Dm snapshot cell as the winner (wrong scoring), OR
(c) Finding Dm in candidates[] because the suppressed-signal scorer built a Dm
    candidates[0] and that is what the (tiePriority, rootPc) lookup finds

---

## Question 5 — Suppression-mode candidates[] content

Under suppression (`suppressProgressionSignals=true`, threshold disabled),
`analyzeChord()` populates `candidates[]` with all threshold-passing cells
from the suppressed-signal run. The suppressed-signal winner may be Dm
(different from the with-signal winner Em7b5/Db).

Report for the `bach_chorale_137` failing region:
- What is `candidates[0]` in suppression mode (before the function layer runs)?
  Is it Dm or Em7b5/Db?
- Is Em7b5/Db present anywhere in `candidates[]` in suppression mode?
- If Em7b5/Db is NOT in `candidates[]` in suppression mode, explain why —
  was it threshold-filtered, or does it not exist as a raw cell at all?

To answer this, read the suppression-mode threshold and cap logic in
`analyzeChord()` (the block gated on `!prefs.suppressProgressionSignals`
at ~L2683). Confirm: in suppression mode, does threshold completely disabled
mean ALL 204 cells (12 rootPcs × 17 templates) for the winning bass are in
`candidates[]`? Or is there still some filtering?

---

## Question 6 — The tick shift (24000 → 24960)

The tick change in `bach_chorale_137` suggests the region map itself may
differ between suppression-on and suppression-off paths.

Read `regionanalyzer.cpp` Pass 2 and Pass 2b logic. Is there any branching
based on `chosenResult` quality or identity that could cause a different
region to be processed or a different tick to be assigned? Could a winner
change in region N cause region N+1 to shift its tick?

---

## Summary question

Based on Questions 1–6, answer:

**What is the true root cause of the winner identity changes?**

Choose the most accurate description:

(A) `buildResult` transforms raw cell identity (rootPc/quality/bassPc) in
ways the snapshot does not capture, so the function layer's snapshot-cell
lookup finds the wrong entry in `candidates[]`.

(B) The suppressed-signal scorer picks a genuinely different winner (Dm
instead of Em7b5/Db) and that Dm winner is what ends up in `candidates[0]`
after gates run. The function layer's rescore also picks Dm because its
signal computation is wrong or incomplete.

(C) The post-scoring gates (A–L, Sub-9a) promote a result DIFFERENT from
the raw suppressed-signal winner into `candidates[0]`, and the function layer
overrides that gate-promoted result back to the raw suppressed-signal winner.

(D) Some other cause — describe precisely.

For each failing test (or at minimum `bach_chorale_137`), identify which of
A/B/C/D applies.

---

## Report format

Answer each question with exact line numbers where relevant. The fix for
E2d-enable will be designed from this report — be specific about what the
code actually does, not what you expect it to do.

**Make zero code changes.**
