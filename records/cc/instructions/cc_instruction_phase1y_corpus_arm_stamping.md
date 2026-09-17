# CC dispatch — phase 1y: stamp the corpus with the arm that produced it

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), on the user's direction of the same date.**
> Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1y_corpus_arm_stamping.md`.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).**
>
> **★ WHY THIS IS NOT APPARATUS WORK, AND WHY IT PRECEDES THE READS.** Under D-438's own test — *does
> the row's subject bear on the analysis, its inputs, or an instrument a measurement depends on?* —
> OI-307 **gates**. The corpus under `tools/corpus/<preset>` is what block (A)'s hard regression stop
> reads. A stamp that cannot distinguish which inference arm produced it is #16 unmet at the point #16
> was written for.
>
> **★★ DO NOT REGENERATE ANY CORPUS.** Regeneration is a re-baseline act under block (A)'s discipline
> and requires its own ratification, snapshot and explained diff. **This wave changes the STAMP and
> the CHECK. It does not produce, replace or refresh a single `.ours.json`.** If a task seems to need
> a regeneration, STOP and report.
>
> **★ NO `src/` change, no goldens, no `tools/robust_stop/` movement, no behaviour change to the
> analysis, no fix to inference, no design.** Phase 1 under D-231.

## 0. THE PREMISE LEDGER (#17a)

**FACT — read at the object by Cowork in the session that wrote this dispatch:**

- **F1.** `tools/run_bach_preset.py:119-133` writes the corpus manifest with these fields and no
  other: schema, corpus, preset, timestamp, git hash, expected count, ours count, complete,
  music21 version, the `batch_analyze` binary's path/size/mtime, and the per-score block.
  **There is no field recording which inference arm produced the outputs.**
- **F2.** `tools/batch_analyze.cpp:4917` initialises the joint artifact directory empty and the joint
  path runs only `if (!jointInferenceDir.empty())` at `:5590` — the flag is **opt-in**, so the same
  binary produces either arm's output depending on invocation.
- **F3.** `tools/run_bach_preset.py:310` offers a flag to **skip** the clean-slate, which establishes
  that clean-slating the output directory is the default behaviour.

**F1 and F2 together are the defect:** the manifest stamps the instrument and not its invocation, so
two corpora produced by different pipelines are indistinguishable in the record.

**ASSUMPTION — each checked before the act it licenses:**

- **A1.** That the corpora currently committed under `tools/corpus/` were produced through the joint
  arm. Cowork has this from the OI-178 adoption narrative, which is a secondary surface.
  **This must be ESTABLISHED, not assumed** — the whole point of the wave is that the record cannot
  currently tell. → **Task 3**.
- **A2.** That `validate_corpus_dir` is the function that reads and enforces the manifest, and that
  `characterise_bir_false.py` and `tools/a8_rebaseline_measure.py` both route through it. → **Task 2.1**.
- **A3.** That `CLAUDE.md` gate block (C) still states corpus commands omitting the flag **after**
  phase 1x's edits. Phase 1x corrected `BUILD_AND_TEST.md` and deliberately did not touch the gate
  block; whether the block reads as Cowork last saw it is unchecked. → **Task 4.1**.

## 1. Task 1 — Stamp the arm

Add to the manifest a field recording **which inference arm produced the outputs**, and — where it is
the joint arm — the artifact directory it was given. Derive it from the invocation actually used, not
from a parameter default.

**Bump the manifest schema.** A manifest written before this change cannot be distinguished from one
written after unless the schema says so.

## 2. Task 2 — Make the check discriminate, with a lawful transition (#23)

**2.1 Check A2** — establish which function enforces the manifest and which measurement tools route
through it. Report the set; if a measurement tool reads the corpus **without** that validation, that
is a second hole and a finding.

**2.2 The new check.** A manifest at the new schema must carry the arm, and a mismatch between the
recorded arm and the arm a measurement expects is a **hard failure**.

**2.3 The transition, declared and bounded.** Manifests at the **old** schema carry no arm and must
not be treated as if they did. They report a distinct **ARM-UNKNOWN** state: loud, named in the
output, and **not** a silent pass — but not a hard failure either, until Task 3 has established what
those corpora actually are. State the retirement condition in the code and in the row: once every
committed corpus carries an established arm, ARM-UNKNOWN becomes a hard failure.

**This is #23 in its plain form** — a temporary violation of the end state, declared, bounded, with a
retirement map. Do not skip the declaration because the window looks short.

## 3. Task 3 — Establish A1, or record that it cannot be established

For each committed corpus directory, establish **from the record** which arm produced it: the OI-178
adoption record, `tools/robust_stop/manifest.json`, the commit that produced the directory, and the
per-score manifest's own binary stamp. Cite what you use.

- Where the arm **is** establishable, back-stamp the manifest with the arm **and the citation that
  establishes it**. A back-stamp without its evidence is an assertion, and it would re-create the
  defect in a form that now looks checked.
- Where it is **not** establishable, leave ARM-UNKNOWN and say so. **Do not guess, and do not
  regenerate to find out** — regenerating to learn what a corpus was is the re-baseline this dispatch
  forbids.

**Report both sets.** If any committed corpus turns out to be legacy-arm output, that is a **#13
STOP** — it would mean the hard stop has been reading a corpus from the dormant pipeline, and nothing
else in this dispatch matters until that is on the table.

## 4. Task 4 — The command sites

**4.1 Check A3** at `CLAUDE.md` gate block (C)'s own text. Report what it currently says.

**4.2 Do NOT redirect the procedure.** Block (C)'s commands write into the directory block (A) reads,
and changing what a ratified gate block instructs is the **user's ruling**, not a session's. What this
wave may do is make the *consequence* visible: with Task 1 and Task 2 in place, a corpus regenerated
by those commands is stamped legacy and the check says so.

**4.3 Row the residue** — that block (C)'s documented procedure clean-slates the hard stop's corpus
with legacy output, and that redirecting it is owed as a user ruling. Cross-reference OI-307 and
OI-308 (the flag default, phase 3).

## 5. Task 5 — Guards, notes, close

Run every guard at the committed tree, with the list **derived by `gen_guard_state.py`** rather than
from this dispatch. Read each output separately. Six guards were failing as of phase 1x; report which
still are and whether this wave changed any.

Verify what is being committed through `tools/audit/changed_paths.py`. Run
`tools/audit/process_check.py` over **this dispatch**.

**Delete the stray zero-byte file `key` at the repository root** — Cowork read it this session and it
is empty.

`STATUS.md` gains one POINTER entry, written as a pointer.

**Still owed and NOT in this dispatch:** the sixty-six reads (next, in dedicated waves), OI-280,
OI-282, OI-283's remedy, OI-274's body-tense half, OI-288 half (a), OI-289's residue at OI-302,
OI-290's document-side remedy, OI-296, OI-299, OI-300, OI-301, OI-305's STALE findings, OI-306,
OI-309, OI-310, the write-list divergence, D-055, and the queued phase-1t dispatch.

## 6. Accepted outcomes

**Task 3 finding a committed corpus is legacy-arm output is a STOP and the most valuable outcome this
wave could produce.** **A1 coming back unestablishable is a result** — it would mean the record cannot
say what its own measurement corpus is, which is the finding stated in its strongest form. **A2
turning up a measurement tool that bypasses validation is a second hole and should be rowed, not
fixed here.**

## 7. Self-check (D-434) — run by Cowork before release

- **#17(a).** Three facts, each read at the object — the manifest fields, the opt-in flag, the
  clean-slate default. Three assumptions, all checked first, and A1 is labelled precisely because the
  wave exists to establish it.
- **Principles.** #16 — the stamp is the point. #23 — the transition is declared and bounded with a
  retirement condition rather than assumed short. #19 — a back-stamp without evidence is refused.
  #13 — the legacy-corpus case is a STOP. #12 — nothing regenerated, nothing replaced.
- **Scope.** No `src/`, no goldens, no corpus regeneration, no gate-block edit. The one deletion is a
  zero-byte stray Cowork read.
- **Sequencing.** This precedes the reads because OI-307 gates under D-438's own test; it is the only
  item on the board that does, and the freeze on apparatus work stands for everything else.
