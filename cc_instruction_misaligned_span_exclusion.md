# CC instruction — re-count the note-side tables with measured-misaligned spans left out (user-ratified 2026-07-19)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, the **OI-184 row in `OPEN_ITEMS.md`** (its two newest
> bracketed additions carry the ruling this dispatch executes), and your own part-2 and
> presence-table records (`cc_note_table_fit_report.md`, the `gen_factor_presence.py` artifacts).
>
> **Current state:** branch `master`, HEAD `73c84b92d3` (verify). The working tree carries TWO
> Cowork-authored uncommitted doc edits riding YOUR commit: `OPEN_ITEMS.md` (the ruling bracket in
> the OI-184 row) and `cowork_handoff.md` (state lines). **PYTHON-ONLY; no `src/`, no build, no
> test suite, no golden, no corpus regen, no re-baseline, NO DECODING, NO EVALUATION, no accuracy
> metric consulted (grep-prove). Pinned instruments and `tools/robust_stop/` import-only.**

**Dispatch author:** Cowork, 2026-07-19, at the user's direction. **The ruling being executed:** the
note-side counted tables (pitch-emission, spelling, event-level boundary) and the chord-factor
presence table are counted with the measured-misaligned ground-truth spans LEFT OUT. **The
criterion, exactly:** a labeled span in which ZERO of the labeled chord's own tones sound (your
existing zero-factors-present diagnostic) is skipped and LISTED — never silently dropped. The
label-sequence tables (chord progression, key transition, entry, bass figure, signature prior) are
alignment-immune and are NOT re-counted — they must remain byte-identical.

## Task 1 — establish the criterion before using it (the Class-B obligation)

Before any re-count: enumerate every zero-factor span (all folds' population — the diagnostic
counted 275 triad + 57 seventh spans at the all-326 fit) into a generated list artifact, and
**verify a sample of 10 at the note data** (chosen by fixed seed, listed): for each, show that the
labeled chord's tones DO sound immediately before or after the span (an anchoring shift — the
misalignment signature confirmed) rather than the label being genuinely tone-free. **If ANY sampled
span shows the label's tones nowhere in its neighborhood (it is not an anchoring error), STOP and
report** — the criterion would then be excluding genuine annotations, which refutes it.

## Task 2 — the re-count

With the criterion established: re-run the note-side counting (`gen_note_tables.py`,
`gen_factor_presence.py`) with zero-factor spans excluded from every numerator and denominator
(emission, spelling, event-boundary, presence), per fold + all-326. The excluded-span list and its
per-fold counts are declared on every artifact, marked **INTERIM — retired by the OI-184 substrate
repair** (after which the criterion must find zero spans and remains as an alarm). Unchanged:
the reliability rule, the smoothing constant, the part-2 exclusions (flagged pieces, anacrusis
measures, multi-meter pieces), the genre-scope declaration.

**Expectations to check and report (never adjust):** the seventh-presence value should move toward
the diagnostic's aligned-conditional figure (≈ 0.97); the triad third-versus-fifth ordering should
be re-reported (the ~1-point inversion sat inside the contamination band — state whether it
persists on clean data); the emission and spelling headline values should move little (the
contamination was ~1.3–2.1 %) — a LARGE movement anywhere is a finding to report prominently.

## Invariants and commit

Label-side tables byte-identical (prove); part-2 note-event substrate file untouched (the exclusion
is a counting rule, not a data edit); combined capacity re-checked per fold (STOP if any fold
fails); byte-reproducible; all figures generated. **One commit:**
`tools: note-side re-count with measured-misaligned spans left out (interim until the alignment repair; user-ratified)` —
amended generators, re-counted note-side + presence artifacts, the span-list artifact, this file
(force-add), the two riding Cowork doc edits. Push **origin only**.

**Report:** the Task-1 sample verification (the 10 spans, each with its neighborhood evidence); the
before/after table values; the excluded-span counts per fold; capacity; reuse-versus-new; anomalies
(a surprise is reported, never built around).
