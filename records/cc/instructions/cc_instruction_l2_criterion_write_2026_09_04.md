# CC INSTRUCTION — write L2's ruled candidate criterion into the generator's committed table (2026-09-04)

> **STATUS: DISPATCH.** Written by the Cowork writing side, 2026-09-04, at tip
> `e03fae855d1cf54fee8103dcef3e7d97adbedf6e` (`refs/heads/master` and `refs/remotes/origin/master`
> both at that hash, read at the two ref files with the file tools immediately before this file was
> written). **Nothing was running when this was written and no other dispatch is out.**
>
> **What it executes.** Five rulings of `cowork_rulings_2026_08_31_decision_surface_sitting.md`
> settled every term of L2's candidate criterion — Ruling 82 (§3ck) the group term, Ruling 86
> (§3co) the keyword list, Ruling 87 (§3cp) and Ruling 88 (§3cq) the home-document list and the
> `ARCHITECTURE.md` passage term, Ruling 89 (§3cr) the one member struck. Every one of those
> sections says in its own words that it does **not** edit the generator, and §3cr states that a
> dispatch writing them into that table **is the next act on the tool**. This is that dispatch.
>
> **The one-sentence statement of the whole job:** put the ruled criterion into
> `tools/audit/gen_derivation_boot_pack.py`, prove at the tool's own matcher that it picks
> 130 + 47 + 67 = 244, and change nothing else.

---

## What this dispatch may NOT do — read before Task 0

- **Author no verdict.** The `VERDICTS` table is not touched, for any subject. No `l2` verdict
  table is created — an empty one would be a claim that the subject has been graded.
- **Withhold nothing.** The `WITHHELD` table is not touched and **no `l2` family is authored**.
  L2's withheld family is ruled list by list at Cowork decision surfaces (Ruling 81, §3cj) and not
  one of those lists exists yet.
- **Render no pack and boot no session.** No file under `tools/audit/derivation_boot_pack/` is
  created, edited, deleted or read for writing, and `tools/audit/derivation_boot_pack.json` is not
  regenerated. `write_all` is never reached: the only mode of the generator you run is `--check`.
- **Do not touch `EXTRAS` or `FROZEN`.** Neither gains an `l2` key. `FROZEN` naming a subject the
  tool does not build is the tool's own STOP 12.
- **DO NOT WIDEN THE EXISTING `KEYWORDS` TUPLE.** It stays exactly the eighteen terms it carries
  today. The reason is mechanical and is the single most important line in this dispatch — see the
  boxed note in Task 1(a). If you find yourself editing the `KEYWORDS` tuple, **STOP** and report.
- **Allocate no `D-NNN`**, create, flip or discard no `OPEN_ITEMS.md` row, and write nothing into
  `DECISIONS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `FRAMEWORK.md`, any ruling record or any other
  governing document, other than the one `STATUS.md` entry Task 5 orders.
- **Take no position on the criterion's content.** Every term below is ruled. You transcribe
  rulings into a table; you do not weigh them, widen them, narrow them or improve them.
- **Recommend nothing.** The report reports.

**STOP conditions, each of which ends the batch with a report and no further task:**

1. The tip at boot is not `e03fae855d1cf54fee8103dcef3e7d97adbedf6e` at **both** ref files — a
   moved tip means something ran that this dispatch does not know about. Read
   `cowork_away_returns.md` before anything else and do not write into the tree.
2. The sanctioned enumeration tool reports a tracked modification other than the one Task 0 names.
3. Any earlier section of `cowork_rulings_2026_08_31_decision_surface_sitting.md` is not at the
   line this dispatch names — the modification is then not additions-only and this dispatch does
   not land it.
4. `python tools/audit/gen_derivation_boot_pack.py --check` does not exit 0 after the edit.
5. Anything under `tools/audit/derivation_boot_pack/` or `tools/audit/derivation_boot_pack.json`
   differs from its committed blob at any point after Task 0.
6. `gen.KEYWORDS` is not the eighteen terms it carries at Task 0.
7. The arithmetic of Task 2(f) does not close at **244 = 130 + 47 + 67**.

---

## Task 0 — land the outstanding work of the Cowork line, and this dispatch

**One commit, four paths, nothing else.**

**(a) One TRACKED modification, additions only:**

```
cowork_rulings_2026_08_31_decision_surface_sitting.md
```

It carries three added sections written by the Cowork session of 2026-09-04 — **§3cp (Ruling 87),
§3cq (Ruling 88) and §3cr (Ruling 89)**.

**Prove additions-only at the object BEFORE committing, and prove it WITH THE FILE TOOLS.**
`Grep` the working-tree file for the pattern `^## (3c[i-r]\.|4\. What this ruling does NOT do)`
with line numbers, and check the eleven positions against this table:

| Anchor | Expected line |
|---|---|
| `## 3ci.` | 5964 |
| `## 3cj.` | 6129 |
| `## 3ck.` | 6226 |
| `## 3cl.` | 6378 |
| `## 3cm.` | 6577 |
| `## 3cn.` | 6740 |
| `## 3co.` | 6902 |
| `## 3cp.` | 7071 |
| `## 3cq.` | 7240 |
| `## 3cr.` | 7383 |
| `## 4. What this ruling does NOT do` | 7508 |

Then `Read` the file at offset 7740 and confirm its **last line is 7746**. The file is
**644,942 bytes** on disk; take that from a directory listing if you have a permitted way to stat
it, and treat it as a secondary confirmation — the eleven positions and the line count are the
proof this dispatch requires.

**★ DO NOT USE A SHELL COMMAND FOR THIS CHECK.** The previous dispatch of this line ordered the
anchor positions taken with `python -c "...open(...)..."`, and your own report of that batch
recorded it as a form the shell-read guard denies (**D-253**). That order is not repeated here:
every read of a working-tree file in this dispatch goes through the file tools. If any task below
tempts you into `wc`, `grep`, `type`, `Get-Content`, `Select-String` or `python -c` on a
repository file, that is a breach — report it rather than absorbing it.

**(b) Two UNTRACKED files of the same line, added as they stand:**

```
cowork_handoff_entry_one_hundred_and_six.md
cowork_handoff_entry_one_hundred_and_seven.md
```

**(c) This dispatch itself:**

```
cc_instruction_l2_criterion_write_2026_09_04.md
```

**The standing untracked `cc_*` population at the repository root is NOT landed** — it is
pre-existing and no dispatch of this line touches it. Enumerate with the sanctioned enumeration
tool rather than with `git status`:

```
cd C:\s\MS && python tools/audit/changed_paths.py --json tools/audit/changed_paths_l2_criterion_task0.json > %TEMP%\cp_task0.txt 2>&1; echo "exit:$?"
```

then read `%TEMP%\cp_task0.txt`. **Expect exactly one tracked modification: the path in (a).** Any
other tracked modification is STOP condition 2. Commit the enumeration artifact with the rest.

Commit message:

```
docs(cowork): land Rulings 87-89, two handoff entries and the L2 criterion-write dispatch

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the commit hash.

---

## Task 1 — the edit

Two insertions into `tools/audit/gen_derivation_boot_pack.py`, and nothing else in that file
changes. Both are pure additions: no existing line is edited, moved or deleted.

### (a) After the `KEYWORDS` tuple, add `L2_KEYWORDS`

The committed file carries, at lines 738–742:

```python
KEYWORDS = (
    "slice", "slicing", "segment", "segmentation", "boundary", "boundaries", "change-point",
    "onset", "release", "harmonic rhythm", "where one chord ends", "finest grain", "grain",
    "atomic", "sounding", "struck", "priority of evidence", "evidence ranking",
)
```

**Leave every one of those lines exactly as it stands.** Insert the block below immediately after
the closing `)` of that tuple and before the blank line preceding `CRITERION = {`.

> ### ★ WHY `KEYWORDS` IS NOT WIDENED, STATED BEFORE THE CODE SO IT CANNOT BE READ AS STYLE
>
> The `harmony-boundary` entry of `CRITERION` carries `"keywords": KEYWORDS` — it reads that
> tuple by name. `harmony-boundary` is in `WITHHELD`, so `build()` derives its candidates on
> **every** run, and it is in `FROZEN`, so its pack directory is pinned at blobs already
> committed. Its `VERDICTS` table is authored for exactly the candidate set those eighteen terms
> produce. Widening the shared tuple to forty-two would hand `harmony-boundary` new candidates
> carrying no authored verdict, and `build_subject` raises a **STOP** on exactly that — *"derived
> candidate(s) carry no authored verdict"*. It would also silently change the derivation of a
> FROZEN subject, which is what the freeze exists to prevent. **L2's forty-two terms therefore go
> in their own tuple. The pilot's eighteen keep one home and are reused, not retyped (#6).**

```python
# ── L2's ruled keyword list — FORTY-TWO TERMS ─────────────────────────────────────────────────
# Ruling 86, §3co of `cowork_rulings_2026_08_31_decision_surface_sitting.md`, in its own words:
# "The pilot's eighteen, unchanged" plus "the twenty-four added for the other three charter
# limbs", and "the six bare words `mode`, `root`, `quality`, `figure`, `applied` and `passing`
# are EXCLUDED" — they must not appear below.
#
# THE EIGHTEEN ARE TAKEN FROM `KEYWORDS` RATHER THAN RETYPED (#6): the ruling says unchanged, and
# a second copy of them would be a second place to change.  `KEYWORDS` ITSELF IS NOT WIDENED —
# `harmony-boundary` reads it, that subject is FROZEN and its verdict table is authored for the
# candidate set the eighteen produce, so widening the shared tuple would derive candidates with
# no verdict and `build_subject` would STOP.
L2_KEYWORDS = KEYWORDS + (
    # the tonality at each moment
    "tonality", "tonic", "local key", "key area", "modulation", "tonicization",
    # which sounding notes belong to the harmony and which elaborate it
    "chord tone", "non-chord", "chord-tone assignment", "elaboration relation",
    "passing tone", "passing note", "neighbour", "neighbor", "suspension", "anticipation",
    "ornament",
    # what chord is read over each span
    "scale degree", "roman numeral", "inversion", "applied chord", "chord quality",
    "figured bass",
    # the charter's own word for what L2 must publish beside its answer
    "rival",
)
```

### (b) Into the `CRITERION` table, add the `l2` entry

The committed table's last entry is `"l0-l1"`, ending at line 780 with `    },`, and the table
closes at line 781 with `}`. **Insert the block below between those two lines** — after `"l0-l1"`'s
closing `},` and before the `}` that closes `CRITERION`. Change no existing entry.

```python
    # ── L2, the next deriving subject under Ruling 10 ─────────────────────────────────────────
    # DORMANT BY DESIGN, AND THE DORMANCY IS DECLARED WITH ITS CONSUMER NAMED (the
    # fact-publication corollary: a fact consumed by no one is declared dormancy or waste).
    # NOTHING REACHES THIS ENTRY TODAY: `build()` iterates `WITHHELD`, and no `l2` withheld
    # family is authored, because L2's family is ruled list by list at Cowork decision surfaces
    # (Ruling 81, §3cj) and no list exists yet.  Its consumer is `build_subject("l2", ...)`, which
    # runs when that family lands — a separate act, not this one.
    #
    # EVERY TERM IS RULED, each cited to the section that ruled it in
    # `cowork_rulings_2026_08_31_decision_surface_sitting.md`:
    #   groups              Ruling 82, §3ck — A, C, D, E, F and G, "the six register groups the
    #                       charter's four limbs and their vocabulary reach".
    #   keywords            Ruling 86, §3co — the forty-two of `L2_KEYWORDS` above.
    #   home_documents      Ruling 87, §3cp — the thirteen documents holding a design-intent entry
    #                       the group and keyword terms do not already reach — PLUS
    #                       `ARCHITECTURE.md`, added by Ruling 88, §3cq: fourteen in all.
    #                       `cowork_layer5_engagement_design.md` is STRUCK by Ruling 89, §3cr,
    #                       its naming refuted at the object, and MUST NOT appear here.
    #   architecture_spans  Ruling 88, §3cq — EMPTY.  The file is named as a document, so no
    #                       passage is named and no anchor is authored.
    #   always              NO RULING OF THAT RECORD NAMES AN IDENTITY FOR THIS SUBJECT, so the
    #                       term is empty.  Said here rather than left to be read off an empty
    #                       tuple, which would not distinguish "none named" from "not yet filled".
    #
    # WHAT THIS TABLE PICKS, and it is the one check that it was written as ruled: over the 244
    # DESIGN-INTENT entries of `tools/audit/rulings_sort_classification.json`'s 411, the group
    # term alone picks 130, the keyword list adds 47 beyond it, and the home-document list adds
    # the remaining 67.  130 + 47 + 67 = 244, and the criterion picks 244 of 244.
    #
    # THE BOUND THAT SURVIVES THAT (#24, D-661): the population is the sort artifact's 411, NOT
    # the decisions register's 477.  Sixty-six register entries are outside it and no term of this
    # criterion can reach them.  Complete is complete relative to that membership and nothing
    # wider.
    "l2": {
        "groups": ("A", "C", "D", "E", "F", "G"),
        "home_documents": (
            "ARCHITECTURE.md",
            "CLAUDE.md",
            "cowork_architecture_review_2026_07.md",
            "cowork_census_full_needs_audit.md",
            "cowork_engage_arc_plan.md",
            "cowork_layer6_grouping_design.md",
            "cowork_notation_output_contract.md",
            "cowork_phrase_boundary_design.md",
            "cowork_progression_schema_design.md",
            "cowork_progression_schema_dictionary.md",
            "cowork_score_census.md",
            "cowork_voiceleading_axis_design.md",
            "docs/llm_integration.md",
            "docs/scoring_model.md",
        ),
        "architecture_spans": (),
        "keywords": L2_KEYWORDS,
        "always": (),
    },
```

### (c) The two things to re-read after the edit, with the file tools

1. The `KEYWORDS` tuple is byte-for-byte what it was — eighteen terms, unchanged.
2. The three existing `CRITERION` entries — `harmony-boundary`, `scoring-model`, `l0-l1` — are
   byte-for-byte what they were.

---

## Task 2 — prove at the tool's own matcher that the table was written as ruled

### (a) Where the script lives

Write it **outside the repository**, at `%TEMP%\l2_criterion_written_check.py`, so nothing
untracked is left in the tree. It writes exactly one file into the tree: the artifact named in
(e).

### (b) What it must not do

It never calls `build()`, `write_all()` or `check_all()`. It imports the module and calls
`candidates()` — the generator's own derivation, so there is no second matcher to disagree with
the first (#6) — and it **injects nothing**: the whole point is that it reads the committed table.

### (c) The script

```python
# READ-ONLY CHECK. Imports the generator and calls its own candidate derivation over the
# COMMITTED criterion table. It injects nothing and it never calls build(), write_all() or
# check_all(), so it writes nothing the generator writes.
import json, os, importlib.util

HERE = r"C:\s\MS\tools\audit"
spec = importlib.util.spec_from_file_location(
    "gen_dbp", os.path.join(HERE, "gen_derivation_boot_pack.py"))
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)          # main() is guarded by __main__, so this renders nothing

PILOT_EIGHTEEN = (
    "slice", "slicing", "segment", "segmentation", "boundary", "boundaries", "change-point",
    "onset", "release", "harmonic rhythm", "where one chord ends", "finest grain", "grain",
    "atomic", "sounding", "struck", "priority of evidence", "evidence ranking",
)
RULED_GROUPS = ("A", "C", "D", "E", "F", "G")
RULED_HOMES = (
    "ARCHITECTURE.md", "CLAUDE.md", "cowork_architecture_review_2026_07.md",
    "cowork_census_full_needs_audit.md", "cowork_engage_arc_plan.md",
    "cowork_layer6_grouping_design.md", "cowork_notation_output_contract.md",
    "cowork_phrase_boundary_design.md", "cowork_progression_schema_design.md",
    "cowork_progression_schema_dictionary.md", "cowork_score_census.md",
    "cowork_voiceleading_axis_design.md", "docs/llm_integration.md", "docs/scoring_model.md",
)
EXCLUDED_BARE_WORDS = ("mode", "root", "quality", "figure", "applied", "passing")

fail = []


def check(name, ok, saw):
    if not ok:
        fail.append({"check": name, "saw": saw})
    return {"check": name, "passed": bool(ok), "saw": saw}


shape = []
# The pilot's tuple is untouched.
shape.append(check("KEYWORDS is still the pilot's eighteen, unchanged",
                   tuple(gen.KEYWORDS) == PILOT_EIGHTEEN, len(gen.KEYWORDS)))
# `harmony-boundary` still reads it.
shape.append(check("harmony-boundary's keywords are still the eighteen",
                   tuple(gen.CRITERION["harmony-boundary"]["keywords"]) == PILOT_EIGHTEEN,
                   len(gen.CRITERION["harmony-boundary"]["keywords"])))
spec_l2 = gen.CRITERION["l2"]
shape.append(check("the l2 group term is A, C, D, E, F, G",
                   tuple(spec_l2["groups"]) == RULED_GROUPS, list(spec_l2["groups"])))
shape.append(check("the l2 keyword list carries forty-two terms",
                   len(spec_l2["keywords"]) == 42, len(spec_l2["keywords"])))
shape.append(check("its first eighteen are the pilot's, in order",
                   tuple(spec_l2["keywords"][:18]) == PILOT_EIGHTEEN,
                   list(spec_l2["keywords"][:18])))
shape.append(check("no term of the list is one of the six excluded bare words",
                   not set(spec_l2["keywords"]) & set(EXCLUDED_BARE_WORDS),
                   sorted(set(spec_l2["keywords"]) & set(EXCLUDED_BARE_WORDS))))
shape.append(check("the l2 home-document list is the ruled fourteen",
                   tuple(spec_l2["home_documents"]) == RULED_HOMES,
                   list(spec_l2["home_documents"])))
shape.append(check("cowork_layer5_engagement_design.md is not a member (Ruling 89)",
                   "cowork_layer5_engagement_design.md" not in spec_l2["home_documents"], None))
shape.append(check("the l2 ARCHITECTURE.md passage term is empty (Ruling 88)",
                   tuple(spec_l2["architecture_spans"]) == (), list(spec_l2["architecture_spans"])))
shape.append(check("the l2 named-identity term is empty",
                   tuple(spec_l2["always"]) == (), list(spec_l2["always"])))
# Nothing was added to the tables this dispatch may not touch.
shape.append(check("no l2 withheld family was authored", "l2" not in gen.WITHHELD, None))
shape.append(check("no l2 verdict table was authored", "l2" not in gen.VERDICTS, None))
shape.append(check("no l2 extras list was authored", "l2" not in gen.EXTRAS, None))
shape.append(check("no l2 freeze was authored", "l2" not in gen.FROZEN, None))

sort = gen.read_json(gen.SORT)
bb_data = gen.read_json(gen.BACKBONE)
backbone = {d["id"]: d for d in bb_data.get("decisions", [])}
for r in bb_data.get("retired_entries", {}).get("entries", []):
    e = r.get("the_entry", {})
    if e.get("id") and e["id"] not in backbone:
        backbone[e["id"]] = e

design_intent = [e for e in sort["entries"] if e.get("proposed_class") == "DESIGN-INTENT"]
cands = gen.candidates("l2", design_intent, backbone)


def by(crit):
    return {c["id"] for c in cands if any(w["criterion"] == crit for w in c["matched_by"])}


G = by("group")
K = by("keyword") - G
H = by("home-document") - G - by("keyword")
SPAN = by("home-inside-an-oracle-span")
NAMED = by("named-by-the-ruling")
ALL = {c["id"] for c in cands}

arith = []
arith.append(check("the design-intent population is 244", len(design_intent) == 244,
                   len(design_intent)))
arith.append(check("the group term alone picks 130", len(G) == 130, len(G)))
arith.append(check("the keyword list adds 47 beyond the group term", len(K) == 47, len(K)))
arith.append(check("the home-document list adds the remaining 67", len(H) == 67, len(H)))
arith.append(check("130 + 47 + 67 = 244", len(G) + len(K) + len(H) == 244,
                   len(G) + len(K) + len(H)))
arith.append(check("the criterion picks 244 of 244", len(ALL) == len(design_intent) == 244,
                   len(ALL)))
arith.append(check("the three parts partition the candidates with none left over",
                   G | K | H == ALL, len(ALL - (G | K | H))))
arith.append(check("no candidate is picked by an ARCHITECTURE.md passage (the term is empty)",
                   not SPAN, sorted(SPAN)))
arith.append(check("no candidate is picked by a named identity (the term is empty)",
                   not NAMED, sorted(NAMED)))


def ids(s):
    return sorted(s, key=lambda i: int(i.split("-")[1]))


homes = {}
for c in cands:
    if c["id"] in H:
        for w in c["matched_by"]:
            if w["criterion"] == "home-document":
                homes.setdefault(w["matched"], []).append(c["id"])

# Each of the fourteen ruled prefixes is distinct and none is a prefix of another, so an entry
# reached by the home-document term is attributed to exactly one document. Checked rather than
# assumed: if the per-document counts sum above 67, some entry was attributed twice.
arith.append(check("the per-document counts of the sixty-seven sum to 67",
                   sum(len(v) for v in homes.values()) == 67,
                   sum(len(v) for v in homes.values())))

result = {
    "what_this_is": (
        "THE CHECK THAT L2's RULED CANDIDATE CRITERION WAS WRITTEN INTO THE GENERATOR AS RULED. "
        "It reads the COMMITTED criterion table and calls the generator's own candidates() over "
        "it. It authors no verdict, withholds nothing, renders no pack and boots no session."),
    "the_rulings_it_checks": [
        "Ruling 82, section 3ck of cowork_rulings_2026_08_31_decision_surface_sitting.md - the "
        "group term at register groups A, C, D, E, F and G.",
        "Ruling 86, section 3co - the keyword list at forty-two terms, the six bare words "
        "excluded.",
        "Ruling 87, section 3cp - the home-document list at thirteen documents.",
        "Ruling 88, section 3cq - ARCHITECTURE.md added as a home document, fourteen in all, and "
        "the passage term EMPTY.",
        "Ruling 89, section 3cr - cowork_layer5_engagement_design.md struck.",
    ],
    "how_it_was_derived": (
        "The generator's own candidates() function over the committed CRITERION table, with "
        "nothing injected. No second matcher exists to disagree with the first (#6)."),
    "the_shape_of_the_table": shape,
    "the_arithmetic": arith,
    "the_counts": {
        "design_intent_class": len(design_intent),
        "sort_entries_total": len(sort["entries"]),
        "candidates": len(ALL),
        "picked_by_the_group_term": len(G),
        "added_by_the_keyword_list": len(K),
        "added_by_the_home_document_list": len(H),
    },
    "the_sixty_seven_by_home_document": {
        k: {"count": len(v), "ids": ids(set(v))} for k, v in sorted(homes.items())},
    "the_bound_on_this_check": (
        "It establishes that the table matches the rulings and that the tool's own matcher picks "
        "the ruled population. It establishes NOTHING about any entry's verdict: a candidate "
        "carries an authored verdict and a candidate ruled OUT is still rendered into the pack, "
        "and no verdict for this subject exists. And the population is the sort artifact's 411, "
        "not the decisions register's 477 - sixty-six register entries lie outside the "
        "criterion's reach and no term of it can reach them (#24, D-661)."),
    "a_defect_of_the_generator_found_by_writing_this_criterion_and_NOT_repaired_here": (
        "candidates() glosses every group match with the hardcoded string 'Layer 2 - the "
        "slicer', which is true only of register group E. Under the l2 criterion's six groups "
        "that gloss is false for A, C, D, F and G. It is INERT today - build() iterates WITHHELD, "
        "l2 has no withheld family, so no manifest or pack renders it, and this artifact does not "
        "copy it. It must be repaired before an l2 pack is ever built. This dispatch does not "
        "repair it: it writes the criterion and nothing else."),
}

out = os.path.join(HERE, "l2_criterion_written_check.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump(result, fh, indent=1, ensure_ascii=False)
    fh.write("\n")

for row in shape + arith:
    print(("PASS " if row["passed"] else "FAIL ") + row["check"] + f"   saw={row['saw']!r}")
print("wrote", out)
print("FAILED CHECKS:", len(fail))
```

### (d) The exact commands

```
cd C:\s\MS && python %TEMP%\l2_criterion_written_check.py > %TEMP%\l2_crit_out.txt 2>&1; echo "exit:$?"
```

then read `%TEMP%\l2_crit_out.txt`. **Rule 2 of the bash-command rules applies** — the run is
redirected to a file and read separately. **Do not paste the artifact's contents into the report;
cite it (D-431).**

### (e) The artifact

```
tools/audit/l2_criterion_written_check.json
```

New, generated, and the ONE home of every figure this check produces.

### (f) What must hold

**`FAILED CHECKS: 0`.** Every shape check and every arithmetic check passes, and in particular:

- the design-intent population is **244**;
- the group term alone picks **130**;
- the keyword list adds **47** beyond it;
- the home-document list adds the remaining **67**;
- **130 + 47 + 67 = 244**, and the criterion picks **244 of 244**.

**Any failure is STOP condition 7.** A run that does not reproduce 244 means the table was not
written as ruled — do not adjust the criterion to make the number come out. Report the failure
with the checks that failed and stop.

---

## Task 3 — prove nothing else moved

**(a) The generator renders exactly what it rendered before.**

```
cd C:\s\MS && python tools/audit/gen_derivation_boot_pack.py --check > %TEMP%\dbp_check.txt 2>&1; echo "exit:$?"
```

**Expect exit 0.** Exit 1 is drift and exit 2 is a STOP; either is STOP condition 4. This is the
strongest single proof the edit is inert: the `l2` entry is reached by nothing, so every rendered
byte for the three built subjects must be identical.

**(b) Nothing under the pack directory or its manifest moved.** Enumerate:

```
cd C:\s\MS && python tools/audit/changed_paths.py --json tools/audit/changed_paths_l2_criterion_task3.json > %TEMP%\cp_task3.txt 2>&1; echo "exit:$?"
```

**Expect exactly one tracked modification — `tools/audit/gen_derivation_boot_pack.py` — and two
untracked additions: `tools/audit/l2_criterion_written_check.json` and the Task 3(b) enumeration
artifact.** Anything under `tools/audit/derivation_boot_pack/` or
`tools/audit/derivation_boot_pack.json` appearing as modified is STOP condition 5.

**(c) The standing guard set.**

```
cd C:\s\MS && python tools/audit/gen_guard_state.py --check > %TEMP%\guard_check.txt 2>&1; echo "exit:$?"
```

**If it exits 0, say so and carry on.** **If it reports drift, DO NOT REGENERATE** — regenerating
a guard artifact is not "the criterion and nothing else". Record the drift in full in the report
as an owed act, name it in the `STATUS.md` entry, and carry on to Task 4 so the batch closes
FINISHED rather than mid-flight. This dispatch does not know whether that artifact pins this
generator's content; that is why the instruction is to measure and report rather than to predict.

Commit the edit, the check artifact and both enumeration artifacts together:

```
feat(audit): write L2's ruled candidate criterion into the boot-pack generator

Rulings 82, 86, 87, 88 and 89 of
cowork_rulings_2026_08_31_decision_surface_sitting.md. The criterion is dormant
until L2's withheld family is ruled; no verdict authored, nothing withheld, no
pack rendered.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the commit hash.

---

## Task 4 — the report

Write `cc_report_l2_criterion_write_2026_09_04.md` at the repository root, untracked, and commit it
in Task 5's commit. It carries, in this order:

1. **The tip at boot and the tip at close**, each read at both ref files with the file tools.
2. **Task 0's result** — the commit hash, the eleven anchor positions found, the line count found,
   and the enumeration showing exactly one tracked modification before the commit.
3. **The edit, described as what it is**: two pure insertions, no existing line touched, and the
   two re-reads of Task 1(c) with what they showed.
4. **Every check of Task 2**, each stated as passed or failed with its own numbers, and the
   arithmetic `130 + 47 + 67 = 244` stated as the identity it is.
5. **Task 3's three results** — the `--check` exit code, the enumeration, and the guard set.
6. **The generator defect the check artifact records** — the hardcoded group gloss — stated as
   found, inert, unrepaired and owed.
7. **Any STOP reached**, in full, with what was and was not done.
8. **A declared-departures section** — anything you did that this dispatch does not order, stated
   rather than absorbed, including any shell command that read a repository file.

**Recommend nothing.**

---

## Task 5 — `STATUS.md` and close

Add ONE dated entry at the head of `STATUS.md`'s entry list, in the established form, recording:
that L2's ruled criterion is now in the generator's committed table; that the entry is dormant
until a withheld family is authored; that no verdict was authored, nothing withheld, no pack
rendered, no pack directory or manifest touched, and no register identity allocated; that the
existing `KEYWORDS` tuple is unchanged; and the guard-set result. **Per the OI-222 pointer
convention this entry is a POINTER and no figure is restated in it (D-431).**

Commit `STATUS.md` and the Task 4 report together:

```
docs(status): record the L2 criterion write

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Then write the close section into `cowork_away_returns.md` in the established form, and one
further commit carrying the end-state guard artifact, so that the batch reads as FINISHED rather
than mid-flight.

---

## Two authored choices this dispatch makes that no ruling fixes

Stated here rather than buried in the code, because a later reader must be able to see that they
were chosen and by whom.

1. **The subject key is `l2`.** No ruling of the record names a key for this subject. The three
   keys the table already carries are `harmony-boundary`, `scoring-model` and `l0-l1`, and the
   record's own name for this subject, throughout, is L2. The key follows the `l0-l1` shape and
   invents no new name. **It is the writing side's choice and not a ruling**, and it is cheap to
   change while the entry is dormant.

2. **The named-identity term is empty.** Ruling 81 (§3cj) fixed that L2's pack carries a withheld
   family and explicitly did not fix the criterion's content; Rulings 82, 86, 87, 88 and 89 fixed
   four terms and none of them names an identity. The pilot's `("D-057",)` rests on an amendment of
   the 2026-08-22 pilot sitting, which is about the pilot's family and not L2's. **So the record
   names none, and the term is empty because nothing fills it** — not because it was left blank.

---

## The writing side's self-check, run before this dispatch was released (D-434)

Read against `CLAUDE.md`'s guiding principles and conventions:

- **#6 (one path per concern).** The pilot's eighteen keywords keep one home and are reused rather
  than retyped; the check calls the generator's own `candidates()` rather than reimplementing the
  match.
- **#13 (surface a surprise as a STOP before building around it).** Two surprises were found while
  writing this dispatch and neither is built around: the shared-`KEYWORDS` trap, which is why the
  forty-two terms go in their own tuple, and the hardcoded group gloss in `candidates()`, which is
  recorded as found, inert and unrepaired.
- **#19 (nothing unestablished is trusted).** The check establishes that the table matches the
  rulings; it claims nothing about any verdict, and the artifact carries that bound in its own
  words.
- **#24 / D-661.** The population bound — 411 and not 477, sixty-six register entries out of reach
  — is written into the generator's comment and into the artifact, at both places a later reader
  meets the criterion.
- **#17f / D-431.** Every figure lands in the generated artifact and is cited, never transcribed
  into the report or into `STATUS.md`.
- **D-249.** This dispatch puts no question to the user and takes no position on any ruled term.
- **D-253, the working-tree read rule.** The writing side read every object for this dispatch —
  the sitting record's §3cj, §3ck, §3co, §3cp, §3cq and §3cr; the generator at its `KEYWORDS`
  tuple, its `CRITERION`, `WITHHELD`, `VERDICTS` and `FROZEN` tables, at `candidates()`,
  `architecture_spans()`, `build()`, `build_subject()` and `main()`; the keyword measurement
  artifact; `DECISIONS.md`; `STATUS.md`; the derived gating answer; and both ref files — through
  the file tools on bridge-staged snapshots. **Two departures are declared rather than absorbed:**
  two reads of a container copy of `tools/audit/nongating_apparatus_rows.json` went through a
  shell (`python`), which is the same breach this dispatch warns the executing side against, and
  every figure taken from that file was re-established with the file tools afterwards. And this
  dispatch **removes** the shell-read form the previous dispatch ordered for its anchor check.
- **The reserved-word convention.** *Measurement tool*, *check*, *script*, *the open-items
  register* are used; *instrument* is not; bare *score* and bare *key* do not appear in a
  non-musical sense.

*Provenance: Cowork writing side, 2026-09-04, at tip `e03fae855d1cf54fee8103dcef3e7d97adbedf6e`,
after the ordinary session-start read in full — `CLAUDE.md` whole, `DECISIONS.md` whole,
`STATUS.md`, and the derived gating answer (218 gating of 243 open rows). Every term written into
the table above is quoted from the ruling that fixed it; the two authored choices are named in
their own section and are the writing side's, not the user's.*
