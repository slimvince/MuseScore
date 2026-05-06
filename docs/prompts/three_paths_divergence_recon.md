# Recon — Three Paths Diverging on m285

**Scope:** Read-only investigation. No source edits, no build, no
tests. Determine why three supposedly-unified user-facing paths
produce three different results for the chord at m285 of the
composing_tests catalog (notes: D5, A#4, F#4, C4):

- **Status bar** shows `Csus(add9)`
- **Right-click "Add chord symbol"** shows `Cm7b5`
- **Annotation emit** produces nothing

The unified analysis pipeline refactor (Phases 1-5b, complete at
commit `da68035054`) was supposed to ensure all four user-facing
paths (P1 Implode, P2 Annotation, P3 Tick-regional, P4 Tick-local)
consume the same `analyzeSection`-produced data. Three different
results for the same note-and-tick context suggests either an
architectural gap in the unification or divergent presentation
logic that effectively un-unifies the output.

This recon mirrors the 3c-recon / Phase 4-recon / Phase 5-recon
patterns — citation-heavy, verdict-driven, recommendation-based.

**Reference docs (read first, in this order):**
- `docs/phase5_recon.md` — Q3 has the bridge surface analysis
  (`NoteHarmonicContext` consumers, status-bar path, right-click
  menu path)
- `docs/phase4_recon.md` — for the post-refactor architecture
  state
- `docs/policy2_coalescing_map.md` — the four-path matrix
  (P1/P2/P3/P4)
- `src/composing/tests/data/chordanalyzer_catalog.musicxml` — the
  catalog file where m285 lives. Inspect the chord at m285 to
  understand its actual notation (might be already-known: notes
  D5, A#4, F#4, C4; tick position; region duration)
- `src/composing/tests/chord_mismatch_report.txt` — current
  mismatch report; m285 entry will show catalog-vs-analyzer text

**Memory references** (auto-loaded):
- `project_chord_symbol_ban` — analyzer reads notes + structural
  metadata only; banned from reading user analytical content
- `project_no_stripping_in_production` — analyzer outputs maximal
  exact identity; no reduction in production
- `project_divergence_d_recon` — context on Phase 3c's closure of
  P3 re-analysis; relevant if the recon surfaces a similar pattern

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).

---

## Background

The chord at m285 is genuinely ambiguous from the notes alone
(missing the third). Multiple defensible interpretations exist:

- **Half-diminished 9** (`Cm7b5(add9)` / `Cø9`): treats F# as
  enharmonic Gb (b5), A# as Bb (b7), D as the 9. Missing the b3
  (Eb), so the chord is rootless or third-omitted.
- **Sus interpretation** (`Csus(add9)` or similar): treats D as a
  sus tone replacing the 3rd. Note that the literal Csus2/Csus4
  conventions don't fit (no perfect 5th, no F natural), so the
  label is unconventional regardless of which path produces it.
- Other readings exist (whole-tone subset, altered dominant
  fragment, German +6 variant) but none match the observed
  Csus(add9) / Cm7b5 outputs.

So the chord supports multiple labels. The recon question isn't
"which label is right" — it's "why do supposedly-unified paths
produce *different* labels for the same note-and-tick context."

---

## Investigation

This is a read-only recon. Do not modify any source file. Do not
run the build or tests. The only file written this session is the
recon report itself.

### Q1 — Status bar call path

Trace from `harmonicAnnotation(Note*)` through whatever it calls
to produce the displayed string. Per `docs/phase5_recon.md` Q3:

> `harmonicAnnotation(Note*)` (`notationcomposingbridge.cpp:474–584`):
> entry point. Calls `analyzeNoteHarmonicContextDetails(note)`
> (line 482) ...

Continue the trace:
- What does `analyzeNoteHarmonicContextDetails` call?
- Does it construct a `NoteHarmonicContext` directly, or delegate
  to another bridge function?
- Does the path go through `analyzeSection` (the unified entry
  point) or take a different route?
- At what point is the displayed chord string formatted? Which
  `chordResults` entry is shown?

### Q2 — Right-click menu call path

Trace from the right-click "Add chord symbol" / "Add Roman numeral"
/ "Add Nashville" submenu builder. Per `docs/phase5_recon.md` Q3:

> `appendAnalysisItemsForContext` (`notationcontextmenumodel.cpp:55–164`)
> receives a pre-populated `NoteHarmonicContext`, reads
> `context.keyFifths` for the formatter (line 58), iterates
> `chordResults` (line 92), and builds symbol/Roman/Nashville
> submenus.

The menu *receives* the `NoteHarmonicContext` pre-populated. Trace
backward: where is that `NoteHarmonicContext` populated?

- Which bridge function calls `appendAnalysisItemsForContext` with
  what `NoteHarmonicContext`?
- That caller — what populates the `NoteHarmonicContext` it
  passes? Does it call `analyzeNoteHarmonicContextDetails` (same
  as status bar) or something else?
- If the populating function is different from the status bar's,
  identify which underlying analyzer path it takes.

### Q3 — Annotation emit call path

Trace from `emitHarmonicAnnotations` (introduced in Phase 3b) for
m285 specifically:

- The path goes through `analyzeSection` (canonical post-Phase-4b)
  and writes Harmony elements via the emitter
- Why is m285 producing nothing? Two main hypotheses:
  - **Divergence C duration gate.** `EmitAnnotationOptions::minimumDisplayDurationBeats = 0.5`
    silences sub-beat regions. m285's region duration: how many
    ticks / beats?
  - **Region not analyzed.** If the analyzer fails to identify a
    chord at m285's region (perhaps the missing-third case
    triggers some "no result" branch), no annotation is written.

Determine which is true for m285. If it's the duration gate,
that's known parked behavior (divergence C, bundled with the
cadence-aware-gate idea for post-Phase-5). If it's a "no result"
case, that's a different finding worth knowing.

### Q4 — `chordResults` content for m285

Determine what the analyzer's `chordResults` vector actually
contains at m285's tick:

- This requires understanding what `analyzeSection` produces for
  m285's region. If you can read this from code (by tracing the
  pass logic given the input notes), report your reasoning. If
  it's not feasible to determine from code reading alone, surface
  that and recommend an empirical step (e.g., add temporary
  logging in a future session) — but do NOT add code in this
  recon.
- Specifically: does the vector contain BOTH `Csus(add9)` and
  `Cm7b5` (with different scores), or different content
  altogether?

If the vector contains both, the divergence is in presentation:
status bar shows entry `[0]` while right-click iterates and shows
multiple entries, OR the two paths apply different sort/filter
logic.

If the vector differs between paths, the divergence is structural:
different code paths produce different `chordResults` for the same
note-and-tick context. That's an architectural unification gap.

### Q5 — Synthesis: type of divergence

Based on Q1-Q4, classify the divergence:

- **(α) Structural divergence.** Status bar and right-click take
  different underlying analyzer paths producing different
  `chordResults`. The unified pipeline has a gap.
  Implication: focused fix to route the diverging path through
  `analyzeSection`, mirroring how Phase 3a-3c unified the four
  emitter paths. Possibly a small follow-up phase, possibly a
  bug fix in a single bridge function.

- **(β) Presentation divergence.** Both paths consume the same
  `chordResults`, but the formatters apply different display logic
  (different sort, filter, or ranking). Implication: align the
  presentation layer; same data, same display rules.

- **(γ) Edge-case formatting.** The chord is genuinely ambiguous,
  the `chordResults` vector contains multiple near-equal-score
  candidates, and different paths happen to surface different
  ones based on internal sort stability or formatter-specific
  decisions. Less of a bug, more of a documented edge-case
  behavior on ambiguous chords.

The answer probably isn't a clean (α) or (β) or (γ) — it might be
a mix. Report what the evidence supports.

### Q6 — Bonus: unconventional `Csus(add9)` label

Separate finding worth surfacing: `Csus(add9)` is an unconventional
label for the actual notes (D, F#, A#, C — no G, no F natural).
Trace the `ChordSymbolFormatter` logic that produces this label:

- What chord identity does the formatter receive (root, quality,
  extensions)?
- What input combination produces the `Csus(add9)` string output?
- Is the formatter producing wrong output, or is the chord
  identity it received already incorrect?

This is adjacent to the main divergence question but is its own
small finding — the formatter producing unconventional labels for
ambiguous chords might be a pattern that affects other ambiguous
chord cases in the corpus.

---

## Deliverable

Write a single report file at
`docs/three_paths_divergence_recon.md` with sections matching
Q1-Q6. Concise and citation-heavy — every claim backed by
file:line. Total length: probably 4-6 pages of markdown.

Suggested skeleton:

```markdown
# Three Paths Divergence at m285 — Recon

Date: 2026-04-26
Scope: read-only, no source edits.
Base commit: `da68035054`

## Verdict

[Type of divergence (α/β/γ); brief evidence; recommended fix
shape]

## Q1 — Status bar call path

[Trace, citations]

## Q2 — Right-click menu call path

[Trace, citations]

## Q3 — Annotation emit at m285

[Why is annotation empty? Duration gate or no-result?]

## Q4 — chordResults content at m285

[What's actually in the vector; how confident is this analysis]

## Q5 — Synthesis

[Verdict reasoning, recommended fix shape, severity assessment]

## Q6 — Unconventional Csus(add9) label

[Formatter analysis, separate from main question]
```

---

## Commit + push

Single commit, just the recon report. Suggested message:

```
Recon: three paths diverge on m285 chord identification

Investigates why three supposedly-unified user-facing paths
produce three different results for m285 of the composing_tests
catalog (notes D5, A#4, F#4, C4):
- Status bar: Csus(add9)
- Right-click menu: Cm7b5
- Annotation: empty

Verdict: [α structural / β presentation / γ edge-case formatting]

Recommends [fix shape] to address the divergence.

Identifies a separate finding on the unconventional Csus(add9)
label that the formatter produces for this chord identity.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Verdict (α/β/γ or mix) with one-sentence evidence summary
- The most surprising finding from Q1-Q6 (if any; "nothing
  surprising" is itself a finding)
- Recommended fix shape (focused single-function fix vs.
  follow-up phase vs. accept-as-edge-case)
- Whether divergence C duration gate is the cause of empty
  annotation at m285 (yes / no / can't tell from code reading)
- Any deviations from this prompt and why

---

## Scope guardrails

- **Do not** modify any source file. The only file written this
  session is `docs/three_paths_divergence_recon.md`.
- **Do not** run the build or tests. Pure code-and-history
  reading. If empirical verification is needed (e.g., to
  confirm `chordResults` content), recommend it as a follow-up
  step rather than performing it here.
- **Do not** propose code changes in the report — fix prompts
  come after, informed by the verdict.
- **Do not** speculate beyond what the code shows. "I can't
  determine this from code alone" is a valid finding;
  confidently-wrong guesses are worse than honest uncertainty.
- **Do not** treat the chord-identity ambiguity as the divergence
  cause. The chord supporting multiple labels doesn't excuse
  three unified paths producing different ones. The recon's
  question is "why do unified paths diverge," not "is the chord
  ambiguous."
- **Do not** confuse the empty-annotation case (likely divergence
  C) with the status-bar-vs-right-click divergence (the
  architectural question). They're separate findings; the recon
  characterizes both.
