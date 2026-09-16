# CC Instruction — Phase 4 (tpc spelling capability): build the shared spelling primitive (production untouched)

> **Context.** Phase 4 per the design `cowork_tpc_capability_design.md` (read it — **scope is option B**: build the
> **shared spelling primitive ONLY**; the Architectural Layer 3 key-spelling term + its weight are **Phase B**; the L4
> spelling-pin that consumes the primitive is the **next** build, not this one). This is **build-it-right capability,
> NOT precision tuning** and **NOT inference-problem-fixing** (the discipline: all refactoring/architecture/algorithmic-
> completion before any precision work). It is **byte-identical by construction** — the primitive has **no production
> consumer** in Phase 4, so nothing on the live path can move.
>
> **Grounded facts (verified at source by Cowork — do not re-derive):** `engravingbridge` is the seam — declarations
> in `regiontonecollector.h`: `soundingAt` (:115), `weightedPcView` (:160), `pitchContextOverSpan` (:267);
> `SoundingNote` (:108) carries raw `tpc` but no layer interprets it into line-of-fifths. `NoteEvent.tpc` is assigned
> `e.tpc = n->tpc()` (`note_model.cpp:53`); every build-path note is real, so the `−1` default never survives.
> Spelling math (`pitchspelling.h:40-51`): `TPC_C = 14`, `TPC_F_BB = −1`, `TPC_MIN = −8`, `TPC_MAX = 40`;
> `tpcIsValid(int)` = `val ≥ TPC_MIN && val ≤ TPC_MAX` (`pitchspelling.h:128` / `pitchspelling.cpp:48`). The diatonic
> window `[sf−1, sf+5]` lives in `analysisutils.h` (`diatonicMaskFromFifths`).

## §0 — Preamble: protect the uncommitted Cowork docs
Commit, **local-only**, the uncommitted Cowork doc edits — the new `cowork_tpc_capability_design.md`, the new
`cc_instruction_tpc_capability_verify.md`, and the `cowork_layer3_reachback_design.md` §3 proxy correction:
`docs(cowork): Phase-4 tpc spelling-capability design (option B) + reach-back §3 proxy correction`. Confirm
`git show --stat` lists only those doc files (no source).

## §1 — Build the shared spelling primitive in `engravingbridge` (the sole interpreter)
Add **one** spelling-derived view, **beside** `weightedPcView`/`soundingAt` (not inside any analysis layer), that
interprets the notated `tpc` into spelling semantics. Two read shapes of the **same** interpretation:
- **Per-note:** line-of-fifths position = `tpc − TPC_C` (`TPC_C = 14`; +1 tpc = +1 fifth); sharp/flat **sense** = the
  sign of that offset. (This is the per-note shape the L4 spelling-pin will consume next.)
- **Over a span:** the line-of-fifths **centroid / sharp-flat / natural distribution** of the window's spellings —
  **signature-AGNOSTIC** (no `fifths` / key-signature input). This is the modulation-direction shape; it is NOT a
  signature key-fit. (The aggregate the L3 key term will consume in Phase B.)
- **Presence test is `tpcIsValid()` — NOT `tpc >= 0` / `tpc != −1`.** The flat side is negative (`TPC_F_BB = −1` down
  to `−8`); a `>= 0` guard silently drops legitimate flat-side spellings. Note plainly (comment): `tpcIsValid` keeps
  the real range but does **not** separate "absent" from a real Fbb (both `−1`) — that is the build-path invariant's
  job, not this function's, and is a recorded **L1** matter (design §5), **out of scope here**.
- **Reuse, don't reinvent:** use the engraving helpers (`tpc2alter`/`tpc2pitch`/`tpcIsValid`) for the spelling math.
  Reproduce the line-of-fifths *interpretation* that `cc_layer3_tpc_keymeasure_report.md` §1 measured genuine — but
  **only the signature-agnostic part** (line-of-fifths position, sense, centroid/distribution). Do **not** re-land the
  discarded `--seq-tpc-weight` WIP from stash `bc4fa79…` (reference only).
- **`diatonicMaskFromFifths` is a Phase-B reuse target, NOT a Phase-4 call — do NOT invoke it.** It takes a
  signature `fifths` argument, so using it computes a **signature-relative key-fit** = exactly the L3 key term the
  design defers to Phase B (§2). **Record it** (in the report ledger) as the Phase-B key-fit reuse target; the Phase-4
  span aggregate must take **no** key-signature input. (Corrects the earlier instruction draft + the verify-report §5
  ledger line that wrongly listed the `[sf−1,sf+5]` window / distance-outside as Phase-4-new — that is Phase B.)

## §2 — Explicitly NOT in this build (no consumer; no other layer touched)
- **Do NOT** wire the primitive into any production path — no caller in L3, L4, or the orchestrator. It is built and
  unit-tested, consumed by nobody yet.
- **Do NOT** touch `keymodeanalyzer` — the L3 spelling term is **Phase B**.
- **Do NOT** compute any signature-relative key-fit / diatonic-window membership** (no `diatonicMaskFromFifths` call, no
  `fifths` argument anywhere in the primitive) — that math IS the deferred L3 key term (Phase B). The span aggregate is
  signature-agnostic.
- **Do NOT** build the L4 spelling-pin or fold L4's inline tpc cluster (`tpcForPc`, `tpcSpellsAsSharp`,
  `tpcConsistencyBonus`, …) into the primitive — that is the **next (L4) build**, not Phase 4.
- **Do NOT** change `NoteEvent`'s `−1` default or the `0–34` comment — that is the recorded **L1** cleanup, not Phase 4.

## §3 — Tests (the only new surface — a pure-function unit test)
Add primitive unit tests (its own test target / file):
- **`G♯` ≠ `A♭`:** the two enharmonic spellings get **different** line-of-fifths positions (the whole point).
- **Sharp/flat sense:** a sharp-side spelling reads sharp, a flat-side spelling reads flat; a natural reads 0.
- **Flat-side validity:** a legitimate flat-side spelling (e.g. `TPC_F_BB = −1`) is **kept** by `tpcIsValid()` and
  interpreted at its correct line-of-fifths position — the regression a `>= 0` guard would cause.
- **Span aggregate:** centroid / sharp-flat distribution over a small fixture matches a hand-computed expectation.

## §4 — Gate (byte-identical, trivially)
- **Corpus + `composing_tests` + `notation_tests` + `pipeline_snapshot_tests` ALL unchanged** — there is no production
  consumer, so nothing on the live path moves. **Any movement → STOP** (something wired the primitive in early — a leak).
- The new primitive unit tests pass.

## §5 — Scope, unification, stops
- **One interpreter.** The primitive is the single place that turns `tpc` into line-of-fifths/sharp-flat. Confirm (a
  repo scan) there is still no second spelling interpreter being added. End the report with the reuse-vs-new ledger and
  *"No new parallel path or logic duplication was introduced."*
- Record (for the L4 build, not now) that L4's inline tpc cluster is the fold-in target so the primitive becomes the
  sole interpreter once L4 is built.
- `upstream` never; `origin` held; **local commit only**.

## §6 — Deliver
Commit **locally (unpushed)**: the primitive + its unit tests (the §0 docs already committed). Write
`cc_tpc_capability_build_report.md` (gitignored): the primitive as built (signatures, where it lives), the §3 test
results, the byte-identity proof (no consumer ⇒ corpus/suites/snapshots unchanged), and the §5 ledger.

## §7 — Stop conditions
- Any corpus/suite/snapshot movement → STOP (a production consumer leaked in — Phase 4 must be byte-identical).
- You wire the primitive into L3/L4/the orchestrator, touch `keymodeanalyzer`, build the L4 pin, or change the
  `NoteEvent` default/comment → STOP (out of Phase-4 scope: those are Phase B / the next L4 build / the L1 cleanup).
- A second spelling interpreter appears → STOP (unification).
- A push targets `upstream` → STOP.
