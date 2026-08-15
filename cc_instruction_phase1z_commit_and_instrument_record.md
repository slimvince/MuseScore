# CC dispatch — phase 1z: commit what is pending, record the instrument change, correct OI-315

> **Status: ACTIVE DISPATCH. RE-ISSUED 2026-08-03 (Cowork)** — widened from its first issue, which was
> written before read wave 1 ran and before the user's OI-315 ruling. Read IN FULL.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1z_commit_and_instrument_record.md`.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).**
>
> **★ THIS IS THE LAST WAVE CARRYING NON-READ WORK.** After it the mechanism set is FROZEN and the
> waves are dedicated reads. A tool defect found from here is **rowed, not fixed**, unless it blocks a
> read.
>
> **★ NO `src/` change, no goldens, no corpus regeneration, no `tools/robust_stop/` movement, no
> behaviour change to the analysis, no fix to inference.** Phase 1 under D-231. Task 3 corrects a
> SPECIFICATION that describes code; it does not touch the code.

## 0. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork this session:**

- **F1.** `ARCHITECTURE.md:3510-3515` specifies the piece-start shortcut **in the present tense**, as
  *"the only exception"* to the priority of evidence, and calls it *"a deliberate pragmatic choice."*
- **F2.** `src/composing/analysis/key/keyresolver.cpp:291-293` states in its own comment: *"The former
  declared-mode piece-start short-circuit was removed in 4b-i."*
- **F3.** **D-058 is homed at `ARCHITECTURE.md:3510-3514`, status live, and carries the LEGACY
  mark** — `decisions/group_F.md:126-138`. Its mark is correct under OI-289's test; what is wrong is
  that the specification claims the mechanism is **live**, when the code says it was **removed**.
  Dormant and deleted are different states and the specification claims neither.
- **F4.** `tools/batch_analyze.cpp` stamps the arm per file — `:4695` `"joint"`, `:1448` the standard
  writer's value, `:3443` `"fullspine"`.
- **F5.** `.gitignore:26` ignores `/tools/corpus/`; the gate corpus is not under version control.

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That `CLAUDE.md` gate block (A) names `tools/a8_rebaseline_measure.py` as the pinned
  instrument. The block has been edited since Cowork last read it. → **Task 2.1**.
- **A2.** That the `+0/−0` robust-stop result is in a **committed artifact**, not only a session
  report. → **Task 2.2**; if absent, generate one before the record cites it.
- **A3.** That `docs/key_path_design.md:65-73` records the removal and dates it as OI-315's table
  quotes. Cowork read that quotation in the row, not the document. → **Task 3.1**.
- **A4.** Whether the `ARCHITECTURE.md` section containing F1 **already carries an OI-232-style
  scoping sentence**. If it does, the correction sits inside that scope; if not, the corrected
  paragraph needs its own. → **Task 3.2**.

## 1. Task 1 — Commit what is pending

Two waves are uncommitted: phase 1y and read wave 1. Verify through `tools/audit/changed_paths.py`
what is outstanding; if anything is modified outside those two waves and this one, **STOP and report**.
Commit them together with this wave's work, per D-230 — the ratifications below belong in the commit
that records them.

## 2. Task 2 — The instrument record at block (A)

**2.1** Check A1 and report what block (A) says about the pinned instrument.
**2.2** Check A2 and cite the artifact.

**2.3** Write the record into block (A)'s provenance — the block that pins the instrument is where a
change to it belongs (#7). It carries: that the instrument now declares an expected arm by default
and **refuses** a corpus whose stamp disagrees; that it **cannot move a figure, only refuse**, cited
to the artifact from A2; the reason — **the defect was that an opt-in flag created an undetectable
hole, and an opt-in detector would reproduce its shape**; and that reversal is one default. Register
entry in the same commit.

## 3. Task 3 — OI-315

**3.1** Check A3 at `docs/key_path_design.md` itself.

**3.2** Check A4 at the section around F1.

**3.3 Correct the specification.** Replace the false paragraph with a statement of what the opening
**actually does** at HEAD, scoped correctly per A4 — this is the legacy key path, and the corrected
text must not read as though it described the production key path. **Add a tried-and-closed line
naming the removal**, using the construction this document already uses at `ARCHITECTURE.md:1420`,
`:1344` and `:306`. Do not invent a new form.

**3.4 D-058 becomes `superseded-in-fact`** — the register's own vocabulary for a later build replacing
what a decision governs without a ruling that names it. **Not falsified**: it was not shown wrong, it
was removed. **The LEGACY mark stays** — its subject is still the legacy path (F3). Verbatim re-taken
from the corrected text; the former preserved in provenance (#12).

**3.5** `docs/key_path_design.md`'s self-contradiction — §1 recording the removal against §2.1 and §5
treating the shortcut as reusable — **stays rowed and is not corrected here.** It is a separate
document and a separate act.

**3.6 Flip OI-315.**

## 4. Task 4 — Ratify the twenty-eight entries

Read wave 1's entries are ratified as drafted, **each keeping the status the record states**, several
of which are *"not stated"*. Ratification confirms the register records the decision correctly; it is
not a judgment that the decision is good. Record per the register's existing entry-ratification
convention.

## 5. Task 5 — Two facts into the record, not only into rows

**5.1** F5 into OI-312: the corpus block (C)'s commands clean-slate is **unversioned**, so recovery is
not a re-run but a **re-baseline-grade act** — new timestamp, new hash, its own snapshot, explained
diff and ratification. Detection is not prevention; redirecting the procedure stays the user's ruling.

**5.2** F4 into OI-307's resolution note: the arm was **always readable per file**, which turned the
back-stamp from an assertion into a reading of the object (#15). A future session facing a provenance
gap should look for an existing stamp before designing one.

## 6. Task 6 — Guards, notes, close

Run every guard at the committed tree with the list **derived by `gen_guard_state.py`**. Report which
pre-existing failures still fail and whether this wave moved any — **and fix none.** The freeze starts
with this wave's close.

Run `tools/audit/process_check.py` over **this dispatch**.

`STATUS.md` gains one POINTER entry stating plainly that the next waves are **dedicated reads** and
that the mechanism set is frozen.

## 7. Accepted outcomes

**A1 or A3 coming back different is reportable** — the record goes where the object actually says.
**A2 absent means the measurement is generated into an artifact before the record cites it**; a record
citing a session report is the defect D-431 exists against. **A4 finding no scoping sentence means the
corrected paragraph carries its own** — do not leave it ambiguous about which arm it describes.

## 8. Self-check (D-434) — run by Cowork before release

- **#17(a).** Five facts read at the objects — the specification paragraph, the code comment, the
  register entry, the arm stamps, the ignore rule. Four assumptions, all checked before the acts
  resting on them; A3 is an assumption precisely because Cowork read it in a row rather than in the
  document.
- **Principles.** #7 — the instrument record goes at the block that pins it; the specification
  correction at the specification. #12 — nothing deleted, former verbatims preserved, the removal
  recorded as tried-and-closed. #15 — 5.2 names the reading-the-object lesson for the next session.
  #10 — a false statement about an inference mechanism in the canonical document is phase 1's own
  truth clause, not a tidy.
- **D-431.** No bare quantity; the entry count is named as read wave 1's set rather than transcribed.
- **Scope.** Task 3 touches a specification, never the code. The freeze begins at this wave's close.
