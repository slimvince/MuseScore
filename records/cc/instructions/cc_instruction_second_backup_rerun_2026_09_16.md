# CC INSTRUCTION — the second backup, re-run with its two stops resolved, 2026-09-16

**THE BASE.** The current commit should be `5d24edb565b2e0e9efc92e082c163112bd97087f` on branch `master`,
and `origin/master` should be the same commit. **Check this first (Task 0(b)).**

**WHY THIS EXISTS.** `cc_instruction_second_backup_commit_and_push_2026_09_16.md` stopped at Task 0, and
`cc_report_second_backup_commit_and_push_2026_09_16.md` (uncommitted) records why: a `.mscx` member in
`tools/audit/derivation_exemplars/l0-l1/` failed its file-type check, and the shell-read guard refused its
byte-level corruption check because interpreter code named repository paths (D-253). **That dispatch is
spent and is not re-run. This one replaces it, changed at exactly those two points.** It is a backup and
nothing else: it commits files as they stand on disk and changes the content of no file except the report
it writes.

**THE TWO CHANGES, AND WHY.**
1. **The score file is held back; its provenance record is committed.**
   `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md` (read whole by the writing
   side this sitting) records that the `.mscx` is an unaltered extraction of the member `temp_10111.mscx`
   from `tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz`, with that
   archive's sha256, the member's recorded length and CRC-32, and the extracted file's sha256. So the
   `.mscx` is recomputable from the archive **if the archive is itself in the repository** — premise 4
   checks that. The same record's §8 leaves open, as the user's question, whether a committed `.mscx`
   should be held byte-stable against line-ending conversion; holding the file back leaves that question
   untouched.
2. **The byte read is replaced by git object queries, and the NUL-byte check is dropped with its bound
   stated.** No interpreter code and no working-tree read through a shell is ordered. Emptiness and size
   come from blobs by hash. **No NUL-byte check is run**, because no route to it inside D-253 is known to
   the writing side, and a route that hides repository paths from the guard (for example, paths read from
   a data file) would be a deliberate use of the guard's published blind spot, which D-253 — a rule about
   what is read, not how the read is spelled — does not permit. The bound, stated so it is not mistaken for
   a pass: **a file truncated with NUL bytes would be committed as it stands.** A commit destroys nothing:
   a tracked file's earlier version stays in history, and an untracked file's disk copy is no worse for
   being backed up.

**WHAT THE WRITING SIDE CHECKED AT THE OBJECTS BEFORE WRITING THIS.** `.git/refs/heads/master` and
`.git/refs/remotes/origin/master` both read the base commit. The stopped run's report, read whole: its
premises, its three lists, its Task 0(e) member lists and its refusal text. The provenance record, whole.
`.gitignore` carries no rule reaching `tools/extra scores/`. **The writing side ran no git command and no
shell command.** Whether the archive is tracked is not known to it — premise 4.

**The writing side does not touch this file, or any file this batch commits, while the batch runs.**

---

## PREMISES — DECLARED UNESTABLISHED; check each and report either way

1. The current commit is the one above, on `master`. **Not so → STOP.**
2. `origin` is `https://github.com/slimvince/MuseScore`, and `origin/master` equals the current commit.
   **`origin` differs → STOP. `origin/master` differs → report it; the push rules in Task 2 govern.**
3. **The shape expected** (a shape, not a count): inside the ALLOWED SET, the changed and untracked paths
   are mainly root `cc_*.md` files (now including the stopped run's dispatch and report, and this
   dispatch), the two `docs/research_papers/` text files, the provenance record, and
   `cowork_handoff_entry_one_hundred_and_eighty_eight.md`. Outside it, paths are **reported, not committed,
   and not a STOP**.
4. The archive `tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz` is
   tracked at the current commit. **Check with
   `git ls-files -- "tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz"`**
   (the path contains spaces; quote it). **It prints nothing → STOP and report**, because holding the
   `.mscx` back would then leave it with no copy anywhere in the repository.

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
or `Codex research inventory/` (those two stand with the user; the stopped run already reported their
members, so they are not re-listed); anything under `src/`, `decisions/`, `open_items/`, or elsewhere under
`tools/`; `CLAUDE.md`, `DECISIONS.md`, `STATUS.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`.
If any of those shows a change, **report its path and change type only.**

---

## TASK 0 — the start state, and pinning

**(a)** Pin this dispatch: `git hash-object -w cc_instruction_second_backup_rerun_2026_09_16.md`. Record the
blob identity, and take every later read of this dispatch from `git cat-file blob <that identity>`.

**(b)** Answer premises 1 and 2 with `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD`,
`git rev-parse origin/master` and `git remote -v`. Answer premise 4 with the command it names.

**(c)** Enumerate with **`python tools/audit/changed_paths.py`** (no flag; **not `--json`**). For every
untracked-directory record inside the ALLOWED SET, enumerate its members with the Glob file tool. Split
every path into **inside the ALLOWED SET**, **outside it**, and **deleted or renamed** (`D` or `R`). If you
hold the enumeration in a file, use a session scratchpad outside `C:\s\MS`, and say so.

**(d)** **Emptiness and size, by git object only.** For the ALLOWED-SET list: `git hash-object -w` over the
paths (on the command line, or with `--stdin-paths` fed from a scratchpad file outside `C:\s\MS`), then
`git cat-file --batch-check` over the printed identities. Neither command prints file content. **Any size
0 → STOP and report the paths. Any size over 50 MB → STOP. Report every size over 5 MB.** *(The size is the
blob's, after git's line-ending conversion — which is exactly what is committed.)*

**(e)** **Size of `cowork_handoff_entry_one_hundred_and_eighty_eight.md`** from 0(d), reported against
**19822** bytes (the writing side's staging call this sitting). **A difference is not a STOP**; if it
differs, say whether a line-ending conversion warning was printed for that path.

**(f)** **If a guard refuses any command in this task, STOP and report the refusal text verbatim. Do not
try another route.**

---

## TASK 1 — commit

**(a)** Stage **exactly** the ALLOWED-SET list, by explicit path. **No `git add -A`, `git add .`, or glob
reaching outside the list.** Do not stage deletions or renames; report them.

**(b)** Run `python tools/audit/changed_paths.py --staged` and compare the staged set against the list **as a
set, in both directions**. **Any difference → unstage everything and STOP.**

**(c)** Commit **verbatim — edit, reformat, re-wrap and normalise nothing** — with this message, followed by
the standing attribution trailer:

```
Second backup: CC session reports, research-paper text files, exemplar provenance (user-ordered, 2026-09-16)

Commits, as they stand on disk, the files the first backup's ALLOWED SET left out:
root cc_*.md files, docs/research_papers/BIBLIOGRAPHY.md and README.md, the
bwv1049_03_presto provenance record, and Cowork record files changed since 5d24edb5.
The .mscx exemplar is held back (recomputable from its tracked archive).
No NUL-byte check was run. No file content changed.
Dispatch: cc_instruction_second_backup_rerun_2026_09_16.md
```

---

## TASK 2 — push

`git push origin master`. **Never `--force`, never `--force-with-lease`, never push to `upstream`, no other
branch.** Rejected for any reason → **STOP; do not pull, merge, rebase or retry with force**; report the
exact error text. After success, `git rev-parse HEAD` and `git rev-parse origin/master` must be equal;
**not equal → report.**

---

## TASK 3 — the report, committed and pushed

**(a)** Write `cc_report_second_backup_rerun_2026_09_16.md` with: the pinned blob identity; premises 1 to 4,
each answered; the Task 0(c) enumeration in its three lists, **every path named**; the Task 0(d) result with
every size over 5 MB named; the Task 0(e) size; the commit identity and the `--staged` output; the push
result and the two identities. **Assert no count of your own acts; name the members.**

**(b)** Commit that report alone (message: `Report: second backup re-run, 2026-09-16`, with the attribution
trailer), push under Task 2's rules, and record the new `HEAD` and `origin/master` at the foot of your chat
reply.

---

## DECLARED BY THE WRITING SIDE

- **What this batch's own orders move:** the git object store (the pinned blob and the blobs 0(d) writes),
  the index and history (two commits), `origin/master` (two pushes), and one new file, its report. **No
  existing file's content is edited, and the spent dispatch is not touched.**
- **No `STATUS.md` entry, forward-bound re-aiming, `tools/audit/` regeneration or guard-set run is ordered.**
  The `STATUS.md` question stands with the user as the first report left it; if you judge a rule requires an
  entry, name it in the report, write none, and do not STOP.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

- Premise 1 or 4 fails, or `origin` is not the URL in premise 2.
- A size 0 or a size over 50 MB at Task 0(d).
- Any guard refusal in Task 0.
- Any difference between the staged set and the list at Task 1(b).
- Any push rejected.
- **Any instruction here found false at the objects.**

## WHAT THIS BATCH MAY NOT DO

Edit any file except its own report; delete any file; stage outside the ALLOWED SET; open, list, stage or
search anything under `docs/research_papers/polyph9-release/`; open the `.mscx`; run interpreter code that
reads repository files; create, flip or discard any open-items row; write any decisions-register entry; touch
`src/`; build, test or measure anything; force-push, pull, merge or rebase.
