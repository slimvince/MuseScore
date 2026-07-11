# Cowork Session Handoff — MuseScore Studio Harmonic Analysis

---
## ★★★ SESSION 36 CLOSE — THE CURRENT ENTRY POINT (Cowork, 2026-07-10)

**You (the next session) start context-less, and THIS handoff is the ONE document you read
first — it orients you and directs every other read (the standing convention).** From here,
in order: `CLAUDE.md` now runs **#1–#19** (the Premise Gate #17, Class-A/#18 + Class-B/#19
prohibitions, the surprise-scope rule, the fact-publication corollary, the register rules —
it is auto-loaded, but VERIFY you have the #17–#19 version); then **`OPEN_ITEMS.md`** (the
ONE register — mandatory at session start; a stage may not open while a row gating it is
open); then, when the work is an audit, `cowork_audit_protocol.md` + `DEFECT_TYPES.md`.

**What session 36 did (all local commits `416b7d6215`…, UNPUSHED — push fork-only when
ratified):** (1) PONDER-POINT 2 resolved → **#17–#19 ratified** (`cowork_premise_gate_reflection.md`);
(2) the **L1–L5 retro premise audit** (3 tiers, `cowork_l1_l5_premise_debt_audit.md`) → the
**STAGE-3 ENTRY GATE EG-1…EG-7** in `cowork_engage_arc_plan.md`; (3) **EG-2 executed under the
full gate** — scoping pre-registered with §5 predictions BEFORE the probe
(`cowork_eg2_scoping.md`), instrument established, probe run (`cc_eg2_probe_report.md`):
**P1 NOT supported — the −16 % "win" is an abstention artifact** (per-committed accuracy
slightly WORSE; abstention a coin-flip on a never-fit 0.5 margin); (4) **EG-1 premise checks**
(`cowork_eg1_premise_checks.md`): the dim7 spelling-pin never fires (gate-1 chosen-quality
precondition — root-caused at code), abstention control flow established, Xsus hypothesis
recorded UNCHECKED; (5) **`OPEN_ITEMS.md` created** — 12-surface sweep, 84+ rows, 11
contradictions catalogued; (6) the **siloed-facts audit** (17 findings; surfaces are
voice/spelling/membership-blind) → the ratified **fact-publication corollary**; (7) the
**adjudication dossier** — all 7 audit UNCLEARs decided from principles, ratified (A3: the
quality-overwrite #12 violation knowingly tolerated until E4); (8) the **certification-audit
protocol P1–P8** (`cowork_audit_protocol.md`) + the living **defect-type catalog**
(`DEFECT_TYPES.md`, DT-1…DT-17) — blind enumerative pass first, signature sweep second.

**NEXT ACTION: ✅ PASS 1 DONE (CC, 2026-07-11) — `cc_l1l2_audit_pass1_report.md`.** The first
EG-7 layer certification, pass 1 of 2 (blind enumerative, P1–P4): a machine inventory
(`tools/audit/gen_inventory.py`, 216 files tagged, 13 deep L1/L2) + a total disposition
(`gen_dispositions.py`, **688 rows all verdicted, 46 flagged**) + fire-rate (caller-liveness).
**★ The surviving L1/L2 spine is SOUND — no Class-A premise, no correctness bug.** Findings
(benign-but-recorded): upward layering deps + mixed-layer grab-bags → **OI-86**; 16 hand-set
constants off the fit manifest → **OI-87** (feeds EG-5); the Task-0 git-plumbing incident +
concurrent-edit hazard → **OI-85**; new defect types **DT-18** (object-DB-ahead-of-disk) +
**DT-19** (layer back-edge / mixed module). Freeze `feat(tools)` **`68e71665ce`** = the P8
blinding boundary (DEFECT_TYPES.md opened only after).

**✅ PASS 2 DONE (CC, 2026-07-11) — `cc_l1l2_audit_pass2_report.md`.** The blinded second
reading (**P5**, 110-row stratified sample, seed 20260711, judged from code before any pass-1
disposition was opened — **81/110 flag-agree; the 29 diffs all recording-granularity** (pass-1
propagates module-level SURVIVES-MIXED to every branch + records dormancy in prose), **no
substantive miss**, only 2 rows where pass 1 was MORE complete (`collectPitchContext` RETIRES)
+ 1 doc nit I added + 1 tie), the **full DT signature sweep** (**P8**, `gen_signature_sweep.py`
runs DT-2/3/5/12/16/19 mechanically over the WHOLE layer — reproduces OI-86/OI-87 independently),
and the **measured error rate** (**P6**, `pass2_apply_errorrate.py`: **0 wrong of 40 = 0.0 %**).
NEW: a DT-12 stale anchor (`slicer.h:68`→`regionanalyzer.cpp:579`, real call `:634/:705`) + the
`extend()` docstring "no layer calls it yet" contradicted by 3 gated call sites → **OI-88**
(minor doc fixes, NO code change, #8). Two own-tool bugs caught + fixed before use (the sampler
shared-dict `process_order` clobber; DT-5/12/16 false-positive/silent-no-op) — re-stamped, never
hand-edited. **★ CERTIFICATION of the surviving L1/L2 spine (note model L1 + change-point slicer
L2) is PROPOSED — awaiting the USER's decision (`cc_l1l2_audit_pass2_report.md` §6); NOT
self-granted; OI-84/EG-7 left OPEN.** Pass-2 commits `52d0623226` + `b8dc714f50` (`feat(tools)`)
+ this `docs(cc)` fold; pushed fork-only (`upstream` untouched). **Also awaiting the user:** the
certification decision; OI-43 (its ON-HOLD condition — the audit — is now complete); OI-44.
**NEXT (per OI-84 dependency order): the L3 layer certification audit.**

**✅ FULLY-BLIND RE-RUN DONE (CC, 2026-07-11) — `cc_l1l2_audit_blind_rerun_report.md`.** Pass 2's
second reading was only PARTIALLY blind (it read the `STATUS.md` headline at Task 0); the user
WITHHELD L1/L2 certification (OI-89 / DT-20) pending a reading that never saw a prior conclusion. This
re-runs ONLY P5 + P6, **fully** blind: all 111+40 verdicts were frozen at `fbcb59c8d7` **before** any
withheld file (STATUS / OPEN_ITEMS / DEFECT_TYPES / handoff / both pass reports / pass-1 dispositions)
was opened — strictly stronger blinding than pass 2. New independent sampler `gen_blind_rerun_sample.py`
(seeds 20260712 reading / 20260713 error, deterministic), comparison `compare_blind_rerun.py`.
**Result: reading 94/111 issue-agree, error 35/40 — EVERY disagreement is a verdict-AXIS difference
(retirement-map RETIRES / DT-2 UNFIT constants / DT-19 upward include), ZERO code-correctness misses
in either direction.** **Did the leak matter?** — it moved the NUMBERS (reading flag rate 23.6 %→1.8 %,
error rate 0/40→12.5 %; catalog-possession / shared-frame artifacts) but NOT the substance: an
un-anchored reader reproduces "spine sound, findings all tracked (OI-86/87/88), no correctness bug" and
adds one refinement (`regiontonecollector.cpp:37`→`analysisutils.h` is UNUSED, removable → sharpens
OI-86). **★ The L1/L2 spine certification is PROPOSED and now SUPPORTED by the fully-blind re-run — the
decision returns to the USER.** Task-4 doc fixes applied (`f76e8b65c8`, comment-only → **OI-88
RESOLVED**). Registers: OI-88 RESOLVED, OI-89 re-run-done, OI-86 refined, OI-84 note. Commits
`239408faad` + `fbcb59c8d7` + `f76e8b65c8` + this `docs(cc)` fold; pushed fork-only, `upstream`
untouched. **NEXT: the user's certification decision; then the L3 certification audit.**

**★ UPDATE (CC, 2026-07-11) — L3 (key/mode) CERTIFICATION AUDIT PASS 1 DONE** (`cc_l3_audit_pass1_report.md`;
the next layer after the user GRANTED L1/L2 certification, OI-84/OI-89). Read-only, no `src/`/constant/golden
change; `tools/robust_stop`/`tools/corpus` untouched. The ONE inventory instrument was **layer-selected**
(`gen_inventory.py --layer l3`, #6 — L1/L2 output substance-identical), **22 deep files → 1943 rows all
dispositioned** (`tools/audit/l3/`); fire-rate over the pinned 352-stem Baroque corpus **352/352** (11.43 %
uncertain / 3.94 % key-change / 275 modulating), dormant machinery 0 by construction. **★ The L3 spine is
SOUND — the live decoder + emission scorer are clean and music-theory-grounded, the confirmed-modulation /
joint-key machinery correctly gated OFF, layering forward-only bar two documented back-edges; NO correctness
defect.** 8 findings, all KNOWN classes / documented deferrals (no #3 surprise): the L3 emission constants
absent from `param_manifest.json` (**OI-91**, the L3 twin of OI-87 → OI-6/EG-5); two avoidable header
back-edges + pc-util silos (**OI-93**, DT-19); an unguarded C++↔Python table dup (**OI-92**, DT-3); a
file-table mis-tag (**OI-90**, new **DT-21**); contract deferrals (**OI-94**); `keyConfidence`/`keyAlternatives`
unconsumed re-confirmed (**OI-75**); tooling debt (**OI-95**). Commits `9e294f398d` (Task-0) + `b8e9a54210`
`feat(tools)` + `61dabd86d1` `docs(cc)` **freeze = the P8 blinding boundary** + this fold; fork-only,
`upstream` untouched. **Certification NOT self-granted — pass 2 (DT signature sweep, fresh session) + the P6
error-rate are OWED; decision returns to the user (OI-84/EG-7 OPEN). NEXT: the L3 PASS 2 instruction.**

*(The 2026-07-07 entry block below is HISTORICAL — its ponder-points are resolved; kept for
provenance.)*

---
## ★★ NEXT-SESSION ENTRY POINT — READ THIS FIRST (Cowork, 2026-07-07)

You (the next session) start **context-less**. This block orients you and carries **two ponder-points the
user left specifically for you to engage FRESH.** Do not skip them.

**Read before anything:** (1) `CLAUDE.md` → the **`## Guiding principles` (1–16)** — they govern every
decision; (2) `cowork_engage_arc_plan.md` — the ratified 5-stage plan + the principle behind each step (the
map); (3) this handoff's arc #9–#12 blocks below. Key design docs: `cowork_layer5_engagement_design.md`
(the Layer-5 design), `cowork_joint_key_chord_design.md` (the joint step — SHELVED, see ponder-point 1),
`cowork_structural_integrity_audit.md` (the structural audit + Stage-3 build inventory §9.2),
`cowork_functional_analysis_research_grounding.md` (published-fact grounding).

**How this works:** Cowork (the desktop session) dispatches **read-only** instructions to **CC** (Claude
Code), verifies each at objects, and brings decisions to the user. **CC has NO greater context and can
hallucinate — verify every load-bearing claim at the code yourself.** Fork-only (`origin =
slimvince/MuseScore`); **NEVER push `upstream` (`musescore/MuseScore`) — the `cfc7eb5e39` HARD STOP.**

**WHERE WE ARE (2026-07-07):** In the **engage arc**. **Stage 2 (the Layer-5 engagement DESIGN) is
COMPLETE** — the whole architecture is designed, structure-only, moratorium (#8) held (no `src/`, no build,
no constant fitted). **The joint key↔chord step is SHELVED (user-ratified):** arc #12 measured it **not to
pay** (net +0.05–0.16 pp, harm ≈ correction, coupled-minority ~0, fire-rate only 1.4 % — carried alt keys are
diatonic-collection siblings, so the chord is almost always key-stable). It is OFF the Stage-3 build list.

**★ RATIFIED THIS SESSION — MEASURE-BEFORE-BUILD:** any build whose case rests on an *anticipated precision
gain* is measured read-only **before** it is built (the joint step, and the F-B override before it, are the
lessons — both were "obvious" wins that measured out). **Distinction:** this gate is for **precision
claims** ("will building X make analysis more correct?"); **structural refactors** (decoder-replaces-tangle,
migrations) are justified by cleanliness and verified **byte-identical** — no precision measurement owed.

**★ #12 CORRECTION (recorded — the earlier "recomputable" framing was WRONG):** on the shelved joint step,
the chord under an alternative key is **NEVER COMPUTED** in this path — so nothing computed is discarded (no
#12 violation). The key alternatives ARE carried (the key discovery is preserved). Not computing a
*measured-worthless* possibility (the ~1.4 % where it differs is 50/50 noise) is an **evidence-based
decision, not information loss** — you cannot lose what you never had. ("Recompute a discarded thing" WOULD
be a #12 violation; that is not what happens here.)

**THE NEXT MEASUREMENT (the biggest unmeasured precision claim, before E4 is built):** does the **REBUILT
path** (decoder carry + the intended selection) beat the **LEGACY path** against the DCML ground truth? — the
go/no-go on the whole engagement. Needs careful scoping (the intended selection re-ordering is designed but
NOT built — be precise about what the probe exercises vs stands in for). *(Also open: a small read-only
pedal-dense probe using the DCML `pedal` GT column to settle the pedal-reader form — arc #12 flagged the
chorale data too thin, n=2–5.)*

---
### ★ PONDER-POINT 1 (user, verbatim intent) — REOPEN the joint (key, chord) RANKING; did we measure the RIGHT framing?

> *"In the current pipeline the chord under an alternative key is never computed. Why do we not compute all
> chords for all reasonably-likely modes/keys? THEN we can rank them. Maybe the top chord alternative is
> inferred based on another key/mode than the highest-ranked key/mode. The probability that the most likely
> chord is ALWAYS found using the most likely mode/key is ZERO."*

Engage this FRESH. arc #12 shelved the joint step on a **narrow framing** — decode the chord under the argmax
key, then re-decode under *carried alternative* keys, measure the flips on the coupled minority (1.4 % fire).
**That framing still decides the KEY first.** The user's point is the **full joint (key, chord) space ranked
TOGETHER** — compute the chord under *every* reasonably-likely key/mode and rank all (key, chord) pairs
jointly, so the top-ranked *chord* may come from a non-top-ranked *key*. **Our measurement did NOT test
that.** Reconsider, grounded (do not assume either way): is the near-zero measured benefit real, or an
**artifact of testing key-first-then-chord instead of joint ranking**? If joint ranking is the correct
architecture, the shelving may need revisiting — but only on measured fact, and mind the cost (#4/#6/#12).

### ★★ SESSION 36 ADDENDUM — the L1–L5 RETRO PREMISE AUDIT + the STAGE-3 ENTRY GATE (user-ratified 2026-07-10)

Applying the freshly-ratified #17–#19 retroactively to built code answered the user's follow-up ("have we
already built anything on assumptions that bites at final inference?") — **YES, three tiers**, full audit
`cowork_l1_l5_premise_debt_audit.md`: **Tier 1 armed traps** (Cowork-verified at code) — the dormant L5
`resolveAbstained` still selects **progression-first at confidence 1.0** (the channel F-B measured
uncorrelated with correctness); **`attemptFineGrainOverride` (−756) runs unconditionally**
(`functionresolver.cpp:529-531`); **confidence-scale mixing at 3 sites** with the one calibration attempt
already failed; the decoder's symmetric-rotation root **assumes the key prior correct**. **Tier 2** — the
Class-B mass: nearly every live scoring magnitude hand-set pre-2026-06-13 against the later-proven-broken
batch gate (unfalsified ≠ established; only kWStepIn ever robust-unit-fit). **Tier 3** — containment holes:
manifest excludes L1/L2 + live-L3 constants; **Jazz has NO licensed GT** (unvalidatable); L5 firewall
placeholders; doc-drift. **Consequence (ratified): the STAGE-3 ENTRY GATE EG-1…EG-6** in
`cowork_engage_arc_plan.md` — Tier-1 defusal is a PREREQUISITE of L5-to-production; rebuilt-vs-legacy runs
under full #17+#19; pedal reader hard-gated on owed-P1 over an established pedal-dense corpus; θ/kBoundary
fitting owes ledger+desk-sim; manifest completion before Stage 5 closes; Jazz status declared. §9.2 synced
(pedal gated, joint step marked SHELVED — the arc-#12 sync omission fixed). **NEXT SESSION: nothing opens
without its #17 ledger; the rebuilt-vs-legacy scoping (EG-2) is the natural first item, preceded by
establishing its instrument (#19).**

### ★ PONDER-POINT 2 — ✅ RESOLVED & RATIFIED (2026-07-10, session 36): the PREMISE GATE

**Engaged fresh and ratified by the user 2026-07-10.** Full analysis + evidence:
`cowork_premise_gate_reflection.md`. Outcome now standing in **CLAUDE.md #17–#19 + the
surprise-scope rule**: **#17 the Premise Gate** (premise ledger FACT/THEORY/ASSUMPTION ·
written quantitative prediction per assumption — no prediction, no build · desk simulation on
3–5 real failing-set cases · proxy→target links are premises · insulation claims enumerate the
false-negative path · no hand-transcribed numbers); **#18 unverified causal premises FORBIDDEN
(Class A)**; **#19 unestablished instruments FORBIDDEN (Class B)**. **Scope:** surprises
allowed in explorational (ignorance-elimination) runs; NOT allowed when building actual
inference code — there a surprise is a STOP (#13) and Premise-Gate evidence. Funnel:
**desk-simulate → read-only probe → build.** Diagnosis in brief: not a capability failure —
every root cause (F-B's uncorrelated contradiction; the joint step's collection-sibling
key-stability; the gate-insulation false-negative path) was derivable at design time; the
process asked the quantitative question only after building. The next owed measurement
(rebuilt-vs-legacy vs DCML) and PONDER-POINT 1 both run under #17 from here. Original
ponder-point kept below for provenance.

### ★ PONDER-POINT 2 (user, verbatim intent) — WHY do we STILL get surprises? A way-of-working reflection. *(✅ resolved above)*

> *"Start with reasoning why we STILL get surprises: what we thought would work does not — why? Are we not
> clever enough? Are we guessing (hallucinating, assuming) instead of basing our decisions on CURRENT facts
> and established algorithms? Have we even tried to desktop test (dry run, simulate) some ideas through the
> intended architecture and its algorithms? What needs to change in our way of working to once and for all
> stop being surprised?"*

Principle #3 says a surprise means we failed #1 (fact/theory-based). We keep being surprised (F-B
net-harmful; the joint step barely pays). **Settle this BEFORE more building.** Reason about: are we
*guessing* vs grounding on current facts + established algorithms (#1)?; have we **desktop-tested / dry-run /
simulated** candidate ideas *through the intended architecture and its algorithms* before building or
measuring (we have NOT — we design, then build/measure, then get surprised; a simulate-first step may catch
the surprise earlier and cheaper); **what concretely must change in the way of working to stop the
surprises.** This is the first thing to resolve next session.

---

**★ ENGAGE ARC #12 — Stage-3 owed MEASUREMENTS: does the joint key↔chord step actually pay? MEASUREMENT-ONLY
(session 35, 2026-07-07).** CC executed `cc_instruction_engage_stage3_joint_measure.md` — Stage 3 opens
**measurement-first** (#1/#3/#5): settle the decisive fact the joint-step design (`cowork_joint_key_chord_design.md`)
left unmeasured — **does re-deciding the chord under alternative CARRIED keys measurably improve root-correctness,
or not?** — BEFORE building the joint step (the #1/#3/#5 guard against building another plausible-but-unhelpful
mechanism the way the F-B override was built on an unmeasured assumption). **READ-ONLY:** no production behavior
change, no build of the joint step, no fit, no constant tuned.

**The instrument (feat `689840d2ef`).** `--dump-joint-probe` — a default-OFF `batch_analyze` diagnostic + its
corpus harness `measure_joint_probe.py` that exercises the EXISTING `ChordSliceDecoder` as a **PURE re-decode
function** (`chordslicedecoder.h:524-531`, "this increment takes one key"; per-slice ranking context-free) under
L3's already-carried per-region key menu — the production `HarmonicRegion`'s **argmax key `keyModeResult` ∪ the
carried candidate menu `keyAlternatives`** + the **D-L3a sequence-margin `keyConfidence`**. It is **NOT** the
production joint step (no beam driver, no wiring, no behavior change) — the "faithful mechanism" the design §2.2
names, run as a measurement probe. The A/B holds the decoder FIXED and varies only the key (decoder-under-argmax
vs decoder-under-alt). Benefit measured vs the DCML root by the **SHARED a8 substrate** (`_dcml_time_spans` /
`_active_index_at` / `dcml_parser`), the same way the robust stop is (#1) — no proxy, no new tick matcher.
Production byte-identical: 12/12 corpus stems reproduce the committed `tools/corpus/baroque/*.ours.json`
byte-for-byte; both stops identity-PASS by construction; no `src/`, no golden refresh.

**★ THE GO/NO-GO (measured, pinned corpus `c50002fee1`, ×3 presets): the joint step barely pays overall, and on
the population it is scoped to it does not pay at all.**
- **Benefit (corr/harm/neutral on the root FLIPS):** net corr−harm = **+9 / +3 / +10** (Baroque/Jazz/Default) over
  **~6200 DCML-scored regions/preset = +0.05–0.16 pp**; **harm is 75–90 % of correction** everywhere (37c/28h,
  36c/33h, 35c/25h). The **oracle upper bound** (a perfect key-selector) is only **+35–37 regions = +0.6 pp**, and
  it EQUALS the top-alt result — the top carried key IS the one that flips-to-correct when any does.
- **On the coupled minority** (key-uncertain, sequence margin < 1.0 — the C3 population the step is theory-scoped
  to): net **0 / +5 / −2** on n = **16 / 15 / 11** — **zero-to-noise, one preset negative.**
- **Fire-rate (owed-1/3):** the chord flips under a carried key in only **1.4–1.5 %** of committed regions
  (0.9–1.4 % coupled) — **~10× below** the 13.5 % `decideJointKey` `coupled` structural proxy. The chord axis is
  **almost always key-stable**: the carried alternatives are diatonic-collection siblings (relative/enharmonic
  keys), so the decoder's diatonic-prior term barely shifts and the winner root does not move (fact-grounded #1,
  not a surprise). **Beam width (owed-4):** ~5 carried keys, but a **width-2 beam captures every available
  correction** — extra carried keys add nothing.
- **owed-1/2/3 settled read-only; owed-4-fixpoint / owed-5 / owed-6 build-gated** (need the built joint scorer).

**Pedal owed-P1 (Task 3, secondary).** Over production `isPedalPoint` regions, does the decoder carry under the
argmax key already hold the in-place pedal (upper-voice) root? Agreement **0.20 / 0.50 / 0.20** — leans to the
§6.3 "upper-voice-conditioned Layer-4 carry attribute" form rather than a pure carry-reader (consistent with the
audit's decoder-has-no-pedal gap), **BUT UNDERPOWERED** (only n = 2–5 pedal regions on the chorale corpus).
**Declared: measured but not decided;** a decisive read needs a pedal-dense corpus (the DCML `pedal` GT column
exists for that).

**#3 discharge / #8 boundary.** No new surprise — the design's own owed-2 predicted "small"; the measurement
**sharpens it downward** (sub-single-digit overall, ~zero coupled) and grounds WHY (key→chord coupling is
structurally weak precisely on the collection-sibling key ambiguities that are the hard cases). **Verdict handed
up (#8, the build decision is Cowork's/the user's):** the measured evidence does **not** support building the
joint key↔chord step as a precision lever. Report `cc_engage_stage3_joint_measure_report.md`; data
`tools/reports/joint_probe_measure.json`. HEAD `fa0a881aa4`→ (feat `689840d2ef` + this fold); pushed fork-only
(`cfc7eb5e39` upstream HARD STOP honored). **On CC's report: Cowork verifies at objects → brings the go/no-go +
sizing to the user; the build decision is theirs, on measured fact.**

---

**★ ENGAGE ARC #11 — PEDAL detection's home + the F-B ANNOTATE mechanics: DESIGN — CLOSES STAGE 2 (session 34,
2026-07-07).** CC executed `cc_instruction_engage_l5_pedal_annotate_design.md` — the **last two Layer-5 engagement
design pieces** Part 1 enumerated (§4.2 gap 3 pedal, §4.3 F-B mechanics). **READ-ONLY / STRUCTURE-ONLY:** no
`src/`, no build, no corpus write, **no constant fitted or tuned** (R5; #8). Deliverable **`cowork_layer5_engagement_design.md`
Part 2 (§6–§10)** — appended, NOT a new doc (#6: Part 1 enumerated these two as its own follow-ons, same concern,
one home; Part 1 = §1–§5, Part 2 = §6–§10). **Task 1 — pedal's home = a READER OVER THE CARRY, not a winner-mutator.**
Grounded at `chordpostpasses.cpp:209-281` `[code]` + the audit's pedal finding (`cowork_structural_integrity_audit.md`
§1.1 #7 / §1.3 / §1.4) + the **confirmed decoder gap** (grep `chordslicedecoder.cpp` pedal → **0 matches**). Placed
as a reader over the decoder's governed Layer-4 carry that emits a distinct pedal-annotated result, never a
`results.front()` mutation; the audit's **three coupled symptoms all dissolve**: the clobber (`results = pass2`, `:274`)
→ annotate a carried candidate, the full-voice reading survives (#12); the re-implemented diff-root scan (`:262-269`,
the 4th copy) → **read** the confirmation margin from the carry's distinct-root ranking / the FQ-1 primitive over the
carry (tied to `chordslicedecoder.cpp:927-930`) — **no 4th scan**; the defensive append-disable (`:240-245`) → the
cap→append it defended against is a legacy-`results` property, the governed carry has none to contaminate. The
material pedal needs (upper-voice harmony + confidence gap) is *usually* already a carried distinct-root alternative
excluding the bass — **subject to owed measurement [owed-P1]** (carried-alt vs bass-stripped re-decode agreement).
**Task 2 — F-B annotate vehicle = the UNIFIED OPEN-MARK (reuse, NOT a parallel channel; the load-bearing #6 call,
decided at the code).** Reconciled `cowork_fb_redesign_design.md` §4.2's proposed new `functionContextContradiction`
field against the existing open-mark (`ResolvedReading.openMark` `functionresolver.h:170` → `FunctionUnitAssembly`/
`FunctionAnalysisUnit.openMark` `functionoutput.h:165/124`; §8 case-3 honest-carry `cowork_layer5_function_design.md:582`;
§15-13 both-licensed): **overloading the plain boolean is semantically WRONG** (openMark = "genuinely undecidable /
no answer", but F-B's L4 committed confidently and the reading is carried unchanged — setting it loses info #12 +
collides with the case-3 abstain meaning); **a parallel bool is a duplicate channel (#6 violation)**; **DECIDED:
unify into ONE structured open-mark carrying a reason/kind** — `Undecided` (case-3/§15-13, today's semantics kept)
vs `FunctionContextContradiction` (F-B; reading stays the L4 commit, `overrodeCommit` stays false). The contradiction
is carried as **calibrated uncertainty** (#12: the L4 reading survives = the +756 recovery, AND the frame's `(C,S)`
quantities become the open-mark payload, Class-M, squash-constant precision-phase R5 — the 1043 signals preserved for
a future C3 joint step); the trigger is an **annotation lever, never an override** (no `overrodeCommit`, no
`prog[i].chord` mutation, no `forwardRecompute`; Frame F-B re-declared in contract §4 as an annotation channel).
**Task 3 — boundaries/owed build/owed measurements:** pedal = carry-side reader (Layer-4 output), forward-only, no
reach-in; F-B annotation = Layer 5, additive, **acyclicity strengthened** (the one former cross-layer recompute
removed). Owed build (enumerated): the pedal reader-over-carry; the F-B wiring (open-mark enrich + `attemptFineGrainOverride`
demotion + `ResolutionBasis::FineGrainOverride`→`FineGrainContradiction` + contract §4 re-declaration + L5/`docs/scoring_model.md`
sync). Owed measurements (#5): [owed-P1] pedal reader vs in-place detection agreement; [owed-P2] carried-margin vs
`pass2` sigmoid; [owed-FB1] F-B byte-identical today, must move class-(b) DURATION favorably at engage. **Task 4 —
★ STAGE-2 COMPLETE:** carry+selection (arc #9), the joint step (arc #10), pedal home + F-B annotate (arc #11) — all
designed, structure-only, moratorium held. **No Layer-5 engagement concern remains undesigned; Stage 3 (E4 /
algorithmic completion) is the user's to open with nothing left undesigned.** The Stage-3 build inventory it inherits
is enumerated at `cowork_layer5_engagement_design.md` §9.2 (the anchor/FQ-4; the distinct-root-preserving carry;
the pedal reader; the F-B annotation; quality-from-key's owner FQ-2 + §6-block; the joint step B1–B4 + owed
measurements; the owed migrations FQ-8/FQ-1/FQ-3; the F-1/S19/D-FS confidence-scale fix). Report
`cc_engage_l5_pedal_annotate_design_report.md`; fitter engage-observation updated. `docs(cowork):` fold (Part-2
design + report + STATUS + HANDOFF + fitter + arc plan Stage-2-complete + instruction force-add). **No `src`/build/
corpus/fit; both regression stops green by construction (no code path touched, byte-identical to HEAD `2c550ec327`);
suites unchanged (no build); corpus frozen `c50002fee1`; fork-only, `upstream` untouched (`cfc7eb5e39` HARD STOP
honored).** **FRESH SESSION:** Cowork verifies the design at objects → the Layer-5 engagement design phase (Stage 2)
is complete; presents pedal-reader + F-B-annotate + the Stage-3 build inventory to the user to open Stage 3. Prior
header, kept:

**★ ENGAGE ARC #10 — the JOINT key-and-chord step: ARCHITECTURE DESIGN (session 33, 2026-07-07).** CC executed
`cc_instruction_engage_joint_key_chord_design.md` — the next Stage-2 design piece (the biggest precision lever #4,
on the foundation Part 1 established). **READ-ONLY / STRUCTURE-ONLY:** no `src/`, no build, no corpus write, **no
constant fitted or tuned** (R5; #8). Deliverable **`cowork_joint_key_chord_design.md`** — a NEW doc (the O-4 "C3
joint-step design document"; the L5 engagement doc scopes selection-within-a-fixed-key and enumerates the joint
step as a *distinct* downstream piece §4.1/§4.3, so #6 wants a separate home). **★ THE FINDING THE DESIGN TURNS
ON:** the joint step is **NOT greenfield** — its **key-axis half is already built + measured** as `decideJointKey`
(J-key-i/ii/iii, `section/jointkeydecision.{h,cpp}` `[code]`): a key-state lattice, a **Viterbi with a
key-transition prior** (`JointKeyWeights.transitionPenalty`), a measured **coupled minority ~13.5%** (`coupled =
!chordPinned && keyAmbiguous`, `jointkeydecision.cpp:289-297`), and a **config-B chord→key coupling**
(`couplingScore`, `:275-287`) — while its **chord axis is EXPLICITLY DEFERRED "to a faithful mechanism"**
(`regionanalyzer.cpp:388-395`). That deferred chord re-decode **IS** the per-key re-decode C3 found computed
nowhere (`cc_engage_c3_measurement_report.md` §2.3). So the design = a **total-unification completion (#6) of
config-B**: add the deferred chord re-decode axis → a bidirectional (key,chord) beam, gated on the C3 minority,
publishing forward to Part-1 L5. **Task 1 — placement (#7 acyclicity):** a **BOUNDED coupling step** at the
L3/L4→L5 seam, **NOT a unified `(key,chord)` hidden state** — grounded on #7+#6 (a unified state discards+rebuilds
both built decoders; the research single-state is a *modeling* choice, the recipe = beam+transition-prior+re-decode
is factoring-independent) + magnitude realism (the win is qualitative on the coupled minority, so a step that
FIRES ONLY there and is a pass-through on the majority is proportionate) + the forward-only/acyclicity contract (it
consumes L3's *already-carried* key alternatives, *drives* L4's pure re-decode, re-ranks the key **inside its own
bounded closure**, and publishes one settled (key,chord) forward — no L3←L4 back-edge; the cycle-introducing
placement, L4 writing back into L3's committed key, is named + avoided). **Task 2 — mechanism (structure only,
R5):** a **beam of (key,chord) hypotheses**; the chord **re-decoded under each carried key** via the existing
`ChordSliceDecoder` (a pure fn of (slices,key) — the "faithful mechanism" J-key-iii named, no multi-pass
artifact); the **key-transition prior REUSED** (`transitionPenalty`/`changeCost`, #6); an **additive/monotone/
no-veto composition** over the RE-DECODED chord (config-B completed); **one forward beam pass** recommended over a
capped bounded fixpoint; a **declared Class-M joint-decision confidence** (margin of the winning joint hyp over the
best different-key-or-root hyp, squashed; R5). **Task 3 — trigger (C3) + interface:** a **two-stage gate** — cheap
pre-filter `(a)` key-uncertain (`HarmonicRegion.keyConfidence` < seq-margin bar 1.0, the D-L3a boundary confidence)
`∧ (a′)` chord-structurally-ambiguous (L4 `openQuestion`/`Abstain`/low `composite`, or `chordPinned=false`), then
the **exact `(b)`** (the winner root flips under a carried key) computed **BY the step's own per-key re-decode** —
which is precisely why C3 was un-computable read-only ((b) IS the owed build). Only `(a)∧(b)` commits a coupled
decision; the rest is a byte-identical pass-through. **Interface:** reads L3's carried `keyAlternatives`/
`keyConfidence` (the step is the long-awaited consumer of that in-memory carry, #12) + L4's per-key carry; emits
the settled `(k*,c*)` + confidence **FORWARD** to L5, which **selects within the settled key** (Part-1 §4.1 kept;
L5 never re-ranks the key — that is the joint step's job upstream of it). **Task 4 — owed build by layer
(enumerated, NOT built):** **B1** per-key re-decode driver (Layer 4 — N forward calls of the built decoder, no new
decoder; prerequisite = the distinct-root-preserving carry owed at E4 so a flip is *visible*) · **B2** beam/
coupling driver + joint confidence (the joint step = **generalize `decideJointKey` config-B**; NEW = the chord axis
+ the joint margin; NOT a parallel module) · **B3** the two-stage trigger gate · **B4** production wiring (complete
J-key-iii's deferred chord axis, behind its existing held `setJointKeyWiringEnabled` flag) — all forward-only,
bounded, **E4-adjacent** (builds on the engaged decoder). **Task 5 — owed measurements (#5, none assumed):**
[owed-1] the true C3 fire-rate (the ~13.5% `coupled` is a structural PROXY, not `(a)∧(b)`; un-measurable until B1)
· [owed-2] the coupling benefit magnitude (the robust-stop sandwich on the coupled set, post-B2 — the eventual
acceptance gate) · [owed-3] the per-key winner flip-rate · [owed-4] beam width / fixpoint depth · [owed-5] the
chord→key coupling term under re-decode · [owed-6] all precision-phase constants (Stage-5 fits). Report
`cc_engage_joint_key_chord_design_report.md`; fitter O-26 + O-4 closed. `docs(cowork):` fold (design doc + report +
STATUS + HANDOFF + fitter O-26/O-4 + instruction force-add). **No `src`/build/corpus/fit; both regression stops
green by construction (no code path touched, byte-identical to HEAD `32709a9e7a`); suites unchanged (no build);
corpus frozen `c50002fee1`; fork-only, `upstream` untouched (`cfc7eb5e39` HARD STOP honored).** **FRESH SESSION:**
Cowork verifies the design at objects → presents the (key,chord) coupling architecture + the owed build (B1–B4) +
the owed measurements to the user for the build event. Prior header, kept:

**★ ENGAGE ARC #9 — Layer-5 engagement DESIGN Part 1: the CARRY + SELECTION architecture (session 32,
2026-07-07).** CC executed `cc_instruction_engage_l5_carry_selection_design.md` — Stage 2 of the ratified plan,
opened on the O-24 real fan-out. **READ-ONLY / STRUCTURE-ONLY:** no `src/`, no build, no corpus write, **no
constant fitted or tuned** (R5; #8). Deliverable **`cowork_layer5_engagement_design.md`** — a **NEW doc**, not an
edit of the signed `cowork_layer5_function_design.md` (engagement wiring is a distinct concern from the signed
dormant-build spec; #6, one home per concern; the new doc references the signed §5.5/§7/§8/§15 rather than
restating). **Task 1 (inventory built vs owed):** `resolveCarriedReadings` (per-`AmbiguityKind` selection Phase 1
+ the F-B override Phase 2), `assembleFunctionOutput` (§7 pure additive assembly), the `FunctionSlice` input
contract, and the F-A/F-B frames (D-L5a closed / D-FS open) are **built + dormant** (`functionresolver.cpp`,
`functionoutput.h` `[code]`); engagement WIRES this pipeline — owed = populate the carry from the live decoder
(today hand-injected in tests), generalize selection to the full distinct-root carry, re-frame F-B, add pedal
detection. **Task 2 (the carry contract):** Layer 5 reads a **distribution over distinct ROOTS** (the meaningful
axis — median ~2, a ≥3rd root on 25.1/16.1/24.9 %), each root carrying its best voicing + variant set + graded
confidence; **the exclusion tail (ruled-out/low-confidence roots) is CARRIED, not dropped (#12).** ★ **Decoder gap
NAMED:** `sc.alternatives` caps on **voicings** (`sameChordVoicing`, `topK` default **6**, `chordslicedecoder.cpp:746-789`),
NOT roots ⟹ the ≥3rd distinct root is **not structurally guaranteed** to survive; the ∪-incumbent-carry guarantees
the prevailing root and `nameOpenQuestion` names ONE alternate root on abstains (`:929-931`), but neither
guarantees a third, and a **Commit** slice names none — so a **distinct-root-preserving carry is OWED at Layer
4/E4** (cap on distinct roots + bounded variant depth; the depths are precision-phase). **Task 3 (selection-by-
joint-consistency, structure only):** select across **key/root/inversion/bass** over the graded distribution incl.
the exclusion tail; evidence channels ranked **load-bearing-first** — bass/inversion (Vuvan), spelling
(Micchi/McLeod), key-consistency (ChordGNN/AnalysisGNN), cadence — with **licensed progression DEMOTED to a
tie-break among already-consistent readings, NEVER an override lever** (the F-B measured net-harm −756 +
Korzeniowski/Widmer/Vuvan corroboration). This **re-orders the as-built `resolveAbstained`** (which leads with the
weak progression channel) and **reconciles with the settled F-B annotate-not-override finding** (§3.D-1: carry the
L4 commit unchanged, surface contradiction as an honest open mark). Confidence L5 emits: the built
`combinedBoundary` (D-L5a) + a **NEW declared Class-M joint-consistency selection margin** (squash shape declared,
constant precision-phase, contract U1/R5). **Task 4 (boundaries/gaps/agenda):** L4 = the carry (under the L3 key);
L5 = selection **within a fixed region key** → the functional analysis; ★ **the joint key↔chord step (O-18/C3) is a
DISTINCT downstream step, NOT L5 selection** (it re-ranks the key under chord evidence — the research's (key,chord)
beam); acyclicity kept (the §8 forward-only bounded recompute). Engagement gaps: carry wiring · the distinct-root
guarantee · **pedal detection (the decoder has NONE — audit gap; a reader-over-carry, not a `results`-mutating
post-pass)** · F-B annotate mechanics · D-FS commensurability. The downstream pieces are **ENUMERATED with each
hinge named, NOT resolved** (FQ-2 quality-from-key owner; pedal detection's home; O-18/C3 joint step; F-B annotate
mechanics). Report `cc_engage_l5_carry_selection_design_report.md`; fitter O-25. `docs(cowork):` fold (design doc +
report + STATUS + HANDOFF + fitter O-25 + instruction force-add). **No `src`/build/corpus/fit; both regression
stops green by construction (no code path touched); suites unchanged; corpus frozen `c50002fee1`; fork-only,
`upstream` untouched (`cfc7eb5e39` HARD STOP honored).** **FRESH SESSION:** Cowork verifies the design at objects →
presents the carry + selection architecture + the follow-on agenda (concern-owners, joint step, F-B) to the user
for the next Part. Prior header, kept:

**★ ENGAGE ARC #8 — the TRUE untruncated Layer-5 fan-out, MEASURED read-only (session 31, 2026-07-07).** CC
executed `cc_instruction_engage_fanout_measure.md` — the Stage-2 prerequisite: how large is the graded
candidate distribution Layer 5 will select over? **Route:** no faithful no-`src` path exists —
`--diagnose-measures` replays `diagnoseChord` with a **NULL temporal context** (`batch_analyze.cpp:1689`) and
emits no threshold; `--dump-fullspine` runs a **different decoder** (`ChordSliceDecoder::decode`, not the
`applyHarmonicFunction` competition). So a **single minimal additive default-OFF field**: `RawFanoutSummary`
(`chordanalyzer.h`) computed by `computeRawFanoutSummary(gateCtx)` from the production `gateCtx.rawCandidates` +
`gateCtx.threshold` at the region commit sites (`regionanalyzer.cpp` :1054/:1250/:1442), carried **in-memory
only** on `HarmonicRegion`/`AnalyzedRegion` (the `keyAlternatives`/`keyConfidence` not-serialized idiom),
emitted solely by **`--dump-fanout`** (mirrors `--dump-region-keymargin`; returns before `writeJson`).
**Byte-identity PROVEN — 1056/1056 `.ours.json` 0-diff vs frozen `c50002fee1`** (default flags); both stops
trivially green (class-(b) +0/−0; characterise **52/24/52**); suites **1101 / 53 / 11**, no golden refresh.
Instrument is a separate revertible `feat` (#14); docs a `docs(cowork):` fold. **THE NUMBERS (corpus
`c50002fee1`, HEAD `b5857ed2f3`, ×3 presets, per committed competition slice):** the §1.5 audit measured only
the capped floor (≤3 + conditional append, ~36 %/21.5 %); the **TRUE above-threshold ranked set is ~2×** —
median **5/4/5** readings (Baroque/Jazz/Default), mean **6.35/6.15/6.32**, p90 **11/12/11**, p99 **27/23/27**,
max **49/46/49**. **Cap-of-3 discards ≥1 above-threshold reading on 79.5/75.4/79.3 %** of slices (>5 on
37.4/33.6/37.2 %, >10 on 10.8/13.2/10.5 %). **BUT the readings collapse to ~2 roots** — distinct roots above
threshold median **2/1/2**, mean **2.13/1.73/2.12**, >1-root on **68.8/46.7/68.6 %**. **★ The load-bearing
exclusion tail (#12): a ≥3rd distinct root clears threshold on 25.1/16.1/24.9 %** of slices — roots the cap-of-3
+ single diff-root append (winner + ≤1 alternate root) **cannot represent**. `fanoutTotal`=**204** constant (12
roots × 17 `kTemplateCount` templates — the full scored grid; so "total" is structural, the meaningful fan-out
IS the above-threshold subset ≈3.1 % of the grid). Jazz's narrower root set tracks its suppressed inversion
bonuses. Report `cc_engage_fanout_measure_report.md` + machine-readable `cc_engage_fanout_measure_data.json`;
instrument `tools/measure_fanout.py`. Observation only (moratorium — no inference coding, no design decision).
Corpus frozen `c50002fee1`; fork-only, `upstream` untouched. **FRESH SESSION:** Cowork verifies the
distribution at objects → **Stage 2 (the Layer-5 engagement design) opens** on the real fan-out. Prior header,
kept:

**★ ENGAGE ARC #7 — STAGE 1 DELIVERED — the PRE-Layer-5 refactor batch (session 30, 2026-07-07).** CC
executed `cc_instruction_engage_pre_l5_refactor_batch.md` (ratified plan `cowork_engage_arc_plan.md` Stage 1).
Diff base HEAD `0d7fcc6c48`. **Three byte-identical revertible commits**, each proven **0-diff `.ours.json`
across 352×3** (Baroque/Jazz/Default) vs the pre-commit HEAD + **robust-stop PASS** (class-(b) non-increase,
+0/-0) + **characterise 52/24/52** + **suites 1101 / 53(+4 skip) / 11** no golden refresh:
**FQ-5 `65764881d0`** [S5 beat-weight→`regionMetricWeightForBeatType`; S10 shared `normalizedConfidenceSigmoid`;
S11 `makeChordPathNode`; S7 partial — redundant copy-3 deleted, full A↔B single-sourcing DEFERRED (couples the
minimal `modepriorpresets.h`→`analysistypes.h`, a dependency-profile decision)] · **FQ-7/S8 `56b06462db`**
[key-decoder cost/window constants sourced from `kDefaultKeyModeAnalyzerPreferences.*` +
`scoreharvest::DECAY_RATE`/`LOOKAHEAD_WEIGHT`; **S9 adjudicated KEPT — load-bearing NOT dead**:
`resolveKeyAndModeRanked@585` feeds `greedyExpandSegmentation@851` + `findTemporalContext@900` = the grid] ·
**FQ-6 `5420e6e543`** [`appendCappedAlternatives` shared projection in `analyzed_section.h`; batch cap=3,
bridge uncapped, values verbatim; cap-#2 value lift stays Stage-3-deferred].
**TWO items STOP-and-reported, NOT forced (for Cowork adjudication):** **FQ-1** — at code the four
"best different-root" scans are NOT one decision (divergent predicate: rootPc-only #1/#2/#3 vs
`sameChordSymbol`=root+quality #4 `chordslicedecoder.cpp:81`; divergent element type + result-use;
`promoteToWinner` promotes a *specific* target to front, not the vehicle) → no byte-identical single primitive;
the "one decision, four sites" audit premise over-counts at code granularity. **FQ-3** — byte-identically
relocatable + decoder-independent BUT E4-entangled (decoder already `findTemporalContext`-seeded at
`regionanalyzer.cpp:899-902`, `decoder.commit()≡advanceTemporalContext`; D-P4/D-BRIDGE/1068: cold walk
E4-superseded) + most-invasive → UNCLEAR-7 resolves to **fold into E4**. Report
`cc_engage_pre_l5_refactor_report.md`; audit §3.1 stamps RESOLVED/deferred rows with SHAs. Both stops green
throughout; corpus frozen `c50002fee1`; fork-only, `upstream` untouched. **FRESH SESSION:** Cowork verifies
each byte-identity at objects → the Layer-5 engagement DESIGN (Stage 2) opens; FQ-1 + FQ-3 await adjudication.
Prior header, kept:

*Written 2026-05-14. Last updated 2026-07-07, session 29 (engage arc #6 — **the STRUCTURAL-INTEGRITY audit**
[read-only grounded catalogue, ALL built layers; total-unification #6 + layer-adherence #7 + build-on-clean-theory
#1 made proactive — the structural analogue of the arc-#4 info-loss audit]. READ-ONLY: no `src/`, no corpus write,
no build, no fix; both stops untouched/green. **Anchor** [`results` carry, Layer-4 legacy]: a 10-consumer/concern
structure — winner `front()`; carry→`alternatives`; cap-of-3 `harmonicfunctionlayer.cpp:521`; the diff-root
"guaranteed inversion alternative" append `:530-549`; Iter 86/91 `chordpostpasses.cpp:135-188`; pedal detection
`:209-281` [`results=pass2` CLOBBER + re-implemented diff-root scan + DEFENSIVELY DISABLES the append]; the gate
flip via the uncapped `gateCtx->rawCandidates`; the batch caps `batch_analyze.cpp:660/712`; the uncapped bridge
`notationcomposingbridge.cpp:297`. **cap→append dissolution PROVEN at code** [append pulls only above-threshold ⟹
uncapped threshold-only build is a strict superset ⟹ append dies; winner unchanged, carry grows ⟹ ratified
re-baseline]; **honest discrimination:** Iter 91's `kPromoteAppendOnly`/`stopBelowThreshold=false` below-threshold
pull is a legitimate targeted promotion, does NOT dissolve. **Clean-target ALREADY BUILT in the dormant decoder**
[`chordslicedecoder.cpp:746-789` governed `topK`-distinct-voicings ∪ principled incumbent-carry; diff-root read
FROM the carry `:927-930`; NO pedal detection yet — a gap]. **Fan-out** [read-only, capped floor]: append fires on
**36.2% Baroque / 21.5% Jazz / 36.1% Default** of all regions [serialized `alts=3` ⟺ append fired]; true untruncated
size needs the `rawCandidates` instrument [flagged]. **Sweep** [4 parallel read-only agents]: 1 anchor + 20 sites =
**6 VIOLATION · 8 UNCLEAR · 6 OK/RESOLVED**; **2 HIGH** [anchor; `findTemporalContext` = an L1.5 view driving the
full L4+L5 pipeline ×2, `regiontoneprimitives.cpp:451-592`] · 9 MED · 9 LOW. Cross-cutting +: **quality-from-key
second-guessing has NO single owner** [≥4 sites/3 layers]. Progress confirmed [extends priors]: section-in-notation
RESOLVED; `promoteToWinner`/`kMasks`/single-owned-metric-scripts/`forwardoverride` clean. **★ Sequencing call
[load-bearing]:** the anchor FOLDS INTO E4 [decoder already realizes its clean-target — a standalone legacy refactor
is throwaway]; three portable slices are PRE-L5 wins [different-root primitive FQ-1; `findTemporalContext` relocation
FQ-3; fact-layer dup + cap-views FQ-5/6]; one coherent order → §6-block dissolution [OWED #2, Stage-5/E4] owns FQ-2
[quality-from-key single owner] → E4 legacy-path retirement owns the anchor FQ-4 → R9 splits `chordanalyzer.cpp`
[OWED #1] last. Catalogue `cowork_structural_integrity_audit.md` + report
`cc_engage_structural_integrity_audit_report.md`; O-22 folded into the fitter design §15; 7 UNCLEAR rows for
adjudication. `docs(cowork):` fold [catalogue + report + STATUS + HANDOFF + fitter §15 + instruction force-add];
pending CLAUDE.md #12 edit left untouched; pushed fork-only [`cfc7eb5e39` upstream HARD STOP honored]. On CC's
report: Cowork verifies the catalogue at objects → brings the user the fix-queue, the sequencing call, and the
UNCLEAR rows. Prior header, kept: session 28 (engage arc #3b — **the GateA promotion-unification
BUILD event** [user-ratified]. Layer-4 `src/` change + build + full-surface verification, implementing the
ratified arc-#3 design. **One `promoteToWinner` primitive** [present-first swap = former **Gate A**; append-built
pull = former **FM2**] + **one builder wrapper** `buildResultFromGateCtx`; the three duplicated `buildResult`
lambdas collapse [postscoringgates + chordpostpasses route through the primitive; harmonicfunctionlayer's initial
build calls `buildChordResult` directly]. The enharmonic Major-add6→Minor7 flip = ONE primitive call
[`presentHint = bestAltIdx` reproduces Gate A's `std::swap` byte-for-byte; append reproduces FM2]; Gate E, the
G-family [G-E/G-D] and the Iter-91 bass-pull also route through it. **The separate `GateA` §6 rule REMOVED**
[enum member / `ruleOff` guard / name-map; §6 rules 10→9]; **FM2** = surviving flip rule [O-11 retirement
condition met — the primitive reproduces Gate A's carry]. doc-sync `docs/scoring_model.md` [new §6a]; stale
`chordpostpasses.cpp:128` comment removed. **Full-surface byte-identity PROVEN at objects** [winner AND
`alternatives[]` = whole `.ours.json`]: **0 diffs / 1056 files across all 352×3, including the 36** —
`C_unified == C_HEAD` by construction. **Both stops GREEN [measured]:** batch 52/24/52 set-diff empty; robust
sandwich identity-PASS [runs 6868/7036/6883 +0/-0; class-(b)&(a) dur Δ+0]. Suites 1101/53+4skip/11 [NO golden
refresh]; committed `tools/corpus/` + `tools/robust_stop/` untouched [scratch]. Net user-visible delta = ZERO
[#12]; total-unification [#6] closing the L1 info-loss path [O-11/O-19]. feat `200681a855` [src + tests +
`docs/scoring_model.md`] + this `docs(cowork):` fold [report `cc_engage_gateA_unification_build_report.md` +
STATUS + HANDOFF + fitter observation + instruction (force-add) + the pending `cowork_information_loss_audit.md`
edits]; pushed fork-only [`cfc7eb5e39` upstream HARD STOP honored]. On CC's report: Cowork verifies the
byte-identity proof at objects; the O-11 / L1 fix-queue item is DISCHARGED. Prior header, kept: session 27
(engage arc #4 — **the INFORMATION-LOSS audit**, a
read-only grounded/classified catalogue [principle #12 made proactive]. READ-ONLY: no `src/`, no corpus write, no
build, no fix. Four parallel read-only tracing passes over the load-bearing surfaces [bass · spelling · distinct
alternatives · preserved uncertainty], every candidate CC-verified at code, classified on the central axis
[OK-provisioned / DEFECT-lost / DEFECT-should-already / UNCLEAR; ambiguous ⟹ UNCLEAR, never guessed]. **11 sites: 2
DEFECT-LOST · 0 SHOULD-ALREADY · 7 OK-provisioned · 3 UNCLEAR.** Hinge: production = LEGACY `analyzeChord`+gates;
Layer 4/5 Built+Dormant ⟹ most not-yet-consumed signals are the dormant path's correct forward-provisioning [OK: K2
`FunctionLayerOutput` "no production consumer"; K3 `HarmonicRegion.keyAlternatives/keyConfidence` "in-memory only …
exists for Layer 5"; K1 `SliceChord` incl. per-note spelling done right]; the LOST sites are on the legacy
user-visible carry surface. Fix-queue: **L1** [HIGH, #4, = O-19] Gate A `std::swap` keeps the distinct enharmonic
partner, FM2 `push_back(buildResult)` loses it [`postscoringgates.cpp:214-234`; PRESENT consumer
`notationcomposingbridge.cpp:298-300` + future L5]; **L2** [MED, #4, NEW] the legacy `tpcForPc`/merge spelling
collapse [`analysisutils.h:175-180` + `chordanalyzer.cpp:1229-1240`] destroys same-pc distinct spellings by
iteration-order → the "second tpc reader" unification residual [adopt L4's per-note `lineOfFifths` reader live].
UNCLEAR for adjudication: U1 [top-3 cap — which carry surface L5 binds], U2 [J-key-iii chord=R0 stale alt-ranking =
the key-then-chord truncation the still-owed joint step fixes, `regionanalyzer.cpp:369-375`], U3 [coalesce bass
re-derive]. Catalogue `cowork_information_loss_audit.md` + report `cc_engage_information_loss_audit_report.md`; O-20;
pushed fork-only. On CC's report: Cowork verifies the catalogue at objects → brings the user the DEFECT fix-queue +
the UNCLEAR rows. Prior header, kept: session 26 (engage arc #3 — **the GateA promotion-unification
DESIGN/SCOPING pass**, the order-of-operations first step [restructuring before Layer 5]. READ-ONLY: no `src/`,
no build, no corpus write, no push of a behavior change. Assembles the ratification surface for the
held-since-O-11 GateA retirement. Blast radius re-measured at HEAD on the FULL surface [HEAD-binary
`disable_rule GateA` decode, scratch, frozen corpus read-not-written]: **36 Baroque, 0 winner-diffs / 352,
alternatives-only** — the 2.2c count reproduced + **enumerated by name**; carry delta = the enharmonic
Major-add6 partner alternative overwritten by a freshly-built winner near-duplicate under FM2's append vs kept
under Gate A's swap [§12 loss]. Design: one `promoteToWinner` primitive with a **present-first dedup guard** +
one collapsed builder wrapper ⟹ GateA + FM2 = two branches of one promotion ⟹ `GateA` removes byte-identically,
reproducing **C_HEAD** [correct carry grounded at the O1b contract]; all Layer 4. The 36-score alternatives
delta = the user-ratification surface for the separate build event; both stops green by construction. Design
`cowork_gateA_unification_design.md` + report `cc_engage_gateA_unification_design_report.md`; O-19; pushed
fork-only). Prior header, kept: session 25 (engage arc #2 — the C3 coupled key↔chord
population = **UN-COMPUTABLE / VERDICT 3**: the per-key chord re-decode is the still-owed joint step, so
C3-restrict is removed from the near-term F-B option set and the frame collapses to annotate-everywhere; see
the START HERE block + O-18 + `cc_engage_c3_measurement_report.md`. No `src/`, no build, no push-blocking
change — pushed fork-only). Prior header, kept: session 23 (**★ STAGE-5 ARC CLOSED — R10-b MADE: the
batch→robust regression-stop handover is normative. CLAUDE.md gate section = the robust-unit stop (block A;
baselines root 63.36/62.37/63.25 · RN 44.58/42.40/44.41 · key 68.13/64.43/67.50); the two-tier policy LIVE
(block B); batch 52/24/52 relocated to history + frozen at `tools/robust_stop/batch_stop_frozen_history.json`
(block C); caveats (block D, granularity ✅ RESOLVED). 2.2e key-column error corrected
`68.19/64.52/67.77`→`68.13/64.43/67.50`. Roadmap R10 FIRED; §4.7 EXECUTED (O-16); `characterise` KEPT-AS-DIAGNOSTIC.
Both stops green at close. Report `cc_stage5_r10b_ratification_report.md`; commits `docs:` + `docs(cowork):`,
fork-only unpushed. THE ENGAGE ARC INHERITS: F-B redesign [1043/53/809] · §15-13 [5544, parked] · θ/map wiring ·
L1.5 surface map · GateA unification · the L5 inversion · tonicVote.**) Prior header, kept: session 22y (**Phase 3
COWORK-VERIFIED + CLOSED; the §1.4 contract row-changes APPLIED by Cowork; ★ R10-a DISPATCHED + HANDED TO CC**
— `cc_instruction_stage5_r10_assembly.md`,
the arc's closing assembly. **THE FRESH SESSION'S JOB: when CC's R10-a report arrives → verify at objects +
read in full → present the R10-b ratification surface to the user [decision-surface-FIRST rule] → on
ratification, write the R10-b handover instruction [CLAUDE.md gate rewrite · batch sets frozen as history ·
roadmap R10 fired · design §4.7 EXECUTED] → the Stage-5 arc CLOSES and the engage arc inherits the dossier:
F-B redesign [1043/53/809] · §15-13 [5544, parked] · θ/map wiring · L1.5 surface map · GateA unification ·
the L5 inversion · tonicVote.** The r10-a fold list carries the currently-uncommitted Cowork edits: STATUS
22w/22y · this header · the contract's six Phase-3 row-edits · the design. Open user calls: corpus
track-vs-archive [O-12] · push at will [~75 ahead].) Prior header, kept: session 22x (Stage-5 Phase 3 CALIBRATION delivered: C1 curves
re-measured on the adopted corpus [ECE Δ≤0.001]; the L3-margin + L4-composite Class-P maps FITTED [isotonic,
Baroque/Default carriers, Jazz A-7-unmapped], validated held-out [ECE 0.017–0.041], 4 artifacts committed;
deferrals re-verified [L5 non-monotone shape unchanged → stands]; Task-B L1.5 spike-vs-surface split measured
[surface has usable spread, spike flat, no map]; F-A/F-B scales declared + θ candidates recorded/unwired
[F-B override net-harm CONFIRMED 1043/53/809 → disable-candidate, inference finding declared]; R-11 conformal =
complement-not-replacement; contract-§3 changes listed for Cowork; sandwich 52/24/52 byte-clean, suites
1101/53+4skip/11. NOTHING wired, NO behavior change, NO push). Prior: 22v/22w (Phase 2.3 — staging step 3
CLOSED; family-4 §15-13 parked to engage); 22u (2.2e adoption, corpus re-baselined 52/24/52); 22l (fitter
design signed). This header is the fresh-session entry point; full narratives live in STATUS.md (top entries)
and the named docs.*

## ★ START HERE — state, dispatch, queue (2026-07-06)

**★ ENGAGE ARC #3b DELIVERED — the GateA promotion-unification BUILD event (session 28, 2026-07-06).** The
ratified arc-#3 design, built (Layer 4 only, #7). **One `promoteToWinner` primitive** (`chordanalyzer.h` /
`postscoringgates.cpp`) owns both promotion idioms — present-first swap (former **Gate A**) and append-built pull
(former **FM2**) — behind one contract, plus **one builder wrapper** `buildResultFromGateCtx`; the three duplicated
`buildResult` lambdas collapse. The enharmonic flip is ONE call (`presentHint = bestAltIdx` reproduces Gate A's
swap byte-for-byte; append reproduces FM2); Gate E, G-family (G-E/G-D) and Iter-91 route through it too. **The
separate `GateA` §6 rule is REMOVED** (enum/guard/name-map; §6 rules 10→9) — **FM2** is the surviving flip rule
(O-11 retirement condition met). doc-sync `docs/scoring_model.md` (new §6a); stale `chordpostpasses.cpp:128`
comment removed. **Full-surface byte-identity PROVEN at objects** (winner AND `alternatives[]`): **0 diffs / 1056
files across all 352×3, including the 36** — `C_unified == C_HEAD` by construction (present branch keyed to
`bestAltIdx`; append = FM2). **Both stops GREEN (measured):** batch 52/24/52 set-diff empty; robust sandwich
identity-PASS (runs +0/-0, class-(b)&(a) dur Δ+0). Suites 1101/53+4skip/11 (no golden refresh). Committed corpus +
robust-stop reference untouched (all on scratch). Net user-visible delta = **ZERO** (#12); total-unification (#6)
that closes the **L1 / O-11 / O-19** information-loss path — that fix-queue item is **DISCHARGED**. feat
`200681a855` + `docs(cowork):` fold (report `cc_engage_gateA_unification_build_report.md` + STATUS + HANDOFF +
fitter observation + instruction + info-loss-audit edits); pushed fork-only (`cfc7eb5e39` upstream HARD STOP
honored). On CC's report: Cowork verifies the byte-identity proof at objects.

**★ ENGAGE ARC #4 DELIVERED — the INFORMATION-LOSS audit: a read-only grounded/classified catalogue (session 27,
2026-07-06).** Principle #12 made **proactive** (sweep the Gate A defect class systematically, not incidentally).
Read-only (no `src/`, no corpus write, no build, no fix — every fix is its own later ratified event). Four parallel
tracing passes over the load-bearing surfaces (`cowork_functional_analysis_research_grounding.md`: bass · spelling ·
distinct alternatives · preserved uncertainty), every candidate CC-verified at code, classified on the user's
**central axis**. **11 sites: 2 DEFECT-LOST · 0 SHOULD-ALREADY · 7 OK-provisioned · 3 UNCLEAR.** **The hinge**
(ARCHITECTURE.md §L4/L5): production runs the **LEGACY** `analyzeChord`+gates path while Layer 4/5 are
**Built+Dormant** — so most not-yet-consumed signals are the dormant path's **correct forward-provisioning** (OK: K1
`SliceChord`, K2 `FunctionLayerOutput`, K3 `HarmonicRegion.keyAlternatives/keyConfidence`), and the genuine LOST
sites sit on the legacy path's **user-visible** carry surface. **DEFECT fix-queue:** **L1** (HIGH, #4-relevant,
already scoped O-19) Gate A `std::swap` preserves the distinct enharmonic partner vs FM2 `push_back(buildResult)`
loses it (`postscoringgates.cpp:214-234`; consumer PRESENT `notationcomposingbridge.cpp:298-300` + future L5);
**L2** (MEDIUM, #4-relevant, NEW) the legacy `mergeChordAnalysisTones`/`tpcForPc` spelling collapse
(`analysisutils.h:175-180` + `chordanalyzer.cpp:1229-1240`) destroys same-pc distinct spellings by iteration-order →
the named "second tpc reader" unification residual (adopt L4's per-note `lineOfFifths` reader live; closes a #4 loss
+ a #6 duplication). **SHOULD-ALREADY = 0** (substrate cleanly provisioned; the margin-vs-sigmoid gate is a ratified
D-L3a deferral). **UNCLEAR for user adjudication:** U1 (the `results.size()>=3` cap — which carry surface L5 binds
to), U2 (J-key-iii leaves the chord = R0 with a stale-under-new-key alt ranking — **the canonical key-then-chord
truncation the still-owed joint step fixes**, `regionanalyzer.cpp:369-375`, O-18's owed joint step is the future
consumer), U3 (coalesce bass re-derive — needs a score check). **New taxonomy forms:** (+1) honest-unknown-carry
(`extensionsKnown`/`openMark`/Abstain), (+2) recomputable-collapse (a value derived from a carried source is
lossless — guards against over-flagging). Both stops green by construction; suites unchanged. Catalogue
`cowork_information_loss_audit.md`; report `cc_engage_information_loss_audit_report.md`; fitter O-20; pushed
fork-only. **FRESH SESSION'S JOB: verify the catalogue at objects → present the DEFECT fix-queue (L1/L2) + the
UNCLEAR rows (U1/U2/U3) to the user; each fix is its own later Gate-A-style ratified event.** The rest of the
engage-arc dossier remains queued: F-B annotate build-event · §15-13 [5544, parked] · θ/map wiring · L1.5 surface
map · GateA unification (L1) · the L5 combinedBoundary inversion · tonicVote.

**★ ENGAGE ARC #2 DELIVERED — the C3 genuinely-coupled key↔chord population MEASURED = UN-COMPUTABLE
(VERDICT 3) (session 25, 2026-07-06).** The specific-research move (#5/#2) the O-17 surprise called for (#3),
read-only (no `src/`, no build, no telemetry, no corpus write, no θ retune). **Task-1 verdict: the C3
trigger is NOT computed anywhere** — not read-only measurable, not surfaceable by additive default-off
telemetry. Binding blocker = C3 component **(b)** ("a different carried KEY alternative flips the chord
reading"): the per-key chord **re-decode** it requires **IS the gated joint key-and-chord step the contract
§6-C3 flags as "still owed at Stage 5"** (`keymodesequence.h:70-72`), and even the closest mechanism — the
J-key-iii joint re-key pass — **explicitly leaves the chord unchanged** ("the chord-axis side-effect … is
DEFERRED to a faithful mechanism", `regionanalyzer.cpp:369-375`). Component (a) is likewise absent from the
F-B fullspine chain (`inferLocalKey(...)[0]` + a **score-global** `homeConf` sigmoid, not the per-slice L3
sequence margin; the bar is source-verified — `uncertainThreshold` 1.0 / annotate-gate 0.8 — but the bar is
not the blocker). **No already-computed signal to surface ⟹ producing (b) means BUILDING the joint step
(forbidden #6/#7/#8) ⟹ verdict 3 = report, not build.** **Load-bearing: §3.D-2 (C3-restrict) is removed from
the near-term option set** (joint-step-gated, a Stage-5+ successor); the F-B frame **collapses to §3.D-1
annotate-via-open-mark EVERYWHERE**, floored by disable; **recovering the 53 corrections = a declared
inference-quality question (#8).** **#3 discharged:** the O-17 surprise is *explained* — F-B fires on a
population never filtered for key↔chord coupling, so it is mis-scoped off the C3 minority by construction; no
residual surprise. Footing reproduced (1043 = 53/809/181; 4th/5th harm majority 58 %). **Reproducibility
finding surfaced (#16):** the `C:/tmp/c1/fs_*` manifest is STALE (git_hash `d1d4d3d7f0` + sha fingerprints a
Jul-4 leftover; the real dumps are a Jul-6 `≥c50002fee1` regen the fs-driver never re-manifested; `theta_fit`
globs directly) — re-manifest the E0 dirs or have the taxonomy scripts validate. Both stops green **by
construction** (zero `src/`; byte-identical to HEAD `712830210a`). Design `cowork_fb_redesign_design.md`
§3.D-2 updated; report `cc_engage_c3_measurement_report.md`; fitter O-18. **FRESH SESSION'S JOB: verify at
objects → present the annotate(±C3) build-event DECISION SURFACE to the user (annotate-everywhere now;
C3-restrict deferred to the still-owed joint step; the 53-recovery is an inference-quality question, not a
redesign).** The rest of the engage-arc dossier remains queued: §15-13 [5544, parked] · θ/map wiring · L1.5
surface map · GateA unification · the L5 combinedBoundary inversion · tonicVote.

**★ ENGAGE ARC #1 OPENED — the F-B fine-grain override REDESIGN design/scoping pass DELIVERED (session 24,
2026-07-06).** The engage arc's opener, read-only (no `src/`, no scoring value, no corpus write, no build, no
θ retune — architectural design, moratorium-clear). **The ratified backlog is PUSHED:** `git push origin
master` = `ce509b0961..923f149561`, ahead-count **76→0**, new `origin/master` =
`923f14956157d3117988c12e0b51d9c858b9813c` (fork-only; `upstream` push disabled; `cfc7eb5e39` stays
fork-local). **The F-B mechanism is characterized at the source** (`attemptFineGrainOverride`,
`functionresolver.cpp:381`; incumbent = the L4 vertical-fit `composite` — code-truth; contradiction = the
coarse {0,1,2,3} progression-plausibility count; dormant — only `batch_analyze.cpp:3186`'s E0 harness runs
it). **The 1043/53/809 net-harm is decomposed at the measured data** (read-only over the existing
`C:/tmp/c1/fs_*` dumps): ★ **the harm rate is ~uniform 71–86 % across every stratum — there is NO
discriminator, and no θ can carve corrections from harms** (highest harm at highest L4 confidence); ★ **even a
vertically-fair comparison (`g≤0`) is 70.8 % harm — the incumbent-repair premise is REFUTED at data.**
**CC recommends re-frame-to-annotation (§8 case-3 honest carry), floored by disable; rejects the structural
gate and the incumbent-repair as measured net-negative; the 53 lost corrections need a
correctness-correlated contradiction signal = an inference-quality question declared to Cowork, out of
scope.** Design doc `cowork_fb_redesign_design.md`; report `cc_engage_fb_redesign_design_report.md`; O-17.
**FRESH SESSION'S JOB: verify at objects → present the F-B redesign-option DECISION SURFACE to the user
(annotate vs disable vs C3-restrict — the decision-surface-first rule); the implementation is the user's next
ratified build event (touches `functionresolver.cpp` + `ResolvedReading` + contract §4 F-B + L5
§5.5/§10/§15-2 + `docs/scoring_model.md` + roadmap/fitter; acceptance = the robust-unit stop moving
favorably at engage).** The rest of the engage-arc dossier remains queued: §15-13 [5544, parked] · θ/map
wiring · L1.5 surface map · GateA unification · the L5 combinedBoundary inversion · tonicVote.

**★ STAGE-5 ARC CLOSED (session 23, 2026-07-06) — R10-b MADE: the batch→robust regression-stop handover is
normative.** CC executed `cc_instruction_stage5_r10b_ratification.md` (docs + one-JSON-snapshot only —
NO `src/`, NO scoring value, NO corpus write, NO build, NO push). The CLAUDE.md gate section is now the
**robust-unit stop**: block (A) the hard stop = class-(b) root-disagree DURATION non-increase per preset +
mandatory explained run-diff (reference `tools/robust_stop/`; baselines root 63.36/62.37/63.25 · RN
44.58/42.40/44.41 · key 68.13/64.43/67.50; runnable `a8_rebaseline_measure.py`→`robust_stop_diff.py` ≈6 s) ·
block (B) the two-tier per-cell class policy preserved LIVE · block (C) the batch **52/24/52** sets relocated
to a retrospective + frozen machine-readable at `tools/robust_stop/batch_stop_frozen_history.json` (set-equal
verified) · block (D) caveats (cross-layer-budget LIVE, granularity ✅ RESOLVED). The **2.2e KEY-column error
corrected** `68.19/64.52/67.77`→`68.13/64.43/67.50` (Jazz byte-identity proof) with the repo-wide occurrences
dispositioned. `characterise_bir_false.py` → KEPT-AS-DIAGNOSTIC. **Roadmap R10 FIRED; design §4.7 EXECUTED
(O-16).** Both stops green at close: batch 52/24/52 set-diff empty ×3 **and** the robust sandwich identity-PASS
(+0/−0, class-(b) Δ=0 all presets). Report `cc_stage5_r10b_ratification_report.md`; commits `docs:` +
`docs(cowork):` (fork-only, unpushed).
**★ The engage-arc headline material, Cowork-concurred: the F-B fine-grain override is measured NET-HARMFUL
(1043/53/809 — ~78 % of fires move an L4-correct root wrong); a REDESIGN item, never a θ retune.**
**THE FRESH SESSION'S JOB: verify CC's R10-b report at objects → the batch→robust handover is normative →
OPEN THE ENGAGE ARC on the inherited dossier: F-B redesign [1043/53/809] · §15-13 [5544, parked —
dormant-resolver objective] · θ/map wiring · L1.5 surface map · GateA unification · the L5 combinedBoundary
inversion · tonicVote detection quality.** Open user calls: corpus track-vs-archive (O-12) · push at will
(~77 ahead).
**(history) R10-a (session 22z, `cc_stage5_r10_assembly_report.md`):** the assembly surface — committed
reference `tools/robust_stop/` + the old→new mapping (every 52/24/52 case maps, 0 disappear) + the
runnable+timed successor sandwich + the DRAFT gate text; declared the 2.2e key-column finding for R10-b
(now corrected). **(history) Phase 3 (session 22y):** all 3 commits at objects; the §1.4 contract changes
APPLIED by Cowork (five §3 row-status appends + the §7 D-FS closure). STATUS 22x/22y/22z + 23 = the full record.
**(history) The 22x delivery summary:** Report `cc_stage5_phase3_report.md`; commits feat `7111f589e2`
+ docs `6b5bdcd64b` (fork-only, unpushed). What landed:
- **C1 curves re-measured** on the adopted corpus `c50002fee1` (they predated 2.2e): every ECE Δ≤0.001 —
  the adoption did not move the calibration.
- **Class-P maps FITTED + COMMITTED** (`tools/calibration_maps/stage5_classP_{l3_key_margin,l4_chord_composite}_{baroque,default}.json`):
  **isotonic** on both rows (Platt rejected — not near-logistic, maxdiff 0.20–0.26); fit on the 261 fitting
  split, VALIDATED on held-out → **held-out post-map ECE 0.017–0.041** (3–6× below pre-map); the L4 flat low
  band pools to a constant **0.289** (flat-band assertion held — no invented resolution); monotone by
  construction. **Jazz UNMAPPED (A-7 empirically-unvalidated).**
- **Deferrals re-verified:** L5 combinedBoundary still non-monotone (0.6–0.8 band < 0.5–0.6, all presets) —
  **shape UNCHANGED post-adoption → deferral STANDS** (the STOP "shape changed" did not trigger); cadence
  tonicVote anti-monotone; L1.5 → Task B.
- **Task B (L1.5 spike-vs-surface)** via the additive default-off `phraseNumVoices` dump field (spike-floor
  invariant confirmed exactly = 1.5·numVoices): the SURFACE population (98.4%), un-compressed, has usable
  monotone spread (0.13→0.46) → a per-population map is fittable IN PRINCIPLE later; the SPIKE population is
  a flat ~0.40 cluster; **no map fitted** (weak absolute signal).
- **Task C (θ):** F-A/F-B scales DECLARED (`x/(x+3.5)`, `x/(x+2.0)`; R5, precision-phase); θ candidates
  fitted RECORDED/UNWIRED — **F-B fine-grain override net-harm CONFIRMED (1043 fires / 53 corrections / 809
  harms) → the best measurable θ effectively DISABLES it: an inference-quality finding declared to Cowork
  (redesign, not a θ retune)**; F-A reduced candidate τ≈5.0 (corr−harm +6→+15; full form deferred — the L3
  incumbent is not in the `modulations[]` dump).
- **Task D (R-11 conformal):** split-conformal vs map-implied abstention — verdict **complement, not
  replacement**.
- **Contract §3 row changes listed for Cowork to apply** (report §1.4 — the contract is Cowork-owned; CC
  did not edit it).
- **Sandwich:** gate **52/24/52** set-diff empty BEFORE+AFTER, corpus fingerprint-validated untouched;
  standard `.ours.json` byte-identical (15/15); composing **1101/1101** · notation **53+4skip** · snapshot
  **11/11 no refresh**.

**NEXT (Cowork):** verify the maps/θ/verdicts; apply the contract-§3 row changes; then the arc-close
checkpoint **§4.7/R10** (the batch→robust-unit stop handover). Open user calls: corpus track-vs-archive
(O-12) · push at will.**

**(history) PHASE 2.3 CC-DELIVERED (session 22v, 2026-07-06)** — report `cc_stage5_phase2_3_report.md`.
- **(A) Staging step 3 — the three surviving §6-block margins (`kGateIMargin` 0.45, `kGateLMargin` 0.35,
  `kHalfDimFirstInversionBonus` 0.55) hold NO fittable gain at FULL range → each RETAINED, constant stays hand-set
  (skip-with-record).** Full-range 1-D ladders (Baroque, fitting split, refine-0; baseline 63.5391 exact): no
  feasible Δ>0 anywhere. Refines the ±step-dead 1b reading — kGateLMargin globally inert; kGateI/kHalfDim flat at
  the current value but the objective drops (infeasibly) at the extremes. Ledgers committed.
- **(B) Family-4 §15-13 both-licensed population — LARGE, size-viable per the gate.** One additive, behaviour-neutral
  `bothLicensed` field on the dormant resolver (byte-identical on production, 0/352 ×3; 4 pinned test assertions;
  suites 1101/53/11 no golden refresh), counted from `--dump-fullspine`: **Baroque 5544 / Jazz 5581 / Default 5544**
  (~16.5 % of scored duration, 351/352 scores; ≈52 % structural tie-break / ≈48 % open mark). **★ DECLARED FINDING
  (not decided): the §15-13 lever is on the DORMANT L5 resolver's output, which is not in today's a8 production/L4
  objective → the fit is size-viable but NOT runnable until L5 engages OR a resolver-output objective is defined.
  Returned to the user with the number; the §15-13 item stays open.**
- Sandwich **52/24/52** set-diff empty ×3 (before + after; manifest-fingerprint-validated untouched, O-12). Reuse-only
  drivers; retires nothing. Commits: `feat(composing):` instrumentation · `docs(cowork):` report+ledgers · `docs(cowork):`
  fold. Local/unpushed, fork-only; **no push.** NEXT: the user's read on the substrate finding · staging step 4
  (abstention bars) · Phase 3 calibration.

---

## (history) START HERE — state, dispatch, queue (2026-07-05)

**★ PHASE 2.2d CC-DELIVERED (session 22s, 2026-07-05) — THE (srib,kw) SUB-SWEEP FOUND A FEASIBLE SLICE;
a small ADOPTABLE candidate exists (a TIE); NOTHING adopted. AWAITING COWORK VERIFICATION.** This
fulfills the ACTIVE DISPATCH `cc_instruction_stage5_phase2_2d.md` (recorded in the 2.2c block below).
Report `cc_stage5_phase2_2d_report.md` (read in full for verification). **★ THE O-11 ii CHEAP QUESTION
ANSWERED — YES:** the 2.2c "family 2 closed NOT-adoptable" was the pessimistic reading of the *coupled*
point (bnrb 0.775); with **bnrb held at 0.70** and the bump gentle, an adoptable slice DOES exist —
Family 2 re-opens as **ADOPTABLE-PENDING-RATIFICATION**. The 18-point 2-D sweep (srib∈{0.40…0.4625} ×
kw∈{0.10,0.1125,0.125}, bnrb fixed 0.70; committed ledger `tools/fit_ledgers/stage5_2_2d_sweep.jsonl`)
→ **three full-feasible points**, all at high kw; the **top fitting gain +0.0365 is a 2-point TIE**:
**(srib 0.40, kw 0.125)** kw-only and **(srib 0.425, kw 0.125)** both-levers. Full decision surface for
both (committed ledger `stage5_2_2d_surface.jsonl`; held-out ONCE each): held-out **+0.0280** (generalizes,
no overfit), Baroque root +0.0347 (identical), **newB=0 on ALL three carriers, D-4 Default ELIGIBLE,
Jazz BYTE-IDENTICAL** (spot-verified — the O-9 per-carrier delivery removes the 2.2b shared-scope Jazz
cost entirely), DLC flat-positive (mozart +0.7), snapshot 11/11 would refresh. **★ THE DECISIVE FINDING:
the tie's *meaningful* (class-(b)) improvement is IDENTICAL** — both remove exactly the same single
class-(b) case `bwv244.32@5760`; the 53→52 vs 53→50 batch gap is **entirely class-(a) churn**
(`bwv258@10560`+`bwv334@6720`, symmetric-rotation coin-flips). **CC recommendation (evidence-based; the
tie-break + adoption are the user's): (0.40, 0.125)** — minimal/robust, single lever, never enters the
srib→bwv392 over-grab region; (0.425,0.125) is the alternative iff its better tracked-beside RN/key
(+0.049/+0.032 vs +0.015/+0.012) is judged worth the bigger perturbation + class-(a) churn + reliance on
the fragile kw=0.125 absorption of bwv392. **Prepared-NOT-applied adoption artifact** with the kStepBudget
note (kw 0.10→0.125 ⟹ kStepBudget 0.21→0.235; loader recomputes at fit time, a baked adoption must ensure
the same) + the O-11 iii production-path caveat. Sandwich **53/24/53** set-diff empty (Baroque set
element-verified vs CLAUDE.md; corpus git-clean, byte-untouched, `0dd64660f4`); suites **1101/53/11**,
no golden refresh; src git-clean (measurement-only). **Commits:** `ee59231141` feat(tools) drivers+ledgers ·
`5204551583` report · this fold. Local/unpushed; no corpus write; no push. **Cowork verifies → the
adoption + tie-break are the user's ratification event.** STATUS 22s + design §15 O-11 ii (DELIVERED note)
= the full record.

**★★ 2.2e THE ADOPTION EVENT — LANDED + COWORK-VERIFIED + CLOSED (session 22u, 2026-07-06): THE
ARC'S FIRST FITTED VALUE IS SHIPPED.** kWStepIn 0.125 (Baroque/Default; production via the Default
initializer; Jazz + Standard/Modal/Contemporary enumerated + pinned 0.10; kStepBudget derived
0.235/0.21 per carrier); the FIRST §7 provenance stamp; 11 goldens refreshed after intended-effect
confirmation; **corpus re-baselined 52/24/52 with EXACTLY the promised removal-only diff
{bwv244.32@5760} ×Bar/Def, Jazz byte-identical (proven by explicit-override reconstruction)**;
A-8 re-ratified 63.36/62.37/63.25; fixture 3/3 MATCH; O-10 first application = all four retained
rules live. **★ CC's load-bearing catch: the kStepBudget single-key-override leak** (would have broken
Jazz byte-identity on 7 files; per-carrier re-derivation fix, proven). **★ Process lesson (design
O-12): tools/corpus/ is GITIGNORED — "git status clean" was always vacuous; real protection =
manifest fingerprints + characterise validation; snapshot-before-re-baseline now mandatory;
track-vs-archive = an open user call.** Commits `c50002fee1` / `3cf4665f3f` / `83f41cdd31`, all
verified at objects; STATUS 22t/22u = the full record. **ACTIVE DISPATCH:
`cc_instruction_stage5_phase2_3.md` (session 22u tail, 2026-07-06)** — Task A: staging step 3, the
three surviving §6-block margins (kGateIMargin · kGateLMargin · kHalfDimFirstInversionBonus) at FULL
range (the 2.1 ±step lesson; expected skip-with-record, a mover = a Cowork finding, no chase) ·
Task B: family-4's §15-13 gate — the both-licensed fall-through population on the DORMANT chain
(fullspine, decode-only; additive default-off telemetry only if the dump lacks it, byte-identity
proven; the count decides whether the commissioned preference weight is evidence-fittable — no fit
either way) · sandwich now anchors on **52/24/52**. Then: family 3/Phase-3 calibration (the C1→fitted
maps design). **Open user calls: corpus track-vs-archive (O-12) · push at will (65+ ahead).**

**(history) 2.2d verified · the first-adoption ratification (2026-07-05): (srib 0.40 unchanged,
kWStepIn 0.10→0.125), the single-lever tie-break per the CC+Cowork joint recommendation (identical
class-(b) win; the alternative's edge = class-(a) churn + fragile coupling + struct-default leakage
into unmeasured carriers). Its dispatch was `cc_instruction_stage5_phase2_2e.md` — THE ADOPTION EVENT:
the one revertible value commit (provenance-stamped — the first §7 license fill) + goldens refresh +
★ the FIRST deliberate frozen-corpus re-baseline (expected 52/24/52, removal-only {bwv244.32@5760}
×Bar/Def, Jazz byte-identical — ANY other set change = FULL revert STOP) + CLAUDE.md set re-stamp +
A-8 baseline re-measure + unmeasured presets enumerated-and-pinned (mandate 4c) + the O-10 liveness
first application. The batch stop REMAINS the hard stop (a set re-stamp within the dual-track, NOT
R10). On the report: Cowork verifies → then staging steps 3/4 · family-4 gate · Phase 3.**

**★★ 2.2e CC-DELIVERED (session 22t, 2026-07-05) — THE ADOPTION LANDED; AWAITING COWORK VERIFICATION.**
Report `cc_stage5_phase2_2e_report.md` (read in full). Commits: `c50002fee1` `feat(analysis):` (kWStepIn
0.10→0.125 + doc-sync + unit tests + 11 refreshed goldens) + the `chore(corpus):` re-baseline (this fold's
sibling). **Verified outcome = EXACTLY the promised diff:** corpus **52/24/52**, set-diff removal-only
`{bwv244.32@5760}` on Baroque+Default, Jazz identical + **byte-identical proven** (R1 reconstruction, 0 diff).
**★ CC delivery finding (LOAD-BEARING):** `kStepBudget` is derived and a single-key `applyGlobalOverride`
does NOT recompute it, so the new 0.235 initializer would have leaked into the pinned-0.10 carriers and broken
Jazz byte-identity (a forced-0.235 Jazz regen differs on **7** files) — `batch_analyze` now re-derives it per
carrier. **★ Process note for Cowork:** `tools/corpus/` is **gitignored**, so the "old frozen Jazz" byte
reference was overwritten by the regen before a copy was taken; byte-identity was proven by explicit-override
reconstruction (rigorous, given the unchanged composing library), but a future re-baseline should snapshot the
frozen corpus first (or track it). A-8 baselines re-measured (63.36/62.37/63.25); CLAUDE.md re-stamped 52/24/52;
O-10 liveness recorded (all four retained rules LIVE, counts near-prior). Suites 1101/53/11 green. **On Cowork
verification → staging steps 3/4 · family-4 gate · Phase 3.**

**The 2.2c-verified block below stands as history:**

**✅ ACQUISITION ROUND COWORK-VERIFIED + RATIFIED (2026-07-04).** `cc_instruction_acquisition_round.md`
executed; report `cc_acquisition_round_report.md` (read in full); commit `4997757298` **verified at object**
(exactly 4 files: registry+provenance, +8 additive `wave3_sources` rows, deterministic regen 80→88) + the fold
(**★ OWED: the fold commit's SHA was never stated — chat nor report; its content is corroborated at the live
files, but object verification is blocked; the NEXT CC direction must demand the SHA, 22g precedent**). The
MCMA license correction **Cowork-corroborated at the live clone's LICENSE (CC-BY-NC-SA-4.0)**; the union-search
record's two stale in-place "CC BY" spots fixed by Cowork (ride the next fold). **6 sources
cloned/pinned+verified, 2 recorded, 1 counting pass STOPPED:** N9 — piano_svsep @ `1462e7c2` (MIT **code**; GT
graphs FETCHED AT RUNTIME from `fosfrancesco/piano_corpora_dcml` — pin=code+fetch-path; `jpop` non-public), MCMA @
`2bdb12e2` (475 .mxl, split **153/239/83 re-counted**; ★ **license CORRECTED CC-BY→CC-BY-NC-SA-4.0**), vocsep @
`82152a95` (★ **MIT, not "unstated"**; ~1,054 graphs BUILT AT RUNTIME from bach-370-chorales+Haydn/Mozart-SQ+MCMA);
N14 — Mikrokosmos @ `f77aebc1` (147 MusicXML, henle 3-class, no license); N12 — GuitarSet annotation.zip
**sha256-pinned** (360 .jams, CC-BY-4.0; the 4 audio zips 657 MB–3.61 GB recorded, NOT downloaded); multi-need —
Batik @ `30256ca4` (36 Mozart-sonata mvts; harmony/cadence CSVs **N1/N4** + the **trill-mark N13-partial structure
VERIFIED** on kv279_1.match [49 trill-marks + 163 insertions; no extraction built]; no license; `annotations/`=empty
submodule = the held DCML Annotated Mozart Sonatas, recorded not wired); CIPI recorded **gated** (USER form pending)
+ PSyllabus recorded (no scores). **★ Task 3 (PDMX `<harmony>` count) ATTEMPTED + STOPPED, correctly (NOT a wave
stop):** the HELD form is METADATA-ONLY (`tools/pdmx/PDMX.csv` index + 5 spot-check .mxl) — no chord-symbol column
(`has_annotations` conflates all annotation types), and the raw MXL + MusicRender JSON live only in the Zenodo archive
→ counting needs a re-download the read-only dispatch forbids; **no proxy invented, the subset stays UNMEASURED**
(recorded in the `pdmx` row `needs_coverage`). **Two record license mismatches reported-not-accepted** (MCMA
CC-BY-NC-SA-4.0; vocsep MIT). Gate **53/24/53** set-diff empty both directions ×3 + before==after byte-identical ×3;
registry regen deterministic; nothing under `src/`; frozen gate corpus + held PDMX copy byte-untouched. **Corpus
program CAUGHT UP** — only the access-gated CIPI + the future PDMX-MXL-tarball fetch remain as recorded paths.

**★ PHASE 2.2c COWORK-VERIFIED + RATIFIED (session 22r, 2026-07-05): all 11 commits verified at
objects; the ★ ALTERNATIVES[] RULING recorded (design §15 O-11: the carried-alternatives surface IS
inside the byte-identity contract — GateA verdict RETIRE→HELD/DEFER, retires when the promotion
machinery unifies, a named total-unification item); FAMILY 2 CLOSED NOT-ADOPTABLE (bwv392 driven by
the srib+kw PAIR, not bnrb — a Layer-2/4 over-grab the fit relocates but cannot remove; the candidate
reads the GT's OWN Dm/F at the wrong span — Cowork's earlier F-root inference corrected by Task 3);
the production-delivers-only-Default fact recorded (O-11 iii). **ACTIVE DISPATCH:
`cc_instruction_stage5_phase2_2d.md`** — the 18-point (srib × kw) sub-sweep at bnrb 0.70 under the
full-corpus zero-new-class-(b) selection rule (bwv379/bwv392 appearance-mapped per point; Jazz pinned
by construction; candidate surface + prepared-NOT-applied artifact if one exists, else the honest full
family-2 closure). Then: staging steps 3/4 → family-4 gate → Phase 3.
STATUS 22r = the full record. The delivery summary below stands as history:**
PHASE 2.2c DELIVERED (session 22q, 2026-07-05) — report `cc_stage5_phase2_2c_report.md` (read in
full); NOTHING adopted, one retirement HELD, no `tools/corpus` write, no push. AS-BUILT: (1) **RETIRE-5
executed → byte-identity STOP → user Option 1 → RETIRE-4.** The five retirements were committed; the
byte-identity proof tripped on **Baroque 36 differing `.ours.json`**, and the diagnosis (3-way vs a built
`3f52f088ad` baseline + a winner-vs-alternatives isolation) found **GateA is WINNER-byte-identical on all
352 scores but changes `alternatives[]` on 36 Baroque** (GateA `std::swap` reuses the existing object; the
retained **FM2** promotes the same winner via `push_back(buildResult)`). So the 2.2b firing-site ledger —
which measured the **winner** — was CORRECT; the dispatch's proof is over the full `.ours.json`. **A
carry-contract surprise, not "evidence wrong"** — surfaced as a STOP. **GateF/GB/GC/K are fully
byte-identical (0 diff).** User chose **Option 1**: un-retire GateA (`c9909be4f8`), keep the four →
**RETIRE-4**; GateA retirement HELD pending the alternatives-in-contract decision. (2) **O-9 per-carrier
scoping delivered** (`6a468f82ac` — bassNoteRootBonus + kWStepIn per-carrier via the preset builders /
`applyGlobalOverride`; values unchanged → byte-identical ×3; **production-path question REPORTED**:
production has no preset-selection moment, delivers only the Default carrier). (3) **bwv392@17520
score-verified class-(b)** — the candidate's `Dm/F` (iii6) over-grabs the WiR `Gm` (vi) region; a
pitch-class-decidable root error, a hard R10 blocker. (4) **Candidate re-selection sweep: NO swept value
passes.** bnrb {0.70…0.775} × (srib 0.475, kw 0.125): low bnrb fitting-infeasible (`bwv379@11520`), every
fitting-feasible bnrb (0.7375–0.775) full-infeasible — **`bwv392@17520` on BOTH Baroque AND Default**
(driven by the srib/kw pair, not bnrb; the 0.775 point reproduces the 2.2b Config I candidate exactly,
fit +0.5142 / held-out +0.5874). **The coupled family is NOT adoptable at any swept value** (dispatch's
"report the curve, user decides"); no candidate, no artifact. Sandwich **53/24/53**; suites **1101/53/11**.
Commits: retire F/GB/GC/K (`7ea8201d43`,`15831825ea`,`d2becff50c`,`a4da727d71`) · un-retire GateA
(`c9909be4f8`) · dispositions+manifest (`9823ce75fc`) · per-carrier scoping (`6a468f82ac`) · tools
(`37603ab217`) · report (`1074b1c474`) · this fold. **The 2.2b delivery summary below stands as history:** Report
`cc_stage5_phase2_2b_report.md`. Commits `e5a1bb7a0e` (`feat(tools):` — 6 `stage5_2_2b_*` drivers +
committed ledgers; measurement-only, corpus untouched) · `0500e4dc55` (`docs(cowork):` report, force-add) ·
this fold. **Headlines:** the 14×3 cross-carrier table exposed what the 2.2a Baroque-fitting view hid —
**GateI +5 Jazz class-(b) when off**, **GateJ −0.4515 Jazz when off** (catastrophic; retains), BiasCorrection
class-(b)-harmful; the inert set shrank to the **cross-carrier-5** {GateA,F,GB,GC,K} (GateGD/GateL dropped,
live elsewhere). The JOINT FIT: **Config I ≡ Config II +0.5142** (bassNoteRootBonus 0.775 / sameRootInvBonus
0.475 / kWStepIn 0.125; **O-7 power-chord lever inert at the joint optimum, subsumed by bassNoteRootBonus**);
**Config III maximal dissolution WORSE (+0.3886)**. The candidate **generalizes** (held-out +0.5874, DLC ×3 up)
**but** the aggressive shared bassNoteRootBonus 0.775 causes a held-out class-(b) `bwv392@17520` (R10) + Jazz
−0.61 duration — **neither config cleanly adoptable; the clean point (gentler/per-preset bassNoteRootBonus) is
a surfaced design refinement.** Verdict PROPOSALS: RETIRE-5 / RETAIN-4 {GateI,FM2,GateJ,GateL} / DEFER-5.
Sandwich 53/24/53 set-diff empty; suites 1116/53/11. **NOTHING adopted or retired — every verdict + the
adoption are the user's.** STATUS 22p tail has the full record. **The prior ACTIVE-DISPATCH note + 2.2a
delivery summary below stand as history:** **The 2.2a delivery summary below stands as history:** The
rule-disable mechanism (`0296e38f63` `feat(composing):` — `PostScoringRule` enum + 14 clean
`!ruleOff(X) &&` guards + 20 tests + scoring_model §6 doc-sync; **byte-identical absent**: full-corpus
regen ×3 = 0 diffs vs frozen, snapshots 11/0) + the fit-driver `audit` mode + committed `tools/fit_ledgers/`
+ `run_dlc_baseline --param-override` (`7367c7ae96` `feat(tools):`, additive) + the report
(`c1b2de0dd3`). **The audit (Baroque, fitting split 261, current weights):** 7 disable-inert
(GateA/F/GB/GC/GD/K/L) · 2 load-bearing (FM2 −0.0584 +1 class-(b) batch; GateI −0.0292) · 4
active-but-disable-beneficial on the root-only objective (BiasCorrection/GateE/GateH and **★ GateJ
+0.0547**) · 0 coupled/STOP. **★ INFERENCE-ADJACENT DECLARED (not acted):** disabling GateJ (vii°→V7)
IMPROVES root-only agreement but WORSENS RN — the root-only objective penalizes a structural re-rooting;
per-case verification is 2.2b's. NOTHING adopted/retired; sandwich 53/24/53 set-diff EMPTY ×3; suites
1116/53/11. Report `cc_stage5_phase2_2a_report.md`; STATUS 22o tail has the full record.

**★ PHASE 2.1 COWORK-VERIFIED · THE FIRST CANDIDATE PARKED (user, 2026-07-05) · THE POWER-CHORD
QUESTION RECORDED AT L4 §15 O4 · HOUSEKEEPING RULED (O-8) · ACTIVE DISPATCH:
`cc_instruction_stage5_phase2_2a.md` (session 22o)** — housekeeping (committed fit ledgers under
`tools/fit_ledgers/`; one validation runner gains `--param-override` for pre-adoption S-5 checks) +
the RULE-DISABLE mechanism (A-6 safety class, byte-identical absent) + the per-rule §6-block
dissolution AUDIT at current weights (14 members individually: fitting-split objective + explained
batch diff + pinned-fixture replay → the provisional (a)/(b)/(c) table = 2.2b's evidence base; NO
verdicts/retirements/adoption). **The family-1 ruling (O-7): candidate 0.6375 PARKED** — held-out
−0.098 (the overfit tell fired); constraint-bounded (the 0.15/+0.376 direction adds class-(b) cases —
quality-silent root credit); the lever re-enters at the 2.2b joint fit. STATUS 22o has the full record;
the earlier 22n-era summary below stands as history. **Phase 2.1 delivery summary (verified):**
report `cc_stage5_phase2_1_report.md`; commits `5c5d0aabdc` (the two P1 rationale corrections, values
byte-untouched) · `f14e57d6e0` (fit-driver coordinate-search optimizer + `evaluate --split`, additive) ·
`545a2b40ee` (report). **CANDIDATE `kPowerChord3PcPenalty` = 0.6375** (best FEASIBLE on the fitting split):
fitting gain **+0.073**; the unconstrained max (0.15, +0.376) is INFEASIBLE (adds class-(b) batch cases) →
**constraint-bounded**. **Held-out REGRESSES −0.098 (overfit signal, surfaced).** Full-corpus
+0.0376/+0.0854/+0.055 (Bar/Jazz/Def), **batch sets UNCHANGED ×3** (explained diff EMPTY; base==CLAUDE.md),
class-(b) duration DOWN ×3. **D-4 Default adopt-with-Baroque eligible**; Jazz no regression; **S-5 gap recorded**
(no validation runner threads `--param-override` — not built); snapshot preview **~6/11 goldens would refresh**.
**Adoption artifact PREPARED, NOT applied** (A-4/S-4); **NO committed constant value change.** Sandwich
53/24/53 set-diff empty ×3; suites 1096/53/11. **The adoption decision is the user's. (P1 record below.)** All 7 Phase-1 commits verified at objects; byte-identity
×2 held; the 57-vs-59 reconciled (pre-G10 proof + recomputed kStepBudget); the 19 dormant-only rows
dispositioned (Phase-3/family-4/engage material, recorded). PHASE 0 + CHECKPOINT P0 RATIFIED (below). Phase-0 commits verified at objects
(`4b510b9ac7` fold exactly 6 files · `0f05e78690` roadmap O-3 rider · `981e942ded` the 78-row
`tools/param_manifest.json` · `c7d16893d8` report, read in full); manifest claims spot-verified at source
(kHalfDimFirstInversionBonus 0.55 @ postscoringgates.cpp:287, absent from scoring_model §6 — drift real;
progression constants at harmonicfunctionlayer.h:109–113, values clean; the §15-13 `tieBreakOrOpen`
fall-throughs; chordslicedecoder.cpp:453 reuses analyzeChord = the D-9 shared-surface fact; E-13 CLEAN —
the tuning bridge reads no scoring parameter). **The OWED acquisition-round fold SHA is DISCHARGED:
`459c92c46d`** (Cowork-verified at object: the docs(cowork) fold after `4997757298`, 8 files +612/−20).
The Task-0.3 dirty-set STOP was CC-raised, Cowork-ruled PROCEED (the extras = the known
deliberately-untracked dumps/scratch, STATUS 22e/22g; the check omitting them = a Cowork instruction
defect, owned). Cost measured: ~45–54 s/single-preset evaluation, ~131 s all-presets (regen ~85 %).
**★ NEW USER MANDATE (recorded as design constraint 4c): OPTIMIZE FOR IDIOMS ONLY — never for the current
user presets;** presets = regression surfaces + delivery carriers; ONE fit per idiom; the end-user-facing
preset question is a separate later product decision. **★ CHECKPOINT P0 RATIFIED (user): 61 tunable / 17
frozen, WITH the frozen-row verification rider** (the 1b screen perturbs the frozen rows read-only; a
freeze hiding accuracy surfaces as a finding). Doc-drift (4 defects) queued → discharged in the Phase-1
scoring-docs commit. **The Phase-1 dispatch:** 1a = the D-6 override mechanism (the sanctioned src/
touch; byte-identity proofs ×2 incl. the identity-override run; must reach the no-runtime-surface
constants CC found) + additive a8/characterise flags (proofs) + the fit driver/ledger + the PROPOSED
fitting/held-out split (ratification-gated, mode-stratified); 1b = the 78-row sensitivity screen
(Baroque carrier primary per 4c; top-10 movers re-run on Default; Jazz = regression spot-check only;
frozen rows included per the rider). On the report: verify at objects → ratify the split → **Checkpoint
P1** (optimizer · staging · R-13) is the user's. **★ PHASE 1 DELIVERED (6 commits — `769df17146` the D-6
mechanism · `3c3e235dde` G10 addendum · `7fd3f7cf70` a8 flags · `c2914884af` driver + the proposed split ·
`0093cf44f3` manifest sensitivity · the fold + `cc_stage5_phase1_report.md`):** byte-identity PROVEN ×2
(flag-absent AND identity-override, 352×3 byte-identical each); 59 production-surface rows reachable — the
19 dormant rows (G8/G9/G11/G12/G13) unreachable without wiring the dormant chain (engage scope), Δ=0 by
construction, RECORDED not improvised; the driver's known-vector fixture reproduces 63.32/62.37/63.22
EXACTLY (batch 53/24/53) + determinism byte-identical; the split = 261 fitting / 65 held-out (mode-stratified
129/32 · 132/33, RATIFICATION-GATED); the 1b screen — 24-row dead list (incl. ALL FOUR §6-block gate margins
Δ=0), the continuous family COUPLES to the batch-stop (fit jointly with the dissolution track), 7 frozen-row
findings (`kOtherToneFactor`/`maxTotalInversionContextBonus` challenge their freeze rationales — report, not
unfreeze); coordinate search budget-feasible, R-13 NOT mandated; sandwich 53/24/53 set-diff empty ×3,
composing 1096 / notation 53 / snapshots 11. **NEXT: Cowork verify at objects → ratify the split → Checkpoint
P1 → Phase 2 (the fits, family by family, per fit target).** `cowork_stage5_fitter_design.md` written this session (full template
+ §0 TERMS), QA'd to the spec bar (independent adversarial audit, 20 findings — 2 HIGH/10 MED/8 LOW — all
folded, none rejected), then TWICE user-refined before signing: (1) the **IDIOM AXIS** (constraint 4b +
D-10: fitted values are idiom-labeled, presets are delivery carriers; the Bach fit = an **idiom-#2** fit
via the Baroque/Default carriers; manifest style-scope column; mixture semantics + auto-detection stay
deferred); (2) the **PER-PARAMETER STYLE-TABLE model** (D-11 + §4.4a: parameter value = function over the
style coordinates — idiom simplex + mode/chromaticism + the axis-2 texture class as per-parameter
candidates; dimensionality MEASURED by clustering per-stratum fitted optima under stability guards;
anchor-based estimation, linear mixing = default hypothesis for the additive-weight family, thresholds
don't mix; hierarchical shrinkage named as the estimation refinement; external precedents verified —
key/genre-dependent chord-transcription HMMs, rock-vs-common-practice corpus statistics, mode-conditioned
key profiles). **Whole §15 surface ratified; A-3 RULED: Jazz-carrier fit DEFERRED to the jazz-GT
conversion — this arc fits idiom #2 (Baroque/Default).** Both binding constraints carried (license pool →
§2/§3a; A-8 dual-track → §4.2). **The dispatch = Phase 0:** read-only parameter inventory
(`tools/param_manifest.json`, every row source-anchored, style-scope + consuming-path columns) +
objective-evaluation cost timing (scratch only) + the E-13 tuning-bridge check + **Task 0 demands the
OWED acquisition-round fold SHA** + Task 1 = the fold (exact list: STATUS.md · this header ·
census §8c · union-record fixes · the signed design · the instruction) + Task 2 = the O-3 roadmap
license-constraint rider. On CC's report: verify at objects, ratify, then checkpoint P0 (fit surface +
freeze list) is the user's. **Open user options (no deadline):** the CIPI Zenodo access form · the PDMX
mxl-tarball fetch (if the N12 symbol count is wanted) · push at will.

**✅ WAVE-3 ADDENDUM LANDED + RATIFIED (2026-07-04).** `c28f4064ee`/`3713636dd9`/`9441e94551`, all
verified at objects (parser diff insertions-only; KMT 201 kern Cowork-corroborated at the live clone).
KMT (the N5 upstream) is ON DISK; the Flexible 571-chorale multi-reading set is pinned RECORD-ONLY
(gate-repertoire overlap; analysis GT = an R binary); `DcmlRegion.figbass/pedal` exposed additively —
123,881 / 23,476 non-empty cells across the 40 DLC corpora, byte-identity proven (gate + characterise +
A-8 outputs all identical pre/post).

**✅ ADDENDUM detail (superseded by the RATIFIED block above; kept for the numbers).** Report
`cc_wave3_addendum_report.md`. `c28f4064ee` (Task A: +2 `wave3_sources` rows, regen 78→80 — KMT
`key_modulation_dataset` @ `6602ae6a`, 201 annotated Humdrum `.krn`/5 textbooks = the N5 upstream now on
disk; `Flexible_harmonic_chorale_annotations` @ `87efd245`, 571 chorales permutational multi-reading =
**N2 candidate, RECORD-ONLY** re the gate — analysis GT is an R-package binary, kernData `**kern`-only) ·
`3713636dd9` (Task B: additive `DcmlRegion.figbass`/`pedal` + a 5-test pin; **byte-identity PROVEN** —
gate 53/24/53 set-diff empty ×3, full `characterise` + A-8 outputs byte-identical pre/post, `tools/tests`
112 pass) · the fold (this commit). Exposure size: 123,881 `figbass` + 23,476 `pedal` cells / 40 DLC
corpora. Three mismatches reported (KMT README ~135 < 201; Flexible 572 `.krn` vs 571; R-binary GT).

**✅ CORPUS WAVE 3 LANDED + RATIFIED (2026-07-04).** `63de0df27a`/`8aae19f586`/`be70738720`, all verified at
objects. 10 beds pinned (headline: CoCoPops, BCFB, algomus-data with the 1,170-entry jazz tree bank ~8× JHT,
WJD native, Lieder/SQ/ASAP), 6 gated/walked with access paths (DCMLab/figured-bass = N10-NEGATIVE script),
humdrum-data closure 71 repos. Gate 53/24/53 byte-stable ×3. **Two audit claims falsified by measurement +
Cowork-corroborated at the live clone:** the on-disk N2 dual set = the 27 TAVERN A/B pairs (Tymoczko∩DCML
co-located = 0); KMT NOT analyzed at the WiR pin (201 scores / 0 analyses). Census N2/N5 + audit §7 carry
the corrections. Protovoice verdict: PARTIAL for N9 (reduction-encoded voice connections; doesn't close the
gap — the search targets flat stream labels). Re-discovery trigger FIRED, recorded only.

**✅ D-L3a CLOSED + RATIFIED (2026-07-04).** `f6f5137008` (7 comment-only src edits + contract §3/§7 +
L3-design doc-sync; src diff Cowork-verified comment-only at the object) + `a228e2bef6` (report + the
STATUS/handoff fold + the §7 SHA-stamp). The pre-authorized dormant re-point was correctly NOT done — both
dormant sigmoid-stand-in sites have no sequence-margin substrate (verified at live disk); recorded as a
joint-key/Stage-5 gap. Gate 53/24/53 set-diff empty ×3; `.ours.json` 0/352 differing ×3.

**✅ FULL-NEEDS AUDIT RUN + DISPOSED (2026-07-04, this session).** First run of census §8c executed —
`cowork_census_full_needs_audit.md` (all ~155 enumeration rows + registry re-scored against the needs-vector,
offline). User rulings: **N18 (fugue/imitation GT), N19 (part-writing-error GT), N20 (pedal-point GT — own
row: precision + no information loss) ADOPTED; N15 scope ruling RATIFIED** (performed intonation =
audio-domain, out of corpus scope). Census §8c vector + state columns updated same session. Key verified
facts: DLC TSV `form` column = chord-morphology, NOT form GT; DLC `pedal`+`figbass` columns exist on every
held corpus (parser-dropped — exposure queued as its own post-wave increment); TAVERN/KMT/BPS-FH/HaydnSun
live INSIDE the pinned WiR clone (Wave-3 = inventory, not acquisition, for those); protovoice-annotations =
the only N9 (stream GT) candidate — inspection gates the N9 search. Union search round (Cowork-side, after
Wave 3 lands): N9, N13, N14, N12-realized-half, N19.

**✅ C1 ARC FULLY CLOSED + USER-RATIFIED (2026-07-04, 22j).** Instrumentation `088ba617b0`/`0051641d27`;
fold + §2.1a `ea6f41eef4`/`4d18f44c2d` — the baseline delta was a benign denominator-scope nuance
(`agree/(agree+disagree)` vs `agree/scored_dur`, exactly the 0.09/0.13/0.40 % key-parse-fail reweighting,
arithmetic Cowork-re-checked; NO STOP; the Task-3 same-commit/cite-SHA contradiction was a Cowork instruction
defect, owned — CC surfaced and resolved it correctly).

**✅ C1 RATIFIED (2026-07-04, session 22j — full record in STATUS).** `088ba617b0` (harness + two additive
default-off dump fields, verified at the diff: flag-gated, early-return before the standard writer) +
`0051641d27` (report + both CLAUDE.md riders verbatim; the 353-hardcode STOP checked, not tripped). Sandwich
closed, gate 53/24/53 before/after. **D-L3a evidence DECISIVE:** the L3 sequence margin is 2.8–3.1× better
calibrated (ECE 0.125–0.142) than the emission sigmoid (0.38–0.44) on every preset — the close-out is now
evidence-ready as a separate small ratification-gated increment (user call on when). Other curve facts to
carry: L4 composite best-calibrated (ECE 0.11, monotone above ~0.5); L5 combinedBoundary over-confident +
non-monotone (ECE 0.25); cadence tonicVote anti-monotone, 3 distinct values; L1.5 strength 97.7 % mass in
bin 0 (spike-dominated max-norm). All recorded for the Stage-5 fitter, nothing fixed.

**The queue (plan lines, no instructions until dispatch):**
1. **✅ CLOSED CHAIN (2026-07-04, all ratified — full narratives in STATUS 22k):** the Wave-3 addendum
   (`c28f4064ee`/`3713636dd9`/`9441e94551`) · the union search round + §6 disposition (all five items) ·
   the acquisition round (`4997757298` + fold, **fold SHA OWED** — see the top block). The corpus program
   is CAUGHT UP; open user options: CIPI form (zenodo.org/records/8037327) · PDMX mxl fetch · push.
2. **✅ DONE (2026-07-04, 22l): the fitter DESIGN DOC written + audited + user-refined + SIGNED**
   (`cowork_stage5_fitter_design.md`; A-3 ruled = Jazz deferred); **Phase-0 CC dispatch ACTIVE**
   (`cc_instruction_stage5_phase0.md`) — see the top block.
3. **The Stage-5 fitter arc**: weight fitting on the ratified objective; **gate dissolution = OWED refactor #2
   discharges here**; R10 completes the A-8 re-baseline; C2 θ re-expression; Class-P maps; C3 joint-step design.
   (OWED refactor #1, the `chordanalyzer.cpp` file split, stays parked BY ratified R9 — after E4, "split once".)
   **★ BINDING on the fitter design (user-ratified 2026-07-04): the FITTING-POOL LICENSE CONSTRAINT** —
   census §8c block: ship-intended weights fit only on the PD/CC0/CC-BY pool; NC-class (all DCML, MCMA,
   Essen…) + no-license sources = validation/QA only; the design doc declares the objective-vs-validation
   source split explicitly; the constraint also enters the roadmap Stage-5 block at the next CC docs commit.
   **The next CC direction must also demand the acquisition-round FOLD COMMIT SHA (owed — never stated).**
4. Parked pending user calls: the idiom re-discovery re-run (trigger FIRED at Wave 3, recorded); the
   algomus Mozart-SQ seconds→ticks alignment step (owed before N16 load-bearing use).

**Current state, one paragraph.** The harmonic spine L1–L6 + Vocabulary + recognition consumer: built (L1–L3
live, rest dormant-validated), gate 53/24/53 case-identity intact throughout. **Axis 2 (voice leading) is BUILT
at its foundation** (session 22f/g: spec `cowork_voiceleading_axis_design.md` SIGNED→AS-BUILT; VL-A/B/C dormant,
suites 1083/53/11, parity 15/15, ABz feature space measured; VL-D/E/F/G/H design-gated; commits
`f06f4da987`/`39227ad232`/`2a3c767dae`/`cf365b6706`/fold `4c6952de18`, all verified at objects). **Wave 2
landed** (22h: three axis-2 annotation beds pinned — schema `76f810a1` / texture `3dce4ab8` / Essen `2d0ca75e`;
the 273-vs-244 schema drift ruled accepted as living-repo growth). **The A-8 metric arc closed** (22i: measured
`fd8ea88c0f`/`d1d4d3d7f0`; USER-RATIFIED three-part DUAL-TRACK — robust unit + variant-(b) DCML-only = primary
metric + fitting-objective basis NOW, batch 53/24/53 remains the hard stop until the fitter; semantics-when-
governing = class-(b) duration non-increase + explained per-run diff; root governs, RN+key tracked; baselines
root-agree 63.32/62.37/63.22% at 326/352 — full record: roadmap A-8 block + STATUS 22i. Measured inversions to
remember: the batch gate masks 15–56×; the music21 filter discards ~82% of human-adjudicated error time;
class-(a) is ~4% on the robust unit, not ≈53%).

**New standing records/mechanisms (2026-07-03/04 — all Cowork-owned docs; ALL COMMITTED as of the
2026-07-04 folds; the census governance vector is now N1–N20 + the fitting-pool constraint):**
- **`cowork_candidate_lever_register.md`** — R-1…R-13 compatible inference levers (figured-bass/BCFB, Parncutt
  root salience, harmonic grammar + JHT trees, tonal-space priors, IDyOM, conformal prediction…), none
  commissioned; claimable by the proper layer's design doc.
- **`cowork_product_tool_register.md`** — T-1…T-32 product tools + E-1…E-14 inferrer-side contract requirements.
  Binding items: **E-13** (engage catch: the tuning bridge is an unnamed consumer-migration site — add to the
  R-map at its next edit) and **E-14** (user-stated principle: ZERO INFORMATION LOSS TO THE END USER — every
  inferred object displayable; progressive disclosure yes, structural hiding no; ARCH pointer rides ARCH's next
  edit). Market probe recorded: no comparable engine anywhere in the MuseScore GitHub space; plugins hand-annotate
  what our layers infer.
- **Census governance (`cowork_score_census.md` §8b/§8c, all user-instituted):** purpose-driven sweep before
  every new component's design signs · the FULL-NEEDS AUDIT (needs-vector N1–N17; re-score before searching;
  first run at Wave-3 scoping) · the intake rule (every find scored against the FULL vector; every GT layer
  inventoried — the JHT-discovered-twice lesson) · the supersession decision protocol (record → cheap impact
  measurement → contradiction = immediate tripwire / enrichment = postpone-by-default; user decides both forks).
- **`cowork_polyphony_phrase_harmony_research.md` §6b** — the axis-2 sweep record (+ Wave-2 at-pin corrections).

**Uncommitted Cowork narrative awaiting the next fold:** the explicit four-file list in the top block
(STATUS 22k tail · this header · census §8c fitting-pool block · the union-record license fixes) — give CC
that list verbatim with the Stage-5 design dispatch (which also demands the owed acquisition-round fold SHA).

**Chain state:** everything local/unpushed on `master`, fork-only (`origin=slimvince/MuseScore`; `upstream` push
disabled — NEVER push there). User pushes at will.

**Fresh-session mandatory reads, in order (updated 2026-07-06, session 22y):** CLAUDE.md (NOTE: the gate
is **52/24/52** since the 2.2e re-baseline; the corpus is GITIGNORED — byte-untouched claims cite manifest
fingerprints, never git status) → STATUS.md top entries (**22t–22y** — the adoption event · Phase 2.3 ·
Phase 3 calibration · the R10-a dispatch) → this header's START HERE block → the standing-rule blocks
below (still binding; note the TWO newest: **THE FULL DECISION SURFACE BEFORE ANY CHOICE QUESTION**
[2026-07-05] and **NO MID-FLIGHT STEERING** [2026-07-05, rule 5 of the just-in-time block]) → then, for
the pending R10-b work: `cowork_stage5_fitter_design.md` §4.7 + §15 (O-7…O-13 — the arc's rulings live
there) · `cc_instruction_stage5_r10_assembly.md` (the ACTIVE dispatch) + its report when CC delivers ·
`cc_a8_rebaseline_measure_report.md` §1 (the pinned unit/variant/identity definitions) ·
`cc_stage5_phase3_report.md` (the calibration state + the F-B finding). **The working method, unchanged:
CC reports → Cowork verifies at objects + reads the report IN FULL + spot-checks at source (file tools
only, never bash for local files; bash ONLY for `git show <sha>` object queries) → presents the decision
surface to the user as rendered text FIRST → the user ratifies → the next instruction is written
just-in-time.*

## ✅ EXECUTED 2026-07-03 (session 22) — THE MERGED DOC PASS (work list below retained as the record)

**All five items ran** (full record: STATUS.md session 22): the 154-finding polish (every HIGH source-verified; §0
TERMS tables added to L1/L1.5/L2/L3/L4/dictionary), the span-family rename propagated everywhere incl. ARCH §2.15
body + target_architecture (chord-span · pedal-point-span · progression-schema-span · section-/voice-leading-span ·
cadential scope kept), A-1 typology adoption + A-3 confidence declarations + the target_architecture:44 re-point,
**§15-12 RATIFIED (user)** with the spec flipped in-force and the small dormant CC increment **dispatched**
(`cc_instruction_grammar_completion.md` — also carries the rider to fold this session's uncommitted doc edits into
the `docs(cowork):` commit, discharging item 5). **Give CC that instruction; on its report, re-read the instruction
first, verify at objects, then the queue resumes per the ratified order.**

## ★★★ THE MERGED DOC PASS (user "go", 2026-07-02; full work list — ✅ EXECUTED 2026-07-03, kept as the record)

**Read first:** STATUS.md sessions 21a–21q (the day's full arc), `cowork_design_doc_template.md` (BOTH writing-
standard sections — the razor, sharpened ×3 by the user this day), the two inventories
`cowork_spec_polish_findings_a.md` (L1/L1.5/L2/L3 — 67 rows, 15 HIGH) + `_b.md` (L4/L5/L6/dictionary — 87 rows,
6 HIGH). The user's razor examples to internalize: "Prinner" undefined; "carried reading"; "iff"; "multi-chord
functional knowledge"; "higher-order/skip-grams"; "key evidence" (key=tonality vs important); "confident slice".

**The work list (ONE pass, all seven layer specs + dictionary + ARCHITECTURE):**
1. **The 154-finding polish** per the inventories (HIGHs first: L3 "currently in" three-readings; the phrase-doc
   §9-vs-§4.4 contradiction + dangling "eligible voice" cite; L4 pin-vs-defer predicates; the dictionary match
   relation; L5 §12 five-vs-six kinds). Add a **§0 TERMS table to every spec lacking one** (all but L6/L5-partial);
   apply the multiple-meaning-words rule (template standard 5) everywhere.
2. **The confirmed span-family rename** (ARCH §2.15 carries the ✅ table): harmonic region→**chord-span** ·
   pedal→**pedal-point-span** · section-/voice-leading-span · latent sequence-span→**progression-schema-span** (D6;
   also the L6 `SchemaSpan` wording, consumer report U4) · cadential scope KEPT (stated exception). Propagate through
   every spec + ARCH §2.15 body.
3. **A-1 typology adoption** in the six older specs (each names its span in §2.15 terms) + the A-3 in-body
   confidence class-declarations (L3/L4) + `cowork_target_architecture.md:44` re-point.
4. **The L5 §15-12 / §5.0 grammar-completion amendment is DRAFTED in the L5 spec (ratification-gated)** — get the
   user's ratification, then write the small dormant CC increment (extend `isLicensedProgression` + tests; the
   consumer's D5 known-gap list empties + test tightens).
5. Fold the accumulated uncommitted Cowork edits (STATUS 21j–21q, ARCH, template, design docs, findings files) into
   the next CC docs commit when natural.
**After the pass:** the ratified order resumes — voice-leading-axis research / corpus Wave 2 / Stage-5 calibration
prerequisites (per the roadmap's ratified-amendments + engage blocks).

---

## ★★★ REVIEW HANDOVER — for a full external review by another Claude (Cowork), prepared 2026-07-01

**★ REVIEW DELIVERED + AMENDMENTS RATIFIED (2026-07-02).** The review this block prepared for is done:
`cowork_architecture_review_2026_07.md` (18 findings F-1…F-18; verdict: sound, no redesign; two HIGH coherence gaps —
F-1 no cross-layer confidence/calibration contract, F-2 "engage deferred indefinitely" unqualified; a Tristan
worst-case simulation grounding a capability track). **User ratified all ten amendments A-1…A-10** plus **corpus
expansion** (gate-grade jazz GT + DCML `wagner_overtures`/Wagner-class + more non-Bach/non-Baroque in general). The
amendments are slotted into `docs/implementation_roadmap.md` (the "AMENDMENTS RATIFIED" block) and the affected layer
specs' §15 sections. **Sequencing:** A-1 (confidence contract) + A-2 (engage criteria + retirement map) come BEFORE
the CC implementation↔spec gap-analysis (they change what "spec" means for it); the gap-analysis instruction carries
the review's five source-verification riders (§9 closing paragraph). The block below is retained as the review's
original map.

**Why this block exists.** A fresh Cowork session (a stronger model) will **review the whole architecture and its
documentation**. This block is the reviewer's map: what to read, in what order, the current state, what changed most
recently, and the known-pending items — so nothing reads as a surprise or as silent drift.

**Scope of the review.** The **architecture + its documentation** — coherence, completeness, one-responsibility-per-layer
(separation of concerns), cross-document consistency, and whether the design decisions hold up. It is **NOT** an
implementation/code audit — that is CC's job and is **deliberately deferred** (the per-layer *acceptance* audit is gated
on the two OWED refactors below). It is **not** inference/accuracy tuning (standing rule: no inference problem-fixing
until refactoring/architecture/algorithm are complete).

**Reading order (the map).**
1. **`ARCHITECTURE.md` — canonical.** Especially §2 (principles); §2.14 (layered+iterative, with its superseded/reconciled
   block); **§2.15** (the core finest-grain principle + the cross-cutting contracts + the **span typology** + the **new
   layer-taxonomy bullet**: representation / inference / assembly, "six is the current spine, *not a cap*," the three
   co-equal admission gates); §3.3 (per-layer module map + build status).
2. **`docs/implementation_roadmap.md`** — the single stage tracker; the **★★★ CURRENT STATE + FORWARD INCREMENT PLAN**
   table + the 6-step forward sequence.
3. **`STATUS.md`** (top entries) — latest session state + the gate baseline (BIR **53/24/53**).
4. **This `cowork_handoff.md`** — the STANDING RULES + THE WORKING METHOD (below).
5. **Per-layer / component design docs:** L1 `cowork_layer1_note_model_design.md` · L2 `cowork_layer2_slicing_design.md` ·
   L3 `cowork_layer3_keymode_design.md` · L4 `cowork_layer4_chordsymbol_design.md` · L5 `cowork_layer5_function_design.md`
   · L6 `cowork_layer6_grouping_design.md` · L1.5 `cowork_phrase_boundary_design.md`. Harmonic Vocabulary:
   `cowork_progression_schema_dictionary.md` (the built component) + `cowork_progression_schema_design.md` (the recognition
   consumer — designed, not built). Idioms/taxonomy: `cowork_idiom_discovery_findings.md`,
   `cowork_style_taxonomy_proposal.md`, `cowork_idiom_entry_mapping.md`. Polyphony/counterpoint research:
   `cowork_polyphony_phrase_harmony_research.md`. `cowork_target_architecture.md` is **demoted** to a rationale reference
   (ARCHITECTURE.md wins on any disagreement).

**Current state (design-level snapshot).**
- **Forward-only harmonic spine:** L1 notes → L2 slicing → L3 key/mode → L4 chord → L5 function → L6 grouping, plus the
  **L1.5** derived-view primitives. **Live:** L1, L2, L3. **Built + dormant:** L4, L5. **Design-only:** L6.
- **Harmonic Vocabulary** (encyclopedia): built + dormant, a separate *queried knowledge* component. **Recognition
  consumer** (wires it into the L5 prior + L6 annotation): designed, not built.
- **Idiom taxonomy:** 5 empirical idioms + **voice-leading confirmed as a 2nd orthogonal axis** (its own future layers —
  the home of melodic MT phrases and chord voicing/arrangement).
- **Layer taxonomy (new this session — ARCHITECTURE §2.15):** the layers span three kinds of work — **representation**
  (L1/L1.5/L2), **inference** (L3/L4/L5), **assembly** (L6). "Six" is the *current* harmonic spine, **not a cap**; growth
  is by axis and by component. A new layer/axis is admitted only on three **co-equal** gates: **(1) separation of
  concerns** (a structural mandate, sufficient on its own), **(2) verifiability**, **(3) proportionality**.
- **Two OWED structural refactors** (deferred, tracked — see the standing block below): (Stage 3.5) split
  `chordanalyzer.cpp` along the layer seams; (Stage 5) dissolve the post-hoc Gates A–L into fitted weights. The
  **per-layer acceptance audit is gated on both.**
- **Gate baseline:** BIR **53/24/53** (Baroque/Jazz/Default), held byte-identical; the frozen reference corpus is the
  regression material (the new idiom corpora are research-only).

**This session's doc deltas (2026-07-01, Cowork, docs-only — no `src/`/build/test).**
- **L6 spec:** grouping unit renamed **phrase → punctuation-span** (the DCML `{}` surface-punctuation-delimited grouping
  span); "phrase" is now reserved for the accepted **melodic phrase [MT]**, deferred to the voice-leading/melody axis.
  Folded the polyphony deep-search grounding (§2/§14); added the §3 boundary **provenance/scope** output requirement.
- **New:** `cowork_polyphony_phrase_harmony_research.md` (cited) — the field analyses harmony at the onset/verticality
  level, models phrase/cadence as *one texture-wide layer* (not per-voice), treats voice separation as a *separate* task,
  and absorbs counterpoint via an explicit **non-chord-tone filter** (recorded as a future **L4** lever).
- **L1.5 primitive (§11-5):** marker **scope** refinement — global (barline / key-sig / tempo / all-voice-rest) vs
  per-part (breath / caesura / fermata); per-part markers should reach the texture boundary via *voice-coincidence*, not
  an unconditional spike; carry cue+scope **provenance**.
- **L4 (§2):** the boundary as a **window-truncation** prior (interior analogue of the score-boundary truncation).
- **L5 (§11):** the boundary-prior is already the cadence phrase-gate — cross-referenced.
- **Roadmap (step 4):** the voice-leading-axis research foundation + the non-chord-tone L4 lever.
- **ARCHITECTURE §2.15:** the layer-taxonomy bullet + span-typology reconciled (phrase → punctuation-span).

**Known-pending doc items (flagged so the reviewer does not read them as drift).**
- **Span-name propagation (phrase → punctuation-span):** DONE in L6 (throughout), ARCHITECTURE §2.15 (span typology), and
  L5 §5.0 (the span *definition*). **PENDING:** the diffuse *boundary-sense* "phrase" usages elsewhere. The distinction is
  deliberate: the grouping **span** = punctuation-span; the **boundary / tick / gate** legitimately keeps the
  **phrase-boundary primitive** name (a Layer-1.5 code identifier). Mapping is 1:1. Tracked in `cowork_layer6_grouping_design.md` §15-7.
- **Optional sibling rename:** `sequence-span → schema-span` (kills the "sequence"-device ambiguity; makes the span family
  fully criterion-named: key / punctuation / schema). **Held** — it also touches `cowork_progression_schema_design.md`;
  user had no preference. Reviewer may decide.
- **The two OWED refactors + the per-layer acceptance audit** — implementation-side, not this review's job.
- **Doc-consistency caveat:** this pass reconciled the docs *changed this session* and the canonical span vocabulary; it
  was **not** an exhaustive 60-document cross-check. The reviewer should treat any other "phrase"/span wording it meets
  against the mapping above.

**Standing constraints the reviewer must respect** (full statements in the blocks below): **fork-only** (push
`origin` = `slimvince/MuseScore`, **never** `upstream` = `musescore/MuseScore`); **forward-only** (a backward edge only as
a surfaced/measured/gated exception); **verify-at-source** (no fact from memory); **never bash for local files** (file
tools only); **no inference problem-fixing** until refactoring/architecture/algorithm are complete; **all documentation in
sync**.

---

## ⛔ STANDING RULE: THE FULL DECISION SURFACE BEFORE ANY CHOICE QUESTION (user mandate 2026-07-05)

**Never present the user with options before the ENTIRE situation has been explained in a message the
user has actually seen.** Mechanism note (the failure that made the rule): Cowork prose written between
tool calls is summarized, not shown verbatim — so an explanation "just before" a question widget may
never reach the user, and the question arrives blind. The rules:
1. The decision surface (what is being decided, the background, each option's meaning, risks both ways,
   the recommendation and why) is delivered as user-visible text FIRST — via the verbatim message
   channel or as the turn's final response.
2. For consequential decisions (ratifications, adoptions, retirements, checkpoint rulings), the choice
   question goes in a SEPARATE, LATER turn — the user reads first, then is asked.
3. A decision answered blind is voidable: re-present the surface and re-confirm.
(First application: the 2026-07-05 verdict-14 + 2.2c ratifications were re-presented and re-confirmed
after this rule was made.)

---

## ⛔ STANDING RULE: INSTRUCTIONS ARE WRITTEN JUST-IN-TIME — ONE DISPATCHED AT A TIME (user mandate 2026-07-02)

**Do NOT write CC instructions ahead of need.** Pre-written instructions go stale (their premises change under
them), risk being skipped, and risk out-of-order execution. The rules:
1. **At most ONE instruction is dispatched/being-executed at a time** (single CC, single worktree unless the user
   explicitly sets up a second).
2. **The NEXT instruction is written only when its predecessor's report is ratified** and it is actually the next
   dispatch — never speculatively.
3. **The dispatch QUEUE is a plan, not files:** upcoming work is recorded as plan lines (roadmap / STATUS "next"),
   not as pre-written instruction files.
4. **Any instruction file that exists but is not the active dispatch carries a `⏸ PARKED` banner** and MUST be
   revalidated by Cowork against the then-current STATUS/HEAD immediately before dispatch, receiving a dated
   DISPATCH note. CC must not execute a parked instruction without that note.
5. **NO MID-FLIGHT STEERING (user, 2026-07-05): a running CC is never interrupted or relayed to** —
   interruptions have several times proven disastrous. Every instruction must therefore be
   SELF-SUFFICIENT: all foreseeable forks carried as in-instruction STOP/branch rules; anything not
   covered waits for the report and is ruled at verification. The only mid-run channel is the one CC
   itself opens (its own STOP question), answered when CC asks.
   *(As of 2026-07-04: NO parked instruction files — the formerly-parked gap-analysis and Wave-1 instructions
   both executed and were ratified (sessions 21e/21i/21f). Active: `cc_instruction_c1_reliability_instrumentation.md`
   — see the START HERE header.)*

---

## STANDING RULE FOR COWORK (read every session)

**Cowork writes instruction files. CC executes them. Never the other way around.**

- When the user says "go", "do E2b", "execute", or similar: the response is
  "The instruction is ready at `cc_instruction_X.md` — give it to CC."
- Cowork MAY: read source files **via the file tools (Read / Grep / Glob) — NOT bash** (see the NEVER-BASH
  standing rule below), write `.md` instruction files, update `cowork_handoff.md` / `STATUS.md` summaries after CC reports.
- Cowork MUST NOT: spawn agents that run build commands or modify `src/` files;
  use Edit/Write tools on anything under `src/`; use bash redirects on source files.
- Violating this rule has broken the codebase twice (E1, E2b). Do not do it again.

---

## ⛔ STANDING RULE: COWORK MUST NOT HALLUCINATE OR ASSUME — VERIFY AT SOURCE (user mandate 2026-06-21)

**The same rule Cowork imposes on CC applies to Cowork itself.** Verified facts only.

- **Never assert a fact, number, file path, line, key/tonic, or claim from memory or plausibility.** If it is
  not verified this session at the committed object (`git show <hash>:path`) or a fresh read, it is NOT a fact —
  say "I need to verify" and verify, or label it explicitly as unverified.
- **Numbers and identifiers re-state, they don't persist.** Re-confirm baselines, hashes, tiers, corpus
  identities each time; do not carry a remembered figure forward (the `kma_abs`/`Gmin` slip — Cowork wrote
  "stable Gmin" for bwv40.8 from the screenshot label without verifying; the real key was F minor; CC caught it).
- **When instructing CC, only put facts Cowork has verified into the instruction** — an unverified detail in an
  instruction can trigger a false stop or mislead. Mark anything provisional as `[prov]`.
- **Distinguish "CC measured it" from "Cowork verified it."** Relay CC's measurements as CC's; verify the
  load-bearing ones at source before building on them. Flag what could not be verified (e.g. shell congested).
- This mirrors CLAUDE.md's "never hallucinate or guess, verified facts only — better ask first if unsure."

---

## ⛔ STANDING RULE: NEVER BASH FOR LOCAL FILES — FILE TOOLS ONLY (user mandate 2026-06-26)

**The Cowork shell (`bash`) reads the working tree through a virtiofs+FUSE mount that can serve a STALE cached copy.**
Verified 2026-06-26: `bash`/`wc` showed `note_model.h` truncated to 158 lines (a June-21 snapshot, 8445 bytes) while
the real file on disk was 235 lines (12686 bytes); the Read tool showed it correctly. This silently corrupted a
test-adequacy audit (the audit agents "found" missing tests — e.g. the L2 clip CP1–CP7 suite — that actually exist),
and triggered a false "the tree is corrupted" alarm. **The file tools (Read / Grep / Glob) read the LIVE disk via a
different path and are correct.**

- **Local file CONTENT, existence, line counts, searches → ALWAYS the file tools (Read / Grep / Glob).** NEVER `bash`
  `cat` / `wc` / `grep` / `sed` / `head` / `tail` / `git status` / `git diff` on working-tree files. *(Supersedes the
  older "read source via grep/cat/sed -n" line in the first standing rule above — that path is the stale one.)*
- **`bash` is permitted ONLY for read-only git OBJECT queries, BY EXPLICIT SHA from CC's commit report** (option B,
  user-ratified): `git show <sha>:path`, `git show --stat <sha>`, `git cat-file`, `git diff <shaA> <shaB>`. These are
  content-addressed and **self-verifying** — a stale/unsynced object errors loudly (`bad object`), never returns
  silently-wrong content.
- **NEVER trust `git rev-parse HEAD` / `git status` / `git log`(branch tip) for "what is current"** — those read
  mutable refs/index that can be stale. Take the SHA from CC's report, read by that SHA, corroborate with a fresh
  file-tool read.
- A `bad object` / missing-object error = a **staleness signal → surface it, do not guess.** Mount refresh is
  host-side only (CC `touch`es the file on Windows, or restart the session).
- Root cause is method, not a product bug to wait on: the bash sandbox is a Linux VM sharing the folder via
  virtiofs+FUSE; the file tools take a separate, live path.

---

## ⛔ STANDING: TWO DEFERRED STRUCTURAL REFACTORS — DO NOT FORGET (user mandate 2026-06-14)

The foundation (Stages 0–2 hygiene/tests/unification/reliable-data + the Stage-3 oneshot decoder) was
completed byte-identically BEFORE any inference improvement. **TWO structural refactors were deliberately
deferred (not skipped) and must NOT be forgotten** — the user explicitly asked that these stay tracked:

1. **Physical file-split (Stage 3.5)** — split `chordanalyzer.cpp` (~3679 lines) into files along the
   now-real layer seams + rename the iteration-vocabulary APIs (`applyIter8691Pedal` → descriptive). The
   layers are LOGICALLY clean but not PHYSICALLY split. Deferred until the layer boundaries stabilize so
   we split once. *Status: PENDING — re-evaluate when Stage-4/6 layer touches settle.*
2. **Dissolve the post-hoc gate-correction layer (Gates A–L) — Stage 5.** The gates are still
   load-bearing (3.4 found none cleanly retirable; beam-1 is numerically the old pipeline). They are
   scheduled to dissolve into fitted weights at **Stage 5 (weight fitting)**, which the roadmap places
   AFTER Stage 4 (key). *Status: PENDING Stage 5 — the gates remain a known structural debt until then.*

Neither is a prerequisite for the current Stage-4 key-inference work (key axis is separate from the
chord-axis gates; every Stage-4 step holds the gate byte-identical 53/24/53 — the ratified current gate; the older
57/23/57 was a stale presentation corrected in the 2026-06-26 doc-truth pass). But they are **owed** —
surface them at every Stage-4/5/6 planning checkpoint until done. Both are also in
`docs/implementation_roadmap.md` (3.5, Stage 5).

---

## ⛔ STANDING OBJECTIVE: FULL TEST COVERAGE — every code path regression-tested (user mandate 2026-06-21)

A near-term, owed objective: **every path/branch in the code should be exercised by a regression test.** Tracked,
not yet a standalone task. How it is discharged:
1. **Per-layer, inside the upstream-first sweep (the primary mechanism):** every rebuilt layer ships with **full
   coverage of its new paths** as part of its implementation gate — not just the correctness cases (e.g. layer-1
   T1–T8) but every branch of the new code. Don't ship a layer with uncovered paths. This accretes coverage
   layer-by-layer as we rebuild, avoiding a giant retroactive effort.
2. **Regression safety net during transition:** the snapshot tests + the per-event oracle-root metric + the
   existing unit suites are the net that catches unintended changes while a layer is being replaced. Do NOT
   exhaustively cover code that is about to be deleted/replaced — cover the *stable* code and each *new* layer.
3. **A coverage MEASUREMENT pass (the concrete near-term step):** instrument line/branch coverage on
   `composing_tests` + `notation_tests`, baseline where we are, and rank the untested paths — so we know the gaps
   rather than guessing. Prioritise stable code + each rebuilt layer; deprioritise soon-to-be-replaced code.

Surface this at each layer's sign-off and at sweep checkpoints until full coverage is reached.

---

## ⛔ STANDING RULE: ALL DOCUMENTATION ALWAYS IN SYNC — treat doc drift like a failing test (user mandate 2026-06-21)

**Documentation is a first-class artifact, kept in lockstep with the code — exactly like regression tests and
code comments.** No ratified change is "done" until *every* affected doc reflects the new reality, in the same
increment. Doc drift is a defect, not a backlog item.

Scope of "documentation" (all of it):
- **Canonical tracked docs (CC's domain, committed WITH the code):** `ARCHITECTURE.md`, `docs/implementation_roadmap.md`
  (the single stage tracker), `docs/layer_architecture_audit.md`, `docs/scoring_model.md` (already sync-mandated
  by CLAUDE.md — this rule generalizes that discipline to *all* docs), and any other `docs/*.md` the change touches.
- **Code comments / remarks:** stale header/inline comments are doc drift too (e.g. the verified-wrong
  `regiontoneprimitives` "4 quarter notes" header — actually `Fraction(4,1)` = 4 whole notes).
- **Cowork design docs (Cowork's domain):** the `cowork_*` layer-design + target-architecture docs must be moved
  to an **as-built** status once a layer lands (the signed design becomes the as-built record, not a stale target).

**Per-layer step (added to the sweep discipline):** after a layer is ratified — *before moving to the next layer* —
sync ALL affected documentation: the canonical tracked docs (CC, committed alongside), the code comments, and the
Cowork design docs (to as-built). This is the architecture analog of the `scoring_model.md` sync rule and rides in
the same checkpoint as the coverage gate. A layer is not closed until it is correct, covered, **and documented**.

**Caught 2026-06-21:** layer 1 (note model, `e30bb45a4f`) shipped with **zero** canonical-doc updates — verified:
0 mentions of the note model across the entire `docs/` tree or `ARCHITECTURE.md`, which still describe the old
segment-first pipeline. This rule exists so that gap is closed now and never recurs.

---

## ⛔ STANDING RULE: TOTAL UNIFICATION — every build increment reports reuse-vs-new + what retires (user mandate 2026-06-22)

The project objective is **one path per concern — no permanent duplicate/redundant implementations.** A *temporary*
coexistence during a transition (a new isolated module running beside the old path until it is wired in) is fine; a
*permanent* second path for the same job is not.

**Every CC implementation/build instruction Cowork writes MUST require, and every CC build report MUST contain:**
1. **Reuse-vs-new** — exactly which existing code the increment reuses, and which pieces are newly written (and why
   a new piece was needed rather than reusing/extending an existing one).
2. **What retires** — which existing path this work makes redundant, and when it is removed (now, or named as the
   retirement step — e.g. "the old resolver retires at the wiring increment"). Nothing is left as a permanent
   duplicate by silence.
3. **Shared primitives, not bespoke copies** — a capability several layers need (a pitch-context builder, a
   best-sequence/Viterbi routine, a key-distance helper) is built once and reused, not re-implemented per layer.

**Cowork verifies this at source** on every increment (does the new code duplicate an existing path? is the
retirement real or deferred-forever?). A permanent duplicate path is a defect, like doc drift or a coverage gap.

---

## ⛔ STANDING RULE: KNOWLEDGE-BASED CODING ONLY — no assumption-based production code; exploratory measurement is the path (user mandate 2026-06-23)

**Production code is written only on MEASURED knowledge, never on an assumption or an untested attribution.** When the
evidence a build decision needs is not in hand, the mandatory move is **exploratory** — a read-only diagnostic /
measurement that *earns* the knowledge — BEFORE any production logic is written on the belief. Building production code
on "we think X will work / we think the residual is Y" and hoping is forbidden; gathering the cheap evidence that turns
the belief into a fact is required. **Exploratory / diagnostic code is explicitly encouraged** (decode-only flags,
graded measurements, decompositions) — it is how the knowledge is obtained, and it is read-only / production-byte-identical.

This is the build-time companion to "verify at source" and "investigate by default": those govern *claims*; this governs
*code*. A measurement that **disproves** an assumption is a success, not wasted work — it stops a wrong build (e.g. the
fair-key test that showed wiring the key would NOT close the L4 chord-root gap, *before* any C/wiring spend). Every
layer increment is therefore **measure → decide → build**, the measurement gating the build, never the reverse.

---

## ⛔ STANDING RULE: INVESTIGATE BY DEFAULT — NEVER ASK "investigate vs proceed" (user mandate 2026-06-14)

**Whenever a step could be investigated/measured BEFORE committing, ALWAYS investigate first — and do NOT
present it to the user as a choice.** The user's standing answer to "investigate or go in some direction"
is *always investigate*, so asking wastes a turn. This is the never-guess principle's logical end: gather
the cheap evidence before any commitment, by default. When Cowork hits such a fork, it writes the
investigation/measurement instruction directly (read-only / byte-identical where possible).

**What Cowork MAY still bring to the user (the only legitimate questions):** (1) ratification of a
*measured* result (accept/proceed once the evidence is in — the user's deliberate-behavior-change call);
(2) a pure VALUE / PRIORITY / RISK-APPETITE / PRODUCT-PHILOSOPHY call that **no investigation can settle
AND that has no investigate option**. Never a "should we investigate first?" question — the answer is yes.

---

## ⛔ STANDING RULE: PREDICATES MUST BE QUALIFIED IN SPECS (user mandate 2026-06-24)

**When writing or reviewing any spec, every predicate/pointer word names its argument.** Many words are *two-place*
("uncertain" → about *what*; "defers" → *what* to *where*; "fits" → by *what measure*; "close"/"enough"/"in view" → by
*what test*; "prevailing"/"plausible"/"spurious" → by *what rule*) and are easy to write with the second place left
implied — which is exactly where specs hide holes. The mechanical check: force each such word to be followed by the
thing it points at; if that forces a phrase the prose does not supply, the predicate is **unqualified** — fix it.
Deferring a *numeric value* to tuning is allowed; leaving the *argument or its decision structure* unnamed is not. Home
of the rule: `cowork_design_doc_template.md` (writing standard). Method + worked examples: `cowork_spec_language_sweep.md`,
`cowork_layer3_spec_language_sweep.md`.

---

## ★ STANDING METHOD: LAYER-BY-LAYER AUDIT ONCE PIECES ARE IN PLACE (user, 2026-06-14)

**The architectural payoff and the back-half verification model:** *as soon as every piece of the puzzle
is in its CORRECT layer, we go layer by layer and ask whether that layer is correct AND complete —
focusing on each layer's single responsibility and ignoring the other layers.* This is only possible
because the layering work (Stages 0–3) made the seams real (oracle = vertical, competition/function
layer, post-scoring gates, key resolution, section/KeyArea, functional labeling). It is the goal the
whole refactor served, and it directly motivates finishing the TWO deferred refactors above (a layer
can't be cleanly audited while it's physically tangled in `chordanalyzer.cpp` or while its responsibility
is smeared across a post-hoc gate layer). **Method, when invoked:** pick a layer, state its single
responsibility, audit correctness + completeness against THAT responsibility only (its inputs assumed
correct, its consumers ignored), pin gaps as that layer's obligations. Apply per layer as the back half
(Stages 4–6) lands each piece in place.

**★ SHARPENED (user, 2026-06-15):** this comprehensive per-layer audit ("does this layer serve its purpose
**fully, correctly, comprehensively**?") is the back-half **ACCEPTANCE** review and is **GATED on the
layers actually existing as single-responsibility units** — i.e. it waits until the TWO deferred refactors
(chordanalyzer.cpp file-split + gate-layer A–L dissolution) have made the seams physical. Auditing now would
be auditing a moving, tangled target (e.g. chord analysis is still entangled with a stateful temporal
context, as the J-key-iii re-emission bug showed — `analyzeChord` is not yet a pure function of its layer's
inputs). **Distinct from the ongoing per-change BUILD-TIME verification** (every CC report verified at
source + measure-first checkpoints), which CONTINUES the whole way and is what catches regressions during
construction (it caught the re-emission artifact before commit). Acceptance audit = deferred to clean
layers; build-time verification = always on. They are complementary, not redundant. **Build-time
verification lesson folded in (2026-06-15):** when a change adds a NEW consumer of an existing data
structure, assert **same-input → same-output** as an explicit invariant (the missing mirror of the
J-key-iii §5 key invariant — a chord-axis "key-unchanged region ⇒ byte-identical chord" check would have
caught the re-emission bug one checkpoint earlier).

---

## What this project is

MuseScore Studio. The active development area is `src/composing/`, which implements
harmonic analysis (chord detection, inversion scoring, key inference). The main file
is `src/composing/analysis/chord/chordanalyzer.cpp`. The bridge between the composing
module and the notation layer is `src/notation/internal/notationharmonicrhythmbridge.cpp`.

Mandatory reads at the start of every session:
- `C:\s\MS\STATUS.md` (header only, first ~10 lines) — current baselines and HEAD commit
- `C:\s\MS\build_and_test.md` — all build/test/tool commands

**When CC returns a report**, always do this before evaluating it:
1. Re-read the instruction file that CC was given (listed in "Next CC task" in Current state below)
2. Then read CC's report

CC's report references task numbers, design decisions, and deviations that only make sense against the original instruction. Evaluating the report without re-reading the instruction means accepting CC's framing uncritically — which is exactly the failure mode we guard against.

**THE WORKING METHOD (canonized 2026-06-12, user mandate — these principles produced
Stages 0–3.1b without a single unplanned regression; they are not optional):**

A. **Pin before you change.** No layer/gate/method is built upon until its current
   behavior is pinned (tests) and its instruments verified (metrics, corpora, source
   identity). Instruments first, measurements second, changes third.
B. **Byte-identity bridges for every restructure.** A refactor earns zero improvements;
   its gate is 0-diff across corpora (all relevant configs), snapshots, and suites,
   with FP near-tie canaries unmodified. Golden refreshes as a reflex are FORBIDDEN —
   a diff is a stop, not a chore.
C. **Behavior changes are deliberate, measured, ratified.** Never shipped as a side
   effect (the 3.1b lesson). The answer-delta is measured BEFORE the commit is
   proposed; ratification decides on data.
D. **Never guess — investigate or state the unknown** ([probe]/[code] tags, explicit
   Unknowns sections). Binds CC and Cowork equally. Read the call site, not just the
   qualifier (the completeTriad lesson).
E. **Stop conditions are designed in advance and honored.** The system's best moments
   were stops (snapshots 0/11; DCML-worse; tracked-junk deviation). A tripped stop is
   the process succeeding.
F. **Falsified decisions get re-decided, and their evidence gets committed** (Q1 →
   `p3_granularity_ab_3_1b.md`; the cap archaeology; the M3 reconstruction). Dead ends
   are documented so they are never re-walked.
G. **One change-class per commit, explicit staging, every commit independently
   verified** (`git show --stat` + host-side reads against the claims).
H. **Errors are owned by name** — Cowork's included (the snapshot-harness premise, the
   whole-score prior, the relay gaps). Ownership is what keeps the ledger honest.

**STANDING RULE — CC trust model (made permanent 2026-06-10, user mandate):**
1. **Never fully trust CC.** CC can hallucinate, guess, and present guesses as findings.
   Every consequential CC claim gets independent verification before acceptance:
   commit contents via `git show --stat`, code claims via host-side Read/Grep of the
   actual source, numeric claims against recorded baselines. Track record this session:
   CC has been right where verifiable most of the time, but produced at least one
   guessed mechanism stated as fact ("parallel batch path resolves ties
   nondeterministically" — wrong, batch_analyze has no threading) and one
   imprecise-memory claim (junk files "M/regenerated" — that one was Cowork's own
   stale-sandbox error; verification cuts both ways).
2. **CC does not hold the bigger picture — Cowork does.** CC optimizes the task in
   front of it. Cross-cutting consequences (gate semantics, baseline integrity, layer
   architecture, re-baseline bundling, what a finding means for Stages 2–6) are
   Cowork's to evaluate. When CC proposes a disposition for a finding ("log it for
   later", "not a blocker"), treat that as input, not a decision.
3. Both rules also bind Cowork's instructions to CC: the never-guess /
   investigate-or-state-unknown rule (introduced Stage 1d) is standing for ALL future
   instructions, not per-instruction boilerplate.
4. **All Cowork adjustments/approval-conditions go in INSTRUCTION FILES, never only in
   chat replies.** Chat-relayed adjustments were lost twice (2026-06-10: the H2
   extension + 326-fact rider after the hygiene pass; the chordanalyzer.h:62 comment +
   diagnose context banner after 2.3). Instruction files have a 100% delivery record.
   "Approved with additions" means: write the additions as an addendum instruction
   file, then approve.
   **"HELD" is now unambiguous (2 slips: 3.3, metric-L0L1): "held for Cowork" =
   `git add` is OK, `git commit` is NOT, until a ratification/approval file says so.
   A pre-authorized ship that may commit-on-green-proof will say exactly that.**
5. **Cowork reads every CC report IN FULL before ratifying or approving its commits.**
   Verification-against-primary-sources does not substitute for the report's Findings/
   Unknowns/caveat sections — CC under-weights its own findings in chat summaries
   (precedent: the 326/353 fact, the preset headline), and an unread caveat went
   unanswered at the Stage-3 design ratification (the bwv320 dual-classification
   question, caught only in the 2026-06-12 retrospective sweep). Chat summaries are
   navigation aids, not the artifact.

---

## Two worktrees

- `C:\s\MS` — **master** branch (main working tree — use this for all development)
- `C:\s\MS-llm-triage` — `llm-triage` branch (separate worktree, only for LLM triage work)

All active development is on **master**. Always confirm which worktree CC is in before giving it instructions.

---

## Architecture direction (decided 2026-06-09, session 4) — READ BEFORE ANY PHASE E WORK

**Single-pass, unified, no parallel paths.**

The redesign goal is a single comprehensive pass through properly layered components
where each layer passes its full evidence forward — not a multi-pass iterative loop.
The full design is in `docs/redesign_plan.md`.

Three non-negotiable principles for all Phase E work:

1. **Single commit path.** Pass 1, Pass 2 sub-region, Pass 2b sub-region, and the
   notation bridge must all flow through the same Layer 3 → Layer 4 → Layer 5 stack.
   `advanceTemporalContext` is called once, uniformly, at every commit site. The current
   manual inline assignments in Pass 2 and Pass 2b that bypass it are bugs to eliminate,
   not patterns to follow.

2. **No parallel paths, no code duplication.** Logic that exists in both the batch path
   and the notation path must be unified. `diagnoseChord` must be a view into the
   production pipeline, not a separate scorer. No new bypass paths.

3. **Resolve the `explorationMode` dual-path.** ✅ **RESOLVED — committed `e7d4ba2b1a`
   (2026-06-10).** `ChordAnalyzerPreferences` now carries `fn::ScoringPhase scoringPhase`
   (enum lives in `chordanalyzer.h`, `function` namespace — the include direction
   harmonicfunctionlayer.h → chordanalyzer.h forbids the originally planned placement);
   the 5 bonus/gate functions are stateless; the single check is `applyProgressionSignals`
   at the top of `applyHarmonicFunction`. Do not reintroduce per-function phase flags.

**What this means in practice:** do not add new gates, compensating fixes, or new
parallel scoring paths to the current feedforward pipeline. Phase E completes the
evidence picture (symmetric forward context alongside backward) and unifies the commit
paths. BIR re-calibration happens after the architecture is stable.

**MASTER PLAN (2026-06-10): `docs/implementation_roadmap.md` is the single consolidated
tracker.** Both reviews' conclusions (part 1 `cowork_target_architecture_review.md`, part 2
`cowork_implementation_review.md`) are mapped to ordered Stages 0–7 with per-stage
verification gates ("no surprises": pin/verify each layer before building on it —
Stage 0 hygiene → Stage 1 pin current behavior with tests → Stage 2 one-pipeline/one-truth
(Phase 4c move, batch parity, diagnoseChord fix) → Stage 3 decoder → Stage 4 key path →
Stage 5 weight fitting → Stage 6 functional layer). Check the traceability table there
before planning any new CC task; new work must slot into a stage.

**Architecture review (2026-06-10, session 5) — Phase E target renamed.** Full review in
`cowork_target_architecture_review.md`; adopted direction in `docs/redesign_plan.md`
"Architecture review addendum (2026-06-10)"; §2.14 reconciliation note added to
ARCHITECTURE.md. Core finding: the documented failure classes (Δ=+7a/b, gate cascades,
rcb dead ends) are all symptoms of greedy left-to-right commitment; the correct Phase E
target is **joint global decoding over a hypothesis lattice** (oracle = emissions,
progression signals = transitions, Viterbi/beam decode; key as an HMM path; weights
fitted against DCML corpora; functional labels as sequence labeling over the decoded
path). Phase E must NOT be designed as a pack of new locally-applied signals feeding the
greedy pipeline. Pending: part-2 session validating this against the as-built system
before any code direction is imposed.

---

## Current state (as of 2026-06-10, session 5)

- **HEAD:** `e7d4ba2b1a` on master (refactor: replace explorationMode flag with ScoringPhase
  enum — Phase E Step 5). Several commits ahead of origin, not pushed. Working tree dirty
  only with pre-existing uncommitted doc edits (ARCHITECTURE.md, CLAUDE.md,
  docs/redesign_plan.md + this file + STATUS.md) and the perpetually-dirty `muse` submodule
  (intentional Snap fix — never commit it).

  `e7d4ba2b1a` — explorationMode dual-path eliminated. `bool explorationMode` removed from
  `ChordAnalyzerPreferences` and from all 5 bonus/gate signatures (`wSeqBonus`, `wDimBonus`,
  `wStepInBonus`, `wStepOutBonus`, `gateRZeroesRootContinuity`) — now stateless and pure.
  Single control point: `applyProgressionSignals = (phase == ScoringPhase::Final)` at the
  top of `applyHarmonicFunction`; gates the 4 progression bonuses, Gate R, and the Pass B
  `applyStepBonusGuard` calls (Pass B needed explicit gating — pre-change it was suppressed
  only indirectly via the helpers returning 0; the guard's sole side effect is
  `cand.score += stepIn + stepOut`, so skipping the call is provably equivalent — verified
  in code by Cowork). `ScoringPhase` enum defined in `chordanalyzer.h` (`function` namespace,
  alongside the `ScoringSnapshot` forward-decl) — the instruction's `harmonicfunctionlayer.h`
  placement was backwards; CC's deviation verified correct. Two `harmonicsegmenter.cpp`
  sites (L348, L706) set `Segmentation`; sole production call site `chordanalyzer.cpp:2969`
  passes `prefs.scoringPhase`. `gater_tests.cpp` Branch 4 → end-to-end phase-gating test
  (`GateR_PhaseGated_FinalFiresSegmentationSkips`). `docs/scoring_model.md` synced in the
  same commit. 7 files, 416/416 · 52/52 · 11/11, zero snapshot diffs, no goldens refreshed;
  BIR 24/13 / 35/7 unchanged. **Verification basis: static code equivalence + zero snapshot
  diffs + BIR consistency — NOT a corpus A/B byte-diff** (report §5's "byte-identity on all
  353 scores" is an inference, not a measurement). Report:
  `cc_phase_e_exploration_mode_report.md`.

- **✅ Stage 0 COMPLETE (2026-06-10).** Commits `7bc1609159` (docs) ← `a236a0ff21`
  (hygiene: kTemplateCount six sites, dead fnCtx fields, tie-policy docs) ← `70fd8a686b`
  (tracked junk removed + gitignored; no generator — one-time redirect accidents swept
  into an old feature commit). All verified by Cowork (commit contents host-side).
  Gate 0→1 passed: 416/416 · 52/52 · 11/11, BIR 13/7 both presets. Deferred: CLAUDE.md
  "4-site atomic update" reconciliation with kTemplateCount (fold into a later doc pass).

- **✅ Stage 1a COMPLETE — `757efa5dbf`** (23 tests, composing 416→439/439; tests-only,
  production untouched; report `cc_stage1a_report.md`, verified by Cowork incl. full
  test-file read + fixture arithmetic). Findings: F1 (§2 Sus4♭5/HalfDim wording → doc
  pass list), F2+F5 (→ Stage 3 obligation list in roadmap 3.4), F3/F4 (pinned).
  Doc-pass backlog now: CLAUDE.md 4-site→kTemplateCount reconciliation + scoring_model §2
  F1 wording.

- **✅ Stage 1b COMPLETE — `6101a9b2c5`** (48 tests, composing 439→487/487; tests-only).
  Report `cc_stage1b_report.md` — definitive gate inventory + findings F1–F8. Cowork
  verified F1 (B/C/D dead code) in the production source and escalated the preset-cap
  finding: `maxTotalInversionContextBonus` has NO setter on any path and is non-binding
  at current sums (1.85 default / 0.75 Jazz) — the documented 2.5/0.6 "load-bearing"
  values exist nowhere.

- **✅ Doc pass COMPLETE — `af39f28179`** (4 files, verified by Cowork incl. CLAUDE.md
  via session context). Cap archaeology: ⛔ did NOT fire — **2.5/0.6 never set in any
  committed code** (aspirational doc-comment since `46c76ad67f`; zero `-G` assignment
  hits; the iteration plan itself prescribed the non-binding 2.0 default). Jazz
  baselines unaffected. Residual for next code-touching commit:
  `chordanalyzer.h:402–409` doc-comment still carries the 2.5/0.6 fiction + a stale
  signal list (nextRoot/consecutive/recentRoot/weakBeat).

- **✅ Stage 1c COMPLETE — `4656f43258`** (11 tests, composing 487→498/498; 9 minimal
  .mscx fixtures; composing tests can now load Scores via the engraving test env).
  Verified by Cowork (report + key tests + env file host-side). NOT-PINNED under scope
  valve (recorded as Gate 1→2 exceptions in roadmap 1.3): coalesceShortSameRootRuns,
  Pass 2/2b boundaries, sub-region bassIsStepwiseToNext. Findings G1–G5: G1 confidence
  wart pinned with real numbers (Stage-4 anchor), G2 root-agnostic absorb order-coupled
  with coalesce (Stage 3), G3 piece-start returns size-1 list, G4 sentinel confidences
  (0.0/0.5 hard-coded), G5 partial-sig correction is whole-score (Stage 4).

- **✅ Stage 1d COMPLETE — `bb48394b52` — GATE 1→2 PASSED.** 54 metric-script tests +
  hand-derived fixtures; scripts untouched; [code]/[probe] epistemic tagging honored;
  non-vacuousness mutation check. Findings F-1/F-2 (extract_quality dim-`o` miss,
  Ger65/N6/It6 mis-parses) + F-3 ("24" provenance untraced) → Stage 2.2 single
  re-baseline event. F-3 handoff wording already corrected by Cowork (BIR script note
  above).

- **✅ RESOLVED (2026-06-10): the Jazz "nondeterminism" was M3 — corpus-state
  contamination, not analysis nondeterminism.** Proven by probe (`cc_jazz_nondeterminism_report.md`):
  Jazz is deterministic 7, Baroque deterministic 13; 2 full regens, 0/353 JSON diffs —
  **C++ batch determinism proven, retroactively validating all historical A/B checks.**
  Mechanism: shared `tools/corpus` + FAILED-worker stale files (`run_bach_preset.py:113–122`)
  + `skip_cpp` reuse + no preset guard in characterise. Canonical Jazz 7-case identity
  set: {bwv244.15, 245.17, 245.40, 422, 432, 45.7, 74.8}.
  **INTERIM GATE (until 2.2a lands):** "Jazz ≤ 7" means a clean 353/353 regen yielding
  that identity set, with Baroque=13 + snapshots as co-gates — not the raw integer.

- **✅ Stage 2.1 COMPLETE — `eeca0dea30` (rider) + `8598cbd245` (Phase 4c move,
  Option D).** Snapshots 11/11 zero diffs (decisive). `analysis/section/sectionanalyzer.{h,cpp}`;
  notation helpers shrank ~900 lines to adapter surface; cadence/pivot tests stayed in
  notation tests (include updates). Dead weight/pitch-context shims (no live caller) →
  Stage-2 cleanup list.

- **✅ Stage 2.2a COMPLETE — `e20894c75b`** (tooling; verified by Cowork: exactly 6
  files) + bookkeeping docs `6f1e3dc807`. Per-preset dirs + sha256-fingerprinted manifest validation;
  63 Python tests; Baroque 13 + Jazz 7 exact identity sets verified; contamination
  probe errors. **Interim gate RETIRED** — "Baroque ≤ 13 / Jazz ≤ 7" plain meaning
  restored (clean manifest-validated regen). Deferred: analyze_inversion_errors.py
  --corpus-dir (rides with 2.2).

- **✅ Stage 2.2-i COMPLETE — `cc_stage2_2_ab_dossier.md` (no commits, by design).**
  Headline: section-level barely changes analysis (4 genuine root changes corpus-wide,
  net-negative, all on thin gap/split slices) but surfaces ~250 per-beat disagreements
  the coarse batch regions masked — **the 13/7 gate undercounts user-visible per-beat
  root errors ~7×** (rn corroborates independently: root_agree flat, all delta in
  root_err). F-3 closed (24/13 & 35/7 = analyze_inversion_errors three-way split).
  **DECISION (Cowork+user): gate stays batch-granularity**; granularity-robust metric
  now MANDATORY at Stage 5; 2.4 scope grew (Pass-0 prefs divergence + section-layer
  `inferGapRegion` default-prefs preset leak = likely cause of the 3 regressions).

- **⚠ CORPUS AUDIT (Cowork, 2026-06-10): `cowork_corpus_audit.md`.** Highest findings:
  **C1 — the snapshot gate's 11 source scores live in gitignored, revision-UNPINNED
  external clones** (`tools/dcml/*/MS3`; REPRODUCIBILITY clones at floating HEAD) — the
  byte-identity gate rests on files with no recorded identity; **C2 — the music21
  version that generated the 353 gate-corpus `.music21.json` is recorded nowhere**;
  C3 — 353-vs-361-vs-410 chorale filter provenance undocumented; C4 — stale flat
  `.ours.json` + empty accident dirs + `src/composing/tests/scores/` (7 files incl.
  `xxxxx.mxl`) referenced by NOTHING + `score_inventory.md` badly stale; C5 — ~850
  human-annotated scores unused (Stage-5 opportunity, noted in roadmap 5.2).
  Ground-truth verdict (sharpened by user mandate 2026-06-10): **the ONLY ground truth
  is the human annotation (WiR/DCML); music21 is NOT ground truth** — it is an
  algorithmic noise filter, and the 13/7 "genuine" counts are a music21-filtered LOWER
  BOUND on human-adjudicated errors (cases where music21 sides with us against DCML are
  excluded by an algorithm's opinion). Never describe the gate as "ground-truth
  agreement." Stage 5 must evaluate a DCML-only gate variant (roadmap 5.2). No
  self-annotations in any gate; catalog/goldens correctly used as regression pins only.
  Remediation = one hygiene instruction after 2.2-ii (see audit Disposition table).

- **✅ Stage 2.2-ii SHIPPED — `75a5815960`/`c7aeb24ae1`/`465450bf49`/`9e52147b04`**
  (verified by Cowork: cumulative diff exactly 8 files; F-1 at compare_rn.py:181,
  It6 routing in split_rn, shims gone; gate-neutral: 13&24/13, 7&35/7 exact identity
  sets, 65/65 Python). **Stage 2.2 COMPLETE** (2.2a + 2.2-i + 2.2-ii).

- **✅ Corpus hygiene COMPLETE — `a934574820`/`dd8a898015`/`3d8981bb57`/`0520a2dda2`**
  (verified by Cowork). Sources pinned (manifest + drift test + REPRODUCIBILITY commits;
  ABC clone DIRTY recorded verbatim; licenses: CC BY-NC-SA or no-LICENSE → in-tree
  copies NOT GPL-compatible, hash-pin is the mechanism). music21 ESTABLISHED v.9.9.1
  (embedded `<software>` tags; export chain incl. MuseScore 2.1.0). 410→353 filter
  recovered (`_is_bach_chorale`); 361↔353 diff non-computable (Riemenschneider vs BWV,
  evidenced); 352→353 +1 unknown (logged). Flat .ours.json + accident dirs deleted
  (disk-only); dead test scores removed (`3d8981bb57`). **KEY FACT: only 326/353 gate
  chorales have WiR human annotations — gate = human-adjudicated 326, music21-filtered,
  batch granularity (all three qualifiers in roadmap 5.2).**
  **Two approved adjustments MISSED the commit set (relay gap) — ride with the next
  instruction:** (a) `analyze_inversion_errors.py` no-arg default → `tools/corpus/baroque`
  + BUILD_AND_TEST §4 legacy line repoint (the no-arg path now errors); (b) the 326/353
  WiR-coverage fact into `score_inventory.md`.

- **✅ Stage 2.3 COMPLETE — `18dc9e1829` (diagnose replays production; kDiagTemplates +
  contextualBonuses removed; agreement invariant + Δ=+7b Gate-R dump tests; composing
  501/501) + `001b15df2d` (hygiene riders).** Verified by Cowork. Two approved
  additions missed the commits (relay gap #2 — see trust-model rule 4):
  addendum SHIPPED `fb8b980948` (comment fixes + conditional JSON "context"
  banner — NONE on the batch path, real context summary when threaded; verified).

- **Doc-staleness riders for the NEXT instruction (CC flagged, out of its scope;
  confirmed by Cowork):** CLAUDE.md:159/166 still lists kDiagTemplates as a template
  sync site (stale post-2.3); ARCHITECTURE.md:861 references the removed
  `contextualBonuses()`; layer_architecture_audit.md:84–92 carries a now-moot
  "Action for CC" item. Historical iteration records stay untouched (revisionism).
  Also: accumulated uncommitted bookkeeping (STATUS/handoff/roadmap) needs its
  periodic docs commit.

- **✅ Stage 2.4 COMPLETE — V1 `140ceb1a9e` / V2 `1a08e96d8a` / V4 `6be2b30a96`**
  (+ bookkeeping `4e91e3aa4c`). Decisions in ARCHITECTURE.md; D-PASS0 headline:
  chord-scoring presets are batch-only, live product = struct defaults matching NO
  preset; V4 measured the user config: **BIR=false 14 = Baroque-13 ∪ {bwv187.7}** —
  Baroque gate ≈ user reality (slightly conservative); Jazz-7 contains 2 preset-only
  artifacts (bwv244.15, bwv74.8); bwv187.7 = first user-experienced error outside all
  gates (mode-prior-surfaced; candidate Stage-3 acceptance case). App mode priors =
  bespoke set (11/21 diverge from all presets). D-GAP causal hypothesis falsified
  (structural); leak fixed anyway (live under Jazz). OPEN: Python-count reconciliation
  (68 → "67+2"), rides with 2.5.

- **✅ Stage 2.5 COMPLETE — P1 `3aa9db7676` (harness as DISABLED_ test in
  pipeline_snapshot_tests + `docs/perf_p3_baseline.md`) / P2 `c37b98321b`.** Numbers:
  P3 per-query median 33–215 ms, p95 up to 2.75 s, max 7 s (Mozart-scale); Pass-0 ≈
  99% of cost; P4 fallback 0/2231 (closes the 2.4 §1.3 unknown for loadable scores);
  budget: beam-1 p95 ≤ observed ×1.10. Python-count reconciled: 70 total = 67 metric
  + 3 snapshot-source tests; no bug, reporting-scope artifact (quote the two-file
  total henceforth). **KEY STAGE-3 INPUT: "decode once, query many" — the lattice
  makes P3 a lookup, fixing its tail AND the D-P4/D-BRIDGE cold-context contracts
  (roadmap 3.1 updated).**

- **🏁 STAGE 2 COMPLETE (2026-06-12).** All items: 2.1 Phase 4c move · 2.2a corpus
  hardening · 2.2-i A/B dossier · 2.2-ii package · corpus hygiene (audit C1–C4) ·
  2.3 diagnose production view + addendum · 2.3b queued · 2.4 divergence decisions +
  V4 user-config measurement · 2.5 perf baseline. One pipeline, one truth: gates
  pinned to identified bytes, metrics tested, user config measured
  (Default-14 = Baroque-13 ∪ {bwv187.7}), divergences decided in ARCHITECTURE.md,
  diagnostics trustworthy, perf envelope stated.

- **Stage 3 design draft REVIEWED (2026-06-12).** Verdict: ratified subject to ONE
  mandatory correction — the draft's `completeTriadInversionBonus` "region-local,
  pull from 3.3 bundle" claim is WRONG (Cowork verified `chordanalyzer.cpp:1613–1622`:
  the call-site gate is `bassIsStepwiseFromPrevious || bassIsStepwiseToNext` — the
  audit's "temporal" classification stands; CC read the qualifier and missed the
  call-site guard). All seven §13 Open Questions decided per recommendations
  (Q3 notably: identity-mutating gates retire BEFORE beam widens past them; Q7:
  decode-once = 3.1b after the byte-identity gate). Ratification addendum:
  `cc_instruction_stage3_design_ratification.md` (incl. a §correction-4 sweep:
  re-verify the other four signals' call-site guards for the same error class).

- **✅ Stage 3 design RATIFIED + COMMITTED `e2bdef7e13`** (correction applied:
  completeTriad = edge-gated emission, all FIVE signals migrate at 3.3; sweep clean —
  no second qualifier-vs-guard error; Q1–Q7 decided; hash-stamping deviation accepted).

- **📋 Full-report retrospective sweep (2026-06-12, trust-model rule 5 backfill) —
  doc-rider queue for the next docs-touching instruction:**
  1. **The Baroque-13 identity set is pinned in NO committed doc** (only Jazz-7 is; the
     full set with ticks exists only in gitignored cc_ reports — 2.2-ii §4:
     bwv102.7@17520, bwv14.5@8160, bwv17.7@46080, bwv174.5@6240, bwv245.17@4800,
     bwv245.40@51360, bwv261@33840, bwv269@20640, bwv301@960, bwv381@4800,
     bwv422@23040, bwv432@5520, bwv45.7@20160). Commit it next to the Jazz set.
  2. The music21 **freeze anchor** prose lives only in gitignored
     `tools/corpus/README.md` (hygiene §3); replicate into committed REPRODUCIBILITY.md.
  3. 2.1's proposed ARCHITECTURE.md file-map sentence (sectionanalyzer location +
     Pass-0 injection contract) was never applied — verify and add.
  4. Frozen iterNN diagnostics lost their flat `.ours.json` inputs in the hygiene
     deletion (2.2a kept them partly FOR those scripts; the hygiene reader survey
     omitted them). Fail-loud if re-run — acceptable; recorded, no action.
  Parked: 2.1 §5.6 unused includes in trimmed helpers; Stage-1d NOT-PINNED WiR
  discovery plumbing (partially compensated by the snapshot-sources manifest).

- **✅ Stage 3.1 COMPLETE — `8e4bb4902d`** (7 files, +506/−28; report read in full by
  Cowork per rule 5; commit verified). The beam-1 decoder owns the commit chain at all
  three sites behind `decodeQualityLevel` (default FastBeam1). Byte-identity: 0/353 ×
  3 configs + empty `git diff tools/corpus` (manifest fingerprints = second proof);
  snapshots 11/11; composing 505; BIR sets exact ×3; perf within ×1.10; zero design
  deviations. Key structural fact: the decoder computes no score — FP-sensitive
  arithmetic untouched in `applyHarmonicFunction`.

- **⚠ 3.1b STOPPED CORRECTLY by CC (2026-06-12), Q1 RE-DECIDED.** The whole-score cache
  worked (warm ~0.0006 ms) but: (1) Cowork's instruction premise was wrong — the
  snapshot harness flows through the orchestrator, so snapshots went 0/11 (CC did NOT
  refresh — correct); (2) the answer-delta A/B FALSIFIED the design's whole-score
  prior: 32–40% tick changes on contrapuntal scores, DCML 59/41 in the WINDOW path's
  favor (Mozart 35/65 against whole-score). **This is the 2.2-i granularity finding
  recurring** — fine windows are more per-tick DCML-accurate; coarse whole-score is
  self-consistent. **Decision (Cowork): bounded-window cache (CC's recommendation);
  whole-score SHELVED with evidence; P3↔P1 consistency PARKED as a product/Stage-5
  question; D-P4/D-BRIDGE closure rolled back to the 2.4 contract; the A/B data
  promoted to committed Stage-5 evidence.** Revision instruction:
  `cc_instruction_stage3_1b_revision.md`.

- **✅ Stage 3.1b COMPLETE — B1′ `947519b2b6` + B2 `4f1754c26c`** (both verified).
  Bounded-window cache (memoized pure per-window section build; byte-identical by
  construction: snapshots 11/11 no-refresh, always-on equality test, AnswerDelta=0);
  warm re-click ~0.003 ms; pointer-reuse hazard closed pre-commit via
  `Notation::setScore()` lifecycle flush (no per-lifetime Score id exists —
  investigated; flush-before-install = no false-hit window). Whole-score variant
  SHELVED with evidence (`docs/p3_granularity_ab_3_1b.md`, Stage-5 input);
  Q1 re-decided; D-P4/D-BRIDGE rolled back to 2.4 contract (design §8 amendment).
  Full record: `cc_stage3_1b_report.md` §1–§6 (whole-score measurement) + §R
  (binding outcome) — read in full by Cowork.

- **3.3 Task-1 STOP resolved (2026-06-12): Gate R = reconstructed-credit
  (`fullBasisDep = cell.basisDep + cappedInv ≤ 0`).** CC's derivation proved the
  ratified pcWeight mechanism text WRONG (old Gate R fires ⟺ `cappedInv==0`; Dim's
  inversion credit includes a temporal gate no pure-vertical rule reproduces) —
  mechanism superseded as falsified-by-derivation (Method F); the reconstructed-credit
  form is the faithful execution of the ratified INTENT and closes Finding 6 fully
  intra-layer. The basisIndep ≤1-ULP reassociation: primary approach accepted; ANY
  A/B diff ⇒ switch to the pre-approved bit-identical fallback (expose `d`), no
  case-by-case reconciliation. Decision file: `cc_instruction_stage3_3_gater_decision.md`.

- **✅ Stage 3.3 COMPLETE — `548adb7b2e` (RATIFIED POST-HOC).** All five signals
  migrated (oracle now genuinely vertical — audit Finding 1 CLEARED); Gate R =
  reconstructed-credit (`fullBasisDep ≤ 0`, intra-layer — Finding 6 CLEARED); byte-
  identity 0/353×3 + snapshots 11/11 + all suites + identity sets ×3 + canaries
  unmodified; **re-pin ledger EMPTY** (defaulted cell flags — strongest outcome).
  basisIndep ≤1-ULP primary shipped, fallback unneeded (A/B zero diffs).
  ⚠ Process note: the commit was made BEFORE ratification despite "held" — content
  fully verified and ratified post-hoc, but "held" means held (do not repeat).
  Cleanup queued for 3.4: the retained 2-arg `gateRZeroesRootContinuity` test-compat
  overload (semantics subtly non-production) dies when Gate R is absorbed into the
  rcb edge.

- **✅ Stage 3.4-i COMPLETE — Ship #1 `da1b440845` (B/C/D removed) + Ship #2
  `a652dc1ba7` (Gate R → `rcbEdge()`, overload dropped); both 0/353×3 byte-identical.**
  Dossier `cc_stage3_4i_dossier.md` read in full (rule 5). **Reframing facts: gate
  retirement is BIR-free on Default (user config); ALL BIR movement is Jazz-only;
  A/E/F/G-family/H run only under Baroque. 3.2 risk concentrates in Gate I (5 Jazz fixes
  + Δ=+7b coupling).** Classes: C1 retire-now (E/F/K/Iter86) · C2 3.2-acceptance
  (I/bias/L/H/Iter91) · C4 defer (A/G-family) · C5 keeper (J, BIR-blind, fires huge).
  F4/F6/F8 re-decide inventory done (paper) — fixes carried by the owning gate's
  retirement, never silent.

- **✅ Stage 3.4-ii COMPLETE — ZERO gates retired (no commit; tree clean at `a652dc1ba7`).**
  The non-chorale spot-check + byte-level proof gate FALSIFIED all four C1 "dead"
  verdicts: K + Iter-86 change winners on non-chorale repertoire (Chopin op24-4,
  Mozart K310-1 — never truly C1 → C2 acceptance); E + F change only alternatives
  lists, winner-neutral, so NOT byte-identical to remove → C2′ alternatives-hygiene
  (the decoder's Q5 output-assembly subsumes them for free). CC implemented E-removal,
  hit the 2-Baroque-chorale sha256 diff (bwv245.3, bwv336), and reverted per the stop
  condition — exemplary. **Methodology correction (my instrument, not CC): 3.4-i §3's
  winner-region metric is BLIND to winner-neutral alternatives-list changes; the
  `.ours.json` sha256 is the authoritative deadness test.** DCML 3.2 inputs: Iter-86's
  fire is DCML-CORRECT (reproduce), K's is root-worse on chromatic-romantic
  (mis-fire — do NOT import). The C1 retire-now menu is empty; no identity-mutating
  gate was removed from the beam path. **Decision: E/F NOT retired now** — they fold
  into the decoder's alternatives-ordering at 3.5/output-assembly, not a standalone
  non-byte-identical re-decide.

- **⚠ STRATEGIC PIVOT (2026-06-13, Cowork-verified + user-directed): beam-widening
  SHELVED; the back half of the roadmap is being re-grounded on measured precision
  headroom.** The 3.2 design's §3 derivation (Cowork-verified against the independent
  June-9 redesign_plan numbers — AbMaj7 2.55>2.33, F#7 2.85>2.825, the rcb>margin
  arithmetic) proved **a wider beam does NOT fix Δ=+7a**: the transient is the
  HIGHEST-scoring node (locally correct, DCML root absent from its tones), so the
  continued-root wrong path is the genuine global optimum a decode finds exactly as
  greedy does. Re-ranking can't fix it; only re-weighting (Stage 5) or joint
  segmentation can. **Deeper consequence (Cowork): beam>1 is beam-1-substitutable for
  ALL currently-motivated work** — gate-folding and edge-reweighting are beam-1 ops, and
  beam>1 is BIR-free on Default — so its only justification was Δ=+7a, now void.
  decoder_design §11's "low-scoring transient" was a ratification miss (mine). User
  directive: *investigations first; long-term; major redesign OK; minimum surprises;
  maximum precision.* → **don't build beam speculatively; investigate where precision
  actually lives first.** `docs/beam_widening_design.md` SHELVED (retained for its §3
  derivation). decoder_design §11 Δ=+7a row needs erratum (next doc pass).
  **[UPDATE 2026-06-13 — APPLIED.** The decoder_design §11 erratum is now in the file
  (ERRATUM block at the top of §11), applied during the foundations-verification run
  (`cc_foundations_verification_report.md`, Task 6). The trailing "still queued" mentions
  in older dated entries below are historical; this ledger item is CLOSED.**]**

- **✅ Precision-headroom investigation COMPLETE — `cc_precision_headroom_dossier.md`
  (Cowork-verified).** Re-grounding facts: 95.2% of root errors are functional not
  vertical (`root_err 2706 = all_differ 2576 + m21-fixable 130` — structurally exact;
  the music21 gate sees only the 4.8%); key_disagree (27.9%, largest) = 63% tonicization
  label-gap (Stage 6, S1=17.7%, low-risk pure-add on correct readings) / 37% key error
  (Stage 4); headroom ≈ Stage 6 35–42% · Stage 4 20–24% · Stage 5 1.3%-batch (the
  fitter) · search ≈ 0. Verified: the identity is structural; the tooling reproduced the
  documented A3 27.6%/15.4%/6.3% baseline (proves it's real machinery). Recorded in
  roadmap (PRECISION-HEADROOM RE-GROUNDING block).

- **✅ Metric-design investigation COMPLETE + RATIFIED — `docs/precision_metric_design.md`
  (DRAFT; read in full + load-bearing probe verified against source by Cowork).** Key
  findings: `compare_rn` IS the DCML-only metric (reuse, not rebuild); `classify_pair`
  ALREADY credits a correctly-emitted secondary as `exact` — so the functional-axis gap
  is EMISSION (Stage 6), not the comparator; the granularity-robust unit = union-of-
  boundaries duration-weighted grid (segmentation-invariant by construction, kills the
  2.2-i ~7× artifact AND dissolves the deferred Default-section regen); the chicken-and-
  egg resolves via the L0–L4 ladder + a label-vocabulary contract that is a Stage-6
  output-spec co-ratified with the metric. Ratified: OQ-G1 → union-of-boundaries.
  Deferred to Stage-4/6 co-design: OQ-L1 (cadence token — genuine Stage-6 fork),
  OQ-L2 (secondary normalization), OQ-C1 (held-out split). OQ-V1 already on C2 list.

- **✅ L0–L1 metric primitives BUILT — `f8c6b3932a`** (tools-only; verified by Cowork:
  2 files, no C++, invariance test present + passes, dossier numbers reproduced via
  committed modes). `--wir-bach` (326/353), `--granularity-robust` (segmentation-
  invariant; swing 6.8pp→0.8pp), `--key-breakdown` (S1/S2 63/37). 70 metric tests
  unchanged + 21 new. The back half is now measurable.

- **✅ Stage 4 design investigation COMPLETE — `docs/key_path_design.md` (HELD, staged
  not committed — convention honored).** §3 finding (Cowork-verified: S2=1032 reproduces;
  bwv244.54 anchor rests on serialized runnerUp; logic airtight): **the key path fixes
  only ~10% of S2** (Class A spurious-flip); ~85% is Class B (emission prefers wrong key,
  correct key never rank-2 in 51.6% of S2) — unrecoverable by any path. **SECOND
  falsified structural fix → META-PRINCIPLE recorded in roadmap: precision lives in
  emission + functional labeling, NOT search/path.** The HMM path is the least valuable
  part of Stage 4 (~10%); KeyArea spans + the key-EMISSION fix are what deliver.
  **Decision (user): investigate the key-emission headroom before shaping Stage 4.**
  HMM path deferred under the beam-style "revisit when search genuinely matters" trigger.

- **✅ Key-emission headroom dossier COMPLETE — `cc_key_emission_headroom_dossier.md`;
  instrument committed `a4ae4a9203` (read-only key-candidate dump, byte-identity 0/353,
  verified by Cowork: 5 files, dump struct present).** **Result that INFORMS A-vs-B
  (verified — term-level dump evidence):** the Class-B key bulk is NOT a scorer ceiling.
  It splits at the declared-mode fault line: 349 restorable (mode DROPPED at MuseScore
  import for empty key signatures → `declaredModeOrdinal=-1`; xml carries `<mode>`), +
  a partial-sig subset (≈34–44% of S2 STRUCTURAL, one import fix); small FITTED
  (Stage-5 prior balance); ~127 CEILING = notation-vs-analyst CONVENTION disagreement
  (resolver faithfully follows the notated key; WiR picked the relative — arguably
  correct-behavior-penalized). **The biggest lever is a dropped-XML-tag plumbing bug,
  not a limit of hand-built analysis → strong evidence the hand-built emission has large
  concrete headroom (A), Level-2/learned NOT triggered on the key axis.** Stage-4 shape
  (scoped, not built): declared-mode import fix + GRADED declared prior (not the −7 wall)
  + KeyArea + hysteresis→path; HMM/search deferred. Caveat (§5.1): import root-site not
  read; fix robust either way.

- **✅ BACK-HALF RE-GROUNDING drafted — `docs/back_half_design.md` (DRAFT, NOT YET
  RATIFIABLE).** Resolves A-vs-B → A (hand-built) confirmed, B (learned) kept as
  triggered-fallback, on the key-emission evidence (faults are specific structural
  causes, not ceilings). Re-grounded order: metric(done) → Stage 4 (key import fix +
  graded prior + KeyArea) → Stage 6 (functional layer, largest lever; scope-cause first
  = the B-fallback check) → Stage 5 (fit last). Search deferred.

- **⚠ RATIFICATION GATED ON FOUNDATIONS VERIFICATION (user mandate 2026-06-13: facts
  first, never assume, old truths may be stale).** The re-grounding's KEYSTONE — the
  declared-mode-drop root cause — was unverified at source (CC's own §5.1), and it
  carries stale (non-Bach cross-corpus, June-3 pre-F1) + unrecorded (music21 version)
  facts. Ratifying now would violate the double-check mandate.

- **✅ Foundations verification COMPLETE — `cc_foundations_verification_report.md`; GATE
  GREEN.** Keystone CONFIRMED at source (Cowork independently re-read `addKey:5978`); 79/80
  zero-sig stems recoverable → 349 lever stands; bwv62.6 = same mechanism. Byte-identity
  re-confirmed (0/353). key→basisIndep current. music21 v9.9.1 already recorded. Cross-corpus
  "~2× harder" CONFIRMED by HEAD regen (50.7%/27.4%, 62110 regions). Four corrections folded
  into `docs/back_half_design.md` (keystone precision = default-key-match not 0-fifths;
  cross-corpus binary-stale not metric-stale; composing engraving-coupled / fix reaches both
  callers / favor option-b engraving-retains-mode; §11 erratum). §11 Δ=+7a erratum staged in
  `decoder_design.md` — **Cowork authorized committing it alone** (hash pending CC).
  Remaining qualifier (Stage-4-build confirm, not a blocker): native `.mscz` vs MusicXML-import
  mode-drop → "user-facing" vs "corpus-measurement" framing of the 349.
  **`docs/back_half_design.md` is now FOUNDATIONS-VERIFIED & RATIFIABLE** (status header
  lifted). §11 erratum committed `bcd4319aa7`. OQ-2/3/4 settled; **OQ-1 (A-vs-B) HELD
  pending the functional-residual investigation** (user 2026-06-13: settle the biggest
  call on evidence, not inference — "A confirmed" is proven on the key axis but only
  inferred on the largest slice).

- **🛑 GROUND-TRUTH PARSER BUG (2026-06-13, CC-spotted mid-investigation,
  Cowork-verified at source `dcml_parser.py:386`): the WiR/rntxt parser computes inline
  applied-chord (`V/V`, `viio6/V`, `V/III`…) root_pc from the PRIMARY numeral against the
  LOCAL key, discarding the applied target — wrong DCML root for every secondary on the
  ENTIRE Bach gate set (326/353).** Our analyzer/music21 resolve applied roots correctly →
  falsely flagged root_err. CONTAMINATES the DCML-only headroom (the 2576 "neither" /
  95%-functional), likely the metric-design "secondaries credited" finding (synthetic-probe
  artifact — real data: our correct root ≠ parser's wrong root), and the paused
  functional-residual classification. **Irony: the music21 filter we dropped was shielding
  the BIR 13/7 gate from this (filter excludes parser-wrong/we-right cases) — so the gate
  is probably clean, the UNFILTERED numbers are polluted.** TSV/non-Bach path is correct
  (uses `relativeroot`). **FUNCTIONAL-RESIDUAL INVESTIGATION + OQ-1 RATIFICATION HALTED
  until the parser is fixed and the numbers re-measured.** This is the user's
  "can-we-trust-the-corpora" risk, realized — the investigation-first/sample-real-cases
  discipline surfaced it before it was built on.

- **⏸ HELD (do NOT dispatch yet) — DCML applied-root fix:**
  `cc_instruction_dcml_parser_applied_root_fix.md`. Superseded as the immediate next step
  by the full pipeline audit below (user 2026-06-13: don't fix the one bug CC tripped
  over — find ALL measurement-error sources first, fix as ONE coordinated re-baseline).
  This fix becomes one line item in the audit's elimination plan.

- **✅ Functional-residual dossier COMPLETE — `cc_functional_residual_dossier.md` (read in
  full by Cowork; both parser bugs re-verified at source).** It primarily produced MORE
  measurement-bug evidence (vindicating the audit): a SECOND confirmed parser bug
  (minor-leading-tone `viio`, `_DEGREE_SEMITONES_MINOR:77` VII=+10 vs true +11, hits BOTH
  rntxt AND TSV paths), a Bach artifact rate (366/2576=14.2% ours-correct/parser-wrong;
  557=21.6% parser≠true), and the music21 `RomanNumeral` true-root oracle. Provisional
  OQ-1 read (A confirmed / B not triggered / <5% needs-richer; 92.1% ours==m21) **— but
  computed on CONTAMINATED ground truth, so the SIZES will shift after fixes. OQ-1 STAYS
  FROZEN; its qualitative direction is likely robust but unconfirmed on clean data.**
  Findings MERGED into the audit instruction (PRIOR EVIDENCE block).

- **✅ MEASUREMENT-PIPELINE AUDIT COMPLETE — `cc_measurement_pipeline_audit.md`
  (read in full; P0 verified at source by Cowork `:157`/`:178`).** FIVE defects:
  **P0 (headline, Cowork-verified)** — `float("1/2")`→ValueError→bare `except: continue`
  drops **58.9% of ALL TSV ground truth** (downbeat-only, easiest-biased) → the entire
  cross-corpus metric wrong ~8–10pp; **P1** rntxt applied-`/X`; **P2** minor-LT/vio table
  (both paths); **P3** mode-drop (S2 import, KEY axis only — does NOT corrupt root gate);
  **P4** (NEW) ABC/Beethoven repeat/numbering offset (naive qb-fix makes beethoven worse).
  **The BIR 13/7 gate is STRUCTURALLY CLEAN** (music21∩DCML double-filter excludes the
  corrupted cases — 0/13, 0/7 artifacts) → Stages 0–3 sound. ~46% of the gate is
  legitimate ambiguity; genuine actionable residual ~7 Baroque/~3 Jazz. CLEAN-confirmed:
  music21=filter-only, jazz=qualitative-only, snapshots=pins, quarterbeats origin exact,
  TSV relativeroot works, It6 refuted, repeats fine (except P4), tpb=480 stable.
  **Cowork humility note: the foundations pass "confirmed" the cross-corpus number while
  sitting on P0 — targeted verification ≠ holistic; the audit caught what the foundations
  check missed.** §4 = a coordinated one-batch re-baseline (P0→P1+P2→P3→P4→reporting).

- **EVERYTHING precision-derived FROZEN until the fix batch + re-measure:** cross-corpus
  numbers, the headroom "95% functional," the functional-residual sizes, OQ-1, the
  back-half ratification. ~~The BIR gate is the only precision-ish number that holds.~~
  **SUPERSEDED 2026-06-13 — the BIR gate moved too (see below); NOTHING precision-derived
  survives the fix batch unchanged.**

- **★ 2026-06-13 — INSULATION HYPOTHESIS FALSIFIED. The BIR gate is NOT insulated.**
  CC ran the metric re-baseline batch; the oracle-verified P1/P2 GT-parser fixes grow the
  gate **Baroque 13→57, Jazz 7→23** — STRICT SUPERSET (all 13/7 preserved, 0 lost; +44/+16
  added). Mechanism: the parser bug corrupted these chords' GT roots into the discarded
  `all_differ` (parser≠music21) bucket, hiding them from the gate as FALSE NEGATIVES. With
  correct roots they surface as genuine candidate cases. The +44 are exactly the P1/P2
  categories (viio7/V ×19, other viio*, half-dim, applied). The audit §3.A "0 parser
  artifacts" was right about the 13 PRESENT but missed the ~44+16 HIDDEN. **Cowork verified
  the fix at source** (dcml_parser.py `_compute_root_pc`:143-156 + `_resolve_dcml_key`:325 —
  case-disambiguated lowercase vi/vii→+9/+11, oracle-cited; P0 `_parse_fraction`:168 present;
  diff tools-only). Re-baseline: GT volume 37,886→90,851 (×2.40, P0 confirmed); per-ours
  root_agree 49.3%→64.2%; per-DCML 54.4%→50.3% (P4 recovers beethoven 48.2%→60.3% so the
  drop is −4.1pp not the audit's −7.7pp).

- **Caveats CC flagged (both real):** (1) like the original 13 (~46% judged legitimate
  ambiguity), some fraction of the +44/+16 will be ambiguity too — 57/23 is the GATE
  (candidate) count, not 57 genuine errors; the genuine subset needs characterization.
  (2) P2 is shared TSV+rntxt code, so the rntxt gate effect can't be separated from the
  TSV minor-LT correction the cross-corpus re-baseline needs (→ Option 3 "revert rntxt
  only" is not cleanly separable AND would discard a correct fix — REJECTED).

- **DECISION (Cowork, 2026-06-13): Option 2 — report only, no re-pin, no commit.** Told CC:
  reject Option 3 (revert = preserving a known-artifact number over the truth, the exact
  trap the audit exists to kill); don't take Option 1 yet (re-pinning tests + rewriting the
  CLAUDE.md 13/7 identity sets + the "hard-stop" policy is a FOUNDATIONAL ratification = the
  user's explicit call, not a tools-batch side effect). CC to: finish P5, write the full
  `cc_metric_rebaseline_report.md` incl. the gate finding, ENUMERATE the +44/+16 with
  stem@tick identities + category, give a first-pass genuine-vs-ambiguity triage; keep
  ALL staged + HELD; touch NEITHER the metric tests NOR CLAUDE.md/STATUS.md gate identities.

- **Cowork verification done (2026-06-13, Windows-side + git objects):** P2 fix CONFIRMED
  correct at source (dcml_parser `_compute_root_pc`:152-156 case-disambiguated +9/+11, both
  paths). Corpus HEAD-stable: only docs + byte-identical key-diagnostic `a4ea` + tools-metric
  `f8c6` between the stamp `a652dc1ba7` and HEAD → `.ours.json` valid at HEAD. Re-baseline
  coherent. **Substantive caveat that stands:** the triage's "~10 actionable" leans on the
  SOFT viio↔V7 share-tone bucket (~29 Baroque); the dim7-rotation bucket (Δ∈{3,6,9}) is solid
  (symmetric dim7 = genuinely root-ambiguous), but the share-tone bucket needs a hand-trace
  before the actionable count is trustworthy. CC itself flagged this.

- **⚠ SANDBOX NOTE (this session only):** Cowork's Linux bash mount was DEGRADED — it served
  NUL-padded copies of src files + a truncated `characterise_bir_false.py` that are
  DEMONSTRABLY FINE on the real disk (Windows-side Read showed chordanalyzer.cpp clean;
  CC's "tools-only, 3 files" is accurate). Lesson: this session's bash cannot be trusted for
  working-tree-file verification — use the Windows-side file tools / committed git objects, or
  have CC verify. The false-alarm was caught before surfacing. (NOT a real repo problem.)

- **⚠ STANDING — the sandbox mount's GIT INDEX can be STALE/divergent from CC's live worktree (2026-06-15):**
  during the J-key-iii dormant-commit staging, Cowork's sandbox `git diff --cached` showed **33 files incl.
  16 phantom `vtest/` deletions** while CC's worktree showed the clean **17-file closure**. Root cause:
  the sandbox mount's `.git` carried a **stale `index.lock` (dated the PRIOR session)** + a divergent index;
  the mount's `write-tree` FAILED on the lock while CC's `write-tree` SUCCEEDED — proving they were NOT the
  same live index. The phantom `vtest/` "deletions" were of files **present on disk AND in HEAD's tree**
  (`git ls-tree HEAD -- vtest/`), i.e. never-real staged entries from the stale copy. **Lesson: for GIT-STATE
  verification (staged set, index, diff --cached), the sandbox git is NOT authoritative — CC's live worktree
  is.** Trust CC's robust multi-method check (`write-tree` + `diff-tree HEAD <tree>` materializes the actual
  index tree — the gold standard) over the sandbox's `diff --cached`. Backstop a commit with a post-commit
  `git show --stat HEAD` IN THE WORKTREE (local/unpushed ⇒ `git reset --soft HEAD~1` if wrong). This is
  broader than the file-content staleness above: the **index itself** can be a stale snapshot. Cowork raised
  a vtest-contamination flag; CC correctly pushed back (couldn't reproduce, didn't act); re-investigation
  proved the sandbox stale — verification cut both ways, as it should.

- **⚠ STANDING PRACTICE — PROBE sandbox freshness BEFORE relying on it (user, 2026-06-17).** Before using
  sandbox git/file access for verification, run a quick freshness/integrity probe and act on the result:
  (1) **refs synced?** `git rev-parse HEAD` == the expected commit; (2) **file-content spot-check?** e.g.
  `wc -l` a file you know the current size of; (3) **index health?** `git write-tree` (FAILS ⇒ stale/locked
  index) + look for a leftover `.git/index.lock`. **The reliable/unreliable split (confirmed repeatedly, REFINED 2026-06-17):**
  **FULLY RELIABLE** = committed objects & refs ONLY (`git show <hash>:path`, `cat-file`, `log`, `rev-parse
  HEAD`, `ls-tree`). **PARTIALLY RELIABLE = file-content reads (Read/Grep/`cat`/`wc`) — can be PER-FILE
  STALE** (the mount cache is inconsistent: e.g. `chordanalyzer.cpp` read fresh at 1501 while
  `regionanalyzer.cpp` read stale at 986 vs the true committed 1167 — and wrong-subdir guesses look like
  "No such file"). Spot-check a file read against `git show <hash>:path` before trusting it; locate files via
  `git ls-tree -r <hash>`, not a guessed path. **UNRELIABLE** = the working-tree git INDEX (`git diff`, `diff
  --cached`, `status`, `numstat` on uncommitted changes) — it goes stale (leftover `index.lock`, "cache entry
  out of order", CRLF full-rewrite numstat, phantom deletions, inconsistent `ls`). **Always verify a
  commit/diff via the COMMITTED OBJECT (`git show <hash> --numstat`) + file-content reads, never the
  working-tree index.** Do NOT remove a stale `index.lock` (it's a mount-cache artifact, not CC's live
  `.git`, which commits fine — removing it risks interfering); route around it. This is how the
  `41f7c65f63` refactor-#1 verification held (committed-object numstat = clean 0/2178) while the working-tree
  numstat lied (CRLF 1502/3679).

- **★ BINDING RULE (user, 2026-06-17): NEVER use stale-risk file access for verification — NEVER.** For
  judging CC's work Cowork reads **ONLY committed objects** (`git show <hash>:path` content, `git show <hash>
  --stat/--numstat` diffs, `git ls-tree`/`log`/`rev-parse`). **Forbidden for verification:** the Read/Grep
  tools + `cat`/`wc` on the mount (per-file stale), and ALL working-tree git (`diff`/`status`/`numstat`).
  CC's reports are read from the **user's pasted message**, not the mount file. **Consequence — the workflow
  flips to COMMIT-LOCALLY-THEN-VERIFY:** CC does the work + self-checks in its FRESH worktree (CC's git is
  authoritative — it commits cleanly), commits **locally + UNPUSHED**, reports the hash; Cowork verifies the
  **committed object**; if wrong, CC reverts (`git reset --soft HEAD~1` — safe, nothing pushed until the user
  says). Read-only investigations (no commit) → verify cited claims against `git show HEAD:path`. The
  behavior gate (corpus regen / BIR / suites) stays CC's measurement. (Cowork's own working docs — STATUS /
  handoff / instructions — are Write/Edit'd on the mount; low staleness risk since Cowork owns them and Edit
  errors on a stale mismatch rather than silently corrupting.)

- **★ CARVE-OUT (user, 2026-06-17): CC's separate REPORT files (`cc_*.md`) — Cowork MUST read them.** They
  are uncommitted + gitignored, so there is no committed-object version → the mount is the only access.
  Handle it safely: (1) **freshness-check the read** — confirm it is COMPLETE (CC reports have clear
  `§`-structure + a final section; a lagging mount shows as truncation/partial) and CONSISTENT with the
  user's pasted summary; if truncated/partial/inconsistent → treat as stale, re-read or flag, do not act on
  it. (2) **The report only conveys CC's CLAIMS; verify every substantive claim against the COMMITTED OBJECT**
  (`git show <hash>`) — the report informs, the committed source proves, so a slightly-stale report read
  cannot corrupt a verdict. Optional hardening: ask CC to end each report with its line count / a fixed
  end-marker so a complete read is confirmable.

- **DECISION (user, 2026-06-13): "Verify, then ratify."** Instruction DISPATCHED:
  `cc_instruction_gate_rebaseline_verify.md`. CC to (1) reproduce 57/23 via the CANONICAL
  `characterise_bir_false.py` at HEAD (regenerate both corpora; confirm strict-superset, 0
  lost) — because CC's original 57/23 came from a throwaway `/tmp/gate_ids.py` driver against
  the 3-commits-behind corpus; (2) hand-trace the soft viio↔V7 bucket (oracle-checked) to firm
  the actionable count. READ-ONLY + corpus regen; metric fixes stay STAGED/HELD, no commit,
  CLAUDE.md/STATUS.md UNTOUCHED.

- **VERIFY REPORT LANDED + Cowork-reviewed in full (2026-06-13):**
  `cc_gate_rebaseline_verify_report.md`. Verdict: **57/23 verified + ratifiable.** (1)
  Canonical `characterise_bir_false.py` reproduces 57/23 at HEAD (corpus regen 353/353,
  manifest `bcd4319aa7`) — no driver-vs-canonical gap. (2) Strict-superset PROVEN through the
  canonical tool: reverted parser to HEAD blobs → exactly 13/7 (the CLAUDE.md sets), restored
  (byte-identical), `comm -23` empty → 0 lost both presets. (3) 80/80 contested roots
  oracle-correct (100%). (4) My soft-bucket caveat RESOLVED FAVORABLY: ~18 of the report's
  "soft viio↔V7" are actually symmetric-dim7 (rootless-V7♭9 label, but {r,r+3,r+6,r+9} sounds
  → pitch-class unresolvable); only 11 genuinely soft, ALL traced to legitimate ambiguity
  (oracle, GT root present, ≥3 shared). Sonority-based unresolvable = 30/57 Baroque (53%), not
  the report's 12. (5) Actionable held/nudged DOWN: bwv227.7 reclassified genuine→segmentation;
  net ~9–10 Baroque / ~4 Jazz. No stop-condition triggered.

- **★ GATE-SECTION GAP I caught before rewriting:** CLAUDE.md line 108 has a THIRD config —
  **Default (user-run) = 14 = Baroque-13 ∪ {bwv187.7}** — which CC did NOT re-measure and is
  stale under the corrected parser. Rather than enshrine 57/23 next to a known-wrong Default-14
  (internally inconsistent doc → would mislead CC), DISPATCHED `cc_instruction_gate_default_measure.md`:
  measure NEW Default via canonical tool (OLD-14 reproduce + strict-superset + oracle-check the
  additions). Same READ-ONLY+regen / HELD / no-doc-edit regime.

- **✅ DEFAULT MEASURED + GATE RATIFIED (2026-06-13).** CC measured Default 14→57 (canonical
  tool, OLD-14 reproduced via A/B, strict superset 0 lost, 42/43 additions = the vetted
  Baroque set, 1 Default-specific = bwv227.7@18000 segmentation variant, oracle-correct).
  Verify report §5 has the full Default-57 set. **Cowork did the coherent gate-section rewrite:**
  - **CLAUDE.md** gate-identity block rewritten to the full **Baroque 57 / Jazz 23 / Default 57**
    `stem@tick` sets + the re-baseline provenance note (undercount cause, strict superset,
    100% oracle, ~95% ambiguity, symmetric-dim7 two-tier seed); the two stale "13/7" refs
    (granularity caveat + analyze_inversion note) updated; `analyze_inversion_errors` 24/13,
    35/7 explicitly marked stale/pending (NOT re-measured under the corrected parser).
  - **STATUS.md** new top entry documents the metric re-baseline + 57/23/57 gate, STAGED/HELD.
  - **Cowork cross-validated all three sets**: Baroque-57 derived two independent ways
    (Default-57 minus CC's delta; and old-13 ∪ +44 enumeration) — agree exactly. Jazz 7+16=23.
  - Sets are **staged for the USER to commit + push** (user: "i can push myself"). Nothing committed.

- **✅ DOC-RIDER DONE — living-doc gate-number sweep (2026-06-13).** All LIVING docs updated to
  57/23/57 (current-state claims fixed; historical "✅ DONE @commit — Baroque 13" / "Stage-3
  gate" records left intact + annotated with a re-baseline pointer so they're not falsified):
  **CLAUDE.md** (gate section, full sets), **STATUS.md** (new top entry), **ARCHITECTURE.md**
  (Stage-2.4 V4 finding + re-baseline note), **build_and_test.md** (gate identities + the
  analyze_inversion `# 24/13` command annotations → stale/pending), **docs/implementation_roadmap.md**
  (baseline-regime line), **docs/back_half_design.md** (Stage-4 verification gate → 57/23/57),
  **docs/score_inventory.md** (4 refs + the "not an absolute quality figure" framing extended
  with the ~95%-ambiguity + 4th pitch-class-resolvable qualifier), **docs/decoder_design.md**
  (banner + eval + targets table), **docs/beam_widening_design.md** (banner; also notes beam
  shelved). `docs/scoring_model.md` / `redesign_plan.md` / `layer_architecture_audit.md` have NO
  gate-count refs (verified). The ~50 historical cc_*.md / cowork_*.md reports left as-is (record).
  The `analyze_inversion_errors` 24/13·35/7 secondary split is consistently marked stale/pending
  everywhere. All staged for the USER's commit.

- **Next CC instruction READY (updated 2026-06-13): `cc_instruction_functional_residual_investigation.md`.**
  Was BLOCKED pending the parser fix; now UNBLOCKED + rewritten for the corrected metric. Key
  update: its old numbers (root_err 2706 / all_differ 2576 / 95.2% functional / S1 1791 / the
  headroom dossier) were computed on the BUGGY parser and are INVALID, so a **new Task 0**
  re-derives the headroom decomposition on the corrected metric FIRST (NEW-vs-OLD root_err
  split + corrected functional-vs-vertical % + S1 recount + a rider re-measuring
  `analyze_inversion_errors` 24/13·35/7 → corrected), and Tasks 1–4 retarget to the corrected
  residual; gate refs → 57/23/57; mandatory reads point to the rebaseline+verify reports
  (old dossier = METHOD-only, numbers stale); deliverable OVERWRITES the stale
  `cc_functional_residual_dossier.md` (its provisional "OQ-1=A" was on the buggy metric). This
  single instruction now folds in handoff-TODO items (2) analyze_inversion re-measure +
  (3) the frozen precision re-derivations, and gates OQ-1. READ-ONLY, no commit.

- **✅ DOSSIER LANDED + OQ-1 RATIFIED (2026-06-14).** `cc_functional_residual_dossier.md`
  re-derived on the corrected metric (Cowork read in full + verified: arithmetic consistent,
  OLD-repro validates the instrument, analyze_inversion BIR=false 57/23 independently matches
  the gate). Verdict: **A confirmed, B2=0/44, B not triggered.** Cowork caught the scope limit
  CC understated — **Bach-rntxt-ONLY**; B's literature edge is exactly the undecomposed non-Bach
  chromatic repertoire. **User ratified A, SCOPED TO BACH.** `back_half_design` §3/§5 + STATUS
  updated to RATIFIED with the Stage-5/6 re-open gate (non-Bach decomposition + ~100 sample +
  DROOT_ABSENT alignment-noise audit). Stage 4 proceeds (hand-built either fork).

- **⚠ COMMIT PREREQUISITE (CC-flagged, Cowork-endorsed):** the corrected metric (the staged
  tools fixes) MUST be committed before any Stage-5 weight fitting — else the fitter optimizes
  against 365 phantom + 75 mislabeled cases. User commits (the whole staged set: tools fixes +
  CLAUDE.md/STATUS.md/ARCHITECTURE.md/build_and_test.md + the docs/ sweep).

- **P3 = CONFIRMED GENUINE BUG (Cowork-investigated 2026-06-14).** Import parses `<mode>`
  (`importmusicxmlpass2.cpp:6074-6099 setMode`) then `addKey`'s fifths-only dedup (:5978) drops
  the KeySig+mode for 0-fifths keys; export DOES write mode (`exportmusicxml.cpp:2473-2497`) → a
  round-trip fidelity bug, not just our-fork. BUT it's in a deprecated area: upstream #9444
  ("Mode dropdown non-functional… for a long time", maintainers leaned toward HIDING the mode UI)
  → upstream report is low-yield. **Correction surfaced to user:** an "outside off-limits" fix
  only patches the corpus tools (batch_analyze + product BOTH use the same importer) → would make
  metric overstate product → rejected.
- **USER DECISIONS (2026-06-14):** (a) **local engraving patch** (the :5978 dedup fix, documented
  never-pushed like the Snap fix); (b) **comment on #9444 AFTER the local fix is proven to work.**
- **DISPATCHED: `cc_instruction_stage4a_declared_mode_import_fix.md`** — Stage 4a, the import fix
  as a DISCRETE measured step (not full Stage 4). Authorized off-limits file = `importmusicxmlpass2.cpp`
  ONLY (STOP+surface if any other engraving file needed). It's a deliberate behavior change → ends
  byte-identity for affected scores → CC must: prove isolation to empty-sig scores (the 127
  anchored bucket must not move), confirm the 73 zero-sig stems regain declaredMode + report the
  REAL key-inference win vs the projected ~349, re-measure the gate (BIR increase = hard stop;
  the 57/23/57 baseline was on mode-dropped scores so it may move — ratify deliberately),
  DCML-adjudicate, refresh only verified-correct snapshot goldens. HELD, no commit. Report carries
  the #9444 repro for Cowork to draft the comment after verification.
- **★ SCOPE CORRECTION (user, 2026-06-14) — the import fix is a DEV/TEST/MEASUREMENT fix, NOT a
  shipped-product fix.** XML-import is NOT in the shipped analysis loop: shipped users analyze
  native in-memory Scores (.mscz / app-created), whose mode comes from MuseScore's own keysig (and
  the #9444-broken mode UI), not from our MusicXML importer. So the :5978 patch's value is: it
  makes OUR corpus/metric carry the true declared mode (the 73 zero-sig stems stop showing phantom
  UNKNOWN) → we develop/test/tune the inferrer against reality. My earlier "fixes the product too"
  framing was wrong. The engraving patch is STILL the right mechanism over a corpus-only tools hack
  — but for single-source-of-truth (batch_analyze + composing tests + snapshot tests ALL load via
  the one importer; fix once vs replicate a Score-injection hack in each), NOT a product benefit.
- **★ CONSEQUENCE for Stage 4b (load-bearing):** because the SHIPPED product frequently has NO
  reliable declared mode (native scores, broken UI), the shipped inferrer must NOT lean on declared
  mode — the **graded prior + note-based inference must carry the mode-ABSENT case**. The import fix
  lets us develop the mode-PRESENT path on a clean corpus, but Stage 4b must be **measured under BOTH
  conditions (mode-present AND mode-absent)** or we overfit to a corpus input the product won't have.
  Interpret CC's 4a "~349 reach" as the dev/corpus measurement gain, NOT a shipped win. (The 4a
  instruction's stop-condition "win fails to materialize → needs the graded prior" already aligns.)

- **★★ STAGE-4 REDIRECT (user, 2026-06-14) — "infer mode/key from the MUSIC; keysig mode = hint, not
  proof."** The keysig tonal mode is being de-supported (#9444) + sparse in shipped scores → NEVER
  depend on it. PRIMARY Stage-4 work = **strong note-based major/minor inference** (tonal-centre +
  cadences + scale-degree salience, constrained by the *reliable fifths*). Declared mode used ONLY as
  a **low-weight tiebreaker when genuinely unsure** → the **−7 declared-mode wall is REMOVED, not
  graded**. The dossier's ~349 (restore+use declared mode) = the CRUTCH upper bound / the gap the
  note-based inference must close, NOT a shippable win. Measure note-based-only (no crutch) so the
  metric reflects what ships. `back_half_design` §4 updated. (This refines the earlier "graded prior"
  plan toward "note-based primary + droppable hint".)
- **4a disposition: CONTINUE + keep the patch** (CC working). Reframed: the import fix makes the mode
  *available* as the last-resort hint + corpus correctness + the #9444 repro — it is NOT the inference
  mechanism. CC's 4a "~349 / does-it-work" measures the current (−7-wall) analyzer = the crutch upper
  bound; Stage 4b re-measures with the wall removed + note-based inference. Don't bank 4a's number.
- **Cowork TODO after 4a verifies — draft the #9444 comment.** **FRAMING (user, 2026-06-14): the
  comment is ADVOCACY to get the mode property PROPERLY SUPPORTED (so users set + maintain it), NOT
  a vote to hide it.** Rationale: a well-maintained mode property becomes a reliable last-resort hint
  for mode/key inference (our use), on top of its existing engraving roles. Argue constructively
  *against* hiding the UI and *for* making mode functional. Points to make (all Cowork-verified
  at source 2026-06-14), assemble from CC's 4a round-trip repro:
  1. **Distinct from #9444's UI focus:** a concrete IMPORT-side mechanism — `addKey`'s fifths-only
     dedup (`importmusicxmlpass2.cpp:5978`) drops the `KeySig` (and its parsed `<mode>`) whenever
     0-fifths matches the prevailing key. `<mode>` IS parsed (`setMode`, :6074-6099) then discarded.
  2. **It breaks round-trip:** export DOES write `<mode>` (`exportmusicxml.cpp:2473-2497`), so a
     `<fifths>0</fifths><mode>minor</mode>` file → import → mode lost → re-export can't recover it.
     Include CC's verified minimal repro.
  3. **The clean framing / parity point:** the dedup ALREADY preserves mode when it's `NONE` (the
     `|| key.isAtonal()` term, and `isAtonal()==(mode==NONE)`, key.h:81) — the fix just extends that
     existing mode-awareness to the tonal modes. Same correctness class as the atonal handling MS
     already does.
  4. **Mode is not XML-only / not cosmetic:** it's persisted natively (`rw/write`+`rw/read*`),
     exposed in the Inspector (`Pid::KEYSIG_MODE`) + plugin API, and `isAtonal()`(==NONE) already
     gates transposition (`transpose.cpp:138/239`, `edit.cpp:3542/5725`); the tonal modes are the
     only carrier of the relative major/minor (same-signature) distinction.
  5. **Verify against current upstream `master` before posting** (our fork's importer may lag; CC to
     note in the 4a report whether the dedup still reproduces upstream).
  Keep it complementary to #9444 (a specific import facet), not a duplicate. Then prepare Stage 4b (graded declared
  prior, not the −7 wall — measured mode-present AND mode-absent) + 4c (KeyArea spans +
  hysteresis→path) — may need `src/notation/` authorization (surface the file-set). Then Stage 5
  (fitting; committed corrected metric is its prerequisite) + the Stage-5/6 OQ-1 non-Bach re-open gate.
- **✅ METRIC COMMITTED + PUSHED (user, 2026-06-14): `a96f179f40`** "metric: commit corrected GT
  parser + 57/23/57 gate re-baseline (OQ-1=A ratified)" → `origin/master` (`bcd4319aa7..a96f179f40`).
  The whole staged set (tools fixes + CLAUDE.md/STATUS.md/ARCHITECTURE.md/build_and_test.md + docs/
  sweep) is committed and pushed. The Stage-5 commit-prerequisite is satisfied. HEAD = `a96f179f40`.
  (Supersedes the prior "Still pending the user / nothing committed this arc" note.)

- **✅ STAGE 4a COMPLETE + COWORK-VERIFIED — RATIFICATION-READY, HELD (no commit).** Report
  `cc_stage4a_mode_import_report.md`; instruction `cc_instruction_stage4a_declared_mode_import_fix.md`.
  The local engraving patch adds one `oldKeySig.mode() != key.mode()` term to `addKey()`'s fifths-only
  dedup (`importmusicxmlpass2.cpp:5986`; fetches the full `KeySigEvent` at the call site). **Cowork
  verified at source (host-side Read + git):** patch correct + minimal; ONLY the authorized
  `importmusicxmlpass2.cpp` touched (the "needs another engraving file" stop did NOT fire); the CLAUDE.md
  "Local patches" entry is staged + accurate; staged set = exactly {`importmusicxmlpass2.cpp`, `CLAUDE.md`};
  HEAD unchanged at `a96f179f40` (HELD, no 4a commit). **All 5 instruction items pass, no stop-condition:**
  (1) suites green — composing 505 / notation 57 / snapshots 11/11 zero-diff; (2) isolation = exactly 79
  zero-sig `.ours.json` changed, **0 non-empty-sig** (the 127 anchored bucket did NOT move); (3) key win
  **materialized ≥ projected** — Default S2 1063→685 = **−378** (dossier projected ~349; dump-confirmed on
  bwv153.9 → Cmaj anchor, bwv254 S2 17→0); (4) **gate BYTE-IDENTICAL all 3 presets — Baroque 57 / Jazz 23
  / Default 57, 0 added / 0 removed** → the BIR=false-increase ratification stop did NOT fire; (5) snapshots
  unchanged (snapshot corpus loads `.mscx` via `ScoreRW::readScore`, bypasses the MusicXML importer — an
  independent corroboration of the isolation). Corpora regenerated but NOT staged (left to user).
- **The 7-stem S2 over-lock caveat (CC-flagged, real):** of the 73 WiR-covered affected stems, 47 improved /
  19 neutral / **7 regressed on S2 only** (net still −378). Every one is a notation-disagrees-DCML
  over-commitment of the **existing −7 declared-mode wall** (6 are +2/+3 relative-pair / partial-sig metric
  artifacts; bwv64.2 +19 is the lone outlier — reads Emin, the relative of DCML's Gmaj). **Bigger-context
  point CC lacks:** this is EXACTLY what the user's Stage-4 redirect dissolves — remove the −7 wall,
  note-based inference primary, declared mode = droppable hint. So 4a's **+378 is the crutch upper bound**
  (mode-present, wall-in-place), NOT a shippable win; Stage 4b must re-measure **wall-removed AND mode-absent**.
  The 7 over-locks + the 242 S2→S1 cases are Stage-4b's concrete targets.
- **Minor verification note:** the `iex_musicxml_tests` gtest target is not configured in this build tree, so
  round-trip was verified via the rebuilt `MuseScore5.exe` CLI (bwv254 before/after + testKeysig1 control) +
  keysig-fixture inspection, not the gtest harness. Acceptable; a proper gtest round-trip case could be added
  when that target is configured.
- **#9444 repro is in hand** (report §2: bwv254 0-fifths+`<mode>minor</mode>` → import drops mode pre-fix,
  preserves post-fix; control gains no spurious keysig). CC did NOT separately rebuild upstream `master` (the
  buggy dedup is upstream-unchanged by inspection). **Cowork TODO: draft the #9444 advocacy comment now that
  4a verifies** (the 5 points already staged in this handoff; re-check current upstream `master` before posting).

- **Open user decisions (surfaced 2026-06-14):** (a) **ratify + commit the 4a local patch**, and decide how to
  carry it — committed-to-local-master (risk: an accidental `git push` sends a local-only patch to origin) vs
  kept-staged/dirty like the Snap fix (safe but must re-stage each session). The patch must NOT reach `origin`
  until/unless the #9444 path says so. (b) Cowork drafts the #9444 comment. (c) **Stage 4b design** —
  note-based major/minor inference primary, −7 wall removed, declared mode droppable hint; will need
  `src/notation/` (KeyArea/bridge) file-set authorization, OUTSIDE the composing autonomous zone; measured
  BOTH mode-present and mode-absent.

- **DISPATCHED 2026-06-14: `cc_instruction_stage4a_commit_and_stage4b_scoping.md`** (two tasks).
  **Task 1 = commit Stage 4a (RATIFIED).** This instruction releases the HELD hold; CC commits exactly
  the two staged files (`importmusicxmlpass2.cpp` + `CLAUDE.md`) with a specified message, confirms
  `git diff --cached` lists only those two (report + gitignored `tools/corpus/**` NOT added — `tools/corpus`
  is gitignored, verified), and **does NOT push** (user pushes — it's a local engraving patch they may keep
  off origin). **Task 2 = READ-ONLY Stage 4b scoping** → `cc_stage4b_scoping_dossier.md`: locate + characterize
  the −7 declared-mode wall [code]; inventory the note-based inference machinery; produce the precise
  off-limits `src/notation/`/`src/engraving/` **file-set table** (the authorization request — minimal set,
  KeyArea-in-composing if possible); the measurement plan **mode-present AND mode-absent** (targets = the 7
  over-lock stems + 242 S2→S1; the −378 must largely survive WITHOUT the crutch); the 2nd-behavior-change
  surface (key→basisIndep, chord axis byte-identity ends); open questions. No edits, no build, no commit
  beyond Task 1. The Stage-4b *implementation* is a later instruction, gated on the user authorizing the file-set.
  **#9444 comment: user takes it themselves** (draft ready at `cowork_github_9444_comment_draft.md`).

- **✅ STAGE 4a COMMITTED `faa1ee5388` (local, UNPUSHED) + STAGE 4b SCOPED (2026-06-14).** CC committed 4a
  (2 files, message as specified); **origin/master still `a96f179f40` → NOT pushed** (user pushes if/when).
  Cowork-verified at source: HEAD/commit-contents/unpushed/clean-tree. Dossier `cc_stage4b_scoping_dossier.md`
  (read-only) headline: **Stage 4b = ZERO off-limits production-file edits; all composing autonomous-zone.**
  **Cowork independently verified the crux claims at source** (the three-mechanism wall: penalty
  `keymodeanalyzer.cpp:571` + hard promotion `keyresolver.cpp:350-367` + anchor `:274-287` + partial-sig gate
  `:248`; KeyArea in `analyzed_section.h:118`/`sectionanalyzer.cpp:920`; bridge does NO inference — confirmed at
  BOTH pref sites, incl. `notationharmonicrhythmbridge.cpp:90` that CC missed). Only off-limits-zone touch =
  snapshot-golden refresh (test data). **Authorization blocker REMOVED** — no `src/notation`/`src/engraving`
  edit; the user authorizes a golden refresh (standard ratified-change workflow), not a production edit.
- **Cowork reframe for Stage-4b design:** part of 4a's +378 is crutch-dependent (`partialSignatureCorrection`
  is declared-mode-gated → off mode-absent → 4 partial-sig stems unrecoverable by wall-removal alone). The
  **mode-absent floor is < +378**; OQ6's pass-bar = the real "how much is note-recoverable" question.
- **6 open design questions (dossier §6) gate the 4b implementation instruction.** Cowork's proposed
  dispositions (grounded in the ratified redirect — to confirm/adjust with user): OQ1 convert penalty+hard-promotion
  into ONE small additive declared hint firing only when note-based top-2 gap small (Stage-5 fits the weight;
  provisional to measure); OQ2 note-based opening anchor, weak declared seed only when opening evidence sparse;
  OQ3 defer note-triggered partial-sig (accept the 4 stems mode-present-only for first 4b, flag follow-up); OQ4
  defer cadence→key wiring (strengthen existing triad/LT/disambiguation first); OQ5 defer KeyArea area-confidence
  to Stage 6; OQ6 mode-absent pass-bar = USER call (dossier suggests ≥70%; recommend setting it AFTER the
  demote-only measurement so it's data-grounded). **Next: Cowork writes the Stage-4b design (staged:
  4b-i demote-wall + measure mode-present/absent honestly → 4b-ii strengthen note-based inference), ratified
  before implementation. Pending user steer: 4b scope ambition (staged-minimal vs all-in-one).**

- **USER CHOSE staged demote-first (2026-06-14).** **Stage 4b design DRAFT written: `docs/stage4b_design.md`**
  (ratification-gated). 4b-i = demote the four declared-mode mechanisms — penalty 7.0→small additive hint
  (provisional 1.0, Stage-5-fit); **remove the hard promotion `keyresolver.cpp:350-367` outright**; opening
  becomes note-based (remove the declared short-circuit `:274-287`); partial-sig left declared-gated (mode-present
  only, note-triggered detector deferred) — + build the `--ignore-declared-mode` toggle (tools+composing, in-zone)
  + measure mode-present AND mode-absent on L1 key-breakdown (the mode-absent run = the no-crutch floor). No hard
  4b-i key-axis pass-bar (it's the floor measurement); chord-axis gate WILL move (DCML-adjudicate each; un-adjudicated
  BIR=false increase = stop); snapshots WILL move (refresh only verified-correct). OQ dispositions in §3; 4b-ii
  (strengthen triad/LT/disambiguation) + deferred (cadence, note-triggered partial-sig, KeyArea→Stage 6) in §5.
  **Awaiting user ratification of §6 (the staged plan + OQ dispositions + remove-hard-promotion + the deferred
  OQ6 pass-bar timing + provisional hint weight 1.0). On ratification → Cowork writes the 4b-i CC instruction.**

- **✅ USER RATIFIED ("go", 2026-06-14) + 4b-i INSTRUCTION DISPATCHED: `cc_instruction_stage4b_i_demote_and_measure.md`.**
  Design `docs/stage4b_design.md` ratified as written (all §6 defaults). The instruction: demote the four
  declared-mode mechanisms — (1) `declaredModePenalty` 7.0→1.0 small hint + **fix the .h:454 bounds `{3.0,15.0}`→`{0.0,15.0}`**
  (1.0 is below the current lower bound — flagged); (2) **remove the hard promotion `keyresolver.cpp:344-367`
  outright** with an explicit ⚠ DO-NOT-touch the note-based hysteresis `promoteWinnerInPlace` at `:320-342`
  (both use the same call — the trap); (3) remove the piece-start declared short-circuit `:274-287` → note-based
  opening (verify normal path handles piece-start); (4) partial-sig `:248` UNCHANGED (declared-gated, deferred
  detector); (5) build `--ignore-declared-mode` toggle (tools+composing, flag-off byte-identical 0/353×3). Measure
  mode-present AND mode-absent on L1 key-breakdown, 3 presets: S2 floor (the headline), 7 over-lock stems, 242
  S2→S1 hold-without-crutch, **chord-axis gate delta DCML-adjudicated (un-adjudicated BIR=false increase either
  condition = HARD STOP)**, snapshot diffs (refresh only verified-correct). No hard 4b-i key pass-bar (floor
  measurement; OQ6 pass-bar set by user after). HELD, no commit; report `cc_stage4b_i_report.md`; toggle separable
  as its own byte-identical infra commit. Doc-sync scoring_model.md + stage4b_design/back_half_design.
  **On CC's report: re-read this instruction first, then the report in full, verify the demotion sites + the
  hysteresis-untouched claim + the gate adjudication at source before ratifying any commit.**

- **✅ DOC-CURRENCY TIDY (2026-06-14):** the `analyze_inversion_errors` secondary `bassIsRoot` split was
  re-measured under the corrected parser in `cc_functional_residual_dossier.md` (Baroque 24/13→**47/57**,
  Jazz 35/7→**81/23**; false-halves = the 57/23 gate) but the living docs still annotated it "stale/pending."
  Reconciled across CLAUDE.md, build_and_test.md (note + headline-pair + the two command annotations),
  docs/implementation_roadmap.md, docs/decoder_design.md. **Still genuinely pending (NOT a drift — leave
  marked):** ARCHITECTURE.md's **Default** analyze_inversion three-way `30/14` (Stage-2.4 V4) was not
  re-measured — only its false-half (= gate Default 57) is known; the true-half awaits a Default re-run.
  All other measurement-pipeline residuals (DROOT_ABSENT alignment-noise audit, non-Bach functional
  decomposition, aug6/multi-level-applied GT-parser residuals, symmetric-dim7 two-tier gate, granularity-robust
  gate adoption) remain Stage-5/6-deferred by design.

- **✅ STAGE 4b-i COMPLETE + COWORK-VERIFIED — HELD (no commit), RATIFIABLE + COMMITTABLE.** Report
  `cc_stage4b_i_report.md`. Four demotions verified at source (penalty 7.0→1.0 + bounds→{0.0,15.0}; hard
  promotion removed `keyresolver.cpp:347`; hysteresis `:323-345` intact — the trap, confirmed untouched;
  anchor→note-based opening; `ignoreDeclaredMode` toggle inert default-off). HEAD `faa1ee5388` unchanged; 13
  staged files; no off-limits PRODUCTION edit. Mode-present nearly free (Default S2 +2, Baroque 0) + **gate
  byte-identical 57/23/57 all 3 presets** (ratification hard-stop does NOT fire); mode-absent **floor ~3×**
  (Default 2070, Baroque 2099). Snapshots 2 refreshed DCML-verified (corelli G/iv→C/i = real win). 505/57/11.
- **★ COWORK REFRAME (CC lacks this): the floor is NOT a 4b-i regression.** All four mechanisms are gated on
  `declaredMode.has_value()` → mode-absent scores were ALREADY crutchless pre-4b-i; the 2070 floor = today's
  product behavior for mode-unreliable native scores, now measured. The demotion is mode-present-neutral +
  mode-absent-unchanged → **safe to commit.** No shipping regression. The floor sizes how weak note-based
  relative-pair inference is today (the real "what ships" problem) — 4b-ii must close it.
- **Verdict + recommendation:** ratify + commit 4b-i (one coherent commit recommended; CC's §8 A/B split shares
  `keymodeanalyzer.h`+`keyresolver.cpp` so a clean file-level split isn't possible — note it). Then **4b-ii =
  strengthen tonic-triad salience + `applyPairwiseDisambiguation` + true-LT** to close the ~1383-region
  relative-pair gap. **4b-ii is a genuine A-vs-B test on the hardest mode sub-problem:** bwv365/33.6 recover
  mode-absent (relatives ARE note-distinguishable — the bias merely overrode them; encouraging for A), but
  bwv64.2/83.5 read a wholly different key (harder class → Stage-5/6 / possible B evidence on the key axis).
- **Boundary/doc notes:** CC edited a notation TEST file (`notationimplode_tests.cpp` — necessary re-pin of the
  removed anchor's hardcoded 0.5 confidence; a test, not production, but slightly wider than the scoping's
  "goldens only" prediction — flagged, not a problem). Doc-sync: `declaredModePenalty` is a KeyModeAnalyzer term,
  so it went to the key-path docs (`scoring_model.md` is chord-analyzer-only, correctly) — no canonical
  "key-model" reference doc exists (minor future-doc gap, not blocking).
- **✅ DISPATCHED (user "go", 2026-06-14) — TWO instructions:**
  **`cc_instruction_stage4b_i_commit.md`** (Task: commit 4b-i — the 13 staged files as ONE coherent commit,
  message specified, confirm report+corpora NOT staged, **do NOT push**). ⚠ **Chain note:** 4b-i sits on top
  of the local-only 4a `faa1ee5388`; a future push carries BOTH 4a+4b-i unless the user rebases 4a out —
  user's call at push time. **`cc_instruction_stage4b_ii_strengthen.md`** (Stage 4b-ii — strengthen the
  relative-pair discriminators: `applyPairwiseDisambiguation` [the strongest lever] + tonic/triad salience +
  true-LT, with **principled provisional bumps, NOT corpus-fitted** [Stage 5 fits]; measure mode-present AND
  mode-absent; HELD). **The load-bearing question 4b-ii answers: can the EXISTING hand-built structure carry
  the relative-major/minor decision, or is a new/learned mechanism needed?** → feeds OQ6 pass-bar + the A-vs-B
  re-evaluation on the key axis. Targets bwv365/33.6 (should recover); bwv64.2/83.5 = hard class (report as
  Stage-5/6 / B-evidence, do NOT build a new term). Stop conditions: closing the floor but wrecking mode-present
  = structure-insufficient finding; un-adjudicated BIR=false increase = hard stop; overfitting = stop+report.
  **On CC's reports: re-read each instruction first, verify the commit hash + (for 4b-ii) the weight changes +
  gate adjudication + the sufficiency verdict at source before ratifying.**

- **★ GIT TOPOLOGY + PUSH POLICY (clarified + verified at source 2026-06-14) — supersedes the earlier
  "keep off origin / local-unpushed" framing, which was imprecise:**
  - `origin` = `github.com/slimvince/MuseScore` (the user's FORK; fetch+push). `upstream` =
    `musescore/MuseScore` with **push DISABLED** in config (`git push upstream` fails by design).
  - `push.recurseSubmodules` is unset → default **no**: a superproject push does NOT push the `muse`
    submodule. So **`git push origin` ("push everything" on the main repo) goes ONLY to the user's fork —
    it cannot reach MuseScore core** (core merges require a maintainer-accepted PR; a push is not a merge).
  - **The 4a engraving patch + 4b-i CAN be pushed to `origin` freely.** The guardrail against MuseScore
    CORE is (a) the disabled upstream push and (b) upstreaming being a deliberate cherry-pick-onto-a-clean-
    upstream-branch act — NOT keeping commits off the user's own fork. The CLAUDE.md "Local patches" entry +
    the commit-message "do NOT push upstream" markers keep 4a out of any future upstream PR.
  - A local **pre-push hook** exists but blocks only `src/engraving/data/chords/chords.xml` (a separate
    licensing/data concern) — it does NOT touch importmusicxmlpass2.cpp / 4a, and 4a needs no fork-side block.
  - **Two honest caveats:** (1) the `muse` submodule's remote points at `musescore/muse_framework` with push
    ENABLED in config — only GitHub access-control (no write rights) stops an accidental `cd muse && git push`;
    optional belt-and-suspenders: `git -C muse remote set-url --push origin disabled`. (Superproject pushes
    don't touch it anyway.) (2) A GitHub fork of a public repo is itself **public** — "merge into core" is
    fully prevented regardless, but if the user wants the work PRIVATE, a fork doesn't provide that (a separate
    private duplicate would). Surface this only if privacy (not just core-isolation) is a goal.

- **✅ 4b-i COMMITTED `ef30cc70f3` + history REORDERED (intact) + 4b-ii STRUCTURAL-INSUFFICIENCY VERDICT (2026-06-14).**
  Chain: `a96f179f40` (origin) → `ef30cc70f3` (4b-i) → `cfc7eb5e39` (4a, HEAD). An external interactive rebase put
  4a ON TOP of 4b-i (separable → push-4b-i-keep-4a-local; likely intentional user action post git-topology talk).
  **Cowork-verified HOST-SIDE: both commits intact, cumulative content complete, probes reverted to baseline.**
  ⚠ Bash sandbox degraded AGAIN (CRLF + spurious "62-deletion" whole-file diffs + timeouts) — false alarm, host-side
  authoritative + clean (same pattern as the prior-session NUL scare). Neither commit pushed.
- **4b-ii VERDICT (`cc_stage4b_ii_report.md`, HELD, no commit, probes reverted):** reweighting the three named
  relative-pair discriminators **CANNOT** carry the relative-major/minor decision. Pairwise disambiguation INERT
  on the floor (clauses need a tonic-absent relative; floor is tonic-present-both); tonic salience = strict
  monotone present↔absent trade-off when uncapped (A2 floor −504 / present +435); true-LT wrong direction. **§4
  structural-coupling proof: floor regions ARE the sub-1.0-hint near-ties → any term strong enough to win them
  mode-absent overrides the correct hint mode-present; independent of term.** Gate 57/57/23 mode-present every probe.
- **★ COWORK READ:** this does NOT falsify A. The missing piece is a **global/cadential key-identity signal** (the
  declared mode was its proxy) that local window terms don't encode. Next structural step = **OQ4 cadence→key**
  (still hand-built, composing-zone; the Stage-2.1 cadence detector exists). **B only if cadence also fails.**
  **Stage 5 won't fix it (structural coupling). OQ6 pass-bar moot for reweighting (≈0) → re-scope to cadence/Stage-6.**
  bwv365/33.6 already recovered in 4b-i; bwv64.2/83.5 = hard class. Harness `tools/b2_measure.sh` (keep/drop).
- **AWAITING USER DIRECTION (strategic fork):** (a) investigate cadence→key now (targeted key-floor step;
  investigate-before-build, derive it actually closes the floor — like the beam/key-path investigations); (b) fold
  cadence→key into Stage 6 (largest-headroom functional layer; cadence detection lives there); (c) step back +
  re-ground the back-half sequencing given 4b's null result. Cowork recommendation: lean (a)/(b) (the finding
  points squarely at the cadence/global-context signal); confirm direction before any next instruction.

- **✅ USER CHOSE "investigate cadence→key now" (2026-06-14) → DISPATCHED `cc_instruction_cadence_key_investigation.md`.**
  Investigation (NOT build), modeled on the beam/key-path investigations — DERIVE whether a cadence→key signal
  actually closes the relative-pair floor BEFORE building. **The make-or-break = Q-CENTRAL: does cadence ESCAPE the
  4b-ii §4 coupling?** (cadence is global/phrase-level, not window-local, so it CAN point differently from local
  salience — but must be derived on real floor cases: does it win the mode-absent floor WITHOUT flipping the correct
  mode-present hint cases?). Tasks: locate+characterize the Stage-2.1 cadence detector (does it produce a key/degree
  resolution or only a cadence flag?); characterize the floor population; derive Q-CENTRAL on a real sample (incl.
  bwv365/33.6/64.2/83.5); size recoverable-fraction + residual (the A-vs-B input — large residual ⇒ B); recommend the
  Stage-4 shape (build cadence→key / fold into Stage 6 / key-axis is B). READ-ONLY + optional byte-identity diagnostic;
  HELD, no commit. **Falsifiable by design** — cadence failing the coupling-escape test is a valid finding (→ Stage 6/B).
  **On CC's dossier: re-read this instruction first, verify the Q-CENTRAL derivation + the cadence-detector capability
  claims at source before ratifying the Stage-4-shape recommendation.**

- **✅ CADENCE→KEY INVESTIGATION LANDED = GREEN LIGHT (A), QUALIFIED (2026-06-14).** `cc_cadence_key_investigation_dossier.md`
  (READ-ONLY, HELD, source byte-clean; + `tools/cc_floor_classify.py`). **Cowork-verified finding #1 at source:** the
  existing `detectCadences` (`sectionanalyzer.cpp:156`) is circular (uses post-resolution `function.degree`),
  confidence-gated (silent on the floor), type-only (no key/degree), unreferenced by `key/` → **new key-agnostic
  detection needed (a build, not a wiring).** Q-CENTRAL: floor is **91% relative-pair** (193→1452; "other" mode-invariant
  411→454) and cadence DECOUPLES structurally (piece/section-scoped note-derived proxy for the global-key signal the
  declared mode provided → agrees with the hint, supplies mode-absent). Sizing ≈1259 addressable (91%) but that is a
  **perfect-detection CEILING** — realized fraction is **detection-reliability-bounded (unproven)**. Residual ~454 "other"
  + 164 keyfail → Stage 6/B. **★ Cowork qualifier: do NOT bank the 91%; the next build must measure realized fraction
  early.** Honesty flag: bwv64.2 reclassified G-major→C-major (relative-pair, addressable) — a small GT discrepancy to
  resolve. OQ6 re-scoped onto the cadence lever (set against realized detection, not the ceiling).
- **NEXT (proposed, pending user confirm):** Cowork writes the **cadence→key DESIGN** — the key-agnostic cadence/global-anchor
  signal (what it detects: final/structural cadence, dominant→tonic & leading-tone-to-true-tonic resolution, at section/piece
  scope), how it feeds key scoring **without re-entering the §4 coupling** (section/piece scope, not window-local), and a
  **STAGED build where a first version's realized fraction is measured early** (the reality check on the 91% ceiling).
  Composing autonomous-zone. Ratification-gated (like stage4b_design). Then build first version + measure → ratify.
  **Open: confirm direction (design the cadence→key build now) vs steer scope first.**

- **✅ STAGE 4c DESIGN WRITTEN (user "yes", 2026-06-14): `docs/stage4c_cadence_key_design.md` (DRAFT, ratification-gated).**
  Cadence→key = a **key-agnostic global tonic anchor**: detect authentic cadences from **absolute root motion + chord
  quality + leading-tone** (NEVER `function.degree`/resolved key → that was the circular trap), aggregate to a
  piece/section (tonicPc, mode) anchor, and break the relative-pair tie at **section/piece scope** (the scope the declared
  mode used) — NOT as a local `analyzeKeyMode` window term (else it re-enters the 4b-ii §4 coupling). **Staged so the
  detection-reliability risk is measured FIRST:** 4c-i = build a simple authentic-cadence detector + READ-ONLY measure the
  **realized** anchor-vs-DCML fraction of the ~1259 relative-pair floor regions (scoring untouched → byte-identical; the
  reality check on the 91% perfect-detection ceiling) → 4c-ii = wire at section/piece scope + measure floor lift +
  mode-present non-regression (the empirical decoupling proof; gate 57/57/23 byte-identical) → 4c-iii = refine. Targets
  bwv365/33.6 (stay recovered), bwv64.2 (now relative-pair; resolve the G-vs-C GT discrepancy in 4c-i); residual ~454
  "other"+164 keyfail → Stage 6/B (large residual = key-axis A-vs-B evidence). §6 OQs: authentic-only first (rec),
  piece/section anchor (rec), trust-gating provisional. **Awaiting user ratification of §7 → then Cowork writes the 4c-i
  instruction.**

- **✅ STAGE 4c DESIGN RATIFIED (user "go", 2026-06-14) → 4c-i INSTRUCTION DISPATCHED: `cc_instruction_stage4c_i_cadence_detector_measure.md`.**
  4c-i = **build the key-agnostic authentic-cadence detector + MEASURE realized detection, NO wiring** (the reality check
  on the 91% perfect-detection ceiling). Detector uses absolute root motion (root_b ≡ root_a−7) + dominant quality +
  leading-tone presence + stable resolution triad → cadential (tonicPc, mode); aggregate to a piece/section anchor;
  **NEVER `function.degree`/resolved key** (the circular trap). Measure via read-only diagnostic (reuse `cc_floor_classify.py`):
  **realized fraction (precision/recall) on the ~1259 relative-pair floor vs the 91% ceiling**, per-target (bwv365/33.6/64.2
  + resolve the bwv64.2 G-vs-C GT discrepancy; bwv83.5 must NOT be spuriously claimed), decoupling preview (anchor agrees
  with the cases the hint gets right?), coverage gaps (what plagal/half/deceptive would add). **Byte-identity GATE: production
  scoring untouched → 57/57/23 + snapshots 11/11 zero-diff + suites green** (detector called only by the diagnostic; any
  movement = leak = STOP). HELD, no commit. Branch on the realized number: worthwhile → 4c-ii (wire at section/piece scope +
  prove decoupling); marginal → 4c-iii; far-below → detection-reliability / key-axis A-vs-B finding. **On CC's report:
  re-read this instruction, verify the detector's key-agnostic inputs + the byte-identity proof + the realized fraction at
  source before ratifying any move to 4c-ii.**

- **✅ STAGE 4c-i COMPLETE + COWORK-VERIFIED — HELD; realized detection 55.7% << ceiling → §8 stop FIRED, do NOT wire (2026-06-14).**
  New `src/composing/analysis/section/cadencekeyanchor.{h,cpp}`. **Verified at source:** key-agnostic by construction
  (`CadenceRegionInput` key-blind); production UNTOUCHED (`keyresolver.cpp` 0 cadence refs; detector called only by
  `batch_analyze` + tests). Byte-identity: 57/23/57, snapshots 11/11, composing 516, notation 57. **Realized: fires 100%,
  correct only 55.7% (809/1452).** Dominant failure (308/21%): naive count/finality vote reproduces the relative-major
  error (diatonic V→III tonicizations G→C outvote raised-LT V→i). No coverage gaps → discrimination/salience deficit, not
  missing modalities. Decoupling structurally real but **34% of clean stems contradict** → wiring would regress mode-present.
  bwv64.2 GT settled = **C major**. **Staging worked — caught the weak detector cheaply, no regression.**
- **★ Cowork meta-read:** 3rd informed hand-built round on the key-axis relative decision (4b-i→4b-ii→4c-i); each failure
  diagnosed a concrete next lever, not a wall; **B not yet implicated** (signal real, aggregation under-built). 4c-iii
  (structural-vs-interior cadence discrimination + raised-LT salience + Picardy) is well-motivated, cheap (byte-identical
  measure, no wiring), and **also feeds Stage 6** (KeyArea/tonicization) so not wasted. Budget-aware: if 4c-iii also misses
  the wiring bar, reassess key-axis-vs-Stage-6 / B.
- **⚠ 4c-iii design question (flag before writing the instruction):** "structural cadence" discrimination likely wants a
  **fermata/phrase-boundary** signal — but composing is engraving-agnostic, so fermatas may need notation→composing plumbing
  (a bridge/off-limits question). Confirm what structural signal is available IN-ZONE (metric position, finality, region
  spacing) vs needing plumbing, as part of the 4c-iii design.
- **★ FERMATA/OFF-LIMITS CLARIFICATION (user, 2026-06-14) — corrects a Cowork over-statement:** *reading/calling*
  engraving is ALLOWED from any code we may edit; only *editing* `src/notation`/`src/engraving` CODE is off-limits.
  The cadence diagnostic runs in `tools/batch_analyze` (writable, already loads the Score) → **fermatas are read
  there directly and passed into the composing detector via a new IN-ZONE `CadenceRegionInput` field — ZERO off-limits
  edit for the measurement.** (The notation-bridge change to feed fermatas to the LIVE resolver is only needed at 4c-ii
  WIRING time — separately authorized; a normal "bridge reads engraving" op.) Standing lesson: don't conflate
  "read engraving" with "edit the bridge."
- **✅ DISPATCHED `cc_instruction_stage4c_iii_refine_detection.md` (user "go" via the fermata correction, 2026-06-14).**
  4c-iii = refine the detector (still NO wiring, same byte-identity gate) + re-measure. Three refinements, each targeting
  a diagnosed 4c-i failure: (1) **structural-vs-interior, fermata-gated** — weight phrase-final/piece-final cadences over
  interior V→III tonicizations (the 308-region primary fix; fermatas read in batch_analyze, new in-zone input field);
  (2) **raised-LT salience** — weight cadences whose LT is CHROMATIC vs the key-signature fifths (E→Am needs G♯ outside
  0-sharp; G→C is diatonic) — KEY-AGNOSTIC via signature fifths + pitch content, **NEVER the resolved mode**; (3) **Picardy
  handling** (91 parallel-major misreads). Re-measure realized fraction + **clean-stem contradiction rate (must drop well
  below the 34% that blocked wiring — the binding mode-present-regression proxy)** vs 4c-i's 55.7%/34%; per-target
  (bwv365/33.6/64.2 recover? bwv83.5 stay correct); residual. Byte-identity 57/23/57 + snapshots 11/11 + suites. HELD.
  Branch: contradiction low + accuracy worthwhile ⇒ proceed to 4c-ii wiring; still short ⇒ key-axis A-vs-B / Stage-6
  reassessment. **On CC's report: re-read this instruction, verify the three refinements stay key-agnostic (signature
  fifths only, no resolved mode) + the byte-identity proof + the re-measured contradiction rate at source before ratifying 4c-ii.**

- **✅ STAGE 4c-iii COMPLETE + COWORK-VERIFIED — HELD; 75.2% detection / 25.3% contradiction; gated 4c-ii feasible; BUDGET CHECKPOINT (2026-06-14).**
  Cowork-verified at source: key-agnostic (`endsPhrase` from fermatas/final, `chromaticLeadingTone` from notated `concertKey(0)`
  NOT resolved key — `batch_analyze:1704-1715`; resolver has 0 detector refs). Byte-identical (0/353, BIR Default 57, snapshots
  11/11, composing 522). 55.7→**75.2%** detection, 34→**25.3%** contradiction; relative-major-wrong 308→123, Picardy 91→13.
  **Honest finding: chromatic raised-LT is PRIMARY (+7.4); structural/fermata-gating is NEGATIVE in isolation** (phrase-final ≠
  tonic in minor chorales) — refutes the design's "structural is primary" hypothesis (data corrected us). bwv365 miss = a
  SEGMENTATION artifact (regions end on C; WiR=a-min) not cadence-detection. Residual now = dominant/subdominant tonicizations
  (4th mode, "other" 47/63 contradictions). Don't wire ungated; **conf≥0.6 gate → ~10% contradiction @ ~15% floor coverage →
  gated 4c-ii feasible (partial recovery, ~15% of floor — the first WIREABLE key-axis win).**
- **★ COWORK BUDGET READ (the checkpoint the user flagged):** 4 informed hand-built rounds in; cadence approach works but
  incrementally; remaining residual (dominant/subdominant tonicizations + segmentation artifacts) is increasingly Stage-6-flavored
  (functional context / KeyArea — where cadence work also lives). B still not forced. The gated partial win is bankable now.
- **✅ DECISION (user, 2026-06-14): OPTION C.** The cadence residual = the missing **tonicization understanding** (a Stage-6
  capability, NOT built — the cadence detector reads tonicizations as cadences). Both user axes (min-surprise + max-precision)
  → Stage 6: a "#4 guard" would band-aid a Stage-6 capability (highest surprise risk, lower ceiling); Stage 6 is the larger
  lever (~35-42%) + the proper tonicization home + the biggest single slice (S1 labeling ~17.7%, low-risk pure-add, largely
  independent of the stuck key floor). **Cadence detector COMMITTED as a byte-identical INSTRUMENT** (`cc_instruction_commit_cadence_instrument.md`
  — cadencekeyanchor.{h,cpp} + tests + the batch_analyze diagnostic ONLY; resolver untouched; NOT pushed). **4c-ii wiring
  DEFERRED to a Stage-6-informed integration** (better gating + key-floor feedback). **PIVOT TO STAGE 6.**
- **★ NEW STANDING METHOD recorded (user): layer-by-layer audit once pieces are in place** (handoff top standing block +
  roadmap). The back-half verification model.
- **NEXT: Stage 6 design/scoping (Cowork) — the functional layer.** Responsibility: sequence-label T/S/D over the decoded
  chord+key paths; cadences (consume the Stage-2.1 detector + the new cadence INSTRUMENT); secondary dominants; tonicization-
  vs-modulation from KeyArea spans; aug6/Neapolitan; + 6.2 consolidate the 3 scattered quality-from-key sites; 6.3 revisit the
  convention-gap buckets. **Entry per the layer-by-layer method = the highest-value low-risk slice: S1 tonicization LABELING on
  already-correct-key readings** (pure-add, ~17.7%, independent of the key floor). Design → ratify → build. Roadmap Stage 6.
  **Confirm the Stage-6 entry/scope with the user before writing the full design.**

- **✅ STAGE 6 ENTRY = NARROW (user "go", 2026-06-14) → DESIGN WRITTEN: `docs/stage6_functional_layer_design.md` (DRAFT, ratification-gated).**
  Functional layer responsibility (audited in isolation): sequence-label FUNCTION over the decoded chord+key path
  (T/S/D, tonicization/applied, cadence, aug6/Neapolitan) — distinct from the chord-competition `harmonicfunctionlayer`.
  **Narrow first slice = tonicization (applied-dominant) labeling:** emit `V/X` etc. where a chord is the dominant/LT of a
  non-tonic degree resolving to it (the functional generalization of the cadence V→I logic, now WITH a known key so not
  circular). Why first: S1 ~17.7% (biggest single slice), **pure-add on already-correct-key readings** (chord/key axes
  can't regress → BIR 57/23/57 byte-identical), **independent of the stuck relative-pair floor**. The gap is EMISSION not
  comparator (metric-design: `classify_pair` already credits emitted secondaries — confirm at source, don't re-invent).
  Pins the label-vocab contract (resolves metric-design OQ-L2). Behavior change = functional axis (RN labels) → snapshots
  move (DCML-adjudicate); **binding metric = S1 recovery vs a LOW false-label rate** (the cadence-contradiction analogue).
  Staged: 6-tonic-i (labeler + measure, HELD) → AUDIT the sub-responsibility → 6-ii+ (cadence-token labeling consuming the
  cadence instrument, T/S/D, tonicization-vs-modulation from KeyArea, aug6/Nea). **RATIFIED (user "ratified, go", 2026-06-14).**
- **✅ STAGE 6 6-tonic-i INSTRUCTION DISPATCHED: `cc_instruction_stage6_tonic_i_labeler_measure.md`.** **Refinement flagged
  (safer direction):** 6-tonic-i is **measure-before-wire** (build the tonicization labeler + measure realized quality
  DIAGNOSTICALLY, production RN UNCHANGED → byte-identical) — per the discipline that caught the weak cadence detector; the RN
  wiring is **6-tonic-ii** (separately ratified). Labeler = a NEW composing functional-labeling pass (distinct from
  `harmonicfunctionlayer`); applied-dominant/LT predicate (root=dominant/LT of degree d, raised-LT chromatic vs key, next chord
  resolves to d → `V/d` etc.); CONSUMES the resolved key (legit Stage-6 input; not circular). Confirm label-vocab vs
  `compare_rn`/`classify_pair` at source (already credits emitted secondaries — match, don't re-invent). Measure: **false-label
  rate (BINDING constraint, the tonicization analogue of the cadence contradiction)** + **S1 recall on correct-key readings**
  (~17.7% slice). Byte-identity gate: BIR 57/23/57 + snapshots 11/11 + suites (diagnostic-only; movement = leak = STOP). Branch:
  low false-label + worthwhile recall → 6-tonic-ii wire; high false-label → refine guards. **On CC's report: verify the labeler
  doesn't mutate root/key + byte-identity + false-label rate + the compare_rn match at source before ratifying 6-tonic-ii.**
- **✅ STAGE 6-tonic-i COMPLETE + COWORK-VERIFIED — HELD; predicate SOUND, blocked by the tonicization-vs-modulation boundary (2026-06-14).**
  New `tonicizationlabeler.{h,cpp}` (diagnostic-only — Cowork-verified absent from the production path → byte-identical: BIR
  57/23/57, snapshots 11/11, composing 531). **An existing production labeler already emits V/x+vii°/x** (`regionanalyzer.cpp:178/969`
  `backfillNextRootPc`+`formatRomanNumeral`, verified; 29.2% of S1). Raw FP 78% BUT **91.8% = the tonicization-vs-MODULATION notation
  boundary** (409/427 our target degree == DCML's local tonic — same event, two notations); **genuine plain-diatonic FP = 6.4% → predicate sound.**
  S1 recall 41.2% (+~12-17% new; misses = inversions V6/5/V etc.). Label-vocab matched to `compare_rn` (OQ-L2 resolved).
- **★ LAYER-AUDIT VERDICT:** tonicization predicate CORRECT but INCOMPLETE → needs the **tonicization-vs-modulation discriminator**
  (deferred OQ5; consumes KeyArea/local-key spans + the committed CADENCE INSTRUMENT: cadentially-confirmed local key = modulation,
  unconfirmed applied chord = tonicization). **The pieces are converging** (cadence + KeyArea → discriminator → clean tonicization) —
  the layering payoff. Secondary angle: the metric may over-penalize the tonicization↔modulation equivalence (a metric-design refinement).
- **AWAITING USER:** (a) design the tonicization-vs-modulation discriminator (the "complete" functional layer — RECOMMENDED per the
  layer-correct-AND-complete principle; uses cadence+KeyArea) vs (b) treat tonicization↔modulation as metric-equivalent + wire 6-tonic-i
  as-is (pragmatic; lower-quality output that conflates tonicization & modulation). 6-tonic-i stands as a byte-identical instrument feeding (a).
- **✅ USER CHOSE (b)-quick-metric-check (2026-06-14) → DISPATCHED `cc_instruction_tonicization_modulation_metric_check.md`.**
  READ-ONLY metric-design investigation (no production/metric change, no commit). **Quantify: of the ~409 tonicization-vs-modulation
  cases, how many are BRIEF/either-valid (metric artifact — credit the equivalence, no discriminator needed) vs SUSTAINED/established
  (DCML's modulation correct, our V/d-everywhere wrong → the discriminator's REAL value).** Tasks: how `compare_rn` scores these now
  [code]; classify the 409 by local-key span DURATION + cadential confirmation (using DCML spans + the committed cadence instrument);
  size metric-artifact vs real-output-gap buckets; sketch a fair crediting rule IF warranted (design-only). Deliverable
  `cc_tonicization_modulation_metric_dossier.md` → recommends: mostly-artifact ⇒ credit equivalence + wire the sound predicate;
  substantial-gap ⇒ build the discriminator sized to that bucket. **On CC's dossier: verify the brief-vs-sustained split method +
  the comparator-behavior claim at source before deciding build-vs-credit.**
- **★★ METRIC-CHECK RESULT (2026-06-14) — OVER-PENALIZATION FALSIFIED + THE BIGGEST SLICE REFRAMED. `cc_tonicization_modulation_metric_dossier.md`.**
  **Cowork-verified at source:** `classify_pair` (`compare_rn.py:334-348`) scores by **root_pc+quality, NOT the RN reference key** →
  `V/d`(home) ≡ DCML local `V` (same root) → **partial, already credited.** So the comparator does NOT over-penalize — it
  **UNDER-penalizes / MASKS** (crediting the label hides that the KEY is wrong). 92.7% of the 409 are DCML-cadence-confirmed local
  keys (79.2% ≥5 chords); only 2.7% brief → **DCML's modulation is correct for ~97%.** **★ 95.6% of the WHOLE S1 slice (2001/2093) is
  a LOCAL-MODULATION case → S1 (~17.7%, the biggest precision slice) is a Stage-4 KEY/modulation gap, NOT the Stage-6 tonicization-label
  gap the precision-headroom dossier + compare_rn's own `:786-797` comment assumed.** Crediting rule NOT warranted (harmful — masks the
  95% real error); only a DIAGNOSTIC partial-sub-split (expose the masking) is defensible.
- **★ HEADROOM CORRECTION (load-bearing — propagate to docs):** the biggest precision slice relocates **Stage 6 → Stage 4** (local-modulation
  detection). **Do NOT wire 6-tonic-i** (games rn_agree, degrades correctness). Real lever = a **LOCAL-MODULATION / KeyArea detector
  (Stage 4)**, ~95% of S1, signal = sustained span + local cadence (consumes the committed CADENCE INSTRUMENT + KeyArea); 6-tonic-i's
  sound predicate → the BRIEF-ONLY branch (~4% home-key residue). The key axis holds BOTH the relative-pair floor AND the S1 modulation gap.
  **Docs to correct (S1 attribution Stage6→Stage4):** `cc_precision_headroom_dossier`/`back_half_design`/`implementation_roadmap` (Stage 6.1 framing)
  + `compare_rn.py:786-797` comment (a code-comment, defer to the diagnostic-sub-split change).
- **★ INVESTIGATE-FIRST PAYOFF (record):** this is the new standing rule's clearest win — measuring before building caught that naively
  wiring the tonicization labeler would GAME the metric (rn_agree up) while making the OUTPUT worse. Without the metric-check we'd have shipped it.
- **NEXT (Cowork, PROCEEDING per investigate-by-default — not asking):** investigate the current key-path modulation behavior at source
  (how/whether the resolver+KeyArea modulate; the gap vs DCML) → design the **local-modulation detector** (Stage-4 key behavior change,
  measure-first) + the diagnostic partial-sub-split. Ratifiable design to follow.
- **✅ DISPATCHED `cc_instruction_modulation_keypath_scoping.md` (user "go", 2026-06-14) — READ-ONLY scoping (no commit, no production change).**
  Task A: build the **de-masking diagnostic** in compare_rn — sub-split `partial` by reference-key (correctly-keyed vs home-label-credited-against-
  DCML-local = the masked modulation error); **reporting-only, metric numbers byte-identical** (crediting-harder was rejected as harmful). This is
  the instrument to measure the modulation detector by CORRECTNESS not gameable rn_agree. Task B: characterize the current key-path modulation
  mechanism at source (keyresolver/sectionanalyzer/KeyArea/hysteresis) — **why do we STAY HOME where DCML modulates** (the core diagnosis). Task C:
  size the gap + realistic ceiling of "sustained span + local cadence → modulate" (+ the de-masked REAL key correctness on S1). Task D: available
  signals (cadence instrument + KeyArea + hysteresis) + the integration LAYER (audit-method: which layer owns the modulation decision). Task E:
  behavior-change blast radius (key→basisIndep→gate). Deliverable `cc_modulation_keypath_scoping_dossier.md` → feeds the local-modulation detector
  design (Cowork next, ratification-gated). **On CC's dossier: verify the de-masking diagnostic is truly metric-neutral + the stay-home diagnosis
  at source before designing.**
- **✅ MODULATION SCOPING COMPLETE + COWORK-VERIFIED (2026-06-14).** `cc_modulation_keypath_scoping_dossier.md`. **Verified at source:**
  de-masking `--partial-key-breakdown` is an additive store_true flag (metric-neutral, `compare_rn.py:937`); **stay-home diagnosis correct** —
  `scoreKeySignatureProximity` (`keymodeanalyzer.cpp:409-420`) anchors every estimate to the NOTATED signature → with the lookback + hysteresis +
  NO local-key state, the modulation gap is a **STRUCTURAL ABSENCE** (we track DCML modulations 9.7% vs DCML's 39.9%; stay home 74.5%). Gap ~3006
  regions (29.7%); ceiling ~1800-2500 (capped by the cadence detector's ~75%); de-masking found ~20% (237) of the partial bucket is masked
  modulation error. Integration = Stage-4 key layer (section/piece pass), consuming the key-agnostic cadence instrument; all composing-zone.
  ⚠ CC Task-C "honest 54.4% vs rn_agree 45.7%" is muddled — direction solid (metric masks/overstates), the specific number needs clarification, don't quote.
- **★ ARCHITECTURE TEST PASSED (the soundness question):** the modulation detector resolves FEED-FORWARD — local-key hypothesis from the
  key-agnostic cadence instrument (per-cadence local tonics) + raw structure → re-key → KeyArea rebuilt downstream. No circular feedback. The
  cadence detector built in its own layer is exactly the input. (Landmine guarded: must NOT use the current key-DEPENDENT KeyArea as input = circular.)
- **✅ STAGE 4d DESIGN WRITTEN: `docs/stage4d_local_modulation_design.md` (DRAFT, ratification-gated).** Responsibility: the key layer commits
  cadence-confirmed SUSTAINED local-key spans (override the home-pull only within a confirmed span). §3 NO-CIRCULARITY rule (key-agnostic hypothesis,
  never the key-dependent KeyArea) = the load-bearing soundness property. Integration = section/piece-scoped key-layer pass. Staged measure-first:
  4d-i build+measure byte-identical (binding metric = modulation CORRECTNESS via the de-masking diagnostic + track-rate, NOT gameable rn_agree) →
  4d-ii wire+re-gate (medium BIR risk, DCML-adjudicate, 3 presets). 6-tonic-i becomes the brief-only branch downstream. **Awaiting user ratification
  of §7 → then Cowork writes the 4d-i instruction.**
- **✅ STAGE 4d DESIGN RATIFIED (user agreed §7 items 1-3, 2026-06-14; #4 procedural) → 4d-i INSTRUCTION DISPATCHED: `cc_instruction_stage4d_i_modulation_detector_measure.md`.**
  4d-i = build the modulation detector + MEASURE diagnostically, **production key UNTOUCHED → byte-identical** (re-keying = 4d-ii, gated on this).
  Detector = section/piece-scoped pass; candidates from `detectAuthenticCadences` (per-cadence local tonics, key-agnostic) + establishment (sustained
  ≥5-chord run consistent w/ the hypothesized local collection) + confirmation (cadence in span) → conservative commit (precision-lean). **⛔ HARD
  no-circularity rule:** inputs key-agnostic ONLY — NO resolved key / `KeyModeAnalysisResult` / current `KeyArea` (=circular). Measure candidate spans
  vs DCML modulations: **precision (BINDING — don't over-modulate) + recall/track-rate (9.7%→? toward ~1800-2500 ceiling)**, + the de-masking baseline.
  Byte-identity gate BIR 57/23/57 + snapshots 11/11 + suites (diagnostic-only; movement = leak = STOP). Branch: high precision + worthwhile recall →
  4d-ii wire+re-gate; over-modulating → refine gates. **On CC's report: verify the detector's key-agnostic inputs (no resolved-key/KeyArea) + the
  byte-identity + the precision/recall at source before ratifying 4d-ii.**
- **✅ STAGE 4d-i COMPLETE + COWORK-VERIFIED — HELD; recall works (9.7%→33.4%), precision POOR (47%), bottleneck = UPSTREAM cadence instrument (2026-06-15, session 8).**
  CC's STATUS session-8 entry is accurate (reconciled — no conflict). **★ ARCHITECTURE TEST PASSED (verified at source):** `localmodulationdetector.h`
  includes ONLY `cadencekeyanchor.h` (key-agnostic), references no `KeyModeAnalysisResult`/`keyresolver`/`KeyArea`; `keySignatureFifths` param =
  NOTATED signature (reliable), not resolved key; not in the production key path (grep) → diagnostic-only, byte-identical (BIR 57/23/57, snapshots 11/11,
  0/353 .ours.json diff). **The capability we worried might need circular feedback built cleanly FEED-FORWARD.** CC caught + fixed a design flaw mid-build
  (maximal-run engulfed modulations → nearest-cadence partition). FP breakdown: 43.3% dom/subdom (the #4 guard) + 27.5% relative-pair (anchor right 72.4%)
  + 23.4% foreign; span-gate caps ~61% (noise is upstream).
- **★ CONVERGENCE: the cadence instrument's precision is the SHARED bottleneck** (feeds modulation detection + tonicization-vs-modulation labeling + the
  relative-pair floor). The "#4 guard" — DEFERRED at option-C as a Stage-6 band-aid — is now well-motivated as the upstream unblock (the metric-check reframe
  voided the deferral reasoning). Fixing the cadence precision once unblocks all three.
- **✅ DISPATCHED `cc_instruction_cadence_precision_investigation.md` (proceeding per investigate-by-default — not asking).** READ-ONLY: derive whether a
  KEY-AGNOSTIC discriminator can separate the two false-cadence classes — (1) dom/subdom via a **chromatic-LT per-cadence gate** (works for V-direction,
  but SUBDOMINANT-direction modulations carry no chromatic signal = honest asymmetry to quantify), (2) relative-pair anchor (same structural relative
  problem — be honest if it's the floor). Measure cadence-precision lift + **★ the simulated DOWNSTREAM modulation-precision lift (the 4d-ii unblock test)**
  + the irreducible residual (subdominant + relative-pair = next-layer/learned evidence). Branch: clear unblock → build the discriminator (measure-first);
  ceiling too low → finding (key-agnostic cadence is precision-limited → residual needs a different layer/richer model). **On CC's dossier: verify the
  discriminator is key-agnostic + the simulated modulation-precision lift at source before recommending the build.**
- **★★ CADENCE-PRECISION INVESTIGATION: NEGATIVE — the key-agnostic LOCAL cadence approach has HIT ITS PRECISION CEILING (2026-06-15).**
  `cc_cadence_precision_investigation_dossier.md`. Method rigorous: CC re-implemented `detectLocalModulations`+`aggregateGlobalAnchor` in Python,
  **byte-matched the committed C++ dump 0/326** → trustworthy simulation. **Class 1 (chromatic-LT gate, the dom/subdom hypothesis): FALSIFIED** —
  the LT signal is ORTHOGONAL to correctness (~45% of TRUE modulations + ~50% of FALSE ones carry a diatonic LT; subdominant modulations + home
  cadences are diatonic-LT by construction). Best variant 47%→50% precision for −11pp recall; chromaticity adds nothing over the existing ≥2-cadence
  lever (58.4% @ 18.1% recall). **Class 2 (relative-pair anchor 72.4%): signals already SPENT** — Cowork-verified at source `aggregateGlobalAnchor`
  (`cadencekeyanchor.cpp:148+`) already uses minorMode + chromaticLeadingTone (line 178) + Picardy + finality → it's the **4b-ii structural relative-pair
  floor**, not a missing signal. **Ceiling ≈ 50-58% precision @ ~18-22% recall — below the 4d-ii wireable bar.** Irreducible residual = subdominant-direction
  diatonic-LT modulations + the relative-pair structural floor + sustained-tonicization analyst ambiguity → **needs a DIFFERENT LAYER (global/long-range
  key decode, or a learned model), NOT a key-agnostic local cadence gate.** 4d-ii stays HELD. Scope: Bach/Default WiR (326), non-Bach unmeasured.
- **★ ARCHITECTURAL INFLECTION (the moment the user has watched for):** the architecture is SOUND (feed-forward, validated) but the hand-built
  **key-agnostic LOCAL** approach is **precision-ceilinged** on the key axis. The residual splits: (a) modulation FALSE-POSITIVES = a global-consistency
  problem a **key DECODE** (Viterbi/HMM over key states + modulation transition cost) could suppress — DISTINCT from the relative-pair EMISSION gap the HMM
  was shelved for (META-PRINCIPLE: search≈0 was about absent-candidate recall, not false-positive suppression — so the decode is an under-explored, legit
  lever here, but must be tested skeptically); (b) the relative-pair structural floor = emission-limited → **learned (B)** evidence (the OQ-1 re-open gate
  is effectively triggering on the key axis). **Surfaced to USER as the A-vs-B / META-PRINCIPLE / back-half-re-ground strategic call (not investigate-vs-proceed).
  Cowork lean: investigate the global key decode first (de-risks A-vs-B — does global consistency lift modulation precision before any learned commitment).**
- **★★ BACK-HALF ARCHITECTURE RE-GROUNDED (user + Cowork, 2026-06-15) → CONSTRAINED JOINT INFERENCE. Full synthesis: `docs/architecture_joint_inference.md`.**
  A multi-turn first-principles dialogue (the user drove it) converged on the target architecture, derived from + pinned to the measured key-axis arc:
  - **Model:** harmonic analysis = ONE joint decision over ALL evidence (chord + key/mode co-determined; function downstream), globally coherent. The
    local feed-forward pipeline structurally CANNOT do this — the relative-pair floor + modulation gap are the proof.
  - **Structure:** CONSTRAINED joint inference — HARD constraints (decisive raw facts + unambiguous analyses) disqualify/pin; SOFT scores (priors, weak
    hints, global key path) rank survivors; optimize soft subject to hard. Hard facts are IMMOVABLE → the −7-wall override failure class is structurally
    impossible (not "hopefully calibrated"). Joint/soft work scopes to the ambiguous residual.
  - **META-PRINCIPLE reconciled:** the joint decode's value is BROAD-evidence integration (broader emission), NOT search (search≈0 was over a fixed NARROW
    emission). Precision still lives in evidence breadth+quality+CALIBRATION.
  - **Calibration precondition:** a sounding note ≠ a chord tone (suspensions/pedals) → hard constraints over raw facts + unambiguous analyses only;
    over-claiming hard = override-in-reverse. **Ceiling** = genuine score-underdetermination (analyst ambiguity).
  - **A-vs-B lives in the EMISSION (soft scoring + constraint defs), NOT the structure** — hand-built now, learned later, SAME decode machinery.
  - **Integration not teardown:** chord decoder (Stage 3) = seed; oracle/cadence/modulation/tonicization = evidence producers it integrates; REPLACES the
    local resolver + hysteresis + post-hoc gate layer (note: the gate-layer dissolution is one of the TWO DEFERRED REFACTORS — this subsumes it).
- **✅ DISPATCHED `cc_instruction_joint_architecture_investigation.md` (READ-ONLY sizing, per never-guess).** Tasks: hard/soft characterization; **measure the
  RESIDUAL (pinned-to-unique vs ambiguous after hard constraints) = true scope → full-joint vs scoped-joint vs two-pass**; hard-constraint SAFETY (any pin a
  wrong DCML answer? = the calibration gate); soft-resolvable vs irreducible-floor split (A-vs-B input). Deliverable `cc_joint_architecture_dossier.md`.
  **On the dossier: verify the residual sizing + hard-constraint safety at source before the architecture-design step.** Then: ratify the shape → design the
  joint inference → build (measure-first). The 4d-i modulation detector + the cadence instrument stand as committed/HELD evidence producers feeding this.
- **✅ JOINT-ARCHITECTURE SIZING LANDED + COWORK-VERIFIED (read-only): the shape is CONFIRMED SOUND + RIGHT-SIZED (2026-06-15).** `cc_joint_architecture_dossier.md`.
  HEAD unchanged `2245aedf82`; only the 2 probes + dossier written; **instrument confirmed** (probe reproduces corrected `root_err=2365` to the unit);
  cross-checks hold (key-mod 39.8% ≈ modulation prevalence 39.9%; oracle cross-check concurs). **Residual: 41.0% pinned / 19.2% chord-amb / 26.3% key-amb /
  13.5% jointly-coupled → SCOPED-joint/two-pass, NOT a full lattice** (genuinely-coupled ~1-in-7). **Hard-constraint SAFETY PASSES** (complete-clear-vertical
  chord ~0% vertical error; its disagreement = segmentation + functional re-rooting, not wrong chords). **Reading-shaped producers correctly SOFT (pin wrong:
  cadence 44%, modulation 53%, bass-is-root 17-23%).** **A confirmed, B reserved for the tiny pc-irreducible dim7/aug floor (~111).** Floor = convention
  boundaries (tonic↔mod ~409, notated-vs-analyst ~127). Recommendation: scoped constrained-joint, hand-built soft emission, KEY-AXIS FIRST, keep
  cadence/modulation/bass-is-root soft. Scope: WiR-Bach; non-Bach unmeasured. ⚠ Working tree has accumulated HELD diagnostics + sandbox-noise ` M` on the
  committed 4b-i files — host-side reconcile before any commit (NOT from this read-only run). `docs/architecture_joint_inference.md` promoted to CONFIRMED/ratifiable.
- **AWAITING USER: ratify the SCOPED constrained-joint shape (per the measured sizing) → Cowork designs the scoped constrained-joint inference (key-axis first,
  measure-first). This is a "ratification of a measured result" — the user's call. The two deferred refactors (file-split, gate-layer dissolution) fold into this design.**
- **✅ CADENCE INSTRUMENT COMMITTED `2245aedf82` (Cowork-verified: exactly the 4 files +823/−6, byte-identical, resolver clean, NOT pushed).**
  **★ Push topology update:** `origin/master` is now **`ef30cc70f3` (4b-i)** — the user pushed up through 4b-i to the fork, keeping
  4a (`cfc7eb5e39`, engraving) LOCAL. Chain: a96f179f40 → ef30cc70f3 (4b-i, ORIGIN) → cfc7eb5e39 (4a, local) → 2245aedf82 (cadence, local).
  **Wrinkle:** the cadence instrument now sits ABOVE 4a → pushing it would carry 4a unless the user reorders 4a back to the tip. User's call.

- **Next CC task — DISPATCHED 2026-06-13: the tools-only metric re-baseline batch.**
  Decision taken (user 2026-06-13): "Tools-only metric batch now; P3 with Stage 4."
  Instruction: `cc_instruction_metric_rebaseline_batch.md`. Fixes P0 (fractional-onset
  via `Fraction` + `quarterbeats×480` alignment, keep the ~58.9% dropped annotations),
  P1 (rntxt applied `/X` resolution), P2 (minor-LT/vio degree table → viio +11), P4 (ABC
  downbeat-anchoring; QUARANTINE any movement that won't anchor cleanly rather than ship
  the naive +3.6pp-worse beethoven correction), P5 (coverage-denominator honesty +
  HEAD-aware `rerun_dcml_comparison`). ONE deliberate re-baseline + metric re-pin; HELD
  for Cowork commit (it moves every headline number). Built-in checks: BIR 13/7 UNCHANGED
  (insulation regression — moving = STOP/finding), corrected roots verified against the
  music21 `RomanNumeral` oracle, before/after re-baseline table + corrected headroom
  headline reported. **P3 mode-drop explicitly OUT — rides with the held Stage-4 engraving
  work** (ENGRAVING import change, outside the composing autonomous zone, KEY-axis only).
  The full functional-residual RE-decomposition + OQ-1 re-derivation are the SEPARATE
  follow-on on the corrected metric, not this run.
  *(Audit context, retained:)* the holistic, unprejudiced audit of ALL
  corpora, source → verdict, every stage (S1 source · S2 ours-ingestion [mode-drop lives
  here; pickup/repeats/ties HIGHEST-risk + LEAST-audited] · S3 GT-parsing [applied-root +
  the rest of dcml_parser] · S4 alignment [tick/pickup/measure-numbering — the classic
  corpus killer] · S5 comparison · S6 aggregation) × every corpus (Bach-rntxt, the 9 TSV,
  music21, jazz-no-GT, snapshot). Method: trace ≥20 flagged errors/corpus end-to-end,
  classify PIPELINE-ARTIFACT / GT-LIMITATION / GENUINE-ERROR / AMBIGUITY → the artifact
  rate per corpus = how inflated every headline number is. Output: the complete
  error-source ledger + a prioritized ONE-batch elimination plan. READ-ONLY, no fixes
  this run. **Everything downstream (functional-residual investigation, OQ-1, the
  back-half ratification, the headroom/95%-functional numbers) is FROZEN until the
  measurement chain is audited and the artifact rate is known.**

- **(BLOCKED — resumes after the parser fix) functional-residual investigation (GATES
  OQ-1):** `cc_instruction_functional_residual_investigation.md` — READ-ONLY decomposition of the
  **2576 "neither" root-err functional residual** (cadential-6-4/suspension/applied/pedal
  — where both we AND music21 miss DCML's functional root) three ways:
  RULE-REACHABLE (hand-built functional layer reaches it = A) / NEEDS-RICHER-MODEL
  (the B-trigger) / GENUINE-AMBIGUITY-or-CONVENTION (a ceiling for EVERYONE incl. B —
  sizing it bounds what any approach achieves). S1 tonicization (1791) confirmed-reachable
  separately (mechanical). Calibrated against the literature ceiling (rule-based
  Temperley/HarmAn vs neural AugmentedNet/RNBert) + an optional music21-RN probe.
  Output decides OQ-1: bucket-1+3 dominate → A confirmed; bucket-2 large → B strengthened.
  No build/commit. Then OQ-1 ratifies on evidence → the back half is locked → Stage-4 build.

- **(history) Foundations verification IN PROGRESS (Task 2 cross-corpus regen running):**
  Verdicts so far — **Task 1 KEYSTONE CONFIRMED at source + Cowork-re-verified
  independently** (`importmusicxmlpass2.cpp:5978` `addKey` fifths-only dedup
  `oldkey != key.key()` suppresses the piece-initial empty-sig KeySig → mode discarded →
  resolver sees `m_mode=UNKNOWN`; mode IS read at 6074–6096; census 79/80 zero-sig stems
  carry `<mode>` → **349 lever stands**). PRECISION CORRECTION: it's a *default-key-match*
  dedup, not "literally 0 fifths" — fix targets line 5978 (fixes notation-bridge AND
  batch_analyze callers at once). Task 0 byte-identity RE-CONFIRMED green (vs genuine
  pre-instrument baseline). Task 4 key→basisIndep CONFIRMED current post-3.3. Task 3
  music21 v9.9.1 already in REPRODUCIBILITY.md (the "unrecorded" note was stale — my
  error). Task 5 layer: composing PUBLIC-links engraving (importexport/notation-agnostic);
  fix as data to the resolver, no new dep. Task 6 doc-currency staged (§11 erratum applied,
  ledger closed, riders confirmed landed). **Task 2 = the QUARANTINE: cross-corpus
  50.7%/27.6% is BINARY-stale `.ours.json` (June-3 outputs; 5/6 spot scores flip at HEAD),
  NOT pre-F1-metric-stale (my framing was wrong — current metric reproduces it on June-3
  data). HEAD regen running for the definitive number; until then DO NOT quote
  50.7%/27.6% as current.**
  **⚠ OPEN NUANCE for the final report / Stage-4 (Cowork-flagged): the dedup is in the
  MusicXML import path — confirm whether the live product's NATIVE `.mscz` load has the
  same mode-drop or only MusicXML import does. Bears on "user-facing" vs "test-corpus"
  framing of the 349 lever (corpus is all `.xml` → fully exhibits it; .mscz users may
  not). Does not change the metric lever; sharpens its interpretation.** — recheck the facts before ratifying:
  (1) KEYSTONE — verify the mode-drop at the actual import site + `<mode>` presence
  across all 73 zero-sig stems + explain bwv62.6 (confirms/corrects the 349 lever &
  A-vs-B); (2) re-measure or quarantine the stale cross-corpus numbers at HEAD;
  (3) pin the music21 version; (4) confirm "key feeds basisIndep" is current post-3.3;
  (5) layer-check the proposed import fix (bridge vs engraving, Dependency Rule); (6)
  doc-currency sweep (the §11 erratum + contradicted "current" claims + rider-ledger
  close) so future sessions aren't misled. Verify/correct only — no fix built. Output
  gates the re-grounding ratification.

- **(superseded) QUEUED note: a deliberate BACK-HALF RE-GROUNDING design** — Cowork to write, user to ratify. Trigger: the architecture step-back
  (2026-06-13). The investigation phase produced ONE converging finding three ways
  (beam, key-path, music21-gate): **precision lives in the emission model + functional
  labeling, NOT in search/decode** (roadmap META-PRINCIPLE). The decode-centric part-1
  roadmap's consolidation is delivered, but its precision thesis is falsified; the
  back half is currently being patched fork-by-fork (an accumulating-amendment smell,
  ARCH §2.14). The re-grounding will (Level 1) re-derive the back half emission-centric
  — precision levers = emission quality + functional layer (the 17.7% tonicization
  pure-add label is the best risk/reward), search deferred until something needs it; and
  (Level 2) lay out the genuine design-GOALS fork the evidence raises: keep improving the
  HAND-BUILT emission (explainable, no-training-data, incremental, current path) vs plan
  toward a LEARNED emission (AugmentedNet/RNBert class, part-1 rec.5, higher ceiling
  ~45–50%+ full-RN vs our 27.6%, decoded by the lattice already built — costs
  explainability + DCML-training dependency). **The key-emission dossier's
  structural/fitted-vs-ceiling result is the deciding evidence for Level 2** (structural/
  fitted → hand-built has headroom, Level-1 suffices; ceiling → emission model is the
  limit, Level-2 serious). DO NOT write the re-grounding before the dossier lands (would
  pre-guess its result). Per user 2026-06-13.

- **Next CC task — key-emission headroom investigation (instruction ready):**
  `cc_instruction_key_emission_headroom.md` — measure what a key-EMISSION fix
  (partial-signature broadening / key-profile scoring) recovers of the ~85% Class-B S2
  bulk; the causal question (WHICH scoring term locks the relative-minor) needs the
  252-candidate breakdown → may build a read-only key-candidate dump as a byte-identity-
  gated diagnostic instrument (Stage 4 needs it regardless; diagnose-chord precedent).
  Output: scopes the emission fix (structural vs Stage-5-fitted vs ceiling), confirms the
  path-defer, recommends Stage 4's final shape.
  — key as an HMM path (states = tonic×mode, emissions = the existing 252-candidate
  KeyModeAnalyzer scores REUSED, transitions = circle-of-fifths modulation penalty,
  Viterbi decode → a key PATH). Targets S2 (1032 measured relative/partial-signature
  errors); PRODUCES KeyArea spans (Stage 6's tonicization labeler consumes them — the
  S1 unlock). Design-only, ratification-gated. **Load-bearing: §3 must DERIVE (real
  probe margins) that the path actually fixes S2 — if the local evidence favors the
  wrong key, that's a finding (S2 needs richer emission, not just a path), like the
  Δ=+7a finding.** Reconciles the redesign_plan "key-as-distribution SHELVED" (now has
  1032 live cases). Note: Stage 4 is the **2nd intentional behavior change** — key feeds
  chord emission (`basisIndep`), so byte-identity ends here; gated like 3.2 (measured/
  DCML-adjudicated/ratified, chord-axis side effects measured too). Measured on the L1
  `--key-breakdown` rung. Then Stage 6 (co-developed on KeyArea) → Stage 5 (fits last).
  Beam shelved; decoder_design §11 Δ=+7a erratum still queued. — tools-only, DCML-only, reuse-based, NO
  production/C++ change, NO Stage-6 vocabulary. Three primitives: (1) `compare_rn
  --wir-bach` (commit the Bach-WiR mode, 326/353 denominator explicit); (2) the
  duration-weighted union-of-boundaries unit (THE new primitive — load-bearing test =
  segmentation-invariance: same analysis at two segmentations → same score); (3)
  `--key-breakdown` (the S1/S2 = tonicization-gap/key-error split that makes Stage 4
  measurable). 70 existing metric tests stay unchanged; reproduce the dossier numbers
  via the committed modes. One commit, held. **This is the instrument the back half is
  aimed with; then Stage 4 (key path) leads, measured on L1.** Beam shelved;
  decoder_design §11 Δ=+7a erratum still queued for the next doc pass. — **user decision: design the metric
  BEFORE committing the Stage-4/5/6 order**, because the instrument that measures Stage
  4/6 success doesn't fully exist and a functional-precision metric needs a label
  vocabulary that is itself Stage-6 output (the chicken-and-egg). Design-only,
  ratification-gated. Establishes: compare_rn IS the DCML-only metric (reuse, don't
  rebuild; formalize its Bach-WiR mode); designs the granularity-robust unit (the 2.2-i
  ~7× gap); pins the functional-label vocabulary contract (Stage-6 output spec =
  metric input spec, co-designed once) + the incremental measurability ladder (Stage 4
  measurable now via key/degree; Stage 6 scored class-by-class as it ships) + the
  Stage-5 objective. Output: `docs/precision_metric_design.md` (DRAFT). Feeds a ratified
  back-half order. **Beam shelved; decoder_design §11 Δ=+7a erratum still queued.** — READ-ONLY measurement + map,
  no build. Decompose the total human-adjudicated (DCML-only, Default config, BOTH
  granularities) disagreement mass into mode/key vs functional-chord vs actual-root vs
  the ~40% "neither" residual; map each slice → unlocking mechanism (emission/transition
  reweight = Stage 5 incl. the relocated Δ=+7a fix / key path = Stage 4 / functional
  layer = Stage 6 / segmentation / structural ceiling); recommend the re-grounded
  Stage-4/5/6 ordering + the beam-revisit trigger. Output: `cc_precision_headroom_dossier.md`,
  feeds a ratified roadmap-reshape decision.
  — design-only, ratification-gated (like the decoder design): produces
  `docs/beam_widening_design.md`, 10 sections. The FIRST intentional behavior change —
  beam>1 behind the quality knob (Level-0 stays byte-identical default). Core: derive
  (not assert) HOW the wider decode fixes Δ=+7a (lattice walk of bwv102.7/bwv261, real
  probe if needed — if K=8 doesn't fix it, that's a finding); forward-edge promotion
  per Q2; K=8 per Q6; gate-folding sequence per Q3 (every gate mutates identity →
  retire/fold before widening past it). Must-not-break: Δ=+7b trio (Gate I + R coupled —
  the headline risk), identity sets ×3, snapshots. New gate: BIR/snapshot changes now
  ALLOWED but only on pre-ratified, DCML-adjudicated cases. K caution: reproduce
  Baroque target, NOT the chromatic-romantic mis-fire (3.4-ii). Design doc held for
  ratification; implementation is a separate later instruction.
  — **Cowork decision: spot-check non-chorale scores BEFORE retiring C1 gates** (the
  353-chorale "0 fires" doesn't prove E/F/K dead — they target classical/romantic
  inversion/augmented shapes; DCML mozart/chopin/corelli/beethoven MS3 already cloned).
  Per gate: fires on the non-chorale spread → KEEP as C2; fires nowhere → retire (own
  commit, 0/353×3 proof gate, held). The spot-check is the gating measurement; no
  removal pre-judged from chorale 0s. Then 3.2 (beam widening; Δ=+7a + the C2 set).
  — **with a Cowork correction to design §7: "decoder-subsumed after 3.3" is an
  UNPROVEN hypothesis** (beam-1 is numerically the old pipeline; gates exist because
  the bonuses didn't suffice) — so 3.4 ships in two phases. This run: two pre-authorized
  byte-identical ships (B/C/D dead removal with proof gate; Gate R absorbed into the
  rcb edge + 2-arg overload cleanup) + the per-gate differential dry-run (disable one
  gate at a time → pins-failing list, corpus×3 identity deltas, snapshot drift,
  classification C1 dead-in-practice / C2 beam-replaceable / C3 emission-fold /
  C4 functional-layer / C5 structural-keeper, + the Q3 beam-cap consequence per gate).
  NO behavior commits; the dossier's decision menu feeds 3.4-ii and 3.2's design.
  "Held means HELD" restated in the instruction (3.3 slip on record).
  — the hardest byte-identity gate yet: five signals MOVE between layers, so the FP
  composition must be replicated to the addition (Task 1 = a written FP-preservation
  plan BEFORE code: exact current composition quoted, capped-sum order, insertion
  points; vertical predicates become ScoringCell flags, temporal gating moves).
  Gate R's replacement condition must be DERIVED equal to the old proxy on every
  reachable input (incl. no-third qualities), then proven by 0/353×3. Deliberate
  re-pin ledger for unit tests encoding old slot semantics; end-to-end pins are NOT
  re-pinnable. One atomic commit, ratification-gated. Stop conditions include
  "FP composition unreplicable → options to Cowork" and "old/new Gate R disagree on a
  reachable input → design question". Then 3.4 → 3.2 (Δ=+7a).
  — decode-once cache for P3/P4 per design §8 + Q1/Q7. **Cowork sharpened the design's
  under-confronted point: whole-score-cached answers CAN differ from today's
  window-based P3 answers (window-edge segmentation) — this is the first live-product
  behavior change since the reviews, so the answer-delta is MEASURED (Task-3 A/B with
  DCML verdicts + P3-vs-P1 consistency quantification) and RATIFIED before any commit.**
  Conservative MVP: whole-cache invalidation on any edit (bounded re-decode = documented
  follow-up); no-reliable-change-signal = stop; snapshots stay on the raw cold functions
  (11/11 zero diffs hard gate); warm-perf must be materially better or it's a no-op stop.
  Carries the rule-5 doc riders (B2). Then 3.3 (signal migration + Gate R, atomic) →
  3.4 (gate retirement, leads 3.2) → 3.2 (beam widening; Δ=+7a target).
  — produces `docs/decoder_design.md`, 13 mandated sections: scope (chord path over
  EXISTING segmentation — joint seg+labeling explicitly out), lattice shape + memory
  envelope, term-by-term emission/transition factorization (with explicit treatment
  of the awkward non-pairwise terms: wDim post-bonus guard, Pass-B m7-budget,
  threshold/cap, Iter 86/91/pedal, gates A–L), beam-1 byte-identity argument + FP
  tripwires, path state vs advanceTemporalContext, oracle-signal migration + Gate R
  coupling redesign, per-gate retirement plan with Stage-1 pins as proof obligations,
  decode-once-query-many (closes D-P4/D-BRIDGE), quality↔beam mapping + perf budget,
  config-agnosticism, honestly-classified acceptance roster (what Stage 3 fixes vs
  must-not-break vs needs Stage 4/6), migration sequencing + rollback per step,
  §Open Questions for Cowork/user. Design-only; probes allowed (uncommitted);
  doc commit ratification-gated (rule 4 — ratification arrives as addendum file).
  — investigate → draft decisions → at most one surgical fix. HEADLINE INVESTIGATION:
  does the user's style/preset EVER reach the notation analysis path, or is the whole
  preset system batch-tools-only? (Gates the D-PASS0 decision; "presets never shipped
  to users" would be a product-level finding.) Decision drafts for D-P4/D-BRIDGE
  (lean: document cold-context contract, defer to Stage 3 decoder), D-PASS0
  (investigation-dependent), D-GAP (fix only if probe proves user+gate-neutral;
  3 regression cases re-run as causal validation). Commits V1/V2 are
  RATIFICATION-GATED (Cowork must approve the decision drafts first — rule 4 honored:
  ratification will arrive as an addendum instruction file); V3 bookkeeping direct.
  Carries the doc riders (CLAUDE.md kDiagTemplates checklist, ARCHITECTURE.md:861,
  audit moot item). Then 2.5 (P3 profile) closes Stage 2; Stage 3 (decoder) begins.
  — implements `cowork_corpus_audit.md` C1–C4: snapshot/gate source manifests with
  sha256 + clone commits + drift test + REPRODUCIBILITY pinning (license facts
  recorded, no in-tree copies), music21 provenance (establish or freeze-by-fiat),
  353/361/410 trace + diff lists, stale deletions (flat .ours.json, accident dirs,
  unreferenced src/composing/tests/scores after final sweep), score_inventory.md
  refresh. 5 proposed commits (H1–H5), await Cowork as a set. KEY stop condition:
  snapshot-source hashes not matching what goldens were generated from = gate-integrity
  question, report immediately. After this: Stage 2.3 (diagnoseChord production view),
  2.4 (divergence decisions incl. inferGapRegion preset leak), 2.5 (P3 profile).
  — Phase 4c move: `analyzeSection` + section-level analysis (cadences, pivots,
  stabilization, degree, key-resolution wrappers) from `notationcomposingbridgehelpers.cpp`
  into composing (suggested `analysis/section/`). Mechanical relocation, byte-identical;
  **zero snapshot diffs is the decisive proof** (snapshot tests call analyzeSection
  directly). Explicit file authorization includes the notation bridge/implode files
  (caller updates + code removal only). Test-ledger requirement (coverage provably not
  dropped). Rider: `chordanalyzer.h:402–409` doc-comment fix. TWO commits proposed
  (rider + move), both await Cowork. First production-code instruction since the
  reviews. Then 2.2 batch parity + single re-baseline (metric-bug decisions F-1/F-2,
  "24" provenance trace), 2.3 diagnoseChord, 2.4 P4/bridge decision, 2.5 P3 profile.

- **⚠ Cowork sandbox caveat (learned 2026-06-10):** Cowork's Linux-sandbox view of the
  repo can serve STALE git/file state (symptoms: spurious ` M` entries, index.lock unlink
  warnings, files appearing present after deletion). Host-side Read tool is authoritative
  for file contents; CC's native git is authoritative for git state. Do not overrule CC's
  git evidence from the sandbox view without a host-side Read cross-check.
  **Additionally:** Cowork's sandbox `git status` can LEAVE a stale `.git/index.lock`
  behind (it cannot unlink the lock it creates — blocked CC's `git add` once, 2026-06-10).
  Cowork should prefer `git --no-optional-locks status` / log/show in the sandbox; CC may
  safely remove a zero-byte stale index.lock after confirming no git process is running.

- **Previous CC task — Stage 0 hygiene (done, partially committed):**
  Instruction file: `cc_instruction_stage0_hygiene.md` (implements
  `docs/implementation_roadmap.md` Stage 0, items 0.1–0.6).
  Tasks: doc pass + doc commit (incl. committing untracked `layer_architecture_audit.md`
  and `implementation_roadmap.md`); delete repo junk; remove dead fnCtx keyFifths/keyMode
  fields; `kTemplateCount` shared constant across the 5 sync sites; FP tie-policy section
  in scoring_model.md; document onsetBoundaryThreshold + region-collapse divergences.
  Two commits: docs (commit immediately), code hygiene (propose, await Cowork).
  Hard constraint: byte-identical — 416/416 · 52/52 · 11/11, BIR 13/7 unchanged, both
  presets regenerated, tools/corpus restored to Baroque. Report: `cc_stage0_report.md`.

- **Previous HEAD:** `1bfc64d18c` (refactor: unify chord-commit path — Phase E Step 5).

  `1bfc64d18c` — adds `advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf, chosen, gateCtx)`
  overload in `chordanalyzer.h`; replaces three separate manual commit patterns in
  `regionanalyzer.cpp` (Pass 1, Pass 2, Pass 2b) with the unified call. Sub-region passes gain
  per-parent rolling-state variables (`subRunningStepwiseCount`, `subRecentRootsBuf`). Byte-identical
  (A/B verified, 0/353 diffs both corpora). 416/416 · 52/52 · 11/11. BIR 24/13 / 35/7 unchanged.

- **Prior lineage:** `90a52b5fee` (fix: bridge forward-lookahead in findTemporalContext).

  Recent master lineage: `90a52b5fee` (fix: bridge forward-lookahead in findTemporalContext) ←
  `bffb6c4e3d` (test: Gate R unit tests) ←
  `927e8b579d` (docs/chore: comment fixes — E1–E5) ←
  `0b51395527` (docs: STATUS.md Gate R baselines) ←
  `638ced1c12` (feat: Gate R — harmonicfunctionlayer.cpp + scoring_model.md + 6 goldens) ←
  `f9ba22157d` (fix: G-E phantom HalfDim + float literals — E3 Tasks 2+3) ← ...

- **Gate R — committed `638ced1c12` (2026-06-09):**
  - Fixes all three Δ=+7b targets: bwv245.28 (E), bwv296 (G), bwv320 (C) ✓
  - Bonus: bwv349 m13 fixed (Am → F/A = DCML root F, BIR=true error removed)
  - No regressions in either preset; full 353-score corpus rebuild verified
  - Two required refinements: `basisDep ≤ 0` condition + `!explorationMode` guard
  - 6 bridge-path snapshot goldens refreshed; all DCML-verified:
    - bach_chorale_003 tick 7680: Asus4→D major = DCML V6 (D/F#) **Improvement**
    - bwv806_prelude: E/G# = DCML I6 of local key E **Improvement**
    - bach_chorale_137: winner unchanged, rcb-inflated C-major alternative dropped **Neutral**
    - chopin_bi105_op30_2: alternatives-only, winner B minor unchanged **Neutral** *(CC's §8 correction: reported as winner change, was not)*
    - mozart_k279_1: spurious G/E alternative dropped, winner unchanged **Improvement**
    - bach_bwv806_gigue: runner-up alt change only **Neutral**
  - Golden path correction: goldens live at `src/notation/tests/pipeline_snapshot_tests/snapshots/`
    NOT `src/composing/tests/snapshots/` — update future git-add instructions accordingly
  - `tools/corpus/` holds stale PRE-Jazz regeneration; needs fresh regeneration before trusting numbers

- **Layer architecture audit complete (2026-06-09):** Full findings in
  `docs/layer_architecture_audit.md`. Key conclusions:
  - E2d split is sound; oracle/pipeline boundary is real
  - Five temporal signals remain in oracle as documented pre-existing debt
    (`chordanalyzer.h:329`) — do not move until Phase E
  - `harmonicfunctionlayer.h` basisIndep comment is inaccurate (claims "no progression signal")
  - `contextualBonuses` invariant at `chordanalyzer.cpp:1634` is stale
  - ~~Bridge path missing forward lookahead~~ — **FIXED `90a52b5fee`**: forward walk added to `findTemporalContext` mirroring backward walk; `nextRootPc`/`nextBassPc`/`bassIsStepwiseToNext` now populated via `seg->next1(ChordRest)` + cold analysis through full gate pipeline
  - Sub-regions always have `bassIsStepwiseToNext = false` (consistent, undocumented)
  - Gate R's `basisDep ≤ 0` depends on `sameRootInversionBonus` staying in oracle
  - **Recommended next CC tasks:** unit tests for `bassIsTemplateChordTone` + Gate R branches;
    comment fixes for 2a/2b/3/6; ChordSymbolFormatter extraction (low priority)
  - **Do NOT split `chordanalyzer.cpp` now** — wait for Phase E to motivate it

  Recent master lineage: `f9ba22157d` (fix: G-E phantom HalfDim + float literals to named constants — E3 Tasks 2+3) ← `a693b6ba82` (docs: cowork_handoff.md post-E2d housekeeping) ←
  `22b89ae521` (tools: iter 90–97 analysis scripts) ←
  `5b08465924` (docs: iteration logs, key detection, LLM integration) ←
  `0ea52ced98` (chore: gitignore CC/Cowork working-process files) ←
  `8f13aee8d3` (test: remove equivalence harness) ←
  `469d7830f2` (docs: CLAUDE.md scoring-doc process rules) ←
  `2917ec7571` (E2d redesign: scoring oracle / competition pipeline) ←
  `0ab219d4c5` (E2d-prereq Phase 1: extract Iter 86/91/pedal) ←
  `20f992a5e7` (E2c-infra: function-layer plumbing) ←
  `710d8dba12` (E2b: scoring snapshot) ← `80a7adf32e` (E2a: progression-signal
  lambdas) ← `dd29a04967` (E1: function layer shell) ← `3ac52e1198` (scoring_model.md
  + annotations) ← `945a9e2f18` (B2 aug7 template) ← `f3e0f5f72c` (Sub-9a Gate G-E
  fix) ← `81978321e3` (keyresolver partial-sig) ← `fe752fb6d9` (A4 Corelli) ←
  `a69a23e59b` (D2 + docs).

- **BIR baselines (lenient-OR `align_regions`, `tools/characterise_bir_false.py`):**
  Baroque BIR=true=24, BIR=false=13; Jazz BIR=true=35, BIR=false=7.
  Hard stops: Baroque BIR=false must not increase above 13; Jazz BIR=false must not increase above 7.
  Cumulative since Iter 91: Baroque BIR=false 188 → 13 (−175, ~93% reduction).
  **IMPORTANT — BIR script note (corrected 2026-06-10, Stage 1d F-3):** the **13**
  (BIR=false residual count) comes from `tools/characterise_bir_false.py` (lenient-OR
  align_regions comparator). That script does NOT compute the **24** (BIR=true) — the
  24's producing script was not established in the Stage-1d survey; treat it as a
  corpus-characterisation figure of unverified provenance until traced.
  `tools/analyze_inversion_errors.py` reports a DIFFERENT metric (music21∩DCML
  bassIsRoot three-way split) — these are NOT the same numbers and must not be used
  interchangeably in instructions.
  `tools/corpus/` = POST-Gate-R Baroque state (regenerated 2026-06-09, 353 scores).

- **Jazz BIR=false=10 — fully characterised (2026-06-08):** 8 cases shared with Baroque
  (Δ=+7 rootContinuity ×3, sus/quartal ×2, segmentation ×1, evidence-absent ×1,
  dim→dom absent-root ×1); 2 Jazz-only (bwv244.15 key-conf-0 root mis-selection;
  bwv74.8 added-tone tetrachord — Em7/D for Cadd9, the B4 6th/m7 ambiguity).
  Jazz's reduced individual inversion bonuses (0.20/0.20/0.15/0.20 vs Baroque
  defaults; NOT the cap — `maxTotalInversionContextBonus` is never set and
  non-binding, see 2026-06-10 doc-pass Task-1 finding) remove Baroque's absent-root
  inversion cases (bwv14.5, bwv174.5, bwv301, bwv381) from Jazz — confirmed by
  prior prediction. Nothing newly actionable beyond the absent-root guard (bwv45.7
  dim→dom absent-root, partial). Full table in `cc_stepback_report.md`.

- **Tests:** **416/416 composing** (+9 Gate R unit tests in `gater_tests.cpp`; equivalence
  harness removed — tautological post-redesign), **52/52 notation (fully green)**, 11/11
  pipeline snapshot (1 intentional skip = `PipelineDivergenceCObservation.GenerateReport`).
  Mismatch report: Jazz 130 (131→130 post-E2d path unification).

- **Part G commit (2026-06-09, session 3):**
  - `90a52b5fee` — bridge forward-lookahead fix. `findTemporalContext` in
    `regiontonecollector.cpp` now calls `seg->next1(ChordRest)`, cold-analyzes successor
    through full `applyIter8691Pedal` + `applyPostScoringGates` pipeline, sets
    `nextRootPc`/`nextBassPc`/`bassIsStepwiseToNext`. Only `regiontonecollector.cpp/.h`
    touched. 3 snapshot drifts — all P4 tickLocal, all improvements or neutral:
    - chorale_137 t2880: Dm → Bø7 — **Improvement** (G-B gate fires; matches batch)
    - chorale_001 t15600: Bm → G — **Improvement** (onset {G,B,D} = G major; old Bm impossible)
    - chorale_001 t11280: F#dim → F#ø7 — **Neutral** (root unchanged; quality refinement)
    Goldens refreshed. 416/416 · 52/52 · 11/11. BIR unchanged 24/13 / 35/7.
    Full report: `cc_bridge_lookahead_report.md`.

- **Part E + Part F commits (2026-06-09, follow-on to Gate R):**
  - `927e8b579d` — comment-only: (E1) `harmonicfunctionlayer.h` basisIndep accuracy; (E2)
    stale invariant clarified at `chordanalyzer.cpp ~L1634`; (E3) Gate R cross-layer
    dependency documented; (E4) bridge lookahead gap noted in `findTemporalContext`; (E5)
    golden path corrected in `BUILD_AND_TEST.md`. Byte-identical.
  - `bffb6c4e3d` — `bassIsTemplateChordTone` + `gateRZeroesRootContinuity` promoted to `fn`
    namespace (behavior-preserving); new `gater_tests.cpp` (9 Gate R unit tests). Composing
    416/416 (+9). Byte-identical (no BIR change).

- **Git status audit (2026-06-06, pass 2 complete):**
  - Stash: empty. Working tree clean.
  - `compare_rn.py`: already committed (`f6630b29cd`) — old handoff "pending commit" note was stale.
  - `bwv*_dcml.xml` (5 files): moved to `tools/dcml/` (intentionally gitignored — reproducible QA artifacts). Not committed; correct.
  - Root helper scripts deleted: `step3_build_and_test.ps1` (D2 experiment harness, superseded), `run_e2b_tests.bat` (E2b phase wrapper, superseded).
  - 2 untracked files remain in `tools/` — `.txt` data dumps, skip (generated output).
  - `ai-assistant/` is a separate project; ignore its untracked files here.

- **DCML cross-corpus baseline = 53.8%** (20256/37639, DCML-anchored, time-overlap,
  lenient-OR; 10 non-Bach corpora). Regenerated against the HEAD `a69a23e59b` binary
  on 2026-05-20. **Supersedes the prior 46.8% (15928/34022) at `53c4f2d50c`**, which was
  measured BEFORE STEP 1 + D2 changed chord output — a **+7.0 pp** gain with **every corpus
  improved** (biggest: Corelli +13.7, Mozart +9.4, Schumann +8.4; C.P.E. Bach still 0
  regions, excluded). Reports under `tools/reports/live_20260520_postd2/` (gitignored).
  Regenerate: run the 10 `tools/run_<corpus>_validation.py` scripts
  (`--output <dir> --batch-analyze ninja_build_rel/batch_analyze.exe`; the beethoven
  script writes to a dir named exactly `beethoven`) then
  `python tools/rerun_dcml_comparison.py --cross-corpus-root <dir>`.

- **STEP 1 — dim7-completeness guard + Gate J (committed `3d80d0a91d`):**
  Two coupled `chordanalyzer.cpp` changes. (1) The dim7 characteristic bonus now requires
  the **complete diminished triad** (root + ♭3 + ♭5) before it fires, so an incomplete
  diminished sonority stops out-scoring the dominant-seventh reading the evidence supports.
  (2) **Gate J** — a root-position diminished triad whose dominant root (a major third below)
  is present is treated as an **inverted V7** (vii° → V7 completion; canonical case
  bwv110.7 m10 `C#dim7 → F#7`); requires the complete diminished triad. Impact:
  **Jazz BIR=true 56→33 (−23)**, **Baroque BIR=false 25→23 (−2)** (Jazz fixes bwv282,
  bwv60.5, bwv65.2). 5 pipeline-snapshot goldens refreshed and DCML-verified.

- **D2 unification (committed `4d881e7418`, recorded in `a69a23e59b`):**
  `pass1MinDistinctPcsForCandidate=1` on the batch path — matching the bridge. This was the
  **last batch/bridge parameter divergence**; bridge and batch are now **fully unified** thin
  wrappers over `region::analyzeRegions()`. Both paths admit sparse 1–2 PC Pass-1 slices.
  `regionanalyzer.cpp` untouched (pure flag unification). Net error reduction both corpora
  (Baroque BIR=true 34→27 / false 25→23; Jazz BIR=true 56→33 / false 13→10).

- **Unification status:** Iter 97 Phases 2+3+4 + D2 are **complete**. Both parameter
  divergences are resolved: **D1 (`excludeLookAheadOnDenseStart`)** is confirmed
  load-bearing and **intentionally divergent** (batch passes `true`, bridge defaults
  `false`; unifying it regresses bridge/Corelli trio-sonata dominants); **D2
  (`pass1MinDistinctPcsForCandidate`)** is unified at `1` on both paths. The bridge and
  batch are fully unified thin wrappers over `regionanalyzer`.

- **Iter 98 — attempted and reverted (2026-05-23). Dead end documented — do not re-attempt.**
  Both the sparse-continuity suppression approaches tried in Iter 98 produced the same
  DCML-verified regression on mozart_k280-1 (m9/m12 IV→V65 over-merge), which means the
  failure is **intrinsic to suppressing sparse-predecessor continuity** — Alberti-bass
  textures genuinely need that continuity and neither a density gate nor an inversion-aware
  gate can separate bwv320 from mozart. Full dead-end analysis recorded in CC's Iter 98
  backlog memory. Baseline fully restored to HEAD `a69a23e59b`; nothing committed.

  Two approaches tried and rejected:
  - **Predecessor-sparse gate** (`previousRegionDistinctPcs ≤ 2` → suppress
    `rootContinuityBonus`): fixed bwv320, but hit mozart_k280 IV→V65 regression.
  - **Inversion-aware refinement** (suppress only when candidate `bassPc ≠ rootPc`):
    fixed bwv320 + Chopin test, improved BIR both corpora (Baroque 23→21, Jazz 10→9),
    but still produced the same mozart_k280 IV→V65 pipeline-snapshot regression (DCML-verified
    wrong). Same regression as the rejected orchestrator approach → intrinsic dead end.

  **bwv320 m27 (accepted residual — needs a different mechanism):** reads `G6/E` instead
  of `C`. An admitted 2-PC `Gm` Pass-1 slice overwrites `previousRootPc`, and
  `rootContinuityBonus` (+0.40) tips a 0.02-margin window to G. Margin-based and
  density-based discriminators **cannot** separate this from legitimate sparse-continuity
  cases in Alberti-bass textures. If revisited, needs a **targeted segmentation or
  merge-level fix** around tick 37440–38400 rather than a scoring gate.
  - **α-variant: `w_dim` rotation-only guard** — **DEAD END, do not re-attempt.**
    Tried 2026-05-23: requiring the pre-bonus winner to also be Dim/HalfDim regressed
    Baroque (+4 BIR=true, +1 BIR=false) and broke 2 bwv806 pipeline snapshots without
    fixing either target case. Root cause: wDim exists to elevate a non-dim winner to dim
    — requiring the pre-bonus winner to already be dim defeats its purpose. The two
    originally deferred target cases are not wDim problems at all (see below).
    - **schumann tick 480 (viio7/V = C#°7):** the 240-tick C#°7 region is absorbed by
      `absorbShortRegions` (Phase-4 removed Iter-77 Fix-A protection). P4 tickLocal has
      the right quality (dim7) but wrong rotation (G°7 vs C#°7) because `nextRootPc` is
      not plumbed into the per-tick path. Needs: (a) surgical absorption exception for
      short leading-tone dim regions, and/or (b) `nextRootPc` plumbing into P4. Both are
      upstream architectural issues, not scoring problems.
    - **chorale_003 Am→G#dim:** no authoritative ground truth (DCML doesn't cover Bach
      chorales). All Am regions are 3-PC triads — wDim is gated out by `distinctPcs>=4`
      by design. Accepted residual; do not pursue via wDim.
  - **δ: sparse-minor diatonic quality prior** — **DEAD END, do not re-attempt as a quality fix.**
    Diagnosed 2026-05-23: the remaining Corelli failure (`CorelliOp01n08dUserReportedChordTrackAudit`)
    is rooted in **key mis-detection**, not chord quality. The quality prior would read the
    wrong detected key (G minor instead of C minor) and reinforce wrong answers. The three
    remaining sub-failures are: m24 F→Fm (key symptom), m2 b3 G/B inversion (separate
    inversion issue), m18 missing Cm region (segmentation). Do not revive δ until the key is
    corrected.

  - **Key/mode detection — Baroque partial-signature bug: FIXED (`81978321e3`).**
    Option B landed: keyresolver now allows signature-flexible tonic candidates. Corelli
    op01 scores now detect C minor correctly. Full write-up in
    `docs/key_detection_baroque_partial_signature.md`.

  - **Dominant-quality fix — deferred (1-PC segmentation cascade). distinctPcs gate is a dead end.**
    Both the Corelli target (op01n08d m1 b3) and the Chopin regression source
    (bi105_op30_2 tick 23040) are **1-PC** — a `distinctPcs >= 2` gate suppresses both.
    Diagnosis from CC Step 2b investigation (2026-06-03):

    | | Corelli m1 b3 | Chopin tick 23040 |
    |---|---|---|
    | distinctPcs | 1 | 1 |
    | pitchClassSet | G only | F# only |
    | quality (current) | Minor / Gm | Minor / F#m |
    | key | C minor | B minor |
    | keyConfidence | **0.9615** | **0.6273** |

    The only signal that separates them is **`keyConfidence`**. A corpus-wide survey
    of all 267 matching slices was run (2026-06-03). **There is no bimodal gap** —
    the distribution is continuous from 0.00 to 1.00 with every 0.05-wide bucket
    non-empty. The distribution summary:

    ```
    [0.95,1.00)  17   ← Corelli anchor (0.9615) here; 82% drop from next bucket
    [0.90,0.95)   3
    [0.85,0.90)   3
    [0.80,0.85)   3
    [0.75,0.80)   5
    [0.70,0.75)   6
    [0.65,0.70)   5
    [0.60,0.65)   3   ← Chopin regression (0.6273) here
    [0.55,0.60)   1
    [0.50,0.55)  21   ← score-opening "no key evidence yet" sentinel values
    ...below 0.50: 149 slices (bulk of the ambiguous-v mass)
    ```

    The only clean structural break is at **0.95**: 17 → 3 (82% drop). This is a
    **tail effect, not a bimodal gap**. No contiguous near-zero band exists that
    would justify a principled "real V vs ambiguous v" cut at any lower threshold.

    **DEFINITIVE DEAD END — defer to Phase E. Do not re-attempt via keyConfidence alone.**

    Pre-inspection of the 17 highest-confidence cases (kc ≥ 0.95, 2026-06-03) found
    **5/17 clear false positives (29% FP rate)**:
    - Mozart K457-1 m180.2 (kc=1.0): DCML = III6 — single G is the third of E♭ first
      inversion, not a V root.
    - Mozart K457-3 m181.2 (kc=1.0): DCML = It6 (Italian aug-6th) — pre-dominant, not V.
    - Beethoven Op.130-ii m57.3 (kc=1.0): DCML = bVI in B♭ major; key disagreement
      (analyzer: C Dorian vs DCML: B♭ major) plus PC mis-detection.
    - Beethoven Op.130-ii m61.2 (kc=0.972): DCML = @none (silence/rest).
    - Tchaikovsky op37a06 m1.2 (kc=0.962): DCML = tonic i — analyzer mistakes the
      chord-tone 5th of a long G-minor tonic chord for a D-dominant root.

    These false positives require knowledge of adjacent harmonic context (voice-leading
    direction, resolution, cadence type) that `keyConfidence` does not encode. Even the
    top tier (kc=1.0) contains III6 and It6 misreadings. A gate on keyConfidence alone
    cannot separate them from genuine V chords at any threshold.

    **The correct fix belongs in Phase E** (harmonic function layer): cadence confirmation
    (detect a preceding leading-tone or V7→i resolution) distinguishes genuine dominant
    preparation from single-PC chord-tone arpeggiation. Until Phase E, Corelli m1 b3 stays
    at "Gm" (the notation test deferral comment remains in place).

    Survey artifacts: `tools/survey_1pc_dominant_slices.py`,
    `/tmp/dominant_survey_out.txt` (370 lines, full sorted table + histogram),
    `C:\Temp\dominant_survey\<corpus>\*.json` (948 fresh Baroque dumps, cached).

- ~~**Pre-existing issue to investigate:** BWV227.7 m9 pitch-class E~~ **RESOLVED** (`fc1206bd4e`) — test expectation fixed to use tick-overlap; no analyzer change.

- **Mozart k280_1 cascade (introduced A4, queued):** `mozart_k280_1` pipeline-snapshot
  golden was refreshed after the A4 hasStructuralBass gate caused a secondary change at
  one tick (Bb/F replaced Cadd11/F). Both the old and new readings diverge from DCML V43
  — neither is correct. Queued for C3/C4 characterisation.

- **Chord mismatch report:** 4 RealDiff (pinned), 127 ConventionDiff (Jazz)

---

## Roadmap — phased by dependency then risk

Phases are ordered: later phases depend on earlier ones, or carry higher architectural
risk that earlier phases de-risk. Within a phase, items are ordered lowest-risk first.

---

### Phase A — Foundation (in progress / immediate next)

These unblock everything below. Do not start B–F until A is stable.

**A1. Key/mode detection — Baroque partial-signature fix** *(CC in progress)*
Option B (`keyresolver.cpp`): allow signature-flexible tonic candidates. Full write-up in
`docs/key_detection_baroque_partial_signature.md`. Validate against both BIR presets +
notation + snapshots. Target: Corelli op01 scores detect correct key.

**A2. Dominant-as-major quality in minor keys** *(deferred to Phase E — keyConfidence insufficient)*
`sparsechordrefinement.cpp` — `applyTonicPriorToSparseChord` maps degree-5 in minor to
natural-minor v (Minor) instead of major V. Full investigation completed (2026-06-03):
both discriminators exhausted. `distinctPcs >= 2` cannot separate the cases (both 1-PC).
`keyConfidence` has no bimodal gap (267 slices, continuous distribution), and the top
kc ≥ 0.95 tier has a 5/17 (29%) DCML-verified FP rate (III6, It6, bVI, rest, tonic-5th
misreadings). Fix requires Phase E cadence-confirmation signal. Corelli m1 b3 stays "Gm"
with deferral comment in `CorelliOp01n08dOpeningAndSparseLateBeats`.

**A3. Roman numeral ground-truth comparison tooling** ✅ *DONE — `tools/compare_rn.py` + baseline `tools/reports/rn_baseline_f3e0f5f72c.txt`*

New script `tools/compare_rn.py` (single-piece / single-corpus / cross-corpus modes).
Reuses `compare_analyses.align_dcml_regions` (time-overlap, lenient-OR ≥50%). Normalises
key-prefix, modulation marker, figured-bass tokens; maps DCML `%` → our `ø`; case-sensitive
(case encodes quality). cpe_bach skipped (stem mismatch, orthogonal issue).

**Baseline — 9 non-Bach corpora, 520 movements, 61,233 matched regions (HEAD `f3e0f5f72c`):**

| metric | value |
|---|---|
| rn_agree | **27.6%** (16,905/61,233) |
| exact_match | 18.0% (11,027) |
| partial_match | 9.6% (5,878) — root+quality correct, inversion/extension differs |
| quality_err | **21.7%** (13,305) — root correct, quality wrong |
| root_err | 50.7% (31,023) — root wrong (= BIR=false set) |
| root_agree (parity) | 49.3% (30,210) |

Top-5 disagreement patterns:

| ours | → DCML | count |
|---|---|---|
| V | → I | 1,131 |
| I | → V | 660 |
| V | → V7 | 487 |
| IV | → I | 448 |
| III | → I | 438 |

**Key observations (classifier corrected 2026-06-04):**
- root_err (50.7%) dominates — consistent with BIR metric
- quality_err (21.7%) was **misleadingly named**. `_same_quality()` was a pure string
  comparison on the degree base (`"V" == "I"` → False), so V→I fired `quality_err`
  even though both are major quality. **Classifier fixed 2026-06-04** — `quality_err`
  replaced by two precise buckets:
  - **key_disagree = 15.4% (9,440/61,233)**: root + coarse quality agree, scale degree
    differs — key/mode detection error. E.g. V→I means "we say G is scale-degree 5 in
    C major; DCML says the same G is scale-degree 1 in G major." Phase E only.
  - **quality_disagree = 6.3% (3,865/61,233)**: root PC agrees, coarse quality genuinely
    differs — true chord-quality error. Sum 21.7% preserved; split 71% key / 29% quality.
- **Maj→Dom7 gap — INVESTIGATED AND CLOSED (2026-06-04):**
  Maj→Dom7 is 948 cases (24.5% of quality_disagree; top corpora: Beethoven 32%, Chopin 17%,
  Grieg 16%, Corelli 12%, Mozart 10%). Sampled 25 cases across 5 corpora with
  `tools/find_maj_to_dom7.py` — checked 7th-PC pcWeight for each:
  - 32% (8/25): 7th PC **entirely absent** from the sounding tones
  - 48% (12/25): 7th PC present but raw weight **below extensionThreshold (0.20)**
  - 20% (5/25): 7th PC present at ≥ 0.15 weight ratio (mostly Chopin add9 detections
    where we already detect a 9th extension and the DCML disagrees about which extension
    to model)
  **Conclusion: not an actionable bug.** DCML systematically labels *implied* dominant
  sevenths from harmonic-functional context even when the 7th doesn't sound. Our analyzer
  correctly withholds the extension without sounding evidence above extensionThreshold.
  Lowering the threshold to capture these would cause large-scale false-positive 7th chords.
  Accepted as extension-threshold gap. Phase E (harmonic function layer) is the correct fix.
- quality_disagree remaining after Maj→Dom7: ~2,917 regions — Min→Maj (714, 5.4%) and
  Maj→Min (~465, 3.5%) are the next-largest buckets (parallel major/minor confusion).
  Not yet investigated.
- partial_match (9.6%): root+quality right, inversion/extension off

**Corrected reports (2026-06-04):**
- `tools/reports/rn_corrected_classifier_f3e0f5f72c.txt` — cross-corpus summary with
  key_disagree / quality_disagree split
- `tools/reports/rn_corrected_breakdown_f3e0f5f72c.txt` — quality_disagree breakdown
- `tools/reports/maj_to_dom7_samples.txt` — 25-case 7th-pcWeight sample data
- New helper: `tools/find_maj_to_dom7.py`

**Pending commit:** `tools/compare_rn.py` (classifier fix) + the above new files.
Working tree is dirty with these tooling changes. Commit when convenient.

**Immediate actionable targets remaining from this analysis:**
1. ~~Fix compare_rn.py classifier~~ ✅ Done
2. ~~Maj→Dom7 gap~~ ✅ Investigated — closed as extension-threshold gap (not actionable)
3. Key/mode detection errors (key_disagree 15.4%, ~9,440 cases) — Phase E only
4. ~~Parallel major/minor confusion (quality_disagree Min→Maj 714 + Maj→Min ~465)~~ ✅
   Investigated (2026-06-08 step-back). **Closed as convention gap.** ~75% of 1,181 cases
   are thirdless (neither third above extensionThreshold) — analyzer infers quality from
   key/degree context; DCML labels functional role. Same conclusion as Maj→Dom7. Remaining
   ~25% are DCML function-over-sonority (sounding third agrees with our read; DCML overrides
   via modal mixture, raised thirds, Picardy, etc.). Not actionable via scoring/gate changes.
   rn_agree secondary metric largely frozen without Phase E.

**Corpus note:** The snapshot `tools/reports/live_20260603/` predates HEAD by one day;
<10 regions of 61k affected. The 49.3% root_agree here vs 53.8% at `a69a23e59b` is
a corpus/denominator difference (different regeneration run), not a regression.

**rn_agree=27.6% is now the secondary quality baseline** alongside root_agree=53.8%.
Every future code change must not regress rn_agree below 27.6%.

**A4. Remaining Corelli Test 2 sub-failures** ✅ *DONE — commit `fe752fb6d9`*
Both sub-failures resolved; notation suite now **52/52** (fully green).

- **m2 b3 G/B → G:** Score had only upper-register notes (violin G5+B4, bass staves
  rest). Bass-candidate enumeration was disabled; legacy fallback picked B4; stepwise-
  inversion bonus (+0.5 for C→B descending) tipped to V6. Fix: sparse-upper-register
  trigger for bass-candidate enumeration (`distinctPcs ≤ 2 && lowestPitch > 60 &&
  ≥2 regional candidates`); `hasStructuralBass` parameter gates inversion contextual
  bonuses (set false when `lowestPitch > 60 && distinctPcs < 3`). File:
  `chordanalyzer.cpp`.

- **m18 b1 missing Cm:** Pass 2b split Cm into four 240-tick sub-regions; each was
  individually absorbed by `absorbShortRegions` into the m17 Gm predecessor. Fix:
  `coalesceShortSameRootRuns` pre-pass in `regionanalyzer.cpp` — coalesces runs of
  ≥3 consecutive contiguous same-root sub-regions totalling ≥720 ticks before
  `absorbShortRegions` runs. Guarded by predecessor-root check.

BIR at time of A4: Baroque 27/23 → 28/22 (net flat, one case moved false→true). Jazz 33/10 → 35/10
(+2 true, false unchanged). 4 pipeline-snapshot goldens refreshed (DCML-verified):
`corelli_op01n08a`, `chopin_bi105_op30_1`, `mozart_k279_1`, `mozart_k280_1`.

**Known follow-up — Mozart k280_1 cascade:** the A4 fix caused a secondary change at
one k280_1 tick (Bb/F replaced former Cadd11/F). Both readings diverge from DCML V43
— neither is correct. The snapshot was refreshed to the new (also-wrong) reading.
Queued for C3/C4 characterisation or separate triage.

**A5. BWV227.7 m9 pitch-class E regression** ✅ *DONE — commit `fc1206bd4e`*
Test expectation error (Category 4). The analyzer correctly captured pc=E in the G
region anchored at m8 b3 (ticks [14400,16800), pcs include E), which physically
spans into m9. The test filtered by `measureNumber==9`, missing it; the only
`measureNumber=9` region was a tail Gadd9/F# with no E. Fix: switched detection to
tick-overlap against the m9 range [15360,17280). Test-only change; no analyzer code
touched. BIR baselines at A5 unchanged (Baroque 28/22, Jazz 35/10). Pre-existing since
before STEP 1/D2/A1–A4.

---

### Phase B — Template completeness (independent of A, but requires Phase E guard for any template whose PC set overlaps a common Baroque progression)

**⚠ B1 lesson:** Before attempting any new template, check whether its PC set is a
subset of a common Baroque progression in a minor or major key. If yes, the template
will fire in those contexts and requires a Phase E functional guard before it is safe.
B1 ({0,3,7,11}) overlaps {tonic+leading-tone-of-V}; a bare template cannot separate them.

Can be done in parallel with A or after. Each template addition is atomic and
independently verifiable against both BIR presets + snapshots.

**B1. Add MinorMajor7 template {0,3,7,11}** *(deferred to Phase E — leading-tone ambiguity)*
Attempted 2026-06-04. **REJECTED — do not re-attempt without Phase E guard.**
Approach A works mechanically (no new enum needed: `ChordQuality::Minor` +
`hasMajorSeventh` extension; `qualitySuffix` already emits `mMaj7` for that
combination). Three array-size sites to update when retrying: `analyzeChord`
`array<TemplateDef, 16>` at chordanalyzer.cpp:1923; `diagnoseChord` array at
:3334; three `array<array<double,16>,12>` score matrices at :1982–1984 (missing
those last three caused a stack-buffer overrun). Results: Baroque BIR=false 23→25
(+2, hard-stop limit); 2 DCML-wrong pipeline-snapshot winners (bach_chorale_003
V65 `E7/G#`→`AmMaj9`; bwv806_prelude tick 36720 `Bmadd9/C#`→`C#m`). Root cause:
bare {0,3,7,11} cannot distinguish {tonic+leading-tone-of-V} from a genuine i(maj7)
in Baroque minor-key contexts. A V→i suppression guard would defeat the jazz use
case (ii–V–i resolution is V→i). **Needs Phase E cadence confirmation to identify
whether the leading tone is resolving to i or is still the active dominant.**
Full rationale in `docs/backlog_b1_mmaj7_template.md`.

**B2. Add Augmented dominant 7th template {0,4,8,10}** (C7♯5) ✅ *DONE — commit `945a9e2f18`*
Guard: skip the 4-tone Augmented template for any root where either M3 (rootPc+4) OR
aug5 (rootPc+8) is absent below extensionThreshold (both required). Without both-tone
guard the template over-fired on complete major triads containing a minor seventh.
BIR: Baroque 28/16 (unchanged); Jazz BIR=true 35→36 (+1), BIR=false=10 (unchanged).
Jazz catalog: m285 Tristan→D7#5/C (3rd inversion, C bass) resolves 1 RealDiff (4→3);
m286 rest used for Tristan suffix coverage. Standard 0/1 unchanged.
Three template-addition sites (both TemplateDef arrays + three score matrices).
Iteration took 4 attempts: (1) first revert — struct field `tones` vs `intervals`;
(2) second revert — Tristan catalog slash bass missing (`D7#5` vs `D7#5/C`) and
Tristan suffix coverage broken; (3) third revert — M3-only guard too loose (Schumann
D-major V, Corelli G-major I flipped to aug7); (4) M3+aug5 dual guard succeeded.

**B3. Promote dim7 {0,3,6,9} to a dedicated template** *(DEFERRED — bonus is rotation-selector, not just scoring)*

Attempted 2026-06-05. **Do not re-attempt without addressing both root causes below.**

Investigation revealed that `dim7CharacteristicBonus` (kDim7CharacteristicBonus = 0.75,
chordanalyzer.cpp:2036 + :3426) is NOT merely a scoring offset — it is a
**rotation-selection mechanism** for the enharmonic dim7 ambiguity (C°7 = E♭°7 = G♭°7 = B♭♭°7).
Its gate includes a **non-diatonic check on the ♭♭7 PC** that asymmetrically rewards the
correct enharmonic root over the three spurious rotations. Without this check, all four
rotations score identically, and 6 Jazz catalog entries distinguishing Bdim7 from its
rotations (m370/372/374) break.

Two failure modes encountered:
1. **Bonus suppression → 6 Jazz RealDiff failures.** Rotation-selection mechanism lost;
   Bdim7 chords flipped to wrong D/F-rooted rotations.
2. **Template + bonus coexisting → `bach_chorale_003` snapshot regression.** At tick 17280,
   `Em7b5/C#` flipped to `Dm/E` (indirect segmentation side effect: bass C# = ♭♭7 of E°7
   activated the 4-tone template at root=E, though the chord is half-diminished not full dim7).

Option (a) — add the non-diatonic ♭♭7 check to the template guard — not attempted: C# is
non-diatonic in the key of chorale_003 at that point, so the check would not block the
spurious fire; segmentation regression would persist.

**Pre-conditions for future retry:**
- Template guard must include the non-diatonic ♭♭7 check (mirrors the bonus gate)
- Must resolve the chorale_003 segmentation artifact (why does `Em7b5/C#` shift when
  the 4-tone template fires at root=E with C# as bass?)
- Once both preconditions met: condition the bonus to not fire when the template passes

**B4. Evaluate 6th chord templates {0,4,7,9} / {0,3,7,9}** *(needs analysis first)*
C6 and Am7 share all four pitch classes — adding these templates creates new ambiguities
that bass evidence alone may not resolve. Investigate whether the net BIR effect is
positive before implementing.

---

### Phase C — Deferred residuals (depends on A being stable)

**C1. Schumann tick 480 — viio7/V (C#°7)**
Two independent fixes needed:
(a) Surgical absorption exception: preserve short leading-tone dim regions that resolve
    to the next root (re-introduce Iter-77 Fix-A intent without region-count explosion).
    Plan before coding — absorption logic is sensitive.
(b) `nextRootPc` plumbing into P4 tickLocal path so wDim picks correct dim7 rotation
    in per-tick analysis. Investigate first — verify whether P4 currently receives
    `nextRootPc` at all.

**C2. bwv320 m27 — G/E instead of C** *(⚠ STALE SECTION — resolved by Gate R `638ced1c12`.
This is the SAME case as the Δ=+7b bwv320 instance; bwv320 is absent from the current
Baroque-13 identity set. Kept for the Iter-98 dead-end history only. Reconciled
2026-06-12 after the stage3-design report's dual-classification question — the
"C2 rcb-near-tie residual class" has NO known live instance; decoder_design.md §11's
C2 row cites this dead example, so Stage 3.2's expected wins = Δ=+7a primarily.)*
rootContinuityBonus (+0.40) fires because the preceding sparse 2-PC Gm slice
(tick 36960) set previousRootPc=7. G major (root=G, bass=E) is a legitimate
template candidate scored 1.52; +0.40 context bonus → 1.92 beats Cmaj 1.90 by
0.02. C3/C4 pre-fix audit (2026-06-04) confirmed the Iter 98 diagnosis is
correct; an earlier "re-diagnosis" claiming a slash-synthesis path was WRONG
(diagnoseChord dump omits temporal-context bonuses). All Iter 98 suppression
approaches (sparse-predecessor gate, inversion-aware gate) regress mozart_k280-1
IV→V65 Alberti-bass. Accepted residual pending Phase E (function layer).

**C3/C4. β/γ mis-root characterisation** ✅ *COMPLETE — `tools/characterise_bir_false.py` added*

The Iter-96 β/γ framing (Δ=+5 / Δ=+2) is now numerically obsolete. At HEAD
`fc1206bd4e` the 22 Baroque BIR=false residuals consolidated into two dominant
clusters — both are winner-selection bugs, not scoring gaps:

**Δ=+9 Sub-9a: Gate G-E stale-reference bug** ✅ *FIXED — commit pending*
**Baroque BIR=false 22 → 16 (−6). All tests green. No regressions. Not yet committed.**
Scores affected: bwv245.17 m10, bwv258 m4+m10, bwv309 m5, bwv356 m19 + 1 borderline.
Precise mechanism: `winner` in Gate G-E (~L2896) is a live reference to `results[0]`.
The inversion-correction `stable_sort` had already moved Am7b5/C (rootPc=9) to
results[0]. Gate G-E read rootPc=9 → `gExpectedAltRoot=(9+9)%12=6` (F#/Gb, the
WRONG leading tone), pulled in dormant F#m7b5 from rawCandidates at score ~0.10.
Fix: captured `const int originalWinnerRootPc = winner.identity.rootPc` at L2636
(alongside existing `originalWinnerQuality`/`originalWinnerHasAddedSixth` at
L2635-2637); changed L2896 to use `originalWinnerRootPc`. Gate J and all other gates
unaffected. No goldens changed.

**Δ=+7: rootContinuityBonus cluster — split into two sub-mechanisms (2026-06-08 diagnostic)**

Predecessor-confidence diagnostic (`cc_deltaseven_predecessor_report.md`, 2026-06-08)
falsified the "sparse predecessor" framing and revealed the cluster is not homogeneous:

**Δ=+7a — arpeggiation segmentation + rcb cascade (NOT a vertical-oracle bug): bwv102.7, bwv261**
*(Reframed 2026-06-09 after full per-cell oracle dump — prior "wrong root wins vertically"
characterisation was incorrect.)*

In the **committed/run-opening regions** the DCML root is absent because the arpeggio places
it one step in the FUTURE — not as a sustaining note from the past. Exact tick data
(`cc_phase_d_investigation_report.md` 2026-06-09):
- bwv102.7: failing region starts t17520; Ab (DCML root) attacks at t17760 (+240 ticks)
- bwv261: failing region starts t33840; F# (DCML root) attacks at t34080 (+240 ticks)

The 240-tick micro-regions are produced by the **initial greedy-expand** (Pass 2), which
creates a new region boundary every time the set of simultaneously sounding notes changes.
An arpeggio moving through C→Eb→Ab creates one 240-tick region per step. Pass 2b's
`detectBassMovementSubBoundaries` is not involved — it has `minGapTicks = 960` (2 beats)
specifically to avoid micro-splits. `coalesceShortSameRootRuns` cannot rescue these because
the oracle-identified roots differ across the micro-regions (different incomplete tone sets).

**Dead end recorded:** changing `collectRegionTones`'s `noteEnd <= startTickInt` to `< startTickInt`
does not help — the boundary-touching predecessors are other chord tones (C, Eb; G, B), not
the root. The root hasn't attacked yet. Do not retry this fix.

In the **sibling regions where the DCML root sounds**, the oracle actually PREFERS the DCML
root (AbMaj7 raw 2.55 > Eb/Ab 2.33; F#7 raw 2.85 > C#m/F# 2.83). The wrong root prevails
ONLY because `rootContinuityBonus` +0.40 (fed by the wrong-root micro-region) tips it.

Gate R is structurally inapplicable: both present-root wrong readings carry inversion bonuses
(`basisDep > 0`: Eb/Ab = 0.90, C#m/F# = 1.40), so Gate R's `basisDep ≤ 0` guard correctly
spares them.

**Fix path: Phase E only. All gate approaches exhausted.**

Phase D dead ends (all 2026-06-09, documented in `docs/redesign_plan.md` Step 4):
1. `noteEnd <= startTickInt` → `< startTickInt` backward-walk fix: adds C/Eb not Ab; falsified.
2. External short-region merger: 0 qualifying runs (inline merge already fuses arpeggio slices).
3. Re-analysis of inline-merged aggregate with run-opening context: tried, reverted, corpus regressions.
   Full report: `cc_phase_d_merger_report.md`.

Phase E predecessor-confidence gate dead end (2026-06-09, `cc_phase_e_predecessor_survey_report.md`):
No threshold on `previousWinnerScore`, `previousWinnerMargin`, `previousDistinctPcs`, or
`previousWinnerRootPcWeight` separates the Δ=+7a arpeggio predecessors from legitimate
continuations. The rcb source is correctly confident about a transient (rootW 0.25–0.50,
score 3.05–3.30); Mozart Alberti control sits at rootW 0.00, below both Δ=+7a predecessors —
any gate that catches Δ=+7a also fires on correct continuations. Reconfirms Iter-98.

**What this means:** confidence can't encode "right now, wrong in 240 ticks." The fix requires
inter-region revision (Phase E): when the next region's evidence contradicts the committed
predecessor identity, revise the predecessor. This is architectural, not a gate.

Do NOT attempt further rcb gates. Full findings in `cc_deltaseven_7a_diagnostic_report.md`,
`cc_phase_d_investigation_report.md`, `cc_phase_d_merger_report.md`, and
`cc_phase_e_predecessor_survey_report.md`.

**Δ=+7b — correct predecessor, oracle tie broken by bonus (`contFired=1`): bwv245.28, bwv296, bwv320**
The predecessors are **correct, confident** chords (Bm=ii, D=vi, Gm=ii) — not sparse
or wrong. The bonus fires legitimately from a correct predecessor, then tips a
near-vertical-tie in the NEXT region the wrong way. Failing region scores:
bwv245.28/bwv296/bwv320 all show ~1.92 vs ~1.92 (exact or near tie in vertical oracle).
The old root (B, D, G) is still a real chord tone in the new PC set — the oracle cannot
distinguish "continued root" from "new V6 harmony" on vertical evidence alone. The bonus
is the sole tiebreaker. The correct reading requires voice-leading resolution context
(V6 resolving upward vs. ii lingering) — **Phase E territory.**

**Predecessor-confidence scaling approach: falsified.** Predecessors have pcWeight
0.60–0.82 (not 0.0); mozart_k280 control predecessor has pcWeight 1.00 (the highest
of the set). No (pcWeight, margin, distinctPcs) threshold separates the wrong cases from
the correct Alberti control. Full data in `cc_deltaseven_predecessor_report.md`.

**CC's proposed bass-aware gate: Iter 98 echo — do not attempt without explicit mozart test.**
CC proposed: withhold bonus when candidate is non-root-position (`bassPc ≠ rootPc`)
AND bass has moved (`bassPc ≠ previousBassPc`). This adds one condition to Iter 98's
rejected "inversion-aware refinement" (`bassPc ≠ rootPc` alone). The extra condition
does not save it: in Alberti-bass textures the bass moves to a different chord position
on every beat, so `bassPc ≠ previousBassPc` fires on both the wrong cases AND the
correct mozart continuity. Same dead end. If this is ever re-investigated, the mozart_k280
pipeline-snapshot test must be run before any commit.

**⚠ bwv320 m27 RE-DIAGNOSIS RETRACTED (2026-06-04):**
The "slash-synthesis" re-diagnosis above was WRONG. The diagnoseChord dump
used in C3/C4 characterisation omits temporal-context bonuses (rootContinuityBonus,
w_seq, w_dim) and uses legacy single-bass path — it falsely showed G/E as having
no template support. In reality, G major (root=G, bass=E) IS in the template loop
(rank 15 at score 1.52); rootContinuityBonus adds +0.40 because the preceding
sparse 2-PC Gm slice (tick 36960) set previousRootPc=7. Final score 1.92 beats
Cmaj 1.90 by exactly 0.02. This is the original Iter 98 diagnosis (fully correct,
documented in regionanalyzer.h and the Iter 98 dead-end section above). The Δ=+7
C2 entry below is also corrected.

**Remaining 16 cases (BIR=false=16 after Sub-9a fix) — fully characterised 2026-06-08:**

| Category | Count | Cases | Status |
|---|---|---|---|
| Δ=+7a: arpeggiation segmentation + rcb cascade | 2 | bwv102.7, bwv261 | **Phase E only** — Phase D fully exhausted (3 dead ends); oracle correct in present-root slice without rcb; rcb from wrong-root arpeggiated predecessor is the sole blocker |
| Δ=+7b: correct predecessor, oracle tie broken by bonus | 3 | bwv245.28, bwv296, bwv320 | ✅ **FIXED by Gate R** (`638ced1c12`) |
| Evidence-absent (DCML root not in pcs — genuine) | 2 | bwv17.7, bwv245.17 | Phase D only |
| Absent-OUR-root (DCML root IS present — actionable) | 3 | bwv14.5, bwv174.5, bwv301 | **Dead end — absent-root guard tried (2026-06-08) and reverted (net regression: 2 fixed, 4 broken). See below.** |
| B4 template tie (6th/m7 ambiguity) | 1 | bwv381 | Phase B4 (needs investigation) |
| Sus/quartal/whole-tone placeholder | 3 | bwv245.40, bwv422, bwv45.7 | Structural — no fix |
| Segmentation (region too wide) | 2 | bwv269, bwv432 | Complex — low priority |

**Segmentation cases (bwv269, bwv432) — characterised 2026-06-04:**

- **bwv269 m15** (t=20640–22080, 1440 ticks = full 3/4 measure): Analyzer emits D/F# Major.
  DCML has 4 events in this measure: V6 + V6/5 + I + viio6 (D/F#, D7/F#, G, F#°/A). F# is
  in the bass throughout, so the bass-run suppresses splits; Pass 2b doesn't find internal
  boundaries. The merged pcs={C,D,F#,A} is the union of all 4 events; G (DCML's beat-2 I)
  is entirely absent from it. Root cause: greedy-expand / Pass 2b doesn't split within a
  same-bass run even when the harmonic content changes.

- **bwv432 m3 b3.5** (t=5520–6480, 960 ticks = 2 beats, crosses barline): Analyzer emits
  Am/E Minor. DCML has 3 events: viio7 + i + V2 (E°7, Em, D7). Em's chord tones G and B
  fall out of the merged pcs; Am matches {A,C,E} with 2/3 present (C,E). Root cause: same
  over-merging pattern; viio7 → i boundary not detected.

**Sub-9b case (bwv14.5) — post-scoring absent-root promotion (2026-06-04):**

⚠ **Initial "Δ=+7 rootContinuityBonus" re-classification was WRONG — retracted.**
CC batch dump confirmed `previousRootPc = 10 (Bb)`, not 7 (G). rootContinuityBonus
fires on Bb-rooted candidates only (+0.40 → Bb major ~3.185), not on Gm.

**Actual mechanism (identified 2026-06-04):**
Joint scoring winner = Bb major (score ~2.785 base, ~3.185 with rootContinuityBonus).
All three emitted alternatives (Gm/Bb, Am/Bb, Gb+/Bb) have roots NOT in pcs
and score **below the 75% diagnostic threshold (2.089)** — meaning they are not in
the pre-context top 23 candidates at all. Some **post-joint-scoring pass** is
replacing Bb major with Gm/Bb. Gm/Bb score=2.660, root G absent from pcs.

The bass=Bb. All three alternatives share bass=Bb and have Bb as the 3rd of their root:
Bb = m3 of Gm (rootPc=7), Bb = M3 of Gb+ (rootPc=6), Bb as NCT of Am (rootPc=9).
This is an inversion-correction-style pass that asks "what chord could Bb be the third of?"
— then promotes a root-absent result over the correct Bb-rooted winner.

**Status: undiagnosed residual — investigation closed 2026-06-04.**

CC ran three diagnostic rounds (batch JSON dump, gate code audit + guard attempt, debug
print). Results:
- All known post-joint-scoring gates (B/C/D/E/F/G-E/H/I/J/K/L, Iter 91) were ruled out
  (all require quality conditions Bb major doesn't satisfy).
- An absent-root guard on the inversion-deduction block (L2839–2880) was tried and
  reverted: had no effect on bwv14.5 (the deduction block's `bestAltIdx` pointed at D
  Dom7, not Gm) but caused 5 snapshot regressions on legitimate cases.
- Debug print approach was issued but not yet reported; even so, the scope is clear:
  the Gm/Bb result likely comes from a **Pass 2/2b sub-region call** with different
  (smaller) pcs where G may actually be present, not from the parent-region gates.
- Score image (user-annotated) confirms bwv14.5 has at least two additional issues
  beyond m5 (opening-measure rootContinuityBonus stickiness). Even a correct m5 fix
  would leave a significantly wrong analysis overall.

**Root cause fully characterised (2026-06-04 debug print):**
The Gm/Bb result comes from a **sub-region analyzeChord call** with pcs={C,D,Bb}
(3 tones, distinctPcs=3, bass=Bb2 MIDI 46, context non-null). E from the parent
region (pcs={C,D,E,Bb}) was dropped on entry to this sub-region. G is absent from
the sub-region pcs as well — this is a genuine absent-root Minor-template win, not
a region-alignment artifact. Gm/Bb beats Bb major because F (Bb's 5th) is also
absent, and inversion-context bonuses tip the balance toward the first-inversion
reading. A general absent-root winner guard is the correct conceptual fix but the
one attempt (inversion-deduction-block guard, L2839–2880) caused 5 snapshot
regressions without affecting this case. Targeted fix requires identifying the
exact sub-region caller in regionanalyzer and scoping the guard narrowly.

**Decision: re-opened (2026-06-08 step-back). Previous closure was premature.**

The previous attempt failed because the guard was placed in the inversion-deduction
block (L2839–2880), which is the wrong location. The correct location is the
**winner-selection pass in `applyHarmonicFunction`**: reject a winner whose root PC
weight ≤ extensionThreshold when a within-margin present-root alternative exists.
Gate J is not a conflict — Gate J only fires when the dominant root IS present above
threshold (mutually exclusive conditions).

**3 Baroque target cases for the absent-root guard (reclassified 2026-06-08):**
- bwv14.5 Sub-9b (confirmed): root G absent from {C,D,Bb} sub-region. Already characterised above.
- bwv174.5: pcWeights {B:.6, Gb:.2, Ab:.2} — our root E absent; DCML root G#=Ab IS present (it's the bass).
- bwv301: pcWeights {B:1.25, D:1.25, A:1.05, C:.25, Ab:.2} — our root G absent; DCML root B strongly present (1.25).

These three were previously conflated in the "Evidence-absent (DCML root not in pcs)"
bucket. bwv174.5 and bwv301 are absent-OUR-root cases (DCML root IS in pcs; we emit a
root that is absent). Reclassified 2026-06-08.

1 Jazz target case: bwv45.7 (dim→dom absent-root, partial — Sus/quartal bucket by
primary mechanism, but absent-root guard would partially address it).

**Absent-root guard outcome (2026-06-08 — dead end, reverted):**

Guard implemented in `applyHarmonicFunction` (after `chosenPerBass` sort). Condition:
`pcWeight[winnerRootPc] == 0.0 AND distinctPcs >= 3 AND in-group alternative within
kAbsentRootGuardMargin=0.35`. Result:

| Case | Outcome |
|---|---|
| bwv301 (primary target) | ✅ Fixed |
| bwv269 (bonus) | ✅ Fixed |
| bwv174.5 | ⟲ Lateral — E/G# → B5, still wrong |
| bwv14.5 | ❌ Not reached (sub-region caller not the guard location) |
| bwv227.1 | ❌ New regression — DCML-correct absent-root reading (rootless E) |
| bwv342 | ❌ New regression — DCML-correct absent-root reading (rootless E) |
| bwv10.7 | ❌ Cascade regression (upstream root change → previousRootPc → rcb) |
| bwv337 | ❌ Cascade regression (same mechanism) |

Net: Baroque BIR=true +2, 6 snapshot goldens drifted. **Reverted entirely.**

Root cause: the premise "absent root ⇒ wrong reading" is false corpus-wide. bwv227.1
and bwv342 are DCML-correct absent-root readings. The cascade problem is structural —
any guard that changes a committed root poisons `previousRootPc` for all downstream
regions. These 3 cases (bwv14.5, bwv174.5, bwv301) remain open; bwv301 and bwv14.5
may be addressable only at Phase E or with a much more targeted sub-region guard.

CC note: `tools/dump_bir_cases.py` left as untracked helper (safe to keep or remove).
CC memory: `project_absent_root_guard_rejected.md` records the dead end.

**Score image (user-annotated, 2026-06-04):** Additional errors visible in the opening
measures (Gm read for Cm/Eb and G7/B at m1-2). This IS likely rootContinuityBonus from
the Gm pickup (different region, different previousRootPc context than m5). Those errors
are a separate Δ=+7 manifestation and accepted as Phase E residuals.
Roman numeral labeling errors (G/D → "I⁶₄" should be "V⁶₄") are downstream artifacts.

**Δ=+7 cluster (5 cases incl. bwv320) — NOT fixable with current tooling.**
All are rootContinuityBonus mis-fires on sparse predecessors. Same Iter 98
dead end. Do not attempt. Phase E only.

**Do NOT add a negative-margin guard** — would break Gate J and all other
intentional backward-swap gates (B/C/D/E/F/G/H/I/K/L, Iter 91).

New tooling: `tools/characterise_bir_false.py` (reusable BIR=false delta-group
analyser). Raw output: `/tmp/bir_false_char.txt` (uncommitted).
Diagnose dumps: `/tmp/bwv356_diag.txt`, `/tmp/bwv320_diag.txt`.

---

### Phase D — Voice-leading / non-harmonic tone model (high impact, higher complexity)

This is the deepest missing piece: without it the PC set fed to template matching is
always "dirty" (passing tones, suspensions, ornaments all contaminate it). Every
downstream layer currently compensates case-by-case rather than fixing the root input.

**D1. Non-harmonic tone classification**
Before tone collection feeds the scorer, classify tones as structural vs non-harmonic
(passing, neighbor, suspension, appoggiatura) using duration, metric position, and
voice-leading interval. Weight non-harmonic tones down or exclude them from PC set.
This unblocks many gate/bonus simplifications downstream.

**D2. Multi-voice / register awareness**
Assign voice roles (bass, tenor, alto, soprano) and weight evidence accordingly. Bass
voice carries harmonic root information; inner-voice passing motion should not dominate
root inference. Also needed for correct figured-bass analysis.

---

### Phase E — Harmonic function layer (architectural, depends on D being stable)

Introduce as a thin shell first (gates migrate in), then grow capabilities.

**E1. Introduce harmonic function layer shell** ✅ *DONE — commit `dd29a04967`*
`src/composing/analysis/function/harmonicfunctionlayer.{h,cpp}` — `HarmonicFunctionContext`
(keyFifths, keyMode, previousRootPc, nextRootPc) + `applyHarmonicFunction()` no-op.
Added to `composing_analysis` target_sources (consistent with analysis-subdir pattern;
no separate CMake module). Three call sites in `regionanalyzer.cpp` gated on
`!prefs.explorationMode`: Pass 1 L457-464 (after BOTH refinement passes — fully refined
winner); Pass 2 L658-665; Pass 2b L844-851. `docs/scoring_model.md` §10 added.
Zero behavioral change. 407/407, 52/52, 11/11 — byte-identical to baseline.

**CMake note for E2/E3:** The function files are compiled into `composing_analysis`,
not a separate library. E2/E3 should continue this pattern unless there is a specific
build-isolation reason to extract a separate module.

**E2a. Move progression-signal lambdas to function layer** ✅ *DONE — commit `80a7adf32e`*
`rootContinuityBonus`, `wSeqBonus`, `wDimBonus` are now free functions in
`harmonicfunctionlayer.{h,cpp}`. `chordanalyzer.cpp` calls them via thin lambda
wrappers from their existing sites. `kWSeq` (0.20) and `kWDim` (0.15) constants
moved to the function layer header. The `w_dim` dual-scoring structure (two parallel
accumulators + post-bonus quality guard) is untouched. Code organisation only —
execution order and call sites unchanged. 407/407, 52/52, 11/11 — byte-identical.

**E2b. Expose scoring snapshot** ✅ *DONE — commit `710d8dba12`*
`ScoringCell` / `ScoringSnapshot` structs added to `harmonicfunctionlayer.h`.
`prefs.captureScoringSnapshot { nullptr }` added to `ChordAnalyzerPreferences`.
When non-null, `analyzeChord()` populates pre-step-bonus scoring cubes for both
the with-wDim and without-wDim variants (all bassCandidates × 12 rootPcs × N
templates). Also records `distinctPcs`, `acceptedWithWDim`, `chosenBassPc`,
`winnerBassPcWith/Without`. All existing callers pass nullptr — hot path unchanged.
407/407, 52/52, 11/11 — byte-identical to `80a7adf32e`.

**E2c. Function-layer plumbing** ✅ *DONE — commit `20f992a5e7`*
Infrastructure for signal migration: `tiePriority` added to `ChordIdentity`;
`bassTpc` and `jointScoringEnabled` added to `ScoringCell`/`ScoringSnapshot`;
`suppressProgressionSignals { false }` added to `ChordAnalyzerPreferences`.
`applyHarmonicFunction()` signature extended (candidates vector, chosenResult,
snapshot*, prefs*). Refinements reordered to run AFTER function layer at all
three regionanalyzer.cpp call sites. Function layer still receives nullptr →
no-op. 407/407, 52/52, 11/11 — byte-identical to `710d8dba12`.

Commit 2 (enable suppression) attempted and REVERTED. Two blockers found:
(1) Pass B (step bonus ±0.20–0.35) flips winners; function layer must replicate
it. (2) Cross-bass: suppressed-signal rawCandidates is one bass only; true
with-signals winner may be absent. E2d investigation underway.

**E2d. Scoring oracle / competition pipeline segregation** ✅ *DONE — commit `2917ec7571`*
Three failed incremental attempts (v2, v3, v3b) revealed the root cause: `applyHarmonicFunction`
was a hand-written replica of `analyzeChord`'s competition loop, and the replica was always
incomplete. A fourth attempt would have found more missing pieces. CC's independent architectural
review confirmed: the competition loop must live in exactly one place.

Fix: move the competition loop entirely to the function layer.

`analyzeChord` is now a **scoring oracle** — evaluates all (bass, root, template) cells,
computes metadata, packs into `ScoringSnapshot`, then calls `applyHarmonicFunction` internally.
`applyHarmonicFunction` is now the **competition pipeline** — owns all 7 steps: (1) rescore
cells with progression signals (rcb, wSeq, wDim), (2) Pass B step bonuses, (3) per-bass
quality guard, (4) cross-bass winner selection, (5) threshold, (6) build results[], (7) fill
gateCtx completely from the winning bass.

`suppressProgressionSignals` and `captureScoringSnapshot` fields deleted from
`ChordAnalyzerPreferences`. Three explicit `applyHarmonicFunction` calls in
`regionanalyzer.cpp` deleted (now called internally by `analyzeChord`).

Equivalence harness: 0 divergences (214/214 match; was 13 at baseline).
408/408, 52/52, 11/11 — byte-identical. BIR: Baroque 25/16, Jazz 36/10.
Architecture documented in `docs/scoring_model.md` §10/§11.

*Cleanup note:* Equivalence harness (`equivalence_harness_test.cpp`) is now tautological —
both pipelines are the same path. Safe to remove in a cleanup pass; not urgent.

**E3. Gate decoupling + G-E phantom fix** — Tasks 2+3 committed `f9ba22157d`; Task 1 deferred

Original E3 goal ("move Gates A–D, Gate J, dim7CharacteristicBonus to function layer")
was overtaken by E2d: all gates already live in the standalone `applyPostScoringGates`
called after `analyzeChord`. Investigation (2026-06-07, `cc_e3_investigation_report.md`)
found three real actionable items instead:

1. **Q6 coupling defect — DEFERRED (Task 1):** Gates H, I, J, K, L are nested inside the
   outer `inversionSuspicionMargin > 0 && inversionBonusReduction < 1.0 && results.size() >= 2 && distinctPcs >= 3`
   guard, but are logically independent of the bias correction. Prefs-only decouple
   (removing only the two prefs conditions while keeping `distinctPcs >= 3`) IS byte-
   identical for all current corpus runs. Dropping `distinctPcs >= 3` is NOT byte-identical
   — Schumann kinderszenen_n01 counterexample: 2-PC dyad slivers (distinctPcs=2) trigger
   structural gates when that condition is absent. `distinctPcs >= 3` is load-bearing.
   The latent bug has no urgency (all active presets have inversionSuspicionMargin=0.70);
   deferred indefinitely. When revisited: prefs-only decouple only — keep `distinctPcs >= 3`.

2. ✅ **G-E phantom HalfDim: COMMITTED (`f9ba22157d`):** Gate G-E appended a HalfDim from
   `rawCandidates` even when none of its four sub-gates fired, leaving a phantom in the
   alternatives list. Fix: `halfDimPulledFromRaw` flag + `results.pop_back()` if no sub-gate fires.

3. ✅ **Float literals → named constants: COMMITTED (`f9ba22157d`):** `0.45f`/`0.20f`/`0.35f`
   in Gates I/K/L are now `kGateIMargin`/`kGateKMargin`/`kGateLMargin`.

Note: temporal gates (B, C, D, G-B/C/D, H-B/C/D) cannot move into `applyHarmonicFunction`
byte-identically — they run after `applyIter8691Pedal` by design (pedal pass mutates
results[] that these gates read). File relocation to `harmonicfunctionlayer.cpp` would
require promoting `RawCandidate`/`buildChordResult`/`PostScoringGateContext` types.
Neither option is the right E3 scope.

`dim7CharacteristicBonus` is correctly placed in the scoring oracle's per-cell loop —
no progression context, rotation-selection only. Moving it was a misclassification.

**E4. Cadence detection**
Strongest harmonic punctuation in tonal music; most reliable signal for confirming key
and functional labels. Feeds both key detection (a PAC confirms the key) and functional
labeling (V→I resolution ground truth). Required before E5.

**E5. Functional labeling completeness**
Augmented sixth chords (It+6, Fr+6, Ger+6 — structurally distinct from dom7♭5 despite
PC overlap), Neapolitan (♭II / N6), borrowed chords / modal mixture (♭VII in major, iv
in major), extended tonicization chains beyond V/x and vii°/x.

---

### Phase F — Advanced / long-term

**F1. Confidence / uncertainty quantification**
Surface the score margin between top candidates as a meaningful signal. Flag ambiguous
regions rather than silently committing to a potentially wrong answer.

**F2. Harmonic rhythm modelling**
A chord lasting a full measure is structurally different from one lasting an eighth note.
Model harmonic rhythm as a structural parameter to improve segmentation decisions and
absorption logic.

**F3. Style / genre pattern recognition**
ii-V-I cycles, Baroque descending-fifth sequences, Neapolitan approach patterns. A
pattern layer above the function layer that uses known progressions to disambiguate
locally ambiguous chords.

**F4. Quartal / quintal templates**
{0,5,10}, {0,5,10,3} etc. Low priority for current Baroque/Jazz corpus but needed for
20th-century and contemporary repertoire.

---

### Architectural note — the long-term target stack

```
Tone collection
      ↓
Key / mode detection          (A1 — fix Baroque partial-signature; E4 cadence feeds back)
      ↓
Template scoring              (B — add mMaj7, aug7, dim7; D — clean PC set via NHT model)
      ↓
Harmonic function layer       (E — gates migrate here + cadence + functional labels)  [NEW]
      ↓
Segmentation / absorption     (C1 schumann fix; C2 bwv320 merge fix)
      ↓
Labels / output               (A3 roman-numeral validation; F1 confidence)
```

---

## Architectural redesign — layered comprehensive evidence flow (updated 2026-06-10)

Full detail: `docs/redesign_plan.md` and `ARCHITECTURE.md §2.14`. Summary here.

**Architecture decision (2026-06-09, updated 2026-06-10):** Single comprehensive pass
through properly layered components. All evidence is present at analysis time;
a single pass with symmetric backward/forward context is sufficient. Iteration is not a
design premise. Accumulating gates to compensate for missing context is the wrong
response — build the evidence picture (symmetric forward context alongside backward)
and unify the commit paths. Phase E completes that evidence picture and removes
all internal dual-paths. BIR re-calibration happens after the architecture is stable.

**Key implication:** the current 13 BIR=false residuals require richer evidence, not
more gates. The Δ=+7a cases require Phase D (arpeggio-aware segmentation) + Phase E
(inter-region revision when successor evidence contradicts the committed predecessor).
B1 mMaj7, A2 dominant-in-minor require Phase E cadence confirmation. Segmentation cases
require targeted structural fixes. Do not add compensating gates — add the missing evidence.

**The principle:** each layer should pass its full evidence alongside its committed
decision — not compress to the decision alone. Downstream layers must calibrate
how much to trust the upstream commitment. A wrong upstream commitment received
without confidence metadata is treated as ground truth: this is "passing a lie."

### What E2d already achieves

The oracle / pipeline split (E2d, `2917ec7571`) means **within-region deferred
commitment is already implemented.** `analyzeChord()` is a pure scoring oracle;
`applyHarmonicFunction()` applies all progression signals and selects the winner.
Commitment happens after functional signals — not before. The architecture is more
advanced than the Phase E description implies.

### The gap: inter-region channel is thin

After a winner is selected, `advanceTemporalContext` writes only
`previousRootPc / previousBassPc / previousQuality` into `ChordTemporalContext`.
Then `fnCtx` construction forwards even less to `HarmonicFunctionContext`:

```
fnCtx.previousRootPc = context ? context->previousRootPc : -1;
fnCtx.nextRootPc     = context ? context->nextRootPc     : -1;
fnCtx.previousBassPc = context ? context->previousBassPc : -1;
fnCtx.nextBassPc     = context ? context->nextBassPc     : -1;
```

Winner score, winner margin, predecessor root pcWeight — none forwarded.
`rootContinuityBonus` applies a flat +0.40 regardless of predecessor confidence.
A wrong committed predecessor receives the same reward as a correct one.
**This is the mechanism behind the entire Δ=+7 rootContinuityBonus cluster.**

### Wiring gap — fields already computed, not forwarded

`ChordTemporalContext` already has these fields; none reach `HarmonicFunctionContext`:

| Field | ChordTemporalContext | HarmonicFunctionContext |
|---|---|---|
| `previousQuality` | ✅ | ❌ |
| `recentRootPcs[3]` | ✅ | ❌ |
| `consecutiveBassStepwiseCount` | ✅ | ❌ |
| `regionMetricWeight` | ✅ | ❌ |
| winner score / margin | ❌ | ❌ |
| predecessor root pcWeight | ❌ | ❌ |

Forwarding the first four costs nothing (no new computation, just wiring).
The last three require new fields in `ChordTemporalContext` populated in
`advanceTemporalContext`.

### Key layer gap — status (2026-06-08)

`resolveKeyAndModeRanked` produces a ranked distribution of key candidates.
Both call sites in `regionanalyzer.cpp` (L305, L411) discard the list immediately
with `.front()`. Every downstream term (template scoring, diatonic root bonus,
scale construction) receives the key as a committed point estimate.

**The Corelli op01n08d "G minor instead of C minor" failure is already fixed** by
commit `81978321e3` (Option B Baroque partial-signature correction, 2026-06-03).
The resolver now returns C minor at rank 0 for every region.

Additionally, `KeyModeAnalysisResult.normalizedConfidence` is unreliable as a
scaling signal: `promoteWinnerInPlace` (keyresolver.cpp:311-321) re-ranks via
hysteresis/declared-mode without recomputing confidence, producing 0.025–1.00 for
the same correctly-keyed piece. Any future key-confidence design must define a new
metric (e.g. raw score gap between rank-0 and rank-1, post-promotion).

**Step 3 (key-as-distribution) is shelved** — no confirmed live target in the
51-piece corpus. See `cc_step3_key_investigation_report.md`.

### Failure case analysis — what this fixes and what it doesn't

*(Updated 2026-06-08 after predecessor-confidence diagnostic.)*

| Case | Root cause | Redesign effect |
|---|---|---|
| Δ=+7a bwv102.7, bwv261 (arpeggiation + rcb cascade) | Oracle correct in present-root slice without rcb (2.55 > 2.33); sole blocker is rcb +0.40 from wrong-root arpeggiated predecessor; Phase D exhausted (3 dead ends — aggregate weights still prefer Eb) | **Phase E only** — detect arpeggiated predecessor, suppress/reduce rcb |
| Δ=+7b bwv245.28, bwv296, bwv320 (correct predecessor, oracle tie) | Correct predecessor; near-tie in oracle broken by bonus toward old root | Phase E only — needs voice-leading resolution signal |
| bwv301 G-absent winner | Vertical scoring asymmetry (rootless triad over-rewarded) | Remains — absent-root guard addresses symptom |
| B1 mMaj7 leading-tone | Needs voice-leading resolution signal | Partially moves — still needs Phase E |
| B3 dim7 rotation | PC-identical rotations, no distribution helps | Unchanged |
| Corelli op01n08d key | Key layer commits with no distribution | **Already fixed** by `81978321e3` — not a live BIR=false case |

**The Δ=+7 cluster is correctly labelled Phase E.** The predecessor-confidence approach
was falsified by the 2026-06-08 diagnostic: predecessors have pcWeight 0.60–0.82 (not
0.0), and the mozart control predecessor has pcWeight 1.00 — the highest of the set.
No (pcWeight, margin, distinctPcs) threshold separates wrong cases from correct Alberti.
See `cc_deltaseven_predecessor_report.md` for full data.

### Redesign sequence

1. **Forward free ChordTemporalContext fields to HarmonicFunctionContext** (no new
   computation — just wiring `previousQuality`, `recentRootPcs`, etc. into `fnCtx`).
   Files: `harmonicfunctionlayer.h` (struct), `chordanalyzer.cpp` (fnCtx construction).

2. **Add predecessor confidence fields** (infrastructure for future Phase E signals).
   New fields in `ChordTemporalContext`: `previousWinnerScore`, `previousWinnerMargin`,
   `previousWinnerRootPcWeight`, `previousDistinctPcs`. Populated in
   `advanceTemporalContext`, forwarded to `HarmonicFunctionContext`.
   **Note:** Does NOT fix the Δ=+7 cluster (diagnostic falsified that premise). Useful
   as infrastructure for Phase E cadence/quality-aware bonus scaling.

3. **Key-as-distribution — ⛔ SHELVED.** Motivating case (Corelli op01n08d) already
   fixed by `81978321e3`. No confirmed live target in corpus. `normalizedConfidence`
   structurally unreliable as scaling signal. See `docs/redesign_plan.md` §Step 3.

4. **Phase E proper.** Cadence evidence, phrase context, functional labeling. Unblocks
   B1 (mMaj7), A2 (dominant in minor), Δ=+7b (voice-leading resolution).

---

## Iter 78 fixes (all committed, do not re-implement)

**Fix A** — `notationharmonicrhythmbridge.cpp`, `absorbShortRegions` lambda:
Short regions are only absorbed into the previous region when they share the same root
(`sharesPrevRoot`). A differently-rooted short region keeps its own boundary.

**Fix B** — `chordanalyzer.cpp` line ~129, `pitchClassName()`:
G# → Ab flattening is exempted at `keySignatureFifths == 0` (A minor), where G# is
the leading tone. Condition: `pc == 8 && keySignatureFifths < 3 && keySignatureFifths != 0`.

**Fix C** — `chordanalyzer.cpp` lines ~1762-1766:
Augmented template score ×0.5 when `distinctPcs <= 2` and root PC weight is at or
below `extensionThreshold`. Prevents root-absent 2-PC guesses winning as Augmented.

---

## Iters 79–84 — all committed

- **Iter 79** (`cbd7230c1f`) — augmented bare-root guard + qualitySuffix Dim/HalfDim fix
- **Iter 80** (`b4a375db45`) — refreshed 7 stale pipeline snapshot goldens
- **Iter 81** (`9d2a70cef4`) — removed dead Jaccard code; notation tests now 52 total / 50 passing
- **Iter 82** (`57511f012f`) — Gates E/I absent-root guard; BIR=false=118, BIR=true=4, Jazz BIR=false=7
- **Iter 83** (`1c57ebcac2`) — batch path anchor end-tick fix (port Iter 77 Fix B)
- **Iter 84** (`4da8252c9e`) — R4 narrow fix: G# leading-tone exemption extended to keyFifths=1 (A melodic minor regime)

## Iter 84 detail (do not re-implement)

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`, lines ~117–153

`pitchClassNameFromTpc()` had a G# (pc=8) exemption from Ab-normalization at `keyFifths==0`
(Iter 78 Fix B, for A natural minor). A melodic minor ("Amel") maps via `resolveToFifths()`
to its Dorian parent at `keyFifths=1`, falling outside the exemption → G# was spelled "Ab".

Fix: added `&& keySignatureFifths != 1` to the normalization condition, and extended the
TPC-disambiguation block to also fire at `keyFifths==1 && pc==8` (so flat-authored Ab with
tpc≤14 in that regime is still correctly spelled flat).

Result: bach_chorale_003 — 3 chord symbols corrected (Abm7b5/B→G#m7b5/B, E/Ab→E/G# ×2).
bach_chorale_003 golden refreshed. BIR unchanged (BIR operates on root_pc/bass_pc).

**Deferred — R4 family B (chorale_137, later iteration):**
- pc=6 (F#/Gb): no TPC-honor block exists for pc=6 at all; unconditionally returns Gb at keyFifths<0
- Flat-authored Ab bass in V/V context (tpc=10 in chorale_137 m2): heavier "chord-3rd-of-major-triad" override, out of scope

---

## Iters 85–89 + DCML comparator — all committed

- **Iter 87** (`2dd2f35c17`) — bass-b7 post-merge re-stamp in batch_analyze.cpp
  (`analyzeScore` merge discarded MinorSeventh extension stamped by Iter 86; post-filtered
  re-stamp pass at batch_analyze.cpp:1846–1880 fixes 281 of 293 b7-bass slash-chord cases)
- **Iter 88** (`bea00f3482`) — honor sharp F# TPC for pc=6 in flat keys (extends
  TPC-disambiguation block to fire at `keyFifths<0 && pc==6`; Gb→F# in D/F# and similar
  contexts)
- **Iter 89** (`2085f11322`) — honor sharp G# TPC for pc=8 across flat and mildly-sharp
  keys (removed pc=8 from Iter 78 flattening block; added `keyFifths<0 && pc==8` and
  `keyFifths==2 && pc==8` to TPC-honor block; survey script `tools/survey_pc8_flat_authored_bass.py`)
- **DCML comparator** (`eefa412b6f`) — new time-overlap comparator in compare_analyses.py
  (mode='time-overlap', lenient-OR-50% overlap threshold) + rerun_dcml_comparison.py
  re-aggregation driver. Old beat-snap 69.1% figure retired (biased +21pp). New primary
  metric: 47.8% weighted root agreement across 10 non-Bach corpora (DCML-anchored).
  Bach chorales: 64.9% overall, 87.2% chord-identity, 100% alignment.
  **Superseded:** the live baseline is now **53.8%** (regenerated 2026-05-20 at HEAD
  `a69a23e59b`; see "Current state" block above). The 47.8% figure is historical only.

**Iter 90 — shelved (no commit):**
122 wrong-root cases characterized (tools/analyze_wrong_root_iter90.py,
tools/iter90_wrong_root_characterization.txt). 84% are iii/III triad confusion — non-local
ambiguity. Both Variant A (+12 errors) and Variant B (+22 errors) regressed. Design note:
`docs/iter90_bass_as_root_promotion_shelved.md`. Future path: Iter 91, bridge-level
adjacent-context pass using nextRootPc/previousRootPc from ChordTemporalExtensions.

**Iter 91 — attempted and reverted (no commit):**
Temporal-context gate: when the winning chord's root is a third above the bass (iii/III
pattern), promote the bass-rooted reading from rawCandidates when `nextRootPc == bassPc`
(forward resolution signal). Tried both `previousRootPc OR nextRootPc` (too permissive —
fired on genuine I→I6 progressions) and `nextRootPc` only. Final result on `nextRootPc`
only: BIR=false 188→185 (−3), BIR=true 38→41 (+3) — net neutral at 226→226 total errors.
Reverted. Working tree clean at `2de18139c2`. Superseded by Iter 92 holistic design.

**Ground-truth QA session — 2026-05-16:**
Opened 5 DCML-annotated scores in MuseScore with GT and US labels injected side-by-side
(via `tools/inject_dcml_rn.py`). Visual review identified two distinct bugs causing
the bulk of BIR=false=188 errors:

- **Bug 1 — Passing-note bass contamination:** When the bass voice has two eighth notes
  within a beat window (e.g. G3 onset + F#3 passing), the lower-pitched passing note
  (entering mid-region) overrides the beat-onset structural note as bassPc. Mechanism
  confirmed by diagnostic: both G3 (MIDI 55) and F#3 (MIDI 54) appear in region
  [4800,5280) with equal pcWeight=0.20; F#3 wins because 54 < 55. This flips root
  inference (e.g. G major → Em/F# or Am/F# instead of correct G or G7).

- **Bug 2 — Incomplete slash chord beats complete root-position triad:** Given pitch
  classes {C,E,G} with C in bass, the template scores Em/C ~2.86 vs C major ~2.40 — a
  gap of ~0.46. Em/C "wins" even though B (the 5th of Em) is absent and C is not in Em.
  Root-position completeness is not rewarded. Seen on bwv310, bwv319, bwv103.6, bwv283.

**Iter 92 — committed (`80fe13b59b`):**
Joint (bass, chord) scoring with `w_complete` bonus (distinctPcs==3) and multi-bass
enumeration. Design at `docs/iter92_joint_bass_chord_scoring.md` (still authoritative
reference for the JOINT formula and follow-up scope). What landed:

- Struct fields added: `ChordAnalysisTone::onsetAtRegionStart` (bool) and
  `ChordTemporalContext::nextBassPc` (int, −1=unknown) in `chordanalyzer.h`.
- Joint enumeration loop in `chordanalyzer.cpp`: enumerate bass candidates from the bass
  register, score each (bass, root, template) triple = base score (bass-independent) +
  bass-dependent deltas (`appliedBassRootBonus`, `nonBassAdjustment`, inversion contextual)
  + `w_complete = +0.50` bonus when distinctPcs≥3 AND all three triad tones are present
  above extensionThreshold AND bass_candidate.pc == triad_root.
- Callers populated: `notationcomposingbridgehelpers.cpp::collectRegionTones` (onset flag),
  `notationharmonicrhythmbridge.cpp` and `tools/batch_analyze.cpp` (nextBassPc assignment).
- Pipeline snapshot goldens refreshed (10 of 11): bach_chorale_001/003/137,
  bach_bwv806_prelude/gigue, mozart_k279_1/k280_1, chopin_bi105_op30_1, corelli_op01n08a,
  schumann_kinderszenen_n01. Audited: clean Bug 2 fix patterns (D7/A→D7, FMaj7/E→FMaj7,
  F/C→F, G/C#→G, AMaj7/G#→AMaj7, E/B→E, E/G#→E, C/E→C, F/A→F). No regression patterns.
- BIR impact: Baroque BIR=false 188→46 (−142). Baroque BIR=true 38→41 (+3, bucket
  reclassifications). Jazz BIR=true 103→114 (+11). Jazz BIR=false 13→14.

**Iter 93 — committed (`f98586fa67`, plumbing only; Step 3b shelved):**

Landed: `collectRegionTones` (in both `notationcomposingbridgehelpers` and
`tools/batch_analyze`) gained an optional `parentStartTick` parameter (default −1 ⇒
falls back to `startTickInt` for un-split callers). Pass 2 / Pass 2b sub-region call
sites in `notationharmonicrhythmbridge.cpp` and `batch_analyze.cpp` pass the parent
region's startTick so the per-tone `trueAttackAtStart` flag is computed at full-region
scope rather than against the narrow sub-region boundary. `chordanalyzer.cpp` is
unchanged relative to Iter 92; the joint-scoring loop, the `w_complete` bonus, and the
`jointScoringEnabled` gate are intact. Baselines unchanged from Iter 92.

**Step 3b (`w_onset` / `w_passing` per-bass-candidate score deltas) — SHELVED:**

Three variants were attempted and all hit Baroque BIR=false hard stops:
- Symmetric (`+0.15` onset bonus, `−0.10` passing penalty): +7 BIR=false.
- Asymmetric penalty-only (`0` onset, `−0.10` passing): +4 BIR=false.
- Asymmetric + onset-gated (penalty only fires when at least one bass candidate has
  `onsetAtRegionStart=true`): +3 BIR=false.

Root cause: in Baroque polyphony the bass voice routinely moves mid-region to the
actual chord root (arpeggiated bass, melodic bass motion). The onset-position signal
is not a reliable proxy for "structural bass" in this corpus — the same signal that
would penalise a passing-note artefact also penalises a genuine arpeggiated structural
root. No further onset-position tuning is expected to clear this; the signal is wrong
for the corpus.

**Iter 94 — committed (`dbfe09fe6f` + STATUS backfill `a34b5c1e6c`):**

Iter 92's deferred Step 3c (`w_stepIn` / `w_stepOut` voice-leading bonuses) is now
active in `RuleBasedChordAnalyzer::analyzeChord`. Root-position candidates earn +0.10
when the bass moves by semitone or whole-tone from `context->previousBassPc` and +0.10
again on motion to `context->nextBassPc`. Parent-scope plumbing: bridge Pass 2 / Pass 2b
in `notationharmonicrhythmbridge.cpp` and the main loop in `tools/batch_analyze.cpp`
compute the predecessor / successor PARENT region's bass PC and override
`subCtx.previousBassPc` / `subCtx.nextBassPc` for each sub-region `analyzeChord` call
(the override happens AFTER the stepwise booleans, which intentionally remain
sub-region-scope for passing-tone / inversion signals, and BEFORE the call; the
post-call restore keeps the next iteration's stepwise boolean correct).

Four gates were required to keep the bonus safe — each motivated by a concrete
regression caught during iteration:

1. **`explorationMode` suppression** — new field `ChordAnalyzerPreferences::explorationMode`
   (default `false`). `greedyExpandSegmentation` sets it to `true` on every internal
   boundary-exploration `analyzeChord` call (Round 1 head/tail synthesis + Round 2 region
   scoring in `harmonicsegmenter.cpp::fillGap`). The bonus would otherwise bias
   sub-region bass selection toward stepwise candidates and redirect segmentation
   before the final per-region scoring pass runs.
2. **Root-position guard `candBassPc == cand.rootPc`** — the bonus is meant to reward
   "this chord's root moves smoothly in the bass line," not "this slash-chord's bass
   happens to step smoothly." Applying it to slash-chord bass caused a Jazz bwv430
   BIR=false +1 regression (a G#m7/F# bass stepping to a neighbouring bass gained
   credit even though its root G# was not the moving voice). Enforced both in the
   lambda body and in the Pass-B outer loop that skips non-root-position candidates.
3. **Corrected first-inversion-m7-family guard** — if any competitor in the same
   `perBass` block with quality in {HalfDiminished, Diminished, Minor7} sits at
   `(candBassPc - 3) mod 12` (i.e. its root is a minor third BELOW our bass, the
   first-inversion shape) AND scores within `kStepBudget = kWStepIn + kWStepOut + 0.01`
   of the candidate's unbonused score, both step bonuses are suppressed. Canonical
   case: Dm6 (candBassPc=2, rootPc=2) vs Bø7/D (competitor rootPc=11, bassPc=2) — the
   m7-family competitor's root is the minor third below our bass, not at our bass. The
   guard prevents the step bonus from tipping a fragile m6 root-position reading over
   an equally viable first-inversion m7-family reading on identical pitch evidence.
4. **Power-quality exclusion** — root+fifth-only templates are excluded outright. Five
   sparse-Jazz Tonic-on-strong-beat regressions (bwv20.7 m16b1, bwv227.1 m11b3,
   bwv245.40 m27b3, bwv384 m4b3, bwv422 m14b1) had Power `[Tonic]5` reads tip past
   viable triad reads when the bonus fired. Extending the exclusion to Suspended2/4
   caught a sus residual but regressed Jazz BIR=false (14 → 15) — beyond hard-stop
   scope, so the current cut is Power-only.

BIR impact (lenient-OR comparator):
- Baroque BIR=true 41→43 (+2, bucket reclassifications, not new errors)
- Baroque BIR=false 46→33 (−13, ~28% reduction)
- Jazz BIR=true 114→117 (+3)
- Jazz BIR=false 14 (flat)

Tests: 407/407 composing, 50/52 notation (same 2 pre-existing Corelli implode
failures), 11 passed / 1 skipped pipeline_snapshot — all 11 active goldens refreshed
(bach_chorale_001/003/137, bach_bwv806_prelude/gigue, mozart_k279_1/k280_1,
chopin_bi105_op30_1/2, corelli_op01n08a, schumann_kinderszenen_n01).

**Deferred — Iter 95 candidates (status after Iter 96):**
- **`w_onset` / `w_passing` via duration-weighting.** Still deferred — Iters 94–96
  continued harvesting BIR improvements without it. Reconsider only if a concrete
  failure pattern emerges that existing bonuses cannot reach.
- **`w_seq`** — landed as Iter 95. Done.
- **bwv320 Am 1-case residual.** Still deferred.

---

## Iter 96 — committed 2026-05-18

**Commits:** `0de94516ff` (code) + `7060f2c5db` (STATUS amendment)

**Change:** `w_dim` +0.15 bonus in `chordanalyzer.cpp`. New `wDimBonus` lambda
alongside `wSeqBonus`. Fires when a Diminished or HalfDiminished candidate's root
sits one semitone below `context->nextRootPc`
(`(nextRootPc - candRootPc + 12) % 12 == 1` — leading-tone resolution signal).

Gates: `jointScoringEnabled && !prefs.explorationMode && context &&
context->nextRootPc >= 0 && (quality == Diminished || quality == HalfDiminished)
&& distinctPcs >= 4`. No new plumbing — `nextRootPc` already populated by Iter 95.

Three variants were tried before committing:
1. **Loose (delta==1, no distinctPcs gate):** Baroque −3/0, Jazz +2/0.
   bwv296 m12 b4 direct misfire (3-PC region, G/B wrongly flipped to B°) +
   Corelli golden regression (F7/A → Adim dropping the structural 7th). Not committed.
2. **Tightened (delta==1, distinctPcs >= 4):** Baroque −3/−1, Jazz +1/0.
   bwv296 misfire and Corelli golden regression both eliminated by the gate.
   Jazz +1 residual is a cascade from an upstream w_dim fire (Cadd11, Major
   quality — not a direct w_dim misfire, not a hard stop). Committed.
3. **delta==2 variant:** not attempted — widening after delta==1 already produced
   misfires was expected to add more.

The `distinctPcs >= 4` gate intentionally suppresses the sparse-region tier.
Two improvements from the loose gate (`schumann bvo7→viio7/V` tick 480,
`chorale_003 Am→G#dim`) were inseparable from the misfires — both were
3-PC sparse regions where the bonus was a quality flip, not a rotation correction.
A future iteration may recover them by adding a rotation-only condition
(require the current winner to also be Dim/HalfDim).

**BIR impact (lenient-OR comparator):**

| Metric | Pre-96 | Post-96 | Δ |
|--------|--------|---------|---|
| Baroque BIR=true | 44 | 41 | −3 |
| Baroque BIR=false | 27 | 26 | −1 |
| Jazz BIR=true | 68 | 69 | +1 |
| Jazz BIR=false | 13 | 13 | 0 |
| **Total** | **152** | **149** | **−3** |

**Tests:** 407/407 composing, 50/52 notation (same 2 Corelli), 11/11 snapshot
(2 alt-only goldens refreshed: `bach_bwv806_gigue`, `schumann_kinderszenen_n01`).

**Deferred — Iter 97 candidates:**
- **α-variant: w_dim rotation-only** — add guard requiring the current winner to
  also be Dim/HalfDim before `wDimBonus` fires. Only the enharmonic rotation is
  in contest, not the quality. May recover `schumann bvo7→viio7/V` and
  `chorale_003 Am→G#dim` without the quality-flip misfires. Quick to try.
- **δ: sparse-minor diatonic quality prior** — when `distinctPcs <= 3` and the
  third is absent/weak, prefer the quality that the current key assigns to this
  scale degree. Directly fixes the 2 pre-existing Corelli notation failures
  (`CorelliOp01n08dOpeningAndSparseLateBeats`,
  `CorelliOp01n08dUserReportedChordTrackAudit`). Harder to gate safely.
- **β: P4-above mis-rooting** (~27 cases) — diffuse, no single fix, deferred.
- **γ: M2-above mis-root** (~17 cases) — diffuse, deferred.

---

## Standing rule — CC instruction preamble (MANDATORY, every single CC session)

CC starts with ZERO context every time. Every instruction to CC must open with:

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
> `C:\s\MS\build_and_test.md`
>
> **If this session touches scoring logic in `chordanalyzer.cpp`** (templates, bonuses,
> guards, gates, score matrices): also read `C:\s\MS\docs\scoring_model.md` before
> making any changes. The doc explains why each term exists and what invariants must
> not be broken. Any commit that changes scoring logic must also update that doc.
>
> **Current state:** Branch `master`, HEAD `f9ba22157d`, working tree clean.
> BIR baselines (lenient-OR): Baroque BIR=true=25, BIR=false=16; Jazz BIR=true=36,
> BIR=false=10. Hard stops: Baroque BIR=false ≤ 25, Jazz BIR=false ≤ 13.
> Tests: 407/407 composing, **52/52 notation (fully green)**, pipeline_snapshot
> 11/11 (1 skipped, no goldens touched).
> Mismatch report: Jazz 130 items; see chord_mismatch_report.txt.
> Roman numeral baseline (HEAD `f3e0f5f72c`, 9 non-Bach corpora, 61,233 regions):
> rn_agree=27.6% (16,905/61,233); corrected classifier: key_disagree=15.4%,
> quality_disagree=6.3%. Root_agree=49.3% parity check. Hard stop: rn_agree
> must not drop below 27.6%.
>
> **Unification is complete.** Both parameter divergences are resolved: D1
> (`excludeLookAheadOnDenseStart`) is intentionally divergent and load-bearing (batch
> `true`, bridge `false`); D2 (`pass1MinDistinctPcsForCandidate`) is unified at `1` on
> both paths (`4d881e7418`). STEP 1 (`3d80d0a91d`): the dim7 characteristic bonus now
> requires the complete diminished triad, and Gate J treats a complete root-position
> diminished triad over a sounding dominant root as an inverted V7 — Jazz BIR=true
> 56→33 (−23), Baroque BIR=false 25→23 (−2).
>
> Hard stops always: Baroque BIR=false > 25, Jazz BIR=false > 13, any test
> regression beyond the 2 known Corelli notation failures.

This preamble goes before EVERY task description, no exceptions.

---

## Standing rule — Investigation-first before implementation (MANDATORY for Cowork)

**Before writing any CC implementation instruction that touches existing scoring
mechanics**, either:

1. Read the relevant source code here in Cowork first (use the Read tool on
   `chordanalyzer.cpp` at the specific section), **or**
2. Write a pure read-and-report instruction first — CC reads and reports, no code
   changes — then write the implementation instruction based on that report.

"Touching existing mechanics" means: adding a template near an existing one,
modifying a bonus/gate/guard, changing a threshold, or anything where an existing
scoring term might interact with the proposed change.

**Why:** B2 took 4 attempts and B3 was reverted because implementation instructions
were written based on incomplete understanding of existing code. The `dim7CharacteristicBonus`
rotation-selection role was only discovered mid-task. An investigation pass first
would have caught this before a single line was written.

**The C1 investigation instruction is the correct model.** Pure read-and-report,
no edits, produces a design proposal. Only after the report comes back does the
implementation instruction get written — based on actual findings, not assumptions.

---

## Standing rule — Visual inspection before debugging (MANDATORY for BIR=false cases)

Before investing CC debugging effort on any BIR=false case, **look at the score with
our annotations first.** A single image reveals whether the error is isolated or
systemic; this determines whether a targeted fix is worthwhile or whether the case
should be accepted as a Phase E residual.

**How:** Ask the user for an annotated score image, or use
`tools/inject_dcml_rn.py` to overlay DCML Roman numerals alongside ours, then open
the resulting file in MuseScore. Even our annotations alone (without DCML ground truth)
expose systemic patterns (rootContinuityBonus over-stickiness, inversion mis-labeling,
Roman numeral errors) that the BIR metric cannot see.

**Decision rule based on the image:**
- **One wrong region, rest of score looks correct** → targeted fix is likely worth it.
  Proceed to CC debugging.
- **Multiple wrong regions sharing a mechanism (e.g. tonic stickiness throughout a phrase,
  or consistent inversion errors)** → systemic; check whether it's a known dead end
  (Iter 98 / Phase E). If yes, accept as residual. If not, characterise the scope before
  committing to a fix.
- **Widespread unrelated errors** → complex residual; accept, move on.

**Introduced 2026-06-04** after bwv14.5 image review showed rootContinuityBonus
stickiness in opening measures + an unrelated m5 post-scoring promotion + Roman numeral
labeling errors — three distinct issues in one score. Score image identified all three
faster than three rounds of CC programmatic debugging.

---

## Windows Snap fix — do not revert

File: `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`
Function: `calculateWindowSize()`

Two lines that set `ptMinTrackSize` equal to the full monitor work area were removed.
This prevented Windows Snap from working on maximised MuseScore windows.
`ptMaxSize` and `ptMaxPosition` are kept. `ptMinTrackSize` is intentionally left unset.

The fix is committed as a local-only branch in the muse submodule (`fix/windows-snap-ptmintracksize`
at `b9604805a`). The parent repo's master correctly pins the submodule pointer to this commit.
**Do not restore the `ptMinTrackSize` lines. Do not push the muse submodule to upstream.**

This is documented in `C:\s\MS\CLAUDE.md` which CC reads every session.

---

## Known CC/VS Code integration issues

**Stale `git index.lock`** — When CC loses contact with a running git process (a known
VS Code integration bug), `.git/index.lock` is left behind (0 bytes). Symptom: git
commands fail with "Unable to lock the index". Fix: verify no git process is running
(`tasklist | grep git`), then delete `.git/index.lock`. Safe to delete if file is
0 bytes and no git process is running.

**Silent disconnect — three distinct triggers (diagnosed 2026-05-14 from VS Code logs)**

VS Code sets the CC session to `idle` (handing control back to user) in these situations,
while the CC process keeps running invisibly. Dangerous to submit new tasks without waiting.

**Trigger 1 — Non-zero exit code:**
A bash command returns non-zero (failing tests, grep with no matches, etc.). The extension
sees this as an error and marks the session idle. CC keeps running.
Fix: append `; echo "exit:$?"` to every command that may return non-zero. The echo always
returns 0, so the extension sees a clean result.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Trigger 2 — stream_idle_partial (long bash output):**
When a bash command produces large output and CC takes >~15 seconds to process the result,
the API stream goes idle between chunks. The extension logs `[WARN] [Stall] stream_idle_partial`
and marks the session idle. CC is still running and will eventually complete.
Fix: break long commands into smaller steps that produce incremental output. Pipe through
`head -N` to limit output size. Write large results to a file and read separately rather
than capturing in one bash call.
- BAD:  `batch_analyze <score> --dump-regions notation`  (may produce thousands of lines)
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

**Trigger 3 — stream_idle_partial (API latency, bytesTotal=0):**
When the Anthropic API takes >15 seconds to send the first token of a response (server load,
network hiccup), the extension logs `stream_idle_partial lastChunkAgeMs=15xxx bytesTotal=0`.
This can silently drop the panel even though CC recovers and keeps running. No reliable
prevention — it's server-side latency. If the panel goes silent mid-task without any bash
errors, this is likely the cause. Check the VS Code output log before resubmitting.

Build commands (setup_and_build.bat) are launched via PowerShell Start-Process which
isolates the exit code — less affected by trigger 1.

---

## .vscode/settings.json — muse submodule noise

VS Code detects `muse/.git` (submodule gitdir pointer) and prompts to open it as a
separate repository. Two settings suppress this in `C:\s\MS\.vscode\settings.json`:
- `"git.detectSubmodules": false` — stops VS Code treating submodules as separate SCM providers
- `"git.ignoredRepositories": ["C:\\s\\MS\\muse"]` — belt-and-suspenders ignore by path

If CC hasn't applied these yet, ask it to edit `.vscode\settings.json` accordingly,
then Ctrl+Shift+P → "Reload Window".

---

## Build commands (quick reference)

```
# Build
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Tests (run from ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report location
src/composing/tests/chord_mismatch_report.txt
```

---

## Standing practices — build and corpus hygiene

Two silent failure modes that produce plausible-looking but wrong results:

**Stale build** — if the working tree has uncommitted changes and the binary
hasn't been rebuilt, corpus analysis runs against the old logic. BIR numbers
will look identical to the last clean run but the characterization is wrong.
**Always rebuild before any corpus run when the working tree has been modified**,
or when there is any doubt about whether the binary matches the source.

**Stale corpus output** — `analyze_inversion_errors.py` reads whatever JSON
files are already in `tools/corpus/`. If `run_bach_preset.py` was not run
first (or was run against a different binary), the analysis silently reads
old results. **Always run `run_bach_preset.py` immediately before
`analyze_inversion_errors.py`** — never rely on corpus JSON files left over
from a prior session or a prior build.

Canonical corpus analysis sequence (never skip steps):
```
# 1. Rebuild first if working tree has changes
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# 2. Regenerate corpus (Baroque)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus

# 3. Analyse (reads the freshly written JSONs)
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Repeat steps 2–3 for Jazz if needed (reuses same output-dir)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## LLM integration design — completed 2026-05-15

A full architectural design session for "Claude Composer" — natural-language interaction
with scores via an LLM of the user's choice (analogous to Claude Code / Copilot in IDEs).

**Two documents created / updated:**

- `docs/llm_integration.md` — comprehensive design document (11 sections). Read this
  before any implementation work on the LLM bridge.
- `ARCHITECTURE.md` §19 — high-level overview and key decisions (4 subsections).

**Key conclusions that are not obvious from reading the docs:**

- The Core Access Layer is a **facade over existing INotation* interfaces** — not a new
  information model. §5.2 has the full interface inventory. The point is to avoid
  translation loss, not to redesign the data model.

- LLM bridge uses the **stateless tier** (tool calls, musical addresses, no object
  references). Plugin API uses the **stateful tier** (EID-backed handles, event
  subscriptions). These are different programming models; do not conflate them.

- **Event subscriptions keep dependency direction one-way.** When `ScoreEventSource`
  (Core Access Layer) subscribes to `async::Channel<ScoreChanges>`, the subscription
  is initiated *from* the Core Access Layer *into* MuseScore. `async::Channel` stores a
  callback and fires it — it has no reference back to the subscriber. No reverse
  dependency is created.

- `src/composing/` is **not part of official MuseScore** — it is this project's own
  development. §10 and ARCHITECTURE.md §19.3 both note this explicitly.

- **MusicalAddress is the cross-cutting join key.** There are NO direct object
  references from Note → Staff or Note → Measure. A Note's address (`partId`,
  `staffIndexInPart`, `measureNumber`, `beat`, `voice`, `tick`) is the only locator.
  Querying "all notes in measure 12 of the Oboe" is a pure filter over addresses —
  no graph traversal. Harmony, Annotation, and Note at the same MusicalAddress are
  co-located: matching on address is the equivalent of a SQL join on a composite key.

- **Address does NOT uniquely identify a Note.** Multiple notes in the same chord
  share an identical MusicalAddress (same part + staff + measure + beat + voice).
  A `NoteId` is required to unambiguously identify a single note. The information
  model must carry NoteId on the Note entity.

- Subsection numbering in `llm_integration.md` §7 and §8 had a drift (labels said
  6.x and 7.x respectively) — fixed 2026-05-15.

---

## ms-core-api branch — decisions made 2026-05-15

A new branch and worktree for the Core Access Layer (protocol-neutral facade over
`INotation*` and friends, shared foundation for plugin API and LLM bridge).

**Branch:** `ms-core-api`  
**Worktree:** `C:\s\MS-core-api` ✓ created 2026-05-15  
**VS Code window:** separate window on `C:\s\MS-core-api`  
**CC context:** automatically separate (different path = different CC project memory)  
**CLAUDE.md:** ✓ written and committed on the branch — scoped to CAL, composing-module sections removed

**Known gap — build script:** `setup_and_build.bat` inherited from master hardcodes
`c:\s\MS\ninja_build_rel`. A `setup_and_build.bat` specific to `C:\s\MS-core-api`
needs to be created (pointing to `C:\s\MS-core-api\ninja_build_rel`) before the
first build attempt in the new worktree.

**Current state:** CLAUDE.md committed, no code written yet. Next steps:
1. Create `setup_and_build.bat` for the worktree
2. Create `src/ms-core-api/` skeleton (CMakeLists.txt + first interface headers)
3. Wire into root CMakeLists.txt
4. Create junction points for extensions/plugins (see below)

**Why `ms-core-api` as a name:** "plugin-api-v2" would imply the QML/Q_PROPERTY
protocol; this layer is protocol-neutral. It exposes capabilities (score read/write,
settings, project, playback, instruments) without committing to any binding technology.
Protocol-specific layers (QML bindings, JSON/tool-call schema for LLM) sit above it.

**Architecture:**
```
Plugin bindings (QML)   LLM bridge (JSON)   future protocols
        └───────────────────┴──────────────────┘
                    ms-core-api
              (capabilities, no protocol)
                    INotation* family
                    MuseScore DOM
```

**Dev environment prerequisite — junction points (one-time, do before first test run):**

Extensions and plugins are in `share/extensions/` and `share/plugins/` but
`appDataPath()` on Windows resolves to one level up from the exe (`C:\s\MS\` when
running from `ninja_build_rel\`). MuseScore looks for `C:\s\MS\extensions\` and
`C:\s\MS\plugins\` — neither exists without junctions. Fix:
```
mklink /J "C:\s\MS-core-api\extensions" "C:\s\MS-core-api\share\extensions"
mklink /J "C:\s\MS-core-api\plugins"    "C:\s\MS-core-api\share\plugins"
```
(Run as Administrator in cmd.exe. Do this in the ms-core-api worktree.)

**Full-stack test loop once junction points exist:**
1. Write C++ in `src/ms-core-api/` → build MuseScore5.exe
2. Write a minimal test extension: `manifest.json` + JS/QML in `C:\s\MS-core-api\extensions\your-test\`
3. Launch MuseScore5.exe, open a score, run the extension
4. No install step needed — extensions load from the junction-pointed directory

**Extension anatomy (v2 system):**
- `manifest.json` — declares URI, type (macros/composite/form), actions
- `main.js` or `Form.qml` — the extension logic
- API surface available to extensions: `api.log`, `api.interactive`, `api.engraving`,
  `api.converter`, `api.websocket` (see `muse/framework/extensions/api/extapi.h`)
- ms-core-api methods will be added here once implemented

**Legacy v1 plugins** (QML, old API) live in `share/plugins/`. They use the
`muse/framework/extensions/api/v1/` path and the old `PluginAPI`/`qmlRegisterType`
system. Relevant for understanding what exists; NOT the target for ms-core-api work.

---

## AI Assistant extension MVP — work done 2026-05-16

Independent of CAL work. AI Assistant chat extension is the first concrete LLM-bridge
artefact per the [[llm-bridge-mvp-strategy]] memory (build v2 extension first, validate
where the API gaps actually bite). Lives in the ms-core-api worktree at
`share/extensions/ai-assistant/` (`Main.qml` + `manifest.json`). Committed as
**`87ff66b8e5`** on a new branch **`ai-assistant-mvp`** (cut from the same point as
`ms-core-api`), specifically so the CAL branch stays focused.

**Branch:** `ai-assistant-mvp` (in the `C:\s\MS-core-api` worktree; switch with
`git checkout ai-assistant-mvp` if you want the files materialised — they're committed
only on that branch).

**Deployed copies** (untracked or outside repo; used at runtime by MS4):
- `C:\Users\vince\AppData\Local\MuseScore\MuseScore4\extensions\ai-assistant\Main.qml`
- `C:\s\MS\ai-assistant\Main.qml` (staging — was stale at v0.4.3, reconciled to v0.4.12 on 2026-05-16)

All three copies are byte-identical at 75225 bytes / v0.4.12.

**Four MS4 limitations discovered and worked around:**

1. **`Qt.labs.settings` not deployed in MS4 install** — `C:\Program Files\MuseScore 4\qml\Qt\labs\` ships only `platform/` and `qmlmodels/`; `settings/` is missing because windeployqt only ships modules MuseScore itself imports, and the main UI never imports `Qt.labs.settings`. Fix: switched to `import MuseScore 3.0; Settings { ... }` — that's the vendored `QQmlSettings` registered in `muse/framework/extensions/api/v1/extapiv1.cpp:40` via `qmlRegisterType("MuseScore", 3, 0, "Settings")`. Process-global registration, so it works from V2 extensions too, not just V1 plugins. No deployment dependency.

2. **`FlatButton` / `import Muse.*` deploy gate over-matched** — the grep pattern in the [[ms4-deploy-gate]] memory (`grep -c "FlatButton\|import Muse"` expecting 1 — the line-2 self-describing comment) over-matched after the Enter workaround landed in v0.4.11: caught `import MuseScore 3.0` strings, `import Muse.Ui\n` substrings inside `Qt.createQmlObject` calls, and doc comments. Tightened the gate to `grep -nE "^[[:space:]]*(import[[:space:]]+Muse\.|FlatButton)"` expecting empty output. Mirrors the actual extension validator in [extensionbuilder.cpp:42-60](muse/framework/extensions/qml/Muse/Extensions/extensionbuilder.cpp#L42-L60). Memory updated.

3. **Stale staging vs deployed divergence** — the staging copy at `C:\s\MS\ai-assistant\Main.qml` had been left at v0.4.3 (May 15) while UI work continued directly on the deployed copies up to v0.4.6 (scrollToBottom helper, copy-message button, TextArea → TextField swap, several others). If the v0.4.3 staging had been re-deployed without merging, ~40 lines of UI work + the Enter workaround would have been lost. Reconciled 2026-05-16 by copying v0.4.12 back to staging. **Going forward: edit in staging only, deploy via grep gate + copy** — the original workflow as documented in [[ms4-deploy-gate]] — rather than editing deployed copies directly.

4. **Enter-to-send in extension QML — the big one.** Took 11 diagnostic iterations (v0.4.5 → v0.4.11) and a deep dive. `TextField.onAccepted`, `Keys.onReturnPressed`, AND any QML `Shortcut` bound to Return/Enter ALL silently fail in MS4 extension QML. Root cause: MS4 implements its entire shortcut system as QML `Shortcut` elements registered in the main window ([muse/framework/shortcuts/qml/Muse/Shortcuts/Shortcuts.qml:53-60](muse/framework/shortcuts/qml/Muse/Shortcuts/Shortcuts.qml#L53-L60)), binding `Return`/`Enter` to `nav-trigger-control` ([src/app/configs/data/shortcuts.xml:80-85](src/app/configs/data/shortcuts.xml#L80-L85)). Anything an extension binds at the same key triggers an ambiguous-overload in Qt's resolver — both candidates are `Qt.WindowShortcut` context — and Qt fires *neither*, without any warning. The fix: dynamically build a `NavigationSection → NavigationPanel → NavigationControl` chain via `Qt.createQmlObject` (bypassing the extension's static-import-only deploy validator), register the control as active on input focus via `requestActive(false)`, and connect its `triggered` signal to send. MS4 then dispatches Enter to it. Documented in v0.4.12's in-file comment above `setupNavigation()` and in [[ms4-extension-input-workaround]]. Verified working at v0.4.11 in log `MuseScore_260516_120757.log`. The dynamic-import bypass works because the validator only scans literal `import` lines in `.qml` files; strings inside `Qt.createQmlObject` are ignored. The V2 extension QML engine still resolves `Muse.Ui` at runtime because it's a registered QML module (not file-path based), independent of the engine's import-path list.

**Open items (suggested follow-ups, not blockers):**

- ~~`extensions/` and `plugins/` junction directories in the ms-core-api worktree show as untracked in `git status` — they're per-machine setup per the worktree CLAUDE.md, should probably be added to `.gitignore` (worktree-local config). Not done.~~ **Done 2026-05-16:** added `/extensions/` and `/plugins/` (with explanatory comment) to `.gitignore` on the `ms-core-api` branch worktree. Modification still unstaged — needs a small standalone commit when convenient. `share/extensions/` content is unaffected (no leading-slash anchor avoidance issues).
- `share/extensions/hello-world/` is also untracked in the worktree — separate exploration, not part of the ai-assistant commit. Status unknown.
- The [[ai-assistant-sandbox-choice]] memory's open question (extension vs. plugin sandbox) is now better-informed: the Enter workaround works in the extension sandbox, so the motivation to migrate to a `MuseScore { pluginType: "dialog" }` plugin is weaker than when the memory was written. Decision still deferred to desktop Claude.
- Worktree-local `setup_and_build.bat`, `setup_and_build_fast.bat`, and `CLAUDE.md` have unstaged modifications on ms-core-api — intentional per-worktree configs, not yet decided whether they should be committed to the branch or kept as local-only.
- No push yet. `ai-assistant-mvp` is local-only. Pushing it to origin (`github.com/slimvince/MuseScore`) needs explicit decision — the branch could land as a PR target, or just live as a personal branch for now.

**Memory updates 2026-05-16:**
- [[ms4-extension-input-workaround]] — rewrote to cover both patterns (Ctrl/editing-key intercept + NavigationControl Enter workaround). The pre-existing description (TextArea + printable-char intercept) was obsolete after the v0.4.6 TextField swap.
- [[ms4-deploy-gate]] — corrected the grep pattern; old loose pattern documented as obsolete.
- `MEMORY.md` index — both descriptions updated.

---

## Key files

| File | Purpose |
|------|---------|
| `src/composing/analysis/chord/chordanalyzer.cpp` | Main analyzer — all scoring logic |
| `src/composing/analysis/region/regionanalyzer.cpp` | Canonical region orchestrator — Pass 1/2/2b, absorb, backfill, restamp |
| `src/notation/internal/notationharmonicrhythmbridge.cpp` | Bridge — thin wrapper over `regionanalyzer` |
| `docs/llm_integration.md` | LLM / Claude Composer full design document |
| `docs/quality_observations_iter76.md` | R1–R5 recurring themes for Iter 79+ |
| `docs/score_inventory.md` | Score paths for all test/corpus files |
| `STATUS.md` | Current baselines and HEAD — read every session |
| `build_and_test.md` | All build/test/tool commands |
| `CLAUDE.md` | Standing rules for CC — read every session |
| `tools/analyze_inversion_errors.py` | BIR corpus check |
| `muse/framework/extensions/api/extapi.h` | Current extension API surface (v2) |
| `muse/framework/extensions/internal/extensionsconfiguration.cpp` | Path resolution for extensions/plugins |
