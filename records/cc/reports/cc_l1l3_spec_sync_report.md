# CC — L1–L3 spec-sync to as-built (Phase-5 sign-off) — execution report

> **Scope.** Apply the exact syncs the delta-check found (`cc_l1l3_delta_check_resync_report.md` §3) so the L1–L3
> design docs + `ARCHITECTURE.md` match the as-built. **DOC + CODE-COMMENT ONLY** — no contract changes, no
> `.cpp`/`.h` *logic* change, no behaviour. This report: per-item done/skipped + the commit sha so Cowork can verify
> by sha that only `.md` + the one `slicer.h` comment changed.

**Commit (local, unpushed):** `c9633aebc4` —
`docs: L1-L3 spec-sync to as-built (build-status + wiring + leading-tone Phase-B label) + ARCHITECTURE types-leaf`
**8 files changed, 93 insertions(+), 41 deletions(-).** Branch `master`. Not pushed.

---

## §1 — Per-item ledger (all DONE; status/wiring/Phase-label only, no contract change)

| Item | Doc / file | What changed | Status |
|---|---|---|---|
| **1** | `cowork_layer1_note_model_design.md` §3 (`:96–102`) + §11 (`:201–206`) | §3 *Widen the covered span* bullet: replaced "Designed, not yet built (verified 2026-06-24 …)" parenthetical with **Built — Phase-1a** (`extend(Direction,int)`, `boundaryReached()`, loaded/selection-span accessors exist in `note_model.h`; append-only, one step, no convergence loop, clamp+report; built *decoupled* from the §11 fix — interim re-walks the whole score, span-scoped walk is Phase-1b). §11: marked *extend* **now built**, dropped the "masks the missing extend" framing, and recorded the **"extend + whole-score-fix = one coupled change" framing as superseded** (built decoupled). | **DONE** |
| **2** | `cowork_tpc_capability_design.md` status (`:2–3`) | "DRAFT … Read-only design — no code" → **BUILT (capability-only, no production consumer)**: cites `spellingview.{h,cpp}` + `tests/spellingview_tests.cpp`, engravingbridge seam beside `weightedPcView`/`soundingAt`, grep-confirmed no production consumer. Body left intact. | **DONE** |
| **3** | `cowork_layer2_reslice_design.md` status (`:3`) + §5 (`:84`) | Status "no code" → **BUILT** (clip at `slicer.cpp:63–97`, multiset clip, inert/byte-identical on whole-score). §5 "**Decision to confirm at build**" → "**Decision taken at build: minimal `Slice` (`{int start; int end;}`)**, consumer derives in-selection/context from the model's selection span". | **DONE** |
| **4** | `cowork_layer2_slicing_design.md` §2 (`:45–46`), §10 (`:151–152`), §11 (`:162–163`) **+** `src/composing/analysis/slicing/slicer.h:67–69` | All four "isolated / not yet connected / not wired" → **Connected; L3 reads the slices** (`regionanalyzer.cpp:579` → `KeyModeSequenceDecoder`). Kept the precise nuance: slicer output **byte-identical** on the whole-score live path (clip inert); the analysis movement came from **L3's consumption**, not the slicer. `slicer.h:67–69` is a **comment-only** edit (verified: all changed lines are `//`). | **DONE** |
| **5** | `cowork_layer3_keymode_design.md` §2 (`:110–120`) | Dropped the reach-back "Designed, not yet built (verified 2026-06-24 …)" note → **Built — gated OFF**: loop at `regionanalyzer.cpp:585–666`, trigger/extend(Earlier)/re-slice/re-decode/converge/output-filter, rides on L1 `extend`, **parameter** `opts.reachBack.enabled` (default false) so production stays whole-score. Algorithm content (direction/stop-condition/hard-bound) unchanged. | **DONE** |
| **6 ★** | `cowork_layer3_keymode_design.md` §11 (`:325`) | Leading-tone presence-gate fix "scheduled in **Phase 4**" → **corrected to Phase B (B2)** — leading-tone de-brittling is inference-quality, behind the inference firewall; **Phase 4 was the tpc-capability foundation, not this**. Swept both L3 docs for other "Phase 4" leading-tone refs: keymode had exactly this one; reachback had none. | **DONE** |
| **7** | `cowork_layer3_reachback_design.md` status (`:3–9`) + §0 (`:11–18`) | Status "no code" → **BUILT (capability, gated OFF; production whole-score)**; recorded the build-decision resolved to the **parameter** form (`AnalyzeRegionsOptions::reachBack` on `analyzeRegions`, *not* a sibling — unification preserved). §0: "builds whole-score on **every** path" → **conditional build** (`regionanalyzer.cpp:536–538`, `opts.reachBack.enabled ? build(score,start,end) : build(score)`), whole-score only on production/default path; cited `:488` → `:506` (def) / `:536` (build). Kept §0's spirit (production stays whole-score, reach-back never fires there). §2/§3 algorithm + measurement-corrected convergence already matched — untouched. | **DONE** |
| **8a** | `ARCHITECTURE.md` (MISSING) | Added a **types-leaf** module-map row `composing/analysis/types/analysistypes.h` (cross-layer value-types leaf, STL-only, pure relocations) + a paragraph recording the **two removed type-only back-edges** (`regiontonecollector.h → {chordanalyzer.h, keymodeanalyzer.h}`; `keymodeanalyzer.h → chord/analysisutils.h`) and the **`PitchContext` un-nest + `using PitchContext = analysis::PitchContext;` alias**. Added a **Relocation** note at the `#### Input — PitchContext` struct (`:1687`). (Was zero `analysistypes` mentions before.) | **DONE** |
| **8b** | `ARCHITECTURE.md` (STALE / internally inconsistent) | Fixed the L2 "isolated / not wired" lines that contradicted the same doc's "consumed by L3" (`:683–688`): the rebuild-target sentence (`:600–601`), the Layer-2 section header (`:635`), the "not wired" intro (`:638–639`), **and** the Layer-3 section's "(Layers 1–2 are built but isolated)" line (`:698`, same inconsistency class) → all now say **wired / consumed by L3** (`regionanalyzer.cpp:579`), preserving the byte-identical-on-whole-score nuance. | **DONE** |

**Skipped (per §2 scope guard / already-synced):** `docs/scoring_model.md` kMasks (already synced — left untouched). No layer contract, algorithm description, or design-content change was made anywhere. The L1 `tpc` default-`−1`/range-comment cleanup and the leading-tone `>0.1` gate remain on-record latent items (not in this sync's scope).

---

## §2 — Gate (build green; both suites + snapshots unchanged)

Built via `setup_and_build.bat` (15/15 targets linked; only pre-existing C4100 warnings). The `slicer.h` comment touch
recompiled its consumers (composing_analysis unity TUs, `slicer_tests`) — byte-equivalent objects, behaviour-neutral.

| Suite | Result |
|---|---|
| `composing_tests.exe` | **826/826 PASSED**, 0 FAILED (exit 0) |
| `notation_tests.exe` | **53/53 PASSED**, 0 FAILED (exit 0) |
| `pipeline_snapshot_tests.exe` | **11/11 PASSED**, 0 FAILED, **no golden refresh** (exit 0) |

All green; snapshots byte-stable (no `--update-goldens`). Confirms nothing compiled meaningfully changed.

---

## §3 — Verification basis for Cowork (by sha)

- `git show --stat c9633aebc4` → exactly **8 files**: the 7 `.md` design/architecture docs + `slicer.h`.
- `git show c9633aebc4 -- src/composing/analysis/slicing/slicer.h` filtered for non-comment changed lines →
  **ALL-CHANGED-LINES-ARE-COMMENTS** (every `+`/`-` line is a `//` comment; no logic).
- Only modifications, no adds/deletes/renames. `scratch_artifacts/` left untracked (not mine; not staged).
- Commit is **local on `master`, unpushed**. No `upstream` interaction.

## §4 — Stops (none hit)

No contract/algorithm/design-content change was required or made; no non-comment source edit; no push to `upstream`.
