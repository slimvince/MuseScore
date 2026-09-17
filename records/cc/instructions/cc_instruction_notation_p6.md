# CC instruction — the OI-204 producer input-scoping fix + the dual-arm classified comparison (seams-2 unit "P6" — the switch-ratification evidence)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (the INDEX; NEW rows
> **OI-203/OI-204** ride your Task-1 commit; open their `open_items/` details — OI-204 is THIS
> dispatch's Task 1), `C:\s\MS\cowork_notation_output_contract.md`.
>
> **What this is:** the second-to-last unit of the notation-layer migration (P0–P4, P-strings,
> the register split, and the note-seam unit are DONE — the handoff's dated blocks are the
> record). This unit (1) closes OI-204 (a PRE-SWITCH gate), then (2) builds and runs the
> dual-arm classified comparison over the FULL notation output surface — the evidence the
> user's switch ratification reads (§8.3(d) of the ratified increment plan).
>
> **Current state:** branch `master`; expected HEAD `903125a5dc` (note-seam Task 3+4, pushed)
> — verify via `git show --stat 903125a5dc`; mismatch = STOP. Riding Cowork edits (verify only
> non-yours tracked diffs): `OPEN_ITEMS.md` (OI-203/OI-204 rows), `open_items/OI-203.md`,
> `open_items/OI-204.md`, `cowork_handoff.md` — all commit with Task 1. This dispatch file
> stays untracked.
>
> **Hard stops, always:** push origin only; ANY behavior change with `useJointNotationRecord`
> OFF — byte-identity per commit (three suites green, NO golden refresh); no legacy-analysis
> call on the record path; no inference edit (an output difference is CLASSIFIED, never
> patched toward either arm); files outside the touchable set; a surprise is a STOP (#13).
> VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-27, at the note-seam verification.

**Touchable set:** `src/composing/analysis/joint/jointfactadapter.{h,cpp}` +
`src/composing/analysis/joint/` producer surface (ONLY the Task-1 input-scoping parameter —
an INPUT-surface addition, no inference arithmetic touched; the boundary guard still passes),
`src/composing/analysis/section/**` + `src/notation/internal/**` (ONLY threading the
exclusion parameter through the record-arm call sites), the pipeline-snapshot test dir (the
dual-arm capture), NEW `tools/notation_seams/` comparison outputs + classifier script, the
relevant test dirs + CMake lists, `ARCHITECTURE.md`, `STATUS.md`, register index + detail
files (row flips/notes only), the riding Cowork files. NOT touchable: the decode/scoring
arithmetic anywhere, corpus, goldens, `tools/robust_stop/`.

---

## Task 1 — OI-204: the producer's analysis-input staff exclusion (ONE commit; flips the row or STOPs)

The hazard (row OI-204): the legacy seams exclude chord-track staves from the ANALYSIS INPUT;
the record producer decodes the whole score — on a populated chord track, re-analysis would
consume the previous implode output (self-feedback).

1. `produceNotationRecord` (and `buildAdapterFacts` beneath it) gains the input-scoping
   parameter (`excludeStaves`, the legacy seams' own form): excluded staves' notes never enter
   the L1 note-model view the adapter reads. This is INPUT selection at the producer — the
   layer that owns its input surface (#7); no consumer-side post-filtering anywhere.
2. Every record-arm call site threads the SAME exclusion set the legacy arm passes at that
   seam (the audited call sites: the annotation emitter, implode, tuning, the note-seam
   funnel) — arm-for-arm input parity.
3. **Establishment (#19):** (a) empty-exclusion byte-identity — the producer with an empty set
   is byte-identical to today's (the corpus/parity establishment untouched; prove on ≥3
   corpus stems via the existing producer tests); (b) the exclusion proven — a fixture with a
   populated chord-track staff: the record with exclusion ≠ without, and the excluded staff's
   notes are absent from the adapter facts; (c) suites green, flag-OFF byte-identical.
4. Flip OI-204 in the INDEX (✅ RESOLVED, this commit, mechanism one-line) + a dated note in
   its detail file. The riding Cowork files commit here.

## Task 2 — the dual-arm capture instrument

A test-harness driver (extend the pipeline-snapshot capture machinery — the config-toggle
hook exists at `pipeline_snapshot_tests.cpp:882-886` per the P3a-era report) that runs the
FULL notation output surface TWICE per snapshot-corpus score — flag OFF (legacy) and flag ON
(record) — and serializes both arms: region/annotation outputs (display chord symbols, Roman
numerals, key strings/KeySig writes, cadence + pivot labels, bracket markers, pedal texts),
the implode chord track (symbols/romans/nashvilles/voicings/key runs), tuning offsets, and
the note-seam answers on a declared tick sample (every downbeat of every measure — declared,
deterministic). Deterministic run-to-run (prove: two runs byte-identical). The flag is
restored OFF by RAII scope (the established pattern); default builds stay byte-identical.

## Task 3 — the classified diff (the ratification evidence; ONE generated artifact)

A classifier (`tools/notation_seams/`, #17f) over the two arms' captures, per output item:

- **identical**;
- **inference-driven** — the record's committed reading differs from legacy's (cite the
  segment span and BOTH readings; these are the adoption's expected differences reaching the
  notation surface);
- **presentation-rule** — cite the specific ratified rule: the C1 two-mode display (no exotic
  suffix); the §4.1 gap-scale gates (cite the constant); the pedal suspension (OI-194); the
  alternatives ordering (content score); the grading-vs-display symbol split (D2); the
  aug-sixth symbol coarseness (OI-201); the applied-chord Nashville "?" convention (legacy's
  own, continuity-preserved);
- **input-scoping** — the OI-204 class (post-fix this should measure ZERO on the snapshot
  corpus; a nonzero count is investigated to mechanism before delivery);
- **UNEXPLAINED — the headline class: every entry investigated to a mechanism before this
  dispatch reports; an unexplained output difference at the pre-switch gate is exactly what
  this instrument exists to catch (#13/#15).** An UNEXPLAINED entry that resists mechanism
  is a STOP, not a report line.

Commit the instrument + the classified report artifact (stable filename,
`tools/notation_seams/dualarm_classified_report.json` + a short human-readable summary
beside it). Per-class counts per score and per output class; every non-identical entry
carries its citation.

## Task 4 — doc sync + closing

`ARCHITECTURE.md` (the dual-arm instrument as-built; the input-scoping parameter);
`STATUS.md` closing entry (counts from the artifact). Commits per change-class (suggested:
Task 1; Task 2; Task 3+4); push origin.

## Report

Hashes; the OI-204 establishment evidence (empty-set byte-identity + the exclusion fixture);
the determinism proof; the classified counts (per class, per output surface) and EVERY
unexplained entry's investigated mechanism (target: zero remaining); the input-scoping count
(expected zero post-fix); notable inference-driven examples (2–3, cited, for the user's
reading); suite totals per commit; reuse-vs-new / what-retires; anomalies (a surprise is a
STOP). Standing self-check before reporting.

**After this unit:** P7 (doc sync/close of the partition) — then the record goes to the user
for the SWITCH ratification with this dispatch's classified report as the §8.4 evidence
(the switch commit itself is a separate, Cowork-written, user-ratified dispatch: flag default
flips, pipeline-snapshot goldens refresh against the established record, CLAUDE.md staged-
scope block + STATUS + ARCHITECTURE + the register rows + the handoff dual-path line move
together).
