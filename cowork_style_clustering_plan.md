# Empirical style clustering — planned future work (the style taxonomy + the style weights, from corpora)

> **Status: committed future direction (user-ratified 2026-06-29) — "we will do this sooner or later."** Not now: it sits
> two steps past the current path (the schema-recognition layer is itself deferred, and this tunes *its* weights). Recorded
> with its groundwork so it is ready when picked up. Related: `cowork_progression_schema_dictionary.md` (the style taxonomy
> + the style weights it would ground), `cowork_progression_schema_design.md` (the consumer that uses the weights),
> target-architecture §2 (the style taxonomy, the verifiability contract).

## 1. What it is
Cluster a large body of tonal scores by their **harmonic-feature distributions**, and read the result two ways:
- the **emergent clusters** are data-derived **styles** — replacing/refining the hand-made style taxonomy with "where the
  harmony actually clusters" (granularity chosen *from our perspective*; the data proposes, we decide the cut);
- each cluster's **feature distribution** is the **per-style weight set** — the "this progression appears in 58% of style
  A vs 3.2% of style B" statistics we currently lack.

The **taxonomy and the weights are one data-derived object** (the clusters and their distributions). **Validation** —
measuring our analyzer's *use* of a style — is a **separate third thing** that needs annotated *scores* (notes + a
ground-truth analysis), not the clustering.

## 2. Why we will do it (the two reasons)
1. **Load-bearing for a future chord-suggestion tool.** Generation must predict unseen chords; the per-style progression/
   substitution statistics *are* the idiomatic-suggestion knowledge. There, the weights are core, not optional.
2. **A marginal inference gain, worth banking in the best-inferrer regime.** On our validated style (Baroque) the gain is
   small — the analyzer is already Baroque-tuned and the residual errors are mostly not progression-resolvable (spelling/
   inversion/symmetric/segmentation), so well under a point. But aiming to be the **best possible inferrer** means the big
   levers are spent and the frontier is a *stack of sub-point gains*; a well-calibrated style prior is one such gain, and
   they add up to something a user notices. (On jazz the gain is larger but currently unmeasurable — no jazz score GT.)

A third, quieter value: it lets us **factually decide the taxonomy** rather than assert it from theory, and it is a
**diagnostic** on our implicit Baroque priors (where the empirical distribution disagrees with our tuned gates).

## 3. The harmonic features to cluster on (the representation)
Per piece, a distribution over — organised by level (most of these are *our own L3–L6 output*):
- **Vertical:** chord-quality distribution (triad + seventh types); extension/density (triad vs 7th vs 9/11/13, added
  tones); alteration profile (altered dominants); inversion + bass-scale-degree distribution; chromaticism rate.
- **Functional:** the degree/function histogram; T/S/D proportions; applied/secondary-dominant rate; modal-mixture rate;
  named-chromatic-chord rates (Neapolitan, aug6, common-tone dim7).
- **Transitional (most discriminative):** root-motion interval distribution; chord-transition n-grams (the harmonic
  language model); schema frequencies (ii–V–I, turnaround, circle-of-fifths); cadence-type distribution; harmonic rhythm.
- **Tonal:** mode distribution (major/minor/modal); modulation rate, distance, keychain shape; tonicization rate.
- **Voice-leading (a different dimension, bordering):** bass-line patterns, voice-leading smoothness, suspension rates.

**Feature coverage by source type:** lead sheets / chord charts give the **functional + transitional + tonal** features
directly (the most discriminative) — sufficient for most of the clustering; **full scores** are needed for the
**inversion / voicing / voice-leading** features; **MIDI-only** needs our analyzer to extract features (adds our error).

## 4. The corpora (freely available, surveyed 2026-06-29)
- **Aggregator:** **ChoCo** (Nature Sci Data 2023) — 18 harmonic-data sources, >1M chord tokens, normalised across Harte /
  lead-sheet / Roman-numeral / ABC. The efficient entry point.
- **Classical / common-practice:** DCML Distant Listening Corpus (~1,326 RN+key+phrase+cadence annotated, MuseScore/
  MusicXML); KernScores/Humdrum (Bach, Mozart, Haydn, Beethoven, Chopin, Scarlatti, Joplin rags; kern+MIDI); OpenScore
  Lieder (~1,300, MusicXML).
- **Jazz:** Weimar Jazz Database (456 solos + full chord changes, bebop/post-bop); iRealPro corpus / Jazz Harmony Treebank
  (1,186 standards as chord sequences in kern).
- **Pop/rock:** Hooktheory/Theorytab (~21,000 melody-chord pairs, key + RN-style functions); POP909 (909, chords + phrase +
  section); McGill Billboard (chord annotations).
- **Folk:** Nottingham (ABC, melody+chords); thesession.org (large Irish-trad ABC).
- **Broad, unannotated:** Lakh MIDI (~176k, genre-mixed); Wikifonia (~6k lead sheets, copyright-encumbered).

**Crucially, the jazz/pop harmonic statistics are reachable now** from lead-sheet / solo-chord corpora, even though jazz/pop
*analysis-validation* ground truth (annotated scores) stays scarce — the clustering+weights half is actionable; the
validation half is not.

## 5. Licensing (it binds even for "statistics only," because the statistics ship)
The derived **statistics/weights are low copyright risk** — aggregate facts, non-expressive, no work reproduced (and a far
stronger fair-use/TDM footing than a generative model). **But** the **license** under which each corpus is obtained is a
contract that can restrict use: a *research-only / non-commercial* corpus can forbid building shipped product behaviour
from it, even weights. So: use **permissive / public-domain** sources (much of Kern, CC-licensed DCML, public-domain
classical) for anything that feeds **shipped** weights; use restricted corpora for **exploration / deciding the clusters**
only. *(Not legal advice — verify per-source terms / get counsel before shipping derived numbers.)* This licensing burden
is part of why the inference-only cost/benefit is poor and the work is deferred to when the suggester (its main
beneficiary) is on the table.

## 6. When to pick it up
- When the **schema-recognition layer** is built (it consumes the weights), or
- when the **chord-suggestion tool** is on the table (its load-bearing input), or
- when we want the **style taxonomy on factual rather than theoretical footing**.
Until then the theory-based taxonomy (`cowork_progression_schema_dictionary.md` §12) is a serviceable v1, and the presets
stay coarse (Baroque/Jazz/Default).

## Sources
ChoCo (nature.com/articles/s41597-023-02410-w). Weimar Jazz Database (ISMIR 2018). Jazz Harmony Treebank / iRealPro corpus
(github.com/DCMLab/JazzHarmonyTreebank; Zenodo 3546040). Hooktheory (Donahue et al. 2022). POP909. DCML Distant Listening
Corpus. KernScores / Humdrum (CCARH). OpenScore Lieder. Lakh MIDI. Accessed 2026-06-29.
