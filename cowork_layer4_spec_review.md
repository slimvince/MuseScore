# Review — the Layer-4 (chord-symbol) design spec

> **Purpose.** An unbiased, comprehensive review of `cowork_layer4_chordsymbol_design.md` *before* Claude Code is
> asked to investigate the Increment-B implementation against it. If the investigation is "implementation versus
> spec," the spec must first be a complete, audience-correct specification — otherwise the investigation has no firm
> baseline. Reviewer: Cowork. Status: findings only; the rewrite follows once these are agreed.

## The standard applied (the three tests)

A design spec is judged here against the user's stated bar:

1. **Complete, without residue.** It fully specifies *what* the layer must do **and the internal method (the
   algorithm) it should use** to do it. It leaves no decision for the implementation to invent in silence.
2. **No *how it is coded*.** Source-level mechanics — file names, function names, data-structure names, commit
   identifiers — do **not** belong in the spec; they are obvious from the source. The spec stops at the algorithm.
3. **Architect-with-music-theory vocabulary.** The reader is a musical architect, not a programmer. Standard music
   theory may be assumed. Invented Cowork/CC terms and programming jargon may **not**.

The headline judgement: the spec is strong on *intent and boundaries* but **fails test 1 at exactly the points where
the implementation went wrong**, and breaks tests 2 and 3 pervasively. The thin-slice phantom-root defect is not a
coincidence — it sits precisely in the spec's largest hole.

---

## A. Completeness — where the spec leaves residue (the most important findings)

A complete spec would let two competent readers derive the *same* behaviour for every slice. This one does not, in
eight places. The first three are the ones the phantom-root defect fell through.

**A1 — "Uncertain" is never defined, and has only one trigger.** The spec leans on "uncertain" throughout (Sections
1, 4, 5, 6, 8, 10) as the layer's honesty mechanism, but the *only* condition it ever gives for raising it is a
**small margin between the best chord and the next-best** (Section 4 step 3; the "confidence" of Section 7). That
captures **ambiguity** — several chords fit and they are close. It is completely silent on the *other* kind of
unsureness: **insufficiency** — too few notes to support *any* confident reading. A lone sounding note can fit one
chord far better than all others, so the margin is *wide* and the slice reads as **confident** — yet it is the least
certain case there is. The spec never says insufficiency is an uncertainty trigger, so the implementation, scoring
only the margin, committed a confident phantom. **This is the residue the phantom-root defect fell through.** A
complete spec must state that uncertainty has *two* sources — readings too close (ambiguity) **and** evidence too thin
(insufficiency) — and that both raise the mark.

**A2 — "Inherit the prevailing chord" is named but not operationalized.** The spec repeatedly says the prevailing
chord should keep an embellishment slice "from spawning a spurious symbol" (Sections 2, 4, 5, 8), but never gives the
**rule**: *when* does a slice take the prevailing chord as its own answer, and when does it earn a fresh symbol? On a
thin slice this is the whole decision — the lone note should be heard as a member of the chord sounding around it
(its third, say), not as the root of a new chord. The spec states the *preference* but not the *decision procedure*,
so the implementation had no instruction to fall back to the prevailing chord and instead named a new one.

**A3 — The window's stopping rule is qualitative only.** The spec says the window "lazy-extends … until the
prevailing harmony is in view, and no further" (Sections 2, 4). That is the right *bound* in principle, but "the
prevailing harmony is in view" is never made operational — there is no stated condition by which the layer *knows* it
has gathered a whole chord's worth of notes and should stop. So "extend until enough" reduces, in practice, to a
guess about how far to look, and the measured under-gathering follows directly. A complete spec must give the
gather-enough condition (for example: extend across contiguous slices that share a single consistent chord reading,
stop at the first slice that does not).

**A4 — Confidence draws on a single source.** Section 7 defines confidence as one number — the margin to the best
different chord. Given A1, it should be a composite: margin (ambiguity) **and** evidence sufficiency (how much of a
chord is actually present) **and** how cleanly membership resolved. The spec commits to the narrowest of the three
without saying why the others are excluded.

**A5 — The evidence sources are listed but their precedence is not closed.** The layer weighs notated spelling, the
key preference, the prevailing chord, the bass, and metric weight. The spec describes each, and pins a few orderings
(spelling pins the root where present and consistent; the key is "a preference, not a determinant"). But it never
states the **full precedence** when they disagree — e.g. bass says one root, spelling says another; or the key
preference points one way and the prevailing chord the other. Two readers would resolve a conflicted slice
differently. A complete spec states the priority order, or the explicit rule that combines them.

**A6 — The membership decision names its cues but not the rule that combines them.** Section 5 step 3 gives two cues —
metric weight, and stepwise approach/departure — but not how they compose into the binary chord-tone/non-chord-tone
call. The hard cases are exactly the ones where the cues disagree: an *accented* passing tone (strong metric weight,
yet stepwise and clearly non-chord), or a *weak leap* (light metric weight, but not stepwise). The spec must say how
the two cues combine, or which dominates, in those cases — otherwise the call is left to the implementation.

**A7 — "Prevailing chord" is used before it exists.** The two-reading scheme (Section 4) names each slice from its own
notes first, *then* refines using neighbours. But the prevailing-chord preference appears in the *first* reading
(Sections 4 step 1, 5 step 2), where no neighbour chords have been decided yet. The spec does not say whether the
prevailing-chord preference applies only on the second reading. This is a genuine ordering ambiguity, not a wording
nit.

**A8 — The glossary omits the two most decision-critical terms.** Section 12 defines chord symbol, chord tone,
non-chord tone, membership, candidate generation, re-ranking, rotation, the key preference, and the prevailing chord —
but **not "uncertain" and not "confidence,"** which are the very concepts the layer's honesty rests on (and the
locus of A1/A4). The terms doing the most work are the ones left undefined.

**The pattern.** A1–A3 are one defect seen three ways: the spec specifies the *easy* path (a slice with a clear chord)
completely, and the *hard* path (a slice without enough notes to be sure) only by naming preferences, never by giving
the decision procedure. The implementation met the hard path and, having no rule, guessed. **A spec "without residue"
must specify the thin-evidence path as concretely as the clear one** — gather first, else inherit the prevailing
chord, else declare uncertain, and *never* commit a root the evidence does not support.

*A note on knowledge-based coding.* Filling these holes does **not** mean inventing thresholds the spec cannot yet
know. The right distinction is **decision-structure vs calibrated value**: the spec must specify the *structure* (that
insufficiency raises uncertainty; that a thin slice falls back to the prevailing chord; the stop condition for the
window) and may legitimately leave the *numeric threshold* to measurement, marked as a tunable. The residue is where
even the structure is missing — which is the case for A1–A3.

---

## B. Level — *how it is coded* that should be removed

The spec repeatedly reaches into the source. By test 2 these belong in a delivery/build document, not the
architecture spec:

- **Code identifiers in the prose:** the existing chord scorer and its post-passes, the sparse-chord-quality helper,
  the per-note query and the aggregate pitch view, the partial-match score formula — all named as code in Sections 1,
  5, 9, 10, 13, 14. The architecture reader does not know these names and should not need to.
- **The "reuse the existing scorer" decision (Section 9, last bullet) and the Section 10/13 implementation
  references** are *delivery* facts (how the build reconciles with current code), not *architecture* (what the layer
  computes). They state how the work will be done, not what the layer is.
- **The Status header carries build state and a commit identifier.** Build progress and version control belong in the
  delivery plan; the architecture spec should read the same whether or not anything has been built yet.

Recommendation: the architecture spec states the *method* (what is computed, from what evidence, by what rule, and
why). The mapping of that method onto existing source — which function to re-point, which commit landed it — moves to
the delivery document.

---

## C. Vocabulary — invented and programming terms for a non-programmer reader

By test 3 these should be replaced with plain music-theory/architecture language (or, for the few worth keeping,
defined once in the glossary):

| In the spec | Problem | Plain replacement |
|---|---|---|
| "lazy-extend" | programming term (lazy evaluation) | "extends only as far as needed" |
| "prior" / "diatonic prior" | statistics term | "a lean toward the diatonic reading"; "preference" |
| "two-pass" | implementation phrasing | "a first reading, then a refinement using the neighbours" |
| "candidate generation" / "re-ranking" | search/algorithm jargon | "listing the possible chords"; "re-scoring that list" |
| "template" / "partial template matching" | code/our jargon (user already flagged) | "chord-type pattern"; "matching even when some notes are missing" |
| "post-hoc" | jargon (user already flagged) | "after the fact" |
| "membership" | coined shorthand | keep, but define once: *the chord-tone / non-chord-tone call per note* |
| "class-(a)/(b)", "BIR", "the two-tier BIR gate" | project measurement codenames | "symmetric-rotation churn" / "functional root error"; move the gate mechanics to the testing/delivery note |
| "tonic-rotated windowed pitch-class features", "logistic re-ranker", "bounded-local joint optimization" (§14, §15) | machine-learning / optimization jargon | describe in words, or move to a research appendix |

"Slice" and "rotation" are coinages but are defined and load-bearing; they can stay, defined in the glossary. The
test for each remaining term: *could a musician-architect who has never seen the source read it cold?*

---

## D. Structure — repetition that hides the rules

Three principles are each restated four or five times: the prohibition on re-deriving a chord from a pooled bag of a
region's notes (Sections 1, 4, 8, 9, 13), the minimality principle (Sections 2, 5, 9, and passim), and the
spelling-pin for symmetric chords (Sections 1, 5, 6, 9, 11). Repetition is not a correctness fault, but here it
**crowds out the decision rules that are actually missing** (Section A): the spec spends its length re-asserting what
the layer must *not* do, while under-specifying what it *must* do on the hard slice. Each principle should be stated
once, authoritatively, and referenced thereafter — which also makes room to add the A1–A3 procedures without the
document growing.

---

## E. The L1–L3 question (grounded, not assumed)

A scan across all the layer specs confirms the same three defects are present below L4, though L4 is the worst
offender. Code identifiers and commit hashes appear in every spec; the Layer-3 increment-C document even contains a
**literal C++ function signature**. So the rewrite is not L4-only — but two things should shape the order:

- **Category confusion to resolve first.** The Layer-3 set mixes *architecture* (`…keymode_design`) with *delivery*
  documents (`…keymode_impl_design`, `…keymode_incrementC_design`, `…analysis_design`). The delivery documents
  legitimately carry code, commits, and build sequencing — that is their job. The fix is not to purge them but to
  **draw the line cleanly**: architecture specs hold *what + method* in plain language; delivery documents hold *how
  it is coded + when it landed*. Several L3 docs currently straddle the line.
- **Order.** Do **L4 first** — it gates Claude Code's next investigation. Then give L1, L2, and the L3 *architecture*
  spec the same pass (lighter: they are mostly clean on completeness; their faults are code-leakage and a few
  jargon terms). The L3 *delivery* documents need only the category line drawn, not a rewrite.

---

## Recommendation

Rewrite the L4 architecture spec to the standard, in this order of importance:

1. **Fill the completeness holes (Section A), especially A1–A3.** Specify the thin-evidence path as concretely as the
   clear path: the two sources of uncertainty (ambiguity *and* insufficiency); the rule for falling back to the
   prevailing chord; the window's gather-enough stop condition; the precedence among evidence sources; the rule that
   combines the membership cues. State each as a *decision structure*, leaving only numeric thresholds to measurement.
   Add "uncertain" and "confidence" to the glossary. **This pre-answers the phantom-root defect** — it makes the
   correct behaviour (gather → inherit → declare uncertain, never guess) a written requirement rather than an
   implementer's choice.
2. **Strip the *how-it's-coded* (Section B)** to the delivery document; the architecture spec reads the same whether
   or not anything is built.
3. **De-jargon to architect/music-theory language (Section C);** define the few kept coinages once.
4. **Consolidate the repeated principles (Section D)** to one statement each.

Only then hand Claude Code the implementation-versus-spec investigation. With A1–A3 written, that investigation
becomes a clean question — *did the implementation gather, inherit, and declare uncertainty as the spec now
requires?* — instead of a comparison against a spec that was itself silent where the code went wrong.
