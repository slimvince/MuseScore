# Drop Right-Click Menu's `normalizedConfidence` Re-Sort

**Scope:** The right-click chord menu currently sorts a copy of
`chordResults` by `normalizedConfidence` before building submenus.
This sort logic is **leftover from the pre-Phase-3c-impl era**, when
`chordResults[0]` could be a prepended region-winner with a
lower score than the candidates following it. Phase 3c-impl
(commit `9f515d6372`) deleted that prepend. After Phase 3c-impl,
`chordResults` is sorted by `score` descending as returned by
`analyzeChord` — `chordResults[0]` is the highest-score candidate.
The right-click sort is now redundant.

This redundant sort produces a real divergence: at m285 of the
composing_tests catalog (and likely other ambiguous chords),
status bar shows `chordResults[0]` (analyzer's top-ranked
candidate) while right-click shows a different candidate that
happens to score higher under `normalizedConfidence`. The fix:
right-click trusts the analyzer's ranking, same as status bar
already does.

This is a small focused fix. Drop the sort, update the stale
header comment, verify behavior alignment. No analyzer changes,
no test infrastructure changes.

**Reference docs (read first):**
- `docs/three_paths_divergence_recon.md` — the recon that
  surfaced this finding
- `docs/divergence_d_recon.md` — context on the prepend pattern
  that the right-click sort was originally compensating for
- `docs/policy2_coalescing_map.md` — divergence map; this fix
  closes Divergence E (presentation-layer)

**Memory references** (auto-loaded):
- `project_divergence_d_recon` — Phase 3c-impl deleted the
  prepend; this is the cleanup that follows from that

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).
3. Force rebuild (`cmd.exe //c "C:\s\MS\setup_and_build.bat"`)
   and verify fresh binary timestamps. Build dir: `ninja_build_rel/`.
4. Cache pipeline_snapshot_tests baseline:
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_resort_baseline/`

---

## Work order

### Step A — Drop the re-sort in `appendAnalysisItemsForContext`

File: `src/notationscene/qml/MuseScore/NotationScene/notationcontextmenumodel.cpp`

Per `docs/three_paths_divergence_recon.md`, the sort is around
line 72 (verify exact location). The current code constructs a
"sorted copy" of `context.chordResults`. Remove the sort step;
iterate `context.chordResults` directly in analyzer-given order.

If `analysisAlternatives()` (or whatever variable holds the sorted
copy) is used elsewhere in the function, replace those references
with direct iteration over `context.chordResults`.

### Step B — Update the stale header comment

The same file has a header comment around lines 67-71 (per the
3c-recon report) explaining why the sort exists:

> The chordResults vector may have a region-winner prepended at
> position 0 (potentially lower-scoring than the fresh display
> analysis); sorting ensures the user always sees the best
> candidate at the top, regardless of that prepend ordering.

This comment is now wrong. The prepend pattern was retired in
Phase 3c-impl (commit `9f515d6372`). Replace with a comment
reflecting current behavior:

> chordResults is sorted by analyzeChord's internal score
> descending; chordResults[0] is the analyzer's top-ranked
> candidate. Trust the analyzer's ranking — do not re-sort by a
> derivative metric. (Phase 3c-impl deleted the legacy prepend
> pattern that this code's earlier sort was compensating for; see
> docs/divergence_d_recon.md.)

### Step C — Check `harmonicAnnotation` (status bar) for similar staleness

File: `src/notation/internal/notationcomposingbridge.cpp` (around
lines 533-540 per Phase 3c-recon).

Status bar's formatter has a similar pattern: it sorts entries
1..N while keeping position 0 fixed as region winner. Per the
recon, this is the dual of right-click's sort — it explicitly
tries to PRESERVE the prepend's position 0 instead of overriding
it. After Phase 3c-impl, there's no prepend; the "preserve
position 0" logic is also stale.

If the status bar sort is purely "keep [0] fixed and sort the
rest by `normalizedConfidence`," that's redundant cleanup
analogous to right-click's. Drop it, iterate in analyzer-given
order.

If the status bar sort does something else (e.g., applies a
display threshold, deduplicates), preserve that logic but make
sure it doesn't reorder candidates. When in doubt, halt and
surface.

### Step D — Verify behavior

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./pipeline_snapshot_tests.exe        # PASS, byte-identical to baseline
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_resort_baseline/
                                      # zero output
./composing_tests.exe                 # 407/407, RealDiff baseline 5
./notation_tests.exe                  # 53/53
```

`pipeline_snapshot_tests` should stay byte-identical — the right-click
menu and status bar aren't exercised by snapshot output. The 10-corpus
goldens shouldn't shift.

`composing_tests` and `notation_tests` should pass unchanged — the
fix doesn't touch test surfaces.

### Halt protocols

- **Pipeline snapshots drift:** the change leaked into a path it
  shouldn't have. Surface.
- **composing_tests or notation_tests regress:** unexpected; surface.
- **Status bar's sort logic does something non-trivial beyond
  reordering** (e.g., dedup, threshold, formatting): preserve
  that logic; only remove the reorder. Surface findings.

---

## Commit + push

Single commit. Suggested message:

```
Drop right-click menu's normalizedConfidence re-sort (close Divergence E)

The right-click chord menu's appendAnalysisItemsForContext was
sorting a copy of chordResults by normalizedConfidence before
building submenus. This was a workaround from the pre-Phase-3c-impl
era when chordResults[0] could be a prepended region-winner with a
lower score than its successors — the sort surfaced the
highest-scoring candidate despite the prepend ordering.

Phase 3c-impl (commit 9f515d6372) deleted the prepend. After 3c-impl,
chordResults is sorted by analyzeChord's score descending; [0] is the
top-ranked candidate. The right-click re-sort is therefore redundant.

In practice, the redundant sort caused right-click to occasionally
display a different candidate first than the status bar (which trusts
position [0]) — divergence at chords where score and
normalizedConfidence don't agree on ordering. m285 of the composing_tests
catalog was the surfaced example: status bar showed Csus(add9)
(highest score), right-click showed Cm7b5 first (higher
normalizedConfidence). Both UIs now trust the analyzer's ranking
uniformly.

Updates the stale header comment in notationcontextmenumodel.cpp
that referenced the retired prepend pattern. [If status bar's
analogous sort was also dropped, mention here.]

Closes Divergence E (presentation-layer divergence between status
bar and right-click chord menu).

pipeline_snapshot_tests: 10/10 byte-identical.
composing_tests: 407/407, RealDiff baseline 5 unchanged.
notation_tests: 53/53.
```

Update `docs/policy2_coalescing_map.md` to add Divergence E and
mark it CLOSED with citation of this commit (analogous to
divergence B and D documentation patterns).

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched (expect small: notationcontextmenumodel.cpp,
  possibly notationcomposingbridge.cpp, policy2_coalescing_map.md)
- LoC delta (expect tiny — line removals + comment update)
- Whether the status bar's analogous sort was also dropped (Step C
  finding)
- pipeline_snapshot_tests byte-identity confirmation
- composing_tests + notation_tests results
- policy2_coalescing_map.md updated to reflect Divergence E closure
- Any deviations and why

---

## Open question for follow-up (do NOT pursue in this session)

The `score` vs `normalizedConfidence` ordering disagreement
revealed at m285 (score puts `Csus(add9)` first, normalizedConfidence
puts `Cm7b5` first) is an analyzer-internal question separate from
this consumer-side fix. Worth investigating in a future session:
are these metrics intended to produce the same ordering? Is the
disagreement at ambiguous chords meaningful or a calculation issue?

This session does NOT investigate that. It accepts the analyzer's
ranking as authoritative for consumer purposes — whatever ordering
the analyzer produces, consumers respect it. The internal-metric
question is separate work.

---

## Scope guardrails

- **Do not** modify `analyzeChord` or any analyzer-internal scoring
  logic. The fix is consumer-side; the analyzer's output is
  trusted.
- **Do not** investigate `score` vs `normalizedConfidence`
  internals. That's a separate session.
- **Do not** modify `analyzeSection`, the pipeline structure, or
  any emitter (`emitImplodedChordTrack`, `emitHarmonicAnnotations`).
- **Do not** modify `chordResults`'s default ordering. The order
  comes from `analyzeChord`; consumers don't second-guess it.
- **Do not** introduce a new metric, flag, or option to control
  ordering preference. The analyzer's order is the answer.
- If Step C reveals the status bar's sort does non-trivial work
  beyond reordering: preserve that work, only drop the reorder
  step. Halt and surface if unclear.
- If pipeline_snapshot_tests drift: halt and surface — the fix
  shouldn't affect emitter output.
