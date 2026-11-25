# The stretch verification scripts (L3 application, Task 3 stretches)

> **STATUS: NOT YET ESTABLISHED.** Written 2026-11-24 by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_two_hundred_and_forty.md`, on the user's decision of that
> date (alternative B of decision 1, recorded in entry 1241): the verification scripts become ONE committed tool,
> established once, then staged and run by every verifying sitting instead of being rewritten each time. Until the
> establishment below has been run and recorded in a handoff entry, nothing may rest on these scripts (#19).

## What they are for

A Cowork sitting that verifies a stretch Claude Code has committed uses them, over STAGED copies only, with
`python3 -I`, on the user's leave for that sitting. They write nothing to the device. Every script takes its paths as
arguments; none has a repository path built in.

| Script | Does |
|---|---|
| `gitobj.py` | reads loose git objects from a staged `.git/objects`, recomputing each SHA-1; prints a commit's text or a tree's entries |
| `treediff.py` | compares pairs of tree objects, one level each, printing the entries that differ |
| `blobhash.py` | the git blob identity of files as they are, with size, line-feed count and carriage-return flag |
| `blobout.py` | writes a blob's content (hash recomputed first) to a file, e.g. the Task 2 commit's reading file |
| `rebuild.py` | rebuilds the reading file from a committed base blob and the instruction's own text; optionally compares with the file on disk |
| `counts.py` | the six standard line counts, *as proposed*, any record names given, and added/deleted lines against other files |

## How a verifying sitting uses them

1. Stage this folder, the three git reference files, the commit objects (path: first two characters of the hash as the
   folder, the other 38 as the file name, built by slicing, never retyped), and the trees on each changed path one
   level per staging call.
2. `gitobj.py` on the commits: each hash recomputed, parents in order, subjects compared with the instruction's.
3. `treediff.py` from each commit's parent root tree to its own, down every changed path: each act changes only what
   the instruction says it lands.
4. `rebuild.py <objects> <previous reading-file blob> <instruction> <out> <reading file on disk>`: the printed blob must
   equal the instruction's expected blob and the commit's tree entry, and the compare must print IDENTICAL.
5. `blobout.py` for the Task 2 commit's reading-file blob, then `counts.py <rebuilt> --base <previous> --task2 <task 2>`
   plus the record names: every figure as the instruction gives it.
6. `blobhash.py` on every landed file: each equals its committed blob.
7. Read Claude Code's report in FULL with the file tools; the scripts do not replace that.

## Establishment (owed before first use — #19)

The first verifying sitting that uses these scripts runs them on the stretch-18 objects, whose results are known from
the hand-made verification in entry 1241 and, for the blob, from the simulated edit in entries 1239 and 1240, and
records the outputs in its handoff entry. Expected:

- commits `e498e84b2510ba040975b64d35738a7dd651b5df` (parent `4edf4b9553b542a6e146302101d49b02bfbd8fe3`),
  `1e18431dc71d7fe0cf2c0a6030f32cebde282a83` (parent `e498e84b…`), `d3df2b7eefb00758291a8d1161027764ca7491ed` (parent
  `1e18431d…`), each "hash ok";
- `treediff.py` on `de343e362eb5b62f22a978cf887c15b73acc565f:f59e62bf1cbeac54a6e806790a8c6f92ed3648e4`: only
  `cowork_comparison_l3_reading.md`, `0c827080c34dc4bfe7fd2cb6bb487073de9815f9` → `12e91510f50e7fa1c0262f3c9f64634935a7de00`;
- `rebuild.py` from `0c827080…` with session 27's instruction
  (`records/cc/instructions/cc_instruction_l3_application_session_27_task_3_stretch_18_2026_11_24.md`, blob
  `2be384ec534f71e4da6e9dfcf22440528f40a054`): 10 rows, 11 lines, blob `12e91510…`, 5,336,157 bytes, 84,758 line feeds,
  and IDENTICAL to the stretch-18 file;
- `blobout.py` on `48e24b2f82f76c57cfd5cd14b86780c567db0f70` (5,135,614 bytes); `counts.py`: 535 / 36 / 53 / 26 / 1 / 1,
  *as proposed* 128, the modal-counts record name 11; against `0c827080…` 23 added and 1 deleted; against the Task 2
  blob 1,319 added and 4 deleted.

**One negative test belongs to the establishment too:** change one character in a copy of the instruction's §3.2 code
block and re-run `rebuild.py` with the copy; the compare must print DIFFERS. Without it a compare that always says
IDENTICAL would pass the test above.

## Limits — where the scripts STOP or do not reach

`rebuild.py` applies only: lines placed after the blank line that ends a row's `*PROPOSED DISPOSITION.*` paragraph, at
rows that carry no earlier `*RULED` or `*RECORDED` line, taken from code blocks headed `*Row <n>.<m> — <k> line(s)`;
and the in-progress line at line 54. It STOPS on anything else it can detect (see its docstring). It does NOT apply
transfer-list (§10) entries, audit-question (§11) lines, lines at rows with earlier lines, or any other change. **A
stretch whose instruction orders one of those needs `rebuild.py` extended first, and the extension established again by
the same kind of test** — the writing sitting that writes such an instruction says so in its handoff entry. A code block
headed `*Row …` that is not a row's lines would be applied as if it were; an instruction keeps that heading for row
lines only.

Claude Code does not use these scripts: it writes from the instruction's prose. That is what keeps the rebuild an
independent check, and why a placement bug shared by the writing side's simulation and the verifying rebuild would
still be caught, as a difference from Claude Code's file.
