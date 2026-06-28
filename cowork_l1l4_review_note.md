# L1–L4 review — Cowork side (docs + architecture coherence): findings + tidy applied

> Companion to `cowork_l1l4_review_charter.md` (the gate) and `cc_l1l4_review_report.md` (CC's code/tests/data side).
> Cowork's half: three parallel read-only passes (file tools only — never bash for working-tree reads), every
> load-bearing claim cited at source. **Headline: the forward-only layered architecture is INTACT; the docs were
> accurate about *what the code does* and lagged only on *whether it's been built* — mechanical status-tidy, no
> algorithmic contradiction. One substantive code question (the tpc-fold) handed to CC.**

## 1. Architecture coherence — VERIFIED INTACT (the most important result)
All five coherence checks passed at source (agent read of includes / contracts / gating):
1. **No new back-edges from the L4 build** — `chordslicedecoder.{h,cpp}` includes only L1/L1.5/L2/L3 + `spellingview`;
   no notation, no L5/progression-grammar. The §4 two-reading look-ahead consumes `nextChord` (an L4 result) and the
   code explicitly disclaims a transition cost ("that is Layer 5").
2. **L4→L5 abstain contract is clean & forward** — `OpenQuestionLabel` *declares* the open question + competing
   readings; L4 does not resolve it (stated 3× in source). Representational; the `SliceDecision` is unchanged by G6.
3. **Header back-edges stay killed** — `regiontonecollector.h` + `keymodeanalyzer.h` include only `analysistypes.h`;
   the leaf is dependency-free.
4. **tpc/spelling single interpreter** — `spellingview` is the one shared interpreter; the pin consumes it (no second
   interpreter *in the decoder*).
5. **Forward-only orchestrator** — `regionanalyzer.cpp` includes L1–L4 only, no L5; reach-back is within-layer; the new
   decoder is isolated (capability-gated, not engaged).
**Verdict: no new coupling, back-edge, or layer violation introduced by the L4 build.** The layered design holds → L5
can open on a clean foundation.

## 2. Documentation — status-banner lag (mechanical), now tidied
The dominant pattern: several docs described a *pre-build* world. **No doc misdescribed what the code does.** Tidy
applied by Cowork:
- `cowork_layer4_chordsymbol_design.md` — banner "not yet rebuilt" → **AS-BUILT (G1–G6+pin) but DORMANT, engage-with-L5**. ✅
- `cowork_types_header_design.md` — "DRAFT for ratification" → **BUILT (`analysistypes.h`, `11f26864f9`)**. ✅
- `cowork_l1l3_stabilization_plan.md` — kMasks COMPLETION → **DONE**; the `batch_analyze`-down HARD PREREQUISITE →
  **RESOLVED (`5357f5a7ed`)**; Phase-5b → **AS-BUILT-dormant**. ✅
- `cowork_phase5b_l4_build_plan.md` — Steps 1 (G1), 3 (G6), 4 (G4/C1) → **✅ DONE** (matching Step 2's mark). ✅
- `cowork_l1l4_architecture_audit.md` — **resolution banner** (Q4 gate/CMake, Q1.3 kMasks, Q2/Q5 decoder-dormant). ✅
- `COWORK_HANDOFF.md` — standing block "57/23/57" → **53/24/53**; header date refreshed to 2026-06-26. ✅
- `cowork_tpc_capability_design.md` §3 — recorded the pin is built; **flagged the fold question** (see §4). ✅

## 3. Canonical-doc OMISSIONS — handed to CC (its domain: living/project docs on Windows)
The gate (53/24/53) is consistent across CLAUDE.md / STATUS.md / ARCHITECTURE.md / `docs/`. Two genuine gaps, in the
CC instruction (§4):
- **STATUS.md has no L4-build entry** (its newest entry predates the build) — add the COMPLETE-dormant L4 entry.
- **ARCHITECTURE.md has no as-built Layer-4 section** (narrative stops at L3) — add one mirroring L1/L2/L3.
- Plus stale source *comments* `slicer.h:67` + `harmonicsegmenter.cpp:155` ("NOT wired"/"isolated", now false).

## 4. The one substantive code question — the tpc-fold (→ CC §1 ★)
The tpc-capability spec §3 requires the L4 spelling-pin to **fold** the ≈55 inline `tpcForPc`/`tpcConsistencyBonus`
reads in `chordanalyzer.cpp` into the `spellingview` primitive (one interpreter). **Did it fold them, or does a second
tpc reader now coexist?** Read-only doc review can't tell; CC resolves at source. Report only — the fold (if owed) is a
gated engagement-step refactor (the legacy scorer is live until engage-with-L5).

## 5. Close
Cowork side: **architecture intact; docs tidied; one code question + two doc-omissions delegated to CC.** When CC's
`cc_l1l4_review_report.md` lands (code/tests/data clean + the tpc-fold truth + STATUS/ARCHITECTURE entries), we fold it
in and reach the **✅ L1–L4 COMPLETE** sign-off (modulo the joint-L5 engagement+retirement+seal) → then L5.

## Limits
Doc-accuracy + static-coherence review, not a build/run and not inference correctness (firewall). The L4-build commit
shas are CC-reported (Cowork verified `6732e77c9a`/the decoder byte-identity by SHA earlier; the rest rest on CC's
reports). The tpc-fold is the one load-bearing item explicitly NOT resolved here (flagged, not asserted).
