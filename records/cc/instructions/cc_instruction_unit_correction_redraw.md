# CC DISPATCH — CORRECT THE UNIT FORMS FOR STRATA 1 AND 2, REDRAW THOSE TWO, RE-SEAL

*Written by the Cowork writing side, 2026-08-27, against tip
`93c154562083516ea41cf6d01bcb6ea6cf4eb859`. Executes Ruling 1 of
`cowork_rulings_2026_08_27_redraw_findings_sitting.md`. This batch performs NO ratification, orders NO
register entry, MAKES NO ADMISSION, and **DOES NOT RUN THE PLACEMENT TEST** — the frame it would be
run against does not exist yet.*

---

## 0. What this batch is, and what it must NOT disturb

The previous batch (`cc_instruction_placement_sample_redraw.md`, report
`cc_report_placement_sample_redraw.md`) redrew and re-sealed the sample and **reported four readings
the rule did not decide**. The user has ruled on all four. **Two of them change a unit; the other two
are ratified as they stand.**

**★ ONLY STRATA 1 AND 2 ARE REDRAWN. STRATA 3, 4, 5, 7 AND 8 ARE CARRIED ACROSS UNCHANGED, AND
STRATUM 6 REMAINS NOT ENUMERABLE.** Redrawing anything else is forbidden by §7's fence.

**★ THE GOVERNING PROPERTY IS UNCHANGED: YOU ARE NOT PERMITTED TO CHOOSE WHAT GOES INTO THIS
SAMPLE.** Where the rule does not decide something, you STOP and report, or — where the previous batch
established that a reading is open — you declare it exactly as you did last time. **You never decide
it.**

**Unchanged and not reopened:** the ordering keys; the threshold `T = 25`; the take formula
`p_i = 1 + ( i * (N - 1) + 12 ) // 24`; the fence-awareness rule; the bullets-only reading of a list
item; the line-ending normalisation for stratum 8. **`T = 25` IS DECLARED, NOT DERIVED** — write it
that way wherever it appears.

---

## Task 0 — start state and landings

**(a)** Read `.git/refs/heads/master` **with the file tool**. It must read
`93c154562083516ea41cf6d01bcb6ea6cf4eb859`. **If it does not, STOP and report.** Name the side
measured wherever you state a hash.

**(b) Do NOT run `git status`** (D-253). Run:

```
python tools/audit/changed_paths.py
```

Record the population. **Commit none of the standing untracked population beyond what (c) names.** If
any path is tracked-modified other than `cowork_handoff.md`, **report it and do not commit it.**

**(c) Land, in one commit**, exactly these four paths:

- `cowork_handoff.md` — **TRACKED-MODIFIED.**
- `cowork_redraw_findings_surface_2026_08_27.md` — untracked
- `cowork_rulings_2026_08_27_redraw_findings_sitting.md` — untracked
- this dispatch

**★ THIS DISPATCH ASSERTS NO COUNT OF NEW HANDOFF ENTRIES.** Establish it yourself at the object, as
you did last batch: resolve `cowork_handoff.md` at the tip to its blob, compare the working tree
against it, and report (i) how many entries are new, (ii) whether the change is additions-only and
prepended with no earlier entry reworded, and (iii) the arithmetic that closes the two sides. **If the
change is anything other than additions-only prepended, STOP and report before committing.**

Then run:

```
python tools/audit/gen_evidence_pin_membership.py
```

---

## Task 1 — stratum 1, redrawn on the corrected unit

**Membership: UNCHANGED** — every repository-root file whose name begins `cowork_rulings_`,
`cowork_ruling_`, `cowork_owner_rulings_`, `cowork_pending_rulings_` or
`cowork_document_route_rulings_`, and ends `.md`. The ruled class of
`tools/audit/gen_artifact_inventory.py`.

**★ ENUMERATE THE MEMBERSHIP AFTER TASK 0(c)'s LANDING, AND REPORT THE COUNT. THIS DISPATCH DECLARES
NO EXPECTED NUMBER AND YOU MUST NOT TAKE ONE FROM IT.** The previous dispatch declared an expected 78,
the true figure was 79, and its stated ground for 78 was wrong at the objects — the writing side's
error, recorded at `cowork_rulings_2026_08_27_redraw_findings_sitting.md` §3. **Task 0(c) lands one
further ruling record, which will itself be a member.** Report what you count. Do not adjust it and do
not reconcile it against anything.

### 1.1 ★ THE CORRECTED UNIT. THE PREVIOUS FORM IS VOID.

**Do not use `^\d+\s*[.)]\s` on its own. It is void for this stratum** — it admitted every ordinary
numbered section heading.

A **numbered ruling** is a **fence-aware markdown heading** whose text, after the leading `#`
characters and after stripping leading `*`, `_`, `★` and whitespace, matches **EITHER**:

```
^(Ruling|RULING)\s+\d+
```

**OR**:

```
^\d+\s*[.)]\s+\**\s*(Ruling|RULING)\b
```

**Nothing else counts.** The second form exists because the records' house style is
`## 1. Ruling 1 — …`, which begins with a digit; the first exists because some records head a ruling
`## Ruling 3 — …` directly.

**A record matching zero contributes ZERO and is reported as contributing ZERO — never construed into
having one. Report the count of zero-returning records and name every one.**

### 1.2 Two figures from the writing side's own measurement, given as context and NOT as an expectation

The writing side opened **22 of the records** and counted with the file tools: **103 headings admitted
by the void form, of which 69 match the corrected form**; and **five of the 22 return zero** —
`cowork_rulings_2026_08_15_period_start.md`, `cowork_rulings_2026_08_15_session_length.md`,
`cowork_owner_rulings_2026_08_07.md`, `cowork_ruling_guard_family_2026_08_08.md`,
`cowork_document_route_rulings_2026_08_08.md`.

**That is a SAMPLE of 22 files, not a census of the class. It licenses no expected `N` and none is
declared. If your zero-returning list does not contain those five, report the difference** — it would
mean the two readings of the corrected form differ.

---

## Task 2 — stratum 2, redrawn on the corrected unit

**Membership: UNCHANGED and FROZEN — exactly the 35 paths the previous dispatch listed by name**
(`cc_instruction_placement_sample_redraw.md` §1.2), and **no signature of any kind**.

**★ DO NOT EXTEND THE LIST.** Decision surfaces written since the list was ruled — including
`cowork_redraw_findings_surface_2026_08_27.md`, which Task 0(c) lands — are **deliberately not
members.** The list is a ruled object and extending it without a ruling is the larger fault. **If any
listed path is not on disk, STOP and report it.**

*(Declared in the ruling and repeated here so it is not read as an oversight: stratum 1's membership
is a signature and therefore grows with this project's own output, while stratum 2's is a frozen list
and does not. The asymmetry is declared, not cured.)*

### 2.1 ★ THE CORRECTED UNIT. THE NUMBERED LIMB IS DROPPED ENTIRELY.

A **numbered decision** is a **fence-aware markdown heading** whose stripped text matches:

```
^(Decision|DECISION)\s+\d+
```

**and nothing else.**

**A listed file matching zero contributes ZERO and is reported as ZERO. Under this form that is
expected to be common, and it is a deliverable rather than a defect: report the count of
zero-returning files and name every one.**

### 2.2 The writing side's measurement, as context and NOT as an expectation

Across **7 of the 35 listed surfaces**: **48 headings admitted by the void form, of which 8 match the
corrected form.** All eight stand in two files —
`cowork_placement_sample_surface_2026_08_27.md` (3) and
`cowork_framework_phase_opening_surface_2026_08_26.md` (5). **Five of the seven carry no numbered
decision at all.**

**Seven files license no estimate over thirty-five and none is declared.**

### 2.3 ★ A STOP, AND ONE CASE THAT IS NOT A STOP

- **If stratum 2 enumerates to ZERO across all 35 files, that is NOT a stop.** Record `N = 0` and say
  so in terms. An empty stratum is a finding about this project's records and must be visible.
- **If `N ≤ 25`, the stratum is a CENSUS** under the standing threshold rule, and no uncertainty range
  is needed for it. That is the ordinary rule doing its work, not an anomaly — do not report it as
  one.

---

## Task 3 — the take, unchanged

For any stratum with `N > T = 25`, positions for `i = 0 … 24`:

```
p_i = 1 + ( i * (N - 1) + 12 ) // 24
```

**Integer division. No rounding function.**

**★ THE MANDATORY SELF-CHECK, per redrawn stratum with `N > 25`:** `p_0` must equal 1; `p_24` must
equal `N`; the 25 positions must be strictly increasing and distinct. **If any fails, STOP and report.
Do not adjust the formula.**

**The ordering is unchanged:** repository-relative path in byte order, then line number. If two items
coincide on both keys, STOP and report.

**Recorded so you do not report it as a defect you found:** item 1 and item `N` are always drawn. That
is the rule's declared cost.

---

## Task 4 — the third sealed file

**Path: `cowork_placement_sample_sealed_third_2026_08_27.md` at the repository root.** Chosen by the
writing side on the existing root convention; not ruled, and the user may rename it in one line.

**★ DO NOT DELETE, EDIT, MOVE OR REGENERATE EITHER EARLIER SEALED FILE.**
`cowork_placement_sample_sealed_2026_08_27.md` and
`cowork_placement_sample_sealed_redraw_2026_08_27.md` both stand as the record of what was drawn under
the earlier rules.

**★ THE BANNER MUST CARRY, IN THIS ORDER:**

1. **DO NOT READ IF YOU ARE AUTHORING THE FRAME** — and it must name **all three** sealed files as
   withheld, not only this one.
2. That this is the sealed placement sample, drawn at tip
   `93c154562083516ea41cf6d01bcb6ea6cf4eb859`, and closed.
3. That it **supersedes `cowork_placement_sample_sealed_redraw_2026_08_27.md`**, which superseded
   `cowork_placement_sample_sealed_2026_08_27.md`, and that both are **kept, not deleted**.
4. That `T = 25` is **declared, not derived**.
5. That **strata 1 and 2 are redrawn on corrected units and strata 3, 4, 5, 7 and 8 are carried across
   unchanged**, so the file is not a fresh draw of the whole sample.
6. That **stratum 6 is NOT ENUMERABLE and is not drawn**, and no stratum is STOPPED.

**Strata 1 and 2** carry: the membership (the signature, or the frozen 35-path list), the **corrected
unit written out in full**, the declared scoping *for this sample only*, `N`, census-or-take with the
positions and the self-check, the zero-returning file list on the stratum's face, and the drawn items
each with verbatim text and `path:line` provenance.

**★ ON STRATUM 1'S FACE, ADDITIONALLY: the circularity.** This stratum contains ruling records —
including the records of the sittings that defined it — so it may carry, as statements to be placed,
the rulings that defined the stratum. Ruled accepted; declared so a reader does not have to
reconstruct it.

**Strata 3, 4, 5, 7 and 8 are CARRIED ACROSS from
`cowork_placement_sample_sealed_redraw_2026_08_27.md`, verbatim** — the same `N`, the same positions,
the same items, the same declared notes, including stratum 3's weak-evidence note and stratum 5's list
of the five ordered items the bullets-only reading does not count.

**★ AND THEY ARE CONFIRMED RATHER THAN TRUSTED.** Re-enumerate each of the five and check that `N` and
the 25 drawn positions are identical to what the previous file carries. **If any differs, STOP and
report — do not redraw it.**

**On the faces of strata 3 and 5, additionally:** the bullets-only reading is now **RULED**, not an
artifact of a dispatch's STOP; ordered list items are excluded and they are plainly list items.

**On stratum 8's face, additionally:** line-ending normalisation is now **RULED**; without it the
stratum returns 610 events instead of 59.

**What this file does NOT carry:** any judgement about placeability, any grouping, any commentary on
the frame, any ranking. **It is a list.**

---

## Task 5 — the root-population hazard

At the previous batch's close the derived candidate population was **19** and the STOP list **five**.
This batch adds root-level `.md` files.

**Read the tool's candidate derivation and report, before writing the sealed file, which of this
batch's files you expect to enter.** Then measure with everything on disk and report the candidate
list and the STOP list.

**If the list widens: report it prominently, do NOT classify it, do NOT cure it, do NOT regenerate the
guard.** **★ AND DO NOT SHAPE ANY FILE TO STAY OUT OF THAT POPULATION.**

*(`--derive-only` is read-only and is explicitly permitted here; the previous batch had to declare it
as an unordered step.)*

---

## Task 6 — `STATUS.md`, the forward bound, the sweep, the report, the commit

**(a)** **Exactly one** POINTER entry in `STATUS.md` (OI-222 remedy; **D-431**: no count, no identity,
no rendered value), written **before** the forward-bound tool runs. The tool's own
`PREFIX_ADJUSTMENT` moves the `Last updated: ` prefix; that is its declared behaviour and needs no
separate declaration this time.

**(b)** Re-aim `tools/audit/gen_status_batch_bound.py` — the five aiming constants — and **append** the
outgoing aiming to `PREVIOUS_AIMINGS` (#12). Report the exact command line and the values set.
**`TASK` is a choice — declare which task number you used and why.**

**(c) The sweep:** `gen_guard_state.py`, then `gen_guard_classification.py`, in that order, **with no
flag passed to either**, to a fixpoint. The three standing DECISION reds are **not yours to cure**. A
staleness red caused by this batch's own writes is cured under the standing sweep rule. **For any
other red: if you cannot tell whether it is a decision red or a regeneration red, treat it as a
DECISION red and STOP.**

**(d)** Write `cc_report_unit_correction_redraw.md` at the root, then commit. State separately:

- the Task 0(c) establishment of the modified handoff, **including your own count of new entries and
  how you derived it**;
- **stratum 1: the membership count you enumerated**, its `N`, census-or-take, the 25 positions with
  `p_0` and `p_24`, and **the zero-returning records by name**;
- **stratum 2: its `N`**, census-or-take, the positions if a take, and **the zero-returning files by
  name**;
- **the five carried-across strata, each with the confirmation that `N` and the positions are
  identical** to the previous sealed file;
- whether the root population widened, with the measured candidate and STOP lists;
- every path written;
- **every departure and every instruction you could not obey.**

*(The report cannot carry its own closing commit hash. If you add it in a second commit whose whole
diff is that line, declare it — the precedent is this project's own and the last two batches both used
it.)*

---

## §7 THE FENCE

Writes permitted at **exactly** these paths:

- `cowork_placement_sample_sealed_third_2026_08_27.md` — new
- `cc_report_unit_correction_redraw.md` — new
- `STATUS.md` — one pointer entry
- `tools/audit/gen_status_batch_bound.py` — the five aiming constants and the appended row, carve-out
- the four Task 0(c) landings and `tools/audit/evidence_pin_membership.json`
- **any file a tool this dispatch orders you to run writes as its own output.** Name each in the
  report.

**Explicitly forbidden.** **No frame text authored, no part of the frame written, no statement placed,
no judgement about placeability recorded.** **No redraw of strata 3, 4, 5, 7 or 8** — they are carried
across and confirmed, never re-derived into a different draw. **No enumeration of stratum 6.** No edit,
deletion, move or regeneration of either earlier sealed file. **No extension of stratum 2's 35-path
list.** No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md` edit. **No register entry** — this batch
performs no ratification, so rule (c) is not engaged. *(That is the SEVENTH consecutive batch shaped to
route around the register blocker. Recorded here, not hidden; curing it is a decision act that has
never been put to the user.)* No item added to, removed from or reordered in the sample except by the
rules at Tasks 1, 2 and 3. **No existing ruling record, surface, dossier, register entry or inventory
row edited — you are reading these, not maintaining them.** No `src/` change, no test changed, moved or
run, no golden. Nothing under `tools/corpus/` or `tools/robust_stop/`. No open-items row created,
flipped or discarded. No finding number allocated. Neither blind output opened; neither brief, neither
pack, the generator, the manifest or any withheld family touched. No other `.py` source edited. Do not
cure the two discard-act checks; do not regenerate `[[OI-372]]`.

**★ THE STANDING CLAUSE.** **If obeying any instruction here would require a write outside this fence,
STOP and report the conflict. Do not choose a route, do not widen the fence, and do not substitute a
weaker form of the instruction to stay inside it.** Stopping and reporting is the correct outcome.
