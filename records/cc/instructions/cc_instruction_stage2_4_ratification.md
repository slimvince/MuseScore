# CC Instruction: Stage 2.4 ratification — commit V1+V2, plus the missing measurement

## Ratification

Cowork ratifies, based on `cc_stage2_4_report.md` (verified):

1. **V1 — RATIFIED AS DRAFTED.** Paste the §2 decision section into ARCHITECTURE.md
   verbatim and apply riders 1–3 exactly as the §4 diffs. One addition to the D-PASS0
   Half-A text (append to its Facts paragraph): *"Sharper still: the struct default
   (`preferMinorOverMajorAdd6=false`) matches NO batch preset — even 'Standard' sets it
   true — so the configuration the live product actually runs has, as of Stage 2.4,
   never been corpus-measured. The `--preset Default` measurement (below) closes that."*
   Commit V1.
2. **V2 — RATIFIED.** Commit the D-GAP threading fix as verified. The §3.2
   falsification of the dossier's causal hypothesis is accepted and has been corrected
   in `docs/implementation_roadmap.md` (2.4 row) by Cowork; your §2 D-GAP draft already
   states it correctly.
3. The §3.2 isolation limitation and §5 unknowns are accepted as stated.

## New Task — measure the configuration users actually run (V4)

The headline's corollary: no BIR/identity numbers exist for the live product's chord
scoring (struct defaults). Close that with a measurement (informational — NOT a new
gate):

1. Add `--preset Default` to `batch_analyze` (or `--preset RawDefault` if "Default"
   collides — your call, document it): `ChordAnalyzerPreferences` untouched struct
   defaults AND mode priors at their code defaults (the app's out-of-box state — verify
   what the app actually defaults to for mode priors [code] and match THAT; if the
   app's defaults differ from code defaults, say so and match the app).
2. Regenerate a third per-preset corpus dir (`tools/corpus/default/`,
   manifest-stamped) and run both metrics:
   `characterise_bir_false --corpus-dir tools/corpus/default` and
   `analyze_inversion_errors --corpus-dir tools/corpus/default`.
3. Report: BIR=false count + identity set + 24/13-style split, side by side with
   Baroque (13/24) and Jazz (7/35). Note overlaps/divergences in the identity sets —
   especially which of the canonical Baroque-13 / Jazz-7 cases persist under the user
   config (those are the ones users actually experience).
4. Record the numbers in STATUS.md-ready form in your report (Cowork writes STATUS);
   add one sentence to the ARCHITECTURE D-PASS0 decision pointing at the measured
   numbers. The existing 13/7 gates are UNCHANGED — this is a third, informational
   column, explicitly labeled "user-default config (no gate)".
5. Commit as V4 `tools: --preset Default + user-default-config corpus measurement
   (Stage 2.4 follow-through)`.

Verification for V4: existing gates untouched (Baroque 13 / Jazz 7 re-validated from
their dirs — cheap, no regen needed if manifests validate); Python suite green (extend
the preset-name test if one pins the preset list).

## Commit order

V1 → V2 → V4, explicit staging each, `muse` never, report all three hashes + the V4
measurement table inline.

Stop conditions: V4's app-default mode priors can't be established (don't guess — ship
the chord-prefs-default measurement with code-default priors and STATE the uncertainty);
any movement in the existing Baroque/Jazz numbers (nothing in this instruction may
touch them).
