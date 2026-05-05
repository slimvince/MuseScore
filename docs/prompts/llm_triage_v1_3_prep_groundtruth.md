# LLM-Triage v1.3-prep — Music21 Ground-Truth Converter

**Scope:** Two parallel deliverables in one CC session:

1. Add `tools/llm_triage/convert_music21_ground_truth.py` — a Python
   script that reads a music21-derived JSON (e.g.,
   `tools/corpus/bwv10.7.music21.json`) and writes a
   `<basename>.ground_truth_response.json` to the chosen output dir,
   matching the unified schema established by the LLM and analyzer
   response files.

2. Run the existing v1.2 LLM pipeline (`run_triage.py`) on
   `tools/corpus/bwv10.7.xml` so the four LLM/analyzer JSON files
   land alongside the new ground-truth JSON. After this session
   finishes, `outputs/bwv10.7.{claude,gemini,openai,analyzer,ground_truth}_response.json`
   all exist with compatible top-level shape — five sources for one
   Bach chorale. v1.3's comparator will be designed against this
   five-source dataset.

**Out of scope for v1.3-prep:**

- The comparator algorithm itself — that's v1.3.
- Triage queue output — v1.3.
- Multi-corpus or multi-chorale batching — v1.4 territory.
- Roman-numeral ingestion as a separate axis — music21 includes
  Roman numerals in its JSON, but our LLM-side schema doesn't have
  a Roman-numeral field. v1.3-prep uses the `chordSymbol` /
  `quality` fields for `chord_label`; Roman numerals are preserved
  in metadata only for now.
- Anything in `src/composing/`.

If during implementation you find yourself wanting to expand scope,
**don't.** Note in the report-back as a v1.3+ open question.

---

## Reference docs

- `docs/prompts/llm_triage_v1_3_pre_analyzer_as_provider.md` —
  parent prompt establishing the unified schema, CLAUDE.md
  override, and parallel-work pact. Read once if not loaded.
- `outputs/pachelbel-canon-in-d-arr-hiromi-uehara.analyzer_response.json`
  — concrete reference for the unified schema your converter must
  emit. The `metadata + tool_input` top-level shape, judgment
  fields, and metadata field names should match.
- `outputs/pachelbel-canon-in-d-arr-hiromi-uehara.claude_response.json`
  — same shape on the LLM side; useful for cross-checking field
  names.
- `tools/corpus/bwv10.7.music21.json` — your input. Schema:
  ```json
  {
    "source": "bwv10.7",
    "detectedKey": "g minor",
    "keyConfidence": 0.9074,
    "corpusName": "...",
    "regions": [
      {
        "measureNumber": 1, "beat": 1.0,
        "startTick": 0, "endTick": 960,
        "duration": 2.0,
        "rootPitchClass": 7, "quality": "Minor",
        "chordSymbol": "minor triad",
        "romanNumeral": "i",
        "key": "g minor", "keyGlobal": "g minor",
        "diatonicToKey": null, "alternatives": []
      },
      ...
    ]
  }
  ```
- `tools/llm_triage/run_triage.py` — for invoking the LLM pipeline
  on bwv10.7.xml in the verification step.

---

## CLAUDE.md override and parallel-work pact

Same as prior sessions. CLAUDE.md is stale on `src/composing/`,
build commands, etc. **This prompt overrides on those points.**
v1.3-prep doesn't touch any pact-protected paths.

**You may freely create/modify:**
- `tools/llm_triage/**` (new Python file is the only addition)
- `docs/prompts/llm_triage_*.md` (this prompt — copy from mainline
  to worktree and commit, see Step 1)

**You may NOT edit:**
- `src/composing/**`, `src/notation/internal/**`, snapshot tests
- `ARCHITECTURE.md`, `STATUS.md`, `REFACTOR_DEDUPLICATION_PLAN.md`
- `docs/policy2_coalescing_map.md`,
  `docs/unified_analysis_pipeline.md`
- The C++ binary (no changes needed)

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

2. **All three LLM API keys available** (the verification step calls
   the LLM pipeline). Same check as v1.1/v1.2:
   ```bash
   for var in ANTHROPIC_API_KEY GOOGLE_API_KEY OPENAI_API_KEY; do
     val="$(printenv "$var" || true)"
     if [ -z "$val" ]; then echo "$var: MISSING"; else echo "$var: set"; fi
   done
   ```
   Halt if any missing.

3. **Confirm the music21 input file exists:**
   ```bash
   ls -la /c/s/MS-llm-triage/tools/corpus/bwv10.7.music21.json
   ls -la /c/s/MS-llm-triage/tools/corpus/bwv10.7.xml
   ```
   Both must exist. Halt if either is missing.

4. **Confirm the v1.2 wrapper still works on Pachelbel** (cache hit
   only, no API spend):
   ```bash
   /c/s/MS/.venv/Scripts/python.exe tools/llm_triage/run_triage.py \
     "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
     ./outputs
   ```
   Expected: all three providers CACHED, exit 0. If not, halt and
   surface — something has decayed and we need to fix that first.

---

## Work order

### Step 1 — Bring this prompt into the worktree and commit

```bash
cd /c/s/MS-llm-triage
cp "/c/s/MS/docs/prompts/llm_triage_v1_3_prep_groundtruth.md" \
   "docs/prompts/llm_triage_v1_3_prep_groundtruth.md"
git add docs/prompts/llm_triage_v1_3_prep_groundtruth.md
git commit -m "LLM-Triage v1.3-prep: prompt file for music21 ground-truth converter"
```

### Step 2 — Implement `convert_music21_ground_truth.py`

Add at `tools/llm_triage/convert_music21_ground_truth.py`. CLI:

```
convert_music21_ground_truth.py <music21_json_path> <output_dir>
```

Output filename: `<basename>.ground_truth_response.json` where
`<basename>` is derived from the music21 input's `source` field
(e.g., `bwv10.7`).

**Output schema** (matches the unified shape; superset additions
clearly marked):

```json
{
  "metadata": {
    "score_basename": "bwv10.7",
    "score_path": "<absolute path of source xml/mscz, if findable; otherwise the music21_json_path>",
    "score_content_hash": "<sha256 of the source score file if findable; '' otherwise>",
    "requested_model": "music21-bach-chorales-v1",
    "provider": "music21_ground_truth",
    "model": "music21-bach-chorales-v1",
    "model_response_id": "deterministic-<sha256-of-music21-json-bytes>-truncated-16",
    "prompt_version": "v1.3-prep",
    "system_prompt_hash": "",
    "tool_definition_hash": "",
    "timestamp_utc": "<ISO-8601 UTC>",
    "input_tokens": 0,
    "output_tokens": 0,
    "stop_reason": "completed",
    "is_authoritative": true,
    "ground_truth_source": "music21",
    "music21_detected_key": "<verbatim, e.g. 'g minor'>",
    "music21_key_confidence": <float>
  },
  "tool_input": {
    "judgments": [
      {
        "measure": <int from measureNumber>,
        "beat_range": "<derived from beat + duration>",
        "tick_start": <int>,
        "tick_end": <int>,
        "chord_label": "<derived: see chord-label rules below>",
        "chord_label_raw": "<verbatim music21 chordSymbol>",
        "chord_label_alternatives": [],
        "key": "<from music21 key, normalized casing e.g. 'G minor'>",
        "mode": "<derived: Ionian/Aeolian/Dorian/etc>",
        "confidence": "very_high",
        "confidence_raw": 1.0,
        "reasoning": "Music21 ground-truth label.",
        "roman_numeral": "<verbatim from music21>",
        "diatonic_to_key": <bool or null>
      }
    ],
    "key_summary": "<verbatim music21 detectedKey field>",
    "ambiguity_flags": [],
    "format_friction": ""
  }
}
```

Two new metadata fields beyond the existing schema —
`is_authoritative: true` and `ground_truth_source: "music21"` —
mark this source as the authoritative reference for the comparator.
The LLM and analyzer responses don't have these fields; the
comparator treats the absence as `is_authoritative: false`.

Two new tool_input.judgment fields —
`chord_label_raw` (verbatim music21 prose) and
`roman_numeral` (verbatim) — preserve music21's original outputs
for audit. Schema is a superset; the comparator reads
`chord_label` for direct comparison and may use the others for
context.

**Chord-label derivation rules:**

```python
PC_TO_LETTER_FLATS = {
    0: "C", 1: "Db", 2: "D", 3: "Eb", 4: "E", 5: "F",
    6: "Gb", 7: "G", 8: "Ab", 9: "A", 10: "Bb", 11: "B",
}

def derive_chord_label(region):
    """Translate music21's region dict to a conventional chord symbol.

    Strategy: use rootPitchClass for the root letter, quality for the
    triad type, and chordSymbol's prose for extension info (7ths).

    Naive flat-default spelling. May produce occasional enharmonic
    mismatches with our analyzer's TPC-aware spellings (e.g., D#
    ground truth might print as Eb here). The comparator is expected
    to handle that as an interpretation question, not a bug.
    """
    pc = region.get("rootPitchClass")
    quality = region.get("quality", "")
    cs_prose = (region.get("chordSymbol") or "").lower()

    if pc is None or quality == "Unknown":
        return ""

    root = PC_TO_LETTER_FLATS[pc]

    # Recognize seventh extensions (check before triad fallback)
    if "dominant seventh" in cs_prose:
        return root + "7"
    if "half diminished" in cs_prose:
        return root + "m7b5"
    if "diminished seventh" in cs_prose and "incomplete" not in cs_prose:
        return root + "dim7"
    if "minor seventh" in cs_prose:
        return root + "m7"
    if "major seventh" in cs_prose:
        return root + "maj7"

    # Triad fallback
    if quality == "Major":
        return root
    if quality == "Minor":
        return root + "m"
    if quality == "Diminished":
        return root + "dim"

    return ""
```

For unrecognized `chordSymbol` strings (e.g., the more exotic ones
like "major-second minor tetrachord", "perfect-fourth minor
tetrachord"), fall through to the triad-fallback. Still better than
emitting empty string; the comparator can flag as a low-confidence
ground truth if it wants.

**Mode derivation:**

```python
KEY_MODE_MAP = {
    "major":     ("Ionian",   "{root} major"),
    "minor":     ("Aeolian",  "{root} minor"),
    "ionian":    ("Ionian",   "{root} major"),
    "dorian":    ("Dorian",   "{root} dorian"),
    "phrygian":  ("Phrygian", "{root} phrygian"),
    "lydian":    ("Lydian",   "{root} lydian"),
    "mixolydian":("Mixolydian","{root} mixolydian"),
    "aeolian":   ("Aeolian",  "{root} minor"),
    "locrian":   ("Locrian",  "{root} locrian"),
}

def parse_music21_key(key_str):
    """E.g. 'g minor' -> ('G minor', 'Aeolian')."""
    parts = (key_str or "").strip().split()
    if len(parts) != 2:
        return key_str, "other"
    raw_root, raw_mode = parts
    # Capitalize first letter; preserve trailing '#'/'b' if present
    letter = raw_root[0].upper()
    accidental = raw_root[1:] if len(raw_root) > 1 else ""
    root = letter + accidental
    mode_info = KEY_MODE_MAP.get(raw_mode.lower())
    if mode_info is None:
        return f"{root} {raw_mode}", "other"
    mode_name, key_template = mode_info
    return key_template.format(root=root), mode_name
```

**Beat-range derivation:**

```python
def beat_range_str(beat, duration):
    """E.g. (1.0, 2.0) -> '1-2'; (1.0, 4.0) -> '1-4'; (1.0, 1.0) -> '1'."""
    start = int(beat) if float(beat).is_integer() else round(beat, 3)
    end_inclusive_raw = beat + duration - 1
    end = int(end_inclusive_raw) if float(end_inclusive_raw).is_integer() else round(end_inclusive_raw, 3)
    if start == end:
        return f"{start}"
    return f"{start}-{end}"
```

Document the convention in a source-comment — `"1-2"` means "beats
1 through 2 inclusive within the measure," so a 2-beat region
starting on beat 1 is `"1-2"`. v1.3's comparator will need to know
this convention.

**Score-content hashing:**

If a `<basename>.xml` (or `.musicxml` / `.mscz`) sibling exists in
the same directory as the music21 JSON input, hash its bytes for
`metadata.score_content_hash`. If not findable, leave the field as
empty string and document with a comment in the script. (For
bwv10.7 the sibling `bwv10.7.xml` exists in `tools/corpus/`.)

### Step 3 — Verify the converter on bwv10.7

```bash
cd /c/s/MS-llm-triage
/c/s/MS/.venv/Scripts/python.exe tools/llm_triage/convert_music21_ground_truth.py \
  tools/corpus/bwv10.7.music21.json \
  ./outputs
```

Expected stdout (one line):

```
provider=music21_ground_truth  judgments=68  output=outputs/bwv10.7.ground_truth_response.json
```

Then **inspect the JSON** to validate schema parity:

```bash
/c/s/MS/.venv/Scripts/python.exe -c "
import json
gt = json.load(open('outputs/bwv10.7.ground_truth_response.json'))
ref = json.load(open('outputs/pachelbel-canon-in-d-arr-hiromi-uehara.claude_response.json'))
print('TOP KEYS:')
print(f'  gt:  {sorted(gt.keys())}')
print(f'  ref: {sorted(ref.keys())}')
print()
print('METADATA KEY DIFF (gt - ref) =', sorted(set(gt['metadata']) - set(ref['metadata'])))
print('METADATA KEY DIFF (ref - gt) =', sorted(set(ref['metadata']) - set(gt['metadata'])))
print()
print('TOOL_INPUT KEY DIFF (gt - ref) =', sorted(set(gt['tool_input']) - set(ref['tool_input'])))
print('TOOL_INPUT KEY DIFF (ref - gt) =', sorted(set(ref['tool_input']) - set(gt['tool_input'])))
print()
j = gt['tool_input']['judgments']
print(f'judgments count: {len(j)}')
print('first 3 judgments (chord_label only):')
for je in j[:3]:
    print(f\"  m{je['measure']:>3} b{je['beat_range']:<6}: {je['chord_label']:<6} (raw={je.get('chord_label_raw','')[:40]:<40} rn={je.get('roman_numeral','')[:8]})\")
print()
print(f'is_authoritative: {gt[\"metadata\"].get(\"is_authoritative\")}')
print(f'ground_truth_source: {gt[\"metadata\"].get(\"ground_truth_source\")}')
"
```

Expected:

- TOP KEYS identical: `['metadata', 'tool_input']` for both.
- METADATA KEY DIFF (gt - ref): includes `is_authoritative`,
  `ground_truth_source`, `music21_detected_key`,
  `music21_key_confidence`. No keys missing from gt that ref has.
- TOOL_INPUT KEY DIFF (gt - ref): empty (gt should have at least
  the same top-level keys as ref).
- 68 judgments.
- First three judgments' chord_labels are plausible:
  - region 1 (m1 b1-2, music21 says "minor triad" with rootPC=7
    in g minor, RN "i"): expected `chord_label: "Gm"`.
  - region 2 (m1 b3-4, "major triad" rootPC=5, RN "bVII6"):
    expected `chord_label: "F"`.
  - region 3 (m2 b1, "major triad" rootPC=10, RN "III"):
    expected `chord_label: "Bb"`.

If any check fails, **halt and surface** with the actual JSON
truncated to first 2KB.

### Step 4 — Run the LLM pipeline on bwv10.7.xml

```bash
cd /c/s/MS-llm-triage
/c/s/MS/.venv/Scripts/python.exe tools/llm_triage/run_triage.py \
  tools/corpus/bwv10.7.xml \
  ./outputs
```

Expected: three lines, all `provider=<X>  model=<Y>  judgments=<N> tokens=...`.
Three API calls (no cache hits; this is a new score). Approximate
spend: ~$1-2.

The C++ binary will also produce
`outputs/bwv10.7.{notes_only,with_symbols,analyzer_output}.txt` and
`outputs/bwv10.7.analyzer_response.json` automatically.

After this step, `outputs/` contains five JSON files for bwv10.7:

```
bwv10.7.analyzer_response.json
bwv10.7.claude_response.json
bwv10.7.gemini_response.json
bwv10.7.ground_truth_response.json
bwv10.7.openai_response.json
```

### Step 5 — Verify all five sources have compatible top-level shape

```bash
/c/s/MS/.venv/Scripts/python.exe -c "
import json, glob
files = sorted(glob.glob('outputs/bwv10.7.*_response.json'))
print(f'Files found: {len(files)}')
for f in files:
    d = json.load(open(f))
    top = sorted(d.keys())
    md_keys = sorted(d.get('metadata', {}).keys())
    ti_keys = sorted(d.get('tool_input', {}).keys())
    n = len(d.get('tool_input', {}).get('judgments', []))
    p = d.get('metadata', {}).get('provider', '?')
    auth = d.get('metadata', {}).get('is_authoritative', False)
    print(f'  {p:<25} judgments={n:<4} authoritative={auth} top_ok={top==[\"metadata\",\"tool_input\"]}')
"
```

Expected: 5 files, all `top_ok=True`. Only the ground-truth file
has `authoritative=True`. Judgment counts will differ by source
(LLMs typically produce per-measure or per-half-measure judgments;
analyzer produces per-region; ground-truth produces what music21
extracted).

If any file's top-level shape differs, **halt and surface**.

---

## Halt-and-surface protocol

Halt and surface to Vincent immediately if:

- Any music21 chordSymbol prose string falls outside the recognized
  list — confirm whether the fall-through-to-triad behavior is
  acceptable, or whether the converter needs additional rules. (For
  bwv10.7 specifically, the distinct strings are listed in this
  prompt's reference section; surface only if you encounter
  unrecognized ones.)
- The score-content-hash sibling file (`bwv10.7.xml`) is unfindable
  in the expected location. Surface; don't silently emit empty
  hash.
- The LLM pipeline run on bwv10.7 produces unexpected behavior
  (very different judgment counts than Pachelbel scaled, schema
  mismatches, API errors not handled by the existing v1.2 retry
  logic).
- Schema parity check fails (top-level keys, metadata field
  mismatches beyond the documented authoritative-source additions).
- Anything in the implementation tempts you to edit a file outside
  `tools/llm_triage/`.

When halting, include: the exact step, command + output, the
relevant JSON content (truncated to 2KB if large), and your
candidate next actions for Vincent's decision.

---

## Commit and push

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/convert_music21_ground_truth.py
git status   # confirm: only the new Python file added
git commit -m "LLM-Triage v1.3-prep: music21 ground-truth converter

Adds tools/llm_triage/convert_music21_ground_truth.py.

Reads a music21-derived JSON (the format produced by the existing
Bach chorale corpus runs in tools/corpus/) and emits a
<basename>.ground_truth_response.json matching the unified schema
established by the LLM and analyzer responses.

The output is a fifth provider in the same shape as the LLMs and
the analyzer, distinguished by metadata.provider =
'music21_ground_truth' and a new is_authoritative: true flag.
The schema is a strict superset on the analyzer side: adds two
metadata fields (is_authoritative, ground_truth_source,
music21_detected_key, music21_key_confidence) and two judgment
fields (chord_label_raw, roman_numeral, diatonic_to_key).

Verified on bwv10.7: 68 judgments emitted, schema parity confirmed
against pachelbel claude_response.json.

This sets up v1.3's comparator to read N voices provider-
agnostically with one optional voice flagged authoritative."
git push origin llm-triage
```

---

## Report-back format

```
## LLM-Triage v1.3-prep — session report

Branch: llm-triage @ <commit_sha>
Pushed to: origin/llm-triage  (yes/no)

### Files added
- tools/llm_triage/convert_music21_ground_truth.py  (<N> lines)

### Verification on bwv10.7

Converter step:
- Input: tools/corpus/bwv10.7.music21.json
- Output: outputs/bwv10.7.ground_truth_response.json
- judgments emitted: <N>
- music21 chordSymbol fall-through cases (if any): <list>

Schema parity:
- top-level keys match LLM responses: <yes/no>
- metadata diff vs LLM responses: gt-ref=<list>, ref-gt=<list>
- tool_input keys match: <yes/no>
- is_authoritative on ground_truth: <true/false>
- is_authoritative absent from other 4 sources: <yes/no>

First 3 ground-truth judgments:
- m1 b1-2: chord_label=<X> raw=<music21 chordSymbol> rn=<roman_numeral>
- m1 b3-4: chord_label=<X> raw=<...> rn=<...>
- m2 b1:   chord_label=<X> raw=<...> rn=<...>

LLM pipeline run on bwv10.7.xml:
- claude:   judgments=<N> tokens=<I>+<O>  cached=<Y/N>
- gemini:   judgments=<N> tokens=<I>+<O>  cached=<Y/N>
- openai:   judgments=<N> tokens=<I>+<O>  cached=<Y/N>
- analyzer: judgments=<N>  (C++ binary, always re-emits)
- approx total API spend: ~$<X>

Five-source consolidated check:
- 5 JSON files in outputs/ for bwv10.7: <yes/no>
- All 5 have top-level == ['metadata', 'tool_input']: <yes/no>
- Provider field of each: <list>

### Cross-source spot-check (m1 b1-2)
- ground_truth: <chord_label> (authoritative)
- analyzer:    <chord_label>
- claude:      <chord_label>
- gemini:      <chord_label>
- openai:      <chord_label>

### Cost log update needed
Yes — append a dated entry to docs/llm_triage_cost_log.md with the
v1.3-prep API spend on bwv10.7. (Don't update in this session; flag
for Vincent.)

### Surprises / open questions for Vincent
- <list, brief>

### Mainline-pact compliance check
- Files touched outside tools/llm_triage/ + docs/prompts/llm_triage_*: <list — must be empty>
```
