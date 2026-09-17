# CC Instruction — Stage-5 Phase 2.2e: THE ADOPTION EVENT — kWStepIn 0.10→0.125 (Baroque/Default carriers) + the first frozen-corpus re-baseline

> **ACTIVE DISPATCH (Cowork, 2026-07-05). THIS IS THE RATIFIED ADOPTION EVENT** — the user ratified
> (2026-07-05) the 2.2d recommended candidate **(sameRootInversionBonus 0.40 [UNCHANGED], kWStepIn
> 0.10→0.125)** per `cc_stage5_phase2_2d_report.md` (its §"Prepared-not-applied adoption artifact" is
> this dispatch's blueprint; read it + design §15 O-11 in full). Unlike every prior dispatch, this one
> IS authorized to change a committed value, refresh goldens, and — **the one-time, explicitly ratified
> exception** — write `tools/corpus/` (the first deliberate frozen-corpus re-baseline). Everything else
> stays forbidden: **no other value moves, no rule changes, no push.**
>
> Read first: CLAUDE.md · STATUS.md (top) · `cc_stage5_phase2_2d_report.md` · design §4.7/O-11 ·
> docs/scoring_model.md §4.
>
> **Current state:** HEAD = the 2.2d fold (`ce10fe74dc`); corpus `0dd64660f4` 53/24/53; suites
> 1101/53/11. Expected dirty: the Cowork fold files (design · COWORK_HANDOFF · STATUS ·
> `cowork_candidate_lever_register.md`) + known scratch.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check + pre-flight
HEAD, branch, dirty set. Re-verify the 2.2d surface's key numbers reproduce at the candidate before
anything lands (one fitting eval + one full-Baroque check via the existing drivers: expect fitting
63.5391, full Baroque batch 52 with removal {bwv244.32@5760}, newB=0). A mismatch = STOP.

## Task 1 — the adoption commit (`feat(analysis):` — the ONE revertible behavior change)
1. **`src/composing/analysis/function/harmonicfunctionlayer.h`:** `kWStepIn` initializer 0.10 → **0.125**
   (production delivery — production ships only the Default carrier, O-11 iii). **Verify `kStepBudget`
   recomputes to `0.125 + 0.10 + 0.01 = 0.235`** (the expression initializer; assert in a unit test) and
   **grep-audit every site that could assume the old 0.21** (report each with its disposition).
2. **`tools/batch_analyze.cpp` (the O-9 per-carrier delivery):** Baroque + Default branches set
   `kWStepIn = 0.125` explicitly; **Jazz pinned 0.10; EVERY OTHER preset branch that exists (enumerate
   them all in the report) pinned EXPLICITLY at 0.10** — no unmeasured carrier changes silently
   (mandate 4c). `sameRootInversionBonus` is NOT touched anywhere (0.40 stands).
3. **`tools/param_manifest.json`:** the `kWStepIn` row — `value` 0.125 (per-preset values stated:
   Baroque/Default 0.125, Jazz/others 0.10), and **the FIRST `license_provenance` fill:** `"fitted on:
   reference-corpus fitting split (PD scores / CC-BY-SA WiR annotations), idiom #2 ground truth, only —
   adoption 2026-07-05"`. The `kStepBudget` row value → 0.235 (derived).
4. **`docs/scoring_model.md`** §4: the `w_stepIn` value + the kStepBudget note synced (same commit —
   the CLAUDE.md sync rule).
5. **Rebuild** (5 binaries), run composing + notation (green expected — the value change affects
   corpus-facing behavior, but confirm no unit test pins 0.10/0.21; any that do: update in this commit
   with a note).
6. **Golden refresh:** run `pipeline_snapshot_tests.exe` (expect failures), then diff one golden's delta
   against the 2.2d snapshot preview to CONFIRM the change is the intended fit effect, then
   `--update-goldens` (expect ≈11/11) and re-run green. The goldens ride this commit.

## Task 2 — the frozen-corpus re-baseline (`chore(corpus):` — the ratified corpus write)
1. Regen ALL THREE presets INTO `tools/corpus/{baroque,jazz,default}` with the adopted binary
   (`run_bach_preset.py`, no override — the adopted values are now the code). New manifests (new
   git_hash = the Task-1 commit).
2. **Expected outcome, verified exactly:** `characterise_bir_false.py` ×3 → **Baroque 52 / Jazz 24 /
   Default 52**; the Baroque and Default set-diffs vs the old CLAUDE.md sets = **removal-only
   {bwv244.32@5760}**, Jazz set identical; **the Jazz `.ours.json` files byte-identical to the old
   frozen Jazz** (the pin proof at corpus level). **ANY other set change = STOP: revert Task 1 + Task 2
   entirely, report** (the 2.2d surface promised exactly this diff; a deviation is an
   evidence contradiction).
3. **CLAUDE.md:** the identity-set section re-stamped — Baroque **52** + Default **52** (the sets minus
   `bwv244.32@5760`, with a dated provenance line: "re-baselined at the ratified 2.2e adoption,
   removal-only"), Jazz 24 unchanged; the surrounding prose counts (53/24/53 → 52/24/52) updated
   everywhere they appear.
4. **A-8 baselines re-measured** (`a8_rebaseline_measure.py`, full run): the new ratified root/RN/key
   baselines recorded in CLAUDE.md's dual-track note + the fit-driver's known-vector fixture updated to
   expect them (same commit); the fitting-split baseline re-derived and recorded in the ledger.
5. **O-10 first application:** re-measure the four RETAINED rules' firing sites (the 2.2b regen-diff
   method) on the new corpus; append to the liveness ledger (counts expected similar; a collapse to
   zero = a finding, report).

## Task 3 — the adoption record + report + fold
1. The fitted-set artifact (design §7): idiom-#2 label · carriers Baroque/Default (+production via
   Default) · the vector (kw 0.125) · ledger refs · the provenance statement. Append the adoption-event
   row to the ledger.
2. Report `cc_stage5_phase2_2e_report.md` (force-add): before/after per preset on both tracks (batch
   sets + robust-unit numbers), the kStepBudget audit, the enumerated-and-pinned preset list, the
   golden-diff confirmation, the O-10 liveness table, the exact CLAUDE.md set diffs, reuse-vs-new +
   retires, all SHAs.
3. Fold (`docs(cowork):`): `STATUS.md` (22t) · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`
   (the O-11 adoption record) · `cowork_candidate_lever_register.md` (R-14, the pending Cowork edit) ·
   `cc_instruction_stage5_phase2_2e.md` (force-add).

## STOP conditions
- Task-0 pre-flight mismatch; the Task-2 set-diff deviating from removal-only {bwv244.32@5760} ×2 +
  Jazz-byte-identical (→ FULL revert of Tasks 1–2, report).
- The golden delta not matching the previewed intended effect; kStepBudget ≠ 0.235; a 0.21-assuming
  site with no clean disposition.
- Any value other than kWStepIn (and the derived kStepBudget) changing; any push.

## Acceptance
Adoption commit with provenance + doc-sync + goldens ✓ · corpus re-baselined 52/24/52 with the exact
removal-only diff + Jazz byte-identity ✓ · CLAUDE.md re-stamped ✓ · A-8 baselines + fixture updated ✓ ·
O-10 liveness recorded ✓ · unmeasured presets enumerated + pinned ✓ · report + fold with SHAs ✓ ·
suites green on the refreshed goldens ✓.
