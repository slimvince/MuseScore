# CC report — the brief-validation rulings landed, the brief RULED, and the pack read-me's boundary scoped so it stays true; no session booted

> **Dispatch:** `cc_instruction_brief_ratification_and_readme_boundary.md` (Cowork, 2026-08-23).
> Executes Ruling 1 of `cowork_rulings_2026_08_23_brief_validation_sitting.md` and records
> Rulings 2 and 3 of the same sitting as applied inside the refreshed brief this batch lands.
>
> **Commits, resolved at the objects by explicit hash:**
> Task 0 `2fddf5767f819eb4251de5923bc8946c020ec880` (parent `d2a517c8db2b2debb2dc41cde3aff2fc8d224d7c`);
> Task 1 `a3ed95077697de6f75e46ecc0a0183346e6e823e` (parent `2fddf5767f…`).
> Task 2's commit and the end-state commit are named in the close.
>
> **★ NO SESSION WAS BOOTED FROM THE PACK. NOTHING WAS DERIVED. NO ORACLE WAS OPENED.** Re-rendering
> the pack is not opening it, and this batch performed only the landing the dispatch orders, the one
> read-me-template wording edit it licenses, and the close.
>
> **★ NO LINE OF THE BRIEF WAS WRITTEN BY THIS SESSION.** The refreshed brief is the writing side's
> text; this batch landed the file as delivered and read it whole to check it, nothing more.

---

## 0. Words used in this report, explained at first use

- **The pilot** — the phase that proves the derivation method before the method is trusted.
- **An implementation-blind deriving session** — one that writes what the analysis *should* do for
  one unit without reading what the code or the specifications say it *does*.
- **The boot pack** — the rendered, self-contained directory such a session opens at boot.
- **The read-me** — `tools/audit/derivation_boot_pack/harmony-boundary/00_READ_THIS_FIRST.md`,
  rendered by the generator from a template inside it. The subject of this batch's one edit.
- **The brief** — `cowork_blind_session_brief_harmony_boundary.md`, the document the blind deriving
  session reads FIRST, before the pack. Written and refreshed by the writing side; tracked.
- **The withheld family** — the recorded decisions, documents and passages cut out of the pack for
  one subject. An AUTHORED input the user rules.
- **The authored table** — the `WITHHELD` and verdict tables inside
  `tools/audit/gen_derivation_boot_pack.py`. Untouched by this batch.

## 1. The declared start state — MATCHED exactly

The dispatch declared two failing checks at the tree this batch would meet, each with its cause, and
made a third failing verdict a STOP-and-report.

**Measured before the first edit, with the whole guard set run in CHECK mode as the dispatch fixes —
exactly two failing checks**, and they are the two declared: [[OI-372]]'s tool, the one standing red;
and the evidence-pin membership check reporting its artifact STALE, caused by this dispatch's own
untracked ruling record. **`gen_guard_state.py --check` opened "STALE vs the run" for the same
cause**, which the dispatch declares is not a third failing check. **Zero STOP verdicts.**
`gen_guard_classification.py --check` was run separately, as its own STOP requires, and **passed**.

**The branch rule was taken at the tip and at nothing else.** Both refs name
`d2a517c8db2b2debb2dc41cde3aff2fc8d224d7c`, whose parent and subject are the ones the dispatch's
premise ledger states. The guard-state summary and the whole `counted` block were re-read at their
own artifacts, as ordered, and both match the ledger.

## 2. Task 0 — the landing, the membership regeneration, and one commit written twice

**A1's check was taken FIRST and entirely at content-addressed objects**, because the bare
working-tree forms are denied by the armed guard and are measured to time out on this mount.

1. **Exactly TWO tracked modifications, and they are the two the dispatch names.** The population was
   ENUMERATED with the sanctioned enumeration tool rather than sampled: `cowork_handoff.md` and
   `cowork_blind_session_brief_harmony_boundary.md`, and no other tracked path anywhere in the tree.
2. **`cowork_handoff.md` — ONE hunk at the file's fourth line**, one deletion, and the deleted line
   is the forty-sixth heading, read at the tip object and confirmed to be that heading. What replaces
   it is the forty-seventh block plus the same heading marked superseded as the entry point.
3. **The brief — FIVE hunks, every one inside a region A1 names.** The banner; §7's output-name
   sentence; §8's heading with its (P2) point; §8's (P4) and (P5) points; and §9's appended amendment
   note. **No hunk falls outside those regions**, which is what establishes that §§0–6 and every other
   line are byte-unchanged — read at the diff against the explicit hash, not assumed.
4. **Both named untracked paths present and absent from the tip**, each checked at the object.

**No stale index lock was met.** Staging was refused by nothing, and the **D-669** remedy the
batch-before-last performed was neither needed nor taken.

**The membership artifact was REGENERATED over the tree as it now stands and its difference MEASURED
against the committed blob before it was accepted, from every route** — the difference written to an
absolute scratch path outside the repository and read with the file tools. **Route A** moved by
exactly the predicted amount and added exactly the predicted name. **Route B** added nothing: the
landed ruling record carries the word that route matches on nowhere in its text, checked at the
record itself with the file tools. **Route C** is unmoved — this batch adds no measurement tool.
**AND NO FURTHER DIFFERENCE AROSE AT ALL:** the artifact's whole difference is the two hunks route A
predicts. No member, route, document, pin constant, state or count moved.

**Five paths were committed and no other**, each staged by explicit path, with the staged set
enumerated before the commit rather than assumed and the commit's own path set re-enumerated at the
commit object afterwards. Pushed; `origin/master` verified at the object to name the Task 0 commit.
The membership check then **PASSES**.

**★ THE COMMIT WAS WRITTEN TWICE, AND THE FIRST ATTEMPT IS DECLARED RATHER THAN ABSORBED.** The first
attempt carried a mangled subject — a PowerShell here-string form (`@'…'@`) passed to a POSIX shell,
which is literal text there and left two stray `@` characters wrapping the prescribed wording. It was
**amended before anything was pushed**. The amended commit carries the dispatch's exact prescribed
subject, read back at the object; its parent, its tree and its five paths are the ones the dispatch
names; the discarded first attempt was never pushed and reached no reader. Declared because the
standing preference is a new commit over an amendment, and because a hash that moved must be visible
to whoever verifies the chain at the objects.

**Registered expectation E0 — MET in every particular**, including the ruling-record count read at
the committed artifact rather than at the run's own console line.

## 3. Task 1 — the one template edit, the re-render, the byte-unchanged pack

One commit, as the dispatch requires.

### 3.1 The edit, and the whole of it

The read-me template's two boundary sentences were rewritten. **The generator's own per-path
difference against the Task 0 commit is ONE hunk, wholly inside the template**, so nothing else in
the file moved: the authored `WITHHELD` and verdict tables, the candidate criterion, the leak check,
`withhold_passage()`, the marker and every STOP are untouched, and no verdict is re-graded.

### 3.2 The re-render, and the generator's own STOPs as the check

The generator was run and `--check` is **green**. Its STOPs are what make that a check rather than a
formality: an anchor not resolving exactly once inside its ruled scope, a closing anchor preceding
its opening, an authored withholding missing its finding, date or reason, an IN verdict without its
identity, a candidate with no verdict, a verdict outside the closed vocabulary, and a verdict for an
entry the derivation no longer returns. **None halted.**

### 3.3 A5, graded at the manifest and at the pack files, item by item

Every figure is at `tools/audit/derivation_boot_pack.json` → `subjects.harmony-boundary.counted` and
none is restated here (**D-431**).

**The manifest's WHOLE difference against the Task 0 commit is EMPTY.** A5 allows a difference
confined to what derives from the read-me's own content; the manifest carries no record of the
read-me's bytes at all — its `the_members_as_rendered` block covers the six MEMBERS, and the read-me
is rendered outside that loop — so the allowed difference is empty and the artifact re-rendered
byte-identical. **Every field of `counted` is therefore unmoved by construction**, the seventy-five
verdict rows and both withheld passages are byte-unchanged, and no identity, document, leak or member
record appears in any difference.

**At the pack, only the read-me changes.** The pack directory's own difference against the Task 0
commit names exactly one file, `00_READ_THIS_FIRST.md`, so **members (1)–(6) are byte-unchanged at
the objects**.

**The rendered read-me was read WHOLE and graded against A5's (i)–(v):**

- **(i)** its title, its unit sentence, its six-file list and order, its stop-on-meeting clause, its
  what-was-cut section and its output section are all unchanged;
- **(ii)** the whole-of-your-read sentence is bounded to this repository, with the brief excepted;
- **(iii)** the NOT-opened list stands, with the brief excepted in its own words;
- **(iv)** the paragraph closes on the beyond-the-pack statement;
- **(v)** it names no brief file name, no staged file name, no ruling record, and says nothing further
  about what was withheld.

**The reworded boundary paragraph, quoted from the rendered file:**

> **This directory replaces the ordinary session-start read for you.** `cowork_handoff.md`,
> `STATUS.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `docs/scoring_model.md`, the open-items register
> and its derived gating answer, and every `cc_*` and `cowork_*` file outside this directory — the
> brief that dispatched you excepted — are **NOT opened**. No branch rule is taken. What you may
> read beyond this directory — your brief, score and analysis files your brief stages to you by
> name, and published research — is stated by your brief, and by nothing in this directory.

**And the whole-of-your-read sentence as rendered:**

> Read them in that order. Together with this file they are **the whole of your read within this
> repository**, apart from the brief that dispatched you and what the boundary below admits.

**The wording is generic**: it carries no subject, no name and no count, and is true for every future
subject the generator renders.

### 3.4 The guard run and the commit

The full guard set was run in **WRITE mode**, as this dispatch orders in terms, so that the artifact
the commit carries is the artifact of a real run. **A2 and A4 held** (§5). Three paths were committed
— the generator, the read-me and `guard_state.json`. **The manifest was not committed because it had
nothing to commit**: it re-rendered byte-identical and is absent from the changed-path enumeration.
Pushed; `origin/master` verified at the object; the commit's path set re-enumerated at the commit
object.

**Registered expectation E1 — MET.** The read-me is at A5 (i)–(v) and quoted above; every other pack
file is byte-unchanged at the object; `counted` is unmoved field by field; `--check` is green;
**`CLAUDE.md`, `ARCHITECTURE.md`, `DEFECT_TYPES.md`, `cowork_design_doc_template.md`,
`cowork_audit_protocol.md`, the phase-definition surface, `DECISIONS.md`, `OPEN_ITEMS.md`,
`docs/scoring_model.md` and every register source are byte-unchanged** — none appears in the
enumerated changed-path set at any point after Task 0; the seventy-five verdict rows and both
passages are byte-unchanged at the manifest; no session booted.

## 4. Task 2 — the pointers and the close

One `STATUS.md` pointer entry per task that did work. The previous batch's entries were moved
verbatim to `STATUS_ARCHIVE.md` through the forward-bound tool at its three declared authored inputs
— **authored-input maintenance (D-648), licensed in terms by this dispatch, so it is not a
departure** — with the previous aiming **APPENDED rather than overwritten** (#12) and the
reconciliation proved in both directions by that tool's own check. The session-start read measurement
was regenerated, which is the red the dispatch predicted at the close and the act that clears it.

The full close is the **THE BRIEF RULED AND THE PACK'S BOUNDARY TRUE: NOTHING STANDS BEFORE THE BLIND
SESSION** section of `cowork_away_returns.md`.

## 5. Assumptions and expectations, graded

| | Verdict |
|---|---|
| **A1** — the working tree, stated by content | **HELD**, item by item, at the objects, with the whole tracked population enumerated and the brief's difference read hunk by hunk: five hunks, none outside the named regions. |
| **A2** — one red remains, zero STOPs | **HELD.** The reds this batch caused were the declared membership red and the close's session-start read red, each cleared by the act that caused it. The generator's own check was red only between the template edit and the re-render, inside Task 1's single commit. |
| **A3** — the membership regeneration from every route | **HELD** on all three routes, measured before acceptance, with NO further difference of any kind. |
| **A4** — the guard registry | **HELD.** No tool added; the population and the failing set unchanged; the three other registry artifacts absent from the changed-path enumeration, so byte-unchanged entirely. `guard_state.json`'s whole difference is one console line of the membership check. |
| **A5** — the manifest and the pack after Task 1 | **HELD, and more strongly than predicted.** The manifest's whole difference is EMPTY; the pack directory's difference names one file; the read-me graded at (i)–(v) and quoted. |
| **E0** | **MET** (§2). |
| **E1** | **MET** (§3.4). |
| **E2** | Graded in the close, at the tree that carries it, and **not asserted here** — the end-state run is a later commit than this report. |

## 6. Declared departures, and acts this dispatch did not name

1. **The Task 0 commit was AMENDED before it was pushed**, its first attempt carrying a mangled
   subject from a PowerShell here-string form passed to a POSIX shell. Nothing was pushed between the
   two; the amended commit carries the exact prescribed subject read back at the object and the
   ordered five paths. Recorded at §2 with its cause and remedy.
2. **The read-me's whole-of-your-read sentence carries a forward-pointing clause A5 does not name,
   and without it the sentence would still be false.** A5 (ii) fixes the sentence as bounded to this
   repository with the brief excepted. But the score and analysis files the brief stages to the
   session by name are ALSO repository files, so a sentence excepting only the brief would still
   assert something the ruled inputs contradict — the very defect Ruling 1 exists to remove. The
   sentence therefore reads *"apart from the brief that dispatched you and what the boundary below
   admits"*, and the boundary paragraph states the exception once, exactly as A5 (iv) fixes it.
   **Nothing is added to what the read-me tells the session**; one clause points forward to the
   paragraph beneath it, and (v)'s prohibitions are untouched. Declared rather than taken silently.
3. **The manifest was not committed at Task 1**, because it re-rendered byte-identical and had
   nothing to commit. That is A5 holding, not an omission.
4. **The zero-passage rendering bound stands unchanged and unlifted.** The previous batch declared
   that the read-me's *Two kinds:* lead-in is hardcoded, so a subject with NO withheld passage would
   need it touched. This batch's licence reaches the boundary wording only, so the lead-in was left.
   Repeated because a declared bound that stops being declared reads as fixed.
5. **Reads not performed:** no rendered pack member was opened except the read-me;
   `cowork_joint_estimator_factorization.md` was not opened; the two `ARCHITECTURE.md` oracle spans
   were not opened beyond what the generator's own run locates; member (4)'s dispatch-protocol section
   was read at its own home, `cowork_audit_protocol.md`, because this dispatch's read-first block
   orders that read; **no oracle document was opened.**

## 7. The standing self-check over this batch's own diff

1. **Principles.** **#19** — the pack's boundary claim is made TRUE rather than overridden, and the
   blind session's inputs stay the ruled ones; nothing is claimed established that was not measured,
   and the candidate criterion's reach stays declared UNMEASURED on its own artifact with no claim
   made about it here. **#6** — what the session may read beyond the pack now has ONE home, the brief,
   and the read-me points at it instead of keeping a second list. **#12** — the read-me's other
   sections are kept whole, the brief's §§0–6 are untouched, the brief's own §9 records the amendment
   rather than replacing history, and the forward bound's previous aiming is appended rather than
   replaced. **#17(f)/D-431** — no count is transcribed in this report, the close, the commit messages
   or the `STATUS.md` entries; every figure is named to an artifact and a field. **#13** — the amended
   commit and the forward-pointing clause were surfaced rather than absorbed. **#24** — no comparison
   between measured quantities is asserted. **Conforms.**
2. **Conventions.** American English. No self-invented label. Music-theory words in their musical
   sense — *measurement tool* is used and never the reserved word; *score* appears only of the musical
   score; *the decisions register* and *the open-items register* are written in full; TOWARDS, never
   the other word, in every orientation phrase.
3. **Figures and premises.** Every quantity is named to its artifact and field; the rulings are quoted
   at their record; every premise the dispatch carried was re-read at the object rather than accepted
   — the tip and both refs, the guard-state summary, the whole `counted` block, the read-me's two
   sentences at the tip object and at the generator's template, and the ruling record's absence of the
   word route B matches on.
4. **The file-tools rule.** Working-tree content was read with the file tools throughout. Shell use
   was limited to read-only git object queries by explicit hash, per-path diffs against an explicit
   hash whose output was written to an absolute scratch path outside the repository and read with the
   file tools, the sanctioned enumeration tool, and the project's own scripts. **The armed guard
   denied two attempts** — an interpreter invocation carrying a literal repository path at the very
   first act, and a `cat` over a scratch path whose shell variable the guard could not expand, denied
   on the standing deny-on-indeterminate policy — and each was replaced with the file-tools route
   rather than worked around.
5. **Uncertainty.** No difference between two measured quantities is asserted anywhere in this batch.

## 8. Quarantined audit questions

**None new.** This batch derived nothing about the analysis and measured nothing about it. The five
already surfaced stand exactly as they were, unacted on, and are not restated here.

**★ NO DEFECT WAS FOUND IN THE REFRESHED BRIEF, AND THE BOUND ON THAT STATEMENT IS STATED WITH IT.**
The dispatch makes a defect in the brief a STOP-and-report. The brief was read WHOLE at the working
tree before Task 0, and its every §8 point, its §7 output name and its §9 amendment note were checked
against the sitting record's own text; all agree, and the sitting's own three rulings are reflected
exactly. **The bound:** this is a reading of the brief against the sitting record and against A1's
regions — not a re-validation of the brief against the pack, which is the writing side's act, already
performed, and not repeated here.

**★ NO FURTHER PARAPHRASE-SHAPED LEAK WAS MET, AND ITS BOUND IS NARROWER THAN THE PREVIOUS BATCH'S.**
The dispatch asks that a leak MET in the spans this batch touches be surfaced with its verbatim and
its location. **None was met.** **The bound:** this batch opened NO rendered pack member except the
read-me. **This is not a sweep and does not claim one**, and the standing bound that member (2) is not
claimed free of other leaks is untouched.

## 9. What this batch did NOT do

No session booted from the pack; no derivation; no comparison; no oracle opened; no pilot act at all.
No change to the generator beyond the read-me template's boundary wording; no edit to the brief's
content; no movement of any verdict, identity, document or passage; no paraphrase sweep. No boot-list
member edited at its home. No register entry, sort artifact or register source touched. No open-items
row created, flipped or discarded — [[OI-179]] stays OPEN and GATES, [[OI-372]] and [[OI-374]] stand
as found. No finding number allocated; the series stands at F88. No `src/` change, no golden, no test
changed, moved or run, nothing under `tools/corpus/` or `tools/robust_stop/`. No document archived,
moved or deleted as a file — the `STATUS.md` entries the forward bound moved are the one licensed
exception and are proved present in the archive and absent from the must-read by that tool's own check
in both directions.

---

*Provenance: Claude Code, 2026-08-23, executing `cc_instruction_brief_ratification_and_readme_boundary.md`.
Every commit hash above was resolved at the object before it was written. TOWARDS the ultimate
objective and TOWARDS the guiding principles.*
