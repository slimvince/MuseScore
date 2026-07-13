# The evidence inventory — every hint each layer finds or could find, who needs it, and the circularity map

> **Cowork, 2026-07-12, at the user's direction:** enumerate ALL the hints/clues each
> layer discovers that should be passed forward; per layer, add what that layer KNOWS
> but nobody ever discussed as downstream-useful; then assess which serve the key
> layer; then map the alleged circular dependencies honestly — with the complete list
> in hand, see whether any circle is real and how each is broken. Sources: the five
> certified audits (which dispositioned every published/siloed/trapped fact), the
> siloed-facts sweep, the diagnosis, the mechanism report, and the research grounding.
> Status labels per fact: PUBLISHED (on the layer's output surface today) · SILOED /
> TRAPPED (computed, unavailable or dying at a boundary — register row cited) ·
> DORMANT (built, gated off) · INPUT (present in the score, read or unread) ·
> UNDISCUSSED (knowable by that layer; never before proposed as downstream evidence).

## 1. The score itself (the input surface — facts that exist before any analysis)

- Notated pitches with SPELLING (tonal pitch classes — F♯ vs G♭ as the composer wrote
  them). INPUT, carried at the note layer, consumed today by one pin only (OI-15).
  **This is the fact that dissolves the spelling circularity — see §8.**
- Notated key signature(s), INCLUDING mid-piece changes. INPUT; read once at start,
  changes never re-anchored (OI-94).
- Declared mode from the file format. INPUT; siloed to the key path (OI-78).
- Time signatures; barlines including double/section barlines; repeats.
  INPUT; time signatures consumed by metric weights; the rest UNDISCUSSED —
  a double barline is a section boundary hint, directly useful for phrase-aligned
  key spans.
- **Fermatas.** In Bach chorales the fermata IS the phrase-end marker — the single
  most reliable phrase-boundary fact in exactly our corpus, and the comparable
  product's biggest key-detection win came from a phrase-end ("pseudo-fermata")
  alignment fix. UNDISCUSSED as key evidence; not in the note model's 11 documented
  facts. Cheap to read; enormous leverage for transition costs and cadence location.
- **Rests/silences as phrase ends** (user-raised 2026-07-12, pairing with the
  fermata fact above): a sufficiently long rest signals a phrase end just as a
  fermata does. Status: HALF-EMBODIED — the dormant phrase-boundary view is already
  a silence-based phrase-end detector, gated off, with "sufficiently long" a
  hand-set 240-tick threshold (one of the OI-87 unfit constants). The composite
  publication the key layer wants: phrase-end facts from fermatas AND long rests
  together (fermatas are a chorale convention; rests generalize to other
  repertoire), the silence threshold fit rather than guessed. Grace notes
  (embellishment hints); slurs/articulation (phrase shaping, weak); lyrics/verse
  structure (chorale phrase structure — UNDISCUSSED, probably redundant with
  fermatas); tempo/character markings (style/preset hints, weak); pedal lines
  (sustain — affects which pitches actually sound together; the known piano-pedal
  gap in the backlog); instrument/part names (voice identification).
- Existing chord-symbol / Roman-numeral / Nashville annotations IN the score —
  recognized as flags, never read (OI-80). A user-provided ground-truth hint the
  analysis ignores entirely.

## 2. Layer 1 — the note model (the fact layer)

- Per note: pitch class, octave/register, onset, duration, tie state, voice and
  staff identity, spelled pitch. PUBLISHED at the model — **but voice/staff identity
  is DROPPED at the shared tone surface** (OI-74), which is why everything above the
  note layer is voice-blind (the structural root of several silos).
- UNDISCUSSED from this layer: **register/bass-register identity as evidence**
  (the bass voice's motion is the strongest functional signal there is — see layer
  1.5); octave doubling counts (which pc the texture emphasizes); courtesy
  accidentals versus functional accidentals (a NOTATED accidental outside the
  signature is a tonicization/mode event in the composer's own hand — a raised
  seventh in minor is literally written on the page).

## 3. Layer 1.5 — the derived views

- Metric weights: region-level weights PUBLISHED; **per-note beat weight
  decoder-private** (OI-82). Beat strength is evidence for cadence arrival and for
  which tones are structural.
- Weighted pitch-class collections per span (with repetition and cross-voice
  boosts — constants unfit, OI-87). PUBLISHED to the key path (its emission input).
- Bass onset/sub-boundary facts. Computed; consumption narrow.
- **Phrase-boundary view: ends-a-phrase facts. DORMANT, gated off** — the exact
  fact the transition-cost design wants (and fermatas §1 would make it sharper).
- Per-note melodic signals (step/leap/suspension — `StepwiseSignals`): **TRAPPED
  inside the decoder's membership internals** (OI-72).
- Texture classification (homophonic/polyphonic; the voice-leading axis): DORMANT.
  The comparable product routes its key detectors BY texture — never discussed here.
- UNDISCUSSED from this layer: **bass MOTION intervals** (a bass falling a fifth
  into a strong beat is the dominant→tonic skeleton — computable voice-aware from
  the model without any chord knowledge); **soprano scale-degree at phrase ends**
  (cadence formulas constrain the melody note — a PAC wants the tonic on top);
  melodic contour per voice; parallel-motion facts (voice-leading legality —
  built in the dormant axis).

## 4. Layer 2 — segmentation

- Slices (change-point boundaries), slice durations, explicit empty slices.
  PUBLISHED.
- UNDISCUSSED from this layer: **boundary STRENGTH** (how decisive the change-point
  evidence was — a graded boundary confidence instead of a binary cut; useful for
  tonicization-boundary arbitration and for the segmentation-edge artifact class);
  **harmonic rhythm** (the pattern of slice durations — accelerating harmonic
  rhythm approaching a phrase end is a classic cadence-approach signal, textbook
  theory, computable purely from slice durations); anacrusis/pickup detection.

## 5. Layer 3 — key/mode (the layer under redesign)

- Produced today: per-region key+mode; the alternatives list (top-4, margins
  DISCARDED — OI-75/OI-81); a sequence-margin confidence (diagnostics only); the
  full 252-state per-slice emission scores (dump-only); the declared-mode
  pass-through.
- UNDISCUSSED facts this layer KNOWS and could publish:
  - **The collection/tonic split.** The decode is often CONFIDENT about the pitch
    collection (one flat) while ambiguous only about the tonic within it (F major
    vs D minor). Publishing "collection: confident; tonic: open between these two"
    instead of one flat key guess is the single most consequential unpublished fact
    in the system — because our own measurements show the chord layer's decisions
    are almost entirely collection-driven (roots are key-invariant under collection
    siblings). The chord layer could consume the confident half while the tonic
    stays honestly open for cadence/grammar evidence to settle. See §8.
  - Per-slice key AMBIGUITY (the emission near-tie structure — where the music is
    locally keyless/transitional; useful to the chord layer's symmetric-rotation
    handling and the function layer's open marks).
  - Boundary-margin facts (how close the decode was to placing a key change one
    slice earlier/later — tonicization-boundary evidence).
  - Which pitch classes DROVE the key choice (evidence decomposition — useful for
    explaining and for spotting emission pathologies).

## 6. Layer 4 — chord

- Produced today: the committed identity (root/quality/inversion/bass/extensions);
  capped alternatives (voicing-biased, OI-9); the raw candidate grid + threshold
  (in-memory); membership verdicts (chord tones vs non-chord tones) — **dying at
  the layer-4→5 boundary** (OI-73); abstention margins; a diatonic-to-key flag.
- UNDISCUSSED / under-discussed from this layer:
  - **Dominant-SHAPE detection as a key vote.** A dominant-seventh-shaped sonority
    implies a tonic a fifth below BY ITS SHAPE, before any key is known. This is
    the named-but-never-built dominant-implication channel (OI-94(b)/OI-68) — the
    strongest chord-derived key hint that needs NO key input.
  - **Leading-tone-resolution events** (a note a semitone below a candidate tonic
    resolving up at an arrival — key-agnostic, voice-aware).
  - Non-chord-tone classifications per note (passing/neighbor/suspension) — the
    anchor-redesign topic; also cleans the key layer's emission input (§8).
  - Chromatic-alteration events (a sounding pc outside the prevailing collection =
    a tonicization signal at its tick).
  - Per-chord decision margin (how decisively the winner won — exists internally,
    truncated at the carry).

## 7. Layer 5 — function (dormant) and the input annotations

- Produced (dormant, certified): functional labels; **cadence detections WITH a
  tonic+mode VOTE and a weight** (the key-agnostic tonic-voting machinery);
  tonicization-versus-modulation decisions; progression licensing
  (grammaticality); open marks; combined confidences.
- UNDISCUSSED: **progression-grammaticality scored UNDER EACH CANDIDATE key** (the
  user's channel — design opening, transition option (e)); the piece's cadence/
  phrase MAP as a global skeleton (where the piece's arrival points are — feeds
  phrase-aligned key spans from the top down); a harmonic-tension curve (weak,
  research-flavored).

## 8. Which of it the KEY layer wants — and the circularity map, faced honestly

**The key layer's shopping list, from the inventory above:** fermatas + phrase-end
facts (transition costs); bass-motion dominant→tonic skeletons and dominant-shape
votes and leading-tone events (cadence-family evidence); notated spelling + notated
accidentals (emission evidence); the declared mode + signature changes (anchoring);
harmonic rhythm + boundary strength (cadence approach, tonicization boundaries);
NCT-cleaned tone collections (emission input hygiene); progression grammaticality
under candidate keys (tonic arbitration); chord-symbol annotations where present
(user-provided truth). Plus its own unpublished facts (the collection/tonic split,
the ambiguity and boundary margins) — published for downstream honesty.

**Now the circles, one by one. The user's suspicion is right: named completely,
each alleged circle either dissolves or has a known, ratified break pattern.**

1. **Key ↔ spelling — NOT CIRCULAR FOR US.** Temperley worried spelling might need
   the key (in audio/MIDI it does). We read NOTATED scores: the composer already
   spelled every note. Spelling is INPUT, not inference. The circle exists only for
   audio systems; ours is broken by the source material itself.
2. **Key ↔ cadence — BROKEN BY THE KEY-AGNOSTIC FORM.** The old detector was
   genuinely circular (it computed degrees FROM the key — the June dossier's
   finding). The rebuilt machinery votes for a tonic FROM root motion, quality, and
   the raised leading tone — no key input. The circle was an implementation
   artifact, already designed away; what remains is plumbing (where the votes are
   consumed) plus the two divergences (OI-118/OI-119) gating its use.
3. **Key ↔ chord — MOSTLY DISSOLVED BY THE COLLECTION/TONIC SPLIT; the remainder
   has two ratified break patterns.** Our own measurement: chord roots are
   key-invariant under collection siblings — the chord layer needs the COLLECTION
   far more than the TONIC. So: the key layer publishes the confident collection
   early; the chord layer runs on it; the cadence/grammar/dominant-shape evidence
   (all computable from chords WITHOUT a settled tonic) then arbitrates the tonic.
   No cycle — a pipeline: collection → chords → tonic-evidence → tonic. For the
   measured-rare cases where even the collection is uncertain AND chords would
   change under the alternatives: the ratified confidence-weighted forward-override
   (a localized recompute, no back-edge), and behind it the gated minority joint
   step — measured mostly unnecessary (the shelved step), kept as the bounded
   escape hatch.
4. **Chord ↔ non-chord-tone — SAME SHAPE, SAME BREAK.** NCT classification needs a
   chord hypothesis; chord identification wants NCT-cleaned tones. The comparable
   product resolves it exactly as our architecture does: chords first, NCTs
   classified against them, with the forward-override for the rare case where the
   NCT reading overturns the chord. Provisional-then-refine, not circular.
5. **Key ↔ progression-grammar — BROKEN BY ENUMERATION.** Grammaticality is scored
   PER CANDIDATE key over the same chord sequence — the key is a hypothesis index,
   not an input. Nothing feeds back; it is a scoring dimension over alternatives
   the key layer already carries.

**The general law all five instances obey:** a circle in the ABSTRACT ("A needs B,
B needs A") becomes acyclic in the CONCRETE when one of: the score already contains
one side (spelling, signatures, fermatas, annotations); a key-agnostic form of the
evidence exists (tonic votes, dominant shapes, bass skeletons); the dependency is on
a COARSER fact that is already stable (the collection, not the tonic); or the
ratified forward-override/joint-minority patterns cover the measured-rare remainder.
Every alleged circle above fell to one of these. None survived as a true blocker —
which is the answer to the user's worry: the circularity challenge, named
completely, stops nothing.

## 8b. Declared future consumers, named by the user (2026-07-13)

**The intonation/tuning feature (held long-horizon, register row OI-62) will consume
the published analysis facts:** knowing the mode, the chord, its function, and the
progression enables just-intonation tuning decisions — especially in the TIME
dimension (staying in tune over time versus allowing controlled drift). This is a
concrete instance of the publish-evidence-broadly rationale: a consumer none of the
producing layers were designed for, recognizable only because the facts are visible.

**Explainability (user, 2026-07-13): the end user may want to know HOW a mode, chord,
or function was inferred.** If the evidence trail behind every inference is published
— which pitch classes drove the key, which cadence vote confirmed the modulation,
which margin separated the winner from the runner-up, why the analyzer abstained —
then "show me why" is a late-bound DISPLAY consumer of facts that already exist, not
a new analysis. Much of the raw material exists today as internal diagnostics (the
chord-diagnosis replay, the dormant function machinery's structured open marks and
ambiguity kinds, the ranked-candidates-plus-margins confidence contract); the gap is
publication, which is wave 3's job anyway. A register row for the feature follows at
the next free number (numbers are in flight in the current CC session).

## 9. What this inventory changes

The design opening's decisions gain a concrete evidence menu: the emission decision
should consider NCT-cleaned collections and notated accidentals, not only spelling
profiles; the transition decision gains fermatas (likely the cheapest high-value
fact in the whole inventory for our corpus) and harmonic rhythm; the output-surface
decision becomes richer — the collection/tonic split is the headline publication
candidate; and layer 2's boundary strength joins the tonicization work. Per the
fact-publication corollary, every fact adopted from this inventory gets a named
consumer at adoption time; the rest are declared dormant here rather than silently
ignored. Nothing in this document is a build decision — it is the menu the design
conversation orders from.

*Cross-references: OI-72/OI-73/OI-74/OI-75/OI-78/OI-80/OI-81/OI-82 (the silo rows
this inventory would resolve), OI-15 (spelling), OI-94/OI-68 (dominant channel),
OI-118/OI-119 (cadence gating), OI-9 (carry truncation), the five certified audit
reports (the per-layer fact dispositions), `cowork_key_layer_design_opening.md`
(the decisions this feeds), `cowork_key_drift_research_grounding.md` §2–§3.*
