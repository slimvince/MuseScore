# EXTRACT — Sears, Pearce, Caplin & McAdams, "Simulating melodic and harmonic expectations for tonal cadences using probabilistic models" — Task B candidacy row 39, SECOND pass, AT THE OBJECT

> **STATUS: SECOND-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-10-15).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet: a CENTRAL source extracted in a second
> independent pass and then cross-checked against the first. Row 39 was decided CENTRAL for L3 by entry 405 §1.
>
> **The grade.** Twenty-four pages, printed pp. 1–24 (the journal's online pagination), read as page images
> through the bridge; the page count was established at the tool by an out-of-range request (it answered
> "PDF has 24 pages"), and all twenty-four images were seen to be present, not merely the calls to succeed.
> No relay, no web read.
>
> **The independence bound, declared and not claimed away.** Before this extraction the writing session had
> read: entry 405 §1 and §3, which state that the sealed first-stage draft names this paper as the study that
> *"takes the cadence category as already given from the harmony"*, quote the first extract's finding (1) —
> the half cadence's terminal events *"no more (or less) predictable than any other … root-position
> dominant"* — and say that the first extract records the cadences as annotated by hand under Caplin's
> typology; entry 404 §3(a), which names the paper's subject; and `FRAMEWORK.md` at §5's L3 block, DP-I and
> Appendix B §S5's L3. **The first extract itself was not opened before this file was landed.** So this pass
> is independent of the first extract's text, and not independent of the three findings just named.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

David R. W. Sears (McGill University), Marcus T. Pearce (Queen Mary University of London), William E. Caplin
and Stephen McAdams (McGill University), "Simulating melodic and harmonic expectations for tonal cadences
using probabilistic models", *Journal of New Music Research*. DOI 10.1080/09298215.2017.1367010. Received 5
November 2016, accepted 14 July 2017 (p. 1).

**The year, recorded rather than resolved.** The first page's header reads *"JOURNAL OF NEW MUSIC
RESEARCH, 2017"* (p. 1); the other odd-page headers carry the journal's name with no year; the pages are
numbered 1–24 with no volume or issue printed, which is the shape of an online-first version. The repository's file name and this extract's file name say 2018. Which year the
volume carries is **not established at this object**; the two are recorded side by side.

**File:** `docs/research_papers/sears_pearce_caplin_mcadams_2018_jnmr_cadence_expectations.pdf`.

## Claims, labeled

### What the paper sets out to do

**[FACT, abstract and §1, pp. 1–2]** The study uses the Information Dynamics of Music model (IDyOM) — a
finite-context (n-gram) model that predicts the next event by unsupervised statistical learning of sequential
structure — to *"predict the terminal melodic and harmonic events from 245 exemplars of the five most common
cadence categories from the classical style"* (abstract). It reports three findings: terminal events from
cadential contexts are more predictable than those from non-cadential contexts; models of cadential strength
advanced in cadence typologies reflect the formation of schematic expectations; and a significant decrease in
predictability follows the terminal note and chord events of the cadential formula.

**[FACT, §1, p. 2]** The paper's own statement of novelty: earlier IDyOM studies were mostly limited to
melodic pitch, *"so this investigation develops new representation schemes that also permit the probabilistic
modelling of harmonic sequences in complex polyphonic textures"*.

### The cadence typology the paper uses

**[THEORY, §2, pp. 2–3]** The cadence is understood both as a time span (a conventionalised harmonic
progression, sometimes with a falling melody) and as a time point (the end of a phrase-structural process),
after Caplin 2004. Cadences are sorted into two fundamental types: those whose goal is tonic harmony and those
whose goal is dominant harmony (p. 3).

**[FACT, Table 1, p. 3]** The five categories, their *"harmonic and melodic characteristics"* and their counts
in the collection (categories with an asterisk are *cadential deviations*):

| Type | Category | Essential characteristics (harmony; melody) | N |
|---|---|---|---|
| I | Perfect authentic (PAC) | V – I; 1̂ | 122 |
| I | Imperfect authentic (IAC) | V – I; 3̂ or 5̂ | 9 |
| I | Deceptive (DC)* | V – ?, typically vi; 1̂ or 3̂ | 19 |
| I | Evaded (EV)* | V – ?; ?, typically 5̂ | 11 |
| V | Half (HC) | ? – V; 5̂, 7̂ or 2̂ | 84 |

The counts sum to 245, the collection size the text states.

**[THEORY, §2, p. 3]** The paper's definitions, in its words or close to them: the PAC is *"a harmonic
progression from a root-position dominant to a root-position tonic, as well as the arrival of the melody on
1̂"*; the IAC is *"a melodic variant of the PAC category"* replacing 1̂ with 3̂ (or more rarely 5̂); the DC
closes on a non-tonic harmony while the melody resolves to a stable degree; the evaded cadence is
characterised by a sudden interruption in the projected resolution — the melody often leaps up to a degree
like 5̂ — so that the events at the expected arrival group forward rather than backward; the HC is
*"categorically distinct"* because its goal is dominant harmony, and its *"terminal harmony may support any
chord member in the soprano"*. **So in this typology two of the five category distinctions — PAC against IAC,
and the evaded cadence — are drawn on the melody, not on the harmony.**

**[THEORY, §2, p. 4]** Two models of cadential strength are named: the *1-schema* model (every category
compared with the PAC; ordering PAC → IAC → DC → EV → HC) and the *Prospective* (or *Genuine*) *Schemas* model
(Sears 2015, 2016; ordering PAC → IAC → HC → DC → EV), in which the HC is a distinct closing schema and so a
stronger ending than the deviations.

### How the cadences in the collection were obtained

**[FACT, §5.1, p. 8]** *"To examine model predictions for the cadences in the corpus, we classified exemplars
of the five cadence categories that achieve (or at least promise) cadential arrival in Caplin's cadence
typology"*. The corpus contains 270 cadences; 15 were excluded because the cadential bass or soprano does not
appear in the cello or first violin respectively; another 10 were excluded because they imply more than one
category (PAC–EV or DC–EV), leaving 245.

**[FACT, absence, as read]** Who performed the classification beyond *"we"*, by what procedure, and with
what agreement between annotators is met nowhere in the pages as read. No agreement figure is reported.

**[FACT, §5.2.1, p. 9]** The key was also assigned by hand: *"we manually annotated the key, mode,
modulations and pivot boundaries for each movement and then included the analysis in a separate text file"*,
supplied with the supplementary materials. Every note event was then associated with the viewpoints `key`
(0–11) and `mode` (0 major, 1 minor).

### The corpus

**[FACT, §5.1, pp. 7–8, Table 2]** Symbolic representations of 50 sonata-form expositions from Haydn's string
quartets (1771–1803), Opp. 17–76: 28 first movements, 11 finales, and inner movements (8 second, 3 third).
All downloaded from the KernScores database **in MIDI format**. Trills, extended string techniques and other
ornaments were removed so that each part is monophonic; for double and triple stops, the note preserving the
voice leading within and between parts was retained.

**[FACT, Table 3, p. 8]** Note events: violin 1 14,506 (per movement mean 290, SD 78, range 133–442); violin 2
10,653 (213, 70, 69–409); viola 9,156 (183, 63, 79–381); cello 8,463 (169, 60, 64–326). Chord events, by full
expansion: 20,290 (406, 100, 189–620).

**[FACT, §5.1, p. 9]** The distribution — PAC and HC most common, IAC least — *"largely replicates previous
findings for Mozart's keyboard sonatas"* (Rohrmeier & Neuwirth 2011).

### The model — multiple viewpoints and IDyOM

**[THEORY, §3, pp. 4–5]** The multiple-viewpoints framework (Conklin 1988, 1990; Conklin & Witten 1995):
each event is a set of basic attributes, each of a *type*; *basic* types are irreducible (for example
chromatic pitch, `cpitch`); *derived* types are partial functions of basic ones (melodic interval, contour,
scale degree), undefined where the derivation has no value; *linked* types are cross-products of their
constituent types, to model correlations between attributes (for example a V–I progression with 1̂ in the
soprano).

**[THEORY, §4.1–4.4, pp. 5–7]** Maximum-likelihood n-gram estimation (Eq. 1); information content
IC = log₂ 1/p (Eq. 2); entropy (Eq. 3); cross entropy H_m as the performance measure (Eq. 4); Prediction by
Partial Match with Moffat's escape method C (Eqs. 5–6) and interpolated smoothing (Eq. 7); and PPM*, which
selects the shortest *deterministic* context as the order bound for each event and, if none exists, the
longest matching context.

**[FACT, §5.3, p. 11]** Only the long-term model trained incrementally on the composition being predicted
(LTM+) is reported; the short-term model is omitted.

**[FACT, §5.4, p. 11]** 10-fold cross-validation, with cross entropy as the measure of performance.

### The viewpoints selected

**[FACT, §5.2, p. 9]** Rhythmic and metric viewpoints were excluded because most terminal events at cadential
arrival are in strong metric positions and few have unexpected durations at arrival.

**[FACT, §5.2.1, pp. 9–10]** Note viewpoints for the outer parts: `cpitch` (MIDI number, C4 = 60), `melint`,
`contour`, `csd` (chromatic scale degree relative to the hand-annotated key, modulo 12). Forward stepwise
selection over these and their linked pairs (ten models): `melint` was best at the first step (cross entropy
3.006 violin 1, 2.798 cello); adding the linked `csd ⊗ cpitch` lowered it to 2.765 and 2.556; no further
addition helped. That combination is called `selection`. `contour` had much higher cross entropy and was
excluded. Final melodic viewpoints: `cpitch`, `melint`, `csd`, `selection`.

**[FACT, §5.2.2, p. 10]** Chord events by *full expansion* (Conklin 2002), which duplicates overlapping note
events at every unique onset time. Two harmonic viewpoints:

- `vintcc` — vertical interval classes, in semitones modulo 12, between the lowest part and each upper part:
  13 classes per pair (0–11 and undefined), 13³ − 1 = 2,196 combinations; after Quinn (2010) upper-part
  doublings of the bass at unison or octave were removed, permutations treated as equal and interval
  repetitions removed, giving 232 possible combinations, of which the corpus contained 190. The paper says its
  chords *"have analogues in figured-bass nomenclature"*.
- `csdc` — combinations of chromatic scale degrees *"intended to approximate Roman numerals"*: 13⁴ − 13¹ =
  28,548 possibilities; keeping the bass degree explicit, permitting permutations only in the upper parts and
  excluding doublings gives 2,784, of which the corpus contained 688.

**[FACT, §5.2.2, p. 10]** `composite` is the product of `selection` (violin 1) and `csdc` at each onset where a
note and a chord event both appear; `csdc` was preferred to `vintcc` there because it encodes the bass's
scale-degree successions with the relevant upper degrees.

## Measured results, as the paper states them

The measured quantity throughout is information content in bits (IC) from IDyOM's LTM+, analysed by Welch's F with estimated ω² and
Bonferroni-corrected planned comparisons that do not assume equal variances (§6.1.1, pp. 11–12).

### Experiment 1 — cadential against non-cadential terminal events (§6.1, pp. 11–14; Tables 4–5)

**Design [FACT, p. 11].** PAC and HC are 206 of the 245 cadences. *Tonic closure*: the 122 PAC terminal events
against two equal-sized random samples of strong-metric events — *tonic* (root-position tonic harmony, any
soprano degree) and *non-tonic* (any other harmony and soprano degree). *Dominant closure*: the 84 HC
terminal events against *dominant* (root-position dominant, any soprano degree) and *other* (excluding
root-position tonic and dominant).

**Tonic closure [FACT, Table 4, p. 13].**

- Violin 1: main effect for `melint` (F 5.80, p .003), `csd` (7.83, < .001), `selection` (8.11, < .001); not for
  `cpitch` (1.56, NS). PAC against the non-cadences significant for `melint`, `csd`, `selection`; PAC against
  *tonic* significant only for `melint` (p .029).
- Cello: main effect for every viewpoint (all p < .001), **but the direction reversed** — IC decreased from PAC
  to the non-cadential levels and from PAC to *tonic*: cadential terminal events in the cello were *less*
  predictable (p. 12). The paper offers the leap of a fifth or fourth in a cadential bass, less frequent than
  smaller intervals, as a possible reason (p. 13).
- Chord events: main effects for `vintcc` (26.32), `csdc` (9.96), `composite` (13.61), all p < .001; PAC
  against the non-cadences significant for all three (p < .001); PAC against *tonic* not significant for
  `vintcc` and `csdc`, and p .052 for `composite`, which the text calls *"marginally significant"* (p. 12).

**Dominant closure [FACT, Table 5, p. 14].**

- Violin 1: main effect for every viewpoint; HC against the non-cadences significant for every viewpoint; **HC
  against *dominant* significant for `cpitch` (p .024), `melint` (.007) and `selection` (.008), not for
  `csd`** — matching the text at p. 12.
- Cello: main effect only for `csd` (6.19, p .003); HC against the non-cadences significant only for `csd`
  (.002); HC against *dominant* not significant for any viewpoint.
- Chord events: main effects for `vintcc` (16.66, < .001), `csdc` (4.00, .020), `composite` (8.04, < .001); HC
  against the non-cadences significant only for `composite` (< .001); HC against *dominant* not significant for
  any of the three. In Figure 3 (p. 14) the *dominant* bar for `vintcc` stands below the HC bar.

**The paper's summary sentence, and how far its own table reaches [FACT, p. 14].** The discussion states:
*"half-cadential contexts generally failed to elicit lower mean IC estimates compared to non-cadential
root-position dominants. Thus, according to IDyOM, the terminal events from the HC level are no more (or
less) predictable than any other instance of root-position dominant harmony selected at random from the
corpus."* Against Table 5 that sentence holds for the cello and for the three chord viewpoints, where HC
against *dominant* is not significant, and **does not hold for violin 1 under `cpitch`, `melint` and
`selection`**, where the HC terminal events were significantly more predictable than random root-position
dominants. The word *"generally"* is the paper's own hedge; the unqualified *"Thus …"* sentence after it is
wider than the table.

**[FACT, Tables 4–6]** In the chord-event rows of Tables 4, 5 and 6 the middle viewpoint is printed `csd`,
where the text and the figures name it `csdc`; this extract reads those rows as `csdc`, on the text.

### Experiment 2 — the five categories against the two strength models (§6.2, pp. 15–17; Table 6)

**[FACT, Table 6, p. 16]**

- Violin 1: main effect for `cpitch` (F 3.19, p .026), `csd` (3.02, .033), `selection` (3.77, .013), not
  `melint` (2.34, NS); a positive linear trend under the Prospective Schemas ordering for all four (p .013,
  .032, .008, .004); genuine categories lower than deviations for all four (p .006, .033, .009, .003).
- Cello: main effect for all four (p < .001); best-fitting contrast quadratic for `cpitch` and `melint`, linear
  for `csd` and `selection`; genuine lower than deviations for all four (p .045, .030, .003, .003). HC had the
  lowest cello IC on average (p. 15).
- Chord events: main effects for `vintcc` (6.68, .001), `csdc` (7.02, < .001), `composite` (7.21, < .001);
  linear Prospective Schemas trend for all three (p .007, < .001, < .001); genuine lower than deviations for
  all three (p .001, .001, .003). For `composite` the linear Prospective Schemas trend *"accounted for roughly
  55% of the variance"* (p. 16).

**[FACT, pp. 15–16]** 10 of the 11 evaded cadences have tonic harmony in root position or first inversion at
the moment of cadential arrival — offered as the reason EV terminal events received lower IC than DC.

**[CONJECTURE, the paper's, p. 16]** That these results replicate the completion ratings of Sears, Caplin &
McAdams (2014) for Mozart keyboard excerpts — a comparison stated, not measured in this paper.

### Experiment 3 — the time course around the terminal event (§6.3, pp. 17–20; Table 7)

**Design [FACT, p. 17].** A 5 × 3 two-way ANOVA, cadence category × time (e_{t−1}, e_t, e_{t+1}), on four
viewpoints: `selection` for violin 1 and for cello, `vintcc`, `csdc`. Only the interaction and simple main
effects are reported, with two planned comparisons: e_t against the surrounding events, and e_t against
e_{t+1}.

**[FACT, pp. 18–19]** Interactions: violin 1 F(8,718) = 3.88, p < .001, ω² = .03; cello F(8,717) = 13.02,
p < .001, ω² = .12; `vintcc` F(8,719) = 3.13, p = .002, ω² = .03; `csdc` F(8,704) = 2.99, p = .003, ω² = .03.
For `csdc` the simple main effects and planned comparisons were not significant and are not reported.

**[FACT, Table 7, p. 19]** e_t against e_{t+1}, the "increase after the terminal event":

- Violin 1 `selection`: PAC t 11.64 (< .001), IAC 2.78 (.032), HC 8.02 (< .001), DC 2.41 (.043), EV −1.58 (NS).
- Cello `selection`: PAC 1.65 (NS), IAC 0.71 (NS), HC 3.76 (< .001), DC 0.97 (NS), EV −3.19 (.009).
- `vintcc`: PAC 4.42 (< .001), IAC 2.09 (NS), HC 3.25 (.003), DC 0.05 (NS), EV 0.04 (NS).

**[FACT, p. 19]** HC was the only category for which the IC of both outer-voice models fell at e_t and rose at
e_{t+1}; for the cello the PAC and IAC did not rise significantly at e_{t+1}, *"thereby undermining the
hypothesis that for the genuine cadence categories at least, the perceived boundary follows the terminal
events of the cadence"*.

## The paper's own limitations (§7, pp. 20–21)

**[FACT]** As the paper states them: *"the rather meager sample size for three of the five cadence
categories"* and of the corpus (the paper does not name the three; by Table 1's counts they are presumably
IAC 9, EV 11 and DC 19 — this side's reading); viewpoints chosen from prior theory; `cpitch` sometimes performing like the more
plausible viewpoints; contiguous n-grams only (threaded viewpoints named as a possible extension); simulation
only, with listeners named as the needed further study. And: *"IDyOM benefited from human annotations of
tonal information in `csd`, but future studies could employ viewpoints like the General Chord Type (GCT)
representation (Cambouropoulos, 2015), which automatically produces Roman numeral-like encodings …"* (p. 21).

## Coupling facts (mandatory)

- **What it ASSUMES upstream.** A monophonic line per instrument (ornaments removed, one note kept per multiple
  stop); MIDI pitch numbers, so no spelling — `key` takes values 0–11 with C♯ and D♭ the same value (p. 9); a
  hand-annotated key, mode, modulation and pivot boundary for every event; a hand-classified cadence category
  and location for every cadence; four-part string texture with a cello bass. Chord events come from full
  expansion at every onset, not from a chord segmentation.
- **What it HANDS downstream.** Per-event probability and information content under each viewpoint, and the
  group statistics reported above. It hands no cadence detection, no cadence label and no key — the label and
  the key are inputs — and its chord events are a mechanical full expansion of the notes, not a chord
  analysis.
- **Its stated scope.** Haydn string-quartet expositions, classical style; five cadence categories of Caplin's
  typology; long-term statistical learning only; pitch viewpoints only (no rhythm or meter); IDyOM's
  contiguous n-grams.

## The check the handoff asks for — does the paper support *"takes the cadence category as already given from the harmony"*?

The wording is the sealed first-stage draft's (`FRAMEWORK.md` Appendix B §S5, L3); the ratified L3 block (§5)
says *"One study takes the cadence category as already given from the harmony and studies what follows from
it"*.

- **"Already given" — SUPPORTED at the paper.** The category is an input to every experiment; the paper
  detects and classifies nothing by its model. The classification was made by the authors (p. 8), and the
  key that `csd` and `csdc` are computed from was annotated by hand (p. 9).
- **"From the harmony" — NOT SUPPORTED as worded.** The categories were given by a hand classification under
  Caplin's typology, not derived from a harmonic analysis, and the typology's own definitions are harmonic
  *and* melodic (Table 1's heading names both). Two of its distinctions are drawn on the melody: the IAC is
  *"a melodic variant of the PAC"*, and the evaded cadence is characterised *"not by a deviation in the
  harmonic progression … but rather by a sudden interruption in the projected resolution of the melody"*
  (p. 15). The HC is defined by its harmonic goal with any chord member in the soprano.
- **"Studies what follows from it" — partly.** The paper studies the predictability of the terminal events
  themselves (Experiments 1–2) and of the events before and after them (Experiment 3), not only what follows.

**What a corrected sentence could say, offered and not applied:** that the study takes the cadence category
as given — hand-classified under a typology defined on the harmony and the outer-voice melody together, with
the key also hand-annotated — and studies how predictable the cadence's terminal events and their surroundings
are. Whether and where the charter's wording is corrected is the L3 specification's author's act, not this
extract's.

## What an L3 detail specification could adopt, adapt, or must argue against

- **Cadence type is a joint harmonic-and-melodic claim in Caplin's typology.** If L3 publishes Caplin's five
  categories, its inputs must include the soprano's scale degree at arrival as well as the decided chords; a
  type read off L2's chords alone could not separate PAC from IAC, nor recognise an evaded cadence. *(This
  side's reading of the paper's Table 1 and §2; a requirement on any system is met nowhere in the pages as
  read.)*
- **The half cadence is distinct by its harmonic goal**, and in this paper's measurement its terminal events
  are, for the cello and the chord viewpoints, no more predictable from preceding context than random
  root-position dominants — while for violin 1 under three of four viewpoints they are. *(FACT, Table 5.)* This
  is a statement about n-gram predictability, not about detection; a detection accuracy is met nowhere in
  the pages as read, so it neither supports nor refutes DP-I's ground (*"the half cadence is measured at F .29 and .41
  without the harmony"*), which rests on other studies.
- **The terminal event is followed by a rise in information content** for most genuine categories in violin 1
  and `vintcc` (Table 7). That is evidence a boundary-strength measure built on predictability could see a
  cadence's end; it is THEORY-adjacent for L3's phrase reading, not a method the paper proposes.
- **The paper's chord encodings** (`vintcc` as a figured-bass analogue, `csdc` as a Roman-numeral
  approximation) are pitch-class and mod-12; they carry no spelling and so are not the form this project's L2
  publishes. A specification citing them would have to say so.

## Findings, routed and not applied

1. **For the L3 charter's wording** (the check above): "already given" is supported; "from the harmony" is not
   as worded. Routed to the L3 specification's author. Documentation only; no algorithm changed by this
   extract.
2. **The p. 14 summary sentence is wider than Table 5** for violin 1. Any citation of the paper for *"HC
   terminal events no more (or less) predictable than random root-position dominants"* should carry the
   viewpoint bound: holds for the cello and the chord viewpoints; not for violin 1 under `cpitch`, `melint`,
   `selection`.
3. **No inter-annotator agreement** is reported for the cadence classification or the key annotation —
   relevant if the categories or the Haydn-quartet annotations were ever proposed as ground truth (principle
   #21).
4. **The year label** — 2017 on the first page's header, 2018 in the repository's names — is unresolved at this
   object.
5. **Bearing on DP-I's recorded ground**: none direct, for the reason given above (no detection measured).

## Closing — the read-back and the sweep, written after both were run

**The read-back** compared the written text with the page images. It found and corrected, before landing:
a claim that *every* page header carries the year 2017 (only the first page's does); an unmarked inference
naming the three small categories the paper's limitation refers to (now marked as this side's reading of
Table 1); a quotation truncated without an ellipsis (p. 21); a coupling sentence saying the paper hands
*"no chord"* where its chord events are a mechanical full expansion (now said so); and a confusing absence
note on `composite`, replaced by the real typesetting point — the chord-event rows of Tables 4–6 print `csd`
where the text names `csdc`.

**The sweep for absolutes** read every hit of *every, all, none, never, only, always, nowhere, nothing,
complete, whole* and bare *no* at its line. Hits stating the paper's own wording (*"every note event"*,
*"All movements"*, *"only present … LTM+"*, *"the only category"*, *"a main effect for every viewpoint
model"*) were checked at their pages and kept. Two of this side's own negatives over the paper were turned
into the form *met nowhere in the pages as read*; *"All values are IC"* was narrowed to the measured quantity.

## The cross-check against the first extract (2026-10-15, after this file had landed)

The first extract (`reading_pass/extracts/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md`,
16,969 bytes when opened) was read whole only after this file had landed at 26,310 bytes.

**Agreements, over every value both extracts carry:** the corpus (50 Haydn expositions, Opp. 17–76,
KernScores); the 270 cadences, the 15 and 10 exclusions and the 245 remaining; the five category counts; the
four note-event counts and the 20,290 chord events; the hand-annotated key, mode, modulations and pivots;
the hand classification under Caplin's typology; LTM+ only; 10-fold cross-validation; PPM* with escape
method C and interpolated smoothing; the exclusion of rhythmic and metric viewpoints; Experiment 1's violin
result (`cpitch` not significant) and the cello reversal with the authors' explanation; Experiment 2's
Prospective Schemas fit, the 55% for `composite`, genuine categories below the deviations; Experiment 3's
two hypotheses and the evaded cadence's rise at, not after, the expected terminal event. **No numerical
disagreement was found.**

**Disagreements, each resolved at the paper's page images, the first extract corrected at its site with its
former wording kept (#12):**

1. **Identity.** The first extract gave volume 47:1 (2018), pp. 29–52, and *"Published online 22 November
   2017"*. At the file, no volume, issue or print page range is printed (pp. 1–24); 22 November 2017 is
   the margin's download stamp. Corrected to what the file shows; the volume figures are recorded as not
   established at this object.
2. **"`csd` and `csdc` — the ones carrying every harmonic result in the paper".** False at p. 10 and Tables
   4–7: `vintcc` is a harmonic viewpoint computed from intervals above the bass with no key, and carries
   results. Corrected; the first extract's conclusion that the method is no L1 candidate still stands on
   `csd`, `csdc`, `composite` and the hand-annotated cadences.
3. **An absolute about the paper's contents** (*"no detection task … anywhere in the paper"*) narrowed to
   *met nowhere in the pages as read*. Both reads agree on the fact.
4. **The first extract's finding (1).** It quotes the p. 14 sentence on the half cadence without the
   viewpoint bound Table 5 sets (violin 1: HC significantly more predictable than random root-position
   dominants under `cpitch`, `melint`, `selection`). The bound is added at the site, the original wording
   left in place.

**One difference of reading, not of fact, left unresolved for the L3 specification's author:** the first
extract reads the half-cadence result as *strengthening* DP-I's recorded ground (detection and
predictability *"agree"*); this extract reads it as bearing on DP-I only indirectly, because the paper
measures group-mean predictability, not detection or separability. Both rest on the same table.

**What this extract carried that the first did not:** the check of the L3 charter's *"from the harmony"*
(this file's own section — the first extract does not address it); that two of Caplin's five distinctions
are melodic; the chord-event rows printed `csd` for `csdc`; the year label. **What the first carried that
this one did not:** the authors' second half of the cello explanation — that the bass-and-upper-voice
viewpoints gave *"considerably lower IC estimates for cadential successions like 5̂–1̂"* (p. 13) — and the
paper's last sentence naming the listener as the object of study (p. 21); both checked at the page and
correct. No claim is made that the comparison was exhaustive: it ran over what the two extracts carry.

**On the handoff's question** — whether the charter's *"takes the cadence category as already given from
the harmony"* holds: *already given* is supported; *from the harmony* is not, as worded (see this file's
check section). Documentation only; no algorithm is changed by this finding, and nothing is applied.
