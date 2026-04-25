# llm_triage

Headless tool that loads one MuseScore score, runs the harmonic analyzer, and emits three plain-text artifacts for hand-evaluation against frontier LLMs:

- `<score>.notes_only.txt` — raw note onsets and durations, no analyzer output, no printed chord symbols. Anchoring-free input for the LLM's independent opinion pass.
- `<score>.with_symbols.txt` — same onsets, plus any printed chord symbol as a `printed:` annotation per region. Input for the prescription-classification pass.
- `<score>.analyzer_output.txt` — our analyzer's per-region chord identity, key, and alternatives. Reference for reading LLM responses against our output. Never pasted to the LLM.

Usage: `llm_triage <input_score_path> <output_dir>`

No LLM API calls are made in v0. See `docs/llm_triage_design.md` for full design rationale.
