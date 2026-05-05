# Recon — `formatSymbol()` Per-Quality Branch Audit

**Scope:** Read-only investigation. No source edits, no build, no
tests. Systematically audit `formatSymbol()` in
`src/composing/analysis/chord/chordanalyzer.cpp` to identify any
per-quality branches that fail to consume detection flags
`detectExtensions()` produces. Three bugs of this class have been
closed in 2026-04 (commits `59f65d569f`, `da68035054`,
`e529b736a1`); the audit is a forward-looking sweep to find any
remaining cases before they surface as user-visible bugs.

This recon mirrors the precedent of the divergence-D recon
(commit `d35f003aa2`) and Phase 4/5 recons — citation-heavy,
verdict-driven, recommendation-based.

**Reference docs (read first):**
- Memory: `project_format_symbol_per_quality_bugs` — pattern
  description and the three closed bugs as precedent
- `src/composing/analysis/chord/chordanalyzer.cpp` — the formatter
  function being audited
- `src/composing/tests/chord_mismatch_report.txt` — current report;
  the 4 remaining RealDiff entries are non-formatter cases (vocab
  mismatches), confirming the catalog isn't surfacing the audit's
  potential targets

**Memory references** (auto-loaded):
- `project_format_symbol_per_quality_bugs` — the pattern this
  audit investigates
- `project_no_stripping_in_production` — analyzer outputs maximal;
  ignored detection flags are reductions, violating principle
- `project_chord_symbol_ban` — analyzer reads notes only; this
  audit doesn't change that

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

### Q1 — Enumerate `formatSymbol()`'s per-quality branches

Read `formatSymbol()` in
`src/composing/analysis/chord/chordanalyzer.cpp` and identify
every per-quality branch. Likely structure: `switch` on chord
quality (Major, Minor, Diminished, Augmented, HalfDiminished,
Major7, Minor7, Dominant7, MinorMajor7, etc.) with a code block
per case.

For each branch, capture:
- Quality name
- Line range
- Brief description of what the branch produces (e.g., "appends
  '7' suffix and consults extension flags X, Y, Z")

Produce a table of branches. This is the ground truth for the
audit — every flag-handling decision must be traceable to a
specific branch.

### Q2 — Enumerate `detectExtensions()`'s output flags

Read `detectExtensions()` (typically called before `formatSymbol`)
and identify every flag/field on its output struct (or whatever
structure carries the detected extensions/alterations into
`formatSymbol`). Likely flags:

- Ninth: natural / flat / sharp
- Eleventh: natural / sharp
- Thirteenth: natural / flat
- Sus2 / sus4
- Possibly add4 / add6 / add9
- Possibly other altered tones

Produce a table of flags and what each represents.

### Q3 — Cross-reference: which flags does each branch consume?

For each (quality, flag) pair, determine whether the corresponding
per-quality branch in `formatSymbol()` consumes the flag.
"Consumes" means either:
- Reads the flag and emits corresponding output text, OR
- Reads the flag and deliberately suppresses output (with a clear
  reason — e.g., this flag is structurally redundant for this
  quality)

Produce a matrix: rows = qualities, columns = flags, cells = one
of:
- ✓ — consumed, emits expected output
- — — consumed, deliberately suppressed (with reason)
- ✗ — NOT consumed; flag would be silently dropped if set

The ✗ entries are the audit findings — potential bugs of the same
class as the three closed cases.

### Q4 — Investigate each ✗ to determine if it's a real bug

For every ✗ in the matrix, determine whether it's:
- **Real bug:** flag would meaningfully appear in real music with
  that quality, but the branch ignores it. Same class as the three
  closed cases.
- **Acceptable gap:** flag never appears with that quality in
  practice (e.g., a Major triad can't have a b9 by definition;
  the b9 flag would never be set on a Major-quality chord), or
  the flag is structurally redundant.
- **Uncertain:** can't determine from code alone; would need
  empirical evidence.

For real-bug cases, report:
- Quality name and flag name
- Why this combination occurs in real music (briefly — e.g.,
  "Cmaj7add6 is a real chord type that some scores notate")
- Severity guess: high (common chord pattern), medium (occasional
  use), low (rare/edge-case)

### Q5 — Synthesis: are there hidden bugs?

Based on Q1-Q4, summarize:

- Total branches: N
- Total flags: M
- Total (branch, flag) pairs: N×M
- ✓ pairs (consumed correctly): X
- — pairs (deliberately suppressed): Y
- ✗ pairs (silently dropped): Z
- Of the Z ✗ pairs:
  - Real bugs: A (these are bugs to fix)
  - Acceptable gaps: B (no action)
  - Uncertain: C (flag for empirical follow-up if value justifies)

The "real bugs" count is the audit's actionable output. If A is 0,
the formatter is consistent and the three closed bugs are the
extent of this class. If A > 0, those become specific fix targets
ranked by severity.

---

## Deliverable

Write a single report file at `docs/format_symbol_audit.md` with
sections matching Q1-Q5. Concise and citation-heavy — every
claim backed by file:line. Total length: probably 3-5 pages of
markdown with the matrix as a table.

Suggested skeleton:

```markdown
# formatSymbol() Per-Quality Branch Audit

Date: 2026-04-26
Scope: read-only, no source edits.
Base commit: `e529b736a1`

## Verdict

[Total real-bug count A; severity distribution; recommended next
actions]

## Q1 — Per-quality branches

[Table of branches with line ranges and brief descriptions]

## Q2 — Detection flags

[Table of flags and what each represents]

## Q3 — Branch × flag consumption matrix

[Matrix with ✓ / — / ✗ cells, citations]

## Q4 — Real-bug analysis

[Per ✗: classification (real-bug / acceptable / uncertain) with
evidence and severity]

## Q5 — Synthesis

[Counts, recommendation]
```

---

## Commit + push

Single commit, just the recon report. Suggested message:

```
Recon: formatSymbol() per-quality branch audit

Systematic read-only audit of formatSymbol()'s per-quality branches
to identify any branches that fail to consume detection flags
detectExtensions() produces. Background: three commits
(59f65d569f, da68035054, e529b736a1) closed missing-extension
bugs of this class; audit is forward-looking to find any
remaining cases before they surface as user-visible bugs.

Findings: [A] real bugs identified (severity: [N high / M medium /
K low]); [B] acceptable gaps (e.g., flag never appears with that
quality in practice); [C] uncertain cases flagged for empirical
follow-up.

[If A == 0]: the formatter is consistent across qualities and
the three previously-closed bugs were the extent of this class.

[If A > 0]: ranked list of fix targets by severity. Each is a
focused per-branch fix similar to the three closed precedents
(typically 3-5 lines).
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Real-bug count (A) with severity distribution
- Most surprising finding (e.g., a flag that's silently dropped
  on a chord quality common in real music; or alternatively, "no
  surprises — the formatter is consistent")
- Any uncertain cases flagged for empirical follow-up
- Any deviations from this prompt and why

---

## Scope guardrails

- **Do not** modify any source file. The only file written this
  session is `docs/format_symbol_audit.md`.
- **Do not** run the build or tests. Pure code reading.
  Empirical verification of uncertain cases is out of scope; flag
  them for follow-up rather than running test code.
- **Do not** propose code changes in the report — fix prompts come
  after, informed by the audit's verdict.
- **Do not** speculate beyond what the code shows. "I can't
  determine this from code alone" is a valid finding.
- **Do not** confuse the absence of detection logic for a flag
  with a formatter bug. If `detectExtensions()` doesn't compute a
  particular flag for a particular quality, the formatter
  obviously can't consume what's not produced. The audit looks
  for cases where detection produces a flag and the formatter
  drops it — not for missing detection.
- **Do not** broaden scope to other formatter functions
  (`romanWithInversion`, `nashvilleNumberFormatter`, etc.). Audit
  is `formatSymbol()` specifically; siblings are separate audits
  if pursued.
- **Do not** propose refactor of `formatSymbol()`'s per-quality
  structure. Even if the audit reveals many ✗ pairs, a
  per-quality refactor is a significant change that warrants its
  own design conversation. The audit's job is to surface the
  current state; refactor decisions follow separately.
