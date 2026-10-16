# L3's research-extracts member — the per-file cut list, 2026-10-16

> **STATUS: A DERIVED LIST FOR THE L3 PACK-BUILD DISPATCH. NO RULING IS TAKEN HERE.** Cowork, 2026-10-16
> (Stockholm), the sitting that booted on `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eleven.md`.
> Entry 411 §3 item 5 orders this list derived first, at each file, and checked at its sources in a turn of its own
> before the dispatch carries it. An interim carrier: it lands in git at the next dispatch's Task 0. **No act of
> this sitting is a commit to git.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both read
> `a01e9402fbaf034fe0d357214b67c06a8294309c`, read as files with the file tools over staged copies.

## 1. What this list is for

L3's boot pack carries a research-extracts member: the first extractions of L3's six slice rows (36, 37, 38, 39,
with 34 and 40 carried from L2's slice — Ruling 3 (i) of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`) and
the eleven first-pass extracts of Ruling 1 of `cowork_rulings_2026_10_15_l3_first_pass_extracts_sitting.md`. Every
file is quoted whole with the passages stating **this project's own positions** cut per file (limb A of Ruling 1 of
`cowork_rulings_2026_09_21_l2_extracts_member_cutting_sitting.md`), the two ruled shared cut strings working where
they reach, and the extras' leak scan (limb B) listing its hits to the user before any boot.

This list gives, for each of the seventeen files, the exact filter entries the dispatch authors into
`EXTRAS["l3"]`'s member (8) in `tools/audit/gen_derivation_boot_pack.py`, in the two forms that tool's
`filter_part` already reads:

- a **cut** — `heading_contains`, `heading_level`, `why`, and `runs_to_end` where the section is the file's last at
  its level (`_cut_spans`: the heading text must match exactly one heading at that level);
- a **removal** — `anchor`, `opens_with`, `closes_with`, `why` (`_removal_spans`: the anchor is found once in the
  whitespace-collapsed text; the removal runs from the nearest `opens_with` *before* the anchor to the first
  `closes_with` *after* it; `opens_with` and `closes_with` are matched in the raw text).

Every string below was taken from the file as it stands at this sitting's staged copy, and placed by reading the
lines around it. **Whether each entry runs without a STOP is proved only by the render**, which also proves in both
directions that nothing else was removed.

## 2. What counts as "this project's own position", and the bound

The criterion is the one limb A and §2.3 of the first-pass record already use, applied to every file the same way:

- **cut** a section, or remove a passage, that states this project's conclusion about its own design, its
  framework's decision points, its principles, its charters or its verification targets; or that is this project's
  bookkeeping — its rows, passes, sessions, rulings, file paths, corrections-of-record notes (the "★ CORRECTED …
  FORMER WORDING, PRESERVED (#12)" notes) and provenance lines;
- **keep** what reports the paper — its claims, its numbers, its stated scope — and the extract's own labelled
  reading of the paper where that reading names nothing of this project.

**Bound, stated so it is not read wider.** The list rests on this side's reading of each file. Passages kept are
named at §5 where a reader could argue the other way. Limb B catches identity strings and withheld document names
only; a paraphrase passes it. **The file titles are kept** — every title names a "row" or a "population row" — as
L2's render kept them; a title is the first line of every quoted span and is not removable by either filter form
without a new mechanism.

## 3. Where the twelve L2 entries come from, and why they are carried

Twelve of the seventeen files are already members of L2's extracts member, with authored entries in
`EXTRAS["l2"]`: rows 34 and 40, and ten of the eleven first-pass extracts (all but ChoCo). L2's pack directory
(`tools/audit/derivation_boot_pack/l2/`) carries modification time 1790514375260 at its listing; each of the twelve
files carries an earlier modification time at the `reading_pass/extracts/` listing. So each file is, by its
modification time, the text L2's render ran its entries over, and that render's both-directions check passed.
**Bound:** a modification time is evidence and not proof; the L3 render re-runs every STOP.

**The rule for these twelve:** the L3 part carries L2's `removals` and `cuts` for that file **unchanged and in
L2's order** — the `why` strings may name this list instead — and appends the additions below. Nothing L2 cut is
restored. **For the other five** (rows 36, 37, 38, 39 and ChoCo) the entries below are the whole part.

Where an entry's `why` is not written below, it is: *"Limb A of Ruling 1 of 2026-09-21: project-facing text
(`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"*. The shared cut string's `why` is
L2's own: *"the ruled shared cut string, unchanged (Ruling 2 of 2026-09-05; Ruling 1 of 2026-09-20; Ruling 1 of
2026-09-21)"*.

## 4. The seventeen files

All paths are under `reading_pass/extracts/`. Each part is `"spans": [{"kind": "whole"}]`. Strings are given as
JSON, so a quotation mark inside one is written `\"`.

### 4.1 Row 36 — `ju-margot-mckay-dahn-fujinaga-2020-automatic-figured-bass-annotation-bach-chorales-figured-bass-dataset.md` (NEW)

Removals, in file order:

```json
[
 {"anchor": "**STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-10-14).** Written under",
  "opens_with": "> ",
  "closes_with": "open-items row or decisions-register entry.**",
  "why": "the opening status block above the first heading: candidacy row, slice placement, handoff entries, independence bookkeeping"},
 {"anchor": "`docs/research_papers/ju_margot_mckay_dahn_fujinaga_2020_ismir_bcfb_figured_bass.pdf`",
  "opens_with": "**File:**",
  "closes_with": "(1,022,218 bytes at the staging result).",
  "why": "the Identity section's file line: a repository path and a staging figure"},
 {"anchor": "the printed word is \"obbligato\". Former wording, preserved (#12): \"obligato\"",
  "opens_with": " *(★ CORRECTED 2026-10-15 at the cross-check against the second extract",
  "closes_with": "\"obligato\".)*",
  "why": "a correction-of-record note"},
 {"anchor": "This bears on guiding principle #20, fit/evaluation separation",
  "opens_with": " *(",
  "closes_with": "cross-validated.)*",
  "why": "this project's principle #20 applied to the paper's figure"},
 {"anchor": "the paper says \"one octave apart\", not \"an octave or more\"",
  "opens_with": " *(★ CORRECTED 2026-10-15 at the cross-check against the second",
  "closes_with": "22\".)*",
  "why": "a correction-of-record note"}
]
```

Cuts, `heading_level` `"## "`:

| `heading_contains` | `runs_to_end` | ground |
|---|---|---|
| `detail specification could adopt, adapt, or must argue against` | — | the shared string; reaches "What an L3 detail specification could adopt, adapt, or must argue against" |
| `★ Findings, routed and not applied` | — | project findings (FRAMEWORK.md appendix, D-514, this project's slice) |
| `Centrality` | — | this project's centrality verdict |
| `What this extract does NOT do` | — | bookkeeping |
| `The read-back, recorded` | — | bookkeeping |
| `The cross-check against the second extract (2026-10-15)` | **true** | the file's last `##` section; carries the `---` rule and the provenance paragraph with it |

### 4.2 Row 37 — `bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md` (NEW)

```json
[
 {"anchor": "**STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under",
  "opens_with": "> ",
  "closes_with": "> #12.)*",
  "why": "the opening status block: candidacy row, V6, DP-I, Ruling 10, correction-of-record notes and a ruling"},
 {"anchor": "that make this L1's paper",
  "opens_with": " ",
  "closes_with": "L1's paper",
  "why": "the `###` heading's trailing words placing the paper in this project's L1; the heading `### ★ The two exclusions` is kept"},
 {"anchor": "`docs/research_papers/bigo_feisthauer_giraud_leve_2018_ismir_cadence_detection_features.pdf`",
  "opens_with": "**File:**",
  "closes_with": "cadence_detection_features.pdf`.",
  "why": "the Identity section's file line: a repository path"},
 {"anchor": "The feature that IS the L1 charter's third cue.",
  "opens_with": " ",
  "closes_with": "third cue.",
  "why": "a bold label tying the paper's feature to this project's L1 charter; `**★ [FACT, §2.1]**` is kept"},
 {"anchor": "the dropped condition is what separates the two features",
  "opens_with": " *(★ CORRECTED 2026-09-20 ON THE USER'S RULING.",
  "closes_with": "the feature whose implied tonality has Z's bass as its tonic.)*",
  "why": "a correction-of-record note"},
 {"anchor": "prints \"hard-coded\", places \"but\" before \"with\"",
  "opens_with": "*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): \"Note that we previously",
  "closes_with": "the citation \"[9]\".)*",
  "why": "a correction-of-record note"},
 {"anchor": "— and it is the framework's own sentence",
  "opens_with": " ",
  "closes_with": "own sentence",
  "why": "a bold label tying the paper's sentence to this project's framework"},
 {"anchor": "and the Table 4 values now given beside the quotation do not bear it",
  "opens_with": " *(★ CORRECTED 2026-09-20 ON THE USER'S RULING. FORMER WORDING, PRESERVED (#12):",
  "closes_with": "and R lowers Haydn PAC.)*",
  "why": "a correction-of-record note"},
 {"anchor": "the page trains PAC and PAC+rIAC on the Bach corpus",
  "opens_with": " *(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED",
  "closes_with": "no rIAC-only classifier was met in the pages as read)*",
  "why": "a correction-of-record note"},
 {"anchor": "\"Suspensions were expected to be significant for both PAC and HC and\"",
  "opens_with": " *(★ CORRECTED 2026-09-20. FORMER WORDING,",
  "closes_with": "they do not appear significantly in these corpora.\")*",
  "why": "a correction-of-record note"}
]
```

Cuts, `"## "`: the shared string (reaches "What an L1 detail specification could adopt, adapt, or must argue
against"); `★ Findings, routed and not applied`; `Centrality`; `What this extract does NOT do` with
`runs_to_end: true` (the last `##` section; the provenance paragraph goes with it).

### 4.3 Row 38 — `karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md` (NEW)

```json
[
 {"anchor": "**STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under",
  "opens_with": "> ",
  "closes_with": "> for the act; the ground is the second extract's §9.4 and §5.",
  "why": "the opening status block: candidacy row, V6, Ruling 10, correction-of-record notes and a ruling"},
 {"anchor": "`docs/research_papers/karystinaios_widmer_2022_arxiv_cadence_detection_gnn.pdf`",
  "opens_with": "**File:**",
  "closes_with": "cadence_detection_gnn.pdf`.",
  "why": "the Identity section's file line: a repository path"},
 {"anchor": "that is, row 37's.",
  "opens_with": " —",
  "closes_with": "row 37's.",
  "why": "a pointer to this project's row 37"},
 {"anchor": "§3.1's text names the time signature",
  "opens_with": "*(★ CORRECTED 2026-09-20 — a locator added",
  "closes_with": "with no locator.)*",
  "why": "a correction-of-record note"},
 {"anchor": "The deliberate weakening of row 37's frame, and its stated purpose.",
  "opens_with": " ",
  "closes_with": "its stated purpose.",
  "why": "a bold label naming this project's row 37; `**★ [FACT, §3.1]**` is kept"},
 {"anchor": "preserved (#12): \"no assumptions and reference to\"",
  "opens_with": "*(★ CORRECTED 2026-09-20 — the page prints \"no assumptions on and reference to\"",
  "closes_with": "\"no assumptions and reference to\".)*",
  "why": "a correction-of-record note"},
 {"anchor": "preserved (#12): \"three different scales, note-wise,",
  "opens_with": "*(★ CORRECTED 2026-09-20 — the page prints \"three different levels",
  "closes_with": "onset-wise and beat-wise (the latter\".)*",
  "why": "a correction-of-record note"},
 {"anchor": "the reference model's Bach PAC precision 0.89",
  "opens_with": "*(★ CORRECTED 2026-09-20 — four bold marks",
  "closes_with": "digit changed.)*",
  "why": "a correction-of-record note"},
 {"anchor": "preserved (#12): \"on Bach fugues\"",
  "opens_with": " *(★ CORRECTED 2026-09-20 — the page prints \"in Bach",
  "closes_with": "\"on Bach fugues\".)*",
  "why": "a correction-of-record note"},
 {"anchor": "independent replication.\" — the page describes a different method",
  "opens_with": "*(★ CORRECTED 2026-09-20 ON THE USER'S RULING. Former wording, preserved (#12): \"★ [FACT, §6.1] The",
  "closes_with": "independent replication.)*",
  "why": "a correction-of-record note"},
 {"anchor": "the quotation had closed with a full stop mid-sentence",
  "opens_with": "*(★ CORRECTED 2026-09-20 —",
  "closes_with": "emerging in the learning model.\"*\".)*",
  "why": "a correction-of-record note"},
 {"anchor": "§6.2 works three examples, not one",
  "opens_with": "*(★ CORRECTED 2026-09-20 — two places in this paragraph.",
  "closes_with": "considerations\".)*",
  "why": "a correction-of-record note"},
 {"anchor": "which the L0 contract also gives",
  "opens_with": ",",
  "closes_with": "never as a fact about the tonality",
  "why": "this project's L0 contract and its key-signature rule, stated beside the paper's input"},
 {"anchor": "\"No chord segmentation, no harmonic analysis, no",
  "opens_with": "*(★ CORRECTED 2026-09-20 — a negative given its bound: the page describes",
  "closes_with": "decided tonality —\".)*",
  "why": "a correction-of-record note"},
 {"anchor": "\"Nothing else: no chord, no key, no segmentation.\"",
  "opens_with": " *(★ CORRECTED 2026-09-20 — a negative given its bound. Former",
  "closes_with": "no segmentation.\")*",
  "why": "a correction-of-record note"},
 {"anchor": "\"Pre-training on a second dataset is required for the best",
  "opens_with": "*(★ CORRECTED 2026-09-20 — two places: a claim wider than Table 2",
  "closes_with": "cannot reach form-level judgements, by design.\")*",
  "why": "a correction-of-record note"}
]
```

Cuts, `"## "`: the shared string (reaches "What an L1 detail specification could adopt, …"); `★ Findings, routed
and not applied`; `Centrality`; `What this extract does NOT do` with `runs_to_end: true`.

### 4.4 Row 39 — `sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md` (NEW)

```json
[
 {"anchor": "**STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under",
  "opens_with": "> ",
  "closes_with": "> changed.",
  "why": "the opening status block: candidacy row, the doubt default, Ruling 10, the cross-check bookkeeping"},
 {"anchor": "FORMER WORDING, PRESERVED (#12): \"*Journal of New Music Research* **47:1**",
  "opens_with": " *(★ CORRECTED 2026-10-15 at the",
  "closes_with": "The \"published online\" date matches the download stamp.)*",
  "why": "a correction-of-record note in the Identity section"},
 {"anchor": "`docs/research_papers/sears_pearce_caplin_mcadams_2018_jnmr_cadence_expectations.pdf`",
  "opens_with": "**File:**",
  "closes_with": "cadence_expectations.pdf`.",
  "why": "the Identity section's file line: a repository path"},
 {"anchor": "added 2026-10-15 at the cross-check:**",
  "opens_with": ",",
  "closes_with": "at the cross-check",
  "why": "a dating of this project's correction inside a bold label; the bound itself, read from the paper's Table 5, is kept"}
]
```

Cuts, `"## "`: `★ The doubt-default question, answered` (this project's verdict that the paper is not an L1
candidate, with two correction-of-record notes inside it); the shared string (reaches "What an L1 detail
specification could adopt, …"); `★ Findings, routed and not applied`; `Centrality`; `What this extract does NOT do`
with `runs_to_end: true`.

### 4.5 Row 34 — `illescas-rizo-inesta-2007-harmonic-melodic-and-functional-automatic-analysis.md` (L2's entry, carried, plus these)

L2's entry stands at `EXTRAS["l2"]`'s part for this file: one removal (the opening status block) and nine cuts
(§1, §2, §4, §5, §6, §7, §8, §10, and §11 with `runs_to_end`). L2's render kept §0, §3 and §9 whole. Additions:

Cut, `"## "`: `0. What this row is, taken from its own rows and not from any summary` — the candidacy row, the
slice row (*"whatever it does with cadences or grouping is L3's"* — this project's placement), the bibliography
row and the citing rows; all of it bookkeeping.

```json
[
 {"anchor": "not fetched, §9)",
  "opens_with": " (",
  "closes_with": "§9)",
  "why": "this read's own act, inside §3"},
 {"anchor": "row 7); results",
  "opens_with": ",",
  "closes_with": "row 7",
  "why": "this project's row number beside the paper's reference [13]; \"(Temperley & Sleator)\" is kept"},
 {"anchor": "and what this read did NOT do",
  "opens_with": ",",
  "closes_with": "did NOT do",
  "why": "the §9 heading's trailing words; \"## 9. What the paper does NOT claim\" is kept"},
 {"anchor": "fetch the online results report, the rule set at the authors' URL",
  "opens_with": "**This read did not**",
  "closes_with": "where they last stood read.",
  "why": "§9's second paragraph: this read's own bookkeeping; the paragraph on what the paper does not claim is kept"}
]
```

### 4.6 Row 40 — `declercq-2015-a-model-for-scale-degree-reinterpretation.md` (L2's entry, carried, plus these)

L2's entry stands: one removal (the opening status block) and nine cuts (Identity, the two ★ sections, the two
checks, the shared string, Findings, Centrality, and the last section with `runs_to_end`). L2's render kept "What
the paper is, in its own structure", "The paper's own claims, labelled" and "Coupling facts (mandatory)". Additions,
all inside those kept sections, in file order:

```json
[
 {"anchor": "§9.3 (a), under the standing rule of handoff entry 198 §7",
  "opens_with": " *(★ CORRECTED 2026-09-19 at the second extract's cross-check",
  "closes_with": "related key area\" — the page prints the hyphen.)*",
  "why": "a correction-of-record note, claim (7)"},
 {"anchor": "its §9.3 (e), under the standing rule",
  "opens_with": " *(★ CORRECTED 2026-09-19 at the second extract's cross-check,",
  "closes_with": "No value is changed.)*",
  "why": "a correction-of-record note, claim (10)"},
 {"anchor": "his words, \"I agree with recommendation A\" — the second extract's §9.4 (f)",
  "opens_with": " *(★ CORRECTED 2026-09-19 ON THE USER'S",
  "closes_with": "image.)*",
  "why": "a correction-of-record note and a ruling, claim (10)"},
 {"anchor": "§9.3 (b), under the standing rule of handoff entry 198 §7",
  "opens_with": " *(★ CORRECTED 2026-09-19 at the second extract's cross-check, its",
  "closes_with": "and its close is now carried.)*",
  "why": "a correction-of-record note, claim (13)"},
 {"anchor": "said the paper \"takes the second position operationally\"",
  "opens_with": " *(★ This sentence's first writing",
  "closes_with": "accidentals is why it can.)*",
  "why": "a correction-of-record note, claim (15)"},
 {"anchor": "and it bears on a live grading convention",
  "opens_with": ",",
  "closes_with": "grading convention",
  "why": "the claim label's trailing words pointing at this project's grading convention"},
 {"anchor": "this quotation is this extract's emphasis; the page prints the sentence without it",
  "opens_with": " *(★ REMARK ADDED 2026-09-19 at the second",
  "closes_with": "measure agreement with an annotator rather than predictive value.",
  "why": "claim (15a)'s remark and the paragraph after it: D-211, CLAUDE.md, and this project's two key columns"},
 {"anchor": "added by the whole reading of this extract",
  "opens_with": ",",
  "closes_with": "extract",
  "why": "the claim (19) label's trailing words: this extract's own history"},
 {"anchor": "Recorded as DATA and routed nowhere",
  "opens_with": " *(★ REMARK ADDED 2026-09-19, the second extract's §9.3 (d):",
  "closes_with": "and no transfer is claimed here.**",
  "why": "claim (19)'s remark and the routing sentence after it, which names D-522"},
 {"anchor": "NOT ADMITTED, and `BIBLIOGRAPHY.md` line 38 records",
  "opens_with": " **That work is candidacy row 24",
  "closes_with": "took the same course.)*",
  "why": "claim (20)'s tail: candidacy row, bibliography line, #1 and row 7"},
 {"anchor": "the bold on \"Figure 5\" is this extract's emphasis",
  "opens_with": "*(★ REMARK",
  "closes_with": "No word is changed.)*",
  "why": "claim (21)'s remark"},
 {"anchor": "\"five or six\"; the whole reading counted",
  "opens_with": " *(★ The first writing of this line read",
  "closes_with": "it is five in each.)*",
  "why": "a correction-of-record note in Coupling facts"}
]
```

### 4.7 The eleven first-pass extracts

L2's entry for each of the ten that are L2 members carries the opening status block's removal (which takes the
2026-09-26 staleness note with it where the file has one — McLeod & Rohrmeier 2021 and 2024, HarmTrace, Sapp,
Hentschel), the shared `Bearing` cut, and a last-section cut with `runs_to_end`. That already covers the §2.3
items of the first-pass record except Feisthauer's claims clause. Additions:

**`feisthauer-2021-lille-thesis-modulations-cadences-sonata-form.md`** (L2's entry + one):

```json
[{"anchor": "the same PAC/HC gap as V6's two verified primaries",
  "opens_with": " —",
  "closes_with": "at this thesis's own corpora.",
  "why": "the V6 clause in the claims (first-pass record §2.3); the V6 clause in the verification section goes with L2's last-section cut"}]
```

**`hamanaka-hirata-tojo-2013-computational-music-theory-gttm.md`** (L2's entry + three). L2's cuts already take the
by-catch section, the does-and-does-not-close section with its staleness note and the provenance line (§2.3).

```json
[
 {"anchor": "`external resarch summary/Computational Music Theory and Its.pdf` —",
  "opens_with": "**File as supplied:**",
  "closes_with": "(see the foot of this file).",
  "why": "a repository path and a pointer to the cut section"},
 {"anchor": "the numbers row 19 exists to supply",
  "opens_with": " —",
  "closes_with": "to supply",
  "why": "this project's row number in the table label"},
 {"anchor": "WHICH IS THE ROW'S WHOLE YIELD",
  "opens_with": ",",
  "closes_with": "WHOLE YIELD",
  "why": "this project's row in the label"}
]
```

**`lazzari-2023-knowledge-based-chord-embeddings-modal-harmony-ontology.md`** (L2's entry + three). L2's cut already
takes the does-not-establish section and the provenance line (§2.3).

```json
[
 {"anchor": "it is a master's thesis**, indexed as a paper nowhere",
  "opens_with": "**Why eight searches missed it:",
  "closes_with": "queries could reach.",
  "why": "this pass's search bookkeeping"},
 {"anchor": "which is population row 8 of this same pass",
  "opens_with": " —",
  "closes_with": "same pass** —",
  "why": "this project's population row"},
 {"anchor": "which is better practice than most",
  "opens_with": " *Declared and acted on,",
  "closes_with": "of the population.*",
  "why": "this extract's grading of the paper against this project's population"}
]
```

**`bachi-2026-boundary-aware-symbolic-chord-recognition.md`** (L2's entry + two):

```json
[
 {"anchor": "a ground-truth-quality fact in the direction of this project's principle #21",
  "opens_with": " —",
  "closes_with": "principle #21.",
  "why": "this project's principle #21"},
 {"anchor": "POORER than this project's notated record",
  "opens_with": " Its L0 is therefore",
  "closes_with": "project's input does not have.",
  "why": "a comparison with this project's L0"}
]
```

**`hentschel-moss-mcleod-neuwirth-rohrmeier-2021-unified-chord-model.md`** (L2's entry + one):

```json
[{"anchor": "the DP-N flashpoint evidence lives elsewhere",
  "opens_with": " —",
  "closes_with": "(the meta-corpus paper)",
  "why": "this project's decision point DP-N and where its evidence is held"}]
```

**`mcleod-rohrmeier-2021-modular-harmonic-analysis.md`** (L2's entry + two):

```json
[
 {"anchor": "exactly the L0 contract this project's framework gives",
  "opens_with": " —",
  "closes_with": "(spelling, meter given)",
  "why": "a comparison with this project's L0 contract"},
 {"anchor": "so nothing like the framework's DP-K rival stream",
  "opens_with": " —",
  "closes_with": "boundary.",
  "why": "a comparison with this project's DP-K"}
]
```

**`deberardinis-etal-2023-choco-chord-corpus.md`** (NEW — not an L2 member):

```json
[{"anchor": "**Establishment bound:** read 2026-08-30 via one prompted extraction call over the open full",
  "opens_with": "> ",
  "closes_with": "(route in the fetched content record).",
  "why": "the opening status block: this pass's retrieval bookkeeping"}]
```

Cuts, `"## "`: `Bearing` (the shared first-pass string); `Verification targets touched` with `runs_to_end: true`.

**No addition** for `napoleslopez-feisthauer-leve-fujinaga-2020-local-keys-modulations-tonicizations.md`,
`sapp-2005-visual-hierarchical-key-analysis.md`, `dehaas-magalhaes-wiering-veltkamp-2013-harmtrace-functional-analysis.md`
and `mcleod-rohrmeier-2024-chord-tone-alterations-suspensions.md`: what survives L2's entries reports the paper.

## 5. Kept, and named so the choice can be challenged

- **Every file's title line**, with its row or population-row number (§2).
- Illescas: the title's parenthesis *"(ICMC 2007 by the bibliography's row; …)"*.
- Hamanaka: *"★ THE READING THIS FORCES, STATED PLAINLY"* — the extract's reading that the implementation puts the
  hierarchy downstream of harmony. It names nothing of this project; it bears on what DP-O leaves open, which the
  charter member states anyway.
- Lazzari: *"The list's description is confirmed on both halves, at the object"* and its three bullets — the
  framing names this pass's list; the bullets quote the thesis.
- de Clercq: claim (2)'s *"What that figure IS and IS NOT"* paragraph, and the *"derived here"* arithmetic.
- McLeod & Rohrmeier 2024: *"This is the load-bearing coupling fact"* — the extract's emphasis on the paper's own
  scope.
- Sears et al.: the Coupling facts sentence *"Nothing in its output is a fact about the music that another layer
  could consume as evidence …"* — "layer" is this project's word, but the sentence states what the paper's output
  is. *(Added at the check, §7.)*

## 6. What this list does NOT do

It edits no tool and no extract, renders nothing, writes no dispatch, takes no ruling and allocates no
decisions-register identity. It does not decide the member's number, file name or title (the dispatch writes
them on L2's shape) and does not decide whether limb B's hits STOP the run or are listed (the generator's current
behaviour stands).

## 7. The check at the sources, run in its own turn after the first landing

Each string of §4 was searched for at its own file's staged copy: every anchor found once (two of them — the
Lazzari population-row anchor and the de Clercq claim (19) label — span a line break and match only in the
whitespace-collapsed text the tool searches), each `opens_with` found before its anchor and each `closes_with`
after it, with no `closes_with` between the two; every heading a cut names found once at `## `. **No string was
changed by the check.** A search of all seventeen files for any decision identity (`D-` and three digits) and for
the names of L3's withheld documents found every hit inside a span this list or L2's entries cut or remove.
**Bound:** that search reaches identities and five document names; it does not reach a paraphrase.

**Corrected at the check, former wordings kept here (#12):** the provenance line below said the files were read
*"whole for the five new parts and at the sections L2's entries keep for the twelve carried ones"* — the ten
first-pass members were read whole, and rows 34 and 40 at their kept sections; and §5 gained the Sears item.

*Provenance: Cowork, 2026-10-16 (Stockholm), the sitting booted on entry 411. Derived at each file's staged copy —
the five new parts and the ten carried first-pass members read whole, rows 34 and 40 at the sections L2's entries
keep — against `EXTRAS["l2"]` in the generator. The user's words: the opening instruction; "continue".*
