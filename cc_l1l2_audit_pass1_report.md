# CC Report — L1/L2 Certification Audit, PASS 1 (blind enumerative) — EG-7 / OI-84

> **Author: Claude Code (host), executing `cc_instruction_l1_l2_audit_pass1.md` (Cowork,
> session 36).** Read-only fact-finding (explorational; no `src/` change, no constant tuned,
> no golden refresh, `tools/robust_stop/` + `tools/corpus/` untouched). This is **PASS 1 of 2**
> — the blind enumerative pass (protocol P1–P4). Certification is **NOT** granted here; Pass 2
> (the signature sweep + P5/P6 sampling) is a separate instruction to a fresh session.
>
> **Provenance:** inventoried at HEAD `7123c7cb55` (src/composing byte-identical to the
> instruction's precondition `52cc701a6d`…`eb624d442d`; the ref advanced to the handoff-rename
> commit mid-session — docs-only, see §0), corpus `c50002fee1`. Instruments:
> `tools/audit/gen_inventory.py` (the machine inventory) + `tools/audit/gen_dispositions.py`
> (the total disposition emitter). Artifacts under `tools/audit/l1l2/`.

---

## 0. Task-0 incident record (git state) — surfaced, not patched (#13)

Two symptoms of ONE root cause were found at session start and resolved with the user's explicit
authorization (read-only diagnosis first; nothing discarded):

1. **Stale main index** — the index staged a wholesale reversal (~740 deletions across 11 files)
   of the session-36 documentation commits. Cleared with `git reset` (unstage only; HEAD and
   working tree untouched).
2. **Unmaterialized working tree** — four docs (`CLAUDE.md`, `OPEN_ITEMS.md`, `STATUS.md`,
   `cowork_handoff.md`) held the PRE-CLOSE state on disk while HEAD (object DB + ref) held the
   correct CLOSE state. Materialized with `git restore` — which *completed* the commits rather
   than discarding anything (every restored file was byte-identical to HEAD).

**Root cause (confirmed by Cowork):** the two final session-36 commits (`eb624d442d`,
`7123c7cb55`) were built entirely through the git **plumbing** path — file contents
reconstructed from HEAD blobs + edit strings, staged via `hash-object`, ref moved — but never
written to the working tree. The object DB/ref were correct and *ahead*; the disk was *behind*.

**Concurrent-edit hazard (new operational finding).** Mid-session the HEAD ref advanced
`eb624d442d → 7123c7cb55` (docs-only rename/fix; `src/composing` byte-identical), and
`OPEN_ITEMS.md` acquired a **live uncommitted Cowork edit dated 2026-07-11** (an expanded OI-43
marking the joint-key question "ON HOLD … until CC's in-progress audit (OI-84) completes"). The
working tree is being **edited concurrently by Cowork**. This audit therefore: (a) never
restored/discarded `OPEN_ITEMS.md`; (b) staged only its own new files for the Task-1/Task-4
commits; (c) appended (never rewrote) shared docs for the Task-5 fold. → register **OI-85**;
promotable defect **type** (see §7): *"plumbing commit without working-tree/index sync — object
DB ahead of disk"*, mechanical signature = `git status` non-empty immediately after a
scratch-index commit; convention = every plumbing commit ends with a main-index refresh + a
disk-vs-HEAD verification.

---

## 1. The machine-generated inventory (P1) + manifest

`tools/audit/gen_inventory.py` enumerates the ENTIRE `src/composing/` tree (tracked files) and
tags every file L1 / L2 / L3+ / RETIRES with a one-line reason; it **exits nonzero if any file
lacks a tag** (P1 totality). For L1/L2 files it extracts functions, numeric literals (trivial
0/1 excluded, rule in-script), header-declared struct fields (cross-visible), branches, and
cross-layer includes, over comment/string/preprocessor-blanked C++ (heuristic, over-capture-biased
— method stated in the script docstring and `manifest.json`).

| inventory table | rows |
|---|---|
| tracked files (file table) | **216** — L1 **11**, L2 **2**, L3+ **199**, RETIRES **4** |
| deep-audited files (L1+L2) | **13** |
| functions | 55 |
| numeric literals | 92 |
| branches | 192 |
| struct fields (cross-visible) | 39 |
| function declarations | 28 |
| cross-layer includes | 66 |

**Instrument establishment (#19).** Cross-checked against ground truth I can verify by hand:
`slicer.cpp` → 1 function (`changePointSlices`), 3 literals (the three `2`s), 3 branches (three
`if`s), 1 cross-layer include — all exact. `note_model.h` → **11** struct fields, matching the L1
design doc's documented "eleven facts per note record" exactly. Manifest stamps HEAD, the
script's blob sha, corpus `c50002fee1`, and per-table counts (wall-clock excluded, EG-2
precedent).

**The 13 deep-audited files.** L1: `notemodel/note_model.{h,cpp}`,
`engravingbridge/{regiontonecollector.{h,cpp}, regiontoneprimitives.cpp, spellingview.{h,cpp},
phraseboundaryview.{h,cpp}}`, `scoreharvest/metricweights.{h,cpp}`. L2:
`slicing/slicer.{h,cpp}`. (harmonicsegmenter is L2-by-definition but RETIRES R6 — see §6.)

---

## 2. Disposition summary (P2) — every row has a verdict

`tools/audit/gen_dispositions.py` maps EVERY inventory row to a closed-set verdict (authored at
file/function/constant/dep granularity, expanded to fine-grained rows by stated blanket rules),
and **fails if any row lacks a verdict**. Result: **688 disposition rows, all with a verdict.**

| verdict class | verdicts (count) |
|---|---|
| CODE (functions/branches/decls) | SURVIVES 186, SURVIVES-MIXED 73, RETIRES 33 |
| CONST (literals) | ESTABLISHED 72, UNFIT 20 |
| DERIVED (fields) | PUBLISHED 39 |
| PREMISE (cross-layer deps) | FACT 62, ASSUMPTION 4 |
| SCOPE (L3+/RETIRES file tags) | 203 |

**Headline:** the L1/L2 **surviving spine is sound** — the note model (L1) and the change-point
slicer (L2) are clean, well-documented, edge-complete, and faithfully established (byte-identical
histories, exact edge handling). **No Class-A unverified causal premise and no correctness bug
was found in the surviving spine.** Every flagged item is one of: a hand-set constant outside the
fit manifest (EG-5 fuel), an upward layering dependency (#7, mostly rides existing retirements),
a mixed-layer module (grab-bag), or a declared-dormant published fact (fact-publication corollary
— consumer named, not waste). Details below.

---

## 3. Flagged rows (46) — file:line + one plain-language sentence each

### 3a. UPWARD cross-layer dependencies (#7 layering) — 4 ASSUMPTION rows + file flags
A file in the fact/segmentation layers should not depend on a higher analysis layer; these do:
- **`metricweights.h:42`** includes `../key/keymodeanalyzer.h` — the L1.5 metric-weight primitive
  reaches *up* into the L3 key analyzer for its `KeyModeAnalyzerPreferences` /
  `KeyModeAnalyzer::PitchContext` types. Plain language: a low-level "how strong is this beat"
  helper is coupled to the much higher-level key-analysis code.
- **`regiontonecollector.cpp:37`** and **`regiontoneprimitives.cpp:37`** include
  `chord/analysisutils.h` (L4); **`regiontoneprimitives.cpp:38`** includes `chord/chordanalyzer.h`
  (L4). Plain language: the note-summary "views" (a fact layer) call into the chord-analysis
  layer. The `regiontonecollector.h` header comment claims this L1.5→L4 back-edge was "killed"
  (audit Q2) — **true only for the header**; the `.cpp` implementation still depends on L4. This
  is checkable and precise → **OI-86**.

### 3b. Mixed-layer modules (grab-bags) — #6/#7 owner-drift (file flags)
- **`regiontonecollector.h` / `regiontoneprimitives.cpp`** are an L1.5 "engraving bridge" that
  *also* hosts: L2-legacy sub-boundary detectors (`detectOnsetSubBoundaries` /
  `detectBassMovementSubBoundaries`, Pass-2/2b — retire R6); an L4 helper (`findTemporalContext`
  — FQ-3/OI-12, live on the notation bridge, moves to E4); and L3 key-context builders
  (`collectPitchContext` legacy + `pitchContextOverSpan` L3-survivor). Plain language: one
  "helpers" module is really four layers' code living together.
- **`metricweights.{h,cpp}`** is an L1.5 metric primitive that *also* hosts L3 key-window
  constants (`LOOKBACK_BEATS`/`LOOKAHEAD_BEATS`/`DECAY_RATE`) and prefs-driven key beat weights,
  and carries **two metric-weight tables** — `regionMetricWeightForBeatType` (hard-coded,
  prefs-free) vs `beatTypeToWeight` (prefs-driven): the same "beat → weight" concept expressed
  twice (potential #6 duplication). → **OI-86**.

### 3c. Inference-affecting constants NOT in the fit manifest (UNFIT, EG-5/T3-1 fuel) — 16 rows
The precise L1/L2 gap `tools/param_manifest.json` does not yet cover (verified by name against
the manifest):
- **beat-weight table** `metricweights.cpp:77-82` (1.0 / 0.85 / 0.75 / 0.5) — the prefs-free
  metric-salience weights; hand-set, no fit record, not in manifest.
- **sliding-window constants** `metricweights.h:57-60` (`LOOKBACK_BEATS`=16, `LOOKAHEAD_BEATS`=8,
  `LOOKAHEAD_WEIGHT`=0.5, `DECAY_RATE`=0.7) + `timeDecay` `beatsPerUnit`=4.0 (`:104`).
- **weightedPcView inference weights** `regiontonecollector.cpp:297` (repetition-boost 0.3),
  `:312` (cross-voice-boost 1.5) — hand-set analysis weights baked into the L1.5 view.
- **SpanWindowWeights seeds** `regiontonecollector.h:249-250` (0.7 / 0.5).
- **detectOnsetSubBoundaries Jaccard threshold** `regiontonecollector.h:194` (0.25) — L2-legacy
  (retires R6).
- **phrase-boundary params** `phraseboundaryview.h`: `k`=1.0 (`:91`), `coincidenceWeight`=0.0
  (`:103`), `minSilenceTicks`=240 (`:107`) — precision-phase, NOT in manifest (whereas `wGap`
  0.50 / `wInterOnset` 0.30 / `wPitch` 0.20 / `spikeCeilingFactor` 1.5 **ARE**: partial coverage).
  `minSilenceTicks`=240 is also a raw tick literal, not `Constants::DIVISION`-derived.

Plain language: these are numbers someone chose by hand that affect the analysis, and they are not
yet on the list the Stage-5 fitter/EG-5 will tune or freeze. → **OI-87** (feeds OI-6 / EG-5).
(NB: `wGap/wInterOnset/wPitch/spikeCeilingFactor` already in the manifest are ESTABLISHED-as-
tracked; the beat table 1.0 and other 0.0/1.0/2/4/12 literals are structural/music-fact, not
tunable — dispositioned ESTABLISHED.)

### 3d. Declared-dormant published facts (fact-publication corollary — consumer named, NOT waste)
Surfaced mechanically by the fire-rate/caller-liveness scan (§4); each has a **named future
consumer**, so per the ratified corollary these are *declared dormancy*, not waste — recorded, not
defects:
- **`note_model.cpp` `extend()`** — production fire-rate 0 (only the dormant L4 decoder reach-back
  + tests call it); consumer named = Phase-3 reach-back. Also self-declared interim debt: Phase-1a
  `extend()` re-walks the whole score per step (byte-identical; Phase-1b deferred).
- **`spellingview` `lineOfFifths`** — only consumer is the dormant L4 spelling-pin; **`spanSpelling`
  / `sharpFlatSense`** — ZERO consumers anywhere (Phase-B L3 key-spelling term).
- **`phraseboundaryview` `phraseBoundaryTicks` / `computePhraseBoundaryProfile`** — production
  fire-rate 0 (batch diagnostics + gated-off joint-key only); consumer named = L5 cadence engage.

### 3e. Self-declared DUPLICATED (R4) — the second tpc reader
- **`spellingview.h`** documents that the fold of `chordanalyzer.cpp`'s inline tpc cluster
  (`tpcForPc`/`tpcSpellsAsSharp`/`tpcConsistencyBonus`/`countTpcMatches`) into this single
  spelling primitive **has not happened** — a second, live tpc reader coexists today. Self-declared;
  retires R4 with the decoder. Plain language: there are two places that read note-spelling; only
  one is the intended single owner. (Aligns with the existing FQ-8/OI-13 "tpc-reader fold".)

*(Full 46-row list with verdicts: `tools/audit/l1l2/pass1_dispositions.{csv,json}`; the file-flag,
crosslayer-upward, const-unfit-not-in-manifest, func-dormant, func-retires kinds.)*

---

## 4. Fire-rate / behavioral characterization (P4)

Route (a) — caller-liveness scan (the O-10 idea): grep the production caller universe (composing
module, notation bridge, tools) for each L1/L2 public symbol. This mechanically separates LIVE
spine from DORMANT (never-fires-on-production) mechanisms without instrumentation. Route (c) — the
per-corpus *rate* of a live-conditional internal branch (e.g. the 0.3/1.5 boosts) is marked "NOT
measured" with reason: it would need a default-OFF counter + a build + byte-identity re-proof,
disproportionate for Pass 1 given the concurrent-edit hazard (§0), and its firing *population* is
code-evident.

| mechanism | file | live on production? | caller (evidence) | matches documented intent? |
|---|---|---|---|---|
| `changePointSlices` | slicer.cpp | **LIVE spine** | regionanalyzer.cpp:632/704, batch_analyze ×5 | yes |
| `NoteModel::build` | note_model.cpp | **LIVE spine** | every analysis (bridge/batch) | yes |
| `NoteModel::extend` | note_model.cpp | **DORMANT** (0) | only dormant L4 decoder reach-back + tests | yes (declared Phase-3) |
| `weightedPcView`/`collectRegionTones` | regiontonecollector.cpp | **LIVE** | batch_analyze:2706, bridge:206/633 | yes |
| repetition-boost 0.3 / cross-voice 1.5 | regiontonecollector.cpp:297/312 | LIVE (conditional) | inside weightedPcView | rate NOT measured (route c) |
| pedal Pass-4 / `buildPedalWindowIndex` | regiontonecollector.cpp / metricweights.cpp | LIVE (conditional) | inside weightedPcView | fires only when pedals present (≈0 on the Bach corpus) — NOT measured |
| dense-start look-ahead exclusion | regiontonecollector.cpp:206 | LIVE (batch only) | batch weightedPcView (bridge passes false) | batch-legacy path |
| `regionMetricWeightForOnsetTick`/`ForBeatType` | metricweights.cpp | **LIVE** | L4 membership / weightedPcView | yes |
| `beatTypeToWeight` (prefs) | metricweights.cpp | **LIVE** (key path) | collectPitchContext / key resolver | yes |
| `collectPitchContext` (legacy) | regiontoneprimitives.cpp | **LIVE** | legacy key resolver seed S2 — **retires R5** | transitional |
| `pitchContextOverSpan` | regiontoneprimitives.cpp | **LIVE** | keymodesequence.cpp:89 (L3 decoder survivor) | yes |
| `findTemporalContext` | regiontonecollector.cpp | **LIVE** | notationcomposingbridge.cpp:609 — **moves to E4** (FQ-3/OI-12) | transitional |
| `detectOnsetSubBoundaries`/`detectBassMovementSubBoundaries` | regiontoneprimitives.cpp | LIVE-exposed | bridge pass-throughs — **retire R6** (Pass-2/2b) | L2-legacy |
| `greedyExpandSegmentation` | harmonicsegmenter.cpp (RETIRES) | **LIVE** | regionanalyzer.cpp:870 — **retires R6** | L2-legacy (see §6) |
| `phraseBoundaryTicks`/`computePhraseBoundaryProfile` | phraseboundaryview.cpp | **DORMANT** (0) | batch diagnostics + gated-off joint-key | yes (declared L5) |
| `spanSpelling`/`sharpFlatSense`/`lineOfFifths` | spellingview.cpp | **DORMANT** (0) | Phase-B / dormant L4 pin only | yes (declared) |

**Finding of note (P4):** `regionanalyzer.cpp` runs **both** segmenters live simultaneously —
`greedyExpandSegmentation` (line 870) *and* `changePointSlices` (632/704). Two live segmenters
coexist on the production region path (the transitional state the L2 design records; FQ-8/OI-13
"two-segmenters retirement", R6). No never-fires or wildly-off-population *surviving* mechanism was
found; every zero-fire mechanism is a declared-dormant future-consumer path (§3d).

---

## 5. Negative-space contract check (P3) — spec → code

From the L1/L2 contracts (`cowork_layer1_note_model_design.md` §3,
`cowork_layer2_slicing_design.md` §3, ARCHITECTURE.md §"Layer 1/2"):

- **L1 note-model contract** — build ✓; return all notes in fixed order ✓ (`notes()`); "which
  notes sound in [A,B)" ✓ (`overlapping`); "which onset in [A,B)" ✓ (`onsetIn`); widen span ✓
  (`extend`, dormant); 11 per-note facts ✓ (`NoteEvent`); derived views ✓ (`weightedPcView`/
  `soundingAt`). **No contract gap in the L1 core.**
- **L2 slicer contract** — give the slices ✓; complete gapless non-overlapping coverage ✓;
  explicit empty slices for silence ✓; consume (not re-decide) L1 eligibility ✓. **No gap.**
- **L1.5 view set** — metric weights ✓; spelling ✓; phrase-boundary ✓. **ABSENCE:** the
  architecture (`cowork_layer2_slicing_design.md` §0) names a **"bass" L1.5 view** beside the
  spelling/phrase views, but there is **no owned bass-view primitive** — "bass = lowest pitch" is
  recomputed inline at `buildTones`, `weightedPcView`, and `pitchContextOverSpan`. Independently
  re-derived here; **already registered as OI-77** (bass/inversion verdict recomputed at ~60 call
  sites). Recorded as a P3 confirmation, not a new item.
- **"Single source of truth / no layer re-reads the raw score"** — held for NOTES (the note model
  is the sole note source), but the L1.5 views still read the `Score` directly for **non-note
  notation facts** (beat type via `tick2measure`, pedal spans via `spanner()`, measures) at
  multiple sites (`metricweights.cpp`, `regiontonecollector.cpp`). This is acknowledged by the L1
  design (the views "need it for beat weights / pedal windows / measure lookups"), so it is a
  scoped-contract observation, not a violation — but it means metric/pedal/measure facts have no
  single owned view yet (a candidate future consolidation, noted, not an OI).

---

## 6. RETIRES list + #12 interpretation-check notes

Code on the R1–R10 map gets NO deep audit — only the #12 check of what embedded interpretation
must be consciously kept or rejected at deletion. L1/L2-relevant retirements:

- **`harmony/harmonicsegmenter.{h,cpp}` — R6 (segment-first spine), LIVE.** The legacy
  greedy-expand segmenter (called at `regionanalyzer.cpp:870`). **#12 keep/reject at deletion:**
  the anchor thresholds `kAnchorMinScore`=1.5, `kAnchorMinDurationTicks`=DIVISION,
  `kRound2MinScore`=1.25 encode a *judgment* about which onsets are structural anchors — the
  change-point slicer replaces this with a pure fact (a boundary at every eligible onset/release),
  so the interpretation is **consciously rejected**, not carried; nothing in the anchor scoring is
  a fact the slicer lacks. The `PlacedRegion` round/confidence metadata is analysis output, not a
  fact to preserve.
- **`detectOnsetSubBoundaries` (Jaccard 0.25) / `detectBassMovementSubBoundaries` (minGap
  2×DIVISION)** in `regiontoneprimitives.cpp` — **R6 Pass-2/2b.** #12: the Jaccard threshold and
  "any bass-PC change fires" rule are segmentation *guesses* the change-point fact supersedes —
  rejected at deletion; the bass-PC-change *signal* itself is a fact already available from the
  note model if a later layer wants it.
- **`collectPitchContext`** (legacy DOM-walk key-context builder) in `regiontoneprimitives.cpp` —
  **R5.** #12: its point-anchored distance weighting is superseded by `pitchContextOverSpan`'s
  span-anchored indexed form; the *window shape* (lookback/lookahead/decay) is the fact to carry
  forward (and it is, via `SpanWindowWeights`), the DOM-walk mechanics are rejected.
- **`findTemporalContext`** (L4 temporal context) — moves to E4 (FQ-3/OI-12), not a pure deletion;
  its previous/next root/quality/bass facts are consumed by L4 and must be **kept** (re-homed),
  not dropped.
- **`chord/chordanalyzer.cpp` + `chord/postscoringgates.cpp`** (tagged RETIRES R1/R9) are L4 and
  out of L1/L2 audit scope — their #12 checks belong to the L4 certification audit; noted here only
  because they intersect the `metricweights.h`→`keymodeanalyzer.h` and regiontone→chord upward deps
  that will dissolve as they retire.

---

## 7. Blinding declaration (protocol P8) — on my honor as a process step

- **NOT YET OPENED at the time of this frozen draft:** `DEFECT_TYPES.md`,
  `cowork_siloed_facts_audit.md`, `cowork_adjudication_dossier.md`. During Task-0 git diagnosis I
  computed `git hash-object` of `DEFECT_TYPES.md` / `cowork_siloed_facts_audit.md` /
  `cowork_adjudication_dossier.md` to prove they were byte-identical to HEAD — **hashing only,
  never reading content**. The enumeration and dispositions in §1–§6 were produced with the
  known-problem catalog withheld (P8 blind-first).
- **Read as required (NOT blinded):** `OPEN_ITEMS.md` (mandatory Task-0.2 read) — its one-line
  register pointers name some already-known items (OI-13 two-segmenters/tpc-fold, OI-77 bass
  recompute, OI-6/EG-5 manifest extension). Where a Pass-1 finding coincides with one of these I
  say so (§3e, §4, §5) — independently re-derived, not new.
- **The blinding boundary is the freeze commit that records this report** (§8). Only *after* that
  commit do I open `DEFECT_TYPES.md` and promote any new problem TYPE (Task 4 step 2). *(This
  section is completed in the fold commit with the first-open declaration + the promoted DT
  rows.)*

---

## 8. Registers touched (Task 5) — see the fold commit

New register rows (next free numbers), each pointing at this report/artifacts:
- **OI-85** — the Task-0 plumbing-sync incident (object DB ahead of disk; two symptoms) + the
  concurrent-edit hazard; DT promotion pending (§7 → Task 4).
- **OI-86** — L1/L2 upward layering deps (`metricweights.h`→key; regiontone*→chord, back-edge
  killed in header only) + mixed-layer grab-bags + the two-metric-weight-tables #6 duplication;
  much rides existing retirements R4/R5/R6 and FQ-8/OI-13.
- **OI-87** — the enumerated L1/L2 constant manifest-gap list (§3c) — concrete EG-5/OI-6 input.

Fire-rate table + dispositions live in `tools/audit/l1l2/`. This report is the frozen Pass-1
artifact; its commit hash is the blinding boundary and is recorded in the fold commit message.
