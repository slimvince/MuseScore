# CC REPORT — the cascade-sweep batch

> **CC, 2026-08-25.** Executing `cc_instruction_cascade_sweep.md` (Cowork, the forty-fifth session's
> fifteenth sitting) on Ruling 1 and Ruling 2 of `cowork_rulings_2026_08_25_cascade_sitting.md`.
>
> **NOTHING STOPPED THE BATCH.** No DECISION red appeared beyond the standing one; the sweep
> converged; every registered expectation is MET. The findings routed under §5 are below and **none
> was fixed.**

---

## 1. DECLARED START STATE (Task 1, §4) — measured, nothing asserted

**The tip.** `git rev-parse HEAD` → **`9b1b0a02943fd047ab0c92ef817e8b81e52cf5a3`**. **Identical to
P1**, and re-measured a second time after a session interruption mid-batch, unchanged. **A2 holds.**

**`python tools/audit/changed_paths.py`** → **835 change records**: **one modified tracked path**,
`cowork_handoff.md`, and **834 untracked**. `cc_instruction_cascade_sweep.md` (record 87) and
`cowork_rulings_2026_08_25_cascade_sitting.md` (record 447) are among the untracked, as P6/P6a
expect. The remaining untracked population is P7's standing condition — **not committed, not
re-litigated.**

**The three files, measured at the WORKING TREE (sha256 of the worktree bytes; see §8 on sides).**

| path | worktree bytes | worktree sha256 |
|---|---|---|
| `cowork_rulings_2026_08_25_cascade_sitting.md` | 10,488 | `595e37eed5907e0c3568fa1a3d3763039741f13e5975b933af85034a895d85a5` |
| `cowork_handoff.md` | 709,374 | `4c1e943264938414118d2a350e2b6f554a7d55524cb465ce4b5a2093d3c648e1` |
| `cc_instruction_cascade_sweep.md` | 18,113 | `f89aa2bdcf5bf5231ce3200d4ffdfd3ba47dfb9ddcc83cd4dcbc79d4684ac502` |

**Neither writing-side file was edited, reflowed or corrected.** Nothing in either is reported wrong.

**The failing set at the tip**, read at `9b1b0a02:tools/audit/guard_state.json` → `summary`:
**`{run 75, passing 73, failing 2, not_run 4, historical_records 16}`** — **P2 confirmed exactly.**
The two failures, quoted from the artifact's own captured output:

| tool | captured output | §0 class |
|---|---|---|
| `tools/audit/gen_filing_convention_application.py --check` | stderr: *"STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md, OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md. An unclassified candidate is a STOP, never a silent pass (D-661)."* | **DECISION — never touched** |
| `tools/audit/gen_session_start_read_size.py --check` | stdout: *"STALE vs the measurement: session_start_read_size.json does not re-derive"* | STALENESS |

**The three `216` sites — measured at the tool's source at the tip, and P3's line numbers all hold.**

| line | where | published into the artifact? |
|---|---|---|
| 34 | the module docstring | no |
| 140 | `FURTHER_SPANS`, the label for the `★_the_live_gating_answer` → `the_gating_rows` span | **yes** |
| 298 | the `★_the_further_spans_and_why_they_are_here` block | **yes** |

The file had **not** moved. **The published artifact carries the string at four lines** at the tip
(`9b1b0a02:tools/audit/session_start_read_size.json`, lines 8, 43, 78, 107).

**`gating_ids` at the tip.** Measured at `9b1b0a02:tools/audit/nongating_apparatus_rows.json` →
`★_the_live_gating_answer` → `gating_ids`: **length 217**, and `OI-376` **is** a member. **P4
confirmed.** Beside it: `population.rows_parsed` 376, `population.open_rows` 242,
`population.first_cut_candidates` 49, `gating_rows` 217, `non_gating_rows` 25.

**The highest identity, measured SEPARATELY on both surfaces.**

- **INDEX `OPEN_ITEMS.md`:** highest is **OI-376** (line 414). No `OI-38x`, `OI-39x`, `OI-4xx` or
  four-digit identity occurs anywhere in the file.
- **`open_items/`:** highest detail file is **`open_items/OI-376.md`**. Enumerated by glob over
  `OI-3*`, `OI-[4-9]*` and the low ranges; no file above 376 exists.

**The two agree.** No disagreement to report, so the "next above the higher of the two" clause did
not fire.

---

## 2. THE IDENTITY AND ITS DERIVATION (Task 2)

**N = 377.** Derivation: highest identity in the INDEX = 376; highest identity in `open_items/` =
376; the two agree; the next free identity is therefore **OI-377**. Measured on both surfaces before
anything was written, never asserted.

**`open_items/OI-377.md`** was created — narrative and provenance only, carrying the
STATUS-IS-AUTHORITATIVE-IN-THE-INDEX banner and **no status of its own**. It carries the defect with
each published site quoted verbatim, why it is a defect and not a nit, why no remedy is ordered in
the ruling's own words, the provenance, and an explicit **NO REMEDY, NO TASK LIST, NO PATCH** block.

### 2.1 The INDEX row, as written

```
| OI-377 | ★ **A generator restates by hand a figure its own run derives — the count of gating rows stands transcribed as `216` at three sites, two of them published into its artifact, against a derived `217` at this tree** | `tools/audit/gen_session_start_read_size.py` carries the string `216` at three sites; two of them are published into `tools/audit/session_start_read_size.json`, so a reader of that artifact is told a number the same artifact's own derivation contradicts — and that artifact's opening field states *"Every value is computed; none is transcribed (D-431)"*. It is the shape **#17f** and **D-431** forbid: a figure enters by citation to a generated artifact, never by transcription. Found 2026-08-25 by `cc_instruction_regeneration_and_citation.md` at ONE site and measured to THREE by Cowork at the objects (Correction 1 of `cowork_rulings_2026_08_25_cascade_sitting.md` §0). **Rowed and nothing else** — the transcription is **NOT** updated to `217`, because the standing mechanism freeze bars tool work that does not block the work and because a hand-count goes stale again at the next row; the right repair removes the transcription and lets the figure enter by citation, which is a DESIGN question with real alternatives and gets its own surface. The three sites, the verbatim quotation of each, and the provenance are in the detail file, and no figure or line number is restated here beyond the defect itself | D — instrument / measurement layer (a generator's own published text restating a figure the same run derives) | OPEN — rowed 2026-08-25 (CC, `cc_instruction_cascade_sweep.md` Task 2) on the user's **Ruling 2** of `cowork_rulings_2026_08_25_cascade_sitting.md` §3, under **Ruling 9** of `cowork_rulings_2026_08_21_successor_plan_sitting.md` and register rules (c) and (e); **rowed is all that is done to it** and no remedy is proposed. **No apparatus declaration and no gating verdict are carried here** — a verdict is derived from a cut and never hand-added ([[OI-319]], [[OI-336]], **D-438**, the decision that states the register's gating cut). No finding number is allocated: **Ruling 9 opens no findings series**. **NOT in doubt:** no behaviour, no measured value, no golden, no corpus of scores, nothing under `tools/robust_stop/` | [detail](open_items/OI-377.md) |
```

**Six cells on `" | "`**, the neighbouring rows' column structure copied exactly; the status cell
opens with the **bare canonical `OPEN` token**; the row is a **pointer**, with a
`[detail](open_items/OI-377.md)` link. **No apparatus claim, no non-gating declaration, no gating
verdict.** The decision cited for that treatment is **D-438**, checked at `DECISIONS.md:786` before
it was written — *"Open-items register rows whose subject is this project's own tracking and
documentation apparatus gate nothing — but an establishment obligation always gates"*. **The
transposition the last batch corrected was not reintroduced.**

Row placement: appended after `OI-376` at the tail of section F's table, which is where `OI-372`,
`OI-374` and `OI-376` also sit; the real classification is carried in the **layer/gate** cell, as
those rows do.

### 2.2 The lint

```
$ python tools/audit/index_status_lint.py
INDEX STATUS LINT: OPEN_ITEMS.md
INDEX STATUS LINT: PASS — every status cell opens with one canonical token, and every row splits.
exit:0
```

**PASS.** Re-run after a mid-batch session interruption, unchanged.

---

## 3. THE SWEEP (Task 3) — CONVERGED IN **TWO** ROUNDS

**The deliverable table. Every round, its failing set, its classification, what it regenerated, what
moved.**

### Round 1

`python tools/audit/gen_guard_state.py` → **`75 guard(s) run, 4 failing, 4 not run, 16 historical
record(s)`**

| # | failing tool | failure text, quoted from its own `--check` run | §0 class | action |
|---|---|---|---|---|
| 1 | `tools/audit/gen_nongating_apparatus_rows.py --check` | *"FAIL: nongating_apparatus_rows.json differs from what the generator now produces"* | **STALENESS** — §0's second phrase, verbatim | regenerated |
| 2 | `tools/audit/gen_filing_convention_application.py --check` | *"STOP: derived candidates with no authored verdict … An unclassified candidate is a STOP, never a silent pass (D-661)."* | **DECISION — the standing red ([[OI-372]])** | **NOT touched, not run in write mode, not investigated** |
| 3 | `tools/audit/gen_evidence_pin_membership.py --check` | *"STALE vs the derivation: evidence_pin_membership.json does not re-derive"* | **STALENESS** — §0's third phrase, verbatim | regenerated |
| 4 | `tools/audit/gen_session_start_read_size.py --check` | *"STALE vs the measurement: session_start_read_size.json does not re-derive"* | **STALENESS** — §0's first and third phrases | regenerated |

**Every classification was made by running the tool's own `--check` and reading its message — not
from the guard artifact and not from reasoning.** Three of the four are STALENESS by §0's literal
test; the fourth is the standing DECISION red and was left exactly as found. **A4 holds for round 1.**

**What was regenerated, and what moved.** Both sides **worktree**, measured with `Get-FileHash`
before and after each write (§8 — `nongating_apparatus_rows.json` is CRLF in the worktree; the other
two are LF; each pair below is worktree-to-worktree, so no ending difference is involved).

| tool | artifact | before (bytes / sha256) | after (bytes / sha256) |
|---|---|---|---|
| `gen_nongating_apparatus_rows.py` | `tools/audit/nongating_apparatus_rows.json` | 176,351 / `82e4c308678e1f15fcb3d26638f37fd6ada30c0bdcd073a3807c48dd77dd5090` | 176,694 / `45df3a8d0ec36eb16acacc4da9a7f212fede8780bab7d3dbffbf5f962103a321` |
| `gen_evidence_pin_membership.py` | `tools/audit/evidence_pin_membership.json` | 16,360 / `571c8cf1d4f80c08eb4738850e1906173c3ac87ca153197564e1c07ac1ff570a` | 16,410 / `7a2b19097a4ef84a7387144d32047594a53252469a3093a6164ccb04f9b107e2` |
| `gen_session_start_read_size.py` | `tools/audit/session_start_read_size.json` | 8,015 / `4716df332980556bdd741ba761b27a41133ca83524bbd26513205456f2d48b27` | 8,015 / `9d1c3384a0fcb0d717ec6a97a1f9db9834a31a7afe710418aad74edd1b765bfd` |

Their own stdout, recorded because it is the measurement:

- `gen_nongating_apparatus_rows.py` — *"open rows 243, first-cut candidates 49 / NON-GATING 25, GATES 24 / A3: confirmed ['OI-280'], refuted ['OI-274'], not in A3 but derived 24"*
- `gen_evidence_pin_membership.py` — *"generated ratification documents 7; ruling records read 64 / members 7 — pinned 5, UNRESOLVED 0 / tools carrying a pin constant 8; outside this class 3"*
- `gen_session_start_read_size.py` — *"total at the tree 290810"*, with the read's four spans and the two further spans; *"vs 1760d9a4a8: 367121 -> 290810 (-76311, -20.79%)"* and *"vs 594074e1e1: 296832 -> 290810 (-6022, -2.03%)"*

**They were regenerated in that order deliberately** — the non-gating apparatus rows first, because
it is the producer of the artifact the other two read.

**Ordering of the three was the only judgment exercised in the round; nothing else was regenerated,
and no tool outside the failing set was run in write mode.**

### Round 2

`python tools/audit/gen_guard_state.py` → **`75 guard(s) run, 1 failing, 4 not run, 16 historical
record(s)`**

| # | failing tool | §0 class | action |
|---|---|---|---|
| 1 | `tools/audit/gen_filing_convention_application.py --check` | **DECISION — the standing red ([[OI-372]])** | none |

**The failing set is the standing red alone. THE SWEEP CONVERGED.** Round 2 regenerated nothing, and
the no-progress rule was never reached. **A3 holds with three rounds of the five-round cap unused.**

### The blast radius, measured

**Opening ONE register row turned THREE derived artifacts red, and they all went red in the SAME
round.** The chain Cowork's §1 predicted — `gating_ids` → `nongating_apparatus_rows.json` →
`session_start_read_size.json` — is confirmed, **and it has a third member the lead did not name**:
`tools/audit/evidence_pin_membership.json`. Not one of the ten further generators P5 listed by name
went red.

**And the tree moved in two further places the classification never touched**, because two members
of the guard set write rather than check — see finding F2 in §6.

**Total: five artifacts moved by one register row.**

### Where OI-377 landed — QUOTED FROM THE REGENERATED ARTIFACT

`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`, **line
361**:

```
   "OI-377",
```

The array now runs lines 187–404 = **218 identities** (`gating_rows: 218`, line 183).

The same artifact states the ground, at `the_gating_rows`:

```json
   {
    "id": "OI-377",
    "gate_ground": "the ruled default - the row is outside the over-inclusive apparatus first cut, so the non-gating declaration does not reach it at all",
    "how_it_was_placed": "the ruled default, the row being outside the over-inclusive apparatus first cut"
   },
```

and lists it under `gating_rows_by_how_they_were_placed` →
`the_ruled_default_outside_the_apparatus_first_cut` (line 587).

**A5 is MET, and it is MET as a MEASUREMENT and not as a reading of the source.** `OI-377` is on the
**gating** side, placed by the **ruled default**, being outside the apparatus first cut — the same
placement `OI-376` received.

### Did any OTHER row's placement change? — NO

| quantity | tip `9b1b0a02` | after the sweep |
|---|---|---|
| `population.rows_parsed` | 376 | 377 |
| `population.open_rows` | 242 | **243** |
| `population.first_cut_candidates` | 49 | **49** |
| `★_the_live_gating_answer.gating_rows` | 217 | **218** |
| `★_the_live_gating_answer.non_gating_rows` | 25 | **25** |
| `totals.non_gating` / `totals.gates` | 25 / 24 | **25 / 24** |

**The 25 `totals.non_gating_ids` are identical member-for-member and in the same order** on both
sides: `OI-205, OI-219, OI-229, OI-233, OI-280, OI-281, OI-290, OI-296, OI-297, OI-299, OI-301,
OI-317, OI-327, OI-329, OI-338, OI-346, OI-347, OI-364, OI-46, OI-48, OI-49, OI-50, OI-58, OI-85,
OI-99`.

Gating and non-gating partition the open population, and the generator HALTs on a row it cannot
place. With the non-gating set unchanged member-for-member, the open population up by exactly one,
and gating up by exactly one, **`gating_new` = `gating_old` ∪ {`OI-377`} exactly.** **No other row
moved, so no STOP was triggered.**

---

## 4. THE TWO COMMITS

### Commit 1 (Task 4) — `428b44143db6e3eeb6f052ad2216cfd63bd01e9a`

Parent `9b1b0a02943fd047ab0c92ef817e8b81e52cf5a3`. **Nine paths, enumerated by
`python tools/audit/changed_paths.py --commit 428b4414…`:**

```
M   OPEN_ITEMS.md
M   cowork_handoff.md
A   cowork_rulings_2026_08_25_cascade_sitting.md
A   open_items/OI-377.md
M   open_items/register_check.json
M   tools/audit/evidence_pin_membership.json
M   tools/audit/guard_state.json
M   tools/audit/nongating_apparatus_rows.json
M   tools/audit/session_start_read_size.json
9 changed path record(s) [commit]
```

`git show --stat`: **9 files changed, 466 insertions(+), 36 deletions(-)**; `OPEN_ITEMS.md` **1 +, 0 −**.

**Message** (verbatim): *"land: the cascade sitting's ruling record and the handoff's sixty-second
entry; OI-377 opened on the hand-transcribed gating-row count in gen_session_start_read_size.py —
rowed at a MEASURED identity, with no finding number, no apparatus declaration, no gating verdict and
no remedy, and the 216 deliberately NOT updated to 217; and the cascade discharged by sweep to a
fixpoint in TWO rounds, regenerating only STALENESS reds — round 1 found four failing and regenerated
three (the non-gating apparatus rows, the evidence-pin membership, the session-start read size),
round 2 found the standing red alone. The standing DECISION red was never run in write mode and is
untouched. No tool source is edited. The end state is NOT asserted here: the guard set run lands
after."*

**The end state is not asserted in it.**

### Commit 2 (Task 5) — the final guard run

Lands `tools/audit/guard_state.json` as the final run wrote it, plus
`cc_instruction_cascade_sweep.md` and this report. Its expected contents are stated at §11 — **a
commit cannot assert its own end state**, and neither can a report that rides it, so §11 states what
commit 2 is expected to carry and claims no measurement of the commit that carries this sentence.

---

## 5. THE FINAL GUARD RUN (Task 5), in its ruled shape

Run at the tree commit 1 left:

**`{run 75, passing 74, failing 1, not_run 4, historical_records 16}`**

**failing_tools:** `tools/audit/gen_filing_convention_application.py --check` — **the standing red,
and it alone.** Expectation met; nothing was fixed.

The four **NOT RUN** are unchanged from the tip: `gen_ratification_surface_set.py`,
`reaim_ratification_surface_paths.py`, `decisions/gen_verbatim_subject_consistency.py`,
`gen_reserved_word_scanner.py`. The sixteen HISTORICAL records are unchanged.

**The artifact this run wrote differs from commit 1's copy by ONE LINE** — `git diff --numstat`
reports `1 1`. It is not a verdict, a count or a population: it is one character inside a captured
PASS message. **The cause is finding F3 in §6 and it is reported, not fixed.**

---

## 6. FINDINGS, routed under §5 — **NONE FIXED, NO FURTHER ROW OPENED**

### F1 — `open_items/OI-376.md` still carries the citation the INDEX row was corrected away from

**Apparatus finding. Reported; not acted on.** Commit `744ed4a708` corrected `OI-376`'s **INDEX** row
in place, `D-436` → `D-438`, with an inline correction note. **The detail file was not corrected with
it.** `open_items/OI-376.md` line 99 still reads:

> *"**No gating verdict.** Whether this row gates is derived from a cut and is never hand-added
> ([[OI-319]], [[OI-336]], **D-436**)."*

— the same sentence, in the same words, carrying the transposed decision. §8 forbids touching
`OI-376` and §5 forbids fixing what is found, so **nothing was done.** *Date: found 2026-08-25 by
this batch while reading `OI-376.md` as the model for the new detail file. Reason it is reported
rather than discarded: it is a live mis-citation in a register detail file, which is the class the
correcting batch judged worth correcting on the neighbouring surface one commit earlier.*

### F2 — the sweep's blast radius includes two artifacts the classification never reaches, because two guards run in WRITE mode

**Apparatus finding. Reported; not acted on, and no row opened.** Two members of the guard set do not
merely check — they **write**, so a guard-set run modifies the tree whether or not anything is red:

- **`tools/open_items_split_check.py`** is invoked by the runner with **no arguments**, which is its
  **living mode** — its own docstring: *"LIVING MODE (default; writes `open_items/register_check.json`)"*.
  It passed in both rounds and rewrote `open_items/register_check.json` anyway. Blob at the tip
  83,444 / `400956aa65f3e8453ee76b4547eb853ef0602f21b569adc32bda7cbbf383b084`; blob at commit 1
  83,671 / `b0277e31ff38b1e4e831bf31e2d4ea3471e8a093aafade7b33faafb2d69cc8c5` (both **blob** side).
  Its captured summary moved *"living mode: index=376 detail=376 baseline=200 post-baseline=176"* →
  *"living mode: index=377 detail=377 baseline=200 post-baseline=177"*.
- **`tools/audit/gen_guard_state.py`** writes its own artifact on every run by construction.

**Consequence, which is why it is worth reporting rather than discarding:** a session told to
*"regenerate every STALENESS red's tool, and nothing else"* will still find **two** further paths
changed at the end of a sweep, and neither is discoverable from the failing set. The measured blast
radius of opening one register row is therefore **five artifacts**, not the three that went red.
Both were committed under Task 4's *"every artifact the sweep regenerated"* clause. *Date: measured
2026-08-25 by this batch at `changed_paths.py` after each round. No remedy proposed.*

### F3 — a live reproduction of the already-open [[OI-374]]: the same unedited guard's captured text changed with the SHELL

**Apparatus finding. Reported; not fixed. NO NEW ROW — [[OI-374]] already carries this exact
subject.** The one-line difference between commit 1's `guard_state.json` and the final run's is:

```
-        "OVERALL PASS � bijection holds, no detail file carries a status of its own, …"
+        "OVERALL PASS — bijection holds, no detail file carries a status of its own, …"
```

`tools/open_items_split_check.py` was **not edited between the two runs**. It is one of the four
tools `OI-374` names as not routing its printing through `tools/audit/output_encoding.py`, so its
captured output follows the environment. The sweep's two rounds were run from **Git Bash**; the final
run was run from **PowerShell** (see F4), and the same em dash arrives as a replacement character
under the one and as an em dash under the other.

**`OI-374`'s row records precisely this tool and precisely this character as its founding
observation.** What this batch adds is that the variable is not only the interpreter's output
encoding but **the launching shell**, and that it moves the committed bytes of a guard artifact
between two commits of the same batch. **No verdict moved** — both runs report `OVERALL PASS`, both
guard runs report the same summary, and encoding touches captured text and never an exit code.
*Date: measured 2026-08-25 by this batch at `git diff --numstat` and `git diff` between commit 1 and
the working tree. Nothing was changed; the row that owns it stands as found.*

### F4 — the Bash execution surface failed mid-batch, and that is why the final run went through PowerShell

**Reported so that F3's one-character difference is not read as a repository event.** Between the
sweep and the final guard run, `python tools/audit/gen_guard_state.py` returned **exit code 4 with an
empty capture**, and a subsequent bare `echo` returned **exit code 107** — a failure of the execution
surface, not of any tool. The final guard run was therefore performed through PowerShell, and it
completed normally and wrote the artifact reported in §5. **The empty first attempt wrote nothing**
(the capture file was 0 bytes) and was superseded by the completed run. *Date: 2026-08-25. This is a
harness observation, not a repository finding, and nothing in the repository is asserted about it.*

### F5 — the transcription is invisible to the tool's own establishment check, and this is now MEASURED

**Carried into `OI-377`'s detail file as part of the defect, and recorded here as the measurement
that confirms it.** After the sweep, `tools/audit/gen_session_start_read_size.py --check` **PASSES**,
while `216` still stands at all three sites of the tool (lines 34, 140, 298, re-measured after the
sweep) and at **four** lines of the regenerated artifact. **A literal re-emits identically, so the
tool's own `--check` can never see it.** *Date: measured 2026-08-25 by this batch. No remedy
proposed; the repair is the DESIGN question Ruling 2 reserves.*

### Nothing was discarded

No finding met §5's third limb. No analysis finding arose — this batch ran no analysis.

---

## 7. THE MEASURED HANDOFF DIFFERENCE (A1) — **with the pattern stated**

**A1 asserts no count and none is inferred. Two patterns, two populations, both reported.**

| pattern | at `9b1b0a02` | at the working tree | difference |
|---|---|---|---|
| lines matching `^## ★★★★★ COWORK SESSION CLOSE` | **63** | **64** | **+1** |
| lines matching `^## ` (all level-2 headings) | **88** | **89** | **+1** |

Both patterns say **ONE entry this cycle**, and the populations differ by what the pattern matches,
not by fact — the second counts the standing-rule and reference sections as well as the entry blocks.

`git diff --numstat 9b1b0a02 -- cowork_handoff.md` reports **134 insertions, 1 deletion** — the new
block, plus the one line where the previously current entry gained its `(SUPERSEDED …)` suffix.

The new block's own heading names itself: *"COWORK SESSION CLOSE (SIXTY-SECOND ENTRY, 2026-08-25 …)"*.
**Whatever these numbers are, they are not a STOP, and none was raised.**

---

## 8. A NOTE ON SIDES (P8) — stated wherever a hash appears above

`.gitattributes` marks these paths `text: auto` and `core.autocrlf` is not set, so a worktree copy
and its blob can differ in line endings alone. **Measured this batch, per file:**

- **CRLF in the worktree** (worktree ≠ blob by endings): `tools/audit/nongating_apparatus_rows.json`
  — worktree 176,694 vs blob 174,083 at commit 1; worktree 176,351 vs blob 173,748 at the tip. **The
  difference is 2,611 and 2,603 bytes respectively, exactly the line counts, and is NOT a content
  difference.**
- **LF in the worktree** (worktree = blob byte-for-byte): `cowork_handoff.md`,
  `cowork_rulings_2026_08_25_cascade_sitting.md`, `OPEN_ITEMS.md`, `open_items/OI-377.md`,
  `open_items/register_check.json`, `tools/audit/evidence_pin_membership.json`,
  `tools/audit/session_start_read_size.json`, `tools/audit/guard_state.json` — each raised git's
  *"LF will be replaced by CRLF the next time Git touches it"* notice on `git add`, which is the
  statement that the worktree copy is LF.

**Every before/after pair in §3 is worktree-to-worktree. Every commit-to-commit comparison in §4 and
§9 is blob-to-blob. No comparison in this report crosses the two.**

---

## 9. REGISTERED EXPECTATIONS (§7) — each MET or NOT MET, with the measurement beside it

**E0 — the two writing-side files land byte-identical. ✅ MET.** Measured at the **committed blobs**
of commit 1 (`git cat-file blob … | sha256sum`), against the **worktree** measurement of Task 1.
Both files are LF in the worktree, so the two sides are the same bytes and the comparison is exact:

| path | Task 1 (worktree) | commit 1 (blob) | equal? |
|---|---|---|---|
| `cowork_rulings_2026_08_25_cascade_sitting.md` | 10,488 / `595e37ee…d85a5` | 10,488 / `595e37eed5907e0c3568fa1a3d3763039741f13e5975b933af85034a895d85a5` | **yes** |
| `cowork_handoff.md` | 709,374 / `4c1e9432…c3648e1` | 709,374 / `4c1e943264938414118d2a350e2b6f554a7d55524cb465ce4b5a2093d3c648e1` | **yes** |

**E1 — commit 1 contains exactly the paths named, and nothing else. ✅ MET.** The nine paths are
listed in §4: the record, the handoff, `OPEN_ITEMS.md`, `open_items/OI-377.md`, and **five** swept
artifacts — `tools/audit/nongating_apparatus_rows.json`, `tools/audit/evidence_pin_membership.json`,
`tools/audit/session_start_read_size.json`, `tools/audit/guard_state.json` and
`open_items/register_check.json`. The last two are swept artifacts by F2's mechanism — written by
guards the sweep ran — and are named there rather than passed over.

**E2 — `OPEN_ITEMS.md` differs from `9b1b0a02:OPEN_ITEMS.md` by exactly ONE added row. ✅ MET.**
`git diff --numstat 9b1b0a02 428b4414 -- OPEN_ITEMS.md` → **`1  0`**: one insertion, **zero
deletions**. The full diff is a single hunk `@@ -412,6 +412,7 @@` whose only `+` line is the
`OI-377` row, sitting after `OI-376` with `OI-374`, `OI-375`, `OI-376` and the following blank line
and `## G.` heading unchanged as context. **No row removed, no existing row's text changed, non-row
lines equal.** Row count `^\| OI-` : **376 → 377.**

**E3 — the sweep converged within five rounds, final failing set the standing red alone. ✅ MET.**
Converged in **two** rounds; round 2's failing set is `gen_filing_convention_application.py --check`
alone. The round table is §3.

**E4 — no tool source file was modified. ✅ MET.** No path under `tools/` ending `.py` appears in
either commit: commit 1's nine paths are four `.md`/`.json` documents and five `.json` artifacts;
commit 2's paths are one `.json` artifact and two `.md` files (§11). Re-measured directly:
`tools/audit/gen_session_start_read_size.py` still carries `216` at lines **34, 140, 298** after the
sweep — **unchanged, and deliberately not updated to `217`.**

**E5 — the batch lands exactly TWO commits, in order. ✅ MET.** Commit 1
`428b44143db6e3eeb6f052ad2216cfd63bd01e9a`, parent `9b1b0a02943fd047ab0c92ef817e8b81e52cf5a3`;
commit 2 its child, landing the final guard artifact, the instruction and this report. **The ordered
structure yielded exactly two; none was invented and none absorbed.**

---

## 10. WHAT THIS BATCH DID NOT DO

No `src/` change; no build; no test written, run, moved or changed; no golden refreshed; nothing
under `tools/corpus/` or `tools/robust_stop/`; no behaviour change and no design.

**No tool source was edited** — the `216` above all, unchanged at all three sites. **[[OI-372]] and
its tool were never touched and never regenerated**; the standing DECISION red was not run in write
mode, not investigated, and no verdict was authored for it. **`OI-376` was not re-opened, re-worded
or given a verdict** — F1 reports a defect in its detail file and leaves it. **Exactly one register
row was opened.** Neither derivation boot pack, the pack generator, the manifest, either withheld
family, either session brief and either blind derivation output was touched, and **no blind output
was read at all.** `CLAUDE.md`, `STATUS.md`, `ARCHITECTURE.md` were not touched; `DECISIONS.md` was
**read** only, at line 786 (`D-438`), 782 (`D-431`), 784 (`D-436`) and 623 (`D-307`). **No finding
number was allocated.** No remedy was proposed for anything rowed. No derivation session was opened,
booted or prepared. **The large pre-existing untracked population was not committed and not
re-litigated.**

**[[OI-179]] stays OPEN and GATES. [[OI-374]] stands as found. The three deferred apparatus items
stay deferred.**

**One deviation from a harness default, disclosed rather than left silent:** commit 1 carries **no
`Co-Authored-By` trailer**, matching every commit in this series; the generic instruction to append
one was set aside in favour of this repository's established commit form. Say the word and it can be
added to future commits.

---

## 11. COMMIT 2 — appended after it exists

Commit 2 hash and its path list are stated in the commit itself and are enumerable with
`python tools/audit/changed_paths.py --commit <hash>`. Expected contents:
`tools/audit/guard_state.json`, `cc_instruction_cascade_sweep.md`, `cc_report_cascade_sweep.md` —
three paths, none of them a `.py`. **This report does not assert commit 2's own end state.**
