# CC Instruction: Doc pass — preset-cap truth, gate-inventory reconciliation, kTemplateCount

## Context

Stage 1b (`6101a9b2c5`) produced a verified gate inventory and two Cowork-verified
documentation-vs-reality errors. This instruction starts with ONE investigation (Task 1 —
its outcome can stop the run), then aligns the docs with verified reality. Base:
`6101a9b2c5`.

Mandatory reads: `cc_stage1b_report.md` §1 + §4 (the verified inventory/findings),
STATUS.md header. Cowork has independently verified: (a) Gates B/C/D are unreachable,
(b) `maxTotalInversionContextBonus` has **no setter on any path** (only the 2.0 default
in `chordanalyzer.h:411`, the optimizer range entry at :574, two `std::min` uses, and a
batch_analyze comment), and (c) the cap **cannot bind at current values**: the four
inversion bonuses sum to 1.85 (Baroque/default prefs) and 0.75 (Jazz) — both < 2.0.

**Scope: documentation only.** No production code, no tests. Editable files: CLAUDE.md,
docs/scoring_model.md, COWORK_HANDOFF.md, docs/implementation_roadmap.md (one line, see
Task 4). Never stage `muse`; never commit `cc_*`/`cowork_*` working files.

---

## Task 1 — Cap archaeology (BLOCKING investigation — do this first)

Question: were Baroque=2.5 / Jazz=0.6 EVER set in code, or always documentation-only?

```
cd C:\s\MS && git log -S "maxTotalInversionContextBonus" --oneline > /tmp/cap_arch.txt 2>&1; echo "exit:$?"
cat /tmp/cap_arch.txt
```
For each hit, inspect what the commit did with the symbol (`git show <hash> --stat` then
the relevant hunks; redirect big output). Also check the provenance trail:
`docs/scoring_model.md` git history for the §4 caps paragraph
(`git log -L` or `-S "2.5, Jazz=0.6"` style searches), and the
`iteration_plan_inversion_redesign.md` file referenced by the `batch_analyze.cpp:1194`
comment (if it exists in the repo or its history).

**Decision fork:**
- **If 0.6/2.5 were NEVER set in code** → the docs were aspirational fiction; proceed to
  Tasks 2–5 documenting that truth.
- **⛔ If Jazz=0.6 was EVER active in code and later removed** → STOP. Do not write any
  docs. Report immediately with the commit hashes: at 0.6 the Jazz cap BINDS (0.75 sum >
  0.6), so its removal silently changed Jazz behavior at that commit, and every Jazz
  baseline since is suspect. Whether to restore the cap or re-baseline is a Cowork/user
  decision, and the doc wording depends on it.
- Baroque=2.5 ever-active matters less (2.5 never binds vs 1.85 sum) but report it.

## Task 2 — `docs/scoring_model.md` corrections (verified-reality sync)

Grep, don't trust remembered line numbers. All edits cite `cc_stage1b_report.md` where
appropriate.

1. **§4 "Preset-specific scoring caps"** (and any other cap mentions): replace the
   "load-bearing 2.5/0.6" claim with the Task-1 truth. Must state: no path sets the
   value; default 2.0; the cap is currently non-binding everywhere (bonus sums 1.85
   Baroque-default / 0.75 Jazz); the Jazz behavioral difference comes from the reduced
   individual inversion bonuses (0.20/0.20/0.15/0.20), not the cap. Keep the parameter
   documented (it exists in prefs + optimizer range) but labeled as currently inert.
2. **§2 template table / ordering note**: fix the Sus4♭5-vs-HalfDim wording — they are
   not "identical PC sets"; the tie arises on their shared subset {0,6,10} when only
   those tones sound (Stage-1a finding F1, pinned in
   `TiePolicy_ExactTie_LowerTiePriorityWins`).
3. **§6 reconciliation against the verified inventory** (stage1b report §1):
   - Execution order: Gate J runs LAST (after K and L); fix the prose/table order note.
   - The outer guard (`inversionSuspicionMargin > 0`, `inversionBonusReduction < 1`,
     `results.size() >= 2`, `distinctPcs >= 3`) gates ALL of A–L, not just the bias
     correction — state it once above the table.
   - Gates B/C/D: mark **UNREACHABLE (dead code)** in their row — Gate A's fast path has
     a strict subset of their preconditions and always fires first; note that removal is
     deliberately deferred (roadmap Stage-3 obligation, not a hygiene fix).
   - Note the mixed live/captured winner reads in H/I/K/L (Sub-9a fixed only G-E), Gate
     F's missing quality/pcWeight guards, G-E's threshold-free rawCandidates pull +
     possible duplicate push, and that results[] can be left unsorted after gate swaps —
     one short "known asymmetries (pinned in postscoringgates_tests.cpp)" block, not a
     rewrite.
4. **§8 constraints**: add "Gate A subsumes B/C/D — do not add temporal conditions to A
   without realizing B/C/D would become reachable and untested" (or equivalent).

## Task 3 — CLAUDE.md corrections (user has authorized these edits)

1. **"4-site atomic update — template additions only" section**: rewrite for the
   kTemplateCount model (`a236a0ff21`): array extents are compiler-derived from
   `analysis::kTemplateCount` (chordanalyzer.h); adding a template = bump the constant +
   add the template/mask/diag entries (the compiler now catches size mismatches; the old
   silent-stack-overrun failure mode is closed). Point to scoring_model §9 as the
   authoritative checklist and make sure §9 agrees (it was updated in `a236a0ff21` —
   verify, align if needed).
2. **"Preset-specific scoring caps" paragraph** ("load-bearing and must not be
   homogenised... Baroque=2.5, Jazz=0.6"): replace per Task-1 truth (same content as
   Task 2.1, shorter).

## Task 4 — COWORK_HANDOFF.md + roadmap touch-ups

1. In the handoff's "Jazz BIR=false=10 — fully characterised (2026-06-08)" entry: the
   sentence attributing the Baroque-vs-Jazz absent-root difference to "Lower
   maxTotalInversionContextBonus (0.6 vs 2.5)" — correct the attribution to the reduced
   individual inversion bonuses, with a pointer to the Task-1 finding. Touch nothing
   else in the handoff.
2. `docs/implementation_roadmap.md`: add one row to the Stage 3 table (after 3.4):
   `3.4b | Remove dead Gates B/C/D (provably unreachable — stage1b F1) as part of the
   gate-retirement work, NOT before (their removal is byte-identical but belongs to the
   deliberate per-gate retirement audit) | stage1b F1 | byte-identical removal commit`.

## Task 5 — Commit

Doc-only; no build or test run required. ONE commit, explicit staging of exactly:
`CLAUDE.md`, `docs/scoring_model.md`, `COWORK_HANDOFF.md`,
`docs/implementation_roadmap.md`. (STATUS.md is Cowork's to update after your report —
do not touch it.) Proposed message:

```
docs: preset-cap truth, gate-inventory reconciliation, kTemplateCount model

maxTotalInversionContextBonus: no code path ever sets the documented
Baroque=2.5/Jazz=0.6 values (<Task-1 finding: never set / removed in <hash>>);
the cap is non-binding at current bonus sums (1.85 default / 0.75 Jazz). Jazz's
inversion behavior comes from its reduced individual bonuses. CLAUDE.md and
scoring_model.md corrected; COWORK_HANDOFF Jazz characterisation re-attributed.

scoring_model §6 reconciled with the Stage-1b verified gate inventory: Gate J
runs last; one outer guard covers all of A-L; Gates B/C/D marked UNREACHABLE
(Gate A subsumes them — removal deferred to Stage 3 gate retirement, roadmap
3.4b); known asymmetries block added (pinned in postscoringgates_tests.cpp).
Sus4b5/HalfDim tie wording fixed (shared {0,6,10} subset). CLAUDE.md template
checklist rewritten for the compiler-enforced kTemplateCount model.
```
Fill in the Task-1 finding in the message. Commit directly (doc-only precedent), report
the hash.

## Report — inline reply (no file)

1. Task-1 archaeology result: full hit list + verdict (never-set vs removed-in-X), and
   whether the ⛔ stop condition fired.
2. Per-file summary of edits (quote the new cap paragraph verbatim).
3. Commit hash + staged-file list.
4. Anything in the §6 reconciliation where the stage1b report and the code disagreed on
   re-reading (i.e., corrections to the corrections — say so explicitly).

Stop conditions: the ⛔ fork in Task 1; any edit that would change a doc's meaning beyond
the specified corrections; anything that looks like it needs a code change.
