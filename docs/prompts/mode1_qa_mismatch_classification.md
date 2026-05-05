# Mode 1 QA Prep — Classify the 135 Symbol/Roman Mismatches

**Scope:** Read the composing_tests mismatch report, classify the
135 symbol/roman mismatches by failure pattern, produce a
categorized summary that makes a future joint QA session efficient.
This is read-only diagnostic work — no analyzer changes, no catalog
changes, no fix attempts.

**Background:** `composing_tests` currently passes 376/376 with
mismatch baseline `abstract=0, symbol/roman=135`. The 135 are cases
where the analyzer's symbolic/roman-numeral output disagrees with
the test catalog's ground truth. They've been a stable baseline
through the entire unified-pipeline refactor (refactor preserved
analyzer behavior; mismatch count never moved). Vincent wants to
understand what's in those 135 before deciding which subsystems to
target for analyzer improvement work.

**Output:** A single markdown report at
`docs/mismatch_classification.md`, structured for a future joint QA
session where Vincent walks through categories and decides per
category whether the analyzer is wrong, the catalog is wrong, or
the case is genuinely ambiguous.

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin.
3. Force rebuild (`setup_and_build.bat`) and verify fresh binary
   timestamps.
4. Run composing_tests fresh to ensure the mismatch report reflects
   current code:
   `cd C:\s\MS\ninja_build_rel && ./composing_tests.exe`
   Confirm 376/376 pass and the report header shows
   `abstract=0, symbol/roman=135`. If counts differ, stop and
   surface — something has changed and we want to investigate
   before classifying.

---

## Step 1 — Read and characterize the report

File: `src/composing/tests/chord_mismatch_report.txt`

Read it end-to-end. Before classifying, characterize:
- What fields does each mismatch entry contain? (E.g. expected
  symbol, actual symbol, score name, measure, beat, key context,
  notes sounding, …)
- How are entries delimited and structured?
- Is there any existing grouping / sectioning in the report?

Surface this characterization briefly in the final report's
"Source format" section — it documents what the classification
worked from.

---

## Step 2 — Propose classification axes from the data

Look at the 135 entries and propose grouping axes that the data
actually supports. Suggested starting axes (not exhaustive — let
the data guide what's useful):

- **Failure type:** wrong root, wrong quality, wrong inversion,
  wrong key, wrong mode, missing entirely, spurious entirely
- **Chord complexity:** simple triad / seventh chord / extension
  (9th, 11th, 13th, sus, alt) / slash chord
- **Voicing density:** dense (4+ simultaneous notes) / sparse
  (1–2 notes) / monophonic
- **Position:** downbeat / weak beat / sub-beat
- **Style/composer:** if score names indicate composer or genre
  (Bach chorale vs. Mozart sonata vs. modal jazz lead sheet etc.)
- **Key context:** major / minor / modal / chromatic /
  modulating

If an axis isn't well-supported by the data, drop it. If a
useful axis surfaces from the data that I didn't list, use it.
The point is to find the patterns the 135 actually have, not to
force them into pre-chosen buckets.

A mismatch can fall into multiple axes — that's fine, the report
should reflect overlap.

---

## Step 3 — Classify all 135

Walk through each entry and tag it on each axis. Capture per-axis
counts.

Look for clusters: if 40 of the 135 are "wrong quality on slash
chords in jazz pieces," that's a cluster worth surfacing as a
named pattern. Patterns the report should call out:

- Tight clusters (>10% of mismatches sharing a specific failure
  shape)
- Surprising patterns (e.g., a specific composer dominates a
  specific failure type)
- Cases that look genuinely ambiguous on the face of it (e.g.,
  the catalog says X, the analyzer says Y, both look defensible
  from the notes alone)
- Cases that look like clear catalog errors (e.g., the catalog
  expects a chord that doesn't seem supported by the notes)
- Cases that look like clear analyzer failures (e.g., the
  analyzer produces something that's obviously wrong given the
  notes)

The "looks like X" judgments are first-pass impressions, not
verdicts — Vincent makes the actual calls in the joint QA session.
Mark them as impressions, not conclusions.

---

## Step 4 — Write the report

File: `docs/mismatch_classification.md` (new).

Suggested structure:

```markdown
# Symbol/Roman Mismatch Classification

Date: [today]
Source: `src/composing/tests/chord_mismatch_report.txt`
   (post-build run, baseline 0/135 abstract, 135/135 symbol/roman)

## Summary

[2–3 sentence top-line: what the 135 mismatches look like as a
group, the dominant pattern(s), the cleanest improvement
opportunities]

## Source format

[Brief description of what each entry in the mismatch report
contains, how entries are delimited]

## Classification axes

[The axes used and their justification — short]

## Pattern summary

| Pattern | Count | % | First-pass impression |
|---|---:|---:|---|
| [pattern name] | [N] | [%] | [impression: clear analyzer failure / clear catalog issue / genuinely ambiguous / mixed] |

## Per-pattern detail

### [Pattern 1 name] — [N entries, X%]

[Description of the pattern. What the entries look like.
Representative examples (3–5). First-pass impression with
reasoning. Subsystems the pattern points at if it's an analyzer
failure.]

### [Pattern 2 name] — [N entries, X%]

[…]

## Cross-axis observations

[Any notable correlations: e.g., "All 'wrong inversion' cases are
in works with figured bass written out" — patterns that wouldn't
show up looking at one axis alone]

## Full enumeration (grouped by primary pattern)

[Every one of the 135 entries listed under its primary pattern.
This section is for the joint QA session — Vincent will walk
through these. Per-entry: score name, measure/beat, expected,
actual, one-line note if relevant.]

## Suggested QA session flow

[A proposed order for the joint review: hardest/most-impactful
clusters first, easy/clear cases batched at the end. The point is
to make the human session efficient.]
```

Adjust the structure if the data suggests something better, but
keep both the summary view (table at top) and the full enumeration
(at bottom) — both serve different purposes.

---

## Commit + push

Single commit, only after the report is written and looks coherent
on a re-read. Suggested message:

```
Mode 1 QA prep: classify 135 symbol/roman mismatches

Read-only classification of the chord_mismatch_report.txt baseline
into pattern groups, with first-pass impressions per group. Output
at docs/mismatch_classification.md is structured for a future joint
QA session where each pattern gets a verdict (analyzer-fix /
catalog-fix / genuinely-ambiguous / no-action).

No source code touched; baseline 376/376 pass, 0/135 abstract,
135/135 symbol/roman preserved.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Top-level summary: how many distinct patterns emerged, the
  three biggest by count, the most surprising finding (if any)
- Number of cases that look like clear analyzer failures vs.
  clear catalog issues vs. genuinely ambiguous (your first-pass
  impressions, not verdicts)
- Any deviations and why
- Anything you noticed that wasn't a mismatch but seemed worth
  flagging (e.g., test infrastructure quirks, report-format
  oddities)

---

## Scope guardrails

- **Read-only.** Do not modify any source file under
  `src/composing/`. Do not modify the catalog XML
  (`chordanalyzer_catalog.musicxml`). Do not modify any test
  file. The CLAUDE.md autonomous-operation authorization for
  mismatch-reduction work does NOT apply to this prompt — this
  is classification, not reduction.
- **No fixes.** Even if a mismatch looks trivially fixable, do
  not fix it. Note the observation in the report, leave the code
  alone. Vincent decides per pattern whether and how to act.
- **No catalog changes.** Even if the catalog looks wrong on a
  specific entry, do not modify it. Note as "looks like catalog
  issue" and leave alone.
- **No analyzer behavior change.** Mismatch count must stay at
  exactly 135 throughout.
- **Only file written:** `docs/mismatch_classification.md`. No
  other doc updates, no test additions, no CMake changes.
- **First-pass impressions only.** "Looks like X" is an
  impression, not a verdict. Phrasing matters: "appears to be a
  catalog issue" is fine; "this is a catalog bug, fix it" is
  out-of-scope.
