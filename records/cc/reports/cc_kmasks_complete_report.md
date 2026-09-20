# CC Report — Phase 5 refactor (2 of 2, COMPLETION): single-source `templates[]` from `kTemplateIntervals`

**Commit (local, unpushed):** `e391f381e6`
`refactor(composing): single-source templates[] intervals from kTemplateIntervals`
**Files changed by the commit:** `src/composing/analysis/chord/chordanalyzer.cpp` **only** (1 file, +45 / −19).
**Parent:** `a0b983839a` (the kMasks-derive step). **Branch:** `master`. `upstream` not touched.

---

## 1. What changed and why

The prior step `a0b983839a` added the canonical `kTemplateIntervals` table in `chordanalyzer.h` and
derived Gate R's `kMasks` from it (`harmonicfunctionlayer.cpp` → `= makeTemplateMasks()`). But `templates[]`
in `chordanalyzer.cpp` still held its **own** inline interval literals, so the duplication had only **moved**
(`kTemplateIntervals` ↔ `templates[].intervals`) rather than being eliminated. This completion lifts the
first pass's no-`chordanalyzer.cpp` constraint and finishes audit Q1.3 to its real intent: **one** interval
source feeding both `templates[]` and `kMasks`.

After this commit `kTemplateIntervals` is the **sole** definition of per-template interval data. There is now
exactly one place in the codebase where the semitone sets (`{0,4,7}`, …) are written.

## 2. The conversion used

A small helper added in the anonymous namespace of `chordanalyzer.cpp`, right after the `TemplateDef` struct:

```cpp
std::vector<int> templateIntervalsVec(std::size_t t)
{
    std::vector<int> intervals;
    intervals.reserve(kMaxTemplateTones);
    for (int interval : kTemplateIntervals[t]) {
        if (interval >= 0) {
            intervals.push_back(interval);
        }
    }
    return intervals;
}
```

It builds the runtime `std::vector<int>` for template `t` from `kTemplateIntervals[t]` (a
`std::array<int, kMaxTemplateTones>`), dropping the trailing `-1` unused slots. Each `templates[]` row's
`intervals` literal was then replaced by `templateIntervalsVec(i)`, where `i` is the row's template index:

```cpp
static const std::array<TemplateDef, kTemplateCount> templates = {{
    { ChordQuality::Major,          templateIntervalsVec(0),  { 0, +4, +1 }       },
    { ChordQuality::Major,          templateIntervalsVec(1),  { 0, +4, +1, +5 }   },  // maj7
    ...
    { ChordQuality::Power,          templateIntervalsVec(16), { 0, +1 }           }
}};
```

- **`TemplateDef` is unchanged** — `intervals` is still `std::vector<int>`; no struct/representation change.
- **No scoring path touched** — `quality` and `tpcDeltas` stay inline (template-scoring data, not the shared
  interval set). The `templateIntervalsVec(i)` call yields the *exact same* vector the inline literal did.
- The index `i` in each row is a positional reference into the canonical table (row order is load-bearing:
  index == template index == tiePriority, per the `kTemplateIntervals` header comment), **not** interval data.
- §1 STOP condition (representation change touching `TemplateDef` or the scoring path) was **not** hit — the
  conversion is clean, `TemplateDef::intervals` takes the derived vector directly.

A clarifying comment was also corrected in the same file (comment-only): the "When adding a template" block
above `templates[]` previously instructed hand-adding the `kMasks` bitmask — stale since `a0b983839a` and
doubly so now. It now reads: bump `kTemplateCount`, add the interval row to `kTemplateIntervals`
(`chordanalyzer.h`), then add the matching `templates[]` row (quality + tpcDeltas; intervals via
`templateIntervalsVec(i)`).

## 3. Intervals-unchanged proof — the 17 lists are value-identical

`templateIntervalsVec(i)` returns `kTemplateIntervals[i]` with the trailing `-1` entries removed. Row-by-row,
this equals the original inline `intervals` literal exactly:

| i  | quality        | `kTemplateIntervals[i]` | → derived vec   | original inline | equal |
|----|----------------|-------------------------|-----------------|-----------------|-------|
| 0  | Major          | `{0,4,7,-1}`            | `{0,4,7}`       | `{0,4,7}`       | ✓ |
| 1  | Major (maj7)   | `{0,4,7,11}`            | `{0,4,7,11}`    | `{0,4,7,11}`    | ✓ |
| 2  | Major (dom7)   | `{0,4,7,10}`            | `{0,4,7,10}`    | `{0,4,7,10}`    | ✓ |
| 3  | Major (dom7b5) | `{0,4,6,10}`            | `{0,4,6,10}`    | `{0,4,6,10}`    | ✓ |
| 4  | Minor          | `{0,3,7,-1}`            | `{0,3,7}`       | `{0,3,7}`       | ✓ |
| 5  | Minor (min7)   | `{0,3,7,10}`            | `{0,3,7,10}`    | `{0,3,7,10}`    | ✓ |
| 6  | Diminished     | `{0,3,6,-1}`            | `{0,3,6}`       | `{0,3,6}`       | ✓ |
| 7  | Sus4b5         | `{0,5,6,10}`            | `{0,5,6,10}`    | `{0,5,6,10}`    | ✓ |
| 8  | HalfDiminished | `{0,3,6,10}`            | `{0,3,6,10}`    | `{0,3,6,10}`    | ✓ |
| 9  | Augmented      | `{0,4,8,-1}`            | `{0,4,8}`       | `{0,4,8}`       | ✓ |
| 10 | Aug dom7       | `{0,4,8,10}`            | `{0,4,8,10}`    | `{0,4,8,10}`    | ✓ |
| 11 | Sus2           | `{0,2,7,-1}`            | `{0,2,7}`       | `{0,2,7}`       | ✓ |
| 12 | Sus4+m7        | `{0,5,7,10}`            | `{0,5,7,10}`    | `{0,5,7,10}`    | ✓ |
| 13 | Sus4+Maj7      | `{0,5,7,11}`            | `{0,5,7,11}`    | `{0,5,7,11}`    | ✓ |
| 14 | Sus4#5         | `{0,5,8,10}`            | `{0,5,8,10}`    | `{0,5,8,10}`    | ✓ |
| 15 | Sus#4          | `{0,6,7,-1}`            | `{0,6,7}`       | `{0,6,7}`       | ✓ |
| 16 | Power          | `{0,7,-1,-1}`           | `{0,7}`         | `{0,7}`         | ✓ |

All 17 lists equal. The `tpcDeltas` lengths (3 for triads, 4 for sevenths, 2 for Power) still match each
derived `intervals` length, so the `intervals`/`tpcDeltas` parallel invariant is preserved.

## 4. Byte-identity proof (suites + snapshots)

Incremental build (single TU recompiled — `composing_analysis` unity object — then relinked; the only warnings
were the two pre-existing C4100 unreferenced-parameter warnings, unrelated to this change):

| Suite | Result |
|---|---|
| `composing_tests.exe` | **695/695 PASSED**, exit 0 (1 disabled) |
| `notation_tests.exe`  | **53/53 PASSED**, exit 0 (4 pre-existing skipped) |
| `pipeline_snapshot_tests.exe` | **11/11 PASSED**, exit 0 (1 skipped) — **NO `--update-goldens`** |

The snapshot suite passing without a golden refresh is the chord-output byte-identity proof: P1/P2/P3/P4 output
is pinned against golden JSON and is unchanged. `git status` after the test runs showed **zero** modified golden
files — the only tracked change in the working tree was `chordanalyzer.cpp` itself (now committed). The
`gater_tests.cpp` F1 set (kMasks coverage per template, derived from `kTemplateIntervals`) and the catalog
template-matching tests are within `composing_tests` and pass — exercising the template intervals end-to-end.

**Corpus BIR 53/24/53:** unchanged **by construction**. The template interval values are byte-identical
(§3), `kMasks` is derived from the same unchanged `kTemplateIntervals` and is snapshot-pinned, and no
scoring/weight/matrix/membership term moved. `batch_analyze` regen was **not** run: a full corpus regen
requires launching `batch_analyze` via Git Bash (per `feedback_batch_analyze_windows.md`), which conflicts
with the standing never-bash rule; per §2 this is the accepted "by-construction + the suites" path, with
`batch_analyze` regen noted as a Phase-5b prerequisite. There is no execution path by which a value-identical
interval list produces a different score.

## 5. Scope confirmation (for sha verification)

- `git show --stat e391f381e6` → **`src/composing/analysis/chord/chordanalyzer.cpp` only** (1 file).
- No weights, no `tpcDeltas` values, no `kMasks`, no score matrices, no scoring logic changed.
- `cowork_l1l3_stabilization_plan.md` shows as modified in the working tree but is a **pre-existing Cowork
  edit, not made by this session and NOT staged/committed** here.
- `upstream` untouched; commit is local and unpushed.

## 6. Result

`kTemplateIntervals` (`chordanalyzer.h`) is now the single interval source; `templates[]` and `kMasks` both
derive from it. The duplication audit-Q1.3 targeted is eliminated (not merely relocated). Byte-identical,
zero scoring change. Audit Q1.3 closed to intent.
