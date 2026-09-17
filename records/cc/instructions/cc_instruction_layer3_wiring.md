# CC Instruction — Layer 3 key/mode: WIRING (Step 1 — replace the per-region resolver with the decoder, BASELINE scorer)

> This is the **first production-changing** Architectural-Layer-3 increment. The isolated decoder
> (`c453315faa`) is built, graded, unified, and the bounded sweep (`2203ad9fda`) confirmed there is **no
> decoder-private improvement left** — so the decoder is ready to become the live key/mode path.
>
> **Two-step plan (do ONLY Step 1 in this increment):**
> - **Step 1 (this increment):** replace the per-region key resolver with the decoder at the region-analyzer seam,
>   **baseline scorer (NO reweight)**, retire the old path, and clear the full production gates.
> - **Step 2 (next, separate increment):** apply the measured `scaleMembership` reweight to the shared scorer
>   (`cc_layer3_sweep_report.md` §3-SPEC), BIR-gated. **Not in this increment.**
>
> **★ Because this moves production, it LEADS with a read-only DESIGN step. Write NO wiring code until the design
> dossier is Cowork-verified and user-ratified.** No-assume: anything about the seam not confirmable at source → STOP.

## §1 — Read-only WIRING DESIGN first (deliverable: a HELD dossier; NO code)
Investigate and specify, at source, exactly how the decoder becomes the live key path. Open questions to answer:
- **The seam.** Confirm `resolveKeyAndModeRanked` @ `regionanalyzer.cpp:633` and the `HarmonicRegion::keyModeResult`
  carrier are still the single production key decision point (the decoder audit dossier found this — re-confirm at
  current HEAD).
- **The slice→region mapping (the central question).** The decoder emits **per-slice** key/mode; the region
  analyzer consumes a **per-region** key. Specify precisely how the per-slice sequence yields each region's
  `keyModeResult`, INCLUDING the case where slices **within one region disagree** (a modulation inside a region):
  which slice's key wins, or is the region re-split? Does the region analyzer already have the Layer-2 slices, or
  must the wiring run the slicer there? State the data flow exactly.
- **Reach-back.** Reconcile the decoder's earlier-context request with the region analyzer's existing windowing —
  does wiring change the analyzed span, and if so, is that within Layer-1's supply contract?
- **The joint-key seam.** `jointKeyWiringEnabled` (default OFF, `:1166`) — confirm wiring does NOT entangle with it;
  keep it OFF/unchanged unless the design explicitly requires otherwise (surface if so).
- **What retires (unification end-state).** Name exactly what this removes: `resolveKeyAndModeRanked` + its
  hysteresis margin, and **`collectPitchContext`** (re-point any remaining caller onto the shared
  `pitchContextOverSpan` view, or retire it). End state must be **one key path, one pitch-context builder** — no
  permanent duplicate.
- **Predicted production move.** The decoder grades −3 Baroque aggregate / +17 Jazz / +modulation vs the resolver,
  so production key output WILL change. Predict where it changes and the likely effect on each gate (§3).
**Output:** `cc_layer3_wiring_design_dossier.md` (HELD/gitignored). **STOP** for Cowork verification + user
ratification. Do not proceed to §2 until ratified.

## §2 — Wiring code (only after the §1 design is ratified) — BASELINE scorer
Implement the ratified design: route the region analyzer's key decision through the decoder, retire the old
resolver path + `collectPitchContext`. **Do NOT apply the scaleMembership reweight** (that is Step 2) — the shared
`KeyModeAnalyzerPreferences` stays at baseline here, so this increment isolates "the decoder replaces the resolver"
as a single, attributable behavior change.

## §3 — Gates (MANDATORY, BOTH presets — this is production-changing)
- **BIR case-identity, no regression:** Baroque **57** / Jazz **23** / Default **57**, byte-or-better. **Any
  BIR=false increase on ANY preset is a HARD STOP.** Run the canonical tools for both Baroque and Jazz
  (`run_bach_preset.py` + `characterise_bir_false.py`, per `CLAUDE.md`).
- **Both test suites pass:** `composing_tests.exe` and `notation_tests.exe` (incl. `pipeline_snapshot_tests`).
- **Pipeline snapshots (P1–P4):** if the key change alters output, the goldens shift. **Do NOT silently refresh.**
  Produce the diff, confirm each change is the decoder being *correct*, and **surface it for ratification** before
  any `--update-goldens`. (First wiring — be conservative.)
- **Key-inference metric (S2):** report the move.
- **Held-out direct metric:** report the wired decoder's production key vs the held-out GT, per preset, to confirm
  the live numbers match the diagnostic grading (no wiring-introduced discrepancy).

## §4 — Unification ledger (standing rule)
State, in the report: what is **reused**, what is **newly written** and why, and what **retires** (the old resolver
+ its hysteresis; `collectPitchContext`). Confirm the end state is **one key path + one pitch-context builder**, and
end with the explicit line: *"No parallel path or logic duplication was introduced."* Cowork verifies at source.

## §5 — Commit + push
- Commit **locally (unpushed)**. **Do NOT push** until Cowork verifies the wiring at source and the user ratifies —
  this is the first production-moving change, so it does not auto-push like the isolated increments.
- Leave held WIP (B2 trio, `STATUS.md`, WIP docs) unstaged. `cc_*` dossier/report gitignored.
- When push is approved: **`origin` only. NEVER `upstream`** (disabled; hard stop).

## §6 — Stop conditions
- The §1 design is not yet ratified → STOP (no wiring code).
- BIR=false increases on any preset, or a test suite fails → STOP (do not refresh goldens to mask it).
- The scaleMembership reweight gets applied here → STOP (that is Step 2, separately gated).
- `collectPitchContext` cannot be cleanly retired / re-pointed → surface the residual rather than leaving two builders.
- The slice→region mapping forces a design choice not covered by the ratified §1 dossier → STOP and surface.
- A push would target `upstream` → STOP (fork-only).
