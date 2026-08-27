# Decision surface — the three declared readings

> **STATUS: DECISION SURFACE.** Cowork, 2026-08-27, the fifty-second session. It is a reading
> document: one decision, the alternatives, what each costs towards the objective and the ruled
> principles, and a recommendation. **There is no question in the turn that delivers it.** The choice
> question is put in a later turn.
>
> **Taken at branch tip `aa3077709117962ab05b27d79466bfacc77a2382`**, read at `.git/refs/heads/master`
> with the file tool. No shell command was run against the repository by this side.
>
> **This is the SECOND of three decisions.** The first — how the four stopped strata are settled — is
> ruled and recorded at `cowork_rulings_2026_08_27_stopped_strata_sitting.md`. The third, the defect
> in the take rule, is put in its own turn afterwards. Nothing here settles it.
>
> **★ A DELIBERATE ABSTENTION, DECLARED AT THE TOP BECAUSE IT SHAPES EVERY RECOMMENDATION BELOW.**
> This side has **not opened** `cowork_evidence_inventory.md`, `ARCHITECTURE.md`, or any other
> document-set member, and will not before this decision is ruled. Choosing how an item is counted
> **while looking at the items** is the same defect your ruling of 2026-08-27 protects the sample
> against — the side that decides the selection must not be able to see what its decision admits.
> The counts are already visible and that hazard is declared; opening the documents would go a
> step further. **Every recommendation below is therefore argued from the wording and the principles,
> never from the content.**

---

## 1. What this decision is about, explained from scratch

The placement sample is drawn from eight populations, called **strata**. For each, the dispatch
declared what **one item** is — the *unit* — because that is a selection choice and therefore not
Claude Code's to make.

In three places the declared unit turned out to admit **more than one mechanical reading**. Claude
Code did not stop on these, and it was right not to: a stop was ordered where a stratum's
**membership** is undeterminable, and in all three of these the membership is perfectly determinable.
It is the *rendering of the unit* that is open. So it took, in each case, **the reading that adds no
judgement of its own**, named the alternative, and reported what the alternative would change.

**All three are yours to confirm or overturn.** They are put together because they share one shape
and one hazard, not because they are one question.

**The hazard they share, and it is why this surface argues the alternatives at full strength.** All
three recommendations below are to **confirm** the reading Claude Code took. A decision whose
recommendation is *"confirm everything"* invites being waved through. **One of the three genuinely
turns a stratum from a sample into a complete census and would change its drawn set entirely**, so
the case for each alternative is put as strongly as this side can put it, and the ground for
preferring the taken reading is stated as a ground rather than as a preference for the status quo.

---

## 2. Reading one — what a "row" of the evidence inventory is

**The stratum.** `cowork_evidence_inventory.md`, one document: the catalogue of what each analysis
layer discovers. It is a member of the specification document set by a delegation
`ARCHITECTURE.md` makes to it.

**The declared unit was "one inventory row".** **The document contains no table.** Claude Code
reports that a search for a line beginning with a table pipe returns zero matches; its records are
markdown list items. So the declared unit does not exist in the document and something has to stand
in for it.

**The reading taken: every markdown list item at any nesting depth. `N = 33`.**
**The alternative: top-level list items only. `N = 24`.**

**What the alternative changes, and it is not a detail.** The threshold is 25. At `N = 33` the
stratum is a **take** — 25 items drawn from 33 by a spacing rule. At `N = 24` the stratum falls at or
below the threshold and becomes a **census**: the whole stratum goes in, and **no uncertainty range
is needed for it at all**. The drawn set is not "the same minus some"; it is a different set.

**Two facts Claude Code reports about the document's shape** *(relayed; this side has not opened the
document)*: 24 items sit at the top level and 9 are nested one level; and **two of the 24 top-level
items are bare labels that introduce nested items** rather than records in their own right, at lines
100 and 123.

### The case for the alternative — top-level only, `N = 24`, census

A census is the strongest form of evidence this sample can produce for a stratum. Your ruling of
2026-08-26 stratified the sample precisely so that a finding could be reported per stratum rather
than pooled, and a stratum taken **whole** yields a finding that carries no uncertainty range to be
argued about later. If the inventory's records really are its 24 top-level items — with the nested
items being sub-details of those records rather than records — then the narrow reading is both truer
to the word *row* and cheaper in evidence terms. **This is a serious case and it is not dismissed
below.**

### The case for the taken reading — every item at any depth, `N = 33`

**It adds no judgement.** The narrow reading requires a proposition nobody has established at an
object: that a nested item is a sub-detail rather than a record. Nothing in the document's own text,
and nothing in any generated artifact, says so.

**And the narrow reading is demonstrably imperfect on its own terms.** It admits two items that are
**bare labels** — not records of anything — while excluding nine items that may well be records. So
the choice is not "the clean reading against the messy one"; it is between two readings that each
mis-sort something, one of which requires an unestablished judgement to reach.

**★ The decisive ground, and it is a ground about us rather than about the document.** The two
readings' counts are now visible, and one of them lands the stratum below the threshold. **Preferring
`N = 24` now cannot be separated from preferring it because it makes the stratum a census.** That is
the sample being shaped by a side that can see the numbers — the exact property Ruling 1 of
2026-08-27 exists to protect, arriving through a different door. The taken reading was fixed by a
rule applied blind; the alternative would be chosen sighted.

**One thing that lowers the alternative's price and is stated so the case is not overstated.** The
third decision, put in the next turn, proposes replacing the take rule with a formula that spreads a
draw properly across a stratum. Under it, a 33-item stratum drawn to 25 is a well-spread take rather
than a contiguous first-25. **The census advantage of `N = 24` shrinks once that is fixed.**

**Recommendation: confirm the taken reading. Every markdown list item at any nesting depth,
`N = 33`.**

---

## 3. Reading two — what a "member" of the document set is

**The strata.** 7, every current heading in the specification document set, and 8, every heading ever
deleted from it. The document set is a **derived** membership — `ARCHITECTURE.md`, every document it
delegates to in an admitted form, and `docs/scoring_model.md` — and it currently holds **26**
members *(relayed from the report)*.

**The declared unit was "one markdown heading in a current member of the document set".** The
question is what *in a member* reaches.

**The reading taken: every heading in the member FILE.**
**The alternative: only the headings inside the member's delegated sections.** Several members carry
a recorded `delegation_scope` of `sections` rather than the whole file, and `ARCHITECTURE.md` itself
is recorded as scoped to three named regions.

### The case for the alternative — delegated sections only

A member document may cover more ground than was ever delegated to it. Headings in its
non-delegated parts are **not part of the specification the frame has to be able to hold**. Placing
them and finding them unplaceable would produce a finding about the frame that the frame does not
deserve — a false positive, and false positives in a test whose whole output is *"the frame cannot
hold X"* are the expensive kind of error.

### The case for the taken reading — the whole member file

**The wording says so.** The stratum's own text, in the successor plan's §6.2, is *"every current
heading … from the document set"* — the document set, whose membership field is a **file path**. The
`delegation_scope` field governs how far a delegation **reaches**; it is not recorded as a boundary
on what the file is. Reading it as a population boundary is a judgement nobody has ruled.

**★ And the alternative has a consequence that is close to disqualifying.** `ARCHITECTURE.md` is
recorded as scoped to three named regions. Under the narrow reading **the project's own architecture
document contributes only those three regions' headings** and stratum 7 collapses towards a
population that excludes most of the specification's spine. *"Every current document heading"* cannot
plausibly mean that.

**How the alternative's real worry is answered without paying for it now.** The concern — that an
unplaceable heading might lie outside any delegated scope — is **checkable after the fact**: the
scope data sits in the same generated artifact the membership comes from, so the placement report can
be re-read against it if a material share of unplaceable items turns out to lie outside delegated
regions. **Nothing is lost by taking the wide reading now; something is lost permanently by taking
the narrow one.**

**Recommendation: confirm the taken reading. The whole member file.**

---

## 4. Reading three — what counts as a "markdown heading"

**The strata.** 7 and 8 again.

**The question.** A line beginning with one to six `#` characters is a markdown heading — except when
it is inside a fenced code block, where `#` opens a shell comment.

**The reading taken: fence-aware — code blocks excluded. `N = 730` current, `59` deleted.**
**The alternative: naive — every matching line. `N = 737` current, `60` deleted.**

**The seven extra lines are all shell comments in `ARCHITECTURE.md`**, at lines 896–907 and
7794–7797; the one extra deleted line is `# Full corpus` at `ARCHITECTURE.md:2523` in a historical
version *(relayed from the report; this side has not opened the file)*.

### The case for the alternative — naive

Only one: it needs no fence tracking, so it cannot be got wrong by a mis-implemented tracker that
silently swallows real headings. That is a real risk and it is the whole of the case.

### The case for the taken reading — fence-aware

**Claude Code reports that under the naive reading two of those shell comments actually landed in the
drawn sample**, at ordered positions 30 and 262. **A shell comment is not a statement of the
specification.** Asking whether the frame can hold `# Full corpus` tests nothing, and a placement
report containing such items is discredited by them.

**And the alternative's one worry is answerable by inspection rather than by trust.** The difference
between the two readings is **eight lines in total across both strata**, and every one of them is
enumerated by file and line in the report. **They can be checked by eye.** A fence tracker that
swallowed real headings would show up as a larger difference than eight.

**Recommendation: confirm the taken reading. Fence-aware, `730` and `59`.**

---

## 5. What follows if all three are confirmed

**No redraw is caused by this decision.** All three recommendations confirm what Claude Code took, so
strata 5, 7 and 8 stand as drawn *by this decision's account of them*.

**They do not stand for another reason, and it is the third decision's.** The take rule has a defect
that forces strata 5, 7 and 8 to be redrawn regardless of what is ruled here. **So confirming these
three readings does not close the sample; it fixes the definitions that the redraw will then be
performed against.** That is the honest order: settle what an item is, then settle how items are
taken.

**If any of the three is overturned instead**, the affected stratum is redrawn under the new reading
— and because the redraw is happening anyway, **overturning one costs no extra dispatch.** That is
stated so the recommendations are not read as being argued from convenience: at this moment in the
sitting, changing a reading is close to free.

---

## 6. What this surface does NOT decide

- **The take rule's defect and the redraw it forces.** Third surface, next turn.
- **Anything about stratum 3's unit**, which was declared in Ruling 1 of this sitting and is not
  reopened here.
- **Anything durable.** These are readings of the units for this sample. No class definition, no
  amendment to any tool, no register entry, no open-items row, no finding number. Nothing is landed
  in git by this session.

---

## 7. Method

**Read whole for this surface:** `cc_report_placement_sample.md`,
`cowork_rulings_2026_08_27_placement_sample_sitting.md`, `cc_instruction_placement_sample.md`, and
the top entry of `cowork_handoff.md`. All through the file tools on a bridge-staged snapshot.

**Deliberately not opened, per the abstention declared in the banner:**
`cowork_evidence_inventory.md`, `ARCHITECTURE.md`, any other document-set member, and any part of
`cowork_placement_sample_sealed_2026_08_27.md`. Also not opened: `CLAUDE.md`, `DECISIONS.md`, any
source file, any measurement output, any dossier, any boot pack.

**★ THE VERIFICATION LIMIT, UNCHANGED.** This side has no shell and cannot resolve a commit or a
blob. **Every figure in §§2–4 that comes from a git object or from a file this side has not opened —
the counts 33, 24, 730, 737, 59, 60, the 26 members, the line numbers, the two shell comments in the
drawn set — is RELAYED from Claude Code's report and is not verified here.** The recommendations are
argued so that they do not depend on those figures being exact: each turns on the wording of a
declared unit or on a principle already ruled, not on a count.
