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

**Why.** Theory basis cited at ARCHITECTURE.md:9 - `cowork_key_chord_joint_inference_grounding.md`; the forcing constraint is the circular dependency list at ARCHITECTURE.md:689-703 (key<->chord, segmentation<->chord, non-chord-tone<->chord, function<->chord identity), which a feed-forward pipeline cannot resolve correctly.

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

**Provenance.** ARCHITECTURE.md:48-49 cites cowork_joint_estimator_factorization.md as the full specification. The cap's FORM is the established semi-Markov default (cowork_joint_estimator_factorization.md:112-114); the VALUE 4 has no recorded derivation anywhere in the record - derivation not recorded

### D-005 — The joint estimator is the production inference layer on the batch and corpus surface

> the joint estimator
> is now the PRODUCTION inference layer on the batch/corpus surface

**In plain words.** Everything the measurement corpus is graded on now comes from the joint estimator, not from the older chord-by-chord pipeline.

**Why.** Measurement, ARCHITECTURE.md:37-38 and `tools/joint_estimator/adoption_record.json`: on the robust unit the joint decode reads root 77.03 / Roman numeral 64.12 / key-local 78.42 %, against the legacy pipeline's 66.04 / 46.33 / 65.99 %, and the class-(b) hard-stop duration falls 33 % (2,714,000 -> 1,817,280 ticks per preset).

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:11-12`

**Provenance.** CLAUDE.md gate block (A); tools/joint_estimator/adoption_record.json; open_items/OI-178 Note (2026-08-02): production on the batch/corpus surface is a development/measurement posture, not distribution; the fitting-pool licence constraint (D-292, reaffirmed binding) governs what may SHIP — see OI-271.

### D-006 — The published uncertainty surface is two full candidate lists, with no truncation

> publishes, per
> committed segment, the ESTABLISHED content-score uncertainty surface as two full candidate lists (no truncation
> constant)

**In plain words.** For every chord it commits to, the estimator also publishes how every other tonality and every other chord would have scored - the complete lists, not a top-few.

**Why.** Stated constraint, `cowork_joint_estimator_factorization.md:173-175`: the full posterior, not only the best path, is retained for the published alternatives and the uncertainty surface (#12, no information loss) - the old carry and abstention policies re-express as posterior mass rather than ad-hoc lists.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:52-54`

**Provenance.** ARCHITECTURE.md:51 names it 'the notation output-surface contract §3.3 GROUP (i)'

### D-007 — The published scores are log-scores, not probabilities

> The scores are LOG-scores, NOT probabilities, and gaps
> are score differences

**In plain words.** The numbers beside each alternative are not chances of being right. They are model scores, and the difference between two of them is a score gap, not a percentage.

**Why.** Stated constraint, ARCHITECTURE.md:58-60: the published numbers are within-segment content scores re-scored by `segmentContentScore`, so they are log-scores and gaps are score differences; turning them into probabilities needs the forward-backward marginals, which are a separate later step.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:59-60`

**Provenance.** ARCHITECTURE.md:59-61; the true-probability step is deferred to OI-193

### D-008 — The true probabilities are deferred to a later step

> **GROUP (ii) forward-backward marginals are NOT delivered here — OI-193's later step.**

**In plain words.** The proper probability for each reading - the kind that can be checked against how often it is actually right - has not been built yet; it is a named later piece of work.

**Why.** Same constraint as D-007: the marginals the true probabilities require are not computed by the decode as it stands (ARCHITECTURE.md:60), so the step is named and deferred rather than approximated.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:60`

**Provenance.** open_items/OI-193 (OPEN)

### D-095 — The dual path during the joint-estimator build is a declared, bounded, pre-ratified migration state

> migration state (#23) is therefore CLOSED on both surfaces, and the legacy `region::analyzeRegions` →
> `analyzeSection` path is compiled and dormant, awaiting deletion at the OI-180 retirement map. The first

**In plain words.** Building the new estimator beside the old one temporarily breaks the rule that there is one way to do each thing. That was declared in advance, bounded, and given a retirement plan.

**Why.** Stated constraint, `CLAUDE.md` principle #23 and open_items/OI-180: an end-state principle (#6, one path per concern) that a planned change must temporarily violate needs a lawful transition - the violation declared, bounded, and pre-ratified with a retirement map - so that migration is a first-class state rather than an undeclared exception.

**Status.** SUPERSEDED IN FACT · decided 2026-07-19 · ratified by user

**Home.** `ARCHITECTURE.md:43-44`

**Provenance.** open_items/OI-180 (PROTOCOL RATIFIED 2026-07-19; forward exit EXECUTED on both surfaces 2026-07-27). The ARCHITECTURE.md text at :39-40 still says the notation layer stays legacy - see OPEN_ITEMS OI-232 ★ Verbatim RE-TAKEN 2026-08-02 (the phase-1 truth-sync): the sentence this entry quoted — 'STAGED SCOPE (declared migration state, #23): the in-app NOTATION layer stays on the legacy L1-L6 pipeline' — was false at HEAD and is corrected in place (OPEN_ITEMS OI-232 item 1). The decision itself is unchanged; what moved is the migration state's status, which the corrected text now states as CLOSED on both surfaces.

### D-096 — Fitted values are fit once against ground truth, never per-case tuned

> **(a) Factor FORMS come from theory; factor VALUES are fit ONCE against ground truth and are never tuned
> per case.** Every factor's shape is derived from established music theory before any number is attached to

**In plain words.** The shape of each piece of evidence comes from music theory. Its numerical strength is learned once from annotated music, and never adjusted to make a particular passage come out right.

**Why.** Stated constraint, OPEN_ITEMS.md:25 (the governing architecture decision banner) with `CLAUDE.md` #8 and DEFECT_TYPES.md DT-2: a value tuned per case is fitted to the case and measures nothing on the next one.

**Status.** LIVE · decided 2026-07-17 · ratified by user

**Home.** `ARCHITECTURE.md:263-264`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:15-26, the governing architecture decision banner (user-ratified 2026-07-17), which tracks work and is not a specification home. OPEN_ITEMS OI-237 closes on this move

### D-097 — Held-out evaluation and a capacity budget are declared before any fit

> **(b) The held-out split and the capacity budget are declared BEFORE any value is fit, and the headline
> number is the held-out one.** The ratified protocol is five-fold cross-validation grouped by the shared

**In plain words.** Before the estimator's numbers are learned, we say in advance which music will be held back to test them on, and how many numbers we are allowed to learn at all. The headline number is always the one measured on the held-back music.

**Why.** Stated constraint, `CLAUDE.md` #20: no value is graded on data that helped fit it, so the split and the capacity budget are declared BEFORE fitting and the headline claim is the held-out figure; a fitted-and-self-measured number is not established (#19). The ratified protocols are open_items/OI-176 (5-fold cross-validation grouped by ground-truth file) and OI-177 (parameter inventory, cell own-estimate only at count >= 20, <= 12 weights).

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Home.** `ARCHITECTURE.md:270-271`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:123 (open_items/OI-176 and OI-177, PROTOCOL RATIFIED 2026-07-19, protocols in `cowork_prefit_gates.md`). The standing principle is CLAUDE.md #20. OPEN_ITEMS OI-237 closes on this move

### D-098 — The exact-decode reserve - the declared prune was never adopted

> **(c) The decode is EXACT; the declared reserve prune was never adopted, and what the decoder does narrow
> has no specified form.** Exact semi-Markov Viterbi over the joint state is the ratified search. A prune was

**In plain words.** The estimator was meant to be allowed to narrow its search when that gets too slow. The narrowing rule that was specified turned out to cost more than it saved, so the estimator still searches exactly - and how it actually narrows in practice was never specified.

**Why.** Stated constraint, `cowork_joint_estimator_factorization.md:170-173`: exact decode is expected tractable at chorale-scale event counts, and the reserve prune is an inference technique requiring its own established-loss measurement, never a silent heuristic. What the decoder actually prunes has no recorded derivation at all (open_items/OI-226).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:282-283`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:211 (open_items/OI-188, OPEN - 'bounds every ceiling claim'); the admission rule actually in production still has no ratified basis (open_items/OI-226). OPEN_ITEMS OI-237 closes on this move

### D-114 — The decoder commits its best path; there is no abstention on the key axis

> **(d) On the key axis the decoder commits its maximum-a-posteriori path; it never abstains.** The estimator
> always names a key for every committed segment, so the abstention counter the regression stop reads is

**In plain words.** The joint estimator always names a key. It never declines to answer on the key axis, so the abstention counter is always zero.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:294-295`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only in the CLAUDE.md gate block (A), the OI-178 adoption baselines (user-ratified 2026-07-26). The tension with D-090 (calibrated abstention, ARCHITECTURE.md §5.7a) is NAMED at the new home and deliberately NOT resolved there - resolving it is later work. OPEN_ITEMS OI-237 closes on this move

### D-270 — The held-out evaluation protocol - five-fold cross-validation grouped by ground-truth analysis file

> 2. **The split: 5-fold cross-validation [prov-ratify] over the 326 WiR-covered pieces, grouped by
>    WiR analysis file.** The 326 pieces resolve to 324 distinct analysis files (`docs/score_inventory.md`
>    — some chorales share an analysis); pieces sharing an analysis file share a fold (leakage guard).
>    Fold assignment is generated once with a fixed, committed seed and committed as a stamped artifact
>    (`tools/` + manifest, the #17f pattern); it never changes across fit events (a re-split is a
>    protocol amendment).
> 3. **Everything fitted is fitted inside the training folds only** — the generative tables, the
>    combination weights, AND the fitted structure choices: the degree vocabulary's count threshold and
>    pooling, the smoothing constants, the L2 penalty. Model selection (λ, thresholds) uses inner
>    validation within the training folds; the held-out fold is touched exactly once, by the final
>    fitted model of that fold.

**In plain words.** Evaluation splits the 326 ground-truth-covered pieces into five folds, grouped so that pieces sharing one ground-truth analysis file share a fold. Fold assignment is generated once from a fixed committed seed and never changes. Everything fitted - the tables, the weights, and the fitted structure choices such as the vocabulary threshold, the smoothing constants and the penalty - is fitted inside the training folds only; the held-out fold is touched exactly once, by that fold's final model.

**Why.** The protocol names what it prevents (cowork_prefit_gates.md:25-28): a headline figure graded on data that helped fit it, including the subtle forms - a vocabulary derived from all-corpus counts, a smoothing constant chosen on the grading data, a threshold checked against the final metric. The grouping rule is a stated leakage guard: some chorales share an analysis file.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:32-42`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols including the marked constants, dated 2026-07-19; the held-out protocol at :23-60. It is the protocol form of register entry D-097, which states the general rule at its ARCHITECTURE.md home. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-271 — The capacity budget - a cell keeps its own estimate only above a stated count, and free parameters are bounded against the training tokens

>    table, its dimensions, its raw cell-count histogram from the training data, and the resulting free
>    parameter count. No prose-only budget.
> 2. **Budget rule:** a table cell keeps its own maximum-likelihood estimate iff its training count
>    ≥ 20 [prov-ratify]; below that it is pooled to its declared parent class (the pooling hierarchy
>    declared per table in the artifact) under additive smoothing with a single declared α per table.
>    The degree vocabulary's rare-class pooling (factorization §1) is the same rule applied to the state
>    space itself.
> 3. **Global sanity bound:** total effective free parameters ≤ training tokens / 10 [prov-ratify],
>    verified in the artifact. The combination-weight vector stays ≤ 14 weights, L2-penalized, per the
>    ratified staged-fitting decision. *(Amended ≤ 12 → ≤ 14 by user ratification 2026-07-19 at the
>    weight-fit dispatch: the ratified factorization gives the four cadence features their own fitted
>    weights, putting the enumerated vector at 12–13; the amendment is the lawful #22 path — capacity
>    impact nil, thousands of training tokens per weight either way. Original text: "≤ 12 weights (one
>    per factor plus the declared-mode strength)".)*

**In plain words.** Before any fit, the parameter inventory is published as a generated artifact: every table, its dimensions, its raw cell-count histogram and its resulting free-parameter count. A table cell keeps its own maximum-likelihood estimate only if its training count reaches twenty; below that it is pooled into its declared parent class under smoothing. Total effective free parameters stay at or below one tenth of the training tokens, and the combination-weight vector stays at or below fourteen weights with a penalty.

**Why.** The protocol names what it prevents (cowork_prefit_gates.md:64-65): overfitting in one shot on a 326-piece single-composer corpus, and hand-picking hidden inside the words 'derived from counts'. Publishing the inventory as a generated artifact before fitting is principle #17(f) applied to the fit itself - the budget cannot be asserted in prose after the fact.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:68-81`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols including the marked constants, dated 2026-07-19; the capacity budget at :62-96, with the twelve-to-fourteen weight amendment recorded in place at :77-81 as a lawful protocol amendment. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-272 — The protocol constants are protocol, not tuning - changing one is an amendment, never a fitting act

> Provisional numeric choices inside the protocols (fold count, cell-count threshold, confidence level)
> are marked **[prov-ratify]** — they become binding at ratification but remain protocol constants, not
> fitted values; changing one later is a protocol amendment (#22), not a tuning act.

**In plain words.** The numeric choices inside the pre-fit protocols - the fold count, the cell-count threshold, the confidence level - become binding when the protocols are ratified but remain protocol constants rather than fitted values. Changing one later is a governance amendment, not an act of tuning.

**Why.** It closes the route by which a governance constant becomes a knob: without the distinction, a fold count or a pooling threshold could be moved in response to a disappointing measurement and the move would look like ordinary calibration. The document states the same rule twice (cowork_prefit_gates.md:5-6 and :17-19), once for the ratification and once for the constants themselves.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:17-19`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:17-19 states the rule and :3-6 records its ratification, dated 2026-07-19. It applies principle #22 (a hard gate declares in advance how it handles the largest change it will meet), registered as D-185, to the pre-fit protocols. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-273 — The architecture-adoption variant of the hard regression stop, written before any diff existed

> 3. **Adoption PASS requires ALL of:**
>    - **(i) Held-out:** A's key-agree vs the LOCAL key exceeds the current baseline beyond the
>      piece-bootstrap CI on every preset; root-agree and RN-agree do not degrade beyond the CI (#24 —
>      a difference within the CI is not a finding, in either direction). **(i-b) The modulation-rate
>      guard:** A's key changes per piece sit within 0.75×–1.25× of the ground truth's rate. **The
>      key-HOME column is TRACKED with a mandatory explained decomposition** against the computed GT

**In plain words.** Adopting an architecture replacement in place of the incremental hard stop requires all of: the held-out key agreement against the local key beating the baseline beyond the stated confidence interval on every preset with root and Roman-numeral agreement not degrading beyond it; a modulation-rate guard keeping key changes per piece within a quarter of the ground truth's rate; a net decrease in the class-(b) root-disagree duration on every preset with every added failing run enumerated, classified and individually diagnosed; class-(a) tracked; and user ratification of the whole record as one revertible commit that re-baselines the reference.

**Why.** The protocol names what it prevents (cowork_prefit_gates.md:100-103): negotiating the hard stop on a live diff. The incremental non-increase ratchet was written for incremental change, and an architecture replacement moves runs in both directions by design - so the exceptional-event variant is written while no diff exists, which is principle #22's requirement (register entry D-185).

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:116-121`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols, dated 2026-07-19; the adoption protocol at :98-145, with the home-column amendment recorded in place at :123-129 as a lawful pre-measurement amendment. The event it governed is the OI-178 adoption, whose outcome is in the CLAUDE.md gate block. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-274 — The reverse map - if the new estimator is not adopted it is removed whole, and the retirement map is void

> 5. **The reverse map (if A is not adopted):** A's module is removed whole (one revertible commit), the
>    fold/fit artifacts are kept as measurement history, and the retirement map is void — declared now
>    so non-adoption has a lawful exit too.

**In plain words.** Non-adoption has a declared lawful exit, written at the same time as the adoption path: the new module is removed in one revertible commit, the fold and fit artifacts are kept as measurement history, and the retirement map that would have deleted the superseded code never executes.

**Why.** It is principle #23 (an end-state principle needs a lawful transition) applied in both directions: the sanction that permits two paths for one concern must say how the duplication ends whichever way the decision goes, so that a declared migration state cannot quietly become a permanent one.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_prefit_gates.md:189-191`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols, dated 2026-07-19; the reverse map is item 5 of the dual-path sanction at :189-191. Register entry D-095 records the sanctioned dual path itself at its ARCHITECTURE.md home. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-283 — Meta-finding: never learn keys, the lever is keychain structure - superseded by the joint estimator and the forms-from-theory rule

> - **Never learn keys; the lever is keychain structure (cadence precision).** Settled from both sides.

**In plain words.** A rejection of a learned key detector in favour of structural levers, cadence precision above all. Whichever reading was intended, the later explicit ratifications govern: the joint estimator infers the key inside a theory-declared generative form whose factor values are fitted once against ground truth, and its cadence factor carries the structural insight forward. This finding binds nothing the current design does.

**Why.** The supersession stands on dates and explicitness alone: D-001 (2026-07-17, ratified, adopted with measurement 2026-07-26) and D-096 (forms from theory, values fit once, never per-case tuned) are later, explicit, user-ratified decisions on the same subject. Ruled so that no future reader treats this as a live prohibition over the key axis (the risk that made OI-270 matter).

**Status.** SUPERSEDED BY D-001 and D-096 · date not stated · ratifier not stated

**Home.** `cowork_architecture_reassessment.md:98`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Stated 2026-06-20 in cowork_architecture_reassessment.md §4 ('Meta-findings to institutionalize'); put to the user in §5 ('Ratify: …') with NO recorded answer (open_items/OI-270.md, the phase-1d wave's remainder). ★ RULED by the user 2026-08-02 (the OI-270 split, all four recommendations adopted): SUPERSEDED BY the named later ratified decisions — the governing status derives from the record's dates and explicitness, not from resolving the original statement's ambiguity. The second-partition read of the archives is instructed to flag anything refining these.

### D-285 — Meta-finding: embellishment is chord-first, never a richer vocabulary - absorbed by the emission design and the ornament-label increment

> - **Embellishment = chord-first** (segmentation + NCT post-process), never union re-derive / richer vocabulary.

**In plain words.** Ornamental tones are handled by classifying them against the committed chord - segmentation first, then a non-chord-tone post-process - never by widening the chord vocabulary until every embellishment is a chord. The ratified factorization’s emission carries exactly this shape (chord-member and non-chord-tone categories), and the ornament-label publication is its own ratified increment.

**Why.** Absorbed by ratified successors: the factorization’s emission categories (D-004’s ground-truth-derived compact vocabulary + the per-tone emission’s membership categories) and the OI-194 ornament-label increment. Ruled bindingly BEFORE the phase-3 family design so the struck-versus-sounding emission fix keeps non-chord-tone handling in the emission’s categories rather than solving its problems by vocabulary inflation.

**Status.** SUPERSEDED BY the ratified factorization emission design (D-004 and the OI-194 increment) · date not stated · ratifier not stated

**Home.** `cowork_architecture_reassessment.md:101`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Stated 2026-06-20 in cowork_architecture_reassessment.md §4 ('Meta-findings to institutionalize'); put to the user in §5 ('Ratify: …') with NO recorded answer (open_items/OI-270.md, the phase-1d wave's remainder). ★ RULED by the user 2026-08-02 (the OI-270 split, all four recommendations adopted): SUPERSEDED BY the named later ratified decisions — the governing status derives from the record's dates and explicitness, not from resolving the original statement's ambiguity. The second-partition read of the archives is instructed to flag anything refining these.

