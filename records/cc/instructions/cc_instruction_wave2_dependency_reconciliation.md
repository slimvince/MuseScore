# CC instruction — wave-2 dependency reconciliation (READ-ONLY premise verification)

**Dispatch author:** Cowork, 2026-07-13. **Type:** a READ-ONLY analysis — the first stage of the #17
funnel (desk-simulate/probe, no build). **No build, no `src/` edit, no golden refresh, no register
re-scope, no corpus/robust-stop/report write.** The single deliverable is a reconciliation report + a
*proposed* corrected sequence for the user to ratify. This is not coding of any kind.

**Why this exists (the premise under test).** The OI-145 readiness gate sequences the key-layer work as
"wave 1 (measurement chain) → wave 2 (the `src/` substrate) → wave 3 (evidence publication), all before the
key layer is built." Wave 1 is closed. But reading the wave-2 rows shows most of the substrate hygiene is
gated by the register on **E4 (the L4 decoder engagement)** and its retirements — OI-86 closes "*dissolves
at E4 retirements; re-verify at each*," and even its one zero-behavior item is annotated "*removal waits for
the E4 #8 timing*"; OI-87 is gated "*Stage-5/EG-5*." So the readiness gate's premise — that wave 2 can and
should complete *before* the key layer — is **unverified against the rows' own #8 gating**. Under #13
(surface a surprise as a STOP before building around it), #18 (no design may carry load on an unverified
causal claim about our own system), and #17a (label every load-bearing dependency FACT / THEORY /
ASSUMPTION before building), that premise must be checked before any wave-2 build or any move to E4. That
check is this dispatch.

Read first (the convention): `CLAUDE.md` in full, `OPEN_ITEMS.md`, then the grounding set in §3.

---

## 1. Governing constraints

Read-only throughout. Apply the Premise Gate (#17): write the predictions in §5 BEFORE checking; verify
every claim **at the objects** (the code, the roadmap, the design docs — not the register's summary of
them, and not memory); label every dependency **FACT** (citation to code/measurement), **THEORY**
(citation to the design/roadmap), or **ASSUMPTION**. No self-invented labels — use OI-N, the retirement
names (R1…R7, E4, FQ-8), the layer names, and the principle numbers the repository already uses; where a
thing has no name, describe it plainly. Self-check the report against these before delivering. Fork-only if
anything is committed (the report only); nothing else is written.

**The register's own E4/Stage-5 gating is itself a claim to VERIFY, not to accept.** For each row, check at
the code whether the gating is real (e.g. is OI-86's `regiontonecollector.cpp:37` include genuinely
un-removable-until-E4, or removable now with zero behavior change?). A register annotation is a lead, not a
fact, until confirmed at the object (#19-style: trusted only after positive establishment).

---

## 2. The two questions to answer per row (the ledger)

For every wave-2 row (the list in §4), produce a two-column premise-ledger entry:

- **Q1 — Does the key layer actually depend on this item?** i.e. would building the key layer on the
  current substrate, with this item unfixed, put load on a duplicated / mis-layered / unestablished thing
  the key layer reads or shares? Answer FACT/THEORY/ASSUMPTION with a citation to the key-layer design
  (`cowork_key_layer_design_opening.md`), the evidence inventory (`cowork_evidence_inventory.md`), the
  layer spec (`ARCHITECTURE.md`), and the code. "The register listed it under wave 2" is NOT an answer —
  trace the actual dependency or its absence.
- **Q2 — Is this item gated on E4 (or another retirement / Stage-5-EG-5), or is it genuinely doable now
  byte-identical?** Verify the gating at the code and the roadmap (`docs/implementation_roadmap.md` R1…R7
  / E4 / FQ-8), not from the register annotation alone. State the mechanism: *why* it dissolves at E4, or
  *why* it does not.

Then classify each row into exactly one:

- **Class 1 — key-layer-gating AND E4-required.** These make E4 a *verified* key-layer prerequisite.
- **Class 2 — NOT key-layer-gating.** The gate over-scoped it; it can ride E4 (or its own gate) whenever
  that lands, and must not block the key layer. Propose re-scoping it out of the wave-2 blocker set.
- **Class 3 — key-layer-gating AND genuinely E4-independent, byte-identical now.** The only legitimate
  "do it now" residue.

If a row splits (part now-doable, part E4-gated), say so per part — do not force a whole-row verdict.

---

## 3. Ground E4 itself, and its own prerequisites

Before classifying, pin what E4 actually is, from the roadmap and the design docs (not memory):

- **What E4 (the L4 decoder engagement) is and what it retires** — the R4/R5/R6 (and any R-numbered)
  retirements it carries, from `docs/implementation_roadmap.md` and `ARCHITECTURE.md`. This is what the
  "dissolves at E4" annotations point to.
- **Whether E4 has its OWN prerequisites** — anything E4 depends on that isn't yet done (so that "E4 next"
  wouldn't itself trip a gate). Note them.
- **The relationship between E4 (L4) and the key layer (the L3/key-mode work).** State plainly whether the
  key layer sits below, beside, or above E4 in the layer order — because a lower layer depending on a
  higher one (the key layer needing L4 engaged first) would itself be a #7 layering concern worth flagging,
  not assuming.

Record this as the analysis's foundation; the per-row Q2 answers hang off it.

---

## 4. The rows to reconcile

From the OI-145 wave-2 enumeration (verify the current list against the OI-145 row at HEAD — it may have
moved):

- **The substrate set:** OI-86, OI-13, OI-87, OI-79, OI-63, OI-92, OI-93, OI-96, OI-98, OI-99, and the
  file-table-reason pair OI-90/OI-101.
- **The cadence-asset pair** OI-118, OI-119 (+ the OI-122(b)/(e) validations) — OI-145 places these
  "before its votes feed anything"; determine whether they gate the key layer's cadence→key channel and
  what they are gated on (the cadence/modulation engage build, not necessarily E4).
- **The design-resolved set** OI-75, OI-81, OI-94, OI-78, OI-15, OI-91, OI-97 — OI-145 calls these "not
  blockers — the key-layer work itself fixes them." Confirm that reading is still right (a one-line check
  each: are they genuinely subsumed by the key-layer build, or is any a hidden blocker?).

Cover every row; no silent sampling (the totality is the point — the same discipline the audits held).

---

## 5. Premise Gate — predictions to write BEFORE checking (#17b)

Record, before opening the code: your predicted class split (how many of the ~11 substrate rows you expect
Class 1 / 2 / 3, and why), your prediction for whether E4 turns out to be a verified key-layer prerequisite
or not, and your prediction for whether E4 has unmet prerequisites of its own. A large gap between the
prediction and the finding is itself diagnostic (#3) — report it. No prediction, no check.

---

## 6. Deliverable — a proposal, not a decision

- **A report `cc_wave2_dependency_reconciliation_report.md`**: the E4 grounding (§3); the per-row ledger
  (§2) with every dependency labeled FACT/THEORY/ASSUMPTION and cited; the Class 1/2/3 partition; and a
  **recommended corrected sequence** — one of:
  (a) E4 is a verified key-layer prerequisite → E4 becomes the next arc, entered through **its own #17
  funnel** (desk-sim → read-only probe → build), with its prerequisites named; or
  (b) the wave-2 blocker set was over-scoped → the specific rows to re-scope out, so the key layer can
  proceed while those ride E4; or
  (c) a mix — a named Class-3 residue to do now byte-identical, plus the re-scoping and/or E4-sequencing for
  the rest.
- **The re-scoping and the E4-vs-key-layer sequencing are the USER's to ratify** — OI-145's own rule is
  "no key-layer build opens while a wave-2 row is open *unless the user explicitly re-scopes a row out*."
  So propose; do not edit OI-145 or any row's scope, and do not open any build. If the analysis finds a
  register annotation that is factually wrong (a row gated on E4 that is actually doable now, or vice
  versa), record it as a proposed correction with the evidence — do not apply it.
- **Commit:** the report as a `docs(cc)` fold, plus a `STATUS.md`/`cowork_handoff.md` note that the wave-2
  premise is under reconciliation and the sequence awaits the user's ratification. Force-add this
  instruction file. Nothing else is written — no `src/`, no register re-scope, no corpus, no build.

**STOP-and-report** if: a wave-2 item turns out to gate the key layer in a way not captured by OI-145 (a
missing dependency); E4 has an unmet prerequisite that changes the picture; or the analysis cannot resolve
a row's class from the objects (say so, with what evidence is missing, rather than guessing).

**On completion:** the readiness-gate sequencing premise is verified (or corrected) on the record, and the
user has a grounded choice — open E4's #17 funnel as the verified next arc, or proceed with the key layer
with the E4-gated substrate items correctly re-scoped. Either way, the next build starts on a checked
premise, not an assumed one.
