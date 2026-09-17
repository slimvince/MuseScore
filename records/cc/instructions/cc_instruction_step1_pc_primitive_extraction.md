# CC Instruction — ARCHITECTURE-FIX STEP 1: extract the shared pc/collection primitives (S3-primitive)

> First structural fix of the phase-2 order (`cowork_phase2_architecture_review.md` §5 step 1). **This is the
> ONLY kind of change allowed right now: a PURE, BYTE-IDENTICAL refactor that extracts duplicated primitives
> into one shared layer. NO inference change, NO behavior change, NO scoring-term touch.** If any production
> output moves by a single bit, the change is wrong → revert. North star is unchanged (best = CORRECT
> inference), but this step does not touch inference at all — it only removes duplication.

## §0 — Why this is safe to do now (the sequencing gate)
Phase 1 + phase 2 are complete and reconciled. Step 1 is the lowest-risk structural item: pure
de-duplication, byte-identical. It is the precondition that makes the later passes reason about ONE copy of
these primitives. It changes no boundary, no score, no gate — only *where the functions live*.

## §0.5 — Handling the held B2 guard (USER DECISION 2026-06-17: PRESERVE — rebase it on)
`section/localmodulationdetector.cpp/.h` carries the uncommitted, dormant **B2 subdominant guard** (working
tree +81/.cpp, +34/.h). Per STATUS.md it is **HELD, excluded from commits** — and it is NOT dead: it is
measured-correct-but-parked, gated on the upstream K1 cadence-anchor fix (the inference-phase work). **The
user chose to PRESERVE it, not revert.** So:

1. **First confirm the working tree is clean except B2.** `git status --short` must show ONLY
   `section/localmodulationdetector.cpp` and `.h` modified. If anything else is dirty, STOP and surface — do
   not stash a mixed set. (Your worktree is authoritative; do not trust a stale index — re-check.)
2. **Set B2 aside:** `git stash push -- src/composing/analysis/section/localmodulationdetector.cpp
   src/composing/analysis/section/localmodulationdetector.h` (or save a named patch). Confirm the tree now
   matches HEAD `a03c2493bb` byte-for-byte.
3. **Do the refactor on the clean tree** (§1–§3 below), build, test, BIR — all the byte-identity gates. The
   refactor's own change to `localmodulationdetector.cpp` (the HEAD version: `lmdPcMod12`/`lmdCollectionMask`
   → shared) is part of the refactor commit.
4. **Commit refactor-only (B2-free, local, unpushed).**
5. **Re-apply B2 on top:** `git stash pop` (or re-apply the patch). The B2 hunks call `lmdPcMod12`, which the
   refactor removed → **resolve the conflict by re-pointing B2's `lmdPcMod12(...)` calls to `normalizePc(...)`**
   (proven identical, §1 Family 1). B2 stays **uncommitted, dormant (flag-OFF), byte-identical to production**.
6. **Verify B2 is intact + still dormant:** the re-applied diff = the original B2 hunks modulo
   `lmdPcMod12`→`normalizePc`; build with B2 in the tree must compile; production output (flag OFF) byte-
   identical. Note in your report (and a one-line `cc_b2_subdominant_guard_report.md` addendum) that B2's
   helper calls were re-pointed — its git diff changed cosmetically, the guard logic did not.

If the stash/pop or the conflict resolution is anything other than mechanical (a hunk that does NOT cleanly
map `lmdPcMod12`→`normalizePc`), STOP and surface — do not force it.

## §1 — Scope (verified at the committed object HEAD `a03c2493bb` by Cowork — paths corrected)
Extract the duplicated pitch-class / collection helpers, currently copy-pasted with `lmd*`/`jkd*` ODR-prefixes,
into the existing shared utility namespace. **Cowork has already verified the paths and the identical-body
facts below at HEAD — trust these over your working-tree line numbers (they did not match last time).**

The duplication, in TWO families (do NOT merge across families — they are different computations):

**Family 1 — trivial pc helpers (truly identical):**
- `pcMod12` / `lmdPcMod12` / `jkdPcMod12` (and `pcInMask`) across `cadencekeyanchor.cpp`,
  `section/localmodulationdetector.cpp`, `section/jointkeydecision.cpp`, `tonicizationlabeler.cpp`.
- **★ FIRST check against the EXISTING shared helper:** `src/composing/analysis/chord/analysisutils.h`
  (namespace `mu::composing::analysis`) already defines `inline int normalizePc(int pitch)`. **Verify whether
  `pcMod12`/`lmd*`/`jkd*` are semantically identical to `normalizePc`** — in particular the **negative-input
  handling** (`((x % 12) + 12) % 12` vs a bare `x % 12`). If identical → route all call-sites to `normalizePc`
  (or a thin alias) and delete the copies. If NOT identical (some take only non-negative input, some guard
  negatives) → keep the exact semantics each call-site relies on; do not "fix" a divergence into existence.

**Family 2a — signature-derived diatonic mask (from `fifths`, key-agnostic):**
- `diatonicMaskFromFifths` in `cadencekeyanchor.cpp` and `tonicizationlabeler.cpp` (CC reported identical).
  **Verify the two bodies are byte-identical, then extract one** shared `diatonicMaskFromFifths` to the header.

**Family 2b — local-key tonic+mode collection (a DIFFERENT primitive from 2a):**
- `lmdCollectionMask(int tonicPc, bool minorMode)` (`section/localmodulationdetector.cpp:62`) and
  `jkdCollectionMask(int tonicPc, bool isMajor)` (`section/jointkeydecision.cpp`). **Cowork VERIFIED the bodies
  are identical** (same `kMajor`/`kMinorHarm` tables, same loop) **EXCEPT the boolean is inverted** — one takes
  `minorMode`, the other `isMajor`. **Extract one shared function with a SINGLE explicit convention** (pick one,
  document it) and **adapt the inverted call-site** (negate the argument). This is byte-identical in OUTPUT but
  requires care at the call boundary — get the inversion right or the masks flip.
- The dependent readers (`jkdInCollectionFraction`, `jkdRootDiatonic`, `lmdRootIsDiatonic`,
  `lmdOutOfCollectionCount`) may also be duplicated — extract only the ones whose bodies you VERIFY identical.
  Leave any that differ.

**Do NOT touch:** `keyScale` (the ordered 7-degree builder, unique to `tonicizationlabeler.cpp` — not
duplicated); `ionianTonicPcFromFifths`/`endsWith` (already shared). Do NOT merge family 2a into 2b (signature
mask ≠ tonic+mode collection — they answer different questions).

## §2 — Placement + the ODR-prefix removal
- Put the shared functions in `mu::composing::analysis` — either extend `analysisutils.h` or add a sibling
  `analysis/pitchclassutils.h` (your call; if you add a file, a pc/key primitive under `analysis/` is cleaner
  than under `analysis/chord/`). `inline` in the header is the correct unity/jumbo-build-safe form.
- **The whole point of the `lmd*`/`jkd*` prefixes was to dodge an ODR clash in the unity build** (documented in
  those files). Once the functions live once, in a header, with `inline` linkage, the prefixes are removed and
  the ODR concern is resolved correctly. **The unity/jumbo build MUST compile** — this is the one real build
  risk; confirm it.

## §3 — The byte-identity proof obligation (MANDATORY, before you trust the refactor)
1. For every function you merge, **diff the original body against the shared one** (accounting for the family-2b
   bool inversion) and state they are character-identical in computed output. Anything not provably identical
   stays separate — do not unify on faith.
2. Build clean (`setup_and_build.bat` via `Start-Process`); the **unity build must compile**.
3. **Both test suites pass:** `composing_tests.exe` AND `notation_tests.exe` (includes `pipeline_snapshot_tests`).
4. **Pipeline snapshots ZERO-diff — do NOT pass `--update-goldens`.** This is a pure refactor; if any golden
   moves, the extraction changed output → it is WRONG → revert and find the divergence (most likely the
   negative-pc handling or the family-2b bool inversion).
5. **BIR byte-identical on all three presets (Baroque 57 / Jazz 23 / Default 57)** via the canonical tools
   (`run_bach_preset.py` + `characterise_bir_false.py` per CLAUDE.md). Same case-identity set, not just the
   integer.
6. No scoring term touched → **no `docs/scoring_model.md` sync required** (confirm you touched no
   template/bonus/guard/gate; this is utilities only).

## §4 — Workflow + deliver
- **Commit LOCALLY (unpushed).** Do NOT push. Write `cc_step1_pc_primitive_report.md`: what you extracted, the
  byte-identity proof per function (incl. the normalizePc consolidation decision + the family-2b inversion),
  the placement choice, the unity-build confirmation, and the four gate results (both suites, snapshot
  zero-diff, BIR 57/23/57 identical).
- Cowork then verifies at the committed object: the new header, every rewritten call-site, that each removed
  body was byte-identical to the shared one, and that the gates held. Revert if anything moved.

## §5 — Stop conditions (any → STOP, do not push, surface)
- Any pipeline-snapshot golden diff, any BIR case-identity change, any test failure → the refactor is not
  byte-identical → STOP + revert + report the divergence.
- A function you assumed identical is NOT (negative handling, the bool sense, a table difference) → do NOT
  unify it; leave it separate and note it.
- The unity build fails to compile → STOP (ODR/linkage); fix the header linkage or report.
- Any temptation to "improve" a primitive while extracting it → STOP. Extraction only; no behavior change.
