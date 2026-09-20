# Measurement-Pipeline Integrity Audit — source → verdict, all corpora

*CC, 2026-06-13. Base `a4ae4a9203`+ (working tree carries docs + the read-only key-candidate
diagnostic; no behavior change). This run is **READ-ONLY analysis + targeted probes — NO fixes**,
per the mandate. Every fix is deferred to the single coordinated re-baseline scoped in §4. All
drivers are throwaway `/tmp/*.py` reusing the committed metric machinery verbatim
(`dcml_parser`, `compare_analyses`, `compare_rn`, `characterise_bir_false`) plus music21 9.9.1's
`roman.RomanNumeral` as a true-root oracle. This file is the only repo write.*

Evidence tags: **[code: f:line]** (quoted source), **[probe: cmd→result]** (ran a script),
**[trace: case]** (hand-read a specific case end-to-end), **[inference]** (deduced, flagged as such).
Rates are sampled-tagged with N. Six parallel sub-agents executed the stage×corpus sweep; every
load-bearing claim below was spot-verified by the parent against source or a re-run.

---

## §0 — TL;DR: the error-source ledger, ranked by blast radius

The audit found **one corpus-wide measurement bug that dwarfs the two known parser bugs**, three
more parser/ingestion defects, a fourth structural-alignment defect, and a reporting-staleness
gap. The headline precision numbers rest on a chain that is materially corrupted — but **the
project's primary BIR 13/7 gate is structurally insulated and remains trustworthy** (it is just
~half legitimate ambiguity, not error).

| # | Finding | Stage | Corpus scope | Blast radius (measured) |
|---|---|---|---|---|
| **🔴 P0** | **Fractional-onset DROP** — `float("1/2")` raises ValueError → bare `except: continue`; **58.9% of all TSV annotations silently discarded** (60 676/103 085); only measure-downbeats survive | S3 | all 10 TSV corpora | The *entire* cross-corpus DCML metric. per-DCML headline **54.4%→46.7% (inflated +7.7pp)**; per-ours **49.3%→59.2% (deflated −9.9pp)**; GT volume scored **×2.40** (37.6k→90.4k) [probe] |
| **🟠 P1** | **rntxt applied-chord `/X` drop** (`primary=numeral.split('/')[0]`) roots applied chords in the local key | S3 | Bach (rntxt) | 877/880 applied rntxt rows mis-rooted (0.3% oracle agreement). Inflates the "functional residual" (the dossier's 366 phantom roots). Gate-excluded (§3.A) [probe] |
| **🟠 P2** | **Minor-key leading-tone / submediant** — natural-minor degree table roots `viio` at +10 (true +11), `vio` at +8 (true +9); also fires inside tonicized keys (`#viio/X`) | S3 | both paths | rntxt 434 + TSV 603 (+~318 applied-disguised) + ~29 `vio`. Poisons TSV root_agree by *removing* correct comparisons (the corrupt rows are also the dropped fractional rows) [probe] |
| **🟠 P3** | **Declared-MODE drop at MusicXML import** (`addKey:5978` default-key-match dedup) → resolver `declaredMode=UNKNOWN` for empty-signature pieces | S2 | Bach (.xml import); native path reaches the same UNKNOWN state via a different mechanism | The *key* metric (`key_disagree` S2), ambiguous subset only. **Does NOT corrupt the root gate** — pitch detection recovers clear pieces (bwv245.17 empty-sig+minor → emits Amin) [code][probe] |
| **🟡 P4** | **ABC/Beethoven structural measure-numbering / repeat offset** — GT `quarterbeats` runs ~4 bars ahead of our written-timeline ticks on repeat-bearing movements | S4/S2 | beethoven (ABC) subset | A *fourth* defect, distinct from P0. The naive `quarterbeats` correction makes beethoven **worse** (+3.6pp root_err); needs downbeat-anchoring, not raw qb [trace] |
| **🟡 P5** | **Stale headline + accidental-measurement defaults** — STATUS/MEMORY's "current" 53.8% cross-corpus baseline is 86 commits old; a current regen (54.4%) sits un-cited; `rerun_dcml_comparison.py` defaults to even-older dirs | S6/S1 | reporting | A reader/operator measures a 24-day-old, ~5pp-low number unless they override defaults [probe] |

**The decisive reframe:** the cross-corpus precision picture is computed on **downbeat-only ground
truth** and is **wrong by 7.7–9.9pp** (direction depends on the anchoring), with **59% of the
ground truth never scored at all**. By contrast the **Baroque-13 / Jazz-7 gate is clean** of all
of these — its only weakness is that ~46% of it is legitimate musical ambiguity, not analyzer
error (§3.A).

---

## §1 — The stage × corpus matrix

Verdict per cell: **CLEAN** (audited, no defect) · **SUSPECTED** (mechanism present, impact
bounded/unquantified) · **BUG** (confirmed defect, with finding-id). Stages: S1 source · S2
ours-ingestion · S3 GT-parse · S4 alignment · S5 compare/classify · S6 aggregate/report.

| Corpus (path / GT / ingestion) | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| **Bach chorales** — gate, 353; WiR rntxt; music21→.xml→MusicXML import | CLEAN | **BUG P3** (mode-drop, 80 empty-sig stems; key-only impact) | **BUG P1** (applied) **+P2** (minor-LT/vio) | SUSPECTED (D2 pickup-collision on the measure-anchor path; not gate-visible) | CLEAN (It6 refuted) | CLEAN (gate insulated, §3.A) |
| **corelli, mozart, chopin, beethoven(ABC), grieg, schumann, dvorak, tchaikovsky, bach_suites** — DCML .tsv; native .mscx | SUSPECTED (binary-staleness P5) | **BUG P3-native** (UNKNOWN-mode widely; key-only) | **🔴 BUG P0** (59% drop) **+P2** (minor-LT) | **🔴 active** (reconstruction bypassed→downbeat-only) **+P4** (beethoven offset) | CLEAN (relativeroot works) | **BUG** (denominator silently downbeat-only, F1) |
| **cpe_bach** — DCML .tsv; native .mscx | CLEAN | n/a | n/a | n/a | n/a | **BUG** (66/66 0-region; texture-threshold, excluded both sides) |
| **music21 `.music21.json`** — algorithmic, NOT GT | CLEAN (v9.9.1 recorded) | — | — | — | CLEAN (used only as the three-way *filter* leg) | CLEAN |
| **jazz** (effendi/omnibook/rampageswing) — NO GT | CLEAN | — | — | — | — | CLEAN (qualitative only; never feeds precision) |
| **snapshot scores (11)** — golden JSON (ours-pinned) | CLEAN (hash-pinned) | — | — | — | — | CLEAN (regression pins, not correctness GT) |

Notes: "key-only impact" = the defect moves `key_disagree`, not `root_err`/BIR. The Bach rntxt path
is **not** hit by P0 (rntxt beats are decimals, parse fine). The TSV path is **not** hit by P1
(relativeroot resolves applied chords). P2 hits both. The `live_head_verify` regen is the current
at-HEAD source for the TSV `.ours.json` [probe: `tools/reports/live_head_verify/`].

---

## §2 — The complete error-source ledger

### S1 — SOURCE

- **L1.1 [P5, reporting] Cross-corpus headline stale by 86 commits.** STATUS.md and MEMORY
  `project_dcml_baseline_head.md` cite **53.8% (20256/37639) @ `a69a23e59b` (2026-05-20)** as the
  "CURRENT BASELINE." `a69a23e59b` is **86 commits / 24 days behind HEAD** [probe:
  `git rev-list --count a69a23e59b..HEAD`→86], predating the entire Stage-1/2/3 refactor. A current
  at-HEAD regen **exists but is un-cited**: `tools/reports/live_head_verify/` (stamped `a4ae4a9203`)
  → re-aggregated read-only gives **54.4% (20480/37640)** [probe: `rerun_dcml_comparison.py
  --cross-corpus-root live_head_verify`]. Not a fabrication; a stale label.
- **L1.2 [P5, trap] `rerun_dcml_comparison.py` defaults to even-older dirs** (`live_20260515`,
  pre-STEP-1/D2, ~5pp low) [code: rerun_dcml_comparison.py:345-355]. No-arg invocation silently
  re-aggregates a stale corpus. **Accidental-measurement vector.**
- **L1.3 [staleness] Bach per-preset manifest binary vanished.** `tools/corpus/{baroque,jazz,default}`
  manifests record binary `a652dc1ba7` (size 48 992 256), but the on-disk binary is now
  `a4ae4a9203` (49 019 392) — the recorded artifact was overwritten by a rebuild, so the manifest's
  binary-identity self-check can no longer be re-run. The `.ours.json` themselves are **sha256-clean
  353/353 and output-current** (intervening commits are read-only/tools-only) [probe].
- **L1.4 [housekeeping] At-risk artifacts.** `tools/tools/` (312 MB superseded dup, gitignored);
  `tools/corpus_baroque/` + `tools/corpus_standard/` (pre-Stage-2.2a orphans, no manifest, name
  collides with the new layout). Safe against the gate (manifest guard refuses manifest-less dirs)
  but deletion candidates [probe].

### S2 — OURS-SIDE INGESTION

- **L2.1 [P3, confirmed] Declared-mode drop at MusicXML import.** `addKey`
  [code: src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp:5978]:
  `if (oldkey != key.key() || key.custom() || key.isAtonal())` creates the KeySig **only** when the
  new signature differs from the in-effect key. At piece start the synthesized default is `Key::C`
  with `KeyMode::UNKNOWN` [code: keylist.cpp:36-44, key.h:96], so an empty-signature `<key><fifths>0`
  collides (`oldkey==key.key()==C`) → **no KeySig object created → the `<mode>` carrier is never
  inserted → resolver reads `declaredMode=UNKNOWN`** [code: keyresolver.cpp:219-238]. **It is a
  default-key-match drop, NOT a `fifths==0` test** (corrects the doc framing). Population: **80
  zero-sig Bach stems, 79 with a recoverable `<mode>`** (54 minor, 25 major, 1 mode-less bwv62.6) —
  **corrects the "73" figure** [probe: count over the gate `.xml`].
  - **Blast radius is the KEY metric only, ambiguous subset.** The resolver's pitch-based detection
    recovers the key for unambiguous pieces: **bwv245.17 (empty-sig + `<mode>minor`) emits `Amin`**,
    not C-Ionian [probe]. The drop bites only relative-major/minor ties and partial signatures
    (the headroom dossier's Class-B), surfacing as `key_disagree` S2 — **it does not corrupt the
    root gate or `root_err`** (verified: 0/13 gate cases on mode-corrupted output, §3.A).
- **L2.2 [P3-native] Native `.mscx` reaches the same UNKNOWN-mode state by a different mechanism.**
  The native readers have **no dedup** [code: read410/tread.cpp:1338-1362, read460/tread.cpp:1307-1331]
  — a native KeySig that carries a mode preserves it. **But** the MS3 writer frequently **omitted
  `<mode>` even on non-empty signatures** (Mozart 2/92, Chopin 68/105, Corelli 152/212, Grieg 90/112)
  and empty-sig native movements carry **no `<KeySig>` element at all** (corelli 86, mozart 20, grieg
  20, cpe_bach 30, …) [probe: scan of `tools/dcml/*/MS3`]. Both → `keySigEvent` returns the C/UNKNOWN
  default → same resolver degradation. **So the UNKNOWN-declared-mode condition spans all 11 corpora**,
  even though the *import-dedup bug* is Bach-only.
- **L2.3 [latent] custom/atonal/mid-score-relative-mode.** The resolver never inspects
  `custom()`/`isAtonal()`; a mid-score `<key>` that changes only the mode (same fifths) would also be
  deduped. **Zero occurrences in the present corpora** (0 custom/atonal of 4584 KeySigs); latent.
- **L2.4 [S2→S4 coupling] Region coordinates.** `measureNumber` = the **displayed 1-based** number
  [code: batch_analyze.cpp:404-436, == measurelayout.cpp:1215-1229], so a **pickup is labeled 1 and
  collides with bar 1**, whereas DCML `mn`/rntxt label the pickup **0** → an off-by-one feeding the
  S4 reconstruction (L4.2). `beat = 1 + tickInMeasure/480`, **meter-unaware** [code:
  batch_analyze.cpp:655]. `startTick` is on the **written, repeat-unexpanded** timeline (no
  `expandRepeats` in the path) — this is CLEAN and matches DCML, *except* the P4 ABC subset (L4.3).
  Ticks-per-quarter is **480 by construction** (duration is defined as ticks/480), so the Python
  "tpb median" is a tautological constant 480 — **stable, not a risk** [code: compare_analyses.py:404-411].

### S3 — GROUND-TRUTH PARSING

- **🔴 L3.1 [P0, the headline] Fractional-`mn_onset` silent drop.** `parse_abc_harmonies_file`
  [code: dcml_parser.py:157] `mn_onset = float(row.get('mn_onset', 0.0))`, but the TSV `mn_onset`
  column holds **whole-note fraction strings** (`"1/2"`,`"3/8"`,`"7/8"`,`"79/2"`). `float("1/2")`
  raises `ValueError`, caught by `except (ValueError, KeyError): continue` [code: dcml_parser.py:178].
  → **every off-downbeat annotation is discarded; only `mn_onset="0"` (downbeat) rows survive.**
  - Verified: K545-1 = 119 rows → **70 regions, all on beat 1.0**; 48 fractional rows dropped
    [probe]. Corpus-wide: **60 676/103 085 = 58.9% dropped** (per-corpus 51.7%–67.0%) [probe:
    `/tmp/drop_probe.py`].
  - Two compounding effects: (a) **coverage loss** of 59% of GT; (b) each surviving downbeat span is
    **ballooned to a whole measure** (`_dcml_time_spans` runs each span to the *next surviving*
    annotation), so our within-measure regions get scored against the wrong (downbeat) label.
  - This is the GT for the **entire cross-corpus metric** (`rerun_dcml_comparison.py:96` →
    `compare_ours_vs_dcml_direct`/`compare_dcml_anchored`; `compare_rn.py:484` `--cross-corpus`;
    and the granularity-robust grid via `grid_score_piece_tsv`).
  - **Note the irony:** the TSV path *correctly* resolves applied chords via `relativeroot` and
    handles `(susp)` figures — but most of those chords are off-beat and **dropped before they're
    ever scored**.
- **🟠 L3.2 [P1, confirmed] rntxt applied-chord `/X` drop.** [code: dcml_parser.py:386]
  `primary = numeral.split('/')[0]` then `_compute_root_pc(primary, current_key)` roots in the local
  key. Oracle: **877/880 Bach applied rntxt rows mis-rooted (0.3% agreement)** [probe: `/tmp/oracle_probe.py`].
  Examples: `bwv10.7 V/vi` in B♭→parser F, true D; `bwv102.7 V6/IV`→parser G, true C [trace]. The
  TSV path is exempt (relativeroot, 86.6% applied agreement, 100% on dvorak/schumann) — **do not
  "fix" the TSV applied path.**
- **🟠 L3.3 [P2, confirmed both paths] Natural-minor degree table.**
  `_DEGREE_SEMITONES_MINOR=[0,2,3,5,7,8,10]` [code: dcml_parser.py:77], used by **both**
  `_compute_root_pc` and `_resolve_dcml_key`. Roots `viio` at tonic+10 (subtonic) not +11
  (leading-tone) and `vio` at +8 not +9. DCML writes the LT as plain `vii`/`viio` in **603/603**
  sampled minor cases (zero `#vii`) [probe: `/tmp/confirm_premises.py`]. Counts: **rntxt 434, TSV 603**
  + **~318 more disguised inside the TSV "applied"** set (`#viio/X`: relativeroot moves to the
  tonicized key correctly, but the `#` is dropped → a semitone flat) + **~29 `vio`** (the new 4th
  sub-bug). The TSV minor-LT corruption lives on the **fractional rows that P0 already drops**, so it
  poisons root_agree by *removing correct comparisons*, not by producing flagged disagreements (§3.B).
- **L3.4 [refined] It6/Ger/Fr/N is NOT the feared None-drop.** On the TSV path the parser feeds the
  **`numeral` column** (`vii`/`V`/`bII`), **not** the raw `It6`/`Ger65` token — so `_compute_root_pc`
  does not return None and does not mis-root It6 at the tonic. TSV aug6/N: **631 rows, 0 None, only 36
  disagree** (all the *applied* `It6/vi`-family). Bach has **2** aug6 tokens total [probe:
  `/tmp/inspect_undef_aug6.py`]. The F-2 hole is real but **small**, and only on `compare_rn`'s
  root-only fallback for the literal `chord` column.
- **L3.5 [clean] `oracle_undef` = music21 limitation, parser is right.** **6899/6899** TSV
  "oracle-undefined" rows are DCML parenthesized-suspension figures (`V(64)`,`I(974)`) that *music21*
  cannot parse but the parser roots **correctly** (its degree regex strips the parens) [probe]. Not a
  parser bug; the right denominator choice.
- **Net S3 artifact rate (oracle, scoreable rows):** **corpus-wide 4.9% (2660/53 837)** mis-rooted —
  **Bach rntxt 7.4%** (applied-dominated), **TSV 3.7%** (minor-LT-dominated). Because P0 drops 59% of
  TSV rows *proportionally*, the true full-corpus applied+minor-LT mass is **~2.4× the downbeat-only
  counts** [probe: `/tmp/summarize.py`].

### S4 — ALIGNMENT

- **L4.1 [active] The reconstruction is bypassed for TSV and the exact column is ignored.**
  `_build_measure_anchors`/`_dcml_tick_for` rebuild DCML ticks from our `measureNumber`+`beat`+
  `startTick` with a single global tpb [code: compare_analyses.py:414-455]. For TSV this only ever
  sees downbeat rows (P0), so it degenerates. **A robust column exists and is unused:** `quarterbeats`
  (absolute quarter position). A corrected aligner using `abs_tick = round(Fraction(quarterbeats)*480)`
  is **exact**: `quarterbeats=0 ⇔ our startTick=0`, **pickup-aware, no offset** — verified
  tick-for-tick on 18 pieces / 3 corpora incl. anacruses and 6/8 [probe: `/tmp/probe_origin.py`].
- **L4.2 [P3/D2, suspected] Pickup off-by-one on the measure-anchor path.** Our pickup region and
  first-full-bar region both carry `measureNumber=1` (L2.4); `_build_measure_anchors` keeps the
  smallest-beat region as the bar-1 anchor → corrupts the first full bar's `measure_start`; and DCML's
  `mn=0` pickup row hits the 4·tpb extrapolation branch. Exposure: irregular bars in 25/54 Mozart,
  10/149 Corelli [probe]. **Did not surface as a Bach gate contaminant** (chorales rarely have
  pickups); for TSV it is largely masked by P0 (the affected rows are dropped anyway). Active on the
  rntxt/Bach path but unquantified there.
- **🟡 L4.3 [P4, new — found in tracing] ABC/Beethoven structural offset.** On some repeat-bearing ABC
  movements the GT `quarterbeats` runs **~4 bars ahead** of our written-timeline ticks (GT last tick
  950 400 vs ours 958 560), so even the *corrected* qb-aligner mis-aligns and manufactures new
  disagreements — the corrected re-score made beethoven **+3.6pp worse** [trace: n14op131_05,
  n16op135_04]. A **fourth, distinct** ingestion/alignment defect (repeat-expansion or
  measure-numbering mismatch), localized to a subset of ABC. Must be handled by **downbeat-anchoring
  to ours**, not raw `quarterbeats`.

### S5 — COMPARISON / CLASSIFICATION

- **L5.1 [clean-ish] `classify_pair` drops un-rootable GT.** A DCML row with `root_pc=None`
  (Ger/Fr/N on the `compare_rn` `chord`-column fallback; @none) is silently excluded from `matched`
  [code: compare_rn.py:302]. Per L3.4 this is **small** (36 TSV applied-aug6 + a handful). Worth a
  one-line coverage note, not a re-baseline driver.
- **L5.2 [known] Coarse quality buckets** (`extract_quality` F-1 letter-`o`, F-2 It6 — already
  corrected in code; `three_way_classify` is root-pc only and **requires music21 non-None**, so the
  no-music21 ABC/Beethoven corpus cannot use the three-way leg and falls back to two-way
  `compare_ours_vs_dcml_direct`). No new defect; documents a structural limitation.

### S6 — AGGREGATION / REPORTING

- **L6.1 [F1] Downbeat-only denominator is never surfaced.** The cross-corpus reports divide by the
  P0-shrunken (downbeat-only) `matched`/`scoreable` set without flagging that 59% of GT was dropped —
  a reader sees "37 640 scoreable" and assumes full coverage. Coverage-honesty gap.
- **L6.2** = L1.1/L1.2 (stale headline + trap defaults).
- **L6.3 [clean] Denominators pinned:** 361 (Riemenschneider `.mscx`), 410 (music21 pre-filter), 353
  (`.xml` post-SATB-filter), 326 (WiR-covered, 324 distinct files) [probe].
- **L6.4 [coverage hole] cpe_bach 66/66 0-region** (`regions:[]`, key still emitted) — a
  texture-threshold gap (galant single-voice-per-staff never accumulates ≥3 simultaneous PCs), not a
  comparator/import bug; correctly excluded both sides [probe].

---

## §3 — Trace results: artifact rate per corpus

### §3.A — Bach gate (rntxt) — **the gate is clean** [trace: 13+7 cases end-to-end, N=20]

The Baroque-13 / Jazz-7 gate is defined by `three_way_classify == 'music21_dcml_agree'`
(music21 root **==** WiR root) **∧** winner `bassIsRoot==False`. **Mechanism of insulation:** the
filter *requires* `music21_root == wir_pc`, so a parser-corrupted `wir_pc` is admitted only if music21
independently coincides with it — and the applied/minor-LT artifacts overwhelmingly land in
`all_differ` (parser ≠ music21), which the gate discards.

| set | GENUINE error | AMBIGUITY | PIPELINE ARTIFACT | GT-LIMITATION |
|---|---|---|---|---|
| **Baroque 13** | **7** (phantom-root, segmentation, mis-qualification) | **6** (V7↔viio, G6≡Em7, sus-over-tonic↔sus-chord) | **0** | 0 |
| **Jazz 7** | **3** (phantom-root inversions) | **4** (same families) | **0** | 0 |

- **0/13 and 0/7 are parser- or mode-artifacts** — every case has
  `gate_dcml_root == rntxt_parser_root == music21_true_root` [trace: `/tmp/trace_out.txt`]. The one
  applied-artifact that reached the `music21_dcml_agree` bucket corpus-wide (**bwv43.11**, `V/V`→parser
  D coincides with music21's chord-root D) has `bassIsRoot==True` and is therefore excluded by the BIR
  filter — a clean demonstration of the double-filter [probe].
- **Broader Bach** (550 clean three-way disagreements): artifact rate **34.4% overall**, but
  **44.6% in `all_differ` (gate-excluded)** vs **2.7% (1/37) in the gate's bucket** [probe:
  `/tmp/sample_out.txt`]. So the parser bugs are large in aggregate yet quarantined away from the gate.
- **Verdict:** the headline gate is **trustworthy as a regression pin**, but as a *precision* metric it
  **over-counts** — ~46% (6/13, 4/7) is legitimate musical ambiguity where our root is often *present in
  the sonority and the GT picks the rootless reading* (bwv269 V7 vs viio6; bwv432 Am vs vi; bwv381
  G6≡Em7). **Genuinely-actionable residual: ~7 Baroque, ~3 Jazz.**

### §3.B — TSV corpora — **≤26% of flagged errors are genuine** [trace: N=39 + corpus-wide re-run]

| corpus | N | pipeline artifact | genuine | ambiguity | dominant artifact |
|---|---:|---:|---:|---:|---|
| corelli | 6 | **83%** | 17% | 0% | float-drop |
| tchaikovsky | 3 | **100%** | 0% | 0% | float-drop |
| schumann | 3 | 67% | 33% | 0% | float-drop |
| grieg | 4 | 50% | 25% | 25% | float-drop |
| chopin | 5 | 40% | 20% | 40% | float-drop |
| mozart | 6 | 33% | 17% | 50% | float-drop (amb = V7-on-5th) |
| dvorak | 3 | 33% | 67% | 0% | float-drop |
| bach_suites | 4 | 0% | 50% | 50% | (ambiguity: cadential 6-4, susp) |
| beethoven(ABC) | 5 | 0% | 20% | 80% | (P4 structural offset) |
| **sample total** | **39** | **44%** | **26%** | **31%** | float-drop |

- **Independent corpus-wide confirmation** [probe: `/tmp/corrected_metric.py`, the production metric
  fed a corrected parser]: flagged `root_err` collapses **corelli −23.5pp, schumann −14.8, tchaikovsky
  −12.7, mozart −6.3** — matching the −9.9pp aggregate from a different direction. **beethoven +3.6pp
  (worse)** isolates the P4 structural-offset confound.
- **The minor-LT/mode-drop buckets are empty in the matched flagged-error set** — structurally, not by
  sampling: the buggy alignment can only match our regions to surviving downbeat rows (plain diatonic
  triads); the minor-LT corruption lives on the dropped `viio/X` rows. **No mode-flip in any of the 39**
  (mode-drop surfaces as `key_disagree`, not `root_err`).
- **Genuine residue (the real target) clusters into fixable patterns:** dominant rooted on a chord-tone
  (mozart K283-3 II7/VI7 for V7), **absent-root over-reach** (dvorak op08n03 invents A♭ over a {C♯,F}
  dyad — the `project_absent_root_guard_rejected` failure mode), applied-leading-tone mis-roots
  (BWV808 `vio` for `viio/V`).
- **Compound meter (6/8):** the tick math is meter-clean (`qb×480` exact in 6/8), but each 6/8 bar
  carries *more* sub-beat onsets, so P0 drops a larger share per measure and balloons a longer span —
  the damage is amplified, the correction is identical [trace: K280-2, K283-2, BWV812].

---

## §4 — Prioritized elimination plan (ONE coordinated re-baseline)

All fixes land together so the precision numbers move once, coherently. Order by blast radius and
dependency; do **not** ship piecemeal (a partial fix would re-baseline against a still-corrupt chain).

**Step 1 — S3 fractional-onset (P0), the dominant lever.** Parse `mn_onset`/`quarterbeats` with
`fractions.Fraction` (never `float`); keep **all** annotations; align by **`quarterbeats×480`
absolute tick**, not measure-anchor reconstruction. *Expected movement:* cross-corpus per-DCML
root_agree **54.4%→46.7% (−7.7pp, de-inflation)**, per-ours **49.3%→59.2% (+9.9pp)**, GT volume
**×2.40**. **Must be co-designed with Step 4** (P4) so repeat-bearing ABC scores anchor to matched
downbeats, not raw `quarterbeats` — else beethoven regresses +3.6pp.

**Step 2 — S3 rntxt applied + minor-LT/vio (P1, P2).** Port the TSV `relativeroot` resolution into
`parse_rntxt_file` (resolve the `/X` before rooting); fix the natural-minor degree table for raised
`viio`/`vio` (or root *all* figures via music21 `roman.RomanNumeral`). *Expected movement:* the Bach
**`all_differ`/"functional residual" deflates** (the dossier's 366 phantom roots + the ~318 disguised
TSV `#viio/X` + ~434 rntxt LT dissolve into agreement). **The 13/7 gate does NOT move** (already
clean) — so this is safe for the gate and corrects the *broad* precision headline only.

**Step 3 — S2 declared-mode (P3).** Restore the declared mode for empty-signature scores at import
(don't dedup a mode-bearing KeySig) and graded-prior the native UNKNOWN-mode case. *Expected
movement:* `key_disagree` **S2** shrinks (the headroom dossier's Stage-4 lever, ~349 + partial-sig);
**`root_err`/BIR unchanged.** This is the existing held Stage-4 work — fold its measurement into the
same re-baseline so key and root numbers move together.

**Step 4 — S4 ABC structural offset (P4).** Detect/repair the `quarterbeats`↔ours tick offset on
repeat-bearing ABC movements (anchor GT to ours by matched downbeats). Required for Step 1's
correction to be valid on beethoven.

**Step 5 — S6/S1 reporting hygiene.** Surface the coverage denominator honestly (post-fix it is the
full annotation set, ×2.40); refresh the stale 53.8% headline to the post-fix number; repoint
`rerun_dcml_comparison.py` defaults to a HEAD-aware path (fail loudly if `git_hash ≠ HEAD`).

**Post-re-baseline expectation:** a *region flagged as an error* corresponds to a real
composer-vs-analyzer disagreement. The honest precision picture becomes: cross-corpus per-DCML
≈46.7% on **full** GT (×2.40 coverage); the BIR gate **unchanged** (it was already clean); the genuine
TSV error residual ≈**26%** of today's flagged set, clustering into the dominant-on-chord-tone /
absent-root-over-reach / applied-LT patterns that are the *real* Stage-5/6 targets. **The dossier's
"95.2% functional / 4.8% vertical" headline is materially inflated** by P0+P1+P2 and must be
re-derived after this batch (the "fit against the current gate" risk in the functional-residual
dossier §4 is now quantified, not hypothetical).

---

## §5 — CONFIRMED-CLEAN (stop suspecting these)

- **music21 is filter-only, never ground truth** — read solely as the `music21_dcml_agree` three-way
  leg; no tool treats it as GT [probe: grep]. Version 9.9.1 recorded in manifests + `.xml`
  `<software>` + REPRODUCIBILITY.md.
- **jazz feeds no precision metric** — consumed only by `compare_omnibook.py` (qualitative root%
  vs the chart's own `writtenRootPc`, `ground_truth:false`); never enters BIR or the cross-corpus
  aggregate [probe: grep]. (`tools/corpus/jazz` is the Jazz *preset* on the 353 Bach chorales, not
  jazz scores.)
- **snapshot goldens are regression pins** — the analyzer's own output frozen by `--update-goldens`;
  the test fails on byte drift; sources hash-pinned. Never a correctness reference [code:
  pipeline_snapshot_tests.cpp:901-926].
- **Repeats are NOT a misalignment source** (except the P4 ABC subset) — no `expandRepeats` in the
  path; both sides on the written, played-once timeline; `measureNumber` monotonic [code: grep clean].
- **`quarterbeats` origin == our `startTick` origin, pickup-aware** — the corrected aligner is exact;
  no constant offset needed (0/18 mismatches incl. anacruses + 6/8) [probe].
- **TSV `relativeroot` applied resolution works** (single-level; 86.6% oracle agreement, 100% on
  dvorak/schumann) — do not touch it [probe].
- **It6/Ger/Fr/N is not a major None-drop** — the parser feeds the `numeral` column; only ~36 TSV
  applied-aug6 + 2 Bach tokens affected [probe].
- **`oracle_undef` rows are a music21 limitation, parser is right** — 6899/6899 are `(susp)` figures
  the parser roots correctly [probe].
- **Ticks-per-quarter is a stable 480 by construction** — not a tpb-instability risk [code].
- **Transposing-instrument concert-vs-written is consistent** — key axis reads `concertKey()`, pitch
  axis collects `ppitch()`; both concert-consistent; corpora are non-transposing anyway [code].
- **The BIR 13/7 gate is structurally insulated** from the parser/mode bugs (double filter; §3.A).
- **Denominators 361/410/353/326 are sound** [probe].

---

## §6 — Unknowns / what needs deeper probing

1. **P4 ABC structural offset — exact scope unmeasured.** Which ABC movements offset, and whether it
   is repeat-expansion vs anacrusis-numbering, is not pinned; the *corrected* beethoven number is
   therefore unreliable. Probe: per-movement compare GT `quarterbeats` span-end to our `max(endTick)`
   and bisect the divergence. Until then, treat the −7.7pp aggregate as "ex-beethoven solid, beethoven
   ±".
2. **P3 mode-drop's exact `key_disagree` blast radius** is taken from the headroom dossier (~349 +
   partial-sig), not re-measured here. A `--dump-key-candidates declaredModeOrdinal==-1` per-region
   count per corpus would size it precisely (the dump field already exists, `a4ae4a9203`).
3. **L4.2 pickup off-by-one on the rntxt/Bach measure-anchor path** — not isolated. The gate is clean,
   but the broader Bach `root_err` residual on pickup chorales is unquantified. Probe: list WiR
   `analysis.txt` with an `m0` line and diff aligned-pair onset ticks.
4. **cpe_bach 0-region** is hypothesized as a texture/≥3-PC-threshold gap from the data; confirming the
   exact gating site needs an analyzer run (out of scope for this read-only pass).
5. **The post-fix net precision number** — the whole point of the re-baseline — is not produced here
   (no fixes this run, by mandate). The corrected-parser probe (§4 Step 1) is the lower-bound estimate;
   the true number needs P1+P2+P4 fixed together.
6. **The non-Bach functional-vs-ambiguity ceiling** (the dossier's bucket-3 for ABC/Beethoven) remains
   unmeasured — no `.music21.json` for those corpora, so the three-way leg is unavailable; the 31%
   "ambiguity" in §3.B is a 39-case sampled judgment, MED confidence.

---

*Drivers (throwaway, `/tmp`, no repo writes): `drop_probe.py` (P0 corpus-wide drop), `oracle_probe.py`
+ `summarize.py` + `confirm_premises.py` (S3 oracle sizing), `corrected_scorer.py` + `build_table.py` +
`probe_direction.py` + `probe_origin.py` (P0 blast radius + quarterbeats origin), `trace_gate.py` +
`sample_artifact.py` (Bach gate trace), `trace_lib.py` + `audit.py` + `corrected_metric.py` (TSV
trace). Six parallel sub-agents (S1-source, S2-keysig, S2-ticks, S3-oracle, P0-blast-radius,
gate-trace, TSV-trace); the parent spot-verified each load-bearing claim against source or a re-run.
This dossier is the only repo write.*
