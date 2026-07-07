# CC Instruction — Engage arc #7: the PRE-Layer-5 refactor batch (Stage 1 of the ratified plan)

> **ACTIVE DISPATCH (Cowork, 2026-07-07).** Stage 1 of the ratified engage-arc plan
> (`cowork_engage_arc_plan.md`): the portable total-unification / layer-adherence wins that stand alone
> BEFORE the Layer-5 design (#8 puts refactoring first; #6/#7 are what these restore). Each is a
> **byte-identical** refactor of a duplicated/misplaced concern — not throwaway (both the legacy and decoder
> paths need them). Source of truth for each fix: `cowork_structural_integrity_audit.md` §3 (FQ rows) + the
> cited site rows.
>
> **Execution discipline (per fix, binding):**
> - **One revertible, provenance-stamped `feat`/`refactor` commit per FQ item** (#14). Regression-test
>   between each (#11).
> - **Byte-identical is the expectation.** Verify the full output surface — winner AND `alternatives[]`,
>   whole `.ours.json` — **0 diff across 352×3** vs the pre-commit HEAD (#15); both stops green
>   (`characterise` 52/24/52; robust sandwich identity-PASS); suites 1101/53+4skip/11 no golden refresh.
>   **Any output move on a supposed byte-identical unification ⟹ STOP** and report (a unification must not
>   change behavior — investigate, do not re-baseline to absorb it).
> - **Layer discipline (#7):** each fix lands in its proper layer/owner. **Doc + tests in sync (#10/#11)** in
>   the same commit.
> - **STOP-and-report any item that snags** (an entanglement, or that can't be done byte-identically) — deliver
>   the clean ones, flag the rest; do NOT force.
>
> **Read first:** `cowork_engage_arc_plan.md` · `cowork_structural_integrity_audit.md` §3 + the FQ site rows.
>
> **Current state:** HEAD `0d7fcc6c48`, branch `master`, fork-only, ahead 0. Both stops green. Corpus
> `c50002fee1`. **Pending uncommitted Cowork edits in the tree:** CLAUDE.md #12 exclusion elaboration +
> `cowork_engage_arc_plan.md` — fold both in the closing docs commit.
>
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read files.**
> **Build via** `powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`.

---

## Task 0 — state
HEAD/branch/ahead; both stops green; confirm the two pending Cowork edits are in the tree.

## Task 1 — FQ-3: relocate `findTemporalContext` out of Layer 1.5 (HIGH, live-path)
Site: `engravingbridge/regiontoneprimitives.cpp:451-592` — an L1.5 "view" instantiates the L4 analyzer and
runs the full L4+L5 decision pipeline ×2 to identify neighbour chords, on the live path.
- **First (the UNCLEAR-7 adjudication):** confirm it is **not simpler to fold into the E4 temporal-context
  ownership move**. If relocating cleanly now requires decoder internals or would be redone at E4 ⟹
  **STOP-and-report** (defer to E4) — do not force a pre-L5 relocation that E4 redoes.
- Else: relocate the neighbour-chord-identity computation to its proper owner (L4 / the temporal-context
  assembly); L1.5 exposes only the tone views. **Byte-identical** (same computation, relocated) — verify per
  the discipline above. Commit.

## Task 2 — FQ-1: unify the "best different-root alternative" scan into ONE primitive
The scan is computed in **four** places (the inversion-append `harmonicfunctionlayer.cpp:537-540`; the pedal
gap `chordpostpasses.cpp:262-269`; the `promoteToWinner`/FM2 primitive; the dormant decoder
`chordslicedecoder.cpp:927-930`). Unify into one primitive (extend `promoteToWinner` or a shared helper it
calls); route all callers through it. **Byte-identical per site** (the audit's FQ-1 claim). Both the legacy
path (until E4) and the decoder use it — not throwaway. Commit.

## Task 3 — FQ-5: fact-layer duplication cleanups (trivial #6 wins)
Each a unify-to-one-source, byte-identical; one commit (or one per site if cleaner):
- **S5** `regiontonecollector.cpp:72-81` — the inlined `{1.0,0.85,0.75,0.5}` beat-weight map → call
  `scoreharvest::regionMetricWeightForBeatType` (header already included).
- **S7** `modepriorpresets` — the 21 "Standard" mode-prior magnitudes exist as three literal copies kept in
  sync by a test → single source.
- **S10** `keymodesequence.cpp:224-226` vs `keymodeanalyzer.cpp:766-767` — the emission-confidence sigmoid
  written twice → one shared helper.
- **S11** `regionanalyzer.cpp` ×3 — the copy-pasted `ChordPathNode` construction → one
  `makeChordPathNode(...)` builder.

## Task 4 — FQ-6: serialization/display cap-views (BYTE-IDENTICAL STRUCTURAL ONLY)
Sites: the batch serialization cap (`batch_analyze.cpp:660/712`, `altIdx<3`) and the bridge display
(`notationcomposingbridge.cpp:297-304`, uncapped). Make them **explicit per-consumer projections over the one
carry** — **keeping the current values** (batch caps at 3, bridge uncapped). **The cap-#2 VALUE lift stays
DEFERRED to Stage 3 (L5 engagement).** This is a structural unification only. **If it cannot be done
byte-identically without changing a serialized value ⟹ STOP and defer the whole item to Stage 3.** Commit
only if byte-identical.

## Task 5 — FQ-7: key-decoder constant sourcing + the S9 dead-work check
- **S8** `keymodesequence.h:117-137` — the cost/window constants copied-by-value from the resolver/scoreharvest
  → source from the shared symbols so a Stage-5 fit moves one place. Byte-identical (same values). Commit.
- **S9** `regionanalyzer.cpp:585/611` (the UNCLEAR): the heavy `resolveKeyAndModeRanked` runs but only
  `.front().{fifths,mode}` seeds the grid. **First verify** it is genuinely dead scored work — that dropping
  it to the corrected-fifths+declared-mode seed leaves the segmentation grid **byte-stable (S2 anchor)**. If
  proven dead + byte-stable, drop it (byte-identical). **If it affects the grid/segmentation, do NOT drop it**
  — keep it, report the finding (S9 is load-bearing, not dead). #5: investigate before cutting.

## Task 6 — closing docs fold + push
1. **Report** `cc_engage_pre_l5_refactor_report.md` (force-add): per-FQ — what unified, the byte-identity
   proof (0-diff full-surface), both stops, any item STOPPED-and-deferred with its reason, all commit SHAs.
2. **Fold** (`docs(cowork):`): **the pending CLAUDE.md #12 edit + `cowork_engage_arc_plan.md`** (commit them
   here) · `STATUS.md` · `COWORK_HANDOFF.md` · `cowork_structural_integrity_audit.md` (mark the completed FQ
   rows RESOLVED with SHAs; any deferred item noted) · `cowork_stage5_fitter_design.md` (engage observation) ·
   this instruction (force-add).
3. **Push fork-only** (`git push origin master`) — never toward `upstream`/`musescore/MuseScore` (`cfc7eb5e39`
   HARD STOP).

## STOP conditions
- Any output move (full-surface byte-diff ≠ 0, or a stop not green) on a supposed byte-identical unification ⟹
  STOP + investigate; do NOT re-baseline or refresh goldens to absorb it.
- FQ-3 not cleanly relocatable pre-L5 (needs decoder internals / would be redone at E4) ⟹ STOP + defer to E4.
- FQ-6 not achievable byte-identically ⟹ STOP + defer to Stage 3.
- FQ-7-S9's resolve NOT proven dead/grid-byte-stable ⟹ keep it, report (do not cut load-bearing work).
- Any cross-layer change beyond the named relocation/unification; any corpus write/re-baseline; any push
  toward `upstream`/`musescore/MuseScore`.

## Acceptance
Each attempted FQ item = one revertible provenance-stamped commit, byte-identical proven on the full surface
(winner + alternatives, 0 diff 352×3), both stops green, suites no-refresh, docs+tests synced ✓ · FQ-3
relocated (or cleanly deferred to E4 with reason) ✓ · FQ-1 primitive unified, all four callers routed ✓ ·
FQ-5 four dedups unified ✓ · FQ-6 byte-identical projections (or deferred) ✓ · FQ-7 S8 sourced + S9
dead-work adjudicated at code ✓ · report + fold (incl. the CLAUDE.md #12 edit + the ratified plan doc + the
RESOLVED FQ rows) with SHAs ✓ · pushed fork-only, upstream untouched ✓.

*Cowork, 2026-07-07. Engage arc #7 — Stage 1 of the ratified plan: pre-Layer-5 portable unification, each a
byte-identical revertible commit. On CC's report: Cowork verifies each byte-identity proof at objects → then
the Layer-5 engagement design (Stage 2) opens.*
