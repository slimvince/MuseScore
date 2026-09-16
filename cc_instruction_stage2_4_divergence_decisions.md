# CC Instruction: Stage 2.4 — Divergence decisions (investigate → draft decisions → one surgical fix)

## Context

Roadmap **2.4**: the accumulated path-divergence findings get DECIDED and written down,
not discovered again. Deliverable is primarily a new ARCHITECTURE.md section of written
decisions (drafted by you, ratified by Cowork before commit), plus at most ONE surgical
code fix (the preset leak) and the queued doc riders. Base: `fb8b980948`.

The four divergences on the table (provenance: part-2 review; audit Finding 3/4;
2.2-i dossier §2/§7):
- **D-P4**: tick-local path builds temporal context cold (no accumulated rolling state,
  no regional tone fields) — same chord can answer differently on P4 vs P3.
- **D-BRIDGE**: `findTemporalContext` analyzes the backward predecessor with `nullptr`
  context; Step-1/2 confidence fields unset on the bridge path.
- **D-PASS0**: notation `analyzeHarmonicRhythm` runs `kDefaultChordAnalyzerPreferences`
  + `excludeLookAheadOnDenseStart=false`; batch runs preset prefs + `true` (the
  excludeLookAhead half is documented load-bearing — D1, Iter 97).
- **D-GAP**: `sectionanalyzer`'s `inferGapRegion` analyzes gap slices with
  `kDefaultChordAnalyzerPreferences` regardless of the caller's prefs (2.2-i dossier:
  likely cause of all 3 genuine A/B regressions).

Standing rules (handoff trust-model incl. rule 4); never guess — every decision draft
must cite [probe]/[code] evidence. Pre-authorized scope + ARCHITECTURE.md + the rider
files listed in Task 4.

---

## Task 1 — Investigations (the decisions depend on these — do them first)

1. **How does the user's style/preset actually reach the notation analysis path?**
   Trace `IComposingAnalysisConfiguration` / `composingconfiguration.cpp` →
   `analyzeHarmonicRhythm` → prefs construction. Key question: when a user works on a
   jazz chart in the app, do Jazz-tuned `ChordAnalyzerPreferences` (the batch-preset
   values: extensionThreshold 0.12, reduced inversion bonuses, preferMinorOverMajorAdd6
   false) EVER apply on P1/P2/P3 — or does the live product always analyze with
   defaults, making the entire preset system a batch-tools-only concept? [probe/code]
   This determines whether D-PASS0 is "documented intentional" or "the preset system
   never shipped to users" — very different decisions.
2. **D-GAP blast radius**: if `inferGapRegion` is threaded with the caller's prefs:
   (a) notation/snapshot path — if that path's prefs are defaults anyway (per #1),
   threading changes NOTHING there (expected: snapshots byte-identical); (b) the
   `--section-level` diagnostic path under a preset — the only behavior change.
   Confirm by probe (run the 2.2-i A/B pair on the 3 regression cases with a threaded
   prototype) BEFORE proposing the fix as safe.
3. **P4 reality check (cheap)**: how often does the P4 fallback actually fire (P3
   returns empty) — grep callers/conditions and reason from code; if establishable
   cheaply via a probe on 2–3 scores, do it; otherwise state unknown.
4. Confirm bridge Step-1/2 field state on the bridge path today [code] (expected:
   default-initialized → predecessor-confidence signals inert there).

## Task 2 — Decision drafts (ARCHITECTURE.md, new section "Path divergence decisions
(Stage 2.4)") — DRAFT in the report first, commit only after Cowork ratifies

For each divergence: the facts (with evidence tags), the decision, the revisit trigger.
Cowork's prior leanings (override with evidence if the investigation contradicts):
- **D-P4 / D-BRIDGE**: document cold-context as the CURRENT CONTRACT (with the
  context-banner precedent from 2.3); defer re-architecture to Stage 3 — the decoder's
  lattice makes accumulated context a decode product, and any pre-pass built now would
  be torn up then. Explicit revisit marker: "Stage 3 design must state what P4/bridge
  consume."
- **D-PASS0**: depends entirely on Task 1.1. If presets never reach users: record that
  as a product-level finding (the Jazz tuning is currently a measurement-only artifact)
  and DEFER any unification to a deliberate product decision — do not silently flip
  the user path onto presets. If presets DO reach users via config: document the
  actual flow and reconcile the docs that claim otherwise.
- **D-GAP**: fix now IF Task 1.2 proves user-neutral + gate-neutral (see Task 3);
  otherwise document + defer with the probe data.

## Task 3 — The one surgical fix (conditional): thread prefs through `inferGapRegion`

Only if Task 1.2 confirms: thread the caller's `ChordAnalyzerPreferences` through
`analyzeSection` → `inferGapRegion` (mechanical parameter plumbing; the notation path
passes what it passes today — no user-visible change by construction). Verification:
full suites; **snapshots 11/11 ZERO diffs (hard — they exercise analyzeSection)**; BIR
both presets 13/7 + identity sets (flag-off batch path doesn't run section — confirm
unchanged); the 3 regression cases re-run under `--section-level` with preset prefs —
report whether they heal (expected, not required; healing validates the dossier's
causal hypothesis, and say so either way).

## Task 4 — Riders

1. CLAUDE.md:159/166 — remove kDiagTemplates from the template-addition checklist
   (post-2.3 reality: one array + kMasks; cite scoring_model §9).
2. ARCHITECTURE.md:861 — `contextualBonuses()` reference → historical phrasing.
3. layer_architecture_audit.md:84–92 — mark the L1634-comment action item DONE-BY-2.3.
4. Periodic bookkeeping docs commit: STATUS.md + COWORK_HANDOFF.md +
   docs/implementation_roadmap.md as they stand (sanity-check coherence, don't rewrite).

## Commits

- V1 (riders 1–3 + Task 2's ARCHITECTURE.md section) — ONLY after Cowork ratifies the
  decision drafts in your report.
- V2 (Task 3 fix, if green) — after ratification likewise.
- V3 (rider 4 bookkeeping docs) — direct, no confirmation needed.

## Report — `cc_stage2_4_report.md`

§1 Task-1 findings (the preset-flow answer is the headline); §2 the four decision
drafts verbatim (ready to paste into ARCHITECTURE.md); §3 D-GAP probe data + fix
verification (or why not fixed); §4 rider diffs; §5 unknowns. Tag everything
[probe]/[code]. STOP and report WITHOUT committing V1/V2: this instruction's commits
are ratification-gated by design.

Stop conditions: preset flow can't be established (don't guess — that answer gates two
decisions); any snapshot diff under the D-GAP fix; anything suggesting the notation
path is NOT default-prefs (would invalidate several prior assumptions — report
immediately, it's bigger than this instruction).
