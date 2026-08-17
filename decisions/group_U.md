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

### D-215 — Gating the root-continuity bonus on a sparse predecessor is a dead end

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **`rootContinuityBonus` sparse-predecessor gate is a dead end** (Iter 98).
>   Both density-based and inversion-aware variants tried; both regress
>   mozart_k280-1 IV→V65 Alberti bass.

**In plain words.** Making the bonus that rewards keeping the same root depend on how much evidence the previous chord had was tried in two forms and abandoned.

**Why.** Measurement named in the record: both the density-based and the inversion-aware variants regress the same passage - a Mozart sonata movement's Alberti-bass progression from the subdominant to the dominant in first inversion.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:1137`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry. ★ THE DECIDING ACT RECORDED AND KEPT (user's ruling of 2026-08-17, cowork_rulings_2026_08_17_residue_sitting.md §2 (Ruling 2) — a ratification of a document reaches the decisions that document carries): the recovered act ratifies `ARCHITECTURE.md`, and that document carries this entry's own subject recogniser the entry's own identity at line 1948, reading — "**Tried and closed on the chord layer — do not retry; the register carries each with its measurement: D-215, D-299, D-300, D-301, D-302, D-317, D-318, D-319, D-320, D-328.** **★ A REBUILT OR RE-TUNED CHORD SCORING MUST NOT RELY ON THE HELD-NOTE REPETITION BONUS THE FAITHFUL NOTE MODEL REMOVED (re-homed into this specification 2026-08-08 on the user's ruling).** Before the note reader was rebuilt, a note held across a tie was counted more than once, and that spurious extra" The match is quoted from `tools/audit/ratified_document_check.json`; no other field of this entry is touched. **A LIVE specification section restates this as binding:** `ARCHITECTURE.md` — the chord layer (at line 1948 on 2026-08-03), under *"Tried and closed on the chord layer — do not retry"*. The LEGACY mark above says this decision's SUBJECT is dormant; what is named there says the prohibition still constrains what a future design may attempt, and the two are not the same claim. Pointer only — the rule is published once, there (#6). See `OPEN_ITEMS.md` OI-302.

### D-220 — The augmented-seventh guard requires both the major third and the augmented fifth

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **B2 aug7 guard requires BOTH M3 and aug5** (`||` not `&&`). M3-only was
>   tried and reverted (Schumann D-major, Corelli G-major snapshot flips).

**In plain words.** The guard fires only when both intervals are present, not when either one is. Requiring only the third was tried and reverted.

**Why.** Measurement named in the record: the either-one form flipped snapshots on a Schumann piece in D major and a Corelli piece in G major.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:1169-1170`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry. ★ **THE VERBATIM AND THE HOME ANCHOR WERE RE-TAKEN 2026-08-09** (CC, `cc_instruction_return_continuation_4.md` Task 1) on the user's **Ruling 24(a)** of `cowork_rulings_2026_08_09_fourth_stop.md`, which repairs the five corrupted pairs `OPEN_ITEMS.md` **OI-358** found. This entry's quote was taken from the bullet its own TITLE and DEFENSE describe, read in place at the home: the title names the augmented-seventh guard requiring both intervals, and the recorded defense names the Schumann D-major and Corelli G-major snapshot flips — both of which are in the bullet now quoted and in no other. **NOTHING ELSE MOVED**: the title, the plain restatement, the defense, the status, the date, the ratifier and the LEGACY mark are untouched, because those were never wrong — what was wrong was the quote and the line. **THE FORMER, INCORRECT VERBATIM, PRESERVED WHOLE (#12):** "- **`hasStructuralBass` gates inversion bonuses.** Sparse upper-register\n  \"bass\" notes do not get inversion bonuses (Corelli op01n08d m2 b3).\n" — which is the bullet belonging to **D-221**. **FORMER HOME ANCHOR, PRESERVED (#12):** `docs/scoring_model.md:1049`. The `verbatim` field carries ONE quote, the correct one (#6); the former quote lives here, in the provenance, which is where a superseded field belongs.

### D-221 — A sparse upper-register lowest note does not earn inversion bonuses

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **`hasStructuralBass` gates inversion bonuses.** Sparse upper-register
>   "bass" notes do not get inversion bonuses (Corelli op01n08d m2 b3).

**In plain words.** A low note that is thin and high in the texture is not treated as a structural bass, so the bonuses that reward a recognisable inversion do not fire for it.

**Why.** Measurement named in the record: a Corelli trio-sonata movement, measure 2 beat 3.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:1177-1178`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry. ★ **THE VERBATIM AND THE HOME ANCHOR WERE RE-TAKEN 2026-08-09** (CC, `cc_instruction_return_continuation_4.md` Task 1) on the user's **Ruling 24(a)** of `cowork_rulings_2026_08_09_fourth_stop.md`, repairing one of the five corrupted pairs `OPEN_ITEMS.md` **OI-358** found. The quote was taken from the bullet this entry's own TITLE and DEFENSE describe, read in place: the title names a sparse upper-register lowest note earning no inversion bonuses, and the recorded defense names the Corelli trio-sonata measure — both are in the bullet now quoted. **NOTHING ELSE MOVED**; the title, restatement, defense, status and mark were never wrong. **THE FORMER, INCORRECT VERBATIM, PRESERVED WHOLE (#12):** "  live `results[0]` reference (Sub-9a lesson).\n" — a two-line FRAGMENT of the pre-sort capture bullet, which belongs to **D-223**. **FORMER HOME ANCHOR, PRESERVED (#12):** `docs/scoring_model.md:1058`. The `verbatim` field carries ONE quote (#6).

### D-222 — If the diminished bonus rotates the winner to a non-diminished chord, the result without it is used

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Post-bonus winner quality guard for `w_dim`.** The bonus can rotate the
>   global winner across bass candidates; if the post-bonus winner is not
>   Dim/HalfDim, fall back to the without-wDim variant.

**In plain words.** The bonus that favours diminished readings can, in the course of comparing bass notes, end up electing a winner that is not diminished at all. When that happens the analysis falls back to the answer it had before the bonus was applied.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The record holds no derivation for this fallback. What stands in its place is the section's BLANKET ground, which covers every bullet in it equally rather than this one in particular: these are load-bearing design decisions that future changes must respect or risk documented regressions. The rule's own text at the home states the DEFECT IT GUARDS AGAINST — the bonus can rotate the global winner across bass candidates, so a post-bonus winner that is not diminished or half-diminished falls back to the variant computed without it — which is the failure it prevents rather than an argument for this remedy over another. ⚠ Legacy subject. ★ AND THIS ENTRY'S RECORDED VERBATIM QUOTES A DIFFERENT RULE THAN ITS TITLE, RESTATEMENT AND DEFENSE DESCRIBE — rowed at `OPEN_ITEMS.md` OI-358. This field is written against the decision the title, restatement and defense identify, which is the post-bonus winner-quality guard at the home, and NOT against the quoted text.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:1180-1182`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry. ★ **THE VERBATIM AND THE HOME ANCHOR WERE RE-TAKEN 2026-08-09** (CC, `cc_instruction_return_continuation_4.md` Task 1) on the user's **Ruling 24(a)** of `cowork_rulings_2026_08_09_fourth_stop.md`, repairing one of the five corrupted pairs `OPEN_ITEMS.md` **OI-358** found. The quote was taken from the bullet this entry's own TITLE and RESTATEMENT describe, read in place: the diminished bonus rotating the winner off a diminished reading, and the fallback to the variant computed without it. **NOTHING ELSE MOVED.** **THE FORMER, INCORRECT VERBATIM, PRESERVED WHOLE (#12):** "  fires only when at least one tone has `onsetAtRegionStart == true` or\n  `distinctMetricPositions > 0` (i.e. came from `collectRegionTones`).\n  Single-tick / status-bar / unit-test paths use the legacy single-bass path." — the tail of the joint-scoring bullet, which belongs to **D-224**. **FORMER HOME ANCHOR, PRESERVED (#12):** `docs/scoring_model.md:1061`. **ONE FURTHER NOTE, because this entry's `rationale` mentions the mismatch:** that field was written on 2026-08-09 by the defense-gap task, deliberately against the decision the title identifies rather than against the then-quoted text, and it carries a marker saying so. It is left exactly as written — the repair does not rewrite a field that was already correct about which decision this entry records. The `verbatim` field carries ONE quote (#6).

### D-223 — A gate that judges the pre-correction winner reads a snapshot, not the live result

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Pre-sort capture for original-winner gates.** Gates that compute against
>   the pre-correction winner must read `originalWinner*` snapshots, not the
>   live `results[0]` reference (Sub-9a lesson).

**In plain words.** Where a gate has to compare against whatever the analysis thought before a correction was applied, it reads a copy taken beforehand rather than the current top result, which the correction may already have changed.

**Why.** Measurement named in the record: the lesson came from a specific numbered attempt in which the live reference had already moved.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:1184-1186`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry. ★ **THE VERBATIM AND THE HOME ANCHOR WERE RE-TAKEN 2026-08-09** (CC, `cc_instruction_return_continuation_4.md` Task 1) on the user's **Ruling 24(a)** of `cowork_rulings_2026_08_09_fourth_stop.md`, repairing THE SHARPEST of the five corrupted pairs `OPEN_ITEMS.md` **OI-358** found. The quote was taken from the bullet this entry's own TITLE and DEFENSE describe, read in place: the title names a gate judging the pre-correction winner reading a snapshot, and the recorded defense names the numbered attempt in which the live reference had already moved — the bullet now quoted names that attempt in terms. **NOTHING ELSE MOVED.** **THE FORMER, INCORRECT VERBATIM, PRESERVED WHOLE (#12):** "---\n\n## 9. How to add a new template safely (checklist)" — **a horizontal rule and a section heading, which is not a decision at all.** That is what made this the case a reader could see without any comparison, and it is preserved because a defect's own evidence is information (#12). **FORMER HOME ANCHOR, PRESERVED (#12):** `docs/scoring_model.md:1329`. The `verbatim` field carries ONE quote (#6).

### D-224 — Joint bass-and-chord scoring requires accumulated regional evidence

⚠ **LEGACY** — this decision's subject is the dormant pipeline awaiting deletion at the retirement map (marking convention user-ratified 2026-08-02; wording weakened by the user's ruling of 2026-08-03 — the mark states what the decision is ABOUT, and makes no claim about the live solution).

> - **Joint scoring requires regional accumulation.** `jointScoringEnabled`
>   fires only when at least one tone has `onsetAtRegionStart == true` or
>   `distinctMetricPositions > 0` (i.e. came from `collectRegionTones`).
>   Single-tick / status-bar / unit-test paths use the legacy single-bass path.

**In plain words.** The scoring that considers the bass note and the chord together only switches on when the notes came from accumulating a whole stretch of music. The single-moment paths - the status bar, a unit test - use the simpler single-bass scoring.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The record holds no derivation. The rule's own text at the home states the CONDITION and its consequence — joint scoring fires only where at least one tone carries evidence of regional accumulation, and the single-tick, status-bar and unit-test paths therefore use the legacy single-bass path — which is the rule restated rather than a ground for it; nothing says why those paths must fall back rather than accumulate, and no alternative is weighed. The section's blanket statement that its bullets are load-bearing decisions covers every bullet equally and is not this entry's own defense. ⚠ Legacy subject. ★ AND THIS ENTRY'S RECORDED VERBATIM QUOTES A SECTION-OPENING CHECKLIST RATHER THAN THIS RULE — rowed at `OPEN_ITEMS.md` OI-358. This field is written against the decision the title, restatement and defense identify, and NOT against the quoted text.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:1188-1191`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry. ★ **THE VERBATIM AND THE HOME ANCHOR WERE RE-TAKEN 2026-08-09** (CC, `cc_instruction_return_continuation_4.md` Task 1) on the user's **Ruling 24(a)** of `cowork_rulings_2026_08_09_fourth_stop.md`, repairing the last of the five corrupted pairs `OPEN_ITEMS.md` **OI-358** found. The quote was taken from the bullet this entry's own TITLE and RESTATEMENT describe, read in place: joint bass-and-chord scoring firing only on accumulated regional evidence, with the single-moment paths falling back to the single-bass path. **NOTHING ELSE MOVED.** **THE FORMER, INCORRECT VERBATIM, PRESERVED WHOLE (#12):** "Derived from the B1, B2, and B3 lessons.\n\n1. **Read the existing template nearest to yours.** Understand its intervals,\n   TPC deltas, and which existing terms / guards apply to it.\n" — the opening of the template checklist in the FOLLOWING section, which is a procedure and not a decision. **FORMER HOME ANCHOR, PRESERVED (#12):** `docs/scoring_model.md:1333`. **ONE FURTHER NOTE:** this entry's `rationale` was written on 2026-08-09 by the defense-gap task, deliberately against the decision the title identifies rather than against the then-quoted text, and it carries a marker saying so; it is left exactly as written. The `verbatim` field carries ONE quote (#6).

### D-281 — The batch measurement tool must emit the structured fields on every alternative, or the corpus figures silently revert

> **★ THE OUTPUT-SCHEMA FLOOR FOR THE BATCH MEASUREMENT TOOL — BELOW IT A CORPUS MEASUREMENT
> SILENTLY REVERTS (homed here 2026-08-07 on the user's ruling; the record states no date and no
> ratifier for the decision itself).** `batch_analyze.cpp` must emit `rootPitchClass`,
> `bassPitchClass`, `quality` and `bassIsRoot` on **every alternative entry**, not on the winner
> alone.

**In plain words.** The batch analysis tool emits root pitch class, bass pitch class, quality and bass-is-root on every alternative entry, not only on the winner. Those fields activate the comparison script's reclassification of readings where the corroborating source matches our second or third candidate; without them the corpus measurement silently reverts to its earlier counts.

**Why.** The failure that produced it is recorded with it: the change was lost to a hard reset and went undetected for three weeks, and only a stale binary holding the documented baseline made the loss visible at all. It is principle #19 applied to a measurement tool - a figure produced without these fields is not the figure it claims to be.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `BUILD_AND_TEST.md:352-356`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** docs/iteration_path1_summary.md:66-72, recorded among the architecture decisions of the completed iteration path; no date or ratifier is stated at this home. A decision about a MEASUREMENT TOOL and its floor, reported separately by the phase-1d enumeration wave (2026-08-02) so that the sealed measurement-tools partition can account for it. ★ RATIFIED (user, 2026-08-02, the phase-1d queue). ★ RE-CLASSIFIED contract-home 2026-08-03 (CC, phase 1k): the user RATIFIED this document's status banner on 2026-08-03 (drafted at phase 1j, presented at `ratification_surfaces/cowork_pending_ratifications_next_session.md` §1). The document therefore satisfies the fifth home case in full — a status banner, the ratification, and the delegation pointer from the owning surface (`CLAUDE.md` decisions-register rule (g), user-ratified 2026-08-02 at `open_items/OI-268.md`). The `gap` classification it carried is discharged; its LEGACY mark, where it carries one, is untouched. ★ HOMED 2026-08-07 (CC, the three-owner-rulings wave, executing the user's ruling R1 of 2026-08-07). This is one of the three entries the licensed homing wave of the same date did NOT home: its recorded owner named two candidate sites in two different files, assumption A1 came back refuted for it, and it was returned to the user with the owner question rather than written into a guessed section. The user answered it. Written into `BUILD_AND_TEST.md` §2, the Corpus Regression Check — the measurement procedure the entry's own recorded owner names, and the section that already carried the four fields, the reclassification they activate and the reversion, as history — in that section's own voice and with its defense. THE EXCLUDED ALTERNATIVE, RECORDED WITH THE RULING (#12): `CLAUDE.md` gate block (A), which governs how the recorded numbers are READ and already delegates commands and tooling to `BUILD_AND_TEST.md`; homing the schema floor there would blur the layer (#7) and restate what is pointed at (#6). One home only — a pointer from the gate block is permitted, a copy is not. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. The edit is ADD-ONLY: no existing line of `BUILD_AND_TEST.md` is modified or deleted. FORMER HOME, PRESERVED (#12): `docs/iteration_path1_summary.md:79-85`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `process` entry (the register's own home rule): heading line 64, section "## Architecture decisions made during this path", label "“Architecture decisions made during this path”", delegated null, delegation "named in no user-ratified surface", states_rules null, verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class contract-home, class_before_phase1q contract-home, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "3. **batch_analyze output schema**: `batch_analyze.cpp` must emit\n   `rootPitchClass`, `bassPitchClass`, `quality`, `bassIsRoot` on every\n   alternative entry. This activates the previously-dormant\n   `_matches_alternative` reclassification in `compare_analyses.py` and is the\n   floor below which corpus measurements revert to pre-Iter-36 counts (~700\n   BIR=false). Committed in Iter 36 (recovered in `5df8421114` after a git\n   reset lost the original commit)." Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, the date it was homed, that the user ruled it, and its defense.

