# CC Instruction: Commit the doc-governance / ARCHITECTURE.md-canonical docs set (fork-only)

## Pre-reading

Read `C:\s\MS\CLAUDE.md` before starting. This is a **docs-only** task — no source,
no build, no tests, no corpus measurement.

---

## Context

A Cowork documentation session (STATUS session 18, 2026-06-30) made `ARCHITECTURE.md`
the canonical, current architecture doc and resolved the two-doc divergence with
`cowork_target_architecture.md`. All edits are documentation only. The user has
reviewed and ratified ARCHITECTURE.md ("looks good"). Fold the whole set into **one**
docs commit.

**Do not modify any file's content** — only stage and commit. Do not touch any source
file. If anything below does not match the working tree, STOP and report.

---

## Step 0 — verify the working tree is docs-only

```
git status -s; echo "exit:$?"
```

**HARD STOP conditions — do NOT commit, report instead — if `git status` shows any of:**
- any change under `src/`, `tools/`, `muse/`, or any `*.cpp` / `*.h` / `*_tests.*`
  file (this session changed **no code** — a dirty source file means something
  unexpected happened);
- any staged change you did not expect from the list below.

The dirty/untracked set should be **documentation only**. Expected members (reconcile
against `git status` — some may be modified, some untracked-new):

- `ARCHITECTURE.md`               (modified — reconciliation, new §2.15, §6.7, §7, full language pass)
- `cowork_target_architecture.md` (modified — demoted to a detailed-rationale reference)
- `cowork_layer2_slicing_design.md` (modified — §13 transitional → as-built "rebuilt to read slices")
- `cowork_layer3_keymode_design.md` (modified — §14 per-layer-decode clarity note)
- `cowork_layer4_chordsymbol_design.md` (modified — 2 locator asides → as-built)
- `cowork_layer5_function_design.md` (modified — §5.0 span disambiguation, §5.4 region→key-span)
- `cowork_layer6_grouping_design.md` (L6 design v1)
- `cowork_progression_schema_dictionary.md` (the Harmonic Vocabulary component spec)
- `cowork_progression_schema_design.md` (the L5/L6 recognition consumer, rewritten v1)
- `cowork_style_clustering_plan.md` (committed future-work plan)
- `STATUS.md`                     (modified — the session-18 entry)

If the actual set differs (extra or missing docs), **report the diff and ask** before
committing — do not silently add or omit.

---

## Step 1 — stage and commit (single commit)

Stage exactly the docs `git status` shows (the set above, reconciled). Then:

```
git commit -m "docs: make ARCHITECTURE.md canonical + current (reconciliation, §2.15 cross-cutting contracts, Harmonic Vocabulary + style taxonomy, L*-doc cleanup, language pass)"; echo "exit:$?"
```

---

## Step 2 — push to the FORK ONLY

```
git push origin HEAD; echo "exit:$?"
```

**★ FORK-ONLY HARD STOP (CLAUDE.md distribution constraint):** push to `origin`
(`slimvince/MuseScore`) only. **NEVER** push or merge toward `upstream`
(`musescore/MuseScore`). If `git push` would target `upstream`, or `origin` resolves
to `musescore/MuseScore`, STOP and report — do not proceed. (`upstream` push is
disabled in this repo; keep it so.)

---

## After

```
git log --oneline -3; echo "exit:$?"
```

Report the commit hash + message and confirm the push reached `origin` only. Do not
touch any source file. Do not run a build or the test suites (nothing compiled changed).
