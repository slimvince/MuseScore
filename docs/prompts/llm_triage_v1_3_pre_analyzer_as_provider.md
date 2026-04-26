# LLM-Triage v1.3-pre — Analyzer as Provider (JSON Emitter)

**Scope:** Extend the v0 C++ binary `tools/llm_triage/llm_triage.cpp`
to emit a fourth artifact per score —
`<basename>.analyzer_response.json` — alongside the existing three
`.txt` files. The new file holds **our analyzer's chord/key
judgments per region**, in a JSON schema compatible with the
LLM-side response files (`<basename>.{claude,gemini,openai}_response.json`)
so v1.3's comparator can read all four provider-agnostically.

This is the conceptual hinge: after v1.3-pre, the analyzer is "just
another voice" in the ensemble, with the same on-disk shape as the
LLMs. Future participants (specialized BERT classifiers per the
design doc) slot in at the same layer.

**Out of scope for v1.3-pre:**

- The comparator itself (analyzer-vs-LLM disagreement scoring,
  triage candidate ranking) — that's v1.3 proper, follows this.
- Any change to the Python wrapper `run_triage.py` — the analyzer
  JSON is C++-emitted on every binary invocation; LLM cache is
  unaffected.
- Multi-score batching — v1.4.
- Anything in `src/composing/` — read-only investigation OK,
  edits forbidden by pact.

If during implementation you find yourself wanting one of these,
**don't.** Note in the report-back as v1.3+ open questions.

**v1.2 baseline** (committed on `llm-triage` at `fb6400e05a`,
do not regress):

- Three LLM JSON files + three `.txt` files per score.
- Caching keyed on (score_content_hash, model, prompt_version,
  system_prompt_hash, tool_definition_hash).
- All three providers tested on Pachelbel; v1.2 verification
  passed.

After v1.3-pre:
- New file: `<basename>.analyzer_response.json` per score.
- Same `metadata + tool_input` top-level shape as LLM responses.
- Provider field: `"musescore_analyzer"`. Model field:
  `"chordanalyzer-v0"`.
- Existing `.txt` and `.json` files unchanged.

---

## Reference docs (read first)

- `tools/llm_triage/llm_triage.cpp` — the v0 C++ binary you're
  extending. Read end-to-end before implementing. Particularly:
  - `emitAnalyzerOutput` (line 1480) — the existing text emitter
    you're paralleling. The new JSON emitter consumes the same
    `std::vector<AnalyzedRegion>` and `Score*` data.
  - `main()` (line 1548) — the four output blocks pattern. You
    add a fifth block (or rather, a fourth alongside the three
    existing).
  - The `openOut` lambda (line 1608) — your new file uses this.
  - `pitchName` (line 1220), `durationName` (line 1229),
    `measureBeat` (line 1248), `keyDisplayStr` (line 1459) —
    helpers you may reuse for measure/beat formatting in the
    JSON.
- `src/composing/analyzed_section.h` — `AnalyzedRegion`,
  `KeyArea`, `KeyModeAnalysisResult`, `KeySigMode` enum
  definitions. The `KeySigMode` enum names map directly to the
  LLM-schema `mode` enum values.
- `src/composing/analysis/chord/chordanalyzer.h` — **READ-ONLY
  investigation only.** Find the `ChordAnalysisResult` /
  `ChordIdentity` type definitions and identify what
  `normalizedConfidence` actually means. See "Confidence
  investigation" below.
- `tools/llm_triage/run_triage.py` (v1.2 final state) — for the
  exact LLM JSON output shape your schema must match. Specifically
  the `_base_metadata` function and the `output_json` dict
  construction in `main()`. Your analyzer JSON's `metadata` block
  should have the same field names where they apply.
- `outputs/pachelbel-canon-in-d-arr-hiromi-uehara.claude_response.json`
  (or any other LLM response in `outputs/`) — concrete reference
  for the schema your analyzer JSON should match.
- `docs/prompts/llm_triage_v1_2_caching_and_openai.md` — for
  the CLAUDE.md-override + parallel-work-pact you treat as
  ambient context.

---

## CLAUDE.md override and parallel-work pact

Same as prior sessions. CLAUDE.md is stale on `src/composing/`,
`ARCHITECTURE.md`, build commands. **This prompt overrides on
those points.**

**You may freely edit:**
- `tools/llm_triage/llm_triage.cpp` (the only file you write).
- `docs/prompts/llm_triage_*.md` (this prompt — copy from
  mainline to worktree and commit, see Step 1).

**You may READ (not edit):**
- `src/composing/analyzed_section.h`
- `src/composing/analysis/chord/chordanalyzer.h`
- `src/composing/analysis/chord/chord_symbol_formatter.h` (for
  the formatter API surface, in case you need it)
- Any other header in `src/composing/` for read-only
  investigation.

**You may NOT edit:**
- `src/composing/**` (any file)
- `src/notation/internal/**`, snapshot tests
- `ARCHITECTURE.md`, `STATUS.md`, `REFACTOR_DEDUPLICATION_PLAN.md`
- `docs/policy2_coalescing_map.md`,
  `docs/unified_analysis_pipeline.md`
- `tools/CMakeLists.txt` is unchanged in v1.3-pre — you do not
  add a new target, you extend the existing `llm_triage` target.

---

## Pre-flight

1. **Worktree and branch:**
   ```bash
   cd /c/s/MS-llm-triage
   git rev-parse --show-toplevel  # /c/s/MS-llm-triage
   git status -sb                 # ## llm-triage  (clean)
   git log --oneline -5
   ```
   Halt and surface if dirty or wrong branch.

2. **v1.2 binary still works:**
   ```bash
   /c/Qt/Tools/Ninja/ninja.exe -C /c/s/MS-llm-triage/ninja_build_llm_triage llm_triage
   ./ninja_build_llm_triage/llm_triage.exe \
     "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
     ./outputs
   ls -la outputs/  # should show 3 .txt files (notes_only, with_symbols, analyzer_output)
   ```
   Must succeed. If the binary has decayed, halt and surface.

---

## Confidence investigation (do this first)

Before implementing the JSON emitter, settle the question:
**what does `normalizedConfidence` actually mean?**

Background: in the v1.0 round we noticed `analyzer_output.txt`
shows confidence values in the 0.05-0.09 range across all
Pachelbel regions. The `hasAssertiveExposure` threshold per
`analyzed_section.h:99` is 0.8 — so 0.05 is way below assertive.
Either (a) Pachelbel really is genuinely low-confidence on every
region (implausible — it's textbook tonal music), (b)
`normalizedConfidence` is a different scale than 0-1, or
(c) the wrong field is being rendered.

**What to do:**

1. Read `src/composing/analysis/chord/chordanalyzer.h` to find
   the `ChordAnalysisResult` and `ChordIdentity` struct
   definitions.
2. Identify all confidence-like fields on those types
   (likely candidates: `normalizedConfidence`, `score`,
   `rawScore`, `confidence`, etc. — actual names depend on the
   header).
3. Note the documented or commented-on range/semantics of each.
4. Decide which field corresponds to "0-1 chord-call confidence"
   and which corresponds to other quantities.

**If `normalizedConfidence` is the right 0-1 field but Pachelbel
genuinely sits at 0.05-0.09:** that's a discovery worth surfacing
(may indicate the analyzer's normalization is too aggressive for
diatonic music). Map to ordinal anyway, but note it in
report-back.

**If `normalizedConfidence` is NOT the right field** (e.g., it's
actually a logit, a relative-rank score, or otherwise not
naturally 0-1): identify which field IS, document the finding,
and use that field for the JSON's confidence mapping. Also fix
the existing text emitter at `emitAnalyzerOutput` line 1534 to
use the correct field — that's a one-line edit in
`tools/llm_triage/llm_triage.cpp` and improves the existing
`.txt` output too.

**Halt-and-surface** if neither interpretation is conclusive
after reading the header — bring the question to Vincent with
specific field names + semantics so he can decide.

**Confidence ordinal mapping** (apply once you have the right
field):

| `confidence` ordinal | Numeric range (0-1 scale) |
|----------------------|---------------------------|
| `very_high`          | ≥ 0.80                    |
| `high`               | ≥ 0.60                    |
| `medium`             | ≥ 0.40                    |
| `low`                | ≥ 0.20                    |
| `very_low`           | ≥ 0.05                    |
| `abstain`            | < 0.05  OR  `!hasAnalyzedChord` |

If the field isn't naturally 0-1, propose an alternative mapping
in the report-back.

---

## Work order

### Step 1 — Bring this prompt into the worktree and commit

```bash
cd /c/s/MS-llm-triage
cp "/c/s/MS/docs/prompts/llm_triage_v1_3_pre_analyzer_as_provider.md" \
   "docs/prompts/llm_triage_v1_3_pre_analyzer_as_provider.md"
git add docs/prompts/llm_triage_v1_3_pre_analyzer_as_provider.md
git commit -m "LLM-Triage v1.3-pre: prompt file for analyzer-JSON session"
```

### Step 2 — Confidence investigation

Per the section above. Output: a written decision in your
report-back about which field to use and why. If the existing
`emitAnalyzerOutput` confidence rendering is wrong, fix it (one
line); the fix is in scope for this commit.

### Step 3 — Implement `emitAnalyzerJson`

Add a function parallel to `emitAnalyzerOutput`:

```cpp
static void emitAnalyzerJson(std::ostream& out,
                             const std::string& sourceBasename,
                             const std::string& sourcePath,
                             const std::vector<AnalyzedRegion>& regions,
                             const Score* score);
```

Use **QJsonDocument / QJsonObject / QJsonArray** for JSON
construction — Qt is already linked (no new dependency). Avoid
hand-rolling JSON; the escaping rules are easy to get wrong and
QJsonDocument writes valid output by default.

The JSON shape (must match the LLM-side schema as a superset):

```json
{
  "metadata": {
    "score_basename": "...",
    "score_path": "...",
    "score_content_hash": "<sha256-hex of score file bytes>",
    "requested_model": "chordanalyzer-v0",
    "provider": "musescore_analyzer",
    "model": "chordanalyzer-v0",
    "model_response_id": "deterministic-<sha256-of-inputs-truncated-16>",
    "prompt_version": "v1.3-pre",
    "system_prompt_hash": "",
    "tool_definition_hash": "",
    "timestamp_utc": "<ISO-8601 UTC>",
    "input_tokens": 0,
    "output_tokens": 0,
    "stop_reason": "completed"
  },
  "tool_input": {
    "judgments": [
      {
        "measure": <int 1-based, best-fit start measure>,
        "beat_range": "<best-fit human-readable, e.g. '1-2', '3-end'>",
        "tick_start": <int>,
        "tick_end": <int>,
        "chord_label": "<via ChordSymbolFormatter>",
        "chord_label_alternatives": [...],
        "key": "<e.g. 'D major'>",
        "mode": "<one of: Ionian, Dorian, ...>",
        "confidence": "<ordinal>",
        "reasoning": "Analyzer call from collected pitch-class set; no free-form rationale.",
        "tones_pc_set": "<e.g. 'D2 F#2 A3 D4'>"
      }
    ],
    "key_summary": "",
    "ambiguity_flags": [],
    "format_friction": ""
  }
}
```

Field-by-field notes:

- **`score_content_hash`** — SHA-256 of the score file's bytes.
  You'll need to compute this in `main()` (where the score path
  is available) and pass it into `emitAnalyzerJson`. Use
  `QCryptographicHash::Sha256` (Qt-native, no new dependency).
- **`model_response_id`** — deterministic for the analyzer (it
  always produces the same output on the same inputs). Compute as
  `"deterministic-" + first-16-hex-chars-of-SHA256(score_content_hash || regions_count_string)`.
  Anything stably derived from the inputs is fine — the goal is a
  unique-but-reproducible string.
- **`timestamp_utc`** — current UTC time at emission, ISO-8601
  format.
- **`input_tokens` / `output_tokens`** — both 0 for the analyzer
  (no tokens involved). Don't omit; downstream consumers should
  see the field with value 0.
- **`measure` and `beat_range`** — best-fit derivation from
  `r.startTick` / `r.endTick`. Use `locateMeasureByTick` (line
  313) and `measureBeat` (line 1248) helpers. For
  `beat_range`: format as `"<startBeat>-<endBeat>"` where
  endBeat is exclusive (or use `"3-end"` if the region runs to
  the measure end). Document your beat-range convention in a
  source comment so v1.3's comparator knows.
- **`tick_start` / `tick_end`** — raw analyzer tick boundaries
  (from `r.startTick` / `r.endTick`).
- **`chord_label`** — produced by
  `ChordSymbolFormatter::formatSymbol(r.chord, r.key.keySignatureFifths)`,
  same call as `emitAnalyzerOutput` line 1499.
- **`chord_label_alternatives`** — array of strings, one per
  entry in `r.alternatives`, formatted the same way. **Dedupe**
  against the primary `chord_label`: if an alternative formats
  to the same string as the primary, drop it. (The v1.0
  hand-paste round identified this as a quality issue —
  `[A, A]` is meaningless to the comparator.) Also dedupe
  against each other — `[F#m, F#m]` collapses to `[F#m]`.
- **`key`** — human-readable form (`"D major"`, `"A minor"`).
  Use `keyDisplayStr` (line 1459) or build similarly.
- **`mode`** — one of the LLM schema's enum values. Map from
  `KeySigMode` enum (in `analyzed_section.h`):
    - `Ionian` → `"Ionian"`
    - `Dorian` → `"Dorian"`
    - … and so on. Names already match.
- **`confidence`** — ordinal, derived per the mapping table in
  the Confidence investigation section.
- **`reasoning`** — fixed string per region (the analyzer
  doesn't produce free-form rationale). Suggested:
  `"Analyzer call from collected pitch-class set; no free-form rationale."`
  Same string for every region is fine.
- **`tones_pc_set`** — the actual sounding pitches the analyzer
  saw (same content as `pcSet` in `emitAnalyzerOutput` lines
  1503-1513). Optional **superset field** beyond what the LLMs
  produce, but useful for the comparator and for human
  inspection. Schema-compatibility: LLM responses won't have
  this field; the comparator should be tolerant of extra fields.

**`tool_input.key_summary`, `ambiguity_flags`, `format_friction`** —
empty strings / empty array. The analyzer doesn't produce these.
Leave the keys present so the JSON top-level shape matches the
LLM response files exactly.

### Step 4 — Wire `emitAnalyzerJson` into `main()`

After the existing block 3 (analyzer_output.txt at line 1635-1642),
add a fourth block:

```cpp
// File 4: analyzer_response (JSON, parallel to LLM responses)
{
    std::ofstream f = openOut("analyzer_response.json");
    if (f.is_open()) {
        emitAnalyzerJson(f, sourceBasename, sourcePath, regions, score);
    }
}
```

The `score_content_hash` should be computed once in `main()` near
where you already have `sourcePath` and the loaded score (line
~1591), since you need the file bytes. Pass it through to
`emitAnalyzerJson` as a parameter.

### Step 5 — Verification

Build and run:

```bash
cd /c/s/MS-llm-triage
/c/Qt/Tools/Ninja/ninja.exe -C ./ninja_build_llm_triage llm_triage
./ninja_build_llm_triage/llm_triage.exe \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
ls -la outputs/pachelbel-canon-*.{txt,json} | sort
```

Expected: 4 files for Pachelbel (3 `.txt` + the existing 3 LLM
`.json`s + the new analyzer JSON). All previous JSON files
unchanged (their cache keys haven't changed).

**Validate the new JSON:**

```bash
/c/s/MS/.venv/Scripts/python.exe -c "
import json
d = json.load(open('outputs/pachelbel-canon-in-d-arr-hiromi-uehara.analyzer_response.json'))
print('top keys:', list(d.keys()))
print('metadata keys:', list(d['metadata'].keys()))
print('tool_input keys:', list(d['tool_input'].keys()))
j = d['tool_input']['judgments']
print('judgments:', len(j))
print('first:', j[0])
from collections import Counter
print('confidence dist:', dict(Counter(je['confidence'] for je in j)))
"
```

Expected:
- `top keys`: `['metadata', 'tool_input']` (parity with LLM)
- `metadata keys`: same as LLM responses (same field names; extra
  field 'requested_model' equal to 'chordanalyzer-v0')
- `tool_input keys`: includes `judgments`, `key_summary`,
  `ambiguity_flags`, `format_friction`
- `judgments`: 77 entries (matching the v0 region count for
  Pachelbel)
- First judgment looks reasonable
- Confidence distribution shows variation (not 100% in one
  bucket — if it does, the mapping or the underlying field is
  questionable)

**Cross-check vs the existing `analyzer_output.txt`:**

Pick 3 regions (e.g., region 1, region 10, region 50) and verify
the JSON's `chord_label` matches the text file's `chord:` line
verbatim. The same `ChordSymbolFormatter` produces both, so they
should be identical.

**Run the v1.2 Python wrapper to confirm no regression:**

```bash
/c/s/MS/.venv/Scripts/python.exe tools/llm_triage/run_triage.py \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Expected: all three LLMs report CACHED. Zero API calls. Exit 0.
(The Python wrapper invokes the C++ binary, which now writes 4
files instead of 3 — but the LLM caching is unaffected because
the `notes_only.txt` content didn't change.)

Halt and surface if any verification step fails.

---

## Halt-and-surface protocol

Halt and surface to Vincent immediately if:

- The confidence-field investigation can't conclude — bring
  Vincent the field names you found + their semantics + your
  recommended choice for explicit decision.
- The new JSON's schema diverges from the LLM-response shape in
  any way besides the documented superset additions
  (`tick_start`, `tick_end`, `tones_pc_set`).
- The judgment count in the new JSON doesn't match the analyzer
  region count printed by stdout (`regions: <N>`).
- Re-running the v1.2 Python wrapper after this commit produces
  any non-CACHED line for the LLM providers (would mean cache
  invalidation, unintended).
- Anything in the implementation tempts you to edit a file
  outside `tools/llm_triage/`.

When halting, include: the exact step, command + output, the
relevant JSON content (truncated to 2KB if large), and your
candidate next actions for Vincent's decision.

---

## Commit and push

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/llm_triage.cpp
git status   # confirm: only llm_triage.cpp changed
git commit -m "LLM-Triage v1.3-pre: emit analyzer_response.json

C++ binary now writes a fourth artifact per score:
<basename>.analyzer_response.json

Schema is a superset of the LLM-side response shape: same
top-level metadata + tool_input structure, same field names where
applicable, with analyzer-specific additions (tick_start,
tick_end, tones_pc_set) for native granularity preservation.

Provider field 'musescore_analyzer'; model 'chordanalyzer-v0'.
Confidence mapped from <field-name-here> to the LLM-schema
ordinal (very_high/high/medium/low/very_low/abstain).

This sets up v1.3's comparator to read all four sources
(claude / gemini / openai / analyzer) provider-agnostically by
iterating over outputs/*.{provider}_response.json."
git push origin llm-triage
```

---

## Report-back format

```
## LLM-Triage v1.3-pre — session report

Branch: llm-triage @ <commit_sha>
Pushed to: origin/llm-triage  (yes/no)

### Files changed
- tools/llm_triage/llm_triage.cpp  (+<X>/-<Y>)

### Confidence investigation
- Field used for `confidence` ordinal mapping: <field_name>
- Documented range/semantics: <verbatim from header comment if any>
- Correction to existing emitAnalyzerOutput? <yes/no — describe>
- Surprises in the field semantics: <list>

### v1.3-pre verification on Pachelbel
- analyzer_response.json: <size, judgments count, valid JSON yes/no>
- Confidence distribution across 77 regions:
    very_high: <N>
    high:      <N>
    medium:    <N>
    low:       <N>
    very_low:  <N>
    abstain:   <N>
- Cross-check vs analyzer_output.txt (3 spot regions):
    region 1:  txt_chord=<X>  json_chord=<Y>  match=<yes/no>
    region 10: ...
    region 50: ...

### v1.2 Python wrapper post-regression check
- claude:  CACHED  ✓
- gemini:  CACHED  ✓
- openai:  CACHED  ✓
- API calls made: 0

### First analyzer judgment (verbatim JSON object)
{
  ...
}

### Surprises / open questions for Vincent
- <list, brief>

### Mainline-pact compliance check
- Files touched outside tools/llm_triage/ + docs/prompts/llm_triage_*: <list — must be empty>
```
