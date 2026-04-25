# LLM-Triage v1.1 — Add Gemini as Second LLM Provider

**Scope:** Refactor `tools/llm_triage/run_triage.py` (introduced in
v1.0) into a provider-agnostic shape and add Google's Gemini as a
second LLM provider. Both providers use the **same** JSON-schema
tool definition and the **same** system prompt — only the SDK
client differs. Each provider writes its own response JSON file.
Per-provider failures are isolated: if Gemini fails, Claude's
output still ships, and vice versa.

**Out of scope for v1.1** (these are later iterations):

- Comparator / triage-disagreement scoring (v1.2).
- Multi-score batching (v1.3).
- Registry of accumulating opinions across runs (v2).
- Per-LLM track records / weighting (v2).
- Concurrent (parallel) API calls — sequential is fine for v1.1
  since the bottleneck is API latency on small workloads.
- Adding a third provider (OpenAI / GPT) — that's v1.4 if Vincent
  decides to go three-wide. v1.1 stops at two.

If during implementation you find yourself wanting one of these
"because it would make v1.1 better," **don't.** Note as an open
question in the report-back.

**v1.0 baseline** (committed on `llm-triage`, do not regress):

- `tools/llm_triage/run_triage.py` — Python wrapper that invokes
  the v0 C++ binary, calls Claude Sonnet 4.6 via Anthropic SDK
  with tool-use structured output, writes
  `<basename>.llm_response.json`.

After v1.1, the file naming convention shifts to **per-provider**:
- `<basename>.claude_response.json`  (was `llm_response.json`)
- `<basename>.gemini_response.json`  (new)

The old single-file name is retired in this commit so downstream
consumers (v1.2 comparator) have a stable convention to target.

---

## Reference docs (read first)

- `docs/prompts/llm_triage_v1_0_python_api_wrapper.md` — the v1.0
  prompt (committed on this branch). Contains the JSON-schema
  tool definition, the system prompt, and the Anthropic API call
  shape. v1.1 reuses the schema and prompt **verbatim** for both
  providers.
- `tools/llm_triage/run_triage.py` — v1.0's implementation.
  Read it end-to-end before refactoring. Note in particular:
  - How the Anthropic client is constructed
  - How `tool_choice` forces tool use
  - How the response's `tool_use` block is parsed
  - How metadata fields (model, response_id, tokens, hashes)
  are written to the JSON
- `docs/llm_triage_design.md` — design decisions. Particularly
  "Multi-LLM, parallel-as-async" and "Availability resilience" —
  the latter explicitly calls for per-provider failure isolation,
  which v1.1 implements.
- `docs/prompts/llm_triage_v0_format_emitter.md` — for the
  CLAUDE.md override and parallel-work pact (read once; they
  apply to every llm-triage CC session).
- Google's `google-genai` Python SDK (web search if needed). The
  `google-generativeai` package is being deprecated in favor of
  `google-genai`. Use `google-genai`. Function-calling
  documentation specifically — Gemini's API supports
  function/tool declarations with JSON schemas, with a
  `tool_config` setting to force a specific function call (the
  Gemini equivalent of Anthropic's `tool_choice`).

---

## CLAUDE.md override and parallel-work pact

Same as v0 / v1.0. `CLAUDE.md` is stale on `src/composing/`,
`ARCHITECTURE.md`, build commands. **This prompt overrides on
those points.** v1.1 doesn't touch any pact-protected paths.

May freely create/modify:
- `tools/llm_triage/**`
- `docs/prompts/llm_triage_*.md` (this prompt — copy from
  mainline to worktree and commit, see Step 1)

May NOT touch (full list lives in v0 prompt; review if uncertain):
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

2. **Both API keys present:**
   ```bash
   for var in ANTHROPIC_API_KEY GOOGLE_API_KEY; do
     val="$(printenv "$var" || true)"
     if [ -z "$val" ]; then echo "$var: MISSING"; else echo "$var: set ($(echo -n "$val" | wc -c) chars)"; fi
   done
   ```
   If `ANTHROPIC_API_KEY` is missing, halt and surface (v1.0
   needs it). If `GOOGLE_API_KEY` is missing, halt and surface —
   Vincent gets it from `aistudio.google.com → Get API key`,
   then `setx GOOGLE_API_KEY <value>` and a full VS Code restart
   (not just a new terminal — VS Code's main process needs to
   re-read environment).
   Do not read, log, commit, or print either key's value.

3. **Python environment:** the venv chosen in v1.0 (mainline's
   or worktree's) — read the comment at the top of
   `run_triage.py` to find which. Verify both SDKs are
   installable into it. Install `google-genai` if not present:
   ```bash
   <chosen_python> -m pip show google-genai 2>&1 | head -3
   <chosen_python> -m pip install google-genai
   ```
   The `anthropic` package should already be there from v1.0.

4. **v1.0 still works:** run `run_triage.py` against Pachelbel
   (no code changes yet) and confirm the Claude response file
   appears as before. If v1.0 has decayed, halt and surface —
   don't paper over.

---

## Work order

### Step 1 — Bring this prompt into the worktree and commit

```bash
cd /c/s/MS-llm-triage
cp "/c/s/MS/docs/prompts/llm_triage_v1_1_add_gemini_provider.md" \
   "docs/prompts/llm_triage_v1_1_add_gemini_provider.md"
git add docs/prompts/llm_triage_v1_1_add_gemini_provider.md
git commit -m "LLM-Triage v1.1: prompt file for Gemini-provider session"
```

### Step 2 — Refactor v1.0 to a provider-agnostic shape

Read `run_triage.py` end-to-end. Identify:
- The shared parts: argparse, score loading, C++ binary
  invocation, reading `notes_only.txt`, building the system
  prompt + tool schema, hashing for metadata.
- The Claude-specific parts: the `anthropic.Anthropic()` client
  construction, the `messages.create(...)` call shape, the
  `response.content` parsing for the `tool_use` block, the
  Anthropic-specific metadata fields (`model_response_id`,
  `stop_reason`, `usage.input_tokens`, etc.).

Refactor into:

- A **shared** module (or top-of-file section) that defines
  `SYSTEM_PROMPT`, `TOOL_NAME`, and `INPUT_SCHEMA` (the
  inner JSON schema, vendor-neutral) once.
- Per-provider helper(s):
  - `def call_claude(notes_only_text: str, model: str, max_tokens: int) -> ProviderResult`
  - `def call_gemini(notes_only_text: str, model: str, max_tokens: int) -> ProviderResult`
  Each takes the shared prompt + schema, wraps it for that
  vendor's SDK, makes the API call, parses the structured
  response, and returns a normalized `ProviderResult`
  containing:
    - `tool_input: dict` — the parsed JSON object (the `judgments`,
      `key_summary`, etc.)
    - `metadata: dict` — provider-neutral fields (model,
      response_id, input_tokens, output_tokens, stop_reason,
      timestamp_utc, prompt_version, system_prompt_hash,
      tool_definition_hash) plus a `provider` field
      (`"claude"` / `"gemini"`).
- A `main()` that:
  1. Parses args (add `--providers` flag, default
     `claude,gemini`, allowing `claude` or `gemini` alone for
     debugging)
  2. Invokes the C++ binary once
  3. Reads `notes_only.txt` once
  4. Loops over the requested providers, calling each helper
     and writing its result to
     `<basename>.<provider>_response.json`
  5. **Per-provider failure isolation:** if one provider's
     helper raises after 3 retries, log the failure to stderr,
     write a stub JSON file
     (`<basename>.<provider>_response.json`) containing only
     the metadata + an `error` field, and continue to the next
     provider. Do not kill the script. Final exit code:
     - 0 if all providers succeeded
     - 1 if at least one provider succeeded and at least one
       failed (partial success)
     - 2 if all providers failed
   This mirrors the design doc's "availability resilience"
   principle.

### Step 3 — Implement `call_gemini`

Wrap the shared `INPUT_SCHEMA` in Gemini's `FunctionDeclaration`
shape. The wire format differs from Anthropic but the JSON
substance is the same. Sketch (verify against current
`google-genai` docs — these APIs evolve):

```python
from google import genai
from google.genai import types

def call_gemini(notes_only_text, model, max_tokens):
    client = genai.Client()  # reads GOOGLE_API_KEY from env

    function_declaration = types.FunctionDeclaration(
        name=TOOL_NAME,
        description=TOOL_DESCRIPTION,  # from shared definition
        parameters=INPUT_SCHEMA,       # the JSON schema dict
    )
    tool = types.Tool(function_declarations=[function_declaration])

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[tool],
        tool_config=types.ToolConfig(
            function_calling_config=types.FunctionCallingConfig(
                mode="ANY",                     # forces a function call
                allowed_function_names=[TOOL_NAME],
            )
        ),
        max_output_tokens=max_tokens,
    )

    response = client.models.generate_content(
        model=model,
        contents=[notes_only_text],
        config=config,
    )

    # Parse the function call from the response.
    # Gemini may wrap the function args differently than Anthropic;
    # find the function_call block and extract its args dict.
    ...
```

**Schema-shape gotchas to expect.** Gemini's schema validator
historically has been pickier than Anthropic's about a few things:
- `enum` on string fields may need `format: "enum"` or specific
  `type` declarations
- Nested `anyOf` / `oneOf` may not be supported the same way
- Required fields must be declared explicitly per object level

If the schema you defined for v1.0 fails Gemini's validation,
**adjust the schema in a way that keeps Anthropic happy too**
(both providers use the same schema). Validate with the
Anthropic call still passing after any adjustment. **Halt and
surface** rather than maintaining two divergent schemas.

**Default model:** use whatever Google currently positions as
their analytical-tier model (likely `gemini-3.0-thinking` or
similar, current as of v1.1 build time). If the model ID isn't
obvious from the SDK or docs, halt and surface — don't guess. A
short web search of `aistudio.google.com` model documentation is
the right move.

**Retries and timeouts:** mirror the Anthropic retry pattern.
3 retries, exponential backoff (1s, 4s, 16s), then propagate the
failure up to `main()` for per-provider isolation.

### Step 4 — Update `call_claude` (already exists from v1.0)

Make sure `call_claude` returns the same `ProviderResult` shape
as `call_gemini`, including the `provider: "claude"` field in
metadata. The actual Anthropic API call body should be unchanged
from v1.0 — we're just normalizing the return type.

The renamed output file (`<basename>.claude_response.json`,
formerly `<basename>.llm_response.json`) is the only behavioral
change to v1.0's output for Claude. Note this rename in the
commit message.

### Step 5 — Verify on Pachelbel

```bash
cd /c/s/MS-llm-triage
<chosen_python> tools/llm_triage/run_triage.py \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Expected stdout (two lines, one per provider):

```
provider=claude  model=claude-sonnet-4-6 judgments=<N> tokens=<I>+<O> output=outputs/pachelbel-canon-in-d-arr-hiromi-uehara.claude_response.json
provider=gemini  model=<gemini-model-id> judgments=<N> tokens=<I>+<O> output=outputs/pachelbel-canon-in-d-arr-hiromi-uehara.gemini_response.json
```

Then **inspect both JSON files:**

1. Both have valid `metadata` blocks with non-empty `model`,
   `model_response_id`, `input_tokens`, `output_tokens`.
2. Both `tool_input.judgments` arrays have ≥30 entries.
3. Both `tool_input.key_summary` say D major.
4. Both `tool_input.format_friction` are read carefully — if
   either model flagged something, surface verbatim in the
   report-back.
5. **Spot-check cross-model agreement on m1**. Both providers'
   first judgment should be for measure 1 with a chord_label
   of `D` (the Pachelbel ground bass starts with D). They may
   disagree on confidence — that's fine, even useful.

If **either** provider's response is malformed, missing the
expected schema, or returns zero judgments, **halt and surface**
with the JSON content. Do not silently fall back.

If the per-provider failure isolation triggered (one succeeded,
one wrote an error stub), surface that even on otherwise-OK
runs — Vincent needs to know which calls cost money/quota and
which didn't.

---

## Halt-and-surface protocol

Halt and surface to Vincent immediately if:

- Either API key is missing or invalid (401/403 on either
  provider).
- The schema-shape adjustments needed for Gemini would force
  the schema to diverge from what Anthropic accepts.
- Either provider returns malformed structured output that
  doesn't match `INPUT_SCHEMA`.
- The judgment count for either provider is under 30 on
  Pachelbel.
- Web search of Google's docs doesn't turn up a clear current
  Gemini model ID — don't guess.
- Anything in the implementation tempts you to edit a file
  outside `tools/llm_triage/`.
- The retry-and-isolate logic catches one provider failure on
  Pachelbel — that's exactly the case the design is built for,
  but Vincent needs to see which provider broke and why before
  signing off on v1.1.

When halting, include: the exact step, command + output, the
relevant JSON if applicable (truncated to first 2KB if large),
and your candidate next actions for Vincent's decision.

---

## Commit and push

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/run_triage.py
git status   # confirm: only run_triage.py changed
git commit -m "LLM-Triage v1.1: add Gemini provider; per-provider isolation

run_triage.py now calls Claude Sonnet 4.6 and Gemini in
sequence using the same JSON-schema tool definition and the
same system prompt. Each provider writes a separate response
file: <basename>.claude_response.json and
<basename>.gemini_response.json. The old singular
<basename>.llm_response.json is retired.

Per-provider failures are isolated: if one provider fails after
3 retries, the script logs the failure, writes an error-stub
JSON for that provider, and continues with the others. Exit
codes: 0 (all OK), 1 (partial), 2 (all failed)."
git push origin llm-triage
```

---

## Report-back format

```
## LLM-Triage v1.1 — session report

Branch: llm-triage @ <commit_sha>
Pushed to: origin/llm-triage  (yes/no)

### Files changed
- tools/llm_triage/run_triage.py  (+<X>/-<Y>)
- (any other Python files split out during refactor)
- requirements.txt or equivalent if updated

### Python environment
- anthropic version: <X.Y.Z>
- google-genai version: <X.Y.Z>

### v1.1 verification on Pachelbel
- Claude:  model=<id>  judgments=<N>  tokens=<I>+<O>  status=<ok|error>
- Gemini:  model=<id>  judgments=<N>  tokens=<I>+<O>  status=<ok|error>

### Cross-model spot-check
- m1 b1 chord_label: claude=<X>  gemini=<Y>  agree=<yes/no>
- m9 b3 chord_label: claude=<X>  gemini=<Y>  agree=<yes/no>
- m37 b1 chord_label: claude=<X>  gemini=<Y>  agree=<yes/no>

### format_friction (verbatim from each provider)
- Claude: "<verbatim>"
- Gemini: "<verbatim>"

### Schema adjustments (if any)
- <list any tweaks made to INPUT_SCHEMA so both providers
  accepted it; verbatim diff or summary>

### Surprises / open questions for Vincent
- <list, brief>

### Mainline-pact compliance check
- Files touched outside tools/llm_triage/ + docs/prompts/llm_triage_*: <list — must be empty>
```

---

## Why this scope and not more

You may be tempted to also wire in the comparator (analyzer
regions vs LLM judgments) since you'll have N=2 LLM data sitting
right there. **Don't.** The comparator is v1.2's whole job and
needs its own design pass (alignment of measure-judgments to
analyzer regions, disagreement scoring, output format for the
triage candidate list). Adding it here would couple two separable
problems and make this CC session twice as long with twice the
review surface.

Same logic for adding OpenAI as a third provider, or batching
across the Hiromi corpus. Each is a clean v1.x increment on its
own. Stay focused.
