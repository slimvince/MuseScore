# CC Instruction — LAYER 3 / Increment A: index the L1 note-model queries (BYTE-IDENTICAL)

> First increment of the L3 key/mode build (`cowork_layer3_keymode_impl_design.md` §1). **Pure performance fix,
> byte-identical output.** The audit verified `NoteModel::overlapping`/`onsetIn` scan `m_notes` from the head →
> O(N) per query → **O(N²) over slices** (`note_model.cpp:141-176`); the per-slice L3 path will call them per slice,
> so this is fatal at full-act scale (requirement R1). Index the queries; **return identical results, just faster.**
>
> **★ This is an L1 amendment, but BEHAVIOR-FROZEN:** L1's *output contract* does not change — same notes, same
> order, for every query. Only the query implementation gets faster. Do **not** change `NoteEvent`, the build
> semantics, ties, flags, or ordering. If anything would change a query *result*, STOP — that is not this increment.
>
> **★ No-assume:** confirm the current behavior at source before editing; the result **order** is load-bearing
> (consumers rely on build order) — preserve it exactly.

## §1 — The fix
`m_notes` is sorted by onset ascending (build order: onset, then staff, voice, note). Make each query O(log N + result):
- **`onsetIn(t0,t1)`** — straightforward: binary-search the onset-sorted vector to the `[t0,t1)` onset sub-range
  (`lower_bound(t0)` … `lower_bound(t1)`), emit in place. Preserves order for free.
- **`overlapping(t0,t1)`** — the harder one: a note with `onset < t0` can still overlap if `release > t0`, so you
  cannot simply binary-search the lower bound on onset. Build a **static interval index once in `NoteModel::build`**
  (O(N log N)) supporting "all notes whose `[onset,release)` overlaps `[t0,t1)`" in O(log N + result). Choose the
  cleanest correct structure (confirm feasibility at source) — e.g. an **interval tree**, or the onset-sorted array
  **augmented with a max-`release` index** (segment/Fenwick tree over the prefix max release) to prune the
  non-overlapping early notes, or an equivalent. **The result must be emitted in the same build order** the linear
  scan produces (sort/merge the hits back into onset/staff/voice/note order if the structure yields them otherwise).
- Keep the existing `t1 <= t0 → {}` guard and all edge behavior identical.
- The index is built once and owned by `NoteModel`; the `Score`-outlives-model contract is unchanged.

## §2 — Gate (identical results + byte-identity + the perf win)
1. **Identical results — a direct unit test.** In `note_model_tests.cpp` (or a sibling), add a test that, for the
   `nm_*` fixtures, runs **many random `[t0,t1)` ranges** (incl. edges: empty, full span, mid-note, exact
   boundaries, before-first/after-last) and asserts **indexed `overlapping`/`onsetIn` == the linear-scan reference,
   element-for-element INCLUDING ORDER** (keep the old linear scan as the reference oracle, or recompute it inline).
   This is the load-bearing correctness proof.
2. **Byte-identity — the suites.** The whole analysis pipeline already calls `overlapping` on real scores, so:
   `composing_tests` 572, `notation_tests` 57, pipeline snapshots 11/11 must pass **byte-identical, no golden
   refresh**; BIR/oracle unchanged. If any moves, a query result changed → STOP.
3. **The perf win — measured.** Show the complexity actually dropped: a micro-benchmark or re-run a per-slice
   `overlapping` workload (e.g. the L2 `--validate-slices` corpus pass, which calls it per slice) before/after and
   report total + worst-stem time. Confirm it scales ~O(N log N), not O(N²).
4. **Full branch coverage** of the new index code (standing rule); any unreachable branch documented.

## §3 — Workflow + deliver
Commit **locally (unpushed)**: `note_model.{h,cpp}` + the new test (+ any micro-benchmark, diagnostic-only). Leave
all held WIP (B2, docs, STATUS) unstaged. Message: `perf(composing): Layer 3/A — index NoteModel overlapping/onsetIn
(byte-identical, O(N²)→O(N log N))`. Write `cc_layer3_incrementA_report.md`: the structure chosen + why, the
identical-results test (ranges/edges covered), the byte-identity confirmation (572/57/11, no golden refresh,
BIR/oracle flat), the before→after timing, and coverage. Cowork verifies identical-results + byte-identity at
source; user ratifies; then push; then Increment B.

## §4 — Stop conditions
- Any query returns a **different result or order** than the linear scan → STOP (this increment is byte-identical).
- Any suite/snapshot/BIR/oracle number moves → STOP (a result changed).
- The index would require changing `NoteEvent` / build semantics / the output contract → STOP (out of scope for A).
- The cleanest correct structure can't hit O(log N + result) without a horizon/cap → STOP and surface (we removed
  the horizon deliberately; do not reintroduce one).
