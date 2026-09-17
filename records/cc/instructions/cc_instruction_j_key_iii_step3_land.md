# CC Instruction — J-key-iii (Step 3): adjudicate snapshots → flip ON → COMMIT the key win

> **Ratified (user, 2026-06-15): ship the J-key-i key win.** Key-only wiring is verified clean (BIR
> byte-identical, §5 win realized). This step adjudicates the moved snapshot goldens, refreshes only the
> verified-correct ones, flips the production default ON, re-runs every gate, and **commits the FIRST
> key-axis production behavior change** (local, UNPUSHED). One Cowork checkpoint: present the adjudication
> HELD for source-verification **before** the final commit.

---

## §1 — The landing sequence
1. Adjudicate every moved snapshot golden (§2).
2. Refresh ONLY the verified-correct goldens; **STOP if any adjudicates as a regression** (§2).
3. Flip the production default ON (§3).
4. Re-run ALL gates with wiring ON (§4) — BIR must stay 57/23/57; suites green.
5. Present HELD with the full adjudication (§5) → Cowork verifies at source → then commit (§5).

## §2 — Adjudicate the 11 moved snapshot goldens (the load-bearing gate)

All 11 snapshots move = key/RN re-contextualization (chords unchanged). For EACH moved golden, adjudicate
whether the new key/RN is **correct**:
- **Bach (WiR) scores:** adjudicate the new RN against **DCML** ground truth (the committed
  `dcml_parser`/`compare_rn` machinery) — does the new key/RN match DCML better than (or equal to) the old.
- **Non-Bach scores** (Mozart/Chopin/etc., outside WiR-Bach scope): adjudicate against the **music21
  `RomanNumeral` oracle** + a **theory spot-check** on any music21 disagreement (music21 is algorithmic, not
  gold — confirm disagreements by hand).
- **Bucket each:** improvement / neutral (equivalent) / **regression**. Document the per-score verdict
  (old RN → new RN, DCML-or-music21 reference, verdict) in the report.

**STOP condition:** if ANY moved golden adjudicates as a **regression** (the new key/RN is worse than the
old per DCML/music21+theory), do NOT refresh it, do NOT flip ON — surface it for a Cowork/user decision.
Only proceed when every moved golden is improvement-or-neutral.

## §3 — Refresh goldens + flip the production default ON
- Refresh the verified-correct goldens: `pipeline_snapshot_tests --update-goldens`, then re-run to confirm
  all pass.
- **Flip the production default ON** so the committed behavior includes the win — make
  `jointKeyWiringEnabled()` default to true (or make the wiring unconditional on the production/bridge path).
  Keep the OFF path available for measurement if cheap, but the **committed default = wiring ON**. Confirm
  the bridge/notation path actually runs the wiring (not just the tools path).

## §4 — Re-run ALL gates with wiring ON
- `composing_tests`, `notation_tests`, `pipeline_snapshot_tests` — all green (snapshots now refreshed). If
  `notation_tests` has any key/RN-pinned assertion that moved, adjudicate it the same way (§2) before
  updating.
- **BIR gate:** regen all 3 presets + `characterise_bir_false` with wiring ON → must be **57/23/57,
  byte-identical case-identity** (chord untouched). **Any BIR=false increase → HARD STOP** (it would mean
  the chord axis moved, contradicting key-only).
- Confirm the key win is live end-to-end (the resolved key + RN reflect the joint decision on the
  production path).

## §5 — Present HELD → Cowork verifies → COMMIT
Write `cc_j_key_iii_step3_report.md` (HELD) with the full §2 per-score adjudication, the §4 gate results,
and the flip-ON confirmation. **Do NOT commit yet** — present for Cowork source-verification of the
adjudication (the 11 per-score verdicts + the BIR-unchanged + the flip-ON site). On Cowork's confirmation,
**commit (local, UNPUSHED)** — the commit message states this is the **first intentional production behavior
change on the key axis (the constrained-joint architecture's key-axis landing)**, key-only (chord axis
byte-identical), win +3.80/+3.50/+12.24 pp. No `docs/scoring_model.md` sync (key-only, no chord-scoring term
moved). **Do NOT push** (origin = the fork; the user pushes separately per the git-topology rule).

## §6 — Stop conditions
- Any moved snapshot/notation golden adjudicates as a **regression** → STOP, surface (do not refresh/flip).
- **BIR moves** on any preset (≠ 57/23/57) → HARD STOP (chord axis should be untouched — key-only).
- Any suite fails un-adjudicated → STOP.
- The flip-ON does not actually reach the production/bridge path (win not live) → STOP, diagnose.
- Any push, or any edit outside `src/composing/` + `tools/` + the committed snapshot goldens → STOP.
- Committing before Cowork has verified the adjudication at source → STOP (present HELD first).
