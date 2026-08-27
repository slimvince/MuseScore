# Decision surface — how the four stopped strata are settled

> **STATUS: DECISION SURFACE.** Cowork, 2026-08-27, the fifty-second session. It is a reading
> document: it sets out one decision, the alternatives, what each costs towards the project's
> objective and its ruled principles, and a recommendation. **There is no question in the turn that
> delivers it.** The choice question is put in a later turn.
>
> **Taken at branch tip `aa3077709117962ab05b27d79466bfacc77a2382`**, read by this side at
> `.git/refs/heads/master` with the file tool — the ref side. **No shell command was run against the
> repository by this side**, and `git status` was never at risk.
>
> **This is the FIRST of three decisions owed before the frame can be authored.** The other two —
> the three declared readings, and the defect in the take rule — are put in their own turns, each on
> its own surface. Nothing here settles either of them.
>
> **The author of this surface has not opened `cowork_placement_sample_sealed_2026_08_27.md`** beyond
> nothing at all: not its banner, not its §0, not one drawn item.

---

## 1. What this decision is about, explained from scratch

The project is reconstructing the specification of the harmonic-analysis module. One act of that
work is a **placement test**: you take statements from *outside* the frame — the frame being the
structure the specification is written into — and try to put each one *into* the frame. Every
statement that fits nowhere is a finding about the frame, not about the statement.

For that test you need a **sample of statements**. On 2026-08-26 it was ruled that the sample is
**stratified**: drawn separately from eight named populations, so that a failure can be reported as
*"the frame cannot hold dormancy declarations"* rather than as one pooled percentage that says
nothing about where the frame breaks. The eight populations, called **strata**, are:

| # | The stratum, in plain words |
|---|---|
| 1 | **ruling records** — the files recording what you have ruled in a sitting |
| 2 | **decision surfaces** — documents of this kind: alternatives argued towards a choice |
| 3 | **dossiers** — the long investigation write-ups |
| 4 | **the DEFERRED entries of the decisions register** — decisions taken but built later |
| 5 | **the evidence inventory** — the catalogue of what each analysis layer discovers |
| 6 | **the declared dormancies** — facts published for a named future consumer instead of removed |
| 7 | **every current heading in the specification document set** |
| 8 | **every heading ever deleted from that document set** |

On 2026-08-27 you ruled three things about how the sample is produced. In short: Claude Code
enumerates and draws but **chooses nothing** (the side that runs the test must not pick its own
examination questions); the writing side declares, **before any count is visible**, that a stratum
of 25 items or fewer goes in whole and a larger one contributes exactly 25; and the sample is
**sealed by being committed**, so the frame's author cannot have shaped the frame around it.

The dispatch went out. Claude Code enumerated all eight strata at their objects. **Four came back
drawn and sealed. Four came back STOPPED.**

A **STOPPED** stratum is not a failure of effort. The dispatch told Claude Code that if a stratum's
membership is *not determinable from a named object* — no artifact defines it, or two artifacts
define it differently — it must **not invent a definition and must not choose between candidates**.
It must report. It did that four times, on the merits, quoting the objects in each case.

**And the frame cannot be authored until you have ruled on every one of them.** That gate is your
own ruling of 2026-08-26 read plainly: a sample missing a stratum nobody ruled on is not sealed, it
is incomplete.

**So this decision is: how are those four settled.**

---

## 2. What was found, stratum by stratum

Everything in this section is stated with its source. Where this side re-established a figure at the
objects itself, it says so; where it is repeating Claude Code's measurement without being able to
verify it, it says that instead.

### 2.1 Stratum 1 — ruling records — two objects disagree, 74 against 78

Two generated tools in the repository both define this class, and they define it differently.

- **`tools/audit/gen_evidence_pin_membership.py`** matches only files named `cowork_rulings_*.md`.
  Its own run reports **74**.
- **`tools/audit/gen_artifact_inventory.py`**, the whole-tree classification, additionally admits
  four other name shapes: `cowork_ruling_`, `cowork_owner_rulings_`, `cowork_pending_rulings_`,
  `cowork_document_route_rulings_`.

**Verified independently by this side, at the directory listing rather than from the report:** the
root holds exactly **74** files matching `cowork_rulings_*.md`, and the four extra files the second
tool admits are all on disk — `cowork_ruling_guard_family_2026_08_08.md`,
`cowork_owner_rulings_2026_08_07.md`, `cowork_pending_rulings_2026_08_02.md`,
`cowork_document_route_rulings_2026_08_08.md`. **74 against 78 is confirmed at the object.**

**One asymmetry that matters and is not obvious.** The second tool's class definition — the one
admitting all five name shapes — **was put to you and ruled**, at
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` §16. The first tool's narrower
definition **was never put to you at all**.

Because a single item is *one numbered ruling inside a record*, four extra files change the item
count by much more than four, which changes the take spacing, which gives an **entirely different
draw** — not the same draw with four items added.

### 2.2 Stratum 2 — decision surfaces — no object enumerates the class

There is a directory, `ratification_surfaces/`, which the whole-tree classification names as a class
and which holds **31 files** (count re-established by this side at the directory itself). But it is
**not the population**, and that is settled at the objects rather than argued: decision surfaces also
stand at the repository root, outside that directory. This side verified four of them on disk —
`cowork_extent_decision_surface.md`, `cowork_phase1_commissioning_surface_2026_08_11.md`,
`cowork_framework_phase_opening_surface_2026_08_26.md`,
`cowork_placement_sample_surface_2026_08_27.md`. The last two are *this phase's own* surfaces.

**A route that looks obvious and is closed, checked at the object so it is not proposed later.**
Defining the class by the word *surface* in the filename over-admits: the same listing shows
`cc_instruction_oi179_reply_and_phase2_surface.md`, which is a dispatch to the coding side, and
`cowork_rulings_2026_08_17_governing_surface_split.md`, which is a ruling record. **A filename
signature cannot carry this class.**

**A hazard in the other direction, named as a hazard and not asserted as a fact.** Several of the 31
files in that directory read *by name* as ratification queues or as readings rather than as documents
that argue alternatives towards a choice — `cowork_decisions_pending_ratification*.md`,
`cowork_ruling_registration_queue_2026_08_09.md`, `cowork_pending_ratifications_next_session.md`,
`cowork_sizing_tests_reading.md`, and others. **This side has not opened them and does not assert
what they are.** It matters only because it means "the whole directory plus the four root files" may
admit documents that are not decision surfaces, and whoever writes the membership must know that
before writing it.

### 2.3 Stratum 3 — dossiers — no defining artifact, and the unit has no determinable form

**Two independent obstacles, and the second is the harder one.**

*Membership.* The only whole-tree, user-ruled classification of every file in the repository has **no
dossier class**, deliberately: it sorts by path and extension only, and says in terms that a
signature which has to open a file is one that can be argued about. It mentions dossiers only inside
the descriptions of two catch-all classes. The one remaining candidate is the filename convention
`*_dossier.md`, which nothing in the record establishes. **Verified by this side at the listing: it
matches 26 root-level files**, and one of them —
`cc_instruction_stage3_4i_gate_retirement_dossier.md` — is simultaneously a **dispatch** under the
ruled classification and a **dossier** under the convention.

*The unit.* The dispatch declared one item to be *"one claim or finding entry in a dossier"*. **No
dossier declares such a thing as its unit of record.** Claude Code opened two to check and reports
they use unrelated structures — one is two lettered Parts, the other numbered task sections with
sub-sections. So even if you ruled the membership today, the items still could not be enumerated.
*(Relayed from the report; this side did not open either dossier.)*

### 2.4 Stratum 6 — declared dormancies — the concept is ratified, the population does not exist

The concept is ratified at `CLAUDE.md:251-255`: a fact consumed by no one is either a **declared
dormancy**, with its future consumer named, or **waste**, and is removed.

**No artifact enumerates them, and no generator writes one.** Three candidate readings exist and they
disagree about the *subject*, not merely the extent:

1. the evidence inventory's own DORMANT-status rows together with its §8b list of future consumers
   you named on 2026-07-13 — a set of rows inside one document;
2. the free-text declarations scattered through `ARCHITECTURE.md`, dispatches, reports and audit
   dispositions, **with no marker convention to find them by**;
3. a per-document `live_or_dormant` property in the specification document set — a **different
   subject** (whether a *document* is dormant, not whether a published *fact* is), named here only so
   it is explicitly ruled out rather than rediscovered and used.

**Reading 2 cannot be enumerated at all without first building a marker convention.** That is
construction work, not a ruling.

---

## 3. What this decision is judged towards

Four things, all of them already ruled or already stated by you.

**(a) The test must not be able to be shaped by the side being tested.** Your ruling of 2026-08-27.
It is why the writing side declares the selection and Claude Code applies it.

**(b) A declared number must be citable as declared, never as measured.** Your ruling of 2026-08-27
about the threshold of 25. Whatever is declared here inherits that obligation.

**(c) A statement that must be interpreted before it can be placed is not a statement.** The
dispatch's own rule for the sealed file. It is the reason a stratum with no determinable unit is a
real obstacle and not a formality: an item that has to be *construed* into existence tests the
construer, not the frame.

**(d) The standing bar against work pitched at too high a meta level** — your words, twice in
successive sittings. Building a durable taxonomy of the project's own document kinds is exactly the
kind of act that bar catches. **The placement test needs a population, not a taxonomy.**

---

## 4. The alternatives

### Alternative A — declare a membership and a unit per stratum, **for this sample only**

The writing side writes into the next dispatch, for each of the four stopped strata, an explicit
membership and an explicit unit, and states on the face of the declaration that it governs **this
sample and nothing else** — it is not a class definition, nothing else in the project may cite it,
and it expires when the sample is drawn. You rule on the four declarations. Claude Code then
enumerates and draws them mechanically, exactly as it did the other four.

**Towards the objective.** The frame's gate opens in one sitting. All eight strata are present, so
the placement test reports coverage across the whole population the plan named.

**Towards (a).** Preserved, and this is worth being precise about. At the level of a **file count**,
three of the four are now visible: 74-or-78 ruling records, 35 candidate decision-surface files, 26
dossier files. At the level of an **item count** — which is what the take rule consumes — **nothing
is visible for any of the four.** So the declaration is still made blind to the numbers that could
be shaped. **This is a real weakening of the property, and it is smaller than it looks; it must be
declared on the face of the dispatch and not glossed.**

**Towards (c).** This is where A is genuinely weak. For stratum 3 the unit does not exist in the
documents, so declaring one is **inventing** the item rather than finding it. Whatever is declared,
the resulting items are units of *this side's* making.

**Towards (d).** Respected — a sample-scoped declaration is not a taxonomy, and it is one sitting.

**Cost.** One sitting for you, plus one dispatch. It leaves the underlying defect — that four of
this project's own document classes have no population — entirely uncured, and the next act that
needs any of these four classes will meet it again.

### Alternative B — build the missing objects first, then draw

Cure the defect properly: extend the ruled whole-tree classification to carry a decision-surface
class and a dossier class; build a marker convention for declared dormancies and sweep the record
for them; rule which of the two ruling-record definitions is the project's, and make the other agree.
Then re-run the enumeration and draw all four strata from real objects.

**Towards the objective.** Strongest sample of the three, and the only one that removes the defect
rather than routing around it. Every later act that needs these classes inherits the cure.

**Towards (a) and (c).** Both fully preserved. The items would be found, not declared.

**Towards (d).** **This is where B fails, and it fails hard.** It is governance work about the
project's own records, several sittings deep, with the frame — the actual deliverable — blocked
behind all of it. The dormancy marker convention alone is a sweep of the whole record. **This is the
shape of act your standing bar names.**

**Cost.** Several sittings, at least one dispatch per piece, and the frame does not move until they
are done.

### Alternative C — drop the four stopped strata; run the test on the four that were drawn

Rule that the sample is the 96 items already sealed, record the four stopped strata as a declared gap
on the frame's face, and proceed.

**Towards the objective.** Cheapest and fastest by a wide margin: the gate opens today.

**And the reason this side does not recommend it.** Look at what the four drawn strata are —
register entries, inventory rows, current headings, deleted headings. **They are the project's
mechanical records.** The four stopped strata are the project's *governance* records: rulings,
decisions, investigations, dormancy declarations. **The frame is most likely to fail exactly where
the statement is a governing one**, and dropping these four removes precisely that half of the test
while leaving a number that reads like a whole result. A pass rate computed over headings and
register rows would be reported per stratum, honestly, and still be read as *the frame holds* by any
successor skimming it.

**Cost.** Low in effort, high in what it silently gives up.

### Alternative D — draw the four from a proxy population

Instead of defining the four classes, draw from the catch-all classes the ruled classification
already carries — *"every other repository-root file beginning `cowork_`"* and *"every other
repository-root file beginning `cc_`"*.

**Towards the objective.** Weak. Those classes mix designs, audits, dossiers, plans, inventories and
findings by path and extension alone. A result from them cannot be reported as *"the frame cannot
hold rulings"*, which is the entire reason the sample was stratified. **It buys coverage and spends
the property that made coverage worth having.** Named here so it is not proposed later as new.

---

## 5. Recommendation

**Alternative A, with one stratum settled differently from the other three.**

The ground: B is the correct engineering answer and the wrong answer for this moment — it blocks the
deliverable behind several sittings of work about the project's own paperwork, which is the act your
standing bar was stated against. C is affordable and quietly guts the half of the test most likely to
produce a finding. A opens the gate in one sitting and pays for it with a declared, bounded,
sample-scoped weakening that is visible on the face of the dispatch and expires with the draw.

What A would declare, per stratum, if it is ruled:

**Stratum 1 — ruling records.** Membership: **the ruled definition, all five name shapes, 78 files.**
Unit unchanged: one numbered ruling in a record. The ground is not that 78 is better than 74; it is
that one of the two definitions **was put to you and ruled** and the other never was, and a ruled
definition beats an unruled one on its face without anyone having to weigh them.

**Stratum 2 — decision surfaces.** Membership: **an explicit list of file paths written into the
dispatch by name** — the 31 files under `ratification_surfaces/` plus the four root-level surfaces —
rather than any signature, because a filename signature is verifiably wrong here. Unit: one numbered
decision in the surface. **With this attached, because §2.2 found it:** the dispatch instructs Claude
Code that a listed file containing **no numbered decision** contributes zero items and is reported as
such, never construed into having one. If several report zero, that is a finding about the directory,
and it is the honest way to learn that the directory is not the class.

**Stratum 3 — dossiers.** Membership: **the 26 root-level `*_dossier.md` files**, with the one
collision — `cc_instruction_stage3_4i_gate_retirement_dossier.md`, which is also a dispatch —
**excluded and named**, since the ruled classification already places it elsewhere: 25 files. Unit:
**every markdown list item at any nesting depth**, the same reading Claude Code took for the evidence
inventory, so that the two strata are read the same way and the difference between their results
means something. **Declared with it, because it is the weakest thing in this surface:** a list item
is not what the dispatch meant by *"one claim or finding entry"*. It is a mechanical stand-in for a
unit that does not exist in the documents, it will over-admit ordinary prose bullets, and a
*placeable* result from this stratum is therefore weak evidence — which the placement report must say
where it reports stratum 3, in the same way it must for the two strata that overlap the frame
author's own reading.

**Stratum 6 — declared dormancies. This one is settled differently: record it as NOT ENUMERABLE, and
record that as a finding.**

The reason is arithmetic rather than judgement. Reading 1 is the only reading enumerable from a named
object today — and its rows sit **inside the evidence inventory**, which is already stratum 5, drawn
as *every markdown list item at any depth*, `N = 33`. **So reading 1 is a subset of a stratum already
in the sample.** Drawing it would spend a stratum to re-ask a question stratum 5 has already asked,
and would double-count those items across two strata that Ruling 3 of 2026-08-26 requires be reported
separately. Reading 2, the one with real coverage, cannot be enumerated without first building a
marker convention — Alternative B's work, in a single stratum. Reading 3 is a different subject.

**And the empty result is worth more than the redundant draw.** This project ratified declared
dormancy as a governing concept on 2026-07-10 and has never built a population of it. The dispatch's
own rule says an empty stratum is a finding about the records and must be visible rather than absent.
**Recording stratum 6 as unenumerable, with the three readings and why each fails, is that finding.**

*The alternative on this stratum, named so it is not lost:* take reading 1 anyway, accept the overlap
with stratum 5, and declare it. It buys the appearance of eight strata drawn. It is not recommended.

---

## 6. What this surface does NOT decide

- **The three declared readings** — how a "row" of the evidence inventory, a "member" of the document
  set, and a "markdown heading" are read. Those are put on their own surface, in their own turn.
- **The defect in the take rule** — that for a stratum between 26 and 49 items the rule collapses to
  the first 25 in order, contiguously, and always leaves an unreachable tail correlated with content.
  That is the third surface, and **its correction requires a redraw of strata 5, 7 and 8**, which is
  why it is put last: what this surface adds and what that one redraws are then a single dispatch.
- **Whether the sealed sample is reopened.** Between this decision and the third, a redraw of the
  drawn strata plus the addition of the stopped ones is very nearly a whole new sample. That is the
  honest position, it is stated here so it is not discovered later, and it is not put as a question:
  it is a consequence of the other three answers, not a choice of its own.
- **Nothing is landed in git by this session.** No ruling record exists for this surface until you
  rule. No register entry, no open-items row, no finding number. The three standing red guards are
  untouched and the register blocker is untouched.

---

## 7. Method — what this side did, and the limit it still has

**Read whole:** `cc_report_placement_sample.md`, `cowork_rulings_2026_08_27_placement_sample_sitting.md`,
`cc_instruction_placement_sample.md`, and the top entry of `cowork_handoff.md`. All through the file
tools on a bridge-staged snapshot, staged path by path.

**Re-established at the objects by this side, not taken from the report:** the branch tip at the ref;
the 74 root-level `cowork_rulings_*.md` files; the on-disk existence of all four extra ruling-record
files; the 31 files in `ratification_surfaces/`; the four root-level decision surfaces; the 26
root-level `*_dossier.md` files and the one dispatch among them; and that a filename signature on the
word *surface* also admits a dispatch and a ruling record.

**★ THE VERIFICATION LIMIT, STATED PLAINLY AND UNCHANGED FOR A NINTH SESSION.** This side cannot
resolve a commit or a blob without a shell, and does not have one. **Every figure taken from a git
object — the two batch commits, the blob sizes, the 279-commit history walk behind stratum 8, the
guard counts — is RELAYED from Claude Code's report, not verified.** What this side did check on that
side is one arithmetic consistency: the tip at the ref is neither of the two commits the report names,
which is what the report's declared third act predicts.

**Not opened by this side:** `cowork_placement_sample_sealed_2026_08_27.md` in any part, `CLAUDE.md`,
`ARCHITECTURE.md`, `DECISIONS.md`, any source file, any measurement output, any boot pack, any
dossier, any file in `ratification_surfaces/`, any PDF in the research folder.

**This session is barred from authoring the frame** on the standing ground that it has read the
handoff and is therefore aware of the material the frame's author must be blind to.
