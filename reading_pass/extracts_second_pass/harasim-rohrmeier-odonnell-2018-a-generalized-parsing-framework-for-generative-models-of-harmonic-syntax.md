# Harasim, Rohrmeier & O'Donnell 2018 — "A Generalized Parsing Framework for Generative Models of Harmonic Syntax" — SECOND INDEPENDENT EXTRACT

> **STATUS: READING-PASS EXTRACT, SECOND PASS. NOTHING HERE IS RULED.** Written 2026-09-19 by the Cowork
> session that booted on `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_two.md`, under the
> second-pass rule of `cowork_reading_pass_commission_2026_08_30.md` §4 **as handoff entry 169 §3 quotes
> it** (a CENTRAL source is extracted in a second independent pass and the two extracts cross-checked)
> and the eight-step order of that same §3, as amended at its naming point by Ruling 2 of entry 186 §2.
> **This session did not open the commission itself**; the form below follows entry 169 §3 step 3 and
> the form of row 40's second extract, which was read for that purpose (§0). **The paper is Task B,
> L2's slice, row 21** — the row number is the progress table's
> (`reading_pass/l2_slice_reading_progress.md`, line 114); the candidacy file that table takes its row
> numbers from was not opened by this side. Held file:
> `docs/research_papers/harasim_rohrmeier_odonnell_2018_ismir_generalized_parsing_harmonic_syntax.pdf`,
> 1,143,148 bytes at this session's staging call. **This side did not list `docs/research_papers/`**;
> the file name was found by a search of the progress record for a PDF name containing *harasim* (one
> hit, line 1385), and that the file is this paper was checked at its page 1 (§1). **8 pages,
> established at the tool** by a deliberately out-of-range request (pages 30–31 refused with "PDF has 8
> pages"). Read whole in one request, pages 1–8; **the eight page images were present** (checked at the
> images, not at the call's success line).
>
> Page numbers below are the PDF's own (1–8). The pages print 152 to 159 in their running heads and
> feet, so PDF page *n* is printed page 151 + *n*.
>
> **Each quotation and each transcribed value below is a language model's read of a page image**; the
> arithmetic at §4.4 is this reader's own, done over those reads. Where a glyph was small or a reading
> unsure, the site says so. Misspellings inside quotations are the page's as read, and are left.

## §0 — Declarations of independence and its bound

- **What this side read of the progress table before opening the paper.** The table was searched, not
  read. The searches, named: (a) the bare word *"OWED"* with its line number, for each line that
  carries it; (b) for the rows numbered 21, 22, 23, 40 and 58, the row-number cell and up to 160
  characters after it; (c) the table's header line (line 60: *Row, Paper, Grade, Extract, Centrality,
  Second pass*); (d) for each line whose last cell carries the word OWED, that last cell whole; (e) two
  count-only searches, one confirming that row 21's line carries OWED inside a cell and one that the
  cell is the line's last; (f) a search for a
  PDF file name containing *harasim*, which returned the path alone. **Of row 21's line (line 114) this
  side therefore saw two strings:** its opening, *"| 21 | Harasim, Rohrmeier & O'Donnell — the held
  file, printing on page 1 the title \*"A GENERALIZED PARSING FRAMEWORK FOR GENERATIVE MODELS OF
  HARMONIC SYNTAX"\*, the"* (cut there by the search), and its last cell, *"**OWED** (flips to not owed
  if the user takes the NOT CENTRAL reading — stated in the extract so the choice is his)"*. **So this
  side knows that the first extract states a NOT CENTRAL reading as an alternative the user may take.**
  It does not know the grounds of either reading, what any finding of the first extract says, or how
  many findings there are. The same last-cell wording stands at rows 58, 40, 23 and 22.
- **`docs/research_papers/BIBLIOGRAPHY.md` was searched for the word *Harasim*** (two lines returned:
  line 35, this paper's row — authors, title, *"ISMIR 2018"*, a URL, a check mark and *"CC"*; and line
  78, the row of a different paper, of which Harasim is the second of four authors). It was not read
  beyond those two lines. *(★ CORRECTED at the user-ordered check, §10. FORMER WORDING, PRESERVED
  (#12): "the row of a different paper by other first authors".)*
- **Name-only look-up, declared under Ruling 2 (entry 186 §2):** `reading_pass/extracts/` was listed by
  file name at boot, to verify other extracts' sizes, and that listing was reused to find the first
  extract's name:
  `harasim-rohrmeier-odonnell-2018-a-generalized-parsing-framework-for-generative-models-of-harmonic-syntax.md`
  (88,188 bytes, modification time 1789212046566). **It was not opened before §9.** The file name
  carries the authors, the year and the paper's own printed title. Its size says the first extract is
  long; nothing else was taken from it. **The same listing shows, by name alone, extracts of works this
  paper cites or stands near:** `rohrmeier-2011-towards-a-generative-syntax-of-tonal-harmony.md` (this
  paper's reference [24], on which its §4 says its model is built), `rohrmeier-2006-…`,
  `granrothwilding-steedman-2012-…` and `granrothwilding-2013-…` (this paper's reference [4] is a 2014
  article by Granroth-Wilding and Steedman; by year it is neither of those two files' works) *(★
  CORRECTED at the user-ordered check, §10. FORMER WORDING, PRESERVED (#12): "a 2014 article by the
  same two authors, a different publication" — the second file's name carries one author)*, and
  `dehaas-magalhaes-wiering-veltkamp-2013-harmtrace-…`. **None of them was opened.**
- **Contamination from the record's own text, beyond those strings.** Of the records read at boot
  (entry 202 whole; entries 201, 200, 186 and 169 whole; 188 at §4–§5; 198 at §7; 152 at its lines
  45–79; 118 at its lines 20–94; `CLAUDE.md` at its six spans; `DECISIONS.md` whole; `STATUS.md` whole;
  the gating answer's identity list), none summarizes this paper's content; entry 202 §3 names row 21
  by its authors and its first extract's size. **Several passages read at boot bear on the paper's
  SUBJECT and not on the paper**, and are named because a reader who knows them may read this paper
  with them in mind:
  - the decisions register's index lines D-501 (a tool may read a written chord symbol only as a
    comparison or ground-truth label, never as input to the analyzer) — **this paper's input is chord
    symbols**; D-001 (key, mode and chord are inferred by one joint decode) and D-526 (the joint
    state's chord axis is scale-degree-valued, relative to the state's own tonic and mode); D-337 (a
    lean toward another degree is a tonicization by default; a key change needs a confirming cadence
    and persistence); D-084, D-406, D-408, D-410, D-411, D-414 and D-502 to D-509 by their index lines
    (lines about a catalog of named progressions and substitutions and about recognizing them) *(★
    CORRECTED at the user-ordered check, §10. FORMER WORDING, PRESERVED (#12): "D-084 and D-406 to
    D-414 and D-502 to D-509 by their index lines (a catalog of named progressions and substitutions,
    and its recognizer, as a consumer of the function layer)" — the index as read carries no D-407,
    D-409, D-412 or D-413, and the parenthesis fitted D-084 and not each of the others)*;
    D-422, D-497 and D-500 (the jazz fit is deferred; the Jazz preset constants are unvalidated;
    gate-grade jazz ground truth is wanted); D-096, D-097, D-270 and D-271 (fitted values are fit once
    against ground truth, with held-out evaluation and a capacity budget declared first); D-533 (a
    continuation too rare to have its own stored probability is scored from the row's leftover); D-586
    (what *function* names in the machine-learning literature);
  - `CLAUDE.md` principles #20 (fit and evaluation separated), #21 (ground truth is a measurement tool
    too, with its D-474 block) and #24 (every reported value carries its uncertainty). **§5 below sets
    what the pages state beside those three; nothing is concluded here about any of them.**
- **Memory.** One memory tool call was made in this sitting, before the paper was opened: a read of
  the project's preferences file, which carries one line about the form of a decision surface and
  nothing about this paper or its subject. The listing of the user's Cowork memory store that the
  system delivers at session start shows, by one-line description alone, a file about a ban on
  user-written chord symbols as analyzer input and a file about a set of twenty scores whose chord
  symbols *"are rhythm-section instructions, not analysis"*; **neither was opened.** Both bear on this
  paper's subject (chord symbols as the thing analyzed) and not on the paper.
  `FRAMEWORK.md`, `population.md`, the findings surface, the slice derivation and the candidacy file
  were **not** opened.
- **Row 40's second extract was read for its form** — its lines 1–80 (banner and §0) and its section
  headings by search. That paper is about cadence choice in Bach's chorale harmonizations and shares no
  author with this one. Nothing from it is used below.
- **Route:** this is entry 169 §3's *fresh session* route. The booting entry (202) does not summarize
  the first extract of row 21, so the caution entry 169 §3 relays from the remedial commission (a fresh
  session is the worse route where the newest handoff entry summarizes the first extract) does not
  bite here on that ground. **The bound that does bite is the last-cell string above.**
- **This reader's prior knowledge.** This side is a language model and has general knowledge of
  context-free grammars, chart parsing, variational inference and of the line of work on generative
  grammars of harmony. **What the paper says is set down from the page and located, not from that
  knowledge.** Where this reader reasons beyond the page (the bold joining sentences in §2, under
  the rule stated at §2's head; the zero-based reading at claim 27; the arithmetic of §4.4; two
  remarks in §7), the site or that rule says the reasoning is this reader's. §7 lists things a reader might supply from the subject that the
  pages as read do not say.

## §1 — Identity, checked at page 1

- **Printed title (page 1):** *"A GENERALIZED PARSING FRAMEWORK FOR GENERATIVE MODELS OF HARMONIC
  SYNTAX"*.
- **Printed authors and affiliations (page 1):** Daniel Harasim (affiliations 1 and 2), Martin
  Rohrmeier (1 and 2), Timothy J. O'Donnell (3). 1: *"Digital and Cognitive Musicology Lab, École
  Polytechnique Fédérale de Lausanne, Switzerland"*; 2: *"Institut für Kunst- und Musikwissenschaft, TU
  Dresden, Germany"*; 3: *"Department of Linguistics, McGill University, Canada"*. One e-mail address
  is printed, the first author's.
- **Venue, as the paper prints it:** the licence footer on page 1 gives the attribution *"19th
  International Society for Music Information Retrieval Conference, Paris, France, 2018"*; the running
  heads of pages 2 to 8 read *"Proceedings of the 19th ISMIR Conference, Paris, France, September
  23-27, 2018"*. Printed pages 152 to 159. Licence as printed: Creative Commons Attribution 4.0
  International (CC BY 4.0).
- **Against the bibliography's row (line 35, by search):** authors, title and *"ISMIR 2018"* match the
  page. **No identity finding.**
- **Shape of the paper:** §1 Introduction (pages 1–2); §2 Overview of the approach (page 2); §3 Abstract
  context-free grammars — §3.1 Definitions, §3.2 Parsing, §3.3 Inference of rule probabilities (pages
  2–4); §4 A generative model of Jazz harmony (pages 4–5); §5 The turnaround problem (page 5); §6
  Experiments — §6.1 Dataset, §6.2 Tree accuracy evaluation, §6.3 Performance diagnosis using scale
  degree frequencies (pages 5–6); §7 Conclusion and future research (page 6); §8 Acknowledgements (page
  6); §9 References, [1] to [32] (pages 7–8). Six figures; no numbered table.

## §2 — Claims, labeled

Labels as in the theory-grounding corollary of `CLAUDE.md` (read at boot): **FACT** — stated or
measured in this paper, about its own method, data or measurement; **THEORY** — published theory the
paper takes over, with the reference it gives; **CONJECTURE** — what the paper offers as a possibility,
an expectation or an interpretation. The label says what kind of statement the paper makes. It does not
say that this reader checked the statement against anything but the page. **A sentence in bold that
follows a quotation and draws something from it is this reader's step, not a sentence of the paper.**

### §2.1 The problem the paper sets (abstract and §1, pages 1–2)

1. **FACT (the paper's own framing).** The abstract names three challenges for models of harmonic
   syntax: *"detecting local and higher-level modulations (most previous models assume a priori
   knowledge of key), computing connected parse trees for long sequences, and parsing sequences that do
   not end with tonic chords, but in turnarounds."* It says the paper addresses them with *"a new
   generative formalism Probabilistic Abstract Context-Free Grammars (PACFGs)"* and with *"variants of
   standard parsing algorithms that efficiently enumerate all possible parses of long chord sequences
   and to estimate their probabilities."*
2. **FACT (abstract).** *"PACFGs specifically allow for structured non-terminal symbols in rich and
   highly flexible feature spaces. The inference procedure moreover takes advantage of these
   abstractions by sharing probability mass between grammar rules over joint features."*
3. **FACT (abstract; the headline claim).** *"The PACFG model outperforms the standard context-free
   approach while reducing the number of free parameters and performing key finding on the fly."* What
   the pages measure beside each of those three clauses is at §4 and §7.
4. **THEORY ([19, 22–24, 30, 31]).** *"Hierarchical models express these relations by assuming a latent
   hierarchical structure"*. The worked example (page 1): in the chord sequence Am7 D7 G7 C△ (the
   paper's △ denotes a major-seventh chord) the first three chords *"form a II V I sequence with
   reference to G7 which is the dominant in C major"* and so *"form a dominant phrase [24]"*; that
   phrase as a whole refers to the tonic chord, and *"All four chords together thus form a tonic
   phrase."*
5. **THEORY (Figure 1, page 1, *"following the approach from [22]"*).** A tree over the A-part of
   *Afternoon in Paris*, whose leaves as read are C△, Cm7, F7, B♭△, B♭m7, E♭7, A♭△, Dm7, G7, C△. Each
   inner node carries a scale degree with a key as subscript. *"Subdominant, dominant, and tonic
   phrases are denoted by the scale degrees II, V, and I, respectively."* The paper's remark on it:
   *"the subsequence Cm7 F7 B♭△ is both a tonic progression in B♭ major and a dominant progression in
   E♭ major. It forms a dominant phrase in A♭ major together with B♭m7 and E♭7."* **So in this
   analysis one chord carries a scale degree in a local key, and that local key is itself placed as a
   scale degree of a key higher in the tree.**
6. **FACT (the paper's account of earlier work, page 1–2).** Such models *"have been successfully
   applied to melody harmonization [16], chord inference from audio [5, 6], and harmonic similarity
   [7]"*; there is *"some empirical evidence for the psychological reality of hierarchical structures
   in music [15, 25]"*. Computational implementation *"to date has been limited to relatively small
   datasets"*: monophonic melodic data [21]; *"a corpus of 39 blues chord progressions with a maximum
   of 24 chords per progression [12]"*; *"a dataset of 76 chord progressions (avg. length 40) from
   Jazz-standards that was restricted to subsequences of pieces that did not change key [4]"*. *"All
   these earlier approaches assume the knowledge of the key of the pieces a priori."*
7. **FACT (the paper's statement about available ground truth, page 2).** There are *"music databases
   of simplified Schenkerian analyses [13], syntactic analyses of melodies based on the generative
   theory of tonal music [8], and annotated harmonic functions [4]. However, to the best of our
   knowledge there is currently no dataset of hierarchically analyzed chord sequences by human experts
   that could serve for the training or the evaluation of models of harmonic syntax. As a consequence,
   there exist no comparisons of models of harmonic syntax against expert analyses."* This is the
   paper's statement as of 2018, hedged by the paper itself (*"to the best of our knowledge"*).
8. **FACT (what the paper says it does, page 2).** *"A first model of Jazz harmony is proposed in this
   framework that covers full pieces by incorporating modulations (i.e., changes in key). We train the
   model in a semi-supervised fashion on a dataset of Jazz-standards and evaluate it on a small set of
   hand-annotated hierarchical analyses."* The implementation is *"publicly available as a package of
   the Julia programming language [1]"*, with a footnote URL (§5).

### §2.2 Why a plain context-free grammar is not enough, as the paper argues it (§2, page 2)

9. **FACT (the paper's argument).** *"Musical categories such as scale degrees, for example, are
   equipped with an arithmetic structure that corresponds to musical transposition."* The paper calls a
   rule of the form X → Y X *"a preparation of X by Y"*, and gives the general principle, with [24] as
   its source: any category consisting of a scale degree *x* and a key *k* *"can be prepared by an
   ascending diatonic fifth (x + 4 mod 7)"* in the same key.
10. **FACT (the design requirement the paper states).** *"a framework for modeling musical structure has
    to account for the fact that the musical categories and rewrite rules are grouped into
    key-independent classes. For example, both V_B♭ and V_A♭ are fifth scale degrees. The probabilities
    of the application a rule to V_B♭ and V_A♭ should therefore be related."* (Subscripts set down here
    with an underscore; the page prints them as subscripts.)
11. **FACT.** In the paper's framework *"constituent categories are allowed to be of any data type and
    the rules are generalized partial functions"*, so that rules *"can therefore take advantage of the
    algebraic structure of categories"*, and the probabilistic version can *"express a wider range of
    probability distributions over rules."*

### §2.3 The formalism (§3.1, pages 2–3)

12. **FACT (Definition 1).** A non-probabilistic Abstract Context-free Grammar is a tuple of a set *T* of
    terminal symbols, a set *C* of constituent categories, a set of start categories *C₀ ⊆ C*, and a set
    Γ of partial functions from *C* to sequences over *T ∪ C*, *"called rewrite rules or rewrite
    functions"*. A derivation applies a rewrite function to the leftmost category at each step; the
    language is the set of terminal sequences that have a derivation.
13. **FACT (the paper's statement of expressive power).** *"Note that if C is finite, the languages that
    can be described by ACFGs are exactly the languages that can be described by standard context-free
    grammars (CFGs)."* The construction given: each rewrite function whose domain has *k* members is
    divided into *k* ordinary context-free rules. **So for a finite category set the formalism adds no
    language a context-free grammar lacks; what it changes is how rules are grouped, and through that
    how probabilities are shared (claim 15).** The second half of that sentence is this reader's joining
    of claims 13 and 15, not a sentence of the paper.
14. **FACT (Definition 2).** A Probabilistic ACFG associates each category *A* with a random variable
    over rewrite functions, with positive probability for a function exactly when it is defined at *A*.
    A derivation's probability is the product of the probabilities of its steps; a terminal sequence's
    probability is the sum over its derivations. *(The clause stating the domain condition reads on the
    page image, as this side read it at two requests of page 3, "A ∈ dom(A)"; the words before it on
    the page are "that is A is in the domain of r". Set down as read; nothing turns on it.)*
15. **FACT (the property the paper builds on).** *"Note that PACFG categories can share the same
    probability distribution over rewrite functions without rewriting to exactly the same right-hand
    sites. This important property allows us to model the structural relations between musical keys."*
    And: *"The sharing of probability mass between rules additionally reduces the number of free
    parameters of a PACFG model."*
16. **FACT (the toy example, page 3).** A grammar with categories S, A, B and terminals a, b generates
    sequences of only a's or only b's. As an ordinary probabilistic grammar *"no probability mass is
    shared between rules"*; with a rewrite function r₃(x) = x x defined for both A and B, *"the grammar
    can learn something about A → A A when it observes B → B B and vice versa."* The paper's closing
    sentence on it: *"Analogously, a PACFG of Jazz chord sequences can generalize classical rewrite
    rules so that their probabilities do not depend on the keys of their left-hand sides to model
    transpositional invariance."*

### §2.4 Parsing (§3.2, pages 3–4; Figure 2)

17. **FACT.** The paper defines parsing as *"the task of computing the distribution of parse trees
    conditioned on this sequence."* It does not put grammars into Chomsky normal form beforehand:
    *"Since grammar transformations into Chomsky normal form considerably blow up the grammar, the here
    presented parser transforms grammars on the fly during parsing, similar to the transformation
    presented in [18]."* Each rule's right-hand side becomes a chain of states with a transition
    function and a completion function; *"the states and the transition function form a search trie"*,
    which *"leads to a compact representation of the forest of all trees for a given input sequence."*
    More generally the parser *"can handle any transition and completion functions derived from
    finite-state automata, see [14]."*
18. **THEORY ([3, 29]).** The algorithm is stated in the *parsing as deduction* framework, which the
    paper describes as *"a meta-formalism to state and compare different parsing algorithms"*. Figure 2
    gives the items (edges and constituents, each with a start and an end index), the goal items, the
    axioms (one per terminal of the input) and three deduction rules named *introduce edge*, *complete
    edge* and *fundamental rule*. The algorithm is bottom-up (*"a generic bottom-up parsing
    algorithm"*). *(Figure 2 prints the goal items with the condition "for A ∈ S", S being the set of
    parser states in the text; the text says the goals "come from the set of start categories". Read
    the same at two requests of page 3; set down as read.)*
19. **What §3.2 does not give:** a complexity statement, a running time, or a sequence length at which
    the parser was run beyond what §6.1 states (pieces of at most 40 chords). See §7.

### §2.5 Learning the rule probabilities (§3.3, page 4)

20. **FACT.** Each category's distribution over its rewrite functions has a Dirichlet prior with
    pseudocounts. The posterior is approximated by variational Bayesian inference [2, 11, 32]:
    following [17], a Dirichlet variational distribution per probability vector under the mean-field
    approximation, fitted by a coordinate descent *"similar to the expectation-maximization
    algorithm"*. The update as the paper states it: *"we set the pseudocounts of our variational
    distributions equal to the expected number of rule usages plus the pseudocount for each rule in the
    prior distribution."*
21. **FACT.** The standard algorithm of [17] needs expected counts over the whole corpus before each
    update; the paper uses instead the stochastic variant of Hoffman et al. [9], with updates computed
    from *"randomly sampled minibatches of the data"*: *"We make use of this stochastic variational
    Bayes algorithm in the results reported below."*
22. **What §3.3 does not give:** the pseudocount values used, a step-size schedule, the number of
    passes over the data, or a random seed. §6.2 speaks of the models before training as *"Under a uniform
    prior"*, and says minibatches held 8 sequences. See §7. *(★ CORRECTED at the user-ordered check,
    §10. FORMER WORDING, PRESERVED (#12): "§6.2 adds that the models were compared "Under a uniform
    prior"" — the page uses the phrase of the untrained state, not of the comparison as a whole.)*

### §2.6 The grammar of Jazz harmony (§4, pages 4–5)

23. **THEORY ([24]).** The model *"models the syntax of Jazz harmony following the proposal in [24]. That
    work addressed the problem of finding a restrictive grammar that describes the full variety of
    syntactic relations in the musical idiom of Jazz-standards."*
24. **FACT (the terminals).** A terminal is a pair of a chord root and a chord form, the form being
    *"one of: a major triad, a major-seventh chord, a major sixth chord, a dominant-seventh chord, a
    minor triad, a minor-seventh chord, a half-diminished-seventh chord, a diminished seventh-chord, an
    augmented triad, or a suspended chord."* Ten forms as listed. **The input to this model is a
    sequence of chord symbols; as the model is described, no notes enter it.**
25. **FACT (the categories).** *"The categories are modeled as pairs of scale degrees and keys"*: seven
    scale degrees (written with Roman numerals I to VII) and twenty-four keys, a key being a pitch
    class for its root and a mode, major or minor. *"All categories with scale degree I are start
    symbols"*. So a piece may start from the tonic category of any of the twenty-four keys; the key of
    the piece is not an input.
26. **FACT (the rewrite functions, as printed on pages 4–5).** With ⟨x, k⟩ a category of scale degree *x*
    and key *k*, and μ(x, k) *"the modulation from k into the key of scale degree x (e.g. μ(II, (0,
    maj)) = (2, min), the key of the second scale degree of C major is D minor)"*:
    - *prolongation*: ⟨x, k⟩ → ⟨x, k⟩ ⟨x, k⟩, for each scale degree;
    - *diatonic preparation*: ⟨x, k⟩ → ⟨x + 4 mod 7, k⟩ ⟨x, k⟩, for each scale degree but IV;
    - *dominant preparation*: ⟨x, k⟩ → ⟨V, μ(x, k)⟩ ⟨x, k⟩, for each scale degree but I;
    - *plagal preparation*: ⟨I, k⟩ → ⟨IV, k⟩ ⟨I, k⟩;
    - *modulation*: ⟨x, k⟩ → ⟨I, μ(x, k)⟩;
    - *mode change*: the tonic category of a major key rewrites to the tonic category of the minor key
      on the same root, and the reverse;
    - *diatonic substitution*, for x among I, II and V: I in major → VI; I in minor → III; II → IV;
      V → VII, each in the same key;
    - *dominant substitution*, indexed by i among 3, 6 and 9: ⟨V, (r, m)⟩ → ⟨V, (r + i mod 12, m)⟩ —
      the fifth degree of the key whose root lies i semitones higher, same mode.
27. **FACT (termination).** *"Additionally, Γ contains appropriate termination rules C ⇸ T according to
    standard Jazz harmony theory (e.g. seventh-chord-termination(⟨4, (0, maj)⟩) = G7, see [20] for
    further explanation)."* **The termination rules are not listed in the paper**; one example is given
    and the reader is sent to [20] (a jazz theory textbook, as the reference list has it). In that
    example the scale degree is written as the number 4 where the text elsewhere writes V; read with
    *"x + 4 mod 7"* in claim 26, scale degrees are counted from zero in the formulas. That reading is
    this side's; the page does not say so in words.
28. **FACT (the tying of probabilities, the point of the construction).** The distribution over rules
    rewriting a category is *"a categorical distribution such that"* the probability of a rule at ⟨x,
    k⟩ equals its probability at ⟨x, k′⟩ *"for all scale degrees x, rules r, and keys k, k′ that have
    the same mode. That is, the probability of r rewriting ⟨x, k⟩ does not depend on the root of k which
    enables the model to learn the parameters of its probability distributions key-independently."* **So
    the tying is across the twelve roots and not across the two modes**: major and minor keep separate
    distributions.
29. **FACT (the paper's grouping, page 5).** *"These grammar rules can be grouped into three classes: the
    prolongation rule, preparation rules, and substitution rules. Preparation rules create categories
    that for the listener generate the expectation to hear the prepared chord. Substitution rules
    substitute chords for other chords that fulfill an equivalent function inside the sequence such as
    tritone substitutions of dominants in Jazz."* The modulation and mode-change functions are not
    placed in any of the three classes by that sentence.

### §2.7 The turnaround problem and cyclic parsing (§5, page 5; Figure 3)

30. **FACT (the problem).** A lead-sheet's chord sequence *"is repeated multiple times in a
    performance. While some lead-sheets end with tonic chords, others include harmonic upbeats to the
    first chord of the piece at the end of the sheet, called turnarounds."* Example: *All of me*
    *"starts for example with a C△ chord and ends with the turnaround E♭°7 Dm7 G7."* The grammar of §4
    *"assumes that pieces end with a tonic chord. Therefore, a simple implementation of this grammar
    would not able to parse lead-sheets that end in turnarounds."*
31. **FACT (the remedy).** *"We solve this problem by cyclic parsing, meaning that we assume that
    constituents can have spans from the end of a piece back to the beginning, see Figure 3."* Figure 3,
    as this side read the drawing, shows the end of the sheet joined to its first chord under one
    constituent. How a span that wraps
    around is counted in the span measurement of §6.2 is not stated.

### §2.8 The experiment and what it found (§6, pages 5–6) — values at §4

32. **FACT (data).** The iRealPro dataset of Jazz standards: *"1173 chord sequences
    electronically-encoded by the Jazz musician community including metadata such as the titles,
    composers, and keys"*, converted to the Humdrum format by Shanahan and Broze [28]. *"The chord
    forms in the iRealPro dataset include information about ninths and elevenths that are not
    considered in this study."* Training used the pieces *"that consist of at most 40 chords"* and,
    among those, the ones the cyclic parser could parse (§4.1).
33. **FACT (the four things compared).** *"(i) the proposed PACFG model that uses a representation of
    rules independent of key, (ii) its PCFG counterpart the rules of which are not independent of key,
    (iii) a baseline of randomly generated trees, and (iv) a right-branching baseline in which all
    constituents split into a constituent on the left and a terminal symbol on the right."* **The
    comparison the headline rests on is therefore between two versions of one grammar, with and
    without the tying of claim 28. No run of another published system is met in the pages as read.**
34. **FACT (the measurement).** *"They are evaluated on 13 pieces hand-annotated by the authors. We
    report the predicted tree accuracy. That is the precision of correctly predicted spans of internal
    tree nodes. A span of a tree node is defined as the start index of its leftmost leaf together with
    the end index of its rightmost leaf."* **As defined, the measurement is over spans alone: the
    category on a node (its scale degree and its key) does not enter it.**
35. **FACT (results; values at §4.2).** Trained, the key-independent model reaches 45.95 % and the
    key-dependent one 39.43 %, from a common 36.30 % before training. The paper's reading: *"The PACFG
    model was thus able to learn more from the data than the PCFG model."* And on size: *"the number of
    free parameters of the PCFG model is approximately 12 times higher than the number of free
    parameters of the APCFG model."* (*"APCFG"* as printed.)
36. **CONJECTURE.** The model *"is still much simpler than models that produce state-of-the-art parsing
    results in computational linguistics"*, which condition on more than the parent category; *"We
    anticipate that the inclusion of similar structures into musical parsing models will lead to
    similar improvements in performance."*
37. **FACT (learning curve, Figure 5).** *"this figure is produced using a stochastic algorithm and is
    therefore inherently noisy. We see that the stochasticity of the inference algorithm leads to
    random jumps of the accuracy up to 0.5%. The models appear to do most of their learning in the
    first 10 minibatches."* See §4.3 for what the plot shows as read by eye.
38. **CONJECTURE (the paper's diagnosis, §6.3, Figure 6).** *"The scale degrees VI in major and III in
    minor are more frequently used by the model than expected. Because these scale degrees are
    substitutions for the first scale degrees and because they enable modulations into the relative
    key (e.g. from C major to A minor and vice versa), the model may be using them to alternate between
    relative keys. The prominence of the VII in minor keys is probably related to the fact that it has
    a dominant-seventh chord form. The model may be interpreting a I in major as a III in the relative
    minor key that is then prepared by the VII in minor."* The paper's example: the transition G7 C△
    *"would in this case be derived by"* a chain that starts from the tonic category of A minor,
    rewrites it to III of A minor, prepares that by VII of A minor, and terminates VII as G7 and III as
    C△. **So the paper itself reports that its trained model may be reading a plain dominant-to-tonic
    in C major as an event in A minor.** The words *"than expected"* are not given a stated expectation
    or a reference distribution in the pages as read.

### §2.9 The paper's conclusions and stated future work (§7, page 6)

39. **FACT (the paper's summary).** *"Experiments show that in contrast to standard context-free models,
    the proposed model is able to learn characteristic structures of the observed data. To the best of
    our knowledge, this is the first computational approach that automatically performs hierarchical
    analyses of chord sequences and evaluates them on analyses by human experts."*
40. **FACT (the paper's own statement of what is missing).** *"Our future research will in particular
    focus on expanding the dataset of hand-annotated expert analyses to provide significance tests of
    the performance comparison of different models, for example."* **The paper thereby implies that
    its comparison comes without a significance test; none is met in the pages as read.**
41. **CONJECTURE (further uses the paper names).** *"models of unsupervised grammar induction, joint
    models of multiple musical levels of musical structure like harmony and rhythm, and models of
    musical structure that have more complex dependencies than those representable in simple tree
    structures."*

## §3 — Coupling facts (mandatory)

**What the paper assumes upstream.**
- **A chord-symbol sequence, already made.** Each input element is a chord root with one of ten chord
  forms (claim 24). As the model is described, what lies upstream of that — notes, voicing, which notes
  are chord tones — is not in it. Where the chord symbols come from is a lead-sheet encoding made by a community of musicians
  (claim 32).
- **Extensions above the seventh are dropped** before the model sees the chord (*"ninths and
  elevenths that are not considered"*).
- **No durations, no meter and no barlines enter the model as described.** The grammar's terminals are
  chords and its categories are scale degrees with keys; the pages as read name no duration or
  metrical feature of the input. The paper lists *"joint models of … harmony and rhythm"* as future
  work (claim 41).
- **As described, no key is given to the model.** The dataset's metadata includes keys (claim 32); the model's start
  categories are the tonic categories of all twenty-four keys (claim 25).
- **A piece is assumed to be one tonic phrase**: it derives from a single tonic category, and, without
  cyclic parsing, ends on a tonic chord (claim 30).
- **The rule inventory is given by hand from theory** ([24] for the rewrite functions, [20] for the
  terminations); what is learned is the probabilities (claims 20, 23, 27).

**What the paper hands downstream.**
- A distribution over parse trees of a chord sequence (claim 17). In a tree each chord sits under a
  category that is a scale degree in a local key, and local keys nest (claim 5). **Against its reference
  analyses the paper measures the spans of the tree; no measurement of another thing it hands down
  is met in the pages as read** (claim 34; Figure 6 reports usage counts, with no reference to set
  them against).
- Learned rule probabilities tied across the twelve roots, separate by mode (claim 28).
- Software: a Julia package (URL at §5).

**Its stated scope.**
- The idiom of Jazz standards; the iRealPro collection; pieces of at most 40 chords; of those, the
  pieces the cyclic parser can parse (357 of 394, §4.1). The 37 that it cannot parse are outside
  what was trained on; the paper does not describe them.
- The formalism of §3 is presented as general (*"a new general grammar and parsing framework tailored
  to the needs of music"*); the one grammar built and measured in it is the Jazz one.

## §4 — Measured results, as the paper states them

### §4.1 The data counts (§6.1, page 5), as printed

| Quantity | As printed |
|---|---|
| Chord sequences in the iRealPro dataset | 1173 |
| Pieces of at most 40 chords, *"considered to train the models"* | 394 |
| Of those, parsable *"using the standard approach"* | *"34.52% (136)"* |
| Of those, parsable *"using the cyclic parsing approach"* | *"90.61% (357)"* |
| The paper's inference from the two | *"Less then 55% of the considered Jazz-standards therefore end in turnarounds."* |
| Sequences the models were trained on | *"the 357 cyclic parsable sequences"* |
| Minibatch size | 8 sequences |
| Pieces the models were evaluated on | *"13 pieces hand-annotated by the authors"* |

### §4.2 Tree accuracy (§6.2, pages 5–6, running text; Figure 4), as printed

*(★ CORRECTED at the user-ordered check, §10. FORMER LOCATOR, PRESERVED (#12): "page 5". "under 10%"
is at the foot of page 5; the four printed values are at the head of page 6.)*

| Model | Before training (*"Under a uniform prior"*) | Trained |
|---|---|---|
| PACFG (rule probabilities independent of the key's root) | 36.30 % | 45.95 % |
| PCFG (rule probabilities not independent of key) | 36.30 % | 39.43 % |
| Randomly generated trees | — | 15.35 % |
| Right-branching baseline | — | *"under 10%"* (no value printed) |

The paper's words for the two gains: the PCFG *"only improves its performance by about 3%"* and the
PACFG *"improves by about 10%"*, each *"in comparison to the uniform prior"*. The two baselines are
not described as trained; Figure 4 draws each of them at the same height under both of its headings.

**Figure 4 as read by eye** (a bar chart headed *posterior* and *prior*, four bars each, with error
bars; the text says they show *"the means of the tree accuracies including 95% confidence intervals
as error bars"*). **No numeric bound of any of those ranges is printed.** By eye, and no finer than
the plot allows: under *posterior* the PACFG bar's error bar runs from about 0.40 to about 0.54 and the
PCFG bar's from about 0.30 to about 0.47; under *prior* the two bars stand at the same height with
error bars from about 0.29 to about 0.44. **As read by eye, the ranges of the two trained models
overlap between about 0.40 and about 0.47** — roughly half of the PACFG range and somewhat less than
half of the PCFG range. That is an eye reading of a small plot and carries no more weight than that; what the
paper itself says about significance is claim 40.

### §4.3 Figures 5 and 6, as read

- **Figure 5** (page 6): tree accuracy of the two models per minibatch update. Caption: *"Note that
  the y-axis displays only values between 33% and 50%."* The horizontal axis is labeled *minibatch
  update* with ticks at 20, 40, 60 and 80 and runs to about 100. The PACFG line lies above the PCFG
  line from early on. **By eye the lines move up and down by more than half a percentage point from
  one update to the next** (the PACFG line ranges between about 0.42 and about 0.49 after its first
  rise), where the text says *"random jumps of the accuracy up to 0.5%"*. What quantity the text's
  0.5 % refers to is not clear to this reader from the pages; the difference is recorded, not resolved.
  **At which minibatch update the values of §4.2 were taken is not stated.**
- **Figure 6** (page 6): caption *"Expected usage of scale degrees to parse the full training
  dataset"*; the text calls it *"the expected frequency of scale-degree use in the whole corpus"*. A
  bar chart of absolute frequency per scale degree, minor and major side by side. No value is printed;
  by eye the tallest bar is V in major (about 3,100), then III in minor (about 1,950), V in minor
  (about 1,400), I in minor and VII in minor (each about 1,250), I in major (about 1,200); III in
  major and VI in minor are the shortest (each about 100); VI in major stands at about 800.

### §4.4 Arithmetic over the printed values (this reader's, not the paper's; done by hand)

- 136 / 394 = 0.34518…, which rounds to the printed 34.52 %. 357 / 394 = 0.90609…, which rounds to the
  printed 90.61 %. Both agree with the page.
- **The turnaround inference does not follow from those two counts as this reader computes it.** Pieces
  parsable cyclically and not by the standard approach: 357 − 136 = 221; 221 / 394 = 0.56091…, that
  is 56.09 %, which is more than 55 % and not *"Less then 55%"*. (The same from the printed
  percentages: 90.61 − 34.52 = 56.09.) Whether the paper's sentence rests on a different count, or
  whether *"Less"* is a slip for *more*, the pages do not say. **An arithmetic residue, recorded and
  not resolved.**
- Not parsable by either approach: 394 − 357 = 37 pieces, 9.39 %.
- Gains over the common starting value: 39.43 − 36.30 = 3.13 points (the paper: *"about 3%"*); 45.95
  − 36.30 = 9.65 points (the paper: *"about 10%"*). Between the two trained models: 45.95 − 39.43 =
  6.52 points. The paper's *"%"* in those two phrases is a difference in percentage points, not a
  ratio.
- 357 sequences in minibatches of 8 is 44.6 minibatches for one pass over the training set; Figure 5's
  axis runs to about 100. Whether minibatches were drawn with replacement, or the data passed over
  more than once, is not stated.

### §4.5 What is not among the measured results

Each line is a negative over the eight page images as read by this side.

- **No measurement of key finding.** The abstract says the model performs *"key finding on the fly"*
  and the dataset's metadata includes keys; the pages as read report no comparison of any key the
  model assigns with any reference key.
- **No measurement of modulation detection**, which the abstract names first among the challenges.
- **No measurement of the categories on tree nodes** (scale degree, local key); the measurement is
  over spans (claim 34).
- **No running time and no parse counts**, beside the abstract's *"efficiently enumerate all possible
  parses of long chord sequences"*.
- **No comparison with any earlier system** ([4] among them); the comparison is internal (claim 33).

## §5 — What the paper states about uncertainty, reproducibility and ground truth (against #24, #16, #21, #20)

- **Uncertainty (#24).** Error bars called 95 % confidence intervals are drawn in Figure 4; no numeric
  bound is printed, and over what the ranges were computed (the 13 pieces, repeated training runs, or
  something else) is not stated. No significance test is reported, and the paper says one is future
  work (claim 40). The learning curve is called *"inherently noisy"* by the paper (claim 37).
- **Reproducibility (#16).** Code: footnote 1, *"https://github.com/dharasim/GeneralizedChartParsing.jl"*.
  Data: footnote 2, *"https://irealpro.com"*; footnote 3,
  *"https://musiccog.ohio-state.edu/home/index.php/iRb_Jazz_Corpus"* (the two separators in the last
  segment read as underscores; small print, reading unsure). **Not stated in the pages as read:** where the 13 hand-made analyses
  can be obtained; which 13 pieces they are; a version of the code or the data; a random seed; the
  prior pseudocounts.
- **Ground truth (#21).** The reference analyses are *"13 pieces hand-annotated by the authors"* — the
  people who wrote the grammar being measured. **Not stated:** how many of the authors annotated each
  piece, by what procedure, whether the annotators saw the grammar's rule set while annotating (they
  are its authors), or any agreement value between annotators. The paper's own statement that no
  expert-analyzed dataset existed (claim 7) is the reason it gives for making its own.
- **Fit and evaluation (#20).** Training is on the 357 chord sequences; the pages describe no tree
  annotation entering the training. **Whether the 13 evaluated pieces are among the 357 is not
  stated.** The introduction calls the training *"semi-supervised"* (claim 8); §3.3 and §6.2 describe
  learning rule probabilities from chord sequences under a prior and describe no use of annotated
  trees in training. What makes the training semi-supervised, as opposed to unsupervised, is not said
  in the pages as read; the hand-written rule inventory may be what is meant, and that is this
  reader's guess, marked as one.

## §6 — Terms the paper uses, in the paper's sense

| Term | The paper's sense |
|---|---|
| **constituent** | A stretch of the chord sequence that the analysis treats as one unit, standing *"in part-whole relationship"* with others (page 1). In the parser, a category with a start and an end index (page 4). |
| **category** | What a constituent is labeled with. In the Jazz grammar, a pair of a scale degree and a key (claim 25). |
| **rewrite rule / rewrite function** | A partial function from categories to sequences of categories and terminals (claim 12). One function stands for a whole family of ordinary rules. |
| **ACFG / PACFG** | Abstract Context-Free Grammar; its probabilistic version (claims 12, 14). The paper also prints *"APCFG"* once (page 6). |
| **PCFG** | Here, the same Jazz grammar with rule probabilities *not* tied across keys (claim 33) — the paper's comparison model, not a different grammar. |
| **preparation** | A rule of the form X → Y X: *"a preparation of X by Y"* (page 2). |
| **tonic / dominant / subdominant phrase** | A constituent whose category's scale degree is I / V / II respectively (page 1; II, not IV, is the paper's numeral for the subdominant phrase). |
| **μ(x, k)** | *"the modulation from k into the key of scale degree x"* (page 4). |
| **turnaround** | *"harmonic upbeats to the first chord of the piece at the end of the sheet"* (page 5). |
| **cyclic parsing** | Parsing under the assumption *"that constituents can have spans from the end of a piece back to the beginning"* (page 5). |
| **edge** | In the parser, *"A state s ∈ S together with a start index i and an end index j"*; the paper glosses edges as *"not yet completed constituents"* (page 4). Not a graph edge. |
| **tree accuracy** | *"the precision of correctly predicted spans of internal tree nodes"* (page 5). |
| **uniform prior / prior, posterior** | In Figure 4 and §6.2, as this side reads them: the model before training and after it. The paper does not define the two headings of Figure 4 in words. |

## §7 — Stated ABSENT: things a reader might supply from the subject that the pages do not say

Each line below is a negative over the eight page images as read by this side: *met in none of the
pages as read*, not *printed nowhere*.

- **Which tree is scored.** The parser computes a distribution over trees (claim 17). Whether the
  scored tree is the most probable one, a sample, or an expectation over trees is not stated. (The
  random baseline is *"randomly generated trees"*; how many, and from what distribution, is not stated
  either.)
- **A recall value.** The measurement is called a precision (claim 34). *This reader's reasoning, not
  the paper's:* the grammar has one-child rules (modulation, mode change, the substitutions,
  termination), so a predicted tree and a reference tree over the same chords need not have the same
  number of inner nodes, and precision and recall can then differ. The pages do not say how a
  one-child node, which shares its child's span, is counted.
- **The size of either model in parameters**; the ratio, *"approximately 12 times"*, is what is given.
  *This reader's arithmetic:* tying across twelve roots (claim 28) would by itself give a factor of
  twelve. The page says *approximately* and does not derive the ratio.
- **Any statement that the tied model finds the right key**, locally or for the piece (§4.5). §6.3
  suggests, in the paper's own words, that it may be alternating between relative keys where a
  listener would hear one (claim 38).
- **Any use of chord duration, metrical position, phrase position or form** (the A-part of Figure 1 is
  a fact about the example, not a feature of the model).
- **How slash chords, repeated chords or *no chord* marks in the lead sheets were handled**; how the
  suspended chord and the augmented triad terminate; the full list of termination rules (claim 27).
- **Any repertoire other than Jazz standards.** The general framework is said to be *"tailored to the
  needs of music"*; no grammar for another idiom is given or measured.
- **What the 37 unparsable pieces have in common**, and what the parser returns for a sequence it
  cannot parse.
- **A description of the 13 annotated pieces**: their titles, lengths, keys, whether they modulate,
  whether they end in turnarounds.

## §8 — The read-back and the sweep (steps 4 and 5 of entry 169 §3), written after the text above was finished

### §8.1 The read-back against the pages

Pages 3 to 6 were requested a second time (one request, four images, each present) and §2.3 to §2.8,
§4 and §5 were read against them. Pages 1, 2, 7 and 8 were not requested again; what rests on them
(§1, §2.1, §2.2, the opening of §2.3, the reference numbers) rests on the first request alone.

Read the same at both requests, and left as written: the four printed counts of §4.1 with their two
percentages; *"Less then 55%"*; the 13 pieces and the minibatch size; the four accuracy values of
§4.2 and *"under 10%"*; *"approximately 12 times"* and *"APCFG"*; *"up to 0.5%"*; the ten chord forms;
the conditions on each rewrite function of claim 26 (but IV; but I; I, II and V; 3, 6 and 9); the
termination example of claim 27; *"A ∈ dom(A)"* at claim 14; Figure 2's goal-item condition.

**Corrected at the read-back, before this file first landed:**
- **A claim firmer than the object.** §4.2 first said that the error ranges of the two trained models
  in Figure 4 *"overlap over most of their length"*. Looked at again, the overlap by eye is from about
  0.40 to about 0.47, roughly half of one range and less than half of the other. The sentence now
  gives those parts. A second clause written in its place, about where the top of the PCFG bar lies
  against the PACFG range, was removed again as finer than an eye reading of that plot supports.
- **A remark pointing at a section that did not yet exist** (claim 14 pointed to this §8.1 for an
  unsure glyph). It now says what was read, at how many requests.
- **Added:** the remark at claim 18 on Figure 2's goal-item condition; at §5, that the footnote-3 URL
  has two separators read as underscores, not one.
- **A declaration that was too wide.** §0 first said *"Nothing below is supplied from"* this reader's
  general knowledge. Two remarks in §7 (on precision and recall; on the factor of twelve) and the bold
  joining sentences of §2 are this reader's reasoning. §0 now says so, §2's head carries the rule for
  the bold sentences, and the two §7 remarks are marked.

### §8.2 The sweep for absolutes

One search of this file for *no, nothing, none, never, only, every, each, all, alone, whole, any,
neither, exactly, entire, complete, exhaustive*, each hit read at its line. Hits inside quotations
from the paper or from the record were left. Changed: *"no notes enter it"* (claim 24), *"Nothing
upstream of that … is in the model"* and *"No key is given to the model"* (§3) now carry *as
described*; *"No other published system is run"* (claim 33) became a negative over the pages as read;
*"The paper thereby says that no significance test … has been provided"* (claim 40) became *implies*,
with the negative scoped to the pages as read; *"measures the spans of the tree and nothing else it
hands down"* (§3) was narrowed to measurement against the reference analyses, with Figure 6 named;
*"The two baselines have no training"* (§4.2) became *not described as trained*; §4.5 gained its
scope line; §0's item (e) was split to say what each of its two count searches showed. Left after
reading: the negatives of §7, which its head scopes; *"No identity finding"*; *"no numbered table"*
(the six figures were counted at the images; a table would have been seen at the first read of each
page, and that is the extent of the look).

### §8.3 What this file rests on, and what it does not

It rests on one whole read of the eight page images and a second look at four of them, by a language
model. *(★ Made stale by §9.1 and left standing, #12: page 2 was requested once more at the
cross-check, so five pages were looked at twice.)* It does not rest on the first extract, on reference [24] or any other cited work, on the
software the paper points to, or on the dataset. **This reader opened none of those.** Two things in
it are residues a later reader can settle at the PDF: the turnaround percentage (§4.4; printed page
156, right column, the second paragraph of §6.1) and what the *"0.5%"* of printed page 157's left
column refers to, set beside Figure 5 above it.

## §9 — The cross-check against the first extract (step 7 of entry 169 §3), written after §0–§8 had landed

§0–§8 landed at 53,173 bytes (last content line 650) before the first extract was opened. The first
extract was then staged (88,188 bytes, modification time 1789212046566) and read whole, 1,149 lines,
two calls.

### §9.1 What was compared, and its bound

Compared: each quotation and each printed value the first extract carries from the paper, against
the page images as this side read them; the first extract's arithmetic; and what each file says the
paper does and does not state. Page 2 was requested once more for the cross-check (image present), so
the sites on pages 2 to 6 rest on two requests each; **the sites on page 1 rest on one request.**
**Not compared, because this side read none of their objects:** the first extract's record-facing
half — its verification table against `FRAMEWORK.md`, its Findings (1) to (6) so far as they speak
about this project's own documents, its cross-primary and reference-list checks, its findings (A) to
(E), its centrality verdict. This cross-check says nothing about those. **No claim is made that the
comparison is exhaustive**; it ran over what both files carry.

### §9.2 Where the two reads agree

Each printed value both files carry: 1173, 394, 40, 136 with 34.52 %, 357 with 90.61 %, the minibatch
size 8, the 13 pieces, *"under 10%"*, 15.35 %, 36.30 %, 39.43 %, 45.95 %, *"approximately 12 times"*,
*"up to 0.5%"*, the first 10 minibatches, the 33 %–50 % axis. The ten chord forms. Each rewrite
function with its domain, the termination example, the tying condition. Figure 2's items, with *"for
A ∈ S"* at the goal items. Eight pages, six figures, no table, thirty-two references.

**Both reads reached, without sight of the other:** the turnaround residue (221 of 394 is 56.09 %,
against the printed *"Less then 55%"*); that the two *"about"* gains are differences in percentage
points (3.13 and 9.65); *"APCFG"* printed once; that Figure 4's ranges are drawn and not printed as
numbers, that the two trained models' ranges appear by eye to overlap, and that the paper names
significance tests as future work; that whether the 13 pieces are among the 357 is not stated; that
the reference analyses are the authors' own; that the comparison is between two versions of one
grammar, beside two baselines that are themselves trees; that the input is a chord-symbol sequence with ninths and
elevenths dropped; that §6.3's diagnosis is the paper's conjecture, in hedged words. *(★ CORRECTED at
the user-ordered check, §10. FORMER WORDING, PRESERVED (#12): "that §6.3's diagnosis is hedged and
unmeasured" — the first extract says in terms that it is unmeasured; this file labels it CONJECTURE
and does not use that word of it.)*

The first extract carries arithmetic this file does not (221 of 357; the two gains as ratios; 168
categories, 24 start categories, 120 as an upper bound on terminals). This side redid each by hand
and each holds: 221 / 357 = 0.6190; 9.65 / 36.30 = 0.2658 and 3.13 / 36.30 = 0.0862; 7 × 24 = 168;
10 × 12 = 120.

### §9.3 Where the page goes against the first extract and no value, finding or verdict moves — corrected under the standing rule

Fourteen items, (a) to (n), each corrected or remarked at its site in the first extract, outside the
quotation, with the former wording preserved (#12), under the standing rule of handoff entry 198 §7.
Ten change words; four are remarks that change none.

- (a) §3.2 claim: the quotation had *"might considerably blow up the grammar"*; the page prints no
  *"might"* (page 3, two requests).
- (b) §4 claim: *"denoted by Roman numerals."* → *"denoted by roman numerals from I to VII."* (page 4).
- (c) §5 claim: *"would not be able to parse"* → *"would not able to parse"*, the page's own slip
  (page 5).
- (d) the same quotation closed on a full stop after *"back to the beginning"*; the page runs on with
  *", see Figure 3."*
- (e) §6.1 claim: *"1173 chord sequences that are electronically-encoded"*; the page prints no *"that
  are"* (page 5).
- (f) §6.1 claim: *"the cyclic parsing approach. Less then"* → *"the cyclic parsing approach described
  above. Less then"* (page 5).
- (g) §6.2 claim, remark: the page prints no full stop between *"15.35%"* and *"Under a uniform
  prior"* (page 6).
- (h) §6.3 claim (the CONJECTURE bullet): the quotation ended *"as a III in minor."*; the page reads
  *"as a III in the relative minor key that is then prepared by the VII in minor."* (page 6). **The same
  shortened words inside Finding (4) are at §9.4.**
- (i) the derivation beside it: subscripts written *α*; this side read an italic lower-case *a* at
  two requests, the key in the sentence before being A minor. Two language-model reads of one glyph;
  corrected to *a* with the former form kept.
- (j) §1 claim: *"for the training and the evaluation"* → *"or"* (page 2, two requests).
- (k) §1 claim, **the two that change what the paper is reported to say**: *"monophonic Schenkerian
  data [21]"* → *"monophonic melodic data [21]"*; *"restricted to subsequences of pieces that did not
  end in turnarounds [4]"* → *"did not change key [4]"* (page 2, two requests). A search of the first
  extract for both former phrases met them at that bullet alone, so no value, Finding or verdict of
  that file was found to rest on either.
- (l) remark at the head of the claims section: bold inside quotations from the paper is the first
  extract's emphasis.
- (m) remark: the sentence about the Julia package is §1's running text; footnote 1 is the URL alone.
- (n) remark: the sentence about 95 % confidence intervals is §6.2's running text; Figure 4's caption
  is *"Tree accuracy plot"*.

### §9.4 ★ Where the page goes against the first extract inside a Finding — three sites, NOT corrected, with the user

Under the last sentence of handoff entry 200 §1 item 2, a word the page does not print that stands
inside or beside a Finding goes to the user.

1. **Finding (4), its counterweight paragraph.** It quotes the paper as saying the model is
   *"alternating between relative keys"* and *"interpreting a I in major as a III in minor"*. The page
   (printed page 157, right column, top) reads *"the model may be using them to alternate between
   relative keys"* and *"The model may be interpreting a I in major as a III in the relative minor key
   that is then prepared by the VII in minor."* Neither quoted string is on the page in that form. The
   sense of the Finding is unchanged by the page's words.
2. **Finding (8), third bullet:** *"**no tree is ever an input to training**"* and *"the graded labels
   are unseen by construction"*. The paper's §1 (printed page 153, left column) says *"We train the
   model in a semi-supervised fashion on a dataset of Jazz-standards"*. §3.3 and §6.2 describe training
   on chord sequences and describe no tree entering it; the pages as read do not say what the
   supervised part is. A search of the first extract for *supervis* met the word *"unsupervised"* in
   the future-work quotation and nothing else, so that file does not carry the paper's word. **As this
   side reads the pages, the bullet is firmer than the paper**: what the pages support is that no use
   of annotated trees in training is described, and that the paper calls its training semi-supervised
   without saying why. The Finding's conclusion (*"intermediate … not established as held-out"*) would
   stand on the narrower wording; its *"stronger than a fitted-and-self-measured number"* half is the
   part that leans on the absolute.
3. **Finding (9):** *"no second annotator"*. The page says *"13 pieces hand-annotated by the authors"*,
   and the paper has three authors; how many of them annotated each piece is not stated. What the page supports
   is that no second annotating group and no agreement value is reported. *(★ CORRECTED at the
   user-ordered check, §10: that sentence first stood in quotation marks, which made this side's
   proposed wording look like a quotation of the page.)*

**The user can settle 1 and 2 at the PDF** at the two places named. Both reads are a language model's
reads of page images.

*(★ This section's heading and its "NOT corrected, with the user" were made stale by the ruling
recorded at §9.7 and are left standing, #12.)*

### §9.5 What the first extract shows about this one

- **Nothing in the first extract went against a value or a quotation of this file** at the places the
  comparison reached.
- This file's claim 27 says the termination rules are not listed and sends the reader to [20] *"a
  jazz theory textbook, as the reference list has it"*; the first extract names it (Levine, *The jazz
  theory book*, 1995), which agrees with page 7 as this side read it.
- The first extract records that `DIAT-SUBST`'s domain is printed after the page break; this file has
  the domain (claim 26) without that remark.
- This file's §4.2 gives eye readings of Figure 4's ranges as numbers; the first extract declines to
  use the plot beyond *"appear to overlap"*. Neither uses it as a result.
- This file carries three things the first does not: the paper's word *"semi-supervised"* (§5; §9.4
  item 2); that Figure 5's swings by eye exceed the text's *"0.5%"* (§4.3); that the abstract's *"key
  finding on the fly"* and *modulations* have no measurement in the pages (§4.5). The first extract's
  coupling facts cite *"key finding on the fly"* for the key not being an input, and its paragraph on
  the evaluation axis says the measurement *"grades the hierarchy, not the reading"*; this side met
  no sentence in it saying that the key finding itself is unmeasured.

### §9.6 The act under the standing rule

The first extract was edited on its staged copy: a banner remark recording the rule and pointing
here, and a remark at each of the sites of §9.3. The paper was the ground for each (pages 2 to 6 at
two requests). No printed value, derived number, Finding or verdict of that file was changed.
Findings (4), (8) and (9) were not touched. Landing values are in handoff entry 203.

*(★ "Findings (4), (8) and (9) were not touched" was made stale by §9.7 and is left standing, #12.)*

### §9.7 ★ The ruling on §9.4's three sites, and the act under it

**The ruling, 2026-09-19, the user's words: "I agree with recommendation A."** It came in reply to the
surface itself; the separate choice question had been announced and had not yet been put. The surface
put two alternatives — A, correct the three sites at their places with the former wording preserved,
record the ruling in the first extract's banner, and add a remark under this file's §9.4; B, leave
the first extract as it is and let §9.4 carry the disagreement — and recommended A, saying that the
choice had in effect collapsed, the same kind of item having been ruled the same way on rows 46, 15,
17, 35, 58 and 40 (as handoff entries 186, 188, 198, 200, 201 and 202 record). **Whether the user
looked at the two pages before ruling is not known to this side.**

**The act, in the first extract:** Finding (4)'s two quotations now read *"using them to alternate
between relative keys"* and *"interpreting a I in major as a III in the relative minor key that is
then prepared by the VII in minor"*, with *possibly* set outside the first to carry the page's *"may
be"*. Finding (8)'s third bullet now says that, as the pages describe the training, the graded labels
are not an input to it and the pages describe no tree entering training, and it carries the paper's
sentence with *"semi-supervised"*; in its fourth bullet *"were never fitted"* reads *"are not
described as fitted"*, with *"if that description is whole"* added. Finding (9) reads *"no second
annotating group and no agreement figure reported"*. Each carries a remark with the former wording
and the ruling; the banner records the ruling, and its sentence that three sites stand with the user
is marked stale and left standing, as is the matching sentence in the remark at that file's §6.3
claim. **No printed value, derived number or verdict was touched; Finding (8)'s conclusion stands.
The paper was not opened again for the act.** One sentence of Finding (8) was left as it stands
although it leans the same way: its closing *"and they are not the fitted-and-self-measured class
either"*. A reader now meets it under the narrowed third and fourth bullets.

**The rule for a later row is unchanged: handoff entry 200 §1 item 2's last sentence stands.**

## §10 — ★ The user-ordered check after landing, written in the act that ran it

The user ordered: *"Fact check what you have written, fix if necessary."* This file was re-read whole
at its landed copy (62,752 bytes, 781 lines, two calls) against the page images still held in the
session, the records read at boot, the first extract as read, and the tool results. Its arithmetic
was redone by hand and holds. No page was requested again. **It did not come back empty.** Corrected
at their sites, former wording preserved:

- **A range wider than the look, in §0** — *"D-406 to D-414"*, where the decisions register's index as
  read carries D-406, D-408, D-410, D-411 and D-414 and no D-407, D-409, D-412 or D-413 (checked by a
  search of the staged index), and a parenthesis that fitted one of the entries named and not each.
  This is the same shape the check of row 40's second extract found in that file's §0.
- **Two loose descriptions in §0** — the bibliography's line 78 called *"a different paper by other
  first authors"*, where Harasim is its second author; and reference [4] called an article *"by the
  same two authors"* beside two file names of which one carries a single author.
- **A gloss standing as the page's, at claim 22** — that the models *"were compared"* under a uniform
  prior; the page uses the phrase of the untrained state.
- **A wrong locator at §4.2's heading** — *page 5*, where the four printed values are on page 6.
- **A statement about this file that was not true of it, at §9.2** — that both reads call §6.3's
  diagnosis *"unmeasured"*; this file does not use that word of it.
- **A proposed wording set in quotation marks, at §9.4 item 3**, where it could be taken for the
  page's.
- Narrowed without a former-wording remark, the change being an added qualifier alone: claim 31's
  reading of Figure 3 and §6's gloss of *prior* and *posterior* now say they are this side's reading.
- Marked stale and left standing: §8.3's count of pages looked at twice; §9.4's heading; §9.6's last
  sentence but one.

**Confirmed and not struck:** each quotation of §2 against the page images as held (pages 2 to 6 at
two requests, pages 1, 7 and 8 at one); the values of §4.1 and §4.2; the arithmetic of §4.4 and §9.2;
the searches §0 names, against the tool results; the first extract's name, size and modification time;
§9.3's count of fourteen as ten and four; the three sites of §9.4 against the first extract's lines.

**The remarks this side wrote into the first extract** (the banner and the sites of §9.3) were read
again in the staged copy's search results; none was struck. One of them, at that file's §6.3 claim,
was made stale by the ruling and carries a remark.

**Degradation.** The check found eight places of the named shapes in writing that had already landed
(the six bullets above that carry a former wording, the first two of them holding two defects each).
Handoff entry 203 §5 reported four before it. **This side found the eight only because the user
ordered the check.**

**What the check did NOT do:** request any page of the paper again; re-read the first extract whole
after the acts; open any record not already read. Over-long lines (this file's lines 103, 405, 413,
471, 533 and 684 as first landed) were left. **Nothing here says a further pass would come back
empty.**
