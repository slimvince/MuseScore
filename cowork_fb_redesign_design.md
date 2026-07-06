# The F-B fine-grain override REDESIGN — design / scoping (engage arc #1)

> **Status: DESIGN + DECISION SURFACE (CC, 2026-07-06). READ-ONLY pass — no `src/` change, no scoring
> value, no corpus write, no build, no θ retune.** First increment of the engage arc (Stage-5 CLOSED at
> R10-b / O-16). The implementation is a **separately-ratified build event** (the user's next event); this
> doc characterizes the mechanism at the code, decomposes its measured net-harm, lays out redesign options
> with projected splits, and states the build-event decision surface. Provenance report:
> `cc_engage_fb_redesign_design_report.md`.
>
> **Grounding rule honored (the user's binding constraint):** every claim about F-B's behavior below is
> tagged to its source — `[code]` = read at the named source symbol; `[data]` = measured from the existing
> `C:/tmp/c1/fs_*` decode-chain dumps (no regen); `[flag]` = an inference the data does NOT support, called
> out as a gap rather than assumed.

---

## §1 — F-B characterized at the source (Task 1)

### §1.1 What F-B is, as built

**The override site is `attemptFineGrainOverride(...)`** in
[functionresolver.cpp:381](src/composing/analysis/function/functionresolver.cpp#L381), invoked from
`resolveCarriedReadings` **Phase 2** ([functionresolver.cpp:529](src/composing/analysis/function/functionresolver.cpp#L529))
after every abstain is base-resolved. It is the §5.5 case-4 / §8 channel-#2 "fine-grain chord override".
`[code]`

**DORMANCY (verified at source).** `resolveCarriedReadings` has **no production consumer**. Its only
callers are: the module's unit tests, and `tools/batch_analyze.cpp` line 3186 inside the **`--dump-fullspine`
(E0) diagnostic harness** — production `.ours.json` is byte-identical without that flag
([batch_analyze.cpp:3186](tools/batch_analyze.cpp), header note
[functionresolver.h:77](src/composing/analysis/function/functionresolver.h#L77)). So every measurement in
§2 is on the **dormant decode chain** — the forward-looking view of what F-B *would* do at engage; the
production pipeline and both regression stops do not run it today. `[code]`

### §1.2 The frame, input by input (source symbols)

The override is a single instance of the generic §8 primitive
[`OnePassClosure::tryOverride`](src/composing/analysis/function/forwardoverride.cpp#L58) with rule
`overrides()` → `contradictionStrength > baseBar + confidenceScale · clamp(earlierConfidence,0,1)`
([forwardoverride.cpp:26-44](src/composing/analysis/function/forwardoverride.cpp#L26)). Frame F-B binds its
two arguments as follows:

| Frame F-B element | Source symbol | As-built definition | Dump field |
|---|---|---|---|
| **Incumbent** `earlierConfidence` | `s.confidence.composite` ([functionresolver.cpp:468](src/composing/analysis/function/functionresolver.cpp#L468)) | `SliceConfidence.composite = min(marginCertainty, sufficiency, cleanliness)` — **all three VERTICAL**: margin = chosen cell's vertical score − best-different vertical score; sufficiency = present/required template tones; cleanliness = membership cleanliness ([chordslicedecoder.h:404-408, 120-121](src/composing/analysis/chord/chordslicedecoder.h#L404)). Already ∈ [0,1]. **Vertical-fit-only is code-truth.** | `l4Composite` |
| **Contradiction** `contradictionStrength` | `bestPlaus − committedPlaus` ([functionresolver.cpp:450](src/composing/analysis/function/functionresolver.cpp#L450)) | Both from `plausibility()` = `wLicensedOut·[licensed out of prev] + wLicensedIn·[licensed into next] + wCadentialFit·[root gets a cadence tonic-vote]` ([functionresolver.cpp:90-107](src/composing/analysis/function/functionresolver.cpp#L90)); weights all default **1.0** ([functionresolver.h:211-213](src/composing/analysis/function/functionresolver.h#L211)) ⟹ `plausibility ∈ {0,1,2,3}`, an **integer count of 3 satisfied progression/cadence features**. | `l5OverrideContradiction` |
| **θ (the bar)** | `params.override` = `{baseBar=1.0, confidenceScale=1.0}` ([forwardoverride.h:80-83](src/composing/analysis/function/forwardoverride.h#L80)) | bar = `1.0 + 1.0·composite` ∈ **[1.0, 2.0]**. | — |
| **Selection pool** | `pool = s.alternatives ∪ {region[prevIdx].chosen, region[nextIdx].chosen}` ([functionresolver.cpp:424-430](src/composing/analysis/function/functionresolver.cpp#L424)) | carried L4 alternatives + the nearest committed neighbour before + the established-next committed harmony; the most-plausible `c` with `!sameRootQuality(c, committed)` wins. Carried **verbatim** (`r.reading = bestAlt`), never re-derived. | `alternatives[]` |
| **Fire gate** | `tryOverride(i, composite, contradictionStrength, params.override)` ([functionresolver.cpp:468](src/composing/analysis/function/functionresolver.cpp#L468)) | one-pass closure keyed by slice `i`; on fire: `prog[i].chord = toPC(bestAlt)` + localized forward recompute of downstream abstains ([functionresolver.cpp:490-497](src/composing/analysis/function/functionresolver.cpp#L490)). | `l5OverrodeCommit` |

### §1.3 The coarseness, read off the arithmetic `[code]`

Because `plausibility ∈ {0,1,2,3}` and a prior gate requires `contradictionStrength > 0`
([functionresolver.cpp:451](src/composing/analysis/function/functionresolver.cpp#L451)), the only firing
contradiction values are **2 or 3** (a value of 1 can never beat `baseBar = 1.0`). The bar tops out at 2.0.
So the override **fires whenever a pool member beats the committed reading by ≥ 2 progression features** —
and does so at ≥ 2 essentially unconditionally once composite < 1.0. The confidence bar is almost inert: the
contradiction quantity's granularity (steps of 1.0) is *coarser than the entire dynamic range of the bar*
(1.0). This is the mechanical form of D-FS's "the contradiction quantity is too coarse {2,3} and the
incumbent band too high." `[code]` + `[data]` (observed S range exactly {2,3}, §2.1).

### §1.4 Contract ↔ code check (drift finding)

The code **faithfully implements** the declared Frame F-B (`cowork_confidence_contract.md` §4): incumbent =
L4 vertical-fit composite; contradiction = licensed-progression + cadential fit of the contradicting
context; selection restricted to carried alternatives / neighbouring committed harmony; never re-derivation.
**No implementation drift.** `[code]`

**The one finding is a premise-invalidation, not an implementation drift.** The contract's *declared
rationale* — §4 F-B and the code comment at
[functionresolver.cpp:461-462](src/composing/analysis/function/functionresolver.cpp#L461): *"vertical-fit-only
… which the frame's θ accounts for (L5 §15-2)"* — asserts that a fitted θ can compensate for the incumbent's
missing progression term. **Phase 3 and the §2 stratification refute that premise at the data**: no θ
(the only lever being to scale the bar by the L4 composite `C`) separates corrections from harms, because
correctness is uncorrelated with both `C` and the contradiction `S` (§2.2–§2.4). The premise "θ accounts for
the missing progression term" is empirically false. This is already recorded as D-FS / the Phase-3
inference-quality finding; this doc grounds *why* at the code and the stratified data.

---

## §2 — The net-harm decomposed structurally (Task 2)

**Measured population** `[data]`: the 1043 GT-aligned F-B fires from `C:/tmp/c1/fs_baroque` (E0 dormant
chain, DCML root GT, preset-invariant — the override lives on the decode chain), joined exactly as
`theta_fit.collect_fb_fires` does (reproduces the ledger's **1043 fires = 53 corrections + 809 harms + 181
neutral** to the unit). Outcome labels (from `theta_fit.py`, unchanged): **correction** = L4-committed root
was wrong (non-symmetric) and the override made it right; **harm** = L4-committed root was **right** and the
override made it wrong; **neutral** = everything else. **~77.6 % of all fires are harms; ~78 % of fires move
an L4-correct root to a wrong one.**

### §2.1 Test of the documented root-cause hypothesis — CONFIRMED `[data]`

*Hypothesis (§1.4 / D-FS): harm is concentrated where the L4-committed root is vertically strong but the
progression-aware contradiction wins anyway.* The stratification confirms it and sharpens it into a stronger
statement — **the harm rate is ~uniform across every measurable stratum**, so there is no "safe" region:

| stratum | slices | harm % | reading |
|---|---|---|---|
| **contradiction `S`=2** | 888 | 77.9 % | the "stronger" contradiction (`S`=3, 155 fires) is **75.5 %** harm — *no more corrective than `S`=2* ⟹ S carries no discriminative signal |
| **incumbent `C` 0.70–0.80** | 601 | 80.7 % | the bulk of fires sit at high L4 confidence and are **more** harmful there |
| **incumbent `C` 0.90–1.00** | 52 | **80.8 %** | at the **highest** L4 vertical confidence the override is **most** harmful — scaling the bar by `C` (the only θ lever) pushes the wrong way |
| **incumbent `C` 0.50–0.60** | 172 | **71.5 %** | at the **lowest** confidence the override is *least* harmful — the bar-by-C direction is anti-corrective |

The incumbent-confidence band and the contradiction value are **both** flat against correctness. Because the
override's *only* tunable knob is `bar = baseBar + confidenceScale·C`, and harm does not fall as `C` falls,
**no θ can carve corrections from harms** — the code-grounded proof of Phase 3's "best measurable θ disables
it" (theta_fit: the corr−harm-maximizing measurable bar drops fires to 0 at corr−harm 0, vs −571 on the
fitting split at the current bar). `[data]`

### §2.2 The mechanism of the harm — fourth/fifth "progression tidying" `[data]`

Decomposed by the root move (final root − L4 root, semitones):

| move (semitones) | fires | harms | harm % | note |
|---|---|---|---|---|
| **7 (↑5th / ↓4th)** | 265 | 227 | **85.7 %** | the single worst and second-largest driver |
| **5 (↑4th / ↓5th)** | 311 | 245 | 78.8 % | the largest driver |
| 8, 9, 3, 2, 4 | 78–106 each | — | 67–83 % | |
| 1 (semitone) | 10 | 4 | 40.0 % | smallest harm % but n=10, 1 correction |

**Fourth/fifth root moves = 576 of 1043 fires (55 %) and 472 of 809 harms (58 %).** This is exactly what
`plausibility` rewards: `isLicensedProgression` scores V→I, ii→V, and other dominant/subdominant motions —
all fourth/fifth root relations. The override preferentially selects a fourth/fifth-related pool member
because that maximizes the progression score, and those picks are ~82 % vertically wrong. The harm is the
progression score doing its job — tidying the *functional* story — at the expense of the *vertical* fact L4
already had right.

### §2.3 The discriminator search — there is NONE on the available signal `[data]`

Cross-tabulated outcome × {final quality, `l5Basis`, `S`, `C`-band, symmetric, move-interval,
vertical-competitiveness gap}. **Every stratum is net-negative (corr − harm < 0).** The most-favorable
sub-populations:

- vertical-competitiveness gap `g ≤ 0` (the selected alternative is vertically **≥** the committed reading,
  §2.4): 26 corr / 189 harm ⟹ corr−harm **−163**;
- root move = 1 semitone: 1 corr / 4 harm;
- final quality Diminished: 0 corr / 6 harm.

There is **no feature, and no combination of the measured features, that isolates a region where corrections
meet or exceed harms.** The 53 corrections are diffuse (largest single bucket: Major/move-3 n=9; Minor/move-4
n=8 — relative/parallel-third corrections), scattered under the 809 harms with the same feature signatures.
A structural gate cannot separate them because the separating information is not in these features.

### §2.4 The incumbent-repair premise, tested directly — REFUTED `[data]`

The documented root-cause blames the *asymmetry* (vertical incumbent vs progression contradiction). The
natural repair is to make the comparison vertically fair: only override when the selected alternative is
itself vertically competitive. **Measured, it does not work.** Each carried alternative dumps its own L4
vertical `score`; classifying the selected reading and banding the vertical gap `committed_score −
selected_score`:

| vertical gap band | fires | corr | harm | harm % |
|---|---|---|---|---|
| `g ≤ 0` (selected vertically **≥** committed) | 267 | 26 | 189 | **70.8 %** |
| 0–0.25 | 309 | 10 | 249 | 80.6 % |
| 0.25–0.5 | 244 | 9 | 193 | 79.1 % |
| 0.5–1.0 | 190 | 2 | 152 | 80.0 % |
| > 1.0 | 14 | 0 | 14 | 100 % |

Even in the **vertically-fair** band (`g ≤ 0` — the alternative is at least as vertically supported as the
committed reading) the override is still **70.8 %** harm (corr−harm −163). So repairing the vertical
asymmetry does **not** reach net-positive: the problem is not merely that the incumbent lacks a progression
term; it is that the progression contradiction is **uncorrelated with root-correctness** at these committed
slices. L4's vertical commit is a far better predictor of the DCML root than F-B's progression re-pick, even
when the alternative is vertically its equal. `[data]`
*(Caveat `[flag]`: `committed_score` uses the first carried alternative on the L4 root as a proxy for the
committed reading's own vertical score; the gap banding is therefore heuristic. The robust conclusion — no
band drops below ~71 % harm — does not depend on the proxy's precision.)*

### §2.5 What the data CANNOT tell us — flagged, not assumed `[flag]`

- **Carried-alt vs neighbour selection is not a dumped field.** `l5Basis` is uniformly `FineGrainOverride`
  for all 1043 fires. Inferring the source by matching the final `(root, quality)` to the carried
  `alternatives[]` gives **1042/1043 = carried alternative, 1 neighbour-only** — so in practice F-B is
  *carried-alternative-only* — but this is a heuristic match, not a first-class basis field. Flagged: a
  redesign that keys on "was this a neighbour import" needs an additive dump field to measure.
- **The C3 joint-step population is not measurable here.** Whether a slice is a "genuinely-coupled key↔chord"
  case (contract §6 C3: L3 key confidence below bar AND chord sensitive to the carried key alternative) is
  not in the dump. The re-frame-C3 option (§3) is therefore proposed with an **UNKNOWN** projected split —
  it needs a new measurement, not an assumption.
- **These are decode-chain (E0) numbers, not production.** F-B is dormant; the production pipeline and both
  regression stops do not run it. The 1043/53/809 is the engage-time forecast, not a current production fact.

---

## §3 — Redesign OPTIONS (Task 3)

Each option is a *design proposal*, not built. Projected splits are from the §2 measured taxonomy; the
evidentiary basis and any `[flag]` are stated. The **floor any redesign must beat is corr−harm 0** — because
disabling already achieves it (§3.A).

### §3.A — (baseline) DISABLE F-B — the reference floor
- **Layer / frame:** remove the Phase-2 override call (or set the bar unreachably high); the confidence
  contract retires Frame F-B (§4 row struck / marked "retired — measured net-harmful").
- **Theory basis:** none needed — it is the measured optimum. Phase 3 already found the best measurable θ ≈
  disables (theta_fit corr−harm 0 vs current −571 fit).
- **Projected split `[data]`:** removes all 809 harms at the cost of all 53 corrections ⟹ **corr−harm 0**,
  a **+756 net-correct-root** recovery vs the as-built override on the GT-aligned decode-chain unit.
- **Blast radius:** dormant ⟹ **byte-identical on production today**; at engage, removes a net-harmful pass.
  Touches `functionresolver.cpp` (delete/guard the call) + the contract §4 F-B row + the L5 §5.5/§10 spec.
- **Surprise/risk:** minimal. The only loss is 53 diffuse corrections that no gate can recover selectively.

### §3.B — (gate) a tighter STRUCTURAL fire condition
- **Layer / frame:** L5 §5.5 — add an entry condition on `attemptFineGrainOverride` (e.g. restrict by chord
  type, move interval, or require `g ≤ 0`).
- **Theory basis:** exclude the harm sub-population identified in §2.
- **Projected split `[data]`:** **degenerates to disable.** §2.3 shows every measurable stratum is
  net-negative; the best structural carve (`g ≤ 0`) is still corr−harm **−163**. A gate on the available
  features can only *approach* the disable floor by excluding almost everything — it cannot beat it, and any
  gate that retains fires retains a net-negative population. A gate helps **only if it consumes a signal not
  currently measured** (which is §3.C or §3.D).
- **Blast radius:** small (one entry condition) but the measured payoff is ≤ 0 vs disable.
- **Surprise/risk:** medium — looks principled, delivers ≈ disable at best, worse if mis-tuned. **Not
  recommended as a standalone.**

### §3.C — (incumbent repair) give the L4 incumbent its missing progression term
- **Layer / frame:** the L4 composite (contract §3 L4 row) gains a progression component so the θ-comparison
  is vertically-and-progressionally symmetric — repairing the L5 §15-2 premise directly.
- **Theory basis:** the theory-first option — it targets the *declared* root cause (asymmetric comparison).
- **Projected split `[data]`:** **REFUTED by §2.4.** Restricting to the vertically-fair band (`g ≤ 0`, the
  measurable proxy for a symmetric comparison) still yields corr−harm **−163**. Making the comparison fair
  does not reach net-positive because the contradiction signal is uncorrelated with correctness. Projected
  best ≈ −163, strictly worse than disable's 0.
- **Blast radius:** **large** — adds a progression term to the L4 composite, touching the decoder, the
  confidence contract §3 L4 row (its "vertical-fit-only by construction" declaration), and every consumer of
  the L4 composite (including the fitted Class-P L4 map).
- **Surprise/risk:** high — large surface, and the data says the premise it repairs is not the binding
  constraint. **Not recommended.**

### §3.D — (re-frame) two theory-aligned alternatives to *overriding*

**§3.D-1 — demote F-B from OVERRIDE to ANNOTATION (carry honestly, §8 case 3).** Instead of overturning the
L4 commit, F-B *flags* the slice "functional-context contradiction" and **carries the L4 reading unchanged**
(an open-mark / advisory, not a re-commit).
- **Theory basis:** §8's own case 3 ("earlier layer uncertain, later evidence still cannot decide → carry
  honestly") — and here L4 is *not* even uncertain (it committed), so silently overturning it is the wrong
  case. Surfacing the contradiction as *uncertainty* is architecture-aligned.
- **Projected split `[data]`:** 0 harms, 0 corrections on the root decision ⟹ **corr−harm 0** (ties the
  disable floor on accuracy) **while preserving the 1043 contradiction signals** as calibrated uncertainty
  (the diagnostic value disable throws away).
- **Blast radius:** small — change the fire *action* from mutate-and-recompute to annotate; F-B stays
  dormant. Contract §4 F-B re-declared as an annotation channel, not an override frame.
- **Surprise/risk:** low. The best accuracy-plus-information option; recommended as the redesign target (see
  §4).

**§3.D-2 — restrict F-B to the C3 genuinely-coupled key↔chord minority.** Fire only where the contract §6-C3
joint-step trigger holds (L3 key confidence below bar AND the chord flips under a carried key alternative) —
a small, well-targeted population, not "any committed slice with a tidier progression."
- **Theory basis:** the contract already *defines* this trigger as the home of coupled key/chord correction
  (C3); F-B's §10 class-(b) "functional/key regression" job belongs there.
- **Projected split:** ~~UNKNOWN~~ → **UN-COMPUTABLE (engage arc #2 measured, 2026-07-06;
  `cc_engage_c3_measurement_report.md`).** The C3 trigger is **not computed anywhere** — VERDICT 3 (not
  read-only measurable, not surfaceable by additive default-off telemetry). The binding blocker is component
  **(b)** ("a different carried KEY alternative flips the chord reading"): the per-key chord re-decode it
  requires **is the gated joint key-and-chord step the contract §6-C3 says is "still owed at Stage 5"**
  ([keymodesequence.h:70-72](src/composing/analysis/key/keymodesequence.h#L70)), and even the closest
  mechanism — the J-key-iii joint re-key pass — **explicitly leaves the chord unchanged** ("the chord-axis
  side-effect … is DEFERRED to a faithful mechanism", [regionanalyzer.cpp:369-375](src/composing/analysis/region/regionanalyzer.cpp#L369)).
  Component (a) is likewise absent from the F-B fullspine chain (which uses `inferLocalKey(...)[0]` + a
  score-global `homeConf` sigmoid, not the per-slice L3 sequence margin; D-L3a's "no sequence-margin
  substrate on that path"). Surfacing (b) would mean **building** the joint step (forbidden by #6/#7/#8) —
  there is no already-computed signal to dump. `[code]` `[flag]`
- **Blast radius:** ~~medium~~ → **large / deferred** — C3-restrict is **gated on the still-owed joint-step
  design + build**; it cannot be scoped as a near-term F-B home. It remains the correct *long-run* home for
  the class-(b) coupled-correction job, but only **after** the joint step exists (a Stage-5+ successor, not
  an engage-arc option).
- **Surprise/risk:** the payoff is **unmeasurable until the joint step is built** — not merely unmeasured. A
  build-time measurement gate is mandatory *and presupposes* the joint machinery.

**Consequence for §4.** With §3.D-2 removed from the near-term option set (un-computable, joint-step-gated),
the recommendation collapses to **§3.D-1 (annotate-via-open-mark) EVERYWHERE**, floored by §3.A (disable) —
no C3 carve-out is available to keep the corrective fires selectively. Recovering the 53 corrections is an
**inference-quality question declared to Cowork (#8), not a redesign this arc can deliver.** The engage
surprise (progression contradiction uncorrelated with correctness) is *explained*: F-B fires on any
committed-slice-with-a-tidier-progression, a population **never filtered for key↔chord coupling** — so it is
mis-scoped off the C3 minority by construction, which is exactly why correctness is uncorrelated with the
contradiction.

---

## §4 — Recommendation + the build-event decision surface (Task 4)

### §4.1 CC's evidence-based recommendation
**Adopt §3.D-1 (demote to annotation) as the redesign, with §3.A (disable the override action) as its
accuracy-equivalent floor; reject §3.B and §3.C as measured net-negative.** Rationale, all `[data]`-grounded:
1. The override is net-harmful by **−756** and **no θ retune** repairs it (§2.1) — this is settled, not a
   tuning question.
2. **No structural gate** on the available features beats disable (§2.3, §3.B).
3. The **incumbent-repair premise is refuted** — a vertically-fair comparison is still 70.8 % harm (§2.4,
   §3.C), so the large-surface fix does not pay.
4. Disable and annotate **tie on accuracy** (corr−harm 0); **annotate strictly dominates disable** by
   preserving the 1043 contradiction signals as uncertainty (the §8 case-3 honest-carry), which is the
   information a future C3 joint step (§3.D-2) will need.
5. §3.D-2 (C3 restriction) is the correct **long-run home** for the correction job but is **unmeasurable
   today** — record it as the follow-on, gated on a new measurement, not adopted now.

**The 53 corrections are a genuine loss** — but they are diffuse class-(b)/relative-third fixes that *no
selective mechanism on the current signal can keep without importing 15× their number in harms*. Recovering
them is a job for a **correctness-correlated contradiction signal** (a new inference quality), which is an
inference-fixing question — **declared to Cowork, out of this design pass's scope.**

### §4.2 What the implementing dispatch would touch
- **`src/composing/analysis/function/functionresolver.cpp`** — the §3.D-1 change: `attemptFineGrainOverride`
  sets an annotation (a new `ResolvedReading` advisory flag) instead of `overrodeCommit = true` +
  `prog[i].chord` mutation + `forwardRecompute`. (Or, for the §3.A floor, guard the Phase-2 call.)
- **`ResolvedReading`** ([functionresolver.h:166](src/composing/analysis/function/functionresolver.h#L166)) —
  a `functionContextContradiction` advisory field if §3.D-1 (additive; keeps the reading = the L4 commit).
- **`cowork_confidence_contract.md` §4** — re-declare / retire Frame F-B (mandatory: "an undeclared
  cross-layer comparison is a contract violation"; a retired/re-framed one must be recorded here).
- **`cowork_layer5_function_design.md` §5.5 / §10 / §15-2** — the §15-2 "θ accounts for the missing
  progression term" premise struck as refuted; §10's class-(b) correction job re-homed to C3 (§3.D-2).
- **`docs/scoring_model.md`** — synced per the CLAUDE.md sync rule wherever the L5 override post-pass is
  documented (the build event confirms the exact section).
- **`docs/implementation_roadmap.md` / `cowork_stage5_fitter_design.md`** — the engage-arc observation
  (O-17) updated to "F-B redesign adopted".

### §4.3 The acceptance gate (the robust-unit stop)
The governing hard stop is **the class-(b) (pitch-class-decidable-root) root-disagree DURATION,
non-increasing per preset**, measured via the successor sandwich (`a8_rebaseline_measure.py` →
`robust_stop_diff.py`), plus the batch 52/24/52 case-identity set as the retained secondary.
- **Today, F-B is dormant** ⟹ any §3.A/§3.D-1 change is **byte-identical on production**, so both stops stay
  green by construction; the build event's sandwich is an identity-PASS.
- **At engage (Phase 5d / E3),** when F-B becomes load-bearing, the redesign must **move the robust-unit stop
  favorably** relative to an F-B-enabled-as-built variant — i.e. removing F-B's 809 harms should **reduce**
  class-(b) root-disagree duration (the harms are ~non-symmetric, pitch-class-decidable roots, so they are
  class-(b) by construction — §2.3 shows 776/809 harms non-symmetric). A redesign that *recovers* F-B's harm
  is the intended direction of the stop, not merely a non-increase.

### §4.4 The moratorium boundary (explicit)
This is architecture/scaffolding design (moratorium-clear). The build event (§3.A or §3.D-1) is
refactoring-driven — it removes/re-frames a measured-harmful override, not an inference tune. **Recovering
the 53 lost corrections** by inventing a correctness-correlated contradiction signal **is** inference-fixing
and is **out of scope** — declared to Cowork as the follow-on question, not built here.

---

## Appendix A — measured tables (reproducible, read-only)

Source: `C:/tmp/c1/fs_baroque/*.ours.json` (E0 dump, corpus `c50002fee1`), joined per
`theta_fit.collect_fb_fires`. Scripts (scratchpad, read-only orchestration over existing dump fields — the
sanctioned "no pinned tool modified" path): `fb_taxonomy.py`, `fb_vertical.py`. Reproduces **1043 = 53 corr +
809 harm + 181 neutral** exactly.

- Outcome × contradiction `S`: `S`=2 → 44/692/152 (n 888); `S`=3 → 9/117/29 (n 155).
- Outcome × incumbent `C`: 0.50–0.60 → 21/123/28; 0.60–0.70 → 9/126/34; 0.70–0.80 → 19/485/97; 0.80–0.90 →
  2/33/14; 0.90–1.00 → 2/42/8. *(corr/harm/neutral)*
- Outcome × move-interval and × final-quality: see §2.2 / §2.3.
- Outcome × vertical gap: see §2.4.
- Selection source (heuristic): carried-alt 53/808/181 (n 1042); neighbour-only 0/1/0 (n 1).

## Appendix B — grounding sources
- Code: `functionresolver.cpp/.h`, `forwardoverride.cpp/.h`, `chordslicedecoder.h`, `batch_analyze.cpp:3186`.
- Contract: `cowork_confidence_contract.md` §3 (L3/L4/L5 rows), §4 (F-A/F-B frames), §5 (R4–R6), §7 (D-FS).
- Measurement: `cc_stage5_phase3_report.md` §2 (Task C); `tools/theta_fit.py`;
  `tools/fit_ledgers/stage5_theta_candidates.jsonl`; `C:/tmp/c1/{theta.json,theta.txt}`; the `fs_*` dumps.
