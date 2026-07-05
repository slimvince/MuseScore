# Style taxonomy — empirical proposal (idioms as tags, presets as idiom-weightings)

> **Status: RATIFIED (2026-06-30) · EXECUTED (StyleTag swap, this commit — 2026-07-02).** The five-idiom set + the two
> cross-attributes are now encoded in the dormant `harmonicvocabulary` component (`enum class Idiom` + `IdiomSet`,
> replacing the `{Baroque, Jazz, Default}` placeholder); the per-entry re-tag is `cowork_idiom_entry_mapping.md`.
> Grounded in the validated idiom-discovery study
> (`cowork_idiom_discovery_findings.md`, v1.5: 5,243 pieces, cap-robust). Per the dictionary §12.1 and the spec, the
> style taxonomy is a **joint decision with the preset system** — this is the proposal, not the ruling. If ratified,
> it supersedes the §12.1 hand-made genre taxonomy and the placeholder `{Baroque, Jazz, Default}` StyleTag.

## 1. What the data settled
Cross-tradition discovery found harmony is **not organized by genre** (tradition-ARI ≈ 0.3, weak and robust). The
robust structure is **five progression idioms** + two cross-axes:

**The five idioms (names ratified 2026-06-30 — provisional, easy to revise):**

| # | Idiom | Signature | Leaned toward |
|---|---|---|---|
| 1 | **Diatonic-functional** | simple V7-cadential — I–V7, ii–V, secondary V; diatonic | folk + simple common-practice |
| 2 | **Chromatic-functional** | functional + tonicization — applied/secondary dim7 (viio7/x), aug6, V7–I | classical (common-practice) |
| 3 | **Seventh-functional** | functional realized in sevenths — ii7–V7–Imaj7, circle-of-fifths sevenths | jazz |
| 4 | **Triadic-modal** | diatonic triads, modal — I–IV–V, ♭VII–IV planing, sus | pop / rock |
| 5 | **Chromatic-coloristic** | non-functional chromatic + modal-static — backdoor/altered dominants, planing sevenths | *cross-cutting — no genre* |

Naming logic: **1→2→3 is the functional family at increasing chord-vocabulary richness** (diatonic → chromatic
tonicization → sevenths); **4** is diatonic-but-non-functional; **5** is beyond both — the chromatic/coloristic
sophisticated idiom. Cross-axes: **mode** (major/minor) and **chromaticism** (diatonic↔chromatic). Key corroborations:
Baroque, galant and Classical share **one** idiom (#2 Chromatic-functional) — era is not an axis; folk collapses into
#1 Diatonic-functional; and the harmonically dense, genre-defying corpora (Steely Dan, Piazzolla, Hiromi) **all
converge on #5 Chromatic-coloristic**. So the categories are structural, not genres.

## 2. The proposal — two layers (reconciling idiom and genre)
The tension that started this (the StyleTag was genre `{Baroque, Jazz, Default}`; the data says idioms) resolves with
**two layers**:

- **Tags = the empirical IDIOMS (structural).** The encyclopedia tags each entry (progression / substitution) with
  the idiom(s) it belongs to — the five above (+ the mode/chromaticism attributes), **not** genres. `ii–V–I` tags
  *Seventh-functional*; `I–♭VII–IV` tags *Triadic-modal*; a backdoor dominant tags *Chromatic-coloristic*. This is what
  the data supports and what makes the tags structurally meaningful.
- **Presets = named IDIOM-WEIGHTINGS.** What a user selects is a **distribution over the idioms** — "this style
  emphasizes these idioms." Genre names (Baroque, Jazz, Pop) become convenient **labels for typical idiom-mixtures**,
  with the weights derived **empirically** from the per-cluster distributions (the clustering plan's "weights"). This
  is exactly the plan's "the taxonomy and the weights are one data-derived object."

This honors both: the tags are honest/structural (idioms), and users still pick familiar genre-named presets that map
to idiom-mixtures.

## 3. Mapping onto the current system
- **Encyclopedia `StyleTag`:** replace the `{Baroque, Jazz, Default}` enum with the **five idiom tags** (+ mode /
  chromaticism attributes); re-tag entries by idiom. (A change to the dormant `harmonicvocabulary` component — CC,
  once ratified.)
- **Presets → idiom-weightings (empirical):** e.g. *Baroque/common-practice* = functional-chromatic + functional-
  diatonic heavy, jazz/cross-cutting ≈ 0; *Jazz* = jazz-seventh + cross-cutting-chromatic heavy; *Default* = balanced.
  Exact weights from the per-idiom distributions.
- **§12.1 hand-made genre taxonomy:** retired in favour of this empirical idiom set.

## 4. Decisions (ratified by the user + confirmed by the data, 2026-06-30)
1. **Granularity — FIVE idioms.** Ratified (precision / no-information-loss) **and data-confirmed**: the candidate
   sixth (modal/static-7th jazz) failed the robustness check at every cap *even with targeted modal-jazz data added*
   (Impro-Visor + weimar), so five is the defensible set. The sixth is a real musical distinction **deferred** to a
   higher-K / explicit-static-harmony-feature study — not a committed idiom.
2. **Cross-axes — mode and chromaticism kept SEPARATE** (orthogonal attributes, not folded into the idiom tags).
   Ratified by the same principle: separating loses no information; folding would either lose major/minor or double
   the idiom count.
3. **Presets = idioms, for now.** The user selects an idiom directly (or it is auto-detected, below); inventing
   "user-friendly" genre-named idiom-mixtures is deferred until a grouping proves useful.
4. **Idiom auto-detection (roadmap; an inference feature → after the architecture is complete, per the standing rule).**
   Because an idiom *is* its progressions, the analyzer can read the idiom-mixture off a score's **committed**
   progressions and weight itself **forward** — a neutral/Default cold-start prior that firms up as more of the score
   is scanned (the existing forward-override mechanism, no back-edge). This reduces a manual preset to a cold-start
   prior + override.

**Idiom #5 confirmed unified** (it stayed one cluster across all caps and absorbed the new chromatic-pop / modal-jazz
material); the curated sophisticated corpora (Steely Dan/Piazzolla/Hiromi) all converge on it.

**Remaining for you:** only the final idiom **names** (the §1 working names) and, eventually, whether to keep
genre-named presets as a user-facing convenience over the idiom set.

## 5. Caveats (carried from the study)
- The idioms are **progression-based** (symbolic chord sources). **Voice-leading is a separate axis** (the spec's
  future layer) — e.g. a chorale's Baroque identity is voice-leading, *not* captured here. The taxonomy is the
  harmonic-progression layer only.
- Jazz/pop idioms are **derivation-validated but analysis-USE-unvalidated** (no jazz/pop analysis ground truth — the
  verifiability "empirically-unvalidated" mark stands until a jazz/pop GT exists).
- Idiom #5 (cross-cutting) is the least genre-pure and the most interesting; worth re-checking as more sources land.

## 6. The user-facing preset layer — the EXEMPLAR/GENRE proposal (user, 2026-07-05; RECORDED, deferred product work)

The §2 "presets = named idiom-weightings" layer gets its derivation-and-naming method (user proposal, raised
during the Stage-5 fitter arc; deferred by the ratified order — this is product/presentation work after the
architecture completes, and the §4-4 auto-detection is its own gated inference feature):

1. **Derivation: cluster the analyzed sources in the idiom-mixture space.** Every analyzed composer/corpus has a
   measurable distribution over the five idioms (the discovery pipeline computes it); clustering those points
   yields the natural preset set, each cluster = one mixture vector.
2. **Naming: exemplar anchoring, genre-era labels.** A preset presents as a familiar label + exemplars users
   know ("60s pop — The Beatles"), never as an idiom name or an obscure exemplar ("Hiromi means nothing to most
   people" — user). Genre names are LABELS over mixtures, never axes (the study's own result: era/genre is not
   the structure — Baroque/galant/Classical share idiom #2).
3. **Coverage beyond the analyzed set — three tiers, no bare guessing:**
   - **Measured:** the held research corpora already cover much of the user's example list — CoCoPops =
     Billboard charts (60s pop, disco); HookTheory = modern pop; the WJD carries per-solo style tags
     (dixieland/swing/bebop/postbop); iRb = the standards/crooner book. Per-genre mixtures are computable
     from existing tags.
   - **Declared:** genres with no held data (metal, shoegaze, grunge, hiphop, funk…) get an EDITORIALLY
     DECLARED mixture with a stated theory rationale (e.g. metal ≈ triadic-modal with high power-chord
     admissibility — the L4 §15 O4 constant is the metal-facing knob), validated when data arrives.
   - **Self-correcting:** the §4-4 auto-detection makes any preset a cold-start prior the score itself
     refines — mis-picked presets degrade gracefully, which is what makes declared mixtures shippable.
4. **★ LICENSE CONSTRAINT (binding — census §8c):** a preset's idiom-mixture is a SHIPPED parameter vector.
   Mixtures DERIVED from NC-class corpora (McGill Billboard, WJD, iRb…) must not silently ship: derive from
   the licensed pool (CoCoPops, OpenEWLD, GuitarSet, OpenScore, PD classical) where possible; DECLARE
   editorially elsewhere; use NC corpora for VALIDATION only. Recorded now so no Billboard-derived preset
   ever ships unnoticed.
5. **Caveats:** composers are not points (late ≠ early Beethoven) — exemplars must strongly evoke ONE mixture
   region; and a user-facing preset spans BOTH axes (harmonic idiom + the orthogonal texture axis), so the
   eventual preset object carries an axis-2 component too.

*Cheap internal prototype available when this activates: compute per-source mixtures from the existing
discovery outputs (research-tier, read-only) and cluster — license-relevant only at shipping.*

### 6a. The bidirectional preset⇄mixture contract (user, 2026-07-05; RECORDED with §6)

- **Forward — a preset IS its mixture, translated all the way down.** Preset → idiom-weight vector →
  composed scoring parameters via the Stage-5 anchor model (`cowork_stage5_fitter_design.md` D-10/D-11:
  per-idiom anchors + the per-family declared mixing rule — linear for the additive-weight family,
  discrete/nearest-anchor for thresholds). Defining a new preset never requires refitting.
- **Backward — every mixture is selectable; the discovered cloud is the EVIDENCE MAP, not the boundary.**
  Named presets = cluster centroids (progressive disclosure); a custom selector admits ANY simplex point
  (E-14 zero information loss). Each chosen point carries an evidence status: inside a discovered cluster
  (validated) · between clusters (interpolation) · outside the cloud (extrapolation — selectable, marked
  empirically-unvalidated; the A-7-mark pattern generalized to mixture space).
- **License split, resolved cleanly:** the ANCHORS are the shipped license-constrained fitted parameters;
  MIXTURE WEIGHTS are user configuration (free); only OUR shipped named-preset defaults carry the §6-4
  derivation constraint (licensed-pool-derived or editorially declared, NC-validated).
- **The loop-closing product feature:** auto-detection (§4-4) computes a score's mixture → "save this
  piece's detected mixture as a named preset" mints user presets from real music — the backward map in
  its most useful form (every combination that occurs in music a user cares about becomes selectable by
  example, not by enumeration).
- **The mixture's PRIMARY persistence home = the score itself (user, 2026-07-05).** Store the score's
  idiom mixture in the score's own metadata — MuseScore already supports user-defined score properties
  alongside title/composer (the metaTag mechanism, saved inside .mscz/.mscx). Consequences: the mixture
  TRAVELS with the file (no separate registry needed for per-score behavior); re-analysis seeds from it
  (the §4-4 cold-start prior becomes a warm start); "save as named preset" then reads FROM the score
  property (per-score setting vs reusable preset = two homes for the same mixture object, score-first).
  Requirements recorded now: (1) **provenance on the stored value** — auto-detected (analyzer
  version + date) vs user-set; a USER-set mixture is never silently overwritten by re-detection (the
  no-surprise rule), an auto-detected one may be refreshed; (2) **staleness** — a score edited after
  detection marks the stored mixture refreshable; (3) **interchange caveat** — user-defined properties
  survive the native format; MusicXML round-trip of custom metadata is partial and needs its own check
  before the feature relies on it; (4) the property schema (one namespaced JSON-valued tag vs several
  tags) is an implementation decision at build time, not now.
