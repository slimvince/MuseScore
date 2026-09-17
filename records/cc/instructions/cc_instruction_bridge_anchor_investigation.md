# CC Instruction — Bridge cadence-anchor mis-resolution: READ-ONLY investigation

> **The B2 negative re-located the blocker.** The subdominant guard is byte-identical + full-score
> precision-positive but does NOT clear the snapshot regressions (0/3): on the bridge/notation path the
> cadence ANCHOR itself mis-resolves (mozart→F, corelli→Gm), upstream of the guard. This step finds out
> **why** — and specifically whether it is a *test-fixture / windowing* artifact (targeted-fixable) or the
> *signal-calibration* wall — before any fix is designed. **Read-only. No code change. No guard commit.**
> First: confirm the B2 guard is NOT committed (HEAD `5fee657578`); recommend reverting it from the working
> tree (its findings live in `cc_b2_subdominant_guard_report.md`).

---

## §1 — The decisive question (resolve this FIRST, at source)

**Is the bridge anchor's mis-resolution a windowing/excerpt artifact, or a real production behavior?**
- **The snapshot test fixtures:** are they **short excerpts** (e.g. 16 measures) or full scores? If the
  `pipeline_snapshot_tests` fixtures for mozart_k279 / corelli / bwv806 are truncated excerpts, the
  "16-measure window" is a TEST artifact, not production.
- **The bridge/notation production path:** does it analyze the **whole score** or analyze in **windows/
  chunks**? Where is the cadence anchor computed, and over what span — the full region stream, or a
  per-window subset? Cite `file:line`. Compare to the **batch** path's scope (which produced the *stable*
  full-score anchor: mozart C 0.679 / corelli C 0.423).
- **Verdict to reach:** (H1) test-excerpt/windowing artifact — a full score in production would feed the
  anchor full context and (likely) resolve correctly → the snapshots OVERSTATE the production problem; or
  (H2) the production bridge genuinely windows → the anchor instability is real in production and the
  batch full-score win does not fully reflect it.

## §2 — Measure the anchor under full-score vs windowed context

On mozart_k279 / corelli / bwv806 (the 3 regression scores):
- What cadences does the **bridge/windowed** anchor see vs the **full-score** anchor? Does the windowed
  anchor mis-resolve because it sees **too few cadences** (windowing/context) or because the cadences it
  sees are themselves **wrong** (calibration)?
- **The H1 test:** if the bridge anchor were given **full-score context** (the same input the stable batch
  anchor uses), would it resolve correctly (mozart→C, corelli→?) and would the snapshot regressions clear?
  (Use the existing `--dump-cadence-anchor` / `--dump-modulation` diagnostics; no rebuild needed for the
  full-score anchor — it is already measured.)

## §3 — Characterize the residual (the calibration-wall test)

Even under full-score context, **corelli's anchor is already low-confidence (C 0.423)** — borderline. So:
- Does full-score context fix **mozart** (anchor C 0.679, strong) but leave **corelli** (0.423) still
  mis-resolving? I.e. is mozart an H1 (windowing, targeted-fixable) case while corelli is an H2 (calibration,
  the recurring wall — low-confidence anchor on a partial-signature minor piece, the J-key-ii-redux class)?
- Quantify: of the non-chorale blocker, how much is windowing-fixable vs calibration-floor.

## §4 — Output: the cause + the fix-or-wall verdict (dossier, no code)

Write `cc_bridge_anchor_investigation_dossier.md` (gitignored, HELD): the §1 verdict (test-excerpt /
production-windowing / calibration, cited at source), the §2 full-score-context measurement (does it clear
the regressions), and the §3 residual split (mozart-windowing vs corelli-calibration). Frame the **two
possible next directions** so the user can choose: (A) a **targeted bridge-anchor-context fix** (feed the
anchor full-score context on the bridge path — if H1 carries most of the blocker), vs (B) accept the
residual as the **calibration wall** (corelli-class) → the global flip stays gated, and the key win is
locked in for the measured Bach-chorale repertoire (dormant/scoped) pending the calibration/learned work.
**Do not build either — surface the measured verdict for a user/Cowork direction call.**

## §5 — Stop conditions
- Any code change / fix built / guard committed in this step (read-only) → STOP.
- The bridge analysis scope cannot be determined at source → cite what IS known + surface the gap; do not
  guess windowed-vs-full.
- Uncertain whether a case is windowing vs calibration → measure both framings; bucket + surface — never
  guess.
