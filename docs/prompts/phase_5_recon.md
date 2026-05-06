# Phase 5 — Recon: Modulation-Aware Roman Numeral Annotation

**Scope:** Read-only investigation. No source edits, no build, no
tests. Characterize the four unknowns that gate Phase 5
implementation: MuseScore engraving capability for pivot notation,
authoritative corpora for tuning, current `NoteHarmonicContext` /
status-bar surface for key data, and `KeyArea` production logic
in the post-4b `analyzeSection`. Output a recon report that drives
the Phase 5 implementation split.

This recon mirrors the 3c-recon and 4-recon patterns
(commits `d35f003aa2`, `640cfe165d`) — citation-heavy,
verdict-driven, implementation-shape recommendation.

**Reference docs (read first, in this order):**
- `docs/unified_analysis_pipeline.md` — overall plan; Phase 5 is
  "modulation-aware Roman numeral annotation via KeyArea spans"
- `docs/divergence_d_recon.md` — the canonical seeding pattern
  for `findTemporalContext` (relevant if KeyArea derivation
  involves similar mechanics)
- `docs/policy2_coalescing_map.md` — Pass 0–4 description; Phase
  4b inlined these into `analyzeSection`
- `src/composing/analyzed_section.h` — `AnalyzedRegion`,
  `AnalyzedSection`, `KeyArea` definitions
- Phase 4b commit `36368d67cc` — current state; `analyzeSection`
  is canonical, `KeyArea` is populated as part of `analyzeSection`'s
  output

**Phase 5 design context:**
- The principle: data is always inferred (regardless of where/how
  it is shown to the end-user). Per Vincent's stated principle,
  modulation/key-area data flows through `NoteHarmonicContext` and
  is available to all consumers. UI surfaces (status bar,
  right-click menu) decide display independently.
- Stripping principle (per `docs/extension_stripping_policy.md`
  and `project_no_stripping_in_production.md`): the shipping
  product never reduces analyzer output. Phase 5's emitter writes
  modulation/pivot information when the underlying data supports
  it; UI/render-layer simplification (if any) is separate.

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).

---

## Investigation

This is a read-only recon. Do not modify any source file. Do not
run the build or tests. The only file written this session is the
recon report itself.

### Q1 — MuseScore engraving capability for pivot notation

The web suggests MuseScore "supports" Roman numeral pivot notation
in the format `I=IV` (and potentially others). What "support"
actually means is unclear and must be determined from the
codebase. Three distinct capability levels exist:

- **Text-only support:** parser accepts the string and formatter
  renders it with Roman numeral typography. No semantic
  understanding of pivot relationships.
- **Semantic support:** MuseScore recognizes the pivot relation
  on the element and exposes it via metadata, transposes
  correctly, etc.
- **No support:** parser rejects, or formatter produces broken
  output.

Investigate:

- **`Harmony` element parser.** Locate the chord-symbol /
  Roman-numeral parser (likely in `src/engraving/dom/harmony.cpp`
  or similar). Does it accept `I=IV`? Does it accept other
  pivot conventions (`IV/I`, `IV → I`, two adjacent
  Romans)?
- **`Harmony` element formatter.** What does the formatter do
  with `I=IV` once parsed — render literally, special typography,
  reject?
- **Element metadata.** Does `Harmony` have any field/method that
  exposes pivot status as data, or is it purely a text element?
  Check the type's interface for keywords like "pivot",
  "modulation", "secondaryFunction", etc.
- **Transposition behavior.** When a score with `I=IV` annotation
  is transposed, does MuseScore handle the dual nature
  correctly (probably not, but verify)?
- **Roman-numeral-specific path.** Roman numerals may have a
  separate parsing/rendering path from chord symbols (per the
  Vincent's note that Romans are "text + format" while chord
  symbols are "text + format + semantic"). Identify both paths
  and characterize separately.

**Question to answer:** What is the actual extent of MuseScore's
support for pivot notation? Which conventions does it parse
cleanly? Is "support" text-only or semantic? Any quirks (rendering
artifacts, parsing edge cases, transposition issues) that the
emitter would need to work around?

### Q2 — Authoritative corpora for modulation tuning

Phase 5 needs ground-truth modulation data for tuning the
modulation-detection threshold and any KeyArea smoothing logic.
The `KeyArea.confidence` field exists but the threshold values
are guesswork without data.

Investigate:

- **DCML corpus key/modulation labels.** The DCML corpus is at
  `tools/dcml/` (per Phase 1a recon, 1538 MSCX scores across 12
  collections). DCML's standard datasets typically include
  per-measure or per-beat key labels in TSV/CSV sidecar files.
  - Which DCML datasets have key labels? Inspect the `tools/dcml/`
    directory structure.
  - What format are the labels in?
  - Are the labels extractable into a comparison harness via
    existing infrastructure, or would new tooling be needed?
- **Chord-symbol-ban applicability.** The chord-symbol-ban (per
  `project_chord_symbol_ban.md`, `docs/symbol_input_audit.md`)
  prohibits using `Harmony` elements as analyzer input. Does it
  apply to KEY annotations as well? Per the ban memo, the
  prohibition is specifically about chord-symbol input — key
  labels are a different category. Verify this interpretation by
  re-reading the ban doc.
- **Other corpora.** Beyond DCML, are there other corpora in
  `tools/` or referenced elsewhere that have modulation labels?
  (Hiromi at `tools/extra scores/hiromi` is non-authoritative
  per `reference_hiromi_corpus.md` — not for tuning.)
- **The 10 snapshot corpus scores.** Two of them (Mozart, Chopin)
  modulate. Do the corresponding DCML entries have key labels we
  could use for verification?

**Question to answer:** Which corpora have authoritative key /
modulation labels usable for tuning Phase 5's threshold and
smoothing logic? Are they extractable today or do we need new
tooling?

### Q3 — `NoteHarmonicContext` and status-bar surface today

Per Vincent's principle, modulation/key-area data should flow
through analyzer outputs to all consumers; UI decides display.
This means `NoteHarmonicContext` (the type P3 returns) likely
needs to gain modulation context — probably a `KeyArea`
reference or copy and possibly an "at boundary" flag.

Investigate:

- **`NoteHarmonicContext` definition** in
  `src/notation/internal/notationcomposingbridge.h`. List all
  current fields. Note especially what key-related data is
  already present (per Phase 1b: `wasRegional` field exists;
  per Phase 3c: `alternatives` and temporal extensions exist).
- **Status-bar consumer path.** Trace from
  `analyzeHarmonicContextAtTick` /
  `analyzeNoteHarmonicContextRegionallyInWindow` through the
  bridge layer to status-bar text formatting. Where does the
  string the user sees actually get assembled?
- **Right-click menu consumer path.** Same trace for the
  right-click "Add chord symbol / Roman numeral / Nashville"
  submenus (per Phase 3c-recon, at
  `src/notationscene/qml/MuseScore/NotationScene/notationcontextmenumodel.cpp:55-151`).
- **`harmonicAnnotation` formatter.** Per Phase 3c-recon, this
  formats up to N candidates with confidence scores. Could it
  also format modulation context (e.g. "in C: V → in G: I")?
  Identify the formatter's current API surface.
- **Where `KeyArea` would slot in.** Given the trace, what's
  the cleanest place to add `KeyArea` exposure on
  `NoteHarmonicContext`? Per Phase 3c precedent (`wasRegional`
  field), small additive fields on this struct have low ripple
  cost.

**Question to answer:** What's the current bridge surface for
key/modulation data flowing to status bar and right-click? What's
the cleanest API addition to expose `KeyArea` data? Where does
formatter logic live for the user-facing string?

### Q4 — `KeyArea` production logic post-4b

`AnalyzedSection` now exposes `keyAreas` as a vector. The values
populated by `analyzeSection` (post-4b) are unverified empirically.
We don't know yet whether the spans are sensible, noisy, or
broken on real corpus.

This recon is read-only and shouldn't run the binary, but should
characterize the production logic from code:

- **Where in `analyzeSection`'s body is `KeyArea` populated?**
  Per Phase 2 (and 4b's inlining), the keyAreas vector is derived
  by walking the AnalyzedRegion list and collapsing adjacent
  regions with the same key+mode into spans. Locate the actual
  derivation code.
- **What does the derivation use?** `AnalyzedRegion.chordResult.key`?
  `AnalyzedRegion.chordResult.mode`? A separate key analysis
  field? Confidence?
- **Is there any smoothing or hysteresis** applied between
  per-region key analysis and the spans? Or are spans purely
  derived from raw per-region key values?
- **What's `KeyArea.confidence`?** A field exists per Phase 2
  audit. How is it populated — averaged over the spanned
  regions, taken from a specific source, hardcoded, computed?
- **Predicted behavior on noisy data.** If a piece has a brief
  V/V tonicization (e.g., 4 beats of D-major harmony in a piece
  in C-major), would the analyzer per-region-classify those 4
  beats as G-major (the V's local tonic) or as still-C-major
  (the surrounding context)? The answer determines whether
  Phase 5 will see lots of micro-modulation noise or genuinely
  stable spans. Read the per-region key analysis logic
  (`resolveKeyAndMode` and friends) to predict.

**Question to answer:** What is the current production logic for
`KeyArea` derivation? What characteristics should we expect from
empirical observation? What confidence-related smoothing exists,
if any?

### Q5 — Synthesis and Phase 5 implementation shape

Based on Q1–Q4, recommend a Phase 5 implementation split. Three
shapes to consider:

- **Phase 5a (empirical observation) → Phase 5b (modulation
  emitter behavior).** 5a adds `KeyArea` capture to the
  pipeline_snapshot_tests harness so we can see what the
  analyzer produces today. Behavior-neutral additive change;
  snapshot diff is "new field appears." We then look at the
  actual KeyArea data and decide threshold/smoothing/notation
  questions with evidence in hand. 5b implements the
  modulation-aware emitter using whatever convention Q1
  surfaced as cleanly supported.
- **Phase 5a (KeyArea consumption infrastructure) → Phase 5b
  (modulation emitter behavior) → Phase 5c (post-observation
  tuning).** Three-step if Q4 reveals the KeyArea population
  needs work first, or if Q1's engraving findings require
  emitter-side work that's separable from the modulation
  decision logic.
- **Single Phase 5 session.** Only viable if: KeyArea
  population is sound (Q4), engraving support is clean and
  one convention is obvious (Q1), tuning corpora are
  available (Q2), and bridge surface needs only a small
  additive change (Q3). Unlikely given the open questions but
  possible.

State the recommendation with reasoning. Identify per-chunk:
- Snapshot impact (Phase 5 is the first behavior-changing phase
  by design — annotation snapshots WILL diff during 5b; predict
  the diff shape so verification can distinguish "expected
  behavior change" from "regression elsewhere")
- Behavior-preservation risk (low / medium / high)
- Whether any chunk needs its own sub-recon

Also call out: any sub-recons that should precede an implementation
chunk (e.g., if Q1 reveals the engraving capability is
under-documented and needs a focused engraving-side investigation
before emitter design).

---

## Deliverable

Write a single report file at `docs/phase5_recon.md` with sections
matching Q1–Q5 above. Concise and citation-heavy — every claim
backed by file:line. Total length: probably 5–8 pages of markdown.

Suggested skeleton:

```markdown
# Phase 5 — Modulation-Aware Annotation Recon

Date: 2026-04-25
Scope: read-only, no source edits.

## Recommended implementation shape

[One sentence: 1 / 2 / 3 sessions, with one-line evidence summary]

## Q1 — MuseScore engraving capability for pivot notation

[Parser/formatter behavior, supported conventions, "support" extent,
quirks, citation-heavy]

## Q2 — Authoritative corpora for modulation tuning

[DCML key labels availability, chord-symbol-ban applicability check,
other corpora]

## Q3 — NoteHarmonicContext and status-bar surface today

[Current fields, consumer paths, formatter location, KeyArea slot-in
recommendation]

## Q4 — KeyArea production logic post-4b

[Derivation logic, smoothing/hysteresis, confidence semantics,
predicted noise characteristics]

## Q5 — Synthesis

[Recommended split, dependency order, snapshot impact predictions,
behavior-preservation risk per chunk, any sub-recons needed]
```

---

## Commit + push

Single commit, just the recon report. Suggested message:

```
Phase 5 recon: characterize modulation-aware annotation surface

Investigates MuseScore engraving capability for pivot notation
(parser/formatter "support" extent), authoritative corpora for
modulation-detection tuning (DCML key labels, chord-symbol-ban
applicability to key annotations), current bridge surface for
key/modulation data flowing to status bar and right-click, and
KeyArea production logic post-4b.

Recommends Phase 5 implementation split: [1/2/3 sessions per Q5
verdict].

Informs Phase 5-impl shape; identifies any sub-recons needed.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- The recommended Phase 5 split (1 / 2 / 3 sessions) with
  one-sentence evidence summary
- The single most surprising finding from Q1–Q4 (this is what we
  pay the recon cost for; if there's nothing surprising, say so —
  that itself is a finding)
- Engraving capability verdict for `I=IV`-style pivot notation:
  text-only support, semantic support, no support, or other
- Whether DCML's key labels are usable for tuning (yes / yes-with-tooling /
  no — cite ban applicability check)
- Behavior-preservation risk picture per chunk (low / medium —
  any "high" should be flagged immediately)
- Whether any chunk requires its own sub-recon
- Any deviations from this prompt and why

---

## Scope guardrails

- **Do not** modify any source file. The only file written this
  session is `docs/phase5_recon.md`.
- **Do not** run the build or tests. This recon is pure code +
  history reading. Empirical KeyArea quality assessment (Q4) is
  characterized from code, not from runtime observation. If empirical
  observation is needed, recommend Phase 5a as the place to do it
  (additive snapshot field + regenerate goldens once gives us the
  data with a small implementation), not in this recon.
- **Do not** propose code changes in the report — the Phase 5-impl
  prompt(s) come after, informed by the recon's verdict and split
  recommendation.
- **Do not** speculate beyond what the code shows. If Q1–Q4 don't
  have clear evidence in places, say so explicitly. "I don't know,
  but here's what I'd need to investigate further" is more useful
  than a confident guess.
- **Do not** conflate the chord-symbol-ban (which prohibits
  `Harmony`-element chord-symbol input as analyzer input) with key
  annotations. These are different categories; Q2 explicitly checks
  whether the ban applies to key labels.
- **Do not** assume any specific pivot notation convention is
  canonical — Q1's job is to discover what MuseScore actually
  supports, not to validate a preconceived choice.
