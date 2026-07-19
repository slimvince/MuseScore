# Checking the counted probability tables against three known-difficult passages, before anything is built

**★ USER-RATIFIED 2026-07-19: options 1a, 2a, and 3a** — after the alternatives were examined
against the guiding principles and the precision objective (the user's confirming readings: option
1b is information loss; option 1c is patching a symptom locally), and with the two user-raised
sharpenings incorporated: the genre scope limit (all counted values are Bach-chorale values; jazz
stays de-scoped per the register's item 7) and the per-factor asymmetry (a silent seventh should be
near-prohibitive for a seventh-chord reading — which per-factor counting delivers automatically).
The checking requirement (capacity protocol, item 4) is DISCHARGED. Execution: the single Claude
Code instruction `cc_instruction_secondary_dominant_refit.md`.

**Author:** Cowork, 2026-07-19, at the user's direction. Rewritten 2026-07-19 at the user's
direction for plain language (terms defined at first use; every choice presented with its
alternatives and their pros and cons — now a standing rule).

## 0. The words this document uses, defined

- **The new probability tables.** Two recent Claude Code work sessions produced tables of
  probabilities by COUNTING events in the 326 Bach chorales that have human harmonic analyses (the
  "When in Rome" ground-truth corpus). For example: among all 1,350 places where a major-key
  dominant chord is followed by another chord, 377 times the next chord is the tonic — so the table
  stores "dominant → tonic: 377/1350 = 0.28". Where this document says a value is **counted from
  the corpus**, that is the meaning: nobody chose the number; it is a frequency read off the
  annotated chorales. (Repository documents call this "fitting" the tables; the files are
  `tools/joint_estimator/tables_all.json` and `note_tables_all.json`.) These tables are NEW and
  belong to the planned joint estimator. They are NOT the existing progression code inside the
  analyzer (`chordanalyzer.cpp` and its neighbors) — that code is untouched and unaffected.
- **The chord-progression table** is one of these new tables: for each chord (in a given mode), the
  probabilities of what chord comes next within the same key.
- **The reliability rule.** A probability is stored individually only if its count is at least 20
  (a rule you ratified in the pre-fit protocols). Progressions observed fewer than 20 times are
  merged into groups ("pooled"), and each stored row keeps one **leftover probability** covering
  everything too rare to store individually.
- **A secondary dominant** (standard music-theory term; some repository documents say "applied
  chord" for the same thing): a chord functioning as the dominant OF some scale degree other than
  the tonic — for example, in C major, a D-major seventh chord acting as the dominant of G ("V of
  V"). Nobody "applies" anything at run time — it is simply a category of chord in the human
  annotations, written there as `V7/IV`, `V/V`, and so on.
- **The desk simulation** (`cowork_factorization_desk_simulation.md`, ratified earlier today): the
  pen-and-paper walkthrough of the planned estimator on ten test passages, done BEFORE these tables
  existed, using placeholder probabilities that were clearly labeled as placeholders.
- **This probe.** The ratified checking protocol requires that, before the new tables carry any
  weight in a build, the three desk-simulation passages whose outcomes depended most on the
  placeholder numbers be recomputed with the REAL counted numbers — with the expected outcome
  written down first, so a wrong expectation is caught as such. This document is that recomputation.
- **Reading the arithmetic:** scores are natural logarithms of probabilities. Only DIFFERENCES
  between competing readings matter. A difference of 1 means one reading is about 2.7 times more
  probable; a difference of 3, about 20 times; a difference of 5, about 150 times.

## 1. The three passages, and the expected outcomes (written before any number was looked up)

**Passage A — "Jesu, der du meine Seele" (bwv352), measure 1, beat 4.** The sounding notes
A–C–E–F♯ admit two readings: an A-minor triad with F♯ as an added sixth, or a half-diminished
seventh chord on F♯. The human annotator chose the half-diminished chord. The desk simulation found
this a genuine near-tie whose outcome depends on which note the bass carries at that beat (a fact
our data does not settle; the note-by-note source for checking it is not currently on disk).
**Expected with the real numbers:** still a near-tie, still decided by the bass note. If either
reading were to win big, that would itself be a warning about the tables, because this passage is
the repository's standard example of genuine ambiguity.

**Passage B — "Meine Seel erhebt den Herren" (bwv10.7), measure 19, beat 4.** The human analysis
has two harmonies here: first an incomplete dominant seventh pointing at C minor (sounding D–F–G,
its third missing), then, on the next downbeat, the C-minor chord itself. Our current analyzer
wrongly merges both into one segment across the barline. The desk simulation, using placeholder
numbers, found the planned estimator ALSO preferred the wrong merged reading — which exposed a gap
in the specification (fixed and re-ratified: penalties are charged per note-event, not per
segment). **Expected with the real numbers:** the verdict flips to the correct two-harmony reading,
decisively, because the counted boundary probability — a new harmony starts on 97% of downbeats —
makes merging across a downbeat very costly.

**Passage C — a constructed deceptive cadence.** In C major: a dominant seventh moving to the
A-minor triad. The estimator must keep the key as C major (reading the A-minor chord as the
submediant — the deceptive resolution) rather than hearing a move to A minor. **Expected with the
real numbers:** C major wins by the same margin as in the desk simulation or a larger one, because
"dominant seventh → submediant" was counted 79 times and is stored individually (0.113), while the
chords the A-minor reading needs are rare.

## 2. What the recomputation showed

**Passage A — as expected.** Still a near-tie, still hinging on the bass note. With F♯ in the bass,
the half-diminished reading wins by roughly 1 to 3 (log difference, depending on how the leftover
probability is divided — see finding 2); with E in the bass, the A-minor reading wins by roughly 3
to 5, because a tonic chord in six-four position was counted at only 6.3%, and a half-diminished
chord with its seventh in the bass was never counted at all. The estimator's correct output for
this passage remains: both readings, with the split published.

**Passage B — as expected, with one qualification.** The correct two-harmony reading now wins by
roughly 1 to 3. The counted boundary probabilities contribute a swing of +5.4 toward it (failing to
start a harmony on the downbeat costs log(0.027) = −3.6 alone). The note classifications add +3.1
(under the two-harmony reading, D and F are chord tones of the dominant seventh; under the merge
they must be explained away as non-chord tones). The qualification: the chord-progression table
currently works AGAINST the correct reading by about 5.5 — the direct consequence of finding 1
below — and the penalty for the missing third is still a placeholder, not a counted value (finding
3). The verdict is correct despite two known defects; fixing them widens it.

**Passage C — verdict correct, expectation partly wrong.** C major wins, but by 1.4 to 3.6 instead
of the desk simulation's 4.9. Two causes, both identified: the table of "which chord opens a new
key" is fine-grained, so even the commonest opening chord is expensive for both readings; and the
pooling rules group the A-minor reading's rare first chord into a family whose counted resolution
to the tonic is strong (0.47), helping the wrong side. The margin expectation is recorded as a
miss; the verdict and the mechanism it tests (the counted asymmetry — dominants resolve deceptively
to the submediant far more often than to other non-tonic chords) are confirmed.

## 3. The findings, each with the alternatives and their pros and cons

### Finding 1 (structural). The chord-progression table cannot express that a secondary dominant resolves to its target.

Verified directly in the table: the row for "dominant seventh of the subdominant", and every other
secondary-dominant row, contains no individually stored progression — each such chord is
individually rarer than 20 occurrences, so the pooling rules (which group by scale degree and by
chord family) merged all of its continuations into the general chord-frequency list of the mode.
Consequence: "the dominant of X moving to X" and "the dominant of X moving anywhere else" read the
SAME probability — the table is blind to the one behavior that defines a secondary dominant. The
recomputation of passage B watched this blindness tax the correct reading by about 5.5. The desk
simulation's tonicization and relative-key verdicts leaned on exactly this regularity, so leaving
it unexpressed would also weaken those.

The count needed to fix it exists: the corpus contains hundreds of secondary-dominant progressions
in total; they are only sparse when split per target and per inversion.

**Option 1a — add one pooling level that groups secondary-dominant progressions by their RELATION
to the target (resolves to the chord it is the dominant of / moves elsewhere), pooled across all
targets; then re-run the counting.** Pros: restores the defining regularity from real counts, with
no hand-chosen number (guiding principle 1, fact-based only); reuses the pooling idea the table
design already rests on — counting the same pattern across transpositions — so no new kind of
machinery (principle 6, one path per concern); the counts are ample, so the two or three new cells
pass the reliability rule easily (the ratified capacity budget stays satisfied). Cons: it amends a
pooling ladder you ratified, so it needs your re-ratification (that is why it is brought here and
was not just done); it adds a small number of parameters.

**Option 1b — leave the table as it is and hope the later stage compensates.** (The ratified plan
has a later stage where roughly ten weights, one per evidence type, are adjusted; a weight
multiplies a table's score.) Pros: no protocol amendment; no work now. Cons: a weight can only
scale what a table says — it cannot restore a distinction the table does not contain (the premise
ledger you ratified states this explicitly: structural gaps are never fixed by weights); the harm
is already measured, not hypothetical (passage B); against the long-term objective of
maximum-precision inference this concedes known, counted signal.

**Option 1c — hand-set a resolution probability for secondary dominants.** Pros: immediate. Cons:
violates the first guiding principle (facts and established theory only, no hand-set values) and
recreates exactly the class of unestablished constants (the register's item 23 lists about thirty
of them) that this whole fitting effort exists to eliminate; would fail the pre-fit gate that
requires every value to be counted or derived.

**Recommendation: option 1a.**

### Finding 2. No document defines how to score a progression that sits inside a row's leftover probability.

Each stored row ends with one leftover probability covering all continuations too rare to store
individually. The decoder, when it eventually runs, must assign a number to ONE SPECIFIC rare
continuation — and nothing yet says how. This probe computed everything under two provisional
readings and reported both (the verdicts above hold under both, which is why the probe could
proceed).

**Option 2a — divide the leftover in proportion to each chord's overall frequency in that mode.**
Pros: uses information we already hold — a common chord is genuinely a likelier unseen continuation
than a rare one (principle 12, no information loss); this is the standard construction in published
back-off models of sequences (principle 1, established method). Cons: none of substance; a little
more arithmetic per lookup.

**Option 2b — divide the leftover evenly among all unseen continuations.** Pros: simplest possible
rule. Cons: asserts that a rare chord and a common chord are equally likely continuations, which
the corpus counts show is false — it discards known information (against principle 12).

**Option 2c — score unseen continuations as impossible.** Pros: none worth naming. Cons: the
corpus is 326 pieces; treating everything it happens not to contain as impossible is factually
wrong and technically fatal (a zero probability destroys any path through it in the decoder).

**Recommendation: option 2a — one sentence added to the build specification.**

### Finding 3. The penalty for a chord tone that fails to sound is still a placeholder, not a counted value.

**The situation, spelled out.** When the estimator weighs a candidate chord reading for a segment,
the sounding notes give evidence in two directions:
- *Notes that sound but do not belong to the candidate chord* — these must be explained as
  non-chord tones (passing tones, suspensions, and so on). This direction WAS counted: the
  note-side tables give the corpus frequencies of chord tone versus in-scale non-chord tone versus
  out-of-scale tone, in their melodic and metric contexts.
- *Chord tones of the candidate that do NOT sound* — an incomplete chord. Passage B is the live
  example: reading the notes D–F–G as a dominant seventh on G means accepting that the chord's
  third (B natural) never sounds in the segment. How improbable is a dominant seventh whose third
  never sounds? TODAY that question is answered by a number I invented for the desk simulation
  (probability 0.35, chosen only to let the paper walkthrough proceed and labeled a placeholder
  then). The ratified specification requires this penalty to exist (and to be charged in
  proportion to how long the segment goes without the tone); no one has yet given it a counted
  value.

**Option 3a — count it, from data already on disk.** The note-extraction work committed earlier
today recorded, for every one of the ~18,000 humanly-labeled chord segments in the 326 chorales,
which notes sound in it; and the label itself names the chord's factors (root, third, fifth, and
seventh where the label is a seventh chord). So the counting is direct: across all segments
labeled with a triad or seventh chord, in what fraction does the ROOT actually sound among the
segment's notes? In what fraction the THIRD? The FIFTH? The SEVENTH? Four frequencies per chord
family (triad versus seventh chord — at most a dozen numbers), each backed by thousands of
observations in THIS corpus.

**Why counting per factor matters musically (user's point, 2026-07-19):** the factors are not
symmetric, and the counts will encode that automatically. A segment the annotators labeled as a
seventh chord virtually always has its SEVENTH sounding — the seventh is what earns the label — so
the counted probability of a silent seventh will be near zero, and the penalty for proposing a
seventh-chord reading whose seventh never sounds will be near-prohibitive. Which is exactly the
correct behavior: "if the seventh does not sound, it is probably wrong to call it a seventh chord"
becomes a counted fact, not a rule anyone writes. The FIFTH, by contrast, is the factor
four-part writing routinely omits, so its counted penalty will be mild; the THIRD sits between —
mostly present (it defines the quality), but analysts do label seventh chords with a silent third
where voice-leading makes the function unmistakable, and passage B (the human analyst's own
`V4/3` over sounding D–F–G, third silent, seventh sounding) is exactly such a case, which the
counts will reflect at their true corpus frequency. One invented blanket number cannot express any
of this; four counted frequencies express all of it.

**The scope limit (user's point, 2026-07-19 — and it applies to EVERY table in this fit, not only
this one):** all of these are counts over the 326 annotated BACH CHORALES, because that is the only
repertoire we hold ground truth for. They are Bach-chorale values. For jazz — where, for instance,
omitting the fifth or even the root from a voicing is normal practice — these frequencies would be
wrong, and no jazz values can be counted because no jazz ground truth exists. This is the already-
ratified position (the register's item 7: jazz correctness claims stay de-scoped until a jazz
ground-truth corpus is established; the ratified style-adaptation pattern is: same table STRUCTURE,
values re-counted per style, only when that gate is passed). The reliability claim in this section
is therefore scoped: "passed thousands of times over" is true of the chorale corpus and claims
nothing beyond it.

Same corpus, same five-fold splits, same generated-artifact discipline as every other table. The
stored result — illustrative, not yet counted: "in seventh-chord segments the third sounds in 96%,"
making passage B's missing-third penalty log(1 − 0.96) ≈ −3.2, a counted fact replacing my invented
log(0.35) ≈ −1.05. Pros: replaces an invented number that demonstrably carries load (passage B's
margin moves with it) with counted facts (guiding principle 1: facts only; and the precision
objective — the right penalty per factor is whatever the corpus says, not one guessed blanket
value); the per-factor asymmetry above comes free; tiny cost (a dozen numbers; the data is
committed; the work is mechanical). Cons: none of substance; one more table to document and
maintain; the genre scope limit — shared by every counted table — must stay declared on the
artifact.

**Option 3b — keep the placeholder.** Pros: no work. Cons: a hand-set value inside a system whose
ratified purpose is that every value be counted (principles 1 and 19); passage B's margin visibly
depends on this number, so the placeholder carries real load.

**Option 3c — drop the missing-tone penalty entirely.** Pros: one less term. Cons: the ratified
specification requires it, so this would be an unratified specification change; without it, an
incomplete chord and a complete chord score identically, discarding audible evidence (principle
12).

**Recommendation: option 3a.**

### For the record (no decision needed)

Across the three passages, no desk-simulation verdict is overturned by the real counted values, but
margins moved by 1.5–3.5 (log difference) in both directions, and one margin expectation was
plainly wrong. Catching exactly this — before any code exists — is what this checking stage is for.

## 4. What is asked of you

Ratify or reject, per finding: (1) option 1a — the added pooling level for secondary dominants,
then a mechanical re-count; (2) option 2a — the leftover-division rule, one sentence in the build
specification; (3) option 3a — the small missing-tone table. If ratified, ONE instruction to Claude
Code covers all three (a re-count and one small new table; no hand-chosen values anywhere), and the
estimator build can then open under the already-ratified parallel-build sanction. The checking
requirement itself (the capacity protocol's item 4: recompute the value-dependent desk-simulation
passages with the real tables before building) is discharged by this document.
