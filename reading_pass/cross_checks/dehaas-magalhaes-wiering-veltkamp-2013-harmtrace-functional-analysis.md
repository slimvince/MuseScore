# Cross-check — row 5: de Haas, Magalhães, Wiering & Veltkamp, HarmTrace

> **The two extracts compared, 2026-08-31**, under `cowork_reading_pass_commission_2026_08_30.md`
> §4 and the independence protocol of `reading_pass/continuation.md` §2.
> First pass: `reading_pass/extracts/dehaas-magalhaes-wiering-veltkamp-2013-harmtrace-functional-analysis.md`
> (session 1, 2026-08-30). Second pass: `reading_pass/extracts_second_pass/` same file name
> (session 2, 2026-08-31), **written and landed before the first extract was opened.**
> **Neither extract has been edited to match the other.**
>
> **The read-tool bound of §0 of the row-1 cross-check applies here unchanged.**

## 1. Agreements, including the one the row exists for

**The parse-space explosion is quoted by both passes from the same sentence, and neither softens
it.** First pass: *"even with a constrained modulation specification that allows modulation only to
specific other keys, and restricts the number of modulations, the total number of ambiguous
analyses quickly explodes."* Second pass: the same sentence with its opening clause — *"Extending
this parameter to contain the key of the piece … is problematic:"* — and the scope statement that
follows from it, *"Our present model does not support full modulation … The model can only handle
change of mode—going from major to minor or vice versa—without changing the root of the key."*

Both also agree on: chord labels and a **given** key as the only inputs, no notes and no voicing; a
functional parse tree as the output, with deleted or inserted chords relative to the input;
error-correcting parsing to depth three with fewest corrections preferred, making the parser total;
**no evaluation of analytical correctness anywhere in the paper**; 3.38 deletions and 9.85
insertions per song on the 5,028-song set with under 6% of chords deleted; ambiguity accepted in
small numbers and controlled by restricting rule application; and the corpus's jazz bias.

**Both passes independently reach the fact of absence that governs how every number here may be
quoted: this paper measures parse coverage, edit counts and time, and grades no analysis against
any human annotation.** Nothing from it is an accuracy figure.

## 2. The one disagreement of record — the publication year — **RESOLVED AGAINST BOTH OUR RECORDS**

The first extract's title line, this population's row 5, and `reading_pass/additions.md` all cite
**CMJ 37(4) 2013**. The second pass flagged the discrepancy and it is now settled at the paper's own
first page: **"Computer Music Journal, 37:4, pp. 37–53, Winter 2014"**, with the copyright line
**"© 2014 Massachusetts Institute of Technology."**

**So the paper's own printed year is 2014, and three of our records say 2013.** Nothing substantive
rides on it — no claim, no figure and no verdict moves — but it is a citation this project would
otherwise carry forward wrong, and correcting it belongs to the bibliography reconciliation the
commission's Task 2 already defers to its own act. **Recorded here; nothing edited.**
*(This pass amends no document, `BIBLIOGRAPHY.md` included.)*

## 3. Items one pass held and the other missed — every one confirmed at the paper

| Held by | Item | Status |
|---|---|---|
| First pass | *"For simplicity, we ignored voice-leading."* | **CONFIRMED** — it is the Figure 1 caption |
| First pass | *"the parser never crashes or refuses to produce valid output"* | **CONFIRMED**, in the experimental-results discussion of the large set |
| First pass | The THEORY label: **Rohrmeier (2007, 2011)** as the generative-syntax basis, **Riemann (ca. 1895)** for the functions | **CONFIRMED** — the second pass had the functions without their attribution, so the first pass's THEORY line is the better-grounded one |
| First pass | Phrase structure deferred to post-processing | **CONFIRMED**, verbatim: *"Such clusterings should be done in a post-processing step, based on metrical positions and phrase-length constraints."* |
| First pass | A Bach chorale shown with no measurement | **CONFIRMED** — Figure 4, the first nine measures of *Ich dank' dir schon durch deinen Sohn* in F major, with no error metric attached |
| Second pass | Preference among competing parses is by **rule ORDER**: *"The order in which the rules are specified also matters, as earlier rules take precedence over later rules; we use this fact to guide the correction process."* | **CARRIED** — it sharpens the first pass's *"typed grammar, precedence"* into the specific mechanism: **no probability, no weight, no confidence separates a rival; an earlier-written rule wins** |
| Second pass | **No comparison against statistical or machine-learned alternatives is made anywhere** | **CARRIED** (a fact of absence) |
| Second pass | Timing at 0.72 s over 72 songs and 384.81 s over 5,028 (76.53 ms per song); hardware stated | **CARRIED** — consistent with the first pass's per-song 10 ms / 76.5 ms, which is the same data |
| Second pass | The grammar's rule count is **not stated**; the paper presents 25 numbered specifications | **CARRIED** — the second extract had listed the count as a gap; it is now a stated absence |
| Second pass | The output's leaf sequence may differ from its input, so a consumer must expect an analysis that disagrees with what it was given | **CARRIED** — the first pass's *"corrected chords as a byproduct"*, stated as a consumer obligation |

## 4. Where the two passes read the SAME fact toward different emphases — recorded, not resolved

Both extracts draw the modulation lesson toward this project's own charters, and they emphasise
differently. The first pass reads it as **chain-level evidence FOR deciding tonality with the chords**
(*"pushed to the grammar level, key changes explode; decided in the one pass, they are a bounded
transition"*). The second pass records the same fact and then warns about the transfer: HarmTrace's
explosion is in **the number of ambiguous analyses a grammar admits**, not in the cost of a
probabilistic decode over a bounded state space, so **whether the lesson carries to a decode is not
settled by this paper.**

**These are not in conflict — the second is a bound on the first.** Neither is a verdict; both are
flagged for Task 4, where the verdict belongs. The point is recorded here so the findings surface
meets the caveat at the same moment it meets the claim, rather than inheriting the stronger reading
alone.

## 5. Verdict

**No value disagrees between the two extracts, and no claim of either is falsified by the other.**
One citation error is found and is common to both our records rather than to either pass (§2). Five
items the first pass held and the second missed are confirmed; five the second held and the first
missed are carried; one shared fact carries a bound the second pass adds (§4).

**The cross-check for row 5 is COMPLETE, at the relayed grade declared above.**

*Provenance: session 2 of the reading pass, 2026-08-31. All resolution reads at the paper's source
URL, `https://dreixel.net/research/pdf/hafha.pdf`. No specification derived, no document amended,
no code opened, no register row or entry written. Neither extract was edited.*
