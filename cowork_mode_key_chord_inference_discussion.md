# Mode/key + chord inference — where and how: the discussion basis

> **Cowork, 2026-07-12.** Opened per the register: the OI-84 certification plan completed
> and the user's held question (register rows OI-43/OI-44) opened. This document is the
> Premise-Gate opening the discussion is required to start from (CLAUDE.md #17): the
> premise ledger with every load-bearing claim labeled FACT / THEORY / ASSUMPTION, a
> written quantitative prediction per assumption recorded BEFORE anything is measured,
> the candidate placements checked against the layer rules, and the read-only
> measurement that must precede any build decision. Nothing here authorizes a build.
>
> **The question, verbatim (the user, from the handoff):** *"In the current pipeline the
> chord under an alternative key is never computed. Why do we not compute all chords for
> all reasonably-likely modes/keys? THEN we can rank them. Maybe the top chord
> alternative is inferred based on another key/mode than the highest-ranked key/mode.
> The probability that the most likely chord is ALWAYS found using the most likely
> mode/key is ZERO."*

## 1. The premise ledger

**Facts (each cited to a measurement or to certified-audit findings):**

- FACT — The one existing measurement (the arc-12 probe,
  `cc_engage_stage3_joint_measure_report.md`, corpus `c50002fee1`) tested the CHORD
  axis only, under a key-first framing: decode under the argmax key, re-decode under
  the carried alternative keys, grade ROOT flips. Result: net corrected-minus-harmed
  +9/+3/+10 regions per preset over ~6,200 graded regions (+0.05–0.16 percentage
  points), oracle ceiling +0.6 points, chord flips under a carried key on only
  1.4–1.5 % of regions, and the carried alternatives are diatonic-collection siblings —
  which is WHY the chord axis barely moves. These numbers bound the chord axis over the
  carried-key menu and survive any framing.
- FACT — That measurement never graded the KEY axis. Whether chord evidence re-ranking
  the KEY improves key correctness is unmeasured (the OI-43 sharpening, 2026-07-11).
- FACT — The ratified baselines (CLAUDE.md): root-agree 63.36 / 62.37 / 63.25 %,
  key-agree 68.13 / 64.43 / 67.50 % (Baroque/Jazz/Default). About a third of graded
  duration disagrees on the key — more headroom than on the root, and the cross-layer
  caveat names the note-identical key-disagreement class (relative major/minor,
  tonicization-versus-modulation) as the genuinely function-shaped remainder on the
  key side.
- FACT — The key layer already computes and carries per-region key alternatives and a
  sequence-margin key confidence, and NO production code consumes them (register row
  OI-75; layer-3 audit). The closeness of the runner-up key is computed and then
  discarded inside the analyzer (row OI-81). The inputs a joint ranking needs are
  already produced and currently wasted.
- FACT — The dormant chord decoder is a pure function of (slices, key): re-decoding the
  chord under a different key requires no new machinery (layer-4 decoder session,
  certified; `chordslicedecoder` takes one key per call). Its alternatives cap binds on
  100 % of slices (the carry-truncation row OI-9), and on the pinned corpus it commits
  34.4 % / inherits 3.0 % / abstains 62.6 % of slices — the chord axis carries real
  uncertainty of its own.
- FACT — Half of the joint machinery already exists, built and gated OFF: the key-state
  lattice with a Viterbi key-transition prior and a chord-to-key coupling term
  (`decideJointKey`, `section/jointkeydecision.{h,cpp}`, behind
  `setJointKeyWiringEnabled`), with the chord re-decode axis explicitly deferred "to a
  faithful mechanism" (layer-3 audit; `cowork_joint_key_chord_design.md`).
- FACT — The dormant layer-5 cadence/modulation machinery is audited and certified,
  with two signed-rule divergences to reconcile before it engages (rows OI-118/OI-119).
  Cadence evidence is a planned key-relevant channel, relevant to any joint ranking's
  evidence set.
- FACT — All five certifications are granted; the remaining Stage-3 entry-gate items
  are OI-1…OI-7, and the resolver defusals (OI-1/OI-2) still gate any layer-5 output
  reaching production. A revived joint step would be built at the engagement stage,
  not before (#8).

**Theory (published research answering this specific question — the grounding document
`cowork_functional_analysis_research_grounding.md` §3):**

- THEORY — Joint modeling of the key↔chord dependency beats sequential pipelines, and
  the win concentrates on hard/ambiguous cases (Raphael & Stoddard 2004 — key and
  chord as ONE hidden state; Pauwels & Martens 2014; Wu & Yoshii 2022, whose taxonomy
  names the sequential coupling as the pipeline to escape).
- THEORY — The recurring fix is a beam of (key, chord) hypotheses with a key-transition
  penalty, NOT committing to a key first (grounding implication 3).
- THEORY — Magnitude realism: where quantified, the joint uplift is low single-digit
  points per task, concentrated qualitatively in hard-case disambiguation
  (AugmentedNet; Papadopoulos & Tzanetakis). Expectations should be set there — the
  question is WHERE the points land (the key axis), not whether they are large.

**Assumptions — each with the written quantitative prediction (#17(b)), recorded now,
before measuring. These are Cowork's grounded estimates, stated to be checked, not to
be right:**

- ASSUMPTION — Chord evidence re-ranking the key corrects more key-disagreement than
  it harms. PREDICTION: on regions where a joint (key, chord) ranking prefers a
  non-argmax key, the committed key flips on 3–8 % of graded regions, and the flips
  are net-positive on key-agreement by at least +0.5 and at most +2.0 percentage
  points of duration per preset. If the measured net is below +0.3 points, the joint
  step stays shelved on the key axis too.
- ASSUMPTION — The win concentrates where the key layer is already unsure.
  PREDICTION: at least 70 % of the correct key flips occur in the lowest quartile of
  the carried key-confidence (the sequence margin), and the flip rate in the top
  quartile is under 1 %. If flips spread evenly across confidence, the gating design
  is wrong and the mechanism is riskier than designed.
- ASSUMPTION — The carried key menu is wide enough; "all reasonably-likely keys" ≈ the
  alternatives already carried. PREDICTION: in at least 80 % of key-disagree regions,
  the ground-truth key is PRESENT in the carried alternatives menu. This is measurable
  read-only and decides whether menu-widening is a separate owed item.

## 2. Where — the candidate placements, against the layer rules

- **The bounded coupling step at the layer-3/4 seam, publishing forward to layer 5**
  (the architecture already designed at `cowork_joint_key_chord_design.md`): generalize
  the built `decideJointKey` by adding its deferred chord axis — a beam of (key, chord)
  hypotheses, the chord re-decoded under each carried key by the pure decoder, the
  key-transition prior reused, one settled pair published forward. Respects the layer
  rules (no back-edge: the step re-ranks the key inside its own bounded closure);
  reuses both built decoders; the build items are already enumerated in that design.
  What changes versus the shelved version is only the FRAMING of what it optimizes and
  how it is measured: rank pairs jointly and grade BOTH axes, rather than deciding the
  key first and grading only root flips.
- **A single unified (key, chord) hidden state** — the research's single-state model.
  Rejected at design time on the unification and layer rules (it discards and rebuilds
  two working decoders for a modeling choice the recipe doesn't require); it stays the
  fallback if the bounded step measures insufficient AND the measurement says the loss
  comes specifically from the factored structure.
- **Sequential kept, coupling term only** — the already-built chord-to-key coupling
  score inside `decideJointKey`, enabled without any chord re-decode. Cheapest; but it
  cannot surface a chord from a non-top key, so it does not answer the user's
  question; it is the fallback if the measurement says re-decoding pays nothing even
  on the key axis.

The choice among these is made AFTER the measurement below, not in this document.

## 3. The owed read-only measurement (the funnel: desk-simulate → probe → build)

1. **Desk simulation first (#17(c)):** hand-trace the joint ranking through 3–5 real
   key-disagree cases from the known failing sets (the note-identical relative-key
   class — e.g. the `bwv352` family named in the cross-layer caveat), answering FIRST
   "does the mechanism fire here?" (is the true key in the carried menu; does the
   re-decoded chord actually differ), THEN "which term moves, by how much."
2. **The probe:** extend the existing arc-12 instrument (`--dump-joint-probe` +
   `measure_joint_probe.py`) to grade the KEY axis: for every region where the joint
   ranking prefers a different (key, chord) pair, compare the KEY against the DCML
   ground truth on the established robust-unit substrate (the same key-agreement
   grading the ratified baselines use), alongside the already-graded root axis. Also
   measure the menu-containment prediction (ground-truth key present in the carried
   alternatives), which needs no ranking at all.
3. **Instrument establishment first (#19):** the extended probe grader is established
   before its numbers are read — the key-agreement column cross-checked against the
   committed robust-stop reference on unchanged regions, and the abstain-aware caveat
   (row OI-33) honored so coverage cannot flatter the result. The OI-140 hard-stop
   hardening (the silent ground-truth-parse catch in the governing stop) should land
   before any adoption event leans on the automated stop, and is noted here as the
   priority instrument item.
4. Everything above is read-only. A build decision — reviving the joint step at the
   engagement stage, keeping it shelved, or re-scoping — is the user's, taken on the
   probe's numbers against the predictions written in section 1.

## 4. What this settles when done

The joint step's single declared status (row OI-44): the design is delivered; the
build was shelved on a chord-axis-only measurement; this discussion either revives it
(key-axis case measured and positive, built at the engagement stage in the already-
designed bounded form), keeps it shelved (key axis also measures out), or re-scopes it
(for example: menu-widening first, if the containment prediction fails). Whatever the
outcome, the carried key alternatives finally get their consumer or their honest
retirement — closing the fact-publication violation they currently embody (OI-75).

*Cross-references: OI-43/OI-44 (the question and status), OI-75/OI-81 (the wasted key
facts), OI-9 (carry truncation), OI-118/OI-119 (cadence machinery divergences),
OI-33/OI-140 (instrument caveats), `cowork_joint_key_chord_design.md` (the bounded
architecture), `cowork_functional_analysis_research_grounding.md` §3 (the theory),
`cc_engage_stage3_joint_measure_report.md` (the chord-axis measurement this reopens).*
