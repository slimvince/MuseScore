# CC Report — Architectural Layer 2, Phase 2: clip the slicer to the loaded span + interim re-slice on extend

**Status:** Built, gated, committed **local-only (unpushed)**. Byte-identical on every existing caller.
**Design:** `cowork_layer2_reslice_design.md` (seam-aware corrected form, §2/§3/§6).
**Commits (local, unpushed):**
- `d1d079234b` — `docs(cowork): Phase-2 L2 re-slice design (seam-aware) + bounded-context §4 correction` (§0 preamble; the two Cowork docs only).
- `6d5a4dc144` — `feat(composing/L2): clip change-point slices to the loaded span (bounded context, Phase 2)` (slicer.cpp + slicer.h + slicer_tests.cpp + ARCHITECTURE.md).

---

## §0 — Protected the uncommitted Cowork doc corrections
Committed first, local-only, before touching code, so they could not be swept:
- `cowork_layer2_reslice_design.md` (was untracked — the new seam-aware design).
- `cowork_bounded_context_design.md` (was modified — the §4 correction: L2 re-slices over the enlarged span, edge slice extends, re-slice equivalence is the correctness guarantee).

`git show --stat d1d079234b` lists **exactly those two files** (8 insertions in the bounded-context doc, 110 in the new design). Confirmed.

---

## §1 — The clip, as built (`slicer.cpp`)
Added between the existing sorted-unique boundary build and the tiling loop, inside `changePointSlices`:

```cpp
const int clipStart = std::max(model.loadedStart(), boundaries.front());
const int clipEnd   = std::min(model.loadedEnd(),   boundaries.back());
boundaries.erase(
    std::remove_if(boundaries.begin(), boundaries.end(),
                   [clipStart, clipEnd](int b) { return b < clipStart || b > clipEnd; }),
    boundaries.end());
boundaries.push_back(clipStart);
boundaries.push_back(clipEnd);
std::sort(boundaries.begin(), boundaries.end());
boundaries.erase(std::unique(boundaries.begin(), boundaries.end()), boundaries.end());
// (degenerate single-tick loaded span can collapse to one boundary -> empty partition)
if (boundaries.size() < 2) { return slices; }
```

This is exactly the §2 rule: clip the **multiset**, not just the ends — **drop** every boundary outside
`[clipStart, clipEnd]`, **inject** the two clip endpoints, re-establish sorted-unique, then tile `[…)` as today.
The pre-existing `if (boundaries.size() < 2) return;` guard is kept *before* the clip (so `front()`/`back()` are
valid); a second `< 2` guard after the clip covers the degenerate single-tick loaded span (cannot occur on
whole-score). The only out-of-range boundaries that ever occur are sustained-in onsets `< clipStart` and
sustained-out releases `> clipEnd` (Layer-1 retention guarantees no eligible release `≤ loadedStart`, no onset
`≥ loadedEnd`), so `clipStart ≤ clipEnd` always holds.

### §1 collapse-on-whole-score confirmation (the inertness proof)
Every production/tooling caller of `changePointSlices` builds a **whole-score** model (verified at source):
- `regionanalyzer.cpp:512` `NoteModel::build(score)` → `:553` `changePointSlices(noteModel)` → `KeyModeSequenceDecoder`.
- `batch_analyze.cpp:1877` (`--validate-slices` diagnostic), `:2150` (key decode), `:2256` (chord decode) — all `NoteModel::build(score)`.
- `harmonicsegmenter.cpp` — comment reference only (the predecessor collector; not a call).

On a whole-score model, `loadedStart == scoreStart == firstMeasure->tick() ≤ firstEligibleOnset` (onsets are at or
after the first measure) and `loadedEnd == scoreEnd == score->endTick() ≥ lastEligibleRelease` (a note cannot sound
past the score end). Therefore `clipStart == boundaries.front()`, `clipEnd == boundaries.back()`, the `remove_if`
drops nothing, and the injected endpoints are already present → the clipped boundary vector is **identical** to the
unclipped one → `changePointSlices` output is **bit-for-bit identical** to before this change. This is a
mathematical identity, not an empirical hope; it is confirmed empirically below (CP1 + S1–S8c + the corpus).

### Spec sync (as-built)
- `slicer.h` — the function doc and the COVERING-PARTITION invariant now state the loaded-span clip and its
  whole-score inertness.
- `ARCHITECTURE.md` — the L2 "Covering / empty slices" paragraph gains the clip + re-slice-on-extend note; the
  coverage/test paragraph corrected (13→20 tests; the stale "not referenced by any production code" claim fixed —
  it IS consumed by L3 regionanalyzer/batch_analyze decode on whole-score, where the clip is inert).

---

## §3 — Tests (slicer_tests.cpp, +7: CP1–CP7), asserting the REAL invariants
All assert the corrected §3/§6 properties (no naïve "all old slices byte-identical").

| Test | Property | Result |
|---|---|---|
| **CP1** Clip_InertOnWholeScore | Degenerate byte-identity: `slices(build(score)) == slices(build(score, everything-span))` over all 14 fixtures; first slice starts at `firstEligibleOnset`, last ends at `lastEligibleRelease` (clip moved no endpoint inward). | PASS |
| **CP2** SustainedIn_FirstSliceStartsAtLoadedStart | `nm_long_sustain` C4[0,9600), select `[4800, e)`: first slice starts at `loadedStart=4800`, C4 in it, **no slice before 4800**. | PASS |
| **CP3** SustainedOut_LastSliceEndsAtLoadedEnd | select `[0,4800)`: last slice ends at `loadedEnd=4800`, C4 in it, **no slice after 4800**. | PASS |
| **CP4** PartialSpan_ClipsEdge_PreservesInterior | `nm_slice_passing`, select `[600,1440)` (D sustains in): slices `{[600,960),[960,1440)}`; interior real change-point 960 preserved; edge clipped to 600; eligible sets verified. | PASS |
| **CP5** Extend_ArtificialSeam_EdgeSliceGrows | Same, extend Earlier 600 → `[0,1440)`: edge slice **grows** (slice covering tick 600 moves from `[600,960)` to `[480,960)` — start `480 < 600`, NOT byte-identical); interior 960 stable; content over the original span `[600,1440)` unchanged. | PASS |
| **CP6** Extend_RealSeam_AdditivePrepend | `nm_dense_start`, select `[960,1920)` then extend Earlier 480: the clip seam at 960 is a **real** change-point, so old slices survive byte-identically and a new `[480,960)` is prepended (the additive case — explicitly distinguished from CP5's growth). | PASS |
| **CP7** ReSliceEquivalence_ExtendEqualsDirectBuild | Over all 14 fixtures: build interior `[a0,a1)`, extend both directions to `[x0,x1)`, assert `slices(sel) == slices(build(score, x0, x1))` (the correctness-critical invariant, §6.3). | PASS |

Full slicer suite: **20/20 PASS** (13 original S1–S8c byte-identical + 7 new). The 13 originals are the in-binary
degenerate byte-identity gate (they pin exact whole-score span lists); all unchanged.

---

## §4 — Gate (byte-identical on production)

| Gate | Before | After | Verdict |
|---|---|---|---|
| `composing_tests` | 631 | **631/631 PASS** (1 disabled = perf) | unchanged |
| `notation_tests` | 53 | **53/53 PASS** | unchanged |
| `pipeline_snapshot_tests` | 11 | **11/11 PASS** (no `--update-goldens`) | unchanged |
| Corpus `.ours.json` byte-diff — Baroque | — | **0 / 353** | byte-identical |
| Corpus `.ours.json` byte-diff — Jazz | — | **0 / 353** | byte-identical |
| Corpus `.ours.json` byte-diff — Default | — | **0 / 353** | byte-identical |
| BIR=false gate — Baroque | 53 | **53** | unchanged |
| BIR=false gate — Jazz | 24 | **24** | unchanged |
| BIR=false gate — Default | 53 | **53** | unchanged |

**Corpus method:** regenerated all three presets with the new binary into scratch dirs
(`tools/corpus/{baroque,jazz,default}_p2`, `run_bach_preset.py`), then `cmp -s` each of the 353 `.ours.json`
against the pre-change baseline (`tools/corpus/{preset}`, regen 2026-06-25 08:50 — only docs/notation-test commits
landed since, so it is a valid pre-change reference). **0 byte-diffs across all 1059 files.** `.ours.json` carries
no timestamp/commit field, so the byte-diff is a pure analyzer-output comparison. `characterise_bir_false.py` on the
new-binary dirs reproduced the ratified **53 / 24 / 53** exactly. Scratch `_p2` dirs removed afterward; the working
tree holds only the four intended files (now committed).

No corpus movement, no suite movement → the clip is inert on every existing caller, as proven in §1.

---

## §5 — Scope & unification ledger

**Reused (no new code path):**
- `changePointSlices` — the **one** slicer; the clip was added *inside* it. No second slicer, no second tiling loop.
- `std::sort` / `std::unique` — the existing sorted-unique step is reused verbatim after the clip's inject.
- `NoteModel::loadedStart()/loadedEnd()` — the Phase-1a accessors; the slicer now reads the loaded span from the
  model instead of deriving it from the notes alone (§2).
- `NoteModel::extend()` — the Phase-1a capability; **re-slice on extend is just re-calling `changePointSlices`** on
  the now-larger model (purity ⇒ identical to a fresh slice over the enlarged span). No re-slice code was added.
- Test scaffolding (`spans`, `eligiblePitches`, `eligibleCount`, `expectCoveringPartition`) reused; only small
  local helpers added (`eligibleSpan`, `sliceCovering`, `isBoundary`, the fixture array).

**New (this Phase):** the clip block in `changePointSlices` (≈12 lines) + CP1–CP7 tests + doc sync. **Not** built:
the Phase-2b incremental/seam-recompute re-slice (explicitly deferred); no L2→layer wiring; no partial selection
threaded into the live path; no second slicer.

**No new parallel path or logic duplication was introduced.**

---

## §7 — Stop conditions: none tripped
- Corpus / suites moved → **no** (0/353 all presets; 631/53/11 unchanged).
- Built an incremental/seam-recompute re-slice → **no** (interim re-call only; Phase 2b untouched).
- `extend` called by a layer / partial selection on the live path → **no** (Phase 3 untouched).
- Second slicer / tiling path → **no**.
- Push to `upstream` → **no** (both commits local, unpushed; nothing pushed anywhere).
