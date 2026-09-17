# CC instruction — the TSV-oracle infrastructure: cadence + phraseend parsing + the L6 validation metrics

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Also: `cowork_layer6_grouping_design.md` §10/§15-1 (the SIGNED spec this executes — signed 2026-07-02 incl. the
> Wave-1 oracle update), your own `cc_corpus_wave1_report.md` §4 (the inventory + proposal sketch — the design basis).
>
> **✅ RE-DISPATCHED (Cowork, 2026-07-02): the L6 gate is PASSED** — the bounded-context/extension build is ratified
> (`cc_extension_build_report.md` §6: §11 items 1–3 all PASS; commits `d39da15d95`…`30b23d9f5c` verified). The L6
> track un-parks with this instruction. **State updates for this run:** HEAD = your `git rev-parse HEAD`
> (post-extension-build tip `30b23d9f5c` or later); suites baseline composing **1015** / notation 53 / snapshots
> 11/11; gate 53/24/53 unchanged. The L1.5 boundary dump + the dormant L5 cadence path are unchanged by the
> extension build — the tasks below stand as written. (The L3-activation A/B remains HELD — separate user decision;
> irrelevant to this run.)
>
> **Dispatch state: ACTIVE (2026-07-02, on the L6 sign-off).** This is the §15-1 build prerequisite for L6
> validation — tools-only, gate-safe, TWO commits. No `src/` change. No θ, no tuning. Bash rules as always.
> Cite code by function/§ anchor, not raw line number (standing policy).

## Task 1 — parser extension (commit 1; additive, gate-safe)

Per your §4 sketch: `dcml_parser.py` gains optional `cadence` + `phraseend` fields on the region record, populated in
the harmonies-TSV read path from the existing columns. **Purely additive**: the RN/root/key read surface is untouched
— prove it by running the full metric test suite + one gate reproduction (`characterise_bir_false` → 53/24/53 exact)
after the change. `form` stays unread (chord-form, excluded per your §4 correction). Unit tests: a fixture TSV with
cadence labels (incl. an HC sub-type `HC.SIM`) + phraseend brackets parses to the expected fields; a TSV without the
columns parses exactly as before.

## Task 2 — the two validation metrics (commit 2; measurement tooling)

A new comparison tool (or `compare_rn`-adjacent module — declare the choice; reuse the existing tick-overlap aligner,
never a second one) computing, per corpus and aggregated:

1. **Punctuation-span-boundary precision/recall** — our boundary ticks (the L1.5 `phraseBoundaryTicks` picked set,
   read via the existing diagnostic dump path) vs the GT `phraseend` bracket ticks, boundary-tolerant (± one beat;
   the tolerance a declared constant, not tuned). Chorale fermata oracle as the secondary view (with the §11
   non-independence caveat printed); `bwv112.5` excluded from the fermata-recall denominator (the §15-4 ruling).
2. **Cadence-location precision/recall** — L5's detected cadences (the dormant `detectFunctionalCadences` via the
   existing `--dump-fullspine`/`--dump-l5` harness output) vs GT `cadence` rows, LOCATION-scoped per L6 §10 (type
   reported as a confusion matrix over {PAC, IAC, HC(+subtypes), DC, EC, PC} but explicitly NOT a gate — the
   type-attribution caveat printed).

Scope: **the dev beds only** (registry `split=dev`: the 10 pre-wave-1 + the 6 named — richest cadence beds
beethoven/mozart/corelli/cpe_bach among them); held-out untouched (E2 discipline). Zero-cadence corpora (the 12,
incl. wagner) auto-skip the cadence metric with a printed note.

## Task 3 — the first read-only measurement (no commit; report)

Run both metrics once on the dev beds. Report per corpus: boundary P/R, cadence-location P/R, the type confusion
matrix, and the top-5 failure exemplars each (stem@tick) for the L6-build design record. **This is a baseline
measurement of the EXISTING dormant detectors** — no constant moves in response to any number (the numbers inform the
L6 build + later calibration, nothing else).

## Deliverable + gate

`cc_tsv_oracle_report.md` (gitignored, HELD; end with line count): §1 parser extension + additivity proof; §2 the
metrics (method, tolerances, aligner reuse); §3 the measurement tables + exemplars; §4 Unknowns. Commits local,
unpushed, fork-only. Gate proof: suites green (metric tests + composing/notation/snapshots untouched-green), corpus
53/24/53 exact once at the end.

## Stop conditions

Anything forcing a change to the RN read surface of `dcml_parser` → STOP (additivity is the contract). A GT column
meaning ambiguity (a `cadence`/`phraseend` value outside the documented vocabulary) → record + skip, don't guess.
No tuning anywhere.

**On your report: Cowork re-reads this instruction, reads the report in full, verifies the parser additivity + the
commit shapes at committed objects before ratifying — then writes the L6 dormant-build instruction.**
