# CC Instruction: constrained-joint-inference architecture investigation (READ-ONLY, sizing)

## Authorization + framing

The back half is being re-grounded onto a **constrained joint inference** architecture (the full rationale
is `docs/architecture_joint_inference.md`): harmonic analysis as one joint decision over all evidence,
where **hard constraints** (decisive raw facts + unambiguous analyses) disqualify/pin and **soft scores**
(priors, weak hints, the global key path) rank the survivors. Before any build, this run **MEASURES the
numbers that right-size and confirm it** (per never-guess). The whole key-axis arc (4a–4d) is the evidence
that the *local* pipeline can't do this; this run sizes the *joint* replacement.

**READ-ONLY** — analysis + measurement on existing diagnostics + the committed evidence producers (oracle
candidates, cadence instrument, modulation detector) + DCML. No production change, no metric change, no
commit. A reporting-only diagnostic addition is allowed if needed; prove headline numbers byte-identical.
Tag every claim `[probe]`/`[code]`/`[oracle]`. Deliverable: `cc_joint_architecture_dossier.md`.

## Task 1 — Hard/soft evidence characterization [code]
Enumerate the evidence sources we already have or can cheaply derive (vertical sonority / chord candidates
from the oracle; cadence events; scale-collection consistency; the notated signature; bass; metric weight;
voice-leading; repetition). For each, classify it as a candidate **hard constraint** (decisive — disqualifies
or pins) vs a **soft score** (ranks), with the rationale. Be precise about what a hard constraint actually
asserts — remember a *sounding* note is not automatically a *chord tone* (suspensions/pedals), so hard
constraints are over **raw facts** + genuinely-unambiguous analyses, NOT over the soft chord-tone reading.

## Task 2 — The residual (the headline) [probe][oracle]
Apply the candidate hard constraints over the WiR-Bach corpus and measure, per position: how many positions
are **PINNED to a unique (chord, key)** by the hard constraints alone, vs how many remain **AMBIGUOUS**
(>1 live hypothesis). **The ambiguous count is the true scope of the joint problem** — it decides
full-joint vs scoped-joint vs two-pass. Report the distribution (pinned %, ambiguous %, and the ambiguity
*type* — chord-only ambiguous, key-only, jointly-coupled).

## Task 3 — Hard-constraint safety / calibration (the precondition) [oracle]
For the positions the candidate hard constraints PIN, how often is the pinned answer **wrong** per DCML? A
hard constraint that pins a wrong answer is a bug (the override-in-reverse failure). Report the
hard-constraint error rate per constraint; flag any constraint that mis-claims certainty (it must be
demoted to soft). This is the safety gate on the whole approach.

## Task 4 — Soft-resolvable vs irreducible floor [probe][oracle]
Of the AMBIGUOUS residual (Task 2): how much would soft/global evidence (the key path, priors, broader
context) plausibly resolve, and how much is **irreducible** (the same notes admit two valid DCML-defensible
readings — the §6 ceiling)? This split is the **A-vs-B input**: the soft-resolvable part is where the joint
*structure* pays; the irreducible-but-feature-shaped part is where a richer/learned **emission** (B) would
pay; the truly-ambiguous part is the ceiling no system reaches.

## Deliverable — `cc_joint_architecture_dossier.md`
The hard/soft characterization; the **residual sizing** (pinned vs ambiguous, by type); the
**hard-constraint safety** rates (the calibration gate); the soft-resolvable vs floor split.
**Recommendation, on the numbers:** small residual + safe constraints ⇒ a lighter scoped-joint / two-pass
suffices; large residual ⇒ the full joint decode is warranted; an unsafe hard constraint ⇒ which to demote.
Plus an honest read of where a learned emission would and would not help. Every number `[probe]`, every
root `[oracle]`. READ-ONLY — no build, no commit.

## Stop conditions
- Drifting into BUILDING the joint decoder (this run SIZES it; the design + build are separate, ratified steps).
- Treating a *sounding note* as a hard chord-tone constraint (it isn't — suspensions/pedals); if a candidate
  hard constraint is actually soft, that is a finding (Task 3), report it.
- Any production/metric change beyond a proven-neutral reporting diagnostic — surface it.
- Scope: WiR-Bach is the measured surface; state non-Bach as unmeasured (do not over-generalize the numbers).
