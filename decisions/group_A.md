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

**Home.** `ARCHITECTURE.md:271-272`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:15-26, the governing architecture decision banner (user-ratified 2026-07-17), which tracks work and is not a specification home. OPEN_ITEMS OI-237 closes on this move

### D-097 — Held-out evaluation and a capacity budget are declared before any fit

> **(b) The held-out split and the capacity budget are declared BEFORE any value is fit, and the headline
> number is the held-out one.** The ratified protocol is five-fold cross-validation grouped by the shared

**In plain words.** Before the estimator's numbers are learned, we say in advance which music will be held back to test them on, and how many numbers we are allowed to learn at all. The headline number is always the one measured on the held-back music.

**Why.** Stated constraint, `CLAUDE.md` #20: no value is graded on data that helped fit it, so the split and the capacity budget are declared BEFORE fitting and the headline claim is the held-out figure; a fitted-and-self-measured number is not established (#19). The ratified protocols are open_items/OI-176 (5-fold cross-validation grouped by ground-truth file) and OI-177 (parameter inventory, cell own-estimate only at count >= 20, <= 12 weights).

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Home.** `ARCHITECTURE.md:280-281`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:123 (open_items/OI-176 and OI-177, PROTOCOL RATIFIED 2026-07-19, protocols in `cowork_prefit_gates.md`). The standing principle is CLAUDE.md #20. OPEN_ITEMS OI-237 closes on this move

### D-098 — The exact-decode reserve - the declared prune was never adopted

> **(c) The decode is EXACT; the declared reserve prune was never adopted, and what the decoder does narrow
> has no specified form.** Exact semi-Markov Viterbi over the joint state is the ratified search. A prune was

**In plain words.** The estimator was meant to be allowed to narrow its search when that gets too slow. The narrowing rule that was specified turned out to cost more than it saved, so the estimator still searches exactly - and how it actually narrows in practice was never specified.

**Why.** Stated constraint, `cowork_joint_estimator_factorization.md:170-173`: exact decode is expected tractable at chorale-scale event counts, and the reserve prune is an inference technique requiring its own established-loss measurement, never a silent heuristic. What the decoder actually prunes has no recorded derivation at all (open_items/OI-226).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:294-295`

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:211 (open_items/OI-188, OPEN - 'bounds every ceiling claim'); the admission rule actually in production still has no ratified basis (open_items/OI-226). OPEN_ITEMS OI-237 closes on this move

### D-114 — The decoder commits its best path; there is no abstention on the key axis

> **(d) On the key axis the decoder commits its maximum-a-posteriori path; it never abstains.** The estimator
> always names a key for every committed segment, so the abstention counter the regression stop reads is

**In plain words.** The joint estimator always names a key. It never declines to answer on the key axis, so the abstention counter is always zero.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `ARCHITECTURE.md:308-309`

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

**Status.** SUPERSEDED BY the ratified factorization emission design (D-004 and the OI-194 increment) · date not stated · ratifier not stated

**Home.** `cowork_architecture_reassessment.md:110`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§4** — `## 4. Meta-findings to institutionalize (cross-cutting)` (heading at line 104). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `contract-home` to `gap`; the former class is kept here rather than overwritten (#12).

**Provenance.** Stated 2026-06-20 in cowork_architecture_reassessment.md §4 ('Meta-findings to institutionalize'); put to the user in §5 ('Ratify: …') with NO recorded answer (open_items/OI-270.md, the phase-1d wave's remainder). ★ RULED by the user 2026-08-02 (the OI-270 split, all four recommendations adopted): SUPERSEDED BY the named later ratified decisions — the governing status derives from the record's dates and explicitness, not from resolving the original statement's ambiguity. The second-partition read of the archives is instructed to flag anything refining these. ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched.

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

**Home.** `cowork_joint_key_chord_design.md:77-96`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§1.1 The decision: a BOUNDED coupling step, NOT a unified `(key,chord)` hidden state”** — `### §1.1 The decision: a BOUNDED coupling step, NOT a unified `(key,chord)` hidden state` (heading at line 70). A delegation at cowork_engage_arc_plan.md:44 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_joint_key_chord_design.md` IN FULL. The step this decision places was shelved against measurement and that shelving is register entry **D-278** (user-ratified 2026-07-07, re-ratified 2026-08-02), so the placement is shelved with it; the document's own banner says it is retained as the record and that the step is off the build inventory. **Reported, not statused as a supersession:** the option this decision REJECTED — one decision over a combined tonality-and-chord state — is what **D-001** later adopts as the production architecture, and no record connects the two; the user ruled at D-278's ratification that the shelving does not bear on D-001, and the two objections raised here are answered elsewhere in the record (the decision-neutrality corollary answers the rebuild objection; the adoption measurement answers the magnitude objection). NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-379 — Whether an alternative tonality would change the chord CANNOT be measured without re-deciding under it — the exact coupled-case condition is not computable read-only, which is why it stayed unmeasured

> **(b) — the chord actually flips — computed BY the step's own per-key re-decode (§2.2).** This is the exact
>   condition, and it is **not pre-computable read-only** — you can only know the winner flips under a carried key
>   by *re-decoding under it*. This is precisely why C3 was found "un-computable read-only"
>   (`cc_engage_c3_measurement_report.md` §2.3): (b) IS the owed build. In the engaged step it is computed on the
>   pre-filtered (a)∧(a′) candidate set, and the step **commits a coupled (re-ranked) decision only where (b)
>   holds** (the winner root differs across the carried keys); where (b) is false the re-decode agrees with the
>   L3-argmax decode and the step passes through.

**In plain words.** The population that a tonality-and-chord coupling would actually help is the set of places where naming a different tonality would change the chord. There is no way to identify that set by inspection: the only way to know the chord changes under an alternative tonality is to re-decide it under that tonality. So the exact condition cannot be measured before the re-decision exists, and every number quoted for it before then is a structural stand-in, not the quantity itself.

**Why.** Established by the attempt: the measurement report that went looking for this population found it computable nowhere, and the record names that finding as the reason. The consequence is designed around rather than assumed away — a cheap two-stage filter narrows the candidates first, the exact condition is computed only on those, and the coupled decision is committed only where it holds.

**Status.** LIVE · decided 2026-07-07 · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_joint_key_chord_design.md:266-272`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§3.1 The trigger, grounded in C3”** — `### §3.1 The trigger, grounded in C3` (heading at line 249). A delegation at cowork_engage_arc_plan.md:44 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_joint_key_chord_design.md` IN FULL. The step the document designs is shelved (**D-278**); this statement is about what is and is not measurable, and stands independently of it — the same document records the shelving probe's own fire-rate as a structural proxy rather than the exact condition. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

### D-449 — Factor granularity is fixed: the bass factor is evaluated per event, the missing-tone penalty per event of segment length, the emission per tone, and the boundary-family factors per boundary

> **Proposed specification amendment (a #17e
> sharpening within the ratified structure, brought for ratification per #13/#22):** (a) the pitch
> emission is per tone (already the ratified text); (b) the BASS factor is evaluated per event — each
> event's sounding bass against the segment's chord — which is Ni's published per-frame form (F9), not a
> new invention; (c) the missing-tone penalty is normalized per event of segment length (a segment
> missing its third pays in proportion to how long it fails to sound it); (d) transition, entry, and
> key-change factors remain per boundary (correct as written).

**In plain words.** The scoring form is written as a term per segment, which left open whether each term is counted once for the whole segment or once for each event inside it. That is now fixed: the bass evidence is judged at every event against the segment's chord, a missing chord tone is charged in proportion to how long it fails to sound, each sounding pitch is judged on its own, and the terms that belong to a boundary stay at the boundary.

**Why.** Measured, on a real case, and the finding is why the amendment exists: under per-segment bookkeeping a longer segment pays the bass and missing-tone terms once where a split pays them twice, so merging harvests a discount unrelated to the music — the classic semi-Markov length bias. On `bwv10.7@36000` that bookkeeping alone decided merge-against-split by about 6.6 nats AGAINST the ground truth; with the bass factor evaluated per event the gap closes to 1.3 nats and the remainder rides two fittable values rather than the structure. The per-event bass form is not an invention — it is Ni's published per-frame form (the F9 derivation).

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_factorization_desk_simulation.md:492-498`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** RATIFIED by the user 2026-07-19 — the document's own banner records that the §7 asks were granted in full, naming this as "the §4.1 granularity amendment (now incorporated in `cowork_joint_estimator_factorization.md` §2/§3 with dated marks)". Entered by the phase-1 reads wave 1 from the full read of `cowork_factorization_desk_simulation.md`. The amendment's incorporated home is the factorization specification, which this wave did NOT read (it is owed at reading order 32); the entry is homed where the ratification is recorded and the incorporation is not verified here. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-450 — The key-signature and declared-mode prior conditions the INITIAL key state only, re-entering only at a notated signature change

> **4.2 The §5a open question SETTLED by trace (S3, concurred by C5): the signature/declared-mode prior
> conditions the INITIAL key state only,** re-entering only at a notated mid-piece signature change (the
> OI-94(a) discharge moment). The persistent-pull variant imposes a linearly growing tax on
> away-from-signature keys with no theory basis (F2: the literature has no signature prior at all) and
> softly re-introduces the OI-174 signature-pull bias in exactly the accidental-free stretches where the
> prior should be silent. Brought for ratification as the §7 record; the factorization doc §7 already
> names this as settled-by-desk-sim.

**In plain words.** What the written key signature and any declared major/minor say about the key is used once, to set the starting key, and then not again — unless the score itself changes signature part way through, which is new written evidence and re-anchors it. The alternative, a pull toward the signature at every point, is rejected.

**Why.** Measured by trace and stated with the decision: a persistent pull taxes every away-from-signature key by roughly 1.7 to 2.0 nats per segment, growing without bound, with no basis in the literature — the published work carries no signature prior at all — and it re-introduces the signature-pull bias an earlier measurement condemned, in soft form, in exactly the accidental-free stretches where the prior should be silent. Two traces settle it (a Dorian-notated opening and a genuinely modal piece), and the initial-state form pays the tax once and lets the music govern thereafter.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_factorization_desk_simulation.md:506-512`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** RATIFIED by the user 2026-07-19 — the document's banner records the §7 asks granted in full, naming "the §4.2 initial-state-only prior record (incorporated at §3.10)". Entered by the phase-1 reads wave 1. As with D-449 the incorporated home is the factorization specification, unread at this wave. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-451 — A desk simulation's table values are provisional, enter no fit, and a verdict that would flip inside a provisional value's plausible range is reported as a near-tie, never as a win

> 1. **All table values are PROVISIONAL** — declared here (§1) before use, each labeled with its
>    provenance class: the FORM is from the ratified specification and the derived forms in
>    `cowork_term_theory_grounding.md` §1 (F1–F10); the VALUES are hand-declared stand-ins whose only job
>    is to let the mechanism be traced. No value here survives into any fit; fitting happens only under
>    the OI-176/OI-177 gates. A verdict that would flip within the plausible range of a provisional value
>    is reported as a NEAR-TIE with the sensitive cell named — never as a win.

**In plain words.** When a mechanism is traced by hand, the numbers used are stand-ins declared up front whose only job is to let the mechanism be followed. None of them may become a fitted value later. And if a trace's answer would change had a stand-in been chosen differently within its believable range, the trace reports a near-tie and names the deciding cell rather than claiming a winner.

**Why.** Stated with the rule and visible in the traces that follow it: several verdicts are reported with their sensitive cells named rather than as wins, and the cells so named are carried forward to the capacity and pooling gate. Without the rule a hand-declared number would silently become an instrument, which is the defect the catalog names DT-2.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_factorization_desk_simulation.md:30-35`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** The ground rules of `cowork_factorization_desk_simulation.md` §0, declared before any trace, in the document the user RATIFIED on 2026-07-19 (banner: the §7 asks granted in full, verdict included). Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-452 — Every desk-simulation trace runs at identity weights — the ratified ablation baseline — so the trace tests the structure and the tables, not the weighting

> 2. **Identity weights.** Every trace runs the generative product (all `w = 1`) — exactly the ratified
>    mandatory ablation baseline. The desk simulation therefore tests the structure and the tables, not
>    the weight layer.

**In plain words.** Each hand trace is run with every weight set to one, which is the baseline the design already requires be measured. That way what the trace checks is whether the shape of the model and its tables behave, and not whether a weighting was chosen well.

**Why.** Stated with the rule: identity weights ARE the mandatory ablation baseline the ratified design already carries, so the choice imports no new premise, and running at anything else would confound a structural verdict with a weighting one.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_factorization_desk_simulation.md:36-38`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** The ground rules of `cowork_factorization_desk_simulation.md` §0, in the document the user RATIFIED on 2026-07-19. Entered by the phase-1 reads wave 1. ★ RATIFIED (user, 2026-08-04, the phase-1z ratification queue — the twenty-eight READ WAVE 1 entries ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated'. The ratification confirms that the register records the decision correctly; it is not a judgment that the decision is good. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-453 — The desk simulation's verdict: the ratified factorization passes nine of ten traces and no finding reopens the structure

> 1. **The verdict:** the ratified factorization passes nine of ten traces as specified; no finding
>    requires re-ratifying the STRUCTURE (variables, factors, decode).

**In plain words.** Ten cases were traced by hand against the agreed model. Nine behaved as the model says they should. The tenth exposed one thing the model had not settled — how finely each term is counted — and that was fixed by sharpening the model rather than by changing what the model is made of. So the variables, the factors and the decoding stay as ratified.

**Why.** This is the outcome of the desk-simulation stage of the premise gate (#17c) run on ten real cases, five constructed and five taken from the corpus with every fact verified at a cited committed source. The one surprise was surfaced as a stop and brought for ratification rather than built around (#13), which is the stage doing its job.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_factorization_desk_simulation.md:590-591`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

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

**Home.** `cowork_joint_estimator_architecture.md:89-103`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

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

**Home.** `cowork_joint_estimator_architecture.md:105-123`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

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

**Home.** `cowork_joint_estimator_architecture.md:125-144`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

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

**Home.** `cowork_joint_estimator_architecture.md:146-167`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

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

**Home.** `cowork_joint_estimator_architecture.md:169-182`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** The fifth of the five ratified design decisions, and the one that discharges the mid-piece signature-change deferral. It is ledgered as OUR form, with the literature's absence of any signature prior explicitly cited. Whether the prior conditions the initial state only or acts as a persistent pull was deliberately left to the desk simulation, which settled it as **D-450**. The standing rule it must not contradict is **D-056** — notes always win. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-529 — The joint architecture's expected win is ASYMMETRIC — large on key and mode, modest on chord root — and the written predictions must say so, because a large root claim would itself be a surprise

> **Reservation 1 — the joint win is asymmetric (grounding doc §2b/§2c), and the predictions must say so.**
> Ni et al.: key ~77→84 %, chord +≈1 pp. Wu et al.: key +3.5 pp, chord ≈flat. RNBERT: explicit joint-decoding
> machinery gave a small degradation. A is the established route to **mode/key** precision; on the **chord
> root** it buys coherence more than accuracy. The root-agree residual (~34 %) is more plausibly dominated by
> emission quality, segmentation, and GT-granularity noise than by missing coupling. The #17b written
> predictions for A's adoption must reflect this asymmetry — large movement expected on the key columns,
> modest on root; a large root claim would itself be a surprise (#3).

**In plain words.** The published results this architecture is grounded in improve tonality substantially and chord identity barely. The predictions written before its adoption must reflect that. If the chord-root number moved a lot, that would be a warning rather than a success.

**Why.** Read off the primary sources rather than hoped for: two of the three cited studies report a large key gain with a flat or near-flat chord gain, and the third records that explicit joint-decoding machinery gave a small degradation. The document draws the further consequence for our own residual — the root disagreement is more plausibly dominated by emission quality, segmentation and ground-truth granularity than by missing coupling.

**Status.** LIVE · decided 2026-07-18 · ratifier not stated

**Home.** `cowork_joint_estimator_architecture.md:200-206`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** The first of two reservations Cowork recorded at the user's request after the architecture ratification, as design-pass input. It is #3 applied in advance: the shape of the expected movement is written down so that an unexpected shape is recognisable as a failure of the premises rather than celebrated. The adoption measurement it governs is the OI-178 re-baseline recorded in `CLAUDE.md` gate block (A). Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-530 — The joint architecture is a CONSTRAINED optimum, not a global one: the learned shared-representation models measure better and are excluded because they are un-establishable and undiagnosable

> **Reservation 2 — A is a constrained optimum, not a global one (stated for honesty of the record).** On
> pure measured precision the published state of the art for symbolic Roman-numeral analysis is the learned
> shared-representation models (AugmentedNet, RNBERT, AnalysisGNN — grounding doc §2c), trained on the same
> DCML corpora used here as ground truth, so "data we lack" is only partially true. A is chosen because those
> models are un-establishable and undiagnosable under #1/#18/#19 — and because their absolute RN accuracy
> (~45–50 %) leaves the gap plausibly small on this domain. The decision stands; its basis is the
> methodology, not a claim that A out-measures the learned systems.

**In plain words.** On measured accuracy alone the best published systems for this task are learned models trained on the same annotated corpora we grade against. They are not chosen. The reason is that they cannot be established or diagnosed under this project's own rules, not that they perform worse.

**Why.** Stated for honesty of the record, with the counter-argument to our own earlier justification included: those models are trained on the very corpora used here as ground truth, so 'data we lack' is only partially true. The remaining ground for the choice is the methodology — #1, #18 and #19 — together with the observation that their absolute accuracy leaves the gap plausibly small on this domain.

**Status.** LIVE · decided 2026-07-18 · ratifier not stated

**Home.** `cowork_joint_estimator_architecture.md:208-214`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** The second recorded reservation, and an instance of the standing ledger corollary to #17: where a design is chosen for methodology-compliance rather than raw measured performance, the record names the unconstrained best known alternative and why it is excluded, so a future reader can re-test whether the constraint still binds. The same fork was ruled on measured evidence a month earlier as **D-531**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-532 — The chord-transition table gains one pooling level that groups a secondary dominant's continuations by their RELATION to its target — restoring from counts the one behaviour that defines the chord class

> **Option 1a — add one pooling level that groups secondary-dominant progressions by their RELATION
> to the target (resolves to the chord it is the dominant of / moves elsewhere), pooled across all
> targets; then re-run the counting.** Pros: restores the defining regularity from real counts, with
> no hand-chosen number (guiding principle 1, fact-based only); reuses the pooling idea the table
> design already rests on — counting the same pattern across transpositions — so no new kind of
> machinery (principle 6, one path per concern); the counts are ample, so the two or three new cells
> pass the reliability rule easily (the ratified capacity budget stays satisfied). Cons: it amends a
> pooling ladder you ratified, so it needs your re-ratification (that is why it is brought here and
> was not just done); it adds a small number of parameters.

**In plain words.** As counted, every secondary dominant was too rare on its own to keep its own row, so all its continuations were merged into the general chord-frequency list. The consequence is that 'the dominant of X moving to X' and 'the dominant of X moving anywhere else' read the same probability — the table is blind to what makes the chord a secondary dominant at all. One extra grouping level, pooled across all targets, restores the distinction from real counts.

**Why.** The defect was verified directly in the table and its cost measured in one of the three checked passages, where the blindness taxed the correct reading. The fix is chosen against two alternatives with their reasons: leaving it to the weight layer cannot work, because a weight can only scale what a table says and cannot restore a distinction the table does not contain — which the ratified premise ledger states explicitly; and hand-setting a resolution probability would recreate the class of unestablished constants the whole fitting effort exists to eliminate.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_sensitive_cell_probe.md:121-129`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Finding 1 of the sensitive-cell probe, ratified in the banner as option 1a. It amends a pooling ladder the user had already ratified, which is why it was brought for re-ratification rather than done. The capacity rule it must still satisfy is **D-271**; the counts are ample enough that the new cells pass it. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-533 — A continuation too rare to have its own stored probability is scored by dividing the row's leftover in PROPORTION to each chord's overall frequency — never evenly, and never as impossible

> **Option 2a — divide the leftover in proportion to each chord's overall frequency in that mode.**
> Pros: uses information we already hold — a common chord is genuinely a likelier unseen continuation
> than a rare one (principle 12, no information loss); this is the standard construction in published
> back-off models of sequences (principle 1, established method). Cons: none of substance; a little
> more arithmetic per lookup.

**In plain words.** Each row of the transition table ends with one pooled probability covering everything too rare to store on its own. When the decoder meets one specific rare continuation it must turn that pooled value into a number for that continuation. It does so in proportion to how common the chord is generally.

**Why.** The chosen rule is the standard construction in published back-off models of sequences, and it uses information already held — a common chord is genuinely a likelier unseen continuation than a rare one (#12). Both alternatives are excluded on facts: dividing evenly asserts that a rare and a common chord are equally likely, which the corpus counts contradict; and treating unseen continuations as impossible is factually wrong on a corpus of this size and technically fatal, because a zero destroys any path through it.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_sensitive_cell_probe.md:155-159`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Finding 2 of the probe, ratified as option 2a, and recorded as one sentence owed to the build specification. It was a genuine gap rather than an ambiguity: no document defined it, and the probe proceeded by computing every verdict under both provisional readings and reporting both. `CLAUDE.md` gate block (A) names this rule as part of the production decoder's configuration. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-534 — The penalty for a chord tone that never sounds is COUNTED per chord factor — root, third, fifth, seventh — replacing one invented blanket number; the per-factor asymmetry then comes free

> **Option 3a — count it, from data already on disk.** The note-extraction work committed earlier
> today recorded, for every one of the ~18,000 humanly-labeled chord segments in the 326 chorales,
> which notes sound in it; and the label itself names the chord's factors (root, third, fifth, and
> seventh where the label is a seventh chord). So the counting is direct: across all segments
> labeled with a triad or seventh chord, in what fraction does the ROOT actually sound among the
> segment's notes? In what fraction the THIRD? The FIFTH? The SEVENTH? Four frequencies per chord
> family (triad versus seventh chord — at most a dozen numbers), each backed by thousands of
> observations in THIS corpus.

**In plain words.** Judging a candidate chord means weighing notes that sound but do not belong to it AND chord notes that never sound at all. The second direction was answered by a number invented for a paper walkthrough. It is replaced by counting, for every humanly labelled chord segment in the corpus, how often each of the chord's own factors actually sounds.

**Why.** The counting is direct because the data is already on disk, and the musical point is the user's: the factors are not symmetric and the counts encode that automatically — a seventh is what earns a seventh-chord label, so a silent seventh will be near-prohibitive; the fifth is the factor four-part writing routinely omits, so its penalty will be mild; the third sits between. One invented blanket number cannot express any of that. The invented value demonstrably carried load: one checked passage's margin moves with it.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_sensitive_cell_probe.md:188-195`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Finding 3 of the probe, ratified as option 3a, with the user's per-factor sharpening incorporated. The scope limit stated with it applies to EVERY table in this fit and is part of the decision: these are Bach-chorale values, no jazz values can be counted because no jazz ground truth exists, and the limit stays declared on the artifact — the standing position **D-422**/`OPEN_ITEMS.md` OI-7. The specification requiring the penalty and charging it per event of segment length is **D-449**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-535 — The checking stage's verdict: the real counted tables overturn no desk-simulation verdict, but margins moved in both directions and one margin expectation was plainly wrong

> Across the three passages, no desk-simulation verdict is overturned by the real counted values, but
> margins moved by 1.5–3.5 (log difference) in both directions, and one margin expectation was
> plainly wrong. Catching exactly this — before any code exists — is what this checking stage is for.

**In plain words.** The three passages whose paper outcomes depended most on placeholder numbers were recomputed with the real counted ones. Every verdict held. The margins did not: they moved appreciably in both directions, and one prediction about a margin was simply wrong.

**Why.** The value of the result is stated with it: catching exactly this before any code exists is what the checking stage is for. The expectations were written down before any number was looked up, which is what makes a wrong expectation detectable as one rather than absorbed.

**Status.** LIVE · decided 2026-07-19 · ratified by user

**Home.** `cowork_sensitive_cell_probe.md:246-248`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** The probe's own summary, and the discharge of item 4 of the ratified capacity protocol — recompute the value-dependent desk-simulation passages with the real tables before building. The desk simulation it checks is **D-453**; the provisional-value rule that made the check owed in the first place is **D-451**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

