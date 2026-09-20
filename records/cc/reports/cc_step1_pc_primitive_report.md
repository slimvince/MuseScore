# CC Step 1 — Shared pc/collection primitive extraction (S3-primitive)

**Commit:** `8bc1441076` (local, UNPUSHED, ahead of origin/master by 5). Parent `a03c2493bb`. Linear history.
**Type:** PURE byte-identical refactor. No inference change, no scoring term touched, no `docs/scoring_model.md` sync required.

---

## 1. What was extracted (placement: extend `chord/analysisutils.h`)

Chose to **extend the existing `src/composing/analysis/chord/analysisutils.h`** rather than add a new
`analysis/pitchclassutils.h`. Rationale: that header already hosts the pc + key-signature primitives this work
belongs with — `normalizePc`, `ionianTonicPcFromFifths`, `endsWith` — so the three new functions are
consistent with what is there, no new file/CMake entry, and `normalizePc` (the Family-1 target) is already in
place. All four TUs now `#include "composing/analysis/chord/analysisutils.h"`. Added `#include <cstdint>` to
the header (needed for the `uint16_t` signatures it now exposes).

Three functions added to `analysisutils.h` (namespace `mu::composing::analysis`, `inline` — unity/jumbo-safe):

| Added | Replaces |
|---|---|
| `bool pcInMask(uint16_t mask, int pc)` | cadencekeyanchor `pcInMask`, tonicizationlabeler `pcInMask` |
| `uint16_t diatonicMaskFromFifths(int fifths)` | cadencekeyanchor + tonicizationlabeler `diatonicMaskFromFifths` (Family 2a) |
| `uint16_t collectionMask(int tonicPc, bool isMajor)` | `lmdCollectionMask` + `jkdCollectionMask` (Family 2b) |

Plus Family 1 routed to the **pre-existing** `normalizePc`.

---

## 2. Byte-identity proof, per function

### Family 1 — pc residue → `normalizePc`
All copies are `inline int …PcMod12(int x) { return ((x % 12) + 12) % 12; }`. The existing
`normalizePc(int pitch) { int pc = pitch % 12; return pc < 0 ? pc + 12 : pc; }` returns the **same value for
every integer input**, negatives included:
- `x ≥ 0`: `x%12 ∈ [0,11]`, both return it.
- `x < 0`: `x%12 ∈ [-11,0]` (C++ truncates toward zero). `pcMod12` = `((neg)+12)%12`; `normalizePc` adds 12
  when `<0`. Both land on the same `[0,11]` residue (e.g. `-1 → 11`, `-13 → 11`).

So `pcMod12 ≡ lmdPcMod12 ≡ jkdPcMod12 ≡ normalizePc` over all `int`. All call sites re-pointed to `normalizePc`;
the three prefixed copies deleted. (`noexcept` was dropped at the merge — irrelevant to output; none of these
throw.) **Decision: consolidate onto the existing `normalizePc`, no new alias.**

### Family 2a — `diatonicMaskFromFifths`
cadencekeyanchor and tonicizationlabeler bodies were character-identical (modulo the internal `pcMod12` name).
Shared body is identical with `pcMod12 → normalizePc`. Output byte-identical.

### Family 2b — `collectionMask(tonicPc, isMajor)` (bool convention = `isMajor`)
`jkdCollectionMask(tonicPc, isMajor)` and `lmdCollectionMask(tonicPc, minorMode)` had the **same tables**
(`kMajor = {0,2,4,5,7,9,11}`, `kMinorHarm = {0,2,3,5,7,8,10,11}`) and **same loop**, differing only in the
bool sense. Chose the **`isMajor`** convention (matches jkd, so jkd sites are a pure rename):
- jkd sites: `jkdCollectionMask(t, isMajor) → collectionMask(t, isMajor)` (no arg change).
- lmd sites: `lmdCollectionMask(t, minorMode) → collectionMask(t, !minorMode)` (**argument negated**).

Verified the negation: `lmd(minorMode=true)`→`kMinorHarm`; `collectionMask(isMajor=false)`→`kMinorHarm`.
`lmd(minorMode=false)`→`kMajor`; `collectionMask(isMajor=true)`→`kMajor`. So
`lmdCollectionMask(t, m) ≡ collectionMask(t, !m)`. Output byte-identical.

### Readers deliberately LEFT LOCAL (not unified — verified NOT byte-identical or unique)
Per the instruction's "extract only the ones you VERIFY identical; leave any that differ":
- **`jkdRootDiatonic` vs `lmdRootIsDiatonic` — NOT identical.** `jkdRootDiatonic` has `if (pc < 0) return false;`;
  `lmdRootIsDiatonic` has **no** such guard. Different bodies → both kept in place, each re-pointed at the shared
  `collectionMask` (and `normalizePc`). Not merged.
- `jkdInCollectionFraction`, `lmdOutOfCollectionCount`, `jkdChordPinned` — no cross-file counterpart (unique).
  Kept local, re-pointed at `collectionMask` / `normalizePc`.
- `keyScale` (tonicizationlabeler, named ns `tonicization_detail`) — unique ordered-degree builder. Untouched
  except its internal `pcMod12 → normalizePc`. `kUpper`/`kLower` numeral tables kept local.

These kept-local helpers **retain their `lmd*`/`jkd*` prefixes**: only the *extracted* helpers needed
de-prefixing. Keeping the local readers' prefixes introduces no new unity-build clash (all names distinct) and
minimizes churn.

---

## 3. ODR-prefix removal / unity build
The `lmd*`/`jkd*` (and the `tonicization_detail` named namespace) existed solely to dodge a unity/jumbo ODR
clash between sibling anonymous namespaces. The extracted helpers now live **once**, `inline`, in a header with
an include guard — the correct, ODR-safe form. The empty anonymous namespace in `cadencekeyanchor.cpp` was
removed entirely. **The unity/jumbo build compiles** (confirmed: full `setup_and_build.bat` linked
`MuseScore5.exe`; the unity TUs that concatenate these files built without error).

---

## 4. Gate results (refactor-only commit `8bc1441076`)
1. **Build:** clean, unity/jumbo compiled, linked.
2. **composing_tests:** 545/545. **notation_tests:** 57/57.
3. **pipeline_snapshot_tests:** 11/11, **ZERO-diff, no `--update-goldens`**.
4. **BIR + `.ours.json`:** regenerated all three presets with the refactored binary into scratch `_s3` dirs and
   diffed `.ours.json` against the HEAD reference corpora (manifest `git_hash 41f7c65f63`, the head of the
   verified byte-identical refactor chain to `a03c2493bb`):
   - Baroque: **0 `.ours.json` diffs**, `characterise_bir_false` = **57**.
   - Jazz: **0 diffs**, **23**.
   - Default: **0 diffs**, **57**.
   `.ours.json` 0-diff ⇒ the BIR **case-identity** set is identical (not just the integer). Scratch dirs removed.
5. No template/bonus/guard/gate touched → no scoring-model sync.

---

## 5. B2 guard preservation (per instruction §0.5 — PRESERVE, rebase on)
**Deviation surfaced:** §0.5 step 1 said the working tree should show ONLY `localmodulationdetector.cpp/.h`
modified. It actually carried a **THIRD** B2 file: `tools/batch_analyze.cpp` (+14 lines, the `--dump-modulation`
diagnostic emitting `anchorConfidence` + the three `LocalKeySpan` B2 fields). The first build failed
(`batch_analyze.cpp` referencing the stashed `LocalKeySpan` fields), which surfaced the coupling. Confirmed via
grep that `batch_analyze.cpp` is the **only** compiled file coupled to the B2 fields, and its entire diff is
B2-only. So B2 is a **three-file instrument set**, not two.

Handled it cleanly: stashed `batch_analyze.cpp` as a second labeled stash alongside the lmd `.cpp/.h`, did the
refactor + all gates on a clean tree, committed refactor-only (B2-free), then re-applied all three:
- `batch_analyze.cpp` + `localmodulationdetector.h` — popped **clean** (refactor never touched them).
- `localmodulationdetector.cpp` — conflicted (B2 calls the removed `lmdPcMod12`). **Resolved mechanically**:
  kept B2's `kSubdominantGuardAnchorConfidenceFloor` constant + the refactor's shared-primitive comment,
  dropped the now-extracted `lmdPcMod12`/`lmdCollectionMask` defs, and re-pointed B2's three
  `lmdPcMod12(...)` calls → `normalizePc(...)` (proven identical, §2 Family 1).

**B2 stays uncommitted, dormant (flag-OFF), byte-identical to production.** Confirmed after re-apply: build with
B2 in the tree compiles + links; composing 545/545 and snapshots 11/11; **Baroque `.ours.json` 0-diff** vs the
HEAD reference (flag-OFF production output unchanged). B2's git diff changed only cosmetically (its three
`lmdPcMod12` calls are now `normalizePc`); the `.h` diff is identical to the original; the guard logic is
untouched. Both stashes dropped after verification.

Working tree now: HEAD `8bc1441076` + the three held B2 files (unstaged) + the standing HELD docs/diagnostics
(untouched, never staged).
