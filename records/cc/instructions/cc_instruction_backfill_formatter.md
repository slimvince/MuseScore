# CC Instruction — Phase 5 backfill round 2, cluster 3 of 4: chordsymbolformatter (~98 upper-bound, oracle-asserted)

> **Why.** Cluster 3 of the stable-half branch backfill. Same rules as clusters 1–2 (`3f2e4bebe2`, `1218ad1003`):
> **coverage is the gap-finder, NOT the goal**; each test asserts the **exact rendered string the chord-symbol /
> Roman-numeral / Nashville convention requires (the oracle), re-derived at source** — never an echo. A correct oracle
> that **fails** current code → `DISABLED_`/xfail + flag (surfaced defect). **Tests-only — no production change.**
> The `~98` is an **upper bound** (re-confirm class at source; skip provably-unreachable defensive + the placeholders).
> *(This file is a `.cpp` in `composing_analysis`, so — unlike cluster 2's header-inline functions — its branches are
> credited normally by the coverage runner.)*

## §1 — The worklist (`chord/chordsymbolformatter.cpp`, ~98)
- **Exact unhit locations:** grep `cc_union_branch_coverage_report.md` (§5) for `chordsymbolformatter.cpp`.
- **Re-confirm class at source:** ADD-TEST (a reachable rendering path → assert the exact string) vs EXCLUDE-DEFENSIVE
  (exhaustive-enum `default:`, alternate-TPC-encoding guards, the `>1-semitone-from-every-degree` "should-not-occur"
  chromatic guard → **skip**, Phase-6 seal). 
- **★ Two known PLACEHOLDERS — pin as LABELLED regression-guards, NOT oracles:** `formatNashvilleNumber`'s
  out-of-range degree → `"?"` and the crude `(bassDegree % 7)+1` slash-bass. Assert current output but **label the test
  a regression-guard** (the correct Nashville chromatic spelling is future work) — do not claim it as a theory oracle.
- Oracle themes (the **starting point** — derive the exact string at source / from convention):
  - **Pitch-class spelling:** `Cb`/`Fb` (+ German `Ces`/`Fes`) flat-range spellings; `A#→Bb` normalization by key sig;
    the key-sig TPC-honoring `G#`/`Ab` split; ≤−5/−6-flat enharmonic spellings.
  - **Quality suffix:** `m69`/`sus269`; `Maj#11`/`Maj7b9`; dom `b13`/`#11`/`b9`/`#9`, `7b9`/`7#9`; `add#11`/`addb9`/
    `add#9`; `mMaj7add13`/`mMaj7`/`mb13`/`mb9`/`m#9`/`m7#9`/`madd#9`; aug `Maj7#5b9`; the sus2 13/11/9/7 ladder; sus4
    alterations; the b5-suppression rules (suppressed when #5 present / on dim / on half-dim).
  - **Roman numeral:** out-of-range degree → `""`; `add6` vs `69`; half-dim alterations (`iiø7b9`…); sus+Maj7 `M`-insert;
    `(add13)`/`(addb9)`; the `#iv` chromatic sharp-fallback; `I64` second-inversion + root-position/inv≤0 unchanged.
  - **Core intervals:** sus2 `{0,2,7}`, sus4 `{0,5,7}`, power `{0,7}` (the inversion-figuring inputs).
  - **Bass-name validator:** reject null / non-uppercase / bad-accidental / >3-char → slash omitted.
  - **formatSymbol / formatRomanNumeral tail:** Maj7sus requalification true/false; slash-bass omitted on
    invalid/out-of-range bass; tonicization `vii°7/x` & `viiø7/x` glyphs; chromatic-degree-not-in-scale → tonicization
    suppressed.
  - **Nashville:** the accidental appends (`♭5`/`♯5`/`♭9`/`♯9`/`#11`/`♭13`/`♯13`) are real ADD-TEST oracles; the `"?"`
    out-of-range + crude slash-bass are the labelled placeholders above.

## §2 — Write the tests + §3 gate + §4 scope — IDENTICAL to clusters 1–2
- New `chordsymbolformatter_branch_tests.cpp` (or extend an existing formatter test), registered in
  `tests/CMakeLists.txt`. Oracle = the exact string from convention, never echoed (except the two labelled placeholders).
- A failing correct-oracle → `DISABLED_`/xfail + expected-vs-actual (rule 2). Do not weaken.
- **Gate:** new tests pass (bar xfails); `composing_tests` grows; `notation_tests` + snapshots **unchanged**; corpus
  53/24/53 by construction; build green. **Any corpus/snapshot movement → STOP.**
- **Re-measure:** clang branch-coverage scoped to `chordsymbolformatter.cpp` → branch% before→after.
- **Tests-only.** A gap closable only by changing production → STOP, flag. Skip defensive + the placeholders' "correct"
  behaviour. Do not annotate exclusions (Phase-6). `upstream` never; local commit.

## §5 — Deliver
Commit **locally (unpushed)**: the new test file + CMake. Write `cc_backfill_formatter_report.md` (gitignored): tests
added, the branches re-classified defensive/placeholder at source (+ the over-count count), any surfaced defects
(xfails), `chordsymbolformatter.cpp` branch% before→after, and the commit sha — so Cowork verifies by sha that only test
files + CMake changed.
