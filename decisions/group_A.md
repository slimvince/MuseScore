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

**Why.** SEARCHED 2026-08-09 and the record HOLDS one, in the decision's own home text: the constraint that forces it is stated in the parenthetical, `ARCHITECTURE.md:33-34` — **presets are presentation concerns**. A preset selects how a result is shown, so nothing it carries may reach what the estimator concludes; the three preset directories being identical at the inference fields is the measured consequence, recorded in `CLAUDE.md` gate block (A) at the OI-178 adoption. What the record does NOT hold is a separate derivation beyond that constraint, and none is invented here.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:33-34`

**Provenance.** CLAUDE.md gate block (A), the OI-178 adoption; open_items/OI-178

### D-004 — The decode state space and the segment cap

> State = `24 keys × a ground-truth-derived Roman-numeral
> vocabulary`, chord = scale-degree-valued (the chord symbol is the derived published fact from (key, degree)), segmentation is a modeled semi-Markov variable, seg_cap 4.

**In plain words.** The estimator chooses among 24 tonalities and a list of chord roles read off the annotated corpus; a chord is named by its role in the key, and the chord symbol is worked out from that. One chord may span at most four consecutive events.

**Why.** SEARCHED 2026-08-09, and the answer differs BY PART, which is why one sentence will not do. The state space's FORM is grounded: the chord is scale-degree-valued and the symbol is derived from (key, degree), and the segmentation is a modeled semi-Markov variable whose form is the established default of that model class (`cowork_joint_estimator_factorization.md:112-114`, which `ARCHITECTURE.md:48-49` names as the full specification). **The segment cap's VALUE — four — has NO recorded derivation anywhere in the record**: no citation, no measurement, no alternative considered. That gap is one of the founding instances `CLAUDE.md`'s carry-its-defense rule names in its own text, and it is stated here rather than filled (a defense written after the fact without a source is invention).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:31-33`

**Provenance.** ARCHITECTURE.md:48-49 cites cowork_joint_estimator_factorization.md as the full specification. The cap's FORM is the established semi-Markov default (cowork_joint_estimator_factorization.md:112-114); the VALUE 4 has no recorded derivation anywhere in the record - derivation not recorded ★ THE DECIDING ACT RECOVERED AND KEPT (user's ruling of 2026-08-16, cowork_rulings_2026_08_16_preparation_return.md §3 (B1)): a passage at `ARCHITECTURE.md` line 3, carrying a user-act marker and matching the decisions register's own recogniser `semi-Markov`, reads — "**★★ GOVERNING DECISION (user-ratified 2026-07-17): the key/mode/chord estimator is JOINT — see `cowork_joint_estimator_architecture.md`.** Key, mode, and chord are inferred by ONE probabilistic decode over `(tonic, mode, chord)` with segmentation as a modeled (semi-Markov) variable and every enumerated clue as a theory-grounded factor — NOT the feed-forward, per-layer pipeline the layer sections below still describe. Those layer sections (L1–L6) remain the accurate description of the CURRENT code and its retirements, but the TARGET architecture is the joint estimator; the layer specs are updated to it as the design pass proceeds. Theory basis: `cowork_key_chord_joint_inference_grounding.md`." The act is quoted from `tools/audit/deciding_act_recovery.json`; no other field of this entry is touched.

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

**Home.** `ARCHITECTURE.md:58-60`

**Provenance.** ARCHITECTURE.md:51 names it 'the notation output-surface contract §3.3 GROUP (i)'

### D-007 — The published scores are log-scores, not probabilities

> The scores are LOG-scores, NOT probabilities, and gaps
> are score differences

**In plain words.** The numbers beside each alternative are not chances of being right. They are model scores, and the difference between two of them is a score gap, not a percentage.

**Why.** Stated constraint, ARCHITECTURE.md:58-60: the published numbers are within-segment content scores re-scored by `segmentContentScore`, so they are log-scores and gaps are score differences; turning them into probabilities needs the forward-backward marginals, which are a separate later step.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:65-66`

**Provenance.** ARCHITECTURE.md:59-61; the true-probability step is deferred to OI-193

### D-008 — The true probabilities are deferred to a later step

> **GROUP (ii) forward-backward marginals are NOT delivered here — OI-193's later step.**

**In plain words.** The proper probability for each reading - the kind that can be checked against how often it is actually right - has not been built yet; it is a named later piece of work.

**Why.** Same constraint as D-007: the marginals the true probabilities require are not computed by the decode as it stands (ARCHITECTURE.md:60), so the step is named and deferred rather than approximated.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:66`

**Provenance.** open_items/OI-193 (OPEN) ★ THE DECIDING ACT RECOVERED AND KEPT (user's ruling of 2026-08-16, cowork_rulings_2026_08_16_preparation_return.md §3 (B1)): a passage at `ARCHITECTURE.md` line 11, carrying a user-act marker, a ratification event named and matching the decisions register's own recogniser `forward-backward marginal`, reads — "**★★ AS-BUILT (the OI-178 adoption, user-ratified 2026-07-26, option 1 — STAGED SCOPE): the joint estimator is now the PRODUCTION inference layer on the batch/corpus surface.** As-built module `src/composing/analysis/joint/`: the **L1 fact adapter** (`jointfactadapter` — score → `Piece` from the published `notemodel::notatedNotes()` tie-unresolved surface + the score's structural facts, per the OI-180 sanction: no module-private raw-note walk); the **event lattice + exact block-factorized semi-Markov Viterbi decoder** (`jointdecoder`) with the ratified **§5 total-order tie-break**; the **factor log-probability provider** (`jointadapter` — the ten-factor log-linear score, Katz leftover option 2a); the frozen generative **tables** (`jointtables` — the committed all-326 `tables_all.json` / `note_tables_all.json` / `factor_presence_all.json` / `fermata_boundary_addendum.json`); and the **wei" The act is quoted from `tools/audit/deciding_act_recovery.json`; no other field of this entry is touched.

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

**Home.** `ARCHITECTURE.md:280-281`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:15-26, the governing architecture decision banner (user-ratified 2026-07-17), which tracks work and is not a specification home. OPEN_ITEMS OI-237 closes on this move

### D-097 — Held-out evaluation and a capacity budget are declared before any fit

> **(b) The held-out split and the capacity budget are declared BEFORE any value is fit, and the headline
> number is the held-out one.** The ratified protocol is five-fold cross-validation grouped by the shared

**In plain words.** Before the estimator's numbers are learned, we say in advance which music will be held back to test them on, and how many numbers we are allowed to learn at all. The headline number is always the one measured on the held-back music.

**Why.** Stated constraint, `CLAUDE.md` #20: no value is graded on data that helped fit it, so the split and the capacity budget are declared BEFORE fitting and the headline claim is the held-out figure; a fitted-and-self-measured number is not established (#19). The ratified protocols are open_items/OI-176 (5-fold cross-validation grouped by ground-truth file) and OI-177 (parameter inventory, cell own-estimate only at count >= 20, <= 12 weights).

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Home.** `ARCHITECTURE.md:289-290`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:123 (open_items/OI-176 and OI-177, PROTOCOL RATIFIED 2026-07-19, protocols in `cowork_prefit_gates.md`). The standing principle is CLAUDE.md #20. OPEN_ITEMS OI-237 closes on this move

### D-098 — The exact-decode reserve - the declared prune was never adopted

> **(c) The decode is EXACT; the declared reserve prune was never adopted, and what the decoder does narrow
> has no specified form.** Exact semi-Markov Viterbi over the joint state is the ratified search. A prune was

**In plain words.** The estimator was meant to be allowed to narrow its search when that gets too slow. The narrowing rule that was specified turned out to cost more than it saved, so the estimator still searches exactly - and how it actually narrows in practice was never specified.

**Why.** Stated constraint, `cowork_joint_estimator_factorization.md:170-173`: exact decode is expected tractable at chorale-scale event counts, and the reserve prune is an inference technique requiring its own established-loss measurement, never a silent heuristic. What the decoder actually prunes has no recorded derivation at all (open_items/OI-226).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:303-304`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:211 (open_items/OI-188, OPEN - 'bounds every ceiling claim'); the admission rule actually in production still has no ratified basis (open_items/OI-226). OPEN_ITEMS OI-237 closes on this move

### D-114 — The decoder commits its best path; there is no abstention on the key axis

> **(d) On the key axis the decoder commits its maximum-a-posteriori path; it never abstains.** The estimator
> always names a key for every committed segment, so the abstention counter the regression stop reads is

**In plain words.** The joint estimator always names a key. It never declines to answer on the key axis, so the abstention counter is always zero.

**Why.** SEARCHED 2026-08-09 and the record holds NO DERIVATION — it states the behaviour and its consequence, never a reason for choosing it. What it does state, and what a reader must not mistake for a defense: that the decoder commits its maximum-a-posteriori path, and that the abstention counter the regression stop reads therefore reads zero on the production arm. **No reason is recorded for committing rather than abstaining on that axis**, and what the record carries instead is a NAMED and deliberately unresolved tension with the calibrated-abstention design (**D-090**) at this entry's own home. So the gap here is a missing justification for a LIVE production behaviour, which is a stronger thing than a missing gloss on a retired one — stated, not filled.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:331-332`

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_prefit_gates.md:32-42`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“The held-out evaluation protocol”** — `## The held-out evaluation protocol (OI-176; gates the fit event; #20/#19/#16)` (heading at line 23). A delegation at ARCHITECTURE.md:52 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_prefit_gates.md:68-81`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“The capacity budget”** — `## The capacity budget (OI-177; gates the fit event; #20)` (heading at line 62). A delegation at ARCHITECTURE.md:52 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols including the marked constants, dated 2026-07-19; the capacity budget at :62-96, with the twelve-to-fourteen weight amendment recorded in place at :77-81 as a lawful protocol amendment. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-272 — The protocol constants are protocol, not tuning - changing one is an amendment, never a fitting act

> Provisional numeric choices inside the protocols (fold count, cell-count threshold, confidence level)
> are marked **[prov-ratify]** — they become binding at ratification but remain protocol constants, not
> fitted values; changing one later is a protocol amendment (#22), not a tuning act.

**In plain words.** The numeric choices inside the pre-fit protocols - the fold count, the cell-count threshold, the confidence level - become binding when the protocols are ratified but remain protocol constants rather than fitted values. Changing one later is a governance amendment, not an act of tuning.

**Why.** It closes the route by which a governance constant becomes a knob: without the distinction, a fold count or a pooling threshold could be moved in response to a disappointing measurement and the move would look like ordinary calibration. The document states the same rule twice (cowork_prefit_gates.md:5-6 and :17-19), once for the ratification and once for the constants themselves.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_prefit_gates.md:17-19`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **the opening block (above the first section heading)** — `# The pre-fit gates for the joint estimator (OI-176 / OI-177 / OI-178 / OI-180) — ★ USER-RATIFIED 2026-07-19` (heading at line 1). A delegation at ARCHITECTURE.md:52 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_prefit_gates.md:116-121`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“The robust-stop architecture-adoption protocol”** — `## The robust-stop architecture-adoption protocol (OI-178; before A's first measured decode; #22/#24)` (heading at line 98). A delegation at ARCHITECTURE.md:52 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols, dated 2026-07-19; the adoption protocol at :98-145, with the home-column amendment recorded in place at :123-129 as a lawful pre-measurement amendment. The event it governed is the OI-178 adoption, whose outcome is in the CLAUDE.md gate block. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-274 — The reverse map - if the new estimator is not adopted it is removed whole, and the retirement map is void

> 5. **The reverse map (if A is not adopted):** A's module is removed whole (one revertible commit), the
>    fold/fit artifacts are kept as measurement history, and the retirement map is void — declared now
>    so non-adoption has a lawful exit too.

**In plain words.** Non-adoption has a declared lawful exit, written at the same time as the adoption path: the new module is removed in one revertible commit, the fold and fit artifacts are kept as measurement history, and the retirement map that would have deleted the superseded code never executes.

**Why.** It is principle #23 (an end-state principle needs a lawful transition) applied in both directions: the sanction that permits two paths for one concern must say how the duplication ends whichever way the decision goes, so that a declared migration state cannot quietly become a permanent one.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_prefit_gates.md:189-191`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“The sanctioned dual path and the retirement map”** — `## The sanctioned dual path and the retirement map (OI-180; #23/#6/#15)` (heading at line 147). A delegation at ARCHITECTURE.md:52 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** cowork_prefit_gates.md:3 records the user's ratification of all four protocols, dated 2026-07-19; the reverse map is item 5 of the dual-path sanction at :189-191. Register entry D-095 records the sanctioned dual path itself at its ARCHITECTURE.md home. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-283 — Meta-finding: never learn keys, the lever is keychain structure - superseded by the joint estimator and the forms-from-theory rule

> - **Never learn keys; the lever is keychain structure (cadence precision).** Settled from both sides.

**In plain words.** A rejection of a learned key detector in favour of structural levers, cadence precision above all. Whichever reading was intended, the later explicit ratifications govern: the joint estimator infers the key inside a theory-declared generative form whose factor values are fitted once against ground truth, and its cadence factor carries the structural insight forward. This finding binds nothing the current design does.

**Why.** The supersession stands on dates and explicitness alone: D-001 (2026-07-17, ratified, adopted with measurement 2026-07-26) and D-096 (forms from theory, values fit once, never per-case tuned) are later, explicit, user-ratified decisions on the same subject. Ruled so that no future reader treats this as a live prohibition over the key axis (the risk that made OI-270 matter).

**Status.** SUPERSEDED BY D-001 and D-096 · date not stated · ratifier not stated

**Home.** `cowork_architecture_reassessment.md:107`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§4** — `## 4. Meta-findings to institutionalize (cross-cutting)` (heading at line 104). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Stated 2026-06-20 in cowork_architecture_reassessment.md §4 ('Meta-findings to institutionalize'); put to the user in §5 ('Ratify: …') with NO recorded answer (open_items/OI-270.md, the phase-1d wave's remainder). ★ RULED by the user 2026-08-02 (the OI-270 split, all four recommendations adopted): SUPERSEDED BY the named later ratified decisions — the governing status derives from the record's dates and explicitness, not from resolving the original statement's ambiguity. The second-partition read of the archives is instructed to flag anything refining these. ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

### D-285 — Meta-finding: embellishment is chord-first, never a richer vocabulary - absorbed by the emission design and the ornament-label increment

> - **Embellishment = chord-first** (segmentation + NCT post-process), never union re-derive / richer vocabulary.

**In plain words.** Ornamental tones are handled by classifying them against the committed chord - segmentation first, then a non-chord-tone post-process - never by widening the chord vocabulary until every embellishment is a chord. The ratified factorization’s emission carries exactly this shape (chord-member and non-chord-tone categories), and the ornament-label publication is its own ratified increment.

**Why.** Absorbed by ratified successors: the factorization’s emission categories (D-004’s ground-truth-derived compact vocabulary + the per-tone emission’s membership categories) and the OI-194 ornament-label increment. Ruled bindingly BEFORE the phase-3 family design so the struck-versus-sounding emission fix keeps non-chord-tone handling in the emission’s categories rather than solving its problems by vocabulary inflation.

**Status.** SUPERSEDED BY the ratified factorization emission design (D-004 and D-426, the OI-194 ornament-label increment) · date not stated · ratifier not stated

**Home.** `cowork_architecture_reassessment.md:110`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§4** — `## 4. Meta-findings to institutionalize (cross-cutting)` (heading at line 104). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Stated 2026-06-20 in cowork_architecture_reassessment.md §4 ('Meta-findings to institutionalize'); put to the user in §5 ('Ratify: …') with NO recorded answer (open_items/OI-270.md, the phase-1d wave's remainder). ★ RULED by the user 2026-08-02 (the OI-270 split, all four recommendations adopted): SUPERSEDED BY the named later ratified decisions — the governing status derives from the record's dates and explicitness, not from resolving the original statement's ambiguity. The second-partition read of the archives is instructed to flag anything refining these. ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched. ★ THE SECOND SUCCESSOR IS NAMED — D-426, by the user's ruling of 2026-08-07 (dispatch `cc_instruction_five_rulings.md` §0a R2). The `superseded_by` field named the second successor as an INCREMENT by its open-items row rather than by a register identifier, so no derivation could read its home and criterion C1 could not be discharged for that half of this entry's content (the finding is at `tools/audit/decisions/r1_superseded_reach.json`, whose D-285 record reported the gap as a NAMING gap rather than an absent successor). The user names D-426 — the decision that the ornament labels get their own increment, with the tracking row created at ruling time — as the recorded decision that carries it. The field formerly read, verbatim: `the ratified factorization emission design (D-004 and the OI-194 increment)` (#12). CONSEQUENCE, stated with the ruling rather than derived after it: D-426 is itself unhomed — its home document's strongest naming is a form the delegation bar excludes — so C1 is still defeated for this entry and the owed act is homing D-426, which is where D-642 puts it and which finish-line item 1 already carries.

### D-376 — The joint key-and-chord step was designed as a BOUNDED COUPLING over the two existing decoders, and the unified single-state alternative was REJECTED — the option later adopted as the production architecture

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> **Decision: (B) — a bounded coupling step.** Grounded, not by preference but by three binding constraints:
>
> 1. **#7 (adhere to layers) + #6 (no duplication).** L3 (`key/keymodesequence`) and L4 (`chord/chordslicedecoder`)
>    are **built as separate layers, each with its own decoder, carry, and confidence** `[code]`. Option (A)
>    discards both built decoders and re-lays the pipeline into one joint-state decoder — a rebuild of what is
>    built (#6 violation) and a re-layering (#7 violation). Raphael & Stoddard's single state is a *modeling*
>    choice `[research]` §3; the **recurring recipe** the literature actually prescribes (a **beam of (key, chord)
>    hypotheses** + a **key-transition prior** + the **chord re-decoded under alternative keys**, `[research]` §3)
>    is realizable in *either* factoring. We pick the factoring that fits the built layers — the bounded coupling
>    over the two existing decoders.
> 2. **Magnitude realism `[research]` §3.** The joint win is **qualitative, concentrated on the hard/coupled
>    cases** (the ~13.5% coupled core `[data]`; low single-digit points elsewhere). Collapsing the whole pipeline
>    into a joint state to serve a minority is disproportionate. A bounded coupling that **fires only on the
>    coupled minority** (the C3 trigger, §3) and is a **pass-through on the ~86.5% majority** is the proportionate
>    realization — and it keeps the majority path byte-identical (a #12 property: no information moved where no
>    coupling exists).
> 3. **The acyclicity / forward-only control-flow contract (§8 / §9-D7; L5 engagement §4.1 `[code]`).** The
>    architecture forbids a back-edge L3←L4; the only cross-layer recompute is the §8 **localized,
>    convergence-bounded, one-pass-closure** mechanism. Option (A) would not violate acyclicity (it has no
>    layers to cycle between), but (B) must be designed to respect it — and it does (§1.3).

**In plain words.** When the coupling of tonality and chord was designed, two shapes were on the table: one decision over a single combined state holding tonic, mode and chord together, or the two existing stages kept apart with a bounded coupling between them. The bounded coupling was chosen, for three stated reasons: the two stages are already built as separate decoders and the combined state would discard both and re-lay the pipeline; the gain is concentrated on a small hard minority, so re-laying the whole pipeline to serve it is disproportionate; and the coupling can be built forward-only, respecting the rule against a later stage reaching back into an earlier one. The step was afterwards shelved against measurement, and the option rejected here is the shape the production engine now has.

**Why.** Three constraints are given as the defense, and the record distinguishes them from preference: principles #6 and #7 (the combined state discards two built decoders and re-lays the pipeline); magnitude realism, citing the research grounding and the measured coupled minority of about 13.5 % of stretches, against which collapsing the whole pipeline is disproportionate; and the forward-only control-flow contract. The record also states what the published literature does and does not settle: the single combined state is a modeling choice, while the recipe the literature actually prescribes — a beam of tonality-and-chord hypotheses, a tonality-transition prior, and the chord re-decoded under alternative tonalities — is realizable in either factoring.

**Status.** SHELVED WITH EVIDENCE · decided 2026-07-07 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_joint_key_chord_design.md:87-106`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§1.1 The decision: a BOUNDED coupling step, NOT a unified `(key,chord)` hidden state”** — `### §1.1 The decision: a BOUNDED coupling step, NOT a unified `(key,chord)` hidden state` (heading at line 80). A delegation at cowork_engage_arc_plan.md:44 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_joint_key_chord_design.md` IN FULL. The step this decision places was shelved against measurement and that shelving is register entry **D-278** (user-ratified 2026-07-07, re-ratified 2026-08-02), so the placement is shelved with it; the document's own banner says it is retained as the record and that the step is off the build inventory. **Reported, not statused as a supersession:** the option this decision REJECTED — one decision over a combined tonality-and-chord state — is what **D-001** later adopts as the production architecture, and no record connects the two; the user ruled at D-278's ratification that the shelving does not bear on D-001, and the two objections raised here are answered elsewhere in the record (the decision-neutrality corollary answers the rebuild objection; the adoption measurement answers the magnitude objection). NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-449 — Factor granularity is fixed: the bass factor is evaluated per event, the missing-tone penalty per event of segment length, the emission per tone, and the boundary-family factors per boundary

> **Factor granularity is fixed, per factor.** The pitch emission is scored **per tone**. The **bass
> factor is evaluated per event** — each event's sounding bass judged against the segment's chord.
> The **missing-tone penalty is normalized per event of segment length**, so a segment missing its
> third pays in proportion to how long it fails to sound it. The **transition, entry and key-change
> factors stay per boundary**. *Why:* measured on a real corpus case, and the measurement is why the
> granularity is fixed at all — under per-segment bookkeeping a longer segment pays the bass and
> missing-tone terms once where a split pays them twice, so merging harvests a discount unrelated to
> the music, which is the classic semi-Markov length bias. On the case that exposed it the
> bookkeeping alone decided merge against split, against the ground truth; with the bass factor
> evaluated per event the remaining gap is small enough to ride two fittable values rather than the
> structure. The per-event bass form is not an invention: it is the published per-frame form of the
> work this factorization is grounded in.

**In plain words.** The scoring form is written as a term per segment, which left open whether each term is counted once for the whole segment or once for each event inside it. That is now fixed: the bass evidence is judged at every event against the segment's chord, a missing chord tone is charged in proportion to how long it fails to sound, each sounding pitch is judged on its own, and the terms that belong to a boundary stay at the boundary.

**Why.** Measured, on a real case, and the finding is why the amendment exists: under per-segment bookkeeping a longer segment pays the bass and missing-tone terms once where a split pays them twice, so merging harvests a discount unrelated to the music — the classic semi-Markov length bias. On `bwv10.7@36000` that bookkeeping alone decided merge-against-split by about 6.6 nats AGAINST the ground truth; with the bass factor evaluated per event the gap closes to 1.3 nats and the remainder rides two fittable values rather than the structure. The per-event bass form is not an invention — it is Ni's published per-frame form (the F9 derivation).

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:434-445`

**Provenance.** RATIFIED by the user 2026-07-19 — the document's own banner records that the §7 asks were granted in full, naming this as "the §4.1 granularity amendment (now incorporated in `cowork_joint_estimator_factorization.md` §2/§3 with dated marks)". Entered by the phase-1 reads wave 1 from the full read of `cowork_factorization_desk_simulation.md`. The amendment's incorporated home is the factorization specification, which this wave did NOT read (it is owed at reading order 32); the entry is homed where the ratification is recorded and the incorporation is not verified here. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The owner question this entry carried was that the joint estimator is specified in the document's OPENING BANNER rather than in a section a decision can be sited inside. The user ruled that `ARCHITECTURE.md` GAINS A DEDICATED JOINT-ESTIMATOR SECTION, and it does: the existing standing-rules block was CONVERTED into a headed section by adding a heading above it, with NO existing text moved and none reworded (the minimal structural act the dispatch's assumption A4 prefers). A second heading was added below the block to bound the section, because three unrelated preamble blocks follow it and would otherwise read as part of the estimator's specification; that too is an addition and moves nothing. This entry is written into a subsection of that new section, in the specification's own voice and with its defense, beside the four other decisions about what the decode counts. Assumption A1 discharged before writing: the destination exists and STATES RULES. FORMER HOME, PRESERVED (#12): `cowork_factorization_desk_simulation.md:492-498`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 485, "section": "## 4. Findings register (surprises recorded, diagnosed, with proposed dispositions)", "label": "§4", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Proposed specification amendment (a #17e
sharpening within the ratified structure, brought for ratification per #13/#22):** (a) the pitch
emission is per tone (already the ratified text); (b) the BASS factor is evaluated per event — each
event's sounding bass against the segment's chord — which is Ni's published per-frame form (F9), not a
new invention; (c) the missing-tone penalty is normalized per event of segment length (a segment
missing its third pays in proportion to how long it fails to sound it); (d) transition, entry, and
key-change factors remain per boundary (correct as written)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-450 — The key-signature and declared-mode prior conditions the INITIAL key state only, re-entering only at a notated signature change

> **The key-signature and declared-mode prior conditions the INITIAL key state ONLY.** What the
> written key signature and any declared major/minor say about the key sets the starting key state
> and is not applied again — **except at a notated mid-piece signature change**, which is new written
> evidence and re-anchors it. The alternative form, a persistent pull toward the signature at every
> step, is **rejected**. *Why:* traced and settled by desk simulation on a Dorian-notated opening and
> a genuinely modal piece. A persistent pull taxes every away-from-signature key at every segment,
> without bound, and it has no basis in the literature — the published work carries no signature
> prior at all; it also re-introduces, in soft form, the signature-pull bias an earlier measurement
> condemned, in exactly the accidental-free stretches where the prior should be silent. The
> initial-state form pays the tax once and lets the music govern thereafter.

**In plain words.** What the written key signature and any declared major/minor say about the key is used once, to set the starting key, and then not again — unless the score itself changes signature part way through, which is new written evidence and re-anchors it. The alternative, a pull toward the signature at every point, is rejected.

**Why.** Measured by trace and stated with the decision: a persistent pull taxes every away-from-signature key by roughly 1.7 to 2.0 nats per segment, growing without bound, with no basis in the literature — the published work carries no signature prior at all — and it re-introduces the signature-pull bias an earlier measurement condemned, in soft form, in exactly the accidental-free stretches where the prior should be silent. Two traces settle it (a Dorian-notated opening and a genuinely modal piece), and the initial-state form pays the tax once and lets the music govern thereafter.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:447-456`

**Provenance.** RATIFIED by the user 2026-07-19 — the document's banner records the §7 asks granted in full, naming "the §4.2 initial-state-only prior record (incorporated at §3.10)". Entered by the phase-1 reads wave 1. As with D-449 the incorporated home is the factorization specification, unread at this wave. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Same owner question and same answer as D-449 — the ruling record routes it to the joint-estimator section the same act created — and it is written there beside D-449, in the specification's own voice and with its defense. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_factorization_desk_simulation.md:506-512`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 485, "section": "## 4. Findings register (surprises recorded, diagnosed, with proposed dispositions)", "label": "§4", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**4.2 The §5a open question SETTLED by trace (S3, concurred by C5): the signature/declared-mode prior
conditions the INITIAL key state only,** re-entering only at a notated mid-piece signature change (the
OI-94(a) discharge moment). The persistent-pull variant imposes a linearly growing tax on
away-from-signature keys with no theory basis (F2: the literature has no signature prior at all) and
softly re-introduces the OI-174 signature-pull bias in exactly the accidental-free stretches where the
prior should be silent. Brought for ratification as the §7 record; the factorization doc §7 already
names this as settled-by-desk-sim." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-451 — A desk simulation's table values are provisional, enter no fit, and a verdict that would flip inside a provisional value's plausible range is reported as a near-tie, never as a win

>     **★ WHAT A DESK SIMULATION'S TABLE VALUES ARE, AND WHAT THEY MAY NEVER BECOME (user-ratified
>     2026-07-19).** Every table value a desk simulation under (c) uses is **PROVISIONAL** — declared
>     before use, each labeled with its provenance class, and hand-declared stand-ins whose only job

**In plain words.** When a mechanism is traced by hand, the numbers used are stand-ins declared up front whose only job is to let the mechanism be followed. None of them may become a fitted value later. And if a trace's answer would change had a stand-in been chosen differently within its believable range, the trace reports a near-tie and names the deciding cell rather than claiming a winner.

**Why.** Stated with the rule and visible in the traces that follow it: several verdicts are reported with their sensitive cells named rather than as wins, and the cells so named are carried forward to the capacity and pooling gate. Without the rule a hand-declared number would silently become an instrument, which is the defect the catalog names DT-2.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:100-102`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** The ground rules of `cowork_factorization_desk_simulation.md` §0, declared before any trace, in the document the user RATIFIED on 2026-07-19 (banner: the §7 asks granted in full, verdict included). Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the licensed homing wave, executing the user's ruling R2 of 2026-08-07, dispatch `cc_instruction_licensed_homing_and_oi344.md` §0a — the LICENSING class of finish-line item 1's re-home set, homed under the edit-surface licence the user ruled on the same date). Written into `CLAUDE.md` principle #17(c), as the rule stating what a desk simulation's table values are and what they may never become, in that section's own voice and with its defense. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. FORMER HOME, PRESERVED (#12): `cowork_factorization_desk_simulation.md:30-35`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `project-convention` entry (the register's own home rule): section "## 0. Ground rules (declared before any trace)", label "§0", verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "1. **All table values are PROVISIONAL** — declared here (§1) before use, each labeled with its\n   provenance class: the FORM is from the ratified specification and the derived forms in\n   `cowork_term_theory_grounding.md` §1 (F1–F10); the VALUES are hand-declared stand-ins whose only job\n   is to let the mechanism be traced. No value here survives into any fit; fitting happens only under\n   the OI-176/OI-177 gates. A verdict that would flip within the plausible range of a provisional value\n   is reported as a NEAR-TIE with the sensitive cell named — never as a win.". Provenance is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, its date and its ratifier where the record states one, and its defense.

### D-452 — Every desk-simulation trace runs at identity weights — the ratified ablation baseline — so the trace tests the structure and the tables, not the weighting

>     **★ EVERY DESK-SIMULATION TRACE RUNS AT IDENTITY WEIGHTS (user-ratified 2026-07-19).** A trace
>     under (c) runs the generative product with every weight at one — exactly the mandatory ablation
>     baseline the design already carries. The desk simulation therefore tests the structure and the

**In plain words.** Each hand trace is run with every weight set to one, which is the baseline the design already requires be measured. That way what the trace checks is whether the shape of the model and its tables behave, and not whether a weighting was chosen well.

**Why.** Stated with the rule: identity weights ARE the mandatory ablation baseline the ratified design already carries, so the choice imports no new premise, and running at anything else would confound a structural verdict with a weighting one.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:110-112`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** The ground rules of `cowork_factorization_desk_simulation.md` §0, in the document the user RATIFIED on 2026-07-19. Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ HOMED 2026-08-07 (CC, the licensed homing wave, executing the user's ruling R2 of 2026-08-07, dispatch `cc_instruction_licensed_homing_and_oi344.md` §0a — the LICENSING class of finish-line item 1's re-home set, homed under the edit-surface licence the user ruled on the same date). Written into `CLAUDE.md` principle #17(c), as the rule that every desk-simulation trace runs at identity weights, in that section's own voice and with its defense. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. FORMER HOME, PRESERVED (#12): `cowork_factorization_desk_simulation.md:36-38`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `project-convention` entry (the register's own home rule): section "## 0. Ground rules (declared before any trace)", label "§0", verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "2. **Identity weights.** Every trace runs the generative product (all `w = 1`) — exactly the ratified\n   mandatory ablation baseline. The desk simulation therefore tests the structure and the tables, not\n   the weight layer.". Provenance is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, its date and its ratifier where the record states one, and its defense.

### D-453 — The desk simulation's verdict: the ratified factorization passes nine of ten traces and no finding reopens the structure

> 1. **The verdict:** the ratified factorization passes nine of ten traces as specified; no finding
>    requires re-ratifying the STRUCTURE (variables, factors, decode).

**In plain words.** Ten cases were traced by hand against the agreed model. Nine behaved as the model says they should. The tenth exposed one thing the model had not settled — how finely each term is counted — and that was fixed by sharpening the model rather than by changing what the model is made of. So the variables, the factors and the decoding stay as ratified.

**Why.** This is the outcome of the desk-simulation stage of the premise gate (#17c) run on ten real cases, five constructed and five taken from the corpus with every fact verified at a cited committed source. The one surprise was surfaced as a stop and brought for ratification rather than built around (#13), which is the stage doing its job.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_factorization_desk_simulation.md:590-591`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§7** — `## 7. What ratification is asked for` (heading at line 588). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** RATIFIED by the user 2026-07-19 — the banner records the §7 asks granted in full, of which this verdict is the first. Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-524 — The joint state's mode axis is TWO modes — major and composite minor; modal and chromatic colour lives in the pitch emission, and the un-rounded reading is published

> **Mode vocabulary (user-ratified 2026-07-19).** The joint state's mode axis is **{major, minor}** —
> minor meaning the composite minor practice (natural/harmonic/melodic as one key with variable sixth and
> seventh degrees). **Modal and chromatic color is modeled in the pitch-emission factor**, not the state:
> the first build carries the minor-scale variants (raised sixth and seventh) only; church-mode variants
> (Dorian sixth, Mixolydian seventh, Phrygian second, …) enter later only through their own premise-ledger
> entries (#17); the dominant-family exotic scales are **excluded from the state space** (constrained-
> optimum ledger record: the 21-mode state space is excluded because its states are ungradable against any
> ground truth we possess — #19/#20 — and OI-174 measured them harming inference). **User's condition,
> part of the decision: the un-rounded reading is preserved and published.** The emission factor's
> modal-variant evidence is published as a derived fact on the output surface, so the presentation layer
> can show the end-user that a passage decoded as, say, D minor would — without the rounding to
> major/minor — be called D Dorian, and can choose whether/how to display that by user preference (the
> eventual preset ↔ mode-prior mapping is a presentation/preference concern, not an inference state).
> Inference states stay two-mode under every preset. This resolves the OI-174/OI-132/OI-147 mode-
> vocabulary question at the design level; the rows close when the build lands.

**In plain words.** The estimator's tonality has only two characters, major and minor, with minor meaning the ordinary minor practice whose sixth and seventh degrees vary. Everything more colourful — Dorian, Mixolydian, the altered scales — is handled as evidence about which notes are likely, not as a separate tonality to decide between. The finer reading is not thrown away: it is published, so the display can tell the user that a passage read as D minor would, unrounded, be called D Dorian.

**Why.** The exclusion is recorded as a constrained optimum with its reason: the larger mode vocabulary's states cannot be graded against any ground truth we hold (#19/#20) and were measured harming inference. The publication half is the user's own condition attached to the decision, and it is what keeps the reduction from being information loss (#12) — the rounding happens for inference, not in the record.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_joint_estimator_architecture.md:89-103`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5a** — `## 5a. Design decisions ratified (the design pass, 2026-07-19 →)` (heading at line 81). A delegation at ARCHITECTURE.md:3 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The first of the five design decisions the governing architecture document records as ratified at the design pass. It resolves the mode-vocabulary question the same document had listed as open, and the rows it settles close when the build lands. The grading convention that reduces an emitted exotic mode to its parent collection's minor key is **D-210**; the desk-simulation decisions that build on this state space are **D-449**…**D-453**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-525 — The fit is STAGED: the factor tables are counted from ground truth and frozen, and only a small vector of combination weights is fit discriminatively — with an all-weights-equal ablation arm that must be beaten

> **Fitting parameterization (user-ratified 2026-07-19).** The staged form: **the factor TABLES are fit
> generatively from ground-truth counts and frozen** (each table established on its own — the
> key-conditioned chord-transition table, the bass-note-given-chord-and-inversion table, the tone-category
> emission tables, the key-change table — every entry a musically meaningful probability, per the
> published forms); **the small vector of COMBINATION WEIGHTS over the factors is fit discriminatively by
> convex conditional likelihood** (the semi-Markov conditional-random-field objective with the logarithms
> of the frozen tables as features; L2 penalty; the OI-176 held-out gate and OI-177 capacity budget
> govern). **Mandatory ablation arm:** all-weights-equal-one IS the pure generative model, so the weight
> layer's contribution is measured on held-out data inside the same machinery, never assumed — its
> adoption is gated on winning that comparison. **Ledger entries attached to the decision:** (a) the
> staged ASSEMBLY is our synthesis (each stage established separately in the literature; the combination
> is an assumption with its own #17b prediction); (b) constrained-optimum record — the unconstrained
> alternative is the fully joint discriminative fit with rich free features (possibly a higher ceiling),
> excluded because fully joint weights sacrifice the modular diagnosability (#3/#19) the error-correction
> loop runs on; re-test if that constraint stops binding; (c) fit-scope declaration (the Noland &
> Sandler lesson): which components may be re-fit is declared before any fit — tables from counts, once,
> frozen; only the combination weights move; (d) the direct-metric few-weight search (the minimum-error-
> rate protocol with bootstrap confidence intervals) is the established fallback if the likelihood-fit
> weights measurably disagree with the reported metric.

**In plain words.** Each table of probabilities is counted from the annotated corpus and then frozen. On top of them sits a short list of weights saying how much each kind of evidence counts, and only those are trained. Because setting every weight to one is exactly the untrained model, the trained weights have to beat that on held-out music before they are adopted at all.

**Why.** The ablation arm is what makes the weight layer's contribution measured rather than assumed, and the document says so: all-weights-one IS the pure generative model, so the comparison runs inside the same machinery. The excluded alternative is recorded as a constrained optimum — a fully joint discriminative fit with rich free features may have a higher ceiling and is excluded because it sacrifices the modular diagnosability the error-correction loop depends on, to be re-tested if that constraint stops binding.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_joint_estimator_architecture.md:105-123`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5a** — `## 5a. Design decisions ratified (the design pass, 2026-07-19 →)` (heading at line 81). A delegation at ARCHITECTURE.md:3 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The second of the five ratified design decisions, recorded with four ledger entries attached: that the staged assembly is our own synthesis and carries its own prediction; the constrained-optimum record; the fit-scope declaration made before any fit; and the named fallback if the likelihood-fit weights disagree with the reported metric. The gates that govern it are **D-270** (held-out protocol) and **D-271** (capacity budget). The ablation baseline is the one every desk-simulation trace runs at, **D-452**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-526 — The joint state's chord axis is SCALE-DEGREE-VALUED — a Roman numeral relative to the state's own tonic and mode — and the chord symbol is a DERIVED fact published once

> **Chord state is scale-degree-valued (user-ratified 2026-07-19).** The joint state's chord axis is a
> **Roman numeral — scale degree, quality, inversion — relative to the state's tonic and mode** (the
> Raphael-Stoddard / Harasim structure). Consequences, all structural: (a) the tonic/degree coupling
> terms (the diatonic-root bonus, `buildChordResult`'s degree, Gate G-E's degree condition,
> `applyTonicPriorToSparseChord`, the segmenter's head-gap tonic prior — the gap map's group 1) dissolve
> by construction — a degree is key-relative by definition; (b) **transposition invariance**: the chord-
> transition table pools all keys' evidence (twelvefold counts per cell — the decisive capacity device on
> a 326-piece corpus); (c) the ground truth is natively degree-valued, so tables fit from counts with no
> conversion layer, and the OI-173 defect class (four inequivalent `diatonicToKey` definitions, two of
> `degree`) is never rebuilt. **The chord symbol (root pitch class, quality, bass) is a DERIVED fact,
> published once** (root = tonic + the degree's interval) — the robust stop's root metric is unchanged
> and every baseline column stays comparable. **Tonicization is applied-degree classes** (the secondary
> dominant V/x, applied leading-tone chords, and the standard chromatic classes — Neapolitan sixth,
> augmented-sixth chords — per the ground truth's own vocabulary; this also matches jazz analytical
> practice, where the secondary dominant, and later the substitute dominant and extended dominant chains,
> are applied-degree devices — jazz-specific classes enter only under the OI-7 jazz-ground-truth gate).
> **Excluded alternatives recorded:** root-valued chord state (forfeits transposition tying and
> structurally preserves the ad-hoc key coupling the audits condemned); momentary modulation for
> tonicization (fits Bach acceptably but shreds jazz tonicization chains into micro-keys and departs from
> the ground truth's labeling convention).

**In plain words.** The estimator decides chords as scale degrees within the tonality it is considering, not as absolute chord roots. The ordinary chord name is then worked out from the degree and published once. Two things follow by construction: the terms that used to couple a chord to a key dissolve, because a degree is key-relative already; and evidence from every key pools into the same table, which is what makes counting on a corpus of this size possible.

**Why.** Three grounded consequences are stated with the decision, and the excluded alternatives with theirs: a root-valued state forfeits the transposition pooling and structurally preserves the ad-hoc key coupling the audits condemned; treating tonicization as momentary modulation fits one repertoire acceptably but shreds jazz tonicization chains into micro-keys and departs from the ground truth's own labelling convention. The ground truth is natively degree-valued, so the tables are counted with no conversion layer and the defect class of several inequivalent degree definitions is never rebuilt.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_joint_estimator_architecture.md:125-144`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5a** — `## 5a. Design decisions ratified (the design pass, 2026-07-19 →)` (heading at line 81). A delegation at ARCHITECTURE.md:3 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The third of the five ratified design decisions. It is why the robust stop's root metric is unchanged and every published baseline column stays comparable — the root is derived, not abandoned. The published-once discipline it invokes is the fact-publication corollary (**D-100**). Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-527 — There is NO live non-chord-tone cleaning stage: each tone is emitted by category inside the one decode, conditioned on chord-independent melodic and metric covariates, and ornament labels are derived AFTER it

> **Non-chord-tone handling (user-ratified 2026-07-19).** **No live cleaning stage exists.** Non-chord
> tones live INSIDE the pitch-emission factor: each tone is emitted by category (chord member vs
> within-scale non-chord tone vs outside-scale tone — the Raphael-Stoddard structure), with the emission
> probability conditioned on **chord-independent melodic and metric covariates** — stepwise approach and
> departure, chromatic-neighbor motion, metric weakness, the tied-over/syncopated preparation (the
> figuration-feature forms Masada & Bunescu fit on chorales; every covariate computable without knowing
> the chord, so no circularity). Chord identity and tone status are decided together in the one decode
> (#12 — no ornament verdict is ever committed early). **Ornament labels (passing tone, neighbor tone,
> suspension, appoggiatura, pedal point) are derived AFTER the decode** from the committed chord by the
> standard definitions and published as a derived fact for the presentation layer — the same pattern as
> the modal-color publication. **Style adaptation is values-only:** the chord-tone boundary shift in jazz
> (tensions as chord members) is a VOCABULARY matter handled by the degree-valued quality classes; the
> changed ornamental/metric conventions (enclosures, anticipations) are covariate TABLE VALUES refit per
> preset — same structure, no per-style rule code; jazz-specific covariate additions enter only under the
> OI-7 jazz-ground-truth gate with their own ledger entries. **Establishment resource:** the BCMH
> reduction is the chorales with non-chord tones removed — aligning the 87 overlapping full-texture
> stems against their reductions yields empirically labeled chord-tone/ornament data for fitting and
> validating these emission tables (BCMH's declared instrument status applies). **Excluded alternatives
> recorded:** a live pre-cleaning stage (the published cleaners' ~28 % error rate would be hard-committed
> upstream, violating #12, and the suspension's chord-relative definition makes pre-cleaning circular);
> pure category emission without melodic covariates (discards the established voice-leading evidence —
> the strongest ornament discriminator).

**In plain words.** The estimator does not first decide which notes are decoration and then read the chord from what is left. Every sounding note is scored by what kind of tone it would be under the chord being considered, using only facts computable without knowing the chord — how it is approached and left, how weak its metrical position is, whether it is tied over. Chord and tone status are settled together, and the ornament names are worked out afterwards from the committed chord.

**Why.** The excluded alternatives carry the argument: a live pre-cleaning stage would hard-commit the published cleaners' error rate upstream, against #12, and the suspension's definition is chord-relative, which makes pre-cleaning circular; while pure category emission without the melodic covariates discards the established voice-leading evidence that is the strongest ornament discriminator. Style adaptation is values-only — the same table structure with re-counted values — so no per-style rule code enters.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_joint_estimator_architecture.md:146-167`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5a** — `## 5a. Design decisions ratified (the design pass, 2026-07-19 →)` (heading at line 81). A delegation at ARCHITECTURE.md:3 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The fourth of the five ratified design decisions. Its named establishment resource is the second chorale annotation set, whose declared instrument status applies — which ties it to **D-475** and `OPEN_ITEMS.md` OI-179: a consumer may not put that corpus under load while it stands unestablished. The deferred detection decision it supersedes in practice is **D-303**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-528 — The key signature and declared mode enter as a WEAK FITTED SOFT PRIOR with no conditional gate anywhere — the probability calculus delivers 'consult it only when unsure', and the hard declared-mode wall is formally retired

> **The key-signature and declared-mode prior (user-ratified 2026-07-19).** A **weak, fitted,
> transposition-invariant soft prior on (tonic, mode)** from the notated signature — a small categorical
> table (local-key tonic distance from the signature's relative pair on the circle of fifths, by mode)
> counted from ground truth; the declared mode, where the score carries one, is a second conditioning
> input with its own fitted strength. **No conditional gate and no threshold anywhere:** the user's
> intent — the signature consulted only where the analysis is otherwise unsure — is delivered by the
> probability calculus itself (a weak prior is negligible where the content likelihood is decisive and
> tips the scale only where the evidence is ambiguous), never by an "if uncertain" code path. Bach's
> modal notation practice (the Dorian chorale written one flat short) is handled statistically as
> measured mass one fifth away in minor — no special case. A mid-piece signature change re-anchors the
> prior (discharging the OI-94(a) deferral). **The signature-influence rate is measured by ablation and
> published at every fit** (the fraction of committed keys the signature factor changed), with the
> recorded expectation that it is SMALL — a large fitted weight or influence rate is a #3 finding to
> investigate, not to ship. **The declared-mode wall (the −7 hard penalty) is formally retired.**

**In plain words.** The written key signature is used as a gentle nudge whose strength is counted from the corpus, not as a rule and not behind an 'if the analysis is unsure' branch. A weak prior is negligible where the notes are decisive and tips the balance only where they are not, which is exactly the intended behaviour without any threshold. The old hard penalty for contradicting the declared mode is retired.

**Why.** Every alternative is excluded with its reason: a hard signature constraint is factually false three ways and is the known wall-defect pattern; no prior at all discards free information and is contradicted by the project's own measurement; and the literal 'consult only when uncertain' branch reintroduces the threshold gate the soft prior makes unnecessary. The composer's modal notation practice is handled statistically as measured mass one fifth away rather than as a special case, and the signature's influence rate is measured by ablation and published at every fit — with the recorded expectation that it is small and that a large one is a finding to investigate.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_joint_estimator_architecture.md:169-182`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5a** — `## 5a. Design decisions ratified (the design pass, 2026-07-19 →)` (heading at line 81). A delegation at ARCHITECTURE.md:3 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The fifth of the five ratified design decisions, and the one that discharges the mid-piece signature-change deferral. It is ledgered as OUR form, with the literature's absence of any signature prior explicitly cited. Whether the prior conditions the initial state only or acts as a persistent pull was deliberately left to the desk simulation, which settled it as **D-450**. The standing rule it must not contradict is **D-056** — notes always win. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-532 — The chord-transition table gains one pooling level that groups a secondary dominant's continuations by their RELATION to its target — restoring from counts the one behaviour that defines the chord class

> **The chord-transition table carries one pooling level for a secondary dominant's continuations,
> grouped by their RELATION to the target.** A secondary dominant's continuations are pooled across
> all targets as *resolves to the chord it is the dominant of* versus *moves elsewhere*, and the
> counting is re-run at that level. *Why:* as counted without it, every secondary dominant is too
> rare on its own to hold a row, so its continuations fall into the general chord-frequency list and
> the table reads the same probability for resolving to the target as for going anywhere else — it is
> blind to the one behaviour that defines the chord class. The defect was verified directly in the
> table and its cost measured in a checked passage, where the blindness taxed the correct reading.
> Two alternatives are excluded on stated grounds: leaving it to the weight layer cannot work,
> because a weight can only scale what a table says and cannot restore a distinction the table does
> not contain; and hand-setting a resolution probability would recreate exactly the class of
> unestablished constants the fit exists to eliminate. The pooling reuses the mechanism the table
> design already rests on — counting the same pattern across transpositions — so it adds no new kind
> of machinery (#6), and the counts are ample enough that the added cells satisfy the ratified
> capacity budget.

**In plain words.** As counted, every secondary dominant was too rare on its own to keep its own row, so all its continuations were merged into the general chord-frequency list. The consequence is that 'the dominant of X moving to X' and 'the dominant of X moving anywhere else' read the same probability — the table is blind to what makes the chord a secondary dominant at all. One extra grouping level, pooled across all targets, restores the distinction from real counts.

**Why.** The defect was verified directly in the table and its cost measured in one of the three checked passages, where the blindness taxed the correct reading. The fix is chosen against two alternatives with their reasons: leaving it to the weight layer cannot work, because a weight can only scale what a table says and cannot restore a distinction the table does not contain — which the ratified premise ledger states explicitly; and hand-setting a resolution probability would recreate the class of unestablished constants the whole fitting effort exists to eliminate.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `ARCHITECTURE.md:458-472`

**Provenance.** Finding 1 of the sensitive-cell probe, ratified in the banner as option 1a. It amends a pooling ladder the user had already ratified, which is why it was brought for re-ratification rather than done. The capacity rule it must still satisfy is **D-271**; the counts are ample enough that the new cells pass it. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed to the joint-estimator section the same act created — the section the pooling ladder this amends belongs to — in the specification's own voice, with its defense and with both excluded alternatives (leave it to the weight layer; hand-set a resolution probability) recorded as the record states them. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_sensitive_cell_probe.md:121-129`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 106, "section": "### Finding 1 (structural). The chord-progression table cannot express that a secondary dominant resolves to its target.", "label": "“Finding 1”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Option 1a — add one pooling level that groups secondary-dominant progressions by their RELATION
to the target (resolves to the chord it is the dominant of / moves elsewhere), pooled across all
targets; then re-run the counting.** Pros: restores the defining regularity from real counts, with
no hand-chosen number (guiding principle 1, fact-based only); reuses the pooling idea the table
design already rests on — counting the same pattern across transpositions — so no new kind of
machinery (principle 6, one path per concern); the counts are ample, so the two or three new cells
pass the reliability rule easily (the ratified capacity budget stays satisfied). Cons: it amends a
pooling ladder you ratified, so it needs your re-ratification (that is why it is brought here and
was not just done); it adds a small number of parameters." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-533 — A continuation too rare to have its own stored probability is scored by dividing the row's leftover in PROPORTION to each chord's overall frequency — never evenly, and never as impossible

> **A continuation too rare to have its own stored probability is scored by dividing the row's
> leftover in PROPORTION to each chord's overall frequency in that mode — never evenly, and never as
> impossible.** Each row of the transition table ends in one pooled probability covering everything
> too rare to store; when the decode meets a specific rare continuation it turns that pooled value
> into a number for that continuation in proportion to how common the chord is generally. *Why:* it
> is the standard construction in published back-off models of sequences (#1), and it uses
> information already held — a common chord is genuinely a likelier unseen continuation than a rare
> one (#12). Both alternatives are excluded on facts: dividing evenly asserts that a rare and a
> common chord are equally likely, which the corpus counts contradict; and treating an unseen
> continuation as impossible is factually wrong on a corpus of this size and technically fatal, since
> a zero destroys any path through it.

**In plain words.** Each row of the transition table ends with one pooled probability covering everything too rare to store on its own. When the decoder meets one specific rare continuation it must turn that pooled value into a number for that continuation. It does so in proportion to how common the chord is generally.

**Why.** The chosen rule is the standard construction in published back-off models of sequences, and it uses information already held — a common chord is genuinely a likelier unseen continuation than a rare one (#12). Both alternatives are excluded on facts: dividing evenly asserts that a rare and a common chord are equally likely, which the corpus counts contradict; and treating unseen continuations as impossible is factually wrong on a corpus of this size and technically fatal, because a zero destroys any path through it.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `ARCHITECTURE.md:474-484`

**Provenance.** Finding 2 of the probe, ratified as option 2a, and recorded as one sentence owed to the build specification. It was a genuine gap rather than an ambiguity: no document defined it, and the probe proceeded by computing every verdict under both provisional readings and reporting both. `CLAUDE.md` gate block (A) names this rule as part of the production decoder's configuration. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed to the joint-estimator section the same act created, beside D-532, in the specification's own voice, with its defense and with both excluded alternatives (divide evenly; treat an unseen continuation as impossible) recorded as the record states them. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_sensitive_cell_probe.md:155-159`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 147, "section": "### Finding 2. No document defines how to score a progression that sits inside a row's leftover probability.", "label": "“Finding 2. No document defines how to score a progression that sits inside a row's leftover probability.”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Option 2a — divide the leftover in proportion to each chord's overall frequency in that mode.**
Pros: uses information we already hold — a common chord is genuinely a likelier unseen continuation
than a rare one (principle 12, no information loss); this is the standard construction in published
back-off models of sequences (principle 1, established method). Cons: none of substance; a little
more arithmetic per lookup." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-534 — The penalty for a chord tone that never sounds is COUNTED per chord factor — root, third, fifth, seventh — replacing one invented blanket number; the per-factor asymmetry then comes free

> **The penalty for a chord tone that never sounds is COUNTED PER CHORD FACTOR — root, third, fifth,
> seventh — and not carried as one blanket value.** Across every humanly labelled chord segment in
> the ground-truth corpus, the fraction in which each of the chord's own factors actually sounds is
> counted, per chord family (triad versus seventh chord). *Why:* the data is already on disk — the
> labelled segments record which notes sound, and the label itself names the chord's factors — so the
> counting is direct rather than inferred, which replaces a value invented for a worked example with
> an established one (#19). The musical point is what makes per-factor counting the right shape: the
> factors are not symmetric and the counts encode that automatically — a seventh is what earns a
> seventh-chord label, so a silent seventh is near-prohibitive; the fifth is the factor four-part
> writing routinely omits, so its penalty is mild; the third sits between. One blanket number cannot
> express any of that, and the invented value demonstrably carried load — a checked passage's margin
> moves with it. **The scope limit rides with the values and is part of the decision:** these are
> Bach-chorale counts, no jazz values can be counted because no jazz ground truth exists, and that
> limit stays declared on the artifact.

**In plain words.** Judging a candidate chord means weighing notes that sound but do not belong to it AND chord notes that never sound at all. The second direction was answered by a number invented for a paper walkthrough. It is replaced by counting, for every humanly labelled chord segment in the corpus, how often each of the chord's own factors actually sounds.

**Why.** The counting is direct because the data is already on disk, and the musical point is the user's: the factors are not symmetric and the counts encode that automatically — a seventh is what earns a seventh-chord label, so a silent seventh will be near-prohibitive; the fifth is the factor four-part writing routinely omits, so its penalty will be mild; the third sits between. One invented blanket number cannot express any of that. The invented value demonstrably carried load: one checked passage's margin moves with it.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `ARCHITECTURE.md:486-499`

**Provenance.** Finding 3 of the probe, ratified as option 3a, with the user's per-factor sharpening incorporated. The scope limit stated with it applies to EVERY table in this fit and is part of the decision: these are Bach-chorale values, no jazz values can be counted because no jazz ground truth exists, and the limit stays declared on the artifact — the standing position **D-422**/`OPEN_ITEMS.md` OI-7. The specification requiring the penalty and charging it per event of segment length is **D-449**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Routed to the joint-estimator section the same act created, in the specification's own voice and with its defense. The scope limit the record states with the decision — Bach-chorale counts, no jazz values countable, the limit declared on the artifact — is carried into the home text as part of the decision rather than dropped. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `cowork_sensitive_cell_probe.md:188-195`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 171, "section": "### Finding 3. The penalty for a chord tone that fails to sound is still a placeholder, not a counted value.", "label": "“Finding 3. The penalty for a chord tone that fails to sound is still a placeholder, not a counted value.”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Option 3a — count it, from data already on disk.** The note-extraction work committed earlier
today recorded, for every one of the ~18,000 humanly-labeled chord segments in the 326 chorales,
which notes sound in it; and the label itself names the chord's factors (root, third, fifth, and
seventh where the label is a seventh chord). So the counting is direct: across all segments
labeled with a triad or seventh chord, in what fraction does the ROOT actually sound among the
segment's notes? In what fraction the THIRD? The FIFTH? The SEVENTH? Four frequencies per chord
family (triad versus seventh chord — at most a dozen numbers), each backed by thousands of
observations in THIS corpus." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-535 — The checking stage's verdict: the real counted tables overturn no desk-simulation verdict, but margins moved in both directions and one margin expectation was plainly wrong

> Across the three passages, no desk-simulation verdict is overturned by the real counted values, but
> margins moved by 1.5–3.5 (log difference) in both directions, and one margin expectation was
> plainly wrong. Catching exactly this — before any code exists — is what this checking stage is for.

**In plain words.** The three passages whose paper outcomes depended most on placeholder numbers were recomputed with the real counted ones. Every verdict held. The margins did not: they moved appreciably in both directions, and one prediction about a margin was simply wrong.

**Why.** The value of the result is stated with it: catching exactly this before any code exists is what the checking stage is for. The expectations were written down before any number was looked up, which is what makes a wrong expectation detectable as one rather than absorbed.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_sensitive_cell_probe.md:246-248`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“For the record”** — `### For the record (no decision needed)` (heading at line 244). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** The probe's own summary, and the discharge of item 4 of the ratified capacity protocol — recompute the value-dependent desk-simulation passages with the real tables before building. The desk simulation it checks is **D-453**; the provisional-value rule that made the check owed in the first place is **D-451**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-565 — Exact score ties in the decode are real and are broken by a declared TOTAL ORDER on paths, implemented identically in every decoder — no epsilon, no platform dependence

> **The tie-break rule (user-ratified 2026-07-20 at the C++ module build's parity finding):** exact
> score ties between candidate decodes are real (proven at 8 corpus pieces — equal-score
> segmentations differing by one boundary on repeated-chord runs) and, unbroken, they make the
> committed output depend on the platform's floating-point library — unacceptable for the
> diff-based adoption measurement and regression stops (#16, reproducibility). Equal-score
> candidates therefore resolve by a declared TOTAL order, implemented identically in every decoder
> of this specification: fewer segments first; then the earliest boundary-tick sequence
> (lexicographic); then the canonical class-key order of the state sequence. No epsilon, no
> platform dependence — a pure order on paths.

**In plain words.** Two different readings of a piece can come out exactly equal, and this happens in real music. Left unresolved, which one the program commits to would depend on the machine's floating-point library. So ties are settled by a fixed rule applied in the same way everywhere: prefer fewer segments; if still tied, prefer the earlier sequence of boundary positions; if still tied, prefer the canonical ordering of the states.

**Why.** Measured, not assumed: exact ties were proven at eight corpus pieces, equal-score segmentations differing by one boundary on runs of a repeated chord. The consequence is stated with the rule — an unbroken tie makes the committed output platform-dependent, which is unacceptable for the difference-based adoption measurement and for the regression stops (#16, reproducibility). A tolerance would not fix it; only a total order on paths does.

**Status.** LIVE · decided 2026-07-20 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_joint_estimator_factorization.md:149-157`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§5** — `## 5. The decode` (heading at line 147). A delegation at ARCHITECTURE.md:276 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** `cowork_joint_estimator_factorization.md` §5, the user-ratified structure-design specification of 2026-07-19; this clause is marked *user-ratified 2026-07-20 at the C++ module build's parity finding*, so it entered the specification a day after the structure was ratified and on a measurement made during the build. Read in full by READ WAVE 4, 2026-08-04.

