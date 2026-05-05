# LLM-Triage v1.3-pre Patch — Add `confidence_raw` to analyzer JSON

**Scope:** Tiny addition to `tools/llm_triage/llm_triage.cpp`. Each
judgment object in `<basename>.analyzer_response.json` currently
carries an ordinal `confidence` field (`very_high` / `high` / ... /
`abstain`) derived from `ChordIdentity::normalizedConfidence`. Add a
`confidence_raw` field alongside it that emits the underlying 0-1
sigmoid value verbatim.

**Why:** The v1.3-pre investigation found that the analyzer's
sigmoid-normalized confidence is **calibration-honest** for tonal
music — when several chord templates score similarly (the diatonic
case), the score gap is small and confidence is correctly low. The
ordinal mapping (`< 0.05 → abstain`) discards information that v1.3's
comparator wants: it can't distinguish "score gap was 0.04" from
"score gap was 0.001," and that distinction matters for the
"notes-alone-ambiguous" issue type. Preserving the raw value alongside
the ordinal closes that gap.

**Out of scope:**

- Changing `confidenceSigmoidMidpoint` or any other analyzer
  preference — calibration is honest as-is, do not touch.
- Adding `confidence_raw` to the LLM response files — they don't
  produce a comparable scalar; their confidence is intrinsically
  ordinal. The schema is asymmetric on purpose; the comparator
  reads `confidence_raw` when present, falls back to the ordinal
  when not.
- Anything in `src/composing/`.

---

## Reference docs

- `docs/prompts/llm_triage_v1_3_pre_analyzer_as_provider.md` —
  parent prompt (committed). Establishes the
  CLAUDE.md-override + parallel-work-pact context. Read once if
  you don't have that loaded.
- `tools/llm_triage/llm_triage.cpp` — `emitAnalyzerJson` is the
  function this patch touches. Should be near the bottom of the
  file (added in v1.3-pre).

---

## Pre-flight

```bash
cd /c/s/MS-llm-triage
git rev-parse --show-toplevel  # /c/s/MS-llm-triage
git status -sb                 # ## llm-triage (clean)
git log --oneline -3           # last commit = v1.3-pre analyzer JSON
```

Halt and surface if dirty or wrong branch.

---

## The patch

In `emitAnalyzerJson` (introduced in v1.3-pre), wherever the per-region
JSON object is built and the ordinal `confidence` field is set, add a
parallel `confidence_raw` field with the **untransformed**
`r.chord.identity.normalizedConfidence` value (a `double` in `[0, 1]`).

Use `QJsonValue` with the double value directly — QJsonDocument
serializes it as a JSON number. Do **not** stringify the value; we
want a JSON number type for downstream consumers.

A reasonable placement near the existing `confidence` line:

```cpp
const double rawConfidence = r.chord.identity.normalizedConfidence;
judgment.insert("confidence", QString::fromStdString(confidenceOrdinal(rawConfidence)));
judgment.insert("confidence_raw", rawConfidence);
```

(Substitute `judgment` and `confidenceOrdinal` for whatever the actual
local names are in the v1.3-pre code — read the function and use
matching names.)

That's the only behavioral change. No new helpers, no new headers, no
schema-shape changes elsewhere.

---

## Verification

```bash
cd /c/s/MS-llm-triage
/c/Qt/Tools/Ninja/ninja.exe -C ./ninja_build_llm_triage llm_triage
./ninja_build_llm_triage/llm_triage.exe \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Then:

```bash
/c/s/MS/.venv/Scripts/python.exe -c "
import json
d = json.load(open('outputs/pachelbel-canon-in-d-arr-hiromi-uehara.analyzer_response.json'))
j = d['tool_input']['judgments']
print('judgment fields:', sorted(j[0].keys()))
print()
print('First 5 regions: ordinal vs raw')
for je in j[:5]:
    print(f\"  m{je['measure']:>3} b{je['beat_range']:<8}: {je['confidence']:<10} raw={je['confidence_raw']:.4f}\")
print()
print('Distribution check: confidence_raw range')
raws = [je['confidence_raw'] for je in j]
print(f'  min={min(raws):.4f}  max={max(raws):.4f}  count={len(raws)}')
print(f'  >= 0.80 (very_high): {sum(1 for r in raws if r >= 0.80)}')
print(f'  >= 0.05 to < 0.80:    {sum(1 for r in raws if 0.05 <= r < 0.80)}')
print(f'  <  0.05 (abstain):    {sum(1 for r in raws if r < 0.05)}')
"
```

Expected:

- `judgment fields` includes both `confidence` and `confidence_raw`.
- `confidence_raw` is a number, not a string.
- Distribution check matches v1.3-pre's reported ordinal distribution
  (1 very_high, 28 very_low, 48 abstain). `confidence_raw` should
  show the actual 0-1 spread underlying those buckets — values like
  0.034, 0.062, 0.087 in the abstain/very_low range, and one value
  near 0.85+ for the single very_high entry.

**Regression check** — v1.2 Python wrapper must still hit the cache:

```bash
/c/s/MS/.venv/Scripts/python.exe tools/llm_triage/run_triage.py \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Expected: claude / gemini / openai all `CACHED`. Zero API calls. The
LLM responses are unaffected by analyzer JSON schema additions.

If verification fails, **halt and surface** with the JSON content
truncated to the first 2KB and the specific assertion that failed.

---

## Halt-and-surface protocol

Halt and surface immediately if:

- The v1.3-pre `emitAnalyzerJson` function is hard to locate or has
  drifted — surface and don't guess at the right insertion point.
- `confidence_raw` ends up serialized as a string instead of a JSON
  number (would break v1.3 comparator expectations).
- The build fails for any reason.
- The post-patch run produces a different judgment count or any
  change to other judgment fields.
- Anything in the implementation tempts you to edit a file outside
  `tools/llm_triage/`.

---

## Commit and push

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/llm_triage.cpp
git status   # confirm: only llm_triage.cpp changed
git commit -m "LLM-Triage v1.3-pre patch: add confidence_raw to analyzer JSON

emitAnalyzerJson now emits a confidence_raw double alongside the
ordinal confidence string in each judgment object. confidence_raw
is the 0-1 sigmoid value from ChordIdentity::normalizedConfidence,
preserved verbatim. The ordinal mapping discards information
(everything below 0.05 collapses to 'abstain'); v1.3's comparator
wants the raw value to distinguish 'score gap was 0.04' from
'score gap was 0.001' for the notes-alone-ambiguous issue type.

Schema is now asymmetric: analyzer_response.json has
confidence_raw; LLM response files do not (their confidence is
intrinsically ordinal). The v1.3 comparator reads confidence_raw
when present and falls back to the ordinal otherwise."
git push origin llm-triage
```

---

## Report-back format

```
## LLM-Triage v1.3-pre patch — session report

Branch: llm-triage @ <commit_sha>
Pushed to: origin/llm-triage  (yes/no)

### Files changed
- tools/llm_triage/llm_triage.cpp  (+<X>/-<Y>)

### Verification on Pachelbel
- judgment fields includes confidence_raw: <yes/no>
- confidence_raw is a JSON number: <yes/no>
- First 5 regions (ordinal | raw):
  m<N> b<range>: <ordinal> raw=<X.XXXX>
  ...
- Distribution check (matches v1.3-pre):
    >= 0.80:        <N>
    0.05-0.80:      <N>
    <  0.05:        <N>

### v1.2 Python wrapper post-regression
- claude / gemini / openai all CACHED: <yes/no>
- API calls made: 0

### Surprises / open questions for Vincent
- <list, brief — likely none for a patch this small>

### Mainline-pact compliance check
- Files touched outside tools/llm_triage/: <list — must be empty>
```
