# LLM-Triage v1.0 — Python Wrapper + Claude API Call

**Scope:** Add `tools/llm_triage/run_triage.py` — a Python script that
takes a score path, invokes the v0 C++ `llm_triage` binary to produce
the three structured-text artifacts, then calls Claude Sonnet 4.6 via
the Anthropic Python SDK with `notes_only.txt` as input and writes the
LLM's per-measure harmonic judgments to a JSON file alongside the
artifacts.

**Out of scope for v1.0** (these are v1.1 / v1.2 / later):

- Analyzer-vs-LLM comparator / triage-disagreement scoring.
- Multi-LLM ensemble (single Claude call only).
- Multi-score batching (single score per invocation).
- Registry of accumulating opinions across runs.
- Per-LLM track records.
- Web/notebook UI.
- Anything in `src/composing/`, `src/notation/internal/`, snapshot
  tests, `ARCHITECTURE.md`, or other mainline-pact-protected paths.

If during implementation you find yourself wanting one of these
"because it would make v1.0 better," **don't.** Note it as an open
question in the report-back.

**v0 baseline** (committed on `llm-triage` branch, do not regress):

- `tools/llm_triage/llm_triage.cpp` produces three `.txt` artifacts.
- Default Hiromi score: `pachelbel-canon-in-d-arr-hiromi-uehara.mscz`.
- Pachelbel run produces 77 analyzer regions; 849 lines of `notes_only.txt`.
- Three frontier LLMs (Claude Sonnet 4.6, GPT-5, Gemini 3 Thinking)
  hand-paste-tested the format — no clarifying questions, sound
  analyses, strong cross-model agreement on Pachelbel structure.

---

## Reference docs (read first)

- `docs/prompts/llm_triage_v0_format_emitter.md` — the v0 prompt
  (committed on this branch). Contains the **CLAUDE.md override
  table** and **parallel-work pact** that apply equally here. Read
  those sections; do not re-read the work-order steps for v0.
- `docs/llm_triage_design.md` — design decisions. v1.0 implements
  the "structured output via tool use" recommendation from the
  "Output format mirrors input" section.
- `tools/llm_triage/llm_triage.cpp` — the v0 C++ binary you're
  invoking from Python. Read its `argv` parsing to know how to
  call it correctly.
- `tools/test_batch_analyze_regressions.py` — Python pattern
  precedent. Mirror its style for argparse, paths, error handling.
- Anthropic Python SDK docs (web search if needed): we want the
  **tool use** API for structured output, not raw `messages.create`
  with a "respond in JSON" prompt. Tool use is reliable; prompted
  JSON is not.

---

## CLAUDE.md override

Same as v0 — `CLAUDE.md` auto-loads with stale pre-authorizations
for `src/composing/`, says `ARCHITECTURE.md` is fair game, prescribes
`cmd.exe //c` for builds. **All of those are wrong for this session.**
This prompt overrides on the same points the v0 prompt overrides
(see its CLAUDE.md override table). v1.0 doesn't touch any of those
files anyway, but the principle stands: this prompt > CLAUDE.md.

---

## Parallel-work pact

Same as v0. Do **not** edit:
- `src/composing/**`
- `src/notation/internal/**`
- `src/notation/tests/pipeline_snapshot_tests/**`
- `ARCHITECTURE.md`, `STATUS.md`, `REFACTOR_DEDUPLICATION_PLAN.md`
- `docs/policy2_coalescing_map.md`, `docs/unified_analysis_pipeline.md`

You may freely create/modify:
- `tools/llm_triage/**` (the only directory v1.0 touches)
- `docs/prompts/llm_triage_*.md` (this prompt — copy from mainline
  to worktree and commit, see Step 1)

v1.0 does not need to edit `tools/CMakeLists.txt` (no new C++
target); leave it alone.

---

## Pre-flight

1. **Confirm worktree and branch:**
   ```bash
   cd /c/s/MS-llm-triage
   git rev-parse --show-toplevel  # must be /c/s/MS-llm-triage
   git status -sb                 # must show: ## llm-triage (clean)
   git log --oneline -3           # last commits = v0 patch + v0 emitter
   ```
   If you're not in the worktree or the tree is dirty, **halt and
   surface**.

2. **Confirm API key is available** in the environment that will
   run the Python script. Don't read or print the key — just check
   it's set:
   ```bash
   if [ -z "$ANTHROPIC_API_KEY" ]; then echo "MISSING"; else echo "set ($(echo -n "$ANTHROPIC_API_KEY" | wc -c) chars)"; fi
   ```
   If `MISSING`, **halt and surface** — Vincent needs to set it
   before you can run the script. (Setting it permanently is
   `setx ANTHROPIC_API_KEY <value>` from cmd.exe; for one shell
   session, `export ANTHROPIC_API_KEY=...` in bash.)
   Do **not** ever write the key to a file, log it, commit it, or
   print its value. It only exists in the environment.

3. **Locate or set up the Python environment.** The repo has a
   `.venv/` at the root. Check whether `anthropic` is installed:
   ```bash
   /c/s/MS-llm-triage/.venv/Scripts/python.exe -m pip show anthropic 2>&1 | head -5
   ```
   If installed, note the version and use this Python. If not
   installed, install into this same venv:
   ```bash
   /c/s/MS-llm-triage/.venv/Scripts/python.exe -m pip install anthropic
   ```
   If the `.venv/` doesn't exist in the worktree (worktrees share
   git history but not untracked dirs — `.venv/` is gitignored),
   create one or use the mainline `.venv/`:
   - **Preferred:** point at mainline's `.venv/` if it exists at
     `/c/s/MS/.venv/Scripts/python.exe`. Cross-worktree Python venv
     reuse is fine since the venv has no repo-state coupling.
   - **Fallback:** create `/c/s/MS-llm-triage/.venv/` and install
     `anthropic` there.
   Either way, decide once and document the chosen Python path in
   a comment at the top of `run_triage.py`.

4. **Confirm the v0 C++ binary still works** by running it:
   ```bash
   cd /c/s/MS-llm-triage
   /c/Qt/Tools/Ninja/ninja.exe -C ./ninja_build_llm_triage llm_triage
   ./ninja_build_llm_triage/llm_triage.exe \
     "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
     ./outputs
   ls -la outputs/  # should show 3 files
   ```
   Must succeed. If the binary has decayed (e.g. Phase 3c-impl
   landed on master and somehow propagated — though that shouldn't
   affect this branch), **halt and surface**.

---

## Work order

### Step 1 — Bring this prompt into the worktree and commit it

Same pattern as v0:
```bash
cd /c/s/MS-llm-triage
cp "/c/s/MS/docs/prompts/llm_triage_v1_0_python_api_wrapper.md" \
   "docs/prompts/llm_triage_v1_0_python_api_wrapper.md"
git add docs/prompts/llm_triage_v1_0_python_api_wrapper.md
git commit -m "LLM-Triage v1.0: prompt file for Python+API session"
```

### Step 2 — Add `run_triage.py` skeleton

Create `tools/llm_triage/run_triage.py` with:

- Shebang line and the chosen Python interpreter path documented
  in a top comment (the `.venv` decision from Pre-flight 3).
- Argparse CLI:
  - Positional `score_path` — path to a `.mscz` / `.musicxml` /
    `.mxl` file
  - Positional `output_dir` — directory to write artifacts +
    JSON response
  - Optional `--llm-triage-binary` — path to the v0 C++ exe;
    default `<worktree>/ninja_build_llm_triage/llm_triage.exe`
  - Optional `--model` — Anthropic model ID; default
    `claude-sonnet-4-6`
  - Optional `--prompt-version` — short string for traceability
    in the response file; default `v1.0`
  - Optional `--max-tokens` — Anthropic API `max_tokens`; default
    `8192` (Sonnet's analytical responses on the Pachelbel run
    were ~3KB; 8K leaves plenty of headroom)
- A `main()` that:
  1. Parses args and validates the score file exists
  2. Invokes the v0 C++ binary via `subprocess.run` to produce
     the three `.txt` files (re-emit even if they exist —
     keeps the JSON response synchronized with the actual
     artifacts that were sent)
  3. Reads `<basename>.notes_only.txt`
  4. Builds the system prompt + user message + tool definition
     (Step 3)
  5. Calls the Anthropic API (Step 4)
  6. Writes the structured response to
     `<basename>.llm_response.json` (Step 5)
  7. Prints a one-line summary to stdout: model, judgment count,
     output file path, total tokens used.

Do **not** put API logic at module scope — only inside `main()`.
That way `import run_triage` for future use (e.g. v1.1
comparator) doesn't trigger an API call.

### Step 3 — Define the response schema and tool definition

The Anthropic API supports tool use, where you define a "tool" with
a JSON schema and the model responds with a tool call whose
arguments match the schema. This is the most reliable way to get
parseable structured output.

Tool definition (in Python; serialize to the API's expected shape):

```python
TOOL_NAME = "submit_harmonic_analysis"

TOOL = {
    "name": TOOL_NAME,
    "description": (
        "Submit your harmonic analysis of the score. Use this tool "
        "exactly once per response, after analyzing the input. Each "
        "judgment covers one harmonic region (typically a half-measure "
        "or full measure). Cover the whole score from start to end "
        "without gaps."
    ),
    "input_schema": {
        "type": "object",
        "required": ["judgments", "key_summary"],
        "properties": {
            "judgments": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": [
                        "measure", "beat_range", "chord_label",
                        "key", "mode", "confidence"
                    ],
                    "properties": {
                        "measure": {
                            "type": "integer",
                            "minimum": 1,
                            "description": "1-based measure number"
                        },
                        "beat_range": {
                            "type": "string",
                            "description": (
                                "Beat range within the measure as "
                                "'X-Y' (e.g. '1-2' for beats 1-2, "
                                "'1-4' for full measure)"
                            )
                        },
                        "chord_label": {
                            "type": "string",
                            "description": (
                                "Chord identity in conventional "
                                "notation: e.g. 'D', 'A7', 'Bm7', "
                                "'D/F#', 'Gmaj7', 'A13sus'. Use "
                                "slash notation for inversions or "
                                "non-root bass."
                            )
                        },
                        "chord_label_alternatives": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": (
                                "Other defensible interpretations "
                                "in score order. Empty if unambiguous."
                            )
                        },
                        "key": {
                            "type": "string",
                            "description": (
                                "Key center (e.g. 'D major', 'A minor')"
                            )
                        },
                        "mode": {
                            "type": "string",
                            "enum": [
                                "Ionian", "Dorian", "Phrygian",
                                "Lydian", "Mixolydian", "Aeolian",
                                "Locrian", "harmonic_minor",
                                "melodic_minor", "other"
                            ]
                        },
                        "confidence": {
                            "type": "string",
                            "enum": [
                                "very_high", "high", "medium",
                                "low", "very_low", "abstain"
                            ],
                            "description": (
                                "very_high: notes unambiguously "
                                "spell this chord. high: clear with "
                                "minor ornamentation. medium: "
                                "defensible but reasonable people "
                                "might differ. low: best guess "
                                "given thin evidence. very_low: "
                                "speculative. abstain: too little "
                                "information to commit."
                            )
                        },
                        "reasoning": {
                            "type": "string",
                            "description": (
                                "1-2 sentence rationale; cite "
                                "specific pitches or context if "
                                "useful."
                            )
                        }
                    }
                }
            },
            "key_summary": {
                "type": "string",
                "description": (
                    "Overall key/tonality summary in 1-3 sentences."
                )
            },
            "ambiguity_flags": {
                "type": "array",
                "items": {"type": "string"},
                "description": (
                    "Specific regions where the analysis is "
                    "ambiguous or where multiple interpretations "
                    "are defensible."
                )
            },
            "format_friction": {
                "type": "string",
                "description": (
                    "If anything in the input format was unclear "
                    "or could be improved, note it here. Empty "
                    "string if format was fine."
                )
            }
        }
    }
}
```

The `format_friction` field is the load-bearing one for v1
iteration: even when the model doesn't ask a clarifying question
in chat, we want it to flag format-improvement candidates.

### Step 4 — Build the API call

System prompt (string constant in `run_triage.py`):

```
You are a music-theory analyst. You will receive a piano score in a
structured plain-text format: one line per note onset, giving
measure-and-beat position, duration, staff name, and pitches with
octave numbers (e.g. F#4, Bb2). Sustained notes are written once at
their onset and not repeated on subsequent beats — read the duration
to know how long each note lasts.

Analyze the harmony of the entire score. Treat the printed key
signature in the header as notational, not analytical — disagree if
the music suggests otherwise. Treat the input as the only ground
truth: do not reference external knowledge of what piece this might
be (titles, composers, conventional analyses) when forming
judgments.

Submit your analysis using the submit_harmonic_analysis tool. Cover
the whole score in measure (or half-measure) judgments. When notes
are sparse or ambiguous, lower your confidence rather than
overcommit. If a passage's interpretation depends on a judgment
call, include the alternative reading in chord_label_alternatives.
```

User message: the entire content of `<basename>.notes_only.txt`,
verbatim.

API call shape (using the `anthropic` Python SDK):

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

response = client.messages.create(
    model=args.model,
    max_tokens=args.max_tokens,
    system=SYSTEM_PROMPT,
    tools=[TOOL],
    tool_choice={"type": "tool", "name": TOOL_NAME},
    messages=[
        {"role": "user", "content": notes_only_content}
    ]
)
```

`tool_choice={"type": "tool", "name": TOOL_NAME}` forces the model
to use the tool — it can't respond with prose instead. That's the
behavior we want.

Error handling:

- API errors (rate limit, network, 5xx): retry up to 3 times with
  exponential backoff (1s, 4s, 16s). After 3 failures, halt the
  script with a clear error message and exit non-zero. Do not
  silently fall back to a partial response.
- Tool-use response missing or malformed: halt with the raw
  response printed to stderr. Do not try to recover by parsing
  prose.

### Step 5 — Write `<basename>.llm_response.json`

Schema:

```json
{
  "metadata": {
    "score_basename": "...",
    "score_path": "...",
    "model": "claude-sonnet-4-6",
    "model_response_id": "...",
    "prompt_version": "v1.0",
    "system_prompt_hash": "...",
    "tool_definition_hash": "...",
    "timestamp_utc": "...",
    "input_tokens": 0,
    "output_tokens": 0,
    "stop_reason": "..."
  },
  "tool_input": { ... the raw tool_use input from the API ... }
}
```

The `system_prompt_hash` and `tool_definition_hash` are SHA-256
hashes of the literal strings — this lets v1.1+ detect when the
prompt or schema changed across runs and decide whether to
invalidate prior responses.

Pretty-print the JSON (`indent=2`) so diffs across runs are
human-readable.

---

## Verification

Run on the default Pachelbel score:

```bash
cd /c/s/MS-llm-triage
<chosen_python> tools/llm_triage/run_triage.py \
  "tools/extra scores/hiromi/pachelbel-canon-in-d-arr-hiromi-uehara.mscz" \
  ./outputs
```

Expected stdout (one line):

```
model=claude-sonnet-4-6 judgments=<N> tokens=<I>+<O> output=outputs/pachelbel-canon-in-d-arr-hiromi-uehara.llm_response.json
```

Then **inspect the JSON**:

1. `metadata.input_tokens` and `metadata.output_tokens` are
   plausible (input ~5-15K, output ~1-5K based on the v0
   hand-paste round).
2. `tool_input.judgments` has at least 30 entries (Pachelbel has
   77 analyzer-regions but the LLM may collapse some — anything
   under 30 measures of judgment for a 77-measure piece would be
   suspect).
3. `tool_input.judgments[0]` is for measure 1 (the bass-only
   opening) and the chord_label / confidence are sensible: probably
   `D` with `medium` or `low` confidence, given the `abstain`-or-
   commit choice the LLM has to make on bass-only material.
4. `tool_input.key_summary` says the piece is in D major.
5. `tool_input.format_friction` — read this **carefully**. If the
   model flagged anything about the input format, surface it in
   the report-back verbatim. This is the v1.1 input.

If any of those checks fail, **halt and surface** with the JSON
content for inspection.

---

## Halt-and-surface protocol

Halt and surface to Vincent immediately if:

- Pre-flight finds the worktree dirty, on the wrong branch, or
  the API key missing.
- Pre-flight finds the v0 C++ binary fails to run.
- The Python venv decision is unclear (e.g. neither mainline nor
  worktree has a usable `.venv`).
- The Anthropic SDK call fails after 3 retries.
- The model returns a malformed tool-use response (missing,
  schema-violating, etc.).
- Verification finds judgments count under 30, missing fields,
  or a `format_friction` value that suggests the model struggled
  with the input.
- Anything in the implementation tempts you to edit a file
  outside `tools/llm_triage/`.

When halting, include: the exact step, the command + output, and
your candidate next actions for Vincent's decision.

---

## Commit and push

```bash
cd /c/s/MS-llm-triage
git add tools/llm_triage/run_triage.py
# Add a requirements.txt if you created one for the Python deps
git status   # confirm: only Python file(s) added
git commit -m "LLM-Triage v1.0: Python wrapper + Claude API call

run_triage.py invokes the v0 C++ llm_triage binary, reads
notes_only.txt, calls Claude Sonnet 4.6 via the Anthropic SDK
with tool-use structured output, and writes per-measure
harmonic judgments to <basename>.llm_response.json alongside
the .txt artifacts.

Single-score, single-model. v1.1 will add the analyzer-vs-LLM
comparator; v1.2 multi-score batching; v2 will add
multi-LLM ensemble and the registry."
git push origin llm-triage
```

---

## Report-back format

```
## LLM-Triage v1.0 — session report

Branch: llm-triage @ <commit_sha>
Pushed to: origin/llm-triage  (yes/no)

### Files added
- tools/llm_triage/run_triage.py  (<N> lines)
- tools/llm_triage/requirements.txt  (if created)

### Python environment
- Interpreter: <path to chosen python>
- anthropic version: <X.Y.Z>
- Other relevant deps: <list>

### v1.0 verification on Pachelbel
- Model: claude-sonnet-4-6 (model_response_id: <id>)
- Tokens: <input>+<output>
- Judgments emitted: <N> (covering m<first> through m<last>)
- Key summary: <verbatim>
- Ambiguity flags count: <N>
- format_friction value: <verbatim, even if empty string>

### Sanity-check sample (first 3 judgments)
- m<N> beats <range>: <chord> (<confidence>) — <reasoning excerpt>
- m<N> beats <range>: <chord> (<confidence>) — <reasoning excerpt>
- m<N> beats <range>: <chord> (<confidence>) — <reasoning excerpt>

### Surprises / open questions for Vincent
- <list, brief>

### Mainline-pact compliance check
- Files touched outside tools/llm_triage/ + docs/prompts/llm_triage_*: <list — must be empty>
```

---

## What v1.0 deliberately does NOT do

For the avoidance of scope creep:

- No comparator (analyzer vs LLM disagreement scoring) — v1.1.
- No multi-score loop — v1.2.
- No multi-LLM ensemble (only Claude Sonnet 4.6) — v2.
- No registry, no track records, no agreement weighting — v2.
- No CLI flags for cost caps, budget tracking, retry tuning
  beyond the simple 3-retry exponential backoff — v2.
- No JSON Schema validation library (e.g. `jsonschema`) on the
  response — Anthropic's tool-use API enforces the schema
  server-side; trust it for v1.0.

If during implementation you find yourself wanting to add one of
these "because it would make v1.0 better," **don't.** Note it as
an open question in the report-back instead.
