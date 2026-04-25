#!/usr/bin/env python3
# Python interpreter: /c/s/MS/.venv/Scripts/python.exe  (mainline venv, anthropic 0.97.0)

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import anthropic

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_WORKTREE = Path(__file__).resolve().parents[2]

TOOL_NAME = "submit_harmonic_analysis"

TOOL: dict = {
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
                        "key", "mode", "confidence",
                    ],
                    "properties": {
                        "measure": {
                            "type": "integer",
                            "minimum": 1,
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
                            "description": (
                                "Key center (e.g. 'D major', 'A minor')"
                            ),
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
                "description": (
                    "Overall key/tonality summary in 1-3 sentences."
                ),
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
    },
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
# Helpers
# ---------------------------------------------------------------------------

def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _call_api(client: anthropic.Anthropic, model: str, max_tokens: int,
              notes_only_content: str) -> anthropic.types.Message:
    """Call the Anthropic API with up to 3 retries (1s, 4s, 16s backoff).

    Streams the response to avoid SDK HTTP timeout guards on large max_tokens.
    """
    last_exc: Exception | None = None
    for attempt in range(3):
        try:
            with client.messages.stream(
                model=model,
                max_tokens=max_tokens,
                system=SYSTEM_PROMPT,
                tools=[TOOL],
                tool_choice={"type": "tool", "name": TOOL_NAME},
                messages=[{"role": "user", "content": notes_only_content}],
            ) as stream:
                return stream.get_final_message()
        except (anthropic.RateLimitError, anthropic.APIStatusError) as exc:
            if isinstance(exc, anthropic.APIStatusError) and exc.status_code < 500:
                raise
            last_exc = exc
            delay = 4 ** attempt  # 1, 4, 16
            print(
                f"API error on attempt {attempt + 1}/3 ({exc}); retrying in {delay}s …",
                file=sys.stderr,
            )
            time.sleep(delay)
        except anthropic.APIConnectionError as exc:
            last_exc = exc
            delay = 4 ** attempt
            print(
                f"Connection error on attempt {attempt + 1}/3; retrying in {delay}s …",
                file=sys.stderr,
            )
            time.sleep(delay)
    raise RuntimeError(
        f"Anthropic API failed after 3 attempts. Last error: {last_exc}"
    ) from last_exc


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

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
        "--model",
        default="claude-sonnet-4-6",
        help="Anthropic model ID (default: claude-sonnet-4-6)",
    )
    parser.add_argument(
        "--prompt-version",
        default="v1.0",
        help="Short string for traceability in the response file",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=32768,
        help="max_tokens for the Anthropic API call (default: 32768)",
    )
    args = parser.parse_args()

    score_path = Path(args.score_path)
    if not score_path.exists():
        sys.exit(f"Error: score file not found: {score_path}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: invoke the C++ binary to (re-)produce the three .txt artifacts.
    binary = Path(args.llm_triage_binary)
    if not binary.exists():
        sys.exit(f"Error: llm_triage binary not found: {binary}")

    result = subprocess.run(
        [str(binary), str(score_path), str(output_dir)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        sys.exit(
            f"Error: llm_triage binary failed (exit {result.returncode}):\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )

    # Step 2: read notes_only.txt.
    basename = score_path.stem
    notes_only_path = output_dir / f"{basename}.notes_only.txt"
    if not notes_only_path.exists():
        sys.exit(f"Error: expected notes_only file not found: {notes_only_path}")

    notes_only_content = notes_only_path.read_text(encoding="utf-8")

    # Step 3: call the Anthropic API.
    client = anthropic.Anthropic()
    response = _call_api(client, args.model, args.max_tokens, notes_only_content)

    # Step 4: extract the tool_use block.
    tool_use_block = next(
        (b for b in response.content if b.type == "tool_use" and b.name == TOOL_NAME),
        None,
    )
    if tool_use_block is None:
        print(f"Raw response:\n{response.model_dump_json(indent=2)}", file=sys.stderr)
        sys.exit(
            f"Error: model did not return a {TOOL_NAME} tool call. "
            f"stop_reason={response.stop_reason}"
        )

    tool_input: dict = tool_use_block.input

    # Step 5: write JSON output.
    system_prompt_hash = _sha256(SYSTEM_PROMPT)
    tool_def_hash = _sha256(json.dumps(TOOL, sort_keys=True))

    output_json = {
        "metadata": {
            "score_basename": basename,
            "score_path": str(score_path.resolve()),
            "model": response.model,
            "model_response_id": response.id,
            "prompt_version": args.prompt_version,
            "system_prompt_hash": system_prompt_hash,
            "tool_definition_hash": tool_def_hash,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "stop_reason": response.stop_reason,
        },
        "tool_input": tool_input,
    }

    json_path = output_dir / f"{basename}.llm_response.json"
    json_path.write_text(json.dumps(output_json, indent=2), encoding="utf-8")

    judgment_count = len(tool_input.get("judgments", []))
    print(
        f"model={response.model} "
        f"judgments={judgment_count} "
        f"tokens={response.usage.input_tokens}+{response.usage.output_tokens} "
        f"output={json_path}"
    )


if __name__ == "__main__":
    main()
