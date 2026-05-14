# Quality Observations — Iter 76 Score Inspection

Four pipeline snapshot scores reviewed visually by user (Vincent Wong) during
Iter 76 snapshot diff evaluation. All chord symbols and Roman numerals shown
in screenshots are from our analyzer. Ground truth reference is DCML annotations
(where available) and user musical assessment.

---

## 1. bach_chorale_003 (BWV 153/3 — Ach Gott, vom Himmel sieh darein, A minor)

**Snapshot diff verdict: ACCEPT greedy-expand** (E/G# more correct than root-position E).

### 1.1 Inversion detection (tick 2400, bar 2 beat 1)
- **Ours:** E (V, root position)
- **Correct:** E/G# (V6 — G# in bass)
- **Status:** Fixed by greedy-expand. Golden updated.

### 1.2 Enharmonic misspelling
- **Ours:** Abm7b5 (bar 1 beat 2 area)
- **Correct spelling:** G#m7b5 (the note is G#, not Ab)
- **Status:** Pre-existing. Enharmonic spelling policy needs review.

### 1.3 Chord identity error — leading-tone chord misread
- **Ours:** Abm7b5 (or G#m7b5 after spelling fix)
- **More accurate reading:** viiø65 in A minor, or interpreted as E7/B
  (dominant 7th of A minor without root, B in bass). The tones are
  G#–B–D–F# which spell out a half-diminished seventh on G#.
- **Status:** Pre-existing. The chord is arguably better labeled E7/B
  (V7 without root) or G#ø7 (viiø7 in A minor). Neither matches our output.

### 1.4 Missing chord coverage — bar 2 beats 2–3
- **Ours:** No chord symbol or Roman numeral at bar 2 beat 2 and beat 3
- **Correct:** Beat 2 = Am, Beat 3 = E (fermata chord)
- **Status:** Pre-existing boundary coverage gap. Interior beats not anchored.

### 1.5 Chord identity error — bar 3
- **Ours:** Am/F
- **Correct:** F major (A is a passing/neighbor tone, not the harmonic root)
- **Status:** Pre-existing. Bass note incorrectly treated as harmonic root.

### 1.6 Chord identity error — bar 3 (Bm7b5/D)
- **Ours:** Bm7b5/D
- **Correct:** E7b9 (tones B–D–F–G# spell out the upper structure of E7b9;
  the functional harmony is a dominant 7b9 pointing to Am)
- **Status:** Pre-existing. Surface chord read instead of functional dominant.

---

## 2. bach_chorale_001 (BWV 269 — Aus meines Herzens Grunde, G major)

**Snapshot diff verdict: ACCEPT greedy-expand** (downbeat boundary at tick 2880
more natural than Jaccard's off-beat boundary at tick 3360; both chord identities
wrong, neither is a regression over the other).

### 2.1 Passing bass treated as harmonic bass (bar 2 beat 1)
- **Ours:** G/D (G major with D as bass)
- **Correct:** G (D is a passing note in bass, not the harmonic root)
- **Status:** Pre-existing. Recurring issue — see also §4.1 (bach_chorale_137).

### 2.2 Missing chord coverage — bar 2 beats 2–3
- **Ours:** No chord symbol at bar 2 beat 2 or beat 3
- **Correct:** Beat 2 = D (8th-note D6 resolving to plain D), Beat 3 = Em
- **Status:** Pre-existing boundary coverage gap. Same pattern as §1.4.

### 2.3 Chord identity error — bar 3 beat 1
- **Ours:** Am7 (or Em/B under greedy-expand)
- **Correct:** C major
- **Status:** Pre-existing. Neither Jaccard nor greedy-expand identifies C correctly.
  Am7 and C share tones (C–E–G–A); the correct root is C.

### 2.4 Chord identity error — bar 4
- **Ours:** G (with fermata)
- **Correct:** D (half cadence or internal cadence on the dominant)
- **Status:** Pre-existing. G and D share tones; dominant incorrectly read as tonic.

---

## 3. schumann_kinderszenen_n01 (G major, 2/4)

**Snapshot diff verdict: REJECT greedy-expand** (greedy misses the vii°7/V
chord entirely; this is a genuine regression blocking the bridge switch).

### 3.1 BLOCKING — Missing fast secondary-function chord (vii°7/V)
- **Jaccard:** Gm/C# labeled as Roman i — wrong identity but boundary present
- **Greedy:** Skips tick 480 entirely; jumps to D (V) at tick 960
- **Correct:** The chord at beat 2 of each measure is C#°7 (C#–E–G–Bb),
  functioning as vii°7/V (leading-tone diminished 7th of the dominant D).
  The original score's own Roman numeral analysis confirms vii°7/V.
- **Root cause:** Greedy-expand does not place a boundary for fast secondary-
  function chords in sparse 2/4 triplet texture. The C#°7 chord lasts
  approximately one beat at a relatively fast tempo; it likely falls below
  greedy-expand's duration floor or score threshold.
- **Status:** Blocking. Must be fixed before bridge switch can be committed.
  See Iter 77.

### 3.2 Chord identity error — C#°7 labeled as Gm/C#
- **Ours (Jaccard):** Gm/C# with Roman i
- **Correct:** C#dim7 (or C#°7), functioning as vii°7/V
- **Status:** Pre-existing chord identity error. The correct label requires
  recognizing the diminished seventh template with C# as root. Related to
  enharmonic spelling (C# vs Db) and root-assignment for diminished chords.
  Address separately after the boundary fix.

---

## 4. bach_chorale_137 (BWV 301 — Du, o schönes Weltgebäude, D minor)

**Snapshot diff verdict: REJECT greedy-expand** (greedy produces BbMaj7/D at
tick 0 where Dm is correct; this is a genuine regression blocking the bridge
switch).

### 4.1 BLOCKING — Opening chord completely wrong under greedy-expand
- **Jaccard:** Dm/C (i) — D minor root correct; C bass wrong or passing
- **Greedy:** BbMaj7/D (VI65) — completely wrong root and quality
- **Correct:** Dm (i) — the opening chord is D minor, root position
- **Root cause:** The opening span of this chorale likely contains a C in the
  bass (passing note or suspension) that greedy-expand accumulates into a
  broader region covering Bb–D–F–A, reading the aggregate as BbMaj7. The
  note-end tick collection (Iter 73) or head-gap synthesis may be pulling
  in extra tones before the first strong anchor.
- **Status:** Blocking. Must be fixed before bridge switch committed. See Iter 77.

### 4.2 Inconsistency — chord symbol vs Roman numeral (Dm/C vs i)
- **Ours:** Dm/C chord symbol but Roman i (root position implied by i)
- **Correct:** Both should reflect root position Dm. The C in the bass is a
  passing note, not the harmonic bass.
- **Status:** Pre-existing. Same category as §2.1 — passing bass treated as
  harmonic bass.

### 4.3 Chord identity error — D6/A
- **Ours:** D6/A
- **Correct:** D6/B (D major with added 6th; B natural in bass, not A)
  Note: B here = English B natural (= H in German/Swedish notation, not Bb).
- **Status:** Pre-existing. Bass note identification error.

---

## Recurring themes across all four scores

### R1 — Passing bass notes treated as harmonic bass
Seen in: bach_chorale_001 (G/D→G), bach_chorale_003 (Am/F→F),
bach_chorale_137 (Dm/C→Dm, D6/A→D6/B).
The bass voice often moves through passing or neighbor tones between harmonic
positions. Accumulating all sounding notes into a chord template without
distinguishing passing bass from harmonic bass leads to systematic slash-chord
over-annotation.

### R2 — Missing interior beat coverage
Seen in: bach_chorale_001 (bar 2 beats 2–3), bach_chorale_003 (bar 2 beats 2–3).
Beats that fall between greedy-expand's anchor points receive no chord annotation.
This is the same mechanism that causes the Schumann vii°7/V to be missed — fast
chords between stronger anchors fall through.

### R3 — Surface chord read instead of functional dominant
Seen in: bach_chorale_003 (Bm7b5/D→E7b9), bach_chorale_001 (G→D at cadence).
The analyzer identifies the surface pitch-class aggregate rather than the
underlying functional harmony. E7b9 and Bm7b5 share four tones; G and D share
three. Temporal context (the chord resolves to Am / is a cadence point) is not
sufficiently influencing the reading.

### R4 — Enharmonic misspelling
Seen in: bach_chorale_003 (Ab vs G#).
The enharmonic spelling of accidentals in chord symbols does not always match
the notated spelling. This is a display quality issue distinct from the harmonic
analysis.

### R5 — Chord/Roman numeral internal inconsistency
Seen in: bach_chorale_137 (Dm/C symbol vs i Roman — inversion inconsistency).
Chord symbol and Roman numeral sometimes disagree on inversion. The Roman numeral
pipeline and chord symbol pipeline may be reading different information.

---

## Priority for Iter 77 (bridge switch blockers)

1. **§3.1** — Greedy-expand misses fast secondary-function chords (Schumann vii°7/V)
2. **§4.1** — Greedy-expand gets opening chord wrong for bach_chorale_137 (BbMaj7/D vs Dm)

## Deferred quality issues (post bridge switch)

- R1: Passing bass distinction
- R2: Interior beat coverage
- R3: Functional dominant vs surface chord
- R4: Enharmonic spelling
- R5: Chord/Roman inversion consistency

---

## LLM Triage as Quality Signal

The `llm-triage` branch contains a pipeline that submits scores to an external
LLM (Claude/Gemini/OpenAI) for chord inference and compares the result against:

1. DCML ground truth annotations
2. Our own analyzer's output

This provides a structured, comparable third opinion — more authoritative than
manual visual inspection alone, and complementary to the BIR metric which only
measures three-way disagreements.

**Recommended workflow for future snapshot diff reviews:**
Before manually inspecting a failing snapshot score, run the LLM triage pipeline
on that score first. The LLM output gives a musical reference point for each
ambiguous chord, reducing reliance on the reviewer's personal harmonic knowledge.

**Particularly useful for:**
- Ambiguous chord identity cases (e.g. Schumann vii°7/V vs Gm/C#)
- Functional vs surface chord questions (e.g. Bm7b5/D vs E7b9)
- Multi-voice passing tone disambiguation (e.g. G/D vs G)

**Maintenance note:**
The `llm-triage` branch diverged from master at an early iteration and needs
periodic re-merging to stay compatible with the current analyzer's output format.
Before running LLM triage on new scores, verify the branch is up to date with
master and the comparison pipeline produces valid output.
