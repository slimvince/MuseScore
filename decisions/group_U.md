# Decisions group U — The standing decision-bearing surfaces

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-213 — The defect-type catalog is the living list of every problem type, and it is added to at discovery

> **Created 2026-07-10 (session 36), user-directed.** The second half of the audit protocol
> (`cowork_audit_protocol.md` P7/P8): every problem TYPE ever discovered in this project, each
> with its detection signature — mechanical where possible. **Standing rule (mirrors the
> OPEN_ITEMS rule): every newly discovered problem TYPE gets a catalog entry in the same
> commit that records its discovery.** Types are never removed; a type made impossible by a
> structural fix is marked NEUTRALIZED with the mechanism that kills it (the kTemplateCount
> precedent). IDs are stable.

**In plain words.** Every kind of problem ever found in this project has an entry saying what it is, the case that first showed it, and how to detect it - mechanically wherever possible. A newly discovered kind of problem gets its entry in the same commit that records the discovery. Entries are never deleted: a kind of problem that a structural change has made impossible is marked as such, with the mechanism that kills it.

**Why.** Stated constraint, DEFECT_TYPES.md:8-9: keeping a neutralized type on the list, with the mechanism that killed it, is what stops the same defect being reintroduced by a later change that removes the mechanism. The named precedent is the template-count constant, which closed a silent buffer overrun by making the compiler enforce the sizes.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `DEFECT_TYPES.md:3`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** DEFECT_TYPES.md:3-9, user-directed 2026-07-10. It is the second half of the audit protocol; the standing rule mirrors the open-items register's rule (c). The catalog is one of the four surfaces the self-check reads (D-196).

### D-214 — The dim7 characteristic bonus is the rotation selector and may not simply be removed

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

> - **`dim7CharacteristicBonus` is the dim7 rotation selector.** Do not
>   suppress without replacing the non-diatonic-♭♭7 mechanism (B3 lesson).

**In plain words.** The bonus that makes a diminished-seventh chord prefer one rotation over another is what selects the rotation. Removing it without putting an equivalent mechanism in its place breaks the choice.

**Why.** Measurement named in the record: the B3 lesson - an attempt that suppressed it and had no replacement for the non-diatonic double-flat-seventh mechanism.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:912`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-215 — Gating the root-continuity bonus on a sparse predecessor is a dead end

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

> - **`rootContinuityBonus` sparse-predecessor gate is a dead end** (Iter 98).
>   Both density-based and inversion-aware variants tried; both regress
>   mozart_k280-1 IV→V65 Alberti bass.

**In plain words.** Making the bonus that rewards keeping the same root depend on how much evidence the previous chord had was tried in two forms and abandoned.

**Why.** Measurement named in the record: both the density-based and the inversion-aware variants regress the same passage - a Mozart sonata movement's Alberti-bass progression from the subdominant to the dominant in first inversion.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:915`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-216 — The stepwise-bass bonus's four gates are each load-bearing

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

> - **`w_stepIn`/`w_stepOut` has four gates, each load-bearing** — the
>   `ScoringPhase::Final` call-site gate, root-position guard,
>   first-inversion-m7-family surgical guard, power-quality exclusion. Each prevents
>   a specific documented regression.

**In plain words.** The bonus for a bass moving by step is switched off in four situations, and each of the four is there because it prevented a specific regression that was actually observed.

**Why.** Measurement named in the record: each gate prevents a specific documented regression.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:919`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-217 — The segmentation phase must suppress every context-dependent bonus

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

>   seq, and dim bonuses plus Gate R are all skipped in the Segmentation phase (gated at
>   the `applyHarmonicFunction` call site, not inside the now-stateless bonus functions).
>   Adding a new context bonus without gating it on `applyProgressionSignals` /
>   `ScoringPhase::Final` will cause segmentation regressions.
>
> - **Template arrays update atomically under `analysis::kTemplateCount`.** All

**In plain words.** While the analysis is still deciding where one chord ends and the next begins, none of the bonuses that look at neighbouring chords may score anything. Adding a new context bonus without that gate will make the segmentation worse.

**Why.** Stated constraint: where a boundary falls decides which notes each candidate sees, and chord identity is itself a signal for where boundaries belong (ARCHITECTURE.md:693-696), so a context bonus scoring the exploratory passes lets the answer choose its own input. Its specification home is D-062.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:925`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-218 — Template array sizes derive from one constant, so the compiler enforces them

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

>   constant since `a236a0ff21`, so the compiler enforces sizes. Adding a template =
>   bump the constant + add the template/mask entries in the same edit (§9 step 5).
>   The historical silent stack-buffer overrun from a missed matrix size is closed.
>   (Stage 2.3 removed the `kDiagTemplates` mirror — one fewer site to keep in sync.)
>
> - **Gate A subsumed Gates B/C/D — now removed (Stage 3.4b, historical); Gate A itself
>   unified into `promoteToWinner`/FM2 (2026-07-06, §6a).** Gate A's entry conditions were a

**In plain words.** Every array whose length must equal the number of chord templates takes that length from a single named constant. Adding a template means changing the constant and adding the template in the same edit.

**Why.** Measurement named in the record: the historical failure was a silent stack buffer overrun from a missed matrix resize, caught during an attempted template addition; deriving the extents from the constant closes it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:932`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-219 — Gates B, C and D were unreachable and were removed; no temporal condition may be added to the enharmonic flip

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

>   removed in the Stage-3 per-gate retirement audit (roadmap 3.4b) as a byte-identical change
>   (0/353 × 3 configs, snapshots zero-diff). Gate A's swap later became the present branch of
>   the unified `promoteToWinner()` primitive under the FM2 rule (byte-identical, full surface).
>   Constraint going forward: do not add temporal conditions to the enharmonic flip — there is
>   no longer a B/C/D safety net; any forward/window/consecutive-stepwise variant of the
>   Major-add6 ↔ Minor flip must be reintroduced explicitly and tested.
>
> - **B2 aug7 guard requires BOTH M3 and aug5** (`||` not `&&`). M3-only was
>   tried and reverted (Schumann D-major, Corelli G-major snapshot flips).
>
> - **Gate thresholds are Baroque-calibrated.** Do not widen Baroque-tuned
>   thresholds to accommodate Jazz or other styles (see CLAUDE.md "Gate
>   threshold and preset policy"). Use a tighter structural guard or a
>   preset-specific override instead.

**In plain words.** Three post-scoring gates turned out to be unreachable, because the conditions of the gate before them were a strict subset of theirs, and they were deleted. The constraint that follows: nothing that depends on time or on neighbouring chords may be added to the major-with-added-sixth against minor flip, because the safety net those gates provided is gone.

**Why.** Measurement named in the record: the removal was proven byte-identical - 0 differences across 353 pieces in three configurations, with the snapshot tests showing no difference either.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:940`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-220 — The augmented-seventh guard requires both the major third and the augmented fifth

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

> - **`hasStructuralBass` gates inversion bonuses.** Sparse upper-register
>   "bass" notes do not get inversion bonuses (Corelli op01n08d m2 b3).

**In plain words.** The guard fires only when both intervals are present, not when either one is. Requiring only the third was tried and reverted.

**Why.** Measurement named in the record: the either-one form flipped snapshots on a Schumann piece in D major and a Corelli piece in G major.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:955`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-221 — A sparse upper-register lowest note does not earn inversion bonuses

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

>   live `results[0]` reference (Sub-9a lesson).

**In plain words.** A low note that is thin and high in the texture is not treated as a structural bass, so the bonuses that reward a recognisable inversion do not fire for it.

**Why.** Measurement named in the record: a Corelli trio-sonata movement, measure 2 beat 3.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:964`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-222 — If the diminished bonus rotates the winner to a non-diminished chord, the result without it is used

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

>   fires only when at least one tone has `onsetAtRegionStart == true` or
>   `distinctMetricPositions > 0` (i.e. came from `collectRegionTones`).
>   Single-tick / status-bar / unit-test paths use the legacy single-bass path.

**In plain words.** The bonus that favours diminished readings can, in the course of comparing bass notes, end up electing a winner that is not diminished at all. When that happens the analysis falls back to the answer it had before the bonus was applied.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:967`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-223 — A gate that judges the pre-correction winner reads a snapshot, not the live result

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

> ---
>
> ## 9. How to add a new template safely (checklist)

**In plain words.** Where a gate has to compare against whatever the analysis thought before a correction was applied, it reads a copy taken beforehand rather than the current top result, which the correction may already have changed.

**Why.** Measurement named in the record: the lesson came from a specific numbered attempt in which the live reference had already moved.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:971`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-224 — Joint bass-and-chord scoring requires accumulated regional evidence

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map; it has no effect on the live solution (marking convention user-ratified 2026-08-02).

> Derived from the B1, B2, and B3 lessons.
>
> 1. **Read the existing template nearest to yours.** Understand its intervals,
>    TPC deltas, and which existing terms / guards apply to it.

**In plain words.** The scoring that considers the bass note and the chord together only switches on when the notes came from accumulating a whole stretch of music. The single-moment paths - the status bar, a unit test - use the simpler single-bass scoring.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:975`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-225 — A corpus is regenerated before its baseline figures are updated

> **IMPORTANT — corpus JSONs must be regenerated before updating baselines.**
> `analyze_inversion_errors.py` reads existing `.ours.json` files and will silently
> report stale numbers if those files are not current. Whenever you update the BIR
> baselines here, you must first regenerate the corpus (as above), then run the script
> against the per-preset dir and record the new figures.

**In plain words.** The measurement scripts read files produced by an earlier run. Updating a recorded baseline without regenerating those files first produces a number that silently describes an older state of the system.

**Why.** Stated constraint, BUILD_AND_TEST.md:286-287: the script reads existing analysis files and will silently report stale numbers if they are not current - silently being the operative word, since nothing about the output reveals it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `BUILD_AND_TEST.md:285`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** BUILD_AND_TEST.md:285-289. The mechanical enforcement is the per-preset corpus manifest: the regeneration script exits nonzero on an incomplete corpus and the measurement refuses a directory whose manifest is missing or whose fingerprints do not match (CLAUDE.md:514-525).

### D-226 — The music21 export is version-pinned; regenerating it is a deliberate re-baseline

> **music21 version pin (audit C2):** the committed `tools/corpus/*.xml` were
>   exported by **music21 v.9.9.1** (recorded in each file's
>   `<software>music21 v.9.9.1</software>` / `<encoding-date>2026-04-05</encoding-date>`
>   tag), and the paired `*.music21.json` ground truth is from the same generator.
>   Regenerating with a different music21 is a **deliberate re-baseline** of the
>   BIR denominators, not a refresh. `run_bach_preset.py` now copies the
>   detected music21 version into each `corpus_manifest.json` (`music21_version`,
>   informational — not validated).

**In plain words.** The committed corpus files and the paired corroborating analyses were produced by one specific version of music21, recorded inside the files themselves. Regenerating them with a different version is not a refresh - it moves the denominators every agreement figure is measured against, and is treated like updating a golden reference.

**Why.** Stated constraint, tools/REPRODUCIBILITY.md:148-152: the committed corroborating analyses are canonical as committed, and regenerating them with ANY version shifts the denominators - so the event is coordinated rather than allowed to happen incidentally. This is the reproducibility principle (#16) applied to a third-party tool.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `tools/REPRODUCIBILITY.md:139`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** tools/REPRODUCIBILITY.md:139-155, recorded as audit finding C2. The pinned version is 9.9.1, enforced in `tools/music21_batch.py` (MUSIC21_PIN), which refuses to regenerate on a mismatch unless explicitly overridden. Note the asymmetry the record itself states: the version copied into each corpus manifest is informational and is NOT validated.

### D-281 — The batch measurement tool must emit the structured fields on every alternative, or the corpus figures silently revert

> 3. **batch_analyze output schema**: `batch_analyze.cpp` must emit
>    `rootPitchClass`, `bassPitchClass`, `quality`, `bassIsRoot` on every
>    alternative entry. This activates the previously-dormant
>    `_matches_alternative` reclassification in `compare_analyses.py` and is the
>    floor below which corpus measurements revert to pre-Iter-36 counts (~700
>    BIR=false). Committed in Iter 36 (recovered in `5df8421114` after a git
>    reset lost the original commit).

**In plain words.** The batch analysis tool emits root pitch class, bass pitch class, quality and bass-is-root on every alternative entry, not only on the winner. Those fields activate the comparison script's reclassification of readings where the corroborating source matches our second or third candidate; without them the corpus measurement silently reverts to its earlier counts.

**Why.** The failure that produced it is recorded with it: the change was lost to a hard reset and went undetected for three weeks, and only a stale binary holding the documented baseline made the loss visible at all. It is principle #19 applied to a measurement tool - a figure produced without these fields is not the figure it claims to be.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/iteration_path1_summary.md:66-72`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** docs/iteration_path1_summary.md:66-72, recorded among the architecture decisions of the completed iteration path; no date or ratifier is stated at this home. A decision about a MEASUREMENT TOOL and its floor, reported separately by the phase-1d enumeration wave (2026-08-02) so that the sealed measurement-tools partition can account for it. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

