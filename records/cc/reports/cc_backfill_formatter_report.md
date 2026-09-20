# CC backfill report — `chord/chordsymbolformatter.cpp` branch backfill (Phase-5 round-2, cluster 3 of 4)

**Commit (local, unpushed):** `45a89f49dfad855e922d57dcf3cd4746ac9b74a6`
`test(composing): chordsymbolformatter branch backfill — oracle tests for unhit formatter arms (Phase-5 round-2 cluster 3)`
**Scope (verify by sha):** `git show --stat 45a89f49df` → **2 files**, test-only —
`src/composing/tests/chordsymbolformatter_branch_tests.cpp` (new, +498) and
`src/composing/tests/CMakeLists.txt` (+1, registration). **No `src/composing/analysis/**` (production) edit.**

---

## §0 — Result headline

| metric | before | after | Δ |
|---|---:|---:|---:|
| `chordsymbolformatter.cpp` UNION branch% (`composing_tests` ∪ `notation_tests`) | **85.51 %** (109 missed / 752) | **95.48 %** (34 missed / 752) | **−75 missed** |
| `chordsymbolformatter.cpp` composing-only branch% | 83.64 % (123 missed) | 94.41 % (42 missed) | −81 missed |
| `composing_tests` total | 778 | **810** (+32 new, 1 new DISABLED) | grows ✓ |
| `notation_tests` | 53 pass / 4 skip | 53 pass / 4 skip | unchanged ✓ |
| `pipeline_snapshot_tests` | 11/11 golden | 11/11 golden | unchanged ✓ |
| BIR gate | 53 / 24 / 53 | 53 / 24 / 53 (by construction — tests-only) | unchanged ✓ |

The **34** residual unhit arm-directions measured after the backfill are **exactly** the set classified
EXCLUDE at source below — the source classification predicted 34, the `llvm-cov` re-measure confirmed 34.
Coverage tool: `tools/coverage/run_branch_coverage.ps1` (UNION, default), outputs in gitignored
`scratch_artifacts/coverage/clang_branch/`. Instrumented `composing_tests` ran **810/810 PASSED**.

---

## §1 — The worklist accounting (109 union-unhit arm-directions)

103 branch tokens / **109 arm-directions** (6 `[TF]` tokens count 2 each). Re-confirmed class at source:

- **75 ADD-TEST** — covered by the new file (incl. `222:22[T]` "Maj#11", hit incidentally by the
  requalification-suppressed test).
- **34 EXCLUDE** — provably-defensive / dead / synthetic-flag / two-same-degree cluster / should-not-occur.
  Not annotated in source (Phase-6 seal); listed in §3.

**Over-count vs the `~98` upper bound:** the `~98` was an upper bound; the faithful at-source count is **75
coverable**. The 23-direction gap (≈98→75) plus the always-excluded should-not-occur/default arms resolve to
the 34 EXCLUDE set in §3. No production change could close any of the 34 without altering behavior (a hard STOP);
none were attempted.

---

## §2 — ADD-TEST coverage (32 test cases, oracle = convention re-derived at source)

Root spelling (`csfPitchClassNameFromTpc`): `Cb`/`Ces` (tpc 7/8 + German), `Fb`/`Fes` (tpc 6/7 + German),
`A#→Bb` normalization (`<5`♯) vs honored `A#` (`≥5`♯) vs German `B`, `G#` honored at +1/+2♯, very-flat
`Cb`/`Fb` (internal tpc 19/18) + German + the non-E/B 6♭ passthrough.

Quality suffix (`csfQualitySuffix`): `sus269`/`sus69`, `Maj7b9`, `addb9`/`add#9`, `mMaj7add13`, `m7#9`,
`madd#9`, `Maj7#5b9` (catalog `C..#5` family), the sus2 dominant ladder `7sus2`/`9sus2`/`11sus2`/`13sus2`,
`Maj7sus` (suspended-quality path), `sus#9`, the ♭5-suppression-on-dim/half-dim rules.

`formatSymbol` tail: `OmitsThird`→`(no 3)` (no-Maj7 path), Maj7sus requalification **suppressed by #11**,
out-of-range bass (`-1`/`12`) → slash omitted (Maj7sus + normal paths).

Roman (`csfDiatonicRoman` / `formatRomanNumeral`): out-of-range degree → `""`, add6 ignored on augmented,
half-dim alterations `iiø7b9`/`#9`/`#11`/`b13`, sus+Maj7 `M`-insert (`IM7sus4`), `(add13)`/`(add#9)`,
sus2/sus4/power inversion figures (`Isus26`/`Isus46`/`I6`), chromatic diminished `biio`, tonicization
suppressed on non-scale target (`bII7`) and on empty base, `viiø7/V` + `viio7/V` leading-tone labels.

Nashville (`formatNashvilleNumber`): the accidental appends `♭5`/`♯5`/`♭9`/`♯9`/`♭13`/`♯13` and the `6/9` tag.

Oracle anchor for the jazz-suffix strings: the project's own ground truth
`src/composing/tests/data/chordanalyzer_catalog_jazz.musicxml` (`kind text="…"`), e.g. `CMaj7#5`, `C13#5`,
`CMaj9#5`, `Cm9b5`, `Cm11b5`, `C7#5b9` — the convention, not the code output.

---

## §3 — EXCLUDE re-classification at source (34 arm-directions — the residual unhit set)

Each is provably non-asserted-faithfully; no production change attempted (would be a STOP).

**(a) Should-not-occur chromatic guard (3) — §1 "skip, Phase-6 seal".** `478:21[F]`, `480:40[T]`, `847:13[T]`.
`csfChromaticRoman` only ever receives a **diatonic parent** mode (all 21 modes map via `CHR_DIATONIC_PARENT`
to SCALES[0..6]). Every diatonic mode has max scale-gap 2, so every chromatic note is exactly one semitone
*below* a degree → the flat loop **always** matches first → the sharp-fallback loop (`478`/`480`) and the
empty `return ""` (`847`) are unreachable through the public API. Provable, not heuristic.

**(b) Bass-name validator reject arms (4).** `717:9[T]` (null), `717:18[T]` (empty), `718:9[T]`
(non-uppercase), `722:13[T]` (>3 chars). `csfIsValidBassNoteName`'s only caller passes a name produced by
`csfPitchClassNameFromTpc`, which always returns a non-null, non-empty, uppercase-led ≤3-char literal — so
these reject paths cannot fire. (The **one** reachable reject — bad accidental, `721:33[T]` — is COVERED; see
§4.)

**(c) Exhaustive-enum `default:` (3) — §1 "skip".** `406:5[T]` (`csfQualitySuffix`), `512:5[T]`
(`csfDiatonicRoman` base), `650:5[T]` (`csfCoreIntervals`). Reachable only via `ChordQuality::Unknown`; `512`
short-circuits the empty-roman early return so `650` is doubly unreachable.

**(d) Two-same-degree extension clusters (11) — no convention oracle.** `222:22[T]` (Maj7 11+#11; note: this
arm is in fact COVERED incidentally by the §4 requalification test, so it is *not* in the residual 34),
`231:22[T]` (dom 13+♭13), `236:22[T]` (dom 11+#11), `239:26[T]` (dom nat9+♭9), `257:22[T]` (add 11+#11),
`279:22[T]` (m 13+♭13), `285:26[T]`/`285:49[T]` (m nat9+♭9 / nat9+#9), `372:43[F]` (sus nat9+♭9),
`390:26[F]` (dead — see (e)). These render a deterministic string only for a **non-standard cluster** (two
alterations of one extension degree); the clean single-alteration form of every named family (`7b9`, `7#9`,
`7#11`, `7b13`, `Maj7b9`, `m7b9`/`m7#9`, `addb9`/`add#9`) **is** covered or already-hit. Asserting the cluster
string would be an echo, not a derivable oracle.

**(e) Provably-dead arms (4).** `251:17[T]`/`252:17[T]` (`else if (hasMin7)` ♭9/#9 appends — any ninth is
caught earlier by `hasMin7 && hasNinth`, so these `if`s are dead), `683:9[T]` (`inversion <= 0` — line 669
already returned when `bass == root`, so `bassInterval != 0` ⇒ `inversion ≥ 1`), `691:13[F]` (triad
`inversion == 2` false — a triad reaching here is always inversion 2), `390:26[F]` (sus #9 `hasNinthSharp`
false — inside an `||` block already gated `flat||sharp` with flat false).

**(f) Synthetic-flag defensive guards (5).** `433:25[F]` (♭5 + #5 simultaneously — mutually exclusive in
`detectExtensions`), `533:105[F]` / `655:33[F]` (DiminishedSeventh flag on a non-Diminished quality — only set
for Diminished), `592:74[F]` (♭5 on a diminished chord carrying a 7th — structurally a half-dim), `438:31[F]`
(empty suffix + non-Major — only Unknown). Reachable only by non-musical flag combinations the analyzer never
emits; the guards are correct defenses.

**(g) Inconsistent pc/tpc enharmonic guards (2).** `187:67[F]` / `189:67[F]` (the `tpc == 20` / `tpc == 19`
false-arms): with a **consistent** (pc, tpc) pair, pc 11 ⇒ tpc ∈ {7,8 (Cb, exits early), 19,20 (B♮)} and pc 4
⇒ {6,7 (Fb), 18,19 (E♮)} — so the second OR operand is always true when evaluated. The false-arm needs an
inconsistent pair (alternate-TPC-encoding guard, §1 "skip").

**(h) Caller-guaranteed-unreachable (3).** `973:13[F]` / `973:28[F]` (`nashvilleDegree`'s own
`degree>=0`/`degree<7` false-arms) — `formatNashvilleNumber` only calls `nashvilleDegree` *inside* an
identical `degree>=0 && degree<7` guard; the out-of-range `"?"` comes from `formatNashvilleNumber`'s own else
(already tested in `nashville_tests.cpp`), never `nashvilleDegree`'s `return "?"`. Plus `488:9[T]`
(`csfDiatonicRoman` `degree < 0`): its two call sites pass `degree ≥ 0` (the `else` branch) or a forced
`degree = 0` (the chromatic-suffix replay), so the negative-degree guard never fires through the public API.

**(i) Lossy-rendering arm — soft flag (1).** `276:26[F]` (`csfQualitySuffix` Minor: a minor-major-7 reaching
here carries an **altered** ninth only, but the branch renders plain `"mMaj7"`, dropping the b9/#9). A correct
oracle would be `"mMaj7b9"` ≠ code's `"mMaj7"`; whether the alteration *should* be shown is a design question
(the Minor path has no altered-9-on-Maj7 handling, unlike the Major path), so this is **flagged for Cowork as
a possible lossy simplification**, not asserted and not xfail'd.

Residual-34 tally (each arm counted once): (a) 3 + (b) 4 + (c) 3 + (d) 8 [`231,236,239,257,279,285:26,285:49,372:43`
— `222:22[T]` is COVERED, not residual] + (e) 5 [`251:17,252:17,683:9,691:13,390:26F`] + (f) 5
[`433:25,533:105,655:33,592:74,438:31`] + (g) 2 + (h) 3 + (i) 1 = **34** — matching the measured residual.

---

## §4 — Surfaced findings (rule 2)

1. **German flat bass names drop the slash (reachable defect, flagged).** `csfIsValidBassNoteName` accepts only
   a leading uppercase letter followed by `#`/`b`. German spelling renders Cb/Fb basses as **"Ces"/"Fes"**,
   whose `'e'`/`'s'` fail the accidental check (`721:33[T]`), so the slash is **dropped**: German `C/Ces`
   renders as `C`, and `CMaj7sus/Ces` as `CMaj7sus`. Pinned as a **labelled enabled regression guard**
   (`RegressionGuard_GermanFlatBass_SlashDropped`) which also covers `740:17[F]` / `776:13[F]` / `721:33[T]`,
   plus a **`DISABLED_GermanFlatBass_ShouldKeepSlash`** documenting the musically-correct `/Ces` oracle. The
   validator's strictness vs German note spelling is a real (minor) defect — **for Cowork to rule on** (fix the
   validator vs accept dropped slashes). Not a production change in this cluster (tests-only).
2. **`mMaj7` drops an altered ninth (§3(i)).** Minor + Maj7 + altered-9-only renders `"mMaj7"`; a `"mMaj7b9"`
   convention would differ. Flagged, not asserted.

No correct-oracle-fails-current-code xfails beyond the single DISABLED bass-slash case above; every enabled
assertion passes against current code.

---

## §5 — Gate confirmation

- Build green (`setup_and_build.bat`); new TU compiled clean.
- `composing_tests` **810/810** (was 778; +32 new, +1 DISABLED) — grows ✓.
- `notation_tests` **53 pass / 4 skip** — unchanged ✓. `pipeline_snapshot_tests` **11/11 golden** (+1
  always-skip) — unchanged ✓.
- Corpus 53/24/53 by construction (no production/scoring code touched) — **no corpus or snapshot run needed or
  performed** (tests-only; CLAUDE.md autonomous-loop applies). No movement possible.
- `upstream` not touched; commit is **local, unpushed** (`45a89f49df`).

Cowork verifies test-only by `git show --stat 45a89f49df` (2 files, `src/composing/tests/` only).
