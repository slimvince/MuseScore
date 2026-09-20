# CC Foundations-Verification Report — the facts the back-half re-grounding rests on

*CC, 2026-06-13. Base `a4ae4a9203`. Method A–H; never-guess in full force (this run IS the
double-check). Read-only except the music21 provenance check (Task 3, already-recorded —
no edit needed) and the doc-currency edits (Task 6, staged not committed). Every claim is
tagged `[code]` (read the source), `[probe]` (Python/shell over committed data), `[dump]`
(the `--dump-key-candidates` instrument), or `[test]` (a suite run). A CORRECTION to any
prior finding is called out loudly.*

> **This report gates ratification of `docs/back_half_design.md`.** The two consolidated
> lists at the end — *facts the re-grounding can stand on* vs *facts corrected/quarantined*
> — are the gate.

---

## LEAD — Task 1 (THE KEYSTONE): the declared-mode drop is CONFIRMED, root-caused, and the reach is NOT diminished

**VERDICT: CONFIRMED** (with a precision that sharpens, not weakens, the lever — and a
clean explanation of the bwv62.6 anomaly that *removes* it as a worry).

The re-grounding's central claim — *MuseScore drops the notated `<mode>` for empty
(0-fifths) key signatures, so the resolver gets `KeyMode::UNKNOWN`* — was previously proven
only at the resolver boundary (`declaredModeOrdinal=-1` [dump], dossier §1.2/§5.1). It is
now verified **at the source**, end to end:

**1. The exact site [code].** The MusicXML import reads `<mode>` for **all** fifths values:
`MusicXmlParserPass2::key()` maps `<mode>` → `key.setMode(KeyMode::…)`
(`importmusicxmlpass2.cpp:6074–6096`), with no fifths guard. That local `KeySigEvent` is
persisted **only** via `addKey()` (the two calls at `:6121`/`:6124` are its sole consumers).
And `addKey()` creates a `KeySig` element only when

```cpp
if (oldkey != key.key() || key.custom() || key.isAtonal())   // importmusicxmlpass2.cpp:5978
```

— a **fifths-only dedup that ignores mode**. For a piece-initial empty signature (`<fifths>0</fifths>`
with `<mode>major|minor`): `key.key()` = `Key::C` = 0; the in-effect default `oldkey` = `Key::C`
= 0; `key.custom()` is false (only `<mode>none` sets custom, `:6077`); `key.isAtonal()` is
false. So the condition is **false → no `KeySig` element is created → the mode that was just
read is discarded.** The resolver then reads `staff->keySigEvent(tick)`, which with no element
present returns a default `KeySigEvent` whose `m_mode = KeyMode::UNKNOWN` (`key.h:96`); the
resolver's switch sends `UNKNOWN` to `default: declaredMode = std::nullopt`
(`keyresolver.cpp:237`) → `declaredModeOrdinal = -1`.

This is mechanism **(a) "dropped at MusicXML import"** — precisely: *read, then discarded*
because the carrier `KeySig` element is suppressed by a fifths-only dedup. Named site:
**`addKey()`, `importmusicxmlpass2.cpp:5978`.**

> **PRECISION (matters for the Stage-4 fix).** The drop is not strictly "0 fifths" — it is
> "**any signature equal to the in-effect default key**." Because the default is C-major
> (0 fifths), only the *piece-initial* empty signature hits it. A mid-piece **return** to 0
> fifths after a non-zero key *would* create the element (`oldkey ≠ 0`) and retain its mode.
> For the constant-signature Bach chorales this is moot (the initial empty sig is the only
> one, so the mode is lost for the whole piece), but **the fix must target the dedup, not a
> bare `fifths == 0` test**, or it will miss/over-fire on key-change scores.

**2. The mode IS recoverable — 79/80, not "73 minus unknowns" [probe `zero_sig_mode_census.py`].**
Parsing the initial `<key>` block of all 353 corpus XMLs:

```
non-zero initial signature : 273
ZERO initial signature     :  80
   ... WITH <mode>          :  79   (recoverable — 54 minor, 25 major)
   ... WITHOUT <mode>       :   1   (bwv62.6 only)
```

So the keystone's load-bearing assumption — *the mode is recoverable for the zero-sig
stems* — **holds for 79 of 80**. The 349-region reach is **not** shrunk by absent tags;
only bwv62.6 lacks a `<mode>`, and it is the already-flagged anomaly (below). (The dossier's
"73" is the WiR-matched subset of these 80; same population, same story.)

**3. End-to-end confirmation [dump].** Two zero-sig stems that *do* carry the tag —
bwv153.9 (`<mode>major`) and bwv254 (`<mode>minor`) — both arrive at the resolver with
`notatedFifths=0, declaredModeOrdinal=-1`. The mode was present in the XML and is gone at
the resolver: `addKey` dropped it. Chain closed.

**4. bwv62.6 EXPLAINED — it is NOT a second mode-handling path [dump+code].** Direct dump
of region 0 (tick `[0,480)`): `notatedFifths=0, declaredModeOrdinal=-1, path="normal"` —
the *same* mechanism. bwv62.6 is a **mixed-signature** stem: its initial key block (`:78`)
is `<fifths>0</fifths>` with **no `<mode>`**, and it switches to `-2 major` (B♭) at `:637+`.
The dossier's cross-tab placed it in the `fifths≠0` column because its *predominant* notated
signature is −2, while its anchor detector measured *region 0*, which lands in the initial
empty span. **Correction to the dossier's "lone anomaly / possibly a different path"
framing:** it is the same `addKey` mechanism; its initial empty sig genuinely lacks a mode
in the source, so it was never in the recoverable-349 set anyway. The §1.2 correlation
("declared mode present iff signature non-empty") is intact.

**Keystone consequence:** the 349 structural lever **stands**; A-confirmed / B-as-fallback
(re-grounding §3) is **not** undermined. The fix design must use the dedup-aware framing
(point 1's PRECISION), and must source the mode (Task 5).

---

## Task 0 — instrument byte-identity: CONFIRMED green (not assumed)

**VERDICT: CONFIRMED.** The instrument `a4ae4a9203` did **not** perturb production; the
dump's §3 term-attribution is trustworthy.

- **Build:** no-op at HEAD (`ninja: no work to do`) — tree already built at `a4ae4a9203`.
- **`composing_tests` 505/505** [test]; **`notation_tests` 57/57** [test]; **pipeline
  snapshots 11/11 PASSED, 1 SKIPPED by design** (the `PipelineDivergenceCObservation`
  report needs `PIPELINE_OBSERVE_DIVERGENCE_C=1`) [test] — no golden refresh.
- **Production byte-identity is PROVEN BY CONSTRUCTION, not just observed [code].** The
  `f8c6b3932a..a4ae4a9203` production diff (`keyresolver.cpp` +26, `keymodeanalyzer.cpp`
  +59) is **entirely additive and `dumpOut`-gated**: both headers default `dumpOut = nullptr`
  (`keyresolver.h:95`, `keymodeanalyzer.h:508`); the dump block in `analyzeKeyMode` only
  reads `evaluations` + recomputes pure terms + sorts `dumpOut` (never touches `results`);
  the only un-gated additions are side-effect-free local copies (`notatedFifths`,
  `beforeMode`/`beforeFifths`). **All three production callers pass no dumpOut:**
  `regionanalyzer.cpp:307` (explicit `nullptr`), `:420` and `notationcomposingbridgehelpers.cpp:187`
  (the 6th arg is `prevResult`; `dumpOut` defaults null). The dump is reachable only via
  `batch_analyze --dump-key-candidates`.
- **Full Baroque sha256: `0 differ / 353 compared` [probe `byte_identity_full.sh`]**,
  against `tools/corpus/baroque` whose `corpus_manifest.json` stamps `git_hash:
  a652dc1ba7` — **genuinely before both `f8c6b3932a` and the instrument**. So this run is a
  true pre-instrument check *and* additionally confirms `f8c6b3932a`'s default output is
  byte-identical. (Independent corroboration: the git-tracked snapshot goldens were
  unchanged in the instrument commit and pass at HEAD — a pre-instrument empirical baseline
  on 11 scores incl. key resolution.)

No stop condition triggered.

---

## Task 4 — "key feeds chord emission" is CURRENT post-3.3: CONFIRMED

**VERDICT: CONFIRMED** (no correction; Stage 3.3 did not touch this path).

- The **resolved** per-region key flows into emission [code]: `resolveKeyAndModeRanked(...)`
  → `ranked.front()` = `localKey` (`regionanalyzer.cpp:418–423`) → `localKeyFifths` /
  `localKeyMode` → **`analyzeChord(tones, localKeyFifths, localKeyMode, …)` at
  `regionanalyzer.cpp:454`** (also `inferNextRootPc:439`,
  `refineSparseChordQualityFromKeyContext:469`, `applyTonicPriorToSparseChord:471`).
- The key enters the **scoring** [code]: `analyzeChord`'s `keyMode` "determines the tonic
  and diatonic scale used for degree assignment and diatonic scoring"
  (`chordanalyzer.h:810–811`); and `basisIndep` is explicitly defined to include
  "bassIndependentContextualBonuses (**diatonic root**, root continuity, resolution bias)"
  (`scoring_model.md:114`). The key-dependent `diatonicRootBonus` (default 0.30) is
  **literally inside `basisIndep`** (`score = (basisIndep + bassDep) × cf × af`).
- **Stage 3.3 (`548adb7b2e`) did not change this.** It migrated the five *temporal/inversion*
  signals (resolutionBonus + the four inversion bonuses) into the competition pipeline,
  byte-identically (commit msg + the byte-identity gate). The key input and the diatonic
  scoring were untouched.

So the re-grounding's framing — *Stage 4 ends the byte-identity era because the resolved key
feeds `analyzeChord` → chord output* — is **accurate and current**. Changing the resolved
key (the import fix) **will** change the diatonic scoring → chord emission. Stage 4 IS a
behavior change on the chord axis.

---

## Task 5 — layer separation for the Stage-4 fix (design input; not implemented)

**Premise correction [code].** "Composing stays notation-agnostic" is only half true.
`composing_analysis` **PUBLIC-links `engraving`** (deliberate since Iter 67 —
`src/composing/CMakeLists.txt`), and the resolver reads `mu::engraving::Score` /
`KeySigEvent` / `KeyMode` **directly** (`keyresolver.cpp:208,216,219,226`). Composing is
**engraving-coupled by design**; it is *importexport-* and *notation-*agnostic (no
`importexport/musicxml` dependency — only test fixtures reference `.musicxml` paths). The
relevant dependency rule is therefore **"composing must not depend on importexport/notation
internals,"** not "composing must not touch engraving."

**Where the mode is, at fix time.** The drop is in `importexport/musicxml addKey` — *below*
composing. By the time **any** analysis runs (the notation bridge **or** `batch_analyze`),
the score is already imported and the mode is **gone from the engraving model** (empirically:
the dump via `batch_analyze`'s own import shows `declaredModeOrdinal=-1`). Neither caller can
read it back from the imported `Score`.

| | Option (b) — fix engraving keysig import (`addKey`) | Option (a) — read `<mode>` in the bridge → pass to resolver |
|---|---|---|
| Composing change | **none**; reads the now-correct `keySigEvent().mode()` | a new `optional<KeySigMode>` data param on `resolveKeyAndModeRanked` |
| New composing dependency | **none** (already depends on engraving) | **none** (receives a value; stays importexport/notation-agnostic) |
| Blast radius | **broad** — rendering, layout, MusicXML round-trip export, **all** score consumers | **narrow** — analysis only |
| Cost / caveats | outside the composing autonomous zone (needs approval); risk a spurious empty-sig keysig renders/exports; engraving-wide regression | the mode is gone post-import → must **re-source** from the original MusicXML (notation→importexport re-parse); **gap** for native/non-MusicXML scores; **`batch_analyze` is a separate caller** — the sourcing can't live "in the bridge" alone |

**Verdict.** *Neither* option forces **composing** to depend on notation/importexport
internals, provided the resolver receives the declared mode as a plain data parameter
(in-layer — composing already takes engraving types). Option (b) is the true root-cause fix
and is layer-cleanest *for composing* (zero composing change), but it is an
engraving/importexport change with a large blast radius and is outside the composing
autonomous-edit zone. Option (a) keeps the blast radius small and composing clean, but its
"**in the bridge**" framing is **incomplete**: `batch_analyze` is a separate consumer that
also lost the mode, so the mode-sourcing must be **shared**, not bridge-local; and it has a
feasibility gap for non-MusicXML scores.

**Design recommendation (OQ-4, build-time call — not implemented here):** the
minimal-blast-radius, layer-clean shape is to have the **engraving import retain the mode**
(even when the fifths-dedup suppresses the *visible* element — e.g. store it without forcing
a printed keysig) so composing reads it unchanged; or add the `optional<KeySigMode>` override
fed by a **single shared mode-sourcing step** both callers use. A bare relaxation of the
`addKey` dedup that *creates* a visible empty-sig keysig is the highest-risk variant
(rendering/export side effects) and should be gated accordingly.

---

## Task 3 — music21 provenance (OQ-V1): CONFIRMED, and ALREADY recorded (task premise is stale)

**VERDICT: CONFIRMED.** Version = **music21 v.9.9.1**.

- **[probe]** The `.xml` carries `<software>music21 v.9.9.1</software>`; the manifest stamps
  `"music21_version": "9.9.1"`, populated by `run_bach_preset.py:_detect_music21_version()`
  reading the `.xml` `<software>` tag (`:70`,`:118`).
- **The `.music21.json` carries NO internal version field** (top-level keys: `source,
  detectedKey, keyConfidence, regions, corpusName`). So the *generator* version of the JSON
  ground truth is recorded **by inference** (same April-2026 campaign, `<encoding-date>2026-04-05</encoding-date>`),
  a documented freeze-by-fiat — not a self-describing stamp.
- **Already committed [code].** `REPRODUCIBILITY.md:80–92` pins v9.9.1 (audit C2), with the
  honest caveats already present: the `.json` "is from the same generator," the manifest copy
  is "informational — not validated," and the `.music21.json` are "canonical as-committed
  … regenerating is a deliberate re-baseline." **The task's premise that this is "recorded
  nowhere committed" is itself now stale** — the corpus-hygiene pass closed it.

**No new edit required.** The existing record is accurate and honest. (A future tooling
improvement — stamp `music21.__version__` *into* the `.music21.json` at generation so the
ground truth is self-describing — is noted as a backlog nicety, not a gap blocking the
re-grounding.)

---

## Task 2 — cross-corpus numbers: QUARANTINED (and the staleness framing is CORRECTED)

**VERDICT: was QUARANTINED → now RESOLVED (CONFIRMED after HEAD regen).** The June-3
`.ours.json` *were* genuinely binary-stale (so quoting them as "current" was unjustified
without re-verification — correctly caught), **but a fresh HEAD regen confirms the aggregate
holds:** non-Bach root_err **50.7%**, rn_agree **27.4%** (was 27.6%). The "~2× harder than
Bach" claim **survives at HEAD**.

- **The metric is NOT the staleness [probe].** Re-running `compare_rn --cross-corpus
  tools/reports/live_20260603` at HEAD with the committed F-1/F-2-fixed metric reproduces
  the cited aggregate **exactly**: `rn_agree 27.6% (16906/61233)`, `root_err 50.7%
  (31023/61233)`, `root_agree 49.3%`, `key_disagree 15.2%`. So the F-1/F-2 fixes did **not**
  move the cross-corpus aggregate. **This corrects the roadmap's "pre-F1-metric stale"
  framing (rows 2.2/5.2):** the metric *reproduces* — the staleness is elsewhere.
- **The OUTPUT is the staleness [probe].** The `live_20260603` `.ours.json` are **June-3
  binary outputs** (mtime Jun 3 17:28; June 3 predates `a652dc1ba7`, so real output-changing
  commits land in the window). Spot-regen at HEAD (`--preset Standard`): **5 of 6 scores
  DIFFER** (corelli op01n01a same; op04n12c, op01n01b, mozart K279-1, K279-2, chopin
  BI105-2 all differ). The op04n12c diff is **substantive** — 220 changed lines incl. a
  winner flip `Bm/D (i6) → D (III)` (rootPc 11→2, Minor→Major, bassIsRoot false→true).
- **Per-corpus (June-3 data, current metric):** corelli root_err 55.0%, mozart 51.5%,
  beethoven 51.7%, tchaikovsky 53.2%, bach_suites 53.5%, grieg 49.1%, schumann 48.9%,
  chopin 41.6%, dvorak 40.8%; **cpe_bach = 0 movements** (texture too thin — known).

- **HEAD regen (definitive) [probe `regen_xcorpus_head.sh` → `tools/reports/live_head_verify`].**
  Full regeneration at HEAD (`--preset Standard`, 10 corpora, 520 movements) + `compare_rn
  --cross-corpus`:

  | quantity | June-3 (stale data) | **HEAD regen** | Δ |
  |---|---|---|---|
  | matched regions | 61233 | **62110** | +877 |
  | rn_agree | 27.6% | **27.4%** (17003/62110) | −0.2pp |
  | root_agree | 49.3% | **49.3%** (30620/62110) | 0 |
  | root_err | 50.7% | **50.7%** (31490/62110) | 0 |
  | key_disagree | 15.2% | **15.3%** (9488/62110) | +0.1pp |

  Per-corpus root_err at HEAD: corelli 54.9%, tchaikovsky 53.8%, bach_suites 53.2%, mozart
  51.9%, beethoven 51.8%, grieg 49.1%, schumann 48.0%, chopin 41.5%, dvorak 40.7%; cpe_bach
  **0 matched** (texture too thin — known). All within ~1pp of June-3.

  **Reading:** the per-score winner flips (5/6 spot-differed) **wash out in aggregate** — the
  non-Bach difficulty profile is essentially identical at HEAD. So: the June-3 data was
  genuinely stale and should not have been quoted as current *without this check*; having
  done the check, the numbers **are now verified and they hold**. The re-grounding's
  "~2× harder than Bach" (non-Bach root_err **50.7%** vs the Bach S2 ~10%) **stands at HEAD**.

---

## Task 6 — doc currency (staged, NOT committed — per the "Held for Cowork" rule)

1. **`decoder_design.md §11` Δ=+7a erratum — APPLIED [code].** Added an ERRATUM block at the
   top of §11 superseding the falsified "Stage-3 wider beam should fix / **low-scoring
   transient**" verdict on the **Δ=+7a** and **C2/bwv320-class** rows (the transient is the
   *highest*-scoring node; the continued-root path is the genuine global optimum a decode
   finds exactly as greedy does — greedy 5.775 > correct 5.600 on bwv102.7; Δ=+7a → Stage 5;
   the C2 example is the dead Gate-R-fixed bwv320 m27 = Δ=+7b instance). The block also voids
   the §12 Q2 ratification's "Δ=+7a depends on forward edges" rationale clause. This was the
   **standing queued rider** explicitly named in COWORK_HANDOFF (lines 481/601/610/620).
2. **`COWORK_HANDOFF.md` ledger — CLOSED.** Line 481's "needs erratum (next doc pass)" now
   carries an APPLIED note; the trailing "still queued" mentions in older dated entries are
   left as historical log.
3. **Rider queue — CONFIRMED landed, CLOSED [code].** Commit `4f1754c26c` ("docs: pin
   Baroque-13 identity set; freeze-anchor + file-map riders") contains all three: CLAUDE.md
   + BUILD_AND_TEST.md Baroque-13 identity set, REPRODUCIBILITY.md freeze-anchor,
   ARCHITECTURE.md `sectionanalyzer` file-map row + Pass-0 sentence.
4. **roadmap / STATUS already current [code]** on the META-PRINCIPLE (roadmap:73),
   beam-falsification (roadmap row 3.2:160; STATUS:8), key-path (roadmap:80), and the
   cross-corpus stale-marking (roadmap 137/196). **Roadmap NOT edited — judgment call,
   flagged.** Its "re-measure the cross-corpus rn numbers (27.6%/**53.8%** are pre-F1-metric,
   stale)" cites a "53.8%" that does **not** match the `compare_rn` root_agree (49.3%) — it is
   a *different-lineage* number (the 37639-region DCML root-correct baseline from
   `project_dcml_baseline_head.md`, not the 62110-region compare_rn cross-corpus). Editing it
   blind would conflate two metrics. The authoritative HEAD re-measurement (50.7% root_err /
   27.4% rn_agree / 49.3% root_agree, 62110 regions) is recorded **in this report** (Task 2);
   the roadmap's "re-measure at Stage 5" marking is left in place pending a Stage-5 owner who
   can disambiguate the 53.8% lineage. Two precisions for that owner: (i) the staleness is
   *binary-output*, not *metric* (the metric reproduces); (ii) the re-measure is now done and
   the aggregate is stable.
5. **`COWORK_HANDOFF §5.1` "import root-site not verified" — now RESOLVED** by Task 1
   (`addKey:5978`). Flagged here; the §5.1 caveat in the key-emission dossier and back-half
   draft can be marked resolved.

**Commit policy.** The standing `feedback_held_for_cowork.md` rule (written today) is
unambiguous: on Cowork doc work, `git add` then **STOP at staged state** until an approval
file or explicit go-ahead. There is **no approval file** for this task
(`cc_instruction_stage3_1b_approval.md` is for a different instruction). The doc edits are
therefore **staged, not committed** — the ready commit is presented for Cowork to land.
Files: `docs/decoder_design.md`, `COWORK_HANDOFF.md`, `cc_foundations_verification_report.md`
(this file). Never `muse`.

---

## THE GATE — two lists

### ✅ Facts the re-grounding CAN stand on (CONFIRMED at HEAD)
1. **Keystone (Task 1):** the empty-signature declared-mode drop is real and root-caused
   (`addKey` fifths-only dedup, `importmusicxmlpass2.cpp:5978`); the mode **is recoverable**
   (79/80 zero-sig stems carry `<mode>`). The **349 structural lever stands**; A-confirmed /
   B-as-fallback is not undermined.
2. **Instrument trust (Task 0):** byte-identical in production (proven by construction + 0/353
   sha256 vs a genuine pre-instrument baseline + unchanged passing snapshot goldens). The dump
   §3 term-attribution is sound.
3. **Stage-4-is-a-chord-behavior-change (Task 4):** the resolved key feeds `analyzeChord`'s
   `basisIndep` (`diatonicRootBonus`) at HEAD; 3.3 was byte-identical and left this path intact.
4. **music21 provenance (Task 3):** v9.9.1, recorded in committed `REPRODUCIBILITY.md`.
5. **Bach gate-set numbers** (S2=1032, 349/127 split, 13/7 BIR identity sets) are Bach-measured
   and reproduce at HEAD.
6. **Cross-corpus difficulty (Task 2) — CONFIRMED after a HEAD regen.** non-Bach root_err
   **50.7%** / rn_agree **27.4%** (62110 regions, regenerated at HEAD); the "~2× harder than
   Bach" claim stands. *Caveat below: the previously-cited figures rested on stale data.*

### ⚠ Facts CORRECTED / QUARANTINED (the re-grounding must reflect these)
1. **Cross-corpus data hygiene (Task 2) — CORRECTION (resolved).** The June-3 `.ours.json`
   the dossiers quoted were **binary-output-stale** (5/6 spot scores differ substantively at
   HEAD) — so the roadmap's "pre-F1-metric stale" diagnosis is wrong (the *metric* reproduces
   the numbers exactly; the *output* had drifted). They should not have been quoted as current
   without re-verification. **Resolved by regen:** the aggregate is stable (50.7%/27.4%), so
   the conclusion survives — but the lesson stands: re-generate cross-corpus, don't quote the
   June-3 dirs. (Roadmap edit deliberately *not* made — see Task 6 note 4: its "53.8%" is a
   different-lineage number; flagged, not blindly overwritten.)
2. **Keystone precision (Task 1) — CORRECTION to framing.** The drop is "default-key-match"
   (a fifths-only dedup), **not** literally "0 fifths"; the fix must target the dedup, not a
   `fifths==0` check. **bwv62.6 is the SAME mechanism, not a second path** — corrects the
   dossier's "lone anomaly / possibly different handling" wording.
3. **Layer premise (Task 5) — CORRECTION.** "Composing stays notation-agnostic" is only true
   w.r.t. importexport/notation; composing already depends on **engraving**. Option (a)'s
   "in the bridge" framing is incomplete (`batch_analyze` is a separate caller).
4. **decoder_design §11 Δ=+7a verdict — CORRECTED** (erratum applied this run).

### Stop conditions
- **None of the report's stop conditions fired.** Task 1 did **not** correct the keystone
  downward (it confirmed it and *strengthened* the recoverability evidence to 79/80). No
  "current" doc fact that a build would have relied on was found contradicted (the one stale
  *quantitative* fact — cross-corpus — was already flagged stale in the roadmap and is not a
  build input). No layer violation is forced by either fix option. No fix was implemented.

---

*Method note: Tasks 0/2 used the committed corpus + `/c/tmp` byte-identity & spot scripts;
Task 1 used `zero_sig_mode_census.py` + the `--dump-key-candidates` instrument; Tasks 3/4/5/6
are `[code]` reads. The cross-corpus HEAD regen is the only long-running item; its result is
slotted above.*
