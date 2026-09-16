# CC Instruction — Phase 5c Step-M consolidation: commit the corrected §5.6 + STATUS checkpoint (docs only, no code)

> **Docs only. No code change, no build, no measurement, no engage.** Your STOP finding was correct and is accepted in
> full: the `V/iv`-on-tonic over-trigger is an inference problem (the major-tonic / `V/iv` pitch-class identity), **not** a
> guard-completion gap. Cowork has corrected §5.6 accordingly. This task records the corrected state in the repo so the
> false "fully-diatonic guard gap" premise does not sit unstaged. **Default constants. No production movement.**
> *(Reminder: the never-bash rule is Cowork's.)*

## §0 — What was decided (context, not an instruction to act on)
- The over-trigger is **re-ruled** as the §5.3–§5.5 inference family (deferred by the firewall — no inference-fixing until
  structural completion is done). My earlier "fix now as completion" ruling is **void** (it rested on my music-theory
  error; you caught it).
- The §5.6 amendment is **already corrected by Cowork** in `cowork_layer5_function_design.md` (the false universal-
  precondition / "fully-diatonic `I→iv`" bullet was reverted and replaced with the accurate inference-deferral note). You
  do **not** edit the spec — only commit it.
- **Engagement is dropped as a near-term goal.** Production is out of scope; the posture is **build + validate every layer
  dormant, compared byte-identically against the fixed references** (the legacy code and the DCML ground truth). L5 stays
  dormant.

## §1 — Commit the corrected Cowork doc (local, unpushed)
- Stage and commit **only** the tracked Cowork doc change(s) — `cowork_layer5_function_design.md` (the corrected §5.6 note),
  plus any other unstaged tracked Cowork `*.md` design docs that are part of this correction. Do **not** stage gitignored
  reports or instruction files.
- Message: `docs(cowork): re-rule V/iv over-trigger as §5.3–§5.5 inference; revert false fully-diatonic guard premise`.
- Report the sha and the exact file list in the commit (so Cowork confirms only the intended doc moved).

## §2 — STATUS.md checkpoint
Add a STATUS.md session entry recording, factually:
- **L5 is structurally complete and dormant**, Step-M-validated against DCML (additive — 0 class-(b)/(a) on all three
  presets; BIR identity sets unchanged **53/24/53**; RN-agree vs DCML **+2.48/+1.91/+2.32**; §5.6 applied guard DCML-
  correct ~92%).
- The **`V/iv`-on-tonic over-trigger** (62/29/56 units; 12/6/13 would-be regressions) is **re-ruled as inference**
  (major-tonic / `V/iv` pitch-class identity, tonic-rooted) — a **recorded input to the eventual §5.3–§5.5 inference
  phase**, not a structural defect; deferred, not lost.
- The **tonicization-vs-modulation residual** is the other recorded §5.4 inference-phase input.
- **Engage (Phase 5d) is deferred indefinitely** — production is out of scope; the mission is dormant build + ground-truth
  validation. Next **structural** work: **L6 (grouping)**, to be designed research-first by Cowork before any build.

## §3 — Gate (docs only)
- After the commits: working tree clean (only gitignored reports/instructions remain untracked); **HEAD advances by the
  doc commit(s) only**; **no** `src/` or `tools/` code change; corpus untouched (no measurement run needed — this is docs).
  If anything other than tracked Cowork docs + STATUS would be committed → STOP and report.

## §4 — Deliver
Report the two shas (the doc commit + the STATUS commit, or one combined if you prefer), the committed file list, and
confirmation the tree is clean. **Nothing else** — no build, no tests, no measurement.

## §5 — Stops
- Any `src/`/`tools/` code change, any build/test/measurement, any engage or production switch, any edit to the spec
  content (you commit it, you do not author it) → STOP. `upstream` → STOP.
