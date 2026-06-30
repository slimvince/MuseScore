# Harmonic idiom discovery — design spec (empirical, low-prejudice discovery of harmonic structure from corpora)

> **Status: design, v1.2 draft (2026-06-30 — prior-art-grounded (§2a) + tpc encoding + lead-sheet trust ruling, plus
> the extraction-tooling decision D6 (music21 uniform extractor, L1/L2-mechanical boundary, never L3+) and the resolved
> open items 1/2/4).** Held to the same QA and rules as the L(n) specs (verified facts only;
> decisions weighed against alternatives; risks and open items explicit). **This is a research/analysis component,
> not a runtime layer** — its output (a data-derived idiom structure + per-idiom distributions) feeds the style tags
> and weights of `cowork_progression_schema_dictionary.md`, and ultimately the presets. Companions:
> `cowork_style_clustering_plan.md` (the corpus survey + the why/when), `cowork_progression_schema_design.md` (the
> consumer of the weights), target-architecture §2 (the verifiability contract, the style taxonomy).

## 1. The question (what this discovers, and what it refuses to assume)
Discover, from a large body of tonal music, the harmonic structure that **actually** partitions it — and read the
result two ways (per the plan): the emergent groups are **data-derived idioms**; each group's feature distribution is
the **per-idiom weight set** we currently lack.

Two assumptions are **explicitly refused** and demoted to hypotheses tested *after* the fact:
- that the partition is **"genre"** (it may cut across genre — modal-vs-functional, sparse-vs-dense, diatonic-vs-
  chromatic, or an axis we have no name for);
- that the **discriminative parameters are the ones we would name** (mode, chord quality, …). We do **not** pre-select
  which musical parameters carry the structure; the data does.

## 2. The core principle — minimal prejudice, not zero
There is **no zero-prejudice method.** A score must be encoded into data *somehow*; a similarity/model must be chosen;
confounds must be controlled. Those are priors. The discipline is to push them to the **lowest, most theory-neutral
level** and to **interpret post-hoc** — never to pretend they are absent.

The governing order is **discover → then name**: learn structure on a low-level encoding carrying **no** theory or
genre labels; only afterward hold the emergent structure up against theory features **and** genre labels, both as
**interpretation lenses, never as clustering input**.

The question therefore has **two stages**: (1) discover which **parameters/axes actually carry structure** in real
scores (chords, progressions, modes, or something unnamed) — *without* pre-selecting them; (2) along those axes, ask
whether the emergent **clusters are "genre"** or something we have **no name for yet**. Stage 2 is only askable once
stage 1 has told us what the axes are.

## 2a. Prior art — what exists, what we reuse, why we still re-run
This has been studied, on a method we **adopt rather than reinvent** — but always **single-tradition**, and (for the
closest precedent) on a **different harmonic object** than ours, so the published *conclusions* do not answer our
question. The art splits along a representational seam:
- **Moss & Rohrmeier 2021, "Discovering Tonal Profiles with LDA"** (Music & Science; DCML, MIT-licensed code
  `github.com/DCMLab/lda_tpcs`) — LDA (a **bag-of-words, order-free** model) over **tonal pitch classes** on ~2,000
  Western-classical pieces / ~600 years. Topics emerge as **diatonic collections / line-of-fifths segments** — i.e.,
  *tonal vocabulary* ("what notes/keys"), **not** progressions. Closest method; **classical-only**; a **different
  object**.
- **The jazz PCFG** (TISMIR, "Unsupervised Induction of Harmonic Syntax for Jazz") — the opposite representation: a
  probabilistic grammar induced unsupervised from chord-symbol sequences, capturing harmonic **syntax** (progression
  structure, parse trees latent). **Jazz-only**; output a grammar, not idiom clusters/weights.
- **Mauch et al. 2015** (Royal Society Open Science) — LDA on **audio**-derived harmonic words → 8 topics → pop style
  classification. **Pop-only**; audio-based, so it had to split harmonic from timbral lexica to stop timbre swamping
  harmony.

**What we reuse — the method, not the conclusions:** the LDA/topic formulation + the MIT code; the discover-then-name
protocol; the PCFG option for the syntax side; Mauch's symbolic-over-audio confound lesson; and the
**tonal-pitch-class (line-of-fifths) encoding** — Moss's spelling is what made topics interpretable (§3).

**Why we still re-run it ourselves:**
1. **Different object.** Idiom (ii–V–I, turnarounds, cadences, substitutions) is *progression/transition* structure.
   Moss's order-free pc-bags discard exactly that, so his topics are tonal *vocabulary*, not the per-idiom progression
   weights the encyclopedia needs; our §4 clusters over **transitions**, aimed at the dimension he discards. No existing
   result *is* our object.
2. **Coverage.** Every precedent is single-tradition (classical / jazz / pop). Nobody runs **one** discovery across
   classical + jazz + pop + folk to find idioms that may **cut across** genre — which *is* the stage-2 question (§1).
   Borrowing classical conclusions would silently impose classical structure on everything: the prejudice we refuse.
3. **Integration / shipping.** The result must be distributions over **our** encyclopedia entries and analyzer
   features, validated against **our** ground truth (DCML/BIR) and reproducible + licensed to ship — not a paper figure.

So "doing it ourselves again" = **running validated tools, for the first time, on the cross-tradition union, aimed at
idiom rather than tonal vocabulary, inside our system** — applying a proven method to a question nobody has asked of it.

## 3. The encoding (the low-prejudice representation)
- **Unit:** the piece, and (open item §11) fixed-length **windows** within a piece, to allow within-piece idiom change.
- **Two complementary views** (the §2a seam — run both):
  - **the progression view (lead, where idiom lives):** **key-normalized chord-transition sequences** — *no* "ii–V",
    *no* "dominant seventh", *no* function/quality *labels*. The method must *discover* that quality or function
    matters, if it does, rather than be told. This is the axis Moss's order-free model discards and ours targets.
  - **the vocabulary view (complementary, Moss's axis):** order-free **tonal-pitch-class profiles**, which Moss showed
    yield interpretable diatonic-set structure. Cheap to add; a useful cross-check and a second lens.
- **Encode the chords as tonal pitch classes (line of fifths) where spelling is reliable.** Moss's line-of-fifths
  encoding is what made topics interpretable, and tpc is still low-prejudice (the raw *written* note, not a functional
  label). The encoding is therefore **per-source**, recorded in the manifest:
  - **classical scores** — tpc (well-spelled);
  - **lead-sheet / chord-symbol corpora** — **trusted** (user ruling 2026-06-30: lead-sheet chord symbols are reliable
    for the harmonic features we cluster on); read the chord root + quality directly, tpc-spelled from the symbol;
  - **raw MIDI / unspelled** — fall back to mod-12 pitch classes (the only place spelling is genuinely absent).
- **Chord provenance, by source type (the plan §3 coverage rule):** chord **symbols** where given (lead sheets / chord
  charts — clean and trusted); **chordify/reduction** where only notes exist (full scores — flagged as added extraction
  noise, §5); **melody-only / monophonic** sources are **excluded** from harmonic discovery (no harmony to read).
- **Extraction tooling — music21, mechanical only, never our analyzer.** Verticalize with **music21** (`chordify` for
  note-only scores; its chord-symbol parsing for lead sheets), applied **uniformly to every source**. This is chosen
  *not* because music21 verticalizes best — our own L1/L2 change-point slicer is arguably cleaner — but because it
  ingests *all* the corpus formats (ABC, kern, MusicXML, MIDI, chord symbols) the **same** way; a mix of extractors that
  correlates with source would be the very confound §5 forbids. **Extraction stops at the mechanical front** — the L1
  (notes) + L2 (slicing) layer, which is *mechanical* (an error there is a bug, not a misinference). **Our L3+ key/chord/
  function inference must NEVER touch the extraction**: it is Baroque-tuned, would rediscover our own priors, and would
  inject genre-correlated error on non-Baroque material — the worst confound for a genre-vs-not study. **Validation:**
  run a shared MusicXML subset through both music21 and our L1/L2 and confirm the verticality streams agree (our trusted
  engine as the yardstick, music21 as the uniform workhorse). And note: *mechanical* = **unbiased, not clean** — the raw
  verticalities still contain passing tones / suspensions (correct output, not a bug); a **neutral, uniform reduction**
  applied identically to every style tames them (or the topic model tolerates them as low-frequency events) — never L4.
- **Key-normalization** (transpose every piece to a common tonic) is the first confound control (§5).
- **Deliberately NOT encoded** (to avoid confounds): absolute key, voice-leading (a separate dimension), instrumentation,
  tempo, absolute duration. (Spelling is now *in*, via tpc.) Some are retained **only** as interpretation-lens
  covariates (§6).

## 4. The discovery method(s)
Lead with **unsupervised methods that build their own features** — run more than one and **triangulate**:
- **A — transition co-occurrence topic model** (NMF / LDA over the pc-set-transition counts): latent "harmonic
  topics" nobody named; each piece a mixture. Lightweight, interpretable, sandbox-feasible.
- **B — transition/chord embedding** (the "harmony as language model" line in our sources — Korzeniowski & Widmer,
  Tymoczko): learn piece/transition vectors, cluster in the embedding space. Heavier (compute/data; §11).
- **C — distance on transition matrices + hierarchical clustering**: yields the **dendrogram** — the "the data
  proposes, we decide the cut" view (the plan §1).

Granularity (how many idioms) is read from **stability + interpretability**, **not** a forced *K*. The feature-based
families (the plan §3) are **not** the clustering input here — they are the §6 interpretation lens.

## 5. Confound control (the part that actually decides validity)
The dominant failure mode: naive clustering discovers **which corpus a piece came from, what key it is in, how long it
is, instrumentation, or encoding quirks** *before* it ever reaches "idiom." So this is a first-class gate, not a
footnote:
- **key-normalize** (§3); **length-normalize** (rate features, fixed-length windows); **balance/stratify** sources;
  **de-duplicate**; **exclude** melody-only sources; **audit** chordify extraction noise on a labeled subset.
- **The source-leakage test (mandatory):** hold out the **source label** and test whether the clusters are explained
  by source/key/length. **If clusters ≈ source, we found bookkeeping, not idiom** — back to the encoding.
A discovered structure earns the word "idiom" only **after** it survives these.

## 6. Interpretation protocol (naming the emergent structure)
**Post-hoc only.** Correlate each emergent axis/cluster against, separately:
- **theory features** — mode distribution, chromaticism rate, extension/density, root-motion-interval profile,
  applied/secondary rate, cadence-type mix, harmonic rhythm (the plan §3 families);
- **external labels** — composer / era / genre / source.

Reading the alignment table answers the real question:
- an axis matching a **theory feature** → we **rediscovered it from data** (validates that parameter);
- an axis matching **genre** → idioms **are** genre-like;
- an axis matching a **source** → **confound** (return to §5);
- an axis matching **nothing we have a name for** → a candidate **unforeseen parameter** — the prize.

## 7. Deliverables
1. The **emergent idiom structure** (the groups + the chosen cut) — what refines or replaces the hand taxonomy
   (`cowork_progression_schema_dictionary.md` §12.1).
2. The **per-idiom harmonic-feature distributions** — the weights the schema consumer wants.
3. The **interpretation table** (emergent axis ↔ theory feature ↔ genre/source).
4. A **reproducible pipeline** + a **manifest-stamped corpus** (provenance, like the BIR corpus manifests).

## 8. Validation & QA (held to the L-spec bar)
- **Reproducible:** fixed seeds, manifest-stamped corpus, deterministic pipeline.
- **Stable:** the solution survives resampling / corpus subsampling.
- **Confound-clear:** the §5 source-leakage test passes.
- **Honesty marks (verifiability contract):** idiom groups are validated against an **analysis** ground truth only
  where one exists (classical: DCML); **jazz/pop groups are "empirically-derived but analysis-unvalidated"** — the
  named GT want (the plan §6). The result is a **hypothesis about idioms, not a labeled truth**, and is marked so.

## 9. Decisions (with alternatives weighed)
- **D1 — discovery-led, theory-as-lens** (not feature-led). *Rejected:* clustering on hand-built functional features —
  it can only rediscover the priors we encoded.
- **D2 — minimal low-level encoding: key-normalized tonal-pitch-class transitions** (line-of-fifths where spelling is
  reliable — classical scores + trusted lead-sheet symbols — else mod-12), run as two views (progression + vocabulary,
  §3). *Rejected:* high-level functional features (prejudges the answer); raw audio/MIDI (timbre/instrumentation/
  performance confounds swamp harmony — Mauch's lesson); bare mod-12 pitch classes everywhere (discards the
  line-of-fifths structure that made Moss's topics interpretable).
- **D3 — multiple methods + triangulation; granularity from stability.** *Rejected:* a single method, or a forced *K*.
- **D4 — confound control as a first-class gate** (the source-leakage test). *Rejected:* naive clustering — it finds
  bookkeeping and calls it style.
- **D5 — chord-symbol corpora preferred; chordify flagged; melody-only excluded.** *Rejected:* treating all sources as
  equal-quality harmony.
- **D6 — music21 as the uniform mechanical extractor; extraction stops at the L1/L2 (mechanical) front; our L3+
  analyzer never used.** *Rejected:* our own L1/L2 as the extractor (cleaner change-point slicing, and it's our audited
  code — but it can't ingest ABC/kern, so it would force a *mix* of extractors correlated with source, a §5 confound);
  our full analyzer for extraction (Baroque-tuned bias that correlates with genre — the worst confound for a
  genre-vs-not study). music21 is chosen for **uniform** format coverage, **cross-validated** against our L1/L2 on a
  shared MusicXML subset to bank the trust.

## 10. Data plan & acquisition (self-serve vs need-help)
- **In hand now (self-serve — no fetching):** the **music21 bundled corpus**, ~3,194 works — Palestrina/Josquin/
  trecento (modal Renaissance), Bach/Corelli/Handel (Baroque), Mozart/Haydn/Beethoven (Classical), Schumann/Chopin
  (Romantic), Ryan's Mammoth/O'Neill's/Essen/Aird's (folk-trad), Schoenberg (atonal). **Multi-era**, but mostly
  **note-level** (needs chordify) and **near-zero jazz/pop**. Confirmed available in the sandbox (music21 9.9.2).
- **Need you to download (my web access is restricted — I cannot pull these myself):** the clean **chord-symbol**
  corpora that the discovery wants for volume + jazz/pop coverage —
  **ChoCo** (the aggregator), **DCML Distant Listening Corpus** (classical RN-annotated), **Jazz Harmony Treebank /
  iRealPro** (jazz), **Hooktheory/Theorytab** (pop/rock), **POP909**, **Nottingham / thesession** (folk-with-chords),
  **McGill Billboard**. Drop them under e.g. `C:\s\MS\corpora\<name>\` and I'll read from there (the exact source URLs
  are in `cowork_style_clustering_plan.md` §4/Sources).
- **Licensing (the plan §5):** permissive / public-domain sources for anything that feeds **shipped** weights;
  restricted corpora for **exploration / deciding the clusters** only.

## 11. Open items
1. **Within-piece idiom change — resolved via the mixture model.** A topic/mixture model (LDA) represents a piece as a
   *distribution over* idioms, so a piece that genuinely changes idiom is carried honestly as a mixture, not blurred
   into one — diffusion only bites under *hard* one-idiom-per-piece assignment (e.g. k-means on whole-piece vectors),
   which we avoid. Lead with whole-piece mixtures; **windowing** is a secondary lens only to *localize where* a piece
   changes idiom. How mixed pieces actually are becomes a measured output — itself a finding. (Residual open: the window
   length, if/when we localize.)
2. **Chordify extraction-noise — quantify on DCML.** Mechanical verticalization (music21 `chordify`, or our L2) yields
   raw verticalities containing passing tones / suspensions — *correct mechanical output, not a bug, and not "clean."*
   Before trusting note-only sources, measure the noise on **DCML** (which carries both the notes *and* a human
   analysis): run the extraction, compare to the human chords, get the error rate, and set the neutral reduction
   accordingly. Lead-sheet chord-symbol sources bypass this entirely.
3. **Compute limits** — the topic-model (A) and transition-matrix (C) paths are sandbox-light; the embedding path (B)
   may need the user's machine for large corpora (to be sized empirically on the user's machine).
4. **Jazz/pop analysis-validation GT — a limitation, not a pending decision.** We *can* derive jazz/pop idioms and
   weights from chord data (reachable); we *cannot yet* validate that *using* them improves our analyzer, because that
   needs annotated **scores** (notes + a ground-truth analysis), which barely exist for jazz/pop. So jazz/pop idioms
   ship with the "empirically-unvalidated" mark (the verifiability contract). The standing **want** is a jazz/pop
   analysis ground truth; nothing to decide now — only to flag honestly.
5. **Promotion path** — how a ratified emergent idiom set replaces the §12.1 placeholder taxonomy and the coarse
   `{Baroque, Jazz, Default}` style tags (a joint decision with the preset system, per the dictionary §12.1).

## 12. Glossary
- **Idiom** — a data-derived harmonic grouping (not assumed to equal genre).
- **Emergent cluster** — a group found by unsupervised discovery on the low-level encoding, before any naming.
- **Low-prejudice encoding** — key-normalized pc-set transition sequences, carrying no theory/genre labels.
- **Confound** — non-harmonic structure (source, key, length, instrumentation, encoding) that clustering may discover
  instead of idiom.
- **Source-leakage test** — the check that clusters are *not* explained by which corpus/source a piece came from.
- **Interpretation lens** — theory features and genre labels used *post-hoc* to name emergent structure, never as input.
- **Per-idiom weights** — each cluster's harmonic-feature distribution (the "this progression in 58% of A vs 3% of B").

## Sources
**Prior art (the §2a precedents, deep-read 2026-06-30):**
- Moss & Rohrmeier, "Discovering Tonal Profiles with Latent Dirichlet Allocation," *Music & Science* 4 (2021), 1–15 —
  fabian-moss.de/publication/2021_moss_lda/ ; code (MIT): github.com/DCMLab/lda_tpcs (a Jupyter notebook on the DCML
  classical corpus; topics = pitch-class distributions ≈ diatonic sets, order-free).
- "The Potential of Unsupervised Induction of Harmonic Syntax for Jazz," *TISMIR* — transactions.ismir.net/articles/10.5334/tismir.217
  (PCFG/grammar induced unsupervised from jazz chord symbols; syntax, jazz-only). Cf. Harasim, Finkensiep et al.,
  "The Jazz Harmony Treebank," ISMIR 2020.
- Mauch, MacCallum, Levy & Leroi, "The evolution of popular music: USA 1960–2010," *Royal Society Open Science* 2 (2015) —
  LDA on audio-derived harmonic words → 8 harmonic topics → data-driven pop style classification.
- Hu & Saul, "A Probabilistic Topic Model for Music Analysis," NIPS 2009 (LDA-on-pitch-class foundation).

**Method + data:** music21 corpus (Cuthbert/MIT, bundled, accessed 2026-06-30). Harmony-as-language-model: Korzeniowski
& Widmer 2018; Tymoczko; Sears et al. Corpora + licensing: see `cowork_style_clustering_plan.md` §4–§5 (ChoCo, DCML,
Jazz Harmony Treebank, Hooktheory, POP909, Nottingham, McGill Billboard).
