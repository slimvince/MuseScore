# CC Instruction — Engage arc #12: Stage-3 owed MEASUREMENTS — does the joint step actually pay? (read-only)

> **ACTIVE DISPATCH (Cowork, 2026-07-07).** Stage 3 opens **measurement-only** (user directive). Before
> building anything, settle the facts the joint-step design deliberately left unmeasured — above all the
> decisive one: **does re-deciding the chord under alternative keys measurably improve root-correctness, or
> not?** This is the #1/#3/#5 guard that stops us building another plausible-but-unhelpful mechanism the way
> the fine-grain override was built on an unmeasured assumption.
>
> **READ-ONLY. No production behavior change, no build of the joint step, no fit/tune.** The measurement
> instrument may be a `tools/` harness or a default-OFF dump (byte-identical production; both stops trivially
> green). It **exercises the EXISTING `ChordSliceDecoder` as a pure re-decode function** — the "faithful
> mechanism" the joint-step design names — under L3's already-carried key alternatives. That is a measurement
> probe, **not** the production joint step (no beam driver, no wiring, no behavior change).
>
> **Build on established fact (#1). Read first:**
> - `cowork_joint_key_chord_design.md` (the mechanism + the six owed measurements) + `cc_engage_c3_measurement_report.md`
>   (why this was un-computable as *production telemetry* — a standalone probe over the pure decoder is a
>   different thing and IS computable).
> - The decoder as a pure fn of `(slices, key)` (`chord/chordslicedecoder.cpp`); L3's carried
>   `HarmonicRegion.keyAlternatives` + `keyConfidence`.
> - The A-8 / robust-metric method (`tools/compare_rn.py`, `dcml_parser.py`) — root-agreement vs the DCML
>   ground truth (the benefit is measured the same way the stop is).
> - The pedal design's owed-P1 (`cowork_layer5_engagement_design.md` §6).
>
> **Current state:** HEAD `fa0a881aa4`, branch `master`, fork-only, ahead 0. Both stops green. Corpus
> `c50002fee1` (#9, pinned). **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`. **Do
> NOT bash to read files.** Build (if a probe field is added) via the standard PowerShell Start-Process.

---

## Task 1 — the probe (read-only; exercise the pure decoder under alternative keys)
Per slice (focus the coupled minority — key uncertain: `keyConfidence` below its bar), re-decode the chord
under **each** carried alternative key via the existing `ChordSliceDecoder` (a pure fn — no production
mutation). Choose the cheapest route (a `tools/` harness over the frozen corpus, or a default-OFF dump);
**production `.ours.json` byte-identical.** Ground the decoder's pure-fn signature at the code.

## Task 2 — the DECISIVE facts (measure vs the DCML ground truth, stamped #16)
On corpus `c50002fee1` ×3 presets:
- **★ The benefit (the one that decides the build):** on slices where the chord's root **flips** under an
  alternative carried key, does the flipped reading agree **better** with the DCML root than the current
  key-then-chord reading? Report **corrections / harms / neutral** (the same net-corr−harm framing that
  exposed the F-B override). **This is the go/no-go on building the joint step.**
- **The fire-rate:** how often the chord flips (different root) under a carried alternative key — the true C3
  fire-rate / per-key flip-rate (vs the ~13.5% coupled-minority the key-axis measured, and the ~25%
  ≥3rd-root fan-out).
- **Beam width:** the distribution of carried-key-alternative counts a beam would traverse.
- Any of the design's six owed measurements that are read-only-now; flag those that genuinely need the build.

## Task 3 — the pedal owed-P1 (secondary, read-only)
Measure whether the pedal *reader-over-carry* (reading the carry's distinct-root margin) agrees with the
current in-place pedal detection — the design's owed-P1 agreement check.

## Task 4 — report + fold + push
1. **Report** `cc_engage_stage3_joint_measure_report.md` (force-add): the probe route, **the benefit
   corr/harm/neutral (the go/no-go)**, fire-rate, beam width, the pedal-P1 agreement, which owed measurements
   remain build-gated, all SHAs. Stamp corpus-hash + instrument-commit (#16).
2. If a probe field was added: its `feat` is a separate revertible commit (#14), with the **production
   byte-identity proof** (default `.ours.json` 0-diff 352×3; both stops green; no golden refresh).
3. **Fold** (`docs(cowork):`): report · `STATUS.md` · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`
   (engage observation) · this instruction (force-add).
4. **Push fork-only** — never toward `upstream`/`musescore/MuseScore` (`cfc7eb5e39` HARD STOP).

## STOP conditions
- Any production behavior change; any build of the joint step into production (beam driver / wiring); any
  fit/tune of a constant. This is measurement only.
- Any move on the default `.ours.json` path (a probe must be default-OFF / a scratch harness).
- Any benefit/fire-rate figure not measured against the DCML ground truth on the pinned corpus (#1/#9) — no
  proxy, no assumption.
- Any push toward `upstream`/`musescore/MuseScore`.

## Acceptance
The probe exercises the existing decoder as a pure re-decode under carried keys, production byte-identical ✓ ·
**the benefit measured as corr/harm/neutral vs DCML — the joint-step go/no-go — reported ×3 presets** ✓ ·
fire-rate + beam-width + the read-only-now owed measurements reported; build-gated ones flagged ✓ · the
pedal-P1 agreement measured ✓ · report + fold, stamped, with SHAs ✓ · no production change / no build / no
fit; both stops green; pushed fork-only ✓.

*Cowork, 2026-07-07. Engage arc #12 — Stage-3 opens measurement-first: measure whether the joint step pays
before building it (#1/#3/#5). On CC's report: Cowork brings you the go/no-go + the sizing numbers → the
build decision is yours, on measured fact.*
