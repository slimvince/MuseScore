# CC instruction — seams part 1: the OI-197 spelling parity + the record-producing entry (dormant)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `OPEN_ITEMS.md` (NEW rows **OI-196/OI-197**, riding
> your Task-0 commit), and the ratified `C:\s\MS\cowork_notation_output_contract.md` §1 (the
> two seams — THIS dispatch builds the producer + the views; the consumer re-plumb is seams
> part 2; the switch is later still).
>
> **Current state:** branch `master`; expected HEAD `e336bd0348` (the modal-reading commit,
> pushed) — verify via `git show --stat e336bd0348` and that HEAD matches; mismatch = STOP.
> Riding Cowork edits (verify only non-yours diffs): `OPEN_ITEMS.md` (OI-196/OI-197 rows),
> `cowork_handoff.md`. This dispatch file stays untracked.
>
> **Hard stops, always:** origin only; files outside the touchable set; ANY change to committed
> corpus bytes, goldens, `tools/robust_stop/`, or notation-path behavior (everything here is
> dormant); a surprise is a STOP (#13). VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-26, at the record-assembly verification. Two purposes:
(1) discharge **OI-197** — the C++ spelling derivation's missing corpus-wide establishment (a
SWITCH PRECONDITION, #19); (2) the §1 seams' PRODUCER side — the one-call score→record entry
plus the span and note views, dormant, fully covered. **No behavior change anywhere.**

**Touchable set:** `src/composing/analysis/joint/**` + its tests + CMake lists;
`tools/batch_analyze.cpp` (ONLY a default-OFF driver extension for Task 1);
`tools/joint_estimator/gen_spelling_establishment.py` (extend for Task 1) + its artifact;
`ARCHITECTURE.md`, `STATUS.md`, `OPEN_ITEMS.md` (row flips only); the riding Cowork files.
Pinned instruments import-only.

---

## Task 0 — the rows commit (ONE commit, first)

Commit the riding Cowork files exactly, message: `register: OI-196 (interim fifths-mapping
duplicate, unifies at map item 2) + OI-197 (C++ spelling establishment owed before the switch);
handoff record-assembly verification`. Push origin. Report the hash.

## Task 1 — OI-197: the lof-exact C++↔Python spelling parity (ONE commit; flips the row or STOPs)

The gap (the row): the §5.2 derived-vs-notated establishment ran on the PYTHON mapping; the C++
mapping — what the switch publishes — needs the same-strength establishment. Both implement one
documented derivation, so the check is exact equality:

1. Extend the establishment surface: a default-OFF `tools/batch_analyze.cpp` driver (extend the
   existing joint diagnostic family) dumps, for EVERY committed segment of the 326-piece corpus
   decode (selected arm, embedded tables), the C++ record's derived root and bass spellings as
   line-of-fifths integers (+ stem@tick + classKey). Extend `gen_spelling_establishment.py` (or
   a sibling comparator in the same file) to emit the Python-side lof per segment and compare:
   **lof-EXACT equality, both fields, all segments** (13,063 roots / 11,182 sounding-bass
   cells — reconcile your counts against the committed `spelling_establishment.json`).
2. **Any divergence = STOP** (one implementation is wrong; do not decide which by editing —
   report). Zero divergence ⟹ the C++ mapping inherits the Python-side corpus establishment
   (root 99.985 % / bass 99.982 % derived-vs-notated with the 4 enumerated enharmonic-
   convention divergences) — state this inheritance explicitly in the artifact's establishment
   block and the report.
3. Commit (code + regenerated artifact with the parity block); **flip OI-197 ✅ RESOLVED** with
   the hash + the zero-divergence figure in the same commit. Push origin.

## Task 2 — the record-producing entry + the two views (ONE commit, with doc sync)

The §1 seams' producer, on the joint module's surface (DORMANT — declared dormancy; named
consumer: seams part 2's re-plumbed notation consumers):

1. **The producer:** one function, score in → record out — `buildAdapterFacts` → the embedded
   `FittedAdapter`/tables → `decodePiece` (§5 decode, selected weights, seg_cap 4) →
   `computePosteriorSlice` → the record assembly (the delivered §3.1–§3.4 form). Whole-score
   decode, once; deterministic (§5); no caching in this increment (a cache is a later,
   measured concern — do not build one speculatively, #17's funnel).
2. **The span view (§1 seam 1):** given [startTick, endTick), the record's segments
   intersecting the span (plus the piece block) — a pure view, no recompute; document the
   intersection semantics (a segment is included iff it overlaps the span).
3. **The note view (§1 seam 2):** given a tick, the CONTAINING segment (`startTick <= t <
   endTick`), its committed reading, derived facts, and both §3.3 group (i) lists — the
   display-ready answer the right-click menu / harmony-write / status-bar consumers will read
   at part 2. Document the boundary rule (a tick at a segment boundary belongs to the segment
   it starts).
4. **Edge duties (report each explicitly):** an empty span; a tick outside the analyzed span;
   a score whose adapter extraction fails (`AdapterFacts.ok == false` — the producer returns
   an unambiguous failure state, never a partial record; no silent fallback to anything, #13).
5. **Coverage:** unit tests — the producer on ≥2 corpus scores (record equals the same
   assembly built from the same decode by parts — an internal-consistency check, plus segment
   fields spot-checked against `decode_parity_ref.json`'s selected arm for those stems); the
   span view's overlap semantics (including a span splitting a segment); the note view's
   boundary rule; every edge duty above.
6. **Doc sync (#10, this commit):** `ARCHITECTURE.md` joint as-built — the producer + views
   (dormant; consumer = seams part 2); `STATUS.md` closing entry.
7. Commit + push origin.

## Report

Hashes; the Task-1 parity figures (segments × 2 fields compared, divergences — expected 0 — and
the count reconciliation vs the committed artifact); the OI-197 flip; the Task-2 view semantics
as implemented + the edge-duty dispositions; suite totals (all three suites); reuse-vs-new /
what-retires (expected: the producer composes exclusively delivered, established parts; nothing
retires — the legacy seam retires at the switch); anomalies (a surprise is a STOP). Standing
self-check before reporting: re-read every commit's actual diff against the principles and
`DEFECT_TYPES.md`.
