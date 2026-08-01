# Claude Code — Standing Instructions for This Repository

## Guiding principles

The standing decision guides for all work in this repository. Every design, build, and
measurement choice is checked against them; they are the guide for making decisions and
override convenience.

1. **Fact- and theory-based coding only.** Build only on established fact and theory —
   published research, public algorithms, public software. Fact-finding (investigative)
   coding is allowed.
2. **Specific research over general.** Most research so far has been general or on
   already-handled topics; target the specific open question.
3. **An unexpected finding means we have failed #1** (and possibly #2, #4, #6). Surprise
   signals that the fact/theory basis was incomplete — treat it as a failure to diagnose,
   not a curiosity.
4. **Long-term goal: maximum-precision inference.**
5. **Investigate when facts may be scarce.** If we are unsure whether facts are scarce,
   gather more facts.
6. **Total unification — no duplication of any code.** One path per concern.
7. **Adhere to layers.** Enhance a layer only with algorithms/methods that belong to it,
   nothing else. Worst case, this forces a layer redesign rather than a cross-layer patch.
8. **No inference-problem-driven coding until all methods and algorithms are implemented
   in their correct layer.**
9. **Test and measure only on corpora known to be non-stale and accurate.**
10. **Documentation always in sync with code.**
11. **Regression test cases always in sync with code; regression-test between iterations.**
12. **No information loss.** Negative/exclusion evidence is information ("finding by exclusion") —
    carry a ruled-out possibility at low confidence rather than dropping it, unless the exclusion is
    recomputable from what is kept.
13. **Surface a surprise as a STOP before building around it** (the operational form of #3).
14. **Every behavior change is user-ratified as one revertible, provenance-stamped commit.**
15. **Verify at objects/data on the full output surface, never at assertion** (winner *and*
    carry, not the winner alone).
16. **Reproducibility.** Every measurement is stamped to corpus-hash + instrument-commit;
    snapshot the outgoing reference before any re-baseline.
17. **The Premise Gate.** Before any inference-affecting design is built or probed:
    (a) a **premise ledger** — every load-bearing causal claim explicitly labeled **FACT**
    (citation to code/measurement), **THEORY** (citation to published research answering the
    *specific* question, #2), or **ASSUMPTION**; (b) a **written quantitative prediction per
    assumption** (fire-rate, magnitude, direction, population) recorded *before* measuring —
    no prediction, no build; (c) a **desk simulation** — trace the mechanism by hand through
    the intended architecture on 3–5 real corpus cases drawn from the known failing sets,
    answering FIRST "does the mechanism FIRE on this case?" (control flow — ratified sharpening
    2026-07-10, the EG-2 desk-sim lesson), THEN "which term moves, by how much?" (arithmetic);
    (d) every **proxy→target
    link is itself a ledger premise** (a structural proxy never stands in for a behavioral
    quantity unvalidated); (e) every **insulation claim** ("X cannot affect Y") must enumerate
    the false-negative path explicitly; (f) **no hand-transcribed measurement numbers** —
    figures enter docs only via generated artifacts (the `manifest.json` pattern).
18. **Unverified causal premises are FORBIDDEN (Class A).** No design may carry load on a
    causal claim about our own system or data that is checkable but unchecked.
19. **Unestablished instruments are FORBIDDEN (Class B).** An instrument, corpus, gate, or
    recorded figure is trusted only after being *positively established* (oracle cross-check,
    derivation of what the measurement unit actually measures, reproduce-check) — never
    because it is merely unfalsified.
20. **Fit/evaluation separation.** No value is graded on data that helped fit it. Every fit
    event declares its held-out data (split or k-fold) and its capacity budget (parameter
    count, regularization, justified against corpus size) BEFORE fitting; the headline claim
    is the held-out figure. A fitted-and-self-measured number is not established (#19).
21. **Ground truth is an instrument too.** The accuracy of ground truth is itself a measured
    quantity — per-axis annotator agreement, not an assumed binary (sharpens #9's "accurate").
    Every precision target and every "irreducible residual" verdict is interpreted against
    that measured ceiling; without it, structural error and annotator disagreement are
    indistinguishable in the residual.
22. **Every hard gate carries a pre-declared protocol for the largest change it will face.**
    A gate written only for incremental change must not be amended under the pressure of a
    live diff — the exceptional-event variant (e.g. architecture-scale adoption: aggregate
    criterion + explained diff + snapshot + ratification) is written and ratified before such
    a change is on the table.
23. **End-state principles need lawful transitions.** When a planned change must temporarily
    violate an end-state principle (e.g. #6, one path per concern, during a parallel build),
    the violation is declared, bounded, and pre-ratified with a retirement map — migration is
    a first-class state, never an undeclared exception.
24. **Every reported figure carries its uncertainty.** Sampling noise on the measurement
    corpus is quantified; a difference within the uncertainty is not a finding, and no
    decision rests on one. (The companion of #16: reproducibility bounds instrument error,
    this bounds sampling error.)

*Ledger corollary to #17 (ratified with #20–#24):* when a decision selects a **constrained
optimum** (a design chosen for methodology-compliance rather than raw measured performance),
the ledger records what the unconstrained best known alternative is and why it is excluded —
so a future reader can re-test whether the constraint still binds.

*Scope of surprise (ratified with #17–19):* surprises are **allowed in explorational runs**
whose purpose is to eliminate ignorance (#5 fact-finding); they are **NOT allowed when building
actual inference code** — there, a surprise is a STOP (#13) and evidence the Premise Gate was
not satisfied. The stage funnel: **desk-simulate (hours) → read-only probe (a session) → build
(an arc)** — each stage kills bad premises before the next pays for them.

*Fact-publication corollary to #6/#7/#12 (ratified by the user, 2026-07-10):* every derived
analytical fact is **published exactly once, on the producing layer's output surface;
consumers read, never re-derive.** A fact consumed by no one is either **declared dormancy**
(its future consumer named) or **waste** (removed). Evidence for why this needs stating:
`cowork_siloed_facts_audit.md` (17 findings) + `cowork_adjudication_dossier.md` Part B.
*Amendment (user, 2026-07-12, at the evidence-inventory discussion):* for EVIDENCE-class
facts (hints/clues a layer discovers that downstream inference could conceivably use —
the `cowork_evidence_inventory.md` catalog), **publish broadly even without a named
consumer** — the user's rationale: a visible smörgåsbord of evidence lets a future design
RECOGNIZE useful facts it would never have thought to request. Guardrails: each published
evidence fact carries its **establishment status** on the surface (established vs
unvalidated — a consumer may not put an unvalidated fact under load, #19); publication is
the in-memory surface (serialization stays selective); and the inventory + the
`ARCHITECTURE.md` layer specifications are kept in sync as facts are adopted (OI-146).

*Decision-neutrality of the existing implementation (corollary to #4/#6/#19; user-ratified
2026-07-26):* Designs are chosen from the principles and the ultimate objective — enabling the
best possible inference — alone. In that choice: **(a)** the value of reusing existing code, and
the cost of making existing code obsolete, are SECONDARY — they may break ties between designs
equal under the principles and the objective, and reuse counts only as carried-forward
establishment (#19), never as sunk cost or saved effort; **(b)** downstream implementation
impact — whether and how many consumers must change — carries NO weight; **(c)**
end-user-visible behavior change carries NO weight (the 2026-07-26 unshipped-scoping ruling),
while every behavior change remains ratification-gated (#14) and verification-gated (#15/#19)
exactly as before. The best-possible-inference design is chosen first; what exists then either
serves it or retires. (This does not weaken #6 — one path per concern is an END-STATE structural
principle, not a preservation claim for the existing path; nor #19 — establishment must still
exist before trust.)

*Provenance: principles 1–11 are the user's standing list; #12 (no information loss) and
#13–16 were ratified by the user on 2026-07-06; #17–19 (the Premise Gate + the Class-A/Class-B
prohibitions) and the surprise-scope rule were ratified by the user on 2026-07-10 — analysis
and evidence in `cowork_premise_gate_reflection.md`; #20–#24 (evaluation statistics, the
ground-truth ceiling, gate/transition governance) and the constrained-optimum ledger corollary
were ratified by the user on 2026-07-18 at the joint-estimator plan review — analysis in
`cowork_joint_estimator_architecture.md` §6/§7, operational rows OI-176…OI-181; the
decision-neutrality corollary was ratified by the user on 2026-07-26 at the notation-layer
adoption increment's decision surface — analysis in `cowork_notation_adoption_increment.md` §2. Companion standing rules elsewhere: the
⛔ TOTAL UNIFICATION rule (`cowork_handoff.md`), the MEASURE-BEFORE-BUILD gate
(`cowork_engage_arc_plan.md`, now the middle stage of the #17 funnel), and the doc-sync,
layer, and gate policies below.*

## The open-items register (user-directed, 2026-07-10; split into index + detail files, user-ratified 2026-07-26)

**The register is `OPEN_ITEMS.md` (the lean INDEX) + `open_items/OI-<n>.md` (one detail file per
item).** The INDEX `OPEN_ITEMS.md` is the ONE home for every discovered-but-unresolved issue and the
**authoritative status surface** (#6 applied to tracking itself — created after a full-repo sweep
found 91 open items scattered across 12 surfaces with 11 status contradictions; split into
index + per-item detail files on 2026-07-26, user-ratified option 1, when the single file grew too
large to render). Each item's full original row (text + source + status) lives verbatim in its
detail file `open_items/OI-<n>.md`, which carries narrative and provenance only and **never a status
of record**. Rules: (a) **read the INDEX `OPEN_ITEMS.md` at session start** (open detail files as
needed); (b) **a stage may not open while a register item gating it is open**; (c) every newly
discovered issue gets an **index row AND its detail file** **in the same commit** that records the
discovery; (d) every resolution **flips the INDEX row** with provenance (the detail file gains a
dated resolution note, never a status of its own); (e) tracking an owed/deferred/TODO item in
prose only, without a register row, is a doc-sync violation (#10). "Deal with everything
discovered" means: every item has ONE index row, an owning layer, and a blocking gate — fixed at its
#8-correct stage, never silently forgotten. (The byte-level split reconciliation instrument is
`tools/open_items_split_check.py` → `open_items/split_reconciliation.json`.)

## The decisions register (shape user-ratified 2026-07-28; content + living surface 2026-08-02)

**The register is `DECISIONS.md` (the lean INDEX) + `decisions/group_<X>.md` (full entries: the
verbatim decision, plain restatement, why, status, home, provenance).** It records WHAT WAS
DECIDED and its STATUS, nothing else — non-conformance is tracked in `OPEN_ITEMS.md` as ordinary
rows pointing back at the decision violated. Rules: (a) **read the INDEX `DECISIONS.md` at
session start** (open group files as needed); (b) a dispatch, design or report touching a
decision's subject CITES its register entry; (c) **a new ratification, shelving or falsification
gets its register entry (data + regenerated files) IN the commit that records it**; (d) the
register is a GENERATED surface — change `tools/audit/decisions/backbone_decisions.json` and
regenerate (`gen_decisions_register.py`; its `--check` and `gen_cluster_dispositions.py
--verify` guard drift, quote fidelity and reference resolution), never hand-edit the rendered
files; (e) a decision belongs, wherever possible, in the OWNING LAYER'S SPECIFICATION — the
register is the index and pointer, never a substitute home.

## Project context

This is MuseScore Studio. The active development area is the `composing` module
(`src/composing/`), which implements harmonic analysis. See
`C:\Users\vince\.claude\projects\c--s-MS\memory\project_chord_analyzer.md` for
full project context.

## Autonomous operation — composing module

When working on the `src/composing/` module you are **pre-authorized** to:

- Edit any file under `src/composing/` without asking for confirmation
- Edit `src/notation/internal/notationaccessibility.cpp` without asking
- Edit `ARCHITECTURE.md` (project root) without asking
- Run the build: `powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`
- Run the tests: `./composing_tests.exe` from `ninja_build_rel/`
- Read `src/composing/tests/chord_mismatch_report.txt` after each test run

**Standard loop for mismatch reduction work** — do all of the following without
stopping for confirmation:
1. Analyse the mismatch(es)
2. Implement the fix in `chordanalyzer.cpp`
3. Build
4. Run tests and read the mismatch report
5. Report results (mismatches before → after, any regressions)

Only stop and ask if:
- A regression is introduced (mismatch count goes up or a previously passing
  test fails)
- A change would touch files **outside** `src/composing/` and
  `notationaccessibility.cpp`
- The catalog XML (`chordanalyzer_catalog.musicxml`) needs to be modified
  (ground-truth changes require explicit approval)
- You are uncertain whether a fix is correct and want a second opinion

## Build and test commands

**Always read these three files at the start of every session:**
- `C:\s\MS\BUILD_AND_TEST.md` — authoritative commands for all build variants, both test suites, and all Python tools
- `C:\s\MS\STATUS.md` — lean since the 2026-07-18 doc split: the current entries, active iteration/next
  action, and pointers to the ratified baselines (gate block (A) below)
- `C:\s\MS\DECISIONS.md` — the decisions register's INDEX (see the register section above); rulings
  bind mechanically only if every session reads them

Do not rely on memory of previous sessions for baseline numbers or iteration state — read STATUS.md.
`STATUS_ARCHIVE.md` and `cowork_handoff_archive.md` hold the superseded historical entries moved out
by the doc split (`cc_instruction_doc_split.md`) — reference-only, NOT part of the session-start read.

```
# Build — use PowerShell Start-Process (cmd.exe //c fails in MSYS2/Git Bash)
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Run composing tests (must be in ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe

# Run notation tests — includes P1/P2/P3/P4 pipeline regression test
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check (always --preset Baroque unless iteration says otherwise)
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report written to:
src/composing/tests/chord_mismatch_report.txt
```

**Both test suites must pass after every code change.** The notation tests include
`pipeline_snapshot_tests` which pins P1/P2/P3/P4 output against golden JSON files.
If a change intentionally alters chord output (e.g. a new inversion gate fires),
the pipeline snapshot goldens need refreshing. Note: `pipeline_snapshot_tests.exe`
is a SEPARATE binary from `notation_tests.exe` — pass `--update-goldens` to it:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
```
Then re-run `./pipeline_snapshot_tests.exe` to confirm all pass.
Only run `--update-goldens` when the output change is verified correct.

## Gate threshold and preset policy

Gate thresholds (e.g. Gate I: 0.45, Gate K: 0.20, Gate L: 0.35) are **calibrated
against the Baroque corpus** and are intentionally Baroque-specific. Do NOT adjust
them to accommodate other musical styles.

### (A) THE ROBUST-UNIT REGRESSION STOP (ratified R10-b, 2026-07-06)

**★ The governing hard regression stop** is the **granularity-robust union-of-boundaries unit,
variant (b) DCML-only** (music21 is NOT ground truth), duration-weighted and
**segmentation-invariant**. **Root governs; RN and key are always tracked beside it.** This is the
granularity-robust metric mandated at Stage 5; it **supersedes the batch 52/24/52 case-identity stop**
(now historical — see block (C)). Ratified at **R10-b (2026-07-06)**; handover provenance
`cc_stage5_r10b_ratification_report.md` (assembly surface: `cc_stage5_r10_assembly_report.md`).

**Committed reference (the diff base): `tools/robust_stop/`** — per-preset `stem@runStartTick`
variant-(b) root-failing run enumerations (**4547 runs on every preset** since the OI-178 adoption
2026-07-26 — identical across presets because inference is preset-independent; was ≈6506 / 6688 / 6522
Baroque/Jazz/Default under the superseded OI-168 legacy-analysis reference), the
`summary.json` aggregates, and `manifest.json` (corpus `git_hash` + instrument provenance + the offsets-
file hash + per-preset summary block + reproduce-status). Generated by the pinned instrument
`tools/a8_rebaseline_measure.py`, which self-validates its variant-(b) duration decomposition byte-
identical to `compare_rn.grid_score_regions()` on all 326×3 covered pieces. The manifest is **derived,
never hand-typed** (#17f): `tools/robust_stop_restamp.py` regenerates every recorded figure from the
candidate `summary.json`, and is established by reproducing the outgoing manifest exactly. A frozen
snapshot of the superseded batch sets lives at `tools/robust_stop/batch_stop_frozen_history.json` (block (C)).

**★ Ratified baselines — RE-BASELINED AT THE OI-178 JOINT-ESTIMATOR ADOPTION, 2026-07-26 (user-ratified,
option 1; measurement provenance `d615152c51`; report `cc_adoption_measurement_report.md`, record
`tools/joint_estimator/adoption_record.json`).** The joint estimator is now the **PRODUCTION inference
layer on the batch/corpus surface**: `batch_analyze --joint-inference <dir>` produces each `.ours.json`
from the joint module's decode (the L1 fact adapter → the ratified §5 decoder at the committed all-326
tables + the direct-metric SELECTED weight vector, seg_cap 4, leftover 2a); `run_bach_preset.py
--joint-inference` regenerates the corpus through it. **Inference is PRESET-INDEPENDENT** (the ratified
mode decision — presets are presentation concerns; the three preset dirs are identical at the inference
fields, so every column below is ONE value, not three): **root-agree 77.03 %, RN-agree 64.12 %, key-agree
vs HOME/global 56.14 %, key-agree vs LOCAL 78.42 %** (variant b, at 326/352 coverage; the OI-143 dual key
column both tracked; **key-abstain 0** — A commits its MAP path, the OI-33 flag reads zero). **The
hard-stop class-(b) root-disagree duration is 1,817,280 ticks per preset** (−33.0 / −34.7 / −33.1 % vs the
superseded OI-168 reference's 2 714 000 / 2 783 680 / 2 718 080; `robust_stop_diff` OVERALL PASS, the
run-level set-diff large in both directions by design, every added class-(b) run enumerated/diagnosed —
the genuine-new fifth-substitution subset is OI-192, the accepted cost side of the net trade).

**STAGED SCOPE — CLOSED AT THE NOTATION SWITCH (user-ratified 2026-07-27).** The OI-178 adoption put the
joint estimator on the batch/committed surface only; **THE NOTATION SWITCH now puts it on the in-app
NOTATION surface too.** `useJointNotationRecord` defaults **ON**, so the in-app notation analysis — the
span-annotation emit, the implode chord-track, the tuning region path, and the note-seam (status-bar /
harmony-write / right-click-menu) — is produced by the joint estimator's A-native notation record (the
seams P0–P7 record path), NOT the legacy `analyzeHarmonicRhythm`/`analyzeChord` path. **The migration state
is now CLOSED on BOTH surfaces.** The legacy notation path remains **COMPILED and DORMANT** (selected only by
an explicit `useJointNotationRecord = false`), awaiting deletion at the **OI-180 retirement map, now fully
live**. The switch is ONE revertible commit: the pipeline-snapshot goldens were refreshed against the record
arm and every diff reconciled against the P6 classified evidence — **0 unexplained, 0 input-scoping, the
non-flag-gated surfaces byte-identical** (`tools/notation_seams/switch_golden_reconciliation.json`; the
inference/§3.3-presentation/inert-auxiliary split is the record arm's expected notation differences). **The
batch/corpus surface and `tools/robust_stop/` are UNMOVED** (the flag is notation-side; `test_batch_analyze_
regressions` passes, no `tools/corpus/` or `tools/robust_stop/` diff). Provenance: dispatch
`cc_instruction_notation_switch.md`; the P6 report `tools/notation_seams/dualarm_classified_report.json`; the
OI-178 adoption record `tools/joint_estimator/adoption_record.json`.

**Superseded columns preserved (#12):** the OI-168 LEGACY-ANALYSIS baselines (root 66.04 / 64.98 / 65.93,
RN 46.33 / 44.10 / 46.23, key-home 71.42 / 67.83 / 70.65, key-local 65.99 / 62.98 / 65.71) live in the
manifest's `reproduce_status.superseded_oi168` and the O-12 snapshot
`tools/robust_stop/snapshot_2026-07-26_pre_oi178_adoption/`. **The OI-168 narrative below is now HISTORICAL
(the superseded legacy-analysis reference), retained for provenance.**

*★ [SUPERSEDED by the OI-178 adoption 2026-07-26 — historical] THE OI-168 RE-BASELINE (2026-07-14; report `cc_oi168_fix_report.md`; outgoing reference preserved at
`tools/robust_stop/snapshot_2026-07-13_pre_oi168/`, O-12). **Every published column above is UNCHANGED at
the two decimals reported here** — what moved is the hard stop itself and the Jazz run count.
`analyzeChord`'s two key-consuming scoring terms (`dim7CharacteristicBonus`, `diatonicRootContribution`)
stopped testing membership in the mode-tonic-anchored set `{(keyTonicPc + scale[i]) mod 12}` and now test the
key SIGNATURE's own collection, `pcInMask(diatonicMaskFromFifths(fifths), pc)` — no tonic, no mode scale.
The two sets are provably identical for 19 of the 21 `KeySigMode` values and differ by a semitone
transposition for `Altered`/`AlteredDomBB7`. **Baroque and Default are BYTE-IDENTICAL** (352/352 `.ours.json`
each; every column and every run set unmoved — the δ=0 derivation verified at runtime, not on paper).
**Jazz: 9 `.ours.json` change and exactly ONE committed chord flips** — `bwv145.5@12960` (local key `D#alt`):
`Ebm` (root 3) → `B/Eb` (root 11), which is the DCML ground-truth root AND the music21 root (the sounding
D♯–F♯–B is a B-major triad; the old reading named a chord the notes do not contain). **The run-level set-diff
is REMOVAL-ONLY: one run, zero additions on any preset.** Class-(b) root-disagree duration **Jazz −480**
(2 784 160 → 2 783 680), Baroque/Default **+0**; class-(a) unmoved; the key columns unmoved (the key layer is
upstream of the corrected terms). Jazz variant-(b) runs 6689 → **6688**; Jazz root-agree 64.9772 → **64.9830 %**
(+0.0058 pp — below the reported precision, hence no column edit above). `robust_stop_diff.py`: **OVERALL
PASS** — the hard stop strictly DECREASES. No pipeline-snapshot golden was refreshed (the suite runs the
Default configuration, which is byte-identical). **Caveat carried forward (OI-170):** this fixed the two
SCORING terms, not the layer — `buildChordResult`'s `diatonicToKey` and the Gate I / Gate L
`invRootIsDiatonic` checks still answer a collection question through the tonic and still carry the same
defect. **L4 is NOT tonic-independent; no design may assume it is.**

*The KEY columns above supersede the OI-142/OI-143 column (key home 71.29/67.49/70.52, key local
65.72/62.49/65.39), preserved in `tools/robust_stop/snapshot_2026-07-13_pre_oi132_oi144/`. **Root and RN did
NOT move** (the mode reduction touches only the key axis): every root-failing run set is byte-identical, the
class-(b) root-disagree duration is unchanged on all presets, and the run-level set-diff is (+0 / −0). What
changed: the five dominant-family exotic modes (Phrygian dominant, altered, Lydian dominant, Lydian augmented,
Mixolydian ♭6) now reduce to the MINOR key of their PARENT COLLECTION — an emitted "C♯PhrygDom" grades as F♯
minor, the key it is the dominant of — in the ONE shared reduction `compare_rn._our_key_tonic`, onto which the
second key parser (`oracle_root_metric`) was folded. Key-abstain also drops (7680/10800/33120 → 0/4080/2400
ticks). The user's ruling and the evidence: `cc_mode_grading_adjudication_probe_report.md` (the parent-collection
reading matches the DCML annotators on 67 % of the affected duration on the local column; the tonic-triad
reading on 0 %). Provenance: `cc_key_grading_and_calibration_rebaseline_report.md`.*

*Earlier columns, for the record: the OI-142/OI-143 re-baseline (user-ratified 2026-07-12) applied the 12
transposed editions' constant offsets to the WiR ground truth at the shared substrate
`dcml_parser.load_wir_regions` (OI-142) and split the key column into home/local (OI-143); its run-level
set-diff was confined to the 12 corrected stems and the class-(b) root-disagree duration DECREASED on all
presets (`cc_key_grading_rebaseline_report.md`; offsets in `tools/robust_stop/corpus_transposition_offsets.json`).
It in turn superseded the R10-b column (root 63.36/62.37/63.25, RN 44.58/42.40/44.41, key 68.13/64.43/67.50),
preserved in `tools/robust_stop/snapshot_2026-07-12_pre_oi142_oi143/`.*

- **The hard stop (per preset):** the **class-(b) (pitch-class-decidable-root) root-disagree DURATION
  must be NON-INCREASING** vs the committed reference — the *meaningful* functional errors never grow.
  Any preset increasing ⟹ FAIL. Run (≈6 s total):
  ```
  python tools/a8_rebaseline_measure.py --out-dir <cand> [--corpus-root <scratch>]   # self-validates grid==oracle per piece
  python tools/robust_stop_diff.py --candidate <cand>                                # exit 0 iff every preset passes
  ```
- **The mandatory explained diff:** every run lists the **run-level set-diff** vs the reference
  (added/removed `stem@runStartTick` runs, each tagged with its two-tier class). Zero-new-case cannot
  scale to ~7k runs, so the gate is a **duration non-increase + an explained per-run diff**, NOT a
  set-identity.
- **Class-(a) duration is TRACKED** (a large net increase trips the `robust_stop_diff.py` INVESTIGATE
  flag — advisory threshold `CLASS_A_INVESTIGATE_TICKS = 9600`, the guardrail-(3) "many symmetric
  sonorities destabilized" carry-over), never an automatic stop; class-(b) is the hard stop above. On
  this unit class-(b) is **~96.5 %** of root-fail time (vs ≈53 % class-(a) on the old batch residual) —
  the robust stop is governed by the meaningful count.
- **Re-baseline discipline for future adoptions (the 2.2e pattern, generalized):** an adoption that
  changes a fitted value **re-baselines the `tools/robust_stop/` reference artifacts** in the adoption
  commit — the run-level set-diff (removals/additions, each with class) **explained per case and
  ratified**, the class-(b) duration non-increase **proven per preset**, the manifest re-stamped with
  the new corpus `git_hash`, and the **outgoing reference snapshotted first (O-12)**.

**★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; `cc_a8_rebaseline_measure_report.md`).** The
**primary reported metric AND the Stage-5 fitting-objective basis** is the robust unit above: root
governs, RN + key(home,local) tracked beside. **★ Ratified baselines — RE-BASELINED AT THE OI-178
JOINT-ESTIMATOR ADOPTION, 2026-07-26 (user-ratified, option 1; the joint estimator IS the production
inference layer on the batch/corpus surface, PRESET-INDEPENDENT — full detail in block (A) above):
root-agree 77.03 %, RN-agree 64.12 %, key-agree vs HOME/global 56.14 %, key-agree vs LOCAL 78.42 %**
(one value per column, all three presets; class-(b) hard-stop duration 1,817,280 per preset;
`robust_stop_diff` OVERALL PASS; measurement provenance `d615152c51`, `cc_adoption_measurement_report.md`).
**The recitation that follows is HISTORICAL — the superseded OI-168/OI-132 legacy-analysis lineage,
retained for provenance.** *The superseded OI-168 columns (variant b, 326/352 coverage; re-baselined at
the signature-mask fix, 2026-07-14, `cc_oi168_fix_report.md`; the movement then was Jazz root-agree
+0.0058 pp, the Jazz run count 6689→6688 and class-(b) −480 vs the OI-132 mode-grading consolidation,
user-ratified 2026-07-13, `cc_key_grading_and_calibration_rebaseline_report.md`): **root-agree Baroque
66.04 % / Jazz 64.98 % / Default 65.93 %**, RN-agree 46.33/44.10/46.23 %, **key-agree vs HOME/global
71.42/67.83/70.65 %** + **vs LOCAL 65.99/62.98/65.71 %** (the OI-143 dual column, both tracked). That consolidation reduces the five
dominant-family exotic modes to their PARENT COLLECTION's minor key in the one shared reduction
`compare_rn._our_key_tonic`; it moved the KEY columns only — root, RN, every root-failing run set and the
class-(b) hard-stop duration are byte-identical (run-diff +0/−0 on all presets). The key columns it superseded
(home 71.29/67.49/70.52, local 65.72/62.49/65.39) came from the OI-142/OI-143 re-baseline (user-ratified
2026-07-12, `cc_key_grading_rebaseline_report.md`), which applied the 12 transposed editions' offsets to the
WiR ground truth at `dcml_parser.load_wir_regions` (OI-142) and split the key column (OI-143); its run-diff was
confined to the 12 corrected stems (the other 314 byte-identical) and class-(b) root-disagree duration
DECREASED on all presets. *The superseded R10-b column (root
63.36/62.37/63.25, RN 44.58/42.40/44.41, key 68.13/64.43/67.50), preserved in
`tools/robust_stop/snapshot_2026-07-12_pre_oi142_oi143/`, was itself re-baselined at the 2.2e kWStepIn
adoption, 2026-07-05; its key-column establishment history: Jazz is byte-identical to the pre-adoption
corpus — proven by an explicit-override
reconstruction — so its root/RN reproduce the prior 62.37/42.40 exactly, and by that **same
byte-identity its key reproduces the prior 64.43 exactly** (measured 64.4321): identical `.ours.json` +
WiR + git-unchanged key-path code cannot move the figure. The earlier-recorded 2.2e key column
**68.19/64.52/67.77 was a non-reproducible measurement-entry error**, corrected at R10-b (2026-07-06) to
the reproducible **68.13/64.43/67.50**; Baroque shows a tiny +0.015 pp shift vs the prior 68.11 from the
kWStepIn re-segmentation, Jazz/Default reproduce the prior 64.43/67.50 to the digit. Prior baselines:
63.32/62.37/63.22, RN 44.56/42.40/44.40, key 68.11/64.43/67.50.)* When it governs, the **hard stop is
the class-(b) root-disagree DURATION non-increase per preset** + the **mandatory explained per-run
set-diff** (zero-new-case cannot scale to ~7,000 runs; class-(b) dominates ~96.5 % at this unit). C1
reliability curves on this unit: `cc_c1_reliability_report.md`.

### (B) The two-tier per-cell class policy — CARRIED OVER, LIVE

**This policy is UNCHANGED at R10-b and now governs the robust unit's per-cell classification** (the
class-(a)/(b) split on the robust unit's failing runs, and the block-(A) class-(b) duration hard stop).
It was authored against the batch BIR=false gate (block (C)); every guardrail, definition, and founding
case below carries over verbatim to the robust unit. (The "BIR=false case" phrasing below is the batch
framing under which it was ratified; on the robust unit the same classification applies per failing
run/cell.)

**Two-tier refinement (user-ratified 2026-06-22) — class-(b) functional regression vs class-(a)
symmetric-rotation churn.** A *new* BIR=false case is one of two classes:
- **Class (b) — functional/key regression: UNCHANGED HARD STOP.** A new BIR=false case at a sonority
  whose root is *pitch-class-decidable* (any non-symmetric chord — triads, dominant sevenths, etc.)
  where the analysis now gets the root or key wrong. **Zero** new class-(b) cases on any preset, ever.
  This is the gate's real intent and does not move.
- **Class (a) — symmetric-rotation churn: TRACKED, CONDITIONAL (not an automatic hard stop).** A new
  BIR=false case at a sonority whose root is *pitch-class-undecidable by construction* — symmetric
  diminished-seventh, augmented, whole-tone, or a share-tone tetrad (half-dim↔m6; dim7-subset-of-V7♭9;
  Maj7↔relative-minor triad). The pitch-class analyzer is spelling-blind and cannot pick the
  spelling-correct rotation; no rotation is more correct by pitch class. Acceptable **only when ALL** of:
  (1) **verified at the score per case** against the actual notes (e.g. the music21 GT region) —
  assertion is not enough; (2) **default to class (b) on any doubt** — if not *proven* class-(a), it
  IS class-(b); (3) **the class-(b) (pitch-class-decidable-root) BIR=false count is non-increasing** on every preset —
  the *meaningful* errors never grow; the class-(a) total may wobble by a **small, every-case-verified**
  amount (the rotation count is a coin-flip, not a quality measure), but a **large class-(a) net
  increase trips mandatory investigation** (a change destabilizing many symmetric sonorities is a
  signal even when each case is individually class-(a)); (4) **case identities recorded** (stem@tick +
  sonority); (5) **interim only** — a
  bridge pending the Stage-5/6 spelling-aware (two-tier) gate, which retires this exception. Applies
  **only** to the symmetric/share-tone structural class; no other source of a new BIR=false case
  qualifies. Root cause: the rotation churn is a **chord-layer (Layer-4) root ambiguity** *surfaced,
  not caused,* by a key change; the proper fix is spelling/voice-leading-aware chord-root selection
  (Layer 4 / Stage 5–6). Founding evidence (Cowork-verified at the score, music21 GT, 2026-06-22):
  `bwv272@4320` (G♯dim7), `bwv289@20160` (A♯dim7), `bwv291@17760` (Eø7↔Gm6), `bwv387@10560`
  (G♯dim7/E7♭9) — all symmetric/share-tone, zero functional regressions; the Layer-3 decoder-wiring
  increment. Full provenance: `cowork_gate_policy_amendment.md`.
- **First accepted class-(a) interim case (Layer-3 wiring, 2026-06-22):** Baroque/Default net **−4** (all new
  cases class-(a)); **Jazz net +1** — accepted under guardrail (3): new `bwv272@4320` (G♯dim7 coin-flip) +
  `bwv291@17760` (Eø7↔Gm6 same-collection center), `bwv244.15@10080` fixed; both new verified class-(a) at the
  score, zero new class-(b), and the L3 reduction-rule lever measured byte-identically inert (a≡b on all presets) —
  so the +1 is irreducible at Layer 3. **Retires when Layer 4 (function/cadence) pins the rotation/center** —
  rotation-pinning is a named early Layer-4 job. Investigation: `cc_layer3_jazz_churn_investigation.md`.

### (C) RETROSPECTIVE — the batch 52/24/52 stop (superseded at R10-b, 2026-07-06 — historical reference)

> The `52/24/52` `stem@tick` case-identity sets below and their full L3-wiring / 2.2e / corrected-parser
> history were **THE hard regression stop through Stages 2–5**. They are **superseded** by the robust-unit
> stop (block (A)) at R10-b and are preserved here as historical reference only. Machine-readable snapshot:
> `tools/robust_stop/batch_stop_frozen_history.json`. Full handover provenance:
> `cc_stage5_r10b_ratification_report.md` (+ assembly `cc_stage5_r10_assembly_report.md`). **Why it was
> replaced:** the batch (cross-barline) region gate under-counted the true per-onset root error **~15–56×**
> — it measured a small music21-filtered reachable corner (class-(a) was ≈53 % of that residual vs ~3.5 % on
> the robust unit) — so the robust-unit stop replaced it at R10-b.

**The batch stop's diagnostic form — KEPT (no longer the stop).** `characterise_bir_false.py` remains a
runnable per-region diagnostic (useful for triage and for cross-checking the robust unit); it is no longer
the regression gate. Its corpus-integrity mechanism is **shared by the robust stop** — the block-(A) a8
instrument imports `characterise_bir_false.validate_corpus_dir`, so this guard cannot bit-rot into
uselessness. Since Stage 2.2a (M3 fix) each preset writes to its **own** dir under `tools/corpus/` and stamps
a `corpus_manifest.json`; `run_bach_preset.py` clean-slates the dir at the start of a regen and **exits
nonzero** unless the corpus is complete (**352/352** at current HEAD — the expected count is derived from the
source `.xml` files, not hard-coded); `characterise_bir_false.py` **refuses** to measure a dir whose manifest
is missing, incomplete, or whose `.ours.json` fingerprints do not match (preset contamination — the old
shared-`tools/corpus` failure mode). Re-run the batch diagnostic with:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz
```

**Re-baselined 2026-06-13 (corrected GT parser).** The prior **13/7/14** gate was an
**undercount**: GT-parser bugs (applied-chord `/X` rooting + minor-key
leading-tone/submediant rooting, fixed in `tools/dcml_parser.py`) corrupted the WiR roots
of applied and `viio`/`vio` chords, pushing genuine candidate cases into the discarded
`all_differ` bucket. With the roots now oracle-correct (music21 `RomanNumeral`, **100% on
all gate cases**), those cases surface. The new gate is a **strict superset** of the old
(every old case preserved, **0 lost** — verified through the canonical tool with an A/B
parser revert). **~95% of the added mass is legitimate ambiguity** — chiefly **symmetric
fully-diminished-7th** sonorities (root pitch-class-undefined by construction; ≈53% of
Baroque) and **viio↔V7 share-tone** readings; the genuinely-new *actionable* error count
is only ~1–3 per preset (net ≈9–10 Baroque / ~4 Jazz). The symmetric-dim7 members are
structurally unresolvable by pitch class and are the seed of a future **two-tier /
spelling-aware** gate (Stage 5/6 — noted, not built). Full provenance:
`cc_metric_rebaseline_report.md` + `cc_gate_rebaseline_verify_report.md`.

**★ (Historical — the batch stop's FINAL frozen state before R10-b) `52 / 24 / 52` (re-baselined at the
ratified 2.2e kWStepIn adoption, 2026-07-05, commit `c50002fee1` + the corpus chore below; frozen as history
at R10-b, 2026-07-06 — machine-readable at `tools/robust_stop/batch_stop_frozen_history.json`).** The 2.2e
delta vs the prior `53 / 24 / 53`: **removal-only
`{bwv244.32@5760}`** on Baroque + Default (the class-(b) case the kWStepIn 0.10→0.125 adoption fixed); Jazz
unchanged (byte-identical). The identity sets below are the 52/24/52 form; the history that produced the
prior 53/24/53 is preserved in the following paragraph.

**★ (History) Corrected to the ratified post-L3-wiring state `53 / 24 / 53` (Stage-0 measurement, commit `b57dbfa7a8`,
2026-06-25).** The `57/23/57` sets previously listed here predated the **already-ratified L3-wiring delta**
(`−4 / +1 / −4`) — the two-tier-gate prose above describes that delta, but these integer tables were never updated.
They are now. The delta, verified by diffing the measured sets against the prior `57/23/57` sets: **Baroque**
`− {bwv102.7@17520, bwv122.6@6720, bwv227.7@18120, bwv301@960, bwv336@8640, bwv381@4800}` (six fixed)
`+ {bwv272@4320, bwv289@20160}` (two class-(a) symmetric dim7) = net **−4**; **Jazz** `− {bwv244.15@10080}`
`+ {bwv272@4320, bwv291@17760}` = net **+1**. (Baroque and Jazz deltas Cowork-verified against the prior sets;
Default measured at `53`.) The **case-identity set, not the integer, is the gate** — re-measure with
`characterise_bir_false.py` after any change.

- **Baroque = 52** with identities (stem@tick):
  `{bwv10.7@36000, bwv14.5@8160, bwv144.6@15360, bwv144.6@16320, bwv151.5@13440, bwv153.1@18240, bwv16.6@16800,
  bwv169.7@24960, bwv17.7@46080, bwv174.5@6240, bwv20.11@13440, bwv244.46@960, bwv245.15@13920,
  bwv245.17@4800, bwv245.37@13920, bwv245.3@12480, bwv245.40@51360, bwv258@10560, bwv261@33840, bwv269@20640,
  bwv272@4320, bwv272@4800, bwv272@8160, bwv282@9120, bwv289@20160, bwv289@21600, bwv300@13440, bwv309@8640,
  bwv320@31680, bwv334@5280, bwv334@6720, bwv342@25440, bwv352@1440, bwv358@6000, bwv364@2880, bwv392@14400,
  bwv40.3@2400, bwv402@22080, bwv416@10080, bwv421@2880, bwv422@23040, bwv423@28320, bwv429@24240, bwv432@5520,
  bwv45.7@20160, bwv48.3@2880, bwv57.8@15360, bwv60.5@30960, bwv64.8@5280, bwv77.6@22080, bwv94.8@24960,
  bwv96.6@13440}` (= prior Baroque-53 − `{bwv244.32@5760}`, the class-(b) case the 2.2e kWStepIn adoption fixed;
  `characterise_bir_false.py --corpus-dir tools/corpus/baroque`, re-baselined at the ratified 2.2e adoption, removal-only).
- **Jazz = 24** with identities (stem@tick):
  `{bwv144.6@15360, bwv144.6@16320, bwv245.15@13920, bwv245.17@4800, bwv245.37@13920, bwv245.40@51360, bwv272@4320,
  bwv272@8160, bwv280@17280, bwv282@9120, bwv291@17760, bwv301@1440, bwv313@14880, bwv334@5280, bwv342@25440,
  bwv392@14400, bwv422@23040, bwv429@24240, bwv432@5520, bwv45.7@20160, bwv48.3@2880, bwv64.8@5280, bwv74.8@13440,
  bwv74.8@13920}` (= prior Jazz-23 − {bwv244.15@10080} + {bwv272@4320, bwv291@17760}).
- **Default (the user-run config) = 52.** Per the `characterise_bir_false.py --corpus-dir tools/corpus/default`
  measurement, Default = Baroque-52 with `{bwv352@1440, bwv60.5@30960}` replaced by `{bwv227.7@18000, bwv387@10560}`
  (the rest identical to Baroque-52). Re-baselined at the ratified 2.2e adoption: removal-only `{bwv244.32@5760}`
  vs the prior Default-53 (the same class-(b) case the kWStepIn adoption fixed on Baroque). *(✅ RE-CONFIRMED by measurement at the 2026-07-03 grammar-completion regen
  (`cc_grammar_completion_report.md`, commit `ce509b0961`): all three presets' case-identity sets matched this
  document exactly, set-diff empty both directions — the earlier Stage-0 prose-inconsistency caveat is discharged and
  the Default identities above may be relied on.)*

### (D) Caveats

**Cross-layer-budget caveat (2026-06-24, O1 measurement) — LIVE (an interpretation caveat, not a granularity
one; it applies equally to the robust unit).** the BIR=false set is **not** the Layer-5 resolver
residual — it is a **work budget distributed across Layers 1–5**, and it overstates the function-only remainder
several-fold. Measured during the O1 investigation (`cowork_uncertain_resolver_investigation.md` +
`cc_uncertain_resolver_measurement_report.md`): ≈60% Baroque / ≈42% Jazz are **spelling-resolvable** (the Layer-4
notated-spelling root pin), and most of the rest is **bass/inversion**, **local voice-leading**, or plain
**segmentation over-grab** the change-point slicer (Layer 2) removes by construction (e.g. `bwv10.7@36000` — a 5-note
scale `C-D-E♭-F-G` over-grabbed across two GT chords `i43`/`iv532`, Cowork-verified at the score). The genuinely
**function-only** remainder reaching Architectural Layer 5 is small: pitch-class-identical share-tone chords
(`bwv352` Am6↔F♯ø7; Jazz `bwv291` Eø7↔Gm6) on the chord side, and the **note-identical** key-disagreement class
(relative major/minor, tonicization-vs-modulation) on the key side. So a BIR=false count is read as cross-layer work,
not as any one layer's accuracy. (O1 resolved: the resolver of "uncertain" is Layer 5 itself, no separate box.)

**Granularity caveat (Stage 2.2-i) — ✅ RESOLVED at R10-b (2026-07-06).** The mandate this caveat raised — "a
granularity-robust metric is mandatory at Stage 5" — is **delivered**: the block-(A) robust-unit stop is the
granularity-robust (segmentation-invariant, duration-weighted, union-of-boundaries) metric, and it now governs
as the hard stop. *(Historical statement of the resolved problem, kept for provenance:)* the former batch
`53/24`→`52/24/52` gate was measured at **batch (cross-barline) region** granularity; the user-visible
**per-beat** root-error rate is ~7× higher when the same scores are scored at measure-aligned (section)
granularity — the block-(A) unit closes that gap. Inspect the per-beat view with `batch_analyze
--section-level` (diagnostic flag, default OFF). See `cc_stage2_2_ab_dossier.md` for the A/B that quantified
the granularity gap.

(`tools/analyze_inversion_errors.py` is a *separate* secondary metric: its three-way
`music21_dcml_agree` genuine split is `bassIsRoot` true/false. **Re-measured under the
corrected parser** (`cc_functional_residual_dossier.md`, 2026-06-14): **Baroque 24/13→47/57,
Jazz 35/7→81/23** — the `bassIsRoot`=false halves (**57 / 23**) independently match the
re-baselined gate. `characterise_bir_false.py` reproduces that BIR=false half (57/23, Default 57).
Since Stage 2.2-ii (Rider 1) it takes `--corpus-dir` and reads BOTH `.ours.json` and
`.music21.json` from the validated per-preset dir — `--ours-dir` is a deprecated,
unvalidated alias.)

If a gate causes BIR=false regressions in a non-Baroque preset, the correct fix is:
1. A tighter **structural entry condition** that excludes the problematic chord type
   regardless of preset (preferred — e.g. an extension guard blocks augmented+seventh
   chords in all styles), OR
2. A **preset-specific threshold override** that leaves the Baroque-tuned value unchanged.

Never widen a Baroque-tuned threshold to cover a non-Baroque edge case.

**Preset scoring caps — corrected 2026-06-10:** `maxTotalInversionContextBonus` is
**never set on any code path** — both presets inherit the 2.0 default, and the cap is
currently non-binding (the four inversion bonuses sum to 1.85 Baroque/default, 0.75
Jazz). The formerly documented "Baroque=2.5 / Jazz=0.6" values were aspirational and
never implemented. Jazz's inversion behavior comes from its **reduced individual
inversion bonuses** (0.20/0.20/0.15/0.20 in `batch_analyze.cpp`), not the cap. Full
story in `docs/scoring_model.md` §4 (note below the "Other terms" table).

## Scoring model — `docs/scoring_model.md` (MANDATORY for scoring sessions)

**Read `docs/scoring_model.md` at the start of any session that touches scoring
logic in `chordanalyzer.cpp`** — this includes adding or modifying templates,
bonuses, guards, gates, score matrices, or post-scoring passes.

The document is the authoritative reference for how the scoring pipeline works,
why each term exists, and what invariants must not be broken. Violating these
invariants without reading the doc first has caused multiple failed attempts
(B1 leading-tone ambiguity, B2 ×4, B3 rotation-selector bypass).

**Sync rule — mandatory:** Any commit that adds or modifies a template, bonus,
guard, gate, or other scoring term in `chordanalyzer.cpp` **must** include a
corresponding update to `docs/scoring_model.md` in the same commit. The two
must never drift apart. Specifically:

- Adding a template: update the Templates section (§2), increment the template
  count in the array-size comment, add the guard description if applicable
- Adding or changing a bonus/gate: update the relevant §4 or §6 entry
- Adding a new constraint or dead end: add it to §8

**Staleness check:** The template count in `docs/scoring_model.md` §2 must
always match the `array<TemplateDef, N>` declaration in `chordanalyzer.cpp`.
If they differ, the doc is stale — update it before proceeding.

**Template additions — the `kTemplateCount` model (since `a236a0ff21`):** All
template-related array extents (the `analyzeChord` template array, the three score
matrices, `kMasks` in `harmonicfunctionlayer.cpp`) are derived from
`analysis::kTemplateCount` in `chordanalyzer.h`, so the compiler enforces size
consistency — the old silent stack-buffer-overrun failure mode (a missed matrix
resize, caught in the B1 attempt 2026-06-04) is closed. (Since Stage 2.3
`18dc9e1829` the duplicate `kDiagTemplates` array is gone — `diagnoseChord` replays
the production pipeline, so there is **one** template array, not two.) Adding a
template means:
1. Bump `analysis::kTemplateCount` N→N+1 (auto-resizes the matrices and `kMasks`)
2. Add the new `TemplateDef` entry in `analyzeChord`
3. Add the interval bitmask to `kMasks` (a zero mask silently disables Gate R)

Remaining trap: bumping the constant **without** adding the `TemplateDef` entry
value-initializes a trailing all-zero template (silent) — always do both in the
same edit. The authoritative checklist is `docs/scoring_model.md` §9.

## Score corpora

For any task involving scores (validation, snapshot tests, manual QA,
LLM-triage, qualitative review), read `docs/score_inventory.md` first. It
maps every score location to its intended use and lists the do-not-touch
files. Companion references: `tools/REPRODUCIBILITY.md` (how to recreate
corpora) and the JSON registries (`tools/corpus_registry.json`,
`tools/extra_scores_registry.json`).

## Local patches — do not revert

The following changes have been made intentionally to fix bugs unrelated to the
composing module. Do **not** revert them, and do not let build scripts or
dependency updates overwrite them without explicit approval.

### Windows Snap fix — `muse` submodule (applied 2026-05-14)

**File:** `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`  
**Function:** `calculateWindowSize()`

Two lines were removed that set `ptMinTrackSize` equal to the full monitor work
area inside the `WM_GETMINMAXINFO` handler. This told Windows the minimum
allowed window size was the entire screen, which prevented Windows Snap from
resizing a maximised MuseScore window into a chosen snap zone (the window
stayed full-screen and lost its title-bar controls).

The fix: `ptMaxSize` and `ptMaxPosition` are kept (they correctly constrain the
maximised position); `ptMinTrackSize` is intentionally left unset.

Upstream issue: musescore/MuseScore#25823 (related cousins: #21344, #16794).  
Introduced by upstream commit `4ad218709` (5 Aug 2025).  
**Do not restore the `ptMinTrackSize` lines.**

### MusicXML declared-mode import fix (Stage 4a, applied 2026-06-14)

**File:** `src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp`  
**Function:** `addKey()` (the `KeySig`-dedup guard, ~line 5976)

The dedup guarded the `KeySig` creation on **fifths only**:
`if (oldkey != key.key() || key.custom() || key.isAtonal())`. At score start the
prevailing key defaults to `{C, KeyMode::UNKNOWN}` (`KeyList::key()` →
`setConcertKey(Key::C)`), so a **0-fifths** key signature carrying an explicit
`<mode>` (e.g. `<fifths>0</fifths><mode>minor</mode>`) matched the prevailing fifths,
the whole `KeySig` was dropped, and the declared `<mode>` went with it →
`KeyMode::UNKNOWN` downstream. Export *does* write `<mode>`
(`exportmusicxml.cpp:2473`), so this broke export/import round-trip of `<mode>` and,
in our pipeline, dropped the declared-mode anchor on ~79 zero-signature Bach stems
(`cc_key_emission_headroom_dossier.md` — `declaredModeOrdinal=-1`). The maintainers'
own `// TODO only if different custom key ?` flags the dedup as known-incomplete.

The fix: fetch the prevailing `KeySigEvent` (not just the `Key` fifths) and add an
`oldKeySig.mode() != key.mode()` term to the guard, so a mode-bearing key at matching
fifths is retained. A key matching the prevailing one in **both** fifths and mode (and
not custom/atonal) still produces **no** `KeySig`, so plain mode-less C-major scores are
unaffected. Verified isolated to empty-signature scores (exactly 79 zero-sig `.ours.json`
changed, 0 non-empty-signature stems); BIR gate byte-identical on all three presets
(Baroque 57 / Jazz 23 / Default 57); key-inference S2 −378 (Default). Round-trip of
`bwv254` (0-fifths `<mode>minor</mode>`) now preserves `<mode>`.

Upstream issue: musescore/MuseScore#9444. The buggy fifths-only dedup is upstream-unchanged
code (the `// TODO only if different custom key ?` line). Stage-4a discrete step; the
graded-prior / KeyArea work that softens the resolver's −7 declared-mode wall is a later
Stage-4 step (see `cc_stage4a_mode_import_report.md`).
**Do not revert; do not let dependency updates overwrite without approval.**

**★ DISTRIBUTION CONSTRAINT (user, 2026-06-15): FORK-LOCAL ONLY — NEVER merge upstream / to the
MuseScore community.** This patch (`cfc7eb5e39`) is fine to have in the **central repo = the user's
fork** (`origin` = `slimvince/MuseScore`) and may be pushed there, but it must **NEVER** be pushed or
merged to `upstream` (`musescore/MuseScore`) or otherwise contributed to the MuseScore community.
`upstream` push is disabled in this repo; keep it so. Any future push/PR/merge that would carry
`cfc7eb5e39` (or its content) toward `musescore/MuseScore` is a HARD STOP — surface, do not proceed.
(The #9444 reference above is the upstream *bug report*; it does NOT authorize contributing THIS patch.)

## VS Code extension — bash command rules (MANDATORY, every session)

The Claude Code VS Code extension (v2.1.141+) has a 15-second stall detector. If the
API stream is silent for >15 seconds — which happens any time a bash command is running
— the extension marks the session `idle` and hands control back to the user, even though
CC is still running. This causes silent disconnects that are hard to detect.

**Two rules that apply to every bash command, no exceptions:**

**Rule 1 — Always append `; echo "exit:$?"` to any command that may return non-zero.**
A non-zero exit code also triggers an immediate idle transition. The echo always returns 0.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Rule 2 — Never let a single bash call produce large output.**
Large output (thousands of lines) takes >15 seconds to process and triggers the stall
detector. Redirect to a file and read separately.
- BAD:  `./pipeline_snapshot_tests.exe`  (many failing tests = large output)
- GOOD: `./pipeline_snapshot_tests.exe > /tmp/snap_out.txt 2>&1; echo "exit:$?"`
         then `head -50 /tmp/snap_out.txt`
- BAD:  `batch_analyze <score> --dump-regions notation`
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

Build commands via `Start-Process` are isolated from these rules (exit code not exposed).

## Conventions

- American English throughout — "analyzer" not "analyser"
- No confirmation prompts between analyse → implement → build → test steps
- Commit only when explicitly asked
- never hallucinate or guess, verified facts only - better ask first if unsure.
- **NEVER WORK FROM MEMORY INSTEAD OF DOCUMENTED FACTS (user-directed, 2026-07-28; binds Cowork
  and CC equally).** No assertion, design, decision, dispatch or report may rest on recalled or
  inferred content when a documented source exists. Open the primary source and cite it
  (file:line). This is STRONGER than the no-guessing rule above and is not satisfied by being
  right: correct memory is indistinguishable from incorrect memory without checking, so "I was
  probably right" is not a defence — and the check is what surfaces the parts the memory did not
  contain. **Where the primary source is:** how a layer *should* work → **that layer's section in
  `ARCHITECTURE.md`** (the primary place such decisions are recorded — not exclusively, but
  first); a ruling → the ratified `cowork_*` decision document and its dated amendments (and, once
  it exists, the decisions register, OI-208); current state and baselines → `STATUS.md` and
  `CLAUDE.md` gate block (A); an open issue → the `OPEN_ITEMS.md` INDEX and its detail file;
  what the code does → the code. **Founding instance:** on 2026-07-28 Cowork reasoned about note
  collection from `ARCHITECTURE.md` §2.15 and the factorization document without opening the
  Layer-2 specification, and reported the position as ambiguous; the specification states it
  explicitly and twice (`ARCHITECTURE.md:1045-1053`, slice identity IS the eligible sounding-note
  set with releases as boundaries; `:3134-3141`, actual sounding notes ranked the STRONGEST
  evidence), which turned an "ambiguous spec, narrowed in implementation" reading into a
  documented decision the implementation contradicts. The primary source was more specific than
  the memory of it, which is the general case, not the exception.
- **No self-invented labels, abbreviations, numbering schemes, or jargon** — in documents,
  register rows, commit messages, and conversation alike. Use the name a thing already has
  in the repository; if it has none, describe it in plain words. (User-directed, repeatedly;
  recorded 2026-07-11.)
- **THE WRITING STANDARDS LIVE IN `cowork_design_doc_template.md` — read it before writing any
  specification, design document, decision surface, or anything presented to the user.** Two
  standards: **predicates must be qualified** (user, 2026-06-24 — every two-place word names its
  argument; the mechanical check is to force the word to be followed by the thing it points at,
  and a phrase the prose cannot supply is a hole), and **defined terms, plain vocabulary, no
  shorthand** (user, 2026-07-02 — a terms table with nothing used before its row; no invented
  synonyms; no insider compression, a jargon handle only after its rule has been stated; inherited
  prose audited as hard as new). That file also carries the fourteen-section document structure,
  the status-banner convention, and the implementation/test locator rule. It is the ONE home for
  writing standards; the entry below sharpens its rule 5 and does not replace it (#6).
- **MUSIC-THEORY WORDS ARE RESERVED FOR THEIR MUSIC-THEORY MEANING (user-directed, 2026-07-28;
  sharpens `cowork_design_doc_template.md` rule 5 of 2026-07-02, whose own examples were *key*,
  *bar* and *measure* — that rule said one declared sense per document; this makes the choice
  mechanical rather than per-document. Binds Cowork and CC equally.)** Any term that coincides even slightly with music theory is used
  ONLY in its musical sense. This is a music-analysis system: an ambiguous domain vocabulary makes
  every document harder to read and every specification easier to misapply. The generalization of
  the "instrument" case — that word means a violin, not a measurement script; say *measurement
  tool*, *check*, *script*, or *generator*. Where a collision already exists in the tree it is NOT
  renamed unilaterally: the pass is scoped and ratified as its own work item (some names carry
  correspondence to the published research the design is grounded in, #1/#2, so the rename is a
  decision surface, not a sweep). But **no NEW collision is introduced**, and **anything written
  for the user avoids the collided sense entirely.** Known collisions in current use, as the
  starting inventory: *instrument*, *score* (numerical vs musical), *key* (map key vs tonality),
  *measure* (to measure vs the bar), *stem* (filename stem vs note stem), *note* (annotation vs
  pitch event), *mode* (operating mode vs musical mode), *tie* (score tie-break vs notated tie),
  *dynamic* (dynamic programming vs dynamics), *register* (issue register vs pitch register),
  *beat* (to defeat vs the pulse), *scale* (to scale vs the collection), *figure* (a reported
  figure vs figuration), *interval* (confidence interval vs pitch interval), *resolution* (of
  detail vs of a dissonance), *sharpen* (to refine vs to raise a pitch), *flat* (a flat profile vs
  the accidental), *root* (root cause vs chord root), *part* (a portion vs a musical part), *rest*
  (the remainder vs the silence).
  **THE DISAMBIGUATION CONVENTION (user-directed, 2026-07-28) — one rule covering every case:
  THE BARE WORD ALWAYS CARRIES THE MUSICAL MEANING; EVERY NON-MUSICAL USE IS EXPLICITLY
  QUALIFIED.** Bare *score* is the music — the numerical sense is always *candidate score* /
  *content score* / *total score*, never bare. Bare *key* is tonality — the other is *map key* /
  *cache key* / *lookup key*. Bare *measure* (noun) is the bar — the gauging sense is
  *measurement* (the verb "to measure" is unambiguous and stays). Bare *note* is a pitch event —
  the other is a *remark* / *annotation* / *entry*. Bare *mode* is the musical mode — the other is
  *operating mode*. Bare *register* is pitch register — the other is *the open-items register*, in
  full. Bare *tie* is the notated tie — the other is *tie-break*, always compound. Bare *dynamics*
  is the musical marking — the other is *dynamic programming*, always in full. Likewise *stem*
  (note stem; the other is *file name* / *piece identifier*), *interval* (pitch; the other is
  *uncertainty range*), *figure* (figuration; the other is *number* / *value*), *resolution*
  (harmonic; the other is *level of detail*), *scale* (the collection; the other is *grows with*),
  *beat* (the pulse; never a verb for "outperformed"), *root* (chord root; the other is
  *underlying cause*), *rest* (the silence; the other is *remainder*), *part* (musical part; the
  other is *portion* / *component*), *flat* (the accidental; the other is *featureless*),
  *instrument* (a violin; the other is *measurement tool* / *check* / *script*). This makes the
  eventual cleanup a BOUNDED job rather than a rename: much of the tree already complies by
  accident (`totalScore`, `content score`, `segmentContentScore` are qualified already), so only
  the BARE uses in a non-musical sense need touching.

- **EVERY DESIGN DECISION CARRIES ITS DEFENSE AT ITS HOME (user-directed, 2026-08-01, at the
  decisions-register ratification review).** Wherever a design decision is recorded — the owning
  layer's specification in `ARCHITECTURE.md` first — the record states WHY the decision was made:
  the published research or algorithm adopted (#1/#2), the measurement that decided it, or the
  constraint that forced it. Every design decision must be defendable, and its defense documented
  where the decision lives. This generalizes `ARCHITECTURE.md` §17.2 (every non-obvious scoring
  weight or threshold must explain its musical reasoning) from scoring values to design decisions
  as a class. The decisions register (`DECISIONS.md`) points at the defense; where a decision's
  derivation is not in the record, the register says **"derivation not recorded"** — the gap is
  stated, never filled in retroactively from memory (a defense written after the fact without a
  source is invention, and the never-work-from-memory rule forbids it). Founding instances of the
  gap: the decode segment cap's value (4), the legacy 16-beats-back/8-forward window, the
  boundary-tick-belongs-to-the-segment-it-starts convention — each recorded with no derivation.

- **ISSUE-EXHAUSTION AND SPECIFICATION COMPLETION BEFORE ANY FIX DESIGN (user-directed,
  2026-08-02; sharpens #8, which forbade inference-problem coding before layer completion — this
  forbids fix DESIGN before knowledge completion).** Three phases, strictly ordered. **Phase 1 —
  the specifications are made COMPLETE and TRUE:** every recorded decision is written into its
  owning specification (the homing acts), with its defense, so that conformance is thereafter
  measured against the specifications themselves — the decisions register remains the status
  ledger (supersession, shelving, the same-commit rule), never the conformance reference; and the
  specification text is corrected wherever it states something false at HEAD (the doc-sync debt),
  because a specification cannot be the compliance standard while it misdescribes the code.
  **Phase 2 — issue-finding is EXHAUSTED with measured coverage:** the remaining audit partitions
  and the blind second pass with its seeded error rate, plus the enumerated discovery channels
  (populations, oracles, invariants, residual decomposition, concept gaps, requirement side),
  each search reporting its detection power, ending in the bounded trust statement — every
  channel enumerated, every miss rate measured, every finding rowed. **Phase 3 — ONE prioritized
  fix plan over the complete list** — where each fix lives (its proper layer), what it groups
  with (its family), in what order, and what refits it forces — and only then does design begin.
  Rationale: #3/#5/#13 generalized from one defect family to the whole system, and the product is
  unshipped, so carrying known defects while knowledge completes costs no user anything.

## The self-check after every coding exercise (user-directed, 2026-07-11)

After EVERY coding exercise — code, scripts, instruments, and document edits alike —
and BEFORE reporting the work done: take a step back, re-read the actual diff of every
touched file, and check it against the guiding principles, the conventions, the gate and
threshold policies in this file, and the known problem types in `DEFECT_TYPES.md`. Any
violation found is surfaced immediately (its own `OPEN_ITEMS.md` row if it cannot be
corrected on the spot within the session's authorized scope), never silently shipped.
The check is of the work actually on disk, not of the intention — read the diff, not the
memory of writing it. This applies to CC sessions and Cowork sessions alike.
