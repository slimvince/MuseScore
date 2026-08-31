# Second-pass extract — row 17: Sapp 2005, "Visual Hierarchical Key Analysis" (keyscapes)

> **STATUS: SECOND INDEPENDENT EXTRACTION (session 2 of the reading pass, 2026-08-31).**
> Written under `cowork_reading_pass_commission_2026_08_30.md` §4, per the independence protocol
> of `reading_pass/continuation.md` §2. **Neither `reading_pass/extracts/` nor
> `docs/research_papers/reading_pass_2026_08/` was opened for this paper before this file was
> written.** Read at its source, `https://ccrma.stanford.edu/~craig/papers/05/p3d-sapp.pdf`, in
> two separately-prompted passes.
>
> **GRADE, DECLARED AT ITS FACE: RELAYED, not at-the-object** — the same web-fetch bound the other
> second-pass extracts carry. Session-and-prompt independence, not read-tool independence.

## Identity

Craig Stuart Sapp, "Visual Hierarchical Key Analysis", *ACM Computers in Entertainment* **4(4)**,
article 3D, pp. 1–19, October 2005.

**Why this row is in the population:** it is one of the three alternatives `FRAMEWORK.md` §11's R-7
names as unread — *tonality estimated at every window size at once*.

## What kind of paper this is — stated first, because it governs everything below

**★ [FACT, established by a direct question] THE PAPER REPORTS NO QUANTITATIVE EVALUATION AT ALL.**
No corpus study, no ground-truth comparison, no precision or recall, no user study. Every example
is a qualitative visual analysis. **So this row can supply no measured value to any design point,
and nothing in R-7's territory is settled by a number from here.**

## Claims, labeled

**[FACT] What a keyscape is.** A two-dimensional plot in which the **horizontal axis is time in the
music**, *"from the start of the piece at the far left side through the end of the piece on the far
right side"*, the **vertical axis is the analysis window size** — *"the duration of music given to
the key-finding algorithm"* — and **colour is the key**: *"the diatonic circle of fifths is mapped
onto the colours of the rainbow"*, with major and minor separated *"by brightness"*.

**★ [FACT] EVERY POINT IS AN INDEPENDENT KEY ANALYSIS.** Verbatim: *"Every point in the plotting
region represents a key analysis done with two parameters: (1) the duration of the analysis window
into the music; and (2) the center-point in time."* A window *"gradually slides through the music
from start to finish; an analysis result is labeled in the plot at the mid-point time location of
the window"*, and the plot assembles *"thousands of key identifications."* The smallest window is
*"some minimum time duration, such as one beat in the music."*

**★ THE STRUCTURAL FACT THAT MATTERS FOR R-7, STATED PLAINLY: THE LEVELS DO NOT TALK TO EACH
OTHER.** Each point is a separate run of a key-finding algorithm over its own window. **There is no
model of the hierarchy — no coupling, no consistency constraint, no propagation between scales.**
The hierarchy in a keyscape is *seen* by the reader in the resulting picture; it is not computed.
This is a different thing from analysing at multiple resolutions jointly, and the difference is the
whole of what this row contributes to R-7.

**[FACT] The underlying algorithm is correlation-based key finding, with profile variants
compared.** Krumhansl–Schmuckler profiles primarily, against Aarden profiles and a root-finding
algorithm independent of key profiles. On the difference, verbatim: *"the Krumhansl weights can be
seen to over-emphasize the dominant key (G major; light blue) at the expense of the sub-dominant
key (F major; yellow). The Aarden weightings come closer to the music-theory expectations."*
**No preference is declared.** Instead, the disagreement between profiles is itself used as a
signal: *"Regions of the plot that shift colors during the morphing between the two profiles are
less certain."*

**★ [FACT] THE WINDOW-SIZE TRADE-OFF, IN THE AUTHOR'S OWN WORDS — this is the sentence R-7 wants.**
*"if too much music is analyzed at once, fewer important keys are suppressed; if too little music is
analyzed at once, the chordal structure of the music is really being analyzed instead of the key
structure."* **A single window size therefore conflates key structure with chord structure at one
end and erases real key regions at the other** — which is the argument for looking at all sizes,
and equally an argument that no one size is the right one.

**[FACT] Only the maximum is displayed.** The underlying algorithm computes correlation values for
all 24 major and minor keys, *"but only the maximum is displayed"*. **No second-best key is
visualised anywhere in the paper**, though it notes that *"ambiguity and clarity measurements
derived from computational key-analysis algorithms can be used [Sapp 2001]"*.

**★ [FACT of absence] THERE IS NO METHOD FOR GETTING A SEGMENTATION OR A KEY LIST OUT OF THE PLOT.**
Asked directly: not stated. No algorithm for finding the boundaries of the coloured regions, no
extraction of a key sequence. **Interpretation is left entirely to the human eye.** So a keyscape is
not, and is not offered as, a component that could sit inside an analysis pipeline and hand
anything downstream.

**[FACT] The paper relates the vertical axis to hierarchical reduction explicitly.** Verbatim:
*"The various vertical positions in the plots are also related to the concept of foreground,
middleground, and background in Schenkerian analysis … Musical keyscape plots, to some extent,
serve as an objective form of Schenkerian analysis."* Lerdahl's GTTM reductions are also referenced,
and elsewhere the plots are said to display structure *"in a hierarchical manner that is similar to
Tree-Notation reductions"*. **The claim to be "an objective form of Schenkerian analysis" is
hedged — "to some extent" — and is supported by no measurement.**

**[FACT] Atonal music is shown, and what it shows there is an absence.** On twelve-tone music:
*"it is easy to see the esthetic of destroying a tonal center … No overall key region becomes
dominant in the large-scale structure of the music. This is, of course, intentional in twelve-tone
music."*

**[FACT] The author's own statement of the underlying algorithm's limit.** Krumhansl–Schmuckler
*"cannot by itself identify cases when there are supposed to be two or more keys present in a
musical sample"*, and *"when more that one key is present in the music, the meaning of the
correlation between a pitch histogram and a prototypical key profile is less reliable."* **[sic] on
the typographical slip; quoted as relayed.**

**[FACT of absence] No statement of computational cost** for the thousands of analyses.

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** a symbolic score reduced to **duration-weighted pitch-class histograms** —
*"count all of the pitch classes (pitch names without octave information) to generate a pitch-class
histogram"*. Octave is discarded. **No spelling requirement is stated** (pitch names are used, but
nothing turns on enharmonic distinction here). A time base fine enough to place windows down to
about one beat. **No chords, no segmentation, no key input.**

**HANDS downstream: a picture.** One committed key per (window size, centre time) point, encoded as
a colour, with the correlation values for the other 23 keys computed and discarded at display. **No
segmentation, no key list, no boundaries, no confidence, no ranked alternatives leave this method
in machine-readable form.** A consumer wanting any of those must build the extraction the paper does
not describe.

**STATED SCOPE:** tonal music *"often conceived of as progressing through a sequence of key
regions"*, demonstrated on pieces from about 1720 to 1936 including twelve-tone works. **The method
is framed as exploratory rather than normative**, and its limitations are stated implicitly through
the underlying algorithm's rather than as a scope clause of its own.

## Bearing, flagged for the findings surface (verdicts are Task 4's, not this file's)

- **R-7's first named alternative is now read at its primary, and what it turns out to be is a
  VISUALISATION, not a competing analysis architecture.** It computes no hierarchy, publishes no
  structure, commits to no segmentation, and grades nothing. **Whether that discharges R-7's
  unread-territory flag for this item, or merely converts it from "unread" to "read and found not
  to be a rival", is Task 4's verdict and is not taken here.**
- **What it does contribute is the window-size trade-off sentence**, which is a clear qualitative
  statement of the problem a decoded segmentation is one answer to — and which is *evidence about
  the problem*, not about any solution.
- **DP-O (hierarchy, open):** this paper asserts a relation to Schenkerian and GTTM reduction and
  measures nothing about it. It supplies DP-O no falsifier and no support that could bear weight.
- **A small point worth keeping:** the profile-morphing device — treating the *disagreement between
  two fitted profile sets* as an uncertainty signal — is a cheap and unusual idea, and it is stated
  without evaluation.

## What this extract does NOT establish

- The exact number of analyses in a plot, or the window-size step.
- Whether the minimum window is literally one beat or that is an example.
- What the "root-finding algorithm" compared against the two profile sets is.
- Whether any later work extracts segmentations from keyscapes (outside this paper's scope).
- **Nothing here is at-the-object.** Every quotation is relayed, and there are no measured figures
  to relay.

*Provenance: second pass of the reading pass, 2026-08-31. Read at the source URL only. No
specification derived, no document amended, no code opened, no register touched.*
