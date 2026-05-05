# Fix 5 `formatSymbol()` Per-Quality Flag-Handling Gaps

**Scope:** Fix the 5 bugs identified by the formatSymbol audit
recon (`docs/format_symbol_audit.md`). All are the same class as
the three previously-closed bugs (commits `59f65d569f`,
`da68035054`, `e529b736a1`) — per-quality branches in
`formatSymbol()` failing to consume detection flags
`detectExtensions()` correctly produced.

**The 5 bugs:**

| ID | Quality | Symptom | Severity |
|---|---|---|---|
| F1 | HalfDiminished | `hasEleventh` dropped — `Cm11b5` not emitted; catalog-confirmed at m296 | Medium |
| F2 | Minor | `hasThirteenth` dropped when `hasMaj7` — `CmMaj13` → `mMaj7` | Medium |
| F3 | Minor | `hasEleventh` dropped when `hasMaj7` — `CmMaj7add11` → `mMaj7` | Medium |
| F4 | Augmented | `hasMaj7` arm uses `hasNinth` instead of `hasNinthNatural` — `CMaj7#5b9` → `Maj9#5` | Low |
| F5 | Suspended4 | Same precision defect as F4 — `CMaj7susb9` → `Maj9sus` | Low |

Each fix is mechanical: locate the relevant per-quality branch in
`formatSymbol()`, identify the missing flag handling, add the
emit code following the precedent pattern. Probably 3-5 lines per
fix.

**Reference docs (read first):**
- `docs/format_symbol_audit.md` — the audit report; per-bug Q4
  analysis details the exact failure mode for each F1-F5
- `src/composing/analysis/chord/chordanalyzer.cpp` — the file to
  modify; `formatSymbol()` is the function being fixed
- `src/composing/tests/chord_mismatch_report.txt` — current
  baseline; m296 entry is F1's catalog-confirmed case

**Memory references** (auto-loaded):
- `project_format_symbol_per_quality_bugs` — the pattern this
  fix continues; three precedent commits documented
- `project_no_stripping_in_production` — analyzer outputs
  maximal/exact; this fix produces correct maximal output
- `project_chord_symbol_ban` — analyzer reads notes only;
  unchanged by this fix

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
   `cp -r src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_5bugs_baseline/`

---

## Work order

### Step A — Read the audit per-bug analysis

For each of F1-F5, read the corresponding entry in
`docs/format_symbol_audit.md`'s Q4 section. Confirm:
- The exact per-quality branch (file:line)
- The exact flag(s) being dropped
- The expected output the fix should produce

If any of the audit's analysis is unclear or seems incorrect when
read against the current code (e.g., the cited line range doesn't
match what's there), halt and surface — don't fix something the
audit might have characterized wrong.

### Step B — Implement F1 (HalfDiminished `hasEleventh`)

Locate the HalfDiminished case in `formatSymbol()`. Add
`hasEleventh` flag handling following the precedent pattern from
the previous HalfDiminished fix (commit `e529b736a1` added
ninth handling; this adds eleventh handling).

### Step C — Implement F2 + F3 (Minor `hasMaj7` + extension)

Locate the Minor branch around line 227 (per audit). The
`hasMaj7 && hasExtended` arm currently emits `mMaj7` and discards
the actual extension flags. Generalize to honor `hasEleventh`,
`hasThirteenth`, and any related alterations on those flags.

F2 and F3 are likely closed by the same generalization — they're
both about the same arm dropping extension flags. If the fix
naturally addresses both, single change closes both bugs.

### Step D — Implement F4 (Augmented `hasMaj7` ninth precision)

Locate the Augmented case's `hasMaj7` arm. Replace `hasNinth`
(which means "any ninth") with `hasNinthNatural` so that the b9/#9
flags can take their separate code paths. The precision defect
mirrors the bug closed by `da68035054` in the Major7/Minor7 case.

### Step E — Implement F5 (Suspended4 `hasMaj7` ninth precision)

Locate the Suspended4 case's `hasMaj7` arm. Same defect as F4;
same fix shape. Replace `hasNinth` with `hasNinthNatural` and add
the b9/#9 branches.

### Step F — Build and run tests

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel
./composing_tests.exe
```

Expected: composing_tests passes. RealDiff baseline drops from 4
toward 3 or fewer. F1 is the only catalog-confirmed case, so the
expected drop is 1 (m296 resolves). F2-F5 may or may not surface
additional catalog entries depending on whether the synthetic
catalog has CmMaj13 / CmMaj7add11 / CMaj7#5b9 / CMaj7susb9 cases.

```
./pipeline_snapshot_tests.exe        # Without --update-goldens first
diff -q src/notation/tests/pipeline_snapshot_tests/snapshots /tmp/snapshots_5bugs_baseline/
                                      # See output
./notation_tests.exe                  # 53/53 expected
```

### Step G — Halt protocol on snapshot drift

The 10-corpus pipeline_snapshot suite has Mozart, Chopin, Bach,
Schumann, Corelli — chords matching F2/F3 (Minor+Maj7+11/13) are
plausible in jazz/Romantic textures. F4/F5 (Augmented or
Suspended4 with Maj7+altered-ninth) are rare; probably no corpus
shifts.

**If snapshots drift after the fix:**

1. Run snapshots without `--update-goldens` first to see the diff
   scope — confirm it's annotation-only (or also `implodedChordTrack`
   if implode is affected).
2. Per affected score, sample 3-5 changed entries:
   - Pre-fix output (from cached baseline)
   - Post-fix output (from current snapshots)
   - Whether the post-fix output looks correct (matches the chord
     types in the music; consistent with editorial Romans if any
     are visible in the score)
3. Halt and surface a structured diff summary BEFORE committing.
   Do NOT auto-regenerate goldens.

**If pipeline_snapshot_tests stays byte-identical:**

Proceed to commit (no halt needed). The fix didn't affect any
corpus chord types.

**If composing_tests baseline drops by more than 1:**

That's good but worth verifying. Sample the additional entries
that resolved (besides m296) to confirm they're real fixes, not
side-effect over-corrections.

### Step H — Final test pass

After approval (if Step G surfaced a halt) or directly (if no
halt):

```
./pipeline_snapshot_tests.exe --update-goldens   # Only if Step G approved updates
./pipeline_snapshot_tests.exe                     # PASS
./composing_tests.exe                              # PASS, baseline at expected new value
./notation_tests.exe                              # 53/53
```

---

## Commit + push

Single commit. Suggested message skeleton:

```
Fix 5 formatSymbol per-quality flag-handling gaps (audit-driven cleanup)

The formatSymbol audit (docs/format_symbol_audit.md, commit
[audit-commit-hash]) identified 5 per-quality branches in
formatSymbol() that fail to consume detection flags
detectExtensions() correctly produces — same class as the three
bugs closed in commits 59f65d569f, da68035054, e529b736a1.

Fixes (per audit IDs F1-F5):

- F1 HalfDiminished hasEleventh: Cm11b5 now emits correctly;
  resolves m296 in composing_tests catalog (was previously
  classified as ambiguous; audit reclassified as real bug)
- F2 Minor hasMaj7+hasThirteenth: CmMaj13 no longer collapses
  to mMaj7
- F3 Minor hasMaj7+hasEleventh: CmMaj7add11 no longer collapses
  to mMaj7. F2 and F3 closed by single generalization of the
  hasMaj7 && hasExtended arm at line 227.
- F4 Augmented hasNinth → hasNinthNatural precision: CMaj7#5b9
  no longer formats as Maj9#5
- F5 Suspended4 hasNinth → hasNinthNatural precision: same fix
  as F4 in the suspended-4 branch

Per-fix LoC: roughly 3-5 lines each, following the precedent
pattern.

composing_tests RealDiff baseline drops from 4 to [N]: m296
resolves (F1); [report any additional catalog-confirmed cases].
[If snapshots shifted: per-score K.279-style validation summary
inline.]

[If snapshots byte-identical:]
pipeline_snapshot_tests: 10/10 byte-identical to pre-fix
baseline.

[If snapshots shifted:]
pipeline_snapshot_tests: [N affected scores]; diffs validated
against editorial Romans / chord content; goldens regenerated.

notation_tests: 53/53.

The audit's remaining-bug count is now zero — formatSymbol's
per-quality branches are consistent across all qualities and
flags. The previously-discussed structural concern about the
per-quality-branch abstraction being brittle remains; refactor
deferred unless a sixth bug of this class surfaces.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Files touched + LoC delta (expect 4-5 small per-branch changes;
  net additive since the fixes add code paths)
- Per-fix verification: each F1-F5 closed cleanly, with quick
  sanity check on the input that previously produced wrong output
- composing_tests baseline drop (expected 1 minimum from F1; report
  exact final value)
- pipeline_snapshot_tests outcome:
  - Byte-identical to baseline → confirm and proceed
  - Drift detected → Step G structured summary
- notation_tests result (expect 53/53)
- Step G summary if snapshot drift occurred (which scores, what
  changed, validation read)
- User approval received before committing if snapshots were
  regenerated
- Any deviations and why

---

## Scope guardrails

- **Do not** modify `detectExtensions()` or any detection logic.
  All 5 bugs are in `formatSymbol()`; detection is producing the
  flags correctly.
- **Do not** modify `qualitySuffix()` or other formatter helpers
  beyond what's necessary to add the missing flag handling. Most
  fixes are likely confined to the per-quality branches.
- **Do not** refactor `formatSymbol()`'s per-quality structure.
  The per-quality-branch abstraction is brittle (per
  `project_format_symbol_per_quality_bugs`), but the refactor is
  a separate design conversation — not part of this fix-bundle.
- **Do not** modify the catalog (`chordanalyzer_catalog.musicxml`).
  Standing do-not-touch.
- **Do not** auto-accept pipeline_snapshot_tests drift. Step G
  halt protocol applies. Surface a structured diff summary and
  wait for user approval if snapshots shift.
- **Do not** introduce stripping into production. The fixes
  produce correct maximal output; no reduction.
- **Do not** modify analyzer pipeline (analyzeSection, passes,
  KeyArea derivation). The fixes are downstream of analysis, in
  symbol formatting only.
- If any individual fix turns out to require touching shared
  helpers (qualitySuffix, etc.) in a way that affects multiple
  qualities simultaneously: surface, don't proceed unilaterally.
- If composing_tests RealDiff baseline drops below 3 in
  unexpected ways: investigate which entries resolved and
  confirm they're real fixes before pinning the new baseline.
- If F2 and F3 don't close together (one is partial), surface —
  the audit suggested a single generalization handles both, so
  partial closure is a sign the fix shape needs adjustment.
