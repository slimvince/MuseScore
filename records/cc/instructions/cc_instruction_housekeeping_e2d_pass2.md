# CC Instruction: Post-E2d Housekeeping Pass 2

## Pre-reading

Read `C:\s\MS\STATUS.md` (header only) and `C:\s\MS\build_and_test.md` before starting.
Current HEAD: `8f13aee8d3`. No build required for any task here.

---

## Task 1 — Delete the two junk files

These are accidental shell-redirect debris and safe to delete immediately:

```
cd C:\s\MS
# The filename starting with "--measures" (a misdirected batch_analyze output)
# and the "elines BIR=..." filename (a botched git diff redirect).
# Find them by partial name since the shell won't expand them cleanly:
ls -la | grep -E "^-.*(-{2}measures|elines)"
```

Delete them with:
```
find . -maxdepth 1 -name "--measures*" -delete
find . -maxdepth 1 -name "elines*" -delete
```

Confirm they're gone. No commit needed — they were untracked.

---

## Task 2 — Add .gitignore rules for working-process files

These files have never been committed (0 tracked), accumulate naturally as CC and
Cowork work, and should never be in source control. Add rules to `.gitignore`:

```
# Working-process instruction and report files (CC / Cowork session artifacts)
/cc_instruction_*.md
/cc_e2d_*.md
/cc_*.md
ai-assistant/CC_INSTRUCTION_*.md
```

Open `.gitignore` (root), find a logical place (near other `*.md` exclusions if any,
or at the end), and add those four lines with the comment above them.

After editing:
```
git diff .gitignore
```

Confirm the rules look right. Then:
```
git add .gitignore
git commit -m "chore: gitignore CC/Cowork working-process instruction files"
```

---

## Task 3 — Commit the documentation files

These are established documentation that belongs in the repo:

**Batch 1 — docs/prompts/ iteration logs (~14 files)**
```
git add "docs/prompts/iteration_66"* "docs/prompts/iteration_67"* \
        "docs/prompts/iteration_68"* "docs/prompts/iteration_69"* \
        "docs/prompts/iteration_70"* "docs/prompts/iteration_71"* \
        "docs/prompts/iteration_72"* "docs/prompts/iteration_73"* \
        "docs/prompts/iteration_74"* "docs/prompts/iteration_75"* \
        "docs/prompts/iteration_76"* "docs/prompts/iteration_77"* \
        "docs/prompts/iteration_78"*
```
(Adjust the glob as needed to match actual filenames.)

**Batch 2 — key detection + LLM integration docs**
```
git add docs/key_detection_baroque_partial_signature.md
git add docs/llm_integration.md
```

**Batch 3 — iter analysis docs (if present)**
```
git add docs/iter90*.md docs/iter92*.md docs/iter97*.md 2>/dev/null || true
```

Then commit all batches together:
```
git commit -m "docs: commit untracked documentation (iteration logs, key detection, LLM integration)"
```

---

## Task 4 — Review and selectively commit tools/ scripts

List the untracked tools files:
```
git ls-files --others --exclude-standard tools/
```

For each `.py` file, show the first 10 lines and the filename:
```
for f in $(git ls-files --others --exclude-standard tools/*.py 2>/dev/null); do
  echo "=== $f ==="; head -10 "$f"; echo
done; echo "exit:$?"
```

**Decision rule:**
- If a script has a docstring or argparse usage description and is >50 lines → commit it.
- If it reads like a one-off dump or debug print script (no docstring, <30 lines, prints
  raw data) → skip (or delete if clearly ephemeral).
- For `.txt` files in tools/ — skip all (generated output/reports, not source).

Commit whatever qualifies:
```
git add <qualifying .py files>
git commit -m "tools: commit analysis scripts from iter 90–97 sessions"
```

If nothing qualifies, skip the commit and report what you found.

---

## Task 5 — Handle the bwv*_dcml.xml files at root

List them:
```
ls bwv*_dcml.xml 2>/dev/null; echo "exit:$?"
```

These are DCML reference XML files that ended up at the repo root instead of
`tools/dcml/`. Move them:
```
mkdir -p tools/dcml
git mv bwv*_dcml.xml tools/dcml/
git commit -m "chore: relocate stray bwv DCML XML files to tools/dcml/"
```

If `tools/dcml/` already exists with files in it, check for name collisions first.
If any file is already tracked at its current root location, `git mv` handles it.
If any is untracked, use `mv` then `git add`.

---

## Task 6 — Assess the helper scripts at root

Show the contents of the two helper scripts (they're small):
```
cat step3_build_and_test.ps1 2>/dev/null; echo "---"
cat run_e2b_tests.bat 2>/dev/null; echo "exit:$?"
```

**Decision rule:**
- If either is a general-purpose helper with lasting utility (not tied to a specific
  session or a since-superseded workflow) → commit it.
- Otherwise → delete it (untracked, so just `rm`).

Apply your judgment and report what you did.

---

## Task 7 — Commit COWORK_HANDOFF.md

This file was updated by Cowork after the E2d housekeeping report. It should be
committed now:

```
cd C:\s\MS
git add COWORK_HANDOFF.md
git commit -m "docs: COWORK_HANDOFF.md — post-E2d housekeeping update"
```

---

## Task 8 — Final git status check

```
cd C:\s\MS
git status
git log --oneline -8
```

The working tree should be clean (or near-clean). Report any remaining untracked
files that weren't covered above so they can be handled in a future pass.

---

## Output

Report for each task:
1. Junk files — deleted or not found.
2. .gitignore — rules added, commit hash.
3. Docs commit — files included, commit hash.
4. Tools scripts — what was committed vs skipped, brief reason.
5. bwv DCML files — moved and committed, or status.
6. Helper scripts — contents summary, committed or deleted.
7. COWORK_HANDOFF.md — commit hash.
8. Final `git log --oneline -8` output.
