# L1–L5 Premise-Debt Audit — the Retroactive #17 Ledger for Built Code

> **Cowork, 2026-07-10 (session 36).** Commissioned by the user immediately after ratifying
> CLAUDE.md #17–#19: *"have we in L1–L5 already built anything on assumptions (or broken any
> other rule) that will not show its ugly head until we really start to do the final parts of
> inference?"* **Answer: YES — three tiers.** This audit is the retroactive premise ledger #17
> implies for already-built code. **Read-only fact-finding (explorational, surprise-permitted
> scope); no code changed.** Method: two parallel sweeps — (1) documentation/provenance
> (`docs/scoring_model.md`, `tools/param_manifest.json`, `cowork_stage5_fitter_design.md`,
> phase reports), (2) code (`src/composing/` inference path). The two most load-bearing Tier-1
> claims were re-verified at source by Cowork directly (#15).

## Tier 1 — ARMED TRAPS: built code carrying premises already measured FALSE, live at engage

These are the highest-severity items because they are the *same premise family the F-B
measurement discredited*, sitting on the E4/L5 engagement path. Dormancy is the only guard.

**T1-1 — The dormant L5 resolver selects progression-FIRST (the discredited channel), at
confidence 1.0.** ✅ Cowork-verified at code: every `resolveAbstained` arm consults
`isLicensedProgression` first and returns `pick(..., ResolutionBasis::Progression, 1.0)`
(`functionresolver.cpp:221-225` TransitionVsContinuation, `:242-246` ShareTone, plus
RelativePair/CloseReading/SymmetricRotation per the sweep, `:154-348`); the soft bass-degree
prior (`:199-213`, confidence 0.25 inline) is reached only when progression fails to separate.
The F-B measurement established progression contradiction is **uncorrelated with
root-correctness** on committed slices (`cowork_fb_redesign_design.md` §2.2–§2.4), and arc #9
designed the demotion (progression = tie-break only, `cowork_layer5_engagement_design.md`
§4/§3) — but the demotion is **design-only; the built ordering is unchanged.** Engaging L5
as-built repeats the F-B mistake at selection time.

**T1-2 — `attemptFineGrainOverride` runs UNCONDITIONALLY on the engagement path.**
✅ Cowork-verified at code: Phase 2 of `resolveCarriedReadings` invokes it for every slice with
no flag guard (`functionresolver.cpp:529-531`); it mutates the progression and fires
`forwardRecompute` (`:490-497`). Measured **net-harmful −756** (1043 fires / 53 corr / 809
harm); the arc-#11 demotion to annotation is design-only. If L5 engages before the F-B wiring
lands, the −756-class harm goes live silently.

**T1-3 — Confidence-scale incommensurability at three comparison/combination sites, with one
calibration attempt already FAILED.** (a) `functionresolver.cpp:468` — L4 `composite` (Class-M,
[0,1], vertical-only) compared against an unbounded plausibility margin via `tryOverride`;
(b) `functionmodulation.cpp:136-137` — L3 squashed sequence-margin vs accumulated cadential
vote-weight; (c) `functionoutput.cpp:124-132` — three different-scale quantities summed with
placeholder weights 1.0 (`functionoutput.h:103-105`), squashed by unfitted `kBoundary=1.0`
(`:106-108`; header admits `combined` is unbounded, "observed to ~25 on the E0 spine"). Each
site's comment defers commensurability to "Stage-5 calibration" — but the premise *"fitting
θ/kBoundary can make these commensurable"* is itself an unverified Class-A premise, and the one
attempt so far — the L5 `combinedBoundary` calibration — **failed (non-monotone mid-range;
map deferred, fitter D-8).** This lands exactly where Stage 5 will stand.

**T1-4 — The decoder's symmetric-rotation root choice assumes the key prior is correct.** The
key enters the slice cube only via `diatonicRootBonus` 0.30 (`chordanalyzer.cpp:896-903`;
`analysistypes.h:191`) and the key-gated `kDim7CharacteristicBonus` 0.75
(`chordanalyzer.cpp:547-580`); the spelling-pin is the only guard and defers when spelling is
absent/contradicted (`chordslicedecoder.cpp:705`, `.h:86/269`). Premise: *key correct at
slice-decode time* — unverified; wrong key ⇒ wrong root, no fallback. Surfaces at E4 when the
decoder replaces the legacy path. (Related latent inconsistency: two chord-equality relations —
`sameChordVoicing` governs the alternatives cap, `sameChordSymbol` governs
confidence/openQuestion, `chordslicedecoder.cpp:74-82` — a #6-flavor trap for any consumer
assuming one meaning. The topK=6 **voicing** cap / missing distinct-root guarantee is already
named at arc #9 §2.3.)

## Tier 2 — the Class-B MASS: live constants tuned against instruments later proven broken

**Nearly every live scoring magnitude was hand-set in the Iter/B-era (pre-2026-06-13), and its
only validation instrument was the batch BIR gate + catalog/snapshot pins — the gate later
proven to under-count true per-onset root error ~15–56× and to sit on a then-buggy GT parser.**
Under #19 the validation basis of these values is retroactively void: they are *unfalsified,
not established*. The set (locations per `tools/param_manifest.json` + `docs/scoring_model.md`):

- **The four inversion bonuses** 0.50/0.50/0.45/0.40 Baroque (`analysistypes.h:226-252`) with
  the Jazz overrides 0.20/0.20/0.20/0.15 (`batch_analyze.cpp:3877-3880`).
- **The §6-block gate margins**: Gate I 0.45, Gate L 0.35 (`postscoringgates.cpp:52/54`), the
  bias margin 0.70, `kHalfDimFirstInversionBonus` 0.55 (`:287` — absent from scoring_model §6,
  self-reported doc-drift). CLAUDE.md's phrase "calibrated against the Baroque corpus" means
  **hand-set to pass cases scored by the broken instrument — no fit record exists.**
- **~25 chord-scorer bonus/penalty magnitudes** (kContradictionPenalty 0.75, kForeignPenalty
  0.45, bassNoteRootBonus 0.70, kWComplete 0.50, the sus4/dom7♭5/power-chord family, etc.).

**Containment status:** this tier is *self-declared* debt — `tools/param_manifest.json`
(61 tunable / 17 frozen, ratified P0 2026-07-04) is the project's own enumeration, and the
Stage-5 fitter is the payment plan. **Exactly ONE constant system-wide has ever been fit
against the established robust unit: kWStepIn 0.125 (2.2e, license-stamped).** Mitigating
measured evidence: Phase-1b found 24/59 reachable constants dead at the root objective
(|Δroot|<0.0005), and both high-leverage re-fit candidates regressed held-out (kPowerChord
0.6375 → −0.098 PARKED; bassNoteRootBonus 0.775 → held-out class-(b) regression) — the
hand values are not obviously bad, but their goodness is unestablished.

## Tier 3 — HOLES IN THE CONTAINMENT itself

**T3-1 — The declared fit surface is incomplete (#19 gap in the Stage-5 plan).** NOT in the
manifest: the L1/L2 beat-weight table, the emission sigmoid (midpoint 2.0 / steepness 1.5,
`analysistypes.h:758-759`, duplicated inline at `chordpostpasses.cpp:271`), segmenter
penalties, and the **live** L3 hysteresis margins (`keyresolver.cpp:312`, tagged
`[empirical]`). Stage 5 as scoped will declare precision complete while an unaudited constant
layer remains under it.

**T3-2 — The Jazz preset is unvalidatable, period (#9/#19).** No licensed jazz ground truth
exists (the A-7 "empirically-unvalidated" mark, fitter D-5); every Jazz override (including
extensionThreshold 0.12) is an untestable style guess. Until a jazz GT corpus is *established*
(#19), Jazz numbers carry no validation claim and Jazz robust-stop columns measure consistency,
not correctness.

**T3-3 — Placeholder constants on the dormant surface** (self-labeled, lower risk): the L5
firewall seeds wLicensedOut/In/CadentialFit = 1.0, decidingMargin 0.5
(`functionresolver.h:211-214`), θ baseBar/confidenceScale 1.0 (`forwardoverride.h:81-82`),
inline selection confidences 1.0/0.5/0.25 in `resolveAbstained`, the §15-13 commissioned
weight = null. Honest (declared "NOT tuned — Phase B"), but they become load-bearing the moment
L5 engages, and several are the Tier-1 mixing inputs.

**T3-4 — Doc-drift (#10, self-reported by the manifest):** scoring_model §4/§6 file/line
anchors stale post-refactor (constants now in `harmonicfunctionlayer.h`/`postscoringgates.cpp`);
`kHalfDimFirstInversionBonus` missing from §6 entirely.

## Consequences — the Stage-3 ENTRY GATE (proposed, folded into the arc plan)

1. **Tier-1 defusal becomes a PREREQUISITE of E4/L5 engagement, not an inventory item:** the
   resolver selection re-ordering (arc #9 design) and the F-B override demotion (arc #11
   design) must land — or the engagement wiring must provably bypass `resolveCarriedReadings`
   Phase 2 and the progression-first arms — **before** any L5 output can reach production.
   T1-3 additionally owes a #17 ledger + desk simulation before any θ/kBoundary fitting is
   attempted (the failed combinedBoundary calibration is the warning).
2. **The rebuilt-vs-legacy go/no-go measurement** (the biggest unmeasured precision claim)
   runs under full #17 (ledger, written predictions, desk simulation) and #19 (its instrument
   — e.g. the E0 decode chain — positively established first; no establishment record found).
3. **The pedal reader is gated on owed-P1 over an established pedal-dense corpus** (#18/#19):
   its load-bearing premise ("the material pedal need is usually already a carried
   distinct-root alternative") is currently *underpowered AND unfavorable* (agreement
   0.20/0.50/0.20 on n=2–5).
4. **Extend the manifest to the full constant surface** (L1/L2 + live-L3 items, T3-1) before
   Stage 5 is declared complete.
5. **Declare the Jazz preset's validation status honestly** (T3-2): unestablished pending a
   jazz GT corpus — a corpus-establishment work item, or an explicit de-scoping of Jazz
   correctness claims.
6. **Tier 2 retires through the existing fitter plan** — each Stage-5 fit against the robust
   unit converts a Class-B-suspect value to established (or pins a dead one as insensitive-at-
   objective, which is an establishment of a different kind). No new mechanism needed; the
   mechanism needs to *run*.
7. **Fix the doc-drift** (T3-4) at the next scoring_model touch (#10).

*Provenance: two read-only sweeps (docs + code), session 36; Tier-1 items T1-1/T1-2
Cowork-verified at `functionresolver.cpp` directly. Companion docs:
`cowork_premise_gate_reflection.md` (the ratified #17–#19), `cowork_engage_arc_plan.md`
(amended this session with the entry gate), `cowork_layer5_engagement_design.md` §9.2 (synced
this session), `tools/param_manifest.json`, `cowork_stage5_fitter_design.md`.*
