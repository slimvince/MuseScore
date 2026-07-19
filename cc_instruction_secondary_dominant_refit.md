# CC instruction — the secondary-dominant pooling amendment (re-count of the chord-progression table) + the chord-factor presence table

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, **`C:\s\MS\cowork_sensitive_cell_probe.md` (the ratified
> findings this dispatch executes — read it in FULL; its section 0 defines the vocabulary this
> instruction uses)**, and your own part-1/part-2 records (`cc_label_table_fit_report.md`,
> `cc_note_table_fit_report.md`, on disk).
>
> **Current state:** branch `master`, HEAD `57ed94a6a4` (verify). The working tree carries THREE
> Cowork-authored uncommitted doc edits that ride YOUR commit (verify each is its only diff):
> `cowork_sensitive_cell_probe.md` (new file — the ratified probe), `cowork_handoff.md` (standing
> rule + state lines), `OPEN_ITEMS.md` (a dated addition inside the OI-184 row), and
> `cowork_joint_estimator_factorization.md` (one added paragraph in §5 — the ratified
> below-threshold scoring rule).
>
> **PYTHON-ONLY; no `src/` edit, no build, no test suite, no golden, no corpus regen, no
> re-baseline, NO DECODING, NO EVALUATION, no accuracy metric consulted (grep-prove, as in parts
> 1–2).** Hard stops as before: pinned instruments and `tools/robust_stop/` are import-only.

**Dispatch author:** Cowork, 2026-07-19, at the user's direction — executing the three
user-ratified probe findings (options 1a and 3a are yours to execute; option 2a is a specification
sentence already recorded in the factorization document §5 and needs no code — verify the doc edit
rides your commit, nothing more).

## Task 1 — the pooling-ladder amendment and the re-count (ratified option 1a)

**What changes:** the chord-progression table's pooling ladder (your part-1 `gen_label_tables.py`
context and outcome chains) gains ONE level for chords with an applied target (the secondary
dominants `V/x` and applied leading-tone chords `viio/x` — every class whose normalized form
carries a target): **group their outgoing progressions by RELATION TO THE TARGET, pooled across all
targets.** Concretely: for an applied-chord context, before falling to the mode's plain frequency
table, its continuations pool into relation cells — at minimum "moves to a chord of its target
degree" (resolution) versus "moves elsewhere"; if the counts support it under the unchanged
reliability rule (≥ 20), the resolution cell may keep sub-cells (target as triad versus target as
seventh chord; target root position versus inverted) — let the counts decide mechanically, never
by choice. The relation cells are counted across ALL targets (the same transposition-pooling
principle the table already uses across keys). Where exactly the level sits in the ladder
(context side, outcome side, or both) follows from your as-built part-1 realization — decide by
the same mechanics, REPORT the as-built form explicitly, and namespace the new cells as you did
in part 1 (the key-collision lesson).

**What must hold:**
- The reliability rule, the smoothing constant, and every other ratified protocol constant are
  UNCHANGED. No value is hand-chosen anywhere.
- Tables 2–6 and the note-side artifacts must be **byte-identical** after the re-count (the
  amendment touches table 1 only) — prove it and report it. If the regeneration moves anything
  else: STOP.
- All five fold variants + the all-326 variant re-counted; the parameter-inventory artifact
  regenerated; the capacity bound re-checked per fold (STOP if any fold fails).
- Reconciliation totals unchanged (labels 18,418 / transition pairs 16,372 / key changes 1,720).
- Byte-reproducible on a second run.

**Report (the review surface):** the counted resolution cells themselves — for example
P(moves to its target | secondary dominant) overall and any sub-cells that cleared the threshold —
with raw counts shown; the applied-context rows before/after (the probe found them collapsed to
the mode's plain frequency table — show what they resolve to now); the parameter-count delta; and
the three passages' affected transition values (the probe's passage B used
"subdominant → dominant-of-the-subdominant → resolution": state the new numbers so Cowork can
re-run that arithmetic).

## Task 2 — the chord-factor presence table (ratified option 3a)

**What is counted:** from the committed note-event data (`note_events/note_events.json`) and the
same ground-truth segment alignment and exclusions as part 2 (the anacrusis-measure and
flagged-piece exclusions), for each humanly-labeled segment: which of the labeled chord's factors
(root, third, fifth; seventh where the label is a seventh chord) sound among the segment's notes.
The table: **P(factor sounds | factor role, chord family)** — chord family = triad versus seventh
chord; per training fold + all-326; the unchanged reliability rule and smoothing; NEW artifact
files (do NOT regenerate or touch the committed part-2 artifacts — additions only).

**What must hold:** the genre scope limit is DECLARED on the artifact (Bach-chorale values only —
the probe's scope paragraph, verbatim or cited); byte-reproducible; the part-2 artifacts
byte-identical.

**Report:** the counted values themselves (all cells — this is a small table), with the sanity
expectation stated by the user checked and reported: the seventh's presence probability in
seventh-chord segments should be near 1 (a silent seventh nearly never earns a seventh-chord
label) and the fifth should be the most-omitted factor. If either does NOT hold, that is a
prominent finding to report (never adjust anything in response — the counts are the fact).

## Commit

**One commit:** `tools: secondary-dominant pooling level + re-count (table 1) and the chord-factor presence table (ratified probe findings 1a/3a)` —
the amended fitter, the re-counted table artifacts, the new presence-table artifacts, this
instruction file (force-add), and the four named Cowork doc edits riding along. Push **origin
only** (the standing hard stop on the upstream remote).

## Self-check before reporting (standing rule)

Re-read the actual diff: nothing outside `tools/joint_estimator/` + this file + the four named doc
files; pinned instruments untouched; tables 2–6 and part-2 artifacts byte-identical; no decode, no
evaluation, no metric anywhere in the code path; all figures generated. Report: commit hash, file
list, the Task-1 and Task-2 review surfaces above, reuse-versus-new, and anomalies (a surprise is
reported, never built around).
