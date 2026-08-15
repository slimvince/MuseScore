# CC dispatch — phase 1s: the falsified rules, D-341's home, and the enumeration tool

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's rulings of the same
> date (ninth set).** Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1s_stale_rules_and_enumeration.md`.
>
> **★ THIS DISPATCH ASSERTS NO FIGURES** (D-431). Quantities are named as an artifact and a field.
>
> **★ TASK 1 IS FIRST FOR A REASON.** The previous dispatch ordered a verification its own rules left
> no sanctioned way to perform, and CC broke the file-tools rule twice complying with it. Task 1
> builds the mechanism that closes that gap, and **every later task in this wave uses it** — including
> this wave's own commit verification. Do not repeat the previous wave's workaround.
>
> **★ `cc_instruction_phase1o_gate_partition_and_probe_rerun.md` is still queued BEHIND this wave.**
>
> **★ THIS WAVE READS NO OI-207 DOCUMENTS.**

## 0. Standing constraints

1. **Every amendment lands in the PROPER LAYER** (#7).
2. **NO inference-problem fixing.** Phase 1 under D-231. No `src/` change, no golden refresh, no
   `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change, no fix, no design.
3. **Never use the shell to read working-tree files.** After Task 1, enumerating *which* files changed
   has a sanctioned tool; reading *what a file says* still goes through the file tools, always.
4. **Never work from memory.** For a claim about the code, the code is primary; a row or a register
   entry is secondary (D-431's premise clause). **This wave exists because that clause was breached
   by both sides** — do not add to it.
5. **A surprise is a STOP** (#13).
6. Bare words carry the musical meaning. Bash: append `; echo "exit:$?"`; no large single outputs.

## 1. The rulings this dispatch carries

| # | Subject | Ruling |
|---|---|---|
| Y1 | The file-tools rule vs. verifying a commit | **Build the enumeration tool** (option 3C), with the scope clarification as its recorded reason |
| Y2 | OI-294, the falsified rules | **Correct (j) and D-435's rationale; convert (i)'s defense from line numbers to a description** (option 1B) |
| Y3 | OI-295, D-341 homeless | **Fix it at the document — move the rule into the section it amends** (option 2B) |
| Y4 | The process check's one control false positive | **Accept CC's judgment; record the over-breadth** (option 4A) |

## 2. Task 1 — The changed-path enumeration tool (Y1)

### 2.1 Why the rule is not being narrowed

The file-tools rule's recorded rationale is specific: a stale mount made the shell return wrong
**content** while the file tools read the live disk correctly, and the git-object exception survives
because content-addressed reads are self-verifying. **Both halves are about content.** A list of
which paths changed is not content.

So the rule's letter stands untouched, and the sanctioned path becomes a committed tool rather than a
permitted shell command. Record that reasoning where the tool lives — it is the tool's justification,
and without it the tool looks like a wrapper around a forbidden command.

### 2.2 What to build

A committed script that reports **the changed-path list and nothing else**. It must be
**structurally incapable of returning file content** — that property is the whole justification, so
state it in the docstring and make it true of the code, not just of the intent.

Establish it (#19): verify it reports a known set of modifications correctly, and verify it reports
nothing when the tree is clean.

### 2.3 Close the two measured guard limits, now that they are coherent

`open_items/OI-292.md` records both, measured live in the previous wave:

- **`git status` is not denied by the shell-read guard.** With the enumeration tool in place this is
  now coherent to close: the tool is the sanctioned path, so the raw command should be denied. Add it,
  and **exempt the new tool by name** so the guard does not deny the thing it makes possible.
- **A false deny fired on `grep -c "^  D-" …`** because the guard splits on whitespace — a shape its
  established false-deny rate does not cover. Fix it and **re-establish**, reporting the new
  false-deny figure from the artifact. If the fix raises false denies elsewhere, **revert and
  report**: a guard that blocks correct commands gets disarmed, which is worse than one with a
  known gap.

### 2.4 Use it for this wave

This wave's own commit verification goes through the new tool. Report what it found.

## 3. Task 2 — OI-294: the three falsified statements (Y2)

All three sit inside user-ruled text. **The user has ruled the correction**, 2026-08-03; cite that
ruling in each edit so the authority is on the surface and not assumed.

- **Rule (j)** (`CLAUDE.md`, D-435) — strike the stale clause asserting that no user-ratified surface
  delegates to `cowork_engage_arc_plan.md`. One now does, in the same file. Replace it with a
  statement that says what (j) is *for* — that the two roles are different tests — without a
  present-tense claim about any particular document's current state.
- **D-435's rationale** in the register — re-take it; the ground it states ("the only naming of it is
  inside a list of citations") is no longer a description of the file. Former rationale preserved in
  provenance (#12).
- **Rule (i)** (`CLAUDE.md`, D-432) — **convert its defense from line numbers to a description.**
  The evidence is that the canonical document distinguishes the two acts in adjacent lines: a bare
  *"Full spec:"* citation, and immediately beneath it a delegation clause naming its target and its
  sections. Say that without quoting line numbers. **The reason for the conversion, and it belongs in
  the text:** a line number quoted inside a rule's prose is not a register anchor, so the anchor
  machinery cannot maintain it and it will go stale on the next insertion — as it just did.

Re-take **D-432**'s verbatim from the corrected text; preserve the former (#12). Flip **OI-294**.

## 4. Task 3 — OI-295: move D-341 into the section it amends (Y3)

**D-341** is homed at `cowork_layer5_function_design.md` §15, "Open items & deferred refinements" — a
tracking list, which the rule-stating half correctly judges as recording findings. Its own verbatim
says what it amends: *"the §5.0 enumeration is amended."*

**Move the rule text into §5.0**, where the layer's specification states its rules. That is #7 in its
plainest form, and it is OI-290's remedy shape — fix the document, not the classification.

- The rule text moves **unchanged** (#12).
- **Leave a dated note at §15** recording that the item moved and where. The tracking history is
  preserved; the rule is not duplicated (#6).
- Re-take D-341's verbatim and anchor from the new home; preserve the former in provenance.
- Re-run the classification and confirm D-341 moves `gap` → `contract-home`. **If it does not, STOP
  and report** — that would mean §5.0 fails the rule-stating half, which would be a surprise.

**Row the sibling sweep.** D-341 is unlikely to be the only ratified rule parked in an open-items or
status section. Open a row for a sweep across the documents whose entries the classification reaches,
looking for rules homed in tracking sections. **Do not run the sweep here** — row it.

`cowork_layer5_function_design.md` is a SIGNED specification; the edit is licensed by the user's
ruling of 2026-08-03 and by nothing else. Say so in the commit.

## 5. Task 4 — Record the process check's over-breadth (Y4)

The user accepts CC's judgment: the word rule is **kept**, both rates published, and the one control
false positive stands. CC's ground is adopted as the reason — the digit path flags the same phrase
identically, so reverting would make the check disagree with itself about spelling rather than remove
a false positive.

**Record the over-breadth as a known property, not a defect to tune around:** a structural description
such as "in two files" is a quantity by D-431's letter and the check flags it correctly. Note it where
the check's establishment lives, so a later session does not "fix" it by adding a noun allowlist —
which would be tuning to a specimen, the thing the establishment artifact already warns against.

No code change.

## 6. Task 5 — Guards, notes, close

Run every guard at the committed tree and read each output separately. **Derive the guard list from
what exists**, not from this dispatch: the previous dispatch named `gen_section_homes.py`, which
commit `a7c627e5a3` had already deleted as superseded by `gen_home_classification.py`, and the dead
path went unremarked. **If a guard this dispatch names does not exist, report that rather than
silently substituting.**

Run `tools/audit/process_check.py` over **this dispatch** and report what it finds against Cowork.

**One commit where the same-commit rule allows it (D-230).** Tasks 2 and 3 both edit `CLAUDE.md` or a
cited specification, so anchors will drift; **re-aim per citation from the drift report's own line
numbers**, never by an assumed shift. Commits by git plumbing; guards run explicitly at the committed
tree.

`STATUS.md` gains one POINTER entry.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's own remedy, OI-274's body-tense
half, OI-287, OI-288, OI-289, OI-290's document-side remedy, the sibling sweep this wave rows, the
owed reads, and the queued phase-1o dispatch.

## 7. Accepted outcomes

Tasks 1–5 are bounded and expected complete. **Task 2.3's fix reverting is an acceptable outcome** if
it raises false denies. **Task 3's D-341 failing to move is a STOP**, not something to work around.
**Task 1 finding that a content-incapable enumeration cannot be built as specified is a STOP** — say
so rather than shipping a wrapper that can return content.

## 8. Self-check (D-434) — run by Cowork on this dispatch before release

- **Principles.** #12 — every moved text unchanged, every former verbatim preserved. #13 — three STOP
  conditions named. #19 — both the new tool and the guard fix carry an establishment step. #7 — D-341
  moves to the section that owns its concern. #6 — the rule is not duplicated at §15, a pointer is
  left instead.
- **Conventions.** No self-invented labels. Bare words carry the musical meaning.
- **Figures and premises (D-431).** No bare quantity. The premise that `gen_section_homes.py` was
  deleted is cited to commit `a7c627e5a3`, read at the object this session — not carried from a report.
- **File-tools rule.** §0.3 now distinguishes enumeration from content, and Task 1 builds the
  mechanism **before** any task needs it — the fault in the previous dispatch, which ordered a
  verification it left no way to perform, is fixed rather than repeated.
- **Uncertainty (#24).** No comparison between measured quantities is asserted.
- **Consistency between rulings.** Checked: Y1's tool is what makes Y2 and Y3's commit verification
  performable; Y2 and Y3 both drift anchors and are ordered into one re-aim; Y4 changes nothing that
  Y1–Y3 depend on.
