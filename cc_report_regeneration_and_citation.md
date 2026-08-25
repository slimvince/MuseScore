# CC REPORT — the regeneration-and-citation batch

> **Written by Claude Code, 2026-08-25**, executing `cc_instruction_regeneration_and_citation.md`.
> **★ THE BATCH STOPPED AT TASK 5.** Tasks 1–4 completed as dispatched. The guard set reports
> **TWO** failing tools, not one: the standing red **and one this batch caused**, mechanically and
> by construction, through Task 3(a)'s own regeneration. **E3 is NOT MET. A4 is FALSIFIED.**
> Nothing was fixed, nothing was investigated beyond naming the cause, and the second commit lands
> the guard run's output, the instruction and this report exactly as the dispatch's §5/§10 direct.

---

## 1. DECLARED START STATE (Task 1 / §4) — measured, nothing asserted

### 1.1 The tip

| measured | value |
|---|---|
| `git rev-parse HEAD` | `64d640317fd652d1192350f0eafe4ef83abca680` |
| its parent (`git log -1 --format='%H %P'`) | `2dfe0ba485f438817f60385b4f6ea9fc0e6e4432` |

**P1 HOLDS. A2 (the tip has not moved) HOLDS.** Proceeded.

### 1.2 The sanctioned changed-path enumeration

`python tools/audit/changed_paths.py` — **834 changed path record(s) [worktree]**:

| status | count | detail |
|---|---|---|
| ` M` modified | 1 | `cowork_handoff.md` |
| `??` untracked | 833 | includes `cc_instruction_regeneration_and_citation.md` (line 267) and `cowork_rulings_2026_08_25_landing_return_sitting.md` (line 447) |

**P6 HOLDS** — the large untracked population stands (833 at this reading; the dispatch cites the
previous batch's ~831, and this is that population plus the two files P5/P5a name). **Not
re-litigated, not committed, not touched.**

**`git status` was never run.** The prohibition at the dispatch's head was observed throughout; the
repository's `PreToolUse` guard independently refused one `ls` aimed at a repository path during this
session, which is the same rule working.

### 1.3 Sizes and sha256 at the working tree, before any act of this batch

| path | bytes | sha256 |
|---|---|---|
| `cowork_rulings_2026_08_25_landing_return_sitting.md` | 9544 | `de7b6b27eead0e95e9efd921185139bc1cdcb41fdfe269ca3323e9b9f0f7f9d1` |
| `cowork_handoff.md` | 698370 | `8e383c6b93406f1efd83b61da7221d536eb54a1fff3f8d68f33dc0511fd8c463` |
| `cc_instruction_regeneration_and_citation.md` | 15190 | `1f473f893fa0f637e4955d012c9b780750f07d4b80b171c8b9bbff9a07fa5cdf` |
| `tools/audit/nongating_apparatus_rows.json` | 176008 | `3d6be24b459d6f3cc286044b432651fb5b90b6dcbbaa1ba3f9d40c26f3b685c8` |
| `tools/audit/evidence_pin_membership.json` | 16129 | `55f1fd741972026a5dd191d279e0dbbdcb9ed2b55c0c031d3b924763ef1c0097` |
| `OPEN_ITEMS.md` | 343346 | `34e5b801d15415cda7e30d48868440a5c259c684d49e5000883042bc4ad28afb` |

*(Measured by a hashing script held in the session scratchpad, OUTSIDE the repository — it returns a
size and a digest and cannot return file content, so it is a measurement tool and not a shell text
read. No repository file was added for it.)*

### 1.4 The `OI-376` row's cell-5 text where the citation stood

> *"…**No apparatus declaration and no gating verdict are carried here** — a verdict is derived from
> a cut and never hand-added (`[[OI-319]], [[OI-336]], **D-436**`) — and the ruling states in terms
> that the verdict *"is put to the user on its own surface"*…"*

### 1.5 P3 re-measured at `DECISIONS.md` (verbatim, this turn)

```
| D-436 | A mechanism is judged on three measured conditions — automatic, detection rate, false-positive rate — and a failing one is REPORTED, not automatically removed | LIVE | — | `cowork_audit_protocol.md` |
| D-438 | Open-items register rows whose subject is this project's own tracking and documentation apparatus gate nothing — but an establishment obligation always gates | LIVE | — | `CLAUDE.md` |
```

**P3 HOLDS.** D-438 is the decision the row means; D-436 is a transposition.

---

## 2. TASK 2 — the citation correction, and only that

### 2.1 Before / after of the `OI-376` row (E2's measurement)

Measured by diffing every `| OI-` row of the working tree against `2dfe0ba485:OPEN_ITEMS.md`
(and, separately, against `64d640317f:OPEN_ITEMS.md` — identical result).

- **rows old 376, new 376; rows only in old `[]`; rows only in new `[]`**
- **rows whose text CHANGED: `['OI-376']`** — and no other
- **non-row lines equal: `True`**

**BEFORE** (the changed fragment; the rest of the row is byte-identical):

> `— a verdict is derived from a cut and never hand-added ([[OI-319]], [[OI-336]], **D-436**) — and the ruling states in terms that the verdict *"is put to the user on its own surface"*.`

**AFTER:**

> `— a verdict is derived from a cut and never hand-added ([[OI-319]], [[OI-336]], **D-438** — *citation corrected 2026-08-25 (CC, `cc_instruction_regeneration_and_citation.md` Task 2): **D-438** is the decision that states the register's gating cut; **D-436** (mechanism judging) was a transposition in the row as first landed*) — and the ruling states in terms that the verdict *"is put to the user on its own surface"*.`

**THE BAR WAS HELD:** `[[OI-319]]` and `[[OI-336]]` stand untouched; no further citation was added;
the finding was not re-worded; no gating verdict and no apparatus declaration were added; the
identity, name, description and subject cells are byte-identical; **the status token is still the
bare canonical `OPEN`.**

### 2.2 The lint

`python tools/audit/index_status_lint.py` — **exit 0**:

```
INDEX STATUS LINT: OPEN_ITEMS.md
INDEX STATUS LINT: PASS — every status cell opens with one canonical token, and every row splits.
```

Re-run after the A3 experiment below and after the final state: **PASS again, exit 0.**

---

## 3. TASK 3 — the two regenerations

### 3.1 (a) `python tools/audit/gen_nongating_apparatus_rows.py` — write mode

Tool output, verbatim:

```
wrote C:\s\MS\tools\audit\nongating_apparatus_rows.json
  open rows 242, first-cut candidates 49
  NON-GATING 25, GATES 24
  A3: confirmed ['OI-280'], refuted ['OI-274'], not in A3 but derived 24
```

Artifact after the write: **176351 bytes, sha256
`82e4c308678e1f15fcb3d26638f37fd6ada30c0bdcd073a3807c48dd77dd5090`.**

#### What the artifact NOW SAYS about `OI-376` — quoted from the file

- **In `gating_ids`? — `True`.**
- **Its entry in `★_the_live_gating_answer` → `the_gating_rows`, quoted:**

```json
{
 "id": "OI-376",
 "gate_ground": "the ruled default - the row is outside the over-inclusive apparatus first cut, so the non-gating declaration does not reach it at all",
 "how_it_was_placed": "the ruled default, the row being outside the over-inclusive apparatus first cut"
}
```

- **In `gating_rows_by_how_they_were_placed` → `the_ruled_default_outside_the_apparatus_first_cut`** —
  present.
- **Among `items` (the first-cut candidates)? — absent (`[]`).** Among `superseded_verdicts`? —
  `False`. Among `retired_verdicts`? — `False`.
- **In the non-gating verdicts? — NO**; the 25 non-gating identities are unchanged (listed in 3.1's
  movement table below).

**★ THE WRITING SIDE'S EXPECTATION IS NOT REFUTED — it is what the artifact says.** The row is
outside the tool's first cut and takes the outside-the-cut ground on the gating side by the ruled
default. **This is reported as the artifact's measurement, not as a confirmation of the reading.**

#### Whether the counts moved — measured against `64d640317f:tools/audit/nongating_apparatus_rows.json`

| figure | at the tip | after the regeneration | movement |
|---|---|---|---|
| `population.rows_parsed` | 375 | 376 | **+1** |
| `population.open_rows` | 241 | 242 | **+1** |
| `population.first_cut_candidates` | 49 | 49 | 0 |
| `totals.non_gating` | 25 | 25 | 0 |
| `totals.gates` (inside the cut) | 24 | 24 | 0 |
| `★_the_live_gating_answer.gating_rows` | 216 | **217** | **+1** |
| `★_the_live_gating_answer.non_gating_rows` | 25 | 25 | 0 |
| `★_the_live_gating_answer.open_rows` | 241 | 242 | **+1** |

#### Whether any OTHER row's placement changed — **NO**

- `gating_ids` **added: `['OI-376']`**; **removed: `[]`**.
- The 25 **non-gating** identities are set-identical before and after.
- The 24 **GATES-inside-the-cut** identities are set-identical before and after.
- `the_authored_verdict_inside_the_apparatus_first_cut` list: unchanged.
- `the_ruled_default_outside_the_apparatus_first_cut` list: unchanged **except** the single insertion
  of `OI-376`.

**No STOP was owed under Task 3(a)'s "if one did, report it and STOP" clause.**

### 3.2 A3 — FALSIFIED BY EXPERIMENT, NOT BY REASONING

The dispatch asks whether the derived placement of `OI-376` differs from what a regeneration **before**
the correction would have produced. **It does not, and this was measured rather than argued.**

**The A/B, run at the tree:**

1. Regenerated with the row **corrected** → artifact sha256 `82e4c308678e…`.
2. Reverted the row to its exact pre-correction text (`OPEN_ITEMS.md` back to
   `34e5b801d154…`, its Task-1 hash, confirming the revert was exact) and regenerated →
   artifact sha256 **`82e4c308678e…` — byte-identical.**
3. Re-applied the correction (`OPEN_ITEMS.md` → `e3863e4591813249e2632268c0237596551b6136f47576eff8b2ed0346d6986b`,
   343584 bytes) and regenerated → artifact sha256 **`82e4c308678e…` — byte-identical again.**

**A3 HOLDS: the citation correction changes neither generator's derivation.** The mechanism is
visible at the tool's own source and agrees with the experiment: the first cut matches on the row's
**subject column** only (`cut = [r for r in open_rows if any(v.lower() in
r["subject_column"].lower() for v in FIRST_CUT_VOCAB)]`), and the **status column is read for its
leading canonical token and for nothing else** — `status_column` is parsed into the row dict and
then read by no verdict and carried into no artifact of this tool. The leading token stayed the bare
`OPEN`. `gen_evidence_pin_membership.py` does not parse the register's rows at all.

### 3.3 (b) `python tools/audit/gen_evidence_pin_membership.py` — write mode

Tool output, verbatim:

```
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 63
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
```

Artifact after the write: **16360 bytes, sha256
`571c8cf1d4f80c08eb4738850e1906173c3ac87ca153197564e1c07ac1ff570a`.**

#### How the record population moved — measured against `64d640317f:tools/audit/evidence_pin_membership.json`

| figure | at the tip | after | movement |
|---|---|---|---|
| `counts.ruling_records_read` | 59 | 63 | **+4** |
| `counts.generated_ratification_documents` | 7 | 7 | 0 |
| `counts.members` | 7 | 7 | 0 |
| `counts.members_pinned` | 5 | 5 | 0 |
| `counts.members_unresolved` | 0 | 0 | 0 |
| `counts.tools_carrying_a_pin_constant` | 8 | 8 | 0 |
| `counts.pinned_tools_outside_this_class` | 3 | 3 | 0 |

**APPEARED — four ruling records, not three:**

```
cowork_rulings_2026_08_25_determination_route_sitting.md
cowork_rulings_2026_08_25_forward_fact_sitting.md
cowork_rulings_2026_08_25_landing_return_sitting.md
cowork_rulings_2026_08_25_method_voiding_sitting.md
```

The three the dispatch names are there. **The fourth is
`cowork_rulings_2026_08_25_landing_return_sitting.md` itself** — it is on disk at this tree (P5) and
the generator reads the tree, so it enters the derivation in the same act that commits it. **This is
reported, not treated as an anomaly.**

**DISAPPEARED: `[]` — no previously-present record vanished. No STOP was owed.**

Every other field of the artifact compared equal; only `counts` and `ruling_records_read` differ.

### 3.4 (c) Both `--check` exit codes

| command | exit code | output |
|---|---|---|
| `python tools/audit/gen_nongating_apparatus_rows.py --check` | **0** | `PASS: nongating_apparatus_rows.json re-derives byte-identically (25 non-gating / 24 gates of 49 candidates over 242 open rows)` |
| `python tools/audit/gen_evidence_pin_membership.py --check` | **0** | `the evidence pin's class membership re-derives` (+ the census lines above) |

**Both now pass.**

### 3.5 A5 — MET

`python tools/audit/changed_paths.py` after both regenerations: **837 records — 4 modified
(`OPEN_ITEMS.md`, `cowork_handoff.md`, `tools/audit/evidence_pin_membership.json`,
`tools/audit/nongating_apparatus_rows.json`) and 833 untracked.** The untracked count is unmoved
from the start state, so **no generator wrote any further path**; the only tracked files changed are
the two named artifacts plus the two the batch was always going to carry.

---

## 4. TASK 4 — the first commit

**Hash: `744ed4a708d3a3cf1c6764ccf2bf6ab33fa5aa2b`.**

`python tools/audit/changed_paths.py --commit 744ed4a708d3a3cf1c6764ccf2bf6ab33fa5aa2b`:

```
M	OPEN_ITEMS.md
M	cowork_handoff.md
A	cowork_rulings_2026_08_25_landing_return_sitting.md
M	tools/audit/evidence_pin_membership.json
M	tools/audit/nongating_apparatus_rows.json
5 changed path record(s) [commit]
```

Message: *"land: the landing-return ruling record and the handoff's sixty-first entry; the OI-376
citation corrected in place D-436 -> D-438 with an inline correction note; and the two owed
regenerations discharged — the non-gating apparatus rows and the evidence-pin membership, both
re-deriving byte-identically on --check. The end state is NOT asserted here: the guard set run lands
after."*

**No generator wrote any further path (A5), so nothing beyond the five was staged or committed.**

---

## 5. TASK 5 — THE GUARD SET, AND THE STOP

`python tools/audit/gen_guard_state.py` (write mode), run at the tree the first commit left.

### 5.1 The summary in its ruled shape

```
{ run: 75,
  passing: 73,
  failing: 2,
  failing_tools: [ tools/audit/gen_filing_convention_application.py --check,
                   tools/audit/gen_session_start_read_size.py --check ],
  not_run: 4,
  historical_records: 16 }
```

The runner's own closing line: `75 guard(s) run, 2 failing, 4 not run, 16 historical record(s)`.

### 5.2 The two failures, quoted from `tools/audit/guard_state.json`

**(1) `tools/audit/gen_filing_convention_application.py --check` — THE STANDING RED, [[OI-372]].**
Exit code 1, stderr:

> `STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md, OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md. An unclassified candidate is a STOP, never a silent pass (D-661).`

**Not touched, not regenerated for, not investigated** — as the dispatch's P2 directs.

**(2) `tools/audit/gen_session_start_read_size.py --check` — ★ A SECOND RED, AND THIS BATCH CAUSED
IT.** Exit code 1, stdout:

> `STALE vs the measurement: session_start_read_size.json does not re-derive`

**★ THIS IS THE STOP. E3 IS NOT MET AND A4 IS FALSIFIED.** Per Task 5 — *"If any other tool fails,
REPORT IT AND STOP — do not fix it"* — **nothing was fixed. `session_start_read_size.json` was NOT
regenerated.**

### 5.3 The cause, established read-only at the objects — reported, NOT remedied

`gen_session_start_read_size.py` measures the ordinary session-start read in characters. Its
membership is three whole documents — `CLAUDE.md`, `STATUS.md`, `DECISIONS.md` — **plus the span
that register rule (a)'s own clause points at, parsed from the clause: `tools/audit/
nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`.**

**Task 3(a) regenerated exactly that artifact, and the regeneration added one identity to exactly
that key.** The tool's own `what_it_checks` says so in terms: *"It goes red when a governing surface
changes, which is the point: the session-start read moved and the record does not yet say so."*

Measured by calling the tool's own `measure()` at the tree **read-only, writing nothing**, and
comparing against the committed `tools/audit/session_start_read_size.json`:

| measured quantity | in the artifact | at the tree now | movement |
|---|---|---|---|
| `CLAUDE.md` characters | 155067 | 155067 | **0** |
| `STATUS.md` characters | 6195 | 6195 | **0** |
| `DECISIONS.md` characters | 126774 | 126774 | **0** |
| `… → ★_the_live_gating_answer → gating_ids` characters | 2748 | **2761** | **+13** |
| `total_characters` | 290784 | **290797** | **+13** |
| `… → ★_the_live_gating_answer → the_gating_rows` characters | 60734 | **61028** | **+294** |
| `the_section_that_carries_the_pointer` characters | 74858 | **75193** | **+335** |
| `characters_the_section_carries_beyond_the_answer` | 72110 | **72432** | **+322** |
| `the_pointer_rule_a_names` (artifact, keys, clause_characters 603) | — | identical | **0** |

**The three whole-document members did not move at all.** The single moved input is the artifact
span this batch regenerated, and the `+13` characters are the one added identity `"OI-376"` with its
punctuation and indentation.

**★ THIS IS THE SAME FAILURE SHAPE THE PREVIOUS BATCH MET AND THE HANDOFF DESCRIBES** — *"the same
artifact also publishes `gating_ids` over **every** open row, so **adding ANY open row moves it by
construction**"* — one consumer further downstream. **The artifact is out of date, not wrong**, on
exactly the ground P2 states for the two reds this batch discharged. **Whether it is regenerated,
and by whom, is not decided here and no remedy is proposed.**

### 5.4 A FINDING THAT REGENERATION ALONE WOULD NOT CLEAR — routed under §5, NO ROW OPENED

`gen_session_start_read_size.py` carries, in its **authored** `FURTHER_SPANS` prose, the string

> `"the 216 gating rows, each carrying its recorded ground — the GROUNDS a session opens when it challenges a verdict, and the third of the five figures Ruling 3 orders corrected"`

**That `216` is a hand-transcribed count of a figure the same run derives, and the derived value is
now `217`.** It appears in the freshly computed read-only measurement, so it is authored in the
tool's source and **a regeneration of the artifact would carry the stale number forward unchanged**.
This is the shape `CLAUDE.md` #17f / **D-431** forbid — a measured figure restated by hand.

**Routed per §5: an apparatus finding, REPORTED. No register row opened** (this batch creates none),
**no remedy proposed, nothing edited.** Finding date **2026-08-25**; reason it is reported rather
than discarded: it is a figure inside a live measurement tool's own published output, so a reader of
that artifact is told a number the same artifact contradicts.

### 5.5 What the guard run wrote

`python tools/audit/changed_paths.py` after the run: **833 records — 1 modified
(`tools/audit/guard_state.json`) and 832 untracked.** No other tracked path moved; the
`--establish`-mode guards in the set re-derived their artifacts identically.

---

## 6. A1 — THE HANDOFF DIFFERENCE, MEASURED (no count was carried in)

Measured against `64d640317f:cowork_handoff.md`:

| measurement | value |
|---|---|
| lines at the tip | 8265 |
| lines at the working tree | 8388 |
| lines added | **124** |
| lines removed | **1** |
| `## ★★★★★ COWORK SESSION CLOSE` heading lines at the tip | **62** |
| the same at the working tree | **63** |
| **new entries prepended** | **ONE** |

The one removed line is the sixtieth entry's heading, which reappears unchanged 124 lines lower —
i.e. the new **SIXTY-FIRST ENTRY** was prepended above it and nothing else in the file moved.

**A1's measured answer is ONE.** *(The dispatch states the writing side has had this assertion wrong
three times; on this cycle it asserted nothing and the measurement is one. Note for the record: the
heading count under the pattern used here is 62 → 63, which is not the same population the previous
batch reported as "44 → 48 entry headings" — a different matching pattern, stated so the two numbers
are not read as contradicting each other.)*

---

## 7. REGISTERED EXPECTATIONS — E0…E4

| # | expectation | verdict | the measurement beside it |
|---|---|---|---|
| **E0** | the two writing-side files land byte-identical | **MET** | `git cat-file blob 744ed4a708…:cowork_rulings_2026_08_25_landing_return_sitting.md \| sha256sum` = `de7b6b27eead0e95e9efd921185139bc1cdcb41fdfe269ca3323e9b9f0f7f9d1`, size 9544 — **equal to the Task-1 working-tree measurement**. `…:cowork_handoff.md` = `8e383c6b93406f1efd83b61da7221d536eb54a1fff3f8d68f33dc0511fd8c463`, size 698370 — **equal to Task 1**. |
| **E1** | Task 4's commit contains exactly five paths | **MET** | `changed_paths.py --commit 744ed4a708…` → the five listed in §4, `5 changed path record(s)`. |
| **E2** | the `OI-376` row differs in exactly the citation and its correction note; no other row changed | **MET** | Row-by-row comparison against `2dfe0ba485:OPEN_ITEMS.md`: 376 rows both sides, none added, none removed, **`rows whose text CHANGED: ['OI-376']`**, **non-row lines equal `True`**. Before/after quoted at §2.1. |
| **E3** | the guard set reports `failing: 1`, the standing red | **NOT MET — REPORTED, STOPPED** | `failing: 2` — the standing red `gen_filing_convention_application.py --check` **and** `gen_session_start_read_size.py --check`, the latter caused by this batch's own Task 3(a) (§5.3). **Not fixed.** |
| **E4** | the batch lands exactly TWO commits, in order | **MET** | `744ed4a708d3a3cf1c6764ccf2bf6ab33fa5aa2b` then the second commit carrying `tools/audit/guard_state.json`, the instruction and this report. The ordered structure yielded exactly two; none was invented and none absorbed. |

**And the dispatch's own assumptions:**

| # | assumption | verdict |
|---|---|---|
| **A1** | no entry count asserted; measure it | **MEASURED — ONE new entry** (§6). Not a STOP. |
| **A2** | the tip has not moved | **HOLDS** (§1.1). |
| **A3** | the citation correction changes neither derivation | **HOLDS, and falsified by experiment rather than argued** (§3.2) — the artifact is byte-identical generated before and after the correction. |
| **A4** | the two regenerations discharge exactly two of the three reds, leaving the standing red alone | **FALSIFIED.** Both regenerations' `--check` now pass and the standing red is untouched — but **a fourth red appeared**, caused by Task 3(a) itself. **STOP declared and reported (§5.2, §5.3).** |
| **A5** | only the two named artifacts change on disk from the regenerations | **HOLDS** (§3.5). |

---

## 8. FINDINGS ROUTED UNDER §5

**Analysis findings: NONE.** This batch read no analysis surface, ran no measurement of the
analysis, and touched nothing under `src/`, `tools/corpus/` or `tools/robust_stop/`.

**Apparatus findings — REPORTED, NO REGISTER ROW OPENED, NOTHING FIXED:**

1. **`gen_session_start_read_size.py --check` goes red by construction whenever an open row is added
   to the register** (§5.3). Its measurement is pinned to a span of
   `tools/audit/nongating_apparatus_rows.json` that the non-gating generator rewrites whenever the
   open population moves. **Found 2026-08-25. Reported because it is the second consumer in two
   consecutive batches to go red on the same single cause, and a reader of the guard summary cannot
   tell from `failing: 2` that one of the two is a downstream echo of an act the same batch
   performed.** Not remedied; no remedy proposed.

2. **A hand-transcribed derived count inside a live tool's own published prose** (§5.4): `"the 216
   gating rows"` in `gen_session_start_read_size.py`'s authored `FURTHER_SPANS` text, where the
   derived value at this tree is `217`. **Found 2026-08-25.** #17f / **D-431**. Not remedied.

3. **`core.autocrlf` is `true` in this clone, so a working-tree sha256 and a `git cat-file blob`
   sha256 agree only for a file whose working copy already has LF endings.** Measured: the two
   writing-side files and `OPEN_ITEMS.md` and `evidence_pin_membership.json` have LF working copies,
   so E0's prescribed measurement was exact for them; **`tools/audit/nongating_apparatus_rows.json`
   has a CRLF working copy** (176351 bytes) **and its blob is 173748 bytes**, so the same comparison
   applied to that artifact would report a false difference. **Found 2026-08-25. Reported so a
   future dispatch prescribing `git cat-file blob … | sha256sum` against a working-tree hash knows
   which files it holds for.** Nothing changed; no `.gitattributes` touched.

**Declined to act on:** all three of the above, and the standing red — the dispatch forbids fixing
what is found, and §8 forbids regenerating any artifact beyond the two named.

**A departure from the harness default, recorded rather than left silent:** the session harness
directs that git commit messages end with a `Co-Authored-By:` trailer. **This repository's commit
messages carry none**, and the dispatch prescribes the message's content precisely inside a batch
whose §8 says it changes nothing else. **Both commits follow the repository's convention and carry
no trailer.** Stated here so the choice is visible and reversible.

---

## 9. WHAT THIS BATCH DID NOT DO (§8, confirmed at the objects)

No `src/` change; no build; no test written, run, moved or changed; no golden refreshed; nothing
under `tools/corpus/` or `tools/robust_stop/`; no behaviour change and no design. **No register row
was created, closed, flipped, re-scoped or re-worded** — `OI-376`'s citation was corrected and
nothing else about it moved, and the row-level diff at §2.1 proves it. **No gating verdict and no
apparatus declaration were added to any row.** [[OI-372]] and its tool were not touched. **No
derivation boot pack, pack generator, manifest, withheld family, session brief or blind derivation
output was touched, and no blind output was read at all.** `CLAUDE.md`, `STATUS.md`, `DECISIONS.md`
and `ARCHITECTURE.md` are unmoved (`DECISIONS.md` was READ, at §1.5, and not written). **No
generated artifact was regenerated other than the two named plus `tools/audit/guard_state.json`,
which the guard run writes of its own accord.** No finding number was allocated. No remedy for
`OI-376`'s hazard is proposed. No derivation session was opened, booted or prepared.

**[[OI-179]] stays OPEN and GATES. [[OI-374]] stands as found. The three deferred apparatus items
stay deferred.**

---

## 10. THE SELF-CHECK (`CLAUDE.md`, after every coding exercise)

The diff of every touched file was re-read on disk before the first commit, not recalled:
`OPEN_ITEMS.md` (one row, one parenthesis, verified row-by-row against two commits); the two
regenerated artifacts (both `--check` PASS, both compared field-by-field against the tip);
`cowork_handoff.md` and `cowork_rulings_2026_08_25_landing_return_sitting.md` (**not edited — only
measured**, and byte-identical at the committed objects). The correction note is American English,
carries no invented label or abbreviation, and names its dispatch and date. `git status` was never
issued; every working-tree read went through the file tools; every historical read was a git object
query by explicit hash.

**One rule was strained and is declared:** measuring a sha256 has no file tool, so it was done with
a hashing script **held outside the repository**, which returns a size and a digest and cannot
return content. The read-only re-measurement at §5.3 imported the guard's own `measure()` and wrote
nothing.

---

## 11. THE TWO COMMITS

| order | hash | what it carries |
|---|---|---|
| 1 | `744ed4a708d3a3cf1c6764ccf2bf6ab33fa5aa2b` | the five paths of §4 |
| 2 | *(this report rides it)* | `tools/audit/guard_state.json`, `cc_instruction_regeneration_and_citation.md`, `cc_report_regeneration_and_citation.md` |

**The E-ordering rule is honored: the first commit asserts no end state, and this run is what says
what the end state is — `failing: 2`, one of them caused by this batch and STOPPED on rather than
fixed.**
