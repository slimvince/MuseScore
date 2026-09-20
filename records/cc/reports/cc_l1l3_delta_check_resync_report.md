# CC — L1–L3 spec↔as-built delta-check (Phase-5 sign-off re-run) — READ-ONLY

> **Scope.** Ledger item E15: before the **L1–L4 COMPLETE** gate, confirm the L1–L3 **design docs match the
> as-built**, so Cowork can sync exactly what diverged. **READ-ONLY — findings only; no source/doc edits were made.**
> Method: read each design doc against the as-built source, citing doc-section ↔ file:line. Verdicts: **OK** (doc
> matches code), **STALE** (doc describes something no longer true), **MISSING** (built capability absent from the
> doc), **DIVERGENCE** (doc says X, code does Y). Possible *code* defects (code wrong vs design intent) are flagged
> separately in §4.
>
> **Headline.** The as-built **contracts** match the designs at every layer. The deltas are almost entirely
> **doc-staleness of build-status**: three capabilities the prose still calls "not yet built / no code" — L1 `extend`,
> L2's loaded-span clip, the L3 reach-back loop, and the L1.5 spelling primitive — **are in fact built and (for the
> slicer/decoder) live**. No new code-vs-intent defect was found; the two known latent items are already on record.

---

## §1 — Per-layer delta-check

### L1 — `cowork_layer1_note_model_design.md` ↔ `notemodel/note_model.{h,cpp}`

| Doc location | Code location | Verdict |
|---|---|---|
| §3/§5/§7 `build` from the selected music; §13 "cue note" flag specified-then-removed | `note_model.h:177` `build(sc)`, `:184` `build(sc,lo,hi)`; `note_model.cpp:89–116`; `note_model.h:71–79` (isCue omission, same rationale) | **OK** — both overloads present; degenerate whole-score delegates to the span overload (`note_model.cpp:95–96`); isCue removal matches §13. |
| §7 "eleven facts" per note record (sounding pitch, spelled pitch, staff, voice, start, end, duration, grace, sounds, visible, staff-eligible) | `note_model.h:80–92` `NoteEvent` = `pitch, tpc, staff, voice, onset, release, duration, isGrace, plays, visible, staffEligible` (11 fields) | **OK** — 1:1. "spelled pitch" = `tpc`. |
| §11 "build currently reads the whole score … interim behaviour, not the target" | `note_model.h:159–163` + `note_model.cpp:118–125` "PHASE 1a (interim) — extend() re-walks the whole score and re-filters" | **OK** — interim rebuild acknowledged identically on both sides. |
| **§3 (the *Widen the covered span* bullet): "This is the **extend** operation … (Designed, not yet built — verified 2026-06-24: no extend operation exists in the note model …)"** (`:96–102`); **§11: "Fixing this and building *extend* are one coupled change"** (`:201–206`) | **`extend(Direction, int)` IS built** — `note_model.h:169` `enum Direction{Earlier,Later}`, `:194` `extend(...)`, `:204` `boundaryReached()`; impl `note_model.cpp:204–237`; accessors `loadedStart/End`, `selectionStart/End` `note_model.h:199–204` | **STALE** — the design's most load-bearing staleness. `extend` + `boundaryReached` + the loaded/selection-span accessors exist and behave as the contract specifies (append-only, clamps at score bound, one step, no convergence loop). The §11 framing "build-whole-score fix + extend are *one coupled change*" is also superseded: `extend` was built **decoupled** as Phase-1a (it itself re-walks the whole score — `rebuildForLoadedSpan`), with the span-scoped walk deferred to Phase 1b. |

**L1 verdict:** the as-built **contract is the doc's contract**. Only the build-status notes in §3/§11 (extend "not yet
built") are STALE.

---

### L1.5 — `cowork_tpc_capability_design.md` ↔ `engravingbridge/spellingview.{h,cpp}` (+ derived-view seam)

| Doc location | Code location | Verdict |
|---|---|---|
| **Status line: "DRAFT for sign-off. Read-only design — no code." (`:2–3`)** | `spellingview.{h,cpp}` are built and unit-tested (`tests/spellingview_tests.cpp`) | **STALE** — the primitive is built; the "no code" status header is obsolete. |
| §1 per-note `lineOfFifths` / `sharpFlatSense`; §1 aggregate `spanSpelling` (signature-agnostic centroid + sharp/flat distribution) | `spellingview.h:81` `lineOfFifths(int)`, `:86` `sharpFlatSense(int)`, `:94–103` `SpanSpelling`/`spanSpelling(...)`; impl `spellingview.cpp:36–76` | **OK** — shape matches exactly: per-note + aggregate, two reads of one interpretation. |
| §1 "test presence with `tpcIsValid()` (= −8 ≤ tpc ≤ 40), never `>=0`/`!=−1`"; lof = `tpc − TPC_C`, `TPC_C=14` | `spellingview.cpp:38` `tpcIsValid(tpc)` guard, `:41` `tpc − Tpc::TPC_C`; `spellingview.h:60–74` (range/guard rationale) | **OK** — single `tpcIsValid` presence test in `lineOfFifths`; `sharpFlatSense`/`spanSpelling` derive from it (the unification rule). |
| §4/§7 "no production consumer yet (capability only); any movement → STOP"; §6 "lives in the engravingbridge derived-view seam beside weightedPcView/soundingAt" | `spellingview.h:24–51` ("Capability only (Phase 4): nothing in production consumes this yet"); module is in `engravingbridge`; **grep confirms** only the build (`CMakeLists`), the test, and the primitive itself reference it — **no production consumer** | **OK** — capability-only is true and is marked as such. |
| §1/§5 "Latent L1 caveat (recorded, NOT fixed here): `NoteEvent.tpc` default `−1` is also a real Fbb; the `0–34` comment is wrong (real range −8…40); clean L1 fix = default `TPC_INVALID` + correct the comment — record for the L1 cleanup pass, do **not** fold into Phase 4" (`:88–99`) | `note_model.h:82` still `tpc = −1` default with comment **"(0-34, circle-of-fifths spelling). -1 = not provided."**; same stale comment echoed at `analysistypes.h:136` (`ChordAnalysisTone.tpc`) | **OK (deferred, on record)** — the code matches the design's *instruction* (don't fix in Phase 4). The inaccurate `0-34` comment + `−1` default remain an **un-actioned L1-cleanup item**; flagged here so the L1 as-built pass picks it up (see §4 latent item). |

**L1.5 verdict:** the primitive is **doc-accurate and correctly marked capability-only with no production consumer**.
Only the doc's "no code" status header is STALE; the recorded L1 `tpc` cleanup is still pending.

---

### L2 — `cowork_layer2_slicing_design.md` + `cowork_layer2_reslice_design.md` ↔ `slicing/slicer.{h,cpp}`

| Doc location | Code location | Verdict |
|---|---|---|
| Slicing-spec §1/§4/§5: boundaries = sorted-unique union of every eligible onset+release; consecutive boundaries form slices; explicit empty slice for interior silence; <2 boundaries → empty | `slicer.cpp:37–61` (collect eligible onset+release, sort-unique, `<2` early-out), `:99–106` (consecutive-boundary tiling) | **OK** — pure, stateless, zero-interpretation, byte-for-byte the spec. |
| Slicing-spec §3/§7 `Slice` = `[start,end)` only, notes fetched on demand; reslice §5 "keep the `Slice` minimal … compute selection-vs-context at the consumer. **Decision to confirm at build.**" | `slicer.h:82–85` `struct Slice { int start; int end; }` (no notes, no in/out-selection tag) | **OK** — the §5 build-time decision was taken: `Slice` is minimal; no selection-vs-context annotation on it. |
| Reslice §2 clip rule `[max(loadedStart, firstEligibleOnset), min(loadedEnd, lastEligibleRelease))`, clip the **multiset** (drop out-of-range boundaries, inject the two endpoints); degenerate whole-score = inert/byte-identical | `slicer.cpp:63–97` — `clipStart/clipEnd` (`:81–82`), `remove_if` out-of-range (`:83–86`), inject endpoints + re-unique (`:87–90`), degenerate-collapse guard (`:95`); "INERT ON WHOLE-SCORE" comment `:74–80` | **OK** — exact implementation of the reslice §2 design decision, incl. the multiset clip and the inert-on-whole-score property. |
| **Reslice status: "DRAFT for sign-off. Read-only design — no code." (`:3`)** | clip is built (`slicer.cpp:63–97`) and tested (per ARCHITECTURE.md CP1–CP7) | **STALE** — clip is built; "no code" header obsolete. |
| **Slicing-spec §2: "Not yet connected into the live analysis pipeline … built and tested on its own; it does not yet change any analysis output"** (`:45–46`); **§10 "Isolation check … not yet connected … outputs are unchanged"** (`:151–152`); **§11 "Not yet connected … isolated until Architectural Layer 3 reads slices"** (`:162–163`) | **L3 now reads the slices live:** `regionanalyzer.cpp:579` `slices = changePointSlices(noteModel)` → `:581–583` `KeyModeSequenceDecoder::decode(slices, …)`, whose `sliceKeys` drive `localKeyForRegion` (`:684–730`). The slicer header `slicer.h:67–69` **still** says "It is NOT wired into the live analysis pipeline … changes no analysis behavior." | **STALE / DIVERGENCE** — the spec's central "isolated / not yet connected" status (§2, §10, §11) **and** the `slicer.h:67–69` header comment are obsolete. L3 was rebuilt to read slices (the spec's own retirement trigger), so L2 is connected. Nuance: L2's *clip* is byte-identical on whole-score; the analysis movement (the ratified L3-wiring BIR −4/+1/−4) came from L3's *consumption*, not from the slicer itself. So "L2 changes no analysis output" is defensible *in isolation*, but "not wired into the live pipeline" is now false. |

**L2 verdict:** the slicing **algorithm + clip contract** match exactly. The pervasive **"isolated / not-yet-wired"
status** across the slicing spec (§2/§10/§11), the reslice "no code" header, and the `slicer.h` module comment are
**STALE** — the slicer is wired and consumed by L3.

---

### L3 — `cowork_layer3_keymode_design.md` + `cowork_layer3_reachback_design.md` ↔ `key/*` + `regionanalyzer.cpp`

| Doc location | Code location | Verdict |
|---|---|---|
| Keymode §3/§5: emission = reuse `KeyModeAnalyzer` unchanged over a per-slice window built via the L1 indexed query (`pitchContextOverSpan`, declared in `regiontonecollector.h`, defined in `regiontoneprimitives.cpp`); decoder = dedicated key Viterbi | `keymodesequence.h:204–211` `decode(...)`; `regiontonecollector.h:270` declares `pitchContextOverSpan`; emission reuses `analyzeKeyMode` (header `:36–67`) | **OK** — the emission scorer, the indexed window view, and the dedicated Viterbi are exactly as designed. |
| Keymode §3/§5/§7: per-slice result = chosen + ranked alternatives + confidence(sequence-margin) + "uncertain"; `redecodeRange` holds the two ends fixed and reproduces the matching slice of a full decode | `keymodesequence.h:151–158` `SliceKeyMode`; `:204` `decode`, `:221` `redecodeRange`, `:243` `decodeLattice`, `:253` `changeCost` | **OK** — data design + sub-range re-decode match §3/§7. |
| Keymode §Status "WIRED — AS-BUILT, Step 1": decoder replaces the per-region resolver at the `regionanalyzer.cpp` seam; duration-majority per coarse region; `excludeStaves` + `resolveKeySignatureContext` + C1 emission-confidence fidelity ties | `regionanalyzer.cpp:556–583` (whole-score decode at the Pass-1 seam, 3 fidelity ties), `:684–730` `localKeyForRegion` (duration-majority); `keymodesequence.h:74–86` (WIRING comment) | **OK** — the live wiring matches the keymode §Status description, incl. the three fidelity ties. |
| Keymode §11 ★ "Brittle leading-tone presence-gate … hard-gated on a `>0.1` window weight (`keymodeanalyzer.cpp:344,374`)" — a known non-Bach regression, fix scheduled for Phase 4 | `keymodeanalyzer.cpp:339` `has1 = weight1 > 0.1` (characteristic pitch, returned `:344`), `:374` `(ltWeight > 0.1) ? boost : 0.0` (true leading tone) | **OK (known issue, accurately on record)** — the gate is present exactly as the §11 note states (the `>0.1` test for char-pitch is at `:339`, returned at `:344`; LT at `:374`). Not a divergence — design documents it as a scheduled fix. |
| **Keymode §2 (the *more music than selected* constraint): "This reach-back **is an extension request** … (Designed, not yet built — verified 2026-06-24: no reach-back/extend code exists at either layer …)"** (`:110–120`) | **Reach-back IS built** (see reachback rows below): L1 `extend` + `regionanalyzer.cpp:585–666` loop | **STALE** — the keymode §Status header was updated for the Step-1 *key* wiring but §2's reach-back "not yet built" note was not; both `extend` (L1) and the reach-back loop exist. |
| **Reachback status: "DRAFT for sign-off. Read-only design — no code." (`:3–9`); §0 "production `analyzeRegions` (`regionanalyzer.cpp:488`) builds whole-score on every path (`build(score)`, 1-arg) … none of the bounded-context model is engaged in production"** (`:11–18`) | **Reach-back loop is built** as the §2/§3 algorithm, gated OFF by default: `regionanalyzer.cpp:67–83` (`measureTicksBefore` increment = the §2 "a measure" unit), `:536–538` (conditional build: `opts.reachBack.enabled ? build(score,start,end) : build(score)`), `:585–666` (trigger → extend(Earlier) → re-slice → re-decode → converge), `:1374–1388` (output-filter = §2 step 7). `analyzeRegions` def is now at `:506`. | **STALE (status) + partial DIVERGENCE (the §0 correction)** — the "no code" status is obsolete: the loop is built. §0's "builds whole-score on **every** path" is also superseded — the build is now **conditional** (`:536–538`): whole-score on the production/default path (reachBack default false), selection-scoped when reach-back is enabled. The *spirit* of §0 still holds (production stays whole-score; reach-back never fires there), and the cited line `:488` has drifted to `:506`/`:536`. |
| Reachback §2/§3: loop owned by the orchestrator (not the decoder); trigger = leading-edge slice unsettled; converge = **leading-edge key stops changing** (the headline criterion, the cheaper "settled context in view" proxy *rejected by measurement*); output = selection only | `regionanalyzer.cpp:585–666` — loop in `analyzeRegions` (decoder untouched/pure); trigger `opening.valid && !opening.settled` (`:638`); converge when `cur.sameKey(lastSettled)` (`:660–662`); proxy-rejection noted in-code `:598–604`; output-filter `:1380–1388` | **OK** — the as-built reach-back **matches the reachback design content exactly**, including the §3 measurement-corrected convergence (leading-edge-key-repeats, not the rejected proxy). Only the doc's *status header* lags. |
| Reachback §0/§2 build-decision: "either a parameter on `analyzeRegions` defaulting to whole-score (production path unchanged) **or** a thin sibling … the build decides" | As-built chose the **parameter** form: `AnalyzeRegionsOptions::reachBack` (`opts.reachBack.enabled`, default false) on the existing `analyzeRegions` — no duplicated orchestration | **OK** — the open build-decision was resolved to the parameter option (unification preserved: one orchestrator). Worth recording in the reachback as-built notes. |

**L3 verdict:** the emission scorer, the sequence Viterbi, and the reach-back loop (trigger / converge / output-filter)
are **built and match the design content** (the keymode §Status is current for the *key* wiring; the reach-back loop
follows the reachback §2/§3 algorithm to the letter, incl. the measurement-corrected convergence). The deltas are
**status-staleness**: keymode §2 and the entire reachback doc still say reach-back is "not yet built / no code," and
the reachback §0 "builds whole-score on every path" no longer literally holds (build is conditional). The §11
leading-tone known issue is accurately on record.

---

## §2 — Cross-cutting structural deltas

| Item | Code location (as-built) | Doc location | Verdict |
|---|---|---|---|
| **Types-leaf header** — value-type closure in `analysis/types/analysistypes.h`; the two type-only back-edges gone | `analysistypes.h:24–51` (leaf charter + relocation list); `regiontonecollector.h:52` includes `…/types/analysistypes.h` and **not** `chordanalyzer.h`/`keymodeanalyzer.h`; `keymodeanalyzer.h:27` includes `../types/analysistypes.h` and **not** `chord/analysisutils.h` | — | **OK (code)** — both header back-edges (`regiontonecollector.h → {chordanalyzer.h, keymodeanalyzer.h}`, `keymodeanalyzer.h → chord/analysisutils.h`) are removed; the leaf is STL-only. |
| **`PitchContext` un-nested** with a `KeyModeAnalyzer::PitchContext` alias | `analysistypes.h:902–916` (`struct PitchContext` un-nested + the member-alias note) | `ARCHITECTURE.md:1687–1696` shows `struct PitchContext` standalone but **does not mention** the un-nesting, the alias, or `analysistypes.h` | **MISSING (doc)** — code is correct; ARCHITECTURE.md neither names `analysistypes.h` nor records the un-nest/back-edge removal (grep for `analysistypes` in ARCHITECTURE.md = 0 hits). The relocation is invisible in the architecture doc and its module map (`:751–755`). |
| **kMasks single-source** — `kTemplateIntervals` is the sole interval source feeding both `templates[]` and `kMasks` | `chordanalyzer.cpp:347–357` + `:1219–1224` (`templates[].intervals` derived from `kTemplateIntervals`); `harmonicfunctionlayer.cpp:176–209` (`kMasks` = `makeTemplateMasks()` over `kTemplateIntervals`, with `static_assert` pinning the 17 byte-identical masks); `harmonicfunctionlayer.h:261–262` | `docs/scoring_model.md:152–163, 282–283, 366, 811–820` | **OK** — code derives both from one source; `docs/scoring_model.md` accurately describes "`kMasks` … derived from `analysis::kTemplateIntervals` … no longer a hand-typed mirror." Doc is synced. (No other doc describes a hand-sync — ARCHITECTURE.md does not re-document it.) |
| **Bounded-context ENGAGEMENT status** — built as a *capability*, production still whole-score (engagement deferred) | Production path is whole-score (`regionanalyzer.cpp:536–538`, reachBack default false); capability built but gated | `ARCHITECTURE.md:683–687` ("`changePointSlices` is consumed by L3 on a **whole-score** model … Phase-2 clip is inert … byte-identical"); L3 section `:698–701` ("Reusing the **whole-score** `noteModel`") | **OK** — **no doc overstates engagement.** ARCHITECTURE.md correctly states production is whole-score with the clip inert. (Conversely the L1/L3 *design docs* UNDERSTATE — they say extend/reach-back are "not built"; captured as STALE in §1.) |
| **ARCHITECTURE.md L2 wired-status** (internal consistency) | Slicer consumed live (`regionanalyzer.cpp:579–583`) | `ARCHITECTURE.md:600–601` ("L2, BUILT — isolated"), `:635` (header "isolated"), `:638–639` ("**not** wired into the live analysis pipeline") vs. `:683–688` ("consumed by L3") + L3 section `:690+` | **STALE (internally inconsistent)** — the L2 roadmap line, section header, and intro still say "isolated / not wired," contradicting the same section's `:683–688` and the L3 section. Same staleness as `slicer.h:67–69` and the slicing-spec §2/§10/§11. |

---

## §3 — Summary of required syncs (for Cowork's precise spec-sync)

**Doc-staleness (the bulk — say "now built / now wired"):**
1. **L1 design §3 (`:96–102`) + §11 (`:201–206`)** — drop "extend … Designed, not yet built"; `extend`/`boundaryReached`/loaded+selection-span accessors are built (Phase-1a, whole-score re-walk). The "extend + whole-score-fix = one coupled change" framing is superseded (decoupled).
2. **tpc-capability doc status (`:2–3`)** — "no code" → built (`spellingview.{h,cpp}`, capability-only, no production consumer). Body is otherwise accurate.
3. **Reslice doc status (`:3`)** — "no code" → clip built (`slicer.cpp:63–97`); the §5 "confirm at build" decision was taken (minimal `Slice`).
4. **Slicing-spec §2/§10/§11 + `slicer.h:67–69` + ARCHITECTURE.md `:600–601/:635/:638–639`** — "isolated / not wired" → wired; L3 reads the slices (`regionanalyzer.cpp:579`). Note the precise truth: L2's clip is byte-identical on whole-score; the analysis movement was L3's consumption.
5. **Keymode §2 (`:110–120`)** — drop the reach-back "not yet built" note (the §Status header is already current for the key wiring; §2 lagged).
6. **Reachback doc status (`:3–9`) + §0 (`:11–18`)** — "no code" → loop built and gated OFF (`regionanalyzer.cpp:585–666`); §0's "builds whole-score on **every** path" → build is **conditional** (`:536–538`), whole-score only on the production/default path; line `:488` → `:506`/`:536`. The §2/§3 algorithm and the measurement-corrected convergence match the as-built — only the status lags. Record the build-decision (parameter on `analyzeRegions`, not a sibling).

**Doc-MISSING (built, but absent from the architecture doc):**
7. **ARCHITECTURE.md** — add the **types-leaf header** (`analysis/types/analysistypes.h`), the two removed back-edges, and the `PitchContext` un-nest + `KeyModeAnalyzer::PitchContext` alias (none are mentioned; `PitchContext` at `:1687` is shown with no relocation note). Optionally record the reach-back *capability* (not in the doc at all) so the bounded-context build-state is complete.

**Already-synced / OK (no action):**
8. **kMasks single-source** — `docs/scoring_model.md` is accurate; code derives `templates[]` + `kMasks` from `kTemplateIntervals`.
9. **Bounded-context engagement** — no doc overstates engagement; production correctly documented as whole-score / clip-inert.
10. The L1 contract (build overloads, `NoteEvent` 11 fields, interim rebuild), the L1.5 primitive shape + capability-only marking, the L2 algorithm + clip, and the L3 emission/Viterbi/reach-back **algorithm** all match their designs.

---

## §4 — Possible code-vs-intent defects (flagged separately from doc-staleness)

**No new code defect found.** The code matches the design *intent* at every layer checked. Two items are **already on
record** (not new):

- **Latent (on record):** `NoteEvent.tpc` (`note_model.h:82`) keeps the default `−1` and the comment **"(0-34 … -1 =
  not provided)"**, but `−1` is the legitimate spelling F𝄫 and the real range is `−8 … 40`. Identical stale comment at
  `analysistypes.h:136` (`ChordAnalysisTone.tpc`). The tpc-capability design **§5 (`:88–99`) records this as a deferred
  L1-cleanup**, explicitly *not* to be fixed in Phase 4; the guarantee today is the build-path invariant (every
  `NoteEvent` on the build path is assigned a real `Note::tpc()`), and there is no production consumer of the spelling
  primitive yet. **Action:** carry into the L1 as-built/cleanup pass (default `TPC_INVALID = −9`; correct the range
  comment) — not a Phase-5 blocker.
- **Known issue (on record):** the brittle `>0.1` leading-tone/characteristic-pitch presence gate
  (`keymodeanalyzer.cpp:339,374`) is the non-Bach K279 F-vs-C regression. Accurately documented in keymode §11 ★ with
  a scheduled Phase-4 emission fix. Not a doc↔code divergence.

---

## Appendix — verification basis (read-only)

- Read in full: the five design docs (`cowork_layer1_note_model_design.md`, `cowork_tpc_capability_design.md`,
  `cowork_layer2_slicing_design.md`, `cowork_layer2_reslice_design.md`, `cowork_layer3_keymode_design.md`,
  `cowork_layer3_reachback_design.md`) and the as-built sources (`note_model.{h,cpp}`, `spellingview.{h,cpp}`,
  `slicer.{h,cpp}`, `keymodesequence.h`, `analysistypes.h`, `regionanalyzer.cpp` orchestration seam, the
  `keymodeanalyzer.cpp` leading-tone gate).
- Grep-confirmed: `spellingview` has **no production consumer** (only build/test/self); the two header back-edges are
  removed (`regiontonecollector.h:52`, `keymodeanalyzer.h:27`); `kMasks` is derived from `kTemplateIntervals`
  (`harmonicfunctionlayer.cpp:176–209`); `jointKeyWiringEnabled()` default OFF (`jointkeydecision.cpp:145`);
  `ARCHITECTURE.md` contains **zero** `analysistypes` mentions.
- **No source or doc files were edited.** This report is the sole artifact.
