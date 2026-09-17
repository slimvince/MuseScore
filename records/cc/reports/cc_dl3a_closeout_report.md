# CC D-L3a close-out — the sequence margin becomes THE Layer-3 boundary confidence

> **Scope: a DECLARATION-ONLY close-out (comments/naming + doc-sync). NO behavior change** — no
> threshold change, no consumer rewiring, no squash/θ change, no value recomputed. Contract §7
> **D-L3a → ✅ CLOSED**, pre-ratified in principle at the contract ratification (§8.4), evidence in
> hand from the C1 reliability curves (the margin is 2.8–3.1× better calibrated than the emission
> sigmoid on every preset; `cc_c1_reliability_report.md` §3). Byte-identical on production **and**
> dormant — no dormant-output byte change (see §3: no re-pointable D-L5a analogue exists).
>
> **Provenance.** Base HEAD `4d18f44c2d` ([probe] `git rev-parse --short HEAD`). Frozen gate corpus
> manifest `git_hash = 0dd64660f4`, complete, 352/352 each preset. The measurement substrates are
> written to scratch; the frozen corpus is byte-untouched. Every quantitative claim below is
> **[probe]** (ran the tool, read the output).

---

## §0 — The two numbers (identities re-verified at source, Task 0)

| | at-source symbol | what it is | rides the L3 boundary as |
|---|---|---|---|
| **Sequence margin** | `SliceKeyMode.confidence` (`keymodesequence.h:156` — "best vs best-different-key/mode") → reduced to `HarmonicRegion.keyConfidence` (= `rep.confidence`, `regionanalyzer.cpp` `localKeyForRegion`, §15-3) | Class-M decision margin (best whole-sequence total vs best total forced-different-at-this-slice) | **THE boundary confidence** (contract §3) |
| **Emission sigmoid** | `KeyModeAnalysisResult.normalizedConfidence` (`keymodeanalyzer.h:102`; computed `keymodeanalyzer.cpp` `1/(1+exp(-steepness·…))`) | the per-slice analyzeKeyMode winner sigmoid | an **internal gate input + diagnostic** |

**Naming hazard (confirmed, per the dispatch):** the frozen-corpus `.ours.json` region field **named
`keyConfidence` carries the SIGMOID**, not the margin (`batch_analyze.cpp` `writeJson` emits
`key.normalizedConfidence` under that JSON name). The C++ `HarmonicRegion.keyConfidence` field is the
**margin**. This close-out does **not** rename the frozen JSON field (the corpus is frozen); it
declares the roles in the C++ boundary types + docs.

---

## §1 — Task 0: the consumer inventory at source (the knowledge that gated the edit)

Every reader of both numbers, wherever L3's result crosses a layer boundary — production, the dormant
chain, and tools. Class per the dispatch: **(a)** boundary confidence · **(b)** internal
gate/threshold input · **(c)** diagnostic/display export.

### Readers of `HarmonicRegion.keyConfidence` (the sequence margin)

| reader | site | class | note |
|---|---|---|---|
| split-region propagation | `regionanalyzer.cpp:259` (`inheritRegionKeyContext`) | plumbing | copies parent→child; carries the margin forward |
| **L5 confidence-weighted forward override** (DORMANT) | the `HarmonicRegion` carry → `cowork_layer5_function_design.md` §8/§9-D7 | **(a)** | the intended consumer; already reads the margin |
| grouping `keyAreaConfidence` (DORMANT) | `groupinglayer.cpp:101` (via `GroupingUnit.keyConfidence`) | **(a)** | the grouping layer has **no production caller** (assembled only in the `--dump-l6` dump + tests) |
| `--dump-region-keymargin` export | `batch_analyze.cpp:700` (`keySeqMargin`) | **(c)** | the C1 export; already labeled "sequence-margin, diagnostic-only" |
| tests | `regionanalysis_tests.cpp`, `grouping_tests.cpp` | test | — |

**No LIVE production consumer computes with the margin** — dormant L5 + dormant grouping + diagnostic
export only. (Confirmed by the C1 report §1: the standard `AnalyzedRegion` conversion drops the margin
at `batch_analyze.cpp:692`.)

### Readers of `normalizedConfidence` (the emission sigmoid)

| reader | site | class | disposition |
|---|---|---|---|
| **0.8 KeyArea-annotate gate** | `sectionanalyzer.cpp:740/747` (`>= kAnnotateKeyConfidenceThreshold`) | **(b)** | THE production role; **input + constant UNCHANGED** |
| **0.8 assertive-exposure gate** | `sectionanalyzer.cpp:721` → `hasAssertiveKeyConfidence` (`sectioncadencedetection.cpp:52`) | **(b)** | same 0.8 threshold; unchanged |
| `KeyArea.confidence` seed | `sectionanalyzer.cpp:753/759` (→ `analyzed_section.h:136`) | **(c)** | serialized into the pipeline snapshots (`pipeline_snapshot_tests.cpp:711`) — value unchanged ⇒ snapshots stable |
| notation display context | `notationcomposingbridge.cpp:280` (`NoteHarmonicContext.keyConfidence`) | **(c)** | display value; consumed only by notation tests. **Not edited** — outside the pre-authorized file set (only `notationaccessibility.cpp` is pre-authorized under `src/notation/`); recorded here |
| legacy resolver dynamic-lookahead threshold | `keyresolver.cpp:319` | **(b)** LEGACY | the legacy path (contract §3 "Legacy path", retires at engage, R8) — **NOT touched** |
| legacy resolver fallback | `keyresolver.cpp:66` | **(b)** LEGACY | legacy — NOT touched |
| joint-key decision prior (DORMANT) | `jointkeydecision.cpp:243`; `regionanalyzer.cpp:454/496` | dormant | joint-key wiring, gated OFF (`jointKeyWiringEnabled()`) |
| joint re-key stand-in for the margin (DORMANT) | `regionanalyzer.cpp:524` (`region.keyConfidence = conf`) | dormant | sigmoid stands in **because the re-key path has NO sequence margin** (documented at source) — see §3 |
| `.ours.json` / fullspine diagnostic exports | `batch_analyze.cpp` (`keyConfidence`, `homeConf`, …) | **(c)** | the frozen JSON field + fullspine home-key sigmoid; **no margin substrate** — see §3 |

### STOP check (Task 0)

The demotion is a **role declaration** (comments/naming), **not a rewiring**. No live consumer's
input or constant changes — the sigmoid keeps feeding the 0.8 gate exactly as before. **No live
consumer's computation changes ⇒ no STOP tripped.** The legacy path is left untouched (R8). The
frozen-corpus JSON field is left untouched.

---

## §2 — Task 1: the close-out edit (declaration-only, byte-identical)

Comments/naming at the boundary types + wiring; the frozen JSON field name is untouched; renames were
**not** needed (the C++ fields are already distinctly named — `keyConfidence` = margin,
`normalizedConfidence` = sigmoid — so a strengthened declaration comment makes the role real to a
reader without a ripple).

| # | file | edit |
|---|---|---|
| 1 | `harmonicrhythm.h` (`HarmonicRegion`) | declared `keyConfidence` **THE Layer-3 boundary confidence** (Class-M sequence margin, D-L3a), with the sigmoid demoted — block comment + the field's inline `///<` |
| 2 | `keymodeanalyzer.h` (`KeyModeAnalysisResult`) | declared `normalizedConfidence` the **emission sigmoid** — an internal gate input (0.8 annotate gate) + diagnostic, **NOT** the boundary confidence |
| 3 | `keymodesequence.h` | fixed the `decode()` side-effect note: the sigmoid is the gate's **input** (not "the scale the gates are calibrated for" — the C1 evidence shows it is *not* well-calibrated); the margin on `SliceKeyMode.confidence` is THE boundary confidence |
| 4 | `regionanalyzer.cpp` (joint-key fallback comment) | fixed the stale "the real **calibrated** normalizedConfidence" → the local candidate's emission sigmoid, the gate's input, not the boundary confidence |
| 5 | `regionanalyzer.cpp` (joint re-key carry, §15-3 PIN #2) | added a D-L3a note: this is a **documented margin-less stand-in, NOT the re-pointable D-L5a analogue** (§3) |
| 6 | `sectioncadencedetection.cpp` (`hasAssertiveKeyConfidence`) | role note: gates on the sigmoid as an INTERNAL 0.8 threshold; input + constant unchanged |
| 7 | `sectionanalyzer.cpp` (KeyArea gate comment) | role note: the `(b)` clause reads the sigmoid as an internal gate input, not the boundary confidence |

All seven are comment/`///<` text only — **byte-identical compiled output** by construction.

**Doc-sync (same commit):**
- `cowork_confidence_contract.md` — §3 L3 row now states the **margin as THE boundary form** (sigmoid
  demoted, named diagnostic); §7 D-L3a → **✅ CLOSED** citing the C1 evidence + this commit's SHA.
- `cowork_layer3_keymode_design.md` — the output-confidence statement updated to as-built (§0 Terms
  row, §12 glossary, the deferred-follow-ups banner: the "sequence-margin confidence redesign" is
  CLOSED by D-L3a; only the Stage-5 calibration of the margin remains).

---

## §3 — Why NO dormant-output byte change (no re-pointable D-L5a analogue)

The dispatch anticipated a possible dormant-chain site "that publishes the sigmoid AS the L3
confidence (the D-L5a analogue)" to re-point to the margin. Task 0 found **two** dormant sites that
stand the sigmoid in for a boundary-confidence field — and **neither is re-pointable**, because
**neither has a sequence-margin substrate on its path**:

1. **`regionanalyzer.cpp:524`** — the joint-key re-key path (`applyJointKeyWiring`, gated OFF by
   `jointKeyWiringEnabled()`) sets `region.keyConfidence = conf` (the local candidate's sigmoid). The
   source comment already states *"this re-key path has no L3 sequence-margin, so the joint emission
   confidence stands in."* The margin is a whole-sequence Viterbi statistic; the joint re-key does no
   such decode, so **no margin value exists** to publish. (Re-pointing to the *pre-override* margin
   would be wrong — that margin belonged to a *different*, now-overridden key.)
2. **`batch_analyze.cpp:3464`** — the `--dump-l6` grouping dump sets `gu.keyConfidence = homeConf`,
   where `homeConf = homeKey.normalizedConfidence` (a single home-key sigmoid). The fullspine path
   carries no per-unit sequence margin (a bare `KeyModeAnalysisResult` has no margin field), so again
   **no margin substrate**. `homeConf` also feeds `modulationRecompute` here (the F-A incumbent) —
   re-pointing it would *change a dump computation*, which the STOP conditions forbid.

Re-pointing either would require **computing a value that does not exist** → the dispatch's STOP ("the
edit starts wanting a … change"). So the close-out is **declaration-only**; both sites are recorded as
genuine margin-less stand-ins (a **joint-key / L5-wiring / Stage-5 gap**, not this close-out), with a
D-L3a note added at site 1. **No production or dormant output byte changes.**

---

## §4 — Reuse-vs-new + what retires

- **Reuses (unchanged):** every consumer wiring — the 0.8 KeyArea/cadence annotate gate, the L5
  forward-override incumbent (`HarmonicRegion.keyConfidence`), the grouping `keyAreaConfidence`, the
  `--dump-region-keymargin` export — all keep their exact inputs.
- **New:** nothing executable. Only declaration comments + doc-sync.
- **Retires:** the emission sigmoid's **boundary-confidence ROLE** — it is now declared an internal
  gate input + diagnostic, never "the L3 confidence." **No code path is duplicated or removed**; the
  sigmoid keeps its live gate job. (The deferred "sequence-margin confidence redesign" tracked in the
  L3 spec is retired as an open item — subsumed by this close-out; only the Stage-5 Class-M→P
  calibration of the margin remains.)

---

## §5 — Acceptance (measured, not argued)

The no-contamination sandwich — the frozen gate corpus is **byte-untouched** (all substrates written
to scratch under `scratchpad/dl3a/`); the new binary regenerated each preset to scratch and was
diffed against the frozen corpus.

| check | result |
|---|---|
| `composing_tests` | **1083 PASS** (2 disabled) [probe] |
| `notation_tests` | **53 PASS** [probe] |
| `pipeline_snapshot_tests` | **11/11 PASS, NO golden refresh** [probe] |
| standard `.ours.json` byte-identical (new binary → scratch vs frozen corpus) | **0 differing files of 352 ×3 presets** (`cmp -s` each) [probe] |
| gate BEFORE (frozen corpus ×3) | Baroque **53** / Jazz **24** / Default **53** [probe] |
| gate AFTER (new-binary scratch corpus ×3) | Baroque **53** / Jazz **24** / Default **53** [probe] |
| gate 53/24/53 **case-identity set-diff** (frozen ↔ new-binary, `stem@tick`) | **EMPTY ×3** (0 differing lines: 53/24/53 cases) [probe] |

The `.ours.json` byte-identity is the strongest form of the sandwich: the gate is a pure function of
`.ours.json` + the (preset-independent, copied) `.music21.json`, so 0 differing `.ours.json` ⇒ the
case-identity sets are reproduced exactly — confirmed independently by the `stem@tick` set-diff.
`composing_tests` / `notation_tests` are unaffected in behavior (the change is comments only); they
were rebuilt and re-run green.

---

## §6 — Commits (local, unpushed, fork-only)

- **`f6f5137008`** `docs(cowork): D-L3a close-out — sequence margin = THE L3 boundary confidence,
  sigmoid demoted (declaration-only)` — **the code + doc-sync commit** (8 files, +39/−12): the seven
  comment/`///<` edits in `src/composing/` (§2) + `cowork_confidence_contract.md` (§3 L3 row + §7
  D-L3a CLOSED) + `cowork_layer3_keymode_design.md` (§0/§12/banner). All src edits are comment-only
  ⇒ byte-identical compiled output.
- **(this commit)** `docs(cowork): D-L3a close-out report + STATUS/HANDOFF fold` — **this report**
  (force-added; `/cc_*.md` is gitignored) citing the code SHA `f6f5137008`, **plus** the two pending
  Cowork close-out edits folded — `STATUS.md` (the 22j ★ CLOSED note + the D-L3a dispatch line) and
  `COWORK_HANDOFF.md` (header) — **exactly those two**, plus the §7 D-L3a **SHA-stamp**
  (`<DL3A_SHA>` → `f6f5137008`).

**Owned mechanic (the self-SHA circularity, as in session 22j):** a commit cannot contain its own
final SHA, so the §7 D-L3a row's SHA (`f6f5137008` = the *code* commit) is **stamped in the report
commit** (the next commit), not in `f6f5137008` itself. The report cites the *code* SHA per the
dispatch ("own commit citing the code SHA").

**Surfaced, not included (per the dispatch):** `cowork_census_full_needs_audit.md` is a **dirty
untracked Cowork file** from Cowork's parallel Wave-3 scoping (the census §8c audit) — left out of
both commits, surfaced here.
