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

## 4. The corpora — verified sources & licensing (surveyed 2026-06-29; links + licenses verified 2026-06-30)
*Licensing tag (per §5): **[ship]** = permissive enough to feed **shipped** weights; **[expl]** = non-commercial /
restricted → **exploration / cluster-deciding only**. Verify each LICENSE before shipping any derived numbers.*

- **Aggregator — ChoCo** (Nature Sci Data 2023): `github.com/smashub/choco` · Zenodo `10.5281/zenodo.7193888`. 18
  sources, >1M chord tokens, normalised (Harte / lead-sheet / RN / ABC) as **JAMS** + `meta.csv`. Mostly
  **CC-BY 4.0 [ship]**; three subsets CC-BY-NC-SA **[expl]**. The efficient entry point.
- **Classical (also our validation GT) — DCML**: `github.com/DCMLab/{mozart_piano_sonatas, ABC (Beethoven),
  romantic_piano_corpus, scarlatti_sonatas}`; the **Distant Listening Corpus** umbrella (Hentschel et al. 2025). TSV +
  MuseScore, RN+key+phrase+cadence. **CC-BY-NC-SA [expl]**. Plus KernScores/Humdrum & OpenScore Lieder
  (public-domain classical **[ship]**).
- **Jazz — Jazz Harmony Treebank**: `github.com/DCMLab/JazzHarmonyTreebank` (`treebank.json`, ~150 tunes; chord
  symbols + trees; verify `LICENSE.md`). Built on the **iRealPro corpus** (Zenodo `3546040`, ~1,186 tunes, Shanahan et
  al.; community-sourced **[expl]**). Weimar Jazz DB (456 solos + changes).
- **Pop/rock — McGill Billboard**: `ddmal.ca/research/The_McGill_Billboard_Project_(Chord_Analysis_Dataset)/`
  (~740 songs, MIREX `.lab` chords, **CC0 [ship]** — the clean pop anchor); **Hooktheory HLSD**
  (~18,843 sections, melody+chord+**key+function**, **CC-BY-NC [expl]**) — the GitHub repo
  `github.com/wayne391/lead-sheet-dataset` ships only a **sample**, and its README's **4.9 GB Google Drive link is
  DEAD** (404 / privatized; every research mirror points back to the same dead id — CC-verified 2026-06-30). The 2018
  crawler is also dead (Hooktheory is now a gated SPA). **Live route (gated, pending HF approval): the HuggingFace
  dataset `m-a-p/HookTheory`** (CC-BY-NC-4.0) — the symbolic harmony is just `Hooktheory.json.gz` (~20 MB) +
  `Hooktheory_Raw.json.gz` (~96 MB) + the Key/Structure `.jsonl` splits (audio is separate 112 GB, skip). Needs the
  user's HF token; download via `huggingface-cli` into `corpora/expl/`. Layout is m-a-p keyed-JSON (parse directly,
  not the wayne391 `event/` tree). Provenance: memory `project_hlsd_full_pending_hf`; **POP909** `github.com/music-x-lab/POP909-Dataset` (MIDI + chord `.txt`; verify LICENSE).
- **Folk — Nottingham**: `github.com/jukedeck/nottingham-dataset` (~1,200, cleaned ABC melody+chords — good harmonic
  content); **thesession.org** `github.com/adactio/TheSession-data` (ABC/JSON/CSV, **ODbL**; *caveat: largely
  melody-only → thin harmony, mostly excluded by the melody-only rule*).
- **Method reference (not a corpus) — lda_tpcs**: `github.com/DCMLab/lda_tpcs` (**MIT** — Moss's notebook to adapt).
- **Broad, unannotated:** Lakh MIDI (~176k, genre-mixed); Wikifonia (~6k lead sheets, copyright-encumbered).

**Minimum viable cross-tradition set:** ChoCo + McGill Billboard (CC0) + DCML + JHT — spans classical/jazz/pop with a
shippable core (McGill Billboard + ChoCo CC-BY parts) and NC corpora reserved for exploration. Folk is the weak link
(Nottingham has chords; thesession is thin). **Acquisition note (2026-06-30):** single text-file datasets (JHT, the
ABC files) are `web_fetch`-able into `C:\s\MS\corpora\` directly; multi-file repos (ChoCo, DCML, POP909) and binary
zips (McGill `.lab` archive, Zenodo) are not — those are `git clone` / Zenodo-download by the user.

## 4a. Already on disk in the repo — `tools/` (do NOT re-download; see `docs/score_inventory.md`)
The project already holds a large corpus pile, gitignored under `tools/`. It roughly **doubles the classical coverage
and adds jazz / tango / sophisticated-pop** beyond the §4 downloads, and is the discovery's **second corpus root**
alongside `corpora/`:
- **DCML RN-annotated (`tools/dcml/<repo>/`, ~1,700 scores, 12 repos — the primary classical base, [expl] NC):**
  bach_chorales **361**, corelli **149** (Baroque), bach_en_fr_suites **89**, ABC/Beethoven-quartets **71**,
  cpe_bach_keyboard **66** (galant), grieg **66**, mozart **58**, chopin **56**, schumann **13**, dvorak **12**,
  tchaikovsky **12**, **when_in_rome 762** (mixed common-practice anthology). Each has `MS3/` scores + `harmonies/`
  RN+key+cadence TSV. **★ This makes most of the `corpora/expl/` DCML re-clones redundant** (mozart, beethoven=ABC,
  romantic=chopin/grieg/schumann/dvorak/tchaikovsky) — use `tools/dcml` as the classical base (richer: it also has
  Bach chorales, Corelli, CPE galant, WiR); `corpora/expl/dcml_scarlatti` is the only genuinely-new DCML clone.
- **music21 Bach chorales (`tools/corpus/`, 353 BWV + music21 RN GT, [expl]):** the BIR gate corpus — overlapping the
  chorale repertoire but a distinct selection/identifier set (do **not** treat as super/subset of `bach_chorales/`).
- **Jazz / non-classical (`tools/`):** Effendi Real Book lead sheets (`corpus_effendi_src/`); Charlie Parker
  **Omnibook** bebop (`corpus_omnibook_src/`); 36 big-band MXL (`corpus_rampageswing_full/`); PDMX many-genre sample
  (`pdmx/spot_check/`). No RN GT — usable for the *discovery* (clustering needs no GT), not for validation.
- **Curated `tools/extra scores/`** (quote the space; `ground_truth:false`): Hiromi Uehara ×20 (jazz piano),
  **Steely Dan**, **Piazzolla** (tango) — small but idiom-interesting for the genre-vs-something-else read.

So the discovery reads **two roots**: `corpora/` (new) **and** `tools/` (existing). Per `score_inventory.md` Hard rules:
read-only; do **not** modify the catalog or the 11 snapshot sources; treat `tools/dcml`, `tools/corpus`, and
`corpora/expl/` as **[expl]** unless separately permissive.

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
