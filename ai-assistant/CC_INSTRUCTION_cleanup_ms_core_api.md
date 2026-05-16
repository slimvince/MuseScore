# CC Instruction — Cleanup + Git commit (ms-core-api worktree)

## This instruction is for the ms-core-api worktree (`C:\s\MS-core-api\`)

## Overview

Three tasks: update stale memory entries, then git commit the v0.5.0 extension source.

---

## Task 1 — Update memory: feedback_ai_assistant_dual_deploy.md

The current entry says `C:\s\MS\ai-assistant\Main.qml` is the source and it deploys to
two targets. That is now wrong. Rewrite the entry to reflect the current layout:

- **Canonical source (edit here):** `C:\s\MS-core-api\share\extensions\ai-assistant\`
  (Main.qml, ScoreAccess.js, ToolSchemas.js, Dispatch.js, manifest.json)
- **Deploy target (MS4):** `%LOCALAPPDATA%\MuseScore\MuseScore4\extensions\ai-assistant\`
  — copy all four code files here after every change
- `C:\s\MS\ai-assistant\` contains design docs only — do not edit extension source there

Update the MEMORY.md index description for this entry to match.

---

## Task 2 — Update memory: feedback_ms4_deploy_gate.md

The entry correctly describes the grep gate pattern, but the example paths reference
`C:\s\MS\ai-assistant\Main.qml` as the source file. Update the example paths to point
to `C:\s\MS-core-api\share\extensions\ai-assistant\Main.qml`. The gate logic itself
is unchanged.

Update the MEMORY.md index description if needed.

---

## Task 3 — Update memory: project_ai_assistant_sandbox_choice.md

This entry records an open question: should ai-assistant stay as a form-extension or
migrate to a `MuseScore { pluginType: "dialog" }` plugin? It was deferred to "desktop
Claude" on 2026-05-15.

That discussion has concluded. The decision is: **stay with form-extension**. The
keyboard workarounds (Keys.onPressed intercept + dynamic NavigationControl chain for
Enter-to-send) are understood and documented. The extension API surface is sufficient
for all planned tools. No migration.

Update the entry to record this as settled. Mark it closed. Update MEMORY.md index.

---

## Task 4 — Git: check status and commit

Run `git -C "C:\s\MS-core-api" status` to see the current state of the worktree.

Then stage and commit the extension source files:

```
git -C "C:\s\MS-core-api" add share/extensions/ai-assistant/Main.qml
git -C "C:\s\MS-core-api" add share/extensions/ai-assistant/ScoreAccess.js
git -C "C:\s\MS-core-api" add share/extensions/ai-assistant/ToolSchemas.js
git -C "C:\s\MS-core-api" add share/extensions/ai-assistant/Dispatch.js
git -C "C:\s\MS-core-api" add share/extensions/ai-assistant/manifest.json
```

Commit message:
```
ai-assistant v0.5.0 — tool calling, layered JS structure, dynamic system prompt

- ScoreAccess.js: MuseScore layer (getScoreInfo, getStructure, addRehearsalMark)
- ToolSchemas.js: per-provider tool schema definitions
- Dispatch.js: tool name → ScoreAccess function dispatch
- Main.qml: tool-calling loops for Anthropic/OpenAI/Gemini/custom,
  dynamic system prompt (chord-symbol spelling + concert pitch from score),
  user-editable system prompt override in settings panel
```

Report the git status output before and after, and confirm the commit hash.

---

## Output

Report:
1. Confirmation of each memory update (what changed).
2. Git status before staging.
3. Commit hash and summary line.
