# CC Instruction — Engage arc #8: measure the TRUE untruncated fan-out (Stage-2 prerequisite, read-only)

> **ACTIVE DISPATCH (Cowork, 2026-07-07).** A small read-only measurement before the Layer-5 engagement
> design (Stage 2): **how large is the graded candidate distribution Layer 5 will select over?** The
> structural audit measured only the **capped floor** (the `alts=3` at-ceiling / append-fire rate ~36 %
> Baroque/Default, 21.5 % Jazz — `cowork_structural_integrity_audit.md` §1.5); the **true** above-threshold
> ranked-set size lives in `gateCtx->rawCandidates` (the uncapped `chosenPerBass`,
> `harmonicfunctionlayer.cpp:570-575`) and is not serialized. This measures it, so Stage 2 designs on the real
> fan-out (#1 — build on measured fact), and the exclusion principle (#12) has the actual tail it reasons over.
>
> **READ-ONLY, byte-identical.** No behavior change, no re-baseline. If any `src/` is needed it is **only** a
> minimal additive default-OFF dump field (byte-identity proven); the default `.ours.json` stays identical, both
> stops trivially green. Moratorium-clear (measurement, not inference or refactor).
>
> **Read first:** `cowork_structural_integrity_audit.md` §1.5 + §1.1 (the `rawCandidates` note) · the
> `rawCandidates`/`chosenPerBass` source (`harmonicfunctionlayer.cpp:520-575`) · `diagnoseChord` (the read-only
> pipeline-replay path).
>
> **Current state:** HEAD `b5857ed2f3`, branch `master`, fork-only, ahead 0. Both stops green. Corpus
> `c50002fee1` (#9, the pinned corpus). **Pending uncommitted Cowork edit in the tree:** the
> `cowork_engage_arc_plan.md` FQ-1/FQ-3→Stage-3 reassignment — fold it in the closing commit.
>
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read files.**

---

## Task 1 — cheapest read-only source (prefer no `src/` change, #6/#5)
Determine the cheapest way to obtain, per slice, the count (and, if cheap, the root/voicing breakdown) of the
**above-threshold** candidate set BEFORE the cap-of-3 — the true fan-out:
- **Prefer** an existing read-only path (`diagnoseChord` replay, or an existing dump that already carries the
  uncapped `rawCandidates`) → measure with a read-only script, **no `src/` change, no build.**
- **Else** a single minimal additive **default-OFF** dump field emitting the untruncated count (reuse the
  fullspine dump if it can carry it — do not add a parallel dump). Prove the default `.ours.json` byte-identical
  (dump off) across 352×3; both stops trivially green; no golden refresh.
State which route, grounded at the source.

## Task 2 — measure the distribution (frozen corpus, stamped)
On corpus `c50002fee1` ×3 presets (#9; stamp corpus-hash + instrument-commit, #16), report:
- **The untruncated fan-out per slice:** min / median / mean / p90 / p99 / max of the above-threshold
  candidate count; the full histogram.
- **The truncation impact:** fraction of slices with >2 carried (where cap-of-3 bites), >3, >5, >10 — i.e.
  how much the cap actually discards vs the ~36 % capped-floor append-fire rate.
- **If cheap:** distinct-**root** count vs distinct-**voicing** count per slice (the decoder dedups voicings;
  Layer 5 selects among readings) — how many genuinely-different-root alternatives exist to reason over.
- A one-line read on what this implies for the Layer-5 selection design (how big/ambiguous the real
  distribution is; where the exclusion tail is load-bearing) — factual, not a design decision.

## Task 3 — report + fold + push
1. **Report** `cc_engage_fanout_measure_report.md` (force-add): the route (Task 1), the distributions + the
   truncation impact, any byte-identity proof if a dump field was added, all SHAs.
2. **Fold** (`docs(cowork):`): the report · `STATUS.md` · `COWORK_HANDOFF.md` · **the pending
   `cowork_engage_arc_plan.md` edit** · `cowork_stage5_fitter_design.md` (engage observation) · this
   instruction (force-add). If a dump field was added, its `feat` is a separate revertible commit (#14).
3. **Push fork-only** — never toward `upstream`/`musescore/MuseScore` (`cfc7eb5e39` HARD STOP).

## STOP conditions
- Any move on the default `.ours.json` path (a dump must be default-OFF; the default surface byte-identical) ⟹
  STOP.
- Any winner/root move (both stops must stay green); any behavior change, corpus write, or re-baseline.
- Any push toward `upstream`/`musescore/MuseScore`.

## Acceptance
The cheapest read-only route chosen + grounded (no-src `diagnoseChord`/existing-dump, else a proven default-OFF
additive field) ✓ · the true untruncated fan-out distribution + truncation impact (+ root/voicing breakdown if
cheap) reported ×3 presets, stamped ✓ · default `.ours.json` byte-identical, both stops green, no re-baseline ✓
· report + fold (incl. the pending plan-doc edit) with SHAs ✓ · pushed fork-only, upstream untouched ✓.

*Cowork, 2026-07-07. Engage arc #8 — the true fan-out measured read-only, so the Layer-5 engagement design
(Stage 2) is built on the real distribution. On CC's report: Cowork brings you the numbers → Stage 2 opens.*
