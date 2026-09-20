# CC INSTRUCTION — the second backup, second re-run, with the path-list route fixed, 2026-09-16

**THE BASE.** The current commit should be `5d24edb565b2e0e9efc92e082c163112bd97087f` on branch `master`,
and `origin/master` should be the same commit. **Check this first (Task 0(b)).**

**WHY THIS EXISTS.** `cc_instruction_second_backup_rerun_2026_09_16.md` stopped at Task 0(d), and
`cc_report_second_backup_rerun_2026_09_16.md` (uncommitted) records why: the shell-read guard refused an
`awk` over a scratchpad copy of the enumeration, because the path was written through the shell variable
`$SP` and the guard could not resolve it. **The defect is partly the writing side's:** that dispatch left
open how the path list reaches git ("on the command line, or with `--stdin-paths` fed from a scratchpad
file"), which invited a shell read of a file. **That dispatch is spent and is not re-run. This one replaces
it, changed at that one point** (Task 0(d) and Task 1(a) now fix the route). Everything else is carried
over unchanged, so this instruction stands on its own.

It is a backup and nothing else: it commits files as they stand on disk and changes the content of no file
except the report it writes.

**CARRIED OVER, WITH THEIR REASONS.**
1. **The score file is held back; its provenance record is committed.**
   `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md` records that the `.mscx` is an
   unaltered extraction from `tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz`,
   with checksums. The stopped re-run's premise 4 found that archive tracked, so the `.mscx` is recomputable
   from the repository. Premise 4 is checked again here. The record's §8 leaves open, as the user's
   question, whether a committed `.mscx` should be held byte-stable; holding it back leaves that untouched.
2. **Emptiness and size come from git objects by hash; no NUL-byte check is run.** No route to a NUL-byte
   check inside D-253 is known to the writing side, and a route that hides repository paths from the guard
   would be a deliberate use of its blind spot, which D-253 does not permit. **The bound: a file truncated
   with NUL bytes would be committed as it stands.** A commit destroys nothing: a tracked file's earlier
   version stays in history, and an untracked file's disk copy is no worse for being backed up.

**WHAT THE WRITING SIDE CHECKED AT THE OBJECTS BEFORE WRITING THIS.** `.git/refs/heads/master` and
`.git/refs/remotes/origin/master` both read the base commit. The stopped re-run's report, read whole,
including its refusal text and its premise answers. **The writing side ran no git command and no shell
command.**

**The writing side does not touch this file, or any file this batch commits, while the batch runs.**

---

## THE ROUTE RULE — read before Task 0

**No shell text utility is run on any file, anywhere** — not `awk`, `sed`, `grep`, `cat`, `head`, `tail`,
`sort`, `wc`, `cut`, and no interpreter code — **including files in your session scratchpad.** **No shell
variable stands for a path. No command reads a file through redirection (`<`).** The only commands this
batch runs are the git commands and the `python tools/audit/changed_paths.py` invocations named below.
You may save tool output into a scratchpad file outside `C:\s\MS` (by redirection `>`, or with the Write
file tool) and read it back **only with the Read file tool**. **You build the path list yourself, from what
you read, and write the paths literally into the commands**, as repository-relative paths, each quoted.

---

## PREMISES — DECLARED UNESTABLISHED; check each and report either way

1. The current commit is the one above, on `master`. **Not so → STOP.**
2. `origin` is `https://github.com/slimvince/MuseScore`, and `origin/master` equals the current commit.
   **`origin` differs → STOP. `origin/master` differs → report it; the push rules in Task 2 govern.**
3. **The shape expected** (a shape, not a count): inside the ALLOWED SET, the changed and untracked paths are
   root `cc_*.md` files (now including both stopped runs' dispatches and reports, and this dispatch), the two
   `docs/research_papers/` text files, the provenance record (inside the untracked-directory record
   `tools/audit/derivation_exemplars/`), and `cowork_handoff_entry_one_hundred_and_eighty_eight.md`. Nothing
   under `reading_pass/` or `ratification_surfaces/` need appear. Outside the set, paths are **reported, not
   committed, and not a STOP**.
4. The archive `tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz` is
   tracked. **Check with
   `git ls-files -- "tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz"`.**
   **It prints nothing → STOP and report.**

---

## THE ALLOWED SET — the only paths this batch may stage

- At the repository root: files matching `cowork_*.md` and `cc_*.md`.
- Everything under `reading_pass/` and under `ratification_surfaces/`.
- Exactly two files under `docs/research_papers/`: `docs/research_papers/BIBLIOGRAPHY.md` and
  `docs/research_papers/README.md`.
- Exactly one file under `tools/`: `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md`.

**HELD BACK — never stage, open, list or search:** anything under `docs/research_papers/polyph9-release/`;
any other path under `docs/research_papers/`; `external resarch summary/`; `scratch_artifacts/`. **Never
stage:** `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; anything under `Claude outputs/`
or `Codex research inventory/` (those stand with the user); anything under `src/`, `decisions/`,
`open_items/`, or elsewhere under `tools/`; `CLAUDE.md`, `DECISIONS.md`, `STATUS.md`, `ARCHITECTURE.md`,
`OPEN_ITEMS.md`, `BUILD_AND_TEST.md`. If any of those shows a change, **report its path and change type
only.** Records the enumeration tool prints under the held-back locations may be named in the report by the
top-level location only, as the stopped re-run's report did.

---

## TASK 0 — the start state, and pinning

**(a)** Pin this dispatch: `git hash-object -w cc_instruction_second_backup_rerun_two_2026_09_16.md`. Record
the blob identity, and take every later read of this dispatch from `git cat-file blob <that identity>`.

**(b)** Answer premises 1 and 2 with `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD`,
`git rev-parse origin/master` and `git remote -v`. Answer premise 4 with the command it names.

**(c)** Enumerate with **`python tools/audit/changed_paths.py`** (no flag; **not `--json`**). For the
untracked-directory record `tools/audit/derivation_exemplars/`, and any other such record inside the ALLOWED
SET, enumerate members with the Glob file tool. Split every path into **inside the ALLOWED SET**, **outside
it**, and **deleted or renamed** (`D` or `R`). Obey the route rule.

**(d)** **Emptiness and size, by git object only, with literal paths.** Run
`git hash-object -w -- "<path>" "<path>" …` over the ALLOWED-SET list, **at most forty paths per command**,
each path written literally. Then pass the printed identities to `git cat-file --batch-check`, written
literally into a bash here-document of identities only (for example
`git cat-file --batch-check <<'EOF'` … `EOF`) — the here-document carries hexadecimal identities and no path,
and git is not an interpreter. Neither command prints file content. **Any size 0 → STOP and report the
paths. Any size over 50 MB → STOP. Report every size over 5 MB.** *(The size is the blob's, after git's
line-ending conversion — exactly what is committed.)* Keep each identity paired with its path by position,
and report the pairing for any path you name.

**(e)** **Size of `cowork_handoff_entry_one_hundred_and_eighty_eight.md`** from 0(d), reported against
**19822** bytes. **A difference is not a STOP**; if it differs, say whether a line-ending conversion warning
was printed for that path.

**(f)** **If a guard refuses any command in this batch, STOP and report the refusal text verbatim. Do not
try another route.**

---

## TASK 1 — commit

**(a)** Stage **exactly** the ALLOWED-SET list with `git add -- "<path>" …`, **at most forty paths per
command**, each path written literally. **No `git add -A`, `git add .`, glob, variable or path file.** Do not
stage deletions or renames; report them.

**(b)** Run `python tools/audit/changed_paths.py --staged` and compare the staged set against the list **as a
set, in both directions**, reading the command's printed output directly, or a saved copy with the Read tool — no shell utility. **Any
difference → unstage everything with `git reset -q` and STOP.**

**(c)** Commit **verbatim — edit, reformat, re-wrap and normalise nothing** — with this message, followed by
the standing attribution trailer:

```
Second backup: CC session reports, research-paper text files, exemplar provenance (user-ordered, 2026-09-16)

Commits, as they stand on disk, the files the first backup's ALLOWED SET left out:
root cc_*.md files, docs/research_papers/BIBLIOGRAPHY.md and README.md, the
bwv1049_03_presto provenance record, and Cowork record files changed since 5d24edb5.
The .mscx exemplar is held back (recomputable from its tracked archive).
No NUL-byte check was run. No file content changed.
Dispatch: cc_instruction_second_backup_rerun_two_2026_09_16.md
```

---

## TASK 2 — push

`git push origin master`. **Never `--force`, never `--force-with-lease`, never push to `upstream`, no other
branch.** Rejected for any reason → **STOP; do not pull, merge, rebase or retry with force**; report the
exact error text. After success, `git rev-parse HEAD` and `git rev-parse origin/master` must be equal;
**not equal → report.**

---

## TASK 3 — the report, committed and pushed

**(a)** Write `cc_report_second_backup_rerun_two_2026_09_16.md` with the Write file tool: the pinned blob
identity; premises 1 to 4, each answered; the Task 0(c) enumeration in its three lists, **every path inside
the ALLOWED SET named**; the Task 0(d) result with every size over 5 MB named; the Task 0(e) size; the commit
identity and the `--staged` output; the push result and the two identities. **Assert no count of your own
acts; name the members.**

**(b)** Commit that report alone with `git add -- "cc_report_second_backup_rerun_two_2026_09_16.md"`
(message: `Report: second backup, second re-run, 2026-09-16`, with the attribution trailer), push under Task
2's rules, and record the new `HEAD` and `origin/master` at the foot of your chat reply.

---

## DECLARED BY THE WRITING SIDE

- **What this batch's own orders move:** the git object store (the pinned blob and the blobs 0(d) writes),
  the index and history (two commits), `origin/master` (two pushes), and one new file, its report. **No
  existing file's content is edited, and neither spent dispatch is touched.**
- **No `STATUS.md` entry, forward-bound re-aiming, `tools/audit/` regeneration or guard-set run is ordered.**
  If you judge a rule requires a `STATUS.md` entry, name it in the report, write none, and do not STOP.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

- Premise 1 or 4 fails, or `origin` is not the URL in premise 2.
- A size 0 or a size over 50 MB at Task 0(d).
- Any guard refusal, anywhere in the batch.
- Any difference between the staged set and the list at Task 1(b).
- Any push rejected.
- **Any instruction here found false at the objects.**

## WHAT THIS BATCH MAY NOT DO

Edit any file except its own report; delete any file; stage outside the ALLOWED SET; open, list, stage or
search anything under `docs/research_papers/polyph9-release/`; open the `.mscx`; run a shell text utility or
interpreter code on any file; create, flip or discard any open-items row; write any decisions-register entry;
touch `src/`; build, test or measure anything; force-push, pull, merge or rebase.
