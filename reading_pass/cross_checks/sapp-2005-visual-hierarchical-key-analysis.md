# Cross-check — row 17: Sapp 2005, "Visual Hierarchical Key Analysis" (keyscapes)

> **The two extracts compared, 2026-08-31**, under `cowork_reading_pass_commission_2026_08_30.md`
> §4 and the independence protocol of `reading_pass/continuation.md` §2.
> First pass: `reading_pass/extracts/sapp-2005-visual-hierarchical-key-analysis.md` (session 1,
> 2026-08-30, **one** prompted call). Second pass: `reading_pass/extracts_second_pass/` same file
> name (session 2, 2026-08-31, **two** prompted calls), **written and landed before the first
> extract was opened.** **Neither extract has been edited to match the other.**
>
> **The read-tool bound of §0 of the row-1 cross-check applies here unchanged.**

## 1. Agreements

Both passes agree that: the keyscape computes a key estimate across window sizes from about one
beat to the whole piece, sliding and centre-plotted, assembled into one picture; **there is no
committed segmentation anywhere in the method**; **the paper carries no systematic accuracy
measurement**, its validation being qualitative on a handful of worked pieces; key-profile choice
materially changes the reading; the foreground/middleground/background analogy to Schenker and to
Lerdahl & Jackendoff is adopted framing rather than anything established here; and downstream the
method hands **a picture** — no boundaries, no committed key list, no chords, no uncertainty
calculus beyond raw correlation values.

Both also reach, independently, the conclusion that matters for R-7: **this is not a rival
decomposition of the analysis task.** The first pass says so in terms — *"read, and it is NOT a
rival decomposition"* — and the second reaches the same place by a different route, from the
absence of any extraction method. **Neither pass takes the verdict; both flag it for Task 4.**

## 2. Items the first pass held and the second missed — confirmed, with the numbers sharpened

**The worked-example figures. CONFIRMED, and one of them corrected upward in precision.**

The first extract carries the Schubert case as *"A major r 0.86 over F♯ minor r 0.78 across a real
two-key form."* At the paper: analysed whole, the variation is *"A major, with an r-value of 0.86.
F# minor (r=0.78) is the second-best choice"*; **split into halves, the first half reads F♯ minor
at r = 0.80 and the second half A major at r = 0.90.** The first extract has the whole-piece pair
right and does not carry the split pair, which is the half that actually makes the point — both
halves score HIGHER on their own key than the whole-piece winner scored on the whole. **Recorded
here in full.**

The BWV 1007 case: **CONFIRMED.** *"the Krumhansl weightings will identify D major as the key of the
piece when given the notes of the entire movement"*, while the Aarden plot shows *"a small region
of light blue which represents the key of G major"* at the top. **A dominant-for-tonic error on a
whole movement, produced purely by the choice of profile set.** The second pass had the general
profile-sensitivity statement without this instance.

**The complete worked-example list, which neither extract carried:** Pohlenz, *Liebes-A-B-C* (1827);
Schubert, 13 Variations on a Theme by Anselm Hüttenbrenner D. 576, Var. 6; Mozart, Divertimento
No. 4 K. 439b, mvt. 1; Bach, Cello Suite prelude BWV 1007; Pachelbel, Canon in D; Barber, *Adagio
for Strings*; Webern, Variations for Piano Op. 27, mvt. 1. **Seven pieces. That is the paper's
entire evidence base**, and it belongs beside the fact that there is no quantitative evaluation.

## 3. A CORRECTION TO THE SECOND PASS'S OWN LABELLING — a claim marked FACT that is an inference

The second extract states, under a **[FACT]** heading and in emphatic terms, that *"THE LEVELS DO
NOT TALK TO EACH OTHER … There is no model of the hierarchy — no coupling, no consistency
constraint, no propagation between scales."*

**Asked directly whether the paper states independence or any linking between window sizes, the
answer came back: NOT STATED.** The paper describes how an individual analysis is computed and does
not address the question either way.

**So the claim is downgraded here.** What the paper supports is the construction: *"Every point in
the plotting region represents a key analysis done with two parameters: (1) the duration of the
analysis window into the music; and (2) the center-point in time"* — from which independence
follows naturally and about which the paper says nothing further. **The reading is well-founded and
is not a stated fact, and it should not travel as one.** Labelled **[CONJECTURE, well-founded on the
stated construction]** from here on.

*This is the second pass's own error, caught by the second pass's own follow-up question, and it is
recorded rather than quietly fixed in the extract. The extract stands as written; this file is the
correction.*

## 4. A second within-session read-tool disagreement, recorded

On that same question, **two of this session's three prompted reads of this paper disagreed**: one
returned *"Independence: Yes—each point is 'a separate key analysis'"* and the other returned *"Not
stated."* Both cannot be right about what the paper says.

Taken with the row-1 cross-check's §2.7 — where one prompted pass in three got the
segmentation-before-versus-jointly question backwards — **this is now the second measured instance
of the same read tool returning inconsistent answers to a directly-put structural question.** It is
the strongest evidence this pass has produced about the grade of its own reading, and it argues that
**a structural claim resting on a single prompted read should not be treated as established.** Where
such a claim carries load, it wants a targeted re-ask, and preferably a read at the object.

## 5. Items the second pass held and the first missed — carried

| Item | Note |
|---|---|
| The axes and the colour mapping stated exactly: horizontal time, vertical *"the duration of music given to the key-finding algorithm"*, colour from *"the diatonic circle of fifths … mapped onto the colours of the rainbow"* with major/minor by brightness | Carried |
| The window-size trade-off in the author's own words — *"if too much music is analyzed at once, fewer important keys are suppressed; if too little music is analyzed at once, the chordal structure of the music is really being analyzed instead of the key structure"* | Carried. **This is the sentence R-7 actually wants from this row** |
| **Only the maximum is displayed** — correlations for all 24 keys are computed and 23 discarded at display; no second-best key is visualised anywhere | Carried |
| **Fact of absence: no method for extracting a segmentation or a key list from the plot.** Interpretation is left to the eye | Carried. This is why the row cannot be a pipeline component |
| The Schenkerian claim quoted with its own hedge — *"to some extent, serve as an objective form of Schenkerian analysis"* — and unsupported by measurement | Carried |
| The author's statement of the underlying algorithm's limit: Krumhansl–Schmuckler *"cannot by itself identify cases when there are supposed to be two or more keys present in a musical sample"* | Carried |
| The atonal case: on twelve-tone music *"No overall key region becomes dominant in the large-scale structure"* | Carried |
| No statement of computational cost | Carried (absence) |

## 6. One shared reading, sharpened at the paper

The first extract's CONJECTURE — *"that stable colour regions indicate analytic certainty and colour
shifts modulation boundaries"* — is close to the text but merges two different devices. At the
paper: *"The regions of the plot that remain in a single color (and thus in a single key) can be
interpreted as being more stable. Regions of the plot that shift colors during the morphing between
the two profiles are less certain to be given the correct key assignment … and could even indicate
the presence of a modulation boundary between adjacent key regions."*

**The second sentence is about shifting under a MORPH BETWEEN TWO PROFILE SETS, not about spatial
colour change across the picture.** The uncertainty signal is *disagreement between two fitted
profile sets at the same point*, which is a different and more interesting idea than "the colour
changes here." The first extract's phrasing loses that. **Corrected here; the extract stands.**

## 7. Verdict

**No value disagrees between the two extracts**, and the first pass's two worked-example figures are
confirmed and completed at the paper. One second-pass claim is downgraded from FACT to a well-founded
conjecture (§3); one shared reading is sharpened (§6); eight second-pass items are carried.

**A finding about this pass's own read tool is recorded at §4 and is the more consequential
outcome of this cross-check than anything about the paper.**

**The cross-check for row 17 is COMPLETE, at the relayed grade declared above.**

*Provenance: session 2 of the reading pass, 2026-08-31. All resolution reads at the paper's source
URL, `https://ccrma.stanford.edu/~craig/papers/05/p3d-sapp.pdf`. No specification derived, no
document amended, no code opened, no register row or entry written. Neither extract was edited.*
