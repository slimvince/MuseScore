# CC — Layer 1 documentation-sync report

> Standing rule (user, 2026-06-21): **all documentation is kept in sync with the code; doc drift is
> a defect.** Layer 1 (note model, `e30bb45a4f`; coverage `4055f89082`) shipped with no
> canonical-doc updates — closed here. **DOC/COMMENT-ONLY; no production/behavior change.** Local
> commit (unpushed); Cowork verifies doc-only + as-built accuracy; user ratifies.

## §1 — Edits made (tracked canonical docs)
1. **`ARCHITECTURE.md`** — added an as-built subsection **"Layer 1 — the lossless note model
   (note-model rebuild, 2026-06-21, as-built)"** before "Region Analysis — Canonical Modules":
   the `notemodel/` module, its role (lossless source of truth), the **11 fields**, the two derived
   views (`weightedPcView`/`soundingAt`), the statement that `collectRegionTones`' note-reading is
   now the model and its weighting is `weightedPcView`, the **transitional** framing of the
   still-live segment-first spine, the 4-layer target pointer (L2 next), and the ratified
   +3/+1/+1 trade-off. Also amended the `regiontonecollector` row to "derived tone views over the
   Layer-1 note model" and suffixed the "Region Analysis — Canonical Modules" heading with
   "note-reading half superseded by Layer 1." (39 insertions / 2 deletions.)
2. **`docs/implementation_roadmap.md`** — added the **"★★ UPSTREAM-FIRST LAYER REBUILD (2026-06-21)"**
   status block before "## Stage 0": the 4-layer table with **L1 = ✅ DONE/RATIFIED/PUSHED + evidence**
   (`edd33901ed`/`e30bb45a4f`/`4055f89082`, gate counts, the +3/+1/+1 trade-off), **L2 = NEXT**,
   L3/LN pending, and the transitional-spine note.
3. **`docs/layer_architecture_audit.md`** — one dated supersede banner at the top ("Superseded for
   Layer 1 by the note-model rebuild (2026-06-21)"), pointing to the as-built ARCHITECTURE.md
   section + the 4-layer target. (It is a historical 2026-06-09 audit; banner suffices per spec.)

## §2 — Code comment fix (verified at source) — already correct, no edit needed
The §0 "verified stale" comment — `regiontoneprimitives.cpp` header "**4 quarter notes**" vs the
`Fraction(4,1)` (= 4 **whole** notes) — was **already corrected by the layer-1 rewrite**: the
`collectSoundingAt`/`soundingAt` header doc now reads "True-span overlap — no horizon" and
"no 4-whole-note backward cap" (`regiontonecollector.h`), and the sole remaining `Fraction(4,1)`
(`regiontonecollector.cpp:157`, the pedal-tail backLimit) carries an accurate "[start − 4 wholes, end)"
comment. Repo-wide `grep "4 quarter"` over the §1 files = none. So no comment edit was required;
verified, not skipped.

## §3 — Drift sweep findings
- **Module/view comments** (`notemodel/`, `engravingbridge/*.cpp`): all accurate as-built (written
  fresh in the layer-1 commit — "single source of truth", "build the note model and derive",
  "Legacy ordering fidelity: collectSoundingAt emitted …"). No stale ownership claims found.
- **`docs/scoring_model.md:38` "Tone collection. Build a 12-element PC histogram from the input
  tones"** — **accurate, not changed.** It describes the chord-scoring (Layer 3) *input*; that
  input is now the `weightedPcView` histogram. It does not imply the analyzer reads notes directly.
- **Listed, not chased** (out-of-scope per §3 — soon-to-be-replaced Layer-2/3 helper/detector code):
  - `src/composing/analysis/scoreharvest/metricweights.h:60` and `:66` — two "4 quarter notes"
    parentheticals (beat-decay helper / Pass-2b detector); the `:66` one may be genuinely stale
    (the detector default is `2*DIVISION`), but it is Layer-2 detector-adjacent → fix when that
    layer is rebuilt.
  - `docs/layer_audit_plan.md:94` — labels `regiontoneprimitives.cpp` as "tone collection"; a
    planning doc that evolves with the layers (and Cowork-owned planning surface) → left.
  - Historical recon docs (`divergence_d_recon.md`, `duplication_audit.md`,
    `iter92_joint_bass_chord_scoring.md`, `redesign_plan.md`) mention "tone collection" as records
    of past states, not current-ownership claims → left.

## §4 — Commit hygiene (★ pre-existing HELD edits excluded)
`ARCHITECTURE.md` and `docs/implementation_roadmap.md` carried **substantial pre-existing HELD,
uncommitted doc edits** (e.g. the ARCHITECTURE.md 2026-06-15 "FORWARD POINTER … investigation-gated
— NOT yet a ratified stable decision" block; the roadmap re-baseline/deferred-refactor/back-half
blocks). Per the established HELD discipline (and because some are explicitly un-ratified), the
doc-sync commit stages **only my Layer-1 edits**: the staged blobs were constructed as
`HEAD + my edits` (LF, matching HEAD), leaving every pre-existing HELD edit untouched in the
working tree. Verified: the staged diff contains **zero** HELD markers and exactly my Layer-1
additions (`git diff --no-index` on the staged vs HEAD blob = 39/2 for ARCHITECTURE.md). The
pre-existing HELD doc edits, the B2 guard, and the gitignored reports remain uncommitted.

## §5 — Gate (doc/comment-only, byte-identical code)
- **Zero source (`.cpp`/`.h`) changes** this round (only `.md` docs) → the analyzer binary is
  byte-identical to `4055f89082`; **snapshot/BIR/oracle unchanged by construction** (corpus not
  regenerated — would be byte-identical).
- **Both suites + snapshots pass:** composing **559**, notation **57**, pipeline snapshots **11/11**.
- Recorded commit diff (authoritative, `git show --numstat`): ARCHITECTURE.md, the roadmap, and the
  audit doc only — all doc files.

## §6 — Deliverable
Single doc-sync commit (local, unpushed): `ARCHITECTURE.md` + `docs/implementation_roadmap.md` +
`docs/layer_architecture_audit.md`. This report (HELD). Fork-only if pushed; never `upstream`.
