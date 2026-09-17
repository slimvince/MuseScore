# CC Instruction — L1–L3 spec-sync to as-built (Phase-5 sign-off, doc/comment-only)

> **Why.** Apply the **exact syncs** the delta-check found (`cc_l1l3_delta_check_resync_report.md` §3) so the L1–L3
> design docs + `ARCHITECTURE.md` match the **as-built**, for the Phase-5 sign-off. The delta-check confirmed the
> **contracts already match** — the deltas are **build-status staleness** ("design / no code" where it's built;
> "isolated / not wired" where it's wired). **DOC + CODE-COMMENT ONLY — no contract changes, no `.cpp`/`.h` *logic*
> change, no behaviour.** Use the report's §3 doc-section↔code-line citations as the worklist.
> *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §1 — The syncs (per delta-check §3 — status/wiring corrections only; do NOT touch the contracts, they match)
1. **`cowork_layer1_note_model_design.md` §3 (`:96–102`) + §11 (`:201–206`)** — drop "extend … Designed, not yet
   built"; mark `extend`/`boundaryReached`/loaded+selection-span accessors **built (Phase-1a, whole-score re-walk)**;
   note the "extend + whole-score-fix = one coupled change" framing is **superseded** (built decoupled).
2. **`cowork_tpc_capability_design.md` status (`:2–3`)** — "Read-only design — no code" → **built** (`spellingview.{h,cpp}`,
   capability-only, no production consumer). Body otherwise accurate.
3. **`cowork_layer2_reslice_design.md` status (`:3`)** — "no code" → **clip built** (`slicer.cpp:63–97`); the §5
   "confirm at build" decision was taken (minimal `Slice`).
4. **`cowork_layer2_slicing_design.md` §2 (`:45–46`) / §10 (`:151–152`) / §11 (`:162–163`)** AND the source comment
   **`slicer.h:67–69`** — "isolated / not yet wired" → **wired; L3 reads the slices** (`regionanalyzer.cpp:579`). Keep
   the precise nuance: L2's clip is byte-identical on whole-score; the analysis movement came from **L3's consumption**,
   not the slicer. *(`slicer.h:67–69` is a comment-only edit — confirm the diff is comment lines, no code.)*
5. **`cowork_layer3_keymode_design.md` §2 (`:110–120`)** — drop the reach-back "not yet built" note (the §Status header
   is already current for the key wiring; §2 lagged).
6. **★ `cowork_layer3_keymode_design.md` §11** — the leading-tone gate's "fix scheduled for **Phase 4**" is **WRONG →
   correct to Phase B (B2)**. Leading-tone de-brittling is inference-quality, behind the firewall; Phase 4 was the tpc
   capability. (Search the L3 docs for any other "Phase 4" leading-tone reference and fix likewise.)
7. **`cowork_layer3_reachback_design.md` status (`:3–9`) + §0 (`:11–18`)** — "no code" → **loop built, gated OFF**
   (`regionanalyzer.cpp:585–666`); §0's "builds whole-score on **every** path" → build is **conditional** (`:536–538`),
   whole-score only on the production/default path; the cited `:488` drifted to `:506`/`:536`. The §2/§3 algorithm + the
   measurement-corrected convergence already match as-built — only the status lags. Record the build-decision (a
   **parameter** on `analyzeRegions`, not a sibling — unification preserved).
8. **`ARCHITECTURE.md`** — (a) **MISSING:** add the **types-leaf header** `analysis/types/analysistypes.h`, the **two
   removed type-only back-edges**, and the **`PitchContext` un-nest + `KeyModeAnalyzer::PitchContext` alias** (zero
   `analysistypes` mentions today; `PitchContext` at `:1687` has no relocation note; module map `:751–755`). (b)
   **STALE / internally inconsistent:** the L2 lines `:600–601` ("isolated"), `:635` (header "isolated"), `:638–639`
   ("not wired") contradict the same doc's `:683–688` ("consumed by L3") — fix the stale three to "wired / consumed by
   L3."

## §2 — Scope guard
- **DO NOT change any layer contract, algorithm description, or design content** — the delta-check confirmed they
  match; this is *status + wiring + the one Phase-label* correction only.
- **No `.cpp`/`.h` logic** — the only source touch is the `slicer.h:67–69` **comment**. Confirm the source diff is
  comment-only.
- `docs/scoring_model.md` (kMasks) is already synced — leave it.

## §3 — Gate & deliver
- **Build green; both suites + snapshots unchanged** (doc/comment-only — nothing compiled meaningfully changes; the
  `slicer.h` comment edit must not alter behaviour). Confirm.
- Commit **locally (unpushed)**: the synced design docs + `ARCHITECTURE.md` + the `slicer.h` comment. Message:
  `docs: L1-L3 spec-sync to as-built (build-status + wiring + leading-tone Phase-B label) + ARCHITECTURE types-leaf`.
- Write `cc_l1l3_spec_sync_report.md` (gitignored): per-item done/skipped, and the commit sha — so Cowork verifies by
  sha that only `.md` + the one `slicer.h` comment changed (no logic).

## §4 — Stops
- Any contract/algorithm/design-content change, or any non-comment source edit → STOP (out of scope).
- A push targets `upstream` → STOP.
