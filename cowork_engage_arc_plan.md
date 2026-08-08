# The Engage-Arc Path Forward — ratified, principle-grounded

> **RATIFIED by the user, 2026-07-07.** The standing reference for the order of work from here to the
> precision phase. It does not re-derive the fix details — those live in `cowork_structural_integrity_audit.md`
> (§3 fix-queue, §4 sequencing) and the roadmap (E4/R9, the §6-block dissolution). This document fixes the
> **order and the principle behind each step**, so the plan is checkable against the principles, not memory.

## The governing rule and the two placement rules

- **#8 sets the macro-shape:** no inference-problem-driven coding until ALL refactoring, architectural design,
  and algorithmic completion are done. Architecture first; precision last.
- **#6 (one path per concern, no duplicated effort) places the legacy tangles:** do not refactor code that is
  about to be retired and already has a clean replacement. The `results` cap→workaround tangle is legacy
  Layer-4 code whose clean-target is **already built in the dormant decoder** — so it is retired by the
  decoder engagement (E4), never a standalone throwaway refactor.
- **#7 (each concern owned by its proper layer) places the owner-decisions:** a fix whose correct owner is a
  layer still being designed waits for that design (e.g. quality-from-key's owner is a Layer-5 decision).

## The stages (in principle order)

**Stage 1 — PRE-Layer-5 refactoring. ★ DELIVERED 2026-07-07 (arc #7).** The portable unification wins that
stand alone (#8-first; restores #6/#7). **Landed byte-identical:** the fact-layer duplication cleanups (FQ-5:
beat-weight, emission-sigmoid, node-builder; S7 partial), the serialization/display cap-views (FQ-6,
byte-identical structural only — the cap-#2 value lift stays deferred to Stage 3), the key-decoder constant
sourcing (FQ-7/S8; S9 verified load-bearing and KEPT). **Reassigned to Stage 3 (E4) after code inspection:**
FQ-1 (the four "best different-root" scans are NOT one decision — legacy compares root-only, the decoder
root+quality; the legacy scans retire with the decoder, not a false pre-L5 unification) and FQ-3
(`findTemporalContext` is relocatable but E4-supersedes it — throwaway pre-L5, #6). Minor open: S7 full
single-sourcing (a dependency-profile call). **Execution discipline:** each is one revertible,
provenance-stamped
commit (#14), verified on the full output surface — winner AND alternatives (#15) — on the frozen corpus
(#9), docs + regression tests in step (#10/#11); byte-identical is the expectation, any output move gets the
explained re-baseline (#16), never a silent edit.

**Stage 2 — the Layer-5 engagement DESIGN (#8's architectural-design phase; read-only). ★ COMPLETE 2026-07-07
(arcs #9/#10/#11).** Built on established fact — the decoder's already-clean carry is the factual basis (#1) —
carrying the full graded distribution incl. ruled-out readings (#12, finding-by-exclusion). Decides the owners
the audit surfaced: quality-from-key (FQ-2), pedal detection's home, the confidence-scale fix (F-1/S19).
Grounded also by `cowork_functional_analysis_research_grounding.md`. **Delivered, structure-only, moratorium
held (no `src/`, no build, no corpus write, no constant fitted/tuned):**
- **arc #9 — the carry + selection architecture** (`cowork_layer5_engagement_design.md` Part 1 §1–§5): the
  distinct-root carry contract with the exclusion tail preserved (#12); selection-by-joint-consistency
  (bass/spelling/key-consistency load-bearing, progression demoted to a non-override tie-break).
- **arc #10 — the joint key-and-chord step.** The ratified contract for the coupled key↔chord decision, and for its
  SHELVING with the evidence that produced it, is `cowork_joint_key_chord_design.md` — D-376…D-379 — which this plan
  delegates to by name and does not restate. Its four entries sit in §1.1, §1.3, §2.2 and §3.1; the delegation names
  the document, and a document-level delegation reaches all of its sections (`CLAUDE.md` rule (h), the granularity
  clause). Content: the coupled key↔chord decision as a generalization of `decideJointKey`, B1–B4 owed build
  enumerated, owed measurements flagged. *(Delegation written 2026-08-03 on the user's direction, the OI-293 write
  list; the previous parenthetical naming was a citation, which rule (i) does not admit.)*
- **arc #11 — pedal detection's home + the F-B annotate mechanics** (`cowork_layer5_engagement_design.md` Part 2
  §6–§10; `cc_engage_l5_pedal_annotate_design_report.md`): pedal placed as a **reader over the carry** (the
  audit's clobber/re-scan/defensive-disable symptoms dissolved); F-B demoted to an **annotation on the unified
  open-mark** (reuse, not a parallel channel — the plain boolean shown semantically wrong for a confident-commit
  contradiction), the contradiction carried as calibrated uncertainty (#12), the trigger an annotation lever
  never an override.

**No Layer-5 engagement concern remains undesigned — Stage 3 (algorithmic completion / E4) is the user's to
open with nothing left undesigned.** The Stage-3 build inventory it inherits is enumerated at
`cowork_layer5_engagement_design.md` §9.2.

**Stage 3 — algorithmic completion: E4 (decoder engages) + the §6-block dissolution (OWED #2).** The
`results` tangle dies by construction as the decoder's governed carry replaces the substrate (FQ-4); the owed
migrations land (two-segmenters retirement, two-pitch-context collapse, tpc-reader fold, `function/` rename);
quality-from-key gets its one owner (FQ-2); the divergent legacy different-root scans retire (FQ-1, the
decoder's root+quality version is the clean one); `findTemporalContext` ownership moves here (FQ-3). Each a ratified behavior change (#14) proven on the full surface
(#15) under the robust-unit regression stop (#11), with the re-baseline discipline (#16).

**★ STAGE-3 ENTRY GATE (ratified 2026-07-10 with #17–#19; evidence `cowork_l1_l5_premise_debt_audit.md`).**
Before any E4/L5 engagement wiring can reach production:
- **(EG-1) Tier-1 defusal is a PREREQUISITE, not an inventory item:** the resolver selection re-ordering
  (arc #9 — the as-built `resolveAbstained` still selects progression-first at confidence 1.0, the channel
  F-B measured uncorrelated with correctness) and the F-B override demotion (arc #11 — `attemptFineGrainOverride`
  runs unconditionally in `resolveCarriedReadings` Phase 2, measured −756) must land, or the wiring must
  provably bypass both, **before** L5 output reaches production.
- **(EG-2) The rebuilt-vs-legacy go/no-go measurement runs under full #17** (premise ledger, written
  quantitative predictions, desk simulation over known failing cases) **and #19** (its instrument positively
  established first — no establishment record exists for the E0 decode chain).
- **(EG-3) The pedal reader is HARD-GATED on owed-P1 over an established pedal-dense corpus** (#18/#19): its
  load-bearing premise is currently underpowered AND unfavorable (agreement 0.20/0.50/0.20, n=2–5). No build
  before the premise is settled.
- **(EG-4) The confidence-scale commensurability premise (T1-3) owes a #17 ledger + desk simulation before
  any θ/kBoundary fitting** — the failed L5 `combinedBoundary` calibration (non-monotone, fitter D-8) is the
  standing warning that "fit will fix it" is unverified.
- **(EG-5) The fit surface is completed before Stage 5 is declared done:** extend `tools/param_manifest.json`
  to the L1/L2 constants (beat-weight table, emission sigmoid, segmenter penalties) and the live L3 hysteresis
  margins (T3-1).
- **(EG-6) The Jazz preset's validation status is declared honestly** (T3-2): unestablished pending an
  established jazz GT corpus (#9/#19) — a corpus-establishment work item or an explicit de-scoping.
- **(EG-7) DEPENDENCY-ORDERED AUDIT CERTIFICATION (added 2026-07-10, user-directed — OI-84):** an E4 step
  may not open until every layer it DEPENDS ON — not merely touches — has passed its exhaustive premise+fact
  audit (#18 at architecture scale: new construction may not carry load on unaudited foundations). The audit
  plan partitions the module by the retirement map (R1–R9): retiring code gets NO audit, only the #12
  interpretation-check at deletion (adjudication dossier A1); the SURVIVING stack is audited exhaustively per
  layer in dependency order (L1 → L2 → L3 → L4 → L5 + instruments), each a read-only session feeding that
  step's #17 ledger. End-state coverage: 100 % before it carries new load. First item: the L1/L2
  certification audit.
Tier-2 (the Class-B mass of pre-2026-06-13 hand-set constants, tuned against the later-proven-broken batch
gate) retires through the existing Stage-5 fitter — each robust-unit fit converts a suspect value to
established; no new mechanism, but the mechanism must run.

**★ MEASURE-BEFORE-BUILD (ratified 2026-07-07, arc #12 lesson) — since 2026-07-10 the MIDDLE stage of the
#17 Premise-Gate funnel: desk-simulate (hours) → read-only probe (a session) → build (an arc).** Every
Stage-3+ item additionally owes a #17 premise ledger (FACT/THEORY/ASSUMPTION), a written quantitative
prediction per assumption, and a desk simulation over known failing cases BEFORE its probe or build is opened
(see CLAUDE.md #17–#19 + `cowork_premise_gate_reflection.md`). Byte-identical structural refactors are exempt
from the prediction requirement — byte-identity IS their prediction. A build whose case rests on an *anticipated*
precision gain is measured read-only **before** it is built, exactly as the joint step was. **The joint key↔chord
step is SHELVED — measured NOT to pay** (arc #12: net +0.05–0.16 pp over ~6200 regions, harm 75–90 % of
correction, oracle ceiling +0.6 pp, coupled-minority net ~0, fire-rate only 1.4 % — the carried alternative
keys are diatonic-collection siblings so the chord is almost always key-stable). It **drops off the Stage-3
build inventory.** The #12 reconciliation (no loss): the key alternatives ARE carried (the key discovery is not
discarded); the chord under an alternative key is **never computed** in this path (so nothing computed is
discarded), and the measurement shows the ~1.4 % where it would differ is 50/50 noise — choosing not to compute
a *measured-worthless* possibility is an evidence-based decision, not information loss. **Distinction:** this
gate applies to **precision claims** ("will building X make analysis more correct?" — measure first); the
**structural refactors** (decoder-replaces-tangle, the migrations) are justified by cleanliness and verified
**byte-identical**, no precision measurement owed. **The biggest unmeasured precision claim, to measure next:**
does the rebuilt path (decoder carry + the intended selection) beat the LEGACY path against the DCML ground
truth? — the go/no-go on the whole engagement, before E4 is built.

> **★ Dated annotation (user ruling, 2026-08-02, at the D-278 ratification).** The shelving above
> stands as recorded, WITH THIS MADE EXTREMELY CLEAR: its subject — the bolt-on joint key↔chord
> re-ranking step over the LEGACY pipeline's carried candidates — is DEPRECATED legacy-era
> machinery that will be ENTIRELY DISCARDED with the legacy path at the retirement map. The
> shelving's measurement binds that class only; it does not bear on the joint estimator (register
> entry D-001, ratified 2026-07-17, adopted 2026-07-26), which is a different mechanism class —
> one generative decode over a joint state space, not a re-ranking of legacy candidates. Register
> entry D-278 carries this scoping.

**★ AND AN ERROR SLICE IS DECOMPOSED BEFORE ANYTHING IS BUILT FOR IT — STRUCTURAL / FITTED /
CEILING (homed here 2026-08-07 on the user's ruling; decided 2026-06-13, the record states no
ratifier).**
MEASURE-BEFORE-BUILD above says that a precision claim is measured before it is built. This says
what the measurement is OF, and it is the standing method for every error slice: **decompose the
slice three ways — what a STRUCTURAL lever reaches, what belongs to the FITTED step, and what is a
genuine CEILING — before anything is built for it.** Then build the structural lever; route the
fitted share to Stage 5; route the ceiling share to accepted ambiguity, or flag it as a possible
B-trigger. **Derive, never assert.** *Why:* the lesson had already been paid three times over in
the session that stated it — three separate investigations each tested a structural lever on a
different slice and each was falsified for the same reason, while the one probe that decomposed
its slice first found the bulk of that slice specific and recoverable. Decomposing first is what
turned a pessimistic reading of the remaining error into an actionable one. It stands BESIDE the
gate above rather than inside it, and the difference is worth stating: the funnel fixes WHEN a
build may open, this fixes what must be known about the error class before the go/no-go question
is even well posed.

**Stage 4 — R9: the `chordanalyzer.cpp` file split (OWED #1), LAST.** "Split once," after the E4 removals.

**Stage 5 — the moratorium lifts (#8): the PRECISION work (#4).** Recover the corrections the fine-grain
override gave up (bass/spelling/joint-consistency, per the research), wire the calibration maps + θ, the
remaining calibration items (L1.5 texture, cadence). Everything deliberately gated behind finishing the
architecture.

**★ AND WHEN THAT PRECISION WORK OPENS, THE TWO AXES TAKE DIFFERENT MEDICINE — AND NEITHER TAKES A
WIDER SEARCH (homed here 2026-08-07 on the user's ruling; decided 2026-06-20, the record states no
ratifier). ⚠ LEGACY subject — the two-axis pipeline this was derived on is superseded on both axes by
the joint estimator; the rule is recorded as the work-programme statement it is, not as a description
of what runs.**
The stages above fix the ORDER of work. This fixes what KIND of work each axis gets when the order
reaches it. **The CHORD axis is hand-buildable:** finish the competition rules that decide between
competing readings, and dissolve the compensation gates into that competition. **The KEY axis is
soft-evidence QUALITY plus CALIBRATION, and is not hand-buildable:** raise the precision of the
evidence fed in — the cadence channel first, because it is the highest-leverage input and feeds
several layers — then let the joint combination's SOFT integration resolve what remains, with
calibration and possibly a learned emission for the residual floors. **Neither axis is improved by a
fancier lattice or a wider search.** *Why:* measured on both sides. On the key side the scoped joint
search was measured to move a fraction of a percent of stretches and to come out slightly negative
overall, which is what located the value of the joint combination in its evidence integration rather
than in its search — the same finding the shelving above records, from its other end. On the chord
side the residual was re-attributed by measurement and most of it turned out to need a candidate that
was never surfaced at all, which is a rules problem and not a re-weighting one. The structural and
cross-cutting findings that sat beside this verdict fed the architecture review rather than this plan.

## Standing habits (throughout)
Surface a surprise as a STOP before building around it (#13); investigate rather than assume when facts are
thin (#5); test/measure only on non-stale corpora (#9); verify at objects on the full surface (#15).

*Cowork, ratified 2026-07-07. Amended 2026-07-10 (user-ratified, session 36): the #17 funnel folded into
MEASURE-BEFORE-BUILD; the STAGE-3 ENTRY GATE (EG-1…EG-6) added on the L1–L5 premise-debt audit
(`cowork_l1_l5_premise_debt_audit.md`); the shelved joint step marked SHELVED in the §9.2 inventory
(doc-sync #10). Cross-refs: `cowork_structural_integrity_audit.md` §3/§4;
`cowork_stage5_fitter_design.md` (O-22, the owed refactors); the roadmap ENGAGE block (E0–E5) + R9;
CLAUDE.md #17–#19 + `cowork_premise_gate_reflection.md`.*

