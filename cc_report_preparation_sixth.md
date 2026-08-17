# CC report — the preparation phase's SIXTH batch: the governing-surface split EXECUTED

> **Dispatch `cc_instruction_preparation_sixth.md`**, executing the four rulings of
> `cowork_rulings_2026_08_17_governing_surface_split.md` over the ratification surface
> `ratification_surfaces/cowork_governing_surface_split_2026_08_16.md` and its two pinned
> measurement artifacts. **No `src/` change, no golden, no test changed, moved or run, nothing
> under `tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis, no design, no
> repair, no derivation of any specification, no mining, no document archived or deleted AS A
> FILE, no decisions-register entry retired or revived.** One open-items row acted on:
> [[OI-370]]'s ordered flip.

---

## 1. The reading scope, the start state, and Task 0

### 1.a The session-start reads, under the ruled interim scope

`CLAUDE.md`, `STATUS.md` (header) and `BUILD_AND_TEST.md` were read under §5(B) of
`cowork_rulings_2026_08_16_preparation_return.md` — the blocks that state of themselves that they
are historical or superseded skipped in `CLAUDE.md`, the resolved rows skipped in
`OPEN_ITEMS.md`. Then, in full: the 2026-08-17 ruling record; the ratification surface; §5 of the
2026-08-16 record; `cc_report_preparation_fifth.md` §4 and §7; the `STATUS.md` archive-rule
precedent (`gen_status_archive_pass.py` and `STATUS_ARCHIVE.md`'s own shape); and
`tools/open_items_split_check.py`.

**★ THE SCOPE HAS EXPIRED.** §5(B) states that it expires without further ruling when the executed
split makes the boundary physical. Task 1's commit is that act, so the scope ended when that commit
landed. A session after this batch reads the five files as they now stand, and reaches the archive
companions only when it re-opens a decision.

### 1.b The start-state guard run — exactly what the dispatch declares

Run BEFORE the first edit:

```
55 guard(s) run, 1 failing, 4 not run, 16 historical record(s)
  [FAIL] tools/audit/gen_filing_convention_application.py --check
```

and `gen_guard_classification.py --check` printed **"the guard classification re-derives"** — no
stale report, **zero STOPs**. That is the dispatch's declared expected start state exactly, so no
STOP-and-report was owed on it.

### 1.c Assumption A1, checked first and entirely at content-addressed objects

`tools/audit/changed_paths.py` reported **exactly ONE tracked modification in the whole working
tree** — `cowork_handoff.md` — with `cowork_rulings_2026_08_17_governing_surface_split.md` and
`cc_instruction_preparation_sixth.md` untracked, and no second tracked difference anywhere.

The difference was taken **blob against blob by explicit hash**: the committed blob resolved from
the explicit commit `9fb1ba01bf` (`ca64770a19`), the working blob from `git hash-object`
(`06cffd9484`). It is **ONE contiguous changed passage**, 79 insertions and 1 deletion, carrying
both parts A1's own sentence names: the twenty-second session-close block inserted above the
twenty-first, and the twenty-first heading gaining this file's own entry-point demotion marker.
**A1 held at the shape its own sentence describes**, and no count of changed passages was asserted
in advance (the F25 lesson).

### 1.d Task 0

Commit **`1f84f5d621`**, parent `9fb1ba01bf`, pushed, **3 paths**, verified at the object.

**E0 — MET.** Exactly 3 paths at `git diff-tree`; one modification whose content matches A1's
stated shape, two additions; no staging override of any kind.

---

## 2. Task 1 — the split EXECUTED

Commit **`53e552296f`**, parent `1f84f5d621`, pushed, **39 paths**, verified at the object.

### 2.a What the act had to be, before it could be performed

The pinned span decomposition (`tools/audit/governing_surface_spans.json`, measured at
`c4f15a7b32`) records **line coordinates**, not span text. Four of the five files are
**byte-identical between that pin and the pre-act blob**, established at the objects
(`git diff --name-status c4f15a7b32 9fb1ba01bf` lists `STATUS.md` alone among the five). `STATUS.md`
is not: the fifth batch's close wrote four entries into it, shifting every line below 8 by +8 and
removing the `Last updated: ` prefix from what had been its newest entry.

So the mover does not trust coordinates against the live tree. It extracts each span's TEXT from the
**pinned blob**, requires that text to occur **exactly once** in the **pre-act blob**, and rebuilds
from there. Exactly ONE textual adjustment was needed and it is declared in the tool and in the
artifact: the `Last updated: ` prefix on that one entry. A span needing a second adjustment is a
STOP.

### 2.b ★ THE A4 SAFEGUARD FIRED FOR REAL, AND IT IS THIS BATCH'S LARGEST FINDING

Ruling 1 binds the executing dispatch to READ every span it archives rather than trusting its class.
The reading test applied is stated once, in the tool, and applied identically to every span:

> A span MOVES only when **(1)** it IS, read whole, a record of the kind its class names — a
> preserved former wording, a self-declared historical or superseded record, a record of declined
> alternatives or accepted costs, a resolved row, a completed batch's pointer entry — and **(2)** no
> part of it states a rule, a STOP, a live caveat or a prohibition that a working session acts on
> today. Anything else stays: the ruled doubt default.

A positional reference inside a moved span ("above", "below", "here") is **not** a ground for keeping
it — every companion entry carries a provenance line naming the parent file and the span's position
in the parent's pre-act blob, so the reference resolves.

**Under that test 17 of the 298 archive-class spans DO NOT read as their class says, and they carry
77,794 characters — more than the 6,540 characters `CLAUDE.md` actually gave up.** Each is left at
site, flagged doubt-defaulted-at-execution, and enumerated with its reason in
`tools/audit/governing_surface_split_application.json`. The four that matter most:

- **`CLAUDE.md` 490–649, 15,395 characters — the decisions register's rules (a) through (n).**
  Classed `preserved-former-wording` on two sentences that POINT AT former wordings preserved in the
  register's own provenance; the span contains none. It is nearly a tenth of the file and it is live
  governing rule text. **The single largest mis-class in the measurement.**
- **`CLAUDE.md` 228–260, 2,940 characters — principle #21's amendment record PLUS PRINCIPLES 22, 23
  AND 24.** The three standing principles carry no blank line above them, so the span rule swept them
  into the archive class. Archiving this span would have removed three principles from the standing
  list.
- **`OPEN_ITEMS.md` — seven INDEX ROWS**, [[OI-179]] among them, each placed in an archive class by a
  `former wording` or `is SUPERSEDED` phrase inside its own narrative. [[OI-179]] is OPEN and GATES
  (#19, the ground-truth ceiling); archiving it would have taken a gating establishment obligation
  out of the register.
- **`DECISIONS.md` — all three of its archive-class spans.** Each either POINTS AT archive material
  held in the register's data file or states the home criterion in force. **So the register's own
  mechanism was never exercised: assumption A3 is moot, not met** — there was no move for it to
  express, and no rendered file was hand-edited.

This is finding F29's residual risk realised, exactly in the direction the ruled doubt default exists
to prevent. **It is also why `CLAUDE.md` shrank by about 3% where the surface's class shares
predicted about 23%.**

### 2.c The moves, and the arithmetic to the character

Per file, against the **pre-act committed blob** at `1f84f5d621`:

| file | archive-class spans | moved | left at site by the reading | characters moved | arithmetic balances |
|---|---:|---:|---:|---:|---|
| `CLAUDE.md` | 16 | 9 | 7 | 6,540 | yes |
| `OPEN_ITEMS.md` | 140 | 133 | 7 | 326,334 | yes |
| `DECISIONS.md` | 3 | 0 | 3 | 0 | yes |
| `STATUS.md` | 131 | 131 | 0 | 457,949 | yes |
| `BUILD_AND_TEST.md` | 8 | 8 | 0 | 2,243 | yes |
| **total** | **298** | **281** | **17** | **793,066** | **yes** |

*(Read from `tools/audit/governing_surface_split_application.json`, which is where these values
live; nothing here is typed by hand.)*

**Moved + kept accounts for each pre-act blob TO THE CHARACTER**, and that equality is a STOP in the
tool rather than a reported figure. The measured size effect, at the git objects by explicit hash:

| file | pre-act bytes | post-act bytes | change |
|---|---:|---:|---|
| `CLAUDE.md` | 157,257 | 152,253 | −5,004 (−3.2%) |
| `OPEN_ITEMS.md` | 615,720 | 344,321 | −271,399 (−44.1%) |
| `DECISIONS.md` | 134,511 | 134,511 | 0 |
| `STATUS.md` | 516,584 | 55,198 | −461,386 (−89.3%) |
| `BUILD_AND_TEST.md` | 28,192 | 27,397 | −795 (−2.8%) |
| **total** | **1,452,264** | **713,680** | **−738,584 (−50.9%)** |

*(`OPEN_ITEMS.md`'s post-act figure includes [[OI-370]]'s flip, which is an addition; the split's own
character arithmetic is in the artifact.)*

### 2.d The pointers, and the one place their shape had to be decided

Every moved span leaves a **compact dated pointer** naming its own companion — §5(D)'s shape, Ruling
3's naming requirement. Two shapes, and the second was forced by the register's own mechanics:

- **Prose spans** (`CLAUDE.md`, `BUILD_AND_TEST.md`) keep a one-line italic pointer carrying the
  date, the companion by name, the span's size and class, and 60 characters of its opening so a
  reader can find it in a companion that keeps parent order. It is deliberately COMPACT — the first
  draft's pointer was longer than several of the `BUILD_AND_TEST.md` spans it replaced, which would
  have defeated the act; the ruling citation lives once, in each companion's header (#6).
- **Resolved rows** (`OPEN_ITEMS.md`) keep a compact pointer **ROW**. The item's ID, its name, its
  layer/gate cell and its detail link stay VERBATIM, and the status cell keeps its own opening — so
  the recorded resolution word is not replaced by a different one, the canonical status token is
  preserved, and **the register's bijection survives the act**: `tools/open_items_split_check.py`
  re-derives at index=375 / detail=375 / baseline=200, bijection holding. A bare deletion would have
  broken all three.
- **`STATUS.md` keeps ONE dated pointer for the whole cleared block**, not one per entry. This is the
  deviation from clause 2's per-span pointer shape that clause 3 orders, and it is stated here as the
  dispatch requires: the file's own banner already names the archive, and the per-entry
  reconciliation is re-derivable by `gen_governing_surface_split.py --check --pair STATUS.md`.

### 2.e ★ RULING 4's BOUND IS REACHED OVER THE MEASURED POPULATION AND NOT OVER THE FILE

Clause 3 orders every dated batch entry except the fifth batch's to move. What moved is the **131
spans the pinned artifact places** — 129 `pointer-entry-of-a-completed-batch` plus the two dated
entries the pointer test did not reach, which clause 2 names separately. **17 dated entries remain at
the site**, because the measurement's pointer recognizer matches the OI-222 remedy's own sentence and
those entries predate it, so they fell to `operative-rule-text`.

**They were not moved, and the ground is the dispatch's own bar:** *"no span moved that the pinned
artifact does not class into an archive class; every doubt-defaulted span stays."* So `STATUS.md`
does **not** end holding only the latest batch's entries — it holds the fifth batch's four, the
clearing pointer, seventeen older dated entries and its operative text. **This is declared rather
than glossed**, and it is one act away from being finished either way: a later measurement that
recognises a pre-OI-222 entry, or a user ruling naming the residue.

### 2.f The anchor remap, per citation

`gen_cluster_dispositions.py --verify` is the drift authority (F3's reading rule; `reaim_home_anchors.py`'s
exit code is never trusted). Immediately after the moves it reported **73 drifted anchors** with
**verbatim quotes found at their cited home 512/512** — so no operative span had moved, which is
clause 4's own STOP condition and it did not fire. `reaim_home_anchors.py` re-aimed all 73, the
register was regenerated through its own mechanism, and the authority now reports:

```
backbone decisions: 512
cross-references resolving: ALL
verbatim quotes found at their cited home: 512/512
cited line numbers correct: 506/506   (6 cited to a file with no line number, by design)
```

**End state `cited line numbers correct` at the full population**, as clause 4 requires. The tool's
own home-anchor STOP is checked against the anchors **as they stood at the pre-act commit**, read
from the git object — comparing post-remap anchors against pre-act span coordinates compares two
coordinate systems and reported a collision that never existed. That was caught by the STOP firing
on the first `--check` run and fixed at the tool.

### 2.g The parsers the pinned inventory names, all run at the edited tree

Clause 5 requires them to RUN, and rules a parser halting on the new shape a STOP.

- **`OPEN_ITEMS.md` (9).** `register_lint.py` PASS (375 unique row IDs); `index_status_lint.py --check`
  PASS (**every status cell opens with one canonical token and every row splits** — the direct proof
  that the new pointer rows are well-formed); `open_items_split_check.py` PASS;
  `gen_cluster_dispositions.py` PASS; `gen_discard_records.py --check` PASS;
  `gen_nongating_apparatus_rows.py --check` PASS; `shell_read_guard.py --establish --check` PASS;
  `gen_index_status_normalization.py` and `gen_oi367_opening_correction.py` — see below.
- **`DECISIONS.md` (2).** `gen_decisions_register.py --check` PASS.
- **`STATUS.md` (1).** `shell_read_guard.py` PASS.
- **`CLAUDE.md` (4).** `shell_read_guard.py` PASS; `claude_md_rule_triage.py --check` PASS.

**Three named parsers HALT, and every one of them halted before this batch.**
`gen_phase1_completion_inventory.py`, `gen_phase1_finish_line.py` and
`gen_item1_rehome_blocker.py` all raise inside `gen_outstanding_delegations.py`. All three are
**HISTORICAL members of the guard set**, and the guard set's own HISTORICAL table records the cause
in its own words: the fifth batch's ruled soft-discard retired every entry homed in
`cowork_structural_integrity_audit.md`, *"so that document stops being class C and the delegation
grading they all import REFUSES to run: they do not go stale, they STOP."* Nothing in this act adds
or removes a document from any such table.

**`gen_oi367_opening_correction.py` STOPs, and NOT on the new shape.** It halts at its
state-movement check naming fourteen rows, all of them resolved rows this act archived — but the
check it halts at is **downstream of** the two checks that would catch a malformed shape: *a row at
this tree does not split* and *rows with no canonical opening at this tree*. **Both passed.** The
state bit it compares is the leading token of the status cell, which the pointer rows preserve
verbatim, and [[OI-370]] — the one row this act genuinely moved between states — does not appear in
its list. It is a completed one-off pass whose baseline the register has legitimately moved past.

### 2.h [[OI-370]] — the one permitted row act, and its condition was TESTED

The row's own closing condition is that the mandatory read succeeds afterwards; the 2026-08-11 pass
declined to flip because it did not. **After this act the file tools read `STATUS.md` without
refusing** — the refusal on size, and before it the refusal on token count, are both gone. The flip
rests on that read and on nothing about the size of what moved (#19). The INDEX row is flipped with
provenance naming this act, the detail file gains a dated resolution note, and the superseded
2026-08-11 half of the status cell is preserved (#12).

---

## 3. The new-tool rule, discharged once

`tools/audit/gen_governing_surface_split.py` is this batch's only new tool, and it landed **with its
authored run-instruction and its authored classification verdict in the SAME commit that adds it**.
Clause 7 orders ONE CHECK PER PARENT/COMPANION PAIR: there are five pairs and one concern
(reconcile a parent against its companion), so the check has **one home** (#6) and is **invoked once
per pair** with `--check --pair <FILE>` — five entries in the guard set, which is the shape
`local_patches_check.py` and `corpus_arm_stamp.py` already use there. It takes `--check` and never
the bare invocation, for the ordinary reason: run with no flag it REWRITES its committed artifact.

What each invocation proves, both directions:

1. **LIVE, at HEAD** — every archived span is byte-present in its companion **exactly once**;
2. **LIVE, at HEAD** — every archived span is **absent from its parent** (moved, not copied);
3. **FROZEN, at the git objects by explicit hash** — moved + kept accounts for the parent's pre-act
   committed blob **to the character**.

The third is a fact about ONE MOMENT, so it is checked at that moment's own object rather than
against a file that legitimately grows — the epoch pattern `gen_status_archive_pass.py` already sets,
and the OI-344 shape avoided by construction. Its STOPs ride with it: an archive-class span with no
authored reading verdict, a verdict naming a span the decomposition does not carry, a moved span not
present exactly once in the pre-act blob, an arithmetic that does not balance, and a register home
anchor inside a moved span.

---

## 4. Every registered expectation, graded

- **E0 — MET.** §1.d.
- **E1 — MET, with one clause moot rather than met.** Moved + stayed accounts for each pre-act blob
  to the character (§2.c), proven by the clause-7 checks in both directions; every archived span
  byte-preserved; `gen_decisions_register.py --check`, `gen_cluster_dispositions.py --verify`,
  `tools/open_items_split_check.py` and all five new invocations pass; every moved artifact value
  enumerated and classed inside the bound (§5); **A4's left-at-site flags enumerated at 17** (§2.b);
  **no operative or doubt-defaulted span moved.** The moot clause is **A3**: `DECISIONS.md` had no
  move to express, so the register's own mechanism was not exercised at all.
- **E2 — see §6**, taken after the Task 2 commit exists, per the ordering rule.

---

## 5. Every artifact that moved, enumerated and classed inside the bound

Clause 5's bound: **movement ONLY in line coordinates, per-class counts, or populations whose
subject is a moved span or an archived resolved row; any other movement is a STOP-and-report.**
Every difference below was taken **blob against blob by explicit hash** against the pre-act commit
`1f84f5d621`.

| artifact | lines changed | what moved | class |
|---|---:|---|---|
| `tools/audit/decisions/backbone_decisions.json` | 160 | 146 `home` lines (the 73 re-aimed anchors) + 14 `delegation` lines | line coordinates |
| `DECISIONS.md` | 0 | **byte-unchanged** | — |
| `decisions/group_{A,C,D,F,G,I,K,L,Q,S,T,U}.md` | 6 each (group_A measured) | the rendered `**Home.**` line per re-aimed entry | line coordinates |
| `tools/audit/claude_md_rule_triage.json` | 144 | `home` lines only | line coordinates |
| `tools/audit/decisions/home_classification.json` | 18 | `delegation_at` lines only | line coordinates |
| `tools/audit/decisions/phase1p_delegation_bar.json` | 36 | `delegation_citation`, `delegation_citation_now` and quoted-line lists | line coordinates |
| `tools/audit/phase3_gate_partition.json` | 20 | quoted-anchor lines only | line coordinates |
| `tools/audit/rulings_sort_classification.json` | 232 | `home` and `the_home_it_names` lines only | line coordinates |
| `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md` | 48 | the same home lines, rendered | line coordinates |
| `tools/audit/nongating_apparatus_rows.json` | 23 | [[OI-370]]'s verdict moved live → retired; `open_rows` 242→241, `first_cut_candidates` 50→49, `gates` 25→24 | a population whose subject is the ordered row act |
| `tools/audit/discard_records.json` | 3 | [[OI-373]] moves into the retired-pointer category | a population whose subject is an archived resolved row |
| `ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` | 18 | see the finding below | a population whose subject is a moved span |
| `tools/audit/guard_state.json` | — | the runner's own captured output | its own subject |

**No movement outside the bound, and no verdict, class, gate or cut moved anywhere** — every
non-coordinate difference is one of the two population movements named above, each with its
subject stated.

**★ ONE POPULATION MOVEMENT IS A FINDING RATHER THAN BOOKKEEPING, AND IT IS REPORTED AS ONE.** The
artifact-inventory ruling surface moves from *"NAMED in the governing record — 51 of 82 files"* to
**50**, and from *"117 of those 571 ignored files are NAMED by the governing record"* to **109**.
Nine files stopped being named — **because their only naming was inside an archived resolved row.**
The governing record is what the retirement caller-check and the census-movement classification
scan, so **archiving spans can move a file from NAMED to NAMED-NOWHERE without anyone deciding
anything about that file.** It is inside clause 5's bound (the subject is a moved span) and it
changes no verdict by itself — *a crossing confers CANDIDACY only, and every ruled condition on a
candidacy stands* — but it is a standing consequence of pruning that the archiving wave must know
about before it runs. **§2.b's left-at-site population and this movement are the two things the
pruning wave taught that the measurement could not.**

**One artifact was RUN and then RESTORED rather than re-baselined.**
`tools/audit/index_status_normalization.json` is a one-off survey pinned to a past moment; clause 5
asks that the parser RUN, not that its record be rewritten, and regenerating it would fold this act
into a completed pass (the OI-301 hazard). It was run (`--survey`), its verdict recorded here —
**rows whose opening is NOT canonical: 0, malformed rows the parser drops: 0**, which is the direct
proof that the new pointer rows parse — and the artifact restored byte-identically from its pre-act
blob (`41949d8735`, hashed both ways).

---

## 6. The guard set at the edited tree, and the two reds that do not clear

Run at the edited tree BEFORE Task 1's commit, as clause 9 orders:

```
60 guard(s) run, 3 failing, 4 not run, 16 historical record(s)
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [FAIL] tools/audit/gen_retirement_caller_check.py --check
  [FAIL] tools/audit/decisions/gen_phase1w_legacy_verification.py --check
```

**Zero STOPs**, and `gen_guard_classification.py --check` printed **"the guard classification
re-derives"** after it was regenerated for the five new invocations — which is its own STOP working:
a tool in the run population with no authored verdict halts it, and the verdict landed in the same
commit as the tool. The population grew from 55 to 60 by exactly those five.

**★ ASSUMPTION A2 IS FALSIFIED, AND IN TWO SEPARATE WAYS, BOTH DECLARED RATHER THAN CLEARED.**

**(i) `gen_phase1w_legacy_verification.py --check` STOPs and is LEFT RED — this batch's
STOP-and-report.** *"recorded figure 80: quote not at OPEN_ITEMS.md:327. It is nowhere in the file
— the premise has changed."* The quote is [[OI-289]]'s row, which the ruled act archived; it is
byte-present in `OPEN_ITEMS_ARCHIVE.md`, so nothing is lost. **The remedy is one line in that tool —
point its `where` at the companion — and clause 5 forbids taking it:** *"a parser halting on the new
shape is a STOP, not an improvised tool edit."* It is a **ruling**, not a session's judgment: teach
the tool about the archive, class the check historical, or revisit the resolved-row fate. Nothing
was adjusted to make it green.

**(ii) `gen_retirement_caller_check.py` cannot be regenerated inside the act that moves it.** Its
live half re-scans the citation split at the governing record, which this act edited; its write mode
refuses without `--at <commit>`, and the commit its new reading belongs to is the one being created.
It is therefore regenerated **after** the close commit exists and lands in the ONE FURTHER commit —
the same ordering rule that caught F32 — and Task 1 and Task 2 both land with it red and declared.

**Every other red the edits turned was classed against its measured cause and then cleared by
regenerating the artifact under the bound** (§5), never by adjusting a check. The two that did not
clear are named here and in the close, and neither is rowed: the dispatch bars it.

---

## 7. Surfaced findings (D-641, #13, #19) — surfaced, not rowed

The dispatch bars creating an open-items row, so each is stated here and in the close.

- **F33 (new, the largest) — THE PINNED MEASUREMENT OVER-CLASSES, AND A4 IS WHAT STOOD BETWEEN THE
  RULING AND A BAD ACT.** 17 of 298 archive-class spans, carrying 77,794 characters, do not read as
  their class says — among them the decisions register's rules (a)–(n), three standing principles
  swept up by a span that overruns, seven OPEN INDEX rows including the gating [[OI-179]], and every
  one of `DECISIONS.md`'s three. **The measurement's error is entirely in the ARCHIVE direction**,
  which is the direction the ruled doubt default exists to prevent, and the surface's own stated
  residual risk is what this realises. §2.b.
- **F34 (new) — RULING 4's BOUND IS NOT REACHED FOR `STATUS.md`, AND THE CAUSE IS THE RECOGNIZER,
  NOT THE ACT.** The pointer recognizer matches the OI-222 remedy's own sentence, so 17 dated batch
  entries predating that remedy fell to `operative-rule-text` and stayed. The file is 89.3% smaller
  and readable, and it does **not** hold only the latest batch's entries. §2.e.
- **F35 (new) — ARCHIVING A SPAN REMOVES NAMINGS FROM THE GOVERNING RECORD, AND RETIREMENT
  CANDIDACY MOVES WITH THEM.** Nine files stopped being named because their only naming was inside
  an archived resolved row. §5.
- **F36 (new) — A STANDING CHECK LOCATES A RECORDED FIGURE BY FILE-AND-LINE IN `OPEN_ITEMS.md`, AND
  ARCHIVING THAT ROW BREAKS IT.** `gen_phase1w_legacy_verification.py --check` STOPs: *"recorded
  figure 80: quote not at OPEN_ITEMS.md:327. It is nowhere in the file — the premise has changed."*
  The quote is [[OI-289]]'s row, archived by this act; it is byte-present in
  `OPEN_ITEMS_ARCHIVE.md`. **The remedy is one line in that tool and clause 5 forbids taking it**
  (*"a parser halting on the new shape is a STOP, not an improvised tool edit"*), so the check is
  left red and reported. This is the batch's one STOP-and-report. §6.
- **F37 (new) — AN ARTIFACT THAT RECORDS THE COMMIT IT WAS TAKEN AT CANNOT BE REGENERATED INSIDE
  THE ACT THAT MOVES IT.** `gen_retirement_caller_check.py` refuses to write without `--at
  <commit>`, and the commit its new reading belongs to is the one being created. Handled by the
  E-ordering pattern the record already uses — regenerated after Task 1's commit exists and landed
  in the following commit — but the shape will recur for every such artifact. §6.
- **F38 (new, small) — THE PINNED READER INVENTORY UNDER-NAMES THE REACH, BY ITS OWN PUBLISHED
  BOUND.** Of the checks this act turned red, only two are among the tools the inventory names as
  parsers of an edited file; the rest read those files INDIRECTLY — through the register's data, or
  through a quote whose source is one of them. The inventory says of itself that it establishes no
  dependency and sees literal paths only, so this is that bound measured rather than a defect in it.
  **Assumption A2's clause treating an unnamed red as a STOP-and-report is therefore falsified as a
  practical bar**, and each red is instead classed by its measured cause in §5 and §6.
- **F39 (new, observation) — the OI-145 hardening battery FAILs its `calib` gate at HEAD**, four
  stage-5 calibration artifacts not reproducing byte-identically. **No file this act touched is a
  calibration artifact**, and the battery's two gates that could have been moved by this act —
  `register` (375 row IDs, no collision) and `a8_diff` (the robust stop, `overall_pass=True`,
  run-diffs 0/0 on all three presets) — both PASS. Recorded as observed, not diagnosed; the battery
  is not in the guard set.
- **F1–F32 (carried, unchanged)**, including **F3**, now eight times surfaced —
  `reaim_home_anchors.py --check` exits 0 while printing drifted anchors, and
  `gen_cluster_dispositions.py --verify` is the drift authority. **Still unfixed and unrowed: the
  dispatch bars both.** F25 did not repeat: no changed-passage count was asserted in advance. F32
  did not repeat: the three pinned tools all passed at every run of this batch.
- **The E3 ordering defect and the A1 premise error of the earlier batches** ride to the phase's
  retrospective as the dispatch orders.
- **No finding bearing on the analysis, its inputs, or a measurement tool the analysis depends on.**
  Every subject of this batch is the project's own record and the apparatus that reads it.

---

## 8. What this batch did NOT do

**No document was archived, moved or deleted AS A FILE** — this batch moved SPANS between files the
record keeps; the retirement/archiving wave for whole documents stays behind its own ruled gates,
untouched. **No sole-carrier member discarded; the 62 are not ruled; the residue surface and the
rulings-sort surface stand awaiting their sittings; the eight KIND-UNDERIVABLE callers and the
prose-citation question stay open.** No finer pruning pass, and **no span moved that the pinned
artifact does not class into an archive class**. No empirical findings ledger, no fact-gate
admission, no curated boot list. **No completion claim of any kind about the superseded phase-1
program.** No derivation of any specification, no design, no repair, no pilot act. **No `src/`
change, no golden, no test changed, moved or run, nothing under `tools/corpus/` or
`tools/robust_stop/`, no measurement of the analysis.** **No open-items row created, flipped or
discarded except [[OI-370]]'s ordered flip** — [[OI-372]] and [[OI-374]] stay exactly as found,
[[OI-179]] stays OPEN and GATES, and `reaim_home_anchors.py`'s F3 defect stays surfaced, unfixed and
unrowed.

*Provenance: CC, 2026-08-17, dispatch `cc_instruction_preparation_sixth.md`.*
