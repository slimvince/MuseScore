# CC INSTRUCTION — The voice-leading axis foundation build: VL-A / VL-B / VL-C, dormant (2026-07-03)

**Status: ACTIVE DISPATCH (written just-in-time after the spec's ratification; the only open instruction).**

## Mandatory reads BEFORE any work

1. `CLAUDE.md` — all standing rules apply, especially the VS Code bash rules (append `; echo "exit:$?"`; never
   large output — redirect to file), build via PowerShell `Start-Process`, both suites after every change.
2. `BUILD_AND_TEST.md` + `STATUS.md` header — current baselines and commands. Gate = **53/24/53 case-identity
   sets** (the sets, not the integers).
3. **`cowork_voiceleading_axis_design.md` — THE contract for this build, SIGNED (user, 2026-07-03). Read it in
   FULL.** Where this instruction and the spec disagree, STOP and report (do not pick).
4. `cowork_confidence_contract.md` §2/§5 (Class M, U1–U5, R4/R5) — VL-C publishes a boundary confidence.
5. `cowork_bounded_context_design.md` §3–§5 — the extension protocol VL-C's requester follows (the L4/L5
   dormant requester patterns from the extension build are the in-repo precedent).

## What this is

Build the **foundation of axis 2** as a new, **dormant** module family under
`src/composing/analysis/voiceleading/`: **VL-A** the voice-linear view (facts), **VL-B** motion & interval
profiles (facts + the per-sample motion-event series), **VL-C** texture classification (the one judgment:
*texture-of-span*, Class M, whole-selection granularity). Spec sections: §5.1–§5.3, §7, §8. NOTHING ELSE from
the spec is in scope (VL-D/E/F/G/H are design-gated).

**Dormant means:** no production call site; consumed only by tests and the new diagnostic. The harmonic spine's
behavior and the corpus gate are untouched **by construction** — prove it, don't argue it (acceptance below).

## Task A — VL-A: the voice-linear view (spec §5.1, §7)

New: `analysis/voiceleading/voicelinearview.{h,cpp}` (namespace `mu::composing::analysis::voiceleading`).

- Input: a built `notemodel::NoteModel` (do NOT re-walk the score — reuse; the note model is the one source).
- Output: `VoiceLine`s per (staff, voice): events ordered by onset; same-voice same-onset pitches grouped into
  ONE chordal event (`chordal` flag); each event carries pitch(es), tpc spelling, onset/release, and the L1
  eligibility flags. Metric weight is NOT stored (spec §7 as signed).
- **Partition + losslessness:** every retained L1 note appears in exactly one line exactly once; nothing
  dropped, flags carried. Round-trip test required (view → flat notes == the model's notes over the span).
- **Reduction is a per-query parameter:** v1 provides exactly `TopNote` (highest sounding pitch per event),
  applied at profile-query time, never mutating the view; the choice rides the output provenance.
- **Profile eligibility filter (declare in the report):** profile queries use the standard analysis-view filter
  (`plays && staffEligible`), consistent with the existing derived views; the lossless view itself keeps
  everything.

## Task B — VL-B: motion & interval profiles (spec §5.2, §0)

Same module directory, e.g. `voiceleadingprofiles.{h,cpp}`.

- **Motion profile** per the spec-§0 simultaneity rule EXACTLY: per concurrent voice pair, sample at the merged
  set of the two lines' onsets; piecewise-constant hold; drop both-static samples; classify
  parallel/similar/contrary/oblique; aggregate length-normalized rates over all pairs.
- **The per-sample motion-event series is part of the export** (spec §5.2): `MotionEvent {pair, sampleTick,
  type, harmonicIntervalBefore, harmonicIntervalAfter}` — facts, exposed alongside the rates.
- **Interval profile** per voice: |interval| histogram bins 0–11, ≥12 + repeat/step/leap rates (repeat = 0,
  step = 1–2, leap ≥ 3 semitones), aggregable over voices.
- **The "parallel" interval-preservation convention (spec §15-2):** READ
  `idiom_discovery/parsers/voiceleading2.py` and replicate its implemented convention exactly (semitone-exact vs
  generic). Declare the answer in the report; it closes spec §15-2 at the doc-sync.
- Deterministic; no tunable thresholds; no confidence.

## Task C — VL-C: texture classification (spec §5.3)

E.g. `textureclassifier.{h,cpp}`.

- **The feature-space measurement FIRST (spec §5.3; knowledge-based coding).** Read-only, in Python, on the
  study's saved feature data (`idiom_discovery/` pipeline; re-derive the matrix if the pickle is absent):
  evaluate the three named candidates — motion-only, two-stage (motion split → interval refinement), z-scored
  concatenation — by nearest-centroid membership agreement against the ratified study clustering (K=4). Pick
  the best-reproducing space; record numbers for all three in the report. The C++ classifier implements the
  winner. **If no candidate reproduces within a defensible tolerance, STOP and report** (the spec's §10(b)
  criterion decides; do not invent a fourth space).
- **Reference set:** the study centroids for the winning space, exported from the Python pipeline into a
  checked-in constants table with provenance comments (run, corpus state, K, seed policy).
- **Output (spec §5.3 as signed):** the committed class is the top of the **full ranked list of ALL class fits
  with weights** — carried in the output, nothing discarded; Class-M *texture-of-span* confidence squashed to
  [0,1]; the three floors by their spec names (**evidential floor**, **margin floor**, **fit floor**);
  abstention = margin below margin floor OR fit below fit floor; single-voice selection → *no-pair* abstention
  (never interval-only classification). Floor defaults: conservative, documented, marked precision-phase —
  derive from the study's fit distributions where cheap, otherwise document the choice.
- v1 granularity: the whole selection is ONE `VoiceLeadingSpan` (the per-span refinement is gated on spec
  §15-1 — NOT this build).

## Task D — the VL-C extension requester (spec §8)

The bounded-context discovery rule, coded + tested (the standing rule: a component ships with its extension
behavior): cue fires iff samples < evidential floor AND margin < margin floor; requester-owned loop calling
`NoteModel::extend` (later first, then earlier; increment = bars converted to ticks; stop = classification +
margin unchanged under further context; hard bound = settings cap; score-boundary honest). Denied/truncated →
`clipped-by-selection-edge` / `cue-denied` provenance on the output (spec §7). Follow the L4/L5 dormant
requester patterns (extension build, session 21j) — reuse, don't reinvent. Whole-score selection ⇒ no cue fires
(inertness test).

## Task E — diagnostic + study parity (spec §5.2 parity duty, §10)

- `--dump-vl` in `tools/batch_analyze.cpp` (default OFF, additive): JSON dump of VoiceLines (note tuples),
  motion/interval profiles, motion events, and the VL-C output for a score.
- `tools/compare_vl_parity.py` (new): feeds the DUMPED note tuples through the study's own feature functions
  (`voiceleading.py` `vl_profile`, `voiceleading2.py` View B) and diffs against the dumped C++ profiles.
  Tolerance declared (float-exact expected on rates; document any deviation). This tests the feature
  ARITHMETIC on identical input — ingestion differences are out of scope by design.
- Run on a pinned sample: ~10 chorale + ~5 keyboard/curated scores chosen per `docs/score_inventory.md`
  (research-tier only; do-not-touch list respected); pin the list in the report.

## Tests (full-coverage duty from birth — every new branch)

Composing-suite additions, oracle-asserted, plain-data constructible: each motion type + holds + both-static
drops + chordal reduction (hand fixtures, oracle by construction); VL-A partition/losslessness/round-trip/tie
inheritance; interval profile bins/rates; classifier: at-centroid / near-tie (margin floor) / far-from-all (fit
floor) / no-pair; ranked-list completeness + ordering + provenance; squash bounds [0,1]; extension: must-fire /
must-not-fire (margin clears) / termination / denial provenance / whole-score inertness; determinism (same
input ⇒ byte-same output, twice).

## Acceptance (ALL required)

1. Full suites green, no snapshot refresh: composing (1056 + new) / notation 53 / pipeline snapshots 11.
2. **Gate proof by measurement:** regen all three presets (`run_bach_preset.py` → `characterise_bir_false.py`,
   per-preset dirs) — case-identity sets byte-identical to CLAUDE.md's 53/24/53 (set-diff empty both ways).
3. **Dormancy grep-proof:** no production call site for any new symbol (tests + `--dump-vl` only).
4. Parity check passes on the pinned sample.
5. **Reuse-vs-new + what retires** in the report (expected: reuses NoteModel, the analysis-view filter, the
   L4/L5 requester pattern, the Python pipeline as validation harness; retires NOTHING — new axis; the Python
   pipeline stays research tooling, stated explicitly).
6. **Doc-sync, same increment:** ARCHITECTURE §2.15 (axis status line + voice-leading-span criterion pointer);
   `docs/implementation_roadmap.md` step 4 (build status); `cowork_confidence_contract.md` §3 inventory row
   (*texture-of-span*, Class M, squash shape per R5); the spec flips **AS-BUILT** carrying the feature-space
   declaration (§5.3) and the §15-2 answer. CLAUDE.md untouched.
7. Commits local, unpushed, fork-only; suggested split: module(s) / tests / diagnostic+parity / docs. Report:
   `cc_vl_foundation_build_report.md` (force-added per the `/cc_*.md` convention).

## STOP conditions (surface, do not proceed)

Any suite red or snapshot refresh needed; any gate set-diff nonempty; the feature-space measurement fails its
criterion; spec↔instruction disagreement; a needed fact not obtainable from the named sources; any change that
would touch files outside `src/composing/` + `tools/` + the named docs.
