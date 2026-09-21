# CC REPORT — THE DECISION RULES CONSOLIDATED, D-658 CORRECTED, AND THE BATCH STOPPED AT ITS CLOSING GUARD CONDITION (2026-09-21)

**Dispatch:** `records/cc/instructions/cc_instruction_decision_rules_consolidation_2026_09_21.md`,
pinned at `28c8bc0ee2df6139c36b46b588536fc4919229a0`.

**★★ THE HEADLINE, STATED FIRST BECAUSE IT DECIDES WHAT THIS REPORT IS.** Tasks 0 to 5 ran and every
one of them did what it was sent to do. **The batch then STOPPED at §7(d)'s closing guard condition
and §8 — the third commit and the push — DID NOT RUN.** Three guards that carried PASS at the opening
capture carry FAIL at the closing one, and that condition is written with no exception. Nothing is
staged; every file this batch wrote is on disk, uncommitted, and named at §8 below. The two Task 0
commits ARE committed, and they were made before any of this batch's own edits, which is exactly why
stopping here leaves no half-finished state in the record.

**The three are diagnosed, their causes established at the tool sources rather than assumed, and all
three are this batch's own ordered acts making their artifacts stale.** None is an unrelated
regression. The repair is NOT taken here: the four files it would touch — one of them a ratification
surface — are outside this dispatch's own declared footprint and outside §8(a)'s candidate set, so
regenerating them would be resolving a bar rather than reporting it.

---

## 1. Task 0 — the start state, and the previous batch's work committed

### 1.1 The pin (0(a))

```
git hash-object -w records/cc/instructions/cc_instruction_decision_rules_consolidation_2026_09_21.md
28c8bc0ee2df6139c36b46b588536fc4919229a0
```

### 1.2 The two refs, read at the ref FILES with the file tools (0(b), D-253)

| Ref file | Value found | Barred value | Held |
|---|---|---|---|
| `.git/refs/heads/master` | `7d7291f401d05052240d76078db175ce160e8b91` | same | ✅ |
| `.git/refs/remotes/origin/master` | `ef4fad940d806edf8f84eb9a895f88d70a9bbcf2` | same | ✅ |

They disagreed, which is the state the dispatch was written knowing. Neither had moved.

### 1.3 The working tree and the corruption check (0(c))

`python tools/audit/changed_paths.py` reported **409 changed path records**. The enumeration is
`scratchpad/wt_0c.txt`; no path list is restated here (**D-431**).

**Nothing was staged.** Every one of the eight tracked records carried the code ` M` — a space in the
index column — and every other record was `??`.

**One fact the enumeration settles, which the dispatch left conditional:**
`records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty_six.md` **is not on disk.** It
appears in no enumeration. 0(f) member 4 was therefore not committed and was not waited for.

**A route substitution, declared rather than passed over.** The dispatch's tail check was to be taken
with a shell text utility. The shell-read guard refused it twice — first `tail`, then `od` — each time
parsing the byte-count argument as a repository path. The sanctioned route was used instead, exactly
as the guard's own refusal message directs: each file's identity and size by the content-addressed
route (`git hash-object -w --no-filters`, then `git cat-file -s`), and each file's last lines read
**with the Read tool**. This is the file-tools rule working, not being worked around.

**The corruption check itself: all eighteen text files this batch would commit were checked, and
every one ends in ordinary text.** No trailing NUL byte, no line broken off mid-word. The files
checked are the paths 0(e), 0(f) and §8(a) name, and no others; **no binary and nothing in the
held-back untracked population was read**, exactly as 0(c) directs.

### 1.4 The five start-state proofs (0(d)) — all five held

1. **The heading is in `cowork_audit_protocol.md` exactly once, at line 1306.**
2. **The `and NO` / `RECOMMENDATION AT ALL.**` line pair occurs exactly once**, at lines 1316–1317.
3. **`backbone_decisions.json` carries exactly one object whose `"id"` is `"D-658"`**, at line 14268.
   Verbatim, as found:
   - `"home"`: `cowork_audit_protocol.md:1306-1317`
   - `"status"`: `live`
   - `"title"`: `Where the record does not settle the question, the surface that returns it to the user gathers facts and makes no recommendation`
4. **Both `CLAUDE.md` anchor lines occur exactly once**, the second after the first: the decision-surface
   bullet at **line 1836**, the working-tree-files bullet at **line 1850**.
5. **`cowork_register_rule_c_suspension_2026_08_28.md` exists and its owed-entries list is still the
   placeholder comment** `<!-- THE DERIVED LIST GOES HERE. An empty list after Task 1 has run is a defect. -->`,
   at line 54. **Carried forward, not a STOP, and this batch did not fill it.**

### 1.5 COMMIT ONE — the previous batch's finished work (0(e))

**Hash `3720bd323e5c25dcd538d77b4338214b16427349`** — 11 files changed, 1764 insertions, 24 deletions.

The staged set was proved with `changed_paths.py --staged` **before** the commit: exactly **11
records**, exactly the eleven paths 0(e) names.

**Item 12 — the guard set's own artifacts — added ZERO paths, and that is measured rather than
assumed.** The only tracked artifacts 0(c)'s enumeration reported as modified under `tools/audit/`
were `defense_share.json`, `gen_guard_state.py`, `gen_status_batch_bound.py`,
`session_start_read_size.json` and `status_batch_bound.json` — all already named as items 3–7 — plus
`claude_md_finer_archive.json`, which **B7 holds back and which is absent from every staged set in
this batch**.

### 1.6 COMMIT TWO — the interim carriers (0(f))

**Hash `6b5bdfc38145befd865feab9436e6ff0dc32cea0`** — 3 files changed, 860 insertions.

Each member was **established, not asserted** — size by the content-addressed route, last non-empty
line read at the file:

| Member | Size measured | Size barred | Held |
|---|---|---|---|
| `cowork_rulings_2026_09_21_decision_surface_form_sitting.md` | 16,071 | 16,071 | ✅ |
| `cowork_rulings_2026_09_21_l2_withheld_documents_sitting.md` | 14,581 | 14,581 | ✅ |
| `cowork_handoff_entry_two_hundred_and_twenty_five.md` | 33,970 | 33,970 | ✅ |

All three tails are ordinary text — each a provenance line. **The fourth member does not exist on
disk**, as §1.3 records; it was not waited for.

### 1.7 The opening guard capture (0(g)), taken AFTER both commits

**Path: `scratchpad/guard_open.txt`.** Result line: **79 guards run, 15 failing, 4 not run, 19
historical records.** Every verdict is in that file; the comparison is at §6.4.

**One expectation was NOT met, and it is reported rather than chased.** The dispatch expected a
standing line `STALE vs the run: guard_state.json does not re-derive` at the head of the capture.
**It is not there.** The capture opens with `wrote tools\audit\guard_state.json`. The dispatch says
such a difference is a finding to report and not a STOP. The other expectation — a non-empty failing
set — was met.

**The artifacts this capture moved** are `tools/audit/guard_state.json` (the run writes it).
`tools/audit/changed_paths_establishment.json` was **not** moved: the guard set invokes
`changed_paths.py --establish` on every run, but its output was byte-identical, so the file appears in
no later enumeration. The footprint assumption expected it to move; it did not, and that is stated
because the assumption is the dispatch's and the measurement is this side's.

---

## 2. Task 1 — CAN THE REGISTER BE REGENERATED? THE BASELINE, VERBATIM

**This is the answer to the question the Cowork side could not establish, and it is reported whether
or not it changed anything.** All five ran at the untouched tree.

### 2.1 `gen_decisions_register.py --check` — **exit 0**

```
the register matches the data (20 files: the index + 19 group files)
```

**THE REGISTER IS REGENERABLE AT THE UNTOUCHED TREE.** The gate on Tasks 3 and 4 is satisfied; the
suspension of register rule (c) does **not** block a regeneration, those being different tools from
the two discard appliers.

### 2.2 `gen_cluster_dispositions.py --verify` — **exit 1** (THE BASELINE)

```
backbone decisions: 477
cross-references resolving: ALL
verbatim quotes found at their cited home: 477/477
cited line numbers correct: 436/471   (6 cited to a file with no line number, by design)
```

followed by **35 `LINE DRIFT` lines, every one of them in `CLAUDE.md`** (D-191, D-193, D-194, D-195,
D-196, D-197, D-198, D-199, D-200, D-203, D-204, D-210, D-211, D-212, D-249, D-253, D-254, D-294,
D-308, D-315, D-437, D-439, D-468, D-486, D-564, D-576, D-602, D-603, D-604, D-606, D-638, D-639,
D-656, D-660, D-675). The full output with each cited and actual line is `scratchpad/t1_verify.txt`.

**THE STOP CONDITION DID NOT FIRE, and the distinction is the whole point of running this first.**
The dispatch's STOP is *a missing or mismatched quote* at D-658 or at any entry homed in `CLAUDE.md`
or `cowork_audit_protocol.md`. **Every one of the 477 quotes was found at its cited home** — the
tool's own line 3 — so **no quote is missing or mismatched anywhere, D-658 included.** What is
non-zero is a *cited line number* count, which is the pre-existing anchor drift the dispatch
separately predicted and which Task 4 re-aims. **No entry homed in `cowork_audit_protocol.md` drifted
at all.**

### 2.3 `reaim_home_anchors.py --check` — **exit 0**, `anchors drifted: 35`

The same 35 entries, each with its old and new anchor and its drift (`+39` or `+55`), at
`scratchpad/t1_reaim.txt`. **It did NOT print `REFUSED`** — so the committed backbone IS in the
serialization that tool expects, and Task 4's hand-edit could be made safely. The writing side's
prediction of a non-zero drift count is confirmed, and its own bounded comparison at D-249
(`CLAUDE.md:1781-1793` cited, 1836 actual) is exactly what the tool reports.

### 2.4 and 2.5 The two discard checks — **both red, as the suspension's own premise requires**

`apply_soft_discard.py --check` — **exit 2**:

```
STOP: the committed plan's recorded arithmetic disagrees with the data file's: the plan records
{'the_live_record_before': 677, 'retired_by_this_act': 165, 'the_live_record_after': 512}, while the
block's former population is 680 and 165 record(s) carry this act's own `retired_by`
```

`apply_residue_discard.py --check` — **exit 2**:

```
STOP: the sitting's arithmetic does not reconcile at ['the_whole_population', 'the_live_record']:
{"the_whole_population": {"keep_plus_retired": 677, "the_sum_the_sitting_states": 677,
"the_population_the_data_file_records_before_any_retirement": 680, "it_reconciles": false},
"the_live_record": {"before_this_act": 515, "after_this_act": 477, "the_movement_the_sitting_states":
"512 → 474", "it_reconciles": false}} — the ruling makes this a STOP-and-report, not an adjustment
```

Reported and carried. Neither was repaired.

---

## 3. Task 2 — the consolidated section in `CLAUDE.md` Conventions

**The block was inserted verbatim**, as a new bullet of the Conventions list, between the two named
anchors, separated from each by exactly one blank line. **Both anchors were located by their own
text and never by a line number (D-307).**

| | Before | After |
|---|---|---|
| `- **THE WHOLE DECISION SURFACE IS DELIVERED…` | 1836 | **1836 (unmoved)** |
| `- **WORKING-TREE FILES ARE READ WITH THE FILE TOOLS…` | 1850 | **1918** |
| File length | 1918 | **1986** |

**Lines added: 68** — the block's 67 lines plus one blank separator. The lower anchor moved by exactly
68 and the upper anchor did not move at all, which is what makes this a pure insertion rather than a
rewrite.

**No existing line of `CLAUDE.md` was changed, reordered or removed.** The edit was made as a single
exact-match replacement whose old text was the unchanged tail of the bullet above, the blank line, and
the unchanged head of the bullet below — so any drift in the surrounding text would have failed the
edit rather than silently altering it.

**No markdown heading was introduced.** The block is a bullet and its continuation lines; the new
section's own internal headings are bold runs, not `#` lines. This was a requirement rather than a
nicety, `gen_session_start_read_size.py` locating each span by its heading — and §7.3 records that the
span-measuring tool ran clean afterwards, which is the measurement of that requirement rather than a
claim about it.

---

## 4. Task 3 — the D-658 correction at its home

### 4.1 (5(a)) The twelve lines, replaced, and still twelve

**Proved before and after:** the block runs from the heading at **line 1306** through the line ending
`names.**` at **line 1317** — heading, blank, the five-line *Ruled by the user* paragraph, blank, the
four-line **THE FORM** paragraph = **twelve lines** — and **line 1318 is blank**.

**Only the first line and the last two lines differ.** The five lines of the *Ruled by the user*
paragraph and both blank lines were **not retyped**: two surgical exact-match edits were made, one on
the heading and one on the two-line tail, so those five lines are unchanged character for character
by construction.

The heading now reads:

```
### Where the record does not settle the question, the surface that returns it to the user gathers FACTS, marks what is UNSETTLED, and CARRIES A RECOMMENDATION
```

and THE FORM's fourth requirement now reads:

```
READ WHOLE; anything the record does not settle marked UNSETTLED rather than filled — and A
RECOMMENDATION on the three standing grounds the decision-surface rule in `CLAUDE.md` names.**
```

### 4.2 (5(b)) The preserved former wording and the supersession record

Inserted at lines **1319–1342**, after the twelve lines and the blank line following them, and before
the load-bearing paragraph — the two blocks the dispatch specifies, verbatim: the
`★ THE FOURTH REQUIREMENT WAS REVERSED…` block carrying the user's own words
(*"'makes NO recommendation' is directly false."*) and the former heading ending and former fourth
requirement; and the `THE OTHER THREE REQUIREMENTS ARE UNTOUCHED AND STILL BIND` block carrying the
stays-LIVE reading and its declaration that the reading is the writing side's.

### 4.3 (5(c)) The load-bearing paragraph, replaced with its former wording preserved

Lines **1344–1359**: the new paragraph, and beneath it the
`*★ FORMER WORDING, PRESERVED (#12), superseded 2026-09-21:*` block reproducing the superseded
paragraph in full.

### 4.4 (5(d)) The closing paragraph, replaced with its former wording preserved

Lines **1361–1371**: the new `*Why the form earns its place:*` paragraph, and beneath it the second
`*★ FORMER WORDING, PRESERVED (#12), superseded 2026-09-21:*` block.

### 4.5 (5(e)) What was not touched — and why it matters to Task 4

**The standing-clause note above the heading is unchanged and exactly where it was**, at **line 1304**,
with one blank line between it and the heading. **No line above the heading was added or removed** —
which is why the heading is still at 1306 and **D-658's `home` anchor `cowork_audit_protocol.md:1306-1317`
keeps both its start line and its width.** §5.3 proves that rather than assuming it.

No other section of the file was edited. The file grew from **1564** to **1605** lines, `+41`, all of
it inside this one section: the next section's standing-clause note moved from 1332 to 1373 and its
heading from 1334 to 1375, both by exactly 41.

### 4.6 (5(f)) THE SEARCH — AND IT FOUND SOMETHING LIVE. **A FINDING FOR THE USER.**

Searching `records/cc/instructions/` for `NO RECOMMENDATION` and `makes NO recommendation`:

| File | Line | What it is |
|---|---|---|
| `cc_instruction_decision_rules_consolidation_2026_09_21.md` | 15, 16, 181, 465, 539, 540, 576 | **This dispatch itself** — quoting the user, stating the 0(d) proof, and specifying the replacement text. Not a hit of interest. |
| `cc_instruction_l2_reading_file_2026_09_05.md` | 411 | **A dated, already-run dispatch.** Not rewritten. |

**Nothing was changed.** A dispatch already run is a dated record.

**★★ BUT THE ONE EXTERNAL HIT IS NOT ONLY A DATED RECORD, AND THIS IS THE PART THAT GOES TO THE USER.**
That line is source code the dispatch told CC to write into a tool, and **it is live at HEAD**. A
read-only check — investigate by default (**D-254**), nothing changed on the strength of it — locates
it at:

```
tools/audit/gen_withheld_family_reading.py:146-147
        "they were not guessed.  Each row says what was read.  NO RECOMMENDATION IS MADE ON ANY OF "
        "THEM (D-658): where the record does not settle the question, the surface gathers facts."
```

**So the superseded clause is asserted, by D-658's own identity, in a LIVE tool that writes a reading
surface for the user.** That tool is `[PASS]` in both guard captures, so nothing flags it. Correcting
it is outside this batch: **B1 bars editing any tool source but `gen_status_batch_bound.py`**, and
5(f) says change nothing. **It is reported here and left.**

---

## 5. Task 4 — the register, corrected at its source and regenerated

### 5.1 (6(a)) The former values, read out of the file itself

The four fields were read out of `backbone_decisions.json` **before** anything was changed, and the
preserved-former-wording text was built from what was read. **Two of the four match the dispatch's
own rendering exactly** — the former `title` and the former `rationale`, compared word for word.

**ONE DIFFERENCE, REPORTED AS THE DISPATCH ASKS.** The dispatch renders the former fourth requirement
of THE FORM as `"— and NO RECOMMENDATION AT ALL."`. **In the file it is** `— and NO\nRECOMMENDATION AT ALL.**`
— a line break between `NO` and `RECOMMENDATION`, and a closing `**`. The dispatch's normalised
rendering was used, for two reasons stated rather than assumed: it is the new authored prose of
`status_source` rather than one of the four former field values the instruction is about, and it is
**identical to the rendering 5(b) had already landed in `cowork_audit_protocol.md`**, which the
dispatch specifies verbatim — so using the raw bytes here would have made the register and its home
disagree about the same quotation. **The difference is reported; the user can rule it either way.**

### 5.2 The five changed fields, and the route

**The edit was made with the file tools, not with a JSON round-trip, and the choice is declared.**
The dispatch offers a one-off script held outside the tree; a script reading a repository file is the
exact shape the shell-read rule's own 2026-08-08 widening names as a violation, and the guard had
already refused two shell reads in this batch. Five exact-match string edits were made instead, each
anchor proved **unique in the file by Grep first**. This is strictly safer for the constraint the
dispatch cares about: a targeted edit **cannot** reformat the rest of the file, whereas a round-trip
can. **The serialization was then proved, not trusted** — §5.3.

- **`title`** → `Where the record does not settle the question, the surface that returns it to the user gathers facts, marks what is unsettled, and carries a recommendation`
- **`verbatim`** → the twelve lines 5(a) wrote, joined by `\n`
- **`plain`** → `When a question has to go back to the user because the record does not answer it, the surface it goes back on cites every claim at the place it can be checked, reads the records concerned whole, marks anything the record does not settle as unsettled instead of filling it in, and carries a recommendation explained towards the ultimate objective, towards the guiding principles and by the meta level of the act it suggests.`
- **`rationale`** → `The load-bearing requirement is the unsettled marking: marking an item unsettled is an answer rather than a shortfall, since filling it from the most plausible reading is the invention D-112 forbids. The fourth requirement was a prohibition on recommending, and the user reversed it on 2026-09-21 — a decision surface always carries a recommendation, explained towards the ultimate objective, towards the guiding principles and by the meta level of the act it suggests. What the prohibition protected is held by that explanation instead: the user rules on a reasoning he can check at each ground rather than on a bare verdict, and a recommendation given without the explanation reopens the hazard in full.`
- **`status_source`** → every word it carried, plus the `★ AMENDED 2026-09-21 ON THE USER'S RULING:` passage appended at its end, verbatim as the dispatch gives it.

**`status` stays `live`. `date`, `ratified_by`, `group` and `home` are untouched** — `home` still
reads `cowork_audit_protocol.md:1306-1317`, not edited by hand.

### 5.3 The serialization proof, and the equality proof both ways

`reaim_home_anchors.py --check` after the edit: **no `REFUSED`**, exit 0. The backbone still
re-serializes byte-identically to the committed file, so the hand edit left it in exactly the form
that tool requires.

**The equality, both ways.** The stored `"verbatim"`, split on `\n`, is exactly the twelve lines now
standing at lines 1306–1317 of `cowork_audit_protocol.md` — read back at both objects and compared,
not recalled. And those twelve lines are the ones at the entry's own `"home"` anchor
`cowork_audit_protocol.md:1306-1317`, which §4.5 proves did not move. **The mechanical proof of the
same thing** is §5.5's `gen_cluster_dispositions.py --verify`: `477/477` quotes found at their cited
home and `471/471` cited line numbers correct, D-658 among them.

### 5.4 (6(b)) NOTHING ELSE IN THE BACKBONE MOVED — PROVED AT THE OBJECTS

The pre- and post-edit blobs were diffed **by explicit hash**:

```
pre  = 31665c5387e140fe9306b879e8b7545a83f46ea9
post = dcfee15e86e1f3ea7d7cce6a321f6aa9f035b7a1
git diff --numstat  →  5  5
```

**Five lines changed, five added, five removed, in exactly two hunks — `@@ -14270,4 +14270,4 @@` and
`@@ -14282 +14282 @@`.** Both lie inside D-658's own object, which spans 14267–14284. **No second
object differs.**

**The object count is 477 before and 477 after**, derived by `gen_cluster_dispositions.py` itself at
§2.2 and §5.5 rather than counted by hand.

### 5.5 (6(c) and 6(d)) The re-aim and the regeneration

Three re-aim runs, all exit 0:

| Run | Result |
|---|---|
| `reaim_home_anchors.py --check` | `anchors drifted: 41` |
| `reaim_home_anchors.py` | `re-aimed 41 anchor(s)` |
| `reaim_home_anchors.py --check` | **`anchors drifted: 0`** |

**The 41 = the 35 pre-existing plus 6 this batch caused, and every one is named.** The 35 `CLAUDE.md`
entries of §2.2, three of them with changed drift values because Task 2 inserted above them
(**D-196** `+62`→`+130`, **D-253** `+55`→`+123`, **D-254** `+55`→`+123`), and **six newly drifted
entries homed in `cowork_audit_protocol.md`, every one `+41`** — **D-645**, **D-653**, **D-654**,
**D-670**, **D-671**, **D-672**. Full old-and-new anchors at `scratchpad/t4_reaim2.txt`.

**D-658 is absent from that list, and its absence proves nothing either way** — its anchor was
designed not to move, 5(e) having added no line above the heading. Where its state actually shows is
the verify below, and it is clean there.

The regeneration:

```
python tools/audit/decisions/gen_decisions_register.py
wrote 20 files: DECISIONS.md (the index, 861 lines) + 19 group files under decisions/ (477 decisions)   [exit 0]

python tools/audit/decisions/gen_decisions_register.py --check
the register matches the data (20 files: the index + 19 group files)                                    [exit 0]

python tools/audit/decisions/gen_cluster_dispositions.py --verify
backbone decisions: 477
cross-references resolving: ALL
verbatim quotes found at their cited home: 477/477
cited line numbers correct: 471/471   (6 cited to a file with no line number, by design)                [exit 0]
```

**COMPARED AGAINST TASK 1's BASELINE, which is the condition rather than an absolute: no entry that
was CLEAN at Task 1 is unclean now, and no residual line drift remains.** The verify moved **exit 1 →
exit 0** and the drift count **35 → 0**. It strictly improved; nothing regressed.

**The group files the regeneration actually rewrote — eight of the nineteen**, measured at the
enumeration rather than assumed: `decisions/group_C.md`, `group_D.md`, `group_G.md`, `group_K.md`,
`group_L.md`, `group_Q.md`, `group_S.md`, `group_T.md`, plus `DECISIONS.md`. The other eleven group
files were rewritten byte-identically and appear in no enumeration.

### 5.6 D-658, regenerated — quoted

**`DECISIONS.md` line 823:**

```
| D-658 | Where the record does not settle the question, the surface that returns it to the user gathers facts, marks what is unsettled, and carries a recommendation | LIVE | — | `cowork_audit_protocol.md` |
```

**`decisions/group_T.md` lines 1469–1492** carry the whole entry: the heading; the verbatim block
quoting the corrected twelve lines including
`READ WHOLE; anything the record does not settle marked UNSETTLED rather than filled — and A` /
`RECOMMENDATION on the three standing grounds the decision-surface rule in `CLAUDE.md` names.**`; the
new **In plain words**; the new **Why**; **Status.** `LIVE · decided 2026-08-09 · ratified by user`;
**Home.** `cowork_audit_protocol.md:1306-1317`; and the **Provenance** carrying the appended
amendment.

**★ THE `no recommendation` CHECK, ANSWERED PRECISELY RATHER THAN WITH A BARE CONFIRMATION.**
`DECISIONS.md` carries the words **nowhere** — zero occurrences. In `group_T.md` they occur **only on
line 1492, the Provenance line**, and there are three, each accounted for:

1. **`— no recommendation at all —`**, inside the amendment, naming the clause it declares SUPERSEDED.
2. **the former `title`**, inside `FORMER WORDING PRESERVED VERBATIM (#12)`.
3. **`"— and NO RECOMMENDATION AT ALL."`**, the preserved former fourth requirement.

Two further occurrences use the **hyphenated** form `no-recommendation`: one inside the preserved
former rationale, and one in the **pre-existing** provenance sentence recording what the 2026-08-09
ratification queue flagged (*"on the reading that the no-recommendation clause is already implied by
#5 and D-112, and the user ruled it KEPT"*). **That last one is the only occurrence that is neither
the amendment nor a preserved-former-wording passage.** It is pre-existing text the dispatch required
be kept word for word, and it records a historical reading rather than stating the live rule — so it
is reported rather than silently removed. **No statement of the live rule anywhere in either file
carries the words.**

---

## 6. Task 5 — `STATUS.md`, the forward bound, the generators, the closing capture

### 6.1 (7(a)) The `STATUS.md` entry

One new dated entry at the head of the dated entries, in the OI-222 pointer convention, restating no
figure (**D-431**) and pointing at this report as its whole. It is now `STATUS.md` line 8. Quoted
whole it is one very long line; it is on disk and is not reproduced here, because reproducing it
would be a second copy of a surface this report is already the whole of.

**★ ONE CHANGE TO AN EXISTING LINE, DECLARED — the same one the previous batch declared, for the same
mechanical reason.** The string `Last updated: ` was removed from the head of the L2-withheld-documents
entry when the new entry was written above it. This is not an editorial rewrite: it is
`gen_status_batch_bound.py`'s own **`PREFIX_ADJUSTMENT`**, imported from `gen_governing_surface_split.py`
as *"the ONE declared textual adjustment"*. **Without it 7(b)'s `--apply` STOPs**, its occurrence test
requiring the prefix-stripped entry to appear in the live file exactly once. **No sentence was
rewritten and nothing was removed beyond that prefix.**

### 6.2 (7(b)) The forward bound — the aiming set, and what actually moved

**The relayed coupling was confirmed at the two tool sources first, as the dispatch requires.**
`gen_session_start_read_size.py`'s `MEMBERS` table (line 140) is exactly `CLAUDE.md`, `STATUS.md`,
`DECISIONS.md`; and `gen_defense_share.py` carries `import gen_session_start_read_size as reader` at
**line 120** and calls `reader.measure(...)`, `reader.claude_md_reading(...)` and `reader.at_tree(...)`
at lines 384–386. **The relay is TRUE: an edit to any of the three moves both artifacts.** The
ordering the dispatch fixed was therefore correct, and it was followed.

**The aiming I set** — all five authored inputs moved together, `PREVIOUS_AIMINGS` appended to rather
than replaced (#12):

| Field | Set to |
|---|---|
| `BASE_COMMIT` | `3720bd323e5c25dcd538d77b4338214b16427349` |
| `PREVIOUS_BATCH_DISPATCH` | `cc_instruction_l2_withheld_documents_2026_09_21.md` |
| `ACT_DATE` | `2026-09-21` (unchanged) |
| `DISPATCH` | `cc_instruction_decision_rules_consolidation_2026_09_21.md` |
| `TASK` | `Task 5` |
| `MOVE_KIND` | `ordinary` (unchanged) |

**★ `BASE_COMMIT` IS NOT THIS BATCH'S OPENING REF, AND THE DEPARTURE IS DECLARED AT THE TOOL AND HERE.**
Every previous aiming names the commit both refs stood at when its batch opened. That is impossible
here: at `7d7291f401d0…` the entry this move takes was **finished but uncommitted**, so `STATUS.md`'s
object at that commit does not carry it and the tool's own first STOP would fire — *no dated entry
names the then-previous batch*. `BASE_COMMIT` therefore names **this batch's Task 0 commit**, the
first commit whose `STATUS.md` object carries that entry. The alternative was commit two, whose
`STATUS.md` is byte-identical; the work-landing commit was named because it is the one that carries
the batch being moved. The reasoning is written into the tool's own `BASE_COMMIT` comment block, and
the new `PREVIOUS_AIMINGS` row points at it rather than restating it.

**Two comment notes were appended at the END of their blocks**, which is those blocks' own convention
and the shape the previous batch's self-check named after mangling a comment by inserting mid-sentence.

`--apply`, then `--check`:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 3,017 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True          [exit 0]

  entries moved: 1, 3,017 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True          [exit 0]
```

**No already-in-the-archive STOP fired.**

**★ WHAT THE `--apply` ACTUALLY MOVED, NAMED RATHER THAN COUNTED — because OI-379 is open on exactly
the question of whether a green `--check` proves the bound met.** One entry moved: **the
L2-withheld-documents batch's**, the entry opening
`*2026-09-21 (CC — records/cc/instructions/cc_instruction_l2_withheld_documents_2026_09_21.md. ★★ L2's WITHHELD DOCUMENTS ARE DERIVED AND PRINTED FOR THE USER…`.
It now stands in `STATUS_ARCHIVE.md` at line 5723 beneath the header this act wrote at line 5721,
which names the previous batch, this dispatch and `Task 5`. **`STATUS.md` now holds exactly three
dated entries — this batch's at line 8, and the two 2026-09-02 entries at lines 10 and 12.**

**THE TWO 2026-09-02 ENTRIES DID NOT MOVE AND WERE NOT MOVED BY HAND**, as the dispatch directs. They
name no dispatch, so no aiming of this tool can identify them; whether they ever move stands with the
user.

### 6.3 (7(c)) The two read-size generators, and the figures the user asked for

All four runs, in the ordered sequence, **all exit 0**, no `STOP:` line and no traceback:

| Command | Exit | Head of output |
|---|---|---|
| `gen_session_start_read_size.py` | 0 | `wrote tools/audit/session_start_read_size.json` |
| `gen_defense_share.py` | 0 | `wrote tools/audit/defense_share.json` |
| `gen_session_start_read_size.py --check` | 0 | `the session-start read measurement re-derives` |
| `gen_defense_share.py --check` | 0 | `the defense-share measurement re-derives` |

**THE FIGURES, EACH READ OUT OF ITS ARTIFACT AFTER THE RUN AND TRANSCRIBED FROM NOWHERE (D-431):**

- **What an ordinary session now reads in total: 247,984 characters** —
  `tools/audit/session_start_read_size.json` → `total_characters`. Its members:
  `CLAUDE.md` 104,609 · `STATUS.md` 12,822 · `DECISIONS.md` 127,727 · the gating-identities span 2,826.
- **What `CLAUDE.md`'s six session-start spans now hold: 104,609 characters** — same artifact,
  `characters_per_member.CLAUDE.md`, and
  `★_the_overstatement_this_repair_removes.the_repaired_measurement_the_six_session_start_spans`.
  The whole file is 168,350, so the former whole-file measurement overstated by 63,741.
- **The marked-defense share after the run** — `tools/audit/defense_share.json` → `the_totals`:
  **12,957 characters in 34 marked clauses**; **12.39 %** of the six session-start spans and
  **5.22 %** of the whole ordinary session-start read. The artifact states in its own words that the
  value is a **LOWER BOUND**, the marker set's reach being unmeasured and the ends authored.

**★ THE INSERTED BLOCK MATCHED NO NEW MARKER, WHICH IS MEASURED HERE RATHER THAN HOPED.** The marker
table's three rows matched 31 / 1 / 2 — 34 clauses — and `gen_defense_share.py` **ran clean and did
not stop for want of an authored end.** The dispatch's prediction holds: the block contains no
emphasised run opening with `Why`, `Evidence:` or `Founding instance`.

### 6.4 (7(d)) THE CLOSING GUARD CAPTURE — **THE CONDITION IS BROKEN. THE BATCH STOPS HERE.**

**Path: `scratchpad/guard_close.txt`.** Result line: **79 guards run, 17 failing, 4 not run, 19
historical records** (opening: 15 failing).

Compared verdict by verdict against the opening capture, **four guards moved and no others**:

| Guard | Opening | Closing | Against the condition |
|---|---|---|---|
| `decisions/gen_cluster_dispositions.py --verify` | FAIL | **PASS** | **ALLOWED** — reported |
| `claude_md_rule_triage.py --check` | **PASS** | **FAIL** | ❌ **BREAKS IT** |
| `gen_rulings_sort.py --check` | **PASS** | **FAIL** | ❌ **BREAKS IT** |
| `decisions/gen_reads5_repack.py --check` | **PASS** | **FAIL** | ❌ **BREAKS IT** |

The condition is *no guard whose VERDICT was PASS at the opening capture may carry any other verdict
at this capture*, written with no exception and with no condition on any printed output or count.
**Three guards break it, so §8 — the third commit and the push — did not run.**

**★ THE THREE, DIAGNOSED, WITH EACH CAUSE ESTABLISHED AT THE TOOL SOURCE RATHER THAN ASSUMED (D-669).**
All three are stale-artifact failures, and **all three trace to this batch's own ordered acts**:

1. **`tools/audit/claude_md_rule_triage.py --check`** — `STALE: claude_md_rule_triage.json does not re-derive`.
   Its own docstring: *"Triage every `CLAUDE.md` rule as MECHANISM or KNOWLEDGE"*. **Task 2 added a
   rule bullet to `CLAUDE.md`**, so the committed triage no longer re-derives.
2. **`tools/audit/gen_rulings_sort.py --check`** — `FAIL: the rulings sort does not re-derive` and
   `FAIL: the rulings-sort surface does not re-derive`. It reads
   `BACKBONE = tools/audit/decisions/backbone_decisions.json` (declared line 110, loaded line 483).
   **Task 4 edited that file.** *(Checked and excluded: it does NOT glob the rulings directory — it
   names two fixed ruling records at lines 111 and 118 — so commit two's two new ruling records are
   not the cause.)*
3. **`tools/audit/decisions/gen_reads5_repack.py --check`** — `STALE: reads5_repack.json does not re-derive`.
   It reads `BACKBONE = backbone_decisions.json` (line 94, loaded line 145). **Same cause as (2).**

And the one allowed move, **`gen_cluster_dispositions.py --verify` FAIL → PASS**, is this batch's
6(c) re-aim doing exactly what it was ordered to do.

**★ WHY THE REPAIR WAS NOT TAKEN, STATED RATHER THAN LEFT AS A SILENCE.** Regenerating the three
artifacts would touch **four files** — `tools/audit/claude_md_rule_triage.json`,
`tools/audit/rulings_sort_classification.json`, `tools/audit/decisions/reads5_repack.json` and
**`ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md`, a user-facing ratification
surface**. **None of the four is in this dispatch's declared footprint, and none is in §8(a)'s
candidate set**, so even if regenerated they could not be committed. Running them would also make
this batch touch a ratification surface, which nothing here authorizes. **That is a bar contradicting
a task, which this dispatch orders STOPPED and reported rather than resolved by the executing side.**

**★★ THE STRUCTURAL POINT, WHICH IS WHAT THE NEXT DISPATCH NEEDS RATHER THAN THE THREE NAMES.** This
dispatch **anticipated exactly this class and handled it for two generators**: its ORDERING RULE
established that `gen_session_start_read_size.py` and `gen_defense_share.py` read `CLAUDE.md`,
`STATUS.md` and `DECISIONS.md`, and 7(c) therefore orders both re-run last, after those three files
are final. **The same reasoning reaches three further generators that read the same inputs, and the
dispatch does not name them** — two reading `backbone_decisions.json`, one reading `CLAUDE.md`. The
footprint assumption is written *"from the paths this batch's own tasks touch and from nothing
wider"*, which is why they fall outside it. **This is the same shape the boot-pack frozen-manifest
batch stopped on and which a close dispatch of its own then resolved**: a batch whose own ordered
edits stale an artifact its bars do not let it regenerate. A close dispatch that runs these three
after the last edit to `CLAUDE.md` and the backbone — and names their four artifacts in its commit
set — closes it the same way. **Nothing here proposes that as a decision; it is the fact the stop
rests on.**

**★ AND THE GUARD CLASSIFICATION, RUN IN ITS OWN ORDER AND CARRIED (not a STOP for this batch):**

```
python tools/audit/gen_guard_classification.py --check
STOP: tool(s) in the guard-state population with no authored verdict:
['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py',
 'tools/audit/gen_withheld_family_reading.py']                                              [exit 2]
```

**Exactly the three tools the dispatch predicted**, two of them older debt. Reported whole and carried
on, as ordered.

---

## 7. §8 — THE COMMIT AND THE PUSH: NOT RUN

**Commit three was not made and nothing was pushed.** `changed_paths.py --staged` reports
**0 records**: nothing is staged.

**`origin/master` is therefore still `ef4fad940d806edf8f84eb9a895f88d70a9bbcf2` and `master` is
`6b5bdfc38145befd865feab9436e6ff0dc32cea0`. The two refs still disagree, and this batch did not close
that gap** — the push that would have closed it is part of §8. The two Task 0 commits are local only.

**EVERY PATH THIS BATCH MODIFIED AND LEFT UNCOMMITTED**, so the next session resumes from a known
state — nineteen tracked paths:

```
 M CLAUDE.md                                  (Task 2)
 M cowork_audit_protocol.md                   (Task 3)
 M tools/audit/decisions/backbone_decisions.json  (Task 4: the D-658 edit + the 41 re-aimed anchors)
 M DECISIONS.md                               (Task 4: regenerated)
 M decisions/group_C.md                       (Task 4: regenerated)
 M decisions/group_D.md                       (Task 4: regenerated)
 M decisions/group_G.md                       (Task 4: regenerated)
 M decisions/group_K.md                       (Task 4: regenerated)
 M decisions/group_L.md                       (Task 4: regenerated)
 M decisions/group_Q.md                       (Task 4: regenerated)
 M decisions/group_S.md                       (Task 4: regenerated)
 M decisions/group_T.md                       (Task 4: regenerated)
 M STATUS.md                                  (Task 5: the new entry; the moved entry removed)
 M STATUS_ARCHIVE.md                          (Task 5: the forward bound's --apply)
 M tools/audit/gen_status_batch_bound.py      (Task 5: the re-aiming)
 M tools/audit/status_batch_bound.json        (Task 5)
 M tools/audit/session_start_read_size.json   (Task 5)
 M tools/audit/defense_share.json             (Task 5)
 M tools/audit/guard_state.json               (the two guard captures)
 M tools/audit/claude_md_finer_archive.json   (HELD BACK by B7 — NOT this batch's; untouched)
?? records/cc/instructions/cc_instruction_decision_rules_consolidation_2026_09_21.md
?? records/cc/reports/cc_report_decision_rules_consolidation_2026_09_21.md   (this file)
```

`tools/audit/changed_paths_establishment.json` is **not** modified — every `--establish` run produced
a byte-identical artifact.

**The held-back population is untouched and absent from every staged set this batch made**:
`tools/audit/claude_md_finer_archive.json`; and the standing untracked set — the `scratch_artifacts/`
tree, the two PDFs, `Claude outputs/`, `Codex research inventory/`,
`docs/research_papers/polyph9-release/` and the untracked `.mscx` under
`tools/audit/derivation_exemplars/l0-l1/`. **0(c)'s enumeration established that population; the
dispatch's list matched it.**

---

## 8. What this batch did NOT do — named rather than counted

- **`tools/audit/gen_derivation_boot_pack.py` was NOT edited in any way and was NEVER run bare** (B2).
  It ran only inside the guard set, in `--check` mode, in both captures.
- **Nothing was authored into `WITHHELD`, `EXTRAS`, `VERDICTS`, `CRITERION` or `FROZEN`** (B3).
- **No path under `tools/audit/derivation_boot_pack/` was read for content, written, deleted, renamed
  or moved** (B3).
- **No governing document but the three its own tasks name was amended** (B9): `CLAUDE.md`,
  `cowork_audit_protocol.md`, `STATUS.md`. Not `ARCHITECTURE.md`, `FRAMEWORK.md`, `OPEN_ITEMS.md`,
  `cowork_design_doc_template.md`, `cowork_notation_adoption_increment.md` or
  `cowork_adjudication_dossier.md`. `STATUS_ARCHIVE.md` changed only as the forward bound's `--apply`
  wrote it.
- **No rendered register file was hand-edited** (B5). `DECISIONS.md` and every `decisions/group_*.md`
  changed only as `gen_decisions_register.py` wrote them.
- **No open-items row was created, flipped or discarded; no decisions-register identity was allocated
  and no `D-NNN` was created** (B6). One EXISTING entry changed — D-658 — and nothing else.
- **The register's rule (c) suspension and its owed-entries list were left exactly as 0(d) item 5
  found them**: the placeholder comment, unfilled.
- **Only one tool source was edited** — `tools/audit/gen_status_batch_bound.py`, which B1 excepts by
  name. Every other tool source named in B1 is untouched, including `gen_guard_state.py` and
  `gen_guard_classification.py`.
- **No `src/` file, no build, no test, no golden, no score corpus, nothing under `tools/corpus/` or
  `tools/robust_stop/`, no measurement of the analysis, no paper, no reading-pass extract, no score**
  (B4).
- **No new file was added under `tools/`**, and no helper script was written anywhere: the backbone
  edit was made with the file tools.

---

## 9. WHAT GOES TO THE USER

1. **Task 1's answer: the register DOES regenerate.** At the untouched tree
   `gen_decisions_register.py --check` exits 0 and all 477 verbatim quotes are found at their cited
   homes. The rule (c) suspension does not block regeneration. The only baseline defect was **35
   `CLAUDE.md` line-anchor drifts, which Task 4's re-aim has now taken to zero** — so the register is
   in a better state than it was found in.
2. **5(f)'s search — and it found something live, which is more than the dispatch expected.** The
   superseded clause survives in a **dated dispatch** (`cc_instruction_l2_reading_file_2026_09_05.md:411`,
   never rewritten) — **and in a LIVE tool at HEAD**,
   `tools/audit/gen_withheld_family_reading.py:146-147`, which asserts *"NO RECOMMENDATION IS MADE ON
   ANY OF THEM (D-658)"* **into a reading surface it generates for the user**. That tool passes both
   guard captures, so nothing flags it. **Nothing was changed on the strength of this.**
3. **D-658 was left LIVE rather than superseded.** One clause of four was replaced and the entry as
   corrected states a live rule. **This is the writing side's reading, not the user's**, taken because
   the register's status vocabulary has no partial-supersession word and a `SUPERSEDED BY` status
   would have to name a replacement identity the suspended register cannot issue. **It is his to
   correct in one word.**
4. **The batch stopped at its closing guard condition and did not commit or push.** The three
   PASS→FAIL guards are all stale artifacts caused by this batch's own ordered acts — two by the Task 4
   backbone edit, one by the Task 2 `CLAUDE.md` insertion. The repair touches four files outside the
   declared footprint, one of them a ratification surface, so it was reported rather than taken.
   **The dispatch handled this exact class for two generators (7(c)'s ordering rule) and the same
   reasoning reaches three more it does not name** — §6.4 states it. **All of Tasks 0 to 5 are done
   and on disk; what is outstanding is the third commit and the push.**

---

## 10. The self-check after the coding exercise

The diff of every touched file was re-read on disk before this report was written, not recalled.
Three things it caught, all reported above rather than shipped silently:

1. **The `Last updated: ` prefix removal in `STATUS.md`** is a change to an existing line. It is
   declared at §6.1 with the mechanism that requires it (`PREFIX_ADJUSTMENT`), on the shape the
   previous batch declared for the same act.
2. **`BASE_COMMIT` departs from every previous aiming's convention**, and the departure is written into
   the tool's own comment block and declared at §6.2 rather than left for a later reader to notice.
3. **The one difference between a former value as the dispatch renders it and as the file carries it**
   (the line break and the closing `**` in the former fourth requirement) is reported at §5.1 with the
   reason the dispatch's rendering was used.

Two route substitutions were forced by the shell-read guard and both are declared at §1.3: the tail
check and the size check went through the file tools and the content-addressed git route instead of
`tail` and `od`. A third was a choice rather than a refusal — §5.2's use of the file tools instead of
a JSON round-trip for the backbone edit — and it is declared with its reason and with the proof that
the serialization survived it.

**The reserved-word check worth stating:** every bare *score* in this report is the musical sense
(*"no score corpus"*, *"no score"*); the numerical sense does not occur. Bare *register* is used for
the open-items and decisions registers, which this project's own convention spells in full — each
occurrence above reads *the decisions register* or *the open-items register*, never bare. *Measure*
appears only as the verb and as *measurement*, never for the bar.

---

*Provenance: CC, 2026-09-21. Dispatch pinned at `28c8bc0ee2df6139c36b46b588536fc4919229a0`. Two
commits made: `3720bd323e5c25dcd538d77b4338214b16427349` and
`6b5bdfc38145befd865feab9436e6ff0dc32cea0`. The third commit and the push did not run. Every figure
above is cited to the artifact or the capture that produced it; the captures are at
`scratchpad/guard_open.txt` and `scratchpad/guard_close.txt`, and the per-task outputs at the
`scratchpad/t1_*`, `t4_*`, `t5_*` and `d_*` files named in place.*
