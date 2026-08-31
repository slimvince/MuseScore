# Cross-check — row 1: McLeod & Rohrmeier 2021, the modular harmonic analyzer

> **The two extracts compared, 2026-08-31, under `cowork_reading_pass_commission_2026_08_30.md` §4
> and the independence protocol of `reading_pass/continuation.md` §2.**
> First pass: `reading_pass/extracts/mcleod-rohrmeier-2021-modular-harmonic-analysis.md` (session 1,
> 2026-08-30). Second pass: `reading_pass/extracts_second_pass/` same file name (session 2,
> 2026-08-31), **written and landed before the first extract or its content record was opened.**
> **Neither extract has been edited to match the other.** Where a disagreement was resolved, the
> resolution below says which side moved and on what evidence.

## 0. What the independence of this cross-check IS, and what it is not — read before the verdicts

The commission asks for a second **independent** pass. What was achieved: a different session, a
different reader, different prompts, and no consultation of the first extract or its content record
until the second extract was on disk. What was **not** achieved, and cannot be in this environment:
**read-tool independence.** Both passes read the paper through the same relaying mechanism — a
web-fetch tool that answers prompted questions over the document rather than putting its pages
before the reader. **So a systematic error of that tool would survive both passes undetected,
and this cross-check cannot see it.** That bound is real and is stated at every use.

*It is not nothing, either:* the disagreements below are all of the shape the double pass exists to
catch — a claim one reader's prompts surfaced and the other's did not — and one of them was a
question the two passes actually answered **differently within the same session** before a targeted
read settled it.

## 1. Agreements, passed over briefly

Both extracts agree, in substance and where quoted in wording, on: the six-module architecture; the
1,540-symbol absolute chord vocabulary; **spelled** pitches (A♯ ≠ B♭) as a deliberate and
uncommon choice; applied chords represented as brief, possibly recursively embedded **key changes**
rather than as a label field; **chords, keys and segmentation decoded in ONE beam search** rather
than in sequence; the paper's own scope statement that suspensions, altered chordal tones and pedal
tones are absent and are future work; the authors' own diagnosis of key-axis noise as a cost of
modularity, quoted identically by both passes; the corpora (742-piece internal, 201-piece F-H, the
latter assembled from TAVERN, BPS-FH and Roman Text); and every value of the CSR results table at
both corpora and all five widths. **No value disagrees anywhere.**

## 2. Disagreements and coverage differences, each resolved at the paper

### 2.1 The merge rule and the over-segmenting transition model — **RESOLVED IN THE FIRST PASS'S FAVOUR; THE SECOND PASS MOVED**

The first extract states that *"a merge rule was added because the transition model OVER-SEGMENTS
and its thresholds were hard to tune."* The second pass's three reads surfaced `ctmin`, `ctmax` and
`C_durmax` as window constraints but **no merge rule and no over-segmentation finding at all** — a
silent gap, which is the more dangerous kind.

**Resolved at the paper, and the first pass is right, close to verbatim.** The paper states *"we
noticed that the CTM was over-segmenting the input, and the thresholds were difficult to tune"*, and
defines the merge as legal for two consecutive windows when the merged duration is still under
`C_durmax` and the two windows carry the same chord.

**Why this one matters more than its size.** It is direct evidence about **boundary-first designs**,
which is what DP-C turns on: a dedicated standalone boundary model, well trained, over-segmented in
practice and needed a repair bolted after it. The second extract would have carried that evidence
away entirely.

### 2.2 The reason for a holistic 1,540-symbol chord output — **RESOLVED IN THE FIRST PASS'S FAVOUR; THE SECOND PASS MOVED**

The first extract states the chord label is decided holistically over whole symbols *"with the
stated reason that separate per-field outputs can combine inconsistently"*. The second pass recorded
the vocabulary but not the reason.

**Resolved at the paper: the reason is stated.** *"In cases such as this, it is important that every
feature of a chord is considered holistically as a unit, rather than potentially classifying the
chord as a C minor 7th chord in 1st inversion"* — the paper's worked case being a bass C with the
reading genuinely uncertain between a C major triad and an A minor seventh in first inversion.

**Why it matters.** This is a primary-source statement of exactly DP-A's ground — that splitting one
decision across per-field outputs lets the fields combine into a reading no field intended — made by
authors who chose the holistic form on that ground. The first pass carried it; the second did not.

### 2.3 The line-of-fifths encoding and the ±14 bound — **CONFIRMED, WITH ONE IMPRECISION IN THE FIRST PASS'S PHRASING**

The first extract names *"the relative-chord line-of-fifths encoding, the ±14-fifths bounded key
transitions"* among its mechanism candidates. The second pass surfaced neither.

**Resolved at the paper: the line-of-fifths encoding is confirmed**, quoted as *"the root pitch
class and bass note pitch class, each represented as the interval above the key tonic on the line of
fifths (−14–14; two one-hots of length 29)"*. **But that quotation is the encoding of a relative
CHORD's root and bass against the key tonic — it is not, on this evidence, a bound on key
TRANSITIONS.** The first pass's phrase attaches the ±14 to the wrong object. **UNRESOLVED as to
whether key transitions carry a fifths bound of their own**; no equation is carried out of the
paper on that point by either side, and a later reader wanting it must go to the paper's key-model
section.

### 2.4 Per-inversion and major/minor breakdowns — **CONFIRMED; A SECOND-PASS COVERAGE GAP**

The first extract carries inversion-position accuracies 71.5 / 54.4 / 38.3 / 40.5 (root / 1st / 2nd
/ 3rd) and minor 44.6 against major 40.9 CSR. The second pass surfaced none of these.
**Confirmed at the paper, every value.**

**★ A collision warning, recorded so nobody trips over it later.** The figure **71.5** appears in
this pass's records twice, for two entirely unrelated quantities: here it is **root-position chord
accuracy in McLeod & Rohrmeier 2021**, and at verification target **V4** it is **the proportion of
strongest-level metrical beats carrying a harmonic change in Temperley 2009** — the subject of
`reading_pass/stop_v4_divergence_2026_08_30.md`. They have nothing to do with each other.

### 2.5 The CSM variants — **A SECOND-PASS GAP, NOW CLOSED**

The second extract recorded, and flagged as unestablished, that it did not know what CSM-I and
CSM-T name. **Settled at the paper:** CSM-I *"outputs a distribution over relative roots and chord
types (348 chords in total), in which case probabilities are shared between different inversions"*;
CSM-T *"includes the CSM-I's inversion invariance, and further shares weights between chords built
upon the same triad."* Both are parameter-sharing arms of the sequence model, not different systems.
This sharpens the first extract's own reading that the invariance helps mainly the key column on the
smaller corpus — the mechanism is weight sharing under a smaller relative vocabulary, which is the
ordinary small-data effect.

### 2.6 Module implementation classes — **A FIRST-PASS COVERAGE GAP, NOT A DISAGREEMENT**

The second extract carries what the first does not: CTM and CCM are a feed-forward layer followed by
a **bi-directional** LSTM; CSM, KTM and KSM a feed-forward layer followed by a unidirectional LSTM;
and the **ICM is not a network at all** — smoothed counts of each chord's proportion in the training
data. Nothing in the first extract contradicts this. **Recorded as carried by the second pass.**

*The bidirectionality is worth keeping in view when this system is read as a chain candidate: the
two modules that see the notes look both ways over the whole input, which is a stronger upstream
assumption than a forward-only reading of the same score.*

### 2.7 The within-session disagreement, declared rather than smoothed

The second pass's own three reads **disagreed with each other** on the load-bearing question of
§1: one returned *"segmentation occurs before classification"* and a targeted read of the Inference
section returned the joint reading. The joint reading is the one the paper supports and the one both
extracts now carry. **It is recorded because it is the measured failure rate of this reading
tool on the single question DP-C turns on** — one prompted pass in three got it backwards, and
only a question aimed at the Inference section by name recovered it.

## 3. Verdict

**The two extracts agree on every value and on every load-bearing claim they share. No claim of
either extract is falsified by the other or by the paper.** Three substantive items the first pass
held and the second missed are confirmed at the paper (§2.1, §2.2, §2.4); one item the first pass
held is confirmed in its object but **mis-attached in its phrasing** and is left explicitly
unresolved (§2.3); two items the second pass held and the first missed are recorded as carried
(§2.5, §2.6).

**The cross-check for row 1 is COMPLETE, at the relayed grade §0 declares.**

*Provenance: session 2 of the reading pass, 2026-08-31. All resolution reads at the paper's source
URL, `https://apmcleod.github.io/pdf/ismir-harmony.pdf`. No specification derived, no document
amended, no code opened, no register row or entry written. Neither extract was edited.*
