# CC INSTRUCTION — map every reference to the root record files before they are moved, 2026-09-16 (READ-ONLY)

**THE BASE.** The current commit should be `5d24edb565b2e0e9efc92e082c163112bd97087f` on branch `master`.
**Check this first (Task 0).**

**WHY THIS EXISTS.** The user ruled on 2026-09-16 that the Cowork and CC record files **cannot stay in the
repository root**. The proposed destination, put to the user with this dispatch, is:

```
records/
  cowork/
    handoff/        cowork_handoff_entry_*.md, cowork_handoff.md, cowork_handoff_archive.md
    rulings/        cowork_rulings_*.md, cowork_ruling_*.md
  cc/
    instructions/   cc_instruction_*.md
    reports/        every other root cc_*.md
```

The other root `cowork_*.md` files — design documents, surfaces, protocols, commissions — are **not** in
that move: several are homes the decisions register and `ARCHITECTURE.md` delegations point at, and
`CLAUDE.md`'s decisions-register section states, at rule (h), that "(g)'s guard is untouched: the
delegation confers, and only the user writes a delegation into `ARCHITECTURE.md`." They are mapped here so that a later step can be ruled.

**The move, the reference fixes, the regeneration and the backup commit and push are a SECOND dispatch**,
written from what this batch reports. The writing side cannot list the repository root and has run no
search of the tools, so it cannot write exact edits without this map. **This batch changes nothing.**

**This dispatch itself is filed at `records/cc/instructions/`**, and its report goes to
`records/cc/reports/`, so this batch adds nothing to the root.

**The writing side does not touch this file while the batch runs.**

---

## THE ROUTE RULE

Read with the file tools only: **Glob** to list, **Grep** to search, **Read** to open. **No shell text
utility and no interpreter code on any file, no shell variable standing for a path, no redirection from a
file.** The only commands are the git commands in Task 0. **Never open, list or search anything under
`docs/research_papers/polyph9-release/`, `scratch_artifacts/`, `external resarch summary/`, `Claude outputs/`,
`Codex research inventory/` or `.git/`** — exclude them from every Grep and Glob with a negated glob. **If a
guard refuses anything, STOP and report the refusal text verbatim.**

---

## TASK 0 — start state, pinning

**(a)** `git hash-object -w records/cc/instructions/cc_instruction_root_records_reference_map_2026_09_16.md`;
record the identity; take later reads of this dispatch from `git cat-file blob <identity>`.

**(b)** `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD`. **Not `master` at the base → STOP.**

---

## TASK 1 — the population to move

With Glob, at the repository root only (no `**`), list every file matching each pattern, **each file named**:

- `cowork_handoff_entry_*.md`; `cowork_handoff.md`; `cowork_handoff_archive.md`
- `cowork_rulings_*.md`; `cowork_ruling_*.md`
- `cc_instruction_*.md`
- `cc_*.md` not matching `cc_instruction_*.md`
- every other `cowork_*.md` (listed separately: **not** in the move)

For each listed file, say whether it is tracked, from `git ls-files -- "<name>"` (at most forty names per
command, written literally). **Report files matched by none of the patterns only by the patterns above;
list nothing else at the root.**

---

## TASK 2 — every reference to those files

**(a) Text references.** Grep the whole repository (with the exclusions above), `output_mode: "count"`,
`head_limit: 0`, for each of these regular expressions separately:

1. `cowork_handoff_entry_[a-z_]+\.md`
2. `cowork_handoff(_archive)?\.md`
3. `cowork_rulings?_[A-Za-z0-9_]+\.md`
4. `cc_instruction_[A-Za-z0-9_]+\.md`
5. `cc_[A-Za-z0-9_]+\.md`
6. `cowork_[A-Za-z0-9_]+\.md` (for the files NOT in the move)

Report every file with a count, per expression, **every file named**.

**(b) Code that finds these files by location.** Grep, `output_mode: "content"`, `head_limit: 0`, over files
matching `*.py`, `*.mjs`, `*.js`, `*.sh`, `*.ps1`, `*.bat`, `*.cmake` (same exclusions), for:
`cowork_`, `cc_instruction`, `cc_report`, `cc_\*`, `listdir`, `glob\(`, `iterdir`, `scandir`. **Report every
hit line with its file and line number**, and for each file say, from reading the hit lines and their
surrounding function with the Read tool, whether the code **(i)** builds a path to one of these files at the
root, **(ii)** scans the root for them, **(iii)** only mentions a name in a string, comment or docstring, or
**(iv)** is unrelated (for example `glob(` over another directory). Quote the lines that decide it.

**(c) Classify every file that Task 2(a) or 2(b) found**, one line each, into exactly one class:

- **CODE** — source that runs (the Task 2(b) file types).
- **GENERATED** — a file a generator writes. Name its generator if the file or the generator's docstring
  states it; say "generator not stated" otherwise. **Mark FROZEN** any file under a directory whose name
  begins `snapshot_`, or that a generator protects with a hash STOP (D-646) as far as the generator's
  docstring states it.
- **LIVE** — a document a session is sent to in order to act, under branch two of D-674 (the filing
  convention in `cowork_design_doc_template.md`, read there with the kind list it sits beside, D-659).
- **DATED** — a dated report, dispatch, handoff entry, rulings record or other record of an act, under
  branch one of D-674 (its body is never rewritten).
- **UNDECIDED** — the two branches do not decide it. Name it and give the reason; **not a STOP.**

Give the reason for each LIVE and UNDECIDED call in one line. **For the files in the move themselves,
class DATED may be given as one statement covering the whole population named in Task 1**, with any
exception named.

---

## TASK 3 — the report

Write, **with the Write file tool**, `records/cc/reports/cc_report_root_records_reference_map_2026_09_16.md`,
carrying: the pinned identity; Task 0's answers; Task 1's lists with tracked status; Task 2(a)'s counts;
Task 2(b)'s hit lines with their verdicts and quotes; Task 2(c)'s classification. **Assert no count of your
own acts; name the members.** A per-expression total may be stated only as a sum of the listed counts.

**Do not commit, stage or push anything.** Report the report's path and the two Task 0 identities at the
foot of your chat reply.

---

## DECLARED BY THE WRITING SIDE

- **What this batch's orders move:** the git object store (the pinned blob) and one new file, the report,
  in a new directory. **No existing file is edited, moved, staged or deleted.**
- No `STATUS.md` entry, no regeneration, no guard-set run.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

- Task 0(b) not at the base.
- Any guard refusal.
- **Any instruction here found false at the objects.**

## WHAT THIS BATCH MAY NOT DO

Edit, move, stage, commit, push or delete any file other than writing its report; open, list or search the
excluded locations; run any generator, guard or build.
