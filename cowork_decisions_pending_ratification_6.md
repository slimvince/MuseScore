# The 26 decisions pending ratification (D-317…D-342) — complete entries

> **GENERATED REVIEW AID (Cowork, 2026-08-02).** Found by phase 1g's five live-core full reads
> (the SIGNED Layer-4 and Layer-5 designs, the ratified decoder design, the scoring model, the
> redesign plan). Entered with status from the record only — RATIFICATION IS YOURS. Notable:
> D-329 (complete candidate listing as the governing Layer-4 design decision — the OI-275
> conflict's ratified side) and D-317…D-320 (four measured do-not-retry prohibitions missing
> from the scoring model's own dead-end section).


## Group G — Layer 4 — chord identity

### D-317 — The backward-walk boundary change is a dead end — do not retry it

> **Falsified.** The boundary-touching predecessors are OTHER chord tones (C, Eb for
> bwv102.7; G, B for bwv261), not the root. The root attacks later. Changing the
> condition to `< startTickInt` would add C/Eb or G/B to the failing slice but would
> not add Ab or F#. Furthermore, the backward walk exists in 12 call sites (including
> 5 notation-display paths); the parent-scope calls correctly use `<= startTickInt` to
> exclude the previous chord's terminal notes. Do not retry this fix.

**In plain words.** Letting the analysis pick up notes that stop exactly where a stretch begins was tried as a way to recover a missing chord root. It does not recover the root, and the line of work is closed.

**Why.** Measured and named in the record: the notes that touch the boundary are other chord tones, not the root, which attacks a quarter-note later; and the same walk is used at twelve call sites, five of them notation display, where excluding the previous chord's terminal notes is correct.

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Home.** `docs/redesign_plan.md:372-377`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/redesign_plan.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-318 — A short-region external merger is a dead end — do not retry it

> Do not retry a short-region external merger. The tones are already aggregated.

**In plain words.** Adding a pass that merges very short neighbouring stretches was tried and closed: by the time such a pass could run, the stretches it was meant to merge have already been merged by an earlier step.

**Why.** Measured: the spot-check found zero qualifying runs across all thirteen failing Baroque scores, both target cases included — the trigger was dead code, because the existing same-root inline merge inside the first pass already combines the arpeggio micro-stretches (`docs/redesign_plan.md`, the short-region-merger dead-end block, `cc_phase_d_merger_report.md`).

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Home.** `docs/redesign_plan.md:394`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/redesign_plan.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-319 — Re-analysing the merged aggregate is a dead end — no tone-aggregation approach fixes the arpeggio root failure

> Do not retry any Phase D tone-aggregation approach for Δ=+7a. The tones are already
> correct; the predecessor signal is wrong.

**In plain words.** Pooling an arpeggio's notes and re-reading the chord from the pool was implemented, measured, and reverted: pooling makes the answer worse, because the wrong note sounds for longer than the right one. The evidence was never the problem.

**Why.** Measured with the full implementation in place: on the two target scores the wrong root still wins the aggregate by 0.15 and 0.225, because the aggregate is duration-weighted and the wrong note carries 720 ticks against the root's 480; the run regressed both presets and was reverted (`cc_phase_d_merger_report.md` Part B+). The vertical scorer already prefers the correct root in the stretch where that root actually sounds.

**Status.** LIVE · decided 2026-06-09 · ratifier not stated

**Home.** `docs/redesign_plan.md:423-424`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/redesign_plan.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-320 — The absent-root guard is REVERTED and must not be retried — 'absent root means wrong reading' is false corpus-wide

> - **Do not retry the absent-root guard.** It was implemented 2026-06-08 and caused a net
>   regression: 2 fixed (bwv301, bwv269), 4 broken (bwv227.1, bwv342 are DCML-correct absent-root
>   readings; 2 further cascade regressions from `previousRootPc` propagation). The cascade problem
>   is structural: any guard that changes a committed root changes `previousRootPc` for all
>   downstream regions, triggering `rootContinuityBonus` changes across 6 snapshot goldens. The
>   premise "absent root ⇒ wrong reading" is false corpus-wide. **The guard was reverted entirely.**
>   The correct next coding task is **Step 1 (free wiring)** from the redesign sequence above.

**In plain words.** A rule that rejected any chord whose own root is not sounding was built, measured, and removed entirely. It fixed two cases and broke four, and the premise behind it is false across the corpus: sometimes the published human analysis names a chord whose root is not sounding.

**Why.** Measured: two fixed against four broken, two of the four being readings the ground truth itself makes with an absent root, and two further cascade regressions from propagating the changed root forward. The cascade is structural — any guard that changes a committed root changes the predecessor every later stretch reads.

**Status.** LIVE · decided 2026-06-08 · ratifier not stated

**Home.** `docs/redesign_plan.md:555-561`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/redesign_plan.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-321 — Winner selection compares candidate scores exactly, with no epsilon anywhere in the ranking

> Winner selection compares candidate scores with **exact `double` comparisons — there is no
> epsilon anywhere in the ranking.** The final per-bass comparator (`harmonicfunctionlayer.cpp`,
> `applyHarmonicFunction`) is, in order:
>
> 1. `a.score != b.score` → higher `score` wins (exact inequality on the raw `double`);
> 2. else lower `tiePriority` wins (`tiePriority` is the template index — see §2 ordering);
> 3. else lower `rootPc` wins.
>
> This is fully deterministic **given identical floating-point evaluation**: the same inputs
> on the same build always produce the same winner. The `tiePriority`-then-`rootPc` keys
> resolve genuine exact score ties (identical PC sets across enharmonic templates, e.g.
> Sus4♭5 ordered before HalfDim). The omission of an epsilon is intentional — an epsilon
> would make the order depend on a threshold that is itself uncalibrated, and would mask
> rather than resolve near-ties.

**In plain words.** Two candidate readings are ordered by comparing their numbers exactly, with no tolerance band; exact ties are broken by a declared order. This is deliberate.

**Why.** Stated with its reason at the home: a tolerance band would make the order depend on a threshold that is itself uncalibrated, and would hide near-ties instead of resolving them. The tie-break keys resolve the genuine exact ties that arise between enharmonically identical readings.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:201-214`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-322 — Any change to optimization flags or to the order of the scoring arithmetic requires a full corpus A/B on both presets

> These could **flip** under any change that re-associates the floating-point arithmetic:
> different compiler / optimization flags (`-ffast-math`, `/fp:fast`, FMA contraction),
> a different platform's libm, or a reordering of the summation in the score expression
> `(basisIndep + bassDep) × complexityFactor × augFactor + wComplete + wSeq [+ wDim] [+ step]`.
> Treat the exact evaluation order as load-bearing: **any change to optimization flags or to
> the order of the scoring arithmetic requires a full corpus A/B on both presets** before it

**In plain words.** Because candidate scores are compared exactly, re-ordering the arithmetic or changing compiler optimization settings can flip a reading that was decided by a hair. Such a change is not trusted to leave the output unchanged until it has been checked against the whole corpus on both tuning presets.

**Why.** Grounded in two named near-tie classes that sit within a hair of each other — the roughly 0.02-margin class and one score at 1.92 against 1.90 — either of which flips under a re-association of the score expression.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:222-227`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.


## Group F — Layer 3 — key and mode

### D-323 — Asking whether a pitch belongs to the key is a question about the collection, never about the tonic — the tonic-anchored form must not return

> **⚠ Do not reintroduce `keyTonicPc + scale` for a membership test.** A scale-DEGREE is tonic-relative
> by definition and legitimately uses that pair (`buildChordResult`); a membership question must not.
> Note that `buildChordResult`'s `diatonicToKey` flag and the Gate I / Gate L `invRootIsDiatonic` checks
> (`postscoringgates.cpp`) still answer a *collection* question through the *tonic* pair and so still
> carry the OI-168 defect — they are declared, not fixed (see `OPEN_ITEMS.md` OI-170).

**In plain words.** A test of the form 'is this note in the key' must read the key signature's own collection of notes, never a scale laid out from a tonic. Asking about a scale degree is a different question and may legitimately use the tonic.

**Why.** Measured: until 2026-07-14 both key-consuming scoring terms tested a set built from the mode's own tonic, which equals the signature's collection for nineteen of the twenty-one modes and is a semitone off for two — sharing only two of seven notes there. The correction moved exactly one committed chord and made it agree with the ground truth.

**Status.** LIVE · decided 2026-07-14 · ratifier not stated

**Home.** `docs/scoring_model.md:292-296`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.


## Group G — Layer 4 — chord identity

### D-324 — Retirement of a post-scoring rule is global — a rule still doing work on any one preset is retained for all

>   Baroque but 18 load-bearing Jazz firing sites, §1.2). Retirement is global, so a rule live on ANY
>   carrier is retained.

**In plain words.** A correction rule is either removed everywhere or kept everywhere. If it still changes an answer under any one of the tuning presets, it stays.

**Why.** Applied in the ratified retirement audit: four rules were retired only after each was shown to change zero winners on all three presets and to be output-identical when removed, while four others were retained precisely because they remained load-bearing on at least one preset.

**Status.** LIVE · decided 2026-07-05 · ratified by the user

**Home.** `docs/scoring_model.md:827-828`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/scoring_model.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-325 — A correction rule that changes a committed chord's identity is retired or folded in BEFORE the search is widened past it

>   **DECIDED (Cowork ratification, 2026-06-12):** (a) — identity-mutating gates are
>   retired/folded BEFORE the beam widens past them; **3.4 leads 3.2 for those gates** (a
>   gate that mutates root/quality/bass feeds backward edges, so it cannot be cleanly
>   separated from a wider-beam decode). §12 sequencing note updated to match.

**In plain words.** Where a later correction can change which chord was committed, that correction is removed or absorbed into the scoring before the search is allowed to consider more alternatives — otherwise the search would be reading a predecessor that a later step is still going to change.

**Why.** Stated with its reason at the home: a rule that changes a committed root, quality or bass feeds the backward-looking evidence, so it cannot be cleanly separated from a wider search. The alternative — searching against uncorrected identities with a documented re-decision — was considered and not taken.

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Home.** `docs/decoder_design.md:675-678`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/decoder_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-326 — The chord-path search emits the whole path with every stretch's alternatives and margins, not the committed reading alone

>   **DECIDED (Cowork ratification, 2026-06-12):** emit the full path + per-node alternatives
>   + margins (evidence-forwarding) — Stage 6 functional labeling consumes the alternatives;

**In plain words.** The search hands forward, for each stretch, the chosen reading together with the readings it beat and by how much — because the layer above chooses among them.

**Why.** Stated at the home as the evidence-forwarding principle applied to the search's own output: the function layer consumes the alternatives, and the committed reading is the first element of the path by construction.

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Home.** `docs/decoder_design.md:694-695`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/decoder_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-327 — The root-continuity guard reads the reconstructed inversion credit, superseding the designed sounding-third test

> **Ratified form (Cowork, 2026-06-12).** Gate R reads the **pipeline-reconstructed full
> basisDep** (`cell.basisDep + fn::inversionContextBonus(...)`, which Pass A computes for the
> score anyway) via the 3-arg `gateRZeroesRootContinuity` overload. This is byte-identical to
> the old proxy on every quality (it reads the same total credit), is fully intra-layer
> (closes the cross-layer dependency the redesign set out to remove — audit Finding 6), and
> has no Dim gap. The "direct pcWeight third" mechanism was an approximation of the proxy's
> true semantics (`cappedInv == 0`); reading the true semantics is the faithful execution of
> the redesign's *intent*. The originally designed mechanism text is retained above for the
> record but is not what shipped.

**In plain words.** The guard that withholds the continue-the-same-root reward asks whether the candidate earned any inversion credit at all, rather than testing directly whether its third is sounding. The two agree everywhere except on diminished chords, where the direct test would be wrong.

**Why.** Derived, not assumed: under the guard's only firing conditions the bass-root bonus is necessarily zero and the smallest inversion bonus strictly exceeds the largest penalty, so the old test fires exactly when no inversion credit was earned. The direct sounding-third test diverges on diminished chords, whose only credit additionally requires stepwise bass — a condition no vertical test can see — producing an output-visible swing.

**Status.** LIVE · decided 2026-06-12 · ratified by Cowork

**Home.** `docs/decoder_design.md:408-416`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/decoder_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-328 — A wider search cannot fix the arpeggio root failure — the wrong reading IS the global optimum, so only re-weighting or joint segmentation can

> wrong-root micro-region is the **HIGHEST-scoring node** (locally correct — the DCML root
> is absent from its tones), so the continued-root path is the **genuine global optimum** a
> decode finds *exactly as greedy does* (greedy 5.775 > correct 5.600 on bwv102.7; gap =
> rcb 0.40 − margin 0.225). The "rcb edge **from a low-scoring transient** does not survive
> against the path through the correct root" premise is therefore **wrong** — the transient
> is not low-scoring. Re-ranking cannot fix Δ=+7a; only **re-weighting** (Stage-5 rcb

**In plain words.** On the arpeggio failures the locally wrong reading is not a weak transient that a broader search would discard: it is the best-scoring reading, so a broader search finds exactly what the narrow one found. Fixing it needs different weights or a different segmentation, not a wider search.

**Why.** Derived from the search lattice and verified three times, including against an independent earlier derivation: on the founding score the wrong path scores 5.775 against the correct path's 5.600, the gap being the continuity reward minus the margin. The premise the earlier verdict rested on — that the transient scores low — is measured false.

**Status.** LIVE · decided 2026-06-13 · ratifier not stated

**Home.** `docs/decoder_design.md:558-563`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `docs/decoder_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-329 — Completeness of the candidate list is the priority — a chord never listed can never be chosen

> 1. **List the possible chords.** From the slice's pitches, generate **every** tertian chord the pitches could spell —
>    each basic type at each root — and score each by how well the pitches fit it. **Completeness is the priority:** a
>    chord never listed can never be chosen, and the measured dominant error is "the right chord was never on the list,"
>    not "the wrong one was picked among good options." The fit measure is the one stated in §5 (present chord tones
>    credited; absent ones a mild shortfall; extra notes carried to the membership decision, not penalised as wrong

**In plain words.** For each stretch the analysis first generates every chord the sounding notes could spell, and only then chooses among them. Leaving a chord off the list is the error that matters most, because nothing downstream can recover it.

**Why.** Measured: the dominant remaining error is that the right chord was never on the list, not that the wrong one was picked among good options — which is why complete listing is chosen over a strong re-ranker on a cheap partial list, and why a learned re-ranker is a later refinement over the complete list, never a substitute for it.

**Status.** LIVE · decided 2026-06-24 · ratified by the user

**Home.** `cowork_layer4_chordsymbol_design.md:208-212`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-330 — Never a pooled recompute — the chord is never re-derived from several stretches' notes thrown together

> - **Never a pooled recompute** (the authoritative statement of this prohibition). Membership is judged per slice
>   against the prevailing chord; the layer never pools several slices' pitches into one bag and re-derives a chord from
>   the bag — that over-reads, treating every passing note as a chord tone, and was the failure that motivated the
>   rebuild (§13). The note model stays the lossless source so membership is decided from the real notes, not a lossy
>   aggregate.

**In plain words.** The analysis never gathers the notes of several consecutive stretches into one bag and reads a chord off the bag. Each note's membership is judged in its own stretch against the prevailing chord.

**Why.** Named as the failure that motivated the rebuild: pooling over-reads, because every passing note enters the bag and inflates the chord. Keeping the note model as the lossless source means membership is decided from the real notes rather than from a lossy aggregate.

**Status.** LIVE · decided 2026-06-24 · ratified by the user

**Home.** `cowork_layer4_chordsymbol_design.md:394-398`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-331 — Every chord decision carries its ranked alternatives and its confidence — committed, inherited, and abstained alike, never pruned

>   carries its ranked `alternatives` (together with the prevailing chord) and its `confidenceModel` on **every**
>   decision — Commit and
>   Inherit included, filled before the trichotomy and never pruned — so Layer 5 overrides **by selecting among the readings
>   this layer carried** (never by re-deriving), and the carried confidence is the quantity its override threshold scales

**In plain words.** Whatever the chord layer decides for a stretch, it carries the readings it did not choose and how sure it was. That carry is what lets the layer above correct a decision by choosing among readings rather than working the notes out again.

**Why.** Verified at the source when the overturnable-commit principle was ratified: the carry is filled before the commit/inherit/abstain choice is made and is never pruned, which is what makes the override safe, and the carried confidence is the quantity the override threshold scales against. A lock-in test pins the carry.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer4_chordsymbol_design.md:576-579`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-332 — A carried alternative's added notes are marked UNKNOWN rather than asserted absent — never synthesized

> `extensionsKnown` = true); a carried *alternative*'s extensions are copied from the scorer's own ranked result where
> that cell produced one, else left **honest-carry** (extensions = 0, `extensionsKnown` = **false** — the seventh is
> *unknown*, never asserted absent, and never synthesized). A Layer-5 consumer reads the extensions only when

**In plain words.** When the chord layer carries a reading it did not choose, it states its added notes (the seventh, ninth and so on) only where they were genuinely worked out. Otherwise it says they are unknown — it never claims there are none, and never invents them.

**Why.** The information-loss principle applied to the carry: an unknown that is recorded as an absence would be read downstream as a fact. A consumer reads the added notes only when they are marked known and otherwise stays at triad level, so an honest gap is a coverage limit rather than a wrong answer.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Home.** `cowork_layer4_chordsymbol_design.md:366-368`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-333 — The membership tie-break's direction is an idiom-calibrated number, never a branch on style — the three-tier structure is fixed

>   **idiom-calibrated** (the style-only-in-calibration contract, ARCHITECTURE.md §2.15) — record the threshold as a
>   preset/idiom constant at the precision phase (§0), never a structural branch. Source: `cowork_architecture_review_2026_07.md` §7 (F-12, A-10).

**In plain words.** How a note that steps on one side only is judged depends on the style: in chorale writing an accented foreign note is usually a real chord note, in late-romantic writing it usually is not. That difference is carried as a number set per idiom, never as a separate code path per style; the three-tier rule itself does not vary.

**Why.** Grounded in the external architecture review's late-romantic simulation, which found that long accented appoggiaturas are the norm in that idiom, so the same weight evidence should lean the other way — and in the standing contract that style lives only in calibration.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Home.** `cowork_layer4_chordsymbol_design.md:606-607`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-334 — The bare-fifth chord type stays in the catalogue structurally; whether it wins is an idiom-calibrated number

>   honest quality-abstention reading for genuinely third-less textures — E-14 zero information loss), and its
>   **competitiveness is an idiom-calibrated constant** (`kPowerChord3PcPenalty` — the Stage-5 manifest already
>   declares it idiom-varying), never a structural per-idiom branch: a large idiom-#2 value effectively yields the
>   dyad to context-completed triads, a small idiom-#4 value lets C5 stand. **Measured support (Stage-5 Phase 2.1,

**In plain words.** Whether a root-and-fifth with no third counts as a chord is a question music theory itself answers differently by style. The pattern therefore stays available to every style, and how strongly it competes is set per idiom rather than switched on and off by style.

**Why.** Grounded in the theory both ways — common-practice theory requires three pitches for a chord while popular practice treats the power chord as a standard label — and measured: the fit's feasible direction on the Bach data raises the penalty, aligning with the common-practice answer, while the blocked direction gains root agreement only because the objective is quality-silent and adds meaningful functional errors.

**Status.** LIVE · decided 2026-07-05 · ratifier not stated

**Home.** `cowork_layer4_chordsymbol_design.md:617-620`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer4_chordsymbol_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.


## Group H — Layer 5 and Layer 6 — function, cadence, grouping

### D-335 — The function layer outputs the Roman numeral; the tonic/subdominant/dominant summary is a derived read-out, never a stored output

> - **D1 — Output the Roman numeral; the three-role summary is a derived read-out (decided, user, 2026-06-26).** The Roman
>   numeral is the complete, precise analysis and is what the reference corpora evaluate; the three-role summary
>   (tonic/subdominant/dominant) is deterministically derivable from it and therefore lossy to store as a primary output.
>   *Rejected:* a first-class three-role analysis — it would have to resolve the few context-dependent role cases, which no
>   reference data can verify, violating the build-only-what-we-can-verify discipline. The read-out, if built for
>   accessibility, defaults those cases to their tonic-side bucket. (Full reasoning: methods catalog §1.)

**In plain words.** The layer's answer is the Roman numeral — the complete, precise reading. The coarse three-role label can be worked out from it whenever a display needs it, so it is never stored or used to drive the analysis.

**Why.** Measured against the field: every published autonomous Roman-numeral system represents and evaluates the analysis as the numeral's components and none emits a three-role head. A first-class three-role analysis is rejected because it would have to resolve context-dependent role cases no reference data can verify.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:612-617`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-336 — Cadence detection is key-agnostic and votes for the key rather than reading one

> - **D2 — Cadence detection is key-agnostic and votes for the key; it does not read a resolved key.** *Rejected:* the prior
>   key-dependent detector, which is circular and conflates the perfect with the imperfect cadence; and the single-chord
>   interval test, which false-positives on tonic-to-subdominant and tonic-to-dominant because it tests leading-tone
>   presence (the major third of any major triad) rather than leading-tone resolution. The event-pair feature test with the
>   phrase gate is the corrected design.

**In plain words.** Points of harmonic closure are found without being told the key, and each one casts a vote for what the key is. Reading a key that a cadence is supposed to help decide would be circular.

**Why.** Both rejected alternatives are named with their defect: the earlier key-dependent detector is circular and conflates the perfect with the imperfect cadence, and a single-chord interval test false-positives on tonic-to-subdominant and tonic-to-dominant because it tests whether the leading tone is present rather than whether it resolves. The layer's own recorded limit is that a plain V-to-I and a plain I-to-IV are exact transpositions, so the resolution event alone cannot separate them — which is why the phrase gate, the seventh, and the key layer's aggregation carry the discrimination.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:618-622`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-337 — A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost

> - **D3 — Tonicization is the default; modulation requires cadence confirmation plus persistence, as a change-cost.**
>   *Rejected:* a fixed-duration rule (no published threshold exists and the boundary is a continuum); and resolving the
>   distinction in the key layer (it needs function). The hysteresis over the local-key decision matches the ground-truth

**In plain words.** When the music leans toward a note other than the home tonic, the home key holds and the chord is written as an applied chord. The key changes only when a cadence confirms the new key and the music stays in it; how long it must stay is a cost that falls as the candidate area grows, not a fixed number of bars.

**Why.** Both alternatives are rejected with reasons: a fixed-duration rule has no published threshold and the boundary is a genuine continuum, and resolving the distinction in the key layer cannot work because it needs function. The hysteresis form is chosen because it matches the ground-truth annotation convention.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:623-625`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-338 — The function layer selects among the chord layer's carried readings and never re-derives a chord from the notes

> - **D4 — The layer selects among Layer 4's carried readings; it never re-derives.** *Rejected:* re-scoring the slice from
>   the notes (that is Layer 4's job and would duplicate it) — the structural content of the ratified resolution-by-
>   selection: a case separable by a note cue is a lower-layer case, a case separable only by function is this layer's,
>   leaving no third box.

**In plain words.** Where the chord layer left a stretch open, this layer picks one of the readings that layer carried. It never goes back to the notes and works out a chord of its own.

**Why.** Structural, and stated as such: a case separable by a note cue is a lower-layer case and a case separable only by function is this layer's, which leaves no third box — so re-scoring from the notes would duplicate the layer below.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:627-630`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.


## Group C — Cross-cutting analysis contracts

### D-339 — A confident earlier decision can be overturned by decisive later evidence, through ONE confidence-weighted forward-recompute mechanism — architecture-wide

> - **D7 — A confident earlier inference can be overturned by decisive later evidence, via one general
>   confidence-weighted forward-recompute mechanism (decided, user, 2026-06-26; see §8).** Every later layer brings its
>   independent evidence to bear on every earlier inference; agreement reinforces, and a *confident* commit is overturned
>   only when the contradicting evidence crosses a threshold scaled to the earlier layer's confidence — firing a localized,
>   forward, convergence-bounded recompute. The two channels this layer needs (the modulation recompute §5.4 and the
>   fine-grain chord override §5.5/§10) are **instances** of this one mechanism. *Rejected:* (a) treating each override as a
>   bespoke one-off (it hides that they are the same mechanism and makes generalizing a rewrite); (b) a hard
>   confidence-gate that locks confident commits permanently (a confidently-wrong commit must stay recoverable — this is
>   what gives the precision phase tunable per-channel thresholds); (c) a backward re-derivation or full joint cross-layer
>   search (measured inert — the gain is soft-evidence quality carried forward, not cycling). The mechanism and its
>   direction are fixed here; the thresholds are precision-phase. **This decision is architecture-wide** (it generalizes the
>   forward-only control-flow contract for all layers, not just this one) — to be promoted into the target-architecture

**In plain words.** Every later stage brings its own evidence to bear on every earlier decision. Agreement strengthens it; disagreement overturns it only when the contradicting evidence is strong enough, and how strong depends on how sure the earlier stage was. When that happens the affected passage is re-read forward once, and the overturned decision is then closed for the rest of the pass.

**Why.** Three alternatives are rejected with reasons: treating each override as a one-off hides that they are the same mechanism; a hard gate that locks confident decisions permanently makes a confidently-wrong decision unrecoverable; and a backward re-derivation or full joint cross-layer search was measured inert, the gain being soft-evidence quality carried forward rather than cycling. Confidence is what sets the bar to overturn, which is what gives the later calibration phase a tunable lever instead of an absolute veto.

**Status.** LIVE · decided 2026-06-26 · ratified by the user

**Home.** `cowork_layer5_function_design.md:637-648`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.


## Group H — Layer 5 and Layer 6 — function, cadence, grouping

### D-340 — The reading the function layer emits IS the selected source's committed identity, carried whole — never rebuilt field by field

> **The carried chord identity is emitted VERBATIM (carry-fix 2, 2026-07-02).** "Additive, does not replace" is literal at
> the struct level: the reading this layer emits for a slice is the *selected source's committed identity carried whole*
> (root + quality + committed **bass/inversion** + the Layer-4-carried **extensions** with their natural-fifth and
> extensions-known flags),
> never a reconstruction from the §5.0 `{root, quality}` progression projection. A standing commit emits its own `chosen`;
> a neighbour-selected override emits that neighbour's identity as-is; an abstain resolution emits the selected carried
> reading — honest-carry `extensionsKnown=false` (unknown, not asserted-absent) states included. This is what lets the
> downstream base Roman numeral render the figured-bass inversion (65/43/42) and the applied-seventh (`V7/x`) from the

**In plain words.** When this layer keeps, overrides or resolves a reading, it passes on the chosen reading's own record intact — its bass, its inversion, its added notes. It never reassembles a reading from the root and quality alone, which would silently drop the rest.

**Why.** Stated with the loss it prevents: rebuilding from the progression's root-and-quality projection would flatten the committed bass and inversion and the carried added notes, so the figured-bass inversion and the applied seventh could no longer be rendered from what the chord layer actually committed. A neighbour-root with this stretch's bass is not a carried candidate, so it is not synthesized.

**Status.** LIVE · decided 2026-07-02 · ratifier not stated

**Home.** `cowork_layer5_function_design.md:547-554`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-341 — The licensed root-motion set is completed by theory — the ascending fifth, the descending second and the diatonic diminished fifth are added

> 12. **★ §5.0 grammar completion (found 2026-07-02 by the D5 consistency check — ★ RATIFIED by the user 2026-07-03;
>     the §5.0 enumeration is amended, the code increment is pending).** The licensed
>     root-motion set descended from the old scoring-bonus signals and omitted three theory-licensed motions the
>     catalog's
>     own musically-correct entries exercise: **ascending fifth / plagal motion** (IV→I, I→V — tonic-to-dominant!),
>     **descending second** (the Phrygian/Andalusian step), and the **diatonic diminished fifth** (the IV→viiᵒ link of
>     the full circle). The amendment: extend `isLicensedProgression` (+ this §5.0's enumeration, now done) accordingly
>     — algorithmic
>     completion per theory, NOT tuning; its own small dormant increment with tests; the consumer's consistency test
>     then tightens to the clean assert. Evidence: the 6-entry/**11-motion** failure table, measured, enumerated and

**In plain words.** The list of chord-to-chord root motions the analysis treats as real functional progressions was inherited from an older scoring mechanism and left out three motions that standard theory licenses and the project's own catalogue uses. They are added. This is completing an algorithm against theory, not tuning it.

**Why.** Measured by the catalogue-versus-grammar consistency check: six catalogue entries exercising eleven motions failed against the grammar as coded, and the eleven are enumerated and pinned in the consumer's own test. The three missing motions are tonic-to-dominant and plagal motion, the Phrygian step, and the diminished fifth that closes the circle of fifths.

**Status.** LIVE · decided 2026-07-03 · ratified by the user

**Home.** `cowork_layer5_function_design.md:888-897`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

### D-342 — Putting the function layer into production is DEFERRED INDEFINITELY — the posture is a dormant build with ground-truth validation

> - **Engagement framing.** References to an "engagement hard-stop" / "before any production switch" (§5/§10) remain true
>   *conditionally* — engagement (Phase 5d) is **deferred indefinitely** (production out of scope; the posture is dormant
>   build + ground-truth validation). The hard-stops apply *if* a switch is ever made; they are not pending work.

**In plain words.** Switching the function layer on in the product is not scheduled. It is built and checked against published human analyses, and stays inactive; the conditions written for a switch apply if one is ever made, and are not outstanding work.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `cowork_layer5_function_design.md:696-698`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Found by the phase-1g triage wave, 2026-08-02, reading `cowork_layer5_function_design.md` IN FULL. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1g ratification queue.

