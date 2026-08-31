# Cross-check — row 2: McLeod & Rohrmeier 2024, chord tone alterations and suspensions

> **The two extracts compared, 2026-08-31**, under `cowork_reading_pass_commission_2026_08_30.md`
> §4 and the independence protocol of `reading_pass/continuation.md` §2.
> First pass: `reading_pass/extracts/mcleod-rohrmeier-2024-chord-tone-alterations-suspensions.md`
> (session 1, 2026-08-30). Second pass: `reading_pass/extracts_second_pass/` same file name
> (session 2, 2026-08-31), **written and landed before the first extract was opened.**
> **Neither extract has been edited to match the other.** Every resolution below names which side
> moved and on what evidence.
>
> **The read-tool bound of §0 of the row-1 cross-check applies here unchanged** — both passes read
> through the same relaying web-fetch tool, so a systematic error of that tool survives both and
> this cross-check cannot see it.

## 1. The load-bearing agreement, reached independently — and it is the important one

**Both passes independently establish that the paper offers NO comparison of its post-hoc shape
against a joint one, and that its stated ground is a label-vocabulary problem.** First pass:
*"joint-versus-sequential deciding of chord and tones not taken up beyond a practical
justification of the sequential shape."* Second pass, from a question aimed directly at it: the
text carries no such discussion, no argument that post-hoc is preferable, and no measurement of
what post-hoc costs.

**This is the point DP-D turns on, and it is now doubly established.** The rival's best-published
form does not argue against deciding chord-tone assignment inside the entangled decision; it
responds to a different problem — the multiplicative blow-up of a flat label vocabulary — which is
a problem about the OUTPUT REPRESENTATION rather than about where the assignment belongs in the
inference. *(What that does to DP-D's verdict is Task 4's; neither extract nor this file takes it.)*

Both also agree, in substance and largely in wording, on: the post-hoc position in the pipeline;
the input label's root, quality and inversion held fixed; the three-step method; the non-default
accuracy sitting at 28.8–39.2 in every condition; the 924-piece corpus at 80/10/10; and the
robustness result under degraded input.

## 2. Disagreements resolved at the paper

### 2.1 What the accuracy is computed OVER — **RESOLVED IN THE SECOND PASS'S FAVOUR; THE FIRST PASS MOVED**

The first extract calls the measurement *"per-note chord-tone detection"* and *"per-note accuracy
split default/non-default/overall."* The second extract calls it exact pitch-class-vector match per
windowed segment.

**Resolved at the paper: the second reading is right, verbatim** — *"Each of these windows is
treated as a separate data point, which we deem correct if the PCs included in the (non-reduced)
ground truth label match exactly the PCs included in the model's output label."*

**Why this is not a quibble.** Per-note chord-tone accuracy and per-window exact-vector accuracy are
different quantities with different difficulty: the window metric is all-or-nothing over a whole
pitch-class set, so **89.2% is 89.2% of WINDOWS fully correct, not 89.2% of notes correctly
classified — a materially harder figure than the first extract's phrasing implies.** Any detail
specification citing this number must cite it as the window figure. The CPM's own per-note sigmoid
is an internal quantity, not the reported metric, and that is exactly the confusion available here.

### 2.2 Whether the merging moves the chord boundaries — **RESOLVED IN THE FIRST PASS'S FAVOUR; THE SECOND PASS MOVED**

The second extract states that *"the SEGMENTATION is not held fixed: consecutive windows are merged
where their pitch-class vectors are compatible, so boundaries do move under this step."* The first
extract states the opposite — boundaries are an upstream input and the method *"does not revise
it."*

**Resolved at the paper: the first reading is right.** The merging operates on the model's own
internal windows **within a single given chord label**; it does not change the input chord
boundaries.

**Why this one matters.** It is the difference between a post-processor that only decorates its
input and one that can move a boundary — and the second reading, uncorrected, would have made the
rival look more capable than it is at exactly the place DP-C and DP-D meet. **The second pass's
claim is withdrawn on this evidence.**

### 2.3 Whether the model sees the chord root — **BOTH PARTLY RIGHT; THE SECOND PASS'S PHRASING SHARPENED**

The second extract records that the CPM's features exclude *"the current chord's root"*. Confirmed —
but the paper's own reason makes the fact almost the opposite of what the bare statement suggests:
each note's pitch class is *"represented as the number of perfect 5ths above the root"*, and the
current chord's root one-hot is dropped only *"since it would always be 0"*.

**So the root is not absent from the model — it is the FRAME OF REFERENCE for every note feature,
and is omitted as a separate field precisely because that frame makes it constant.** The second
extract's sentence is true and misleading; it is corrected here rather than in the extract. The
first extract carries neither the fact nor the error.

## 3. Items one pass held and the other missed — every one confirmed at the paper

| Held by | Item | Status |
|---|---|---|
| First pass | The vocabulary ground, verbatim: *"Adding an additional feature to each chord label results in a multiplicative increase in vocabulary size … which reduces the possible training data per label and weakens predictive power."* | **CONFIRMED** — the second pass had the conclusion without the mechanism |
| First pass | Baseline figures: overall **76.1** with ground-truth input, **61.1** with noisy input (full vocabulary), against the method's 89.2 and 73.2 | **CONFIRMED** — the second pass carried the method's column only, so it could not state the gain |
| First pass | The Ju et al. 2017 positioning | **CONFIRMED, verbatim**: *"Their model is designed to work specifically on 4-part Chorales … Their model also treats enharmonically equivalent PCs as identical (i.e., it considers only 12 PCs), while ours uses 35 … Finally, our method takes a hypothesis chord label as input, while theirs only takes the PCs."* |
| First pass | The corpus includes **internal (unreleased) data** beside ABC, the Mozart sonatas and 36 Corelli trio sonatas | **CONFIRMED** — the second pass's relay named only the three public sets. *The unreleased portion is a bound on anyone's ability to reproduce these figures, and it belongs with the figures.* |
| First pass | The ~4-point vocabulary-reduction cost under noisy input against ~11 under ground truth | **CONFIRMED**, and it is arithmetic both passes' tables support (89.2→78.4 and 73.2→69.0) |
| Second pass | The CPM's architecture: feed-forward → one or more **bi-directional** LSTM layers → feed-forward → one sigmoid per note | **CARRIED** — no contradiction |
| Second pass | The three thresholds *d*, *a*, *r* with their grids, and the merge-compatibility rule quoted | **CARRIED** |
| Second pass | The baseline is a **rule set that runs the same merging procedure** — so the gain is over hand-written rules with identical segmentation machinery, not over nothing | **CARRIED**, and it sharpens the first pass's *"heuristic baseline"* |
| Second pass | **Pedal tones are not discussed anywhere** — the 2021 companion named them as future work beside suspensions, and this paper does not deliver them | **CARRIED** (a fact of absence) |
| Second pass | The non-default column barely moves under degraded input while the default column loses ~18 points | **CARRIED** — a reading of both passes' tables, not a new figure |

## 4. Verdict

**No value disagrees between the two extracts.** Two substantive readings diverged and both are now
settled at the paper — one against each side (§2.1 to the second pass, §2.2 to the first) — and one
phrasing is sharpened (§2.3). Everything else is coverage, and every covered item is confirmed.

**The cross-check for row 2 is COMPLETE, at the relayed grade declared above.**

**★ One thing worth carrying to Task 4 whichever way DP-D falls:** the figure most likely to be
quoted from this paper is **89.2%**, and it is a per-window exact-match figure on **ground-truth
chord labels**, over a corpus a portion of which is unreleased. The comparable figure when the
chords come from a model rather than from an annotator is **73.2%**, and the accuracy on the
alterations themselves — the thing the method exists to find — is **36.7%** and **35.8%**
respectively.

*Provenance: session 2 of the reading pass, 2026-08-31. All resolution reads at the paper's source
URL, `https://apmcleod.github.io/pdf/chord-sus-jnmr.pdf`. No specification derived, no document
amended, no code opened, no register row or entry written. Neither extract was edited.*
