# CC INSTRUCTION — Wave-3 addendum: two DDMAL pickups + the DLC column exposure (2026-07-04)

**Status: ACTIVE DISPATCH (the only open instruction). Two small tasks in one dispatch, ONE change class
per commit: Task A is code-free acquisition (the Wave-3 mechanism, verbatim); Task B is the queued additive
parser exposure (`tools/dcml_parser.py` ONLY — no `src/`, no consumer changes, byte-identity proven). The
frozen gate corpus stays byte-untouched throughout.**

## Mandatory reads BEFORE any work

1. `CLAUDE.md` (bash rules; the gate = the 53/24/53 case-identity sets) + `STATUS.md` header + 22k.
2. `cc_corpus_wave3_report.md` — the wave this addendum extends (esp. §6 the WiR/KMT correction, §7 the
   humdrum-data closure that surfaced the chorale-annotation repo).
3. `tools/REPRODUCIBILITY.md` (the `corpora/gt/` Wave-3 section — Task A follows it verbatim) +
   `cowork_score_census.md` §3/§4/§8c (intake rule: full N1–N20 needs note per row).
4. `tools/dcml_parser.py` — read the whole parser before Task B; know exactly which columns it reads today
   (numeral/chord/keys + cadence/phraseend since 21k) and which consumers import it.

## Task A — two DDMAL direct pickups (code-free; the Wave-3 clone+pin+inventory mechanism)

1. **KMT — `github.com/DDMAL/key_modulation_dataset`** (the upstream of the key/modulation/tonicization GT
   the audit wrongly located inside WiR — Wave-3 correction, STATUS 22k). Clone + hash-pin into
   `corpora/gt/` (held-out, hash-pin-only). **Verify at the data and report:** what it actually contains —
   annotation format, score alignment (the DLfM 2020 paper describes textbook examples: Aldwell, Kostka,
   Reger…), piece/example counts per textbook, license. Score against the full vector (expected primary:
   **N5**; report any other layer per the intake rule — every GT layer inventoried).
2. **`github.com/DDMAL/Flexible_harmonic_chorale_annotations`** (surfaced by the Wave-3 humdrum-data
   closure). Clone + hash-pin + WALK it: what is it (annotator(s), format, chorale coverage, how the
   "flexible" annotations differ from single-reading RN)? **⚠ It overlaps the GATE repertoire (Bach
   chorales). RECORD-ONLY:** inventory + registry row + census row; it must NOT be wired to, compared
   against, or even bulk-diffed with the gate corpus in this dispatch — any use over gate pieces is a
   future user ruling (census §4 dedupe rule / the M3 contamination lesson). Expected needs value: a
   potential SECOND annotation layer over gate-class chorales (**N2** candidate) + N1-residual — record
   that as expectation, not as measurement.

Registry: two `wave3_sources` rows (the established generator; deterministic regen, two-run byte-identical
check). Census §1: two rows marked "entered at Wave-3 addendum, provenance this report".

## Task B — the DLC column exposure (`pedal` + `figbass`), additive, byte-identity proven

**What:** `tools/dcml_parser.py` gains two additive `DcmlRegion` fields parsed from the DLC harmonies TSVs:
`pedal` (the pedal-point column — N20) and `figbass` (the figured-bass/inversion column — N10). Both were
audit-verified present on every held DLC corpus (header row of `harmonies/*.tsv`; e.g. K279-1: …
`localkey · pedal · chord · numeral · form · figbass · changes …`).

**Rules:**
- **Additive only.** New fields with safe defaults; NO existing field's parsing changes; NO consumer
  changes (no tool starts reading the new fields in this dispatch); no signature breaks for existing
  callers.
- **Do not touch** `src/`, the frozen gate corpus, or any other tool's logic.
- The DCML `form` column is **chord-morphology** (NOT form/section GT — audit-verified); if you touch its
  neighborhood, keep the existing comment/claim accurate but do NOT expose it as if it were section GT.

**Proof obligations (measured, not argued):**
1. **Byte-identity of every existing output:** run the gate reproduction (`characterise_bir_false.py`
   ×3 presets — 53/24/53, case-identity set-diff empty both directions) AND re-run the A-8 instrument's
   summary on one preset, diffing its output against a pre-change run (byte-identical expected — nothing
   reads the new fields). Any diff = STOP.
2. **The exposure statistics (the point of the increment):** per-corpus counts of non-empty `pedal` and
   `figbass` cells across all 40 DLC members (+ the Mozart cadence-layer corpora), reported as a table —
   this is the N10/N20 material-size fact the future L4-evidence-channel and pedal-point-span designs
   will cite.
3. Any existing unit tests over the parser still pass; if the parser has none covering the new paths, add
   the minimal test that pins the two new fields on a known fixture (full-coverage standing objective).

## Task C — report + fold

- Report `cc_wave3_addendum_report.md` (force-added): Task-A inventories + verification, the Task-B edit
  surface + both proofs + the statistics table, reuse-vs-new + what retires (expected: retires nothing;
  the exposure closes the "parser-dropped columns" note), **commit SHAs mandatory** (report commit cites
  prior SHAs, per precedent).
- Suggested commits: (1) Task A clones/registry/census · (2) Task B parser + test · (3) the
  `docs(cowork):` fold + report. **Fold list — exactly these, surfacing anything else dirty:** `STATUS.md`
  (the 22k Wave-3-ratified append + addendum dispatch line), `cowork_handoff.md` (header),
  `cowork_score_census.md` (the N2/N5 corrections + Wave-3 state updates), `cowork_census_full_needs_audit.md`
  (the §7 corrections addendum), force-added `cc_instruction_wave3_addendum.md`.
- Local/unpushed, fork-only.

## STOP conditions

Task-B byte-identity fails anywhere (gate set-diff non-empty, A-8 summary diff non-empty); either DDMAL
repo's content contradicts its record in a way that changes its handling (surface, don't improvise); any
temptation to compare/wire the chorale-annotation set against the gate corpus (record-only this dispatch);
anything under `src/`; the registry regen stops being deterministic.
