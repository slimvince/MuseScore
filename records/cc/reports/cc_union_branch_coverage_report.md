# UNION branch coverage — `composing_tests` ∪ `notation_tests` — the true L1–L4 criterion-4 baseline

**Measurement-only. No `src/` edits, no production MSVC/ninja build change, BIR 53/24/53 + snapshot goldens untouched.**

- **Runner-extension commit (build-config only):** `b2de0771fc80330898a7d0838357fab4bbd5c1e0`
  (`tools(coverage): UNION branch coverage (composing_tests + notation_tests)` — 1 file changed,
  `tools/coverage/run_branch_coverage.ps1`, +91 / −37). Cowork can verify build-config-only by
  `git show --stat b2de0771fc` (single file, the runner).
- Scope: `llvm-cov` over `src/composing/analysis`, `--show-branches=count`.
- Toolchain: portable LLVM 22.1.8, MSVC 14.42, Qt 6.10.1 (same as the composing-only spike).
- Method: the **one** clang-cl-instrumented `composing_analysis` lib was relinked (via `lld-link`) into **both**
  `composing_tests` **and** `notation_tests`, each run under instrumentation → two `.profraw`; `llvm-profdata merge`
  combined them → `union.profdata`. No production binary was rebuilt or touched (the runner recompiles only the 3
  `composing_analysis` unity TUs under clang into a separate `scratch_artifacts/` out-dir, never invoking
  `setup_and_build.bat`).
- Artifacts (gitignored `scratch_artifacts/coverage/clang_branch/`): `union_branch_report.txt`,
  `union_branch_export.json`, `union_html/`, plus the per-suite `composing_branch_report.txt`,
  `composing_testrun.log`, `notation_testrun.log`.

---

## §1 — Headline

| Profile | Branch coverage over `src/composing/analysis` | Missed branches |
|---|---|---|
| `composing_tests` only (the spike) | **69.75 %** | 1690 / 5586 |
| **UNION (`composing_tests` ∪ `notation_tests`)** | **82.12 %** | **999 / 5586** |

`notation_tests` newly covers **691** branch directions that `composing_tests` never reaches. The union is the
true whole-corpus criterion-4 baseline across the two existing suites.

**Suite health under instrumentation (both ran clean — coverage is valid):**
- `composing_tests`: **695 / 695 PASSED** (1 pre-existing DISABLED).
- `notation_tests`: **53 PASSED, 0 FAILED, 4 SKIPPED.** The 4 skips are *unconditional* `GTEST_SKIP()` **xfail**
  markers (the parked C→F key regression from `a6b08af3fe`, L3 decoder wiring) — they skip in *every*
  `notation_tests` run, instrumented or not, so the union is the true current baseline, **not** a relink artifact.
  (Caveat for Cowork: two of those xfails — `MozartK279OpeningPrefersCMajorOverFLydian`,
  `PopulateChordTrackEmitsCadenceMarkersOnCorelli` — exercise key/section paths; if/when they un-xfail, the
  `key/`+`section/` numbers below can only rise.)

---

## §2 — UNION per-module branch % (true criterion-4 baseline)

Per file (= module) under `src/composing/analysis`, with the composing-only → union delta. `Br` = total branch
directions, `Miss` = missed (union). Files where `notation_tests` lifted coverage are marked **↑**; files where
it added **nothing** are marked **=** (a triage signal — see §5).

| Module | Br | composing-only % | **UNION %** | Miss (union) | |
|---|---:|---:|---:|---:|:--|
| `chord/analysisutils.h` | 46 | 93.48 | 93.48 | 3 | = |
| `chord/chordanalyzer.cpp` | 734 | 95.64 | **97.82** | 16 | ↑ |
| `chord/chordanalyzer.h` | 52 | 61.54 | **78.85** | 11 | ↑ |
| `chord/chorddiagnose.cpp` | 48 | 81.25 | 81.25 | 9 | = |
| `chord/chordpostpasses.cpp` | 182 | 72.53 | **90.66** | 17 | ↑ |
| `chord/chordslicedecoder.cpp` | 214 | 81.31 | 81.31 | 40 | = |
| `chord/chordsymbolformatter.cpp` | 752 | 83.64 | **85.51** | 109 | ↑ |
| `chord/chordvoicing.cpp` | 116 | 90.52 | 90.52 | 11 | = |
| `chord/postscoringgates.cpp` | 340 | 82.94 | **85.29** | 50 | ↑ |
| `engravingbridge/regiontonecollector.cpp` | 154 | 61.04 | **84.42** | 24 | ↑ |
| `engravingbridge/regiontonecollector.h` | 16 | 25.00 | **62.50** | 6 | ↑ |
| `engravingbridge/regiontoneprimitives.cpp` | 244 | 69.26 | **84.84** | 37 | ↑ |
| `engravingbridge/spellingview.cpp` | 14 | 100.00 | 100.00 | 0 | = |
| `function/harmonicfunctionlayer.cpp` | 216 | 97.22 | 97.22 | 6 | = |
| `function/tonicizationlabeler.cpp` | 54 | 77.78 | 77.78 | 12 | = |
| `harmony/harmonicsegmenter.cpp` | 381 | 55.12 | **83.46** | 63 | ↑ |
| `key/keymodeanalyzer.cpp` | 290 | 87.59 | **89.66** | 30 | ↑ |
| `key/keymodeanalyzer.h` | 20 | 100.00 | 100.00 | 0 | = |
| **`key/keymodeformatting.cpp`** | 88 | **0.00** | **64.77** | 31 | **↑ (0%-file)** |
| `key/keymodesequence.cpp` | 140 | 85.00 | 85.00 | 21 | = |
| `key/keyresolver.cpp` | 131 | 75.57 | **76.34** | 31 | ↑ |
| `notemodel/note_model.cpp` | 78 | 94.87 | **96.15** | 3 | ↑ |
| `region/regionanalyzer.cpp` | 452 | 37.61 | **67.04** | 149 | ↑ |
| `region/sparsechordrefinement.cpp` | 82 | 6.10 | **48.78** | 42 | ↑ |
| `scoreharvest/metricweights.cpp` | 76 | 47.37 | **73.68** | 20 | ↑ |
| `section/cadencekeyanchor.cpp` | 54 | 83.33 | 83.33 | 9 | = |
| `section/jointkeydecision.cpp` | 168 | 69.05 | 69.05 | 52 | = |
| `section/localmodulationdetector.cpp` | 80 | 75.00 | 75.00 | 20 | = |
| **`section/sectionanalyzer.cpp`** | 260 | **0.00** | **41.54** | 152 | **↑ (0%-file)** |
| **`section/sectioncadencedetection.cpp`** | 86 | **0.00** | **72.09** | 24 | **↑ (0%-file)** |
| `slicing/slicer.cpp` | 18 | 94.44 | 94.44 | 1 | = |
| **TOTAL** | **5586** | **69.75** | **82.12** | **999** | |

(Files with `Br = 0` — `chordslicedecoder.h`, `decode/chordpathdecoder.h`, `key/modepriorpresets.cpp`,
`notemodel/note_model.h`, `region/harmonicrhythm.h` — carry no branch instrumentation; omitted from the table.)

---

## §3 — The 0%-files verdict: **HYPOTHESIS CONFIRMED**

All three files that `composing_tests` left at a literal **0 %** lift under `notation_tests` — i.e. they are
**`notation_tests`-driven**, never reached by `composing_tests` at all:

| File | composing-only | **UNION** | Lift |
|---|---:|---:|---:|
| `key/keymodeformatting.cpp` | 0.00 % (88/88 missed) | **64.77 %** (31/88) | +64.77 |
| `section/sectioncadencedetection.cpp` | 0.00 % (86/86) | **72.09 %** (24/86) | +72.09 |
| `section/sectionanalyzer.cpp` | 0.00 % (260/260) | **41.54 %** (152/260) | +41.54 |

Verdict: **confirmed** — the hypothesis that these are notation-suite-driven holds for all three. **But not fully
covered even in the union:** `sectionanalyzer.cpp` reaches only **41.54 %** (152 of 260 directions still unhit) and
remains the single largest unhit cluster in the whole module (see §4).

---

## §4 — Triage signals (the real gap Cowork will triage)

The union still-unhit set is **999** directions (summary) / **1001** export-level arm-directions; the +2 is
`llvm-cov` folded-branch accounting (`harmonicsegmenter.cpp` +1, `keyresolver.cpp` +1). The full file+location list
is in **§5**. Three observations worth surfacing (not triaging — that's Cowork's call):

**(a) Largest residual unhit clusters in the union** (add-test / wire-or-remove candidates):
- `section/sectionanalyzer.cpp` — **152** unhit (41.54 %). Biggest gap by far; even with `notation_tests` < half its
  branches fire. The unhit run is dense and contiguous (lines ~222–569, almost all `[TF]` = *both* arms unhit →
  whole blocks never entered).
- `region/regionanalyzer.cpp` — **149** unhit (67.04 %). Large absolute count; a contiguous `[TF]` block at lines
  ~381–490 (both arms — entire sub-path never entered).
- `chord/chordsymbolformatter.cpp` — **109** unhit (85.51 %) — but on 752 branches (formatting variety; many are
  rare chord-spelling arms).
- `harmony/harmonicsegmenter.cpp` — **63**; `section/jointkeydecision.cpp` — **52**; `chord/postscoringgates.cpp` — **50**;
  `region/sparsechordrefinement.cpp` — **42** (48.78 %, second-lowest %); `engravingbridge/regiontoneprimitives.cpp` — **37**.

**(b) `section/` splits cleanly — a strong wire-vs-test signal.** Within `section/`, two files are notation-driven
and lifted hugely (`sectionanalyzer`, `sectioncadencedetection`), but **three did not move *at all* between
composing-only and union**:
- `section/jointkeydecision.cpp` — **69.05 % → 69.05 %** (52 unhit, unchanged). Per STATUS.md this module is *wired
  but gated OFF* in production (`jointKeyWiringEnabled()` default false, `regionanalyzer.cpp:581`) — so its 52 unhit
  directions are plausibly **unreachable in the current production config**, i.e. a *wire-or-exclude* question, not
  an add-test one. **(flag, not a conclusion — Cowork has the architectural context to decide.)**
- `section/cadencekeyanchor.cpp` — 83.33 % → 83.33 % (9 unhit, unchanged).
- `section/localmodulationdetector.cpp` — 75.00 % → 75.00 % (20 unhit, unchanged).
Neither suite advances these three; whatever covers them today is `composing_tests`, and `notation_tests` adds zero.

**(c) Other files `notation_tests` left exactly unchanged** (composing-only already at ceiling for these suites;
candidates whose residual is *not* a notation-path gap): `analysisutils.h`, `chorddiagnose.cpp`,
`chordslicedecoder.cpp` (40 unhit, no lift), `chordvoicing.cpp`, `harmonicfunctionlayer.cpp`,
`tonicizationlabeler.cpp`, `keymodesequence.cpp` (21 unhit, no lift), `slicer.cpp`.

---

## §5 — UNION still-unhit branch DIRECTIONS (file + location)

`L:C[dir]` = source line:column of the branch, `dir` = which arm never executed (`T` = true-arm, `F` = false-arm,
`TF` = *both* arms — the branch point was never reached). Derived from `union_branch_export.json`.
Total: **1001** unhit arm-directions across 29 files.

```
## chord/analysisutils.h  (3)
   62:5[T] 72:5[T] 75:5[T]

## chord/chordanalyzer.cpp  (16)
   259:63[F] 278:35[F] 327:59[F] 327:71[F] 385:36[T] 430:37[F] 546:36[F] 581:36[F] 857:73[F] 1041:40[F]
   1055:17[F] 1105:35[F] 1112:33[F] 1370:38[F] 1495:5[F] 1496:5[T]

## chord/chordanalyzer.h  (11)
   121:9[T] 167:20[T] 167:45[TF] 182:13[F] 182:26[TF] 937:38[F] 940:32[T] 942:32[F] 1014:12[T]

## chord/chorddiagnose.cpp  (9)
   41:9[T] 117:40[F] 118:17[F] 124:13[F] 137:35[F] 142:17[F] 160:16[F] 161:16[F] 162:16[F]

## chord/chordpostpasses.cpp  (17)
   71:30[T] 74:13[F] 76:5[T] 84:27[F] 87:27[F] 88:27[T] 90:27[T] 91:27[T] 103:32[T] 146:29[F] 175:12[F]
   183:48[F] 187:39[F] 187:58[F] 191:41[F] 192:21[T] 222:29[F]

## chord/chordslicedecoder.cpp  (40)
   96:13[T] 96:15[F] 96:28[F] 96:43[F] 96:64[F] 97:18[F] 150:12[F] 150:12[T] 151:15[T] 163:39[F] 209:63[F]
   212:13[F] 213:26[T] 215:46[F] 216:26[T] 224:30[F] 226:38[F] 238:34[F] 274:26[F] 274:46[F] 334:13[F]
   343:35[F] 468:9[F] 476:9[F] 500:9[T] 500:19[T] 500:35[T] 500:51[T] 509:9[T] 514:26[TF] 518:17[TF]
   519:17[TF] 536:13[F] 536:24[F] 546:13[F] 548:13[F] 551:13[F]

## chord/chordsymbolformatter.cpp  (109)
   108:26[T] 108:38[T] 108:56[TF] 109:38[T] 109:56[T] 134:18[T] 134:30[TF] 136:24[T] 141:44[T] 144:44[T]
   187:54[T] 187:67[F] 188:20[T] 189:41[F] 189:54[T] 189:67[F] 190:20[T] 206:9[T] 207:9[T] 222:22[T]
   227:26[T] 231:22[T] 236:22[T] 239:26[T] 251:17[T] 252:17[T] 257:22[T] 259:22[T] 259:47[T] 272:26[F]
   276:26[F] 279:22[T] 285:26[T] 285:49[T] 288:21[F] 289:21[T] 298:48[T] 330:21[T] 352:13[T] 353:22[TF]
   353:49[TF] 353:74[TF] 366:17[F] 372:43[F] 387:33[T] 389:21[F] 390:26[TF] 406:5[T] 433:25[F] 433:43[F]
   434:19[F] 438:31[F] 478:21[F] 480:40[T] 488:9[T] 488:34[T] 512:5[T] 524:106[F] 533:105[F] 551:13[T]
   552:13[T] 553:13[T] 554:13[T] 568:17[T] 592:74[F] 602:13[T] 610:20[T] 641:5[T] 644:5[T] 647:5[T]
   650:5[T] 655:33[F] 669:9[T] 683:9[T] 691:13[F] 717:9[T] 717:18[T] 718:9[T] 721:33[T] 722:13[T]
   733:76[F] 734:88[F] 738:20[F] 738:51[F] 740:17[F] 774:47[F] 776:13[F] 810:21[F] 836:41[T] 847:13[T]
   909:44[F] 948:35[T] 949:25[T] 951:32[T] 973:13[F] 973:28[F] 1002:13[T] 1003:13[T] 1004:13[T] 1005:13[T]
   1007:13[T] 1008:13[T] 1009:13[T]

## chord/chordvoicing.cpp  (11)
   41:13[F] 65:13[F] 86:75[F] 89:76[F] 117:82[F] 123:12[F] 123:82[F] 187:9[T] 200:13[T] 204:32[T] 212:9[F]

## chord/postscoringgates.cpp  (50)
   66:12[F] 146:28[F] 147:28[F] 149:43[T] 184:65[F] 193:53[F] 195:33[F] 196:36[F] 228:24[F] 230:64[T]
   250:25[T] 318:24[F] 327:37[F] 328:25[F] 337:17[F] 346:21[F] 349:28[T] 358:24[F] 359:24[F] 369:25[T]
   370:28[F] 371:28[TF] 413:25[F] 421:21[F] 423:24[F] 424:24[F] 429:42[T] 431:25[TF] 431:46[TF] 431:67[TF]
   438:24[T] 456:16[F] 457:16[F] 492:16[F] 493:16[F] 501:25[F] 502:28[F] 503:21[T] 529:16[F] 530:16[F]
   537:21[T] 540:33[F] 543:21[T] 562:16[F] 564:17[F] 572:29[T]

## engravingbridge/regiontonecollector.cpp  (24)
   58:9[T] 76:9[T] 88:35[F] 89:19[F] 89:30[F] 121:13[T] 141:45[T] 161:13[T] 171:13[T] 173:13[T] 190:17[T]
   194:17[F] 205:17[T] 208:17[F] 231:17[T] 235:31[F] 239:17[T] 260:17[T] 286:17[T] 286:37[TF] 323:9[F]
   333:17[T] 372:24[F]

## engravingbridge/regiontonecollector.h  (6)
   73:9[T] 77:9[T] 80:9[T] 84:12[F] 93:9[T] 96:9[T]

## engravingbridge/regiontoneprimitives.cpp  (37)
   54:35[F] 55:19[F] 55:30[F] 55:43[F] 135:9[T] 138:9[T] 167:44[T] 173:46[T] 179:25[T] 179:39[T] 232:27[F]
   233:19[F] 296:9[T] 314:44[T] 319:46[T] 322:21[T] 326:25[T] 326:39[T] 354:35[F] 381:9[T] 400:44[T]
   405:46[T] 408:21[T] 412:25[T] 412:39[T] 429:9[T] 485:44[T] 491:44[F] 528:9[T] 528:32[TF] 539:10[F]
   543:44[T] 549:44[F] 585:9[T] 585:32[TF]

## function/harmonicfunctionlayer.cpp  (6)
   108:53[T] 495:33[T] 496:36[T] 519:9[F] 520:12[F] 539:9[F]

## function/tonicizationlabeler.cpp  (12)
   46:9[T] 70:9[T] 79:13[T] 79:29[T] 92:13[T] 123:51[F] 127:20[F] 128:23[TF] 131:17[F] 133:56[T] 155:22[T]

## harmony/harmonicsegmenter.cpp  (64)
   74:5[T] 83:9[T] 85:9[T] 99:9[T] 99:19[T] 109:46[T] 121:21[T] 126:21[T] 126:54[T] 129:36[F] 130:25[T]
   130:39[T] 167:9[T] 167:19[T] 172:9[T] 179:13[T] 184:50[T] 193:21[T] 199:25[T] 199:39[T] 226:13[T]
   231:50[T] 240:21[T] 249:25[T] 249:39[T] 262:21[F] 278:9[F] 287:58[T] 296:29[T] 304:55[F] 345:9[T]
   345:19[T] 345:37[T] 389:13[T] 398:13[F] 409:13[F] 451:13[T] 474:16[F] 476:16[F] 537:13[T] 541:13[T]
   551:16[F] 585:9[T] 603:9[F] 605:44[F] 616:13[T] 620:9[F] 647:35[F] 657:37[F] 679:13[T] 696:9[T]
   730:13[T] 736:13[T] 742:13[T] 811:13[F] 815:17[F] 819:17[F] 819:39[F] 850:45[F] 894:41[F] 907:17[F]
   911:17[F] 911:39[F] 940:13[F]

## key/keymodeanalyzer.cpp  (30)
   156:9[T] 183:5[T] 256:25[F] 257:18[F] 347:9[F] 354:12[TF] 405:5[T] 463:44[F] 467:44[F] 467:57[T]
   476:44[F] 479:44[F] 479:57[F] 482:9[F] 485:22[T] 507:9[F] 526:43[TF] 613:9[F] 645:9[F] 681:39[F]
   682:42[F] 684:42[F] 685:47[F] 686:50[F] 738:32[F] 762:9[F] 764:38[F] 841:18[F]

## key/keymodeformatting.cpp  (31)   [0%-file -> 64.77%]
   79:13[F] 82:5[T] 83:5[T] 87:5[T] 89:5[T] 90:5[T] 91:5[T] 92:5[T] 93:5[T] 94:5[T] 95:5[T] 98:5[T]
   100:5[T] 102:5[T] 103:5[T] 110:13[F] 113:5[T] 114:5[T] 115:5[T] 118:5[T] 120:5[T] 121:5[T] 122:5[T]
   123:5[T] 124:5[T] 125:5[T] 126:5[T] 129:5[T] 131:5[T] 133:5[T] 134:5[T]

## key/keymodesequence.cpp  (21)
   146:13[F] 149:13[T] 179:29[F] 206:13[T] 206:22[T] 210:13[T] 222:33[T] 252:19[T] 291:17[F] 308:9[F]
   313:26[T] 317:33[TF] 318:25[TF] 357:23[F] 366:43[T] 378:37[F] 378:63[F] 380:51[T] 389:28[T]

## key/keyresolver.cpp  (32)
   117:21[T] 122:9[T] 122:32[T] 134:9[T] 134:24[T] 143:9[T] 152:13[T] 156:44[T] 161:46[T] 167:25[T]
   167:39[T] 186:45[F] 198:9[F] 198:9[F] 198:32[F] 227:9[T] 229:9[T] 230:9[T] 231:9[T] 232:9[T] 233:9[T]
   234:9[T] 308:12[F] 330:13[T] 341:35[F] 344:13[F] 349:24[F] 351:17[T] 351:29[TF] 352:32[TF]

## notemodel/note_model.cpp  (3)
   82:9[T] 134:9[T] 177:25[T]

## region/regionanalyzer.cpp  (149)
   75:64[F] 76:9[F] 78:13[F] 130:17[T] 154:21[T] 163:29[F] 204:21[F] 267:13[T] 270:13[T] 273:41[F]
   274:13[T] 275:13[T] 284:13[F] 311:13[T] 323:13[T] 340:67[TF] 342:14[TF] 343:56[TF] 344:21[TF] 344:26[TF]
   381:9[TF] 381:28[TF] 395:9[TF] 395:40[TF] 399:13[TF] 399:37[TF] 401:20[TF] 401:44[TF] 413:35[TF]
   417:13[TF] 418:19[TF] 423:24[TF] 426:28[TF] 431:13[TF] 433:17[TF] 433:17[TF] 433:52[TF] 439:13[TF]
   440:29[TF] 445:29[TF] 452:13[TF] 455:30[TF] 460:33[TF] 460:61[TF] 468:9[TF] 473:24[TF] 478:13[TF]
   485:33[TF] 489:46[TF] 490:17[TF] 490:58[TF] 516:9[T] 516:19[T] 522:9[T] 544:25[F] 545:13[F] 545:41[F]
   612:32[F] 612:53[F] 624:79[F] 628:17[T] 633:22[F] 638:13[F] 638:30[F] 646:21[T] 659:21[F] 685:13[T]
   685:34[T] 707:17[T] 711:17[T] 718:13[T] 725:54[T] 772:17[F] 776:13[T] 810:27[F] 830:32[F] 834:54[F]
   848:17[F] 862:18[F] 868:45[F] 876:17[T] 887:28[T] 896:17[F] 911:37[T] 913:37[F] 919:31[F] 954:9[T]
   954:28[TF] 960:78[F] 1027:21[T] 1041:36[F] 1045:53[F] 1052:43[F] 1076:44[F] 1110:29[T] 1117:21[F]
   1126:41[T] 1128:41[F] 1158:78[F] 1163:31[F] 1231:25[T] 1243:40[F] 1247:57[F] 1254:47[F] 1272:48[F]
   1307:33[T] 1314:25[F] 1323:45[T] 1325:45[F] 1348:9[T] 1369:9[T] 1391:13[F]

## region/sparsechordrefinement.cpp  (42)
   37:9[T] 37:23[T] 58:31[F] 61:9[F] 61:31[F] 74:27[TF] 76:13[TF] 82:13[TF] 82:30[TF] 82:59[TF] 95:13[T]
   125:9[F] 132:9[TF] 132:23[TF] 134:13[TF] 145:9[TF] 154:9[TF] 155:12[TF] 156:12[TF] 157:13[TF] 157:28[TF]
   161:9[TF] 195:9[T] 207:9[TF] 213:9[TF]

## scoreharvest/metricweights.cpp  (20)
   43:13[F] 45:5[T] 60:9[T] 60:21[T] 66:9[T] 66:27[T] 79:5[T] 89:9[T] 93:9[T] 98:9[T] 98:21[T] 142:13[T]
   147:13[T] 152:13[T] 152:61[T] 158:13[T] 163:13[T] 163:42[T] 163:75[T] 173:17[F]

## section/cadencekeyanchor.cpp  (9)
   51:13[T] 180:13[T] 180:13[T] 180:44[TF] 188:9[F] 195:13[T] 195:35[T] 203:25[F]

## section/jointkeydecision.cpp  (52)   [wired but gated OFF in production — likely unreachable; Cowork to confirm]
   56:12[F] 62:9[TF] 128:40[F] 139:12[T] 139:18[TF] 139:31[TF] 139:44[TF] 139:57[TF] 139:70[TF] 224:17[F]
   224:56[F] 241:47[T] 242:17[TF] 242:57[TF] 250:16[F] 255:17[F] 255:48[F] 256:60[F] 262:13[F] 266:13[T]
   267:18[TF] 267:49[TF] 268:21[TF] 268:52[TF] 269:16[TF] 279:30[TF] 280:17[TF] 294:44[T] 295:48[T]
   297:44[T] 311:30[T] 379:34[F] 381:17[F] 381:57[F] 382:20[F] 382:61[F] 388:13[T]

## section/localmodulationdetector.cpp  (20)
   83:9[T] 105:29[T] 139:41[T] 140:41[T] 140:73[TF] 141:41[T] 141:73[TF] 142:24[TF] 142:40[TF] 169:29[F]
   170:52[F] 181:39[F] 184:45[T] 190:53[F] 199:37[F] 201:40[F]

## section/sectionanalyzer.cpp  (152)   [0%-file -> 41.54%; largest residual cluster]
   71:13[T] 84:9[T] 94:9[F] 131:13[F] 178:9[T] 178:16[T] 190:9[T] 222:13[TF] 223:16[TF] 228:13[TF]
   228:33[TF] 234:31[TF] 236:17[TF] 241:17[TF] 242:20[TF] 246:17[TF] 266:13[TF] 267:35[TF] 270:35[TF]
   271:25[TF] 276:21[TF] 290:13[TF] 292:35[TF] 293:21[TF] 302:31[TF] 304:17[TF] 310:13[TF] 317:13[TF]
   333:34[TF] 340:29[TF] 341:21[TF] 346:21[TF] 348:28[TF] 350:28[TF] 352:28[TF] 360:17[TF] 366:17[TF]
   369:24[TF] 372:24[TF] 375:24[TF] 382:17[TF] 382:35[TF] 387:13[TF] 416:13[TF] 428:13[TF] 430:17[TF]
   437:13[TF] 450:13[T] 458:13[F] 459:51[F] 460:17[T] 483:31[TF] 485:17[TF] 492:13[TF] 500:21[TF]
   503:21[TF] 505:25[TF] 512:17[TF] 512:31[TF] 516:17[TF] 516:35[TF] 521:13[TF] 522:22[TF] 530:13[TF]
   531:22[TF] 539:13[TF] 539:31[TF] 543:13[TF] 543:27[TF] 547:13[TF] 547:32[TF] 556:13[TF] 556:31[TF]
   569:13[TF] 603:17[T] 607:20[F] 622:13[T] 623:22[TF] 630:38[TF] 649:21[T] 649:47[TF] 658:33[F] 665:21[F]
   670:17[T] 688:22[F] 697:16[F]

## section/sectioncadencedetection.cpp  (24)   [0%-file -> 72.09%]
   64:9[T] 64:23[T] 73:41[F] 75:16[T] 85:16[T] 90:13[T] 98:44[F] 99:47[F] 101:46[F] 103:46[F] 104:23[F]
   105:23[F] 148:9[T] 148:28[T] 171:13[T] 180:52[T] 199:17[F] 200:20[F] 201:20[F] 219:37[F] 223:17[T]
   226:17[T] 242:17[F] 242:38[F]

## slicing/slicer.cpp  (1)
   95:9[T]
```

---

## §6 — Gate / scope confirmation — measurement-only, stop-conditions clear

- **Production MSVC build + BIR 53/24/53 + snapshots: UNTOUCHED.** The runner never invokes `setup_and_build.bat`
  or the production ninja build; it recompiles only the 3 `composing_analysis` unity TUs under clang into
  `scratch_artifacts/coverage/clang_branch/` and relinks copies (`*_cov.exe`) there. No production binary, gate, or
  golden was rebuilt, run, or written.
- **No `src/` edits.** The only tracked change is the build-config runner (`tools/coverage/run_branch_coverage.ps1`,
  commit `b2de0771fc`). No test changes — the existing `composing_tests` + `notation_tests` binaries were used.
- **Stop-conditions: none triggered.** `notation_tests` relinked (`lld-link`) and ran on the cheap path **without
  any `src/` edit or Qt-under-clang rebuild** — the §5 STOP condition did not arise. No `upstream` push.
- **Out-of-scope working-tree note:** `cowork_l1l3_stabilization_plan.md` is modified in the tree (Cowork's own
  Phase-5b/6 edit — adds the "criterion-4 completion" sealing phase this measurement feeds). CC did **not** touch it
  and it is **not** in commit `b2de0771fc`.

## Reproduction

```
pwsh -File tools\coverage\run_branch_coverage.ps1                 # UNION (default)
pwsh -File tools\coverage\run_branch_coverage.ps1 -ComposingOnly  # original single-suite report
```
Outputs land in `scratch_artifacts/coverage/clang_branch/` (`union_branch_report.txt`, `union_branch_export.json`,
`union_html/`, `composing_branch_report.txt`).
