# CC Report — Layer 3 / Increment A: index the L1 NoteModel queries (byte-identical)

**Scope:** the byte-identical L1 query-indexing prerequisite of the L3 key/mode build
(`cowork_layer3_keymode_impl_design.md` §0.1 / §1). Pure performance fix:
`NoteModel::overlapping` / `onsetIn` go from O(N)-per-call (→ O(N²) over slices) to
O(log N + result). **Output contract unchanged** — same notes, same order, every query.

Commit (local, unpushed): `perf(composing): Layer 3/A — index NoteModel overlapping/onsetIn (byte-identical, O(N²)→O(N log N))`
Files: `note_model.h`, `note_model.cpp`, `note_model_tests.cpp` only. All other WIP left unstaged.

---

## 1. The structure chosen, and why

A new self-contained component **`NoteQueryIndex`** (declared in `note_model.h`, defined in
`note_model.cpp`), owned by `NoteModel` and built once at the end of `NoteModel::build`
(O(N log N)). It stores **only ints** (onset keys + a release tree) — it does **not** alias the
`NoteEvent` storage, so it copies/moves with the model (the tests copy `NoteModel` by value).

- **`onsetIn(t0,t1)`** — trivial. `m_onsets` is the onset-sorted key array; the notes whose onset
  lies in `[t0,t1)` are the contiguous block `[lower_bound(t0), lower_bound(t1))`. Two binary
  searches, emit in place → build order preserved for free. O(log N + result).

- **`overlapping(t0,t1)`** — the hard one (a note with `onset < t0` can still overlap if
  `release > t0`, so an onset bound alone is insufficient). Backed by a **max-release segment tree**
  over the onset-sorted array (a perfect binary tree; real leaves carry `release`, padded leaves
  carry `INT_MIN`, internal nodes carry the subtree max). The query is:
  *report every leaf in the onset prefix `[0, qHi)` whose `release > t0`*, where
  `qHi = onsetLowerBound(t1)`. The descent prunes two ways:
    - `nodeLo >= qHi` → the node's whole range is beyond the onset prefix; skip.
    - `maxRelease(node) <= t0` → no leaf in the subtree overlaps; skip the subtree whole.
  Recursing **left child before right** yields leaf indices in **ascending order**, i.e. exactly the
  build order the old head scan produced — no post-sort needed. Cost O(log N + result·log N), i.e.
  ~O(log N + result), and over a full per-slice pass ~O(N log N) instead of O(N²).

**Why a segment tree over the alternatives** (interval tree / bucket index): it (a) is built directly
over the existing onset-sorted array with no reordering, (b) yields hits already in build order
(left-first descent), and (c) needs only two flat `vector<int>` — trivially copyable, no pointer
aliasing, no horizon/cap (the deliberately-removed backward horizon is **not** reintroduced).

**A note on the audit's premise:** the audit/instruction expected the L2 `--validate-slices` path to
already call `overlapping` per slice. It does **not** — the current `changePointSlices`
(`slicer.cpp`) only reads `model.notes()` + boundary ticks. The O(N²) it warns about is the
*future* per-slice L3 emission path (Increment C). The fix is still the correct prerequisite; the
perf win is measured directly on the indexed query (below) rather than through the slicer.

## 2. Identical-results proof (the load-bearing gate)

New tests in `note_model_tests.cpp`. The reference oracles `linearOverlapping` / `linearOnsetIn` are
**byte-copies of the pre-A linear implementations**; every assertion is `EXPECT_EQ` on the full
`std::vector<const NoteEvent*>` → **element-for-element, including order**.

- **IDX1 — indexed == linear on all 14 `nm_*` fixtures** (ties, long sustains, grace, cross-staff,
  multi-voice unison, flags, eligibility, dense onsets, the four slicer fixtures, and the 204-note
  `nm_solid_theory`). Per fixture: the **exhaustive cross-product of all boundary ticks** (every
  exact onset/release, incl. `a>=b` empty cases), the targeted edges (`t1==t0`, `t1<t0`, full span,
  before-first onset, after-last release, first-tick-only), and **400 random ranges in both
  orders**. All pass.
- **IDX2 — `NoteQueryIndex` in isolation:** the `N==0` build path (which the `NoteModel`
  `m_notes.empty()` guards never reach), the `qHi<=0` and `m_segSize==0` guards, and the singleton
  (`segSize==1`, root-is-leaf) including the `release > t0` strict-inequality boundary.
- **IDX3 — synthetic 13-note tree** (non-power-of-two ⇒ padded leaves; mixed short/long sustains) vs
  a brute-force oracle over **5000 random ranges** — exercises internal-node recursion, the
  max-release subtree prune, and the prefix prune together.
- **IDX4 — empty model** (`build(nullptr)`): both queries short-circuit to `{}`.

## 3. Byte-identity (the suites) — no golden refresh

| Suite | Result | Note |
|---|---|---|
| `composing_tests` | **576 / 576** | was 572; +4 new tests (IDX1–IDX4). 1 disabled (perf). |
| `notation_tests` | **57 / 57** | unchanged |
| `pipeline_snapshot_tests` | **11 / 11** | **byte-identical, goldens NOT refreshed** |

`chord_mismatch_report.txt` unchanged. **BIR / oracle unchanged by construction:** `overlapping` /
`onsetIn` are pure deterministic functions of the note set; IDX1 proves the new implementation
returns identical results (incl. order) on representative fixtures and IDX3 proves it on 5000
adversarial random ranges, so the output is identical for *all* inputs — the snapshot byte-identity
(P1–P4, the four analysis paths) confirms the live pipeline output did not move. No corpus regen was
needed (this is not a gate addition/modification; the change cannot alter any chord/key output).

## 4. The perf win — measured

`DISABLED_IDX_PERF_ScalingIndexedVsLinear` (run with `--gtest_also_run_disabled_tests`) times a
per-slice `overlapping` workload (one query per `[onset_i, onset_{i+1})` slice) at growing N,
indexed (real production code) vs the pre-A linear scan. `linSum == idxSum` asserted equal at every N
(identical hit counts).

```
  N      linear(ms)   indexed(ms)   ratio
  1000         0.33         0.32      1.1
  4000         5.08         1.67      3.0
  16000       82.04         6.84     12.0
  64000     1335.85        27.47     48.6
```

- **linear** ×~16 per ×4 N (15.4 → 16.1 → 16.3) → **O(N²)**, as expected.
- **indexed** ×~4 per ×4 N (5.2 → 4.1 → 4.0) → **~O(N log N)**.
- separation grows monotonically (1.1× → 48.6×); at N=64k the indexed pass is **~49× faster** and the
  gap widens with N — the O(N²) → O(N log N) transition is realized.

## 5. Coverage

Full branch coverage of the new index code:
- `NoteQueryIndex::build` — `N==0` (IDX2) and `N>0` (all) paths.
- `overlapIndices` — `qHi<=0` / `m_segSize==0` guards (IDX2) and the normal descent (IDX1/IDX3).
- `collect` — both prune branches (`nodeLo>=qHi`, `maxRelease<=t0`) and the leaf-vs-internal split,
  all reached by IDX3's 5000 random ranges + IDX1.
- `NoteModel::overlapping` / `onsetIn` — `t1<=t0` (IDX1/IDX4), `m_notes.empty()` (IDX4), and the
  populated path (IDX1). The leaf body has **no runtime branch** by design: reaching a leaf already
  implies `nodeLo < qHi` (first guard) and `release > t0` (second guard), and padded leaves
  (`INT_MIN`) are always pruned — so the leaf unconditionally qualifies. This removes what would
  otherwise be a dead `nodeLo < N` guard.

## 6. Stop-condition check

None hit: no query returned a different result/order than the linear scan (IDX1/IDX3); no
suite/snapshot/BIR/oracle number moved (only added tests); `NoteEvent` / build semantics / the output
contract are untouched; the structure hits O(log N + result) with **no horizon/cap** reintroduced.

**Hand-off:** Cowork verifies identical-results + byte-identity at source; user ratifies; then push;
then Increment B (the held-out ground-truth harness).

## 7. Push to the fork (2026-06-22, user-ratified)

Pushed to **`origin` (`slimvince/MuseScore`) only** — `upstream` never targeted.

- **Ahead-set = exactly `4bce14e804`** (nothing else): `git log --oneline origin/master..HEAD` →
  `4bce14e804 perf(composing): Layer 3/A — index NoteModel overlapping/onsetIn …`. Pre-push
  HEAD = `4bce14e804…`, `origin/master` = `566d64d383`, parent of the commit = `566d64d383`.
- **`git show --stat 4bce14e804`** = only the 3 files:
  `note_model.cpp` (108), `note_model.h` (44), `note_model_tests.cpp` (292) — 425 ins / 19 del.
- **Staged set empty** before push (`git diff --cached --name-only` → nothing).
- **Push:** `git push --no-recurse-submodules origin master` →
  `566d64d383..4bce14e804  master -> master` (pre-push hook passed, no force/bypass).
- **`git ls-remote origin master`** = `4bce14e80444de3335a7182c3e6311a032700026` ✓.
- **`upstream`** still `disabled (push)` ✓ (unchanged, never targeted).
- **Held WIP stayed UNSTAGED through the push:** the B2 trio
  (`section/localmodulationdetector.{cpp,h}` + the `tools/batch_analyze.cpp` B2 hunks) and the WIP
  docs (ARCHITECTURE.md, STATUS.md, the `cowork_*`/`docs/*` set) — the push shipped the commit, not
  the working tree (`git diff --cached` empty; post-push ahead-set empty, working tree unchanged).
- STATUS.md updated (session 9f entry; LOCAL/uncommitted, consistent with prior entries).
