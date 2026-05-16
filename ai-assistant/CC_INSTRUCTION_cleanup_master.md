# CC Instruction — Cleanup + Git commit (master worktree)

## This instruction is for the master worktree (`C:\s\MS\`)

## Overview

Remove stale extension source files from the design-docs folder, then git commit.

---

## Task 1 — Delete stale extension source files

The following files in `C:\s\MS\ai-assistant\` are extension source files that were
created here by mistake. The canonical copies live in
`C:\s\MS-core-api\share\extensions\ai-assistant\`. Delete these four files:

- `C:\s\MS\ai-assistant\Main.qml`
- `C:\s\MS\ai-assistant\ScoreAccess.js`
- `C:\s\MS\ai-assistant\ToolSchemas.js`
- `C:\s\MS\ai-assistant\Dispatch.js`

Do NOT delete any `.md` files or `CC_INSTRUCTION_*.md` files. Those are design
documents and stay here.

After deleting, list the remaining contents of `C:\s\MS\ai-assistant\` to confirm
only `.md` files and `CC_INSTRUCTION_*.md` files remain.

---

## Task 2 — Git: check status and commit

Run `git -C "C:\s\MS" status` to see the current state of the worktree.

Stage the four deletions:
```
git -C "C:\s\MS" rm ai-assistant/Main.qml
git -C "C:\s\MS" rm ai-assistant/ScoreAccess.js
git -C "C:\s\MS" rm ai-assistant/ToolSchemas.js
git -C "C:\s\MS" rm ai-assistant/Dispatch.js
```

Commit message:
```
ai-assistant: remove stale extension source from design-docs folder

Canonical source is now C:\s\MS-core-api\share\extensions\ai-assistant\.
C:\s\MS\ai-assistant\ contains design docs only (*.md, CC_INSTRUCTION_*.md).
```

Report git status before and after, and confirm the commit hash.

---

## Output

Report:
1. Confirmation that the four files were deleted.
2. Remaining file list in `C:\s\MS\ai-assistant\`.
3. Git status before staging.
4. Commit hash and summary line.
