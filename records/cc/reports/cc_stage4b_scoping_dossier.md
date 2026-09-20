# Stage 4b Scoping Dossier — note-based mode/key as the PRIMARY signal, declared mode demoted

> **READ-ONLY scoping run (2026-06-14).** No `src/` file edited; no build; no commit. Produces the
> exact off-limits file-set for the user to authorize before any Stage-4b code is written. Every
> empirical claim is tagged `[code]` (read in source, file:line quoted) / `[probe]` (measured) /
> `[unknown]` (stated, not guessed). Base HEAD `faa1ee5388` (Stage-4a committed this run).
>
> **Design ratified in** `docs/back_half_design.md` §4 step 2 (the 2026-06-14 ★ REDIRECT): make
> **note-based major/minor inference PRIMARY**, **REMOVE the −7 declared-mode wall** (not grade it),
> demote declared mode to a **low-weight droppable tiebreaker** consulted only when note-based
> inference is genuinely unsure. Stage 4a (committed) made the declared mode *available* on the
> corpus; it is NOT the inference mechanism.

---

## §0 — Headline scoping result (the one thing the user needs)

**Stage 4b can be implemented with ZERO edits to any off-limits (`src/notation/`, `src/engraving/`)
production file.** [code] Every piece of the design lives in the **composing autonomous zone**:

- The declared-mode influence (the "−7 wall") is **three** composing-zone mechanisms, not one (§1).
- The note-based inference is entirely in `keymodeanalyzer.cpp` (§2).
- **KeyArea already exists** — struct in `analyzed_section.h`, built in composing's
  `sectionanalyzer.cpp`, already plumbed through the notation bridge as **pure consumption** (§3).
- Key/mode stabilization (`stabilizeHarmonicRegionsForDisplay`) is composing-only (§3).

The notation bridge **renders** the already-decided key (RNs from KeyArea); it performs **no key
inference**, so Stage 4b does not touch it. The only notation-zone artifacts that move are **test
goldens** (`pipeline_snapshot_tests/snapshots/*.json`), refreshed via `--update-goldens` — test
data, not production code (§5). **The §3 authorization-request table is therefore empty of
production files** — the user is asked to authorize a *test-golden refresh*, not a notation source edit.

---

## §1 — The −7 wall, located and characterized [code]

The declared mode is `keyResolver`'s `declaredMode`, derived from the engraving `KeySigEvent.mode()`
at [keyresolver.cpp:224-239](src/composing/analysis/key/keyresolver.cpp#L224) (the
`EMode::MAJOR/MINOR/...` → `KeySigMode` switch). It then drives **three distinct, independently-firing
mechanisms** — Stage 4b's "remove the wall" must address **all three**, not just the penalty:

### 1a. The −7 penalty proper — `declaredModePenalty = 7.0` [code]
- **Default:** [keymodeanalyzer.h:319](src/composing/analysis/key/keymodeanalyzer.h#L319) —
  `double declaredModePenalty = 7.0;  ///< Penalty for modes outside the declared class [empirical]`.
  Bounds `{3.0, 15.0, true}` (isManual) at [keymodeanalyzer.h:454](src/composing/analysis/key/keymodeanalyzer.h#L454).
- **Applied:** [keymodeanalyzer.cpp:571-577](src/composing/analysis/key/keymodeanalyzer.cpp#L571) —
  inside the 252-candidate `(tonicPc, modeSlot)` loop, *subtracted* from `eval.score` for every
  candidate whose mode is not `modeIsCompatibleWithDeclared(candidate, *declaredMode)`:
  ```cpp
  if (declaredMode.has_value()) {
      const KeySigMode candidate = keyModeFromIndex(modeIndex);
      if (!modeIsCompatibleWithDeclared(candidate, *declaredMode)) {
          eval.score -= prefs.declaredModePenalty;   // the −7 wall
      }
  }
  ```
  `modeIsCompatibleWithDeclared` ([keymodeanalyzer.cpp:~500-513](src/composing/analysis/key/keymodeanalyzer.cpp#L500)):
  Ionian declared ⇒ accept any major-class mode; Aeolian ⇒ any minor-class; specific mode ⇒ exact match.
- **Dump term:** surfaced as `declaredPenalty` (a `KeyCandidateScore` field) in the read-only
  `--dump-key-candidates` instrument [keymodeanalyzer.cpp:777,789](src/composing/analysis/key/keymodeanalyzer.cpp#L777)
  and documented at [keymodeanalyzer.h:157](src/composing/analysis/key/keymodeanalyzer.h#L157). This is
  the term the key-emission dossier inspects. **−7 ≈ −7.0 SUBTRACTED**; it dwarfs the strongest single
  note-based term (`disambiguationTriadBonus = 4.50`, `tonicWeight = 1.60`), so on a relative-pair tie it
  is decisive — the "wall."

### 1b. The hard post-hoc promotion — "Strong declared-mode prior" [code]
- [keyresolver.cpp:344-367](src/composing/analysis/key/keyresolver.cpp#L344). **Even with the −7
  penalty removed**, this *separately* forces declared-mode compliance: if the resolver's winner
  (`results.front()`) is incompatible with the declared class, it calls `promoteWinnerInPlace(...)` to
  hoist the highest-ranked **compatible** candidate to the front — **regardless of score gap**. It is a
  second, harder wall (a hard veto, not a −7 nudge). Comment self-describes: *"the composer's intent
  overrides note-content inference."* **Stage 4b must demote/remove this too**, else removing 1a alone
  changes nothing for any case where note-based inference already out-scored the declared mode but got
  overridden here.

### 1c. The piece-start anchor — declared-mode seed [code]
- [keyresolver.cpp:274-287](src/composing/analysis/key/keyresolver.cpp#L274). When `prevResult == nullptr`
  and a declared mode exists and we are inside the opening lookback window, the resolver **short-circuits
  the entire note-based analysis** and returns a single declared-mode result with
  `score = prefs.relativeKeyHysteresisMargin`, `path:"anchor"`. The next region must beat that margin via
  hysteresis (§ below) to switch away. This is a *soft* seed (not a veto), but it is **declared-mode-sourced**
  and is exactly the mechanism the 4a report credits for the bwv153.9 win (`path:"anchor"`, S2→0). Stage 4b's
  "note-based primary" must replace this seed with a note-based opening anchor when note evidence is sufficient.

### 1d. Partial-signature correction is also declared-mode-gated [code]
- [keyresolver.cpp:248-251](src/composing/analysis/key/keyresolver.cpp#L248): `partialSignatureCorrection`
  only runs `if (declaredMode.has_value())`. So a mode-absent condition (§4) **disables** it. The Baroque
  partial-sig targets among the 7 over-lock stems (bwv83.5/276/371/437) depend on the declared mode existing
  → Stage 4b cannot recover them purely by "removing the wall"; the note-based inference (or a note-triggered
  partial-sig detector) must reach those tonics without the declared-mode trigger. **Flag for design.**

**Removal is purely a composing-zone change [code].** All four mechanisms live in
`src/composing/analysis/key/{keymodeanalyzer,keyresolver}.{h,cpp}` — the autonomous zone. No
`src/notation` or `src/engraving` file reads or writes the penalty/prior/anchor. Confirmed: the only
non-composing caller is the notation bridge ([notationcomposingbridgehelpers.cpp:186](src/notation/internal/notationcomposingbridgehelpers.cpp#L186)),
which passes `prefs` in and consumes `ranked.front()` out — it never references `declaredModePenalty`
or the promotion. `[code]`

---

## §2 — The current note-based mode/key inference, inventoried [code]

All in `KeyModeAnalyzer::analyzeKeyMode` ([keymodeanalyzer.cpp:519](src/composing/analysis/key/keymodeanalyzer.cpp#L519)),
which evaluates **252 candidates** (12 tonics × 21 modes) and sums **six orthogonal terms** per candidate
([keymodeanalyzer.cpp:559-569](src/composing/analysis/key/keymodeanalyzer.cpp#L559)). Defaults from
`KeyModeAnalyzerPreferences` ([keymodeanalyzer.h:172-381](src/composing/analysis/key/keymodeanalyzer.h#L172)):

| Term | Function | Default weight(s) | Strength on the 0-sig major/minor call |
|---|---|---|---|
| Scale membership | `scoreScaleMembership` | inBoth 1.00 / candOnly 0.25 / keySigOnly −0.20 / neither −0.05 | **Weak discriminator** for relative pairs: C-major and A-minor share the *same* diatonic set, so scale membership is near-identical for the relative pair. |
| Triad evidence | `scoreTriadEvidence` | tonic 1.60, third 0.70, fifth 0.50, LT 0.40; completeTriad **+2.50**, missingTonic **−2.50**; extraScale 0.10 (cap 5.0) | **The strong link.** Tonic presence + complete-triad/missing-tonic is what actually separates C from a. This is where "strengthen note-based inference" should concentrate. |
| Characteristic pitch | `scoreCharacteristicPitch` | boost +1.80 / penalty −0.60 | Distinguishes modal members (Dorian ♮6 etc.); weak on the plain major/minor axis. |
| True leading tone | `scoreTrueLeadingTone` | boost +1.20 | Semitone-below-tonic; strong tonic indicator, **directional** (helps pick which of the relative pair is tonic). A second strong link. |
| Key-signature proximity | `scoreKeySignatureProximity` | per-step penalty 0.60 | Anchors to the *fifths* (the reliable signal per the design); does NOT separate the relative pair (same fifths). |
| Mode prior | `scoreModePrior` | **Ionian +1.20, Aeolian +1.00** (Δ=0.20), modal/exotic negative | The ±0.20 major-vs-minor prior the design references. **Weak** (0.20) by design — it should stay weak; it is NOT the lever. |

**Two post-hoc refinements (also note-based):**
- **Pairwise disambiguation** [keymodeanalyzer.cpp:581-607](src/composing/analysis/key/keymodeanalyzer.cpp#L581):
  on the top-2 modes sharing the signature, `applyPairwiseDisambiguation` applies
  `disambiguationTriadBonus +4.50` / `Cost −1.50` / `TonicBonus +1.00` ([keymodeanalyzer.h:305-307](src/composing/analysis/key/keymodeanalyzer.h#L305)).
  **This is the strongest existing relative-pair discriminator** and the most promising lever to strengthen.
- **Tonal-centre family selection** [keymodeanalyzer.cpp:619-667](src/composing/analysis/key/keymodeanalyzer.cpp#L619):
  `tonalCenterScore` (tonic 2.20 / third 1.00 / fifth 0.70 / LT 0.50 / triad 2.00, Δ-threshold 0.25,
  [keymodeanalyzer.h:281-286](src/composing/analysis/key/keymodeanalyzer.h#L281)) picks the winner among
  modes sharing the signature, guarded so it cannot overturn a materially stronger raw winner.

**What "strengthen note-based inference" concretely means, and WHERE [code]:** the weak link on the
0-sig relative-pair decision is **not** scale membership or mode prior (both near-symmetric on the
relative pair); it is the **tonic/triad-salience + leading-tone + pairwise-disambiguation** complex.
Concretely Stage 4b strengthens some subset of: `triadScore` weighting (1.60/2.50/−2.50),
`trueLeadingToneBoost` (1.20), `applyPairwiseDisambiguation` (4.50/1.50/1.00), and possibly cadence
evidence (the design names "cadence evidence" — **[unknown]: no cadence term currently feeds
`analyzeKeyMode`**; cadence detection exists elsewhere in composing but is not wired into key scoring —
adding it is new composing-zone work). **All of these are in `keymodeanalyzer.{h,cpp}` — the autonomous
zone.** The fitting of the final weights is explicitly Stage 5's job (the fitter), per the design.

**Autonomous-zone statement (explicit):** every proposed change in §1 and §2 — remove/demote the
penalty (1a), demote the hard promotion (1b), replace the anchor seed (1c), re-source partial-sig (1d),
strengthen triad/LT/disambiguation/cadence (§2) — is **inside `src/composing/`**, which CLAUDE.md
pre-authorizes. **None is outside the autonomous zone.**

---

## §3 — KeyArea spans + stabilization: the off-limits surface — **already built, pure consumption** [code]

**Finding: the off-limits surface is empty of production files; KeyArea is not new work.**

| Concern | Where it lives | Zone | Stage-4b change |
|---|---|---|---|
| `KeyArea` struct (startTick/endTick/keyFifths/mode/confidence) | [analyzed_section.h:118-137](src/composing/analyzed_section.h#L118) | **composing** | none (struct sufficient; design may add an area-level confidence — composing edit) |
| KeyArea construction (confidence-gated grouping, 0.8 threshold) | [sectionanalyzer.cpp:920-957](src/composing/analysis/section/sectionanalyzer.cpp#L920) | **composing** | re-tunes naturally as inference changes; no structural edit forced |
| Key/mode **stabilization + hysteresis** (`stabilizeHarmonicRegionsForDisplay`) | [sectionanalyzer.cpp:911](src/composing/analysis/section/sectionanalyzer.cpp#L911) (defined in same file; grep confirms it exists **only** in composing) | **composing** | the hysteresis behavior shifts with the demoted prior; composing edit |
| Per-region key resolve + `prevResult` chaining (region-to-region hysteresis carrier) | [regionanalyzer.cpp:306-309, 418](src/composing/analysis/region/regionanalyzer.cpp#L306) | **composing** | none forced |
| Hysteresis margins (`hysteresisMargin`, `relativeKeyHysteresisMargin`, both 2.0) | [keymodeanalyzer.h:360-366](src/composing/analysis/key/keymodeanalyzer.h#L360); applied [keyresolver.cpp:320-342](src/composing/analysis/key/keyresolver.cpp#L320) | **composing** | may retune; composing edit |
| **Bridge: carry KeyArea to consumers** | [notationcomposingbridge.cpp:283-287](src/notation/internal/notationcomposingbridge.cpp#L283) (populate `enclosingKeyArea` from `keyAreaId`) | `src/notation` (OFF-LIMITS) | **none — already wired, pure pass-through** |
| **Bridge: render RNs in KeyArea key** | [notationcomposingbridge.cpp:1116-1141](src/notation/internal/notationcomposingbridge.cpp#L1116) | `src/notation` (OFF-LIMITS) | **none — generic "roman key ≠ per-region key" re-contextualization already handles whatever key Stage 4b decides** |
| Bridge call into resolver | [notationcomposingbridgehelpers.cpp:186-195](src/notation/internal/notationcomposingbridgehelpers.cpp#L186) | `src/notation` (OFF-LIMITS) | **none — passes `prefs` in, consumes `.front()` out** |

**The minimal off-limits set is ∅ (zero production files).** [code] The notation bridge already:
(a) consumes the composing-built `KeyArea` (`enclosingKeyArea` populated from `keyAreaId`), and
(b) renders Roman numerals from the enclosing KeyArea's key via a **generic** mechanism that re-derives
degree/function for *whatever* key composing decides ([notationcomposingbridge.cpp:1133-1141](src/notation/internal/notationcomposingbridge.cpp#L1133)).
Stage 4b changes *which key composing decides*, not the rendering contract — so the bridge needs no edit.
This matches the design's own "favor having engraving import RETAIN the mode … the resolver gets the mode
as a data value" and "KeyArea computed in composing, only thin bridge plumbing in notation" — **and that
thin plumbing already exists.**

**Authorization request:** **no `src/notation/` or `src/engraving/` production-file edit is required.**
The only off-limits-zone artifacts that change are **test goldens** (§5) — the user is asked to authorize
a snapshot-golden refresh, which CLAUDE.md already covers via `pipeline_snapshot_tests --update-goldens`.

---

## §4 — Measurement plan, under BOTH conditions [probe-design]

Stage 4b must be measured **mode-present AND mode-absent**, or it overfits to a corpus input (the
declared `<mode>`) the shipped product usually lacks (the design's core warning — #9444 is hiding the UI;
native `.mscz` may not carry it).

### 4.1 Producing the mode-absent condition
Three options, in preference order:
1. **A `batch_analyze` flag `--ignore-declared-mode` (recommended) [probe-design].** `batch_analyze.cpp`
   is in `tools/` (NOT off-limits — only `src/notation`/`src/engraving` editing is forbidden; composing +
   tools are writable). The flag forces `declaredMode = std::nullopt` into the resolver path. Deterministic,
   reversible, no corpus mutation, lets the *same* corpus be scored both ways. **Note:** the resolver derives
   `declaredMode` internally from `KeySigEvent.mode()` ([keyresolver.cpp:224-239](src/composing/analysis/key/keyresolver.cpp#L224)),
   so the toggle needs either a `prefs`/parameter to suppress it or a resolver overload — a small composing+tools edit (in-zone), built at implementation time, **not in this read-only run**.
2. **Corpus strip [probe-design].** Score a copy of the `.xml` Bach corpus with `<mode>` stripped (or
   simply the pre-4a binaries, where the mode was dropped at import). No code, but mutates corpus inputs —
   use only as a cross-check on option 1.
3. **`.mscz`/native-load probe [unknown]:** whether native load even carries the mode is the design's open
   "Build-confirm." Out of scope for the metric, but the mode-absent condition is the *conservative proxy*
   for it regardless.

### 4.2 Metric rung and unit
- **L1 `--key-breakdown`** on the corrected DCML-only, **granularity-robust** unit (the committed
  `f8c6b3932a` / re-baselined `a96f179f40` instrument). The 57/23/57 BIR gate is the **chord-axis**
  guard (§5). Key axis measured by the S1/S2/S3/S4 functional decomposition (`cc_functional_residual_dossier.md`
  vocabulary), as in the 4a report's S2 table.
- **Granularity caveat** (CLAUDE.md Stage 2.2-i): the gate is batch-region granularity; per-beat root
  error is ~7× higher. Report both if the section-level view (`batch_analyze --section-level`) is informative,
  but the **gate** stays at batch granularity.

### 4.3 Concrete targets to RECOVER (from `cc_stage4a_mode_import_report.md`)
- **The 7 over-lock stems** [4a report §4.4]: **bwv64.2** (S2 1→20, reads Emin = relative of DCML G-major),
  **bwv365** (4→7, C↔a), **bwv33.6** (14→16, C↔a), **bwv83.5** (10→13, partial-sig d-min), **bwv276**
  (19→21, partial-sig), **bwv371** (13→15, partial-sig G), **bwv437** (15→17, partial-sig d-min). These
  regressed under 4a precisely because the **−7 wall over-committed to the notated key** when notation ≠ DCML.
  Stage 4b's removal + note-based primary should recover them (note evidence points at the DCML tonic).
  **bwv64.2 is the stress case** (+19; demands the note-based inference reach G-major/E-minor against the
  notated 0/minor). bwv83.5/276/371/437 additionally need §1d (partial-sig reachable without the declared trigger).
- **The 242 S2→S1 cases** [4a report line 145-149]: regions the 4a import fix moved from key-disagreement
  (S2) into tonicization-label-gap (S1 = root+global-key correct, only the `V/V`-class label missing,
  Stage-6's domain). Stage 4b must **hold these in S1 WITHOUT the declared-mode crutch** — i.e. note-based
  inference alone must keep the global key correct on these 242.

### 4.4 Must-NOT-regress (the real test)
- The 4a **47 improved + 19 neutral / net S2 −378 (Default)** [4a report §4.4] should **largely survive
  mode-ABSENT**. That is the genuine pass/fail: if the win collapses when the declared mode is removed, the
  inferrer was leaning on the crutch and is not shippable. **Framing:** Stage 4b *passes* iff (a) mode-absent
  S2 win is ≥ a stated fraction (design to set, e.g. ≥70%) of the −378, AND (b) the 7 over-lock stems do not
  regress further, AND (c) the chord-axis 57/23/57 gate is DCML-adjudicated (it WILL move — §5), AND (d) no
  new BIR=false identity appears un-adjudicated. **Mode-present** is the upper-bound sanity check (the crutch
  ceiling), not the ship metric.

---

## §5 — Behavior-change surface (called out, not pre-decided)

Stage 4b is the project's **2nd intentional behavior change** (4a was the 1st). Because **resolved key
feeds chord emission** — `analyzeChord`'s `basisIndep` consumes the key/mode (the design's
"byte-identity era ends"), and the notation bridge renders RNs off the KeyArea key
([notationcomposingbridge.cpp:1129-1141](src/notation/internal/notationcomposingbridge.cpp#L1129)) —
**byte-identity ends on the CHORD axis too, not just the key axis.** Expected consequences, to be
**DCML-adjudicated and ratified, not pre-decided**:

- The **57/23/57 BIR gate identity sets may move** (CLAUDE.md gate policy: any BIR=false increase in any
  preset is a hard stop *until adjudicated*; every changed case adjudicated against DCML).
- **Chord-axis `.ours.json`** will change on stems where the resolved key shifts.
- **`pipeline_snapshot_tests` goldens WILL change** — unlike 4a. The 4a report §5 notes the snapshot corpus
  loads `.mscx` directly via `ScoreRW::readScore`, **bypassing the MusicXML importer**, so 4a (an import-path
  fix) could not reach it (0 golden diffs). **Stage 4b changes the RESOLVER (composing)**, which IS on the
  `.mscx` → `resolveKeyAndModeRanked` → `sectionanalyzer` → `keyAreas` → bridge-RN path, so the snapshot
  `keyAreas[]` arrays and RN annotations **will** move. Refresh via `pipeline_snapshot_tests --update-goldens`
  **only after the output change is DCML-verified correct** (CLAUDE.md). This golden refresh is the *only*
  off-limits-zone (test-data) artifact touched.

This is **expected and flagged, not pre-resolved.** The ratification gate (DCML-adjudicate every moved
gate case + every moved snapshot) is the control.

---

## §6 — Open questions for Cowork/user (need a decision before implementation)

1. **Demotion target for the hard promotion (§1b).** Removing the −7 penalty (1a) is clear; the design says
   "droppable tiebreaker." Does the hard post-hoc promotion at [keyresolver.cpp:350-367](src/composing/analysis/key/keyresolver.cpp#L350)
   get **removed outright**, or **converted** to a small additive tiebreaker that only fires when the
   note-based top-2 gap is below a confidence threshold? **"Genuinely unsure" must be defined** — proposed:
   `normalizedConfidence < dynamicLookaheadConfidenceThreshold (0.60)` OR top-1/top-2 raw gap < a new
   `declaredHintGap`. Needs a number (Stage 5 can fit it, but a provisional is needed to measure).
2. **The piece-start anchor (§1c).** Replace the declared-mode seed with a **note-based opening anchor**
   (run `analyzeKeyMode` on the opening window and seed from it), or keep a *weak* declared seed as the
   droppable hint only when opening note evidence is sparse? Affects bwv153.9-class wins.
3. **Partial-signature without the declared trigger (§1d).** `partialSignatureCorrection` is gated on
   `declaredMode.has_value()`. Under mode-absent, bwv83.5/276/371/437 lose it. Decide: (a) re-trigger
   partial-sig from note evidence (a Dorian/Mixolydian-signature note pattern detector), or (b) accept those
   4 as out-of-scope for mode-absent and target them only mode-present. Material to §4.3's recovery claim.
4. **Cadence evidence wiring [unknown].** The design names "cadence evidence" as a note-based term, but no
   cadence term currently feeds `analyzeKeyMode` (§2). Build cadence→key wiring now (new composing work,
   larger), or strengthen the existing triad/LT/disambiguation terms first and defer cadence? Sizing decision.
5. **KeyArea: extend now or defer?** KeyArea exists and suffices structurally (§3). Does Stage 4b add an
   area-level confidence / "notated key ≠ analytical key" carrier now (for the 127 convention cases and
   Stage 6's label contract, per design OQ-3), or defer to Stage 6? Composing-only either way.
6. **Mode-absent pass threshold (§4.4).** What fraction of the −378 win must survive mode-absent to pass?
   The design must set this number before measurement is meaningful.

---

## §7 — Stop-conditions check (Task 2)
- ✅ READ-ONLY honored: no `src/` edit, no build, no commit.
- ✅ The −7 wall **is** where the dossier expected (`keymodeanalyzer.cpp:575`, penalty `keymodeanalyzer.h:319`) —
  plus two additional declared-mode enforcers (§1b/1c) the single-"wall" framing understated; reported.
- ✅ Measurement is achievable read-only at design time; the mode-absent toggle is a *future* composing+tools
  edit (in-zone), not an off-limits one — **no off-limits edit is needed even to measure.**
- ✅ No off-limits production file must be edited (the surface is ∅; only test goldens move — §5).

*Deliverable complete. Implementation is a later instruction, gated on the user authorizing §3 (here: a
test-golden refresh, no production off-limits edit) and resolving the §6 open questions.*
