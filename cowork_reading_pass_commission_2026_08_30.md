# The primary-source reading pass — commission (2026-08-30)

> **STATUS: COMMISSIONED, NOT STARTED.** Written by the Cowork writing side on the user's Ruling 2
> of `cowork_rulings_2026_08_30_detail_phase_opening_sitting.md`. This document is the
> self-sufficient instruction for the pass; the user opens it with the fresh session(s) of his
> choice (the 2026-08-26 role ruling: the writing side writes instructions to disk and never
> starts the sessions that run them). It executes an existing ruling and takes no new decision;
> where a step below reaches a question the record does not settle, that is a STOP to the user.

## 0. Boot — read before any other act

You start clueless, and a single-file opening instruction is not an exemption from the standing
conventions (`CLAUDE.md` Conventions, the ordinary-session-start-read rule, ratified 2026-08-29).
In order:

1. The ordinary session-start read: `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, and the
   derived gating answer (`tools/audit/nongating_apparatus_rows.json` →
   `★_the_live_gating_answer` → `gating_ids`).
2. `cowork_rulings_2026_08_30_detail_phase_opening_sitting.md` — the two rulings this pass
   executes: the detail-specification phase is OPEN, and this pass is its FIRST ACT.
3. `FRAMEWORK.md` §9 (the design points), §11 (the risks R-1..R-10), and §5 (the layer charters).
4. `cowork_research_list_disposition_surface_2026_08_29.md` whole — the pass's population is
   derived from it (§2 below).
5. This document, whole.

**Standing rules that bind every session of this pass:** working-tree files are read with the
file tools, never through a shell (D-253); no self-invented jargon — plain words, the repository's
own names; music-theory words keep their music-theory meaning; nothing is asserted from memory
where a documented source exists; every session lands its work on disk before it closes (the
detail-specification phase's own record rule — a session that ends with work only in its context
has lost it).

**What this pass is NOT licensed to do:** derive any specification; amend any document; open any
code path as design input (the detail phase's NOT-ALLOWED clause: no implementation-derived
material); change any measurement tool, gate, golden, corpus or anything under `tools/corpus/` or
`tools/robust_stop/`; open the workbook at
`external resarch summary/external research.xlsx` (its ruled classification: never opened by
sessions or batches, never amended); write any open-items row or register entry (the register
rule-(c) suspension stands — findings are recorded in this pass's own output files and routed).

## 1. Purpose, in one paragraph

The ratified framework (`FRAMEWORK.md`) was derived from sources read on our side, and it
survived a falsifier search over the user's external research list — but that search ran on the
list's RELAYED evidence, and the framework's own risk list declares unread territory (R-7, R-8,
R-9). The user has ruled (guiding principle #1 applied): held-but-unread research is not a
knowledge base. This pass reads the unread at the primary source, verifies the figures the chosen
design points rest on, and delivers the findings in a form that lets the architecture be judged
as a WHOLE — coupled choices, chains against chains — before any detail specification is derived
inside the frame.

## 2. Task 1 — derive the reading population

Derive, do not hand-pick. The population comes from three sources, each already on disk:

- **(a) The unread classes**, as `cowork_research_list_disposition_surface_2026_08_29.md` §1
  names them: the McLeod & Rohrmeier family; the executable grammar and ontology branch
  (HarmTrace, the functional and modal harmony ontologies, the representation ontologies); the
  mode branch; the recent and multilingual items (BACHI, the 2020 local-keys evaluation
  methodology, Hu & Arthur 2021, the German and French branches). The historical-lineage class
  (item 5 of that section) is EXCLUDED by the ruling — declined as scope on #2.
- **(b) R-7's named unread alternatives** (`FRAMEWORK.md` §11): multi-resolution tonality,
  time-span reduction trees, tonality in a transform space; **R-8**: the tonality-profiles
  primary not on disk; **R-9**: the annotation-ceiling paper whose named file contains a
  different paper — the true paper is to be fetched and read.
- **(c) The load-bearing citation list**: enumerate from `FRAMEWORK.md` every measured figure a
  CHOSEN design point's defense cites (the [FACT] tags of §4, §5 and §9 — for example the
  tonality/chord separation costs, the segmentation-given-versus-found accuracies, the
  multi-task incoherence figures, the metric-versus-likelihood fitting comparison). Each such
  figure names a verification target: the primary paper and the claimed value.

Identify each primary from the names, authors and row citations the disposition surface itself
carries. **Where a primary cannot be identified from those, STOP and put the item to the user —
never open the workbook to find it.** Record the derived population as a file
(`reading_pass/population.md`, one row per paper: what it is, which class admitted it, which
design points it bears on) BEFORE any fetching or reading, and land it.

**Candidacy upgrades (coverage follows load, not novelty):** while reading, any paper — including
one of the fifty-eight at `docs/research_papers/` whose first read was abstract-and-method — that
turns out to be a live algorithm candidate for any detail specification is ADDED to the
population and read whole. An addition is recorded in the population file with its reason.

## 3. Task 2 — fetch or flag

- New fetches land under `docs/research_papers/reading_pass_2026_08/`, one file per paper, named
  by author-year-short-title. Nothing is added to `BIBLIOGRAPHY.md` itself by this pass; a
  companion file `reading_pass/additions.md` records what was fetched, from where, and when, so
  the bibliography can be reconciled later as its own act.
- A paper that cannot be fetched (paywall, dead link, unidentifiable) is FLAGGED in the
  population file and **nothing is carried out of it** — no equation, no figure, no claim from a
  secondary description without saying so at every use (the theory-grounding corollary,
  `CLAUDE.md`). An unfetchable paper is a recorded gap, not a blocker.

## 4. Task 3 — read and extract

Every population paper is read WHOLE. Per paper, one extraction file under
`reading_pass/extracts/`, carrying:

- **Claims, labeled** FACT (stated or measured in the paper, with its location), THEORY
  (established published theory), or CONJECTURE — nothing unlabeled carries load later.
- **Coupling facts, mandatory** (the user's ruled widening): what the method ASSUMES about its
  upstream (its stated input requirements), what it HANDS downstream (its outputs and their
  form), and its own STATED SCOPE and limits — because choices are evaluated as chains, and a
  method's admissibility at one layer depends on what its neighbours must then be.
- **Measured results**, with corpus, metric and value as the paper states them.
- **CENTRAL sources** — any paper whose claims would carry load in a detail specification or
  against a design point — are extracted in a SECOND independent pass (a fresh session, or a
  cleanly separated re-read that does not consult the first extract) and the two extracts
  cross-checked; disagreements are resolved at the paper or recorded as unresolved. The
  population file marks which papers are central.

For the load-bearing citation list (Task 1c): verify each claimed figure at its primary and
record VERIFIED (with location), DIVERGES (with both values — this is a STOP, see §6), or
UNVERIFIABLE (paper unfetchable or figure not found).

## 5. Task 4 — the findings surface

One document, `cowork_reading_pass_findings_<date>.md`, delivered to the user, organized by the
framework's own structure, not paper by paper:

- **Per design point of `FRAMEWORK.md` §9** (chosen, underived and routed alike): what the pass
  found, with the verdict vocabulary of the disposition surface — SUPPORTS / ENRICHES /
  RIVAL-SHAPED / NO BEARING — and, where anything approaches CONTRADICTS, the full case stated
  (see §6 first).
- **Per interface** (the §5 boundary contracts): the candidate algorithm CHAINS the read material
  supports — which methods compose with which, on their own stated assumptions — so the
  architecture can be compared as a whole against rival wholes. Where the read material exhibits
  a chain the ratified frame cannot express, that is stated plainly as such.
- **The verification table** for the load-bearing figures (Task 1c's outcomes).
- **The routed extracts**: which FACT-labeled findings feed which detail specification, which
  feed measurement design, which feed the style system — so the detail phase starts with its
  primary-read debt pre-paid.
- **The bound**: what was NOT read (the flagged unfetchables, the excluded historical class),
  stated so the surface's own coverage is never overstated (DT-26).

## 6. STOPs — surface, never absorb

- **A falsifier candidate against any CHOSEN design point** — a primary-read measurement or
  stated result that contradicts a chosen point's recorded ground — is a STOP: the finding is
  written up on its own and put to the user before the pass continues past it. The frame stays
  ratified; the amendment mechanism is the ruled route; this pass amends nothing itself.
- **A DIVERGES verdict on a load-bearing figure** is the same STOP in its measurement form.
- **A population item unidentifiable without the workbook** — STOP to the user.
- **Anything that would require opening code, changing a document, or writing a register row** —
  STOP; it is outside this pass's licence.

## 7. Session discipline

The pass may span several sessions (the user: "If necessary we should let a fresh LLM session do
it"). Each session: boots per §0; takes a bounded slice of the population; lands its extraction
files and an updated population file before closing; and stops at a member boundary, recording
what was done, what was not, and that the remainder is untouched (the ruled stop form). The
cadence is the context protection — a session that feels its context thinning closes at the next
boundary by choice rather than being compacted mid-paper.

## 8. Done

The pass is DONE when: every population row is read-whole, flagged-unfetchable, or
stop-reported; central papers carry cross-checked double extracts; the verification table has a
verdict per load-bearing figure; and the findings surface is delivered. The user then rules on
its findings; the first-deriving-subject decision (deferred at Ruling 2) returns after that
ruling; and the whole-architecture coherence review waits at the phase's far end, where the
derived specification set is ratified as a chain.

---

*Provenance: written by the Cowork writing side, 2026-08-30, executing Ruling 2 of
`cowork_rulings_2026_08_30_detail_phase_opening_sitting.md`. No count of the population is stated
here because the population is derived, not hand-listed (#17f, D-431). This document takes no
decision; every choice it encodes is quoted from or pointed at a ruled source.*
