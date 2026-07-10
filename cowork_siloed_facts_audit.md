# Siloed Analyzed Facts — the Fact-Publication Audit (user-directed, 2026-07-10)

> **Cowork, session 36.** User question after the spelling finding (OI-15): *"what else is
> analyzed and recognized but not for anybody to consume, but only for specific use?"*
> Read-only code sweep of `src/composing/`. **The through-line: the shared cross-layer
> surfaces (`ChordAnalysisTone`, `HarmonicRegion`/`AnalyzedRegion`, `FunctionSlice`) carry
> root/quality/bass/key but are VOICE-BLIND, SPELLING-BLIND, and MEMBERSHIP-BLIND** — every
> voice-leading, spelling, and NCT fact is either recomputed per consumer or stranded on a
> producer-local struct the layers above L4 never see. This is precisely the gap the L5
> engagement design §3.2 names as the missing load-bearing selection channels. Register rows
> OI-72…OI-80; design ownership: the E4 carry/surface design (#7 — facts belong to the fact
> layer; publication is an architecture concern, not a patch).

Severity: **TRAPPED** (dies inside a function) · **SILOED** (surface exists, ≤1 consumer) ·
**DIAGNOSTIC-ONLY** (no production consumer) · **DUPLICATED** (recomputed per consumer).

| # | fact | computed | consumed today | needed by (design) | severity |
|---|---|---|---|---|---|
| 1 | Per-note NCT/embellishment structure: `StepwiseSignals` (suspension, stepIn/stepOut, leapIn/leapOut, per voice) | `chordslicedecoder.cpp:260-318` (.cpp-local struct) | ONLY the decoder's own membership ladder | L5 selection voice-leading evidence; pedal upper-voice reads | **TRAPPED** (OI-72) |
| 2 | Membership verdict `chordTonePcs`/`nonChordTonePcs` + implausibility | `classifyMembership`, written to `SliceChord` | ZERO external readers — `FunctionSlice` never copies it; dies at L4→L5 | L5 joint-consistency; pedal bass-as-NCT test | **SILOED-to-none** (OI-73) |
| 3 | Per-pc spelling `tpcForPc` window snapshot / `FocalNote.tpc` | `chordanalyzer.h:529`; `chordslicedecoder.h:471` | chord layer internally; ONE mechanism (the symmetric pin) | spelling = load-bearing channel #2 (§3.2); never lifted above L4 | **SILOED** (= OI-15, the headline case) |
| 4 | `HarmonicRegion.keyAlternatives` (carried key menu) | `regionanalyzer.cpp:550/1031/1050` | production ZERO — tests + `--dump-fullspine`; struct comment: "has NO consumer — it exists for Layer 5" | the L5 carry contract's key input | **DIAGNOSTIC-ONLY** (OI-75) |
| 5 | `HarmonicRegion.keyConfidence` (D-L3a sequence margin) | same sites | production ZERO — diagnostics | the L5 override-bar input; THE declared L3 confidence | **DIAGNOSTIC-ONLY** (OI-75) |
| 6 | Key runner-up (in-analyzer gap; `keyModeRunnerUp`) | `keymodeanalyzer.cpp:764`, `keymodesequence.cpp:222` (used for sigmoid, discarded); serialized only by batch tool | grading harness only | — | **TRAPPED** / DIAGNOSTIC-ONLY |
| 7 | Cadence detections — (a) production `detectCadences` transient, recomputed per emit path, not stored on regions; (b) L5 `FunctionalCadence` inside the dormant stack | `sectionanalyzer.h:98-129`; `functioncadence.*` | (a) notation bridges only; (b) dormant L5 | cadence tonic-vote channel (§3.2) | **SILOED/transient** (OI-76) |
| 8 | `bothLicensed` §15-13 telemetry | `functionresolver.cpp:223/244` | `--dump-fullspine` only (dormant surface) | the Stage-5 family-4 fit | DIAGNOSTIC-ONLY (by design, OK) |
| 9 | `RawFanoutSummary` + the uncapped `gateCtx.rawCandidates` behind it | `chordanalyzer.h:598`; commit sites `regionanalyzer.cpp:1054/1250/1442` | `--dump-fanout` only; the cap-of-3 at `harmonicfunctionlayer.cpp:521` discards the actual readings | the L5 selection's full graded distribution (#12) | **DIAGNOSTIC-ONLY**; readings lost (rides OI-9) |
| 10 | Metric position: region-level IS shared (`FunctionSlice.metricWeight` ✓); per-note beat weight decoder-local | `metricweights.h:74-97`; `FocalNote.metricWeight` | region level available; per-note only in membership | fine-grained salience for selection/pedal | partial — per-note **SILOED** |
| 11 | Bass/inversion VERDICT (is-bass-a-chord-tone / inversion) | `function::bassIsTemplateChordTone` — shared function | recomputed at ~60 call sites / 20 files from raw (root,tiePriority,pc); no cached verdict on any surface | channel #1 (load-bearing) | **DUPLICATED** (OI-77) |
| 12 | `declaredMode`/KeySig mode from import | key path params | key path exclusively; chord diatonic bonus reads only the inferred key | general evidence prior | **SILOED** (OI-78) |
| 13 | `isPedalPoint`/`pedalBassPc` | `chordpostpasses.cpp:275`; on `ChordIdentity` | ONE consumer: `notationcomposingbridge.cpp:1202-1207` (lossy root redirect) | pedal-annotate design wants it as a carried slice attribute | **SILOED** (rides OI-4) |
| 14 | Score annotation inputs (chord symbols / RN / Nashville) | NOT computed — `analysistypes.h:394-411` TODO flags | nothing | declared input priors | **TRAPPED**/unbuilt (OI-80) |
| 15 | Best different-root scan (confirmation margin) | 4 sites (FQ-1): `chordpostpasses.cpp:262`, decoder `:~949`, `harmonicfunctionlayer.cpp:539`, carry-side | each consumer re-rolls it | one carry-served primitive (#6) | **DUPLICATED** (= OI-11) |
| 16 | Pedal confidence sigmoid constants (midpoint 2.0 / steepness 1.5) | inlined `chordpostpasses.cpp:271`, duplicating prefs; S10: emission sigmoid written in two files | — | one named constant home | **DUPLICATED** (OI-79) |
| 17 | Voice/staff identity | `NoteEvent.staff/voice` (L1 ✓) | **dropped at `ChordAnalysisTone`** (`analysistypes.h:134-163` carries neither); only `FocalNote.voice` re-reads it, for the stepwise test | pedal "upper-voice-conditioned" reads; any voice-aware evidence | **structural** — the shared tone surface is voice-blind (OI-74) |

**Reading (labeled inference, consistent with the design docs):** items 1/2/3/17 share one
root cause — the L1→L4 shared tone surface drops voice and spelling, and the L4→L5 boundary
(`FunctionSlice`) drops membership — so each higher layer that needs these facts either cannot
get them (L5 selection channels, the pedal reader) or a producer re-derives them locally (the
pin, the membership ladder). **The fix is a surface/carry design decision at E4** (which
fields the shared surfaces publish — #7: facts to the fact layer, one publication per fact,
consumers read), NOT per-site patches. OI-14/OI-15's spelling options and the §9.2
distinct-root carry (OI-9) are instances of this one design question.

*Cowork, session 36. Method: targeted read-only sweep (grep + struct inspection) over
`src/composing/`; consumers counted by grep; design needs cited to
`cowork_layer5_engagement_design.md` §3.2 and the pedal-annotate design. Register: OI-72…OI-80.*
