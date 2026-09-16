# CC Instruction — close the override-readiness gap on the earlier judgment layers (byte-identical)

> **Why.** The newly-ratified architecture principle (the *confidence-weighted forward override*, `cowork_target_architecture.md`
> control-flow contract + `cowork_layer5_function_design.md` §8/§9-D7) lets the function layer (L5) overturn a *confident*
> earlier-layer inference **by selecting among the readings that layer carried forward** — never by re-deriving. A
> read-only source check sized the impact: **the chord layer (L4) already satisfies this** (its `alternatives` +
> `confidenceModel` are filled before the commit/inherit/abstain split and never pruned — VERIFIED), and the **slicing
> layer (L2) is not impacted** (deterministic fact-grid, no alternatives). **The one real gap is the key layer (L3):** it
> *computes* ranked alternative keys per slice (`SliceKeyMode.alternatives`) but **drops them at the slice→region
> reduction** — each `HarmonicRegion` carries only the single chosen key + a scalar confidence, so L5 has no carried key
> menu to select among at the region level. This instruction closes that gap **byte-identically** (carry already-computed
> data forward; nothing consumes it yet) and adds two lock-in tests so neither layer can silently regress.
> *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test runs.)*

## §0 — Preamble (sweep)
Commit local-only any unstaged Cowork docs (the L5 spec, methods catalog, ledger, the architecture-doc control-flow
update): `docs(cowork): L5 spec + confidence-weighted-override + override-readiness assessment`. Report the sha.

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check — verify at source, report)
1. Re-confirm the gap: in the slice→region key reduction (`regionanalyzer.cpp` `localKeyForRegion` ~714/729) only
   `SliceKeyMode.chosen` is consumed; `HarmonicRegion` (`harmonicrhythm.h` ~78–86) has **no ranked-key-alternatives**
   field (its `alternatives` is `ChordAnalysisResult` chord candidates, not keys). Confirm the slice decoder DOES carry
   `SliceKeyMode.alternatives` (+ confidence) on **every** slice (`keymodesequence.h` ~152) — read the producer in
   `keymodesequence.cpp` to VERIFY it is populated on confident (non-uncertain) slices, not only at seams.
2. **★ The byte-identity gate — the load-bearing check.** Determine whether `HarmonicRegion` (or whatever you add the
   field to) is **serialized into any production output**: the `.ours.json` corpus emission, the pipeline snapshot
   goldens, or the notation annotations. If a new field would appear in any of those, it is NOT byte-identical. The new
   field **must be excluded from all production serialization** (it is an in-memory carry for L5 only). Report exactly
   which serializers touch the region and confirm the field can be added without entering any of them.
3. Decide the **reduction** (how region-level alt keys derive from the slices). Default v1: **carry the representative
   slice's `alternatives`** (the `repSlice` that already determines the region's chosen key) + that slice's confidence —
   the minimal, faithful choice. The *exact* reduction (e.g. a vote-ranked union across the region's slices) is refined
   when L5 actually consumes it; since nothing consumes it now, v1 only needs to be a sensible ranked set. State your
   choice. **This v1 is a deliberate, tracked placeholder** — it is pinned precisely as the first task of the L5
   modulation step (the earliest point the consumer is known; standing obligation per `cowork_layer5_function_design.md`
   §15-3). Keep the reduction in one clearly-named helper so that later precise pin is a single-site change.
4. If the field cannot be added without entering a production serializer, or the reduction is not clean (e.g. the region
   has no stable `repSlice`) → **STOP and report** (a design question for Cowork), do not force it.

## §2 — BUILD the byte-identical forward-carry (key layer)
- Add a **ranked alternative-keys field** (+ the carried key confidence) to the region structure, populated from the
  slice-level alternatives at the reduction per §1.3. The region's **chosen key and everything consumed today stay
  byte-identical** — this is additive plumbing of already-computed data with **zero production consumers** (it exists for
  L5).
- **Do not** enter any production serializer with the new field (§1.2). **Do not** change the chosen-key vote, the
  confidence scale, or any downstream key consumer (KeyArea, cadence, pivot).

## §3 — The two override-readiness lock-in tests (oracle-asserted)
- **Key layer (the new carry):** a test asserting that on a **confident region** (not an uncertain seam) the region
  carries a **non-empty ranked alternative-keys list + a key confidence** — locks the forward-carry so a future change
  can't silently drop it again.
- **Chord layer (lock the already-true invariant):** a test asserting `chordslicedecoder` populates a non-empty
  `alternatives` **and** a computed `confidenceModel` on **Commit** and **Inherit** slices (not only Abstain) — locks the
  override material the L4 check found already present.
- Both assert the *contract* (presence + shape), not analyzer-echoed values.

## §4 — Gate (byte-identical)
- **Production byte-identical:** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, **no golden refresh**. Any movement → STOP (the field leaked into an output, or the
  reduction changed a consumed value). The two new tests are additive.

## §5 — ASSESS
- Confirm byte-identical + suites green + the two new tests green. Report the before/after corpus (must be identical) and
  that no serializer changed.

## §6 — Deliver
Commit **locally (unpushed)**: the key-layer additive field + populate + the two lock-in tests (key + chord). Write
`cc_l3_keyalt_forwardcarry_report.md` (gitignored): the §1 confirm (incl. the serializer check), the §2 change, the §3
tests, the §4 gate result, and the commit sha — so Cowork verifies by sha that only the additive field + tests changed
and production is byte-identical.

## §7 — Stops
- The field would enter a production serializer and can't be excluded; or the reduction isn't clean → STOP, report.
- Any corpus/suite/snapshot movement → STOP (not byte-identical). Inference change of any kind → STOP. `upstream` → STOP.
