# The L0+L1 boot pack — the spent packs frozen, the pack rendered (report, 2026-08-31)

> **STATUS: DONE.** Written by the CC run of `cc_instruction_l0l1_boot_pack_second_2026_08_31.md`,
> executing **Ruling 17** of `cowork_rulings_2026_08_31_decision_surface_sitting.md`.
>
> **★ THE HEADLINE.** `--check` is **GREEN**, and it is green for exactly the three reasons §7
> names and for no other. The two spent packs were **NOT re-rendered**: they are FROZEN at the
> blobs Task 1 recorded, and every one of their **fourteen** files still carries its recorded blob,
> proven by re-hash after the render. The `l0-l1` pack **exists** — ten files, the ruled six intact
> and in their ruled order, then the three extras. The filter was widened by the **one** ruled
> anchor and no other. The four residuals are repaired.
>
> **★ AND THE FREEZE IS ESTABLISHED, NOT DECLARED.** Six falsification cases were run against it and
> all six behaved as required, including the two directions of the directory comparison. A guard
> that has never been seen to fire is unfalsified, not established (#19).
>
> Per the OI-222 pointer convention this report POINTS at its artifact,
> `tools/audit/l0l1_boot_pack_freeze_and_render.json`; no count and no hash is restated here
> (**D-431**).

## Task 0 and Task 1 — the start state, established before anything asserted on it

This is the dispatch's own standing fix, and it is why this batch could finish where the first
writing could not: **the start state of every check this batch asserts on was established first.**

**`--check`'s output was taken line by line at HEAD, before this batch touched anything.** The
relayed list is **CONFIRMED, not corrected**: exactly six red lines — the manifest, members (2) and
(4) of both existing packs, and the missing `l0-l1` directory. **No seventh appeared**, and none
appeared at any later point either.

**The fifteen blobs were recorded per file**, and one property was established with them rather than
assumed: for every one of the fifteen, `git hash-object` and `git hash-object --no-filters` **agree**.
That settles what the recorded digest is the digest *of* — the bytes on disk, not a
newline-normalized form — and it is what makes the freeze reproducible from outside this project's
own tools.

**One thing Task 1 did not order and this batch measured anyway, because the dispatch resolves the
manifest line by REGENERATION and a session that regenerates without knowing what will move cannot
say what it changed.** The on-disk manifest was diffed against a freshly built one, in memory,
before anything was written. **The difference is exactly two kinds:** four scalar count fields —
`lines_rendered` and `characters` for members (2) and (4) of the two existing subjects, moving
because `CLAUDE.md` and `cowork_audit_protocol.md` have grown — and the whole absent `l0-l1` block.
Every figure is at the artifact.

**The previous batch's extension is PRESENT and as reported**, each item re-established at
`tools/audit/gen_derivation_boot_pack.py` by its own symbol rather than taken on trust: the
per-subject `EXTRAS` table rendering after the ruled six; `removals` and `cuts` with both-ways
verification; the derived read-me count; the STOP on the ruled six; and `l0-l1` in all four authored
tables with an empty withheld family. **No STOP.**

## Task 2 — the freeze, built as a mechanism

`FROZEN` is a fifth authored table: per spent subject, one digest per file, each subject carrying
its **finding, its date and its reason** — the same D-677 shape every other authored input in this
tool answers, with the same STOP behind it.

- **`write_all` writes nothing into a frozen subject's directory.** Not the pack, not one file of
  it. Proven at the objects by the post-render re-hash, and mechanically by the skip itself.
- **`check_all` verifies a frozen subject against its recorded digests instead of against a
  re-render**, in **both directions** — every recorded file present and equal, and no file present
  that the freeze does not record.
- **A mismatch RAISES rather than joining the drift list.** A frozen file that has moved is not
  staleness to be regenerated away; it is the record of a completed derivation having been altered,
  and D-646 calls for a hash STOP.

**Why the digest is the git blob hash and not a bare content hash, stated because it is the whole
value of the choice:** `git hash-object <file>` reproduces every recorded value from outside this
tool, so the freeze does not rest on the word of the generator that declares it (#19).

### ★ ONE DECISION THIS BATCH HAD TO TAKE, DECLARED RATHER THAN SLIPPED IN

§2's last bullet keeps both subjects' manifest entries. Those entries are built by the same code
path as every other subject, **from today's sources** — so after regeneration a frozen subject's
member records state counts for a render that is **not the one on disk**. That is a falsity in a
generated record, and leaving it silent would put the tool's own manifest at odds with the directory
it describes.

**It is disclosed, not shipped silently.** Each frozen subject's entry now carries `★_FROZEN`,
which states that the directory is not re-rendered, that the member records below it describe what
the sources *would* render, and that **the digests are the authority on what the directory holds**.
**The alternative — regenerate and say nothing — was available and is recorded here so the user can
take it instead.** Two further alternatives were considered and are recorded because an excluded
alternative is evidence about the choice: **freezing the manifest entry itself** would require
authoring each spent subject's whole record as data, duplicating the `VERDICTS` table (#6); and
**replacing the entry with a stub** is what §2's last bullet forbids in terms.

## Task 3 — the one further removal

Added by anchor text: **`This is adopted from this project's material`**. It matched **exactly
once**, sits inside its own `*(`…`)*` pair, and is verified in both directions like the two before
it. Its effect is measurable and was checked: the charter member is exactly **161 characters**
shorter than the previous batch's dry render, which is the number of characters this removal takes
out.

**Nothing else was added to the filter, and no new candidate was found.** The sweep's other
candidates stay in place **by ruling**, and the grounds are written into the tool beside the filter
so a later reader meets them there: DP-N's two disagreeing analyses and DP-Q's three exemplar
analyses describe **corpus material** rather than what this project's system does and are
load-bearing evidence for their design points; the two references to the ledger are **moot**, member
(9) carrying that document whole.

## Task 4 — the four residuals, under the relaxed bar

1. **`the_pack_files_in_order` is DERIVED PER SUBJECT**, from the member records already built —
   one derivation of a pack's file list, not a second walk of `MEMBERS` and `EXTRAS` beside the
   first (#6).
2. **`the_rulings_it_executes`, `the_STOPS` and `what_is_AUTHORED`** are brought to the tool's
   actual state. **`the_STOPS` went from eight entries to twelve**, and the docstring's own list
   gained the freeze STOP so the two cannot drift apart.
3. **The read-me's stop-and-record count is derived.** **Only the count moved** — the rule the
   clause states is unchanged, and the boundary clause above it is untouched.
4. The docstring block that recorded these four as knowingly-unrepaired is replaced by one
   recording the repair and naming the ruling that permitted it. Leaving it would have been a new
   falsity of exactly the kind it was written to prevent.

**★ ONE WIDENING BEYOND THE LETTER, REPORTED IN THE SAME ACT (the D-654 shape).** "Brought to the
tool's actual state" is the bar, and `the_rulings_it_executes` did not merely lag the extension — it
**under-named the tool before the extension too**. Two rulings this generator has been executing
since before this batch were absent from it: the 2026-08-23 member-two second-leak ruling, which is
why member (2) carries a second withheld passage, and Ruling 2(a) of the 2026-08-24 sizing-leak-list
sitting, which is what licenses `criterion_block`'s empty branch. **Both are now named.** Naming
only the new ones would have left the field false in the direction it was already false.

## Task 5 — the render

`l0-l1` renders **ten files**: the read-me, the ruled six in their ruled order, and the three extras
at 7, 8 and 9. Both filters passed their both-ways verification on the render, as the extension
already requires. The charter member's three removals are **absent from the rendered text**, checked
at the rendered object and not only at the tool's report of itself (#15).

**What the read-me a blind session opens now says, checked at the object:** it heads its listing
*"The nine files of this pack, in order"* and lists nine; its stop-and-record clause says *"one of
these nine"*; and its what-was-cut section states truthfully that **three passages** were taken out
of the charter member and **five whole sections** out of the extracts member, deleted with no mark —
while saying, correctly, that **nothing is held back as an answer to be compared against**, this
subject's withheld family being empty.

**The heading counts MEMBERS, not directory entries, and that is the pre-existing convention rather
than a defect this batch introduced:** `harmony-boundary` reads *"The six files of this pack"* over a
directory of seven, and the read-me's own next sentence distinguishes itself from the listed files —
*"Together with this file they are the whole of your read"*. It is stated here so the nine-over-ten
arithmetic is not mistaken for a slip.

## Task 6 — Ruling 17(d)

Nothing was done. The what-was-cut section's derivation from the counts stands as CC built it and as
the ruling ratified it, and this batch's own render exercises it: the `l0-l1` section says
**"three passages"** because three were removed, not because a subject name was matched.

## The freeze, established under #19

Six cases were run against `verify_frozen`, each perturbing the **authored table in memory only** —
no repository file was written, moved or deleted. **All six behaved as required:** the baseline
verifies; a moved digest STOPs; a recorded file missing from the directory STOPs; a file present
that the freeze does not record STOPs; a freeze record lacking its reason STOPs; and a `FROZEN`
entry naming a subject the tool does not build STOPs at `build`. The probe's whole output is at the
artifact.

**What this does NOT establish:** that the frozen blobs are the *right* content. They are the content
the packs carried at this batch's start, and that the two sessions ran on them is a fact of the
record, not something this batch measured.

## Done — against Task 1's findings, line by line

**`--check` is GREEN, exit 0.** Each of the six red lines Task 1 recorded:

| Task 1's red line | Resolved by |
|---|---|
| `derivation_boot_pack.json does not re-derive` | **Regeneration**, which Ruling 17(c) permits |
| `harmony-boundary/02…` does not re-render | **The freeze** — verified against its digest, not re-rendered |
| `harmony-boundary/04…` does not re-render | **The freeze**, same ground |
| `scoring-model/02…` does not re-render | **The freeze**, same ground |
| `scoring-model/04…` does not re-render | **The freeze**, same ground |
| `l0-l1: the pack directory is missing` | **Task 5's render** |

**It is green for no other reason, and that was checked rather than assumed.** No red line outside
Task 1's list appeared at any point. Nothing was made green by relaxing a check: for a **live**
subject the manifest comparison, the directory-listing comparison and the per-file byte comparison
are all exactly as they were. What changed is that a **frozen** subject is verified against digests
instead — which on the question the freeze asks is **stricter**, since it also STOPs on a file
added to the directory.

**Also done:** the ruled six stand intact and in order for every subject, enforced by a STOP rather
than promised; the new anchor matched exactly once and verified both ways; **the two frozen
subjects' fourteen files are byte-identical to the blobs Task 1 recorded, proven by re-hash**; and
**no STOP was met on any act of this batch** — every render, every check and every filter passed.
The only STOPs that fired anywhere were the **six deliberately provoked in the falsification probe**,
which is what establishes the freeze rather than a failure of it.

## The footprint, as it actually stands

**Created:** `tools/audit/derivation_boot_pack/l0-l1/` and its ten files; this report; and this
batch's artifact `tools/audit/l0l1_boot_pack_freeze_and_render.json`.

**Edited:** `tools/audit/gen_derivation_boot_pack.py` only. **Regenerated:**
`tools/audit/derivation_boot_pack.json`. The forward bound's own per-batch re-aiming was not needed
and was not run.

**Written into NEITHER existing pack directory** — proven by re-hash, not asserted.

**Read and never written:** `FRAMEWORK.md`, the five extracts, `EMPIRICAL_FINDINGS_LEDGER.md`.
**`FRAMEWORK.md` IS NOT AMENDED** — the filtering governs what a pack carries, never what that
document says.

**Not done at all:** no build, no test, no golden, no measurement of the analysis, nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; no governing document amended; **no
open-items row created, flipped or discarded**; **no decisions-register entry and no `D-NNN`**; the
workbook not opened; **no score staged, copied or moved**; no brief written; no session booted.

**The pins.** This file and every file §0 names were pinned before any other act and **re-hashed at
the close: all eight reproduce exactly.** No read disagreed with its pin.

**The tracked-modification assumption, DECLARED and not established.** The session-start snapshot
the harness supplied showed exactly two tracked modifications —
`cowork_rulings_2026_08_31_decision_surface_sitting.md` and
`tools/audit/gen_derivation_boot_pack.py` — which are the two §9 names by name, and no other.
**That bound is DECLARED from that snapshot, not established by a shell `git status`**, which the
standing rule forbids (#24: where a condition cannot be established at an inspectable object the
session may reach, it is declared and the result stands with the bound attached).

## The self-check

**The diff was read on disk, blob to blob by explicit hash, not from the memory of writing it.**
Against the last commit the one edited file is **753 insertions and 14 deletions**, of which the
previous batch's report accounts for eleven; **the three remaining are this batch's and each is
named**: the read-me's hard-coded *"these six"*, replaced by the derived count (Task 4(3)); the
global `the_pack_files_in_order`, replaced by the per-subject derivation (Task 4(1)); and
`drift = []` re-annotated as `drift: list[str] = []` beside the new `frozen_checked` dict, which is
a type annotation and no behaviour change.

**The bound on that diff, stated because it is a real limit.** The previous batch's post state was
never committed and this batch did not pin it, so the isolated previous-batch-to-now diff was not
available and the diff was taken against the last commit instead. A line the **previous** batch
added and this batch replaced therefore nets out as an insertion rather than showing as a deletion.
Three such replacements were made — the residuals docstring block, STOP-11's terminal punctuation,
and the filter's own comment — each ordered by Tasks 3 and 4, and each performed by an
exact-match-or-fail replacement, which is a mechanical guarantee rather than a recollection.

**And the substance was verified at the output surface rather than at the diff (#15).** The dry run
before the render showed the extended generator still rendering **five of `harmony-boundary`'s seven
files byte-identically** to their frozen blobs — including member (5), whose rendering exercises the
whole withheld-family, verdict, cross-reference and leak machinery, and the read-me, whose rendering
exercises both derived counts and the what-was-cut section. **The only two that differ are the two
whose sources grew.** That is stronger evidence than the diff that no mechanism was disturbed.

Checked against the principles. **#6** — one derivation of a pack's file list, not two; the freeze
lives in one function called from one place; `check_all` gained no second path for live subjects.
**#12** — the freeze exists so that no completed derivation's record is overwritten, and the
superseded docstring block was replaced by one recording what it superseded rather than by silence.
**#13** — the manifest's would-be falsity about the frozen subjects was surfaced and disclosed
before it could be built around. **#15** — the removals were verified at the rendered object and the
freeze at the files, not at the tool's assertion about itself. **#17(b)** — the prediction was
written first **and content-addressed before the measured block existed**, so its ordering is
checkable and not merely asserted. **#17(f)/D-431** — no figure is transcribed into this report;
each is at the artifact, and the artifact's own digest list is read from the tool rather than typed
beside it. **#19** — the freeze was falsified in six directions before being trusted, and its digest
form was chosen so an independent tool can confirm it. **#24** — the tracked-modification bound is
declared with its ground. **`DEFECT_TYPES.md`** — every scope is stated on its own claim rather than
left to read as total (DT-26): what the freeze establishes and what it does not, what the pre-render
manifest diff measures, and the bound on the self-check's diff.

---

*Provenance: CC, 2026-08-31, under `cc_instruction_l0l1_boot_pack_second_2026_08_31.md`. Every
working-tree read through the file tools; shell used only for git object queries by explicit hash,
for `git hash-object`, for running the generator, and for three scratchpad drivers. The artifact is
`tools/audit/l0l1_boot_pack_freeze_and_render.json`; no figure of it is restated here (#17f,
D-431).*
