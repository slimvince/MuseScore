# Row 1 — SECOND INDEPENDENT EXTRACTION

**Raphael, Christopher & Stoddard, Josh — "Harmonic Analysis with Probabilistic Graphical Models",
ISMIR 2003.**

Held at `docs/research_papers/raphael_stoddard_2003_ismir_harmonic_analysis_pgm.pdf`, 93,277 bytes at
a bridge listing of `docs/research_papers/`. **Read AT THE OBJECT, as page images with the file
tools, whole — all five pages.**

---

## §1 — What this file is, and the bound on its independence

This is the **second** of the two independent extractions the reading-pass commission's §4 requires of
a CENTRAL source: *"CENTRAL sources … are extracted in a SECOND independent pass (a fresh session, or
a cleanly separated re-read that does not consult the first extract) and the two extracts
cross-checked; disagreements are resolved at the paper or recorded as unresolved."*
(`cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, read whole at the object this
sitting.)

**The route taken is the second one — a cleanly separated re-read in a session that has not opened the
first extract.** The first extract is
`reading_pass/extracts/raphael-stoddard-2003-harmonic-analysis-with-probabilistic-graphical-models.md`,
recorded at 22,611 bytes in the hundred-and-seventieth handoff entry's §1. **It was not opened before
§1 through §8 of this file were written.** The cross-check against it is a later section of this file,
written after this one had landed.

**THE CONTAMINATION, DECLARED RATHER THAN CLAIMED AWAY.** A session booting on the handoff line does
not arrive blank, and two things it read before opening the paper bear on this paper:

- **The hundred-and-seventieth entry's §1 states row 1's progress-record row**, and that row carries
  the first extract's own conclusion: *AT THE OBJECT, whole, all five pages, CENTRAL, second pass
  OWED*. So this side knew before reading that the first pass graded the paper CENTRAL. **It did not
  know on what ground.**
- **`cowork_reading_pass_remedial_commission_2026_08_31.md` §3 carries a starting hypothesis**, which
  that document states in terms is *"the writing side's reading of the bibliography, not an
  established set"*, and which names *"the probabilistic graphical model … as joint-decode
  designs"* among the papers it expects the candidacy derivation to admit. So this side knew before
  reading that the record expects this paper to bear on joint decoding.

**Neither was used as a finding and neither is repeated below as though this reading produced it.**
What this side did NOT hold when it read: the first extract's text, any figure it carries, its
Centrality reasoning, any question it recorded as owed to a second pass, and the progress record's own
table row beyond the summary quoted above. **The progress record was not opened at all in this
sitting.**

**The page count was established AT THE TOOL**, by a deliberately out-of-range page request, which
answered *"PDF has 5 pages"* and matches the progress row's *all five pages*. **Each of the five page
images was checked to be present and legible at the image itself, not at the call's success line**
(the standing page-image-fault cadence).

**The identity was checked before anything was extracted.** The paper's own page 1 prints the title
*Harmonic Analysis with Probabilistic Graphical Models*, the authors *Christopher Raphael* and *Josh
Stoddard*, both at *Dept. of Mathematics and Statistics, Univ. of Massachusetts, Amherst 01003-4515*,
and the copyright line *©2003 Johns Hopkins University*. `docs/research_papers/BIBLIOGRAPHY.md` line
15 reads *"Raphael & Stoddard, 'Harmonic Analysis with Probabilistic Graphical Models,' ISMIR 2003"*.
**They match, so no identity finding.** Page 1 also carries the funding footnote *"This work is
supported by NSF ITR grant IIS-0113496."*

**A BOUND THE BIBLIOGRAPHY ITSELF SUPPLIES AND THIS READING CANNOT CROSS.** The line immediately below
it, line 16, reads *"Raphael & Stoddard, 'Functional Harmonic Analysis Using Probabilistic Models,'
CMJ 28(3), 2004"*, marked **PAYWALL** and not held. **That is a later, longer treatment by the same
two authors, and it is not held and has not been read.** Nothing below is a statement about what the
2004 journal article contains — in particular, **the absence of any evaluation is a fact about the
2003 conference paper alone.** *(That the 2004 article treats the same system is this side's reading
of its title against this paper's, not something either document states to the other.)*

---

## §2 — What the paper is, in plain words

The two authors propose to take a piece of music in symbolic form, cut it into equal metrical
stretches, and give each stretch one label saying what the harmony is there. The label is a triple:
which note is the tonic, whether the passage is major or minor, and which scale degree the chord is
built on (I through VII). They do this with a hidden Markov model — a standard piece of statistical
machinery in which an unseen sequence of labels is assumed to march forward one step at a time with
fixed transition tendencies, and each label "emits" the notes you actually see.

Two properties follow from choosing that machinery, and the paper argues for both explicitly. First,
the label sequence that best explains the notes can be found **exactly**, by dynamic programming,
rather than approximated by a rule-driven walk through the piece. Second, the numbers inside the model
can be estimated from **unlabelled** music — ordinary MIDI files with no harmonic annotation — by the
forward-backward (Baum-Welch) algorithm.

The paper's distinguishing claim against its neighbours is that key and chord are recognised
**simultaneously**, in one state, rather than key first and chord after.

The paper ends by outlining, but not building, a richer model in which the music is treated as several
independent voices given the harmony.

**Nothing in this section is a finding.** It is the orientation a reader needs before §3.

---

## §3 — The model, transcribed at the pages

### 3.1 The input partition (page 2)

Analysis runs on a **fixed musical period `q`** — the paper's illustration is *"a measure (q = 1) or
half measure (q = 1/2)"*, introduced with *"say"*, so the two values are examples rather than the
permitted set. The pitches of the piece are partitioned into a sequence of subsets `y_1, …, y_N`, where
`y_n` is *"the collection of pitches whose onset time, in measures, lies in the interval
[nq, (n+1)q)"*. The collection is written `y_n = {y_n^1, …, y_n^K}`, **with the number of pitches `K`
depending on `n`** (page 2).

Analysis is **on pitch class only**: the pitches are elements of `{0, 1, …, 11}`, the paper giving
enharmonic pairs at each end of the range (page 2). *(The accidental glyphs in that enumeration are
small in the page image and are not transcribed here; the load-bearing fact is the mod-12 pitch-class
alphabet, which the surrounding sentences state twice.)* The paper's own stated reason for not
modelling spelling: *"While the extension of our approach to include enharmonic spellings is clearly
possible, since MIDI does not use enharmonic spellings, we do not model them."* (page 2).

### 3.2 The label alphabet (page 2)

> `L = T × M × C = {0,…,11} × {major, minor} × {I, II, …, VII}`

*"where T, M, C stand for tonic, mode, and chord"* (page 2). So **|L| = 12 × 2 × 7 = 168**. *(The
product is this side's arithmetic over the paper's own three factors; the paper states the squared
figure at page 3 — see 3.5 — from which 168 follows.)*

**The paper's own worked example of a label**, printed immediately after the definition:

> *"For instance, (t, m, c) = (3, major, II) would represent the triad in the key of 2 = d major built
> on the II = 2nd scale degree which contains pitches e,g,b."*

**★ That sentence may not agree with itself, and the question is recorded at §7.1** — the leading
numeral of the triple, as it renders in the page image, is not the same number as the key index the
same sentence then names. **★ CORRECTED AT THE POST-LANDING CHECK OF 2026-09-13. FORMER WORDING,
PRESERVED (#12): "That sentence does not agree with itself, and the disagreement is recorded at
§7.1".** That stated as established what §7.1 states as conditional on one small glyph — §7.1 says in
terms that under one reading of it there is no defect at all — so the two sections contradicted each
other.

The paper states, in the same paragraph, these deliberate omissions (page 2):

- *"We will ignore the usual convention of using lower and upper case roman numerals for minor and
  major triads."*
- *"While it is possible to use a broader range of possible chords (in fact, we do in our experiments)
  nothing significant is lost by limiting ourselves to the seven basic triads in this discussion."*
- *"Similarly, it would be possible to include more modes than the basic major and harmonic minor that
  we treat here."*
- *"We do not currently model chord inversion in this work."*

### 3.3 Secondary function is expressed as modulation (page 2)

The paper works the point at an example: in *"a clearly established c major context"*, the progression
**c major, d major, g major**, where d acts as *"the 'dominant' of the dominant chord g major — a
so-called secondary dominant, often notated (V/V)"*. Its vocabulary carries no secondary chords, and
its answer is to spend a key change instead:

> *"the above example can be represented as (c=0, major, I), (g=7, major, V), (g=7, major, I)."*

And its claim for that choice: *"Clearly our representation allows for a rich variety of secondary
functionality while avoiding murky distinctions between secondary functions and actual modulation."*
(page 2).

### 3.4 The two hidden-Markov assumptions (page 2)

**The chain over labels:**

> `p(x_{n+1} | x_1, …, x_n) = p(x_{n+1} | x_n)`

described as *"a homogeneous Markov chain"* (page 2).

**The emission:**

> `p(y_n | x_1, …, x_n, y_1, … y_{n-1}) = p(y_n | x_n)`

glossed by the paper as *"every time we visit a state (harmonic label) the data are obtained by
'spitting out' a collection of pitches from a distribution characteristic of the state"* (page 2).

The paper's defence of the Markov assumption is stated in musical terms rather than by a measurement
(page 2). Keys, it says, *"tend to remain constant for relatively long periods of time"*, so *"the key
at each time point is, with high probability, the same as it was on the previous time period."*
*(★ CORRECTED AT THE POST-LANDING CHECK. FORMER WORDING, PRESERVED (#12): "Keys remain constant over
long stretches, so …" — a paraphrase that dropped the paper's own hedge and stated as flat fact what
the paper states as a tendency.)* Music under a constant key is *"often
composed of familiar chord progressions such as the stabilizing **I V I V I** or the ubiquitous Rock
and Roll progression **I IV I V IV I**"*. And chord behaviour shows transition tendencies — *"V tends
to go to I, ii often goes to V, etc."* The paper then observes that chord-transition and
key-modulation tendencies mirror one another, *"as the chords I and V frequently appear side by side,
modulations to neighboring keys in the circle of fifths are also common"*, adding the parenthesis
*"(While treated separately in our model, these phenomena are really not completely distinct)"*.

The paper states two candid limits on its own assumptions at this point: the Markov assumption is *"of
course only an approximation"*, and *"While chord progressions often have longer memory, as in the
Rock example"* — the second of the two progressions quoted above — the model does not carry that
memory.

### 3.5 The parameter problem, stated in figures (page 3, §2.1 *Hand-Tying of States*)

The section that carries the simplifying assumptions is headed **§2.1 Hand-Tying of States**, opening
at the foot of page 2 and running through page 3.

> *"at present the transition probabilities consist of (12 × 2 × 7)² = 28224 parameters — more than we
> can expect to train reliably with a modest data set; a similar problem exists with the output
> probabilities p(y_n|x_n)."*

*(28224 is the paper's own printed figure. 168² = 28224, so the printed value is internally consistent
with the alphabet of 3.2 — this side's arithmetic, stated as such.)*

The paper's stance on the remedy is stated in the same paragraph and is worth carrying verbatim,
because it is a methodological claim and not only a modelling one: *"We introduce some hand-crafted
simplifying assumptions that lead towards feasible training. As in the preceding, our research bias is
for making our assumptions explicit, even when they seem questionable."*

### 3.6 The transition factorization (page 3, Eqns. 1 and 2)

With `x = (t, m, c)` a tonic-mode-chord triple:

> `p(x'|x) = p(t', m', c' | t, m, c)`                                      **(1)**
> `        = p(t', m' | t, m) · p(c' | t', m', t, m, c)`
> `        = p(t' − t, m' | m) · { p(c'|c)   t' = t, m' = m ;  p(c')  otherwise }`   **(2)**
> `   ≝     q_t(t' − t, m' | m) · { q_c²(c'|c)  t' = t, m' = m ;  q_c¹(c')  otherwise }`

**The assumptions are named at the paper, each with the paper's own defence. Named rather than
counted:**

- **The key transition ignores the current chord.** *"In Eqn. 1 we have assumed that the probability
  of the new key, t', m', given the current state, t, m, c, p(t', m'|t, m, c), does not in fact depend
  on the current chord c."* *(Which equation this assumption actually sits in is taken up at §7.5.)*
- **Key-modulation translation invariance.** *"The left factor of Eqn. 2 represents a translation
  invariance assumption about key modulations — the probability of modulating by some particular
  interval does not depend on the current tonic."* Defended by ear rather than by measurement: *"As
  one who does not have perfect pitch and hears only relative pitch movement, this and other pitch
  translation invariance assumptions seem unassailable."* With the arithmetic note *"(The difference
  t' − t is taken modulo 12.)"*
- **Chord-transition translation invariance, within a constant key.** *"The first (top) is that when
  the key is constant the chord transitions do not depend on the current key."* The paper calls this
  *"undeniable as long as we restrict our attention to either major or minor mode"*, then immediately
  widens it and flags the widening: *"The assumption goes a bit further and asserts that, for example,
  the probability of moving from I to V is the same in both major and minor modes."*
- **The chord after a key change is drawn without regard to either key.** *"The second (bottom)
  assumption is that when we do move from one key to another we choose the new chord and random
  without regard for the new or old keys."* *(This side reads the printed word as "and" at every
  request of page 3 it made — four of them, named at §7.1's correction; **the first extract reads it as
  "at"**, and the disagreement is recorded at §9.4. The sense is the same under either reading.)* On
  which the paper
  says plainly *"We doubt this particular assumption would hold up under empirical investigation but
  also doubt that a more nuanced modeling of this case will achieve significant improvements in
  recognition accuracy."*

**The parameter count after the reduction, as printed (page 3):**

> *"These assumptions reduce the number of parameters necessary to represent p(x'|x) to those involved
> in the distributions q_t, q_c¹, q_c²: 12 × 2 × 2 + 7 × 7 + 7 = 104 parameters, further reduced by
> the constraint that each probability distribution must sum to 1."*

*(48 + 49 + 7 = 104, so the printed sum is arithmetically correct — this side's check, stated as
such.)*

### 3.7 The output model, and the rhythm covariate (page 3, Eqns. 3 and 4)

The paper's stated motive (page 3): *"while expressive dissonances are a mainstay of musical surprise,
surprise is almost by definition an exception to the norm; in particular, we anticipate that chord
tones are more likely to occur on rhythmically strong beats than weak ones."* Its method is to
**decline to quantify that directly** — *"Rather than trying to quantify such a notion directly, we
simply allow the output distributions to depend on the known measure positions in a manner we will
learn from data. Thus we treat the measure positions as covariates in our model and condition on them
as well as the chord label."*

Each pitch `y^k` carries a measure-position label `r^k`. The paper's own worked assignment, **for music
in 4/4** (page 3): `r^k` is *"0 if y^k occupies the start of a measure, 1 if y^k begins on the 2nd half
note of the measure, 2, if y^k lies on the 2nd or 4th quarter note positions, etc. with a final
category 3 for 'other.'"*

> `p(y|x,r) = p(y¹,…,y^K | x, r¹,…,r^K)`
> `         = ∏_{k=1}^{K} p(y^k | x, r^k)`                                    **(3)**
> `         = ∏_{k=1}^{K} p(d(y^k,x) | r^k) / V(d(y^k,x))`                    **(4)**
> `    ≝      ∏_{k=1}^{K} q_o(d(y^k,x) | r^k) / V(d(y^k,x))`

**The five pitch categories**, printed as a braced case list (page 3), the subject symbol in each line
rendering in the page image as a Greek gamma where the surrounding definition `d(y^k, x)` requires the
observed pitch `y^k` (see §7.6):

| `d` | condition, as printed |
|---|---|
| 1 | root of chord `t, m, c` |
| 2 | third of chord `t, m, c` |
| 3 | fifth of chord `t, m, c` |
| 4 | in scale `t, m` **but not triad** `t, m, c` |
| 5 | otherwise |

*"and V(d) is the number of chromatic pitches falling into the dth category: V(1) = V(2) = V(3) = 1 ;
V(4) = 4 ; V(5) = 5."* *(1 + 1 + 1 + 4 + 5 = 12, so the five categories partition the chromatic octave
— this side's arithmetic.)*

**What the two equations assume, in the paper's own words:**

- Eqn. 3: *"given the harmonic label, x, the pitches y¹,…,y^K are random samples from their respective
  rhythm-conditional (r^k) distributions."* The paper names this as **its own worst assumption** at
  this point: *"While we expect that this assumption will seem familiar to many, we believe it is
  among the most problematic: the order in which pitches appear clearly affects one's harmonic
  perception."* It points forward to §5 for the variation that drops it, and defends keeping it here
  only on cost: *"The assumption does, however, lead to a significant reduction in model complexity."*
- Eqn. 4: *"the probabilities of observing the categories chord root, chord third, chord fifth,
  non-triad scale tone, or non-scale tone are fixed and do not depend on the harmonic label. There are
  several chromatic pitches in the latter two categories and our assumption is that within a category
  the pitches will be equally likely."*

**Two worked consequences follow that sentence on the same page**, and the first of them is where §7.2
is recorded:

1. *"for notes at a given measure position, the probability of observing d in the IV chord of c major
   is the same as that of b♮ in the I chord of d minor."* **The accidental on the second pitch decides
   whether the example is right, and it is read with both readings and no verdict at §7.2.**
2. *"Additionally the pitches c♯, d♯, f♯, a♭, b♭ all have the same probability in the key of c major,
   regardless of the particular chord, however this probability depends on the measure position."*
   *(Those five spellings name the five pitch classes outside the c major scale, so the example agrees
   with V(5) = 5 — this side's check against the paper's own category table.)*

**The output parameter count, as printed (page 3):** *"q_o(d|r) is the probability of observing a pitch
of category d ∈ {1,…,5} for a note beginning at rhythmic position r ∈ {0,…,5}. These assumptions reduce
the number of parameters in the representation of p(y|x,r) to 5 × 6 = 30."*

**★ A tension between that sentence and the rhythm-category scheme given earlier on the same page is
recorded at §7.3.**

### 3.8 Training (pages 3–4)

**What is trainable and why (page 3, §3):** *"the transition probabilities parameters, q_t, q_c¹, q_c²,
and the output distributions, q_o, can be trained from unlabeled examples. Since our model is based on
rhythm as well as pitch, essentially any collection of MIDI files that explicitly represent both
rhythm and pitch can be used for training. This is the case for most MIDI files that do not come from
actual performances."*

**The labelled case, given as the easy contrast (page 4):** a chord-transition probability *"could be
estimated as the ratio of the number of times we observed the chords c, c' (with common key) to the
total number of times we observed c (with the next chord in the same key)"* — **the symbol the paper
prints for that probability is taken up at §7.7** — and `q_o(d|r)` *"as the ratio of the … times we
observed a note of rhythm category r and pitch category d divided by the number of times we observed
rhythm category r"*, with the paper's own parenthesis *"(Note that the harmonic label must be known to
compute d = d(y^k, x).)"*

**The unlabelled case, which is the actual method (page 4):** *"the forward-backward, or Baum-Welch
algorithm, is to iteratively estimate the hidden labels and reestimate the model parameters. It is
well known that this is an example of the more general EM algorithm for maximum likelihood estimation
of parameters in a mixture model"*, citing Rabiner (1993).

**The recursions, as printed (page 4).** Forward:

> `α_1(x_1) = p(x_1) p(y_1|x_1)`
> `α_{n+1}(x_{n+1}) = Σ_{x_n ∈ L} α(x_n) p(x_{n+1}|x_n) p(y_{n+1}|x_{n+1})`

Backward:

> `β_N(x_N) = 1`
> `β_{n-1}(x_{n-1}) = Σ_{x_n ∈ L} β_n(x_n) p(x_n|x_{n-1}) p(y_n|x_n)`

With the identifications *"α_n(x_n) = p(x_n, y_1,…,y_n) where the latter is viewed as a function of
x_n with the y's held fixed; similarly, β_n(x_n) = p(y_{n+1},…,y_N|x_n)"*, and the posterior

> `p(x_n|y_1,…,y_N) = α_n(x_n)β_n(x_n) / Σ_{x'_n} α_n(x'_n)β_n(x'_n)`

**The soft-count idea, in the paper's own gloss (page 4):** *"The probabilities p(x_n|y_1,…,y_N)
function as surrogates for the true class labels. For instance, in estimating the output distributions
if p(x_n|y_1,…,y_N) = 1/2 for some particular state x_n, then y_n counts as 1/2 a sample from the
output distribution for x_n."* The reestimation formulas for `q_o` and for `q_c²` are printed in full
on page 4, the `q_c²` sum being restricted to adjacent periods whose key and mode are equal —
`(t_n, m_n) = (t_{n+1}, m_{n+1})` — which is the estimator matching the top branch of Eqn. 2. The page
closes *"We can also estimate q_c¹ and q_t in an analogous manner."*

### 3.9 Decoding — exact, not approximate (page 4, §4)

> `x̂ = arg max_x p(x|y) = arg max_x p(x,y)`

constructed by dynamic programming from `P_1(x_1) = p(x_1,y_1) = p(x_1)p(y_1|x_1)` and

> `P_n(x_n) ≝ max_{x_1,…,x_{n-1}} p(x_1,…,x_n, y_1,…,y_n) = max_{x_{n-1}} P_{n-1}(x_{n-1}) p(x_n|x_{n-1}) p(y_n|x_n)`

with the back-pointer `Q_n(x_n) ≝ arg max_{x_{n-1}} P_{n-1}(x_{n-1}) p(x_n|x_{n-1}) p(y_n|x_n)`,
recovered by `x̂_n = Q_{n+1}(x̂_{n+1})` from `x̂_N = arg max_{x_N} P_N(x_N)`.

**★ The sentence that decides the computational character of the method**, printed at the end of that
paragraph (page 4):

> *"While in many applications the dynamic programming recursion is approximated with a 'beam search,'
> the size of our state space allows for full-fledged dynamic programming."*

### 3.10 The outlined extension (page 5, §5)

The paper names the conditional independence of pitches as *"the most troubling modeling assumption we
make"* — *"in essence, the collection of pitches associated with a chord is a random sample from some
distribution. This assumption disregards the way music is usually composed of independent parts or
voices that obey an internal logic such as a preference for scales and arpeggios."* Its stated reason
for having started without voices: *"Given the often unvoiced nature of MIDI data and our current
focus on piano music, we have begun with a simple model that does not require voicing information."*

The proposed replacement: *"a model that regards the data as a collection of voices where the evolution
of each voice is conditionally independent of the others, given the harmonic state."* **★ CORRECTED AT
THE CROSS-CHECK. FORMER WORDING, PRESERVED (#12): "…as a collection of voices where evolution of each
voice is conditionally independent…" — this side had dropped the article. The first extract had it
right; resolved at page 5. Nothing rests on it.** Formally (page 5),
`y_1,…,y_N` becomes *"a sequence of pitch classes … corresponding to a single voice"*, `X_1,…,X_N`
remains *"the sequence of (key,chord) variables, assumed to be a Markov chain as before"*, and
*"unlike before we now assume that the distribution of Y_n depends on X_n and Y_{n−1}, rather than
just X_n."*

**★ The extension re-uses the index `n` of §2 without saying how a voice's own note positions line up
with the period grid that `n` counted there.** Recorded at §7.8.

**The figure.** The paper says *"Figure 5 shows a graphical representation of such a model containing
two conditionally (on X) independent voices."* The graph at the top of page 5 carries three row labels
at its left margin — **Label**, **Voice 1**, **Voice 2** — with edges running horizontally along each
row and vertically from the Label row down to voice nodes, and **with the Voice 2 nodes not aligned
with the Voice 1 nodes**, which is how two voices whose notes fall at different times would be drawn.
**The graph carries no printed caption and no printed number** — see §7.9.

**On getting voices in the first place (page 5):** *"Automatically partitioning MIDI data into voices
is, no doubt, a challenging problem if one requires the voicing to be identical to the true voicing,
if one exists, or the ground truth supplied by a musician. But it is rather simple to create an
algorithm that performs reasonably. We use a simple dynamic programming algorithm maximizing a
function measuring the plausibility of a voice partition."* It names Kilian & Hoos (2002) as an
alternative, and states its own input assumption: *"We assume here that we begin with voiced data,
either from an official or algorithmic source. In particular, we begin with a collection of monophonic
overlapping voices with no assumption about the number of voices that overlap at any particular time
or the range of pitches associated with a particular voice."*

**What the extension is claimed to buy, and what is claimed about its cost (page 5):** *"Such a model,
suitably trained, would understand a voice's preference for scales within the key, arpeggios within
the (key,chord) pair, and tendencies regarding the resolution of non-chord tones. These preferences
should assist in distinguishing between various chord hypotheses, given data."* And: *"While this
model is not an HMM, it has a linear structure amenable to an analogous training algorithm as well as
the identification of the most likely state sequence. Thus the model is every bit as computationally
tractable as the HMM."*

**This extension is OUTLINED AND NOT BUILT.** No implementation, no experiment and no measurement of
it is met anywhere in the five pages as read. The abstract says so in its own words: *"An extension to
a more complex probabilistic graphical model is **outlined** in which music is modeled as a collection
of voices that evolve independently given the harmonic progression."* (page 1; the emphasis is this
side's.)

---

## §4 — Claims, labeled

The commission's §4 requires every claim to carry FACT (stated or measured in the paper, with its
location), THEORY (established published theory), or CONJECTURE. **Nothing unlabeled below carries
load later.**

### FACT — what the paper states of itself, with its location

- **F1 (page 2).** The state is a single triple `(tonic, mode, chord)` and key and chord are decided
  **in one state, simultaneously**, not in stages. The paper claims this as a difference from every
  neighbour it knows: *"Another significant difference between our approach and all others we know is
  our simultaneous recognition of chord and key."*
- **F2 (page 4).** The decode finds the **exact global maximum** of `p(x, y)` by dynamic programming
  over the full state space, the paper stating that its state space does not require the beam-search
  approximation many applications use — see 3.9's quoted sentence.
- **F3 (page 2, page 3 §3).** The model is trainable from **unlabelled** symbolic data by
  forward-backward; no harmonic annotation is required for training.
- **F4 (page 4, §4).** In the experiments actually run, **only `q_o` and `q_c²` were learned.** *"The
  remaining parameters of the transition probabilities, q_t and q_c¹, seem to require larger training
  sets to be reliably estimated; we have set these parameters by hand in the experiments here, but
  plan on automatically learning them in the future."*
- **F5 (page 5).** **The paper states in terms that it offers no measure of success**, and this side
  met no accuracy figure, error rate or comparison anywhere in the five pages as read. Verbatim: *"At
  this point we do not offer any objective measure of success, such as 'error rate,' or comparison of
  our results. This is due, in part, to the difficulty in defining and obtaining 'correct' harmonic
  analyses. However, we also believe that rather straightforward continued efforts may lead to
  significant improvements and that evaluation will be more appropriate at a later stage."*
- **F6 (page 2).** **Chord inversion is not modelled** — *"We do not currently model chord inversion
  in this work."*
- **F7 (page 2).** **Enharmonic spelling is not modelled**, and the stated reason is the input format:
  *"since MIDI does not use enharmonic spellings, we do not model them."*
- **F8 (page 2).** **Secondary function is spelled as a key change**, not as a secondary-chord label —
  3.3 above, with the paper's own three-label worked example.
- **F9 (page 3).** The parameter reduction is from **28224** unreduced transition parameters to **104**
  in `q_t, q_c¹, q_c²`, and the output representation to **30** in `q_o`. All three figures are
  printed.
- **F10 (page 5).** The reported run used **the dominant 7th chord added to the seven basic triads**,
  and the paper says that **fully diminished 7th chords and chords in minor mode built on the flat
  seventh scale degree *"are needed in these experiments"***, while *"more exotic additions such as
  augmented sixth chords, and Neapolitan chords are possible."* Harmonic transitions were restricted
  to **2-beat boundaries** in the Haydn and Chopin examples and relaxed to **1-beat boundaries** in
  the Debussy example, which the paper says *"results in a somewhat overanalyzed labeling."*
  **★ THE CHORD-EXTENSIONS HALF OF THIS ENTRY WAS ADDED AT THE CROSS-CHECK**, where this side's
  reading of that sentence was found wrong — see §9.2.
- **F11 (page 5).** The paper reports where its method does **worse**: *"(The less successful results
  seem to mostly be compositions with very sparse textures)."*
- **F12 (pages 1–2).** The method is **not rule-based** — *"Our approach, like that of Pardo (2002) is
  decidedly not rule-based"* — and the paper states two reasons it rejects rule-based schemes: they
  *"fail to articulate any measure of goodness of the possible 'answers' and hence do not formulate
  the problem clearly"*, and they *"balance each decision or transformation precariously on the
  shoulders of previous decisions and hence irrevocably propagate errors forward"* (page 2).

### THEORY — established published machinery the paper adopts rather than invents

- **T1.** The hidden Markov model, its forward-backward / Baum-Welch estimation, and the reading of
  Baum-Welch as an instance of EM — the paper cites Rabiner (1993) for this and presents the
  recursions as standard (*"A standard argument shows…"*, *"It is well known that…"*, page 4).
- **T2.** Viterbi-style dynamic programming for the most likely state sequence — presented as
  *"well-known"* (page 4).
- **T3.** Key identification by matching a pitch histogram against key templates, credited to
  Krumhansl (1990); the paper states its own key-appropriateness computation is *"similar to that of
  Krumhansl (1990)"* (page 1).
- **T4.** Two positions taken over from Temperley & Sleator (1999) and named as shared rather than new
  (page 1): that **rhythmic content is useful in harmonic analysis**, and that **analyses fluctuating
  rapidly between keys are implausible and should be discouraged or penalized**.

### CONJECTURE — what the paper asserts without measuring it

- **C1 (page 2).** *"The hope here is that the more structured sequence of chord functions (e.g.
  tonic, dominant etc.) will help guide the analysis when the choice of chord … is ambiguous."*
  **This is the motive for joint decoding and no measurement of it is met in the five pages as read.**
  The word in the paper is *hope*.
- **C2 (page 3).** That the new chord after a key change is chosen without regard to either key — the
  paper itself grades this one: *"We doubt this particular assumption would hold up under empirical
  investigation but also doubt that a more nuanced modeling of this case will achieve significant
  improvements in recognition accuracy."* **Both halves are unmeasured.**
- **C3 (page 3).** That the probability of moving from I to V is the same in major and minor. Stated
  as a consequence the assumption *"goes a bit further"* to reach; no evidence offered.
- **C4 (page 5).** That the voice extension *"should assist in distinguishing between various chord
  hypotheses"*. Unbuilt, so unmeasured.
- **C5 (page 5).** That the voice extension is *"every bit as computationally tractable as the HMM"*.
  An analytic claim about a model that was not implemented; no timing is given for it.
- **C6 (page 5).** That the three published examples *"are comparable to the majority of cases we have
  examined in which our program produces a plausible interpretation"*. **The set of cases examined is
  not enumerated and its size is not given, and no definition of "plausible interpretation" is met in
  the five pages as read** — and F5 says in terms that no objective measure is offered.
- **C7 (page 3).** That the translation-invariance assumptions *"seem unassailable"*. The stated
  ground is the authors' own hearing, not a measurement: *"As one who does not have perfect pitch and
  hears only relative pitch movement…"*

---

## §5 — Coupling facts (mandatory under the commission's §4)

### 5.1 What the method ASSUMES about its upstream

- **Symbolic input carrying both pitch and rhythm explicitly.** The paper's own statement of what
  qualifies: *"essentially any collection of MIDI files that explicitly represent both rhythm and
  pitch can be used for training. This is the case for most MIDI files that do not come from actual
  performances"* (page 3). **The paper does not say performance MIDI is barred**; what its sentence
  says is that performance MIDI is, as a rule, not among the files that meet the stated requirement.
- **A metrical grid.** Two separate things depend on it: the fixed period `q` that defines the
  partition into `y_1,…,y_N` (page 2), and the measure-position covariate `r^k` attached to every
  pitch (page 3). *This side's reading of the specification, not a statement of the paper's: the
  output model as written cannot be evaluated without `r`, because `q_o(d|r)` takes `r` as an
  argument.*
- **A period length chosen in advance.** `q` is a parameter of the analysis, not something the method
  discovers (page 2). **In the reported runs the period reached one beat** — the Debussy example
  allowed transitions on 1-beat boundaries (page 5), which in 4/4 is a quarter of a measure, below
  both of the two values §2 offered as illustrations. *This side's reading: the label boundaries the
  method can place are the period boundaries, so a region arises from adjacent periods sharing a label
  rather than from the method placing a boundary anywhere else. The paper does not state this; it
  follows from the partition of 3.1.*
- **Onset times.** The partition is defined on onset time — *"the collection of pitches whose onset
  time … lies in the interval [nq, (n+1)q)"* (page 2). **No clause met in the five pages as read
  carries a note's duration, or the fact that it is still sounding, into any later period**: a pitch
  enters exactly the one subset its onset falls in.
- **A time signature the rhythm categories were designed for.** The worked category assignment is for
  4/4 (page 3), and the paper says its three published examples *"are all in 4/4 time to facilitate a
  uniform definition of the rhythm variables"* (page 5). **No category scheme for any other metre is
  met in the five pages as read.**
- **For the §5 extension only: a voice partition.** *"We assume here that we begin with voiced data,
  either from an official or algorithmic source"* (page 5).

### 5.2 What the method HANDS downstream

- **One label per period**: `(t, m, c)` with `t ∈ {0,…,11}`, `m ∈ {major, minor}`, `c ∈ {I,…,VII}`
  (page 2) — i.e. **key, mode and chord function together, on one axis of time, at the period grid.**
- **Contiguous labelled regions.** The abstract's own description of the output: *"partitions a piece
  of music into contiguous regions and labels each with the key, mode, and functional chord"* (page 1).
- **A single committed sequence** `x̂`, the global argmax (page 4). **No ranked alternatives and no
  per-period confidence are published anywhere in the five pages as read.** The posterior
  `p(x_n | y_1,…,y_N)` exists inside the machinery and is written down on page 4 — but it is used
  there **as a training surrogate for the class label**, and no sentence met in the paper proposes it
  as an output.
- **No inversion, no bass information** (F6). **No chord quality beyond the degree in the exposition**;
  in the experiments, the dominant 7th as one addition (F10).
- **No secondary-function labels.** A `V/V` reaches the downstream reader as a modulation to the
  dominant key (F8). *This side's reading of what that costs a consumer: in a passage using secondary
  function, a consumer counting key changes in this output will count changes the Roman-numeral
  reading would have spelled inside one key. The paper does not treat this as a cost; it presents it
  at 3.3 as an advantage.*
- **A demonstration format, not a data format.** What the paper actually emitted was *"a MIDI file of
  a mechanical piano performance with the series of chords produced by our algorithm superimposed as
  sustained harmonica chords"*, plus *"text messages … giving the harmonic label as a (roman numeral,
  tonic, mode) triple, aligned to highlight key changes"*, *"written as chord changes occur,
  essentially annotating the MIDI performance in real-time"* (pages 4–5). **The ordering of that
  printed triple is taken up at §7.6.**

### 5.3 The method's own STATED SCOPE and limits

Collected from the paper's own sentences rather than inferred:

- **Pitch and rhythm only.** *"At the outset we acknowledge that there are likely no two elements of
  music that do not interact in some musical situation; thus limiting our treatment to these two
  elements undoubtedly loses some relevant information"* (page 2).
- **Seven basic triads in the exposition**, major and harmonic minor only, no inversion (page 2). **In
  the reported experiments the vocabulary is larger**: the dominant 7th added, and fully diminished
  7ths and flat-seventh minor-mode chords *"needed in these experiments"* (page 5, F10). *(This line's
  second sentence was added at the cross-check — §9.2.)*
- **No spelling** (page 2).
- **No evaluation** (F5).
- **Trained on very little.** *"around 5 or so short movements"* (page 4, §4).
- **Two of the four parameter groups hand-set** (F4).
- **Piano music.** *"our current focus on piano music"* (page 5).
- **Worst on sparse textures** (F11).
- **The pitch conditional-independence assumption is named by the authors themselves as their most
  troubling one** (page 3 and page 5).

---

## §6 — Measured results

**The paper states that it offers none, and that statement is the finding.**

The commission's §4 asks for *"Measured results, with corpus, metric and value as the paper states
them."* **This paper states no metric and no value**, and none is met anywhere in the five pages as
read. What it puts where a results section would go is F5's sentence — *"At this point we do not offer
any objective measure of success, such as 'error rate,' or comparison of our results"* (page 5).

**What the paper does give in that place**, recorded exactly and with no figure promoted out of it:

| What the paper gives | Where | As printed |
|---|---|---|
| Training material | page 4 | *"around 5 or so short movements"* |
| Training time | page 4 | *"several minutes of computing on a 1 GHz Linux box"* |
| Training iterations | page 4 | *"around 5 iterations of the training algorithm"* |
| What was learned | page 4 | `q_o` and `q_c²` only; `q_t` and `q_c¹` hand-set |
| Demonstration pieces | pages 4–5 | first movement of Haydn Piano Sonata 6; Chopin Raindrop Prelude in D flat, Op. 28, no. 15; Debussy Prelude from *Suite Bergamasque* |
| Where the demonstrations live | page 4 | `http://fafner.math.umass.edu/ismir03` |
| Transition granularity | page 5 | 2-beat boundaries (Haydn, Chopin); 1 beat (Debussy) |
| Chord set actually used | page 5 | seven basic triads **+ dominant 7th**, with fully diminished 7ths and flat-seventh minor-mode chords *"needed in these experiments"* |
| Self-assessment of the examples | page 5 | *"representative of the more successful applications"* |
| Self-assessment of the failures | page 5 | *"compositions with very sparse textures"* |

**Three qualifications on that table, so nothing in it is read as more than it is.**

1. **"around 5 or so short movements" is the whole of what the paper says about its training corpus.**
   No piece list, no note count and no composer for the training set is met in the five pages as read,
   and the paper does not say whether the three demonstration pieces were among the training material
   or held out from it.
2. **The three demonstration pieces are an availability claim, not a result.** The paper says the
   examples are *available on the web*; it states no verdict on them beyond *"plausible
   interpretation"*, which it does not define.
3. **The web address is a 2003 URL and was NOT visited by this reading.** No web access of any kind
   was made in this sitting. Whether anything is still there is unchecked and unasserted.

---

## §7 — Defects and tensions met in the pages as read

**Named rather than counted**, and each read at its own line. **Each is a statement about what is
printed in these five pages; none is a statement about the record, about our own design, or about the
2004 journal article.** *(No claim is made that this is everything a further reader would find.)*

### 7.1 The label alphabet's worked example disagrees with itself (page 2)

Printed immediately after the definition of `L`:

> *"For instance, (t, m, c) = (3, major, II) would represent the triad in the key of 2 = d major built
> on the II = 2nd scale degree which contains pitches e,g,b."*

**Two of the sentence's three halves agree with each other and with the paper's own numbering.** The
paper numbers pitch classes from c = 0 (page 2), so *2 = d* is right; and the triad on the second
degree of d major is **e, g, b**, which is what the sentence names. **The leading numeral of the
triple is the half that does not fit**: with `t` the tonic index, `t = 2` is what *d major* requires.

**Both readings of that glyph are recorded and no verdict is taken on it.** The numeral is small in
the page image; page 2 was requested four times in this sitting — the whole read, a two-page request
and a single-page request at the read-back, and a two-page request at the cross-check — and the
numeral read as **3** at every one. *(★ CORRECTED AT THE POST-LANDING CHECK. FORMER WORDING, PRESERVED
(#12): "it was read twice, in a two-page request and again in a single-page request, and read as 3
both times." That counted the read-back's two requests only and omitted the whole read and the
cross-check.)* **If it is 3, the example names a key its own next clause contradicts. If it is
2, there is no defect here at all.** What is established either way is that **the key index and the
named pitches are mutually consistent**, so nothing about the paper's numbering scheme is in doubt.

### 7.2 An accidental decides whether a worked example is right (page 3)

> *"for notes at a given measure position, the probability of observing d in the IV chord of c major is
> the same as that of b♮ in the I chord of d minor."*

By the paper's own five categories (3.7): **d in the IV chord of c major is category 4** — IV of c
major is the f major triad, d is not one of its tones, and d is in the c major scale. For the example
to hold, the second pitch must also be category 4 in its own context, i.e. **in the d harmonic minor
scale but not in the d minor triad**.

- **Read as b♭:** b♭ is in d harmonic minor and is not a tone of the d minor triad → **category 4, and
  the example is correct.**
- **Read as b♮:** b♮ is not in d harmonic minor (which the paper names as its minor mode, page 2) →
  **category 5, and the example is wrong by the paper's own table.**

**This side reads the glyph as a natural sign and records both readings with no verdict**, because the
accidental is small in the page image and the same paragraph prints two unambiguous flats (*a♭, b♭*)
two lines below. **What is established is that the example is right under one reading and wrong under
the other, and that nothing else in the paper turns on which.**

### 7.3 An internal tension in the rhythm-category alphabet (page 3)

Page 3 introduces the measure-position categories for 4/4 as *"0 if y^k occupies the start of a
measure, 1 if y^k begins on the 2nd half note of the measure, 2, if y^k lies on the 2nd or 4th quarter
note positions, etc. with a final category 3 for 'other.'"* — a final category **3**, which caps the
alphabet at four values, `r ∈ {0,1,2,3}`.

Later on the same page: *"q_o(d|r) is the probability of observing a pitch of category d ∈ {1,…,5} for
a note beginning at rhythmic position **r ∈ {0,…,5}**"*, pricing the output model at *"5 × 6 = 30"*
parameters.

**Six rhythm categories against a scheme whose last named category is 3.** The arithmetic `5 × 6 = 30`
is consistent with `r ∈ {0,…,5}` and inconsistent with `r ∈ {0,…,3}`, which would give 20. **The paper
does not reconcile the two, and the *"etc."* in the first passage is the only bridge between them.**
This side takes no verdict on which alphabet is intended; **what is established is that the two
passages cannot both be read literally.**

### 7.4 Printed defects of wording, each at its line

**★ THIS SECTION WAS CUT AT THE CROSS-CHECK. ONE OF ITS TWO LOAD-BEARING ITEMS WAS A DEFECT THIS SIDE
MANUFACTURED, AND IT IS WITHDRAWN AT ITS SITE BELOW (#12). See §9.2.**

One that **changes what a sentence says** — *and it is itself disputed between the two extracts*:

- **Page 3**, in the second transition assumption: *"we choose the new chord and random without regard
  for the new or old keys"* — **"and random"** where the sense requires *at random*. **This side reads
  the printed word as "and" at every request of page 3 it made — four of them; the first extract quotes
  the sentence with "at". §9.4 records the disagreement.** The intended reading is the same under
  either, and 3.6 carries it. *(★ "three separate page requests" at the post-landing check; corrected
  to four, the count being over this side's own acts.)*

**★ WITHDRAWN AT THE CROSS-CHECK — A DEFECT THIS SIDE MANUFACTURED. FORMER WORDING, PRESERVED (#12):**
*"**Page 5**, in the chord-set paragraph: 'Some basic extensions, such as fully diminished 7th chords
and chords in minor mode built on the flat seventh scale degree, are **possible** in these experiments;
however, more exotic additions such as augmented sixth chords, and Neapolitan chords are possible.' —
the same predicate, are possible, on both sides of a "however" that announces a contrast. As printed
the sentence contrasts nothing. The intended reading is not recoverable from the page and is not
guessed at here: one of the two clauses does not say what the connective requires, and which one it is
cannot be settled at this paper. A reader therefore cannot tell from these five pages whether
diminished sevenths and flat-seventh minor-mode chords were IN the reported experiments or merely
available in principle."*
**The paper prints "are NEEDED in these experiments", not "are possible".** The first extract read it
correctly and this side did not; **the sentence is coherent as printed and there is no defect here at
all.** Re-read at page 5 at the cross-check. **The consequence is recorded as a fact at F10 and 5.3:
those chord extensions were in the reported experiments.**

Three that **do not change what a sentence says**, recorded because they were met and not because they
carry load:

- **Page 2**: *"this rather obvious virtue of beginning with simplicity **lead** us to start here"* —
  *led* is required.
- **Page 4**, in the labelled-training paragraph: *"the ratio of **the of the** times we observed a
  note of rhythm category r"* — the phrase is doubled.
- **Page 4**, in the forward recursion: the summand is printed **`α(x_n)`**, without the subscript `n`
  that the line above and the identification below both require (`α_n(x_n)`).

### 7.5 WITHDRAWN AT THE CROSS-CHECK — a second defect this side manufactured (page 3)

**FORMER WORDING, PRESERVED (#12):** *"**The equation an assumption is attributed to (page 3).** The
paper writes 'In Eqn. 1 we have assumed that the probability of the new key … does not in fact depend
on the current chord c.' **Eqn. 1 as printed is an identity** — `p(x'|x) = p(t',m',c'|t,m,c)` — and
assumes nothing; the independence appears in the line beneath it, in the factorization carrying
`p(t', m' | t, m)` with no `c`. **A small thing, recorded because the whole factorization is read
through this sentence.**"*

**That rested on a reading of where the equation number sits, and the reading was wrong.** Re-read at
page 3 at the cross-check: **the label `(1)` sits at the right of the SECOND line of the block — the
factorization `p(t', m'|t, m) p(c'|t', m', t, m, c)` — not at the right of the identity above it.**
`(2)` sits at the right of the braced line below. **So Eqn. 1 IS the factorization, the paper's
attribution is exactly right, and there is no defect here at all.**

**The heading is kept rather than removed so that §7.6 onward keep the numbers the rest of this file
cites.** *(The first extract did not report this defect either; it is this side's alone, and the
cross-check is what found it — see §9.2.)*

### 7.6 The same object is named three ways (pages 2, 4, 5)

The harmonic state is introduced on page 2 as the triple **`(t, m, c)` = (tonic, mode, chord)**, in
that order, and `L = T × M × C` fixes the order.

- **Page 4** describes the emitted text as giving *"the harmonic label as a **(roman numeral, tonic,
  mode)** triple"* — the same three components, reversed.
- **Page 5** calls the chain *"the sequence of **(key,chord)** variables"* — a pair, where *key*
  presumably absorbs tonic and mode.

Alongside this, the rhythm covariate is written **`r^k`** on page 3, indexed per pitch within a
period, and **`r_n`** on page 5, indexed per period. **None of these is a defect of fact and none
changes a value.** They are recorded because a reader assembling the interface from the paper meets
the same object under three shapes and must decide for themselves that they are one thing.

### 7.7 A distribution named by the wrong symbol (page 4)

The labelled-training paragraph reads *"For instance, **q_t(c'|c)** could be estimated as the ratio of
the number of times we observed the chords c, c' (with common key) to the total number of times we
observed c (with the next chord in the same key)."*

**The quantity being described is the within-key chord transition**, which the paper defines on page 3
as **`q_c²(c'|c)`** and reestimates on this very page under exactly the restriction the sentence
states — the sum over adjacent periods with `(t_n, m_n) = (t_{n+1}, m_{n+1})`. **`q_t` is the key
distribution**, whose arguments everywhere else in the paper are `(t' − t, m' | m)` and never `(c'|c)`;
and the same page closes *"We can also estimate q_c¹ and q_t in an analogous manner"*, treating `q_t`
as a different thing still to be dealt with.

**So the symbol as printed does not name the quantity the sentence describes.** This side reads the
subscript as **t**; **the finding does not depend on that reading**, because the printed symbol carries
no superscript 2 in either reading, and `q_c` without a superscript is not a distribution the paper
defines. **Nothing rests on the value** — the surrounding prose says unambiguously which quantity is
meant.

### 7.8 The outlined extension does not say what its time index counts (page 5)

§2 defines `n` as the index of the period `y_n`, a subset of the piece's pitches under a fixed metrical
period `q`. §5 re-uses `y_1,…,y_N` for *"a sequence of pitch classes … corresponding to a single
voice"*, one pitch class per index, and keeps `X_1,…,X_N` *"as before"*.

**A voice's notes do not in general fall one per metrical period, and two voices do not in general
place their notes at the same times** — which the figure at the top of the page depicts, its two voice
rows being drawn out of alignment with each other. **No sentence met in the five pages as read says how
the voices' own note positions are reconciled with the period grid the harmonic chain runs on, or with
each other.** Recorded as a gap in the outline, not as a defect: **the extension is explicitly an
outline** (3.10), so the paper does not undertake to specify it.

### 7.9 A figure is cited by a number the page does not print (page 5)

Page 5's §5 directs the reader to *"Figure 5"*. The graph at the top of that page — the one described
at 3.10 — is the only figure met anywhere in the five pages as read, and **it carries no printed
caption and no printed number in the page image**. So a reader is sent to *Figure 5* by a document in
which one figure is met and none is numbered. **This side does not know whether the number is a
leftover from a longer manuscript** and does not guess.

### 7.10 The two Computer Music Journal references cannot both be right (page 5, references)

Reference **[2]** gives Pardo (2002), *Computer Music Journal*, **vol. 26, no. 2, 2002**. Reference
**[3]** gives Temperley & Sleator (1999), *Computer Music Journal*, **vol 15, no. 1, 1999**. **The same
journal is cited at a HIGHER volume number for an EARLIER year than the other**: volume 26 for 2002
against volume 15 for 1999, so the volume numbering runs backwards between the paper's own two
citations of it. **At least one of the two volume-year pairs is therefore wrong. Which one is not
establishable at this paper**, and no verdict is taken. *(Derived from the paper's two references
against each other; no outside knowledge of the journal is used.)*

**A second volume-year pair is noted and NOT checked:** reference **[7]** gives Rabiner (1993),
*Proceedings of the IEEE*, **77, 257–286, 1993**. There is no second citation of that journal in the
paper, so nothing about it can be established here. **No verdict.**

**And one cross-check that HELD, recorded because a negative result is a result.** References [1] and
[5] both cite *"the Third International Conference on Music Information Retrieval, Paris, France,
2002"*; reference [6] cites *"the Second … Bloomington, Indiana, 2001"*; and this paper's own page 1
carries the 2003 copyright of its host. **Second in 2001, Third in 2002, this paper in 2003 — the
sequence is consistent and no finding arises from it.**

### 7.11 Two citation styles, one of them never used

The body cites by author and year throughout — *Krumhansl (1990)*, *Pardo (2002)*, *Temperley and
Sleator (1999)*, *Barthelemy & Bonardi (2001)*, *Kilian & Hoos, (2002)*, *Rabiner (1993)*. The
reference list is **numbered [1] to [7]**. **No bracketed citation is met anywhere in the body in the
five pages as read.** The numbering is therefore inert. *(Not a defect of fact; recorded because a
later reader chasing a bracketed number will find none.)*

### 7.12 A small inconsistency with the paper's own stated convention (page 2)

Page 2 says *"We will ignore the usual convention of using lower and upper case roman numerals for
minor and major triads."* Two paragraphs earlier on the same page the prose writes *"V tends to go to
I, **ii** often goes to V, etc."*, using the lower-case form the paper says it ignores. **The
convention is stated of the label alphabet and the lapse is in prose**, so this is a reading hazard
rather than a contradiction; it is recorded so a reader does not take the case of a numeral in this
paper as carrying quality.

### 7.13 An author list checked, and found to agree

Page 1's body gives *"Pickens, Bello, Monti, Crawford, Dovey, Sandler, & Byrd, (2002)"*; reference
**[1]** gives *"Pickens J., Bello J. B., Monti G., Crawford T., Dovey M., Sandler M., & Byrd D."*
**The two agree on the seven surnames and on their order.** Recorded as checked rather than as a
finding.

---

## §8 — The closing section: what the read-back and the sweep found

**This section was written as its own edit, after §1 to §7 were finished and before this file was
landed**, which is the order the hundred-and-sixty-ninth handoff entry's §3 sets (write with the
closing section absent; read back and sweep; then add the closing section recording what those two
acts found). **The first extract was still unopened when this section was written.**

> **★ READ §9 BEFORE RELYING ON THIS SECTION. It is a dated record of what the PRE-LANDING acts found
> and it is left standing as that (#12) — but the cross-check has since overturned two of the things
> it reports as findings.** Specifically: **8.2's line about "the two that change what a sentence
> says" is now stale**, because one of those two was a defect this side manufactured and §7.4 has
> withdrawn it; and **8.6's second question is withdrawn entirely**, at its own site below. Nothing
> else in this section is moved by the cross-check.
>
> **★ AND A THIRD, ADDED AT THE POST-LANDING CHECK OF 2026-09-13: 8.1's account of the read-back's
> reach, and 8.6's "two page-image requests", are both counts of this side's own acts that undercount
> them.** 8.1 is corrected at its own line below; **8.6's first item says "two page-image requests did
> not settle" the two glyphs, where page 2 was requested four times in the sitting and page 3 four
> times** — the conclusion that neither glyph is settled is unchanged, the count is not.

### 8.1 What the read-back was

After §1 to §7 were written, **the paper was re-opened and every transcription in them was compared at
its page.** Four requests were made after the whole read, named rather than counted: **pages 2 and 3
together; page 2 alone; page 3 alone; pages 4 and 5 together.** The two single-page requests were made
to look harder at two small glyphs — the leading numeral of §7.1's triple and the accidental of §7.2 —
and **they returned the same rendering as the two-page requests, so neither glyph is settled and both
are recorded with both readings.**

**NO TRANSCRIBED VALUE MOVED.** Every figure the read-back's four requests reached was re-read at its
page and stands as first written — **the requests covered pages 2 to 5 and NOT page 1**, so the one
figure this extract takes from page 1, the NSF grant number **IIS-0113496** at §1, was not among them.
*(★ CORRECTED AT THE POST-LANDING CHECK. FORMER WORDING, PRESERVED (#12): "Every figure in this
extract was re-read at its page and stands as first written".)* The figures re-read: `(12 × 2 × 7)² = 28224`; `12 × 2 × 2 + 7 × 7 + 7 = 104`; `5 × 6 = 30`;
`V(1) = V(2) = V(3) = 1`, `V(4) = 4`, `V(5) = 5`; `d ∈ {1,…,5}`; `r ∈ {0,…,5}`; the five-category
table; both equation blocks; the three demonstration pieces; the 2-beat and 1-beat granularities; and
the 1 GHz machine.

### 8.2 What the read-back ADDED, because the first writing had missed it

- **The label alphabet's own worked example** (page 2) had been omitted entirely. It is now at 3.2 —
  **and it turned out to carry a disagreement with itself**, which is §7.1. A gap in the first writing
  was therefore also a missed finding.
- **The two chord progressions the Markov defence names** — *I V I V I* and *I IV I V IV I* — had been
  omitted, **while the sentence that refers back to "the Rock example" had been kept**, so a reader of
  the first writing met a referent that was not there. Both are now at 3.4.
- **§2.1's heading, *Hand-Tying of States***, had been omitted; it names the section the simplifying
  assumptions live in. Now at 3.5.
- **The symbol defect on page 4** — a within-key chord-transition probability printed under the key
  distribution's name — had not been caught on the first pass at all. Now §7.7.
- **The same state object named three ways** across pages 2, 4 and 5, and the rhythm covariate indexed
  two ways. Now §7.6.
- **The outlined extension's unstated time index.** Now 3.10 and §7.8.
- **What the page-5 figure actually shows** — three labelled rows and two voice rows drawn out of
  alignment — had been recorded only as an absence of a caption. Now 3.10, with §7.9 keeping the
  caption point.
- **That the reported runs went below both period values §2 illustrates**, the Debussy example
  allowing 1-beat transitions. Now 3.1 and 5.1.
- **The conference-numbering cross-check that HELD** (Second 2001, Third 2002, this paper 2003). Now
  at §7.10, recorded because a negative result is a result.
- **Reference [7]'s volume-year pair**, noted with no verdict because nothing in this paper can check
  it. Now at §7.10.
- **Three wording slips that change nothing** were separated from the two that change what a sentence
  says; the first writing had them in one undifferentiated list. Now §7.4, in two groups.
- **The lower-case numeral against the paper's own stated convention.** Now §7.12.

### 8.3 What the read-back FALSIFIED in this extract's own writing

**Three claims of this side's were struck, not weakened.**

1. **A count this side wrote and then contradicted two lines below it.** §3.6 opened *"Three
   assumptions are named at the paper, each with the paper's own defence"* and its third item then
   began *"The right factor carries two more"* — **three announced, four listed.** The heading is
   struck and the assumptions are now **named rather than counted**. This is the cadence's own rule —
   *put no number on your own acts, name the members* — broken and caught inside one file.
2. **A second count of the same shape.** §3.2 read *"The paper states four deliberate omissions at
   this point"*. Struck; the omissions are now introduced without a count.
3. **An argument resting on a premise this paper cannot supply.** The Computer Music Journal finding
   was first written as *"Eleven volumes separating three years, in the same journal, is not possible
   for an annually-volumed periodical"* — **which assumes a fact about how that journal numbers its
   volumes, and no such fact is on this paper's pages.** Struck and replaced by an argument that uses
   only what the paper prints: the volume number runs **backwards** between the paper's own two
   citations of the same journal, so one of the two pairs is wrong whatever the numbering rate. **The
   finding survives; its ground changed.**

### 8.4 What the sweep for absolutes struck

Every hit was read at its own line. **Named rather than counted, with the former wording quoted so the
change is inspectable.**

Unbounded negatives, each now bounded to the five pages as read:

- **F5** read *"The paper offers no accuracy figure of any kind."* **Struck.** The paper's own sentence
  now carries the negative, with this side's reading bounded to the pages it read.
- **C6** read *"'plausible interpretation' is not defined anywhere in the paper."*
- **5.1** read *"Nothing in the specification carries a note's duration or its continued sounding into
  the next period."*
- **5.1** read *"The paper gives no category scheme for any other metre."*
- **5.2** read *"The paper publishes no ranked alternatives and no per-period confidence."*
- **7.11** read *"No numbered citation appears anywhere in the body."*
- **3.10** read *"No implementation, no experiment and no measurement of it appears anywhere in the
  five pages."*
- **§6** opened *"There are none, and that is the finding."* **Struck**, because it made this side's
  own sweep the ground for a negative the paper states about itself in one sentence.

Claims that said more than the paper does:

- **F2** read that the paper is *"explicitly declining beam search"*. **It declines nothing** — it says
  the size of its state space allows full dynamic programming. Reworded.
- **5.1** read *"Performance MIDI is therefore excluded by the paper's own sentence."* **The paper bars
  nothing.** Reworded to what its sentence says: performance MIDI is, as a rule, not among the files
  that meet the stated requirement.
- **5.2** read *"so a consumer counting key changes will count more of them than a Roman-numeral
  analyst would"* — an unqualified generalization over consumers and over music. **Narrowed** to
  passages that use secondary function, marked as this side's reading, and set beside the paper's own
  opposite framing of the same fact as an advantage.
- **3.4** read *"The paper's own defence of the Markov assumption is musical, not statistical."*
  Reworded to *stated in musical terms rather than by a measurement*.

Two inferences of this side's written as though the paper stated them, **now carrying an explicit
marker that they are this side's reading of the specification**: that the output model cannot be
evaluated without `r`, and that the label boundaries the method can place are the period boundaries.

**And one bound added rather than removed:** §1's sentence about the 2004 journal article now says in
terms that *"the 2004 article treats the same system"* is **this side's reading of two titles**, not
something either document states. §7's preamble gained *"No claim is made that this is everything a
further reader would find."*

### 8.5 What these two acts did NOT do

**They did not open the first extract** — that is the next section's work and it had not begun when
this section was written. **They did not open the progress record, the findings surface,
`FRAMEWORK.md`, `population.md`, the slice derivation, or any other extract.** **No web access of any
kind was made**, so the 2003 URL at 3.10 and §6 is unvisited and unasserted. **No repository sweep was
run for this paper** — not for its authors, not for its title, not for any of its values — **so this
extract asserts nothing about what the record says of it.** **No shell command was run**, in the
container or on the device.

### 8.6 The two questions this extract leaves

**Neither is proposed as an act; both are recorded where the next reader will meet them.**

1. **§7.1 and §7.2 each turn on one small glyph that two page-image requests did not settle.** Both are
   recorded with both readings and no verdict. **Nothing in this paper's argument rests on either**,
   and under one reading of each there is no defect at all — so neither is a stop, and neither needs an
   act unless someone wants the paper's worked examples graded.
2. **★ WITHDRAWN AT THE CROSS-CHECK. FORMER WORDING, PRESERVED (#12):** *"**§7.4's second item leaves
   a fact about the reported experiments undecidable from these five pages**: whether fully diminished
   sevenths and flat-seventh minor-mode chords were in the chord set the reported runs used, or merely
   available in principle. **The sentence that would say so contrasts nothing as printed.** A reader
   routing this paper's chord vocabulary anywhere should carry that gap rather than pick a reading."*
   **There is no gap.** The paper says those chords *"are needed in these experiments"*; this side had
   misread the word. **The fact is now at F10 and 5.3, and this question is closed rather than left
   open.** See §9.2.

---

## §9 — The cross-check against the first extract

**Written after this file had landed carrying §1 to §8, and after — and only after — the first extract
was opened for the first time.** That is step 7 of the hundred-and-sixty-ninth handoff entry's §3
procedure, and the order was kept: **§1 to §8 above were written, swept and landed with the first
extract unopened.**

The first extract is
`reading_pass/extracts/raphael-stoddard-2003-harmonic-analysis-with-probabilistic-graphical-models.md`,
**22,611 bytes, read whole in one call.** It is dated 2026-09-05 and was written by the session that
booted on the hundred-and-thirteenth handoff entry, in the same sitting that read row 28.

### 9.1 What agreed

**EVERY NUMERIC VALUE THE TWO EXTRACTS BOTH TRANSCRIBED AGREES, DIGIT FOR DIGIT.** Named rather than
counted: `(12 × 2 × 7)² = 28224`; `12 × 2 × 2 + 7 × 7 + 7 = 104`; the 168 labels; `V(1) = V(2) = V(3) =
1`, `V(4) = 4`, `V(5) = 5`; `d ∈ {1,…,5}`; `r ∈ {0,…,5}`; `5 × 6 = 30`; *"around 5 or so short
movements"*; *"around 5 iterations"*; the 2-beat and 1-beat transition granularities; the file's 93,277
bytes; five pages; seven references. **Not one of the disagreements below carries a digit** — they are
over words, over an equation's conditioning set, and over where an equation's number sits.

**Three structural agreements are worth naming**, because each is two blind reads landing on the same
thing:

1. **Both reads independently met the rhythm-category tension of §7.3.** The first extract records it
   inline — *"a later sentence on the same page writes r ∈ {0, …, 5} and counts 5 × 6 = 30 output
   parameters — both statements are as printed"*. **Neither read took a verdict on it.**
2. **Both reads independently transcribed the label example's leading numeral as 3** (§7.1). The first
   extract quotes the sentence with *(3, major, II)* and **does not notice that its own next clause
   says the key is 2**; it later even uses *"2 = d major"* as the example's key in its own analysis.
   **So the transcription agrees and the finding is this side's alone.**
3. **Both reads independently established that the paper reports no measured result** — see 9.3.

### 9.2 Where this side was wrong and the first extract was right

**Two, both resolved at the paper, both corrected at their sites above with the former wording
preserved (#12), and both of them defects this side MANUFACTURED rather than merely missed.**

1. **Page 5, the chord-extensions sentence.** This side read *"are **possible** in these experiments"*
   and built a finding on the resulting broken contrast — §7.4's second item — and a question on top
   of that finding — §8.6's second. **The paper prints *"are NEEDED in these experiments"*.** The
   first extract read it correctly. **Re-read at page 5 at this cross-check; the sentence is coherent
   as printed and there was never a defect.** Both the finding and the question are withdrawn at their
   sites, and what the sentence actually establishes — that fully diminished 7ths and flat-seventh
   minor-mode chords were in the reported experiments — is now recorded as a fact at **F10** and
   **5.3**, where this side had recorded nothing.
2. **Page 3, where the equation number `(1)` sits.** This side read `(1)` as labelling the identity
   line `p(x'|x) = p(t', m', c'|t, m, c)`, and on that reading wrote §7.5: that the paper attributes
   an assumption to an equation that assumes nothing. **Re-read at page 3 at this cross-check: `(1)`
   sits at the right of the SECOND line — the factorization — and `(2)` at the right of the braced
   line below.** **So Eqn. 1 IS the factorization and the paper's attribution is exactly right.**
   §7.5 is withdrawn at its site. **The first extract did not report this defect either** — it simply
   cites *"Equations (1)–(2)"* — so the doubling did not catch it by agreement; **this side caught its
   own error only because the cross-check sent it back to the page.**

**One smaller one, in the same direction:** page 5's *"where **the** evolution of each voice"*, from
which this side had dropped the article. The first extract had it. Corrected at 3.10. **Nothing rests
on it.**

### 9.3 The decisive questions the first extract left, and what happened to each

The first extract's **Centrality** section names what a second pass is owed: *"its decisive questions
are finding (1)'s wording and whether any measured value exists anywhere in the paper."*

**The second is ANSWERED, by agreement of two blind reads.** This side read all five pages whole
**without knowing that question had been asked**, and met no accuracy figure, no error rate and no
comparison — §6 and **F5**, which rest on the paper's own sentence at page 5. The first extract reaches
the same place and draws the same consequence in its own finding (2): *"whatever establishment the
joint form has in the literature comes from the systems descended from it, not from this paper's own
results."* **Two independent whole reads, written without sight of each other, both met nothing.**

**The first is NOT answered by this sitting, and the bound is stated rather than blurred.** Finding
(1)'s subject is a wording in **`FRAMEWORK.md`** — its *"Voice membership is given"* bullet, which the
first extract reads as saying the authors *could not* extend their model. **`FRAMEWORK.md` was not
opened in this sitting at all**, so this side has checked nothing about that bullet. **What this side
can say, and says only of the paper:** page 5 states the extension as a proposal, calls voice
partitioning *"a challenging problem"* while adding that *"it is rather simple to create an algorithm
that performs reasonably"*, names Kilian & Hoos (2002) as an alternative, and then **assumes voiced
input**. **No sentence met in the five pages as read says the authors could not.** That is agreement
with the first extract on the paper's side of its finding; **the other half — what `FRAMEWORK.md`
actually prints — remains unchecked by this side.**

### 9.4 Where the paper goes against the FIRST extract — recorded, and that file left untouched

**Four, named rather than counted. None of them moves a value, and none of them moves any verdict the
first extract reaches.** Each was resolved at the paper.

1. **A transcribed equation carries a term the paper's own assumption removes.** The first extract
   writes the factorization as *"p(x' | x) = p(t', m' | t, m, **c**) · p(c' | t', m', t, m, c)"*. **The
   paper prints `p(t', m'|t, m)`** — without `c`. **The absent `c` is the entire content of the
   assumption**, and the first extract's very next sentence states that assumption correctly (*"the key
   change does not depend on the current chord"*), **so its own prose contradicts its own transcribed
   equation.** Re-read at page 3.
2. **A quotation with a word changed.** The first extract quotes page 2 as *"we partition the pitches
   in **our** musical composition"*. **The paper prints *"in any musical composition"*.**
3. **A quotation with a plural made singular.** The first extract quotes page 2 as *"murky distinctions
   between secondary **function** and actual modulation"*. **The paper prints *"secondary functions"*.**
   *(This is the mirror of the defect class the hundred-and-sixty-ninth entry records finding in row
   27's first extract, where a singular had been pluralised.)*
4. **A printed defect silently repaired inside quotation marks — recorded with both readings.** The
   first extract quotes page 3 as *"at random without regard for the new or old keys"*. **This side
   reads the printed word as *"and"* at every request of page 3 it made — the whole read, two at the
   read-back and one at this cross-check, four in all** — and records it as a printed defect at §7.4.
   *(★ "at the whole read and at two further page requests, three readings in all" at the post-landing
   check; corrected to four.)* **If the print is *"and"*, the first
   extract presented as verbatim a phrase it had repaired**, which is what quotation marks may not do.
   **If the print is *"at"*, this side has misread one short word three times and §7.4's remaining
   load-bearing item falls with it.** **Nothing else turns on it either way** — the sense is identical.

**THE FIRST EXTRACT WAS NOT EDITED.** This side recorded these and left that file untouched, on the
same ground the two preceding sittings of this line gave for row 27 and row 28: **rewriting another
read's text destroys what the doubling compares.** **Whether they are corrected at their own site is
the user's, and it is the same question he already holds for those two rows.**

### 9.5 What the cross-check did NOT do

It **opened no page of the paper except pages 2, 3 and 5**, and those only to resolve the
disagreements named above. It **read no other extract**, **did not open the progress record**, **did
not open `FRAMEWORK.md`, `population.md`, `candidacy_upgrades.md`, the slice derivation or the findings
surface**, and **ran no web access and no shell command**. It **moved no verdict**, **flipped no row**,
**routed nothing**, and **edited no file but this one**. It **changed no transcribed value**: every
figure, equation, table and quoted measurement above stands exactly as it was first landed, and the
sites it edited are **named rather than counted** — 3.6's note on the disputed word, 3.10's dropped
article, F10, 5.3, §7.4, §7.5, §8's head-note and §8.6's second item — with every former wording
preserved in place. *(★ CORRECTED AT THE POST-LANDING CHECK. FORMER WORDING, PRESERVED (#12): "the
corrections it made are at four sites — §7.4, §7.5, 3.10, and the F10/5.3 pair". That counted four
where it named five, and omitted three sites the cross-check also edited.)*

---

## §10 — The user-ordered fact- and source-check, run after this file had landed

**Written in the act that ran it, 2026-09-13.** The user's standing rule of 2026-09-12 extends the
pre-landing check to landed work on four axes — completeness, coherence, correctness, and misuse of
hyperbole and absolutes — and he ordered it on this sitting's writing. **This file was re-read WHOLE as
landed, at the device's own copy staged back, at 76,260 bytes.**

**Every defect it found is corrected above at its own site with the former wording preserved (#12).
Named rather than counted:**

- **A contradiction between two sections of this file.** §3.2 said the label example *"does not agree
  with itself"*; §7.1 says the disagreement holds only under one reading of one glyph and that under
  the other there is no defect at all. §3.2 now matches §7.1.
- **A paraphrase that dropped the paper's own hedge.** §3.4 read *"Keys remain constant over long
  stretches"*; the paper says they *"tend to remain constant for relatively long periods of time"*.
- **A table row left behind by a correction made at the cross-check.** §6's *Chord set actually used*
  row still read *"seven basic triads + dominant 7th"* after F10 and 5.3 had been corrected to record
  that fully diminished 7ths and flat-seventh minor-mode chords were *"needed in these experiments"*.
  **The cross-check corrected two sites and missed the third that carried the same fact.**
- **Four counts of this side's own page requests, every one an undercount**, at §7.1 (*"read twice"*),
  §3.6 and §7.4 (*"three separate page requests"*), and §9.4 (*"three readings in all"*). **Page 2 and
  page 3 were each requested four times in this sitting.** None of them changes a reading of the paper;
  each of them misstates what this side did.
- **A claim about this side's own reading that the read-back's own account refutes.** §8.1 said *"Every
  figure in this extract was re-read at its page"*; the read-back's four requests covered pages 2 to 5
  and not page 1, whose NSF grant number this extract transcribes.
- **A count that named more sites than it counted, and omitted others.** §9.5's *"four sites"* listed
  five and left out three the cross-check had also edited.
- **§8's head-note gained a third staleness item**, because 8.6's own *"two page-image requests"* is
  the same undercount.

**★ WHAT THIS CHECK ESTABLISHES ABOUT THE SITTING, AND IT IS NOT COMFORTABLE.** The
hundred-and-seventy-first handoff entry's (x) reported one degradation tell — *a number put on this
side's own reading without deriving it* — and said **"NONE reached a landed file."** **That was true of
the five instances it named and FALSE as a general statement: four more instances of the same tell were
in THIS file when it landed**, and are corrected only now. **The entry is corrected at its own site.**

**What this check did NOT do.** It fetched no page image, opened no paper, opened neither first
extract, ran no web access, swept no repository, and **edited no file but the three this sitting
wrote**. It **moved no verdict, routed nothing, flipped no row**, and **changed no transcribed value**:
every figure, equation, table and quoted measurement above stands exactly as it was first landed. It
reaches this sitting's own writing and nothing else.
