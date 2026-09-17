# The staggered-entries exemplar — decoded, whole-staff-checked, named and provenanced (report, 2026-09-01)

> **STATUS: COMPLETE.** Executes `cc_instruction_exemplar_decode_2026_09_01.md` whole.
>
> **★ THE OUTCOME IN ONE SENTENCE. Condition (i) is MET — no staff pair is identical over the whole
> staff, all 36 diverge — so the fallback did NOT fire; condition (ii) is MET — the copyright metaTag
> says CC0, the file is written byte-identical to the extraction and proven so, and the provenance
> record carries all nine items.**
>
> **★ THE ONE FINDING THAT MATTERS BEYOND THIS BATCH, STATED FIRST.** The 24-chord window the
> previous batch tested would not have separated **any** of the three flagged pairs: they first
> diverge at pitch **126**, **95** and **401**. **A window would have had to run past 401 chords to
> catch the last of them** — so Ruling 19's condition (i) was not a formality, and the reading that a
> window suffices is refuted by the object.
>
> **★ AND WHAT THIS BATCH DID NOT DO. IT STAGES NOTHING.** No brief was written, no boot pack was
> rendered, no session was booted. The Frescobaldi fallback file was not touched.

---

## 0. Boot — performed

The ordinary session-start read was performed in full before any other act; a single-file opening
instruction is not an exemption (ratified 2026-08-29, P-1).

1. `CLAUDE.md` whole; `DECISIONS.md` whole (all 862 lines, preamble and index); `STATUS.md` whole;
   the derived gating answer at `tools/audit/nongating_apparatus_rows.json` →
   `★_the_live_gating_answer` → `gating_ids`.
2. `BUILD_AND_TEST.md` — **condition NOT met and it was not read.** This batch built nothing, ran no
   test, and ran no measurement of the analysis. No step tempted toward a build.
3. `docs/score_inventory.md` — **whole.** Hard rules 2 and 3 bind this batch by name and both are
   honored: no snapshot source and no pin was touched, and `"tools/extra scores"` was quoted in
   every command that names it.
4. `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3o (Ruling 15), §3u, §3v and §3w
   (Ruling 19) — each read whole.
5. `cc_mscz_container_establishment_report.md` — whole.
6. This batch's dispatch, whole.

---

## 1. Task 0 — the pins

Pinned with `git hash-object -w` before any other act, and **re-verified at the close. Every pin
reproduced exactly; no read disagreed with its pin**, so that STOP was not met.

| File | Pin (blob sha1) | Re-verified at close |
|---|---|---|
| `CLAUDE.md` | `e012d3f2adc10e4557bf422236f0d50014559568` | identical |
| `DECISIONS.md` | `238cff78e61d4ff4cd8e5a41dc17f6fab4ab7d59` | identical |
| `STATUS.md` | `a9163ead8ade542c67cde43bf611e30477e0459b` | identical |
| `tools/audit/nongating_apparatus_rows.json` | `a2ca9f64783d45a50bd3fb299d46afe46b9fe678` | identical |
| `BUILD_AND_TEST.md` | `42df316140c8bf178b620b461b84fadacb976299` | identical |
| `docs/score_inventory.md` | `4de7d6986614d876796bc75aed473c6ce3bf92c4` | identical |
| `cowork_rulings_2026_08_31_decision_surface_sitting.md` | `70fc8e6d51554e2fc33ffede2d7406ad1b03ac47` | identical |
| `cc_mscz_container_establishment_report.md` | `7938580a0142f59131c45de0a7df1a52e228e07b` | identical |
| `cc_instruction_exemplar_decode_2026_09_01.md` | `a2f4ffc1bb268909908a3ffbc6c411ea5ca7382e` | identical |

**Two pins differ from the previous batch's, and both are expected rather than a STOP.** The sitting
record moved `a7481ab1…` → `70fc8e6d…`, having since gained §3v, §3w and §3x — which the dispatch's
§7 names in terms. The container report moved because the previous batch created it after taking its
own pins. **The STOP is a read disagreeing with its OWN pin inside this batch, and none did.**

## 1a. Task 1 — the start state, established BEFORE anything rested on it

### The source archive is the object the previous batch measured

| | Required by §1 | Measured this batch | Match |
|---|---|---|---|
| Byte size | 75,260 | **75,260** | yes |
| `sha256` | `56e2241707caea88e24ec9ab9ae0e5ff9f26dffabfd7638badda8df6acf89cfb` | **identical** | yes |

Its mtime is `2026-07-28 10:47:00.027952900 +0200`, which reproduces the previous batch's record to
the digit. **The file has not moved. The STOP was not met.**

### The tracked-modification shape

**Exactly four tracked-and-modified paths, and no others:**

```
 M	FRAMEWORK.md
 M	cowork_rulings_2026_08_31_decision_surface_sitting.md
 M	tools/audit/derivation_boot_pack.json
 M	tools/audit/gen_derivation_boot_pack.py
```

**All four are the four §7 names, in the same order. There is no OTHER tracked modification, so the
§7 STOP was not met.** 866 changed-path records in total at the start: 4 tracked-modified and 862
untracked.

**★ THE SHELL-READ GUARD REFUSED `git status --porcelain`, EXACTLY AS THE DISPATCH ANTICIPATES, AND
THE REFUSAL IS REPORTED RATHER THAN WORKED AROUND.** The guard's own message named **D-253** and its
sanctioned substitute, `python tools/audit/changed_paths.py`, which reports paths and status codes
and cannot return file content. That substitute was used and the shape above is its output. **The
guard chose the route, not this session's judgment.**

**A second guard refusal, reported for the same reason.** An `ls` aimed at the destination path was
refused under the same rule — existence goes through the file tools. The destination's absence was
then established by the file tools instead, below.

### The destination did not already exist

Established three ways before anything was written:

- **Glob `tools/audit/derivation_exemplars/**` → no files.** The same pattern over the sibling
  `tools/audit/derivation_boot_pack/**` returns 24 files, so the pattern resolves.
- **Glob `**/bwv1049_03_presto*` → no files** anywhere in the tree, so neither destination file
  existed under any path.
- **A directory test on `tools/audit/derivation_exemplars` reported it ABSENT**, which settles the
  one case a file glob cannot see, an existing but empty directory.

**Confirmed a fourth time by the act itself:** the directories were created with `mkdir` and **not**
`mkdir -p`, so an already-existing directory would have failed the command. Both levels returned 0.
**The STOP was not met.**

### The line-ending hazard, established at `.gitattributes` before any file was written

Read at the object. The file carries `*               text=auto` as its first rule, marks
`*.mscz          binary`, and **carries no rule for `*.mscx` anywhere in its 31 lines.** Its own
comment, quoted verbatim, reads:

> `# Binary MuseScore scores (.mscz is a ZIP container) must NEVER be line-ending`
> `# normalised — the default `* text=auto` above would corrupt the zip on a CRLF`
> `# checkout (the OI-195 / OI-34 line-ending-normalisation class). Marked binary so`
> `# git stores and checks them out byte-for-byte. (.mscx is uncompressed XML and is`
> `# left under text=auto by design — only the committed .mscz set needs this.)`

**So a committed `.mscx` IS subject to line-ending normalization — the OI-195 / OI-34 class the same
file names.** The wording is confirmed at the object and reported. **`.gitattributes` was NOT
edited**, and §5 leaves the question owed.

---

## 2. Task 2 — extraction, and the plainness and provenance facts re-established at the file

**Absolute scratch path, outside the repository working tree:**

```
C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\6b4face2-78a8-4be4-9973-475402b45381\scratchpad\exemplar_decode
```

That is the OS temp directory. It is not under the repository, not a gitignored path under it, and
not tracked anywhere within it. **The STOP "extraction writing anywhere under the repository working
tree" was not met.**

**Re-established at the extracted file, not at the previous report (#15). Every value the dispatch
relays is confirmed; none diverges.**

| Fact | Previously reported | Measured this batch | Verdict |
|---|---|---|---|
| the single `.mscx` member's name | `temp_10111.mscx` | `temp_10111.mscx` | **confirmed** |
| its uncompressed byte length | 1,701,770 | archive records **1,701,770**; extraction is **1,701,770** | **confirmed, and equal** |
| its `sha256` | `a4d9d897…fbac80` | `a4d9d89798469f654e120e08884c4c6e3c47c2842e2b2fccc53ec9db87fbac80` | **confirmed** |
| `<Harmony>` / `<FiguredBass>` / `<StaffText>` | 0 / 0 / 0 | **0 / 0 / 0** | **confirmed** |
| part-list and body `<Staff id="N">` sections | 9 and 9 | **9 and 9**, ids 1–9 in both | **confirmed** |
| `<museScore version>` / `<programVersion>` | `3.01` / `3.0.0` | **`3.01` / `3.0.0`** | **confirmed** |

The archive's member listing also reproduces exactly: three members, all `Defl:N`, the score member
carrying CRC-32 `6c222647`; `unzip -t` reported **"No errors detected in compressed data"** over all
three, so every stored CRC verifies against its decompressed bytes.

**The 18 `<trackName>` and 9 `<instrumentId>` values reproduce the previous report's lists in the
same order**, which is what fixes the staff-to-part correspondence used in §3: staff 1 Violino
principale, 2 Flauto 1, 3 Flauto 2, 4 Violino 1, 5 Violino 2, 6 Viola, 7 Violoncello, 8 Violone,
9 Continuo (Harpsichord). **The nine part-list `<Staff>` ids are 1…9 in part order**, which is what
makes that correspondence a read rather than an inference.

**★ §3v's THIRD CHECK QUESTION — *whose file is it?* — CONFIRMED AT THE FILE.** The head of
`temp_10111.mscx` reads `<museScore version="3.01">`, `<programVersion>3.0.0</programVersion>`,
`<programRevision>c1a5e4c</programRevision>`. **`version.cmake` sets `MUSE_APP_VERSION_MAJOR "5"`,
`MUSE_APP_VERSION_MINOR "0"` and `MUSE_APP_VERSION_PATCH "0"`, read at the object this session** —
so `3.0.0` is two major versions before what this repository builds, and **the file cannot be this
build's output.**

**One fact the dispatch's table did not ask for and this batch reports as an addition, not a
divergence:** the declared `programRevision` is `c1a5e4c`, **which has the shape of a revision hash
and is NOT the `abc123456` placeholder §3v found in the ABC archive.** It strengthens the
exoneration rather than qualifying it.

---

## 3. Task 3 — CONDITION (i), the whole-staff check

**Method, stated so the result can be challenged.** For **every** body staff, the ordered sequence of
`<pitch>` values over the **whole** staff — every `<Chord>` in document order, every `<pitch>` child
in file order — then **all 36 pairs** compared position by position. A grace-note chord, being its
own `<Chord>` element, counts as a chord, which is the previous batch's stated method unchanged.

**The enumeration reconciles, so the verdict is about every chord and not a sample:** the nine
staves' chord counts sum to **6,361**, which is exactly the whole-file `<Chord>` count, and the
whole-file `<pitch>` count is also **6,361** — so every chord holds exactly one pitch, every chord
lies inside a body staff, and no chord was left out of a sequence (DT-26).

### **THE VERDICT: NO PAIR IS IDENTICAL OVER THE WHOLE STAFF. ALL 36 DIVERGE. CONDITION (i) IS MET.**

**The three pairs the window flagged:**

| Pair | Parts | Chords / pitches, each staff | Identical over the whole staff | First divergence, index | The two values there | Positions agreeing, over the shorter staff |
|---|---|---|---|---:|---|---|
| **1 ↔ 4** | Violino principale / Violino 1 | 1,345 / 1,345 · 564 / 564 | **No** | **126** | 74 against 76 | 161 of 564 — **28.5 %** |
| **2 ↔ 3** | Flauto 1 / Flauto 2 | 604 / 604 · 596 / 596 | **No** | **95** | 74 against 78 | 164 of 596 — **27.5 %** |
| **7 ↔ 9** | Violoncello / Continuo | 671 / 671 · 690 / 690 | **No** | **401** | 50 against 52 | 421 of 671 — **62.7 %** |

**And the one-line verdict for every other pair: none matches over the whole staff either.** All 33
remaining pairs diverge at index 0 — the very first pitch. Their per-pair first-divergence values and
agreement proportions are carried in full in the provenance record beside the score file, and are not
restated here (#6).

**The nine staves' totals**, since a length difference alone already refutes identity for several
pairs: staff 1 1,345 · staff 2 604 · staff 3 596 · staff 4 564 · staff 5 775 · staff 6 636 ·
staff 7 671 · staff 8 480 · staff 9 690.

### The written prediction, marked

**§3's prediction — "all three pairs DIVERGE" — HELD, in all three parts.**

**But the reading offered as its ground is NOT thereby established, and this batch does not upgrade
it.** The dispatch stated the ground itself: *"The reading is this side's and is not evidence; the
sequences are."* What the sequences show is that the three pairs separate, at indices 126, 95 and
401. **Whether the agreeing stretches are concerto-grosso doublings, imitation at the unison, or
something else is not established here and no such reading is asserted** — in the report or in the
provenance record.

**★ AND THE FINDING THE PREDICTION DID NOT REACH, WHICH IS THE REASON CONDITION (i) EARNED ITS
PLACE.** The tested window was **24 chords**. The three flagged pairs first diverge at **126, 95 and
401**. **Every one of those lies beyond the window, and the last lies beyond it by more than
sixteen-fold.** So the window's result was not merely incomplete — **no window shorter than 402
chords would have separated pair 7 ↔ 9**, and the previous batch's care in reporting *matches over
the tested window* rather than *duplicate* is vindicated at the object.

---

## 4. Task 4 — CONDITION (ii): the license, the write, the digests

### (a) The license, checked at the file BEFORE anything entered the repository

Read in the extracted `.mscx`, quoted in full:

```
<metaTag name="copyright">OpenScore (CC0)</metaTag>
```

**It says CC0.** It matches `tools/extra_scores_registry.json`'s recorded
`"license_metaTag_raw": "OpenScore (CC0)"` and `"license": "CC0"` for this path exactly. **The STOP
"the licence metaTag not saying CC0, or empty" was not met**, and the write proceeded.

### (b) The destination, as the dispatch declares it

```
tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md
```

**Both paths are the writing side's declared choices**, recorded as such in the provenance record's
§8 and stated there to be the user's to overturn. This batch took neither choice and invented no
name of its own.

### (c) The write, and the measurement that keeps its claim honest

The extracted file was copied **byte-for-byte** — no re-encoding, no re-formatting, no line-ending
conversion.

| | `sha256` | Bytes |
|---|---|---:|
| As extracted, in the scratch directory | `a4d9d89798469f654e120e08884c4c6e3c47c2842e2b2fccc53ec9db87fbac80` | 1,701,770 |
| As it now stands on disk in the repository | `a4d9d89798469f654e120e08884c4c6e3c47c2842e2b2fccc53ec9db87fbac80` | 1,701,770 |

**The two digests are equal. The STOP was not met — nothing normalized the file on the way in**, and
the provenance record's claim that no byte was altered is therefore true of the object as it stands.
The file carries 64,500 line feeds and **zero carriage returns**.

**Reported without acting on it, as §4(c) requires:** `.gitattributes` leaves `.mscx` under
`text=auto`, so a later checkout on a CRLF platform may alter this file's line endings. **The file
was NOT edited and no ignore rule was added.** Two related facts, established rather than assumed:
the new path is **not** matched by any ignore rule (`git check-ignore` exits 1 on it, and the
changed-path enumeration reports the directory as `??` untracked rather than ignored), so the file
will be tracked when it is added.

### (d) The provenance record

Written at `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md`, carrying all
nine items §4(d) enumerates: the source archive's path, size and `sha256`; the member name and its
recorded length; that the file arrived by container extraction with no byte altered, the proof stated
as extracted-length-equals-recorded-length plus the verified stored CRC-32, with both digests beside
each other; the declared `<museScore version>` and `<programVersion>` with the plain statement that
`3.0.0` predates this repository's `5.0.0`; the license metaTag quoted; the three annotation counts,
all 0; **condition (i)'s result in full, all 36 pairs with the three flagged pairs' first-divergence
indices**; that the naming and the directory are the writing side's choices under Ruling 19 condition
(ii), with the `.gitattributes` caveat; and the authority, Ruling 19 (§3w).

**No figure of this project's own analysis measurement appears in it (#17f, D-431).** Every number in
it is a property of the score file, established at that file in this session.

---

## 5. Divergences and observations — reported rather than resolved

**None of these is a STOP, and none changes this batch's outcome.**

1. **★ A CHECKABLE CLAIM OF §3v IS FALSE AT THE REGISTRY, IN BOTH HALVES.** §3v states that *"both
   archives' registry rows carry a musescore.com `source` URL and a CC0 licence read from the file's
   own copyright metaTag."* Read at `tools/extra_scores_registry.json`:

   | Archive | `source` | `license` | `license_metaTag_raw` |
   |---|---|---|---|
   | Brandenburg (this batch's) | **empty string** | `CC0` | `OpenScore (CC0)` |
   | Haydn | `http://musescore.com/user/30859765/scores/5452080` | **`undetermined`** | **`(1761?)`** |

   **Neither row carries both.** Brandenburg has the CC0 licence and no source URL; Haydn has the
   source URL and a licence the registry itself records as undetermined from a bare date — which is
   the case `docs/score_inventory.md` describes for the eleven rows whose tag is empty or a bare
   date. **This does not disturb this batch's licence check, which was run at the FILE and passed**;
   what it disturbs is one supporting sentence of §3v's exoneration. It is reported, not repaired —
   the record is the writing side's.

2. **The archive's `<programRevision>` is `c1a5e4c`**, which the dispatch's table did not ask for.
   An addition to what §3v established, not a divergence from it.

3. **The shell-read guard refused `git status --porcelain`** and separately refused an `ls` at a
   repository path; both refusals were taken as routing and the sanctioned substitutes used. §1a.

4. **No divergence from the previous report's figures was found.** Every value of the dispatch's §2
   table reproduced exactly, and so did every row of the 24-chord window and both naming lists.

---

## 6. STOPs

**No STOP of §6 was met.** Taken in the order §6 lists them:

| STOP | Met? |
|---|---|
| The source archive's size or `sha256` not matching §1 | **No** — 75,260 and `56e22417…` both reproduced, mtime too |
| The destination directory or either destination file already existing | **No** — established absent four ways, including by a non-`-p` `mkdir` that would have failed |
| The licence metaTag not saying CC0, or empty | **No** — it reads `OpenScore (CC0)` |
| **Any staff pair identical over the whole staff** | **No** — all 36 pairs diverge; condition (i) MET |
| The on-disk `sha256` differing from the extracted `sha256` | **No** — both `a4d9d897…fbac80` |
| Extraction writing anywhere under the repository working tree | **No** — the scratch path is under the OS temp directory |
| A read disagreeing with its pin | **No** — all nine pins reproduced at the close |
| Any act outside §7 | **No** — see the footprint below |

**The "not a STOP, reported rather than resolved" cases:**

| Case | Occurred? |
|---|---|
| Any divergence from the previous report's figures | **No** — every relayed value reproduced |
| The prediction of §3 falsified | **No** — it HELD in all three parts; its stated ground is separately noted as a reading and is not upgraded |
| The shell-read guard refusing a command | **Yes, twice** — reported at §1a and §5.3 |

**Because condition (i) is MET, Ruling 19's fallback did NOT fire.** The Frescobaldi file
`tools/dcml/frescobaldi_fiori_musicali/MS3/12.15_Recercar_dopo_il_Credo.mscx` was **not staged, not
copied and not touched**, and this batch did not open it.

---

## 7. The footprint, as executed

**Created — three objects and nothing else:**

- `tools/audit/derivation_exemplars/` and `tools/audit/derivation_exemplars/l0-l1/`
- `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`
- `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md`
- this report

**Edited: NOTHING.** **`.gitattributes` was NOT edited. No `.gitignore` rule was added.** No score
anywhere was edited, renamed, moved, converted or re-saved — **the source `.mscz` was read only, and
its `sha256`, size and mtime at the close are identical to its start state.** No registry, manifest
or pin was touched; **`tools/snapshot_sources_manifest.json` and the eleven snapshot sources are
untouched (Hard rule 2)**; `tools/extra_scores_registry.json` was **READ only** and gained no row. No
tool source was edited.

**Not done at all:** no build, no test, no golden, no measurement of the analysis, nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; **no boot pack rendered and neither frozen
pack opened**; **no governing document amended** — including `docs/score_inventory.md`, which this
batch read and did not touch; **no open-items row created, flipped or discarded**; **no
decisions-register entry and no `D-NNN` allocated** — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route; the workbook was not opened; **NO
SCORE STAGED**; **the Frescobaldi fallback file not touched**; no brief written; no session booted.

**The tracked-modification shape at the close is identical to the start state** — the same four
tracked-and-modified paths, and no fifth. Measured three times: **866 records at the start, 867 after
the two files were written, 868 after this report existed.** The two added records are
`?? tools/audit/derivation_exemplars/` — git reporting an untracked directory as a single record,
which is why two new files add one — and `?? cc_exemplar_decode_report_2026_09_01.md`. **This batch
modified nothing tracked, and created nothing untracked inside the repository except the two files
§4(b) names and this report.**

**Hard rule 3 was honored in every command** that names `"tools/extra scores/…"` — the two digest and
size passes, the `unzip -v`, the `unzip -t` and the `unzip -j`.

**The scratch material** — the extracted `.mscx`, the two analysis scripts, the result file and the
two changed-path enumerations — lives under the OS temp path named in §2 and is outside the
repository.

---

## 8. The standing self-check

Run before this report was written, on the work actually on disk rather than on the intention.

**The diff on disk, read rather than remembered.** Two files are new inside the repository. The
`.mscx` is a byte-for-byte copy whose digest was taken **after** it landed and equals the
extraction's — so its diff is exactly the extracted member and nothing else. The provenance record
was re-read on disk after writing and **three defects were found in it and corrected there**, which
is the check working rather than a formality:

- **American English (Conventions).** `normalised` → `normalized` twice, and `licence` → `license` in
  a heading. **The `.gitattributes` comment quoted inside it keeps its own British spelling, being a
  verbatim quote.**
- **The reserved-word convention (D-113).** The record's closing sentence used bare *note* in the
  annotation sense; bare *note* is a pitch event. Rewritten to *record*. **The file name
  `bwv1049_03_presto.provenance.md` is the dispatch's own and was not changed** — and the collided
  word does not appear in it.
- **Predicate qualification and an over-broad claim.** *"It establishes that no staff is a copy of
  another"* claimed more than the test performs — the test compares ordered pitch sequences and says
  nothing about rhythm. Narrowed to exactly what was run. In the same pass, *"a real defect found
  elsewhere in this repository's corpora"* was asserting at second hand a fact this batch did not
  establish; it now cites §3u as the record that establishes it.

**Against the principles.** **#15** — every claim is verified at the object: the pins at the blobs,
the sizes and digests at the files, the member list and CRCs at the archive, the counts and sequences
at the parsed XML, `MUSE_APP_VERSION` at `version.cmake`, the licence at the metaTag, the
line-ending rule at `.gitattributes`, the registry fields at the registry. **#17(f) / D-431** — no
figure of this project's own analysis measurement is restated, in the report or in the provenance
record. **#19** — the byte-identity of the write is *positively* established by a digest taken after
the file landed, not inferred from the copy having succeeded; and the destination's prior absence is
established by four independent routes rather than by one that could fail silently. **#18** — no
causal claim is made about what produced the archive, and the reading that the agreeing stretches are
doublings is explicitly NOT asserted. **#12** — the prediction is marked at its own terms and its
ground is separated from its claim; the whole 36-pair result is carried, not the three flagged pairs
alone. **#13** — the window-versus-whole-staff finding, and the false §3v registry claim, are both
surfaced rather than absorbed. **#6** — the 33 unflagged pairs' detail lives in the provenance record
only, and this report points at it rather than keeping a second copy.

**Against `DEFECT_TYPES.md`.** **DT-26 (scope-assumed enumeration)** is the live risk in this batch
and is met head-on: the per-staff chord counts **reconcile arithmetically** against the whole-file
element counts (1,345 + 604 + 596 + 564 + 775 + 636 + 671 + 480 + 690 = **6,361** = the file's
`<Chord>` total = its `<pitch>` total), so the "no pair is identical" verdict is a statement about
every chord in the file and not about a window — which is precisely the defect the previous batch's
24-chord scope would have carried had its result been read as a verdict. **DT-11 (hand-transcribed
figure)** — every number here is a command's output in this session, and both new files' digests were
taken from the objects. **DT-23 (silent-failure path)** — the analysis script carries no bare
`except`; an XML parse failure or a missing element would have raised, and none did. **DT-12 (stale
anchor)** — every document and file this report cites was opened in this session.

**One thing this report does NOT claim.** That the Brandenburg file should be staged, or that the
passages where two of its staves agree are doublings. **Condition (i) is met and condition (ii) is
met; nothing is staged.** What follows is the user's.

---

*Provenance: executed by Claude Code, 2026-09-01, against `cc_instruction_exemplar_decode_2026_09_01.md`
(pin `a2f4ffc1bb268909908a3ffbc6c411ea5ca7382e`), which executes **Ruling 19 (§3w)** of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`. Every fact above was established at the
object in this session; the dispatch's relayed figures were re-established at the extracted file and
none diverged. The scratch directory used was
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\6b4face2-78a8-4be4-9973-475402b45381\scratchpad\exemplar_decode`.*
