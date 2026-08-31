# Cross-check — row 18: Viaccoz, Harasim, Moss & Rohrmeier 2023, Wavescapes

> **The two extracts compared, 2026-08-31**, under `cowork_reading_pass_commission_2026_08_30.md`
> §4 and the independence protocol of `reading_pass/continuation.md` §2.
> First pass: `reading_pass/extracts/viaccoz-harasim-moss-rohrmeier-2023-wavescapes.md` (session 1,
> 2026-08-30, **one** prompted call). Second pass: `reading_pass/extracts_second_pass/` same file
> name (session 2, 2026-08-31, **two** prompted calls), **written and landed before the first
> extract was opened.** **Neither extract has been edited to match the other.**
>
> **The read-tool bound of §0 of the row-1 cross-check applies here unchanged.**

## 1. Agreements

Both passes agree on: the transform taken of **duration-weighted 12-dimensional pitch-class
vectors**; six working coefficients each tracking a collection family; **all temporal scales at
once**; **no key labels and no key-finding algorithm anywhere**; **enharmonic equivalence by
construction, spelling discarded at the input**; **no accuracy evaluation of any kind**, the
evidence being eight case studies from Josquin to Ligeti/Coltrane; the Liszt magnitudes 0.652 and
0.172; and a downstream hand-off that is a picture — no decisions, no boundaries, no chords, no
keys.

Both also reach, independently, the same conclusion for R-7: **read at the primary, and it is not a
rival decomposition of the analysis task.** Neither takes the verdict; both flag it for Task 4.

## 2. THE ONE SUBSTANTIVE ERROR FOUND — and it is exactly what a cross-check is for

The first extract glosses the Liszt figures as *"hexatonic 0.652 vs augmented-triad 0.172"*.

**Resolved at the paper: 0.652 is coefficient k = 3 and 0.172 is coefficient k = 6, and the paper
associates k = 3 with HEXATONIC scales and k = 6 with WHOLE-TONE scales.** The first extract's own
claims list, three lines above, states the correspondence correctly — *"hexatonic at 3, whole-tone
at 6"* — so the file contradicts itself: **the second figure is attributed to the augmented triad,
which is the other family sharing coefficient 3, not the family of coefficient 6.**

**Why this is worth the space.** Both values are right and their contrast is the paper's point — a
hexatonic reading strongly outweighing a whole-tone one in the *Faust Symphony*. Mis-labelled, the
pair reads as **hexatonic against augmented triad, which is a comparison WITHIN one coefficient and
therefore one the wavescape does not make at all.** A later reader taking the pair from the extract
would have carried away a false statement about what the method distinguishes. **The first extract's
figures are correct; its labelling of the second is not.** Corrected here; the extract stands
unedited, per the protocol.

## 3. Items the first pass held and the second missed — confirmed

| Item | Status |
|---|---|
| The sharper positioning quote — *"Thus, keyscapes based on key-finding algorithms are not suitable for representing extended tonality."* | **CONFIRMED verbatim.** The second pass had only the milder *"the notion of a diatonic key is not equally applicable to pieces from all time periods or styles."* **Both are in the paper; the first pass has the stronger one**, and it is a direct claim against row 17's method by name |
| The determinism/bias claim | **CONFIRMED verbatim:** *"Since wavescapes produce visual analyses deterministically, a number of potential subjective biases are removed."* The first extract's CONJECTURE label and its own rejoinder — the analyst still chooses the resolution and the coefficient and still does the interpreting — are both sound, and the paper's own admission that *"the role of the analyst is thus focused on the interpretation and contextualization of the results"* stands beside it |
| The THEORY label: the coefficient/collection correspondences are established Fourier phase-space music theory applied here, not established here | **CARRIED.** The second extract did not label them; the first pass's labelling is the better-grounded one |

## 4. Items the second pass held and the first missed — carried

| Item | Note |
|---|---|
| **The k = 5 phase collision, confirmed verbatim:** *"Since G is its center on the circle of fifths, the phases for this diatonic scale and the singleton G are identical."* | **The single most load-bearing fact either pass found about this representation.** The fifth coefficient's phase gives a continuous, key-free position on the circle of fifths — and gives **the same position to a whole diatonic collection and to one note at its centre.** It cannot separate relative major from relative minor either, both being one collection. Anyone proposing this space as a tonality representation meets that first |
| **Magnitude is given NO interpretive gloss** — not clarity, not prototypicality, not salience; it is defined geometrically as *"the distance to zero"* | Carried. **A reader tempted to use normalised magnitude as a confidence is not authorised by the paper to do so** |
| **The effect of the base resolution r is not stated**, and no coefficient is named best for common-practice tonality; resolutions were chosen per piece from the time signature | Carried (absences) |
| The paper neither claims nor **disclaims** replacing key finding — it *"substitute[s] such algorithms by outputs of the DFT"* with no disclaimer | Carried |
| The stated limitation that bears on DP-O: the method does *"not explicitly provide a tree- or graph-structured analysis of the music"*, is *"a first approximation"* and *"a first building block"*, with the authors noting the *"theoretical and practical difficulties for automatic hierarchical music analysis"* | Carried. **DP-O gets no support and no falsifier from this row, by the authors' own words** |
| Complementarity with Lieck & Rohrmeier's pitch scapes: *"Their approach can therefore be considered complementary to ours"* | Carried — a pointer to a further unread item, **not added to the population here** (that would be a candidacy upgrade, and this pass has none) |
| A Python implementation at `https://github.com/DCMLab/wavescapes` | Carried. **Neither pass opened it** |
| The chain observation: this method discards at its input precisely the information V3 measures the value of — Temperley 2002's 83.8% against 87.4% with spelling | Carried as an observation for Task 4, not a verdict |

## 5. A citation discrepancy in our own records — RESOLVED AGAINST US

`reading_pass/additions.md` and the first extract's title line both give the issue as **27(3)**. The
journal page states **Volume 27, Issue 2**, pp. 390–427 — confirmed on **three separate reads**
across both passes.

**Note that `additions.md` already carries one correction to this row's citation** — the reachability
report's venue, *JNMR* → *Musicae Scientiae*, which is confirmed here. **The issue number is a second
error in the same citation.** Both belong to the bibliography reconciliation the commission defers to
its own act. **This pass amends nothing.**

*Recorded alongside the row-5 citation finding: that makes **two of the four fetched central papers
carrying a citation error in our own records** — one in the year, one in the issue. That is a rate
worth the reconciliation act knowing about.*

## 6. Verdict

**One substantive error is found and corrected (§2) — a figure correctly recorded and incorrectly
labelled in the first extract.** One citation error in our records is confirmed (§5). Three
first-pass items are confirmed, including the stronger positioning quote; eight second-pass items
are carried, one of them — the k = 5 phase collision — materially changing how this representation
should be read.

**No value disagrees between the two extracts.**

**The cross-check for row 18 is COMPLETE, at the relayed grade declared above.**

*Provenance: session 2 of the reading pass, 2026-08-31. All resolution reads at the article's
source URL, `https://journals.sagepub.com/doi/full/10.1177/10298649211034906`. No specification
derived, no document amended, no code opened, no register row or entry written. Neither extract was
edited.*
