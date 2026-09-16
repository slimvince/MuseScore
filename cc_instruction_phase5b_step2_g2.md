# CC Instruction — Phase 5b Step 2: G2/G3 — three-tier membership ladder + plausibility fix

> **Why.** Step 2 of the grounded `cowork_phase5b_l4_build_plan.md`. Step 1 (`f21273ce3b`) built G1 and **closed the
> −15** (per-slice 58→77% among committed) — but at **~53% abstention**, partly because G1's **inherit is conservative
> (template-only)**. Step 2 builds the spec's **three-tier structure-first membership ladder (G2)** and **fixes the
> plausibility check (G3)** — which both corrects membership AND **completes inherit (the stepwise relaxation deferred
> from G1)**, so it should **convert many abstains into correct inherited chords** (raising coverage toward the
> coverage-matched engage comparison). **Algorithmic completion per spec — build-it-right, NOT inference-tuning.**
> Decoder still **production-dead → byte-identical on production.** *(Reminder: the never-bash rule is Cowork's.)*

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read the spec's membership rule (`cowork_layer4_chordsymbol_design.md` §5 step 3 — the three-tier ladder + the
implausibility/plausibility test) against the as-built `chordslicedecoder` flat weak-OR-stepwise membership. Confirm and
report:
- **The three tiers** map cleanly onto the decode loop's per-tone classification:
  (1) **stepwise-embellishing → NCT regardless of weight**;
  (2) **no stepwise neighbour → chord-tone extension regardless of weight**;
  (3) **one-sided → metric weight + prevailing chord decide**.
- **The plausibility check fix (G3):** Step 0 found it "tests the wrong tones." Identify exactly which tones it should
  test (per spec — the required/template tones, the C-vs-Cadd9 discriminator) vs what it tests now.
- **The inherit coupling:** confirm the membership ladder is what G1's inherit needs for its *stepwise relaxation* (so
  a slice that is the prevailing chord + a stepwise NCT now **inherits**, where G1 (template-only) **abstained**).
- If a tier or the plausibility fix can't map onto the as-built decode without a structural change beyond the decoder →
  **STOP and report** (a spec or decomposition question).

## §2 — BUILD G2/G3 (in `chordslicedecoder`, dormant)
- Replace the flat membership with the **three-tier ladder** (structure-first: stepwise → NCT; no-stepwise →
  chord-tone-extension; one-sided → weight + prevailing).
- **Fix the plausibility check** to test the correct (required/template) tones (G3).
- **Relax inherit** to use the new membership: inherit the prevailing chord through a thin slice whose extra notes are
  **stepwise NCTs** of it (not only exact template tones). Keep the one `analyzeChord` cube; decision logic only.

## §3 — RE-MEASURE (the assess checkpoint — report BOTH accuracy AND coverage)
Re-run the diagnostic new-vs-legacy comparison (Baroque + Default), reporting **before(G1)→after(G2)**:
- **among-committed chord-root accuracy** (should stay high / improve);
- **the abstain / coverage rate** (should **drop** — more correct inherits);
- and, if feasible, a **coverage-matched** number (accuracy at legacy's coverage, or the inherited-correctly rate) — the
  trend toward the Step-M engage question.

## §4 — Gate
- **Production byte-identical:** corpus **53/24/53**, both suites, snapshots **unchanged** (decoder production-dead).
  **Any production movement → STOP.**
- **New unit tests** (oracle-asserted): each tier (a stepwise NCT vs an extension chord-tone vs a one-sided weight
  decision), the plausibility discriminator (C vs Cadd9), and an inherit-via-stepwise-NCT case that G1 abstained on.
- Build green.

## §5 — ASSESS (does the sequence hold?)
- **Expected:** membership is correct per spec AND the **abstain rate drops materially** (fuller inherit) with
  among-committed accuracy holding. → proceed to Step 3 (confidence/open-question, G6).
- **If membership is right but abstention does NOT drop** (or accuracy drops) → **STOP and report** — assess whether
  inherit needs more (Layer-5 territory?), or the sequence/spec needs amendment. Do not push to Step 3 on a failed
  assessment.

## §6 — Deliver
Commit **locally (unpushed)**: the G2/G3 logic + unit tests (decoder + tests only). Write `cc_phase5b_step2_report.md`
(gitignored): the §1 confirm, the §2 build, the §3 re-measure (accuracy + **coverage/abstain** before→after), the §5
assessment, and the commit sha — so Cowork verifies by sha that only `chordslicedecoder.*` + tests changed, production
byte-identical.

## §7 — Stops
- A tier / plausibility fix needs a structural change beyond the decoder → STOP (spec/decomposition question).
- Any production movement → STOP (decoder leaked live).
- Abstention doesn't drop / accuracy regresses → STOP, report (amend).
- A push targets `upstream` → STOP.
