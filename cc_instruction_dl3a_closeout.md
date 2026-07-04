# CC INSTRUCTION — D-L3a close-out: the sequence margin becomes THE L3 boundary confidence (2026-07-04)

**Status: ACTIVE DISPATCH (the only open instruction). A small, declaration-level close-out — contract §7
D-L3a, pre-ratified in principle at the contract ratification (§8.4: "small byte-visible-only-in-dormant
fixes"), evidence now in hand (C1: the margin is 2.8–3.1× better calibrated than the sigmoid on every preset,
`cc_c1_reliability_report.md` §3). NO behavior change: no threshold change, no consumer decision change, no
squash/θ change. Runs in parallel with Cowork's Wave-3 scoping (census §8c audit) — no shared files.**

## Mandatory reads BEFORE any work

1. `CLAUDE.md` (bash rules; both suites; gate discipline) + `STATUS.md` header + 22j.
2. `cowork_confidence_contract.md` §3 (the L3 row), §7 (D-L3a), §8.4.
3. `cc_c1_reliability_report.md` §2.1/§2.1a/§3 (the evidence + the two numbers' identities at source).
4. `cowork_layer3_keymode_design.md` — the §15-3 margin provenance + wherever the spec names the L3 output
   confidence.

## The two numbers (identities as established by the C1 dispatch — re-verify at source, Task 0)

- **Sequence margin** = `HarmonicRegion.keyConfidence` (= `rep.confidence`, regionanalyzer.cpp §15-3).
- **Emission sigmoid** = `KeyModeAnalysisResult.normalizedConfidence` — NOTE the naming hazard: the frozen
  corpus `.ours.json` region field NAMED `keyConfidence` carries the SIGMOID, not the margin.
- [prov, verify] The sigmoid's remaining production role is the downstream 0.8 gate (C1 report §5.1 —
  CC-asserted, not yet Cowork-verified; Task 0 confirms or corrects).

## Task 0 — consumer inventory at source (the knowledge that gates the edit)

Enumerate EVERY reader of both numbers (production + dormant chain + tools): `HarmonicRegion.keyConfidence`
and `normalizedConfidence` wherever L3's result crosses a layer boundary. For each reader, state whether it
treats the value as (a) a boundary confidence, (b) an internal gate/threshold input, or (c) a diagnostic
export. **STOP if the demotion would change what any live consumer computes** — that would be a behavior
change needing a Cowork ruling, not a close-out.

## Task 1 — the close-out edit (declaration + demotion, byte-identical)

- At the L3 output boundary, declare the **sequence margin THE boundary confidence** and the sigmoid
  **internal/diagnostic** — comments + naming at the boundary types/wiring as appropriate. Keep the mechanical
  footprint minimal; renames only where they make the declaration real to a reader of the code, and NEVER the
  frozen-corpus JSON field name (`keyConfidence` in `.ours.json` stays byte-identical — the corpus is frozen).
- The 0.8 gate (or whatever Task 0 shows the sigmoid feeds) keeps its input and constant UNCHANGED — demotion
  is a role declaration, not a rewiring.
- If Task 0 shows a dormant-chain site that publishes the sigmoid AS the L3 confidence (the D-L5a analogue),
  re-point it to the margin — that is the "byte-visible-only-in-dormant" part §8.4 pre-ratified. Any
  dormant-output byte change must be exactly this re-point, shown in the report.

## Task 2 — doc-sync (same commit as the code edit)

- `cowork_confidence_contract.md`: the §3 L3 row states the margin as THE boundary form (sigmoid demoted,
  named diagnostic); §7 D-L3a → **✅ CLOSED** citing the C1 evidence (ECE 0.125–0.142 vs 0.38–0.44) + this
  commit's SHA pattern per the D-L5a row's format.
- `cowork_layer3_keymode_design.md`: the output-confidence statement updated to as-built.
- Any stale comment that calls the sigmoid "the confidence" at a boundary site.

## Task 3 — acceptance + report (`cc_dl3a_closeout_report.md`, force-added, own commit citing the code SHA)

- Both suites green; snapshots 11/11 NO refresh; standard `.ours.json` byte-identical (spot-diff); the gate
  sandwich 53/24/53 case-identity set-diff empty ×3 (measured, not argued).
- Report: the Task-0 consumer table; the exact edit surface; any dormant-output byte change isolated and
  shown; reuse-vs-new + what retires (expected: the sigmoid's boundary-confidence ROLE retires; no code path
  duplicated); **commit SHAs mandatory**.
- The docs commit may ALSO fold the two pending Cowork close-out edits — `STATUS.md` (the 22j ★ CLOSED note +
  the new dispatch line) and `COWORK_HANDOFF.md` (header) — exactly those two, surfacing any other dirty
  cowork file rather than including it.

## STOP conditions

Task-0 shows a consumer whose computation would change; the frozen-corpus JSON would change; snapshots or the
gate sandwich fail; the edit starts wanting a threshold/constant change (record for Stage 5, never do it);
anything under the legacy path (it retires at engage, R8 — do not touch it).
