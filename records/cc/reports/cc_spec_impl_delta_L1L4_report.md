# Spec ↔ Implementation delta-check — Architectural Layers 1–4 (read-only diagnosis)

> **Scope.** Per-layer two-way classification (MATCH / CODE-GAP / SPEC-GAP / DIVERGENCE) of the now-tightened L1–L4
> specs against the implementation, with `file:line` evidence. **Read-only — no fix attempted.** Local/gitignored.
> CC-hallucination guard honoured: every classification cites a source location; "could not locate" is stated where
> it applies. Specs read: `cowork_layer1_note_model_design.md`, `cowork_layer2_slicing_design.md`,
> `cowork_layer3_keymode_design.md`, `cowork_layer4_chordsymbol_design.md`, `cowork_layer3_spec_language_sweep.md`.

---

## 0. DIVERGENCE — the only "act now" class (surfaced together at top)

Two genuine spec↔code disagreements in **built** logic (both in the L4 Increment-B membership path), plus one
build-state note. None is in L1/L2/L3's core decode.

| # | Where | Spec says | Code does | Cite |
|---|-------|-----------|-----------|------|
| D1 | L4 membership cue-combination | NCT ⟺ **weak AND stepwise**; **weak leap** (weak, *not* stepwise) → **chord tone** (a weak member, e.g. arpeggiated). Spec §5 step 3 | NCT ⟺ **weak OR stepwise** → a weak-but-leapt extra note is marked **NCT**, opposite of spec | `chordslicedecoder.cpp:398-402` |
| D2 | L4 "implausible chord tones" penalty | "a sounding note **the rule classifies as NCT** that a candidate is **forced to treat as a chord tone**" — i.e. penalise template tones the membership rule would reject. Spec §5 / §4 step 2 | Penalises **structural extra notes** (strong, non-stepwise, *outside* the basic template) the candidate must treat as a chord-tone extension; template tones bypass the rule and are never penalised (`anyChordTone[pc]=true; continue;`). The charged set is effectively the **inverse** of the spec's | `chordslicedecoder.cpp:390-406` |

Build-state note (not a logic divergence, but flag-worthy): the **catalogue still uses the replaced extension-flag
model** — dim7 is `Diminished` quality + a `DiminishedSeventh` extension *flag*, not its own four-note type
(`chordanalyzer.cpp:232,246`; `ChordQuality` enum has no dim7/minor-major member, `chordanalyzer.h:76-86`;
`Extension` bitmask `chordanalyzer.h:202-205`). Spec §9 explicitly names this the *replaced* design ("mishandled
[dim7] as a diminished triad plus a flag, with no place to pin its spelled root"). Classified CODE-GAP (rebuild not
yet done) rather than DIVERGENCE, but it is the specific replaced-design item — see L4 backlog item 10.

---

## 1. L1 — NOTE MODEL (AS-BUILT): light confirm → **CLEAN**

| Rule | Spec § | Code `file:line` | Class | Note |
|------|--------|------------------|-------|------|
| Tie-resolution = one sounding note per tied group | §1, §4 | `note_model.cpp:127` (skip `tieBack()` continuations) + `:59-60` (`playTicksFraction()` → one onset/release) | MATCH | one start, one end |
| Lossless / keep-and-mark — never drop muted/invisible/non-tonal | §1, §7 | flags set unconditionally `note_model.cpp:62-64`; notes appended with no flag-gated drop `:120,:132`; only rests/tie-continuations skipped | MATCH | test `note_model_tests.cpp:280-283` |
| Eleven per-note facts | §7 | `NoteEvent` struct `note_model.h:80-92` (pitch, tpc, staff, voice, onset, release, duration, isGrace, plays, visible, staffEligible) | MATCH | all 11 present |
| No backward-in-time search limit in span query | §2 | `overlapping()` `note_model.cpp:217-223` (bounds: onset<t1, release>t0; no horizon cap); index = onset-sorted array + max-release segment tree, prune on release only `:196` | MATCH | |
| Indexed span query ≡ linear scan (test exists) | §10 | `note_model_tests.cpp:517` `IDX1_IndexedEqualsLinear_AllFixtures` (+ IDX2-4), equality asserts `:496,:498` | MATCH | cited |

**L1 drift:** none load-bearing. (Side-note, out of this check's 5 promises: L1 spec §3 lists a "widen the covered
span" operation; no `widen`/reach-back method located in `note_model.h` — relevant only to L3-H4 below, where the
reach-back consumer is likewise unbuilt.)

---

## 2. L2 — CHANGE-POINT SLICING (AS-BUILT): light confirm → **CLEAN**

| Rule | Spec § | Code `file:line` | Class | Note |
|------|--------|------------------|-------|------|
| Boundary at every sounding-tonal note **start AND stop** | §4, §9 | `slicer.cpp:47-48` (pushes both `e.onset` and `e.release`) | MATCH | test `slicer_tests.cpp:196-210` (release-only boundary) |
| Complete coverage incl. explicit empty slices for silence | §2, §5 | `slicer.cpp:63-69` (every consecutive boundary pair → a slice, silence included) | MATCH | test `slicer_tests.cpp:279-295` |
| Identity = exact note set, not pc-folded mask | §7 | boundaries from per-note onset/release `slicer.cpp:47-48`; identity comment `slicer.h:49-54` | MATCH | test `slicer_tests.cpp:218-235` (unison-shrink boundary) |
| No thresholds / smoothing / note special-casing | §2 | whole fn `slicer.cpp:29-71` (dedup via sort+unique only; no threshold/merge); `slicer.h:39-44` | MATCH | test `slicer_tests.cpp:246-273` (grace not special-cased) |
| Consumes L1 eligibility (`plays && visible && staffEligible`), doesn't re-decide | §2 | `slicer.cpp:40-41` | MATCH | tests `slicer_tests.cpp:353-409` |
| Whole-corpus validation hook | §10 | `--validate-slices` `batch_analyze.cpp:2524-2525,2768-2781`; `runSliceValidation` `:1887`; driver `tools/validate_slices_corpus.py` | MATCH | independent oracle |

**L2 drift:** none.

---

## 3. L3 — KEY/MODE (WIRED): four steps confirmed; H1–H4 actual coded values

**The four steps (spec §5) — all present, MATCH:**

| Step | Code `file:line` | Class |
|------|------------------|-------|
| 1. Local-fit emission (existing scorer over slice±window, via indexed `pitchContextOverSpan`) | `keymodesequence.cpp:184-189` (`buildSliceContext` → `analyzeKeyMode`), window `:81-95` | MATCH |
| 2. Change cost (stay=0; base + per-fifth×distance + relative-pair extra) | `changeCost` `keymodesequence.cpp:303-312` | MATCH |
| 3. Best whole sequence (forward Viterbi + back-pointers, linear in slices) | `decodeLattice` `keymodesequence.cpp:337-393` | MATCH |
| 4. Per-slice results: chosen + ranked alts + confidence(=sequence margin) + "uncertain" | `keymodesequence.cpp:422-468`; margin `:449-453`; `uncertain` `:454` | MATCH |

**H1 — key-distance metric (what the change cost measures "how far apart" by):**
**Circle-of-fifths / key-signature distance** — NOT semitone distance, NOT scale-tone-count. `cofDistance`
(`keymodesequence.cpp:65-73`) places each tonic pc on the 12-step circle via `(pc*7)%12` and takes the cyclic gap
`min(d, 12-d)`, computed over the **parent Ionian tonic pc** (`State.ionianPc`); consumed in `changeCost`
(`:309`). So C→F♯ and C→G♭ both = 6; B→F♯ = 1. (Closes sweep-H1: the metric is line-of-fifths.)

**H2 — change-cost scale (one common scale with local-fit?):**
**Yes — emission-score units, one common scale.** The Viterbi adds emission and subtracts change cost in the same
accumulator: `v = alpha[t-1][sp] − changeCost(...)` then `alpha[t][s] = best + emissions[t][s]`
(`keymodesequence.cpp:356,363`). Header states the magnitudes (2.0 / 0.60 / 2.0) are "already in emission-score
units" (`keymodesequence.h:45-47,105-113`). (Closes sweep-H2.)

**H3 — brief vs sustained (any slice-count threshold?):**
**No slice-count threshold** — purely the fit-versus-cost arithmetic of the Viterbi forward pass
(`keymodesequence.cpp:345-367`). No "how many slices" constant exists; an excursion survives iff its accumulated
better emission repays the two change costs. (`windowBeats`, `keymodesequence.h:119`, is the *emission look-around
window*, not a brief/sustained gate.) (Closes sweep-H3: confirm "brief/sustained is not a count.")

**H4 — reach-back "set limit" (unit and value):**
**NO IMPLEMENTING CODE LOCATED.** The decoder operates only on the slices handed to it (`decode`
`keymodesequence.cpp:472-486`); there is no widen/reach-back call, and no `widen`/`reachBack` symbol anywhere under
`src/composing/analysis` (grep, 0 hits) nor in `note_model.h`. The spec §5 "reach back until the prevailing earlier
key is in view or a set limit is reached" is **unbuilt**, so its unit/value does not yet exist in code. Classify
**CODE-GAP**; the sweep-H4 question (bars? beats? slices? notes?) cannot be answered from code — recommend Cowork
treat it as a not-yet-built item, not merely an unqualified predicate.

**L3 DIVERGENCE vs the four steps:** none. Two SPEC-GAPs (code does more than the spec states), both benign:
- **SG-L3a** — `populateEmissionConfidence` (`keymodesequence.cpp:272-299`) writes a *second*, emission-scale sigmoid
  confidence onto `chosen.normalizedConfidence` for the downstream 0.8 key-gates (C1). Spec §5/§7 names only the
  sequence-margin confidence; the margin is still carried on `SliceKeyMode.confidence` (`:451-453`), so this is an
  added output field, not a contradiction.
- **SG-L3b** — the decode-only `tpcKeyFitWeight` line-of-fifths spelling term (`keymodesequence.cpp:119-140,203-230`),
  **default 0.0** → byte-identical to the committed pitch-class path when off (`keymodesequence.h:127-146`). Spec §15
  marks tpc-spelling as *deferred* (and routes it to Layer 5). Present as off-by-default measurement scaffolding,
  consistent with "deferred"; flag so spec and as-built don't silently disagree.

---

## 4. L4 — CHORD SYMBOL (Increment-B decoder vs the REWRITTEN spec): build backlog

The decoder source (`chordslicedecoder.cpp`) is **ahead of its own header banner** — the header still says
"INCREMENT A only / membership STUBBED EMPTY" (`chordslicedecoder.h:26-49`) but the `.cpp` implements Increment-B
(adaptive window, two-pass, `classifyMembership`); git HEAD `5f6b9828a5` confirms Increment B landed. So membership
is partially built; the §5-step-4 **commit/inherit/abstain** machinery is not. Per-item classification, in build
order:

### Prioritized [backlog] (CODE-GAP — to build)

1. **[backlog] Gather → inherit → abstain; never a new symbol from too few notes (the phantom-root rule).**
   *Spec §4 step 3, §5 step 4.* **ABSENT.** `decideSlice` commits `ranked.front()` and sets `hasChord=true` whenever
   the candidate list is non-empty, with **no** sufficiency test (≥3 distinct chord tones), **no** inherit-prevailing
   fallback, **no** abstain (`chordslicedecoder.cpp:296-319`). Thin slices are *scored* (`minDistinctPcs=1` relaxes
   the gate, `:519` + `chordslicedecoder.h:124`), so a 1-note slice yields and commits a chord. The prevailing chord
   is carried only as a ranked *alternative* (`:343-363`), never inherited. **This is the defect that started the
   rebuild.** (Static read is conclusive — there is no inherit/abstain code to invoke; behavioural confirmation via
   `--decode-chords` is available but unnecessary.)
2. **[backlog] Insufficiency-uncertainty (uncertain on too-few-notes independent of margin).**
   *Spec §7.* **ABSENT.** `uncertain` is **margin-only**: `confidence = chosen.score − bestOtherSymbol` then
   `uncertain = confidence < uncertaintyMargin` (`chordslicedecoder.cpp:311-319`). A thin slice with a wide margin is
   *not* marked uncertain — exactly the case spec §7 says must be ("a wide margin does not rescue an insufficient
   slice").
3. **[backlog] Composite confidence (margin + sufficiency + membership-cleanliness).**
   *Spec §7.* **margin-only.** `SliceChord.confidence` is the single margin scalar (`chordslicedecoder.cpp:311-318`);
   no sufficiency or membership-cleanliness term feeds it. (Same site as item 2.)
4. **[backlog] "Uncertain" carries an about-what payload (root / quality / a named note's membership).**
   *Spec §7.* **ABSENT.** `SliceChord` has a bare `bool uncertain` and no open-question field
   (`chordslicedecoder.h:208-226`, `:214`). Downstream (Layer 5) cannot be told *which* question is open.
5. **[backlog] Window stop condition = contiguous-consistent extension, stop at first inconsistent slice.**
   *Spec §2.* **partial / proxy.** `adaptiveWindow` extends until distinct-pc-count ≥ `minHarmonyPcs` **or** ±
   `maxContextSlices` (`chordslicedecoder.cpp:131-156`, stop `:150-155`). This is a **pc-count** stop, not the spec's
   "stop at the first slice whose notes are *inconsistent with the chord reading*." A crude bound (header admits it,
   `chordslicedecoder.h:104-141`), not the consistency-driven window.
6. **[backlog] Evidence precedence ladder (spelling-pin > sounding-note fit > key/prevailing tie-break; prevailing on
   weak slice, key on strong).** *Spec §5.* **ABSENT.** Selection is vertical-score argmax plus a membership penalty
   (`finalizeSlice` `chordslicedecoder.cpp:461-483`); the key enters only as the diatonic prior inside
   `analyzeChord` (`candidatesForWindow` `:266`), the prevailing chord only as membership context + a carried
   alternative. No metric-weight-gated prevailing-vs-key arbitration, no spelling pin at the top of a ladder.
7. **[backlog] Catalogue = basic types only; dim7 & minor-major their own four-note types; added notes off
   membership; symmetric root pinned from notated spelling.** *Spec §1, §9.* **ABSENT (replaced model still in use).**
   `analyzeChord`'s catalogue keeps triad qualities and represents the seventh as an **extension flag**: dim7 =
   `Diminished` + `DiminishedSeventh` flag (`chordanalyzer.cpp:232,246`; `Extension` bitmask `chordanalyzer.h:202-205`);
   no `ChordQuality` member for dim7 or minor-major (`chordanalyzer.h:76-86`); minor-major bare template was rejected
   (project memory `backlog_b1_mmaj7_template`). The decoder only **labels** `rootTpc` from `tpcForPc`
   (`chordslicedecoder.cpp:274-275`) — it does **not pin** the symmetric root from spelling; the header marks the
   spelling-pin + new types "Increment C, deferred" (`chordslicedecoder.h:44-49`). This is the spec §9 *replaced*
   design still live (see Divergence build-state note).

### [present] (MATCH / partial — already built)

8. **[present] Membership cue-combination rule exists** — `classifyMembership` combines metric salience and stepwise
   treatment (`chordslicedecoder.cpp:368-420`, salience `:173-178`, stepwise `:192-243`). **But the combination
   logic DIVERGES** (`weak OR stepwise`, see D1) and the accented-passing case is matched without the spec's
   "prevailing chord clear and excludes it" guard. Built but not to spec.
9. **[present] Two-reading scheme** — first reading uses own notes + key prior, **no** prevailing-chord term
   (`buildSliceWork` calls `decideSlice(..., std::nullopt, ...)` `chordslicedecoder.cpp:453`); second reading uses
   provisional neighbours on both sides + carried prevailing (`finalizeSlice` `:461-483`, neighbour wiring
   `decodeWindowed:558-567`). Structure MATCHES spec §4 — *except* the prevailing chord's spec role on reading 2
   (the inheritance fallback) is the missing item 1.
10. **[present] "Implausible chord tones" penalty exists** — `implausibilityPenalty` summed and fed back as
    `score −= membershipPenaltyWeight × penalty` (`chordslicedecoder.cpp:403-406,468-473`). Built, but its **definition
    differs from spec** (see D2): it charges structural *extras*, not template tones the rule would call NCT.

**Build order recommendation (from the backlog above):** 1 (sufficiency + inherit/abstain — the phantom-root fix)
→ 2/3 (composite/insufficiency confidence, same struct) → 4 (about-what payload) → fix D1 (cue-combination) and D2
(penalty definition) in the existing membership pass → 5 (consistency window) → 7 (catalogue: dim7/minor-major types
+ spelling pin, the Increment-C block) → 6 (precedence ladder, last — it leans on 1 and 7).

---

## 5. Unification observation (read-only — observed, not changed)

- **Parallel decoder shape, L3 ↔ L4.** `SliceKeyMode` (`keymodesequence.h:161-167`) and `SliceChord`
  (`chordslicedecoder.h:208-226`) carry the same `chosen / alternatives / confidence / uncertain` shape with the same
  "margin to best *different* symbol" semantics and a near-identical no-competitor sentinel (`kSingleStateConfidence`
  `keymodesequence.cpp:53` ↔ `kNoCompetitorConfidence` `chordslicedecoder.cpp:41`). Two hand-written copies of one
  per-slice decision record + confidence rule.
- **Duplicated vertical-score formula.** `verticalScore` (`chordslicedecoder.cpp:49-53`) is documented as "Identical
  to `DiagnosticOracleCell::verticalScore` (chordanalyzer.h)" — a second copy of the one fit formula.
- **Repeated eligibility predicate.** `plays && visible && staffEligible (&& !grace)` is re-spelled at ≥4 sites:
  `slicer.cpp:40-41`, `chordslicedecoder.cpp:96-98` (`eligibleNotesInSpan`), `weightedPcView`/`pitchContextOverSpan`
  (engravingbridge), and the `batch_analyze.cpp:1904-1913` validation oracle. One L1 eligibility predicate, copied.
- **Two window builders over the same indexed query.** L3 uses `pitchContextOverSpan`; L4 uses `weightedPcView` +
  `eligibleNotesInSpan` — both ultimately over `NoteModel::overlapping`. The shared indexed-query floor is honoured;
  the per-layer thin window wrappers are parallel but not unified.

These are observations for a future unification pass, surfaced per the read-only mandate.

---

No fix was attempted; this is diagnosis only.
