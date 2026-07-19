# The pre-fit gates for the joint estimator (OI-176 / OI-177 / OI-178 / OI-180) — ★ USER-RATIFIED 2026-07-19

**Ratified by the user 2026-07-19, as asked:** the four protocols including the [prov-ratify]
constants (5-fold; cell-count threshold 20; tokens/params ≥ 10; 95 % piece-bootstrap CI). The
OI-176/OI-177/OI-178/OI-180 rows read "protocol ratified — pending execution"; changing any protocol
constant hereafter is a protocol amendment (#22), not a tuning act.

**Author:** Cowork, 2026-07-19, at the user's direction — the funnel stage after the ratified desk
simulation (`cowork_factorization_desk_simulation.md`; handoff 2026-07-19 block). **Nothing here is a
build and nothing here fits a value** — these are the four governance protocols the plan amendments
(`cowork_joint_estimator_architecture.md` §7 items 1, 2, 3, 5) require to be written and ratified
BEFORE the estimator funnel advances (#20/#22/#23). Each gate states its pass conditions and its
register-row disposition. **Ratifying this document ratifies the four protocols;** the rows then read
"protocol ratified — pending execution," and the funnel's next stage (the read-only probe / build arc
under OI-180's sanction) may open only under them.

Provisional numeric choices inside the protocols (fold count, cell-count threshold, confidence level)
are marked **[prov-ratify]** — they become binding at ratification but remain protocol constants, not
fitted values; changing one later is a protocol amendment (#22), not a tuning act.

---

## The held-out evaluation protocol (OI-176; gates the fit event; #20/#19/#16)

**What is being prevented:** a headline figure graded on data that helped fit it — including the
subtle forms: a degree VOCABULARY derived from all-corpus counts, a smoothing constant chosen on the
grading data, a threshold "checked" against the final metric.

1. **Unit and axes.** Evaluation is on the robust unit (CLAUDE.md block (A)): duration-weighted
   union-of-boundaries cells, root governs, RN + key(home, local) tracked beside, DCML-only GT through
   `dcml_parser.load_wir_regions` (the OI-142-corrected substrate), all three presets.
2. **The split: 5-fold cross-validation [prov-ratify] over the 326 WiR-covered pieces, grouped by
   WiR analysis file.** The 326 pieces resolve to 324 distinct analysis files (`docs/score_inventory.md`
   — some chorales share an analysis); pieces sharing an analysis file share a fold (leakage guard).
   Fold assignment is generated once with a fixed, committed seed and committed as a stamped artifact
   (`tools/` + manifest, the #17f pattern); it never changes across fit events (a re-split is a
   protocol amendment).
3. **Everything fitted is fitted inside the training folds only** — the generative tables, the
   combination weights, AND the fitted structure choices: the degree vocabulary's count threshold and
   pooling, the smoothing constants, the L2 penalty. Model selection (λ, thresholds) uses inner
   validation within the training folds; the held-out fold is touched exactly once, by the final
   fitted model of that fold.
4. **The headline claim is the pooled cross-validated figure** (per axis, per preset), with a
   piece-level bootstrap 95 % confidence interval [prov-ratify] (#24). The comparison baseline is the
   current system's figure on the same pieces — noting for honesty that the current system was
   hand-tuned against this corpus over months, so the comparison is conservative against A, not for it.
5. **The publishable model** may then be refit on all 326 (same protocol constants); its full-corpus
   figures are reported BESIDE the CV headline, never in place of it. The identity-weight generative
   baseline (the ratified mandatory ablation) runs through the SAME folds and is reported beside.
6. **The BCMH overlap (87 stems, OI-179) is NOT a CV resource** — it is reserved as the independent
   establishment/validation set for the ornament/emission cells (§5a decision 4), used with its
   declared instrument status.
7. **Precondition (dependency):** OI-184 (the WiR anacrusis beat-alignment convention) must be
   positively established (#19) before per-beat/boundary-table counts are drawn from anacrusis-bearing
   pieces — the emission and transition counts at region granularity are unaffected, so table fitting
   may begin while OI-184 is being settled, but the boundary/metric tables' counts wait for it.

**Pass condition:** every figure reported from the fit event carries its fold provenance and CI, and
no fitted object saw its grading data. **Register disposition:** OI-176 → "protocol ratified — pending
the fit event."

## The capacity budget (OI-177; gates the fit event; #20)

**What is being prevented:** overfitting-in-one-shot on a 326-piece single-composer corpus, and
silent hand-picking hidden inside "derived from counts."

1. **The parameter inventory is published before fitting** as a generated artifact (#17f): every
   table, its dimensions, its raw cell-count histogram from the training data, and the resulting free
   parameter count. No prose-only budget.
2. **Budget rule:** a table cell keeps its own maximum-likelihood estimate iff its training count
   ≥ 20 [prov-ratify]; below that it is pooled to its declared parent class (the pooling hierarchy
   declared per table in the artifact) under additive smoothing with a single declared α per table.
   The degree vocabulary's rare-class pooling (factorization §1) is the same rule applied to the state
   space itself.
3. **Global sanity bound:** total effective free parameters ≤ training tokens / 10 [prov-ratify],
   verified in the artifact. The combination-weight vector stays ≤ 12 weights (one per factor plus the
   declared-mode strength), L2-penalized, per the ratified staged-fitting decision.
4. **The desk-sim sensitive-cell record (`cowork_factorization_desk_simulation.md` §4.3) gets explicit
   treatment:** the artifact reports, by name, the raw count and own-MLE-vs-pooled disposition of the
   named cells (V6→viø7, viø7→IV, i→IV-raised-6, the applied retrogression cells vi→V/vi and
   V/x→(not x), V→vi, the incomplete-seventh missing-third penalty, the tactus-beat boundary
   probability) — and the named desk-sim cases (C2, C3, S5) are re-checked against the FITTED tables
   at the first probe, prediction-first (#17b/#17c).
5. **Fit-scope declaration (the Noland lesson, already ratified at §5a(c)), restated as a gate item:**
   tables from counts, once, frozen; only the combination weights move in the discriminative stage;
   nothing is re-fit in response to a metric excursion (the DT-2 firewall). What may never be re-fit
   blindly: the emission tables against the key axis (Noland's measured 91 % → 18–28 % collapse).
6. **Scope of the values:** fitted values are Bach-chorale values; generalization claims stay
   de-scoped (the OI-7 pattern); Jazz-preset correctness claims remain gated on OI-7's jazz GT.

**Pass condition:** the fit event's artifact satisfies 1–3 and contains 4; a fit run without the
artifact is void. **Register disposition:** OI-177 → "protocol ratified — pending the fit event."

## The robust-stop architecture-adoption protocol (OI-178; before A's first measured decode; #22/#24)

**What is being prevented:** negotiating the hard stop on a live diff. The class-(b) per-preset
non-increase ratchet (CLAUDE.md block (A)) was written for incremental change; an architecture
replacement moves runs in both directions by design. This is the pre-declared exceptional-event
variant, written while no diff exists.

1. **Output mapping, declared now:** A commits its MAP (Viterbi) path — no abstention state on the
   committed surface (the old carry/abstention re-expresses as posterior mass, per the ratified decode
   plan). Under the OI-33 convention this means no abstain-reducibility on either axis: the root
   respect has no A-side abstained cells, and key-abstain is 0 by construction; `robust_stop_diff`'s
   abstention flag should read zero — a nonzero value is a harness defect, not a result.
2. **Sequence:** (a) the OI-176/OI-177 protocols are satisfied and the CV headline + identity-weight
   ablation are in hand; (b) the written #17b adoption prediction is recorded BEFORE the full-corpus
   measurement — reflecting the ratified asymmetry (architecture doc §6 reservation 1): substantial
   improvement predicted on the key columns (home and especially LOCAL), modest-to-flat on root; a
   large root improvement would itself be a surprise to investigate (#3); (c) O-12 snapshot of the
   outgoing `tools/robust_stop/` reference; (d) the full-corpus a8 measurement, all three presets.
3. **Adoption PASS requires ALL of:**
   - **(i) Held-out:** A's key-agree (local AND home) exceeds the current baseline beyond the
     piece-bootstrap CI on every preset; root-agree and RN-agree do not degrade beyond the CI (#24 —
     a difference within the CI is not a finding, in either direction).
   - **(ii) Full-corpus aggregate criterion (replacing zero-new-case for this one event):** the
     class-(b) root-disagree DURATION shows a NET DECREASE on every preset. Added (new-failing) runs
     are permitted inside the net decrease — but the mandatory explained diff sharpens: EVERY added
     run is enumerated, classified (a)/(b) per the two-tier policy (block (B), unchanged), and each
     added class-(b) run carries an individual diagnosis note (which factor mis-carried it). An added
     class-(b) run that cannot be diagnosed is a STOP (#13), not an acceptable loss.
   - **(iii)** Class-(a) tracked with the existing INVESTIGATE threshold; the key and RN columns
     non-degrading beyond declared uncertainty on the full corpus.
   - **(iv) User ratification of the whole record as ONE revertible, provenance-stamped adoption
     commit (#14),** which re-baselines the `tools/robust_stop/` reference per the generalized 2.2e
     pattern (set-diff explained and ratified, manifest re-stamped, outgoing reference snapshotted).
4. **On FAIL:** the diagnosis is structural (#3) — a factor's form or a premise P1–P8 — never a value
   tweak outside the ratified fitting protocol; the dual path persists un-adopted under OI-180's
   bounds, or A is retired by OI-180's reverse map.

**Register disposition:** OI-178 → "protocol ratified — pending A's adoption event."

## The sanctioned dual path and the retirement map (OI-180; #23/#6/#15)

**The declared, bounded violation:** building A beside the certified stack duplicates the
key/mode/chord concern. Sanction terms:

1. **Isolation.** A lives in its own new module (physical name fixed at the build dispatch); it reads
   ONLY the L1/L1.5 published fact surface (notes, notated spellings/tpc, metric weights, fermatas,
   signature and declared mode) — never legacy L2/L3/L4 outputs. Insulation false-negative path,
   enumerated (#17e): shared utility primitives — permitted only for dependency-free pc/mask helpers
   (`normalizePc`, `diatonicMaskFromFifths` — the OI-173 shared-predicate leaf), the allowed list
   enumerated in the build dispatch; any other shared include is a violation surfaced at review.
2. **Production byte-identity for the entire build arc.** A runs only behind a default-OFF diagnostic
   driver (the fullspine pattern); every increment proves both suites + pipeline snapshots untouched;
   no golden refresh occurs on A's account before adoption.
3. **Side-by-side grading on the full output surface (#15):** committed path AND posterior mass (the
   carry analogue), all three presets, through the retained OI-145 measurement chain — never the
   winner alone.
4. **The retirement map (executes ONLY after the OI-178 adoption ratification, each item its own
   verified increment):**
   1. the L2 segmenter's filter cascade and the OI-175 head-gap tonic prior → superseded by the
      modeled semi-Markov segmentation;
   2. the L3 key emission (21-mode vocabulary, OI-174/OI-147) and the key-mode decoder's hand-set
      change costs (OI-91/OI-97) → superseded by the two-mode joint state and fitted key factors;
   3. the L4 transition fragments (`wSeq` V→I, `resolutionBonus`, Gate J, root-continuity-as-
      self-transition) → superseded by the fitted chord-transition table (F5);
   4. the enharmonic-rotation gate block (FM2/H/G-D/G-E) → superseded by the in-model spelling
      factor (F3); each drop verified by retained-rule liveness counts (OI-36) before deletion;
   5. the Gates A–L post-hoc layer dissolution — the standing deferred refactor #2 (CLAUDE.md) —
      is scheduled here, as fitted weights subsume the gate corrections;
   6. the OI-23 hand-set constant mass retires as the fitter's tables replace the terms carrying it.

   Each retirement flips its register row with provenance; ARCHITECTURE.md and the affected docs sync
   in the same increments (#10).
5. **The reverse map (if A is not adopted):** A's module is removed whole (one revertible commit), the
   fold/fit artifacts are kept as measurement history, and the retirement map is void — declared now
   so non-adoption has a lawful exit too.
6. **Bound and visibility (DT-13 guard):** the dual path's retiring gate is A's adoption event (or the
   reverse map). The handoff's entry block carries the dual-path status line every session until one
   of the two exits executes; a session that finds the dual path stalled with neither exit in motion
   surfaces it as a register item.

**Register disposition:** OI-180 → "protocol ratified — sanction in force from the build dispatch on."

---

*Ratification asked for: the four protocols as stated, including the [prov-ratify] constants (5-fold;
cell-count threshold 20; tokens/params ≥ 10; 95 % piece-bootstrap CI). After ratification: the rows
flip, and the funnel's next stage is the read-only probe / build arc under the OI-180 sanction — whose
dispatches are written just-in-time per the standing rule.*
