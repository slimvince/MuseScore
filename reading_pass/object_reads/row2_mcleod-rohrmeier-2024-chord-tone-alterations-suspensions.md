# Task A, row 2 — McLeod & Rohrmeier 2024, chord tone alterations and suspensions — AT THE OBJECT

> **STATUS: TARGETED RE-READ, AT THE OBJECT, 2026-08-31. IT RAISES A STOP.** Executing §2 of
> `cowork_reading_pass_remedial_commission_2026_08_31.md`. **All fourteen printed pages read as page
> images with the file tools**, from the PDF the user supplied at
> `docs/research_papers/reading_pass_2026_08/chord-sus-jnmr.pdf`, staged through the bridge. **No
> web-fetch read of any kind was used on this row.** A targeted re-read of the existing extracts'
> load-bearing structural claims, not a third extraction. **Nothing of the findings surface is
> edited here.**
>
> **This paper prints its own page numbers**, and every location below is the printed page.
>
> **★ TWO CORRECTED VERDICTS, both on claims the findings surface used to reach its rival-defused
> verdict at DP-D.** By the commission's §2 that is a falsifier candidate and a STOP. The STOP is
> written on its own at
> `reading_pass/object_reads/stop_row2_dpd_defusal_2026_08_31.md` and put to the user; **Task A does
> not continue past it.**

## What was enumerated, and from where

Every structural claim of `reading_pass/extracts/…`, `…/extracts_second_pass/…` and
`…/cross_checks/…` for this row that carries load in `cowork_reading_pass_findings_2026_08_31.md` —
in DP-D's verdict, in DP-M's contrast, in the §3.1 coupling table, in the §3.2 chain, or in §5's
routed extracts. Tabulated values are excluded by the commission; they were seen in passing at
Tables 1, 2 and 3 and **none diverged** from the extracts, which is recorded and is not a
verification.

---

## The CONFIRMED claims

### C1 — The method runs after a chord label and holds its root, quality and inversion fixed — **CONFIRMED**

At **p. 2**: the method takes *"as input a chord label (and the notes present in the score for the
duration of that label)"* and outputs *"a set of pitch classes (PCs) that should be incorporated into
the label."* At **p. 4** the current chord's root, quality and inversion are input features to the
model, not outputs. At **p. 12**, §5, the three steps are stated in the same order. **Nothing in the
paper revises the input label's root, quality or inversion.** The findings surface's *"holds them
fixed"* is exact.

### C2 — Its stated ground is a vocabulary problem — **CONFIRMED in substance, with the sentence's own framing recorded**

At **p. 2**: *"Nonetheless, to our knowledge, no chord labeling model has yet been proposed that
includes an analysis of such complex chord forms directly in their output chord labels. One possible
reason for this is clear: adding an additional feature to each chord label results in a
multiplicative increase in vocabulary size (since each alteration might occur with any existing
label), which reduces the possible training data per label and weakens predictive power."*

**Two things to record precisely, because the record's own bar is to transcribe what is printed.**
*(i)* Our files quote the sentence beginning *"Adding an additional feature…"* with a capital A; the
page prints it lowercase, as the second clause of a sentence beginning *"One possible reason for
this is clear:"*. **The substance is untouched; the transcription is not exact.** *(ii)* The sentence
as printed is the authors' hedge about why **the field** has not done this, not a declaration of
their own design ground — but the paper does then reason from it for its own design two paragraphs
later (*"this runs into the multiplicative problem discussed above"*), so **the surface's substance
holds**: the ground is about the label vocabulary, not about where the assignment belongs.

### C3 — The evaluation is a per-window exact pitch-class-vector match, not a per-note accuracy — **CONFIRMED, verbatim**

At **p. 6**, §3.1.4: *"we measure the accuracy of an output by first splitting the input piece into
windows by cutting it at each point where either the (non-reduced) ground truth label or the model's
output label changes. This includes completely new chords as well as chords which differ only by,
e.g., an added tone. Each of these windows is treated as a separate data point, which we deem
correct if the PCs included in the (non-reduced) ground truth label match exactly the PCs included in
the model's output label."*

**The cross-check's resolution of §2.1 is right and its quotation is exact.** The surface's *"per-window
exact pitch-class-vector match on ground-truth labels"* stands.

### C4 — The chord root is the frame of reference for every note feature, not an absent input — **CONFIRMED**

At **p. 4**: each note's pitch class is *"represented as the number of perfect 5ths above the root"*,
and for the current chord the root one-hot *"is not included (since it would always be 0)"*. **The
cross-check's sharpening is right at the page.**

### C5 — The baseline runs the same merging procedure — **CONFIRMED**

At **p. 7**, §3.2: the rule-based baseline's *"output is processed in the same way as our proposed
method's binary PC vectors, using the merging procedure described in Section 2.3."* **The gain is
over hand-written rules with identical segmentation machinery**, as the second pass held.

### C6 — Pedal tones are nowhere in the paper — **CONFIRMED at the whole read**

The 2021 companion names suspensions **and pedal tones** as future work (row 1, C8). This paper
delivers the first and never mentions the second, at any page. **A fact of absence, established over
the whole document rather than by a prompted question.** It bears on §3.2's chain sentence, which
says row 1 *"names suspensions and altered tones as future work and row 2 delivers them"* — true as
written, and worth knowing that the third named item is still unowned by anything in the read set.

### C7 — The corpus includes unreleased data — **CONFIRMED**

At **p. 5**, §3.1.1: *"a mixture of internal (but to-be-released) data and publicly available
corpora"* — ABC, the Annotated Mozart Sonatas, and 36 Corelli trio sonatas; 924 pieces; 80/10/10.
**The reproduction bound the cross-check attaches to the figures is real and is at the page.**

### C8 — The Ju et al. 2017 positioning — **CONFIRMED, verbatim, p. 2**

*"Their model is designed to work specifically on 4-part Chorales … Their model also treats
enharmonically equivalent PCs as identical (i.e., it considers only 12 PCs), while ours uses 35 …
Finally, our method takes a hypothesis chord label as input, while theirs only takes the PCs."*

---

## ★ The CORRECTED claims — both bear on DP-D's rival-defusal

### ★★ K1 — "The merging … does not move the input chord boundaries" — **CORRECTED. The method changes the segmentation, and doing so is its stated goal.**

**The claim as the findings surface carries it**, twice: at §2, DP-D — *"the merging it does operates
on its own internal windows within one given chord label and **does not move the input chord
boundaries**"*; and in the §3.1 coupling table — *"Hands downstream: The same labels augmented with a
pitch-class set; **boundaries unchanged**"*, placing the row at *"**L3** — it consumes L2's output
and revises none of it."* The cross-check reached the same reading at its §2.2, resolving **against**
the second pass, whose claim that *"boundaries do move under this step"* was withdrawn.

**What the pages say. Four places, and they agree with each other:**

1. **p. 5, §2.3, the method section:** *"Any remaining unmerged vectors after this process are
   treated as **separate chord labels**, not shown in the pseudocode, as they necessarily contain
   incompatible PCs, and would therefore be represented by the same (duplicated) chord label, but
   with distinct alterations."* **So one input chord span can leave the method as several output
   chord labels.**
2. **p. 6, §3.1.3, *Chord Merging*:** *"Any consecutive chords which are identical (as a result of a
   vocabulary reduction) are merged on input. Likewise, consecutive chords with identical root,
   quality, and inversion are also merged. This merges, for example, two C major triads which only
   differ by a chord tone alteration. Importantly, each merge only occurs in the model's input. The
   ground truth targets remain unchanged: **the goal is therefore that our method will leave such
   chords unmerged in its output.**"* **Re-splitting an input span is not a side effect; it is the
   task the experiment sets.**
3. **p. 6, §3.1.4:** the evaluation windows are cut wherever *"the model's output label changes"*,
   and that *"includes completely new chords as well as chords which differ only by, e.g., an added
   tone."* **The metric is built to score a segmentation the model produces.**
4. **p. 10:** two reported errors are boundary errors in exactly this sense — *"our method correctly
   identifies the 7th, but incorrectly merges the two chords together"*, and *"with the full
   vocabulary, our method incorrectly merges the two chords together (including the 4 suspension)."*

**What survives of the claim, stated exactly.** No input boundary is deleted or relocated, and root,
quality and inversion are never revised: every label the method emits inside an input span is *the
same chord label with different alterations*. **What is false as written is that the boundaries are
unchanged.** The method **subdivides** them, by design, and its own metric and error analysis are
built around that.

**Why this is a STOP and not a footnote.** In this framework's terms, adding a boundary inside a span
L2 published is a revision of L2's segmentation — which the **L3 → L2 "Nothing"** contract (§5) and
**DP-M** forbid. The coupling table's *"consumes L2's output and revises none of it"* is therefore
the load-bearing half of how row 2 was placed, and it does not hold at the paper. **Which way that
cuts is not this file's to decide** — see the STOP memo — but it is not a small correction: it
changes what the pass's one rival-shaped item actually is.

### ★ K2 — "The paper contains NO COMPARISON of post-hoc against joint … no argument that post-hoc is preferable" — **CORRECTED in part; its third clause stands**

**The claim as the findings surface carries it** (§2, DP-D), and it is the leg the defusal leans on
hardest: *"AND THE PAPER CONTAINS NO COMPARISON OF POST-HOC AGAINST JOINT. Established by a question
put directly at the text: no such discussion, no argument that post-hoc is preferable, **no
measurement of what post-hoc costs**."* Both extracts reached it independently, and the cross-check
calls that convergence *"the strongest convergence in the whole cross-check exercise"*.

**What the pages say, at p. 2, where the paper sets out its options:**

- It enumerates alternatives and gives reasons against them. Putting alterations in the vocabulary
  *"runs into the multiplicative problem discussed above."* Treating them as a separate
  classification problem *"runs into a slightly subtler issue: The meaning of an alteration is often
  context dependent"*, which *"is not impossible for a model to learn, but it can complicate the
  learning process. Furthermore, it suggests that a different way of looking at the problem might
  lead to a simpler, more direct solution."*
- **It names the joint option and does not refuse it:** *"Care would have to be taken to ensure that
  the chosen alteration aligns with the chosen chord label … but **it is possible to inject this
  dependence into a model**, as in the model proposed by Micchi et al. (2021)."*
- It reports that two options were *"considered (and tried)"* — **both of them post-hoc**, both
  taking a chord label as input — and that the first was abandoned because *"the model would output a
  PC that was never present during a given chord."*
- And at **pp. 9–10**, Experiment 2 and the Discussion make a **measured** argument for splitting the
  task: a chord model on a reduced vocabulary plus this method's post-hoc induction improves accuracy
  on the rarer qualities — *"By making the labeling model's task easier (through a vocabulary
  reduction), and instead relying on our proposed method to induce the rarer chord qualities during
  its late post-processing, a balance can lead to an increase in performance on those rare chords."*

**So: there IS a discussion of alternatives, and there ARE stated arguments for this shape — one of
them measured.** The first two clauses of the claim are corrected.

**The third clause stands, and it is the one that matters.** **No comparison anywhere in the paper
measures post-hoc chord-tone assignment against assignment decided together with chord identity.**
Every alternative it weighs is an alternative *label-space allocation* — where the alteration lives
in the vocabulary — and every measured comparison is within the post-hoc family or against a rule
baseline. **The surface's conclusion that this paper does not argue against joint assignment survives
the correction; its statement that the paper argues nothing does not.**

---

## What this row does NOT establish

- **No tabulated value was verified**, by the commission's exclusion. Tables 1, 2 and 3 were seen and
  agreed with the extracts.
- **The training-strategy experiment (§3.3.1), the vocabulary-reduction figures and Figures 3–7**
  were read but are values and are not enumerated here.
- **Nothing about whether DP-D's chosen position moves.** That is the user's, on the STOP.

## Verdict for the row

**Eight load-bearing structural claims CONFIRMED. Two CORRECTED, both on claims the findings surface
used to reach the DP-D rival-defusal — K1 on what the method does to the segmentation, K2 on what the
paper argues. K1 is the falsifier candidate. Task A stops here.**

*Provenance: read 2026-08-31 at `docs/research_papers/reading_pass_2026_08/chord-sus-jnmr.pdf`, all
fourteen printed pages as page images, staged through the bridge and read with the file tools. Both
extracts and the cross-check for this row were read at the file first, to enumerate. No shell was run
on the repository or on any staged copy of it. No specification derived, no document amended, no code
opened, no register row or entry written.*
