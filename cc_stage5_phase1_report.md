# CC report — Stage-5 fitter, Phase 1 (the fitting harness 1a + the sensitivity screen 1b)

**Dispatch:** `cc_instruction_stage5_phase1.md` (Cowork, 2026-07-04) · **Design:** `cowork_stage5_fitter_design.md` (SIGNED)
**HEAD at dispatch:** `c7d16893d8` · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** 1a is INFRASTRUCTURE (the one sanctioned `src/` touch of the arc — flag-gated, byte-identical when absent, proven). 1b is MEASUREMENT (decode-only; nothing adopted; no committed constant value changed). NO FIT happened.

---

## Commit SHAs (this dispatch)

| Commit | SHA | Type | Contents |
|---|---|---|---|
| 1 — the override mechanism | **`769df17146`** | `feat(analysis):` | paramoverride.{h,cpp} + G1/G6/G7 conversion + batch_analyze `--param-override` + 13 loader tests + scoring_model.md note + the 4 drift fixes |
| 1b — G10 addendum | **`3c3e235dde`** | `feat(analysis):` | reach the one missed production row (kAnnotateKeyConfidenceThreshold, sectionanalyzer.h) — same-pattern conversion; loader-test count 37→38 |
| 2 — a8 additive flags | **`7fd3f7cf70`** | `feat(tools):` | a8 `--corpus-root` / `--preset` (default byte-identical) |
| 3 — the fit driver + split | **`c2914884af`** | `feat(tools):` | stage5_fit_driver.py + stage5_split_registry.json (the proposed split) + a8 `--scores` + run_bach_preset `--param-override` |
| 4 — manifest sensitivity | **`0093cf44f3`** | `feat(tools):` | param_manifest.json `sensitivity` column (values only; 0 non-sensitivity lines changed) |
| 5 — the fold | **`d69336a9bf`** | `docs(cowork):` | STATUS 22m · COWORK_HANDOFF · design markers · cc_instruction_stage5_phase1.md (force-add) |
| 6 — this report | *(this commit)* | `docs(cowork):` | cc_stage5_phase1_report.md (force-add) |

---

## Task 0 — state check

- **HEAD** `c7d16893d8`, branch `master`, fork-only, local/unpushed.
- **Dirty set** matched the dispatch's expectation exactly: the Cowork narrative fold files (`COWORK_HANDOFF.md`, `STATUS.md`, `cowork_stage5_fitter_design.md`) + the deliberately-untracked dumps/scratch (`idiom_discovery/vl_*_out.txt`, `scratch_artifacts/` — STATUS 22e/22g standing ruling). Nothing else dirty. No STOP.
- **Corpus** (re-read at source): baroque/jazz/default each **352/352** `.ours.json`, manifest `git_hash 0dd64660f4` (differs from HEAD as expected — intervening commits are docs-only folds). 352 `.xml` sources present.
- **Suites at entry:** composing 1083 / notation 53 / snapshots 11.

---

## Task 1 (1a-i) — the parameter-override mechanism (the sanctioned `src/` touch)

### Shape (design D-6 / A-6)

An OPTIONAL, flag-gated external override of the scoring pipeline's numeric constants, read once at analysis-binary startup: `batch_analyze --param-override <file>`. The file is line-based — `name value` per line, `#` comments, blank lines ignored — chosen over JSON so the loader lives in the `NO_QT` `composing_analysis` library with zero Qt dependency (Phase-1's file-format latitude, design D-6).

**New module `src/composing/analysis/param/paramoverride.{h,cpp}`:** a by-name registry (three typed maps: double / int / bool) whose entries are the ADDRESSES of the mutable global scoring constants + `ChordAnalyzerPreferences` field setters. `loadAndApply(path, prefs)` parses the file and writes each pair; it is STRICT (an unknown name, malformed number, extra token, or missing file throws `std::runtime_error`), coerces int/bool from the numeric token, and recomputes the one DERIVED constant (kStepBudget = kWStepIn + kWStepOut + 0.01) when its inputs move and it is not pinned. The override loader is the ONLY writer.

### The conversion (constexpr → mutable global), minimal + mechanical

Every hand-chosen scoring constant on the PRODUCTION fit surface became a mutable global (dropping `constexpr`/`const`) with its SAME literal initializer, read exactly as before:

- **G1 (chordanalyzer.cpp):** the 24 file-level `static constexpr double` scoring constants → `static double`; PLUS four former function-local / embedded-literal shaping constants relocated to file scope with unchanged values so their addresses can be registered at static-init (a function-local static is not initialized until its function first runs — too late for the startup loader): `kWComplete` (0.50), `kWCompletePresenceThreshold` (0.05, the wComplete lambda's presence bar), `kComplexityEvidenceFloor` (0.5, the Iter-74 complexity-discount threshold-and-floor — kept as ONE constant to preserve the formula's continuity at the breakpoint), `kAugThinEvidenceFactor` (0.5, the Iter-78/79 augmented thin-evidence halving, both `*=` sites). = 28 G1 globals.
- **G6 (harmonicfunctionlayer.h):** the 5 progression-signal constants (`kWSeq`/`kWDim`/`kWStepIn`/`kWStepOut`/`kStepBudget`) `inline constexpr double` → `inline double`, registered in harmonicfunctionlayer.cpp. `kStepBudget` KEEPS the exact `kWStepIn + kWStepOut + 0.01` expression (NOT the literal `0.21`) to preserve its last-bit IEEE value; kWStepIn/kWStepOut have static (constant) initializers so they are initialized before kStepBudget's dynamic initializer reads them — no cross-TU init-order hazard.
- **G7 (postscoringgates.cpp):** the 4 §6-block gate margins (`kGateIMargin`/`kGateKMargin`/`kGateLMargin`/`kHalfDimFirstInversionBonus`) relocated from function/block locals to file scope + registered.
- **G10 (sectionanalyzer.h, the addendum `3c3e235dde`):** `kAnnotateKeyConfidenceThreshold` (0.8) — the section-layer abstention bar, an `inline constexpr double` of exactly the no-runtime-surface class the dispatch names; missed in the first pass, reached in the same mechanical way.
- **G2–G5 (analysistypes.h `ChordAnalyzerPreferences`):** already runtime-settable struct fields; the loader sets them by name on the per-preset `chordPrefs` object built in batch_analyze (so a prefs override lands on the preset-configured value).

**Total reach: 38 registered globals + 21 prefs fields = 59 reachable override names** covering the entire PRODUCTION fit surface (the manifest's `both` 49 + `production` 10 rows).

### The dormant-row finding (scoping — declared, not improvised)

The dispatch asked the mechanism to "reach ALL 61 tunable rows." The mechanism reaches all **production-surface** rows. The remaining **19 rows are NOT reachable by this mechanism and could not be without wiring the dormant chain (engage-arc scope):**

- **G8 (7 fittable + 1 frozen):** kBoundary, baseBar, confidenceScale, wLicensedOut/In, wCadentialFit, decidingMargin, maxForwardExtendSlices — these are NOT file-level constexpr; they are **struct-member defaults** (`FunctionOutputParams`, `ForwardOverrideParams`, `FunctionResolverParams`) consumed ONLY by the default-off dormant L5 chain. Reaching them means instantiating and wiring the dormant chain into batch_analyze — out of a Phase-1-harness scope, and they are Phase-3 calibration (θ/squash) + Phase-2 family-4 (§15-13) targets, not Phase-1 continuous-scoring ones.
- **G9 (1):** the §15-13 preference-among-licensed weight — value `null` by design (no constant exists yet; the site is recorded, family 4).
- **G11 (1 frozen):** sufficiencyChordTones — a dormant L4 decoder struct member.
- **G12 (5 fittable):** the L1.5 phrase-boundary strength weights — dormant/gated (jointKeyWiring OFF); Phase-3 measurement targets.
- **G13 (4 frozen):** the axis-2 VL-C study-derived floors — dormant; outside the idiom-#2 harmonic fit by construction.

**Consequence for the 1b screen:** every dormant-only row is **Δ=0 by construction on the production carrier** (it is not read on the path that writes `.ours.json`). They appear in the 1b dead-list-by-construction with that reason, and are correctly REJECTED by the strict loader if named (they are not registered). This is faithful reporting of the production/dormant boundary (design D-9), not a silent skip.

### Proofs (all before any 1b run)

1. **Flag absent → byte-identical.** Full-corpus regen ×3 presets to scratch (`run_bach_preset.py`, flag absent) — **352/352 `.ours.json` byte-identical** to the frozen corpus per preset (0 diffs, 0 missing). Re-proven after the G10 addendum (0 diffs ×3).
2. **Identity override → byte-identical.** A per-preset identity override (every reachable constant at its current value; kStepBudget omitted so the loader recomputes it exactly) — **352/352 ×3 byte-identical** again. `batch_analyze` reported `applied 57 overrides (36 global constants, 21 prefs fields)` on a direct run, proving the loader genuinely writes (not a silent no-op).
3. **A changed value moves output.** A single perturbation (bassNoteRootBonus 0.70→2.0) produced a `.ours.json` that DIFFERS from baseline — the mechanism is live, not inert.
4. **Loader unit tests (13):** registry coverage (38 globals), current-values-match-literals, isKnownName spanning globals+prefs, identity-file no-op, changed-global, prefs-field set (incl. int/bool coercion), comments/blank lines ignored, kStepBudget recompute (and explicit-pin-not-recomputed), unknown-name / malformed-value / extra-token / missing-file rejection — all under a fixture that snapshots+restores every registered global so no test perturbs the process-global scorer.
5. **Suites (no golden refresh):** composing **1096** (1083 + 13 new) / notation **53** / snapshots **11**.
6. **Build:** PowerShell `Start-Process setup_and_build.bat` — all 5 binaries relinked, exit 0.

### Doc-sync (same commit, per the CLAUDE.md rule)

`docs/scoring_model.md` gained the §1 override note (scoring constants readable from an optional override file; byte-identical when absent; dormant rows out of reach) and the **four recorded Phase-0 doc-drift fixes**: (1) the missing §6 `kHalfDimFirstInversionBonus` entry ADDED; (2) the §4 progression-signal locations corrected (`w_stepIn/Out/seq/dim` → `harmonicfunctionlayer.*`; the Stage-3.3 migration); (3) the stale §4 anchors (`dim7CharacteristicBonus`, `w_complete`) replaced with stable file+symbol references; (4) the stale §6 gate-table `~Lxxxx` anchors replaced with stable code-region / constant-name references, and the intro's "line numbers reference…" claim corrected.

---

## Task 2 (1a-ii) — additive instrument flags

**`a8_rebaseline_measure.py`** gained `--corpus-root <dir>` (read a scratch root's `<root>/<preset>` subdirs) and `--preset <name>` (single-preset), plus (Commit 3) `--scores <stemlist>` (the fitting-split objective). **Proofs:**

- **Default byte-identical:** a run with NO new flags produced `summary.json` + all per-preset enumerations **byte-identical (0 diffs)** to the pre-change baseline.
- **Single-preset self-validation intact:** `--preset baroque` — grid==oracle OK, `batch_gate=53`; the baroque summary entry AND all baroque enumerations byte-identical to the full-run baroque slice.
- **`--corpus-root` on a manifest-stamped scratch regen:** validated + reproduced 53.
- **`tools/tests` green:** test_metric_scripts 67, test_oracle_root_metric 15, test_metric_primitives_l0l1 22, test_dcml_parser_figbass_pedal 5.

**`characterise_bir_false.py`** already accepts `--corpus-dir` on a scratch dir (Phase-0 finding, re-verified: 352 scores / 326 WiR / **53** on the flag-absent scratch regen) — **no change needed.**

---

## Task 3 (1a-iii) — the fit driver + the ledger + the split

**`tools/stage5_fit_driver.py`** — reuses the pinned instruments verbatim (`run_bach_preset` regen + `a8_rebaseline_measure` objective; batch-stop cases with class read from a8's `mapping.json`); no scoring/comparison logic re-implemented (constraint 10). `evaluate(vector, preset)`: write a minimal override → regen the carrier to a manifest-stamped scratch dir → objective (**variant-(b) root-agree duration; RN + key tracked beside**) → per-evaluation constraints (**no NEW class-(b) batch-stop case** vs the 53/24/53 identity sets; **class-(b) root-disagree DURATION non-increase**) → one ledger row (design §7 schema; `_run_id` + `_timestamp` in separate columns). It **REFUSES a vector touching a frozen row** (P0 enforcement); `--perturb-frozen` exposes the Phase-1b read-only rider (labeled `perturb_frozen` in the ledger).

- **Known-vector fixture (through the full driver, identity override, full coverage):** reproduces the ratified baselines EXACTLY — **Baroque 63.32 % / Jazz 62.37 % / Default 63.22 %** (root governs; RN 44.56/42.40/44.40 % match; key tracked), batch **53/24/53**. **Fitting-split baselines recorded beside** (defined by this task): Baroque **63.50 %** / Jazz **62.43 %** / Default **63.37 %**.
- **Determinism:** two identical evaluations → **byte-identical ledger rows** (ex-timestamp/run_id).

### The PROPOSED fitting/held-out split (ratification-gated — design §4.3 1a)

`tools/stage5_split_registry.json`. The 326 WiR-covered scores, **mode-stratified** (music21 `detectedKey`), deterministic ~80/20 (every 5th score within each mode stratum → held-out, so both strata carry members in BOTH splits — the §4.4a mode strata exist inside the fitting split), each score carrying a `split` field (OQ-C1 discipline):

| mode | fitting | held-out | total |
|---|---|---|---|
| major | 129 | 32 | 161 |
| minor | 132 | 33 | 165 |
| **TOTAL** | **261** | **65** | **326** |

= **80.1 % / 19.9 %.** **This split is ratification-gated: Cowork/user ratify before Phase 2 uses it.** The 1b screen ran on the full-corpus objective (the ratified 326 denominator) with the split-robustness caveat stated below.

---

## Task 4 (1b) — the sensitivity screen (decode-only; nothing adopted)

**Method.** One-at-a-time perturbation of each reachable row through the driver on the
**Baroque carrier** (the idiom-#2 primary). Step policy (design §4.3 1b, stated per row in
`tools/reports/stage5_screen.jsonl`): values in [0,1] → ±0.05 absolute; values >1 → ±10 %;
ints → ±1; the one bool → flip; a non-negative double clamped to 0 in the down direction
is recorded (no eval). **Objective = full-corpus (326 WiR-covered) variant-(b) root-agree
duration**, per the design's ratified denominator; the fitting-split objective ranks
identically (sensitivity is split-robust — the dispatch's stated caveat), so the leverage
ranking is not split-dependent. The 17 frozen rows were perturbed **read-only** (the
P0-ratified rider, `perturb_frozen` flagged in the ledger). Baseline: root **63.3234 %**,
batch **53**. 59 reachable rows screened (117 eval rows); **eval cost ~45 s each**, total
~90 min — within the Phase-0 estimate (no cost STOP).

### Leverage ranking (top movers, Baroque; max |Δroot| over both directions)

| Δroot | parameter | group/family | batch-stop interaction |
|---|---|---|---|
| 0.349 | `extensionThreshold` | G5 abstention | YES — 53→58 both dirs; many new class-(b) |
| 0.308 | `kPowerChord3PcPenalty` | G1 continuous | **NO** (clean high-leverage) |
| 0.279 | `sameRootInversionBonus` | G3 continuous | YES (down 53→49; up 53→55) |
| 0.259 | `kRootToneFactor` | G1 continuous | YES (down 53→59) |
| 0.211 | `bassNoteRootBonus` | G2 continuous | YES (up +0.05 → root +0.211 AND 53→48) |
| 0.210 | `tpcConsistencyBonusPerTone` | G2 continuous | YES (down 53→71!) |
| 0.191 | `kSecondToneFactor` | G1 continuous | YES |
| 0.149 | `rootContinuityBonus` | G2 continuous | YES |
| 0.139 | `kWStepIn` | G6 continuous | YES |
| 0.116 | `kSus4MissingFourth` | G1 continuous | YES (clsB dur only) |

The leverage clusters in **bass/root/inversion evidence** (G2/G3), the **template tone
weights** (G1 root/second-tone factors), **extension detection** (`extensionThreshold`),
and the **power-chord penalty**. `kPowerChord3PcPenalty` is the one high-leverage row with
**no** batch-stop interaction — the cleanest single fit lever.

### Dead list (24 rows, max |Δroot| < 0.0005 both directions — "fit-to-zero" candidates, roadmap 5.2)

`kContradictionPenalty`, `kForeignPenalty`, `kTemplateToneWeightCap`, `kExtraNoteWeightCap`,
`kSus4FlatThirdFactor`, `kSus4SharpThirdFactor`, `kSus4Maj7MissingP5`, `kSus4VariantMissing7th`,
`kDom7FlatFiveTpcPenalty`, `kDom7FlatFiveMissing7th`, `kAugThinEvidenceFactor`,
`kWCompletePresenceThreshold`(fr), `kExtensionThreshold`(fr file), `kBassSupportPresenceThreshold`(fr),
`kSus4StructuralFourthThreshold`(fr), **`kGateIMargin`, `kGateKMargin`, `kGateLMargin`,
`kHalfDimFirstInversionBonus`** (the entire G7 §6-block gate-margin set), `inversionBonusReduction`,
`harmonicBoundaryJaccardThreshold`, `bassPassingToneMinWeightFraction`, `pedalTailWeightMultiplier`,
`kAnnotateKeyConfidenceThreshold`(G10).

**Two structural findings in the dead list:**
- **The G7 §6-block gate margins are all Δ=0 at ±step** — the gates are NARROW corrections
  that do not move the root objective at small perturbations. This is direct evidence for the
  Phase-2 family-2 dissolution audit: the margins are inert at the objective's resolution, so
  the retire/retain question turns on the pinned-fixture replay, not on objective leverage.
- **G10 (`kAnnotateKeyConfidenceThreshold`) is dead**, confirming the manifest's prediction
  that its root-objective sensitivity is nil/indirect. Reaching it was for coverage
  completeness; the screen confirms Δ=0 (not merely by-construction, but measured).

### Interaction warnings (the family-staging signal)

**Nearly every high-leverage row also perturbs the batch-stop set** (batch 53 → 47–71) and/or
adds new class-(b) batch cases. The objective (root-agree) and the batch-stop constraint are
**tightly coupled** on the continuous scoring family (G1/G2/G3/G6). Concretely: `tpcConsistencyBonusPerTone`
down drives batch 53→71 (+17 new class-(b)); `extensionThreshold` ±0.05 drives 53→58; `kRootToneFactor`
down drives 53→59. Per design §4.4, these rows **must be fitted jointly with the §6-block
dissolution track** — a continuous fit cannot be evaluated independently of its batch-stop
churn. (This is a screen finding; no candidate was adopted — the tripwire simply flags each
constraint-violating perturbation in the ledger.)

### Frozen-row findings (the P0 rider — REPORT, do NOT unfreeze)

Seven frozen rows show material leverage under read-only perturbation — exactly the "a freeze
that hides real accuracy surfaces as a finding" case the P0 rider was ratified to catch:

| Δroot | frozen row | freeze rationale (manifest) | finding |
|---|---|---|---|
| 0.161 | `kOtherToneFactor` | "baseline reference =1.0; fitting redundant with scaling the pair" | moves the objective ±0.16 — the "redundant baseline" rationale is challenged; scaling it is NOT equivalent to scaling the other tone factors at the objective |
| 0.156 | `minDistinctPcsForCandidate` | "structural entry gate" | 3→4 costs −0.156 (+3 new class-(b)); a real entry-gate/objective tension |
| 0.110 | `preferMinorOverMajorAdd6` | "boolean structural switch" | flipping it costs −0.110 (+1 class-(b)) — confirms it is genuinely load-bearing (correctly frozen, but not inert) |
| 0.101 | `maxTotalInversionContextBonus` | "INERT/non-binding cap (bonuses sum ≤1.85 < 2.0)" | inert at 2.0, but reducing to 1.8 **binds** and costs −0.101 — the "inert" claim holds only at the current value, not as a fittable |
| 0.017 | `kStepBudget` | "derived guard tolerance" | small but nonzero (the +0.01 slack); derivation faithful under the loader recompute |
| 0.017 | `kSeventhThreshold` | "structural presence bar" | small leverage |
| 0.007 | `kDim7CharacteristicBonus` | "rotation-selector; B3 dead end" | small; the rotation role is unmeasured by root-agree alone |

**Recommendation: keep all seven frozen** (the rider is a measurement, not an unfreeze
trigger), but surface `kOtherToneFactor` and `maxTotalInversionContextBonus` to the user at
Checkpoint P1 — their freeze rationales ("redundant baseline" / "inert cap") are contradicted
by the measured leverage and may warrant a ratified re-classification before Phase 2.

### Default top-10 re-run (constraint 4c — expected near-identical; a divergence is a finding)

The top-10 Baroque movers re-run on the Default carrier (base root 63.2192 %, batch 53).
**The leverage ranking is robust** — the same rows dominate in nearly the same order
(`kPowerChord3PcPenalty` and `sameRootInversionBonus` top both):

| parameter | Baroque Δroot | Default Δroot |
|---|---|---|
| kPowerChord3PcPenalty | 0.308 | 0.302 |
| sameRootInversionBonus | 0.279 | 0.265 |
| bassNoteRootBonus | 0.211 | 0.217 |
| tpcConsistencyBonusPerTone | 0.210 | 0.210 |
| kOtherToneFactor (frozen) | 0.161 | 0.155 |
| minDistinctPcsForCandidate (frozen) | 0.156 | 0.145 |
| kRootToneFactor | 0.259 | 0.236 |
| kSecondToneFactor | 0.191 | 0.159 |
| rootContinuityBonus | 0.149 | 0.187 |
| **extensionThreshold** | **0.349** | **0.230** |

**One divergence worth recording:** `extensionThreshold` is markedly LESS leveraged on Default
(0.230) than Baroque (0.349), and `rootContinuityBonus` slightly MORE (0.187 vs 0.149). Both
carriers use the SAME extensionThreshold value (0.20), so this is not a value difference — it
is the two carriers' slightly different batch-stop sets and PC-decidable-root populations
responding differently to the same detection bar. The divergence is modest and does not change
the family-staging conclusions; it is recorded per constraint 4c (a carrier is a regression
surface, not an optimization target — D-4 evaluates the idiom-#2 vector on Default at adoption,
it does not re-fit).

### Jazz spot-check (shared-scope constraint status only — NOT a fit; A-3 defers the Jazz fit)

The top-10 shared movers re-run on the Jazz carrier (base root 62.3664 %, batch 24) for
**constraint status, not leverage**. The batch-stop coupling is **consistent with Baroque**:
the same rows churn the batch-stop (`tpcConsistencyBonusPerTone` 24→30 / +7 class-(b);
`kRootToneFactor` 24→22), and the two rows that stay clean on Baroque stay clean on Jazz —
`kPowerChord3PcPenalty` (batch 24, 0 new class-(b)) and `bassNoteRootBonus` (batch 24, 0 new).
**No shared-scope row is clean on Baroque but regresses Jazz** — there is no hidden preset
conflict among the high-leverage shared rows. (Jazz's per-row Δroot magnitudes are larger, but
that is leverage, not the spot-check's concern; the Jazz carrier receives no fit — A-3.)

---

## Reuse-vs-new + what retires

- **Reuses (verbatim):** `run_bach_preset.py` / `a8_rebaseline_measure.py` / `characterise_bir_false.py` as the regen + objective + batch-stop readers; the frozen corpus; the `bounds()` optimizer-range table; the manifest.
- **New (committed):** `paramoverride.{h,cpp}` + the constant conversions (the mechanism, `769df17146` + `3c3e235dde`); `paramoverride_tests.cpp`; the a8 additive flags; `stage5_fit_driver.py`; `stage5_split_registry.json`; the scoring_model.md sync.
- **Additive-only tool edits (byte-identical when unused):** a8 `--corpus-root`/`--preset`/`--scores`; run_bach_preset `--param-override`.
- **Retires:** NOTHING. Infrastructure + measurement only; no adoption, no fit, no committed constant value changed.

---

## Checkpoint P1 — the decision surface (the user's call)

**Optimizer feasibility (design D-3).** The measured evaluation cost held at **~45 s/eval**
(regen-dominated, as Phase-0 found). The dead-list pruning removes **24 of 59** reachable
rows from the live set (fit-to-zero), so a coordinate/pattern search runs over **~35 live
fittable rows**; one coordinate sweep at 5 steps ≈ 175 evals ≈ **~2.2 h/pass**. **The
derivative-free coordinate/pattern-search default (D-3) is budget-feasible** — no need to
escalate to a decomposable-loss structured perceptron or CMA-ES on the measured cost. The
single-preset a8 mode (Task 2) already cuts the measure leg; the regen remains the per-vector
floor.

**Suggested family staging (from the interaction warnings).** The continuous scoring family
(G1/G2/G3/G6) is tightly coupled to the batch-stop / §6-block: most objective-moving
perturbations also churn the batch-stop set. Suggested order:
1. **`kPowerChord3PcPenalty` first** — the one high-leverage lever with NO batch-stop
   interaction (a clean, isolated fit target).
2. **The bass/root/inversion continuous cluster (G2/G3) + the tone weights (G1 root/second
   factors) fitted JOINTLY WITH the §6-block dissolution track** (family 1 ∩ family 2) — the
   screen shows they cannot be evaluated independently of their batch-stop churn (design §4.4
   "fitted jointly with the dissolution track").
3. **The §6-block gate margins (G7) via the pinned-fixture replay, not objective leverage** —
   they are Δ=0 at the objective's resolution, so the retire/retain verdict is a fixture
   question (design §4.4 family 2, D-7).
4. **Abstention bars (family 3) last** (extensionThreshold is high-leverage but is an
   indicator threshold — discrete mixing validity, design D-11 vi; it moves the batch-stop
   sharply and is best fitted against the correct-abstention/wrong-commit rates, not the
   continuous objective alone).

**R-13 (transposition augmentation) data-limitation read (§14).** The screen does **not**
show a strong data-limitation signal: the objective's ceiling reads as **coupling-limited**
(the batch-stop churn on nearly every high-leverage row) rather than variance-limited by the
261-score fitting split. The high-leverage rows have large, stable, sign-consistent deltas —
not the noisy small deltas that would motivate augmentation. **Recommendation: R-13 is
optional, not mandated by the sensitivity numbers.** The 326-score single-composer risk
(design §11) remains real for generalization (the validation-pool sweep at each adoption is
the guard), but the fit itself is not measurably data-starved. The user decides at P1.

**The split ratification** (Task 3): the proposed 261/65 mode-stratified split awaits
Cowork/user ratification before Phase 2 uses it; the 1b ranking above is split-robust and
does not depend on it.

---

## Sandwich + suites (end-of-run acceptance)

- **Sandwich — `characterise_bir_false.py` on the REAL per-preset dirs ×3:** Baroque **53** / Jazz **24** / Default **53**; **stem@tick set-diff EMPTY both directions** vs the CLAUDE.md identity sets, all three presets (verified against a8's batch-case mapping on the real corpus). `SANDWICH_RESULT: ALL_MATCH_SETDIFF_EMPTY`.
- **Frozen corpus byte-untouched:** `git status tools/corpus/` = 0 dirty throughout; manifest `git_hash 0dd64660f4` unchanged. Every regen (proofs, fixture, determinism, the ×3 screens) went to scratch dirs.
- **Suites (flag absent, the G10 binary; no golden refresh):** composing **1096** / notation **53** / snapshots **11**.

---

## STOP conditions — status (none tripped)

- **Byte-identity:** PASSED both proofs (flag absent + identity override, 352×3 each), re-proven after the G10 addendum. The arc's central safety property holds. No workaround needed.
- **Constexpr conversions:** all mechanical; none needed logic restructuring. The one derived constant (kStepBudget) is handled by a loader recompute — no read-site logic change; its exact IEEE value is preserved.
- **Dormant-row reach:** recorded as a factual production/dormant boundary finding (design D-9), NOT a STOP — no listed STOP fires; the 19 rows are unreachable without wiring the dormant chain (engage scope) and are Δ=0 by construction on the production carrier. Surfaced for Cowork.
- **1b cost:** ~45 s/eval, within the Phase-0 estimate (< 2×; far under the 4× STOP).
- **Indeterminate perturbation semantics:** none. Every reachable row got a determinate step (int → ±1; bool → flip; [0,1] → ±0.05; >1 → ±10 %); the only "no-op" direction is the down-clamp of a param already at 0 (recorded, not indeterminate).
- **No fit, no adoption, no committed constant value changed.**
