# Task A, row 17 — Sapp 2005, "Visual Hierarchical Key Analysis" (keyscapes) — AT THE OBJECT

> **STATUS: TARGETED RE-READ, AT THE OBJECT, 2026-08-31.** Executing §2 of
> `cowork_reading_pass_remedial_commission_2026_08_31.md`. **All nineteen pages read as page images
> with the file tools**, from the PDF the user supplied at
> `docs/research_papers/reading_pass_2026_08/p3d-sapp.pdf`, staged through the bridge. **No web-fetch
> read of any kind was used on this row.** A targeted re-read, not a third extraction. **Nothing of
> the findings surface is edited here.**
>
> **This paper prints its own page numbers** (1–19; ACM *Computers in Entertainment* 4(4), October
> 2005, Article 3D); every location below is the printed page.
>
> **★ ONE CORRECTED VERDICT — and it corrects an item the commission itself cites as the model of a
> claim downgraded to conjecture.** It moves no design point and is **not** a STOP.

## The CONFIRMED claims

### C1 — The window-size trade-off, in the author's own words — **CONFIRMED verbatim, with a printing oddity recorded**

Carries **DP-C's SUPPORTS** entry, where the surface calls it *"qualitative evidence about the
problem a decoded segmentation answers, and equally an argument that no single window size is
right."*

**p. 7**, printed exactly as our records quote it: *"Note that if too much music is analyzed at once,
fewer important keys are suppressed; if too little music is analyzed at once, the chordal structure
of the music is really being analyzed instead of the key structure."* The sentence immediately
following is the one that carries the surface's second reading: *"So what is the proper duration of
music to give as input to the Krumhansl-Schmuckler key-finding algorithm?"*

**★ The oddity, recorded and NOT corrected into our records.** As printed, the first clause is at odds
with the paper's own worked case three paragraphs above it, where *"only one key in the music was
identified because the Krumhansl-Schmuckler analysis window was too large and included two key
regions"* — a too-large window there **suppresses** an important key. The printed clause says
*fewer* are suppressed. **Our quotation is exact; the tension is the paper's.** Neither reading
changes what the surface takes from the sentence, and no verdict is taken here. *(This is the row-19
bar applied: transcribe what is printed, put the observation beside it, never in place of it.)*

### C2 — The method examines every window size and commits to no segmentation — **CONFIRMED**

**p. 7**, §3, the paper's own framing: *"This author's approach is to examine **all possible
segmentations** of the music."* **p. 8:** *"Every point in the plotting region represents a key
analysis done with two parameters: (1) the duration of the analysis window into the music; and (2)
the center-point in time of the analysis window."*

**No committed segmentation is produced anywhere in the paper**, established over the whole read.

### C3 — What it hands downstream is a picture — **CONFIRMED**

Carries the §3.1 coupling table's *"A picture. No segmentation, no labels, no rivals, no
confidence"* → *"Compose with nothing"*, and **DP-K's** *"Rows 1, 12, 17, 18 and 19 publish no rivals
at all."*

**p. 8:** *"Since every point in the plotting domain shown in Figure 11 is a separate key analysis, it
would be difficult to display analysis results in textual form. Instead, each key analysis result is
assigned a color."* The key equation at **p. 5** is an explicit maximum over the twenty-four rotations
— so one key per point is displayed and **no second-best key is displayed anywhere in the paper.**
**No method for extracting a segmentation or a key list from the plot is given**, established over
the whole read. Interpretation is left to the eye.

### C4 — No quantitative evaluation; seven worked pieces are the whole evidence base — **CONFIRMED at the whole read**

Pohlenz *Liebes-A-B-C* (Fig. 1), Schubert D. 576 var. 6 (Fig. 10), Mozart Divertimento K. 439b mvt. 1
(Fig. 18), Bach BWV 1007 prelude (Fig. 22), Pachelbel Canon (Fig. 24), Barber *Adagio for Strings*
(Fig. 26), Webern Op. 27 mvt. 1 (Fig. 28). **Seven pieces, no accuracy measurement, no corpus, no
ground truth anywhere in the article.** The bibliography runs to seven entries; the paper was
*"Received June 2005; accepted August 2005"* (p. 19).

### C5 — Profile choice materially changes the reading, with the BWV 1007 instance — **CONFIRMED**

**p. 15**, §5.1: *"the Krumhansl weightings will identify D major as the key of the piece when given
the notes of the entire movement, most likely due to an over-emphasis of the dominant key region"*,
against the Aarden plot in which *"at the top of the plot there is a small region of light blue which
represents the key of G major."* **A dominant-for-tonic error on a whole movement, produced by the
choice of profile set alone.** The cross-check's addition holds at the page.

### C6 — The uncertainty signal is disagreement between two profile sets, not spatial colour change — **CONFIRMED**

The cross-check's §6 sharpening is right at the page. **p. 10:** *"Included with this paper is an
animation graphic that interpolates the key profile weights between those of Krumhansl and Aarden.
The regions of the plot that remain in a single color (and thus in a single key) can be interpreted
as being more stable. Regions of the plot that shift colors **during the morphing between the two
profiles** are less certain to be given the correct key assignment by either set of weights, and
could even indicate the presence of a modulation boundary between adjacent key regions."*

### C7 — The Schenkerian claim carries the author's own hedge — **CONFIRMED**

**p. 9:** *"Musical keyscape plots, to some extent, serve as an objective form of Schenkerian analysis
[see Narmour 1977]."* Unsupported by any measurement, as C4 records.

### C8 — The underlying algorithm's stated limit — **CONFIRMED**

**p. 6:** *"The correlation technique enumerates the possible keys in the musical selection, but it
cannot by itself identify cases when there are supposed to be two or more keys present in a musical
sample."*

### C9 — The atonal case — **CONFIRMED**

Carries **DP-Q's ENRICHES** entry. **p. 19:** *"No overall key region becomes dominant in the
large-scale structure."*

### C10 — The Schubert worked figures — **CONFIRMED and completed**

**p. 6:** whole variation — *"the best key for the music is in A major, with an r-value of 0.86. F#
minor (r=0.78) is the second-best choice, followed by C# minor (r=0.62), and E major (r=0.57)."*
**p. 7:** split in halves — *"The first half will be identified as F# minor (r=0.80); the second half
will be identified as A major (r=0.90)."* **Both pairs confirmed**, and the two further values
(0.62, 0.57) are new to our records.

---

## ★ The CORRECTED claim — the paper DOES state that each window's analysis is separate

**What the cross-check says** (§3): the second extract's emphatic **[FACT]** — *"THE LEVELS DO NOT
TALK TO EACH OTHER … no coupling, no consistency constraint, no propagation between scales"* — was
**downgraded to [CONJECTURE, well-founded on the stated construction]**, on the ground that *"Asked
directly whether the paper states independence or any linking between window sizes, the answer came
back: NOT STATED. The paper describes how an individual analysis is computed and does not address the
question either way."* Its §4 then records that **two of three prompted reads disagreed** on exactly
this — one returning *"Independence: Yes—each point is 'a separate key analysis'"*, the other *"Not
stated"* — and treats that as a measured failure of the read tool.

**What the page says. p. 8, opening its second paragraph:** *"**Since every point in the plotting
domain shown in Figure 11 is a separate key analysis**, it would be difficult to display analysis
results in textual form."*

**So the paper states it, in a subordinate clause used as a premise.** The independence of each
window's computation is not an inference from the construction; it is the reason the author gives for
why the results cannot be tabulated. **The downgrade is CORRECTED: the computation-independence half
of the claim is a stated FACT at p. 8**, and it should carry that grade from here. *(The second
extract's further gloss — *"there is no model of the hierarchy"* — remains the reader's phrasing of
what follows from it, not the paper's words, and keeps its own grade.)*

**★ And the read-tool finding at cross-check §4 needs re-reading in that light, which is the more
useful half of this correction.** The two prompted answers were not two failures. **One of them was
right** — the read that returned *"Yes—each point is 'a separate key analysis'"* quoted the page
almost exactly — **and the cross-check adopted the wrong one**, because "not stated" is the safer
answer and safety was mistaken for accuracy. That does not weaken §0's read-tool bound: the tool did
contradict itself, which is the bound's whole content. **What it adds is that the resolution
procedure has its own failure mode** — when two relayed answers disagree and neither reader can open
the page, the conservative answer wins by default, and here the conservative answer was the false
one. **This is the third instance in this pass of a doubled reading settling an item the wrong way**,
after row 2's boundaries and row 5's caveat that never reached the surface.

**No design point moves.** DP-C's entry does not rest on independence; §0's grade table and
`population.md` §3b record the disagreement rather than a verdict. **This is not a STOP** — it is a
correction to a grade label and to how one cross-check reasoned.

---

## Additions worth carrying

- **The paper labels the window-size axis with its own interpretive hierarchy.** Figure 20 (p. 14)
  annotates the vertical axis, top to bottom, *Key of Piece / Strong Keys / Weak Keys / Tonicizations
  / Cadences / Chords*. **That is the author's own claim that window size and analytical level are
  the same axis** — which is the strongest form of C1's trade-off and is not in either extract.
- **The plot is a display device, not a method.** **p. 11:** *"Any key-finding algorithm can be input
  into the plot, not just those based on key-profile correlations"*, and Figure 17 plots *"the output
  from a root-finding algorithm that is independent of key-profiles."* **This is why the row composes
  with nothing: what it publishes is a rendering of somebody else's decisions.**
- **The vertical scale is a choice with an argument attached.** pp. 13–14: linear plots weight window
  sizes unevenly, so a logarithmic scaling is introduced *"since all levels of the music are weighted
  equally by the logarithmic scaling"*.
- **Two printing oddities, recorded so a later reader does not "correct" them into our records.**
  Figure 10's caption (p. 6) reads *"in A minor, D. 576 (1817)"* while the text of the same page reads
  *"in A major, D. 576 (1817)"*; and the caption prints *"Hütenbrenner"* against the text's
  *"Hüttenbrenner"*.

## What this row does NOT establish

- **No tabulated value was verified** by the commission's exclusion; the r-values seen agree with the
  extracts and are completed at C10.
- **Nothing about DP-D**, recorded because the user's ruling holds that question open across all
  seven rows: **row 17 bears on it not at all** — it assigns no chord tones and decides no chord.
- **Whether R-7 is discharged.** The row is confirmed to be an unevaluated visualisation that decides
  nothing and composes with nothing; **whether that discharges R-7 is Task 4's verdict and stands as
  the findings surface left it.**

## Verdict for the row

**Ten load-bearing structural claims CONFIRMED, several with additions. One CORRECTED — a grade
label, from conjecture back to stated fact — with a finding about the cross-check's resolution
procedure attached. No falsifier candidate. No STOP.**

*Provenance: read 2026-08-31 at `docs/research_papers/reading_pass_2026_08/p3d-sapp.pdf`, all
nineteen pages as page images, staged through the bridge and read with the file tools. The first-pass
extract and the cross-check for this row were read at the file first, to enumerate; the second-pass
extract's claims were taken from the cross-check, which quotes them. No shell was run on the
repository or on any staged copy of it. No specification derived, no document amended, no code
opened, no register row or entry written.*
