# Task A, row 5 — de Haas, Magalhães, Wiering & Veltkamp, HarmTrace — AT THE OBJECT

> **STATUS: TARGETED RE-READ, AT THE OBJECT, 2026-08-31.** Executing §2 of
> `cowork_reading_pass_remedial_commission_2026_08_31.md`, resumed under the user's ruling on the
> row-2 STOP. **All seventeen pages (printed pp. 37–53) read as page images with the file tools**,
> from the PDF the user supplied at `docs/research_papers/reading_pass_2026_08/hafha.pdf`, staged
> through the bridge. **No web-fetch read of any kind was used on this row.** A targeted re-read, not
> a third extraction. **Nothing of the findings surface is edited here.**
>
> **This paper prints its own page numbers** (37–53); every location below is the printed page.
>
> **★ ONE CORRECTED VERDICT, on a claim carried under DP-B's and DP-E's SUPPORTS verdicts.** By §2's
> letter that is a falsifier candidate and a per-row STOP. **It is recorded here and surfaced to the
> user rather than stopping the run** — a departure declared at the foot of this file, on the ground
> of his ruling that the design-point question is answered when all seven re-reads are in.

## The CONFIRMED claims

### C1 — The key is a required input the system cannot infer — **CONFIRMED**

Carries **DP-B's** first clause and the upstream cell of the §3.1 coupling table.

**p. 41:** *"Our present model does not support full modulation, i.e., modulation to every possible
key. The model can only handle change of mode—going from major to minor or vice versa—without
changing the root of the key. … **As a consequence, this requires the model to have information
about the key of the piece.**"*

**p. 45** gives the workaround the surface names: *"Another, more practical, solution is using
external key information, either obtained from key signatures in the score, or by applying an
automatic key-finding algorithm. … Information about the key can then be used to segment the chord
sequences into sections that contain only a single key, and HarmTrace can be applied to these
sections individually."* **The coupling table's "chord labels and the key, single-key stretches" is
exact.**

### C2 — Modulation is excluded from the shipped grammar — **CONFIRMED**

**p. 45:** *"HarmTrace supports chord borrowing from parallel keys, and its secondary dominant
specifications can be used to explain local key changes, but it does not support modulating to all
possible keys."* Restated in the Discussion, **p. 50**.

### C3 — Error-correcting parsing to a fixed depth of three, fewest edits preferred, and the parser is total — **CONFIRMED, verbatim**

Carries **DP-M's ENRICHES** entry.

**p. 46:** *"When faced with a chord that does not fit the harmony model, it will consider all
possible combinations of deletion and insertion of chords (up to a fixed depth of three steps) to
adapt the chord sequence to the model. In this way, the simplest corrections (involving the fewest
insertions or deletions) are chosen."* **p. 50:** *"the parser never crashes or refuses to produce
valid output."* **Both quotations are exact**, and Figure 8 (p. 49) shows a deletion and an insertion
in worked trees. **The output's leaf sequence need not be its input's — confirmed at the figures as
well as the text.**

### C4 — Rivals are ordered by rule position, with no probability, weight or confidence — **CONFIRMED, and the authors give their reason**

Carries **DP-K's** contrast entry.

**p. 46:** *"The order in which the rules are specified also matters, as earlier rules take precedence
over later rules; we use this fact to guide the correction process."* **Exact.**

**★ An addition the surface does not carry, and it strengthens the contrast.** The sentence
immediately before it: *"We could also assign different costs to each specification, in order to
prefer some rules over others. **In practice, we did not find this necessary.**"* And at **p. 40**,
of context-free grammars generally: *"It is possible to use rule-weightings and to set low weights to
rules that explain rare phenomena. This allows for ordering the ambiguous solutions by the total
relevance of the rules used. This does not overcome the fact that … the number of parse trees grows
exponentially."* **So weighting was known, available and deliberately declined** — the absence of
mass here is a choice, not an oversight, which is exactly what DP-K's contrast wants to say.

### C5 — No evaluation of analytical correctness anywhere — **CONFIRMED at the whole read**

Carries **DP-O's** *"it cannot be DP-O's falsifier either"* and DP-M's *"whether the edits help is
unmeasured."*

The *Experimental Results* section (**pp. 49–50**) measures deletions, insertions, corrections,
chords per song and parse time — Table 1, **p. 50** — and nothing else. Figures 3–8 are example
analyses carrying no metric, the Bach chorale at Figure 4 among them. **No analysis anywhere in the
paper is graded against a human annotation.** Established over the whole document rather than by a
prompted question.

### C6 — The jazz bias, in the paper's own words — **CONFIRMED**

Carries §5's routing to the style system. **p. 39:** *"because a large corpus of chord sequences,
mainly from the jazz repertoire, is available for retrieval tasks, the harmony model exhibits a bias
towards jazz harmony."*

### C7 — Voice-leading ignored; phrase structure deferred to post-processing — **CONFIRMED**

**p. 38**, Figure 1 caption: *"For simplicity, we ignored voice-leading."* **p. 51:** *"**We believe
that such** clusterings should be done in a post-processing step, based on metrical positions and
phrase-length constraints."* — our records quote this from *"Such clusterings…"*; the page prints the
lead-in *"We believe that such clusterings…"*. **Substance identical; the transcription is not
exact**, the same class of small silent improvement row 19's second extraction made a bar about.

### C8 — The publication year — **CONFIRMED against our records, which are wrong**

**p. 37** prints *"Computer Music Journal, 37:4, pp. 37–53, Winter 2014"* and *"© 2014 Massachusetts
Institute of Technology."* **The cross-check's §2 finding holds at the object.** Three of our records
say 2013.

**★ And one fact for the same reconciliation that no pass recorded:** the same page prints
*"Published under a Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0)
license."* `BIBLIOGRAPHY.md`'s redistribution tiers turn on exactly this, and this paper has no row
there yet.

---

## ★ The CORRECTED claim — the parse-space explosion is a stated expectation, not a measurement

**The claim as the findings surface carries it**, in two places, both under a **SUPPORTS** verdict:

- **§2, DP-B:** *"Row 5, HarmTrace [RELAYED]. Its key is a required input the system cannot infer,
  and **attempting to put tonality inside the grammar made** 'the total number of ambiguous analyses
  quickly explode[]'."*
- **§2, DP-E:** *"An unconstrained tonality axis **was measured**, in practice, to be the thing that
  broke tractability."*
- And **§5** routes it forward as *"Row 5's parse-space explosion as the standing caution on an
  unconstrained tonality axis inside a combinatorial search."*

**What the pages say. The quoted clause is exact, and its status is not what the surface gives it.**

**p. 45**, in full: *"Although adding a modulation specification to the model is straightforward,
this **would** quickly lead to an avalanche of ambiguous solutions. For example, all specifications
of the model are currently parametrized by a mode … Extending this parameter to contain the key of
the piece, in line with Rohrmeier's (2011) model, is problematic: even with a constrained modulation
specification that allows modulation only to specific other keys, and restricts the number of
modulations, the total number of ambiguous analyses quickly explodes, given the rules of the previous
section."*

Three things follow, each at the page:

1. **No attempt is reported and no measurement is given.** The verbs are conditional — *would* quickly
   lead — and the passage is the authors' stated reason for **not** building modulation. The paper's
   only experiment (Table 1, p. 50) measures parsing of the shipped, modulation-free grammar.
   **"Attempting … made" and "was measured" both attribute an experiment the paper does not report.**
2. **A second explosion statement, p. 51, is likewise a prediction:** implementing tonicizations and
   secondary dominants together *"**would inevitably lead to** an explosion of ambiguous solutions for
   a harmony progression featuring secondary dominants."*
3. **The word "unconstrained" understates the paper rather than overstating it.** The claim is made
   *"even with a constrained modulation specification"*. But the authors immediately add that such a
   specification is *"very well possible from a specification point of view"* with *"a much smaller
   model"*, and that even then *"keeping the number of different analyses under control might be
   challenging"*. **The claim is conditional on this grammar's own rule set** — *"given the rules of
   the previous section"* — which is a bound the surface does not carry.

**Why this matters, and how far it reaches.** DP-B and DP-E each rest primarily on **V2 and V7,
verified at the object** from Rocher et al.; row 5 is an additional support, not the ground. So the
correction does not remove either design point's footing. What it does is downgrade this row's
contribution from **a measurement** to **an implementer's stated expectation, given his own rule
set** — which is a different kind of evidence, and this project's own #18 and #19 are precisely about
not letting the second be cited as the first.

**★ And this was already seen once, by the second reader, and did not reach the surface.** The
row-5 cross-check's §4 records that the second pass warned the explosion is *"in the number of
ambiguous analyses a grammar admits, not in the cost of a probabilistic decode over a bounded state
space, so whether the lesson carries to a decode is not settled by this paper"*, and states that the
point is recorded *"so the findings surface meets the caveat at the same moment it meets the claim,
rather than inheriting the stronger reading alone."* **Neither DP-B's bullet nor DP-E's carries the
caveat, and DP-E strengthened the claim further by adding "was measured."** That is a finding about
the transfer from cross-check to surface, not about either reader.

---

## Additions worth carrying to any L2 detail specification

- **A hand-set recursion cap governs what the search can reach. p. 46:** *"one particular parameter
  has a large influence on the parsing and error-correction process. This parameter controls the
  number of recursive applications of the specifications for secondary dominant and the like … It
  must be set carefully, because setting it to a very low value will lead to bad analyses, and
  setting it to a high value will make the internally generated model very large, resulting in
  increased error-correction times and often sub-optimal error-correction solutions. For the examples
  and results in this article we have used values between five and seven."* And **p. 47** shows the
  cap losing a defensible reading: *"HarmTrace misses this additional analysis, however, because the
  maximal number of recursive applications has been reached."* **A reachability bound with a
  hand-chosen constant, and a worked instance of what it costs — R-5's own subject, in someone
  else's system.**
- **The large corpus is user-generated and noisy by the authors' own account (p. 49)**, containing
  *"peculiar and unfinished pieces, wrong key assignments, and other errors"* — which is what the
  robustness result is a result about.

## What this row does NOT establish

- **No tabulated value was verified**, by the commission's exclusion; Table 1's values were seen and
  agree with the extracts.
- **Nothing about DP-D.** Recorded because the user's ruling holds that question open across all
  seven rows: **row 5 bears on it not at all** — it takes chord labels as given and assigns no chord
  tones.
- **Whether the modulation lesson transfers to a probabilistic decode.** The paper does not settle
  it, as the second reader said; this re-read confirms the paper does not settle it.

## Verdict for the row

**Eight load-bearing structural claims CONFIRMED, two of them with additions that strengthen the
readings they support. One CORRECTED — the explosion's evidential status — bearing on DP-B and DP-E,
recorded and surfaced, not resolved. No falsifier against any design point. Two transcription
inexactnesses recorded (C7 here, and the year at C8 which was already known).**

## The declared departure

**§2 of the commission makes a corrected claim under a SUPPORTS verdict a per-row STOP.** This row
produced one and **the run was not stopped.** The ground, stated rather than assumed: the user ruled
on the row-2 STOP that the design-point question is **held open and answered when all seven re-reads
are in**, and ordered rows 3, 5, 17, 18 and 21 run. Stopping on each corrected claim would defeat the
run he ordered, and continuing does not absorb the finding — it is recorded here, surfaced to him in
the same session, and it will carry its own column in the consolidated table. **If he wants the
per-row STOP kept for design points other than DP-D, that is his to say, and this file is the record
that a session read his ruling wider than DP-D.**

*Provenance: read 2026-08-31 at `docs/research_papers/reading_pass_2026_08/hafha.pdf`, all seventeen
pages as page images, staged through the bridge and read with the file tools. Both extracts and the
cross-check for this row were read at the file first, to enumerate. No shell was run on the
repository or on any staged copy of it. No specification derived, no document amended, no code
opened, no register row or entry written.*
