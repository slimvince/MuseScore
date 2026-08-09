# DRAFT — channel 3, the invariance and metamorphic probes: specification skeletons

> **COWORK READING SURFACE — landed at the return STOP 2026-08-09; NOT ratified.** Phase-2 preparation: one specification skeleton per
> theory-derived relation the ratified §4 channel names, so that when phase 2 opens each probe
> needs only its predictions filled and a dispatch slot. Pattern source: the OI-243/244
> transposition probe and its 2026-08-03 repository-side re-run — the one member of this
> family already built, established, and re-run clean; its apparatus
> (`tools/joint_estimator/transposition_probe_2026_08_02/` + `_rerun_2026_08_03/`) is the
> establishment template every probe below copies. Explorational scope: surprises are the
> intended product (#5), each rowed; predictions written before measuring (#17b); read-only
> throughout; every probe stamps corpus-hash + tool-commit (#16) and publishes per-condition
> equivalence on the robust unit so results are commensurable with the baselines.

## Probe 3a — transposition (DONE in substance; residue only)

Already run and ESTABLISHED (OI-243/244): 66.26 % segment equivalence, mechanism located
(spelling-factor canonical anchoring; absolute-pc tie-break). Phase-2 residue: (i) promote the
apparatus into a permanent cheap regression check per the channel's own each-HOLD-becomes-a-
guard rule — blocked until the family design fixes the representation (a guard that always
fails guards nothing; it lands WITH the fix); (ii) the named-but-unrun follow-up from OI-227:
whether the full 24-key set (prune off) recovers fitBlocked events — one flag, one run,
predictions first.

## Probe 3b — octave doubling (PARTIALLY DONE via OI-277; the residue is the check)

OI-277 measured it: 13.2 % of segments move under one upper-voice octave doubling. The
mechanism is diagnosed (per-note-record summation — trained semantics, a model property). What
phase 2 still owes: nothing exploratory — the finding is made; the probe spec here is only the
REGRESSION form for after the family design decides the counting semantics. Prediction
template: under pc-level or voice-deduplicated emission, doubling equivalence should be exact
(100 %) minus a named bass-register exception (a doubling BELOW the bass changes the sounding
bass and MAY legitimately change readings — the spec must carve that case out explicitly
before it is a guard).

## Probe 3c — uniform time-stretching (NOT RUN; full skeleton)

**Relation (#1-derived):** multiplying every duration and onset by k (e.g. 2) shifts tick
positions proportionally and changes NO reading: same slices at scaled boundaries, same keys,
same chords, same segment structure. **Where it could fail, known in advance (the prediction's
attention list, not a design):** any absolute-tick constant in the pipeline (window sizes,
lookaheads, duration-weighted priors fitted at chorale tick scales — the metric-position
covariates in the emission read beat positions, which SHOULD be scale-free if derived from
time signature + measure position, and the probe tests exactly that). **Apparatus:** MusicXML
transform (divisions or note-type doubling — both variants, since they exercise different
import paths); the OI-243 comparison harness reused (per-condition equivalence on the robust
unit, violations classified by moving factor). **Conditions:** k = 2 and k = ½ minimum.
**Establishment:** the identity condition (k = 1 round-trip through the transform) must be
bit-exact before any measured condition is read — the OI-243 pattern.

## Probe 3d — part order (NOT RUN; full skeleton)

**Relation:** renumbering staves/parts without changing content changes nothing. **Attention
list:** any iteration-order dependence (map traversal, tie-breaks on staff index), the bass
determination (must be by sounding pitch, not by staff number — if a tie-break anywhere reads
staff order, this probe finds it), the adapter's event assembly. **Apparatus:** part-order
permutation of the MusicXML (2–3 permutations per piece incl. full reversal); same harness.
**Prediction:** bit-exact equivalence — this is the strictest relation in the set; ANY
movement is a finding (there is no defensible-variation class for staff numbering).

## Probe 3e — the no-information-loss check (#12 as a mechanical property; NOT RUN)

**Relation:** on every published surface, wherever a winner is committed the carried
alternatives are present (winner AND carry, #15's full output surface). **Form:** not a
transform probe — a mechanical predicate over the record's published surfaces (the two full
candidate lists with no truncation, D-006; the exclusion-tail carry rules). **Runs as:** a
walk over batch outputs asserting the predicate per segment; failures classified by surface.
**Establishment:** seed one deliberate truncation in a scratch copy and confirm detection.

## Probe 3f — enharmonic respelling (the OI-243 sibling worth naming now)

Uniform respelling at the SAME pitch (e.g. all F♯→G♭ spellings in the source) is a weaker
transform than transposition and isolates the spelling factor alone (the lattice, keys and pcs
all unchanged). OI-243's separation already classifies the tritone case as genuinely
ambiguous; this probe would give the spelling factor its own equivalence figure independent of
the transposition machinery. LOW priority (the mechanism is already located); listed so the
enumeration is complete rather than sampled.

## Ordering within channel 3 (proposal for the phase-2 surface)

3d (strictest, cheapest, bit-exact expectation) → 3c (two conditions, new transform) → 3e (the
predicate walk) → 3a-residue and 3f (ride the family design) → 3b (post-design regression
form). Each HOLD becomes a permanent guard; each violation is a row; nothing is fixed inside
the probe (read-only, the freeze and D-231 untouched).
