# Decisions group A — The estimator architecture — the joint estimator

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-001 — Key, mode and chord are inferred by ONE joint decode

> Key, mode, and chord are inferred by ONE probabilistic decode
> over `(tonic, mode, chord)` with segmentation as a modeled (semi-Markov) variable and every enumerated clue
> as a theory-grounded factor

**In plain words.** The tonality, the major/minor character and the chord are not worked out one after another. They are worked out together, in a single pass that also decides where one chord ends and the next begins.

**Why.** Theory basis cited at ARCHITECTURE.md:9 - `cowork_key_chord_joint_inference_grounding.md`; the forcing constraint is the circular dependency list at ARCHITECTURE.md:682-696 (key<->chord, segmentation<->chord, non-chord-tone<->chord, function<->chord identity), which a feed-forward pipeline cannot resolve correctly.

**Status.** LIVE · decided 2026-07-17 · ratified by user

**Home.** `ARCHITECTURE.md:4-6`

**Provenance.** ARCHITECTURE.md:3 (GOVERNING DECISION banner); OPEN_ITEMS.md:15-26

### D-002 — The fitted tables and weights are compiled into the binary verbatim

> compiles the five committed artifacts + the selected weight vector
> VERBATIM (JSON bytes, not a parsed-structure codegen) into the generated `jointembeddedartifacts.{h,cpp}`

**In plain words.** The numbers the estimator was trained on are built into the program at compile time rather than read from disk at run time, so a running copy cannot quietly disagree with the numbers we published.

**Why.** Stated constraint, ARCHITECTURE.md:22-23: compiling the fitted values into the binary provenance-LOCKS them at build time (#16/#19) so they cannot silently drift; the `joint_embedded_tests` drift guard (:27-29) is what makes the lock checkable.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:21-22`

**Provenance.** ARCHITECTURE.md:20 names it 'ratified Decision D1'; the ratifier and date are not stated at this home

### D-003 — Inference is preset-independent; presets are presentation concerns

> Inference is **preset-independent** (presets are
> presentation concerns)

**In plain words.** Choosing the Baroque, Jazz or Default preset changes nothing about what the estimator concludes; it changes only how the result is shown.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:33-34`

**Provenance.** CLAUDE.md gate block (A), the OI-178 adoption; open_items/OI-178

### D-004 — The decode state space and the segment cap

> State = `24 keys × a ground-truth-derived Roman-numeral
> vocabulary`, chord = scale-degree-valued (the chord symbol is the derived published fact from (key, degree)), segmentation is a modeled semi-Markov variable, seg_cap 4.

**In plain words.** The estimator chooses among 24 tonalities and a list of chord roles read off the annotated corpus; a chord is named by its role in the key, and the chord symbol is worked out from that. One chord may span at most four consecutive events.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:31-33`

**Provenance.** ARCHITECTURE.md:43-44 cites cowork_joint_estimator_factorization.md as the full specification. The cap's FORM is the established semi-Markov default (cowork_joint_estimator_factorization.md:112-114); the VALUE 4 has no recorded derivation anywhere in the record - derivation not recorded

### D-005 — The joint estimator is the production inference layer on the batch and corpus surface

> the joint estimator
> is now the PRODUCTION inference layer on the batch/corpus surface

**In plain words.** Everything the measurement corpus is graded on now comes from the joint estimator, not from the older chord-by-chord pipeline.

**Why.** Measurement, ARCHITECTURE.md:37-38 and `tools/joint_estimator/adoption_record.json`: on the robust unit the joint decode reads root 77.03 / Roman numeral 64.12 / key-local 78.42 %, against the legacy pipeline's 66.04 / 46.33 / 65.99 %, and the class-(b) hard-stop duration falls 33 % (2,714,000 -> 1,817,280 ticks per preset).

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:11-12`

**Provenance.** CLAUDE.md gate block (A); tools/joint_estimator/adoption_record.json; open_items/OI-178

### D-006 — The published uncertainty surface is two full candidate lists, with no truncation

> publishes, per
> committed segment, the ESTABLISHED content-score uncertainty surface as two full candidate lists (no truncation
> constant)

**In plain words.** For every chord it commits to, the estimator also publishes how every other tonality and every other chord would have scored - the complete lists, not a top-few.

**Why.** Stated constraint, `cowork_joint_estimator_factorization.md:173-175`: the full posterior, not only the best path, is retained for the published alternatives and the uncertainty surface (#12, no information loss) - the old carry and abstention policies re-express as posterior mass rather than ad-hoc lists.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:47-49`

**Provenance.** ARCHITECTURE.md:46 names it 'the notation output-surface contract §3.3 GROUP (i)'

### D-007 — The published scores are log-scores, not probabilities

> The scores are LOG-scores, NOT probabilities, and gaps
> are score differences

**In plain words.** The numbers beside each alternative are not chances of being right. They are model scores, and the difference between two of them is a score gap, not a percentage.

**Why.** Stated constraint, ARCHITECTURE.md:53-55: the published numbers are within-segment content scores re-scored by `segmentContentScore`, so they are log-scores and gaps are score differences; turning them into probabilities needs the forward-backward marginals, which are a separate later step.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:54-55`

**Provenance.** ARCHITECTURE.md:54-56; the true-probability step is deferred to OI-193

### D-008 — The true probabilities are deferred to a later step

> **GROUP (ii) forward-backward marginals are NOT delivered here — OI-193's later step.**

**In plain words.** The proper probability for each reading - the kind that can be checked against how often it is actually right - has not been built yet; it is a named later piece of work.

**Why.** Same constraint as D-007: the marginals the true probabilities require are not computed by the decode as it stands (ARCHITECTURE.md:55), so the step is named and deferred rather than approximated.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:55`

**Provenance.** open_items/OI-193 (OPEN)

### D-095 — The dual path during the joint-estimator build is a declared, bounded, pre-ratified migration state

> STAGED SCOPE (declared migration state, #23)

**In plain words.** Building the new estimator beside the old one temporarily breaks the rule that there is one way to do each thing. That was declared in advance, bounded, and given a retirement plan.

**Why.** Stated constraint, `CLAUDE.md` principle #23 and open_items/OI-180: an end-state principle (#6, one path per concern) that a planned change must temporarily violate needs a lawful transition - the violation declared, bounded, and pre-ratified with a retirement map - so that migration is a first-class state rather than an undeclared exception.

**Status.** SUPERSEDED IN FACT · decided 2026-07-19 · ratified by user

**Home.** `ARCHITECTURE.md:39`

**Provenance.** open_items/OI-180 (PROTOCOL RATIFIED 2026-07-19; forward exit EXECUTED on both surfaces 2026-07-27). The ARCHITECTURE.md text at :39-40 still says the notation layer stays legacy - see OPEN_ITEMS OI-232

### D-096 — Fitted values are fit once against ground truth, never per-case tuned

> **(a) Factor FORMS come from theory; factor VALUES are fit ONCE against ground truth and are never tuned
> per case.** Every factor's shape is derived from established music theory before any number is attached to

**In plain words.** The shape of each piece of evidence comes from music theory. Its numerical strength is learned once from annotated music, and never adjusted to make a particular passage come out right.

**Why.** Stated constraint, OPEN_ITEMS.md:25 (the governing architecture decision banner) with `CLAUDE.md` #8 and DEFECT_TYPES.md DT-2: a value tuned per case is fitted to the case and measures nothing on the next one.

**Status.** LIVE · decided 2026-07-17 · ratified by user

**Home.** `ARCHITECTURE.md:256-257`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:15-26, the governing architecture decision banner (user-ratified 2026-07-17), which tracks work and is not a specification home. OPEN_ITEMS OI-237 closes on this move

### D-097 — Held-out evaluation and a capacity budget are declared before any fit

> **(b) The held-out split and the capacity budget are declared BEFORE any value is fit, and the headline
> number is the held-out one.** The ratified protocol is five-fold cross-validation grouped by the shared

**In plain words.** Before the estimator's numbers are learned, we say in advance which music will be held back to test them on, and how many numbers we are allowed to learn at all. The headline number is always the one measured on the held-back music.

**Why.** Stated constraint, `CLAUDE.md` #20: no value is graded on data that helped fit it, so the split and the capacity budget are declared BEFORE fitting and the headline claim is the held-out figure; a fitted-and-self-measured number is not established (#19). The ratified protocols are open_items/OI-176 (5-fold cross-validation grouped by ground-truth file) and OI-177 (parameter inventory, cell own-estimate only at count >= 20, <= 12 weights).

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Home.** `ARCHITECTURE.md:263-264`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:123 (open_items/OI-176 and OI-177, PROTOCOL RATIFIED 2026-07-19, protocols in `cowork_prefit_gates.md`). The standing principle is CLAUDE.md #20. OPEN_ITEMS OI-237 closes on this move

### D-098 — The exact-decode reserve - the declared prune was never adopted

> **(c) The decode is EXACT; the declared reserve prune was never adopted, and what the decoder does narrow
> has no specified form.** Exact semi-Markov Viterbi over the joint state is the ratified search. A prune was

**In plain words.** The estimator was meant to be allowed to narrow its search when that gets too slow. The narrowing rule that was specified turned out to cost more than it saved, so the estimator still searches exactly - and how it actually narrows in practice was never specified.

**Why.** Stated constraint, `cowork_joint_estimator_factorization.md:170-173`: exact decode is expected tractable at chorale-scale event counts, and the reserve prune is an inference technique requiring its own established-loss measurement, never a silent heuristic. What the decoder actually prunes has no recorded derivation at all (open_items/OI-226).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:275-276`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:211 (open_items/OI-188, OPEN - 'bounds every ceiling claim'); the admission rule actually in production still has no ratified basis (open_items/OI-226). OPEN_ITEMS OI-237 closes on this move

### D-114 — The decoder commits its best path; there is no abstention on the key axis

> **(d) On the key axis the decoder commits its maximum-a-posteriori path; it never abstains.** The estimator
> always names a key for every committed segment, so the abstention counter the regression stop reads is

**In plain words.** The joint estimator always names a key. It never declines to answer on the key axis, so the abstention counter is always zero.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:287-288`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only in the CLAUDE.md gate block (A), the OI-178 adoption baselines (user-ratified 2026-07-26). The tension with D-090 (calibrated abstention, ARCHITECTURE.md §5.7a) is NAMED at the new home and deliberately NOT resolved there - resolving it is later work. OPEN_ITEMS OI-237 closes on this move

