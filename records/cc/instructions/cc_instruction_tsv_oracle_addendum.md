# TSV-oracle addendum — boundary-source ruling (Cowork, 2026-07-02)

> Addendum to `cc_instruction_tsv_oracle_infrastructure.md`. Your STOP was correct: the instruction's premise
> ("read via the existing diagnostic dump path") was **wrong — Cowork's error**, verified by your exhaustive dump
> sweep (fullspine computes `phraseTicks` but never emits them; the anchor dump is region-granular; nothing else is
> phrase-related).

## Ruling: Option 1 — add the gate-safe fullspine dump emission

1. **Authorized scope extension:** ONE additive emission in `tools/batch_analyze.cpp` — the `--dump-fullspine`
   payload gains a top-level `phraseBoundaryTicks:[…]` (the already-computed `eb::phraseBoundaryTicks` picked set,
   verbatim ticks). `batch_analyze` is tools/, not `src/`; the standard `.ours.json` writeJson path stays
   byte-identical; the flag is default-OFF. **Third commit** (`feat(tools): emit phraseBoundaryTicks in
   --dump-fullspine`), one change-class, fine.
2. **Proof unchanged:** the gate reproduction (53/24/53 exact) + suites after the C++ rebuild — the same additivity
   proof discipline as Task 1. Any movement = STOP.
3. Then **Tasks 2 + 3 proceed in full** (both metrics + the measurement), per the original instruction.

## Findings accepted

- **Finding 1 (rest-row `phraseend` = 10.7%):** your dedicated every-row `parse_cadence_phrase_markers()` extractor
  is the right call — ratified (an 11% silent GT drop would have been a measurement defect).
- **Finding 2 (sparse L5 cadence firing on the dev beds → near-zero recall expected):** understood and expected —
  Task 3 is the honest descriptive baseline of the existing dormant detector, no target, no tuning. Report the
  numbers as they are; the failure exemplars are the valuable output (they feed the L6-build design record and the
  later calibration).

All other terms of the instruction unchanged (dev beds only; zero-cadence corpora auto-skip; no θ; report HELD).
