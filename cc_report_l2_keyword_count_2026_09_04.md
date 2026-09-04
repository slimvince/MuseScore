# CC report — THE READ-ONLY KEYWORD COUNT OWED BEFORE L2's KEYWORD LIST IS RULED

**Dispatch:** `cc_instruction_l2_keyword_count_2026_09_04.md`, performed 2026-09-04.

**This report RECOMMENDS NOTHING**, exactly as the dispatch orders. No verdict was authored, no pack
was rendered, no pack directory or manifest was touched, no register identity was allocated, and no
position is taken here on which keywords should be in L2's list. The list is the user's to rule at a
Cowork decision surface.

**★ THE ARTIFACT IS THE ONE HOME OF EVERY FIGURE THIS MEASUREMENT PRODUCED (D-431).**
`tools/audit/l2_keyword_count_measurement.json` carries the three lists verbatim, the per-word table
for every one of LIST_B's members, both marginal populations with each entry's matched text in its
own context, and the measurement's own stated bound. The figures below are the ones Task 2 names by
name and no others; everything else is cited, never transcribed.

---

## 1. The tip at boot and the tip at close

Both read at **both** ref files with the file tools — `.git/refs/heads/master` and
`.git/refs/remotes/origin/master`.

| | `refs/heads/master` | `refs/remotes/origin/master` |
|---|---|---|
| **at boot** | `5922a1f5bc62073681ed4187b5e71bb14e302954` | `5922a1f5bc62073681ed4187b5e71bb14e302954` |
| **at close** | `425c9a12b3a6de5f1e2efba6444e2c9459cb0627` | `425c9a12b3a6de5f1e2efba6444e2c9459cb0627` |

The boot tip is the one the dispatch declares, so **STOP condition 1 did not fire**.

| Act | Commit |
|---|---|
| the tree met | `5922a1f5bc62073681ed4187b5e71bb14e302954` |
| Task 0 | `bd6ccb722be3700d31b5f5a195e4c9b294c82280` |
| Task 1 | `425c9a12b3a6de5f1e2efba6444e2c9459cb0627` |
| the close | the commit carrying this report |
| the end state | the one further commit, which the close does not assert |

---

## 2. Task 0's result

**Commit `bd6ccb722be3700d31b5f5a195e4c9b294c82280`, pushed.** Six paths — the enumerated
`(a) + (b) + (c)` set, which is one tracked modification, four untracked handoff entries and the
dispatch itself. (Task 0's heading says *five paths*; its own enumeration names six. See §8.)

### The seven anchor positions found

Every one is exactly the position the dispatch declares, in the order it declares them.

| Anchor | Expected | Found |
|---|---|---|
| `## 3ci.` | 5964 | **5964** |
| `## 3cj.` | 6129 | **6129** |
| `## 3ck.` | 6226 | **6226** |
| `## 3cl.` | 6378 | **6378** |
| `## 3cm.` | 6577 | **6577** |
| `## 3cn.` | 6740 | **6740** |
| `## 4. What this ruling does NOT do` | 6902 | **6902** |

No earlier section moved, so the modification is additions-only and this dispatch may land it.

### The byte size found

**598,937 bytes** — the size the dispatch declares. Taken at the OBJECT: the staged blob hash is
`b093a8a7c7995cd408b6d0ab659ebcbee1f8a778`, and `git cat-file -s` on that explicit hash returns
598937.

**Additions-only was additionally proven at the objects, which the anchor positions alone do not
prove.** `git diff --numstat` between the HEAD blob `717c8083783748704f3372ea3beeabfefabbb381` and
the staged blob `b093a8a7c7995cd408b6d0ab659ebcbee1f8a778` returns **773 added lines and 0 deleted
lines**.

### The enumeration before the commit

`tools/audit/changed_paths.py` over the working tree reported **853 records**, of which **exactly
one is a tracked modification** — ` M cowork_rulings_2026_08_31_decision_surface_sitting.md`, the
path Task 0(a) names — and every other record is untracked (`??`). The four
`cowork_handoff_entry_one_hundred_and_{two,three,four,five}.md` files were present as untracked
additions; the standing untracked `cc_*` population at the repository root was met and correctly not
landed. **STOP condition 2 did not fire.**

The staged enumeration before the commit, and the `--commit` enumeration after it, each reported the
same six paths and nothing else.

---

## 3. The three counts

The population is the **DESIGN-INTENT class of the rulings sort**, and the group term is the one
Ruling 82 (§3ck) fixed — register groups **A, C, D, E, F, G**. The home-document and
`ARCHITECTURE.md` passage terms are **empty in every criterion measured**, their members not being
ruled, so each count is a count for the criterion *as far as it is ruled*.

| | keywords alone | with the group term | added beyond the group term |
|---|---|---|---|
| **the group term alone** | — | **130** | — |
| **LIST P** — the pilot's own eighteen | 73 | **161** | **31** |
| **LIST W** — widened to all four charter limbs | 109 | **177** | **47** |
| **LIST B** — LIST W plus the six bare words | 157 | **201** | **71** |

Design-intent class: **244**.

---

## 4. The five keywords of LIST_B with the largest `of_those_OUTSIDE_the_six_groups`

This is the column the dispatch names as the one the decision turns on: how many design-intent
entries a word reaches that the ruled group term does not already reach.

| Rank | Keyword | Entries outside the six groups | Which list it belongs to |
|---|---|---|---|
| 1 | `mode` | **19** | LIST B only — one of the six bare words |
| 2= | `boundary` | **13** | LIST P — the pilot's eighteen |
| 2= | `applied` | **13** | LIST B only — one of the six bare words |
| 4 | `tonic` | **9** | LIST W — added for the tonality limb |
| 5 | `slice` | **8** | LIST P — the pilot's eighteen |

`boundary` and `applied` are tied at 13. The sixth and seventh places are `tonality` and `root` at 7
each, so the fifth place is not itself a tie. Every other per-word figure is in the artifact.

---

## 5. The entries LIST_B adds that LIST_W does not

**24 entries** (71 − 47). Each is named with the word or words that matched it; the matched text in
its own context is in the artifact, one record per match.

| Identity | Group | Matched by |
|---|---|---|
| D-180 | S | `figure` |
| D-182 | S | `figure` |
| D-206 | S | `mode` |
| D-222 | U | `quality`, `applied` |
| D-223 | U | `applied` |
| D-229 | I | `mode` |
| D-389 | H | `mode`, `quality` |
| D-393 | H | `applied` |
| D-406 | M | `root` |
| D-421 | M | `applied` |
| D-440 | N | `mode` |
| D-441 | N | `mode` |
| D-442 | N | `mode` |
| D-443 | N | `mode` |
| D-444 | N | `mode` |
| D-447 | N | `mode` |
| D-448 | N | `mode` |
| D-470 | I | `applied` |
| D-471 | J | `applied` |
| D-492 | H | `mode` |
| D-503 | M | `mode` |
| D-509 | M | `root`, `quality` |
| D-542 | M | `applied` |
| D-544 | M | `mode` |

---

## 6. Every check of Task 1(f)

| Check | Result |
|---|---|
| **1.** `the_population.design_intent_class` is 244 | **PASSED** — 244. |
| **2.** for each list, `with_the_group_term` = `group_term_alone + added_beyond_the_group_term` | **PASSED** — LIST P: 130 + 31 = 161. LIST W: 130 + 47 = 177. LIST B: 130 + 71 = 201. All three close. |
| **3.** `LIST_P.added` ≤ `LIST_W.added` ≤ `LIST_B.added` | **PASSED** — 31 ≤ 47 ≤ 71. |
| **4.** every id in `what_LIST_W_adds_beyond_the_group_term` carries ≥ 1 `matched_by` record whose `criterion` is `keyword` and whose `in_context` shows the matched text | **PASSED** — measured at the artifact: the section carries **47** `id` records, and between each `id` line and the next there is at least one `in_context` line. Every `matched_by` record in that section is a keyword record, `marginal()` admitting no other kind. |

A fifth identity closes beside them and is reported although it is not one of the four asked for: the
two marginal populations carry **71** `id` records between them — 47 and 24 — which is exactly
`LIST_B.added_beyond_the_group_term`.

### Task 1(g) — nothing else moved

After the run, `tools/audit/changed_paths.py` over the working tree reported **848 records, every one
of them untracked (`??`) and therefore ZERO tracked modifications**, with exactly one addition
against the pre-run enumeration: `tools/audit/l2_keyword_count_measurement.json`. **Nothing under
`tools/audit/derivation_boot_pack/` and not `tools/audit/derivation_boot_pack.json` appears in the
enumeration at all**, so both are unchanged against the commit and **STOP condition 5 did not fire**.
The record arithmetic closes: 853 − 6 landed + 1 written = 848.

The artifact was then committed **alone**, `425c9a12b3a6de5f1e2efba6444e2c9459cb0627`, whose
`--commit` enumeration reports one path, and pushed.

---

## 7. STOPs reached

**None.** All five of the dispatch's STOP conditions were tested and none fired:

1. the tip at boot was `5922a1f5bc62073681ed4187b5e71bb14e302954` at both ref files;
2. the sanctioned enumeration tool reported exactly the one tracked modification Task 0 names;
3. importing the generator module raised nothing, and `gen.candidates(...)` raised nothing for any of
   the four criteria — the run exited 0;
4. the measurement's arithmetic closes at all four checks of Task 1(f);
5. nothing under `tools/audit/derivation_boot_pack/` or `tools/audit/derivation_boot_pack.json`
   differed at any point after Task 0.

Nothing the dispatch forbids was done: the `VERDICTS` table was not touched, `write_all`, `build`,
`--check` and `--subject` were not run, no file under `tools/audit/derivation_boot_pack/` was
created, edited, deleted or read for writing, `tools/audit/derivation_boot_pack.json` was not
regenerated, **not one line of `tools/audit/gen_derivation_boot_pack.py` was edited**, no `D-NNN` was
allocated, no `OPEN_ITEMS.md` row was created, flipped or discarded, and nothing was written into
`DECISIONS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `FRAMEWORK.md` or any ruling record.

---

## 8. Declared departures — stated rather than absorbed

**(a) Task 0(a)'s exact command could not be run, and the same facts were established by the routes
the standing rules require.** The command the dispatch gives is a `python -c` code string carrying a
literal repository path. The shell-read guard **denied** that form when it was attempted this session,
and the working-tree read rule it enforces — `CLAUDE.md` Conventions, register entry **D-253**, as
widened on 2026-08-08 to cover interpreter code — is what denies it. The seven anchor positions were
therefore taken with the **Grep file tool** over the same file, which is the route that rule names.
Every position matched.

**(b) The byte size was taken at the object rather than at the working-tree file**, for the same
reason: `git cat-file -s` on the staged blob's explicit hash, which is a content-addressed read the
rule admits in terms. It returns the declared 598,937. Because that route reads the staged blob and
not the working tree, **additions-only was proven a second way** — 773 added, 0 deleted between the
two explicit blob hashes — so the claim rests on a measurement and not on the anchor table alone.

**(c) Task 0's heading and Task 0's enumeration disagree on the path count.** The heading says *"One
commit, five paths"*; (a) names one path, (b) names four and (c) names one, which is six. The six
**enumerated** paths were committed, the enumeration being what names actual files. Nothing was added
to or withheld from that set.

**(d) The report carries figures, on a reading of two clauses that pull against each other.** Task
1(e) says no figure from the artifact is transcribed into any other document; Task 2 items 3, 4 and 5
order this report to carry the three counts, the five keywords *"named with their numbers"*, and the
entries *"by identity, with the word that matched each"*. The reading taken: Task 2 is the specific
and later instruction about this report's content, so the report carries **exactly the figures Task 2
names by name and no others**, cites the artifact as their one home, and the `STATUS.md` entry
restates none of them (Task 3 orders it a pointer).

**(e) One observation of fact is reported, and it is not a recommendation.** Several of the per-word
figures are driven by **substring matches inside longer words**, visible in the artifact's own
`in_context` fields: `tonic` matches inside *Diatonic-functional* (D-131); `mode` matches inside
*model* throughout group N, which is why seven of that group's language-model entries appear in
§5; and `applied` matches the ordinary non-musical *"was applied"* (D-222, D-223, D-421, D-470,
D-471). This is a **known and documented property of the matcher, not a surprise** (#13): the keyword
branch of `candidates()` in `tools/audit/gen_derivation_boot_pack.py` carries a comment saying in
terms that a keyword can match inside a longer word, and it emits `in_context` for exactly that
reason. It is stated because it bears on how §4's column is read. **No position is taken on what
should follow from it.**

**(f) The ordinary session-start read was performed in full before the dispatch was acted on** —
`STATUS.md`, the `DECISIONS.md` INDEX, and the derived gating answer at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`. This is not
a departure but the standing convention ratified 2026-08-29 (Ruling 5, the framework phase
retrospective, P-1), and it is recorded here so that the record shows it was done.

**(g) `STATUS.md`'s continuous-pruning bound was NOT maintained by this batch, and the reason is the
dispatch's own scope clause.** That file's archive pointer states the bound as *"this file keeps only
the latest batch's entries"*, maintained forward at every batch close. Moving the previous batch's
entries out would be writing into `STATUS.md` beyond the one entry Task 3 orders, which this
dispatch's *What this dispatch may NOT do* section forbids in terms. **The file already carried two
batches' entries on arrival** — the 2026-09-04 boot-pack freeze and the 2026-09-02 comparison batch —
so the bound was already unmaintained before this batch and this batch neither repaired nor worsened
it beyond adding its own entry. The only edit made beside the new entry is the removal of the
`Last updated:` prefix from the entry that was previously at the head, without which the file would
carry two such markers; the entry's text itself is untouched apart from *this batch's close* becoming
*that batch's close*, which the new head makes true.

**Nothing else.** No `src/` change, no golden, no test changed, moved or run, no build, no
measurement of the analysis, nothing under `tools/corpus/` or `tools/robust_stop/`. The measuring
script was written **outside the repository**, at `%TEMP%\l2_keyword_count.py`, exactly as Task 1(c)
orders, so nothing untracked was left in the tree beyond the artifact itself.

---

*Provenance: CC, 2026-09-04, at boot tip `5922a1f5bc62073681ed4187b5e71bb14e302954`, under
`cc_instruction_l2_keyword_count_2026_09_04.md`, which executes the measurement Ruling 83 (§3cl of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`) declared owed before L2's keyword list is
ruled. The three candidate keyword lists are the writing side's authored measurement inputs and are
not a ruling.*
