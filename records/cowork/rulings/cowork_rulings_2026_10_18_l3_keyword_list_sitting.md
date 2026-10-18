# Rulings — the L3 keyword-list sitting, 2026-10-18

> **STATUS: RULING RECORD.** Cowork, 2026-10-18 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_two.md`. An interim carrier under the standing
> clause that a sitting record is written in the turn its ruling is given and lands in git at the next dispatch's
> Task 0. **No act of this sitting is a commit to git.** `.git/refs/heads/master` and
> `.git/refs/remotes/origin/master` both read `986b9663085c4ab21c6a4d3f3957b3fbe9d45b23`, read as files with the file
> tools over staged copies; `.git/logs/HEAD` names it the end-state commit of
> `records/cc/instructions/cc_instruction_l3_keyword_count_2026_10_17.md`.

---

## 0. What was put, and in what form

One decision: the **membership of the L3 keyword list** — item 3 of the L3 outgoing-population ruling
(`cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md` §2, Option B), the list whose search over the 26
members of `tools/audit/specification_document_set.json` admits passages into the L3 comparison. The surface was
delivered as user-visible text in one turn, self-contained, carrying no question; its check at its sources was
delivered as a turn of its own (nine corrections, none moving the recommendation; §3); the choice question was then
put alone in a later turn, no widget. **The user's word: "B".**

## 1. Why the question was the user's

Option B item 3 of the 2026-10-17 ruling states that the writing side drafts the list and *"the user rules its
membership as its own decision before the population dispatch is written."* The count taken before it is put follows
the L2 precedent (Ruling 83's owed count, §3cl, and Ruling 86, §3co, of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`), as entry 422 recorded.

## 2. Ruling — Option B

**L3's keyword list is these 26 terms, and no others:**

*The 21 core terms kept:* `cadence`, `cadential`, `plagal`, `phrase end`, `phrase boundary`, `phrase grouping`,
`grouping layer`, `chord symbol`, `chord-symbol`, `chordsymbol`, `bass note`, `slash chord`, `root pitch class`,
`inversion`, `figured bass`, `figured-bass`, `thoroughbass`, `harmonic rhythm`, `harmonic-rhythm`, `harmonicrhythm`,
`read-off`.

*The 5 counted-in-context terms kept:* `phrase`, `grouping`, `period`, `contradiction`, `deceptive`.

**Excluded:** `continuo` (28 of its 30 in-set hit lines are *continuous* / *continuously*; of its two whole-word uses one
is also hit by `figured bass` and `bass note`), `sentence` (its four musical in-set lines are four of the lines
`period` adds; the other 29 it adds are the grammatical sense), and `bass` (of the 396 in-set lines it adds beyond the
core terms, about 40 bear on L3's five facts by this side's reading; the rest concern how L2 decides the chord, the
bass-is-root measure, generation, display and tuning). The three terms with zero hits (`phrase grouping`,
`thoroughbass`, `read-off`) are kept on Ruling 86's ground: *a term that matches nothing costs nothing.*

**The facts the ruling rests on**, each cited to `tools/audit/l3_keyword_count_measurement.json` (D-431): the core
terms alone 1,013 in-set hit lines; all 29 drafted terms 1,813; what each counted-in-context term adds beyond the core
terms at `what_each_COUNTED_IN_CONTEXT_word_adds_beyond_CORE`. **Derived by this side, not run:** the core terms without
`continuo` reach 984 lines (29 of `continuo`'s lines carry no other core term, read at the records); the ruled list
therefore reaches **at most 1,382** in-set hit lines, the exact figure being the population tool's to count. For scale,
L2's 42 terms reached 2,664 (`tools/audit/l2_outgoing_population.json` → `the_measured_size` → `item_3`). **Which sense
of a term fired is this side's reading of the hit lines, not a mechanical count.**

**Declined:** A — all 29 terms (strongest on #12; weakest on #2: `bass`, `sentence` and `continuo` add lines almost
entirely about something other than L3's subject). C — the core terms alone without `continuo` (loses the hyphenated
*phrase-boundary* / *phrase-end* material, the grouping material and the contradiction material, three of L3's
subjects; fails #12 for a saving the count does not justify). D — B plus narrow replacements for `bass` (a further
count dispatch and round trip for about 40 lines that items 1 and 2 of the 2026-10-17 ruling may reach for nothing — a
reading, item 2's document list not yet derived; the shape of the third route not taken at Ruling 86).

**Accepted cost, stated with the ruling:** some L3-relevant passages reached only by bare `bass` are not admitted by
this term; whether items 1 and 2 reach them is unchecked. **Not measured and not ruled in:** `punctuation-span` (this
document set's former name for the grouping unit), and the drafter's stated omissions (`section`, `figured`, `root`,
`quality`, `fermata`, `key area`).

## 3. The check of the surface, run in its own turn before the question — findings

Nine points, each corrected in the conversation before the question was put: B's bound tightened from 1,411 to 1,382
(dropping `continuo` removes its 29 unique lines); C's figure made exact at 984; "the same ground as Ruling 86" narrowed
— it fits `continuo` and `sentence`, while excluding `bass` rests on #2; "drops about 380 lines" replaced by "removes at
least 431, about 40 of them bearing on L3"; the L2 cost unit restated (hit lines are a ceiling on passages, which
merge, and hits inside spans compared whole are not counted again); the melodic-phrase share of `phrase` raised from
about 45 to about 60; the `punctuation-span` co-occurrence observation withdrawn as uninformative by construction; the
expectation that items 1 and 2 reach the `bass` lines marked unchecked; the `chordsymbol` / `harmonicrhythm` sample
stated as small; and "pushed" stated as read at the remote-tracking ref file, not at GitHub. None moved the
recommendation.

## 4. Documentation and algorithm

This ruling decides only which existing documentation is compared. It amends no specification and changes no
algorithm. The currently decided method for L3 is `FRAMEWORK.md` §5's L3 block — it publishes the cadence at each
phrase end with its type, the phrase and section grouping, the chord symbol (root pitch class, quality and bass note),
the figured bass and the harmonic rhythm — with DP-I (*"split — cues at L1, type at L3"*, quoted from the L3 ruling
records, not re-read at `FRAMEWORK.md`).

## 5. What this ruling does NOT do

It writes no dispatch (D-250), derives no population, compares nothing, puts none of the derivation's five user-marked
questions (OQ-L3-2, 3, 6, 8, 10), edits no tracked document, and allocates **no decisions-register identity** — the
register cannot accept one while `cowork_register_rule_c_suspension_2026_08_28.md` is the route (that file not opened
by this sitting). The next act is the L3 population dispatch (Option B item 3; D-250).

## 6. Departures of this sitting

**One shell command in the container** — a bare `echo` that read and wrote nothing — run in breach of the user's
opening instruction, declared to him in the turn it happened. No other shell command, in the container or on the
device. Device-info call first; `C:\s\MS` requested after it; folders listed: the handoff folder and the rulings folder —
never the repository root. No memory tool, git, widget, task list, subagent or web access.

*Provenance: Cowork, 2026-10-18 (Stockholm). The user's words: the opening instruction; "continue" (the check);
"continue" (the question); "B" (Ruling 1).*
