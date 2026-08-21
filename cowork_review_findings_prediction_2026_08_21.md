# Registered prediction — what survives of the plan review so far, and what the two fresh evaluations should re-find

> **STATUS: A REGISTERED PREDICTION under `CLAUDE.md` #17(b), recorded BEFORE the two evaluations
> of `cowork_plan_evaluation_brief_2026_08_21.md` run.** Cowork, 2026-08-21. It orders no act,
> touches no document, takes no ruling, and is authority for nothing.
>
> ## ⛔ THIS FILE IS NOT AN INPUT TO EITHER EVALUATION
>
> **Neither the CC evaluator nor the second Cowork evaluator may be given this file, or told what
> is in it.** The brief's §2 requires both to be blind to every prior verdict on the plan. A
> prediction shown to the thing it predicts is not a prediction, and a finding an evaluator was
> handed is not a re-derivation. Its readers are the user, and the session that writes the
> successor plan AFTER both evaluations have returned.
>
> **What it is for.** Each item below is a claim that an unbiased evaluation should reach on its
> own evidence. When the two evaluations return, this file is the test: an item re-found
> independently by both is established twice over; an item found by neither was probably an
> artifact of the refute-only brief; an item found by one and not the other localises a real
> question. That comparison is the point, and it only works if this file stays sealed until then.

---

## 0. How to read the establishment column

The existing review declared, in its own §6.2, which of its verdicts it established at the primary
source itself and which rest on citations from nine read-only subagent sweeps it did not
personally re-open. That distinction is carried here, because it decides how much re-derivation
each item needs.

| mark | meaning |
|---|---|
| **DIRECT** | established at the primary source by the party that reported it |
| **SWEEP** | rests on a subagent's citation the reporting party did not personally re-open (#19: not established) |
| **THIS SESSION** | re-derived at the primary source by the 2026-08-21 Cowork session, coordinates confirmed at HEAD |

---

## 1. The single most valuable output so far — a design artifact, not a verdict

**The replacement form for a specification statement's falsification field.** The plan's §5 makes
field five one sentence of prose and mandatory on every statement. Five probes were traced into
the code from the delta side; exactly one — an existence statement about a named field — was
returnable without interpretation. The proposed replacement carries five sub-fields:

- **ARM** — `joint` / `legacy-live` / `legacy-dormant`; the arm cannot be recovered from the code's
  own text (see §3.1 below).
- **SITE** — a named symbol, never a description. *"The boundary-proposal site"* resolved to two
  sites with opposite answers.
- **OBSERVABLE** — what the check actually reads, stated so it does not depend on interpreting a
  word the code does not use.
- **DECISION RULE** — a predicate over the observable, so the verdict is a computation rather than
  a reading.
- **NOT-FALSIFIED-BY** — the named near-miss the clause must not be satisfied by. **All five probes
  had one, and three of the five lived in a different file from the true site**, so without this
  line the likeliest error is not a wrong verdict but a right verdict against the wrong object.

*Establishment:* **SWEEP** for the individual code sites, **DIRECT** for the reasoning. *Prediction:*
an evaluator that traces any small set of behavioural statements into this code will reach the same
shape, because the causes are structural, not particular to these five.

---

## 2. Findings that stand on their own evidence and should be re-found

**2.1 A frame taken from `ARCHITECTURE.md`'s headings is contaminated.** The entire Layer 1–6
analysis specification — the document's principal body of musical knowledge — sits as `####`
children of §3.3, a section about where source files live (`:1537` → `:1560` Layer 1 … `:2192`
Layer 6). §3 is a source-tree listing and §4 is one subsection per class. Separately: the document
carries 26 `##` headings while its table of contents (`:582-603`) lists items 1..19 and **omits the
joint estimator's own standing-rules section (`:265`)**, document governance (`:551`) and both
appendices — so a heading enumeration and a table-of-contents enumeration disagree exactly on the
live production layer. And five `^# `-matching lines at `:896-907` are shell comments inside a
fenced code block, so a "mechanical" enumeration is not mechanical.
*Establishment:* **DIRECT** for the table of contents and the fenced-code hazard; **SWEEP** for the
§3.3 subordination. *Prediction:* re-found, cheaply, by anyone who opens the file.

**2.2 The concerns are coupled, and the coupling is measured, not argued.** The chord axis is
scale-degree-valued relative to the state's own tonic and mode (D-526), so a section derived with
the key section closed produces statements about absolute roots — the wrong representation. Rule
(b)'s capacity budget is **one budget over the union of all sections** (`:293-296`). And the record
already carries a case where a bookkeeping decision belonging to one section decided another
section's outcome against the ground truth (`:438-445`, the semi-Markov length bias).
*Establishment:* **DIRECT.** *Prediction:* re-found by anyone who reads the joint estimator's
standing rules, because the plan's own §15 names this as the deepest risk and points at the text.

**2.3 A live, declared, unsettled contradiction sits in the record right now, and no plan has a
step that would find it.** Rule (d) (`:331-338`): on the key axis the decoder commits its
maximum-a-posteriori path and never abstains; *"This sits in tension with the abstention rule at
§5.7a … The two statements are both in force in the record … Which governs is not settled here."*
**This is a standing fact about the specification, independent of any plan**, and it is the
concrete instance of why a per-section method that closes each unit needs a cross-unit consistency
step. Neither the plan nor the ruled framework phase contains one.
*Establishment:* **DIRECT.** *Prediction:* re-found, and it deserves its own disposition regardless
of which plan wins.

**2.4 Failing runs cannot be attributed to a section from the committed artifact.** The reference
records exactly eight fields per run; the only cause-bearing one is a class letter computed from
**our own** pitch-class set, so it says the root is undecidable by symmetry, not which decision
failed — and 94.3 % of failing cells carry it. Nine richer per-cell fields built one function
earlier are dropped at the run merge. Real attribution needs a full corpus regeneration (the corpus
is gitignored), plus re-derived key, bass and boundary verdicts, **plus the musical score itself**
for spelling, because the corpus JSON carries pitch classes only.
**Consequence, which is the part that matters:** error mass per section feeds *both* the ordering
and the depth tier in the plan, so this removes the load under two of its four derived axes.
*Establishment:* **SWEEP.** *Prediction:* re-found; cheap to re-check at the writer and the reader.

**2.5 The ground-truth annotation schema enumerates conclusions, not decisions.** No field records
where a harmony boundary falls; none records which sounding tone is a non-chord tone; none records
abstention or confidence; the alternatives are at most one, unranked. The gate runs on the narrower
of the two formats. The corpus's own documentation calls its analyses *"a reductive act … not in
any sense 'definitive'"* — which is principle #21 arriving exactly where the plan proposed to lean.
*Establishment:* **SWEEP.** *Prediction:* re-found by anyone who opens the schema with the question
*"which decision does this field record?"*

**2.6 Walking the deletion history does not fit any budget yet proposed.** Measured over 13
specification documents: 229 commits touch them, 150 delete at least one line, 15,483 lines deleted
across 844 sites, 38,252 diff lines total. **The cost driver is classification, not reading** —
deletions here are frequently relocations into five append-only archive documents, so 780
non-rewrite sites each need a destination cross-check before they can be called deleted rather than
moved. `ARCHITECTURE.md` alone holds 13,725 deleted lines, 90.3 % of them inside two whole-file
rewrites where a dropped section is invisible without a section-by-section comparison.
**This is a cost fact about any method that walks deletion history**, ruled or not.
*Establishment:* **SWEEP** (one ordered measurement, method stated). *Prediction:* re-found, and it
is the finding most likely to change the shape of the successor plan rather than a clause of it.

**2.7 A section whose defect is a HOLE has no advance signature.** Rule (c) is recorded as having
*"no specified form anywhere in this architecture and no recorded basis"* (`:309-313`). Nothing in
a heading, a dependency order, an error count or a source-list size announces that the record is
**silent** where a specification is owed — it is visible only on opening the section. This is the
general argument against deciding reading depth before reading.
*Establishment:* **DIRECT.** *Prediction:* re-found.

**2.8 Two axes that change the answer are on nobody's list.** Whether a section's subject is **LIVE
or DORMANT** (`docs/scoring_model.md`'s ratified banner declares its mechanism content describes a
scorer dormant on both production surfaces; `ARCHITECTURE.md` §4.1/§4.2 specify legacy classes),
and **establishment status** (§8 declares every hand-set scoring magnitude UNFALSIFIED, NOT
ESTABLISHED). Also: pointer sections and sections that are not about the analysis at all (File
Persistence, Coding Standards, Contributing) fit no depth tier and no axis assigns them one.
*Establishment:* **DIRECT** for the banners. *Prediction:* re-found.

**2.9 Arithmetic on the frame test.** With a sample of 60 and a stop at more than ten unplaceable,
a missing axis covering 10 % of out-of-frame statements gives an expected 6 and roughly a **3 %**
chance of reaching 11 — the test essentially never fires; it acquires usable power only around a
20–25 % true rate. **And the plan contradicts itself:** its A5 says *"an unplaceable statement is a
finding about the FRAME"* while its §10 says fewer than eleven means the frame is not wrong. Its
own founding instance refutes the threshold — the gap that produced v2 was found by placing **one**
example and watching it not fit.
*Establishment:* **DIRECT** (arithmetic, and both sentences quoted from the plan). *Prediction:*
re-found. Note this is a finding **against a threshold**, not against the test, which is good.

**2.10 One guardrail is self-sealing and one instructs a breach.** Guardrail 11 makes *"a proposal
to build something that checks these guardrails … itself the tell firing"* — so the one guardrail
that cannot be verified is protected by a clause forbidding the act that would verify it. And
guardrail 2 (*"findings attach to their section; no numbers, no rows"*) collides with the
open-items register's rule (c) and with D-641, which require a finding bearing on the analysis to
be surfaced and rowed.
*Establishment:* **DIRECT.** *Prediction:* re-found.

**2.11 The plan lineage has already lost load-bearing material with nothing recording the loss.**
v1's ten stop clauses — and v1's own statement that the failure is named *"so the guardrail cannot
be softened into general advice"* — are absent from v2. v2's self-declared governing correction,
*"`ARCHITECTURE.md` is one of several polluted documents, not the polluted document"*, survives in
neither v3 nor v4. Guardrails 7, 9 and 10 each lose their operative second clause between v3 and
v4. **This is why the brief makes all four versions the object of evaluation.**
*Establishment:* **DIRECT.** *Prediction:* re-found only if all four versions are read, which is
why it is a clause of the brief rather than a hope.

---

## 3. Findings that bear on the ANALYSIS rather than on the plan

These two were surfaced under D-641 and are owed a disposition whatever happens to the plan. Both
were re-derived at the primary source by this session, so they are not sweep-borrowed.

**3.1 Three live source files declare themselves DORMANT while the switch that selects them
defaults to true — and there is a fourth contradicting site.** `jointdecoder.h:43` *"DORMANT (no
production consumer)"*; `jointtables.h:44-45` *"This module is DORMANT — no production path reads
it"*; `jointnotationproducer.cpp:40` *"this increment is dormant"* — against
`composingconfiguration.cpp:178` `setDefaultValue(USE_JOINT_NOTATION_RECORD, Val(true))` and
`jointnotationrecord.h:47-49` asserting LIVE. **The fourth site the existing review does not name
is the comment block at `composingconfiguration.cpp:174-177`**, which itself states that the joint
record is the production notation analysis. **Any specification-against-code comparison that trusts
a file's own self-declaration answers against the wrong arm** — which is what comparability
principle #10 exists to protect.
*Establishment:* **THIS SESSION**; all five coordinates confirmed at HEAD.

**3.2 `CLAUDE.md` #21 routes a gating #19 obligation through a superseded phase numbering.** #21
commissions the ground-truth ceiling measurement to *"OPEN WITH PHASE 2, DESK SIMULATION FIRST"*.
Under the six-phase structure ruled 2026-08-15, phase 2 is the pilot on `docs/scoring_model.md`.
The correct remapping exists at the phase-definition surface §3.5:319-321 — but **`CLAUDE.md` is a
mandatory session-start read and the ratification surface is not**, and #21 carries no pointer to
it. **Open sub-question, not settled by anything read:** §3.5 marks that mapping AUTHORED, *"the
user rules it with this surface"*, and the sitting record does not say in terms that this
sub-mapping rode with the ruling.
*Establishment:* **THIS SESSION**, both sides.

**3.3 [[OI-179]] is OPEN, GATES, and is the one obligation that bears on the objective.** Confirmed
in `gating_ids` at `tools/audit/nongating_apparatus_rows.json` on 2026-08-21 (216 gating, 25
non-gating, 241 open). It is computable from data that already exists and is independent of every
plan on disk.
*Establishment:* **THIS SESSION.**

---

## 4. What is GOOD in the plan — recorded because the refute-only brief could not say it

No one has yet been asked this question. Recorded so the successor does not lose it by default.

- **The defense rule.** *"Because the implementation does this is not a defense"*, with a statement
  supported only by code marked UNSUPPORTED. This is the operational form of the ruled evidence
  rule and it is the best sentence in the document.
- **A6 worked.** Proving the statement format on a few statements before writing anything in it
  found the format insufficient before ten sections had been written in it — which is exactly what
  it was for. The plan had also already assigned the judging to the delta side.
- **A5's instinct.** Placing statements drawn from outside the frame, with an unplaceable one
  counted as a finding about the frame, run adversarially by the other side. Only the threshold is
  bad (§2.9).
- **§11's refusal to invent a number.** *"No number is fixed here, because no honest basis for one
  exists yet"*, with a stated method for earning one. The existing review scores this as a
  guardrail breach; declining to invent a figure you cannot ground is #17 and #24 behaviour, and it
  is the same restraint that review exercises elsewhere under D-658.
- **§6's bounded migration with a terminus ruled at the start**, under #23, with the stated reason
  that a migration with no ruled terminus is how the last one ended.
- **§13's negative scope declaration**, and **§15 existing at all** — the plan was written to be
  attacked, and the attack found real things.

---

## 5. Corrections of record about the existing review

Recorded so the successor does not inherit them, and so the fresh evaluations can be checked
against them.

**5.1 The plan's open questions were read as violations.** §14 asks the user *"Does this replace
the ruled PILOT phase, or execute it?"*, *"Is the curated boot list still needed?"*, *"Is the
structure kept, tested-then-kept, or rebuilt?"* A draft that orders no act and puts a collision to
the ruler is not overriding a ruling; asking is the only legitimate route to amending one.

**5.2 The OI-179 row inverts the direction of gating.** The review quotes the §7 heading *"not
gated by it"* and reads it as the plan denying that OI-179 gates. The plan's body says *"It is a
#19 obligation, so it **always gates whatever its subject** … Until it exists, no residual on any
axis can be interpreted."* Plan and surface §3.8 agree; it is listed as a divergence.

**5.3 The largest stated return is a conformance finding, not a merit finding.** Every row of it
reads *"the ruled structure holds X, the plan does Y"*. It contains no argument that the plan is
wrong. It was nonetheless stated first, carried into the commit message, and mixed with eight
measured findings.

**5.4 The review declined to press its own strongest argument because the target was a ruling.**
Its own words: *"A reviewing side asked to refute a user ruling either attacks the ruling or reports
that it cannot. This report does the second."*

**5.5 THE RULE-GENERATION CORRECTION, and it is the one most likely to be got wrong again.**
Eighteenth-stop Ruling 10 (*reconciliation, not rollback — pending a pilot*) was **formally
SUPERSEDED by derivation-first**, ruled 2026-08-15, `cowork_rulings_2026_08_15_phase_definition_sitting.md`
§6, the user's word recorded as *"yes"*. The ruling states its own character: *"**An extension, not
a reversal:** Ruling 10's character test — does this text express a design intent, or describe an
implementation? — survives at full strength inside the disposition discipline, applied AFTER
derivation against a derived statement."*

**So the current rule is an ORDERING, not a prohibition:** derive blind from independent sources and
fact-gated findings; **then open the current text and its history at full strength**; judge each
difference by the character test against the derived statement; never absorb an implementation
description as design input — quarantine it as an audit question. The implementation is one input
among many and is never authority. The pilot's own inputs say so in terms (surface §3.2): *"derived
blind; then — only after the derived statement is written — the current text and its history at the
preserved pre-restructuring version `b006dc15b5`, the fired changed passage met at full strength."*

The existing review quoted only §3.2's **constraints** line (*"NOT ALLOWED: reading
implementation-derived material inside the deriving session"*) and not its **inputs** line, which
turns an ordering rule into a prohibition. The 2026-08-21 Cowork session then compounded it by
declaring the ruled rule defective — a verdict aimed at a superseded generation, and withdrawn.

**5.6 What the unverifiability argument actually reaches.** *"Reading leaves no trace"* is a valid
attack on the plan's **guardrail 4** — a freeze on a declared source list, which is a promise about
what a session did not read. It is **not** a valid attack on derivation-first, which requires that a
derived statement and its defense exist as written text before the comparison is written, and that
leaves exactly the trace the argument says does not exist.

**5.7 AUTHORED, by the 2026-08-21 Cowork session — not ruled, and offered for refutation.** The
ordering derivation-first requires is provable at content-addressed objects by the E-ordering proof
this project has already run twice: the thirteenth batch established that the report blob at
`1fdce14fdd` carried no `## 13.`, no `## 14.` and no occurrence of `73 guard`, with §13 appearing
first at `9fbe98a305`, after the run — *no sentence asserting the end state existed anywhere before
the act that produced it.* If derived statements land in one commit and the comparison lands in a
later one, the ordering is provable by anyone afterward rather than asserted by the session.

---

## 6. The prediction, stated so it can fail

**Expected re-found by both evaluations:** §2.1, §2.2, §2.3, §2.6, §2.7, §2.9, §2.10.
**Expected re-found if the evaluator traces statements into code:** §1, §2.4, §2.5.
**Expected re-found only if all four plan versions are read:** §2.11.
**Expected to be found ONLY by an evaluator that is genuinely permitted a positive finding:** the
whole of §4 — and if neither evaluation returns anything under it, that is evidence the brief's
two-polarity clause failed, not evidence that the plan has no good parts.
**Expected NOT to be re-found, because it is a conformance artifact of the refute-only brief:** the
"not situated against the ruled six-phase structure" return as a *largest* return. An unbiased
evaluation may still note the collision — it is real — but should rate it as conformance and should
not lead with it.

**What would falsify this prediction as a whole:** both evaluations returning a substantially
different set of merit findings. That outcome would say the existing review's evidence was an
artifact of its method, and the successor plan should then be built from the new evidence and not
from this file.
