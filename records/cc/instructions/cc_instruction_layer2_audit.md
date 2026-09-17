# CC Instruction — LAYER 2 (change-point slicing): READ-ONLY audit

> Layer 2 is **signed off** (`cowork_layer2_slicing_design.md`). Before any code, do the **read-only audit** (same
> shape as the layer-1 audit): verify the as-is `[verify]` items at source, characterize the onset+offset slicing
> on real scores, and specify the deterministic slicer test cases. **READ-ONLY — no production code, no behavior
> change, no commit of production.** Output is a dossier; Cowork verifies; user ratifies; THEN we design the impl.
>
> **★ Context you do not have (so do not re-derive it):** this is one layer of a ratified 4-layer rebuild —
> **note model (L1, DONE) → change-point slicing (L2, here) → per-slice analysis with context (L3) → grouping
> (LN)**. Layer 2's *only* job is to enumerate **constant-sonority slices** from the **layer-1 note model** as a
> deterministic FACT (boundaries at every note ONSET and every note RELEASE). It is **NOT** wired into the live
> pipeline and changes **no** behavior — the old segment-first machinery keeps driving analysis until L3. Do not
> "improve" analysis, scoring, or segmentation here. See `cowork_layer2_slicing_design.md` §0–§1 for the contract.
>
> **★ No-assume rule (applies to you):** every as-is statement in the dossier must cite `file:line` from a source
> read. Anything you cannot confirm at source → mark `[unverified]` and list it; do **not** guess.

## §1 — Verify the as-is `[verify]` items at source (the machinery L2 replaces)
The design §3 lists these from a call-flow map; confirm each at `file:line` and record the **exact** criterion
(not a paraphrase). Read the real code, quote the deciding lines:
1. **`harmonicsegmenter::greedyExpandSegmentation`** — the exact coarse-boundary criterion (the Jaccard/greedy
   expansion threshold + stop condition + what evidence it consumes — confirm it is fed the
   `collectRegionTones`/`weightedPcView` callback).
2. **`denseBoundaryTicks`** (`regionanalyzer.cpp` ~270) — what it computes and how it seeds boundaries.
3. **`detectOnsetSubBoundaries`** — the exact onset-PC Jaccard threshold + min-gap.
4. **`detectBassMovementSubBoundaries`** — the exact bass-PC-change criterion + the `kPass2bMinRegionTicks`
   eligibility (`4 * DIVISION`).
5. **Pass orchestration** (`regionanalyzer`) — confirm Pass-1 (coarse) → Pass-2 (onset sub) → Pass-2b (bass sub) →
   Pass-3 merge (`coalesceShortSameRootRuns` / `absorbShortRegions`), and **where** each is called.
6. **The merge** — confirm it is chord-dependent and mutates region tones (the anchor's stale-chord seam), at
   `file:line`. This is the §4.4 defect being designed out.
Deliver this as a precise as-is map (the "what L2 retires" reference), so the eventual retirement plan (§7) is
grounded, not assumed.

## §2 — Characterize the onset+offset slicing on real scores (sizing + sanity)
The offset policy is RESOLVED (boundaries at every onset AND release); confirm it is **sane and sized** on real
data, and answer the two §7 open sub-questions with numbers, not opinion:
- **Method:** a **READ-ONLY, throwaway diagnostic** over the **layer-1 note model** (`NoteModel::build` +
  `overlapping`/onset queries) that enumerates the onset+offset change-point grid per score. **It must NOT touch
  production code paths, NOT be wired into `regionanalyzer`, and NOT be committed as production** — a standalone
  probe / gtest-only harness you run and report from (delete or keep as a clearly-marked diagnostic; do not commit
  to the production pipeline). If building even a throwaway probe risks production entanglement, fall back to a
  hand-worked analysis on 3–5 representative stems and say so.
- **Report, across a representative corpus slice (state which stems):**
  (a) slice count per score and per measure (the candidate-grid density — sizes the L3 per-slice analysis cost,
  the §7 performance question);
  (b) **redundant release-slice frequency** — how often a release opens a slice whose *sounding set otherwise
  implies the same harmony* (i.e. would be grouped away at LN) — this sizes the §7 "collapse early vs leave to
  LN" sub-question. State whether the lean (leave to LN) is comfortable or whether the redundancy is large enough
  to reconsider.
  (c) any **degenerate cases** (e.g. dense tremolo/trill regions, grace clusters) that explode the slice count —
  flag them for the impl design.
- **Do NOT decide the collapse policy here** — surface the data + a lean; the decision rides into the impl design.

## §3 — Specify the deterministic slicer test cases (the impl's coverage spec)
Slicing is a fact, verifiable directly against the note model (no analysis). Specify (do not yet write production)
the deterministic fixtures + expected slice sets, extending the `nm_*` layer-1 fixtures:
- chord + one passing tone → **3 slices** (chord / chord+passing / chord);
- held chord under a moving melody → **a slice per melody onset**;
- a **tie chain** → **no internal boundary** (layer-1 tie-merge already collapses it — confirm);
- **a chord tone releasing mid-span** → a **new slice** (the offset boundary — the §5 amendment's core case);
- **grace note** → attaches to the following slice, **no own one-grace slice**;
- **all-rest** region → empty sounding set (no slice / a single empty slice — state which the design wants);
- **edges:** `end <= start`, single note, onset exactly at a boundary, release exactly at a boundary.
For each: the fixture, the expected `[start,end)` slice list, and which §6 oracle property it checks (completeness
/ constant-sonority / no-spurious-or-missed). This becomes the layer-2 coverage gate (full branch coverage of the
new slicer, per the standing full-coverage rule).

## §4 — Deliver
Write `cc_layer2_audit_dossier.md`: the §1 as-is map (file:line + exact criteria; `[unverified]` for anything not
confirmed), the §2 slicing characterization (numbers + the stems used + the two sub-question leans), and the §3
test spec. **No production code committed.** If a throwaway probe was built, say exactly what it was and that it is
not in the production tree. Cowork verifies the as-is citations at source and that nothing production changed; user
ratifies; then we write the impl design.

## §5 — Stop conditions
- Any **production / behavior / scoring change**, or a probe that entangles with `regionanalyzer`/the live pipeline
  → STOP (this is read-only).
- An as-is criterion cannot be confirmed at source → mark `[unverified]`, do not guess.
- The slicing characterization needs a corpus regen or any non-read-only step → STOP and surface (the audit is
  read-only; sizing should come from the existing note model + existing scores).
