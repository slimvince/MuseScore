# The joint estimator's factorization — structure-design specification (★ USER-RATIFIED 2026-07-19)

**Ratified by the user 2026-07-19** — the variable structure (§1), the score form (§2), the factor
roster (§3), the premise ledger P1–P8 (§4), the decode plan (§5), and the desk-simulation forms and
case list (§6) are the governing structure. Values remain unfit. **The §6 desk simulation has RUN and
its findings are user-ratified (2026-07-19, same day — `cowork_factorization_desk_simulation.md`):**
nine of ten traces pass as specified; the amendments it produced (the §2 factor-granularity rule and
the §3.10 initial-state-only prior) are incorporated below with dated marks. The funnel's next stage
is the pre-fit gates (OI-176/OI-177/OI-178/OI-180).

**Author:** Cowork, 2026-07-19, at the user's direction. **Standing:** the structure-design step of
`cowork_joint_estimator_architecture.md` §4 (step 2), building on the five ratified §5a decisions and
the derived forms in `cowork_term_theory_grounding.md`. **This is a specification, not a build** — the
estimator funnel stays shut. Every load-bearing conditional-independence claim is an explicit premise
(P1–P8 below), labeled THEORY or ASSUMPTION per #17a, with its false-negative path named per #17e.
**Ratifying this document ratifies the structure and the premise ledger; all VALUES remain unfit** and
enter only through the ratified fitting protocol (§5a) under the OI-176/OI-177 gates.

---

## 1. The random variables

A piece is a sequence of **events** — the minimal segments between consecutive note onsets/offsets
(the Pardo & Birmingham partition, already the analyzer's slice unit). The estimator chooses, jointly:

- **The segmentation** `S`: a partition of the event sequence into contiguous **harmonic segments**
  (semi-Markov: segment boundaries are decided, not given).
- **Per segment j, the state** `h_j = (k_j, c_j)`:
  - `k_j = (tonic, mode)` — tonic one of the twelve pitch classes; mode ∈ {major, minor} (ratified);
  - `c_j = (degree class, quality, inversion)` — the Roman numeral (ratified): diatonic degrees,
    applied-degree classes (the secondary dominant and applied leading-tone chord per target), and the
    standard chromatic classes (Neapolitan sixth, augmented-sixth chords). **The degree vocabulary is
    derived from the ground truth, not invented:** the set of degree classes observed in the corpus
    annotations, with a count threshold and one pooled rare-class — the threshold set at fit time under
    the capacity budget (OI-177), the pooling declared, nothing hand-picked.

A **key change is permitted only at a segment boundary** (a change of key without a change of harmony
is not expressible in this label space — definitional, not an assumption). The **chord symbol** (root
pitch class, quality, bass) is the derived published fact: root = tonic + the degree's interval.

## 2. The joint score

Per the ratified staged fitting, the model is log-linear over frozen generative tables: the score of a
candidate `(S, h)` given the notes is the sum over segments of weighted factor terms,

```
Score(S, h) =  w_prior · log P_prior(k_1 | signature, declared mode)            [once, at the start]
            + Σ_j  w_emit  · log P_emit(tones in segment j | k_j, c_j)          [pitch emission]
            + Σ_j  w_spell · log P_spell(spelled tones in j | k_j)              [spelling emission]
            + Σ_j  w_bass  · log P_bass(bass degree of j | c_j)                 [bass/inversion]
            + Σ_j  w_chord · log P_chord(c_j | c_{j-1}, mode_j)   [same-key chord transition]
            + Σ_j  w_key   · log P_key(k_j | k_{j-1})             [key transition; = 1-cell if no change]
            + Σ_j  w_entry · log P_entry(c_j | key change)        [entry chord at a key change]
            + Σ_j  w_bound · log P_bound(boundary at j | beat strength, fermata)  [segmentation]
            + Σ_j  w_cad   · (cadence evidence features at j → k_j)             [cadence factor]
```

with the identity-weight setting (all `w = 1`) being exactly the generative product — the mandatory
ablation baseline (ratified). The weight vector is small (one weight per factor, roughly ten), fit by
convex conditional likelihood under the held-out gate.

**Factor granularity (amendment, user-ratified 2026-07-19 at the desk simulation —
`cowork_factorization_desk_simulation.md` §4.1, the `bwv10.7@36000` length-bias finding):** the
per-segment sums above are evaluated at these granularities — the pitch and spelling emissions **per
tone**; the BASS factor **per event** (each event's sounding bass against the segment's chord — Ni's
published per-frame form); the missing-template-tone penalty inside `P_emit` **normalized per event of
segment length** (a segment missing a template tone pays in proportion to how long it fails to sound
it); the chord-transition, key-transition, entry, and boundary factors **per boundary/event** (as
written). Without this rule, per-segment factor instances give longer segments an evidence-free
discount (the semi-Markov length bias) that the desk simulation measured deciding merge-vs-split
against ground truth by ~6.6 nats on the named case.

## 3. The factors — form, table, provenance (values all unfit)

1. **Pitch emission** `P_emit(tone | k, c; covariates)` — each tone classified into categories:
   chord member (root / third / fifth / seventh-or-tension per the degree class's template),
   within-collection non-chord tone, outside-collection tone; emission probability conditioned on the
   category AND the chord-independent covariates ratified in §5a: metric weakness, stepwise approach,
   stepwise departure, chromatic-neighbor motion, tied-over preparation. Table: category × covariate
   cells, pooled where counts are thin (pooling declared at fit). Provenance: Raphael-Stoddard category
   structure + Masada-Bunescu figuration covariates; the minor-mode variable sixth and seventh degrees
   are emission variants (ratified). Fit: counts from ground-truth-labeled segments; the BCMH
   reduction alignment (87 stems) is the independent fitting/validation resource for the ornament cells.
2. **Spelling emission** `P_spell(spelled degree | k)` — the tonal-pitch-class term: the spelled note's
   scale-degree relation to the key, with the leading-tone/subtonic contrast in minor as the sharpest
   cell (Temperley's tonal-pitch-class profile form; his measured +3.6 points on key is the basis).
   Also carries the collection question through the signature mask (the OI-168 form) — no tonic in the
   membership test.
3. **Bass/inversion** `P_bass(bass chord-factor | c)` — categorical: which chord factor (root, third,
   fifth, seventh) sounds in the bass, given the degree class and inversion; the figured-bass tradition
   is the theory, Ni's bass-given-chord chain the published probabilistic analogue. **Evaluated per
   event within the segment (the 2026-07-19 granularity amendment, §2).** Bass-motion
   continuity across segments is NOT in the first structure (recorded as a possible later factor with
   its own ledger entry).
4. **Same-key chord transition** `P_chord(c_j | c_{j-1}, mode)` — the asymmetric first-order degree
   table, transposition-tied across keys, **fit separately for major and minor** (Raphael & Stoddard
   assumed mode-independence and doubted it themselves; the corpus statistics — the strong affinity of
   minor to its relative major, the mediant's prominence in minor — say fit per mode; the tying still
   pools all twelve keys per mode). Provenance: Ni's key-conditioned transition; Rohrmeier & Cross's
   measured asymmetries. First-order is a declared ASSUMPTION (P2); the harmonic-syntax grammar is the
   recorded future form upgrade for this one factor.
5. **Key transition** `P_key(k_j | k_{j-1})` — transposition-invariant small table over (circle-of-
   fifths distance between tonics, mode pair), with the relative and parallel relations as their own
   cells (the Noland/Rocher family; asymmetries permitted — the table is fit, not a symmetric curve).
   Staying in the key is the overwhelmingly probable cell; the fitted stay/change balance is the
   modulation rate.
6. **Entry chord at a key change** `P_entry(c | key change)` — the distribution of the first degree in
   a new key, fit from the ground truth's modulation points (replacing Raphael & Stoddard's
   uniform-entry device, which they themselves doubted).
7. **Segmentation/boundary** `P_bound` — the probability of a segment boundary at an event, conditioned
   on beat-strength class (the Temperley 2009 change-on-strong-beat shape: above-tactus ≫ tactus ≫
   sub-tactus; our values fit from the corpus) and on the fermata (below). Segment duration is
   otherwise implicit-geometric with a hard length cap (the established semi-Markov default; an
   explicit harmonic-rhythm duration model is recorded as CONJECTURE-gated future work).
8. **Fermata** — enters `P_bound` as a boundary prior (the chorale phrase-end convention) and enters
   the cadence factor as a cadence-location prior, with de Clercq's weak-beat displacement (the
   cadential arrival may sit one strong beat before a metrically weak fermata) as a covariate, not an
   exception.
9. **Cadence factor** — key-axis evidence at candidate cadence sites: the leading-tone resolution
   (seventh degree rising to the tonic in candidate key k), the tritone pair (both the fourth and
   seventh degrees of k sounding in the approach), dominant-to-tonic bass motion (falling fifth /
   rising fourth), each a feature with a fitted weight (the Bigo feature forms + the Feisthauer
   beats-since-decay shape). The known false positives (the parallel major/minor of the same tonic;
   plagal motion misread) are carried as feature refinements, and the factor's weight must respect the
   measured weakness of half-cadence detection. This is the OI-166 channel delivered as a factor.
10. **Signature/declared-mode prior** `P_prior(k_1 | signature, declared mode)` — the ratified weak
    fitted table. **SETTLED (user-ratified 2026-07-19 at the desk simulation, its §4.2 — the S3/C5
    traces): the prior conditions the INITIAL key state only, re-entering only at a notated mid-piece
    signature change (the OI-94(a) discharge moment); the persistent-pull variant is rejected** (a
    linearly growing tax on away-from-signature keys with no theory basis, softly re-introducing the
    OI-174 signature-pull bias). The signature-influence rate is measured by ablation and published at
    every fit.

## 4. The premise ledger (conditional independences — #17a/#17e)

| # | Premise | Label | False-negative path (what would break it, and how we would see it) |
|---|---|---|---|
| P1 | Tones within a segment are conditionally independent given (k, c) and their covariates | ASSUMPTION (Raphael-Stoddard's, flagged weak by them) | Voice-leading dependencies between simultaneous tones (parallel motion, doubling rules) are unmodeled; visible as systematic emission residual on specific voicings — diagnosed at the emission table, not patched by weights |
| P2 | The same-key chord transition is first-order Markov in the degree | ASSUMPTION | Long-range harmonic syntax (a preparation referring across intervening chords) invisible; visible as transition-table residual on sequential progressions; the grammar upgrade is the recorded remedy |
| P3 | Chord transitions are transposition-invariant within a mode | THEORY (Raphael-Stoddard; Ni's tying; standard) | A key-specific idiom (unlikely in this repertoire) would smear; detectable by per-key residual split |
| P4 | Key changes are transposition-invariant (distance and mode pair only) | THEORY (same lineage) | Absolute-key preferences (choral tessitura effects) would smear; detectable by per-key residual split |
| P5 | The entry chord at a key change depends only on the new key | ASSUMPTION (weaker than Raphael-Stoddard's, which we replace) | Pivot-chord modulation says entry depends on the OLD key too (the pivot is diatonic in both); visible as entry-table residual at pivot modulations; remedy is a pivot-aware entry table, its own ledger entry |
| P6 | The bass chord-factor depends only on the chord (not the key) | ASSUMPTION (figured-bass theory adjacent) | Degree-specific inversion practice (the cadential six-four sits on scale degree five) crosses chord and key; NOTE: the cadential six-four is representable as its own degree class in the vocabulary, which discharges the sharpest case — declared here so the vocabulary decision covers it |
| P7 | Segment boundaries depend on meter and fermatas, not on the key | ASSUMPTION | Cadential closure influences segmentation beyond meter; partially covered by the cadence factor sitting at boundaries; visible as boundary residual at cadences |
| P8 | Factor overlap (spelling ~ signature ~ collection; cadence ~ transition) is corrected by the combination weights, not by the tables | The ratified §5a structure | If a single weight cannot correct a structured overlap, the residual shows in the weight fit diagnostics; remedy is a factor merge/split, a structure change — never a value tweak |

## 5. The decode

**The tie-break rule (user-ratified 2026-07-20 at the C++ module build's parity finding):** exact
score ties between candidate decodes are real (proven at 8 corpus pieces — equal-score
segmentations differing by one boundary on repeated-chord runs) and, unbroken, they make the
committed output depend on the platform's floating-point library — unacceptable for the
diff-based adoption measurement and regression stops (#16, reproducibility). Equal-score
candidates therefore resolve by a declared TOTAL order, implemented identically in every decoder
of this specification: fewer segments first; then the earliest boundary-tick sequence
(lexicographic); then the canonical class-key order of the state sequence. No epsilon, no
platform dependence — a pure order on paths.

**The below-threshold scoring rule (user-ratified 2026-07-19 at the fitted-table probe,
`cowork_sensitive_cell_probe.md` finding 2, option 2a):** where a fitted table row stores a pooled
leftover probability for continuations below the count-reliability threshold, the decoder scores a
specific such continuation as the row's leftover mass apportioned in proportion to that outcome
class's overall frequency in the mode (the standard back-off construction) — never by even division
and never as zero.

**Exact semi-Markov Viterbi over the joint state** is the target (the ratified architecture): states
`(k, c)` — 24 keys × the degree vocabulary; the transition factorizes into the block structure
(same-key: chord-transition table; key-change: key-transition × entry tables), which keeps the
per-boundary cost far below the naive square of the state count. With chorale-scale event counts
(roughly 60–150 events), the established segment cap, and the block factorization, exact decode is
expected tractable; **if measurement shows otherwise, the reserve is documented pruning** (restricting
key-change candidates to a fitted-mass neighborhood on the circle of fifths) — an inference technique
requiring its own established-loss measurement, never a silent heuristic. The full posterior (not only
the best path) is retained for the published alternatives and the uncertainty surface (#12; the
carry/abstention policies of the old architecture re-express as posterior mass, not as ad-hoc lists).

## 6. The desk-simulation forms (discharging OI-181)

> **STAGE RUN AND RATIFIED (2026-07-19):** the simulation below was executed on paper as specified —
> `cowork_factorization_desk_simulation.md`, user-ratified 2026-07-19. Outcome: nine of ten traces pass;
> one specification under-determination found and amended (§2 factor granularity); the §5a prior
> question settled (initial-state-only, §3.10). OI-181 is discharged.

Two declared forms, replacing the infeasible full hand-trace:

**(a) Small synthetic cases — hand-computable DP tables, state space truncated to a declared candidate
set (the truncation is part of the exercise's record):**
1. a plain authentic cadence (dominant to tonic, eight events) — the mechanism must commit the obvious;
2. a relative-pair ambiguity (a melody diatonic to one signature, no leading tone until late) — the
   prior and cadence factors must resolve it exactly when the leading tone appears, not before;
3. a Dorian-notated opening (signature one flat short) — the prior's fifth-away mass must behave;
4. a tonicization (the dominant of the dominant, then the dominant) — the applied-degree class must win
   against the momentary-modulation reading by the transition economics, not by fiat;
5. a deceptive cadence (dominant to submediant) — the asymmetric transition table's work.

**(b) Single-piece traces on 3–5 real corpus cases from the known failing sets** (the #17c form:
FIRST "does the mechanism fire?", THEN "which term moves, by how much?"), proposed:
`bwv145.5@12960` (the altered-region chord flip the OI-168 fix corrected — the new structure must get
it without the fix's special form), `bwv352@1440` (the share-tone Am6 vs F♯ø7 case — spelling and bass
factors must carry it), `bwv10.7@36000` (the segmentation over-grab — the boundary factor's test), one
relative-major/minor key-failure case drawn from the key-local residual, and one genuinely modal
chorale (prior + emission variants). The traces are run on paper against the specification BEFORE any
code exists; a surprise at this stage is cheap and is the point.

## 7. What this document does NOT decide

The values of any table or weight (the fitting protocol and its gates: OI-176, OI-177); the robust-stop
adoption protocol (OI-178) and the dual-path/retirement plan (OI-180) — separate documents; the jazz
vocabulary and covariates (the OI-7 gate); the grammar upgrade of the chord-transition factor and the
bass-motion continuity factor (recorded future ledger entries). *(The persistent-vs-initial signature
prior, listed here as open at ratification, was settled by the desk simulation as forecast — see §3.10.)*

*Ratification asked for: the variable structure (§1), the score form (§2), the factor roster (§3), the
premise ledger (§4), the decode plan (§5), and the desk-simulation forms and case list (§6).*
