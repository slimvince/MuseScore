# Scoped Constrained-Joint Inference — Design (the back-half build)

> **DRAFT — ratification-gated.** Cowork design, 2026-06-15. Implements the **ratified**
> `docs/architecture_joint_inference.md` (user ratified the shape 2026-06-15) at the size the investigation
> measured (`cc_joint_architecture_dossier.md`): genuinely-coupled core ~13.5% → **scoped-joint / two-pass,
> not a full lattice**; hard-constraint safety PASSES; reading-shaped producers are SOFT; A confirmed, B
> reserved for the ~111 dim7/aug floor. **Key-axis first. Measure-first build. No code until this is ratified.**

---

## §1 — What this builds, and what it replaces

A **constrained joint decision** per analysis position: **hard constraints** prune/pin the hypothesis space;
**soft scores** rank the survivors; a **scoped joint decision** resolves only the ~1-in-7 positions where
chord and key are *mutually* ambiguous. It **replaces** the current local key resolver + its hysteresis +
the **post-hoc gate layer (Gates A–L)** — those gates were the local pipeline's *compensation* for not
being joint; the constrained-joint decision subsumes them (this dissolves **deferred-refactor #2**, §9).

**Structure (two-pass with a scoped joint core), respecting the measured residual:**
1. **Vertical chord candidates** (key-independent) — the oracle's per-position candidate set.
2. **Hard-constraint pruning/pinning** (§3) — disqualify violators; where a unique survivor remains, PIN it
   (the measured 41% + the safe vertical-chord majority).
3. **Key pass** (§6, built first) — soft scores + the global key path resolve key-only ambiguity (26.3%);
   the **scoped joint decision** (§5) resolves the jointly-coupled core (13.5%).
4. **Chord refinement** (later) — soft, key-informed, resolves chord-only ambiguity (19.2%).
5. **Function** — chord + established key → Roman numeral (downstream).

## §2 — The hypothesis space

Per position: candidate **(chord-identity, key/mode)** pairs. Chord candidates from the vertical oracle;
key/mode candidates from the local key evidence + the cadence-derived local-tonic hypotheses (key-agnostic).
Function is *not* in the joint space — it is a deterministic downstream read of (chord, key).

## §3 — HARD constraints (the validated, safe set — §safety PASSED)

Only these (measured ~0% vertical error; everything else is soft):
- **Raw facts:** the sounding pitch-class set (as a set), the bass pc, metric weights.
- ⚠ **The notated key signature is NOT hard — CORRECTED by J-key-i (2026-06-15).** The design originally
  listed the signature *fifths* as a reliable hard fact. J-key-i measured the fifths-as-hard pin and it
  **fails the safety gate at ~17% (56 stems)** on the Bach chorale corpus — partial/modal (Dorian)
  signatures whose fifths do not match the DCML key (bwv254/265: D minor notated 0 flats). The signature
  is therefore a **soft prior**, and the home key is established by **note-based home-key inference**
  (J-key-ii), not pinned from the signature. (`cc_j_key_i_report.md` §6a; Cowork-verified at source.)
- **Complete-clear-vertical-chord:** a complete, unambiguous triad/7th *as a vertical sonority* pins the
  chord identity (root+quality). This does NOT assert chord-tone-ness of every sounding note (suspensions/
  pedals remain soft), and does NOT pin function or key.
Hard constraints **disqualify** any hypothesis that violates a raw fact and **pin** where a unique survivor
remains. **They are immovable — no soft score can override them** (this is the −7-wall-in-reverse safety
property, structurally enforced). Any constraint that fails the safety gate (pins a wrong DCML answer) is
demoted to soft — the investigation already cleared the §3 set.

## §4 — SOFT scores (everything reading-shaped — measured to pin wrong as "hard")

All ranking evidence is soft, including the producers the dossier measured pin-wrong: **cadence anchor
(44% wrong), local-modulation hypotheses (53%), bass-is-root (17–23%)** — plus scale/collection priors, the
**global key-path transition costs** (modulation penalty), voice-leading, metric/cadential weight, the
declared-mode *hint* (the 1.0 tiebreaker already shipped). Soft scores rank only the hypotheses that survive
the hard constraints. **Weights are provisional `[empirical]`; Stage-5 fitting calibrates them** — and
calibration is load-bearing (a mis-scaled soft score can't override a hard fact, but it can mis-rank the
ambiguous residual).

## §5 — The SCOPED JOINT decision (the ~13.5% coupled core)

For positions where, after hard pruning, **both** chord and key remain ambiguous **and** are coupled (the
chord identity depends on the key and vice-versa), make one **joint** decision over the surviving (chord,
key) pairs, scored by the broad soft evidence + the global key path, **subject to** the hard constraints.
This is a *small, local* joint — not a global lattice — because the coupled core is sparse (~1-in-7) and
mostly short-span. Everywhere else the two-pass forward flow suffices (most positions are hard-pinned or
one-sidedly ambiguous, resolved by soft scores without a joint search).

## §6 — KEY-AXIS FIRST (the first build)

The first build is the **key decision**: hard-fifths-pinned where unambiguous; soft scores + the global
key-path resolving the relative-pair (key-only, 26.3%) and the modulation/key-coupled residual; the §5
scoped joint on the coupled core. This is where the measured gaps live (relative-pair floor, modulation),
and the chord axis is mostly hard-pinned (safe) so it can follow. The committed **cadence instrument** and
**modulation detector** feed in as **soft** evidence + the key-path transition model.

## §7 — The emission, and A-vs-B (decided: A, with a reserved B slot)

The soft scoring is **hand-built** for the bulk (confirmed sufficient — ~68% of chord-ambiguity soft-
resolvable, A confirmed). Provide a **clean emission interface** so a **learned** scorer can later plug into
the *same* constrained-joint machinery for the one measured feature-shaped slice — the pc-irreducible
symmetric **dim7/augmented floor (~111)**. **Do not build the learned model now**; reserve the seam.

## §8 — Measure-first staging (the discipline, non-negotiable)

Each step builds **diagnostically first** (produce the decision, measure vs DCML, production UNCHANGED →
byte-identical: BIR 57/23/57, snapshots 11/11), then **wire + re-gate** only on a clean measurement:
- **J-key-i (first):** the scoped-joint KEY decision, diagnostic. Binding metrics: the **de-masking
  `--partial-key-breakdown`** (modulation correctness, not gameable rn_agree), the relative-pair recovery,
  and — critically — that **no hard constraint is violated** and the soft producers stay soft.
- **J-key-ii:** wire the key decision into production; re-gate all three presets, DCML-adjudicate every
  moved case; un-adjudicated BIR=false increase = hard stop.
- **J-chord, J-function, J-gate-dissolution (§9):** later staged steps, each measure-first + ratified.

## §9 — The two deferred refactors fold in here

- **Gate-layer dissolution (deferred-refactor #2):** Gates A–L were local-pipeline compensation; the
  constrained-joint decision replaces them. They are retired **as the joint decision demonstrably reproduces
  or supersedes each gate's pinned fix** (the Stage-1 gate tests are the proof obligations) — not bulk-deleted.
- **File-split (deferred-refactor #1):** the constrained-joint inference is a **new, cleanly-layered module**;
  building it is the natural moment the layer seams become physical. `chordanalyzer.cpp` splits along them as
  the joint module subsumes the resolver/gate logic.
Both remain tracked in the handoff standing block until done.

## §10 — Safety + stop conditions (carried into J-key-i)
- A hard constraint pinning a WRONG answer (per DCML) — STOP, demote it to soft (the safety gate; §3 set
  already cleared, re-confirm on build).
- A soft producer being treated as hard (cadence/modulation/bass-is-root must stay soft) — STOP.
- The diagnostic step changing production output (it must be byte-identical) — STOP.
- A wiring step regressing the chord-axis gate un-adjudicated — hard stop.
- Building the full lattice (the measured core is ~13.5% → scoped only) or the learned model (reserved) —
  out of scope; STOP and surface.

## §11 — For user ratification
1. Approve the scoped two-pass-with-joint-core structure (§1–§5) and the validated hard/soft split (§3–§4).
2. Approve **key-axis-first** (§6) and the measure-first staging (§8: J-key-i diagnostic → J-key-ii wire).
3. Approve folding the two deferred refactors in (§9) — gate dissolution by proof-obligation, file-split as
   the module lands.
4. On ratification, Cowork writes the **J-key-i** instruction (build the scoped-joint key decision +
   measure diagnostically; production byte-identical; HELD).
