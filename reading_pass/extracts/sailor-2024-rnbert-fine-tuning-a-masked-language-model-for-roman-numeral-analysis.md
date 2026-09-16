# EXTRACT — Sailor, "RNBERT: Fine-Tuning a Masked Language Model for Roman Numeral Analysis" — Task B candidacy row 50, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All eight pages of the held PDF were read AT THE OBJECT: staged through the bridge
> and read with the file tools as page images. **No relay, no web-fetch read, no prompted
> extraction.** The held document prints no proceedings page numbers, so every location below is
> given as the printed section, table or figure number together with the page of the eight-page
> document. **Page 6 — the page carrying Table 4, from which every value in this extract is taken —
> was read a second time on its own and every transcribed cell re-checked against the image.**
>
> **★ ROW 50 IS GROUP 3's FOURTH MEMBER** ("the scoring architecture and its fitting",
> `reading_pass/candidacy_upgrades.md` line 177), after rows 45, 48 and 49. **THREE live places of
> the record rest on this paper, not the two the carried items name** — DP-A's and §S4(a)'s
> *.762→.859* pair, §S4(a)'s *"names the failure exactly"* claim, **and §S4's entanglement argument
> at line 1642, which the carried items do not list and which the identity sweep found.** All three
> were verified FIRST, before anything else was extracted.
>
> **Where the record cites this paper, established by `Grep` of the staged tree BEFORE extracting,
> never inherited. What was searched and where, stated as a rule rather than as a tally.** Over the
> staged tree: an IDENTITY sweep — **"RNBERT"** case-insensitively (which covers the record's own
> *RNBert* and the file name's *rnbert*), **"RN-BERT"**, and the bare author name **"Sailor"** — and
> then a FIGURE sweep — **".762"**, **".859"**, **"teacher forcing"** and **"teacher-forcing"**.
> **`FRAMEWORK.md` DP-A and §S4(a) were also READ WHOLE, not only searched.**
>
> **★ THE METHOD FACT ROWS 48 AND 49 PAID FOR WORKED AGAIN, AT A DIFFERENT SENTENCE.** DP-A's live
> sentence about this system (line 681) **names neither the paper, the system nor the author**, so
> the identity sweep did not reach it; the figure sweep did, because that sentence carries the two
> numbers. **And the identity sweep reached a place the figure sweep and the carried items both
> missed** — `FRAMEWORK.md` line 1642, which names *RNBert* and carries no figure at all. **So the
> rule row 49 stated holds and is now demonstrated in both directions: search the identity, search
> the figure, and read the design point's own text — each of the three reaches a place the others
> do not.**
>
> **The record bears on this paper in EIGHT places outside this line's own working files.** The
> candidacy row (`reading_pass/candidacy_upgrades.md` line 122); the slice derivation
> (`cowork_l2_task_b_slice_derivation_2026_09_05.md` line 85); the bibliography
> (`docs/research_papers/BIBLIOGRAPHY.md` line 69); **`FRAMEWORK.md` DP-A line 681, the LIVE
> ground**; **`FRAMEWORK.md` §S4(a) lines 1561–1562** (the decoherence claim) and **lines 1566–1567**
> (the figure), both in the sealed first-stage text; **`FRAMEWORK.md` line 1642, the entanglement
> argument's *Chord ↔ tonality* bullet, carrying a `[FACT]` tag** — **a place none of the nine
> carried items names**; and `reading_pass/population.md` line 110 (**V9**).
> **`cowork_reading_pass_findings_2026_08_31.md` carries no hit on any of the eight search terms**,
> so the findings surface does not name this paper at all. **The bound on the eight-place claim:** it
> is a claim about the files in this session's staged tree, which the provenance below enumerates,
> and not about every file in the repository.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## ★ The verification target (a) — the ratified FIGURE, CONFIRMED at the primary, with four precisions

The record states the item in three places:

- **`FRAMEWORK.md` DP-A, line 681 (the LIVE ground):** *"…conditioning the degree head on the
  tonality, raising degree accuracy from .762 to .859. [FACT — every figure reported by the paper
  named.]"* — **the paper, the system and the author are all unnamed here.**
- **`FRAMEWORK.md` §S4(a), lines 1566–1567 (the sealed first-stage text):** *"RNBert conditions the
  degree head on the tonality and measures degree accuracy rising from .762 to .859."*
- **`reading_pass/population.md` V9, line 110:** *".762→.859 = RNBERT (Sailor 2024), Table 4 lines 4
  vs 6 + §4.1 (degree .762 unconditioned → .859 key-conditioned with teacher forcing; with PREDICTED
  key it is .749 — the teacher-forcing bound travels with the figure)"*.

**EVERY PART OF V9's LOCATOR IS EXACT AT THE OBJECT.** Table 4, page 6, *All data* block:

- **line 4, RNBert (unconditioned): Degree .762**
- **line 6, RNBert (key conditioned, teacher forcing): Degree .859**
- **line 5, RNBert (key conditioned): Degree .749**

The table, the two lines the pair comes from, the third line the bound comes from, and the
conditions attached to each are all as V9 states them. **V9's VERIFIED verdict does not move and no
value changes.** The whole of Table 4 is transcribed in "The measured results" below, so the three
cells can be read in their context.

**THE MECHANISM CONFIRMED.** §3.6 "Key conditioning", pages 4–5, in the paper's own words: *"In
these key-conditioned experiments, we embed the key tokens with a two-layer MLP with hidden and
output dimensions of 256 and GELU activation. We then concatenate this key embedding with the
output from MusicBERT to obtain the input to the Roman numeral classification heads."* And: *"In
training, we employ teacher forcing, that is, we condition on the ground-truth key annotations from
the labeled data. In evaluation, we first predict the key with a separately fine-tuned model, then
condition the chord predictions on these predicted keys."*

**PRECISION (1) — THE PAPER CALLS LINE 6 A SANITY CHECK, NOT A RESULT.** §4.1, page 5, first
paragraph, verbatim:

> *"In Table 4, line 6, it can be seen that conditioning the Roman numeral prediction on the
> ground-truth key (i.e., teacher forcing) has a large effect on degree accuracy. This constitutes a
> sanity check that the conditioning works as expected: if the model knows the key of the
> annotation, its ability to predict the Roman numeral's degree shoots up."*

So the author's own reading of the 9.7-point rise is that the wiring is connected — the model given
the answer to the key does better at the question that depends on it — and not that the machinery
improves the analysis.

**PRECISION (2) — THE DEPLOYABLE CONDITIONING MOVES DEGREE ACCURACY THE OTHER WAY, AND THE AUTHOR
SAYS SO.** Line 5 is the same conditioning with the key **predicted** by a separately fine-tuned
model, which is what a running system would have. Derived at Table 4, sign convention *line 5 minus
line 4, positive meaning the conditioned model higher*: **Degree −.013** (.749 against .762),
Quality −.003, Inversion 0.000, Key +.001, **RN₋root +.004** (.624 against .620). §4.1, page 5–6:

> *"It is somewhat harder to interpret a comparison of RNBert, conditioned on the predicted key
> (line 5), with the unconditonal RNBert (line 4). The unconditional model does better predicting
> degree, but the conditioned model does better predicting the composite RN₋root. These results make
> sense if key conditioning makes the key and Roman numeral predictions more coherent with one
> another."*

*(«unconditonal» is the paper's own spelling at that sentence and is recorded as printed.)* The
author's stated mechanism for the direction is in the same paragraph: an unconditional model that
gets the key wrong will still hit the labelled degree some of the time, which lifts its degree
accuracy without lifting the analysis.

**PRECISION (3) — THE SAME FIGURE IS LOAD-BEARING IN TWO PLACES OF THE RECORD AND THE
TEACHER-FORCING BOUND BEARS ON THEM DIFFERENTLY. This is the reading this extract most wants
carried.** At **§S4's entanglement argument (line 1642)** the claim is that chord and tonality are
entangled, and there the ground-truth key is exactly the right instrument: giving the model the true
tonality and watching the degree accuracy move 9.7 points is a clean demonstration that the degree
decision depends on the tonality, and the bound costs that claim nothing. At **DP-A (line 681) and
§S4(a) (lines 1566–1567)** the same figure is offered as an instance of *"machinery to undo the
separation"* — of a later system's remedy working — and there the bound is the whole of the matter,
because the only measurement of that remedy under conditions a system could actually run in is
**−.013 on the metric the sentence names** and **+.004 on the composite**. **Neither DP-A's live
sentence nor §S4(a)'s carries the bound; V9 does.**

**PRECISION (4) — "THE DEGREE HEAD" IS NARROWER THAN WHAT THE PAPER CONDITIONS.** The key embedding
is concatenated into the input of **all** the Roman numeral classification heads (§3.6), not the
degree head alone. The effect concentrates on degree because, in the author's words at §4.1, *"key
conditioning, with or without teacher forcing, has little effect on the 'quality' and 'inversion'
metrics… since these tasks do not depend on the key: a first-inversion minor chord is a
first-inversion minor chord regardless of the key in which it occurs."* Table 4 bears that out:
Quality −.002 and Inversion 0.000 between lines 4 and 6.

**HOW THIS IS GRADED, STATED SO IT CAN BE OVERRULED.** It is **NOT** graded a corrected structural
claim and **no STOP of either class fires on it**. Every figure is reported by the paper, which is
all DP-A's `[FACT]` tag claims; the pair is at the cells V9 names; the machinery the sentence
describes exists and is described correctly; and the record already carries the bound at V9. What is
imprecise is that two of the three live sentences state as a system's gain what the paper states as
a sanity check, where the deployable form of the same machinery runs the other way on the metric
those sentences name. **Stated accurately it would make DP-A's chosen "no" stronger rather than
weaker** — a remedy for divided heads that does not pay when the tonality must itself be predicted
is an argument against dividing them — which is the same shape as row 45's finding (1) and is why
that finding was graded STOP-shaped where this one is not: there the record's claim was false at the
object, here it is true and incomplete. **A reader who weighs the two live sentences as claims about
the machinery WORKING may grade this a corrected structural claim; the facts for both readings are
above.** Routed to the findings surface's DP-A block and to L2's detail specification; **applied
nowhere.**

## ★ The verification target (b) — §S4(a)'s decoherence claim, CONFIRMED, with three precisions

`FRAMEWORK.md` §S4(a), lines 1561–1562: *"RNBert names the failure exactly — a passage genuinely
ambiguous between `I` and `vi6` can draw an incoherent composite `I6`."*

**CONFIRMED at §3.3, page 3, in the paper's own words:**

> *"It should be noted, however, that this multitask approach may obtain a smaller vocabulary size at
> the expense of some coherence among the different elements of the Roman numeral. For example,
> suppose there is a passage that is ambiguous between I and vi6 (two chords which share two of their
> three pitch-classes as well as the same bass note). If the model distributes the probability
> roughly equally between the two possibilities it may easily occur that the inversion and degree
> predictions "decohere" and we end up with a plainly incorrect prediction like I6 (rather than I) or
> vi (rather than vi6). (One solution to this problem of decoherence was proposed by [21], which we
> discuss in Section 3.6 below.)"*

The record's *"exactly"* survives: the pair is the same pair, the composite is the same composite,
and the reason given — two chords sharing two of three pitch classes and the same bass note — is the
paper's own. **Nothing is owed to that sentence.**

**PRECISION (1) — IT IS A CONSTRUCTED EXAMPLE, NOT AN OBSERVED CASE.** *"suppose there is a
passage"* and *"it may easily occur"*: the author is arguing that the multitask decomposition can
decohere, not reporting that it did. **No figure for label incoherence appears anywhere in the
paper.** This is the same shape as row 45's finding (1), where DP-A's *"the papers measure what
happens when they are allowed to disagree"* met a paper that measures nothing about it — **and it is
recorded BESIDE row 45's finding, not merged with it**, because §S4(a)'s sentence here claims only
that the paper NAMES the failure, which it does.

**PRECISION (2) — THE PAPER NAMES TWO INCOHERENT COMPOSITES, THE RECORD ONE.** *"I6 (rather than I)
**or vi (rather than vi6)**"*. Recorded so a later citation does not narrow the example to the half
the record quotes.

**PRECISION (3) — THE PAPER'S OWN WORD FOR THE FAILURE IS "DECOHERE" / "DECOHERENCE".** §S4(a) does
not use it. A detail specification quoting this passage should carry the author's term, which is
what §3.6 and the reference to [21] both hang on.

## ★ The verification target (c) — §S4's entanglement argument, a place the carried items do not name

`FRAMEWORK.md` line 1642, inside "The entanglement argument, stated once": *"**Chord ↔ tonality.**
Rocher's ablation, above; C36; and RNBert's measured degree gain from conditioning on the tonality.
[FACT.]"*

**CONFIRMED, and this is the one of the three live places the teacher-forcing bound does NOT
weaken** — see precision (3) above. The measured degree gain from conditioning on the tonality is
Table 4's line 6 against line 4, **+.097**, and it is measured with the tonality given, which is
precisely what an entanglement claim wants: it isolates the dependence of the degree decision on the
tonality from the difficulty of finding the tonality. **Nothing is owed to the bullet.** **One
precision:** the bullet's `[FACT]` covers three items and this reader verified only the third; the
Rocher ablation and C36 were not re-examined here.

**Why this place is recorded at all:** the nine carried items name DP-A, §S4(a) twice and V9, and
this is a fourth live use of the same paper, carrying a `[FACT]` tag, inside the argument that makes
L2's four questions **one decision**. It was found by the identity sweep, which the figure sweep
could not reach because the bullet carries no number. Routed to the findings surface; **applied
nowhere.**

## ★ The carried item (b) — ANSWERED: the "replacing" wording is RNBERT's own, verbatim

`population.md` V9 quotes RNBERT §4 describing AugmentedNet's re-fusion as *"replacing the quality,
degree, and root predictions with a vocabulary of the 75 most common Roman numerals"*. **At the
object, §4, page 5, the sentence reads in full:**

> *"Finally RN_alt refers to an alternate task learned in [6, 10], replacing the quality, degree, and
> root predictions with a vocabulary of the 75 most common Roman numerals in the AugmentedNet v1
> training set. We did not train RNBert on this task, but we report the prior results on it to
> facilitate comparison with our results."*

**So the wording is RNBERT's own and V9 quotes it correctly and in context** — the question row 48's
read left open is answered, and it is answered against the record's compression having introduced
anything. **The precision that remains is about RNBERT's description of AugmentedNet, not about the
record:** the sentence describes a **task** whose label vocabulary replaces those three predictions,
and **row 48's read established at AugmentedNet's own text that its six conventional heads are all
still learned and all still reported**. Read as a claim that AugmentedNet drops those heads, the
sentence would be wrong; read as a description of the RN_alt task, which is what it says, it is
right. **This is a precision on a second-hand description and not a correction of AugmentedNet,
which row 48 settled at the primary.** Routed to the findings surface's V9 row; **applied nowhere.**

## ★ The carried item (g) — ANSWERED at a SECOND held primary: "Micchi et al. 2021" corroborated, still not held

RNBERT's reference **[21]**, page 7: *G. Micchi, K. Kosta, G. Medeot, and P. Chanquion, "A deep
learning method for enforcing coherence in Automatic Chord Recognition," in Proceedings of the
International Society for Music Information Retrieval Conference, 2021, pp. 443–451.*

**That is the same work row 49's reference [8] identified, now corroborated at a second held primary
and with page numbers added (443–451).** **It is still NOT HELD:** `docs/research_papers/
BIBLIOGRAPHY.md` was read whole this session and carries no row for it, and
`reading_pass/extracts/` was listed this session and holds no extract for it — **both checked at
their own objects by this reader, on the method warning row 48's read paid for and row 49's read
applied. Nothing is carried out of it.**

**AND RNBERT ADDS A MEASURED STATEMENT ABOUT [21]'s MECHANISM THAT NARROWS V9's PARENTHESIS FROM A
SECOND SIDE.** §3.6, page 5:

> *"Another attempt to encourage coherence between key and Roman numeral predictions is [21], who use
> a neural autoregressive distribution estimator (NADE). Their approach extends beyond ours insofar
> as it conditions each sub-task of the Roman numeral classification on the previous tasks. In
> preliminary experiments applying a similar approach to RNBert, we observed a small decline in
> performance across all metrics. We defer to future work a qualitative evaluation of these
> predictions and further similar experiments."*

Two things follow. **(i)** Two independently read primaries — row 49's paper and this one — describe
[21]'s mechanism as **NADE, an autoregressive conditioning of each sub-task on the previous ones**,
which is not the post-hoc reconciliation V9's parenthesis attributes to it. **Row 49's precision (2)
is therefore corroborated rather than merely repeated**, and is recorded here beside it, unmerged.
**(ii)** This is a **third measured statement against cross-head dependency machinery**: row 49's
paper measures NADE at +2.1 over its baseline but −0.7 against its dynamically weighted loss and
concludes at §6 that such techniques are *"not particularly beneficial or necessary"*; this author
reports *"a small decline in performance across all metrics"* from a similar approach. **Its bound
travels with it:** *"preliminary experiments"*, *"a similar approach"* rather than [21]'s own, and
**no figure, no table and no uncertainty of any kind.** Routed to the findings surface's DP-A block
and to L2's detail specification; **applied nowhere.**

## ★ The carried item (h) — ANSWERED: the lineage narrative is confirmed from ONE END ONLY, a third time

Row 45's §5.1 proposes the consistency-enforcing post-processing that §S4(a)'s narrative says the
lineage's later systems supply. **This paper does not present its key conditioning as answering that
proposal.** Its reference [5] is Micchi, Gotham & Giraud 2020 (candidacy row 45) and it is cited at
§2 as prior work and at §3.3.1 for spelled inputs; **the decoherence discussion at §3.3 names [21],
not [5], as the proposed solution**, and §3.6 names [21] again. **So after rows 48, 49 and 50 —
three consecutive successors read at their own objects — §S4(a)'s narrative stands confirmed from
one end only: row 45 states the problem, and no successor says it is answering it.** **A datum, not
a defect**, and the third instance is what makes it worth recording as a pattern rather than as one
paper's silence. Routed to the findings surface's DP-A block.

## Identity — a MILD tier finding, and the row's short title MATCHES this time

**Printed title, page 1:** *"RNBERT: FINE-TUNING A MASKED LANGUAGE MODEL FOR ROMAN NUMERAL
ANALYSIS"*. **Author:** Malcolm Sailor, Yale University, `malcolm.sailor@gmail.com` — **one author.**
**The attribution box at the foot of page 1:** *"© M. Sailor. Licensed under a Creative Commons
Attribution 4.0 International License (CC BY 4.0). **Attribution:** M. Sailor, 'RNBERT: Fine-Tuning
a Masked Language Model for Roman Numeral Analysis,' in Proc. of the 25th Int. Society for Music
Information Retrieval Conf., San Francisco, United States, 2024."*

**The bibliography's row** (`docs/research_papers/BIBLIOGRAPHY.md` **line 69**) reads in full:
*"Sailor, "RNBERT," ISMIR 2024 | https://malcolmsailor.com/assets/RNBERT_ISMIR_Camera_Ready.pdf | ✓
| LINK (author copy)"*.

**(a) THE ROW'S SHORT TITLE IS THE PRINTED TITLE'S LEADING WORD.** The progress record's carried
warning was that *"RNBERT" may again be a short title that is the MODEL's name rather than the
paper's*, which is what row 49 turned out to be. **Here it is both**: RNBERT is the model's name and
it is the first word of the printed title, so the row matches as a leading word — the same shape as
rows 45, 47 and 48 and **not** row 49's. **The author and the venue match**, which row 49's row could
not offer at all.

**(b) THE PAPER PRINTS THE NAME TWO WAYS AND THE RECORD FOLLOWS THE SECOND.** The title and abstract
print **RNBERT**; the body text and footnotes print **RNBert** (for example footnote 3, *"RNBert's
performance"*). `FRAMEWORK.md` writes *RNBert* and `population.md` writes *RNBERT*; **both spellings
are the paper's own** and neither is a record error. Recorded so a later search covers both, which
is why this read's identity sweep was run case-insensitively.

**(c) A TIER PRECISION, THE SAME SHAPE AND DIRECTION AS ROWS 30's AND 49's.** The row's
redistribution tier is **LINK (author copy)**; the document prints **CC BY 4.0**, which is the
register's own **CC** tier. Routed to the bibliography reconciliation. **The author-copy-versus-
proceedings question does not arise as a finding:** the held file is the camera-ready and prints the
ISMIR attribution box naming the 25th ISMIR conference, San Francisco, 2024, so the venue the row
states is established at the held document itself — row 49's shape.

**The input, established at §3.2 and §3.3.1, pages 2–3: SYMBOLIC ONLY, AND UNSPELLED.** Scores in
MusicXML, MuseScore or Humdrum are converted to a tabular form and encoded for MusicBERT, which
*"uses unspelled pitch inputs (midi numbers like '67') rather than letter names (like 'F#5')"*.
**This is the first member of group 3 read at the object whose input discards the spelling the score
carries** — rows 45, 48 and 49 are all spelled. **So no domain caveat under the candidacy
derivation's consequence (ii) applies** (it is symbolic Western classical music, our own input kind),
but the L0 boundary condition does: see the adopt-or-argue section.

**Structure of the held document:** six numbered sections — 1 Introduction; 2 Related Work; 3
Experimental Setup (§3.1 Corpus; §3.2 Data representation; §3.3 Task, with §3.3.1 Pitch spelling;
§3.4 Data augmentation; §3.5 Model, with §3.5.1 MusicBERT, §3.5.2 Token classification, §3.5.3
Fine-tuning procedure; §3.6 Key conditioning; §3.7 Post-processing steps); 4 Results and Discussion
(§4.1 Effect of key conditioning; §4.2 The problem of multiple acceptable analyses); 5 Conclusion; 6
References. **Two figures, four tables, twenty-nine numbered references** — the reference list runs
[1] to [29] and was read whole. Eight pages. *(The section names above are taken from the printed
headings themselves, read on the pages, not from where a passage was found.)*

**File:** `docs/research_papers/sailor_2024_ismir_rnbert.pdf` (707,204 bytes at this session's
`docs/research_papers/` listing, the one file of that listing whose name matches the row).

## Claims, labeled

### The task and the approach (§1, §2, §3.3, §3.5, pages 1–4)

- **[FACT]** The abstract states the contribution: *"this paper applies pretraining methods to a
  music theory task by fine-tuning a masked language model, MusicBERT, for roman numeral analysis. We
  apply token classification to get a chord label for each note and then aggregate the predictions of
  simultaneous notes to achieve a single label at each time step. The resulting model substantially
  outperforms previous roman numeral analysis models."*
- **[FACT]** §2: *"All of these models for Roman numeral analysis are trained from scratch, not
  making use of self-supervised pretraining."* And: *"As far as we know, the best performance in the
  existing literature has been obtained by AugmentedNet [6, 7] and ChordGNN [10], and we compare our
  results below with those reported in [6, 10]."* — **[6] is candidacy row 48 and [10] is candidacy
  row 49.**
- **[FACT]** §3.3: Roman numeral analysis is *"framed… as a multitask learning problem, where we
  predict the key, quality, inversion, and degree separately. (The degree is sometimes further
  decomposed into 'primary' and 'secondary' components, but in the current work, we predict these
  jointly.)"* — **four tasks, where rows 45, 48 and 49 carry six, eleven and eleven.**
- **[FACT]** §3.3's decoherence passage, quoted in full under "The verification target (b)" above.
- **[FACT]** §3.5.1: the model fine-tuned is MusicBERT [11], *"a bidirectional transformer encoder
  pretrained on a masked language modeling task"* over *"a corpus of over 1 million midi files, 3
  orders of magnitude larger than our Roman numeral dataset."* The "base" architecture is used:
  hidden dimension 768, 12 layers, 12 attention heads.
- **[FACT]** §3.5.2: *"we adopt a token classification approach, predicting the key and Roman numeral
  for each token in the input. Since each token corresponds to a note, this amounts to predicting the
  chord during which each note occurs. While training, we calculate the loss on a per-token basis. In
  evaluation, in order to obtain a single prediction for each token in the input, we average the
  logits of simultaneous notes."* The heads are two-layer MLPs of inner dimension 768.
- **[FACT]** §3.5.2: *"To obtain the overall loss, we simply take the mean of the cross-entropy loss
  for each individual task. We tried learning a weighting of the contribution of each task to the
  global loss, following the approach introduced by [28] and implemented in an MIR context by [29],
  but observed a small degradation in model quality when doing so."*
- **[FACT]** §3.6's key-conditioning description and §3.7's post-processing description, both quoted
  in full above and below.

### Data representation and the grid (§3.2, pages 2–3)

- **[FACT]** *"First, following MusicBERT, the score is quantized at the 64th note level."*
- **[FACT]** *"Second, we 'salami-slice' the score: at each timestep with one or more onsets or
  releases, we split any ongoing notes into two, in order to obtain a purely homophonic rhythmic
  texture in which all onsets and releases are synchronized across all parts."* And: *"Salami-slicing
  is necessary to ensure that each note belongs to only one chord."*
- **[FACT]** *"Fortunately for our purposes, salami-slicing should not affect harmonic analysis,
  because it does not change the pitch content of the score. Moreover, musical idioms like
  suspensions and pedal tones that cross changes of chord are analyzed the same whether or not they
  are tied or sounded anew at the onset of the new chord."*
- **[FACT]** *"Third, we dedouble the notes of the score, removing any notes that have the same
  pitch, onset, and release"*, with two stated advantages — a shorter sequence and a more homogeneous
  texture across ensemble sizes.
- **[FACT]** §3.2: *"MusicBERT has a maximum sequence length of 1000 tokens. Therefore, in both
  training and evaluation, we crop scores into segments of 1000 tokens, stepping through the score
  with a hop size of 250."*

### Pitch spelling (§3.3.1, page 3)

- **[FACT]** *"One difference between our approach and some prior work (e.g., [5, 7]) is that
  MusicBERT uses unspelled pitch inputs (midi numbers like '67') rather than letter names (like
  'F#5'). Our output key predictions are therefore also unspelled (e.g., pitch-class 6, rather than
  'F-sharp'), because, with unspelled inputs, the output spelling is undefined."*
- **[FACT]** *"We consider our model's inability to predict spelled keys unimportant. Given spelled
  inputs (e.g., pitches like 'Db5' rather than MIDI numbers like '61') and an unspelled key (e.g., '1
  major'), predicting a spelled key (e.g., 'Db major') is trivial and could likely be performed with
  perfect accuracy by a rule-based algorithm (e.g., taking the enharmonically equivalent key closest
  to the centroid of the spelled pitches on the 'line of fifths' [23]). Moreover, keys with plausible
  enharmonic equivalents (like F-sharp major or E-flat minor) are rarely used. Their classification is
  therefore unlikely to significantly affect validation/test performance."* — **[23] is Temperley,
  "The Line of Fifths", Music Analysis 19(3), 2000.**

### Corpus, augmentation, fitting and evaluation (§3.1, §3.4, §3.5.3, §4, pages 2–5)

- **[FACT]** §3.1: *"To our knowledge, the corpus used in this study is the largest yet assembled for
  Roman numeral analysis."* Its named components are the DCML corpora [15–17], TAVERN [18], the
  Beethoven Piano Sonatas of [4], When in Rome [19] including Bach preludes and chorales, and *"a
  large number of 19th century lieder, including works by women composers."*
- **[FACT] Table 1, page 2, transcribed whole:**

| Data subset | Scores | Notes | Chords |
|---|---|---|---|
| All | 1,404 | 1,289,888 | 161,473 |
| AugmentedNet v1 | 347 | 701,703 | 77,570 |

- **[FACT]** §3.1: *"For a fair comparison with [6, 10], we also train and evaluate on the subset of
  our data used in those papers, employing the same training/validation/testing splits."* For TAVERN
  scores with two annotators' analyses, *"AugmentedNet v1 includes both versions (following [6]),
  whereas in the full corpus, we randomly choose only one of the two versions for inclusion"* — the
  duplicates comprising 106,981 notes.
- **[FACT]** Footnote 3: *"7 scores from AugmentedNet v1 were excluded because of preprocessing
  errors… These scores exclusively came from the training split and so, if their omission has any
  effect on RNBert's performance relative to that of the other models trained on the AugmentedNet v1
  dataset, it should bias it downwards."*
- **[FACT]** §3.1: *"Unlike some prior work (e.g., [6, 9]), we do not experiment with training and/or
  evaluating on smaller, more homogenous subsets of our corpus (for example, the Beethoven piano
  sonatas only)."*
- **[FACT]** §3.4: transposition to all 12 chromatic keys, and a duration-scaled version of each
  score (×2 or ÷2 toward the training set's mean duration), both on training data only.
- **[FACT]** §3.4: *"We experimented with adding synthetic data similar to the procedure introduced
  in [6, 7] and also adopted in [10]. However, we did not find that it improved the model
  performance."* The stated reason: for AugmentedNet the inputs are pitch vectors at each time step,
  *"for our model, the inputs are simply the notes of the score, and therefore the difference between
  synthetic and real data is more apparent to the model."*
- **[FACT]** §3.5.3: *"we found it important to freeze parts of the model to reduce the number of
  trainable parameters and avoid overfitting. Freezing the first 9 layers of MusicBERT seemed to give
  the best results."* Learning rate 2.5 × 10⁻⁴, linear warmup of 2500 steps then linear decay to 0;
  50,000 fine-tuning steps for multi-task Roman numeral classification, 25,000 for key classification
  only. And: *"When experimenting with varying these hyperparameters, we did not typically find their
  precise values to have much effect on the performance of the model. This implies that the
  fine-tuning is fairly robust to different hyperparameter choices."*
- **[FACT] Table 3, page 4** — parameter counts: Base 108,805,598 total, 26,782,729 trainable; Key
  conditioned 111,023,816 total, 28,859,891 trainable.
- **[FACT]** §4: *"Table 4 provides our results, expressed following [6] as the proportion of time
  that the predicted labels are accurate, with 32nd-note resolution."*
- **[FACT]** §4: the composite labels are defined — *"RN₋root refers to the conjunction of degree,
  quality, inversion, and key, while RN₊root adds to these the chord root. Predicting the root is
  redundant: the root of a Roman numeral is a deterministic function of the degree and key (e.g., the
  root of #iv in C major is F-sharp)."* — so the full-corpus models predict no root and report only
  RN₋root, while the AugmentedNet v1 models predict the root for comparability, *"It can be seen that
  the inclusion or exclusion of the root makes almost no difference, as one would expect."*
- **[FACT]** §4's RN_alt sentence, quoted in full under "The carried item (b)" above.

### The post-processing, including a tonality-axis decode (§3.7, page 5)

- **[FACT]** *"In postprocessing, we collate the predictions from each segment, combining the
  overlapping logits of adjacent segments by linearly interpolating between them… We then average the
  logits of simultaneous notes to obtain a single set of logits for each salami-slice."*
- **[FACT]** *"To avoid implausibly brief key changes of one or two salami-slices' duration (which
  otherwise sometimes occur at transitions between keys, when the model estimates both keys to be
  approximately equiprobable), we use a dynamic programming approach to decode the key predictions.
  Specifically, we employ the Viterbi algorithm, using RNBert's output probabilities as the emission
  probabilities and defining a transition probability matrix that is uniform, except for
  self-transitions, whose probabilities are upweighted. This decoding scheme has a negligible effect
  on the measured accuracy of the predictions, while effectively eliminating implausibly brief key
  changes."*

### The results and the author's readings of them (§4, §4.1, §4.2, §5, pages 5–6)

**[FACT] Table 4, transcribed whole, both blocks, every cell re-checked at the image on a second read
of page 6.** The caption states: *"Accuracy of RNBert and two prior models. The meanings of RN₊root,
RN₋root, and RN_alt are described in Section 4. In the model comparison of lines 1–3, we indicate the
best metric in bold type. Because the teacher-forcing model on line 6 does not predict key, and RN
prediction involves key prediction, we do not report RN results for this model."* A blank cell is
printed where the model reports no value; bold is reproduced below as printed.

| | Model | Degree | Quality | Inversion | Key | RN₊root | RN₋root | RN_alt |
|---|---|---|---|---|---|---|---|---|
| | *AugmentedNet v1 data subset* | | | | | | | |
| 1 | AugmentedNet [6] | .67 | .797 | .788 | **.829** | .464 | | .515 |
| 2 | ChordGNN+(Post) [10] | .714 | .784 | **.803** | .813 | .518 | | .529 |
| 3 | RNBert (key conditioned) | **.731** | **.819** | .796 | .825 | **.574** | **.575** | |
| | *All data* | | | | | | | |
| 4 | RNBert (unconditioned) | .762 | .867 | .872 | .822 | | .620 | |
| 5 | RNBert (key conditioned) | .749 | .864 | .872 | .823 | | .624 | |
| 6 | RNBert (key conditioned, teacher forcing) | .859 | .865 | .872 | N/A | | N/A | |

*(AugmentedNet's Degree cell is printed to two decimals where every other cell carries three;
recorded as printed.)*

- **[FACT]** §4: *"When training on the AugmentedNet v1 subset (Table 4, line 3), RNBert
  substantially outperforms the prior models on degree and quality. However, it outperforms the
  earlier models by a much more substantial margin when predicting the composite Roman numeral
  RN₊root. This implies that there is more coherence among the various dimensions of its predictions.
  Such coherence may be due to the robustness of the representations MusicBERT learns in its
  pretraining. It implies that, even where RNBert's predictions don't agree with a human annotator's,
  they are more likely to be useful, since they are more likely to be internally consistent."*
- **[FACT]** §4: *"One thing to note about these results is that, while the models on lines 4 and 5
  greatly exceed the performance of the models on lines 1–3 on degree, quality, inversion, and RN₋root
  prediction, when it comes to key prediction, the AugmentedNet v1-trained models actually perform
  better (with the exception of the ChordGNN model). We believe this occurs because key prediction on
  the subset is simply an easier problem, since it contains less music from the late 19th century and
  beyond, a period when music tended to modulate more widely."*
- **[FACT]** §4.1's two paragraphs, quoted in full under "The verification target (a)" above.
- **[FACT]** §4.1 and Figure 2, the worked example on Beethoven's String Quartet in F major, op. 18
  no. 1, iv, mm. 7–8: the two RNBert analyses differ at one chord, the cadential six-four on the
  downbeat of the second measure, where *"the conditioned model gives the correct annotation I64/V,
  the unconditioned analysis gives I64, which is incorrect, since this is a C major chord, and the
  annotated key is F. The unconditional model's key and Roman numeral predictions are each plausible
  on their own—I64 is the most common annotation for a cadential 64 chord—but they do not cohere with
  one another. And yet, in spite of being incorrect with respect to its predicted key, this I64
  prediction happens to agree with the ground truth, and thus the degree accuracy of this example is
  (spuriously) higher for the unconditioned model."*
- **[FACT]** §4.2: *"One important problem in evaluating Roman numeral analysis models is that there
  is often more than one correct analysis of a musical passage, so that a model's predictions can be
  labeled 'inaccurate' even when they present valid alternate readings."* And: *"On a priori grounds,
  as well as based on qualitative sampling of the model's predictions, we suggest that a high
  proportion of RNBert's 'inaccurate' predictions are likely to be acceptable alternate analyses."*
  And: *"These considerations may place a ceiling on the accuracy of all Roman numeral analysis
  models."*
- **[FACT]** §5: *"In the specific case of Roman numeral analysis, we suggest that Roman numeral
  analysis models have now matured to the point where they are ready to be used in large-scale
  musicological studies."* Future extensions named: *"the analysis of dissonant idioms (suspensions,
  passing tones, and the like) or melody harmonization."*
- **[FACT]** Footnote 2, page 1: *"Unfortunately, the results of [7] are reported in a manner that
  makes them difficult to compare directly with these other papers and with our own results."* — [7]
  is Nápoles López's 2022 PhD dissertation.

### Derived here, with the sign convention stated, and read as directions only

**Table 4 prints no uncertainty of any kind — no spread, no repeat count and no significance test —
so every difference below is a direction and not a result** (#24).

- **[DERIVED] Key conditioning at the PREDICTED key, line 5 minus line 4, positive meaning the
  conditioned model higher:** Degree **−.013**, Quality −.003, Inversion **0.000**, Key +.001, RN₋root
  **+.004**. **The metric the record's sentence names moves DOWN; the composite moves up.**
- **[DERIVED] Key conditioning at the GROUND-TRUTH key, line 6 minus line 4:** Degree **+.097**,
  Quality −.002, Inversion **0.000**. Key and both composites are N/A on line 6 by the caption's own
  statement.
- **[DERIVED] RNBert against ChordGNN+(Post), line 3 minus line 2, positive meaning RNBert higher:**
  Degree +.017, Quality +.035, Inversion **−.007**, Key +.012, **RN₊root +.056**.
- **[DERIVED] RNBert against AugmentedNet, line 3 minus line 1:** Degree +.061, Quality +.022,
  Inversion +.008, Key **−.004**, **RN₊root +.110**.
- **[DERIVED] The author's coherence claim is borne out by the table as a direction:** on both
  comparisons the composite margin (+.056, +.110) exceeds every single-component margin, which is
  what §4's *"much more substantial margin"* sentence asserts. **Its bound is the same as row 49's
  §5.1 bound:** this is a comparison between three different architectures and not an ablation inside
  one, and no cell carries an uncertainty.
- **[DERIVED] ★ TABLE 4's LINES 1 AND 2 REPRODUCE ROW 49's TABLE 1 "FULL" BLOCK EXACTLY, ON EVERY
  SHARED METRIC.** Against the row 49 extract's own transcription, read whole this session — **row
  49's paper was not opened here and the ChordGNN figures are cited to that extract, not to that
  paper** — ChordGNN's Full block gives AugNet Key 82.9, Degree 67.0, Quality 79.7, Inversion 78.8,
  RN 46.4, RN_alt 51.5, and ChordGNN+Post Key 81.3, Degree 71.4, Quality 78.4, Inversion 80.3, RN
  51.8, RN_alt 52.9. **RNBERT's lines 1 and 2 carry .829 / .67 / .797 / .788 / .464 / .515 and .813 /
  .714 / .784 / .803 / .518 / .529 — the same twelve values as proportions.** Two things follow.
  **(i)** RNBERT's *"AugmentedNet v1 data subset"* and ChordGNN's *"Full"* set are the same evaluation
  set, which neither paper says in those words. **(ii)** **The record's own .462→.491 pair is from
  ChordGNN's BPS block, a DIFFERENT set from the one this paper compares on** — so the two ratified
  figures of rows 49 and 50 are not on a common footing and must not be read across. Recorded as a
  cross-primary check; **the progress record, read whole this session, records no earlier one, and no
  "first" is asserted.** Routed to measurement design and to the findings surface's DP-A block.
- **[DERIVED] The two read primaries of this lineage disagree on learned task weighting, and both are
  recorded as printed.** Row 49's paper measures its dynamically weighted loss at +2.8 Roman numeral
  points over its own baseline (cited to the row 49 extract's Table 2 transcription, read this
  session); this author *"observed a small degradation in model quality"* from learning a task
  weighting following [28], the same auxiliary-task-weighting line row 49's paper cites for its own
  loss. **Neither is reconciled here and no figure exists on this side of it.** Routed to L2's detail
  specification beside D-525 and DP-P.

## Coupling facts (mandatory)

**What the method ASSUMES about its upstream.**
- A **notated symbolic score** in MusicXML, MuseScore or Humdrum, converted to a tabular
  note-per-row form with onset, release and pitch. **Spelling is discarded** by the encoding: pitches
  are MIDI numbers.
- **A 64th-note quantisation**, applied before anything else, following MusicBERT.
- **A salami-sliced, dedoubled texture** — every ongoing note split at every onset or release in any
  part, so that onsets and releases are synchronised across parts, and exact duplicate notes removed.
- **A time signature MusicBERT's OctupleMIDI encoding supports** — seven scores were dropped for
  failing this (footnote 3).
- A **pretrained MusicBERT checkpoint**; the analysis-specific training is fine-tuning on top of it,
  with the first nine layers frozen.
- For TRAINING: Roman numeral annotations, on [6, 10]'s splits for lines 1–3 and on the author's own
  full corpus for lines 4–6; transposition and duration-scaling augmentation confined to training.

**What it HANDS downstream.**
- **Per-salami-slice labels for four tasks** — key, degree, quality, inversion — obtained by
  averaging the per-note logits of simultaneous notes; the root is predicted only in the AugmentedNet
  v1 configuration, and is declared redundant.
- **Two composite Roman numerals assembled from those heads**, RN₋root and RN₊root. **The assembly is
  a conjunction of head outputs, not a decision the model takes.** RN_alt is **not** learned by this
  model at all.
- **An UNSPELLED key**, by the encoding's own limit, with the author's argument that respelling it is
  trivial given the score.
- **A Viterbi-decoded key sequence** — the one place the model decides anything sequentially — over a
  transition matrix uniform except for upweighted self-transitions.
- **NO segmentation decision, no boundary variable, no segment and no length term on the chord
  axis.** A chord boundary exists only where two adjacent salami slices carry different labels.
- **No rivals, no confidence, no posterior published.** Logits exist at every head and at every note,
  are averaged and interpolated internally, and nothing is published from them.
- **No figured bass, no cadence, no phrase or section grouping, no harmonic rhythm head, no
  chord-tone assignment** — the last named at §5 as a task the approach *"could be readily extended
  to"*.

**Its own STATED SCOPE and limits.**
- **Domain:** Western tonal symbolic music, the author's assembled corpus of 1,404 scores, with the
  stated caveat that MusicBERT's pretraining is *"not trained solely or even mainly on Classical
  music"* and the author's argument that this does not matter because the tonal idiom is shared.
- **Decision scope:** key, degree, quality, inversion — and the root where trained for comparison —
  **per salami slice.** **Not** where the harmony changes as a decision; **not** which notes are
  harmonic; **not** the spelling of anything.
- **Fitting:** [6, 10]'s splits for the comparison rows; the author's own full corpus for the rest;
  hyperparameters reported as insensitive; layer freezing chosen because it *"seemed to give the best
  results"*, on a set the paper does not name.
- **The authors' own bounds:** the results of [7] are not directly comparable (footnote 2); a high
  proportion of the model's apparent errors may be acceptable alternate analyses, which *"may place a
  ceiling on the accuracy of all Roman numeral analysis models"* (§4.2); the NADE-style experiment
  was preliminary and declined (§3.6).

## What an L2 detail specification could adopt, adapt, or must argue against

- **★ MUST ARGUE AGAINST — the multi-head architecture, DP-A's rival for the fourth row of group 3
  running**, and here in its narrowest form yet: **four heads**, decided in one pass over a shared
  encoder, with **no consistency enforced anywhere in the model** and the coherence remedy —
  conditioning the Roman numeral heads on the key — **bolted on outside the deciding, trained with
  the true key and run with a predicted one**. The progress record's summaries of the three earlier
  reads, read whole this session, record row 45's system as six heads, row 48's as eleven with a
  re-fused *reconstruction* and row 49's as eleven with a post-hoc *re-deciding pass*; **this one is
  four heads with an *input-side conditioning*.** **What a detail specification must meet is that all
  four undo the separation somewhere other than in the deciding** — which is where DP-A's own cut is
  — **and that this one's remedy is the only one of the four whose deployable measurement is
  reported, and it is negative on the metric the record names.** Routed to L2's detail specification
  and to the findings surface's DP-A block.
- **★ A RIVAL SHAPE FOR WHERE THE REPRESENTATION COMES FROM, NEW TO THIS SLICE.** Every other member
  of group 3 read so far learns its encoder on the analysis task. This one **fine-tunes a
  general-purpose pretrained encoder** and attributes its coherence advantage to *"the robustness of
  the representations MusicBERT learns in its pretraining"* (§4). **That is a claim about where
  analytical competence comes from**, and a detail specification choosing a hand-built factorisation
  over a learned one has to meet it. Its bound: the attribution is the author's stated belief, not a
  measurement — no ablation removes the pretraining. Routed to L2's detail specification and to the
  findings surface's DP-A block.
- **★ MUST ARGUE AGAINST — the input contract runs the opposite way to L0's.** This system **throws
  away the spelling the notated score carries** and argues that the loss is unimportant because the
  spelling can be restored afterwards by a rule (§3.3.1, citing the line of fifths). **The record's
  L0 bullet says spelling is GIVEN and V3 records it measured to help tonality**; row 45's read
  records full spelling measured *not worse while performing a harder task*. **So this paper supplies
  the position DP-F must argue against, stated by an author who chose it for a practical reason —
  the pretrained model's encoding — rather than for an analytical one.** Recorded with the precision
  that the paper offers **no measurement either way**: it does not compare spelled against unspelled
  inputs. Routed to the findings surface's DP-F/G/H block and to L2's and L1's detail specifications
  beside V3 and D-450; **applied nowhere.**
- **★ ADOPT-OR-ARGUE — the salami-slicing grid is the L1 charter's own grid, where row 49's was
  not.** *"at each timestep with one or more onsets or releases"* — **onsets AND releases**, which is
  Pardo and Birmingham's partition-point construction and the L1 charter's ground at V8. **Row 49's
  read recorded that ChordGNN's grid is onsets only; this one is onsets and offsets.** So the two
  neighbouring members of the same lineage sit on opposite sides of the charter's own boundary rule,
  and this one sits on the charter's side. A datum for V8 and for the L1 charter, routed to the L1 and
  L2 detail specifications.
- **★ A TONALITY-AXIS STABILITY MECHANISM WITH ITS COST DECLARED — a fifth worked shape for the
  slice's length-term question.** The slice's four shapes so far are linear/exponential needing no
  segmental decode (rows 19, 20's baseline, 18), Gaussian needing it (row 11's example),
  unbounded-history needing an approximate decode (row 20's chosen model), and no length term at all
  (rows 45, 47, 48, 49). **This paper adds: no length term on the chord axis, and on the TONALITY
  axis a first-order self-transition bonus decoded by Viterbi AFTER the labelling, whose stated
  purpose is to remove key changes of one or two slices and whose stated cost is "a negligible effect
  on the measured accuracy".** It is the same mechanism row 30 fits as a Weber-table transition cost
  and row 26 carries in its transition matrix, **applied here as post-processing rather than inside
  the decision**, and **with no figure published for the negligible-effect claim.** Routed to L2's
  detail specification beside D-347, D-348 and DP-E, and to the findings surface's DP-E block.
- **A DATUM ON THE EVALUATION GRID, of the shape the slice has met before.** The model predicts per
  note, aggregates per salami slice, and the metric is *"the proportion of time that the predicted
  labels are accurate, with 32nd-note resolution"*, following [6] — a **duration-weighted metric on a
  fixed 32nd-note grid**, the same convention row 49's paper uses. Routed to measurement design
  beside D-115, row 19's mir_eval finding and row 20's WCSR.
- **★ AN ON-REPERTOIRE CEILING STATEMENT, from an author of the ground truth we use.** §4.2's
  multiple-acceptable-analyses argument and its *"may place a ceiling on the accuracy of all Roman
  numeral analysis models"*, made about symbolic classical music by a co-author of the When in Rome
  meta-corpus [19]. **Nothing is carried out of it as a value:** it is argued on a priori grounds
  plus qualitative sampling, with no agreement figure and no annotator study. Routed to measurement
  design beside principle #21, D-474, OI-179 and the findings surface's DP-K block; **applied
  nowhere.**
- **A DATUM AGAINST ROW 48's OWN HEADLINE CONTRIBUTION.** §3.4 reports that synthetic training data
  of the kind row 48 introduced and row 49 adopted *"did not… improve the model performance"* here,
  with the author's stated reason. Recorded as a successor's report on a predecessor's mechanism, not
  as a measurement of row 48's system; routed to L2's detail specification.
- **A DATUM ON WHERE THIS LINEAGE IS GOING, not a finding.** §5 names the analysis of dissonant
  idioms — suspensions and passing tones — and melody harmonisation as ready extensions. **That is
  DP-D's question named as a next task by a fourth author group**, and candidacy row 52's own reading
  will meet the same direction. Recorded, carried nowhere.

## ★ Findings, routed and not applied

**(1) THE RATIFIED FIGURE IS CONFIRMED AT ITS OWN CELLS, WITH FOUR PRECISIONS, AND THE THIRD IS THE
ONE THAT MATTERS.** Set out in full at "The verification target (a)". Table 4's *All data* block
carries **.762** at line 4 and **.859** at line 6, and **.749** at line 5, exactly where V9 locates
them; **V9 is VERIFIED in every part, including its bound.** The precisions: the paper calls line 6 a
**sanity check**; the deployable conditioning measures **−.013 on degree** and **+.004 on the
composite**; **the same figure carries different weight at its three live homes** — clean evidence of
entanglement at line 1642, a claim about machinery working at DP-A line 681 and §S4(a) lines
1566–1567, where neither sentence carries the bound V9 carries; and the conditioning reaches all the
Roman numeral heads, not the degree head alone. **Graded a precision and NOT a corrected structural
claim, with the reasoning stated at the target above so the user can overrule it.** Routed to the
findings surface's DP-A block and V9 row; **applied nowhere.**

**(2) §S4(a)'s DECOHERENCE CLAIM IS CONFIRMED VERBATIM IN SUBSTANCE**, with three precisions: the
passage is a **constructed example** and the paper measures nothing about label incoherence; the
paper names **two** incoherent composites where the record names one; and the paper's own word is
**"decohere"**. Recorded **beside** row 45's finding (1) and merged with it nowhere. Routed to the
findings surface's DP-A block; **applied nowhere.**

**(3) ★ A FOURTH LIVE PLACE OF THE RECORD RESTS ON THIS PAPER AND NONE OF THE NINE CARRIED ITEMS
NAMES IT.** `FRAMEWORK.md` line 1642, the entanglement argument's *Chord ↔ tonality* bullet, carrying
a `[FACT]` tag. **CONFIRMED at the object**, and it is the one live use of the figure the
teacher-forcing bound does not weaken. **It was found by the identity sweep, which the figure sweep
could not reach** — the bullet carries no number — **which is the mirror of DP-A line 681, which the
figure sweep reached and the identity sweep could not.** Routed to the findings surface; **applied
nowhere.**

**(4) THE CARRIED ITEM (b) IS ANSWERED: the "replacing" wording is RNBERT's own, quoted correctly by
V9.** What remains is a precision on RNBERT's description of AugmentedNet, which row 48 settled at
that system's own text. Routed to the findings surface's V9 row; **applied nowhere.**

**(5) THE CARRIED ITEM (g) IS ANSWERED AT A SECOND HELD PRIMARY.** RNBERT's reference [21] names
Micchi, Kosta, Medeot & Chanquion 2021 in full, with pages 443–451, corroborating row 49's [8]. **It
is still not held and no extract exists for it** — both checked at their own objects this session —
**and nothing is carried out of it.** Two independently read primaries now describe its mechanism as
**NADE**, which narrows V9's parenthesis from a second side. Routed to the bibliography
reconciliation and to the findings surface's V9 row; **applied nowhere.**

**(6) ★ A THIRD MEASURED STATEMENT AGAINST CROSS-HEAD DEPENDENCY MACHINERY, FROM A SECOND AUTHOR
GROUP.** §3.6: *"In preliminary experiments applying a similar approach to RNBert, we observed a
small decline in performance across all metrics."* Beside row 49's NADE row and its §6 conclusion,
this is two independent groups reporting that the machinery DP-A's ground names as the lineage's
remedy does not pay. **Its bound is stated with it: preliminary, no figure, and a similar approach
rather than [21]'s own.** Routed to the findings surface's DP-A block; **applied nowhere.**

**(7) THE CARRIED ITEM (h) IS ANSWERED, AND FOR THE THIRD SUCCESSOR RUNNING.** This paper does not
present its conditioning as answering row 45's §5.1 proposal; it names [21]. **§S4(a)'s narrative
stays confirmed from ONE END ONLY after rows 48, 49 and 50.** A datum, not a defect. Routed to the
findings surface's DP-A block.

**(8) ★ A CROSS-PRIMARY CHECK: ROW 50's TABLE 4 LINES 1 AND 2 ARE ROW 49's TABLE 1 "FULL" BLOCK.** Twelve values match to the digit as proportions, cited to the row 49 extract
read whole this session — **that paper was not opened here**. It establishes that the two papers'
comparison sets are the same set under two names, and that **the record's .462→.491 pair sits on
ChordGNN's BPS block, a different set from the one this paper's figures compare on**, so the two
rows' ratified figures must not be read across. Routed to measurement design and to the findings
surface's DP-A block.

**(9) THE PAPER DISCARDS PITCH SPELLING AND ARGUES THE LOSS AWAY WITHOUT MEASURING IT.** The
position DP-F must argue against, taken here for an engineering reason and defended by an appeal to a
rule-based respelling and to the rarity of enharmonically ambiguous keys — **with no experiment
either way in the paper.** Routed to the findings surface's DP-F/G/H block beside V3 and to L1's and
L2's detail specifications; **applied nowhere.**

**(10) FIT AND EVALUATION AT THE OBJECT.** The comparison rows reuse [6, 10]'s splits deliberately,
as row 49's paper does, so the held-out question is answered by **inheritance** for lines 1–3;
augmentation is confined to training; and the excluded scores are declared with their bias direction
argued. **What is absent: no uncertainty on any cell of Table 4, no repeat runs, no significance
test, and a layer-freezing choice made because it "seemed to give the best results" on a set the
paper does not name.** **The four read rows of group 3 now give the slice four differently reported
protocols on one lineage** — row 45's (every figure on a validation split, no held-out test set), row
48's (tuned on validation, run once on a test split), row 49's (row 48's splits reused, no procedure
of its own described) and this one's (splits inherited for the comparison rows, own corpus for the
rest, one selection choice undescribed). **The row 45 and row 48 halves are cited to the progress
record and to the row 49 extract respectively, neither of those papers having been opened here.**
Routed to measurement design beside D-097, D-574, principle #20 and principle #24; **applied
nowhere.**

**(11) AN ON-REPERTOIRE CEILING STATEMENT WITH NO FIGURE BEHIND IT.** §4.2, recorded at "adopt or
argue" above. Routed to measurement design beside principle #21, D-474 and OI-179; nothing carried
out of it as a value.

**(12) THE TWO READ PRIMARIES OF THIS LINEAGE DISAGREE ON LEARNED TASK WEIGHTING**, and both are
recorded as printed with no reconciliation attempted. Routed to L2's detail specification beside
D-525 and DP-P.

**(13) NO FALSIFIER of a chosen design point, so NO STOP of the falsifier class; and NO CORRECTED
STRUCTURAL CLAIM on a live recorded ground, so NO STOP of the remedial commission §5 class either.**
All three ratified places resting on this paper are CONFIRMED at the paper's own text. **Finding (1)
is the one a reader might grade otherwise, and the grounds for both readings are stated at the
verification target.**

## Centrality — CENTRAL, and a second independent extraction is OWED

**CENTRAL**, on three live places of the record resting on this paper — **the three are named here
and no comparison with any other row of the slice is asserted**: DP-A's and §S4(a)'s **.762→.859**
pair (a measured FIGURE), §S4(a)'s
**decoherence claim** (a claim about what the paper says), and **§S4's entanglement bullet at line
1642** (a `[FACT]` inside the argument that makes L2's four questions one decision) — and this read
verifies all three at the paper's own text. A detail specification arguing DP-A's chosen "no" will
cite this system's pair, and finding (1) changes what may be said when it does; the entanglement
argument's own bullet rests on the same cells. **A second independent extraction is OWED.**

**The ground on which NOT CENTRAL could be argued, stated in full so the verdict is challengeable
here.** All three items were already marked VERIFIED or were carried as sealed first-stage text, and
this read confirms rather than corrects them, so no value and no verdict moves. Nothing in the
architecture would be adopted: a fine-tuned general-purpose transformer is DP-A's rival, not a
candidate. The paper decides no segmentation, no chord-tone assignment and no boundary, and it
discards the spelling L0 gives. And every figure it reports is a **single run with no uncertainty**,
which bounds how much any argument can lean on it. **A reader who weighs those points may grade this
row NOT CENTRAL and drop the second pass; the facts for both readings are above.**

## What this extract does NOT do

It amends nothing. `FRAMEWORK.md` (DP-A, DP-F/G/H, §S4(a), the entanglement argument),
`reading_pass/candidacy_upgrades.md`, `cowork_l2_task_b_slice_derivation_2026_09_05.md`,
`reading_pass/population.md`, `cowork_reading_pass_findings_2026_08_31.md` and
`docs/research_papers/BIBLIOGRAPHY.md` all stand exactly as they stand. **Row 18's finding (3), row
47's two corrected structural claims and row 45's finding (1) are not applied, not restated as
settled and not built on** by anything here; where this paper's text bears on the same passages, it is
recorded **beside** them. Row 48's finding (2) and row 49's after-training precision are treated the
same way.

**Not read, and nothing carried out of any of it:** the paper's released code
(`https://github.com/malcolmsailor/rnbert`); its corpora — the DCML corpora, TAVERN, the Beethoven
Piano Sonatas set, When in Rome, and the 19th-century lieder it names — and MusicBERT's own
pretraining corpus; and every work it cites, among them **Micchi, Kosta, Medeot & Chanquion 2021
(reference [21]), which finding (5) corroborates and which is NOT HELD**, together with Pauwels et
al. 2019, Aldwell/Schachter/Cadwallader 2011, Kostka & Payne 2004, Chen & Su 2018, 2019 and 2021,
Micchi, Gotham & Giraud 2020, Nápoles López, Gotham & Fujinaga 2021, Nápoles López 2022,
Karystinaios & Widmer 2023, Zeng et al. 2021 (MusicBERT), Chou et al. 2021 (MidiBERT-Piano), Devlin
et al. 2019, Li et al. 2023, Neuwirth et al. 2018, Hentschel et al. 2021, Hentschel et al. 2022,
Devaney et al. 2015, Gotham et al. 2023, White & Quinn 2016, Badura-Skoda 1995, Temperley 2000,
Huang et al. 2018, Oore et al. 2020, Huang & Yang 2020, Hsiao et al. 2021, Liebel & Körner 2018 and
Qiu et al. 2022 — **were not fetched and are not read; only the held file was.** The ISMIR 2024
proceedings deposit of this paper was not fetched; the held camera-ready PDF is what was read.

---

*Provenance: Cowork, 2026-09-06, the fifteenth reading session of L2's slice, after the ordinary
session-start read (`CLAUDE.md` whole, loaded by the harness; `DECISIONS.md` whole; `STATUS.md`
whole; the derived gating answer at `tools/audit/nongating_apparatus_rows.json` →
`★_the_live_gating_answer`, its three counts and its `gating_ids` list whole), the hundred-and-thirtieth
handoff entry whole, the hundred-and-eighteenth entry whole for its bridge-fault section,
`reading_pass/l2_slice_reading_progress.md` whole, `reading_pass/candidacy_upgrades.md` whole, both
commissions whole, `cowork_l2_task_b_slice_derivation_2026_09_05.md` whole,
`docs/research_papers/BIBLIOGRAPHY.md` whole, the row 49 extract whole for the form and for its
Table 1 and Table 2 transcriptions, `FRAMEWORK.md` at the design-point opening with DP-A to DP-H
(660–719), at §S4's L0 bullets with §S4(a) to §S4(d) (1528–1597) and at the entanglement argument
(1630–1659), and `reading_pass/population.md` at its verification rows V3 to V13 — **the section
names taken from the printed headings on the pages themselves and not from where a passage was
found**. The `reading_pass/extracts/` and `docs/research_papers/` directory listings were both read,
the first on the method warning row 48's read paid for and row 49's applied. The tip was re-read at
both ref files with the file tools and stands at `911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb`. Every
file was read with the file tools from bridge-staged copies; no shell read repository content or any
staged copy of it. No figure of this project's own measurement is restated (#17f, D-431); every value
above is this paper's own, or is derived here from this paper's own table with the sign convention
stated, or is cited to the row 49 extract where it is that paper's.*
