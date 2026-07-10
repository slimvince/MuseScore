# The Premise Gate — Ponder-Point 2 Resolution: Why We Still Get Surprises

> **RATIFIED by the user, 2026-07-10 (Cowork, session 36).** Resolves PONDER-POINT 2
> (`cowork_handoff.md` entry point, user verbatim: *"Start with reasoning why we STILL get
> surprises... What needs to change in our way of working to once and for all stop being
> surprised?"*). Outcome: **CLAUDE.md principles #17 (the Premise Gate), #18 (unverified
> causal premises FORBIDDEN — Class A), #19 (unestablished instruments FORBIDDEN — Class B),
> plus the surprise-scope rule** (surprises allowed in explorational/ignorance-elimination
> runs; NOT allowed when building actual inference code). This doc is the evidence and the
> diagnosis behind that ratification.

## 1. The evidence — the documented surprise inventory

Seven surprises compiled from the repo's own provenance docs (each verifiable at the cited
source; the two most load-bearing claims re-verified at source this session).

### Class A — an unverified causal premise carried the design's full load

**A1 — the F-B fine-grain override (net-harmful −756).** Designed on the stated premise
"a fitted θ accounts for the incumbent's missing progression term"
(`cowork_fb_redesign_design.md:72`, echoing `cowork_layer5_function_design.md` §15-2) —
a causal claim about our own system, checkable against existing data, never checked.
Measured: 1043 fires → **53 corrections / 809 harms**; correctness **uncorrelated** with both
incumbent confidence C and contradiction strength S (§2.2–§2.4); harm *highest* (80.8 %) at
highest L4 confidence, so the only θ lever pushes the wrong way; disabling recovers **+756**
net-correct roots. Mechanism: `plausibility` rewards 4th/5th root motion regardless of the
vertical fact (576/1043 fires, ~82 % vertically wrong). Root cause per §3.D-2/§4: fired on a
population never filtered for genuine key↔chord coupling.

**A2 — the joint key↔chord step (barely pays; fire-rate 10× below the proxy).** Designed as
"the biggest precision lever (#4)" (`cowork_joint_key_chord_design.md`); the ~13.5 %
`decideJointKey` `coupled` **structural proxy was accepted as the fire-rate estimate**.
Measured (`cc_engage_stage3_joint_measure_report.md`): behavioral fire-rate **1.4–1.5 %**;
net +9/+3/+10 regions = **+0.05–0.16 pp**, harm 75–90 % of correction, oracle ceiling +0.6 pp,
coupled-minority net 0/+5/−2 (n=16/15/11). Root cause (report §4): the carried key
alternatives are **diatonic-collection siblings**, so the chord scorer's only key-dependent
terms barely move — the chord axis is almost always key-stable. **This was desk-derivable at
design time** from the scorer's own term structure plus elementary theory (relative
major/minor share the collection); nobody asked "which term moves, by how much?" before the
probe was built. (The design *did* honestly flag the magnitude as owed-2/unmeasured — which is
why arc #12 records "no new #3 surprise, a sharpening"; the proxy→fire-rate substitution is
the Class-A element.)

**A3 — the gate-insulation hypothesis (falsified).** The measurement-pipeline audit predicted
"the 13/7 gate does NOT move (already clean)" — a one-sided logical argument that checked the
admission path but not the false-negative path. It moved: **13→57 / 7→23**
(`cc_metric_rebaseline_report.md` §5: the P1/P2 parser bugs had pushed corrupted-root cases
into the discarded `all_differ` bucket).

### Class B — the instrument was trusted, not established

**B1 — the batch BIR gate undercount (~15–56×).** The cross-barline region unit was assumed to
measure user-visible per-onset root error; nobody derived what the unit actually measures.
Measured: per-beat root error ~7× higher at section granularity (`cc_stage2_2_ab_dossier.md`
§3.2/§3.5); the robust-unit re-derivation put the undercount at ~15–56× (a music21-filtered
reachable corner — `cc_stage5_r10b_ratification_report.md` block (C)). Resolved by the R10-b
robust-unit stop.

**B2 — the GT-parser bugs.** The corpus was treated as "known accurate" (#9) by assumption:
`dcml_parser` mis-rooted 877/880 applied-chord rows (`V/vi` rooted in the local key) and
minor-key `viio`/`vio` at the wrong degree — the ground truth itself was wrong until
oracle-cross-checked against music21 `RomanNumeral` (100 % on gate cases)
(`cc_metric_rebaseline_report.md` §1).

**B3 — the 68.19/64.52/67.77 key-column entry error.** Hand-transcribed figures ratified as
baselines; no re-run reproduces them. Caught at R10-b only by byte-identity reasoning
(identical `.ours.json` + unchanged key-path code cannot move a figure); corrected to the
reproducible 68.13/64.43/67.50 (`cc_stage5_r10b_ratification_report.md` Task 1b).

### Class C — local change, system-level interaction ignorance (CLOSED by mechanism)

**C1 — B1/B2×4/B3 template dead-ends** (`docs/scoring_model.md` intro, §8, §9): mMaj7
leading-tone ambiguity + a silent stack-buffer overrun; aug7 over-fire flipping Schumann/Corelli
snapshots; dim7 template bypassing the rotation selector. **These stopped recurring once the
lessons became mechanical constraints** (`kTemplateCount` compiler-enforced sizing; the §9
checklist) — the existence proof that converting a surprise class into a structural constraint
kills it.

### The in-repo counter-examples (simulate-first worked)

- **Cadence-precision investigation** (`cc_cadence_precision_investigation_dossier.md`) —
  derive-and-SIMULATE only: clean NEGATIVE at simulation cost, no build, no downstream surprise.
- **Gate-retirement dry-run dossier** (`cc_stage3_4i_dossier.md`) — measured the design's
  hypotheses instead of executing them.

Where we simulated first, the surprise arrived early and cheap; where we designed-then-built
(F-B) or designed-then-probed (joint step), late and expensive. Our own history contains the A/B.

## 2. The diagnosis — the user's four questions answered

**Are we not clever enough? No — the evidence is in the timing.** Every post-hoc root cause
(collection siblings; plausibility-rewards-4th/5th; the false-negative path) was derived
quickly and correctly *once measured*, from information available at design time. The
capability was present; the process applied it after building instead of before. An
epistemic-process failure, not a capability failure.

**Are we guessing? Yes — in one specific, repeatable way.** The designs are rigorous
everywhere *except at the single point where they assert the mechanism will help*. There,
plausible-mechanism reasoning ("progression tidying should fix roots") substituted for
quantitative reasoning ("how often, how big, in which population, via which terms"). Every
Class-A surprise is an unquantified magnitude or an unvalidated proxy. Beneath it a #2
failure: the specific research answering "does progression evidence beat vertical evidence on
root identity?" existed (Korzeniowski/Widmer; Vuvan — progression weak, bass/spelling
load-bearing) and was found *after* F-B failed, not before it was designed.

**Have we desktop-tested / dry-run / simulated? Almost never — and the exceptions prove the
point** (§1, counter-examples). The standing loop was design → build/probe → measure →
surprise; the simulate step existed only ad hoc.

**What must change?** Surprises cannot go to zero — the residual is genuine domain
uncertainty, and #3 read as "zero surprises ever" would forbid learning anything. The
achievable goal: **every surprise is caught at the cheapest possible stage, and only ever
occurs at a point explicitly labeled ASSUMPTION beforehand.** Measure-before-build (arc #12)
already moved the joint-step surprise from post-build to pre-build; the Premise Gate moves the
catch one stage earlier still.

## 3. The ratified rules (now CLAUDE.md #17–#19 + scope)

**#17 The Premise Gate** — before any inference-affecting design is built or probed:
(a) premise ledger, every load-bearing causal claim labeled FACT / THEORY / ASSUMPTION with
citation; (b) a written quantitative prediction per assumption, recorded before measuring —
no prediction, no build; (c) a desk simulation by hand through the intended architecture on
3–5 real corpus cases from the known failing sets; (d) every proxy→target link is itself a
ledger premise; (e) every insulation claim enumerates its false-negative path; (f) no
hand-transcribed measurement numbers — generated artifacts only.

**#18 Unverified causal premises FORBIDDEN (Class A).** No design carries load on a causal
claim about our own system or data that is checkable but unchecked.

**#19 Unestablished instruments FORBIDDEN (Class B).** An instrument, corpus, gate, or
recorded figure is trusted only after being positively established (oracle cross-check,
derivation of what the unit measures, reproduce-check) — never merely unfalsified.

**Scope of surprise.** Surprises are allowed in **explorational runs** whose purpose is to
eliminate ignorance (#5 fact-finding). They are **NOT allowed when building actual inference
code** — there a surprise is a STOP (#13) and evidence the Premise Gate was not satisfied.

**The funnel** (composing #17 with the ratified MEASURE-BEFORE-BUILD gate):
**desk-simulate (hours) → read-only probe (a session) → build (an arc)** — each stage kills
bad premises before the next pays for them.

## 4. Immediate application

The next owed measurement — **does the REBUILT path (decoder carry + intended selection) beat
LEGACY against the DCML ground truth?** (the go/no-go on the whole engagement, before E4) —
is the first work item to run under #17: its instruction must open with the premise ledger,
written predictions, and a desk simulation over known failing cases before the probe is
specified. PONDER-POINT 1 (reopening the joint (key,chord) ranking framing) likewise: the
question "was the near-zero benefit an artifact of key-first-then-chord framing?" is itself a
Class-A premise check, and a desk simulation over the arc-#12 flip cases is the cheapest first
move.

*Cowork, 2026-07-10. Sources verified at: `cowork_fb_redesign_design.md`,
`cc_engage_stage3_joint_measure_report.md`, `cc_metric_rebaseline_report.md`,
`cc_stage2_2_ab_dossier.md`, `cc_stage5_r10b_ratification_report.md`,
`docs/scoring_model.md`, `cc_cadence_precision_investigation_dossier.md`,
`cc_stage3_4i_dossier.md`, `cowork_engage_arc_plan.md`, `cowork_handoff.md`.*
