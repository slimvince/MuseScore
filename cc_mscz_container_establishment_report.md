# The `.mscz` container, and the plainness of three candidate scores — Ruling 15's constraint (iii), established (report, 2026-09-01)

> **STATUS: COMPLETE.** Executes `cc_instruction_mscz_container_establishment_2026_09_01.md` whole.
> **This report reports facts about files.** It selects no score, stages nothing, promises nothing,
> and wrote no decoded copy into the repository. **Nothing in the repository was edited.**
>
> **★ THE ONE THING THE BATCH FOUND THAT THE DISPATCH DID NOT ANTICIPATE, STATED FIRST.** The
> losslessness test of §3(a) compares two files that are **different MuseScore format versions** —
> the sibling on disk is format `3.02` (`programVersion 3.6.2`), the `.mscx` inside the archive is
> format `5.00` (`programVersion 5.0.0`). **So that comparison does not measure what zipping costs;
> it measures a format migration.** The container's own losslessness is established separately and
> cleanly, below. Surfaced here rather than built around (#13).

---

## 0. Boot — performed

The ordinary session-start read was performed in full before any other act, the single-file opening
instruction being no exemption (ratified 2026-08-29, P-1):

1. `CLAUDE.md` whole; `DECISIONS.md` whole (all 862 lines, both index and preamble);
   `STATUS.md` whole; the derived gating answer at
   `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`.
2. `BUILD_AND_TEST.md` — **condition NOT met and it was not read.** This batch built nothing, ran no
   test, and ran no measurement of the analysis. No step tempted toward a build.
3. `docs/score_inventory.md` — **whole.** Hard rules 2 and 3 bind this batch by name and both are
   honoured: no snapshot source or pin was touched, and `"tools/extra scores"` was quoted in every
   command in which it appears.
4. `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3l (Ruling 12), §3o (Ruling 15) and §3u —
   each read whole.
5. This batch's dispatch, whole.

---

## 1. Task 0 — the pins

Pinned with `git hash-object -w` before any other act, and **re-verified at the close**. Every pin
reproduced exactly; **no read disagreed with its pin**, so the §6 STOP was not met.

| File | Pin (blob sha1) | Re-verified at close |
|---|---|---|
| `CLAUDE.md` | `e012d3f2adc10e4557bf422236f0d50014559568` | identical |
| `DECISIONS.md` | `238cff78e61d4ff4cd8e5a41dc17f6fab4ab7d59` | identical |
| `STATUS.md` | `a9163ead8ade542c67cde43bf611e30477e0459b` | identical |
| `tools/audit/nongating_apparatus_rows.json` | `a2ca9f64783d45a50bd3fb299d46afe46b9fe678` | identical |
| `BUILD_AND_TEST.md` | `42df316140c8bf178b620b461b84fadacb976299` | identical |
| `docs/score_inventory.md` | `4de7d6986614d876796bc75aed473c6ce3bf92c4` | identical |
| `cowork_rulings_2026_08_31_decision_surface_sitting.md` | `a7481ab12a2c27c57e9e990c9d43bae770fe2025` | identical |
| `cc_instruction_mscz_container_establishment_2026_09_01.md` | `8c2689364cd85e61fcdebd84742dc4c40df4ce01` | identical |

*(`git hash-object` emitted its ordinary CRLF normalisation warning on the seven text files. That is
a note about how git would store the blob, not about the file on disk; the pin is stable, which is
what the mechanism is for — every hash reproduced at the close.)*

## 1a. Task 1 — the four input files, established BEFORE anything rested on them

All four exist at the paths the dispatch names. **Every size matches the dispatch's table exactly**,
so no file moved since the dispatch was written and every count below is about the objects the
dispatch meant.

| Path | Bytes this batch measured | Dispatch's table | Match |
|---|---:|---:|---|
| `"tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz"` | 75,260 | 75,260 | yes |
| `"tools/extra scores/large/haydn-symphony-no-6.mscz"` | 127,386 | 127,386 | yes |
| `tools/dcml/ABC/MS3/n01op18-1_01.mscz` | 430,695 | 430,695 | yes |
| `tools/dcml/ABC/MS3/n01op18-1_01.mscx` | 2,050,969 | 2,050,969 | yes |

**The `sha256` / size / mtime record that replaces the pin for these four untracked files:**

| Path | sha256 | size | mtime |
|---|---|---:|---|
| `"…/large/bach-brandenburg-…-presto.mscz"` | `56e2241707caea88e24ec9ab9ae0e5ff9f26dffabfd7638badda8df6acf89cfb` | 75,260 | 2026-07-28 10:47:00.027952900 +0200 |
| `"…/large/haydn-symphony-no-6.mscz"` | `4ba5c99070386541cbfd9fe77fd55f77df05b26fe614367c7a042d1e11f6dffd` | 127,386 | 2026-07-28 10:51:49.173893000 +0200 |
| `tools/dcml/ABC/MS3/n01op18-1_01.mscz` | `727f230e8d3216d0263cb548bc4b5c5876363fa8186b844950068b76bd5d6946` | 430,695 | 2026-04-15 15:41:35.825071400 +0200 |
| `tools/dcml/ABC/MS3/n01op18-1_01.mscx` | `a4ccf07d2fd30b9059363fb0f8e0e7ca2bde50cea9b81dffb0c8397f663d98a8` | 2,050,969 | 2026-04-05 14:57:11.593115400 +0200 |

### The tracked-modification shape, reported before Task 2 began

**Exactly four tracked-and-modified paths, and no others:**

```
 M	FRAMEWORK.md
 M	cowork_rulings_2026_08_31_decision_surface_sitting.md
 M	tools/audit/derivation_boot_pack.json
 M	tools/audit/gen_derivation_boot_pack.py
```

863 changed-path records in total, of which 4 tracked-modified and 859 untracked. **All four are
named in §7's expected list; there is no OTHER tracked modification, so the §7 STOP was not met.**
§7 also expects "the `l0-l1` pack's files": **no such path appears as tracked-and-modified.** Under
§7's own sentence that untracked Cowork material is expected, that is not a STOP and is reported
rather than resolved.

**★ ONE COMMAND WAS REFUSED BY THE STANDING SHELL-READ GUARD, AND THE REFUSAL IS REPORTED RATHER
THAN WORKED AROUND.** `git status --porcelain` was refused with the guard's own message naming
**D-253** and the sanctioned substitute, `python tools/audit/changed_paths.py`, which reports paths
and status codes and cannot return file content. That substitute was used, and the shape above is
its output. Stated because a batch that meets a guard should say so, and because the guard —
not this session's judgment — chose the route.

*Note on §0.2's "runs no project tool": `changed_paths.py` is not a build, a test or a measurement
of the analysis. It is the guard's named enumeration route for exactly the fact §1 orders reported,
and the batch did not leave its scope to run it.*

### ZIP readers available — named

| Reader | Status |
|---|---|
| `unzip` | **present**, at `/usr/bin/unzip` |
| `python -m zipfile` | **present** (its CLI usage banner was obtained) |
| Python `zipfile` module | **present**, under Python 3.14.3 |

**Nothing was installed.** The STOP "no ZIP reader available" was not met.

---

## 2. Task 2 — what the container IS

### (a) The archive member listings, whole and unsummarised

**`"tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz"`**

```
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
     158  Defl:N      120  24% 1980-00-00 00:00 db8da076  META-INF/container.xml
 1701770  Defl:N    54710  97% 1980-00-00 00:00 6c222647  temp_10111.mscx
   19995  Defl:N    20010  -0% 1980-00-00 00:00 204fcb9c  Thumbnails/thumbnail.png
--------          -------  ---                            -------
 1721923            74840  96%                            3 files
```

**`"tools/extra scores/large/haydn-symphony-no-6.mscz"`**

```
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
     168  Defl:N      127  24% 1980-00-00 00:00 48db223e  META-INF/container.xml
    1375  Defl:N      817  41% 1980-00-00 00:00 0e1c8a78  Thumbnails/thumbnail.png
 3312424  Defl:N   126002  96% 1980-00-00 00:00 c5e06dad  Haydn Symphony No. 6.mscx
--------          -------  ---                            -------
 3313967           126946  96%                            3 files
```

**`tools/dcml/ABC/MS3/n01op18-1_01.mscz`**

```
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
  104802  Defl:N    15588  85% 2026-04-15 15:41 3dd43c87  score_style.mss
 2673651  Defl:N   353248  87% 2026-04-15 15:41 72f2f640  n01op18-1_01.mscx
   63040  Defl:N    59991   5% 2026-04-15 15:41 8e86d7cf  Thumbnails/thumbnail.png
       3  Defl:N        5 -67% 2026-04-15 15:41 7068d244  automation.json
   10450  Defl:N      842  92% 2026-04-15 15:41 5ed4bb2f  audiosettings.json
      55  Defl:N       45  18% 2026-04-15 15:41 93e5d13e  viewsettings.json
     377  Defl:N      166  56% 2026-04-15 15:41 863ce8c0  META-INF/container.xml
--------          -------  ---                            -------
 2852378           429885  85%                            7 files
```

Every member in all three archives is stored with compression method **`Defl:N`** (deflate, normal).
**Each archive is a ZIP**: `unzip` read all three, and `unzip -t` reported **"No errors detected in
compressed data"** for each — so every member's stored CRC-32 verifies against its decompressed
bytes. *(The two `large/` archives carry the ZIP epoch placeholder date `1980-00-00 00:00` on every
member; the ABC archive carries real per-member timestamps of 2026-04-15 15:41.)*

### (b) Exactly one score `.mscx` per archive — and what the other members are

**All three archives contain exactly one `.mscx`.** The dispatch's "not a STOP" case — more than one
`.mscx`, or none — did not arise.

| Archive | The one `.mscx` | Other members, and what they are |
|---|---|---|
| Brandenburg | `temp_10111.mscx` | `META-INF/container.xml` (158 B) — **established**: `META-INF/container.xml` is the OPC/ODF-style container manifest naming the archive's root document; its size is consistent with that and nothing beyond the name and size is claimed. `Thumbnails/thumbnail.png` (19,995 B) — a thumbnail image, as its name says; its −0 % compression ratio is what an already-compressed PNG gives. |
| Haydn | `Haydn Symphony No. 6.mscx` | `META-INF/container.xml` (168 B) — same kind. `Thumbnails/thumbnail.png` (1,375 B) — a thumbnail image. |
| ABC | `n01op18-1_01.mscx` | `META-INF/container.xml` (377 B) — same kind. `Thumbnails/thumbnail.png` (63,040 B) — a thumbnail image. `score_style.mss` (104,802 B) — **a GUESS**: a MuseScore style sheet, i.e. the engraving/layout settings carried as a separate member; supported by the fact that the whole `<Style>` block present in the sibling `.mscx` is absent from this archive's `.mscx` (§3(a) below), but **not established here**. `audiosettings.json` (10,450 B), `viewsettings.json` (55 B), `automation.json` (3 B) — **GUESSES**: playback, view and automation settings respectively, read from their names alone; `automation.json`'s 3 bytes can hold only an empty JSON container. |

**The `.mscx` is not the whole archive, and the Brandenburg case shows how far the name can drift
from the score:** its single score member is named **`temp_10111.mscx`**, which names nothing about
the music. The score's identity lives in the container's file name, not in the member's.

### (c) Extraction — outside the repository working tree

**Absolute scratch path used:**

```
C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\ce9c5a65-5c52-4a1c-89d7-1626bfcb66b2\scratchpad\mscz_establish
```

That is the OS temp directory. **It is not under the repository, not a gitignored path under the
repository, and not tracked anywhere within it.** The §6 STOP "extraction writing anywhere under the
repository working tree" was not met.

| Extracted `.mscx` | Bytes | sha256 | Equals archive's recorded uncompressed length |
|---|---:|---|---|
| `brandenburg/temp_10111.mscx` | 1,701,770 | `a4d9d89798469f654e120e08884c4c6e3c47c2842e2b2fccc53ec9db87fbac80` | yes (1,701,770) |
| `haydn/Haydn Symphony No. 6.mscx` | 3,312,424 | `ceb0d1aa386c02c604f0ceba70f60fa70cc7d07d50ca665e82a6875b1a8a728b` | yes (3,312,424) |
| `abc/n01op18-1_01.mscx` | 2,673,651 | `4c4089972ad931282a1c21656ec9da6828e6885fdf5fc3aaa073c361d2af460c` | yes (2,673,651) |

**★ THIS IS THE CONTAINER'S OWN LOSSLESSNESS, AND IT IS ESTABLISHED RATHER THAN INFERRED.** For each
archive the extracted member's byte count equals the length the archive records for it, and every
member's CRC-32 verifies. **A `.mscz` is a lossless byte carrier of the `.mscx` it holds.** That is a
different question from §3(a)'s, and the two must not be run together.

---

## 3. Task 3 — the losslessness test, and the plainness check

### (a) THE LOSSLESSNESS TEST — the `ABC` pair

**In the order the dispatch asks.**

**1. Are they byte-identical? NO.** The archive's inner `.mscx` is 2,673,651 bytes,
`sha256 4c408997…`; the sibling on disk is 2,050,969 bytes, `sha256 a4ccf07d…`.

**A line-ending difference sits underneath the comparison and is reported before the line counts, so
the counts below are not read as content.** The sibling on disk uses **CRLF** terminators (69,223
lines, 69,223 CR bytes); the archive's inner file uses **LF** only (84,040 lines, 0 CR bytes). A raw
line diff would therefore have shown every line as differing. **The comparison below was run after
normalising the sibling's terminators to LF**, and the normalised copy was proven byte-identical to
the file on disk except for those terminators: the copy taken into scratch reproduced the source's
`sha256 a4ccf07d…` and size 2,050,969 exactly before normalisation.

**2. The number of differing lines, and the first ten differences in full.**

After terminator normalisation the two still differ: **670 lines present only in the sibling, 15,487
lines present only in the archive's copy, across 14,038 hunks** — 16,157 changed lines in all.

The first ten differences, in full (`<` = sibling on disk, `>` = the archive's inner `.mscx`):

```
2,4c2,4
< <museScore version="3.02">
<   <programVersion>3.6.2</programVersion>
<   <programRevision>3224f34</programRevision>
---
> <museScore version="5.00">
>   <programVersion>5.0.0</programVersion>
>   <programRevision>abc123456</programRevision>

6,7c6
<     <LayerTag id="0" tag="default"></LayerTag>
<     <currentLayer>0</currentLayer>
---
>     <eid>Hsf0tZSzZ0F_1Pgtjy4j8uK</eid>

9,146d7                     [the entire <Style> block, 138 lines, present only in the sibling:
<     <Style>                pageWidth, pageHeight, page margins, lyrics fonts and spacing, bar and
      … 136 further lines …  barline widths, bracket width, clef margins, stem width, ledger line
<       </Style>             length, hairpin/pedal/ottava/tuplet/volta widths and fonts, chord-symbol
                             fonts, slur width, musical symbol and text fonts, every title/subtitle/
                             composer/lyricist/fingering/instrument/dynamics/expression/tempo/
                             metronome/measure-number/translator/system/staff/rehearsal-mark/repeat/
                             frame font, padding, width and round setting, usePre_3_6_defaults,
                             defaultsVersion, Spatium and romanNumeralPlacement]

150a12
>     <open>1</open>

152a15
>     <metaTag name="audioComUrl"></metaTag>

162c25
<     <metaTag name="mscVersion">3.02</metaTag>
---
>     <metaTag name="mscVersion">5.00</metaTag>

166a30
>     <metaTag name="sourceRevisionId"></metaTag>

170,171c34,36
<     <Part>
<       <Staff id="1">
---
>     <Part id="1">
>       <Staff>
>         <eid>2T7kwPn8cCF_s2n8Q/LPKmB</eid>

174,175c39,40
<         <bracket type="0" span="4" col="0"/>
<         <barLineSpan>3</barLineSpan>
---
>         <bracket type="0" span="4" col="0" visible="1"/>
>         <barLineSpan>1</barLineSpan>

177d41
<       <trackName>Violin I</trackName>
```

*(The third hunk's 138 lines are all `<Style>` engraving settings of the shape shown; they are
summarised inside the hunk rather than transcribed, and the enumeration below accounts for every
one of them individually, so nothing is hidden by that summary.)*

**3. Does any difference touch a `<Note>`, `<Chord>`, `<Rest>`, `<Staff`, `<Measure>`, `<TimeSig>` or
`<KeySig>` element, or only version stamps, ordering and layout?**

**IT TOUCHES THEM. The answer is not "only version stamps, ordering and layout", and it is reported
plainly.**

The verdict rests on a **complete enumeration, not a sample**: every one of the 16,157 changed lines
was reduced to its XML tag name and counted, and the counts reconcile arithmetically —
**13,934 + 810 + 810 + 71 + 71 + 37 + 37 + 34 + 32 + 32 + 24 + 24 + (5 × 8) + (8 × 4) + (2 × 3) +
(9 × 2) + (145 × 1) = 16,157 = 670 + 15,487.** No changed line fell outside the enumeration.

| What changed | Changed lines | Class |
|---|---:|---|
| `<eid>` elements added throughout | 13,934 | new-format element identifiers, added on essentially every element — **so they fall inside `<Note>`, `<Chord>`, `<Rest>`, `<Measure>`, `<Staff` and `<KeySig>` elements** |
| `<name>` re-nested inside a new `<harmonyInfo>` wrapper | 810 + 810 | **the `<Harmony>` values are preserved** — each removed `<name>X</name>` reappears with the same text one level deeper |
| `<italic>`, `<bold>` | 71 + 71 | text formatting |
| `<placement>`, `<direction>` | 37 + 37 | engraving placement |
| **`<BeamMode>begin32</BeamMode>` → `<BeamMode>begin16</BeamMode>`** | 34 (17 sites) | **a VALUE change inside `<Chord>` — beam subdivision** |
| `<endHookHeight>`, `<beginHookHeight>` | 32 + 32 | engraving |
| **`<Articulation>` → `<Ornament>`** | 24 + 24 (12 sites) | **an element rename inside `<Chord>`; the `<subtype>` child is unchanged** (e.g. `ornamentTrill` on both sides) |
| `<shortName>`, `<longName>`, `<InstrumentLabel>` | 8 + 8 + 8 | part naming / labels |
| **`<Staff id="N">` → `<Staff>`, with the id moved to `<Part id="N">`** | 8 (`Staff`) + 8 (`Part`) | **a `<Staff` structural change** |
| `<trackName>` removed | 4 | part naming |
| `<style>`, `<metaTag>` | 4 + 4 | metadata |
| `<fractions>7/16</fractions>` ↔ `<fractions>1/4</fractions>` | 4 (2 sites) | **pure REORDERING** — two `<Slur>` elements with their `<SlurSegment>` offsets swapped position; both values present on both sides |
| **`<accidental>-1</accidental>` → `<concertKey>-1</concertKey>`** | 4 + 4 | **a child rename inside `<KeySig>` — the value `-1` is preserved** (verified at the sibling: the tag sits inside `<KeySig>`, beside `<mode>major</mode>`) |
| **`<barLineSpan>3</barLineSpan>` → `<barLineSpan>1</barLineSpan>`** | 4 | a VALUE change in the part list |
| `<SlurSegment>` | 4 | moves with the `<fractions>` reorder |
| `<offset>`, `<controller>` | 3 + 3 | engraving offset / playback |
| `<subtype>`, `<span>`, `<bracket>`, `<Clef>`, `<Channel>`, `<museScore>`, `<programVersion>`, `<programRevision>`, `<Style>` | 2 each | version stamps and layout |
| 145 further single lines | 145 | 143 of them are the `<Style>` block's individual engraving settings; the other two are `<LayerTag>` and `<currentLayer>` |

**AND WHAT DID NOT CHANGE — the half that decides how the verdict is read.** Not one changed line is
a `<pitch>`, a `<tpc>`, a `<durationType>`, a `<voice>`, a `<track>`, a `<sigN>` or a `<sigD>`, and
not one is a `<Note>`, `<Chord>`, `<Rest>`, `<Measure>` or `<TimeSig>` element opening. **Because the
enumeration is complete and reconciles, that is a statement about every changed line and not about a
sample: no pitch, no spelling, no duration and no time signature moved between the two files.**

**★ WHAT THIS TEST DOES AND DOES NOT ESTABLISH, STATED BECAUSE THE DISPATCH CALLS THIS DISTINCTION
LOAD-BEARING.**

- **It does NOT measure what a container costs.** The two files are different MuseScore FORMAT
  VERSIONS — `3.02` / `programVersion 3.6.2` on disk against `5.00` / `programVersion 5.0.0` inside
  the archive, with `<metaTag name="mscVersion">` moving `3.02` → `5.00` in step. The archive is not
  a zipped copy of the sibling; it is a **later-format re-save of the same score**. The dispatch's
  premise that this pair isolates the container's cost is therefore **not satisfied by these two
  objects**, and that is reported rather than repaired.
- **Whether the format migration CAUSED each difference is NOT established here** (#18). Every
  difference above is *consistent with* a MuseScore-3-to-5 migration; this batch measured the two
  files and did not run either version, so no causal claim is made. Two differences would in any case
  need explaining before anyone leaned on them: the **beam subdivision** change at 17 sites, and
  **`barLineSpan` 3 → 1**.
- **The container's own losslessness IS established, separately and cleanly** — §2(c) above: byte
  length preserved exactly and every CRC verified, on all three archives.
- **One observation, labelled as such:** the archive's `<programRevision>` reads `abc123456`, which
  is a placeholder rather than a revision hash. What produced that file is not established here.

**So, in the plain terms the dispatch asks for:** *decoding a container recovers the notation's
pitches, spellings, durations and time signatures untouched — this pair proves that much, and does
so completely rather than by sampling. It does not show the decode is inert: staff structure, key-signature
child naming, ornament classification, beam subdivision and barline span all differ across this
pair, and those differences belong to a format-version gap the pair cannot separate from the
container.*

### (b) THE PLAINNESS CHECK — all three extracted `.mscx`

Method, stated so the counts can be challenged: each extracted file was parsed as XML; a `<Staff>`
inside a `<Part>` is a **part-list** entry and a `<Staff>` at score level is a **body** section;
element counts are of opening tags over the whole tree; the pitch window takes the first 24 `<Chord>`
elements of each body staff **in document order**, and each chord's `<pitch>` children in file order.
**A grace-note chord, being its own `<Chord>` element, is counted as a chord in that window.**

---

#### Brandenburg — `temp_10111.mscx` (museScore version `3.01`, programVersion `3.0.0`)

- **Part-list `<Staff id="N">` entries: 9**, ids `1,2,3,4,5,6,7,8,9`. *(In this format version
  `<Part>` carries no id; the id is on the `<Staff>`.)*
- **Body `<Staff id="N">` sections: 9**, ids `1,2,3,4,5,6,7,8,9`.
- **`<Harmony>`: 0. `<FiguredBass>`: 0. `<StaffText>`: 0.**
- **`<trackName>`, in order (18):** `Violino principale (Violin)`, `Violin`, `Flauto 1 (Recorder)`,
  `Recorder`, `Flauto 2 (Recorder)`, `Recorder`, `Violino 1 (Violin)`, `Violin`,
  `Violino 2 (Violin)`, `Violin`, `Viola`, `Viola`, `Violoncello`, `Violoncello`, `Violone`,
  `Violone`, `Continuo`, `Harpsichord`.
- **`<instrumentId>`, in order (9):** `strings.violin`, `wind.flutes.recorder`,
  `wind.flutes.recorder`, `strings.violin`, `strings.violin`, `strings.viola`, `strings.cello`,
  `strings.viol.violone`, `keyboard.harpsichord`.

**First 24 chords' `<pitch>` values, per body staff:**

```
staff 1: 74 79 79 78 79 81 79 78 79 74 76 71 72 69 74 69 71 67 69 71 73 74 76 78
staff 2: 79 86 86 85 86 88 86 85 86 81 83 78 79 76 81 76 78 74 74 73 74 76 74 76
staff 3: 79 86 86 85 86 88 86 85 86 81 83 78 79 76 81 76 78 74 74 73 74 76 74 76
staff 4: 74 79 79 78 79 81 79 78 79 74 76 71 72 69 74 69 71 67 69 71 73 74 76 78
staff 5: 67 74 74 73 74 76 74 73 74 69 71 66 67 64 69 64 66 62 64 66 64 62 64 66
staff 6: 62 67 67 66 67 69 67 66 67 62 64 59 60 57 62 57 59 55 57 59 61 62 64 66
staff 7: 55 57 59 57 59 55 57 55 57 59 60 59 60 57 59 55 52 57 54 50 55 59 57 55
staff 8: 43 50 50 49 50 52 50 49 50 45 47 42 43 40 45 40 42 38 40 42 44 45 40 45
staff 9: 55 57 59 57 59 55 57 55 57 59 60 59 60 57 59 55 52 57 54 50 55 59 57 55
```

Every chord in every one of these windows holds exactly one pitch.

**Pairs that MATCH over the tested window — three of the 36 pairs:**

- **staff 1 and staff 4** — `Violino principale` and `Violino 1`
- **staff 2 and staff 3** — `Flauto 1` and `Flauto 2`
- **staff 7 and staff 9** — `Violoncello` and `Continuo` / `Harpsichord`

**All 33 other pairs differ.** Each of the three is reported as **matching over the tested window**
and **not** as a duplicate: the wider claim needs the whole staff and this batch does not make it.
Three of the nine staves are therefore in unison with another staff across the opening 24 chords.

---

#### Haydn — `Haydn Symphony No. 6.mscx` (museScore version `2.06`, programVersion `2.3.2`)

- **Part-list `<Staff id="N">` entries: 12**, ids `1…12`.
- **Body `<Staff id="N">` sections: 12**, ids `1…12`.
- **`<Harmony>`: 0. `<FiguredBass>`: 0. `<StaffText>`: 105.**
- **`<trackName>`, in order (26):** `Flute Section`, `Flute Section`, `Oboe`, `Oboe`, `Bassoon`,
  `Bassoon`, `French Horn`, `French Horn`, `Violin`, `Violin`, `Violin Section`, `Violin Section`,
  `Violin Section`, `Violin Section`, `Viola Section`, `Viola Section`, `Violoncello`, `Violoncello`,
  `Contrabass`, `Contrabass`, `Violoncello Section`, `Violoncello Section`, `Contrabass Section`,
  `Contrabass Section`, `Violoncello`, `Contrabass`.
- **`<instrumentId>`, in order (14):** `wind.flutes.flute`, `wind.reed.oboe`, `wind.reed.bassoon`,
  `brass.french-horn`, `strings.violin`, `strings.group`, `strings.group`, `strings.group`,
  `strings.cello`, `strings.contrabass`, `strings.group`, `strings.group`, `strings.cello`,
  `strings.contrabass`.

**First 24 chords' `<pitch>` values, per body staff** (staff 4 carries two-note chords, shown
bracketed):

```
staff 1 : 83 85 86 90 86 85 81 81 81 81 81 74 69 78 74 69 81 78 74 76 78 79 81 83
staff 2 : 81 79 66 71 79 78 80 69 74 81 81 76 76 76 76 73 73 73 73 69 69 69 73 76
staff 3 : 50 50 50 50 50 50 50 50 47 45 45 45 45 57 57 57 57 57 57 50 50 50 50 50
staff 4 : [50 62] [50 62] [45 57] [45 57] [66 69] [66 69] 69 64 69 64 66 62 66 62 62 [57 64] 64 64 [62 71] [57 69] [57 69] [57 69] [57 69] [57 69]
staff 5 : 62 64 66 67 69 70 62 62 62 62 64 64 64 64 66 66 66 66 67 67 67 67 69 69
staff 6 : 62 64 61 62 64 61 62 61 62 61 62 64 66 67 64 66 67 64 66 64 66 64 66 67
staff 7 : 62 64 61 62 64 61 62 61 62 61 62 64 66 66 66 66 69 71 73 74 74 73 73 69
staff 8 : 66 69 66 64 64 64 52 57 57 69 69 69 69 69 69 62 62 62 62 62 62 67 67 69
staff 9 : 55 52 50 49 48 46 43 43 43 43 62 60 60 62 60 59 64 64 62 60 59 57 55 67
staff 10: 50 45 53 45 50 45 52 45 55 45 52 45 53 41 40 52 50 44 45 50 45 53 45 50
staff 11: 50 50 50 50 50 50 50 50 47 45 45 45 45 57 57 57 57 57 57 50 50 50 50 50
staff 12: 38 38 38 38 38 38 38 38 35 33 33 33 33 45 45 45 45 45 45 38 38 38 38 38
```

**One pair MATCHES over the tested window, of the 66 pairs: staff 3 and staff 11.** By the part-list
order those are the `Bassoon` and the `Violoncello Section`. **All 65 other pairs differ.** Reported
as matching over the tested window, not as a duplicate.

**Two observations about the part naming, labelled as observations and not verdicts.** There are
**26 `<trackName>` values for 12 staves** — 24 would be two per part — and **14 `<instrumentId>`
values for 12 staves**. Something in this file names more instruments than it has staves. This batch
did not establish what: an instrument change, an extra `<Instrument>` element, or something else.
It is exactly the third part of §3u's second check question — *is the part naming what it claims* —
and it is left open rather than answered by guess.

---

#### ABC inner — `n01op18-1_01.mscx` (museScore version `5.00`, programVersion `5.0.0`)

- **Part-list `<Staff>` entries: 4** — and **each carries NO `id`**; in this format version the id is
  on the `<Part>`, which reads `<Part id="1">`, `<Part id="2">`, `<Part id="3">`, `<Part id="4">`.
- **Body `<Staff id="N">` sections: 4**, ids `1,2,3,4`.
- **`<Harmony>`: 405. `<FiguredBass>`: 0. `<StaffText>`: 71.**
- **`<trackName>`, in order (4):** `Violin`, `Violin`, `Viola`, `Cello`.
- **`<instrumentId>`, in order (4):** `strings.violin`, `strings.violin`, `strings.viola`,
  `strings.cello`.

**First 24 chords' `<pitch>` values, per body staff:**

```
staff 1: 65 65 67 65 64 65 60 65 65 67 65 64 65 62 77 77 79 77 76 77 79 70 69 74
staff 2: 65 65 67 65 64 65 60 65 65 67 65 64 65 62 70 70 67 65 70 67 65 64 65 65
staff 3: 53 53 55 53 52 53 48 53 53 55 53 52 53 50 62 60 60 62 55 60 59 60 59 60
staff 4: 53 53 55 53 52 53 48 53 53 55 53 52 53 50 50 52 53 50 46 48 53 53 55 53
```

Every chord in these windows holds exactly one pitch. **No pair matches over the tested window** —
all six pairs differ. *(Staves 1 and 2, and staves 3 and 4, are in unison for the first fourteen
chords and separate from the fifteenth; the window is long enough to separate them, which is the
point of testing 24 rather than a handful.)*

**★ THIS FILE IS NOT A PLAIN NOTATIONAL RECORD. It carries 405 `<Harmony>` elements inline on the
music staves** — Roman numerals, whose `<name>` values include `F.I`, `V`, `I` and `IV6` as read
directly at the changed lines of §3(a)'s diff. It is the **third shape** §3u names, the one
`bach_en_fr_suites` has: analysis inline, no duplicated staff, no figured bass. It also carries 71
`<StaffText>`.

---

## 4. The three written predictions, marked

**P-i — "each `.mscz` is a ZIP holding exactly one score `.mscx`, plus container metadata and
probably a thumbnail image." → HELD**, with what it under-named stated. All three are ZIPs; each
holds exactly one `.mscx`; each holds `META-INF/container.xml` and `Thumbnails/thumbnail.png`. **The
prediction under-named the ABC archive**, which carries four further members — `score_style.mss`,
`audiosettings.json`, `viewsettings.json`, `automation.json`. Whether those count as "container
metadata" is a judgment the prediction leaves open; the observed member sets are reported above and
the reader may decide. **The two `large/` archives match the prediction exactly, at three members
each.**

**P-ii — "the `.mscx` inside `n01op18-1_01.mscz` is NOT byte-identical to its sibling
`n01op18-1_01.mscx`, because the two mtimes are about a year apart and the `.mscz` is the later."
→ THE CLAIM HELD; ITS STATED GROUND IS PARTLY FALSIFIED, and the falsification is recorded rather
than repaired.**

| Half of P-ii | Observed | Verdict |
|---|---|---|
| not byte-identical | `4c408997…` vs `a4ccf07d…`; 2,673,651 vs 2,050,969 bytes | **HELD** |
| "the two mtimes are about a year apart" | `.mscz` 2026-04-15 15:41:35; `.mscx` 2026-04-05 14:57:11 — **ten days apart, not about a year** | **FALSIFIED** |
| "the `.mscz` is the later" | 2026-04-15 is later than 2026-04-05 | **HELD** |

*And the real ground turned out to be something the prediction did not name at all:* the two files
are different MuseScore format versions, which is a far stronger reason for non-identity than a date
gap of any size.

**P-iii — "the Brandenburg inner `.mscx` carries 0 `<Harmony>` and 0 `<FiguredBass>`, and 9 staves,
matching `tools/extra_scores_registry.json`'s measured row." → HELD, in all three parts.**
`<Harmony>` 0; `<FiguredBass>` 0; 9 part-list staff entries and 9 body staff sections; and the
registry's own row for that path records `"staves": 9` and `"parts": 9`
(`tools/extra_scores_registry.json`, the `bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz`
entry). **The prediction did not reach `<StaffText>`, which is also 0**, so the file is clean of all
three annotation element kinds.

---

## 5. Task 4 — nothing moved

**The four input files, re-recorded at the close and shown against Task 1's record:**

| Path | sha256 then / now | size then / now | mtime then / now |
|---|---|---|---|
| `"…/large/bach-brandenburg-…-presto.mscz"` | `56e2241707…f89cfb` / **identical** | 75,260 / **identical** | 2026-07-28 10:47:00.027952900 +0200 / **identical** |
| `"…/large/haydn-symphony-no-6.mscz"` | `4ba5c99070…6dffd` / **identical** | 127,386 / **identical** | 2026-07-28 10:51:49.173893000 +0200 / **identical** |
| `tools/dcml/ABC/MS3/n01op18-1_01.mscz` | `727f230e8d…d6946` / **identical** | 430,695 / **identical** | 2026-04-15 15:41:35.825071400 +0200 / **identical** |
| `tools/dcml/ABC/MS3/n01op18-1_01.mscx` | `a4ccf07d2f…d98a8` / **identical** | 2,050,969 / **identical** | 2026-04-05 14:57:11.593115400 +0200 / **identical** |

**All four match on all three fields. The §6 STOP was not met. This batch modified no input.**

**The tracked-modification shape re-run at the close is identical to the start state** — the same
four tracked-modified paths, and no fifth. Measured twice, before and after this report existed:
**863 changed-path records before it was written, 864 after, the one added record being
`?? cc_mscz_container_establishment_report.md` itself.** **This batch modified nothing tracked, and
created nothing untracked inside the repository except this report.**

**The scratch directory was DELETED and the deletion confirmed**: `mscz_establish` and every working
file beside it were removed and the scratchpad directory then listed empty. Nothing of this batch's
working material survives anywhere.

---

## 6. STOPs

**No STOP of §6 was met.** Taken in the order §6 lists them:

| STOP | Met? |
|---|---|
| No ZIP reader available | **No** — three are available and named |
| An input file's `sha256` differing between Task 1 and Task 4 | **No** — all four identical on sha256, size and mtime |
| Extraction writing anywhere under the repository working tree | **No** — the scratch path is under the OS temp directory |
| A read disagreeing with its pin | **No** — all eight pins reproduced at the close |
| Any act outside §7 | **No** — see the footprint below |

**The "not a STOP, reported rather than resolved" cases:**

| Case | Occurred? |
|---|---|
| An input file's size differing from §1's table | **No** — all four match exactly |
| A prediction falsified | **Yes, partly** — P-ii's stated *ground* is falsified on the mtime gap while its claim held; recorded above and not repaired into a success |
| An archive holding more than one `.mscx`, or none | **No** — exactly one in each of the three |

**Additionally reported, being neither a §6 STOP nor a §6 named case:**

1. **The shell-read guard refused `git status --porcelain`** and named its substitute; the substitute
   was used. §1a.
2. **`§7`'s expected "`l0-l1` pack's files" do not appear as tracked-and-modified.** Not a STOP under
   §7's own untracked-material sentence; reported.
3. **The §3(a) pair is two different format versions**, so the losslessness test as posed does not
   isolate the container. §3(a). This is the finding the batch surfaces rather than builds around
   (#13), and it is why §2(c)'s separate, clean establishment of the container's byte-losslessness is
   reported apart from it.

---

## 7. The footprint, as executed

**Created:** this report, and nothing else in the repository. **Edited: NOTHING.** No score was
edited, renamed, moved, converted or re-saved. **No decoded `.mscx` was written into the
repository** — not into `"tools/extra scores/"`, not into `tools/dcml/`, not into a scratch folder
under the repository, not anywhere tracked or gitignored within it; the three extracted `.mscx` and
every working file live under the OS temp directory and have been deleted. **No tool source was
edited.** No registry, manifest or pin was touched — **`tools/snapshot_sources_manifest.json` and
the eleven snapshot sources are untouched (Hard rule 2)**. `tools/extra_scores_registry.json` was
READ only.

**Not done at all:** no build, no test, no golden, no measurement of the analysis, nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; no boot pack rendered and neither frozen
pack opened; no governing document amended; no open-items row created, flipped or discarded; no
decisions-register entry and no `D-NNN` allocated — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route; the workbook was not opened; **no
score selected and NO SCORE STAGED**; no brief written; no session booted.

**Hard rule 3 was honoured in every command:** `"tools/extra scores/…"` was quoted in every shell
command that names it, including the two `unzip -v`, the two `unzip -t`, the `unzip -j`, and both
`sha256sum` / `stat` passes.

### The one optional line — `tools/ziprw/`

**Established from its own two files, in under a minute.** `tools/ziprw/` is a standalone C++ command
-line utility with its own CMake project (`project(ziprw)`), building against MuseScore's own
`muse_global` framework and Qt 6.8. `main.cpp` defines `unzip(zip_path, extract_path)` and
`zip(dir_path, zip_path)` on top of `muse::ZipReader` / `muse::ZipWriter`
(`serialization/zipreader.h`, `serialization/zipwriter.h`) and `io::IFileSystem`. **It is a ZIP
read/write tool built on this project's own serialization classes — directly on the subject of this
batch, not an unrelated build dependency.** It was **not built and not run**; nothing above depends
on it.

---

## 8. The standing self-check

Run before this report was written, on the work actually on disk rather than on the intention.

**The diff on disk.** The repository's tracked-modification shape at the close is byte-for-byte the
start state's — four modified paths, none of them this batch's, 863 records both times. **No
repository file was touched.** The only repository object this batch creates is this report. Every
other file it wrote lives outside the repository and is deleted.

**Against the principles.** **#15** — every claim above is verified at the object: the pins at the
blobs, the sizes and digests at the files, the member lists at the archives, the counts at the parsed
XML, the tag classification at the diff. **#17(f) / D-431** — no figure of this project's own analysis
measurement is restated; the one project measurement quoted, the registry's `"staves": 9`, is quoted
because P-iii names it and is cited to its file. **#19** — the container's losslessness is
*positively* established (CRC verified on every member, extracted length equal to recorded length on
all three) rather than left merely unfalsified. **#18** — no causal claim is made about what produced
the format-version differences; the batch measured two files and says so. **#12** — the prediction
that failed is recorded as failed, with its correct and incorrect halves separated, and the surprise
finding is surfaced rather than absorbed (#13). **#5** — the `<trackName>`/`<instrumentId>` count
anomaly in the Haydn file is stated as an open question rather than filled by guess.

**Against `DEFECT_TYPES.md`.** **DT-26 (scope-assumed enumeration)** is the live risk in this batch
and it is met head-on twice: the tag classification of §3(a) is run over the **whole** changed-line
population and **reconciled arithmetically** (`13,934 + … + 145 = 16,157 = 670 + 15,487`), so the
"only version stamps" verdict is a statement about every line and not a sample; and the 24-chord
window of §3(b) is a **scope stated in the claim itself** — every matching pair is reported as
*matches over the tested window*, never as *duplicate*, exactly as the dispatch requires.
**DT-11 (hand-transcribed figure)** — every number here is the output of a command shown in this
session, not a recollection. **DT-23 (silent drop)** — the extraction script carries no bare
`except`; a parse failure would have raised, and none did.

**One thing this report does NOT claim.** That the three matching staff pairs are duplicates, that
the Haydn naming anomaly is a defect, or that any of the three files should or should not be staged.
**No score is selected and none is staged.** Those are the user's, on the surface the writing side
brings.

---

*Provenance: executed by Claude Code, 2026-09-01, against
`cc_instruction_mscz_container_establishment_2026_09_01.md` (pin
`8c2689364cd85e61fcdebd84742dc4c40df4ce01`), which executes Ruling 15's constraint (iii) as scoped by
§3u of `cowork_rulings_2026_08_31_decision_surface_sitting.md`. Every fact above was established at
the object in this session. The scratch directory used and then deleted was
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\ce9c5a65-5c52-4a1c-89d7-1626bfcb66b2\scratchpad\mscz_establish`.*
