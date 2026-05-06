# LLM-Triage Session Bootstrap

**How to use:** Paste the contents below as your first message in a new
Cowork (Claude desktop) conversation. It establishes the parallel-work
context so the new session can pick up the LLM-triage build without
seeing the refactor session's history.

---

You're picking up the planning side of a parallel work stream on the
MuseScore Studio composing module. The other session (still running)
is orchestrating a multi-phase refactor of the analysis pipeline. Your
session is building the LLM-triage workflow. The two streams touch
different parts of the codebase and can run independently — your job is
to plan and draft CC implementation prompts; CC does the actual code.

## Read these first (all in `/sessions/.../mnt/.auto-memory/` or repo)

- `MEMORY.md` — index of all memories, auto-loaded
- `project_llm_triage_design.md` — the original design discussion from
  2026-04-23
- `docs/llm_triage_design.md` (if present in the repo) — fuller design
  doc referenced from the memory
- `reference_hiromi_corpus.md` — the 20 Hiromi scores at
  `C:\s\MS\tools\extra scores\hiromi` (quote the path — has a space).
  Your primary v0 corpus
- `project_chord_symbol_ban.md` — non-negotiable constraint: chord
  symbols are banned as analyzer input. Tools may read symbols only
  as comparison metadata, never as input. The LLM-triage workflow
  exists *because* of this constraint — we can't measure
  non-authoritative corpora through ground-truth comparison, so we
  use LLM judgment instead
- `project_unified_analysis_pipeline.md` — what mainline is doing.
  Read so you know what NOT to touch and what analyzer interface
  you're consuming

## What the other (mainline) session is doing

A multi-phase refactor unifying the implode/annotation/tick-regional
analysis paths into a single shared `analyzeSection()` entry point.
Phase 3a (implode) and Phase 3b (annotation) have landed. Phase
3c-impl (tick-regional + alternatives field + temporal extension
migration) is in flight or recently landed by the time you're reading
this. Phases 4 (HarmonicRegion retirement) and 5 (modulation-aware
Roman numerals) are upcoming.

For your purposes: `AnalyzedSection` is the canonical shared analysis
output, holding `AnalyzedRegion` entries with chord identity,
alternatives (post-3c), key, and temporal extensions. Plus `KeyArea`
spans for modulation-aware work (post-Phase-5). This is what you'll
feed to LLM judgments.

## Parallel-work pact

**Do NOT touch in any CC session you draft:**
- `src/composing/` — analyzer logic, mainline owns it
- `src/notation/internal/` — bridge layer, mainline owns it
- `src/notation/tests/pipeline_snapshot_tests/` — snapshot harness,
  mainline owns it
- `ARCHITECTURE.md` — mainline updates this as it lands phases
- `docs/policy2_coalescing_map.md` — same
- `docs/unified_analysis_pipeline.md` — same

**DO touch:**
- New code in `tools/llm_triage/` (or similar new directory)
- New design docs at `docs/llm_triage_*.md`
- Memory entries (especially LLM-triage-specific ones)
- `MEMORY.md` index (line-level conflicts here are easy to resolve)

**Branch:** all CC work for LLM-triage on a dedicated branch
(`llm-triage` or similar) off master. Don't commit to master
directly — that'd race the other session.

## Working pattern (mirrors the mainline session)

For each chunk of CC implementation work:

1. You and Vincent settle design decisions in chat (small explicit
   decision lists work well — present 3–5 options, recommend one
   with rationale, let Vincent override or accept)
2. You draft a self-contained CC prompt as a markdown file in
   `docs/prompts/` (CC sessions start cold, no conversation history,
   so prompts must be standalone)
3. Vincent runs the prompt in CC, reports back with results
4. You ingest the report, surface what's worth knowing, save
   anything non-obvious to memory, plan the next chunk

Standard CC prompt elements that have proven important:
- Pre-flight check (`git status` / `git diff --stat` to detect
  prior-session truncation; force rebuild on branch switches)
- Explicit work order with verification gates between steps
- Hard scope guardrails (what NOT to touch)
- Halt-and-surface protocol when the verification fails (do not
  paper over diffs; surface for guidance)
- Push-to-remote at session end for backup
- Report-back format Vincent can scan quickly

CC's build/test loop (informational):
- Build dir is `ninja_build_rel/` (NOT `ninja_build/` — the
  CLAUDE.md is stale on this; see `feedback_build_dir.md`)
- `setup_and_build.bat` for full build
- `composing_tests.exe` for unit tests; mismatch baseline
  currently 0/135 abstract, 135/135 symbol/roman — must not
  regress on any CC session
- `notation_tests.exe` for notation tests; 53/53 baseline

## Suggested v0 scope (open for your refinement)

A minimum-viable LLM-triage workflow:

- Reads N scores from a target corpus (Hiromi as the v0 set)
- Runs the analyzer to produce `AnalyzedSection` per score
- For each region, builds a structured prompt summarizing: notes
  sounding in the region, analyzer's chord identity + alternatives +
  key, surrounding context (1 region back / forward)
- Sends the prompt to one LLM (start single, ensemble in v1)
- Captures the LLM's reasonableness judgment + reasoning
- Aggregates per-score and per-corpus reports

The interesting design questions (read the design doc to see if
they're already settled, otherwise propose):
- Which LLM(s) for the ensemble (Claude / GPT-4 / Gemini / open
  models — depends on what's accessible from MuseScore tooling)
- Prompt structure (zero-shot vs few-shot; what context to include)
- Aggregation rules (majority vote? weighted? ranked?)
- Output format (per-region rows? per-score summary? both?)
- How to handle LLM disagreement (flag for human review? majority
  wins? configurable threshold?)

## First task

Read everything in the "Read these first" list. Then propose a v0
scope to Vincent — what's the minimum useful LLM-triage workflow
that's worth building now, given that the analyzer interface will
gain more capabilities over the next few weeks (Phase 4, 5, etc.)
that v1+ can adopt.

Don't over-design v0 — the point is to get a workflow running on
real Hiromi data, see what the LLM judgments look like, and iterate.
v0 can be intentionally small.

When you and Vincent have v0 scope settled, draft the first CC
prompt as a self-contained markdown file in `docs/prompts/`. The
prompt initiates the LLM-triage tool's first commit — could be just
"create the directory structure, initial CMake wiring, hello-world
that loads one Hiromi score and prints region-level analyzer output
to stdout." Or could be more ambitious. Your call after reading the
design.

Good luck. Report back periodically; the mainline session and this
one will sync via memory and via Vincent.
