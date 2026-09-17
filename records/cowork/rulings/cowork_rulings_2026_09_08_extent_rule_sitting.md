# Ruling — the marked-clause extent rule, 2026-09-08 (the fourth sitting of the defense-share arc)

> **STATUS: RULING RECORD.** Cowork, 2026-09-08. Written in the turn the ruling was given, under the
> standing clause that a sitting record is written then and lands in git at the next dispatch's
> Task 0.
>
> **Taken at tip `cdd7ff4aca948156291725c76535bedfd84d9be5`**, read at `.git/refs/heads/master` with
> the file tools. Nothing was running; the third issue of the arc had closed. The surface ruled on
> was delivered whole as user-visible text in its own turn, with **no choice question in it** —
> because the alternatives had collapsed, which the surface said in terms rather than presenting a
> menu (his ruling of 2026-08-28).

---

## 1. Ruling — a marked defense clause ENDS at its paragraph's end OR at the next marked clause, whichever comes first; that is the measurement's definition (the user's words: *"agree, let us continue"*)

**What was put.** `cc_instruction_defense_share_sizing_third_2026_09_08.md` fixed a marked clause's
extent as *"From the first character of the marker through the end of the paragraph containing it"*,
and in the same task made two establishment STOPs: that **no two clauses overlap**, and that **a
span's clause characters do not exceed that span's own count**. **At this tree those cannot all
hold**, because `CLAUDE.md` routinely writes two marked defenses inside ONE paragraph, so under the
literal wording both run to that paragraph's end and overlap. The executing batch measured the
conflict before deciding anything, implemented the closing rule in order to produce the ordered
measurement at all, and declared the departure at the tool, on the artifact, in `STATUS.md` and in
its report — handing the definition back to this side, which is where a measurement definition
belongs.

**Ruled.** **The closing rule IS the definition.** A marked clause reaches its paragraph's end or
the next marked clause, whichever comes first. The literal wording of the dispatch is a **drafting
defect in a bar this side wrote**, and it is corrected rather than ratified.

**The ground, recorded so a later session can test it rather than re-argue it.**

1. **The quantity the dispatch NAMES is characters** — *"the characters standing inside
   explicitly-marked defense clauses"* — **and a character standing inside two clauses is one
   character.**
2. **The two establishment STOPs already said so.** Both are violated only by double-counting, so
   the dispatch's own checks demand a character count and not a sum of extents.
3. **The closing rule loses nothing.** For clauses ordered by their start and running to one
   paragraph end, **the union of the untruncated extents and the union of the closed ones are the
   SAME CHARACTER SET.** The only change is that a character is counted once. This was checked at
   the reasoning and at the published per-clause records, not taken on the batch's word.
4. **The literal reading measures a DIFFERENT quantity** — the total size of the paragraphs that
   happen to contain a marked defense — **which cannot be expressed as a share of anything**: at
   this tree it attributes 159,825 characters to six spans holding 97,805 in total, across 20
   overlapping pairs. Adopting it would additionally require striking two establishment STOPs, which
   is a second decision nobody asked for.

**Both readings stay published (#12).** Every per-clause record on `tools/audit/defense_share.json`
carries its closed length AND the length it would have had running to its paragraph end, and the
artifact carries the literal sum and the overlapping-pair count. **Nothing is re-derived by this
ruling and no measured value moves.**

## 2. What this ruling does NOT do

- **It authorizes no move of text.** No satellite file is created, nothing leaves `CLAUDE.md`, and
  `CLAUDE.md` is not edited.
- **It says nothing about MOVABILITY.** Whether any measured character may live in a satellite is
  Ruling 1 of `cowork_rulings_2026_09_08_defense_satellite_sitting.md`, and neither the measurement
  nor this ruling answers any portion of it.
- **It does not touch the marker table**, does not widen or narrow what counts as a defense, and
  does not lift the declared bound: the marker set's reach stays UNMEASURED and the published value
  stays a **LOWER BOUND** under **D-673**.
- **No decisions-register entry is written and no `D-NNN` is allocated.** The register debt stands
  in the shape the hundred-and-forty-eighth and hundred-and-forty-ninth entries record: the
  accumulated run is CLASSIFIED first and put to the user as a reading file, with no entry written
  before he rules the classification. **He can overrule that in one word.**
- **No open-items row is created, flipped or discarded. The reading gate is not lifted and both the
  row-by-row extraction and the pruning pass stay paused.**

## 3. What is owed to a later batch — small, mechanical, and named so it is not rediscovered

**(a) The spent dispatch is RE-BANNERED, never rewritten (`D-674`).**
`cc_instruction_defense_share_sizing_third_2026_09_08.md` has run and is committed; it is a dated
instruction the record has overtaken, so its body stands as it was executed and a banner at its head
records that its extent sentence was defective as written, how the executing batch resolved it, and
that the resolution is ruled here. **Rewriting its body would falsify what the batch actually ran
against.**

**(b) The tool's and the artifact's "owed to the writing side" wording is now stale and is corrected
AT THE GENERATOR, never by hand.** `tools/audit/defense_share.json` is a generated file; its
declared-departure block says the definition is outstanding, and after this ruling it is not. The
correction is an edit to `tools/audit/gen_defense_share.py`'s own strings plus a regeneration, in one
act, by the side that executes. **The measured values do not move** — this changes what the artifact
SAYS about the definition's standing, not the definition — **and that must be proved by the
regenerated artifact rather than asserted.**

Neither (a) nor (b) is urgent, and neither gates anything. They are named here so that a later
session finds them written down rather than deriving them again.

---

*Provenance: Cowork, 2026-09-08, at tip `cdd7ff4aca`. The surface was delivered whole in its own
turn and carried no choice question, the alternatives having collapsed. The user's word, verbatim:
"agree, let us continue". The conflict was found and declared by the executing batch of
`cc_instruction_defense_share_sizing_third_2026_09_08.md`, whose report
`cc_report_defense_share_sizing_third_2026_09_08.md` was read in FULL by this side and whose
load-bearing claims about the departure were re-verified at `tools/audit/defense_share.json` before
the surface was written.*
