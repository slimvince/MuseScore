# Task B — the candidacy-upgrade derivation, one verdict per register row

> **STATUS: DERIVED 2026-08-31. NO PAPER WAS READ FOR IT.** Written by the session opened on
> `cowork_reading_pass_remedial_commission_2026_08_31.md`, executing its §3 first instruction — the
> derivation is *"a slice of its own and should be landed before any reading begins, so the
> population is on disk before it is worked."* **It takes no decision, derives no specification
> statement, amends no document, opens no code and writes no register row.** The verdicts below
> decide only what is READ next; every one of them is challengeable at its own row.

## The criterion, quoted rather than paraphrased

Commission §3: a held paper is a candidacy upgrade **"when its METHOD — not merely a figure it
supplies — is a live candidate for a decision inside a ratified charter: that is, when a detail
specification of L1, L2 or L3 could adopt, adapt, or have to argue against the way that paper
actually does the thing the charter owns. A paper that supplies only a measured figure, a corpus, an
evaluation convention or a representation is not an upgrade."** And: **"A paper whose own text does
not settle whether its method is a candidate is INCLUDED — the default on doubt is to read."**

**Two consequences of the criterion's own words, applied throughout and stated here so they are not
re-argued per row.** *(i)* **"Have to argue against" admits a rival.** A method a chosen design
point excludes is a candidate for that decision, because the exclusion is what a detail
specification must carry. *(ii)* **A domain bound is a caveat, not a disqualifier.** DP-B's own
recorded ground is an audio study (`FRAMEWORK.md` §9, DP-B; findings surface V2), so an audio method
is not excluded by being audio; what it is admitted for is its method, and its domain travels with
it.

## What was read to derive it

`docs/research_papers/BIBLIOGRAPHY.md` **whole** — it is the derivation's population and the source
of every row's title, venue and held-or-not state. `FRAMEWORK.md` **§5** (the L0 input contract, the
L1, L2 and L3 charters, the second axis, the three not-a-layer items, the boundary contracts), **§9**
(§9.0 and DP-A…DP-Q) and **§11** (R-1…R-10). `cowork_reading_pass_findings_2026_08_31.md` §2, §3 and
§5, for what the pass already routed. The commission whole.

**The bound on every verdict below, declared once (DT-26).** A verdict is taken on the register
row's own title, venue and subject, together with what this project's own ratified record already
establishes about that source — `FRAMEWORK.md`'s citations of it, the findings surface's
characterisation of it, and the commission's own starting hypothesis. **No paper was opened for
this derivation.** That is exactly why the criterion's default falls on INCLUDE: where the register
row and the record together do not settle that a source's method is outside every charter, the row
is admitted and the question is answered by reading it, not here.

## The starting hypothesis, tested per paper

The commission offers a list of candidates *"not to be adopted without the derivation"*. **Every
item of it is a register row, and every item is admitted below** — the segmental CRF model (Masada & Bunescu), the
semi-Markov formalism (Sarawagi & Cohen), the neural semi-CRF system (Harana), the probabilistic
graphical model (Raphael & Stoddard), the unified probabilistic polyphonic model (Temperley 2009),
the concurrent chord-and-key estimation paper (Rocher et al.), the chordal-analysis paper (Pardo &
Birmingham), the generalized parsing framework (Harasim et al.), the multi-task lineage, the
figured-bass annotation work (Ju et al. 2020) and the duration-and-language-model chord recogniser
(Korzeniowski & Widmer). **Each is admitted on the criterion at its own row, not on the
hypothesis** — the hypothesis is confirmed, not relied on. It is also **not exhaustive**: the
derivation admits sources it does not name. One of its items, *the multi-task lineage*, is a class
rather than a single row, and it is admitted row by row in its own section below.

---

## The verdicts — core joint-model and factor-form sources

| # | Source, as the register names it | Held | Verdict | Reason |
|---|---|---|---|---|
| 1 | Raphael & Stoddard, ISMIR 2003, harmonic analysis with probabilistic graphical models | ✓ | **ADMITTED** | A method that decides tonality and chord together over a score. Directly a candidate for L2's one entangled decision (§5, L2). The commission's hypothesis names it. |
| 2 | Raphael & Stoddard, CMJ 28(3) 2004, functional harmonic analysis using probabilistic models | — | **ADMITTED** | The journal account of the same method; the fuller statement of what row 1 does. **Paywalled and not held** — carried as an admitted row that cannot be read from here. |
| 3 | Ni, McVicar, Santos-Rodríguez & De Bie, TASLP 2012, an end-to-end machine learning system for harmonic analysis | ✓ | **ADMITTED** | An end-to-end system deciding chord and key; a whole-chain candidate to compare L2's charter against. Audio domain, carried as a caveat under (ii). |
| 4 | Pardo & Birmingham, CMJ 26(2) 2002, algorithms for chordal analysis | ✓ | **ADMITTED** | It supplies L1's partition-point construction — `population.md` V8 records that the framework's L1 charter uses that paper's own term — and its tie-breaking residual is the measurement DP-C carries. Its METHOD is L1's and L2's, not only its figures. |
| 5 | Temperley, ICMAI 2002, a Bayesian approach to key-finding | ✓ | **ADMITTED** | A tonality-deciding method, and the source of V3's spelling measurement. Admitted for the method, not the figure. |
| 6 | Temperley, Music Perception 17(1) 1999, "What's Key for Key?" | — | **ADMITTED** | A key-finding model. **Paywalled and not held.** |
| 7 | Temperley & Sleator, CMJ 23(1) 1999, modeling meter and harmony: a preference-rule approach | ✓ | **ADMITTED** | Decides meter and harmony together by preference rules — a rival shape for the L1/L2 division, and for how metric strength enters (§5, L1). |
| 8 | Temperley, JNMR 38(1) 2009, a unified probabilistic model for polyphonic music analysis | ✓ | **ADMITTED** | The unified probabilistic model the hypothesis names; it is also V4's primary, but it is admitted for its method. |
| 9 | Temperley 2001, Temperley 2007, Krumhansl 1990 (books) | — | **ADMITTED, AND UNREADABLE FROM HERE** | Krumhansl 1990 is the tonality-profiles primary. A profile is a factor form an L2 detail specification could rest on, so the criterion admits it. **This raises no new STOP:** the gap is already declared as `FRAMEWORK.md` **R-8** and as population row 20, FLAGGED-UNFETCHABLE. Recorded, not re-raised. |
| 10 | Masada & Bunescu, TISMIR 2(1) 2019, chord recognition in symbolic music: a segmental CRF model | ✓ | **ADMITTED** | The segmental CRF; the machinery of DP-C's chosen answer and the source of V5 and of DP-C's segmental gains. Symbolic, on our repertoire's kind of input. |
| 11 | Sarawagi & Cohen, NIPS 2004, semi-Markov conditional random fields | ✓ | **ADMITTED** | The formalism under DP-C's chosen option, including the linear-versus-exponential result the design point carries. An L2 detail specification adopts or adapts it. |
| 12 | Lafferty, McCallum & Pereira, ICML 2001, conditional random fields | ✓ | **ADMITTED** | The base formalism the two rows above extend; it decides how L2's score is formed and normalised, which §5 leaves expressly to the detail specification. |
| 13 | Ng & Jordan, NIPS 2001, discriminative versus generative classifiers | ✓ | **ADMITTED, ON THE DOUBT DEFAULT** | It bears on which fitting regime L2's score takes (DP-P), and whether that is a *method for a charter decision* or a general result is not settled by the row. Included by the criterion's own default. |
| 14 | Sha & Pereira, NAACL 2003, shallow parsing with conditional random fields | ✓ | **ADMITTED, ON THE DOUBT DEFAULT** | A segmentation-and-labelling method in another domain; whether it carries anything DP-C's chosen option does not already is unsettled here. |
| 15 | Och, ACL 2003, minimum error rate training | ✓ | **ADMITTED** | Its METHOD — fitting combination weights to the metric wanted — is the live candidate for DP-P, which §9 names as L2 detail. V13 is its figure; the admission is for the method. |
| 16 | Sutton & McCallum 2006, an introduction to conditional random fields | ✓ | **ADMITTED, ON THE DOUBT DEFAULT** | A tutorial rather than a primary method. Admitted because the record does not settle whether it carries the inference and fitting detail the three CRF rows above leave out. |
| 17 | Burgoyne, Pugin, Kereliuk & Fujinaga, ISMIR 2007, a cross-validated study of modelling strategies for chord recognition | ✓ | **ADMITTED** | Its subject is the comparison of model families for the chord decision — the shape of the choice an L2 detail specification makes. |
| 18 | Sheh & Ellis, ISMIR 2003, chord segmentation and recognition using EM-trained HMMs | ✓ | **ADMITTED** | DP-C's 68.8-against-23.3 primary, and its method is the boundaries-given-versus-found design that measurement is about. |
| 19 | Yang, Cwitkowitz & Duan, ISMIR 2023, harmonic analysis with neural semi-CRF (Harana) | ✓ | **ADMITTED** | The neural semi-CRF; DP-C's largest-ablation-contributor evidence, and a current candidate architecture for L2. |
| 20 | Korzeniowski & Widmer, ISMIR 2018, combining duration and harmonic language models | ✓ | **ADMITTED** | A segment-duration model beside a chord language model — directly a candidate for how L2 scores segment length, which the charter leaves to detail. |
| 21 | Harasim, Rohrmeier & O'Donnell, ISMIR 2018, a generalized parsing framework for generative models of harmonic syntax | ✓ | **ADMITTED** | The parsing framework the hypothesis names; DP-O is open and this is a method for the thing it is open about. |
| 22 | Rohrmeier, JMM 5(1) 2011, towards a generative syntax of tonal harmony | ✓ | **ADMITTED** | The grammar DP-O's *for* side rests on. **Paywalled, and HELD since 2026-09-12** — the user placed `docs/research_papers/Rohrmeier2011.pdf`, established at its page 1 as this work on title, author, journal, volume, issue, year and DOI, **and renamed it later that day to `rohrmeier_2011_jmm_generative_syntax_tonal_harmony.pdf`** (confirmed at the folder's listing). *(Former wording, preserved #12: "**Paywalled and not held.**")* |
| 23 | Rohrmeier, DCRR-004 2006, towards modelling harmonic movement | ✓ | **ADMITTED, ON THE DOUBT DEFAULT** | Whether it carries a method or the theory behind row 22 is not settled by the row. |
| 24 | Rohrmeier & Cross, ICMPC 2008, statistical properties of tonal harmony in Bach's chorales | — | **NOT ADMITTED** | Corpus statistics, not a method: it supplies distributions, which is exactly the *"measured figure"* class the criterion excludes. Routes to data design. **Not held; no open copy recorded.** |
| 25 | Tsushima, Nakamura, Itoyama & Yoshii, arXiv:1708.02255, generative statistical models with self-emergent grammar of chord sequences | ✓ | **ADMITTED** | A method that learns the chord-sequence structure rather than being given it — a candidate for the chord-transition question inside L2. |
| 26 | Noland & Sandler, ISMIR 2006, key estimation using a hidden Markov model | ✓ | **ADMITTED** | A tonality-deciding method with an explicit transition structure; DP-E's *where may the tonality change* is that structure's question. |
| 27 | Rocher, Robine, Hanna & Oudre, ISMIR 2010, concurrent estimation of chords and keys | ✓ | **ADMITTED** | The primary of DP-B **and** of the soft-versus-hard coupling the L2 charter fixes; the hypothesis names it, and V2 and V7 both come from it. Admitted for the coupling design, not the figures. |
| 28 | Catteau, Martens & Leman, GfKl 2006, a probabilistic framework for tonal key and chord recognition | ✓ | **ADMITTED** | A joint key-and-chord probabilistic framework — the same decision L2 owns, done another way. |
| 29 | Chew, ICMAI 2002, the spiral array: determining key boundaries | ✓ | **ADMITTED** | A method that places tonality boundaries — DP-E's question — in a continuous space rather than over discrete labels. |
| 30 | Feisthauer, Bigo, Giraud & Levé, SMC 2020, estimating keys and modulations | ✓ | **ADMITTED** | A modulation-deciding method on symbolic classical music, our own repertoire and input kind. |
| 31 | Teodoru & Raphael, ISMIR 2007, pitch spelling with conditionally independent voices | ✓ | **NOT ADMITTED** | Its method answers a question no charter owns: spelling is **given** at L0 and DP-F settles that it is not a layer for notated input. Routes to the L0 boundary-condition literature. |
| 32 | Meredith, ESCOM 2003, pitch spelling algorithms (ps13) | ✓ | **NOT ADMITTED** | Same ground as row 31. |
| 33 | Foscarin, Audebert & Fournier-S'niehotta, ISMIR 2021, PKSpell | ✓ | **NOT ADMITTED** | Same ground as row 31. |
| 34 | Illescas, Rizo & Iñesta, ICMC 2007, harmonic, melodic and functional automatic analysis | ✓ | **ADMITTED** | A whole analysis method covering the harmonic and functional questions L2 and L3 own. |
| 35 | Ju, Condit-Schultz, Arthur & Fujinaga, ISMIR-LBD 2017, non-chord tone identification using deep neural networks | ✓ | **ADMITTED** | **The excluded rival of DP-D**, and V11's primary. The criterion admits a method a design point must argue against; DP-D's exclusion ground is about this method's shape. |
| 36 | Ju, Margot, McKay, Dahn & Fujinaga, ISMIR 2020, automatic figured bass annotation (BCFB) | ✓ | **ADMITTED** | **L3 publishes the figured bass and the read set contains no producer for it** (findings surface §3.2). The hypothesis names this row for exactly that reason. |
| 37 | Bigo, Feisthauer, Giraud & Levé, ISMIR 2018, relevance of musical features for cadence detection | ✓ | **ADMITTED** | V6's primary, and the method behind DP-I's split: which cues are computable before the harmony is the L1 charter's own content. |
| 38 | Karystinaios & Widmer, ISMIR 2022, cadence detection using graph neural networks | ✓ | **ADMITTED** | The second half of V6, and a different method for the same L1/L3 split. |
| 39 | Sears, Pearce, Caplin & McAdams, JNMR 47(1) 2018, simulating melodic and harmonic expectations for tonal cadences | ✓ | **ADMITTED, ON THE DOUBT DEFAULT** | A computational model of cadential arrival; whether its method bears on L1's cues or only on perception is not settled by the row. |
| 40 | de Clercq, EMR 10(3) 2015, a model for scale-degree reinterpretation | ✓ | **ADMITTED** | A model of how a degree is re-read under a changed tonality — DP-E's and L3's territory, and adjacent to the tonicization-versus-modulation line the ruled conventions already carry. |
| 41 | Hadjeres, Pachet & Nielsen, ICML 2017, DeepBach | ✓ | **NOT ADMITTED** | A generation method. No charter owns generation; L1–L3 decide an analysis of a given score. Routes to nothing in this frame. |
| 42 | Liang, Gotham, Johnson & Shotton, ISMIR 2017, BachBot | ✓ | **NOT ADMITTED** | Same ground as row 41. |
| 43 | Mauch & Dixon, ISMIR 2010, approximate note transcription for difficult chords | ✓ | **NOT ADMITTED** | Its method recovers notes from audio — the L0 input contract supplies notes by construction. Routes to the L0 boundary-condition literature. |
| 44 | Mauch & Dixon, TASLP 18(6) 2010, simultaneous estimation of chords and musical context | — | **ADMITTED** | Simultaneous estimation of chord together with its context is L2's entangled decision in another domain. **Not held** (the register records the author copy as image-only). |

## The verdicts — the neural and multi-task lineage

The framework reads this lineage as **evidence about DP-A**. The commission asks whether the same
papers are also **candidate scoring architectures for L2**, and the criterion answers yes for each:
every one of them decides the same questions L2 decides, and the machinery each adds to undo the
separation (§9, DP-A) is machinery an L2 detail specification could adopt or must argue against.

| # | Source | Held | Verdict | Reason |
|---|---|---|---|---|
| 45 | Micchi, Gotham & Giraud, TISMIR 3(1) 2020, "Not All Roads Lead to Rome" | ✓ | **ADMITTED** | The lineage's baseline architecture and the source of DP-A's self-contradiction quotation. |
| 46 | Chen & Su, ISMIR 2018, functional harmony recognition (BPS-FH) | ✓ | **ADMITTED** | Decides degree, quality and inversion over a score. |
| 47 | Chen & Su, ISMIR 2019 Harmony Transformer; TISMIR 2021 "Attend to Chords" | ✓ | **ADMITTED** | The register carries two papers in one row. The Harmony Transformer decides **segmentation and labelling together** — DP-C's own question — and is BACHI's named comparable in the findings surface. |
| 48 | Nápoles López, Gotham & Fujinaga, ISMIR 2021, AugmentedNet | ✓ | **ADMITTED** | Carries the re-fusion of degree, quality and root into one joint label — DP-A's *adds machinery to undo the separation*. |
| 49 | ChordGNN, ISMIR 2023 | ✓ | **ADMITTED** | V8's onset-level representation, and the learned coherence pass of DP-A's .462→.491. |
| 50 | Sailor, ISMIR 2024, RNBERT | ✓ | **ADMITTED** | Conditioning the degree decision on the tonality — DP-B's and DP-A's shared question, with the teacher-forcing bound the framework already carries. |
| 51 | Wu, Nakamura & Yoshii, APSIPA 2020 | ✓ | **ADMITTED, ON THE DOUBT DEFAULT** | The register names no subject beyond the venue; nothing in the record settles what its method does. The default is to read. |
| 52 | AnalysisGNN, arXiv:2509.06654, 2025 | ✓ | **ADMITTED** | V1's and V9's primary, and the logit-fusion architecture DP-A cites. Admitted for the architecture. |

## The verdicts — ground-truth and annotation sources

**This whole section is where the criterion's exclusion bites**, and it is stated once rather than
per row: a corpus, an annotation standard and an agreement measurement are the *corpus* and
*evaluation convention* classes the criterion names, and they are **already routed** — to measurement
design by the findings surface §5, and to `OPEN_ITEMS.md` OI-179 and principle #21 by the record.
**Not admitted is not "not useful": it is "not read for this reason."**

| # | Source | Held | Verdict | Reason |
|---|---|---|---|---|
| 53 | Devaney, Arthur, Condit-Schultz & Nisula, ISMIR 2015, TAVERN | ✓ | **NOT ADMITTED** | A corpus. Already carried on the ceiling question at principle #21 / D-474. |
| 54 | Neuwirth, Harasim, Moss & Rohrmeier, 2018, the Annotated Beethoven Corpus | ✓ | **NOT ADMITTED** | A corpus. |
| 55 | Hentschel, Neuwirth & Rohrmeier, TISMIR 2021, the Annotated Mozart Sonatas | ✓ | **NOT ADMITTED** | A corpus. |
| 56 | Gotham, Micchi, Nápoles López & Sailor, TISMIR 2023, "When in Rome" | ✓ | **NOT ADMITTED** | A meta-corpus — our own ground truth. Routes to measurement and data design. |
| 57 | Condit-Schultz, Ju & Fujinaga, ISMIR 2018, a flexible approach to automated harmonic analysis | ✓ | **ADMITTED** | **The exception in this section.** Its subject is an analysis METHOD, not a corpus, whatever section of the register it sits in. |
| 58 | Ju et al., ISMIR 2019, an interactive workflow for generating chord labels | ✓ | **ADMITTED, ON THE DOUBT DEFAULT** | A workflow for producing labels may or may not carry a labelling method; the row does not settle it. |
| 59 | Hentschel, Karystinaios, Widmer & Neuwirth, 2026, Dilemmadata | ✓ | **NOT ADMITTED** | A dataset, and one already named at principle #21 as a computable-agreement candidate. Routes to measurement design. |
| 60 | de Clercq & Temperley, Popular Music 30(1) 2011, a corpus analysis of rock harmony | ✓ | **NOT ADMITTED** | A corpus analysis; its agreement figures are already recorded, off-domain, with D-474. |
| 61 | Koops et al., Utrecht TR 2017 / JNMR 2019, annotator subjectivity | ✓ | **NOT ADMITTED** | An agreement measurement — V12's primary. Evaluation convention, already routed and already read at the object for V12. |
| 62 | Humphrey & Bello, ISMIR 2015, four timely insights on automatic chord estimation | ✓ (**wrong paper in the file**) | **NOT ADMITTED** | Insights and evaluation, not a method; and it is **population row 21**, already read this pass. The register's ✓ is false at the object — that is R-9, and it stands. |
| 63 | Sears, Verbeten & Percival, JEP:HPP 2023, "Does Order Matter?" | ✓ | **NOT ADMITTED** | A perception experiment. No charter decision turns on its method. |
| 64 | BCMH corpus (PeARL lab) | ✓ | **NOT ADMITTED** | A corpus, and one whose establishment status is already ruled at D-475. |

## The verdicts — the grammar branch, added on the user's ruling of 2026-09-12

**These three rows were RULED IN by the user on 2026-09-12** — not derived under the criterion by a
session — after the session that read row 25 established that all three are named in read rows'
reference lists (rows 25, 46, 57 and 58) and in no row of the register. The register rows are the new
section of `docs/research_papers/BIBLIOGRAPHY.md` of the same date. **The verdict is the user's; the
reason column states what the ruling admits them FOR, read off page 1 and the citing rows, so the reads
know what they are told to do.** All three sit in the grammar branch — group 6 of the proposed order —
against which DP-O stays open.

| # | Source, as the register names it | Held | Verdict | Reason |
|---|---|---|---|---|
| 65 | Granroth-Wilding & Steedman, "Statistical Parsing for Harmonic Analysis of Jazz Chord Sequences" (ICMC 2012 by row 25's citation; page 1 prints no venue or year) | ✓ (`granrothwilding_steedman_2012_icmc_statistical_parsing_jazz_chord_sequences.pdf`) | **ADMITTED — RULED IN BY THE USER** | A grammar-based statistical parser of jazz chord sequences measured against a Markov baseline on the same corpus, by page 1's abstract — the tree-against-sequence comparison DP-O's *for* half (row 21) turned out not to contain, and on chord symbols like rows 21 and 25. A method for the thing DP-O is open about. |
| 66 | Granroth-Wilding, PhD thesis, University of Edinburgh 2013, *Harmonic Analysis of Music Using Combinatory Categorial Grammar* | ✓ (`granrothwilding_2013_phd_edinburgh_harmonic_analysis_ccg.pdf`) | **ADMITTED — RULED IN BY THE USER** | The thesis behind row 65's method; cited by rows 46 and 58. 183 pages; the whole-read cost is to be judged out loud before it is opened, as the standing rule requires. |
| 67 | Jacoby, Tishby & Tymoczko, JNMR 2015, an information theoretic approach to chord categorization and functional harmony | ✓ (`jacoby_tishby_tymoczko_2015_jnmr_information_theoretic_chord_categorization.pdf`, PAYWALL) | **ADMITTED — RULED IN BY THE USER** | The paper row 25's authors cite, with Rohrmeier & Cross 2008 (row 24), for chord categories resembling harmonic functions being obtained by unsupervised learning — the prior result behind DP-O's *against* half's third claim, and a candidate for the chord-category question inside L2's chord-transition territory. Cited by rows 25, 46 and 57. |

---

## The count, and what it means

**Sixty-seven register rows carry a verdict; none is left unclassified.** *(★ RE-DERIVED 2026-09-12 on
the user's ruling adding rows 65–67. **FORMER WORDING, PRESERVED (#12): "Sixty-four register rows carry a
verdict; none is left unclassified." / "ADMITTED — forty-seven: rows 1–23, 25–30, 34–40, 44–52, 57, 58."**
The doubt-default list, the NOT ADMITTED list and the unreadable list are untouched.)*

- **ADMITTED — fifty:** rows 1–23, 25–30, 34–40, 44–52, 57, 58, 65–67.
- **NOT ADMITTED — seventeen:** rows 24, 31–33, 41–43, 53–56, 59–64, each with the class it routes to.
- Of the admitted, **seven** stand on the doubt default: rows 13, 14, 16, 23, 39, 51, 58.
- Of the admitted, **four cannot be read from here**: rows 2, 6 and 9 are paywalled or books,
  and row 44's only recorded copy is image-only. Row 9's gap is `FRAMEWORK.md` **R-8** and is not
  re-raised. *(★ CORRECTED 2026-09-12. **FORMER WORDING, PRESERVED (#12): "Of the admitted, five cannot
  be read from here: rows 2, 6, 9 and 22 are paywalled or books, and row 44's only recorded copy is
  image-only."** Row 22 is now held — see its row above. **Row 22 remains PAYWALLED**; what changed is
  that a copy is on disk, and being paywalled was never by itself a bar to reading, rows 28 and 29 being
  PAYWALL-tier, held and already read in this pass.)*

**The derivation is complete in both directions**: every register row appears exactly once, and no
admitted row lacks a reason.

**That this set is large is the finding, not a defect of the criterion.** `population.md` §4 records
**none**, and the eighty-fifth handoff entry states the gap in terms — *"the held fifty-eight
contain obvious live algorithm candidates for the detail specifications."* Coverage follows load,
and the load of L2's entangled decision is carried by most of this register.

## Proposed reading order — stated, not ruled

The commission orders reading *"in priority order by the weight the charter puts on the decision it
bears on — L2's entangled decision first."* Applied:

1. **The joint tonality-and-chord decision** — rows 27, 28, 1, 2, 8, 3, 44, 26, 29, 30, 5.
2. **Segmentation decided with the labelling** — rows 10, 11, 19, 20, 18, 4, 47.
3. **The scoring architecture and its fitting** — rows 45, 48, 49, 50, 52, 46, 51, 15, 12, 13, 14, 16, 17.
4. **What L2 must publish that nothing in the read set produces** — rows 35 (the chord-tone rival), 36 (figured bass), 57, 58.
5. **L1's cues and L3's types** — rows 37, 38, 39, 7, 40.
6. **The grammar branch, against which DP-O stays open** — rows 21, 22, 23, 25, 34, **and rows 65, 66, 67 as ruled in on 2026-09-12** *(former wording, preserved #12: "rows 21, 22, 23, 25, 34")*.
7. **Unreadable from here** — rows 6, 9 (already R-8), and 2, 44 if no open copy is found. *(★ CORRECTED 2026-09-12; **former wording, preserved (#12): "rows 6, 9 (already R-8), and 2, 22, 44 if no open copy is found."** Row 22 is held as of that date. Group 6 above already names row 22 and is unchanged.)*

**Each is extracted in the original commission's §4 form, coupling facts mandatory**, and centrality
is decided per paper as that commission's own rule requires. **No reading is begun in this file.**

## ★ READING PROGRESS — appended 2026-08-31, after Ruling 10

**The order this file proposes is not the order being worked, and the reason is a ruling taken after
it was written.** **Ruling 10** of `cowork_rulings_2026_08_31_decision_surface_sitting.md` makes
**L0+L1** the detail phase's first deriving subject, and the standing gate is that no derivation may
begin before that subject's slice of Task B is in. The proposed order above is *"stated, not ruled"* by
this file's own words, so it is not overridden — **it is entered at the slice the ruled subject
requires.** The remaining order stands as proposed, headed by L2's entangled decision.

**The L0+L1 slice, derived from this file's own verdicts against `FRAMEWORK.md` §5:**

- **L0's slice is EMPTY, and that is derived rather than assumed.** The four rows that would bear on
  the input contract — rows 31, 32 and 33 (pitch spelling) and row 43 (note recovery from audio) — are
  NOT ADMITTED above, refused because L0 *gives* what they infer and DP-F/G/H settle that they are not
  layers for notated input. There is nothing to read for L0.
- **L1's slice is five rows, all held:** **4** (the partition-point construction), **7** (meter and
  harmony by preference rules — a rival shape for the L1/L2 division and for how metric strength
  enters), **37** and **38** (the two halves of the cadence-cue evidence behind DP-I's split), and
  **39** (admitted on the doubt default). It is this file's group 5 **minus row 40**, whose subject is
  DP-E and L3 rather than L1, **plus row 4**, placed in group 2 above for its DP-C residual although
  the row's own reason names L1 first.
- **One borderline, recorded so it is not rediscovered.** Row 8 supplies L1's metric-strength ground,
  but its METHOD is L2's joint model, so it stays in the L2 slice; its L1-bearing value is already read
  at the object and ruled (the V4 divergence, Ruling 2).
- **No STOP fires** under the remedial commission's §5: all five PDFs are held under
  `docs/research_papers/`, checked at the directory before the slice was claimed workable.

**Read so far:**

| Row | Paper | Grade | Extract | Centrality | Second pass |
|---|---|---|---|---|---|
| 4 | Pardo & Birmingham 2002, algorithms for chordal analysis | **AT THE OBJECT**, whole, pp. 27–49 | `reading_pass/extracts/pardo-birmingham-2002-algorithms-for-chordal-analysis.md` | **CENTRAL** | **OWED** |
| 7 | Temperley & Sleator 1999, modeling meter and harmony | **AT THE OBJECT**, whole, pp. 10–27 | `reading_pass/extracts/temperley-sleator-1999-modeling-meter-and-harmony.md` | **CENTRAL** | **OWED** |
| 37 | Bigo, Feisthauer, Giraud & Levé 2018, relevance of musical features for cadence detection | **AT THE OBJECT**, whole, pp. 355–361 | `reading_pass/extracts/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md` | **CENTRAL** | **OWED** |
| 38 | Karystinaios & Widmer 2022, cadence detection using graph neural networks | **AT THE OBJECT**, whole, 8 pp. | `reading_pass/extracts/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md` | **CENTRAL** | **OWED** |
| 39 | Sears, Pearce, Caplin & McAdams 2018, simulating expectations for tonal cadences | **AT THE OBJECT**, whole, pp. 29–52 | `reading_pass/extracts/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md` | **NOT CENTRAL for L1** | not decided here |

**What row 4's read produced, in one line each — the extract is the record and nothing is restated
here (#6):** the L1 charter's partition-point construction is confirmed at its own primary including
the release half; DP-C's tie-breaking residual is verified at the object with no correction owed; **one
ADDITION CANDIDATE to DP-C's defense is routed to the user and not applied** — an on-domain
boundaries-given-versus-found gap where a guaranteed-optimal search over a context-free segment content
score still fails to recover the analyst's segmentation; one authors' suggestion is labelled CONJECTURE
so it cannot be carried as support for L1's metric strength; and **no falsifier, so no STOP.**

**What row 7's read produced, in one line each — the extract is the record and nothing is restated here
(#6):** the framework's L0 meter [FACT], the unsolved meter-and-harmony circularity, verifies at the
object in the authors' own words with no correction owed; **the named rival shape for the L1/L2 division
reports NO accuracy value of any kind, on no corpus, with hand-tuned weights** — which decides how much
weight that rival can carry rather than criticising the paper; a **second instance** of the fitting
pathology the findings surface already records once at row 19, routed to measurement design; one passage
**supporting** a chosen L2 clause (the garden-path effect corroborating the no-early-discard rule); a
second-hand remark on the R-8 gap out of which **nothing is carried**; and **no falsifier, so no STOP.**

**What rows 37 and 38 produced, read as a pair because the second reports the first's own numbers beside
its own — the extracts are the record and nothing is restated here (#6):** the L1 charter's whole
cadence-cue paragraph verifies at its primaries — **no tonality estimation and no chord segmentation**
in the authors' own words, **F .80 on perfect authentic cadences**, and the half cadence's weakness with
**the charter's own stated reason**, the variable bass motion into it; **the ".29 and .41" pair both sit
in row 38's Table 2**, one of them row 37's figure reported by its comparator; **DP-I's split is
supported by two primaries and an explicit independent replication**, both now at the object; the
charter's third cue is row 37's `Z-bass-compatible-with-I` feature, whose *candidate tonality* is one
**implied by the bass of the arrival chord**, which is what keeps the cue inside L1's decides-nothing
rule; row 38 **removed** row 37's hand-named anchor heuristics and reached comparable results by letting
graph context supply the surroundings, which is a boundary statement for L1 rather than a licence; and
**both papers independently report that the annotation, not only the method, bounds the measured
figure** — routed to measurement design. **No falsifier, so no STOP.**

**What row 39 produced — the doubt default's own question, ANSWERED BY READING as that default intends
(#6, the extract is the record):** its method **does not bear on L1's cues**, on three independent
grounds at the object — it consumes hand-annotated cadences rather than detecting any, its harmonic
viewpoints are computed from a **hand-annotated key**, and its authors name the listener rather than the
music as their object of study. **It is not an L1 candidate and the derivation should not treat it as
one.** The read still paid: a **third independent statement, by a different kind of measurement, that
the half cadence is not separable by local evidence** — an addition candidate to DP-I's defense; a
**precision about the "two independent studies"** the charter cites, which are independent in METHOD but
share their annotated material, row 37's Haydn annotations coming from this paper's own author group; a
finding that **a cue defined over the bass alone can carry the wrong sign**, the cadential leap being
less predictable in isolation than the stepwise motion it must be told apart from; a boundary-evidence
claim routed to the phrase-boundary primitive and L3 rather than L1; and a fourth instance of the
ground-truth-bounds-the-figure pattern. **No falsifier, so no STOP.**

## ★★ THE L0+L1 SLICE IS COMPLETE

**All five members of the ruled subject's slice are read whole at the object and extracted.** L0's slice
was empty by derivation; L1's five rows are in. **The gate the eighty-seventh handoff entry states — no
derivation before the chosen subject's slice of Task B is in — is therefore discharged for L0+L1.**

**What is owed and is NOT discharged, stated so the completion is not read as more than it is:** four of
the five rows are CENTRAL and **each owes a second independent extraction** under the original
commission's §4; none has been performed. **Three findings are routed to the user as addition candidates
or precisions and none is applied** — the on-domain boundaries-given-versus-found gap for DP-C's defense
(row 4), the third-method half-cadence corroboration for DP-I's defense (row 39), and the
independence-of-method-not-of-data precision on the charter's two-study citation (row 39). **No
`FRAMEWORK.md` text is amended by any of this.**

**Not read: the whole of Task B outside this slice — the L2 and L3 groups, in the order this file
proposes, headed by L2's entangled decision. The remainder is untouched.**

---

*Provenance: written 2026-08-31 by the session opened on
`cowork_reading_pass_remedial_commission_2026_08_31.md`, after the ordinary session-start read
(`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived gating answer), the eighty-fourth
and eighty-fifth handoff entries, the findings surface, `reading_pass/population.md`, `FRAMEWORK.md`
§5, §9 and §11, the original commission and this one. `docs/research_papers/BIBLIOGRAPHY.md` was
read whole at the file for the population. No paper was opened. No shell was run on the repository
or on any staged copy of it. No figure of this project's own measurement is restated (#17f, D-431);
the counts above are counts of this file's own rows.*
