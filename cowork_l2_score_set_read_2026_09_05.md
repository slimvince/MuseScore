# L2's staged score set, with each claim checked at the file — read 3 of §11

> **STATUS: DERIVED 2026-09-05, A READ PUT TO THE USER BY NAME. NOT RULED. NOTHING IS STAGED TO ANY
> SESSION BY THIS FILE.** Written by the Cowork session that booted on
> `cowork_handoff_entry_one_hundred_and_eleven.md`, at tip `911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb`
> (`refs/heads/master` and `refs/remotes/origin/master` both read with the file tools). This is act 1's
> third item in §11 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md`: *"the staged score set with
> each claim beside it (Ruling 7)"*. It takes no decision, reads no paper, renders no pack, writes no
> dispatch and amends no document. Every claim below is challengeable at the file it names.

## 1. The test, quoted

Ruling 7: *"A small set of scores with their When in Rome/DCML analyses (the only annotation family
established as ground truth under the ruled grading conventions; BCMH is not, D-475), chosen to exhibit
named phenomena of L2's four limbs — a modulation with a tonicization beside it; a cadential six-four; a
passage where the annotation records a rival reading in the same stream; a suspension or passing-tone
texture where the chord-tone assignment is non-trivial — each claim checked at the file before it is
staged, the named set put to the user with each claim beside it before anything is staged (Ruling 15's
form). Plus the l0-l1 plain-score set unchanged. The standing bars carry over: files staged BY NAME and
never a directory; EXEMPLARS, NOT A CORPUS; the session builds, designs, scopes and runs no measurement."*

## 2. What was read to derive it

- `docs/score_inventory.md` whole (the mandatory read for any score task), for where the two annotation
  sources of the ruled family live: the DCML clones under `tools/dcml/<repo>/` and the *When in Rome*
  anthology under `tools/dcml/when_in_rome/Corpus/`.
- `cowork_blind_session_brief_l0_l1.md` §3, for the plain-score set of Ruling 15 (four files, quoted in
  §5 below).
- `cowork_blind_session_brief_harmony_boundary.md` §3 and §8 (P3), for the pilot's precedent on staging
  analyses and for the route to the *When in Rome* files.
- `FRAMEWORK.md` §5 (the "NOT A LAYER" block, lines 467–475), §4.2's elaboration-chord bullet (lines
  245–252), §9's DP-K with its two further grounds (lines 731–767), and Appendix B's first-stage draft
  §S2 "What a harmonic analysis IS, read off the ground truth" (lines 1445–1489) — the last is where the
  record states, at the object, that the ruled family records a rival reading *in the same stream*: the
  RomanText `mNvar1` lines.
- The files named in §3 and §4, each read with the file tools from a bridge-staged copy.

## 3. The set for L2, one file pair per exemplar, each claim beside it

### Exemplar A — the DCML form: Mozart, Piano Sonata K. 545, first movement

**Files (both staged; the `.mscx` carries the DCML labels inline as `<Harmony>` elements, the table is
their parsed form):**
- `tools/dcml/mozart_piano_sonatas/MS3/K545-1.mscx` (413,065 bytes at staging)
- `tools/dcml/mozart_piano_sonatas/harmonies/K545-1.harmonies.tsv` (9,164 bytes)

| Phenomenon | Claim | Checked at |
|---|---|---|
| Cadential six-four | The annotation writes it as a dominant carrying 6/4 suspensions, `V(64)`, at bars 11 (beats 2 and 4), 24 and 69. Bar 24 → bar 25 `V7` → bar 26 `I\|PAC` is the textbook shape, in the local key of G (`localkey` V). | `harmonies` rows for `mn` 11, 24, 25, 26, 69. `notes/K545-1.notes.tsv` bar 24: left hand D4–B4–G4–B4 under the D bass; bar 25: D4–C5–F♯4–C5 with A5 above. In the `.mscx`, `<name>V(64)</name>` occurs six times, as the table has six `V(64)` rows; `V65/V`, `V2(4)` and `V.V{` are likewise found there as `<Harmony>` names. |
| Modulation with a tonicization beside it | Bar 10 beat 4.5 `V65/V` (a tonicization of G inside C), bar 11 `V\|HC`, then bar 13 `V.V{` — the local key changes to G. And bar 68 `viio7/V` immediately before the `V(64)` of bar 69, in C. | `harmonies` rows for `mn` 10, 11, 13, 68, 69 (`localkey` column reads I, I, V, I, I). `notes` bar 10 beat 4.5: F♯3 in the left hand, D5–C5 above. |
| Suspension with a non-trivial chord-tone assignment | `V2(4)` at bars 15, 17, 60, 62: the seventh in the bass and a 4 held over it. | `notes` bar 15: left hand C4–D4–B3–D4, right hand G5 (a dotted eighth) resolving to F♯5 at beat 1.75; the label then changes to `V43` at beat 2 over A3. |
| Passing-tone texture with a non-trivial chord-tone assignment | Bar 5 is labelled one chord, `IV`, over a full sixteenth-note run. | `notes` bar 5: left hand F4 then F3+C4; right hand A4 then B4 C5 D5 E5 F5 G5 A5 G5 F5 E5 D5 C5 B4 A4 — B, D, E, G are not tones of F major and the annotation gives no chord change. |

### Exemplar B — the *When in Rome* form: Bach, chorale 003 "Ach Gott, vom Himmel sieh darein" (BWV 153/1)

**Files (both staged):**
- `tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx` (49,128 bytes; notes only —
  no `<Harmony>` element; two `<StaffText>`s, the title and `(BWV 153/3; R 005)`)
- `tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/003/analysis.txt`
  (901 bytes; analyst Andrew Jones, proofread Tymoczko and Robb)

**NOT staged:** `003/analysis_BCMH.txt` — D-475, as Ruling 7 says.

| Phenomenon | Claim | Checked at |
|---|---|---|
| Rival reading in the same stream | `m4 i6/4 b2 V b3 i :\|\| b4 G: V6` and `m4var1 III+6 b2 V b3 i \|\| b4 G: V6` — the same bar twice, differing in the first label only. `m6 i b2 iv6 b3 V \|\| b4 i` and `m6var1 i b2 iio6/4 b2.5 ii/o4/3 b3 V \|\| b4 i` — the variant has four statements where the principal has three, so the rival differs in segmentation as well as label. | `analysis.txt` lines 17–18 and 21–22. |
| Cadential six-four, with the analyst's chord-tone reason written beside it | m4 beat 1 is read `i6/4`; the note above it: *"reasonably common cadential figure in m4. If G# is an incomplete neighbor, it is i6/4, otherwise III+6 with A as a regular neighbor."* The label is stated to depend on which tone is heard as elaboration. | `analysis.txt` lines 16–18. The G♯ is in the score: `<tpc>22</tpc>` in bar 4 of the second staff of the `.mscx` (two occurrences). |
| Modulation | Three tonality changes in four bars: `b4 G:` at m4, `b1.5 e:` at m5, `a:` at m7, with the piece opening `m0 b4 a: V`. Tonicizations `viio7/IV` (m9 b4) and `viio7/V` (m10 b2) stand inside a:, not beside a modulation — that pairing is Exemplar A's. | `analysis.txt` lines 12, 17, 19, 23, 25, 26. |

**That the two files are the same music, checked at three points:** the `.mscx` opens with a one-beat
pickup (`<Measure len="1/4">`) whose soprano is B4, and the analysis opens `m0 b4 a: V`; the `.mscx`
splits bar 4 as `12/16` + `4/16` with the repeat there, and the analysis writes `m4 … b3 i :|| b4 G: V6`;
the G♯ of the analyst's note is in bar 4. `003/remote.json` records BWV 153.1, Riemenschneider 3, CPE 3.

### Exemplar C — the *When in Rome* form, no tonality change: Bach, chorale 001 "Aus meines Herzens Grunde" (BWV 269)

**Files (both staged):**
- `tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx` (58,371 bytes; notes only, no
  `<Harmony>`; `<StaffText>`s the title and `(BWV 269; R 030)`)
- `tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/001/analysis.txt`
  (768 bytes; same analyst and proofreaders)

**NOT staged:** `001/analysis_BCMH.txt` (D-475).

| Phenomenon | Claim | Checked at |
|---|---|---|
| Rival reading in the same stream, label alone | `m11 vi b2 iii6 b3 ii6` against `m11var1 vi b2 I6/4 b3 ii6`, under the note *"consecutive first inversion triads"* — the second beat read as a chord in its own right or as a passing six-four. | `analysis.txt` lines 22–24. |
| Rival reading that changes the segmentation | `m17 vi b2 IV b3 I` against `m17var1 vi b2 IV b2.5 viio6/4 b3.5 I` — four statements against three, and the third statement moves from beat 3 to beat 3.5. | `analysis.txt` lines 30–31. |
| One tonality throughout, with a tonicization | `m0 b3 G: I` and no later key statement; `V7/IV` at m13 b3 into `IV` at m14. | `analysis.txt` lines 11, 26, 27. |

**Same music, checked:** 3/4 in both (`<sigN>3</sigN>`; `Time Signature: 3/4`), a one-beat pickup in both
(`<Measure len="1/4">`; `m0 b3`), bar 7 split `4/8` + `2/8` in the `.mscx` and `m7 I :|| b3 I` in the
analysis. `001/remote.json` records BWV 269.

*Why C beside B rather than B alone:* C supplies the rival-reading case where the label alone differs and
the case where the segmentation differs, in a piece with no tonality change at all, so the session can
see the rival mechanism apart from the modulation mechanism; it is one small file pair.

## 4. Why these and not others

- **One DCML exemplar and two *When in Rome* exemplars** because the two forms record the same things
  differently — most sharply the cadential six-four, `V(64)` in one and `i6/4` (with `III+6` as its
  rival) in the other, which is the DP-N flashpoint — and the session should meet both at the object.
- **Rival readings only exist in the *When in Rome* form.** The header row of five DCML harmonies
  tables (`K545-1`, `K545-2`, `K282-1`, `K280-2`; `ABC/n14op131_03`) carries no alternative-label column
  (three of the five carry a `special` column, which is not one), and no `label` cell in the five
  contains a hyphen; `tools/dcml_parser.py` handles no alternative either. Only `K545-1` and
  `n14op131_03` were read whole; the other three were read at the header and searched.
- **Chorales 001 and 003** are the ones the framework's §9 reading and the pilot already used. That is
  a cost (nothing new to the record) and a gain (the analyst's note the framework calls its most
  load-bearing evidence is met at the file, not as a quotation). A different chorale pair would need its
  variants found first; every rival-reading claim here is checked.
- **K. 545/i** because it is short, in the sonata corpus's own annotation, and carries all four
  phenomena in the DCML form in one file.

## 5. The plain-score set of Ruling 15, unchanged (four files, all present at staging)

- `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` (1,701,770 bytes)
- `tools/dcml/bach_chorales/MS3/011 Jesu, nun sei gepreiset.mscx` (103,829 bytes)
- `tools/dcml/cpe_bach_keyboard/MS3/wq55n02a.mscx` (552,240 bytes)
- `tools/dcml/couperin_clavecin/MS3/02_second_prelude.mscx` (143,156 bytes)

The `l0-l1` brief's rule that the session does not read `<Harmony>` or `<StaffText>` in these four is a
brief matter, not settled here; for L2 the analyses are the point, so the brief will have to say which
files that rule still covers.

## 6. Three observations, stated and not acted on

1. **The route to the *When in Rome* files is the pilot's:** they sit eight folders below `C:\s\MS` and
   the bridge stages at most seven deep; the user connected
   `C:\s\MS\tools\dcml\when_in_rome\Corpus\Early_Choral\Bach,_Johann_Sebastian\Chorales` directly this
   session, as on 2026-08-22. The blind session's desktop must do the same (the harmony-boundary brief
   §8 (P3) already says so).
2. **`docs/score_inventory.md` (line 105) says each of its twelve sub-repositories has a `harmonies/`
   folder; the `bach_chorales` clone has none** (its folders are `MS3`, `measures`, `notes`, `reviewed`; its scores carry no
   `<Harmony>`). Evidence for the audit; the document is not corrected here.
3. **The DCML chorale files' `<StaffText>` numbers do not match the *When in Rome* numbers:** `001`
   reads `(BWV 269; R 030)` where `remote.json` says BWV 269; `003` reads `(BWV 153/3; R 005)` where
   `remote.json` says BWV 153.1, Riemenschneider 3. The music was matched at the points named in §3; what
   "R" denotes in the DCML text is not established here.

## 7. What this does not do

It stages nothing to any session, lifts no gate, writes no dispatch, and does not decide the brief's
text. Ruling 1's gate stands: no derivation before L2's slice of Task B (36 papers) is read, and none is
read. Nothing was measured over any score; the counts above are byte sizes and line numbers of the files
named.

*Provenance: Cowork, 2026-09-05. Every file above read with the file tools from a bridge-staged copy;
no shell touched the repository. Counts are of this file's own rows and of file sizes at staging.*
