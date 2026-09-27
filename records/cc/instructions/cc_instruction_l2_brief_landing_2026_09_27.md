# CC INSTRUCTION — THE L2 BRIEF LANDING: RULING 1 OF THE LEAK-LIST SITTING, THE RE-RENDER, THE CUT INPUT CONTRACT, THE CLOSE (2026-09-27)

> **STATUS: RELEASED 2026-09-27. Run it from Task 0 in order.** Written and source-checked by the Cowork
> sitting booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_three.md`.
> **If any expected result does not appear, stop at that step and report it. Do not continue to the
> next one, and do not resolve a bar that contradicts a task.**
>
> **THE WRITING SIDE'S RESTRAINT, declared.** This dispatch is final at hand-over. The writing side
> will not touch it, nor any file it names, while this batch runs. The one file the writing side writes
> after this dispatch lands and before hand-over is its own handoff entry,
> `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_four.md`, which is why Task 0
> states no size for it.

**What this batch does.** Five things, in this order:

1. commits the Cowork side's uncommitted records, the draft L2 brief and this dispatch (Task 0);
2. carries **Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md`**
   into `tools/audit/gen_derivation_boot_pack.py`: the cross-reference rule searches only `title`,
   `verbatim` and `plain` **for every subject that is not FROZEN**; frozen subjects keep the five-field
   search (Task 2);
3. re-renders the L2 pack and proves the three frozen subjects did not move (Task 3);
4. carries **Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md`**:
   writes the INPUT CONTRACT — `cowork_derived_specification_l0_l1_2026_09_03.md` copied verbatim with
   ONE named passage removed — and runs a search over it whose hits go to the user **as the cut list, not
   acted on** (Task 4);
5. runs the standing close — `STATUS.md`, the forward bound, the regenerations a `STATUS.md` change
   forces, the guard captures — and commits and pushes (Tasks 5 and 6).

**The user's condition on Ruling 1 of the leak-list sitting, verbatim, binds this whole batch:** *"B
under the condition we are NOT spending time on apparatus that has NO bearing on ultimate objective,."*
So: **no per-entry review of the entries the edit returns to the pack, no further surface on it, and
nothing done here that the tasks below do not name.**

---

## 1. Bars

**B1 — TWO TOOL SOURCES AND NO OTHER ARE EDITED.** `tools/audit/gen_derivation_boot_pack.py`, at
exactly the five replacements of Task 2 and nowhere else; and `tools/audit/gen_status_batch_bound.py`,
at its authored aiming inputs, their comments and one appended row of `PREVIOUS_AIMINGS` (Task 5(b)),
and no function. **No other tool source is touched** — in particular not
`tools/audit/gen_withheld_family_reading.py`, not `tools/audit/gen_evidence_pin_membership.py`, not
`tools/audit/gen_guard_classification.py`. If a task seems to need another tool edited, **STOP and
report it; do not resolve it.**

**B2 — NO EXTRACT IS EDITED.** Nothing under `reading_pass/` changes.

**B3 — THE THREE FROZEN SUBJECTS ARE NOT RE-RENDERED TO DISK.** Nothing under
`tools/audit/derivation_boot_pack/harmony-boundary/`, `…/scoring-model/` or `…/l0-l1/` is written,
deleted, renamed or moved.

**B4 — no `src/` file, no build, no test, no golden, no score corpus, nothing under `tools/corpus/`,
`tools/robust_stop/` or `tools/dcml/`, no measurement of the analysis, no paper.** No score or analysis
file is copied, moved or edited: the seven exemplars the brief names stay where they are.

**B5 — NO OPEN-ITEMS ROW is created, flipped or discarded. NO DECISIONS-REGISTER IDENTITY IS
ALLOCATED** (register rule (c) is suspended at `cowork_register_rule_c_suspension_2026_08_28.md`).

**B6 — NO FIGURE IS TRANSCRIBED FROM THIS DISPATCH INTO ANY ARTIFACT (D-431).** The sizes and hashes
this file states are start-state bars and expected values.

**B7 — NO GOVERNING DOCUMENT IS AMENDED EXCEPT `STATUS.md` at Task 5(a).** Not `CLAUDE.md`, not
`FRAMEWORK.md`, not `ARCHITECTURE.md`, not `OPEN_ITEMS.md`, not any ruling record, **and not
`cowork_derived_specification_l0_l1_2026_09_03.md`, which is READ and never written.** The draft brief
`cowork_blind_session_brief_l2.md` is committed as it stands and **not edited.**

**B8 — the live consumer at `tools/audit/gen_withheld_family_reading.py` lines 146–147 is NOT
repaired; `tools/audit/gen_guard_classification.py`'s STOP is CARRIED, NOT CHASED**: report it whole
and carry on.

**B9 — `tools/audit/claude_md_finer_archive.json` is held back**: not staged, not reverted, not
investigated.

**THE FOOTPRINT ASSUMPTION.** This batch **modifies** `tools/audit/gen_derivation_boot_pack.py`,
`tools/audit/derivation_boot_pack.json`, files under `tools/audit/derivation_boot_pack/l2/`,
`STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`,
`tools/audit/status_batch_bound.json`, and — only where the tool that owns each writes it —
`tools/audit/evidence_pin_membership.json`, `tools/audit/l0_l1_outgoing_population.json`,
`tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json` and the guard set's own
artifacts. It **creates** `tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md`
and your report. Anything else the enumeration shows as modified by this batch is outside the
assumption: report it and **STOP before the commit**.

---

## 2. Task 0 — the start state, and the uncommitted records committed

**0(a) — pin this dispatch:**

```
git hash-object -w records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md
```

Record the hash and `git cat-file -s <hash>`; take every later re-read of this dispatch from that blob.

**0(b) — the refs, expected to AGREE.** Read `.git/refs/heads/master` and
`.git/refs/remotes/origin/master` **with the file tools** (D-253; never `git rev-parse`). **Both must read
`84ab3a5c404bf9953a568df7c0c57022dba06f8f`** *(read so at both files by the writing side at release)*.
Anything else: **STOP**, and report both values as found.

**0(c) — the working tree.** `python tools/audit/changed_paths.py`; report it whole. **Nothing may be
staged**; if anything is, report exactly what and **STOP**. Then check the last bytes of each TEXT file
0(d) commits: **a trailing NUL byte, or a final line that breaks off mid-word, is a STOP** — name the file
and stop; do not repair it.

**0(d) — ONE COMMIT: the interim carriers.** By explicit path, never a directory pathspec, exactly
these; take each size by `git hash-object -w --no-filters <path>` then `git cat-file -s <identity>`, and
**a size different from the one given is a STOP** (the writing side touches none of them while this
batch runs):

1. **This dispatch**, at the blob 0(a) pinned.
2. `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md` — **6,212** *(bridge
   listing)*.
3. `records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md` — **6,716** *(bridge staging
   result after its landing)*.
4. `cowork_blind_session_brief_l2.md` — **35,582** *(bridge staging result after its second landing)*.
5. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_two.md` — **6,552** and
   `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_three.md` — **6,627** *(bridge
   listing)*.
6. `records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md` — **71,202** *(bridge staging
   result)* — the report whose §12.7 was appended after the previous batch's commit (relayed from entry
   253 §1). Commit it only if 0(c) reports it modified.
7. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_one.md` — **6,001** *(bridge
   listing)* — **only if 0(c) reports it untracked or modified**; the writing side runs no git and does
   not know whether it is committed.
8. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_four.md` — **only if it exists.**
   No size is stated (restraint paragraph above): report the size you find. If it does not exist, say so
   and commit the rest. **Do not wait for it.**

**0(c)'s enumeration establishes the actual set; this list is a guide to it.** A path the enumeration
reports that is not named here is held back and reported; a path named here that the enumeration does not
report is reported and not committed. Prove the staged set before committing. Do not push yet.

**0(e) — THE OPENING GUARD CAPTURE, taken AFTER the commit.** Run the guard set once; save the capture
**outside** the repository working tree; name the file in your report; record every guard's verdict.
`tools/audit/gen_guard_classification.py` is expected to STOP (B8).

---

## 3. Task 1 — the pack re-derives at the untouched tree

**(a)** `python tools/audit/gen_derivation_boot_pack.py --check`. **Record the exit code and the whole
output verbatim.** Expected: `the derivation boot pack re-derives`, three `FROZEN — N file(s) at their
recorded blobs` lines, exit 0. **Anything else is INHERITED: report it and STOP.**

**(b)** Record `git hash-object tools/audit/gen_derivation_boot_pack.py` and
`git hash-object tools/audit/derivation_boot_pack.json`. The second is Task 3(c)'s before-side.

---

## 4. Task 2 — Ruling 1 of the leak-list sitting, in the generator

Five replacements in `tools/audit/gen_derivation_boot_pack.py`. **Each OLD text must occur EXACTLY ONCE
in the file before it is replaced; if it does not, STOP** — do not search for a near match. Nothing else
in the file changes.

**2(a) — the constants and the function signature.** OLD:

```python
def cross_reference_additions(authored: set[str], docs: set[str],
                              design_intent: list[dict], backbone: dict) -> list[dict]:
    """Every DESIGN-INTENT entry that quotes or cross-references a withheld identity or document."""
```

NEW:

```python
# ── the fields the cross-reference rule searches ───────────────────────────────────────────────
# Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md`: for every
# subject that is NOT FROZEN the rule searches only the fields member (5) renders besides the
# identifier — `title`, `verbatim`, `plain`.  A FROZEN subject keeps the five-field search its pack
# was built under, so that its manifest record — the record of what its session was given — does not
# move; the same scoping as limb B's `extras_leaks` in `build_subject` (D-657).
XREF_FIELDS_FROZEN = ("title", "verbatim", "plain", "rationale", "status_source")
XREF_FIELDS = ("title", "verbatim", "plain")


def cross_reference_additions(authored: set[str], docs: set[str],
                              design_intent: list[dict], backbone: dict,
                              searched: tuple[str, ...]) -> list[dict]:
    """Every DESIGN-INTENT entry that quotes or cross-references a withheld identity or document,
    in the fields `searched`."""
```

**2(b)** OLD:

```python
        fields = haystack(e, bb, ("title", "verbatim", "plain", "rationale", "status_source"))
```

NEW:

```python
        fields = haystack(e, bb, searched)
```

**2(c)** OLD:

```python
    adds = cross_reference_additions(authored_ids, docs, design_intent, backbone)
```

NEW:

```python
    adds = cross_reference_additions(authored_ids, docs, design_intent, backbone,
                                     XREF_FIELDS_FROZEN if subject in FROZEN else XREF_FIELDS)
```

**2(d) — the manifest's description of the additions, made true per subject.** OLD:

```python
                "★_what_these_are": (
                    "Entries of the DESIGN-INTENT class whose own text QUOTES OR "
                    "CROSS-REFERENCES a withheld identity or names a withheld document, added to "
                    "the withheld set by the derivation rather than by hand. The fields searched "
                    "include `rationale` and `status_source`, which the pack does not render — a "
                    "cross-reference in either is still a route to the withheld material."),
```

NEW:

```python
                "★_what_these_are": (
                    "Entries of the DESIGN-INTENT class whose own text QUOTES OR "
                    "CROSS-REFERENCES a withheld identity or names a withheld document, added to "
                    "the withheld set by the derivation rather than by hand. The fields searched "
                    "include `rationale` and `status_source`, which the pack does not render — a "
                    "cross-reference in either is still a route to the withheld material.")
                if subject in FROZEN else (
                    "Entries of the DESIGN-INTENT class whose own text QUOTES OR "
                    "CROSS-REFERENCES a withheld identity or names a withheld document, added to "
                    "the withheld set by the derivation rather than by hand. The fields searched "
                    "are `title`, `verbatim` and `plain` — the fields member (5) renders besides "
                    "the identifier (Ruling 1 of "
                    "`cowork_rulings_2026_09_27_l2_leak_list_sitting.md`); `rationale` and "
                    "`status_source`, which the pack does not render, are not searched for this "
                    "subject."),
```

**2(e) — the ruling recorded among those the tool executes.** OLD:

```python
            "with a derived leak check over the extras beside it (limb B).",
        ],
```

NEW:

```python
            "with a derived leak check over the extras beside it (limb B).",
            "Ruling 1 of `cowork_rulings_2026_09_27_l2_leak_list_sitting.md` — the cross-reference "
            "rule searches only the fields member (5) renders, for every subject that is not "
            "FROZEN.",
        ],
```

**2(f)** Report the whole diff of the tool by explicit blob hashes (Task 1(b)'s hash against the new
one).

---

## 5. Task 3 — the render, and the proof that only what the ruling names moved

**3(a) — the render.** `python tools/audit/gen_derivation_boot_pack.py` (write mode, no `--subject`).
Record the output verbatim. **The `l2` line's verdict figures must read `IN 111 / OUT 133 / UNPLACED 0`**
— the edit does not touch verdicts. Any other figure: **STOP.**

**3(b)** `--check`: expected `the derivation boot pack re-derives`, the three `FROZEN` lines, exit 0.
Record verbatim.

**3(c) — THE PROOF (D-657).** A short Python script **outside the repository working tree** (not
committed) loads the manifest at Task 1(b)'s blob (via `git show <blob>`) and the manifest on disk, and
establishes and prints:

1. `subjects["harmony-boundary"]`, `subjects["scoring-model"]` and `subjects["l0-l1"]` are EQUAL as
   parsed JSON in the two documents;
2. the top-level keys are the same set, and every top-level value is equal **except two**:
   `the_rulings_it_executes`, which must be the old list followed by exactly the one string 2(e) adds;
   and `subjects`, which must differ **only** under the key `l2`;
3. **in the new document,
   `subjects["l2"]["THE_WITHHELD_FAMILY"]["derived_cross_reference_additions"]["additions"]` carries
   exactly the identities `D-406` and `D-656`** — the two the leak-list record found matching in a
   rendered field (§1 of that record, "two matched in `verbatim` — D-406 and D-656 — and stay withheld").

**Any other difference, or any other membership at 3(c)3, is a STOP before the commit**: report it
whole and name every path this batch has modified. Record the script's text and its output.

**3(d) — what moved in `l2`, reported and NOT reviewed** (the user's condition). Read out of the new
manifest, never transcribed from here: `subjects.l2.counted` before and after (both documents); and
`subjects.l2.LEAKS.entries` — the entries of members (5) and (6) the standing leak check struck. **No
per-entry review is performed on either.**

**3(e)** List `tools/audit/derivation_boot_pack/l2/` and report the file names and sizes. Confirm that no
file under the three frozen directories changed (`git status` is not used; the enumeration of Task 6
shows it).

---

## 6. Task 4 — the INPUT CONTRACT, cut, and the search whose hits go to the user

**4(a) — write the cut copy.** Create the directory `tools/audit/derivation_exemplars/l2/` if it does not
exist, and write `tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md` with
a Python script **outside the repository working tree** (not committed; its text goes into the report)
that does exactly this:

1. Read `cowork_derived_specification_l0_l1_2026_09_03.md` from the repository root **as bytes**, and
   decode it as UTF-8. Record its size in bytes and `git hash-object` of it.
2. Take its line ending: `"\r\n"` if the text contains `"\r\n"`, otherwise `"\n"`. Call it `EOL`.
3. Build the NEEDLE — **the one passage Ruling 1 of the brief sitting names**, the sentence at lines
   187–189 of the source — as these three pieces joined by `EOL`:
   - `" The ratified L2 architecture's use of it as a fitted prior (D-528,"`
   - `"  D-450) is in conflict with the charter's §8.6 and C-2, and that conflict is L2's to resolve at its"`
   - `"  own derivation and surface — flagged, not decided."`
4. **The NEEDLE must occur EXACTLY ONCE in the text. If not, STOP** — write nothing, and report the count.
5. Remove it, replacing it with the empty string. The line it sat on then reads, verbatim,
   `  it as evidence about the music."*` — **print that line of the result and confirm it.**
6. Prepend this HEAD, its lines joined by `EOL`, followed by one blank line:
   - `> **THE INPUT CONTRACT — the ratified specification of L0 and L1, cut for the L2 deriving session.**`
   - `> Below this block the ratified specification stands verbatim, except that passages stating the L2`
   - `> layer's own ratified or current design have been removed where they stood, with no mark. Do not`
   - `> try to reconstruct them, and do not treat a gap as a hint.`
7. Write the result as UTF-8 bytes. **Establish, and print:** (i) that the result, with the HEAD and its
   blank line removed from the front, equals the source with the NEEDLE removed, byte for byte; (ii) the
   result's size in bytes; (iii) its `git hash-object`.

**4(b) — THE SEARCH OVER THE CUT COPY. Its hits are REPORTED, and NOTHING more is cut in this batch.** A
second script **outside the working tree** reads the new manifest and the cut copy, and prints, for every
line of the cut copy (numbered from 1 in the cut copy), every hit of:

1. **every withheld identity of `l2`**: every `id` in
   `subjects.l2.THE_WITHHELD_FAMILY.identities` and every `id` in
   `subjects.l2.THE_WITHHELD_FAMILY.derived_cross_reference_additions.additions`, each matched as a whole
   identity (regular expression `re.escape(id) + r"(?!\d)"`);
2. **every withheld document of `l2`**: every key of `subjects.l2.THE_WITHHELD_FAMILY.documents`, as a
   plain substring;
3. the string `ARCHITECTURE.md`, and every match of `\b(?:docs|src)/[A-Za-z0-9_./+-]+` — the tool's own
   `PATH_LIKE`;
4. the token `L2` (regular expression `\bL2\b`).

**Print each hit as: line number, which of 1 to 4 matched, what matched, and the line verbatim.** Then
print the count per kind. **This is the cut list's raw material and it goes to the user through the
writing side.** Do not remove, edit or judge any hit. *(Why it is not cut here: a bare identifier standing
without its content is not a leak — Ruling 2 of the leak-list sitting's own ground — and telling the two
apart is a reading, not a search.)*

**4(c)** Confirm in the report that `cowork_derived_specification_l0_l1_2026_09_03.md` is byte-identical
to Task 4(a)1's hash after both scripts have run (B7).

---

## 7. Task 5 — the close: `STATUS.md`, the forward bound, the regenerations, the closing capture

**In this order and no other.**

**5(a) — the `STATUS.md` entry.** One new dated entry at the head of the dated entries, in the OI-222
pointer convention the file uses: a POINTER whose whole is your report, restating **no figure** (D-431).
It says what this batch did — the Cowork side's records and the draft L2 brief committed; Ruling 1 of the
2026-09-27 leak-list sitting carried into the boot-pack generator for every subject not frozen; the L2
pack re-rendered, the three frozen subjects proved unmoved; the input contract written from the ratified
L0/L1 specification with one named passage cut, under Ruling 1 of the 2026-09-27 brief sitting; the
search over it run — and what it did not do: **no session booted, the brief NOT released, the search's
hits NOT acted on and sent to the user, no score or analysis file moved**, no open-items row, no `D-NNN`.
**No existing sentence of `STATUS.md` is rewritten or removed.** This is the last write to `STATUS.md` in
this batch.

**5(b) — the forward bound.** Re-aim `tools/audit/gen_status_batch_bound.py` so that the batch it
identifies is the PREVIOUS one — the batch of
`records/cc/instructions/cc_instruction_l2_pack_build_second_half_2026_09_27.md`, whose entry heads
`STATUS.md`'s dated entries at the writing side's read. **That batch's CLOSE,
`cc_instruction_l2_pack_build_close_2026_09_27.md`, wrote no `STATUS.md` entry of its own** — it corrected
the second-half entry in place at its R1 — so it selects nothing and is not named; the same shape the
current aiming's comment records for the consolidation batch's close. **The aiming, at the tool's
authored inputs (read at the tool by the writing side at release):**

- `BASE_COMMIT` = the hash of Task 0's commit. Task 0 commits no `STATUS.md`, so that commit's
  `STATUS.md` object is the one both refs carried at 0(b), which carries the second-half entry at the
  head of the dated entries. If the tool's first STOP fires (the batch cannot be identified at the base
  commit), report it whole and make no further change.
- `PREVIOUS_BATCH_DISPATCH` = `"cc_instruction_l2_pack_build_second_half_2026_09_27.md"`.
- `DISPATCH` = `"cc_instruction_l2_brief_landing_2026_09_27.md"`.
- `TASK` = `"Task 5"` — this dispatch orders this batch's own entry at 5(a) and this move at 5(b), both
  inside its Task 5, which §7's heading names in those words.
- `ACT_DATE` = the date the move actually runs.
- `MOVE_KIND` = `"ordinary"`. `RULINGS` unchanged.
- `PREVIOUS_AIMINGS`: APPEND one row, in the shape of the rows above it —
  `{"executing_act": "cc_instruction_l2_brief_landing_2026_09_27.md, Task 5", "base_commit": <the
  BASE_COMMIT you set>, "the_then_previous_batch": "cc_instruction_l2_pack_build_second_half_2026_09_27.md",
  "the_kind_of_move": "ordinary"}`. The aiming being replaced is ALREADY that list's last row, so nothing
  else is appended and no row is edited.
- Each field's comment is re-stated the way every previous re-aiming re-stated it — the former value
  named, not deleted (#12).

Run `--apply`, then `--check`. **The declared prefix adjustment is expected to fire**, the second-half
entry carrying the `Last updated: ` prefix at the base commit; that is why 5(a) writes this batch's entry
first. **If `--apply` reports its already-in-the-archive STOP, report it whole and make no further
change.** Do not read a green `--check` as proof the bound is met (`OPEN_ITEMS.md` OI-379): report the
entries `--apply` actually moved, by name. **The two 2026-09-02 entries do NOT move and are not moved by
hand.** Report the tool's whole diff by explicit blob hashes.

**5(c) — the regenerations the tree now forces**, after 5(a) and 5(b):

```
python tools/audit/gen_evidence_pin_membership.py
python tools/audit/gen_evidence_pin_membership.py --check
python tools/audit/gen_l0_l1_outgoing_population.py
python tools/audit/gen_l0_l1_outgoing_population.py --check
python tools/audit/gen_session_start_read_size.py
python tools/audit/gen_defense_share.py
python tools/audit/gen_session_start_read_size.py --check
python tools/audit/gen_defense_share.py --check
```

Record all eight outputs and exit codes verbatim. *(Why each: the pin tool reads every ruling record
under `records/cowork/rulings/`, and two land at Task 0; `gen_l0_l1_outgoing_population.py` reads
`STATUS.md` among the governing documents; the two read-size tools move with `STATUS.md`.)* For each of
`evidence_pin_membership.json` and `l0_l1_outgoing_population.json`, compare with its blob at Task 0's
commit and **report every member or entry added, removed or changed, by name**; resolve none. **A `STOP:`
line or a traceback from any of the four tools is a STOP before the commit**; do not edit the tool.

**5(d) — THE CLOSING GUARD CAPTURE.** Compare it with 0(e)'s **verdict by verdict**.

> **THE CONDITION: no guard whose VERDICT was PASS at the opening capture may carry any other verdict at
> this capture.** FAIL → PASS is allowed and reported. No condition is written on printed output or on
> counts.

`tools/audit/gen_guard_classification.py` is expected to STOP (B8): report it whole and carry on. **A
guard that moved PASS → anything else is a STOP before the commit**: report the guard, its two verdicts
and its output, and name every path this batch has modified.

---

## 8. Task 6 — the commit and the push

**6(a) — THE BATCH COMMIT, by explicit path, never a directory pathspec.** The candidate set is exactly:

1. `tools/audit/gen_derivation_boot_pack.py`
2. `tools/audit/derivation_boot_pack.json`
3. every file under `tools/audit/derivation_boot_pack/l2/` **that the enumeration reports modified**,
   each by its own path
4. `tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md`
5. `STATUS.md`
6. `STATUS_ARCHIVE.md`
7. `tools/audit/gen_status_batch_bound.py`
8. `tools/audit/status_batch_bound.json`
9. `tools/audit/evidence_pin_membership.json`, `tools/audit/l0_l1_outgoing_population.json`,
   `tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json` — each only if its tool
   wrote it
10. `records/cc/reports/cc_report_l2_brief_landing_2026_09_27.md`
11. the guard set's own artifacts, **only those the enumeration reports as modified** — name each.

**Prove the staged set is EXACTLY this set before committing.** Nothing under the three frozen pack
directories may be staged (B3). **Held back, and confirmed absent from the staged set:**
`tools/audit/claude_md_finer_archive.json` (B9), and every other path the enumeration reports that no
commit in this batch names.

**6(b) — push** every branch that received commits. `origin` is the fork; `upstream` is not used;
**never `--force`**. Read `.git/refs/remotes/origin/master` with the file tools afterwards and confirm it
equals `master`. If the push fails for any reason, report it.

---

## 9. The report

`records/cc/reports/cc_report_l2_brief_landing_2026_09_27.md`, carrying in task order, verbatim, every
output this dispatch says to record:

1. Task 0 — the pin, both refs, the enumeration, the commit's staged set proved and its hash, the
   opening capture's path and every verdict.
2. Task 1's results.
3. Task 2's diff.
4. Task 3 — the render, the `--check`, 3(c)'s script and output, 3(d)'s counts and struck entries, 3(e)'s
   listing.
5. **Task 4 — 4(a)'s script and output; and 4(b)'s script and EVERY HIT, as its own section headed
   `THE CUT LIST'S RAW MATERIAL — for the user, not acted on`**, followed by 4(c).
6. Task 5 — the `STATUS.md` entry quoted whole; the forward bound's aiming, `--apply` and `--check` with
   the entries moved; 5(c)'s eight outputs and the members changed; the verdict-by-verdict comparison of
   the two captures, with the guard classification's result reported whatever it is.
7. The commits' hashes, the pushed branches, and `origin/master` after the push.
8. **What you did NOT do**, named rather than counted: no tool source but the two B1 names edited; no
   extract edited; nothing written under the three frozen pack directories; no governing document but
   `STATUS.md` amended; the source specification and the brief not edited; no score or analysis file
   moved; no session booted; the search's hits not acted on; no open-items row and no `D-NNN` touched.

**WHAT GOES TO THE USER, named rather than counted:** the search's hits over the input contract; what the
re-render struck at 3(d); the pinned-evidence and outgoing-population changes of 5(c); and any STOP.

**If any expected result does not appear, stop at that task and report it. Do not continue to the next
one, and do not resolve a bar that contradicts a task.**

---

*Provenance: Cowork, 2026-09-27 (Stockholm), the sitting booted on entry 253, both refs read at
`84ab3a5c40…` at their own files. Checked at the objects by that sitting before release: the five OLD
texts of Task 2 searched in the staged tool, each found once (lines 6034–6036, 6043, 6376, 6545–6550,
6673–6676 at the staging); `build_subject`'s `extras_leaks` scoping and `leak_strings`/`PATH_LIKE`
read there; the l2 manifest's additions whose `derived_because` names a rendered field — D-406 and D-656
only — at `tools/audit/derivation_boot_pack.json`; the source specification's lines 184–189 read at the
file; `gen_status_batch_bound.py`'s authored inputs and the last row of `PREVIOUS_AIMINGS`; `STATUS.md`'s
head entry; the pinned second-half dispatch's §1, §2, §11 to §14 and the close dispatch whole, whose shape
this file follows; and the Task 0 sizes at the bridge listing or staging result named beside each.*
