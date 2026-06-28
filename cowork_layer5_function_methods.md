# Architectural Layer 5 — FUNCTION — methods catalog (research-first, pre-spec)

> **Status: research synthesis (2026-06-26), grounds the L5 spec.** Built from three internal source surveys (our own
> function/cadence machinery; the L4→L5 contract; our prior in-repo research) + two external literature passes
> (function-assignment + cadence detection), each primary-sourced. This is the L5 parallel to the L3 key/mode methods
> catalog. **No code; no spec yet** — it catalogs what L5 must do, what the literature establishes, and what we reuse vs
> build, so the spec rests on knowledge, not assumption.

## 0. The two findings that reshape L5

**Finding 1 — L5 outputs Roman numerals, NOT tonic/subdominant/dominant classes (literature: very high confidence).**
Every published autonomous RNA system (Chen & Su 2018; Micchi/Gotham/Giraud TISMIR 2020; AugmentedNet/Nápoles 2021;
ChordGNN 2023) represents and evaluates the analysis as the **RN component tuple** — {local key, primary degree,
secondary degree, quality, inversion, root} — and **none emits a T/S/D head**. AugmentedNet *explicitly lists "tonal
function (T, S, D)" as future work it did not implement.* The word "function" in the ML literature is a documented false
friend: it means the generalized RN components, **not Riemann's *Funktionstheorie***. T/S/D, where it exists (music21's
`analysis.harmonicFunction`), is a **deterministic lookup from the RN**, not a prediction. This matches our own world
exactly: our ground truth (DCML/music21) and our output (`formatRomanNumeral`) already treat "function" as the RN
itself (scale-degree + quality + applied/secondary), and our `harmonicfunctionlayer` is **misnamed** — it does chord-
identity competition, with cadence + functional labeling marked "E4 (planned)" = L5.
➡ **L5's prediction target is the RN.** T/S/D is an optional **derived view** (a thin RN→{T,S,D} table) for
accessibility/explanation, never the primary output. (See §1 for the scoping decision this raises.)

**Finding 2 — L5 is "thin derivation + the resolver", and its real work is concentrated + small (cross-layer budget).**
The architecture already fixed L5 as "the chord symbol read *in* the key — mostly a derivation once L3+L4 are known"
PLUS the ratified O1 role: **the resolver of every upstream "uncertain" mark**, performed at its gated entry by
**selecting among the readings L4 carried** (never re-deriving from notes, never inventing a chord). The measured
function-only residual is small and concentrated: share-tone chords on the chord side, relative-major/minor +
tonicization-vs-modulation on the key side, plus the genuine transition/close ties — everything else is another layer's
budget. So L5 is not a heavy new inference engine; it is **derivation + a constrained selector + cadence/tonicization
arbitration.**

## 1. ★ DECIDED (user, 2026-06-26) — output the Roman numeral; T/S/D is a derived read-out only
**L5's output is the Roman numeral — the most precise, complete analysis.** The tonic/subdominant/dominant labels are a
**lossy summary derivable from the Roman numeral** (a deterministic lookup, music21's `analysis.harmonicFunction`), so
building them as a stored/primary output would be deliberately discarding information and keeping the truncated version.
The user's principle: *as precise as possible beats rounded/masked — do not implement information loss.* The three-role
view is therefore a **trivial on-demand read-out** (a pure formatter), built **only if/when** the accessibility/teaching
display actually wants it; it never drives analysis and is not a stored layer output. The few context-dependent chords
(e.g. iii as tonic- vs dominant-substitute, IV predominant vs post-cadential) are **ambiguities of the three-role
scheme, not information the Roman numeral lacks** — "first-class roles" would *invent* a judgment with no ground truth to
verify, which violates the build-only-what-we-can-verify discipline. **Rejected: a first-class T/S/D analysis.** The
read-out, if built, defaults those few cases to their tonic-side bucket.

## 2. Function / RN assignment — the thin derivation + the relational labels
The base RN (diatonic degree + quality + inversion + chromatic root) is **largely already produced** by L3+L4 +
`diatonicDegreeForRootPc` + `formatRomanNumeral` (which already emits chromatic RN, aug6, and inline secondary-dominant
labels). L5 OWNS and unifies the **function-bearing relational labels** the literature standardizes (adopt the
RomanText/DCML vocabulary — it *is* our ground-truth standard), each with a concrete trigger:
- **Applied / secondary (`V/x`, `V7/x`, `viio7/x`)** — trigger: a raised **secondary leading tone** manufacturing
  dominant function toward a non-tonic degree. *Traps (DCML-documented):* in **major**, the secondary LT of V is
  scale-degree 7 (not #7) — the accidental is in the spelling, the RN root is unaltered; and `/` is relative to the
  **local** key, not global. We have a built+tested but **dormant** `tonicizationlabeler` that already does exactly this
  (V/d, viio/d…) with a chromatic-LT false-positive guard — L5 wires + unifies it (it currently duplicates the
  `formatRomanNumeral` inline path).
- **Neapolitan (`bII6`/`N6`)** — trigger: major triad on **b2̂**, first inversion; predominant. (DCML always `bII6`.)
- **Augmented sixths (`It6`/`Fr6`/`Ger6`)** — trigger: the **b6̂–#4̂** augmented sixth + the degree selector (It+1̂,
  Fr+2̂, Ger+b3̂); chromatic predominants of V. **Ger6 ↔ V7 is pitch-class-identical** — separable **only by spelling +
  resolution**. This is the *same structural class* as our symmetric-dim7 / share-tone churn → L5 must be **spelling-
  aware** here (consume `spellingview`, exactly the Phase-4 primitive + the L4 spelling-pin).
- **Modal mixture (`bVI`, `iv`-in-major…)** — trigger: a borrowed lowered/raised degree; changes quality, **not** key
  (no local-key change). Root prefix `b`/`#`.

## 3. Cadence detection — replace BOTH broken detectors with one correct one
Our two existing detectors are both wrong: the production `sectioncadencedetection` is **circular** (reads the resolved-
key `function.degree`) and **conflates PAC with IAC** (no inversion/soprano test); the dormant key-agnostic
`cadencekeyanchor` **structurally false-positives on I→IV / I→V** (its "leading tone" = the major third, present in every
major triad). The literature (Caplin; Bigo et al. ISMIR 2018; Karystinaios & Widmer ISMIR 2022; Sears et al. JNMR 2018)
gives the corrected design:
- **Detect on an EVENT PAIR (penult → arrival), scored by a feature vector — never a single chord's interval content.**
  The mandatory **sequence** (predominant → dominant → tonic) is what kills the I→IV/I→V false positive.
- **Required features:** bass-degree pair (**5̂→1̂** authentic; →5̂ half), **root-position flags** for both chords (these
  are **bass-derived and robust**), **leading-tone RESOLUTION** (7̂→1̂ across the boundary — *resolution*, not LT
  *presence*), predominant on the preceding beat, and **metric / phrase salience**.
- **★ The "soprano arrival degree" (1̂=PAC vs 3̂=IAC) is theory-standard but implementation-fragile, so DEMOTED in the
  spec (user, 2026-06-26).** It needs the *structural melody*, and the **highest sounding voice is not reliably that line**
  (orchestral doubling; barbershop lead *below* the top). So the spec makes the perfect/imperfect call on the
  **bass-derived inversion** criterion and uses the top-voice arrival only as a *soft, optional* confidence nudge in
  homophonic textures — never the hard test. The tool does not attempt melody identification. (See L5 spec §5.2 / §15-0.)
- **Apply the cadential-6/4 collapse FIRST** — a 2nd-inversion tonic-spelled sonority over a held 5̂ bass proceeding to a
  root-position dominant is **dominant function (V6/4–5/3)**, not a tonic arrival; collapse the pair so the cadential
  bass reads 5̂→1̂. (Do not let the 6/4's tonic spelling register as tonic.)
- **Typology (Caplin-standard, operational):** PAC (root-pos V→I, soprano 1̂); IAC (V→I failing inversion/soprano, or
  viio6 substitution); HC (terminal **root-position** V — prefer triad; **Phrygian** = iv6→V, bass semitone 6̂→5̂);
  Deceptive (cadential V → vi); Plagal + IAC = **lower confidence** (Caplin demotes plagal to post-cadential); Evaded
  (arrival abandoned/re-launched). **HC detection is the universally weakest link** — expect lower confidence there.
- **For Bach chorales: gate cadence candidates on the fermata / phrase boundary** — the cheapest, most reliable phrase-
  end signal; removes mid-phrase false positives by construction. We already have the primitives: `endsPhrase` (fermata/
  piece-final) and `chromaticLeadingTone` on `cadencekeyanchor`.
- **Direction of inference (the cure for circularity):** detect cadences **key-agnostically**, then have each surviving
  candidate cast a **weighted tonic vote** (weight = bass-5̂→1̂ ∧ LT-resolution ∧ V7/tritone-resolution ∧ metric/fermata/
  piece-final salience). Cadence **confirms** key/tonic; it never reads an already-resolved key.

## 4. Tonicization vs modulation — the function-level arbitration
The literature's near-universal criterion: **tonicization has no cadence in the new key; modulation incorporates at
least one cadence (PAC/IAC/HC) in the new key.** The boundary is a true continuum graded by cadence-confirmation +
persistence, **not a duration constant** (DCML's operational rule: stay in the old key via `/x` for fleeting
tonicizations; change the local key "only when the music genuinely stays in the new key"). AugmentedNet models Key
(modulation) and Tonicization (`/`) as **two separate heads** — mirroring the notation. ➡ L5 default = **tonicize (stay
in key, `/x`)**; promote to modulation **only on cadence-confirmation in the candidate key + persistence**, implemented
as a **change-cost / hysteresis** decision over the L3 local-key layer (Temperley/HMM style), the gated forward-recompute
the architecture already specifies. This is also where the **TPC-spelling key signal belongs** (our prior measurement:
the spelling term helps modulation regions but hurts stable regions as a standalone L3 term — *function gates it here*).
Expect irreducible fuzziness on fast-harmonic-rhythm chorales; defensible tonicization-vs-short-modulation disagreement
is a **non-error**.

## 5. The resolver — selecting among L4's carried readings (the O1 job)
L5 consumes, per abstained slice, L4's `OpenQuestionLabel` (readingA, readingB, the `AmbiguityKind`, the disputed axis)
+ `SliceConfidence` + the ranked `alternatives`, and **selects** (never re-derives). Mapping the measured abstain
buckets → the resolution evidence L5 brings:
- **Transition (~47%)** — thin slice heading into a *different* next chord → resolve by the **progression / cadential
  continuation** (does the fragment belong to the prevailing harmony or the arriving function?).
- **Close (~25%)** — general low-margin tie → break with **functional/cadential plausibility** + the bass-degree prior.
- **ShareTone (~20%)** — pc-identical readings (Am6↔F♯ø7) → resolve by **progression context / function** (which reading
  participates in a real progression toward the next function).
- **RelativePair (~3.4%)** — roots a minor third apart, major↔minor (C↔Am) → the **key/tonic decision**, resolved by the
  **cadence tonic-vote** (§3) + same-collection center.
- **Insufficient (~4.6%)** — genuinely too thin → select from carried readings on function, or accept the abstain.
- **Class-(b) override duty:** L5 (with section-grouping) must drive the **86 projected class-(b) transients** to zero —
  fine-grain sub-slice wrong commits that the coarse functional/cadential context contradicts; L5 **overrides** them at
  engagement. (No new class-(b) exists in production today — the decoder is dormant; these are projected at engage.)
*(Caveat: the L4 `NoteMembership`/`contestedPc` axis is reserved/unpopulated this increment — L5's input is Root/Quality
open questions only; do not assume a membership dispute arrives.)*

## 6. The bass-degree / Rule-of-the-Octave prior (soft)
The partimento Rule of the Octave maps each **bass** scale-degree to a first-choice harmony (1̂/5̂/8̂→stable 5/3;
4̂/7̂→6/5,6/3; 2̂→inverted dominant-seventh; descending 6̂→applied-dominant), and functional-bass theory biases bass
5̂/7̂→D, 4̂/2̂→S/predominant, 1̂/3̂→T. It is theoretically authoritative and **largely unexplored as an explicit
computational prior** — a defensible, **low-risk SOFT prior / tie-breaker** for L5's resolver (§5) and cadence test
(§3), **never a gate** (it is many-to-one, direction-dependent, overridden by sequence/cadence/applied context). Pairs
naturally with our existing inversion/bass work.

## 7. Reuse vs build
**Reuse (already in-repo):** `formatRomanNumeral` (RN incl. chromatic/aug6/inline-tonicization emission);
`diatonicDegreeForRootPc` (scale-degree); the **dormant `tonicizationlabeler`** (applied-chord labeling + chromatic-LT
guard — wire + unify); the **dormant `cadencekeyanchor`** primitives (`endsPhrase`, `chromaticLeadingTone`, key-agnostic
frame — rebuild the detector logic per §3 on these inputs); the proto-functional heuristics (`wSeqBonus` V→I,
`wDimBonus`/`resolutionEdgeBonus` LT-resolution, the function-bearing gates G-E/I/J/K/L) as **priors**; `spellingview`
(for the Ger6/applied spelling-awareness). **Build:** the correct **event-pair cadence detector** + tonic-vote; the
**tonicization-vs-modulation arbiter** (cadence-confirmed hysteresis over L3 local keys); the **resolver** (select-among-
L4-readings per §5); the unification of the two tonicization paths; the optional T/S/D derived view (§1).

## 8. Out of scope (firewall / later layers)
- **Prolongation / reduction** (GTTM time-span & prolongational reduction; Schenker) — needs grouping+meter+whole-piece
  recursive parsing + scarce expert annotation, below human accuracy computationally → **L6/future, not L5.** Borrow only
  a light metric/phrase-position weight.
- **Accuracy tuning** of the cadence/function thresholds on hard cases → **Phase B** (the firewall), after the layer is
  built right.
- **Joint key+chord neural prediction** (AugmentedNet-style one-step) — rejected by our decomposition; the gated forward-
  selection is the design.

## 9. Open questions to settle in the spec
1. The §1 T/S/D-derived-view decision (user).
2. Where L5 physically lives + the rename of the mislabeled `harmonicfunctionlayer` (it's chord-identity competition,
   not function) — a structural/naming step to schedule (coordinate with the joint-L5 engagement, like the other
   migration debt).
3. The exact L5↔L3 forward-recompute contract for a cadence-confirmed modulation (the gated localized recompute the
   architecture specifies) — the one place L5's decision feeds a bounded re-run of L3, and the boundary that must not
   become a back-edge.
4. Whether the cadence detector is its own L5 sub-unit consumed by both the tonicization arbiter and the resolver
   (likely yes — it's shared evidence).
5. Pull `backlog_extended_harmonic_functions.md` + `backlog_cadence_i18n.md` (project memory, CC-readable on Windows)
   before finalizing the function vocabulary + cadence i18n.

## Sources
Internal: the three survey agent reports (this session); `cowork_layer4_chordsymbol_design.md` §15-O1; `CLAUDE.md`
cross-layer-budget; `cc_phase5b_stepM_measure_report.md`. External (primary): Chen & Su ISMIR 2018; Micchi/Gotham/Giraud
TISMIR 2020; Nápoles López et al. AugmentedNet ISMIR 2021; Karystinaios & Widmer ChordGNN ISMIR 2023 + cadence-GNN ISMIR
2022; Bigo/Feisthauer/Giraud/Levé ISMIR 2018; Sears/Pearce/Caplin/McAdams JNMR 2018; Caplin JAMS 2004 / OUP 2024;
Aldwell & Schachter; RomanText (ISMIR 2019) + DCML Guidelines 2.3.0; Sanguinetti / Gjerdingen (Rule of the Octave);
Lerdahl & Jackendoff GTTM; music21 `analysis.harmonicFunction` / `roman` docs.
