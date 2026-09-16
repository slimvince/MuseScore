# CC Instruction — Phase 5c Step M: the read-only measure + the engage GO/NO-GO (L5, NO production movement)

> **A MEASUREMENT, not an accuracy chase, not an engage.** L5 is built dormant (Steps 0–6 + the A-D2 follow-up), byte-
> identical by construction. Step M answers one question: **if we engaged L5, what would change against the DCML ground
> truth, per case, signed — and does it pass the two-tier BIR gate?** You **measure and recommend**; Cowork verifies and
> the user ratifies the engage. **Do NOT engage, do NOT switch production, do NOT retire any legacy path, do NOT tune any
> constant, do NOT fix any inference.** Spec: `cowork_layer5_function_design.md` (the §7 output is what you measure); gate
> policy: `CLAUDE.md` (the two-tier BIR — class-(b) hard stop, class-(a) tracked). **Reuse the existing corpus tooling, do
> not re-implement. Proportionality.** *(Reminder: the never-bash rule is Cowork's — you run the corpus tools.)*

## §0 — Preamble (sweep + STATUS)
Commit local-only any unstaged Cowork docs (the §5.6 amendment already rode with `9bd60a063b`; commit anything else
pending) and add a STATUS.md session entry opening Step M. Report the shas.

## §1 — INVESTIGATE-confirm BEFORE measuring (read-only — the harness must not become a production consumer)
Confirm and report:
- **A diagnostic path can invoke the dormant L5 output assembly (`assembleFunctionOutput`, §7) over a score and dump its
  would-be labels** (the Roman numeral + cadence/key markers + open marks, per unit/region) to a side file — **without**
  any production path reading it (the pattern of the existing `batch_analyze --section-level` diagnostic flag: default
  OFF, offline, no production consumer). If the only way to run L5 over the corpus is to wire it into production → **STOP
  and report** (that would be engage, not measure).
- **The existing RN-comparison + corpus tooling is reusable** for the diff: `compare_rn` (the RN equivalence/credit logic),
  `dcml_parser.py` (the oracle-correct ground-truth roots), `characterise_bir_false.py` (the two-tier BIR characterizer),
  `run_bach_preset.py` (the per-preset regen). Confirm the would-be L5 labels can be fed through `compare_rn` against the
  DCML ground truth the same way production labels are. If a new comparator must be written, say so (prefer reuse).
Report the harness plan + the reuse map. If a measurement needs structure beyond a diagnostic-only path → **STOP.**

## §2 — BUILD the measurement harness (diagnostic-only, default OFF, NO production consumer)
- A diagnostic flag/tool that runs the dormant L5 (`assembleFunctionOutput`) over a score and writes the **would-be L5
  labels** to a side file — **not** wired into any production output path. Same discipline as `--section-level`: offline,
  default OFF, zero production consumer.
- **Gate this build itself:** corpus **53/24/53** unchanged, suites + snapshots green, no golden refresh — the harness
  reads the dormant units and writes a side file; it must not move production. Movement → STOP.

## §3 — MEASURE against DCML, all three presets (Baroque / Jazz / Default), per case, signed
For each preset, produce the **would-be engage delta**: diff the dormant-L5 would-be labels against the DCML ground truth
(via `compare_rn`), and report **per changed case** (stem@tick + the from→to label + the DCML truth + signed: improves /
regresses / neutral-rotation). Then **classify each changed case two-tier** (per `CLAUDE.md`):
- **class-(b) — functional/key regression:** a pitch-class-**decidable** root now read wrong (the gate's real intent —
  **must be non-increasing on every preset for GO**).
- **class-(a) — symmetric-rotation churn:** a pitch-class-**undecidable** sonority (symmetric dim7 / augmented / whole-tone
  / share-tone tetrad) — tracked, small wobble OK, **a large net increase trips mandatory investigation**.
- Default to class-(b) on any doubt; record case identities (stem@tick + sonority); verify class-(a) **at the score** per
  case, not by assertion.

## §4 — Resolve the deferred items AS MEASUREMENTS (not fixes)
Quantify each, read-only — report the numbers, do not change anything:
- **The two applied-label divergences** (`V7/III` on diatonic `bVII7→III`; `viio/III` on diatonic `ii°→III`): does the
  DCML ground truth agree with the **guard** (reject — diatonic numeral) or the legacy **inline path** (emit applied)?
  Per case, per preset. This is the engage-time reconciliation the §5.6 final bullet defers to here.
- **The Inherit class-(b) override coverage** (the 61 Commit / 25 Inherit split, Step 3): how many Inherit-class slices
  would the fine-grain override touch at engage, and with what signed effect against DCML?
- **The `kEstablishmentMinChords` modulation floor** (Step 4): its measured effect on the corpus (how many regions
  promote/stay, signed against DCML).
- **The pinned region-reduction content** and the **minor-key mixture scope:** their measured would-be effect, if any.

## §5 — PRODUCE the GO/NO-GO table
Per preset, a single table: the **class-(b) signed delta** (the GO criterion: ≤ 0, non-increasing), the **class-(a) signed
delta** (tracked; flag if a large net increase), the **net case-identity changes** (added/removed stem@ticks), and the
**applied-divergence verdicts** (DCML sided with guard / inline, per case). Then a one-line **recommendation**: GO (engage
passes the two-tier gate — zero new class-(b), class-(a) within small-wobble) or NO-GO (a class-(b) regression or a large
unexplained class-(a) increase — name the cases). **The recommendation is yours to state; the engage is the user's to
ratify.**

## §6 — Constants
- **No tuning, none** (firewall). Step M measures the dormant build at its default constants. If the measurement suggests a
  constant is mis-set, **record it for Phase B** — do not change it.

## §7 — Deliver
Commit **locally (unpushed)**: the diagnostic harness + any measurement scripts (no production movement). Write
`cc_phase5c_stepM_report.md` (gitignored): the §1 confirm + reuse map, the §2 harness, the §3 per-preset signed two-tier
deltas (with case identities), the §4 deferred-item measurements, the §5 GO/NO-GO table + recommendation, and the shas —
so Cowork verifies the harness is diagnostic-only (production byte-identical), the measurement is against DCML (not self-
graded), the two-tier classification is per-case-verified, and the GO/NO-GO follows the gate.

## §8 — Stops
- The measurement cannot be done without wiring L5 into production (that is engage) → STOP, report. A class-(b) regression
  appears on any preset → that is not a STOP for *measuring* (measure and report it), but it is a **NO-GO** for engage —
  surface it, do not engineer around it. Any production movement, any threshold **tuning**, any inference fix, retiring a
  legacy path, the engage switch itself → STOP (engage is Phase 5d, after Cowork verifies + the user ratifies). `upstream`
  → STOP.
