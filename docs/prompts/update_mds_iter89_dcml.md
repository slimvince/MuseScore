# CC Instruction — Update STATUS.md, COWORK_HANDOFF.md, check ARCHITECTURE.md

## Read first (every session)

`C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\build_and_test.md`

**Current state:** Branch `master`.
HEAD is `eefa412b6f` — DCML time-overlap comparator commit (tools/compare_analyses.py +
tools/rerun_dcml_comparison.py). Prior HEAD was `2085f11322` (Iter 89 — pc=8 TPC sharp-honor fix).
Baselines: 407/407 composing, 50/52 notation (2 pre-existing Corelli failures — do not regress),
pipeline_snapshot 11 passed / 1 skipped, BIR=true=4, BIR=false=118, Jazz BIR=false=7.

---

## Task: update three markdown files

This is a documentation-only task. Do NOT touch any .cpp files, do NOT build, do NOT run
tests. Only edit .md files. No stopping for confirmation — make all edits in sequence.

---

## Step 1 — Update STATUS.md "Current State" section

Read STATUS.md (the full "Current State" section, lines ~9–60 approx). Replace it entirely
with the text below. The giant header prose block (lines 1–5, covering Iters 84–89 and back)
stays untouched — only replace the "## Current State (summary)" section that follows the
`---` separator.

**Replacement text for "## Current State (summary)" section:**

```
## Current State (summary)

**Last committed:** `eefa412b6f` — DCML time-overlap comparator
(tools/compare_analyses.py + tools/rerun_dcml_comparison.py).

**Prior commits in this cycle (all on master):**
- `2085f11322` Iter 89 — honor sharp TPC for pc=8 (G#/Ab) across flat and mildly-sharp keys
- `bea00f3482` Iter 88 — honor sharp TPC for pc=6 (F#/Gb) in flat keys
- `2dd2f35c17` Iter 87 — bass-b7 post-merge re-stamp (fixes analyzeScore merge discarding
  MinorSeventh extension); companion Iter 86 stamp inside analyzeChord retained
- `4da8252c9e` Iter 84 — R4 narrow G# leading-tone fix at keyFifths=1 (A melodic minor)

**Test baseline (as of Iter 89 / eefa412b6f — no code changes in comparator commit):**
- Composing tests: 407/407 passing
- Notation tests: 50/52 passing (2 pre-existing Corelli implode failures remain —
  `CorelliOp01n08dOpeningAndSparseLateBeats`, `CorelliOp01n08dUserReportedChordTrackAudit`)
- Pipeline snapshot tests: 11 passed / 1 skipped (`PipelineDivergenceCObservation.GenerateReport`
  — intentional opt-in, not a failure)
- Chord mismatch report: 4 RealDiff (pinned baseline), 127 ConventionDiff (Jazz catalog)

**BIR baselines (Baroque preset, batch path, unchanged since Iter 82):**
- BIR=true=4, BIR=false=118
- Jazz BIR=false=7 (Jazz BIR=true=63)

**Iter 90 — shelved (no commit):**
Bass-as-root promotion for 122 wrong-root cases. Characterization showed 84% of BIR=false=118
are iii/III triad confusion ({C,E,G} = C major vs Em/C) — non-local ambiguity that cannot be
resolved with a local gate. Variant A (+12 errors) and Variant B (+22 errors) both regressed.
Design note at `docs/iter90_bass_as_root_promotion_shelved.md`. Paths for future Iter 91:
(a) bridge-level adjacent-context pass using nextRootPc/previousRootPc, or (b) temporal-context-
gated promotion using existing ChordTemporalExtensions fields.

**DCML ground-truth comparison — current figures (post-eefa412b6f):**

PRIMARY metric: DCML-anchored time-overlap comparator (lenient-OR-50% overlap threshold).
Old beat-snap comparator was biased +21pp because it only scored the ~35% of regions that
happened to land near a DCML annotation boundary. Time-overlap scores ALL emitted regions
against their overlapping DCML annotation span.

Cross-corpus weighted root agreement (10 non-Bach corpora):
  **47.8%** (time-overlap, honest) — was 69.1% (beat-snap, biased)

Bach chorales (352 chorales, run via run_validation.py):
  **64.9%** overall root agreement
  **87.2%** chord-identity agreement on aligned regions
  **100%** region alignment (was 73% with old beat-snap; drop was a measurement artifact
  from sub-beat boundaries from Iters 72/73/83 not matching music21's beat-anchored positions)

Per-corpus DCML-anchored (time-overlap):
  Chopin       65.6%
  Dvorak       57.5%
  Grieg        53.0%
  Beethoven    49.2%
  Tchaikovsky  46.0%
  Schumann     43.6%
  Mozart       40.2%
  Corelli      39.6%
  Bach suites  37.7%
  C.P.E. Bach  0 regions (pre-existing issue — batch_analyze produces 0 output for all 66 mvts)

Reports at `tools/reports/` (most recent run: post-eefa412b6f).

**Queued / open:**
- Iter 91: bass-as-root promotion via bridge-level adjacent-context (see design note)
- C.P.E. Bach 0-regions: pre-existing, undiagnosed
- Sub-beat boundary cleanup: Iters 72/73/83 introduced sub-beat boundaries that don't align
  with music21's beat-anchored DCML comparison; harmless to accuracy but creates alignment
  measurement noise
- STATUS.md header prose is intentionally long (full audit trail); do not shorten it
```

---

## Step 2 — Update COWORK_HANDOFF.md

Read the full COWORK_HANDOFF.md. Make the following targeted edits:

### 2a. Replace the "Current state" section

Find the block starting `## Current state (as of 2026-05-14, updated after Iter 84 commit)`
and replace it with:

```
## Current state (as of 2026-05-15, updated after Iter 89 + DCML comparator commit)

- **HEAD:** `eefa412b6f` on master (DCML time-overlap comparator —
  tools/compare_analyses.py + tools/rerun_dcml_comparison.py)
- **Prior HEAD in cycle:** `2085f11322` (Iter 89 — pc=8 G#/Ab TPC sharp-honor fix)
- **Working tree (uncommitted):**
  - Doc drift only after this update (`ARCHITECTURE.md`, `CLAUDE.md`, `STATUS.md`,
    `COWORK_HANDOFF.md`) — leave alone unless explicitly asked
- **Composing tests:** 407/407 passing
- **Notation tests:** 50/52 passing (2 pre-existing Corelli failures remain — do NOT regress:
  `CorelliOp01n08dOpeningAndSparseLateBeats`, `CorelliOp01n08dUserReportedChordTrackAudit`)
- **Pipeline snapshot tests:** 11 passed / 1 skipped (skip = `PipelineDivergenceCObservation.
  GenerateReport`, intentional opt-in)
- **BIR baselines:** BIR=true=4, BIR=false=118, Jazz BIR=false=7 (unchanged since Iter 82)
- **Chord mismatch report:** 4 RealDiff (pinned), 127 ConventionDiff (Jazz)
```

### 2b. Replace the "Standing rule — CC instruction preamble" section

Find the block containing `**Current state:** Branch \`master\`, HEAD \`4da8252c9e\``
and replace just that one line (keep the surrounding boilerplate) with:

```
> **Current state:** Branch `master`, HEAD `eefa412b6f` (DCML time-overlap comparator;
> prior: Iter 89 pc=8 G#/Ab fix at `2085f11322`).
> Baselines: 407/407 composing, 50/52 notation (2 pre-existing Corelli failures — do not
> regress), pipeline_snapshot 11 passed / 1 skipped, BIR=true=4, BIR=false=118, Jazz BIR=false=7.
```

### 2c. Add an "Iters 85–89 + comparator" section

Insert the following block immediately before the `## Standing rule — CC instruction preamble`
section:

```
## Iters 85–89 + DCML comparator — all committed

- **Iter 87** (`2dd2f35c17`) — bass-b7 post-merge re-stamp in batch_analyze.cpp
  (`analyzeScore` merge discarded MinorSeventh extension stamped by Iter 86; post-filtered
  re-stamp pass at batch_analyze.cpp:1846–1880 fixes 281 of 293 b7-bass slash-chord cases)
- **Iter 88** (`bea00f3482`) — honor sharp F# TPC for pc=6 in flat keys (extends
  TPC-disambiguation block to fire at `keyFifths<0 && pc==6`; Gb→F# in D/F# and similar
  contexts)
- **Iter 89** (`2085f11322`) — honor sharp G# TPC for pc=8 across flat and mildly-sharp
  keys (removed pc=8 from Iter 78 flattening block; added `keyFifths<0 && pc==8` and
  `keyFifths==2 && pc==8` to TPC-honor block; survey script `tools/survey_pc8_flat_authored_bass.py`)
- **DCML comparator** (`eefa412b6f`) — new time-overlap comparator in compare_analyses.py
  (mode='time-overlap', lenient-OR-50% overlap threshold) + rerun_dcml_comparison.py
  re-aggregation driver. Old beat-snap 69.1% figure retired (biased +21pp). New primary
  metric: 47.8% weighted root agreement across 10 non-Bach corpora (DCML-anchored).
  Bach chorales: 64.9% overall, 87.2% chord-identity, 100% alignment.

**Iter 90 — shelved (no commit):**
122 wrong-root cases characterized (tools/analyze_wrong_root_iter90.py,
tools/iter90_wrong_root_characterization.txt). 84% are iii/III triad confusion — non-local
ambiguity. Both Variant A (+12 errors) and Variant B (+22 errors) regressed. Design note:
`docs/iter90_bass_as_root_promotion_shelved.md`. Future path: Iter 91, bridge-level
adjacent-context pass using nextRootPc/previousRootPc from ChordTemporalExtensions.
```

---

## Step 3 — Check ARCHITECTURE.md

Read ARCHITECTURE.md around these two topics and add brief notes only if no equivalent note
already exists:

**Topic A — iii/III disambiguation is non-local:**
Search for any section covering chord ambiguity, inversion gates, or the composing module's
known limitations. If there is a "Known limitations" or "Design decisions" section, add a
brief note: "iii/III triad confusion ({C,E,G} = C major vs Em/C) is non-local — cannot be
resolved with a local gate in chordanalyzer.cpp. Fix belongs in a bridge-level adjacent-context
pass (see docs/iter90_bass_as_root_promotion_shelved.md for characterization and Iter 91 design)."
If no appropriate section exists, skip (do not create a new top-level section for this alone).

**Topic B — sub-beat boundaries and DCML alignment:**
Search for any section on segmentation, boundary detection, or batch_analyze. If there is a
note about greedy-expand or the batch segmenter, add: "Sub-beat boundaries from Iters 72/73/83
(note-end tick collection, head/tail-gap synthesis) do not align with music21's beat-anchored
DCML annotation positions. This creates alignment measurement noise but does not affect chord
accuracy. The time-overlap comparator (tools/compare_analyses.py, mode='time-overlap') handles
this correctly via lenient-OR-50% overlap threshold."
If no appropriate section exists, skip.

Do NOT add sections to ARCHITECTURE.md that aren't warranted by existing structure.

---

## Step 4 — Verify

After all edits:
1. Read the STATUS.md "Current State" section and confirm the replacement landed correctly.
2. Read COWORK_HANDOFF.md "Current state" section and the preamble to confirm updates.
3. Report what was changed in each file (or skipped for ARCHITECTURE.md if no appropriate
   section existed).

Do NOT commit. Do NOT run any builds or tests.
