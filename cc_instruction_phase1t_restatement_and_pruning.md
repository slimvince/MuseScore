# CC dispatch — phase 1t (STAGE 1): the restatement rule, the STATUS sweep, and the handoff split

> **Status: ACTIVE DISPATCH. RE-ISSUED 2026-08-03 (Cowork) at STAGE-1 scope**, under the user's
> sequencing ruling of the same date: *facts before action; our own effort is not a consideration.*
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1t_restatement_and_pruning.md`.
>
> **★ WHAT CHANGED FROM THE EARLIER ISSUE, AND WHY.** The `CLAUDE.md` mechanism triage is **removed**
> from this wave. Its measurement half is fact-gathering and belongs in stage 2; its moving half is
> action and belongs after the gathering. And the earlier issue's §0.1 hard constraint rested on a
> **premise now known false** — see F3 below.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).**
>
> **★ THIS WAVE READS NO OI-207 DOCUMENTS.** No `src/`, no goldens, no `tools/corpus/`, no
> `tools/robust_stop/`, no behaviour change, no fix, no design. Phase 1 under D-231.

## 0. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork in the session that wrote this dispatch:**

- **F1.** D-431's home is `cowork_audit_protocol.md` — `decisions/group_T.md:499`.
- **F2.** `cowork_handoff.md` carries **ten** session-close blocks, and `cowork_handoff_archive.md`
  exists at the repository root.
- **F3. ★ The earlier issue's hard constraint was wrong.** `tools/open_items_split_check.py` reads the
  index for **IDs only** (`:104-112`) and compares byte-verbatim against the **detail** row
  (`:184-186`). **Index rows are not in the protected set.** The earlier issue stated the opposite and
  scoped this wave partly on it. The scope below is unchanged, but its **reason** is different and is
  stated correctly at §2.2. OI-299 carries the corrected reason.

**ASSUMPTION — each with an ordered check before the act it licenses:**

- **A1.** That `cowork_handoff_archive.md` is declared reference-only and outside the session-start
  read. Cowork has this from a handoff block, which is the surface this wave exists to distrust.
  → **Task 2.1**.
- **A2.** That the handoff's entry-point block is self-sufficient at HEAD. → **Task 2.2**, and it
  carries a STOP.

## 1. Task 1 — Generalize D-431, and sweep STATUS

### 1.1 The rule

D-431 binds *"a dispatch or a session report."* Every measured carried-quantity failure in this arc —
on both sides — came from surfaces it does **not** reach: STATUS entries, handoff blocks and
open-items rows.

**Widen it at its existing home (F1)**, re-taking the verbatim from the corrected text and preserving
the former (#12). **Do not create a second entry** — one concern, one rule (#6). Add to its defense
that the failures it now covers were on tracking surfaces, cited to the rows and artifacts that hold
them, not transcribed.

### 1.2 The sweep, and its scope — with the corrected reason

Sweep **`STATUS.md`'s current entries** and **`cowork_handoff.md`'s entry-point block**. Replace each
restated quantity with a citation to the artifact and field that publishes it. `STATUS.md` entries
become **pointers**, which the OI-222 remedy already requires.

**Historical open-items rows stay out of scope — and NOT because a guard protects them (F3).** They
are out of scope because they are **the record**: a row states what was found when it was found, and
rewriting it to tidy a figure edits history rather than correcting it (#12). Say so in the commit, so
the corrected reason replaces the wrong one in the record.

Where a `STATUS.md` entry predates the current arc, move it to `STATUS_ARCHIVE.md` under the existing
split.

## 2. Task 2 — The handoff split

### 2.1 Check A1

Establish, at `STATUS.md` and `CLAUDE.md` themselves, whether the archive is declared reference-only
and outside the session-start read. **Report what you find.** If it is not so declared, the split
still proceeds but the declaration is owed and must be made in the same commit — moving content into
an undeclared state is the failure this check exists to prevent.

### 2.2 Check A2 — and this one STOPS

Read the entry-point block **in full** and establish whether it is self-sufficient at HEAD. It is
written to be — *"you start clueless, this block is the entire handover"* — but that is a design
intention, not a measurement. **If it depends on a block you are about to move, STOP and report**:
the split would then remove something the mandated read still needs.

### 2.3 The split

Move the superseded blocks to `cowork_handoff_archive.md`, keeping **the entry point and its
immediate predecessor** and nothing else. Every moved block goes across **unchanged** (#12). Nothing
is deleted.

**The reason, for the commit message:** the handoff is a restatement surface that has supplied stale
quantities into a mandated read, measurably, more than once. Splitting it removes a source of false
facts from circulation. It is not done to make the read shorter.

## 3. Task 3 — Guards, notes, close

Run every guard at the committed tree; **derive the list from what exists** and report rather than
substitute if one this dispatch names is absent. Read each output separately. Verify what is being
committed through `tools/audit/changed_paths.py`. Run `tools/audit/process_check.py` over **this
dispatch** and report what it finds against Cowork.

Anchor drift from the Task 1 amendment is re-aimed **per citation from the drift report's own
numbers**. The handoff and `STATUS.md` are not register-cited surfaces, but **verify that rather than
assume it** — if a register entry cites either, its anchor moves.

`STATUS.md` gains one POINTER entry, written to the standard this wave installs.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283's remedy, OI-274's body-tense half,
OI-288 half (a), OI-289 (stage 2, dispatched separately), OI-290's document-side remedy, OI-296's
sweep, OI-299, OI-300, OI-301, the `CLAUDE.md` mechanism triage (its measurement half is stage 2, its
moving half stage 4), and the owed reads.

## 4. Accepted outcomes

Tasks 1 and 3 are bounded and expected complete. **A2 stopping the split is a success** — that is the
check working, and it is why it is a check rather than an assertion. **A1 coming back different is
reportable**, and the declaration is then owed in the same commit.

## 5. Self-check (D-434) — run by Cowork before release

- **#17(a).** Three facts cited to the objects; two assumptions, both from handoff blocks — the
  surface this wave distrusts — each checked before the act resting on it, one carrying a STOP.
- **★ A correction of Cowork's own record.** F3 states plainly that the earlier issue's hard
  constraint was false and that Cowork asserted a property of a script it had not read. The scope it
  produced survives on a different and correct reason (#12, not a guard).
- **Principles.** #12 nothing deleted, blocks move unchanged, history out of scope. #6 D-431 widened
  at its home rather than duplicated. #13 A2 is a STOP.
- **D-431.** No bare quantity; F2's block count is a reproducible count in a named file.
- **Sequencing.** This wave is action, placed first only because gathering done under the current
  recording practice manufactures the errors the gathering exists to find. No item here is justified
  by saving effort, and the earlier issue's two such justifications are removed.
