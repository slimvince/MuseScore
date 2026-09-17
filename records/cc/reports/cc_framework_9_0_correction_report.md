# `FRAMEWORK.md` §9.0 and §11's R-6 — the ruled correction executed, the pack re-rendered (report, 2026-08-31)

> **STATUS: DONE.** Written by the CC run of `cc_instruction_framework_9_0_correction_2026_08_31.md`,
> executing **Ruling 8** (§3g) as scoped by **Ruling 18** (§3r) of
> `cowork_rulings_2026_08_31_decision_surface_sitting.md`.
>
> **★ THE HEADLINE.** The start state was established before anything rested on it: **`--check` is
> GREEN at the object**, and the three passages this dispatch quotes stand at the file **word for
> word**. The three corrections are made and **nothing else in that document moved** — proven blob to
> blob, with **every deleted line preserved verbatim beside its correction**, checked mechanically
> rather than by eye. The re-render matched the prediction **exactly**: member (7) is the only pack
> file that changed, the read-me and the other nine are byte-identical, and the two frozen packs'
> fourteen files re-hash to the blobs recorded before the act. **No STOP was met.**
>
> **★ AND THE PRESERVED WORDING IS PRESENT IN THE RENDERED MEMBER**, which is what Ruling 18(b)
> requires and what its absence would have falsified — verified at the rendered object, not at the
> tool's report of itself (#15).
>
> **★ THREE THINGS THIS BATCH DID NOT TOUCH ARE REPORTED RATHER THAN LEFT TO BE NOTICED**, one of
> them a divergence between a ruling's own locator and the file. See §6.

## 0. The boot, and the pins

The ordinary session-start read was performed in full before the named file was acted on — a
single-file opening instruction is not an exemption (ratified 2026-08-29, P-1): `CLAUDE.md`,
`DECISIONS.md`, `STATUS.md`, the derived gating answer at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`, then
`BUILD_AND_TEST.md` (conditionally mandatory, **condition MET** — this batch runs a Python tool),
then §3g and §3r of the ruling record whole, then `cc_l0l1_boot_pack_second_report.md` whole, then
this batch's dispatch.

**The pins, taken before any other act** (`git hash-object -w`), and **re-hashed at the close: all
eight non-target pins reproduce exactly. No read disagreed with its pin.**

| File | Pin | At the close |
|---|---|---|
| `CLAUDE.md` | `e012d3f2adc10e4557bf422236f0d50014559568` | unchanged |
| `DECISIONS.md` | `4f9e4d175131c601645be2034ae4d082ac094610` | unchanged |
| `STATUS.md` | `a9163ead8ade542c67cde43bf611e30477e0459b` | unchanged |
| `tools/audit/nongating_apparatus_rows.json` | `8df833a54ed5452971c213b1625848ebafa856aa` | unchanged |
| `BUILD_AND_TEST.md` | `42df316140c8bf178b620b461b84fadacb976299` | unchanged |
| `cowork_rulings_2026_08_31_decision_surface_sitting.md` | `f8ff38a118577b631075b3b9a9f8fe2a89186c0b` | unchanged |
| `cc_l0l1_boot_pack_second_report.md` | `7f4a5193dce8f675ed2aad9eb991273193c57e3d` | unchanged |
| `cc_instruction_framework_9_0_correction_2026_08_31.md` | `f49007b8d0cfe9db2045ead3bcee3b64e08daa3a` | unchanged |
| `FRAMEWORK.md` | `0b4a96dbc1ab8f94af3611010233c952d9b54e72` | `ec1febdb93e44d2f6aa0342de87672063842b74b` — this batch's own authorized edit |

**★ ONE PROPERTY ESTABLISHED WITH THE PINS RATHER THAN ASSUMED, because it decides what a pin is a
digest OF.** For each file both `git hash-object` and `git hash-object --no-filters` were taken.
**They agree for seven of the nine**, so those pins are digests of the bytes on disk. **They disagree
for `DECISIONS.md` and `tools/audit/nongating_apparatus_rows.json`**, which hold CRLF line endings the
clean filter normalizes — so for those two the table above records the `--no-filters` value, which is
the disk-byte digest, and the filtered values (`238cff78…` and `a2ca9f64…`) are recorded here so
neither is mistaken for a moved file. **`FRAMEWORK.md` agrees in both**, which is the one that
mattered: every hash of it in this report is a digest of the bytes on disk.

## 1. Task 1 — the start state, established before any assertion rested on it

**`--check` is GREEN, exit 0**, taken at the object at HEAD before this batch touched anything. Its
output is three lines: that the boot pack re-derives, and that each of the two spent subjects is
**FROZEN at its recorded blobs**. **The relayed claim of `cc_l0l1_boot_pack_second_report.md` is
therefore CONFIRMED, not corrected**, and the dispatch's STOP condition — red at Task 1 — did not
fire.

**The `l0-l1` pack's blobs, recorded per file before the act**, together with the manifest:

| Member | Blob before |
|---|---|
| `00_READ_THIS_FIRST.md` | `7e7339cf3250ac87337317ca109cf9645dd31b8d` |
| `01_the_phase_definitions.md` | `518b1e50d60af2b4e2ddcd8978623832eb071899` |
| `02_the_guiding_principles_and_the_conventions.md` | `00ffb0bede471f15d70de6cb7435a617b09caa58` |
| `03_the_writing_standards.md` | `518048459da6a865285a0f7c66c5d8f8045f0fc2` |
| `04_the_dispatch_protocol.md` | `02107d1ab37af197821edf3ca98ccf6f7ae5c0d3` |
| `05_the_ratified_design_intent.md` | `60563ab26e5c5c8827e32645b12eceaeb355933b` |
| `06_the_defect_type_catalog.md` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` |
| `07_the_charter_the_layers_and_the_decisions.md` | `b373880edf1a993111c10a77d78937c6071be7cf` |
| `08_the_five_research_extracts.md` | `54d0892b022107a8bd4cedc9e4bba54679a1ed41` |
| `09_the_empirical_findings_ledger.md` | `2bf845db798e91382236387e7f35fabf48b2ec07` |
| `tools/audit/derivation_boot_pack.json` | `4459695e5ed3769e1e2eafd23b70c23752258541` |

The two frozen packs' fourteen files were recorded the same way, so the freeze could be proven at the
close by re-hash rather than asserted from the tool's own report of itself.

**All three quoted passages stand at the file EXACTLY as this dispatch quotes them**, read at
`FRAMEWORK.md` itself: §9.0's heading, §9.0's closing sentence, and §11's R-6 — the last matching word
for word across a different line wrapping. **No mismatch, so no STOP.**

**One further thing was established rather than taken from the dispatch, because the corrected text
quotes it:** §0's glossary states, in its own words, that a factor *"is a means of computing a
decision, never a decision"*. It is quoted in the correction from that line and from nowhere else.
*(A second, earlier-stage glossary inside Appendix B words it "not a decision"; the live §0 is the one
quoted, and Appendix B is not in the pack member.)*

## 2. Task 2 — the three corrections, and nothing else

**(a) §9.0's heading** now states that the question is settled and what it is settled at, and cannot be
read as open:

> `### 9.0 The prior question: what is a unit? — SETTLED: a unit is a DECISION the analysis makes about the music`

**(b) §9.0's closing sentence** now records that the user ruled it on 2026-08-31, naming Ruling 8 of
`cowork_rulings_2026_08_31_decision_surface_sitting.md` as the record, and carries **the ruling's own
two operative statements and no more**: that a factor is not a unit, with §0's own words for why; and
that the factor roster and the terms that rate candidate readings stay inside L2's detail
specification, where §5's L2 charter and DP-P already place them. **Both cross-references were
resolved at the file before the sentence was written** — §5's L2 charter and DP-P both exist and both
say what the sentence says they say — so the correction introduces no dangling reference (DT-12).

**(c) §11's R-6** no longer lists §9.0 among the items awaiting a ruling. Its heading drops *"and one
is put to the user"*; the §9.0 clause is struck and the sentence before it closes with a full stop.
**DP-N, DP-O and DP-Q stand EXACTLY as they are, character for character, and so does the closing
sentence that none is filled with the most plausible reading** — the diff below shows their lines as
context, untouched.

**(d) The preservation, which is branch two's own requirement.** Each corrected statement carries its
FORMER WORDING in place, verbatim, marked **SUPERSEDED**, naming the date and the ruling. Two blocks:
one closing §9.0, carrying the former heading and the former closing sentence with their heading
marker and emphasis markers intact; one following R-6, carrying that risk row's whole former paragraph
with its own emphasis markers intact.

### ★ THE PROOF THAT NOTHING WAS LOST, TAKEN MECHANICALLY AND NOT BY EYE

The blob-to-blob difference `0b4a96db…` → `ec1febdb…` over a document of more than two thousand lines
is **three deleted regions and two added blocks, and nothing else**. Four lines were deleted in all:

| Deleted line | Still standing in the corrected sentence | Preserved beside it |
|---|---|---|
| §9.0's heading | `### 9.0 The prior question: what is a unit? —` and `SETTLED` | the whole line, verbatim |
| §9.0's closing sentence | — (replaced outright) | the whole sentence, verbatim, with its emphasis markers |
| R-6's first line | all but *"and one is put to the user"* | the whole former paragraph, verbatim |
| R-6's third line | `conditions stated.` and `**None is filled with` | the whole former paragraph, verbatim |

**This was checked by a driver, not by reading.** A scratchpad script — reading the two materialized
blobs outside this repository, never a repository path — took each deleted line from the *before* blob
by index, normalized whitespace on both sides, and required the line to occur in the *after* text.
**All four PRESERVED, plus R-6's whole four-line former paragraph re-assembled across its own wraps.
`ALL DELETED TEXT ACCOUNTED FOR`, exit 0.** The whitespace normalization is what lets a preserved
sentence be re-wrapped inside its block and still be proven word-identical; nothing else was relaxed.

**★ WHAT THE RULED EDIT DID NOT TOUCH, enumerated because the ruling closes the scope.** §9.0's three
candidate readings, its evidence paragraph and its *what the factor reading would change / what the
reconciliation reading would change* paragraph are **untouched, character for character** — they
appear in the diff only as unchanged context. No design point is reopened, no charter, no boundary
contract and no other section of `FRAMEWORK.md` is edited.

## 3. Task 3 — the re-render, against the prediction stated before the act

**The prediction (#17(b)), recorded before the generator was run:** only member (7) changes, because
only §9 moved and §11 is not in that member; the read-me and members (1)–(6), (8) and (9) re-render
byte-identically; the two frozen packs are not written at all; any other difference is a STOP.

**The measurement, by re-hash after the render:**

| | Result |
|---|---|
| `07_the_charter_the_layers_and_the_decisions.md` | `b373880e…` → **`a0513707886414a1c193a884e3f5f15ffd3f12f5`** — CHANGED |
| The read-me and members (1)–(6), (8), (9) | **byte-identical**, all nine reproducing their recorded blobs |
| `harmony-boundary`'s seven files | **byte-identical**, all seven reproducing their recorded blobs |
| `scoring-model`'s seven files | **byte-identical**, all seven reproducing their recorded blobs |
| `tools/audit/derivation_boot_pack.json` | `4459695e…` → `8ceed61767a7536354e1eaf57db1643b5aaf452f` — CHANGED, and inside this batch's footprint |

**The prediction held exactly. No other difference appeared, so no STOP.**

**That member (7) cannot contain R-6 was established at the tool, not inferred:** its authored spans
are §5 (to §6) and §9 (to §10), so §11 is outside the member by construction — which is why the
prediction could be made at all.

**What moved in the manifest, established by diffing the two manifest blobs:** exactly **three scalar
count fields**, all belonging to member (7) of the `l0-l1` subject — the §9 span's rendered line
count, the part's character count, and the member's character count. **No frozen digest moved, no
other subject moved, and no other field of any kind moved.** The values are in the manifest itself and
are not restated here (#17f, **D-431**).

### Verified at the rendered object, not at the tool's report of itself (#15)

- **The corrected heading is PRESENT** in the rendered member.
- **The corrected closing statement is PRESENT**, carrying the ruling, the date and the two operative
  statements.
- **The preserved former wording IS PRESENT** — the rendered member carries *"PUT TO THE USER, NOT
  SETTLED"* and *"It is not settled here"* verbatim inside a block marked SUPERSEDED. **This is the
  check Ruling 18(b) makes load-bearing: its absence would have meant a filter had reached it.** It
  did not.
- **The three ruled removal anchors remain ABSENT** from the rendered member, searched for by their
  exact anchor text and not found. The generator's own both-ways verification — what each filter
  removed is absent, and re-inserting it at its offsets reproduces the source byte for byte — is a
  STOP re-run on every render, and it passed.

**`--check` at the end state is GREEN, exit 0**, with both frozen subjects still verifying against
their recorded blobs.

## 4. The tracked-modification bound — ESTABLISHED this time, not declared

The preceding batch could only DECLARE this bound from the harness's session-start snapshot (#24).
**This batch established it**, through the sanctioned enumerator `tools/audit/changed_paths.py`, which
by construction can report a status code and a path and cannot return file content — so the answer
comes from a committed tool rather than from a forbidden shell read, and rests on no snapshot.

**Exactly four tracked modifications exist in the working tree:**

- `FRAMEWORK.md` — **this batch's own authorized edit**;
- `cowork_rulings_2026_08_31_decision_surface_sitting.md`, `tools/audit/gen_derivation_boot_pack.py`,
  `tools/audit/derivation_boot_pack.json` — the three the dispatch's §6 names by name.

**No other tracked modification, so the dispatch's STOP did not fire.** The `l0-l1` pack directory
appears as **untracked**, one record, which is git's own `--untracked-files=normal` behaviour for a new
directory; the two frozen pack directories **do not appear at all**, which is independent corroboration
that the freeze held.

*The one bound that remains, stated because a control believed to be in place and not in place is worse
than none:* this enumerator reports what git reports, so a path `.gitignore` hides is invisible to it —
the same blind spot every git-based answer has, and the tool says so of itself.

## 5. Done — against the dispatch's own clause

| The clause | The state |
|---|---|
| `--check` is GREEN | **Yes**, exit 0, at the end state, both frozen subjects verifying |
| The three corrections, with preserved former wording, and no other edit | **Yes**, proven blob to blob and by the mechanical preservation driver |
| Member (7) is the only changed pack file | **Yes**, by re-hash of all ten |
| The two frozen packs are byte-identical | **Yes**, by re-hash of all fourteen |
| Every STOP met is written up | **No STOP was met on any act of this batch** |

## 6. Three things this batch did NOT touch, reported rather than left to be noticed

**(a) THE MISSTATED METRIC-STRENGTH FIGURE'S THIRD INSTANCE IS UNTOUCHED — AND ITS LOCATOR DIVERGES
FROM THE FILE.** Ruling 18(c) leaves it OWED and unauthorized, and this batch did not edit it. **But
the ruling locates it at §14.1, and §14.1 does not carry it.** Read at the file, §14.1's bullet for
that source states only *"The metrical constraint on harmonic change, counted rather than assumed"* —
**no figure at all**, so nothing there can be a misstated one. The uncorrected numeric restatement
stands instead in **Appendix B, the sealed first-stage draft**, where the stage-one wording survives.
The three instances the record counts are therefore: §4's live clause, **corrected** on 2026-08-31
under Ruling 2; that correction's own preserved former wording, **marked superseded**; and Appendix B's
restatement, **uncorrected**. *This is stated as a finding about a locator, not as a criticism:*
nothing operational turns on it — the passage is unauthorized either way, and it is outside member (7)
either way, so it does not reach the derivation. **This batch amends no ruling record and takes no
verdict.**

**(b) FIVE FURTHER PASSAGES OF `FRAMEWORK.md` SAY §9.0 IS UNSETTLED, AND ALL FIVE ARE UNTOUCHED.** They
were enumerated before the edit, because a correction that leaves the same claim standing three
paragraphs away is not a correction. All five sit in dated records rather than in live text: **Appendix
A**, the stage-two amendment record, twice — its change list stating that the finding *"is unchanged and
is still put to the user"*, and its sizing record counting *"one put to the user"* among what that stage
produced — and **Appendix B**, the sealed first-stage draft, twice more, including that draft's own DP1.
*(A sixth textual match is unrelated: it records a different conflict that was put to the user and
ruled.)* **Ruling 8 closes its scope in terms — *"No other edit to `FRAMEWORK.md` is authorized"* — so
none was made.** Whether a dated appendix's present-tense sentence about a now-settled question is
branch-one filing (re-bannered, never rewritten) or something owed is **not adjudicated here**.

**(c) THE MANIFEST'S DESCRIPTION OF MEMBER (7)'s FILTER IS ONE BEHIND ITS FILTER.** The authored
`rendered_from` string still reads *"§5 and §9 whole, with two passages removed"* while the filter has
carried **three** since Ruling 17(b) widened it in the preceding batch. It is **not this batch's doing
and not in this batch's scope** — no tool source is edited — and it does **not** reach any rendered
member: the read-me's what-was-cut section is DERIVED from the counts and correctly says three
passages, as the preceding batch's report records. The falsity is confined to one authored string in
the manifest.

**★ THE SCOPE OF (b), STATED ON THE CLAIM ITSELF (DT-26).** That enumeration is complete for
`FRAMEWORK.md` and for nothing else. A tree-wide search, taken before this report existed, finds
**fifteen** files carrying the grain-of-a-unit phrasing. One is `FRAMEWORK.md` itself and one is the
pack's own rendered copy of §9, which is that document quoted; the remaining thirteen are dispatches,
dated reports, handoff entries, ruling records and ratification surfaces. **None was classified and
none was touched** — this batch amends no other governing document — and their number is recorded here
only so that the enumeration above is not read as an answer about the repository.

## 7. The close, on the ruled stop form

**WHAT WAS DONE.** The boot read in full; nine files pinned and re-hashed; `--check` established GREEN
at the object before and after; the three quoted passages confirmed word for word at the file; the
three ruled corrections made with both preservation blocks; the no-loss property proven mechanically;
the pack re-rendered against a prediction stated first, and the prediction met exactly; the rendered
member verified at the object for the correction, the preservation and the three absent anchors; the
frozen packs proven unmoved by re-hash; the tracked-modification bound established rather than
declared; three untouched items reported, one of them a divergence between a ruling's locator and the
file.

**WHAT WAS NOT DONE.** No build, no test, no golden, no measurement of the analysis; nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`. **No other governing document amended** and
no other section of `FRAMEWORK.md` edited. **No open-items row created, flipped or discarded. No
decisions-register entry and no `D-NNN` allocated** — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route. **No tool source edited at all** — the
forward bound's own per-batch re-aiming was not needed and was not run, so even its named carve-out went
unused. The workbook was not opened; no score was staged; no brief was written; no session was booted.
**Nothing was written into either frozen pack directory.**

**THE REMAINDER IS UNTOUCHED.** §14.1 and Appendix B's metric-strength restatement, the five §9.0-status
passages in the two appendices, the fourteen other files carrying that phrasing, and the manifest's
`rendered_from` string all stand exactly as this batch found them.

## The footprint, as it actually stands

**Edited:** `FRAMEWORK.md` — the three corrections of §2 and nothing else. **Regenerated:**
`tools/audit/derivation_boot_pack/l0-l1/07_the_charter_the_layers_and_the_decisions.md` and
`tools/audit/derivation_boot_pack.json`. **Created:** this report.

## The self-check

**The diff was read on disk, blob to blob by explicit hash, not from the memory of writing it.** It is
the three regions of §2 and the two preservation blocks; every other line of a two-thousand-line
document appears as unchanged context.

**#1 / #2** — nothing is built and nothing is claimed from research; the one quotation the corrected
sentence carries was read at §0 rather than recalled. **#6** — the ruling is stated once, at the
statements it corrects, and pointed at from the risk row rather than copied into it; no third home was
made. **#12** — this is the principle the whole act turns on: every deleted line stands preserved,
verbatim, marked superseded, with its date and its ruling, and the proof is a driver rather than a
reading. **#13** — the locator divergence at §14.1 was surfaced the moment it was found, before the
report was drafted around it, and no verdict was built on top of it. **#15** — the correction, the
preservation and the three absent anchors were checked at the rendered object; the freeze at the files
by re-hash; the tracked-modification bound at a committed enumerator. **#17(b)** — the re-render's
expected difference was stated before the act and met exactly. **#17(f) / D-431** — no figure of this
project's own measurement enters this report; the manifest's three moved counts are named by field and
left at the manifest. The blob hashes here are identities, not measurements, and the dispatch orders
them reported. **#19** — the start state was established at the object rather than relayed, which is
the fix the preceding batch's first writing lacked; and the preservation claim is measured, not
asserted. **#24 / D-253** — working-tree content was read only through the file tools; the shell was
used for `git hash-object`, for `git cat-file` by explicit hash, for the generator, for the sanctioned
path enumerator and for one scratchpad driver whose inputs are outside this repository. Two shell
attempts were refused by the guard — one interpreter read naming a repository path, one working-tree
`git diff` — and **both were abandoned rather than reworded**, the answers taken through the file tools
and through blobs by explicit hash instead. **D-307** — the corrected text cites §0, §5, DP-P and the
two rulings by section, never by line number. **Conventions** — American English; no self-invented
label, abbreviation or numbering; the reserved music-theory words were checked one by one against the
added text and none is used in a non-musical sense. **`DEFECT_TYPES.md`** — **DT-12**, both new
cross-references resolved at the file before being written; **DT-26**, the §9.0 enumeration's scope is
stated on the claim itself and the tree-wide count published beside it, so a sweep complete inside one
file is not read as complete about the repository.

**One bound on this report.** The preservation proof normalizes whitespace, so it establishes that
every deleted line's *words* survive in order, not that its original line wrapping does. That is the
right test for a preserved sentence re-wrapped inside a block, and it is stated so the proof is not
read as stronger than it is.

---

*Provenance: CC, 2026-08-31, under `cc_instruction_framework_9_0_correction_2026_08_31.md`, executing
Ruling 8 as scoped by Ruling 18 of `cowork_rulings_2026_08_31_decision_surface_sitting.md`. Every
working-tree read through the file tools. Shell used only for `git hash-object`, for `git cat-file` by
explicit hash, for running the boot-pack generator and the sanctioned path enumerator, and for one
scratchpad driver reading materialized blobs outside this repository. No figure of this project's own
measurement is restated (#17f, D-431).*
