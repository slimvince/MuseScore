# Second-pass extract — row 5: de Haas, Magalhães, Wiering & Veltkamp, HarmTrace

> **STATUS: SECOND INDEPENDENT EXTRACTION (session 2 of the reading pass, 2026-08-31).**
> Written under `cowork_reading_pass_commission_2026_08_30.md` §4, per the independence protocol
> of `reading_pass/continuation.md` §2. **Neither `reading_pass/extracts/` nor
> `docs/research_papers/reading_pass_2026_08/` was opened for this paper before this file was
> written.** Read at its source, `https://dreixel.net/research/pdf/hafha.pdf`, in two
> separately-prompted passes.
>
> **GRADE, DECLARED AT ITS FACE: RELAYED, not at-the-object** — the same web-fetch bound the other
> second-pass extracts carry. Session-and-prompt independence, not read-tool independence.

## Identity

W. Bas de Haas, José Pedro Magalhães, Frans Wiering & Remco C. Veltkamp, "Automatic Functional
Harmonic Analysis", *Computer Music Journal* **37:4**, pp. 37–53.

**★ A bibliographic discrepancy, recorded not resolved.** The paper's own printed issue line, as
relayed twice, reads **Winter 2014**; this population's row 5 and `reading_pass/additions.md` both
cite the year as **2013**. CMJ 37:4 is ordinarily the Winter 2013 issue. Nothing substantive rides
on it, but the bibliography reconciliation this pass owes should settle it at the object rather
than inherit either.

## Claims, labeled

**[FACT] What it is.** A parser that takes a **symbolic chord sequence** and returns a
**hierarchical functional analysis** — a parse tree whose leaves are the input chord labels, whose
internal nodes are harmonic relations (functional category, scale degree, transformation) and whose
root is the piece.

**[FACT] The formalism is a context-free grammar encoded as Haskell generalized algebraic data
types.** Relayed verbatim: *"The HarmTrace system explores the relations between (generalized)
algebraic data types and context-free production rules."* Grammaticality is then enforced by the
language's own type checker rather than by a separately written parser check. What the grammar
encodes: Riemann's tonic / dominant / subdominant functions, Roman-numeral scale degrees, chord
classes, and transformations — secondary dominants, tritone substitutions, diatonic chains of
fifths.

**[FACT] Error correction is the mechanism that makes it total.** Relayed verbatim: *"When faced
with a chord that does not fit the harmony model, it will consider all possible combinations of
deletion and insertion of chords (up to a fixed depth of three steps) to adapt the chord sequence
to the model."* The fewest-edit correction wins, so **every input yields an analysis**; an
unparseable sequence is not refused, it is repaired.

**★ [FACT] THE PARSE-SPACE LESSON, WHICH IS WHY THIS ROW IS IN THE POPULATION.** Relayed verbatim:
*"Extending this parameter to contain the key of the piece … is problematic: even with a
constrained modulation specification that allows modulation only to specific other keys, and
restricts the number of modulations, the total number of ambiguous analyses quickly explodes,
given the rules of the previous section."*

**[FACT] How modulation is handled instead — by exclusion, and the scope statement says so.**
Relayed verbatim: *"Our present model does not support full modulation, i.e., modulation to every
possible key. The model can only handle change of mode—going from major to minor or vice versa—
without changing the root of the key."* The recommended workaround is to **segment the chord
sequence by key first** — with external key information or a key-finding algorithm — and analyse
each section independently.

**★ THE READING OF THOSE TWO TOGETHER, STATED PLAINLY BECAUSE IT IS THE ROW'S WHOLE POINT.** A
grammar rich enough to express functional harmony, given a free tonality axis, **does not merely
get slower — its number of admissible analyses explodes**, and the authors' response was not a
better search but to **remove the tonality axis from the grammar and require it as a parameter
from outside.** That is a measured-in-practice statement about the cost of putting tonality inside
a combinatorial harmonic search, made by people who tried it.

**[FACT] The key is a required INPUT, not an inference.** Relayed verbatim: *"This requires the
model to have information about the key of the piece."* The system is parametrised by key and
mode, and the user supplies them.

**[FACT] Ambiguity is admitted but bounded, and the ranking is by rule ORDER, not by a score.**
The paper accepts *"a small number of ambiguous analyses"* where the context does not prefer one,
on the ground that *"Musical harmony is ambiguous and chords can have multiple meanings depending
on the tonal context in which they occur."* Preference among competing parses is positional:
*"The order in which the rules are specified also matters, as earlier rules take precedence over
later rules; we use this fact to guide the correction process."* **There is no probability, no
weight and no confidence anywhere in the selection** — a rival is preferred because its rule was
written earlier in the file. Specific specifications are additionally restricted from applying
where basic ones do, explicitly to stop ambiguity growing exponentially.

**★ [FACT of absence, from a targeted read] THE PAPER REPORTS NO EVALUATION OF ANALYTICAL
CORRECTNESS.** Its evaluation is parse coverage, edit counts and timing. **No comparison against
human harmonic analyses is reported.** So none of its numbers is an accuracy figure, and none may
be quoted as one.

**[FACT of absence] No comparison against statistical or machine-learned alternatives is made.**
The paper does not argue the grammar approach's merits against a learned one.

**[FACT] It performs no segmentation and addresses no ornamentation.** It takes a chord sequence
whose segmentation is already given as text labels; non-chord tones are outside it entirely.

**[FACT] A stated corpus bias.** Relayed verbatim: *"Because a large corpus of chord sequences,
mainly from the jazz repertoire, is available for retrieval tasks, the harmony model exhibits a
bias towards jazz harmony."* The authors say it *"can be used to analyze some classical works as
well"*, secondary to that focus.

**[CONJECTURE / stated applications, unmeasured here]** Harmonic similarity estimation, automatic
chord transcription (Chordify) and automatic harmonisation are named as applications; **no measured
result for any of them is given in this paper.**

## Measured results, as tabulated

| Corpus | Quantity | Value |
|---|---|---|
| Small, 72 songs | deletions per song | 0.83 |
| Small, 72 songs | insertions per song | 2.79 |
| Small, 72 songs | total parse time | 0.72 s |
| Large, 5,028 songs | deletions per song | 3.38 |
| Large, 5,028 songs | insertions per song | 9.85 |
| Large, 5,028 songs | total parse time | 384.81 s (76.53 ms per song) |
| Large, 5,028 songs | chords deleted | under 6% of all chords |

Hardware as stated: Intel Core 2 6600 at 2.4 GHz, 3 GB RAM, GHC 7.0.3.

**These are coverage-and-cost figures, not accuracy figures** — see the fact of absence above.

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** a **chord sequence already segmented and already labelled** in the Harte et
al. (2005) syntax, **and the key and mode supplied from outside**. It infers no tonality, finds no
boundaries, reads no notes. Of everything read in this population so far, this method sits furthest
downstream: it presupposes that the entangled decision has already been made by someone else.

**HANDS downstream:** a parse tree — functional category, scale degree and transformation per node
— over the input chords, with chords possibly **deleted or inserted** relative to the input.
**A consumer must be prepared for an output whose leaf sequence is not its input sequence**, which
is an unusual and load-bearing property: the analysis can quietly disagree with what it was given.

**STATED SCOPE and limits:** no full modulation, mode change only; jazz-biased model; symbolic
chord labels only; no segmentation; no ornamentation; no accuracy evaluation; ambiguity resolved
by rule order rather than by evidence.

## Bearing, flagged for the findings surface (verdicts are Task 4's)

- **The parse-space explosion is direct primary-source evidence about the cost of a free tonality
  axis inside a combinatorial harmonic search** — relevant wherever this project's L2 charter is
  challenged as too entangled, and equally as a caution about what makes such a search tractable.
  *Note the asymmetry carefully, because it cuts both ways:* HarmTrace's explosion is in the number
  of **ambiguous analyses admitted by a grammar**, not in the cost of a probabilistic decode over a
  bounded state space. Whether the lesson transfers is a question for Task 4 and is not answered
  here.
- **Its ambiguity handling is the opposite of DP-K's shape**: rivals exist but are ordered by where
  their rule was written, and no evidence-bearing quantity separates them.
- **Its error correction is a candidate mechanism and a candidate hazard**: a total parser that
  edits its input to fit the model will always produce an analysis, including where the model is
  wrong about the music.

## What this extract does NOT establish

- The grammar's size in rules, or what "Spec. 16–17" name.
- Whether the small and large corpora are annotated at all, and by whom.
- What fraction of songs required correction at all, as against the per-song edit means.
- Whether the ambiguity restriction mentioned for specific specifications changes any analysis.
- **Nothing here is at-the-object.** Every figure and quotation is relayed.

*Provenance: second pass of the reading pass, 2026-08-31. Read at the source URL only. No
specification derived, no document amended, no code opened, no register touched.*
