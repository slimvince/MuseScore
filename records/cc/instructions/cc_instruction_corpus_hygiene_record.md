# CC Instruction — record the corelli corpus-hygiene removal in tracked docs (docs only)

> The corelli removal is byte-identical and done, but the corpus is gitignored so it left **no tracked diff** — and it
> changed a tracked **fact**: the chorale gate is now **352** chorales, not 353. Record it and fix the stale count.
> **No empty marker commit. Docs only — no `src/`/`tools/` code, no corpus re-track, no push.** *(The never-bash rule is
> Cowork's.)*

## §1 — STATUS.md (do it)
Add a session entry: the stray non-chorale `corelli.xml` was removed from the chorale gate; the corpus is now **352 bwv
chorales** (was 352 bwv + 1 corelli orphan); **326** retain WiR coverage; the **BIR gate is 53/24/53 byte-identical**
(proven two ways — the 352 `.ours.json` byte-identical pre/post, and the BIR identity sets diff-clean vs CLAUDE.md);
corelli was a gate-non-contributing orphan (one of the non-WiR scores, structurally unable to produce a BIR=false case);
`tools/corpus/` is gitignored so there is no tracked corpus diff; 44 frozen historical dirs retain corelli artifacts and
were left untouched. Reference report: `cc_corpus_hygiene_report_corelli.md`.

## §2 — The stale "353" count (investigate, then propose CLAUDE.md edits; update the others)
- **Grep all tracked files** for live chorale-corpus-count references (`353`, "353/353", "353 stems/scores/stems") and
  report the list with file:line.
- **Update the *current-state* count → 352** in `docs/score_inventory.md` and any non-policy tracked doc, with a brief
  "(corelli stray removed 2026-06-29; gate byte-identical)" note. **Preserve dated/historical mentions** (e.g. "the
  353-stem gate as of <date>" or a prior report's figure) — do **not** rewrite history.
- **CLAUDE.md is the standing project-instructions file:** do **not** bulk-edit it. **Propose** the specific
  `353`→`352` edits (the gate-policy lines) as a declared list for Cowork/user ratification, and leave CLAUDE.md unchanged
  until ratified.
- **Tooling check:** confirm no `tools/*.py` hardcodes `353` as a required count (your successful 352/352 regen suggests
  the completeness check is dynamic `N/N`). If anything hardcodes 353, **flag it** (do not change tooling logic here).

## §3 — Commit + deliver
Commit **locally (unpushed)** the docs changes (STATUS.md + score_inventory.md and any non-policy doc): message
`docs: record corelli corpus-hygiene removal; chorale gate now 352, BIR 53/24/53 byte-identical`. Report the sha, the
changed-file list, the grep results, and the **proposed CLAUDE.md edits** (for ratification). **Push is a separate
Cowork-issued step.** `upstream` → STOP. Any `src/`/`tools/` code change or corpus re-track → STOP.
