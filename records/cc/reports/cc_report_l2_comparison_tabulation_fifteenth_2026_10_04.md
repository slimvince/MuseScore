# Report — the L2 comparison, the fifteenth tabulation batch: §7, §8, §9 and §14 written, each whole in its own commit; the reading file is complete over its population and in its once-written sections

> **STATUS: SESSION REPORT. It decides nothing.** Claude Code, 2026-10-04, under
> `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md` (called *the dispatch*
> below). Every disposition in the reading file is a proposal; nothing here recommends anything about the derivation,
> the method or any open question. The check outputs this report rests on are kept verbatim in Appendices A to C, in the
> shape the user ruled on 2026-10-03; no log of shell calls is kept. A hash this report cannot contain (the close
> commit's own) is at the git log.

## 0. In one paragraph

The batch tabulated no member, the population having been complete since position 62. It wrote the four sections the
reading file writes once after the last member — §7, §8, §9 and §14 — **each whole and in its own commit, in that
order**, each opened only after a capacity judgment written out and logged. **§7 is generated** from the committed
file's own rows by a script whose one change from the fourteenth batch's is that it reads a verdict written once for a
range of claims once per claim; **its four equations against §13 all held** (AGREES, DIFFERS, THE DERIVATION IS SILENT,
and the total — Appendix B.1a), Rows 17.29 and 17.52 being the only range-form rows it read, and no row unreadable.
**§8** quotes each of the eighteen open questions from the derivation and gives one sentence naming the rows that speak
to it, the five questions the derivation marks for the user listed exactly like the others and put to nobody; **§9**
does the same for the five points of the derivation's §7; **§14** relays the derivation's §6.1 to §6.6 byte for byte,
with no verdict word, names the rows carrying a SEEN mark, and keeps the wider-check sentence with its opening words
changed. §0 and §16 were brought true at each commit; one clause was added, at §7's commit, to §0's sentence on the
fourteenth batch, stating its stop and its reason; no other word of §0's sentences on the earlier batches changed.
**A5 held after every section commit and at the close**: §6.1 to §6.62, §1 to §5, §10 to §13 and §15 byte-identical to
the blob `a77405a2…`. The close ran whole: the forward bound moved exactly the fourteenth batch's one entry, A3 held term
by term, and the two guard captures are identical verdict for verdict. The context was **not** compacted.

## 1. The ordered first read, and Task 0

**The ordered first read.** The opening instruction named only the dispatch, so its first 580 lines were read before
the derivation (declared at §5, departure 1). The derivation `cowork_blind_derivation_l2_2026_09_27.md` was then read
**§5 first, then §6, then §7, then the whole file**, before any other read; `CLAUDE.md` and the auto-memory index had
reached the context at boot as injected context, before any tool call. The counts at the derivation, taken by this
session: **49 statements** (L2-S1 to L2-S49), **18 open questions** (OQ-L2-1 to OQ-L2-18), **5 marked ★** (OQ-L2-2,
4, 5, 8, 16), **five points** in its §7 — the reading file's manifest's counts, no difference. Then the reads (1) to
(10) in order: `CLAUDE.md`'s six session-start spans (in context at boot), `STATUS.md`, `DECISIONS.md` whole,
`BUILD_AND_TEST.md`, the gating identities; the dispatch-protocol section of `cowork_audit_protocol.md` whole; the three
ruling records whole; the phase-definition surface §0 and §3.4; `FRAMEWORK.md` §5 from *L0* to the end of *The boundary
contracts*; the brief's §2, §4 and §7; the boot pack's `subjects → l2 → counted`, `THE_WITHHELD_FAMILY` (identities,
documents, passages) and `LEAKS`, whole (113 identities, 21 documents, 6 passages, 2 leaks); entry 277 whole;
`the_tabulation_population`, position 62 the last entry of `the_members`; and the reading file at the ranges read (10)
names — save §10, read at its head only (§5, departure 3). Not read: the L0/L1 reading file, the outgoing texts, the
fourteenth report.

**0(a) — the pin.** `git hash-object -w` of the dispatch: blob **`425081e5e09378b3b7986117bd1b264b5f3ddf09`**, 172,405
bytes (entry 277's listing); proved unmoved immediately before staging (the same hash, printed again).

**0(b) — the refs and the chain.** Both ref files read `5aa808b736207da82e64aff6962520ee5eee8225` before Task 0. The
chain at the objects (Appendix C.8): **`5aa808b7…`** — *"Close: the L2 tabulation at position 62 and its sections so
far, under its dispatch"*, parent `c3cd3ba4…`, carrying `STATUS.md`, `STATUS_ARCHIVE.md`, the fourteenth report,
`defense_share.json`, `gen_status_batch_bound.py`, `guard_state.json`, `l2_outgoing_population.json`,
`session_start_read_size.json` and `status_batch_bound.json`; **`c3cd3ba4…`** — member 62, the reading file only, parent
`7c0e8ee9…`; **`7c0e8ee9…`** — the fourteenth dispatch and entry 276, parent `57a4293e…`. The relayed chain holds. (The
FACT listed the reading file and the two Task-0 records among the close set "before the report was added"; at the
object they are in the member and Task 0 commits, and the close carries the fourteenth report itself — the close set is
otherwise as relayed.)

**0(c) — A1.** `tools/audit/changed_paths.py`, whole at Appendix C.1: **one tracked modification**,
`tools/audit/claude_md_finer_archive.json`; the two landed paths untracked (each confirmed by `git ls-files --others
--exclude-standard`); the standing untracked population. Nothing staged: the index tree equalled the tip's tree,
`abd2bc901f0ced4ed9a11e9cda5ce3c404a6ab64` both. **A1 holds.**

**0(d) — the last bytes** (Appendix C.2): both landed files end on the newline byte, no zero byte, no carriage return.

**0(e) — the commit.** Exactly the two paths, the staged tree `9bfbdf702a454ffe9d75608a94b321a5fed2004f` differing from
the tip's tree in those two paths alone; commit **`92a1159f875a8ef1f1eebdb0d3e55bbb23d820ee`**, parent `5aa808b7…`,
subject *"record: entry 277 and the fifteenth L2 tabulation dispatch"*; pushed; both ref files read `92a1159f…`.

**0(f) — the opening guard capture** (Appendix C.3a), under Git Bash 5.2.37, `PYTHONIOENCODING` unset, `PYTHONUTF8`
unset, Python 3.14.3: **80 run, 12 failing — exactly A2's twelve — 4 not run, 19 historical**;
`gen_evidence_pin_membership.py --check` PASSES. The classification (C.3b) STOPs naming exactly the four carried tools.
**A2 holds.**

**0(g) — the three blobs.** At `92a1159f…` the derivation is `d78ac530992860d38d1f605a77a2961d5440a2f6` (125,549 bytes)
and the brief `c5ff83dcad2107ac8c05ead21724cbab0d9471fd` (35,952 bytes); at `5aa808b7…` the reading file is
`a77405a2d324cf17f590e4ac98c6f0967bc58235` (4,393,194 bytes); the working copies hash to the same three. Every scratch
copy below was extracted from these blobs by explicit hash.

**E0: met** — two paths in one commit; `origin/master` at it; the pin proved; A1 enumerated; the capture against A2; the
three blobs verified.

## 2. Task 1 — the four once-written sections

### 2.1 The capacity judgments, quoted from the log

The log is whole at Appendix A. In short: before **§7** — 4642 row headings counted at the blob, §13's 5481 statements
and 5541 verdicts, generated not hand-written, *"I can finish §7 whole"*; before **§8** — eighteen questions, scripted
searches, *"I can finish §8 whole"*; before **§9** — five points, *"I can finish §9 whole"*; before **§14** — 203 lines
of the derivation's §6 relayed by script, *"I can finish §14 whole"*. **The §14 judgment corrects my own log**: the §7,
§8 and §9 judgments called that span *222 lines*, an estimate never read at the file; read at the blob it is 203 (lines
1389 to 1591). Each judgment says whether the context had been compacted; none had.

### 2.2 Compaction

The context was not compacted at any point of the batch.

### 2.3 The four section commits

| Section | Commit | Parent | Tree | Reading-file blob | Bytes |
|---|---|---|---|---|---|
| §7 | `a7ff25d189f16891bebc358ae7d1c3c5d5367227` | `92a1159f…` | `4d296c412a9af69f106962f59f63e2354f702639` | `feff1df77f4db5d4ed9a87132ebeb69704fc6d86` | 4,419,982 |
| §8 | `9046ead50a8e9a6423aad96863b97e54db316aa4` | `a7ff25d1…` | `90771c5570d570eb4ab9cf9f043b6f04e0511bb3` | `cd089cb4a95811768e57f7bc2b16b08e1c54eac3` | 4,435,006 |
| §9 | `e2f37ff740794ae8dbcb148a7ff65556a92d2337` | `9046ead5…` | `d049251d1ba874dd81d977236022efa5265f7dbd` | `3cd269c633748345b57f360be6ca2ff225320cbc` | 4,438,371 |
| §14 | `2e17c3be2a998b2895e9d2afbdbb84f7d5db81a8` | `e2f37ff7…` | `9d0355218bce53c6f3f0da246add891ab0526e7a` | `4c15b9338895e092c017223acaece9d8324db41d` | 4,451,292 |

Each commit carries the reading file alone, proved by the staged tree's name-status against the previous commit's tree;
each subject is the dispatch's, verbatim; each was pushed and both ref files read equal to it; each working copy hashed
to the scratch build's blob before staging. At §7's commit the banner clause and the one clause on the fourteenth batch
were applied; at every commit §0's sentence on this batch and on the once-written sections, and §16's last clause, were
brought true — the build checks print each changed passage (Appendices B.1c, B.2f, B.3f, B.4e).

### 2.4 §7 — the generating script, and its output

The fourteenth batch's scratch `rowparse.py` and `gen_s7.py` (in that batch's scratch directory, `917d1e1e…`) survived
and were copied with the file tools into this batch's scratch, each change stated at §2.7. **The one change to the
counting:** `rowparse.split_axis` reads a claim mark followed by *" to (x)"*, or by *", (y) … and (z)"* or *" and (y)"*,
later claims in ascending order, as ONE written verdict standing for every claim from the first to the last, and the
generator counts it once per claim. The output, whole, is Appendix B.1a: 4642 rows parsed; **the range- or list-form
axis paragraphs read: Row 17.29, claims (i) to (iv), four counted; Row 17.52, claims (iii) to (v), three counted — and
no other**; rows with no axis, by design: 52, member 62's 49 pointer rows and 3 flagged items, printed by number and
contributing nothing; rows whose heading parses but whose axis or claims cannot be read: **none**; the same statement and
verdict twice inside one claim: none. **The four equations: AGREES 1011 = 1011, DIFFERS 858 = 858, THE DERIVATION IS
SILENT 3672 = 3672, total 5541 = 5541 — all True**; no member's parsed counts differ from its §13 row; member 17 parses
at 23 / 14 / 92, its §13 row. The fourteenth dispatch's prediction is met; it was not a target, and the script was not
adjusted to reach it. One derived statement, **L2-S46**, is named by no row under either verdict, and its entry reads
THE OUTGOING TEXT IS SILENT. **Titles:** the derivation gives its statements no separate titles, so each entry quotes the
statement's first sentence and §7 says so; all 49 were checked at the derivation's blob, each directly after its own
*"L2-Sn. "* (B.1b).

### 2.5 §8 and §9 — the search terms, and the rows each found

The searches are `s8search.py` over every row's *Outgoing statement.* quotation at the blob `a77405a2…` — three passes
for §8 (the first with six hits printed per term; a second, sharper pass; a third printing every hit of *pivot*,
*successor*, *grace* and *NCT* so that a sentence saying none of those rows says something is drawn from all of them) and one
for §9; their outputs are whole at Appendices B.2a to B.2c and B.3a. Each hit was read in the quotation the search
printed for it (the row's own quoted words, with up to about two hundred characters around the match); every quotation
a sentence carries was then checked at its row by the short-quotation check. The terms, and the rows each sentence
names:

| Entry | Search terms | Rows named in the sentence |
|---|---|---|
| OQ-L2-1 | added sixth; ninth; eleventh; double sharp / flat / accidental; chord vocabulary; closure / ceiling; an applied chord's chain or depth | 6.33, 6.85, 1.8 |
| OQ-L2-2 ★ | Dorian / Phrygian / Mixolydian; modal; twenty-one / 21 modes / two modes / composite minor | 7.42, 7.48, 48.29, 49.31 |
| OQ-L2-3 | segment cap / length cap / seg_cap; Lerdahl / Weber; recency; signature, weak or soft prior | 10.32, 17.10, 48.13, 48.48, 48.50 |
| OQ-L2-4 ★ | appoggiatura; escape tone / échappée; retardation; pedal point | 13.3, 48.45, 6.91 |
| OQ-L2-5 ★ | pivot (all twenty hits) | 10.43, 30.58, 30.60 |
| OQ-L2-6 | stops changing / converge; in-selection output / stop condition | 45.12, 45.14, 2.47 |
| OQ-L2-7 | retardation / suspension; restat-; grading near boundary; re-annotation / same chord | 5.100, 43.150 |
| OQ-L2-8 ★ | exact decode / beam / tractab- / prune; very large / large scores / orchestral | 1.8, 1.11, 10.52 |
| OQ-L2-9 | chordal voice / successor / following note / next note (all seventeen hits); chord-bearing / chordal | 46.26, 46.75 |
| OQ-L2-10 | grace (all sixteen hits) | 23.336, 43.125, 44.15 |
| OQ-L2-11 | lowest sounding / lowest pitch / lowest note | 5.32, 23.292, 10.17 (claim (ii)) |
| OQ-L2-12 | cue window / look-back / fourth and seventh (all three hits); window | 10.34, 5.93, 7.156 |
| OQ-L2-13 | NCT / non-chord-tone ground truth, annotation, labels (all thirty-nine hits) | 3.11, 13.1 |
| OQ-L2-14 | calibrated probability / margin class / Class M; full posterior | 9.22, 6.127, 7.13, 47.22 |
| OQ-L2-15 | top-K / capped / no truncation / threshold with alternatives; full candidate list / full posterior | 49.23, 49.22, 6.192 |
| OQ-L2-16 ★ | unfold / volta / notated order / performed order; repeat (all twenty hits) | 5.39, 40.50, 44.7 |
| OQ-L2-17 | enharmonic | 2.50, 2.51, 5.346 |
| OQ-L2-18 | pedal; pedal point | 24.92, 8.104, 6.125 |
| Point 1 | one decode / jointly / entangled / decided together (all eleven hits) | 48.44, 48.3, 39.185 |
| Point 2 | exact decode / Viterbi / beam / search (the first twenty-five of eighty-seven hits) | 1.9, 1.8, 1.14 |
| Point 3 | unfold / notated order / repeat (all twenty hits) | 5.39, 40.50, 44.7 |
| Point 4 | non-chord-tone or chord-tone with ground truth or annotation (all six hits) | 3.11, 6.146 |
| Point 5 | grading with boundary or label / retardation label / restated chord (all seventeen hits) | 40.9 |

Where a sentence says that none of the rows a search found speaks to something, every hit of that search was read (the
table says *all*); the Point 2 sentence, which read the first twenty-five of eighty-seven hits, makes no such claim. The
★ marks stand only at the heads of OQ-L2-2, 4, 5, 8 and 16 inside the quotations, taken from the derivation; this
file's own prose carries no ★ (B.2d). No sentence judges, recommends or answers; none says whether the derivation's §7 is
right.

### 2.6 §14

The derivation's §6.1 to §6.6 — 203 lines — relayed in a block quote, each line prefixed, each subsection under its own
heading as the derivation heads it; **byte-for-byte equal to the blob `d78ac530…`'s span with the prefixes removed**
(B.4c), each §6.k heading present once, and none of *independent*, *contaminated*, *clean*, *compromised*,
*established* in this file's own prose of §14 (B.4b). **The SEEN sentence** names Row 15.19, Row 17.5 (claim (i)), Row
17.14 and Rows 45.7 to 45.15, found by a scripted search of every foot's *SEEN rows:* line — 62 such lines, three naming
rows (§6.15's, §6.17's and §6.45's), 59 reading none (B.4a) — and read at those three feet. The wider-check sentence
is kept, its opening words changed to *"Stated here because it bound every row:"*, the remainder unchanged.

### 2.7 The checks, and every change to a script

**The consistency script's first run over the committed reading file at `a77405a2…`** (B.0a): *"rows parsed: 4642;
travelling refs checked: 2464; as-at refs checked: 861; flags: 0"* — it flags nothing. Proved before that first use on
two planted faults, both flagged (B.0b). It was then run over each built file before its commit and flagged nothing
each time (B.1e, B.2h, B.3h, B.4g). **Its reach into §7, §8, §9 and §14 is nil**: it parses only `**Row M.N — `
headings, none of the sections carries one (the parsed count stays 4642), and none carries a *travelling with* or an
*as at*. The script itself was not changed between runs; its only differences from the fourteenth batch's are the
scratch path and the removal of an unused `--only-members` option.

**The quotation check against the derivation** (`qcheck.py`, new): proved before its first use at each section by one
quotation altered in a copy and reported (B.1b, B.2e, B.3e, B.4c); no failure in any real run. **The short-quotation and
count check** (`shortq.py`, new): for §8, 55 quotations checked at their rows and 55 row names checked to exist; for
§9, 9 and 12; proved by one altered quotation reported (B.2d, B.3d). **The build check** (`build_check.py`, rewritten
from the fourteenth batch's member form for a section): at every commit the §6.1–§6.62 span identical (3,998,446
characters each side), the changed passages outside the section exactly the banner (at §7 only), §0's stop paragraph and
§16's last bullet, the built file ending on a newline with no carriage return. **The word scan** (`wordscan.py`, the
fourteenth batch's, now also dropping block-quoted lines and listing *judgement*): §7 0 hits; §8 eight hits on its
first run — *centre* reworded to *center*, the other seven read by eye as musical senses (*added notes*, *double flat*,
*large scores* and *following note* / *next note* as search terms, *tritone resolution*, *key-span*) — and seven on the
second run, the same seven; §9 0; §14 0; every changed §0/§16 text 0; the `STATUS.md` entry three, read by eye
(*decisions register* twice, qualified; *corpus of scores*, musical).

**Every other script change, stated:** `rowparse.py` gained `split_axis` and now also records per row its range groups,
whether it has an axis and its block; `split_claims`, which the consistency check reads dispositions through, is
unchanged. `gen_s7.py` re-aimed to this scratch, prints the range-form rows, the rows with no axis, the unreadable rows
and duplicate pairs, and writes each entry as *AGREES (n): Rows …* / *DIFFERS (n): …*. `assemble.py` (new) — an unused
line removed before its first run; after §9's first assembly printed *"§14 stay NOT YET WRITTEN"*, read by eye in the
build check's output, the verbs were made to agree with the count and §9 was re-assembled before its commit (the kept
build check is the second run). `s8data.py` — *centre* to *center*. `gen_s8.py` — its introduction's ★ glyph was
replaced by words before the first check, so that this file's own prose carries no ★, and `shortq.py`'s exemption for
it was removed. `s9data.py` — Point 3's sentence reworded for grammar after its first check; re-checked. `gen_s14.py` —
its first run counted one foot line, §6.1's *"SEEN rows: none** — no SEEN home lies in this member."*, as naming rows;
the pattern was widened to that form of *none* and the run repeated, giving three and 59. `s8search.py` gained the
second and third query sets. `cmp_artifacts.py` is the fourteenth batch's unchanged but for its header; `gcompare.py` is
re-aimed and reads the new `guard_state.json` at its blob rather than in the working tree.

### 2.8 A5 after every section commit

Each section's blob against `a77405a2…`, both extracted by explicit hash, trailing newlines trimmed: **§6.1 to §6.62,
§1 to §5, §10 to §13 and §15 identical** at `feff1df7…`, `cd089cb4…`, `3cd269c6…` and `4c15b933…` (B.5).

**E1: met** — each section whole, in its own commit, in 1(e)'s form and in the order §7, §8, §9, §14, §7 first; §7's
four equations holding with its range-form rows printed; §8's and §9's sentences naming rows that exist, the search terms
in §2.5; §14 relayed whole with no verdict word and its SEEN sentence naming the rows of the three feet; §0 and §16 true
of the file at each commit; each capacity judgment written out before its section and logged; no recommendation; no row
of §6.1 to §6.62 and nothing in §10 to §13 edited; A5 intact.

## 3. Task 2 — the close

**2(a).** The `STATUS.md` pointer entry was written first, the `Last updated: ` prefix moved to it from the fourteenth
batch's entry, and word-scanned (§2.7).

**2(b).** `STATUS.md`'s object was the same blob, `8361f6736e6df6aa49e4a947199c75d51286eb29`, at `92a1159f…`, at
`5aa808b7…` and in the tree before the entry was written. The five authored constants were re-aimed — `BASE_COMMIT`
`92a1159f…` (was `7c0e8ee9…`), `PREVIOUS_BATCH_DISPATCH` the fourteenth dispatch (was the thirteenth), `ACT_DATE`
`2026-10-04` (unchanged; the move ran on the dispatch's date), `DISPATCH` this dispatch (was the fourteenth), `TASK`
`"Task 2"` (unchanged) — each former value named in its comment, `MOVE_KIND` `"ordinary"`, and this batch's aiming
appended to `PREVIOUS_AIMINGS`. The `BASE_COMMIT` edit did not match at its first attempt (the comment line above it
begins *"# THE ENTRIES EXPECTED"*); it was re-applied, and all five were read back at the tool source before `--apply`.
`--apply` and `--check` (C.5a, C.5b): **one entry moved, 2,591 characters**, byte-present in the archive exactly once,
absent from the must-read. **Read at the files:** the entry moved is the fourteenth batch's, now at `STATUS_ARCHIVE.md`
under a header naming this dispatch's Task 2, without its prefix; the two 2026-09-02 entries stay in `STATUS.md`.

**2(c).** The five regenerations and their `--check` runs, `PYTHONUTF8` unset, all exit 0 (C.6). Compared with the
blobs at `2e17c3be…` (C.7): `evidence_pin_membership.json` and `l0_l1_outgoing_population.json` **identical**;
`l2_outgoing_population.json` moved only in `STATUS.md`'s residue record and the tally — **two terms moved, *boundary*
−1 and *struck* −1, each equal to its change in that record's hit records** (the outgoing entry carried both; this
batch's entry carries neither); every other field identical; **`the_tabulation_population → the_members` identical by
that path, 62 and 62**; the residue file list identical. `defense_share.json` and `session_start_read_size.json` moved
only in `STATUS.md`'s new size. **A3 holds.**

**2(d).** The closing capture under the opening capture's environment (C.4a): identical to the opening one verdict for
verdict — population 80, the same twelve FAIL, the NOT RUN and HISTORICAL lines identical; the artifact's `summary`
identical and its 80 per-tool verdicts read at `runs` identical (C.4c); the classification STOPs naming exactly the four
tools (C.4b).

**E2: met** — population 80; zero STOPs in the runner; the failing set exactly the twelve, plus none; the
classification STOP unchanged.

**The close set, staged before this report was added, against the tip's tree and against `5aa808b7…`'s** (C.9): the
eight Task 2 files, and over the whole batch nothing beyond the reading file, the two records, `STATUS.md`,
`STATUS_ARCHIVE.md` and the six audit files; the derivation and the brief stand at `d78ac530…` and `c5ff83dc…` in that
tree.

## 4. E0, E1, E2 and A1 to A5, each checked

- **E0** met (§1). **E1** met (§2.8). **E2** met (§3).
- **A1** holds: exactly one tracked modification at boot, the two untracked records, the standing population (C.1).
- **A2** holds: exactly the twelve at the opening capture, `gen_evidence_pin_membership.py --check` passing (C.3a).
- **A3** holds term by term, the members identical by path (C.7).
- **A4** holds: one tool source touched, `gen_status_batch_bound.py`'s authored aiming; no tool added or enrolled;
  population 80 throughout.
- **A5** holds: after every section commit (B.5) and at the close (C.9) — the derivation, the brief, the pack, the boot
  pack artifact, the input contract, the L0/L1 reading file, every outgoing text, the five named tools, every governing
  document but `STATUS.md` and `STATUS_ARCHIVE.md`, both registers' sources and the fourteenth report absent from the
  batch's difference; the reading file's §6.1 to §6.62, §1 to §5, §10 to §13 and §15 byte-identical.

## 5. Declared departures

1. **The dispatch before the derivation.** The opening instruction named only the dispatch, and its first 580 lines were
   read before the derivation; the remainder after. `CLAUDE.md` and the auto-memory index were in context at boot.
2. **The boot pack's `derived_cross_reference_additions`** (between `passages` and `LEAKS`) was not read; read (7) does
   not name it.
3. **§10 was read at its head only** (its opening paragraph and first entries), not whole as read (10) orders. Nothing
   in §10 was edited, A5 proves it byte-identical, and none of the four sections draws on it.
4. **A hash in a shell variable, once:** the new `STATUS.md` blob's hash was passed through `H=$(…)` to extract the
   entry for the word scan; the guard did not deny it. A few commands also assigned unused path variables (`P=…`,
   `O=…`) while writing every path literally.
5. **The by-eye reads of search hits** were of the quotation each search printed for its hit (§2.5), not a separate
   read of each row block; every quotation a sentence carries was then checked at its row by script.
6. **A long build check ran past the shell tool's foreground limit** once (§7's first) and finished in the background;
   later ones were given a longer limit.
7. **Scratch scripts ran with `PYTHONUTF8=1`**, as the dispatch permits; the guard runner and every repository tool ran
   without it.
8. **One `git add` carried `2>/dev/null`**, suppressing git's line-ending warnings at the close staging; the staged set
   was proved by tree afterwards.

## 6. The targeted reads of §6.1 to §6.62 under read (10), named

Read directly with the file tools: Rows 1.1 to 1.3 (the row shape), §6.62 whole, Rows 17.29 and 17.52 whole, §6.17's
foot, and §6.1's *SEEN rows:* line. Read in the quotation a search printed (§2.5): every row in the search outputs at
Appendices B.2a to B.2c and B.3a; the rows the sentences quote are the twenty-three entries' rows of §2.5's table. No row
of §6.1 to §6.62 was otherwise read, and none was edited.

## 7. Findings and observations

**No finding under 1(h) or the Findings section.** §7's equations held; no row was unreadable; no derived statement,
open question or §7 point was missing at the derivation's blob. Observations needing no act:

1. **The range form is confined to Rows 17.29 and 17.52**, as the fourteenth report found; this batch's parser, which
   also reads a list form, found no third.
2. **L2-S46 is the one derived statement no row names under either verdict** (§7's entry reads THE OUTGOING TEXT IS
   SILENT); §8's OQ-L2-16 and §9's Point 3, on the order the analysis works in, find no row on it either. Recorded as
   what the rows carry, not as a judgment.
3. **One foot writes its *none* in a second form** (§6.1's *"SEEN rows: none** — …"*); harmless, left at its site.
4. **§0's sentence at the §9 commit read *"§14 stays NOT YET WRITTEN, to be written once each"*** — the dispatch's
   template wording, true and replaced at §14's commit.
5. **My own log's span estimate** (*222 lines*) was corrected in the §14 judgment (§2.1).

## 8. What this batch did not do, and the plan's tell

It tabulated no member, wrote no row, gave no disposition and derived no mark; edited no row of §6.1 to §6.62, nothing
in §10 to §13, §1 to §5 or §15; edited no outgoing text, derivation, brief, pack, boot pack artifact, input contract,
L0/L1 reading file, source of the decisions register or of the open-items register, or governing document but `STATUS.md` and `STATUS_ARCHIVE.md`; touched no tool
source but the forward bound's authored aiming; booted no session; built, ran or designed no measurement of the analysis;
created, flipped or discarded no open-items row; allocated no decisions-register identity; put none of the five
questions; recommended nothing. **§0's sentences on the earlier batches stand unchanged by this batch's commits save the
one clause 1(f) adds to the fourteenth batch's sentence — nothing struck.** **The plan's tell: this batch produced
nothing other than the landed records, the four once-written sections with their §0 and §16 updates, the one clause
added to §0, the one banner edit, the Task 2 files and this report.**

## 9. The self-check, over the work on disk

1. *Principles.* **#19** — §7 is generated and reconciled by four printed equations, and every authored quotation is
   checked at its source by script with a proof run first; no verdict word on the independence record. **#6** — §7
   restates no outgoing sentence, pointing at rows; §8 and §9 quote rows rather than the source documents; the
   derivation's words are quoted once, from its blob. **#12** — nothing struck; the former wordings stand in git; the
   one §0 clause adds. **#13** — the STOP at §7 was armed and did not fire. **#10** — §0 and §16 made true at each commit.
   **#17(f)/D-431** — the counts this report gives are the check outputs' own, quoted from the appendices; the
   `STATUS.md` entry restates none. **#24** — no difference between measured quantities is asserted.
2. *Conventions.* American English (*center*, *analyzer*); the word scans' hits read and either reworded or recorded as
   musical senses. This report's own prose was scanned too: 25 hits on the first run, of which four non-musical uses
   were reworded (*rests on*, *the rest* twice, a bare *register*) and one heading word (*Figures*); the second run's 22
   hits are musical senses, mentions of the scanned words themselves, or *register* in its qualified forms. No label
   invented without explanation (*the range form*, *a once-written section*, *a pointer row*
   are the dispatch's).
3. *Quantities and premises.* Every count is quoted from a check output kept verbatim below; premises are cited to the
   object they were checked at.
4. *File-tools rule.* Working-tree files were read with the file tools; the shell ran git object queries by explicit
   hash, the named audit tools and scratch scripts with literal paths, save the departure at §5 item 4.
5. *Uncertainty.* Not engaged: no comparison between measured quantities is made.

---

## Appendix A — the capacity log, whole

### Task 1(h)

*Saved to scratch as `capacity_log.txt`.*

```
CAPACITY JUDGMENT BEFORE §7 (Task 1(h)), written out in the session before §7 was opened.
§7 — the derived side. What it gathers: by a scratch script over the blob a77405a2… extracted to scratch, every row of §6.1 to §6.62 — 4642 row headings, counted at that copy just now by a search for the `**Row M.N — ` heading — reconciled to §13's totals as they stand at the same blob, read at the file and verified by hash: 5481 statements and 5541 verdicts (AGREES 1011, DIFFERS 858, THE DERIVATION IS SILENT 3672). It is generated, not hand-written: one entry per L2-S1 to L2-S49, each a title quoted from the derivation's blob plus the rows by number. The fourteenth batch's generation ran in seconds; the one change I make is to its parser, counting a range- or list-form verdict once per claim.
Whether the context has been compacted: NO. No earlier log entry exists — this is the batch's first judgment. The context now carries the ordered reads and Task 0.
What the batch owes after §7: §8 (eighteen questions, each with an authored sentence built by search), §9 (five points), §14 (the derivation's §6, 222 lines, relayed by script extraction), then the whole close (STATUS entry, forward bound, five regenerations, the A3 tally check, the closing guard capture, the report with its appendices).
JUDGMENT: I can finish §7 whole. Its cost is a script and its checks, not reading, and there is room for the sections after it and the close. If the four equations fail, the first-unit rule stops the batch with nothing committed to the reading file.

CAPACITY JUDGMENT BEFORE §8 (Task 1(h)), written out in the session before §8 was opened, after §7 was committed (a7ff25d1…) and A5 held for it.
§8 — the eighteen open questions OQ-L2-1 to OQ-L2-18, counted at the derivation's blob (when read whole, and again by the §8 quotation check's own count). Each question is quoted verbatim in a block quote and checked against d78ac530…; each gets ONE authored sentence naming the rows of §6.1 to §6.62 whose outgoing statements speak to its subject, found by a scripted search over the committed blob with the terms named in the report and read at the row; short quotations in those sentences are checked against the rows' Outgoing statement quotations.
Whether the context has been compacted: NO. My log, read rather than remembered, holds one earlier entry (the §7 judgment).
What remains after §8: §9 (five points, the same method), §14 (a scripted relay), and the whole close.
JUDGMENT: I can finish §8 whole. The searches are scripted and their outputs bounded; the cost is reading about eighteen short hit lists plus a few rows, which leaves room for §9, §14 and the close. If my reading shows the tells of 1(g), I stop at the §8 boundary and commit nothing of it.

CAPACITY JUDGMENT BEFORE §9 (Task 1(h)), written out in the session before §9 was opened, after §8 was committed (9046ead5…) and A5 held for it.
§9 — the derivation's §7, its five points, counted at the derivation's blob by the quotation check's own count. Each point is quoted verbatim in a block quote and checked against d78ac530…, followed by ONE authored sentence on what the tabulated outgoing text says to it, built as §8's were (a scripted search over the rows' quotations, the hits read at the row, short quotations checked at the rows); no verdict on whether the derivation's §7 is right.
Whether the context has been compacted: NO. My log holds two earlier entries (the §7 and §8 judgments).
What remains after §9: §14 (a relay extracted by script and checked byte for byte), then the whole close.
JUDGMENT: I can finish §9 whole — five points against §8's eighteen, with the same scripts — and leave room for §14 and the close.

CAPACITY JUDGMENT BEFORE §14 (Task 1(h)), written out in the session before §14 was opened, after §9 was committed (e2f37ff7…) and A5 held for it.
§14 — the independence record, relayed: the derivation's §6.1 to §6.6, read at the derivation's blob from line 1389 ("### 6.1 What reached this session, and how") to line 1591 — 203 lines — relayed whole in a block quote, extracted by script and checked byte for byte against d78ac530…; one sentence naming the rows with a SEEN mark, found by a scripted search of every foot's SEEN rows line; and the section's existing wider-check sentence kept, its opening words changed as 1(e) orders.
A correction to my own log: my §7, §8 and §9 judgments called this span "222 lines"; that was an estimate, not read at the file. It is 203.
Whether the context has been compacted: NO. My log holds three earlier entries.
What remains after §14: the whole close.
JUDGMENT: I can finish §14 whole — a scripted relay and two sentences — and the close after it.
```

## Appendix B — the once-written sections' check outputs

### B.0a — the consistency script's first run over the committed reading file at a77405a2

*Saved to scratch as `consistency_first.txt`.*

```
rows parsed: 4642; travelling refs checked: 2464; as-at refs checked: 861; flags: 0
```

### B.0b — the same script over two planted faults (the proof, run before the first use)

*Saved to scratch as `consistency_planted.txt`.*

```
rows parsed: 4642; travelling refs checked: 2464; as-at refs checked: 861; flags: 2
FLAG Row 48.1(i) [ADOPTED — carried]: travelling with Row 48.2(ii) whose disposition(s) are ['HISTORICAL']
FLAG Row 48.11: L2-S34 DIFFERS as at Row 10.14(v), which carries [('L2-S34', 'AGREES')]
```

### B.1a — §7: the generating script's output, whole

*Saved to scratch as `gen_s7_run1.txt`.*

```
rows parsed in §6: 4642
rows with no axis, by design (member 62's pointer rows and flagged items): 52
    62.1, 62.2, 62.5, 62.6, 62.7, 62.8, 62.9, 62.10, 62.11, 62.12, 62.13, 62.14, 62.15, 62.16, 62.17, 62.18, 62.19, 62.20, 62.21, 62.22, 62.23, 62.24, 62.25, 62.26, 62.27, 62.28, 62.29, 62.30, 62.31, 62.32, 62.33, 62.34, 62.35, 62.36, 62.37, 62.38, 62.39, 62.40, 62.42, 62.43, 62.44, 62.45, 62.46, 62.47, 62.49, 62.50, 62.51, 62.52, 62.53, 62.54, 62.55, 62.56
range- or list-form axis paragraphs read: 2
    Row 17.29: claims (i) to (iv) written as one verdict -> 4 claims counted
    Row 17.52: claims (iii) to (v) written as one verdict -> 3 claims counted
rows whose heading parses but whose axis or claims cannot be read: 0
same statement and verdict written more than once inside one claim: 0
L2-S1: AGREES 31, DIFFERS 24
L2-S2: AGREES 16, DIFFERS 7
L2-S3: AGREES 18, DIFFERS 0
L2-S4: AGREES 32, DIFFERS 17
L2-S5: AGREES 4, DIFFERS 1
L2-S6: AGREES 14, DIFFERS 22
L2-S7: AGREES 3, DIFFERS 2
L2-S8: AGREES 2, DIFFERS 8
L2-S9: AGREES 6, DIFFERS 0
L2-S10: AGREES 17, DIFFERS 12
L2-S11: AGREES 23, DIFFERS 168
L2-S12: AGREES 13, DIFFERS 3
L2-S13: AGREES 25, DIFFERS 5
L2-S14: AGREES 12, DIFFERS 13
L2-S15: AGREES 8, DIFFERS 0
L2-S16: AGREES 11, DIFFERS 5
L2-S17: AGREES 24, DIFFERS 25
L2-S18: AGREES 21, DIFFERS 21
L2-S19: AGREES 0, DIFFERS 1
L2-S20: AGREES 18, DIFFERS 32
L2-S21: AGREES 3, DIFFERS 0
L2-S22: AGREES 78, DIFFERS 21
L2-S23: AGREES 31, DIFFERS 23
L2-S24: AGREES 12, DIFFERS 13
L2-S25: AGREES 9, DIFFERS 7
L2-S26: AGREES 2, DIFFERS 2
L2-S27: AGREES 31, DIFFERS 21
L2-S28: AGREES 15, DIFFERS 2
L2-S29: AGREES 1, DIFFERS 4
L2-S30: AGREES 18, DIFFERS 9
L2-S31: AGREES 17, DIFFERS 22
L2-S32: AGREES 23, DIFFERS 8
L2-S33: AGREES 3, DIFFERS 1
L2-S34: AGREES 43, DIFFERS 60
L2-S35: AGREES 3, DIFFERS 54
L2-S36: AGREES 10, DIFFERS 14
L2-S37: AGREES 14, DIFFERS 6
L2-S38: AGREES 73, DIFFERS 65
L2-S39: AGREES 8, DIFFERS 1
L2-S40: AGREES 52, DIFFERS 65
L2-S41: AGREES 6, DIFFERS 2
L2-S42: AGREES 8, DIFFERS 12
L2-S43: AGREES 20, DIFFERS 15
L2-S44: AGREES 6, DIFFERS 14
L2-S45: AGREES 19, DIFFERS 24
L2-S46: AGREES 0, DIFFERS 0
L2-S47: AGREES 19, DIFFERS 2
L2-S48: AGREES 29, DIFFERS 1
L2-S49: AGREES 160, DIFFERS 24
EQUATION 1 AGREES: 1011 = 1011  -> True
EQUATION 2 DIFFERS: 858 = 858  -> True
EQUATION 3 SILENT: 3672 = 3672  -> True
EQUATION 4 TOTAL: 5541 = 5541  -> True
members whose parsed counts differ from §13's row: 0
member 17: parsed AGREES/DIFFERS/SILENT [23, 14, 92] ; §13 (23, 14, 92)
statements no row names under either verdict: L2-S46
```

### B.1b — §7: the quotation check's proof (one title altered), then the titles checked at the derivation

*Saved to scratch as `qcheck_s7_proof.txt`.*

```
altered one quotation: 'The applied target is a chain, not a single field.' -> 'The applied target is a list, not a single field.'
titles checked: 49 | numbers in order 1..49: True
FAILURES: 1
FAIL L2-S5: title not found in the derivation: The applied target is a list, not a single field.
```

*Saved to scratch as `qcheck_s7.txt`.*

```
titles checked: 49 | numbers in order 1..49: True
FAILURES: 0
```

### B.1c — §7: the build check (built on a77405a2)

*Saved to scratch as `build_check_s7.txt`.*

```
§6.1 to §6.62 span identical (trailing newlines trimmed): True 3998446 3998446
--- changed passage 1: replace base lines 11-11 -> new lines 11-11
  - > `records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md` Task 1, executing
  + > `records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md` Task 1, and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md` Task 1, executing
--- changed passage 2: replace base lines 146-146 -> new lines 146-146
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 and 42, each whole in its own commit, and stopped by its own capacity judgment to leave room for the close. The ninth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md`, opened with position 43 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 44 and 45, each whole in its own commit, and stopped by its own capacity judgment, written before position 46 was opened, to leave room for its correction commit and its close. The tenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md`, opened with position 46 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 47 and 48, each whole in its own commit, and stopped by its own capacity judgment, written before position 49 was opened, to leave room for the close. The eleventh batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`, opened with position 49 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 50 whole in its own commit, and stopped by its own capacity judgment, written before position 51 was opened, to leave room for the close. The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 52 whole in its own commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close. The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there. The fourteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`, opened with position 62 as that dispatch ordered (**D-670**) and tabulated it whole in one commit. §7, §8, §9 and §14 stay NOT YET WRITTEN, to be written once each, in the order §7, §8, §9, §14. **A member marked NOT YET TABULATED is UNTOUCHED** — not
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 and 42, each whole in its own commit, and stopped by its own capacity judgment to leave room for the close. The ninth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md`, opened with position 43 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 44 and 45, each whole in its own commit, and stopped by its own capacity judgment, written before position 46 was opened, to leave room for its correction commit and its close. The tenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md`, opened with position 46 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 47 and 48, each whole in its own commit, and stopped by its own capacity judgment, written before position 49 was opened, to leave room for the close. The eleventh batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`, opened with position 49 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 50 whole in its own commit, and stopped by its own capacity judgment, written before position 51 was opened, to leave room for the close. The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 52 whole in its own commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close. The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there. The fourteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`, opened with position 62 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, and stopped at the section boundary after position 62 because §7's generated reconciliation to §13 did not hold, which that dispatch's Task 1(e) made a STOP (the difference located by row in `records/cc/reports/cc_report_l2_comparison_tabulation_fourteenth_2026_10_04.md` §2.7). The fifteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md`, opened with §7 as that dispatch ordered (**D-670**) and wrote it whole in its own commit. §7 is written; §8, §9 and §14 stay NOT YET WRITTEN, to be written once each, in the order §7, §8, §9, §14. **A member marked NOT YET TABULATED is UNTOUCHED** — not
--- changed passage 3: replace base lines 74277-74277 -> new lines 74277-74277
  -   once-written sections — §7, §8, §9 and §14 — stand as §0 says: §7, §8, §9 and §14 are NOT YET WRITTEN.
  +   once-written sections — §7, §8, §9 and §14 — stand as §0 says: §7 is written; §8, §9 and §14 are NOT YET WRITTEN.
changed passages outside the section: 3
section lines: base 6 -> new 274
base section still NOT YET WRITTEN: True | new section NOT YET WRITTEN: False
ends with newline: True no CR: True
```

### B.1d — §7: the word scans — the section's own prose, then the changed §0, §16 and banner text

*Saved to scratch as `wordscan_s7.txt`.*

```
hits: 0
```

*Saved to scratch as `wordscan_added_s7.txt`.*

```
added lines written: 3
hits: 0
```

### B.1e — §7: the consistency check over the built file

*Saved to scratch as `consistency_s7.txt`.*

```
rows parsed: 4642; travelling refs checked: 2464; as-at refs checked: 861; flags: 0
```

### B.2a — §8: the first search pass (six hits printed per term)

*Saved to scratch as `s8search_out.txt`.*

```
==================== OQ-L2-1
-- term /added[- ]sixth/: 2 rows
   Row 5.146 [ADOPTED — carried] share-tone: select the reading that participates in a licensed progres :: …ne** (two readings explaining the same pitch classes — for instance a minor triad with an added sixth versus a half-diminished seventh a third below): select the reading that **participates in a licensed progres…
   Row 5.201 [ADOPTED — carried] resolving a share-tone abstention by the established progression. :: …*Outgoing statement.* "**Resolving a share-tone abstention.** Layer 4 carried both the added-sixth and the half-diminished readings and abstained; the established progression toward the next function selects …
-- term /\bninth/: 7 rows
   Row 6.33 [QUARANTINED] the added notes are read off the membership decision. :: …*Outgoing statement.* "**the added notes** — any sixth, ninth, eleventh, thirteenth, or altered tone above the basic quality, read off the membership decision (§5), not ma…
   Row 6.39 [ADOPTED — carried, QUARANTINED] the added notes are kept out of the catalogue and recovered afterward. :: …ng statement.* "What is deliberately **not** in the catalogue is the added notes (sixths, ninths, suspensions): established practice finds that folding these into the chord vocabulary degrades recognition,…
   Row 6.75 [QUARANTINED] a chord tone above the basic triad or seventh is the added note. :: …dded notes fall out of this: a chord tone above the basic triad or seventh *is* the sixth/ninth." — §4, step 2 (locator: line 218).…
   Row 6.85 [ADOPTED — carried, QUARANTINED] added notes are not candidate types; they come out of membership. :: …*Outgoing statement.* "Added notes (sixths, ninths) are not candidate types — they come out of membership." — §5, item 1 (locator: lines 247–248). Two claims: …
   Row 6.139 [ADOPTED — carried] chosen: the symbol and the membership are one decision. :: …ership co-determine each other (you cannot separate `C` from `Cadd9` without deciding the ninth's membership), and splitting them forces each half to guess the other." — §9, *Chord symbol and chord-tone me…
   Row 6.155 [RELOCATED] the behavior tests. :: …h the note flagged; a sustained strong-beat note above the triad is a chord tone (a sixth/ninth chord); a suspension is a non-chord tone; a thin slice over a clear prevailing chord **inherits** it; a thin …
-- term /eleventh/: 1 rows
   Row 6.33 [QUARANTINED] the added notes are read off the membership decision. :: …*Outgoing statement.* "**the added notes** — any sixth, ninth, eleventh, thirteenth, or altered tone above the basic quality, read off the membership decision (§5), not matched as a…
-- term /double[- ](?:sharp|flat|accidental)/: 0 rows
-- term /chord vocabulary|vocabulary of chord/: 3 rows
   Row 6.39 [ADOPTED — carried, QUARANTINED] the added notes are kept out of the catalogue and recovered afterward. :: …tes (sixths, ninths, suspensions): established practice finds that folding these into the chord vocabulary degrades recognition, so the standard recipe is **a small catalogue of basic types plus recovering the added …
   Row 6.62 [QUARANTINED] the style preset as a weak preference on the likely chord vocabulary. :: …*Outgoing statement.* "The style preset enters as a **weak preference on the likely chord vocabulary** — Baroque expects triads and sevenths; Jazz raises the extended and altered chords; "Standard" sits between…
   Row 56.5 [HISTORICAL, HISTORICAL] embellishment chord-first: segmentation, then a non-chord-tone pass; n :: …-chord tones; (ii) never by re-deriving the chord from pooled notes, and never by a wider chord vocabulary.…
==================== OQ-L2-2
-- term /dorian|phrygian|mixolydian/: 27 rows
   Row 5.9 [RELOCATED] cadence detection: locate and classify the points of closure. :: …onic closure (the perfect and imperfect authentic cadence, the half cadence including its Phrygian form, the deceptive cadence, and — at lower confidence — the plagal and evaded cadences)." — §1, the first jo…
   Row 5.49 [RELOCATED] cadence markers with the full typology, location and confidence. :: …**type from the full typology** (perfect authentic, imperfect authentic, half — including Phrygian — deceptive, plagal, evaded; §5.2), its **location**, and its **confidence** — never a reduced set (not merel…
   Row 5.84 [HISTORICAL, UNPLACED] the grammar-completion amendment: the pre-amendment set omitted three  :: …ng fifth** (tonic→dominant and plagal motion — I→V, IV→I), **the descending second** (the Phrygian/Andalusian step — i→♭VII, ♭VII→♭VI, ♭VI→V), and **the diatonic diminished fifth** (the IV→viiᵒ link of the fu…
   Row 5.119 [RELOCATED] the Phrygian half cadence. :: …*Outgoing statement.* "The **Phrygian** half cadence (minor mode) is the special case of a first-inversion pre-dominant moving to the dominant with…
   Row 5.340 [RELOCATED] the cadence typology is a superset of the standard's six labels. :: …*Outgoing statement.* "The §5.2 cadence typology (PAC, IAC, Half incl. Phrygian, Deceptive, Plagal, Evaded) is a **superset of** DCML's six labels (`PAC/IAC/HC/DC/EC/PC`)." — §15, item 8 (l…
   Row 7.7 [QUARANTINED] the key/mode: a tonal center with its mode, F-mixolydian among them. :: …*Outgoing statement.* "The tonal centre together with its mode (C-major, F-mixolydian). This layer's output object." — §0, the terms table, row *Key/mode* (locator: line 49).…
-- term /\bmodal\b/: 51 rows
   Row 1.51 [ADOPTED — carried] the signature pins the wrong home key on a substantial minority of the :: …home key and pin the wrong one on a substantial minority of the material, concentrated in modal and partial signatures; the signature is therefore soft evidence that leans." — the second bullet (locator: l…
   Row 5.7 [ADOPTED — carried, QUARANTINED] the layer reads the chord decided by Layer 4 in the key decided by Lay :: …lteration, and its relational role (applied/secondary chord, Neapolitan, augmented sixth, modal mixture)." — §1 (locator: lines 27–29). Two claims: (i) it produces the Roman numeral with those components; …
   Row 5.47 [ADOPTED — carried] the relational label at full specificity. :: …r`, `Ger`) and inversion figure, never a generic `+6`; the **Neapolitan** (`bII6`); and **modal mixture** as the precise borrowed/altered degree." — §3 (locator: lines 111–114).…
   Row 5.64 [QUARANTINED] step 5: emit the relational labels, each on its defining trigger. :: … "**Emit the relational labels** (§5.6) — applied/secondary, Neapolitan, augmented sixth, modal mixture — each on its defining trigger, spelling-aware where the distinction is a spelling distinction." — §4…
   Row 5.167 [QUARANTINED] the four relational labels are tested in a fixed precedence, first mat :: …ed **precedence**, first match wins: **augmented sixth → Neapolitan → applied/secondary → modal mixture**." — §5.6 (locator: lines 454–455).…
   Row 5.168 [QUARANTINED] modal mixture is decided as the residual label. :: …*Outgoing statement.* "So "modal mixture" is decided not by a positive test for "borrowed" but by being a quality-altering borrowed degree tha…
==================== OQ-L2-3
-- term /segment cap|length cap|maximum (?:segment|span) length|seg_cap/: 5 rows
   Row 10.32 [ADOPTED — carried, HISTORICAL] segment duration implicit-geometric with a hard length cap; an explici :: …*Outgoing statement.* "Segment duration is otherwise implicit-geometric with a hard length cap (the established semi-Markov default; an explicit harmonic-rhythm duration model is recorded as CONJECTURE-ga…
   Row 10.52 [HISTORICAL, HISTORICAL] exact decode expected tractable; the reserve a documented prune with i :: …ing statement.* "With chorale-scale event counts (roughly 60–150 events), the established segment cap, and the block factorization, exact decode is expected tractable; **if measurement shows otherwise, the reser…
   Row 17.10 [UNPLACED, ADOPTED — carried, ADOPTED — carried, QUARANTINED] the state space, the degree-valued chord, the semi-Markov segmentation :: …rived published fact from (key, degree)), segmentation is a modeled semi-Markov variable, seg_cap 4." — the as-built paragraph (locator: lines 31–33). Four claims: (i) the state is twenty-four keys by a voca…
   Row 17.33 [QUARANTINED] the producer: one call from the score to the record. :: …bles/adapter + the SELECTED weight vector (Decision D1) -> `decodePiece` (§5 total order, seg_cap 4) -> `assembleNotationRecord` (which attaches the §3.3 slice)." — the record-path paragraph, subsection (1) …
   Row 62.10 [] L0/L1 Row 11.10: segment duration as implicit-geometric with a hard le :: …oing statement it carries.* "Segment duration is otherwise implicit-geometric with a hard length cap (the established semi-Markov default; an explicit harmonic-rhythm duration model is recorded as CONJECTURE-ga…
-- term /lerdahl|weber/: 0 rows
-- term /recency/: 0 rows
==================== OQ-L2-4
-- term /appoggiatura/: 4 rows
   Row 6.91 [UNPLACED] the third tier: the one-sided case decided by metric weight and the pr :: …*Outgoing statement.* "An appoggiatura (leapt to, resolved by step), an escape tone (approached by step, left by leap), or an incomplete neighbour: …
   Row 13.3 [UNPLACED] the common kinds of non-chord tone, named. :: …n types: passing tones (PT), neighbor tones (NT), suspensions (SUS), anticipations (ANT), appoggiaturas, escape tones, pedal tones, chromatic neighbors, cambiata, échappée." — the section *What NCT detection woul…
   Row 26.14 [HISTORICAL] the Baroque ornaments. :: …*Outgoing statement.* "Baroque: trill, mordent, turn, appoggiatura, acciaccatura, Schleifer" — §7.4 *Ornament Vocabulary*, the style-specific ornament types (locator: line 5770…
   Row 48.45 [UNPLACED] the ornament labels derived after the decode from the committed chord, :: …*Outgoing statement.* "**Ornament labels (passing tone, neighbor tone, suspension, appoggiatura, pedal point) are derived AFTER the decode** from the committed chord by the standard definitions and publish…
-- term /escape tone|échappée|echappee/: 2 rows
   Row 6.91 [UNPLACED] the third tier: the one-sided case decided by metric weight and the pr :: …*Outgoing statement.* "An appoggiatura (leapt to, resolved by step), an escape tone (approached by step, left by leap), or an incomplete neighbour: a note foreign to a **clear prevailing chord*…
   Row 13.3 [UNPLACED] the common kinds of non-chord tone, named. :: …g tones (PT), neighbor tones (NT), suspensions (SUS), anticipations (ANT), appoggiaturas, escape tones, pedal tones, chromatic neighbors, cambiata, échappée." — the section *What NCT detection would do* (locator…
-- term /retardation/: 0 rows
-- term /pedal point/: 13 rows
   Row 8.110 [QUARANTINED] the carry and the channels both change if a pedal is a carried slice a :: …tement.* "The distinct-root carry (§2.3) and the selection channels (§3.2) both change if pedal points are a carried slice attribute." — §4.3, item *Pedal detection's home* (locator: lines 298–299).…
   Row 23.15 [QUARANTINED, QUARANTINED] the pedal flag, left empty on the record path. :: …*Outgoing statement.* "bool isPedalPoint = false; // Bass is a structural pedal point (§5.12; empty on the record // path — see §7.4's voice-independent successor)" — *Output — `ChordAnalysisResu…
   Row 24.89 [HISTORICAL] the two-pass pedal detector: implemented. :: …utgoing statement.* "**Status: Implemented (Session 18, master `fb9a27ce9a`).**" — §5.12 *Pedal Point Detection — Two-Pass Analysis* (locator: line 4873).…
   Row 24.90 [UNPLACED, QUARANTINED, HISTORICAL] superseded by a voice-independent pedal class in the ornament vocabula :: …ow can only see the lowest voice, and it retires with the legacy analysis path." — §5.12 *Pedal Point Detection — Two-Pass Analysis* (locator: lines 4873–4876). Three claims: (i) the pedal point is a voice-indep…
   Row 24.91 [HISTORICAL, QUARANTINED, QUARANTINED] the replacement deferred; the two-pass detector still runs on the lega :: … the legacy arm; on the production record path the pedal fields are left empty." — §5.12 *Pedal Point Detection — Two-Pass Analysis* (locator: lines 4876–4878). Three claims: (i) the replacing class is deferred …
   Row 24.92 [ADOPTED — carried] a structurally lighter lowest tone may not belong to the upper voices' :: … tonic organ point — it may not belong to the chord formed by the upper voices." — §5.12 *Pedal Point Detection — Two-Pass Analysis* (locator: lines 4880–4882).…
==================== OQ-L2-5
-- term /\bpivot/: 20 rows
   Row 10.43 [UNPLACED] P5: the entry chord depends only on the new key. :: …nds only on the new key | ASSUMPTION (weaker than Raphael-Stoddard's, which we replace) | Pivot-chord modulation says entry depends on the OLD key too (the pivot is diatonic in both); visible as entry-tabl…
   Row 11.52 [RELOCATED, HISTORICAL] the need for key and modulation ground truth. :: …modulation_dataset` upstream (direct-acquisition candidate, next corpus increment). Sears pivots: no public deposit. SWD score-aligned local keys unchanged (ChoCo). WiR analyses still carry local keys gene…
   Row 13.27 [HISTORICAL] the estimate for the features downstream: indirect improvement. :: …*Outgoing statement.* "**On downstream features (cadence, pivot, key inference):** Indirect improvement." — the section *Quality impact estimate* (locator: lines 105–106).…
   Row 20.5 [QUARANTINED] the chord staff: a part the user adds, filled on demand with the harmo :: …n numerals, canonical or collected voicings, key/mode annotations, borrowed chord labels, pivot detection, and cadence markers." — §1.4 *Implemented Components* (locator: lines 654–658).…
   Row 22.107 [QUARANTINED] the section analyzer: stabilization, cadence and pivot detection. :: … | Section-level unified analysis — `analyzeSection`, key/mode stabilization, cadence and pivot detection (`detectCadences`, `detectPivotChords`). Moved here in Stage 2.1 (Phase 4c). |" — the region-analys…
   Row 22.109 [QUARANTINED] the section-level analysis's home. :: …* "Section-level unified analysis — `analyzeSection`, key/mode stabilization, cadence and pivot detection — lives in `composing/analysis/section/`." — §3.3, the section-level analysis (locator: lines 2297–…
==================== OQ-L2-6
-- term /stops changing|stop(?:s)? when it stops|converge/: 28 rows
   Row 2.47 [HISTORICAL, QUARANTINED] the reach-back convergence proxy measured false and dropped; the as-bu :: …*Outgoing statement.* "**The reach-back convergence PROXY was measured FALSE and is dropped; the as-built tracks the leading-edge key itself and stops when th…
   Row 5.141 [QUARANTINED] the recompute is localized, forward and convergence-bounded. :: …* (it re-runs the lower reading with a decided fact; it sends no request upstream), and **convergence-bounded** (a key change decided once; the recompute does not re-open the key decision that triggered it)."…
   Row 5.224 [UNPLACED] cases 2 and 4 are realized by one localized, forward, convergence-boun :: …Cases 2 and 4, when they fire, are realized by **one mechanism**: a **localized, forward, convergence-bounded recompute** — the dependent reading is re-run over the **affected region only**, with the correcte…
   Row 5.251 [UNPLACED] every later layer brings its evidence to bear; agreement reinforces; a :: …osses a threshold scaled to the earlier layer's confidence — firing a localized, forward, convergence-bounded recompute." — §9, D7 (locator: lines 647–650).…
   Row 5.320 [HISTORICAL] the exact forward-recompute contract is to be pinned with the key laye :: …tement.* "**The exact forward-recompute contract** (§5.4) — the precise region bound, the convergence guarantee, and the confidence-versus-evidence threshold *shape* (not its constant) — to be pinned with the…
   Row 7.64 [QUARANTINED] the built reach-back loop: its trigger, its action and its stop. :: …re-slice (Layer 2) → re-decode (Layer 3), repeated until the leading-edge **settled** key stops changing across iterations (settled = not "uncertain" and at-or-above that same confidence minimum), the hard bound (m…
==================== OQ-L2-7
-- term /retardation|suspension/: 19 rows
   Row 1.49 [ADOPTED — carried] chord membership is decided inside the analysis, not before it. :: …t: the same four sounding pitches may be one chord with an added fourth or a chord with a suspension that resolves away, so chord membership is decided inside the analysis rather than before it." — the first bu…
   Row 5.100 [UNPLACED, RELOCATED] the cadential six-four is the dominant's accented suspension: the pair :: …at proceeds to a root-position dominant over the same bass, it is the dominant's accented suspension, not a tonic arrival: collapse the pair into a single **dominant approach** so the cadential bass reads five-…
   Row 5.283 [UNPLACED] glossary: the cadential six-four as the dominant's accented suspension :: …ial six-four** — a second-inversion tonic spelling functioning as the dominant's accented suspension, not a tonic arrival." — §12 (locator: lines 718–719).…
   Row 6.26 [QUARANTINED] the type of a non-chord tone is not classified here. :: …atement.* "It does **not** classify the **type** of a non-chord tone (passing, neighbour, suspension, anticipation): naming the chord needs only the chord-tone-versus-non-chord-tone call; the type label is a se…
   Row 6.39 [ADOPTED — carried, QUARANTINED] the added notes are kept out of the catalogue and recovered afterward. :: …ment.* "What is deliberately **not** in the catalogue is the added notes (sixths, ninths, suspensions): established practice finds that folding these into the chord vocabulary degrades recognition, so the stand…
   Row 6.89 [ADOPTED — carried] the first tier: a stepwise-embellishing note is a non-chord tone even  :: …ne), or held over from the previous chord and resolving down by step into a chord tone (a suspension), is a non-chord tone — *even on a strong beat*." — §5, item 3, the first tier (locator: lines 257–259).…
-- term /restat/: 4 rows
   Row 11.71 [HISTORICAL] a plan: the constraint carried into the roadmap and restated in the fi :: …ntation_roadmap.md`'s Stage-5 block at the next CC docs commit, and the fitter design doc restates it in its §2/§6 (data declaration) — not optional." — §8c, *The FULL-NEEDS AUDIT*, the license constraint's…
   Row 12.24 [UNPLACED, ADOPTED — carried] tables from counts, once, frozen; only the combination weights move; n :: …ing statement.* "**Fit-scope declaration (the Noland lesson, already ratified at §5a(c)), restated as a gate item:** tables from counts, once, frozen; only the combination weights move in the discriminative…
   Row 46.14 [RELOCATED] that stop the robust-unit one, gate block (A) the one authority. :: …ndaries unit — and it is the ONE authority for what this term means here; no criterion is restated in this document (#6, D-431).**" — §0 *Terminology*, the project terms (locator: lines 82–84).…
   Row 62.38 [] L0/L1 Row 26.3: the mode and the chromaticism carried as cross-attribu :: …" — `cowork_idiom_entry_mapping.md`, the banner (the L0/L1 row's own locator: lines 8–9); restated in the notes, *"Each entry also gets the two cross-attributes … tagged independently of the idiom."* (lines…
==================== OQ-L2-8
-- term /exact decode|exact inference|beam|tractab|\bprune/: 25 rows
   Row 1.8 [ADOPTED — carried, HISTORICAL, QUARANTINED] the decode is exact; the reserve prune never adopted; what the decoder :: …*Outgoing statement.* "**(c) The decode is EXACT; the declared reserve prune was never adopted, and what the decoder does narrow has no specified form.**" — rule (c) (locator: lines 303–…
   Row 1.10 [HISTORICAL] the reserve prune, declared for use only if exact decode proved intrac :: …*Outgoing statement.* "A prune was declared in reserve — restricting key-change candidates to a fitted-mass neighborhood on the circle of fi…
   Row 1.11 [QUARANTINED] the prune was never adopted: its measured cost is worse than exact dec :: … statement.* "It was never adopted: measured at the fitted weights its cost is worse than exact decode." — rule (c) (locator: lines 308–309).…
   Row 1.13 [HISTORICAL] tried and closed on the search. :: …osed on the search — do not retry; the register carries each with its measurement: D-288 (beam widening, shelved), D-328 (a wider search over the same scoring, refuted), D-278 (the joint key-and-chord ste…
   Row 6.190 [ADOPTED — carried, UNPLACED, UNPLACED, QUARANTINED] the carry on every decision, never pruned; the override selects among  :: … **every** decision — Commit and Inherit included, filled before the trichotomy and never pruned — so Layer 5 overrides **by selecting among the readings this layer carried** (never by re-deriving), and th…
   Row 7.161 [UNPLACED] this is the per-layer decode, not the rejected global cross-layer join :: …path decode — internal to Layer 3 — not the rejected **global cross-layer** joint Viterbi/beam decode; cf. ARCHITECTURE.md §2.14.)*" — §14, *Built on — the deciding method* (locator: lines 473–474).…
==================== OQ-L2-9
-- term /chordal voice|successor|following note|next note in/: 17 rows
   Row 9.105 [RELOCATED] class-(b) root-disagree duration non-increase on the fitting split. :: …gree duration non-increase on the fitting split's covered cells**, same preset scope (the successor-stop semantics, tracked from day one so the R10 handover is continuous)." — §4.2, *Per-evaluation hard constr…
   Row 9.162 [HISTORICAL] the R10 decision surface assembled once the families are adopted. :: …ng the ratified per-run set-diff semantics; the A-8 instrument emits both forms), and the successor stop semantics (constraint 2)." — §4.7, *Phase 4 — adoption and the R10 re-baseline* (locator: lines 502–505)…
   Row 9.165 [HISTORICAL] R10-a: the decision surface built. :: …ng (every 52/24/52 case still-failing under variant (b), 0 disappear), the runnable+timed successor sandwich (`tools/robust_stop_diff.py`; class-(b) duration non-increase + explained run-diff; ≈6 s), and the D…
   Row 9.236 [QUARANTINED] until the pool broadens, fitted values are Bach-chorale-shaped. :: …g statement.* "Residual risk is real and stated: until the fitting pool broadens (D-5 and successors), fitted values are Bach-chorale-shaped — exactly as the hand-tuned values already are, but now measurably s…
   Row 9.385 [HISTORICAL] the restriction option removed; the override frame collapses to annota :: …strict) is **removed from the near-term option set** — it is joint-step-gated (a Stage-5+ successor), so the F-B frame collapses to **§3.D-1 (annotate-via-open-mark) EVERYWHERE**, floored by disable; recoverin…
   Row 9.399 [RELOCATED] O-15(iv): the successor check, runnable and timed; the hard stop's for :: …*Outgoing statement.* "**(iv) The successor sandwich — runnable + timed:** new instrument **`tools/robust_stop_diff.py`** (thin orchestration over a8 out…
==================== OQ-L2-10
-- term /grace/: 16 rows
   Row 22.37 [RELOCATED, RELOCATED, RELOCATED, RELOCATED, RELOCATED, HISTORICAL] the lossless, tie-resolved note model and what it carries. :: …ach `NoteEvent` carries 11 fields: `pitch, tpc, staff, voice, onset, release, duration, isGrace, plays, visible, staffEligible`. Tied groups are merged into **one** span/onset (via the DOM `firstTiedNote`/…
   Row 22.74 [RELOCATED] no note kind is special-cased; grace and tuplet outcomes follow from t :: …*Outgoing statement.* "**No special-casing of any note kind** — grace and tuplet outcomes fall out of the note-model spans as facts (verified at source: a grace event carries onse…
   Row 22.75 [RELOCATED] the slicer needs no grace or tuplet code. :: …*Outgoing statement.* "The slicer needs no grace/tuplet code." — Layer 2 (locator: line 1680).…
   Row 23.336 [QUARANTINED] grace notes always excluded, as ornamental and not harmonic. :: …*Outgoing statement.* "// Grace notes are ornamental, not harmonic — always exclude from analysis" — *Score Traversal Pattern*, the code bloc…
   Row 34.1 [UNPLACED] the core scope, modal and jazz harmony among it. :: …analysis cache, enharmonic spelling, score error detection, musical language detector and graceful degradation, extensible style system, initial five styles, ML interface design throughout, unified tempora…
   Row 34.4 [UNPLACED] outside the scope: post-tonal, serial and non-Western music, degrading :: …d real-time operation, film synchronization, adaptive game music, non-Western traditions (graceful degradation at boundary), post-tonal and serial music (graceful degradation at boundary), audio transcript…
==================== OQ-L2-11
-- term /lowest sounding|lowest pitch|lowest note/: 10 rows
   Row 1.52 [HISTORICAL, ADOPTED — carried] three reading-shaped producers measured to pin wrong must stay soft. :: …ust stay SOFT: a cadence-based tonic anchor, a modulation detector, and the rule that the lowest sounding pitch is the chord's root.**" — the third bullet (locator: lines 531–533). Two claims: (i) each was measured …
   Row 5.32 [ADOPTED — carried, RELOCATED] from Layer 1: each note's spelling and voice, and the bass of each sli :: …ared Layer-1.5 spelling view), each note's **voice**, and the **bass** of each slice (the lowest sounding note)." — §3 (locator: lines 85–86). Two claims: (i) each note's spelling and voice; (ii) the bass of each sl…
   Row 5.110 [RELOCATED] perfect when both chords are in root position. :: …** when both the dominant and the tonic are in **root position** (the bass — reliably the lowest sounding voice — carries the cadential five-to-one) **and** no other perfect-condition fails." — §5.2 (locator: lines …
   Row 23.292 [RELOCATED] figured bass, step 1: the bass note. :: …*Outgoing statement.* "Identify the bass note (lowest sounding pitch — already `ChordAnalysisTone::isBass`)." — *Note on figured bass* (locator: line 3900).…
   Row 24.38 [QUARANTINED] the lowest sounding note is wrongly made the root. :: …*Outgoing statement.* "The lowest sounding note gets promoted to root status incorrectly." — §5.8 *Known Analyzer Limitations*, *Rootless voicings* (loc…
   Row 24.45 [HISTORICAL] the single cause found: the bass-root bonus fired on every lowest note :: …ur corpora confirms a single root cause: `bassNoteRootBonus` fires unconditionally on the lowest sounding note, regardless of whether that note is actually the chord root." — §5.8 *Known Analyzer Limitations*, *bass…
==================== OQ-L2-12
-- term /cue window|look-?back|fourth and seventh|fourth and the seventh/: 3 rows
   Row 5.93 [RELOCATED] a leading-tone resolution and a tritone resolution are detected voice  :: …e** at the arrival; a **tritone resolution** is detected when the dominant's tritone (the fourth and seventh degrees) contracts or expands by step to the tonic's third and root across the boundary." — §5.0 (locator: li…
   Row 7.156 [HISTORICAL] what this layer replaces: the per-region key-selection code. :: … for one coarse region at a time, with a small "don't flip too easily" margin and a fixed look-back/look-ahead window." — §13 (locator: lines 454–456).…
   Row 10.34 [UNPLACED] the cadence factor: three key-axis features, each with a fitted weight :: …ution (seventh degree rising to the tonic in candidate key k), the tritone pair (both the fourth and seventh degrees of k sounding in the approach), dominant-to-tonic bass motion (falling fifth / rising fourth), each a…
==================== OQ-L2-13
-- term /non-chord-tone|chord-tone label|nct/: 677 rows
   Row 1.31 [ADOPTED — carried] chord membership is settled by the categories, not by whether the note :: …oing statement.* "Whether it belongs to the chord is what the emission's chord-member and non-chord-tone categories are for — it is not settled by whether the note happened to be struck at this event." — the same s…
   Row 2.37 [HISTORICAL] the gate trade-off on record. :: …que **53** (net −4), Jazz **24** (net +1), Default **53** (net −4); zero new class-(b) (functional) regressions — every new case is a class-(a) symmetric-dim7 / share-tone **rotation** ambiguity (root pi…
   Row 2.38 [HISTORICAL] the Jazz +1 accepted, to retire when Layer 4 pins the rotation. :: …ate amendment (CLAUDE.md, "Gate threshold and preset policy"); it retires when Layer 4 (function/cadence) pins the rotation." — (locator: lines 1856–1857).…
   Row 3.11 [HISTORICAL] non-chord-tone detection waits for the annotated material it needs. :: …*Outgoing statement.* "Non-chord-tone detection waits for the annotated material it needs." — (locator: lines 1964–1965).…
   Row 3.26 [QUARANTINED] proven where it commits; its abstention mostly function-dependent. :: …*Outgoing statement.* "**Proven where it commits; abstains where function decides.** Per the L4-build grading reported in the engage-with-L5 ratification (`cowork_l1l4_review_chart…
   Row 4.1 [ADOPTED — carried, QUARANTINED, RELOCATED] the function layer produces the Roman numeral and local-key markers fr :: …*Outgoing statement.* "The function layer reads the L4 chord **in** the L3 key and produces the **Roman numeral** (the precise superset of a T…
==================== OQ-L2-14
-- term /calibrated probabilit|margin class|margin-class|confidence class|class m\b/: 15 rows
   Row 6.127 [ADOPTED — carried, QUARANTINED, RELOCATED] the composite is a declared margin-family class, vertical-fit only, co :: …-layer confidence contract (`cowork_confidence_contract.md`) this composite is declared **Class M (declared-composite)** — a margin-family quantity, not a calibrated probability, **vertical-fit only** by con…
   Row 7.13 [QUARANTINED, ADOPTED — carried, QUARANTINED] the confidence: a sequence margin, declared a margin class, published  :: …an the best sequence forced to a different key/mode at that slice (§5 step 4). Declared **Class M** (a margin, not a calibrated probability) under the cross-layer confidence contract (`cowork_confidence_cont…
   Row 9.22 [RELOCATED] glossary: the two admissible confidence classes. :: …*Outgoing statement.* "The two admissible confidence classes of the confidence contract: Class M = a squashed decision margin (a rank statement); Class P = a calibrated…
   Row 21.47 [RELOCATED] the confidences the override compares are bounded, declared by class a :: …h departs from it, OI-231): every boundary confidence is [0,1], class-declared (margin vs calibrated probability), and cross-layer comparisons happen only in the contract's declared frames.*" — §2.15, the second contract …
   Row 21.64 [HISTORICAL, RELOCATED, RELOCATED] six layers not a ceiling; the voice-leading axis built; grouping above :: …val profiles (facts) + VL-C texture classification (the one v1 judgment: texture-of-span, Class M) + its bounded-context requester; measured orthogonal to the harmonic spine (cross-ARI 0.030); VL-D/E/F/G/H n…
   Row 21.69 [RELOCATED] a confidence at a layer boundary is in [0,1], declared by class, and s :: …nother layer may read — a confidence is **in [0,1], class-declared (a ranking margin or a calibrated probability), and stated together with the decision it is the confidence of**." — §2.15, the cross-layer confidence cont…
==================== OQ-L2-15
-- term /top-?k\b|\bcap(?:ped)?\b.*(?:alternative|reading|rival)|no truncation|threshold.*(?:alternative|reading|rival)/: 29 rows
   Row 5.319 [QUARANTINED] the override calibration facts: the chord layer's confidence is vertic :: …only** (no progression signal — this layer supplies the functional context itself, so the threshold scales against vertical decisiveness, not total decisiveness); the carried `alternatives` are **capped (topK)** and **exclude spelling-pinned symmetric siblings** (so an override that wanted to revisit a spelling-resolved rotation must decide its interaction with the spelling-pin); and there is **no cross-slice neighbourhood confidence** — this layer derives neighbourhood decisiveness itself from adjacent slices' carried confidence/alternatives." — §15, item 2 (locator: lines 819–825).…
   Row 6.190 [ADOPTED — carried, UNPLACED, UNPLACED, QUARANTINED] the carry on every decision, never pruned; the override selects among  :: …carried** (never by re-deriving), and the carried confidence is the quantity its override threshold scales against." — §15, O1b (locator: lines 575–579; the sentence opens one line before the home as the artifact cites it, 576–579, and the home lies wholly inside it). Four claims: (i) the layer carries its ranked alternatives and its confidence on every decision, commit and inherit included; (ii) the carry is never pruned; (iii) the function layer overrides by selecting among the carried readings, never by re-deriving; (iv) the carried confidence is the quantity the override threshold scales against.…
   Row 6.192 [QUARANTINED, QUARANTINED] the carried confidence is vertical-fit only; the alternatives capped a :: …ression signal folded in — that is Layer 5's to supply), and the carried alternatives are capped at a fixed number of highest-ranked readings (a tunable; identifier `topK`) and exclude spelling-pinned symmetric siblings — calibration facts the Layer-5 override design accounts for, not defects here." — §15, O1b (locator: lines 581–584). Two claims: (i) the carried confidence is vertical-fit only; (ii) the carried alternatives are capped at a fixed number and exclude the spelling-pinned symmetric siblings.…
   Row 7.81 [QUARANTINED] the candidate set: the union of every slice's top-K, available at ever :: …the as-built rule, verified at `keymodesequence.cpp` `buildLattice`):** take each slice's top-K best-scoring candidates, and form the **union of those top-K sets across all slices** (plus any pinned candid…
   Row 8.39 [QUARANTINED] the measured fan-out: wide in readings, narrow in roots. :: …t.md`) fixes the **factual shape** of the carry `[data]`: per competition slice the above-threshold ranked set is **wide in readings but narrow in roots** — median **5/4/5** readings (Baroque/Jazz/Default) but distinct **roots** median **2/1/2**, mean **2.13/1.73/2.12**." — §2.1, *What Laye…
   Row 8.50 [QUARANTINED] the decoder's alternatives: distinct voicings after the chosen chord,  :: … chord **voicings** after `chosen` — deduped by `sameChordVoicing` (`:752`), capped at **`topK` (default 6, `chordslicedecoder.h:169`)**;" — §2.3, *Does the decoder's governed carry provide this?* (locato…
==================== OQ-L2-16
-- term /unfold|volta|notated order|repeat/: 20 rows
   Row 5.39 [RELOCATED] a section end is a phrase boundary that coincides with a structural bo :: …hrase boundary that **also coincides with a structural score boundary** — a double bar, a repeat mark, or the end of the piece — used only as the section-end salience cue in §5.2.)" — §3 (locator: lines 95–…
   Row 7.64 [QUARANTINED] the built reach-back loop: its trigger, its action and its stop. :: …sk Architectural Layer 1 to `extend(Earlier)` → re-slice (Layer 2) → re-decode (Layer 3), repeated until the leading-edge **settled** key stops changing across iterations (settled = not "uncertain" and at-o…
   Row 10.47 [QUARANTINED, ADOPTED — carried] exactly equal candidate scores between decodes are real; unbroken, the :: … real (proven at 8 corpus pieces — equal-score segmentations differing by one boundary on repeated-chord runs) and, unbroken, they make the committed output depend on the platform's floating-point library —…
   Row 23.179 [QUARANTINED] the mode-name helpers use separate arrays per mode family. :: …TonicOffset()` use separate static arrays per mode family and share comment patterns that repeat the same "mode family / parent key signature" logic." — §4.1i *Technical Debt and Refactor Backlog (reviewed …
   Row 23.255 [HISTORICAL] stop when the same winner survives repeated expansion. :: …*Outgoing statement.* "the same winner survives repeated expansion" — *Phase 1b — Minimal Monophonic Fallback Without Chord Symbols* (locator: line 3666).…
   Row 24.52 [QUARANTINED] the notation path merges repeated slices of the same chord into one re :: …*Outgoing statement.* "The notation bridge now uses the same collapse rule, so repeated slices that analyze to the same chord merge into one region even in preserve-all mode." — §5.8 *Known Analy…
==================== OQ-L2-17
-- term /enharmonic/: 41 rows
   Row 2.50 [ADOPTED — proposed, HISTORICAL] a key span needs an enharmonic-identity rule, and does not have one. :: …*Outgoing statement.* "**A key SPAN needs an enharmonic-identity rule, and it does not have one** (the Layer-3 half of the ratified cadence-less-confirmation amendme…
   Row 2.51 [QUARANTINED, ADOPTED — proposed] enharmonic reinterpretation is handled per chord only; the amendment r :: …*Outgoing statement.* "Enharmonic reinterpretation is handled at the single-chord level; nothing decides whether a span is written in one spell…
   Row 4.19 [ADOPTED — carried] the layer needs key-confirmation channels that do not require a cadenc :: …O NOT REQUIRE A CADENCE (the Layer-5 half of the ratified amendment whose other half — an enharmonic-identity rule for key spans — is at Layer 3; the two cross-point).**" — the second obligation (locator: lines…
   Row 5.346 [ADOPTED — proposed] an enharmonic key-span identity rule: one identity with a spelling fra :: …*Outgoing statement.* "Also part of A-4: an **enharmonic key-span identity rule** (F-14) — when two candidate keys are enharmonically equivalent (`G♭`↔`F♯`), the key-…
   Row 8.71 [ADOPTED — carried, QUARANTINED] the pitch-spelling channel: load-bearing, read only where the distinct :: …*Outgoing statement.* "**load-bearing** — disambiguates enharmonic/symmetric roots pitch-class-blind fit cannot (the symmetric-rotation churn). Read only where the distinction …
   Row 9.352 [QUARANTINED] O-21: one promotion primitive owns all post-scoring promotion; Gate A  :: …ve + one builder wrapper `buildResultFromGateCtx` now own all post-scoring promotion; the enharmonic Major-add6→Minor7 flip is one primitive call whose present branch (`presentHint = bestAltIdx`) reproduces Gat…
==================== OQ-L2-18
-- term /pedal/: 95 rows
   Row 6.125 [QUARANTINED] the pedal-point flags are not carried. :: …*Outgoing statement.* "(The pedal-point flags are **not** carried — no Layer-5 §5 rule consumes them; identifiers: `isPedalPoint`/`pedalBassPc`…
   Row 8.37 [HISTORICAL] built and owed: pedal detection, none in the decoder. :: …*Outgoing statement.* "| Pedal detection | **none in the decoder** (audit gap) `[code]` | a **new reader-over-carry** — enumerated §4.2 |" —…
   Row 8.103 [QUARANTINED] gap 3: the decoder has no pedal detection; the legacy pedal pass overw :: …*Outgoing statement.* "**Pedal detection as a reader-over-carry** — the **decoder has none** (structural-integrity audit gap; the legacy `ch…
   Row 8.104 [QUARANTINED, HISTORICAL] pedal detection is needed as a reader over the carry, its home a later :: …*Outgoing statement.* "Engaged Layer 5 (or its carry) needs pedal detection as a **reader over the carry**, not a `results`-mutating post-pass. **Its home is a downstream deci…
   Row 8.109 [QUARANTINED] the hinge: whether pedal detection is a chord-layer annotation or a re :: …*Outgoing statement.* "**Hinge:** §4.2 gap 3 — whether pedal detection is a Layer-4 carry annotation (a slice property the carry exposes) or a Layer-5 reader-over-carry d…
   Row 8.110 [QUARANTINED] the carry and the channels both change if a pedal is a carried slice a :: …tement.* "The distinct-root carry (§2.3) and the selection channels (§3.2) both change if pedal points are a carried slice attribute." — §4.3, item *Pedal detection's home* (locator: lines 298–299).…
rows indexed: 4642
```

### B.2b — §8: the second search pass

*Saved to scratch as `s8search_out2.txt`.*

```
==================== OQ-L2-1b
-- term /closure|ceiling/: 41 rows
   Row 5.9 [RELOCATED] cadence detection: locate and classify the points of closure. :: …*Outgoing statement.* "**Cadence detection** — locate and classify the points of harmonic closure (the perfect and imperfect authentic cadence, the half cadence including its Phrygian form, the deceptive cad…
   Row 5.49 [RELOCATED] cadence markers with the full typology, location and confidence. :: …*Outgoing statement.* "**Cadence markers** at each point of closure: the cadence **type from the full typology** (perfect authentic, imperfect authentic, half — including Phrygi…
   Row 5.224 [UNPLACED] cases 2 and 4 are realized by one localized, forward, convergence-boun :: …r that pass**: it is **marked final for the remainder of this analysis pass** (a one-pass closure flag on the decision), so the recompute it triggers — and any later override in the same pass — cannot re-tar…
   Row 5.279 [RELOCATED] glossary: the cadence, split into perfect and imperfect by inversion. :: …*Outgoing statement.* "**Cadence** — a point of harmonic closure; authentic (dominant to tonic), half (ending on the dominant), deceptive, plagal, evaded; the authentic split…
   Row 5.308 [RELOCATED] the phrase boundary is defined generally: rests and structural boundar :: …vering non-chorale textures too (rests, structural score boundaries — **but not cadential closure**, which is *this* layer's and would be circular)." — §15, item 0 (locator: lines 799–802).…
   Row 6.157 [QUARANTINED] the chord-root residual is a few percent; the membership call is the l :: …5 step 3) and window (§2) are the main open tunables." — §11, *The chord axis is near its ceiling; the chord-tone/non-chord-tone call is the real lever* (locator: lines 481–483).…
   Row 6.205 [ADOPTED — carried, RELOCATED] the open ends: a pop ground truth to fit the value; the power-chord la :: …splayed* in common-practice output is an L6/product presentation question (progressive disclosure), separate from the scorer's competitiveness constant." — §15, O4 (locator: lines 626–629). Two claims: (i) t…
   Row 7.157 [QUARANTINED] deciding one region at a time is the measured ceiling; the held-out ba :: …*Outgoing statement.* "Deciding one region at a time is the measured ceiling on relative-pair and modulation accuracy (the held-out baseline it must beat — measured as key/mode agreement…
   Row 8.19 [QUARANTINED] the dormant bounded-context extension loop is also built. :: … the base resolver), and the §8 primitive it fires through (`forwardoverride.cpp` `OnePassClosure::tryOverride` / `forwardRecompute`)." — §1.2 (locator: lines 77–79).…
   Row 8.99 [ADOPTED — carried, QUARANTINED] acyclicity: the only cross-layer recompute is the bounded forward mech :: …compute* is the §8 localized-forward-convergence-bounded mechanism (marked-final one-pass closure), never a back-edge." — §4.1, *Acyclicity (the forward-only control-flow contract, §8/§9-D7)* (locator: lines…
   Row 8.100 [QUARANTINED, QUARANTINED] the joint step, when built, a bounded instance of the forward discipli :: …a **bounded** instance of that same forward discipline (a declared exception with its own closure), not a free cross-layer search — which the spec measured inert (§8 "What this is NOT")." — §4.1 (locator: li…
   Row 8.186 [HISTORICAL, QUARANTINED] to build 6: the joint step, shelved; measured not to pay. :: …oc-sync #10)*: measured NOT to pay (net +0.05–0.16 pp, harm 75–90 % of correction, oracle ceiling +0.6 pp, coupled-minority net ~0, fire-rate 1.4 % — `records/cc/reports/cc_engage_stage3_joint_measure_report…
   Row 9.121 [HISTORICAL, HISTORICAL, HISTORICAL, HISTORICAL, QUARANTINED] P1 ratified: the split, the optimizer, the staging, no augmentation, t :: …ive's resolution) → abstention bars last; (4) **R-13 augmentation SKIPPED** (the measured ceiling is coupling-limited, not data-limited); (5) **the two rider-flagged frozen rows STAY FROZEN with corrected ra…
   Row 9.240 [QUARANTINED] much of the batch residual is not reachable by weights. :: … bass/inversion, segmentation — not weight-reachable." — §11, the item on the objective's ceiling (locator: lines 825–826).…
   Row 9.241 [HISTORICAL] the arc's success criterion is honest movement plus the structural del :: …5 direct yield small: ~1.3 % batch / ~6–7 % section)." — §11, the item on the objective's ceiling (locator: lines 826–829).…
   Row 9.254 [HISTORICAL] O-7: the family-1 candidate parked, not adopted. :: …*Outgoing statement.* "**O-7 (Phase 2.1 closure, user-ruled 2026-07-05): the family-1 candidate is PARKED, not adopted.**" — §15, O-7 (locator: line 963).…
   Row 9.272 [HISTORICAL, QUARANTINED] O-11(ii): family 2 closed not adoptable; the blocking case a segmentat :: … Gm region — the weight fit relocates the boundary failure, it cannot remove it; the §11 "ceiling is upstream of weights" caveat, now measured at a single case)." — §15, O-11 (locator: lines 1024–1031). Two …
   Row 9.294 [HISTORICAL] nothing adopted; family 2 re-opens as adoptable pending ratification. :: … (Family 2 re-opens as ADOPTABLE-PENDING-RATIFICATION, superseding the 2.2c not-adoptable closure)." — §15, O-11 (locator: lines 1081–1083).…
   Row 9.304 [QUARANTINED] the rules are load-bearing but hold no fit. :: …TAIN verdicts are re-confirmed by leverage) but hold no fit — a legitimate staging-step-3 closure." — §15, O-13 (locator: lines 1111–1113).…
   Row 9.313 [QUARANTINED, RELOCATED] O-14(vi): conformal against the maps, measured; a complement, not a re :: …hievable targets (better efficiency, finite-sample-valid) but slips where the correctness ceiling nears the target → **complement, not replacement** (recorded for the Cowork disposition)." — §15, O-14 (locat…
   Row 9.374 [QUARANTINED] the go/no-go: a small net gain, harm most of the correction. :: …LIPS = **+9 / +3 / +10** over ~6200 DCML-scored regions/preset (**+0.05–0.16 pp**; oracle ceiling **+0.6 pp**); **harm = 75–90 % of correction** everywhere." — §15, O-19, the joint-step measurement (locator:…
   Row 10.45 [ADOPTED — carried] P7: segment boundaries depend on meter and fermatas, not on the key. :: … Segment boundaries depend on meter and fermatas, not on the key | ASSUMPTION | Cadential closure influences segmentation beyond meter; partially covered by the cadence factor sitting at boundaries; visible …
   Row 11.10 [HISTORICAL] the partial containers named and bounded. :: …m beyond PDMX (ToS-unwalkable); CPDL/IMSLP symbolic subsets; craigsapp's ~100 kern repos (closure tool exists: `humdrum-tools/humdrum-data`); abcnotation.com long tail | **Named, bounded**" — §1, the table o…
   Row 11.39 [HISTORICAL] the residual container classes not yet walked. :: …manifest = 71 repos/16 orgs, incl. `DDMAL/Flexible_harmonic_chorale_annotations` — Wave-3 closure, cloned nothing**), national-library MEI editions, the ABC long tail, non-Western symbolic sets (SymbTr, jing…
   Row 11.41 [RELOCATED] non-Western symbolic sets are out of the analysis's scope by ruling. :: …le later** (craigsapp via `humdrum-tools/humdrum-data`; DLC piece counts at clone time) — closure rides the acquisition instruction; (c) **snippet-verified rows** ([reported] marks) — a budget choice made vi…
-- term /applied.{0,40}(?:chain|depth|recursive)|V/V//: 0 rows
==================== OQ-L2-2b
-- term /twenty-one|21 modes|two-mode|two modes|composite minor/: 20 rows
   Row 7.42 [QUARANTINED] the key/modes recognized: twelve centers by twenty-one modes. :: …mode is one of the **12 tonal centres** (the twelve pitch classes) combined with one of **21 modes**, giving 252 possible key/modes." — §1, *Which key/modes Architectural Layer 3 recognizes* (locator: lines 1…
   Row 7.48 [RELOCATED] modal readings beyond major and minor cannot be checked against the gr :: …*Outgoing statement.* "(Recognizing all 21 modes does not mean all 21 can be *measured*: the human Roman-numeral ground truth used to grade this layer, Sectio…
   Row 7.56 [QUARANTINED] the style preset as a weak prior over the modes.** *WITHHELD — D-345. :: …*Outgoing statement.* "The preset enters here as a **weak prior on which of the 21 modes are likely in this style** — the per-mode bias values in the scorer (Baroque pushes the prior toward major an…
   Row 7.162 [QUARANTINED] the scorer is a mode-complete descendant of key-profile correlation. :: …*Outgoing statement.* "Our scorer is a richer, mode-complete descendant (all 12 tonics × 21 modes), so it works in any musical style, not only major/minor." — §14 (locator: lines 479–480).…
   Row 12.50 [HISTORICAL] retirement 2: the legacy tonality emission and the hand-set change cos :: …I-147) and the key-mode decoder's hand-set change costs (OI-91/OI-97) → superseded by the two-mode joint state and fitted key factors;" — the section *The sanctioned dual path and the retirement map*, item 4.…
   Row 17.52 [QUARANTINED, RELOCATED, QUARANTINED, QUARANTINED, QUARANTINED] the chord-track writer's record path: the Roman numeral, the display s :: … gates read the stored bucket; the borrowed-key source-key search is restricted to the C1 two modes (the exotic-mode enumeration + the 0.35 mode-suffix gate are legacy-arm-only, inert on the record arm by two-…
   Row 17.57 [QUARANTINED] one shared per-segment mapping for the span and the note seams. :: …the span seam `analyzeSectionFromRecord` and the note seam derive the committed reading + two-mode key + §3.3 alternatives in ONE place — the span loop then adds only `tones`, which the note view carries none…
   Row 17.58 [QUARANTINED, QUARANTINED, QUARANTINED, HISTORICAL, QUARANTINED] what a single note's context carries: the reading and its alternatives :: …3 content score as `identity.score` (the "(%.2f)" suffix); `keyFifths`/`keyMode` = the C1 two-mode key; `keyConfidence` = the RAW §3.3 key-axis gap in nats (a model-internal quantity, NO [0,1] remap); the ped…
   Row 17.66 [RELOCATED] every difference between the arms classified, an unexplained one inves :: …, both readings cited); **presentation-rule** (a ratified rule accounts for it, cited: C1 two-mode display / the §4.1 exposure gates / OI-194 pedal suspension / §3.3 alternatives ordering / D2 grading-vs-disp…
   Row 22.8 [QUARANTINED] the legacy tonality analyzer, over all twenty-one modes. :: …*Outgoing statement.* "keymodeanalyzer.h/.cpp ← KeyModeAnalyzer, all 21 modes" — §3.1, the directory listing (locator: line 1361).…
   Row 23.182 [QUARANTINED] the key analyzer rates twelve tonics against twenty-one modes. :: …*Outgoing statement.* "**Algorithm:** Scores all 12 possible tonics against all **21 modes** (7 diatonic + 7 melodic minor family + 7 harmonic minor family = 252 candidates) using six orthogonal helpe…
   Row 23.192 [QUARANTINED] twenty-one modes in all. :: …*Outgoing statement.* "}; // 21 modes total" — *Output — `KeyModeAnalysisResult`*, the code block (locator: line 3320).…
   Row 23.205 [QUARANTINED, HISTORICAL] the mode priors, read from the user's preferences; they replaced a fou :: …le Parameters — `KeyModeAnalyzerPreferences`* (locator: lines 3351–3353). Two claims: (i) twenty-one priors, filled from the user's preferences in the bridge; (ii) they replaced a four-tier grouping.…
   Row 23.345 [QUARANTINED] the Contemporary preset's mode priors, the final weights set by an opt :: …*Outgoing statement.* "| Contemporary | All 21 modes at moderate penalty; optimizer determines final weights from corpus |" — §4.6 *User Preferences — Configurati…
   Row 33.15 [QUARANTINED] the modal extension to twenty-one modes. :: …*Outgoing statement.* "Modal extension — melodic minor and harmonic minor families (21 modes total)" — *Phase 1 — Analysis Foundation* (locator: line 7869).…
   Row 47.1 [HISTORICAL] the principles amendment and all five recommendations ratified by the  :: … slice is the first delivered step; the marginal completion is rowed **OI-193**), **C1** (two-mode key + published un-rounded modal reading), **D1** (tables embedded as provenance-stamped generated source), *…
   Row 47.28 [ADOPTED — carried, RELOCATED, ADOPTED — carried] the two-mode tonality on the surface; the modal reading beside it; no  :: …*Outgoing statement.* "**Option C1 — the surface carries A's two-mode key; the un-rounded modal reading is published beside it as its own fact; no 21-value mode label is ever infe…
   Row 48.29 [ADOPTED — carried, ADOPTED — carried] the mode axis major and minor, the minor a composite with variable six :: …fied 2026-07-19).** The joint state's mode axis is **{major, minor}** — minor meaning the composite minor practice (natural/harmonic/melodic as one key with variable sixth and seventh degrees)." — §5a, the mode voca…
   Row 48.33 [ADOPTED — carried] the inference states two-mode under every preset.** *WITHHELD — D-524. :: …*Outgoing statement.* "Inference states stay two-mode under every preset." — §5a, the mode vocabulary (locator: line 102).…
   Row 49.31 [ADOPTED — carried] no 21-value mode label inferred or published anywhere.** *WITHHELD — D :: …*Outgoing statement.* "No 21-value mode label is inferred or published anywhere (C1); the two-mode key plus this table informationally dominates the retired labels (#12)." — §3.4 *Per key run* (locator: lines…
==================== OQ-L2-3b
-- term /signature prior|key-signature prior|weak prior|soft prior/: 13 rows
   Row 4.11 [ADOPTED — proposed, ADOPTED — carried] the bass-scale-degree prior is admitted as a soft prior and tie-breake :: …Outgoing statement.* "**The bass-scale-degree / Rule-of-the-Octave prior is admitted as a SOFT prior and TIE-BREAKER only, never a gate (D-585).**" — the second standing constraint (locator: lines 2120–2121). T…
   Row 5.156 [QUARANTINED] the both-licensed case: where both readings are licensed, the progress :: …ral steps (the transition rule's passing-within-the-prevailing-harmony arm, then the §5.7 soft prior) and, where those do not separate it either, to the honest open mark." — §5.5 (locator: lines 415–420).…
   Row 5.197 [ADOPTED — proposed, ADOPTED — carried] it is used only as a soft prior and tie-breaker, never as a gate. :: …*Outgoing statement.* "It is used **only** as a soft prior and tie-breaker in §5.2 and §5.5, **never as a gate**: it is many-to-one, direction-dependent, and overridden…
   Row 5.245 [ADOPTED — proposed, ADOPTED — carried] D5: the bass-scale-degree prior is soft, never a gate. :: …-scale-degree prior is soft, never a gate.**" — §9 (locator: line 640). Two claims: (i) a soft prior; (ii) never a gate.…
   Row 7.56 [QUARANTINED] the style preset as a weak prior over the modes.** *WITHHELD — D-345. :: …*Outgoing statement.* "The preset enters here as a **weak prior on which of the 21 modes are likely in this style** — the per-mode bias values in the scorer (Baroque pushes …
   Row 48.48 [ADOPTED — carried, UNPLACED] a weak, fitted soft prior on the tonality from the signature; the decl :: …clared-mode prior (user-ratified 2026-07-19).** A **weak, fitted, transposition-invariant soft prior on (tonic, mode)** from the notated signature — a small categorical table (local-key tonic distance from the …
   Row 48.49 [ADOPTED — carried] no gate and no threshold: the weak prior decides only where the eviden :: …ere the analysis is otherwise unsure — is delivered by the probability calculus itself (a weak prior is negligible where the content likelihood is decisive and tips the scale only where the evidence is ambiguou…
   Row 48.50 [ADOPTED — carried] Bach's modal notation handled statistically: mass one fifth away, no s :: …led statistically as measured mass one fifth away in minor — no special case." — §5a, the signature prior (locator: lines 176–178).…
   Row 48.51 [ADOPTED — carried] a signature change within the piece re-anchors the prior.** *WITHHELD  :: …ce signature change re-anchors the prior (discharging the OI-94(a) deferral)." — §5a, the signature prior (locator: lines 178–179).…
   Row 48.52 [RELOCATED] the signature's influence measured by ablation and published at every  :: … fitted weight or influence rate is a #3 finding to investigate, not to ship." — §5a, the signature prior (locator: lines 179–182).…
   Row 48.53 [HISTORICAL] the hard wall on the declared mode retired.** *WITHHELD — D-528. :: …ment.* "**The declared-mode wall (the −7 hard penalty) is formally retired.**" — §5a, the signature prior (locator: line 182).…
   Row 48.54 [HISTORICAL] whether the prior acts on the first tonality only, left to the desk si :: …cts as a weak persistent pull is settled by the desk simulation, not assumed." — §5a, the signature prior (locator: lines 183–184).…
   Row 48.55 [ADOPTED — proposed] the signature's other role, naming the collection, a separate factor u :: …on, the OI-168 mask — is a different factor and untouched by this decision.)*" — §5a, the signature prior (locator: lines 189–190).…
==================== OQ-L2-6b
-- term /in-selection output|output stops changing|stop condition/: 19 rows
   Row 6.53 [ADOPTED — carried, QUARANTINED] at the selection edge, request an extension; at the score boundary, pr :: …ural Layer 4 either **requests an extension** (one harmony's worth, the same bound as the stop condition above) or, if Architectural Layer 1 reports the **score boundary**, proceeds with the truncated window." — §2…
   Row 7.62 [QUARANTINED] the reach-back's direction, stop condition and hard bound. :: …unded-context contract (`cowork_bounded_context_design.md`): direction = earlier in time, stop condition = *"the prevailing key before the selection is in view,"* hard bound = a maximum reach, terminating at the sc…
   Row 21.48 [ADOPTED — carried, RELOCATED, QUARANTINED, RELOCATED, RELOCATED, HISTORICAL] the current span names and what bounds each. :: …bounded look-ahead a deferred decision integrates over — bounded by the deferring layer's stop condition and hard bound, per the Bounded-context contract below) · the **cadential scope** (the span a cadence closes …
   Row 21.59 [ADOPTED — carried, ADOPTED — carried] the analysis runs on the selection; a layer needing more requests an e :: …ension from L1 (a data-supply call down the stack, not an analysis back-edge), carrying a stop condition and a hard bound." — §2.15, the bounded-context contract (locator: lines 1171–1173). Two claims: (i) the anal…
   Row 41.78 [RELOCATED] the grouping only surfaces the cue; extending is the orchestrator's de :: …ontract, `cowork_bounded_context_design.md` §6) under the §2.15 bounded-context contract (stop condition + hard bound), never L6's." — §5.1 *Punctuation-span segmentation* (locator: lines 218–222).…
   Row 43.75 [ADOPTED — carried, RELOCATED, ADOPTED — carried] a layer needing more requests an extension; the supplier loads more no :: …nly, clamping at — and reporting — the score boundary; the requesting layer carries the **stop condition** and a **hard bound**, so extension terminates." — §2 *The layer model*, bounded context (locator: lines 204…
   Row 45.12 [ADOPTED — carried] the principled stop is convergence: extend until the in-selection outp :: …*Outgoing statement.* "The principled stop is **convergence**: extend until the layer's **in-selection output stops changing** with further context." — §3 *The bounded-context contract*, item 6 (locator: lines 63–64).…
   Row 45.26 [ADOPTED — carried, ADOPTED — proposed] a refused extension: proceed on truncated evidence, and the output car :: … "When an extension is refused (hard bound, score boundary at a *selection* edge with the stop condition unmet, or a driver-level safety cap), the layer proceeds on truncated evidence AND the affected output carrie…
   Row 45.32 [ADOPTED — carried] the request: extend in one direction until the stop condition, the har :: …tural Layer 1: *"extend the loaded span in direction D (earlier / later in time) until my stop condition holds, or my hard bound is reached, or the score boundary is reached."*" — §4 *The protocol*, the request (lo…
   Row 45.39 [ADOPTED — carried] the requester tests its stop condition again and may extend again. :: …*Outgoing statement.* "The requesting layer re-tests its stop condition; if still unmet and neither the hard bound nor the score boundary is reached, it may extend again." — §4 *The…
   Row 45.44 [ADOPTED — proposed, QUARANTINED] only the slices the new music reaches infer again; composed with the e :: …d decays inward), so only the affected slices re-infer — the same locality that makes the stop condition terminate, and which composes with the existing *"re-analyse a sub-range"* capability." — §4 *The protocol*, …
   Row 45.47 [RELOCATED, ADOPTED — carried] the supplier holds no analysis knowledge; the decision to extend and t :: …It holds **no analysis knowledge** — it supplies notes; the *decision* to extend, and the stop condition, belong to the requesting layer (single responsibility)." — §5 *Per-layer roles*, Architectural Layer 1 (loca…
   Row 45.70 [ADOPTED — proposed] the cost per extension bounded by the stop condition and the hard boun :: …*Outgoing statement.* "**Re-slice / re-decode cost per extension** — bounded by the stop condition and the hard bound; the hard bound prevents runaway reach-back." — §8 *Risks & the non-trivial parts* (locato…
   Row 45.85 [ADOPTED — carried] glossary: the stop condition, the requesting layer's test of enough mu :: …*Outgoing statement.* "**Stop condition** — the requesting layer's "enough context now" test." — the glossary paragraph (locator: lines 261–262).…
   Row 46.46 [RELOCATED] the axis's components under the bounded-context contract. :: …`): every component analyses the selection, requests append-only extension from L1 with a stop condition and hard bound when its reasoning needs more, and carries the denial/truncation provenance honestly (§8)." — …
   Row 46.114 [RELOCATED] texture classification asks for more music when both its evidence and  :: …f constants), VL-C requests extension (direction: both — later first, earlier only if the stop condition is still unmet; increment: bars — the smallest span that adds enough new motion samples to move a rate statis…
   Row 51.21 [ADOPTED — carried, QUARANTINED] a later layer needs music before the selection; its stop condition its :: …usic was in just **earlier in time than the point where the selection begins** (Layer 3's stop condition for that request is its own — the leading-edge settled key stops changing, `cowork_layer3_keymode_design.md` …
   Row 51.52 [QUARANTINED, RELOCATED] scenario: widening earlier by the requester's own stop condition; the  :: … to extend the covered music **earlier in time** than the selection, iterating by its own stop condition (the leading-edge settled key stops changing — Layer 3's operational test, `cowork_layer3_keymode_design.md` …
   Row 62.43 [] L0/L1 Row 18.27: that the forward cascade is bounded because a carried :: …d decays inward), so only the affected slices re-infer — the same locality that makes the stop condition terminate." — `cowork_bounded_context_design.md`, §4 (the L0/L1 row's own locator: lines 144–147).…
==================== OQ-L2-7b
-- term /grad.{0,60}boundar|boundar.{0,60}grad/: 20 rows
   Row 4.16 [RELOCATED] cadences are looked for at phrase ends, read from the graded phrase-bo :: …nces are looked for at phrase ends, which this layer reads as a published L1.5 fact — the graded phrase-boundary profile." — (locator: lines 2144–2146).…
   Row 5.273 [RELOCATED] the phrase-boundary primitive's non-chorale markers are unvalidated. :: …*Outgoing statement.* "**The phrase-boundary primitive's non-chorale markers are unvalidated.** The graded model carries rest- and structural-boundary cues for general (non-chorale) textures, but the corpus is enti…
   Row 5.306 [QUARANTINED, QUARANTINED] two inputs gate the build: the metric weight, resolved as the beat str :: …oundary + phrase segmentation** — **✅ BUILT (dormant) + Cowork-verified 2026-06-26**: the graded per-voice model lives in `engravingbridge/phraseboundaryview.{h,cpp}` (commits `0d10b37a87` de-dup + `5c5d992356` graded model), reachable only behind the default-of…
   Row 5.348 [RELOCATED] in punctuation-poor textures the phrase gate starves the detector. :: …ctuation (the review's F-11 — "unendliche Melodie": no fermatas, elided phrase ends, flat graded boundary-strength profile) the gate **starves** the detector and everything downstream of its votes." — §15, item 11 …
   Row 9.152 [QUARANTINED] the L5 combined boundary confidence is non-monotone. :: …*Outgoing statement.* "**L5 combinedBoundary:** **not Class-P-upgradable as-is** — non-monotone mid-range (the 0.6–0.8 band scores below the 0.5–0.6 band)." — §4.5, item 1 (locat…
   Row 34.4 [UNPLACED] outside the scope: post-tonal, serial and non-Western music, degrading :: … operation, film synchronization, adaptive game music, non-Western traditions (graceful degradation at boundary), post-tonal and serial music (graceful degradation at boundary), audio transcription from recording, spatia…
   Row 40.5 [RELOCATED] the boundary-strength profile: graded per onset, published as a margin :: …*Outgoing statement.* "| **Boundary-strength profile** | The graded per-onset measure of §4 (per-voice, and aggregated to the texture). Its published form is a **Class-M bound…
   Row 40.8 [RELOCATED] from the notated surface alone, a graded profile, the picked ticks and :: …*Outgoing statement.* "This primitive computes, from the notated surface alone, a **graded boundary-strength profile** over the score — a per-onset measure of how strongly the surface evidence marks a phrase …
   Row 40.52 [RELOCATED] a sudden tempo change, or a written ritardando into an arrival. :: …g statement.* "a **sudden (subito) tempo change** — a new tempo marking reached with **no gradual transition** (a structural section/phrase boundary, spiked at the change), or a **written ritardando / rallentando** — a notated slowing into an arrival (spike…
   Row 40.97 [RELOCATED] a graded model, not a binary union. :: …*Outgoing statement.* "**D4 — A graded boundary-strength model, not a binary union (user-ratified 2026-06-26).**" — §6 *Architecture decisions* (locator: li…
   Row 40.135 [RELOCATED] glossary: the sudden tempo change and its gradual counterpart. :: …going statement.* "**Sudden (subito) tempo change** — a new tempo marking reached with no gradual transition; a sparse, high-precision structural-boundary marker (§4.2). A written ritardando/rallentando into an arrival is the gradual counterpart." — §9 *Glossary*…
   Row 40.157 [RELOCATED] a per-part marker should reach the texture only through voice-coincide :: …ach a **texture** boundary only through the same **voice-coincidence aggregation** as the graded cues (§4.3) — a lone breath then yields a **per-voice** boundary (already exposed by this primitive, and the raw material for the future voice-leading / melody-line axis, `c…
   Row 41.54 [RELOCATED] it consumes the phrase-boundary primitive's ticks and strengths. :: …*Outgoing statement.* "**The phrase-boundary primitive** (`phraseBoundaryView` — `phraseBoundaryTicks()` and the graded `PhraseBoundaryProfile`): the boundary ticks and their strengths (fermata / breath / rest / barline / key-s…
   Row 41.139 [RELOCATED] the one chorale without a fermata handled in the metric. :: …case for the fermata punctuation-span oracle (handle in the metric, e.g. fall back to its graded boundary, or exclude from the fermata-recall denominator — a §10 metric detail, not a layer rule)." — §11 *Risks & te…
   Row 44.33 [ADOPTED — carried, UNPLACED, HISTORICAL] the strength of a boundary, harmonic rhythm as a cadence-approach sign :: …ED from this layer: **boundary STRENGTH** (how decisive the change-point evidence was — a graded boundary confidence instead of a binary cut; useful for tonicization-boundary arbitration and for the segmentation-ed…
   Row 46.53 [RELOCATED] the phrase-boundary primitive's per-voice cues as phrase evidence, rea :: …*Outgoing statement.* "**The L1.5 phrase-boundary primitive** (its graded profile + per-part cue/scope provenance; evidence for VL-E when designed): the per-part cues (breath, caesu…
   Row 47.23 [ADOPTED — carried, HISTORICAL, HISTORICAL] the contract the full posterior; the slice delivered first; the comple :: …ii) the completion to the marginals is a named step with its own row, not an indefinite upgrade. *Boundary mark:* the sentence opens on D-425's home as cited, the one line 282, and runs past it; the decisions regist…
   Row 52.10 [RELOCATED, HISTORICAL] the phrase-boundary strength: max-normalized, comparable within one pi :: …*Outgoing statement.* "| L1.5 phrase-boundary | boundary-at-tick | graded boundary strength, max-normalised per profile → [0,1] | M (salience-margin variant) | Relative salience wit…
   Row 52.13 [QUARANTINED, QUARANTINED, QUARANTINED] the function confidence a composite to be published squashed; unbounde :: …ternally, publish the squashed form. **Stage-5 calibration (Phase 3, 2026-07-06): combinedBoundary NOT Class-P-upgradable as-is — non-monotone mid-range re-confirmed on corpus `c50002fee1` (the 0.6–0.8 band below the 0.5–0.6 ba…
   Row 52.31 [RELOCATED] the deliverable: reliability curves and maps upgrading each confidence :: …*Outgoing statement.* "Deliverable: reliability curves + fitted maps that upgrade each boundary confidence from Class M to Class P." — §6 *Calibration obligations (Stage 5)* (locator: lines 117–118).…
-- term /re-?annotat|restrike|same chord/: 9 rows
   Row 6.68 [QUARANTINED] the consumers: the function layer, the grouping layer, the later settl :: …mbol *in* the key); Architectural Layer 6 (grouping — merges adjacent slices carrying the same chord-and-membership); and the later function step that resolves the slices marked "uncertain."" — §3 (locator: lin…
   Row 13.26 [UNPLACED, HISTORICAL] the same music in different voicings should give the same chord. :: …*Outgoing statement.* "Same music in slightly different voicings should produce same chord ID; NCT detection stabilizes this if voice-leading context is consistent." — the section *Quality impact esti…
   Row 17.37 [QUARANTINED, RELOCATED] every seam passes the same excluded staves; the analysis's own written :: …*Outgoing statement.* "Each record-arm seam threads the SAME chord-track exclude set its legacy arm passes (arm-for-arm input parity), so a populated chord track's own notes ar…
   Row 17.52 [QUARANTINED, RELOCATED, QUARANTINED, QUARANTINED, QUARANTINED] the chord-track writer's record path: the Roman numeral, the display s :: …x gate are legacy-arm-only, inert on the record arm by two-mode construction); `kSameChordReannotationGap` (960) is a declared presentation-timing constant." — subsection (3) (locator: lines 185–193). Five cla…
   Row 22.119 [QUARANTINED] the same chord may answer differently on the two paths. :: …*Outgoing statement.* "The same chord can therefore in principle answer differently on P4 vs P3." — §3.3, D-P4 (locator: lines 2339–2340).…
   Row 24.52 [QUARANTINED] the notation path merges repeated slices of the same chord into one re :: …e notation bridge now uses the same collapse rule, so repeated slices that analyze to the same chord merge into one region even in preserve-all mode." — §5.8 *Known Analyzer Limitations*, *bassNoteRootBonus mis…
   Row 43.150 [ADOPTED — carried] a passing-tone slice carries the same chord analysis and merges. :: …* "A passing-tone slice that layer 3 labels as "still chord X (with an NCT)" carries the *same chord analysis* as its neighbors, so grouping merges `[X][X+passing→X][X]` into one `X` region with the NCT annotat…
   Row 43.161 [RELOCATED, ADOPTED — carried] several slices to one annotated event, all carrying the same analysis. :: …acle event, and they should all carry the **same** analysis (or be NCT-flagged within the same chord)." — §6.5 *Cross-cutting — slices vs oracle events* (locator: lines 410–411). Two claims: (i) several slices …
   Row 44.69 [ADOPTED — carried] grammar rated per candidate tonality over the same chords; the tonalit :: …*Outgoing statement.* "Grammaticality is scored PER CANDIDATE key over the same chord sequence — the key is a hypothesis index, not an input." — §8, the circles, the fifth (locator: lines 191–193…
==================== OQ-L2-8b
-- term /very large|large scores|whole orchestral|orchestral/: 6 rows
   Row 5.1 [RELOCATED] the perfect/imperfect distinction rests on the bass-derived inversion; :: … on the **top voice** — the highest sounding voice is not reliably the structural melody (orchestral doubling; barbershop lead below the top), so the call is made on the **bass-derived inversion** criterion and…
   Row 5.311 [RELOCATED] demoted: the perfect/imperfect call is made on the bass-derived invers :: … is demoted: **the highest sounding voice is not reliably the structural melody** (§5.2 — orchestral doubling, barbershop lead below the top), so the perfect/imperfect call is made on the **bass-derived inversi…
   Row 40.74 [RELOCATED, RELOCATED] chorale-inert by construction, and to be validated on orchestral and c :: …vention every voice holds together, so global and per-voice coincide — and it matters for orchestral and contrapuntal textures, where it is to be validated (§8)." — §4.4 *Peak-picking* (locator: lines 214–216).…
   Row 40.151 [HISTORICAL] both first-cut simplifications, to be pinned with non-chorale cases. :: … proportionate first-cut simplifications, inert while dormant; pin them with non-chorale (orchestral / non-SATB) test cases." — §11 *Open items* (locator: lines 382–383).…
   Row 40.158 [RELOCATED] the fermata as the borderline case. :: …hen-coincidence is inert on chorales, where all voices hold together, and more correct on orchestral scores.)" — §11 *Open items*, item 5 (locator: lines 402–404).…
   Row 40.159 [RELOCATED] chorale-inert: the refinement matters only off the chorale texture. :: …a/breathe together, so the texture boundary is unchanged; the refinement matters only for orchestral / contrapuntal (non-SATB) textures — consistent with the byte-identical-on-chorales discipline and adjacent t…
==================== OQ-L2-9b
-- term /chord-bearing|to one line|several pitches|chordal/: 12 rows
   Row 4.10 [RELOCATED] the top voice may nudge the confidence in a chordal texture; it never  :: …*Outgoing statement.* "The top voice may nudge the confidence in a chordal texture; it never decides." — (locator: lines 2115–2116).…
   Row 42.91 [RELOCATED] built on the onset-and-offset slice of the published algorithms. :: …Built on:** the **onset-and-offset "salami slice"** — Pardo & Birmingham, "Algorithms for Chordal Analysis" (Computer Music Journal, 2002), and the verticalization done by **music21's `chordify`** (Cuthbert …
   Row 46.26 [RELOCATED, RELOCATED] a voice of chords a chordal voice, a fact; any reduction of it to one  :: …*Outgoing statement.* "A voice whose events are chords is recorded as a **chordal voice** (a fact); any reduction of a chordal voice to a single line for feature purposes is a **declared redu…
   Row 46.73 [RELOCATED] a chordal voice a recorded fact, marked per event. :: …*Outgoing statement.* "**Chordal voices are a recorded fact,** not an error: a voice whose events carry multiple simultaneous pitches (keyboar…
   Row 46.75 [RELOCATED] one reduction offered: the top note of each event. :: …*Outgoing statement.* "A consumer needing one line from a chordal voice names a reduction rule (v1 provides exactly one: **top-note** — the highest sounding pitch per event, t…
   Row 46.83 [HISTORICAL] the declarations owed at the build. :: …preservation convention for "parallel" (semitone vs generic — §15-2) and the treatment of chordal voices (which declared reduction the profile query uses; default top-note, per §5.1)." — §5.2 *VL-B — motion …
   Row 46.102 [RELOCATED] part-writing checking: parallel perfect intervals, awkward leaps, tend :: …vals — per-voice interval facts), and tendency-tone resolution (leading tone resolves up, chordal seventh down — needs scale degrees, hence the committed L3 key, a D6-checked cross-axis read like VL-F's)." —…
   Row 46.106 [RELOCATED] the per-voice line type: its identity and its ordered events, derived  :: …ne** — voice identity (staff, voice), ordered events (onset, duration, pitches, spelling, chordal flag, and the L1 eligibility flags), losslessly derived from L1." — §7 *Data design* (locator: lines 495–496)…
   Row 46.130 [RELOCATED] the voice-linear view's tests. :: …ing statement.* "**VL-A:** unit tests — losslessness round-trip, tie handling mirrors L1, chordal-voice marking, reduction-rule provenance; every branch covered (the full-coverage standing objective applies …
   Row 46.131 [RELOCATED] the profiles' tests: hand-built fixtures and the study-parity check. :: …oice fixtures give an oracle by construction (each motion type, holds, both-static drops, chordal-voice reduction); plus the **study-parity check**: reproduce the Python pipeline's profiles on a pinned sampl…
   Row 46.140 [HISTORICAL, RELOCATED] other reductions deferred; the top note the one rule of the first vers :: …*Outgoing statement.* "**Alternative declared reductions** for chordal voices (bass-note, per-stream post-VL-D) — comparison deferred until a consumer needs one; top-note is the si…
   Row 46.158 [RELOCATED] the advisory's design owns the construction, by two routes. :: …pt-checked 46 consecutive-5th/8ve instances in the Bach chorales (categorized fermata/NCT/chordal) + Fitsioris-Conklin's 18 parallel-5th passages — with the remaining chorales as near-negatives; (ii) a synth…
==================== OQ-L2-12b
-- term /window/: 88 rows
   Row 2.43 [UNPLACED] a global tonic anchor enters at resolver or section scope, never as on :: … enters key scoring at RESOLVER / SECTION scope — never as one more local term inside the window scorer. ⚠ LEGACY: both mechanisms it names are legacy-scoped.**" — the second standing rule (locator: lines 1…
   Row 2.44 [HISTORICAL] section-level evidence applied where the section is decided, the per-w :: …pe the removed declared anchor occupied — gating the relative-major/minor choice; the per-window candidate scoring is left unchanged." — (locator: lines 1880–1883).…
   Row 2.45 [QUARANTINED] the LEGACY mark follows a check at the code: neither named mechanism i :: …statement.* "**The LEGACY mark follows a check at the code, not the decision's age:** the window scorer this rule excludes (`KeyModeAnalyzer::analyzeKeyMode`) is reached only through the legacy resolver and…
   Row 5.72 [QUARANTINED, ADOPTED — carried] the span is bounded by a look-ahead window and carries no single-key a :: …*Outgoing statement.* "It is bounded by a **look-ahead window** (≈ one punctuation-span's extent — far enough to reach the cadence a few slices later); it carries **no sin…
   Row 5.287 [QUARANTINED] glossary: the region, meaning the decision-context span. :: …e cadence-vote scope (§5.2) and the resolution look-ahead (§5.5), bounded by a look-ahead window (≈ one punctuation-span's extent), no single-key assumption. Distinct from the **key-span** (the modulation r…
   Row 6.3 [HISTORICAL] two refinements deferred to the engage step. :: …*Outgoing statement.* "§15-O2 (bounded-window joint) + C2 (new four-note types) are deferred to the engage step." — the status banner (locator: line 17).…
   Row 6.28 [ADOPTED — carried] the local stepwise treatment of a note is one membership cue. :: …Outgoing statement.* "It *does* use the **local** stepwise treatment of a note within its window — a note approached and left by step is embellishment-like — as one membership cue; that is a property of the…
   Row 6.50 [QUARANTINED] the window extends while the neighbors support one consistent reading. :: …*Outgoing statement.* "The window starts at the slice and its immediate neighbours and extends across contiguous neighbouring slices **while th…
   Row 6.51 [QUARANTINED] the window never reaches past the first inconsistent slice; the next c :: …tent boundary is the operational meaning of "the slice's chord is now fully in view"; the window never reaches past it, because the *next* chord is progression reasoning and belongs to Architectural Layer 5…
   Row 6.52 [ADOPTED — carried] the window must not assume a neighbor slice exists. :: …*Outgoing statement.* "The window must **not assume a neighbour slice exists.**" — §2, *Bounded context at the selection edge* (locator: lines …
   Row 6.53 [ADOPTED — carried, QUARANTINED] at the selection edge, request an extension; at the score boundary, pr :: … or, if Architectural Layer 1 reports the **score boundary**, proceeds with the truncated window." — §2 (locator: lines 151–153). Two claims: (i) at the selection edge the layer requests an extension, and a…
   Row 6.56 [UNPLACED] a notated structural boundary is a second reason the window should not :: …an (§0), which is downstream) is a second, **surface** reason the embellishment/neighbour window should not read across: a neighbour slice *after* a phrase end is not context for the chord *before* it." — §…
   Row 6.57 [ADOPTED — carried, QUARANTINED] a window-truncation prior, and the wide context kept in the key layer. :: …*Outgoing statement.* "It would enter as a **window-truncation prior**, not as wide phrase-length context (which stays in Architectural Layer 3 and feeds forward…
   Row 6.70 [QUARANTINED] the slices read left to right, each within its window. :: …*Outgoing statement.* "Read the slices left to right, each within its window (§2)." — §4 (locator: line 206).…
   Row 6.82 [QUARANTINED, HISTORICAL] one refinement reading is the baseline; a bounded-window alternative i :: …*Outgoing statement.* "One refinement reading is the baseline; a more precise bounded-window alternative is a flagged later refinement (§15)." — §4 (locator: lines 233–234). Two claims: (i) one refineme…
   Row 6.87 [ADOPTED — carried] each sounding note judged a chord tone or an embellishment from its me :: …** or as an **embellishment** (a non-chord tone), read from its melodic motion within the window." — §5, item 3 (locator: lines 253–255).…
   Row 6.96 [QUARANTINED] sufficiency: at least three distinct chord-tone pitch classes. :: … pitch classes** that are chord tones of the candidate (doublings not counted), after the window has gathered and membership has removed the non-chord tones." — §5, item 4, *Sufficiency* (locator: lines 285…
   Row 6.111 [QUARANTINED, QUARANTINED] an arpeggio: each note its own thin slice, the window gathering the fi :: …*Outgoing statement.* "When a chord is arpeggiated, each note is its own thin slice whose window (§2) gathers the figure's notes, so the chord emerges and each slice is named it or inherits it; Architectura…
   Row 6.112 [ADOPTED — carried, UNPLACED, QUARANTINED] the window's gathering is governed by the membership rule, never a poo :: …*Outgoing statement.* "The window's gathering is **governed by the membership rule**, never a pooled recompute (§8): a run of notes forms a cho…
   Row 6.113 [UNPLACED] a phrase-length prolongation is a reduction judgment beyond this layer :: …*Outgoing statement.* "Only short figuration within the window is named here; a phrase-length prolongation of one harmony is a reduction judgment beyond this layer." — §5 (…
   Row 6.130 [QUARANTINED] the layer's settings are tunable values. :: … recognized vocabulary (preset-dependent), the metric-weight and stepwise thresholds, the window's extent, the strength of the key and prevailing-chord preferences, the sufficiency count, and the certainty …
   Row 6.135 [QUARANTINED] narrow context, forward from the key. :: …*Outgoing statement.* "**Narrow context, forward from key** — the window is small and bounded by the slice's own chord (§2); the wide phrase-length context lives in key (Architectura…
   Row 6.157 [QUARANTINED] the chord-root residual is a few percent; the membership call is the l :: …o most remaining quality is in the membership call, whose cue combination (§5 step 3) and window (§2) are the main open tunables." — §11, *The chord axis is near its ceiling; the chord-tone/non-chord-tone c…
   Row 6.170 [QUARANTINED] glossary: the prevailing chord. :: …*Prevailing chord** — the chord of the nearest preceding already-decided slice within the window." — §12 (locator: lines 505–506).…
   Row 6.195 [QUARANTINED] the baseline settles the neighbor dependency with the two-reading sche :: …rship↔neighbour chicken-and-egg with the two-reading scheme (§4)." — §15, *O2 — a bounded-window joint resolution for the neighbour dependency (deferred)* (locator: lines 593–594).…
==================== OQ-L2-13b
-- term /\bNCT\b|non-chord-tone ground truth|annotated non-chord|non-chord-tone annotation|non-chord-tone labels/: 39 rows
   Row 9.273 [HISTORICAL] O-11's open follow-up: a cheap sub-sweep; the Layer-4 fix deferred. :: … the blocking bump (investigate-by-default) may find a smaller feasible gain; the Layer-4/NCT fix (R-14) stays deferred to its proper turn." — §15, O-11 (locator: lines 1032–1033).…
   Row 13.1 [HISTORICAL] deferred until the LLM-triage data shows which gaps the detection woul :: …utgoing statement.* "Deferred until LLM-triage corpus data identifies which analyzer gaps NCT detection would actually address." — the opening lines (locator: lines 4–5).…
   Row 13.2 [ADOPTED — carried] a non-chord tone sounds in a chord region but does not belong to the c :: …*Outgoing statement.* "A non-chord-tone (NCT) is a note that sounds during a chord region but isn't part of the chord's harmonic identity." — the section …
   Row 13.3 [UNPLACED] the common kinds of non-chord tone, named. :: … escape tones, pedal tones, chromatic neighbors, cambiata, échappée." — the section *What NCT detection would do* (locator: lines 10–13).…
   Row 13.4 [QUARANTINED] the analyzer of the document's date does not tell chord tones from non :: …ent.* "Today the analyzer doesn't distinguish chord tones from NCTs." — the section *What NCT detection would do* (locator: line 15).…
   Row 13.5 [QUARANTINED] it counts everything sounding in a region as belonging to the chord. :: …"It labels everything sounding during a region as part of the chord." — the section *What NCT detection would do* (locator: lines 15–16).…
   Row 13.6 [QUARANTINED] that output is correct at the surface but can diverge from the convent :: …h "reads through" passing material to identify the structural chord." — the section *What NCT detection would do* (locator: lines 17–20).…
   Row 13.7 [ADOPTED — carried] most non-chord tones are identified by stepwise approach and resolutio :: …se approach AND stepwise resolution within a single voice line." — the section *What good NCT detection requires*, item 1 (locator: lines 36–38).…
   Row 13.8 [RELOCATED, QUARANTINED] the detection needs durable voice tracking across chord boundaries; th :: …ries — the analyzer doesn't currently track voices as entities." — the section *What good NCT detection requires*, item 1 (locator: lines 38–40). Two claims: (i) the detection needs durable tracking of v…
   Row 13.9 [ADOPTED — carried] non-chord tones typically on weak beats, chord tones on strong. :: …NCTs typically fall on weak beats, chord tones on strong beats." — the section *What good NCT detection requires*, item 2 (locator: lines 41–42).…
   Row 13.10 [QUARANTINED] the analyzer does not consult metric position when scoring chord-tone  :: …tly consult metric position when scoring chord-tone candidates." — the section *What good NCT detection requires*, item 2 (locator: lines 42–44).…
   Row 13.11 [ADOPTED — proposed] the detection must be aware of the idiom, a naive one misclassifying. :: …*Outgoing statement.* "Naive NCT detection misclassifies based on style." — the section *What good NCT detection requires*, item 3 (locator: l…
   Row 13.12 [RELOCATED, UNPLACED] reading the idiom may not use user-written analytical content; structu :: …ion, tempo, key signature density) might be defensible signals." — the section *What good NCT detection requires*, item 3 (locator: lines 48–51). Two claims: (i) detecting the idiom may not read user-wri…
   Row 13.13 [ADOPTED — carried] the classification is confidence-weighted, not boolean. :: …lyzers (music21's various tools, the DCML team's analyses) use." — the section *What good NCT detection requires*, item 4 (locator: lines 53–55).…
   Row 13.16 [ADOPTED — carried] the chord identification aware of non-chord tones is the right fit. :: …*Outgoing statement.* "Shape A is the right architectural fit if NCT detection is pursued." — the section *Architectural fit* (locator: lines 74–75).…
   Row 13.20 [HISTORICAL] the estimate against editorial Roman-numeral analysis: where the detec :: …tgoing statement.* "**On real-music annotations against editorial Roman analysis:** Where NCT detection genuinely helps." — the section *Quality impact estimate* (locator: lines 86–87).…
   Row 13.22 [HISTORICAL] the detection would bring the labels closer to the Roman-numeral conve :: …*Outgoing statement.* "NCT detection would produce annotations closer to traditional Roman numeral conventions: `I — IV — V — I` instead…
   Row 13.24 [HISTORICAL] a naive detector tuned for common practice would strip genuine colorin :: …*Outgoing statement.* "A naive CPE-tuned NCT detector would strip genuine `b9` and `#11` colorings on dominant chords." — the section *Quality impact esti…
   Row 13.26 [UNPLACED, HISTORICAL] the same music in different voicings should give the same chord. :: …oing statement.* "Same music in slightly different voicings should produce same chord ID; NCT detection stabilizes this if voice-leading context is consistent." — the section *Quality impact estimate* (l…
   Row 13.29 [HISTORICAL] suspension detection would clean up the cadence output. :: …*Outgoing statement.* "Cadence detection particularly — suspensions are NCT-by-construction, and proper suspension detection cleans up cadence output significantly." — the section *Qual…
   Row 13.31 [HISTORICAL] step 2: decide from that report whether the detection is the best next :: …*Outgoing statement.* "From that report, decide whether NCT detection is the highest-leverage next investment vs. alternatives (better key inference for non-CPE styles, …
   Row 13.32 [HISTORICAL] step 3: voice tracking, metric weighting, simple detection, measuremen :: …structure → metric-weighting integration → simple PT/NT detection → measurement → broader NCT vocabulary." — the section *Sequencing*, item 3 (locator: lines 140–142).…
   Row 43.118 [HISTORICAL, HISTORICAL] the chord axis near its ceiling; the real work in the slicing and the  :: … work is layer-2/3 (slicing makes over-grab moot; analysis-with-context carries the key + NCT levers)." — §5 *Implications for the upstream-first sweep* (locator: lines 325–326). Two claims: (i) the chor…
   Row 43.131 [ADOPTED — carried] telling chord tones from non-chord tones needs a narrow window: the ne :: …*Outgoing statement.* "Chord/NCT discrimination needs a **narrow** window (the slice + its immediate neighbors + metric strength — enough to s…
   Row 43.133 [HISTORICAL] the lean: the tonality over a wide window first, then the chord given  :: …ent context scopes; *lean:* resolve the **keychain over a wide window first**, then chord/NCT per slice over a narrow window given the local key." — §6.2 *Layer 3 — the analysis* (locator: lines 363–365)…
==================== OQ-L2-15b
-- term /no truncation|full candidate list|full posterior|candidate lists/: 13 rows
   Row 2.8 [ADOPTED — carried] the joint design carries a full posterior by construction. :: …oing statement.* "*For a reader arriving from the joint estimator:* that design carries a full posterior by construction, so the concern this shelving withdrew is met by a different design rather than by reviving t…
   Row 10.53 [ADOPTED — carried] the full posterior retained for the published alternatives and the unc :: …*Outgoing statement.* "The full posterior (not only the best path) is retained for the published alternatives and the uncertainty surface (#12; the car…
   Row 17.16 [QUARANTINED] the published candidate lists: per committed segment, every key and ev :: …ublishes, per committed segment, the ESTABLISHED content-score uncertainty surface as two full candidate lists (no truncation constant): a **KEY axis** — the committed chord class re-scored under every scoreable candida…
   Row 21.30 [QUARANTINED, ADOPTED — proposed] cycling or re-ranking over the per-layer candidate lists adds nothing, :: …D and is not withdrawn: global cycling / re-ranking over the per-layer pipeline's carried candidate lists adds nothing, and that remains binding on any future cycling-style design (#12 — an exclusion is information)…
   Row 47.1 [HISTORICAL] the principles amendment and all five recommendations ratified by the  :: …ations — **A2** (the joint-native record IS the surface), **B-full** (the contract is the full posterior; the established slice is the first delivered step; the marginal completion is rowed **OI-193**), **C1** (two…
   Row 47.8 [ADOPTED — carried] the full posterior retained for the alternatives and the uncertainty s :: …*Outgoing statement.* "The ratified decode plan (factorization §5) requires: "The full posterior (not only the best path) is retained for the published alternatives and the uncertainty surface (#12; the car…
   Row 47.19 [ADOPTED — carried] the decode plan already says it: the full posterior retained. :: …and, before any option is weighed:** the ratified decode plan (§5) already says it — "the full posterior (not only the best path) is retained for the published alternatives and the uncertainty surface (#12)"." — §4…
   Row 47.21 [ADOPTED — carried] all three point one way: the surface is the full posterior. :: …*Outgoing statement.* "All three point the same way: the surface is the full posterior." — §4 *Decision B* (locator: lines 223–224).…
   Row 47.22 [ADOPTED — carried, ADOPTED — carried, ADOPTED — carried] the uncertainty surface the full posterior: marginal mass per span by  :: …*Outgoing statement.* "**Option B-full — the contract's uncertainty surface is the full posterior: per-span/state marginal mass from exact forward-backward over the decode lattice, published as model probabi…
   Row 47.23 [ADOPTED — carried, HISTORICAL, HISTORICAL] the contract the full posterior; the slice delivered first; the comple :: …locator: lines 282–284). Three claims: (i) the contract of the uncertainty surface is the full posterior; (ii) the local slice, established and a strict subset of that surface, is the first step delivered; (iii) th…
   Row 49.22 [QUARANTINED, HISTORICAL] both axes publish the full lists of candidates; the runner-up wording  :: …n 1, 2026-07-26, at the posterior-slice delivery):** both axes publish the FULL scoreable candidate lists — the original "runner-up" / "top-N" wording is superseded." — §3.3, the second amendment (locator: lines 108…
   Row 49.23 [UNPLACED, ADOPTED — carried, RELOCATED] no truncation constant; nothing computed discarded at the boundary; di :: …*Outgoing statement.* "No truncation constant exists anywhere in the publication (a breadth "N" or a gap-window width would be a hand-set value wi…
   Row 62.48 [ADOPTED — carried, ADOPTED — carried] L0/L1 Row 25.5: the decided segment boundary's marginal mass, *"L2's p :: …clared loss, a passage whose boundary is ambiguous looking artificially certain; (ii) the full posterior leaves no mass invisible, the mass across segmentations every local slice hides included.…
==================== OQ-L2-16b
-- term /unfold|volta|notated order|performed order/: 0 rows
-- term /\brepeat/: 20 rows
   Row 5.39 [RELOCATED] a section end is a phrase boundary that coincides with a structural bo :: …hrase boundary that **also coincides with a structural score boundary** — a double bar, a repeat mark, or the end of the piece — used only as the section-end salience cue in §5.2.)" — §3 (locator: lines 95–…
   Row 7.64 [QUARANTINED] the built reach-back loop: its trigger, its action and its stop. :: …sk Architectural Layer 1 to `extend(Earlier)` → re-slice (Layer 2) → re-decode (Layer 3), repeated until the leading-edge **settled** key stops changing across iterations (settled = not "uncertain" and at-o…
   Row 10.47 [QUARANTINED, ADOPTED — carried] exactly equal candidate scores between decodes are real; unbroken, the :: … real (proven at 8 corpus pieces — equal-score segmentations differing by one boundary on repeated-chord runs) and, unbroken, they make the committed output depend on the platform's floating-point library —…
   Row 23.179 [QUARANTINED] the mode-name helpers use separate arrays per mode family. :: …TonicOffset()` use separate static arrays per mode family and share comment patterns that repeat the same "mode family / parent key signature" logic." — §4.1i *Technical Debt and Refactor Backlog (reviewed …
   Row 23.255 [HISTORICAL] stop when the same winner survives repeated expansion. :: …*Outgoing statement.* "the same winner survives repeated expansion" — *Phase 1b — Minimal Monophonic Fallback Without Chord Symbols* (locator: line 3666).…
   Row 24.52 [QUARANTINED] the notation path merges repeated slices of the same chord into one re :: …*Outgoing statement.* "The notation bridge now uses the same collapse rule, so repeated slices that analyze to the same chord merge into one region even in preserve-all mode." — §5.8 *Known Analy…
   Row 24.81 [HISTORICAL] repeated identical labels on dense piano writing. :: …*Outgoing statement.* "Dvořák Silhouettes and Chopin Mazurkas show repeated identical chord labels (e.g. `Bb×8`, `Fsus×20`) from Jaccard boundary firing on dense arpeggiated texture."…
   Row 40.50 [RELOCATED] a double, final or repeat barline. :: …*Outgoing statement.* "a **double, final, or repeat barline** (a structural division — treated, for this primitive, as a phrase boundary);" — §4.2 *The determini…
   Row 40.104 [RELOCATED] oracle tests of the cues and the picking on constructed cases. :: …ak; a long note among short ones yields an inter-onset peak; a fermata and a double/final/repeat barline yield marker spikes; a single mid-phrase leap does **not** clear the threshold alone; a region contai…
   Row 40.139 [RELOCATED] glossary: the structural barline. :: …*Outgoing statement.* "**Structural barline** — a double, final, or repeat barline (a notational division)." — §9 *Glossary* (locator: line 353).…
   Row 44.7 [RELOCATED] time signatures, barlines including double and section barlines, repea :: …*Outgoing statement.* "Time signatures; barlines including double/section barlines; repeats." — §1 *The score itself* (locator: line 23).…
   Row 45.13 [UNPLACED, ADOPTED — carried] the test applied directly to the quantity the extension was asked for; :: …nfers over the enlarged span, compares that quantity step against step, and stops when it repeats." — §3 *The bounded-context contract*, item 6 (locator: lines 66–67). Two claims: (i) the convergence test i…
   Row 45.14 [QUARANTINED] the built reach-back tracks the leading-edge settled tonality and stop :: …actly this — it tracks the **leading-edge settled key across iterations and stops when it repeats**, which is the criterion itself and not a stand-in for it (the convergence note above the reach-back loop i…
   Row 45.50 [QUARANTINED] reach-back an extension request: earlier, stopping when the leading-ed :: …k **is** an extension request: direction = earlier, stop = *"the leading-edge settled key repeats across iterations"*, bound = a maximum reach." — §5 *Per-layer roles*, Architectural Layer 3 (locator: lines…
   Row 45.92 [QUARANTINED, ADOPTED — carried] what it changes in the tonality layer's specification. :: … framed as an extension request (direction = earlier, stop = the leading-edge settled key repeats across iterations, hard bound); leading-edge window behaviour (request-or-truncate)." — §10 *Spec propagatio…
   Row 46.30 [RELOCATED] the interval profile: a per-voice histogram of intervals and the repea :: …nterval statistics of a span: the |interval|-in-semitones histogram (bins 0–11, ≥12) plus repeat/step/leap rates (repeat = 0, step = 1–2, leap ≥ 3 semitones)." — §0, *This design's operational terms [VL]* (…
   Row 46.109 [RELOCATED] the interval profile type. :: …*Outgoing statement.* "**IntervalProfile** — histogram bins + repeat/step/leap rates + note count, per voice or aggregated." — §7 *Data design* (locator: line 501).…
   Row 53.17 [RELOCATED] a harmonic sequence: the same progression repeated at successive trans :: …*Outgoing statement.* "**Harmonic sequence** — the same progression repeated at successive transpositions (Monte, Fonte, a descending-fifths sequence)." — §0, the terms, row *Harmonic …
   Row 53.50 [RELOCATED, UNPLACED] a sequence at least two transposed statements of the same entry; its e :: …sequence requires ≥2 transposed statements of the SAME recognised entry** — that is what "repeated at successive transpositions" (§0) means; a run's `repetitions` counts the matched windows, and the evidenc…
   Row 62.44 [] L0/L1 Row 18.31: that reach-back IS an enlargement request, with its d :: …k **is** an extension request: direction = earlier, stop = *'the leading-edge settled key repeats across iterations'*, bound = a maximum reach." — `cowork_bounded_context_design.md`, §5, third bullet (the L…
rows indexed: 4642
```

### B.2c — §8: the third search pass, every hit printed

*Saved to scratch as `s8search_out3.txt`.*

```
==================== OQ-L2-5c
-- term /\bpivot/: 20 rows
   Row 10.43 [UNPLACED] P5: the entry chord depends only on the new key. :: …nds only on the new key | ASSUMPTION (weaker than Raphael-Stoddard's, which we replace) | Pivot-chord modulation says entry depends on the OLD key too (the pivot is diatonic in both); visible as entry-tabl…
   Row 11.52 [RELOCATED, HISTORICAL] the need for key and modulation ground truth. :: …modulation_dataset` upstream (direct-acquisition candidate, next corpus increment). Sears pivots: no public deposit. SWD score-aligned local keys unchanged (ChoCo). WiR analyses still carry local keys gene…
   Row 13.27 [HISTORICAL] the estimate for the features downstream: indirect improvement. :: …*Outgoing statement.* "**On downstream features (cadence, pivot, key inference):** Indirect improvement." — the section *Quality impact estimate* (locator: lines 105–106).…
   Row 20.5 [QUARANTINED] the chord staff: a part the user adds, filled on demand with the harmo :: …n numerals, canonical or collected voicings, key/mode annotations, borrowed chord labels, pivot detection, and cadence markers." — §1.4 *Implemented Components* (locator: lines 654–658).…
   Row 22.107 [QUARANTINED] the section analyzer: stabilization, cadence and pivot detection. :: … | Section-level unified analysis — `analyzeSection`, key/mode stabilization, cadence and pivot detection (`detectCadences`, `detectPivotChords`). Moved here in Stage 2.1 (Phase 4c). |" — the region-analys…
   Row 22.109 [QUARANTINED] the section-level analysis's home. :: …* "Section-level unified analysis — `analyzeSection`, key/mode stabilization, cadence and pivot detection — lives in `composing/analysis/section/`." — §3.3, the section-level analysis (locator: lines 2297–…
   Row 23.320 [QUARANTINED] above the second staff: the borrowed-chord mark, the pivot label and t :: …e key (e.g. "Bb min") when a non-diatonic chord has an identifiable diatonic source, plus pivot label (e.g. "pivot: IV → I in G maj") at modulation boundaries and cadence marker (PAC, HC, DC, PC); these ar…
   Row 30.45 [QUARANTINED] and the key-dependent markings only above a higher one. :: …*Outgoing statement.* "Key signatures, modulation relationship labels, pivot labels, borrowed-chord markers, and cadence markers are written only when confidence is at least 0.8" — §11.5…
   Row 30.57 [QUARANTINED] the pivot chord written at a key-region boundary. :: …*Outgoing statement.* "At key region boundaries, annotate the pivot chord when one exists:" — §11.5, the modulation-path annotation (locator: line 7273).…
   Row 30.58 [QUARANTINED] the pivot: the last chord before the boundary diatonic to both keys. :: …he last chord before the key boundary that is diatonic to both the old and new key is the pivot." — §11.5, the modulation-path annotation (locator: lines 7277–7278).…
   Row 30.60 [QUARANTINED] a change of key with no pivot marked as direct. :: …*Outgoing statement.* "When no pivot chord exists (direct chromatic modulation), annotate as "direct modulation"." — §11.5, the modulation-path an…
   Row 30.66 [QUARANTINED] the pivot labels, from the legacy pivot detector. :: …*Outgoing statement.* "Pivot chord labels — **implemented** (Session 14); uses `detectPivotChords()` in `notationcomposingbridgehelpers.cp…
   Row 30.70 [QUARANTINED] no cadence, pivot or applied-dominant markings in the Nashville displa :: …*Outgoing statement.* "No cadence markers, no pivot labels, no tonicization labels." — *Annotate path annotation layers (Roman numeral mode)* (locator: line 7302…
   Row 30.71 [QUARANTINED] the pivot detector looks for assertive changes of tonic or mode betwee :: …*Outgoing statement.* "**Pivot detection** (`detectPivotChords`): scans for assertive key transitions (consecutive regions with different `k…
   Row 30.73 [QUARANTINED] the pivot: the last chord in the selection diatonic to both keys. :: …*Outgoing statement.* "The pivot chord is the last in-selection chord diatonic to both the old and new key." — *Annotate path annotation layer…
   Row 30.74 [QUARANTINED] the pivot label's written form. :: …*Outgoing statement.* "The pivot label format is `vi → ii` (U+2192 RIGHT ARROW, no "pivot:" prefix, no key-name context)." — *Annotate path an…
   Row 43.94 [HISTORICAL, HISTORICAL] the latent spans named when needed; the gradients: tonicization, the p :: …on/Zug); plus the gradients — tonicization (a proto-key-span that did not establish), the pivot (a modulatory overlap), the cadential approach (the pre-dominant→dominant→tonic formula)." — §2 *The layer mo…
   Row 46.72 [RELOCATED] a note serving two lines a question for the stream tier, never for the :: …*Outgoing statement.* "A note serving two perceptual lines (a compound-melody pivot, a voice crossing) is a **stream**-tier phenomenon — whether one note may belong to two streams is a recorded…
   Row 46.151 [RELOCATED] may one note belong to two streams? :: … question** (user-raised 2026-07-03): may one note belong to two streams (compound-melody pivots, voice crossings)?" — §15 *Open items & deferred refinements*, item 8 (locator: lines 694–695).…
   Row 49.44 [RELOCATED] the cadence labels the section layer's derivation over the record. :: …*Outgoing statement.* "| cadence/pivot inputs (7) | section reads of key/degree/quality/confidence | §3.2 + §3.3 (the cadence labels stay the sectio…
==================== OQ-L2-9c
-- term /chordal voice|successor|following note|next note in/: 17 rows
   Row 9.105 [RELOCATED] class-(b) root-disagree duration non-increase on the fitting split. :: …gree duration non-increase on the fitting split's covered cells**, same preset scope (the successor-stop semantics, tracked from day one so the R10 handover is continuous)." — §4.2, *Per-evaluation hard constr…
   Row 9.162 [HISTORICAL] the R10 decision surface assembled once the families are adopted. :: …ng the ratified per-run set-diff semantics; the A-8 instrument emits both forms), and the successor stop semantics (constraint 2)." — §4.7, *Phase 4 — adoption and the R10 re-baseline* (locator: lines 502–505)…
   Row 9.165 [HISTORICAL] R10-a: the decision surface built. :: …ng (every 52/24/52 case still-failing under variant (b), 0 disappear), the runnable+timed successor sandwich (`tools/robust_stop_diff.py`; class-(b) duration non-increase + explained run-diff; ≈6 s), and the D…
   Row 9.236 [QUARANTINED] until the pool broadens, fitted values are Bach-chorale-shaped. :: …g statement.* "Residual risk is real and stated: until the fitting pool broadens (D-5 and successors), fitted values are Bach-chorale-shaped — exactly as the hand-tuned values already are, but now measurably s…
   Row 9.385 [HISTORICAL] the restriction option removed; the override frame collapses to annota :: …strict) is **removed from the near-term option set** — it is joint-step-gated (a Stage-5+ successor), so the F-B frame collapses to **§3.D-1 (annotate-via-open-mark) EVERYWHERE**, floored by disable; recoverin…
   Row 9.399 [RELOCATED] O-15(iv): the successor check, runnable and timed; the hard stop's for :: …*Outgoing statement.* "**(iv) The successor sandwich — runnable + timed:** new instrument **`tools/robust_stop_diff.py`** (thin orchestration over a8 out…
   Row 11.58 [RELOCATED, HISTORICAL] the need for hierarchical harmony trees. :: … README-only repo, the 41 excerpts were never committed (access = dissertation page; 2024 successor arXiv 2408.07184); GTTM located (~300 pairs) but no single artifact + license unclear — access recorded, not …
   Row 22.120 [QUARANTINED] the bridge analyzes its neighbors with no context. :: …utgoing statement.* "`findTemporalContext` analyzes the backward predecessor (and forward successor) with `nullptr` context [code]." — §3.3, D-BRIDGE (locator: lines 2354–2355).…
   Row 23.15 [QUARANTINED, QUARANTINED] the pedal flag, left empty on the record path. :: …structural pedal point (§5.12; empty on the record // path — see §7.4's voice-independent successor)" — *Output — `ChordAnalysisResult`*, the code block (locator: lines 2562–2563). Two claims: (i) the result f…
   Row 23.95 [QUARANTINED] the parent region's bass overrides the sub-region's neighbor basses. :: …ge.cpp` and the main analysis loop in `tools/batch_analyze.cpp` compute the predecessor / successor PARENT region's bass PC and override `subCtx.previousBassPc` / `subCtx.nextBassPc` for each sub-region call."…
   Row 39.281 [HISTORICAL] un-computable, and a long-run successor rather than a near-term choice :: ….* "So the verdict is un-computable rather than unmeasured, and this option is a long-run successor rather than a near-term choice." — §8, *The fine-grain function override — falsified, its repair refuted, its…
   Row 46.26 [RELOCATED, RELOCATED] a voice of chords a chordal voice, a fact; any reduction of it to one  :: …*Outgoing statement.* "A voice whose events are chords is recorded as a **chordal voice** (a fact); any reduction of a chordal voice to a single line for feature purposes is a **declared reduction …
   Row 46.73 [RELOCATED] a chordal voice a recorded fact, marked per event. :: …*Outgoing statement.* "**Chordal voices are a recorded fact,** not an error: a voice whose events carry multiple simultaneous pitches (keyboard writ…
   Row 46.75 [RELOCATED] one reduction offered: the top note of each event. :: …*Outgoing statement.* "A consumer needing one line from a chordal voice names a reduction rule (v1 provides exactly one: **top-note** — the highest sounding pitch per event, the stu…
   Row 46.83 [HISTORICAL] the declarations owed at the build. :: …preservation convention for "parallel" (semitone vs generic — §15-2) and the treatment of chordal voices (which declared reduction the profile query uses; default top-note, per §5.1)." — §5.2 *VL-B — motion & inte…
   Row 46.140 [HISTORICAL, RELOCATED] other reductions deferred; the top note the one rule of the first vers :: …*Outgoing statement.* "**Alternative declared reductions** for chordal voices (bass-note, per-stream post-VL-D) — comparison deferred until a consumer needs one; top-note is the single v…
   Row 51.50 [RELOCATED] scenario: three tied quarters and a following note become two notes. :: …rter-notes followed by a different note become **two** notes — one long held note and the following note — not four notes, and the held note is not counted three times." — §6 *Runtime view (scenarios)* (locator: li…
==================== OQ-L2-10c
-- term /grace/: 16 rows
   Row 22.37 [RELOCATED, RELOCATED, RELOCATED, RELOCATED, RELOCATED, HISTORICAL] the lossless, tie-resolved note model and what it carries. :: …ach `NoteEvent` carries 11 fields: `pitch, tpc, staff, voice, onset, release, duration, isGrace, plays, visible, staffEligible`. Tied groups are merged into **one** span/onset (via the DOM `firstTiedNote`/…
   Row 22.74 [RELOCATED] no note kind is special-cased; grace and tuplet outcomes follow from t :: …*Outgoing statement.* "**No special-casing of any note kind** — grace and tuplet outcomes fall out of the note-model spans as facts (verified at source: a grace event carries onse…
   Row 22.75 [RELOCATED] the slicer needs no grace or tuplet code. :: …*Outgoing statement.* "The slicer needs no grace/tuplet code." — Layer 2 (locator: line 1680).…
   Row 23.336 [QUARANTINED] grace notes always excluded, as ornamental and not harmonic. :: …*Outgoing statement.* "// Grace notes are ornamental, not harmonic — always exclude from analysis" — *Score Traversal Pattern*, the code bloc…
   Row 34.1 [UNPLACED] the core scope, modal and jazz harmony among it. :: …analysis cache, enharmonic spelling, score error detection, musical language detector and graceful degradation, extensible style system, initial five styles, ML interface design throughout, unified tempora…
   Row 34.4 [UNPLACED] outside the scope: post-tonal, serial and non-Western music, degrading :: …d real-time operation, film synchronization, adaptive game music, non-Western traditions (graceful degradation at boundary), post-tonal and serial music (graceful degradation at boundary), audio transcript…
   Row 38.4 [QUARANTINED] grace notes always excluded. :: …*Outgoing statement.* "// Always exclude grace notes — cr->isGrace()" — *Appendix B*, the code block (locator: line 8258).…
   Row 42.88 [QUARANTINED] the old code computed the moments and discarded most of them. :: …ed** most of them by selecting a subset using chord-score thresholds (and it also skipped grace notes and snapped mid-tuplet moments)." — §13 *Background* (locator: lines 214–216).…
   Row 43.26 [RELOCATED] layer 1, the note model: the notated record read once, lossless, with  :: …otated set of sounding notes (pitch, tpc, staff, voice, onset, offset, duration, ties, `isGrace`, `plays`, `visible`, staff-eligibility). Preserved end-to-end. **No** weighting, filtering, or aggregation. …
   Row 43.124 [RELOCATED] the note model keeps the grace notes, flagged. :: …*Outgoing statement.* "Per "collect, don't drop," the note model keeps grace notes flagged `isGrace`." — §6.1 *Layer 2 — the change-point set*, grace notes (locator: line 348).…
   Row 43.125 [RELOCATED, ADOPTED — carried] a grace opens no slice; it is annotated onto the following slice as an :: …*Outgoing statement.* "*Lean:* **a grace does not open a slice of its own** — it is annotated onto the following slice as an ornament, so analysis see…
   Row 43.126 [RELOCATED] a grace an annotation of the note model, not a slicing boundary. :: …*Outgoing statement.* "(Equivalent to treating grace as a layer-1 annotation, not a layer-2 boundary.)" — §6.1 *Layer 2 — the change-point set*, grace notes (loca…
   Row 44.15 [ADOPTED — carried, RELOCATED, ADOPTED — carried] grace notes, slurs, lyrics, tempo markings, pedal lines and part names :: …*Outgoing statement.* "Grace notes (embellishment hints); slurs/articulation (phrase shaping, weak); lyrics/verse structure (chorale phras…
   Row 51.43 [RELOCATED] building walks every staff, voice and position, resolves ties, records :: …uilding the note model walks every staff, every voice, and every time-position (including grace notes), resolves ties, records the per-note facts, and sorts the records by start time." — §5 *Building-block…
   Row 51.53 [RELOCATED] the eleven facts each note record carries. :: …start time — the tie-resolved sounding length); and four yes/no facts — whether it is a **grace note**, whether it actually **sounds** (false for muted notes and for imported cue notes — an imported score …
   Row 51.57 [HISTORICAL, RELOCATED] grace-note timing to be confirmed; no special handling of grace notes. :: …*Outgoing statement.* "**Grace-note timing** — exactly how a grace note's start time, end time, and duration are recorded should be confirme…
==================== OQ-L2-13c
-- term /\bNCT\b|non-chord-tone ground truth|annotated non-chord|non-chord-tone annotation|non-chord-tone labels/: 39 rows
   Row 9.273 [HISTORICAL] O-11's open follow-up: a cheap sub-sweep; the Layer-4 fix deferred. :: … the blocking bump (investigate-by-default) may find a smaller feasible gain; the Layer-4/NCT fix (R-14) stays deferred to its proper turn." — §15, O-11 (locator: lines 1032–1033).…
   Row 13.1 [HISTORICAL] deferred until the LLM-triage data shows which gaps the detection woul :: …utgoing statement.* "Deferred until LLM-triage corpus data identifies which analyzer gaps NCT detection would actually address." — the opening lines (locator: lines 4–5).…
   Row 13.2 [ADOPTED — carried] a non-chord tone sounds in a chord region but does not belong to the c :: …*Outgoing statement.* "A non-chord-tone (NCT) is a note that sounds during a chord region but isn't part of the chord's harmonic identity." — the section …
   Row 13.3 [UNPLACED] the common kinds of non-chord tone, named. :: … escape tones, pedal tones, chromatic neighbors, cambiata, échappée." — the section *What NCT detection would do* (locator: lines 10–13).…
   Row 13.4 [QUARANTINED] the analyzer of the document's date does not tell chord tones from non :: …ent.* "Today the analyzer doesn't distinguish chord tones from NCTs." — the section *What NCT detection would do* (locator: line 15).…
   Row 13.5 [QUARANTINED] it counts everything sounding in a region as belonging to the chord. :: …"It labels everything sounding during a region as part of the chord." — the section *What NCT detection would do* (locator: lines 15–16).…
   Row 13.6 [QUARANTINED] that output is correct at the surface but can diverge from the convent :: …h "reads through" passing material to identify the structural chord." — the section *What NCT detection would do* (locator: lines 17–20).…
   Row 13.7 [ADOPTED — carried] most non-chord tones are identified by stepwise approach and resolutio :: …se approach AND stepwise resolution within a single voice line." — the section *What good NCT detection requires*, item 1 (locator: lines 36–38).…
   Row 13.8 [RELOCATED, QUARANTINED] the detection needs durable voice tracking across chord boundaries; th :: …ries — the analyzer doesn't currently track voices as entities." — the section *What good NCT detection requires*, item 1 (locator: lines 38–40). Two claims: (i) the detection needs durable tracking of v…
   Row 13.9 [ADOPTED — carried] non-chord tones typically on weak beats, chord tones on strong. :: …NCTs typically fall on weak beats, chord tones on strong beats." — the section *What good NCT detection requires*, item 2 (locator: lines 41–42).…
   Row 13.10 [QUARANTINED] the analyzer does not consult metric position when scoring chord-tone  :: …tly consult metric position when scoring chord-tone candidates." — the section *What good NCT detection requires*, item 2 (locator: lines 42–44).…
   Row 13.11 [ADOPTED — proposed] the detection must be aware of the idiom, a naive one misclassifying. :: …*Outgoing statement.* "Naive NCT detection misclassifies based on style." — the section *What good NCT detection requires*, item 3 (locator: l…
   Row 13.12 [RELOCATED, UNPLACED] reading the idiom may not use user-written analytical content; structu :: …ion, tempo, key signature density) might be defensible signals." — the section *What good NCT detection requires*, item 3 (locator: lines 48–51). Two claims: (i) detecting the idiom may not read user-wri…
   Row 13.13 [ADOPTED — carried] the classification is confidence-weighted, not boolean. :: …lyzers (music21's various tools, the DCML team's analyses) use." — the section *What good NCT detection requires*, item 4 (locator: lines 53–55).…
   Row 13.16 [ADOPTED — carried] the chord identification aware of non-chord tones is the right fit. :: …*Outgoing statement.* "Shape A is the right architectural fit if NCT detection is pursued." — the section *Architectural fit* (locator: lines 74–75).…
   Row 13.20 [HISTORICAL] the estimate against editorial Roman-numeral analysis: where the detec :: …tgoing statement.* "**On real-music annotations against editorial Roman analysis:** Where NCT detection genuinely helps." — the section *Quality impact estimate* (locator: lines 86–87).…
   Row 13.22 [HISTORICAL] the detection would bring the labels closer to the Roman-numeral conve :: …*Outgoing statement.* "NCT detection would produce annotations closer to traditional Roman numeral conventions: `I — IV — V — I` instead…
   Row 13.24 [HISTORICAL] a naive detector tuned for common practice would strip genuine colorin :: …*Outgoing statement.* "A naive CPE-tuned NCT detector would strip genuine `b9` and `#11` colorings on dominant chords." — the section *Quality impact esti…
   Row 13.26 [UNPLACED, HISTORICAL] the same music in different voicings should give the same chord. :: …oing statement.* "Same music in slightly different voicings should produce same chord ID; NCT detection stabilizes this if voice-leading context is consistent." — the section *Quality impact estimate* (l…
   Row 13.29 [HISTORICAL] suspension detection would clean up the cadence output. :: …*Outgoing statement.* "Cadence detection particularly — suspensions are NCT-by-construction, and proper suspension detection cleans up cadence output significantly." — the section *Qual…
   Row 13.31 [HISTORICAL] step 2: decide from that report whether the detection is the best next :: …*Outgoing statement.* "From that report, decide whether NCT detection is the highest-leverage next investment vs. alternatives (better key inference for non-CPE styles, …
   Row 13.32 [HISTORICAL] step 3: voice tracking, metric weighting, simple detection, measuremen :: …structure → metric-weighting integration → simple PT/NT detection → measurement → broader NCT vocabulary." — the section *Sequencing*, item 3 (locator: lines 140–142).…
   Row 43.118 [HISTORICAL, HISTORICAL] the chord axis near its ceiling; the real work in the slicing and the  :: … work is layer-2/3 (slicing makes over-grab moot; analysis-with-context carries the key + NCT levers)." — §5 *Implications for the upstream-first sweep* (locator: lines 325–326). Two claims: (i) the chor…
   Row 43.131 [ADOPTED — carried] telling chord tones from non-chord tones needs a narrow window: the ne :: …*Outgoing statement.* "Chord/NCT discrimination needs a **narrow** window (the slice + its immediate neighbors + metric strength — enough to s…
   Row 43.133 [HISTORICAL] the lean: the tonality over a wide window first, then the chord given  :: …ent context scopes; *lean:* resolve the **keychain over a wide window first**, then chord/NCT per slice over a narrow window given the local key." — §6.2 *Layer 3 — the analysis* (locator: lines 363–365)…
   Row 43.143 [ADOPTED — carried, UNPLACED] embellishments judged chord-first, per slice, with the neighbors; neve :: …*Outgoing statement.* "**NCT/embellishment discrimination is chord-first, per slice, with neighbors — never a union recompute.**" — §6.2 *…
   Row 43.144 [ADOPTED — carried] hold a chord reading and judge each extra pitch by a membership test,  :: …ctus): hold a basic chord reading and judge each slice's "extra" pitches as chord-tone vs NCT using a per-note **chord-membership** test informed by metric position + the prev/next chord." — §6.2 *Layer …
   Row 43.150 [ADOPTED — carried] a passing-tone slice carries the same chord analysis and merges. :: …Outgoing statement.* "A passing-tone slice that layer 3 labels as "still chord X (with an NCT)" carries the *same chord analysis* as its neighbors, so grouping merges `[X][X+passing→X][X]` into one `X` r…
   Row 43.152 [ADOPTED — carried] the non-chord-tone decision lives in the analysis, not in the grouping :: …*Outgoing statement.* "(This is why the NCT decision must live in layer 3, not here.)" — §6.3 *Layer N — grouping* (locator: lines 393–394).…
   Row 43.161 [RELOCATED, ADOPTED — carried] several slices to one annotated event, all carrying the same analysis. :: …al slices map to one oracle event, and they should all carry the **same** analysis (or be NCT-flagged within the same chord)." — §6.5 *Cross-cutting — slices vs oracle events* (locator: lines 410–411). T…
   Row 44.50 [ADOPTED — carried, UNPLACED, ADOPTED — carried, UNPLACED, ADOPTED — carried, UNPLACED, ADOPTED — carried, ADOPTED — carried, ADOPTED — carried, UNPLACED] the key layer's wish list from the inventory. :: …horing); harmonic rhythm + boundary strength (cadence approach, tonicization boundaries); NCT-cleaned tone collections (emission input hygiene); progression grammaticality under candidate keys (tonic arb…
   Row 44.65 [ADOPTED — carried] the classification of non-chord tones needs a chord; the chord wants c :: …*Outgoing statement.* "NCT classification needs a chord hypothesis; chord identification wants NCT-cleaned tones." — §8, the circles, th…
   Row 44.66 [UNPLACED, UNPLACED] chords first, non-chord tones classified against them, an override for :: …irst, NCTs classified against them, with the forward-override for the rare case where the NCT reading overturns the chord." — §8, the circles, the fourth (locator: lines 187–190). Two claims: (i) chords …
   Row 44.76 [ADOPTED — carried, ADOPTED — carried, UNPLACED, UNPLACED, ADOPTED — carried] the design's evidence menu: cleaned collections and accidentals, ferma :: … opening's decisions gain a concrete evidence menu: the emission decision should consider NCT-cleaned collections and notated accidentals, not only spelling profiles; the transition decision gains fermat…
   Row 46.158 [RELOCATED] the advisory's design owns the construction, by two routes. :: …script-checked 46 consecutive-5th/8ve instances in the Bach chorales (categorized fermata/NCT/chordal) + Fitsioris-Conklin's 18 parallel-5th passages — with the remaining chorales as near-negatives; (ii)…
   Row 48.7 [HISTORICAL, ADOPTED — carried] the cleaned tone content to a pitch emission, weighted by meter. :: …*Outgoing statement.* "NCT-cleaned **tone collections / pitch content** → emission `P(pitches | tonic, mode, chord)`, metric-weighted;" …
   Row 49.8 [UNPLACED, UNPLACED] the ornament labels derived after the decode, the pedal point among th :: …*Outgoing statement.* "*Ornament labels* — the ratified post-decode non-chord-tone labels (OI-194), including the voice-independent pedal-point class (§10 ruling)." — the terms, above §1 (locator: li…
   Row 56.5 [HISTORICAL, HISTORICAL] embellishment chord-first: segmentation, then a non-chord-tone pass; n :: …*Outgoing statement.* "**Embellishment = chord-first** (segmentation + NCT post-process), never union re-derive / richer vocabulary." — §4, the meta-findings to institutionalize (locat…
   Row 62.27 [] L0/L1 Row 21.8: the non-chord-tone-cleaned, metric-weighted tone colle :: …*The outgoing statement it carries.* "NCT-cleaned **tone collections / pitch content** → emission `P(pitches | tonic, mode, chord)`, metric-weighted" —…
rows indexed: 4642
```

### B.2d — §8: the short-quotation and count check — its proof, then the final run

*Saved to scratch as `shortq_s8_proof.txt`.*

```
PROOF: altered quotation 'any sixth, ninth, eleventh, thirteenth, or altered tone above the basic quality' -> 'anyX sixth, ninth, eleventh, thirteenth, or altered tone above the basic quality'
entries: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] | in order 1..18: True
★ questions at the derivation: [2, 4, 5, 8, 16]
★ outside the quotations (own prose): 0 | ★ at the head of a quoted question: [2, 4, 5, 8, 16] | other ★ inside quotations: 0
pairs checked: 55 | row names checked: 55
FAILURES: 1
FAIL s8 1: quotation not found at Row 6.33's outgoing statement: anyX sixth, ninth, eleventh, thirteenth, or altered tone above the basic quality
```

*Saved to scratch as `shortq_s8.txt`.*

```
entries: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] | in order 1..18: True
★ questions at the derivation: [2, 4, 5, 8, 16]
★ outside the quotations (own prose): 0 | ★ at the head of a quoted question: [2, 4, 5, 8, 16] | other ★ inside quotations: 0
pairs checked: 55 | row names checked: 55
FAILURES: 0
```

### B.2e — §8: the quotation check against the derivation — its proof, then the final run

*Saved to scratch as `qcheck_s8_proof.txt`.*

```
altered one quotation: 'convergence of masses.**' -> 'convergence of weights.**'
entries checked: 18 | numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
FAILURES: 1
FAIL s8 entry 6: quotation not found: OQ-L2-6 (face (c), (h); L2-S22) — convergence of weights. When L2 enlarges its context, wh
```

*Saved to scratch as `qcheck_s8.txt`.*

```
entries checked: 18 | numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
FAILURES: 0
```

### B.2f — §8: the build check (built on the §7 blob feff1df7)

*Saved to scratch as `build_check_s8.txt`.*

```
§6.1 to §6.62 span identical (trailing newlines trimmed): True 3998446 3998446
--- changed passage 1: replace base lines 146-146 -> new lines 146-146
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 and 42, each whole in its own commit, and stopped by its own capacity judgment to leave room for the close. The ninth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md`, opened with position 43 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 44 and 45, each whole in its own commit, and stopped by its own capacity judgment, written before position 46 was opened, to leave room for its correction commit and its close. The tenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md`, opened with position 46 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 47 and 48, each whole in its own commit, and stopped by its own capacity judgment, written before position 49 was opened, to leave room for the close. The eleventh batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`, opened with position 49 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 50 whole in its own commit, and stopped by its own capacity judgment, written before position 51 was opened, to leave room for the close. The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 52 whole in its own commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close. The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there. The fourteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`, opened with position 62 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, and stopped at the section boundary after position 62 because §7's generated reconciliation to §13 did not hold, which that dispatch's Task 1(e) made a STOP (the difference located by row in `records/cc/reports/cc_report_l2_comparison_tabulation_fourteenth_2026_10_04.md` §2.7). The fifteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md`, opened with §7 as that dispatch ordered (**D-670**) and wrote it whole in its own commit. §7 is written; §8, §9 and §14 stay NOT YET WRITTEN, to be written once each, in the order §7, §8, §9, §14. **A member marked NOT YET TABULATED is UNTOUCHED** — not
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 and 42, each whole in its own commit, and stopped by its own capacity judgment to leave room for the close. The ninth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md`, opened with position 43 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 44 and 45, each whole in its own commit, and stopped by its own capacity judgment, written before position 46 was opened, to leave room for its correction commit and its close. The tenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md`, opened with position 46 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 47 and 48, each whole in its own commit, and stopped by its own capacity judgment, written before position 49 was opened, to leave room for the close. The eleventh batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`, opened with position 49 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 50 whole in its own commit, and stopped by its own capacity judgment, written before position 51 was opened, to leave room for the close. The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 52 whole in its own commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close. The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there. The fourteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`, opened with position 62 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, and stopped at the section boundary after position 62 because §7's generated reconciliation to §13 did not hold, which that dispatch's Task 1(e) made a STOP (the difference located by row in `records/cc/reports/cc_report_l2_comparison_tabulation_fourteenth_2026_10_04.md` §2.7). The fifteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md`, opened with §7 as that dispatch ordered (**D-670**) and wrote §7 and §8, each whole in its own commit. §7 and §8 are written; §9 and §14 stay NOT YET WRITTEN, to be written once each, in the order §7, §8, §9, §14. **A member marked NOT YET TABULATED is UNTOUCHED** — not
--- changed passage 2: replace base lines 74545-74545 -> new lines 74545-74545
  -   once-written sections — §7, §8, §9 and §14 — stand as §0 says: §7 is written; §8, §9 and §14 are NOT YET WRITTEN.
  +   once-written sections — §7, §8, §9 and §14 — stand as §0 says: §7 and §8 are written; §9 and §14 are NOT YET WRITTEN.
changed passages outside the section: 2
section lines: base 6 -> new 171
base section still NOT YET WRITTEN: True | new section NOT YET WRITTEN: False
ends with newline: True no CR: True
```

### B.2g — §8: the word scans — the first run, the run after rewording, then the changed §0 and §16 text

*Saved to scratch as `wordscan_s8.txt`.*

```
BRITISH centre | e tabulated outgoing text speaks to it at Row 7.42, a tonal centre  , at Row 7.48,  , at Row 48.29,  , and at Row 49.31,  .  *
RESERVED notes |  text speaks to the vocabulary at Row 6.33, where the added notes —   — are  , and at Row 6.85,  , and to the admission rule 
RESERVED flat | n rule at Row 1.8,  ; a search for a double sharp, a double flat or a double accidental, and for the chain or the depth of a
RESERVED scores |    (Row 10.52); the six rows a search for very large, large scores and orchestral finds say nothing about the cost of the deco
RESERVED note | nteen rows a search for chordal voice, successor, following note and next note finds, none names a link from a pitch event t
RESERVED note | earch for chordal voice, successor, following note and next note finds, none names a link from a pitch event to its successo
RESERVED resolution | ctor's features at Row 10.34,   among them, and the tritone resolution at Row 5.93, where  ; the three rows a search for cue windo
RESERVED key | says   (Row 2.50) and   (Row 2.51), and names an enharmonic key-span identity rule for the case   (Row 5.346).  **OQ-L2-18*
hits: 8
```

*Saved to scratch as `wordscan_s8b.txt`.*

```
RESERVED notes |  text speaks to the vocabulary at Row 6.33, where the added notes —   — are  , and at Row 6.85,  , and to the admission rule 
RESERVED flat | n rule at Row 1.8,  ; a search for a double sharp, a double flat or a double accidental, and for the chain or the depth of a
RESERVED scores |    (Row 10.52); the six rows a search for very large, large scores and orchestral finds say nothing about the cost of the deco
RESERVED note | nteen rows a search for chordal voice, successor, following note and next note finds, none names a link from a pitch event t
RESERVED note | earch for chordal voice, successor, following note and next note finds, none names a link from a pitch event to its successo
RESERVED resolution | ctor's features at Row 10.34,   among them, and the tritone resolution at Row 5.93, where  ; the three rows a search for cue windo
RESERVED key | says   (Row 2.50) and   (Row 2.51), and names an enharmonic key-span identity rule for the case   (Row 5.346).  **OQ-L2-18*
hits: 7
```

*Saved to scratch as `wordscan_added_s8.txt`.*

```
added lines written: 2
hits: 0
```

### B.2h — §8: the consistency check over the built file

*Saved to scratch as `consistency_s8.txt`.*

```
rows parsed: 4642; travelling refs checked: 2464; as-at refs checked: 861; flags: 0
```

### B.3a — §9: the search

*Saved to scratch as `s9search_out.txt`.*

```
==================== POINT-1
-- term /one decode|jointly|entangled|decided together|together in one/: 11 rows
   Row 5.330 [HISTORICAL] the interaction with section grouping is to be specified jointly. :: …he interaction with section grouping** for the class-(b) override duty (§10) — to specify jointly." — §15, item 6 (locator: line 849).…
   Row 7.129 [QUARANTINED] the change cost cannot be cleanly optimized until the function layer a :: …Layer 5 (function) can arbitrate that boundary." — §11, *The change-cost tuning is partly entangled with the later layer* (locator: lines 390–393).…
   Row 9.119 [HISTORICAL] the screen's deliverables. :: …arnings (parameters whose perturbation flips §6-block rule firings — these must be fitted jointly with the dissolution track, §4.4), and the frozen-row verification findings." — §4.3, item 1b (locator: lines…
   Row 9.121 [HISTORICAL, HISTORICAL, HISTORICAL, HISTORICAL, QUARANTINED] P1 ratified: the split, the optimizer, the staging, no augmentation, t :: … the coupled continuous cluster (G1 tone factors + G2/G3 bass/root/inversion + G6) fitted JOINTLY with the §6-block dissolution track → the G7 gate margins by pinned-fixture replay (Δ=0 at the objective's re…
   Row 21.27 [HISTORICAL] the superseded proposal: every layer emits ranked candidates and a glo :: …window, segmentation hypotheses), and a global decode (Viterbi / beam search) selects the jointly best path." — §2.14, the 2026-06-10 reconciliation (locator: lines 1028–1032).…
   Row 21.31 [ADOPTED — carried, QUARANTINED] the finding does not bear on the joint decode, one decode over a joint :: …locator: lines 1045–1049). Two claims: (i) the finding does not bear on the joint decode, one decode over the joint state of tonality, mode and chord; (ii) the joint decode's gain was measured at its adoption.…
   Row 21.48 [ADOPTED — carried, RELOCATED, QUARANTINED, RELOCATED, RELOCATED, HISTORICAL] the current span names and what bounds each. :: … (the span a cadence closes *and* confirms — where a punctuation-span and a key-span are *jointly* articulated, which is why one cadence detector feeds both grouping and key) · the **progression-schema-span*…
   Row 39.185 [ADOPTED — carried] coupled quantities decided together, not one committed early.** *WITHH :: …same principle the production estimator carries on its own terms — coupled quantities are decided together rather than one being committed early." — §5 *Joint (bass, root, template) scoring* (locator: lines 854–856).…
   Row 43.93 [RELOCATED] the cadential scope: one detector feeds the phrase and the tonality. :: …e** — the span a cadence **closes and confirms**: where a phrase span and a key-span are *jointly* articulated (a cadence marks both a phrase ending and a key confirmation — the reason one detector feeds bot…
   Row 48.3 [ADOPTED — carried] every enumerated clue a term in the one decode. :: … `cowork_evidence_inventory.md` enters as an emission, transition, or prior *term* in the one decode — the joint model is the antidote to the information loss a pipeline causes (#12)." — §1 *What A is* (locator…
   Row 48.44 [ADOPTED — carried] the chord and the status of each tone decided together in the one deco :: …*Outgoing statement.* "Chord identity and tone status are decided together in the one decode (#12 — no ornament verdict is ever committed early)." — §5a, the non-chord tones (locator: …
==================== POINT-2
-- term /exact decode|viterbi|beam|search/: 87 rows
   Row 1.9 [ADOPTED — carried] exact semi-Markov Viterbi over the joint state is the ratified search. :: …*Outgoing statement.* "Exact semi-Markov Viterbi over the joint state is the ratified search." — rule (c) (locator: line 304).…
   Row 1.10 [HISTORICAL] the reserve prune, declared for use only if exact decode proved intrac :: … fitted-mass neighborhood on the circle of fifths — to be used only if measurement showed exact decode intractable, and only with its own established-loss measurement, never as a silent heuristic (`cowork_joint_e…
   Row 1.11 [QUARANTINED] the prune was never adopted: its measured cost is worse than exact dec :: … statement.* "It was never adopted: measured at the fitted weights its cost is worse than exact decode." — rule (c) (locator: lines 308–309).…
   Row 1.13 [HISTORICAL] tried and closed on the search. :: …*Outgoing statement.* "*Tried and closed on the search — do not retry; the register carries each with its measurement: D-288 (beam widening, shelved), D-328 (a wide…
   Row 1.14 [HISTORICAL] do not retry widening the search.** *WITHHELD — D-288. :: …*Outgoing statement.* "**Do not retry widening the search to consider more candidate readings in parallel.**" — the block *"★ WHAT D-288 IS"*, which marks itself LEGAC…
   Row 1.16 [HISTORICAL] the consequence that closed the build. :: … the build rather than merely discouraging it: for every OTHER motivated use, a width-one search substitutes for the wider one, so nothing else justified building it." — the same block (locator: lines 324–3…
   Row 1.56 [ADOPTED — proposed] the search consumes scores and constraints and is indifferent to how t :: …*Outgoing statement.* "The machinery that searches for the best reading consumes scores and constraints and is indifferent to how they were produced, so a lea…
   Row 3.35 [ADOPTED — carried] the chord-path search emits the whole path with every stretch's altern :: …*Outgoing statement.* "**The chord-path search emits the WHOLE PATH with every stretch's alternatives and its margins — not the committed reading alone. ⚠ L…
   Row 3.36 [ADOPTED — carried] per node, the chosen reading with the readings it beat and by how much :: …*Outgoing statement.* "The search hands forward, per node, the chosen reading together with the readings it beat and by how much." — (locator: …
   Row 3.37 [HISTORICAL] the mechanism the rule governs is the dormant staging.** *WITHHELD — D :: …ng statement.* "**The mechanism it governs is the dormant staging described above** — the search is not wired, and what becomes of this decoder is open at the retirement map." — (locator: lines 2059–2060).…
   Row 4.14 [ADOPTED — carried, QUARANTINED] published "function" means the Roman numeral's components; the legacy  :: …*Outgoing statement.* "When published research says a system predicts "function" it means the Roman numeral's parts (the degree, the quality, the applied re…
   Row 5.228 [QUARANTINED, UNPLACED] what the mechanism is not: a backward re-derivation or a full joint se :: …g statement.* "**What this is NOT:** a backward re-derivation or a full joint cross-layer search — that was measured inert (the gain is soft-evidence quality, carried forward), so the architecture spends it…
   Row 5.253 [UNPLACED, ADOPTED — carried, QUARANTINED] rejected: bespoke one-off overrides, a hard confidence gate, and a bac :: …e tunable per-channel thresholds); (c) a backward re-derivation or full joint cross-layer search (measured inert — the gain is soft-evidence quality carried forward, not cycling)." — §9, D7 (locator: lines …
   Row 7.17 [QUARANTINED] the best-sequence decode: one pass of dynamic programming over per-sli :: …c-programming decode over per-slice scores plus change costs (§5 step 3; the literature's Viterbi decode, §14)." — §0, the terms table, row *Best-sequence (Viterbi) algorithm* (locator: line 60).…
   Row 7.151 [ADOPTED — carried] glossary: the best-sequence algorithm. :: …hest-scoring sequence given per-slice scores and change costs; this is the literature's **Viterbi** dynamic-programming decode (Section 14), named plainly in the body." — §12 (locator: lines 444–446).…
   Row 7.161 [UNPLACED] this is the per-layer decode, not the rejected global cross-layer join :: …r** key-path decode — internal to Layer 3 — not the rejected **global cross-layer** joint Viterbi/beam decode; cf. ARCHITECTURE.md §2.14.)*" — §14, *Built on — the deciding method* (locator: lines 473–474).…
   Row 8.67 [ADOPTED — carried] select by joint consistency across key, root, inversion and bass, not  :: …*Outgoing statement.* "The decisive published lesson `[research]` §2: **select by joint consistency across key / root / inversion / bass**, not by maximizing any single scor…
   Row 8.81 [UNPLACED] the load-bearing channels are exactly those the override lacked. :: …els are bass / spelling / key-consistency / cadence** (§3.2) — exactly the channels the research says carry root correctness and F-B lacked." — §3.3 (locator: lines 224–225).…
   Row 8.97 [UNPLACED] the joint step re-ranks the key under chord evidence, and the reverse. :: … machinery that **re-ranks the key under chord evidence** (and vice versa) — the "carry a beam of (key, chord) hypotheses and let downstream chord evidence re-rank the key" of `[research]` §3." — §4.1 (lo…
   Row 8.100 [QUARANTINED, QUARANTINED] the joint step, when built, a bounded instance of the forward discipli :: …me forward discipline (a declared exception with its own closure), not a free cross-layer search — which the spec measured inert (§8 "What this is NOT")." — §4.1 (locator: lines 269–271). Two claims: (i) th…
   Row 8.113 [UNPLACED] the carry contract is designed to feed the joint step; its place is re :: …*Outgoing statement.* "the carry contract (§2) is designed to **feed** it (the beam of hypotheses `[research]` §3), and the §4.1 boundary reserves its place." — §4.3, item *O-18 / C3* (locator:…
   Row 9.121 [HISTORICAL, HISTORICAL, HISTORICAL, HISTORICAL, QUARANTINED] P1 ratified: the split, the optimizer, the staging, no augmentation, t :: …lit RATIFIED** (`tools/stage5_split_registry.json`); (2) **optimizer = coordinate/pattern search** (D-3's default, confirmed budget-feasible at ~45 s/eval, ~35 live rows post-dead-pruning); (3) **staging ad…
   Row 9.209 [HISTORICAL] D-3: the default optimizer, coordinate or pattern search. :: …*Outgoing statement.* "*Default:* **coordinate / pattern search** over family-scoped subspaces (derivative-free, constraint-friendly, trivially deterministic, easy to ledger…
   Row 9.322 [QUARANTINED, UNPLACED] O-26(a): the joint step completes the built key-axis coupling and adds :: …tion (#6) of the built `decideJointKey`** (J-key-i/ii/iii) — its key-axis half (lattice + Viterbi + **key-transition prior** `transitionPenalty` + measured **coupled minority ~13.5%** + config-B chord→key `c…
   Row 9.325 [HISTORICAL] O-26(d): the joint candidate score's composition, all terms precision- :: … + −keyTransitionCost` — all terms precision-phase (`transitionPenalty`, `couplingBonus`, beam width, trigger bar 1.0)." — §15, O-26 (locator: lines 1189–1191).…
==================== POINT-3
-- term /unfold|notated order|repeat/: 20 rows
   Row 5.39 [RELOCATED] a section end is a phrase boundary that coincides with a structural bo :: …hrase boundary that **also coincides with a structural score boundary** — a double bar, a repeat mark, or the end of the piece — used only as the section-end salience cue in §5.2.)" — §3 (locator: lines 95–…
   Row 7.64 [QUARANTINED] the built reach-back loop: its trigger, its action and its stop. :: …sk Architectural Layer 1 to `extend(Earlier)` → re-slice (Layer 2) → re-decode (Layer 3), repeated until the leading-edge **settled** key stops changing across iterations (settled = not "uncertain" and at-o…
   Row 10.47 [QUARANTINED, ADOPTED — carried] exactly equal candidate scores between decodes are real; unbroken, the :: … real (proven at 8 corpus pieces — equal-score segmentations differing by one boundary on repeated-chord runs) and, unbroken, they make the committed output depend on the platform's floating-point library —…
   Row 23.179 [QUARANTINED] the mode-name helpers use separate arrays per mode family. :: …TonicOffset()` use separate static arrays per mode family and share comment patterns that repeat the same "mode family / parent key signature" logic." — §4.1i *Technical Debt and Refactor Backlog (reviewed …
   Row 23.255 [HISTORICAL] stop when the same winner survives repeated expansion. :: …*Outgoing statement.* "the same winner survives repeated expansion" — *Phase 1b — Minimal Monophonic Fallback Without Chord Symbols* (locator: line 3666).…
   Row 24.52 [QUARANTINED] the notation path merges repeated slices of the same chord into one re :: …*Outgoing statement.* "The notation bridge now uses the same collapse rule, so repeated slices that analyze to the same chord merge into one region even in preserve-all mode." — §5.8 *Known Analy…
   Row 24.81 [HISTORICAL] repeated identical labels on dense piano writing. :: …*Outgoing statement.* "Dvořák Silhouettes and Chopin Mazurkas show repeated identical chord labels (e.g. `Bb×8`, `Fsus×20`) from Jaccard boundary firing on dense arpeggiated texture."…
   Row 40.50 [RELOCATED] a double, final or repeat barline. :: …*Outgoing statement.* "a **double, final, or repeat barline** (a structural division — treated, for this primitive, as a phrase boundary);" — §4.2 *The determini…
   Row 40.104 [RELOCATED] oracle tests of the cues and the picking on constructed cases. :: …ak; a long note among short ones yields an inter-onset peak; a fermata and a double/final/repeat barline yield marker spikes; a single mid-phrase leap does **not** clear the threshold alone; a region contai…
   Row 40.139 [RELOCATED] glossary: the structural barline. :: …*Outgoing statement.* "**Structural barline** — a double, final, or repeat barline (a notational division)." — §9 *Glossary* (locator: line 353).…
   Row 44.7 [RELOCATED] time signatures, barlines including double and section barlines, repea :: …*Outgoing statement.* "Time signatures; barlines including double/section barlines; repeats." — §1 *The score itself* (locator: line 23).…
   Row 45.13 [UNPLACED, ADOPTED — carried] the test applied directly to the quantity the extension was asked for; :: …nfers over the enlarged span, compares that quantity step against step, and stops when it repeats." — §3 *The bounded-context contract*, item 6 (locator: lines 66–67). Two claims: (i) the convergence test i…
   Row 45.14 [QUARANTINED] the built reach-back tracks the leading-edge settled tonality and stop :: …actly this — it tracks the **leading-edge settled key across iterations and stops when it repeats**, which is the criterion itself and not a stand-in for it (the convergence note above the reach-back loop i…
   Row 45.50 [QUARANTINED] reach-back an extension request: earlier, stopping when the leading-ed :: …k **is** an extension request: direction = earlier, stop = *"the leading-edge settled key repeats across iterations"*, bound = a maximum reach." — §5 *Per-layer roles*, Architectural Layer 3 (locator: lines…
   Row 45.92 [QUARANTINED, ADOPTED — carried] what it changes in the tonality layer's specification. :: … framed as an extension request (direction = earlier, stop = the leading-edge settled key repeats across iterations, hard bound); leading-edge window behaviour (request-or-truncate)." — §10 *Spec propagatio…
   Row 46.30 [RELOCATED] the interval profile: a per-voice histogram of intervals and the repea :: …nterval statistics of a span: the |interval|-in-semitones histogram (bins 0–11, ≥12) plus repeat/step/leap rates (repeat = 0, step = 1–2, leap ≥ 3 semitones)." — §0, *This design's operational terms [VL]* (…
   Row 46.109 [RELOCATED] the interval profile type. :: …*Outgoing statement.* "**IntervalProfile** — histogram bins + repeat/step/leap rates + note count, per voice or aggregated." — §7 *Data design* (locator: line 501).…
   Row 53.17 [RELOCATED] a harmonic sequence: the same progression repeated at successive trans :: …*Outgoing statement.* "**Harmonic sequence** — the same progression repeated at successive transpositions (Monte, Fonte, a descending-fifths sequence)." — §0, the terms, row *Harmonic …
   Row 53.50 [RELOCATED, UNPLACED] a sequence at least two transposed statements of the same entry; its e :: …sequence requires ≥2 transposed statements of the SAME recognised entry** — that is what "repeated at successive transpositions" (§0) means; a run's `repetitions` counts the matched windows, and the evidenc…
   Row 62.44 [] L0/L1 Row 18.31: that reach-back IS an enlargement request, with its d :: …k **is** an extension request: direction = earlier, stop = *'the leading-edge settled key repeats across iterations'*, bound = a maximum reach." — `cowork_bounded_context_design.md`, §5, third bullet (the L…
==================== POINT-4
-- term /non-chord-tone.*(?:ground truth|annotat)|(?:ground truth|annotat).*non-chord-tone|chord-tone.*ground truth/: 6 rows
   Row 3.11 [HISTORICAL] non-chord-tone detection waits for the annotated material it needs. :: …*Outgoing statement.* "Non-chord-tone detection waits for the annotated material it needs." — (locator: lines 1964–1965).…
   Row 6.26 [QUARANTINED] the type of a non-chord tone is not classified here. :: …, neighbour, suspension, anticipation): naming the chord needs only the chord-tone-versus-non-chord-tone call; the type label is a separable later annotation." — §1 (locator: lines 88–89).…
   Row 6.42 [QUARANTINED] minimality: settle only what the notes and the key decide, defer every :: …ble sub-problem**: the unfixable symmetric-sonority root (→ the later function step), the non-chord-tone *type* (→ a later annotation), and voice-leading across the progression (→ a relational later concern)." — §2, *Minimality (the governi…
   Row 6.121 [QUARANTINED, ADOPTED — carried, QUARANTINED, QUARANTINED, QUARANTINED] what each slice's result holds. :: …— the held-out chord-root + bass agreement of §10) scores); the **chord-tone set**; the **non-chord-tone set** (chord-tone-versus-not only; the type is a later annotation); the **competing readings**; a **confidence**; and the **"uncertain" mark with its open-question label** (root / quality / a named note's membership — so a downstream selector knows *what* to resolve, not merely that something is open)." — §7 (locator: lines 351–356). Five claims: (i) the chord symbol; (ii) the chord-tone set and the non-chord-tone set; (iii) the non-chord-tone type left to a later annotation; (iv) the competing readings and a confidence; (v) the uncertain mark with its open-question label.…
   Row 6.146 [UNPLACED] chosen: only the chord-tone call here; the type a later annotation. :: …"Chosen: naming the chord needs only chord-tone-versus-not; the type is a separable later annotation." — §9, *Only the chord-tone/non-chord-tone call here; the non-chord-tone TYPE is deferred* (locator: lines 436–437).…
   Row 8.138 [UNPLACED] what the reader emits: the carried alternative excluding the bass, mar :: …*Outgoing statement.* "**What it emits:** on the pedal structural condition (bass is a non-chord-tone of the committed reading) **and** a carried distinct-root alternative excluding the bass clearing the pedal-confidence bar, the reader **marks that alternative as the pedal reading** (`isPedalPoint`, `pedalBassPc`, the upper-voice chord as the identity) and carries it as the slice's pedal-annotated candidate" — §6.3 (locator: lines 415–418).…
==================== POINT-5
-- term /grad(?:e|ed|ing).*(?:boundar|label)|retardation label|restated chord/: 17 rows
   Row 4.16 [RELOCATED] cadences are looked for at phrase ends, read from the graded phrase-bo :: …nces are looked for at phrase ends, which this layer reads as a published L1.5 fact — the graded phrase-boundary profile." — (locator: lines 2144–2146).…
   Row 5.273 [RELOCATED] the phrase-boundary primitive's non-chorale markers are unvalidated. :: …statement.* "**The phrase-boundary primitive's non-chorale markers are unvalidated.** The graded model carries rest- and structural-boundary cues for general (non-chorale) textures, but the corpus is entirely fermata-marked chorales, so those marker…
   Row 5.306 [QUARANTINED, QUARANTINED] two inputs gate the build: the metric weight, resolved as the beat str :: …oundary + phrase segmentation** — **✅ BUILT (dormant) + Cowork-verified 2026-06-26**: the graded per-voice model lives in `engravingbridge/phraseboundaryview.{h,cpp}` (commits `0d10b37a87` de-dup + `5c5d992356` graded model), reachable only behind the default-off joint-key gate → **byte-identical on production** (verified at source), with the full marker set." — §15, item 0 (locator: lines 793–799). Two claims: (i) the slice metric weight is the beat strength at the slice's start tick, owned by a named module; (ii) the phrase-boundary model is built dormant and reachable only behind a default-off gate.…
   Row 5.348 [RELOCATED] in punctuation-poor textures the phrase gate starves the detector. :: …ctuation (the review's F-11 — "unendliche Melodie": no fermatas, elided phrase ends, flat graded boundary-strength profile) the gate **starves** the detector and everything downstream of its votes." — §15, item 11 …
   Row 40.5 [RELOCATED] the boundary-strength profile: graded per onset, published as a margin :: …*Outgoing statement.* "| **Boundary-strength profile** | The graded per-onset measure of §4 (per-voice, and aggregated to the texture). Its published form is a **Class-M boundary confidence** under `cowork_confidence_contract.md`. |" — §0 *Terms*, the terms table (locator: line 42).…
   Row 40.8 [RELOCATED] from the notated surface alone, a graded profile, the picked ticks and :: …*Outgoing statement.* "This primitive computes, from the notated surface alone, a **graded boundary-strength profile** over the score — a per-onset measure of how strongly the surface evidence marks a phrase end — and from it the **picked boundary ticks** and the derived per-region flag **"this region ends a phrase."**" — §1 *Purpose* (locator: lines 50–…
   Row 40.9 [RELOCATED] a graded strength, so a consumer reads a boundary's confidence. :: …*Outgoing statement.* "It emits a *graded strength*, not only a yes/no, so a consumer can read the confidence of a boundary, not just its presence." — §1 *Purpose* (locator: lines 55–56).…
   Row 40.97 [RELOCATED] a graded model, not a binary union. :: …*Outgoing statement.* "**D4 — A graded boundary-strength model, not a binary union (user-ratified 2026-06-26).**" — §6 *Architecture decisions* (locator: li…
   Row 40.144 [HISTORICAL] this primitive unifies the scan and replaces the fermata-only definiti :: …ated scan into one owned Layer-1.5 view and replaces the fermata-only definition with the graded surface-cue + marker model above; the concrete file map and the cue formulas are in the build instruction and the methods catalog (`cowork_phrase_boundary_methods.md`)." — §10 *Background* (locator: lines 366–368).…
   Row 40.157 [RELOCATED] a per-part marker should reach the texture only through voice-coincide :: …ach a **texture** boundary only through the same **voice-coincidence aggregation** as the graded cues (§4.3) — a lone breath then yields a **per-voice** boundary (already exposed by this primitive, and the raw material for the future voice-leading / melody-line axis, `c…
   Row 41.54 [RELOCATED] it consumes the phrase-boundary primitive's ticks and strengths. :: …**The phrase-boundary primitive** (`phraseBoundaryView` — `phraseBoundaryTicks()` and the graded `PhraseBoundaryProfile`): the boundary ticks and their strengths (fermata / breath / rest / barline / key-signature / tempo cues — strengths scaled to the strongest cue, local maxima selected as boundaries; the primitive's max-normalisation and peak-picking, `cowork_phrase_boundary_design.md` §4)." — §3 *Inputs and outputs* (locator: lines 158–161).…
   Row 41.92 [RELOCATED, RELOCATED] any confidence the grouping publishes is a margin-class boundary confi :: … not the **diagnostic sigmoid** (the Layer-3 emission-scale confidence squash used by the grading diagnostics, named in the Layer-3 spec banner as the C1 fidelity fix).)*" — §5.2 *Key-area grouping* (locator: lines 254–261). Two claims: (i) a confidence the grouping publishes is a margin-class boundary confidence in [0,1], its combiner and inputs named; (ii) its input is each unit's declared boundary tonality confidence, not the diagnostic squash.…
   Row 41.139 [RELOCATED] the one chorale without a fermata handled in the metric. :: …case for the fermata punctuation-span oracle (handle in the metric, e.g. fall back to its graded boundary, or exclude from the fermata-recall denominator — a §10 metric detail, not a layer rule)." — §11 *Risks & te…
   Row 44.33 [ADOPTED — carried, UNPLACED, HISTORICAL] the strength of a boundary, harmonic rhythm as a cadence-approach sign :: …ED from this layer: **boundary STRENGTH** (how decisive the change-point evidence was — a graded boundary confidence instead of a binary cut; useful for tonicization-boundary arbitration and for the segmentation-edge artifact class); **harmonic rhythm** (the pattern of slice durations — accelerating harmonic rhythm approaching a phrase end is a classic cadence-approach signal, textbook theory, computable purely from slice durations); anacrusis/pickup detection." — §4 *Layer 2 — segmentation* (locator: lines 87–92). Three claims: (i) a graded confidence of each boundary instead of a binary cut, useful for arbitrating the boundaries of a tonicization; (ii) harmonic rhythm, computed from the slice durations, as a signal that a cadence app…
   Row 47.23 [ADOPTED — carried, HISTORICAL, HISTORICAL] the contract the full posterior; the slice delivered first; the comple :: …nd the marginal completion is a NAMED, ROWED step of this increment — not an indefinite upgrade.**" — §4 *Decision B*, the recommendation (locator: lines 282–284). Three claims: (i) the contract of the uncertainty surface is the full posterior; (ii) the local slice, established and a strict subset of that surface, is the first step delivered; (iii) the completion to the marginals is a named step with its own row, not an indefinite upgrade. *Boundary mark:* the sentence opens on D-425's home as cited, the one line 282, and runs past it; the decisions regist…
   Row 52.10 [RELOCATED, HISTORICAL] the phrase-boundary strength: max-normalized, comparable within one pi :: …*Outgoing statement.* "| L1.5 phrase-boundary | boundary-at-tick | graded boundary strength, max-normalised per profile → [0,1] | M (salience-margin variant) | Relative salience within the profile — **comparable within one score's profile only**; consumers (L5 phrase gate, L6) must not compare across scores. **Stage-5 Task-B spike-vs-surface split MEASURED (Phase 3, 2026-07-06): the SURFACE population alone (98.4 % of ticks), normalized within itself, has usable monotone spread (0.13→0.46 across deciles, mono-viol 2) — a per-population map is fittable in principle at a later increment; the SPIKE population (1.6 %) is a flat ~0.40 cluster. No map fitted now (weak absolute signal, tops at 0.46). The C1 "insufficient spread" reading is refined, not overturned: the spread exists in the surface cues once un-compressed from the spike-dominated per-profile max.** |" — §3, the per-layer inventory, row *L1.5 phrase-boundary* (locator: line 55). Two claims: (i) the phrase-boundary strength is a margin-class confidence, max-normalized per profile and comparable within one piece's profile …
   Row 52.31 [RELOCATED] the deliverable: reliability curves and maps upgrading each confidence :: …*Outgoing statement.* "Deliverable: reliability curves + fitted maps that upgrade each boundary confidence from Class M to Class P." — §6 *Calibration obligations (Stage 5)* (locator: lines 117–118).…
rows indexed: 4642
```

### B.3d — §9: the short-quotation and count check — its proof, then the final run

*Saved to scratch as `shortq_s9_proof.txt`.*

```
PROOF: altered quotation 'Chord identity and tone status are decided together in the one decode' -> 'ChordX identity and tone status are decided together in the one decode'
entries: [1, 2, 3, 4, 5] | in order 1..5: True
pairs checked: 9 | row names checked: 12
FAILURES: 1
FAIL s9 1: quotation not found at Row 48.44's outgoing statement: ChordX identity and tone status are decided together in the one decode
```

*Saved to scratch as `shortq_s9.txt`.*

```
entries: [1, 2, 3, 4, 5] | in order 1..5: True
pairs checked: 9 | row names checked: 12
FAILURES: 0
```

### B.3e — §9: the quotation check against the derivation — its proof, then the final run

*Saved to scratch as `qcheck_s9_proof.txt`.*

```
altered one quotation: '**Inference is missing as a face.**' -> '**Inference is absent as a face.**'
entries checked: 5 | numbers: [1, 2, 3, 4, 5]
FAILURES: 1
FAIL s9 entry 2: quotation not found: Inference is absent as a face. The charter's no-discarding rule makes the search's exactne
```

*Saved to scratch as `qcheck_s9.txt`.*

```
entries checked: 5 | numbers: [1, 2, 3, 4, 5]
FAILURES: 0
```

### B.3f — §9: the build check (built on the §8 blob cd089cb4; the kept run is the second, after the verb correction)

*Saved to scratch as `build_check_s9.txt`.*

```
§6.1 to §6.62 span identical (trailing newlines trimmed): True 3998446 3998446
--- changed passage 1: replace base lines 146-146 -> new lines 146-146
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 and 42, each whole in its own commit, and stopped by its own capacity judgment to leave room for the close. The ninth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md`, opened with position 43 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 44 and 45, each whole in its own commit, and stopped by its own capacity judgment, written before position 46 was opened, to leave room for its correction commit and its close. The tenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md`, opened with position 46 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 47 and 48, each whole in its own commit, and stopped by its own capacity judgment, written before position 49 was opened, to leave room for the close. The eleventh batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`, opened with position 49 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 50 whole in its own commit, and stopped by its own capacity judgment, written before position 51 was opened, to leave room for the close. The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 52 whole in its own commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close. The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there. The fourteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`, opened with position 62 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, and stopped at the section boundary after position 62 because §7's generated reconciliation to §13 did not hold, which that dispatch's Task 1(e) made a STOP (the difference located by row in `records/cc/reports/cc_report_l2_comparison_tabulation_fourteenth_2026_10_04.md` §2.7). The fifteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md`, opened with §7 as that dispatch ordered (**D-670**) and wrote §7 and §8, each whole in its own commit. §7 and §8 are written; §9 and §14 stay NOT YET WRITTEN, to be written once each, in the order §7, §8, §9, §14. **A member marked NOT YET TABULATED is UNTOUCHED** — not
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 and 42, each whole in its own commit, and stopped by its own capacity judgment to leave room for the close. The ninth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md`, opened with position 43 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 44 and 45, each whole in its own commit, and stopped by its own capacity judgment, written before position 46 was opened, to leave room for its correction commit and its close. The tenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md`, opened with position 46 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 47 and 48, each whole in its own commit, and stopped by its own capacity judgment, written before position 49 was opened, to leave room for the close. The eleventh batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`, opened with position 49 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 50 whole in its own commit, and stopped by its own capacity judgment, written before position 51 was opened, to leave room for the close. The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 52 whole in its own commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close. The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there. The fourteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`, opened with position 62 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, and stopped at the section boundary after position 62 because §7's generated reconciliation to §13 did not hold, which that dispatch's Task 1(e) made a STOP (the difference located by row in `records/cc/reports/cc_report_l2_comparison_tabulation_fourteenth_2026_10_04.md` §2.7). The fifteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md`, opened with §7 as that dispatch ordered (**D-670**) and wrote §7, §8 and §9, each whole in its own commit. §7, §8 and §9 are written; §14 stays NOT YET WRITTEN, to be written once each, in the order §7, §8, §9, §14. **A member marked NOT YET TABULATED is UNTOUCHED** — not
--- changed passage 2: replace base lines 74711-74711 -> new lines 74711-74711
  -   once-written sections — §7, §8, §9 and §14 — stand as §0 says: §7 and §8 are written; §9 and §14 are NOT YET WRITTEN.
  +   once-written sections — §7, §8, §9 and §14 — stand as §0 says: §7, §8 and §9 are written; §14 is NOT YET WRITTEN.
changed passages outside the section: 2
section lines: base 5 -> new 47
base section still NOT YET WRITTEN: True | new section NOT YET WRITTEN: False
ends with newline: True no CR: True
```

### B.3g — §9: the word scans — the section's own prose, then the changed §0 and §16 text

*Saved to scratch as `wordscan_s9.txt`.*

```
hits: 0
```

*Saved to scratch as `wordscan_added_s9.txt`.*

```
added lines written: 2
hits: 0
```

### B.3h — §9: the consistency check over the built file

*Saved to scratch as `consistency_s9.txt`.*

```
rows parsed: 4642; travelling refs checked: 2464; as-at refs checked: 861; flags: 0
```

### B.4a — §14: the generator's output — the SEEN-row search over every foot, the relay's length, the wider-check sentence

*Saved to scratch as `gen_s14_out.txt`.*

```
foot lines with 'SEEN rows:': 62 | naming rows: 3 | reading none: 59
    - **SEEN rows: 15.19 (D-279) — §6.3 entry 4.** The check was made at the homes, not at the identities the artifact
    - **SEEN rows: 17.5, claim (i) (D-002); 17.14 (D-095) — both §6.3 entry 4.** The check was made at the homes as
    - **SEEN rows: 45.7, 45.8, 45.9, 45.10, 45.11, 45.12, 45.13, 45.14 and 45.15**, inside D-261's home (lines 57–71), each
relay lines: 203
wider-check sentence now: **Stated here because it bound every row:** the wider check — whether an outgoing statement is the home of any design-intent entry the pack rendered in member 05 within the lines the deriving session read, other than the eight §5 names — is NOT made by this comparison.
```

### B.4b — §14: the count check

*Saved to scratch as `s14check_out.txt`.*

```
§6.1 heading inside the relay: 1
§6.2 heading inside the relay: 1
§6.3 heading inside the relay: 1
§6.4 heading inside the relay: 1
§6.5 heading inside the relay: 1
§6.6 heading inside the relay: 1
own prose, 'independent': 0
own prose, 'contaminated': 0
own prose, 'clean': 0
own prose, 'compromised': 0
own prose, 'established': 0
wider-check sentence with the new opening: True
former opening absent: True
SEEN sentence names 15.19, 17.5 (claim (i)), 17.14 and 45.7 to 45.15: True
FAILURES: 0
```

### B.4c — §14: the relay checked against the derivation — its proof (one word altered), then the final run

*Saved to scratch as `qcheck_s14_proof.txt`.*

```
altered one quotation: '> - **Message one** carried the brief alone.' -> '> - **Message one** carried the brief only.'
relay lines: 203 | source lines: 203
byte-for-byte equal to the derivation's §6.1 to §6.6: False
equal under the normalization: False
FAILURES: 1
FAIL relay differs from the derivation's §6.1 to §6.6
```

*Saved to scratch as `qcheck_s14.txt`.*

```
relay lines: 203 | source lines: 203
byte-for-byte equal to the derivation's §6.1 to §6.6: True
equal under the normalization: True
FAILURES: 0
```

### B.4d — §14: the word scans — the section's own prose (the relay removed), then the changed §0 and §16 text

*Saved to scratch as `wordscan_s14.txt`.*

```
hits: 0
```

*Saved to scratch as `wordscan_added_s14.txt`.*

```
added lines written: 2
hits: 0
```

### B.4e — §14: the build check (built on the §9 blob 3cd269c6)

*Saved to scratch as `build_check_s14.txt`.*

```
§6.1 to §6.62 span identical (trailing newlines trimmed): True 3998446 3998446
--- changed passage 1: replace base lines 146-146 -> new lines 146-146
  - `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 and 42, each whole in its own commit, and stopped by its own capacity judgment to leave room for the close. The ninth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md`, opened with position 43 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 44 and 45, each whole in its own commit, and stopped by its own capacity judgment, written before position 46 was opened, to leave room for its correction commit and its close. The tenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md`, opened with position 46 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 47 and 48, each whole in its own commit, and stopped by its own capacity judgment, written before position 49 was opened, to leave room for the close. The eleventh batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`, opened with position 49 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 50 whole in its own commit, and stopped by its own capacity judgment, written before position 51 was opened, to leave room for the close. The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 52 whole in its own commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close. The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there. The fourteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`, opened with position 62 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, and stopped at the section boundary after position 62 because §7's generated reconciliation to §13 did not hold, which that dispatch's Task 1(e) made a STOP (the difference located by row in `records/cc/reports/cc_report_l2_comparison_tabulation_fourteenth_2026_10_04.md` §2.7). The fifteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md`, opened with §7 as that dispatch ordered (**D-670**) and wrote §7, §8 and §9, each whole in its own commit. §7, §8 and §9 are written; §14 stays NOT YET WRITTEN, to be written once each, in the order §7, §8, §9, §14. **A member marked NOT YET TABULATED is UNTOUCHED** — not
  + `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eighth_2026_09_29.md`, opened with position 39 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 40, 41 and 42, each whole in its own commit, and stopped by its own capacity judgment to leave room for the close. The ninth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_ninth_2026_09_29.md`, opened with position 43 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 44 and 45, each whole in its own commit, and stopped by its own capacity judgment, written before position 46 was opened, to leave room for its correction commit and its close. The tenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_tenth_2026_09_29.md`, opened with position 46 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 47 and 48, each whole in its own commit, and stopped by its own capacity judgment, written before position 49 was opened, to leave room for the close. The eleventh batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_eleventh_2026_10_03.md`, opened with position 49 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 50 whole in its own commit, and stopped by its own capacity judgment, written before position 51 was opened, to leave room for the close. The twelfth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_twelfth_2026_10_03.md`, opened with position 51 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated position 52 whole in its own commit, and stopped by its own capacity judgment, written before position 53 was opened, to leave room for the close. The thirteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`, opened with position 53 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, then tabulated positions 54 to 61, each whole in its own commit, and stopped at the member boundary after position 61 because that dispatch bounded the batch there. The fourteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`, opened with position 62 as that dispatch ordered (**D-670**) and tabulated it whole in one commit, and stopped at the section boundary after position 62 because §7's generated reconciliation to §13 did not hold, which that dispatch's Task 1(e) made a STOP (the difference located by row in `records/cc/reports/cc_report_l2_comparison_tabulation_fourteenth_2026_10_04.md` §2.7). The fifteenth batch, under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md`, opened with §7 as that dispatch ordered (**D-670**) and wrote §7, §8, §9 and §14, each whole in its own commit, so that the file's population and its once-written sections are complete. §7, §8, §9 and §14 are written. **A member marked NOT YET TABULATED is UNTOUCHED** — not
--- changed passage 2: replace base lines 74750-74750 -> new lines 74750-74750
  -   once-written sections — §7, §8, §9 and §14 — stand as §0 says: §7, §8 and §9 are written; §14 is NOT YET WRITTEN.
  +   once-written sections — §7, §8, §9 and §14 — stand as §0 says: §7, §8, §9 and §14 are written.
changed passages outside the section: 2
section lines: base 8 -> new 219
base section still NOT YET WRITTEN: True | new section NOT YET WRITTEN: False
ends with newline: True no CR: True
```

### B.4g — §14: the consistency check over the built file

*Saved to scratch as `consistency_s14.txt`.*

```
rows parsed: 4642; travelling refs checked: 2464; as-at refs checked: 861; flags: 0
```

### B.5 — A5 after every section commit: each section's blob against a77405a2

*Saved to scratch as `a5_sections.txt`.*

```
§6.1 to §6.62: a77405a2d3 vs feff1df77f identical: True (3998446 / 3998446 characters)
§1 to §5: a77405a2d3 vs feff1df77f identical: True (15311 / 15311 characters)
§10 to §13: a77405a2d3 vs feff1df77f identical: True (285078 / 285078 characters)
§15: a77405a2d3 vs feff1df77f identical: True (310 / 310 characters)
sizes: 4393194 4419982
§6.1 to §6.62: a77405a2d3 vs cd089cb4a9 identical: True (3998446 / 3998446 characters)
§1 to §5: a77405a2d3 vs cd089cb4a9 identical: True (15311 / 15311 characters)
§10 to §13: a77405a2d3 vs cd089cb4a9 identical: True (285078 / 285078 characters)
§15: a77405a2d3 vs cd089cb4a9 identical: True (310 / 310 characters)
sizes: 4393194 4435006
§6.1 to §6.62: a77405a2d3 vs 3cd269c633 identical: True (3998446 / 3998446 characters)
§1 to §5: a77405a2d3 vs 3cd269c633 identical: True (15311 / 15311 characters)
§10 to §13: a77405a2d3 vs 3cd269c633 identical: True (285078 / 285078 characters)
§15: a77405a2d3 vs 3cd269c633 identical: True (310 / 310 characters)
sizes: 4393194 4438371
§6.1 to §6.62: a77405a2d3 vs 4c15b93388 identical: True (3998446 / 3998446 characters)
§1 to §5: a77405a2d3 vs 4c15b93388 identical: True (15311 / 15311 characters)
§10 to §13: a77405a2d3 vs 4c15b93388 identical: True (285078 / 285078 characters)
§15: a77405a2d3 vs 4c15b93388 identical: True (310 / 310 characters)
sizes: 4393194 4451292
```

## Appendix C — Task 0 and the close

### C.1 — 0(c), A1's enumeration (tools/audit/changed_paths.py), whole

*Saved to scratch as `t0_changed_paths.txt`.*

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventy_seven.md
??	scratch_artifacts/baseline_composing.txt
??	scratch_artifacts/baseline_notation.txt
??	scratch_artifacts/baseline_snapshot.txt
??	scratch_artifacts/baseline_table.md
??	scratch_artifacts/batch_analyze.both.bak
??	scratch_artifacts/batchreg.log
??	scratch_artifacts/bir_after_baroque.txt
??	scratch_artifacts/bir_after_default.txt
??	scratch_artifacts/bir_after_jazz.txt
??	scratch_artifacts/bir_baroque.log
??	scratch_artifacts/bir_baroque.txt
??	scratch_artifacts/bir_default.log
??	scratch_artifacts/bir_default.txt
??	scratch_artifacts/bir_jazz.log
??	scratch_artifacts/bir_jazz.txt
??	scratch_artifacts/build_backfill.txt
??	scratch_artifacts/build_backfill2.txt
??	scratch_artifacts/build_backfill2_err.txt
??	scratch_artifacts/build_backfill_err.txt
??	scratch_artifacts/build_dbg.log
??	scratch_artifacts/build_final.log
??	scratch_artifacts/build_g1.log
??	scratch_artifacts/build_g2.log
??	scratch_artifacts/build_g2b.log
??	scratch_artifacts/build_iso.log
??	scratch_artifacts/build_out.txt
??	scratch_artifacts/build_revert.log
??	scratch_artifacts/build_revert_err.log
??	scratch_artifacts/build_step1.log
??	scratch_artifacts/build_step1b.log
??	scratch_artifacts/build_step1c.log
??	scratch_artifacts/build_step2.log
??	scratch_artifacts/build_stepM.log
??	scratch_artifacts/build_stepM2.log
??	scratch_artifacts/build_stepM_err.log
??	scratch_artifacts/build_task1.log
??	scratch_artifacts/build_task2.log
??	scratch_artifacts/c5_guardhelp.txt
??	scratch_artifacts/c5_p1w.txt
??	scratch_artifacts/c5_triage.txt
??	scratch_artifacts/c5_triage2.txt
??	scratch_artifacts/c8_bar.txt
??	scratch_artifacts/c8_bar2.txt
??	scratch_artifacts/c8_build.log
??	scratch_artifacts/c8_class.txt
??	scratch_artifacts/c8_classchk.txt
??	scratch_artifacts/c8_ct.txt
??	scratch_artifacts/c8_disp.txt
??	scratch_artifacts/c8_dispv.txt
??	scratch_artifacts/c8_gc_t0.txt
??	scratch_artifacts/c8_gc_t1.txt
??	scratch_artifacts/c8_gc_t2.txt
??	scratch_artifacts/c8_gc_t4.txt
??	scratch_artifacts/c8_gc_t4b.txt
??	scratch_artifacts/c8_gp.txt
??	scratch_artifacts/c8_guard_final.txt
??	scratch_artifacts/c8_guard_final2.txt
??	scratch_artifacts/c8_guard_start.txt
??	scratch_artifacts/c8_guard_t0.txt
??	scratch_artifacts/c8_guard_t0b.txt
??	scratch_artifacts/c8_guard_t0c.txt
??	scratch_artifacts/c8_guard_t1.txt
??	scratch_artifacts/c8_guard_t1b.txt
??	scratch_artifacts/c8_guard_t1c.txt
??	scratch_artifacts/c8_guard_t2.txt
??	scratch_artifacts/c8_guard_t2b.txt
??	scratch_artifacts/c8_guard_t4.txt
??	scratch_artifacts/c8_guard_t4b.txt
??	scratch_artifacts/c8_guard_t4c.txt
??	scratch_artifacts/c8_guardclass_start.txt
??	scratch_artifacts/c8_inv.txt
??	scratch_artifacts/c8_lint.txt
??	scratch_artifacts/c8_nt.txt
??	scratch_artifacts/c8_oi357_a.txt
??	scratch_artifacts/c8_oi357_b.txt
??	scratch_artifacts/c8_oi357_c.txt
??	scratch_artifacts/c8_ps.txt
??	scratch_artifacts/c8_r1.txt
??	scratch_artifacts/c8_r12.txt
??	scratch_artifacts/c8_reaim.txt
??	scratch_artifacts/c8_reaimhelp.txt
??	scratch_artifacts/c8_reg.txt
??	scratch_artifacts/c8_regchk.txt
??	scratch_artifacts/c8_routes.txt
??	scratch_artifacts/c8_split.txt
??	scratch_artifacts/c8_sweep.txt
??	scratch_artifacts/c8_sweep2.txt
??	scratch_artifacts/c8_sweep3.txt
??	scratch_artifacts/c8_sweep4.txt
??	scratch_artifacts/c8_sweep5.txt
??	scratch_artifacts/c8_sweep6.txt
??	scratch_artifacts/c8_sweep_list.txt
??	scratch_artifacts/c8_t1_bar.txt
??	scratch_artifacts/c8_t1_bar2.txt
??	scratch_artifacts/c8_t1_blk.txt
??	scratch_artifacts/c8_t1_class.txt
??	scratch_artifacts/c8_t1_class2.txt
??	scratch_artifacts/c8_t1_class3.txt
??	scratch_artifacts/c8_t1_disp.txt
??	scratch_artifacts/c8_t1_disp2.txt
??	scratch_artifacts/c8_t1_fl.txt
??	scratch_artifacts/c8_t1_inv.txt
??	scratch_artifacts/c8_t1_outd.txt
??	scratch_artifacts/c8_t1_reaim.txt
??	scratch_artifacts/c8_t1_reg.txt
??	scratch_artifacts/c8_t1_reg2.txt
??	scratch_artifacts/c8_t1_routes.txt
??	scratch_artifacts/c8_t1_routes2.txt
??	scratch_artifacts/c8_t1_routes3.txt
??	scratch_artifacts/c8_t1_routes4.txt
??	scratch_artifacts/c8_t2_blk.txt
??	scratch_artifacts/c8_t2_class.txt
??	scratch_artifacts/c8_t2_class2.txt
??	scratch_artifacts/c8_t2_class3.txt
??	scratch_artifacts/c8_t2_class4.txt
??	scratch_artifacts/c8_t2_class5.txt
??	scratch_artifacts/c8_t2_disp.txt
??	scratch_artifacts/c8_t2_fl.txt
??	scratch_artifacts/c8_t2_inv.txt
??	scratch_artifacts/c8_t2_outd.txt
??	scratch_artifacts/c8_t2_r1.txt
??	scratch_artifacts/c8_t2_reaim.txt
??	scratch_artifacts/c8_t2_reg.txt
??	scratch_artifacts/c8_t2_routes.txt
??	scratch_artifacts/c8_t4_blk.txt
??	scratch_artifacts/c8_t4_cp.txt
??	scratch_artifacts/c8_t4_cp2.txt
??	scratch_artifacts/c8_t4_cp3.txt
??	scratch_artifacts/c8_t4_cphelp.txt
??	scratch_artifacts/c8_t4_fl.txt
??	scratch_artifacts/c8_t4_fl2.txt
??	scratch_artifacts/c8_t4_inv.txt
??	scratch_artifacts/c8_t4_inv2.txt
??	scratch_artifacts/c8_t4_ng.txt
??	scratch_artifacts/c8_t4_ng2.txt
??	scratch_artifacts/c8_t4_p1w.txt
??	scratch_artifacts/c8_t4_p1w2.txt
??	scratch_artifacts/c8_t4_p1w3.txt
??	scratch_artifacts/c8_t4_r1.txt
??	scratch_artifacts/c8_t4_routes.txt
??	scratch_artifacts/c8_triage.txt
??	scratch_artifacts/c8_triage2.txt
??	scratch_artifacts/c9_changed.txt
??	scratch_artifacts/c9_class.txt
??	scratch_artifacts/c9_classchk.txt
??	scratch_artifacts/c9_guard_start.txt
??	scratch_artifacts/c9_guards1.txt
??	scratch_artifacts/c9_guards2.txt
??	scratch_artifacts/c9_p1w.txt
??	scratch_artifacts/c9_r1.txt
??	scratch_artifacts/c9_reaim.txt
??	scratch_artifacts/c9_regen1.txt
??	scratch_artifacts/c9_regen2.txt
??	scratch_artifacts/c9_regen3.txt
??	scratch_artifacts/c9_routes.txt
??	scratch_artifacts/c9_shellguard_1.txt
??	scratch_artifacts/c9_shellguard_rep.txt
??	scratch_artifacts/c9_split.txt
??	scratch_artifacts/c9_verify1.txt
??	scratch_artifacts/c9_verify2.txt
??	scratch_artifacts/cadence_tests.txt
??	scratch_artifacts/cc_collect.txt
??	scratch_artifacts/ccc_collect2.txt
??	scratch_artifacts/ccc_log.txt
??	scratch_artifacts/ccc_notation.txt
??	scratch_artifacts/ccc_path.txt
??	scratch_artifacts/char_baroque.txt
??	scratch_artifacts/char_baroque_l5m.txt
??	scratch_artifacts/char_default.txt
??	scratch_artifacts/char_default_l5m.txt
??	scratch_artifacts/char_jazz.txt
??	scratch_artifacts/char_jazz_l5m.txt
??	scratch_artifacts/claude_baroque.txt
??	scratch_artifacts/claude_baroque_sorted.txt
??	scratch_artifacts/claude_default.txt
??	scratch_artifacts/claude_default_sorted.txt
??	scratch_artifacts/claude_jazz.txt
??	scratch_artifacts/claude_jazz_sorted.txt
??	scratch_artifacts/clone_algomusdata.txt
??	scratch_artifacts/clone_asap.txt
??	scratch_artifacts/clone_batch1.log
??	scratch_artifacts/clone_batch2.log
??	scratch_artifacts/clone_batch3.log
??	scratch_artifacts/clone_batik.log
??	scratch_artifacts/clone_bcfb.txt
??	scratch_artifacts/clone_cocopops.txt
??	scratch_artifacts/clone_figbass.txt
??	scratch_artifacts/clone_lieder.txt
??	scratch_artifacts/clone_mcma.log
??	scratch_artifacts/clone_mikrokosmos.log
??	scratch_artifacts/clone_openewld.txt
??	scratch_artifacts/clone_piano_svsep.log
??	scratch_artifacts/clone_protovoice.txt
??	scratch_artifacts/clone_schenker41.txt
??	scratch_artifacts/clone_sq.txt
??	scratch_artifacts/clone_vocsep.log
??	scratch_artifacts/cmp_manifest_sha.py
??	scratch_artifacts/commit1_msg.txt
??	scratch_artifacts/commit1_out.txt
??	scratch_artifacts/commit2_msg.txt
??	scratch_artifacts/commit2_out.txt
??	scratch_artifacts/commit_msg_step2.txt
??	scratch_artifacts/comp_run.txt
??	scratch_artifacts/comp_run2.txt
??	scratch_artifacts/comp_run3.txt
??	scratch_artifacts/comp_run4.txt
??	scratch_artifacts/comp_step1.txt
??	scratch_artifacts/comp_step1c.txt
??	scratch_artifacts/composing.cobertura.xml
??	scratch_artifacts/composing_final_out.txt
??	scratch_artifacts/composing_full.txt
??	scratch_artifacts/composing_new_out.txt
??	scratch_artifacts/composing_test.log
??	scratch_artifacts/composing_test2.log
??	scratch_artifacts/composing_tests_out.txt
??	scratch_artifacts/corpus_decode_chord_g1/
??	scratch_artifacts/corpus_decode_chord_g2/
??	scratch_artifacts/corpus_decode_chord_g2iso/
??	scratch_artifacts/corpus_decode_chord_g6/
??	scratch_artifacts/corpus_decode_chord_step2final_A/
??	scratch_artifacts/corpus_decode_chord_step2final_B/
??	scratch_artifacts/corpus_decode_chord_stepM/
??	scratch_artifacts/corpus_ours_check/
??	scratch_artifacts/corpus_ours_check_g2/
??	scratch_artifacts/cov_after.log
??	scratch_artifacts/cov_after2.log
??	scratch_artifacts/cov_final.log
??	scratch_artifacts/cov_final2.log
??	scratch_artifacts/coverage/
??	scratch_artifacts/coverage_merged.txt
??	scratch_artifacts/coverage_report.txt
??	scratch_artifacts/curation_worksheet.txt
??	scratch_artifacts/decode_baroque_step0.log
??	scratch_artifacts/decode_default_step0.log
??	scratch_artifacts/decode_g1_baroque.log
??	scratch_artifacts/decode_g1_baroque2.log
??	scratch_artifacts/decode_g1_default2.log
??	scratch_artifacts/decode_g1_driver.py
??	scratch_artifacts/decode_g2_baroque.log
??	scratch_artifacts/decode_g2_default.log
??	scratch_artifacts/decode_g2iso.log
??	scratch_artifacts/decode_step0_run.log
??	scratch_artifacts/decode_stepM_baroque.log
??	scratch_artifacts/decode_stepM_default.log
??	scratch_artifacts/decompose_g1_after.log
??	scratch_artifacts/decompose_g1_before.log
??	scratch_artifacts/decompose_g2_after.log
??	scratch_artifacts/decompose_g2_before.log
??	scratch_artifacts/decompose_g2iso.log
??	scratch_artifacts/decompose_step0.log
??	scratch_artifacts/dlc_baseline_run.log
??	scratch_artifacts/dlc_pins.json
??	scratch_artifacts/driver_smoke.err
??	scratch_artifacts/e0dp_cap_decomp.py
??	scratch_artifacts/e0prime_grader.log
??	scratch_artifacts/e0prime_supp.log
??	scratch_artifacts/e0prime_supp.py
??	scratch_artifacts/filter_hunks.py
??	scratch_artifacts/fs_regen_baroque.log
??	scratch_artifacts/fs_regen_default.log
??	scratch_artifacts/fs_regen_driver.log
??	scratch_artifacts/fs_regen_jazz.log
??	scratch_artifacts/g1_composing.log
??	scratch_artifacts/g1_decode_tests.log
??	scratch_artifacts/g1_notation.log
??	scratch_artifacts/g1_one_decode.err
??	scratch_artifacts/g1_one_decode.json
??	scratch_artifacts/g1_snapshots.log
??	scratch_artifacts/g2_composing.log
??	scratch_artifacts/g2_decode_tests.log
??	scratch_artifacts/g2_notation.log
??	scratch_artifacts/g2_snap.log
??	scratch_artifacts/gate_after_baroque.txt
??	scratch_artifacts/gate_after_default.txt
??	scratch_artifacts/gate_after_jazz.txt
??	scratch_artifacts/gate_baroque.txt
??	scratch_artifacts/gate_before_baroque.txt
??	scratch_artifacts/gate_before_default.txt
??	scratch_artifacts/gate_before_jazz.txt
??	scratch_artifacts/gate_check.py
??	scratch_artifacts/gate_setdiff.py
??	scratch_artifacts/grade_g1_after.log
??	scratch_artifacts/grade_g1_before.log
??	scratch_artifacts/grade_g2_after.log
??	scratch_artifacts/grade_g2_before.log
??	scratch_artifacts/grade_g2iso.log
??	scratch_artifacts/grade_step0.log
??	scratch_artifacts/guitarset_curl_err.txt
??	scratch_artifacts/guitarset_dl_err.txt
??	scratch_artifacts/guitarset_zenodo.json
??	scratch_artifacts/harvest_final.txt
??	scratch_artifacts/harvest_final2.txt
??	scratch_artifacts/harvest_final3.txt
??	scratch_artifacts/harvest_run1.txt
??	scratch_artifacts/harvest_run2.txt
??	scratch_artifacts/harvest_run3.txt
??	scratch_artifacts/hd_LIST.txt
??	scratch_artifacts/hd_branch.txt
??	scratch_artifacts/hd_dl.txt
??	scratch_artifacts/hd_err.txt
??	scratch_artifacts/hd_lists.json
??	scratch_artifacts/hd_repo.json
??	scratch_artifacts/hd_repos.txt
??	scratch_artifacts/hd_repos_final.txt
??	scratch_artifacts/hd_root.json
??	scratch_artifacts/hd_tree.json
??	scratch_artifacts/humdrum_data_closure_71repos.txt
??	scratch_artifacts/humdrum_gitmodules.txt
??	scratch_artifacts/humdrum_gitmodules2.txt
??	scratch_artifacts/keyparse_probe.log
??	scratch_artifacts/l4.err
??	scratch_artifacts/l4.patch
??	scratch_artifacts/l5.err
??	scratch_artifacts/l5.patch
??	scratch_artifacts/l5_smoke.err
??	scratch_artifacts/l5_smoke.json
??	scratch_artifacts/line_hits.py
??	scratch_artifacts/ninja_direct.txt
??	scratch_artifacts/notation.cobertura.xml
??	scratch_artifacts/notation_after.txt
??	scratch_artifacts/notation_final.txt
??	scratch_artifacts/notation_full.txt
??	scratch_artifacts/notation_run.txt
??	scratch_artifacts/notation_step1.txt
??	scratch_artifacts/notation_test.log
??	scratch_artifacts/notation_test2.log
??	scratch_artifacts/notation_tests_out.txt
??	scratch_artifacts/oi357_production_arm/
??	scratch_artifacts/oi357_production_arm_legacy_control/
??	scratch_artifacts/ours_A/
??	scratch_artifacts/ours_B/
??	scratch_artifacts/ours_check_baroque.log
??	scratch_artifacts/parse_cov.py
??	scratch_artifacts/parse_merge.py
??	scratch_artifacts/pdmx_inspect.py
??	scratch_artifacts/pipeline_snapshot_tests_out.txt
??	scratch_artifacts/quote_verify.txt
??	scratch_artifacts/quote_verify2.txt
??	scratch_artifacts/reg_A.json
??	scratch_artifacts/reg_B.json
??	scratch_artifacts/reg_pre_acq.json
??	scratch_artifacts/reg_run1.json
??	scratch_artifacts/reg_run1.txt
??	scratch_artifacts/reg_run2.txt
??	scratch_artifacts/regen_baroque.log
??	scratch_artifacts/regen_baroque_l5.log
??	scratch_artifacts/regen_default.log
??	scratch_artifacts/regen_default_l5.log
??	scratch_artifacts/regen_driver.log
??	scratch_artifacts/regen_g2_baroque.log
??	scratch_artifacts/regen_jazz.log
??	scratch_artifacts/regen_jazz_l5.log
??	scratch_artifacts/rel_tests.txt
??	scratch_artifacts/repro30.txt
??	scratch_artifacts/repro_block.txt
??	scratch_artifacts/repro_check/
??	scratch_artifacts/s5_2b_task1_tables.txt
??	scratch_artifacts/set_baroque.txt
??	scratch_artifacts/set_default.txt
??	scratch_artifacts/set_jazz.txt
??	scratch_artifacts/setdiff.py
??	scratch_artifacts/sm_comp.txt
??	scratch_artifacts/sm_notation.txt
??	scratch_artifacts/sm_snap.txt
??	scratch_artifacts/smoke.err
??	scratch_artifacts/smoke.json
??	scratch_artifacts/smoke_and_cadence.py
??	scratch_artifacts/snap_after.txt
??	scratch_artifacts/snap_final.txt
??	scratch_artifacts/snap_full.txt
??	scratch_artifacts/snap_run.txt
??	scratch_artifacts/snap_step1.txt
??	scratch_artifacts/snap_test.log
??	scratch_artifacts/snap_test2.log
??	scratch_artifacts/snapshot_full.txt
??	scratch_artifacts/stepM_analysis_all.txt
??	scratch_artifacts/stepM_analysis_test.txt
??	scratch_artifacts/stepM_analyze.py
??	scratch_artifacts/stepM_l5_measure.txt
??	scratch_artifacts/taskB_run.sh
??	scratch_artifacts/u1_byteid/
??	scratch_artifacts/u1_composing_tests.txt
??	scratch_artifacts/u1_pipeline_snap.txt
??	scratch_artifacts/v2_composing.txt
??	scratch_artifacts/v2_notation.txt
??	scratch_artifacts/v2_snap.txt
??	scratch_artifacts/wjd_curl_err.txt
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
396 changed path record(s) [worktree]
```

### C.2 — 0(d), the last-bytes check

*Saved to scratch as `t0_lastbytes_out.txt`.*

```
records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md
  blob (--no-filters): 425081e5e09378b3b7986117bd1b264b5f3ddf09 size: 172405
  zero bytes: 0
  carriage returns: 0
  last 70 bytes: b'. TOWARDS the ultimate objective and TOWARDS the guiding principles.*\n'
  ends with newline byte: True
records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventy_seven.md
  blob (--no-filters): 4001d599f82b450cf7f2bef2ae196f3dd4d2995b size: 12207
  zero bytes: 0
  carriage returns: 0
  last 70 bytes: b'ce: Cowork, 2026-10-04 (Stockholm), the sitting booted on entry 276.*\n'
  ends with newline byte: True
```

### C.3a — 0(f), the opening guard capture, whole

*Saved to scratch as `guard_open.txt`.*

```
wrote tools\audit\guard_state.json
  [PASS] tools/audit/register_lint.py 
  [PASS] tools/audit/index_status_lint.py --check
  [PASS] tools/audit/gen_arm_comment_sweep.py --check
  [PASS] tools/audit/local_patches_check.py 
  [PASS] tools/audit/local_patches_check.py --establish --check
  [PASS] tools/audit/guard_armed_check.py 
  [PASS] tools/audit/process_check.py --establish --check
  [PASS] tools/audit/shell_read_guard.py --establish --check
  [PASS] tools/audit/output_encoding.py --establish --check
  [PASS] tools/audit/changed_paths.py --establish
  [PASS] tools/audit/claude_md_rule_triage.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --establish --check
  [PASS] tools/audit/instrument_arm_declaration_effect.py --check
  [FAIL] tools/audit/gen_phase3_gate_partition.py --check
  [PASS] tools/audit/gen_nongating_apparatus_rows.py --check
  [PASS] tools/audit/gen_discard_records.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach_rows.py --check
  [PASS] tools/audit/gen_gating_row_sizing.py --check
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [PASS] tools/audit/decisions/gen_phase1q_snapshot_establishment.py --check
  [PASS] tools/audit/gen_period_stratum_split.py --check
  [PASS] tools/audit/gen_july_screen.py --check
  [PASS] tools/audit/gen_specification_document_set.py --check
  [PASS] tools/audit/gen_l0_l1_outgoing_population.py --check
  [PASS] tools/audit/gen_withheld_family_reading.py --subject l2 --check
  [FAIL] tools/audit/gen_artifact_inventory.py --check
  [FAIL] tools/audit/gen_artifact_inventory_surface.py --check
  [PASS] tools/audit/gen_status_archive_pass.py --check
  [PASS] tools/audit/gen_doc_change_candidates.py --check
  [FAIL] tools/audit/gen_test_construction_evidence.py --check
  [PASS] tools/audit/gen_decisions_filter.py --check
  [FAIL] tools/audit/gen_retirement_caller_check.py --check
  [PASS] tools/audit/gen_deciding_act_recovery.py --check
  [PASS] tools/audit/gen_rulings_sort.py --check
  [PASS] tools/audit/gen_sole_carrier_subclass.py --check
  [PASS] tools/audit/gen_ratified_document_check.py --check
  [FAIL] tools/audit/decisions/apply_soft_discard.py --check
  [FAIL] tools/audit/decisions/apply_residue_discard.py --check
  [PASS] tools/audit/gen_framework_untrusted_candidates.py --check
  [PASS] tools/audit/gen_phase1_gate_readers.py --check
  [PASS] tools/audit/gen_discard_reach_split.py --check
  [PASS] tools/audit/decisions/gen_retired_subject_moves.py --check
  [PASS] tools/audit/gen_census_movement_classification.py --check
  [PASS] tools/audit/gen_governing_surface_spans.py --check
  [PASS] tools/audit/gen_governing_surface_readers.py --check
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair CLAUDE.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair OPEN_ITEMS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair DECISIONS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair BUILD_AND_TEST.md
  [PASS] tools/audit/gen_status_batch_bound.py --check
  [PASS] tools/audit/gen_status_residue_move.py --check
  [PASS] tools/audit/gen_retirement_census_movement.py --check
  [PASS] tools/audit/gen_claude_md_finer_spans.py --check
  [PASS] tools/audit/gen_claude_md_finer_surface.py --check
  [PASS] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [PASS] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
  [PASS] tools/audit/gen_l2_outgoing_population.py --check
  [PASS] tools/audit/decisions/gen_decisions_register.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --verify
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --producible
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
  [PASS] tools/audit/decisions/gen_reads5_repack.py --check
  [PASS] tools/audit/decisions/gen_decision_clusters.py --check
  [PASS] tools/audit/decisions/gen_phase1w_legacy_verification.py --check
  [PASS] tools/audit/decisions/reaim_home_anchors.py --check
  [PASS] tools/audit/decisions/gen_live_prohibition_pointers.py --check
  [PASS] tools/audit/gen_claude_md_growth.py --check
  [PASS] tools/audit/prune_at_amendment_lint.py --check
  [PASS] tools/open_items_split_check.py 
  [PASS] tools/notation_seams/gen_callpath_facts.py --check
  [NOT RUN] tools/audit/gen_ratification_surface_set.py
  [NOT RUN] tools/audit/reaim_ratification_surface_paths.py
  [NOT RUN] tools/audit/decisions/gen_verbatim_subject_consistency.py
  [NOT RUN] tools/audit/gen_reserved_word_scanner.py
  [HISTORICAL] tools/audit/gen_phase1_completion_inventory.py
  [HISTORICAL] tools/audit/gen_phase1_finish_line.py
  [HISTORICAL] tools/audit/decisions/gen_outstanding_delegations.py
  [HISTORICAL] tools/audit/gen_claude_md_finer_archive.py
  [HISTORICAL] tools/audit/gen_post_split_archive.py
  [HISTORICAL] tools/audit/decisions/gen_phase1n_reading_regime.py
  [HISTORICAL] tools/audit/decisions/gen_reads5_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads6_yield.py
  [HISTORICAL] tools/audit/decisions/gen_phase1m_measurements.py
  [HISTORICAL] tools/audit/decisions/gen_phase1g_triage.py
  [HISTORICAL] tools/audit/decisions/gen_reads1_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads2_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads3_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_yield.py
  [HISTORICAL] tools/audit/decisions/gen_finish_line_item1_routes.py
  [HISTORICAL] tools/audit/decisions/gen_item1_rehome_blocker.py
  [HISTORICAL] tools/audit/decisions/gen_r1_superseded_reach.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_oi326_application.py
  [HISTORICAL] tools/audit/gen_claude_md_prune_backlog.py
80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

### C.3b — 0(f), the guard classification after it

*Saved to scratch as `guardclass_open.txt`.*

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

### C.4a — 2(d), the closing guard capture, whole

*Saved to scratch as `guard_close.txt`.*

```
wrote tools\audit\guard_state.json
  [PASS] tools/audit/register_lint.py 
  [PASS] tools/audit/index_status_lint.py --check
  [PASS] tools/audit/gen_arm_comment_sweep.py --check
  [PASS] tools/audit/local_patches_check.py 
  [PASS] tools/audit/local_patches_check.py --establish --check
  [PASS] tools/audit/guard_armed_check.py 
  [PASS] tools/audit/process_check.py --establish --check
  [PASS] tools/audit/shell_read_guard.py --establish --check
  [PASS] tools/audit/output_encoding.py --establish --check
  [PASS] tools/audit/changed_paths.py --establish
  [PASS] tools/audit/claude_md_rule_triage.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --establish --check
  [PASS] tools/audit/instrument_arm_declaration_effect.py --check
  [FAIL] tools/audit/gen_phase3_gate_partition.py --check
  [PASS] tools/audit/gen_nongating_apparatus_rows.py --check
  [PASS] tools/audit/gen_discard_records.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach_rows.py --check
  [PASS] tools/audit/gen_gating_row_sizing.py --check
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [PASS] tools/audit/decisions/gen_phase1q_snapshot_establishment.py --check
  [PASS] tools/audit/gen_period_stratum_split.py --check
  [PASS] tools/audit/gen_july_screen.py --check
  [PASS] tools/audit/gen_specification_document_set.py --check
  [PASS] tools/audit/gen_l0_l1_outgoing_population.py --check
  [PASS] tools/audit/gen_withheld_family_reading.py --subject l2 --check
  [FAIL] tools/audit/gen_artifact_inventory.py --check
  [FAIL] tools/audit/gen_artifact_inventory_surface.py --check
  [PASS] tools/audit/gen_status_archive_pass.py --check
  [PASS] tools/audit/gen_doc_change_candidates.py --check
  [FAIL] tools/audit/gen_test_construction_evidence.py --check
  [PASS] tools/audit/gen_decisions_filter.py --check
  [FAIL] tools/audit/gen_retirement_caller_check.py --check
  [PASS] tools/audit/gen_deciding_act_recovery.py --check
  [PASS] tools/audit/gen_rulings_sort.py --check
  [PASS] tools/audit/gen_sole_carrier_subclass.py --check
  [PASS] tools/audit/gen_ratified_document_check.py --check
  [FAIL] tools/audit/decisions/apply_soft_discard.py --check
  [FAIL] tools/audit/decisions/apply_residue_discard.py --check
  [PASS] tools/audit/gen_framework_untrusted_candidates.py --check
  [PASS] tools/audit/gen_phase1_gate_readers.py --check
  [PASS] tools/audit/gen_discard_reach_split.py --check
  [PASS] tools/audit/decisions/gen_retired_subject_moves.py --check
  [PASS] tools/audit/gen_census_movement_classification.py --check
  [PASS] tools/audit/gen_governing_surface_spans.py --check
  [PASS] tools/audit/gen_governing_surface_readers.py --check
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair CLAUDE.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair OPEN_ITEMS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair DECISIONS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair BUILD_AND_TEST.md
  [PASS] tools/audit/gen_status_batch_bound.py --check
  [PASS] tools/audit/gen_status_residue_move.py --check
  [PASS] tools/audit/gen_retirement_census_movement.py --check
  [PASS] tools/audit/gen_claude_md_finer_spans.py --check
  [PASS] tools/audit/gen_claude_md_finer_surface.py --check
  [PASS] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [PASS] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
  [PASS] tools/audit/gen_l2_outgoing_population.py --check
  [PASS] tools/audit/decisions/gen_decisions_register.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --verify
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --producible
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
  [PASS] tools/audit/decisions/gen_reads5_repack.py --check
  [PASS] tools/audit/decisions/gen_decision_clusters.py --check
  [PASS] tools/audit/decisions/gen_phase1w_legacy_verification.py --check
  [PASS] tools/audit/decisions/reaim_home_anchors.py --check
  [PASS] tools/audit/decisions/gen_live_prohibition_pointers.py --check
  [PASS] tools/audit/gen_claude_md_growth.py --check
  [PASS] tools/audit/prune_at_amendment_lint.py --check
  [PASS] tools/open_items_split_check.py 
  [PASS] tools/notation_seams/gen_callpath_facts.py --check
  [NOT RUN] tools/audit/gen_ratification_surface_set.py
  [NOT RUN] tools/audit/reaim_ratification_surface_paths.py
  [NOT RUN] tools/audit/decisions/gen_verbatim_subject_consistency.py
  [NOT RUN] tools/audit/gen_reserved_word_scanner.py
  [HISTORICAL] tools/audit/gen_phase1_completion_inventory.py
  [HISTORICAL] tools/audit/gen_phase1_finish_line.py
  [HISTORICAL] tools/audit/decisions/gen_outstanding_delegations.py
  [HISTORICAL] tools/audit/gen_claude_md_finer_archive.py
  [HISTORICAL] tools/audit/gen_post_split_archive.py
  [HISTORICAL] tools/audit/decisions/gen_phase1n_reading_regime.py
  [HISTORICAL] tools/audit/decisions/gen_reads5_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads6_yield.py
  [HISTORICAL] tools/audit/decisions/gen_phase1m_measurements.py
  [HISTORICAL] tools/audit/decisions/gen_phase1g_triage.py
  [HISTORICAL] tools/audit/decisions/gen_reads1_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads2_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads3_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_yield.py
  [HISTORICAL] tools/audit/decisions/gen_finish_line_item1_routes.py
  [HISTORICAL] tools/audit/decisions/gen_item1_rehome_blocker.py
  [HISTORICAL] tools/audit/decisions/gen_r1_superseded_reach.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_oi326_application.py
  [HISTORICAL] tools/audit/gen_claude_md_prune_backlog.py
80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

### C.4b — 2(d), the guard classification after it

*Saved to scratch as `guardclass_close.txt`.*

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

### C.4c — 2(d), the two captures compared verdict by verdict, and guard_state.json's summary and per-tool verdicts

*Saved to scratch as `gcompare_out.txt`.*

```
opening verdict lines: 104 ; closing verdict lines: 104
IDENTICAL VERDICT FOR VERDICT: True
closing FAIL set:
  [FAIL] tools/audit/gen_phase3_gate_partition.py --check
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [FAIL] tools/audit/gen_artifact_inventory.py --check
  [FAIL] tools/audit/gen_artifact_inventory_surface.py --check
  [FAIL] tools/audit/gen_test_construction_evidence.py --check
  [FAIL] tools/audit/gen_retirement_caller_check.py --check
  [FAIL] tools/audit/decisions/apply_soft_discard.py --check
  [FAIL] tools/audit/decisions/apply_residue_discard.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
closing summary: 80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
guard_state.json summary at 2e17c3be: {'run': 80, 'passing': 68, 'failing': 12, 'failing_tools': [{'tool': 'tools/audit/gen_phase3_gate_partition.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_filing_convention_application.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_artifact_inventory.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_artifact_inventory_surface.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_test_construction_evidence.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_retirement_caller_check.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/apply_soft_discard.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/apply_residue_discard.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_epoch_write_path.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_recognizer_establishment_sort.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/gen_home_classification.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/gen_phase1p_delegation_bar.py', 'args': ['--check']}], 'not_run': 4, 'historical_records': 19}
guard_state.json summary, new blob e8368a23ceec45ef63355b36ef9af43674641838: {'run': 80, 'passing': 68, 'failing': 12, 'failing_tools': [{'tool': 'tools/audit/gen_phase3_gate_partition.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_filing_convention_application.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_artifact_inventory.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_artifact_inventory_surface.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_test_construction_evidence.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_retirement_caller_check.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/apply_soft_discard.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/apply_residue_discard.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_epoch_write_path.py', 'args': ['--check']}, {'tool': 'tools/audit/gen_recognizer_establishment_sort.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/gen_home_classification.py', 'args': ['--check']}, {'tool': 'tools/audit/decisions/gen_phase1p_delegation_bar.py', 'args': ['--check']}], 'not_run': 4, 'historical_records': 19}
per-tool verdicts read from the artifact's `runs`: 80 and 80 ; identical: True
FAIL in the new artifact: ['tools/audit/decisions/apply_residue_discard.py --check', 'tools/audit/decisions/apply_soft_discard.py --check', 'tools/audit/decisions/gen_home_classification.py --check', 'tools/audit/decisions/gen_phase1p_delegation_bar.py --check', 'tools/audit/gen_artifact_inventory.py --check', 'tools/audit/gen_artifact_inventory_surface.py --check', 'tools/audit/gen_epoch_write_path.py --check', 'tools/audit/gen_filing_convention_application.py --check', 'tools/audit/gen_phase3_gate_partition.py --check', 'tools/audit/gen_recognizer_establishment_sort.py --check', 'tools/audit/gen_retirement_caller_check.py --check', 'tools/audit/gen_test_construction_evidence.py --check']
```

### C.5a — 2(b), the forward bound's --apply

*Saved to scratch as `bound_apply.txt`.*

```
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 2,591 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

### C.5b — 2(b), its --check

*Saved to scratch as `bound_check.txt`.*

```
  entries moved: 1, 2,591 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

### C.6 — 2(c), the five regenerations and their --check outputs

*Saved to scratch as `regen.txt`.*

```
=== gen_evidence_pin_membership
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 102
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
write exit:0
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 102
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
check exit:0
=== gen_l0_l1_outgoing_population
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
write exit:0
l0_l1_outgoing_population.json re-derives
check exit:0
=== gen_l2_outgoing_population
item 1: ## The joint estimator — the standing rules of the production inference layer — 286 lines
item 1: #### Layer 3 — key/mode is the sequence decoder — 207 lines
item 1: #### Layer 4 — the per-slice chord-symbol decoder — 140 lines
item 1: #### Layer 5 — the function/cadence layer — 117 lines
item 2: 20 distinct names, 20 resolve (1123671 bytes), 8 in the specification set
item 3: 26 in-set files with a hit, 2664 distinct hit lines over them (ARCHITECTURE.md inside the four spans: 87, outside: 683); residue files: 168
item 4: in a specification-set member — 56
item 4: in an item-2 document that resolves — 28
item 4: inside item 1 — 19
item 4: reached by item 4 alone — 8
transfer span: 287 lines
tabulation population: 62 members, 14232 lines, 1317940 bytes
wrote C:\s\MS\tools\audit\l2_outgoing_population.json
write exit:0
l2_outgoing_population.json re-derives
check exit:0
=== gen_defense_share
wrote tools/audit/defense_share.json
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   39804  ( 8.72%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (104609): 12.39%
    of the whole session-start read (246771): 5.25%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
write exit:0
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   39804  ( 8.72%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (104609): 12.39%
    of the whole session-start read (246771): 5.25%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
check exit:0
=== gen_session_start_read_size
wrote tools/audit/session_start_read_size.json
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              39804
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 168350, the six session-start spans 104609, overstated by 63741
    CLAUDE.md                                                                104609
    STATUS.md                                                                 11609
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 246771
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 246771 [ruled membership]  (-120350, -32.78%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 246771 [ruled membership]  (-50061, -16.87%)  <- CROSSES A REGIME BOUNDARY
write exit:0
the session-start read measurement re-derives
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              39804
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 168350, the six session-start spans 104609, overstated by 63741
    CLAUDE.md                                                                104609
    STATUS.md                                                                 11609
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 246771
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 246771 [ruled membership]  (-120350, -32.78%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 246771 [ruled membership]  (-50061, -16.87%)  <- CROSSES A REGIME BOUNDARY
check exit:0
```

### C.7 — 2(c), the artifacts compared line by line with the last section commit 2e17c3be, and A3's tally check

*Saved to scratch as `cmp_artifacts_out.txt`.*

```
===== tools/audit/evidence_pin_membership.json: committed blob 54f774d82a2d2e5a9ec99b13666bd83d63ac5257 -> new blob 54f774d82a2d2e5a9ec99b13666bd83d63ac5257: IDENTICAL
===== tools/audit/l0_l1_outgoing_population.json: committed blob e310fb57ac53f9a06f8a9295d70c17ec143e3ce3 -> new blob e310fb57ac53f9a06f8a9295d70c17ec143e3ce3: IDENTICAL
===== tools/audit/l2_outgoing_population.json: committed blob 3c0005274cbfca42e0ae6f67e3627e5bb2e81bb9 -> new blob ddc45c24a658fd1d248b0214f3158a889eacb444: MOVED
  --- committed
  +++ new
  @@ -753 +753 @@
  -    "boundary": 1023,
  +    "boundary": 1022,
  @@ -776 +776 @@
  -    "struck": 63,
  +    "struck": 62,
  @@ -40133,2 +40133,2 @@
  -     "hit_lines_distinct": 2,
  -     "hits": 3,
  +     "hit_lines_distinct": 1,
  +     "hits": 1,
  @@ -40137,12 +40136,0 @@
  -      {
  -       "line_number": 8,
  -       "term": "boundary",
  -       "tier": "admitting",
  -       "line": "*Last updated: 2026-10-04 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`. **★★ THE L2 TABULATION REACHED ITS LAST MEMBER: POSITION 62, THE L0/L1 TRANSFER INPUT, IS TABULATED WHOLE, AND THE READ
  -      },
  -      {
  -       "line_number": 8,
  -       "term": "struck",
  -       "tier": "admitting",
  -       "line": "*Last updated: 2026-10-04 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`. **★★ THE L2 TABULATION REACHED ITS LAST MEMBER: POSITION 62, THE L0/L1 TRANSFER INPUT, IS TABULATED WHOLE, AND THE READ
  -      },
===== tools/audit/defense_share.json: committed blob d3a319706f6ee83cfa26f1d768f5e19d99a74c0e -> new blob 63ea64563bf463cd87845cdbe0ec9b24353c4785: MOVED
  --- committed
  +++ new
  @@ -80 +80 @@
  -  "the_whole_ordinary_session_start_read": 247030,
  +  "the_whole_ordinary_session_start_read": 246771,
===== tools/audit/session_start_read_size.json: committed blob dc8c9a7e03494f2b181f0eb5de9142f4198f6474 -> new blob deae34383394af7f2bf5a480677ee5177f396880: MOVED
  --- committed
  +++ new
  @@ -179 +179 @@
  -   "STATUS.md": 11868,
  +   "STATUS.md": 11609,
  @@ -183 +183 @@
  -  "total_characters": 247030,
  +  "total_characters": 246771,
  @@ -279 +279 @@
  -   "to_total": 247030,
  +   "to_total": 246771,
  @@ -281,2 +281,2 @@
  -   "change_in_characters": -120091,
  -   "change_percent": -32.71,
  +   "change_in_characters": -120350,
  +   "change_percent": -32.78,
  @@ -290 +290 @@
  -   "to_total": 247030,
  +   "to_total": 246771,
  @@ -292,2 +292,2 @@
  -   "change_in_characters": -49802,
  -   "change_percent": -16.78,
  +   "change_in_characters": -50061,
  +   "change_percent": -16.87,
===== tools/audit/status_batch_bound.json: committed blob fc7baaaca69cb8d7751bd43c51cfc6dd9bda16a1 -> new blob 37eb33bb7d3d678d0a90504846625a7991b5a28e: MOVED
  --- committed
  +++ new
  @@ -4 +4 @@
  - "dispatch": "cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md, Task 2",
  + "dispatch": "cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md, Task 2",
  @@ -491,0 +492,6 @@
  +  },
  +  {
  +   "executing_act": "cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md, Task 2",
  +   "base_commit": "92a1159f875a8ef1f1eebdb0d3e55bbb23d820ee",
  +   "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md",
  +   "the_kind_of_move": "ordinary"
  @@ -495,2 +501,2 @@
  - "base_commit": "7c0e8ee9eff818528de690601553beed1ac21ea2",
  - "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md",
  + "base_commit": "92a1159f875a8ef1f1eebdb0d3e55bbb23d820ee",
  + "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md",
  @@ -499 +505 @@
  - "characters_moved": 2535,
  + "characters_moved": 2591,
  @@ -503,2 +509,2 @@
  -   "characters": 2535,
  -   "sha256": "17e0d38f5d97ef3dfb9657889891944af8e379329020fcff067727196d8dca64",
  +   "characters": 2591,
  +   "sha256": "065ba4bbf54b4a64ba12c9d707917b93f1a7012b50104f398cb99984fc62841f",
  @@ -507 +513 @@
  -   "opening": "*2026-10-04 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_thirteenth_2026_10_03.md`. **★★ THE L2 TABULATION CONTINUED FROM PO"
  +   "opening": "*2026-10-04 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourteenth_2026_10_04.md`. **★★ THE L2 TABULATION REACHED ITS LAST "
===== A3 tally check
term | tally committed | tally new | tally change | STATUS.md residue hit_records committed | new | change | equal
boundary | 1023 | 1022 | -1 | 2 | 1 | -1 | True
struck | 63 | 62 | -1 | 1 | 0 | -1 | True
every term's tally change equals its change in STATUS.md's residue hit records: True
terms whose tally moved: 2
every other field outside STATUS.md's residue record and the tally identical: True
the_tabulation_population -> the_members identical by that path: True (62 and 62 members)
residue file list identical: True
STATUS.md residue record: hits 3 -> 1 ; hit_lines_distinct 2 -> 1
```

### C.8 — 0(b), the chain below the previous close

*Saved to scratch as `t0_chain_out.txt`.*

```
commit 5aa808b736207da82e64aff6962520ee5eee8225 parent c3cd3ba47d739238930c5d9b7da3d71972e05536 tree abd2bc901f0ced4ed9a11e9cda5ce3c404a6ab64 subject: Close: the L2 tabulation at position 62 and its sections so far, under its dispatch
    STATUS.md                                          |    2 +-
    STATUS_ARCHIVE.md                                  |    4 +
    ..._comparison_tabulation_fourteenth_2026_10_04.md | 2206 ++++++++++++++++++++
    tools/audit/defense_share.json                     |    2 +-
    tools/audit/gen_status_batch_bound.py              |   51 +-
    tools/audit/guard_state.json                       |   12 +-
    tools/audit/l2_outgoing_population.json            |    4 +-
    tools/audit/session_start_read_size.json           |   16 +-
    tools/audit/status_batch_bound.json                |   20 +-
commit c3cd3ba47d739238930c5d9b7da3d71972e05536 parent 7c0e8ee9eff818528de690601553beed1ac21ea2 tree 9f90971057007769f27d16b26bda89b7ddb2d7ce subject: comparison L2: member 62 tabulated - 49 pointer rows, 4 full rows and 3 flagged items, proposals only
    .../cowork_comparison_l2_reading.md                | 766 ++++++++++++++++++++-
commit 7c0e8ee9eff818528de690601553beed1ac21ea2 parent 57a4293e5356e5be9443ee8c119de1c73c280c81 tree 003553ed96c5442737eb5ecd13c18f1eb0ceb0ad subject: record: entry 276 and the fourteenth L2 tabulation dispatch
    ..._comparison_tabulation_fourteenth_2026_10_04.md | 1871 ++++++++++++++++++++
    ...rk_handoff_entry_two_hundred_and_seventy_six.md |  128 ++
parent of the fourteenth batch's Task 0: 57a4293e5356e5be9443ee8c119de1c73c280c81
```

### C.9 — A5 at the close: the staged close set (before this report was added) against the tip and the previous close

*Saved to scratch as `a5_close.txt`.*

```
--- staged close set (without the report) against the tip 2e17c3be's tree 9d0355218bce53c6f3f0da246add891ab0526e7a:
 STATUS.md                                |  2 +-
 STATUS_ARCHIVE.md                        |  4 +++
 tools/audit/defense_share.json           |  2 +-
 tools/audit/gen_status_batch_bound.py    | 52 +++++++++++++++++++++++++++++---
 tools/audit/guard_state.json             | 12 ++++----
 tools/audit/l2_outgoing_population.json  | 20 +++---------
 tools/audit/session_start_read_size.json | 16 +++++-----
 tools/audit/status_batch_bound.json      | 20 +++++++-----
 8 files changed, 85 insertions(+), 43 deletions(-)
--- the same staged tree against the previous close 5aa808b7's tree abd2bc901f0ced4ed9a11e9cda5ce3c404a6ab64 (everything this batch changed):
M	STATUS.md
M	STATUS_ARCHIVE.md
M	ratification_surfaces/cowork_comparison_l2_reading.md
A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifteenth_2026_10_04.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seventy_seven.md
M	tools/audit/defense_share.json
M	tools/audit/gen_status_batch_bound.py
M	tools/audit/guard_state.json
M	tools/audit/l2_outgoing_population.json
M	tools/audit/session_start_read_size.json
M	tools/audit/status_batch_bound.json
--- blobs in the staged tree:
d78ac530992860d38d1f605a77a2961d5440a2f6
c5ff83dcad2107ac8c05ead21724cbab0d9471fd
4c15b9338895e092c017223acaece9d8324db41d
f3edcfe810b96ec6bfde07af2ba213564c59add4
db340baf15f7fa3ad1ab29d067f12a47b4354ace
```
