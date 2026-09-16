# CC Instruction — Phase 5b Step 0: ground the L4 build (read-only investigation + measurement)

> **Why.** Per `cowork_phase5b_l4_build_plan.md`, the L4 build is **incremental with an investigation at every step**.
> This Step 0 grounds the whole sequence: what the new chord path (`chordslicedecoder`) already is vs the spec, how it
> compares to the legacy path **today** (now that the corpus gate is restored), and any **architecture friction** — so
> the increment list and a first engage/no-go read are grounded in fact, not assumption. **READ-ONLY for source (no
> production edits); it MAY *run* the diagnostic corpus comparison (measurement, no production change).**
> *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §0 — Preamble: protect the uncommitted Cowork docs (sweep)
Commit, local-only, `cowork_phase5b_l4_build_plan.md` (new) + the `cowork_l1l4_completion_ledger.md` F16 edit:
`docs(cowork): Phase-5b incremental L4-build plan + F16 done`. Confirm `git show --stat <sha>` lists only docs; report
the sha.

## §1 — `chordslicedecoder` as-built vs the L4 spec (the gap)
Read `chord/chordslicedecoder.{h,cpp}` and `cowork_layer4_chordsymbol_design.md`. Report:
- **What is built:** the per-slice decode path — what it produces (root / quality / inversion / membership), the
  Increment-A naming, the Increment-B membership/`twoPass`, and **what abstain/"uncertain"/inherit handling exists
  today** (the spec's "declare uncertainty, not guess").
- **What is missing vs the spec, precisely:** the symmetric-root **spelling-pin** (Increment-C, consuming the Phase-4
  `engravingbridge/spellingview` primitive) — confirm it is unbuilt; the **three-tier membership rule**; any abstain/
  inherit gap. Map each gap to its spec section.
- **Production status:** confirm `chordslicedecoder` is still production-dead (diagnostic-only via `--decode-chords`),
  i.e. building on it stays byte-identical until engagement.

## §2 — New path vs legacy, measured TODAY (the baseline — uses the restored gate)
Run `chordslicedecoder` over the corpus **diagnostically** (`batch_analyze --decode-chords`, NOT engaged) and compare
its chord identity to the **legacy production** path (the live `analyzeChord`/region output) and/or the GT, on Baroque +
Default. Report:
- where the new per-slice path **agrees vs differs** from legacy, and **by how much** (a BIR-style count);
- the **shape** of the differences (per-slice finer granularity vs per-region; symmetric-root cases the spelling-pin
  would fix; abstain cases);
- so we know how close the new path is to legacy/GT **before** completion (the starting point for Steps 1–n).

## §3 — Architecture friction (the amendment radar)
Assess whether the spec's L4 decomposition still fits the as-built L1–L3, and flag anything that suggests an increment
or the **layer architecture** needs amendment:
- **per-slice (new) vs per-region (legacy):** how does the new chord identity relate to `changePointSlices` (L2)? Does
  the spec's per-slice unit fit the as-built slicer?
- **L3 + section interaction:** how would a per-slice chord path interact with L3 key (which now consumes the slices)
  and the section-stabilization layer the live product runs on top?
- any other friction (bounded-context, the types-leaf, the dense-start config gap) that bears on the build.

## §4 — Deliver
Write `cc_phase5b_step0_report.md` (gitignored): the §1 gap, the §2 measured new-vs-legacy baseline (with numbers), the
§3 friction, and — the point of Step 0 — a **grounded increment sequence** (which sub-builds, in what order) + a **first
engage/no-go read** (is the new path plausibly equivalent-or-better once completed, or does something need a rethink
first?). Report the §0 doc-commit sha. **No production source edits.**

## §5 — Stops
- Any production `src/composing/` source edit → STOP (this is read-only + measurement).
- A push targets `upstream` → STOP.
