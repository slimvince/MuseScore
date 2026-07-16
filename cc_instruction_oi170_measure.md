# CC instruction — OI-170: whole-layer tonic-use enumeration + classification + magnitude (build + default-OFF)

**Dispatch author:** Cowork, 2026-07-13. **Type:** a MEASUREMENT build — default-OFF instrumentation + a
default-OFF full-sweep signature-mask variant. **The default production path is unchanged and must
regenerate the committed corpus byte-identically; NO fix is promoted.** The deliverable is the complete map
of L4's tonic-uses (every site, each classified) plus the magnitude of unifying the collection-membership
ones — the full input to *design* the tonic-independence fix and size its re-baseline.

**Why.** OI-168 fixed two terms; OI-170 then found three more collection-membership sites with the identical
δ≠0 corruption on the live region path (`diatonicToKey` in `buildChordResult` + its five re-derivations;
`invRootIsDiatonic` in Gate I and Gate L, which swap the committed winner). This is the third time "the
collection/tonic split holds" has been found incomplete — because the defect is a *pattern* scattered across
the layer, and site-by-site auditing keeps missing sites. So before any fix we need (1) a **complete,
proven** enumeration of every tonic-use in L4, (2) each **classified** collection-membership-δ-bug vs
genuine-tonic-use, and (3) the **magnitude** of routing all the δ-bug sites through one signature-mask
primitive. Measure before designing; measure before building (#9/#19/#17 funnel).

Read first: `CLAUDE.md` (build/test commands, VS Code bash rules, the OI-110 default-OFF byte-identity
precedent), `OPEN_ITEMS.md` (OI-170, OI-167, OI-168, OI-169), the reports
`cc_oi167_collection_tonic_report.md` / `cc_oi168_magnitude_report.md` / `cc_oi168_fix_report.md`, and the
code.

---

## 1. Governing constraints

- **Byte-identity of the default path is the success condition.** All counters and the sweep variant are
  default-OFF; with them OFF the corpus regenerates sha256-identical on 352×3 and the establishment battery +
  both C++ suites are unchanged (the OI-110 pattern). If the OFF build is not byte-identical, STOP.
- **No fix is promoted.** The signature-mask sweep is exercised ONLY through the opt-in variant.
- **Adversarial completeness (#15/#19):** the point is to find EVERY tonic-use, not to re-confirm the known
  five. A site you cannot classify is reported as unresolved, not assumed.
- Premise Gate (#17): write the §6 predictions BEFORE measuring. Fork-only push. VS Code bash rules.
  Self-check the diff.

## 2. Task 0 — register commit

Commit any waiting Cowork register/handoff edits (verify `git status --porcelain`; STOP if unexpected).
Leave `cowork_joint_key_chord_design.md` unstaged.

## 3. Task 1 — enumerate every tonic-use in the L4 path (prove completeness)

Systematically enumerate every use of `keyTonicPc` / `keyMode` / `scale` / `keyModeTonicOffset` (and any
equivalent tonic-derived quantity) across the whole L4 region/gate/refinement path — `analyzeChord` +
`buildChordResult` (`chordanalyzer.cpp`), the post-scoring gates (`postscoringgates.cpp`), the sparse
refinement (`sparsechordrefinement.cpp`), and the `diatonicToKey` producer + its re-derivation consumers
(`sectioncadencedetection`, `functionrelationallabel`, `functionromannumeral`, `sectionanalyzer`, and any
other found by grep). Do this by a **mechanical sweep** (grep the constructions, then read each hit), and
state the completeness basis — "these N sites are every occurrence of the pattern in these files," not "the
ones previously found."

## 4. Task 2 — classify each site

For each tonic-use, classify and cite (FACT with code line):
- **(a) collection-membership-through-the-tonic** — it answers "is this pc in the key's collection?" via
  `(keyTonicPc + scale/interval) % 12` membership (or equivalent), where the correct question is signature
  membership. These are the δ-bug; the signature-mask primitive replaces them exactly (byte-identical for
  δ=0 modes, corrected for Altered/AlteredDomBB7).
- **(b) genuine tonic-use** — the identity, degree, label, or refinement truly depends on the tonic itself,
  not just the collection (e.g. the Aeolian lone-tonic guard's disambiguation, or a degree/role that is
  inherently tonic-relative). These are NOT fixable by the primitive; each is a real dependence to flag as a
  **design question** (does it belong in L4, or move to where the tonic is legitimately produced).
- If a site is ambiguous, say so and give the evidence both ways — do not force a class.

The (a)/(b) split is the answer to "can L4 be made fully tonic-independent": all-(a) ⇒ yes, via the
primitive; any (b) ⇒ a named design constraint remains.

## 5. Task 3 — the A/B magnitude of unifying the (a) sites

Add a **default-OFF variant** that (i) routes every class-(a) site through the single signature-mask
primitive `rootInSignatureCollection(fifths, pc) ≡ pcInMask(diatonicMaskFromFifths(fifths), pc)`, and (ii)
single-sources `diatonicToKey` — the producer computes it via the primitive and the five consumers read the
published fact instead of re-deriving it. Run the corpus **current vs variant** on all three presets and:

- report the committed-chord flip count per preset, and **per site** where feasible (which gate/term/flag
  causes which flip) — Gate I and Gate L swap winners, so attribute their flips specifically;
- for every flip, note whether the variant's reading matches the sounding notes / DCML (the toward-correct
  check — a flip toward the notes is a correctness gain, as `bwv145.5` was for OI-168);
- confirm the `diatonicToKey` single-sourcing is byte-identical (the five re-derivations already equal the
  published value) or report any discrepancy (a #6 divergence — itself a finding).

**Prove the OFF path inert:** with the variant and counters OFF, regenerate the corpus (sha256 vs
`tools/corpus`), the establishment battery byte-identical, `composing_tests`/`notation_tests`/
`pipeline_snapshot_tests` green, no golden refreshed, `tools/robust_stop`/`tools/corpus` untouched.

## 6. Premise Gate — predictions before measuring (#17b)

Record first: the number of tonic-use sites you expect to find (and whether you expect any class-(b)); the
predicted committed-chord flip count (total and per Gate I/Gate L); and whether you expect the
`diatonicToKey` single-sourcing to be byte-identical. A gap between prediction and finding is diagnostic (#3).

## 7. Deliverable

- **A report `cc_oi170_measure_report.md`**: the Task-1 complete enumeration (with the completeness basis),
  the Task-2 per-site classification (a)/(b) with citations, the Task-3 flip magnitude per site with the
  toward-correct check + the `diatonicToKey` single-sourcing result, the predicted-vs-actual, and the
  OFF-path byte-identity proof. Conclude with: **can L4 be made fully tonic-independent** (all-(a)?), the
  recommended fix design (the unifying primitive + single-sourced `diatonicToKey`), and the fix path
  (byte-identical if 0 flips, else a correctness re-baseline with the region/golden list). Flag every
  class-(b) site as a design-pass question.
- **Commit:** the default-OFF instrumentation + sweep variant (byte-identity-proven, OI-110 pattern) as a
  default-OFF `feat` commit, plus the report as a `docs(cc)` fold, plus `STATUS.md`/`cowork_handoff.md`
  notes. Force-add this instruction file. No golden refresh, no fix promoted, `tools/robust_stop`/goldens
  untouched. Push `origin` only.
- **STOP-and-report** if the OFF build isn't byte-identical, if the enumeration cannot be proven complete,
  or if a class-(b) genuine tonic-need is found (that changes whether full tonic-independence is even
  reachable — surface it, do not rationalize it).

**On completion:** we have the complete, classified map of L4's tonic-uses and the measured magnitude of
unifying them — the full understanding to design the tonic-independence fix (one shared signature-mask
primitive + single-sourced `diatonicToKey`, which also removes the internal inconsistency) and to size its
re-baseline, or to name precisely what genuine tonic-dependence blocks it. The fix itself is the next,
separately-ratified step; the key-layer funnel stays shut until the corrected layer assignment is ratified
as a whole.
