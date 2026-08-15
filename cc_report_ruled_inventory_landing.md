# CC report — the ruled landing, the guard clearing, and the class-1 construction-evidence check

> **Dispatch:** `cc_instruction_ruled_inventory_landing.md` (Cowork, 2026-08-15), executing
> `cowork_rulings_2026_08_15_inventory_sitting.md` §1 (the landing), §3.1 (the class-1 check) and
> §5 (the guard clearing). **Performed 2026-08-15 (CC).**
>
> **This report is the whole of what the coding side says back.** Every count it names is at the
> artifact it cites, and no population, member list or verdict is restated from one (**D-431**),
> except where the dispatch itself orders names published — which it does once, for the
> SPEC-DERIVED-EVIDENCE members.
>
> **★ THREE THINGS NEED THE USER, and they are §1, §2 and §3 below**; a fourth finding, surfaced by
> the batch's own guard runs and diagnosed at the code, is at **§4.a**. Everything after §4 is the
> per-task record.

---

## 1. ★ THE CLASS-1 CHECK RETURNED 20 MEMBERS WITH SPEC-DERIVED EVIDENCE — the follow-up ruling §3.1 provides for is OWED

§3.1 ruled class 1 conditionally, in the user's own words: *"IFF the regression test were
constructed based solely on code and not at all on specs - I agree with you (A)."* The check has
run. **The condition is NOT met as stated**, and the ruling's own consequence applies: a test
established as SPEC-DERIVED carries design intent and **returns to the user** rather than being
silently excluded.

**The distribution, at `tools/audit/test_construction_evidence.json`:** population **123**;
**SPEC-DERIVED-EVIDENCE 20**; **CODE-BUILT 103**, split into **52** with positive evidence of
construction beside or from the code and **51** with no establishable construction evidence at all
— the ruling's own default, recorded as a distinct sub-case exactly as the dispatch requires.

**The 20, BY NAME** (the dispatch orders them named; every one is a member of
`src/composing/tests/`):

*Evidence located IN THE FILE ITSELF — 18:*

`decode_chord_tests.cpp`, `forwardoverride_tests.cpp`, `functioncadence_tests.cpp`,
`functionmodulation_tests.cpp`, `functionoutput_tests.cpp`, `functionprogression_tests.cpp`,
`functionrelationallabel_tests.cpp`, `functionresolver_tests.cpp`,
`functionromannumeral_tests.cpp`, `inference_presentation_boundary_tests.cpp`,
`joint_modal_tests.cpp`, `joint_record_tests.cpp`, `joint_slice_tests.cpp`,
`joint_spelling_tests.cpp`, `modepriorpresets_tests.cpp`, `note_model_tests.cpp`,
`progressionrecognizer_tests.cpp`, `regionanalysis_tests.cpp`.

*Evidence located ONLY in a commit subject — 2:* `CMakeLists.txt`, `joint_producer_tests.cpp`.

**What the in-file evidence looks like**, so the finding can be judged rather than taken:
`functionromannumeral_tests.cpp` carries the line *"// Spec: cowork_layer5_function_design.md
§5.1."* — a remark stating the specification the test's expectations were taken from. That is the
shape of the 18.

**★ THE ONE LIMITATION THAT BEARS ON HOW THE 20 ARE READ, stated rather than corrected.** A commit
subject describes the COMMIT, not one file inside it. For the two members whose only statement sits
in a commit subject, what is established is that a change naming a contract section touched the
file — **not** that the file's own expectations were read out of that section. Every row records
where its statements were located so the two cases can be told apart without re-deriving anything.
Narrowing the evidence to in-file statements would have dropped the dispatch's own second source,
and weighting one against the other would have been this side deciding what the ruling sends to the
user.

**What the check does NOT establish (#19).** The recognizers are AUTHORED and their reach against
the text they scan is **unmeasured** — the defect the record has met twice already ([[OI-367]],
[[OI-368]]). What the STOPs establish is that every population member carries a verdict and that no
positive verdict rests on nothing. **The ruling's own default is what bounds the error**: an
unestablished construction is treated as code-built, so a missed statement errs toward exclusion,
which the ruling records as the recoverable direction. **A reader may not take the artifact as
evidence that no further specification-derived test exists.**

**The catalogs, which §3.1 asks about separately:** `chordanalyzer_catalog_jazz.musicxml` is
CODE-BUILT with positive evidence; `chordanalyzer_catalog_standard.musicxml` is CODE-BUILT by the
ruling's default. **Neither carries specification-derived evidence**, so on this check the two
catalogs do NOT differ from the tests in the direction the question anticipated — they sit on the
code-built side, which is where the class-1 proposal already put them.

**Nothing was done with any of this.** No test was edited, moved or run; no class verdict was
adopted, narrowed or applied.

---

## 2. ★ THE GUARD CLEARING'S SECOND HALF IS NOT PERFORMED, AND THE REASON IS AT THE CODE — [[OI-373]] IS UNTOUCHED

§5's extension orders [[OI-373]] flipped RESOLVED with provenance after the invocations are
authored. **The invocations ARE authored and the runner's STOP IS cleared** — the substance of the
row is discharged. **The flip is not performed**, and this is a STOP-and-report rather than an
omission.

**Established at the code, not argued.** `tools/audit/gen_discard_records.py` carries an authored
discard pointer for [[OI-373]] in its own `AUTHORED` table, and `build()` refuses on any entered row
that is resolved at the INDEX — `gen_discard_records.py:317-321`:

> `STOP: {row} is RESOLVED at the INDEX and this table carries a discard record for it. A discard is
> not a resolution and a resolved row does not need one — the two states have come apart and are not
> reconciled here.`

A row's state is its status cell's leading token and nothing else (register rule (f)), so **flipping
[[OI-373]] turns that guard red by construction.** It is a member of the guard run set and it passes
today.

**Why that is a divergence and not a preference.** The flip would leave **two** standing reds. The
ruling's own words are *"After the act, [[OI-372]] is the one standing red"*, and the dispatch's
registered expectation **E2** is *"one FAIL ([[OI-372]]), zero STOPs"*. Performing the flip makes
both false, and makes them false through this batch's own edit — which is exactly the condition the
standing self-check exists to surface rather than ship.

**Why the coherent version of the act is not this session's.** Flipping the row AND retiring the
discard pointer from `gen_discard_records.py`'s authored table, whole and with the reason it left
(#12), is a change to a mechanism's structure that **D-436** reserves to the user — the same ground
on which [[OI-372]] records that its own closing act needs a retired block added.

**So [[OI-373]] is left ENTIRELY untouched:** no status cell moved, no dated remark added to its
detail file. **The cost of leaving it open is nil while the user decides** — the row is DISCARDED
under the worth test, so it gates nothing and draws no capacity; what remains is bookkeeping.

**The two acts available, neither taken:** *(a)* retire the discard pointer with its reason and flip
the row in one act; or *(b)* flip the row and leave the pointer, accepting a red in
`gen_discard_records.py` — which would make the standing reds two again, the number this batch was
ordered to reduce to one.

---

## 3. ★ THE RULED `.gitignore` EDIT DOES NOT END THE DISAGREEMENT IT WAS RULED TO END

§1 orders the rule `/cc_*.md` removed, and the dispatch orders that line and no other to move. Both
were done exactly. **But `.gitignore` carries the NARROWER rule `/cc_instruction_*.md` two lines
above it, untouched — so 92 of the 122 files landing under §1 were still ignored and had to be
staged with `-f`.**

**What that means going forward.** The 122 are tracked now, and a later edit to any of them is
visible, so the landed material is safe. **What is still exposed is every dispatch written after
this commit**: a new `cc_instruction_*.md` file remains silently outside git, which is the
rule-versus-practice disagreement the ruling named — *"ending the silent rule-versus-practice
disagreement in the direction that keeps records"* — surviving in its narrower form.

**Not fixed here, deliberately.** Removing a second ignore rule is a change to what the ruling
decided, and the dispatch's own words are *"No other line moves."* It is reported so the user can
rule on the remaining line rather than discover it at the next handover. (The record already carries
the confusion this causes: the previous batch's Task 0 commit message attributes the `-f` staging of
two dispatch files to `/cc_*.md` alone, which was never the whole cause.)

---

## 4. The guard set, both states

**Run BEFORE the first edit and again at the end** — the inventory batch's declared departure is not
repeated.

**AT THE START** (`gen_guard_state.py --check`, before any file was written): **45 guards run, 44
passing, ONE failing** — `gen_filing_convention_application.py --check`, which is [[OI-372]], rowed
and discarded. **One STOP**, the runner's own, naming exactly two tools —
`gen_doc_change_candidates.py` and `gen_status_archive_pass.py` — which is the dispatch's
**assumption A2 CONFIRMED**. The runner also reported the committed `guard_state.json` STALE against
its own run. Separately, `gen_guard_classification.py --check` STOPped naming exactly one tool,
`gen_discard_records.py`, the 2026-08-13 entrant — **assumption A1 CONFIRMED**.

**AT THE END:** **48 guards run, 47 passing, ONE failing — the same one, [[OI-372]] — and NO STOP of
any kind.** `guard_state.json` was regenerated by its own generator and a second full run reports,
in its own opening words, **"the guard state re-derives"**; `guard_classification.json` likewise
regenerates and re-derives. **The only red this batch leaves is the one it found**, and it is
untouched.

**Assumption A3** (every listed cited-and-ignored file still on disk) is CONFIRMED mechanically: git
resolved all 122 pathspecs, and every one of the 123 records staged was an ADDITION.

### ★ 4.a A SURFACED FINDING — `guard_state.json` CANNOT re-derive across a commit, and the cause is now diagnosed

**The condition.** The runner's `--check` reports **STALE** at both ends of this batch: at the
opening run, before anything was edited, and at the final run after this batch's commits. In both
cases **every verdict is identical** and what differs is captured text.

**The cause, established at the code and not inferred.** `tools/audit/gen_artifact_inventory.py`'s
live half resolves the **CURRENT HEAD** and prints its short hash — *"the signature table still
covers the tree at `<sha>` with nothing unclassified"* (`gen_artifact_inventory.py:779-782`). The
runner normalizes exactly one shape of commit hash in captured output, the literal word `HEAD`
followed by a sha (`gen_guard_state.py`'s `HEAD_SHA` pattern), and **this line does not carry that
word**, so it is not normalized. **Committing anything therefore makes `guard_state.json` stale by
construction** — which is the very failure the runner's own comment beside that pattern describes,
reappearing in a form the pattern does not reach. The same tool's second printed line, which says
whether the untracked appendix moved, varies with the working tree for the same reason.

**Why this matters beyond housekeeping.** The artifact's own `--check` is one of the record's
guards. As it stands it is red at every tree except the single one it was generated at, which
teaches a reader to ignore it — the exact failure mode the R4 ruling exists to prevent. It also
explains the STALE the previous batch's opening run reported and did not diagnose.

**NOT FIXED HERE, and the artifact was NOT regenerated a second time to hide it.** Widening the
runner's normalization, or changing what the inventory check prints, is a change to a mechanism's
structure that **D-436** reserves. Regenerating would make the artifact match for exactly as long as
it takes to commit it. **The committed `guard_state.json` is the full 48-guard run of this batch,
with its verdicts, and it is stale at HEAD for the reason above.** No open-items row was opened —
this batch's bars forbid it — so it is declared here for the writing side.

---

## 5. The per-task record

**Every commit is pushed to `origin` and verified at the object by explicit hash through
`changed_paths.py --commit`.** Task 0 `dfea49b7a5`, Task 1 `0fcff4f6e2`, **Task 3 `811244d57c`**,
**Task 2 `4a65a40e03`**, and this close's own commit.

**★ TASKS 2 AND 3 ARE COMMITTED IN THAT ORDER — INVERTED, DELIBERATELY, AND DECLARED.** Task 3's
tool carries a `--check` mode, so it joins the runner's derived candidate population **by
existing**; committing Task 2's guard table first would have committed a list naming a file the tree
did not carry, which is the phase-1r failure the runner's existence STOP was built against. Each
task is still ONE commit and each commit's own message states the reason.

### Task 0 — the writing-side records landed. Commit `dfea49b7a5`, pushed

Exactly the three paths the dispatch names, verified at the index through the sanctioned enumeration
before the commit and at the object after it: `cowork_rulings_2026_08_15_inventory_sitting.md`
(new), `cowork_handoff.md` (modified), `cc_instruction_ruled_inventory_landing.md` (staged with
`-f`). The dispatch's fourth path was UNMODIFIED on disk and already tracked, so its line was the
no-op the dispatch says it is. **Registered expectation E0 — three paths — MET.**

### Task 1 — the ruled landing. Commit `0fcff4f6e2`, pushed. See §3 for what it does not achieve

`.gitignore`'s `/cc_*.md` line deleted and no other line moved. The landing list parsed from the
ruling surface's own *The cited-and-ignored files (DERIVED)* section, **counted exactly 122** — the
dispatch's STOP condition met rather than assumed — and staged with `.gitignore` as ONE commit.
**Registered expectation E1 — path count 123, and `git log --all` for
`cc_adoption_measurement_report.md` showing exactly one commit, this one — MET on both limbs.**

### Task 2 — the guard clearing. Commit `4a65a40e03`, pushed. See §2 for what was NOT done

Each tool was **read in full with the file tools before anything was written about it**, which is
what the ruling governing the classification requires of a verdict. **Three classification verdicts
and three invocations authored, all LIVE**, each with its evidence citation, its reason, and its own
statement of what it does NOT assert.

**★ BOTH DIRECTIONS OF THE MECHANISM WERE EXERCISED ON THE WAY, and neither was contrived.** After
the verdicts but before the invocations, the classification STOPped with its OTHER stop — *"verdict(s)
naming a tool the guard state does not carry"* — which is the two tables refusing to drift apart.
And the confirming run made before Task 3's tool was registered STOPped naming
`gen_test_construction_evidence.py`, so the runner was **seen** catching a new guard rather than
trusted to.

**★ TASK 3's OWN TOOL IS REGISTERED IN THE ACT THAT CREATES IT** — invocation and classification
verdict both. That practice's absence is precisely what produced the condition [[OI-373]] records,
twice.

### Task 3 — the class-1 construction-evidence check. Commit `811244d57c`, pushed. See §1 for the finding

`tools/audit/gen_test_construction_evidence.py` → `tools/audit/test_construction_evidence.json`.
**The population is read from the committed artifact inventory's own class membership and is never
hand-listed**, and is reconciled with the graded set in BOTH directions on every run — which is the
tool's live half. **Every reading is pinned to the commit that inventory records** and taken from
git objects, so editing a test does not turn the check red; that is the [[OI-301]]/[[OI-305]] shape
avoided by construction rather than tolerated. **No test was edited, moved or run.**

**Registered expectation E3 — the large majority classify CODE-BUILT, and any SPEC-DERIVED-EVIDENCE
member is a finding rather than a defect — MET**: 103 of 123, with the 20 returned at §1.

---

## 6. What this batch did NOT do

- **No `src/` edit, no golden, no test changed, moved or run**; nothing under `tools/corpus/` or
  `tools/robust_stop/`; **no measurement of the analysis built, designed, scoped or run; no design,
  no repair, no fix to inference.**
- **No open-items row created, flipped or discarded** — including [[OI-372]], which stays exactly as
  found, and [[OI-373]], which §2 explains.
- **No decisions-register entry written** (the filtering ruling stands).
- **No file archived, retired, renamed or deleted.** Every retirement flag still waits behind the
  caller-check, which is NOT started. **The remaining 449 ignored files are NOT landed.**
- **No verdict authored for any tool this batch did not read in full.**
- **No ruled verdict written back onto the inventory's generated surface or its artifact** — the
  ruling record remains the carrier, as §7 of that record states.
- **[[OI-179]] stays OPEN and GATES. D-231 and #8 stand.**

---

## 7. The standing self-check (D-434) over this batch's own work

Run against the diff on disk rather than against the memory of writing it.

1. **★ THE ORDERED ACT THAT COULD NOT BE PERFORMED COHERENTLY WAS STOPPED RATHER THAN FORCED** —
   §2. The alternative, performing the flip and reporting the new red afterwards, would have been
   the workaround-then-declare shape the record forbids.
2. **★ THE RULED EDIT'S RESIDUE WAS DECLARED RATHER THAN QUIETLY WIDENED** — §3. Staging with `-f`
   is the repository's own practice, but using it silently would have hidden that the ruled remedy
   is partial.
3. **THE NEW TOOL WAS REGISTERED IN ITS OWN ACT**, and the check that proves it needed to be was run
   and read rather than assumed (§5, Task 2).
4. **THE COMMIT-SUBJECT LIMITATION WAS FOUND BY READING THIS BATCH'S OWN OUTPUT**, not by design: a
   build file classified SPEC-DERIVED on a commit subject alone, which is what put the per-row
   `where_the_statements_were_located` field and the published limitation into the artifact.
5. **ON D-253 IN EVERY DIALECT.** Every read of repository content went through Read / Grep / Glob.
   The shell was used for: the guard runs and the two new tools' own runs, `git add` / `git commit
   -F` / `git push`, the sanctioned changed-path enumeration, one `git show -s` of a commit named by
   explicit hash, and counting lines in a scratchpad file OUTSIDE the repository. **One attempt was
   refused by the guard and the refusal was correct**: an interpreter heredoc carrying a literal
   repository path, used for a bulk text substitution; the edit was made with the file tools
   instead. A second refusal fired on a `tail` whose path was a shell variable pointing outside the
   repository — a conservative deny, and the file was read with Read.
6. **ON THE FIGURES RULE (D-431).** Every count above names the artifact it was read from. The one
   place names are published rather than pointed at is the SPEC-DERIVED-EVIDENCE list, which the
   dispatch orders published by name.
7. **ON THE RESERVED-WORD CONVENTION.** Bare *score*, *key*, *measure*, *note*, *mode*, *register*,
   *root*, *part*, *rest*, *figure*, *interval*, *scale*, *beat*, *tie*, *stem* and *flat* appear in
   no non-musical sense in this batch's new prose: *measurement* carries the gauging sense, *value*
   the numeric one, *remark* the annotation sense, *the open-items register* and *register entry*
   are always compound, *`--check` mode* and *verify-only mode* are always qualified, and *tool* is
   used where *instrument* would have collided. **Two inherited terms are carried knowingly**: a
   row's *resolution*, which is the open-items register's own established word for the act rule (d)
   names, and *contract*, which is the record's own name for a ratified specification document.
8. **A GUARD-SET CONDITION WAS DIAGNOSED RATHER THAN REGENERATED AWAY** — §4.a. The obvious move
   was to re-run the generator until the artifact matched; the reason that is wrong is written
   into the runner itself, and reading it is what turned a recurring unexplained STALE into a
   located cause.
9. **WHAT THE SELF-CHECK DID NOT RESOLVE**, stated rather than left implicit: the class-1
   recognizers' reach is unmeasured (§1), and the artifact says so of itself; the guard set's own
   encoding exposure ([[OI-374]]) is untouched, as it was found; and §4.a's condition is declared,
   not repaired.
