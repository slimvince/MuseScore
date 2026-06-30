# Layer 6 (Grouping) — Research & methods synthesis (pre-design)

> Research-first scan feeding the L6 design. Not the design itself. Sources: the DCML Annotation Reference 2.3.0,
> the `contrapunctus_findings.md` L6 addendum (DCML 4-layer target, flat-phrase finding, verifiability caveat,
> proportionality), a read-only reuse survey of `src/composing/`, and the tonal-segmentation literature scan below.

## 1. What L6 is — the validatable target
The DCML ground truth annotates four layers: **keys, chords, phrases, cadences**. Chords (L4) and keys (L3) and the
Roman numeral / cadence *detection* (L5) are owned upstream. **L6 owns the GROUPING outputs:**
- **Flat phrases** — `{ … }` spans (structural ending typically the cadence ultima; phrase length measured `{`→`{`;
  interlocking `}{`; codetta/annexe between `}` and the next `{`). **Non-hierarchical by the standard's own statement.**
- **Key-areas** — contiguous local-key (`localkey`) spans.
- **Cadence-to-phrase alignment** — cadences (detected in L5) marked on the ultima, **usually but not always** at a
  phrase end (DCML: "cadences rarely occur without a phrase ending, but many phrases end without a cadence").

**Out of the validatable core** (no DCML oracle): hierarchical grouping, Caplinian periods/sentences, multi-phrase
**sections**, and prolongation/reduction. Per the verifiability contract (target-arch §2, 2026-06-29) these are **not
ruled out** — they require a chosen alternative-confidence path + an "unvalidated" mark, weighed at design time.
**Proportionality:** Contrapunctus is SOTA-competitive with *no* explicit grouping (it falls out of stable key runs),
so L6 is a deliberate explainability bet — keep it the thin assembly layer, do not let it balloon.

## 2. The reuse landscape — L6 is ASSEMBLY, not new detection
A read-only survey of `src/composing/` shows nearly every primitive L6 needs already exists (built dormant or live):

| L6 input | Source (file : symbol) | Status | L6 use |
| --- | --- | --- | --- |
| Phrase boundaries | `engravingbridge/phraseboundaryview` : `phraseBoundaryTicks()`, `PhraseBoundaryProfile` (graded, marker spikes) | dormant (gated off) | the phrase-segmentation primitive — consume ticks; optionally weight by strength |
| Cadences (type + tonic vote) | `function/functioncadence` : `detectFunctionalCadences`, `FunctionalCadence` | dormant | classify phrase endings; align to phrase ends |
| L5→L6 contract | `function/functionoutput` : `assembleFunctionOutput`, `FunctionLayerOutput` (RN + confidence + open mark + per-region cadences + local key) | dormant | **L6's direct input** |
| Key-areas | `section/…` `KeyArea` (live in `AnalyzedSection`); L3 `keyModeResult` + `keyAlternatives`; `localmodulationdetector`:`LocalKeySpan` (diagnostic) | mixed | group the local-key spans into key-areas |
| **Existing LIVE scattered grouping to REBUILD** | `section/sectioncadencedetection` : `detectCadences` (PAC/PC/DC/HC), `detectPivotChords`; `KeyArea` grouping | **LIVE, key-dependent/circular** | the forward-only rebuild target — L6 unifies these into one clean layer, retired at engage (the L5 pattern) |

So L6's substance is: assemble phrases from the boundary primitive, group the L3 local-key spans into key-areas, align
the L5 cadences to phrase ends, carry open marks through — and **replace the old scattered live machinery**
(`detectCadences`/`detectPivotChords`/`KeyArea`), which is key-dependent and circular, exactly as L5 replaced the
scattered function machinery. Little or no new detection.

## 3. External / SOTA methods (borrow / discard)
- **Phrase-boundary detection — LBDM** (Cambouropoulos; IOI/pitch/rest local-change profile, peak-pick over threshold):
  already the basis of our phrase primitive. **Borrowed; done.** Nothing new to build.
- **Key-area / tonal segmentation — Spiral Array + the Argus algorithm** (Chew; segments by the discrepancy between
  past/future tonal context at each point) and **change-point methods** (graph + change-point structure analysis, 2023;
  local-key regularization, 2024). These validate the *approach* (change-point over tonal context) — but **we already
  have our own** (L3 local-key spans + `localmodulationdetector`), so key-area grouping = **group OUR spans**, not adopt
  a new detector. The literature is corroboration, not a build.
- **Section-boundary detection — CNN barwise section detection** (2025, outperforms audio + block-matching) and the
  unified **AnalysisGNN** (2025; phrase-boundary + section-boundary + cadence as **flat note-level classification**).
  Two takeaways: (a) even SOTA does grouping as **flat boundary identification, not parsing** — confirms our flat scope;
  (b) **sections** are a real, learnable unit but **beyond the DCML flat core** — an extension under the verifiability
  contract, not core L6.
- **Cadence–phrase relationship** (DCML): align L5 cadences to phrase ends; do **not** force coincidence (a phrase may
  end without a cadence; a cadence implies a phrase ending). This is a rule, not an algorithm to import.

## 4. Design implications (for the L6 spec)
1. **L6 is the flat assembly layer:** phrases (primitive) + key-areas (group L3 spans) + cadence-to-phrase alignment
   (L5) + open-mark carry-through. Reuse-not-duplicate; no second detector.
2. **It is a forward-only rebuild** of the live scattered `detectCadences`/`detectPivotChords`/`KeyArea` machinery
   (key-dependent, circular) — built dormant, byte-identical, retired at engage (deferred indefinitely; production out
   of scope).
3. **Sections / periods / hierarchy / form / reduction = extensions beyond the validatable core** — admitted only under
   the verifiability contract (alternative oracle + "unvalidated" mark), weighed explicitly at design time, default out.
4. **Proportionality + dormant-and-measured posture** carry over from L5.

## 5. Open questions to resolve in the design
- **Does our chorale ground truth carry the `{ }` phrase + `|`-cadence annotations?** **✅ RESOLVED (CC corpus check,
  2026-06-29):** **No.** The chorale oracle is **When-in-Rome RomanText + music21** (no DCML `harmonies/` dir for the Bach
  chorales). On the 353-stem gate: **local-key = present** (validatable, 326/353 human + 353/353 music21);
  **phrases = absent** (no `{}`/`\\`) → validate against **score fermatas** (351/353, the fallback oracle);
  **cadences = absent** (0/353 — no `|PAC` etc.). The `{}`/`|cadence` columns exist only in the **DCML-TSV non-chorale
  corpora** (Corelli/Mozart/…: cadence `PAC×209/HC×65/IAC×36/DC/EC`, `phraseend` columns), which `dcml_parser` does not
  currently extract. **Consequence:** key-areas are GT-validatable; phrases are fermata-validatable; **cadence-to-phrase
  alignment has NO direct oracle on the chorale gate** — a verifiability-contract case (alt-oracle or unvalidated mark).
  (Data-hygiene, declared by CC: a stray non-chorale `corelli.xml` in the 353-stem glob; `bwv112.5` lacks a fermata.)
- The exact **L6 output structure** (the flat phrase + key-area + cadence-alignment contract to the display layer above).
- The **cadence-to-phrase alignment rule** (snap an L5 cadence to the nearest phrase end? within what window? what when
  a phrase ends with no cadence, or a cadence falls mid-phrase?).
- The **L5-override ↔ L6-merge division** for the class-(b) duty (L5 §15-6, the standing joint item).
- **Sections: in or out of the core?** (Lean: out — an extension; the DCML core is phrases + key-areas.)

## 6. Validation strategy (user-ratified 2026-06-29) — two-step use of the DCML-TSV oracle
Resolving the cadence-oracle gap (§5) under the verifiability contract, in two sequenced steps:
1. **NOW (for L6) — narrow TSV oracle for phrase + cadence-LOCATION.** Bring the DCML-TSV corpora (Corelli/Mozart/… — the
   `{}`+`|cadence`-annotated repertoire) and extend `dcml_parser` to read the `cadence` + `phraseend` columns. Validate
   L6's **phrase-boundary** and **cadence-LOCATION** outputs (precision/recall of boundary/cadence ticks) — the parts
   **robust to RN errors**. Phrases thereby gain a **second** oracle (chorale fermatas **+** TSV `{}`); cadence-location
   gets its **first**. Caveat: cadence-location has **mild** harmony-dependence (it leans slightly on L4's dominant→tonic
   read) — robust, not immune. **Cadence-TYPE** (PAC/IAC/HC) is harmony-dependent → measured but **caveated, not a clean
   gate** on this repertoire.
2. **LATER (pre-inference baseline) — wide full-pipeline generalization measurement.** At the structural-done /
   pre-inference boundary (with the upstream sync + re-baseline), run the **full L1–L6** on the wider DCML-TSV corpora and
   measure RN + key + cadence + phrase against the full 4-layer GT — the **generalization baseline before inference-
   bettering begins**, so chorale-focused tuning can be checked against generalization (anti-overfit). **Reuses step-1's
   infrastructure** (corpora + parser extension), so step 1 is not throwaway.

Both steps are **measurement / validation-infrastructure, not inference-fixing** (firewall-clean). **Prerequisite
hygiene:** remove the stray non-chorale `corelli.xml` from the 353-stem chorale glob (clean separation of the chorale gate
vs the new TSV validation corpora), re-confirming/attributing the 53/24/53 baseline; note `bwv112.5` lacks a fermata
(1-stem edge for the fermata phrase oracle).

## Sources
DCML Harmonic Annotation Guidelines 2.3.0 (`dcmlab.github.io/standards` — reference, first_phrase). AnalysisGNN
(arXiv 2509.06654, 2025). Barwise Section Boundary Detection (arXiv 2509.16566, 2025). Symbolic Music Structure with
Graphs + Change-point (arXiv 2303.13881, 2023). Chew, Spiral Array / Argus tonal segmentation (INFORMS J. Computing).
Gedizlioğlu & Erol, local-key regularization (2024). LBDM (Cambouropoulos). Reuse map: read-only survey of
`src/composing/` (2026-06-29). Accessed 2026-06-29.