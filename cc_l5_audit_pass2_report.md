# L5 (function) + INSTRUMENTS Certification Audit — PASS 2 (blind second reading + catalog sweep + measured error rate)

**EG-7 / OI-84 / OI-116. CC session, 2026-07-12.** The second and final pass of the L5
dependency-ordered certification, and the last session of the whole OI-84 plan.
Read-only fact-finding plus the one authorized deletion (Task 0). No production change, no
constant tuned, no golden refresh; `tools/robust_stop/` and `tools/corpus/` written by
NOTHING this session.

---

## 0. Task-0 preconditions, register commit, and the authorized deletion

- **Register commit** `e6d6df8a46` (`docs(cowork):`) — staged `OPEN_ITEMS.md` (Cowork's
  waiting edits: OI-134 deletion authorized + OI-38 corpus-expansion directive) **without
  opening it**, force-added `cc_instruction_l5_audit_pass2.md`. `git status` after: only the
  known carry `cowork_joint_key_chord_design.md` + untracked scratch — clean.
- **Authorized deletion (OI-134)**: `tools/tools/` (untracked debris, 0 git-tracked files,
  312 MB) deleted with `rm -rf`. Confirmed afterward: `tools/tools/` no longer exists;
  `git status --short` unchanged by the deletion (the directory was untracked/ignored). The
  justifying comparison is committed in the harness pass-1 fold (`708d0c3708`); OI-134 closes
  here.
- **Git state (no commit messages displayed):** `HEAD = e6d6df8a46…` at Task 0;
  `git merge-base --is-ancestor 38a1adeaeb HEAD` → `exit:0`.

## 1. The blind work (Task 1) — sample designs, seeds, method

**Sampler:** `tools/audit/gen_pass2_sample_l5.py` (committed), adapted from the L4 sampler.
Rebuilds the full 3,372-row domain from the RAW inventory (`l5_*.csv`) only — never reads a
`pass1_dispositions_*`. Self-checks the domain against the frozen counts before drawing
(total 3372; per-kind and per-population exact); aborts on drift.

**NEW seeds, distinct from every recorded audit seed** (L1/L2 20260711/424242; L3 pass-1
20260712/13 + pass-2 20260714/15; L4 pass-2 20260801/02):
- **Reading sample** — seed **20260901**, ≥140 rows: a TWO-LEVEL proportional draw — across
  the four populations in proportion to their row counts (dormant resolver 34 / instrument
  core 40 / grading+fitting 30 / harness 36 = 140), then across the seven deep row kinds
  within each population, plus coverage top-ups so all 34 deep files appear → **147 rows**
  (140 + 7 top-ups), all 34 files covered.
- **Error-rate sample** — seed **20260902**, **40 rows uniform over the whole 3,372**.

**Method (the three paid-for lessons baked in):** FULL blinding until the verdicts were
frozen and committed; the error-rate rows judged blind FIRST; the FULL protocol-P2 vocabulary
at full resolution. The 147 reading rows were judged by **six independent, source-only blind
readers** (one per file-group; each read only the named source + grep, forbidden from opening
any `tools/audit/`, `cc_*`, `cowork_*` [except the protocol], `STATUS.md`, `OPEN_ITEMS.md`,
`DEFECT_TYPES.md`) — one row its reader skipped was supplied by the second reader from the
code. The **40 error-rate rows were judged personally by the second reader at the code**,
blind. All verdicts consolidated in `tools/audit/l5/pass2_blind_verdicts.json` (source-tagged)
and applied to the sample files by `tools/audit/apply_l5_pass2_verdicts.py`.

**★ Freeze commit `20fbc8142d` (`feat(tools)`) = the blinding boundary.** Every withheld file
was opened ONLY after it. Reading verdict distribution: SURVIVES 108 / ESTABLISHED 34 /
PUBLISHED 3 / FACT 2 (3 flagged). Error-rate: SURVIVES 30 / ESTABLISHED 10 (1 flagged).

**When each withheld file was first opened — all AFTER `20fbc8142d`:** `OPEN_ITEMS.md`,
`DEFECT_TYPES.md`, `STATUS.md`, the four `cc_l5_audit_pass1_*` reports, and the four
`pass1_dispositions_*` artifacts, in Task 3's mandated order. (The deferred mandatory
`OPEN_ITEMS.md` session-start read was moved to Task 3 by the instruction — the DT-20 fix; no
blinding conflict.)

## 2. Comparison vs pass 1 (Task 3) — both samples

Matched by (file, line, kind); pass-1 kinds normalized (the instruments-core partition tags
kinds in the plural). Axes: `{SURVIVES, PUBLISHED, FACT, THEORY, ASSUMPTION}` = code/fact;
`{ESTABLISHED, UNFIT, DEAD}` = constants; `{RETIRES, DEAD, SILOED, TRAPPED, DUPLICATED}` +
a real defect flag = a defect claim. A **substantive** disagreement = the two sides differ on
whether the row is a defect; a **verdict-axis** difference = same substance, different token.

### 2.1 Error-rate sample (40) — the measured error rate

| class | count |
|---|---|
| token-concordant | 35 |
| verdict-axis (field `SURVIVES`↔`PUBLISHED`) | 4 |
| **substantive disagreements** | **0** |

**★ Measured audit error rate = 0/40 = 0.0 % substantive. No failing rows; no class
re-opened.** (Matches L3 and L4, both 0/40.) The 4 verdict-axis rows are output struct fields
I judged `SURVIVES` (code-axis: the field is legitimate) where pass 1 judged `PUBLISHED`
(derived-fact axis) — both affirm the field is correct. The one row my classifier first
flagged (`oracle_root_metric.py:159`) is a **concordance**: I flagged it `low: silent skip`
and pass 1 dispositioned it `silent-failure-swallow` (OI-128) — both readers independently
caught the same DT-23 site.

### 2.2 Reading sample (147)

118 token-concordant + 17 axis-same + 7 axis-cross + 5 examined. The 7 axis-cross are all
literals I judged `ESTABLISHED` (structural constant) where pass 1 judged `FACT` (music
theory, e.g. `12` pitch-classes, `7`→G) or `SURVIVES` (code) — verdict-axis, no defect
disagreement. The systematic field `SURVIVES`↔`PUBLISHED` axis choice recurs (my readers
foregrounded the code-axis for output fields; pass 1 the more-informative derived-fact axis);
it changes no defect call and re-opens no class — the same axis divergence L3/L4 pass-2
diagnosed. The 5 examined rows, each diagnosed:

1. **`batch_analyze.cpp:3718`** (`onsetBoundaryThreshold = 0.25`) — pass 1 flagged
   `onset-boundary-threshold-hardcoded` (**OI-135b**, DT-3 value-copy); I judged
   `ESTABLISHED` clean. *Miss of a tracked hygiene finding.* Diagnosis: the blind reader
   verified the value mirrors production (correctness-positive) but did not apply the DT-3
   value-copy lens — that is the P8 catalog sweep's role (§3 re-finds it mechanically). Not a
   correctness defect; already tracked.
2. **`batch_analyze.cpp:3982`** (`--reachback-ab`) — pass 1 flagged `flags-absent-from-help`
   (**OI-136**, DT-25); I judged `SURVIVES` clean. Same diagnosis: the reader verified the
   flag is wired/correct but did not run the DT-25 help-text diff (P8 re-finds it). Tracked.
3. **`functionoutput.h:104`** (`wLicensedFit = 1.0`) — I flagged the §7-weights manifest gap
   (**re-found OI-120**) and judged `ESTABLISHED`; pass 1 judged `UNFIT`. Concordant finding,
   constants-axis token difference.
4. **`functionresolver.h:272`** (`maxForwardExtendSlices = 8`) — I flagged a manifest
   site-line drift; pass 1 judged `ESTABLISHED` clean. **A genuine second-pass find** → §4,
   OI-139.
5. **`characterise_bir_false.py:149`** (`except Exception: pass` around WiR parse) — I flagged
   a silent-failure; **pass 1 dispositioned this exact row a clean "control-flow guard"** (not
   flagged). **A genuine second-pass find** → §4, OI-140.

## 3. Whole-scope catalog sweep (Task 4) — all 25 DEFECT_TYPES over all 3,372 rows

**Mechanical rules — `tools/audit/gen_signature_sweep.py --layer l5`** (the ONE
layer-selected instrument; extended additively with an `l5` config + four new rules gated on
`py_rules` so `--layer l1l2/l3/l4` stay byte-identical; the Python-aware signatures the L5
instrument population needs). Fails loud if any rule cannot run. Artifacts:
`tools/audit/l5/sweep_results.{json,txt}`.

| catalog rule | hits | disposition |
|---|---|---|
| DT-2 unestablished constant | 25 | the dormant-resolver `*Params` firewall seeds off the manifest = **OI-120** — and the sweep **mechanically corrects OI-120**: `wLicensedOut/wLicensedIn/wCadentialFit/decidingMargin/maxForwardExtendSlices` are ABSENT from the hits (i.e. registered in G8), contradicting OI-120's "NOT registered / only the θ pair" claim (§4, OI-139) |
| DT-3 value-copied constant | 5 | 2 real in `batch_analyze.cpp` Default-carrier block (`bassNoteRootBonus 0.70`/`presetKWStepIn 0.125` "== struct default") = **OI-135** family; 3 false positives (the `metricWeight` "higher = stronger" comment fooled the soft-copy regex) |
| DT-5 siloed fact | 7 | all dormant-resolver functions with 0–1 production consumers = the **declared dormancy** (OI-116/OI-117; pass-1 resolver P4 "no `src/` consumer"); `deriveBaseRomanNumeral` (0 consumers) is the g1b DUPLICATED-tendency note (retires at engage). Not defects |
| DT-5 dead local field | 0 | no dead local C++ struct field in the dormant resolver (pass-1 "no DEAD" reproduced) |
| DT-12 stale anchor (source→doc) | 2 | both **false positives** — the content-check's symbol-hint regex grabbed prose words ("falling", "adoption") from comment text, not real symbols; the `.cpp:line` anchors are ordinary prose |
| DT-12 manifest-site drift (manifest→source) | 5 | **NEW** (my rule): the manifest's `functionresolver.h` site lines (`:197/198/199/200/258`) are stale by ~14 — actual decls at `211/212/213/214/272`. § 4, **OI-139** |
| DT-16 raw-DOM outside L1 | 0 | the dormant resolver is hand-injected; the harness reads via the pipeline, not raw `->notes()` |
| DT-19 layer-boundary upward include | 1 | `batch_analyze.cpp:109` includes `grouping/groupinglayer.h` (L6) — the harness is a driver that exercises `--dump-l6`; a legitimate driver include (same class as its other crosslayer includes, pass-1 SURVIVES) |
| DT-23 silent-failure (Python) | 40 | reproduces + **extends** OI-123 (core) + OI-128 (grading+fitting): the enumerated consequential subset (~21) plus same-family best-effort/informational excepts, **and** the consequential untracked WiR path `a8_rebaseline_measure.py:307` + `characterise_bir_false.py:149/152` → §4, **OI-140**. Full 40-site list in `sweep_results.json` |
| DT-24 destructive default | 2 | `music21_batch.py:515 --output tools/corpus` = **OI-130** (genuine); `run_bach_preset.py:292 --corpus-dir tools/corpus` = **false positive** — a read-only INPUT default (its output defaults to the SEPARATE `tools/corpus_{preset}`, clean-slated only when separate) |
| DT-25 undocumented mode | 7 | `--reachback-ab` + the 5 `--key-in-*` = **OI-136** (exactly); `--help` is a benign self-reference (the help flag does not list itself) |

**Review rules (DT-1, DT-4, DT-6, DT-7, DT-8, DT-9, DT-10, DT-11, DT-13, DT-14, DT-15,
DT-17, DT-18, DT-20, DT-21, DT-22)** — applied against the full inventory + pass-1
dispositions + my reading; every one maps to an existing register row with **no new
correctness defect**: DT-22 = OI-118/OI-119 (its founding instances; no new signed-rule
divergence found); DT-11 = OI-133/OI-114; DT-6 = OI-132/OI-126; DT-7 = the dormancy
(OI-116/OI-117, declared, not a never-fires defect); DT-21 = OI-117; DT-17 = OI-122; DT-4 =
none (the resolver is selection-only, never overwrites a committed field — g1a confirmed);
DT-1/DT-8/DT-9/DT-10/DT-13/DT-14/DT-15 = no L5 hit / Stage-5-owned (OI-25/OI-27/OI-33);
DT-18/DT-20 = not applicable this session (Task-0 was clean; the instruction correctly
withheld `OPEN_ITEMS.md` until after the freeze — the DT-20 fix held).

**★ The sweep found NO untracked correctness defect.** Every mechanical hit is covered by an
existing register row, a false positive (reviewed), or one of the two new non-correctness
findings below.

## 4. New findings (register rows)

- **OI-139 (NEW) — OI-120 factual correction + `param_manifest.json` `functionresolver.h`
  site-line drift (DT-12).** At HEAD the manifest **registers** `wLicensedOut`, `wLicensedIn`,
  `wCadentialFit`, `decidingMargin` (G8, `§15-13`) and `maxForwardExtendSlices` (G8,
  `abstention`) — all `functionresolver.h` params — contradicting **OI-120's** "ONLY the
  `forwardoverride` θ pair is in the manifest / FunctionResolverParams
  wLicensedOut/In/wCadentialFit/decidingMargin NOT registered." The manifest predates the
  audit (last committed `c50002fee1`), so OI-120 erred, not the manifest — OI-120's true
  gap is the cadence/modulation/output/recognition seeds (the DT-2 sweep's 25 hits), NOT
  these 5. Separately, the manifest's `site` lines for those 5 are **stale by ~14** (cites
  `:197/198/199/200/258`; actual `211/212/213/214/272`) — a DT-12 manifest-anchor drift
  (sibling of OI-138a, different file). Mechanically confirmed by the new
  `DT-12_manifest_site_drift` sweep rule (5 hits). Fix at the EG-5/Stage-5 manifest work +
  the next manifest restamp (`#8`; auditor did not amend).

- **OI-140 (NEW) — WiR-coverage → the governing hard stop can pass silently (DT-23 + DT-2;
  second-pass find, cross-refs OI-123/OI-124).** `a8_rebaseline_measure.py:307-310` (the
  GOVERNING regression-stop measurement) wraps `dcml.parse_rntxt_file` in a broad
  `except Exception: wir_regions=[]` then `if not wir_regions: continue` — a WiR-parse failure
  silently EXCLUDES that piece from the variant-(b) class-(b) measurement. `robust_stop_diff.py`
  never reconciles WiR coverage between candidate and reference (grep: zero
  coverage/`wir` references). So a systematic WiR-parser breakage in a candidate run would drop
  pieces, LOWER the class-(b) root-disagree duration, and PASS the automated non-increase hard
  stop. Mitigation exists but is human-dependent: the mandatory explained per-run set-diff
  (CLAUDE.md block A) would list the removed runs for a reviewer — the automated gate would
  not fail. `characterise_bir_false.py:149-153` has the identical diagnostic-side
  `except Exception: pass` (pass 1 dispositioned that exact row a clean control-flow guard).
  LATENT today (runs reproduce byte-identical, failure population empty) — the same character
  as OI-123/OI-124, which pass 1 tracked OPEN. Fix: a WiR-coverage reconcile in
  `robust_stop_diff` + a skip-counter/surfacing on the a8/characterise WiR excepts, at the next
  corpus-tooling touch (`#8`; auditor did not amend).

Also recorded (report-level, no new row): the DT-23 sweep's 40 sites are broader than
OI-123/OI-128's enumerated ~21 — OI-123/OI-128 should be broadened to the full
`sweep_results.json` list at their next touch (a note added on those rows). No new DEFECT
TYPE was founded this session — every finding maps to DT-2/DT-3/DT-5/DT-12/DT-19/DT-23/DT-24/
DT-25.

## 5. Certification proposal (Task 5) — PROPOSED, awaiting the user's decision

The four conditions are met: (a) the first pass is complete across all four populations
(OI-116); (b) the blind reading (147, seed 20260901) and error rate (40, seed 20260902) were
measured at FULL P2 vocabulary resolution, frozen at `20fbc8142d` before any withheld file was
opened; (c) every disagreement is diagnosed (§2 — all verdict-axis, or tracked findings the
P8 sweep re-finds, or the two second-pass finds); (d) the whole-scope 25-DT sweep found NO
untracked correctness defect. **Measured error rate 0/40 substantive.**

**★ I therefore PROPOSE certifying Layer 5 (function) + the instruments — proposed, awaiting
the user's decision. NOT self-granted; OI-84, OI-116, and the Stage-3 entry-gate condition
are left OPEN.** The proposal is weakened only by named, tracked, **non-correctness** gaps,
every one an engage-time / next-touch fix: the DORMANT signed-rule divergences OI-118/OI-119
(DT-22, fix before the modulation/cadence path engages); the manifest gaps + site-drift
OI-120/OI-139; the instrument silent-failure / establishment / destructive-default /
duplication findings OI-123–OI-133; the harness findings OI-135–OI-138; and the new
WiR-coverage hard-stop gap OI-140. None is a correctness defect; all are consistent in
character with the pass-1 findings the user has been tracking.

**Completion statement (orientation for the user, not a status I set):** IF the user grants
this certification, the **OI-84 dependency-ordered certification plan is COMPLETE** — every
surviving layer (L1/L2, L3, L4, L5) and the measurement chain audited on two passes each — and
per the register the **held OI-43 discussion opens** (mode/key + chord inference — where and
how; OI-44's single-declared-joint-step status decided in the same discussion), along with the
remaining Stage-3 entry-gate items OI-1…OI-7.

## 6. Self-check

Re-read the diff of every touched file against the guiding principles, conventions, and gate
policies: sampler is mechanical + seeded (no hand-picked rows); seeds distinct from all
recorded; two-level population×kind stratification + uniform-40 per the instruction; verdicts
use only the P2 vocabulary + inventory row-kind names (no invented labels/abbreviations); the
sweep-tool edits are additive + gated (other layers byte-identical); no production code, no
constant, no golden touched; `tools/robust_stop`/`tools/corpus` unwritten; findings became
register rows, not patches (auditor, not amender); plain-language finding slugs throughout.
Task-0 deletion confirmed. Push to `origin` only (`upstream` push disabled — verified).
