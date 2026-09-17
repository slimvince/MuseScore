# CC Instruction — L5-closing QA review (CC's source-level half): code · tests · corpora · staleness

> **A layer-closing QA round before L6 opens.** Question to answer, for the whole L5 build: **is it complete AND correct,
> and is there any discovery that should change our mind about the L5 algorithm or the architecture?** This is your
> **source-level** half (code, tests, corpora/test-data, staleness); Cowork takes the architecture + documentation half and
> synthesizes. **Read-and-report + tidy the clear-cut imperfections only.** Declare every judgment call (anything touching
> algorithm/architecture, or any inference matter) for Cowork — **do not act on it**. **No inference-fixing (firewall). No
> production movement. Dormancy + byte-identity preserved.** *(Reminder: the never-bash rule is Cowork's — you read source
> with your file tools, and may run build/tests/corpus for verification.)*

## §0 — Scope + ground rules
- **In scope to fix during this round (tidy):** stale doc/comment/STATUS text, stale counts, dead code, obviously-missing
  test cases, mislabeled/duplicated test data — the imperfections a close is meant to clean.
- **Declare, do NOT act:** anything that changes an algorithm, a contract, or the architecture; anything that is an
  inference/accuracy fix; anything you are unsure is correct. Surface it with evidence for a Cowork ruling.
- **Invariants that must still hold (verify, report any breach):** every L5 unit is **dormant** (no `src/` production
  consumer — only its tests + `tools/batch_analyze.cpp` diagnostics); **reuse-not-duplicate** (no second formatter / no
  re-implemented detector); the **§8 closure** has no back-edge; **default constants** (firewall); corpus **53/24/53**.

## §1 — Code review (the L5 units, at source)
For each unit in `src/composing/analysis/function/` — `functionprogression`, `functionromannumeral`, `functioncadence`,
`functionresolver`, `forwardoverride`, `functionmodulation`, `functionrelationallabel`, `functionoutput` (+ the reused
`tonicizationlabeler`, `engravingbridge/phraseboundaryview`, the L3 carry on `harmonicrhythm.h`) — report:
- **Correctness:** does the code do what its §5.x spec rule says? Flag any divergence (like the Step-M over-trigger: a path
  that emits before its guard, an early-return that bypasses a check, an off-by-one in a degree/inversion).
- **Dormancy:** re-grep — zero `src/` production consumers. Name every includer.
- **Reuse:** confirm no duplicated formatter/detector; the delegations (`formatRomanNumeral`, `labelTonicizations`,
  `detectLocalModulations`, `forwardoverride`) are live, not forked.
- **Quality:** dead code, unreachable branches, leftover TODO/FIXME, value-initialized-but-unused fields, comment typos,
  the `kTemplateCount`-style size-coupling invariants. Tidy the clear-cut ones; list what you changed.

## §2 — Test-case audit
- **Coverage matrix:** one row per §5.x rule / ambiguity kind (all six incl. symmetric-rotation) / relational label
  (applied, Neapolitan, aug6 It/Fr/Ger, mixture) / cadence type (PAC/IAC/half/…) / the §8 override + closure / the §7
  output assembly. Mark covered / gap.
- **Oracle quality:** are assertions checked against known theory (not self-referential / not tautological)? Flag any
  vacuous or circular test.
- **Tidy:** add the clear-cut missing tests (dormant, oracle-asserted). Declare any gap whose correct expectation is a
  judgment call.

## §3 — Corpora / test-data verification
- **Gate reproducibility:** confirm the **53/24/53** case-identity sets reproduce from a clean regen of all three presets
  (`run_bach_preset.py` + `characterise_bir_false.py`), manifests stamped, fingerprints matching. Report any drift.
- **Harness correctness:** `batch_analyze --dump-l5` + `tools/cc_stepM_l5_measure.py` — confirm the measurement still runs,
  the substrate is the legacy region source (as documented), and the dump remains read-only / no production consumer.
- **DCML ground truth:** spot-confirm `dcml_parser.py` roots are oracle-correct on a sample (the parser-rebaseline cases) —
  no regression in the ground-truth itself.
- **Test data hygiene:** any do-not-touch corpus files intact (`docs/score_inventory.md`); no orphaned/duplicated fixtures.

## §4 — Staleness sweep
- **Docs/comments/STATUS vs as-built:** flag and tidy stale text — references to the reverted "fully-diatonic guard"
  premise, the old "joint L4+L5 engage / Phase 5d as next" framing (now: engage deferred indefinitely), superseded counts,
  the template-count invariant in `docs/scoring_model.md` §2 vs the array extent, the deferred-item ledger accuracy.
- **Cross-doc consistency:** the L5 design doc's §7 contract / §15 joint items / §5.x rules must match the code; flag any
  drift (Cowork owns the spec text — you **report** spec drift, you do not edit the spec).

## §5 — Discoveries (the mind-changing question)
Surface, with evidence, anything that should change our mind about the **L5 algorithm or the architecture** — a latent
premise-error like the over-trigger, a contract that the as-built can't actually honor, a reuse that is subtly wrong, a
place where the spec assumes something the data contradicts. **Declare each; do not act.** If you find none, say so
explicitly (a clean bill is a valid finding).

## §6 — Gate (this round moves nothing in production)
- Any tidy is **docs / tests / dead-code only** — corpus **53/24/53** unchanged, suites + snapshots green, no golden
  refresh, dormancy intact. **Any production movement, any constant/threshold change, any inference fix → STOP and
  declare.** `upstream` → STOP.

## §7 — Deliver
Commit local-only the clear-cut tidies (separate commits by kind: `test(...)`, `chore(...)`/`docs(...)` — keep spec-text
edits out, those are Cowork's). Write `cc_phase5c_L5_close_review.md` (gitignored): the §1 per-unit code findings, the §2
coverage matrix + added tests, the §3 corpus/harness/GT verification, the §4 staleness tidies, the **§5 declared
discoveries** (or the explicit clean bill), the §6 gate, and the shas — so Cowork verifies each finding at source and folds
it into the complete-and-correct verdict. **Declare everything uncertain; this round's value is the discoveries, not the
green checks.**
