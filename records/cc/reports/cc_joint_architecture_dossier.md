# Constrained-Joint-Inference — architecture SIZING dossier

*CC, 2026-06-15. READ-ONLY measurement + characterization. No production code, no metric redefinition,
no commit. Sizes the constrained-joint-inference target (`docs/architecture_joint_inference.md` §9) before
any build. Base = HEAD `2245aedf82` (corrected GT parser committed at `a96f179f40`; `compare_rn.py` carries
the working-tree key-classification helpers used by the committed key-axis probes). Corpus =
`tools/corpus/default` (the user-run "Default" config; manifest 353/353) and `tools/corpus/baroque`,
decomposed over the **326 WiR-rntxt-covered Bach stems** (10,109 DCML-aligned regions; 11,255 total). DCML
roots are oracle-correct (committed `dcml_parser.py` `RomanNumeral` resolver). The cadence/modulation/
tonicization producers are the committed working-tree instruments (default-OFF → production output
byte-identical to HEAD; the design docs' standing invariant).*

**Evidence tags:** **[probe]** ran a script, read output · **[oracle]** music21 9.9.1 / DCML-WiR ground truth
· **[code]** read from source. Classifications marked **sampled** (read N cases) or **inferred** (deduced
from aggregate structure).

**Byte-identity attestation.** No production C++, no metric script, and **no corpus file** was modified.
The two new drivers (`tools/cc_joint_residual_probe.py`, `tools/cc_oracle_crosscheck.py`) are read-only:
they consume the **existing committed** `.ours.json` corpora (generated at HEAD with the diagnostic flags
default-OFF) and reuse `compare_analyses`/`compare_rn`/`dcml_parser` verbatim. The oracle cross-check calls
`batch_analyze --diagnose-measures` (a committed, default-OFF diagnostic whose output goes to stdout; the
production `writeJson` region path is untouched). The probe's `root_agree = 7744/10109 = 76.6%` and
`root_err = 2365` reproduce `cc_functional_residual_dossier.md` §0 **to the unit** — the instrument is the
same metric machinery. This dossier + the two probes are the only repo writes.

---

## §0 — Why this is a SIZING run, and the unit of measurement

The architecture (`architecture_joint_inference.md`) replaces the local feed-forward pipeline with **one
constrained joint decision**: **hard constraints** (raw facts + genuinely-unambiguous analyses) *prune* the
hypothesis space; **soft scores** (priors, weak cues, the global key path) *rank* the survivors. The whole
key-axis arc (4a–4d) is the standing evidence that a *local* mechanism structurally cannot do this. This run
**measures** the three numbers that right-size the replacement (§9 of the architecture doc): the **residual**
(pinned vs ambiguous), the **hard-constraint safety**, and the **soft-resolvable vs floor** split.

**The unit is the production region** (the analyzer's segmented sonority window), the same unit the gate and
the functional-residual dossier score. The decision object is **(vertical chord, key, function)**; the
measurements below keep those facets explicit, because — as §5 of the architecture warns and §3 here
confirms — **a sounding note is not automatically a chord tone**, so "hard" is true at the vertical/raw-fact
level and *false* at the functional level. Conflating them is the over-claim-in-reverse bug.

---

## §1 — Task 1: Hard/soft evidence characterization [code]

Every evidence source the system has or can cheaply derive, classified by whether it can act as a **hard
constraint** (decisive — disqualifies/pins) or only a **soft score** (ranks). The decisive test (§5 of the
architecture): does the source assert a **raw fact** or a **genuinely-unambiguous analysis**, or does it
assert a *reading* that a competent analyst could overturn?

| Evidence source | Kind | HARD or SOFT | Rationale (what it actually asserts) |
|---|---|---|---|
| **Sounding pitch-class set** | raw fact | **HARD (as a set)** | The pcs *do* sound — a fact. But "these pcs are the chord tones" is **not** hard (suspension/pedal/NHT). The hard pin is only the **complete-clear-chord** case (§2: pc-set = exactly one template). |
| **Bass pitch class** | raw fact | **HARD (as a pc)** | The lowest sounding pc is a fact → pins the *bass*. **"bass = root" is SOFT** (inversions, cadential 6-4; §3 measures the leak). |
| **Note duration / metric weight / onset** | raw fact | **HARD (as a value)**, soft as evidence | The values are facts; their *interpretation* (strong-beat ⇒ structural harmony) is a soft prior. |
| **Notated key signature (fifths)** | raw fact | **HARD for the collection, with caveats** | The fifths pin the diatonic *collection* — **except** Baroque partial/Dorian signatures (systematically mis-keyed, `project_key_detection_baroque_partial_signature`) and it pins **neither mode (relative-pair) nor local key**. |
| **Complete, clear, unique triad/7th on the sonority** | unambiguous analysis | **HARD (vertical sonority only)** | When the sounding pcs equal exactly one chord template, the **vertical sonority** is pinned (§2 PINNED, §3 safe). The **functional root/inversion** is NOT pinned by it. |
| **Vertical oracle candidates** (`oracle_top`) | producer | **SOFT (a scored ranking)** | A 75%-of-top **vertical-score** threshold, not a constraint; it *ranks* roots. Useful as the chord-hypothesis generator (§8 "seed of the joint lattice"), but it is soft by construction. |
| **Key-agnostic cadence anchor** (Stage 4c-i) | producer | **SOFT (measured)** | Correctly anchors only **55.7%** of the relative-pair floor; mis-anchors 44.3%, systematically to the relative major (§3). **Demote to soft** — a hard cadence pin would be wrong ~44% of the time. |
| **Local-modulation detector** (Stage 4d-i) | producer | **SOFT (measured)** | Non-home key commits at **47.0% precision / 33.4% recall** (§3). Cannot pin a local key. |
| **Tonicization labeler** (Stage 6-tonic-i) | producer | **SOFT (label)** | 6.4% genuine false-label rate but **409** tonicization-vs-modulation cases are a *convention* boundary (§4) — a soft/joint choice, not a fact. |
| **Global mode (major vs relative minor)** | analysis | **SOFT** | Structurally undetermined by the signature (the relative-pair floor) — the central lesson of 4b/4c. |
| **Local key (tonicization / modulation)** | analysis | **SOFT/joint** | DCML reads a local≠global key at **39.9%** of positions (§2); none is pinned by local raw facts. |
| **Repetition / voice-leading / phrase context** | analysis | **SOFT** | Contextual priors that rank; never decisive alone. |

**Task-1 verdict:** the genuinely-hard set is small and **raw-fact-shaped** — the sounding pc-set (as a
set), the bass pc, the metric values, the notated collection (caveated), and the *complete-clear-chord*
analysis. **Every producer that emits a *reading* (oracle, cadence, modulation, tonicization, mode, local
key, "bass-is-root") is SOFT**, and three of them (cadence, modulation, bass-is-root) are measured below to
**pin wrong** often enough that calling them hard would re-create the override bug. This is the architecture's
§2/§5 line, confirmed on the corpus rather than assumed.

---

## §2 — Task 2: the residual — pinned vs ambiguous (THE HEADLINE) [probe][oracle]

### §2.1 — Chord-axis hard-constraint pinning (raw pc-set, ALL 11,255 regions) [probe]

`cc_joint_residual_probe.py` classifies each region's **sounding pc-set** (a raw fact, read from
`pitchClassSet`) by how many chord templates it matches **exactly** (template vocabulary = `chordanalyzer.cpp`
`coreIntervals()` base qualities × 7th variants + the two 6th chords; symmetric sets flagged):

| class | meaning | Default | Baroque |
|---|---|---:|---:|
| **PINNED** | pc-set = **exactly one** clear triad/7th/6th — a genuinely-unambiguous vertical analysis | **7630 (67.8%)** | 7653 (67.9%) |
| NO_CLEAN | matches **no** single template (foreign/added/incomplete → NHT/suspension reading needed) | 2408 (21.4%) | 2394 (21.2%) |
| SHARETONE | matches **≥2 non-symmetric** templates (sus2≡sus4, C6≡Am7, m6≡ø7) | 974 (8.7%) | 977 (8.7%) |
| SYM_DIM7 | symmetric dim-7th {0,3,6,9} — **4 equal roots, root pc-undefined** | 102 (0.9%) | 102 (0.9%) |
| SYM_AUG | symmetric aug triad {0,4,8} — 3 equal roots | 9 (0.1%) | 9 (0.1%) |
| SPARSE | ≤2 distinct pcs (dyad/unison) — cannot determine a triad | 132 (1.2%) | 133 (1.2%) |
| | **chord-PINNED** | **67.8%** | **67.9%** |
| | **chord-AMBIGUOUS** (sum of the other five) | **32.2%** | 32.1% |

**The chord-axis pin is preset-ROBUST** (Default 67.8% ≡ Baroque 67.9%, every class within 0.2 pp) [probe] —
as it must be, because it is a property of the **notes + segmentation**, not the scorer. Note SYM_DIM7 is
only **0.9%** of *all* regions: the "~53% dim7" figure in CLAUDE.md is 53% of the **57-case BIR=false gate**
(the hardest residual), not of the corpus.

### §2.2 — Joint residual: chord × key 2×2 (the ambiguity-type breakdown) [probe][oracle]

Cross-tab each DCML-aligned region (10,109) by **chord-pinned?** and **DCML local modulation?** (local key ≠
global key — the oracle measure of inherent key ambiguity at the position):

| | key-STABLE (local==global) | key-MODULATION (local≠global) | row |
|---|---:|---:|---:|
| **chord-PINNED** | **4147 — 41.0% — FULLY PINNED** | **2654 — 26.3% — key-only ambiguous** | 6801 (67.3%) |
| **chord-AMBIGUOUS** | **1939 — 19.2% — chord-only ambiguous** | **1369 — 13.5% — jointly-coupled** | 3308 (32.7%) |
| col | 6086 (60.2%) | 4023 (39.8%) | 10109 |

*(The key-modulation column = 4023 = **39.8%** independently matches the modulation detector's DCML
prevalence 4036/10109 = **39.9%** [probe] — the two probes agree to 0.1 pp.)*

**The headline residual.** Hard constraints over raw facts **fully pin ~41% of positions** (chord clear AND
key stable). The **~59% ambiguous residual** — the true scope of the joint problem — splits:

- **chord-only ambiguous: 19.2%** — the notes admit >1 chord, but the key is stable.
- **key-only ambiguous: 26.3%** — the chord is clear, but a local-key/function decision is open. *(This is the
  largest single ambiguity, and it is dominated by the S1 tonicization slice — see §4: mostly soft-resolvable
  label, not deep ambiguity.)*
- **jointly-coupled: 13.5%** — both axes open at once (the slice where the joint *structure* genuinely pays:
  the chord reading and the key co-determine — symmetric-dim7-in-context, viio↔V7 share-tone, cad64).

*Granularity note:* the key axis here is **local** modulation (the per-position fact). The **global-mode
relative-pair** is a separate *piece-level* overlay — small at the shipping (mode-present) config (**193/10109
= 1.9%** S2, `cc_floor_classify`), large only mode-absent (1452) — so the "FULLY PINNED 41%" is "chord-clear +
locally-stable"; ~1.9% of those pieces additionally carry an unresolved global-mode call. The relative-pair is
sized as a soft-resolvable slice in §4.2, not folded into the 2×2.

### §2.3 — Oracle cross-check of the chord-axis pin [oracle][probe]

`cc_oracle_crosscheck.py` runs the committed **vertical oracle** (`--diagnose-measures`, downbeat region per
measure) over the WiR stems and counts **distinct roots in `oracle_top`** (the system's own vertical
near-tie set). Validation: structural-PINNED ⟺ oracle sees a single root.

Over **326 WiR stems / 4688 diagnosed downbeat regions** [oracle][probe], the structural class and the
committed oracle's distinct-root count agree on which positions are vertically ambiguous:

| structural class | n | oracle sees **1 root** | oracle sees **≥2 roots** |
|---|---:|---:|---:|
| **PINNED** | 3066 | **2427 (79.2%)** | 639 (20.8%) |
| NO_CLEAN | 1126 | 318 (28.2%) | **808 (71.8%)** |
| SHARETONE | 463 | 147 (31.7%) | **316 (68.3%)** |
| SYM_DIM7 | 29 | 3 (10.3%) | **26 (89.7%)** |
| SYM_AUG | 4 | 3 | 1 |
| **overall** | 4688 | 2898 (**61.8%**) | 1790 (38.2%) |

structural-PINNED overall = **65.4%** on this downbeat sample. **The predicate and the producer concur**:
where the pc-set is one clear chord, the oracle returns a single root **79%** of the time; where it is
NO_CLEAN/SHARETONE/SYM, the oracle returns **multiple** roots **68–90%** of the time. The oracle is slightly
*more* permissive (61.8% single-root < 65.4% structural-PINNED), because its **soft 75%-of-top-vertical-score
threshold** admits near-ties even on clean chords — i.e. the oracle is a soft ranker, not a hard pin, exactly
as §1 classifies it. (Sample caveat: `--diagnose-measures` emits one region/measure; downbeats run slightly
*less* pinned than the all-region 67.8%.)

The structural predicate (strict pc-set uniqueness: 65.4% pinned on the downbeat sample, 67.8% all-region)
and the soft oracle (75%-threshold single-root: 61.8% on the same sample) **bracket** the chord-pin rate
within ~4 pp; the gap is exactly the oracle's soft threshold admitting vertical near-ties even for clean
chords. Both land in the **62–68% chord-pinned** band — the chord-axis residual is robust to how "hard" the
line is drawn.

### §2.4 — What the residual decides (full-joint vs scoped-joint vs two-pass)

A **41%-pinned / 59%-ambiguous** residual, with the ambiguity concentrated on the **key axis (39.8%, mostly
soft-resolvable)** and a **13.5% jointly-coupled core**, is **not** a "every position is wide open" surface
that would demand a full joint decode of the whole piece. The chord is hard-pinned for 2/3 of positions; the
genuinely-coupled slice where chord and key must be solved *together* is **~1 in 7 positions**. This sizes a
**scoped joint** decision (hard constraints prune to the 59%; the joint/soft reasoning runs on the survivors,
with the key path as the dominant soft axis) rather than a full unconstrained lattice — exactly the
"efficient + scoped" claim of architecture §3, now with a number on it.

---

## §3 — Task 3: hard-constraint safety / calibration (the precondition) [oracle]

For positions a candidate hard constraint PINS, how often is the pinned answer **wrong** per DCML? A
constraint that pins wrong must be **demoted to soft**.

### §3.1 — The pc-set "complete-clear-chord" pin: VERTICALLY safe, FUNCTIONALLY not

Our **production root** vs DCML root, per structural class (10,109 aligned) [probe][oracle]:

| class | aligned | root-agree | agree % |
|---|---:|---:|---:|
| **PINNED** | 6801 | 5495 | **80.8%** |
| NO_CLEAN | 2215 | 1533 | 69.2% |
| SHARETONE | 879 | 593 | 67.5% |
| SYM_DIM7 | 94 | 31 | **33.0%** |
| SYM_AUG | 9 | 5 | 55.6% |
| SPARSE | 111 | 87 | 78.4% |
| **ALL** | 10109 | 7744 | **76.6%** |

A naive read says "PINNED disagrees with DCML 19.2% of the time — unsafe!" **That read is wrong**, and the
decomposition shows why. Splitting every disagreement by **is DCML's root even present in our sounding
pc-set?** [probe]:

| | PINNED disagreements (1306) |
|---|---:|
| **DCML root ABSENT from our pc-set** (segmentation/alignment/foreign) | **996 (76.3%)** |
| DCML root PRESENT (functional re-rooting of a *sounding* tone — cad64, inversion, added-6th) | 310 (23.7%) |

So **of the 19.2% PINNED "errors," ~0% are vertical-chord errors.** In 76% the disagreement is that **DCML's
root is not even in the notes our segment captured** — a **segmentation/alignment** difference (the §6
"alignment noise" the functional dossier flagged), not a wrong chord. The other 24% are **functional
re-rootings of a tone that IS sounding** (the cadential-6-4 reads the {D,G,B} triad as V-of-C; an added-6th
reads C6 as Am7). In **both** cases the *vertical sonority* the constraint pinned is **correct** — the notes
do form that chord. **The complete-clear-chord pin is SAFE as a constraint on the vertical sonority.**

### §3.2 — Where "hard" would be UNSAFE (the constraints to keep soft)

| candidate hard constraint | measured wrong-pin rate | verdict |
|---|---|---|
| pc-set = one clear chord → pin the **vertical sonority** | ~0% vertical error (§3.1) | **HARD — safe** |
| pc-set = one clear chord → pin the **functional root** | 19.2% disagree, but ~100% of it is segmentation (76.3%) + functional re-rooting (23.7%); ~0% vertical error | **SOFT** — the functional root is not a raw fact |
| **"bass = root"** → pin root-position | PINNED bass-is-root still 17.4% disagree (3853/4666) vs bass≠root 23.1% (1642/2135) | **SOFT** — inversions/cad64 re-root |
| **cadence anchor** → pin global tonic+mode | **44.3% wrong** on the relative-pair floor (643/1452); systematic relative-major capture | **SOFT — demote** |
| **modulation detector** → pin local key | **53% wrong** when committing a non-home key (47.0% precision) | **SOFT — demote** |
| notated signature → pin global **mode** | the relative-pair floor (193 mode-present S2) is mode-undetermined | **SOFT** for mode (HARD only for the collection) |

**Task-3 verdict — the calibration precondition is satisfiable, and it lands exactly on the §5 line.** The
**only** safe hard constraints are the **raw facts** (sounding pc-set, bass pc, metric values, notated
collection) and the **complete-clear-chord pin restricted to the vertical sonority**. Every *reading*-shaped
candidate (functional root, bass-is-root, cadence, modulation, mode, local key) pins wrong often enough to
**require soft treatment** — and three of them are measured to fail at 17–53%. No safe hard constraint
mis-claims certainty; the unsafe ones are identified and demoted. This is the **green light** on the
architecture's safety precondition: the −7-wall-in-reverse failure is **avoidable**, because the facts that
are hard really are decisive (~0% vertical error) and the facts that aren't are measurably caught.

---

## §4 — Task 4: soft-resolvable vs irreducible floor [probe][oracle]

Of the ~59% ambiguous residual, how much would soft/global evidence plausibly resolve (where the joint
*structure* pays), vs how much is the §6 ceiling (where even analysts pick by convention — where a richer/
learned **emission** is the only lever, and even that has a ceiling)?

### §4.1 — Chord-axis ambiguity: ~68% is ALREADY soft-resolved [probe]

The production scorer **already applies soft progression context**, so its root-agreement on the
chord-ambiguous classes is a *realized* lower bound on soft-resolvability. Aggregating the chord-ambiguous
classes (§3.1): **2249 / 3308 = 68.0%** already get the correct root from soft context. By class: SPARSE 78%,
NO_CLEAN 69%, SHARETONE 68%, SYM_AUG 56%, **SYM_DIM7 33%**. So:

- **Soft-resolvable (chord axis): ≈ 68%** of chord-ambiguity, realized today; the residual 32% is the
  not-yet-fitted + floor.
- **Feature-shaped floor (where a richer EMISSION would pay): the symmetric sets** — SYM_DIM7 at 33% is
  **pc-irreducible by construction** (4 equal roots), resolvable only by **spelling / voice-leading**
  features the current emission lacks. This is the cleanest "B could help" slice (architecture §7) — small
  (~111 regions) but genuinely emission-shaped, not structure-shaped.

### §4.2 — Key-axis ambiguity: mostly soft-resolvable label, with a convention floor [probe][oracle]

The 39.8% key-modulation residual is **not** deep ambiguity — it is dominated by the **S1 tonicization
slice** (`cc_functional_residual_dossier` §0.5: **1885** regions where our **root AND global key are already
correct** and only the local-key *label* differs — a pure-add label, the largest single soft-resolvable mass).
The remaining key resolvability, measured on the committed producers:

- **Relative-pair (global mode):** the declared-mode crutch already resolves the bulk (mode-present Default
  relative-pair S2 = **193**; mode-absent floor = **1452**) [probe]. The cadence anchor resolves **55.7%**
  (809/1452) of the mode-absent floor [probe] — a soft signal, not a pin. **Soft-resolvable.**
- **Local key (tonicization vs modulation):** the labeler's **409** "target == DCML local tonic" cases are
  the **tonicization-vs-modulation convention boundary** [probe] — a *defensible-either-way* label choice =
  **floor**.
- **Notated-key vs analyst-key convention:** **≈127** relative-pair cases where the resolver faithfully
  follows the notated key and the analyst chose its relative (`cc_key_emission_headroom_dossier`) — **floor**
  (arguably correct behavior penalized by the metric).

### §4.3 — The functional residual, already decomposed (corroborating Task 4) [probe][oracle]

`cc_functional_residual_dossier.md` (corrected parser) decomposed the 2153-region "neither-vertical-analyzer-
reaches-DCML" residual and found, on Bach: **rule-reachable (B1) ≈ 26–55%**, **ambiguity/convention/noise
(B3, = floor) ≈ 41–74%**, **needs-a-learned-model (B2) ≈ 0** (0/44 sampled; corpus upper bound ~7%). music21's
*vertical* RN analyzer fails the same functional roots (0/4) → it is a functional-**layer** problem (soft/
joint), not a vertical-scorer ceiling. This is the same split this dossier reaches from the chord/key side:
the residual is **soft-resolvable + convention-floor, with an empty "only-a-learned-model-gets-this" bucket.**

### §4.4 — The split, assembled

| residual slice | size (Default, region-scale) | disposition |
|---|---:|---|
| **Soft-resolvable** — joint structure / key path / functional layer resolves | dominant | **where the joint STRUCTURE pays** |
| · S1 tonicization label (root+global already correct) | 1885 | pure-add label (KeyArea + labeler) |
| · chord-ambiguity already soft-resolved | ~2249 of 3308 | realized today |
| · relative-pair via cadence/key-path | ~56% of the mode floor | soft signal |
| · rule-reachable functional (B1) | ≈ 550–1180 | hand-built layer |
| **Feature-shaped floor** — richer EMISSION (B) could pay, structure cannot | small | **where a learned EMISSION pays** |
| · symmetric dim7/aug (spelling/voice-leading) | ~111 | pc-irreducible; B-shaped |
| **Irreducible floor (§6)** — defensible-either-way; ceiling for everyone incl. B | sizeable | **where NOTHING pays** |
| · tonicization↔modulation convention | ~409 | label convention |
| · notated-key vs analyst-key convention | ~127 | metric-penalized correct behavior |
| · functional ambiguity/convention/alignment-noise (B3) | ≈ 970–1600 | inflated by alignment noise (shrinkable) |

---

## §5 — Recommendation, on the numbers

**The constrained-joint shape is CONFIRMED sound, and the numbers size a SCOPED joint / two-pass, not a full
unconstrained decode.**

1. **The residual is moderate and concentrated, not total.** Hard constraints fully pin **~41%** of positions;
   the chord is hard-pinned for **~68%**. The genuinely-coupled core (chord *and* key open together) is
   **13.5%** — ~1 in 7 positions. **⇒ A scoped-joint / two-pass** (hard constraints prune; the joint/soft
   decision runs on the ~59% survivors, dominated by the key axis) is right-sized. A full
   every-position-open lattice is **not** warranted by the residual. *(architecture §2.4)*

2. **The safety precondition is met.** The hard constraints that are safe (raw facts + complete-clear-chord on
   the **vertical sonority**) have **~0% vertical error**; the dangerous over-claims (functional root,
   bass-is-root, cadence, modulation, mode, local key) are **identified and measured to fail at 17–53%**, so
   they are correctly **soft**. The −7-wall-in-reverse failure is structurally avoidable. **No safe constraint
   mis-claims certainty.** *(the load-bearing §5 skill is realizable hand-built)*

3. **Constraints to DEMOTE (explicit):** the **cadence anchor** (44% wrong on the floor) and the
   **modulation detector** (53% wrong on non-home commits) must enter the joint decision as **soft scores**,
   never as pins — exactly as their own Stage-4c/4d designs already stage them (anchor at section scope,
   measured-not-wired). **"bass-is-root"** must likewise stay soft. This dossier supplies the numbers those
   designs deferred.

4. **A confirms; B is not triggered by the structure — only a small feature-shaped slice.** Soft/joint
   evidence already resolves ~68% of chord-ambiguity and the entire S1 label mass is pure-add; the
   needs-a-learned-model bucket is **empty** on the structure side (§4.3, corroborating the ratified OQ-1=A).
   **Where B would pay is the EMISSION on the feature-shaped floor** — chiefly **symmetric-dim7 spelling/
   voice-leading (~111)** — decoded by the *same* constrained-joint machinery (architecture §7). That is a
   later, optional emission upgrade, not a reason to delay the hand-built joint structure.

**Net:** build the **scoped constrained-joint decision** with hand-built soft emission; lead with the **key
axis** (the largest ambiguity, 39.8%, mostly soft-resolvable and KeyArea-gated — reinforcing the ratified
Stage-4-first order); keep cadence/modulation/bass-is-root **soft**; reserve a learned emission for the
small, measured, feature-shaped dim7/voice-leading floor if and when it becomes the binding ceiling.

---

## §6 — Where a learned emission would and would not help (honest read)

- **Would help (small, real):** the **symmetric-dim7/aug** floor (33% root-agree, pc-irreducible) is exactly
  a *spelling/voice-leading feature* gap — a learned emission with enharmonic/voice-leading features could
  lift it where no amount of *structure* can (4 equal roots admit no vertical pin). ~111 regions. Also the
  hardest **B3** label-disambiguation tail on chromatic non-Bach repertoire (unmeasured here — §7).
- **Would NOT help:** the **41% already pinned** (nothing to beat); the **S1 label mass** (already root+key
  correct — a labeler, not a model); the **convention floor** (tonicization↔modulation, notated-vs-analyst —
  a *ceiling for B too*, by definition); and the **segmentation/alignment** share of the residual (a
  re-segmentation/joint-window problem, not an emission problem — and a lenient-alignment audit would *shrink*
  it, strengthening A).

The architecture's §7 claim — "A-vs-B lives in the emission; the structure is agnostic and accommodates
both" — is the right frame: the **structure** is justified by the 59% residual independent of A/B; the **only**
emission slice where B beats a hand-built feature is the small pc-irreducible floor.

---

## §7 — Unknowns / what is NOT measured (do not over-generalize)

1. **Bach WiR-rntxt only.** All numbers are the `tools/corpus/default` / `baroque` Bach gate corpus. The
   non-Bach TSV corpora (corelli/mozart/chopin/beethoven) are **unmeasured** here — and per the back-half
   design, B's advantage concentrates on that harder, chromatic repertoire. The 41%-pinned / 13.5%-joint
   figures are **Bach**; chromatic repertoire will pin less and couple more (state, do not extrapolate).
2. **Segmentation is the production segmentation.** "Chord-pinned" and the DCML-root-absent (76% of PINNED
   disagreement) both depend on the segment boundaries `batch_analyze` chose. A joint decision that also
   decides segmentation would move this line; the residual is sized **at the current segmentation**, which is
   the honest baseline but not segmentation-invariant. The DROOT_ABSENT/alignment share inflates the apparent
   floor (functional dossier §5.2) — a lenient-alignment audit (unbuilt) would shrink it.
3. **Oracle cross-check is downbeat-region only** (`--diagnose-measures` emits one region/measure,
   region-in-isolation). It validates the chord-axis pin on a representative sample, not every region; the
   structural probe (full-coverage) is the primary, the oracle the cross-check.
4. **"key-MODULATION" = DCML local≠global** is the *inherent* key-ambiguity proxy, not a measure of whether
   *we* resolve it; §4 sizes resolvability separately (S1 = already-correct, cadence = 56%).
5. **The §4 soft-resolvable vs floor magnitudes** rest on the functional dossier's sampled B1/B3 line (MED
   confidence) and the producers' realized rates (HIGH). The B2≈0 / "no learned-model-only bucket on the
   structure side" conclusion is the robust part; the B1↔B3 magnitude is the soft part — both route away from
   a structural need for B.

---

*Drivers (read-only): `tools/cc_joint_residual_probe.py` (chord-axis structural pin + DCML safety + joint
2×2; reuses `compare_analyses`/`compare_rn`/`dcml_parser`), `tools/cc_oracle_crosscheck.py` (committed
vertical-oracle cross-check via `batch_analyze --diagnose-measures`). Existing committed probes re-run for
the key axis: `cc_floor_classify.py`, `cc_cadence_anchor_measure.py`, `cc_stage4d_i_modulation_measure.py`,
`cc_tonicization_measure.py`. Corpora: `tools/corpus/{default,baroque}` + `default_4ci_abs`/`default_4ci`/
`default_mod`/`default_6tonic` (committed, HEAD-generated, default-OFF flags). No production/metric/corpus
file modified. This dossier + the two new probes are the only repo writes.*
