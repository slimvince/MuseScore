# The information-loss audit — a grounded, classified catalogue (Engage arc #4)

> **Purpose (principle #12 made proactive).** The no-information-loss principle turned from *accidental* into a
> *systematic* sweep. The Gate A case (O-11/O-19) proved this defect class is real, lurks on exactly the surface
> Layer 5 will consume, and was found only incidentally. This document catalogues the suspected information-loss
> sites across the load-bearing surfaces, each **grounded at the code** (symbol + line + mechanism) and **classified
> on the central axis**. **READ-ONLY: no `src/` change, no fix.** Every fix is its own later ratified event
> (the Gate-A pattern). Provenance: static sweep (Cowork engage arc #4, 2026-07-06), four parallel read-only tracing
> passes over the load-bearing surfaces named in `cowork_functional_analysis_research_grounding.md` (bass, spelling,
> distinct alternatives, preserved uncertainty), every hit verified at code by CC. HEAD = `b0acb5c436` (the O-19
> GateA design-fold; the build has not landed). Fitter O-20.

## The central classification axis (the user's binding rule)

Not-yet-consumed information is **NOT automatically a defect.** Every site is classified as one of:

- **OK — PRESERVED, awaiting a future/dormant consumer.** Intact and carried; simply not consumed *yet* because
  its consumer (e.g. Layer 5) is not built yet. Correct forward-provisioning — records the engage-ready substrate.
- **DEFECT — LOST.** Destroyed / overwritten / collapsed / dropped so **no** consumer — present OR the
  architecture-intended future one — can recover it. (The Gate A case: a distinct alternative overwritten by a
  near-duplicate.)
- **DEFECT — SHOULD-ALREADY.** Preserved/available, but a consumer that **already exists and should be using it now**
  does not receive it (a routing/wiring gap).
- **UNCLEAR — consumer-status ambiguous.** Not guessed (#1); recorded for user adjudication.

**Severity:** deprives an architecture-intended consumer = **high**; cosmetic / nothing-ever-consumes = **low**.
**#4-relevant** = the loss touches a research-confirmed load-bearing correctness signal (bass / spelling / distinct
alternatives / preserved uncertainty — `cowork_functional_analysis_research_grounding.md` §1/§4).

**The two-track architecture the classification hinges on (ARCHITECTURE.md §Layers 4/5).** Production runs the
**LEGACY** `analyzeChord` + post-scoring-gates path (where the `results[]` alternatives carry, Gate A/FM2, and
`tpcForPc` live). Layer 4 (`ChordSliceDecoder`) and Layer 5 (`functionoutput`) are **Built+Dormant**, engaging
jointly. The dormant path is a **rich, correct carry substrate** (open-question labels, per-note spelling, honest
"unknown"); most not-yet-consumed signals are *its* forward-provisioning (→ OK). The genuine LOST sites are on the
LEGACY path's user-visible carry surface, which O-11 ruled is *inside the byte-identity contract* (E-14
user-visible) **and** the surface the future L5 selects among.

---

## Table 1 — DEFECT: LOST (the prioritized fix-queue; each a later, separate ratified event)

| # | location (file:line · symbol) | surface | form | information | consumer(s) | severity | grounded evidence |
|---|---|---|---|---|---|---|---|
| **L1** | `postscoringgates.cpp:214-234` · Gate A vs FM2 (in `applyPostScoringGates`) | chord `alternatives[]` carry | (a) overwrite + (d) lossy dedup + (i) rebuild | the winner's **distinct enharmonic Major-add6 partner** reading | **PRESENT** (`notationcomposingbridge.cpp:298-300` → `outContext.chordResults`, E-14 user-visible) **+ future L5** selector | **HIGH** (#4-relevant — distinct alternatives) | Gate A `std::swap(results[0], results[bestAltIdx])` (l.217) **keeps** the partner; FM2 `results.push_back(buildResult(rc)); std::swap(results[0], results.back())` (l.229-230) appends a **freshly-built near-duplicate of the winner**, the distinct partner is not equivalently preserved. The correct-carry model is the Gate G-E phantom-pop `results.pop_back()` at `postscoringgates.cpp:388-392`. **Already scoped: O-19** (`promoteToWinner` + present-first dedup guard). |
| **L2** | `analysisutils.h:175-180` · `mergeChordAnalysisTones` **and** `chordanalyzer.cpp:1229-1240` · `tpcForPc` build | pitch spelling | (h) spelling flatten + (d) lossy dedup | a **distinct enharmonic TPC** when two sounding tones share a pitch class but spell it differently (e.g. G♯ vs A♭, C♯ vs D♭) | **PRESENT** legacy scorer/namer — `tpcConsistencyBonus`/`countTpcMatches`, `rootTpc`/`bassTpc` naming | **MEDIUM** (#4-relevant — spelling predicts root, research §1) | the merge keeps the **lower-pitch** tone's tpc, else the first-seen (l.176-179); `tpcForPc` keeps only the **first** sounding tpc per pc (comment l.1229-1230: "the TPC of the first sounding tone") — the arbitration is **iteration-order**, not voice/weight/duration. The distinct spelling is destroyed **for this analysis** (the source `NoteModel` retains it). The rebuild L4 path does **not** consume `tpcForPc` — it reads per-note `FocalNote.tpc` through the shared `engravingbridge::lineOfFifths` (the G4/C1 spelling-pin) — so no *future* consumer is deprived; the fix is the already-named **"second tpc reader" unification residual** (ARCHITECTURE.md L4 §Unification residual): adopt L4's per-note spelling on the live path (the owed tpc-fold). |

*(L1 is the pattern the whole arc is named for; L2 is the one new #4-relevant LOST site the sweep surfaced.
Both are legacy-path-scoped, in-layer, and independently ratifiable.)*

---

## Table 2 — DEFECT: SHOULD-ALREADY

**None found.** The sweep did not surface a site where a signal is preserved/available yet a **present** consumer
that *should* consume it now is denied it. The one apparent candidate — the present 0.8 KeyArea/annotate gate reads
the **weaker-calibrated** emission sigmoid (`keyModeResult.normalizedConfidence`) while the **better-calibrated**
Layer-3 sequence-margin (`HarmonicRegion.keyConfidence`, C1: 2.8–3.1× better) sits carried-but-unconsumed — is a
**ratified deferral**, not a gap: `harmonicrhythm.h:90-96` declares D-L3a as "Declaration only; no wiring/threshold
change," the margin provisioned for L5. Recorded here as an empty bucket **because that is itself informative**: the
substrate is cleanly forward-provisioned rather than mis-wired.

---

## Table 3 — OK: PRESERVED, awaiting a future/dormant consumer (the engage-ready substrate)

| # | location (file:line · symbol) | what is carried | intended (future) consumer | note |
|---|---|---|---|---|
| **K1** | `chordslicedecoder.h:404-461` · `SliceChord` (Layer-4, DORMANT) | `chosen` + ranked `alternatives` (∪ prevailing), `confidence` (margin), `uncertain`, `decision` (commit/inherit/**abstain**), `confidenceModel` (`SliceConfidence`: margin/sufficiency/membershipCleanliness/composite), `openQuestion` (`OpenQuestionLabel`: question + ambiguity + readingA/readingB), `chordTonePcs`/`nonChordTonePcs`, per-note `FocalNote.tpc` + the G4/C1 spelling-pin | Layer 5 (function) — selects among carried readings | The **rich, correct** chord carry substrate. `extensionsKnown` is **honest-carry** (never a guess — a triad-level read when the seventh is unknown). This is where spelling and uncertainty are done **right** (the counter-model to L1/L2). |
| **K2** | `functionoutput.h:85-145` · `FunctionLayerOutput` / `FunctionAnalysisUnit` / `FunctionConfidence` (Layer-5, DORMANT) | full DCML Roman numeral, `openMark` (honest undecided), three fixed confidence components + `combined` **and** its `combinedBoundary` [0,1) squash, the committed L4 identity carried **verbatim** (additive §7) | Layer 6 (grouping/display) | `functionoutput.h:66`: "**DORMANT … NO production consumer — nothing in `src/` calls it**." The OK archetype. `combined` **and** `combinedBoundary` both kept (representational, no decision changed). |
| **K3** | `harmonicrhythm.h:118-119` · `HarmonicRegion.keyAlternatives` / `keyConfidence` | the region-level ranked candidate-key menu (excl. chosen) + the Layer-3 boundary (sequence-margin) confidence | Layer-5 modulation recompute — selects among the carried keys | `harmonicrhythm.h:88/113-117`: "**IN-MEMORY ONLY, no consumer yet** … it exists for Layer 5"; "**DELIBERATELY NOT SERIALIZED** … adding them is byte-identical." The OK archetype for the **key** side. |
| **K4** | `chordpathdecoder.h:69-74` · `ChordPathNode.alternatives` / `winnerMargin` | per-node emitted alternatives + winner margin | Stage 3.2 wider-beam decode / Stage 6 functional labelling | Beam-1 **inert** (FastBeam1); structure forward-provisioned, `path()` unread. Comment-accurate dormancy. |
| **K5** | `keymodesequence.cpp:389-395` · `SliceKeyMode.alternatives` (cap `maxAlternatives=4`) + `keymodeanalyzer.cpp:788-830` · `analyzeKeyMode` `dumpOut` (full 252) | the ranked surviving key candidates per slice; the **full** 252 (tonic×mode) lattice is scored at **every** slice via the global top-K union | region key reduction (`regionanalyzer.cpp:768-773` reads `chosen`+`alternatives` → the K3 menu) | The visible `alternatives` cap is 4 (form f), but the **lattice union is complete** and the collapse to `normalizedConfidence` (sigmoid, `keymodeanalyzer.cpp:766`) is **recomputable** (deterministic) and the alternatives are carried. Not a loss. |
| **K6** | `keymodesequence.h:157` · `SliceKeyMode.uncertain` (not propagated to the region struct) | the boolean "margin < threshold" mark | (reach-back gate, optional) | **Lossless**: `uncertain ≡ confidence < uncertainThreshold`, and `confidence` (the source) **is** carried to `HarmonicRegion.keyConfidence` (K3). The derived boolean is recomputable — dropping it loses nothing. |
| **K7** | `functionresolver.cpp:450-468` · override reads `s.confidence.composite` only; `forwardoverride.cpp:37-44` · boolean gate | the `SliceConfidence` **components** (margin/sufficiency/cleanliness) remain on the carried struct (K1); the F-B `contradictionStrength` becomes `functionConfidence` on fire | Layer 5 (the resolver is Layer 5, DORMANT) | **Considered as a candidate LOSS (Agent-flagged) and reclassified OK.** The composite is the **§7 designed min-combination**, not a destructive collapse — the three components stay available on `confidenceModel`; a decision gate collapsing a comparison to a boolean is normal decision-making, not information loss (the alternatives themselves are carried). The F-B override is itself a **declared net-harmful disable-candidate** (O-17/O-18). No consumer is deprived of a form it needs. |

---

## Table 4 — UNCLEAR (consumer-status ambiguous → user adjudication; #1, not guessed)

| # | location (file:line · symbol) | form | the ambiguity | provisional lean |
|---|---|---|---|---|
| **U1** | `harmonicfunctionlayer.cpp:520-528` · the `results.size() >= 3` cap in `applyHarmonicFunction` | (c) partial-truth + (f) cap | The legacy `results[]` is capped at 3 (the full scored cube is retained internally but **not carried** — only `diagnoseChord`/tests read the snapshot). **Which carry surface does the future L5 bind to** — the legacy 3-capped `results[]` (the O-11/E-14 carry contract) or the rebuild L4 `SliceChord` full-cube `alternatives` (which re-reads the whole cube)? If the former, the cap limits the L5 carry; if the latter, the cap is legacy-only. The present bridge consumer surfaces only the top-3. | **UNCLEAR** — cross-refs L1 (same surface). If L5 binds the legacy surface, promote toward the L1 fix; if it binds the rebuild L4, the cap is a low product choice. |
| **U2** | `regionanalyzer.cpp:369-375` · J-key-iii leaves the chord = R0 | (e) ordering/ranking loss | The joint re-key updates only `region.keyModeResult`; the chord + its `alternatives` are left as **Pass-1 artifacts, not re-ranked under the new key**. Design-intentional (a faithful per-region re-emission measured ~6% same-key root-flip **artifact**, dossier §6). This is the **canonical "key-then-chord truncation the owed joint step is meant to fix"** (O-18: the joint step is "**still owed at Stage 5**"). Is the stale-under-new-key ranking an **OK owed-future-step**, or a **should-already** faithful re-rank? | **UNCLEAR** — leans OK-owed (the joint step is the architecture-intended future consumer; the design honestly declines to inject artifact), but flagged because it is the joint-step anchor. |
| **U3** | `regionanalyzer.cpp:157-175` · `coalesceShortSameRootRuns` | (i) overwrite-on-recompute + (d) | On coalescing short same-root runs, the longest sub-region's chord is kept (`std::move`) but the **bass is re-derived from the merged tone union** (`bassPc`/`bassTpc` overwritten), and the non-kept sub-regions' `alternatives`/confidence are dropped in the move. Is the re-derived whole-region bass **richer** (correct) or a **loss** of the contextually-analyzed bass? Not decidable read-only (needs a score/runtime check). | **UNCLEAR-low** — a runtime/score check adjudicates; low priority. |

---

## Sites considered and classified OK / not-a-defect (overwrite-on-recompute on the LIVE path)

Recorded so the axis application is auditable (a genuine-loss must not be waved through as OK, and vice-versa):

- **Pedal Pass-2 overwrite** — `chordpostpasses.cpp:285-290`: on a **confirmed** structural pedal, `results = pass2`
  replaces the Pass-1 reading. **OK**: Pass-1 *mis-includes* the sustained pedal bass as a chord tone, so it is the
  **wrong** reading — discarding it is the intended correction — and the pedal **provenance is preserved**
  (`isPedalPoint = true`, `pedalBassPc = bassPc`, l.288-289). Not information loss (the discarded reading is the error).
- **Sparse chord quality refinement** — `sparsechordrefinement.cpp:119-166` (`refineSparseChordQualityFromKeyContext`)
  + `applyTonicPriorToSparseChord`: `Unknown → diatonic` quality. **OK**: **evidence-gated** — it only assigns when the
  tones actually fit the diatonic triad shape (`tonesFitTriadShape`, l.161) and it **explicitly leaves genuinely
  ambiguous cases `Unknown`** (the Aeolian lone-tonic/dominant carve-out, l.154-159; dense 3+-PC regions untouched,
  l.184). A constrained inference, not a guess; the honest "unknown" survives exactly where it is genuinely unknown.

---

## Taxonomy coverage (the a–i forms swept + the new forms the code revealed)

| form | swept? | representative hit(s) |
|---|---|---|
| (a) overwrite/replace distinct with a duplicate/weaker | ✓ | **L1** (FM2 append of a winner near-duplicate) |
| (b) compute-then-drop | ✓ | dump surface (K/OK) — `rootTpc`/`bassTpc`/`oracleCells`/`rawCandidates`/competition-signals/`scale` not in `batch_analyze` JSON (recomputable via `diagnoseChord`; the `chordSymbol` string carries spelling) → **low/OK** |
| (c) partial-truth (collapse a set to one; keep winner) | ✓ | **U1** (top-3 cap) |
| (d) lossy dedup/merge | ✓ | **L1**, **L2**, **U3** |
| (e) ordering/ranking loss | ✓ | **U2** (stale chord-alternative ranking under re-key) |
| (f) silent truncation/cap | ✓ | **U1** (top-3), **K5** (key alts cap 4 — but lattice complete) |
| (g) uncertainty collapse | ✓ | **K5** (sigmoid; recomputable), **K7** (composite min; components retained) |
| (h) spelling flattening | ✓ | **L2** (`tpcForPc`/merge) |
| (i) overwrite-on-recompute | ✓ | **L1** (FM2 rebuild), **U3** (coalesce), pedal/sparse (OK) |
| **(+1) honest-unknown-carry** *(new — the positive counter-form)* | ✓ | **K1** `extensionsKnown` / `openMark` / `SliceDecision::Abstain` — carrying "we don't know" explicitly rather than guessing. The correct pattern L2's `Unknown→diatonic` and any future guess must respect. |
| **(+2) recomputable-collapse** *(new — a collapse that is NOT a loss)* | ✓ | **K5** (sigmoid), **K6** (`uncertain` flag) — a hard value derived from a **carried** source (or deterministically regenerable) is lossless; not every collapse is a defect. Guards against over-flagging. |

---

## The prioritized DEFECT fix-queue (each a future separate, ratified, Gate-A-style event)

1. **L1 — Gate A / FM2 promotion unification (HIGH, already scoped).** Adopt the O-19 design: one `promoteToWinner`
   primitive with a **present-first dedup guard** + one collapsed builder wrapper ⟹ Gate A + FM2 become two branches
   of one promotion ⟹ the distinct partner is preserved on **both** idioms (winner AND carry byte-identical to
   C_HEAD). Ratification surface = the 36-score alternatives delta (O-19). #4-relevant.
2. **L2 — legacy per-note spelling adoption (MEDIUM, #4-relevant).** Retire the legacy `tpcForPc`/merge spelling
   collapse in favour of the L4 per-note `FocalNote.tpc` + shared `engravingbridge::lineOfFifths` reader (the named
   **"second tpc reader" unification residual**, ARCHITECTURE.md L4). Closes a #4-load-bearing (spelling→root) loss
   and a total-unification (#6) duplication in one move. Sequence: after or with the L1/L4-L5 engage work, since the
   correct reader already exists on the dormant path.

**Adjudication asks (Table 4):** U1 (which carry surface L5 binds to — settles whether the top-3 cap is L1-adjacent
or a low product choice); U2 (is the owed joint step's stale-alt-ranking acceptable-until-engage, or a faithful
re-rank owed now); U3 (is the coalesce bass re-derivation a correction or a loss — needs a score check).

## Research cross-references (#4-relevant losses)

- **L1** (distinct alternatives) and **L2** (spelling) both touch signals
  `cowork_functional_analysis_research_grounding.md` §1/§4 names as **load-bearing for the correct root**: "Bass
  note / inversion — a strong, semi-independent evidence channel"; "**Pitch spelling** — disambiguates enharmonic
  roots that pitch-class-blind vertical fit cannot" (Micchi 2020; McLeod & Rohrmeier 2021). Losing them degrades the
  exact lever §4 identifies for recovering wrongly-overridden roots — flagged **high-value** even where severity is
  medium.
- **K1/K3** (carried alternatives + preserved uncertainty) are the substrate §2's "select by **joint consistency**,
  carry a beam of hypotheses" lesson requires — the audit confirms that substrate is present and correct on the
  dormant path, an engage-readiness datum.

*Cowork engage arc #4, 2026-07-06. Read-only catalogue; every fix is its own ratified event. Provenance:
`cc_engage_information_loss_audit_report.md`; fitter O-20.*
