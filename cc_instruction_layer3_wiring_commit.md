# CC Instruction — Layer 3 wiring: COMMIT Step-1 (decoder replaces the per-region resolver) under the (B)-amended gate

> The two-tier gate is refined and ratified (CLAUDE.md guardrail (3) → **class-(b) count non-increasing** + class-(a)
> verified/recorded/magnitude-watch). The Jazz +1 is **accepted** as documented interim class-(a) (retires at Layer 4
> rotation-pinning). Commit the faithful **Step-1-only** wiring (rule (b) duration-majority, S2 seed, **Step-2
> reverted**, shared scorer baseline).
>
> **★ FIRST production-moving commit.** Run the full gate, classify the snapshot diff, **then STOP and surface before
> any `--update-goldens` or commit** (golden refresh + the commit both need ratification). Commit **locally only**;
> **do NOT push** until Cowork source-verifies and the user ratifies.

## §1 — Confirm the held state is exactly Step-1
- Working tree = Step-1-only wiring: rule (b) duration-majority, S2 seed kept, **Step-2 reverted**, shared scorer at
  baseline (`scaleScoreInKeySigOnly = -0.20`, `scaleScoreInNeither = -0.05`), no reweight residue. The 5 modified
  source files. Corpora reproduce **Baroque 53 / Jazz 24 / Default 53**.

## §2 — Re-run the full gate under the (B)-amended rule (both presets)
- **BIR (canonical tools, both presets):**
  - **Zero new class-(b)** on any preset (guardrail 1) — re-confirm.
  - **class-(b) (decidable-root) count non-increasing** (guardrail 3, refined) — the meaningful errors did not grow.
  - **Every new class-(a) case verified at the score and recorded** (stem@tick + sonority): Baroque
    `{bwv272@4320, bwv289@20160}`, Jazz `{bwv272@4320, bwv291@17760}`, Default `{list the 3}`. Net: Baroque/Default
    **−4**, Jazz **+1** (accepted). Magnitude small (≤3/preset) — within the watch.
  - **Any** new case not *provably* class-(a), or any class-(b), or a *large* class-(a) swing → **STOP/surface.**
- **Both suites:** `composing_tests` + `notation_tests` (incl. `pipeline_snapshot_tests`).
- **Snapshots:** produce the diff and **classify every change** as one of: (i) a legitimate key/RN improvement (the
  −3 Baroque / +17 Jazz / modulation gains), (ii) a class-(a) rotation relabel, or (iii) a confidence-gated
  KeyArea/cadence change (the C1 mapping). **P4 goldens must be byte-identical** (P4-defer) — if any P4 golden moves,
  STOP. **Do NOT `--update-goldens` yet.**
- **S2 grid stable; held-out faithfulness == the as-graded decoder.**

## §3 — STOP and surface (before goldens, before commit)
Surface for Cowork source-verification + user ratification: the BIR class-(a)/(b) split per preset (with the
verified class-(a) identities), and the **classified snapshot diff** (so the user ratifies exactly which pinned
goldens change and why). **Do not proceed to §4 until ratified.**

## §4 — (After ratification) refresh goldens + commit LOCALLY
- `--update-goldens` for the ratified P1/P2/P3 snapshot changes only (P4 untouched); re-run to confirm green.
- Commit **locally (unpushed)** the Step-1 wiring + the refreshed goldens + the **STATUS.md** BIR-baseline update
  (the post-wiring state: class-(b) baseline unchanged, the accepted class-(a) interim cases, the cases fixed, per
  preset). **Do NOT** edit the CLAUDE.md canonical class-(b) identity sets in this commit (a deliberate re-baseline
  is a separate Cowork doc-sync; the CLAUDE.md amendment already records the Jazz interim case).
- Leave the *other* held WIP (B2 trio, WIP docs) unstaged. `cc_*` report gitignored.

## §5 — Unification ledger (in the report)
Reuse / newly-written / retired. End-state: **one key path (decoder) + one builder (`pitchContextOverSpan`) on the
production region path.** Surface the residuals: P4 still on the resolver (tracked follow-up = P4-redecode); the
resolver + `collectPitchContext` remain as the diagnostic/grading baseline. End with: *"No NEW parallel path or logic
duplication was introduced."* Cowork verifies at source.

## §6 — Push = separate, gated
- **Do NOT push.** Hold for Cowork source-verification of the committed object + user ratification. When approved:
  **`origin` only, NEVER `upstream`** (disabled; hard stop).

## §7 — Stop conditions
- Any new class-(b), an unverified class-(a) case, or a large class-(a) swing → STOP.
- A P4 golden moves, the coarse grid shifts, or held-out faithfulness diverges from the as-graded decoder → STOP.
- `--update-goldens` before §3 ratification, or any push before approval → STOP.
- `upstream` targeted → STOP.
