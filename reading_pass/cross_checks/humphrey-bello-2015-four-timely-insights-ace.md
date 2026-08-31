# Cross-check — row 21: Humphrey & Bello 2015, "Four Timely Insights on Automatic Chord Estimation"

> **The two extracts compared, 2026-08-31**, under `cowork_reading_pass_commission_2026_08_30.md`
> §4 and the independence protocol of `reading_pass/continuation.md` §2.
> First pass: `reading_pass/extracts/humphrey-bello-2015-four-timely-insights-ace.md` (session 1,
> 2026-08-30, two prompted calls over an open mirror). Second pass:
> `reading_pass/extracts_second_pass/` same file name (session 2, 2026-08-31, three prompted calls
> over the ISMIR archive copy), **written and landed before the first extract was opened.**
> **Neither extract has been edited to match the other.**

## 0. THE DECLARED CONTAMINATION — stated here as the continuation file requires

`reading_pass/continuation.md` §2 requires this cross-check to say so: **this session read
`population.md` §3, and target V12 there states a substantive finding about this paper** — that
Humphrey & Bello do not carry the above-human-agreement claim and their systems score below their
measured annotator agreement. **This session met that finding before reading the paper.**

**So on the V12 point the two passes are NOT independent, and the second pass's agreement is a
confirmation, not a second discovery.** On everything else the second pass is independent in the
ordinary sense — it had not seen the first extract, which as it turns out carries a substantial
finding about this paper that the verification table does not (§2 below), and which the second pass
consequently did not know to look for.

The read-tool bound of §0 of the row-1 cross-check applies here as well, **and this row produced a
third instance of it — see §4.**

## 1. Agreements

Both passes agree on: the four insights and their wording; the Rock Corpus's dual expert
annotations as the agreement evidence; the annotator-agreement row (root 0.932, thirds 0.903,
majmin 0.905, tetrads 0.835); the two systems at tetrads 0.590 and 0.540 against the better-matching
reference; the affinity-vector proposal as **proposed, not built and not measured**; the domain
bound — audio, popular music, nothing symbolic; and that this domain is the same off-domain class
principle #21 and D-474 already refuse as a ceiling for this project's repertoire.

**V12's negative establishment is confirmed** (with §0's caveat on what that confirmation is worth):
the paper's systems fall well short of its human–human agreement, and asked directly whether it
anywhere claims machines match or exceed human agreement, the answer is **no**.

## 2. THE FINDING THE SECOND PASS MISSED ENTIRELY — and it is the most important thing in the paper

The first extract carries this, and the second does not:

> *"on a four-reference case no two human references exceed 65% tetrads agreement while each system
> matches AT LEAST ONE human reading for ~90% of the song — disagreement is between defensible
> readings, and the systems live inside that space."*

**Resolved at the paper, and the first pass is right, with the figures now exact.** The case is
"I Saw Her Standing There" (The Beatles), compared across **six perspectives**: four human
references — *"Isophonics (Iso), Billboard (BB), David Temperley (DT), Trevor deClercq (TdC)"* — and
the two systems. The paper's own sentences:

> *"Based on the tetrads comparison, no two reference annotations correspond to greater than a 65%
> agreement, with the DNN and kHMM scoring 28% and 52% against the ground truth Isophonics
> reference, shown at the top. Despite this low score, the DNN and kHMM estimations agree with at
> least one of the four human annotations **89.1%** and **92.3%** of the song, respectively."*

**Why the second pass's miss matters, and why the first pass's phrasing needs one correction.**

The second pass surfaced the 65% figure and stopped there, so its extract carries only the half that
makes the systems look bad. **The full picture is the opposite in shape: measured against one
designated reference the systems score 28% and 52%; measured against the union of four defensible
human readings they score 89.1% and 92.3%.** That is a nearly threefold difference produced by
nothing but the choice of what to compare against — and it is the paper's own demonstration of its
insight 4. **A reading of this paper that carries the 65% and not the 89.1/92.3 is not a partial
reading; it is a misleading one.**

**The one correction to the first extract:** it attaches a conclusion to the example — *"disagreement
is between defensible readings, and the systems live inside that space"* — and asked directly, **the
paper does not draw that conclusion explicitly.** It reports the numbers and does not characterise
the disagreements as definitively real versus defensible. **The inference is a good one and it is
the reader's, not the authors'.** It should travel labelled as such.

**★ AND NOTE WHAT THIS DOES NOT DO TO V12.** The 89.1/92.3 figures are agreement against
*at least one of four* references — a deliberately generous union — while the 0.835 annotator figure
is *pairwise* on two references. **They are not comparable quantities, and putting them side by side
would produce exactly the "machines beat humans" claim V12 was checked for and which this paper does
not make.** V12's negative establishment stands.

## 3. Items the second pass held and the first missed — carried

| Item | Note |
|---|---|
| **Insight 3 in its own words** — chord *transcription* as *"an abstract task related to functional analysis, taking into consideration high-level concepts such as long term musical structure, repetition, segmentation or key"*, against chord *recognition* as *"quite literal, and … closely related to polyphonic pitch detection"*, with reference sets mixing the two *"to some unknown degree"* | Carried. **This is the item with the strongest claim on this project's attention, because it is about what a reference annotation set IS rather than about audio** |
| **Insight 2's mechanism** — *"C:maj7 and C:maj"* are not mutually exclusive *"since the former contains the latter"*, and one-of-K quantisation *"effectively mak[es] all errors equivalent"* | Carried |
| **Insight 1's two named failure sources** — tuning away from A440 *"by more than a quarter-tone"* producing semitone-displaced estimates, and repertoire that *"do[es] not truly make use of … chords"* (rap, hip hop, reggae, funk, disco), with the conclusion *"chords may not be a valid way to describe all kinds of music"* | Carried |
| The glass-ceiling framing: *"system performance appears to be converging to yet another glass ceiling"* | Carried |
| The systems' input representations (constant-Q spectral patches for the DNN; beat-synchronous multiband chroma for the kHMM), the four corpora with sizes, the **1,217**-track merged training set, the **157**-class vocabulary, and the on-ground-truth tetrads scores kHMM **0.721** / DNN **0.705** | Carried |
| The paper's own caveat of *"a mismatch in chord vocabulary"* in the Rock Corpus evaluation | Carried |
| Confirmation from the archive side that **paper 000294 is this paper** — so R-9's mis-filing is established from both ends | Carried |

## 4. A THIRD read-tool inconsistency, recorded

One read returned, as a verbatim quotation, *"That said, the human annotators do agree a deal more
that is attained by either system, indicating that there is likely room for improvement."* A later
read asked for that sentence with its context and reported it **not found in exact form**.

**One of those two answers is wrong about what the paper contains.** This is the third measured
self-contradiction of this reading tool in this session — after the row-1 segmentation
question and the row-17 independence question — and it is the first involving a **quotation** rather
than a structural reading, which is the more troubling kind.

**What it does NOT do is unsettle V12.** V12's negative establishment rests on **Table 2's numbers**,
returned consistently across every read and across both sessions: annotator–annotator 0.835 at
tetrads against systems at 0.590 and 0.540. **The conclusion does not depend on that sentence.** But
the sentence should not be quoted as verbatim in any downstream document without a read at the
object.

**Taken together, the three instances say something the findings surface must carry: this pass's
reading tool is reliable on tabulated values and unreliable at the margin on structural
readings and on the existence of particular sentences.** That is the honest characterisation of the
grade every extract in this pass declares.

## 5. Verdict

**No value disagrees between the two extracts.** The first pass holds one major finding the second
missed entirely (§2), now confirmed with exact figures and with one attached inference re-labelled
as the reader's rather than the authors'. Seven second-pass items are carried, including insight 3
in the authors' own words. A third read-tool inconsistency is recorded (§4).

**V12 stands as session 1 recorded it, with §0's caveat on this pass's independence at that point.**

**The cross-check for row 21 is COMPLETE, at the relayed grade declared above, and with its
contamination declared.**

*Provenance: session 2 of the reading pass, 2026-08-31. All resolution reads at
`https://archives.ismir.net/ismir2015/paper/000294.pdf`. No specification derived, no document
amended, no code opened, no register row or entry written — the bibliography's R-9 URL correction
belongs to the reconciliation act. Neither extract was edited.*
