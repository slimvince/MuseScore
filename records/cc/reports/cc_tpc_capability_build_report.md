# Phase 4 (tpc spelling capability) — the shared spelling primitive: BUILD report

**Build-it-right capability, NOT precision tuning. Byte-identical by construction (no production consumer).**
`origin` held, `upstream` untouched, local commit only. Implements `cowork_tpc_capability_design.md` (option B —
the **shared spelling primitive only**; the L3 key-spelling *term* + weight are Phase B; the L4 spelling-pin that
consumes the per-note shape is the next build). Grounded by `cc_tpc_capability_verify_report.md` (tpc 100% populated;
seam correct; no existing shared interpreter). Scope confirmed with Cowork (2026-06-26): **span aggregate is
signature-AGNOSTIC** (centroid + sharp/flat distribution only); the signature key-fit is the Phase-B L3 term.

HEAD at build start: `d7dae4573f` (the §0 docs commit). Build: `setup_and_build.bat`, exit 0, no errors/warnings on
the new TUs (`spellingview_tests.cpp` compiled at `[8/11]`).

---

## 1. The primitive as built

**Where it lives:** `src/composing/analysis/engravingbridge/spellingview.{h,cpp}`, namespace
`mu::composing::analysis::engravingbridge` — **beside** the other Layer-1-derived views (`soundingAt` /
`weightedPcView` / `pitchContextOverSpan` in `regiontonecollector.h` / `regiontoneprimitives.cpp`), **not** inside any
analysis layer. Registered in `src/composing/analysis/CMakeLists.txt` (the `composing_analysis` module).

**Signatures (the single tpc → spelling interpreter, two read shapes of one interpretation):**

```cpp
// per-note (the Layer-4 spelling-pin's input shape)
constexpr int kNoLineOfFifths;          // = TPC_INVALID - TPC_C = -23 (absence sentinel; never a real position)
int lineOfFifths(int tpc);              // tpc - TPC_C (TPC_C=14); C=0, G=+1, F=-1, G♯=+8, A♭=-4; sentinel if !tpcIsValid
int sharpFlatSense(int tpc);            // sign of lineOfFifths: +1 sharp side, -1 flat side, 0 = C / invalid

// over a span (the Phase-B Layer-3 key term's input shape — signature-AGNOSTIC)
struct SpanSpelling { int count; double lofCentroid; int sharpCount, flatCount, naturalCount; };
SpanSpelling spanSpelling(const std::vector<int>& tpcs);   // centroid + sharp/flat/natural distribution
```

**Design points honored:**
- **Presence is `tpcIsValid()`** (engraving, `pitchspelling.h`), **never `tpc >= 0` / `!= -1`.** The flat side of the
  line of fifths is negative (`TPC_F_BB = -1` down to `-8`); a `>= 0` guard would silently drop legitimate flat-side
  spellings. This is the regression the verify report's §5 caveat warned of, and a unit test pins it.
- **The −1 ambiguity is documented, not "fixed" here.** A comment on `lineOfFifths` states plainly that `tpcIsValid`
  keeps the real range but does **not** separate "absent" from a real F𝄫 (both `-1`); that separation is the
  **build-path invariant's** job, a recorded **Layer-1** matter (design §5), out of scope in Phase 4. `NoteEvent`'s
  `-1` default and `0-34` comment were **not** touched.
- **One interpreter.** `lineOfFifths` is the *sole* function that computes `tpc - TPC_C` and the *sole* function that
  applies `tpcIsValid`; `sharpFlatSense` and `spanSpelling` **derive from it** (a `kNoLineOfFifths` return encodes
  "absent/invalid"). The interpretation exists in exactly one place.
- **Reuse, not reinvent:** engraving `Tpc::TPC_C` / `Tpc::TPC_INVALID` / `tpcIsValid()` are reused; no spelling math is
  re-derived. `tpc - TPC_C` is the canonical line-of-fifths normalization (tpc *is* the line-of-fifths index), not a
  reinvention.
- **Signature-agnostic span (option A, Cowork-ratified).** `spanSpelling` takes **no** key signature; it is the
  centroid + distribution only. `analysisutils::diatonicMaskFromFifths` (`[sf-1, sf+5]`) is **not** invoked — it is
  recorded as the **Phase-B L3 key-fit term's** reuse target (using it requires a signature ⇒ that is the deferred
  term), see §4.

---

## 2. Test results (§3 — the only new test surface)

New pure-function suite `src/composing/tests/spellingview_tests.cpp` (`composing_tests` target). **8/8 pass.**

| test | asserts |
|---|---|
| `GSharpAndAFlatGetDifferentLineOfFifths` | G♯ (+8) ≠ A♭ (−4) — the enharmonic distinction (the whole point) |
| `LineOfFifthsIsTpcMinusTpcC` | C=0, G=+1, D=+2, F=−1; range boundaries TPC_MIN=−22, TPC_MAX=+26 |
| `SharpFlatSenseIsSignOfLineOfFifths` | sharp→+1, flat→−1, C→0; naturals away from C are non-zero (by design = LoF side) |
| `FlatSideSpellingIsKeptByTpcIsValidNotDroppedByGteZero` | F𝄫 (tpc −1) is `< 0` (a `>=0` guard would drop it) yet `tpcIsValid`-kept and read at −15 |
| `InvalidTpcReturnsTheAbsenceSentinel` | TPC_INVALID (−9) and out-of-range → `kNoLineOfFifths` / sense 0; sentinel never collides |
| `SpanAggregateMatchesHandComputedCentroidAndDistribution` | {C,G,D,F,A♭,INVALID} → count 5, centroid −0.4, sharp 2 / flat 2 / natural 1; invalid skipped |
| `SpanAggregateOfEmptyOrAllInvalidIsZero` | empty / all-invalid → count 0, centroid 0.0 |
| `DerivedShapesAreConsistentAcrossTheValidRange` | over the full tpc range, sense == sign(LoF) and span counts partition by it (one-interpreter proof) |

---

## 3. Byte-identity proof (§4 — the gate)

The primitive has **no production consumer** in Phase 4, so nothing on the live analysis path moves.

- **Structural (the proof):** a whole-source-tree grep for every primitive symbol (`lineOfFifths`, `sharpFlatSense`,
  `spanSpelling`, `kNoLineOfFifths`) returns references in **exactly three files** — `spellingview.h`,
  `spellingview.cpp`, and `spellingview_tests.cpp`. **Zero** references in L3, L4, the orchestrator, or
  `batch_analyze`. The live path is untouched by construction.
- **`composing_tests`: 643/643 pass** (635 prior + the 8 new; 0 failures). The pre-existing tests are unchanged.
- **`notation_tests`: 53 passed / 4 SKIPPED / 0 FAILED.** The 4 skips are pre-existing, environment/data-gated
  (`MozartK279…`, `…CadenceMarkersOnCorelli`, the two `…HarmonyPinning.BehaviorSnapshot_*`) — not caused by this change.
- **`pipeline_snapshot_tests`: 11 passed / 1 SKIPPED (report generator) / 0 FAILED.** The P1/P2/P3/P4 goldens are
  **byte-identical** — the live four-path chord/key output did not move.
- **Corpus (empirical confirmation):** Baroque + Jazz regenerated with the rebuilt `batch_analyze` (manifest-validated,
  353/353, git `d7dae4573f`) and re-measured with `characterise_bir_false.py`: **Baroque `TOTAL genuine BIR=false: 53`,
  Jazz `24`** — identical to the CLAUDE.md baseline (53 / 24), same case-identity sets (spot-checked: `bwv352@1440` …
  `bwv96.6@13440`; Jazz `bwv272@4320`, `bwv291@17760` …). **Zero movement.** Default follows by the same zero-consumer
  construction.

The change set is exactly: `spellingview.{h,cpp}` (new), `spellingview_tests.cpp` (new), and two `CMakeLists.txt`
registrations (compilation units only — no logic). No existing production logic was edited.

---

## 4. §5 ledger — reuse vs new, and the recorded L4 fold-in target

| concern | reuse (existing) | new (Phase 4) |
|---|---|---|
| tpc → line-of-fifths position | `Tpc::TPC_C` (=14) | `lineOfFifths()` — the one accessor |
| absence sentinel | `Tpc::TPC_INVALID` (=−9) | `kNoLineOfFifths` (= TPC_INVALID − TPC_C) |
| presence / validity test | engraving `tpcIsValid()` | used as the sole presence test (NOT `>= 0`) |
| sharp/flat sense | — (sign of the LoF offset) | `sharpFlatSense()` — derived from `lineOfFifths` |
| span centroid / distribution | — | `spanSpelling()` (signature-agnostic) — derived from `lineOfFifths` |
| signature diatonic window `[sf-1,sf+5]` | `analysisutils::diatonicMaskFromFifths` | **NOT built** — recorded as the **Phase-B L3 key-fit term** reuse target |
| existing L4 inline tpc interpretation | `chordanalyzer.cpp`: `tpcDeltas`, `countTpcMatches`, `tpcConsistencyBonus`, inline `tpcSpellsAsSharp`/`tpc8SpellsAsFlat`, `tpcForPc` (41 sites, confirmed at HEAD) | **the next (L4) build folds these INTO this primitive** — not Phase 4 |

**Recorded for the L4 build (not now):** the L4 spelling-pin must **fold the `chordanalyzer.cpp` inline tpc cluster
into this primitive** so it becomes the sole interpreter once L4 is spelling-aware. Building it now (or wiring any
consumer) is out of Phase-4 scope and would break byte-identity.

**No new parallel path or logic duplication was introduced.** A repo scan confirms the primitive is the single place
that turns a tpc into line-of-fifths / sharp-flat semantics; no second spelling interpreter was added (the L4 inline
cluster is the recorded fold-in target, not a competitor created here).

---

## 5. Scope honored / stops

- Did **not** wire the primitive into any production path (L3/L4/orchestrator/batch_analyze) — zero consumers.
- Did **not** touch `keymodeanalyzer` (the L3 spelling term is Phase B), build the L4 pin, or fold L4's inline cluster.
- Did **not** change `NoteEvent`'s `-1` default or the `0-34` comment (the L1 cleanup).
- Did **not** invoke `diatonicMaskFromFifths` (signature-agnostic span, option A).
- `upstream` never; `origin` held; local commit only. External `cowork_*` doc edits present in the working tree
  (Cowork's own activity) were **left untouched** and excluded from the build commit.
