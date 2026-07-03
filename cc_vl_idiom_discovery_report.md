# Voice-leading idiom discovery — the axis-2 study (CC, 2026-07-03)

> **Read-only research/measurement increment.** Python pipeline only — **no `src/` change, no build, no
> gate-corpus touch. The BIR gate is untouched by construction**: this pipeline reads note-level TSVs / scores
> and clusters feature vectors; it never runs the C++ analyzer and never writes any corpus, so no regen is
> needed and no gate number can move. Method contract: `cowork_idiom_discovery_design.md` (discover → then
> name; confound gate first-class; no theory features in the encoding). Follow-on to the pilot verdict in
> `cowork_idiom_discovery_findings.md` §"Voice-leading — is it a separate axis? PILOT: YES". The axis question
> (is VL a separate axis) was already answered YES and is **not** re-litigated here; this study answers the two
> fuller questions the pilot warranted: **(1) what are the VL idioms**, and **(2) the formal orthogonality test**.

## TL;DR

1. **Voice-leading organizes by *texture*, not by corpus or instrumentation.** The confound gate is decisive: the
   VL clustering's ARI vs **voice-count is 0.037** and vs **source is 0.07** (near-zero — *not* the "4 voices vs
   2 staves" instrumentation confound, *not* bookkeeping), while vs **texture it is 0.32** and vs **era 0.13–0.29**.
2. **The discriminative VL feature is *how voices move together* (motion type), not raw melodic-interval size.**
   Ablation: **View B (voice-pair motion-type rates) alone recovers texture at ARI 0.37–0.46**; **View A (the
   pilot's interval histogram) alone only 0.15–0.20**. This is the VL analogue of the harmonic study's
   "root-motion-alone" finding (v1 §3).
3. **The two robust VL idioms are contrapuntal part-writing vs homophonic melody+accompaniment**, cutting across
   era (Baroque chorales + Renaissance sacred + Baroque trio-sonata all land contrapuntal; solo-keyboard sonatas
   of every era land homophonic). View A adds a second, era-correlated melodic-complexity sub-axis
   (stepwise → leapy/pianistic).
4. **The formal orthogonality test passes: cross-ARI(VL clusters, harmonic clusters) = 0.030** on the 1,283
   pieces carrying both views. Voice-leading and harmony partition the same music **independently** — the full
   structure is confirmed **≥ 2-D**.
5. **The two predicted probes both confirm:** the curated sophisticates (Steely Dan / Piazzolla / Hiromi — *one*
   harmonic idiom per v1.6) **split by voice-leading**; the Bach chorales (harmonically *scattered* per v1/v1.1)
   are **98% VL-tight**.

---

## 1. Coverage (Task 1) — enumerated and declared

**Canonical DCML/DLC source = `tools/dcml/`** (41 corpora that carry `notes/*.tsv`). The `corpora/expl/dcml_*`
dirs were **dedup-verified as clones** of `tools/dcml/` corpora and **excluded** (byte-identical `dcml_scarlatti`
≡ `scarlatti_sonatas`; `dcml_mozart` ≡ `mozart_piano_sonatas`; `dcml_beethoven` ≡ `ABC` = the Annotated Beethoven
Corpus string quartets, same `n01op18-1…` naming; `dcml_romantic/*` all present under `tools/dcml/`). `when_in_rome`
carries no `notes/` and is excluded. Total **2,102 pieces / 45 sources**:

| Family | Sources | Pieces | View-A usable | View-B usable |
|---|---|---|---|---|
| (a) DCML/DLC note corpora | 41 | 1,687 | 1,687 | 1,663 |
| (b) music21 4-part Bach chorales (full; pilot `limit=60` dropped) | 1 (`m21_chorale`) | 368 | 368 | 368 |
| (c) curated arrangements, **note level per (staff,voice), NOT chordify** | 3 (`steely_dan` 22 · `piazzolla` 6 · `hiromi` 19) | 47 | 47 | 47 |

Per-corpus DCML counts (pieces): `bach_chorales` 361, `corelli` 149, `beethoven_piano_sonatas` 91,
`couperin_concerts` 91, `bach_en_fr_suites` 89, `ABC` 70, `scarlatti_sonatas` 69, `bach_solo` 68, `cpe_bach_keyboard`
66, `grieg_lyric_pieces` 66, `kleine_geistliche_konzerte` 56, `chopin_mazurkas` 56, `mozart_piano_sonatas` 54,
`kozeluh_sonatas` 49, `frescobaldi_fiori_musicali` 47, `jc_bach_sonatas` 29, `mendelssohn_quartets` 24,
`schubert_winterreise` 24, `rachmaninoff_piano` 22, `liszt_pelerinage`/`medtner_tales`/`monteverdi_madrigals` 19 each,
and a long tail of ≤14 (full list in `idiom_discovery/vl_discovery_out.txt`). `bach_solo`'s View-B coverage is
partial (44/68) — solo violin/cello has few concurrent voices, so motion-type is often undefined (correct behavior).

**Declared limitation (stated, not solved):** we read **notated** voices only. Implied polyphony / compound melody
in a single notated voice reads as leapy; that is a property of the representation, recorded here, not corrected by
any inference (its own future task — `cowork_polyphony_phrase_harmony_research.md`). Concretely, the curated
arrangements were reduced **chord → top (melody) note per notated voice** (declared; differs from the DCML branch,
which explodes chord tones per the pilot — see §6 caveat), and their many notated voice-layers (9–20) make their
View-B strongly oblique-dominant.

**Bach-chorale near-duplication (declared, and turned into a cross-check).** The DCML `bach_chorales` (361, note-only,
no `harmonies/`) and the music21 `m21_chorale` set (368) are two encodings of substantially the **same** repertoire.
Rather than drop one, both are kept as **distinct sources** — the confound test then reveals whether two independent
encodings of the same music land in the same VL idiom. They do (98% / 98% into the same cluster — §5), which is a
bonus extraction-robustness result. Caps (below) prevent the ~720 combined chorales from dominating.

---

## 2. Method — two feature views (Task 2)

- **View A (baseline — the pilot's, UNCHANGED).** Per-piece per-voice `|melodic interval|` histogram (bins 0–11,
  ≥12) + repeat/step/leap rates = 16 dims. The pilot's `vl_profile` is imported and reused verbatim; **View-A
  vectors reproduce the pilot byte-for-byte** (verified 69/69 identical on `scarlatti_sonatas`; the full pilot
  subset reproduces exactly — 60 chorale / 193 "piano" pieces, profiles 65%/21% chorale vs 40%/49% keyboard). So
  the pilot is a strict subset.
- **View B (new).** **Voice-pair motion-type rates** = 4 dims `[parallel, similar, contrary, oblique]`, pure
  interval arithmetic, no theory labels. **Simultaneity rule (as implemented):** for each concurrent voice pair,
  sample at the merged sorted set of the two voices' note onsets; a voice's pitch at a sample is its most recent
  onset ≤ t (piecewise-constant hold); classify motion between consecutive samples (dropping samples where neither
  voice moves); aggregate rates over all voice pairs. `parallel` = same direction with the harmonic interval
  preserved; `similar` = same direction, interval changes; `contrary` = opposite; `oblique` = exactly one voice
  moves. View B reduces each onset to a single top pitch, so — unlike View A — it does **not** explode chords
  (making it the extraction-clean view; see §6).
- **A+B** = the 20-dim concatenation, run both raw (`AB`) and z-scored (`ABz`, giving View B's 4 dims weight equal
  to View A's 16).

Portability (Task 0): `parsers/voiceleading.py`'s `__main__` no longer hardcodes the sandbox path — the corpus root
is now `argv[1] > $VL_CORPUS_ROOT > repo-root-from-__file__`. `vl_profile` / `load_chorales_vl` / `load_dcml_notes_vl`
are untouched, so the baseline stays reproducible.

> **Note on the pilot's 0.683 headline.** Re-run here the pilot's *feature vectors* are byte-identical (piece counts
> and mean profiles match exactly), but the reported ARI reads **0.595** rather than 0.683. Because the matrix is
> provably identical, the shift is entirely `sklearn`'s KMeans changing between the sandbox and this machine
> (sklearn 1.9.0), **not** the encoding. The qualitative result is unchanged and in fact strengthens at full
> coverage (§3).

---

## 3. Discovery + confound gate (Task 3)

**Full-coverage pilot replication (View A, KMeans-2):** chorale (368) vs keyboard/quartet (193) → **ARI 0.821**
(chorale 64% step / 21% leap; keyboard 40% / 49%) — *cleaner* than the pilot's 60-chorale 0.683, as predicted.

**Stability sweep** — K ∈ {2…8} × 5 seeds × per-source caps {40, 80, 150}. Reference partition for the recovery
column = `texture`. (Full tables: `vl_discovery_out.txt`.) Representative rows at **cap=150**:

| view | K=2 | K=3 | K=4 | K=5 | K=6 | self-stab (K=3) |
|---|---|---|---|---|---|---|
| **A** (intervals) | 0.165 | 0.184 | 0.179 | 0.195 | 0.167 | 1.000 |
| **B** (motion type) | 0.403 | **0.458** | 0.372 | 0.363 | 0.323 | 0.982 |
| **AB** (raw) | 0.254 | 0.267 | 0.227 | 0.263 | 0.302 | 0.997 |
| **ABz** (z-scored) | 0.252 | 0.333 | 0.272 | 0.268 | 0.298 | 0.999 |

Numbers are texture-recovery ARI (mean over 5 seeds; sd ≤ 0.01 throughout — highly stable). **Ablation verdict:**
View B alone carries the texture structure (peak **0.46** at K=3, perfect/near-perfect self-stability); View A alone
is weak (≤0.20); **raw A+B dilutes View B** because View A's 16 dims outvote View B's 4 by count; z-scoring
recovers part of it (0.33). So **the discriminative VL feature is voice-pair motion type, not interval size** —
the analogue of the harmonic study's root-motion-alone result. **Natural granularity:** View B is robust at **K=2–3**
(a coarse contrapuntal/homophonic split; texture-ARI peaks, self-stab = 1.000) and degrades past K=5; the
interpretable finer cut is **K=4** (below).

**Confound gate** (K=4, cap=80) — ARI / AMI of the VL clusters against each covariate. (The harmonic study's
"tradition" {classical/jazz/pop/folk} is near-constant on this axis — coverage is notated-music, ≈all classical
plus 47 arrangements — so the relevant grouping covariate is **texture**; source/era/voice-count/length are the
bookkeeping/instrumentation confounds the gate must clear.)

| covariate | View A | View B | View AB |
|---|---|---|---|
| **source** (the leakage label) | 0.096 / 0.284 | **0.073** / 0.232 | 0.105 / 0.304 |
| **texture** | 0.154 / 0.229 | **0.321** / 0.314 | 0.184 / 0.268 |
| **era** | **0.285** / 0.291 | 0.133 / 0.169 | 0.264 / 0.310 |
| **voice-count** | 0.046 / 0.051 | **0.037** / 0.086 | 0.034 / 0.066 |
| **piece-length** | 0.131 / 0.135 | 0.091 / 0.121 | 0.120 / 0.147 |

**Readings.**
- **The instrumentation confound is decisively absent.** Voice-count ARI is **0.034–0.046** across all views —
  the VL clustering is *not* "4 voices vs 2 staves." (This directly answers the instruction's explicit worry.)
- **Not bookkeeping.** Source ARI 0.07–0.11 (low) — the clusters are not a re-discovery of which corpus a piece
  came from.
- **View B = the texture axis** (0.32, its top covariate). **View A = an era / melodic-complexity axis** (era
  0.285 > its texture 0.154): melodic language became leapier and wider-ranged over historical time, so the
  interval histogram recovers era. *Caveat (§6): View A's era signal is partly a chordal-density/explosion artifact
  (later-era keyboard is denser → more exploded chord tones → more "leaps"); View B, which never explodes chords,
  tracks era only weakly (0.133), so the clean, extraction-robust axis is View B's texture split.*
- **Length is not the organizer** (0.09–0.13); the rate features are length-normalized by construction.

**Idiom table** (View AB, K=4, cap=80 — cluster → texture/source mix → elevated/low features → post-hoc name):

| cluster | n | texture mix | top sources | signature (Δ vs corpus mean) | post-hoc name |
|---|---|---|---|---|---|
| **c3** | 325 | chorale 155 · chamber 118 · kbd 35 | m21_chorale 79 · bach_chorales 76 · couperin_concerts 58 · corelli 56 | **+step .21 +P\|iv\|=2 .14 +contrary .11 +similar .08**; −oblique .23 −leap .21 | **Contrapuntal part-writing** (stepwise, contrary/similar motion) |
| **c0** | 360 | kbd 154 · chamber 114 · vocal 67 | ABC 53 · bach_en_fr_suites 50 · kleine_geistliche_konzerte 39 · frescobaldi 35 | +step .08 +repeat .07 +P\|iv\|=0 .07; −leap .15 | **Moderate/mixed** (early-music, sacred vocal, ensemble — restrained motion) |
| **c2** | 395 | kbd 325 · chamber 27 · arr 22 | mozart 49 · scarlatti 45 · cpe_bach 42 · kozeluh 34 | +oblique .10 +leap .08 +P\|iv\|=3 .03 | **Classical keyboard figuration** (homophonic, moderate leap) |
| **c1** | 329 | kbd 280 · vocal 42 | beethoven_sonatas 49 · grieg 49 · chopin 37 · schubert 19 | **+leap .28 +oblique .08 +P\|iv\|≥12 .07**; −step .23 −P\|iv\|=2 .14 | **Romantic / virtuosic pianistic** (leapy, wide-range, homophonic) |

The four clusters instantiate a **2-sub-axis** structure: **motion-type** (c3 contrapuntal ↔ c1/c2 homophonic; the
View-B axis) × **melodic-interval complexity** (c0/c3 stepwise ↔ c2 → c1 increasingly leapy; the View-A/era axis).
The View-B-only table makes the first axis explicit: cluster **c1_B** = chorale (m21 71 · bach 69) with
**+contrary .14 +similar .10, −oblique .28** (independent SATB part-writing); cluster **c2_B** = solo keyboard
(beethoven/cpe/mozart/kozeluh) with **+oblique .15** (melody-over-accompaniment). Crucially, corelli and
couperin_concerts (multi-voice chamber, *exploded* like keyboard in View A) group **with** the chorales in the
contrapuntal cluster — so the split is genuine texture, not a chorale-encoding artifact (§6).

---

## 4. The formal orthogonality test (Task 4)

On the **1,283 pieces** carrying **both** a VL vector (`notes/`) and a harmonic-view vector (DCML `harmonies/`,
built through the existing pipeline — `parsers/dcml` + `extract` + `discover`, LDA-12 → KMeans, verbatim), both
sides clustered at K=4:

```
cross-ARI(VL clusters, harmonic clusters) = 0.030      cross-AMI = 0.055
  on the same pieces:  VL clusters   vs texture 0.195 · era 0.225 · source 0.115
                       Harm clusters vs texture 0.024 · era 0.121 · source 0.045
```

**cross-ARI ≈ 0.03 = statistical independence.** The voice-leading partition and the harmonic partition of the same
music are orthogonal: VL tracks texture/era, harmony tracks neither (harmonic clusters are ~invariant to texture,
0.024). The **contingency table** (VL rows × harmonic cols) is close to the product of marginals — every VL cluster
spreads across every harmonic cluster (the one structured cell is VL1 avoiding H1):

```
        H0   H1   H2   H3   | row
 VL0    53   42   95  135   | 325
 VL1   164    0   77  136   | 377
 VL2    31   45   73  109   | 258
 VL3   101    7   81  134   | 323
 col   349   94  326  514
```

**Curated probe — one harmonic idiom, split by voice-leading.** Steely Dan / Piazzolla / Hiromi are *one* harmonic
idiom (v1.6: all converge on the cross-cutting chromatic/modal cluster). By **voice-leading they split** (cluster
ids below are from an independent KMeans-3 refit on the 47 curated pieces — local ids, the finding is the *split*):

| set | n | VL-cluster spread | step | leap | contrary | oblique |
|---|---|---|---|---|---|---|
| steely_dan | 22 | {c0:10, c1:9, c2:3} | 25% | 44% | 7% | 79% |
| piazzolla | 6 | {c1:5, c2:1} | 39% | 31% | 5% | 82% |
| hiromi | 19 | {c2:16, c1:2, c0:1} | 36% | 48% | 5% | 86% |

Hiromi concentrates in one VL cluster (dense pianistic — high leap), Piazzolla in another, Steely Dan spreads —
three artists that are harmonically *one* thing are voice-leading-*several* things. (All three are uniformly
oblique-dominant, 79–86% — the shared "homophonic arrangement" texture from the top-note reduction — and separate on
the melodic-interval sub-axis; see §6 caveat.)

**Chorale projection — VL-tight, harmonically-scattered (pilot prediction confirmed at full coverage).** Both chorale
encodings collapse into a single VL cluster (all-pieces KMeans-4 fit; cluster index arbitrary — the point is the
concentration):

```
m21_chorale    n=368  → VL cluster c1 holds 98%   (spread c1:361, c2:7)
bach_chorales  n=361  → VL cluster c1 holds 98%   (spread c1:353, c2:8)
```

Chorales were harmonically *scattered* across the functional clusters (v1/v1.1 — they refused to form a harmonic
idiom); here they are **98% VL-tight**. A chorale's identity is its stepwise SATB part-writing, not its chords —
exactly the pilot's prediction, now at full coverage. **Bonus:** the two *independent* chorale encodings
(music21-note vs DCML-TSV) agreeing 98% / 98% on the same VL cluster is a live **extraction-robustness cross-check**
— the VL features are stable across ingestion path.

---

## 5. What the axis-2 study concludes

The pilot's implication is measured and confirmed: **the full style structure is ≥ 2-D — (harmonic idiom) ⟂
(voice-leading idiom), with mode and chromaticism as further cross-axes.** Concretely:

- **Voice-leading is organized by texture**, and the discriminative feature is **voice-pair motion type**
  (contrapuntal contrary/similar ↔ homophonic oblique), *not* melodic-interval size and *not* instrumentation.
- **The robust VL idioms** are (by stability): **contrapuntal part-writing** vs **homophonic
  melody+accompaniment**, with a secondary, era-correlated **stepwise → leapy/pianistic** melodic sub-axis
  refining the homophonic mass into classical-keyboard vs romantic-pianistic.
- **VL ⟂ harmony formally** (cross-ARI 0.03): the same classical pieces are partitioned independently by the two
  axes; sophisticated arrangements are one harmonic idiom but several VL idioms; chorales are one VL idiom but
  several harmonic ones.

For the spec's **voice-leading layer**, the empirical footing is therefore: a **motion-type-led** VL feature set
(parallel/similar/contrary/oblique rates) as the primary discriminator, an interval-profile as a secondary
melodic-complexity descriptor, and a texture taxonomy of **{contrapuntal, homophonic-classical,
homophonic-pianistic, moderate/mixed}** — coverage is **notated-music only** (classical + chorale + arrangement),
distinct from the cross-tradition harmonic axis (lead sheets have no voices).

---

## 6. Caveats (honest marks)

- **View A explosion asymmetry.** The DCML branch explodes chord tones within a notated voice (pilot behavior);
  the chorale branch drops chords (`isNote`); the curated branch reduces chords to top note. So View A's leap rate
  is inflated for chord-dense keyboard/arrangement material, and its **era** recovery is *partly* this
  chordal-density artifact rather than pure melodic language. **This is why the primary finding rests on View B**,
  which reduces every onset to a single top pitch (no explosion) and still recovers the texture split cleanly — and
  which groups *exploded* chamber corpora (corelli, couperin_concerts) *with* the chorales, ruling out a
  chorale-encoding artifact. A uniform per-source reduction rule is a possible v-next refinement (recorded, not
  built).
- **Curated top-note reduction** makes all three arrangement sets oblique-dominant (79–86%), so their VL *split*
  rides mainly on the View-A melodic sub-axis; the qualitative claim (one harmonic idiom → several VL readings)
  holds, but the arrangements share a "homophonic arrangement" macro-texture by construction of the reduction.
- **Notated-voice-only** (declared in §1) — compound melody / implied polyphony reads as leapy; a representation
  property, not corrected here.
- **Texture/era covariate maps are a declared interpretation lens** (musicological consensus), never clustering
  input (spec §6). They are approximate at the margins (e.g. `wagner_overtures` tagged "orchestral/romantic";
  `scarlatti`/`cpe_bach` galant tagged "classical").
- **Chorale near-duplication** (m21 vs DCML, ~720 pieces) is capped, and its effect is bounded — the two encodings
  co-cluster, so it reinforces rather than distorts (and the finding survives the confound test with source ARI 0.07).
- **`sklearn`-version drift** on the pilot ARI number (0.683 → 0.595) — features identical; noted so the pilot line
  is reproducible at the *feature* level, not the KMeans-init level.

---

## 7. Cost, reuse, and scope

- **Cost (measured, this machine).** Full parse of all 2,102 pieces = **67 s** (music21 chorale parse ≈ 40 s of
  it; DCML pandas reads ≈ 24 s; curated note-level parse ≈ 9 s — note-level is cheap because it is **not** chordify).
  The full stability sweep + confound gate + idiom tables + the orthogonality run complete within the same run.
  **The full study fits on this machine with no sandbox cap — no scaled-down version was needed** (records are
  cached to a pickle so re-analysis is instant).
- **Reuse vs new** (per the standing rule): **reused** the discovery machinery — `discover.leakage_report` (ARI/AMI
  reporter), the `stab.py` stability-table discipline (K×seed×cap), and for the orthogonality test the entire
  harmonic pipeline verbatim (`parsers/dcml`, `extract.build_corpus`, `discover.fit_lda`). **New** = the View-B
  motion-type extractor + the fuller note-level loaders (`parsers/voiceleading2.py`) and the two run scripts
  (`run_vl_discovery.py`, `run_vl_orthogonality.py`). **What retires: nothing** — View A is imported unchanged, so
  the pilot remains a strict subset.
- **Files** (pipeline code + this report; the findings doc is **not** edited here — Cowork folds
  `cowork_idiom_discovery_findings.md` after ratification):
  - `idiom_discovery/parsers/voiceleading.py` — Task-0 portability (`__main__` corpus root; `vl_profile` untouched)
  - `idiom_discovery/parsers/voiceleading2.py` — View-B extractor + fuller loaders + lens maps (**new**)
  - `idiom_discovery/run_vl_discovery.py` — coverage + stability + confound gate + ablation + idiom tables (**new**)
  - `idiom_discovery/run_vl_orthogonality.py` — cross-ARI + contingency + curated/chorale probes (**new**)
  - `idiom_discovery/vl_discovery_out.txt`, `vl_orthogonality_out.txt` — the raw measurement dumps
- **Levers recorded for their proper layer, not coded here** (no inference-problem-fixing in this increment):
  a motion-type / static-harmony feature is the natural home of the modal/static-jazz "wobbly sixth" the harmonic
  study deferred (v1.6); a uniform per-source note reduction would retire the View-A explosion asymmetry. Both are
  measurement observations for Cowork, not changes.
- **Hard limits honored:** nothing under `src/`; no build; no gate regen (by-construction statement above); the
  frozen gate corpus and held-out research beds untouched (read-only throughout); fork-local.
