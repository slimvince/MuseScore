# CC Instruction — Engage arc #3b: Gate A promotion unification — the BUILD event (user-ratified)

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** The user **ratified** the Gate A unification build on the
> engage-arc #3 design surface (the 36-score alternatives ratification surface). This dispatch **implements**
> the committed design — a `src/` change (Layer 4 only) that needs a build.
>
> **The design proved this is byte-identical to HEAD on the FULL output surface (winner AND alternatives)
> across all 352 scores × 3 presets — including the 36.** The present-first primitive reproduces Gate A's
> swap carry, and the append path (FM2) is dormant behind Gate A at HEAD (it never runs where Gate A fires),
> so adding the guarded primitive is byte-identical and removing the separate Gate A rule afterward is
> byte-identical. **Net user-visible delta = zero (#12 preserved).** This is a pure total-unification (#6)
> that also removes a latent information-loss path (the FM2 append overwriting a distinct alternative with a
> near-duplicate of the winner). Every behavior change is user-ratified as one revertible, provenance-stamped
> commit (#14) — this is that commit.
>
> **Read first (the committed plan — implement it, do not re-derive):**
> `cowork_gateA_unification_design.md` — §Task 3 (the unified path: `promoteToWinner` primitive with
> present-first dedup; the collapsed builder wrapper; Gate A + FM2 as two branches of one promotion; the
> byte-identical Gate A removal) and §Task 4 (the build-event verification plan + the exact 36-stem list).
>
> **Current state:** HEAD `b0acb5c436`, branch `master`, fork-only, ahead 0. Both stops green. Corpus
> `c50002fee1`.
>
> **VS Code bash rules:** append `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read
> files** — use the file tools. **Build via** `powershell.exe -Command "Start-Process
> 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`.

---

## Task 1 — implement the unified promotion (Layer 4 only, per §Task 3)
- Add the single `promoteToWinner` primitive with the **present-first dedup guard**, swapping the exact
  `bestAltIdx` so the produced permutation is **byte-identical to Gate A's `std::swap(results[0], …)`**.
- Collapse the three thin builder wrappers (the two byte-identical `gateCtx` copies at
  `postscoringgates.cpp:65` + `chordpostpasses.cpp:129`, and the `WorkCand` variant at
  `harmonicfunctionlayer.cpp:516`) into **one** builder wrapper over the existing `buildChordResult`.
- Route **both** promotion idioms (swap-existing: Gate A/E/G; append-built: FM2/Iter 91) through the one
  primitive, so Gate A and FM2 become the two internal branches of one promotion.
- **Remove the separate `GateA` rule** — it retires byte-identically (winner AND carry) once the primitive
  reproduces its carry, per the O-11 retirement condition.
- **Layer discipline (#7): Layer 4 promotion/carry machinery only. Nothing cross-layer.**

## Task 2 — doc-sync (#10, mandatory same commit)
- Update `docs/scoring_model.md` where Gate A / the promotion machinery is documented (Gate A removed; the
  unified `promoteToWinner`; adjust any gate/rule count).
- Fix the stale comment flagged in the design (`chordpostpasses.cpp:128` "…/analyzeChord" — `analyzeChord`
  delegates to `fn::applyHarmonicFunction`).

## Task 3 — build + verify (the #14/#15 full-surface discipline)
1. **Build** (PowerShell Start-Process).
2. **Full-surface byte-diff — winner + `alternatives[]` — across all 352 scores × 3 presets vs HEAD
   `b0acb5c436`. EXPECTED: byte-identical EVERYWHERE, including the 36.** Any residual diff (winner OR
   alternative, any score) ⟹ **STOP** — the primitive is not reproducing the carry; investigate, do NOT
   refresh anything.
3. **Both regression stops:** `characterise_bir_false.py` ×3 = **52/24/52** set-diff empty; robust sandwich
   (`a8_rebaseline_measure.py` → `robust_stop_diff.py`) **identity-PASS** (roots unchanged by construction).
4. **Suites:** composing **1101** (note any fixture disposition), notation **53 + 4 skip**, pipeline_snapshot
   **11/11 — NO refresh** (the design proved zero overlap with the 36; if any golden would move ⟹ STOP, do
   not update goldens).

## Task 4 — commit + fold + push
1. **One revertible, provenance-stamped `feat(composing):` commit** (#14): the unified promotion + Gate A
   removal + the doc-sync. Provenance stamp per the adoption-event protocol.
2. **Report** `cc_engage_gateA_unification_build_report.md` (force-add): the full-surface byte-identity proof
   (0 net move on 352×3), both stops, suites, reuse-vs-new + what retires (Gate A retires; three wrappers →
   one; two idioms → one primitive), all SHAs.
3. **Fold** (`docs(cowork):`): `STATUS.md` · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`
   (engage-arc observation) · this instruction (force-add) · **AND the pending in-tree Cowork edits to
   `cowork_information_loss_audit.md`** (the U1/U2/U3 adjudications + the exclusion-information refinement +
   the `+3` taxonomy form + the U1 fix-queue item, applied by Cowork 2026-07-06) — commit them in this fold so
   they are not left uncommitted.
4. **Push fork-only** (`git push origin master`) — never toward `upstream`/`musescore/MuseScore` (the
   `cfc7eb5e39` distribution HARD STOP).

## STOP conditions
- **Any residual full-surface byte-diff** (winner OR alternatives) on any score ×preset — the design says
  byte-identical everywhere; a diff means the carry is not reproduced. STOP and investigate; do NOT refresh
  goldens or re-baseline to absorb it.
- Any pipeline-snapshot golden that would move (design proved none does) ⟹ STOP.
- `characterise` ≠ 52/24/52 or robust sandwich not identity-PASS.
- Any cross-layer change, or any `src/` change beyond the Layer-4 promotion machinery + the mandated
  doc-sync.
- Any corpus write; any push/PR/merge toward `upstream`/`musescore/MuseScore`.

## Acceptance
The unified `promoteToWinner` primitive + one builder wrapper implemented in Layer 4; Gate A removed ✓ ·
`docs/scoring_model.md` synced + the stale comment fixed ✓ · full-surface byte-identity proven (winner +
alternatives, 0 net move on 352×3) ✓ · both stops green; suites 1101/53+4skip/11 no-refresh ✓ · one
revertible provenance-stamped commit + report + fold with SHAs ✓ · pushed fork-only, upstream untouched ✓.

*Cowork, 2026-07-06. Engage arc #3b — the ratified build. A byte-identical total-unification that also
closes a latent information-loss path (#6 + #12). On CC's report: Cowork verifies the byte-identity proof at
objects.*
