# Layer-4 (chord) certification audit — PASS 1 (blind enumerative), session 3 of 3: the satellites

> **CC, 2026-07-11. EG-7 / OI-84 / OI-102.** Third and final session of the layer-4
> first pass. Scope: the shared chord-symbol formatter, the beam-1 chord-path decoder,
> the sparse-slice quality refinement, and the layer-4 chord types. This is the FREEZE
> draft (written blind — before any withheld file was opened). The unblind reconciliation
> (register cross-refs, defect-type promotions, "when opened" log) is appended in the
> documentation fold after this freeze commit. **Certification is NOT decided here** — it
> awaits the whole-layer second pass (catalog signature sweep + blind second reading +
> measured error rate).

## 0. Provenance

- **Audit protocol:** `cowork_audit_protocol.md` (P1 enumerate-then-classify, P2 closed
  verdict set, P3 contract direction, P4 behavioral characterization), first pass of P8.
- **Inventory (frozen, read-only):** `tools/audit/l4/{l4_functions,l4_literals,l4_fields,
  l4_branches,l4_decls,l4_crosslayer}.csv` + `manifest.json`, stamped corpus `c50002fee1`,
  extraction commit recorded in the manifest.
- **This session's instruments (committed in the freeze):**
  `tools/audit/l4/pass1_satellites_dispositions.py` (dispositions),
  `tools/audit/l4/pass1_satellites_firerate.py` (behavioral characterization).
- **Artifacts:** `tools/audit/l4/pass1_dispositions_satellites.{csv,json}`,
  `tools/audit/l4/pass1_satellites_firerate.json`.
- **Corpus:** `tools/corpus/{baroque,jazz,default}` — each verified at `git_hash c50002fee1`,
  352 pieces, 11222 / 10863 / 11211 regions.
- **Scope declaration:** READ-ONLY fact-finding. No production behavior changed; no constant
  tuned; no golden refreshed; `tools/robust_stop/` and `tools/corpus/` untouched. No
  production counter was added (least-invasive routes sufficed — see §6).

## 1. Scope, populations, and inventory sizes

Five deep-audited files; every one is **LIVE surviving code** (population c), not retiring
and not the dormant slice-decoder rebuild (which is `chordslicedecoder`, a different file,
covered by session 1). One file carries an open retire-vs-survive question (the path
decoder, §5.2) but is LIVE today.

| File | Population (verified at code) | Rows in scope |
|------|------------------------------|---------------|
| `chord/chordsymbolformatter.cpp` | LIVE shared formatter | 505 |
| `decode/chordpathdecoder.h` | LIVE beam-1 path re-expression (retire/survive at engagement OPEN) | 16 |
| `region/sparsechordrefinement.cpp` | LIVE post-commit quality refinement | 63 |
| `region/sparsechordrefinement.h` | (surface of the above) | 3 |
| `types/analysistypes.h` (L4-type rows only) | LIVE value-types leaf | 112 |
| **Total** | | **699** |

**The analysistypes.h split.** analysistypes.h is a mixed cross-layer leaf. Only the L4
chord-type rows are dispositioned here: `DecodeQualityLevel`, `ChordQuality`,
`ChordAnalysisTone`, `ChordAnalyzerPreferences` (+ `kDefault`), `ChordTemporalContext`
(lines up to 537; `function::ScoringPhase` and `ParameterBound` are shared/relocated
neighbors on lines 67–95, kept in scope with a note). The L3 types (`KeySigMode`,
`KeyModeAnalyzerPreferences`, `PitchContext`; lines ≥546) are **out of scope** — covered by
the L3 audit; 255 raw rows excluded. The instrument enforces the line-<546 cut (one row
that first appeared as an in-scope function was an L3 preferences method with `start_line`
≥546 and was correctly excluded once the functions table's `start_line` column was read).

By kind: 32 functions, 319 literals, 288 branches, 51 fields, 7 cross-layer, 2 decls.

## 2. Disposition summary (protocol P2 — every row has a verdict)

| Verdict | Count | Class |
|---------|-------|-------|
| SURVIVES | 332 | code (functions, branches, decls, methods) |
| ESTABLISHED | 305 | constant (music-theory/TPC/notation integers; scoring defaults) |
| PUBLISHED | 44 | derived-fact (cross-layer type fields; the diatonic-degree primitive) |
| ASSUMPTION | 15 | premise (the enharmonic-spelling normalization branches) |
| DEAD | 3 | constant (declared-placeholder toggles — reserved, named future consumer) |

"No issue" is a recorded verdict with a stated reason in every row's `note` column; the
full per-row table is `pass1_dispositions_satellites.csv`. No DUPLICATED-derived-fact
verdict was used: the duplicated tables are ESTABLISHED music-theory constants whose
duplication is carried as a FINDING flag on the table-head row (§4), not as a value-verdict.

**Constants and `param_manifest`.** Every ChordAnalyzerPreferences numeric default was
checked against `tools/param_manifest.json`: 19 scoring-weight defaults are formal fit-rows,
`extensionThreshold` is referenced in the manifest notes only, and `decodeQualityLevel` /
`scoringPhase` are (correctly) absent (not scoring weights). The formatter's ~221 numeric
literals are all music-theory / TPC-encoding / notation-catalog integers (pitch classes,
scale intervals, TPC codes, figured-bass indices) — ESTABLISHED, not tunable, none in the
manifest. No DEAD numeric literal was found; the three DEAD rows are the reserved boolean
placeholder toggles.

## 3. Contract-direction check (protocol P3 — spec → code)

The layer's contract for these files lives in `ARCHITECTURE.md` §4.3 (the formatter),
`docs/scoring_model.md` (the file-layout note and the scoring pipeline), `docs/decoder_design.md`
(the path decoder), and `docs/duplication_audit.md` §5.4 + `ARCHITECTURE.md` §4.1c (the sparse
refinement). Every expected output was located, or its absence flagged.

**Formatter coverage statement (the identity space renders).** The committed-identity space
is `ChordQuality` (9 values incl. `Unknown`) × the `Extension` flag set × bass/root. Checked
at the code:
- `formatSymbol` covers every quality: `csfQualitySuffix` has a case for each and a `default`
  → `""` (so an `Unknown` quality renders as the bare root name, never a crash or garbage).
  Slash-bass is guarded by `csfIsValidBassNoteName` (the `/p` fix). `(no 3)` marks OmitsThird.
  **Corpus: 100% of regions render a non-empty symbol on all three presets; 0 empty.**
- `formatRomanNumeral` covers diatonic (`I`…`vii`), chromatic (`♭VII`…), inversion figures
  (`6/64/65/43/42`), tonicization (`V7/x`, `viiø7/x`), and augmented-sixth (`It/Fr/Ger+6`).
  It returns `""` only for `Unknown` quality (the `csfDiatonicRoman` `default`) at a
  non-diatonic root. **Corpus: 100% non-empty; 0 empty** — because no committed region reaches
  the formatter with `Unknown` quality (the sparse refinement / `forceChordTrack` upgrade it
  first; see §5.1). So the theoretical uncovered corner (`Unknown` + non-diatonic root →
  empty label) does not occur on the live paths, but it exists at the contract level and is
  closed only by the upstream refinement.
- `formatNashvilleNumber` has a **coverage gap** (§4, finding): a non-diatonic (chromatic)
  root renders as `"?"`, and the bass degree is mapped by a crude `(bassDegree % 7) + 1`.

**Doc-sync checks against the code (findings in §4):** the ARCHITECTURE §4.3 "File:" header
and the "move to its own `chordsymbolformatter.{h,cpp}` pair" fix are stale relative to
`refactor #1`; the §4.3 "extensions beyond the 7th are not yet emitted" statement is
contradicted by the code and corpus; the §5.11 aug6 preset-gating is asserted but deferred
in the formatter.

## 4. Findings (every flagged row, file:line, one sentence)

Findings are surfaced only — **no fix is made** (guiding principle 8). Register rows
(`OPEN_ITEMS.md`) are assigned at unblind (§8); duplication findings are anchored at the
table-head row in the dispositions CSV.

**Duplication (guiding principle 6 — one path per concern):**
1. `chordsymbolformatter.cpp:46-58` & `88-99` — the four note-name tables (SHARP/FLAT and
   their German variants) are duplicated verbatim between `csfPitchClassName` and
   `csfPitchClassNameFromTpc` (a latent mis-spelling risk if one copy is edited without the
   other). **This one is already noted in `ARCHITECTURE.md`** with a proposed shared helper —
   reference, do not duplicate the note.
2. `chordsymbolformatter.cpp:457-465` & `788-796` — the 7-mode diatonic scale-interval table
   is duplicated in-file (`csfChromaticRoman` `SCALES` vs `csfTonicizationScales`) **and** the
   shared key-layer primitive `keyModeScaleIntervals` already holds it (the sparse refinement
   uses that shared copy). Three copies of one music-theory table.
3. `chordsymbolformatter.cpp:799-803` & `840-844` — the 21-entry KeySigMode→diatonic-parent
   mapping is byte-identical in two places (`csfTonicizationParent` and the local
   `CHR_DIATONIC_PARENT` inside `formatRomanNumeral`).
4. `chordsymbolformatter.cpp:466-467`, `492-493`, `937-938` — the UPPER/LOWER Roman-numeral
   string arrays recur three times.

**Doc-sync / contract mismatch (guiding principle 10; verified at code+data, principle 15):**
5. `chordsymbolformatter.cpp:539-545,584-615` — `csfDiatonicRoman` **does** emit 9th/11th/13th
   Roman-numeral levels (and `(add9/11/13)`); the corpus shows ~129/80/129 such labels per
   preset. `ARCHITECTURE.md §4.3` states "extensions beyond the 7th are not yet emitted" —
   stale/contradicted.
6. `chordsymbolformatter.cpp:884-899` — the aug6 label block (`It/Fr/Ger+6`) fires
   unconditionally; its own comment says preset gating is "deferred — `formatRomanNumeral()`
   has no preset context". `ARCHITECTURE.md §5.11` asserts aug6 is "Gated to Standard and
   Baroque presets only. Jazz … continue to emit chromatic Roman numerals." The corpus shows
   Baroque 8 / Default 7 / **Jazz 0** aug6 labels — but the Jazz 0 is an upstream-analysis
   coincidence (the `SharpThirteenth` extension is not set under the Jazz preset), **not** the
   documented gate; any effective gating would be at the (out-of-scope) call site.
7. The ARCHITECTURE §4.3 "File: `chordanalyzer.h`" header and the §"move `ChordSymbolFormatter`
   to its own `chordsymbolformatter.{h,cpp}` pair" fix are stale: `refactor #1`
   (`docs/scoring_model.md` file-layout note) split the **implementation** into
   `chordsymbolformatter.cpp` while intentionally keeping the **declarations** in
   `chordanalyzer.h` (the stable boundary) — so the `.h` half of the proposed pair will not
   happen, and ARCHITECTURE was not updated. (No `chordsymbolformatter.h` exists.)

**Contract-coverage gap (protocol P3):**
8. `chordsymbolformatter.cpp:1013-1020,1029-1032` — `formatNashvilleNumber` renders a chromatic
   (non-diatonic) root as `"?"` and maps the bass by a crude `(bassDegree % 7) + 1` (both marked
   "refine as needed"). LIVE via the notation bridge / imploder / context-menu, so the gap is
   user-reachable, not test-only. Not every committed identity has a defined Nashville rendering.

**Premise provenance (Premise Gate 17f — figures via generated artifacts):**
9. `chordsymbolformatter.cpp:108-193` — the enharmonic-spelling normalization branches
   (`pc=3`/`pc=8`/`pc=10`, `Cb`/`Fb`) are notation-convention ASSUMPTIONS whose justification is
   hand-transcribed corpus-survey counts in comments ("533 sharp-authored pc=8", "155/277",
   "95/256"; Iter 78/84/89), not a generated artifact. Display-layer only — it does not affect
   chord identity or inference — but load-bearing for display spelling correctness.

## 5. Boundary facts for the two open questions (facts, not decisions)

### 5.1 Sparse refinement — L4 field overwritten from an L5-flavored concern

- The three refinement functions consume the **resolved key** (`keyFifths`, `keyMode`) as a
  prior and **overwrite the committed `identity.quality`** (an L4 field) **after** `analyzeChord`
  has committed the winner and the post-scoring gates ran (`regionanalyzer.cpp:1003-1006`,
  post-commit; the refined identity then feeds `decoder.commit`, so it also flows into the next
  region's `previousQuality`).
- `refineSparseChordQualityFromKeyContext` acts only when `quality == Unknown` (Unknown → the
  key's diatonic triad, if tones fit); `applyTonicPriorToSparseChord` is stronger — it overwrites
  a committed **non-Unknown thin** quality (`Power`/`Suspended2`/`Suspended4`) on ≤2-PC regions;
  `forceChordTrackQualityFromKeyContext` (chord-track annotation only) forces Unknown → diatonic
  triad with no tone-fit check and no Aeolian exclusion.
- Callers: `regionanalyzer.cpp` (batch/region path, Pass-1 + Pass-2/2b), `sectionanalyzer.cpp`,
  the notation bridge. `diatonicDegreeForRootPc` (same file) is a **pure** helper consumed
  layer-wide (the L5 function modules `functionresolver`/`functionromannumeral`/
  `functionrelationallabel`, section, bridge, batch) — a single published copy (no duplication),
  but its home (region/sparse-refinement) is narrower than its consumer set (a possible
  misplacement of a shared music-theory primitive).
- **The ownership decision (L4 vs L5) is not made here** — it is the existing open register
  question; these facts enrich it.

### 5.2 chordpathdecoder.h — retire vs survive at the engagement

- **Callers:** `regionanalyzer.cpp` only — the production region path (Pass-1 loop +
  two Pass-2/2b sub-loops, three construction sites) — plus `decode_tests.cpp` (the
  byte-identity equivalence test). No other caller.
- **Coupling to the retiring competition:** `commit()` is a byte-identical re-expression of
  `advanceTemporalContext()` — the hand-threaded temporal state of the legacy region-competition
  path (the path that retires at the L4+L5 engagement). If `advanceTemporalContext` retires,
  `commit()` retires with it.
- **Coupling to the surviving consumer:** the forward members (`path()`, `recordNode()`,
  `alternatives`, `winnerScore`, `winnerMargin`) are shaped for the **surviving** Stage-6
  functional-labeling consumer and the wider-beam future (`docs/decoder_design.md`: "Wins come
  at Stage 3.2"). At beam 1 they are **inert — zero consumers today** — declared dormancy with a
  named future consumer (Stage 6 / Stage 3.1b decode-once-query-many), which satisfies the
  fact-publication corollary (declared dormancy, not waste).
- **The retire/survive decision is not made here.** The facts point both ways: coupled to the
  retiring competition via `advanceTemporalContext`, shaped for the surviving consumer via
  `path()`.

## 6. Behavioral characterization (protocol P4 — fire rates)

Full artifact: `tools/audit/l4/pass1_satellites_firerate.json` (all figures generated, not
hand-transcribed; per-preset corpus `c50002fee1`).

**Formatter — route: the batch outputs themselves** (the `chordSymbol` / `romanNumeral` in
each region ARE the formatter's output; Standard spelling — so the German-spelling branches
fire 0 here, reachable only on the notation render path with a German score style, exercised
by the enharmonic-spelling unit tests). Baroque figures (Jazz / Default alongside in the JSON):

| Formatter branch | Baroque fires / 11222 regions |
|---|---|
| `formatSymbol` (non-empty) | 11222 (100%) |
| `formatRomanNumeral` (non-empty) | 11222 (100%) |
| slash-bass symbol | 4124 |
| inversion figure (RN) | 3144 |
| tonicization label `V7/x`,`viiø7/x` (RN) | 440 |
| `(add…)` notation (RN) | 327 |
| 9th/11th/13th extension level (RN) | 129 |
| chromatic numeral `♭/♯` prefix (RN) | 96 |
| `M7`/`M9`… major-seventh marker (RN) | 85 |
| augmented `+` (RN) | 6 |
| augmented-sixth `It/Fr/Ger+6` (RN) | 8 (Jazz **0**) |
| `Cb`/`Fb` very-flat spelling (symbol) | 1 |
| `(no 3)` OmitsThird (symbol) | 1 |

Every documented formatter branch fires on the corpus at a rate consistent with its
population; none is a never-fires or always-fires surprise (the rare branches — very-flat
spelling, OmitsThird — fire ≥1, and the German branches are reachable off the batch path).
The Jazz-0 aug6 is the §4 finding-6 coincidence, not a formatter gate.

**Path decoder — route: reading + the equivalence test** (dormant plumbing has no corpus
signal). `commit()` fires once per committed region and once per Pass-2/2b sub-region,
byte-identical to `advanceTemporalContext` (`decode_tests.cpp` proves the equivalence). The
`path()`/`recordNode()`/`alternatives`/`winnerScore`/`winnerMargin` members have **zero
consumers** today (inert). `DecodeQualityLevel::Normal`/`Deep` behave as `FastBeam1` (no-op).

**Sparse refinement — route: corpus opportunity population + reading** (two entry points, per
Task 2):
- `refineSparseChordQualityFromKeyContext` and `applyTonicPriorToSparseChord` are **called on
  every region** (unconditional at `regionanalyzer.cpp:1003/1005`) → call-fire rate 100%.
- The **quality change** is confined by the guards: `refine` acts only on `Unknown`; `tonicPrior`
  only on thin quality + ≤2-PC. Corpus bound: ≤2-PC regions are **125 / 122 / 124** (~1.1% of
  ~11k), `Unknown`-final = **0**, thin-on-≤2-PC-final = **0** on all presets — i.e. **every**
  ≤2-PC region ends as a triad, strong evidence the refinement upgrades them; the change is
  bounded at ≤125 regions per corpus.
- `forceChordTrackQualityFromKeyContext` fires **0** on the batch corpus (chord-track /
  notation-annotation path only — `notationcomposingbridge.cpp:1157`, `notationimplodebridge.cpp:1182`).
- The **exact** refine-vs-tonicPrior change split is **not separately instrumented**: a production
  default-OFF counter + byte-identity re-proof is disproportionate to the marginal gain over this
  tight corpus bound (recommended as a follow-up only if the L4/L5 boundary decision needs the
  exact split). This is the P4 "fire rate not measured with the reason" allowance applied to the
  residual quantity only, not the whole mechanism.

## 7. "No issue" items of note (checked, clean)

- `csfIsValidBassNoteName` (711-725) — the slash-bass name guard (the `/p` bug fix) is present
  and correct.
- The documented `sussus→sus` sanitize (`ARCHITECTURE.md`, "Fixed 2026-04-13") is **absent** from
  the current formatter, but the single-token `csfQualitySuffix` builder and the Sus4+Maj7
  requalification (`formatSymbol:733-746`) mean the double-prefix string can no longer be produced
  — no regression; the historical mechanism is simply gone (a doc-history note, not a finding).
- `maxTotalInversionContextBonus` (analysistypes 254-268) — a documented-inert cap that never
  clamps at current values; consumer is the competition pipeline (oracle session). Not a finding.
- The three `use*Annotations`/`useExistingChordSymbols` toggles + the commented `StylePrior`
  (388-414) — DEAD-but-reserved, ARCHITECTURE "Do not remove" placeholders with named future
  consumers; declared, not silent dead code.
- The analysistypes.h types are documented as a **pure relocation** leaf (same name/namespace/
  layout); nothing in the L4-type rows contradicts that.

## 8. Unblind, reconciliation, and register (appended after the freeze)

**When each withheld file was first opened.** All were opened only **after** the Task-3 freeze
commit `10495a6bca` (the blinding boundary — no withheld file was opened before it), in this
order: `OPEN_ITEMS.md` (in full), then `DEFECT_TYPES.md`, then `STATUS.md`, then
`cc_l4_audit_pass1_report.md`, `cc_l4_audit_pass1_decoder_report.md`,
`cc_l4_audit_pass1_oracle_report.md`. The mandatory session-start `OPEN_ITEMS.md` read was
deferred to here by the instruction (Cowork performed the register check for the dispatch).

**No new defect TYPE.** Every §4 finding maps to an existing `DEFECT_TYPES.md` type — DT-3
(value-copied constant tables), DT-11 (hand-transcribed measurement number), DT-12 (stale
anchor / doc drift), DT-17 (silently-truncating / incomplete specified capability). This
matches sessions L4-2a and L4-2b (existing types only). `DEFECT_TYPES.md` is unchanged.

**No correctness defect.** As with L4-2a (decoder) and L4-2b (oracle), the satellites reproduce
their documented design. The nearest-to-functional finding is the Nashville chromatic-root
coverage gap (finding 8) — a display-layer, opt-in-path degradation, not an inference/identity
defect.

**Register reconciliation (new rows and references):**
- **New — OI-111** (DT-3/#6): the formatter's internal duplicated music-theory tables
  (findings 1–4). Sibling of OI-92 / OI-97 (L3 duplications).
- **New — OI-112** (DT-12/#10): the formatter/satellites ARCHITECTURE.md doc drifts (findings
  5–7). Sibling of OI-107 (the oracle's ARCHITECTURE drifts). Finding 7's *header-location*
  substance is already OI-108(b) + ARCHITECTURE §4.1i — OI-112 carries only the stale §4.3
  wording; it references OI-108(b), does not duplicate it.
- **New — OI-113** (DT-17/P3): the `formatNashvilleNumber` chromatic-root / bass coverage gap
  (finding 8).
- **New — OI-114** (DT-11/#17f): the enharmonic-spelling normalization premise provenance
  (finding 9), display-layer only.
- **Referenced, not duplicated:** the §5.1 sparse-refinement boundary facts enrich **OI-102(i)**
  and the **OI-10 / OI-29 / DT-4** quality-from-key-single-owner substance; the §5.2 path-decoder
  facts enrich **OI-102(ii)**; the `bassNoteRootBonus` 0.65-vs-0.70 ARCHITECTURE drift at
  `analysistypes.h:177` is already **OI-107(a)** (the oracle session) — not re-flagged; the
  three `use*Annotations` placeholder toggles are already **OI-80** (annotation-input TODO
  flags never read) — the DEAD-but-reserved disposition references it.
- **Manifest-gap check (the L4-2c "OI-91-class" task from the parent report §L4-2c row):** the
  ChordAnalyzerPreferences scoring defaults in `analysistypes.h` **ARE** in
  `tools/param_manifest.json` (19 fit-rows; `extensionThreshold` in the notes; the two
  non-scoring knobs correctly absent) — so unlike the decoder (OI-103) and the oracle
  file-statics (OI-106), **there is no new manifest-publication gap for this scope**.
- **OI-102 updated** to record L4-2c done (this report + freeze `10495a6bca`), with the
  boundary facts folded into (i)/(ii).

## 9. Status

This completes the **layer-4 first pass** (sessions 1 decoder, 2 oracle, 3 satellites). Layer-4
**certification is not decided** by this pass — it awaits the whole-layer second pass (the
catalog signature sweep with the full defect-type catalog, a blinded second reading, and the
measured residual-error rate), after which the certification decision goes to the user.
