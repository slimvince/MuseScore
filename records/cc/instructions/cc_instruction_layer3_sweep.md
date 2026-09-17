# CC Instruction — Layer 3 key/mode: the BOUNDED L3 SWEEP (isolated; act only on the clean-L3 set)

> The decomposition (`cc_layer3_error_decomposition_report.md`) bounded the real L3-recoverable headroom to the
> **clean set = A∩stable + B∩stable ≈ 11.5 % Baroque / 7.4 % Jazz of misses** — everything else is L5
> (tonicization-vs-modulation arbitration, same-collection tonal-center selection) or a tiny chord/spelling tail.
> This increment acts on the clean set and ONLY the clean set. The decoder stays **isolated** (graded via
> `--decode-keymode`, NOT wired), so **production analysis output stays byte-identical**.
>
> **★ No-assume / no-context guards (read these first):**
> - **Do NOT touch the shared emission scorer.** `KeyModeAnalyzer` / `KeyModeAnalyzerPreferences` are shared with
>   the live per-region resolver. Changing any emission weight there moves PRODUCTION → byte-identity breaks. The
>   only settings you may tune are the **decoder-private** `KeyModeSequencePreferences`.
> - **Do NOT chase the A-pile headline (54.5 %/33.9 %).** Most of it is A∩modulation = the tonicization problem,
>   which is L5. Target A∩stable + B∩stable only.
> - **Do NOT wire the decoder.** Wiring is the next, separately-ratified increment.

## §1 — Step 1 (read-only): confirm A∩stable before tuning anything
The clean-L3 claim rests on A∩stable, which was NOT in the 4 decomposition spot-checks. Hand-verify a small sample
(≥5 per preset) of A∩stable cases against the raw score: confirm each is genuinely *a stable region where a
strongly-present distinguishing pc was out-scored* (emission underweighting), NOT a mislabeled tonicization. Report
the agreement. If a material fraction are actually tonicizations (i.e. A∩stable is itself contaminated), STOP and
surface it — the clean-L3 number would need revising before any tuning.

## §2 — What the sweep may change (decoder-private only)
Tune **only** `KeyModeSequencePreferences` (decoder-private; production-safe because the decoder is unwired):
- **`changeBaseCost` / `relativePairExtraCost` / `changePerFifthStep`** — for **B∩stable** (over-smoothed real
  modulations the cost suppressed). **This is a tradeoff, not a free win:** the decomposition §3 showed the B/C
  boundary is L5-contested in the 1–2-measure band — lowering the cost to recover B-modulations will also
  un-suppress C-tonicizations. So you MUST report the **tradeoff curve** (B recovered vs C newly-wrong) across the
  swept values and pick a defensible point, not the B-maximizing one. Do not trade C-errors for B-gains net-negative.
- **`topK` / `maxAlternatives`** — for the **E-pruning** coverage share (a viable state locally outranked). Widening
  surfaces more carried states; report whether it actually recovers misses or just enlarges the lattice (it is
  necessary-but-not-sufficient — the carried state still has to win selection).
- **`windowBeats`** — only if Step 1 / grading shows a window-size effect on A∩stable; otherwise leave it.

All swept values stay **settings** (effort-retrofit hygiene); record the chosen defaults + the sweep range.

## §3 — A∩stable (the headline lever): DIAGNOSE + SPECIFY here, APPLY at wiring
A∩stable's root cause is the **shared emission scorer underweighting a present distinguishing pc** — so the clean
fix is an emission-weight change, which you may NOT apply in this isolated increment (it would move production).
Do this instead:
- **Diagnose** which `KeyModeAnalyzerPreferences` weight is responsible (e.g. the third / leading-tone /
  characteristic-modal-degree weight) by measuring, over the A∩stable sample, which present pc lost and what weight
  governs it.
- **Specify** the proposed reweighting and its **predicted** effect on the clean set, as a written spec for the
  **wiring increment** (where the decoder replaces the resolver and the scorer can be tuned once for BOTH paths —
  no byte-identity conflict, no throwaway decoder-side shim). Do NOT build a decoder-side re-rank that compensates
  for the emission — that would be a permanent duplicate of the scorer's job (violates the unification rule).
- If you believe a decoder-side selection stage is genuinely architectural (not a scorer shim), STOP and surface
  the design question rather than building it — Cowork/user decide whether it belongs in the decoder or the scorer.

## §4 — Grade + close the loop (one grading path)
After tuning the decoder-private knobs, on the held-out **TEST** split, per preset, reusing the existing harness:
- Report the **directional move** vs the pre-sweep decoder (the unambiguous full-match + the modulation-region
  top-1), and confirm **production is byte-identical** (composing/notation/snapshot/`.ours.json` unchanged — the
  decoder is still unwired).
- **Re-run the decomposition** (`--decompose`) and the **calibration** (`--characterize`) and report whether the
  clean-L3 piles (A∩stable + B∩stable) actually **shrank**, and whether calibration moved (reliability-curve
  sharpness; `uncertain` recall — though recall is mostly a later `uncertainThreshold` question, note it).
- **Stopping rule:** when further knob tuning yields diminishing returns on the clean set, STOP. The residual is
  then the attributed L5 mass + the A∩stable emission spec deferred to wiring. Report the plateau — that is the
  signal that the identifiable L3 improvements are exhausted.

## §5 — Constraints
- Decoder stays isolated/unwired; production byte-identical. The shared `KeyModeAnalyzer(Preferences)` is untouched.
- Only `KeyModeSequencePreferences` changed; all changes are settings, not hardcoded constants.
- One grading path (extend the existing `cc_layer3_keymode_baseline.py` modes; no second metric).
- No L5 work, no chasing A∩modulation / C / D / F. If a lever can only move those, it is out of scope — note it.

## §5a — Unification: ZERO parallel paths / logic duplication (standing rule)
Total unification is a hard project objective — one path per concern, no second copy of any logic. This increment is
mostly setting changes, so the risk is low, but it must be confirmed, not assumed:
- **No new parallel path.** Tuning is in-place on the existing decoder settings; any harness change EXTENDS the single
  grading path (`cc_layer3_keymode_baseline.py`), it does not fork a second metric or a second decode driver.
- **No duplicated logic.** Do not add a second copy of the change-cost, circle-of-fifths-distance, pitch-context, or
  selection logic. Reuse the existing primitives (`pitchContextOverSpan`, `cofDistance`, `KeyModeAnalyzer`,
  `decodeLattice`). If A∩stable tempts a decoder-side selection stage, that is the scorer's job — specify-and-defer
  (§3), do not duplicate.
- **Report the ledger (mandatory).** The sweep report must state, exactly as the build increments do: what existing
  code is **reused**, what (if anything) is **newly written** and why a new piece was unavoidable, and what — if
  anything — this **retires**. It must end with an explicit line: *"No parallel path or logic duplication was
  introduced."* Cowork verifies this at source; a permanent duplicate path is a defect, like doc drift or a coverage gap.

## §6 — Deliverable, commit + push
- Commit the decoder-private setting changes + any harness additions locally (its own increment). Leave held WIP
  (B2 trio, `STATUS.md`, WIP docs) unstaged; the `cc_*` sweep report gitignored/local.
- Report `cc_layer3_sweep_report.md`: Step-1 A∩stable confirmation, the swept knobs + chosen defaults, the B/C
  tradeoff curve, the directional + decomposition + calibration re-measure, the byte-identity confirmation, and the
  **A∩stable emission-reweighting spec handed to the wiring increment**.
- **Push `origin` only. NEVER `upstream`** (disabled; hard stop). Report the new `origin/master` SHA + file list.

## §7 — Stop conditions
- Step 1 shows A∩stable is contaminated by tonicizations → STOP (the clean-L3 target needs revising first).
- A change would touch `KeyModeAnalyzer` / `KeyModeAnalyzerPreferences` or any production path → STOP (byte-identity).
- The B-cost tuning trades C-errors for B-gains net-negative → STOP at the defensible point; do not maximize B.
- You are about to build a decoder-side re-rank that duplicates the emission scorer's job → STOP and surface.
- A push would target `upstream` → STOP (fork-only).
