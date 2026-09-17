# CC — Measurement-chain hardening (OI-145 wave 1) — report

**Dispatch:** `cc_instruction_measurement_chain_hardening.md` (Cowork, 2026-07-12) — the first arc of
the OI-145 key-layer readiness gate: harden the measurement chain (every future key-work probe/fit
is graded through it) BEFORE the key layer is built. A FIXING session on the `tools/` measurement
instruments — NOT inference coding; no `src/composing` analysis behavior changed.

**Governing outcome — NO GRADING DIGIT MOVED.** Every fix is to failure paths, validation,
duplication, and documentation. The establishment battery reproduced byte-for-byte after every
commit: a8 root/class-(b) run-diff +0/−0 all presets, calibration maps sha256-identical, BIR
54/24/54, validate_corpus_dir 3/3, the stage5 fixture root 66.04/64.98/65.93. **Three DISCOVERIES
were surfaced (D1/D2/D3) — none is a digit moved by this session's work; each is a pre-existing
inconsistency the hardening exposed, recorded and reported, none silently absorbed.**

HEAD at start `f554d74829` → after the Task-0 register commit `f079a78f6c`; corpus `c50002fee1`;
music21 9.9.1.

---

## 1. The establishment battery (the session's instrument)

`tools/audit/hardening_battery.py` (commit `979e07db46`) — orchestrates the committed instruments
exactly as used, defines no metric of its own, PASS/FAIL per gate vs the committed reference:

| Gate | What | Cadence |
|---|---|---|
| `a8_diff` | a8_rebaseline_measure → scratch, then robust_stop_diff vs `tools/robust_stop`; PASS iff diff exit 0 AND every preset (+0/−0) AND WiR coverage unchanged | after every fix |
| `calib` | calibration_fit → scratch; PASS iff all 4 committed `tools/calibration_maps/*.json` reproduce sha256-identical | after every fix |
| `validate` | `validate_corpus_dir` on all 3 presets | after every fix |
| `fixture` | stage5_fit_driver fixture (full corpus regen ×3 + a8); root-% stability vs the recorded baseline | start + end + OI-133 |
| `regen` | run_bach_preset → scratch, per-score sha256 vs `tools/corpus` | only on a batch_analyze.cpp touch (none landed) |

**Clean starting state (recorded before any fix):** a8_diff PASS (+0/−0 all presets, class-(b) Δ+0,
coverage 326/326/326, key-agree home 71.29/67.49/70.52 local 65.72/62.49/65.39); calib 4/4
byte-identical; validate 3/3 OK (352/352, git c50002fee1); BIR 54/24/54; fixture reproduces root
66.04/64.98/65.93 batch 54/24/54 **deterministically** (but see D1).

**Final state (after all landed fixes):** identical — a8_diff PASS +0/−0, calib 4/4, validate 3/3,
BIR 54/24/54, fixture root 66.04/64.98/65.93 stable + now self-reports MATCH/PASS (D1 corrected).

---

## 2. The three discoveries (surfaced, not absorbed)

**D1 — the stage5 fixture's self-check was left stale by the OI-142/OI-143 re-baseline.** The
adoption `d9b52ba969` (user-ratified) moved the a8/robust_stop reference + CLAUDE.md + manifest to
root 66.04/64.98/65.93, but `stage5_fit_driver`'s hardcoded `RATIFIED` constant (63.36/62.37/63.25)
and its "vs 53/24/53" batch prose were NOT updated then. At HEAD the fixture reproduced the correct
user-ratified numbers yet self-reported MISMATCH / FIXTURE:FAIL. **Not a digit moved by this session
— a stale figure exposed by the battery.** Corrected under OI-133 to the ratified reference (the
measurement never changed); the fixture now self-reports MATCH/PASS. No re-baseline needed (the
target was already ratified).

**D2 — the two OURS key parsers embed a genuine music-theory divergence (OI-132 DT-6).**
`oracle_root_metric.parse_our_key` (exact mode-set) and the shared `compare_rn._our_key_tonic`
(prefix rule maj/ion/lyd/mix) disagree on the dominant-family exotic modes: PhrygDom + alt = MAJOR
vs minor, Lydb7 = None vs major (98 + 24 + 5 corpus regions). A/B on all 3 presets: `parse_dcml_key`
IS byte-identical to `_dcml_key_tonic`, but swapping `parse_our_key` → `_our_key_tonic` **MOVES**
oracle_root_metric's KEY-tier split (jazz +1, default +13 records shuffling KEY-HARD /
KEY-TONICIZATION / AMBIGUOUS; the charged/floor ROOT sets — the primary 3878/… metric — are
UNCHANGED on all presets). `compare_rn` is also the substrate the RATIFIED a8 key-agree column uses,
so the other fold direction would move that column instead — **neither direction is byte-identical.**
Consolidating needs a music-theory adjudication (which reading is authoritative) + a coordinated
re-baseline. NOT done silently; the dead `lt_2` (DT-5) WAS deleted; a prominent note added at
`parse_our_key`. OI-132 stays OPEN on the DT-6 adjudication.

**D3 — the committed calibration maps + secondary graded figures are on PRE-OI-142 (uncorrected)
WiR (OI-144).** `c1_reliability._load_wir` (and via it `calibration_fit`) + `oracle_root_metric`
read WiR through the RAW `parse_rntxt_file`, NOT the OI-142-corrected `load_wir_regions` the four
governing consumers use. MEASURED: patching `_load_wir` to the corrected substrate and re-running
`calibration_fit` **MOVES all 4 committed `tools/calibration_maps/*.json`** — the committed maps are
fit on the uncorrected WiR (the 12 transposed pieces graded wrong). Since these are GRADED surfaces,
routing them through the corrected substrate is the correct fix BUT it MOVES committed artifacts → a
RE-BASELINE needing the full ritual (O-12 snapshot + user ratification), NOT a byte-identical hygiene
edit. NOT done this session; a prominent uncorrected-WiR caveat note added at each raw read site.
**Surfaced for the user's decision; the routing waits on the ratified re-baseline.**

---

## 3. Per-row disposition

### The five blocking rows

**OI-140 — WiR-coverage reconcile closes the governing hard-stop's silent shrink** (commit
`1d634abd30`). a8_rebaseline_measure distinguishes a MISSING WiR annotation (find_wir_file None →
`wir_no_annotation`) from a PARSE FAILURE (present file that throws/yields 0 → NAMED per-stem +
loud stderr); publishes `coverage.wir_covered/wir_no_annotation/wir_parse_fail`; `robust_stop_diff`
reconciles the candidate `wir_covered` against the reference and FAILs (exit 1, `COVERAGE SHRUNK`)
on any shrink. Reference manifest re-stamped with the coverage sub-fields (metadata only). Guard
proven by a simulated shrink (321<326 → FAIL). Battery: PASS byte-identical. **CLOSED.**

**OI-124 — fingerprint the .music21.json ground truth + the WiR source identity** (commit
`0a6d0d9ff5`). `run_bach_preset._write_manifest` records the `.music21.json` sha256; `validate_corpus_dir`
checks it (backward-compatible); the 3 local manifests re-stamped provenance-preservingly (git_hash
c50002fee1 kept). A mandated poisoned-GT scan of all 1056 committed `.music21.json` found **0
error-field / 0 zero-region / 0 unparseable** — no OI-123/OI-128-shape poison (no discovery).
`robust_stop_diff` cross-checks the reference manifest class-(b) against its sibling `summary.json`
and surfaces WiR-source drift; a8 publishes `coverage.wir_source_sha256`. Tamper-detection proven.
Battery: PASS. **CLOSED.**

**OI-129 — the grading chain routes through validate_corpus_dir** (commit `ee84ff9d70`).
`calibration_fit` (per carrier) + `c1_reliability` (per preset) now call `validate_corpus_dir` on
`tools/corpus/{preset}` before reading it (now including the OI-124 GT fingerprint). Byte-identical:
4 maps sha256-identical, c1 clean. RESIDUAL: the km/fs scratch substrate stays manifest-less
(producer-side, tracked; addressed partially by OI-35). **CLOSED (mandated half).**

**OI-132 — DISCOVERY D2 (above); dead `lt_2` deleted** (commit `eb58d905e1`). OPEN on the DT-6
adjudication.

**OI-33 — the abstain-aware grading convention** (commit `5e4c7171fd`). Convention WRITTEN (a8
docstring + robust_stop `manifest.abstain_convention_note`) + mechanically ENFORCED: ROOT counts an
abstained cell as a DISAGREEMENT (not abstention-reducible); KEY-agree EXCLUDES abstained cells, so
`robust_stop_diff` reports the key-abstain BESIDE key-agree and FLAGS a candidate abstain above the
reference (at the manifest's 4-dp precision — no false-fire on the clean run; the flag fires on a
simulated rise 0.09→6.03 %). Informational only; exit code + pinned root metric untouched. Battery:
PASS. **CLOSED.**

### The Task-3 rows

**OI-123 + OI-128 — narrow the DT-23 silent-failure swallows** (commit `704d1abbf6`). Two
wrong-bucket folds CLOSED: (1) music21_batch — a chordify() failure wrote `{regions:[], error}`
straight to `{stem}.music21.json` (a FAKE GT); it now writes `{stem}.music21.FAILED.json` + returns
None (no GT file). (2) a8 — a corrupt `.ours.json` was folded into `no_wir`; it now has its own
`coverage.ours_load_fail` bucket (+ `empty_ours`, `m21_load_fail`). Broad excepts narrowed to the
load/parse types + surfaced with the stem across dcml_parser, compare_rn (whole-piece drops),
oracle_root_metric, characterise_bir_false, analyze_inversion_errors, c1_reliability (6),
calibration_fit (5). Byte-identical (0 failure population; the OI-124 scan found 0 poisoned GT).
Battery + BIR 54/24/54 unchanged. **BOTH CLOSED.**

**OI-130 — scratch-default outputs + enforce the music21 pin** (commit `cab69d1fef`). No instrument
defaults its output into a committed artifact: music21_batch `--output`, calibration_fit `--out-dir`,
stage5_fit_driver `split --out` all default to scratch. The music21 v9.9.1 pin is enforced at run
start where GT is produced (music21_batch exits 2 on a mismatch unless `--allow-version-mismatch`;
proven: simulated 9.0.0 blocks, installed 9.9.1 passes). Byte-identical. **CLOSED (DT-24 family
closed at the producing side).**

**OI-126 — delete the two dead DCML parsers + single-source the note→pc map** (commit `bac76ce676`).
`parse_dcml_file` + `find_dcml_file` DELETED (verified dead by repo-wide grep = only self/docstring/
frozen-audit-artifact refs); `compare_rn._KB_NOTE_OURS/_KB_NOTE_DCML` single-sourced from
`dcml_parser._NOTE_TO_PC` (were 3 verbatim copies). Byte-identical. **CLOSED.**

**OI-125 — centralize the comparator's hand-set tolerances** (commit `eae9cf2ea2`).
`compare_analyses.py` gains one named block: `ALIGN_OVERLAP_FRACTION`=0.5, `ALIGN_BEAT_DISTANCE_TOL`=0.5
(split out, semantically distinct), `EXTRAPOLATION_BEATS_PER_MEASURE`=4 — each `[hand-set;
re-derivation flagged]`. Byte-identical. RESIDUAL: the re-derivation (#19) is later work. **CLOSED
(single-home + note half).**

**OI-133 + OI-138 + OI-139 — doc-precision + the D1 fixture correction** (commit `5df81720d9`).
D1 corrected (above); oracle_root_metric docstring figures → pointer to regenerable output (#17f);
analyze_inversion_errors dangling `chordanalyzer.cpp ~1916-1923` anchor → symbol-led + its empty-input
error prints the real dir; param_manifest.json batch_analyze line-anchors → symbol-led (OI-138) +
functionresolver.h site lines restamped 197–200/258 → 211–214/272 (OI-139); BUILD_AND_TEST.md
`--preset jazz` → `Jazz`. Byte-identical; fixture MATCH/PASS. **ALL THREE CLOSED** (OI-133 residual:
the 13 scattered tolerances flagged for re-derivation).

**OI-144 — DISCOVERY D3 (above)** (commit `9275fc3790`). Caveat notes added at the raw read sites;
routing the graded surfaces waits on the ratified re-baseline. **STAYS OPEN.**

**OI-35 — read-site substrate-coverage validation** (commit `cdfc374661`). The generalized
"validate-or-re-manifest at the read site" rule applied at the km/fs read (calibration_fit checks
the substrate's per-carrier stem coverage vs the validated corpus + surfaces a partial/stale
substrate; silent on the full substrate today → byte-identical). RESIDUAL: a full manifest-based
validate needs the km/fs producer to stamp a manifest (OI-129 km/fs half). **CLOSED (read-site half).**

---

## 4. OI-145 wave-1 completion state

**Closed this session (13 rows + the battery):** OI-140, OI-124, OI-129 (mandated half), OI-33,
OI-123, OI-128, OI-130, OI-126, OI-125, OI-133, OI-138, OI-139, OI-35 (read-site half). Discoveries
D1 (resolved), D2 (surfaced, OI-132 open), D3 (surfaced, OI-144 open).

**Remaining wave-1 rows (deferred at a clean row boundary, battery green — Task 4.4):**

- **OI-132 (DT-6 key-parser)** — OPEN pending the music-theory adjudication (D2). The dead-code half
  is done.
- **OI-144 (D3)** — OPEN pending the ratified re-baseline that routes the secondary graded surfaces
  through `load_wir_regions`. The surfacing + caveat notes are done.
- **OI-135, OI-136, OI-137 (batch_analyze.cpp)** — DEFERRED as a coherent unit: all three touch the
  one C++ harness and therefore require a build + the mandated full corpus-regen sha256 verification.
  **OI-135** (single-source the "Default" 21 mode priors + the `onsetBoundaryThreshold` 0.25) needs
  the CLI to initialize and read the composing module's Settings-framework defaults
  (`settings()->setDefaultValue(MODE_PRIOR_*, …)` in `composingconfiguration.cpp`) — a
  config-unification architectural change, not a byte-identical hygiene edit; the values are proven
  copies today (the corpus reproduce-check passes). **OI-136** (add the 6 undocumented flags to
  `printHelp()`) + **OI-137** (document the CRLF/exit-path asymmetry) are byte-identical but share
  the same build+regen gate. Not attempted rather than thin the mandated verification.
- **OI-125 / OI-133 residuals** — the actual re-derivation / oracle-establishment of the hand-set
  tolerances (#19) is later work, flagged per constant.
- **OI-127** (documented/minor + audit-tooling notes) — not in the Task-3 dispatch; not addressed
  this session.

**The gate lifts when the listed rows close.** OI-145 wave 1 is substantially delivered (the five
blocking rows all closed or their blocker surfaced); the remainder is the batch_analyze.cpp build
group + two discovery-adjudications + the flagged re-derivations.

---

## 5. Self-check (over every diff, before reporting done)

- Every fix is one revertible commit; the register flip rides the SAME commit as its fix (isolated
  via git plumbing so Cowork's concurrent OI-145/OI-146/CLAUDE.md working-tree edits never rode my
  commits — the OI-85 discipline).
- No self-invented labels/jargon; plain-language register + commits; American English.
- The battery ran after every fix (byte-identical throughout); the three discoveries are the only
  deviations and each is surfaced (own register status + this report), never absorbed.
- Staged only my own files by name; `cowork_joint_key_chord_design.md` (+ the other concurrently-
  edited Cowork docs) stayed unstaged; `cc_*.md` gitignored, this report + the instruction force-added.
- `upstream` push confirmed disabled; pushed to `origin` only.
