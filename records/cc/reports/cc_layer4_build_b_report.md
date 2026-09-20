# CC — Architectural Layer 4 (CHORD SYMBOL + NON-CHORD TONES) — Increment B build report

**Status:** BUILT, unit-tested, graded, committed **locally (UNPUSHED)** on top of Increment A (`48909fb752`, already on
`origin`). The per-note **membership decision** (chord-tone vs non-chord-tone) + its **score feedback** + the **two-pass
neighbour-aware resolution** + the **adaptive lazy-extend window** + the filled result carrier + the membership-metric
harness + behaviour tests. **Production byte-identical** (the decoder still runs only under the read-only
`batch_analyze --decode-chords` diagnostic, which returns before `analyzeScore`). `upstream` untouched.

**Spec:** `cowork_layer4_chordsymbol_design.md` (SIGNED). **Builds on:** Increment A (`cc_layer4_build_a_report.md`) —
which stood up the per-slice path + grading and measured the **−28pt embellishment over-read** (per-slice 45.8/45.7 vs
per-region 73.8/73.7; **22.2% of sounding notes are GT non-chord-tones the empty-membership decoder swallowed**).
Increment B is the **lever** that closes that gap. Still **isolated**: the spelling-pin / new chord types are
Increment C, wiring is later.

§0 was already satisfied at session start — `git ls-remote origin master` = `48909fb752` (Increment A), equal to local
HEAD; `upstream` not touched.

---

## §1 — The membership decision as built

For each Layer-2 slice and each candidate chord, every **focal** sounding note (the notes in `[slice.start, slice.end)`,
read off the **INDEXED** `NoteModel::overlapping` per-note stream — `eligibleNotesInSpan`, NOT the aggregated
`weightedPcView`) is classified **chord-tone vs non-chord-tone** from exactly the two design cues:

- **Metric salience** — `metricWeight[0.5,1] × min(1, durationQn / refDur)`. The beat weight is the **prefs-free indexed
  per-note** `scoreharvest::regionMetricWeightForOnsetTick(score, onset)` (tick→beat-type via `tick2measure` +
  `rtick2beatType`, no segment walk). A weak/short/off-beat note is embellishment-like.
- **Local stepwise treatment** (`isStepwiseTreated`) — per-voice, within the window: a **passing/neighbour** tone
  (approached *and* left by step, both between chord tones) **or** a **suspension** (a tone held from the previous chord
  that resolves DOWN by step to a chord tone). Uses the neighbour chords as *context only* — no chord-to-chord
  transition cost, no progression grammar (that is Layer 5).

A focal note whose pitch class is a **basic template tone** of the candidate (tested via the one chord-tone oracle
`function::bassIsTemplateChordTone` / the `kMasks` table — no second interval set) is always a chord tone. An **extra**
note (pc outside the basic triad/seventh) is a **non-chord tone** when it is embellishment-like (weak salience OR
stepwise), otherwise a **chord-tone extension** — the sustained strong 6th/9th that "falls out" of membership (design §5;
no separate extension detector, no new chord type). Membership sets (`chordTonePcs` / `nonChordTonePcs`) are filled on
the carrier over the focal slice's pcs (a pc is non-chord only when *all* its focal notes are embellishment-like).

**The feedback (the lever, design §5 step 3):** a candidate is charged
`membershipPenaltyWeight × salience` for every **structural** focal note (an extra note it must treat as a chord-tone
extension — an *implausible chord tone the basic template does not contain*). Candidate scores are re-ranked by
`verticalScore − penalty`, so the chosen chord is the one that best explains the slice as **a chord plus its non-chord
tones**. Weak/stepwise extras cost the chord nothing (they are explained as embellishments) — this is what recovers both
the over-read and the chord-root.

Every cost-driving value is a **setting** on `ChordSliceDecoderPreferences` (effort hygiene — nothing hardcoded):
`membershipSalienceThreshold` (0.55), `membershipReferenceDurationQn` (1.0), `membershipPenaltyWeight` (0.6),
`stepwiseGapToleranceTicks` (0), `enableMembership`/`twoPass` switches, plus the window settings below. All exposed as
decode-only CLI overrides (`--chord-memb-salience / --chord-memb-penalty / --chord-memb-ref-dur / --chord-stepwise-tol /
--chord-no-membership / --chord-no-two-pass`).

## §2 — Two-pass resolution

The membership↔neighbour-chord chicken-and-egg is resolved in two passes (spec §4), reusing one cached candidate cube
per slice (**no second `analyzeChord`** — the scorer cost is paid once per slice in pass 1):

- **Pass 1** names each slice provisionally from its own window + the key prior alone (`decideSlice`, no neighbour-chord
  context, no membership feedback). The pass-1 chosen is **context-free** (depends only on the slice's window).
- **Pass 2** re-decides each slice's chord-and-membership using the **provisional pass-1 neighbours on both sides**
  (`prevC`/`nextC`) — a passing tone needs the chord it leaves *and* the chord it resolves to. Single refinement pass;
  the bounded-joint alternative (spec §15) is deferred.

`redecodeRange(first,last)` reproduces a full decode's slices **exactly** (the redecode behaviour test passes): because
the pass-1 and pass-2 chosen chords are context-free w.r.t. the prevailing incumbent, the driver recomputes pass 1 over
`[first-2, last+1]` and pass 2 from `first-1`, reproducing chosen / confidence / membership **and** the ∪-prevailing
alternative.

## §3 — Adaptive lazy-extend window

The window (`adaptiveWindow`) starts at the narrow base (`±contextSlices`, default 1) and grows one slice each side at a
time, stopping as soon as it holds `≥ minHarmonyPcs` distinct pitch classes (the prevailing harmony is in view) OR
reaches `±maxContextSlices` (default 3 — bounded by one harmony's worth of figuration, never a phrase). A dense (triad)
slice already meets `minHarmonyPcs` (3) so it keeps the base window; only thin (arpeggio / dyad) slices extend. The
distinct-pc probe reuses the **INDEXED** `NoteModel::overlapping` — **no new window builder**.

---

## §4 — The directional result (held-out TEST split, out-of-sample, both presets)

**The decisive question — does per-slice + membership meet/beat the per-region baseline?** **Answer: NO, not yet — but
membership recovers ~45% of the gap, and it is the membership *re-rank feedback* (not the window) that does it.**

| chord-root, dur-weighted (TEST) | Baroque | Jazz |
|---|---|---|
| per-region **baseline** (`.ours.json`) | **73.8%** | **73.7%** |
| per-slice, **Increment A** (fixed window, no membership) | 45.8% | 45.7% |
| per-slice, **Increment B** (adaptive + membership + feedback) | **58.4%** | **58.3%** |
| Δ B − A (the membership lever) | **+12.6** | **+12.6** |
| Δ B − per-region (residual gap) | **−15.4** | **−15.4** |

**Ablation (Baroque, decisive decomposition of the +12.6):**

| variant | dur-wt root |
|---|---|
| Increment A (fixed window, no membership) | 45.8% |
| B / adaptive window, `--chord-no-membership` | **45.8%** (window inert on root) |
| B / adaptive + membership labels, `--chord-memb-penalty 0` (no re-rank) | **45.8%** (labelling alone inert on root) |
| B / full (adaptive + membership + re-rank, penalty 0.6) | **58.4%** |

So the **entire** chord-root gain is the **membership score-feedback re-rank**; the adaptive window and the labelling are
each ~inert on the root number (the corpus's slices are mostly already dense enough that the window rarely lazy-extends).

**Membership metric (now non-trivial — the lever measured in its own right):**

| NCT membership (TEST, per (slice,pc)) | Baroque | Jazz |
|---|---|---|
| NCT recall (true non-chord tones caught) | **34.5%** (was 0%) | 34.5% |
| NCT precision (of our NCT calls, how many right) | 50.4% | 50.4% |
| CT precision (1 − residual over-read) | **82.9%** (was 77.8%) | 82.9% |
| CT recall (true chord tones not wrongly dropped) | 90.3% | 90.3% |

Membership catches **a third** of the true non-chord tones at coin-flip precision, lifting CT precision 77.8 → 82.9
(the over-read 22.2% → 17.1% residual). The two presets are within noise of each other (membership reads the
preset-independent sounding-note set; only the chosen chord differs).

**Residual breakdown (where it still under-/over-calls), reported, not tuned away:**
- **Chord-root residual (−15.4 to per-region)** is dominated by two sources the *membership* lever structurally cannot
  fix: (a) the decoder is fed the **single notated key signature** as its prior (one key for the whole piece), where the
  per-region baseline has the full production key resolution — a **wiring-increment** concern (per-slice Layer-3
  feed-forward), not membership; and (b) the top misses are **symmetric / relative root confusions**
  (`2→9, 9→4, 9→2, 7→2, 5→2` — D-attractor, dim7 rotations, relative major/minor) that the **spelling-pin (Increment C)**
  addresses, not membership.
- **Membership residual:** NCT recall is 34.5% — the caught third are the metrically-weak and the clearly-stepwise
  embellishments; the missed two-thirds are NCTs that are *neither* weak *nor* locally stepwise within the window
  (chromatic appoggiaturas on strong beats, NCTs whose resolution lies outside the bounded window, and the genuinely
  function-dependent cases the spec carries as "uncertain" for Layer 5). NCT precision 50.4% reflects extras called NCT
  that the GT actually counts as chord tones (added-tone readings the basic-template vocabulary cannot name yet —
  Increment C).

**Settings note (not a target chase):** `membershipPenaltyWeight` was seeded at a defensible 0.6 and the result reported
honestly. The two-point sensitivity already measured (penalty 0 → 45.8, penalty 0.6 → 58.4) shows the feedback is the
lever and the effect is large; a finer sweep is the spec's "swept later" future work, not part of this increment.

---

## §5 — Gate: ISOLATED + byte-identical (verified)

- **Production byte-identical — VERIFIED.** The new helpers and the decoder are reachable **only** from decode-only
  paths (grep-proven): `regionMetricWeightForOnsetTick` is called **only** by `chordslicedecoder.cpp`;
  `beatTypeForOnsetTick` only by `metricweights` (self) and the `pitchContextOverSpan` key path's
  `beatWeightForOnsetTick` (the L3 decode-only path); `ChordSliceDecoder` only by its own files + tests +
  `--decode-chords`. The live per-region `analyzeChord` seam is untouched.
- **composing tests: 617/617 pass** (611 prior + **6 new** `Composing_DecodeChord` membership tests); chord-mismatch
  report unchanged (RealDiff Std/Jazz unmoved — the decoder is isolated).
- **pipeline snapshots: 11/11 pass, NO golden refresh.**
- **notation tests: 52/57 — the SAME 5 failures as Increment A**, byte-for-byte
  (`MozartK279…PrefersCMajorOverFLydian`, `Corelli…SmearPreviousChord`, `…CadenceMarkersOnCorelli`,
  `HarmonyPinning.BehaviorSnapshot_{RomanNumeral,Nashville}`) — all driven by the **held, uncommitted key-decoder WIP**
  in the working tree, NOT by Layer 4. **No new notation failure** (§7 STOP not triggered). The `beatWeightForOnsetTick`
  refactor is behaviour-identical (a thin wrapper over the extracted shared lookup) and decode-only anyway, so it cannot
  move the set.
- **Behaviour tests** (`decode_chord_tests.cpp`, 6 new, scorer-free `classifyMembership`): a clean triad → all chord
  tones; a **weak short extra → non-chord tone** (chord stays); a **sustained strong extra → chord-tone extension**
  (a 6th, with the basic triad charged the implausibility penalty); a **suspension → non-chord tone** even on a strong
  beat; a **passing tone → non-chord tone** purely by stepwise treatment; determinism. Plus the existing scorer-free
  selection tests and the end-to-end fixtures (clean-triad naming, ranked-cube, determinism, redecode) all pass with
  membership ON by default.

## §5a — Unification ledger (standing rule)

**Reused (from source, not forked):**
- the **one chord scorer** `analyzeChord` + its candidate cube (the generation lever) — pass 2 re-ranks the cached cube,
  it does NOT re-run the scorer (no second scorer, no O(N²): the scorer cost is paid once per slice in pass 1);
- the **one chord-tone oracle** `function::bassIsTemplateChordTone` (the `kMasks` table) for membership — no second
  interval set;
- the **indexed** `NoteModel::overlapping` for both the focal/window per-note streams **and** the adaptive-window
  distinct-pc probe — **no new window builder, no DOM walk**;
- the **indexed beat-type lookup**: `beatTypeForOnsetTick` was extracted into `scoreharvest/metricweights` as the **single
  source** for tick→beat-type, and the pre-existing `pitchContextOverSpan` helper `beatWeightForOnsetTick` was
  **refactored to call it** — so the key path (prefs-weighted) and the chord membership (prefs-free
  `regionMetricWeightForOnsetTick`) share one implementation rather than duplicating the `tick2measure +
  rtick2beatType` logic;
- the **L3 harness substrate** (`compare_analyses` / `dcml_parser` / the `md5(stem)%100` held-out split) for the grader.

**Two views for two purposes (not a duplicated builder):** membership reads the **indexed per-note** stream
(`eligibleNotesInSpan` over `NoteModel::overlapping`); candidate scoring stays on `weightedPcView` — the §5a discipline.

**Slated to RETIRE at wiring (NOT this increment):** the per-region chord path → per-slice; the per-region flattened
`pcWeight` aggregate as the membership input → the lossless per-note stream (already the input here, under the
diagnostic); the single notated-key prior → the Layer-3 per-slice key feed-forward (the source of much of the residual
chord-root gap). The duplicate `beatWeightForOnsetTick` is now collapsed (single-source) ahead of wiring.

**No new parallel path or logic duplication was introduced.**

---

## §6 — Commit / files

**Committed locally (UNPUSHED)** on top of `48909fb752`:
- `src/composing/analysis/chord/chordslicedecoder.{h,cpp}` — membership + feedback + two-pass + adaptive window + filled
  carrier;
- `src/composing/analysis/scoreharvest/metricweights.{h,cpp}` — additive `beatTypeForOnsetTick` /
  `regionMetricWeightForOnsetTick` (single-source);
- `src/composing/analysis/engravingbridge/regiontoneprimitives.cpp` — **the refactor hunk only**
  (`beatWeightForOnsetTick` → wrapper over the shared lookup); the held `p.tpc` WIP line left **unstaged**;
- `src/composing/tests/decode_chord_tests.cpp` — 6 new membership behaviour tests + the renamed scorer-free test;
- `tools/batch_analyze.cpp` — **my hunks only** (the membership/window CLI overrides + help + the runChordDecode
  comment); the held B2 / modulation hunks left **unstaged**;
- `tools/cc_layer4_chord_baseline.py` — membership report now reports the non-trivial precision/recall; the directional
  line asks the meet/beat question.

**Left UNSTAGED (held WIP):** the key-decoder/tpc/B2 hunks (`keymodesequence.*`, `keymodeanalyzer.h`,
`localmodulationdetector.*`, `regiontoneprimitives.cpp` p.tpc, the `batch_analyze.cpp` B2/modulation hunks, the
`cc_layer3_*`/`compare_rn.py` edits, the `*.md` doc set). **Gitignored:** this report (`/cc_*.md`) + the decode output
(`/tools/corpus_*/`, including the two Baroque ablation dirs). `upstream` left untargeted.
