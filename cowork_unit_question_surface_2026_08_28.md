# Decision surface — the unit question (§9.0 of the framework document): what is a unit?

> **Decision surface (Cowork writing side, 2026-08-28).** Written under the eightieth handoff entry's
> cadence, whose item 4 names this the next act that moves the plan. It presents ONE decision. The
> choice question is put in a separate, later turn, after this surface has been read (the standing
> presentation mandate, `CLAUDE.md` Conventions, user mandate 2026-07-05).
>
> **Presentation rules followed:** every advantage and disadvantage names the principle it rests on,
> and every option is rated on the two ruled axes — towards the principles and guardrails, and
> towards the ultimate objective, the best possible inference (**D-424**, user-ratified 2026-07-26).
> Everything is re-explained from scratch; nothing assumes memory of earlier sittings.

## 1. The background, from scratch

**The framework document** is `cowork_framework_document_draft_2026_08_28.md` — the draft
"all-encompassing architecture" of the harmonic analysis, derived on 2026-08-28 in two stages: first
blind, from published research and the ground truth alone; then revised on the record against this
project's own material. Its job is to decide the **layer decomposition**: which questions the
analysis answers, where each question is answered, and what each part may assume about what reaches
it. It is a draft: not compared against the placement sample, not ratified, and ratification of the
decomposition is separately held until the external list of published research you are assembling
arrives and is dispositioned against it (the document's own §1.4).

**§9.0** is the first item of that document's "Architecture decisions" section. The document
deliberately does not settle it and offers it to you as this phase's first ratified finding. The
question: when the architecture is cut into pieces — pieces that get charters, boundary contracts,
and eventually their own detail specifications — **what kind of thing is one piece?** The document
calls a piece a *unit*.

**Why this is ruled first.** On 2026-08-28 you ruled (Ruling 2 of the framework-delta sitting) that
this question comes before the sharpest difference between the old and new architectures — the
question of whether a layer owns *the answer to one question* (the derived framework's rule) or *one
evidence source's contribution to one question* (the incumbent rule, `ARCHITECTURE.md` §2.15,
re-read at that file by this session). Both of those rules are statements about units, so neither
can be graded before the unit is fixed. Ruling the unit question does **not** decide that
layer-ownership question; it makes it gradable.

One honest qualification: the phase's ruled output form admits a design point recorded as
"underived: open, needs a ruling or new research", so an unruled §9.0 does not by itself block the
phase's postcondition. What waits on it is the grading of the layer-ownership question and of the
framework's charters generally.

## 2. The three candidate readings, and what each would change

The framework document's own terms, so the options are concrete:

- **A decision** — one question about the music that the analysis settles, and could settle
  differently. Examples: what is the tonality over this stretch; where does one harmony give way to
  the next; is this sounding note part of the chord or an elaboration of it; which chord is read
  over this span.
- **A factor** — one additively combined term of the numerical score the engine assigns to a
  candidate reading. Examples: how well the sounding notes fit a candidate chord in a candidate
  tonality; how plausible one chord-to-chord move is. A factor is a means of computing a decision.

**The factor reading: units are factors of the model.** The framework's middle layer — the one
place where tonality, harmonic boundaries, chord-tone assignment and chord identity are settled
together — would decompose into roughly ten units, one per term of its candidate score. The
framework would own the factor roster and the conditional-independence premises (which factor may be
treated as independent of which), and the boundary contracts between units would become independence
claims rather than contracts about published facts. The document's §5 decomposition would have to be
re-derived in that vocabulary before the placement test could mean anything.

**The decision reading: units are decisions the analysis makes about the music.** This is the
reading the document is drafted at. A layer is a question: the first layer reads the notation for
facts, candidate boundaries and evidence, and decides nothing; the middle layer settles the four
entangled questions as one decision, published with its rival readings; the last layer reads off
what follows (cadences, grouping, chord symbols, figured bass) and decides nothing new; a
voice-leading axis runs beside. Factors stay inside the middle layer's later detail specification,
as means rather than units.

**The reconciliation reading: units are decisions, each carrying its factors as sub-units.** Every
decision's charter would additionally enumerate the factor set that computes it. Roughly double the
unit count; every charter two-tiered.

## 3. The evidence, fact-checked

What I verified at the files this session, and what is relayed:

1. **The ground truth is a record of decisions and contains no factor.** The framework document
   labels this FACT, read at the ground-truth analysis files. *(Relayed from that document; I did
   not re-open the analysis files.)*
2. **Disagreement between two independent analysts of the same piece is disagreement about
   decisions** — is this a chord, which figure, which tonality. *(Same status as 1.)*
3. **The empirical findings ledger's admitted facts are overwhelmingly statements that a decision is
   underdetermined by the evidence at a moment.** **Verified by me at `EMPIRICAL_FINDINGS_LEDGER.md`**
   for the four entries §9.0 cites: C2 (a sonority readable as a chord or as the chord a third
   above it — the separating evidence is the surrounding music), C6 (an added-sixth chord and a
   seventh chord on the related root carry the same pitch-class content), C34 (a sonority whose
   defining third does not sound), C35 (three pitch classes containing a tritone — the rotation is
   not determined by the sounding pitches). All four are exactly statements that a *decision* is
   underdetermined at a moment; none is a statement about a factor.
4. **The published multi-task systems' separately predicted heads are decisions, and their measured
   pathology is decisions disagreeing** — the framework document quotes *"potential for
   self-contradictory outputs in which the six sub-labels have different ideas about the chord"*,
   and reports that every later system in that lineage adds machinery to undo the separation, with
   the paper-reported accuracy movements given per system. *(The FACT labels are the framework
   document's own, from papers it reports fetched and read; verified by me that the document states
   them, not re-verified at the papers.)*

## 4. The options rated, on the two ruled axes

**The decision reading.**
*Towards the principles:* strong. It is the reading the evidence supports (#1, fact-based only —
every item in §3 is about decisions; none is about factors). Each question gets one home (#6), and
the chord symbol and Roman numeral become views computed from a settled decision, so no second home
for one fact. It keeps factor choices in the next phase's detail specifications, where the ruled
six-phase order puts them — the framework phase decides decomposition, charters and contracts, not
scoring mechanics. And it puts no conditional-independence premise under load before the Premise
Gate (#17) can examine one; a checkable-but-unchecked independence claim is exactly what #18
forbids a design to carry.
*Towards the objective:* the measurements the document carries say the entangled questions analyse
music best when decided together, and that dividing the deciding along factor-like lines produces
incoherent composites that later systems spend machinery repairing. Units-as-decisions is the
reading that lets one layer hold the four entangled questions as one decision.
*The case opposing it, with its principle:* under this reading the framework says nothing about
factor structure, so conditional-independence assumptions go ungoverned until the
detail-specification phase — a deferred #18 exposure. The answer on the record: the Premise Gate
governs them there by standing rule, and a framework-level factor claim made now would itself be an
unestablished premise.

**The factor reading.**
*Towards the principles:* the one argument for it is #17's spirit — premises made explicit early,
by owning the factor roster and independence claims at the framework. Opposing it: the ground truth
contains no factor, so the reading has no evidence behind it (#1); the framework would be writing
the middle layer's detail specification inside the framework phase, which the ruled phase order
forbids; and its boundary contracts would be independence claims — causal claims about our own
system that are checkable but unchecked today, which #18 forbids putting under load.
*Towards the objective:* no measurement in the record says a factor decomposition of the deciding
analyses music better; the multi-task lineage measures the opposite for divided deciding.

**The reconciliation reading.**
*Towards the principles:* it appears to keep both truths — decisions decided together, factors
visible and governed now. Opposing it: a factor named as a framework sub-unit and specified again in
the detail specification is one concern in two homes (#6); and the framework would fix factor
rosters it has no evidence for yet — the document itself leaves how the middle layer's score is
formed and fitted to the detail specification and the measurement design (its DP-P), so the two-tier
charters would be filled by conjecture (#1, #17).
*Towards the objective:* nothing measured supports the doubled structure analysing music better;
its cost is carried by every later specification.

## 5. The recommendation, with its reason

**The decision reading.** Every piece of evidence the record holds about what the pieces of a
harmonic analysis are — the ground truth's own form, the analysts' disagreements, the ledger's
admitted facts, the multi-task literature's pathology — is about decisions. The factor structure
loses nothing by waiting: factors remain the means inside the middle layer's detail specification,
where the Premise Gate already governs them.

## 6. What ruling this does, and what it does not do

It fixes what a unit is, which is the vocabulary the framework's charters and the layer-ownership
question are graded in. It does **not** decide the layer-ownership question. It ratifies no part of
the decomposition — the §1.4 hold on your external research list stands, and the two held
differences (segmentation rivals, and retiring merge-equal) stay held. It changes no code, no
measurement, no golden, and writes no register entry (the register cannot currently accept one; the
rule-(c) suspension record is the route). If the external list, when it arrives, bears on the unit
question, this ruling is revisitable at ratification like every finding of the phase. If the factor
or reconciliation reading is chosen instead, the framework document goes back for re-derivation of
its §5 in that vocabulary before the placement test is meaningful.

## Provenance

Written by the Cowork writing side, 2026-08-28, under the eightieth handoff entry. Read at the
objects this session through the file tools on bridge-staged snapshots: the framework document §0,
§1, §2, §4, §5, §9.0 and its design points, §10.1 opening, Appendix A.4;
`cowork_rulings_2026_08_28_framework_delta_sitting.md` whole; `EMPIRICAL_FINDINGS_LEDGER.md` §6 at
C1–C8 and C34–C37; `ARCHITECTURE.md` at the single-responsibility clause and the
three-kinds-of-work statement; `decisions/group_K.md` at D-424 and D-430;
`cowork_design_doc_template.md` whole. No shell command of any kind was run and no git object was
resolved. The published-literature figures and the ground-truth readings are relayed from the
framework document's own FACT labels and are marked so above. This file is not covered by
`cc_instruction_landing_2026_08_28.md`, which predates it; it rides a later landing act.
