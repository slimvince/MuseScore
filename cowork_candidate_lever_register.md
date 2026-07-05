# The candidate-lever register — compatible methods/theory not yet in the plan

> **Status: RESEARCH NOTE (Cowork, 2026-07-03; user-directed).** A durable register of algorithms, methods, and
> music theory that are **compatible with the layered architecture** and could add inference precision (even
> marginally), but are **NOT in the current plan and NOT commissioned**. Purpose: ideas survive as claimable
> records, not chat answers — each future layer design doc claims from here.
>
> **Process discipline (binding):** nothing in this register is work. A lever enters the plan only through the
> standing gates — its proper layer's design doc, measure-first evidence, and ratification; **datasets enter only
> via the census** (each dataset row below is a census candidate, not an onboarding); **no inference
> problem-fixing until all refactoring / architectural design / algorithmic completion is done** — every lever
> here queues behind that. Confidence marks per the research-doc convention: **[verified]** = checked at a fetched
> primary source; **[reported]** = search-result/abstract level, re-confirm before load-bearing use; **[theory]**
> = established music theory, no implementation claim.
>
> Origin: the 2026-07-03 "what compatible levers remain?" survey + per-duty targeted searches (the user's
> standing method: better knowledge → more specific searches per segregated duty).

## L1 (note model) / L1.5 (derived views) — representation levers

- **R-1 Ornament expansion (L1 derived view).** Trills/turns/mordents/appoggiaturas notated as symbols carry
  implied sounding notes the harmonic layers never see. A lossless, annotate-don't-transform derived view
  (ornament-expanded note set, flagged as implied). Verifiability: notated-realization pairs are scarce — likely
  ships rule-based with the empirically-unvalidated mark. Size: small, style-dependent (Baroque ornaments sit on
  cadential trills — exactly where cadence detection looks). Entry: an L1.5-style view design; verify first what
  the engraving DOM exposes per ornament. **[theory]**
- **R-2 Hypermeter inference (L1.5).** We consume notated metric weight; inferred **hypermetrical** weight
  (Temperley's meter models) sharpens the "harmonic change prefers strong positions" prior at the 2/4-bar scale.
  Verifiability: indirect (does it improve downstream respects?) — a decode-only A/B at its design. Size: small.
  **[reported]** (Temperley, *The Cognition of Basic Musical Structures* line of work)

## L3 (key) — evidence-space levers

- **R-3 Principled tonal-distance spaces as structured priors.** Three related, mutually compatible candidates to
  replace hand-shaped key/chord transition constants with *structured* features at Stage-5 fitting (fewer free
  parameters on 326 scores):
  - **Lerdahl's Tonal Pitch Space** distances (key↔key, chord↔chord within key) as transition priors. **[theory]**
  - **Chew's spiral array / centre-of-effect** (helix embedding of pitches/chords/keys; the CEG key-finder
    reports >90% key recognition on audio within seconds — the symbolic case is easier). Candidate: CE distance
    as key evidence + a boundary-detection view. **[reported]**
    (https://en.wikipedia.org/wiki/Spiral_array_model)
  - **DFT phase space (Yust; Tymoczko & Yust):** the phases of the 3rd/5th Fourier coefficients of the
    pitch-class distribution give a 2-D tonal space where nearest-key is a geometric read; the component
    magnitudes are principled **chromaticism/diatonicity descriptors** — a clean footing for the mode/chromaticism
    cross-axes. **[reported]** (https://people.bu.edu/jyust/tonalDist_rev.pdf ·
    https://sites.bu.edu/jyust/files/2022/09/ICMMlong_paper.pdf)
  Entry: an L3 §15 evidence item; decode-only A/B against the current profile evidence on the ratified A-8 unit.

## L4 (chord) — emission levers

- **R-4 Figured-bass evidence (Baroque; composer-stated chord GT).** Notated figures are direct emission-level
  evidence where we infer from pitch alone. Two dataset candidates (census events, not onboarded):
  - **BCFB — Bach Chorales Figured Bass** (ISMIR 2020): 139 Bach chorales WITH figured-bass encodings
    (MusicXML/kern/MEI) — the gate corpus's own repertoire; the paper's automatic annotators reach ~85%,
    i.e. the task is tractable and the data is real. **[reported]**
    (https://archives.ismir.net/ismir2020/paper/000040.pdf)
  - **DCMLab/figured-bass** — the census §7 residual, still uninspected. **[reported]**
  Also: DCML harmony labels already encode inversion via figured bass in the label grammar — a consistency
  cross-check. Size: potentially non-marginal on Baroque bass/inversion (≈42% of the exact cap is
  bass/inversion). Entry: census → an L4 evidence-channel design.
- **R-5 Psychoacoustic root salience (Parncutt 1988, rev. Terhardt).** Virtual-pitch root weights over a
  pitch-class set — one of the few principled tools for the **share-tone rotation class** (ø7↔m6): pc-identical,
  but root salience differs. Cannot help true symmetric dim7 (structurally rootless). Reference implementation
  exists: `parn88` (pc-set → root, root-ambiguity score, 12-dim weight vector) — the ambiguity score is also a
  natural class-(a) *detector*. **[reported]** (https://github.com/pmcharrison/parn88)
  Entry: L4 §15 rotation-pinning support evidence; measured against the named share-tone gate cases first.
- **R-6 Voicing/doubling priors.** Part-writing regularities as emission features: a doubled leading tone is
  rare, spacing/doubling conventions differ by idiom — weak evidence for chord-identity/inversion, natural
  axis-2-informed features (VL-A/B facts feed them, D6-safe). **[theory]** Entry: with the L4 NCT-filter design
  (same evidence neighborhood).
- **R-14 Explicit non-chord-tone classification by melodic role (the L4 NCT-filter's evidence base;
  researched 2026-07-05, user question at the bwv392 case).** The literature splits into two families:
  (a) **magnitude/penalty scorers** (Pardo & Birmingham's HarmAn template matching; OUR production scorer)
  treat NCTs as attenuated evidence mass — the indirect route, weakest on accented NCTs (metric position
  RAISES our tone weight, so accented NCTs get the biggest wrong vote); (b) **melodic-role systems** read
  the step context directly: species counterpoint DEFINES each NCT type by approach/departure motion (Fux
  1725); Temperley's Melisma harmony program carries an explicit ornamental-dissonance preference rule (a
  non-chord pitch should be closely followed by stepwise motion — melodic context as first-class evidence);
  and the explicit-classifier line (Ju, Condit-Schultz, Arthur & Fujinaga 2017, DLfM; the ISMIR-2018
  follow-up) identifies NCTs FIRST and analyzes harmony on the residue — "by identifying non-chord tones,
  the task of harmonic analysis is much simplified"; on 140 **Bach chorales** (our exact domain) F1 rose
  57 %→72 % when METRIC + a CONTEXTUAL WINDOW joined pitch-class-only features — the step-context and
  metric-role features carry the signal. Modern neural RN systems learn the same implicitly. **In-house
  substrate already built:** the dormant VL-A voice-linear view (axis 2) supplies exactly the per-voice
  approached-by/left-by-step facts a melodic-role classifier needs (D6-safe: axis-2 FACTS feeding an L4
  lever); the dormant L4 membership rule's stepwise tiers are the claim site. Entry: the roadmap's L4
  NCT-filter lever (step 4) claims this at its design; the chorale F1 numbers set the calibration
  expectation. **[researched — not commissioned; founding case bwv392 m9 b4 (GT = Dm/F, vi6 in F, bass G
  passing — Tymoczko, the user, and species theory agree; the magnitude-only scorer is bass-bonus-fragile
  exactly there)]**

## L5 (function) and above — syntax levers

- **R-7 Hierarchical harmonic grammar (the biggest theory item left).** Rohrmeier's generative syntax of tonal
  harmony (2011) + the jazz-harmony grammar; prolongation as a tree over functions ("I–V–I spans and governs its
  inside"), beyond our deliberately-pairwise §5.0 grammar. **Ground truth exists and is already in our research
  corpora: the Jazz Harmony Treebank** (expert hierarchical analyses of complete standards); unsupervised
  grammar-induction results exist (TISMIR). Compatible as a **cross-cutting annotation layer above the flat L6
  partition** (the flat punctuation-span oracle stays; prolongation-spans would be a new span family — a §2.15
  typology event). Size: potentially non-marginal for RN disambiguation + the recognition consumer's prior; also
  the natural successor to the Stage-5 partial matcher. **[reported]**
  (https://www.tandfonline.com/doi/abs/10.1080/17459737.2011.573676 ·
  https://program.ismir2020.net/static/final_papers/80.pdf ·
  https://transactions.ismir.net/articles/10.5334/tismir.217)
- **R-8 Neo-Riemannian transformation channel (chromatic-coloristic idiom).** Where functional syntax fails
  (Tristan-class chromaticism, third-relations), PLR-transformation parsimony is the accepted alternative
  plausibility measure — the verifiability contract's alternative-confidence-path shape, for the capability
  track (A-3/A-4/A-5 neighborhood). Entry: with the capability track's design; validated on `wagner_overtures`.
  **[theory]** (Tonnetz/DFT connections: https://people.bu.edu/jyust/yustTonnetzSub.pdf)

## Axis 2 (voice leading) — levers for the design-gated components

- **R-9 IDyOM-class melodic expectation (Pearce).** Information-content (unexpectedness) per note from an
  unsupervised statistical model; published segmentation performance (boundary F1 ≈ .58 vs annotations, ≈ .64 vs
  listeners) — direct **VL-E** boundary evidence beside the GTTM rules; AND an **L4 NCT prior** (expected notes
  are more often passing/ornamental — an axis-2-informed emission feature, D6-safe). **[reported]**
  (https://onlinelibrary.wiley.com/doi/full/10.1111/j.1756-8765.2012.01214.x ·
  https://archives.ismir.net/ismir2008/paper/000228.pdf)
- **R-10 Tessitura/range priors for stream separation (VL-D).** Voice-range and crossing-avoidance priors from
  the separation literature — already implicit in the named methods; recorded so VL-D's design weighs them
  explicitly. **[theory]**

## Calibration / metric — method levers (Stage-5 neighborhood)

- **R-11 Conformal prediction.** Distribution-free calibration giving coverage *guarantees* for abstention
  (vs fitted reliability maps' estimates) — a complement or alternative at the Class-P step; needs only the C1
  instrumentation's data. Entry: weigh at the Stage-5 calibration design. **[reported — standard ML method]**
- **R-12 Multi-granularity self-consistency.** Run the analysis at two window scales; disagreement = an
  uncertainty signal feeding calibration. Nearly free; uses existing machinery. Entry: a C1-follow-up
  measurement. **[internal]**
- **R-13 Fitting-time data augmentation.** Transposition invariance (already exploited by the discovery
  pipeline's key normalization) + mode-mixture augmentation for rare classes at Stage-5 fitting — standard,
  cheap, guards the 326-score fit. **[method]**

## What was looked for and NOT found (so it is not re-searched)

- No published system modeling overlapping per-voice phrases for harmonic purposes (re-confirmed across all
  sweeps — the axis-2 separation stands).
- No prior piece-level motion-type texture-idiom taxonomy (the axis-2 discovery result appears novel).
- No implied-polyphony stream ground truth (the VL-D census gap stands).
