# THE SUCCESSOR PLAN — reconstructing the specifications, built from two independent evaluations

> **STATUS: DRAFT FOR THE USER'S RATIFICATION. NO WORK BEGINS UNTIL THIS PLAN IS RULED.**
> Cowork, 2026-08-21, written at branch tip `3cfb220b1d` (parent `7d7a0e76f7`; `origin/master`
> at `891bacc5d2`). It orders no act, touches no document, moves no candidacy, takes no ruling,
> allocates no finding number, and is authority for nothing. It is the successor to the four plan
> versions of 2026-08-19, which are withdrawn and preserved on disk (#12).
>
> **How it was built, so the provenance of every choice is checkable.** Under Ruling 3 of
> `cowork_rulings_2026_08_21_evaluation_brief_sitting.md`, this session booted normally, read the
> two independent evaluations of the four plan versions — `cc_report_plan_evaluation.md` (Claude
> Code, at commit `3cfb220b1d`, verified at the object) and
> `cowork_report_plan_evaluation_2026_08_21.md` (a separate Cowork session on a different model) —
> tabulated the sealed prediction against both BEFORE drafting a line
> (`cowork_prediction_tabulation_2026_08_21.md`, on disk), and only then opened the four versions,
> the earlier refute-only review (`cc_report_plan_challenge.md`) and its dispatch. Under Ruling 4,
> the earlier review's evidence enters below as LABELLED INPUT only — its DIRECT items cited, its
> SWEEP items marked UNESTABLISHED — never as a verdict.
>
> **The decision surface is §12.** Every choice this plan needs from the user is put there with
> its alternatives, each alternative's case for and against, the principle named, and a rating
> TOWARDS the ultimate objective and TOWARDS the guiding principles. Per the standing rule, this
> text is delivered for reading first; the choice questions are put separately, in a later turn.

---

## 0. Terms, re-explained from scratch before anything rests on them

- **The specifications** — the documents that state what the harmonic analysis should do and why.
  The canonical one is `ARCHITECTURE.md` (it wins every disagreement, decisions-register entry
  D-091); beside it sit `docs/scoring_model.md` and the per-layer and per-component design
  documents that `ARCHITECTURE.md` delegates to by name.
- **The pollution** — specification text that was written FROM the code rather than from music
  theory, published research or measurement. Until 2026-08-15 a standing rule ordered that the
  specification be corrected wherever it disagreed with the code; that rule was superseded, so the
  cause is stopped, but the text it produced is still in place. This is the diagnosis every plan
  version carries and both evaluations confirm at the primary source (`CLAUDE.md:1599-1619`).
- **The ruled six phases** — the governing work structure, ruled by the user on 2026-08-15
  (`cowork_rulings_2026_08_15_phase_definition_sitting.md` §2; their one home is
  `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3): **preparation** (the
  record made ready) → **the pilot** (the derivation method proved on one subject before it is
  trusted) → **the framework** (the architecture decided before the details: the decomposition,
  each unit's charter, the boundary contracts) → **the detail specifications** (every
  specification re-derived inside its charter, the outgoing text dispositioned) → **measurement
  design** (the measurement layer's own design content) → **the audit** (the code examined against
  the derived specifications). The fix plan follows the audit and is unchanged territory. Every
  phase closes with a recorded retrospective.
- **Derive blind, then compare (derivation-first)** — the ruled method: a deriving session writes
  what the analysis should do, with its defense, from independent sources, BEFORE it opens the
  current specification text or its history; then it opens them as untrusted sources and judges
  each difference. Ruled 2026-08-15 (the sitting record §6), superseding the earlier
  reconciliation shape; an ordering, not a prohibition on ever reading the current text.
- **Implementation-derived material** — our code, and anything whose content reflects what the
  code does: outputs, saved results, fitted tables, measured behaviour, documents describing the
  implementation, and which corpus runs fail. A deriving session may not read it.
- **Independent sources** — published research actually fetched and read, the user's ratified
  rulings (design intent, not implementation management), and musical scores annotated by others.
- **The fact-gate and the empirical findings ledger** — the ruled admission mechanism for our OWN
  experimental findings. The test: *does the fact survive the implementation being thrown away?*
  A fact that passes enters the ledger, approach-level and implementation-stripped, with its
  provenance, uncertainty and establishment status. The ledger is a ruled preparation output and
  **has not been built** (`cowork_curated_boot_list_draft_2026_08_19.md` §4).
- **The disposition discipline** — the ruled rule that every statement of an outgoing
  specification text reaches exactly ONE recorded fate — adopted / relocated (to the cross-layer
  transfer list) / quarantined (as an audit question) / discarded (under the worth test, with
  finding, date and reason) / historical — with completeness checked by arithmetic.
- **A statement** — one atomic rule of a derived specification, carrying the fields §7 fixes.
- **The unit** — the thing one derivation pass produces a statement set for. Its grain is a
  decision of this plan (§12, decision 2).
- **The frame** — the complete list of units, derived before any content work.
- **A factor** — one term in the formula the production engine maximizes. The engine scores every
  candidate reading of a piece (key, mode, chord, and where the chords change) by adding ten
  separate terms — how well the sounding pitches fit the chord, how well the bass fits, how likely
  this chord follows the previous one, how likely a harmony boundary falls here, and so on. Each
  term is a factor; the ten were ratified by the user on 2026-07-19
  (`cowork_joint_estimator_factorization.md:73-132`).
- **A decision** — one question the analysis must answer about the music, independent of how any
  engine is built: where one harmony ends and the next begins; which sounding tones belong to the
  chord; the root; the bass; the key in force; whether the key has changed or only leaned; the
  chord's function; the spelling; whether to abstain.
- **A placement test** — a test of whether the FRAME is complete. Real statements are taken from
  documents NOT used to build the frame and each is filed under a unit; a statement that fits
  nowhere is evidence the frame lacks a unit or a whole category of unit. It is run by the side
  that did not author the frame. It is distinct from an **establishment test** (principle #19),
  which asks whether a METHOD or TOOL can be trusted by running it on something whose answer is
  already known — decision 4 concerns establishment tests, decision 5 the placement test.
- **The ground-truth ceiling** — how well two human annotators agree on this repertoire, per axis;
  the quantity principle #21 demands and the literature does not hold (D-474); tracked at
  [[OI-179]], OPEN and GATING as an establishment obligation.
- **The preserved pre-restructuring version** — the tree at commit `b006dc15b5`, ruled the most
  valuable single untrusted source of the pre-pollution text (the sitting record §5).
- **The July screen** — `tools/audit/july_screen_report.md`, generated by
  `tools/audit/gen_july_screen.py`: a measurement of changed passages in the specifications,
  classified by whether each change's source is a fact read in the code. It exists; its period is
  bounded and its limits are declared at its own `:13`.
- **Guardrail** — a standing constraint on every pass of this plan, each aimed at a failure this
  project has actually recorded, the failure named beside it (§8).
- **A tell** — one short sentence the user reads at the end of every pass, which says whether the
  pass produced anything other than what a pass may produce.

---

## 1. What this plan is for, and the one thing the evaluations settled about its predecessors

**Purpose, unchanged from every version:** produce the first derived version of the
specifications — what the analysis should do and why — from independent sources, with what is
worth keeping salvaged from the current text, ratified per unit, written so each statement can
later be compared against the code. It serves maximum-precision inference (#4) the only way a
specification can: by letting a precision change be checked against a defensible statement
rather than guessed.

**What both evaluators established, independently and first.** The predecessors' METHOD is
right and their OBJECTS were wrong. Both evaluations, working blind to each other, reach the
same five method choices from the objective — derive before compare; declare the sources before
reading and fix them for the pass; test the frame adversarially by the side that did not author
it; prove the statement format before writing in it; budget with overrun as a stop — and both put
first the same object-level defect: the predecessors' document set was taken from a derivation
that answers a different question and excludes `ARCHITECTURE.md` by construction
(`tools/audit/decisions/home_classification.json`, 146 entries over 34 non-specification
documents; `DECISIONS.md:250`). Both also found that no version accounts for the text it
replaces: the grading ran from the derivation outward only, so anything in the old text the
derivation never approached was never looked at. This plan keeps the five method choices whole,
replaces the three objects — the unit, the document set, the trust measurement — and adds the
accounting.

**What this plan is NOT.** It is not a replacement for the ruled six phases. Every predecessor
asked whether it replaced or executed the ruled pilot; both evaluators found the collision wider
than one phase (the predecessors' Phase A substitutes for the framework phase; their Phase B is
the detail-specification phase). This plan is written as an EXECUTION of the ruled pilot,
framework and detail-specification phases, situated against the ruled text at each step, and
where an evaluator found a ruled rule wrong, that is put to the user at §12 as a question about
the rule — never silently departed from.

---

## 2. The facts this plan rests on — each checked at its object, with its checker named

| fact | where, and by whom it was established |
|---|---|
| The superseded truth-half of the three-phase rule is preserved at `CLAUDE.md:1613-1619` and the replacement rule — a specification/code disagreement is evidence reserved for the audit — stands at `:1599-1601` | both evaluators, at the file; this session, at the file |
| The delegation-bar home population is 146 entries across 34 documents and excludes `ARCHITECTURE.md` and `CLAUDE.md` by construction (`DECISIONS.md:250`) | both evaluators, at `home_classification.json`; this session at `DECISIONS.md:250` |
| `ARCHITECTURE.md` is 532,289 bytes and `docs/scoring_model.md` 127,593 at the tip; at `b006dc15b5` they are 383,785 and 82,528 | CC, `git ls-tree -l` at explicit hashes (exact object sizes, no uncertainty) |
| The July screen exists and takes the specifications' provenance as its subject, per document (`tools/audit/july_screen_report.md:17-19, 24-29`) — the predecessors' fact row that no such artifact exists is false at the object | CC, at the file; **this session has not opened it** and carries it as CC's finding |
| The recorded dead ends of `docs/scoring_model.md` §8 are LEGACY-scoped and disclaim use against a rebuilt layer (`:1369-1373, 1410-1411`); some entries nonetheless carry facts about the music that survive the implementation (`:1396, 1434-1435`) | both evaluators, at the file |
| The ratified factorization (`cowork_joint_estimator_factorization.md`, user-ratified 2026-07-19) states what is jointly chosen, ten factors with form, table and research provenance (`:73-132`), eight premises with their false-negative paths (`:134-145`), and five corpus traces with recorded outcomes (`:196-203`) | CC, at the file |
| The predecessors' fact row "677 entries" is a pinned, historical value (`tools/audit/gen_decisions_filter.py:131`); the rendered index publishes 474 (`DECISIONS.md:212`) | CC, at the artifact; this session at `DECISIONS.md:212` |
| [[OI-179]] is in `gating_ids` at `tools/audit/nongating_apparatus_rows.json` | both evaluators; this session, 2026-08-21 |
| The empirical findings ledger is not built | the boot-list draft §4; both evaluators |
| The predecessors lost load-bearing text between versions with nothing recording the loss: v1's ten named-failure clauses, v1's parking clause on the source freeze, v2's unit-shape correction with its ratified grounding, v2's governing correction, three guardrails' operative second clauses at v4, and v1's principle that the unit is derived from the domain | both evaluators at the files; this session at the files |

**Carried as UNESTABLISHED (Ruling 4; #19), not as fact — the earlier review's SWEEP items that
neither evaluation re-derived:** that the committed failing-run artifact cannot attribute a run
to a unit (CC did not reach it; the Cowork evaluator reached its consequence from feasibility);
that the annotation schema records conclusions and not decisions (neither opened the schema);
the deletion-history cost measurement (229 commits, 15,483 deleted lines — neither re-measured);
and the five-sub-field falsification form reached by tracing statements into code (neither
traced). They enter this plan only where marked, and the plan does not depend on them.

**Owed dispositions that bear on the ANALYSIS, surfaced and not this plan's to fix:** three
source files declare themselves DORMANT against a live default (the earlier review's finding (1),
re-derived by the 2026-08-21 Cowork session at five coordinates); and `CLAUDE.md` #21 routes the
ceiling commissioning through a superseded phase numbering with no pointer to the remap. Both
evaluators read #21 through the remap without flagging the stale text. These are recorded here so
they are not lost; their rows are a later act.

---

## 3. Scope

**In scope:** the specification of the analysis — reconstructed unit by unit, ratified per unit,
written in the form of §7, inside the ruled pilot, framework and detail-specification phases; the
measurement layer's design content at the ruled measurement-design stage.

**Out of scope, named so no session drifts into them:** repairing the existing documents in
place; recovering the provenance of any sentence; classifying or repairing the decisions
register; changing any code; running any build, test or guard; the archiving wave except where
the ruled pruning plan already orders it; the open-items register except the ruled remapping
inside the disposition discipline; the phase-1 finish line, which describes a superseded
programme; the delta comparison against the code, which is the audit phase and is not
authorized here.

---

## 4. Step zero — measure the founding premise before spending against it

The predecessors declared that they "do not measure how polluted the specifications are and do
not need to." Both evaluators reject that: "the specifications are polluted by the
implementation" is a checkable causal claim about our own data, and principle #18 forbids
carrying load on a checkable-but-unchecked claim. CC adds that the measurement already exists in
bounded form — the July screen — and that v4's reading-depth inputs need it twice.

**The act:** the July screen's period is widened to cover the whole candidate document set of §5,
its method untouched, and its per-document distribution published. **This is a preparation-phase
act** (the ruled preparation phase mines the record with generated tools) and it is the one
mechanism this plan builds, stated as such so guardrail 3 is not breached silently.

**What it yields:** a per-document pollution distribution that feeds the reading depth at §6.3
and the ordering at §6.2.

**Failure signal, declared in advance:** if most passages land UNDETERMINED the premise is not
measurable, and that is a STOP to the user — not a licence to proceed as if it were measured.

The alternative — skip the measurement — is rated at §12, decision 7.

---

## 5. The document set — derived from what specifies the analysis, never from the register

**Dropped, on both evaluators' finding:** the home population admitted by the delegation bar. It
answers *where does a decisions-register entry whose home is not a specification live*, not *which
documents specify the analysis*; it excludes the canonical specification by construction and is
being drained by the ruled re-homing route (`CLAUDE.md:582-603`).

**Derived instead, in three limbs, each mechanical and each checkable by reading:**

1. **The canonical specification**: `ARCHITECTURE.md` — the analysis layers' sections (filed as
   children of §3.3, a section about where files live; the frame is NOT taken from these
   headings), the joint estimator's standing-rules section above the table of contents (absent
   from it), and document governance.
2. **Every document `ARCHITECTURE.md` delegates to in an ADMITTED form** under the ruled
   delegation-form rule (`CLAUDE.md` decisions-register rule (i): an explicit delegation clause or
   a named home with sections; never a bare citation or a glob). The member list is produced by
   reading the delegations, with each delegating line quoted.
3. **`docs/scoring_model.md`** — the ruled pilot subject, with its own banner's declaration that
   its mechanism content describes a scorer dormant on both production surfaces carried as a
   property of the document.

**Excluded, with the reason:** `CLAUDE.md`'s gate block and grading conventions are measurement
content and belong to the measurement-design stage, not the analysis derivation; `DEFECT_TYPES.md`
is a catalog of engineering and method defects and carries almost no musical knowledge (its type
column may serve a deriving session; its founding-instance and signature columns are
implementation descriptions — the Cowork evaluator's finding on the boot-list draft's member (6));
`OPEN_ITEMS.md`, the handover records, dispatches and coding-side reports are process record and
enter only as mining inputs behind the fact-gate.

**Per document, three properties travel with it into every later step:** its pollution
distribution from step zero; whether its subject is LIVE or DORMANT on the production surfaces
(declared by its own banner or by the joint estimator's standing rules); and the establishment
status of its content where the document declares one (`docs/scoring_model.md` §8 declares every
hand-set magnitude UNFALSIFIED, NOT ESTABLISHED). These are the two axes the earlier review found
missing from v4's depth inputs (re-found in part by the Cowork evaluator at its C1 and R1), and
the pollution axis CC found missing.

---

## 6. The phases as this plan executes them

### 6.1 The PILOT — the method proved before it is trusted (ruled phase two)

**Subject:** as ruled, `docs/scoring_model.md`; whether it stays the subject is decision 3 at
§12, because both evaluators reached — one explicitly, one in substance — a preference for a
unit of the production model, and the record's own grounds for the ruled subject are real.

**Prerequisite, with a declared hole:** the ruled curated boot list (drafted 2026-08-19, ruled
2026-08-21 for the two evaluations only — its ruling for derivation sessions is still owed); and
the empirical findings ledger, which is not built. Whether the pilot waits for the ledger is
decision 8.

**What the pilot must return — the three establishment tests, not one.** The predecessors
measured the method by its withdrawal rate alone, which is one-sided: a derivation that produces
little is never withdrawn. Both evaluators found the predecessors' trust measurement — collisions
with the recorded dead ends — unsound at the object, because the dead ends are LEGACY-scoped and
have a different subject from a blind derivation. The pilot therefore returns:

- **(a) the withdrawal rate at the record check** — kept, as one signal among three, with the
  admission test of §6.4 deciding which dead ends may withdraw a statement;
- **(b) the format test** — five statements written in the §7 form by the deriving side and
  judged from the comparison side for whether the falsification field is returnable without
  interpretation; **the sample includes a probabilistic factor form and a conditional-independence
  premise** (CC's finding: the five kinds the predecessors chose omit the two dominant kinds in the
  production layer's ratified specification, so the test would pass on the tractable kinds and
  leave the hard kind untested);
- **(c) the held-out test** — the deriving side derives one decision for which a user-ratified
  design-intent ruling exists, with that ruling WITHHELD from it; if the blind derivation
  reproduces the ruled intent, or produces a defended alternative the user would rank beside it,
  the method is positively established (#19); if it produces nothing, the ordering is refuted on
  the refuting side. The Cowork evaluator names the evidence-ranking decision
  (`ARCHITECTURE.md:394-402`, user-ruled 2026-08-11) as the oracle; CC names the five corpus traces
  of the ratified factorization (`:196-203`) as a trust test with a recorded answer. Both are
  carried as candidates; which runs is decision 4.

**Sizing record, as ruled:** time per statement, statements per unit, share withdrawn, share
needing a user ruling, share whose falsification field could not be written, and a noise
measurement — which boot-list inputs the session actually consulted. The budget for every later
unit is set from these; no value is invented here.

**Output:** a proposal per difference, never a rewrite; the derived text QUARANTINED as
provisional until the framework rules the charters (ruled).

### 6.2 The FRAMEWORK — the frame derived from the domain, tested adversarially, ratified (ruled phase three)

**The principle restored from v1, refuted in neither evaluation and dropped at v2:** the unit is
derived from the domain, not inherited from the documents being replaced. v1's authored list of
ten questions was rightly withdrawn as an assumption; its principle was not refuted.

**The frame's two levels, on which both evaluators converge.**

- **Level one — one document, the joint objective:** what the decode maximizes, over what state
  (tonic × mode × scale-degree chord, with segmentation a modelled variable), which factors, under
  which evidence ranking, what is committed and what is carried as alternatives, what is
  abstained. This is the ruled framework phase's charters and boundary contracts in the shape the
  production model actually has: in a joint model there is no dependency order between questions —
  that is what *joint* means — so the decomposition is the structure of the objective, and the
  surrounding contracts (the fit event, the held-out protocol, the capacity budget, the licence
  pool, the idiom split, the tie-break, the key-axis abstention policy) attach to the estimator as
  a whole and have a home here that neither v1's questions nor v2–v4's document sections could
  hold.
- **Level two — per-unit statement sets INSIDE level one,** each required to be coherent with the
  objective. The grain of the unit — a factor of the model (CC) or a decision the analysis makes
  (the Cowork evaluator) — is decision 2.

**How the unit list is derived (the Cowork evaluator's three-source derivation, with the ratified
factorization added as the fourth because it is a user-ratified design-intent ruling and
therefore admissible to a blind session):** (i) the ground-truth annotation schema — what is
graded; (ii) the state and factor spaces of the published models this project rests on, fetched
and read; (iii) theory — what a harmonic analysis of this repertoire consists of, including what
annotators do not write down; (iv) the ratified factorization's variables and factors. A unit
present in one source and absent from the others is a finding about the frame, never dropped.
The earlier review's SWEEP claim that the schema enumerates conclusions rather than decisions is
why (i) alone is insufficient; it is carried UNESTABLISHED and source (i) is not given more
weight than the others.

**What the current headings and the deleted headings become:** NOT the frame's source. They are
demoted to a TEST POPULATION for the placement test below — every current heading and every
heading ever deleted from the document set is a statement to be placed — which keeps the one
real value of the history walk (a removed section is a dropped perspective) without inheriting
the structure or paying the history walk's unmeasured cost up front.

**The placement test, run adversarially by the side that did not author the frame.** A declared
sample of statements drawn from OUTSIDE the frame — ruling records, decision surfaces, dossiers,
the DEFERRED decisions-register entries, the evidence inventory, the declared dormancies, and the heading
population above — each placed; the brief is *place these; report every one you cannot*, never
*does this frame look complete?* **Every unplaceable statement is a finding about the frame.**
The predecessors' bright line (more than ten of sixty unplaceable → the wrong frame) is dropped:
both evaluators found the sample size and threshold undefended, the Cowork evaluator computed
that at sixty the test separates a badly wrong frame from a sound one and cannot separate a
mildly incomplete one, and the record's own founding instance was found by placing ONE statement.
What replaces it is decision 5.

**The format test** (§6.1 (b)) is run here if the pilot did not already discharge it.

**Output:** the ratified frame with its derivation, its exclusions, every unplaceable statement
and the user's ruling on each; the cross-layer transfer list OPENED (ruled); per design point, the
candidates from both source kinds with establishment status and at most one chosen or NONE
(ruled, method-directions §2.3).

### 6.3 The DETAIL SPECIFICATIONS — per unit, inside the ratified frame (ruled phase four)

Executed in this order and no other, per unit.

**Step one — declare the sources and the reading depth; show both before reading.** The
independent sources for this unit (the research to be fetched, the annotated scores, the ratified
design-intent rulings whose subject it is, the ledger's admitted facts); and the untrusted sources
to be opened AFTER derivation — the passages of every document-set member that cover the unit,
the same passages at the preserved pre-restructuring version `b006dc15b5`, the deletions from
those passages to the declared depth, the July screen's examination set where it touches the
unit, and the `docs/scoring_model.md` §8 entries that pass the admission test of §6.4.
**Code sites and failing runs are NOT sources of a deriving pass** — the ruled constraint
(`…surface…:250-252`), and on the merits: the annotated scores are uncontaminated, which runs
fail is a fact about our code, and failure identities enter the audit's question feed (the
Cowork evaluator's R2). **The reading depth** is declared per unit from the properties that
travel with the documents (§5) and the dependency structure of the objective, reported with its
inputs; it decides how much history is opened, over a source list that does not depend on it (the
Cowork evaluator's R7: the predecessors' density axis was a function of the tier it was meant to
choose). A unit that opens and proves to need more depth is a STOP and a request to raise it,
never a silent expansion. The user may add or remove members; the list and the depth are then
fixed for the pass (guardrail 4).

**Step two — derive blind.** Write what the unit's statements should be, from the independent
sources only, every statement carrying its defense in the same breath, every load-bearing claim
labelled FACT / THEORY / CONJECTURE, an unfetched source yielding no statement (the
theory-grounding corollary, `CLAUDE.md:268-278`). What cannot be settled is written as an open
question, never filled with the most plausible reading.

**Step three — open the untrusted sources and grade the derivation.** The closed outcome set,
kept: **confirms** → stands, cited · **contradicts** → an open question, both readings stated ·
**adds** → salvage, admitted with its own defense · **records a dead end the derivation walked
into** → withdrawn, **only where the dead end passes the admission test of §6.4**. An
implementation description met in the current text is QUARANTINED as an audit question (ruled),
never absorbed; a statement whose only support is the code is marked UNSUPPORTED (kept from
every version — it is the ruled quarantine in statement form).

**Step four — dispose of the outgoing text from the outgoing text's side.** This is the step no
predecessor had and both evaluators put among their largest findings. Every statement of the
covered passages reaches exactly one of the five ruled fates — adopted / relocated / quarantined
/ discarded (worth test; finding, date, reason) / historical — with completeness checked by
arithmetic. The re-bannering of the old passages is the OUTCOME of this step, never the act.

**Step five — the assembly check.** The unit's statements are checked against the level-one
objective and against every already-ratified unit for joint coherence (the Cowork evaluator's M6;
the earlier review's DIRECT finding that the record carries a live, declared, unsettled tension
between the key-axis commit rule and the abstention rule at `ARCHITECTURE.md:331-338`, which a
per-unit method with closed units would pass straight through). A contradiction found here is an
open question to the ratification, never resolved by the session.

**Step six — the adversarial read, by the side that did not derive, in BOTH polarities.** Brief:
what survives, what falls, what cannot be decided on the declared sources — find the defense that
does not support its statement, the statement whose only support is the implementation, the
falsification field that cannot be checked, AND say which statements are sound with grounds. The
predecessors' refute-only brief ("a review returning 'sound' is not a completed review") is
dropped: a review forbidden one class of verdict returns a sample of refutations with no
denominator, which is the defect the two evaluations were commissioned to repair. The attack list
itself — load-bearing assumptions each with its refutation condition — is kept.

**Step seven — ratification.** One surface: the statements, the open questions, the sources read
and the depth, the exclusions, the disposition record with its arithmetic, the assembly check,
and what the adversarial read refuted and confirmed. No question in the turn that delivers it.

**Step eight — land it** under the declared end state (§9).

### 6.4 The admission test for a recorded dead end, and the ledger it implies

A recorded dead end may withdraw a derived statement **only if** it passes the fact-gate's ruled
test — *does the fact survive the implementation being thrown away?* — and is approach-level. A
prohibition on re-attempting a specific mechanism of the dormant scorer does not; a fact about the
music or the corpus ("an absent root does not mean a wrong reading, corpus-wide";
`docs/scoring_model.md:1396`) does. Both evaluators reached this separately (CC §2.2; the Cowork
evaluator R3/M1), and both identified the ruled empirical findings ledger as the mechanism built
for exactly this material. The ledger is not built. Decision 8 asks whether it is built before
the pilot or whether the pilot applies the test by hand with the ledger's entry shape and its
admissions seeding the ledger when built.

### 6.5 The MEASUREMENT-DESIGN stage (ruled phase five) and the ground-truth ceiling

The measurement layer's design content — metric definitions, grading conventions, what counts as
ground truth — is derived here, after the detail specifications, as ruled. The ceiling
measurement's DESIGN opens here, desk simulation first, as the ruled remap places it
(`…surface…:318-321`).

The predecessors' §7 — that the ceiling "runs beside the plan", "is computable from data that
already exists" and "is independent of this plan" — is dropped on both evaluators' finding: the
record it cites says the opposite of "computable" (`CLAUDE.md:184-193`: neither computable route
is established, neither checked at its data, the within-repertoire leg a PROXY between annotation
traditions, and the choice a design decision). What survives is the predecessors' correct point:
until the ceiling exists, no residual on any axis can be interpreted (`CLAUDE.md:142-145`).
**The two evaluators disagree on whether the ruled placement is right** — CC says placing it fifth
of six leaves every earlier measurement uninterpretable; the Cowork evaluator says the ruling's
ground is sound because what-is-ground-truth is itself a design decision. That disagreement is
decision 10, and the plan records one fact that bears on it: under the ruled order no residual
is interpreted before the audit, and the audit comes AFTER measurement design, so the cost CC
names bites only if a measurement is read before the audit — which the ruled order forbids.

### 6.6 The AUDIT — not authorized here

Every divergence found later between a statement and the code is evidence reserved for the
audit, a licence to change neither side. This plan does not authorize that comparison; it is the
ruled sixth phase under its own ruling. The quarantined audit questions, the failure identities
and the falsification fields of §7 are what this plan hands it.

### 6.7 The retrospective, at the close of each phase

Ruled 2026-08-15 and absent from every predecessor (both evaluators, as CONFORMANCE, each saying
the rule is right). Each phase of this plan — the pilot, the framework, the detail
specifications, measurement design — closes with a recorded retrospective: what the phase taught,
with evidence, routed to its home (a way-of-working lesson → a proposed amendment to the phase
definitions; a design lesson → the ledger through the fact-gate or a framework amendment
proposal; a process antipattern → the constraints), proposing and never applying. It lands on
disk and is named in the handover.

---

## 7. The form of every statement — six fields, one rule per statement

Atomic, because a paragraph cannot be compared against code. The predecessors' five fields plus
the one both evaluators found missing in different words:

1. **The statement** — what the analysis must do, or what it must be able to do (the
   enablement class restored from v2: a requirement that the implementation not preclude
   something, grounded in the fact-publication corollary, `CLAUDE.md:239-252`).
2. **The defense** — the music theory, the published research fetched and read, or the
   measurement that decides it, each load-bearing claim labelled FACT / THEORY / CONJECTURE.
   *"Because the implementation does this"* is not a defense; a statement supported only by the
   code is marked UNSUPPORTED.
3. **The source class** — derived · salvaged · measured — and, for a measured statement, its
   uncertainty (#24) and its establishment status (#19); a measured defense is read under the
   ceiling caveat at #21 until the ceiling exists.
4. **The status** — settled · open.
5. **The premise it rests on, and that premise's false-negative path** (#17(a), #17(e)) — the
   field CC found the predecessors' form had no place for: the production layer's ratified
   specification carries eight modelling premises each with the path that would break it, and a
   form that cannot hold them would silently drop the premise ledger of the one layer that has
   one.
6. **What would falsify it** — in code where the statement is behavioural; **in the residual**
   where it is a modelling premise, because a premise has no code site to check. For the
   behavioural half, the sub-fields the earlier review proposed from the comparison side — the
   ARM (joint / legacy-live / legacy-dormant), a named SITE, the OBSERVABLE read, the DECISION RULE
   over it, and the named near-miss it is NOT falsified by — are carried as **UNESTABLISHED
   input** (the earlier review's five probes were sweep-borrowed and neither evaluation traced
   statements into code); the format test of §6.1 (b) is where they are tested, not assumed.

A statement that cannot carry field six is marked as unverifiable rather than left to look
checkable (kept from every version).

---

## 8. The guardrails — restored to their v1 form, each with its named failure, and two repaired

The failure is named so the guardrail cannot be softened into general advice (v1's own reason,
dropped at v2 and re-found by both evaluators as a loss).

1. **A pass produces specification statements, an open-questions list, a disposition record and
   a findings remark — nothing else.** No new tool, artifact, rule or numbered finding. *Stops:*
   fourteen preparation batches whose outputs were machinery for the next batch. *(Step zero's
   one widened generator is declared at §4 and is not a pass output.)*
2. **REPAIRED. A finding that bears on the analysis goes to the quarantined audit questions; a
   finding about the apparatus is rowed and lapses under the ruled lapse rule; everything else
   is discarded under the worth test with finding, date and reason.** The predecessors' "no
   numbers, no rows" collided with the open-items register's rules (c) and (e) and with D-641
   (both evaluators, as CONFORMANCE, each saying the rules are right), and it lost the one thing
   worth keeping — any record that the finding was made. *Stops:* a findings series that reached
   F88, each member acquiring an owner and a lifecycle.
3. **No mechanism is built during a pass.** What can only be checked by a tool is recorded as
   unchecked, with its reason. *Stops:* the establishment recursion.
4. **The sources and the depth are declared before reading and never extended mid-pass.
   Anything found outside them is written down as an input to a later unit, or parked on the
   cross-layer transfer list** (v1's parking clause, restored; it is the same function the ruled
   transfer list performs). *Stops:* the rabbit hole, every instance of which was individually
   justified. *Declared honestly:* that a pass read only what it declared is not verifiable after
   the fact; what IS verifiable is the ORDER — the derived statement and its defense land in one
   commit and the comparison in a later one, provable at content-addressed objects — and that
   ordering is what derivation-first requires.
5. **Every phase and every unit carries a declared budget; overrun is a stop, not a continue.
   The first unit at any grain carries a PROVISIONAL budget, declared as provisional, whose
   overrun is a stop that reports the measured cost** (the Cowork evaluator's R6: the
   predecessors' first unit ran with no budget). *Stops:* the absence of any cost ceiling on any
   act in this project's history.
6. **The done condition is written before the work starts.** *Stops:* a finish line that now
   describes a superseded programme.
7. **No ruling is taken during a pass; open questions accumulate to one ratification at the end.**
   *Stops:* the engine itself — return, rulings, dispatch, return.
8. **One file per unit, and no record about the record.** *Stops:* a batch of 77 written lines
   that generated about 1,500 lines describing itself.
9. **A ratified unit is closed; a later unit that bears on it produces an open question at the
   assembly check, and re-opening takes the user's word.** *Stops:* the same subjects re-litigated
   across four sittings.
10. **The frame is closed once ratified; an addition is the user's, never a session's.** *Stops:*
    a unit of work that generates more units.
11. **One tell, checked at the end of every pass, in one sentence:** *did this pass produce
    anything other than what guardrail 1 allows? If yes — name it.* Checked by the user reading
    one short thing, not by a guard. **If a session proposes building something to check these
    guardrails, that proposal is itself the tell firing.** Kept verbatim: the earlier review
    called this clause self-sealing; both independent evaluators rate it correct, on the ground
    that the recorded cause of the apparatus backlog is a mechanism that draws capacity
    indefinitely, so a guardrail checked by new apparatus reproduces the cause it was written
    against.

---

## 9. The end state, declared now — a bounded migration with a ruled terminus

Kept from v3 whole, and CC found it improves on the ruled pruning plan, whose archive-per-
specification rule cannot be executed as written for `ARCHITECTURE.md`, one file holding many
specifications. While the programme runs, the derived units accumulate as their own document and
`ARCHITECTURE.md` stands unedited — a declared #23 migration, not an oversight. As each unit is
ratified and its disposition record is complete, the passages it covers are marked superseded
with the former wording preserved in place (#12); nothing is deleted. The terminus is one
ratified replacement at which `ARCHITECTURE.md` becomes the new text or a pointer to it — ruled at
the START (decision 11), because a migration with no ruled terminus is how the last one ended.

---

## 10. Stop conditions

A pass halts and reports rather than continuing when: a declared source cannot be located; the
derivation and the record contradict on a point the pass cannot leave open; a budget — provisional
or set — is reached; the assembly check finds a contradiction with a ratified unit; a unit proves
to need more reading depth than declared; step zero's distribution is uninformative; the
placement test returns an unplaceable statement (reported as a finding, per decision 5); the pass
would have to build something, change code, or take a ruling to continue. A stop records what was
done, what was not, and that the remainder is untouched rather than half-worked.

---

## 11. Budget and the order of first acts

**Nothing is sized here that the record says cannot be sized before the pilot**
(`…surface…:564-574`). Step zero costs one working session on the ground that the generator
exists; it carries a stop-and-report threshold of one session, not an estimate. The pilot's cost
is unknown and that is the point of the pilot. Every later budget is set from the pilot's sizing
record, provisionally for the first unit at each grain.

**The order of first acts, once ruled:** (1) the next Claude Code dispatch lands at its Task 0 the
2026-08-21 records — the thirty-sixth handover block, the sitting record, the evaluation dispatch,
the brief, the boot list, the sealed prediction, both evaluation reports, the tabulation, and this
plan — and performs step zero; (2) the ledger decision (8) is executed; (3) the pilot opens under
its ruled definition with the subject decision 3 rules.

---

## 12. THE DECISIONS FOR THE USER — each with its alternatives, rated

Each alternative carries its case for and against with the principle named, and a rating towards
the ultimate objective (maximum-precision inference) and towards the guiding principles. The
recommendation is stated; the decision is the user's and is not pre-empted. Where the two
evaluators disagree, both positions are given.

**Decision 1 — The relation to the ruled six phases.**
*A — this plan EXECUTES the ruled pilot, framework and detail-specification phases (recommended).*
For: every collision both evaluators found becomes a question put here rather than a departure
taken silently; the ruled structure already holds the pieces the predecessors lacked (the
framework phase, the disposition discipline, the transfer list, the retrospective). Against: six
phases carry sequencing cost. Towards the objective: highest — the audit waits for a trustworthy
measurement tool, which is the eighteenth-stop lesson. Towards the principles: conforms.
*B — this plan REPLACES them.* For: fewer boundaries. Against: re-decides five things the user
ruled on 2026-08-15 without a ground either evaluator found; the collision the predecessors
under-declared by a factor of three. Towards the objective: lower. Towards the principles: #14's
spirit (deliberate, ratified change) breached.

**Decision 2 — What one unit is: the thing one derivation pass writes a statement set for.**
The two evaluators disagree, and the disagreement is this decision. (The terms *factor*,
*decision* and *frame* are defined in §0.)

*A — one unit = one FACTOR of the ratified ten-factor model; ten specifications (CC's
derivation).* For: every fitted value, every table and every code site belongs to exactly one
factor, so a specification per factor is directly comparable to the code; the ten factors are
terms of ONE sum, so writing them separately does not pretend they are independent of each other;
the independences the model does rest on are already written down with what would break each
(eight premises at `cowork_joint_estimator_factorization.md:134-145`). Against: the factors are the
structure of the CURRENT engine. If the derivation were to find that the engine should have a
term it lacks, or lack a term it has, a per-factor frame has no place for that — the frame would
inherit the very design derivation-first exists to re-derive. Towards the objective: high.
Towards the principles: #6 and #18 served; the decision-neutrality corollary strained, because
the existing design would shape the frame.

*B — one unit = one DECISION the analysis must make about the music, with the list derived from
three sources that owe nothing to our code — what the human annotators grade, what the published
models decide, what music theory says a harmonic analysis consists of (the Cowork evaluator's
derivation).* For: the list is derived, not inherited; it can hold things the current engine does
not model (what annotators never write down; abstention); it is v1's principle — the unit comes
from the domain, not from the documents being replaced — which no evaluator refuted. Against: a
decision does not map one-to-one onto a code site, so the later comparison against the code is
less mechanical; in a joint engine the decisions have no natural order, so the order must come
from the engine's objective anyway. Towards the objective: high. Towards the principles: the
decision-neutrality corollary and #18 served; #6 served if the assembly check of §6.3 holds.

*C — the plan does NOT fix the grain; the framework phase derives it (recommended).* The ruled
framework phase exists precisely to decide the decomposition before the details. So the
framework phase derives the unit list from FOUR sources — the three of alternative B, plus the
ratified ten-factor model, admissible because it is a user-ratified ruling — and whether the
resulting units are factors, decisions, or a reconciliation of the two (a decision served by two
factors; a factor serving two decisions) is the framework phase's first ratified finding, put to
the user then, with the evidence. For: the grain is decided where the ruled structure says it is
decided, from evidence, rather than in this plan in advance of it, by two evaluators who
disagree; neither inherited structure nor pure authorship dominates, because the model is one
source among four. Against: the pilot runs before the grain is ruled, so the pilot's subject must
be a unit under EITHER reading — the harmony-boundary question is both a decision and a factor,
which is why decision 3 offers it. Towards the objective: highest, because the grain is derived.
Towards the principles: #17(a) (the plan's own unit is not an assumption), #6 and #18 served.

**Decision 3 — The pilot's subject.**
*A — keep the ruled subject, `docs/scoring_model.md`.* For: ruled 2026-08-15 on stated grounds —
the hardest implementation-blind case, low boundary exposure, holder of the one changed passage
the July screen established as code-influenced; changing it is a ruling. Against: its own banner
declares its mechanism content dormant on both production surfaces, so a statement derived for it
is quarantined on arrival, and the sizing may not transfer (the Cowork evaluator's C1 — CANNOT
ESTABLISH, no recommendation under D-658). Towards the objective: medium — it proves the method
on the hardest case but on a dormant subject. Towards the principles: conforms; #19 served.
*B — move the pilot to the boundary/segmentation decision of the production model.* For: it has
published grounding, a real named failing case (`bwv10.7@36000`), and a measured cost of a
specification error (the length-bias finding); it is a unit under both grains of decision 2; the
held-out and trace tests of decision 4 both have an oracle there; both evaluators reached it. 
Against: it re-opens a ruling; it is not the hardest implementation-blind case, so the sizing may
be optimistic; its changed passages were not the fired one. Towards the objective: high — the
method is proved on a live subject whose statements will be kept. Towards the principles: #14's
spirit requires the change be ruled, which is what this decision is.
*C — both: the ruled subject for the sizing record it was ruled for, and the boundary decision as
the held-out method test of decision 4 (recommended).* For: keeps the ruling and its grounds;
adds the positive establishment the ruled pilot lacks; the two tests measure different things
(sizing on the hard case; method on a live unit). Against: two pilot units before the framework
opens, which is calendar. Towards the objective: highest — the method is established on a live
subject AND sized on the hard one. Towards the principles: #19 served twice; the pruning
direction (session context) paid once more.

**Decision 4 — The method's establishment test(s).**
*A — the withdrawal rate alone (the predecessors).* For: cheapest. Against: one-sided; a
derivation that produces little is never withdrawn. Towards the objective: low. Towards the
principles: #19 not met (merely unfalsified).
*B — the three tests of §6.1 — withdrawal rate, format test, held-out test against a withheld
user-ratified ruling — with CC's five recorded corpus traces as the held-out oracle's second arm
where the pilot unit is a factor of the factorization (recommended).* For: positive establishment
(#19); the traces share a subject with the derivation (what the analysis should do on real music),
which the dead-end collision test does not; the withheld ruling is recent, explicit and
user-worded. Against: cost — the held-out test is a pass of its own. Towards the objective:
highest. Towards the principles: #19, #17(b) (the prediction — the withheld ruling — exists before
the test runs).

**Decision 5 — What happens when the placement test (§0; §6.2) finds a statement that fits no
unit.** The predecessors said: fewer than eleven unplaceable out of a sample of sixty means the
frame is not wrong. The question is what replaces that line.
*A — keep "more than ten of sixty".* For: a bright line a session can apply. Against: undefended
(both evaluators); low power at sixty; contradicts the plan's own sentence that one unplaceable
statement is a finding; a difference of one inside sampling noise would decide a STOP (#24).
Towards the objective: low. Towards the principles: #24 breached.
*B — every unplaceable statement is a finding reported to the user with the sample's size and the
observed proportion and its uncertainty range; the user rules per finding whether the frame is
amended, and the frame's rebuild is the user's act (recommended).* For: the founding instance
(one placed example found the gap) is honoured; no invented value (#17(f), D-658); the user
decides the frame as guardrail 10 already says. Against: more rulings reach the user; no automatic
stop. Towards the objective: high. Towards the principles: #24, #12 served; the user's time is the
cost, which the record parks until sizing exists.
*C — no placement test.* Declined by both evaluators and every version; listed so the exclusion
is on record. Towards the objective: lowest — the category error the test exists against goes
undetected.

**Decision 6 — The document set.**
*A — derived from `ARCHITECTURE.md`'s admitted delegations plus `docs/scoring_model.md`, with the
three per-document properties of §5 (recommended).* For: answers the right question; mechanical
and checkable by quoting each delegating line; the ruled delegation-form rule already exists.
Against: depends on `ARCHITECTURE.md`'s delegations being complete, which is itself a finding
to record, not assume. Towards the objective: high. Towards the principles: #6, rule (i).
*B — a hand-listed set.* For: fast. Against: authored; the DT-26 scope-assumed-enumeration
shape. Towards the objective: lower. Towards the principles: #17(a) breached.

**Decision 7 — Step zero, the pollution measurement.**
*A — widen the July screen's period over the whole document set; method untouched (recommended).*
For: #18 — the founding premise is checkable and load-bearing; the generator exists and its
classes are ruled; it supplies the pollution axis the reading depth needs. Against: one mechanism
is run in a plan that otherwise builds none, and the screen's own limits (`:13`) bound what it
can show. Towards the objective: high. Towards the principles: #18, #5 served; guardrail 3
declared rather than breached.
*B — skip it, as every predecessor did.* For: nothing built. Against: the plan then carries load
on an unchecked causal claim about our own data, which #18 forbids outright. Towards the
objective: lower. Towards the principles: #18 breached.

**Decision 8 — The empirical findings ledger.**
*A — build the ledger (a ruled preparation output) before the pilot opens.* For: the pilot then
reads admitted facts from one home; the admission test of §6.4 is mechanical. Against: one more
preparation batch before any specification text exists — the shape v1's diagnosis (d) names.
Towards the objective: medium. Towards the principles: #6, #19 served; the pruning direction
strained.
*B — the pilot opens with the declared hole: the admission test is applied by hand, each admitted
fact recorded in the ledger's ruled entry shape, and those entries seed the ledger when it is
built (recommended).* For: the pilot is not serialized behind every preparation act (the ruled
pilot definition says so in terms, `…surface…:237-240`); the hole is declared, not hidden (the
boot-list draft's own two readings). Against: admissions made by hand must be re-checked when the
ledger's gate exists. Towards the objective: high — specification text sooner. Towards the
principles: #19 served by the re-check; #6 deferred and declared.

**Decision 9 — Guardrail 2.**
*A — as the predecessors wrote it: findings attach to their unit, no numbers, no rows.* For: the
named failure is real. Against: instructs a breach of the open-items register's rules (c)/(e) and
D-641 (both evaluators); loses any record the finding was made. Towards the objective: lower.
Towards the principles: #10, #12 breached.
*B — the repaired form of §8 (recommended): analysis findings → the quarantined audit questions;
apparatus findings → rowed and lapsed; the remainder → discarded under the worth test.* For: the
record already built the graded route; the plan's aim (no findings series) is delivered without
the breach. Against: rows still exist for apparatus findings, which then lapse by the ruled
mechanism. Towards the objective: high. Towards the principles: conforms.

**Decision 10 — The placement of the ceiling measurement's design (the evaluators' disagreement).**
*A — keep the ruled placement at the measurement-design stage, desk simulation first
(recommended).* For: the ruling's ground is sound — what counts as ground truth is a design
decision and belongs with the measurement layer's design; under the ruled order no residual is
interpreted before the audit, which comes after this stage, so CC's cost does not bite where the
ruled order is followed. Against: CC's argument — the obligation gates every phase, so its design
could start earlier at no cost to the analysis derivation. Towards the objective: high. Towards
the principles: #21, #19 served in sequence; the "beside" option was presented and declined on
2026-08-15.
*B — open the ceiling's DESIGN beside the framework phase.* For: earlier; the obligation is the
one bearing directly on the objective. Against: re-opens the 2026-08-15 sub-choice on a ground the
user already rated (parallel streams cost session context; the fact-gate's traffic stays
one-directional); no measurement can be interpreted earlier anyway. Towards the objective: equal
on what is learned, earlier in calendar. Towards the principles: the pruning direction paid.

**Decision 11 — The terminus of the migration.** Carried from v3/v4 unchanged: at the end,
`ARCHITECTURE.md` becomes the new text (A) or a pointer to it (B). *A* for: one document, the
canonical one, stays canonical; against: one file holding many specifications is the shape that
made the ruled archive-per-specification rule inexecutable. *B* for: one home per specification;
against: the canonical document becomes a table of pointers. No recommendation: the record does
not settle it (D-658) and the choice turns on the grain ruled at decision 2.

**Decision 12 — Reading depth.**
*A — v4's three closed tiers, decided before reading.* For: a stated decision rather than
discretion mid-pass. Against: the density axis was circular and the tiers contradicted the
source declaration (the Cowork evaluator); two of the four derived axes were unavailable; the
axes that change the answer — pollution, dormancy, establishment — were missing. Towards the
objective: lower. Towards the principles: #18 (unmeasured premise that depth is decidable in
advance).
*B — depth declared per unit at the source declaration from the three document properties and
the objective's dependency structure, reported with its inputs, over a tier-independent source
list, with raising a STOP-and-request (recommended).* For: keeps what the tiers were for
(discretion mid-pass is how the previous programme grew) without the closed set; the inputs are
the measured ones. Against: more per-unit judgment shown to the user. Towards the objective:
high. Towards the principles: #17(f) — no invented tier; the STOP makes the expansion visible.

---

## 13. What this plan does NOT do

No `src/` change, no build, no test, no guard run; no measurement of the analysis built, designed,
scoped or run (step zero measures the DOCUMENTS' provenance, not the analysis, and is the one
generator it widens). Nothing deleted, archived or moved except as the ruled pruning plan already
orders. No open-items row created, flipped or discarded by this plan; the two owed dispositions
of §2 are named, not acted. No finding number allocated. No ruling re-opened except where §12
puts it to the user as a question. No existing specification text edited before a ratified unit
covers its subject and its disposition record is complete. It does not authorize the audit.

---

## 14. What this plan carries from the earlier review, labelled (Ruling 4)

**DIRECT, cited:** the rule-generation correction (derivation-first is an ordering, not a
prohibition; `cowork_rulings_2026_08_15_phase_definition_sitting.md` §6); the live unsettled
tension between the key-axis commit rule and the abstention rule (`ARCHITECTURE.md:331-338`);
the table-of-contents omission of the standing-rules section (`:582-603` against `:265`); the
fenced-code heading hazard; guardrail 2's collision; the lineage losses; the 474-against-677
correction. **SWEEP, UNESTABLISHED, not rested on:** the five-sub-field falsification form; the
failing-run attribution finding; the annotation-schema finding; the deletion-history cost; the
code-inventory values. **REFUTED twice over by the independent evaluations and not carried:**
that guardrail 11 is self-sealing. **NOT carried, as a conformance artifact of the refute-only
brief:** the "not situated against the ruled structure" return as a largest finding — the
collision is real and is handled at decision 1 as conformance.

---

*Provenance: Cowork, 2026-08-21, the successor-plan session, at tip `3cfb220b1d`. Every governing
document named above was read from a snapshot staged through the device bridge with the file
tools: `CLAUDE.md` 1–1845 and `DECISIONS.md` 1–858 in full by this session; the phase-definition
surface, its sitting record and the method-directions record whole; both evaluation reports
whole; the four plan versions, the boot-list draft, the earlier review and its dispatch whole;
`cowork_design_doc_template.md` whole before drafting. Not opened by this session:
`tools/audit/july_screen_report.md`, `home_classification.json`, `cowork_joint_estimator_factorization.md`,
`ARCHITECTURE.md`'s body — every claim about them above is cited to the evaluator that read it.
`git show --stat` and `git show <hash>:path` were run at the explicit hash `3cfb220b1d` on the
user's machine; `git log`, `git status` and `git rev-parse` were not run. One declared tell at
boot (shell utilities over a staged copy). Nothing was committed and nothing was pushed.*
