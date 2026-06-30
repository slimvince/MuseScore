# Upstream merge-risk inventory — recorded for the eventual merge boundary

> **Status: reference, recorded 2026-06-30.** A forward-looking inventory, **not** an active breakage and **not**
> a merge. Provenance: a **read-only** investigation by CC (`git fetch upstream` updated remote-tracking refs only;
> no working tree / index / local branch touched, nothing merged). The git facts below are CC's findings,
> transcribed here so they survive to the merge boundary (they will be long out of context by then). The
> **recommendation** (defer) is Cowork's architectural read.

## Recommendation (Cowork): defer the merge to the engage / pre-inference boundary
Do **not** merge mid-rebuild. The entire current verification regime is **byte-identity against a frozen
baseline** — every dormant layer step signs off as "53/24/53 unchanged BY CONSTRUCTION." The highest-risk
upstream change (`clampEnharmonic`, item 2) feeds the spelling-aware Layer-4 root pin **and** the BIR gate;
merging it now would move that baseline and force a gate **re-baseline in the middle of the layer rebuild**,
polluting the clean byte-identity story — for **zero current benefit** (no upstream commit touches
`src/composing/`; no active breakage). The natural merge point is the **stable boundary already parked in the
plan — the pre-inference / engage boundary**, where a gate re-baseline is expected anyway. Merge there, on
purpose; not now, by opportunity.

## ★ Operational gotcha — a future merge MUST target `upstream/main`
Upstream renamed its default branch **master → main**. `upstream/master` is now **frozen** at `3c30b9676a`
(May 8) — the **exact point we already merged**. `deprecated_master` ends May 15 (an ancestor of `main`); all
development since lives on `upstream/main`. So a future merge that targets `upstream/master` would pull
**nothing** and silently look "up to date." **Any future merge must point at `upstream/main`.**
(`upstream/4.7` is a separately-diverged release branch, not our dev line.)

## The fork-only HARD STOP is not a blocker for merging IN
The distribution constraint (CLAUDE.md) forbids pushing/PR'ing `cfc7eb5e39` **toward** `musescore/MuseScore`
(the *outbound* direction). A `git merge upstream/main` pulls upstream **into** the fork — it cannot carry our
patch outbound, so it does **not** trip the rule. The HARD STOP still stands on any `push`/PR targeting
`upstream`; a post-merge push goes to `origin` (`slimvince/MuseScore`) only, as always.

## Baseline points (CC, 2026-06-30)
- **Last-merged upstream point (merge-base):** `3c30b9676a` (May 8), brought in by the May-11 merge `d6ddb6a3b1`.
- **Live upstream line today:** `upstream/main` at `bbca7f0410` (Jun 30) — **555 commits ahead**.

## Local patches — direct-clobber status (all clear)
| Patch | Upstream commits touching the exact site | Status |
|---|---|---|
| `addKey()` dedup guard — `importmusicxmlpass2.cpp` (Stage-4a, `cfc7eb5e39`) | 0 (the 11 commits on this file are elsewhere) | **Not clobbered** |
| Windows Snap fix — `muse/.../winwindowscontroller.cpp` | 0 (muse advanced 165 commits, none here) | **Not clobbered** (in pointer `b9604805a3`, clean tree) |
| composing's `notationaccessibility.cpp` | 0 | **Clean** |

## Fork-relevant upstream changes (CC's verified merge-risk inventory)
1. **MusicXML `<mode>` round-trip refactored — same subsystem as the Stage-4a fix.** Import `d846f61285`
   "simplify mode setting" rewrote the `<mode>` parser in `MusicXmlParserPass2::key()` to
   `TConv::fromXml(…, KeyMode::UNKNOWN)`; export (`exportmusicxml.cpp`) replaced the explicit `KeyMode` switch
   with `if (mode != UNKNOWN) tag("mode", TConv::toXml(mode))`. **Not a direct conflict** with our `addKey()`
   guard (different function), but **adjacent** and it changes the none/custom edge of mode handling. Our 79
   zero-sig stems use `<mode>minor</mode>` (preserved) so the patch premise holds — **re-verify the
   none→`setCustom(true)` behavior at merge.** **Silver lining:** if this refactor already fixes #9444, our
   fork-local patch can **retire** — and the distribution-constraint worry on `cfc7eb5e39` dissolves with it.
   Check at merge.
2. **Pitch-spelling / TPC — `pitchspelling.cpp` `94da206551` "Fix clampEnharmonic conditions."** TPC/enharmonic
   output feeds the spelling-aware Layer-4 root pin **and** the planned Stage-5/6 two-tier gate. A
   `clampEnharmonic` change can shift the TPCs the analyzer sees → could move spelling-derived roots / gate
   baselines. **Highest behavioral-watch item — re-run the BIR gate at merge.**
3. **`SegmentType` refactor — `segment.h` `563d853b5d`.** The Layer-2 slicer iterates segments by type; an enum
   refactor is a **recompile-and-verify** item.
4. **Chord-symbol model** (the analyzer emits `Harmony`): `chordlist.cpp` `5283680402` "Fix inverted `isEmpty()`
   check"; `harmony.cpp` `b66c0eafa1` "Find correct segment for harmony when drawing."
5. **Note model — `note.h`:** "Stave sharing" `c367181e2b`, tie-mask refactors.
6. **Build system — broad churn** in `CMakeLists.txt`, `SetupConfigure.cmake`,
   `buildscripts/cmake/{DependencyManifest,SetupDependencies,SetupQt6}.cmake`, etc. The classic
   merge-breaks-the-build surface; a merge may pull new dependency versions our `setup_and_build.bat` /
   `ninja_build_rel` flow must absorb.
7. **`muse` submodule — 165 commits ahead** (`b9604805a3` → `8c223d87b9`). Our Snap-fix file is untouched
   upstream, so re-applying on a bump is conflict-free — but per CLAUDE.md a bump must **carry `cfc7eb5e39`-style
   local fixes forward**.

## At the merge boundary — the checklist
1. Merge against **`upstream/main`**, never the frozen `master`.
2. Scrutinize the **`<mode>` round-trip refactor** (item 1) — re-verify the declared-mode import patch + the
   none/custom edge; check whether it already fixes #9444 (→ retire our patch).
3. Re-run the **BIR gate** after the **`clampEnharmonic`** change (item 2) — the spelling-aware path is sensitive.
4. Recompile-and-verify the **`SegmentType`** enum change (item 3) against the Layer-2 slicer.
5. Absorb the **build-system + submodule churn** (items 6, 7) — "make it compile again," carrying local fixes forward.
6. Bottom line (CC): nothing here affects current work — no upstream commit touches `src/composing/` (it's our
   code; upstream doesn't have it). This is forward-looking risk, not active breakage.
