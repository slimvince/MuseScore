# EXTRACT — Sears, Pearce, Caplin & McAdams 2018, "Simulating melodic and harmonic expectations for tonal cadences using probabilistic models" — Task B candidacy row 39, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **The grade.** All twenty-four pages read AT THE OBJECT as page images through the bridge. **No
> relay, no web-fetch read.**
>
> **Why this paper, and what the read was for.** Row 39 of `reading_pass/candidacy_upgrades.md`,
> admitted **ON THE DOUBT DEFAULT**: *"A computational model of cadential arrival; whether its method
> bears on L1's cues or only on perception is not settled by the row."* **The doubt default's whole
> point is that such a question is answered by reading, not by the derivation. This read answers it.**
> Fifth and last member of the L1 slice **Ruling 10** made the phase's first reading.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

David R. W. Sears, Marcus T. Pearce, William E. Caplin & Stephen McAdams, "Simulating melodic and
harmonic expectations for tonal cadences using probabilistic models", *Journal of New Music Research*
**47:1** (2018), pp. 29–52. Published online 22 November 2017, DOI 10.1080/09298215.2017.1367010.
McGill University; Queen Mary University of London.

**File:** `docs/research_papers/sears_pearce_caplin_mcadams_2018_jnmr_cadence_expectations.pdf`.

## ★ The doubt-default question, answered

**Its method does NOT bear on L1's cues. It bears on perception, and — secondarily — on how a cadence
ground truth and a cadence measurement are read.** Three findings at the object settle it, and any one
of them would:

1. **It does not detect cadences. It consumes them.** The cadence collection is **annotated by hand**
   under Caplin's typology and supplied to the analysis; the study then measures how *predictable* the
   annotated terminal events are. There is no detection task, no classifier, no precision and no recall
   anywhere in the paper.
2. **★ Its harmonic viewpoints require a hand-annotated tonality.** [FACT, §5.2] *"to relate `cpitch`
   to a referential tonic pitch class for every event in the corpus, we manually annotated the key,
   mode, modulations and pivot boundaries for each movement."* **The scale-degree viewpoints `csd` and
   `csdc` — the ones carrying every harmonic result in the paper — are computed from a key that a human
   supplied.** A method that consumes a decided tonality cannot produce an L1 cue, L1 being the layer
   that decides nothing and runs before any tonality exists.
3. **The authors name their own object of study, in the paper's last sentence.** [FACT, §7] *"the
   schematic expectations formed by listeners for cadences and other recurrent temporal patterns amount
   to these sorts of probabilistic inferences requires an entirely different approach, one in which the
   listener, rather than the music, represents the primary object of study."*

**So the doubt resolves against L1 candidacy — and the reading was still worth its cost**, because three
of its findings bear on things the record does care about. Those are §"Findings" below.

## Claims, labeled

### What the method is

**[FACT, abstract, §1]** The model is **IDyOM** — a finite-context (*n*-gram) model that predicts the
next event in a musical stimulus by unsupervised statistical learning of sequential structure — applied
to the terminal melodic and harmonic events of **245 exemplars** of the five most common cadence
categories in the classical style.

**[FACT, §3, §5.2]** Events are represented in Conklin's **multiple viewpoints** framework. The melodic
viewpoints are chromatic pitch (`cpitch`), melodic interval (`melint`), chromatic scale degree (`csd`)
and an optimised combination (`selection`); the harmonic ones are vertical interval class combination
(`vintcc`) and chromatic scale-degree combination (`csdc`), the latter *"intended to approximate Roman
numerals"*; and `composite` is the joint probability of the melodic and harmonic models.

**[FACT, §4]** Probabilities come from maximum-likelihood *n*-gram counts smoothed by **Prediction by
Partial Match**, in the variable-order **PPM\*** variant with interpolated smoothing and Moffat's escape
method C. The reported quantity is **information content**, IC = log₂(1/p), in bits.

**[FACT, §5.3]** Only the **long-term model** (LTM+) is used: *"the STM should be irrelevant for the
present purposes, since cadences exemplify the kinds of inter-opus patterns that listeners are likely to
store in long-term memory."*

**[FACT, §5.4]** Evaluation is **10-fold cross-validation**, the corpus serving as both training and
test set.

### Its own preprocessing, recorded because it bounds what the figures mean

**[FACT, §5.1]** *"To ensure that each instrumental part would qualify as monophonic … all trills,
extended string techniques, and other ornaments were removed."* Double and triple stops were reduced to
the note events preserving the voice leading. Chord events are formed by **full expansion**, duplicating
overlapping note events at every unique onset time.

**[FACT, §5.2]** Rhythmic and metric viewpoints were **deliberately excluded**: *"the terminal events at
the moment of cadential arrival appear in strong metric positions, and few of the cadences feature
unexpected durations or inter-onset intervals at the cadential arrival, so we have excluded viewpoint
models for rhythmic or metric attributes from the present investigation."*

## Measured results, as the paper states them

**Corpus (§5.1, Tables 2–3).** 50 sonata-form expositions from Haydn's string quartets (1771–1803),
Opp. 17–76, from KernScores. 270 cadences annotated, 25 excluded (15 where the cadential bass or soprano
is absent from cello or first violin; 10 implying more than one category), leaving **245 cadences**:
PAC 122, IAC 9, deceptive 19, evaded 11, half cadence 84. Note events: violin 1 14,506; violin 2 10,653;
viola 9156; cello 8463; expanded chord events 20,290.

**Experiment 1 — are cadential terminal events more predictable than non-cadential ones?** For the first
violin, mean IC increased significantly from PAC to non-cadential contexts for `melint`, `csd` and
`selection`, but not for the baseline `cpitch` (Table 4). **For the cello the direction reversed**: mean
IC *decreased* in every model from PAC to the non-cadential levels — *"contrary to our predictions, the
terminal events in the cello from cadential contexts were actually less predictable than those from
non-cadential contexts."* For the chord viewpoints `vintcc`, `csdc` and `composite`, cadential terminal
events were more predictable than non-cadential ones, `composite` showing *"an ascending staircase"*
from PAC through tonic to non-tonic.

**★ [FACT, §6.1.3] The authors' own explanation of the cello reversal, and it is a fact about the
evidence rather than about the model.** *"since the leap in the bass by descending fifth (or ascending
fourth) in perfect authentic cadential contexts occurs less frequently than motion by smaller intervals
in any other context …, it may also be that cadential bass lines are simply less predictable than their
stepwise, non-cadential counterparts when considered in isolation. For the viewpoints that explicitly
model the interaction between the bass and the upper voices, however (e.g. `vintcc`, `csdc`, or
`composite`), IDyOM produced considerably lower IC estimates for cadential successions like 5̂–1̂ than
for non-cadential successions like 1̂–1̂, 2̂–1̂, or 7̂–1̂."*

**★ [FACT, §6.1.3] The half cadence, measured by a third method.** *"half-cadential contexts generally
failed to elicit lower mean IC estimates compared to non-cadential root-position dominants. Thus,
according to IDyOM, the terminal events from the HC level are no more (or less) predictable than any
other instance of root-position dominant harmony selected at random from the corpus."*

**Experiment 2 — do the IC estimates order the cadence categories as a typology predicts?** The
*Prospective Schemas* ordering PAC→IAC→HC→DC→EV fits better than the *1-Schema* ordering
PAC→IAC→DC→EV→HC; for `composite` the Prospective model *"accounted for roughly 55% of the variance …
which represents the largest effect demonstrated across all of the polynomial contrasts from every
viewpoint model"* (Table 6). Genuine cadence categories received lower mean IC than the cadential
deviations in every model.

**★ Experiment 3 — where the boundary evidence actually sits.** [FACT, §6.3] The two hypotheses tested
are *"(1) that the terminal event of a group is the most expected (i.e. predictable) event in the
surrounding sequence; and (2) that the next event in the sequence is comparatively unexpected (i.e.
unpredictable)"*, on the ground that *"unexpected events engender prediction errors that lead the
perceptual system to segment the event stream into discrete chunks."* Results (Table 7, Figure 6): for
the first violin, *"the mean IC estimates … increased significantly following the predicted boundary for
every cadence category in the collection"*, and for PAC, IAC, HC and DC the increase from the terminal
event to the following one was significant. For the **evaded** category the significant increase occurs
*at* rather than after the expected terminal event, which the authors give as the predicted behaviour
for a cadential deviation. The framing sentence: *"the strength of the potential boundary between two
sequential events results in part from the increase in information content (or decrease in probability)
from the first to the second event."*

**The authors' own stated limitations** [FACT, §7]: *"the rather meager sample size for three of the
five cadence categories … casts some doubt upon the generalisability of the reported findings"*; the
melodic models assume listeners expect *specific* intervals rather than small ones generally, which is
*"theoretical, rather than empirical"*; only contiguous *n*-grams were used, which *"is particularly
acute for corpus studies of tonal harmony, where the musical surface contains considerable repetition,
and many of the vertical sonorities from the notated score do not represent triads or seventh chords,
thereby obscuring the most recurrent patterns"*; and *"IDyOM benefited from human annotations of tonal
information in `csd`."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score reduced so that each instrumental part is
monophonic (ornaments and multiple stops removed); **a hand-annotated key, mode, modulation and pivot
boundary track**; and **a hand-annotated cadence collection** typed under Caplin. It assumes no
segmentation of its own and performs none.

**What it HANDS downstream.** Per-event information content in bits, per viewpoint — a scalar of
*predictedness*, not a label, not a boundary and not a decision. Nothing in its output is a fact about
the music that another layer could consume as evidence without first deciding what an IC value means.

**Its own STATED SCOPE and limits.** One composer, one genre, one form section: Haydn string-quartet
sonata-form expositions. Rhythm and meter excluded by design. The object of study is the listener.

## What an L1 detail specification could adopt, adapt, or must argue against

**Nothing, and that is the finding.** The method needs a key L1 does not have, needs cadence labels L1
does not produce, and outputs a quantity that is not evidence about the score. **It is not an L1
candidate and should not be treated as one in the derivation.** Its bearing is on L3's cadence typing,
on the phrase-boundary primitive, and on measurement design — all named below and all outside the L1
slice.

## ★ Findings, routed and not applied

**(1) ★ A THIRD INDEPENDENT STATEMENT THAT THE HALF CADENCE IS NOT SEPARABLE BY LOCAL EVIDENCE — AND IT
COMES FROM A DIFFERENT KIND OF METHOD ENTIRELY.** Rows 37 and 38 say it in F-measure (0.29 and 0.41
against 0.80 for the perfect authentic cadence). This study says it in information content: the terminal
events of a half cadence are *"no more (or less) predictable than any other instance of root-position
dominant harmony selected at random from the corpus."* **Detection and predictability are different
measurements, and they agree.** This strengthens DP-I's recorded ground — cues at L1, type at L3 —
beyond what the charter currently cites. **Routed as an addition candidate to DP-I's defense; not
applied, an amendment being the user's act on a surface.**

**(2) ★ A PRECISION ABOUT THE "TWO INDEPENDENT STUDIES", worth carrying because a later reader will lean
on it.** The L1 charter cites rows 37 and 38 as two independent studies. **They are independent in
METHOD and not in DATA:** row 38 states it uses *"two datasets also used by Bigo et al."*, and row 37's
Haydn cadence annotations are *"from Sears and colleagues"* — that is, from **this paper's own author
group and annotation programme**. So the replication is a second method over largely the same annotated
material. **The charter's sentence is not wrong** — they are two studies and they are independent — **but
the independence does not extend to the ground truth, and a derivation that leans on the replication
should say which kind of independence it is relying on.** *(Finding (1) is not subject to this caveat in
the same way: it is a third method AND a different measurement, though on the same composer.)*
**Recorded; nothing amended.**

**(3) ★ A FINDING ABOUT BASS EVIDENCE THAT BEARS ON HOW ANY CUE IS FORMED.** In isolation, the cadential
bass leap is *less* predictable than the stepwise motion of non-cadential contexts — so a single-voice
statistical model **penalises exactly the motion that signals the cadence**, and the sign of the effect
reverses. Only viewpoints that model the interaction between bass and upper voices recover the expected
direction. **The practical statement for a detail specification: a cue defined over the bass alone can
have the wrong sign; the cue is the bass motion IN RELATION to what sounds above it.** *(Read beside row
37, which reaches the same place from the other side: its bass-move features are always relative to the
chord at the arrival, never to the bass line alone.)* **Routed to the L1 and L2 detail specifications.**

**(4) A boundary-evidence claim, routed to the phrase-boundary primitive and to L3, not to L1.**
Experiment 3's result is that a boundary's strength lies partly in the **rise** in information content
*after* the terminal event, not in the terminal event alone. **This is a claim about where boundary
evidence sits in time**, and its owner in our frame is the phrase-boundary primitive and L3's grouping,
not L1's cues. **Recorded, routed, not applied.**

**(5) A fourth instance of the ground-truth-bounds-the-figure pattern.** The authors exclude 25 of 270
annotated cadences because the annotation cannot be made to fit the analysis — 15 for a missing bass or
soprano, 10 for implying more than one category — and name the small sample for three of five categories
as a limit on generalisability. **Routed to measurement design**, beside rows 37 and 38's own versions of
the same point.

**(6) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**NOT CENTRAL for L1** — no claim of this paper carries load in an L1 detail specification, which is the
doubt-default question answered above. **Its findings (1), (3) and (4) do carry load elsewhere** — DP-I's
defense, the L2 detail specification, and the phrase-boundary primitive — so **whether a second
extraction is owed is a question for the sessions that take up those subjects, and is deliberately not
decided here.** Recorded rather than assumed either way.

## What this extract does NOT do

It derives no specification statement, amends no document, opens no code, touches no measurement tool,
corpus or golden, writes no open-items row and allocates no decisions-register identity. It does not
re-open DP-I; finding (1) is an addition candidate put to the user, not an amendment.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. The paper was read
at the object as page images, all twenty-four pages. Read beside it for findings (1) and (2): this
session's own row-37 and row-38 extracts. No shell command was run on the repository or on any staged
copy of it for content or for listings; the container copy used for writing this file is declared. Every
value above is the paper's own (#17f, D-431).*
