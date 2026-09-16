# CC Instruction — ARCHITECTURAL LAYER 4 (chord symbol + non-chord tones): read-only AUDIT (no code)

> Architectural Layer 4 is **signed** (`cowork_layer4_chordsymbol_design.md`). Before any build, pin at source what
> the layer will **reuse**, the real **call sites/seam**, the **tunables**, the **metrics/fixtures**, and the **gaps**
> — exactly as the L3 decoder audit did before the L3 build. **Read-only: produce a dossier, change no code, no
> production behaviour.**
>
> **★ No-assume:** every "as-is" claim cites `file:line` read this session; anything not confirmable → tag
> `[unverified]`, do not guess. Flag anything that contradicts the signed spec so we reconcile before building.

## §1 — The existing chord scorer (the reuse core)
- **`chordanalyzer.{h,cpp}`:** pin the **template set** — the `array<TemplateDef, kTemplateCount>` and `kTemplateCount`
  (cross-check `docs/scoring_model.md` §2): the exact recognized chord **vocabulary** (which triads / sevenths /
  sixths / extensions, per quality), so the build reuses it rather than inventing a new model. Pin `analyzeChord`'s
  scoring shape (how a pitch set scores against a template; the bonuses/gates), and the `ChordAnalysisResult` output
  fields (root pc, quality, **bass/inversion?**, score, alternatives?, any uncertainty?).
- **Confirm the candidate-generation mechanism:** does `analyzeChord` already generate the *complete* set of
  candidate chords (every template at every root) with scores, or only return a single winner? The signed spec makes
  *complete generation* the lever — pin whether the existing code surfaces a full candidate list or must be extended.

## §2 — Sparse / incomplete + bass / post-pass logic (reuse, to be integrated)
- **`sparsechordrefinement.{h,cpp}`:** pin `refineSparseChordQualityFromKeyContext`, `applyTonicPriorToSparseChord`,
  `forceChordTrackQualityFromKeyContext` — the key-diatonic-prior-for-sparse logic the spec reuses (note it currently
  runs as a **post-pass**, to be *integrated* into generation/scoring, not bolted on).
- **`chordpostpasses.cpp`:** pin the bass-anchoring / pedal logic (`cptIsBassChordTone`, Iter-86/91) — the bass→root
  and slash-vs-pedal handling the spec's bass-anchoring reuses.

## §3 — NCT / membership (the largely-NEW part — pin the gap)
- Search for any existing **non-chord-tone / chord-membership** logic (does the current per-region path decide
  per-note chord-tone-vs-NCT, or does it analyse a flattened tone aggregate?). The spec's per-slice, neighbour-aware,
  **binary membership** decision + the **two-pass** neighbour resolution is expected to be largely new — confirm what
  exists vs what must be built, and pin the **metric-weight / stepwise** inputs available per note (onset metric
  position, the note model's fields).

## §4 — tpc / spelling (maximal-information)
- Confirm the **note model carries tpc** (the L1 `NoteEvent` field) and pin whether `chordanalyzer` currently reads it
  or works in **pitch class only**. The spec names the chord root from the **notated spelling** (esp. symmetric
  dim7/aug) — pin what spelling-aware root logic exists vs is new, and where tpc is threaded (or not) into the chord
  path.

## §5 — The seam, the window, the index
- **Seam:** pin the production chord call site — `analyzeChord` @ `regionanalyzer.cpp` (~`:668`) and how `localKey`
  (now the L3 decoder's key, post-wiring) feeds it. This is the per-region call the L4 build re-points to **per-slice**
  (the future wiring seam — pin it, do not change it).
- **Window / context:** pin the windowing primitives available (`weightedPcView`, `pitchContextOverSpan`, the
  neighbour/prevailing-chord context) for the spec's **adaptive lazy-extend** window.
- **Index (perf floor):** confirm the per-slice window must use the **indexed** note query (`NoteModel::overlapping`),
  not a DOM/region walk — the same O(N²)-avoidance the L3 build required.

## §6 — Metrics & fixtures
- Pin the existing **chord-root (BIR) + chord-quality** metric tooling (the gate, `characterise_bir_false` etc.).
- **Flag the missing membership metric:** the spec (§10) requires NCT-membership precision/recall, which the
  chord-root metric does not measure — confirm it does not exist yet (a build deliverable).
- Pin the **chord test fixtures** (`chordanalyzer` tests) the build's behaviour tests extend.

## §7 — Unification preview (so the build starts clean)
List, from source: what the L4 build **reuses** (templates + `analyzeChord` scoring; sparse + bass logic;
`weightedPcView`/`pitchContextOverSpan`; the `keyModeResult` carrier), what is **newly written** (per-slice
orchestration; the adaptive window; the two-pass membership/NCT decision; spelling-aware root naming; the membership
metric), and what **retires** at the eventual wiring (the per-region chord path; the sparse/bass **post-passes** as
bolt-ons, folded into generation). One chord path end-state; surface any pre-existing duplication.

## §8 — Deliverable
`cc_layer4_audit_dossier.md` (held/gitignored): §1–§7 with `file:line` citations, the `[unverified]` list, and any
**spec-vs-source contradictions** to reconcile before the build. **No code, no production change, no commit beyond the
held dossier; `upstream` untouched.**

## §9 — Stop conditions
- Any production code/behaviour would change → STOP (read-only audit).
- A finding contradicts the signed spec (e.g. the templates can't express the spec's vocabulary; no complete
  candidate list; tpc genuinely absent) → record it and STOP for reconciliation, do not design around it silently.
