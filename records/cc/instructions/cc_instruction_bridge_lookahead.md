# CC Instruction: Bridge forward-lookahead fix

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`,
and `C:\s\MS\docs\layer_architecture_audit.md` (Finding 3 and Finding 7).

**This is a correctness and infrastructure fix. It is not a BIR improvement
exercise.** Do not target BIR outcomes. The goal is to bring the bridge path into
parity with the batch path for forward-context signals. Snapshot drifts caused by
this change should be verified as DCML-correct or DCML-neutral — not evaluated by
whether they help BIR counts.

---

## Background

`findTemporalContext` in `regiontonecollector.cpp` (~L749–818) constructs a
`ChordTemporalContext` for a single chord in the live MuseScore annotation path
(the "bridge path" — cursor annotation, status bar, live chord track).

The function looks **backward** only:
- Calls `seg->prev1(SegmentType::ChordRest)` to find the predecessor
- Cold-analyzes the predecessor chord with `nullptr` context
- Sets `previousRootPc`, `previousQuality`, `previousBassPc`, `bassIsStepwiseFromPrevious`

It does **not** look forward. `nextRootPc`, `nextBassPc`, and `bassIsStepwiseToNext`
are left at their default values (-1 / false).

This is an implementation gap, not a design constraint. `seg->next1(SegmentType::ChordRest)`
is already used in the same file at lines 142, 409, and 692. The batch path (`regionanalyzer.cpp`)
provides full forward context for every chord. The bridge path's omission means the following
signals never fire on the live annotation path:

- `stepwiseBassLookaheadBonus` in `bassDependentContextualBonuses`
  (`chordanalyzer.cpp`) — uses `bassIsStepwiseToNext`
- Gate B (MajorAdd6 → Minor swap via `nextRootPc + bassIsStepwiseToNext`)
- Gate G-B (MinorAdd6 → HalfDim7 swap via `nextRootPc + bassIsStepwiseToNext`)
- Gate H-B (Augmented rotation via `nextRootPc + bassIsStepwiseToNext`)
- Gate E (first-inversion detection — uses `bassIsStepwiseToNext` as a condition)
- Gate F (second-inversion detection — uses `bassIsStepwiseToNext` as a condition)
- Iter 91 (bass-as-root promotion — uses `context->nextRootPc == bassPc`)

All of these fire correctly in the batch path but silently no-op on the bridge path.
The 6 bridge-path snapshot drifts from Gate R were a direct consequence of this: batch
had already stopped awarding the lookahead bonus to the wrong Δ=+7b candidates, but
bridge had never been awarding it at all.

**Reference:** `docs/layer_architecture_audit.md` Finding 3 for the full analysis.

---

## The fix

Add a forward-lookahead walk to `findTemporalContext` that mirrors the existing backward
walk. The pattern is already established in the backward direction — replicate it forward.

### What to add

After the backward walk (which sets `previousRootPc`, `previousBassPc`,
`bassIsStepwiseFromPrevious`), add a forward walk:

1. Call `seg->next1(SegmentType::ChordRest)` to get the successor segment
2. If null or if the successor is in a different measure and it's not useful (use
   your judgment), leave the forward fields at defaults
3. If a successor segment exists:
   - Collect its sounding tones (the same way the backward walk collects predecessor
     tones — look at how `prevSeg` is handled)
   - Cold-analyze it: call `RuleBasedChordAnalyzer{}.analyzeChord(nextTones, ...)` with
     `nullptr` context, the current key signature, and standard prefs (same approach as
     the predecessor cold analysis)
   - Apply `applyIter8691Pedal` and `applyPostScoringGates` to the result (the batch path
     does this; the cold analysis must replicate it for `nextRootPc` to be valid)
   - Set `ctx.nextRootPc = result.front().identity.rootPc`
   - Set `ctx.nextBassPc = result.front().identity.bassPc`
   - Compute `ctx.bassIsStepwiseToNext = isDiatonicStep(currentBassPc, ctx.nextBassPc)`
     using the same `isDiatonicStep` helper used for `bassIsStepwiseFromPrevious`

The "cold" limitation is the same as for the backward walk — the successor is analyzed
without its own temporal context. That is acceptable: `nextRootPc` is what the downstream
gates need, and a cold-analyzed `nextRootPc` is far better than -1.

### Where to look

The backward walk in `findTemporalContext` is the direct pattern to mirror. Read it
carefully before writing the forward walk. The tone-collection and cold-analysis approach
should be identical.

Also check how `applyIter8691Pedal` and `applyPostScoringGates` are called at the main
production call sites in `regionanalyzer.cpp` — the cold analysis of the successor should
go through the same gate pipeline so `nextRootPc` reflects the committed gate-corrected
identity, not the raw oracle winner.

---

## Constraints

- Change only `regiontonecollector.cpp` (and any helpers it calls that need exposing).
  Do not touch the scoring logic, gate thresholds, or any other file in `src/composing/`.
- Keep the cold-analysis approach consistent with the existing backward walk. Do not
  introduce a recursive call that could trigger infinite-depth analysis.
- The `!explorationMode` guard does not apply here — `findTemporalContext` is already
  outside the exploration loop.

---

## Testing

Run both test suites:

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/bridge_comp.txt 2>&1; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/bridge_nota.txt 2>&1; echo "exit:$?"
head -5 /tmp/bridge_comp.txt
head -5 /tmp/bridge_nota.txt
```

Run the pipeline snapshot tests separately:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/bridge_snap.txt 2>&1; echo "exit:$?"
head -30 /tmp/bridge_snap.txt
```

If snapshots drift, that is expected — the forward-lookahead gates and Iter 91 will now
fire on bridge-path chords that previously had `nextRootPc == -1`. For each drifting
snapshot:

1. Show the before/after chord identity for every changed tick
2. Look up the DCML ground truth for those ticks via `batch_analyze --preset Baroque` on
   the corresponding score (the batch path already has forward context and reflects the
   correct analysis)
3. Classify each change: **DCML improvement** (bridge now matches batch/DCML), **neutral**
   (alternatives-only or winner unchanged), or **regression** (bridge diverges from DCML)

If any snapshot drift is a regression (bridge moves AWAY from DCML), stop and report —
do not update the golden for it.

If all drifts are improvements or neutral, update the goldens:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens > /tmp/bridge_goldens.txt 2>&1; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/bridge_snap2.txt 2>&1; echo "exit:$?"
head -5 /tmp/bridge_snap2.txt
```

---

## BIR check (for information only — not a pass/fail criterion)

After both test suites pass, regenerate the Baroque corpus and check BIR. The result is
informational — this fix is not targeted at BIR and should not be rolled back or adjusted
based on BIR movement (unless a regression is genuine and identifiable as caused by this
change):

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py; echo "exit:$?"
```

**Note:** Use `characterise_bir_false.py`, not `analyze_inversion_errors.py` — the latter
reports a different metric. Expected baseline: BIR=false=13 (Baroque). Any change is
informational.

---

## Commit

After all tests pass and any snapshot drifts are classified and handled:

```
git add src/composing/analysis/engravingbridge/regiontonecollector.cpp
# add any other files touched (e.g. header if helpers were exposed)
git add src/notation/tests/pipeline_snapshot_tests/snapshots/  # if goldens updated
git commit -m "fix: bridge forward-lookahead in findTemporalContext — populate nextRootPc/nextBassPc/bassIsStepwiseToNext via seg->next1()"
```

---

## Report format

Write findings to `C:\s\MS\cc_bridge_lookahead_report.md`.

Include:
1. Summary of what was added to `findTemporalContext`
2. Test results: composing N/N, notation N/N, snapshot N/N
3. For each snapshot drift: tick, before/after chord identity, DCML ground truth,
   classification (improvement / neutral / regression)
4. BIR result (informational)
5. Commit hash
6. Any structural surprises (e.g. if the gating of `next1()` across measure boundaries
   required judgment calls, document the decision)
