# CC report — Phase 5c Step-5 V7/IV correction (Part A) + Step 6 output assembly (Part B), L5 §7, dormant

> **Plan:** `cowork_phase5c_l5_build_plan.md` Step 6. **Spec (SIGNED):** `cowork_layer5_function_design.md` §5.6 (corrected)
> + §7 + §3 "Produces" + §9-D1 + the §5.0 shared defs. **Discipline:** dormant + byte-identical, reuse-heavy, default
> constants (firewall), proportionality.
> **Outcome: BOTH parts DONE, dormant, byte-identical on production by construction. Steps 0–6 of the L5 build plan COMPLETE.**

## §0 — Sweep (commit the unstaged Cowork doc)
Committed local-only the modified `cowork_layer5_function_design.md` — the §5.6 applied-trigger correction (the broadened
trigger: a chromatic dominant-function chord of a non-tonic degree, the chromaticism a raised secondary leading tone **or**
a ♭7̂; the false-positive guard rejects only a genuinely diatonic chord) + the §5.3 Step-4 note.
- **`0911195d9e`** `docs(cowork): Phase-5c Step-5 ratification + §5.6 applied-trigger fix`.

---
# PART A — Step-5 correction: emit `V7/IV` (the ♭7̂ applied-trigger fix)

## A1 — The change (`function/functionrelationallabel.{h,cpp}`, the unified applied path)
**Problem (the Step-5 declared divergence, now ruled by Cowork).** The unified `emitAppliedLabel` reused the dormant
`tonicizationlabeler`, whose false-positive guard is a **raised-secondary-leading-tone-only** check
(`pcInMask(collMask, d+11)` → skip when the target's leading tone is *diatonic*). For **V7/IV** the target IV's leading
tone is the **diatonic third degree**, so the guard wrongly **dropped** `V7/IV` — yet `V7/IV` IS a genuine applied
dominant whose chromaticism is the **♭7̂**, and the production `formatRomanNumeral` inline applied path **correctly emits**
it. A dormant emitter that drops `V7/IV` would regress at engagement and mis-measure at Step M.

**The fix (broaden the trigger, keep the guard).** After the guarded labeler returns *not applied*, `emitAppliedLabel` now
checks the **♭7̂-chromatic applied-dominant** case the labeler drops: a **dominant seventh** (Major + `MinorSeventh`) whose
root is a **perfect fifth above a non-tonic diatonic degree** and whose **minor seventh (♭7̂) is itself chromatic** to the
key. When it fires, the label is emitted via the **production `formatRomanNumeral` inline path** (`makeResult(in, nextRootPc)`
→ `formatRomanNumeral`) — **reuse, no second formatter** (§3). The false-positive guard for a **genuinely diatonic** chord
is **kept**: the broadening fires **only** when the ♭7̂ is chromatic, so a fully-diatonic dominant seventh of a non-tonic
degree (e.g. the natural-minor `VII7→III`, no accidental) stays **not applied** (§5.6: "rejects only a genuinely diatonic
chord, no chromaticism at all"). The raised-LT applied chords (`V/V`, `V7/V`, `viiø7/V`, the plain-triad `V/x`) still flow
through the guarded labeler unchanged.

★ **Why the production inline path is NOT delegated wholesale.** The production inline path is **unguarded** (it emits
`V7/x` for *any* dom7 a fifth above a non-tonic diatonic target). On a **minor key** that over-emits: a fully-diatonic
`VII7→III` (e.g. `G7→C` in A minor, no accidental) would be wrongly labeled `V7/III`. The corrected §5.6 still requires
chromaticism ("a chord … that is *chromatic* relative to the home key"), and the labeler's comment cites this exact
false-positive as DCML-agreed-not-applied. So the fix keeps the chromaticism guard and reuses the production path **only
for the string emission** of the genuinely-chromatic ♭7̂ case. (Decision A-D1, declared below.)

## A2 — Tests (oracle-asserted, +3, all green) + the still-open viio/IV divergence
`functionrelationallabel_tests.cpp` (16 → 19):
- **`AppliedDominantSeventhOfSubdominantFlatSeven`** — `C7→F` in C major → **`V7/IV`**, role `AppliedSecondary`,
  targetDegree 3, targetPc F (the ♭7̂ Bb is the chromatic tone; the raised LT E is diatonic).
- **`AppliedFlatSevenGuardRejectsDiatonicSeventh`** — `G7→C` in **A minor** (the natural-minor `VII7→III`, both LT B and
  ♭7̂ F diatonic) → **not applied** (the kept guard; DCML agrees).
- **`AppliedFlatSevenTriadOfSubdominantIsNotApplied`** — the **same root motion without the seventh** (a plain `C→F`
  triad = `I→IV`) → **not applied** (the broadening requires the chromatic seventh).
- The existing `V/V`, `V7/V`, `viiø7/V`, Neapolitan, It/Fr/Ger-by-spelling, modal-mixture, precedence, and role-None tests
  all still pass (16/16 unchanged).

★ **Declared (A-D2): the `viio/IV` case is left as a still-open divergence — out of Part A's stated scope.** Part A's
broadening is, per A1, the **♭7̂ applied DOMINANT** (`V7/IV`). The leading-tone analogue — a diminished chord rooted on a
*diatonic* leading tone (e.g. an `E-G-B♭` viio of IV, root E diatonic but the chord chromatic) — is **also** dropped by the
labeler's raised-LT guard and **emitted** by the unguarded production inline path, so the unified emitter and production
**still diverge** on `viio/IV`. §5.6 (corrected) names only the raised-LT and ♭7̂ **dominant** cases; the `viio/IV` case is
not named, so I did **not** speculatively broaden to it (the standing rule: declare inference-shaped divergences, do not
code around them). **Cowork ruling requested**: should the leading-tone-of-a-subdominant case likewise be admitted (it is
genuinely chromatic), or held as the inline path's residual over-emission to reconcile at Phase 5d?

## A-Gate — dormant + byte-identical (no movement, no STOP)
- **composing 958 → 961 (+3** FunctionRelationalLabel).
- **notation 53** (4 skipped baseline).
- **pipeline_snapshot 11/11 — NO golden refresh** (chord output byte-identical).
- **corpus 53/24/53 unchanged BY CONSTRUCTION** — `functionrelationallabel` has **no production consumer**; the change
  only adds a fallback emission path inside the dormant unit and *reuses* (does not modify) `formatRomanNumeral` /
  `region::diatonicDegreeForRootPc` / the analysisutils primitives. The existing production tonicization paths
  (`tonicizationlabeler`, `chordsymbolformatter`) are byte-identical (`git diff` empty). Corpus regen not run — consistent
  with the Step-1..5 dormant-no-production-reach precedent (snapshot no-refresh proves chord-output identity).
- **Commit:** **`c86bb276fa`** `fix(function): L5 emit V7/IV — broaden the applied trigger to the ♭7̂ applied dominant (Phase 5c Step-5 correction, dormant)`.

---
# PART B — Step 6: output assembly (§7), dormant

## B1 — INVESTIGATE-confirm (read-only, all GREEN — no STOP)
Confirmed at source that the per-unit outputs of Steps 1–5 are assemblable into the §7 contract — every §7 field has a
producing unit:

| §7 field | Source unit (Step) | Type / member |
|---|---|---|
| Roman numeral (degree+alteration+quality+inversion + relational label, full DCML, no simplification) | functionrelationallabel (Step 5), wrapping functionromannumeral (Step 1) | `RelationalLabel.label` (the base numeral for role None, the relational label otherwise — base RN + relational label already combined) |
| function confidence — §5.2 cadence-vote weight | functioncadence (Step 2) | `FunctionalCadence.tonicVote` |
| function confidence — §5.0 licensed-progression fit | functionprogression (Step 1) | `isLicensedProgression(from, to)` (a boolean fit) |
| function confidence — margin to next-best | functionresolver (Step 3) | `ResolvedReading.functionConfidence` |
| open mark (genuinely undecided) | functionresolver (Step 3) | `ResolvedReading.openMark` |
| local key (possibly modulated) | functionmodulation (Step 4) | `ModulationDecision { tonicPc, minorMode, isModulation }` |
| cadence markers (type, location, salience) | functioncadence (Step 2) | `FunctionalCadence { type, approachTick, arrivalTick, tonicVote, … }` |
| committed identity (additive over L4) | the L4 decoder's committed chord | `ChordIdentity` (carried into each unit) |

**Verdict:** the assembly is a faithful marshal of existing outputs + the confidence combination; no field forced a
re-derivation; the only reuse is the Step-1 `isLicensedProgression` predicate for the licensed-fit component. No STOP.

## B2 — BUILD the L5 output assembly (§7), dormant
One new dormant unit **`function/functionoutput.{h,cpp}`** (namespace `mu::composing::analysis`).

**Output types (the L5→L6 contract).**
- `FunctionConfidence` — the **three FIXED components** (`cadenceVoteWeight`, `licensedProgressionFit`, `nextBestMargin`) +
  `combined` (the default-weighted sum; the **combining weights are precision-phase**, the components fixed).
- `FunctionAnalysisUnit` — per unit: `romanNumeral` (the full DCML numeral), `relationalRole`, `confidence`, `openMark`,
  and **`committedIdentity`** (the L4 chord, carried **verbatim** — additive, NOT replaced).
- `FunctionRegionMarkers` — per region: `localTonicPc` / `localMinorMode` / `modulated` (the local key, possibly changed by
  a confirmed §5.4 modulation) + `cadences` (the §5.2 markers, carried verbatim).
- `FunctionLayerOutput` — `{ units, region }`: the per-unit numerals + the region markers = the **L5→L6 contract**.

**`assembleFunctionOutput(units, cadences, modulations, homeTonicPc, homeMinorMode, params)`** — pure assembly:
- **Roman numeral** = `relational.label` (base RN + relational label already combined upstream by `classifyRelationalLabel`)
  — **no simplification, no second formatter**.
- **function confidence**, per unit, the three §7 components combined at default weights:
  - `cadenceVoteWeight` = the **tonic-vote of the cadence anchoring the unit** — the cadence whose **arrival** falls in the
    unit's span `[startTick, endTick)` (max vote if several; 0 if none) — a deterministic spatial attribution;
  - `licensedProgressionFit` = `isLicensedProgression(prevCommitted.chord, this.chord) ? 1 : 0` — the §5.0 motion **into**
    the unit, read through the **Step-1 predicate** (reuse, a boolean fit — no new score); 0 for the region's first
    committed unit (no preceding harmony);
  - `nextBestMargin` = the resolver's `functionConfidence`;
  - `combined` = `wCadenceVote·… + wLicensedFit·… + wNextBestMargin·…` (all default 1.0).
- **open mark** = the resolver's `openMark` (the numeral is still carried to display — the mark names what is unresolved,
  it does not erase the displayed numeral).
- **local key** = the **first confirmed §5.4 modulation**'s key (a region carries one local key — the unit between
  modulations), else the **home key**; a non-modulation §5.3 decision (a tonicization) leaves the home key (the break-even
  defaults to tonicization). `cadences` carried verbatim.
- **ADDITIVE over L4**: `committedIdentity` is copied verbatim into each unit — the assembly annotates, it never overwrites
  the L4 decision.

**The L5→L6 contract is this output** (the Roman numeral + cadence/key markers + any open mark). **The T/S/D derived
read-out is NOT built** (§9-D1 — deferred; the output is the Roman numeral, the three-role summary is a later
accessibility-display read-out).

## B3 — Constants
The **function-confidence combination weights** (`FunctionOutputParams`, all 1.0) are **default seeds** (firewall — the
combining weights are precision-phase). The **components are fixed** by §7. Only the direction is fixed (each component
non-negative; more evidence never lowers `combined`). No tuning.

## B4 — Tests (oracle-asserted, +8, all green)
`functionoutput_tests.cpp` (8 tests):
- **`ResolvedUnitCarriesNumeralAndConfidence`** — a `V→I` region: the tonic unit carries `"I"`, `openMark=false`, the
  three components (cadence-vote 3.0 / licensed-fit 1.0 / margin 1.0) and `combined=5.0`; the first unit's licensed-fit is
  0 (no predecessor).
- **`LicensedFitZeroForUnlicensedMotion`** — an ascending-fifth `C→G` (not in §5.0's licensed set) → fit 0.0.
- **`UndecidedUnitCarriesOpenMark`** — an abstained slice the resolver could not decide → `openMark=true` **and** the
  numeral still carried to display.
- **`RegionCarriesHomeKeyAndCadencesWithoutModulation`** — no modulation → local key = home key, `modulated=false`; the
  cadence markers (type/arrival) carried verbatim; region start/end ticks spanned.
- **`RegionLocalKeyReflectsConfirmedModulation`** — a confirmed §5.4 modulation → local key = the new key, `modulated=true`.
- **`RegionNonModulationDecisionKeepsHomeKey`** — a §5.3 tonicization (`isModulation=false`) → home key holds.
- **`AdditiveOverLayer4CommittedIdentityPreserved`** — the L4 committed root+quality carried **verbatim** alongside the L5
  numeral (the additive-over-L4 contract).
- **`CadenceVoteAttributedToArrivalUnitOnly`** — the cadence vote lands on the **arrival** unit only.

## B5 — Gate (dormant + byte-identical — no movement, no STOP)
- **composing 961 → 969 (+8** FunctionOutput).
- **notation 53** (4 skipped baseline).
- **pipeline_snapshot 11/11 — NO golden refresh** (chord output byte-identical).
- **corpus 53/24/53 unchanged BY CONSTRUCTION** — `functionoutput` has **no production consumer**: a grep of `src/` +
  `tools/` finds the new identifiers (`functionoutput`, `assembleFunctionOutput`, `FunctionLayerOutput`,
  `FunctionAnalysisUnit`, `FunctionConfidence`, `FunctionUnitAssembly`, `FunctionRegionMarkers`) **only** in the module,
  its test, and the two `CMakeLists.txt`. No scoring/gate/template/region/bridge code touched. Corpus regen not run
  (the Step-1..5 dormant precedent; snapshot no-refresh proves chord-output identity).
- **Commit:** **`217a875bf9`** `feat(function): L5 output assembly (Phase 5c Step 6, dormant)`.

## §7b — Declared build-detail decisions (Cowork review)
- **A-D1** — the unified emitter **reuses the production `formatRomanNumeral` for the V7/IV string only**, **not** the
  production inline path's *unguarded trigger*. The unguarded path over-emits on the diatonic minor-key `VII7→III`; §5.6
  (corrected) still requires chromaticism, so the ♭7̂-chromatic guard is kept and only the string emission is reused.
- **A-D2** — **`viio/IV` left as a still-open divergence** (the labeler drops it, the inline path emits it). Out of Part A's
  ♭7̂-DOMINANT scope; §5.6 names only the raised-LT and ♭7̂ dominant cases. Ruling requested (see A2).
- **B-D1** — **cadence-vote attribution by tick**: the §5.2 cadence-vote component of a unit is the tonic-vote of the
  cadence whose **arrival** falls in the unit's span (max if several). A deterministic spatial rule, not a judgment.
- **B-D2** — **licensed-fit reuses the Step-1 predicate** over the nearest preceding **committed** chord (the §5.0 "into"
  motion); 0 for the first committed unit. No new score; a boolean fit.
- **B-D3** — **local key = the first confirmed §5.4 modulation's key**, else the home key. A region carries one local key
  (the unit between modulations); a non-modulation §5.3 decision leaves the home key (break-even tonicizes).
- **B-D4** — **the assembly is producer-agnostic / hand-injectable** (the Step-2..5 precedent): it reads only the already-
  built value types (`RelationalLabel`, `FunctionalCadence`, `ModulationDecision`, `ProgressionChord`, `ChordIdentity`),
  never a decoder/region/engraving type, so it is exercised by hand-built inputs.
- **B-D5** — **the T/S/D read-out is correctly ABSENT** (§9-D1). The output is the Roman numeral; the three-role summary is
  a later accessibility-display read-out, not part of the analysis.

## Status
**Steps 0–6 of `cowork_phase5c_l5_build_plan.md` COMPLETE** (progression model + base RN + cadence detector + resolver +
the §8 forward-override + tonicization-vs-modulation + the modulation recompute + the two §15-3 pins + the relational
labels + the unified tonicization emitter [now emitting `V7/IV`] + the §7 output assembly — all dormant / byte-identical).
**Next: Step M — the read-only measure + the engage GO/NO-GO** (run the full dormant L1→L5 spine over the corpus,
coverage-matched RN accuracy + correct-abstention, the class-(b) hard-stop projection — *not* an accuracy chase).
