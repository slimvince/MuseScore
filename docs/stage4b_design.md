# Stage 4b Design — note-based mode/key PRIMARY, declared mode demoted to a droppable hint

> **★ HISTORICAL RECORD — a design that LANDED and whose decision is now superseded in fact. Banner
> added 2026-08-11 under the FILING CONVENTION (`cowork_design_doc_template.md`, the user's Ruling
> 62 of `cowork_rulings_2026_08_11_fourteenth_stop.md`), by the derived enumeration that convention
> ordered. THE BODY BELOW IS UNTOUCHED (#12).**
>
> **What this document is a record OF:** a design, written 2026-06-14, for making note-based
> mode/key inference primary and demoting the declared mode to a droppable hint.
>
> **The fate of its subject:** it was **ratified and BUILT** — Stage 4b-i landed the note-based
> opening, and `ARCHITECTURE.md` §5.2 records both of that increment's removals with their pins.
> The decision this document carries — that the declared-mode influence becomes a small additive
> hint with smallness as the gate — is recorded **superseded in fact** on the production arm
> (register entry **D-571**, homed here): the joint estimator takes the signature and declared mode
> as a weak fitted soft prior with no conditional gate anywhere, and conditions the initial key
> state only.
>
> **So the banner beneath is spent, and it is the reason this one is needed.** *"No code is written
> until this design is ratified"* was true when written; the code was written, and a reader meeting
> that line first is told a design is awaiting a decision that was taken, executed and since
> overtaken.
>
> **DRAFT — ratification-gated.** Cowork design, 2026-06-14. Implements the user's ratified
> Stage-4 redirect (`docs/back_half_design.md` §4: note-based major/minor inference PRIMARY, the
> −7 declared-mode wall REMOVED not graded, declared mode a low-weight droppable tiebreaker). Scoped
> by `cc_stage4b_scoping_dossier.md` (Cowork-verified at source: all work is composing autonomous-zone;
> ZERO `src/notation`/`src/engraving` production edits; only a snapshot-golden refresh). **User chose
> the staged, demote-first approach (2026-06-14).** No code is written until this design is ratified;
> then the 4b-i CC instruction follows.

---

## §1 — Scope and staged plan

Stage 4b is the project's **2nd intentional behavior change** (4a was the 1st): the resolved key
feeds chord emission (`basisIndep`) and the rendered Roman numerals, so byte-identity ends on the
**chord axis too**, not just the key axis. It is therefore staged so each change-class is measured
and ratified before the next (working-method "pin before you change").

- **4b-i — demote the wall + measure the honest floor.** Demote all three declared-mode enforcers to
  a single small droppable hint, make the piece-start opening note-based, and **measure key inference
  mode-present AND mode-absent**. The mode-absent run is the **no-crutch floor** — the real "how much
  of 4a's +378 is genuinely note-recoverable" number. No note-based-inference strengthening yet, so the
  demotion cost is attributable in isolation. (This run also builds the `--ignore-declared-mode`
  measurement toggle.)
- **4b-ii — strengthen note-based inference to lift the floor.** Data-driven from 4b-i: strengthen the
  terms that actually separate relative pairs (triad/tonic salience, true leading tone, pairwise
  disambiguation) to recover what the demotion costs, toward the mode-present ceiling. Final weights are
  Stage 5's fit; 4b-ii sets the structure + provisional weights.
- **Deferred (later sub-steps / Stage 6):** note-triggered partial-signature detection (OQ3),
  cadence→key wiring (OQ4), KeyArea area-level confidence + "notated≠analytical key" carrier (OQ5).

Everything in 4b-i and 4b-ii is inside `src/composing/` (CLAUDE.md autonomous zone) plus `tools/`
(the measurement toggle). The only off-limits-zone artifact is a **snapshot-golden refresh**
(`pipeline_snapshot_tests --update-goldens`), the standard ratified-change workflow.

---

## §2 — 4b-i detailed design (the next implementation)

All sites verified at source by Cowork. Four declared-mode mechanisms are demoted:

### 2.1 The −7 penalty → a small additive declared *hint* (OQ1)
- **Current** [code]: `keymodeanalyzer.cpp:571-577` subtracts `prefs.declaredModePenalty = 7.0`
  (`keymodeanalyzer.h:319`) from every candidate incompatible with the declared class — large enough to
  override the strongest note term (triad 2.50, disambiguation 4.50), i.e. a wall.
- **Change:** reduce the magnitude to a small value (**provisional 1.0**, `[empirical — Stage-5 fits]`)
  and keep it as the only declared influence on the 252-candidate score. A small magnitude makes it a
  genuine **tiebreaker**: it can only flip the winner when the raw note-based gap is already within ~1.0
  (i.e. "when genuinely unsure"), and it cannot override clear note evidence. No explicit confidence
  gate is needed — smallness *is* the gate. Keep the application point unchanged. (Optionally rename to
  `declaredHintWeight` for honesty; mechanically identical.)
- **Droppable by construction:** mode-absent (§2.5), `declaredMode == nullopt`, so the hint is simply
  not applied — the score is pure note-based.

### 2.2 The hard post-hoc promotion → REMOVED (OQ1)
- **Current** [code]: `keyresolver.cpp:344-367` ("Strong declared-mode prior") promotes the
  highest-ranked declared-compatible result to the front **regardless of score gap** — a hard veto
  ("the composer's intent overrides note-content inference").
- **Change:** **remove it outright.** It is incompatible with "note-based primary." Leaving it would
  make §2.1's demotion a no-op wherever note inference already out-scored the declared mode but got
  vetoed here. The residual declared influence is now *only* the small hint in §2.1.

### 2.3 The piece-start anchor → note-based opening (OQ2)
- **Current** [code]: `keyresolver.cpp:274-287` short-circuits the whole analysis at piece start when a
  declared mode exists, returning a declared-mode anchor (`score = relativeKeyHysteresisMargin`,
  `path:"anchor"`) the next region must beat. This is the mechanism the 4a report credited for the
  bwv153.9 win.
- **Change:** **remove the declared short-circuit; let the normal `analyzeKeyMode` lookahead path run
  from piece start** (it already handles the opening window). The opening is then note-based; residual
  declared influence is the §2.1 hint only. Mode-absent, this is the sole opening behavior. (Expected
  cost: some bwv153.9-class openings lean on note evidence in the opening window instead of the
  declaration — exactly what we want to measure.)

### 2.4 Partial-signature correction — unchanged for 4b-i (OQ3)
- **Current** [code]: `keyresolver.cpp:248` runs `partialSignatureCorrection` only
  `if (declaredMode.has_value())`. So it is **inherently crutch-dependent** — disabled mode-absent.
- **4b-i decision:** **leave it as-is.** It still helps mode-present; it is honestly absent mode-absent.
  Consequence (already flagged): the 4 partial-sig over-lock stems (bwv83.5/276/371/437) are recoverable
  only mode-present in 4b-i — the mode-absent floor will show them unrecovered. A **note-triggered**
  partial-sig detector (recovering them without the declared trigger) is a deferred sub-step, not 4b-i.

### 2.5 The mode-absent measurement toggle (in-zone)
- Add `--ignore-declared-mode` to `batch_analyze` (in `tools/`, writable) + a `prefs`/parameter path
  that forces `declaredMode = std::nullopt` into the resolver (`keyresolver.cpp:224-239` derives it; a
  small composing+tools edit, in-zone). Deterministic, reversible, scores the *same* corpus both ways —
  no corpus mutation. Cross-check option: the pre-4a binaries (mode was dropped at import) should match
  the mode-absent run on the affected stems.

### 2.6 Measurement + 4b-i ratification gate
Measure all three presets (Default = user config, Baroque, Jazz), **mode-present AND mode-absent**, on
the corrected DCML-only granularity-robust **L1 `--key-breakdown`** (committed `a96f179f40` instrument):
- **Key axis:** S2 delta vs the 4a baseline (mode-present) and the **mode-absent floor**; whether the
  **7 over-lock stems** recover (bwv64.2 the stress case); whether the **242 S2→S1** cases hold in S1
  *without the crutch* (note-based inference keeps the global key correct).
- **Chord axis:** the 57/23/57 BIR gate **will** move *(superseded 2026-06-26: live gate now 53/24/53 — L3-wiring delta; CLAUDE.md authoritative)* — DCML-adjudicate **every** changed case; an
  **un-adjudicated BIR=false increase on any preset is a hard stop** (CLAUDE.md gate policy).
- **Snapshots:** `pipeline_snapshot_tests` goldens **will** move (4b changes the resolver, which is on
  the `.mscx`→resolve→sectionanalyzer→keyAreas→bridge-RN path — unlike 4a). Refresh **only**
  DCML-verified-correct diffs.
- **No hard key-axis pass-bar for 4b-i** — it is the floor *measurement*. The full-4b mode-absent
  pass-bar (OQ6) is set *after* seeing 4b-i's floor, so it is data-grounded, not guessed.

### 2.7 — 4b-i IMPLEMENTED + measured (2026-06-14) — HELD

The four demotions landed (keymodeanalyzer.cpp/.h: penalty 7.0→1.0 + bounds lower 3.0→0.0 + the
`ignoreDeclaredMode` toggle; keyresolver.cpp: piece-start anchor removed, strong declared-mode
promotion removed, `--ignore-declared-mode` clear). Full provenance + per-case adjudication in
`cc_stage4b_i_report.md`. Headline:

- **Demoting the 7.0 wall to a 1.0 hint is nearly free mode-present.** S2 (genuine key error, DCML L1):
  Default 685→**687** (+2), Baroque 683→**683** (0), Jazz 1937→**2002** (+65, Jazz key S2 unreliable —
  39–46% key-parse failures). **BIR gate byte-identical mode-present (57/23/57, 0 moved on all three
  presets).** Snapshots: 2 refreshed, both DCML-verified (corelli_op01n08a G/iv→**C/i** = matches DCML
  globalkey=c; chopin_bi105_op30_2 confidence-only 0.975→0.393, key unchanged). Suites green
  (composing 505 / notation 57 / snapshots 11/11).
- **The mode-absent floor collapses ~3×** (Default S2 687→**2070**, +1383; Baroque →**2099**, +1416).
  The declared mode is a near-total **relative-pair tiebreaker** crutch: note-based inference alone
  cannot resolve relative major/minor, so dropping it flips ~1383 near-tie regions. S1 (Default)
  2127→1205 mode-absent (−922) → the 242 S2→S1 gains of 4a do **not** hold without the crutch. This is
  a **finding, not a failure** (per §7) — it quantifies crutch-dependence and is the 4b-ii target.
- **Mode-absent BIR gate** moved (floor only, not shippable): Default 57→**58** (+bwv40.8@30720),
  Baroque swap (−bwv60.5@30960 +bwv40.8@30720), Jazz identical. All key-collapse artifacts —
  bwv40.8@30720 is **correct mode-present** (kConf 0.04 under the collapsed mode-absent key). DCML-
  adjudicated; no shippable-config regression (mode-present is byte-identical).
- **7 over-lock stems:** bwv365/bwv33.6 recover to a-minor **mode-absent only** (the 1.0 hint still
  over-locks them mode-present); bwv371(G)/bwv437(D)/bwv276(D, absent) recover the correct **tonic**
  (wrong church-mode flavor); bwv64.2/bwv83.5 do **not** recover any condition (note inference itself
  reads A-minor, disagreeing with DCML — needs 4b-ii note-term strengthening or is genuine ambiguity).

**4b-ii implication:** the floor↔ceiling gap is almost entirely **relative-pair disambiguation**.
Strengthen the relative-pair discriminators (triad/tonic salience, true leading tone,
`applyPairwiseDisambiguation`) so note-based inference resolves relatives without the declared crutch.

---

## §3 — Open-question dispositions (dossier §6)

| OQ | Disposition (4b-i unless noted) |
|---|---|
| 1 — hard-promotion demotion | Penalty → small additive hint (provisional 1.0, Stage-5-fit); **hard promotion removed**. Smallness = the "genuinely unsure" gate (only flips near-ties). |
| 2 — piece-start anchor | Remove the declared short-circuit; opening is note-based; residual declared influence = the §2.1 hint only. |
| 3 — partial-sig without trigger | **Deferred.** 4b-i keeps it declared-gated (mode-present only); note-triggered detector is a later sub-step. The 4 partial-sig stems are honestly unrecovered mode-absent. |
| 4 — cadence→key wiring | **Deferred.** Strengthen existing triad/LT/disambiguation terms in 4b-ii first; add cadence only if the floor needs it. |
| 5 — KeyArea extend | **Deferred to Stage 6** (area-level confidence + notated≠analytical carrier = label-contract work). KeyArea struct suffices for 4b. |
| 6 — mode-absent pass-bar | **Set after 4b-i's floor measurement** (data-grounded). Dossier's ≥70% of the +378 is the starting reference; **user ratifies the number** once the floor is known. |

---

## §4 — Behavior-change surface + ratification control

Expected, to be DCML-adjudicated and ratified — **not pre-decided**:
- The **57/23/57 BIR gate identity sets may move** on the chord axis (key feeds `basisIndep`). Every
  changed gate case adjudicated against DCML; un-adjudicated BIR=false increase = hard stop.
- **Chord-axis `.ours.json`** changes where the resolved key shifts.
- **Snapshot goldens** move; refresh only DCML-verified-correct (CLAUDE.md), report each with adjudication.
- `docs/scoring_model.md` / `back_half_design.md` synced if any scoring term/weight changes (CLAUDE.md sync rule).

The control is the ratification gate: 4b-i is HELD, Cowork verifies the report (every moved gate case +
snapshot adjudicated), user ratifies before commit.

---

## §5 — 4b-ii (directional) + deferred

- **4b-ii:** strengthen the relative-pair discriminators identified in the dossier §2 — `triadScore`
  weighting (tonic 1.60 / completeTriad 2.50 / missingTonic −2.50), `trueLeadingToneBoost` (1.20), and
  `applyPairwiseDisambiguation` (4.50/1.50/1.00) — to lift the mode-absent floor toward the mode-present
  ceiling. Structure + provisional weights in 4b-ii; final weights are Stage 5's fit. Measured the same
  way (mode-present AND absent); pass-bar from OQ6.
- **Deferred sub-steps:** note-triggered partial-sig detector (recovers bwv83.5/276/371/437 mode-absent);
  cadence→key wiring (new composing term feeding `analyzeKeyMode`); KeyArea area-confidence (Stage 6).

---

## §6 — For user ratification

1. **Approve the staged plan** (4b-i demote+measure → 4b-ii strengthen → deferred) and the §3 OQ
   dispositions.
2. **Confirm OQ1's "remove the hard promotion outright"** (vs. keep a vestigial gated version). Recommended:
   remove — it is a veto incompatible with note-based-primary.
3. **OQ6 pass-bar is deferred to post-4b-i by design** — confirm you're content to set the mode-absent
   survival threshold once the floor is measured, rather than now.
4. **Provisional declared-hint weight = 1.0** for measurement (Stage 5 fits the final). Confirm or set a
   different provisional.

On ratification, Cowork writes the 4b-i CC instruction (demote the four mechanisms + the
`--ignore-declared-mode` toggle + the dual-condition measurement; HELD, ratification-gated).

---

## §7 — Stop conditions (for the 4b-i implementation, when it runs)
- Any need to edit a `src/notation`/`src/engraving` **production** file (the scoping says none — if one
  appears, STOP and surface for authorization).
- An un-adjudicated BIR=false increase on any preset (ratification stop).
- The mode-absent floor collapsing far below the mode-present win **is a finding, not a failure** — it
  quantifies crutch-dependence and shapes 4b-ii; report it, do not paper over it.
