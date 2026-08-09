# DRAFT — the OI-179 ground-truth ceiling measurement: the design surface

> **STATUS: COWORK READING SURFACE — landed at the return STOP 2026-08-09. NOT ratified;
> a decision surface for the user's commissioning. NOT a build.** Sources read this session: `open_items/
> OI-179.md` in full (the census, the literature verdict, the BCMH zip inspection, the JEP:HPP
> reading, the 2026-08-04 note), principle #21's ★ clause (D-474), the D-475 establishment
> record. The row GATES (#19) and D-474 makes measuring it here the ONLY route — there is
> nothing to cite. It is phase 2's critical path: channel 5's residual decomposition and every
> "irreducible residual" verdict are bounded by it.
>
> This surface proposes; the user commissions. No corpus is promoted (research-tier-on-entry
> untouched); no measurement is built here.

## What exists, from the record

**In-repo, on-domain:** 87 of the 326 WiR-covered chorale stems carry a second analysis
(`analysis_BCMH.txt`) beside the primary; the BCMH originals are local
(`tools/BCMH_dataset/`: 100 homorhythmic reductions with `**harm` spines + unmodified
KernScores sources), so grading can run against BCMH's own spines, removing or cross-checking
the machine-translation noise the WiR copies carry. **BCMH's status (D-475):** independent in
origin, SINGLE reading, annotator count and validation UNDOCUMENTED — every in-repo and
published route exhausted; the one remaining route is contacting the PeARL laboratory, which
only the user can do. **Off-domain bounds (recorded with D-474):** rock/pop only; the one
invariant worth keeping is the axis ordering (root and key agreement ≫ full-label agreement);
the numbers themselves may not be used as a ceiling for this repertoire. **External,
uncomputed:** TAVERN released duplicate annotations (classical variations repertoire) and
published no number; Dilemmadata (2026) names 84 dual-annotated pieces and computes nothing —
both are computable BY US as additional legs, each with a declared domain caveat.

## The proposed design, in the record's own disciplines

**1. The unit is the robust unit.** The ceiling must bound the residual, so it is measured in
the SAME unit the residual is reported in: union-of-boundaries, duration-weighted,
segmentation-invariant; per axis (root / RN / key, key against both home and local per the
standing convention); coverage denominators published (the measurement conventions in gate
block (A) apply to this measurement like any other). A ceiling in any other unit would be
incommensurable with what it must bound.

**2. The primary leg: DCML/WiR versus BCMH on the 87-stem overlap.** What it measures, stated
honestly on the instrument: agreement between two independent annotation TRADITIONS (one
reading each), not within-lab multi-annotator agreement — declared exactly as D-475's status
requires. Still the first such figure the field has for this repertoire (the row's own words).

**3. The two pre-declared conventions the 2026-08-04 note demands.** (a) **Alignment:** BCMH
annotates a homorhythmic reduction; our grading is full-texture. The convention (grid mapping
of the reduction's harmonic rhythm onto the full-texture tick lattice, versus restriction to
spans where both slicings agree) is chosen at a DESK SIMULATION over 3–5 stems first (#17c),
with per-assumption predictions written before any corpus run (#17b), and the convention's own
sensitivity reported (both alignments computed on the desk-sim stems; if the verdict flips
between them, that is a NEAR-TIE reported with the sensitive convention named, per the desk-sim
rule). (b) **Translation noise:** graded against the local `**harm` spines primarily; the
translated WiR copies as cross-check; any spine-versus-translation disagreement quantified
separately so it cannot masquerade as annotator disagreement.

**4. Establishment of the comparison tool itself (#19/#16/#24).** Oracle cross-check on
hand-verified stems; seeded-disagreement recall (inject known label changes, measure
detection); reproduce-check; corpus-hash + tool-commit stamping; uncertainty by bootstrap over
pieces (#24) so the ceiling carries an interval, not a point.

**5. Optional legs, each its own establishment, each domain-caveated on its face:** TAVERN's
duplicates (within-corpus, true inter-annotator, off-repertoire); Dilemmadata's 84 dual
pieces (domain to be checked at the data). Neither substitutes for the primary leg; each
brackets it.

**6. What the measured ceiling then licenses:** #21 interpretation of every residual; channel
5's decomposition floor ("residual below measured annotator disagreement is not attributable
and must not be chased"); honest #17b targets for the eventual precision phase.

## The decisions this surface puts to the user (at the return STOP)

(1) Commission the measurement (it gates; nothing else can discharge #21). (2) The alignment
convention — after the desk simulation, not before (#17c produces the options with traced
cases). (3) Whether to contact PeARL for BCMH's annotator record — strengthens interpretation,
does not block the measurement (status is declared either way). (4) Whether the TAVERN /
Dilemmadata legs ride along. (5) Where it runs in phase 2's order — proposed: early, since
channel 5 and every residual claim wait on it.
