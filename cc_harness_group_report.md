# CC — the harness group (OI-145 wave-1 remainder): OI-135 / OI-136 / OI-137 + OI-153 + OI-52

**Session:** CC, 2026-07-13. **Dispatch:** Cowork's harness-group instruction (force-added at the fold).
**Type:** a FIXING session on the shared measurement harness and the establishment/register tooling —
**not inference coding.** No `src/composing` analysis behavior changed.

**Governing outcome, met: BYTE-IDENTICAL.** No grading digit moved, the committed corpus regenerates
bit-for-bit (0 of 1056 `.ours.json` differ), no golden refresh was owed, and every gate reproduced.

**One discovery, declared not absorbed: OI-155** — the OI-132 consolidation left two regression tests
red, and one of them hides a grading-semantics question the user has never ruled on. Pre-existing;
verified not caused by this session's work. It is the one thing on this page that needs a decision.

---

## 1. What landed

| commit | item | substance |
|---|---|---|
| `0922e2bfdc` | Task 0a | Cowork's four register/design edits, committed by name and unread. `cowork_joint_key_chord_design.md` left uncommitted (the standing carry). |
| `a62c67e423` | **OI-153** | The register ID-collision lint, wired as gate 0 of the establishment battery so it runs at every fold. |
| `70f64e4bcb` | **OI-135** | The two value-copied inference-affecting constants, genuinely single-sourced. |
| `92d5092f33` | **OI-136** | The six undocumented measurement flags surfaced in the harness's own `--help`. |
| `f4d1878dcf` | **OI-137** | Output + exit disciplines **established**; neither changed, and the code now records why. |
| `375c984366` | **OI-52** | One shared root-comparison helper across every graded site. |
| `3f839e0e24` | **OI-155** | The discovery, filed as its own row + commit. |

---

## 2. The establishment battery — before and after

The battery (`tools/audit/hardening_battery.py`) was run to record the clean starting state, after the
Python fold, and after the harness rebuild. **The `regen` gate is the load-bearing one for this
dispatch** — it is the only proof that recompiling `batch_analyze.cpp` changed nothing.

| gate | start | after OI-52 (Python) | after the rebuild | proves |
|---|---|---|---|---|
| `register` | *(did not exist)* | PASS 154 IDs | **PASS** 155 IDs, no collision | OI-153 |
| `a8_diff` | PASS +0/−0 ×3 | **PASS +0/−0 ×3** | **PASS +0/−0 ×3** | class-(b) hard-stop duration Δ+0; the governing metric |
| `calib` | PASS 4/4 | PASS 4/4 | **PASS 4/4** | the four committed calibration maps reproduce sha256-identical |
| `validate` | PASS 3/3 | PASS 3/3 | **PASS 3/3** | corpus integrity, 352/352, `c50002fee1` |
| **`regen`** | — | — | **PASS — baroque 0 differ, jazz 0 differ, default 0 differ** | **the 352×3 byte-identity proof** |

**Suites:** composing **1103/1103** (1101 + the 2 new contract tests), notation **53 + 4 skipped**,
pipeline-snapshot **11 + 1 skipped — no golden refresh owed**, `test_batch_analyze_regressions` passed.

**Ratified figures, unmoved:** root 66.04 / 64.98 / 65.93, RN 46.33 / 44.10 / 46.23, key HOME
71.42 / 67.83 / 70.65, key LOCAL 65.99 / 62.98 / 65.71. Batch diagnostic reproduces 54 / 24 / 54.

---

## 3. Prediction vs outcome (#17b — written before measuring)

| # | prediction, written first | outcome |
|---|---|---|
| whole dispatch | every gate byte-identical; regen 352×3 sha256 identical; a8 +0/−0; calib 4/4; suites green | **met exactly** |
| OI-135(a) | the 21 harness literals are proven copies of the 21 app defaults, so single-sourcing cannot move a value | **met** — machine diff *before* the edit: 21/21 identical, zero differences |
| OI-135(b) | the `AnalyzeRegionsOptions` struct default is already 0.25, so reading the shared constant cannot move a value | **met** |
| OI-137(a) | flipping the standard path to binary/LF would rewrite **every** committed `.ours.json` | **met** — all **1056** are strictly CRLF and **all 1056** would change sha256 |
| OI-137(b) | the exit-code behavior is unchanged | **met** — standard 0, `--validate-slices` 0, unreadable score 1 |
| OI-52 | the helper is the same expression, so every site's verdict is unchanged | **met** — proven *exhaustively* (below), not sampled |

Zero surprises (#3). Every figure landed where it was predicted to land.

---

## 4. OI-135 — single-sourced, not sync-tested

The dispatch offered a mechanical sync test as the documented fallback. It was not needed: the **true
#6 fix was available**, because `composing_analysis` is the one library both the app and
`batch_analyze` link — which is precisely why `modePriorPresets()` was moved there in the first place.
The same door was open for both constants.

**(a) The 21 "Default" mode priors.** They now live once, in `mu::composing::modePriorAppDefaults()`,
read by **both** `ComposingConfiguration::init()` (which registers them as the `MODE_PRIOR_*` settings
defaults) and the harness's `"Default"` branch. The hand-copied literal block and its "KEEP IN SYNC"
comment are gone. `applyPreset()`'s *second* copy of the 21-line assignment block — the named-preset
loop — folded into one `applyModePriors()` helper as well.

**(b) `onsetBoundaryThreshold`.** Now `analysis::kDefaultOnsetBoundaryThreshold` in the dependency-free
types leaf, read by the `AnalyzeRegionsOptions` struct default, by the settings registration, and by the
harness's three sites. This closes the documented roadmap-0.6 divergence: a change to the config default
can no longer leave the corpus measuring a pipeline nobody runs.

Two contract tests were added that *establish* (rather than restate) the documented claim that the app
defaults are neither "Standard" — they diverge on exactly **11 of the 21** modes and agree on the other
10 — nor a sixth named preset.

**Residual, named not hidden:** `notationharmonicrhythmbridge.cpp:85` still carries a 4th literal `0.25`
as its null-config fallback. It is a one-line change to read the same constant, **not made** because that
file is outside this dispatch's authorized edit scope.

---

## 5. OI-137 — established, and *therefore* not changed

Both halves were measured, and the measurement is what says leave them alone.

**(a) Line endings.** All 1056 committed `.ours.json` are strictly CRLF, and all 1056 would change
sha256 if the standard path were opened binary. Dropping `QIODevice::Text` is a **full-corpus
re-baseline**, not a cleanup — out of scope. The dispatch also invited "aligning the diagnostic writers,
which are not corpus"; **that was declined on the evidence.** The diagnostic writers already use
`std::ofstream(std::ios::binary)`, which is the **OS-independent** discipline. Aligning *them* to the
standard path would spread the platform dependence rather than remove it — the correct alignment
direction is the other one, and that is the re-baseline.

**The live hazard, now stated in the code:** corpus byte-identity holds only while regeneration stays on
Windows. The same code on Linux writes LF, and every fingerprint in `corpus_manifest.json` moves (#16).

**→ A byte-identical fix exists, and is offered rather than taken** (§8).

**(b) Exit-path asymmetry.** Established as **load-bearing in both directions, not an oversight** —
which inverts the framing the row was filed under:

- The **standard path may** force-exit: it has already flushed and closed everything by hand
  (`cout.flush()` + `fflush(stdout)`, or `outFile.flush()` + `close()`), so skipping the destructors
  cannot truncate it. Every error return happens *before* it — verified at the binary: an unreadable
  score exits 1. It masks no failure code.
- The **diagnostic paths may not** adopt it: they rely on `std::ofstream`'s **destructor at scope exit**
  to write their output, which `_Exit`/`TerminateProcess` would skip — **truncating it**. And
  `--validate-slices` returns a meaningful 0/2 that a `force-exit(0)` would silently swallow.

So "tidying" this asymmetry in either direction would have introduced a defect. Verified side by side at
the built binary on one score: standard → exit 0, 1704 CRLF / 0 LF; `--validate-slices` → exit 0,
0 CRLF / 17 LF, output complete.

---

## 6. OI-52 — the shared helper, and the D2 risk actually checked

`compare_analyses.roots_agree()` now owns the "does our root equal the ground-truth root" decision.
Its substance is not `a == b`; it is the **abstain convention** (OI-33), now encoded once instead of
carried by prose across several copies — the construction that let two copies of the *key* parser drift
into different readings (OI-132's discovery D2), where folding them *moved a graded figure*.

**A complete enumeration found three sites the register row had not listed** — `three_way_classify`
(the three-way BIR metric's ours-vs-DCML leg), `dcml_direct`, and `dcml_anchored`. They were folded too:
closing the row while leaving three more copies of the very comparison it is about would have been a
false close. `three_way_classify`'s *music21*-vs-DCML leg deliberately does **not** route through the
helper — that is corroborator-vs-GT, not ours-vs-GT, and the convention is about *our* abstain.

The scoreability guards (`is not None`) deliberately stay at their call sites: they decide the
**denominator**, not the equality.

**The D2 risk was checked, not assumed.** `compare_analyses.classify` is the one site with no GT-None
guard, where `None == None` → True would read a both-abstained pair as a root match. Measured over the
committed corpus: **0 of 33,296 aligned pairs (all 3 presets) carry a `None` root on either leg** — the
divergence is latent-but-unreachable, and the sites agree in practice as well as in intent.

**Value-identity was proven exhaustively, not sampled:** `roots_agree(a,b) == (a == b)` on all **169**
pairs over the full domain {None, 0..11}², and `three_way_classify` old-vs-new agrees on all **2,197**
(ours, m21, dcml) triples. Inertness on the governing metric was then proven **independently of the C++
work** — the Python fold was gated against the committed corpus *before* the harness was rebuilt.

---

## 7. ★ THE DISCOVERY — OI-155 (needs a ruling)

**The OI-132 consolidation left two regression tests red, and one of them hides a grading-semantics
question nobody has ruled on.** Found while establishing OI-52. **Pre-existing** — verified by re-running
both assertions against HEAD's files with this session's changes absent, where both already failed. The
parent-collection consolidation (`800f1a12bf`, user-ratified 2026-07-13) changed the shared key reduction
but did not update the tests that pin it, so `tools/tests/` has been red since it landed (a **#11** break).

**(a) Stale, and harmless.** `test_metric_primitives_l0l1` expects `_our_key_tonic("EPhrygDom")` to be
`(4, False)` — E minor, the *superseded* same-tonic reading. At HEAD it returns `(9, False)` — A minor,
because E Phrygian dominant is the dominant of A, so the parent collection *is* A minor. **The code is
right and the test is stale;** the correct expectation follows directly from the user's ruling.

**(b) Not stale — a rule nobody stated.** `test_oracle_root_metric` expects
`parse_our_key("Cweird") == (0, None)` — an *abstain* on an unknown mode. At HEAD it returns
`(0, 'minor')`. `parse_our_key` is now a thin adapter over the shared reduction, whose `_mode_is_major()`
is a prefix-membership test — so **any unrecognized mode suffix falls through to minor rather than
abstaining.** An unparseable mode now grades as a *definite minor key* instead of a keyfail.

That cuts against the abstain convention (**OI-33**: an abstain must not be silently converted into a
confident reading), and it is the same family as **OI-152** (the Dor♭2 key-parse abstain). It sat inside
the ratified measurement — the OI-132 report records `oracle_root_metric`'s key tiers shuffling by 5/9/11
identities, all outside the key-error tiers — so **no committed figure is wrong.** But the *rule* was
never stated.

**Not fixed here, deliberately.** (b) is a grading-semantics decision for Cowork/the user, and editing a
red regression test's expectation to match the current code is exactly how a defect gets laundered.

> **Owed:** rule on (b) — *does an unrecognized mode abstain, or read as minor?* — then update both test
> expectations to the ruled behavior in one commit. It blocks nothing measured; the suites stay red until
> it lands.

---

## 8. Two things offered to the user, not taken

1. **The corpus line-ending normalization (OI-137a).** A byte-identical fix exists: open the standard
   output binary and write the CRLF **explicitly**, which reproduces the committed bytes exactly (the
   regen gate would prove it) while removing the dependence on regenerating from Windows. It touches the
   governing instrument's output path, so it is offered for ratification rather than taken as a side
   effect of a byte-identical dispatch.
2. **The bridge's 4th `0.25` (OI-135 residual).** One line in `notationharmonicrhythmbridge.cpp`, outside
   this dispatch's edit scope.

---

## 9. Self-check (the standing rule)

The diff of every touched file was re-read against the guiding principles, the conventions, the gate and
threshold policies, and `DEFECT_TYPES.md` — the work on disk, not the memory of writing it.

- **#6 total unification** — the driver of OI-135 and OI-52. In both, the complete set of copies was
  enumerated rather than trusting the row's list; OI-52 gained three sites that way.
- **#14 one revertible provenance-stamped commit per change** — `batch_analyze.cpp` and `OPEN_ITEMS.md`
  are each touched by three items, so a single commit would have broken revertibility. They were split by
  restoring both files and rebuilding the commits one item at a time; **the reconstructed
  `batch_analyze.cpp` was then verified byte-identical to the version that was actually built,
  regen-proven and suite-tested**, so the split introduced nothing.
- **#13/#3 surprise is a STOP** — one difference appeared during the OI-52 A/B and was chased to ground
  before proceeding. It was **my rig, not the code**: the HEAD-copied tools, run from a scratch directory,
  resolved the ground truth relative to `__file__`, found no WiR, and silently reported *0 coverage* —
  the OI-140 failure mode, reproduced by accident. Replaced with the exhaustive domain proof (§6).
- **No self-invented labels** — every name used here already exists in the repository.
- **#19 established, not merely unfalsified** — the register lint is proven in both directions (passes
  clean on the real register; fails, naming the ID and both line numbers, on a synthetic duplicate).
- **Scope** — no `src/composing` analysis behavior changed; the two `src/composing` edits are a literal
  replaced by the named constant it already equalled, plus the new shared table. Nothing outside the
  authorized scope was touched; `cowork_joint_key_chord_design.md` remains uncommitted.

---

## 10. Status

**The OI-145 wave-1 remainder is closed**, subject to the two named residuals (§8) and the OI-155 ruling.
OI-135 / OI-136 / OI-137 / OI-153 / OI-52 are all flipped with provenance. Waves 2–3 follow; the
key-layer readiness gate lifts when all its listed rows close.
