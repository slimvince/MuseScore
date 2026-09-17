# CC instruction — OI-168: measure the δ tonic-dependence magnitude (build + default-OFF instrumentation)

**Dispatch author:** Cowork, 2026-07-13. **Type:** a MEASUREMENT build — default-OFF instrumentation + a
default-OFF signature-mask A/B variant. **The default production path is unchanged and must regenerate the
committed corpus byte-identically; NO fix is promoted to default here.** The single deliverable is the
measured magnitude of the OI-168 defect, which decides the fix's path. The fix itself is a separate,
ratified step.

**Why (what the number decides).** OI-168: `analyzeChord`'s two key-consuming terms
(`dim7CharacteristicBonus` `chordanalyzer.cpp:575`, `diatonicRootContribution` `:902`) test membership in
`{keyTonicPc + scale[i]}`, and the tonic cancels only when δ=0 — false for `Altered` (offset 1) and
`AlteredDomBB7` (offset 8), which the engaged decoder scores against a mis-transposed collection. The break
is confirmed at the code; the fix (swap both loops to `pcInMask(diatonicMaskFromFifths(keySignatureFifths),
pc)` — `analysisutils.h:77/87`, signature-only) is confirmed available. **Unknown:** whether the corrupted
bonus ever actually flips a committed chord, or is a latent miscalculation that never changes a winner. That
magnitude decides the fix path — **byte-identical structural hardening (0 flips)** vs a **correctness
re-baseline (>0 flips, O-12 + goldens + your ratification)** — and measuring after deciding would be
choosing blind (#9/#19). Measure first; the fix follows on a known number.

Read first: `CLAUDE.md` (esp. the build/test commands + the VS Code bash rules), `OPEN_ITEMS.md` (OI-168,
OI-167, OI-110 for the default-OFF instrumentation byte-identity precedent), the audit report and
`cc_oi167_collection_tonic_report.md`, and the code.

---

## 1. Governing constraints

- **Byte-identity of the default path is the success condition for the instrumentation.** Follow the
  OI-110 pattern: all counters and the A/B variant are default-OFF, and with them OFF the corpus
  regenerates sha256-identical and the establishment battery + both C++ suites are unchanged. If the OFF
  build is not byte-identical, the scaffold is not inert — STOP.
- **No fix is promoted to default.** The signature-mask form is exercised ONLY through the opt-in variant
  for the A/B. The production terms stay as-is until the fix is separately ratified.
- The Premise Gate (#17): write the §6 predictions BEFORE measuring. Verify at the objects. Fork-only push
  (origin only). The VS Code bash rules (`; echo "exit:$?"`, redirect large output to a file). Self-check
  the diff before reporting.

## 2. Task 0 — register commit

Commit any waiting Cowork register/handoff edits (verify `git status --porcelain`; STOP if the tree differs
from expected). Leave `cowork_joint_key_chord_design.md` unstaged.

## 3. Task A — the Aeolian guard zero-fire, with a real counter

CC's OI-167 report inferred the `sparsechordrefinement` Aeolian guard's zero-fire from the output surface
(no `Unknown`-quality lone-pitch-class region). Confirm it with a **default-OFF branch counter** at the
guard itself (`sparsechordrefinement.cpp:154-159`): count entries and fires across all three corpora.
Expected: 0 fires. Report the counts.

## 4. Task B — the Altered / AlteredDomBB7 population, with a real counter

Confirm the emitted population with instrumentation, not the output-surface estimate (24 Jazz): count the
regions the engaged decoder scores under `keyMode ∈ {Altered, AlteredDomBB7}` on each preset
(Baroque/Jazz/Default). Report the per-preset, per-mode counts.

## 5. Task C — the A/B: does the tonic-corrupted bonus flip a committed chord? (the crux)

Add a **default-OFF variant** that swaps the two membership loops to
`pcInMask(diatonicMaskFromFifths(keySignatureFifths), pc)` (byte-identical for the 19 δ=0 modes by
construction — the diatonic collection is the same set). Run the corpus **current vs variant** on all three
presets and **diff the committed chords** (`.ours.json`):

- Report the total committed-chord flip count per preset, and **specifically on the Altered/AlteredDomBB7
  regions from Task B** — how many of those regions change their committed chord, and to what.
- For every flip, note whether the variant's reading is the musically-correct one (the actual signature
  collection) — since the variant is the *corrected* form, a flip is a case the current code scores wrong.
- If the flip count is 0 everywhere: the defect is latent (never changes a winner) → the fix is
  **byte-identical** structural hardening. If >0: those regions are the correctness delta the fix carries →
  a **re-baseline**.

**Prove the OFF path inert:** with the variant and counters OFF, regenerate the corpus and confirm sha256
identity vs the committed `tools/corpus` (the OI-110/harness regen pattern), the establishment battery
byte-identical, and `composing_tests` + `notation_tests` + `pipeline_snapshot_tests` green with no golden
refresh. The A/B variant is exercised only through its opt-in flag.

## 6. Premise Gate — predictions before measuring (#17b)

Record first: your predicted committed-chord flip count (total and on the Altered/AlteredDomBB7 regions),
whether you expect any flip at all, and the Task-A/B counts. A gap between prediction and finding is
diagnostic (#3).

## 7. Deliverable

- **A report `cc_oi168_magnitude_report.md`**: the Task-A guard counts, the Task-B population counts, the
  Task-C flip count + per-region detail (with the corrected reading), the predicted-vs-actual, the OFF-path
  byte-identity proof, and a **fix-path recommendation** — byte-identical hardening (0 flips) or a
  correctness re-baseline with the golden/region list (>0 flips). The fix itself is NOT applied; its
  application + ratification is the next step.
- **Commit:** the default-OFF instrumentation + A/B variant (byte-identity-proven, the OI-110 pattern) as a
  `feat(tools)`/`feat(composing)` default-OFF commit, plus the report as a `docs(cc)` fold, plus
  `STATUS.md`/`cowork_handoff.md` notes. Force-add this instruction file. No golden refresh, no fix
  promoted, `tools/robust_stop`/`tools/corpus`/goldens untouched.
- **STOP-and-report** if the OFF build is not byte-identical (the scaffold isn't inert), or if the flip
  count is large or surprising (report the magnitude; do not apply or promote anything).

**On completion:** the fix path is known on a measured number. If 0 flips, the next step is the
byte-identical structural hardening (apply the signature-mask form as default, ratified behavior-neutral);
if >0, the next step is the correctness re-baseline (O-12, goldens, your ratification). Either resolves
OI-168 and clears OI-167's premise; then the OI-166 cadence-vote precision probe proceeds, with the
key-layer funnel still shut until the corrected layer assignment is ratified as a whole.
