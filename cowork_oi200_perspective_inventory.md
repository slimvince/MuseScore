# The perspective inventory — how this project searches for what it does not know

> **★ STATUS: §4 RATIFIED BY THE USER 2026-08-03 — THE ONE HOME FOR THE ENUMERATED DISCOVERY
> CHANNELS.** `CLAUDE.md`'s phase-2 clause (register entry **D-231**) now POINTS at §4 instead of
> listing six subjects of its own, so §4's ten channels are the enumeration of record and the
> clause carries no second, shorter list (#6). Ratified together with the scope ruling written into
> §4 — which of channels 4, 8, 9 and 10 that clause reaches — and after the correction of record in
> channel 9, which was applied FIRST so that nothing untrue was ratified. Register entry **D-439**.
>
> **★ WHAT THE RATIFICATION DOES NOT DO, stated so a later reader does not assume more was decided
> than was.** The **§6 program is NOT adopted**, in whole or in part. **OI-200 is not pulled
> forward**, and this document's own §9 request — adopt, amend or reject the §6 program — **stays
> open and untaken**. No probe, fix, design or inference change is authorized. **Phase 1 is not
> complete.** What was ratified is the ENUMERATION and its scope, and nothing else.
>
> *Drafted as:* **STATUS: DRAFT for discussion (Cowork, 2026-08-01).** Prepared at the user's
> direction while the
> OI-207 adjudication is in flight, as an input to the architecture step-back (the open-items
> register row OI-200), whose scheduled turn is after the OI-198/OI-199 reviews. Nothing here is
> ratified; nothing here edits the open-items register (the adjudication dispatch owns that surface
> until it closes — the concurrent-edit hazard recorded at OI-85). OI-200 is this document's home
> row, so no new row is required. This is a methodology decision surface, not a component design;
> the fourteen-section component structure applies where it maps (a terms table, decisions with
> alternatives, related work) — the building-block, runtime, data-design and deployment sections are
> not applicable and that omission is stated once, here. *(The drafted banner is preserved verbatim
> under #12 — the two clauses about the register and about OI-200's schedule still hold; what the
> ratification changes is the first clause, "nothing here is ratified", and it changes it for §4
> only. The reading surface the user ruled from is
> `ratification_surfaces/cowork_perspective_inventory_ratification.md`.)*

---

## §0 Terms

Every term below is either standard music theory in its standard sense, defined here, or cited to
the document that defines it. Nothing is used before its row.

| Term | Meaning |
|---|---|
| **the open-items register** | `OPEN_ITEMS.md` (the index) plus `open_items/OI-<n>.md` (detail files) — the one home for every discovered-but-unresolved issue. "OI-<n>" names a row in it. |
| **the decisions register** | The companion index of rulings (what was decided and its status), shape ratified by the user 2026-07-28 (OI-208), population in flight (the OI-207 adjudication). |
| **observation channel** | Anything that generates observations about the system: an input fed to it, a reference it is compared against, a question asked of its output, or a reader examining it. Defined here because the whole document turns on it. |
| **envelope** | The set of inputs a component was fitted, established and measured on. For the joint estimator: 326 Bach chorales, roughly 60–150 events per piece (OI-39, OI-209). **Out-of-envelope** means outside that set. |
| **oracle** | An independent source of the same answer, used for cross-checking — for example the pure-Python reference decode beside the C++ decode, or the music21 reading beside the DCML ground truth. (Established usage in this repository, e.g. principle #19's "oracle cross-check".) |
| **detection power** | The fraction of defects of a given kind that a given search method actually finds, measured by planting known defects and counting how many the search reports. The repository's existing name for the planted-defect procedure is the **seeded error rate** (the OI-199 pass-2 requirement). |
| **residual** | The disagreement that remains between the system's output and the ground truth after all known mechanisms are accounted for. |
| **ground-truth ceiling** | The measured agreement between independent human annotators on the same music (OI-179). No system can be validated beyond it, and residual below it cannot be attributed. |
| **invariant check** | A property that must hold on every input, checked mechanically, without knowing in advance what failure would violate it. Example: analyzing a transposed edition of a piece should give the transposed analysis and change nothing else. |
| **metamorphic relation** | The general form of an invariant check: a stated relation between the analysis of an input and the analysis of a defined transformation of that input. The term is from the software-testing literature (Chen et al., metamorphic testing); it is defined here so no reader needs that literature. |
| **field report** | An observation arriving from real use rather than from any planned measurement — the user reporting a stall (OI-206), a crash (OI-211), or a requirement (OI-209). |
| **concept gap** | A phenomenon a published analysis system explicitly models and this project's stack has no representation of at all — as distinct from a phenomenon both model and one handles worse. |

---

## §1 Purpose

The user's question, verbatim: *"Unknown unknowns — how can we find out what we do not know?"* —
asked in service of the standing goal that the open-items register eventually be the one
comprehensive, complete and correct list of everything open, so the plan can say when each item is
taken care of.

This document answers the question as far as it can honestly be answered, grounds every part of
the answer in this repository's own recorded precedents, and turns the answer into a concrete,
bounded program proposed for the architecture step-back (OI-200). It decides nothing; it is the
prepared decision surface the user asked for.

## §2 The question, framed exactly

Divide what there is to know into four classes:

1. **Known and recorded.** The established baselines, the certified layers, the ratified
   decisions. Homes exist: `CLAUDE.md` gate block (A), `STATUS.md`, the decisions register.
2. **Known unknowns.** Questions we have named but not answered. The home is the open-items
   register — every row is a known unknown with an owner and a gate.
3. **Unknown knowns** — things this project once knew and lost sight of. This class is real and
   has caused the worst recent damage: the Stage-3.1b shelving was recorded, with evidence, and a
   later build contradicted it because the record lived in an archive outside the session-start
   read (OI-210's history; the founding case for the decisions register). Published-but-unconsumed
   facts (OI-221) are the same class on the code surface. **The systematic remedy is already in
   flight:** the OI-207 adjudication plus the decisions register exist precisely to empty this
   class and keep it empty.
4. **Unknown unknowns.** Issues no row names, no session remembers, and no current check exercises.

The exact statement of what is possible for class 4: **an unknown unknown cannot be searched for
by its content, because naming the content is what would make it known. What CAN be done is (a) to
vary the things that GENERATE observations, since every finding in this project's history arrived
through some observation channel and unknowns survive only where no channel points; and (b) to
MEASURE how much each search method misses, so the remaining ignorance is bounded even though it
is not enumerated.** Everything in §4 and §5 is an instance of (a) or (b).

## §3 What the record shows has actually worked

Before proposing anything new, the honest inventory of how this project's genuinely unanticipated
findings were actually found. Each pattern below is a precedent, cited:

- **A new input population, not a new reading of the code.** The empty-decode family
  (OI-215/OI-227) was invisible on the entire fit corpus — zero admission failures on all 326
  chorales — and appeared the first time the 23 committed orchestral scores were decoded. The
  OI-199 pass-1 report drew the lesson itself: a fire-rate measurement on the fit corpus alone
  would have missed it; deep passes must characterize out-of-envelope inputs.
- **An independent reference disagreeing.** The C++-decoder-slower-than-Python surprise (OI-216)
  was caught only when Cowork compared CC's fresh timings against values already committed in the
  repository. The corrected ground-truth parser (the 2026-06-13 re-baseline) came from the music21
  oracle disagreeing with the DCML parse.
- **A stated prediction missing its band.** The weight fit's stop (OI-187) and the desk
  simulation's one failed case (which became the granularity amendment) were both surprises made
  visible because a quantitative expectation had been written down first (#17b). An expectation
  never written down cannot be missed visibly.
- **A field report.** The interactive stall (OI-206), the parked crash (OI-211) and the
  large-score requirement itself (OI-209) all arrived from the user's real use, not from any
  planned measurement.
- **A challenge to a defended premise.** The emission's struck-versus-sounding departure (OI-228)
  surfaced when the user refuted Cowork's decay argument in one line and the code was then opened.
  The observation channel was an outside reader refusing an insider rationalization.
- **History re-read.** The 3.1b contradiction was found by re-reading archived evidence against
  the current implementation — the channel the OI-207 adjudication is now running systematically.

What has NOT historically produced unknown-unknown findings: re-reading already-audited code with
the same questions, and sweeps for already-catalogued defect signatures. Those confirm and
inventory (they are necessary for other reasons); discovery has come from the channels above.

## §4 The perspective inventory — the channels, each with its principle, precedent, and proposed probes

This is the "out-of-the-box, outside-in" program, made enumerable and checkable. Each channel
states what is varied, why it can catch what nothing else catches, and what a bounded probe looks
like. Probes follow the standing funnel (#17): predictions written before measuring; read-only
first; a surprise is a STOP (#13) — noting the scope-of-surprise rule: these are explorational
runs, where surprises are the intended product (#5), not inference builds, where they are
forbidden.

### Channel 1 — Population variation (vary the INPUT)

**What is varied:** the music fed to the system, chosen deliberately from outside every envelope
the system was shaped on. **Why it works:** a system molded by fitting, establishment and
regression-measurement on one population conforms to that population; its unexamined behavior
concentrates exactly where the population never reaches (the OI-215 lesson, and principle #9's
reason for existing). **Precedent:** the orchestral set (found the whole admission family).
**Proposed probes:** (a) the late-romantic-through-atonal expansion already mandated at OI-38,
used explicitly as a measured discovery run, not only as future fit material; (b) a
notation-feature census — tuplets, grace notes, multi-bar rests, linked staves, ties across
system breaks, percussion staves, transposing parts (the feature list OI-206's hypothesis (b)
already enumerated as never exercised by the corpus) — with one probe piece per feature;
(c) synthetic extreme textures constructed to sit at structural corners: strict monophony, a
single sustained cluster, silence-heavy writing, a canon at the unison — each legal input the
fit corpus cannot contain by construction.

### Channel 2 — Oracle multiplication (vary the REFERENCE)

**What is varied:** the independent source the output is compared against. **Why it works:** two
independent derivations of the same quantity disagree wherever at least one hides an unknown;
every disagreement is a finding with a location attached. **Precedent:** OI-216 (committed
values vs fresh timings); the corrected ground-truth parser (music21 vs the DCML parse); the
Python-vs-C++ decode parity establishment. **Proposed probes:** (a) run publicly available
harmonic-analysis systems on our corpora and mine the disagreement set — not to adopt their
readings but to cluster where and why they differ (each cluster names a candidate mechanism we
may lack); (b) for each of our own derived published facts, one independent re-derivation from
theory or from a second implementation, disagreements rowed; (c) the ground-truth ceiling
measurement (OI-179) itself, which is the oracle-of-the-oracle and is already rowed.

### Channel 3 — Invariant and metamorphic checks (vary the QUESTION)

**What is varied:** the question asked of the output — from "does it match the ground truth
here?" to "does it satisfy a property that must hold everywhere?" **Why it works:** this is the
one channel that requires no anticipation of the failure mode at all: the property is derived
from music theory (#1), the check is mechanical over whole corpora, and any violation names an
unknown mechanism by construction. **Precedent in this repository:** the transposed-editions
defect (OI-142) — twelve chorales transposed relative to their reference edition produced 100 %
key- and chord-root-disagreement purely by misalignment; a standing transposition check would
have caught it the day it entered. **Proposed probes, each a theory-derived relation:**
(a) **transposition** — analyzing a piece transposed by any pitch interval must yield the
transposed keys and chord roots and change nothing else; (b) **octave doubling** — adding an
octave doubling of an existing tone must not change any chord's identity; (c) **uniform
time-stretching** — halving every duration must shift the analysis's tick positions
proportionally and change no reading; (d) **part order** — renumbering staves without changing content must change nothing;
(e) **the no-information-loss property (#12)** as a mechanical check on every published surface
(carried alternatives present wherever a winner is committed). Each relation that FAILS is a row;
each that HOLDS becomes a permanent cheap regression guard.

### Channel 4 — Prediction-first operation (vary the EXPECTATION)

**What is varied:** whether an expectation exists before the observation. **Why it works:** a
band miss is an unknown announcing itself at the moment of measurement; without the band the same
observation reads as noise. **Precedent:** #17(b) is already standing law, and OI-219 records
what its absence cost (the analysis-cost dispatch's interpretation error). **Proposed probe:**
none new — the channel is already mandated; the inventory lists it so the program is complete and
so its role in unknown-hunting is named: every future probe in channels 1–3 carries written bands.

### Channel 5 — Residual decomposition (vary the GRAIN of attention)

**What is varied:** the level of detail at which disagreement with the ground truth is examined —
from one aggregate number to named families. **Why it works:** an aggregate residual hides
mechanisms; decomposing it until every mass has a name either assigns each mass to a known cause
or names a new one. The ground-truth ceiling (OI-179) bounds the exercise: residual below
measured annotator disagreement is not attributable and must not be chased (#21). **Precedent:**
OI-192 — the fifth-substitution family was named by decomposing the adoption diff's cost side;
the two-tier class-(a)/class-(b) split itself is a residual decomposition that reshaped the
governing regression stop. **Proposed probe:** after the ceiling measurement lands, one
systematic pass clustering the current robust-unit failing runs by texture, position and
mechanism until every cluster either cites a row or gets one.

### Channel 6 — Public-research comparison (vary the CONCEPTUAL FRAME)

**What is varied:** the vocabulary of phenomena itself — using the published field as an external
enumeration of what a harmonic-analysis system CAN model. **Why it works:** a concept gap (§0)
cannot be found from inside the system's own vocabulary, by construction; it is visible only
against an external inventory. This is OI-200's theoretical half, verbatim ("vs the public state
of the art"), narrowed from a benchmark comparison into a concept-inventory comparison.
**Precedent:** the joint-estimator architecture itself came from exactly this move (the
2026-07-17 decision grounded in the published joint-inference literature). **Proposed probe:**
enumerate the concept inventories of the main published lines — voice-leading models, meter and
hypermeter, phrase and cadence schemata (galant schema theory), function theory beside
scale-degree theory, neo-Riemannian/transformational models for chromatic music, expectation
models — and for each concept record: modeled by us / deliberately excluded with a ruling /
absent with no ruling. The third class is the finding; each instance is a row. (The existing
evidence-inventory habit, OI-146, is the in-house half of the same move.)

### Channel 7 — Requirement-side enumeration (vary the DIRECTION — outside-in)

**What is varied:** the starting point — from the implementation outward to "from each thing a
user does, inward." **Why it works:** implementation-outward review can only examine what exists;
requirement-inward review finds the mechanism that does not exist. **Precedent:** the large-score
requirement (OI-209) instantly exposed that both the cost and accuracy envelopes were
chorale-shaped — no code reading would have said so; the explainability item (OI-154) is the
same shape. **Proposed probe:** enumerate the user-visible tasks (annotate a span, read the
status bar, implode to a chord track, tune a region, edit continuously while composing, analyze
a symphony, ask "why this reading?") and for each record which mechanism serves it and whether
that mechanism is established on the population the task implies. Gaps are rows. Field reports
(OI-206/209/211) are this channel arriving unsolicited; the probe runs it deliberately.

### Channel 8 — Fresh-reader passes with measured power (vary the OBSERVER)

**What is varied:** who reads, and with how much inherited framing. **Why it works:** an
incumbent reader carries the same premises as the code; a blind reader re-derives them or fails
to — and the certified two-pass pattern (blind second reading, seeded error rate) MEASURES how
much such a pass misses instead of assuming it misses nothing (#19 applied to the search
itself). **Precedent:** the certified L1–L5 audits (OI-84); the blinding failure and its standing
remedy (OI-222 — withheld findings never enter a mandatory session-start read); the sealed-
findings reconciliation experiment now assigned to the measurement-tools partition of OI-199.
**Proposed probe:** already scheduled — OI-199 pass 2 and partitions 2–3 run exactly this; the
inventory adds only the explicit instruction that each pass REPORT its seeded detection power so
§5's arithmetic has inputs.

### Channel 9 — History mining (vary the TIME of observation)

**What is varied:** when the evidence was produced — re-reading old rulings, shelvings,
falsifications and dead ends against the current tree. **Why it works:** it targets class 3
(unknown knowns) directly, and class 3 is where this project demonstrably bled. **Precedent:**
the 3.1b contradiction; the whole OI-207 adjudication now in flight. **Proposed probe:** none
new — the OI-207 adjudication is this channel **IN FLIGHT, not run to completion**: its residual
second pass ran on 2026-08-02, and both of its faces are still live at HEAD — the unresolved
cluster residual (`tools/audit/decisions/disposition_manifest.json` →
`disposition_counts.unresolved`, the rule BR-8 population the manifest's own text calls "the
honest outcome") and the owed full document reads (tracked on the `OPEN_ITEMS.md` OI-207 row,
whose correction of record of 2026-08-03 states how many design documents are read in full and
how many are owed, and whose proposal is to read them all and carry no tail). Running the
adjudication to completion is what discharges this channel; the decisions register plus its
session-start-read rule is the mechanism that keeps the class empty afterward.

> **★ CORRECTION OF RECORD (2026-08-03, made immediately before the ratification below).** The
> sentence above formerly read, verbatim: *"**Proposed probe:** none new — the adjudication is
> this channel run to completion, and the decisions register plus its session-start-read rule is
> the mechanism that keeps the class empty afterward."* That was untrue of both faces at HEAD.
> It was corrected BEFORE the ratification rather than after it, on the user's ruling of
> 2026-08-03, because ruling this channel's scope while its own text said the work was finished
> would have ratified a contradiction. The former wording is preserved here under principle #12;
> nothing else in this channel's text changed, and no verdict of
> `tools/audit/phase3_gate_partition.json` moves — that partition states each verdict against
> the SUBJECT `CLAUDE.md`'s clause names, using this document's channel numbers as locators only.

### Channel 10 — Defect-signature sweeps (the honest limit, stated)

The `DEFECT_TYPES.md` catalog sweeps find instances of KNOWN classes; by construction they cannot
find a class nobody has named. Their role in this program is inventory completeness and
regression, not discovery — with one exception worth naming: the catalog GROWS from surprises
(DT-22 and DT-26 were both promoted from findings), so every channel-1-through-9 finding should
ask "is this a new defect TYPE?" and feed the catalog, which then converts one unknown into a
sweepable known class forever.

### Which of these channels `CLAUDE.md`'s phase-2 clause reaches — ruled by the user, 2026-08-03

`CLAUDE.md`'s phase-2 clause names *"the enumerated discovery channels"* and, as of the same
2026-08-03 act that ratified this section, points here for them. **Until that act it listed six
subjects of its own** — populations, oracles, invariants, residual decomposition, concept gaps,
requirement side — which are channels 1, 2, 3, 5, 6 and 7 above; the four it never named are 4, 8,
9 and 10. Those four are what a pointer would otherwise leave ambiguous, so the user ruled on
2026-08-03 what the clause reaches, each verdict resting on the channel's own text rather than on a
judgment made here:

- **Channel 9 (history mining) — IN.** It is a distinct search, and the clause named it nowhere:
  neither the six subjects nor the two items stated before them (the remaining audit partitions;
  the blind second pass with its seeded error rate) is history mining. It also gates the phase-3
  family design on the partition's own verdict.
- **Channel 4 (prediction-first operation) — ALREADY REACHED, and it adds nothing.** Its own text
  says *"none new — the channel is already mandated"*: it is an obligation carried BY the other
  probes, not a search of its own, so there is nothing for the clause to reach separately.
- **Channel 8 (fresh-reader passes) — ALREADY REACHED.** Its own text says *"already scheduled —
  OI-199 pass 2 and partitions 2–3 run exactly this"*, and those are precisely the two items the
  clause states in the words immediately preceding the channel half. Naming it again would
  double-count work the clause already enumerates.
- **Channel 10 (defect-signature sweeps) — NOT a discovery channel**, on its own account: it
  states in terms that *"by construction they cannot find a class nobody has named"*, and that
  *"their role in this program is inventory completeness and regression, not discovery."* Its
  catalog-feeding role is noted rather than dropped — every finding from channels 1 through 9
  asks whether it is a new defect TYPE, and the catalog converts each answered yes into a
  sweepable known class.

**What this ruling does not touch: the phase-3 gate partition's verdicts.** That partition asks a
different question of the same channels — *must the struck-versus-sounding family design WAIT on
this item?* — and answers it against the item's search space, not against the clause's reach. The
two answers can differ without contradicting, and for channel 10 they do: a sweep cannot find a
new defect CLASS (so the clause does not reach it as a discovery channel) while a sweep for the
family's already-named classes can still find another INSTANCE (so the family design waits on it).
`tools/audit/phase3_gate_partition.json` carries that verdict with its reason, unchanged by this
ruling, and now carries the ruling itself beside them (its `the_channel_enumeration_source.the_scope_ruling`
block) so that a reader of the artifact meets both answers together. One consequence is recorded
there rather than silently corrected: that artifact's per-item `kind` field labels channel 10 a
discovery channel, which the ruling above supersedes. The field is left standing because a
registered prediction is not re-touched after the fact; this section is the authority on what the
clause reaches. — how ignorance is bounded without being enumerated

The question "did we find everything?" is unanswerable. The question "what fraction does this
method find?" is measurable, and the project already owns the machinery:

- **Seeded detection power per method.** For each audit pass and each mechanical check: plant
  defects of the kinds it claims to catch, run it cold, count. The OI-199 pass-2 seeded error
  rate is this; the harvest's check that all ten seeded decisions were found was this. The
  program's addition
  is only uniformity: every search method reports its power, none is assumed complete because it
  is diligent (#19 — a search is a measurement tool like any other).
- **The sealed-finding reconciliation.** Where findings already exist, seal them, run the blind
  pass, and score whether the method rediscovers them (the OI-222-remedied design, assigned to
  the measurement-tools partition). This measures power against REAL defects, not planted ones.
- **Coverage accounting per channel.** Each channel's probe declares its covered set (which
  populations, which relations, which concepts, which tasks) so the eventual claim has the form:
  *within these enumerated channels, at these measured detection powers, on these declared
  envelopes* — and anything outside that boundary is declared out of scope rather than silently
  assumed in.

**What "comprehensive, complete and correct" can then honestly mean:** not an absolute, but a
trust statement — every channel enumerated, every probe run with written predictions, every
search's miss rate measured, every declared envelope named, and every finding rowed with an owner
and a gate. That is the strongest completeness claim a finite process can make, and it is
strictly stronger than any list assembled without the miss-rate arithmetic, because it says how
wrong it is likely to be.

## §6 The proposed program for OI-200, sequenced

When OI-200's turn arrives (after OI-198/OI-199, per its row), the step-back runs the inventory
in this order — cheap and mechanical first, judgment-heavy last, each probe read-only with
predictions first:

1. **Invariant checks (channel 3)** — cheapest, fully mechanical, and each surviving check
   becomes a permanent guard. Transposition first (it has already drawn blood, OI-142).
2. **Requirement-side enumeration (channel 7)** — a bounded table, no code run; it prioritizes
   everything after it by naming which gaps face the user.
3. **Residual decomposition (channel 5)** — gated on the ground-truth ceiling (OI-179), which
   should therefore be scheduled before or with it.
4. **Population probes (channel 1)** — the notation-feature census and synthetic corners; the
   OI-38 repertoire expansion joins when the user schedules it.
5. **Oracle mining (channel 2)** — the public-system disagreement study.
6. **Concept-gap comparison (channel 6)** — the survey pass, feeding the refinement agenda that
   OI-200 is chartered to prioritize.

Channels 4, 8, 9 and 10 are already standing law or already scheduled; they appear in the program
only as reporting obligations (detection power, catalog growth).

## §7 Alternatives considered

**Alternative A — rely on the already-scheduled audits alone (do nothing extra).** For: no new
work; the audit trio (OI-198/199/200) is ratified and unfinished, and adding scope before it
completes risks the recency-chasing error the method reminders warn against. Against: the audits'
discovery record is measured and modest for unknown unknowns — pass 1's corpus-fire arm would
have missed OI-215 (its own report says so), and signature sweeps find only known classes; #19
forbids trusting a search whose detection power is unmeasured, and #5 directs investigation when
facts may be scarce — which "we do not know what we do not know" is by definition. Rejected as
insufficient, but its caution is honored by anchoring the program inside OI-200's existing slot
rather than creating a new work stream.

**Alternative B — the channel program above (proposed).** For: every channel has a precedent in
this repository's own findings (§3), the program is bounded and sequenced, the completeness claim
it supports is measurable (§5), and it satisfies #1/#2 by deriving probes from theory and
published research rather than from hunches. Against: real cost, mostly in corpus preparation and
the concept survey; partially mitigated because the two most expensive inputs (repertoire
expansion, ground-truth ceiling) are already mandated rows (OI-38, OI-179) that this program
consumes rather than duplicates (#6 at the process level).

**Alternative C — formal exhaustiveness (verification-style guarantees).** For: the only approach
that could claim absolute completeness for the properties it covers. Against: it covers only
stated properties — the unknown-unknown problem recurs one level up (which properties to state),
which is exactly what channel 3 does at proportionate cost; and the proof machinery for a system
of this size is out of reach for this project's build effort. Rejected; channel 3 is its
affordable core.

## §8 Related work and external sources

Metamorphic testing (Chen, Cheung, Yiu 1998 and the subsequent literature) — the formal home of
channel 3; adopted as method, no code borrowed. The seeded-defect measurement of a search's power
is standard in software inspection research (capture-recapture and fault-seeding literatures) and
is already this repository's practice via the OI-199 pass-2 requirement; the program only makes
its reporting uniform. The concept inventories named in channel 6 (voice-leading models, schema
theory, neo-Riemannian/transformational theory, meter and expectation models) are survey targets
for OI-200's theoretical half, to be cited concretely in that pass's own report — deliberately
not summarized from memory here (the never-work-from-memory rule; the survey is the probe).

## §9 What this document is not

It is not a register edit (the adjudication owns that surface until it closes); not a new work
stream (its home is OI-200's existing slot); not a fix or a design for any open defect (the
struck-versus-sounding family keeps its deferred fix surface untouched); and not a completeness
claim (it is the method by which a bounded completeness claim could eventually be made). Its one
requested decision, when the user chooses to take it: adopt, amend or reject the §6 program as
the shape of OI-200's discovery half.
