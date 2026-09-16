# CC Instruction — SYNC docs/implementation_roadmap.md (hold the un-ratified joint-inference out)

> User decision (2026-06-21): bring the roadmap current with the ratified/current content, but **HOLD OUT the
> un-ratified 2026-06-15 "CONSTRAINED JOINT INFERENCE" re-grounding** — exactly as the `ARCHITECTURE.md`
> forward-pointer is held. The roadmap's working tree carried a large pre-existing WIP (≈509 lines) that is mostly
> legitimate current content (the 06-14 user mandates, the 06-13 corrections, the layer status) **plus** the one
> un-ratified joint-inference block. Commit the legitimate content; strip the joint-inference block. **Doc-only.**
>
> **Sequencing:** run **after** the Layer-2 fork push (`cc_instruction_push_layer2.md`), so the roadmap can cite
> `origin/master = e470e2667e` and L2 as pushed.
>
> **★ Provenance you do NOT have (do not re-derive):** the "constrained joint inference" re-grounding is an
> **investigation-gated, NOT-yet-ratified** direction. Its full design lives in `docs/architecture_joint_inference.md`
> (its held home — **do NOT touch that file; nothing is lost by omitting its pointer here**). It is also held as the
> unstaged `ARCHITECTURE.md` 2026-06-15 forward-pointer. The roadmap must **not assert it as the plan** until
> ratified. This is the same hold you already honor in `ARCHITECTURE.md`.

## §1 — Edit the working-tree `docs/implementation_roadmap.md` (strip is surgical)
Start from the current working-tree file (the WIP). Make exactly these changes; change nothing else:

1. **Remove the joint-inference re-grounding block in full** — the contiguous paragraph that begins:
   `**★★ BACK-HALF ARCHITECTURE RE-GROUNDING (2026-06-15): CONSTRAINED JOINT INFERENCE.**`
   and ends:
   `… Stages 4–7 below are re-interpreted under this target as it ratifies.`
   Delete the whole paragraph and tidy surrounding blank lines / `---` separators so the **06-14 LAYER-BY-LAYER
   AUDIT** block flows cleanly into the **UPSTREAM-FIRST LAYER REBUILD (2026-06-21)** block (one separator, no
   double blank).

2. **Remove the dangling forward-reference** at the end of the layer-rebuild block. The sentence currently reads
   (≈line 62–64): `… This upstream-first arc interleaves with — does not replace — the Stage 0–7 plan below; the
   constrained-joint target above is the L3 shape.` → drop the clause `; the constrained-joint target above is the
   L3 shape`, ending the sentence at `… the Stage 0–7 plan below.`

3. **KEEP, do not touch:** the 06-14 "TWO DEFERRED STRUCTURAL REFACTORS" block and the 06-14 "LAYER-BY-LAYER AUDIT"
   block (both ratified user mandates), the whole Stage 0–7 body, the Traceability/Relationship sections. (Deferred
   refactor #2 names "dissolution of the post-hoc gate layer into fitted weights" — that is the ratified *mandate*,
   not the joint-inference *solution*; leave it.)

4. **Update the layer-status table to the ratified/pushed state** (this is the owed Layer-2 entry):
   - **L2 row** → status `✅ DONE + RATIFIED + PUSHED (2026-06-21)`; drop "pending Cowork verify + user ratify";
     add `origin/master = e470e2667e` to its evidence. Keep the rest of the L2 evidence (it is Cowork-verified).
   - Update any **current** `origin/master =` pointer that now reads `4055f89082` to `e470e2667e` (the fork HEAD
     after the L2 push). Leave L1's *historical* push-point reference (`4055f89082` as L1's coverage commit) intact
     where it documents L1's own evidence — only the "current fork HEAD" pointer changes.

## §2 — Verify the strip before committing
- `grep -niE "joint inference|constrained joint|joint decision|joint decoder|re-grounding" docs/implementation_roadmap.md`
  → must return **nothing** (the block + the dangling clause are the only occurrences; confirm none remain).
- Confirm the 06-14 mandates + the layer-status table are still present, and the L2 row reads DONE/RATIFIED/PUSHED.
- Confirm `docs/architecture_joint_inference.md` is **unchanged** (the joint-inference design's held home).

## §3 — Commit (doc-only, roadmap only) + push
- Stage **only** `docs/implementation_roadmap.md` (`git add docs/implementation_roadmap.md`). Confirm
  `git diff --cached --name-only` = that one file. The `ARCHITECTURE.md` forward-pointer hunk and the held B2 files
  stay **unstaged** (do not stage them).
- Commit: `docs(roadmap): sync to current plan + Layer-2 status; hold the un-ratified joint-inference re-grounding out (mirrors ARCHITECTURE.md)`.
- Push to the **fork only**: `git push --no-recurse-submodules origin master`. **NEVER `upstream`** (disabled;
  leave it). Verify `git ls-remote origin master` = the new commit; confirm `upstream` still `disabled (push)`.

## §4 — STATUS.md + deliver
- STATUS.md: note the roadmap is now in sync (layer status current; joint-inference held out, consistent with
  ARCHITECTURE.md); fork advanced to the roadmap-sync commit.
- Report: the strip diff (the removed block + clause), the `grep` = empty proof, the L2-row update, the commit hash,
  the `ls-remote` confirmation, and that `architecture_joint_inference.md` is untouched.

## §5 — Stop conditions
- The grep in §2 still finds a joint-inference assertion after the strip → STOP (under- or mis-removed); surface.
- Removing the block would also remove 06-14 mandate or layer-status content → STOP (over-removal); the strip is
  ONLY the 06-15 block + the one dangling clause.
- Any non-roadmap file gets staged, or any push targets `upstream` → STOP.
- The roadmap edit turns out to require touching `architecture_joint_inference.md` or `ARCHITECTURE.md` → STOP
  (out of scope; this is roadmap-only).
