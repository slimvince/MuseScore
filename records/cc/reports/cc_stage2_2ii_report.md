# CC Stage 2.2-ii — Ship the decided re-baseline package — report

*Run date 2026-06-11. HEAD at run start: `e20894c75b` (Stage 2.2a). All work is in the
working tree; **no commits made** — the 4 commits below are PROPOSED, to be committed only
after Cowork confirms the set (per the instruction). Everything in §"Verification" was run
against the built working tree.*

Sources: `cc_stage2_2_ab_dossier.md` (the 2.2-i A/B + decision menu §6), `docs/implementation_roadmap.md`
rows 2.2 / 2.4 / 5.2, Stage-1d `tools/tests/test_metric_scripts.py`.

---

## 1. Per-commit summary (proposed; 4 commits, in order)

| # | Title | Files | What |
|---|---|---|---|
| **C1** | `tools: add --section-level diagnostic flag to batch_analyze (Stage 2.2-ii)` | `tools/batch_analyze.cpp` (+72/−2) | The prototype from 2.2-i, already in the working tree. Default OFF; only affects `--dump-regions batch`. Feeds batch's preset region stream into `analysis::analyzeSection` and rebuilds `.ours.json` from `section.regions`. Help text + signature `bool sectionLevel=false`. |
| **C2** | `tools: metric corrections — letter-o diminished, It6 routing; analyze_inversion_errors --corpus-dir (Stage 2.2-ii)` | `tools/compare_rn.py` (+19/−2), `tools/analyze_inversion_errors.py` (+41/−6), `tools/tests/test_metric_scripts.py` (+63/−18) | F-1, F-2, Rider 1, and the deliberate test re-pins (below). |
| **C3** | `refactor: remove dead weight/pitch-context shims from notation bridge helpers (Stage 2.2-ii rider)` | `notationcomposingbridgehelpers.h` (−28), `.cpp` (+4/−50) | Rider 2. Removes 6 zero-caller `mu::notation::internal` pass-throughs + the now-dead `shv` alias and `metricweights.h` include. Behavior byte-identical (build + all suites green; see §5). |
| **C4** | `docs: gate-granularity note (CLAUDE.md) + BUILD_AND_TEST sync (Stage 2.2-ii)` | `CLAUDE.md` (+16/−3), `build_and_test.md` | The one gate-granularity sentence + `--section-level` and `analyze_inversion_errors --corpus-dir` documentation; corrected the now-stale "analyze_inversion `--corpus-dir` deferred / bassIsRoot 27/22" parenthetical to the verified 24/13 & 35/7. |

C2 bundles F-1/F-2/Rider 1 + tests in one commit per the instruction; C3 is its own byte-identical commit.

---

## 2. The It6 treatment chosen (and why)

**Chosen: the safe unparseable→root-only fallback (NO invented root mapping).**

`It6` (Italian augmented sixth) is the *only* augmented-sixth/Neapolitan token whose leading
letter the degree regex accepts: `Ger`/`Fr`/`N` already fail `_DEGREE_RE` and return `None`,
but `It6` matched degree `I` and was mis-read as a major tonic (`extract_quality("It6") → "Maj"`).

Treatment: add `_IT6_RE = ^It(?:\d|/|$)` and make `split_rn` return `None` for it (covers `It`,
`It6`, `It6/ii`). This routes It6 through the **same** unparseable branch in `classify_pair`
(lines 231–248) as Ger/Fr/N — root-only: same root → `partial`, different root → `root_err`.

- **No root mapping is invented.** The DCML-side `root_pc` is owned by `dcml_parser._compute_root_pc`
  and is unchanged by this fix; I only stop the *quality-level* misparse. This is the "decided safe
  choice" the instruction names (dossier §4 / §6: "fix the It6→Maj misparse; leave Ger/Fr/N as
  unparseable-fallback"). I did **not** establish a principled DCML root mapping because none was
  needed — the fallback is correct and theory-free.
- **Scope note (honest):** on the *real* corpus `dcml_parser` still resolves It6's root to the tonic
  (degree `I`), whereas Ger/Fr/N get `root_pc=None` and are dropped entirely. So at the `dcml_parser`
  layer It6 is not byte-for-byte identical to Ger/Fr/N. Making it identical would require nulling
  It6's root in `dcml_parser` — a separate change, out of this package's scope (and it would NOT
  change `extract_quality`, which the test re-pin requires). The compare_rn-level fix is exactly what
  the test and dossier ask for; the residual is documented here, not silently absorbed.
- **Bach impact: nil** — only 2 It6 tokens in the Bach WiR (2/10118); 0 Ger65/N6. Cross-corpus value
  (It6=277, dossier §4). Bach gate unchanged (§4).

---

## 3. Re-pinned / added tests (`tools/tests/test_metric_scripts.py`)

All re-pins carry the comment `# re-pinned 2026-06-10: intentional metric correction (Stage 2.2-ii; dossier §4)`.
**Deviation:** the instruction wrote the comment with `//`; these are Python files, so I used `#`
with the same wording.

| test | change |
|---|---|
| `test_letter_o_diminished_is_NOT_recognised` → **renamed** `test_letter_o_diminished_is_recognised` | re-pinned: `viio6→Dim`, `viio7→Dim7`, `iio65→Dim7` (was `Min`/`Min7`/`Min7`). Covers both the **viio6** triad shape and the **iio65** seventh shape. |
| `test_degree_sign_diminished_would_be_recognised` → **renamed** `test_degree_sign_diminished_still_recognised` | the **°-sigil case kept**: `vii°7→Dim7`, `vii°→Dim` still pinned (guards the `°` branch against the new `o` branch). |
| `test_augmented_sixth_and_neapolitan_unparseable` | re-pinned: `It6→"?"` (was `"Maj"`); added `It→"?"`, `It6/ii→"?"`; `Ger65`/`N6→"?"` unchanged. |
| **NEW** `test_split_rn_routes_it6_to_unparseable` | `split_rn("It6"/"It"/"It6/ii")→None`; genuine tonics `I`/`I6`/`i` unaffected. |
| **NEW** `test_it6_routes_to_root_only_fallback` | `classify_pair` with It6: same root→`partial`, diff root→`root_err` (parallels the existing Ger65 fallback test). |

Full Python suite: **65 tests, OK** (63 prior + 2 new). `python -m unittest discover -s tools/tests`.

---

## 4. Verification gate

| check | required | result |
|---|---|---|
| Build | clean | ✅ clean, no warnings (incremental: only `notation` + `batch_analyze` relinked; composing untouched) |
| composing_tests | 498 | ✅ **498/498** |
| notation_tests | 52 | ✅ **52/52** |
| pipeline_snapshot_tests | 11/11 zero diffs | ✅ **11 passed**, 1 SKIPPED (`GenerateReport`, the non-golden report generator) |
| Python metric suite | green | ✅ **65/65** (2 deliberate re-pins + 2 new tests; §3) |
| Baroque `characterise_bir_false --corpus-dir` | 13 | ✅ **13** (`Corpus OK: preset=Baroque 353/353`) |
| Jazz `characterise_bir_false --corpus-dir` | 7 + exact identities | ✅ **7**, identity set EXACT: `{bwv244.15, bwv245.17, bwv245.40, bwv422, bwv432, bwv45.7, bwv74.8}` |
| Baroque `analyze_inversion_errors --corpus-dir` | 24/13 | ✅ **24/13** (three-way genuine 37 = 24 BIR=true + 13 BIR=false) |
| Jazz `analyze_inversion_errors --corpus-dir` | 35/7 | ✅ **35/7** (three-way genuine 42 = 35 + 7) |
| Flag-off byte-identity (3 scores vs committed corpus) | holds | ✅ `bwv244.15`, `bwv102.7`, `corelli` all **byte-identical** (direct-CLI flag-off `diff`-clean vs the regenerated committed `tools/corpus/baroque/*.ours.json`) |
| Flag-on smoke (1 score) | sane, no crash | ✅ `corelli --section-level`: exit 0, valid JSON, 49 regions (vs 43 flag-off), region0 = `F Major [0,960)`; output differs from flag-off (flag is live) |

**Gate-neutrality corroboration:** the flag-off Baroque regen reproduced **11267 aligned regions**
— the exact dossier §3.2 OFF baseline — and 90.8% chord-identity agree. Corpus manifests written
complete (353/353) for both presets at git `e20894c75b`.

**Baroque BIR=false 13 identity set** (recorded for future gate-diffing; not previously enumerated in
the docs): `bwv102.7@17520, bwv14.5@8160, bwv17.7@46080, bwv174.5@6240, bwv245.17@4800,
bwv245.40@51360, bwv261@33840, bwv269@20640, bwv301@960, bwv381@4800, bwv422@23040, bwv432@5520,
bwv45.7@20160`. All are known historical residuals (Δ=+7a bwv102.7/261, the bwv245.x set, bwv301/269/422/432).
No new or shifted case → gate-neutral.

**F-1/F-2 measured impact on the Bach gate: zero** — both presets reproduce identical gate numbers
and identity sets with the fixes live, confirming the dossier's "Bach-gate-neutral" prediction
(F-1 latent/inert on Bach; F-2 only 2 It6 tokens).

---

## 5. Rider 2 — shim-removal sweep evidence

Full-repo qualified-caller sweep over all `.{h,cpp,hpp,cc}` for the 6 symbols
(`beatTypeToWeight`, `safeBeatType`, `regionMetricWeightForBeatType`, `timeDecay`,
`distinctPitchClasses`, `collectPitchContext`):

- **Live callers are all the composing-module versions** (`shv::*` in `metricweights`, `ebr::collectPitchContext`):
  `regiontonecollector.cpp`, `regionanalyzer.cpp`, `keyresolver.cpp`. Those definitions are **untouched**.
- **`mu::notation::internal` versions had 0 callers.** Content sweep restricted to `src/notation`
  found the 6 names ONLY in `notationcomposingbridgehelpers.{h,cpp}` themselves (the decl + the
  pass-through body). The 4 bridge TUs (`notationcomposingbridge.cpp`,
  `notationharmonicrhythmbridge.cpp`, `notationimplodebridge.cpp`, `notationanalysisinternal.h`) and
  all notation tests `#include` the header but **call none of the 6**.
- Removed: the 6 decls (header) + their definitions (cpp) + the now-dead `namespace shv` alias and
  the `metricweights.h` include (their only users were the removed functions). The comment block was
  trimmed to drop `collectPitchContext` from the "separate entry points" list.
- **Byte-identical claim verified empirically:** build clean, composing 498 / notation 52 / snapshots
  11/11, and the flag-off corpus byte-identity (§4) — none of which would hold if a live caller had
  been cut.

---

## 6. Deviations / unknowns (honest)

1. **Comment sigil:** re-pin comments use `#` not `//` (Python). Same wording, intentional language fix.
2. **It6 dcml_parser residual** (§2): the fix is at the compare_rn layer (where the test and dossier
   scope it). The DCML-side It6 root remains `dcml_parser`'s tonic, so on the real corpus It6 is
   root-only-scored rather than dropped like Ger/Fr/N. Documented, not absorbed; nulling it in
   `dcml_parser` is a possible future tightening (out of this package's scope; would not change
   `extract_quality`).
3. **CLAUDE.md / BUILD_AND_TEST stale-number correction:** Rider 1 made the "analyze_inversion
   `--corpus-dir` deferred" and "bassIsRoot 27/22" notes false. I corrected them to the verified
   24/13 & 35/7 (dossier §1 explicitly flags the old wording as imprecise). Also corrected the
   `reference_bir_metric_scripts` memory + its MEMORY.md index line, which had asserted the opposite
   ("analyze_inversion_errors does NOT yield 24/13"). STATUS.md provenance wording is Cowork's — left
   untouched.
4. **Baroque-13 identity set** is not pinned anywhere in the docs (only Jazz-7 is). I recorded it in
   §4 so a future regression can be diffed against it; the count + known-case composition is the
   evidence of gate-neutrality.
5. **Default flat `tools/corpus`** path in `analyze_inversion_errors.py` is preserved unvalidated for
   back-compat (no manifest there). `--corpus-dir` validates; `--ours-dir` warns + reads music21 from
   the same dir (the `:93` fix) but does NOT validate, by design.
6. **No commits made** — awaiting Cowork confirmation of the 4-commit set.

---

## 7. Stop-condition check

None tripped: no gate number or identity-set moved (measured gate-neutral); no caller found in the
shim sweep; snapshots zero-diff; the It6 treatment is the decided fallback (no new theory).
