# `FRAMEWORK.md` DP-C — the ruled narrowing of one sentence, SECOND WRITING (dispatch, 2026-09-20)

> **STATUS: WRITTEN, NOT STARTED.** Written by the Cowork writing side on 2026-09-20. **The user opens it
> with the CC run of his choice.**
>
> **★ WHAT THIS REPLACES.** `records/cc/instructions/cc_instruction_framework_dp_c_correction_2026_09_20.md`
> — the FIRST writing — was run and **STOPPED AT ITS TASK 1 WITH NOTHING WRITTEN**; its report is
> `records/cc/reports/cc_framework_dp_c_correction_report_2026_09_20.md`. **That dispatch is superseded
> by this one and is NOT to be run again.** Its banner still reads *"WRITTEN, NOT STARTED"*; that is stale
> and left standing (#12), and this paragraph is where the supersession is recorded. **What changed, and
> why, each established at its object by the writing side after that report was read:**
> 1. **The re-render of the `l0-l1` boot pack is DROPPED.** The first writing's §3 called `l0-l1` a live
>    subject. **It is not:** `tools/audit/gen_derivation_boot_pack.py` carries it in its `FROZEN` table,
>    dated 2026-09-04 (Ruling 17(a); `D-646`), and that file's `write_all` writes nothing into a frozen
>    subject's directory. The first writing's premise was the superseded wording that table preserves.
>    **Member (7) keeps the old sentence, correctly**: the pack records what its deriving session was given.
> 2. **The start-state guard condition is stated as the failing set it may carry**, not as "red".
> 3. **The boot-pack manifest's inherited mismatch is established BEFORE anything touches it** (Task 2),
>    so the edit cannot mask it (`D-669`).
> 4. **CC does NOT open the paper.** The first run could not render its pages. **On the user's ruling of
>    2026-09-20 — his words, *"I agree on A"* — the check at the page images was made by the writing side**
>    and is recorded at `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nine.md` §2. **This
>    batch writes the checked text verbatim and does not re-verify it at the paper.**
> 5. **Two defects of the first writing's correction note are repaired** (§3(c)): an over-wide negative
>    about rulings records, and a locator naming one section where the ground stands in two.
> 6. **The tracked-modification shape** names the one inherited modification the first run found.
>
> **★ THE WRITING SIDE'S RESTRAINT.** From hand-over, the writing side does not touch this file or any
> file named in §0's read-first block while the batch runs.
>
> **This batch narrows one sentence of one governing document, and regenerates one derived manifest
> twice. It opens no paper, stages no score, writes no brief, boots no session and derives nothing.**

---

## 0. Boot — read before any other act

You start clueless; a single-file opening instruction is not an exemption (ratified 2026-08-29, P-1;
`D-230`).

1. The ordinary session-start read: `CLAUDE.md` at its ruled membership (six spans, the membership read
   at that file's own "Build and test commands" block), `DECISIONS.md` whole, `STATUS.md`, and the
   derived gating answer (`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`).
2. `BUILD_AND_TEST.md` — conditional on running a tool whose command lives there. **Establish it and read
   the file if the condition is met.** (The first run established it NOT met; re-establish, do not relay.)
3. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seven.md` **§1 items 2 to 4** — the
   ruling this batch executes, and the surface it was taken on.
4. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nine.md` **whole** — the verification at
   the paper, the ruling that put it there, and this side's check of the first run's report.
5. `records/cc/reports/cc_framework_dp_c_correction_report_2026_09_20.md` **whole** — the first run.
   Its claims are **RELAYED**; the ones this batch rests on are re-established at Task 1.
6. This document, whole.

The bash rules of `CLAUDE.md`'s VS Code section bind every command this batch runs; that span's own
condition — any session that runs bash commands — is met here. **If any shell command is denied by the
guard, quote it verbatim in the report**, with the route taken instead. (The first run's report says one
such command was denied and does not say which.)

---

## 1. Task 0 and Task 1 — pin, then establish the start state

**Pin** with `git hash-object -w`, before any other act: this file; every file §0 names; `FRAMEWORK.md`;
`tools/audit/derivation_boot_pack.json`; `tools/audit/guard_state.json`;
`tools/audit/gen_derivation_boot_pack.py`; `tools/audit/claude_md_finer_archive.json`; and **every file
under `tools/audit/derivation_boot_pack/`**, in every subject directory there. Every later read comes from
`git cat-file blob`. **A read disagreeing with its pin is a STOP.**

**Establish and report, BEFORE any assertion rests on it:**

- **The guard set's current output, line by line.** **The failing set it may carry is: exactly the
  failing tools `tools/audit/guard_state.json` → `summary` → `failing_tools` names, PLUS
  `tools/audit/gen_derivation_boot_pack.py --check` — and that last one ONLY if its output is the single
  drift line `derivation_boot_pack.json does not re-derive`**, with no pack member of any subject named
  and no frozen-subject verification raised. **Any other failing guard, or any other line in that
  tool's drift output, is a STOP.** Do not restate the committed list in the report; name the artifact
  and report whether the run's set equals it plus that one (`D-431`). **The measure here is the failing
  SET, not `gen_guard_state.py --check`'s exit code**: that tool compares the whole run against the
  committed record, which the first run reports differing in the number of guards run as well. Report
  its exit code and every stale line it prints, and act on none of them.
- **How many sites in `FRAMEWORK.md` carry the target sentence.** Search the file for `26%`,
  `tie-breaking` and `tie breaking`, and report every line each returns. **Two sites are expected: one in
  the main text at design point DP-C, one in Appendix B at candidate decomposition (d). A third is a
  STOP.**
- **That the passage quoted at §3(a) stands in the file exactly as quoted — matched as a SUBSTRING.** Its
  first quoted line begins mid-line in the file: the closing words `reported by the work named.]` of the
  preceding label `[FACT — each reported by the work named.]` stand before it on the same line, and are
  not part of it. **A mismatch in the quoted words is a STOP.**
- **The tracked-modification shape** (§7), enumerated with the sanctioned route and reported.

**Locate by the words, never by a line number** (`D-307`). The main-text site sits under the heading
`**DP-C — Is segmentation decided before, with, or after chord identity?**`, inside `## 9. Architecture
decisions` → `### The design points`. The Appendix B site sits under `## S4. The candidate
decompositions, enumerated`, in the paragraph headed `**(d) Segment first, then label.**`

---

## 2. Task 2 — establish the manifest's inherited mismatch, BEFORE `FRAMEWORK.md` is touched

**Why this comes first.** The first run found `gen_derivation_boot_pack.py --check` failing on the
manifest alone, where `tools/audit/guard_state.json` records it passing. **Its cause was not
established.** The generator's own `frozen_block` says a frozen subject's member records in the manifest
are built *"from the sources AS THEY STAND TODAY"* — so a change to a source document can move the
manifest while no pack directory moves. **That is where to look; it is not a finding**, and the
`FRAMEWORK.md` edit of Task 3 will move the manifest again, so the two must be separated or the second
masks the first (`D-669`: a maintenance act establishes the cause before it touches the mechanism).

1. Run `python tools/audit/gen_derivation_boot_pack.py` in **write mode, with no `--subject`**. Before
   running it, establish at the generator's `build()` and `write_all` which directories write mode can
   write, and report it. **Then prove at the objects that NO file under `tools/audit/derivation_boot_pack/`
   moved** — every one re-hashes to its pin. **Any pack file moving is a STOP**, and the manifest is
   restored from its pin before stopping.
2. **Report the difference** between the manifest's pinned blob and the regenerated file, **every changed
   key path**, and for each: which input the record is built from, read at the generator — a source
   document, or the generator's own authored tables — and whether that input has changed since the
   manifest's own last commit (`git log` by path; for the generator, its own history). **A changed
   record whose input has NOT changed since that commit, or whose input cannot be named at the
   generator, is a STOP** — the cause resists establishment, and no fix is taken on a guess (`D-669`).
3. Run `--check` and report it. **It must now pass**, printing the three frozen subjects.
4. **Commit** `tools/audit/derivation_boot_pack.json` alone, staged by explicit path, with a message that
   says in terms it is the **inherited** manifest mismatch, cause established, and names the changed
   inputs. **This commit carries nothing of the `FRAMEWORK.md` correction.**

---

## 3. Task 3 — the one correction, and nothing else

The authority is the user's ruling of 2026-09-20 recorded at entry 207 §1 item 4: **alternative A —
narrow the sentence in place to what the authors report, with the former wording preserved.** The filing
is the convention's **branch two** — a live governing surface whose body is corrected with the former
wording preserved in place (**#12**). **No other edit to `FRAMEWORK.md` is authorized by this batch.**

### (a) The passage as it stands, quoted from the file

The closing sentence of DP-C reads, whole:

> One further measurement is worth carrying: with perfect tie-breaking
> between equally-scoring labels, one published segment-then-label system would still remove only 26% of
> its errors — the rest needs tonal context and voice leading its decomposition does not admit. [FACT.]

**Its scope ends there.** The `[FACT — each reported by the work named.]` label standing immediately
BEFORE *"One further measurement"* belongs to the list of measurements above it and **is not touched**.
Everything else in DP-C — its candidates, its CHOSEN line, its rival's ground, and the ground for
excluding the rival — **is not touched**.

### (b) The replacement text, written in place of the quoted sentence, VERBATIM

> One further measurement is worth carrying, and the conditions it was made under carry with it. In one
> published segment-then-label system, whose chord naming considers harmonic context only through a
> single tie-breaking rule for the resolution of diminished seventh chords, the segmentation for the
> labeling experiment was taken from the positions of the chord labels in the answer key, and every
> labeling error on every excerpt of the corpus was then examined and classified, to understand what
> error remains when full tie breaking is enabled. The authors report that perfect tie-breaking between
> equally-scoring labels would eliminate three of those error classes — 26% of the errors — and they
> call that the maximum improvement improved tie-breaking can give. For the rest they name a different
> cause or a different remedy class by class: an incomplete chord identifiable only through tonal
> function in context (12% of the errors); a class they say might perhaps be resolved through a deep
> understanding of structural voice leading, whose passages they expect would probably coincide with
> disagreement among human analysts (15%); beat information added to the note weights for two classes
> (23% and 6%), with heavily syncopated music still a problem; a two-pass system over the chord names
> for one idiomatic sequence (6%); and the answer key itself, or timing variation in the performed MIDI
> file, for two more (6% and 5%). They add that knowledge of adjacent chord labels might be used to
> adjust the chord-label weights, and that this would make the calculation of chord labels much more
> difficult, because the weights across a piece would then influence one another. [FACT — Pardo and
> Birmingham 2002, pp. 31–35; each class percentage is the value printed in Figure 8, in small
> numerals.]

**Write it verbatim.** Every percentage in it is a numeral printed in that paper's Figure 8, or the
paper's own 26%; **none is a sum, and none may be added to, rounded or re-expressed** (#17f, `D-431`).
**It was checked at the paper's page images by the writing side** (entry 209 §2) **and is NOT re-verified
here; do not open the paper.** Re-wrap the paragraph to the file's own line width; no other formatting
change.

### (c) The correction note, placed immediately beneath the corrected paragraph, VERBATIM

Its form is taken from two correction notes this file already carries, each about a claim from a
published source — the one beneath *"Why metric strength earns its place"* in §5, and the one headed
*"★ GROUND 2 WAS NARROWED HERE"* at DP-K.

> **★ NARROWED HERE 2026-09-20 ON THE USER'S RULING, WITH THE FORMER WORDING PRESERVED IN PLACE (#12.)**
> The ruling is recorded at `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seven.md` §1
> item 4 — the user's words, *"I agree: A"* — taken on the self-contained surface that entry's §1 item 2
> sets out, whose three alternatives were: narrow the sentence in place to what the authors report (A);
> keep the 26% and delete the second half (B); strike the whole sentence (C). **No separate rulings
> record was written for this ruling** — at a listing of `records/cowork/rulings/` on 2026-09-20, no
> file name there carries a date after 2026-09-11 — so the handoff entry is the record this note cites;
> whether a rulings record is owed for it is not settled here. **THE FORMER WORDING WAS:** *"One further
> measurement is worth carrying: with perfect tie-breaking between equally-scoring labels, one published
> segment-then-label system would still remove only 26% of its errors — the rest needs tonal context and
> voice leading its decomposition does not admit. [FACT.]"* *Why it was narrowed:* the source's second
> independent extraction,
> `reading_pass/extracts_second_pass/pardo-birmingham-2002-algorithms-for-chordal-analysis.md`, bears on
> it in two places. **First, the attribution was too wide** (that extract's §9.4 item 2): of the seven
> error classes the 26% does not cover, the authors attribute two to tonal context and to structural
> voice leading, and for the other five they name beat information, a two-pass relabeling, the answer
> key itself and performed timing. **Second, the measurement's own conditions were absent** (that
> extract's §5.1, which records the segmentation as taken from the answer key): the errors were counted
> under given boundaries, so the figure bears on labeling and not on what a segmenter of that design
> produces — which is the question this design point decides. **The replacement text was checked at the
> paper's printed pages 31–35, at the page images, by the writing side on 2026-09-20**, on the user's
> ruling of that date that the check be made there, recorded at
> `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nine.md` §2. **DP-C is not reopened and
> its choice is unchanged:** its stated grounds are the ledger's **C27**, three measurements and one
> formal result, and this sentence stands, then as now, as a further measurement worth carrying rather
> than as a ground.

### (d) ★ APPENDIX B IS NOT EDITED, AND NEITHER IS ANY OTHER PASSAGE

The second site — Appendix B's candidate decomposition **(d)** — **is left exactly as it stands. No note
is added to it, and no caveat is added at the appendix's head.** Grounds, each read at its object by the
writing side:

1. **Appendix B's own banner** reads *"★ NEVER EDITED AFTER STAGE TWO OPENED."* and its heading *"APPENDIX
   B — The first-stage draft, whole and unedited"*.
2. **§3t of `records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md`** records the
   question *"whether a dated appendix's present-tense sentence about a now-settled question is
   branch-one filing or something owed"*, then *"The question is therefore OWED and NOT BLOCKING"*, and
   says of itself *"It does not settle the branch-one question it names."* This batch does not settle it.

**Nor is any other passage of `FRAMEWORK.md` touched** — including §14.1's list entry that restates the
human-human-agreement finding DP-K's correction narrowed, which the previous sitting reported to the
user (entry 208 §1 item 3) and which is outside this batch.

### (e) Then, at the rendered objects

1. Re-run the generator in **write mode**, and prove again that **no file under
   `tools/audit/derivation_boot_pack/` moved** (re-hash against the pins). **Any pack file moving is a
   STOP.**
2. **Report the manifest's difference against Task 2's commit, key path by key path.** **Expected, stated
   before the act (#17(b)):** only records built from `FRAMEWORK.md` move — **establish at the generator
   which records those are, and report it, before running**. **A moved record built from any other source
   is a STOP.**
3. Run `--check`: **it must pass.**
4. **Prove the `FRAMEWORK.md` edit by a blob-to-blob difference against its pin**: the only changed region
   is DP-C's closing sentence and the note beneath it; every deleted word either still stands in the
   corrected paragraph or is preserved verbatim inside the note; **Appendix B is byte-identical.**
5. Run the whole guard set again. **Its failing set must be exactly `guard_state.json`'s committed
   `failing_tools`, and nothing more** — the failing set, as at Task 1, not the exit code of
   `gen_guard_state.py --check`, which is reported and not acted on. A guard that passed at Task 1 and fails now is a STOP** — report it;
   do not fix it.
6. **Commit** `FRAMEWORK.md` and `tools/audit/derivation_boot_pack.json`, staged by explicit path, with a
   message naming the ruling (entry 207 §1 item 4) and the verification record (entry 209 §2).

---

## 4. Task 4 — the close

1. **`STATUS.md`** — this batch's own entry, as a **pointer** to this batch's report (the OI-222 pointer
   convention), and the forward bound re-aimed in the same act with
   `tools/audit/gen_status_batch_bound.py --apply`, **following that tool's own documented convention for
   an aiming, read at the tool**. **Any path that `--apply` writes other than the ones the tool's own
   documentation names as its outputs is a STOP.**
2. **Commit** `STATUS.md` and every file `--apply` wrote, **plus** this dispatch, the first writing, the
   first run's report and this batch's report — each staged by explicit path.
3. **Push to remote.** After `STATUS.md` is updated and before reporting back, push every branch that
   received a commit this session to the central remote. Use the remote name the repository is configured
   with (check `git remote -v`; typically `origin`). **If a push fails — authentication, network,
   non-fast-forward — report it; do not skip it silently, and never pass `--force` without the user's
   explicit approval.** Name the pushed branches and every commit hash in the report.
4. **The report**, on the ruled stop form, at
   `records/cc/reports/cc_framework_dp_c_correction_second_report_2026_09_20.md`.

**The standing self-check runs before the report is written** — the actual diff on disk of every touched
file, read as a diff and not from the memory of writing it, against the guiding principles, the
conventions and `DEFECT_TYPES.md`.

---

## 5. Done

Done when: the start-state failing set is as §1 allows; Task 2's cause is established record by record
and committed alone; `FRAMEWORK.md` carries the one corrected paragraph and its note and **no other
edit**, proven blob to blob; **Appendix B is byte-identical**; **no file under
`tools/audit/derivation_boot_pack/` moved at any point**; `--check` passes; the closing failing set is
exactly the committed one; `STATUS.md` carries the entry; the branches are pushed; and every STOP met is
written up.

---

## 6. STOPs

A read disagreeing with its pin; a failing guard at Task 1 outside what §1 allows, or a boot-pack drift
line other than the manifest's; a third site of the sentence in `FRAMEWORK.md`; §3(a)'s quoted words not
matching the file; any file under `tools/audit/derivation_boot_pack/` moving; at Task 2, a changed
manifest record whose input did not change since the manifest's last commit or cannot be named; at Task
3, a moved manifest record built from a source other than `FRAMEWORK.md`; a blob-to-blob difference
showing a deleted word neither standing nor preserved; any change to Appendix B; a guard that passed at
Task 1 failing after the edit; `--apply` writing a path its own documentation does not name; **opening
the paper**; any act outside §7.

---

## 7. The footprint

**Edited:** `FRAMEWORK.md` — the one correction of §3 and nothing else; `tools/audit/derivation_boot_pack.json`
— regenerated twice (Task 2, Task 3(e)); `STATUS.md`, and the files the forward bound's `--apply` writes.
**Created:** this batch's report. **Committed** besides those: this dispatch, the first writing and the
first run's report (§4 item 2).

**No tool source is edited**, except the forward bound's own per-batch re-aiming,
`tools/audit/gen_status_batch_bound.py --apply`, **EXCEPTED BY NAME** (Ruling 5 of
`records/cowork/rulings/cowork_rulings_2026_08_26_amendment_landing_sitting.md`).

**Written into NO directory under `tools/audit/derivation_boot_pack/`.** The generator's `FROZEN` table
carries three subjects; whatever that directory holds, nothing in it is written.

**Not done at all:** no paper opened; no build, no test, no golden, no measurement of the analysis;
nothing under `tools/corpus/`, `tools/robust_stop/` or `src/`; **no extract edited**; **no other
governing document amended**; **no open-items row created, flipped or discarded**; **no
decisions-register entry and no `D-NNN` allocated**; no score staged; no brief written; no session
booted; **`tools/audit/guard_state.json` not regenerated**.

**The tracked-modification assumption, as a SHAPE with a STOP.** This batch expects untracked Cowork
material — **changed paths under `records/cowork/handoff/` are expected as UNTRACKED additions, not as
tracked modifications**, which is what the first run found there — and expects
**tracked-and-modified files under `reading_pass/`**, which a third backup dispatch is owed for. **It also expects ONE tracked modification outside that directory:
`tools/audit/claude_md_finer_archive.json`**, found by the first run before any act of its own. **The
writing side does not know what modified it; this batch does not touch it, does not commit it, and
reports whether it still stands as pinned.** **Any OTHER tracked modification this batch did not make IS
a STOP**, and the batch reports it rather than working around it.

---

*Provenance: written by the Cowork writing side, 2026-09-20, after reading the first run's report whole
and checking its central claims at the objects: the `FROZEN` table, `write_all`, `check_all`, `main` and
`frozen_block` at `tools/audit/gen_derivation_boot_pack.py`; the committed `summary` at
`tools/audit/guard_state.json`, which records `gen_derivation_boot_pack.py --check` passing; the target
sentence at both `FRAMEWORK.md` sites and at the frozen member (7); and the 2026-09-04 freeze report.
**Every passage quoted here was read at its file this sitting**: DP-C whole and its closing sentence;
Appendix B's heading and banner; the two existing correction notes, for the note's form; §3t of the
2026-08-31 rulings record; the second extract's §5.1 and §9.4. §3(b)'s text is the first writing's §2(b),
unchanged, and was checked clause by clause at the paper's PDF pages 5 to 9 this sitting, at the page
images (entry 209 §2). The rulings-record negative in §3(c) rests on one listing of
`records/cowork/rulings/` taken this sitting and on nothing else. No figure of this project's own
measurement is restated (#17f, `D-431`). No shell command was run, in the container or on the device, by
the writing side.*
