# The backlog triage pass — report

> **CC, 2026-07-13.** Executing `cc_instruction_backlog_triage.md` (Cowork, 2026-07-12). The
> register's weakest tier — the rows whose recorded plan was only "triage: verify this is still
> real, then assign or supersede" — is eliminated. **Every such row now carries a checked verdict
> from the closed set** (SUPERSEDED / STILL REAL — ASSIGNED / STILL REAL — USER DECISION /
> CLOSED AS DECIDED). No row keeps the verdict "triage later".
>
> **Read-only in substance.** No source file changed, no constant tuned, no golden refreshed, no
> corpus or ground-truth file written. `tools/robust_stop/` and `tools/corpus/` were written by
> nothing. The one authorized action beyond reading was a **build + the three test suites at HEAD**
> (`setup_and_build.bat` reported `ninja: no work to do` — the binaries were already at HEAD source),
> used to convert two claims from memory into measurement.
>
> **HEAD** `3966502265` (the Task-0 register commit). Corpus `c50002fee1`. Ancestry against
> `STATUS.md`'s newest hash `26f53b5ba2` confirmed (`git merge-base --is-ancestor` → 0).

---

## 0. What was measured, not remembered

| Instrument | Result |
|---|---|
| `setup_and_build.bat` at HEAD | `ninja: no work to do` — binaries already at HEAD source |
| `composing_tests.exe` | **1101/1101 pass**, 2 disabled |
| `notation_tests.exe` | **53 pass, 4 SKIPPED** |
| `pipeline_snapshot_tests.exe` | pass, 1 skipped (env-gated), 3 disabled (perf/sweep) |

The four notation SKIPs are the evidentiary core of this session — see §2, OI-59 / OI-148.

---

## 1. The verdict table

| Row | The claim it carried | Check performed | Evidence | Verdict |
|---|---|---|---|---|
| **OI-47** | STATUS.md submission-era sections contradict the governing docs | Read the four sections at HEAD | `STATUS.md:570` (Current State, BIR 25/16 at `:585`), `:2302` (Known Gaps), `:3721` (Post-submission priorities), `:3730` (Future Architectural Considerations) — all present, all contradicting the governing robust-unit stop | **STILL REAL — ASSIGNED.** Its *triage* half is DISCHARGED by this session (every §G row is now verdicted); the *banner* half remains |
| **OI-48** | `backlog_chord_track_flag.md` referenced by two live docs, file DOES NOT EXIST | Resolved the path; checked the substance at code | The file **exists** — as a Claude Code memory (`~/.claude/projects/c--s-MS/memory/backlog_chord_track_flag.md`, 1017 bytes), never a repo file. Referenced from `STATUS.md:3744`; cited as the canonical DT-12 example at `DEFECT_TYPES.md:24`. Substance is live: `regiontonecollector.h:73` `isChordTrackStaff()` is still name-based | **STILL REAL — ASSIGNED** (re-point the reference; nothing is lost) |
| **OI-52** | S20 root-equality helper (trivial; "likely not worth it" — decide and close either way) | Grepped the comparison sites; re-read the ratified adjudication | Still written out at `a8_rebaseline_measure.py:148`, `compare_analyses.py:243-244`, `compare_rn.py:352/370/474`. **The row's status is stale**: the A6 verdict ("add the one shared helper at the next instrument touch") was *already user-ratified* on 2026-07-10 under OI-42 (`cowork_adjudication_dossier.md:78-84`) | **STILL REAL — ASSIGNED** — the "decide either way" framing is discharged; see §3 for the justification |
| **OI-53** | Tonicization classifier (V/V, V/ii) **wired, not implemented** | Read the code myself at both paths | **Refuted.** A tonicization classifier IS implemented and IS live: `chordsymbolformatter.cpp:901-940` emits `V7/x` and `vii°/x`, fed unconditionally by `backfillNextRootPc` (`regionanalyzer.cpp:284-290`, called at `:1465`), user-reachable via `formatRomanNumeral` (`notationcomposingbridge.cpp:492/809/944/1159`, `notationcontextmenumodel.cpp:87`). A richer version sits dormant in the certified L5 machinery (`functionrelationallabel.cpp:215`, `functionmodulation.cpp:26`, `tonicizationlabeler.cpp:64`) | **SUPERSEDED** |
| **OI-54** | Pedal-point calibration needs corpus evidence | Re-confirmed the absorbing rows | OI-4 and OI-38 both OPEN and both carry the pedal-dense corpus | **SUPERSEDED** (merge re-confirmed; stays listed until OI-4/OI-38 close, per the register's own convention) |
| **OI-55** | Ninth-detection gap (melody/harmony conflation) | Read the live ninth path and the dormant discriminator | **Still present, exactly as described.** The live ninth verdict is a bare pitch-class weight cutoff (`chordanalyzer.cpp:302-314`; `kExtensionThreshold=0.20` at `:129`) over one 12-bin histogram, with a `0.1` floor (`:1081`) — no voice, no line, no non-chord-tone verdict. The discriminator exists but is **dormant**: `ChordSliceDecoder::classifyMembership` (`chordslicedecoder.cpp:794-855`), whose own comment names this bug — *"the passing D heard as Cadd9's ninth"* (`:825`) — with a test on the dormant path (`decode_chord_tests.cpp:658`). Live tests confirm the verdict is a tunable cutoff: the same voicing flips on/off with the threshold alone (`chordanalyzer_tests.cpp:2218` vs `:2243`) | **STILL REAL — ASSIGNED** → §B, the L4 decoder engagement + the NCT-filter lever (OI-68); the membership verdict's publication is OI-73. Gate: E4 (#8) |
| **OI-56** | `auto_review.py` designed, not implemented | Globbed the repo; read the design; enumerated what now exists | No such file anywhere. Designed at `ARCHITECTURE.md:5717-5770` in three modes. **Mode 3** (score against ground truth) is over-served by the measurement chain. **Modes 1/2** (judge *without* ground truth — its stated reason for existing, `:5721-5725`) have **no code on master** (zero `anthropic\|openai\|llm judge` hits in `tools/` + `src/`); `docs/llm_triage_design.md:3` — "Discussion only. No implementation committed." An implementation exists on the **unmerged** `llm-triage` branch (`git merge-base --is-ancestor llm-triage master` → **1**; last commit 2026-05-14) | **STILL REAL — USER DECISION** (§4) |
| **OI-57** | Corpus QA systematic pass (84-score registry era) | Counted the registry and the disk myself | **Half superseded.** The ground-truth corpora now have real integrity discipline (`run_bach_preset._write_manifest` fingerprints `.ours.json` *and*, since OI-124, the paired `.music21.json`; `validate_corpus_dir` refuses stale/foreign/incomplete dirs; `tools/tests/test_snapshot_sources.py` pins source bytes). **NOT superseded:** `tools/extra_scores_registry.json` holds **140 entries** (jazz 104 + piazzolla 6 + steelydan 23 + snarkypuppy 7; `_updated: 2026-04-24`) against **163 score files on disk** under `tools/extra scores/` → **23 unregistered**, including **all 20 `hiromi/` scores** that `docs/score_inventory.md:33` designates the LLM-triage corpus. No tool validates this registry | **STILL REAL — ASSIGNED** (rescoped) → §D, owner: the corpus-onboarding event (OI-38) |
| **OI-58** | Known-Gaps block (6 sub-items) | Each checked at code — see §2 | 2 superseded, 1 re-filed, 3 still real | **SPLIT** — see §2 |
| **OI-59** | Corelli regressions + 4 deferred notation tests + chopin_bi105 cascade | **Built and ran the suites at HEAD**; read the goldens and expectations | All three original claims are dead — see §2. But the *count* "4 deferred tests" coincidentally still holds, for an **entirely different set with a newer root cause** | **SUPERSEDED** + a new row (**OI-148**) for the 4 current xfails |
| **OI-60** | Blocking trio: chord-symbols-as-input; declaredMode soft-boost; implode chord-track gaps | Read all three at code | All three fixed — see §2 | **SUPERSEDED** |
| **OI-61** | Future Architectural Considerations (6 items) | Read the list; checked two against the register | Hold still right, with two dedupes — see §5 | **HOLD CONFIRMED** (moved to §H) + one item promoted via OI-74 |
| **OI-62** | Tuning §11.3a–f documented-not-implemented | Read the code | **Confirmed at code.** `computeSusceptibility` (`notationtuningbridge.cpp:510-520`) returns `Free` for *all* non-anchor notes — *"Duration-based and context-based classification is a future addition… All non-anchor notes are Free for now"* (§11.3c). No `TuningSessionState` and no voice-role type anywhere in `src/` (§11.3d, §11.3b). The six gaps listed at `STATUS.md:2106-2115` are accurate | **STILL REAL — USER DECISION** (§4) |
| **OI-71** | Roadmap 0.1 doc pass (stale `explorationMode` refs; untracked audit doc) | Resolved all three claims | **All three discharged.** `docs/layer_architecture_audit.md` **is tracked** (committed at `7bc1609159`, 2026-06-10, *"docs: consolidated roadmap + architecture-review updates (Stage 0.1)"*); `explorationMode` occurs **0** times in it; the 3 remaining occurrences in `ARCHITECTURE.md` (`:1564/:1570/:1856`) are accurate *historical* notes explaining the rename to `ScoringPhase`, not "as-live" references. The roadmap itself marks Stage 0 COMPLETE citing that commit (`docs/implementation_roadmap.md:271`) | **SUPERSEDED** — a row left open for work finished five weeks ago |

---

## 2. The three rows that needed the suites and the score data

### OI-58 — the Known-Gaps block, sub-claim by sub-claim

| # | Sub-claim | Check | Verdict |
|---|---|---|---|
| 1 | Tone weights 1.0 | `analysistypes.h:137` declares `weight`. It **is** populated on the region path (`regiontonecollector.cpp:384`, duration × metric weight) but left at the `1.0` default on the single-tick `buildTones` path (`regiontoneprimitives.cpp:112-120`, used by the status-bar bridge). **Nothing** populates it from dynamics/velocity — `NoteEvent` carries no velocity field at all (`note_model.cpp:51-66`) | **STILL REAL, restated** — "never populated, always 1.0" is inaccurate; the true gap is *duration × metric only, never dynamics; and the single-tick path defaults to 1.0* |
| 2 | Tie re-split | The original text is about **intonation retuning**, not analysis: `notationtuningbridge.cpp:1218` — one non-partial tie on *any* note skips the **whole chord** for splitting. The analyzer has **no** tie defect (`note_model.cpp:45-46, 57-60, 181-192` — tie continuations skipped, exactly one onset per tied group) | **MIS-FILED** → re-filed under the tuning row (OI-62) |
| 3 | Cadence labels English | Raw literals `"PAC"/"PC"/"DC"/"HC"` at `sectioncadencedetection.cpp:104/106/110/137`, written verbatim to the score at `notationcomposingbridge.cpp:1244`. Zero `qtrc\|mtrc\|TranslatableString\|tr(` in all of `src/composing/` | **STILL REAL** |
| 4 | MusicXML sus export bug | **Fixed in this fork** at `exportmusicxml.cpp:9040-9042` (commit `70e679e819`) — the upstream bug is an index-assign into an empty String, so the degree-text guard never fires. **Not regression-locked** (no C9sus2 export test) | **SUPERSEDED** (fix landed; missing test carried as residue) |
| 5 | Piano-pedal decay model | Sustain-pedal tails **exist** but apply a **flat** 0.3 discount (`regiontonecollector.cpp:316-341`; `pedalTailWeightMultiplier = 0.3` at `analysistypes.h:325`) — no decay term, though the codebase *has* a decay primitive (`shv::timeDecay`) used only for span windows | **STILL REAL** |
| 6 | Rampageswing walking bass | **Refuted.** It is a 36-file **horn-only** big-band corpus (`tools/corpus_rampageswing_full/`) — a horn-only chart has no bass part, so walking-bass dilution cannot be the mechanism. The later `--inject-written-root` experiment raised agreement **39.8 % → 98.3 %** (`ARCHITECTURE.md:2036/2132`, `STATUS.md:1494-1500`), diagnosing an **absent** root/bass — the opposite failure | **SUPERSEDED** (description refuted) |

### OI-59 — measured at HEAD, and the discovery underneath it

**Claim 1 — Corelli "Gm vs G m1 b3": FIXED.** The expectation was reverted to `"G"` exactly as
`STATUS.md:646` prescribed — `notationimplode_tests.cpp:1165` `{ 1, 960, "G", "Cm", true }`, with the
sibling m10 b3 correctly *keeping* `"Gm"` (`:1173`). Both formerly-failing Corelli implode tests are
active and passing at HEAD.

**Claim 2 — chopin_bi105 segmentation cascade: NEVER TRIGGERED.** It was only ever an *indirect
consequence of landing* the deferred key-confidence-gated dominant-quality fix — which was never
landed. The golden `chopin_bi105_op30_2.json` shows tick 4800 as one unsplit `F#m` region (no `Bm`
at the head of `[4800, 6240)`). **Carried forward (#12):** the latent fragility returns if that
specific fix is ever re-attempted → recorded as a standing caution at **OI-70**.

**Claim 3 — "4 deferred notation tests": the count coincides, the tests do not.** Measured at HEAD:
`notation_tests` = **53 pass, 4 skipped**. The four are:

1. `Notation_ImplodeTests.MozartK279OpeningPrefersCMajorOverFLydian` (`notationimplode_tests.cpp:731`)
2. `Notation_ImplodeTests.PopulateChordTrackEmitsCadenceMarkersOnCorelli` (`:1708`)
3. `NotationInteractionHarmonyPinning.BehaviorSnapshot_RomanNumeral` (`notationinteraction_harmony_pinning_tests.cpp:211`)
4. `NotationInteractionHarmonyPinning.BehaviorSnapshot_Nashville` (`:265`)

All four are `GTEST_SKIP()` xfails charged to **one** root cause — the key-emission regression from
`a6b08af3fe` (L3 decoder wiring) — and they are **not** the submission-era "4 deferred" (that was the
cadence/pivot batch, `ARCHITECTURE.md` doc-version 3.25). **This is the session's most consequential
finding**, so it gets its own row (**OI-148**) rather than a footnote. Three facts make it load-bearing:

- **The mechanism is the key layer's own, verified at the code.** The `characteristicPitch` and
  `trueLeadingTone` scorer terms are **hard-gated on a `> 0.1` window weight** —
  `keymodeanalyzer.cpp:339-354` (below the cliff the candidate takes the *penalty*, not a reduced
  boost) and `:374` (`(ltWeight > 0.1) ? trueLeadingToneBoost : 0.0`). C major's leading tone B♮
  carries weight **0.093** in the 4-beat decoder window at the K279 opening — just under the gate — so
  C is denied its anchors and the opening flips to F. That is exactly the emission-model-plus-window
  defect the OI-141 mechanism report pinned as *"the largest loss point, 2/3 traces"* and that the
  design opening's **decision 2** (the emission model: leading-tone term, window treatment) exists to fix.
- **One of them is a live in-suite instance of OI-147.** The Corelli xfail mis-keys the C-minor ending
  as **G Phrygian-dominant**, under which `Cm→G` reads `iv→I` instead of `i→V` and a spurious plagal
  cadence marker is emitted at m38 b1. An exotic dominant-family mode emitted where a plain diatonic
  reading is right *is* OI-147's signature — and Phrygian-dominant is one of the five modes the user
  just ruled on at OI-132. OI-147 was a corpus statistic; it now also has a reproducible, user-visible,
  DCML-checked test case.
- **Their scheduled fix does not exist.** All four skip messages say *"Fix scheduled: L1/L3
  stabilization plan Phase 4c"*. `cowork_l1l3_stabilization_plan.md` **has no Phase 4c** — its Phase 4
  is the tpc spelling capability. (`STATUS.md`'s "Phase 4c" is the already-landed `analyzeSection`
  refactor move, `8598cbd245` — a different thing.) So these four xfails have had **no owner in the
  register**. They now do.

### OI-60 — the blocking trio, all three fixed

- **(a) chord-symbols-as-input context-menu path — FIXED, and the row's polarity was misleading.** The
  symbol-reading path was **deleted wholesale** (`02e3733afb`); `forceClassicalPath`,
  `scoreHasChordSymbols`, `collectChordSymbolBoundaries`, `analyzeHarmonicRhythmJazz` have **zero hits
  in `src/`**; `ARCHITECTURE.md:3454-3459` — *"no Jazz path and no symbol-reading gate"*. The row reads
  as if reading symbols were a wanted feature; it was the **bug to remove**. Consuming them as *input
  evidence* is a distinct **future** item, already carried at **OI-80**.
- **(b) declaredMode soft-boost — FIXED.** The hard override is gone (`keyresolver.h:43-45`); the
  declared mode is now a **graded additive prior** — `keymodeanalyzer.cpp:594-603`, a small penalty on
  out-of-class modes (`declaredModePenalty = 1.0`, fit-bounds `{0.0, 15.0}`, droppable via
  `ignoreDeclaredMode`), regression-covered at `decode_keymode_tests.cpp:379-405`. (Coded as a penalty
  on out-of-class modes rather than a boost on the declared one — ranking-equivalent.) The *remaining*
  declaredMode concern — siloed to the key path — is **OI-78**, untouched.
- **(c) implode chord-track gaps — both named mechanisms verified present.** Repeated-chord suppression
  has its escape hatch (`notationimplodebridge.cpp:646-679`; `kSameChordReannotationGap` at `:661`), and
  the head-gap **and** tail-gap synthesis safety nets survived the move into
  `harmonicsegmenter.cpp:799-896` (checked directly — the one unknown the first pass could not close).
  **Residue, stated honestly:** the original "Oak and the Lark" fixture is **gone from the repo**, so the
  specific three-symptom report is not re-testable. Implode gap-filling has no dedicated fixture beyond
  Corelli — a score-acquisition matter that rides OI-38.

---

## 3. OI-52 — the decision, justified

The row's own framing ("trivial; likely not worth it — decide and close either way") is **already
superseded by a ratified decision**: the adjudication dossier's A6 verdict —
*"add the one shared helper at the next instrument touch; close the row then. Not worth its own commit;
not acceptable to leave forever"* (`cowork_adjudication_dossier.md:78-84`) — was **user-ratified on
2026-07-10** as one of OI-42's rule applications. The register row was simply never updated.

And the evidence has since moved *against* "not worth it". The risk A6 named — *"if the comparison ever
needs nuance, someone updates three of four sites and the headline number silently forks"* — **has
already fired in the sibling family**: OI-132's discovery D2 found the two OURS **key**-parsers embedding
different music-theory readings of the dominant-family modes, so that folding them moves a graded figure
in either direction. The root comparison carries exactly the same kind of latent nuance today: the
abstain convention (OI-33) had to be *written into prose* precisely because "what does a missing root
mean" is a decision that must be identical at every `==` site (`a8_rebaseline_measure.py:34` states it;
`compare_analyses.py:243-244` and `compare_rn.py:352/370/474` each re-implement the comparison). A
convention enforced by prose across four copies is the same construction that produced D2.

**Decision: build the shared helper** — not "close as not worth it". The row is therefore **STILL REAL —
ASSIGNED** to the next measurement-instrument touch (the OI-145 wave-1 remainder), which is precisely the
"next instrument touch" A6 named. The "decide either way" tier is eliminated: the decision is made and the
work is owned.

---

## 4. The two USER-DECISION rows — stated for a reader who does not know the code

### OI-56 — do we want a music-theory judge that works *without* ground truth?

**The situation.** Our whole measurement chain grades our analysis against **human-annotated ground
truth** (the DCML/When-in-Rome corpora, plus music21 as a corroborator). That machinery is strong and
getting stronger. But it only works on repertoire somebody has already annotated — roughly, the Bach
chorales and a few classical corpora. For everything else (the jazz scores, the Piazzolla, the Steely
Dan, the Hiromi), we have **no way to tell whether our chord analysis is any good**, because there is
nothing to compare it against.

`auto_review.py` was designed in 2026 to fill exactly that hole: feed our output to an LLM and ask it to
judge the analysis on music-theory grounds alone, with no reference annotations. It was never built on
master. A working implementation **does** exist, on a branch (`llm-triage`) that was last touched
2026-05-14 and has never been merged.

**Why it is your call and not a rule application.** An LLM judge is *not* ground truth — the standing
rule (#9, and the "music21 is not ground truth" convention) says we measure only against corpora known
to be accurate. So this tool could never grade us; at most it could *triage* — point a human at the
scores most likely to be wrong. Whether that is worth having, and worth maintaining a branch for, is a
scope judgement about what the project is for.

**The options.**

- **(a) Land it, rescoped.** Merge the `llm-triage` branch's judge, restricted to its Modes 1/2 (no
  ground truth), explicitly as a **triage** instrument that never produces a graded number. Cost: a merge
  of a two-month-old branch plus ongoing maintenance. Payoff: the first quality signal we would ever have
  on the ~163 unannotated scores — which matters more once the corpus-expansion directive (OI-38) lands.
- **(b) Defer it to the corpus-onboarding event.** Keep the row, do nothing now, and decide when
  non-annotated repertoire is actually onboarded (OI-38). Costs nothing; risks the branch rotting further.
- **(c) Drop it.** Declare the ground-truth measurement chain sufficient and close the row. Honest and
  cheap — but it means accepting that we will not know how good the analysis is on anything outside the
  annotated corpora.

*(Note: the design's third mode — scoring against known ground truth — is obsolete either way; the
measurement chain does it far better than an LLM could.)*

### OI-62 — is the intonation/tuning feature still a goal?

**The situation.** Separately from the harmonic analysis, this fork has a **microtuning** feature: it
retunes notes by a few cents so chords sound in just intonation rather than equal temperament. A good
deal of it is built and working (the tuning tables, the tonic anchoring, basic zero-sum centering,
split-and-slur for held notes, the FreeDrift mode, the UI).

`ARCHITECTURE.md` §11.3 specifies **six further refinements** that were designed and never built, and
I confirmed all six are still missing at the code — for instance `computeSusceptibility()`
(`notationtuningbridge.cpp:510-520`) still returns "freely retunable" for *every* note that is not
explicitly anchored, with the comment *"Duration-based and context-based classification is a future
addition."* The six are: voice-role-weighted centering; a duration-based susceptibility budget;
sustained fifth/octave protection; per-note offset clamping; tuning-session drift state; and a
FreeDrift reset marker. (The "tie re-split" gap from the old Known-Gaps list turns out to belong here
too — it is a *tuning* limitation, not an analysis one.)

**Why it is your call.** Every one of these is real, checked, and unbuilt — but **nothing in the current
programme touches them**. The entire arc (the key layer, the engage arc, the certification audits) is
about harmonic *analysis*. No register row gates on tuning. So this is not a question of sequencing; it
is a question of whether the tuning feature is still something we intend to finish.

**The options.**

- **(a) Keep it held.** Confirm the six as a deliberate long-horizon hold (§H), revisited when the
  analysis work reaches a natural pause. They stay visible and never get forgotten.
- **(b) Schedule it.** Give the six an owner and a stage — which means competing for time with the key
  layer.
- **(c) Close it as out of scope.** Declare the tuning feature complete-as-shipped and delete the six
  from the register (the specification stays in `ARCHITECTURE.md` as a record of what was designed).

---

## 5. Task 2 — the long-horizon holds (§H)

| Row | Hold still the right disposition? | Trigger / owner still accurate? |
|---|---|---|
| **OI-64** (engage plan E1–E5, gates G1–G6) | **Hold confirmed** — the arc itself | Accurate; now gated by *two* things: the Stage-3 entry gate (OI-1…OI-7) **and** the key-layer readiness gate (OI-145) |
| **OI-65** (retirement map R1–R9) | **Hold confirmed** | Accurate — trigger is E4 |
| **OI-66** (recognition consumer) | **Hold confirmed** | Accurate — trigger is the recognition-consumer build (roadmap A-6) |
| **OI-67** (style clustering / idiom auto-detection) | **Hold confirmed for the build** | **Source understated:** a cross-tradition idiom study has since **landed** — `idiom_discovery/`, commits `d9b2020623` (5 idioms + the voice-leading axis), `95374ef16a`, `2a3c767dae`. The evidence base for OI-39's "idiom coverage 1/5" now exists; the *build* stays deferred to Stage 5+. Row's source enriched |
| **OI-68** (capability tracks A-3/A-4/A-5 + NCT L4 lever + voice-leading axis) | **★ TRIGGER HAS FIRED → PROMOTED** | **A-3** = *"dominant-implication key evidence in the L3 emission"* (`docs/implementation_roadmap.md:233`). The key-layer work now names exactly this: the OI-141 mechanism report found *"no cadence/dominant channel in the decode (OI-68)"*; the design opening's **decision 3** is the cadence→key channel; and **the user confirmed leading-tone/cadence work as the second lever** (recorded at OI-141). A-3 is no longer a deferred capability track — it is an active key-layer design input → **STILL REAL — ASSIGNED**. A-4/A-5 and the voice-leading axis stay held; the **NCT-filter L4 lever** now has a named consumer (OI-55) |
| **OI-69** (joint segmentation) | **Hold confirmed** | Accurate — past Stage 5 |
| **OI-70** (standing constraints: B3 dim7 dead end; rootContinuity sparse-gate dead end; Gate-A enharmonic constraint) | **STANDING — confirmed** | **+ one caution added (#12 carry from OI-59):** re-attempting the key-confidence-gated dominant-quality fix re-triggers the Chopin op30-2 `[4800,6240)` segmentation cascade |
| **OI-71** (roadmap 0.1 doc pass) | **NOT a hold — already done** | **SUPERSEDED** (see §1) — closed at `7bc1609159` |
| **OI-61** (Future Architectural Considerations, moved here from §G) | **Hold confirmed as a list** | **Two dedupes:** its *"Voice role information in HarmonicRegion"* item is the substance of the active **OI-74** (the tone surface is voice-blind, owned by the E4 fact-publication design + OI-145 wave 3) — and its stated trigger (*"revisit when sophisticated tuning algorithm is implemented"*) is **wrong**: the trigger fired by a different route. Its *"isChordTrackStaff() → Part-level flag"* item is OI-48's substance |

---

## 6. New rows opened by this session (same-commit rule)

| ID | What | Why it is new |
|---|---|---|
| **OI-148** | The four key-emission xfail notation tests (`a6b08af3fe`) — the key layer's ready-made acceptance tests; their "Phase 4c" schedule anchor does not exist | Surfaced by re-running the suites for OI-59; no register row owned them |
| **OI-149** | German-flat-bass slash drop — `csfIsValidBassNoteName` rejects German flat names (`"Ces"`/`"Fes"`), so the slash is **dropped and the bass is lost from the symbol** (`C/Ces` renders as `C`). A correct-oracle test is checked in **disabled** (`chordsymbolformatter_branch_tests.cpp:318`) with an in-source *"flagged for Cowork"* — and **no register row** | A defect tracked only in a source comment is a #10 register-completeness gap (the OI-109 pattern). User-visible display defect; sibling of OI-113/OI-114 |
| **OI-150** | `BUILD_AND_TEST.md` stale test baselines — says composing **"974/974"** (measured **1101/1101** + 2 disabled) and notation **"53/53"** (measured **53 pass + 4 SKIPPED**, unmentioned). The notation line actively **hides the four xfails** | Doc-sync (#10), found by running the suites |

---

## 7. Self-check (CLAUDE.md, after every coding exercise)

Re-read the actual diff of every touched file against the principles, the conventions, and
`DEFECT_TYPES.md`:

- **#8 (no fixing out of stage) — honored.** Nothing was fixed. Every temptation (the S20 helper, the
  STATUS banner, the `BUILD_AND_TEST.md` baselines, the German-bass validator) became a **row**, not a
  patch — including the three that would have taken under a minute.
- **#15 (verify at objects, never at assertion) — honored.** Every SUPERSEDED verdict rests on code or
  measurement I read myself: I personally re-read `chordsymbolformatter.cpp:901-940` and
  `regionanalyzer.cpp:284-290/1465` before closing OI-53; personally counted the 140 registry entries
  against 163 disk files before rescoping OI-57; personally confirmed the head/tail gap nets at
  `harmonicsegmenter.cpp:799-896` before closing OI-60(c); personally ran the three suites.
- **#12 (no information loss) — honored.** Nothing was dropped on closure. The Chopin cascade
  fragility, the missing C9sus2 export regression test, the live tonicization labeler's limits (dom7 and
  dim/half-dim only, no chromatic-leading-tone guard), and the absent implode fixture are each **carried
  forward** at a named row rather than discarded with their parent.
- **#3/#13 (a surprise is a STOP, not a curiosity).** Two surprises were found and are surfaced, not
  built around: the four xfails' scheduled fix (**"Phase 4c"**) does not exist, and a checked-in
  correct-oracle test (**OI-149**) was flagged only in a source comment. Both are now rows.
- **Conventions — honored.** No self-invented labels, abbreviations, or numbering: every name used here
  (`class-(b)`, A-3, R9, Phase 4c, S20, DT-12) is the repository's own; where a thing had no name I
  described it in plain words. American English.
- **DEFECT_TYPES.md.** The new findings are existing types — OI-148 and OI-150 are **DT-12** (stale
  anchor / dangling reference), OI-149 is the **OI-109 pattern** (an issue tracked only in a source
  comment). **No new defect type.**

---

## 8. Register state after this pass

The register's weakest tier is gone: **no row's plan is a promise to make a plan.**

- **SUPERSEDED (closed with provenance):** OI-53, OI-54, OI-59, OI-60, OI-71 — plus OI-58's sub-claims 4
  and 6.
- **STILL REAL — ASSIGNED (moved, with owner/stage/gate):** OI-55 (→ §B, E4 decoder engagement),
  OI-57 (→ §D, the corpus-onboarding event), OI-52 (→ §D, next instrument touch), OI-68's A-3 (→ the
  key-layer build), OI-47 and OI-48 (→ §F, doc-sync), OI-58's surviving three (→ §H, owners named).
- **STILL REAL — USER DECISION (awaiting the user, §E):** OI-56, OI-62.
- **HOLD CONFIRMED (§H):** OI-61, OI-64, OI-65, OI-66, OI-67, OI-69, OI-70.
- **NEW:** OI-148, OI-149, OI-150.

**The one thing worth carrying out of this session:** the key layer already has four failing,
user-visible, DCML-checked acceptance tests sitting in the suite — and until now, nobody owned them.
