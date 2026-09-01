# The 242 invisible notes in `wq55n02a.mscx` — what they are, established at the file (report, 2026-09-01)

> **STATUS: CLOSED ON THE RULED STOP FORM.** Executes
> `cc_instruction_invisible_notes_establishment_2026_09_01.md` whole. **Nothing was staged, nothing
> was selected, and no verdict on the file's suitability is offered.**
>
> **★ THE OUTCOME IN ONE SENTENCE.** The subject file matched its recorded size and digest exactly;
> all three counts re-established at the file (invisible **242**, non-sounding **5**, cue-sized
> **244**); the 242 invisible notes are **concentrated in 24 of the file's 84 bars, in six contiguous
> runs**, sit **only in voices 2 and 3 and never in voice 1**, are **never alone at their moment**,
> **never tied to anything**, and **every single one of the 242 has a visible note of the same pitch
> sounding at the moment it starts.**
>
> **★ THE PREDICTION THAT FAILED, STATED FIRST BECAUSE IT IS THE ONE THE WRITING SIDE ASKED TO BE
> ABLE TO CONTRADICT.** **P-2 is FALSIFIED as worded.** It predicted that a majority of the invisible
> notes have a visible partner **at the same tick** with the same pitch. **28 of 242 do — 12 %, not a
> majority.** The prediction's underlying idea nonetheless holds at a width it did not name: on the
> test *is a visible note of the same pitch SOUNDING when this invisible note starts*, the answer is
> **242 of 242**. Both tests are reported; the second is an ADDED count and does not replace the
> first.
>
> **★ AND TWO DEFECTS OF MY OWN, BOTH FOUND AND CORRECTED INSIDE THIS BATCH.** My first tie matcher
> read only the `<fractions>` half of a MuseScore `<location>` and ignored its `<measures>` half, so
> every tie crossing a bar line failed to match — 37 of 47. Corrected, **48 of 48 ties match**, and the
> correction turned the tie table into the independent validation of the tick arithmetic that Tasks
> 2(c) and 3(a) needed. The second was found by the standing self-check, in this report as first
> written: **an excerpt was labelled with a bar number I had inferred from the line's position in the
> file and never checked.** All three excerpt labels are now established by counting opening tags; §10
> counts it.

---

## 0. Boot — performed

The ordinary session-start read was performed in full before any other act; a single-file opening
instruction is not an exemption (ratified 2026-08-29, P-1, `CLAUDE.md` Conventions).

1. `CLAUDE.md` whole (all 1,864 lines); `DECISIONS.md` whole (all 862 lines); `STATUS.md` whole; the
   derived gating answer at `tools/audit/nongating_apparatus_rows.json` →
   `★_the_live_gating_answer` → `gating_ids`.
2. `BUILD_AND_TEST.md` — **condition MET and read whole.** This batch wrote and ran a Python script.
3. `docs/score_inventory.md` — **whole. Hard rules 2 and 3 bind and both are honored:** no snapshot
   source and no pin was touched — the subject file is not among the eleven — and no command names
   `"tools/extra scores"`, that tree being outside this batch's scope.
4. `cowork_rulings_2026_08_31_decision_surface_sitting.md` **§3o (Ruling 15), §3u, §3v, §3aa, §3ab
   (Ruling 21) and §3ac (Ruling 22)** — each read whole. §3ac is the authority for this batch.
   **Under §3ab the word *bar* is used in this report only for the metric unit; the excluding sense
   is written *exclude*.**
5. `cc_slot_sweep_report_2026_09_01.md` — whole.
6. This batch's dispatch, whole.

Read additionally, because the work required grounding rather than recall: `tools/audit/gen_score_tags.py`
whole, which is where §1's third bullet is answered, and the row of
`tools/audit/score_tags_l0l1_sweep.json` for the subject file.

---

## 1. Task 0 — the pins

Taken with `git hash-object -w` before any other act, **and re-taken at the close. All nine reproduced
exactly**, so no read disagreed with its pin.

| File | Pin (blob sha1) | Re-verified at close |
|---|---|---|
| `CLAUDE.md` | `e012d3f2adc10e4557bf422236f0d50014559568` | identical |
| `DECISIONS.md` | `238cff78e61d4ff4cd8e5a41dc17f6fab4ab7d59` | identical |
| `STATUS.md` | `a9163ead8ade542c67cde43bf611e30477e0459b` | identical |
| `tools/audit/nongating_apparatus_rows.json` | `a2ca9f64783d45a50bd3fb299d46afe46b9fe678` | identical |
| `BUILD_AND_TEST.md` | `42df316140c8bf178b620b461b84fadacb976299` | identical |
| `docs/score_inventory.md` | `4de7d6986614d876796bc75aed473c6ce3bf92c4` | identical |
| `cowork_rulings_2026_08_31_decision_surface_sitting.md` | `d4be3385f38c0c7fd0cd068669c568f8216b4eac` | identical |
| `cc_slot_sweep_report_2026_09_01.md` | `088bddad08cd466db1ef06631ab042bc5c7de2b4` | identical |
| `cc_instruction_invisible_notes_establishment_2026_09_01.md` | `e8ee29fc8075ff5b03d62e6d329f33f8a18f7ae2` | identical |

**Seven of these nine files were pinned by the preceding batch too, and six of the seven are
byte-identical to its recorded pins.** The seventh, the sitting record, moved `88997004…` →
`d4be3385…`, **which is expected and is named in this dispatch's own provenance**: it has since gained
§3aa, §3ab and §3ac. The remaining two carry no earlier pin — the sweep report was created by the
preceding batch and not pinned by it, and this dispatch is new. **No read disagreed with its own pin
inside this batch, so that STOP was not met.**

## 1a. Task 1 — the start state, established before anything rested on it

### The subject file is the object the sweep measured — both required values match

| Required by §1 | Measured this batch | Match |
|---|---|---|
| 552,240 bytes | **552,240** | yes |
| the `sha256` the sweep table records | **`28f9b09548b46ec71328fcbb938024ad1a5222f2340cbf3717151162e3ab02d4`** | yes |

The sweep's recorded digest for
`tools/dcml/cpe_bach_keyboard/MS3/wq55n02a.mscx` is the same string, read at
`score_tags_l0l1_sweep.json` → the row at that path. **The §8 STOP was not met.**

### The six counts, re-established at the file

Recomputed from the file with the generator's own definitions, not read across from the table:

| Count | Sweep table | Re-established | Match |
|---|---:|---:|---|
| `notes_invisible` | 242 | **242** | yes |
| `notes_non_sounding` | 5 | **5** | yes |
| `cue_sized_small` | 244 | **244** | yes |
| `chords` | 1,140 | **1,140** | yes |
| `measures` (`<Measure>` elements) | 168 | **168** | yes |
| `body_staves` | 2 | **2** | yes |

**No divergence on any of the six.** Corroborating values from the same pass, none of which the
dispatch required: `<Note>` **1,290**, `<Harmony>` **167**, `<StaffText>` **13**, part-list staves
**2**, `<Division>` **480** ticks per quarter, `programVersion` **3.6.2**.

### What each of the three counts actually counts, read at `tools/audit/gen_score_tags.py`

**This matters more than it looks, and the dispatch says so.** The three terms are pinned to what the
script measured before anything is inferred from them. The generator's own lines:

**`notes_invisible`** — the loop is over `<Note>` elements and the test is on a **child element**,
with the attribute form counted beside it so its absence is established rather than assumed:

```python
    # Invisibility is a <visible>0</visible> CHILD element in this format, not a
    # visible="0" attribute. Both forms are counted so the absent one is visible
    # as absent rather than assumed away.
    notes_invisible = 0
    notes_non_sounding = 0
    for note in root.iter("Note"):
        vis = note.find("visible")
        if vis is not None and _text(vis) == "0":
            notes_invisible += 1
        if note.get("visible") == "0":
            notes_invisible += 1
```

So `notes_invisible` counts **`<Note>` elements carrying a `<visible>` child whose stripped text is
exactly `0`**. **In this file the attribute form contributes nothing:** `visible_attribute_form_seen`
is `false`, re-established here, which reproduces the sweep's finding that the attribute form appears
in zero of 648 files.

**`notes_non_sounding`** — the same loop, a different child:

```python
        play = note.find("play")
        if play is not None and _text(play) == "0":
            notes_non_sounding += 1
```

So it counts **`<Note>` elements carrying a `<play>` child whose stripped text is exactly `0`**.

**`cue_sized_small`** — and this one is **not** a count of notes:

```python
    row["cue_sized_small"] = n("small")
    row["cue_sized_small_parents"] = dict(sorted(small_parents.items()))
```

`n(tag)` reads the file's whole element-tag histogram, so `cue_sized_small` is **the number of
`<small>` elements ANYWHERE in the file**, whatever their parent. **The parents are published beside
it and in this file they are `Note` 239 and `Chord` 5** — re-established here at both values. **So
"244 cue-sized notes" is 239 cue-sized notes plus 5 cue-sized chords**, and §3(b) below is answered at
both levels rather than at the loose reading.

### ★ A definitional divergence the dispatch's own wording contains, reported and not resolved by me

**§2(a) asks how many of "the file's 168 bars" contain an invisible note. The file does not have 168
bars. It has 84.** `measures` is the count of `<Measure>` **elements**, and this file has two staves,
each carrying its own 84 `<Measure>` elements — 84 × 2 = 168. Re-established: `<Measure>` elements per
staff, staff 1 **84**, staff 2 **84**.

**Both readings are therefore answered below and neither is folded into the other**: 24 of the **84
bars**, and 31 of the **168 `<Measure>` elements**. This is a divergence from the dispatch's wording,
which §8 makes a reportable matter and not a STOP. It is the same shape as the two column corrections
the preceding batch reported: it ADDS a count and removes none.

### ★ The tick arithmetic, positively established before Tasks 2(c) and 3(a) rested on it (#19)

Two of the questions below — *does an invisible note ever stand alone at its moment*, and *is there a
visible note at the same tick* — cannot be answered without a position for every note. A position is
computed, not read off the file, so it is an instrument and had to be established rather than trusted.

**The first walk flagged 49 voices that do not fill their bar, and 40 survive in the corrected walk.**
Read at the objects, **every one of them is a TRAILING gap** — a voice whose last element ends before
the bar line, with nothing after it. A trailing gap cannot move any position, because positions
accumulate forward from the start of the bar. An *interior* gap could, and MuseScore writes an
explicit `<location>` for one, which this walk consumes.

**But that reasoning is an argument, and #19 asks for a positive establishment, so one was run.**
Every spanner in this file states the distance to its own other end as a `<location>` pair,
`<measures>` and `<fractions>`. Resolving that distance with this walk's own bar starts and in-bar
positions must land exactly on the element carrying the matching end. A wrong bar length, a missed
interior gap or a mishandled tuplet would break the landing.

**160 spanner starts; 159 land exactly. The single miss is explained at the object and is not a tick
error:** at staff 2 bar 23 the slur's other end sits on a `<Rest>`, and my end-collector scanned only
`<Chord>` and `<Note>`. Counting rests, the figure is 160 of 160. **Taken by kind: Tie 48 of 48, Slur
111 of 112 (112 of 112 with the rest included).** The 48 ties are the sharper half of the test,
because each also pins a pitch and most cross a bar line.

**What this establishes and what it does not.** It establishes that the bar starts, in-bar positions,
tuplet scaling and `<location>` handling reproduce the file's own stated distances everywhere the file
states one. It does not establish that a position is correct where the file states no distance; there,
the trailing-gap argument above is what carries it, and it is stated as an argument.

### The tracked-modification shape

**★ THE STANDING SHELL-READ GUARD REFUSED `git status --porcelain`, EXACTLY AS §1 ANTICIPATES.** Its
message named **D-253** and its sanctioned substitute, `python tools/audit/changed_paths.py`. That
substitute was used and the shape below is its output. **The guard chose the route, not my judgment.**

**Exactly four tracked-and-modified paths, and no others:**

```
 M	FRAMEWORK.md
 M	cowork_rulings_2026_08_31_decision_surface_sitting.md
 M	tools/audit/derivation_boot_pack.json
 M	tools/audit/gen_derivation_boot_pack.py
```

**All four are the four §9 names, in the same order, and there is no fifth, so the §9 STOP was not
met.** **872 changed-path records: 4 tracked-modified and 868 untracked.** §9's other expectations
also hold — `tools/audit/derivation_exemplars/`, `tools/audit/gen_score_tags.py` and
`tools/audit/score_tags_l0l1_sweep.json` all stand as untracked records, being the two preceding
batches' products.

---

## 2. Task 2 — where the invisible notes sit

### (a) They are concentrated in six contiguous runs, not spread

**24 of the file's 84 bars carry at least one invisible note — 29 %.** Read as `<Measure>` elements,
**31 of 168**.

**The bar numbers, as ranges:** **21–25 · 36–40 · 44–47 · 65 · 72–76 · 81–84.**

**Per staff.** Staff 1 (the upper): bars 21–25, 36–40, 44–46, 65, 72–76 — **19 bars, 162 notes**.
Staff 2 (the lower): bars 22, 23, 37, 38, 46, 47, 73, 74, 81–84 — **12 bars, 80 notes**. Seven bars
carry invisible notes in both staves.

**They are gathered, not spread.** Six runs over an 84-bar piece, the longest five bars, and the
densest single bar carrying 20 of the 242. The count per bar:

| Bar | 21 | 22 | 23 | 24 | 25 | 36 | 37 | 38 | 39 | 40 | 44 | 45 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Invisible notes | 6 | 14 | 13 | 8 | 4 | 6 | 14 | 15 | 10 | 6 | 16 | 8 |

| Bar | 46 | 47 | 65 | 72 | 73 | 74 | 75 | 76 | 81 | 82 | 83 | 84 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Invisible notes | 14 | 20 | 4 | 7 | 15 | 15 | 10 | 10 | 4 | 9 | 8 | 6 |

The twenty-four figures sum to **242**, which is the whole population — no invisible note falls
outside this table.

**One qualification on the bar numbers.** They are POSITIONAL `<Measure>` indices within a staff,
1-based. **Four measures carry `<irregular>`** — staff 1 bars 81, 82, 83 and 84 — so a bar number
printed by MuseScore may differ from the positional index at the end of the piece. Both staves hold 84
`<Measure>` elements, so the indices are aligned between the staves throughout.

### (b) The split by staff and by voice — never voice 1

| Staff | Voice 1 | Voice 2 | Voice 3 | Voice 4 | Invisible total |
|---|---:|---:|---:|---:|---:|
| 1 | **0** | 146 | 16 | **0** | **162** |
| 2 | **0** | 38 | 42 | — | **80** |

For contrast, the same split over all 1,290 notes of the file:

| Staff | Voice 1 | Voice 2 | Voice 3 | Voice 4 | All notes |
|---|---:|---:|---:|---:|---:|
| 1 | 595 | 208 | 21 | 6 | 830 |
| 2 | 341 | 69 | 50 | — | 460 |

**Not one invisible note is in voice 1 of either staff.** Voice 1 holds 936 of the file's 1,290 notes
and none of them is invisible.

**A sharper unit, because it reconciles the population exactly.** Taking one unit as *one `<voice>` of
one `<Measure>` of one `<Staff>`*, the file has **231 units holding at least one note**. Of those:

- **196 hold no invisible note at all.**
- **33 hold nothing but invisible notes** — 235 notes between them.
- **2 are mixed**, and they are named: staff 1 bar 46 voice 2 (5 notes, 4 invisible) and staff 2 bar 23
  voice 2 (4 notes, 3 invisible) — 7 invisible notes between them.

**235 + 7 = 242**, and **196 + 33 + 2 = 231**. Both reconcile, so no unit and no note is unaccounted.

### (c) They are never alone at their moment — the answer is zero, and it is not a near miss

**There is no tick in this file at which every sounding note is invisible. The count of such moments
is 0.**

The test, stated so it can be disagreed with: for each of the **197 distinct onset ticks** at which an
invisible note begins, take every note whose own span `[onset, onset + duration)` contains that tick,
across both staves and all voices, and ask whether any of them is visible. **At every one of the 197,
at least one is.**

It is not a near miss. The number of **visible** notes sounding at an invisible note's onset:

| Visible notes sounding | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| Invisible notes at such a tick | 23 | 182 | 5 | 30 | 2 |

The five columns sum to **242**. The minimum over the whole population is **one**, never zero.

### (d) None of them is tied to anything — so none is tied to a visible note

**The answer is 0, and it is 0 by a wider fact:** **not one of the 242 invisible notes carries a tie
endpoint of any kind**, start or end.

The file holds **48 tie spanners**, all matched to their partners (see the tick establishment above).
**All 48 join two visible notes.** Both-invisible pairs: **0**. Mixed pairs: **0**. The 95 notes
carrying a tie endpoint are all visible.

### (e) Three verbatim excerpts, quoted as the XML stands

**First appearance in the file** — `wq55n02a.mscx` lines 2374–2389, staff 1, bar 21, voice 2. This is
the first invisible note in the file, and it is also one of the five that carry `<play>0</play>`:

```xml
          <Chord>
            <BeamMode>no</BeamMode>
            <durationType>16th</durationType>
            <Articulation>
              <subtype>articStaccatoAbove</subtype>
              <anchor>0</anchor>
              </Articulation>
            <noStem>1</noStem>
            <Note>
              <visible>0</visible>
              <pitch>67</pitch>
              <tpc>15</tpc>
              <small>1</small>
              <play>0</play>
              </Note>
            </Chord>
```

**Middle of the file** — lines 10553–10573, **staff 1, bar 73, voice 2** (the staff, bar and voice
established by counting the opening tags that precede the line, not inferred from its position in the
file), showing two of the `<Segment>` spacing elements that surround these chords:

```xml
          <Segment>
            <leadingSpace>0.153392</leadingSpace>
            </Segment>
          <Chord>
            <BeamMode>no</BeamMode>
            <durationType>32nd</durationType>
            <Articulation>
              <subtype>articStaccatoAbove</subtype>
              <anchor>0</anchor>
              </Articulation>
            <noStem>1</noStem>
            <Note>
              <visible>0</visible>
              <pitch>60</pitch>
              <tpc>14</tpc>
              <small>1</small>
              </Note>
            </Chord>
          <Segment>
            <leadingSpace>0.153392</leadingSpace>
            </Segment>
```

**Last in the file** — lines 18484–18505, staff 2, bar 84, voice 3. It is the final invisible note of
the 242 and the last `<Chord>` of the piece; the excerpt runs past ten lines because the slur spanner
sits inside the chord and cutting it would hide the context:

```xml
          <Chord>
            <BeamMode>no</BeamMode>
            <durationType>16th</durationType>
            <Spanner type="Slur">
              <prev>
                <location>
                  <fractions>-3/8</fractions>
                  </location>
                </prev>
              </Spanner>
            <Articulation>
              <subtype>articStaccatoBelow</subtype>
              <anchor>1</anchor>
              </Articulation>
            <noStem>1</noStem>
            <Note>
              <visible>0</visible>
              <pitch>48</pitch>
              <tpc>14</tpc>
              <small>1</small>
              </Note>
            </Chord>
```

---

## 3. Task 3 — what the invisible notes are, tested against what would distinguish them

### (a) The duplication test, at the width the dispatch names and at two wider ones

**The dispatch's test, exactly as worded: is there a visible note at the same tick with the same
pitch, anywhere in the file?**

| | Count |
|---|---:|
| Invisible notes | **242** |
| **With** a visible note at the same tick and the same pitch | **28** |
| **Without** one | **214** |

**Where the 28 partners sit:** **all 28 in the same staff, in a different voice.** Same staff and same
voice: **0**. Other staff: **0**. The three classes sum to 28, so the classification reconciles. The
28 fall in bars 21–25, 36–40, 65 and 73–76.

**★ TWO WIDER TESTS ARE ADDED BESIDE IT, BECAUSE THE EXACT TEST ANSWERS A NARROWER QUESTION THAN THE
ONE THE DISPATCH SAYS IT IS FOR.** The dispatch's stated purpose is *"A note written twice, once
visibly and once not, is a different thing from a note written once and hidden."* A note written twice
against a **held** note shares the held note's pitch without sharing its onset, and the exact test
cannot see that. **Neither added test replaces the ordered one; both ADD a count.**

| Test | With a partner | Without |
|---|---:|---:|
| **1.** A visible note at the **same onset tick**, same pitch (the ordered test) | 28 | 214 |
| **2.** A visible note of the **same pitch SOUNDING** at that tick | **242** | **0** |
| **3.** A visible note of the same **pitch class** sounding at that tick | 242 | 0 |

**Every one of the 242 invisible notes has a visible note of the same pitch sounding at the moment it
starts, and in every case that visible note is in the same staff in a different voice.** Tests 2 and 3
give the same figure, so the pitch-class relaxation adds nothing: the match is at the exact pitch,
never merely at the octave.

**Verified at the object rather than taken from the table (#15).** At staff 1 bar 21, voice 1 carries a
visible quarter note at pitch 67, tied forward. Voice 2 of the same bar opens with
`<location><fractions>1/4</fractions></location>` — the same position — then a `<Tuplet>` of
`normalNotes` 4 / `actualNotes` 6 over `baseNote` 16th, whose six 16th notes are all pitch 67,
invisible, `<small>`, `<noStem>`, staccato. Six 16ths at 4/6 scaling occupy 480 ticks, which is exactly
the visible quarter note's 480. Bar 21's invisible count is 6, which is that tuplet and nothing else.

### (b) The overlap with the cue-sized notes — they are very nearly the same notes

**Answered at both levels, because `cue_sized_small` counts `<small>` anywhere and not only on notes.**

At **note** level — `<small>` as a child of `<Note>`, 239 of them:

| | Count |
|---|---:|
| Invisible **and** cue-sized | **237** |
| Invisible but **not** cue-sized | **5** |
| Cue-sized but **not** invisible | **2** |

At **chord** level, the remaining 5 of the 244: **all five `<small>` elements on a `<Chord>` sit on
chords whose only note is invisible**, and those five notes are exactly the five that carry no
note-level `<small>`. **So all 242 invisible notes are cue-sized, at one level or the other**, and the
244 `<small>` elements divide as **242 attached to invisible notes and 2 attached to visible ones**.

**The two visible cue-sized notes are named, because they are the whole of the difference:** they are
the single visible note in each of the two mixed units of §2(b) — staff 1 bar 46 voice 2 and staff 2
bar 23 voice 2. **Both sit on a chord carrying `<noStem>`**, exactly as the invisible ones do; over the
file's 1,048 visible notes, only these two carry `<small>` and only these two sit on a stemless chord.

### (c) The five non-sounding notes are a subset of the 242

**All five `<Note>` elements carrying `<play>0</play>` are invisible.** None is visible. Each is also
cue-sized. They sit at:

| Staff | Bar | Voice | Pitch | Duration |
|---|---:|---:|---:|---|
| 1 | 21 | 2 | 67 | 16th |
| 1 | 22 | 2 | 67 | 16th |
| 1 | 23 | 2 | 67 | 16th |
| 1 | 36 | 2 | 62 | 16th |
| 1 | 37 | 2 | 62 | 16th |

**The two facts L0's contract keeps separate do come apart in this file, but in one direction only.**
Every non-sounding note is invisible; **237 invisible notes sound and are not visible**, and **no note
is non-sounding while visible**. Of the file's 1,290 notes, 1,048 are visible and sounding, 237 are
invisible and sounding, 5 are invisible and non-sounding, and 0 are visible and non-sounding. The four
cells sum to 1,290.

### (d) What they look like as music — counts only, no interpretation

**Durations.** Every one is un-dotted; the `<dots>` count is 0 for all 242.

| Written duration | 16th | 32nd | 64th |
|---|---:|---:|---:|
| Invisible notes | 105 | 107 | 30 |

In ticks (480 per quarter), which separates the tuplet members: **120** ticks ×75, **80** ticks ×30,
**60** ticks ×107, **30** ticks ×30. **30 of the 242 lie inside a tuplet**; 212 do not, and the 30 are
all written 16ths, sounding 80 ticks. **The file holds 13 `<Tuplet>` elements and every one of them
scales by two thirds** — five written `normalNotes` 4 / `actualNotes` 6 on a 16th base, six 2 / 3 on a
16th base, two 2 / 3 on a 32nd base — so a 16th inside any of them is 80 ticks, which is where the 30
sit. **Which of the thirteen carry them is not established here and is not claimed.**

**Ornaments and other articulations on their chords.** **239 of the 242 sit on a chord carrying at
least one `<Articulation>`;** 3 do not.

| Articulation subtype on the chord | Count |
|---|---:|
| `articStaccatoAbove` | 187 |
| `articStaccatoBelow` | 51 |
| `ornamentMordent` | 1 |

The three subtype counts sum to 239, which is also the number of invisible notes sitting on a chord
that carries any articulation, so **each such chord carries exactly one**. **One ornament articulation
in the whole population**, against 238 staccato marks. The `<anchor>` values on those articulations:
`0` ×145, `1` ×26, `4` ×12, `3` ×8 — **191 in all, so the remaining 48 articulations carry no
`<anchor>` child.**

**Accidentals.** **Not one of the 242 carries an `<Accidental>` child.** For contrast, 97 of the
file's 1,048 visible notes do.

**Ties.** **0 tie starts and 0 tie ends**, as §2(d) records.

**Other note-level and chord-level marks.**

| Mark | Invisible notes carrying it | Visible notes carrying it |
|---|---:|---:|
| `<small>` on the `<Note>` | 237 | 2 |
| `<small>` on the `<Chord>` | 5 | 0 |
| `<noStem>` on the `<Chord>` | **242** | 2 |
| `<head>` on the `<Note>` | 16 (all `cross`) | 0 |
| `<Accidental>` on the `<Note>` | 0 | 97 |
| grace marker on the `<Chord>` | 0 | — |

**Every one of the 242 sits on a stemless chord.** None is a grace note.

**Pitches.** 21 distinct pitches, from MIDI 40 to 81. The commonest are 60 ×52, 62 ×43, 67 ×38, 51 ×15,
63 ×15, 79 ×12; the remaining fifteen pitches account for 67 between them. The 242 sit at **241
distinct staff-voice-tick positions**, so exactly one chord carries two of them and every other carries
one.

**★ ONE CATEGORY THAT IS NOT A NOTE, REPORTED RATHER THAN DROPPED (DT-26).** The file holds **264
`<visible>` elements and every one of them reads `0`**. They divide by parent as **`Note` 242, `Rest`
19, `NoteDot` 2, `Tempo` 1**. So invisibility is used in this file on nineteen rests and one tempo
marking as well as on the notes. **Ten of the nineteen invisible rests are whole-bar rests in voice 1**
— staff 1 bars 82–84, staff 2 bars 14, 34, 59–63 — and the rest are shorter rests in voices 1 and 2.
The 242 + 19 + 2 + 1 sum to the 264 the element histogram holds, so nothing in the `<visible>`
population is unaccounted.

---

## 4. Task 4 — the corpus context, from the sweep table and not by re-reading scores

Every figure here is a field of `tools/audit/score_tags_l0l1_sweep.json`. **No score was re-read for
this section.**

**Of the 66 `.mscx` files in `tools/dcml/cpe_bach_keyboard/MS3`, 11 carry at least one invisible note
and 55 carry none.** What each of the eleven carries:

| File | Invisible notes | Non-sounding | `<small>` | Notes in the file |
|---|---:|---:|---:|---:|
| `wq55n02a.mscx` | **242** | 5 | 244 | 1,290 |
| `wq50n03a.mscx` | 10 | 0 | 20 | 2,203 |
| `wq55n02b.mscx` | 3 | 1 | 5 | 751 |
| `wq57n06b.mscx` | 3 | 0 | 6 | 854 |
| `wq57n03.mscx` | 2 | 0 | 3 | 1,566 |
| `wq50n01c.mscx` | 1 | 0 | 0 | 1,175 |
| `wq50n03c.mscx` | 1 | 0 | 2 | 773 |
| `wq55n04b.mscx` | 1 | 1 | 0 | 819 |
| `wq55n04c.mscx` | 1 | 1 | 1 | 1,558 |
| `wq56n06a.mscx` | 1 | 0 | 2 | 512 |
| `wq57n06c.mscx` | 1 | 0 | 2 | 911 |

**242 is not the top of a range within its own corpus; it is an outlier by a factor of about
twenty-four.** The second-placed file carries 10, and eight of the eleven carry one or two. The whole
corpus's invisible notes number 266, of which this one file holds 242.

**Non-sounding notes in the same 66 files:** five files carry any, and only `wq55n02a` carries more
than one — 5 against one each in `wq55n02b`, `wq55n04b`, `wq55n04c` and `wq55n06a`.

**★ AND ONE OF THOSE FIVE CARRIES A NON-SOUNDING NOTE WITH NO INVISIBLE NOTE AT ALL.** `wq55n06a.mscx`
appears in the non-sounding list and **not** in the eleven-file invisible list, so its `<play>0</play>`
note is a **visible** one. **That is the opposite direction from the one this file shows** — here every
non-sounding note is invisible — and it is worth recording because §3(c)'s point is that L0's contract
holds *sounds* and *is visible* apart. **Read from the table only; that score was not opened, and no
claim is made about it beyond the two counts its row carries.**

**★ THIS IS CONTEXT AND NOT A CRITERION.** Ruling 20's fourth bound holds: a whole-corpus count says
what the corpora cannot exercise and **must not be used to pick or reject an exemplar**. The numbers
are reported; **no conclusion is drawn from frequency here, and none is offered.**

---

## 5. Task 5 — the thirteen `<StaffText>` items, quoted verbatim

**All thirteen, in file order. Eleven are the string `ten.` and two are a symbol reference.**

| # | Staff | Bar | The `<text>` content, verbatim |
|---:|---:|---:|---|
| 1 | 1 | 14 | `<sym>accidentalNatural</sym>` |
| 2 | 1 | 26 | `<sym>accidentalNatural</sym>` |
| 3 | 1 | 59 | `ten.` |
| 4 | 1 | 60 | `ten.` |
| 5 | 1 | 78 | `ten.` |
| 6 | 2 | 5 | `ten.` |
| 7 | 2 | 8 | `ten.` |
| 8 | 2 | 17 | `ten.` |
| 9 | 2 | 21 | `ten.` |
| 10 | 2 | 27 | `ten.` |
| 11 | 2 | 32 | `ten.` |
| 12 | 2 | 36 | `ten.` |
| 13 | 2 | 72 | `ten.` |

**The two symbol items in full, because their `<text>` is not a literal string:**

```xml
          <StaffText>
            <minDistance>-2.61403</minDistance>
            <offset x="4.49951" y="-2.94297" />
            <text><sym>accidentalNatural</sym></text>
            </StaffText>
```

```xml
          <StaffText>
            <minDistance>-3.18141</minDistance>
            <offset x="0.511307" y="-2.84046" />
            <text><sym>accidentalNatural</sym></text>
            </StaffText>
```

A representative `ten.` item in full — the three in staff 1 additionally carry
`<placement>below</placement>`; the eight in staff 2 do not:

```xml
          <StaffText>
            <placement>below</placement>
            <text>ten.</text>
            </StaffText>
```

**What this is and is not.** **None of the thirteen is a Roman numeral, a chord symbol or any other
analysis annotation.** Eleven are a performance direction and two are a symbol reference to a natural
sign. **This batch takes no view on whether that makes the `<StaffText>` exclusion unnecessary** — the
dispatch says in terms that the strings are reported and the question is the user's, and §3aa's
plainness repair is in any case still unruled. It is worth setting one fact beside them, since it bears
on the same instruction and is re-established above: **the file also carries 167 `<Harmony>` elements**,
which the exclusion's other half names.

---

## 6. The four predictions, marked with the observed value

**Each is marked held or falsified against what was measured. A falsified prediction is recorded as
falsified and is not repaired into a success.**

**P-1 — the invisible notes are concentrated, not spread; they fall in a minority of the bars.
✅ HELD.** **24 of 84 bars — 29 %** (31 of the 168 `<Measure>` elements — 18 %). They fall in **six
contiguous runs**, the longest five bars long, and the five densest bars hold 81 of the 242 between
them. A minority on either reading of the denominator.

**P-2 — a majority have a visible partner at the same tick and pitch. ❌ FALSIFIED as worded.**
**28 of 242 — 12 %.** 214 have no visible note at the same onset tick with the same pitch.
**The prediction's idea survives at a width it did not state, and this is recorded beside the
falsification rather than in place of it: on the test *is a visible note of the same pitch SOUNDING at
that moment*, the answer is 242 of 242.** The prediction named the exact onset, and the exact onset is
what the measurement refutes.

**P-3 — the invisible notes and the cue-sized notes are largely the same notes. ✅ HELD, and more
tightly than "largely".** At note level **237 of 242** invisible notes are cue-sized, and **237 of 239**
cue-sized notes are invisible. Counting the five chord-level `<small>` elements, **all 242 invisible
notes are cue-sized** and the only two cue-sized notes that are not invisible are the two named in
§3(b).

**P-4 — the five non-sounding notes are a subset of the 242 invisible ones. ✅ HELD.** **5 of 5.** None
is visible.

**No prediction of my own about what the notes mean is added**, as the dispatch directs.

---

## 7. Divergences and observations — reported rather than resolved

**None is a STOP, and none changes this batch's outcome.**

1. **The 168-versus-84 bar count of §1a.** The dispatch's §2(a) speaks of "the file's 168 bars"; 168 is
   the `<Measure>` element count over two staves and the file has 84 bars. Both are answered and
   neither is folded into the other.

2. **★ A DEFECT OF MINE, FOUND INSIDE THIS BATCH AND CORRECTED THERE.** My first tie matcher read only
   the `<fractions>` half of a MuseScore `<location>` and ignored `<measures>`, so all ten ties
   crossing a bar line failed to match — 37 of 47, with the ten reported as unmatched. **Every one of
   the ten carried `measures: 1`, which is what named the cause.** Corrected: **48 of 48**. The same
   correction made the spanner-distance check into the tick establishment §1a rests on, so the defect
   is what produced the check.

3. **The one unmatched spanner is not a tick error.** At staff 2 bar 23 a slur ends on a `<Rest>`,
   which my end-collector did not scan. Established at the object; counting rests the figure is 160 of
   160. **Named rather than folded in, because a check that quietly matches everything establishes
   nothing.**

4. **The shell-read guard fired three times and every refusal was taken as routing.** **(i)** It
   refused `git status --porcelain`, naming **D-253** and its substitute
   `tools/audit/changed_paths.py`, which was used. **(ii)** It refused an `awk` over a file in the
   session scratchpad — **a path outside the repository**, matched on the file's name — naming D-253
   again; the file tools were used instead, which is the sanctioned route in any case. **(iii)** It
   refused a `python -c` whose code string carried a literal repository path, naming D-253 and the
   **guard-family ruling of 2026-08-08**; the same enumeration was then taken with `Grep`. **No figure
   in this report depends on any refused command**, and each refusal cost only the route, not the
   answer. **The second is recorded because the guard's reach beyond the repository is a fact about the
   guard that was not on the record here**; the third is the guard behaving exactly as its own ruling
   describes.

   **★ AND MY OWN THREE PROBE SCRIPTS TAKE THE SCORE PATH AS AN ARGUMENT, WHICH IS THE FORM THE GUARD
   ADMITS AND IS ITS DECLARED CEILING RATHER THAN A LICENCE.** I record having relied on it, as the
   preceding batch recorded the same reliance, instead of letting the pass go unremarked. The scripts
   are files invoked by path, not code strings, which is the form the guard's own substitute takes.

5. **`<Segment>` elements appear inside the voice stream** of the passages carrying invisible notes —
   13 in the file, each holding a `<leadingSpace>` — and they are visible in the middle excerpt.
   **They carry no duration and this walk consumes none**; they are named so a reader of the excerpt
   is not left wondering whether something was skipped.

6. **The four `<irregular>` measures are all in staff 1, bars 81–84**, and staff 2's corresponding
   measures carry no such element. It is reported because bars 81–84 carry invisible notes in staff 2,
   so the positional index is what this report uses throughout. **No causal claim is made about the
   asymmetry.**

---

## 8. STOPs

**No STOP of §8 was met.**

| STOP | Met? |
|---|---|
| The subject file's size or `sha256` not matching §1 | **No** — 552,240 bytes and the recorded digest both reproduced |
| A read disagreeing with its pin | **No** — all nine pins re-taken at the close and all nine reproduced |
| Writing anywhere outside this batch's report | **No** — see the footprint |
| Any act outside §9 | **No** — see the footprint |

**The "not a STOP, reported rather than resolved" cases:**

| Case | Occurred? |
|---|---|
| A count diverging from the sweep table | **No** — all six reproduced exactly |
| A prediction falsified | **Yes, one** — P-2; §6 |
| The shell-read guard refusing a command | **Yes, three times** — §7.4 |
| A category that turns out not to apply | **Yes** — §2(d): no invisible note carries a tie endpoint at all, so the invisible-tied-to-visible category is empty by a wider fact than "none found" |

---

## 9. The footprint, as executed

**Created — one object inside the repository and nothing else: this report.**

**Edited: NOTHING.** **No score was edited, renamed, moved, converted, copied or re-saved, and no
score was written anywhere** — `wq55n02a.mscx` was read only, and read only through the file tools and
through a read-only script that opens it, parses it and closes it. **Nothing was staged.** **The
Couperin fallback file was not touched, not opened and not read.** No registry, manifest or pin was
touched; `tools/audit/score_tags_l0l1_sweep.json` and `tools/audit/gen_score_tags.py` were **read
only** and neither was edited or regenerated. `.gitattributes` was **not** edited — that question
stays owed to the user (§3y).

**Not done at all:** no build, no test, no golden, **no measurement of the analysis** — every count in
this report is a property of a score file as written, and none is an output of this project's analyzer;
nothing under `tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; **no boot pack rendered and
neither frozen pack opened**; **no governing document amended**; **no open-items row created, flipped
or discarded**; **no decisions-register entry and no `D-NNN`** — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route; the workbook not opened; **no score
selected and no score staged**; **no brief written or amended** — the brief's two stale passages stay
owed; no session booted.

**The temporary scripts are outside the repository**, in the session scratchpad, as §9 permits: **five
of them** — three read-only probes over the score, one that dumps a single `<Measure>` as raw XML, and
one that maps a raw line number to its staff, bar and voice — plus their output files. **Every one is
read-only over the score and none writes anywhere but the scratchpad. Nothing was written inside the
repository except this report.**

**The tracked-modification shape at the close is identical to the start state, measured and not
asserted** — the same four tracked-and-modified paths, in the same order, and no fifth. Changed-path
records: **872 at the start and 873 at the close**, the one added record being
`?? cc_invisible_notes_establishment_report_2026_09_01.md`. **This batch modified nothing tracked and
created nothing untracked inside the repository except this report.**

---

## 10. The standing self-check

Run before this report was written, on the work actually on disk rather than on the intention.

**The diff on disk, read rather than remembered.** Inside the repository the diff is one new file:
this report, which was re-read in full on disk after it was written and not from the memory of writing
it. Outside the repository, five scripts and their outputs in the scratchpad. **No repository file was
modified, so there is no edit to re-read against the principles — the check is therefore of this
report's own claims and of the scripts that produced them.**

**Against the principles.** **#15 — verified at objects, not at assertions.** The pins at the blobs;
the file's size and digest at the file; the three counts recomputed from the file rather than read
across from the table; the exact-partner case and its 6:4 tuplet at staff 1 bar 21 read in the raw XML;
the mixed unit at staff 2 bar 23 read in the raw XML; the offset 64th-note voice at staff 1 bar 44 read
in the raw XML; the three excerpts quoted from the file itself, each located to its staff, bar and voice
by counting opening tags rather than by inferring from its position in the file. **#19 — the tick arithmetic is an instrument
and was positively established**, by resolving all 160 of the file's own stated spanner distances, not
merely left unfalsified; and the one miss was traced to my collector rather than waved through.
**#17(f) / D-431 — no figure is transcribed from a prior record.** Every count is either recomputed
here or cited to a field of `tools/audit/score_tags_l0l1_sweep.json`, and the figures the dispatch
relayed were re-established at the file. **No figure of this project's own analysis measurement appears
anywhere in this report.** **#13 — the surprises are surfaced, not built around:** the falsified
prediction, my two defects, the bar-count divergence and all three guard refusals are each reported at
the point they arose. **#12 — nothing is folded into anything:** the exact and the sounding
duplication tests are both carried, both cue-size levels are carried, and the 19 invisible rests and 2
invisible note-dots are reported rather than dropped for not being notes. **#18 — no causal claim is
made** about what produced the invisible notes, what they are for, or whether they are an editorial
artifact; that is the user's ruling and this batch does not anticipate it. **#6 — one artifact:** this
report; the sweep table and its generator gained nothing.

**Against `DEFECT_TYPES.md`.** **DT-26 (scope-assumed enumeration) is the live risk the dispatch names,
and it is met head on with six reconciliations, each of which sums to a population total rather than to
a plausible-looking number:** the per-bar counts sum to 242; the per-staff-and-voice counts sum to 242;
the three per-bar-voice unit classes account for all 231 units and all 242 notes; the
visible-notes-sounding distribution sums to 242; the exact-partner classes sum to 28; and the
`<visible>` element population divides into 242 + 19 + 2 + 1 = 264, which is the whole of it. **No
invisible note falls outside a category anywhere in this report**, which is the dispatch's own stated
requirement. **DT-23 (silent-failure path)** —
the probes catch no exception broadly; a voice that does not fill its bar is recorded and printed, not
absorbed, which is how the 40 shortfalls came to be investigated at all. **DT-11 (hand-transcribed
value)** — every number is either a script's output in this session or a named field of the sweep
table. **DT-12 (stale anchor)** — every file and every line number cited was opened in this session.

**Two defects of my own, both found and corrected rather than shipped.** The first is the tie matcher's
missing `<measures>` term, §7.2, found while the work ran; it is recorded rather than quietly fixed,
because the corrected matcher is what the tick establishment rests on. **The second was found by THIS
check, in the report as first written:** the middle excerpt of §2(e) was labelled *staff 1, bar 46*,
which I had inferred from the line's position in the file and never checked. **It is staff 1, bar 73.**
The label was corrected and every one of the three excerpt labels was then established by counting the
`<Staff>`, `<Measure>` and `<voice>` opening tags that precede the line — the other two, bar 21 and bar
84, were already right. **This is principle #18's class — a checkable fact asserted without checking it
— and it is counted here rather than absorbed.**

**The reserved-word convention (D-113) and Ruling 21.** *Bar* is used in this report only for the
metric unit; the excluding sense is written *exclude*, per §3ab. *Measure* appears only as the element
name `<Measure>`, quoted. *Note* is a pitch event throughout. *Score* is the music. *Register* is
written in full as *the open-items register* / *the decisions register*. No new collision is
introduced.

**One thing this report does NOT do.** **It does not say what the invisible notes are for, whether
they are ordinary notation or an editorial artifact of this edition, or whether the file is suitable
as an exemplar.** The dispatch reserves all three to the user, and the facts above are assembled so
that ruling can be taken on them.

---

## Done, on the ruled stop form

**What was done.** The dispatch and its §0 subjects pinned, nine blobs, re-verified at the close, all
nine reproducing and none disagreeing. The subject file established as the object the sweep measured, at both its size and its
digest. All six counts re-established at the file, none diverging, and the generator's own definition
of each of the three quoted from its source — including the fact that `cue_sized_small` counts
`<small>` elements anywhere and not notes. The tick arithmetic established positively against the
file's own 160 spanner distances before any answer rested on it. §2's location facts given as counts,
bar ranges, a per-staff-and-voice table and a per-bar-voice unit reconciliation, with the
never-alone answer measured at 197 onsets and the tie answer at all 48 ties. Three verbatim excerpts
quoted from the first, middle and last of them. §3's duplication test answered at the width the
dispatch names and at two wider ones, with the cue-size and non-sounding overlaps counted at both
levels. §4's corpus context taken from the sweep table without re-reading a score. §5's thirteen
strings quoted. All four predictions marked, one of them falsified.

**What was not done, and why.** **No score was selected, ranked, recommended or staged**, and **no
view is offered on whether the file is suitable** — because §0 and §9 forbid it, not because the batch
stopped short. No registry, manifest, pin or governing document was touched. The Couperin fallback was
not opened. `.gitattributes` was not edited and the byte-stability question stays owed. Nothing found
was repaired.

**The remainder is untouched.**

---

*Provenance: executed by Claude Code, 2026-09-01, against
`cc_instruction_invisible_notes_establishment_2026_09_01.md` (pin
`e8ee29fc8075ff5b03d62e6d329f33f8a18f7ae2`), which executes the condition that is part of **Ruling 22
(§3ac)** of `cowork_rulings_2026_08_31_decision_surface_sitting.md`. Every count above was recomputed
from `tools/dcml/cpe_bach_keyboard/MS3/wq55n02a.mscx` in this session, except §4's, which are fields of
`tools/audit/score_tags_l0l1_sweep.json` and are cited as such; none is transcribed from a prior record
(#17f, **D-431**), and the figures the dispatch relayed were re-established at the file. Working-tree
files were read with the file tools; shell access was used for the `git hash-object -w` pinning Task 0
orders, for `tools/audit/changed_paths.py` as the guard's named substitute, and for running five
read-only scripts that live outside the repository in the session scratchpad, each taking the score
path as an argument (**D-253**, and its 2026-08-08 widening, whose declared ceiling that argument form
is — recorded at §7.4 rather than passed over). **The standing shell-read guard fired three times and
every refusal was taken as routing.***
