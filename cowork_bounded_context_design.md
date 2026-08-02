# Bounded context & selection-extension — cross-layer architecture & design

> **Status: SIGNED (user, 2026-07-02) — THE GATE (user directive, same day): L6 is prohibited until this design is
> CODED and REGRESSION-TESTED for L1–L5 (the §11 acceptance list).** The coding+test instruction is written
> just-in-time AFTER the gap-analysis v2 report lands (its Dimension-A completeness matrix may surface additional
> per-layer obligations to fold into the build). Consolidation note (2026-07-02): the
> short-lived duplicate `cowork_temporal_extension_contract.md` is KILLED and its novel content merged here — the
> **L5 discovery rule + pinned decision-context extent** (§5), the **L4 decision-relevance sharpening** (§5), the
> **denial provenance** (§3 item 10), and the **gate-proof framing** of the degenerate case (§8). This document is
> the ONE cross-layer extension spec; ARCHITECTURE §2.15's bounded-context bullet points here.
> A cross-cutting design (it spans Architectural Layers 1–6, not one layer). It
> replaces the assumption silently baked into the current code — *"the whole score is always loaded, so every layer
> can see any context it wants and never has to ask for more"* — with the model the shipped product actually needs:
> the analysis works on the **user's selection**, and a layer that needs evidence beyond the selection **asks for it**.
> Designed **before** Architectural Layer 4 and above are built, because the assumption is foundational: building more
> layers on "infinite context" bakes it deeper, and unwinding it afterward is a cross-cutting, expensive retrofit.
> *(Deployment view and Human-interface design are N/A — backend analysis code.)*

## 1. Introduction & purpose

The shipped product analyses **the part of the score the user has selected**, never the whole score. (Reading a whole
score start-to-end happens only in the offline batch-testing harness, which is not part of the product.) A selection
is a **temporal subset** of the piece, and a layer often needs evidence from *outside* the selection to judge its
edges correctly — the key established *before* the selection begins, a chord's neighbour just *past* the selection's
end. The current code sidesteps this by loading the whole score regardless, so all context is incidentally present.
That is the wrong foundation for the product, and the wrong thing to build on.

This design defines the **bounded-context** model: Architectural Layer 1 loads the selection; any layer works within
what is currently loaded and **explicitly requests more context** when its reasoning needs it; the request terminates
at a layer-chosen stop condition, a hard bound, or the score's own start/end. It is designed now so every layer above
is built to obey it, rather than built to assume infinite context and retrofitted later.

## 2. The three spans (the core distinction)

- **Selection span** — what the user picked. It is the **output span**: analysis labels are emitted only for the
  selection.
- **Loaded span** — what Architectural Layer 1 currently holds. It **starts equal to the selection** and grows by
  extension. Always **selection ⊆ loaded ⊆ score**.
- **Score** — the whole piece; the hard outer bound that extension can never pass.
- **Context (evidence) span** — *loaded minus selection*: the extra music a layer pulled in **as evidence only**,
  never labelled in the output.

**Invariant.** The analysis output covers **exactly the selection**; everything outside it is evidence, never a
result.

**The whole-score case is the degenerate case.** When the selection *is* the whole score (batch testing), the loaded
span already spans the piece, no layer's edge reasoning has anywhere to extend to, and **no extension ever fires** —
so behaviour is identical to today. The bounded model therefore *generalises* the current behaviour; "load the whole
score" is simply the special case "selection = score." This is what keeps the batch-testing path unchanged.

## 3. The bounded-context contract (what every layer obeys)

1. A layer **never reads notes or slices outside the loaded span.**
2. When a layer's reasoning needs evidence beyond the loaded span, it either **(a) requests an extension** from
   Architectural Layer 1 in that direction, or **(b) recognises it has reached the score boundary** (nothing more
   exists) and proceeds with what it has.
3. A layer must distinguish **"unavailable because not loaded"** (→ request extension) from **"unavailable because the
   score starts/ends here"** (→ proceed, truncated). Architectural Layer 1 reports which.
4. A layer **outputs analysis only for the selection**; extended context is evidence, never labelled.
5. A layer **never guesses how much** more context it needs — guessing an amount is the un-knowledge-based move this
   contract forbids. It knows *what* it needs, not how far away that is, so it **extends incrementally and stops on a
   principled condition**; the amount is **discovered, not chosen**.
6. The principled stop is **convergence**: extend until the layer's **in-selection output stops changing** with
   further context. This is self-validating — you have enough context exactly when adding more does not change the
   answer — and it is what keeps the result independent of the extension step size (the equivalence invariant, §4). In
   practice a layer uses a **domain proxy that *implies* convergence** rather than re-checking its whole output each
   step (Architectural Layer 3 reach-back: *"a settled, stable prevailing key is in view"* — once a confident earlier
   key is established, the change-cost/decay means reaching further back will not move the selection's leading-edge
   key). The proxy is validated **once, in design**, to imply convergence.
7. Every extension also carries a **hard bound** (a maximum reach) and terminates at the **score boundary** — these are
   **safety caps for the pathological "never converges," not the needed amount**, with a no-oscillation guard.
8. The **increment size** — how much to load per step before re-checking convergence — is **chosen by the requesting
   layer; it is not fixed and not Architectural Layer 1's to decide.** Architectural Layer 1 is domain-blind, and no
   single size fits every layer (Architectural Layer 3 probes at phrase/measure scale, Architectural Layer 4 at
   harmony/slice scale), so the requester sets it to **its own natural inference scale** — the smallest step that
   could plausibly change its output (knowledge, not a guess). It is an **efficiency knob only**: a larger increment
   means fewer round-trips (and perhaps a slightly larger final loaded span), never a different answer, because
   convergence (item 6) fixes the result. Mechanically this is forced — the requester owns the *extend → re-infer →
   re-check* loop, and Architectural Layer 1's *extend* executes **exactly the one requested step and never evaluates
   convergence** (that would be inference, which it does not do), so the increment can only be a per-call parameter
   from the requester.
10. **Denial/truncation is honest, never silent (merged 2026-07-02).** When an extension is refused (hard bound,
   score boundary at a *selection* edge with the stop condition unmet, or a driver-level safety cap), the layer
   proceeds on truncated evidence AND the affected output carries **`clipped-by-selection-edge`** provenance
   (+ `cue-denied` where a request was actually refused) — a truncated result is never presented as a complete one.
   Layer 6 (when resumed) surfaces these marks and the `extension-cue` tag (its §5.1 amendment); it never acts on them.
9. **Units.** The request to Architectural Layer 1 is in **ticks** — it is unit-blind (it loads a time range, it knows
   nothing of slices or measures). The **fundamental quantum of meaning is the slice (change-point)**: the sounding
   set is constant within a slice, so no analysis can change at finer granularity — a **beat or sub-change-point step
   would load no new note and change nothing**, so requesters never reach finer than a change-point. Above that floor,
   the requester steps in **its own natural unit** and converts to a tick target: Architectural Layer 3 reach-back in
   **measures** (a key's scale, and a notation boundary nameable before the earlier notes are loaded); Architectural
   Layer 4's window in **slices**. The new slices then emerge from Architectural Layer 2 re-slicing the loaded region —
   the requester never enumerates them to Architectural Layer 1.

## 4. The protocol — request → supply → bounded recompute

- **Request.** A layer asks Architectural Layer 1: *"extend the loaded span in direction D (earlier / later in time)
  until my stop condition holds, or my hard bound is reached, or the score boundary is reached."*
- **Supply (Architectural Layer 1).** It loads the additional notes in that direction, **appends** them to the note
  model (never dropping already-loaded notes), keeps its look-up index consistent, and returns the **new loaded span**
  and **whether the score boundary was hit**. Re-requesting an already-loaded span is a **no-op** (idempotent).
- **Bounded recompute — a fresh forward re-inference, not a patch.** "Re-run" means each affected layer **re-infers as
  if running for the first time** over the enlarged loaded span — never a local patch of its previous output.
  Architectural Layer 2 re-slices over the enlarged span: its **interior** real change-points are stable, but the
  **edge slice abutting the old loaded boundary extends** into the newly-loaded context (the old clip boundary was
  artificial, not a real change-point — see `cowork_layer2_reslice_design.md` §3). This is benign: what guarantees
  correctness is **re-slice equivalence** (the result equals a fresh slice over the enlarged span), and the edge
  extension is exactly the "more context at the leading edge" convergence (§3.6) absorbs. The requesting layer then
  **re-infers** with the new context in view; and because more context can
  change *what it decides*, **its changed inference propagates forward** — every inferring layer **after** it re-infers
  in turn (a different leading-edge key changes the chord there, which changes the function, and so on). The requesting
  layer re-tests its stop condition; if still unmet and neither the hard bound nor the score boundary is reached, it may
  extend again.
- **The re-inference cascade IS the forward-only contract, not an exception to it.** The extension **request** is a
  data-supply call **down** to Architectural Layer 1 (a higher layer using a lower layer's service — control, not
  inference). The new notes and every re-inference then flow **forward** (Architectural Layer 1 → 2 → 3 → …), exactly
  as on a first run. **Inference never flows backward** — a later layer re-inferring cannot alter an earlier layer's
  result. So an extension is precisely *"ask down for more raw material, then infer forward again,"* with no backward
  inference edge anywhere; this is what makes it consistent with the project's forward-only analysis contract.
- **Equivalence invariant (the correctness guard).** The result after **any** sequence of extensions must equal a
  **single fresh run over the final loaded span** — extension is an optimisation of *"load more, then run from
  scratch,"* never a different computation. In practice the forward cascade is **bounded**: the new context changes
  inference only where it actually reaches (a carried-in key affects the leading-edge slices and decays inward), so
  only the affected slices re-infer — the same locality that makes the stop condition terminate, and which composes
  with the existing *"re-analyse a sub-range"* capability.

## 5. Per-layer roles

- **Architectural Layer 1 — the supplier.** Owns the loaded span; offers *build over a selection* and *extend(direction,
  stop, bound)*. Extension is **append-only**, keeps the index consistent, **clamps at the score's start/end**, and
  **reports boundary-reached**. It holds **no analysis knowledge** — it supplies notes; the *decision* to extend, and
  the stop condition, belong to the requesting layer (single responsibility).
- **Architectural Layer 2 — re-slice on extend.** When the loaded span grows, it produces the change-point slices for
  the **newly loaded region**, preserving complete coverage and slice identity over the larger span. Slices that fall
  in the context span are usable as evidence but are **not** output.
- **Architectural Layer 3 — the main consumer today (reach-back).** Reach-back **is** an extension request: direction
  = earlier, stop = *"the prevailing key before the selection is in view"*, bound = a maximum reach. Its per-slice
  evidence window (± a few beats) at the **leading edge** of the selection requests extension, or truncates at the
  score start. The whole-run decode then runs over selection slices **plus** context slices; the context slices
  **anchor the carried-in key**, and output is emitted only for the selection slices.
- **Architectural Layer 4 — forward-compatible (built later, but its contract is fixed here).** Its neighbour window
  (the slice ± a few neighbour slices, and the rewritten *"extend until the chord is in view, stop at the first
  inconsistent slice"* rule) must, at a **selection edge**, **request extension or recognise the score boundary** —
  never assume the neighbour slice exists. Designing this now is the whole point: Architectural Layer 4 is built to the
  bounded contract, not to "neighbours are always there." **Discovery sharpening (merged 2026-07-02):** the request
  fires only when the truncation is **decision-relevant** — the decision under the truncated window is not already a
  full-margin `Commit` (a truncated window whose evidence sufficed requests nothing). *(As-built status: this
  request path is UNCODED — the window silently truncates; gap-analysis item #5. The build item of this design.)*
- **Architectural Layer 5 — discovery rule + the pinned decision-context extent (merged 2026-07-02; pins the L5
  spec's §15-3, which deferred the extent to "engagement time").** A slice's **decision-context span** extends
  forward until the FIRST of: **(i)** a cadence-anchored function (a chord whose function a §5.2 cadence fixed),
  **(ii)** a punctuation boundary (the L1.5 primitive's picked tick), **(iii)** a hard bound of `K` slices / `B`
  beats (settings — the §3.7 safety cap). **Discovery:** a §5.5 resolution, §5.2 vote aggregation, or §5.3
  persistence decision whose span was cut by the **selection edge before any of (i)–(iii) held** requests a forward
  extension (stop = any of (i)–(iii); increment = its natural unit, slices). Extension re-runs flow forward under the
  §8 one-pass closure (an extension may finalize an open decision, never re-open a closed one — data supply, not a
  back-edge). Denied → the decision resolves on what it saw (or its honest open mark) + the item-10 provenance.
- **Architectural Layer 6 — consumer only (forward note).** L6 requests nothing (assembly); it surfaces the item-10
  provenance and the `extension-cue` tag (L6 §5.1 amendment, 2026-07-02).

## 6. Runtime view (scenarios)

- **Interior selection, key established earlier.** The user selects measures 20–40. Architectural Layer 3 finds the
  opening has no settled key → requests an earlier extension; Architectural Layer 1 loads back to (say) measure 16;
  Architectural Layer 2 slices 16–20; Architectural Layer 3 re-decodes with the carried-in key now visible → the
  opening of the selection is anchored. Output covers **only 20–40**; 16–20 was evidence.
- **Selection at the score start.** The user selects measures 1–20. Architectural Layer 3 requests an earlier
  extension; Architectural Layer 1 reports the **score boundary at measure 1** → Architectural Layer 3 proceeds with
  what exists (there is no earlier context to want).
- **Selection = whole score (batch testing).** No edge reasoning has anywhere to extend to → **no extension fires** →
  behaviour identical to today.
- **Architectural Layer 4 edge slice (when built).** The last slice of the selection needs a right-hand neighbour to
  decide membership → a one-harmony later extension, or truncation at the score end.

## 7. Architecture decisions (with alternatives)

- **Load the selection and extend on demand — do not load the whole score.** Alternative: keep loading the whole score
  (today's stopgap). Chosen: selection + extend, because the product is selection-based and the whole-score assumption
  is exactly the expensive-to-retrofit error; the batch path survives as the degenerate "selection = score" case.
- **Extension is append-only and idempotent.** Alternative: reload the larger span from scratch each time. Chosen:
  append — repeated extensions stay cheap and the model never loses what it had.
- **The requesting layer owns the stop condition; Architectural Layer 1 owns only the mechanism.** Alternative:
  Architectural Layer 1 decides how much to load. Chosen: the layer knows its own "enough context" test; Architectural
  Layer 1 stays free of analysis knowledge (single responsibility).
- **Output = selection only; context = evidence.** Alternative: also label the extended context. Chosen:
  evidence-only, so extension never changes what the user asked to have analysed.
- **A data-supply call down the stack is not an analysis back-edge** — recorded so the forward-only contract is not
  read as forbidding extension.
- **Design the contract before building Architectural Layer 4+** — rather than build on infinite context and retrofit.
  This is the whole reason the document exists.

## 8. Risks & the non-trivial parts

- **The note-model index under extension is the main implementation difficulty** (the genuinely non-trivial piece).
  The start-time-ordered list and the "latest end-time so far" structure must extend consistently — by append +
  re-index, or by an incremental structure. **Interim:** until that is built, Architectural Layer 1 may *rebuild* over
  the enlarged span on each extension (correctness first, speed later) — but the *contract* (build-selection + extend)
  is what every layer above is written against, so the interim is invisible to them.
- **Re-slice / re-decode cost per extension** — bounded by the stop condition and the hard bound; the hard bound
  prevents runaway reach-back.
- **Determinism independent of extension granularity.** The final analysis must not depend on **how many** extension
  steps reached a given loaded span — extending in one big step or several small ones to the same span must give the
  same result. (A required test.)
- **Composition with incremental re-analysis.** The layers already offer "re-analyse a sub-range" (for score edits).
  Extension (grow the loaded span) and re-analysis (re-run part of it) must compose cleanly — an edit *inside* the
  selection and an extension *outside* it are different operations on the same model.
- **Batch-path preservation.** The degenerate case (selection = score) must stay **byte-identical** to today, or the
  corpus metrics move for the wrong reason. This is the regression guard for the whole change. **(Gate-proof framing,
  merged 2026-07-02:** with selection = score no request ever fires, so the corpus gate 53/24/53 is byte-identical
  **by construction** — the standing proof obligation of the build.)

## §11 Acceptance (the L6 gate — user directive 2026-07-02)

1. This design **ratified** (it was never signed; sign-off is now the first step).
2. **Coded, L1–L5:** L1 build-selection + extend seam (interim rebuild allowed, §8); L2 re-slice-on-extend (done);
   L3 reach-back activated as this design's request (from gated-off) ; L4's request-or-truncate path (uncoded today,
   gap-analysis #5) + item-10 denial provenance; L5's pinned extent + discovery rule.
3. **Regression-tested, per layer + system:** must-fire / must-not-fire fixtures per discovery rule; the §4
   **equivalence invariant** (any extension sequence ≡ one fresh run over the final loaded span); step-size
   independence (§8); denial provenance; hard-bound/no-oscillation termination; determinism; and the degenerate-case
   **byte-identity with the corpus gate 53/24/53**.
4. Then the L6 track resumes (its TSV-oracle instruction un-parks, then the L6 dormant build).

> **★ Dated annotation (user ruling, 2026-08-02, at the D-266 ratification).** THE GATE ITSELF
> STANDS AND TRANSFERS to the current architecture: Layer 6 does not resume until a
> bounded-context implementation is coded and regression-tested in the architecture that
> actually ships. **THE ACCEPTANCE LIST ABOVE (items 1–4) IS DEPRECATED — NOT TO BE USED, NOT
> EVEN RELEVANT:** it names layers, seams and a corpus gate of the superseded legacy stack (the
> 53/24/53 batch stop was itself superseded 2026-07-06). The acceptance conditions are to be
> RESTATED against the current stack as part of the phase-3 plan (with the engage-era
> re-disposition, open-items row OI-259). Register entry D-266 carries this ruling.

**Selection span** — the user's selected range; the output span. **Loaded span** — what Architectural Layer 1 currently
holds (selection ⊆ loaded ⊆ score). **Context / evidence span** — loaded minus selection; used as evidence, never
labelled. **Extension** — a layer's request to grow the loaded span in a direction. **Stop condition** — the requesting
layer's "enough context now" test. **Hard bound** — a maximum reach on an extension. **Score boundary** — the start/end
of the piece; extension clamps here. **Bounded recompute** — re-running the affected layers over the enlarged loaded
span after an extension. **Degenerate (whole-score) case** — selection = score, so no extension ever fires (the
batch-testing path).

## 10. Spec propagation — what this changes in the layer specs (done with this design)

- **Architectural Layer 1:** *build over a selection* + *extend(direction, stop, bound)*; the loaded-vs-selection-span
  distinction; append-only, boundary-clamping, boundary-reporting; the §11 "reads the whole score" note becomes an
  explicit **interim** behind the build-selection + extend contract; the old "widen" operation is this *extend*,
  designed in full.
- **Architectural Layer 2:** re-slice the newly loaded region on extend; context slices are evidence, not output.
- **Architectural Layer 3:** reach-back framed as an extension request (direction = earlier, stop = prevailing key in
  view, hard bound); leading-edge window behaviour (request-or-truncate).
- **Architectural Layer 4:** the window/edge contract — at a selection edge, request extension or recognise the score
  boundary; never assume the neighbour slice exists. (Added to the already-rewritten spec.)
- **Architectural Layers 5–6:** a forward note that they obey the same contract (functional context at the selection
  edge is the likely future extension).
