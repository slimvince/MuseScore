# Investigation: Corelli greedy-expand boundary failure root cause

**No code changes in this session. Diagnosis only.**

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\build_and_test.md`, `C:\s\MS\STATUS.md` first.
Working baseline: Iter 71 head (415b3ba563). Do not modify any source files.

---

## Background

Six notation tests still fail when the bridge is switched to greedy-expand.
The primary failures are five Corelli op01n08d tests. Before designing the next
fix, we need to understand the actual failure mechanism at the score level —
not just at the threshold level.

Two hypotheses are open:
- **H1**: No note-change tick exists at the failing beat positions because
  `collectNoteChangeTicks()` only collects note-START events (new onsets),
  and the harmonic shift in Corelli op01n08d at those beats is caused by
  note ENDINGS (a sustained chord dissolves, leaving a different pitch set)
  rather than new onsets.
- **H2**: A note-change tick does exist at the failing positions (at least
  one voice has a new onset there), but the candidate region's score is
  below effectiveRound2MinScore, so it is not placed.

These require different fixes. This session resolves which hypothesis is correct.

---

## Question 1 — Does collectNoteChangeTicks collect note-end events?

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp`.
Find `collectNoteChangeTicks()`. Describe precisely:

- What event types does it collect? Only note-start ticks? Note-end ticks too?
  Any other segment types?
- If a note ends at tick T (with no new note starting at T in any voice), would
  tick T appear in the output?
- Quote the relevant lines.

---

## Question 2 — What actually happens at the failing ticks in Corelli op01n08d?

For the score `src/notation/tests/data/corelli_op01n08d.mscx` (or wherever
the test fixture lives — find it), examine the actual note content at the
five failing beat positions:

```
m1  beat 3  → tick  960
m6  beat 3  → tick 8160
m8  beat 1  → tick 10080
m10 beat 3  → tick 13920
m11 beat 3  → tick 15360
```

For each tick, report:
- Which staves have a new note onset AT this tick (note starts here)
- Which staves have notes that END at this tick (note started before, ends here)
- Which staves have notes that are sustained THROUGH this tick (started before,
  end after)
- What pitch classes are sounding in the window [tick, tick+480)?

You may read the .mscx XML directly (it is MusicXML-like), or add a temporary
diagnostic to batch_analyze that prints note events around those ticks for
this score. Do not modify harmonicsegmenter.cpp or notationcomposingbridgehelpers.cpp.

---

## Question 3 — Is each failing tick in collectNoteChangeTicks output?

Add a temporary fprintf diagnostic to `greedyExpandSegmentation()` that prints
the full collectNoteChangeTicks output (all collected ticks) when the score
path contains "corelli_op01n08d". Build batch_analyze only (not full rebuild).
Run on the Corelli fixture. Report whether ticks 960, 8160, 10080, 13920,
15360 appear in the output.

If a tick IS present: report its candidate's initialScore and whether it
reached Round 1 or Round 2 placement.
If a tick is NOT present: cross-reference with Question 2 to confirm whether
this is because (a) no note change of any kind occurs there, or (b) a note
change occurs but collectNoteChangeTicks doesn't capture it (note-end only).

---

## Question 4 — Which BIR=true case resolved with broad Fix A?

From the Iter 71 diagnostic run you already performed (broad Fix A, BIR=true
went 5→4), which specific BIR=true case resolved? Report: score, measure,
beat, what the winner was before and after.

This is already measured — just report it.

---

## Question 5 — Low-confidence Dvorak test

For `HarmonicAnnotationKeepsRomanAtLowConfidenceNoteContext`:
The test expects keyConfidence < 0.5 for a specific note in Dvorak op08n06.
Greedy-expand produces 0.7575 for that note.

Without changing any code: look at what region greedy-expand places the note
in (its startTick, endTick, confidence) vs what Jaccard produced (inferred
from the test expectation). Is the greedy-expand region musically reasonable —
i.e., does it span a section that genuinely should have high confidence, or is
it absorbing a passage that genuinely has harmonic ambiguity?

Read the score fixture if needed. Give a one-paragraph musical assessment:
should this test be re-anchored to greedy-expand's output, or is greedy-expand
wrong here?

---

## Report format

```
Q1 — collectNoteChangeTicks event types:
  Collects note-start events: [yes/no]
  Collects note-end events: [yes/no]
  Other events: [describe]
  Relevant lines: [quote]

Q2 — Corelli note content at failing ticks:
  tick 960  (m1 b3):  onsets=[staves], endings=[staves], sustained=[staves], pcs=[list]
  tick 8160 (m6 b3):  onsets=[staves], endings=[staves], sustained=[staves], pcs=[list]
  tick 10080 (m8 b1): onsets=[staves], endings=[staves], sustained=[staves], pcs=[list]
  tick 13920 (m10 b3): ...
  tick 15360 (m11 b3): ...

Q3 — Tick presence in collectNoteChangeTicks:
  tick 960:   [present / absent] — [if present: initialScore=N, placed=R1/R2/not placed]
                                   [if absent: reason per Q2]
  tick 8160:  ...
  tick 10080: ...
  tick 13920: ...
  tick 15360: ...

Q4 — BIR=true case resolved by broad Fix A:
  Score: bwvN, m=N, b=N
  Before: winner=[chord], agreed-root=[pc]
  After: winner=[chord], agreed-root=[pc]
  Resolved because: [brief description]

Q5 — Dvorak low-confidence test:
  Greedy-expand region for the note: startTick=N endTick=N confidence=N
  Jaccard-inferred region: [smaller / larger / different boundaries]
  Musical assessment: [re-anchor / greedy-expand is wrong — reason]
```
