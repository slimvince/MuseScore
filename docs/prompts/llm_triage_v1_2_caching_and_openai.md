# LLM-Triage v1.2 — Response Caching + OpenAI Provider

**Scope:** Two changes to `tools/llm_triage/run_triage.py`:

1. **Skip-if-cached behavior.** Each provider's response file
   already carries metadata identifying the score, model, prompt
   version, system-prompt hash, and tool-definition hash. Use those
   five fields as a cache key. If a provider's response file already
   exists and matches the would-be cache key, **skip the API call**
   and reuse the existing file. A `--force-refresh` CLI flag
   overrides cache and re-calls all selected providers regardless.
   This realizes the design doc's "registry retains all opinions"
   model — opinions persist across runs, you don't re-pay for them.

2. **Add OpenAI as third provider.** Same shape as v1.1's Gemini
   addition. Same `INPUT_SCHEMA`, same `SYSTEM_PROMPT`, same
   `ProviderResult` return shape, per-provider failure isolation,
   forced function calling. Default model: whichever GPT model
   currently corresponds to "GPT-5 thinking" or the analytical
   reasoning tier — verify via OpenAI docs at v1.2 build time
   (halt-and-surface on the model-ID question, same protocol as
   v1.1's Gemini ID question).

**Out of scope for v1.2** (these are later iterations):

- Comparator (analyzer-vs-LLM disagreement scoring) — v1.3.
- Multi-score batch driver — v1.4.
- Registry consolidation — v1.5.
- Effort-tier metadata / per-model thinking-budget tracking — v2.
- Per-LLM track records / weighting — v2.
- Concurrent (parallel) API calls — v2 if it ever matters.

If during implementation you find yourself wanting one of these,
**don't.** Note in the report-back as a v1.3+ open question.

**v1.1 baseline** (committed on `llm-triage` at `5af1eaa81d`,
do not regress):

- `tools/llm_triage/run_triage.py` (535 lines) — Python wrapper
  with Claude + Gemini providers, per-provider failure isolation,
  exit codes 0/1/2.
- Output files: `<basename>.claude_response.json`,
  `<basename>.gemini_response.json`, plus the three v0 `.txt`
  artifacts.

After v1.2:
- New file: `<basename>.openai_response.json`.
- Cache-hit log lines (one per cached provider) in stdout.
- A new `<basename>.{provider}_response.json` is **only**
  rewritten when the cache key changes or `--force-refresh`
  is passed.

---

## Reference docs (read first)

- `tools/llm_triage/run_triage.py` — the v1.1 implementation.
  Read it end-to-end. Particularly:
  - `_base_metadata` (lines ~193-213) — already produces
    `system_prompt_hash` and `tool_definition_hash` you'll
    extend for the cache key.
  - `call_claude` (~220-289) and `call_gemini` (~290-393) —
    parallel structure to follow for `call_openai`.
  - `main()` (~398-531) — the per-provider loop where caching
    plugs in.
- `docs/prompts/llm_triage_v1_1_add_gemini_provider.md` — the
  v1.1 prompt (committed on this branch). Has the
  CLAUDE.md-override + parallel-work-pact you should treat as
  ambient context.
- `docs/llm_triage_design.md` — particularly the "Multi-LLM,
  parallel-as-async" and "Availability resilience" sections,
  which are what the caching pattern realizes.
- OpenAI Python SDK docs (web search if needed). Function calling
  with forced tool choice via `tool_choice={"type": "function",
  "function": {"name": TOOL_NAME}}`. The response shape is
  `response.choices[0].message.tool_calls[0].function.arguments`,
  which is a **JSON string** (not dict) — `json.loads` it before
  passing to `ProviderResult.tool_input`.

---

## CLAUDE.md override and parallel-work pact

Same as v1.0 / v1.1. CLAUDE.md is stale on `src/composing/`,
`ARCHITECTURE.md`, build commands. **This prompt overrides on
those points.** v1.2 doesn't touch any pact-protected paths.

May freely create/modify:
- `tools/llm_triage/**`
- `docs/prompts/llm_triage_*.md` (this prompt — copy from
  mainline to worktree and commit, see Step 1)

May NOT touch (full list in v0 prompt; review if uncertain):
- `src/composing/**`, `src/notation/internal/**`, snapshot tests
- `ARCHITECTURE.md`, `STATUS.md`, `REFACTOR_DEDUPLICATION_PLAN.md`
- `docs/policy2_coalescing_map.md`,
  `docs/unified_analysis_pipeline.md`

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

2. **All three API keys present:**
   ```bash
   for var in ANTHROPIC_API_KEY GOOGLE_API_KEY OPENAI_API_KEY; do
     val="$(printenv "$var" || true)"
     if [ -z "$val" ]; then echo "$var: MISSING"; else echo "$var: set ($(echo -n "$val" | wc -c) chars)"; fi
   done
   ```
   ANTHROPIC_API_KEY and GOOGLE_API_KEY are required to verify
   v1.1 still works after the refactor. If `OPENAI_API_KEY` is
   missing, halt and surface — Vincent gets it from
   `platform.openai.com → Settings → API keys → Create new`,
   then `setx OPENAI_API_KEY <value>` and a full VS Code restart
   (close all windows, verify no `Code.exe` in Task Manager,
   relaunch). OpenAI requires billing setup before keys work — a
   credit card on file with $5-10 loaded covers v1.2 and the
   validation round many times over.

   Do not read, log, commit, or print any key value.

3. **Python environment:** the venv used in v1.0/v1.1 (see top
   comment of `run_triage.py`). Verify the OpenAI SDK installs:
   ```bash
   <chosen_python> -m pip show openai 2>&1 | head -3
   <chosen_python> -m pip install openai
   ```
   `anthropic` and `google-genai` should already be there.

4. **v1.1 still works end-to-end** by running the script:
   ```bash
   cd /c/s/MS-llm-triage
   <chosen_python> tools/llm_triage/run_triage.py \
     "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
     ./outputs
   ```
   Expected: both providers OK, 154 judgments each, JSON files
   written. If v1.1 has decayed, halt and surface — don't paper
   over.

---

## Work order

### Step 1 — Bring this prompt into the worktree and commit

```bash
cd /c/s/MS-llm-triage
cp "/c/s/MS/docs/prompts/llm_triage_v1_2_caching_and_openai.md" \
   "docs/prompts/llm_triage_v1_2_caching_and_openai.md"
git add docs/prompts/llm_triage_v1_2_caching_and_openai.md
git commit -m "LLM-Triage v1.2: prompt file for caching + OpenAI session"
```

### Step 2 — Implement caching

Add a `score_content_hash` to the metadata block: SHA-256 of the
score file's bytes, computed once in `main()` from
`Path(score_path).read_bytes()`. Add it to the metadata dict
constructed when writing each provider's JSON.

Cache-key fields (a tuple of five strings):
- `score_content_hash`
- `model`
- `prompt_version`
- `system_prompt_hash`
- `tool_definition_hash`

Helper function:

```python
def _is_cached(json_path: Path, expected: dict) -> bool:
    """Return True if json_path exists with metadata matching all
    five cache-key fields. Error-stub responses (those with an
    'error' top-level field) are never treated as cached — they
    must always re-run.
    """
    if not json_path.exists():
        return False
    try:
        existing = json.loads(json_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    if "error" in existing:
        return False
    meta = existing.get("metadata", {})
    return all(meta.get(k) == v for k, v in expected.items())
```

In `main()`'s per-provider loop, **before** the API call:

```python
expected_cache_key = {
    "score_content_hash": score_content_hash,
    "model": model,
    "prompt_version": args.prompt_version,
    "system_prompt_hash": _sha256(SYSTEM_PROMPT),
    "tool_definition_hash": _sha256(json.dumps(TOOL, sort_keys=True)),
}

if not args.force_refresh and _is_cached(json_path, expected_cache_key):
    existing = json.loads(json_path.read_text(encoding="utf-8"))
    n = len(existing.get("tool_input", {}).get("judgments", []))
    print(f"provider={provider}  CACHED  judgments={n}  output={json_path}")
    skipped += 1
    continue
```

CLI flag:

```python
parser.add_argument(
    "--force-refresh",
    action="store_true",
    help="Re-call all selected providers, ignoring the cache.",
)
```

Tracking counter `skipped` alongside `succeeded` and `failed`.
Update the exit-code logic:
- 0 if `failed == 0` (regardless of skipped/succeeded mix).
- 1 if `failed > 0` and `(succeeded + skipped) > 0`.
- 2 if `failed > 0` and `succeeded + skipped == 0`.

(A run that's all cache-hits is exit 0 — nothing failed, even
though no API call happened.)

### Step 3 — Add OpenAI provider

Mirror `call_gemini`'s structure. Sketch:

```python
import openai

def call_openai(
    notes_only_text: str, model: str, max_tokens: int, prompt_version: str
) -> ProviderResult:
    client = openai.OpenAI()  # reads OPENAI_API_KEY from env

    tool_param = {
        "type": "function",
        "function": {
            "name": TOOL_NAME,
            "description": TOOL_DESCRIPTION,
            "parameters": INPUT_SCHEMA,
        },
    }

    last_exc = None
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": notes_only_text},
                ],
                tools=[tool_param],
                tool_choice={
                    "type": "function",
                    "function": {"name": TOOL_NAME},
                },
                max_completion_tokens=max_tokens,  # newer OpenAI param name
            )
            break
        except (openai.RateLimitError, openai.APIStatusError) as exc:
            last_exc = exc
            if attempt == 2:
                raise
            time.sleep([1, 4, 16][attempt])

    # Parse the forced tool call.
    msg = response.choices[0].message
    if not msg.tool_calls:
        raise RuntimeError("OpenAI response missing tool_calls")
    args_str = msg.tool_calls[0].function.arguments  # JSON string
    tool_input = json.loads(args_str)

    metadata = _base_metadata(
        provider="openai",
        model=response.model,  # actual model used (may include version suffix)
        response_id=response.id,
        input_tokens=response.usage.prompt_tokens,
        output_tokens=response.usage.completion_tokens,
        stop_reason=msg.tool_calls[0].finish_reason
                    if hasattr(msg.tool_calls[0], "finish_reason")
                    else (response.choices[0].finish_reason or ""),
        prompt_version=prompt_version,
    )
    return ProviderResult(tool_input=tool_input, metadata=metadata)
```

**Schema-shape gotchas to expect with OpenAI:**

- OpenAI's function calling supports "strict mode"
  (`"strict": true` in the function dict), which enforces the
  schema more rigidly. Try it; if it rejects something the
  shared `INPUT_SCHEMA` declares (e.g., extra type unions), turn
  it off — non-strict mode is still validated on the client side
  by the SDK on parse, just less strictly server-side. Either is
  acceptable.
- OpenAI's `max_completion_tokens` replaced `max_tokens` in
  newer SDK / API versions for chat completions. Use whichever
  the SDK currently expects (test with one parameter; if it
  rejects it, swap).
- Reasoning models (`o3`, `o4-mini`, etc.) may not support
  `tools` the same way as standard chat completions. If the
  default analytical-tier model is a reasoning model that
  doesn't support function calling, halt and surface — switch
  to a model that does, but only with Vincent's go.
- Some OpenAI models include reasoning-token usage in
  `response.usage`. If you can record it as a separate metadata
  field (e.g. `reasoning_tokens`), do so; if not, fold into
  output_tokens or omit. Note in the report-back which choice
  you made.

**Default model:** whichever OpenAI currently positions as their
analytical/reasoning-tier flagship. As of v1.2 build time,
candidates likely include `gpt-5`, `gpt-5-thinking`, `o3`, etc.
**Halt and surface** if the right model ID isn't obvious from
OpenAI's current docs — Vincent's hand-paste round used "GPT-5
thinking" in the chat picker, so we want the closest API model
to that.

### Step 4 — Wire OpenAI into `main()`

Add to the dispatch:

```python
_OPENAI_DEFAULT = "<determined-during-build-time>"

# add CLI flag
parser.add_argument(
    "--openai-model",
    default=_OPENAI_DEFAULT,
    help=f"OpenAI model ID (default: {_OPENAI_DEFAULT})",
)

# update default --providers
parser.add_argument(
    "--providers",
    default="claude,gemini,openai",
    help="Comma-separated list of providers (default: claude,gemini,openai)",
)

# update model_for
model_for = {
    "claude": args.claude_model,
    "gemini": args.gemini_model,
    "openai": args.openai_model,
}

# add to dispatch in the loop
if provider == "claude":
    pr = call_claude(...)
elif provider == "gemini":
    pr = call_gemini(...)
elif provider == "openai":
    pr = call_openai(notes_only_content, model, args.max_tokens, args.prompt_version)
else:
    raise ValueError(f"Unknown provider: {provider!r}")
```

### Step 5 — Bump `prompt_version` default

Bump the default value of `--prompt-version` from `"v1.1"` to
`"v1.2"`. This deliberately invalidates v1.1-cached responses
for the next run — v1.2 has different code (cache logic, new
provider) and a fresh run gives all three providers consistent
v1.2 metadata. Note in the commit message that v1.1 cached
responses won't survive the version bump — that's intentional.

(The existing claude_response.json and gemini_response.json
from v1.1 will be re-derived on the post-v1.2 run, but that's
3 API calls — acceptable cost for clean v1.2 metadata across
the trio.)

---

## Verification

Run a four-step verification on Pachelbel to exercise both
features:

**Run 1 — fresh v1.2 run** (no cache, all three providers):

```bash
cd /c/s/MS-llm-triage
rm outputs/pachelbel-canon-in-d-arr-hiromi-uehara.{claude,gemini,openai}_response.json 2>/dev/null
<chosen_python> tools/llm_triage/run_triage.py \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Expected: 3 lines, all `provider=<X>  model=<Y>  judgments=<N>  ...`.
All three response files written.

**Run 2 — cache validation** (no flags, no changes):

```bash
<chosen_python> tools/llm_triage/run_triage.py \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Expected: 3 lines, all `provider=<X>  CACHED  judgments=<N>  ...`.
Zero API calls. Exit 0.

**Run 3 — force refresh:**

```bash
<chosen_python> tools/llm_triage/run_triage.py \
  --force-refresh \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Expected: 3 lines, all `provider=<X>  model=<Y>  judgments=<N>  ...`.
Three API calls (force-refresh bypassed cache). Exit 0.

**Run 4 — partial cache** (one provider only):

```bash
<chosen_python> tools/llm_triage/run_triage.py \
  --providers openai \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Expected: 1 line, `provider=openai  CACHED  ...`. (Run 3
populated the cache for all three providers; only openai is
selected, and it should hit the cache.) Exit 0.

Then **inspect** the OpenAI response file specifically:

- `metadata.provider == "openai"`, `metadata.model` is the chosen
  model ID, `metadata.score_content_hash` matches the SHA-256 of
  the score file's bytes.
- `tool_input.judgments` has ≥30 entries.
- `tool_input.key_summary` says D major.
- `tool_input.format_friction` — read carefully, surface verbatim.
- `tool_input.judgments[0]` is for measure 1 with chord_label
  `D` (or close — Pachelbel openings are unambiguous).

Cross-spot-check vs Claude and Gemini files:

- m1 b1-2: all three should label `D`. (Confidence may differ.)
- m37 b3-4: this is the known disagreement region — Claude
  said `A`, Gemini said `Asus4`. OpenAI's call here is
  informative no matter what it says.
- m72 b1-2: chromatic walk — should be `E7` or close in all three.

If any verification step fails, **halt and surface** with the
relevant JSON content (truncated to 2KB if large) and the
specific assertion that failed.

---

## Halt-and-surface protocol

Halt and surface to Vincent immediately if:

- Any of the three API keys is missing or invalid.
- The OpenAI model-ID question is unclear after a brief docs
  check — don't guess.
- The default OpenAI analytical-tier model doesn't support
  function calling (e.g. it's a pure reasoning model with no
  tools support).
- The shared `INPUT_SCHEMA` needs adjustments to satisfy OpenAI
  that would force divergence from what Anthropic and Gemini
  accept. (Gemini's `minimum: 1` adjustment in v1.1 is precedent —
  a tweak both providers accept is fine; a fork is not.)
- Run 2 (cache validation) shows non-zero API calls when no
  flags are passed.
- Run 3 (force-refresh) shows any cached responses (every
  provider should re-call).
- Any provider returns judgment count under 30 on Pachelbel.
- Anything in the implementation tempts you to edit a file
  outside `tools/llm_triage/`.

When halting, include: the exact step, command + output, the
relevant JSON if applicable (truncated to 2KB if large), and
your candidate next actions for Vincent's decision.

---

## Commit and push

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/run_triage.py
git status   # confirm: only run_triage.py changed
git commit -m "LLM-Triage v1.2: response caching + OpenAI provider

Two changes to run_triage.py:

1. Skip-if-cached. Each provider's response file is treated as
   a cache entry keyed on (score_content_hash, model,
   prompt_version, system_prompt_hash, tool_definition_hash).
   Re-runs without --force-refresh skip API calls when the
   cache key matches, realizing the design doc's
   'opinions persist across runs' model. Error-stub responses
   are never cached.

2. Add OpenAI as third provider. Mirrors the v1.1 Gemini
   addition: same INPUT_SCHEMA, same SYSTEM_PROMPT, forced
   function calling, per-provider failure isolation.

Bumped --prompt-version default from v1.1 to v1.2; v1.1
cached responses will be re-derived on the next run, which is
intentional — v1.2 has different code paths and we want clean
v1.2 metadata across the trio."
git push origin llm-triage
```

---

## Report-back format

```
## LLM-Triage v1.2 — session report

Branch: llm-triage @ <commit_sha>
Pushed to: origin/llm-triage  (yes/no)

### Files changed
- tools/llm_triage/run_triage.py  (+<X>/-<Y>)

### Python environment
- openai version: <X.Y.Z>
- anthropic / google-genai unchanged from v1.1

### v1.2 verification on Pachelbel — four-run cache test

Run 1 (fresh):
- claude:  model=<id>  judgments=<N>  tokens=<I>+<O>
- gemini:  model=<id>  judgments=<N>  tokens=<I>+<O>
- openai:  model=<id>  judgments=<N>  tokens=<I>+<O>

Run 2 (cache validation, no flags):
- claude:  CACHED
- gemini:  CACHED
- openai:  CACHED
- API calls made: 0

Run 3 (--force-refresh):
- claude:  model=<id>  judgments=<N>  tokens=<I>+<O>  (re-called)
- gemini:  model=<id>  judgments=<N>  tokens=<I>+<O>  (re-called)
- openai:  model=<id>  judgments=<N>  tokens=<I>+<O>  (re-called)

Run 4 (--providers openai, no flags):
- openai:  CACHED

### OpenAI default model chosen
- <model_id>: <one-sentence rationale, e.g. "GPT-5-thinking analytical
  tier, closest match to hand-paste reference">

### Cross-model spot-check (m1, m37, m72)
- m1 b1-2:  claude=<X>  gemini=<Y>  openai=<Z>  agree=<all|2of3|none>
- m37 b3-4: claude=<X>  gemini=<Y>  openai=<Z>  agree=<all|2of3|none>
- m72 b1-2: claude=<X>  gemini=<Y>  openai=<Z>  agree=<all|2of3|none>

### format_friction (verbatim)
- Claude: "<verbatim>"
- Gemini: "<verbatim>"
- OpenAI: "<verbatim>"

### Schema adjustments (if any)
- <list any tweaks made to INPUT_SCHEMA so all three providers
  accepted it; verbatim diff or summary>

### Surprises / open questions for Vincent
- <list, brief>

### Mainline-pact compliance check
- Files touched outside tools/llm_triage/ + docs/prompts/llm_triage_*: <list — must be empty>
```
