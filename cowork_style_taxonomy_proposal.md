# Style taxonomy — empirical proposal (idioms as tags, presets as idiom-weightings)

> **Status: proposal for ratification (2026-06-30).** Grounded in the validated idiom-discovery study
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
