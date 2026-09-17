# CC Instruction — ANCHOR (architecture fix): implement the recompute-on-merged-tones core

> Ratified design: `cc_anchor_design_dossier.md` Option A′, **isolated-core form** (Cowork-reconciled,
> source-verified at HEAD `dd418ecfed`). **This is the FIRST output-moving change** — it fixes the architecture
> defect (a merged region's chord is inherited from a pre-merge slice instead of re-derived from the final tone
> union). It is ARCHITECTURE (the proper-layer fix), and the inference movement is its consequence. North star:
> move root/chord output **toward the DCML/music21 oracle**.
>
> **★ PROTOCOL — measure-then-ratify-then-commit (no surprises, principles 2/4/5):** implement → MEASURE in
> full → **STOP and report the measured movement → await Cowork+user ratification → only THEN update goldens +
> commit.** Do NOT `--update-goldens` and do NOT commit before the movement is ratified correct.

## §0 — Scope: ONLY the recompute. Three things explicitly DEFERRED.
**IN scope:** add a "recompute the merged region's chord (root/quality/extensions) against the COMBINED tones"
step inside the two merge helpers, guarded so it is byte-identical for every region whose tones did not change.
**DEFERRED — do NOT touch in this step:**
1. The **split-first pass re-order** (one `P_max`) — separate structural item; its byte-identity is unproven
   (the min-gap/`lastBoundaryTick` re-span risk, dossier §5.1). Not needed for this fix.
2. The **joint-key re-emit** (`applyJointKeyWiring` re-emitting the chord) — a later, gated step after this is
   validated.
3. **Removing `restampBassMinorSeventhAfterMerge`** — the general recompute likely subsumes it (dossier §5.5),
   but verify-and-remove is a SEPARATE follow-up; leave it in place now (if it double-stamps, note it in the
   report, don't remove yet).

## §1 — The change, in the proper layer
The merged region's identity must be a function of its FINAL tones. The merge helpers own the merged region, so
the recompute belongs there. **Use the production oracle — call `IChordAnalyzer::analyzeChord` (the same path
the passes use), NOT a re-implementation of root/quality logic.** The helpers therefore gain access to the
analyzer + the region's key (a new parameter on `tryCollapseSameChordRegion` and `coalesceShortSameRootRuns`).

- **`tryCollapseSameChordRegion`** (`regionanalyzer.cpp:166`, called :725/:928): on a firing merge, after
  `mergeChordAnalysisTones` builds the combined tone set, recompute the surviving region's `chordResult` by
  `analyzeChord(combinedTones, <the surviving region's key>, …)` and adopt it — **subject to the guard (§2).**
  Keep the existing bass recompute as-is (or let the full recompute subsume it — verify identical bass result).
- **`coalesceShortSameRootRuns`** (`regionanalyzer.cpp:73`, called :1144): same — after the run's tones are
  merged (~:138), recompute the survivor's chord on the union, adopt subject to the guard.
- **Key to use:** the merged region's OWN already-resolved/inherited key (`keyModeResult` / the localKey that
  produced the surviving chord). **Do NOT re-resolve the key here** — that couples the key axis into this change
  (dossier §5.2). Same key, final tones. (The joint-key axis is the deferred step.)

## §2 — ★ The byte-identity guard (isolates movement to merged regions)
**Adopt the recomputed identity ONLY when the combined tone-set actually differs from the tone-set the surviving
chord was scored against.** When a merge does not change the survivor's tones (or the recompute yields the
identical identity), output is **byte-identical** — unmerged regions and no-op merges are provably unchanged.
This is what makes the snapshot/BIR diff small, inspectable, and confined to exactly the held-harmony population
the anchor targets. Verify: a region that never merges is bit-for-bit identical to HEAD.

## §3 — Bounded settle (dossier §3.3 step 5)
Recomputing a merged cell's identity can in principle change its (root,quality) and thus re-enable/disable an
adjacent equal-chord merge. Re-run the collapse→recompute **only over the affected local neighborhood**, capped
at a small N. **Log the observed max iteration count.** Expectation is 1 (occasionally 2); **>2 is a signal to
STOP and investigate, not to raise the cap.** Convergence must be monotone-ish (collapse only ever merges
already-equal chords) — if you observe oscillation, STOP and report.

## §4 — Measurement (run ALL before reporting; obey the VS Code stall rules — redirect large output to a file,
append `; echo "exit:$?"`)
1. **Build** clean (unity). **`composing_tests` + `notation_tests`** both pass.
2. **Settle count** logged (§3).
3. **Snapshots:** run `pipeline_snapshot_tests` WITHOUT `--update-goldens`, redirect to file. The goldens WILL
   move on merged regions. **Inspect EACH diff** — list them, and for each state whether the new chord is
   correct vs the oracle (the union-of-tones reading should be the true held harmony). **Do NOT update goldens
   yet.**
4. **BIR hard gate** — the full per-preset protocol (CLAUDE.md): regenerate Baroque + Jazz + Default into their
   per-preset dirs, run `characterise_bir_false.py`. Capture the **case-identity sets before vs after**, all
   three presets. **Baroque 57 / Jazz 23 / Default 57 must HOLD or improve. Any BIR=false increase in any
   preset is a HARD STOP** — report and await guidance, do not commit.
5. **Oracle correctness (the gate that matters):** root-error / BIR=false **case-identity before vs after** —
   the change must move identities **OUT** of the error set (toward DCML), net, with no new actionable errors.
   Report at BOTH batch-region and `--section-level` granularity (the per-beat view should benefit most).
   Secondary: `analyze_inversion_errors.py`.

## §5 — Report + the handshake (do NOT commit yet)
Write `cc_anchor_recompute_report.md`: the exact change (both helpers + the new param + the guard), the settle
count, the full snapshot diff list with per-diff oracle assessment, the BIR before/after case-identity sets
(3 presets), and the oracle root-error before/after (both granularities). **STOP there.** Cowork verifies the
mechanism at the working tree + reviews the measured movement; the **user ratifies the behavior change**. Only
after ratification: `--update-goldens` (now verified correct), re-run snapshots to confirm green, commit locally
(unpushed), and report the commit hash for Cowork's committed-object verification.

## §6 — Stop conditions (any → STOP, report, do not commit)
- **BIR=false increases in ANY preset** (case-identity) → HARD STOP.
- Net oracle movement is NOT toward DCML, or new actionable errors appear → STOP (the fix is wrong or
  incomplete — redesign, don't ship).
- Settle loop exceeds 2 iterations or oscillates → STOP.
- The recompute is NOT byte-identical for an unmerged region → the guard is wrong → STOP + fix the guard.
- The change appears to need a template/gate/scoring-term edit, or anything outside the chord/region/key
  orchestration + the two merge helpers → STOP and surface (separate scoring task under the CLAUDE.md rules).
- A non-merge code path changes output → STOP (scope leak).
