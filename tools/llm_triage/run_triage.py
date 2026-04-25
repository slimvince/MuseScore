#!/usr/bin/env python3
# Python interpreter: /c/s/MS/.venv/Scripts/python.exe  (mainline venv, anthropic 0.97.0, google-genai 1.73.1)

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import anthropic
from google import genai
from google.genai import types as gtypes

# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

_WORKTREE = Path(__file__).resolve().parents[2]

TOOL_NAME = "submit_harmonic_analysis"
TOOL_DESCRIPTION = (
    "Submit your harmonic analysis of the score. Use this tool "
    "exactly once per response, after analyzing the input. Each "
    "judgment covers one harmonic region (typically a half-measure "
    "or full measure). Cover the whole score from start to end "
    "without gaps."
)

# Vendor-neutral JSON schema for the tool's input.
# Note: 'minimum' removed from 'measure' — Gemini's schema validator
# does not support numeric range constraints; Anthropic is unaffected.
INPUT_SCHEMA: dict = {
    "type": "object",
    "required": ["judgments", "key_summary"],
    "properties": {
        "judgments": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "measure", "beat_range", "chord_label",
                    "key", "mode", "confidence",
                ],
                "properties": {
                    "measure": {
                        "type": "integer",
                        "description": "1-based measure number",
                    },
                    "beat_range": {
                        "type": "string",
                        "description": (
                            "Beat range within the measure as "
                            "'X-Y' (e.g. '1-2' for beats 1-2, "
                            "'1-4' for full measure)"
                        ),
                    },
                    "chord_label": {
                        "type": "string",
                        "description": (
                            "Chord identity in conventional "
                            "notation: e.g. 'D', 'A7', 'Bm7', "
                            "'D/F#', 'Gmaj7', 'A13sus'. Use "
                            "slash notation for inversions or "
                            "non-root bass."
                        ),
                    },
                    "chord_label_alternatives": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": (
                            "Other defensible interpretations "
                            "in score order. Empty if unambiguous."
                        ),
                    },
                    "key": {
                        "type": "string",
                        "description": "Key center (e.g. 'D major', 'A minor')",
                    },
                    "mode": {
                        "type": "string",
                        "enum": [
                            "Ionian", "Dorian", "Phrygian",
                            "Lydian", "Mixolydian", "Aeolian",
                            "Locrian", "harmonic_minor",
                            "melodic_minor", "other",
                        ],
                    },
                    "confidence": {
                        "type": "string",
                        "enum": [
                            "very_high", "high", "medium",
                            "low", "very_low", "abstain",
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
                        ),
                    },
                    "reasoning": {
                        "type": "string",
                        "description": (
                            "1-2 sentence rationale; cite "
                            "specific pitches or context if "
                            "useful."
                        ),
                    },
                },
            },
        },
        "key_summary": {
            "type": "string",
            "description": "Overall key/tonality summary in 1-3 sentences.",
        },
        "ambiguity_flags": {
            "type": "array",
            "items": {"type": "string"},
            "description": (
                "Specific regions where the analysis is "
                "ambiguous or where multiple interpretations "
                "are defensible."
            ),
        },
        "format_friction": {
            "type": "string",
            "description": (
                "If anything in the input format was unclear "
                "or could be improved, note it here. Empty "
                "string if format was fine."
            ),
        },
    },
}

# Anthropic SDK tool shape (wraps the shared schema).
TOOL: dict = {
    "name": TOOL_NAME,
    "description": TOOL_DESCRIPTION,
    "input_schema": INPUT_SCHEMA,
}

SYSTEM_PROMPT = """\
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
call, include the alternative reading in chord_label_alternatives."""


# ---------------------------------------------------------------------------
# Shared data type
# ---------------------------------------------------------------------------

@dataclass
class ProviderResult:
    tool_input: dict
    metadata: dict


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _base_metadata(
    provider: str,
    model: str,
    response_id: str,
    input_tokens: int,
    output_tokens: int,
    stop_reason: str,
    prompt_version: str,
) -> dict:
    return {
        "provider": provider,
        "model": model,
        "model_response_id": response_id,
        "prompt_version": prompt_version,
        "system_prompt_hash": _sha256(SYSTEM_PROMPT),
        "tool_definition_hash": _sha256(json.dumps(TOOL, sort_keys=True)),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "stop_reason": stop_reason,
    }


# ---------------------------------------------------------------------------
# Claude provider
# ---------------------------------------------------------------------------

def call_claude(
    notes_only_text: str, model: str, max_tokens: int, prompt_version: str
) -> ProviderResult:
    client = anthropic.Anthropic()
    last_exc: Exception | None = None
    response = None

    for attempt in range(3):
        try:
            with client.messages.stream(
                model=model,
                max_tokens=max_tokens,
                system=SYSTEM_PROMPT,
                tools=[TOOL],
                tool_choice={"type": "tool", "name": TOOL_NAME},
                messages=[{"role": "user", "content": notes_only_text}],
            ) as stream:
                response = stream.get_final_message()
            break
        except (anthropic.RateLimitError, anthropic.APIStatusError) as exc:
            if isinstance(exc, anthropic.APIStatusError) and exc.status_code < 500:
                raise
            last_exc = exc
            delay = 4 ** attempt
            print(
                f"Claude API error attempt {attempt+1}/3 ({exc}); retry in {delay}s …",
                file=sys.stderr,
            )
            time.sleep(delay)
        except anthropic.APIConnectionError as exc:
            last_exc = exc
            delay = 4 ** attempt
            print(
                f"Claude connection error attempt {attempt+1}/3; retry in {delay}s …",
                file=sys.stderr,
            )
            time.sleep(delay)
    else:
        raise RuntimeError(
            f"Claude API failed after 3 attempts. Last: {last_exc}"
        ) from last_exc

    tool_block = next(
        (b for b in response.content if b.type == "tool_use" and b.name == TOOL_NAME),
        None,
    )
    if tool_block is None:
        raise RuntimeError(
            f"Claude did not return a {TOOL_NAME} call. "
            f"stop_reason={response.stop_reason}"
        )

    return ProviderResult(
        tool_input=tool_block.input,
        metadata=_base_metadata(
            provider="claude",
            model=response.model,
            response_id=response.id,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            stop_reason=response.stop_reason,
            prompt_version=prompt_version,
        ),
    )


# ---------------------------------------------------------------------------
# Gemini provider
# ---------------------------------------------------------------------------

def call_gemini(
    notes_only_text: str, model: str, max_tokens: int, prompt_version: str
) -> ProviderResult:
    client = genai.Client()  # reads GOOGLE_API_KEY from env

    function_declaration = gtypes.FunctionDeclaration(
        name=TOOL_NAME,
        description=TOOL_DESCRIPTION,
        parameters=INPUT_SCHEMA,
    )
    gemini_tool = gtypes.Tool(function_declarations=[function_declaration])
    config = gtypes.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[gemini_tool],
        tool_config=gtypes.ToolConfig(
            function_calling_config=gtypes.FunctionCallingConfig(
                mode="ANY",
                allowed_function_names=[TOOL_NAME],
            )
        ),
        max_output_tokens=max_tokens,
    )

    last_exc: Exception | None = None
    response = None

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model,
                contents=[notes_only_text],
                config=config,
            )
            break
        except Exception as exc:
            last_exc = exc
            delay = 4 ** attempt
            print(
                f"Gemini API error attempt {attempt+1}/3 ({exc}); retry in {delay}s …",
                file=sys.stderr,
            )
            time.sleep(delay)
    else:
        raise RuntimeError(
            f"Gemini API failed after 3 attempts. Last: {last_exc}"
        ) from last_exc

    # Find the function call in the response parts.
    func_call = None
    for candidate in response.candidates:
        for part in candidate.content.parts:
            if (
                hasattr(part, "function_call")
                and part.function_call is not None
                and part.function_call.name == TOOL_NAME
            ):
                func_call = part.function_call
                break
        if func_call:
            break

    if func_call is None:
        finish = (
            response.candidates[0].finish_reason
            if response.candidates
            else "unknown"
        )
        raise RuntimeError(
            f"Gemini did not return a {TOOL_NAME} function call. "
            f"finish_reason={finish}"
        )

    # func_call.args is a MapComposite (dict-like proto wrapper).
    # JSON round-trip converts all nested proto types to plain Python.
    tool_input: dict = json.loads(json.dumps(dict(func_call.args)))

    usage = response.usage_metadata
    input_tokens = getattr(usage, "prompt_token_count", 0) or 0
    output_tokens = getattr(usage, "candidates_token_count", 0) or 0
    response_id = getattr(response, "response_id", "") or ""
    stop_reason = (
        str(response.candidates[0].finish_reason)
        if response.candidates
        else "unknown"
    )

    return ProviderResult(
        tool_input=tool_input,
        metadata=_base_metadata(
            provider="gemini",
            model=model,
            response_id=response_id,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            stop_reason=stop_reason,
            prompt_version=prompt_version,
        ),
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

_CLAUDE_DEFAULT = "claude-sonnet-4-6"
_GEMINI_DEFAULT = "gemini-3.1-pro-preview"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the LLM triage pipeline on a single score."
    )
    parser.add_argument("score_path", help="Path to .mscz / .musicxml / .mxl file")
    parser.add_argument("output_dir", help="Directory to write artifacts + JSON response")
    parser.add_argument(
        "--llm-triage-binary",
        default=str(_WORKTREE / "ninja_build_llm_triage" / "llm_triage.exe"),
        help="Path to the v0 C++ llm_triage binary",
    )
    parser.add_argument(
        "--providers",
        default="claude,gemini",
        help="Comma-separated list of providers to call (default: claude,gemini)",
    )
    parser.add_argument(
        "--claude-model",
        default=_CLAUDE_DEFAULT,
        help=f"Claude model ID (default: {_CLAUDE_DEFAULT})",
    )
    parser.add_argument(
        "--gemini-model",
        default=_GEMINI_DEFAULT,
        help=f"Gemini model ID (default: {_GEMINI_DEFAULT})",
    )
    parser.add_argument(
        "--prompt-version",
        default="v1.1",
        help="Short string for traceability in the response file",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=32768,
        help="max_tokens for API calls (default: 32768)",
    )
    args = parser.parse_args()

    score_path = Path(args.score_path)
    if not score_path.exists():
        sys.exit(f"Error: score file not found: {score_path}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    providers = [p.strip() for p in args.providers.split(",") if p.strip()]
    model_for = {"claude": args.claude_model, "gemini": args.gemini_model}

    # Invoke the C++ binary once to produce the .txt artifacts.
    binary = Path(args.llm_triage_binary)
    if not binary.exists():
        sys.exit(f"Error: llm_triage binary not found: {binary}")

    cpp_result = subprocess.run(
        [str(binary), str(score_path), str(output_dir)],
        check=False,
        capture_output=True,
        text=True,
    )
    if cpp_result.returncode != 0:
        sys.exit(
            f"Error: llm_triage binary failed (exit {cpp_result.returncode}):\n"
            f"stdout: {cpp_result.stdout}\nstderr: {cpp_result.stderr}"
        )

    basename = score_path.stem
    notes_only_path = output_dir / f"{basename}.notes_only.txt"
    if not notes_only_path.exists():
        sys.exit(f"Error: expected notes_only file not found: {notes_only_path}")

    notes_only_content = notes_only_path.read_text(encoding="utf-8")

    # Call each provider; isolate failures.
    succeeded = 0
    failed = 0

    for provider in providers:
        model = model_for.get(provider, "")
        json_path = output_dir / f"{basename}.{provider}_response.json"
        try:
            if provider == "claude":
                pr = call_claude(notes_only_content, model, args.max_tokens, args.prompt_version)
            elif provider == "gemini":
                pr = call_gemini(notes_only_content, model, args.max_tokens, args.prompt_version)
            else:
                raise ValueError(f"Unknown provider: {provider!r}")

            output_json = {
                "metadata": {
                    "score_basename": basename,
                    "score_path": str(score_path.resolve()),
                    **pr.metadata,
                },
                "tool_input": pr.tool_input,
            }
            json_path.write_text(json.dumps(output_json, indent=2), encoding="utf-8")

            judgment_count = len(pr.tool_input.get("judgments", []))
            print(
                f"provider={provider}  "
                f"model={pr.metadata['model']}  "
                f"judgments={judgment_count}  "
                f"tokens={pr.metadata['input_tokens']}+{pr.metadata['output_tokens']}  "
                f"output={json_path}"
            )
            succeeded += 1

        except Exception as exc:
            failed += 1
            print(f"ERROR: provider={provider} failed: {exc}", file=sys.stderr)
            error_json = {
                "metadata": {
                    "score_basename": basename,
                    "score_path": str(score_path.resolve()),
                    "provider": provider,
                    "model": model,
                    "prompt_version": args.prompt_version,
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                },
                "error": str(exc),
            }
            json_path.write_text(json.dumps(error_json, indent=2), encoding="utf-8")
            print(
                f"provider={provider}  status=FAILED  error_stub={json_path}"
            )

    # Exit codes: 0 = all OK, 1 = partial, 2 = all failed.
    if failed == 0:
        sys.exit(0)
    elif succeeded > 0:
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()
