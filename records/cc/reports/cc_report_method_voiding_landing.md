# CC REPORT — the method-voiding landing batch

> **CC, 2026-08-25.** Executing `cc_instruction_method_voiding_landing.md` (measured at the working
> tree this session: **17220 bytes**, sha256
> `b99c0e9abd4dd9b19a44efb61128982355f0abb0b299681f838848e4823778d1`).
>
> **★ THE BATCH RAN TO ITS END AND THEN STOPPED AT TASK 3's OWN STOP CLAUSE.** Both commits landed.
> The guard set was run and reports **THREE** failures, not one. **Nothing was fixed**, no artifact
> was regenerated to make a check pass, and no verdict was added to the new row. §7 below gives each
> failure, and §8 establishes which of them this batch caused and which it did not.

---

## 0. TASK 0 — the stale lock

| what was measured | result |
|---|---|
| `.git/index.lock` present before the act | **YES** |
| its size | **0 bytes** — as §0 predicted; **no STOP** |
| its last-write time | `2026-08-25T13:45:52.6350016+02:00` |
| any running `git` / `git-remote-https` / `gitk` process | **NONE** |
| deleted | **YES**, and re-checked absent afterwards |

**The instruction's premise held in both halves.** The lock was zero bytes and no git process was
running, so the §0 STOP condition was not reached.

---

## 1. TASK 1 — the declared start state, measured before any write

### 1.1 The tip (P1 / A2)

```
git rev-parse HEAD            -> f225b61343ff3de022d32d6b7514d835b87093cf
refs/heads/master             -> f225b61343ff3de022d32d6b7514d835b87093cf
refs/remotes/origin/master    -> f225b61343ff3de022d32d6b7514d835b87093cf
git symbolic-ref HEAD         -> refs/heads/master
```

**P1 CONFIRMED — the tip is unmoved and both refs stand at it. A2 not falsified.** (For
completeness: `refs/remotes/upstream/master` is at `3c30b9676a6f764b28185e757f7156164c2d735c`, which
is the fork's upstream and is unrelated to this batch.)

### 1.2 The changed-path enumeration — AND A SUBSTITUTION THIS SESSION HAD TO MAKE

**§4 asks for the output of `git status --porcelain -uall`. THAT COMMAND IS BLOCKED IN THIS
REPOSITORY.** The `PreToolUse` guard refused it with:

> *"`git status` is not trusted for what is current — `CLAUDE.md` Conventions, register entry
> D-253. The sanctioned way to enumerate which paths changed is `python
> tools/audit/changed_paths.py` (`--staged`, or `--commit <hash>`), which reports paths and status
> codes and cannot return file content."*

**The sanctioned tool was used instead, in every place §4 and E1 call for a status enumeration.**
This is recorded as a finding at §9(F-1) and is not treated as a defect in the instruction's
substance — the enumeration was obtained, by the route this repository mandates.

**The enumeration at session start, before any write:**

| class | count |
|---|---|
| tracked, modified | **1** — `cowork_handoff.md` |
| untracked | **835** |
| **total changed path records** | **836** |

Of the 835 untracked paths, **exactly four are this batch's**: the three 2026-08-25 ruling records
of P2 and the instruction file of P2a. **The other 831 are a pre-existing untracked population**
that stood in the tree before this session began and that this batch neither created nor touched.
See §9(F-2) — this is the one place the tree does not match A4's expectation, and none of the 831
entered either commit.

### 1.3 The four P2 paths, measured AT THE WORKING TREE before any write

| path | measured bytes | P2 bytes | measured sha256 | matches P2 |
|---|---|---|---|---|
| `cowork_handoff.md` | 688028 | 688028 | `cf5f2a49479945809f9ecf65343fc16a499d122209c49e1d355463576996dad9` | **YES** |
| `cowork_rulings_2026_08_25_determination_route_sitting.md` | 7635 | 7635 | `e3791743a73899d9c7027d67f55d2fa6a5fd0e171dd3e5ea651ed649999153e5` | **YES** |
| `cowork_rulings_2026_08_25_forward_fact_sitting.md` | 8859 | 8859 | `cd60697990c167c771e2800308775636ba11a1add6a8491312f4d01b6f47197d` | **YES** |
| `cowork_rulings_2026_08_25_method_voiding_sitting.md` | 19961 | 19961 | `0c27e6f88d941deed1b239876d6da61b21c2c717b1013152137fa54d49cbd6a4` | **YES** |

**All four match P2's table exactly, at the working tree, before anything was staged.**

### 1.4 The instruction file (P2a)

| path | bytes | sha256 |
|---|---|---|
| `cc_instruction_method_voiding_landing.md` | **17220** | `b99c0e9abd4dd9b19a44efb61128982355f0abb0b299681f838848e4823778d1` |

**It was not edited.**

### 1.5 The register's highest identity, measured on BOTH surfaces

| surface | how it was measured | highest identity |
|---|---|---|
| `OPEN_ITEMS.md` (the INDEX) | Grep over the file for any identity of 376 or above (three-digit values from 370 up, all four-digit values); the highest match is `OI-375`, at line 413 | **OI-375** |
| `open_items/` | Glob `open_items/OI-3[5-9][0-9].md` (highest present is `OI-375.md`) and `open_items/OI-[4-9][0-9][0-9].md` (**no files found**) | **OI-375** |

**THE TWO SURFACES AGREE. No disagreement of the kind P4 asks about was found at the maxima**, so
the next free identity is taken as the one above the agreed maximum: **OI-376**.

**And the derivation was confirmed independently, after the fact, by a tool this batch did not
author.** `tools/audit/register_lint.py` — run as a member of the guard set at Task 3 — writes
`open_items/register_check.json`, whose committed copy at the tip reads `index_item_count: 375` and
`detail_file_count: 375`, and whose copy after this batch reads **376 and 376**. Both counts equal
the maximum identity in both states, so the register carries **no gap and no orphan** across
`OI-1…OI-375`, and `OI-376` was in fact free. See §5.

### 1.6 §0's result

Reported at §0 above.

---

## 2. THE §1 QUOTE VERIFICATION — §9 of the instruction made this a STOP condition

**All four quotations in the instruction's §1 were checked against the objects they cite. All four
match. NO STOP.**

| quoted from | checked at | verdict |
|---|---|---|
| `cowork_rulings_2026_08_25_method_voiding_sitting.md` §5 — *"One ordinary CC dispatch is owed…at an identity it MEASURES."* | the file in the working tree, lines 206–209 | **MATCHES** |
| the same record §4 — *"It is rowed in the open-items register under rules (c) and (e)…never asserted by this side."* | the same file, lines 164–170 | **MATCHES** |
| the same record §4 — *"The landing batch therefore creates the row WITHOUT a non-gating declaration…put to the user on its own surface."* | the same file, lines 197–199 | **MATCHES** |
| `cowork_rulings_2026_08_21_successor_plan_sitting.md` §9 (Ruling 9) — *"A finding that bears on the analysis…No findings series is opened."* | **the git object at the tip**, `f225b61343:cowork_rulings_2026_08_21_successor_plan_sitting.md`, §9 at lines 107–113 | **MATCHES verbatim** |
| `CLAUDE.md` register rules (c) and (e) | the live file, lines **317–321** | **MATCHES verbatim** |

**So the writing side's §4 correction — that there is no "Ruling 9(b)" and that Ruling 9 opens no
findings series — is itself correct at the object.** Ruling 9's text at the tip reads, in full:
*"A finding that bears on the analysis goes to the quarantined audit questions; a finding about the
apparatus is rowed under the open-items register's rules (c) and (e) and lapses under the ruled
lapse rule (D-676); everything else is discarded under the worth test (#10) with finding, date and
reason. The predecessors' 'no numbers, no rows' is not adopted. No findings series is opened."*
It carries no limbs.

**One reading note, recorded because it cost a step and would cost the next reader one too:** a
plain search of `CLAUDE.md` for the phrase *"newly discovered issue"* returns **nothing**, because
rule (c)'s wording is broken across a line — *"every newly⏎discovered issue"*. The rule is present
and verbatim; only a line-anchored search misses it. Nothing is wrong with the file.

---

## 3. TASK 2 — the identity, the detail file, the row, and the commit

### 3.1 The identity and how it was derived

**N = 376.** Derived as §1.5 records: the highest identity was measured **independently on both
surfaces** — `OI-375` in the INDEX and `OI-375.md` in `open_items/` — the two agreed, and the next
free identity above the agreed maximum was taken. **No identity was carried from P4's lead**; P4's
value was treated as the lead the instruction declares it to be and was re-measured. **No finding
number was allocated**, Ruling 9 opening no findings series.

### 3.2 The detail file — `open_items/OI-376.md`

Written from `cowork_rulings_2026_08_25_method_voiding_sitting.md` §4, **quoting rather than
paraphrasing where that record states the finding**. It carries narrative and provenance only and
**no status of its own** (P3), and it carries each of the seven things Task 2(a) requires:

1. **The finding**, quoted from §4 verbatim.
2. **The mechanism, attributed as a relayed account** — with the record's own boundary sentence
   quoted (*"this side ran no measurement of the mechanism and does not claim one"*), and **the
   walk-up variable recorded as INFERRED, NOT OBSERVED**, again in the record's own words.
3. **The four configurations**, listed and marked **relayed, not endorsed**.
4. **The consequence**, including *"a ruling is not binding mechanically. It binds only a session
   that met it."*
5. **The irony**, quoted, with the reason it makes the row non-trivially-closable.
6. **Provenance** — discovered 2026-08-25, surfaced unasked by a throwaway Cowork session opened by
   the user and relayed by the user; rowed on Ruling 3 of the method-voiding record under Ruling 9
   of the successor-plan record and register rules (c) and (e).
7. **NO REMEDY.** None is proposed, sketched or listed. `CLAUDE.md` was **not** edited, split,
   moved, renamed, copied or duplicated, and **no** tripwire, check, marker or fallback file was
   added.

### 3.3 The INDEX row — `OPEN_ITEMS.md`

Appended as the **last row of section F**, immediately after `OI-375` and before the `## G.`
heading. **That is the register's own established append point:** every recent row (`OI-366`…
`OI-375`) sits at the tail of section F irrespective of what its own subject cell says, and the
derivations parse rows, never sections.

**The row shape was copied from its neighbours and verified mechanically, not by eye.** It splits
into **six** cells on `" | "`, and its status cell opens with the bare canonical token **`OPEN`**.
Confirmation, run before the commit:

```
python tools/audit/index_status_lint.py
  INDEX STATUS LINT: PASS - every status cell opens with one canonical token, and every row splits.
  exit:0
```

**The row is a pointer, not a restatement**: a name, a short description, the owning area, and the
`[detail](open_items/OI-376.md)` link. Its owning-area cell reads *"governing-instruction delivery
— whether this repository's standing instructions reach a session at all"*.

**★ THE ROW CARRIES NO APPARATUS CLAIM AND NO NON-GATING DECLARATION**, as ruled. It was **not**
"helpfully" declared apparatus. §8.1 records what the derivations then did with it.

### 3.4 The commit

```
2dfe0ba485f438817f60385b4f6ea9fc0e6e4432
```

**Message:** *"record: the three 2026-08-25 ruling records land, together with the handoff entries
they close on (the tree carries FOUR new entries, through the sixtieth, not the one the dispatch
anticipated); and OI-376 opens on the CLAUDE.md discoverability hazard — rowed under register rules
(c) and (e) in the same commit that records the discovery, at a MEASURED identity, with no finding
number, no apparatus declaration and no remedy"*

**Changed-path list (`git show --name-status`), exactly six paths:**

```
M  OPEN_ITEMS.md
M  cowork_handoff.md
A  cowork_rulings_2026_08_25_determination_route_sitting.md
A  cowork_rulings_2026_08_25_forward_fact_sitting.md
A  cowork_rulings_2026_08_25_method_voiding_sitting.md
A  open_items/OI-376.md
```

**No other path entered it.**

---

## 4. TASK 3 — the guard set

**Run:** `python tools/audit/gen_guard_state.py` (write mode), at the tree Task 2's commit left.

**The summary, in its ruled shape:**

```
{
  "run": 75,
  "passing": 72,
  "failing": 3,
  "failing_tools": [
    { "tool": "tools/audit/gen_nongating_apparatus_rows.py",   "args": ["--check"] },
    { "tool": "tools/audit/gen_filing_convention_application.py", "args": ["--check"] },
    { "tool": "tools/audit/gen_evidence_pin_membership.py",    "args": ["--check"] }
  ],
  "not_run": 4,
  "historical_records": 16
}
```

**The population is UNMOVED at 75**, and `not_run` (4) and `historical_records` (16) are unmoved
from the committed baseline. **What moved is `passing` 74 → 72 and `failing` 1 → 3.**

**The committed baseline at the tip, for comparison:** `{run 75, passing 74, failing 1,
failing_tools [gen_filing_convention_application.py --check], not_run 4, historical_records 16}`.

**★ TWO FAILURES BEYOND THE STANDING RED. Task 3's stop clause was obeyed: NOTHING WAS FIXED.** No
artifact was regenerated to clear a check, no verdict was added to `OI-376`, and no tool was
edited. §8 establishes the cause of each.

**What the run legitimately produced** (the only two paths it wrote):

| path | what changed |
|---|---|
| `tools/audit/guard_state.json` | the run's own record, including its three failures |
| `open_items/register_check.json` | `index_item_count` and `detail_file_count` each 375 → 376, `OI-376` added to `post_baseline_ids` |

`open_items/split_reconciliation.json` did **not** change: it is pinned to `baseline_commit
cb246a7580` and reconciles the 200 items that existed at the split, so a new row does not enter it.

---

## 5. THE MEASURED HANDOFF DIFFERENCE (A1) — FALSIFIED, IN THE DIRECTION A1 ALLOWS

**A1 orders a measurement rather than an assertion, and the measurement disagrees with the writing
side's expectation in BOTH of its halves. A1 states this is expected-possible and NOT a STOP.**

**Measured at the git objects** — the tip blob `5d6c643eb687353674f1242524db861473873bc0` against
the staged blob `da089f1f234e3a0a964ce0aa5ee9dab8b348c22c`:

```
git diff --shortstat  ->  1 file changed, 449 insertions(+), 1 deletion(-)
git diff -U0          ->  ONE hunk: @@ -4 +4,449 @@
```

### 5.1 The number of inserted entries: **FOUR**, not one

Entry headings, counted on both sides with the same pattern:

| side | entries | newest |
|---|---|---|
| the tip (`f225b61343:cowork_handoff.md`) | 11 matched headings from the head down | **FIFTY-SIXTH** |
| the working tree | 15 matched headings from the head down | **SIXTIETH** |

**The four inserted entries are the SIXTIETH, FIFTY-NINTH, FIFTY-EIGHTH and FIFTY-SEVENTH** — at
working-tree lines 4, 164, 282 and 368 respectively.

**The tail is provably unmoved.** Every one of the eleven shared headings sits at exactly **+448**
lines in the working tree relative to the tip (FIFTY-SIXTH 4→452, FIFTY-FIFTH 130→578, FIFTY-FOURTH
230→678, FIFTY-THIRD 343→791, FIFTY-SECOND 457→905, FIFTY-FIRST 547→995, FIFTIETH 630→1078,
FORTY-NINTH 727→1175, FORTY-EIGHTH 820→1268, FORTY-SEVENTH 897→1345, FORTY-SIXTH 1009→1457), and
the single diff hunk begins at line 4 — so the change is **448 wholly new lines prepended plus one
rewritten line**, and nothing below it moved.

### 5.2 The one rewritten line is the **FIFTY-SIXTH** entry's heading, not the fifty-ninth's

The instruction's A1 says the writing side *"appended a superseded-marker to the fifty-ninth
heading"*. **At the tip there is no fifty-ninth entry at all** — it is one of the four new ones. The
single deleted-and-replaced line is the **FIFTY-SIXTH** entry's heading, which gained the trailing
marker *"(SUPERSEDED as the entry point by the fifty-seventh entry above.)"*.

Any superseded-markers on the fifty-seventh, fifty-eighth and fifty-ninth headings are **inside the
448 newly inserted lines** and therefore invisible to a diff against this tip.

### 5.3 What this does and does not mean

**It is not a STOP** — A1 says so in terms. **The four files still land byte-identical** (§7, E0), so
nothing about the landing is affected. What it means for the record is only that the handoff on disk
was **three cycles further ahead** of the tip than the instruction assumed.

---

## 6. THE §5 ROUTING — nothing was acted on

**No finding that bears on the analysis was met.** This batch read no analysis code, no measured
value, no corpus and no blind derivation output.

**No second register row was opened.** This batch opened exactly one, `OI-376`, and every apparatus
finding below is reported here and nowhere else, as §5 directs.

**Nothing found was fixed.** §9 lists each finding; none was repaired.

---

## 7. REGISTERED EXPECTATIONS

### E0 — the four files land byte-identical: **MET**

**Measured at the committed objects** (`git cat-file blob 2dfe0ba485:<path> | sha256sum`), not at
the working tree:

| path | committed bytes | committed sha256 | equals P2 |
|---|---|---|---|
| `cowork_handoff.md` | 688028 | `cf5f2a49479945809f9ecf65343fc16a499d122209c49e1d355463576996dad9` | **YES** |
| `cowork_rulings_2026_08_25_determination_route_sitting.md` | 7635 | `e3791743a73899d9c7027d67f55d2fa6a5fd0e171dd3e5ea651ed649999153e5` | **YES** |
| `cowork_rulings_2026_08_25_forward_fact_sitting.md` | 8859 | `cd60697990c167c771e2800308775636ba11a1add6a8491312f4d01b6f47197d` | **YES** |
| `cowork_rulings_2026_08_25_method_voiding_sitting.md` | 19961 | `0c27e6f88d941deed1b239876d6da61b21c2c717b1013152137fa54d49cbd6a4` | **YES** |

**★ AND A HAZARD THAT DID NOT BITE, RECORDED BECAUSE IT NEARLY COULD HAVE.** `git add` emitted, for
every one of the six paths, *"LF will be replaced by CRLF the next time Git touches it"* — this
repository normalizes line endings. **It did not alter any blob**: the worktree copies already carry
LF, so index and worktree bytes are identical, and the committed sha256 values above are proof
rather than assumption. The two register files landed at `OPEN_ITEMS.md` 343346 bytes /
`34e5b801d15415cda7e30d48868440a5c259c684d49e5000883042bc4ad28afb` and `open_items/OI-376.md` 6797
bytes / `f9d77d8602e9b594babeeadb0051a86247c7a07e1df247ae68d4cf2057db436b`.

### E1 — the row and its detail file, at a measured identity, in the SAME commit as the four files: **MET**

**The commit's changed-path list contains exactly six paths** — the four of P2, `OPEN_ITEMS.md` and
`open_items/OI-376.md` (listed at §3.4; count verified as **6**).

**The identity is N = 376**, derived as §1.5 and §3.1 record: measured independently on both
surfaces, the two agreeing at `OI-375`, and confirmed after the fact by `register_check.json`'s
count moving 375 → 376 with no gap and no orphan.

### E2 — the batch lands exactly TWO commits, in order: **MET**

**Two, in order:** Task 2's `2dfe0ba485f438817f60385b4f6ea9fc0e6e4432`, then Task 3's, whose parent
is that commit.

**★ ONE THING THIS REPORT CANNOT CARRY, AND IT IS STATED RATHER THAN GUESSED: TASK 3's COMMIT HASH
IS NOT IN THIS FILE.** This report rides Task 3's commit (P2a), and **a file cannot state the hash
of the commit that contains it** — the same reason the instruction itself gives for publishing no
expected hash of its own. What is stated instead is everything that determines it: its **parent**
(`2dfe0ba485f438817f60385b4f6ea9fc0e6e4432`), its **exact changed-path list** (§10), and its
**message** (§10). It is read off the branch with `git log -1 --format=%H`. **No third commit was
made to record it**, because that would break E2 for a bookkeeping convenience.

---

## 8. THE TWO FAILURES BEYOND THE STANDING RED — which this batch caused, and which it did not

### 8.1 `gen_nongating_apparatus_rows.py --check` — **CAUSED BY THIS BATCH. A5 IS FALSIFIED.**

```
FAIL: nongating_apparatus_rows.json differs from what the generator now produces
```

**A5 predicted the non-gating apparatus set would be unaffected. It is not — the ARTIFACT no longer
re-derives.** The instruction's own falsification clause is what is being reported here, and its
instruction was followed exactly: **the artifact was NOT regenerated, no verdict was added to
`OI-376` to make the check pass, and the tool was not touched.**

**Why A5's reasoning was half right, read at the tool's own source.** A5's ground was that the row
makes no apparatus claim and so is not one of the set's candidates. **That half holds.** The tool's
first cut is `any(v.lower() in row.subject_column.lower() for v in FIRST_CUT_VOCAB)` — matched
against **cell 4 only** — and `OI-376`'s cell 4 (*"governing-instruction delivery — whether this
repository's standing instructions reach a session at all"*) contains **no member** of that
vocabulary. So the row is **outside the over-inclusive first cut**, it needs no authored verdict,
and the tool did **not** raise its missing-verdict STOP.

**What A5 did not account for is the OTHER side of the same artifact.** Since 2026-08-17 the file
also publishes **the live gating answer** — `gating_ids`, which is the *complement* of the
non-gating verdicts over **every open row the tool parses** — together with `open_rows`. Adding one
open row therefore moves the artifact **by construction**, whatever its subject. `--check`
re-derives and exits 1 on any difference, so the failure is the artifact being **out of date, not
wrong**.

**★ WHAT THIS BATCH CAN AND CANNOT SAY ABOUT WHETHER `OI-376` GATES.** It **cannot** say it from the
artifact: `--check` does not write, so the derivation's own answer about `OI-376` does not exist on
disk, and producing it would have been the regeneration this batch is forbidden. What it can say is
a **reading of the tool's source, labelled as such**: a row outside the first cut takes
`OUTSIDE_THE_CUT_GROUND` and is placed on the **gating** side by the ruled default. That is the
outcome §4 of the ruling record intends. **It is a reading, not a measurement, and Cowork should
treat it as one.**

**A neighbouring derivation was checked and is UNAFFECTED, which is worth knowing:**
`gen_gating_row_sizing.py --check` **PASSED**. Its population is not "every gating row" but
`phase1_completion_inventory.json → the_gating_split.gates.ids`, which is computed over that tool's
**wide cut** — rows whose cell 4 matches a documentation vocabulary, or whose text matches a list of
falsity signals. `OI-376` matches neither, so it does not enter that population and **no sizing is
owed for it by that pass**. Recorded so that a later reader does not mistake the sizing pass's
silence for an oversight.

### 8.2 `gen_evidence_pin_membership.py --check` — **NOT CAUSED BY THIS BATCH. IT WAS ALREADY FAILING AT THE TREE AS FOUND.**

```
STALE vs the derivation: evidence_pin_membership.json does not re-derive
```

**Established from three measured facts, each recorded here so the conclusion can be checked rather
than believed:**

1. **What the tool derives from**, read at its own source: *"RULING RECORDS — Every root-level
   `cowork_rulings_*.md`."* It scans the **filesystem**, not git, so an untracked record in the root
   is an input exactly as a committed one is.
2. **The three 2026-08-25 ruling records were already present in the working tree at the tip** —
   measured by this session at §1.3 **before any write**, with sizes and hashes matching P2.
3. **The committed artifact carries no 2026-08-25 record at all.** A search of
   `tools/audit/evidence_pin_membership.json` for `cowork_rulings_2026_08_2[0-9]` returns matches for
   `…_08_21`, `…_08_22`, `…_08_23` and `…_08_24` and **none** for `…_08_25`.

**Therefore the derivation and the artifact already disagreed at session start**, and `--check`
would have reported STALE before this batch did anything. The committed `guard_state.json` recording
`failing: 1` was produced by the batch that made `f225b61343`, at a tree that did not yet carry
those three files — the writing side wrote them afterwards, in the sitting that produced this
instruction.

**This is an INFERENCE from three measurements, not a re-run.** The check was **not** re-run with
those files absent, because doing so would have meant moving committed files out of the tree. If
Cowork wants it observed rather than inferred, that is a separate act.

**It was not fixed.** The commit at the tip whose message ends *"the membership is regenerated"*
shows that regenerating this artifact is the ordinary act when the ruling-record population moves —
**but this batch is not authorized to perform it**: §8 of the instruction forbids regenerating any
generated artifact except as Task 3's run does so of its own accord, and `--check` writes nothing.
**The regeneration is therefore OWED and is left for Cowork to route.**

### 8.3 `gen_filing_convention_application.py --check` — the standing red, unchanged

Failing exactly as the instruction predicts, on `OPEN_ITEMS.md` **OI-372**. **Untouched.**

---

## 9. FINDINGS ROUTED UNDER §5 — every one, including those declined

**All are apparatus findings. Per §5 none opened a second register row, and per the standing bar
none was fixed.**

**F-1 — `git status` is forbidden in this repository, and the instruction asks for it.** §4 orders
*"the output of `git status --porcelain -uall`"*; the repository's `PreToolUse` guard refuses that
command, citing `CLAUDE.md` Conventions and register entry **D-253**, and names
`tools/audit/changed_paths.py` as the sanctioned route. **Date:** 2026-08-25. **Reason it is
reported rather than discarded:** it is a live contradiction between a dispatch's declared start
state and a standing repository rule, and it will recur in every future dispatch written with that
wording. **Action taken:** the sanctioned tool was used; the enumeration §4 asks for was obtained in
full. **Not fixed, and no row opened.**

**F-2 — the tree carries 831 untracked paths unrelated to this batch, so A4's expectation does not
describe it.** A4 declares P2's four plus P2a's two to be *"the complete set of paths this batch
expects to differ from the tip"*. **Measured: 836 changed path records at session start** — one
tracked modification and 835 untracked. **Date:** 2026-08-25. **Reason:** A4 instructs that any
other path be reported. **Established as pre-existing:** the same population is visible in this
session's own start-of-conversation snapshot, before any act of this batch. **Action taken:** none
of the 831 entered either commit; both commits' path lists were verified explicitly before and after
committing. **Not fixed, and no row opened** — this is a standing condition of the tree, not a
defect this batch created.

**F-3 — A1 is falsified in both halves.** Four inserted handoff entries, not one; and the one
rewritten line is the fifty-**sixth** entry's heading, not the fifty-**ninth**'s. **Date:**
2026-08-25. **Measured at the git objects**, §5. **A1 declares this expected-possible and not a
STOP**, and it was treated as such. **Reason it is reported:** the writing side records having got
this assertion wrong twice, and the measurement now says it was wrong a third time and by three
entries.

**F-4 — A5 is falsified: the non-gating apparatus artifact no longer re-derives.** §8.1. **Date:**
2026-08-25. **Not fixed**, exactly as A5 instructs.

**F-5 — a second guard was already red at the tree as found, and the instruction did not know it.**
§8.2. **Date:** 2026-08-25. **Reason:** the instruction names exactly one standing red and directs a
STOP on any other, so a reader of the batch record must be told that this one predates the batch,
or the two commits will be read as having caused it. **Its regeneration is OWED and is left for
Cowork.** **Not fixed, and no row opened.**

**F-6 — a commit-message convention was deviated from deliberately, and it is disclosed rather than
silently taken.** This session's harness carries a standing default to end every commit message with
a `Co-Authored-By` trailer. **Every commit in this repository's recent history carries no trailer at
all** — verified at the objects, `git log -3 --format=%B f225b61343`. **Both commits of this batch
follow the repository's convention and carry no trailer.** **Date:** 2026-08-25. **Reason:** this
repository's commit messages are themselves part of the record the project keeps, and introducing an
unrequested trailer into it is a change to the record's form that no ruling asked for. **Reported so
that the choice is the user's to reverse, not silently made.**

**F-7 — a reading note that is NOT a defect, recorded to save the next reader a step.** Rule (c) of
the open-items-register section cannot be found in `CLAUDE.md` by searching for *"newly discovered
issue"*, because the phrase is broken across a line. **Date:** 2026-08-25. **The rule is present and
verbatim at lines 317–321.** **Discarded** under the worth test: nothing is out of sync, no
consumer is affected, and the file is correct as it stands.

---

## 10. TASK 3's COMMIT

**Parent:** `2dfe0ba485f438817f60385b4f6ea9fc0e6e4432`

**Changed-path list — exactly four paths:**

```
M  open_items/register_check.json
M  tools/audit/guard_state.json
A  cc_instruction_method_voiding_landing.md
A  cc_report_method_voiding_landing.md
```

**Message:** *"end state: the guard set run at the tree Task 2's commit left — 75 run, 72 passing,
THREE failing, and the two beyond the standing red are reported and NOT fixed; the one this batch
caused is A5 falsified (the register's open population moved by OI-376) and the other was already
red at the tree as found; the instruction and the report land"*

**Nothing else entered it.** In particular no regenerated derivation, no governing document, and
none of the 831 unrelated untracked paths.

---

## 11. WHAT THIS BATCH DID NOT DO — checked against §8 of the instruction

No `src/` change; no build; no test written, run, moved or changed; no golden refreshed; nothing
under `tools/corpus/` or `tools/robust_stop/`; no behaviour change and no design.

It did not touch either derivation boot pack, the pack generator, the manifest, either withheld
family, either session brief, or either blind derivation output; **it did not read either blind
output at all, not even a bounded receipt**; it did not open, close, flip, re-word or annotate any
register row other than `OI-376`, which it created; it did not amend, reflow or correct any of the
four landing files; it did not touch `CLAUDE.md`, `STATUS.md`, `DECISIONS.md`, `ARCHITECTURE.md` or
any other governing document; **it regenerated no generated artifact except the two Task 3's guard
run wrote of its own accord** (§4); it allocated no finding number; it proposed no remedy for the
hazard it rowed; and it opened, booted and prepared no derivation session.

**[[OI-179]] stays OPEN and GATES. [[OI-372]] and [[OI-374]] stand as found. The three deferred
apparatus items stay deferred — none was picked up.**

---

## 12. THE SELF-CHECK, AFTER READING THE ACTUAL DIFF

**What was re-read, stated at the precision it was actually done rather than as a blanket claim.**
Task 2's six paths were verified **at the committed objects** by size and sha256 (§7), and
`cowork_handoff.md`'s change was read as a git-object diff, hunk by hunk (§5). Of Task 3's two
generated artifacts, `open_items/register_check.json` was compared head-to-head against its tip blob
and `tools/audit/guard_state.json` was read at its summary block and at each failing tool's captured
output; **neither was read as a full diff**, both being tool-written rather than authored here. The
two authored register files and this report were read in full.

- **The two new register files are the only authored content.** `open_items/OI-376.md` carries no
  status of its own (P3) and no remedy (Task 2(a)(7)). The `OPEN_ITEMS.md` change is exactly one
  inserted row; the lint confirms every row still splits into six cells and every status cell still
  opens with a canonical token.
- **No self-invented label, abbreviation or numbering scheme was introduced.** The row uses the
  register's own identity scheme; no finding number exists.
- **#17f / D-431 respected:** no figure was hand-transcribed. Every count, size and hash in this
  report was measured this session at the object or the working tree, and every artifact figure is
  quoted from the artifact.
- **#12 respected:** nothing was deleted, collapsed or overwritten. The two red checks are recorded
  as found rather than cleared, and the pre-existing one is distinguished from the caused one.
- **#19 respected in the direction that matters here:** the claim that `gen_evidence_pin_membership`
  was already failing is labelled an **inference from three measurements**, not a re-run, because it
  was not observed.
- **The never-work-from-memory rule:** every quotation in §2 was opened at its object; nothing in
  this report rests on the instruction's account of a source.

---

*Provenance: CC, 2026-08-25, executing `cc_instruction_method_voiding_landing.md` at tip
`f225b61343ff3de022d32d6b7514d835b87093cf`. Two commits: `2dfe0ba485f438817f60385b4f6ea9fc0e6e4432`
and its child, which carries this report. The batch completed both tasks and then obeyed Task 3's
stop clause: the two guard failures beyond the standing red are reported and neither is fixed.*
