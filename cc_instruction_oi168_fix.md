# CC instruction — OI-168 fix (correctness re-baseline, USER-RATIFIED) + OI-167 Aeolian re-home

**Dispatch author:** Cowork, 2026-07-13. **Ratified by the user 2026-07-13.** **Type:** an inference-affecting
**correctness re-baseline** on the governing hard stop (class-(b) −480, removal-only) + a **byte-identical**
L4 re-home. This is architectural completion — making L4 structurally tonic-independent — not
inference-problem-fixing; the one corrected chord is a side effect. Baroque and Default are byte-identical;
only Jazz re-baselines. Follow the re-baseline ritual exactly.

**What the measurement established (`cc_oi168_magnitude_report.md`):** swapping the two tonic-dependent
membership loops to the signature-mask primitive flips exactly one committed chord — `bwv145.5@12960`
(`D#alt`): `Ebm` (root 3) → `B/Eb` (root 11), which the sounding D♯–F♯–B (a B-major triad) and DCML both
confirm — plus 22 score-only changes on Jazz; Baroque/Default byte-identical (δ=0 verified at runtime). The
robust-stop diff is removal-only: class-(b) −480 Jazz, +0/+0 Baroque/Default, zero additions, OVERALL PASS —
a strict improvement.

Read first: `CLAUDE.md` in full (esp. the block-(A) robust-unit re-baseline discipline + the build/test
commands + the VS Code bash rules), `OPEN_ITEMS.md` (OI-168, OI-167, OI-169), `STATUS.md`, and the two
reports `cc_oi167_collection_tonic_report.md` + `cc_oi168_magnitude_report.md`.

---

## 1. Governing constraints (the re-baseline discipline)

- **O-12 first:** snapshot the outgoing `tools/robust_stop/` reference to
  `tools/robust_stop/snapshot_2026-07-13_pre_oi168/` with a `SNAPSHOT_NOTE.md` (what it preserves, why
  superseded) BEFORE any edit.
- **One revertible, provenance-stamped commit for the behavior change** (#14); the re-home is its own
  byte-identical commit.
- **The class-(b) non-increase hard stop must hold** — here it strictly DECREASES (−480, removal-only), so
  it passes; still run the diff and record the explained per-run diff (the single removed run
  `bwv145.5@12960`, zero additions).
- **Goldens refreshed ONLY for the verified-correct change**, never to bless a wrong reading — confirm the
  `bwv145.5` change is toward the notes/DCML before refreshing.
- Premise Gate (#17): write the predictions (Baroque/Default 0 diff; Jazz 9 files; 1 flip; class-(b) −480)
  before regenerating. Fork-only push. VS Code bash rules. Self-check the diff.

## 2. Task 0 — register commit

Commit any waiting Cowork register/handoff edits (verify `git status --porcelain`; STOP if unexpected).
Leave `cowork_joint_key_chord_design.md` unstaged.

## 3. Task 1 — apply the signature-mask fix (the behavior change)

In `chordanalyzer.cpp`, swap both membership loops to the signature-only primitive:
`dim7CharacteristicBonus` (`:574-578`) and `diatonicRootContribution` (`:901-905`) — replace the
`(keyTonicPc + interval) % 12 == pc` scan with `pcInMask(diatonicMaskFromFifths(keySignatureFifths), pc)`
(`analysisutils.h:77/87`). After the swap the terms take **no tonic and no mode-scale** — remove the now-dead
`keyTonicPc`/`scale` parameters and thread `keySignatureFifths` where needed, so tonic-independence is
structural (the point: a future mode-table edit cannot silently reopen this). Update `docs/scoring_model.md`
in the same commit (the §4 entries for these two terms — the sync rule). If a caller has no
`keySignatureFifths` in scope, STOP and report rather than reconstructing the tonic.

## 4. Task 2 — regenerate, verify, re-baseline

- Build, then regenerate all three preset corpora to scratch and diff against committed `tools/corpus`:
  **Baroque/Default MUST be 352/352 byte-identical** (0 differ); **Jazz: exactly 9 files change**. If
  Baroque/Default differ at all, STOP — the δ=0 property was mis-derived.
- **Confirm the one flip** `bwv145.5@12960` reads `B` (root 11) and the other 8 files carry only score
  changes (no committed-chord/root change). Any additional committed-chord flip is a surprise — STOP.
- Run the robust-stop diff (`a8_rebaseline_measure` → scratch, `robust_stop_diff`): confirm **class-(b) −480
  Jazz, +0 Baroque/Default, zero additions, OVERALL PASS**. Re-stamp the `tools/robust_stop/` reference +
  `manifest.json` (new corpus git_hash, the explained removal-only diff) — the 2.2e/O-12 re-baseline
  pattern.
- Refresh any affected `pipeline_snapshot_tests` golden (`bwv145.5` if pinned) toward the corrected reading;
  re-run to confirm pass. Run `composing_tests` + `notation_tests` + `pipeline_snapshot_tests` — all green.
- **Re-stamp CLAUDE.md gate block (A)** and the A-8 baselines with the measured new columns (root-agree Jazz
  improves by the one flip; RN/key as measured; class-(b) −480), with provenance. Update `STATUS.md`.

## 5. Task 3 — OI-167: re-home the dead Aeolian guard (byte-identical, its own commit)

Execute the disposition your OI-167 report proposed for `refineSparseChordQualityFromKeyContext` — re-home
it out of L4 to the presentation surface (it is proven fully dead: 0/0/0, body unexercised across all four
call sites). Prove **byte-identical** (the corpus regenerates identically; 0 fires means 0 behavior change).
This makes L4 cleanly tonic-independent and closes OI-167. If the re-home target is not clean, STOP and
report rather than forcing a cross-layer move — the disposition can then go to the design pass.

## 6. Deliverable and closure

- **Commits:** O-12 snapshot; the Task-1 fix + Task-2 re-baseline as one revertible provenance-stamped
  commit (the behavior change, with the golden refresh + gate-block re-stamp + `scoring_model.md` sync); the
  Task-3 re-home as its own byte-identical commit; a `docs(cc)` fold (`cc_oi168_fix_report.md` — the
  regeneration proof, the explained diff, the new baselines) + OI-167/OI-168 flipped to resolved +
  `STATUS.md`/`cowork_handoff.md`. Force-add this instruction file. Push to `origin` only, `upstream`
  untouched.
- **STOP-and-report** if Baroque/Default are not byte-identical, if any second chord flips, if the
  robust-stop diff is not removal-only −480/PASS, or if the re-home isn't clean.

**On completion:** L4 is structurally tonic-independent, the collection/tonic premise holds (OI-167 +
OI-168 closed), and the next step is the OI-166 chord-free cadence-vote precision probe. OI-169
(`structuralPenalties` unused `extThreshold`) stays declared for its own later magnitude measurement. The
key-layer funnel stays shut until the corrected layer assignment is ratified as a whole.
