# CC Instruction — read-only spec↔implementation delta-check, Architectural Layers 1–4

> **Purpose.** The four layer specs were tightened (L4 rewritten; L1–L3 swept for unqualified predicates). Check, per
> layer, whether the **implementation** matches the **now-tightened spec**. This is **read-only diagnosis, not
> repair** — produce a delta list, fix nothing. The L4 deltas are expected to be the *build backlog* for the next
> increment (the decoder predates the rewrite); the L3 deltas mostly *close* unqualified predicates by reading the
> real coded value.
>
> **CC-hallucination guard (mandatory):** every classification cites a **source location (`file:line`)**. A claim with
> no `file:line` is not accepted — Cowork spot-verifies at the cited location. If you cannot find the implementing
> code for a spec rule, say so explicitly ("no implementing code located") rather than inferring.

## §0 — The diff is two-way; classify every rule
For each rule / algorithm / named quantity a spec states, locate the implementing code and label it:
- **MATCH** — code does what the spec says (cite both spec § and `file:line`).
- **CODE-GAP** — the spec specifies it; the code does **not** do it yet. (Expected for L4 — the decoder predates the
  rewrite. This is backlog, not a bug.)
- **SPEC-GAP** — the code does something the spec does not state, **or** the spec's predicate is still unqualified and
  the code reveals the missing argument (per the predicate-qualification rule). (Expected for L3 — H1–H4.)
- **DIVERGENCE** — spec and code **actively disagree** (code does X, spec says not-X). The dangerous class; surface
  each one prominently.

Do **not** rank or fix. Just classify with evidence.

## §1 — L1 (note model, AS-BUILT): light confirm
Expect MATCH throughout; flag any drift. Check the load-bearing promises against the code:
- tie-resolution = **one** sounding note per tied group (one start, one end);
- **lossless / keep-and-mark** — muted/invisible/non-tonal notes kept and flagged, never dropped;
- **no backward-in-time search limit** in the span query;
- the **eleven** per-note facts (spec §7) are all present;
- the indexed span query returns **exactly** what a linear scan returns (the test exists — cite it).

## §2 — L2 (slicing, AS-BUILT): light confirm
Expect MATCH; flag any drift:
- a boundary at **every** sounding-tonal note **start AND stop**;
- **complete coverage** incl. explicit **empty slices** for silence;
- a slice's identity is the **exact note set**, not a pitch-class-folded mask (a same-pitch doubling that drops is a
  boundary);
- **no thresholds, no smoothing, no note special-casing**.

## §3 — L3 (key/mode, WIRED): confirm the four steps, and close H1–H4 from the code
Confirm the wired decoder implements the spec's four steps (local-fit; change cost; best-sequence; per-slice results
with confidence = sequence-margin and the "uncertain" mark). Then **read the code as the source of truth** and report
the real value behind each predicate the language sweep flagged unqualified (`cowork_layer3_spec_language_sweep.md`),
so the spec can be qualified with knowledge, not assumption:
- **H1 — key-distance metric:** what does the change cost actually measure "how far apart two keys are" by? Line of
  fifths? Semitone distance? Scale-tone difference? Cite the exact computation (`file:line`).
- **H2 — change-cost scale:** are change cost and local-fit on **one common scale** (so the sum is meaningful)? How
  are they combined? Cite it.
- **H3 — brief/sustained:** confirm there is **no slice-count threshold** — that "brief vs sustained" is purely the
  fit-versus-cost arithmetic. Cite the code path (or, if a slice-count constant exists, surface it — that would be a
  SPEC-GAP).
- **H4 — reach-back limit:** the unit and value of the "set limit" (bars? beats? slices? notes?). Cite it.
Flag any genuine DIVERGENCE between the wired decoder and the spec's four steps.

## §4 — L4 (chord, the Increment-B decoder vs the REWRITTEN spec): the main event = the build backlog
The L4 spec was rewritten (`cowork_layer4_chordsymbol_design.md`). For **each** specified rule below, classify
present / partial / absent in the **current Increment-B decoder** (`chordslicedecoder.{h,cpp}` and what it calls), with
`file:line`. Most will be CODE-GAP (the decoder predates the rewrite) — that is the expected outcome and the value: it
yields the prioritized backlog for bringing the decoder up to spec.
1. **Gather → inherit → abstain; never a new symbol from too few notes** (spec §4 step 3, §5 step 4 — the phantom-root
   rule). Does the decoder currently commit a best-scoring chord on a thin slice regardless of note count? (Almost
   certainly yes = CODE-GAP / the defect that started this.)
2. **Insufficiency-uncertainty** (spec §7): is "uncertain" raised on **too-few-notes independent of margin**, or only
   on a small margin? Cite the confidence computation.
3. **Window stop condition** (spec §2): contiguous-consistent extension stopping at the first inconsistent slice — or a
   fixed reach? Cite the window builder.
4. **About-what payload** on "uncertain" (spec §7): does the result carry *which* question is open (root / quality /
   a named note's membership), or only a yes/no?
5. **Composite confidence** (spec §7): margin + sufficiency + membership-cleanliness — or margin-only?
6. **Membership cue-combination rule** (spec §5 step 3): weak **AND** stepwise → non-chord tone; accented passing tone
   (strong-but-stepwise over a clear prevailing chord) → non-chord tone; weak leap → chord tone. Present?
7. **Evidence precedence ladder** (spec §5): spelling-pin (symmetric) > sounding-note fit > key/prevailing tie-break;
   prevailing-chord wins on a metrically weak slice, key on a strong one. Present?
8. **"Implausible chord tones"** (spec §5 step 3): is the membership-feedback penalty defined as "a sounding note the
   rule calls a non-chord tone that the candidate is forced to treat as a chord tone"?
9. **Two-reading scheme** (spec §4): first reading has **no** prevailing-chord term (no decided neighbours yet);
   inheritance + prevailing-chord preference act only on the second reading. Present?
10. **Catalogue = basic types only; added notes from membership** (spec §1, §9): are dim7 and minor-major their **own
    four-note types**, and are 6ths/9ths read off membership (not separate detectors)? Is the symmetric root pinned
    from notated spelling? Cite the template set + the spelling read.
Mark each item **[backlog]** (CODE-GAP, to build) or **[present]** (MATCH/partial), so §6 yields a clean to-do list.

## §5 — Optional behavioural confirmation (read-only)
Where a static read is ambiguous, you **may** confirm behaviourally via the existing read-only decode diagnostic
(`--decode-chords`) — e.g. does the decoder ever emit a new symbol on a 1-note slice? Redirect large output to a file
and read a slice of it (CLAUDE.md bash rules: append `; echo "exit:$?"`, no large inline output). **No production
path, no wiring, no build of a fix.**

## §6 — Deliverable
`cc_spec_impl_delta_L1L4_report.md` (held/gitignored): a per-layer delta table — `rule | spec § | code file:line |
MATCH / CODE-GAP / SPEC-GAP / DIVERGENCE | note`. Plus:
- L1/L2: clean? (list any drift);
- L3: the H1–H4 **actual coded values** (so Cowork can qualify the spec predicates) + any DIVERGENCE;
- L4: the prioritized **build backlog** (the [backlog] items, in a sensible build order) + any [present] items;
- any **DIVERGENCE** across all layers, surfaced together at the top (the only "act now" class);
- close with the unification observation (any parallel path / duplicate logic **observed** — read-only, so observe,
  don't change), ending: *"No fix was attempted; this is diagnosis only."*

## §7 — Constraints
- **Read-only / diagnosis only.** No production change, no wiring, **no fix** — finding a gap is the deliverable, not
  closing it. The report is **local (gitignored)**; no commit required.
- **Every claim cites `file:line`** (the hallucination guard). "Could not locate" is an acceptable, honest finding.
- One reading per concern; reuse the existing decode diagnostic if you confirm behaviour (do not build a new harness).
- `upstream` untouched; no push needed for a read-only check.

## §8 — Stop conditions
- Any production output moves, or a build of a fix begins → STOP (read-only diagnosis).
- You start *repairing* a gap (editing the decoder to satisfy the spec) → STOP (that is the next, gated build
  increment, not this check).
- A push would target `upstream` → STOP.
