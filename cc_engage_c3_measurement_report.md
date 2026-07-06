# Engage arc #2 — the C3 genuinely-coupled key↔chord population: FEASIBILITY VERDICT

> **Status: INVESTIGATION (CC, 2026-07-06). READ-ONLY — no `src/` change, no build, no telemetry,
> no corpus write, no θ retune.** Executes `cc_instruction_engage_c3_measurement.md` (engage arc #2).
> Principle-driven and principle-cited throughout (the ratified `CLAUDE.md ## Guiding principles`, 1–16).
> Provenance: this report + the design-doc §3.D-2 update.
>
> **Grounding rule honored (the binding constraint):** every claim is tagged — `[code]` = read at the
> named source symbol on live disk at HEAD `712830210a`; `[data]` = measured from the existing
> `C:/tmp/c1/fs_*` decode-chain dumps (no regen); `[flag]` = an inference the evidence does not support,
> called out as a gap. No step rests on an unverified assumption.

---

## §0 — Headline

**Task-1 verdict: VERDICT 3 — the C3 trigger is NOT computed anywhere; it is UN-COMPUTABLE read-only AND
un-surfaceable by additive default-off telemetry.** The binding blocker is C3 component **(b)** — "a
different carried KEY alternative flips the chord reading." The per-key chord re-decode that (b) requires is
**computed nowhere on any path**: it is precisely the **gated joint key-and-chord step that the contract
§6-C3 says is "still owed at Stage 5"** and the L3 decoder header names as the unbuilt "later, gated
key-and-chord step." Even the one mechanism that comes closest — the J-key-iii joint re-key pass
(`regionanalyzer.cpp`) — **explicitly leaves the chord unchanged** ("the chord-axis side-effect … is DEFERRED
to a faithful mechanism"). There is therefore **no already-computed signal to surface** (which is what
verdict 2 would require); surfacing (b) would mean **building** the joint step — forbidden by #6 (total
unification), #8 (no inference-problem-driven build), #7 (layers), and the dispatch's explicit STOP.

This is the load-bearing finding the dispatch anticipated: **§3.D-2 (C3-restrict) cannot be scoped as a
near-term F-B home** — it requires the owed joint-step machinery. Per the dispatch, verdict 3 is a
**report, not a build.**

**Consequence for the engage frame (Task 3):** the principled F-B endgame stands at **annotate-via-open-mark
everywhere** (§3.D-1 — honest carry, no correction, no information loss, #12/#6/#7). Recovering the 53
corrections becomes an **open inference-quality question — declared to Cowork, blocked by #8**, not built.

---

## §1 — The C3 trigger, restated in contract terms (what must be derivable)

The C3 joint-step trigger (`cowork_confidence_contract.md` §6-C3, verbatim): a slice where **(a)** the L3 key
confidence is **below its bar** AND **(b)** the L4 decision is **sensitive to the carried KEY alternatives —
a different carried key flips the chord reading.** `[code]`

Two things the dispatch is explicit about, and I hold to:
- **(b) is about carried KEY alternatives**, NOT F-B's chord-alternative pool (`s.alternatives`). The F-B
  dump's `alternatives[]` are **L4 chord alternatives** (different root/quality/bass under the *same* key);
  they are not key alternatives. Conflating them would be a category error the dispatch forbids. `[code]`
- The joint step's own design doc **is still owed at Stage 5** (contract §6-C3, last sentence) — i.e. the
  contract itself flags the mechanism as unbuilt. `[code]`

---

## §2 — Feasibility at the source + the fs_* dump schema (Task 1)

### §2.1 — The F-B measurement chain, at the source `[code]`

The 1043 F-B fires live on the **`--dump-fullspine` (E0) dormant decode chain**
([batch_analyze.cpp:3005-3186](tools/batch_analyze.cpp#L3005)). That chain, input by input:

| stage | source | what it produces on THIS chain |
|---|---|---|
| L3 key | `inferLocalKey(score, refStaff, …, Fraction(0,1), …)[0]` ([batch_analyze.cpp:3028](tools/batch_analyze.cpp#L3028)) | **ONE home key** at tick 0 → `homeFifths / homeMode / homeTonicPc / homeMinor` + `homeConf = homeKey.normalizedConfidence` ([:3034](tools/batch_analyze.cpp#L3034)) |
| L4 chord | `ChordSliceDecoder::decode(slices, model, homeFifths, homeMode, …)` ([:3046](tools/batch_analyze.cpp#L3046)) | **ONE decode** over the home key; per-slice `chosen` + ranked **chord** `alternatives` |
| L5 key track | `detectAndDecideModulations(...)` + `modulationRecompute(...)` ([:3134-3162](tools/batch_analyze.cpp#L3134)) | per-slice **committed** local key (`localTonic[i]/localMinor[i]`) = home ∪ confirmed modulation spans |
| L5 override | `resolveCarriedReadings(...)` → `attemptFineGrainOverride` ([:3186](tools/batch_analyze.cpp#L3186)) | the F-B fires |

**The E0 region schema** ([batch_analyze.cpp:3410-3469](tools/batch_analyze.cpp#L3410)) dumps per region:
`keyConfidence` (= `homeConf`, [:3421](tools/batch_analyze.cpp#L3421)), `localTonicPc/localMinor`, the L4
block (`l4Decision / l4RootPc / l4Composite / l4Margin / l4Sufficiency / l4Cleanliness`), `ambiguityKind`,
the L5 block (`l5OverrodeCommit / l5OverrideContradiction / l5Basis / …`), and `alternatives[]` — each a
**chord** candidate `{rootPitchClass, bassPitchClass, quality, bassIsRoot, extensions, extKnown, score}`
([:3457-3468](tools/batch_analyze.cpp#L3457)). `[code]`

### §2.2 — Component (a): L3 key confidence below its bar — NOT on this chain `[code]`

- **The declared L3 boundary confidence** is the **sequence margin** — `SliceKeyMode.confidence`
  ([keymodesequence.h:156](src/composing/analysis/key/keymodesequence.h#L156)) / `HarmonicRegion.keyConfidence`
  (contract §3 + delta **D-L3a**, both closed). Its **bar** (verified at source, per the "do not assume the
  value" rule): the sequence-margin's own abstention bar is `uncertainThreshold` **default 1.0**
  ([keymodesequence.h:141](src/composing/analysis/key/keymodesequence.h#L141)); the alternative "bar" often
  cited — `kAnnotateKeyConfidenceThreshold` **0.8** ([regionanalyzer.cpp:390](src/composing/analysis/region/regionanalyzer.cpp#L390))
  — gates the **demoted emission sigmoid** (`normalizedConfidence`), which D-L3a explicitly demoted OUT of
  the boundary role. So the bar is well-defined at source but attaches to the sequence margin, not the
  sigmoid. `[code]`
- **On the F-B (fullspine) chain there is NO per-slice sequence margin.** The chain never runs
  `KeyModeSequenceDecoder::decode`; it uses `inferLocalKey(...)[0]` (a single tick-0 key). The only
  key-confidence in the dump is `homeConf = homeKey.normalizedConfidence` — the **demoted emission sigmoid**,
  and it is **score-global** (byte-identical across every region of a score, [:3421](tools/batch_analyze.cpp#L3421)).
  Both wrong: wrong quantity (D-L3a-demoted sigmoid, not the boundary margin) **and** wrong granularity
  (score-scalar, so it cannot discriminate per-slice fires within a score). `[code]`
- This is exactly D-L3a's own note: *"the fullspine grouping dump `batch_analyze.cpp` … [has] no
  sequence-margin substrate on [its] path, so re-pointing would compute a non-existent value."* Surfacing (a)
  on this chain would require **running the sequence decoder** there — a new computation on this path, not the
  surfacing of an already-computed value. `[code]`

### §2.3 — Component (b): chord flips under a carried KEY alternative — computed NOWHERE `[code]`

(b) requires two things, neither present:

**(i) Carried KEY alternatives at the slice.** A ranked key-alternative list exists **only** as
`SliceKeyMode.alternatives` ([keymodesequence.h:155](src/composing/analysis/key/keymodesequence.h#L155)) on
the L3 `--decode-keymode` diagnostic path, and as `HarmonicRegion.keyAlternatives` on the production region
path. **Neither is on the F-B fullspine chain**, which carries only home key ∪ committed modulation spans
(one committed key per slice, no ranked per-slice key alternatives). `[code]`

**(ii) The chord reading re-decoded under each key alternative.** This is the decisive gap. The L4 decoder
**takes exactly one key** ("this increment takes one key" —
[chordslicedecoder.h:133](src/composing/analysis/chord/chordslicedecoder.h#L133); the key is a *diatonic
prior*, [:130](src/composing/analysis/chord/chordslicedecoder.h#L130)) and is called **once** over the home
key ([batch_analyze.cpp:3046](tools/batch_analyze.cpp#L3046)). **No path re-decodes the chord under an
alternative key.** Concretely:
  - The chord *is* key-dependent in principle (the diatonic prior tips close readings; for symmetric
    sonorities the rotation is key-dependent, G4/C1). So a different key *could* flip the winner — but nothing
    computes that counterfactual. `[code]`
  - The **gated joint key-and-chord step** — the mechanism that *would* re-decode the chord under the carried
    key alternatives — is explicitly **UNBUILT**: *"The genuinely ambiguous residual (relative pair,
    modulation seam) … [is] left for the later, gated key-and-chord step — never forced"*
    ([keymodesequence.h:70-72](src/composing/analysis/key/keymodesequence.h#L70)); *"the joint step's own
    design doc is still owed at Stage 5"* (contract §6-C3). `[code]`
  - **The closest existing mechanism confirms the gap by omission.** The J-key-iii **joint re-key pass**
    (`applyJointKeyWiring`, default OFF) re-keys regions jointly — and **deliberately does not touch the
    chord**: *"The CHORD is left as the production chord R0 (NOT re-emitted): a faithful per-region chord
    re-emission under the joint key cannot reproduce the multi-pass pipeline chord … so the chord-axis
    side-effect … is DEFERRED to a faithful mechanism. The key axis alone therefore moves; BIR/chord output is
    byte-identical to production"* ([regionanalyzer.cpp:369-375](src/composing/analysis/region/regionanalyzer.cpp#L369)).
    So even the one place a joint key exists, the key↔chord **coupling** — the exact quantity (b) needs — is
    an explicit, named deferral. `[code]`

**Therefore (b) is not an already-computed signal.** Surfacing it via additive telemetry (verdict 2) is
impossible **because there is no computed value to surface**; producing it means **building** the per-key
chord re-decode — the owed joint step — which the dispatch, #6, #7, and #8 forbid.

### §2.4 — The three-way feasibility verdict

| verdict | applies? | why |
|---|---|---|
| **1 — read-only measurable** | ✗ | neither (a) nor (b) is in the fs_* dumps as the required per-slice quantity |
| **2 — minimal additive telemetry** | ✗ | telemetry may only *surface an already-computed* signal (the `bothLicensed`/`phraseNumVoices` precedent). (b)'s per-key chord-flip is computed **nowhere**; (a)'s per-slice sequence margin is not computed **on this chain** — neither is an existing quantity awaiting a dump field |
| **3 — trigger NOT computed anywhere → STOP-and-report** | ✅ | (b) = the unbuilt gated joint step; even J-key-iii defers the chord axis by name. A load-bearing finding: C3-restrict needs the owed joint machinery |

**VERDICT 3.** `[code]`

---

## §3 — The population footing + what CAN and CANNOT be measured (Task 2)

Because the C3 trigger is un-computable, the C3-qualifying **count** and its **corr/harm/neutral split
within the 1043 fires cannot be measured** — this is the reported un-computable finding, not a number. What I
*did* establish, read-only, to keep the footing honest:

### §3.1 — The 1043-fire population reproduced exactly `[data]`

Joined per `theta_fit.collect_fb_fires` over the existing `C:/tmp/c1/fs_baroque/*.ours.json`:
**1043 fires = 53 corrections + 809 harms + 181 neutral** — reproduced to the unit (matches
`fb_taxonomy_out.txt` / the design-doc §2 population). `[data]`

### §3.2 — The complement (= the whole population, since C3 cannot be carved out) `[data]`

With C3 un-isolable, the entire 1043-fire population *is* the measured whole (no C3 subset can be removed).
The dispatch's expected complement signature is **confirmed**: the fourth/fifth "progression-tidying" harm
majority holds — root moves of **5 semitones (↑4th/↓5th) + 7 semitones (↑5th/↓4th) = 576 of 1043 fires (55 %)
and 472 of 809 harms (58 %)**, harm rate 78.8 % and 85.7 % respectively (design-doc §2.2, `fb_taxonomy_out.txt`).
The whole population is 77.6 % harm, 5.1 % correction. `[data]`

### §3.3 — Bar-sensitivity — handled without assumption, but moot for C3 `[code]`

The dispatch asked that if the "bar" is range-dependent, the split be reported across the plausible range.
I verified the two candidate bars at source (§2.2: sequence-margin `uncertainThreshold` 1.0; annotate-gate
0.8). **The bar is not the binding constraint** — component (b) is un-computable regardless of any bar value,
so no bar-sweep of a C3 split is possible or meaningful. Recorded so the verdict does not rest on an
unverified bar assumption. `[code]`

### §3.4 — Reproducibility-hygiene finding: the fs_* manifest stamp is STALE `[data]` `[flag]`

While stamping the measurement (#16), I found a provenance defect worth surfacing (it does **not** affect the
structural verdict, which is source-grounded at HEAD):
- `C:/tmp/c1/fs_baroque/corpus_manifest.json` self-reports `git_hash: d1d4d3d7f0` (a Jul-3 commit; 51
  commits and real analysis-code drift *before* the pinned `c50002fee1`, Jul-5) and file mtime Jul-4 11:18.
- The **actual dumps** (`bwv10.7.ours.json`) have mtime **Jul-6 07:16** and sha256 **`85a44730…`** ≠ the
  manifest-recorded **`4281c8fc…`**. So the fs-regen driver re-dumped fullspine on Jul-6 (HEAD ≥ `c50002fee1`)
  **without rewriting the manifest** — the manifest git_hash + sha fingerprints are a stale Jul-4 leftover.
- `theta_fit.py` (and the taxonomy scripts) **glob `*.ours.json` directly and never call
  `validate_corpus_dir`** (grep: 0 hits), so the 1043 measurement reads the real Jul-6 content — consistent
  with the design-doc's `c50002fee1` attribution. But any consumer that *did* run the standard staleness
  guard against this dir would (correctly) reject it as fingerprint-mismatched. **Flag to Cowork:** the E0
  `fs_*` dirs should carry a manifest refreshed by the fullspine driver, or the taxonomy scripts should
  validate — otherwise the #16 corpus-hash stamp on F-B/θ/C3 measurements is unverifiable at the dir.
  `[data]` `[flag]`

---

## §4 — Verdict + decision surface (Task 3)

### §4.1 — Does C3 close the surprise? (#3 discharge)

The engage-arc surprise (from the F-B design pass): **the progression contradiction is uncorrelated with
root-correctness; the theory-first repair is net-negative.** The C3 measurement was the specific-research
move (#5/#2) to test whether the override is net-positive on the coupled minority for which its correction
job is theory-defined.

**C3 cannot itself close the surprise by isolating a net-positive subpopulation — because C3 is
un-computable.** But the verdict-3 finding **explains the surprise structurally**, which *is* a #3 discharge:

> F-B fires on **any committed slice with a tidier progression** (design §2.2), i.e. its fire condition is a
> vertical-commit ∪ a ≥2-feature progression contradiction — a population with **no key↔chord-coupling
> gate**. The C3 minority — the *only* population for which the contract theory-justifies a key-coupled chord
> correction — is **not where F-B fires, and cannot be**, because the gate that would restrict it (the joint
> re-decode) does not exist. So the override was **mis-scoped by construction**: it applies a coupled-key
> correction rule to a population that was never filtered for coupling. That the correction is uncorrelated
> with correctness is the *expected* consequence of firing off-population, not a residual mystery.

Per #3/#1: the surprise signals an **incomplete fact/theory basis** — specifically, F-B was wired to fire
**before its theory-home (the joint step) was buildable**. The fix is not a tune; it is to stop asserting a
coupled correction the machinery cannot yet target. **No residual surprise remains** at the design level: the
one open item — recovering the 53 corrections — is a *declared* inference-quality question (needs a
correctness-correlated contradiction signal), not an unexplained result.

### §4.2 — The annotate(±C3) decision surface for the build event

- **§3.D-2 (C3-restrict) is NOT a viable near-term F-B home.** [verdict 3] It requires the owed joint
  key-and-chord step (design doc + build), which is out of scope and gated by #8. It remains the *correct
  long-run home* for the class-(b) coupled-correction job, but only *after* the joint step exists — it is a
  Stage-5+ successor, not an engage-arc option.
- **The frame therefore stands at §3.D-1 — annotate-via-open-mark EVERYWHERE** (honest carry, #12 no
  information loss; #6 reuse the existing open-mark carry; #7 the L5 layer surfaces contradiction as
  uncertainty, never overturns a committed L4 fact it cannot out-decide). Ties the disable floor on accuracy
  (corr−harm 0) while preserving all 1043 contradiction signals as calibrated uncertainty — the very signal a
  future joint step would consume.
- **Recovering the 53 corrections is an open inference-quality question — DECLARED to Cowork, blocked by
  #8** (no inference-problem-driven coding until all methods live in their correct layer). It needs a
  correctness-correlated contradiction signal, which is an inference-fixing job, not this arc's.

### §4.3 — What the eventual build event would touch (no build here — #10 doc-sync map)

The annotate-everywhere build event (the user's separately-ratified event, #14) would touch:
- `src/composing/analysis/function/functionresolver.cpp` — `attemptFineGrainOverride` sets an **annotation**
  (reusing the existing open-mark carry) instead of `overrodeCommit = true` + `prog[i].chord` mutation +
  `forwardRecompute`.
- `ResolvedReading` ([functionresolver.h:166](src/composing/analysis/function/functionresolver.h#L166)) — an
  additive `functionContextContradiction` advisory flag (keeps reading = the L4 commit).
- `cowork_confidence_contract.md` §4 — Frame F-B **re-declared as an annotation channel** (mandatory:
  an undeclared/retired cross-layer comparison must be recorded).
- `cowork_layer5_function_design.md` §5.5 / §10 / §15-2 — the §15-2 "θ accounts for the missing progression
  term" premise struck as refuted; §10's class-(b) correction job **re-homed to C3, gated on the joint step**.
- `docs/scoring_model.md` — synced per the CLAUDE.md sync rule wherever the L5 override post-pass is
  documented.
- **Acceptance gate:** the robust-unit stop (class-(b) root-disagree DURATION non-increase per preset, via
  `a8_rebaseline_measure.py` → `robust_stop_diff.py`) + the batch 52/24/52 secondary. **Dormant today ⟹
  identity-PASS by construction; at engage the redesign must move the robust stop favorably** (removing the
  809 harms — ~776/809 non-symmetric, pitch-class-decidable = class-(b) — reduces class-(b) duration).

**No build in this pass** (#8; the dispatch moratorium boundary). This report characterizes the C3
feasibility at the source and hands the decision surface up; the build event is the user's ratified event.

---

## §5 — Acceptance checklist (this pass)

- ✅ **C3 feasibility verdict stated** — VERDICT 3 (un-computable; not read-only, not surfaceable by
  additive telemetry), source-grounded at (b) = the unbuilt joint step + J-key-iii's named chord-axis
  deferral.
- ✅ **C3-qualifying count + corr/harm/neutral split** — reported as the **un-computable finding** (cannot
  be measured; the joint re-decode is not computed anywhere), per the dispatch's verdict-3 branch.
- ✅ **Complement measured** — the whole 1043-fire population (C3 un-isolable): 53/809/181; fourth/fifth
  harm majority **confirmed** (472/809 = 58 % of harms).
- ✅ **Bar-sensitivity handled without assumption** — both candidate bars verified at source (1.0 / 0.8);
  the bar is not the binding constraint (b is).
- ✅ **Verdict on C3 as a correction home** — not a near-term home; frame stands at annotate-everywhere;
  §3.D-2 is a post-joint-step successor.
- ✅ **#3 surprise-closure** — discharged: the override was mis-scoped off the C3 population by
  construction; no residual surprise; 53-recovery = declared inference question (#8).
- ✅ **No behavior change / no telemetry / no golden refresh** — zero `src/` touched; both stops green **by
  construction** (byte-identical to HEAD `712830210a`, at which STATUS session 22x/23 recorded batch 52/24/52
  set-diff empty + robust sandwich identity-PASS; no analysis code changed ⟹ both inherit the green state; no
  re-measurement was run because there is nothing to perturb).
- ✅ **Reproducibility finding surfaced** — the fs_* manifest stamp is stale (§3.4), flagged to Cowork.
- ➡️ **Fold + push** — design §3.D-2 + STATUS + HANDOFF + fitter O-18 + the CLAUDE.md principles edit + this
  report + the instruction; `git push origin master` (fork-only; `cfc7eb5e39` upstream HARD STOP honored).

*CC, 2026-07-06. Engage arc #2. Investigation (measurement-first), principle-driven: #3/#5/#2 opened it,
#12/#6/#7 fix the eventual frame (annotate-everywhere), #8 bounds it (verdict 3 = report, not build). On this
report: Cowork verifies at objects → presents the annotate(±C3) build-event decision surface to the user.*
