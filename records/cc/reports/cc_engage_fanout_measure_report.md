# CC Report — Engage arc #8: the TRUE untruncated Layer-5 fan-out, measured read-only

**Dispatch:** `cc_instruction_engage_fanout_measure.md` (Cowork, 2026-07-07).
**Instrument commit (feat):** the `--dump-fanout` read-only field (see §5 for SHAs).
**Docs fold commit:** this report + STATUS/HANDOFF/plan (see §5).
**HEAD at measurement:** `b5857ed2f3`, branch `master`, fork-only.
**Corpus:** `c50002fee1` (the pinned corpus — 352 source `.xml`, all three preset manifests stamp
`git_hash=c50002fee1`). Measured at HEAD `b5857ed2f3`, whose default `.ours.json` is **byte-identical to
`c50002fee1`** (proven §4), so the fan-out measured at HEAD == the fan-out at the pinned corpus.
**Machine-readable data:** `cc_engage_fanout_measure_data.json`. **Instrument:** `tools/measure_fanout.py`.

---

## 0. TL;DR

The structural audit (§1.5) measured only the **capped floor** — what survives applyHarmonicFunction()'s
**cap-of-3** into `results[]`/`.ours.json` (the ~36 % Baroque/Default, 21.5 % Jazz append-fire rate). This
measures the **uncapped above-threshold ranked set** the cap truncates — `gateCtx->rawCandidates` filtered by
`gateCtx->threshold`, captured with the **real production temporal context**.

- **The true above-threshold fan-out is ~2× the capped floor:** median **5** readings (Baroque/Default), **4**
  (Jazz); mean **6.35 / 6.15 / 6.32**; a long tail to **p99 ≈ 23–27, max ≈ 46–49**.
- **The cap-of-3 bites on ~80 % of slices:** `>3` above-threshold readings on **79.5 % / 75.4 % / 79.3 %** of
  competition slices — i.e. on 4 of 5 slices the cap discards ≥1 above-threshold reading.
- **But the readings collapse to a SMALL distinct-root set:** distinct **roots** above threshold — median **2**
  (Baroque/Default), **1** (Jazz); mean **2.13 / 1.73 / 2.12**. The large reading count is mostly
  template/voicing variants of the same ~2 roots (the decoder scores all 12 roots × 17 templates = **204**
  cells per bass; the "total" fan-out is that structural constant, so the meaningful fan-out is strictly the
  above-threshold subset).
- **The load-bearing exclusion tail (#12):** a **3rd-or-more distinct root** clears threshold on **25.1 % /
  16.1 % / 24.9 %** of slices — roots the current cap-of-3 + single diff-root append (which surfaces at most
  winner + 1 alternate root) **cannot represent**. That is the tail Layer-5 selection needs the uncapped set
  to see.

---

## 1. Route (Task 1) — the chosen path, grounded at the source

**Chosen: a single minimal additive default-OFF dump field.** No no-`src` route is faithful; proof below.

### 1.1 Why the existing read-only path (`diagnoseChord`) is NOT faithful
`diagnoseChord` already reads `gateCtx.rawCandidates` into `diag.competition`
(`chorddiagnose.cpp:106`), and `batch_analyze --diagnose-measures` already dumps it
(`batch_analyze.cpp:1800`). **But that path passes a NULL temporal context**
(`batch_analyze.cpp:1689`, `diagContext = nullptr`) — the region-in-isolation view. The production
`rawCandidates` are scored **with** the real inter-region signals (rcb / resolution / wDim / wSeq / step),
which change (a) which bass group wins → the candidate set, and (b) `gateCtx.threshold` → the above-threshold
cut. `diagnoseChord` also never emits the threshold. So `--diagnose-measures` would measure a different
distribution than the one Layer 5 selects over — a #1/#3 violation to report as "the true fan-out." Rejected.

### 1.2 Why `--dump-fullspine` cannot carry it
`runFullSpine` runs its **own** `ChordSliceDecoder::decode` (`batch_analyze.cpp:3045`) — a different layer than
the production `applyHarmonicFunction` competition. It has no `gateCtx.rawCandidates`. Reusing it would measure
the wrong substrate. Rejected (so the "reuse fullspine" preference does not apply — different decoder).

### 1.3 The faithful capture site
The production above-threshold set lives in `gateCtx` at the **region commit sites** in `regionanalyzer.cpp`
(`analyzeChord(... &gateCtx)` at :988 / :1384), where the real temporal context is already threaded. That is
where `makeChordPathNode` already derives `winnerScore`/`winnerMargin` from `gateCtx.rawCandidates`. So the
fan-out summary is captured there, from the same `gateCtx` — a faithful, in-context view.

---

## 2. The additive field (minimal, default-OFF)

A read-only summary struct + pure helper (no scoring, no re-decision — a faithful count of the reading set the
pipeline already produced):

- `analysis::RawFanoutSummary { total, aboveThreshold, distinctRootsTotal, distinctRootsAbove }` and
  `computeRawFanoutSummary(const PostScoringGateContext&)` — `chordanalyzer.h` (after the full
  `PostScoringGateContext` definition, beside the existing inline predecessor-score derivation). `total =
  rawCandidates.size()`; `aboveThreshold` = candidates with `score >= gateCtx.threshold` (the `results[]`
  admission test, `harmonicfunctionlayer.cpp:524`); `distinctRoots*` = distinct `rootPc` (all / above).
- `HarmonicRegion::fanout` — `harmonicrhythm.h`, **IN-MEMORY ONLY**, following the established
  `keyAlternatives`/`keyConfidence` "deliberately not serialized, additive plumbing of already-computed data"
  idiom (no production serializer reads it).
- Populated at the three competition build sites (`regionanalyzer.cpp` Pass-1 :1054, Pass-2 :1250, Pass-2b
  :1442) via `computeRawFanoutSummary(gateCtx/subGateCtx)`. Inherited / gap / fallback regions (no fresh
  competition) keep the default `total=0` and are excluded from the distribution.
- `AnalyzedRegion::fanout` + `--dump-fanout` — `tools/batch_analyze.cpp`, mirroring the
  `--dump-region-keymargin` diagnostic exactly: runs the BATCH region path (`sectionLevel=false`, how the
  frozen gate corpus was produced) and returns **before** `writeJson`, so the standard `.ours.json` is
  byte-identical by construction.

---

## 3. The distribution (Task 2), stamped

Corpus `c50002fee1` × 3 presets, HEAD `b5857ed2f3`. Per-slice unit = one BATCH committed region that ran a
fresh competition (`fanoutTotal > 0`). Every score processed, 0 failures.

| Metric (above-threshold ranked set) | Baroque | Jazz | Default |
|---|---|---|---|
| competition slices | 11 205 | 10 849 | 11 194 |
| min | 1 | 2 | 1 |
| **median** | **5** | **4** | **5** |
| mean | 6.35 | 6.15 | 6.32 |
| p90 | 11 | 12 | 11 |
| p99 | 27 | 23 | 27 |
| max | 49 | 46 | 49 |

**Above-threshold histogram** (readings clearing `threshold`; `>12` = tail bucket):

| count | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | >12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baroque | 2 | 215 | 2075 | 2543 | 2178 | 1041 | 525 | 341 | 617 | 462 | 183 | 99 | 924 |
| Jazz | — | 163 | 2511 | 2824 | 1701 | 766 | 546 | 616 | 173 | 122 | 227 | 129 | 1071 |
| Default | 2 | 224 | 2087 | 2547 | 2174 | 1035 | 524 | 337 | 625 | 468 | 184 | 98 | 889 |

**Truncation impact — fraction of competition slices where the cap-of-3 discards above-threshold readings**
(`aboveThreshold > k`):

| | > 2 | > 3 | > 5 | > 10 |
|---|---|---|---|---|
| Baroque | 98.1 % (10 988) | **79.5 % (8 913)** | 37.4 % (4 192) | 10.8 % (1 206) |
| Jazz | 98.5 % (10 686) | **75.4 % (8 175)** | 33.6 % (3 650) | 13.2 % (1 427) |
| Default | 98.0 % (10 968) | **79.3 % (8 881)** | 37.2 % (4 160) | 10.5 % (1 171) |

**Distinct-root vs distinct-voicing (the decoder dedups voicings; each reading = one voicing).** `aboveThreshold`
above IS the distinct-**voicing** (reading) count; the distinct-**root** count is far smaller:

| distinct roots above threshold | Baroque | Jazz | Default |
|---|---|---|---|
| mean | 2.13 | 1.73 | 2.12 |
| median | 2 | 1 | 2 |
| p90 | 4 | 3 | 4 |
| max | 11 | 9 | 11 |
| slices with > 1 distinct root | 68.8 % | 46.7 % | 68.6 % |
| **slices with ≥ 3 distinct roots** | **25.1 %** | **16.1 %** | **24.9 %** |

Distinct-root-above histogram (`>6` = tail):

| roots | 1 | 2 | 3 | 4 | 5 | 6 | >6 |
|---|---|---|---|---|---|---|---|
| Baroque | 3494 | 4898 | 1422 | 966 | 293 | 56 | 76 |
| Jazz | 5783 | 3321 | 951 | 612 | 107 | 42 | 33 |
| Default | 3512 | 4892 | 1430 | 939 | 285 | 58 | 78 |

**Total fan-out is a structural constant:** `fanoutTotal` = 204 on every slice/preset (12 roots × 17
`kTemplateCount` templates — the oracle scores the entire grid for the winning bass). So `total` is
uninformative as "fan-out"; the meaningful ranked set is exactly the above-threshold subset (~3.1 % of the
grid).

---

## 4. Byte-identity proof + both stops green

Full-corpus regeneration with the new binary, **default flags (no `--dump-fanout`)**, diffed against the frozen
`c50002fee1` corpus:

```
Baroque: compared=352 differing=0
Jazz:    compared=352 differing=0
Default: compared=352 differing=0   → 1056/1056 .ours.json byte-identical
```

The new fields are read by **no** production serializer (only `writeFanoutJson` under the default-OFF flag) and
`--dump-fanout` returns before `writeJson`; the empirical 1056/1056 zero-diff confirms it. Because both
regression stops are computed from these identical `.ours.json`, **both are trivially green** (class-(b)
duration non-increase = +0/−0; characterise **52/24/52** unchanged) — no re-baseline. Suites: **composing
1101 / notation 53 (+skips) / pipeline_snapshot 11**, all pass, no golden refresh.

---

## 5. What this implies for the Layer-5 selection design (factual, not a design decision)

The distribution Layer 5 will select over is **wide in readings but narrow in roots**. The above-threshold set
is real and sizeable (median 5–6, tail to ~27–49), and the cap-of-3 hides part of it on ~80 % of slices — but
~⅔ of those hidden readings are template/voicing variants of the same ~2 roots the winner+append already
surface. **The load-bearing exclusion tail is the ≥3rd distinct root: on ~25 % (Baroque/Default) / ~16 %
(Jazz) of slices a genuinely-different third-or-more root clears threshold, and neither the cap-of-3 nor the
single diff-root append can carry it** — that is precisely where the uncapped `rawCandidates` (#12, finding-by-
exclusion) is load-bearing for Layer-5 selection, and where the capped-floor view undercounts the ambiguity.
Jazz's narrower root set (median 1 root, 46.7 % multi-root) tracks its suppressed inversion bonuses.

*(Observation only, per the moratorium — no inference-problem coding, no design decision. Numbers for Stage 2.)*

---

## 6. SHAs / reproduce

- Instrument (feat, revertible #14): `0361e55e4a` — `feat(composing): --dump-fanout read-only uncapped
  competition fan-out instrument`.
- Docs fold (`docs(cowork):`): this commit (report + STATUS + HANDOFF + plan + fitter-design + instruction).
- Reproduce: `python tools/measure_fanout.py --out <file>` (runs `batch_analyze --dump-fanout` over
  `tools/corpus/*.xml` × {Baroque,Jazz,Default}, parses per-region fan-out, aggregates). Byte-identity:
  `python tools/run_bach_preset.py --preset <P> --corpus-dir tools/corpus --output-dir <scratch>` then `cmp`
  vs `tools/corpus/<p>/*.ours.json`.

*Cowork, 2026-07-07. Arc #8 — the true fan-out measured read-only, on the pinned corpus, both stops green.
Cowork brings the numbers → Stage 2 (the Layer-5 engagement design) opens.*
