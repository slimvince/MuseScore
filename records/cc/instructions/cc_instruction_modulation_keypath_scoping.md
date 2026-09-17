# CC Instruction: local-modulation scoping — current key-path behavior, the gap, and the de-masking diagnostic

## Authorization + framing

The metric-check (`cc_tonicization_modulation_metric_dossier.md`) reframed the biggest precision slice:
**S1 (~17.7%) is 95.6% LOCAL-MODULATION detection — a Stage-4 KEY gap, not Stage-6 tonicization labeling.**
`compare_rn` scores by chord root, so it **already credits** our home-key `V/d` against DCML's local `V`
(partial) — which **masks** that we have the KEY wrong (we should have modulated). Before designing the
local-modulation detector, this run SCOPES it: characterize how the current key path handles modulation,
size the gap honestly (with a de-masking diagnostic), and locate the cleanest integration layer.

**READ-ONLY.** No production behavior change, no commit. The one tooling addition (Task A) is a
**reporting-only** sub-split of `compare_rn` that **does not change any metric number or category** — it
only adds a diagnostic breakdown. Prove the headline numbers are byte-identical after it. Tag every claim
`[probe]`/`[code]`/`[oracle]`. Deliverable: `cc_modulation_keypath_scoping_dossier.md`.

## Task A — build the de-masking diagnostic (reporting-only; the measurement instrument)

Add to `compare_rn` a diagnostic that **sub-splits the `partial` bucket by reference-key match**: of the
credited `partial` pairs, how many are "our key == DCML local key" (correctly-keyed) vs "our home-key label
credited against DCML's LOCAL key" (the masked modulation error — we stayed home, DCML modulated). **The
metric categories + rn_agree MUST be unchanged** (this is additive reporting, NOT a crediting change — the
crediting-harder option was rejected as harmful). Prove byte-identity of the existing headline numbers.
This instrument is what lets us measure the modulation detector by CORRECTNESS, not by the gameable rn_agree.

## Task B — characterize the current key-path modulation mechanism [code]

Read `keyresolver.cpp`, `sectionanalyzer.cpp` (KeyArea), `regionanalyzer.cpp`, the hysteresis margins
(`hysteresisMargin`, `relativeKeyHysteresisMargin`). Answer at source, quoting file:line:
- Does the resolver modulate (change key between regions) at all today? What governs whether it switches
  vs stays — the hysteresis margins, the declared-mode hint, lookahead window?
- Does KeyArea already group sustained same-key spans? Is there any "local key / modulation" concept, or is
  the key essentially global+hysteresis?
- **Why do we STAY HOME where DCML modulates?** Pin the mechanism (e.g. hysteresis too sticky, no
  local-key hypothesis, window too short to see the local cadence). This is the core diagnosis.

## Task C — size the gap + the realistic ceiling [probe][oracle]

Using Task A's diagnostic + the metric-check's ~95.6%-of-S1 local-modulation population: of those cases,
how many would a **"sustained span + local cadence confirmation → modulate to the local key"** rule
correctly capture (the lever's realistic ceiling), and how many are harder (ambiguous, brief, or
wrong-local-key)? Give the de-masked picture: what is our REAL key-axis correctness on S1 once the masking
is exposed (how inflated was the headline)?

## Task D — available signals + the integration LAYER (the audit-method question) [code]

What signals exist for the detector: the committed **cadence instrument** (local V→I confirmation), KeyArea
sustained spans, region durations, the resolver hysteresis. Are they sufficient for "sustained +
cadence-confirmed local key"? Then the layer question: **which layer should own the modulation decision** —
the key resolver, the section/KeyArea pass, or a new pass — and where does it plug in cleanly (state its
single responsibility; what it consumes; what it must NOT entangle). Confirm it is all composing-zone; flag
any off-limits need.

## Task E — behavior-change blast radius [probe]

Modulation detection changes the resolved key → changes RN labels + chord emission (`basisIndep`) + the BIR
gate. Estimate the blast radius: roughly how many region keys would change; the chord-axis gate (57/23/57)
risk; whether snapshots move. (No build — estimate from the gap population + how key feeds emission.)

## Deliverable — `cc_modulation_keypath_scoping_dossier.md`
The de-masking diagnostic (+ byte-identity proof of unchanged headline numbers); the current modulation
mechanism + the stay-home diagnosis; the gap size + realistic ceiling + the de-masked real correctness;
the available signals + the recommended integration layer/responsibility; the blast-radius estimate. This
feeds the local-modulation detector DESIGN (Cowork-written next, ratification-gated). Every number
`[probe]`, every root `[oracle]`. READ-ONLY — no production change, no commit.

## Stop conditions
- Task A changing any metric category/number (it is reporting-only — if a number moves, you changed
  crediting; STOP and revert).
- Drifting into BUILDING the modulation detector (this run scopes + diagnoses only).
- Needing an off-limits (`src/notation`/`src/engraving`) edit — surface it; scoping should be read-only.
- The "stay home" diagnosis being unclear from source — report the unknown explicitly (do not guess the
  mechanism); it is the load-bearing input to the design.
