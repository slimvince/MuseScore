# EXTRACT — Hentschel, Moss, McLeod, Neuwirth & Rohrmeier 2021, "Towards a Unified Model of Chords in Western Harmony" (MEC 2021) — population row 3, CENTRAL, first pass

> **Establishment bound:** read 2026-08-30 via two prompted extraction calls over the full text
> at the author's open copy (method and limits in the fetched content record). CENTRAL: second
> independent pass owed.

## Claims, labeled

- **[FACT — §model]** The model keeps generic, spelled and enharmonic pitch classes as DISTINCT
  TYPES with one-directional conversion (spelled → enharmonic/generic, never back), and treats
  octave and enharmonic equivalence as explicit flags — never destructive normalization.
- **[FACT — §model]** Mode is a first-class interval collection (named diatonic modes AND
  arbitrary interval sets), and a key is tonic + mode + an optional hierarchy type
  (global/local/secondary).
- **[FACT — §model]** A chord is a graph over explicit properties; theories that specify less are
  still representable, with missing properties induced only where derivable.
- **[FACT — §model]** Suspensions are representable as per-note functions naming what is
  suspended; non-chord tones are ignorable per annotation standard.
- **[FACT — §scope]** This paper does NOT discuss the cadential six-four as a standards
  flashpoint — the DP-N flashpoint evidence lives elsewhere (the meta-corpus paper).
- **[THEORY]** The representational distinctions themselves (spelled vs enharmonic pitch,
  scale degree vs interval) are standard music theory formalized, not new claims.
- **[CONJECTURE — §future]** That the model can serve as a generalized interchange standard —
  offered as "a first step," unmeasured.

## Coupling facts (mandatory)

- **Assumes upstream:** nothing computational — it is a REPRESENTATION, not an algorithm; it
  assumes only that "chord" as a pitch collection is meaningful in the style.
- **Hands downstream:** a typed representation whose queries (graph patterns) can express
  musicological questions; conversion/induction operations between levels.
- **Stated scope:** Western harmony broadly (classical, jazz, rock, pop annotation standards);
  explicitly not exhaustive.

## Measured results

None — no experiments; a representation paper.

## Bearing on the framework (first pass)

- **DP-L / §7 data design:** direct support for the disposition surface's reading — a candidate
  reference for the data design at the detail phase: distinct spelled/enharmonic types with
  non-destructive equivalence flags is exactly the shape of this project's C-5-congruent
  publication rules, and the first-class mode collection bears on the mode-vocabulary question
  (routed to L2 detail).
- **DP-N:** nothing here decides the cadential six-four; the point stays open.
- No falsifier candidate against any chosen point.

## Verification targets touched

- None of V1–V13 originates here.
