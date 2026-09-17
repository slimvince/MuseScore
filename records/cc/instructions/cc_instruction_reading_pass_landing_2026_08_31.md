# CC dispatch — land the reading pass, execute Rulings 2 and 3, prepend the staged handoff entries

> **Written by the Cowork writing side, 2026-08-31, on the user's direction of that date.** The user
> opens this with Claude Code; no session starts it and no session lands anything itself (the
> 2026-08-26 role ruling, **D-252**).
>
> **Nothing in this dispatch is a decision.** Every text change it orders executes a ruling the user
> has already taken, and the ruling record is where the change's content comes from — never this
> file's paraphrase of it.

## Task 0 — pin first, then establish. Write nothing.

**The user's opening line carries the pin order** (the ratified standing form, P-2). Pin THIS
dispatch to a blob before reading it, and take every later read of it from that object.

Then, before any act:

1. **Establish the tip.** Read `master` and `origin/master` at the object and report both. If they
   differ, **STOP**.
2. **Run the FULL guard set in CHECK mode** and report the summary. **The declared start state is
   75 run, 67 passing, 8 failing** — the three long-known
   (`gen_filing_convention_application.py`, `apply_soft_discard.py`, `apply_residue_discard.py`)
   plus five stop-reported ordered-edit reds (`gen_artifact_inventory_surface.py`,
   `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py` — which crashes on a
   `KeyError` — `gen_derivation_boot_pack.py`, and `decisions/gen_cluster_dispositions.py --verify`,
   whose cited line number drifted while its quote stayed intact). **A ninth failure is news:
   report it and STOP.** Do not repair any of the eight; they are the known start state and their
   repairs are separately owed to the user.
3. **Enumerate the working tree** — tracked modifications and untracked paths, both — and report the
   enumeration before Task 1. This dispatch's Task 2 works from that enumeration, never from a list
   typed into this file.

## Task 1 — the two ruled corrections to `FRAMEWORK.md`

**Both are the user's rulings of 2026-08-31, recorded at
`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3a and §3b. Read that record, and the
surface each ruling names, AT THE OBJECT and take the correction's content from there. Do not take
it from this dispatch, which deliberately paraphrases and is not the source.**

- **Ruling 2 (V4), Option A — correct minimally.** The clause at `FRAMEWORK.md` §5, L1, *"Why metric
  strength earns its place"*, is corrected to the primary's own three-level gradient as the ruling
  states it, **with the former wording preserved in place (#12)**. **Option B is declined and its
  content must NOT enter the charter** — the ruling says why in terms. The supporting case is
  `reading_pass/stop_v4_divergence_2026_08_30.md`.
- **Ruling 3 (DP-K's second ground), Option B — qualify in place and add the on-domain evidence.**
  At `FRAMEWORK.md` §9, DP-K's second ground is narrowed to what its primary supports and the two
  on-domain findings are added as further grounds, **each carrying its read grade** — one RELAYED,
  one DECLARED PARTIAL at chapter level. Former wording preserved (#12). **DP-K itself is not
  reopened and its first ground is untouched.**

**Bounds on this task.** `FRAMEWORK.md` is a ratified document and these are the only two edits
authorised anywhere in it. Both must be **proven additions-plus-preserved-former-wording at the
blob-to-blob difference** — no deletion line except where a ruling's own preservation form requires
the old text to move rather than vanish, and if it does, the moved text must be shown intact at its
new place. **No other line of `FRAMEWORK.md` changes. No `D-NNN` is allocated and no register entry
is written** — the rule-(c) suspension stands
(`cowork_register_rule_c_suspension_2026_08_28.md` is the route).

## Task 2 — track the untracked population

Work from Task 0's enumeration. Classify every untracked path into one of three, and report the
classification in full before adding anything:

- **(i) The line's records and outputs — TRACK.** The reading pass's own files
  (`reading_pass/` — the population, the fetch record, the continuation file, the STOP memo, the
  extracts, the second-pass extracts, the cross-checks, and anything else the pass wrote there), the
  findings surface at the repository root, the decision and ratification surfaces under
  `ratification_surfaces/`, the ruling records at the root, and the commissions at the root
  (`cowork_reading_pass_commission_2026_08_30.md`,
  `cowork_reading_pass_remedial_commission_2026_08_31.md`,
  `cowork_rulings_2026_08_30_detail_phase_opening_sitting.md`,
  `cowork_rulings_2026_08_31_decision_surface_sitting.md`). **This is the whole point of the batch:
  the entire evidence base of the detail-specification phase currently exists in exactly one place,
  untracked, on one machine.**
- **(ii) The staged handoff entry files — NOT tracked as files.** They are Task 3's inputs and are
  deleted there once their prepend is proven. Their content survives at their pinned blobs and
  inside `cowork_handoff.md`.
- **(iii) ★ THE HELD PAPER BINARIES under `docs/research_papers/reading_pass_2026_08/` — ESTABLISH
  BEFORE DECIDING, AND STOP IF YOU CANNOT.** `docs/research_papers/BIBLIOGRAPHY.md` maintenance rule
  3 states that **PAYWALL-tier copies must never enter a public repo**, and `origin` is the user's
  public fork. **Establish at the objects whether the existing fifty-eight PDFs under
  `docs/research_papers/` are tracked at HEAD, and by what mechanism the tree currently keeps them
  in or out** (a `.gitignore` entry, or their simple absence from the index). **Then treat the new
  folder exactly as the established convention treats the old one, and report which convention you
  found and how you established it.** If the convention cannot be established at the objects — if
  the existing copies are tracked in a way that does not settle the new ones, or if the new folder
  mixes tiers the old one does not — **STOP and put it to the user.** Do not decide a redistribution
  question, and do not add a `.gitignore` rule of your own invention.

**No signature-table change, and no artifact-inventory repair.** Adding files will very likely move
what `gen_artifact_inventory_surface.py` derives, and that check is already one of the known eight
reds. **Run it after the additions and REPORT what it says — do not repair it, and do not touch the
signature table**, whose amendment mechanism is reserved to the user (his act, exercised once for
`FRAMEWORK.md` and once for the workbook folder). The classification of these new paths is a
user act that follows this batch; this batch establishes what the check says once they are there.

## Task 3 — prepend the staged handoff entries, in order

**Four entries are staged and none has been landed:** `cowork_handoff_entry_eighty_two.md`,
`cowork_handoff_entry_eighty_three.md`, `cowork_handoff_entry_eighty_four.md`, and
`cowork_handoff_entry_eighty_five.md`. They prepend into `cowork_handoff.md` **in that order** —
eighty-two first, eighty-five last, so the newest block ends up on top. The eighty-first entry is
the newest block inside `cowork_handoff.md` itself until this batch runs.

**Use the same construction the phase-close batch used** — the ratified splice, whose inputs are
read at **content-addressed git objects by explicit hash** and which reads no working-tree file at
all, with the character arithmetic proven exact and the difference insertions-only. **Locate that
tool in the tree and establish it before using it; if you cannot locate or establish it, STOP** —
do not retype an entry and do not write a new splice of your own design.

Because the construction reads blobs, the entries must exist as objects before they can be spliced:
**follow the phase-close batch's proven commit order rather than forcing one commit** — land the new
files first so their blobs exist, then splice, then land the splice and the staging-file deletions.
**Each staging file is deleted only after its own prepend is proven**, and the resulting
`cowork_handoff.md` entry count is established at the resulting object.

## Task 4 — land and push

Land in as few commits as the construction above allows, each with a provenance-stamped message.
**Re-establish every landed blob at the commit object equal to its pin.** Push, and **verify
`origin/master` by two independent routes.** Report every commit identity; the writing side relays
identities and never resolves them.

## Task 5 — the report

Write `cc_report_reading_pass_landing_2026_08_31.md` into the tree and land it. It carries: Task 0's
pins, tip and guard summary; the tree enumeration; the Task 1 blob-to-blob differences with the
additions-only proof; Task 2's full classification with the redistribution convention you
established and how; the artifact-inventory check's post-addition output, unrepaired; Task 3's
splice proofs and entry count; and every commit identity. **Per the OI-222 pointer convention the
`STATUS.md` entry is a POINTER — no count, no identity and no rendered value is restated in it
(D-431).** Update `STATUS.md` in the same batch, maintaining its own forward bound (only the latest
batch's entries stay; the rest move to `STATUS_ARCHIVE.md`).

## Standing bounds on this whole batch

**Do not:** derive or amend any specification; open the workbook
(`external resarch summary/external research.xlsx`) in any portion, or rename or move that folder;
touch any file under `tools/corpus/` or `tools/robust_stop/`; run any measurement, golden, build or
test; change any tool source **except** where a task above names one, and none does; create, flip or
discard an open-items row; write a register entry or allocate a `D-NNN`; repair any of the eight
known guard failures; edit `FRAMEWORK.md` anywhere but the two ruled clauses; or edit the reading
pass's own record files, which are landed as they stand.

**Every departure from this dispatch is DECLARED in the report, never absorbed silently.** If a task
cannot be performed as written, STOP at that task and report; the later tasks are not attempted
around it unless they are independent of it, and independence is stated rather than assumed.

---

*Provenance: written by the Cowork writing side, 2026-08-31, on the user's direction that the pass's
output be committed at a proper point. Its factual basis was read at the files this session:
`cowork_handoff_entry_eighty_two.md`, `cowork_handoff_entry_eighty_three.md`,
`cowork_handoff_entry_eighty_four.md`, `cowork_rulings_2026_08_31_decision_surface_sitting.md`
§3a–§3b, `cowork_reading_pass_findings_2026_08_31.md`, `reading_pass/population.md`, the
`reading_pass/` listing, and `docs/research_papers/BIBLIOGRAPHY.md` whole. No shell command was run
on the repository or on any staged copy of it, and no git object was resolved by the writing side.*
