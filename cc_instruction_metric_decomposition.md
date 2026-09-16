# CC Instruction — DECOMPOSE the per-event charged-error set: key-driven vs chord/segmentation-driven — READ-ONLY

> Round 3 (`cc_metric_round3_report.md`, Cowork-reconciled) validated the fine-grained per-event oracle-root
> metric and revealed the **true root-error rate is ~21% per-event (≈10× the batch ~2%)** — the batch gate was
> hiding the bulk. **Before building the standing tool or committing K1 effort, that 10× must be ATTRIBUTED.**
> Round 3 attributed it to "region over-grab" (a segmentation cause), but that is one hypothesis; the other is
> **key-span propagation** (a wrong key over a long span charges *every* event in it — also a ~10× multiplier).
> These are different architectural layers (segmentation vs key) and decide the inference priority (the
> re-assessment's K1-first hypothesis vs a segmentation pivot). **READ-ONLY: no build, no committed tool, no
> production/gate/scoring/threshold change.** Use the per-event data already on disk (`tools/cc_round3_out.json`
> + the per-preset corpora + `dcml_parser`). North star: best = CORRECT vs the DCML/music21 oracle.

## §1 — The decomposition (the one cut that matters)
For **each charged event** (the `music21_dcml_agree` set from round 3, per preset — Baroque HEAD =
`baroque_kma_abs`, Jazz, Default), classify it into exactly one bucket by comparing OUR key to the ORACLE key at
that event's tick:

1. **KEY-DRIVEN** — our **key** (tonic+mode) ≠ the oracle key (DCML local key, music21-corroborated) at that
   event. The root is wrong *because the key is wrong*; the chord-relative reading may even be right. → the
   **key axis (K1/K3)** owns it.
2. **CHORD/SEGMENTATION-DRIVEN** — our key **matches** the oracle key, but our root still ≠ the oracle root. Then
   sub-split if cleanly possible:
   - **OVER-GRAB** — our region spans the event but the oracle asserts a *different* root at this event than at
     our region's dominant tick (i.e. our single region covers ≥2 oracle roots). → the **segmentation** layer.
   - **CHORD-ID** — our region aligns 1:1 with the oracle event but we still pick the wrong root (e.g. a genuine
     vertical/competition miss). → the **chord** layer.

Report the **per-preset counts and percentages** for KEY-DRIVEN vs CHORD/SEGMENTATION-DRIVEN (and the
over-grab/chord-ID sub-split where determinable). This is the deliverable.

## §2 — Method notes (reuse, read-only)
- Our key per event: from `.ours.json` region `keyModeResult` covering the tick. Oracle key: DCML local key
  (`dcml_parser` — the key the RN is measured in), music21 key as corroboration. Compare tonic-pc + mode.
- "Over-grab" test: does the oracle assert ≥2 distinct roots within the tick-span of our single region covering
  this event? (Reuse the round-3 event grid; you already have per-event oracle roots.)
- Keep it pitch-class typed where possible (key tonic-pc, root-pc) — normalizer-immune, same as round 3.
- If a charged event cannot be cleanly bucketed (e.g. key partially overlaps, or the oracle key itself is
  disputed), put it in an explicit **AMBIGUOUS** bucket and report its size — do not force it.

## §3 — The question this answers (state the verdict)
- If **KEY-DRIVEN dominates** → the ~10× is key-span propagation; it **confirms K1 as the #1 lever** and shows
  its true impact is ~10× the batch number. The re-assessment's plan stands, sharpened.
- If **OVER-GRAB dominates** → segmentation under-grab/over-grab is a larger lever than the re-assessment
  assumed; flag a re-prioritization (segmentation before/alongside K1).
- If **CHORD-ID dominates** → the chord axis is less "near-ceiling" than concluded; flag.
- Most likely a mix — **report the split and name which layer owns the plurality**, with the per-preset numbers.

## §4 — Deliver
`cc_metric_decomposition_report.md`: the per-preset KEY-DRIVEN / CHORD-SEGMENTATION (over-grab / chord-ID) /
AMBIGUOUS counts + percentages, the method, a handful of worked example events per bucket (stem@tick, our
key+root vs oracle key+root), and the verdict on which layer owns the plurality of the ~21% per-event error.
**READ-ONLY — HEAD `dd418ecfed`; no build, no committed tool, no production/gate/scoring/threshold change.**
Cowork reconciles; user ratifies the priority before the standing `--oracle-root` tool is built and before K1
work begins.

## §5 — Stop conditions
- The per-event key comparison needs data not in `.ours.json`/the corpora (a build) → STOP, describe the minimal
  read needed, do not build.
- A large share lands in AMBIGUOUS (can't bucket) → report it honestly; do not force a verdict that the data
  doesn't support.
- Any temptation to commit a tool / change a threshold / touch scoring → STOP (post-ratify build step).
