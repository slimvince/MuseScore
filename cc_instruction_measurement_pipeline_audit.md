# CC Instruction: Measurement-pipeline integrity audit — ALL corpora, source → verdict

## Why (the mandate)

Two corrupting bugs in the measurement chain were found *by accident* this session — the
declared-mode drop at score ingestion (`addKey:5978`) and the applied-chord root error at
ground-truth parsing (`dcml_parser:386`). Both turned **pipeline artifacts into apparent
analyzer errors**. Every precision number (headroom, 95%-functional, S1/S2/S3, OQ-1) rests
on this chain. **Before any of it is trusted, audit the WHOLE chain, unprejudiced.**

**Goal:** after this audit + the fixes it scopes, *a region flagged as an error must
correspond to a REAL disagreement between what the composer wrote and what our analyzer
inferred* — never an artifact introduced anywhere from source acquisition to the final
bucket. **Find ALL error sources; do not stop at the two known bugs.**

**This run is READ-ONLY analysis + targeted probes. NO fixes** — find them all first, so
they land in ONE coordinated re-baseline, not piecemeal. The applied-root fix instruction
is HELD until this ledger exists. Base `a4ae4a9203`+. Method A–H; never-guess; **unprejudiced
= actively HUNT each stage, don't just re-confirm the two known bugs.** You may use
parallel sub-agents per corpus/stage; the instruction defines the full scope so nothing is
skipped.

## PRIOR EVIDENCE TO FOLD IN (from the functional-residual dossier — extend, don't rediscover)

The functional-residual investigation (`cc_functional_residual_dossier.md`) already
surfaced concrete artifacts via real-case tracing of the Bach 2576 "neither" mass. Treat
these as CONFIRMED/SUSPECTED inputs; the audit's job is to verify-at-source, **size them
corpus-wide across ALL corpora**, and find what they MISSED — not re-trace the same cases.

**CONFIRMED bugs (Cowork-verified at source — going into the ledger as findings):**
1. **S2 ingestion — declared-mode drop.** `addKey` fifths-only dedup
   (`importmusicxmlpass2.cpp:5978`) suppresses the piece-initial empty-sig KeySig → mode
   lost → resolver `UNKNOWN`. Affects the Bach gate set (.xml import).
2. **S3 parse — applied-chord root.** `dcml_parser.py:386`
   `primary = numeral.split('/')[0]` discards the `/X`; `_compute_root_pc` roots the
   primary in the local key. WiR-rntxt path. (TSV path resolves applied via `relativeroot`.)
3. **S3 parse — minor-key leading-tone `viio`.** `_DEGREE_SEMITONES_MINOR` (`:77`) roots
   degree VII at tonic+10 (subtonic); DCML's minor `viio` is the leading-tone triad at
   tonic+11. So `viio6` in g-minor → parser F, true F♯. **Hits BOTH rntxt AND TSV paths**
   (both use this table) — so it likely contaminates the non-Bach corpora too (UNMEASURED
   — size it).

**The TRUE-ROOT ORACLE (use it systematically).** music21's `roman.RomanNumeral(figure,
key)` maps a notation RN → its correct root, INDEPENDENT of the buggy parser. CC piloted
it on Bach (parser-root ≠ true-root in 557/2576 = 21.6%; ours == true-root in 366 = 14.2%).
**The audit must run this corpus-wide on ALL corpora** to count *exhaustively* (not sample)
how many ground-truth roots the parser computes wrong — per corpus, per bug class. That
number is the S3 artifact rate.

**SUSPECTED (from the dossier — verify + size):**
- **S4 alignment noise** (dossier §5.5): some "neither" cases are time-overlap artifacts —
  DCML's annotation lands on an adjacent beat/region, mis-pairing. Test for systematic
  offset (pickup/measure-numbering) AND incidental adjacent-beat mis-pairing.
- **NHT over-segmentation** (dossier §2.3, NHT_HELD 685): our region over-segments an
  embellishment inside a sustained harmony → flagged as disagreement. Is this an
  S2-ingestion/segmentation issue, an S4 granularity-alignment issue, or genuine? Classify.
- The mode-drop + both parser bugs together accounted for a large fraction of the Bach
  "functional residual" — meaning the headroom dossier's "95% functional" is materially
  inflated. The audit quantifies the TOTAL inflation across all corpora.

## The pipeline stage map — audit EVERY stage × EVERY corpus

For each corpus (below), trace the full path and classify each stage
**CONFIRMED-CLEAN / SUSPECTED / CONFIRMED-BUG** with evidence ([code]/[probe]):

**S1 — SOURCE.** Acquisition, identity, currency, format. Are the source files
current/correct/unmodified at HEAD? (corpus_audit C1 pinned snapshot sources — EXTEND to
ALL, incl. the cross-corpus `.ours.json` *binary-staleness* already found.) Per-corpus
format (.mscx/.xml/.mxl/.musicxml/.tsv/.rntxt) and provenance.

**S2 — OURS-SIDE INGESTION** (score → the pitch/tick stream our analyzer consumes — the
LEAST-audited, HIGHEST-risk stage). Per import path (MusicXML import [mode-drop lives
here], native .mscz, music21 export), HUNT for anything that makes our analyzer see a
DIFFERENT score than the annotator did:
- key signature + **mode** (confirmed bug — is it the ONLY keysig issue?);
- **pickup/anacrusis** handling (a measure-numbering or tick offset here mis-aligns
  EVERYTHING downstream — the classic corpus killer);
- **repeats / voltas** (expanded in our tick timeline? in the annotation's? must match);
- ties (held vs re-struck — does the analyzer see the right sounding pitches?);
- tuplets, grace notes, ornaments (realized or not?);
- transposing instruments (concert vs written pitch);
- multiple voices/staves collapse; chord-symbol vs notated-pitch;
- the tick timeline our analyzer builds vs the score's nominal time.

**S3 — GROUND-TRUTH PARSING** (annotation → root_pc/quality/key/tick). Audit ALL of
`dcml_parser` (not just :386):
- rntxt path: the tokenizer (beat/key/chord tokens), `_compute_root_pc` (the degree regex,
  degree maps, accidental/mode handling) for **every** numeral class (not just applied),
  key resolution (localkey/globalkey/relativeroot), tick/beat conversion;
- TSV path: the columns, mn/mn_onset, relativeroot resolution;
- music21 `.json`: what it represents (chord labels vs RN), version provenance (v9.9.1,
  recorded), whether it's used as input where it shouldn't be;
- enharmonic/spelling, chord-symbol-vs-numeral divergence, `@none`/rest handling.

**S4 — ALIGNMENT** (joining ours-ticks ↔ DCML-ticks — the second classic killer).
`align_dcml_regions` time-overlap + the new granularity unit. HUNT for systematic offsets:
measure numbering (mc vs mn, 0- vs 1-indexed), pickup offset, repeat expansion mismatch,
the quarterbeats×480 / beat conventions, the lenient-OR ≥50% rule's edge behavior. **A
one-measure or pickup misalignment would manufacture errors corpus-wide** — test for it
explicitly (e.g. do aligned pairs' onset ticks actually coincide, or is there a constant
offset on pickup scores?).

**S5 — COMPARISON / CLASSIFICATION.** `classify_pair` / `three_way_classify`: root match,
quality match, `normalise_rn` (the It6/Ger/Fr/N holes — F-2), enharmonic pc-collapse
(does it over- or under-collapse?), the buckets, the music21 three-way leg.

**S6 — AGGREGATION / REPORTING.** Coverage denominators (326/353), per-corpus vs aggregate
honesty, stale-output detection, cross-corpus orchestration.

## The per-corpus matrix (cover ALL — heterogeneous paths)

| Corpus | GT format | Ingestion path | Audit focus |
|---|---|---|---|
| Bach chorales (gate) | WiR rntxt | music21→.xml→MusicXML import | rntxt parser (S3, the known bugs) + import mode-drop (S2) + pickup/align (S4) |
| corelli, mozart, chopin, beethoven(ABC), grieg, schumann, dvorak, tchaikovsky, bach_en_fr_suites, cpe_bach | DCML .tsv (`harmonies`) | .mscx native | TSV parser (S3), .mscx ingestion (S2), the binary-stale `.ours.json` (S1), cpe_bach "0 regions" (known — root-cause it) |
| music21 `.music21.json` | (algorithmic, not GT) | — | confirm it's used ONLY as the three-way filter leg, never as ground truth (corpus audit C2) |
| jazz (effendi/omnibook/rampageswing) | NO ground truth | — | confirm they're not silently feeding any precision metric (they have no GT — used only for qualitative) |
| snapshot scores (11) | golden JSON (ours-pinned) | .mscx | confirm goldens are regression-pins only, not correctness GT |

## The holistic trace method (the decisive test)

For each corpus, **sample ≥20 flagged errors (root_err / quality_disagree) and trace each
end-to-end:** (a) is the ours-side pitch/tick what the score ACTUALLY contains (open the
source)? (b) is the DCML-side root/quality/key/tick what the annotation ACTUALLY says
(read the rntxt/tsv line)? (c) do they actually co-occur in time (alignment correct)?
Classify each flagged error:
- **PIPELINE ARTIFACT** (ingestion/parse/align bug — our analyzer or the GT is right but
  the chain corrupted it) → a bug class to fix;
- **GROUND-TRUTH LIMITATION** (the annotation itself is wrong/idiosyncratic);
- **GENUINE ANALYZER ERROR** (the real precision target);
- **LEGITIMATE AMBIGUITY / CONVENTION** (defensible disagreement — the ceiling).
The artifact classes that emerge ARE the bug taxonomy. Report the artifact rate per corpus
(what fraction of "errors" are not real) — this is the number that says how much every
headline figure is inflated.

## Deliverable — `cc_measurement_pipeline_audit.md`

§1 the stage×corpus matrix (clean/suspected/bug per cell, with evidence). §2 the complete
**error-source ledger**: every artifact class found, its stage, its corpus scope, its
estimated blast radius on the headline numbers (headroom root_err, 95%-functional, S1/S2,
BIR 13/7). §3 the trace results (artifact rate per corpus). §4 a **prioritized
elimination plan** — all fixes batched into ONE coordinated re-baseline (parser fixes,
ingestion fixes, alignment fixes), with the order and the expected number-movement. §5 what
is CONFIRMED-CLEAN (so we stop suspecting it). §6 unknowns / what needs deeper probing.
Every claim [code]/[probe]/[trace]; every rate sampled-tagged with N.

Stop conditions: finding an alignment/ingestion bug with corpus-wide blast radius (report
immediately — it may dwarf the two known parser bugs); discovering a corpus is being used
for something it can't support (e.g. jazz feeding a precision metric); any stage you cannot
audit without building (note it, don't guess). **Do not fix anything this run** — the
ledger drives the coordinated fix batch next.
