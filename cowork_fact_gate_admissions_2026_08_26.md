# Fact-gate admissions — the hand-applied test, 2026-08-26

> **THIS FILE IS NOT THE EMPIRICAL FINDINGS LEDGER AND MUST NOT BE READ AS ONE.** It is the record of
> hand admissions under **Ruling 8 of 2026-08-21**, which opens the pilot without the ledger built and
> applies the admission test by hand: *"each admitted fact is recorded in the ledger's ruled entry
> shape; those entries seed the ledger when it is built, and every hand admission is re-checked at the
> ledger's gate then."* **Every admission below is therefore provisional and is re-checked at that
> gate.**
>
> **No fact is transcribed here.** Each admitted candidate's five-field entry already stands in
> `cowork_empirical_findings_candidates.md` and is cited by identifier. Retyping one would be the
> transcription the record forbids (**D-431**), and it would let the two copies drift.

---

## The test, and what it is not

**The gate's ruled test:** *does the fact survive the implementation being thrown away?* — plus the
separately judged question of whether the statement is **approach-level**, that is, stated without our
implementation's words in it.

**It is not a correctness test, and this was clarified by the user at this sitting.** Correctness is
not decided at the gate; it travels with the entry in two of the five fields — **uncertainty** and
**establishment status**. A fact measured once, with no interval given, is admissible carrying exactly
that on its face.

**What admission does.** An admitted fact crosses the blindness barrier: it joins the independent
sources a deriving session **may** read, where our own code and every document derived from it may
not be read at all. Under §6.4 of the successor plan an admitted fact may also **withdraw a derived
statement** — so it is an input while v1 is written and a corrective afterwards.

**What is decided later, not here.** Where admitted facts and other sources contradict, the framework
phase resolves it per design point — candidates enumerated with their establishment status, at most
one chosen or **none** (*"underived: open, needs a ruling or new research"*), rivals recorded in the
defence. What is finally correct is settled at the audit, which is two-directional.

---

## Round one — EIGHT ADMITTED

**The user's words, recorded verbatim because they state the criterion more clearly than the record
does:** *"None of the eight even smells code - they all are about music - regardless of if they are
correct or not."*

| Candidate | The fact, in one line | Entry |
|---|---|---|
| **C1** | A chord reading whose root is not sounding is not thereby wrong; the published human analysis itself makes such readings | `cowork_empirical_findings_candidates.md` §C1 |
| **C2** | Where a sonority may be read as a chord or as the chord a third above it, nothing local separates the two readings; the separating evidence is the surrounding music | §C2 |
| **C4** | Over arpeggiated harmony the non-root tone can carry more duration than the root, so a duration-weighted aggregate prefers the wrong root — **music half only** | §C4 |
| **C5** | Where a vertical reading and the annotated reading disagree about the root, the cases are overwhelmingly bare three-note triads, for which bass-as-root is the correct default | §C5 |
| **C6** | An added-sixth chord and a seventh chord on the related root carry the same **pitch-class content**, so no reading of that content separates them | §C6 |
| **C7** | A residual disagreement between reading a sonority vertically and reading it by its role is a legitimate divergence between two readings, not an analyzer defect | §C7 |
| **C12** | An octave doubling leaves the sonority's harmonic identity unchanged | §C12 |
| **C13** | The fitted corpus is 326 four-part Bach chorales, which do not double; the repertoire the system must handle does — so any doubling figure fitted here is an in-envelope floor | §C13 |

**Each is admitted with the uncertainty and establishment status its entry already carries.** Nothing
is upgraded by being admitted, and no figure is restated (**D-431**).

**Not admitted with C1 and C4, and named so silence claims nothing:** the prohibitions that sit beside
them in their sources — *"do not retry the absent-root guard"*, *"do not retry any tone-aggregation
approach"*. Both are about our code, both fail the gate, and both must stay behind the barrier
precisely because a deriving session must not learn what our implementation already tried.

**Carried with C7:** it has a standing sibling already homed at `CLAUDE.md` gate block (A), **D-604**.
Whether the two are treated together is open and was not decided here.

---

## Round two — THREE ADMITTED, ONE ROUTED AS A POINTER, THREE HELD, TWO FAILED

**Admitted** (the user's words: *"admit 14,15,16"*):

| Candidate | The fact, in one line | Entry |
|---|---|---|
| **C14** | Baroque scores are frequently notated one accidental short of modern practice, so the signature under-determines the tonic; the detecting signal is itself musical | `cowork_empirical_findings_candidates.md` §C14 |
| **C15** | The DCML MS3 and *When in Rome* chorale numberings are different schemes — they coincide on some pieces and disagree on others. **Pair by content, never by number** | §C15 |
| **C16** | The chorale scores carry no harmony annotation; the human analysis is a separate RomanText file, **and it carries analyst variants** — the published ground truth is not a single reading | §C16 |

**C15 is flagged as the most immediately dangerous item in the harvest**, in its own entry's words: a
wrong pairing corrupts a measurement silently and in a direction nothing downstream can detect.

**Not admitted with C14:** the handling — detect and reinterpret the signature one step, rather than
offering every score two signature families — is a DESIGN decision (**D-575**) and is not part of the
candidate.

**C17 — ROUTED AS A POINTER, NOT AN ENTRY** (the user's word: *"17=pointer"*). The fact — that no
published study reports per-axis inter-annotator agreement for Roman-numeral or key annotation of this
repertoire — **passes the gate's test cleanly**. It is not admitted as a ledger entry because it is
**already homed** at `CLAUDE.md` principle #21 and registered as **D-474**; an entry would put one fact
in two homes, which #6 forbids. **The ledger carries a pointer to its existing home instead.**

**C3, C10, C18 — HELD, each with its measurement named** (the user's words: *"held/named 3 10 18"*).
In each case a music fact plausibly sits underneath, **and in each case the source explicitly refuses
the generalization** — C3's own section banner says whether the coupling holds under the production
estimator *"is not stated here and is not asserted"*; C18's approach-level reading is one its source
does not make. **Restating these would not be stripping our vocabulary off a music fact; it would be
writing a claim the source declined to write.** The measurement each needs is stated at its entry
(§C3, §C10, §C18) and is not restated here.

**C19, C20 — FAIL the gate; nothing admitted.** Every quantity in both is a property of one arm of our
implementation, and throwing the implementation away removes the subject. **C20 is recorded as the
cleanest illustration in the harvest of why the gate is needed:** the finding is real, careful and
well established, and it is still not ledger material.

---

## Round three — THREE ADMITTED AS RESTATED MUSIC HALVES

The user's round-two ruling did not reach C8, C9 and C11; they were recorded as neither admitted nor
refused and put again. **The user's words: *"admit the three"*.**

**★ THESE THREE ARE THE ONE PLACE IN THIS RECORD WHERE THE ADMITTED TEXT IS TRANSCRIBED RATHER THAN
CITED, AND IT HAS TO BE:** the admitted sentence is a **restatement** and exists nowhere else. The
source's own sentence is NOT what is admitted. Each restatement below is the admitted text; each
entry's five fields stand at its citation.

| Candidate | **The admitted restatement, verbatim** | Entry (five fields) |
|---|---|---|
| **C8** | *A root-position major triad and the first inversion of its submediant share the bass and two of three pitch classes, so they are near-indistinguishable vertically in any major key.* | `cowork_empirical_findings_candidates.md` §C8 |
| **C9** | *The presence of a leading tone does not distinguish the genuine cases.* | §C9 |
| **C11** | *Relative major and minor name the same diatonic collection, so the chord read under one is the chord read under the other.* | §C11 |

**What was stripped, and why each restatement was needed.** C8's source sentence says the submediant
*"scores"* close to the tonic — **"scores" is our scorer's word** and the sentence as written is about
our scorer. C9's source claim is bounded by *"available at analysis time"*, which names the fields OUR
implementation computed; only the leading-tone clause is free of that bound. C11's source carries
measured percentages over *"the regions where OUR key disagreed, on OUR carried menu"*, and its
companion menu-containment figure measures how often the right key was on our list — **all of that
stays behind the barrier; only the diatonic-collection half crosses.**

**The line this round draws, recorded because it is the working rule for every future round.**
C8, C9 and C11 crossed because **the source states the music fact and merely dresses it in our
vocabulary** — stripping is a translation. C3, C10 and C18 were held because **the source refuses the
generalization**, so restating them would not be stripping but **writing a claim the source declined
to write.**

---

## Round four — the seed-list source, `DEFECT_TYPES.md`

**C21 and C22 ADMITTED** (the user's words: *"21 and 22, yes they are notstrictly about music, but
they not code either. Agree on your recommendation."*).

| Candidate | The fact, in one line | Entry |
|---|---|---|
| **C21** | A mechanism can be built and shipped while the configuration it was designed for is absent from the repertoire, or present in nearly all of it; neither is visible from the design | `cowork_empirical_findings_candidates.md` §C21 |
| **C22** | A mechanism can be correct in its body and inert in practice because its guard is satisfied by a small fraction of the cases it was written for | §C22 |

**The writing side sharpened its own recommendation before recording it, and said so.** Round four
first leaned toward routing C22 to the phase definitions as a process rule. That was **routing the
candidate by its remedy rather than by its fact**: the fact is a property of a designed mechanism
meeting a real repertoire; the remedy — count the firings, measure the pass rate — is what belongs in
the phase definitions' stop rules. **Both were recorded to the ledger on the corrected reading**, put
to the user before recording.

**C23, C24, C25 — proposed for nothing, recorded so the harvest is not silently incomplete.** C23 is
undecidable (the general claim survives; the measured divergence is one proxy in one implementation)
and its rule half is already `CLAUDE.md` **#17(d)**. C24 is a design rule about our own architecture
and already a standing decision. C25 passes the test cleanly but is **already ruled and homed** in the
governing document as a grading convention; the verdict is #6, not weakness.

**Twenty-one of the twenty-six catalog rows were routed AWAY as process antipatterns and nothing was
written into any phase definition.** Two are flagged in the harvest and are repeated here because they
bear on phases not yet run: **DT-20**, an instruction whose mandatory preconditions defeat one of its
own requirements — founding instance a required session-start read leaking exactly what a blinding
requirement withheld, **LIVE in the present arrangement**; and **DT-26**, scope-assumed enumeration,
whose founding record is four consecutive audits of one defect family each missing sites.

---

## Round five — the coding side's measurement reports

**★ THIS IS THE SOURCE WHERE THE FIFTH FIELD — THE FAILURE DIAGNOSIS — IS PRESENT AT THE SOURCE**,
which the first harvest could not obtain: these reports state not only that an approach was measured
worse but WHY, and several state why a neighbouring approach cannot substitute.

**ELEVEN ADMITTED** (the user's words: *"admit the eleven"*) — **C26, C28, C29, C30, C33, C34, C35,
C36, C37, C38, C39**, each cited at its entry in `cowork_empirical_findings_candidates.md` and each
carrying the uncertainty and establishment status that entry already states. **Nothing is upgraded and
no figure is restated (D-431).**

**Bounds that travel with three of them, named so they are not lost:** **C38**'s corpus-wide
regression claim rests on the test suites and snapshot drift, **not** on a corpus run — the change was
reverted before one; attached rule (a) applies, so what is ruled out is *aggregation-first re-analysis
as a route to the root of an arpeggiated harmony*, not the approach in every form. **C37** carries its
source's own ranking of itself as a *secondary* push. **C39** is measured over the widest population
of any candidate in either harvest.

**C27 AND C32 ADMITTED ON THEIR FACT HALVES** (the user's words: *"27 and 32 are both about (musical
chord/key) inference too, the remedy statement is about our 'software/spec development procedure'"*).
C27 crosses as *the information that discriminates an embellishment lives in the boundary placement,
not inside a flattened sonority*; the half about our pipeline does not. C32 crosses as **the
conflict** — Alberti figuration requires carrying a root across a moving bass while sustained
arpeggiation requires not re-rooting onto the passing sonority, so one continuity term cannot serve
both — and **its remedy is explicitly not admitted**, its own source stating the separating gate
*"must still be corpus-validated on both presets before any commit"*.

**C31 — HALF (b) ADMITTED, HALF (a) ROUTED TO THE PHASE DEFINITIONS.** The admitted statement: **two
opposite error mechanisms exist here — the ground-truth root absent from the sounding pitches, and our
root absent while the ground-truth root is present and strong — and a remedy for one is not a remedy
for the other.** The reverse family was the larger. Routed away: *a bucket of errors named after an
assumed cause gets trusted as a partition when it is not one*, which is about how we classify our own
errors.

**A writing-side error at this round, recorded:** C31's two halves were put to the user as *"which
half"*, which read as asking him to **select one of two mechanisms**. Both mechanisms are real; that
is the finding. The choice was only ever between two statements drawable from it. He caught the
phrasing.

**C41 ADMITTED; C40 ROUTED TO THE PHASE DEFINITIONS** (the user's word: *"yes"*).

**C41** — *where an analysis wrongly carries a root forward, the carried root characteristically
neither matches the following harmony's root nor resolves to it, while a correct reading either
continues into the next harmony or resolves to it; so the separating evidence arrives AFTER the moment
of the error, not at it.* Harmonic syntax. **Bound: three enumerated cases, stated as small by its
source**, and the mechanism already encoding part of it is gated off on exactly these sonorities
(**C33**).

**C40 routed, and the routing is the user's rule doing its work.** Its durable half — *a
structurally-predicted benefit must be graded against the prediction, and the failure mode must be
predicted too* — is a statement about our development procedure. The half that would be a ledger fact
is one mechanism's refutation, bound to the implementation tried. **Recorded beside it, because it is
to the source's credit and not against it:** C40 is measured against a **pre-declared prediction**,
which the harvest records as rare in this population and as the establishment class the Premise Gate
asks for. Good work, wrong side of the gate.

---

## THE HARVEST IS FULLY DISPOSED — the arithmetic, checked

| Disposition | Count | Which |
|---|---:|---|
| **ADMITTED** | **31** | C1, C2, C4, C5, C6, C7, C8*, C9*, C11*, C12, C13, C14, C15, C16, C21, C22, C26, C27†, C28, C29, C30, C31†, C32†, C33, C34, C35, C36, C37, C38, C39, C41 |
| Routed as a POINTER (already homed, #6) | 1 | C17 |
| HELD, measurement named | 3 | C3, C10, C18 |
| FAILED the gate | 2 | C19, C20 |
| Proposed for nothing (#6 / undecidable) | 3 | C23, C24, C25 |
| Routed to the phase definitions | 1 | C40 |

**31 + 1 + 3 + 2 + 3 + 1 = 41.** The count closes against the two harvests' 20 + 21.

\* admitted as a **restated music half**, the restatement transcribed above because it exists nowhere
else. † admitted on a **named half or bound**, with the remedy or implementation half explicitly not
admitted.

---

## ★ THE WORKING RULE THE USER ARTICULATED, RECORDED BECAUSE IT IS SHARPER THAN THE RULED SPLIT

**A fact about musical inference crosses the gate; a statement about our software or spec-development
procedure goes to the phase definitions' constraints and stop rules.**

The ruled polarity split says *design antipatterns into the ledger, process antipatterns into the
phase definitions*. That wording made the writing side route two candidates by their **remedy**. The
user's formulation locates the cut at the **subject** instead — is the statement about the music being
analysed, or about how we work — and it settled C27, C31 and C32 in one line. **Recorded as the
working rule for the remaining rounds. It is not proposed as an amendment to the ruled split; whether
it should become one is not decided here.**

---

## An error of the writing side at this round, recorded

**C6 was proposed for pulling, and the proposal was wrong.** This side compressed the candidate's
*"no reading of that content can separate them"* into *"no reading can separate them"*, dropping the
restriction to pitch-class content; the user objected that bass and context do separate the two chords
in practice, which is correct of the compressed claim and not of the candidate. This side then
proposed holding C6 — **applying a correctness filter that is not the gate's job.** The user corrected
the framing. **The candidate as written was always admissible; the defective statement was this
side's.**

---

## Still owed at this sitting

**The first harvest is now fully disposed: fourteen admitted (eleven as written, three as restated),
one routed as a pointer, three held with their measurements named, two failed.**

**The ledger itself is not built.** These 31 admissions are its **seed**, under Ruling 8, and every one
of them is re-checked at the ledger's own gate when it is built. Building it is the next act and it is
not performed here.

**★ THE ROUTED-AWAY MATERIAL HAS NOWHERE TO GO, AND THAT IS NOT A SMALL PROBLEM.** Twenty-one
`DEFECT_TYPES.md` rows, C31's half (a) and C40 are all routed to *"the phase definitions' constraints
and stop rules"*. **The phase definitions live in a frozen ratification surface**
(`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`) whose §3 is proposal text —
purpose, prerequisites, postcondition, constraints — with **no place to receive a constraint added
later**, whose banner still reads *"NOTHING HERE IS RULED"* on its first line, and whose Decisions 2–5
remain open. **This is the same wall the phase-status finding hit at the amendment-landing sitting.**
Nothing routed there by this harvest has been written anywhere, and **there is currently no artifact
that could receive it.**

**The routed-away material.** Twenty-one `DEFECT_TYPES.md` rows and C31's half (a) stand routed to the
phase definitions' constraints and stop rules, **and nothing has been written into any phase
definition**. DT-20 in particular is live now.

**The standing coverage bound on the whole exercise:** the second harvest reached **12 of 265** files
of the coding side's measurement reports. The complement is named exactly and its thirty most
promising members individually, at `cowork_empirical_findings_candidates.md` §8.2. **A continuation
resumes there and no claim of harvest completeness rests anywhere.**

**Standing bound on the whole exercise:** the second harvest reached **12 of 265** files of the coding
side's measurement reports. The complement is named exactly and its thirty most promising members
individually. **No claim of harvest completeness rests anywhere.**
