# CC INSTRUCTION — the read-only keyword count owed before L2's keyword list is ruled (2026-09-04)

> **STATUS: DISPATCH.** Written by the Cowork writing side, 2026-09-04, at tip
> `5922a1f5bc62073681ed4187b5e71bb14e302954` (`refs/heads/master` and `refs/remotes/origin/master`
> both at that hash, read at the two ref files with the file tools immediately before this file was
> written). **Nothing was running when this was written.**
>
> **What it executes.** Ruling 83 (§3cl of `cowork_rulings_2026_08_31_decision_surface_sitting.md`)
> ruled that L2's candidate criterion widens its keyword list to all four limbs of the L2 charter,
> and stated in its own *What this ruling does NOT do* section: *"IT DOES NOT MEASURE WHAT THE
> WIDENED KEYWORD LIST COSTS, AND THAT IS OWED BEFORE THE KEYWORD LIST IS RULED."* **This dispatch
> takes that measurement and nothing else.**
>
> **The one-sentence statement of the whole job:** measure how many candidates three different
> keyword lists produce for L2, publish the numbers as a generated artifact, and change nothing else.

---

## What this dispatch may NOT do — read before Task 0

- **Author no verdict.** The verdict table `VERDICTS` in `tools/audit/gen_derivation_boot_pack.py`
  is not touched, for any subject.
- **Withhold nothing, render no pack, boot no session.** `write_all`, `build`, `--check` and
  `--subject` are NOT run. No file under `tools/audit/derivation_boot_pack/` is created, edited,
  deleted or read for writing. `tools/audit/derivation_boot_pack.json` is NOT regenerated.
- **Do not edit `tools/audit/gen_derivation_boot_pack.py`.** Not one line, not the `KEYWORDS`
  tuple, not the `CRITERION` table. The measurement injects its scratch criteria **into the
  imported module object in memory**, which writes nothing to disk. If you find yourself editing
  that file, **STOP** and report.
- **Allocate no `D-NNN`**, create, flip or discard no `OPEN_ITEMS.md` row, and write nothing into
  `DECISIONS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `FRAMEWORK.md`, `STATUS.md` or any ruling record
  other than the `STATUS.md` entry Task 3 orders.
- **Take no position on which keywords should be in the list.** The list is the user's to rule. This
  dispatch measures three candidate lists and reports numbers.

**STOP conditions, each of which ends the batch with a report and no further task:**

1. The tip at boot is not `5922a1f5bc62073681ed4187b5e71bb14e302954` — a moved tip means something
   ran that this dispatch does not know about.
2. The sanctioned enumeration tool reports a tracked modification other than the one Task 0 names.
3. Importing the generator module raises, or `gen.candidates(...)` raises, for any of the four
   criteria.
4. The measurement's own arithmetic does not close — see the checks named in Task 1(f).
5. Anything under `tools/audit/derivation_boot_pack/` or `tools/audit/derivation_boot_pack.json`
   differs from its committed blob at any point after Task 0.

---

## Task 0 — land the outstanding work of the Cowork line, and this dispatch

**One commit, five paths, nothing else.**

**(a) One TRACKED modification, additions only:**

```
cowork_rulings_2026_08_31_decision_surface_sitting.md
```

It carries five added sections written by four Cowork sessions — §3cj and §3ck (Rulings 81 and 82),
§3cl and §3cm (Rulings 83 and 84), and §3cn (Ruling 85). **Prove additions-only at the object before
committing**, by these exact positions in the working-tree file:

| Anchor | Expected line |
|---|---|
| `## 3ci.` | 5964 |
| `## 3cj.` | 6129 |
| `## 3ck.` | 6226 |
| `## 3cl.` | 6378 |
| `## 3cm.` | 6577 |
| `## 3cn.` | 6740 |
| `## 4. What this ruling does NOT do` (as a heading line) | 6902 |

Exact command:

```
cd C:\s\MS && python -c "import io;p='cowork_rulings_2026_08_31_decision_surface_sitting.md';L=io.open(p,encoding='utf-8').read().split(chr(10));print([(i+1,l[:12]) for i,l in enumerate(L) if l.startswith('## 3c') or l.startswith('## 4. What this ruling does NOT do')])"; echo "exit:$?"
```

**Expected:** the seven positions above, in that order, and the file 598,937 bytes.
**If any earlier section has moved, STOP** — the modification is then not additions-only and this
dispatch does not land it.

**(b) Four UNTRACKED files of the same line, added as they stand:**

```
cowork_handoff_entry_one_hundred_and_two.md
cowork_handoff_entry_one_hundred_and_three.md
cowork_handoff_entry_one_hundred_and_four.md
cowork_handoff_entry_one_hundred_and_five.md
```

**(c) This dispatch itself:**

```
cc_instruction_l2_keyword_count_2026_09_04.md
```

**The standing untracked `cc_*` population at the repository root is NOT landed** — it is
pre-existing and no dispatch of this line touches it. Enumerate the tracked population with the
sanctioned enumeration tool (`tools/audit/changed_paths.py`) rather than with `git status`, and
**expect exactly one tracked modification: the path in (a)**. Any other tracked modification is
STOP condition 2.

Commit message:

```
docs(cowork): land Rulings 81-85, four handoff entries and the L2 keyword-count dispatch

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the commit hash.

---

## Task 1 — the measurement

### (a) What is being measured, in one paragraph

L2's candidate criterion has five terms. The **group term** is ruled: register groups **A, C, D, E,
F, G** (Ruling 82, §3ck). The **keyword list** is ruled *widened to all four limbs of the L2
charter* but its members are not ruled (Ruling 83, §3cl). The home-document and `ARCHITECTURE.md`
passage terms are ruled wide but their members are not ruled either, so **both are EMPTY in every
criterion this dispatch measures** — measuring them is a later act. What is measured here is what
each of three candidate keyword lists adds **beyond the group term**.

### (b) The three candidate keyword lists, authored here

**LIST P — the pilot's own eighteen, unchanged.** Copied verbatim from `KEYWORDS` in
`tools/audit/gen_derivation_boot_pack.py`:

```python
LIST_P = (
    "slice", "slicing", "segment", "segmentation", "boundary", "boundaries", "change-point",
    "onset", "release", "harmonic rhythm", "where one chord ends", "finest grain", "grain",
    "atomic", "sounding", "struck", "priority of evidence", "evidence ranking",
)
```

**LIST W — the pilot's eighteen plus the precise vocabulary of the other three charter limbs.**
Every added term is taken from the L2 charter's own words at `FRAMEWORK.md` §5, and every added
term is a phrase or a word chosen so that its ordinary non-musical sense does not match:

```python
LIST_W = LIST_P + (
    # the tonality at each moment
    "tonality", "tonic", "local key", "key area", "modulation", "tonicization",
    # which sounding notes belong to the harmony and which elaborate it
    "chord tone", "non-chord", "chord-tone assignment", "elaboration relation",
    "passing tone", "passing note", "neighbour", "neighbor", "suspension", "anticipation",
    "ornament",
    # what chord is read over each span
    "scale degree", "roman numeral", "inversion", "applied chord", "chord quality",
    "figured bass",
    # the charter's own word for what L2 must publish beside the answer
    "rival",
)
```

**LIST B — LIST W plus the six bare words that sweep.** These are measured so the cost of taking
them is a number rather than an opinion:

```python
LIST_B = LIST_W + ("mode", "root", "quality", "figure", "applied", "passing")
```

### (c) The measuring script

Write it **outside the repository**, at `%TEMP%\l2_keyword_count.py`, so that nothing untracked is
left in the tree. It writes exactly one file into the tree, the artifact Task 1(e) names.

```python
# READ-ONLY MEASUREMENT. Imports the generator and calls its own candidate derivation.
# It never calls build(), write_all() or check_all(), so it writes nothing the generator writes.
import json, os, importlib.util

HERE = r"C:\s\MS\tools\audit"
spec = importlib.util.spec_from_file_location(
    "gen_dbp", os.path.join(HERE, "gen_derivation_boot_pack.py"))
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)          # main() is guarded by __main__, so this renders nothing

sort = gen.read_json(gen.SORT)
bb_data = gen.read_json(gen.BACKBONE)
backbone = {d["id"]: d for d in bb_data.get("decisions", [])}
for r in bb_data.get("retired_entries", {}).get("entries", []):
    e = r.get("the_entry", {})
    if e.get("id") and e["id"] not in backbone:
        backbone[e["id"]] = e

design_intent = [e for e in sort["entries"] if e.get("proposed_class") == "DESIGN-INTENT"]

GROUPS = ("A", "C", "D", "E", "F", "G")

LIST_P = (
    "slice", "slicing", "segment", "segmentation", "boundary", "boundaries", "change-point",
    "onset", "release", "harmonic rhythm", "where one chord ends", "finest grain", "grain",
    "atomic", "sounding", "struck", "priority of evidence", "evidence ranking",
)
LIST_W = LIST_P + (
    "tonality", "tonic", "local key", "key area", "modulation", "tonicization",
    "chord tone", "non-chord", "chord-tone assignment", "elaboration relation",
    "passing tone", "passing note", "neighbour", "neighbor", "suspension", "anticipation",
    "ornament",
    "scale degree", "roman numeral", "inversion", "applied chord", "chord quality",
    "figured bass",
    "rival",
)
LIST_B = LIST_W + ("mode", "root", "quality", "figure", "applied", "passing")

def run(name, groups, keywords):
    gen.CRITERION[name] = {"groups": tuple(groups), "home_documents": (),
                           "architecture_spans": (), "keywords": tuple(keywords),
                           "always": ()}
    return gen.candidates(name, design_intent, backbone)

def ids(cands):
    return sorted({c["id"] for c in cands}, key=lambda i: int(i.split("-")[1]))

group_only = run("m-group", GROUPS, ())
kw_p       = run("m-kw-p", (), LIST_P)
kw_w       = run("m-kw-w", (), LIST_W)
kw_b       = run("m-kw-b", (), LIST_B)
both_p     = run("m-both-p", GROUPS, LIST_P)
both_w     = run("m-both-w", GROUPS, LIST_W)
both_b     = run("m-both-b", GROUPS, LIST_B)

G = set(ids(group_only))

def per_word(cands, keywords):
    rows = {}
    for kw in keywords:
        hit = {c["id"] for c in cands
               if any(w["criterion"] == "keyword" and w["matched"] == kw
                      for w in c["matched_by"])}
        rows[kw] = {"design_intent_entries_matched": len(hit),
                    "of_those_OUTSIDE_the_six_groups": len(hit - G),
                    "ids_outside_the_six_groups": sorted(
                        hit - G, key=lambda i: int(i.split("-")[1]))}
    return rows

def marginal(cands):
    out = []
    for c in cands:
        if c["id"] in G:
            continue
        out.append({"id": c["id"], "group": c["group"], "title": c["title"],
                    "matched_by": [w for w in c["matched_by"] if w["criterion"] == "keyword"]})
    return sorted(out, key=lambda r: int(r["id"].split("-")[1]))

result = {
    "what_this_is": ("THE READ-ONLY KEYWORD COUNT owed by Ruling 83 (section 3cl of "
                     "cowork_rulings_2026_08_31_decision_surface_sitting.md) before L2's keyword "
                     "list is ruled. It measures three candidate keyword lists against the ruled "
                     "group term. It authors no verdict, withholds nothing and renders no pack."),
    "how_it_was_derived": ("The generator's own candidates() function, called with scratch criteria "
                           "injected into the imported module in memory. The committed CRITERION "
                           "table and KEYWORDS tuple are unchanged on disk."),
    "the_population": {"design_intent_class": len(design_intent),
                       "sort_entries_total": len(sort["entries"])},
    "the_ruled_group_term": {"groups": list(GROUPS), "candidates": len(G)},
    "the_three_lists": {
        "LIST_P_the_pilots_eighteen": list(LIST_P),
        "LIST_W_widened_to_four_limbs": list(LIST_W),
        "LIST_B_widened_plus_the_six_bare_words": list(LIST_B),
    },
    "the_counts": {
        "group_term_alone": len(G),
        "LIST_P": {"keywords_alone": len(ids(kw_p)),
                   "with_the_group_term": len(ids(both_p)),
                   "added_beyond_the_group_term": len(set(ids(kw_p)) - G)},
        "LIST_W": {"keywords_alone": len(ids(kw_w)),
                   "with_the_group_term": len(ids(both_w)),
                   "added_beyond_the_group_term": len(set(ids(kw_w)) - G)},
        "LIST_B": {"keywords_alone": len(ids(kw_b)),
                   "with_the_group_term": len(ids(both_b)),
                   "added_beyond_the_group_term": len(set(ids(kw_b)) - G)},
    },
    "per_word_LIST_B": per_word(kw_b, LIST_B),
    "what_LIST_W_adds_beyond_the_group_term": marginal(kw_w),
    "what_LIST_B_adds_that_LIST_W_does_not": [
        r for r in marginal(kw_b)
        if r["id"] not in {x["id"] for x in marginal(kw_w)}],
    "the_bound_on_this_measurement": (
        "It counts CANDIDATES, not withheld entries: a candidate carries an authored verdict and a "
        "candidate ruled OUT is rendered into the pack. The home-document and ARCHITECTURE.md "
        "passage terms are EMPTY here because their members are not ruled, so every count is a "
        "count for the criterion AS FAR AS IT IS RULED and not for the finished criterion."),
}

out = os.path.join(HERE, "l2_keyword_count_measurement.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump(result, fh, indent=1, ensure_ascii=False)
    fh.write("\n")

c = result["the_counts"]
print("design-intent class:", result["the_population"]["design_intent_class"])
print("group term alone   :", c["group_term_alone"])
for k in ("LIST_P", "LIST_W", "LIST_B"):
    print(f"{k}: alone {c[k]['keywords_alone']:>4} · with group {c[k]['with_the_group_term']:>4} "
          f"· added beyond group {c[k]['added_beyond_the_group_term']:>4}")
print("wrote", out)
```

### (d) The exact command

```
cd C:\s\MS && python %TEMP%\l2_keyword_count.py > %TEMP%\l2_kw_out.txt 2>&1; echo "exit:$?"
```

then

```
type %TEMP%\l2_kw_out.txt
```

**Rule 2 of the bash-command rules applies** — the run is redirected to a file and read separately.
**Do not paste the artifact's contents into the report; cite it (D-431).**

### (e) The artifact

```
tools/audit/l2_keyword_count_measurement.json
```

New, generated, and the ONE home of every figure this measurement produces. **No figure from it is
transcribed into any other document** — the report and the `STATUS.md` entry cite it (D-431).

### (f) The checks that must pass, each an arithmetic identity the script's own output supports

1. `the_population.design_intent_class` is **244**. If it is not, **STOP** — the sort artifact has
   moved under this dispatch and every count below would be over a different population.
2. For each of the three lists: `with_the_group_term` equals
   `group_term_alone + added_beyond_the_group_term`. If any of the three does not close, **STOP**.
3. `LIST_P.added_beyond_the_group_term` ≤ `LIST_W.added_beyond_the_group_term` ≤
   `LIST_B.added_beyond_the_group_term`. A wider list cannot add fewer entries; if it does, the
   run is wrong and this is a **STOP**.
4. Every id in `what_LIST_W_adds_beyond_the_group_term` carries at least one `matched_by` record
   whose `criterion` is `keyword` and whose `in_context` shows the matched text. An entry that
   cannot be seen to have matched is a **STOP**.

### (g) Prove nothing else moved

After the run, enumerate with the sanctioned enumeration tool. **Expected: exactly one untracked
addition, `tools/audit/l2_keyword_count_measurement.json`, and ZERO tracked modifications.**
Anything under `tools/audit/derivation_boot_pack/` or `tools/audit/derivation_boot_pack.json`
appearing as modified is STOP condition 5 — the measurement was supposed to touch neither.

Commit the artifact alone:

```
chore(audit): measure the L2 candidate keyword lists (read-only, no verdict authored)

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the commit hash.

---

## Task 2 — the report

Write `cc_report_l2_keyword_count_2026_09_04.md` at the repository root, untracked, and commit it in
Task 3's commit. It carries, in this order:

1. **The tip at boot and the tip at close**, each read at both ref files.
2. **Task 0's result** — the commit hash, the seven anchor positions found, the byte size found, and
   the enumeration tool's output showing exactly one tracked modification before the commit.
3. **The three counts**, as the numbers the artifact carries — the group term alone, and for each of
   the three lists: alone, with the group term, and added beyond the group term.
4. **The five keywords of LIST_B with the largest `of_those_OUTSIDE_the_six_groups`**, named with
   their numbers, because that is the measurement the user's decision turns on.
5. **The entries LIST_B adds that LIST_W does not**, by identity, with the word that matched each.
6. **Every check of Task 1(f)**, each stated as passed or failed with its own numbers.
7. **Any STOP reached**, in full, with what was and was not done.
8. **A declared-departures section** — anything you did that this dispatch does not order, stated
   rather than absorbed.

**Recommend nothing.** The report reports; the keyword list is the user's to rule at a Cowork
decision surface.

---

## Task 3 — `STATUS.md` and close

Add ONE dated entry at the head of `STATUS.md`'s entry list, in the established form, recording:
the measurement was taken, its artifact's path, that no verdict was authored, no pack rendered, no
pack directory or manifest touched, and no register identity allocated. **Per the OI-222 pointer
convention this entry is a POINTER and no figure is restated in it (D-431).**

Commit `STATUS.md` and the Task 2 report together:

```
docs(status): record the L2 keyword-count measurement

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Then write the close section into `cowork_away_returns.md` in the established form, and one
further commit carrying the end-state guard artifact, so that the batch reads as FINISHED rather
than mid-flight.

---

## The writing side's self-check, run before this dispatch was released (D-434)

Read against `CLAUDE.md`'s guiding principles and conventions:

- **#19 (nothing unestablished is trusted).** The measurement establishes nothing about any entry's
  verdict and claims nothing about the criterion's reach; its own bound is written into the artifact
  it produces.
- **#6 (one path per concern).** The measurement calls the generator's own `candidates()` rather
  than reimplementing the matching, so there is no second matcher to disagree with the first.
- **#17f / D-431.** Every figure lands in the generated artifact and is cited, never transcribed.
- **D-249.** This dispatch puts no question to the user and takes no position on the list's
  membership.
- **The working-tree read rule.** The Cowork writing side read every object for this dispatch —
  `FRAMEWORK.md` §5, the generator, the manifest, the register's data file and the sitting record —
  through the file tools on bridge-staged snapshots. No shell read any working-tree file on the
  writing side.
- **The reserved-word convention.** *Measurement tool*, *check*, *script* are used; *instrument* is
  not.

*Provenance: Cowork writing side, 2026-09-04, at tip `5922a1f5bc62073681ed4187b5e71bb14e302954`,
after the ordinary session-start read in full and with Ruling 85 recorded at §3cn of the sitting
record. The three candidate keyword lists are AUTHORED by the writing side as measurement inputs and
are not a ruling; the user rules the list after this measurement is in front of him.*
