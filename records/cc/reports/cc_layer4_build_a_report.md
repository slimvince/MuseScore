# CC — Architectural Layer 4 (CHORD SYMBOL + NON-CHORD TONES) — Increment A build report

**Status:** BUILT, unit-tested, graded, committed **locally (UNPUSHED)**. The per-slice chord module + its tests + the
`--decode-chords` diagnostic + the grading/membership harness. **Production byte-identical** (the decoder is NOT wired
into the live analyzer; it runs only under the read-only `--decode-chords` diagnostic, which returns before
`analyzeScore`). `upstream` untouched.

**Spec:** `cowork_layer4_chordsymbol_design.md` (SIGNED). **Pre-build audit:** `cc_layer4_audit_dossier.md`. **Models
the build on:** the Layer-3 decoder increment (`keymodesequence` — same isolated-module + graded-against-held-out-GT
shape). This is **Increment A** only: it stands up the per-slice path + the grading so the genuinely-new parts
(membership, the spelling-pin, the new types) land on a measured baseline. Increments B/C are NOT in this commit.

---

## §1 — The per-slice path as built

New module `src/composing/analysis/chord/chordslicedecoder.{h,cpp}` (namespace `chordslice`), beside `chordanalyzer`.
For each Layer-2 slice (`changePointSlices(noteModel)`):

1. **Window — the indexed `weightedPcView`.** The slice's tone window is the slice span expanded by `contextSlices`
   neighbour slices on each side (default 1 — "the slice and its immediate neighbours"), built through the **indexed**
   engravingbridge view `weightedPcView` over `NoteModel::overlapping` — **never** a region aggregate or a DOM walk
   (audit §5/§6 STOP honored). A crude fixed stand-in for the design's adaptive lazy-extend window (Increment B); the
   window extent is a **setting**, not a constant.
2. **Score + surface the cube.** `RuleBasedChordAnalyzer::analyzeChord(window, key, …, &snapshot)` runs the **existing
   scorer**; the complete `(bass × root × template)` candidate cube — `fn::ScoringSnapshot::cells`, each with its
   vertical fit score — is surfaced via `snapshotOut`, exactly as the L3 decoder surfaced `analyzeKeyMode`'s
   252-candidate dump. No second scorer (§4a).
3. **Rank + select + carry.** Every cell is projected to a `ChordSliceCandidate` (root + quality + bass/inversion + tpc
   + the cell's vertical score `(basisIndep + basisDep)·cf·af + wComplete`). The list is ranked (score desc; tie-break
   tiePriority, then root, then bass — deterministic); the **chosen** chord is the top candidate; the **ranked
   alternatives** are the distinct chord voicings below it, capped at `topK`, **∪ the prevailing chord** (the previous
   slice's chosen — kept alive as a carried alternative when expressible, the L3 incumbent pattern).
4. **Confidence + uncertain.** `confidence` = the chosen cell's vertical score minus the best score over any
   **different `(root, quality)`** chord (an inversion of the same chord is not a competitor); a slice is `uncertain`
   when that margin is below `uncertaintyMargin`. **Membership sets are STUBBED EMPTY** (Increment B).

KEY is a feed-forward **prior** (the notated signature in the diagnostic; per-slice L3 feed-forward is the later wiring
step). `redecodeRange(first,last)` reproduces a full decode's slices exactly (the per-slice decision is context-free;
one slice of look-back recovers the first slice's prevailing).

**This increment does NOT** (verified, STOP conditions honored): decide per-note chord-tone-vs-NCT membership; pin the
symmetric (dim7/aug) root from spelling; add the diminished-seventh / minor-major **types**; or read extensions from
membership. No second chord scorer, no third window builder.

### Settings (effort-retrofit hygiene — `ChordSliceDecoderPreferences`)
`contextSlices` (1), `topK` (6), `uncertaintyMargin` (0.5, vertical-score units), `minDistinctPcs` (1 — the
greedy-expand sparse-anchor relaxation, decode-only on a prefs copy; production's 3 untouched). All seeds, swept later.
Exposed as decode-only CLI overrides `--chord-context-slices / --chord-topk / --chord-uncertain-margin / --chord-min-pcs`.

---

## §2 — Grading harness (the read-only diagnostic + both metrics)

- **`batch_analyze --decode-chords`** (default OFF, mirrors `--decode-keymode`): builds the note model, slices, runs
  the per-slice chord decoder, and emits per slice — root + quality + inversion + confidence + uncertain + the ranked
  alternatives, the **focal-slice sounding pitch classes**, and the (empty) membership split — in a region shape the
  chord-root graders read (`compare_analyses.load_analysis` → `Region.root_pc/quality/bass_is_root/…`). **Returns
  before `analyzeScore`** ⇒ production untouched.
- **Driver** `tools/decode_chord_corpus.py` (mirrors `decode_keymode_corpus.py`; Git-Bash launch per the Windows Qt
  constraint) → `tools/corpus_decode_chord/<preset>/<stem>.decode.json` (353/353 each, Baroque + Jazz).
- **Grader** `tools/cc_layer4_chord_baseline.py` — **one grading path, extended not forked**: reuses
  `compare_analyses.load_analysis` + `align_dcml_regions` (time-overlap) + the held-out `md5(stem)%100<20=test` split,
  exactly as the L3 harness. GT root + GT chord-tones come from **music21's `RomanNumeral`** parse of the SAME WiR
  annotation the project's metric uses (`root().pitchClass` and `pitchClasses`) — the coherent single GT source for
  both metrics.
- **The membership metric is stood up NOW** (spec §10 build deliverable — it did not exist): per sounding note, CT-vs-NCT
  vs the GT chord-tone set, precision/recall. INCREMENT A reports the **trivial baseline** (membership empty).

---

## §3 — Gate: ISOLATED + byte-identical (verified)

- **Production byte-identical — VERIFIED.** The new module is referenced ONLY by its own files + the `--decode-chords`
  diagnostic (`grep`-proven: `src/.../chordslicedecoder.{h,cpp}`, `tests/decode_chord_tests.cpp`, `tools/batch_analyze.cpp` —
  **nothing** in `notation/`, `region/`, or `section/`). The live per-region `analyzeChord` seam
  (`regionanalyzer.cpp:763`) is untouched.
  - **composing tests: 611/611 pass** (596 prior + **15 new** `Composing_DecodeChord`); chord-mismatch report unchanged.
  - **pipeline snapshots: 11/11 pass, NO golden refresh.**
  - **notation tests: 52/57** — the 5 failures are **PROVEN pre-existing**, NOT from Layer 4. They are all key/harmony
    outputs (`MozartK279…PrefersCMajorOverFLydian` = `keySignatureFifths` −1; `Corelli…SmearPreviousChord`;
    `…CadenceMarkersOnCorelli`; `HarmonyPinning.BehaviorSnapshot_{RomanNumeral,Nashville}`) driven by the **held,
    uncommitted key-decoder WIP** in the working tree (`keymodesequence.{cpp,h}`, `keymodeanalyzer.h`,
    `localmodulationdetector.{cpp,h}`, `regiontoneprimitives.cpp`). **Proof:** rebuilt `notation_tests` against
    `composing_analysis` with **Layer 4 reverted out of the build** (HEAD + held-WIP, no Layer 4) → the **identical 5
    failures** (52/57). So `notation(HEAD+WIP) == notation(HEAD+WIP+Layer4)`; my change moves nothing.
- **Behavioural unit tests** (`decode_chord_tests.cpp`, 15): scorer-independent `decideSlice` (chosen = top score;
  confidence = margin to best *different* chord; an inversion of the chosen is not a competitor; alternatives
  ranked-and-capped; the prevailing chord kept alive below topK; an inexpressible prevailing not forced; single-chord
  no-competitor sentinel; empty candidates → no-chord; membership sets empty) + note-model fixtures (a clean C-major then
  G-major triad each names THAT chord root-position; the complete candidate list is surfaced and ranked;
  `redecodeRange == full decode`; determinism).

### Directional baseline (the learning, NOT a pass/fail bar) — held-out TEST split, per preset

| | Baroque | Jazz |
|---|---|---|
| chord-root match, **per-region baseline** (`.ours.json`), dur-wt | **73.8%** | **73.7%** |
| chord-root match, **per-slice decoder**, dur-wt | **45.8%** | **45.7%** |
| Δ (decoder − baseline), dur-wt | **−28.1 pts** | **−28.0 pts** |
| NCT-membership over-read (sounding notes that are GT non-chord-tones) | **22.2%** (4531/20427) | **22.2%** (identical) |
| CT precision / NCT recall (trivial baseline) | **77.8% / 0.0%** | **77.8% / 0.0%** |

The decoder is **~28 pts rougher** than the per-region baseline — **exactly the expected embellishment over-read**: with
no membership yet, the ±1-neighbour window pools passing/neighbour tones into the chord, and they are read as chord
tones. The membership metric makes that headroom explicit: **22.2% of sounding notes are GT non-chord-tones the decoder
over-reads** (CT precision 77.8% < 100%; NCT recall 0% by construction — every true NCT missed). **This gap IS the
Increment-B membership lever — reported, not tuned away** (per instruction §3). The membership numbers are
**preset-invariant** (the sounding-note set + GT chord-tones are preset-independent; only the chosen chord differs,
which the empty-membership metric does not see). Top decoder root-misses are the symmetric/relative confusions
(`9→4`, `2→9`, `9→2`, `7→2`) the spelling-pin (Increment C) and membership (B) address.

---

## §4a — Unification ledger

**Reused (from source, not forked):**
- the **17-template scorer** `analyzeChord` and the complete **candidate cube** `fn::ScoringSnapshot::cells` via
  `snapshotOut` (the generation lever) — the one chord scorer;
- the **indexed window** `engravingbridge::weightedPcView` over `NoteModel::overlapping` (the per-slice perf floor is met
  by construction; the L3 O(N²) risk does not recur) — no third window builder;
- the **L2 slicer** `changePointSlices` (the per-slice observation grid);
- the **chord-root metric substrate** `compare_analyses.{load_analysis,align_dcml_regions,three_way_classify}` +
  `dcml_parser` + the `md5(stem)%100` held-out split (the L3 harness's substrate).

**Newly written (this increment):**
- the **per-slice chord module** `chordslicedecoder.{h,cpp}` (window → scorer → cube ranking → result carrier);
- the **result carrier** `SliceChord` with `confidence` / `uncertain` / ranked alternatives (+ the empty membership
  sets) — the spec §7 fields the old `ChordAnalysisResult` lacks (no `ChordFunction` carried — the L4/L5 boundary kept
  clean);
- the **`--decode-chords` diagnostic** + the driver `decode_chord_corpus.py`;
- the **NCT-membership precision/recall metric** harness (spec §10) — graded GT chord-tones from music21 `RomanNumeral`.

**Slated to RETIRE at the eventual wiring (NOT this increment):** the per-region chord path
(`regionanalyzer.cpp:763`, one `analyzeChord` per coarse region) → per-slice; the sparse/bass post-passes as bolt-ons →
folded into generation; the region-level flattened `pcWeight` aggregate as the membership input → the lossless per-note
`NoteEvent` stream; the key-driven `dim7CharacteristicBonus` rotation selector → the spelling-pin (Increment C).

**No NEW parallel path or logic duplication was introduced.**

---

## §5 — The increments after this (context, not this commit)

- **B** — the per-note neighbour-aware **membership** decision + the **two-pass** resolution + the **adaptive
  lazy-extend window** (the lever; graded by the membership metric + chord-root — this baseline shows the 22.2%
  over-read it must recover).
- **C** — the deterministic spelling-aware **symmetric (dim7/aug) root pin** replacing the key-driven
  `dim7CharacteristicBonus`; the new **types** (diminished-seventh; re-test minor-major); extensions read from membership.
- **Then** the wiring increment — re-point `regionanalyzer.cpp:763` per-slice; strip the L5 leftovers; gate on BIR +
  snapshots.

---

## §6 — Commit / files

**Committed locally (UNPUSHED):** `chordslicedecoder.{h,cpp}` + `decode_chord_tests.cpp` + the two `CMakeLists.txt`
additions + the `--decode-chords` hunks of `tools/batch_analyze.cpp` (the held B2 subdominant-guard hunks reverted out
before staging and restored after — backup-verified) + `tools/decode_chord_corpus.py` +
`tools/cc_layer4_chord_baseline.py` (force-added; load-bearing harness, like `cc_layer3_keymode_baseline.py`).

**Left UNSTAGED (held WIP):** the key-decoder WIP (`keymodesequence.{cpp,h}`, `keymodeanalyzer.h`,
`localmodulationdetector.{cpp,h}`, `regiontoneprimitives.cpp`), the B2 hunks of `batch_analyze.cpp`, the pre-existing
`tools/cc_layer3_keymode_baseline.py` / `tools/compare_rn.py` edits, and the `*.md` doc set. **Gitignored:** this report
(`/cc_*.md`) + the decode output (`/tools/corpus_*/`). `upstream` left untargeted.
