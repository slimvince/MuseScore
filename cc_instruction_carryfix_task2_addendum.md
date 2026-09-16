# Addendum — Task 2 ruling (Cowork, 2026-07-02): Option 1, "publish combinedBoundary only"

> Addendum to `cc_instruction_carryfix_dl5a_e0prime.md`. Your STOP was correct, and your grep/site analysis is
> **Cowork-verified at the committed objects** (`.combined` written only at `functionoutput.cpp:124` + 1 test;
> §5.5 incumbent = `s.confidence.composite`; §5.4 incumbent = `homeKeyConfidence`). **The premise error was in the
> instruction's Task-2 part (b)** — it contradicted the confidence contract's own §4 frame table (which correctly
> names the F-A/F-B incumbents as L3/L4 quantities). The contract stands; the instruction is corrected here.
> Owned by Cowork.

## Task 2, as ruled (commit 2)

1. **Part (a) as specified:** `FunctionConfidence` gains `combinedBoundary = combined / (combined + k)` (k = 1.0
   default, NOT tuned), computed at the output assembly (`functionoutput.cpp`) — the L5→L6/§7 **output boundary** is
   where the contract's U2 squash applies. Internal uses unchanged. This IS the D-L5a close-out.
2. **Part (b) is VACUOUS as written — do not re-plumb anything.** The §8 sites stay byte-identical. Instead, add a
   **code comment at each of the two sites** stating the frame per the contract (§4 F-A / F-B): the exact incumbent
   and contradiction quantities compared, and that their scale commensurability + θ are Stage-5 calibration items.
   No behavior change of any kind.
3. Tests/doc-sync as originally specified for part (a); additionally sync
   `cowork_confidence_contract.md` is Cowork's edit (already done — §7 D-L5a close-out semantics precise + the new
   **D-FS** delta), not yours.

## Task 3 amendments (E0′)

- **#9 reads `combinedBoundary`** from the output/dump (must be [0,1) over the E0-observed 0…25.25 range).
- **NEW cheap rider (frame-scale evidence for Stage 5):** report observed min/median/max of the two contradiction
  quantities as they fire — the §5.5 plausibility-diff (`bestPlaus − committedPlaus`) and the §5.4
  `cadentialWeight` — per preset. Read-only; this is the D-FS scale evidence the θ-calibration will need.

## Unchanged

Task 1 exactly as specified (your two-tier extraction plan — `deriveChordExtensions` factored pure + byte-identical,
chosen = guaranteed full extraction, alternatives = match-or-honest-carry — is consistent with the ratified shape 1;
proceed). Option 2 (re-plumbing §8 to read L5 combined) is REJECTED as a silent data-flow/behavior change; if the
Stage-5 calibration later wants the L5 function confidence as an input to any frame, that is a declared new-frame
design step per contract §4, never a plumbing side effect. All stop conditions unchanged.
