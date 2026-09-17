# CC report — the SECOND member-two passage withheld: the founding-instances sentence cut from the rendered pack, the read-me made to count its own passages; no session booted

> **Dispatch:** `cc_instruction_second_passage_withheld.md` (Cowork, 2026-08-23). Executes Ruling 1
> of `cowork_rulings_2026_08_23_member_two_second_leak_sitting.md`.
>
> **Commits, resolved at the objects by explicit hash:**
> Task 0 `1ff83f569a9c96e6cf4284e8a890e5850a9dffac` (parent `972ba18005a7d9668a99523a3066dffe3f5c9366`);
> Task 1 `cf00b6af7b89a6599c610b31bc9f47b639ccb217` (parent `1ff83f569a…`).
> Task 2's commit and the end-state commit are named in the close.
>
> **★ NO SESSION WAS BOOTED FROM THE PACK. NOTHING WAS DERIVED. NO ORACLE WAS OPENED.** Re-rendering
> the pack is not opening it, and this batch performed only the addition the one ruling orders,
> the one rendering edit the ruling licenses, and the close.

---

## 0. Words used in this report, explained at first use

- **The pilot** — the phase that proves the derivation method before the method is trusted.
- **An implementation-blind deriving session** — one that writes what the analysis *should* do for
  one unit without reading what the code or the specifications say it *does*.
- **The boot pack** — the rendered, self-contained directory such a session opens at boot, and
  outside which it opens nothing.
- **The held-out test** — one decision derived blind with the user's own ratified ruling on it
  withheld; that withheld ruling is the *oracle*.
- **The withheld family** — the recorded decisions, documents and passages cut out of the pack for
  one subject. An AUTHORED input the user rules.
- **The authored table** — the `WITHHELD` and verdict tables inside
  `tools/audit/gen_derivation_boot_pack.py`. Inputs to the generator, corrected by hand under a
  ruling record, never a hand edit to the generator's output.
- **The reading file** — `ratification_surfaces/cowork_withheld_family_harmony_boundary_reading.md`,
  written for the user and not generated.
- **The founding-instances sentence** — the sentence that closes `CLAUDE.md`'s
  defense-at-its-home bullet, naming three decisions recorded with no derivation. The subject of
  this batch's one ruling.

## 1. The declared start state — MATCHED exactly

The dispatch declared two failing checks at the tree this batch would meet, each with its cause, and
made a third failing verdict a STOP-and-report.

**Measured before the first edit, with the whole guard set run in CHECK mode** — which is the
correction the dispatch makes in terms of the predecessor's `--help` invocation — **exactly two
failing checks**, and they are the two declared: [[OI-372]]'s tool, the one standing red; and the
evidence-pin membership check reporting its artifact STALE, caused by this dispatch's own untracked
ruling record. **`gen_guard_state.py --check` opened "STALE vs the run" for the same cause**, which
the dispatch declares is not a third failing check. **Zero STOP verdicts.**
`gen_guard_classification.py --check` was run separately, as its own STOP requires, and **passed** —
so the third red the previous batch caused by running write-mode before its first edit did not arise
here at all.

## 2. Task 0 — the landing, the membership regeneration, and one state that did NOT recur

**A1's check was taken FIRST and entirely at content-addressed objects**, because the bare
working-tree forms are denied by the armed guard and are measured to time out on this mount.

1. **Exactly ONE tracked modification: `cowork_handoff.md`.** Its difference against the tip is the
   forty-sixth block inserted above the committed content; the one deletion is the forty-fifth
   heading, replaced by the same heading marked superseded as the entry point.
2. **Both named untracked paths present and absent from the tip**, each checked at the object.
3. **The population was ENUMERATED rather than sampled.** A1 makes a modification at any other
   tracked path a STOP, so the whole tracked-modification set was enumerated with the sanctioned
   enumeration tool and written to a generated artifact outside the repository: it holds exactly the
   one path above and no other.

**★ THE STATE THE PREVIOUS BATCH REPORTED DID NOT RECUR, AND ITS ABSENCE IS RECORDED.** The stale
zero-length `index.lock` that refused every staging operation at the previous Task 0 was **not
present**. Staging was refused by nothing; the removal remedy the previous batch performed under
**D-669** was neither needed nor taken. Recorded because a hazard reported once reads as standing
until someone says it did not repeat.

**The membership artifact was REGENERATED over the tree as it now stands and its difference MEASURED
against the committed blob before it was accepted, from every route** — the changed passages written
to an absolute scratch path outside the repository and read with the file tools, as the dispatch
directs. **Route A** moved by exactly the predicted amount and added exactly the predicted name.
**Route B** added nothing: the landed ruling record carries the word that route matches on nowhere in
its text, checked at the record itself. **Route C** is unmoved — this batch adds no measurement tool.
**AND NO FURTHER DIFFERENCE AROSE AT ALL:** unlike the previous batch, the regeneration produced no
additive derived cross-reference, so the artifact's whole difference is the two passages route A
predicts. No member, route, document, pin constant, state or count moved.

**Four paths were committed and no other**, each staged by explicit path, with the staged set
enumerated before the commit rather than assumed. Pushed; `origin/master` verified at the object to
name the Task 0 commit; the paths that commit touched enumerated at the commit object and found to
be exactly those four. The membership check then **PASSES**.

**Registered expectation E0 — MET in every particular**, including the ruling-record count read at
the committed artifact rather than at the run's own console line.

## 3. Task 1 — the one addition, the one licensed edit, the re-render, the reading file

One commit, as the dispatch requires.

### 3.1 (a) The authored `withheld_passages` list gains ONE entry and loses nothing

The entry is written in the shape the existing one uses: `CLAUDE.md`, member 2, the
defense-at-its-home bullet as its `scope_anchor`, the sentence located by its own opening and
closing text and **never by line number**, with the finding, the date and the reason the dispatch
fixes — the **D-677** shape. **The existing entry is untouched at every field**, which the manifest's
own difference proves rather than this report asserting it.

**The date on the new entry is written as a literal and not from the module's `DATE` constant**,
because the constant carries the previous sitting's date and the dispatch fixes this entry's date as
the date of THIS ruling. That is part of the addition, not a further change.

### 3.2 (b) The one licensed read-me rendering edit

The template sentence that hardcoded *"one passage inside …"* now **derives its number from the
passages actually applied for the subject** — singular wording at one, plural at more — so it stays
true for a subject carrying any count. The rendering function takes the applied-passage list as a
parameter and the call site passes it after the passages have been applied.

**Nothing else in the read-me and nothing else in the generator changes.** The candidate criterion,
the leak check, `withhold_passage()`, the marker and every STOP are untouched; no verdict is
re-graded; the manifest's own `the_rulings_it_executes` list was deliberately NOT extended, because
that would be a third change and the dispatch admits two.

### 3.3 (c) The re-render, and the generator's own STOPs as the check

The generator was run and `--check` is **green**. Its STOPs are what make that a check rather than a
formality: an anchor not resolving exactly once inside its ruled scope, a closing anchor preceding
its opening, an authored withholding missing its finding, date or reason, an IN verdict without its
identity, a candidate with no verdict, a verdict outside the closed vocabulary, and a verdict for an
entry the derivation no longer returns. **None halted.**

### 3.4 (d) A5, graded at the manifest and at the pack files, item by item

Every figure is at `tools/audit/derivation_boot_pack.json` → `subjects.harmony-boundary.counted` and
none is restated here (**D-431**). Graded field by field: **every field of `counted` is unmoved
except the passage count**, which is at the value A5 predicts.

**The manifest's WHOLE difference was measured against the committed blob rather than sampled**, and
it is three passages: the passage count; the added passage record with its derived matched text,
its character length and its marker; and member (2)'s own rendered character count. **No verdict row
appears in that difference**, so the seventy-five verdict rows are byte-unchanged; nor does the first
passage's record, the withheld-identity list, the withheld document, the leaks, the cross-reference
additions, the candidate criterion, or any other member's record.

At the pack files, read at the rendered files rather than inferred:

- **the rendered member (2) carries the marker exactly TWICE**, at the two ruled bullets;
- it carries **none** of the four strings the dispatch names, and a search over the **whole pack
  directory** returns none of them in any file;
- **the bullet's own statement stays whole above the second marker** — from the bullet's opening
  through *"…never filled in retroactively from memory (a defense written after the fact without a
  source is invention, and the never-work-from-memory rule forbids it)."* — read at the file;
- **the first cut and its marker are unchanged**, which the absence of any hunk touching them in the
  file's own difference establishes;
- the read-me's withholding sentence states the derived count and the read-me changes in no other
  way — its difference is exactly one line;
- **only four files move against the previous tip in this task's subject area** — the generator, the
  manifest, member (2) and the read-me — so **members (1), (3), (4), (5) and (6) are byte-unchanged**.

### 3.5 (e) The reading file, at the ruled lists and no further

The banner now names **both** ruling records and states that the second one's single ruling adds a
second withheld passage to LIST FIVE. LIST FIVE became **the withheld PASSAGES**, with two entries
under their own sub-headings: the first stands with its widened anchors and every word unchanged;
the second states **where** (the defense-at-its-home bullet of `CLAUDE.md`'s Conventions span,
boot-pack member (2)), **what** (the sentence, by its opening and closing anchors), **why** (the
ruling's finding, in this file's own words), and **how it was applied** (cut from the rendered member
and marked in place, the bullet's principle whole above the cut, `CLAUDE.md` untouched). The stated
bound is repeated and explicitly **not lifted**, together with the second ruling's own knowingly
accepted trade. **Nothing else in the file changes.**

**Registered expectation E1 — MET.** The authored list carries exactly the two passages; A5 held
field by field; `--check` is green; member (2) carries two markers and none of the four strings; the
read-me's sentence is true at two and derivable at any count; LIST FIVE carries two entries;
**`CLAUDE.md`, `ARCHITECTURE.md`, `DEFECT_TYPES.md`, `cowork_design_doc_template.md`,
`cowork_audit_protocol.md`, the phase-definition surface, `DECISIONS.md`, `OPEN_ITEMS.md`,
`docs/scoring_model.md` and every register source are byte-unchanged**, verified together and
returning an empty difference; the seventy-five verdict rows are byte-unchanged at the manifest
against the previous tip; no session booted.

## 4. Task 2 — the pointers and the close

One `STATUS.md` pointer entry per task that did work. The previous batch's entries were moved
verbatim to `STATUS_ARCHIVE.md` through the forward-bound tool at its three declared authored inputs
— **authored-input maintenance (D-648), licensed in terms by this dispatch, so it is not a
departure** — with the previous aiming **APPENDED rather than overwritten** (#12) and the
reconciliation proved in both directions by that tool's own check. The session-start read
measurement was regenerated, which is the red the dispatch predicted at the close and the act that
clears it.

The full close is the **THE SECOND PASSAGE WITHHELD: THE PACK AT ITS RULED STATE** section of
`cowork_away_returns.md`.

## 5. Assumptions and expectations, graded

| | Verdict |
|---|---|
| **A1** — the working tree, stated by content | **HELD**, item by item, at the objects, with the whole tracked population enumerated. The one state the previous batch met did not recur, and its absence is recorded in §2. |
| **A2** — one red remains, zero STOPs | **HELD.** The reds this batch caused were the declared membership red and the close's session-start read red, each cleared by the act that caused it. The guard-classification red the dispatch warned of did NOT occur, because the pre-edit run was taken in check mode. |
| **A3** — the membership regeneration from every route | **HELD** on all three routes, measured before acceptance, with NO further difference of any kind. |
| **A4** — the guard registry | **HELD.** No tool added; the population and the failing set unchanged; the three other registry artifacts byte-unchanged, verified together and returning an empty difference. |
| **A5** — the manifest from every field of `counted` | **HELD**, field by field, with the manifest's whole difference measured rather than sampled, and every pack-file check taken at the rendered file. |
| **E0** | **MET** (§2). |
| **E1** | **MET** (§3.5). |
| **E2** | Graded in the close, at the tree that carries it, and **not asserted here** — the end-state run is a later commit than this report. |

## 6. Declared departures, and acts this dispatch did not name

1. **The Task 1 guard run was taken in WRITE mode, and the pre-edit run in CHECK mode.** The dispatch
   fixes CHECK mode for the run before the first edit and for the run at the end, and it separately
   orders Task 1 to commit *the guard artifacts the run rewrote* — which a check-mode run does not
   produce. The pre-edit run was therefore in check mode, exactly as ordered; Task 1's was in write
   mode so that the artifact it commits is the artifact of a real run. **The whole difference that
   run made to `guard_state.json` was measured, not assumed:** one console line of the membership
   check, moved by the ordered Task 0 landing. No verdict moved, and `--check` is green after it.
2. **The zero-passage rendering of the read-me sentence is not reached by the licensed edit, and the
   bound is stated.** The sentence now derives its number, but the *Two kinds:* lead-in above it is
   hardcoded, so a subject with NO withheld passage would need that lead-in touched as well. The
   licence reaches one sentence and no more, so the lead-in was left. Recorded so a later session
   meets the bound rather than discovering it.
3. **The reading file's H1 title still reads *put to the user for a ruling*.** Not among the ordered
   changes; the status banner directly beneath it states RULED. The previous batch declared the same,
   and it is repeated because a departure that stops being declared reads as fixed.
4. **Reads not performed:** no boot-list member was opened beyond the spans the generator renders,
   the anchors it locates, and member (4)'s dispatch-protocol section, which this dispatch's own
   read-first block orders read in full;
   `cowork_blind_session_brief_harmony_boundary.md` was not opened; the pack directory was read only
   at the two files this batch's own checks name; **no oracle document was opened.**

## 7. The standing self-check over this batch's own diff

1. **Principles.** **#19** — one ruled withholding applied and nothing wider; the criterion's reach
   stays declared UNMEASURED on its own artifact and this batch makes no claim about it; the
   member-two bound is restated rather than weakened. **#6** — ONE authored list, the pack derived
   from it; the read-me's count derived from the applied passages rather than stated a second time.
   **#12** — the sentence is cut from the pack and not from its home, the first passage is untouched
   at every field, nothing is re-graded, the forward bound's previous aiming is appended rather than
   replaced, and the ruling's own wording is kept verbatim in the authored table rather than edited.
   **#17(f)/D-431** — no count is transcribed in this report, the close, the commit messages or the
   `STATUS.md` entries; every figure is named to an artifact and a field. **#13** — the one
   presentation-form observation was surfaced rather than absorbed (§8). **#24** — no comparison
   between measured quantities is asserted. **Conforms.**
2. **Conventions.** American English. No self-invented label. Music-theory words in their musical
   sense — *measurement tool* is used and never the reserved word; *the decisions register* is
   written in full; TOWARDS, never the other word, in every orientation phrase.
3. **Figures and premises.** Every quantity is named to its artifact and field; the ruling is quoted
   at its record; every premise the dispatch carried was re-read at the object rather than accepted
   — the tip and both refs, the guard-state summary, the whole `counted` block, the read-me's
   hardcoded sentence at the generator, and all three `CLAUDE.md` anchors located by their own text
   and each found exactly once.
4. **The file-tools rule.** Working-tree content was read with the file tools throughout. Shell use
   was limited to read-only git object queries by explicit hash, per-path diffs against an explicit
   hash whose output was written to an absolute scratch path outside the repository and read with
   the file tools, the sanctioned enumeration tool, and the project's own scripts. **The armed guard
   denied one attempt** — an interpreter invocation carrying a literal repository path, at the very
   first act — and it was replaced with the file-tools route rather than worked around.
5. **Uncertainty.** No difference between two measured quantities is asserted anywhere in this batch.

## 8. Quarantined audit questions

**None new.** This batch derived nothing about the analysis and measured nothing about it. The five
already surfaced stand exactly as they were, unacted on, and are not restated here.

**★ NO FURTHER PARAPHRASE-SHAPED LEAK WAS MET, AND THE BOUND ON THAT STATEMENT IS STATED WITH IT.**
The dispatch asks that a leak MET in the spans the generator renders be surfaced with its verbatim
and its location. **None was met.** The bound: this batch read member (2) at the two cut regions and
at the two marker positions, and member (4)'s whole dispatch-protocol section because the dispatch's
own read-first block orders that read; no other member was opened beyond the anchors the generator
locates. **This is not a sweep and does not claim one** — the sitting declines the sweep in terms,
and the standing bound that member (2) is not claimed free of other leaks is untouched.

**★ ONE PRESENTATION-FORM OBSERVATION, SURFACED BECAUSE IT WOULD OTHERWISE READ AS A CONTRADICTION,
AND IT MOVES NO VERDICT.** The ruling record's finding — which the dispatch fixes in terms and which
is therefore written into the authored table verbatim — says the sentence stands *"outside both
passages so far ruled"*. The record elsewhere establishes that there is **ONE** withheld passage and
not two: Ruling 5 of the withheld-family sitting widened the first passage's anchors and says in its
own words that the authored table carries ONE passage replacing the narrower anchors, *"not a second
passage (#6)"*. Read together, the phrase means *both passage RULINGS so far*, which is true. **The
authored table keeps the ruling's own wording** — a ruled text is not edited by the session executing
it (#12, #14) — **and the reading file, whose words are this session's, states it accurately.**
Surfaced rather than rowed: it is a wording inside a ruling record, it bears on no analysis question
and on no measurement, and correcting a ruled text is not a session's act.

## 9. What this batch did NOT do

No session booted from the pack; no derivation; no comparison; no oracle opened; no pilot act at all.
No change to the generator's mechanism beyond the one authored addition and the one licensed
rendering edit, and no re-grading of any verdict. No paraphrase sweep — declined in terms by the
sitting. No boot-list member edited at its home. No register entry, sort artifact or register source
touched. No open-items row created, flipped or discarded — [[OI-179]] stays OPEN and GATES,
[[OI-372]] and [[OI-374]] stand as found. No finding number allocated; the series stands at F88. No
`src/` change, no golden, no test changed, moved or run, nothing under `tools/corpus/` or
`tools/robust_stop/`. No document archived, moved or deleted as a file — the `STATUS.md` entries the
forward bound moved are the one licensed exception and are proved present in the archive and absent
from the must-read by that tool's own check in both directions.

---

*Provenance: Claude Code, 2026-08-23, executing `cc_instruction_second_passage_withheld.md`. Every
commit hash above was resolved at the object before it was written. TOWARDS the ultimate objective
and TOWARDS the guiding principles.*
