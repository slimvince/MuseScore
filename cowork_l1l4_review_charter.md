# L1–L4 comprehensive review + tidy — charter (the step-3 QA gate, before L5)

> **Context (ratified 2026-06-26).** **Engage-with-L5** is the ratified strategy: the **L4 build is COMPLETE and
> PROVEN** (G1, G2/G3, two-reading inherit, G6, spelling-pin — measured +5.5/+5.8 better where it commits; ~85% of its
> abstention is genuinely function-dependent → L5), but it is **dormant**, and the **production switch + legacy
> retirement + the coverage seal are joint with L5**. Before opening L5, the user mandates a **comprehensive review of
> L1–L4** with two aims:
> 1. **KNOW, don't assume** — every load-bearing claim verified at source (the standing "verified facts only" rule).
> 2. **Tidy imperfections** — code, test cases, test data, documentation.
>
> **Scope:** the built layers **L1, L1.5, L2, L3, L4** (incl. the dormant new `chordslicedecoder` path) + their tests,
> fixtures, and docs. **Out of scope:** L5/L6 (not built); inference *accuracy* (firewall — Phase B).

## Standards (apply to every finding)
- **Verified, not assumed:** cite file:line / commit-sha; mark VERIFIED vs INFERRED. The mount-staleness rule holds —
  **Cowork uses the file tools, never bash for working-tree reads**; CC reads on Windows (authoritative).
- **Tidy guardrails — what may be fixed vs what must NOT:**
  - **Freely tidy:** documentation (accuracy / consistency / staleness), orphaned test data + fixtures, stale/weak
    tests, stale code *comments*, dead-vocabulary names.
  - **Tidy only byte-identical or gated:** behavioural code changes go under the two-tier BIR gate + suites + snapshots;
    a genuine correctness bug (e.g. German-bass) is **flagged**, fixed only as a ratified gated step — not folded silently.
  - **MUST NOT touch:** inference accuracy (the leading-tone C→F gate, scoring tuning — firewall, Phase B); the
    **dormant new-L4 path and the staged scaffolding** (`chordslicedecoder`, `redecodeRange`, `tonicizationlabeler`,
    `DecodeQualityLevel`) — they are *deferred-engagement*, NOT dead-code-to-delete (their wire-or-remove verdict is the
    joint L4+L5 engagement). Removing them is a STOP.
  - **No inference-problem-fixing** anywhere (the firewall stands until the whole stack is built + tested).

## Division of labour
**Cowork (docs + architecture coherence) — file tools / agents, read-only + doc edits:**
- Every L1–L4 **design doc / spec** (the layer docs, the bounded-context / reach-back / tpc / L4 spec, the Phase-5b
  plan, the ledger) — accurate, complete, internally consistent, **synced to as-built** (the delta-check covered L1–L3
  status; re-confirm + cover L4/the new path).
- `ARCHITECTURE.md`, `docs/scoring_model.md`, `STATUS.md`, `COWORK_HANDOFF.md`, the gate tables — current, accurate,
  non-contradictory (the doc-truth pass fixed 57/23→53/24; confirm nothing stale remains).
- **Architecture coherence:** does the *as-built* still realise the forward-only layered intent (no new back-edges from
  the L4 build; the L4→L5 abstain contract is clean; the tpc/spelling/types-leaf are where the design says)?

**CC (code + tests + test data + the tidying) — on Windows, source + build/run:**
- **Code:** correctness vs spec (verified), unification (no new duplication from the L4 build; the deferred
  `analysisutils.h` relocation; the two-segmenter / two-pitch-context state), dead-vs-staged honesty, stale comments,
  dead-vocabulary names (e.g. `applyIter8691Pedal`).
- **Tests:** the suites green; oracle-quality (not echoing); the `DISABLED_`/xfail surfaced-defect ledger; stale/orphaned
  tests.
- **Test data:** orphaned fixtures (the `chord_analysis_test` stubs etc. — re-verify whole-repo, then remove the
  confirmed orphans); fixture hygiene; corpus integrity.
- **Tidy** the freely-tidyable imperfections (per the guardrails), each gated; **flag** (do not silently fix) anything
  behavioural or firewall-adjacent.

## Output & close
Each side writes a findings + tidy report (CC: `cc_l1l4_review_report.md`; Cowork: a consolidated review note). Then:
the tidy commits land (gated, by-sha-verified), the surfaced defects are a tracked list, and we reach the **✅ L1–L4
COMPLETE / nothing-left (modulo the joint-L5 engagement+retirement+seal)** sign-off → **then L5.**
