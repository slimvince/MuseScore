# The LEAK LIST for the `scoring-model` boot pack — put to the user for a ruling

> **STATUS: AWAITING THE USER'S RULING.** One decision is asked: whether the standing leak check
> goes on excluding the entries listed below from the boot pack an implementation-blind session
> will read for the sizing subject.
>
> Prepared by Claude Code, 2026-08-24, under `cc_instruction_sizing_pack_preparation.md` Task 1(e),
> executing Ruling 1 of `cowork_rulings_2026_08_24_sizing_pilot_sitting.md` — *"The leak list goes
> to the user as a reading file in the shape List Four took."*
>
> **No session has been booted from this pack.** Rendering a pack is not opening it.
>
> **★ THIS FILE WITHHOLDS NOTHING, AND THAT IS THE FIRST THING TO READ.** For this subject the
> withheld family is **EMPTY by your own ruling**: no register entry, no document and no passage is
> held back. The list below is not a withholding and is not an oracle. It is the residue of a
> different check, which exists for a different reason, and which is stated in full below.

---

## 1. The words used here, explained first

- **The sizing subject** — the second subject of the pilot: the unit whose specification
  `docs/scoring_model.md` carries, ruled on 2026-08-15 as the hardest implementation-blind case and
  derived blind by a later session so that the record can be sized from what that derivation cost.
- **An implementation-blind deriving session** — a session that writes what the analysis *should*
  do for one unit, without reading what the current code or the current specifications say it
  *does*.
- **The boot pack** — the rendered, self-contained directory such a session opens, and the only
  thing inside this repository it opens. The sizing subject's now exists on disk at
  `tools/audit/derivation_boot_pack/scoring-model/`.
- **The withheld family** — the recorded decisions, documents and passages cut out of a pack so
  that a held-out answer does not reach the session by a side route. **For this subject it is
  empty**, because this unit is not held out and has no oracle.
- **The leak check** — the standing string test described in §2. It is not a withholding, and it
  predates this subject: it has run over every pack this generator has rendered.

## 2. What the leak check is, and what it is for

The pack has six members. **Four are quoted whole** from a governing document; **two are
GENERATED** by the tool that renders the pack — the design-intent file, which carries register
entries, and the defect-type catalog, which carries two columns of a table.

Before either generated member is written, every entry and every row that would go into it is
tested against its own rendered words. **An entry whose rendered words carry a `docs/` or a `src/`
path, or the string `ARCHITECTURE.md`, is NOT rendered into the pack. It is listed instead** — in
the manifest, and here.

**What the test is for:** the pack's own boundary clause tells the deriving session that the
implementation's documents and code are not opened. An entry whose text hands that session a live
path into `docs/`, into `src/`, or into the implementation's own specification is a route out of
the pack, offered by the pack itself. The check closes that route. **It is about pointing INTO the
implementation, and it is not about any oracle** — this subject has none.

## 3. The scope, stated because a scope that is not stated reads as total

**The check runs over the two GENERATED members only** — the design-intent file and the
defect-type catalog. The four members quoted whole are **not** string-tested, and that is
deliberate rather than an omission: they are ruled whole, and one of them names `ARCHITECTURE.md`
inside the never-work-from-memory rule *by design* — a string test over it would strike the very
rule that tells a deriving session where a primary source lives.

**This file therefore does not claim the four whole members carry no path of their own.** It
states what the check covers, and no more.

## 4. The leak list, in full

*Every entry below reached the design-intent member and was listed rather than rendered. Each is
given with its identifier, its title, the rendered field the match was found in, and the exact
string that matched.*

| ID | Title | Field | The exact string that matched |
|---|---|---|---|
| D-270 | The held-out evaluation protocol - five-fold cross-validation grouped by ground-truth analysis file | `verbatim` | `docs/score_inventory.md` |
| D-296 | READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits | `verbatim` | `src/notation` and `src/engraving` |
| D-440 | The language-model integration is purpose-built and does not wait for the plugin-API reform | `verbatim` | `src/llm/` |

**No row of the defect-type catalog matched**, and the catalog member renders byte-identically for
this subject and for the harmony-boundary one — measured at the content-addressed objects, not
assumed.

*The list, the per-match field and kind, and every count are published at
`tools/audit/derivation_boot_pack.json` → `subjects.scoring-model.LEAKS` and `…counted`. No count
is restated here (**D-431**).*

**★ WHAT THE THREE HAVE IN COMMON, AND WHAT THEY DO NOT.** Each matched on a **repository path**
written inside the decision's own quoted words — a `docs/` document in one, `src/` directories in
the other two. **None matched on `ARCHITECTURE.md`**, and none was excluded for anything to do with
the sizing subject. **The same entries, and only these, were listed for the harmony-boundary
subject**, where the family was not empty: so the emptying of the family added no leak and removed
none.

## 5. What is being asked

**One question: does the leak check keep excluding these entries from this subject's pack?**

That is the whole of it. Nothing else on this surface is a decision, and no recommendation is made
here. Stated in terms, so that the question is not read as larger than it is:

- **You are NOT being asked to withhold anything.** The withheld family for this subject is empty
  by your Ruling 1, and this list does not change that.
- **You are NOT being asked to rule on any of the three decisions themselves.** Their standing in
  the decisions register is untouched by whether a pack renders them.
- **You are NOT being asked to re-rule the check.** You ruled it on 2026-08-22 for the
  harmony-boundary subject (LIST FOUR, your word: "A"), with two alternatives declined at that
  ruling — rendering with the matched path removed, which would be a hand edit to a ratified
  entry's quoted words inside a generated member and a second copy differing from the register
  (#6); and dropping the `docs/`/`src/` path test, which is the test that catches routes into the
  code. **That ruling is not reopened by this file.** What is asked is only whether it goes on
  applying here, to a subject whose family is empty.

## 6. What this file does NOT do

- **It boots no session.** The blind derivation of the sizing subject is a separate, later act.
- **It withholds nothing**, and it is not a withheld-family surface. The family is empty by ruling.
- **It grades nothing about the analysis**, proposes no fix, and takes no design decision.
- **It moves no register entry and no status.** Not rendering an entry into one pack says nothing
  about that entry's standing.
- **It closes no open item.** [[OI-179]] stays OPEN and GATES; [[OI-372]] and [[OI-374]] stand as
  found.
- **It touches nothing of the harmony-boundary subject** — that pack, its family, its own reading
  file and its manifest block are byte-unchanged by the act that produced this file, proven by
  enumeration and at the content-addressed objects rather than asserted.
- **It does not claim the check's reach is complete.** The check tests the rendered words of the
  two generated members for the strings §2 names, and nothing else; what it does not test is
  stated at §3.

---

*Provenance: Claude Code, 2026-08-24, at the tree carrying commit
`ac81167005660bbe12aa8840196ff8318e8df2e1`, under `cc_instruction_sizing_pack_preparation.md`
Task 1(e). The list above is DERIVED — it is read from
`tools/audit/derivation_boot_pack.json` → `subjects.scoring-model.LEAKS.entries`, which the
generator wrote in the same act, and nothing in it is authored. The claim that the four
whole-quoted members and the catalog member render identically across the two subjects was
measured at the staged blob identifiers, not inferred. `docs/scoring_model.md` was not opened.
TOWARDS the ultimate objective and TOWARDS the guiding principles.*
