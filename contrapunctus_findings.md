# Contrapunctus — Findings & Competitive/Reference Notes

> **What this is.** Research notes on **Contrapunctus** (contrapunctus.app), a music-theory web app whose
> closed harmonic-analysis engine is benchmarked, in the open, against the academic state of the art at
> autonomous Roman-numeral analysis. It is a direct parallel to our MuseScore `composing` module. Compiled by
> Cowork from the public site + the public benchmark repo. **Accessed 2026-06-20.**
>
> **Provenance caveat.** Numbers and claims below are **Contrapunctus's own**, from its site and repo. The
> methodology is unusually rigorous and self-reproducible (`make score` from committed data), but I have not
> independently re-run it. Where a claim is theirs, it is attributed. Sources at the foot.

---

## 1. What Contrapunctus is

A browser-based music-theory platform (free public beta), built by a solo "music theory nerd and software
engineer" in Minneapolis (GitHub `Tomczik76`, `info@contrapunctus.app`, a Discord). Feature surface:

- **Real-time notation/guitar-tab editor** with autonomous Roman-numeral analysis (triads, 7ths, extensions,
  secondary dominants), labeled as you write.
- **Part-writing error detection** (parallel 5ths/8ves, voice crossing, spacing, unresolved tendency tones).
- **Non-chord-tone detection** — passing / neighbor / suspension / embellishment, auto-classified on the score.
  *(Directly relevant to our anchor problem — see §6.)*
- **Species counterpoint** — an interactive edition of **Fux's _Gradus ad Parnassum_ (1725)**, all five species,
  46 exercises, original Latin alongside translation, plus an LLM tutor ("Aloysius") answering in-character.
- **Guitar tab mode** (score↔tab toggle, auto fret positioning, 2,000-shape chord dictionary).
- **MusicXML import** from Sibelius / MuseScore / Finale (`.musicxml` + `.mxl`).
- **Community layer** — author/solve exercises, 15 ranks (Motif→Opus), weekly/all-time leaderboards, solution
  gallery; **classroom tools** — classes, invite links, authored assignments, color-coded gradebook.
- Roadmap: MIDI/MusicXML export, mode transforms, an "AI Assistant" for analysis suggestions.

Stack: **Scala** core compiled to **WebAssembly** (Scala.js `fullLinkJS`), running browser-local in a Web
Worker; the corpus harness is Python; the site is a client-rendered SPA on S3.

## 2. The engine (architecture)

A **hybrid Roman-numeral analysis engine**, three stages:

1. **Rule-based key detection.** Three building-block detectors — **HMM, Hybrid, Heuristic** — all consuming the
   same features; a **`KeyChainRouter`** composite classifies each piece's texture and routes to a detector.
   Output is a *keychain* (per-beat key spans).
2. **Rule-based chord-candidate generation.** Produces a candidate set of Roman numerals per beat.
3. **A small _learned_ re-ranker that picks the final label** — **logistic regression over tonic-rotated,
   windowed pitch-class features.** On by default; weights baked into the WASM. *This is the component that put
   them ahead of AugmentedNet.*

Their one-line rule (verbatim): **"never learn keys; do learn the chord label."** The engine's wire input is
per-beat `{dp, accidental}` + tonic + scale + key signature + time signature (MusicXML parsing lives in the app,
not the engine). Public entrypoints: `analyzeHarmony`, `identifyChord`, `warmup`, `checkFirstSpecies/Second/Third`.

## 3. The open benchmark — headline numbers

**"Closed model, open evals."** The engine source is closed; the evaluation is fully public and reproducible
(`github.com/Tomczik76/contrapunctus-bench`, Apache-2.0 harness, eval-only WASM engine). Latest release
**2026-06-11**, corpus **When-in-Rome**.

**Genre-balanced macro-average (each of 9 genres = one observation), autonomous, out-of-sample:**

| Engine | Type | Exact % | a-d % | Genres won |
|---|---|---|---|---|
| **Contrapunctus** | hybrid: rules + learned re-ranker | **52.25** | 70.66 | **7 / 9** |
| AugmentedNet 11+ (ISMIR 2021) | neural CNN | 47.94 | 68.04 | 2 / 9 |
| AnalysisGNN v1.0 (2024) | neural GNN | 38.72 | 59.23 | 0 / 9 |
| Music21 10.1.0 *(keys given — not autonomous)* | rule-based | 23.33 | 41.12 | 0 / 9 |

**+4.31pp over AugmentedNet, out-of-sample vs an opponent measured largely in-sample** (see §4). All-pieces
micro (chorale-tilted, 505 pieces / 48,242 events): Contrapunctus **59.63** vs AugmentedNet 51.51.

**Per genre (Δ vs AugmentedNet):** Bach chorales **68.33 (+13.10)**, Brahms lieder 49.25 (+9.82), Haydn Op.20
55.59 (+9.02), Mozart sonatas 63.39 (+7.55), Beethoven Op.18 49.44 (+5.24), Bach WTC I 39.16 (+4.26), Schubert
58.66 (+4.17). **Loses** TAVERN (43.48 vs 49.27) and Beethoven BPS-FH (42.96 vs 51.53) — *both AugmentedNet
training collections*, both figural/variation textures where a chord is spread across an arpeggio.

## 4. Methodology (what makes it credible — and mirrors our own discipline)

- **Autonomous single-pick exact match.** Raw MusicXML → exactly one Roman numeral per ground-truth event. The
  only apples-to-apples setting across rule/neural/hybrid engines. Music21 has no key detector, so it's *given*
  the analyst key — flagged "(keys given)" as an easier-conditions upper bound; still last.
- **Every GT event counts** (no label = miss; no denominator shrinking to a "confident" subset).
- **Pinned common-subset intersection.** A piece is scored for *every* engine or *none* (505-piece intersection).
  `score.py` writes `common_subset.json` and **fails if a later run's intersection differs** — because "a partial
  competitor cache silently changing the subset composition has, in this project's history, flipped an aggregate
  verdict without any engine changing." *(≈ our manifest-stamped per-preset dirs + `characterise_bir_false`
  refusing to measure mismatched fingerprints.)*
- **Two aggregations:** all-pieces micro (chorale-tilted: 370/505 are chorales) + **genre-balanced macro (the
  honest head-to-head)**. *(≈ our per-preset + batch-vs-section granularity caveat.)*
- **Out-of-sample (ours) vs in-sample (rivals).** Their number is **5-fold cross-validation by piece** (every
  piece scored by a model that never trained on it). AugmentedNet's released model is **manifest-verified** as
  ~in-sample on 7 of 9 genres. The asymmetry runs *against* them deliberately — "the lead survives the most
  generous reading of the opponent."
- **One parity-tested normalizer** (`rn_normalize.py`, 986 fixtures, parity-tested against the engine's Scala
  normalizer) scores all four engines. **A 2026-06-09 audit found they'd been scoring their own engine through
  the Scala normalizer but rivals through two drifted Python copies — all three drifts inflated their lead — and
  re-scored everyone.** *(≈ our corrected-DCML-parser re-baseline + the A/B parser-revert verification.)*
- **6 cumulative match tiers** quantify *how* misses miss (defensible reading vs wrong chord), credited
  identically for all engines, reported as **annotator-defensible (a-d)** but never cited alone:
  `exact ⊂ +sameChord ⊂ +inversion ⊂ +convention ⊂ +sharedBass ⊂ +secondaryDiatonic`. **The convention examples
  are *our* ambiguity buckets verbatim:** Cad⁶₄ ↔ I⁶₄/V⁶₄, `vii°6 ↔ V`, `V/V ↔ II`, inversion figures, shared-bass
  (`iii ↔ I6`, `V6 ↔ vii°`), `#vii° ↔ vii°` typography. *(= our convention-boundary "honest floor.")*
- **Frozen 9-piece held-out set**, never iterated against, as an overfitting guard on top of the CV.

## 5. Negative results (their "what didn't work" — the most useful section for us)

These are explicitly published "so a reader can see the search was adversarial, not a victory lap." Several
**independently reproduce conclusions we reached on our own engine:**

1. **"Learned _key_ detectors lose, every time."** LR / MLP / random-forest key detectors beat the hand-tuned
   heuristic on *per-beat key accuracy* yet **regressed chord-ID exact by 5–9pp** — because chord-ID depends on
   the *structure* of the keychain (long, phrase-aligned key runs) more than per-beat correctness, and a learned
   detector's short spurious segments each cost several wrong-key chord beats. → **never learn keys.**
   *(≈ our K3 finding: the joint key **search** is inert; the lever is soft-evidence quality + keychain
   structure, not per-beat reweighting. And our K1/K1b: short spurious modulation over-extensions hurt.)*
2. **"Bigger models overfit."** A higher-capacity neural chord-ID re-ranker scored *below* the plain logistic
   regression. "Capacity was not the lever; the feature representation was. Simpler generalized better."
   *(≈ our "calibration / soft-evidence quality, not a fancier search.")*
3. **"The selection layer is saturated."** With the LR re-ranker shipped, three further re-ranking mechanisms
   were built, measured, and **rejected**: (a) tick-level **Viterbi decoding over the model's posteriors with
   learned transitions — negative at every blend weight**; (b) span-structural-bass refiguring — "the analyst's
   inversion is a per-event harmonic reading, not a function of the bass voice over any span"; (c) a
   **metric-weighted window-support score — a near-perfect no-op** (surviving candidates' window coverage is
   near-identical). **Conclusion: remaining chord-ID error is candidate/emission-level or key-level, NOT
   selection-level.** *(≈ our audit-#6 re-attribution: competition/selection owns only ~24%; pure re-rank ~1.7%;
   most cases "need a candidate never surfaced → functional rules, not re-weights." And ≈ our K3 "scoped joint
   search inert.")*
4. **Scoring-side strictness probes rejected on the merits** — e.g. forcing the cadential-6-4 family to count
   only at `exact` was reverted as penalizing a documented annotator convention. *(≈ our convention-boundary
   discipline.)*

## 6. Relevance to our current work (the anchor / NCT redesign)

- **They ship automatic non-chord-tone classification** (passing/neighbor/suspension) — the exact
  embellishment discriminator CC's anchor-redesign investigation is trying to place in the right layer
  (candidates A–D). Their engine's existence is proof the discrimination is tractable; *how* they do it is in
  the closed engine, but the **"top confusion pairs"** section of their benchmark likely exposes the same
  `sus`/`add` over-read failure mode we just hit on the naive union-recompute.
- **★ The NCT algorithm, stated in their docs (`/help`):** "The classification reads from harmonic context
  (**current chord, previous/next chord, beat strength**), so re-harmonising a passage updates the labels
  live." This is a direct hit on our anchor diagnosis: their NCT discriminator consumes **prev/next chord +
  metric beat-strength** — precisely the temporal/metric context CC's recompute *threw away* by passing
  `context=nullptr` on a flattened tone union. It is concrete external support for **candidate A (temporal
  context)** combined with a **beat-strength signal**, and against the "raw union, no context" approach that
  hard-stopped. Note the dependency direction they accept: chord → NCT label (re-harmonizing updates labels),
  i.e. the chord identity is resolved *first* and embellishments are classified *against* it — the opposite of
  re-deriving the chord from the embellishment-laden union.
- **Their negative result #3 is a direct signal for our anchor sequencing:** they found the *selection* layer
  saturated and the residual to be **candidate/emission-level or key-level** — i.e. the lever is *which chord
  candidates get generated*, not re-ranking. That aligns with treating the merged-region chord as an
  **emission/candidate** problem (recompute the right candidate from the right tone-core) rather than a
  selection tweak — and supports candidate **C** (region-layer "adopt only a genuinely different root/quality,
  not a same-root sus/add over-spec") over a heavier scoring change.
- **Their metric-weighted-window-support no-op (#3c)** is a caution for our candidate **B** (duration/metric
  weighting): metric weighting did *nothing* for their **selection**. Our case is different (candidate
  generation on merged tones, not selection), but it tempers the expectation that duration-weighting alone will
  carry the fix.
- **Architecture shape match:** rule-based key + rule-based candidates + a *small* learned re-ranker (LR over
  tonic-rotated windowed PC features). This is a concrete, working instance of the "reserved learned-emission
  slice" we've floated for the symmetric-dim7 / partial-sig floors — and a data point that **a deliberately
  simple LR re-ranker beats neural approaches out-of-sample.**

## 7. External references (datasets, rival engines, papers to chase)

- **When-in-Rome** corpus (Gotham et al.; new content CC BY-SA 4.0) — the analyst-label source; bundles
  Riemenschneider chorales (Craig Sapp **kern), OpenScore Lieder (CC0), DCML Mozart, TAVERN, BPS-FH (Chen & Su
  2018), HaydnSun. *(We already use DCML; When-in-Rome is a broader superset worth knowing.)*
- **AugmentedNet** (Nápoles López et al., **ISMIR 2021**) — neural CNN RNA, the SOTA baseline they beat. MIT.
- **AnalysisGNN** (2024) — neural GNN RNA. MIT.
- **music21** (BSD-3-Clause) — rule-based, used (keys-given) as a floor.
- **"Detecting chord tone alterations and suspensions"** (Journal of New Music Research, 2024) — surfaced
  separately; the closest published treatment of the NCT/suspension problem our anchor faces.

## 8. Repo map + how to reproduce

`github.com/Tomczik76/contrapunctus-bench` (Python 65% / JS 22% / Shell 12%; 5 commits; main branch):

```
README.md                 headline + methodology summary
methodology/              match-tiers.md · corpus.md · protocol.md
corpus/manifest.json      every piece: id, genre, events, source, license
corpus/prep/              scripts deriving ground truth from the When-in-Rome submodule
harness/score.py          the aggregator `make score` runs (Python 3.9+, stdlib only)
harness/rn_normalize.py   the single parity-tested normalizer all engines share
harness/engines/          per-rival runners + setup
results/<date>/           dated releases: 4 scored reports + scores.json + PROVENANCE.md
engine/                   the closed engine as a stripped WASM bundle + run.mjs
```

- `make score` — 1-minute reproduction of the tables from committed `results/` (no engine, stdlib Python).
- `make check` — asserts every README number matches `scores.json`.
- `make bench` — the heavy path (runs each rival model; needs the When-in-Rome submodule + rival envs + closed
  engine).
- `node engine/run.mjs` — run the live WASM engine on a progression (**in-sample on the corpus — does NOT
  reproduce the published OOS numbers**).

## 9. Open questions / possible next steps

- **Read `harness/score.py` + `rn_normalize.py`** to see exactly how they tier-classify — our `compare_rn` /
  `dcml_parser` do the same job; their normalizer (986 fixtures, Aug6 collapse, `#vii°` strip) may have edge
  cases worth importing into ours.
- **Pull the "top confusion pairs" data** (on the `/engine` page / `results/`) — likely the same `sus`/`add`
  and `vii°↔V7` confusions as our audit-#6 patterns; a free external corroboration of our error taxonomy.
- **Consider benchmarking our engine against When-in-Rome** (broader than DCML) and/or **adding our engine to
  their comparison** (they accept PRs that score through the shared normalizer) — would give us an external,
  third-party number against AugmentedNet/AnalysisGNN.
- **The JNMR 2024 suspension-detection paper** is the best external reference if anchor candidate D (a
  scoring-layer NCT discriminator) turns out to be required.

---

---

## 10. Addendum (2026-06-20) — behind-login content + the two harness scripts

### 10a. The analyzer, as documented (`/help`)
- **Roman numerals** appear once ≥3 sounding pitches form a triad/7th/extension; inversions, secondary/applied
  dominants, and augmented sixths "recognized in context."
- **Runs in a Web Worker against a locally-bundled WASM engine.** For long scores it analyzes **only the
  visible measure range (+ buffer) first, then backfills** — analysis follows the viewport. (Our engine runs
  the whole score in-process; theirs is incremental/viewport-scoped for editor responsiveness.)
- **Context-sensitive part-writing rules** (a design philosophy worth noting): voice-crossing/spacing rules
  *don't fire* in 2-voice writing; doubled-leading-tone fires *only* when both LT voices actually resolve up by
  step (i.e. a real parallel octave is imminent); root-not-doubled is a *soft warning*, not an error, "because
  real practice (Bach, Mozart, Haydn) doubles the third or fifth regularly when voice leading demands it." This
  is the same "credit the documented convention, don't penalize defensible practice" stance as their benchmark
  tiers — and as our convention-boundary floor.
- **Voice modes:** free-form (voices *inferred* from pitch stacking) vs SATB/strict (explicit voices → a
  distinct analyzer path with counter-parallel detection + voice-named errors). Mirrors our explicit-voice vs
  inferred handling.
- **Mistake-reporting loop:** a "Report Incorrect Analysis" button pre-fills the score + the analyzer's output;
  community votes on corrections. (A crowdsourced error-correction pipeline — we rely on the DCML/music21
  oracle instead.)
- **Community** (logged in as Vincent Wong, rank Motif): an early/small exercise feed, seeded mostly by one
  author ("The Architect") — Mozart K545, Tristan harmony, Pathétique, modal-jazz realize-harmony, all five
  species. Low attempt counts. Confirms it's an early beta; the engine/benchmark is the substantive artifact,
  not the community size.

### 10b. `harness/score.py` (the aggregator — Apache-2.0, stdlib-only)
- **Per-piece report schema** (one JSON per engine): `{mode, group, piece, total, exact, sameChordGained,
  inversionGained, conventionGained, sharedBassGained, secondaryDiatonicGained}`. Only `mode=="single-pick"`
  rows are scored. a-d = exact + the 5 tier gains. *(Directly comparable to our BIR tier/bucket counts.)*
- **The coverage-gate code is the notable part:** the common subset is computed as the 4-engine intersection,
  then **pinned to `common_subset.json`; a later run that recomputes a different intersection raises
  `COVERAGE GATE FAILED` and aborts.** Verbatim rationale: "a partial rival cache cannot silently change the
  evaluated piece set and flip a verdict (it has, historically; hence the pin)." This is *exactly* our
  `corpus_manifest.json` + `characterise_bir_false` fingerprint-refusal discipline, independently arrived at.
- **`--diff-prose`** compares a fresh run against a prior `scores.json` and prints a review checklist —
  **winner flips, win-tally moves, 10%-threshold crossings, lead sign-flips, lead moves >0.5pp, common-subset
  changes, stale `results/<date>` references in the README** — "so a release can't silently outrun its prose."
  **This is an idea worth stealing for our STATUS.md/scoring_model.md sync rule:** an automated guard that
  flags when measured numbers have drifted from the hand-written narrative that cites them.
- **`--check`** asserts every headline+per-genre number literally appears in README.md; generated tables live
  between `<!-- BEGIN/END GENERATED -->` sentinels, prose is hand-written and never auto-touched; re-running on
  unchanged data is a byte-for-byte README no-op (their "faithfulness contract" — our byte-identical discipline,
  applied to docs).

### 10c. `harness/rn_normalize.py` (the single normalizer — the most reusable artifact for us)
- **Single source of truth**: every competitor scorer imports `normalize` from this one module; a Python port
  **parity-tested against the engine's Scala normalizer over 986 committed fixtures**
  (`test_rn_normalize_parity.py`).
- **★ The fairness-audit story is our GT-parser re-baseline, twin:** a 2026-06-09 audit found they were scoring
  *their* engine through the Scala normalizer but the three rivals through **two independently-drifted Python
  copies**, and **all three drifts inflated their own relative number** — (1) the tonicization-slash keep-set
  was missing lowercase `v`/`n` so `/v,/vi,/vii` lost their slash for rivals only; (2) the `Ger65/Ger7→Ger6`
  collapse was absent; (3) the `#vii→vii` strip was applied too broadly. Unified + everyone re-scored; "a
  correction that, by construction, can only have *lowered* our reported lead." This is the same class of bug
  and the same symmetric-re-score remedy as our applied-chord `/X` + minor-key leading-tone GT-parser fix
  (`tools/dcml_parser.py`).
- **The canonicalization rules our `compare_rn`/`dcml_parser` should cover** (rule-for-rule, processing order
  brackets → alteration-suffix → inversion-shorthand → aug6 → `#vii`-strip): Unicode super/subscript → ASCII;
  `°→o`, `♯/♭→#/b`, `⁺→+`, `Δ` elided; **`/o7 → ø7`** half-diminished shorthand; **slash before a roman-letter
  char = tonicization (kept), any other slash = figured-bass (dropped)** with keep-set `{I,V,i,v,N,n,F,G,C}`
  (note: both `/V` DCML and `/v` Bach-WTC styles); strip `[..]` brackets; strip bare `#3`/`b5` alteration
  suffix; `V2→V42`, `*63→*6` inversion shorthand; aug6 `Ger65/Ger7→Ger6`, `Fr6→Fr43`, strip decorative `+`;
  **`#vii→vii` only at the exact tier, no-slash/local forms only** (secondary `#viio65/ii` keeps the chromatic
  marker). Also a `rntxt_beats_per_measure` map incl. `slow/fast` compound meters (`fast 6/8 → 2`). **Action:
  worth diffing against our normalizer to catch edge cases (Ger collapse, the lowercase-`v` tonicization
  keep-set, the exact-tier-only `#vii` strip) before they bite our oracle comparison the way they bit theirs.**

### 10e. HIGH-value repo files (run.mjs wire format, scores.json tiers, AugmentedNet splits, PROVENANCE)

**`engine/run.mjs` — the probe spec (this is what we'd build a black-box probe against).** Entrypoints:
`analyzeHarmony(JSON.stringify(req)) → JSON`, plus `warmup(tag)`. Wire format:
- **Note** = `{ dp, accidental }` where `dp = octave*7 + letterIndex` (C=0 D=1 E=2 F=3 G=4 A=5 B=6); `accidental`:
  `""` = follow key sig, `"n"` natural, `"#"/"b"/"##"/"bb"` explicit.
- **beat** = `{ notes: [...] }`; **request** = `{ tonic:{letter,accidental}, scale:"major"|"minor"|modes,
  keySig:{count,type:"sharp"|"flat"}, tsTop, tsBottom, measures:[{beats:[...]}] }`.
- **Output** per beat: `{ romanNumerals:[...], chordNames:[...] }` + `timings.analyzeMs`; `error` on failure.
- Demos shipped: `I–IV–V–I`, `ii7–V7–I`, `I–V/V–V–I` (the V/V reads a D-major triad as secondary dominant). The
  model is on; labels are the production engine's. (Reminder: in-sample on the benchmark pieces — for OOS use
  `make score`.) **→ a probe feeds per-beat note-sets + a key and reads back `romanNumerals[0]`/`chordNames[0]`.**

**`scores.json` — the per-tier cumulative ladder** (where each engine's a-d total comes from, micro/all-pieces):
- Contrapunctus: exact **59.63** → +sameChord 62.72 → +inversion 65.96 → +convention 67.13 → **+sharedBass
  72.73** → +secondaryDiatonic 73.16. **The biggest single jump is `+sharedBass` (+6.77pp)** — most of their
  non-exact misses are bass-sharing ambiguities (`iii↔I6`, `V6↔vii°`), i.e. *incomplete-chord / bass-anchoring*
  cases — the same bucket our audit-#6 flagged (bass-anchoring bias 216/345).
- AugmentedNet's big jump is `+inversion` (+6.23pp) — the neural engine misses bass position more than root.
- **Pre-tonal Monteverdi (modal, exploratory):** Contrapunctus 45.09 exact, **music21 (keys-given) 44.49 —
  nearly equal**, while the neural engines collapse (33.7 / 31.35). On modal pre-tonal polyphony the learned
  re-ranker's edge evaporates and a rule engine with the key handed to it is competitive — a useful boundary on
  where learned chord-ID helps (tonal) vs not (modal).

**`harness/engines/augmentednet/README.md` — the in-sample caveat, made concrete.** AugmentedNet (Nápoles López,
Gotham & Fujinaga, ISMIR 2021; MIT) released model `augnet-v11-rnalt`; its own manifest (`augnet_splits.json`,
**380 pieces = 260 train / 60 val / 60 test**) is dumped by `augnet_splits_dump.py` and shows 7/9 genres overlap
training. Runs on Python 3.11 + **TensorFlow 2.15** (TF 2.16/Keras-3 can't load the 2021 architecture). The
scorer `augnet_comparison.py` **imports the shared `rn_normalize` + the `music21_comparison` tier-classifier** —
so all engines share one scorer (the fairness fix). Same 3 known structural failures (Op.18/1 mvt 2, *Die
Stadt*, WTC fugues 19 & 22).

**`results/2026-06-11/PROVENANCE.md` — release discipline (mirrors our STATUS.md provenance).** Engine build git
`0706f1cc`; Contrapunctus report is the Scala `WhenInRomeSuite`, **OOS 5-fold CV**. The release ships only
`single-pick` rows (the source reports also held per-detector/key-accuracy diagnostic modes, dropped). Notable:
- **A symmetric tier-rule change** (Neapolitan `N6 ≡ bII6` now matches at *exact* — a notation identity, unlike
  the interpretive Cad⁶₄ which stays at the convention tier) was applied to **both** the Scala and Python
  classifiers and **every engine re-credited** (+0.05pp each). The first release attempt **carried** stale rival
  reports and was **refused by the parity gate** because they predated the rule — "the gate working as designed."
  *(≈ our re-baseline + the manifest fingerprint refusal.)*
- Inter-release gains 2026-06-10→11: an `RnEventTicks` event→tick alignment fix (2 bugs) + model re-bake on
  corrected ticks; **Brahms key-detection ("pseudo-fermata") flipped Brahms −1.07→+9.82, tally 6/9→7/9**;
  the N6 rule. Headline genre-balanced **50.17 → 52.25**. The falsified selection mechanisms (Viterbi,
  span-structural-bass, metric-weighted window) are documented in the engine's *private* `docs/engine/next-steps.md`.

**`corpus/manifest.json` (70 KB, skimmed — per-piece provenance, not transcribed whole).** Top-level `counts`
(total **563** / tonal **515** / common **505**; by_genre incl. monteverdi 48, schubert 46, tavern 10 before the
coverage intersection) + a `corpora` block (per-genre display/period/texture/score_source+url+license /
analysis_source+url+license) + a 1,900-line per-piece array (id, genre, events, source, license, in_common_subset
flag). Analyst labels are **When-in-Rome** (Gotham; CC BY-SA 4.0); chorale scores are Craig Sapp's
`bach-370-chorales` (Humdrum **kern). Scores/analyses are **not** redistributed — derived from the WiR submodule
at build time.

### 10d. What I did NOT access
The live **editor** canvas (an interactive notation surface — best seen visually, little text to extract),
the **Gradus** tutor chat, the **educator** dashboard, and the **closed engine source** (only the stripped WASM
+ its description are public). The analyzer's behavior is fully described in `/help` (§10a); its *implementation*
is closed.

---

## 11. The `/engine` sections in full (MEDIUM sweep)

**Cross-detector — the four key paths (449-piece corpus, chord-ID exact / per-beat key acc):**

| Detector | Mechanism | Key acc | Chord-ID exact |
|---|---|--:|--:|
| **Production** (shipped) | hybrid: routed keys + agreement switch + rules + **learned chord-ID** | (routed) | **58.83** |
| Heuristic | **pure rule-based** | **75.26** | 51.69 |
| Hybrid | rules + K-S statistical | 71.39 | 48.75 |
| HMM | statistical (Viterbi) | 71.32 | 47.39 |
| LR + Viterbi | **learned KEY detector (experimental)** | 72.75 | **43.20** |

**★ This table is the quantified "never learn keys."** The pure-rule **Heuristic** has the *best* key accuracy
(75.26) AND the best building-block chord-ID (51.69); the **learned** key detector has competitive key accuracy
(72.75) but the **worst** chord-ID (43.20), and — in the per-genre broader table — **loses in all 9 genres**
(e.g. chorales 52.62 vs Heuristic 64.49). The shipped **Production** adds the learned *chord-ID re-ranker*
(`selectPrimaryRn`) + a `KeyChainRouter` that routes by texture + an "agreement switch," lifting ~7pp over the
best single rule detector (51.69 → 58.83). So: **learn the chord label (≈ +7pp), never the key.** Their two
"learned models" are distinct — the experimental learned KEY detector (loses) vs the learned chord-ID re-ranker
(the headline win).
- **Tier composition is stable across detectors:** `+sharedBass` is the single biggest annotator-defensible
  tier for *every* detector (~6.6–7.0pp) — i.e. ~7% of events are bass-sharing/incomplete-chord ambiguities
  regardless of the engine. Robust external confirmation that the bass-anchoring/incomplete-chord bucket (our
  audit-#6 216/345) is a real, large, engine-independent ambiguity class.

**What the benchmark does NOT measure (their engine does more than chord-ID):** NCT classification
(passing/neighbor/suspension/appoggiatura/changing-tone, **with cause attribution**), voice-leading rule
checking (30+ named rules), species counterpoint (Fux checkers), and **modulation-aware analysis where every
detected modulation traces to a named harmonic event (V→I cadence, leading-tone resolution)** — explainable,
unlike the neural engines' implicit keychains. *(That cadence/LT-anchored, explainable modulation is our
`cadencekeyanchor` philosophy, independently.)*

**Performance (Apple M3 Max, CPU):** the neural baselines are heavy — AugmentedNet **8.88 s/piece median**,
543 MB RSS, 8 s model load; AnalysisGNN 5.24 s, 732 MB, 12 s load. Rule-based Music21 is 146 ms. Contrapunctus
ships as a **~250 KB browser WASM** running locally in a Web Worker — i.e. the rules + small-LR design is
deployable client-side where the neural SOTA is not. (A point in favor of our own non-neural direction for an
embeddable engine.)

**With-your-keys lift:** giving the engine analyst modulations instead of detecting them adds **+25.80pp on
Monteverdi, +20.55pp on chorales** — i.e. autonomous key detection is the largest single cost, biggest on
modally-ambiguous and dense-modulation repertoire.

**Not published (placeholders only):** the **Top confusion pairs**, **Per-harmonic-function accuracy**, and
**Held-out diagnostic** sections are "run `sbt … WhenInRomeSuite`" placeholders — the actual data is *not* on
the public page (it requires their private engine). So the confusion-pair taxonomy I hoped to line up against
audit #6 **is not publicly available**; the `+sharedBass` tier-composition above is the closest public proxy.

---

## 12. External research (the cited engines + the corpus + the suspension paper)

**AugmentedNet** (Nápoles López, Gotham & Fujinaga, ISMIR 2021; MIT). A **convolutional-recurrent** net
(separate conv blocks for **bass** and **chromagram** inputs) trained with **synthetic data augmentation** and
**multitask learning** over several simultaneous tonal tasks; predicts common Roman-numeral *classes* then
**reconstructs the full label** from them. Tested on 6 datasets (ABC, BPS, HaydnSun, TAVERN, When-in-Rome, WTC).
The SOTA baseline Contrapunctus beats. (PDF: archives.ismir.net/ismir2021/paper/000050.pdf; repo
napulen/AugmentedNet.)

**AnalysisGNN / ChordGNN** (Karystinaios et al., ISMIR 2023, arXiv 2307.03544, repo manoskary/ChordGNN; unified
follow-up "AnalysisGNN," CMMR 2025, arXiv 2509.06654). A **graph neural network** over the score: each **note is
a node**, edges encode note inter-dependencies; it produces **onset-wise** predictions from note-wise features
via a **novel edge-contraction algorithm**. The unified version handles multiple analysis tasks at once.
(Weaker than AugmentedNet on this benchmark: 38.72 genre-balanced.)

**When-in-Rome** (Mark Gotham et al.; github.com/MarkGotham/When-in-Rome; new content CC BY-SA 4.0). The
analyst-label corpus the whole benchmark scores against — an aggregation of RN-analyzed repertoire (chorales,
WTC, ABC quartets, DCML Mozart, TAVERN, BPS-FH, HaydnSun, OpenScore lieder). We currently score against DCML;
WiR is the broader superset and the de-facto common evaluation corpus for autonomous RNA.

**★ "Detecting chord tone alterations and suspensions"** (JNMR 52(5):425–435, online 2024-10-11; EPFL/DCML
orbit — Rohrmeier lab). **The most directly anchor-relevant paper of all.** It is a **post-processing** method:
input = a score *with basic chord labels*; output = the same labels *with* chord-tone alterations/suspensions
added. Its motivation is exactly our failure mode — you **cannot** fold alterations into the chord vocabulary
(the multiplicative blow-up already pushes RNA vocabularies past 1,000 labels, and re-analyzing for richer
chords over-reads). Three steps; **step 1 assigns each note a probability of belonging to the chord named by the
basic label** — a per-note chord-membership score that separates chord tones from NCTs/suspensions. It beats a
strong heuristic baseline on both ground-truth and detected-chord input, and **lets a chord detector train on a
SMALL vocabulary (e.g. triads only)** and recover the alterations afterward.

**→ Why this matters for the anchor.** It is the published, evaluated form of the redesign direction CC's
investigation is circling: **keep the basic chord identity; do NOT re-analyze the merged tone union into a
richer sus/add chord; instead classify the extra tones as NCTs via a per-note chord-membership probability.**
This is "chord-first, NCT-second" — the same dependency direction Contrapunctus's docs state (NCT read from
current/prev/next chord + beat strength). It argues the anchor's merged-region fix should be a **membership/NCT
discriminator over the union**, not a re-emission that lets the union vote a new chord quality — and it is a
concrete, citable method (and small-vocabulary training strategy) to model candidate B/D on if an in-layer
guard (candidate C) proves insufficient.

---

## Addendum (2026-06-26) — Contrapunctus does NO explicit phrase segmentation or cadence detection

Verified at the benchmark README (re-fetched 2026-06-26, github.com/Tomczik76/contrapunctus-bench). Relevant because we
are designing an explicit **phrase-boundary primitive** + **cadence detector**.

- **Contrapunctus's whole task is per-beat RN labeling** — "given a raw MusicXML score and nothing else, label *every
  beat* with a Roman numeral." Architecture: rule-based key detection + a learned chord-label re-ranker. **Phrase
  boundaries and cadences are not an input, a component, or an output.** ("Cad⁶₄" appears only as a chord-*label*
  convention in its scoring tiers — not a detected cadence event.)
- **Phrase structure matters to it, but only IMPLICITLY, via stable key runs.** Its headline negative result: learned
  per-beat key detectors *beat* the rule-based one on per-beat key accuracy yet **regressed chord-ID 5–9 pp**, because
  chord-ID depends on "the *structure* of the keychain — long, **phrase-aligned key runs** — more than on per-beat
  correctness." So phrases fall out of *stable key spans* (rule-based smoothing), never from a phrase detector.
- **It is SOTA-competitive with none of this** — 52.25% genre-balanced / 68.33% Bach-chorale exact, beating AugmentedNet
  out-of-sample, **without** any explicit phrase or cadence machinery.

**★ Proportionality discipline (user-ratified 2026-06-26) — carry into the phrase-boundary build.** The leading system
needs no explicit phrase/cadence layer for competitive RN, so our **phrase-boundary → cadence-gate → key/function** path
is a *deliberate architectural bet* (chosen for explainability and the tonicization-vs-modulation distinction L5 needs),
**not an accuracy requirement**. Therefore: **keep the phrase-boundary primitive proportionate** — it is load-bearing for
*our* cadence mechanism (a means to key/function), not for RN accuracy per se. Do not let it balloon. If the explicit
phrase/cadence path proves hard, there is a **proven fallback**: get phrase-alignment implicitly, via stable key runs, the
way Contrapunctus does. (Recorded also in `cowork_phrase_boundary_methods.md` and the design's scope note.)

---

**Sources:** contrapunctus.app/landing · /engine (benchmark, updated 2026-06-13, commit a896b554) · /help
(analyzer docs) · /community (logged-in feed) · github.com/Tomczik76/contrapunctus-bench (README,
methodology/{protocol,match-tiers,corpus}.md, engine/README.md, harness/{score,rn_normalize}.py, engine/run.mjs,
results/2026-06-11/{scores.json,PROVENANCE.md}, corpus/manifest.json, harness/engines/augmentednet/README.md;
release 2026-06-11) · AugmentedNet (Nápoles López et al., ISMIR 2021) · AnalysisGNN/ChordGNN (Karystinaios et
al., arXiv 2307.03544 / 2509.06654) · When-in-Rome (github.com/MarkGotham/When-in-Rome) · Detecting chord tone
alterations and suspensions, JNMR 52(5) 2024 (tandfonline 10.1080/09298215.2024.2412595). Accessed 2026-06-20.
