# CC Instruction — Step 3D: PUSH the dormant commit to the fork (topology-safe) → then B (#4 guard scoping)

> **Ratified (user, 2026-06-15): push.** Publish the landed J-key-iii dormant commit (`5fee657578`) + its
> ancestors to **origin = the user's fork**, topology-safe (no upstream, no submodule push, hook runs), then
> proceed to the already-written **instruction B** (#4 dominant/subdominant guard scoping, read-only).
> **Push from CC's live worktree — it is authoritative for git state (the sandbox index is stale; handoff
> standing note).**

---

## §1 — Pre-push verification (confirm + surface scope BEFORE pushing)
- **Remote:** confirm `origin` = `https://github.com/slimvince/MuseScore` (the user's FORK) for push, and
  `upstream` (musescore/MuseScore) push is **disabled**. Push goes ONLY to origin.
- **Scope:** confirm `git log --oneline origin/master..HEAD` is **exactly these 3 commits** and nothing more:
  - `5fee657578` J-key-iii dormant wiring
  - `2245aedf82` 4c cadence instrument
  - `cfc7eb5e39` **Stage-4a MusicXML import local patch** ⚠ — this publishes 4a to the FORK. It is an
    ancestor of J-key-iii (cannot be excluded without history rewrite), it is ratified, and the sibling 4b-i
    patch is already on origin, so this is consistent + contained (upstream push is disabled). **If the
    scope is anything other than these 3 commits → STOP and report.**

## §2 — The push (topology-safe)
- Run: **`git push --no-recurse-submodules origin master`**
  - **`--no-recurse-submodules`** keeps the `muse` submodule's **Snap fix** (`b9604805a`,
    `fix/windows-snap-ptmintracksize`) **LOCAL** — it must NOT be pushed.
  - **Let the pre-push hook run** (`.git/hooks/pre-push` — blocks only `chords.xml`, which these commits do
    not touch). **Do NOT use `--no-verify`.**

## §3 — Post-push verification (CC's worktree is authoritative)
- Confirm `git rev-parse origin/master` now = `5fee657578`.
- Confirm the push output pushed **only main-repo refs** (no submodule push) — the `muse` Snap fix stays
  local. `git submodule status` unchanged (`b9604805a`).
- Report the push output + the new `origin/master`.

## §4 — Then proceed to B (read-only, no commit)
After the push is confirmed, execute **`cc_instruction_b_dominant_subdominant_guard_scoping.md`** — the
read-only investigation that locates the I→IV/I→V over-detection on the 3 non-chorale regression scores,
measures whether the tonicization-vs-modulation discriminator is separable (suppress the regressions WITHOUT
breaking Bach modulation precision), and designs the #4 guard. **No code change in B.** Its dossier unblocks
the eventual global flip-ON.

## §5 — Stop conditions
- Push target ≠ origin/the fork, or ANY push to `upstream` → STOP.
- `--recurse-submodules` / the `muse` Snap fix being pushed → STOP (keep it local).
- The pre-push hook fails or blocks → STOP, report the hook output (do NOT `--no-verify`).
- `origin/master..HEAD` is anything other than the 3 expected commits → STOP, report (do not push an
  unexpected scope).
- In B: any code change / no separable threshold / a guard that would suppress genuine Bach modulations →
  STOP + surface (per B §5).
