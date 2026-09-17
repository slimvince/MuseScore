# CC Instruction — LAYER 3 (key/mode): READ-ONLY audit

> Layer 3 (key/mode) is **signed** (`cowork_layer3_keymode_design.md` — read it first; it is the spec). Before any
> code, do the **read-only audit**: verify the as-is `[verify]` items at source, verify the §0.2 scope/scale/
> incrementality/extension (R1–R3) at source, **establish the direct key/mode-vs-ground-truth metric and baseline
> the current resolver**, and pin the path / emission / transition design. **READ-ONLY — no production code, no
> behavior change, no commit of production.** Output a dossier; Cowork verifies; user ratifies; THEN the impl design.
>
> **★ Context you do NOT have (do not re-derive):** L3's ONE job is **key/mode** (`C-major`, `F-mixolydian`) per
> slice — NOT chord symbol, NOT function. The dependency order is fixed (key/mode → chord symbol → function →
> grouping); key/mode is evidenced from the **notes + note-level cadence cues only**, key-agnostic of chord symbols.
> L3 changes analysis behavior (it is NOT byte-identical when built) — but **this audit changes nothing**; any
> diagnostic must leave production output byte-identical.
>
> **★ No-assume rule:** every as-is statement cites `file:line` from a source read; anything not confirmable →
> `[unverified]`, listed, not guessed.

## §1 — Verify the as-is at source (the `[verify]` items)
Read and pin, at `file:line`, the exact behavior of:
1. **`keyresolver.cpp` `resolveKeyAndModeRanked`** — the full flow: the fixed backward lookback (`LOOKBACK_BEATS`),
   the dynamic forward lookahead loop (stop = `dynamicLookaheadConfidenceThreshold` ∨ `dynamicLookaheadMaxBeats`),
   the **hysteresis** block (`hysteresisMargin` / `relativeKeyHysteresisMargin`), the note-based opening, and how
   `prevKeyResult` threads.
2. **`keymodeanalyzer.cpp` `analyzeKeyMode`** — confirm the six scoring terms (scale membership, triad evidence,
   characteristic pitch, true leading tone, key-sig proximity, mode priors), the 252-candidate (tonic × 21-mode)
   sweep, the relative-major/minor disambiguation, the **sigmoid confidence** (top1−top2 gap), and the **weak,
   droppable declared-mode hint** (`declaredModePenalty`, the Stage-4b-i demotion). This is the **emission** the
   path will reuse — pin its inputs/outputs precisely.
3. **`cadencekeyanchor`** — the key-agnostic cadence detection + home anchor (the note-level cadence cue source).
4. **`localmodulationdetector`** — the candidate → establishment (sustained diatonic run) → V→I confirmation →
   conservative commit; confirm it is **key-agnostic** (cannot read the resolved key) and currently **diagnostic
   only** (production never calls it). This is the passing-key-vs-modulation instrument to promote (4d-ii).
5. **`regionanalyzer`** per-region call site — where key/mode is resolved per coarse region (the argmax the path
   replaces).
6. **★ The key-agnostic-of-chords check (design §4.4):** confirm what key/mode evidence currently flows from —
   notes + cadence cues vs anything chord/region-derived. Flag any coupling that would violate "key/mode before
   chord symbol" (so the impl can sever it). `[verify]` precisely.

## §2 — Verify scope / scale / incrementality / extension at source (§0.2 R1–R3)
- **(R1) complexity:** pin the actual complexity of `NoteModel::overlapping()` / range queries and the resolver's
  pitch-context collection + per-region/per-slice loops — **indexed or O(N²)?** State whether it holds at full-act
  scale (the validation harness runs whole acts; shipping runs a selection).
- **(R2) edit-trigger / invalidation:** map the **selection → analyzed range** path (how a user selection becomes
  `[startTick,endTick)`), and whether an edit re-runs a **region** or the **whole score**. `[verify]` the UI/bridge
  invalidation path; if not readable this session, mark `[unverified]` and say what to read.
- **(R3) context extension:** confirm the as-is hybrid (fixed backward `LOOKBACK_BEATS` + dynamic forward
  lookahead) and the two gaps — **asymmetric** (backward is fixed, not lazy) and **scattered** (keyresolver vs
  cadence anchor vs region lookahead). Map every place that reaches outside the current window, so the impl can
  unify + symmetrize them.

## §3 — Establish the DIRECT key/mode-vs-ground-truth metric + baseline (the new gate)
This is the headline of the L3 audit — L3 is the first layer with human ground truth (design §6).
- **Extract ground-truth key/mode per location** from the RN corpora: DCML `localkey`/`globalkey` and/or music21
  `RomanNumeral.key`. Reuse the existing `compare_rn` / `dcml_parser` tooling — confirm at source whether they
  already surface the local key/mode (they handle RN, which carries it). State the extraction precisely.
- **Define the unambiguous vs ambiguous split:** unambiguous = the annotation/parser sources **concur** on the
  local key/mode (the DCML ∧ music21 policy-A analogue); ambiguous = they differ (relative major/minor, modulation
  boundaries, passing-vs-structural). **Report the corpus split** (what fraction is unambiguous) — this sizes the
  done-bar.
- **Baseline the CURRENT resolver** against this ground truth, **read-only** (a diagnostic over the annotated
  corpus, like the L2 proxy — must NOT change production output): the current key/mode correspondence on the
  **unambiguous** cases (the real defect rate today) and behavior on the ambiguous ones. Use a **held-out** split
  where possible (out-of-sample; the Contrapunctus discipline). Report the numbers per preset.
- Scope caveat (state it): the annotated corpora are **major/minor functional**; the modal palette has no ground
  truth (indirectly measured only).

## §4 — Pin the path / emission / transition design (for the impl design — verify feasibility, don't build)
From the §5.1 catalog, confirm at source that the pieces compose, and specify (do not implement):
- **Emission** = the existing `analyzeKeyMode` 252-candidate score (per window/slice). Confirm its interface is
  reusable per-slice over the note model.
- **Path** = a **Viterbi/beam over key/mode states**; transition = key-distance + **self-transition penalty** (the
  principled hysteresis). Confirm whether the existing `ChordPathDecoder` infra is reusable for a key path or a
  dedicated decoder is cleaner; estimate the state space / beam width before it crosses into the **gated joint**
  design (do not design the joint step).
- **Passing keys** = self-transition penalty + **promote `localmodulationdetector` (4d-ii)** + optional
  **multi-timescale (keyscape) persistence** check — confirm the inputs exist key-agnostically.
- **Output representation** (design §1 contract): how the path will carry **ranked alternatives + confidence** and
  mark the **flagged residual** so L4 reads a prior and the gated Stage-5 joint step resolves the rest.
- **Extension protocol** (R3): how L3 (demand) will signal L1/L2 (supply) to grow the span (the passing-key
  backward reach); the stop seed = "until the prevailing/home key is established."
- **Deterministic test cases** to specify for the impl (fixtures over the note model): a clear single-key passage;
  a relative-major/minor pair (the disambiguation); a brief tonicization that must NOT switch the key; a real
  cadence-confirmed modulation that MUST switch; a selection starting mid-tonicization (forces backward extension).

## §5 — Deliver
Write `cc_layer3_keymode_audit_dossier.md`: the §1 as-is map (file:line + exact behavior; `[unverified]` where
not confirmed), the §2 R1–R3 findings, the §3 ground-truth metric definition + the **baseline correspondence
numbers** (current resolver, per preset, unambiguous/ambiguous, held-out) + the corpus split, and the §4 path
design feasibility + test-case spec. **No production code committed.** If a read-only diagnostic/probe was built to
baseline, say exactly what it is and that production is byte-identical. Cowork verifies the citations + that nothing
production changed; user ratifies; then the impl design.

## §6 — Stop conditions
- Any production / behavior / scoring change, or a baseline diagnostic that alters analysis output → STOP (read-only).
- An as-is item or an R1–R3 item cannot be confirmed at source → mark `[unverified]`, do not guess.
- The ground-truth extraction needs a corpus regen or any non-read-only step → STOP and surface (baseline from
  existing scores + annotations + the existing tooling).
- The path design would require building the **gated joint key↔chord** step to work → STOP (out of scope; L3-core
  is bounded feed-forward; the joint step is Stage 5).
