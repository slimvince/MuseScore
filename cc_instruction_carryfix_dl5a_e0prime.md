# CC instruction — the L4→L5 carry-fix (shape 1) + the D-L5a boundary squash + E0′ (capped-measures re-run)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Also: `cc_e0_fullspine_report.md` §4-A (your own inventory — the design basis), `cowork_confidence_contract.md`
> §2/§5/§7, `cowork_layer4_chordsymbol_design.md` §7, `cowork_layer5_function_design.md` §7.
>
> **Dispatch state: ACTIVE (dispatched 2026-07-02, on the ratified E0 verdict).** Three tasks, THREE separate
> commits (one change-class each), all dormant-layer/byte-identical-on-production, local, unpushed. **No θ/threshold
> calibration anywhere in this run** (Stage-5; the E0 §6-3 sweep stays out of scope). Bash rules as always.
>
> **Cowork ratifications this instruction executes:** carry-fix **shape 1** (carry the fields verbatim — shape 2's
> per-voice-note channel REJECTED: it would re-introduce note-reading into the pure L5 units); the override is NOT
> extended to Inherit; `isPedalPoint`/`pedalBassPc` stay un-carried (your rule-by-rule sweep: no L5 §5 consumer).

## Task 1 — the carry-fix (commit 1)

Extend the L4→L5 carry with the dropped identity fields, per your §4-A inventory:
1. `ChordSliceCandidate` (+ therefore `SliceChord.chosen` and the carried `alternatives`) gains
   `extensions` (the full `ChordIdentity.extensions` bitset) + `naturalFifthPresent`.
2. **Population:** the chosen cell gets the full-identity extraction (per your note the cube cell alone lacks it —
   run the identity extraction on the chosen cell's tones; declare the exact mechanism used). For the carried
   **alternatives**: populate where obtainable **without re-derivation beyond what the decoder already computes**;
   where an alternative's extensions are not obtainable at equal fidelity, carry `extensions=0` + a per-candidate
   `extensionsKnown=false` flag (honest-carry, never a guess) — and REPORT which case occurred.
3. Consumers: the L5 base-RN (§5.1 figured-bass), the `V7/x` applied gate, and the aug6 nationality read the carried
   fields through the existing `formatRomanNumeral` path — verify no second formatter appears (unification).
4. Tests: extend the L4 carry lock-in test (extensions survive the projection; a V7 cell carries MinorSeventh) + an
   L5 test (a carried V7 emits `V7`, fires `V7/x` where the target rules hold). Oracle-asserted.
5. Doc-sync (same commit): `cowork_layer4_chordsymbol_design.md` §7 (the carry now includes extensions +
   naturalFifthPresent + the honest-carry flag) and the §15-O1b carry-limits note; `functioncadence.h:90` comment
   updated (the projection now carries the seventh — the per-voice-note channel remains for the RESOLUTION events,
   which are voice-motion by definition, not a carry workaround anymore).
6. Gate: dormant-layer change only — composing/notation/snapshots green, NO golden refresh, corpus flag-OFF regen
   53/24/53 exact sets, zero production reach (grep-proof as in E0).

## Task 2 — the D-L5a boundary squash (commit 2)

Per contract §5 R5 + §7 D-L5a: `FunctionConfidence` keeps its unbounded internal `combined`, and additionally
publishes a **boundary form** `combinedBoundary = combined / (combined + k)` (monotone rational squash → [0,1); the
shape is fixed here, `k` is a precision-phase constant, default `k = 1.0` — do NOT tune it). Every place the §8
mechanism reads an L5 confidence as a *comparison input* (`forwardoverride` call sites: the §5.4 recompute bar, the
§5.5 case-4 override) reads the boundary form; internal uses unchanged. Tests: boundary ∈ [0,1) on the E0-observed
range (0…25.25), monotone. Doc-sync: contract §7 D-L5a marked CLOSED (this commit hash), `cowork_layer5_function_design.md`
§7 note. Same dormancy gate as Task 1. **Note:** this makes the §8 comparison *commensurable*; it does not claim to
fix the override's net-harm (that is θ-calibration, Stage 5 — E0 §6-3).

## Task 3 — E0′: re-run ONLY the capped/affected measures (commit: none — read-only)

With Tasks 1–2 in: re-run the E0 harness (all 3 presets) and report ONLY:
1. **#1 raw full-RN + EXACT levels** (the cap should close: E0 predicted +7.8/+7.9 EXACT pts recovery) + triad and
   root levels as controls (they should be ≈unchanged — a movement there means Task 1 leaked beyond its scope: STOP).
2. **#7 relational labels** — `V7/x` now firable (E0 counted 316 DCML occurrences); Ger+6 count (expected 0 in Bach).
3. **#9 confidence readout** — the L5 boundary form's min/med/max (must be [0,1)).
4. **The E0 §6-6 rider:** spot-check ~a dozen `keyparse_fail` cases (855 chain vs 110 legacy) — key-naming artifact
   vs genuine key error; report which.
5. The updated §5 better/worse table rows for the re-measured respects only.
Byte-identity: flag-OFF corpus untouched (no regen needed if nothing production-reachable changed — state the
argument); suites green. Deliverable: `cc_e0prime_report.md` (gitignored, HELD), ending with its line count.

## Stop conditions

Task-1 population needing anything resembling re-derivation/synthesis beyond the decoder's existing computation →
STOP + report (the honest-carry flag is the fallback, not silent synthesis). Any control-level movement in E0′ #1
(root/triad) → STOP. Any suite/gate movement → STOP. No θ, no constant tuning, anywhere.

**On your report: Cowork re-reads this instruction, reads the report in full, verifies the two commits at committed
objects (carry fields present in the struct; squash at the §8 read sites) before ratifying.**
