# Harmonic idiom discovery — v1 empirical findings

> **Status: v1 results (2026-06-30), from the `idiom_discovery/` pipeline.** First cross-tradition run; preliminary
> and evolving (3 traditions, symbolic chord sources, will grow as folk + note-level + more sources are added). Method
> and contract: `cowork_idiom_discovery_design.md`. These are the **discover → then name** outputs (spec §2/§6); the
> idiom names are a post-hoc reading of the cluster signatures, not labels given to the algorithm.

## Corpus (this run)
Balanced 500 pieces/tradition from: **classical** = DCML (Scarlatti/Mozart/Beethoven/Romantics) + Corelli (Baroque);
**jazz** = Jazz Harmony Treebank (1,170) + ChoCo `real-book` (2,846); **pop** = McGill Billboard (890) + ChoCo
`isophonics`. Encoding: key-normalized **line-of-fifths root + canonical quality** transition tokens (`1:dom7>0:maj`
= V7→I); LDA(12 topics) → KMeans; the source-leakage / tradition-ARI confound test.

## Findings

**1. Natural granularity ≈ 4–5 clusters, and the structure is robust (not a single-seed anecdote).** Across 5 KMeans
seeds: tradition-ARI **0.349 ± 0.000** at K=4, self-stability **1.000**; stable through K=5 (0.342, 0.999); degrades
past K=5 (K=6: 0.271 ± 0.023, self 0.900).

**2. Genre is only a *moderate, partial* organizer — and weakened as the corpus grew.** Tradition-ARI ≈ **0.35**
(K=4), down from a 0.41 single-seed first pass once more sources + Baroque were added. Harmony is *not* cleanly
partitioned by tradition.

**3. ~85% of the genre signal is in the *progressions*, not chord quality.** Stripping quality and clustering on
**root motion alone** (vocab 1347 → 226) drops ARI only 0.35 → 0.30. It is real progression idiom, not a
chord-spelling artifact.

**4. The emergent idioms are harmonic-structural, and several cut across genre.** At K=5 (stable), the five clusters,
named from their characteristic transitions:

| Idiom (named post-hoc) | Tradition mix | Signature transitions |
|---|---|---|
| **Triadic diatonic / modal core** | pop 71 · cl 18 · jz 11 | IV–I, I–IV, V–I, **♭VII–IV / I–♭VII** (mixolydian planing) |
| **Functional tonal, major** | cl 66 · jz 18 · pop 16 | V7–I, I–ii, **applied/secondary diminished** (viio7/x), viio–I |
| **Jazz ii–V–I / circle-of-fifths** | jz 88 · pop 11 | ii7–V7–Imaj7, descending ii–V chains, backdoor V7→maj7 |
| **Blues / chromatic-dominant & static-7ths** | pop 56 · jz 44 | ♭VII7–I7, planing dom7/min7 (lift ×16–19 — very distinctive) |
| **Functional tonal, minor** | cl 83 · pop 12 · jz 5 | V7–i, i–iv, iiø7–i, aug6 region |

## What it means
The axes the music actually clusters on are **not genre**. They are: **(a) chord-vocabulary complexity** (triadic →
functional+applied → jazz sevenths), **(b) mode** — the "classical" mass splits into *major-functional* vs
*minor-functional*, **not** by composer or era — and **(c) diatonic vs blues/chromatic**. Genre only partially rides
along: the jazz ii–V idiom ≈ jazz, but the triadic-modal core and the blues-dominant idiom **cut across** genre. So
the idioms we "really need" look closer to **{triadic-modal, functional-major, functional-minor, jazz-sevenths,
blues-chromatic}** than to **{Baroque, Jazz, Pop}** — the first empirical footing for the §12.1 taxonomy / StyleTag
decision (which we had deliberately deferred to exactly this).

## Caveats / next
Three traditions only (no folk yet); symbolic chord sources only (no note-level Bach/voice-leading idiom yet); K=5 is
one defensible cut (K=4 merges the two functional idioms + folds in blues); LDA config fixed (12 topics); the names
are interpretive. **Next:** add folk (Nottingham) and note-level Bach chorales (via chordify — also the
music21↔L1/L2 neutral-extractor cross-check, a build task), then re-derive — does a folk idiom and a Baroque
voice-leading idiom split off? Pipeline: `idiom_discovery/` (model + parsers + extract + discover).

## v1.1 — folk + note-level Bach added (2026-06-30)
Added **folk** (ChoCo Nottingham, 1,002 tunes, via the m21-symbol reader) and **note-level Bach** (40 chorales via
music21 `chordify` — the neutral mechanical path, *not* our analyzer). 4-tradition balanced run (400 each):
- **Genre weakened further:** tradition-ARI **0.25 (K=5) / 0.29 (K=6)** — adding folk lowered it again. Genre keeps
  shrinking as an organizer as more traditions enter.
- **Folk is NOT a distinct idiom.** Nottingham collapses ~70% into a single **"simple diatonic V7" idiom** (I–V7,
  ii–V, secondary dominants) that it **shares most with classical, not pop** — folk ≈ a *simplified common-practice
  functional* harmony, not its own category.
- **Bach forms no distinct chord-idiom.** The chordified chorales spread across the minor-functional / triadic /
  chromatic clusters rather than grouping together — consistent with the spec's premise that chorale "Baroque-ness"
  lives in **voice-leading, a separate dimension**, not in the chord-progression skeleton (modulo chordify
  passing-tone noise on only 40 chorales).
- Net: the structural axes (vocabulary-complexity · mode · diatonic-vs-chromatic) hold; genre keeps *not* being the
  organizer. **The music21↔L1/L2 neutral-extractor cross-check (spec D6) remains a build task** (needs the C++
  analyzer) — flagged for CC.

## v1.2 — vocabulary (tonal-profile) second view (2026-06-30)
Ran Moss's axis — key-normalized **line-of-fifths chord-tone histograms** per piece — as an independent lens on the
4-tradition corpus, to cross-check the progression-based idioms (spec §2a, two views):
- **Vocabulary tracks genre even *less*:** tradition-ARI **0.17** (vs the progression view's 0.29). Pitch-class
  *content* is broadly shared — most traditions sit in the **diatonic-major collection** (profile mass at fifths
  −1..+5); the view mainly separates major from **flat-side/modal** (one mixed pop/folk/jazz cluster) and
  **chromatic/minor classical**. This **replicates Moss** ("topics = diatonic-set regions on the line of fifths") —
  now on cross-tradition data.
- **The two views only weakly agree** (progression ↔ vocabulary ARI **0.22**) → genuinely *complementary*, not
  redundant (validates running both).
- **Sharpened conclusion: idiom lives in the *progressions*, not the vocabulary.** The pitch-class vocabulary is a
  shared diatonic substrate across traditions; what differs by idiom is how the chords *move*. So the data-derived
  idiom set is a **progression** taxonomy, with the tonal-profile (major/modal/chromatic) as an orthogonal second axis.

## v1.3 — full-coverage symbolic run (5,041 pieces, 2026-06-30)
`build_full.py` (FAST/symbolic: every chord-symbol source — DCML incl. **CPE galant + Bach suites**, JHT, ChoCo
real-book, McGill, isophonics, Nottingham; ChoCo `ireal-pro` raw excluded). 5,041 pieces parsed in **17 s**;
tradition-ARI **0.324** (K=6). **Six idioms:** (1) blues/chromatic-dominant *(jazz∩pop)*; (2) common-practice
functional + applied-dim/aug6 *(classical)*; (3) simple diatonic-V7 *(folk)*; (4) triadic core / pop-rock *(pop)*;
(5) jazz ii–V–I sevenths *(jazz)*; (6) **modal / static-7th jazz** *(jazz)* — a second jazz idiom the larger corpus
split out (ii–V functional vs modal planing).

**★ Key new finding — Baroque, galant, and Classical share ONE harmonic idiom.** Scarlatti, Corelli, Bach suites,
CPE Bach (galant), and Mozart ALL land **~95–100% in the same cluster** (the functional + applied-diminished/aug6
idiom). There is **no separate Baroque or galant progression-idiom** — ~200 years of common-practice share one
harmonic idiom; the era differences live in texture / rhythm / voice-leading / form, **not** the chord-progression
vocabulary. Strongly reinforces: era/genre is not the organizing axis.

**Cost (measured):** symbolic full-coverage = 17 s / 5k pieces; **chordify is the driver** (~0.3 s/chorale but ~5 s
per large arrangement, and voicing-noisy). A full run incl. note-level (Bach + `.xml`/curated) is **~10 min**, best on
the user's machine (no sandbox cap). `build_full.py` auto-includes the curated `.mxl` once CC converts them.

## v1.4 — the curated-scores probe (Steely Dan / Piazzolla / Hiromi, 2026-06-30)
Chordified 22 of the 49 curated full-arrangement scores (all three sets represented) and projected them into the
six-idiom space (c0 blues/chromatic-dom · c1 common-practice functional · c2 simple-V7 folk · c3 triadic-pop · c4 jazz
ii–V · c5 modal/static-7th jazz). Where they land:
- **steely_dan** → c0 (blues-chromatic) 64% · c5 (modal-7th) 27% · c1 9%
- **piazzolla**  → c0 50% · c5 33% · c1 (classical-functional) 17%
- **hiromi**     → c5 40% · c0 40% · c3 (pop-triadic) 20%

**★ The sophisticated scores land in the *cross-cutting chromatic/modal* idioms (c0, c5) — not the clean ones
(jazz ii–V, pop-triadic, classical-functional).** This is musically correct and non-obvious: Steely Dan reads as
chromatic-dominant + modal-7th, **not** textbook ii–V bebop; Piazzolla (tango) and Hiromi (fusion) likewise
congregate in the chromatic/modal region despite nominal pop/tango/jazz labels. Two conclusions: (a) it **validates
the idiom set** — a naive genre tag would mis-place these; the *harmony* places them correctly; and (b)
harmonically sophisticated, genre-defying music does **not** form a new idiom — it is **heavier use of the existing
cross-cutting chromatic/modal idioms**. The cross-cutting clusters flagged early as "the something-else, not genre"
are exactly where this music lives. *Caveats: 22/49 (chordify slow on full arrangements; rest drainable),
voicing-noise on dense chordify, 5 force-converted scores.*

## v1.5 — FINAL: full balanced run + cap-robustness (CC, on the user's machine, 2026-06-30)
Full run (9.4 min, up to 5,243 pieces), cap-robustness sweep at per-source caps **400 / 700 / 1200**:
- **★ ROBUST — not an artifact of the balancing knob.** Tradition-ARI stays in a tight **0.26–0.33** band across all
  three caps (no collapse, no runaway), and the **same ~5 idioms recur at every cap** (cluster indices shuffle, idiom
  *content* is constant). The robust set:
  1. **Jazz ii–V–I / maj7** (90–98% jazz)
  2. **Classical chromatic — dim7 / aug6** (76–93% classical)
  3. **Folk dom7-cadential** (72–78% folk)
  4. **Pop sus / major-shift** (67–73% pop)
  5. **Cross-cutting chromatic/modal** (mixed — *no* dominant tradition)
  A 6th cluster (a secondary-jazz split, maj7↔dom7) **wobbles** between caps — the only non-robust one; the
  modal/static-7th sub-distinction does **not** survive the robustness check, so the defensible set is **five**.
- **★ Curated probe (47/49) — all three converge on ONE shared idiom.** Steely Dan, Piazzolla, *and* Hiromi all
  collapse into the **single cross-cutting chromatic/modal idiom** (#5), away from the tradition-pure clusters. Three
  harmonically dense, genre-defying corpora occupy one common idiom. (2 degenerate scores dropped; per CC the probe
  refits an independent KMeans, so the finding is the *convergence*, not the cluster index.)

**Final empirical conclusion.** The data-derived idiom set is **five robust progression idioms** — four
tradition-leaning (jazz ii–V, classical chromatic-functional, folk dom7-cadential, pop sus/triadic) **plus one
cross-cutting chromatic/modal idiom** — with **mode and chromaticism as cross-axes**. Genre is a weak organizer
(ARI ≈ 0.3, robust); harmonically sophisticated music shares the single cross-cutting idiom. This is the validated
footing for the taxonomy / StyleTag decision (see `cowork_style_taxonomy_proposal.md`).

## v1.6 — FINAL expanded run: all sources, the two open questions resolved (CC, 2026-06-30)
9,427 pieces at the top cap; cap-robustness 400/700/1200; now including ChoCo **weimar + jaah + jazz-corpus +
wikifonia**, **Impro-Visor** (2,603 modal-jazz leadsheets), and **Chordonomicon** (chromatic pop, capped from
99,913). All six new sources loaded nonzero.
- **Cap-robust, and genre weaker still:** ARI **0.166 / 0.184 / 0.163** across caps — *lower* than before, because more
  diverse sources make the clusters cut across tradition even more (idioms ≠ genres). The same ~5 idioms recur at every
  cap (jazz ii–V seventh-chain · pop diatonic maj/min shuttle · folk dom7-cadential · classical minor/diminished
  functional · the cross-cutting chromatic/modal idiom).
- **★ The wobbly 6th does NOT firm up — resolved as "not a separable idiom."** Even with targeted modal jazz added
  (weimar 429 + Impro-Visor 2,603), **no stable modal/static-7th sixth cluster appears at any cap** — the modal-jazz
  mass is absorbed into the jazz ii–V / min7 clusters. So the committed set is **five**; the modal/static distinction
  is below the resolution of the progression-transition representation at K=6 (it would need a higher K or an explicit
  static-harmony/sus feature — a future refinement, not a committed idiom).
- **★ Idiom #5 stays ONE — confirmed unified.** The cross-cutting chromatic/modal idiom persists at every cap
  (balanced tri-tradition, e.g. jazz 34 / pop 33 / classical 31 at cap-400); adding Chordonomicon + modal jazz
  **reinforced** it rather than splitting it into chromatic-jazz / impressionist / blues sub-idioms.
- **★ Curated probe (full 47):** Steely Dan **100%** / Piazzolla **83%** / Hiromi **100%** all converge on the single
  cross-cutting cluster — three sophisticated artists, three traditions, one idiom: the strongest evidence yet for #5.

**FINAL conclusion (empirical phase complete).** Five robust progression idioms — **jazz-seventh, pop-triadic,
folk-V7, classical-functional, and cross-cutting chromatic/modal** — with **mode and chromaticism as cross-axes**.
Genre is a weak organizer (ARI ≈ 0.16, robust, and weakening as coverage grows). Idiom #5 is the home of harmonically
sophisticated, genre-defying music. The candidate sixth (modal/static jazz) is real musically but not separable at
this resolution — deferred to a higher-K / static-feature study. This is the final footing for the *harmonic* taxonomy.

## Voice-leading — is it a separate axis? PILOT: YES (2026-06-30)
Built a voice-leading feature extractor (`parsers/voiceleading.py`): per-voice melodic-interval profile — the
`|interval|` histogram + repeat/step/leap rates — on **note-level sources only** (the harmonic study's lead-sheet
sources have no voices). Pilot: **60 Bach chorales** (music21, SATB) vs **193 DCML piano movements**
(Mozart/Beethoven/Scarlatti, via the `notes/` TSVs).
- **★ Voice-leading is a STRONG axis.** The unsupervised VL clustering recovers the chorale/piano distinction at
  **ARI 0.683** — *far* cleaner than harmony recovered genre (≈0.16–0.3). The profiles are starkly different:
  **chorale 65% stepwise / 21% leaps; piano 40% stepwise / 49% leaps.**
- **★ The chorale prediction holds.** Chorales — which *refused* to form a harmonic idiom (they scattered across the
  functional clusters) — separate **tightly** by voice-leading. A chorale's identity is its stepwise SATB
  part-writing, **not** its chords, exactly as predicted.
- **★ Implication: a SEPARATE, ORTHOGONAL axis.** Pieces that are one thing harmonically split by voice-leading, and
  vice-versa. So the full structure is **≥ 2-D: (harmonic idiom, voice-leading idiom) + mode + chromaticism.**
- **Scope:** note-level only (classical / chorale / arrangement). Lead-sheet jazz/pop have no voices, so the
  voice-leading axis is a **notated-music** axis — different coverage from the cross-tradition harmonic axis.

**Verdict:** the axis question is answered — voice-leading is a real, strong, orthogonal organizing axis; the spec's
**voice-leading layer is warranted.** The fuller follow-on (not the axis question, which is settled) would discover the
voice-leading *idioms* (beyond chorale-vs-piano — contrapuntal/fugal, pianistic, jazz-comping…) and run a formal
orthogonality test (cross-ARI of VL vs harmonic clusters on the same pieces).

## v2.0 — the AXIS-2 STUDY: VL idioms discovered + orthogonality formally measured (CC, 2026-07-03; ratified)
The fuller follow-on ran at full note-level coverage — **2,102 pieces / 45 sources** (41 DCML/DLC `notes/` corpora
1,687 · full music21 4-part chorales 368 · the 47 curated arrangements at note level per notated (staff,voice), NOT
chordify; `corpora/expl/dcml_*` dedup-verified as clones of `tools/dcml/` and excluded). Two low-level views:
**View A** = the pilot's per-voice |interval| histogram (unchanged — pilot reproduces byte-for-byte, a strict
subset) · **View B (new)** = **voice-pair motion-type rates** (parallel/similar/contrary/oblique — pure interval
arithmetic). Full record: `cc_vl_idiom_discovery_report.md`; pipeline `idiom_discovery/parsers/voiceleading2.py` +
`run_vl_discovery.py` / `run_vl_orthogonality.py`.
- **★ VL organizes by TEXTURE, not corpus or instrumentation.** Confound gate: VL-cluster ARI vs voice-count
  **0.034–0.046** (the instrumentation worry — decisively absent) and vs source **0.07–0.11** (not bookkeeping);
  vs **texture 0.32** (View B's top covariate). The texture/era covariates are declared per-source interpretation
  lenses, post-hoc only, never clustering input (spec §6 discipline — Cowork-verified at the lens maps).
- **★ The discriminative feature is HOW VOICES MOVE TOGETHER, not interval size** — the VL analogue of the harmonic
  study's root-motion-alone result. Ablation: View B alone recovers texture at **0.37–0.46** (self-stability
  0.98–1.00); View A alone ≤0.20; raw A+B dilutes B (16 dims outvote 4); z-scoring partly recovers (0.33).
- **★ The robust VL idioms:** **contrapuntal part-writing** (stepwise, contrary/similar motion — Bach chorales +
  Renaissance sacred + Baroque trio-sonata, across era) **vs homophonic melody+accompaniment** (oblique-dominant),
  natural K=2–3; the interpretable K=4 refines the homophonic mass along View A's era-correlated melodic-complexity
  sub-axis into **classical-keyboard figuration** vs **romantic/virtuosic pianistic** (+ a moderate/mixed
  early-music cluster). Caveat honored: View A's era signal is partly a chord-explosion artifact — the primary
  finding rests on View B, which never explodes chords and still groups exploded chamber corpora (Corelli, Couperin)
  WITH the chorales, ruling out an encoding artifact.
- **★ ORTHOGONALITY FORMALLY CONFIRMED: cross-ARI(VL, harmonic) = 0.030** on the 1,283 pieces carrying both views —
  statistical independence; the contingency table ≈ product of marginals. Harmonic clusters are ~texture-invariant
  (0.024) while VL tracks texture — two independent partitions of the same music. **The full style structure is
  ≥ 2-D: (harmonic idiom) ⟂ (voice-leading idiom) + mode + chromaticism.**
- **★ Both predicted probes confirm:** the curated sophisticates (SD/Piazzolla/Hiromi — ONE harmonic idiom, v1.6)
  **split by voice-leading** (Hiromi dense-pianistic, Piazzolla apart, SD spread; all oblique-dominant by the
  declared top-note reduction, the split riding the melodic sub-axis); the Bach chorales (harmonically scattered,
  v1/v1.1) are **98% VL-tight** — and the two independent chorale encodings (music21 vs DCML TSV) agreeing 98%/98%
  is a bonus extraction-robustness cross-check.
- **Footing for the voice-leading layer spec:** a **motion-type-led** feature set (parallel/similar/contrary/oblique)
  as the primary discriminator, the interval profile as a secondary melodic-complexity descriptor, and a texture
  taxonomy of **{contrapuntal, homophonic-classical, homophonic-pianistic, moderate/mixed}**; coverage is
  notated-music only (lead sheets have no voices). Levers recorded for their proper layers (not coded): a
  motion-type/static-harmony feature as the natural home of the deferred modal/static-jazz "wobbly sixth" (v1.6);
  a uniform per-source note-reduction rule to retire View A's explosion asymmetry. (Pilot-number note: the 0.683
  headline reads 0.595 under this machine's sklearn — feature matrix provably identical; KMeans-init drift only.
  At full coverage the split strengthens to 0.821.)
