# CC INSTRUCTION — THE DECISION RULES CONSOLIDATED, AND D-658's HOME CORRECTED (2026-09-21)

**What this batch does.** It writes ONE new section into `CLAUDE.md`'s Conventions stating the
combined rule for a decision surface **and the order in which its parts apply**, citing each part at
its own home rather than copying it; and it corrects **D-658** at its home in
`cowork_audit_protocol.md`, where the rule as written is now false. It also commits the previous
batch's finished-but-uncommitted work, which is why it opens the way it does.

**Why it exists.** On 2026-09-21 the user gave a four-clause standing ruling on the form of a
decision surface, recorded whole at
`records/cowork/rulings/cowork_rulings_2026_09_21_decision_surface_form_sitting.md`. Its clause 4
requires every decision surface to carry a recommendation. **That reverses the fourth requirement of
D-658, whose home still states the opposite**, and the user named that falsity himself. He quoted the
heading — *"Where the record does not settle the question, the surface that returns it to the user
gathers FACTS and makes NO recommendation"* — said it **"is not correct"**, and then, of its last
clause, **"'makes NO recommendation' is directly false."** In the same turn he directed that the scattered
decision rules be fixed, because he does not know all the places they are kept. The Cowork side put a
decision surface with six alternatives and he ruled the one this dispatch executes: **one governing
statement in `CLAUDE.md` Conventions, citing rather than moving.**

**THE WRITING SIDE'S RESTRAINT, declared.** This dispatch is final at hand-over. The writing side
will not touch it, nor any file it names, while this batch runs.

**TWO STATES THIS DISPATCH IS WRITTEN KNOWING, because a dispatch written without them stops on its
own start state.**

- **THE TWO REFS DISAGREE, AND THAT IS THE EXPECTED STATE.** `.git/refs/heads/master` reads
  `7d7291f401d05052240d76078db175ce160e8b91`; `.git/refs/remotes/origin/master` reads
  `ef4fad940d806edf8f84eb9a895f88d70a9bbcf2`. Both were read with the file tools by the Cowork side
  at this sitting. The previous batch
  (`records/cc/instructions/cc_instruction_l2_withheld_documents_2026_09_21.md`) committed at its
  Task 0, then stopped at its own 5(e) — so it never reached its §6 at all: **neither its second
  commit nor its push happened**, and its Tasks 1 to 3 are finished work sitting uncommitted. **Task
  0 below is written for two differing refs and is not the usual "both must read `<hash>`" shape.**
- **`tools/audit/gen_guard_classification.py` STOPs, AND IT WAS ALREADY STOPPING BEFORE THAT BATCH
  RAN.** Established at the objects by the Cowork sitting recorded at handoff entry 225 §2: that
  tool's population comes from `gen_guard_state.AUTHORED` and not from the committed artifact; two
  tools were already in that table before the last batch ran; and a search of the classification
  source returns no occurrence of any of the three tool names, so none carries an authored verdict.
  **Clearing it needs verdicts for three tools, two of them older debt. It is not this batch's work.**
  **Its STOP is CARRIED, NOT CHASED: report it whole and carry on. It is not a STOP for this batch.**

---

## 1. Bars

**B1 — ONE TOOL SOURCE AND NO OTHER IS EDITED BY THIS BATCH:** `tools/audit/gen_status_batch_bound.py`
(Task 5, the forward-bound re-aiming), which this bar excepts **by name** so that the bar cannot
contradict its own task. **Every other tool source is untouched** — including
`tools/audit/decisions/reaim_home_anchors.py`, `tools/audit/decisions/gen_decisions_register.py`,
`tools/audit/decisions/gen_cluster_dispositions.py`, `tools/audit/gen_session_start_read_size.py`,
`tools/audit/gen_defense_share.py`, `tools/audit/gen_guard_state.py` and
`tools/audit/gen_guard_classification.py`. If a task below seems to need a second tool edited, that
is a bar contradicting a task — **STOP and report it; do not resolve it.**

**B2 — `tools/audit/gen_derivation_boot_pack.py` IS NOT EDITED, IN ANY WAY, AND IS NEVER RUN BARE.**
Not `WITHHELD`, not `EXTRAS`, not `VERDICTS`, not `CRITERION`, not `FROZEN`, not `DATE`, not one
comment. It is run in `--check` mode only, and only where the guard set runs it. **A bare run of it
is a STOP.**

**B3 — NOTHING under `tools/audit/derivation_boot_pack/` is read for content, written, deleted,
renamed or moved. Nothing is authored into `WITHHELD`, `EXTRAS`, `VERDICTS`, `CRITERION` or
`FROZEN`.** The second half of the pack-build dispatch is a separate act and nothing here
anticipates it.

**B4 — no `src/` file, no build, no test, no golden, no score corpus, nothing under `tools/corpus/`
or `tools/robust_stop/`, no measurement of the analysis, no paper, no reading-pass extract, no
score.**

**B5 — THE RENDERED REGISTER FILES ARE NEVER HAND-EDITED.** `DECISIONS.md` and every
`decisions/group_*.md` change **only** as `gen_decisions_register.py` writes them. The decisions
register's own rule (d) in `CLAUDE.md` says so in its own words: *"the register is a GENERATED
surface — change `tools/audit/decisions/backbone_decisions.json` and regenerate
(`gen_decisions_register.py`; its `--check` and `gen_cluster_dispositions.py --verify` guard drift,
quote fidelity and reference resolution), never hand-edit the rendered files"*.

**B6 — NO OPEN-ITEMS ROW is created, flipped or discarded. NO DECISIONS-REGISTER IDENTITY IS
ALLOCATED and no `D-NNN` is created.** Register rule (c) is suspended in writing at
`cowork_register_rule_c_suspension_2026_08_28.md` while the two discard checks are red, so the user's
ruling of 2026-09-21 cannot be given an identity by this batch. **What this batch changes in the
register is one EXISTING entry, D-658, and nothing else.** No entry is added, removed or
re-classified, and no other entry's fields are touched by hand.

**B7 — `tools/audit/claude_md_finer_archive.json` is held back**: not staged, not reverted, not
investigated. Its modification's cause is still established by nobody and establishing it is not this
batch's work.

**B8 — NO FIGURE IS TRANSCRIBED INTO ANY ARTIFACT FROM THIS DISPATCH (D-431).** Every count this
batch reports is measured by the tool that owns it and cited to its artifact. **The figures this
dispatch itself states are exactly these, and each is a START-STATE BAR rather than a value to be
written anywhere:** the two ref hashes above, and the three interim-carrier sizes at 0(f), each
measured at a directory listing by the Cowork side. **None of them is written into any artifact by
this batch.**

**B9 — NO GOVERNING DOCUMENT IS AMENDED EXCEPT THE THREE NAMED BY THEIR OWN TASKS:** `CLAUDE.md`
(Task 2), `cowork_audit_protocol.md` (Task 3) and `STATUS.md` (Task 5). Not `ARCHITECTURE.md`, not
`FRAMEWORK.md`, not `OPEN_ITEMS.md`, not `cowork_design_doc_template.md`, not
`cowork_notation_adoption_increment.md`, not `cowork_adjudication_dossier.md`. **In each of the
three, no superseded wording leaves the page.** Task 2 is an insertion and changes nothing existing.
Task 3 replaces three passages whose content the user's ruling reversed, and **each replaced passage
is reproduced verbatim, immediately beneath its replacement, inside a dated
preserved-former-wording block (#12)** — so nothing is lost and nothing is quietly rewritten. Task 5
adds one `STATUS.md` entry and rewrites no existing sentence of it. `STATUS_ARCHIVE.md` changes only
as the forward bound's own `--apply` writes it.

**THE FOOTPRINT ASSUMPTION, written from the paths this batch's own tasks touch and from nothing
wider.** This batch's own orders **modify** exactly these existing files: `CLAUDE.md` (Task 2),
`cowork_audit_protocol.md` (Task 3), `tools/audit/decisions/backbone_decisions.json` (Task 4, by hand
and then by `reaim_home_anchors.py`), `DECISIONS.md` and the `decisions/group_*.md` files the
generator rewrites (Task 4, by the generator only), `STATUS.md` (Task 5),
`tools/audit/gen_status_batch_bound.py` (Task 5), `STATUS_ARCHIVE.md` (Task 5, by the forward bound's
`--apply`), and — as the ordinary consequence of running them —
`tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json`,
`tools/audit/status_batch_bound.json`, **`tools/audit/changed_paths_establishment.json` — which the
guard set rewrites on every run, at 0(g) and again at 7(d)** — and the guard set's other artifacts.
It **creates** exactly one new file: your report. **Every other path this batch commits is already on disk from the previous
batch or from the Cowork side and is committed unchanged**, and §8 orders each one's unchangedness
proved.

**THE ORDERING RULE, and it is a rule rather than a convenience.**
`tools/audit/gen_session_start_read_size.py` measures what an ordinary session reads, and its
membership is `CLAUDE.md`, `STATUS.md` and `DECISIONS.md`; `tools/audit/gen_defense_share.py`
measures the marked-defense share of `CLAUDE.md`'s six session-start spans. **So Task 2's edit to
`CLAUDE.md` moves both artifacts; Task 4's regeneration of `DECISIONS.md` and Task 5's edit to
`STATUS.md` move the read-size artifact for certain, and the defense-share artifact too if that
generator reads through the other one.**

*(What is established and how far it reaches: both statements above about WHAT each artifact measures
are read at the two ARTIFACTS — `tools/audit/session_start_read_size.json`'s `the_membership` block
and `tools/audit/defense_share.json`'s own `what_this_is` — by the Cowork side at this sitting.
**Neither generator's SOURCE was opened.** The further claim that `gen_defense_share.py` carries
`import gen_session_start_read_size as reader`, and that an edit to `STATUS.md` therefore moves both,
is **RELAYED** from handoff entry 222 §4 through the previous dispatch and was checked by nobody on
this side. **Confirm the coupling at the two tool sources before you rely on the ordering, and report
what you found.**)*

Therefore the two read-size generators run **last**, after `CLAUDE.md`, `DECISIONS.md` and
`STATUS.md` are all final, and nothing after them writes to any of the three. **That ordering is
correct whichever way the relay turns out**, so a surprise at the coupling is a finding to report
rather than a reason to re-order the tasks.

---

## 2. Task 0 — the start state, and the previous batch's work committed

**0(a) — pin this dispatch**, and take every later re-read of it from its blob:

```
git hash-object -w records/cc/instructions/cc_instruction_decision_rules_consolidation_2026_09_21.md
```

Record the hash and report it.

**0(b) — the refs, expected to DISAGREE.** Read `.git/refs/heads/master` and
`.git/refs/remotes/origin/master` **with the file tools** (`D-253`; never `git rev-parse`).
**`master` must read `7d7291f401d05052240d76078db175ce160e8b91` and `origin/master` must read
`ef4fad940d806edf8f84eb9a895f88d70a9bbcf2`.** If they now agree, or if `master` has moved further,
**STOP**: something ran that this dispatch does not know about, and the whole start state is void.
Report both values as found.

**0(c) — the working tree, and the corruption check.** Take the enumeration with
`python tools/audit/changed_paths.py` — the sanctioned route, the shell-read guard having refused a
working-tree `git diff` to an earlier batch. Report it whole. **Nothing may be staged when this batch
opens**; if anything is, **report exactly what is staged and STOP.**

Then, before anything is built on top of that tree: a Cowork session's landing and a CC session's
write can both be truncated by an interrupted write. **Check the last bytes of each TEXT file that
this batch will commit** — that is, the paths 0(e), 0(f) and §8(a) name, and no others. **A trailing
NUL byte, or a final line that breaks off mid-word, is a STOP** — name the file and stop there; do
not repair it.

**Check nothing else, and in particular check no binary and nothing in the held-back untracked
population** — the PDFs, the `.mscx`, `scratch_artifacts/` and the rest §8(a) names. **A binary
file's last bytes are not text and reading them as text would produce a STOP that means nothing.**

**0(d) — the five start-state facts, proved at the objects with the file tools.** Report what you
found for each, as found. **Any one failing is a STOP; report which, and what you found instead. Do
not repair it.**

1. `cowork_audit_protocol.md` carries the line
   `### Where the record does not settle the question, the surface that returns it to the user gathers FACTS and makes NO recommendation`
   **exactly once**. Report the line number you find it at.
2. That same file carries the text `NO\nRECOMMENDATION AT ALL.**` — that is, a line ending in `and NO`
   followed by a line beginning `RECOMMENDATION AT ALL.**` — **exactly once**.
3. `tools/audit/decisions/backbone_decisions.json` carries an object whose `"id"` is `"D-658"`
   **exactly once**. Report that object's `"home"`, `"status"` and `"title"` verbatim.
4. `CLAUDE.md` carries the line
   `- **THE WHOLE DECISION SURFACE IS DELIVERED AS USER-VISIBLE TEXT BEFORE ANY CHOICE QUESTION (user`
   **exactly once**, and the line
   `- **WORKING-TREE FILES ARE READ WITH THE FILE TOOLS; SHELL ACCESS IS LIMITED TO GIT OBJECT QUERIES BY`
   **exactly once**, the second occurring after the first. Report both line numbers.
5. `cowork_register_rule_c_suspension_2026_08_28.md` exists and its owed-entries list is still the
   placeholder comment `<!-- THE DERIVED LIST GOES HERE.` **Report what you find, whichever it is.**
   This is a fact about the register's blocked state that the report carries forward; **it is not a
   STOP either way and this batch does not fill that list.**

**0(e) — COMMIT ONE: the previous batch's own finished work.** That batch ran its Tasks 1 and 2 and
the first four parts of its Task 3, and stopped at its own 5(e) — the closing guard capture — before
its second commit, so everything those parts produced is on disk and uncommitted.
**This batch moves the same artifacts** — `STATUS.md`, `session_start_read_size.json`,
`defense_share.json`, `status_batch_bound.json` and the guard artifacts — **so that work is committed
first, or the two batches' work becomes inseparable in one commit.** That is the reason for this
step and it is the whole of it.

Commit, by explicit path and never a directory pathspec, exactly the candidate set that batch's own
§6(a) names:

1. `tools/audit/gen_l2_withheld_documents.py`
2. `tools/audit/l2_withheld_documents.json`
3. `tools/audit/gen_guard_state.py`
4. `tools/audit/gen_status_batch_bound.py`
5. `tools/audit/status_batch_bound.json`
6. `tools/audit/session_start_read_size.json`
7. `tools/audit/defense_share.json`
8. `STATUS.md`
9. `STATUS_ARCHIVE.md`
10. `records/cc/instructions/cc_instruction_l2_withheld_documents_2026_09_21.md`
11. `records/cc/reports/cc_report_l2_withheld_documents_2026_09_21.md`
12. the guard set's own artifacts, **only those 0(c)'s enumeration actually reports as modified** —
    name each one in your report rather than assuming which moved.

**0(c)'s enumeration is what establishes the actual set; this list is a guide to it, not a statement
of it.** *(The list is RELAYED from that dispatch's §6(a), which the Cowork side read whole, and from
handoff entry 225 §0, which relays CC's own enumeration.)* **Prove the staged set is exactly the
paths this step names and nothing else before committing.** Do not push yet.

**0(f) — COMMIT TWO: the interim carriers.** The standing interim-carrier clause says a sitting
record is written in the turn its ruling is given and lands in git at the next dispatch's Task 0.
**This is that task.** Commit, by explicit path:

1. `records/cowork/rulings/cowork_rulings_2026_09_21_decision_surface_form_sitting.md`
2. `records/cowork/rulings/cowork_rulings_2026_09_21_l2_withheld_documents_sitting.md`
3. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty_five.md`
4. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty_six.md` — **only if it exists
   on disk.** It is the handover entry of the Cowork sitting that wrote this dispatch, written after
   this dispatch was landed, so this dispatch states **no size for it**: report the size you find.
   **If it does not exist, say so and commit the other three. Do not wait for it.**

**Establish each rather than asserting it**: take its size by the content-addressed route
(`git hash-object -w --no-filters <path>`, then `git cat-file -s <identity>`), read its last
non-empty line, and report both. **A tail that is not ordinary text, or a NUL byte, is a STOP.**
Members 1, 2 and 3 must measure **16,071**, **14,581** and **33,970** bytes — the figures the Cowork
side measured at the directory listings — and **a different figure at any of them is a STOP**,
because nothing in this batch may have changed them. **The writing side will not touch any of the
three while this batch runs**, which is what makes those three figures safe to bar on. Do not push
yet.

**0(g) — THE OPENING GUARD CAPTURE, and it is taken AFTER the two commits above, not before.** Run
the guard set once and save the capture **outside** the repository working tree; name the file in
your report. Record every guard's verdict.

**★ WHY THE ORDER IS THIS WAY ROUND, and it is a correctness matter rather than a preference.**
**Running the guard set WRITES artifacts** — among them `tools/audit/changed_paths_establishment.json`,
because the guard set invokes `tools/audit/changed_paths.py` with `--establish` and that tool has no
verify-only mode: it writes its establishment artifact on every run. *(Established at the objects by
the Cowork sitting recorded at handoff entry 225 §2, which read both `changed_paths.py`'s establish
mode and `gen_guard_state.py`'s authored list.)* **Taking the capture BEFORE the commits would put
this batch's own artifact movements inside a commit whose whole purpose is to carry the PREVIOUS
batch's work** — which is the conflation 0(e) exists to prevent. **Every artifact this capture moves
belongs to COMMIT THREE at §8(a), never to commit one or two.**

**Expected and to be reported as found rather than assumed:** a standing line `STALE vs the run:
guard_state.json does not re-derive` at the head of the capture, and a non-empty failing set. *(Both
are RELAYED from handoff entries 222 §3 and 225 §2; neither was checked by the writing side, which
has no shell.)* **That standing line predates this batch and is CARRIED, NOT CHASED.** **If either
expectation is not what you find, report it and carry on** — neither is a STOP.

---

## 3. Task 1 — CAN THE REGISTER BE REGENERATED? Measured before anything is edited

**This task edits nothing. It is the gate on Tasks 3 and 4 and it runs at the untouched tree.**

Register rule (c) is suspended while `tools/audit/decisions/apply_soft_discard.py --check` and
`tools/audit/decisions/apply_residue_discard.py --check` are red. **Whether that blocks a
REGENERATION of the register is not established by the writing side** — those are different tools
from the register generator, and neither was run or read at the tree. **This task establishes it.**

Run these five, at the untouched tree, and report every output and every exit code **verbatim**:

```
python tools/audit/decisions/gen_decisions_register.py --check
python tools/audit/decisions/gen_cluster_dispositions.py --verify
python tools/audit/decisions/reaim_home_anchors.py --check
python tools/audit/decisions/apply_soft_discard.py --check
python tools/audit/decisions/apply_residue_discard.py --check
```

**How to read the results:**

- **The two `apply_*_discard.py --check` runs are EXPECTED to be red.** That is the suspension's own
  premise. **Report them and carry on. They are not a STOP** and this batch does not repair them.
- **`reaim_home_anchors.py --check` is EXPECTED to report a non-zero drift count.** The writing side
  compared D-249's `home` field, which reads `CLAUDE.md:1781-1793`, against that bullet's actual
  position in the current `CLAUDE.md`, which it read at a different place. **That comparison is the
  writing side's own and is bounded**: that tool resolves a start line through
  `gen_cluster_dispositions`'s own normalising `find_start_line`, which the writing side did not run.
  **Report the drift list whole, as found.** A pre-existing drift is **not** a STOP: Task 4 re-aims
  it in the same act that adds to it.
- **`gen_decisions_register.py --check` and `gen_cluster_dispositions.py --verify` ARE THE BASELINE,
  AND A PRE-EXISTING PROBLEM IN THEM IS NOT A STOP.** The register carries several hundred entries
  homed across many documents that have been edited for weeks, and **the writing side does not know
  their state** — it ran neither tool and has no shell. **So: record whatever these two report here,
  entry by entry, as THE BASELINE.** A missing or mismatched quote at an entry this batch does not
  touch is **carried and reported, not chased and not repaired** — the same shape this project
  already uses for the standing guard-capture line.
  **The one thing that IS a STOP here:** a missing or mismatched quote at **D-658**, or at any entry
  homed in `CLAUDE.md` or in `cowork_audit_protocol.md` — the two files this batch edits. Those
  entries must be sound BEFORE the edit, or the edit cannot be told apart from what was already
  wrong. **Report which entry, and stop there.**
- **`reaim_home_anchors.py --check` printing `REFUSED` is a STOP, and it means something specific.**
  That tool refuses when re-serializing the untouched backbone is not byte-identical to the committed
  file. **If it refuses here, at the untouched tree, then the committed backbone is not in the
  serialization that tool expects, and Task 4's hand-edit cannot be made safely** — any write would
  reformat the whole file. **Report the refusal whole and STOP.** Do not reformat the backbone to
  satisfy it.
- **If `gen_decisions_register.py --check` cannot run at all** — a traceback, an import failure, a
  refusal — **STOP and report it whole.** Tasks 3 and 4 depend on the register being regenerable, and
  if it is not, the D-658 correction cannot land as designed and the batch must not attempt it.
  **THE BATCH THEN STOPS HERE AND RUNS NOTHING FURTHER — not Task 2 either.** Task 2's insertion into
  `CLAUDE.md` would drift register anchors that only Task 4 re-aims, and would move two artifacts
  that only Task 5 regenerates, so running it alone leaves the tree half-done. 0(e) and 0(f) have
  already committed, so **stopping here leaves a clean tree and the consolidation waits for the
  register's repair** — which is a member boundary with nothing half-done (**D-672**), and is the
  right stop.

---

## 4. Task 2 — the consolidated section in `CLAUDE.md` Conventions

**Insert the block below into `CLAUDE.md`, as a new bullet of the Conventions section**, immediately
after the bullet whose first line begins
`- **THE WHOLE DECISION SURFACE IS DELIVERED AS USER-VISIBLE TEXT BEFORE ANY CHOICE QUESTION (user`
and before the bullet whose first line begins
`- **WORKING-TREE FILES ARE READ WITH THE FILE TOOLS; SHELL ACCESS IS LIMITED TO GIT OBJECT QUERIES BY`.
Both anchors are located by their own text and never by a line number (**D-307**); 0(d) item 4
established that each occurs exactly once.

**Separate it from the bullet above and the bullet below by exactly one blank line each**, matching
the spacing those two bullets already have between them. **Nothing existing is edited, reordered or
removed by this task — it is an insertion and nothing else.**

**★ THE BLOCK INTRODUCES NO NEW MARKDOWN HEADING, and that is a requirement rather than an
observation.** `tools/audit/gen_session_start_read_size.py` locates each of `CLAUDE.md`'s spans by
its HEADING and, by that artifact's own account, STOPs unless the heading is found exactly once; a
new `##` or `###` line inside Conventions would cut that span in two and change what the tool
measures. **The block is a bullet of the existing Conventions list and nothing else. If you find
yourself needing a heading, STOP and report it.**

**THE BLOCK, to be inserted VERBATIM:**

```
- **HOW A DECISION SURFACE IS WRITTEN, AND IN WHAT ORDER ITS RULES APPLY (consolidated here on the
  user's direction, 2026-09-21; each part keeps its own home and is CITED, never copied — #6).** The
  rules governing what is put to the user for a decision live in four register entries homed in four
  documents, and in a run of per-sitting rulings that carry no register entry at all. A session can
  hold every one of them and still apply them in the wrong order, and on 2026-09-21 one did: it
  established the fact that decides which rule governs, and then took the other branch. **This block
  exists for the ORDER.**
  **ONE WORD BEFORE THE LIST, so nothing is read the wrong way round.** The numbered STEPS below are
  this block's own. Where a step cites *clause N*, that means one of the FOUR CLAUSES the user gave
  on 2026-09-21, whose numbering is his — **and the two numberings do not line up**: his clause 1 is
  step 2 here, his clause 2 is step 3, his clause 3 is step 4, and his clause 4 is step 5. **The
  order is:**
  1. **APPLY THE STANDING PRINCIPLES FIRST (D-599).** Where the guiding principles and the ultimate
     objective decide the question, there is no genuine choice for the user, and what remains for him
     is ratifying the derivation rather than picking an option.
  2. **THEN ASK WHETHER ANY REAL CHOICE REMAINS** — valued towards the ultimate objective, towards
     the guiding principles, and by the meta level of the suggested act. **If none remains, say so
     and present NO decision surface** (the user's ruling of 2026-09-21, clause 1, generalising his
     ruling of 2026-08-28: *"There is no choice anymore, B or what?"*). **A bar this side wrote for
     itself is not a question for the user**: check whether the record already answers it before
     escalating it (2026-08-28).
  3. **WHERE A CHOICE REMAINS, A DECISION SURFACE IS OWED** (2026-09-21, clause 2), **and it presents
     ALL the alternatives** (clause 3).
  4. **EVERY ALTERNATIVE IS WEIGHED ON THREE STANDING GROUNDS** (clause 3, sharpening **D-424** and
     Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md`):
     **towards the ultimate objective** — maximum-precision inference, #4; **towards the guiding
     principles**; and **marked for the META LEVEL of the suggested act** — whether it acts on the
     analysis, on a measurement tool, or on this project's own governance apparatus. The three named
     are the floor and not the ceiling. Every alternative is **fact-based**: a checkable claim about
     our own system is checked before it carries load in a surface (#18), and one that cannot be
     checked is LABELLED a reading rather than stated as a fact. **Every pro and con names the
     principle, rule or gate it rests on (D-424).** Where the objective and the principles conflict,
     the objective takes precedence — **and how far that reaches is an OPEN QUESTION the user has not
     answered**: read at its widest it could be taken as licence to override #18, #19 or #20 by
     asserting a benefit to the objective, and §3 of that same record states that the narrowing is
     not a session's to take. Until he answers, it is applied as written, and any case where the wide
     reading would change an outcome is flagged to him.
  5. **THE SURFACE CARRIES A RECOMMENDATION, ALWAYS, EXPLAINED IN THOSE SAME THREE TERMS**
     (2026-09-21, clause 4). His words with the ruling: *"I cannot think of any example of decision
     surface that should exclude a recommendation."* **A recommendation given WITHOUT its
     three-ground explanation reopens the hazard the superseded rule existed against** — the user
     ruling on a verdict rather than on a reasoning he can check at its grounds.
  6. **THE WHOLE SURFACE IS DELIVERED AS TEXT THE USER HAS ACTUALLY SEEN, BEFORE ANY CHOICE
     QUESTION (D-249)**, self-contained, **every identifier re-explained from scratch** (2026-08-15).
     For a consequential decision the choice question goes in a **SEPARATE, LATER turn**, and **ONE
     DECISION PER TURN** (2026-08-21). **No multiple-choice widget** (2026-09-04). **A decision
     answered blind is voidable** (D-249).
  7. **IT IS WRITTEN IN PLAIN, UNCOMPRESSED ORDINARY ENGLISH**, reasoning on the page rather than
     summarising a reasoning that happened elsewhere, with no vocabulary invented for the occasion,
     and **no rating compressed into a stub** (Ruling 21 of the 2026-08-31 record). The record form
     belongs in the records and not in conversation with the user (2026-08-28). The two writing
     standards of `cowork_design_doc_template.md` bind it: that document states in its own words that
     they are NOT kind-scoped and bind every document and everything written for the user.
  8. **WHERE A QUESTION GENUINELY GOES BACK TO THE USER BECAUSE THE RECORD DOES NOT ANSWER IT, THE
     THREE SURVIVING REQUIREMENTS OF D-658 HOLD**: every claim cited at its source and read in place;
     the records concerned read whole; and anything the record does not settle **marked UNSETTLED
     rather than filled**. **D-658's fourth requirement — no recommendation at all — is SUPERSEDED by
     step 5 above, which is the user's clause 4, and is dead.** It is corrected at D-658's own home in
     `cowork_audit_protocol.md`, the former wording preserved there in place (#12).
  **WHAT THIS BLOCK IS, AND WHAT IT IS NOT.** It states the combined rule and its order. The verbatim
  of each part stays at its own home and is cited here, never copied (#6): **D-249** in this
  Conventions section; **D-424** in `cowork_notation_adoption_increment.md`; **D-599** in
  `cowork_adjudication_dossier.md`; **D-658** in `cowork_audit_protocol.md`. The per-sitting rulings
  of 2026-08-15, 2026-08-21, 2026-08-28, 2026-09-04 and 2026-09-21 live in their handoff entries and
  ruling records and are cited here by their dates. **NO DECISIONS-REGISTER IDENTITY IS ALLOCATED for
  the 2026-09-21 ruling or for this block** — that register cannot accept one while its rule (c) is
  suspended, and `cowork_register_rule_c_suspension_2026_08_28.md` is the route.
```

**Then report:** the two anchor lines with their line numbers before and after the insertion, the
number of lines added, and a confirmation that no existing line of `CLAUDE.md` was changed or
removed. **Do not run the read-size generators yet** — they run at Task 5, after `STATUS.md` and the
register are also final.

---

## 5. Task 3 — the D-658 correction at its home

**Run this task only if Task 1 did not STOP.**

**5(a) — replace the twelve lines that carry the rule, keeping the line count at twelve.** In
`cowork_audit_protocol.md`, the block that begins at the heading 0(d) item 1 located, and runs
through the line ending `RECOMMENDATION AT ALL.**`, is exactly twelve lines — count them and confirm
before replacing anything. **Replace those twelve lines with exactly these twelve lines:**

```
### Where the record does not settle the question, the surface that returns it to the user gathers FACTS, marks what is UNSETTLED, and CARRIES A RECOMMENDATION

**Ruled by the user, 2026-08-09** (`records/cowork/rulings/cowork_rulings_2026_08_09_fourth_stop.md`, Ruling 27), on the
user's own instruction, quoted in the ruling verbatim: *"follow the rule: fact based decisions or
exploration to gather facts are allowed, not decided on unsure/fabulated/misremembered facts."* The
third member of the family above, and the case those two do not cover: not *the plain form would
state something false*, but *the record does not answer the question at all*.

**THE FORM.** Where a question the session cannot settle has to go back to the user, the surface it
goes back on carries: **every claim CITED AT ITS SOURCE and read in place; the records concerned
READ WHOLE; anything the record does not settle marked UNSETTLED rather than filled — and A
RECOMMENDATION on the three standing grounds the decision-surface rule in `CLAUDE.md` names.**
```

**Only the first line and the last two lines differ from what is there now.** The five lines of the
"Ruled by the user" paragraph and both blank lines are **unchanged, character for character** — do
not retype them; leave them where they are. **Prove the replaced block is twelve lines and that the
line immediately after it is blank, and report both.**

**5(b) — the preserved former wording and the supersession record**, inserted **after** the twelve
lines and the blank line that follows them, and **before** the paragraph that currently begins
`**The last clause is the load-bearing one`:

```
*★ THE FOURTH REQUIREMENT WAS REVERSED ON THE USER'S RULING OF 2026-09-21, AND THE FORMER WORDING IS
PRESERVED HERE IN PLACE (#12).* The heading above formerly ended *"gathers FACTS and makes NO
recommendation"*, and THE FORM's fourth requirement formerly read *"— and NO RECOMMENDATION AT
ALL."* **The user struck that wording himself, on 2026-09-21, in these words:** *"'makes NO
recommendation' is directly false."* The ruling that reversed it is
`records/cowork/rulings/cowork_rulings_2026_09_21_decision_surface_form_sitting.md`, Ruling 1,
clause 4: a decision surface always carries a recommendation, explained towards the ultimate
objective, towards the guiding principles and by the meta level of the suggested act. His words with
that ruling: *"I cannot think of any example of decision surface that should exclude a
recommendation."* *(Why no residue of the old clause survives is the writing side's reading and not
his: under clause 2 a question that goes back to the user because the record does not answer it is a
decision, so a surface is owed and clause 4 reaches it; under clause 1, where no choice remains, no
surface is presented at all. **His own ground is the sentence quoted above and needs no derivation
from this side.**)* **No decisions-register identity is allocated for that ruling** — the register
cannot accept one while its rule (c) is suspended, and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route.

**THE OTHER THREE REQUIREMENTS ARE UNTOUCHED AND STILL BIND**: every claim cited at its source and
read in place, the records concerned read whole, and anything the record does not settle marked
UNSETTLED rather than filled. **That is why this entry stays LIVE rather than becoming superseded** —
one clause of four was replaced, and the entry as corrected states a live rule. *(That reading is the
Cowork writing side's, taken because the register's status vocabulary has no partial-supersession
word and because a SUPERSEDED BY status must name its replacement by an identity the suspended
register cannot issue. It is stated here so the user can correct it in one word.)*
```

**5(c) — the load-bearing paragraph, corrected with its former wording preserved.** Replace the
paragraph that begins `**The last clause is the load-bearing one` — the whole of it, through the
sentence ending `the never-work-from-memory rule forbids.` — with:

```
**The load-bearing requirement is now the UNSETTLED marking, and it is the one a session will be
tempted to break.** Marking an item UNSETTLED is an ANSWER and not a shortfall — *the record does not
address this* is what a reader needs in order to rule, and filling it from the most plausible reading
is the invention the never-work-from-memory rule forbids. **What the superseded clause protected is
now held by the recommendation's own form**: a recommendation explained on the three standing grounds
lets the user rule on a reasoning he can check at each ground, rather than on a verdict. A
recommendation given WITHOUT that explanation reopens the hazard in full, which is why the second
half of the user's clause 4 — *explained in terms of* those three grounds — is not decoration.

*★ FORMER WORDING, PRESERVED (#12), superseded 2026-09-21:* "**The last clause is the load-bearing
one, and it is the one a session will be tempted to break.** A fact-gathering pass that ends in a
recommendation has decided the question it was sent to inform: the user then rules on the session's
reading rather than on the facts, which is the outcome the instruction above exists against. Marking
an item UNSETTLED is likewise an ANSWER and not a shortfall — *the record does not address this* is
what a reader needs in order to rule, and filling it from the most plausible reading is the invention
the never-work-from-memory rule forbids."
```

**5(d) — the closing paragraph, corrected with its former wording preserved.** Replace the paragraph
that begins `*Why the form earns its place:*` — the whole of it, through the sentence ending
`than by the user on facts.` — with:

```
*Why the form earns its place:* applied at the case that produced it, gathering the facts settled
more than the question asked — and it LOCATED a conflict between two records that nobody had put
side by side, with two readings visible. **What the form protects is that the user rules on a
reasoning he can check at its grounds rather than on a bare verdict**, and since 2026-09-21 the
recommendation's three-ground explanation is what carries that load.

*★ FORMER WORDING, PRESERVED (#12), superseded 2026-09-21:* "*Why the form earns its place:* applied
at the case that produced it, gathering the facts settled more than the question asked — and it
LOCATED a conflict between two records that nobody had put side by side, with two readings visible
and neither chosen. A pass permitted to recommend would have chosen one, and the conflict would have
been resolved by a session's reading of intent rather than by the user on facts."
```

**5(e) — what this task does NOT touch.** The note that stands above the heading with one blank line
between them, `*★ STANDING CLAUSE — a dispatch's read-first block requires the clause below to be
met.*`, is **unchanged and stays exactly where it is**. No other section of
`cowork_audit_protocol.md` is edited. **No line above the heading is added or removed**, so the
heading keeps its own line number and D-658's `home` anchor keeps its start line and its width —
Task 4 proves that rather than assuming it.

**5(f) — one search, reported and not acted on.** The standing-clause note says a dispatch's
read-first block requires D-658's clause to be met, so the superseded wording may have been copied
into dispatch templates. **Search `records/cc/instructions/` for the strings `NO RECOMMENDATION` and
`makes NO recommendation` and report every hit with its file and line.** **Change nothing** — a
dispatch already run is a dated record and is never rewritten. This is a finding for the user.

---

## 6. Task 4 — the register, corrected at its source and regenerated

**Run this task only if Task 1 did not STOP.**

**6(a) — the backbone, edited by hand at ONE entry.**

**★ FIRST, CAPTURE THE FORMER VALUES FROM THE FILE ITSELF.** Before changing anything, read that
object's current `"title"`, `"verbatim"`, `"plain"` and `"rationale"` out of
`tools/audit/decisions/backbone_decisions.json` and hold them. **The preserved-former-wording text
below is built from WHAT YOU READ, never retyped from this dispatch** — a transcription of a field
into an instruction is exactly the defect D-431 exists against, and the writing side's own copy of
those strings is not the object. **Where the text below shows a former value, use the string you
read instead, and report any difference between the two.**

In the object whose `"id"` is `"D-658"` and in no other object:

- **`"title"`** becomes:
  `Where the record does not settle the question, the surface that returns it to the user gathers facts, marks what is unsettled, and carries a recommendation`
- **`"verbatim"`** becomes **exactly the twelve lines 5(a) wrote into the file, joined by `\n`**.
  **Prove it rather than retyping it**: read the twelve lines back out of `cowork_audit_protocol.md`
  and build the string from what you read. **Then prove the equality both ways** — that the stored
  `"verbatim"`, split on `\n`, equals those twelve lines, and that those twelve lines are the ones at
  the entry's `"home"` anchor. **Report the proof.**
- **`"plain"`** becomes:
  `When a question has to go back to the user because the record does not answer it, the surface it goes back on cites every claim at the place it can be checked, reads the records concerned whole, marks anything the record does not settle as unsettled instead of filling it in, and carries a recommendation explained towards the ultimate objective, towards the guiding principles and by the meta level of the act it suggests.`
- **`"rationale"`** becomes:
  `The load-bearing requirement is the unsettled marking: marking an item unsettled is an answer rather than a shortfall, since filling it from the most plausible reading is the invention D-112 forbids. The fourth requirement was a prohibition on recommending, and the user reversed it on 2026-09-21 — a decision surface always carries a recommendation, explained towards the ultimate objective, towards the guiding principles and by the meta level of the act it suggests. What the prohibition protected is held by that explanation instead: the user rules on a reasoning he can check at each ground rather than on a bare verdict, and a recommendation given without the explanation reopens the hazard in full.`
- **`"status"`** stays **`live`**, and `"date"`, `"ratified_by"` and `"group"` are unchanged.
- **`"home"`** is **NOT edited by hand** and is left exactly as it stands. 6(c) re-aims it if it has
  drifted; 6(d) proves where it ended up.
- **`"status_source"`** keeps every word it now carries and gains, appended to its end, exactly:
  ` ★ AMENDED 2026-09-21 ON THE USER'S RULING: the fourth requirement of THE FORM — no recommendation at all — is SUPERSEDED by clause 4 of Ruling 1 of records/cowork/rulings/cowork_rulings_2026_09_21_decision_surface_form_sitting.md, which requires a recommendation of every decision surface, explained towards the ultimate objective, towards the guiding principles and by the meta level of the act it suggests. The user named the former wording false in those terms. The other three requirements are untouched and the entry stays LIVE, one clause of four having been replaced; the register's status vocabulary carries no partial-supersession word, and a SUPERSEDED BY status would have to name a replacement identity the register cannot issue while its rule (c) is suspended (cowork_register_rule_c_suspension_2026_08_28.md). FORMER WORDING PRESERVED VERBATIM (#12) — title: "Where the record does not settle the question, the surface that returns it to the user gathers facts and makes no recommendation"; the fourth requirement of THE FORM: "— and NO RECOMMENDATION AT ALL."; the former rationale: "The no-recommendation clause is the load-bearing one and the one a session will be tempted to break: a fact-gathering pass that ends in a recommendation has decided the question it was sent to inform, so the user then rules on the session's reading rather than on the facts — which is exactly what the user's quoted instruction exists against. Marking an item unsettled is likewise an answer rather than a shortfall, since filling it from the most plausible reading is the invention D-112 forbids. Evidenced at the case that produced it: gathering the facts LOCATED a conflict between two records that nobody had put side by side, wrote both readings onto the surface, and chose neither — a pass permitted to recommend would have chosen one, and the conflict would have been settled by a session's reading of intent."`

**★ THE SERIALIZATION IS A HARD CONSTRAINT, and it is stated because a tool refuses on it.**
`tools/audit/decisions/reaim_home_anchors.py` reads the backbone, re-serializes it with
`json.dumps(..., indent=2, ensure_ascii=False) + "\n"`, and **REFUSES with exit code 2 if that
round-trip is not byte-identical to the committed file** — its own message is *"REFUSED:
re-serializing the untouched backbone is not byte-identical to the committed file, so writing would
reformat it."* **So the edit must leave the file in exactly that form.** Make the edit by loading the
JSON, changing the five fields of that one object, and writing it back with
`json.dumps(data, indent=2, ensure_ascii=False) + "\n"` and `newline=""`.

**★ DO IT WITH A ONE-OFF COMMAND OR A SCRIPT HELD OUTSIDE THE REPOSITORY WORKING TREE. NO NEW FILE
IS ADDED UNDER `tools/`**, and no new tool is created by this batch — the footprint assumption says
this batch creates exactly one new file, your report, and a helper committed into the tree would
falsify it. If the helper must live on disk, put it outside the working tree and name its path in
your report.

**Then prove it**: run
`reaim_home_anchors.py --check` and confirm it does not print `REFUSED`. **If it refuses, STOP** —
the file has been reformatted and the change must be redone.

**6(b) — prove nothing else in the backbone moved.** Report the number of objects in `"decisions"`
before and after the edit, and confirm that the only object whose serialized text differs is
`"D-658"`. **Any second object differing is a STOP.**

**6(c) — re-aim the drifted anchors.** Both `CLAUDE.md` (Task 2) and `cowork_audit_protocol.md`
(Task 3) gained lines, so entries homed below those insertions have drifted.

```
python tools/audit/decisions/reaim_home_anchors.py --check
python tools/audit/decisions/reaim_home_anchors.py
python tools/audit/decisions/reaim_home_anchors.py --check
```

Report all three outputs and exit codes verbatim, and **name every entry it moved with its old and
new anchor**. The third run must report zero drift.

**★ HOW THAT TOOL BEHAVES, READ AT ITS SOURCE, SO ITS SILENCE IS NOT MISREAD.** It prints **only the
entries whose anchor MOVED**, one line each, then a count. **It prints NOTHING for an entry it
passes over** — neither for an entry already at the right line, nor for one whose verbatim it cannot
find in the home file, which its own docstring calls *"a different event"* that is *"left for a
reader"*. **So a skip is INVISIBLE in this tool's output, and you must not go looking for a skip list
it does not emit.**

**What that means for D-658.** Its anchor is designed not to move — 5(e) added no line above the
heading — so **D-658 is EXPECTED to be absent from this tool's output, and its absence here proves
nothing either way.** Where its state actually shows is `gen_cluster_dispositions.py --verify` at
6(d): if 6(a)'s equality proof was wrong, the verify reports D-658's quote as missing or mismatched,
and **that** is the STOP.

**6(d) — regenerate and verify.**

```
python tools/audit/decisions/gen_decisions_register.py
python tools/audit/decisions/gen_decisions_register.py --check
python tools/audit/decisions/gen_cluster_dispositions.py --verify
```

Report all three outputs and exit codes verbatim.

**★ THE CONDITION IS A COMPARISON AGAINST TASK 1's BASELINE, NOT AN ABSOLUTE.** Task 1 recorded what
these two reported at the untouched tree. **The bar here is: no entry that was CLEAN at Task 1 may be
unclean now, and no residual line drift may remain** — the re-aim at 6(c) exists to leave zero. **An
entry that was already unclean at Task 1 stays carried and reported; it is not repaired here and it
does not stop this batch.** An entry that was clean at Task 1 and is not clean now is a **STOP**:
this batch caused it. **Report which entry, what changed, and stop there; do not repair it by hand.**

**Then report, quoted from the regenerated files:** D-658's row in `DECISIONS.md`, and D-658's whole
entry in `decisions/group_T.md`. **Confirm that neither still carries the words `no recommendation`
outside a preserved-former-wording passage.** Report the list of `decisions/group_*.md` files the
regeneration actually rewrote.

---

## 7. Task 5 — `STATUS.md`, the forward bound, the two read-size generators, the closing capture

**In this order and no other.**

**7(a) — the `STATUS.md` entry.** Write ONE new dated entry, at the head of the dated entries, in the
OI-222 pointer convention this file already uses: a POINTER whose whole is your report, restating
**no figure** (D-431). It says what this batch did — the previous batch's work committed; the
decision-surface rules consolidated into one section of `CLAUDE.md` Conventions with every part left
at its own home and cited; D-658 corrected at its home and in the register's source, its former
wording preserved, its status left LIVE; the register regenerated and re-verified — and what it did
not do: no pack authored or rendered, no open-items row, no `D-NNN` allocated, the register's rule
(c) still suspended and its owed-entries list still as 0(d) item 5 found it. **No existing sentence
of `STATUS.md` is rewritten or removed.** This is the last write to `STATUS.md` in this batch.

**7(b) — the forward bound.** Re-aim `tools/audit/gen_status_batch_bound.py` so that the batch it
identifies is the PREVIOUS one — the batch whose entry 0(e) committed — and run its `--apply`, so
that batch's entries move to `STATUS_ARCHIVE.md` in the same act that writes this batch's own.
*(**The writing side did not open that tool**, so the SHAPE the aiming takes — a base commit, a
dispatch name, or something else — is not stated here. Set the aiming the tool's own form requires,
and report exactly what you set.)* Then run its `--check` and report the output. **If `--apply`
reports its already-in-the-archive STOP, report it whole and make no further change.**

**Do NOT read a green `--check` as proof the bound is met.** `OPEN_ITEMS.md` OI-379 is open on
exactly that: that tool is re-aimed by hand at every close and its `--check` reconciles only the
aiming currently authored. **Report the aiming you set and the entries the `--apply` actually moved,
by name.** *(OI-379 is named here as `STATUS.md`'s own pointer paragraph states it; the row itself
was not opened by the writing side.)* **The two 2026-09-02 entries do NOT move and are not to be
moved by hand** — `STATUS.md`'s own pointer records that they name no dispatch, so no aiming can
identify them, and whether they ever move is a question standing with the user.

**7(c) — the two read-size generators, after 7(a) and 7(b) and not before:**

```
python tools/audit/gen_session_start_read_size.py
python tools/audit/gen_defense_share.py
python tools/audit/gen_session_start_read_size.py --check
python tools/audit/gen_defense_share.py --check
```

Report all four outputs and all four exit codes verbatim. **Both `--check` runs are expected to exit
0.** A `STOP:` line or a traceback from either is a STOP; **do not edit either tool** (B1).

**★ AND REPORT THE FIGURES THE USER ASKED FOR, NAMED HERE RATHER THAN COUNTED, EACH CITED TO ITS
ARTIFACT AND TRANSCRIBED FROM NOWHERE (D-431):** what an ordinary session now reads in total, and
what `CLAUDE.md`'s six session-start spans now hold, both read out of
`tools/audit/session_start_read_size.json` after the run; and the marked-defense share after the
run, read out of `tools/audit/defense_share.json`.
**★ THE INSERTED BLOCK SHOULD MATCH NO MARKER, AND THAT WAS CHECKED RATHER THAN HOPED.**
`gen_defense_share.py`'s clause ends are AUTHORED per marker, published at
`cowork_defense_clause_ends_2026_09_08.md`, so a newly matched marker would need an authored end this
batch has not made. **Its marker table has three rows**, read at `tools/audit/defense_share.json`'s
own `the_marker_table` by the Cowork side: an italic or bold run whose content opens with
`Why[ :,]`, with `Evidence:`, or with `Founding instance[:,]`. **The block Task 2 inserts contains no
emphasised run opening with any of those three**, which the writing side checked against the block's
own text. **So this generator is expected to run clean.**

**If it nonetheless matches something new, or stops for want of an authored end:** report it whole,
**do not author an end and do not edit that pass's published ends**, and **STOP before the commit** —
naming every path this batch has modified so far, so the next session can resume from a known state.

**7(d) — the CLOSING GUARD CAPTURE**, taken after 7(c). Compare it against 0(g) **verdict by
verdict**.

> **THE CONDITION: no guard whose VERDICT was PASS at the opening capture may carry any other verdict
> at this capture.** A guard that moves FAIL → PASS is ALLOWED and REPORTED. **No condition is
> written on any guard's printed output, on any count inside that text, or on the number of failing
> guards.**

**`tools/audit/gen_guard_classification.py` is EXPECTED to STOP**, for the reason established at
handoff entry 225 §2 and restated at the head of this dispatch. **Run it in its own stated order,
report it whole, and CARRY ON. It is not a STOP for this batch and it is not repaired here.**

---

## 8. The commit, and the push

**8(a) — COMMIT THREE, by explicit path, never a directory pathspec.** The candidate set is exactly:

1. `CLAUDE.md`
2. `cowork_audit_protocol.md`
3. `tools/audit/decisions/backbone_decisions.json`
4. `DECISIONS.md`
5. every `decisions/group_*.md` the regeneration actually rewrote — **name each in your report rather
   than assuming which moved**
6. `tools/audit/gen_status_batch_bound.py`
7. `tools/audit/status_batch_bound.json`
8. `tools/audit/session_start_read_size.json`
9. `tools/audit/defense_share.json`
10. `STATUS.md`
11. `STATUS_ARCHIVE.md`
12. `records/cc/instructions/cc_instruction_decision_rules_consolidation_2026_09_21.md`
13. `records/cc/reports/cc_report_decision_rules_consolidation_2026_09_21.md`
14. `tools/audit/changed_paths_establishment.json` and the guard set's other artifacts, **only those
    the enumeration actually reports as modified** — name each one in your report. **These belong
    here and not in commit one or two, because 0(g) and 7(d) are what moved them.**

**Prove the staged set is EXACTLY the candidate set and nothing else before committing.**

**HELD BACK, AND NAMED SO NOTHING SWEEPS THEM IN:** `tools/audit/claude_md_finer_archive.json`; and
the standing untracked population — the `scratch_artifacts/` tree, the two PDFs, `Claude outputs/`,
`Codex research inventory/`, `docs/research_papers/polyph9-release/` and the untracked `.mscx` under
`tools/audit/derivation_exemplars/l0-l1/`. *(That list is RELAYED from the previous dispatch's §6,
which the Cowork side read whole, and which attributes it to handoff entry 223 §0 — a record the
Cowork side did NOT open. Entry 225 §0 carries the population forward by pointer and does not
enumerate it. **0(c)'s enumeration is what establishes the actual untracked set; this list is a
guide to it, not a statement of it.**)*
**Held back also: every other path the enumeration reports that no commit in this batch names.**
**Confirm in your report that each named path is absent from every staged set.**

**8(b) — push.** After all three commits, push every branch that received them. `origin` is the fork;
`upstream`'s push is disabled and is not to be used. **The refs disagreed when this batch opened, so
this push is also what closes that gap — read `.git/refs/remotes/origin/master` with the file tools
after the push and confirm it equals `master`.** *(If that loose ref file is not there, git may have
written the value into `.git/packed-refs` instead. **Report that you did not find the loose file and
say where you read the value from; it is not a failure.**)* **If the push itself fails for any
reason, REPORT IT; do not skip it silently and never pass `--force`.** Name the pushed branches.

---

## 9. The report

`records/cc/reports/cc_report_decision_rules_consolidation_2026_09_21.md`, carrying:

1. Task 0's pin; both refs as found; the enumeration of 0(c) and the corruption check's result; the
   five start-state proofs of 0(d) with what you found at each; both Task 0 commits with their staged
   sets proved and their hashes; and **then** the opening capture with its path and every guard's
   verdict, together with the artifacts that capture itself moved.
2. **TASK 1's FIVE RESULTS, VERBATIM, RECORDED AS THE BASELINE** the later checks are compared
   against — the register's regenerability at the untouched tree, the pre-existing anchor drift, the
   pre-existing quote state entry by entry, and the two discard checks. **This is the answer to a
   question the Cowork side could not establish, and it is reported whether or not it changed
   anything.**
3. Task 2's insertion: both anchor lines with line numbers before and after, lines added, and the
   confirmation that nothing existing changed.
4. Task 3, edit by edit, each with the proof it carries: 5(a)'s replacement proved to be twelve lines
   with a blank line after it; 5(b)'s inserted block; 5(c)'s replaced paragraph with its preserved
   former wording beneath it; 5(d)'s the same; the confirmation that 5(e)'s standing-clause note and
   every other section of the file are untouched; and **5(f)'s search results in full, as a
   finding**.
5. Task 4: the former field values as you read them out of the backbone, and any difference between
   them and what this dispatch shows; the five changed fields quoted whole; the equality proof both
   ways; the object-count proof; the three re-aim runs with every entry moved; the regeneration and
   both verifications **compared against Task 1's baseline**; D-658's regenerated row and entry
   quoted; and the list of rewritten group files.
6. Task 5's four parts: the `STATUS.md` entry quoted whole; the forward bound's aiming, `--apply` and
   `--check`; the four generator outputs and exit codes together with the figures 7(c) names, each
   cited to its artifact; and the verdict-by-verdict comparison of the two captures, naming
   every guard that moved and in which direction, with the guard classification's result reported
   whatever it is.
7. The third commit's hash, the pushed branches, and `origin/master` after the push.
8. **What you did NOT do**, named rather than counted — and in particular: that
   `tools/audit/gen_derivation_boot_pack.py` was not edited and never run bare; that nothing was
   authored into `WITHHELD`, `EXTRAS`, `VERDICTS`, `CRITERION` or `FROZEN`; that no pack directory
   was read for content, written or moved; that no governing document but the three named was
   amended; that no rendered register file was hand-edited; that no open-items row and no `D-NNN` was
   touched; and that the register's rule (c) suspension and its owed-entries list were left exactly
   as 0(d) item 5 found them.

**WHAT GOES TO THE USER AND IS THE POINT OF THE REPORT, named rather than counted:** Task 1's answer on whether the
register regenerates; 5(f)'s search for the superseded wording elsewhere; and the statement that
D-658 was left **LIVE** rather than superseded, which is the writing side's reading and is his to
correct.

**If any expected result does not appear, stop at that task and report it. Do not continue to the
next one, and do not resolve a bar that contradicts a task.**
