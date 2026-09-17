# E0 addendum — carry-cap disposition (Cowork ruling on the 2026-07-02 checkpoint)

> Addendum to `cc_instruction_e0_fullspine_measure.md`. Your STOP was correct and per instruction. **Ruling:
> PROCEED — build the full harness, faithful `extensions=0`, byte-identity-prove + commit, run ALL 3 presets** —
> with the riders below. The carry gap is itself an E0 *finding* (the gap-analysis Rider-2 class), not a blocker:
> E0 measures what exists. The carry FIX (extending the L4→L5 carry) is a Cowork-owned design change, ratified
> separately after your report + the gap-analysis; do NOT implement it this run.

## Riders (binding)

1. **Measure #1 (RN accuracy) is reported at THREE levels, clearly separated:**
   - **Root-level** (root pc + bass/inversion) — uncapped, a primary verdict measure.
   - **Triad-normalized RN** — BOTH sides (the chain's RN and the legacy RN, and the DCML reference) normalized to
     triad-level (sevenths/extensions stripped) before comparison — this is the FAIR capped comparison; a primary
     verdict measure. Raw full-RN vs an unstripped opponent is NOT fair (legacy emits `V7`; the capped chain cannot)
     — do not present it as a verdict.
   - **Raw full-RN** — diagnostic only, explicitly labeled "carry-capped, artifact class: seventh/extension drop";
     included so the cap's size is quantified (it sizes the value of the carry fix), never as a better/worse verdict.
2. **Measure #7 (relational labels):** report which labels structurally cannot fire on this substrate (`V7/x`,
   `Ger+6`) and score only the firable set (`viio/x`, Neapolitan, modal mixture) as measures; count the non-firable
   set's DCML occurrences (that count = the second component of the cap's size).
3. **All other measures (#2–#6, #8, #9) unchanged** — uncapped per your own analysis; the override-duty headline
   (#6) remains the marquee deliverable.
4. **Report additions for Cowork verification:** quote `git rev-parse HEAD` at build time; quote verbatim (with
   file:line) the three carry-claims — the projection drop site (`chordslicedecoder.cpp` ~:443), the
   `functioncadence.h` seventh-not-on-projection comment, and the `formatRomanNumeral` extensions-read
   (`chordsymbolformatter.cpp` ~:862–946) — Cowork verifies them against the committed objects before ratifying any
   carry-fix design.
5. **§4 of your report (regression classes NAMED) gains a mandatory first entry:** the carry gap itself —
   fields dropped, where, the two candidate fix shapes (carry `extensions`+`naturalFifthPresent` on the
   carry struct verbatim vs a per-voice-note channel like the cadence detector's), and any OTHER field the
   projection drops that any L5 §5 rule could ever want (sweep the projection site once, completely — one list,
   so the carry fix is designed against the full inventory, not discovered twice).
6. **Do NOT synthesize, default, or reconstruct** the seventh anywhere (unchanged STOP rule) — `extensions=0`
   faithful throughout.

## What happens after your report

Cowork verifies riders 4–5 at source → ratifies the carry-fix design (expected shape: carry the fields; the
per-voice-note channel was a cadence-specific workaround, not the general contract) → a separate small dormant
increment implements it → **E0′**: re-run ONLY the capped measures (#1 full-RN level, #7 full set) on the fixed
carry. The harness you build now is unchanged by that fix — build once, re-run cheap.
