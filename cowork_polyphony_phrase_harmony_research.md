# Polyphony, phrase structure, and harmonic analysis in counterpoint — research findings

> **What this is.** A durable, cited record of the deep search run in response to the user's fugue/polyphony
> question: *how do research, public algorithms, and published software handle phrase/segmentation structure and
> harmonic (chord / Roman-numeral) analysis in polyphonic, contrapuntal music — where several voices carry
> concurrent, overlapping, out-of-phase phrases and the harmony is implied by the counterpoint rather than stated
> as block chords?* Compiled by Cowork. **Accessed 2026-07-01.**
>
> **Confidence marking.** Claims verified against a fetched primary abstract are marked **[verified]**; claims from
> a search-result snippet or established-literature knowledge (not independently re-fetched here) are marked
> **[reported]** — reliable but to re-confirm at the primary source before it becomes load-bearing in a build.

---

## 0. The one-line answer

The field does **not** model concurrent, overlapping, per-voice phrases for the purpose of harmonic analysis.
Harmony in polyphony is analysed at the **onset / verticality level** (one label per vertical slice), and the
counterpoint difficulty — implied harmony, chords "teased out" of the lines — is handled by **non-chord-tone
filtering**, not by recovering phrase structure. **Voice separation** exists as a mature but *separate* task, used
when you actually want the independent voices (for voice-leading), and is standardly **decoupled** from chord
inference. Our forward-only architecture already matches this consensus.

## 1. Phrase / cadence detection in polyphony — one texture-wide layer, not per-voice

- Cadence detection is framed as **node classification over a note-graph of the whole texture** — a single
  texture-wide task, not a per-voice one (*Cadence Detection in Symbolic Classical Music using GNNs*, arXiv
  2208.14819). **[reported]**
- The newest unified analyser (**AnalysisGNN**, arXiv 2509.06654) treats cadence and phrase as **note-level tasks
  on one shared graph**, alongside key and Roman numeral. **[verified]**
- Per-line **melodic** phrase segmentation exists (*A DNN for Melodic Phrase Segmentation*, arXiv 1811.05688) but
  is a **melody** task — it segments a single line and is **not** fed into harmonic analysis. **[reported]**
- **No system found detects concurrent, overlapping phrases for harmonic purposes.** The overlapping-phrase
  structure of a fugue (staggered subject entries in independent voices) is simply **not represented** in the
  harmonic pipeline of any published system located.

**Consequence for us:** a single **flat** harmonic-grouping layer (our L6) is the field norm for harmony. The
accepted *melodic* phrase, and the overlapping per-voice phrases of a fugue, belong to a **different axis**
(voice-leading / melody-line), not to harmonic grouping.

## 2. Voice separation — a mature, *separate* task

Recovering independent voices from an implied-polyphonic surface (e.g. a keyboard fugue) is a well-established task
with both rule-based and learned methods:

- **Chew & Wu contig-mapping** (2005) — split the score into *contigs* of constant voice-count, then connect
  fragments across contig boundaries by pitch proximity. The classic rule-based baseline. **[reported]**
- **VISA** — Voice Integration/Segregation Algorithm (Karydis, Cambouropoulos et al., ISMIR 2007). **[reported]**
- **Temperley, "Voice and Stream"** (Music Perception, 2008) — the perceptual streaming framing. **[reported]**
- **Musical Voice Separation as Link Prediction** (GNN, IJCAI 2023 / arXiv 2304.14848) — the modern learned
  formulation: predict which note-pairs are voice-adjacent. **[reported]**

**Consequence for us:** these are the methods to lean on **when we build the voice-leading / melody-line axis**
(the confirmed second axis, `cowork_idiom_discovery_findings.md`). They are preprocessing for *voice-leading*
analysis and are standardly **not** wired into chord inference.

## 3. Harmonic / Roman-numeral analysis of counterpoint — done at the verticality level, with explicit non-chord-tone handling

- **ChordGNN** (arXiv 2307.03544): processes note-wise features and their interdependencies but **contracts to an
  onset-wise output** via an edge-contraction step — **every note at an onset shares one Roman numeral**. It
  reports outperforming the prior state of the art on the reference datasets. **[verified]**
- **music21** `chordify` reduces the polyphonic surface to a sequence of verticalities, then labels each — the same
  onset/verticality reduction. **[reported]**
- The counterpoint difficulty is addressed by **explicit non-chord-tone handling**. AnalysisGNN integrates a
  dedicated **Non-Chord-Tone prediction module that identifies and excludes passing and non-functional notes from
  all tasks**, improving label consistency. **[verified]** The one system closest to ours, **Contrapunctus**
  (contrapunctus.app), likewise ships explicit non-chord-tone classification (passing / neighbour / suspension /
  embellishment) plus Fux species counterpoint, and is state-of-the-art-competitive **with no explicit grouping
  layer** (`contrapunctus_findings.md`, accessed 2026-06-20). **[reported]**
- Conceptual framing of *why* counterpoint is hard: in a fugue the harmony must be "teased out" and is not at the
  surface; non-harmonic tones (suspensions, neighbours, passing tones, pedals, anticipations) are extraneous to
  the harmony and governed by contrapuntal rather than harmonic laws; a single line-motion such as D→C over a held
  {F, A} is genuinely ambiguous between a chord change and a "merely linear" passing motion (*Computational music
  analysis from first principles*, arXiv 2407.21130). **[reported]** An older survey figure of "<50% Roman-numeral
  accuracy" is **dated** — neural systems now reach ~80%+ on chorales (harder repertoire lower); do not cite the
  50% as current.

**Consequence for us:** our **L2 change-point slice → L4 chord** path (label per verticality) **is** the field
standard. The place where counterpoint difficulty is actually absorbed is an explicit **non-chord-tone filter** —
see §5.

## 4. Feedforward vs joint — the trend is joint multi-task on a shared representation, *not* voice/phrase → chord feedback

- The state-of-the-art direction is **joint multi-task** models on a shared note-graph (**AnalysisGNN**), where the
  non-chord-tone module improves harmony, cadence, and key **together**. **[verified]**
- But this is *multi-task on a shared representation* — **not** a pipeline where a voice-leading layer or a phrase
  layer feeds **back** into chord inference. No mainstream system runs phrase → chord or voice → chord as an
  iterative loop.

**Consequence for us:** our forward-only architecture with a **gated** joint step (the ratified key↔chord coupling)
is consistent with this. A future non-chord-tone module (§5) is the natural candidate for that shared/joint
representation.

## 5. The three implications carried into our design (proper-layer)

1. **Our approach is the field standard — validated.** Onset/verticality harmony (L2→L4) = ChordGNN / chordify /
   Contrapunctus. A single flat harmonic-grouping layer (L6) = how everyone models phrasing for harmony. Per-voice
   phrasing as a separate voice-leading axis = the standard decoupling of voice separation from chord inference.
   *(Folded into `cowork_layer6_grouping_design.md` §2 / §14.)*

2. **The real lever for polyphonic accuracy is an explicit non-chord-tone filter — an L4 (emission) concern,
   informed by the voice-leading axis.** This is where the whole field puts the counterpoint difficulty, and it is
   an **emission-level** lever (consistent with our meta-principle: precision lives in emission + the functional
   layer, not in search). Recorded as a **future L4 / joint-step lever**, **not built now** (standing rule: no
   inference problem-fixing until refactoring / architectural design / algorithmic completion is done).
   *(Logged in `docs/implementation_roadmap.md`, forward-increment step 4.)*

3. **Overlapping per-voice phrases are genuinely nobody's harmonic input.** Keeping L6 flat omits no standard
   technique. The fugue's staggered subject entries belong to the voice-leading / melody-line axis, decoupled from
   harmony — exactly as we have it. *(This is also the terminology fix in L6 §0: L6's "phrase" is a harmonic
   grouping span, not the accepted melodic phrase.)*

## 6. The research foundation to lean on for the voice-leading / melody-line layer (axis 2)

When we build the second axis — where **voice leading**, **melodies**, and the **accepted (broadly monophonic)
music-theory phrase** are identified — the methods above are the starting corpus:

- **Voice recovery from implied polyphony:** Chew & Wu contig-mapping (2005); VISA (Cambouropoulos/Karydis, ISMIR
  2007); Temperley "Voice and Stream" (2008); Voice Separation as Link Prediction (IJCAI 2023, arXiv 2304.14848);
  and the voice/stream facilities in `partitura` / `music21`.
- **Melodic (per-line) phrase segmentation:** the DNN segmenter (arXiv 1811.05688) and the classical grouping
  rules (Lerdahl & Jackendoff GTTM grouping preference rules; the melodic-boundary literature).
- **Cadence as a texture-wide signal** (arXiv 2208.14819) and the unified multi-task framing (AnalysisGNN, arXiv
  2509.06654) — for the eventual coupling of the two axes.

## 7. Sources

- ChordGNN — *Roman Numeral Analysis with Graph Neural Networks: Onset-wise Predictions from Note-wise Features*,
  arXiv 2307.03544. https://arxiv.org/abs/2307.03544 · repo https://github.com/manoskary/chordgnn **[verified]**
- AnalysisGNN — *Unified Music Analysis with Graph Neural Networks*, arXiv 2509.06654.
  https://arxiv.org/abs/2509.06654 **[verified]**
- Cadence Detection in Symbolic Classical Music using GNNs — arXiv 2208.14819.
  https://arxiv.org/abs/2208.14819 **[reported]**
- Musical Voice Separation as Link Prediction — IJCAI 2023 / arXiv 2304.14848.
  https://arxiv.org/abs/2304.14848 **[reported]**
- A DNN for Melodic Phrase Segmentation — arXiv 1811.05688. https://arxiv.org/abs/1811.05688 **[reported]**
- Computational music analysis from first principles — arXiv 2407.21130. https://arxiv.org/abs/2407.21130
  **[reported]**
- Chew & Wu, contig-mapping voice separation (2005); Karydis/Cambouropoulos VISA (ISMIR 2007); Temperley, "Voice
  and Stream" (Music Perception, 2008). **[reported]**
- Contrapunctus (contrapunctus.app) — internal notes `contrapunctus_findings.md` (accessed 2026-06-20).
