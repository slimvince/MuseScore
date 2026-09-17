# CC — OI-155: restore abstain-on-unknown in the ONE shared key reduction

**Dispatch:** `cc_instruction_oi155_abstain_on_unknown_mode.md` (Cowork, 2026-07-13, after the user's
ruling on the harness-group report). **Type:** a grading-CONVENTION fix on the measurement chain
(`tools/` only). No `src/composing` inference change; no `src/` change of any kind.

**The user's ruling:** OI-155 resolves as **restore abstain-on-truly-unknown**. An emitted mode suffix
that is not a known-major class, not a known-minor class, and not one of the five parent-collection
exotics **abstains on the mode axis** (a keyfail on the mode axis, per OI-33) instead of being silently
graded minor.

**Outcome: the ruling is implemented, and it moved NO grade.** Every a8 output file — the summary, all
run and cell enumerations, the mapping — is **byte-identical** on all three presets, because all 14 mode
suffixes the corpus actually emits are in the producer's vocabulary, so the restored abstain path fires
on no real cell. The two red tests are green **by the code**, not by an edited expectation. A third,
hidden red assertion in the same test (masked behind the first failure) is also fixed: the same fold had
dropped the reduction's unicode-accidental normalization.

---

## 1. The premise ledger and the written prediction (#17, recorded BEFORE measuring)

| # | premise | class | basis |
|---|---|---|---|
| P1 | The complete set of mode suffixes the chain can emit is the 21 returned by `keyModeSuffix()` in `src/composing/analysis/key/keymodeformatting.cpp`; the graded key string is `keyModeTonicName(fifths, mode) + keyModeSuffix(mode)` (`tools/batch_analyze.cpp:820-821`). | **FACT** | Read at the producer; the switch is total over `KeySigMode` (21 = `KEY_MODE_COUNT`, `keymodeanalyzer.h:47`). |
| P2 | The producer itself declares the major/minor partition of those 21 modes: `keyModeIsMajor()` (`keymodeanalyzer.h:60-75`) — 9 major-third modes, 12 minor-third. The grader must READ that partition, not re-decide it (#6, the fact-publication corollary). | **FACT** | Read at the producer. |
| P3 | The five OI-132 dominant-family exotics (PhrygDom / Mix♭6 / Lyd♭7 / Lyd+ / alt) are graded by the user-ruled parent-collection reduction, ahead of the major/minor partition. Unchanged here. | **FACT** (ratified) | `compare_rn._parent_collection_reduction`; user ruling 2026-07-13. |
| P4 | Every mode suffix that actually occurs in the three committed corpora is one of the 21 and is classifiable — so the abstain path fires on NO real corpus cell. | **FACT (measured, before the fix)** | Scan of all `.ours.json` in `tools/corpus/{baroque,jazz,default}` (§3). |
| P5 | A key-abstain rise is mechanically detected: `a8` publishes `b_key_fail` / `key_parse_fail_pct` and `robust_stop_diff` FLAGS a candidate abstain above the reference (OI-33's enforcement half). | **FACT** | `tools/robust_stop_diff.py:258-272`; `tools/robust_stop/manifest.json` `key_parse_fail_pct` = 0.0 / 0.0492 / 0.0289. |

**THE PREDICTION (written before the measurement, #17b): ZERO real-grade movement.** Fire-rate of the new
abstain path on the corpus: **0 cells, all three presets** (from P4). Direction/magnitude: **none**.
Therefore the full establishment battery must reproduce **byte-identical**: `a8_diff` +0/−0 runs on all
presets, class-(b) duration Δ+0, `calib` 4/4 byte-identical, `validate` 3/3, key columns unmoved (home
71.42/67.83/70.65, local 65.99/62.98/65.71), `key_parse_fail_pct` unmoved (0.0 / 0.0492 / 0.0289), Python
metric suites green, the two named red tests green.

**The STOP condition (not reached):** if ANY real cell newly abstained, that would mean a real emitted mode
fell outside the allowlist — a discovery needing its own register row and a re-baseline decision.

---

## 2. The allowlist, grounded in the producer (§2 of the dispatch)

The mode vocabulary is **owned by the producer** and was read from it, not invented here. Two sources, both
in `src/composing/analysis/key/`:

* **`keymodeformatting.cpp` → `keyModeSuffix()`** — the 21 suffix spellings the chain can emit (the switch
  is total over `KeySigMode`);
* **`keymodeanalyzer.h` → `keyModeIsMajor()`** — the producer's **own** major-third / minor-third partition
  of those same 21 modes (9 major-third, 12 minor-third).

The complete enumeration, partitioned as the ruling requires:

| producer mode (`KeySigMode`) | emitted suffix | producer `keyModeIsMajor()` | grader class |
|---|---|---|---|
| Ionian | `maj` | major | **known-major** |
| Lydian | `Lyd` | major | **known-major** |
| Mixolydian | `Mixolyd` | major | **known-major** |
| IonianSharp5 | `Ion+` | major | **known-major** |
| LydianSharp2 | `Lyd#2` | major | **known-major** |
| Dorian | `Dor` | minor | **known-minor** |
| Phrygian | `Phryg` | minor | **known-minor** |
| Aeolian | `min` | minor | **known-minor** |
| Locrian | `Loc` | minor | **known-minor** |
| MelodicMinor | `mel` | minor | **known-minor** |
| HarmonicMinor | `harm` | minor | **known-minor** |
| DorianB2 | `Dor♭2` | minor | **known-minor** |
| AeolianB5 | `Loc#2` | minor | **known-minor** |
| LocrianSharp6 | `Loc#6` | minor | **known-minor** |
| DorianSharp4 | `Dor#4` | minor | **known-minor** |
| AlteredDomBB7 | `altDom` | minor | **known-minor** |
| PhrygianDominant | `PhrygDom` | major | **parent-collection exotic** (−7, minor) |
| MixolydianB6 | `Mix♭6` | major | **parent-collection exotic** (−7, minor) |
| LydianDominant | `Lyd♭7` | major | **parent-collection exotic** (−5, minor) |
| LydianAugmented | `Lyd+` | major | **parent-collection exotic** (−3, minor) |
| Altered | `alt` | minor | **parent-collection exotic** (+1, minor) |

5 + 11 + 5 = **21** — the partition is total, and every producer mode is placed. **No mode needed a
judgment call**, so there was nothing to STOP on: the two non-exotic classes are exactly
`keyModeIsMajor()`'s partition restricted to the 16 modes the OI-132 ruling does not cover.

**The classification agrees with the superseded prefix rule on all 21 real modes**, which is why no
committed figure was ever wrong. The prefix rule (`mode.lower()[:3] in {maj,ion,lyd,mix}`) was
nevertheless the wrong RULE: it had **no unknown state**, so anything it did not recognize fell through
to MINOR — a change to the emitted vocabulary would have been graded silently instead of surfacing.

**The provenance is now mechanical, not prose.** `tools/tests/test_metric_primitives_l0l1.py`
(`TestModeVocabularyMatchesProducer`) **parses both C++ sources** and asserts the grader's table is
(a) **complete** — every emitted mode is classified, none falls through to abstain; (b) **faithful** —
each non-exotic mode's class equals `keyModeIsMajor()`; (c) **exactly five exotics** — the parent-collection
dict's keys are precisely the five ruled modes; (d) **invented-entry-free** — every grader-set suffix is one
the producer actually emits; and (e) the count equals the producer's own `KEY_MODE_COUNT`. A 22nd producer
mode now turns the suite **red** instead of grading silently.

---

## 3. What the corpus actually emits (the premise-P4 measurement)

Scan of every `.ours.json` region key in the three committed corpora:

| preset | regions | emitted suffixes (count) |
|---|---|---|
| baroque | 11 222 | `maj` 6700, `min` 3510, `harm` 854, `PhrygDom` 45, `Mixolyd` 41, `Dor` 39, `mel` 24, `Mix♭6` 5, `Phryg` 2, `Lyd+` 2 |
| jazz | 10 863 | `maj` 5316, `min` 2913, `Dor` 1166, `Mixolyd` 691, `mel` 421, `harm` 227, `Lyd` 53, `PhrygDom` 40, `alt` 24, `Dor♭2` 5, `Mix♭6` 4, `Lyd♭7` 2, `Lyd+` 1 |
| default | 11 211 | `maj` 6587, `min` 4036, `mel` 177, `harm` 133, `Lyd` 102, `Mixolyd` 84, `Dor` 47, `Mix♭6` 14, `PhrygDom` 13, `Lyd+` 12, `Dor♭2` 3, `Lyd♭7` 3 |

**14 distinct suffixes, all 14 in the vocabulary; zero unknown.** All tonics are ASCII (`A`–`G` with `#`/`b`);
no unicode accidental and no double-sharp spelling occurs. `Dor♭2` is the OI-152 key-parse abstain
(rejected by the mode regex's `[A-Za-z]+`, unchanged here) — it is the whole of the residual key-abstain
(4 080 ticks Jazz / 2 400 Default / 0 Baroque).

---

## 4. The consumer audit (the load-bearing step)

Adding the `(pc, None)` state — tonic known, mode abstained — is a third case that a consumer assuming a
bool could mishandle. Every reader of the mode field was enumerated and checked.

| consumer | reads | treatment of mode=None | action |
|---|---|---|---|
| `compare_rn.key_disagree_subtag` | `_our_key_tonic(...)[1]` | would have compared `(pc, None)` against a bool and returned **`ne_global`** — a fabricated *genuine key error* | **FIXED** — routes through the new `_our_key_ident`; an abstain is `keyfail` |
| `compare_rn.score_regions` (`keyparse_fail`) | element 0 only | would have counted a mode-abstain as a parse *success* | **FIXED** — same helper; the abstain caveat counts both halves |
| `a8_rebaseline_measure.add_cell` (**the governing instrument**) | `_our_key_tonic(...)[1]`, home + local | would have graded a mode-abstain as **`disagree`** instead of `keyfail` — i.e. charged a key error for a key it could not read | **FIXED** — `_our_key_ident`; both columns |
| `classify_key_disagreement._build_cells` | the tuple | same as a8 (it mirrors a8's verdict, by its own stated contract) | **FIXED** — same helper, so the two stay reconciled |
| `oracle_root_metric.parse_our_key` / `_as_mode_name` | the tuple | mapped `None` → **`"minor"`** (the OI-155 defect itself) | **FIXED** — carries the three states; `(pc, None)` = mode abstain |
| `oracle_root_metric.classify_charged_event` (the KEY tiers) | `parse_our_key(...)[1]` | **already correct**: `mode_match = (our_mode is None or dcml_mode is None or ...)` — mode compared only when both sides resolve | none needed (it was written for the pre-fold three-state contract) |
| `c1_reliability` + `calibration_fit` (the fit through it) | `cell["key_verdict"]` from a8's grid | inherit a8's fix; both already **exclude** `keyfail` cells from the key-agree/fit denominator — the correct abstain semantics (an abstain is not a "key incorrect" training example) | none needed |
| `measure_joint_probe` | its OWN enum-index table | **stale, and not because of this fix** — see below | **DECLARED: OI-157** |
| the `cc_*` one-off probes (`cc_eg2_probe`, `cc_floor_classify`, `cc_tonicization_*`, `cc_layer3_keymode_baseline`, `cc_kma_relpair_probe`, `cc_cadence_anchor_measure`) | the tuple | tuple comparisons — no crash; a mode-abstain would read as a key disagreement, but it **cannot fire**: no corpus cell emits an unknown mode | left unchanged (read-only report drivers, not governing surfaces) |

**The one shared decision (#6).** Rather than four copies of "what counts as a key abstain", the audit
produced **one helper** — `compare_rn._our_key_ident(k) -> (tonic, is_major) | None` — that every graded
site now routes through. It returns None when EITHER half of the identity is missing (no tonic, or no mode
class). This is the OI-52 pattern (one shared root comparison) applied to the key axis, and it is what keeps
a8 and the key-disagreement classifier reconciled by construction instead of by prose.

---

## 5. The result — zero movement, proven

**Establishment battery** (`tools/audit/hardening_battery.py`), run on the clean tree before the fix and on
the fixed tree after:

| gate | before | after |
|---|---|---|
| register (OI-153 lint) | PASS — no ID collision | PASS — no ID collision (157 rows) |
| a8_diff (the governing hard stop) | PASS — `diff_exit=0`, run-diffs (+0/−0)×3, coverage OK | **PASS — identical** |
| calib | PASS — 4/4 byte-identical | **PASS — 4/4 byte-identical** |
| validate | PASS — 3/3 | **PASS — 3/3** |

**Stronger than the gate:** every file `a8_rebaseline_measure.py` writes is **byte-identical (sha256)**
before vs after — `summary.json` (which carries root, RN, key-home, key-local, the class-(a)/(b) durations
and `b_key_fail`), all six variant-(a)/(b) run and cell enumerations, and all three mapping files. 16 of 16
outputs identical, all three presets. So root **66.04 / 64.98 / 65.93**, RN **46.33 / 44.10 / 46.23**, key-home
**71.42 / 67.83 / 70.65**, key-local **65.99 / 62.98 / 65.71** and the key-abstain **0.0 / 0.0492 / 0.0289 %**
are all exactly where they were. The prediction of §1 is confirmed at the strongest available resolution;
no reference artifact needs re-baselining and no snapshot was taken (nothing was superseded).

**Python metric suites: 119 tests, all green** (was 117 with 2 failures). The two red tests:

* `test_oracle_root_metric.test_parse_our_key` — green **by the code**: `parse_our_key("Cweird")` is
  `(0, None)` again because the reduction abstains, exactly as the dispatch required. Its expectation was
  **not** touched.
* `test_metric_primitives_l0l1.test_our_key_tonic_mode_qualified_normalization` — the genuinely stale one:
  `EPhrygDom` now expects the **parent-collection** answer `(9, False)` = A minor (E Phrygian-dominant is the
  dominant of A minor, offset −7). That is the OI-132 ruling, orthogonal to the abstain question.

---

## 6. Declared: three findings the work surfaced

**(a) A THIRD hidden red assertion in the same test — the fold also dropped unicode normalization.**
`test_parse_our_key` asserts `parse_our_key("F♯maj") == (6, "major")`. At HEAD it returned `(None, None)`;
the failure was **masked** because `assertEqual` aborts at the earlier `"Cweird"` line. The pre-fold
`oracle_root_metric.parse_our_key` (`git show 800f1a12bf^`) normalized `♯`/`♭` to ASCII **before** parsing;
the shared reduction only normalized inside the parent-collection branch, so a unicode-accidental TONIC fell
off the graded path entirely. **Fixed in the same one reduction** (`_ascii_accidentals`, applied once, used
by both branches) — the same class of fix as the abstain restoration: a capability the fold dropped, pinned
by a test. **Zero effect on real cells** (no corpus tonic uses a unicode accidental — §3), which the
byte-identical battery confirms.

**(b) OI-157 (new row) — a third copy of the mode classification, in `measure_joint_probe.py`, went stale at
OI-132.** `_MAJOR_MODE_IDX` (`:86`) classifies a key from its `KeySigMode` **enum index**, and its comment
claims it is "derived from `compare_rn._mode_is_major`" and "verified faithful per row against
`crn._our_key_tonic`". Both claims are false at HEAD: `_mode_is_major` no longer exists, and the table still
encodes the superseded same-tonic prefix rule — `PhrygianDominant` (index 18, absent from the set) graded
minor **at its own tonic**, whereas the shared reduction has, since OI-132, reduced the five exotics to a
**different** tonic, which an (index → is_major) table cannot express at all. Not a governing surface (a
read-only probe, not in the battery); it moved no committed figure. **Declared, not fixed** — out of this
dispatch's edit scope, and the probe's outputs are frozen report evidence. Its own faithfulness self-check
(`:307-314`) is the mechanism that would surface this at its next run.

**(c) A latent wrong-tonic path in the OI-152 family (noted on that row's territory, not a new row).** The
producer can spell a tonic with a double sharp (`Fx` / `Cx` / `Gx` — `ALTERED_NAMES` / `ALTERED_DOM_BB7_NAMES`
at extreme sharp signatures). `_KB_OURS_KEY_RE`'s tonic group is `([A-G])([#b]?)`, so `"Fxalt"` parses as
tonic **F** plus a bogus mode `"xalt"` — the wrong tonic. With this fix the mode now abstains (it is not in
the vocabulary) instead of grading minor, but the tonic is still wrong. **It cannot fire today** (no corpus
cell carries such a tonic — §3), and the tonic regex is OI-152's territory (the key-parse abstain family),
so it is recorded there rather than fixed here.

---

## 7. The two deferred rows the dispatch asked for (§6 — filed, not fixed)

* **OI-156 (new row)** — the bridge's 4th hard-coded `0.25` onset literal
  (`src/notation/internal/notationharmonicrhythmbridge.cpp:85`, the null-config fallback), a value-copy of
  `analysis::kDefaultOnsetBoundaryThreshold` (`analysistypes.h:94`) that OI-135(b) made the single source.
  Filed as its own row because **OI-135 is closed**; **gate: the next `src/notation` config-unification
  touch**. Verified at the code before filing.
* **OI-34 (amended)** — the corpus line-ending platform-dependence: the committed corpus is CRLF only because
  regeneration runs on Windows with `QIODevice::Text`, so a Linux regen would move every fingerprint (#16).
  Recorded as a **deferred obligation of the O-12/OI-34 corpus git-tracking decision**, cross-referenced from
  **OI-137(a)**, which established it at the data and deliberately changed nothing.

**Also corrected (doc-sync, #10):** OI-152's row cited `_KB_MAJOR_MODE_PREFIXES` as the anchor for the
church-mode declared choice. That constant is gone; the row now points at `_KB_MINOR_MODES` and the comment
block above it.

---

## 8. Self-check against the standing rules

Read the diff of every touched file against `CLAUDE.md`, the conventions, the gate policy, and
`DEFECT_TYPES.md`.

* **#6 (total unification)** — the change *removes* duplication rather than adding it: one abstain decision
  (`_our_key_ident`) replaces four copies of the same predicate, and one normalization helper
  (`_ascii_accidentals`) replaces the inline `.replace()` chain. The grader's mode table is a mirror of the
  producer's vocabulary, and that mirror is **mechanically checked** against the C++ (not a prose "keep in
  sync" comment — the construction OI-135 was opened to kill).
* **#7 (layers)** — the grader reads the producing layer's published vocabulary; it does not re-decide it.
* **#10 / #11 (doc + test sync)** — the a8 abstain-convention docstring, the reduction docstrings, and the
  OI-152 anchor are updated in the same commit as the code; the tests pin the new rule and the producer link.
* **#13 / #17 (surprise = STOP; prediction before measurement)** — the prediction was written first and held
  exactly; the one surprise found (the hidden third assertion) was surfaced in §6(a), not built around.
* **#16 (reproducibility)** — nothing was re-baselined, because nothing moved; the committed reference and its
  manifest are untouched, and no snapshot was owed.
* **Conventions** — American English; no self-invented labels, abbreviations or numbering (every name used is
  the repository's own: the OI numbers, the DT types, the producer's function names).
* **`src/composing` untouched.** No inference-problem-driven coding: this is a measurement-chain convention
  fix, in `tools/`, at the layer that owns grading.
