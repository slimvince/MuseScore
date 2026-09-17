# Wave-2 dependency reconciliation — is E4 a verified key-layer prerequisite?

> **CC, 2026-07-13.** A **READ-ONLY** analysis — stage 1 of the #17 funnel (desk-simulate / probe,
> no build). No `src/` edit, no build, no golden refresh, no register re-scope, no corpus or
> robust-stop write. Dispatch: `cc_instruction_wave2_dependency_reconciliation.md` (Cowork).
> The deliverable is this report + a **proposed** corrected sequence. **Every sequencing and
> re-scoping decision below is the USER's to ratify** — OI-145's own rule is that no key-layer
> build opens while a wave-2 row is open *unless the user explicitly re-scopes a row out*.
> Nothing in the register was edited.
>
> **Freeze:** `8b3811cdce`. Every claim below is verified at the object (the code, the roadmap,
> the design docs) — never from the register's summary of them, never from memory.

---

## 0. The headline

**The OI-145 readiness gate's wave-2 premise is FALSE, and it is false in the direction of
OVER-SCOPING.** Three findings, in order of consequence:

1. **E4 is NOT a key-layer prerequisite. Zero wave-2 rows are Class 1** (key-layer-gating AND
   E4-required). The reason is structural and reproduces at the code: **the rebuilt L3 key
   decoder already reads the correct substrate.** Every duplication the wave-2 rows name
   (two segmenters, two pitch-contexts, two tpc readers, the value-copied window constants)
   lies on the **legacy** side of the legacy-vs-rebuilt seam. The key layer does not touch it.
   The duplications dissolve when the *legacy* half is deleted — which is what "dissolves at E4"
   actually means. It never meant the key layer needs E4.

2. **E4 is far further away than the "dissolves at E4" annotations imply — and had wave 2
   genuinely required it, OI-145 would have been self-contradictory.** E4 is not a next step;
   it is the *fifth* step of the engage program, behind a hard gate, an unbuilt layer, and a
   user-ratification event (§1). A gate that said "finish wave 2, then build the key layer"
   would, if wave 2 truly needed E4, have been saying "build the key layer after the entire
   engage program" — the opposite of the arc's intent.

3. **Two register annotations are factually wrong at HEAD**, both discovered by checking the
   claim at the code rather than accepting it (§4). Both *overstate* a risk to the key layer
   that does not exist. Proposed corrections are recorded with evidence; **neither was applied.**

**Recommended sequence: option (b) + a small (c) residue** — the wave-2 blocker set was
over-scoped. Nine rows (or row-parts) should be re-scoped **out** of the key-layer blocker set to
ride E4 whenever it lands; a **six-item Class-3 residue** is genuinely key-layer-gating,
E4-independent, and byte-identical-now. **E4 should NOT become the next arc.** Details in §6.

**One STOP-and-report item** (§5): the key layer's cadence→key channel would make L3 a consumer
of an L5 fact — a real upward dependency. Cowork's design already names this as "the one genuine
ARCHITECTURE question"; this report confirms it is real at the code and shows it is what actually
governs OI-118/OI-119, *not* E4.

---

## 1. Grounding E4 (§3 of the dispatch) — what it is, what it retires, what it needs first

Pinned from `docs/implementation_roadmap.md` (the ENGAGE CRITERIA + RETIREMENT MAP block,
user-ratified 2026-07-02) and `ARCHITECTURE.md`. **Not from the register's annotations.**

### 1a. What E4 is

E4 is **not a standalone refactor step**. It is the **fourth stage of the six-stage engage
program**, and every stage before it is a prerequisite:

| stage | what it is | status at HEAD |
|---|---|---|
| **E0** | dormant full-spine measurement | ✅ DONE 2026-07-02 — **and it recorded "G2 NOT met today"** |
| **E1** | wire the dormant spine default-OFF (byte-identity proof) | ◻ not done |
| **E2** | measured A/B + the broad-corpus pre-engage reference frozen | ◻ not done |
| **E3** | **default-ON — a USER RATIFICATION EVENT**, one revertible commit | ◻ not done |
| **E4** | **the retirements** (R1…R9) | ◻ not done — *this* is what the annotations point at |
| **E5** | coverage seal + doc flip + deliberate gate re-baseline | ◻ not done |

E4 is the step where the **legacy machinery is DELETED** once the rebuilt spine is live in
production. That is the entire content of the "dissolves at E4" annotations: the *duplicate* dies
because the *legacy* half is removed. **FACT** — roadmap, ENGAGE CRITERIA block.

### 1b. What E4 retires (the retirement map)

The rows below are the R-numbers the wave-2 annotations ride. **FACT** — roadmap retirement map:

- **R1** legacy chord competition + Gates A–L (E4, or Stage 5 if first)
- **R4** dual tpc reader → the shared spelling view *(rides R1)*
- **R5** `resolveKeyAndModeRanked` + `collectPitchContext` shrink *(seed S2 at E4)*
- **R6** segment-first spine *(E4)*
- **R7** `harmonicfunctionlayer` rename *(rides R1)*
- **R8** legacy confidence sentinels *(rides R1/R5)*
- **R9** `chordanalyzer.cpp` file-split — AFTER E4 removals
- **R2** legacy circular cadence detector; **R3** `cadencekeyanchor` kept-as-diagnostic through E4

Note what every one of these has in common: **they all delete or shrink LEGACY code.** None of
them *builds* anything the key layer could read.

### 1c. E4's OWN unmet prerequisites — the finding that changes the picture

E4 cannot be "the next arc". Its prerequisite chain, all verified at the roadmap and the register:

1. **The bounded-context / temporal-extension cluster is a HARD GATE.** Roadmap, user directive
   2026-07-02: *"L6 … is PROHIBITED until the extension behavior is specified → CODED →
   REGRESSION-TESTED for L1–L5."* Sequence: sign `cowork_bounded_context_design.md` → code+test →
   verify → resume L6. **FACT.**
2. **G1 requires L6 built dormant.** The engage gate G1 = "spine complete: L4+L5 dormant-validated
   (✅) + **L6 built dormant** + the A-1 contract as-built deltas closed (D-L3a remains)". L6 is
   `◻ DESIGN v1` in the roadmap's own current-state table. **FACT.**
3. **G2 is explicitly NOT met.** E0's own record: *"G2 NOT met today; residuals named: L4 NCT
   ≈45 % of the EXACT cap, bass/inversion ≈42 %, θ-calibration [D-FS], per-slice key
   feed-forward, L6."* **FACT.**
4. **E3 is a user-ratification event** standing between E2 and E4. **FACT.**
5. **`OPEN_ITEMS.md` section A is titled "STAGE-3 ENTRY GATE — blocks E4/L5 engagement"** and
   carries **OI-1…OI-7 all OPEN** — OI-1 and OI-2 explicitly labeled "prerequisite". **FACT.**

**So: "E4 next" would trip a hard gate (the extension cluster), an unbuilt layer (L6), an unmet
engage gate (G2), a user event (E3), and seven open entry-gate rows.** E4 is not a near-term
step by any reading.

### 1d. E4 (L4) vs the key layer (L3) — the layer-order question the dispatch asked

**FACT** (roadmap current-state table + `ARCHITECTURE.md` §"Layer 3" / §"Layer 4"):

| layer | status |
|---|---|
| **L3 — key/mode** (`KeyModeSequenceDecoder`) | ✅ Built + **LIVE** — the first rebuilt decision layer to go live |
| **L4 — chord (per-slice decoder)** | ✅ Built + **DORMANT** — not wired; engages with L5 |

The architecture is **forward-only**: L1 → L2 → **L3 (key)** → **L4 (chord)** → L5 → L6. **The key
layer sits BELOW E4's subject matter.** L3 is already live; L4 is dormant and engages later.

This is the structural reason finding #1 holds. A lower, already-live layer does not need a
higher, still-dormant layer to be *engaged and then have its legacy predecessor deleted* before it
can be improved. **Had the answer come out the other way — had the key layer genuinely required
E4 — that would itself have been the #7 layering violation to flag.** It did not.

---

## 2. The premise ledger — the ~11 substrate rows (§2 of the dispatch)

Every row below: **Q1** = does the key layer actually depend on it? **Q2** = is it E4-gated, or
doable now byte-identical? Every dependency labeled **FACT** (code/measurement citation),
**THEORY** (design/roadmap citation), or **ASSUMPTION**. Rows that split are split.

---

### OI-86 — L1/L2 layering findings → **SPLITS: Class 2 + Class 3**

**Q2 first (the mechanism), because it decides Q1.**

**(a) The `regiontonecollector.cpp:37` back-edge — Class 3, byte-identical NOW.**
The register's blind-re-run refinement claims the include is not merely upward but **UNUSED**.
**VERIFIED AT CODE (FACT).** `regiontonecollector.cpp:37` is
`#include "composing/analysis/chord/analysisutils.h"`. I enumerated all six symbols that header
exports (`endsWith`, `ionianTonicPcFromFifths`, `normalizePc`, `pcInMask`, `diatonicMaskFromFifths`,
`collectionMask`) and grepped each against that translation unit: **0 references, all six.** The
include is dead. Removing it deletes that specific L1.5→L4 back-edge with **zero behavior change**.

The register annotates *"removal itself waits for the E4 #8 timing."* **That annotation is not
supported.** The include is dead *today*; its removal does not depend on any retirement, because
there is nothing to retire — nothing uses it. It needs a build-confirm, nothing more. **Proposed
correction (§4c).**

**(b) `metricweights.h:42` → `../key/keymodeanalyzer.h` (L1.5→L3) — Class 2.** **VERIFIED (FACT).**
A real upward include. But it points *at* the key layer, not *out of* it: the key layer does not
read `metricweights.h`'s dependency on itself. It is a hygiene concern for L1.5, not a load the key
layer carries. Rides the L1.5/R5-R6 cleanup.

**(c) `regiontoneprimitives.cpp:37/38` → `analysisutils.h` + `chordanalyzer.h` — Class 2.**
**VERIFIED (FACT).** Both includes present. This file hosts `collectPitchContext` — the **legacy**
DOM-walk pitch-context builder (see OI-13 below), which retires at R5. The back-edge dies with it.

**(d) The `SpanWindowWeights` value-copies — Class 2, and the risk claim is REFUTED.**
The register (pass-2 refinement) says `decayRate=0.7` / `lookaheadWeight=0.5` are DT-3 value-copies
of `scoreharvest::DECAY_RATE`/`LOOKAHEAD_WEIGHT`, *"a refit silently diverges."* **This is
overstated and does not reach the key layer — VERIFIED AT CODE (FACT):**
- The literals *are* value-copies: `regiontonecollector.h:249-250`, `= 0.7` / `= 0.5` with a
  **comment** `///< == scoreharvest DECAY_RATE`, not a reference.
- **But the only production construction of `SpanWindowWeights` is `keymodesequence.cpp:86`**, and
  it **overrides all three fields** from `seqPrefs` — the defaults are never taken. (The only
  default-taking constructions in the tree are two *test* call sites,
  `engravingbridge_branch_tests.cpp:601/617`.)
- And `KeyModeSequencePreferences` — the struct the live key decoder actually uses —
  **single-sources BY REFERENCE** (`keymodesequence.h:139-141`):
  `decayRate = scoreharvest::DECAY_RATE`, `lookaheadWeight = scoreharvest::LOOKAHEAD_WEIGHT`,
  plus `changeBaseCost` / `changePerFifthStep` / `relativePairExtraCost` reading
  `kDefaultKeyModeAnalyzerPreferences` by reference — with an explicit code comment saying exactly
  why: *"FQ-7/S8: sourced from the resolver's shared symbols … rather than copied literals, so a
  Stage-5 fit of the resolver's hysteresis/key-distance margins moves these decoder defaults from
  one place."*

**So a Stage-5 refit of `scoreharvest::DECAY_RATE` DOES move the key decoder's `decayRate`.** The
divergence the register warns about is **inert on the production path.** This was the single most
plausible route by which a wave-2 row could have gated the key layer's *fitting* stage — and it is
closed, by design, already. **Proposed correction (§4b).**

**Q1 verdict:** (a) is key-layer-adjacent hygiene, free now → **Class 3**. (b), (c), (d) →
**Class 2** — not key-layer-gating.

---

### OI-13 — FQ-8 owed migrations → **SPLITS: all four parts Class 2**

This is the row I predicted would hide a genuine Class-1 dependency. It does not. Each part,
verified at the code:

**(i) Two segmenters (R6) — Class 2.** **VERIFIED (FACT).** `greedyExpandSegmentation`
(`harmony/harmonicsegmenter.cpp:576`, the legacy segment-first spine) vs `changePointSlices`
(`slicing/slicer.h`, L2). The file's own comment (`harmonicsegmenter.cpp:153-156`) states that L3
**already consumes `changePointSlices`** (`regionanalyzer.cpp:579/651`). **The key layer is already
on the rebuilt segmenter.** The legacy one retires at R6/E4. Not a key-layer dependency.

**(ii) Two pitch-contexts (R5) — Class 2.** **VERIFIED (FACT), and this is the cleanest proof of
the whole report.** `regiontonecollector.h:230-237` declares `collectPitchContext` and documents it
verbatim as: *"**LEGACY** (DOM-walk, point-anchored) … It does NOT use the Layer-1 index. The
indexed, span-anchored successor is `pitchContextOverSpan` (below), **which the Layer-3 key/mode
sequence decoder consumes**; this builder is retired once the decoder is the live key path … Until
then both exist — collectPitchContext stays the **live resolver's** builder, pitchContextOverSpan
the **L3** one."*
Call sites confirm it exactly: `keyresolver.cpp:311` (the legacy `resolveKeyAndModeRanked`, = R5)
calls `collectPitchContext`; `keymodesequence.cpp buildSliceContext` (the live L3 decoder) calls
`pitchContextOverSpan`. **The key layer already reads the correct one.** The duplication is
legacy-side and dissolves at R5/E4 *by construction*.

**(iii) The tpc-reader fold (R4, rides R1) — Class 2 for the DELETION; the key-layer-relevant half
is OI-15, already in the design-resolved set.** **THEORY + FACT.** R4 = "dual tpc reader → the
shared spelling view (rides R1)". The key-layer design *does* want spelling
(`cowork_key_layer_design_opening.md` Decision 2(a), spelling-aware Temperley profiles, "our
spelled-pitch facts already exist at the note layer"). **But the two halves are separable:**
*creating* a shared spelling view (publishing spelling as a first-class evidence fact) does not
require *deleting* the legacy tpc reader. The key layer needs the former; R4/E4 does the latter.
The former is **OI-15**, which OI-145 already (and correctly) places in the DESIGN-RESOLVED set.
**So the tpc row does not gate the key layer; OI-15 does, and it is already correctly classified.**

**(iv) The `function/` dir rename (R7, rides R1) — Class 2.** A directory rename. Zero key-layer
bearing. **FACT** — `analysis/function/` exists; the rename rides R1.

---

### OI-87 — L1/L2 constants not in `param_manifest.json` → **Class 2 (with a Stage-5 caveat)**

**Q2: VERIFIED (FACT).** I grepped `tools/param_manifest.json` (464 lines) for the named constants:
`LOOKBACK_BEATS`, `DECAY_RATE`, `minSilenceTicks`, `coincidenceWeight` — **all absent.** The
manifest gap is real.

**Q2 gating: NOT E4 — Stage-5/EG-5.** The row's own status says so, and the roadmap agrees: the
manifest is the Stage-5 fitter's Phase-0 inventory (OI-6/EG-5). It has nothing to do with the
retirements. **The register's own annotation is right here; the dispatch's suspicion that "most
wave-2 hygiene is E4-gated" does not apply to this row.**

**Q1: NOT key-layer-gating for the BUILD.** Two of the listed constants (`DECAY_RATE`,
`LOOKAHEAD_WEIGHT`) *are* consumed by the key decoder — but by reference (see OI-86(d)), so the fit
moves them correctly whether or not they are registered. Registration is a **fitting-stage
bookkeeping** obligation, and it lands with the key layer's own fitting work, not before its build.
**Class 2** for the key-layer build; a genuine Stage-5 obligation that OI-6/EG-5 already owns.

---

### OI-79 — duplicated constants → **SPLITS: half REFUTED, half Class 2**

**(a) "Emission sigmoid written in two files" — REFUTED AT CODE.** **FACT.**
`normalizedConfidenceSigmoid` is **defined once** (`keymodeanalyzer.h:36`) and **called by
reference** from `keymodeanalyzer.cpp:766`, `keymodeanalyzer.cpp:774`, **and
`keymodesequence.cpp:224`**. It is single-sourced. There is no second emission-sigmoid
implementation. The row's claim is **false at HEAD**. **Proposed correction (§4a).**

**(b) The pedal sigmoid — real, and Class 2.** **FACT.** `chordpostpasses.cpp:271` writes
`1.0 / (1.0 + std::exp(-1.5 * (gap - 2.0)))` — the constants **1.5 / 2.0 hard-inlined** instead of
calling the shared helper with prefs. The code comment admits it: *"Sigmoid constants
(midpoint=2.0, steepness=1.5) are the empirical defaults from ChordAnalyzerPreferences, **inlined
here**…"*. This is a **chord-layer (L4) post-pass**, and per OI-8 the pedal post-pass **dies by
construction at E4** (*"cap→append + pedal clobber + Iter 86/91 die by construction"*). Not
key-layer. **Class 2 — and it may need no fix at all, since its host is deleted.**

---

### OI-63 — mode-prior single-sourcing → **Class 3 (gates the FIT, not the build)**

**Q2: VERIFIED (FACT), E4-independent.** The C++ side is already single-sourced and **test-guarded**:
`modepriorpresets.{h,cpp}` own `modePriorPresets()` / `modePriorAppDefaults()`;
`composingconfiguration.cpp:223` consumes `modePriorAppDefaults()`; and `modepriorpresets_tests.cpp`
holds a field-by-field `EXPECT_DOUBLE_EQ` sync test across all mode fields. Nothing here touches a
retirement. The residual is the **harness half** — which the register itself already routes to
**OI-135 (wave 1)**.

**Q1: KEY-LAYER-GATING — yes, for the FITTING stage.** **THEORY** (`cowork_key_layer_design_opening.md`
Decision 6 + the governing framing, user-ratified 2026-07-13): *"governed by the preset mode-priors,
**FITTED not hand-set**"*, and *"the inventory decision comes FIRST, then the surviving priors are
FIT against the local column at the fitting stage — never hand-set again."* The mode priors are an
explicit key-layer fitting target. If the C++ defaults and the Python harness's copy can diverge, a
refit is unsafe. **Class 3** — but note it gates the **fit**, not the **build**, and its live half
is already wave-1 work (OI-135).

---

### OI-92 — `kJkdTemplates` C++↔Python value-copy → **Class 2**

**Q2: VERIFIED (FACT), E4-independent — but the host is SHELVED.** `jointkeydecision.cpp:73`
declares `kJkdTemplates` (14 entries); the comment at `:68` claims it is *"IDENTICAL to
`tools/cc_joint_residual_probe.py` TEMPLATES"* with no sync test. Real DT-3 duplication.

**Crucially: the host is gated OFF and the design does not reopen it.** `decideJointKey` is called
from `applyJointKeyWiring` (`regionanalyzer.cpp:493`), which is gated on `jointKeyWiringEnabled()`,
**default OFF** (`regionanalyzer.cpp:1472`). And `cowork_key_layer_design_opening.md` Decision 7 is
explicit: *"The shelved joint key↔chord step stays shelved on its measured record; **nothing in this
document reopens it**."*

**Q1: NOT key-layer-gating.** The key layer, by its own ratified design, does not consume the joint
step. A sync test on a shelved, gated-off diagnostic's template table is hygiene, not a blocker.
**Class 2.** (Cheap to fix, and worth doing whenever `jointkeydecision` is next touched — but it
must not block the key layer.)

---

### OI-93 — L3 cross-layer includes → **SPLITS: (a) Class 3, (b) Class 2**

**(a) The two section headers' heavy back-edge — Class 3, byte-identical NOW. VERIFIED (FACT).**
- `section/cadencekeyanchor.h:50` → `#include "composing/analysis/chord/chordanalyzer.h"  // ChordQuality`
- `section/jointkeydecision.h:85` → same include, same reason.
- `ChordQuality` actually lives in the dependency-free types leaf: **`analysis/types/analysistypes.h:139`**.
- I checked whether these headers use *any other* symbol from the heavy `chordanalyzer.h`:
  **they do not.** `cadencekeyanchor.h` references `ChordQuality` 3×; `jointkeydecision.h` 5×;
  **no other `chordanalyzer.h` symbol appears in either.**

So this is a **pure one-line include swap to the types leaf, in each of two headers**, killing an
avoidable L3→L4 header back-edge with **zero behavior change**. It is E4-independent (the leaf
already exists — the same refactor was already applied to `keymodeanalyzer.h` and
`regiontonecollector.h`, and simply **left** here). **Class 3.**

*(Doc-precision nit: the register cites `analysistypes.h:120` for `ChordQuality`; the actual line is
`analysis/types/analysistypes.h:139`. Line drift — noted in §4c, not applied.)*

**(b) Five core-L3 `.cpp` files including `chord/analysisutils.h` for `normalizePc` /
`diatonicMaskFromFifths` — Class 2.** These are dependency-free pitch-class primitives siloed under
`chord/`. Real layering smell, but it rides a **shared-pitch-utils leaf decision** that the register
itself flags — not E4, and not a load the key layer carries (the functions are correct; only their
*home* is wrong). Doable independently whenever the leaf decision is made.

---

### OI-96 — dead field `extraToneScore` in `keymodeanalyzer.cpp` → **Class 3, byte-identical NOW**

**VERIFIED (FACT).** Exhaustive grep across `analysis/`: exactly **two** occurrences —
`keymodeanalyzer.cpp:217` (declaration, `double extraToneScore = 0.0;`) and `:588` (write,
`eval.extraToneScore = 0.0;  // folded into triadScore via scoreTriadEvidence`). **Zero reads.**

**Q1: key-layer-gating — yes**, trivially: it is dead code sitting **inside the key layer's own
central emission file**, which the key-layer work will rewrite (Decision 2, the emission model).
Removing it is waste-removal (#6/#12) in exactly the file the key layer touches first.
**Q2: E4-independent, zero behavior change.** The register's "#8 timing" annotation is satisfied
*by the key-layer work itself* — this is the touch. **Class 3.**

---

### OI-98 — `keyresolver.cpp:107` raw-DOM read → **Class 2**

**VERIFIED (FACT).** `partialSignatureCorrection` (`keyresolver.cpp:107`) walks the engraving DOM
directly (`toChord(cr)->notes()` at `:166`, `n->ppitch()` at `:170`), bypassing the L1 NoteModel.
Real DT-16 layering finding.

**Q1: NOT key-layer-gating for the build.** This is in `keyresolver.cpp` — the **legacy** resolver
(the R5 shrink's subject), not the rebuilt `KeyModeSequenceDecoder`. The row's own text notes the
read may be **irreducible** (the histogram needs a per-segment `keySigEvent().concertKey()` filter
the NoteModel does not expose), and that its caller `resolveKeySignatureContext` is
**KEEP-conscious past the R5 shrink**.
**Q2: the row itself names R5/E4** as the re-homing occasion. Correct. **Class 2** — but flagged:
*if* the key-layer work adopts Decision 4 (re-anchoring at notated mid-piece key changes), the
signature-reading path is exactly what it touches, and the L1 primitive this row asks for
(a signature-scoped pc histogram) may become the natural thing to build then. **Recommend the user
note it as a watch-item for Decision 4, not a blocker.**

---

### OI-99 — dangling doc reference → **Class 3, comment-only, FREE**

**VERIFIED (FACT).** `regionanalyzer.cpp:534` and `:815` both cite
`cowork_phase5c_step4_report.md §6 byte-identity proof`. **That file does not exist in the repo**
(`ls` → no such file; not tracked, not gitignored). Two production source comments pointing at
nothing (#10 doc-sync).

`regionanalyzer.cpp` is the key layer's own region/decode driver — the key-layer work touches it.
Comment-only, zero behavior. **Class 3.**

---

### OI-90 / OI-101 — the file-table reason strings → **Class 3, data-only, FREE, and NOT src/**

**VERIFIED (FACT).** `tools/audit/l1l2/file_table.csv` (33 KB) carries reason strings that the L3
and L4 audits later corrected (`chordpathdecoder.h` is the **chord**-path decoder = L4, not "L3
key-mode decoder scaffolding"; `chordanalyzer.cpp` is the **surviving scorer core**, not whole-file
RETIRES; etc.).

**These are audit *artifacts* under `tools/`, with NO `src/` consumer** — I grepped `src/` for
`file_table`: **zero hits.** Correcting them is a **data/doc edit, no code, no build, no behavior**.
The only reason they are not already fixed is that nobody has touched that CSV. **Class 3, free.**

*(Note: these rows are **not** `src/` substrate at all. Listing them among the wave-2 "`src/`
structural" set is itself a small mis-scoping in OI-145's own wording.)*

---

### OI-97 — `relativeKeyHysteresisMargin` soft-coupling → **Class 3 (gates the FIT)**

**VERIFIED (FACT), with a line correction.** `analysis/types/analysistypes.h`:
- `:801` `double hysteresisMargin = 2.0;  ///< … [empirical]`
- `:807` `double relativeKeyHysteresisMargin = 2.0;  ///< Same-key-sig switch barrier [empirical, = hysteresisMargin by default]`

Two conceptually-distinct knobs sharing a default **by comment, not by reference**. And I confirmed
the row's own caveat: the **decoder's** copies *are* single-sourced —
`keymodesequence.h:139-141` reads `kDefaultKeyModeAnalyzerPreferences.hysteresisMargin` and
`…relativeKeyHysteresisMargin` **by reference**.

**Q1: key-layer-gating — yes, for the FIT.** These two constants **are** the key layer's transition
model: `changeBaseCost` = `hysteresisMargin`, `relativePairExtraCost` = `relativeKeyHysteresisMargin`
(`keymodesequence.h`). Decision 3 of the key-layer design (the stickiness lever, and the
relative-key confusion class) fits exactly these. Refitting `hysteresisMargin` alone silently leaves
`relativeKeyHysteresisMargin` at 2.0. **Real.**
**Q2: E4-independent.** Nothing retires. **Class 3** — the fix is a fitting-stage discipline
("treat the two as independent, or single-source"), and it lands with OI-91 in the manifest.

*(Doc-precision nit: register cites `analysistypes.h:788`; actual `:801`/`:807`. §4c.)*

---

## 3. The other two sets (§4 of the dispatch)

### 3a. The cadence-asset pair — OI-118, OI-119 (+ OI-122(b)/(e))

**Both divergences VERIFIED at code (FACT):**
- **OI-119** — `functioncadence.cpp:387`, inside `tryHalf`:
  `c.genuineDominant = false;  // a seventh WEAKENS a half (not credited)`. Set
  **unconditionally**. The comment describes *neutral*; §5.2 of the L5 design specifies a
  **down-weight**. The *direction* is a spec rule, so its absence is a genuine divergence.
- **OI-118** — `functionmodulation.cpp:52-60`, `decideTonicizationVsModulation` counts **any**
  `FunctionalCadence` with a matching tonic+mode as confirming a modulation; it never checks
  `c.type`, though §5.3(a)/§5.4 **and the file's own header** restrict confirmation to authentic
  or half. A **deceptive** cadence — which by definition *denies* the tonic arrival — would wrongly
  confirm a key change.

**Q1 — do these gate the key layer? YES — but not via E4.** **THEORY**
(`cowork_key_layer_design_opening.md` Decision 3(b)): the cadence→key channel is *"the largest
single precision opportunity in this document"* and *"what holds the true key through a real
modulation … and what the relative floor has been waiting for."* If the key layer consumes cadence
votes, it consumes them from this machinery — and a mis-typed cadence vote would feed the key
decode a false tonic confirmation. **OI-145's framing ("before its votes feed anything") is
correct, and this report confirms it at the code.**

**Q2 — E4-gated? NO.** The rows are annotated *"at the modulation-arbiter engage build"* /
*"at the cadence engage build"*. But **the #8-correct timing is "at the first consumer of the
cadence votes"** — and if the user ratifies the cadence→key channel, **the key layer's own
cadence-channel build IS that first consumption event.** Verified: `FunctionalCadence` today has
**exactly one consumer outside `analysis/function/` — `groupinglayer` (L6)** — and **no L3/key
consumer at all.** So the fixes ride the key-layer cadence build, not E4.

**Proposed:** re-annotate OI-118/OI-119's timing from "at the cadence/modulation engage build" to
"**at the first consumer of the cadence votes**" — which, if Decision 3(b) is ratified, is the key
layer. **Not applied; the user's to ratify.**

**OI-122(b)/(e):** (b) the aug6 ♭6̂-root L4 input assumption — an **L4→L5** contract assumption,
**not** a key-layer input → not key-layer-gating. (e) the `combinedBoundary` `kBoundary<=0` guard
(0/0→NaN, default 1.0 safe, dormant) — a **defensive guard in L5 output**, not a key-layer input →
not key-layer-gating. Both should validate at *their* consumption event. **Neither blocks the key
layer.** *(These are the only two OI-122 parts OI-145 lists; (a)/(c)/(d) are outside this dispatch.)*

### 3b. The design-resolved set — OI-75, OI-81, OI-94, OI-78, OI-15, OI-91, OI-97

OI-145 calls these *"not blockers — the key-layer work itself fixes them."* **The reading holds for
six of seven. One correction, one flag:**

| row | one-line check | verdict |
|---|---|---|
| **OI-75** | `keyAlternatives`/`keyConfidence` published-but-unconsumed; the 0.8 gate reads the emission **sigmoid**, not the better-calibrated **margin** | ✅ **Subsumed** — this IS key-layer Decision 5 (the output surface). Confirmed. |
| **OI-81** | key runner-up margin computed then discarded in-analyzer | ✅ **Subsumed** — Decision 5 verbatim ("ending the computed-then-discarded waste"). **But its register STATUS says "E4 fact-publication design" — that annotation is now wrong**; the key-layer work owns it. §4c. |
| **OI-94** | (a) mid-piece notated key-sig change never re-anchored; (b) the A-3 dominant-implication channel (=OI-68) | ✅ **Subsumed** — (a) is Decision 4 verbatim; (b) is Decision 3/2(b) territory. Confirmed. |
| **OI-78** | `declaredMode` siloed to the key path | ✅ **Subsumed** — Decision 4 ("integrate the declared mode as a graded prior rather than a silo"). Confirmed. |
| **OI-15** | spelling as a first-class evidence primitive | ✅ **Subsumed** — Decision 2(a) (spelling-aware profiles). **And this is the row that absorbs OI-13's tpc half** (§2, OI-13(iii)) — worth stating explicitly, because it is the *only* thing that made OI-13 look key-layer-gating. |
| **OI-91** | the ENTIRE L3 emission surface absent from `param_manifest.json` | ⚠️ **Subsumed but load-bearing** — it lands with the key layer's fitting stage (Decision 2(e)/6). **Flag:** the row asks a question nobody has answered — *"Cross-check whether `cowork_stage5_fitter_design.md` deliberately defers L3 key-emission fitting; if not, a coverage gap."* **That cross-check is still owed** and the key-layer fitting work depends on the answer. Recommend it be done before the fitting stage opens. |
| **OI-97** | the two hysteresis knobs (§2 above) | ✅ **Subsumed** — lands with OI-91 in the manifest, as its own status says. |

---

## 4. Proposed register corrections (evidence recorded; **none applied**)

Per the dispatch: *"If the analysis finds a register annotation that is factually wrong … record it
as a proposed correction with the evidence — do not apply it."*

### 4a. OI-79 — "emission sigmoid written in two files" is **FALSE at HEAD**
**Evidence:** `normalizedConfidenceSigmoid` is defined once (`keymodeanalyzer.h:36`) and called by
reference from `keymodeanalyzer.cpp:766`, `:774`, and `keymodesequence.cpp:224`. Grep for a second
sigmoid body across the module returns only `chordpostpasses.cpp:271` (the *pedal* sigmoid) and
`textureclassifier.cpp:111` (an unrelated distance kernel).
**Proposed:** strike the emission-sigmoid clause; the row's genuine content is the **pedal sigmoid**
only (`chordpostpasses.cpp:271`, constants 1.5/2.0 inlined), which is L4 and dies at E4 per OI-8.

### 4b. OI-86 (pass-2 refinement) — "a refit silently diverges" is **overstated**
**Evidence:** the only production `SpanWindowWeights` construction (`keymodesequence.cpp:86`)
overrides every field from `KeyModeSequencePreferences`, which single-sources
`decayRate`/`lookaheadWeight` **by reference** to `scoreharvest::DECAY_RATE`/`LOOKAHEAD_WEIGHT`
(`keymodesequence.h:139-141`, with the explicit FQ-7/S8 comment). Default-taking constructions exist
only in two test call sites.
**Proposed:** amend to "the `SpanWindowWeights` *defaults* are value-copies; **inert on the
production path** — the sole production caller overrides them from the by-reference
`KeyModeSequencePreferences`. A Stage-5 refit of `scoreharvest::DECAY_RATE` **does** move the key
decoder."

### 4c. Three smaller corrections
- **OI-86(a):** *"removal itself waits for the E4 #8 timing"* — **not supported.** The
  `regiontonecollector.cpp:37` include is **dead** (all 6 exported symbols unreferenced in the TU);
  its removal depends on no retirement. Needs a build-confirm only.
- **OI-81 status:** *"OPEN — E4 fact-publication design"* — the key-layer design (Decision 5) now
  owns this. Not E4.
- **Line drift (doc-precision, #10):** OI-93 cites `analysistypes.h:120` for `ChordQuality`
  (actual: `analysis/types/analysistypes.h:139`); OI-97 cites `analysistypes.h:788` (actual:
  `:801`/`:807`).

---

## 5. STOP-and-report — the one #7 layering item

**The key layer's cadence→key channel would make L3 (key) a consumer of an L5 (function) fact.**

**Confirmed at the code (FACT):** the cadence machinery the design points at
(`cowork_key_layer_design_opening.md` Decision 3(b): *"the dormant, certified layer-5 cadence
machinery (`functioncadence.cpp`) appears to BE that pre-scan's built form"*) lives at
**`analysis/function/functioncadence.cpp` = L5**. `FunctionalCadence` today has **exactly one
consumer outside `analysis/function/`: `groupinglayer` (L6)** — i.e. it is currently consumed only
*downward-forward*. A key-layer (L3) consumer would be a **new upward L5→L3 dependency**, which the
forward-only architecture does not permit as a back-edge.

**This is not a missed dependency — Cowork's design already names it** as *"the one genuine
ARCHITECTURE question in this conversation: where the key-agnostic cadence primitive LIVES so that
layer rules hold — published as an early analysis fact consumable by the key decode, versus consumed
later as the forward-override trigger."* **I am reporting it because it is now CONFIRMED real at the
code, and because it — not E4 — is what actually governs OI-118/OI-119.**

Note also (`ARCHITECTURE.md` §2.14, ratified): the architecture **already sanctions** the
**cadence-confirmed key override** as a forward recompute. So the second horn (consume later as a
forward-override trigger) is already legal; only the first horn (publish a key-agnostic cadence
primitive early enough for L3 to read) needs a home decision. **This decision is the user's, and it
belongs to the key-layer design conversation — not to this reconciliation.**

---

## 6. The recommended corrected sequence — **option (b) + a Class-3 residue**

### 6a. The class partition

| class | rows | count |
|---|---|---|
| **Class 1** — key-layer-gating AND E4-required | **— none —** | **0** |
| **Class 2** — NOT key-layer-gating (re-scope out; ride E4 or their own gate) | OI-86(b)(c)(d), **OI-13 (all four parts)**, OI-87, OI-79(b) *(and (a) is refuted)*, OI-92, OI-93(b), OI-98 | **9 rows/parts** |
| **Class 3** — key-layer-gating, E4-independent, byte-identical now | **OI-86(a)** (dead include), **OI-93(a)** (2× include swap), **OI-96** (dead field), **OI-99** (dangling doc ref), **OI-90/OI-101** (file-table data, not `src/`), **OI-63** + **OI-97** (fitting-independence; land with OI-91) | **6** |

**Plus, outside the substrate set:** the **cadence pair OI-118/OI-119** is genuinely
key-layer-gating (for the cadence channel) and **E4-independent** — it rides the key layer's own
cadence-channel build, if the user ratifies Decision 3(b).

### 6b. The recommendation

**E4 should NOT become the next arc.** It is not a key-layer prerequisite (§1d, §2 — zero Class-1
rows), and it is not reachable anyway without first clearing a hard gate (the bounded-context
cluster), an unbuilt layer (L6), an unmet engage gate (G2), a user-ratification event (E3), and
OI-1…OI-7 (§1c).

**Proposed to the user, for ratification:**

1. **Re-scope the 9 Class-2 rows/parts OUT of the key-layer blocker set.** They are legacy-side
   duplications that the rebuilt key decoder does not touch; they dissolve when their legacy half is
   deleted at E4/R1–R6, and they gate nothing the key layer reads. Keep their register rows OPEN
   (they are real hygiene) — just not as key-layer blockers.
2. **Do the 6-item Class-3 residue now, as one byte-identical `src/`-hygiene commit** (plus the
   data-only file-table fix). It is small, it is all inside the key layer's own files, it needs no
   retirement, and it is exactly the kind of work OI-145's rationale was written for. *(Note OI-86(a)
   and OI-93(a) are compile-affecting and need a build-confirm + both suites; OI-96/OI-99 are
   dead-code/comment; OI-90/OI-101 are `tools/` data. OI-63/OI-97 are fitting-stage discipline that
   land with OI-91, not code today.)*
3. **Move OI-118/OI-119 out of "wave 2" framing and attach them to the key layer's cadence-channel
   build** — the #8-correct consumption event — contingent on the user ratifying Decision 3(b).
4. **Answer OI-91's owed cross-check** (does `cowork_stage5_fitter_design.md` deliberately defer L3
   key-emission fitting?) before the key layer's fitting stage opens.
5. **Then open the key layer's own #17 funnel** — the four read-only probes in
   `cowork_key_layer_design_opening.md` §4 are all cheap and none of them depends on any wave-2 row.
6. **Settle the §5 layering question** (where the key-agnostic cadence primitive lives) inside the
   key-layer design conversation, before the cadence channel is built.

**What this does NOT propose:** touching OI-145's scope, any register row, any `src/` file, or any
build. All of the above is the user's to ratify.

---

## 7. Premise Gate — predictions vs findings (#17b / #3)

Predictions were written **before** the roadmap, the design docs, and the code were opened
(scratchpad, this session; reproduced verbatim).

| # | prediction | finding | gap |
|---|---|---|---|
| **P1** | Class 1: **1–2** · Class 2: **5–6** · Class 3: **3–4** | Class 1: **0** · Class 2: **9** · Class 3: **6** | **Class 1 over-predicted.** I expected the tpc/spelling row (OI-13/R4) to be a genuine E4-required key-layer dependency. It is not — because *creating* the shared spelling view is separable from *deleting* the legacy tpc reader, and the creation half is already OI-15 in the design-resolved set. **The diagnostic lesson: I conflated a duplication's *resolution* with its *deletion*.** That conflation is, I now think, exactly the error the "dissolves at E4" annotations encode — which is why the gate over-scoped. |
| **P2** | E4 is **NOT** a verified key-layer prerequisite (L4 sits above L3; expecting a #7 inversion if it were) | **CONFIRMED** — zero Class-1 rows; L3 is live and below L4 | none |
| **P3** | E4 **has** unmet prerequisites (predicted: OI-1/OI-2) | **CONFIRMED, and far larger than predicted** — the bounded-context hard gate, L6 unbuilt, G2 unmet, E3 a user event, *and* OI-1…OI-7 | **Under-predicted by a wide margin.** I predicted two open rows; the real answer is an entire program. **This is the diagnostic that matters most:** the phrase "dissolves at E4" *reads* like a near-term timing note, but E4 is five stages and a hard gate away. Any row annotated "waits for E4" has effectively been annotated "waits for the entire engage program" — and I do not believe that was the intent when those annotations were written. |
| **P4** | If most rows are Class 2/3, the gate merely over-scoped → correction is a re-scope, not a re-sequence | **This is what happened.** | none |

---

## 8. Self-check against the standing instructions

Per CLAUDE.md ("The self-check after every coding exercise"), re-read against the actual diff:

- **Read-only respected.** The only files written this session: this report, the
  `STATUS.md`/`cowork_handoff.md` notes, and the force-added instruction file. **No `src/` edit, no
  build, no test run, no golden refresh, no corpus/robust-stop write, no register edit, no re-scope.**
- **#17a (label every load-bearing premise).** Every dependency in §2/§3 is labeled FACT (with a
  file:line citation), THEORY (design/roadmap citation), or ASSUMPTION. No unlabeled load.
- **#17b (prediction before check).** §7. Predictions written before any object was opened.
- **#19 (never trust an unestablished claim).** Every register annotation was re-checked at the
  code. **Three were found wrong or overstated** (§4) — which is the whole justification for the
  dispatch's "a register annotation is a lead, not a fact" rule.
- **#3/#13 (surprise = STOP, not build-around).** The one genuine surprise — the L5→L3 cadence
  dependency — is surfaced in §5 as a STOP, not designed around.
- **Conventions.** American English. **No self-invented labels** — I used only OI-N, R1…R9/E0…E5,
  FQ-8, the layer names, and the principle numbers the repository already owns. Where a thing had no
  name (e.g. "the legacy-vs-rebuilt seam") I described it in plain words rather than coining a tag.
- **#10 (doc-sync).** Three doc-precision drifts found (§4c) — recorded as proposed corrections, not
  silently fixed.
- **Deliverable is a proposal.** §6 recommends; it does not decide. Every item is marked as the
  user's to ratify.

*Cross-references: `OPEN_ITEMS.md` (OI-145 the readiness gate; OI-13/OI-15/OI-63/OI-75/OI-79/OI-81/
OI-86/OI-87/OI-90/OI-91/OI-92/OI-93/OI-94/OI-96/OI-97/OI-98/OI-99/OI-101/OI-118/OI-119/OI-122);
`docs/implementation_roadmap.md` (ENGAGE CRITERIA + retirement map; the temporal-extension hard
gate); `ARCHITECTURE.md` (the forward-only layer order; §2.14 the ratified frame);
`cowork_key_layer_design_opening.md` (Decisions 1–7); `cowork_evidence_inventory.md` (wave 3's
menu); `cc_instruction_wave2_dependency_reconciliation.md` (this dispatch).*
