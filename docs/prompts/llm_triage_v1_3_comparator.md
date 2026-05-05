# LLM-Triage v1.3 — Comparator + Triage Queue

**Scope:** Add `tools/llm_triage/compare_triage.py`. Reads the
per-source response JSON files for one score (analyzer + 1–3 LLMs +
optional ground truth), bucketizes judgments by measure, computes
multi-axis agreement (root / quality / extension / inversion /
exact), classifies each measure-bucket into an issue type per the
taxonomy below, prioritizes, and emits a triage queue in two forms:
`<basename>.triage_queue.md` (human-readable, prioritized — what an
inspector reads) and `<basename>.triage_queue.json` (structured,
with empty verdict fields ready for the inspector to fill in).

The comparator is **provider-agnostic**: it iterates over
`outputs/<basename>.*_response.json` files in the output directory
and treats each as a "voice." Adding a new voice (plugin in v1.4,
specialized BERT in v2) requires no comparator changes — only a
new response file.

**Out of scope for v1.3:**

- Verdict-capture mechanism (CSV / JSON / Sheets sync) — v1.3.5
  decides this after one round of manual triage.
- Multi-score batching — v1.4.
- Registry consolidation across scores — v1.5.
- Plugin integration — v1.4 per the planned-scope doc.
- Specialized music-BERTs — v2.
- Anything in `src/composing/`.

If during implementation you find yourself wanting one of these,
**don't.** Note in the report-back as a v1.3.5+ open question.

**v1.3-prep baseline** (committed at `ceb415b858`, do not regress):

- All four/five provider response JSON files are produced for each
  score by the existing tooling: `run_triage.py` for the LLMs and
  the C++ binary's analyzer JSON, `convert_music21_ground_truth.py`
  for ground truth (when available).
- Pachelbel has 4 sources (no GT). bwv10.7 has 5 sources (with GT).
- All five files share the `metadata + tool_input` top-level shape,
  with `metadata.is_authoritative: true` only on the ground-truth
  file.

---

## Reference docs (read first)

- `docs/prompts/llm_triage_v1_3_prep_groundtruth.md` and
  `docs/prompts/llm_triage_v1_3_pre_analyzer_as_provider.md` —
  prior prompts establishing schema parity and the worktree
  conventions. Read once.
- `outputs/bwv10.7.*_response.json` — five source JSONs your
  comparator reads. Inspect the actual fields before designing
  the parser to avoid mismatched-assumption bugs.
- `outputs/pachelbel-canon-in-d-arr-hiromi-uehara.*_response.json`
  — four-source case (no GT). Comparator must run cleanly without
  a ground-truth file.
- `tools/llm_triage/run_triage.py` and
  `tools/llm_triage/convert_music21_ground_truth.py` for Python
  style precedent (argparse, output paths, error handling).

---

## CLAUDE.md override and parallel-work pact

Same as prior sessions. CLAUDE.md is stale on `src/composing/`,
build commands, etc. **This prompt overrides on those points.**
v1.3 is a Python-only chunk; no C++ touched, no build needed.

**You may freely create/modify:**
- `tools/llm_triage/**` (one new Python file is the only addition)
- `docs/prompts/llm_triage_*.md` (this prompt — copy from
  mainline to worktree and commit, see Step 1)

**You may NOT edit:**
- `src/composing/**`, `src/notation/internal/**`, snapshot tests
- `ARCHITECTURE.md`, `STATUS.md`, `REFACTOR_DEDUPLICATION_PLAN.md`
- `docs/policy2_coalescing_map.md`,
  `docs/unified_analysis_pipeline.md`
- `tools/CMakeLists.txt`

---

## Pre-flight

1. **Worktree and branch:**
   ```bash
   cd /c/s/MS-llm-triage
   git rev-parse --show-toplevel  # /c/s/MS-llm-triage
   git status -sb                 # ## llm-triage (clean)
   git log --oneline -5
   ```
   Halt and surface if dirty or wrong branch.

2. **Confirm input data exists:**
   ```bash
   ls outputs/pachelbel-canon-in-d-arr-hiromi-uehara.*_response.json | wc -l  # expect 4
   ls outputs/bwv10.7.*_response.json | wc -l                                  # expect 5
   ```
   Halt and surface if either is short.

3. **No API keys needed for v1.3.** The comparator is local-only —
   reads JSON, writes JSON+markdown. No LLM or other API calls.

---

## Work order

### Step 1 — Bring this prompt into the worktree and commit

```bash
cd /c/s/MS-llm-triage
cp "/c/s/MS/docs/prompts/llm_triage_v1_3_comparator.md" \
   "docs/prompts/llm_triage_v1_3_comparator.md"
git add docs/prompts/llm_triage_v1_3_comparator.md
git commit -m "LLM-Triage v1.3: prompt file for comparator session"
```

### Step 2 — Implement `compare_triage.py`

Add `tools/llm_triage/compare_triage.py`. CLI:

```
compare_triage.py <score_basename> <output_dir>
```

For example:
```
compare_triage.py pachelbel-canon-in-d-arr-hiromi-uehara ./outputs
compare_triage.py bwv10.7                                  ./outputs
```

The script:
1. Discovers all `<basename>.*_response.json` files in the
   output dir.
2. Loads each, validates `top_level == ['metadata', 'tool_input']`.
3. Bucketizes judgments by measure (per-source).
4. For each measure, computes per-axis agreement across sources
   and classifies the issue type.
5. Prioritizes the resulting list.
6. Emits `<basename>.triage_queue.md` and
   `<basename>.triage_queue.json` to the same output dir.

#### Bucketing and alignment

Source granularities differ (analyzer 46 / claude 56 / gemini 53 /
openai 65 / music21 68 on bwv10.7 — see v1.3-prep report). Don't
attempt index-based alignment. Use **measure-level bucketing**:

```python
def bucketize_by_measure(judgments):
    """Return {measure_int: [judgment_dicts]}."""
    out = {}
    for j in judgments:
        m = j.get('measure')
        if m is None:
            continue
        out.setdefault(m, []).append(j)
    return out
```

When a source has multiple judgments per measure (LLMs typically
emit per-half-measure or per-beat), use the *predominant* one for
single-cell comparison, but also record the within-measure
sub-disagreements. Cleanest definition: when a source's
within-measure judgments all share a chord_label, that's the cell
value. When they disagree internally (e.g., LLM says `Eb` for b1-2
and `F` for b3-4), emit two cells for that measure-source: one for
the half-measure split, with a `sub_measure_position` field.

Pragmatic v1.3 approach: emit one comparison per (measure,
beat_range) tuple where `beat_range` is the set of distinct
beat-ranges any source uses for that measure. Compare across
sources at each (measure, beat_range) cell. Tolerate slight
beat-range mismatches by overlap-matching: a source's "1-2"
judgment is matched against another source's "1-1" if the
intervals overlap. For v1.3 this can be approximate; v1.4+ may
introduce exact tick-overlap alignment if false matches become a
problem.

#### Chord-label canonicalization

Parse each `chord_label` into structured components for
multi-axis comparison:

```python
@dataclass
class ChordParts:
    root_pc: int          # 0-11, enharmonic-equivalent
    root_letter: str      # original spelling, e.g. "F#" or "Gb"
    quality: str          # one of {"maj", "min", "dim", "aug", "sus2", "sus4", "sus", "unknown"}
    has_seventh: bool     # whether a 7th extension is present
    has_minor_seventh: bool  # b7 specifically (vs maj7)
    extensions: set[str]  # tokens like {"9", "11", "13", "b9", "#11", "add9"}
    bass_pc: int | None   # slash-bass pitch class, None if no slash
    bass_letter: str | None
    raw: str              # original chord_label string
```

Parser must handle:
- Plain triads: `C`, `Cm`, `Cdim`, `Caug`
- Sevenths: `C7`, `Cm7`, `Cmaj7`, `Cm7b5`, `Cdim7`, `CmMaj7`
- Extensions: `C9`, `C11`, `C13`, `Cmadd9`, `Cmaj7#11`, `C7b9`,
  `C13b9#11`
- Suspended: `Csus`, `Csus2`, `Csus4`, `C7sus4`, `Asus269`,
  `A7sus4`, `A13sus`
- Slash chords: `D/F#`, `Gm/Bb`, `D/Gb` (treat enharmonic
  bass-note spellings as same `bass_pc`)
- Bizarre/non-standard: `Asus269` (analyzer's idiosyncratic
  output) — best-effort parse; if not parseable, set `quality =
  "unknown"` and surface in metadata.
- Empty string: `chord_label == ""` (the music21
  `quality=Unknown` case). Parser returns `None` for the whole
  ChordParts.

Use a small dictionary for the root + accidental ⇒ pitch class
mapping (case-insensitive root letter, support both `b` and `#`).
Document the parser conservatively — when in doubt, emit
`quality = "unknown"` rather than guessing wrong.

#### Multi-axis agreement

For a (measure, beat_range) cell with N parsed `ChordParts` from
N sources, compute these flags:

- `same_root_pc`: all non-None sources share `root_pc`.
- `same_quality`: all non-None sources share `quality`.
- `same_extension_class`: all share whether they have any
  seventh/extension at all (avoids treating `C` vs `C7` as
  identical, but doesn't penalize `C7` vs `C9`).
- `same_full_extensions`: all share the exact set of extension
  tokens.
- `same_inversion`: all share `bass_pc` (None counts as a value —
  i.e., "no slash bass" is a position, not absence-of-data).
- `exact_match`: all share `raw` string verbatim.

`None` ChordParts (empty chord_label, e.g. ground truth's
`quality=Unknown` regions) are excluded from agreement counts;
they don't establish disagreement on their own. The cell still
exists, just without that source's vote.

#### Issue-type taxonomy

Compute issue type per cell using a priority cascade. First match
wins.

| Priority | Issue type | Detection |
|----------|------------|-----------|
| 1 (highest) | `boundary_disagreement` | Sources have non-overlapping or wildly-different beat ranges within the measure. Detected at the bucketing layer, not per-cell. |
| 2 | `root_disagreement` | Cell has ≥2 distinct `root_pc` values across sources. |
| 3 | `quality_disagreement` | All same `root_pc`, but ≥2 distinct `quality` values. |
| 4 | `inversion_disagreement_with_gt` | All same root+quality, ≥2 distinct `bass_pc`, AND ground truth (if present) sides with one over the others. |
| 5 | `extension_disagreement_with_gt` | All same root+quality+inversion, ≥2 distinct extension sets, AND ground truth (if present) sides with one over the others. |
| 6 | `inversion_only` | Same root+quality, ≥2 distinct `bass_pc`, no ground truth (or GT silent). |
| 7 | `extension_only` | Same root+quality+inversion, ≥2 distinct extension sets, no ground truth (or GT silent). |
| 8 | `outlier_voice` | Special case: when N-1 sources agree exactly and 1 disagrees, flag separately even if the disagreement axis is "extension only." Useful inspector signal — points at the disagreer. |
| 9 (lowest) | `all_agree` | `exact_match` is true. Low-priority but include for completeness. |

#### Ground-truth handling

When a ground-truth source is present (`metadata.is_authoritative
== true`), per-cell add a flag:

```python
{
    "ground_truth_position": "matches_consensus" |
                              "matches_minority"  |
                              "out_of_alignment"  |
                              "absent",   # GT had no judgment for this cell
    "ground_truth_chord_label": "...",
    "non_gt_consensus_chord_label": "...",  # most common label among non-GT sources
}
```

`out_of_alignment` is the highest-value signal — ground truth
disagrees with all non-GT consensus. These cells should bubble to
the top of the priority list regardless of the issue-type
priority above. Add a `+5` priority boost (or equivalent) so they
outrank category-2 root-disagreements when both are present.

When no ground-truth source exists (Pachelbel case), all cells
have `ground_truth_position: "absent"` and the `+5` boost never
fires.

#### Priority ordering for the queue

Final priority score per cell = base priority (table above) ×
`-1` (so smaller is more urgent) + GT boost. Sort ascending. Ties
broken by measure number ascending.

Document the priority formula in source comments so v1.3.5+ can
tweak.

#### Output format

`<basename>.triage_queue.md` — markdown, the inspector's primary
read. Sketch (a real example follows the spec):

```markdown
# Triage Queue: <basename>

Sources: <list of provider names, ground-truth flagged>
Total cells: <N>
Flagged cells: <M>  (priority < <threshold>)
Generated: <ISO-8601 UTC>

## High priority

### 1. m<N> beats <range>: <issue_type>

| Source | chord_label | confidence | confidence_raw |
|--------|-------------|------------|----------------|
| ...    | ...         | ...        | ...            |

Suggested action: <inspector-actionable hint based on issue_type>

(repeat for each flagged cell)

## Medium priority
...

## Low priority
...

## All-agree (collapsed)

<count> cells where all sources agreed exactly, listed compactly:
m1 b1-2 (Gm), m1 b3-4 (F), ...
```

`<basename>.triage_queue.json` — structured twin. Same content,
plus empty verdict fields per cell:

```json
{
  "score_basename": "...",
  "generated_utc": "...",
  "sources": [
    {"provider": "musescore_analyzer", "is_authoritative": false, "model": "...", ...},
    ...
  ],
  "summary": {
    "total_cells": <N>,
    "flagged": <M>,
    "by_issue_type": {"all_agree": 12, "extension_only": 3, ...},
    "by_priority": {"high": 4, "medium": 8, "low": 11, "all_agree": 25}
  },
  "entries": [
    {
      "id": 1,
      "priority": "high" | "medium" | "low" | "all_agree",
      "priority_score": <numeric>,
      "issue_type": "...",
      "measure": <int>,
      "beat_range": "...",
      "tick_start": <int or null>,
      "tick_end": <int or null>,
      "sources": {
        "musescore_analyzer": {
          "chord_label": "...",
          "confidence": "...",
          "confidence_raw": <float or null>,
          "parsed": { "root_pc": ..., "quality": "...", "bass_pc": ... }
        },
        "claude":   { ... },
        "gemini":   { ... },
        "openai":   { ... },
        "music21_ground_truth": { ... }   # only present if 5-source
      },
      "axes": {
        "same_root_pc": true,
        "same_quality": true,
        "same_extension_class": false,
        "same_full_extensions": false,
        "same_inversion": false,
        "exact_match": false
      },
      "ground_truth_position": "matches_consensus" | "matches_minority" | "out_of_alignment" | "absent",
      "suggested_action": "...",
      "verdict": null,
      "verdict_chord_label": null,
      "verdict_notes": null,
      "verdict_user": null,
      "verdict_timestamp": null
    },
    ...
  ]
}
```

The verdict fields are deliberately empty — v1.3.5 designs the
capture mechanism (JSON edit / CSV / Sheets per the planned-scope
doc).

### Step 3 — Verify on Pachelbel (4 sources, no GT)

```bash
cd /c/s/MS-llm-triage
/c/s/MS/.venv/Scripts/python.exe tools/llm_triage/compare_triage.py \
  pachelbel-canon-in-d-arr-hiromi-uehara \
  ./outputs
```

Expected stdout (one line):

```
score=pachelbel-canon-in-d-arr-hiromi-uehara  cells=<N>  flagged=<M>  output=outputs/pachelbel-canon-in-d-arr-hiromi-uehara.triage_queue.md
```

Spot-check the markdown output:

- The known m9-b3-region "boundary disagreement" (analyzer collapses
  what LLMs split into 5 chord changes) appears in the high-priority
  section.
- m37 b3-4 (the known three-way split: Claude=`A`, Gemini=`Asus4`,
  OpenAI=`A7sus4`) appears as either `extension_disagreement` or
  `outlier_voice` depending on canonicalization.
- m5+ where all 4 sources agree appears collapsed in the
  all-agree section.

### Step 4 — Verify on bwv10.7 (5 sources with GT)

```bash
/c/s/MS/.venv/Scripts/python.exe tools/llm_triage/compare_triage.py \
  bwv10.7 \
  ./outputs
```

Expected: similar stdout shape. Spot-check:

- m1 b1-2: full 5-way agreement on `Gm`, all-agree section.
- m1 b3-4: GT says `F`, analyzer + Claude say `F/A`, Gemini +
  OpenAI say `F`. Should classify as
  `inversion_disagreement_with_gt` (priority 4 + GT-boost), with
  `ground_truth_position: "matches_minority"`.
- m2 b4: GT says `D`, analyzer says `D/Gb` (enharmonic of `F#`),
  three LLMs say `D/F#`. Comparator MUST recognize `Gb` and `F#`
  as same `bass_pc`. Issue type: same root+quality+inversion (after
  enharmonic normalization), so `extension_only` or `all_agree`
  depending on whether `D` (no slash) and `D/F#` (slash) are
  treated as same `bass_pc`. **Reasonable to treat `bass_pc =
  None` as different from `bass_pc = 6`** — that surfaces as
  `inversion_only`, which is correct: GT says no inversion, others
  say yes.
- m3 b3: GT/Gemini/OpenAI say `Bb`, analyzer says `Bbadd9`,
  Claude says `F/A`. Multiple things wrong simultaneously —
  comparator should classify as `root_disagreement` (Claude's
  `F/A` has root_pc=5, others have root_pc=10) and the GT-boost
  should push this near top of queue.
- m4 b2: GT has `chord_label=""` (quality=Unknown). Comparator
  must NOT mark this as `out_of_alignment` — GT is silent here.
  `ground_truth_position` should be `"absent"` for this cell.
- m5: full 5-way agreement on `Bb`, all-agree section.

Halt and surface if:
- Any cell's expected classification is wrong by an obviously-wrong
  amount (e.g., m1 b3-4 classifies as `all_agree`, or m3 b3
  classifies as `extension_only`).
- The chord-label parser fails to parse a label that any source
  actually emitted (it should at minimum produce
  `quality=unknown` rather than crash).
- Pachelbel verification produces fewer than ~5 high-priority cells
  or more than ~30 (we know there are real disagreements but not
  most cells should be flagged).

---

## Halt-and-surface protocol

Halt and surface to Vincent immediately if:

- Any source JSON file is missing or has unexpected schema.
- The chord-label parser can't handle a label any source emitted —
  surface with the specific label so Vincent can see whether it
  needs a parser extension or it's an analyzer/LLM bug.
- The priority cascade produces obviously-wrong classifications on
  the spot-checked cells above.
- The triage queue's high-priority section is empty for both
  scores (suggests the comparator isn't detecting any
  disagreements — likely a bug, given the data).
- The triage queue's high-priority section is huge (>40 entries
  per score) — suggests over-flagging, the priority/threshold
  needs tuning.
- Anything in the implementation tempts you to edit a file outside
  `tools/llm_triage/`.

When halting, include: the exact step, command + output, the
relevant cell content (truncated to 2KB if large), and your
candidate next actions for Vincent's decision.

---

## Commit and push

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/compare_triage.py
git status   # confirm: only the new Python file added
git commit -m "LLM-Triage v1.3: comparator + triage queue output

compare_triage.py reads N source-response JSON files for one
score (analyzer + LLMs + optional ground truth), bucketizes by
measure, computes multi-axis chord-label agreement (root,
quality, extension, inversion, exact), classifies each cell into
an issue-type per the documented taxonomy, and emits both
human-readable markdown (<basename>.triage_queue.md) and
structured JSON (<basename>.triage_queue.json) prioritized by
inspector-action urgency.

When a ground-truth source is present (is_authoritative: true on
metadata), the comparator distinguishes ground-truth-confirmed
agreement from ground-truth-contradicted disagreement and boosts
out-of-alignment cells to the top of the queue. Pachelbel
(4-source, no GT) and bwv10.7 (5-source, with GT) verified.

Verdict fields in the triage_queue.json are deliberately left
empty; v1.3.5 designs the capture mechanism (JSON edit / CSV /
Sheets sync) after one round of manual triage."
git push origin llm-triage
```

---

## Report-back format

```
## LLM-Triage v1.3 — session report

Branch: llm-triage @ <commit_sha>
Pushed to: origin/llm-triage  (yes/no)

### Files added
- tools/llm_triage/compare_triage.py  (<N> lines)

### Verification on Pachelbel (4 sources, no GT)
- cells: <N>
- flagged (priority < all_agree): <M>
- by_issue_type: <dict, e.g. {"all_agree": 25, "extension_only": 12, ...}>
- by_priority: <dict>
- High-priority cells (top 5 by priority): <list with measure/beat/issue_type>
- m37 b3-4 classification: <issue_type>  (expected: extension_disagreement or outlier_voice)

### Verification on bwv10.7 (5 sources with GT)
- cells: <N>
- flagged: <M>
- ground_truth out_of_alignment cells (sorted by priority, top 5): <list>
- m1 b3-4 classification: <issue_type>  (expected: inversion_disagreement_with_gt)
- m2 b4 enharmonic handling: analyzer's "D/Gb" recognized as same bass_pc as LLMs' "D/F#"? <yes/no>
- m3 b3 classification: <issue_type>  (expected: root_disagreement, GT-boosted)
- m4 b2 (empty GT): ground_truth_position = "absent"? <yes/no>

### Chord-label parser
- Total distinct labels parsed: <N>
- Labels that fell back to quality=unknown: <list, with source>

### Surprises / open questions for Vincent
- <list, brief>

### Mainline-pact compliance check
- Files touched outside tools/llm_triage/ + docs/prompts/llm_triage_*: <list — must be empty>
```

---

## Why this scope and not more

The verdict-capture mechanism (JSON edit / CSV / Sheets sync) is
deliberately deferred to v1.3.5, because the right answer depends
on what the friction actually feels like when working through
Pachelbel's queue manually once. Designing it pre-empirically would
just be a guess. v1.3 produces the queue; v1.3.5 watches you use it
and picks the capture friction-level you find livable.

The plugin integration (chordIdentifierPopJazz fork) is v1.4 — see
`docs/llm_triage_planned_scope.md` for the deferred design.

Multi-score batching is v1.4+. v1.3 deliberately handles one score
at a time so the comparator's logic gets exercised cleanly on
Pachelbel and bwv10.7 individually, before being subjected to
"runs across 20 scores in a row" stress.
