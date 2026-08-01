# The decision inventory — a READING SAMPLE from the decision harvest

> **★ SUPERSEDED AS AN AUTHORITY (2026-08-01, the OI-207 adjudication). The decisions register is
> `DECISIONS.md`.** Read that first; it is the one place a decision's status is recorded. This file
> stays as a reading aid and for provenance.
>
> **What this document is — restated honestly.** A **reading sample**: a legible, subject-organized
> selection of decision-bearing statements the mechanical harvest found, presented for a reader who
> knows music theory and software architecture but nothing about this project's internal vocabulary.
> **It is NOT authoritative and NOT complete.** Its earlier opening called the entries "the canonical,
> load-bearing decisions", which is a completeness judgment — and the dispatch that produced this file
> forbade adjudication, so no such judgment could have been made here. The 2026-08-01 adjudication
> established the point concretely: the harvest's signature net cannot see a decision written as plain
> specification, so load-bearing decisions were provably absent from it (the priority-of-evidence
> ranking `ARCHITECTURE.md:3134-3141`, the slicer's boundary rule `:1045`, the piece-start shortcut
> `:3128-3130`). The register was therefore built by reading the layer specifications in full, with
> this harvest as the searchable index and the backstop it genuinely is.
>
> The complete, verbatim, machine-readable list — every one of the
> **15,224** decision-bearing statements the harvest found — lives beside this file in
> `decision_candidates.json` and `decision_candidates.csv`. Every one of those statements now carries a
> recorded disposition in `cluster_dispositions.csv` (the OI-207 adjudication, Task 3).
> **This document does not decide anything, does not judge whether a
> statement is still in force, and does not check any decision against the code.** Those were the
> next pass's work, and it has run: `DECISIONS.md` (status) and `OPEN_ITEMS.md` (conformance).
>
> **How each entry reads.** Every entry gives the decision **verbatim** (the exact recorded
> words, which the conformance audit depends on) followed by a one- or two-sentence **plain
> restatement** — what it actually decided, in ordinary words. The verbatim never replaces the
> restatement, and the restatement never replaces the verbatim. Each carries its source location
> as `file:line`, which is the stable provenance; the machine list holds its own internal
> identifiers (`DH-…`, i.e. decision-harvest candidate numbers) if a statement needs tracing there.
>
> **Scope of THIS document versus the machine list.** The harvest cast a deliberately wide net
> and over-captured (15,224 candidates, of which 8,741 are in Claude Code's own session reports,
> which mostly *restate* decisions made elsewhere). This document presents a **sample** of
> decisions that seemed load-bearing on a first reading — quoted from the home the harvest recorded,
> grouped by subject. It makes **no claim of completeness and no claim of authority**: a decision
> absent from this file may still be load-bearing, and a decision present here may since have been
> superseded. `DECISIONS.md` is where that is settled.

---

## A note on words (in force for this whole document)

This is a music-analysis project, so many ordinary software words collide with music-theory
words. The standing convention (recorded in `CLAUDE.md`) is: **the bare word always carries its
music-theory meaning; every non-musical use is spelled out.** So in this document —

- **score** bare = the piece of music. The number a candidate reading earns is a *candidate
  score* or *numerical score*.
- **key** bare = tonality. A lookup handle is a *map key*.
- **measure** bare = the bar. To gauge something is a *measurement*; the act is *to gauge*.
- **note** bare = a pitch event. A written comment is an *annotation* or *remark*.
- **register** bare = pitch register. The project's issue tracker is *the open-items register*,
  always in full.

A handful of project-internal terms have no everyday meaning and are **defined at first use**,
in the entry where they first appear. The recurring ones:

- **slice** — the smallest stretch of time the analyzer works in: the music is cut wherever any
  note starts or stops, and each gap between two such cuts is one slice.
- **segment** — a longer stretch the analyzer commits to a single reading (one key, one chord).
- **the joint estimator** (or *joint decode*) — the single combined method that works out key,
  chord, and where the boundaries fall all at once, rather than as separate stages.
- **the record** — the one published data structure the in-app analysis reads its answers from.
- **seam** — a place in the program where some other feature asks the analyzer a question
  ("what chord is under this note?").
- **arm** — one of two code paths kept side by side during a changeover (the old *legacy arm*
  and the new *record arm*).
- **emission** — the part of the model that judges how well the pitches actually sounding fit a
  proposed chord.
- **factor** — one named piece of musical evidence the model weighs.
- **gate** — a yes/no rule that decides whether a candidate reading is even allowed to compete.

Nine subjects follow.

1. [Which notes we look at, and when](#1-which-notes-we-look-at-and-when)
2. [How the music is cut into stretches for analysis](#2-how-the-music-is-cut-into-stretches-for-analysis)
3. [How a key is decided](#3-how-a-key-is-decided)
4. [What may count as a chord, and how one is chosen](#4-what-may-count-as-a-chord-and-how-one-is-chosen)
5. [How non-chord tones are treated](#5-how-non-chord-tones-are-treated)
6. [What the analysis publishes, and who may read it](#6-what-the-analysis-publishes-and-who-may-read-it)
7. [How the result is displayed](#7-how-the-result-is-displayed)
8. [How we gauge ourselves, and what counts as a regression](#8-how-we-gauge-ourselves-and-what-counts-as-a-regression)
9. [How work is sequenced and ratified](#9-how-work-is-sequenced-and-ratified)

---

## 1. Which notes we look at, and when

**Sounding notes are the strongest evidence there is.**
*Verbatim:* the priority-of-evidence table ranks, from strongest to weakest — "Actual sounding
notes | what is literally happening now" (Strongest); "Temporal context | surrounding measures"
(Strong); "Notated key signature" (Weak); "`KeyMode` enum | explicit major/minor tag" (Weakest).
— `ARCHITECTURE.md:3134-3141`.
*In plain words:* what the ear actually hears at a moment outranks the surrounding bars, and both
outrank the written key signature and any explicit major/minor tag. The notes decide; the
paperwork only leans.

**A note counts toward the analysis only if it is really playing, visible, and on a pitched
staff — but a note ruled out is carried along, never thrown away.**
*Verbatim:* "A note participates in boundary generation iff layer 1 flagged it `plays && visible
&& staffEligible`. … A muted / invisible / non-tonal-staff note opens **no** boundary, yet still
rides along in each slice's `overlapping()` set (passed through, not dropped)." —
`ARCHITECTURE.md:1047-1051`.
*In plain words:* muted, hidden, or non-pitched notes don't create new analysis boundaries, but
they are still kept beside every slice as passenger information rather than discarded — losing
information is not allowed even for notes that don't drive the reading.

**A slice's identity is exactly the set of notes sounding through it — not merely which pitch
classes are present.**
*Verbatim:* "**Slice identity is the eligible sounding-NOTE set** (not the octave-folded PC set —
a unison/octave shrink is a real boundary though the PC set is unchanged)." —
`ARCHITECTURE.md:1052-1053`.
*In plain words:* if two voices in octaves collapse to one, that is a real change of texture and
starts a new slice, even though the collection of pitch classes did not change. (*Pitch class* =
a note name regardless of octave; *octave-folded* = treating all octaves of a name as the same.)

**At the very first moment of a piece, a declared key signature is trusted outright — as a
pragmatic exception, not a general rule.**
*Verbatim:* "the function returns the declared mode immediately (confidence 0.5) rather than
waiting for pitch evidence that cannot yet exist. This is a deliberate pragmatic choice for the
score opening, not a general bypass." — `ARCHITECTURE.md:3128-3130`.
*In plain words:* before any notes have sounded there is nothing to analyze, so the piece's
opening simply believes the written key signature; everywhere else the notes still win.

> **A live conformance question sits under this subject** (rowed, not decided, as **OI-215's
> sibling** and Task 0 of the dispatch that produced this document): the model's chord-fit
> judgment was decided to read *per sounding tone*, but the code as built reads only tones whose
> **onset** falls inside a segment, so a note still ringing from earlier contributes nothing.
> That is a gap between a recorded decision and the implementation, and it is exactly the kind of
> thing the conformance audit exists to find — it is flagged in the open-items register, not
> resolved here.

---

## 2. How the music is cut into stretches for analysis

**The cut points are every note-start and every note-end of the eligible notes — nothing else.**
*Verbatim:* "Boundaries = the sorted-unique union of every **onset AND every release** of the
**eligible** notes; consecutive boundaries form the slices." — `ARCHITECTURE.md:1045`.
*In plain words:* the analyzer places a boundary wherever any qualifying note begins or stops
sounding, and the stretches between consecutive boundaries are the slices; a note ending matters
just as much as a note starting, because the sonority changes either way.

**Where one reading ends and the next begins is not fixed in advance — it is something the model
works out, not a preset grid.**
*Verbatim:* the governing architecture decision — the estimator is "one probabilistic decode over
`(tonic, mode, chord)` **with segmentation as a modeled (semi-Markov) variable** and every
enumerated clue as a theory-grounded factor". — `OPEN_ITEMS.md:16-18`.
*In plain words:* rather than chopping the music on a fixed rhythm and labeling each chunk, the
method treats "where does this harmony stretch to?" as one of the unknowns it solves for.
(*Semi-Markov* is the mathematical name for a process that stays in a state for a stretch of
variable length before jumping — here, a chord persists over a segment whose length is itself
inferred.)

**The official regression gauge is deliberately blind to how finely the music was cut.**
*Verbatim:* the governing hard regression stop is "the **granularity-robust union-of-boundaries
unit, variant (b) DCML-only** …, duration-weighted and **segmentation-invariant**." —
`CLAUDE.md` gate block (A), line 232.
*In plain words:* two analyses that carve the same passage differently but reach the same
harmonic conclusions must gauge as equal, so that a change to how the music is sliced can never
by itself look like an improvement or a regression. (Full treatment of this gauge is in
subject 8.)

**On the corpus/batch path, the old rule that let the slicer itself fix a chord's root and
quality from the key is gone.**
*Verbatim:* the segmenter's tonic-prior overwrite "**SUPERSEDED-IN-FACT on the batch/corpus
surface 2026-07-26 (OI-178 — the joint decode never runs greedyExpandSegmentation); remains LIVE
on the legacy notation path**". — `OPEN_ITEMS.md:113` (OI-175 row).
*In plain words:* deciding what a chord *is* while you are still deciding where it *starts and
ends* was ruled a layering violation; the new combined method never does it on the batch path,
though the same fault still lives in the older in-app path until that path is retired.

---

## 3. How a key is decided

**Key, mode, and chord are decided together, as one judgment — not by a separate "key stage"
feeding a "chord stage".**
*Verbatim:* "The key/mode/chord estimator is **JOINT (option A)** — one probabilistic decode over
`(tonic, mode, chord)` … NOT a feed-forward pipeline, NOT a separable 'key layer.'" —
`OPEN_ITEMS.md:16-18`.
*In plain words:* the project rejected a pipeline where key is settled first and handed
downstream; instead one method weighs all the evidence and settles key, mode, and chords in a
single coordinated decision, because these choices constrain each other.

**The published key answer is a two-mode key plus a raw count of the actual scale color — no
21-name mode label is ever emitted.**
*Verbatim:* "No 21-value mode label is inferred or published anywhere (C1); the two-mode key plus
this table informationally dominates the retired labels (#12)." —
`cowork_notation_output_contract.md:145-147`.
*In plain words:* rather than forcing a single exotic mode name (Dorian, Phrygian-dominant, …),
the analysis publishes the key as one of two modes plus an exact tally of which raised/lowered
scale degrees were actually heard; that tally carries strictly more information than any one
label would, so no label is lost by dropping it.

**That scale-color tally is published exactly as counted — nothing rounded, nothing hand-set.**
*Verbatim:* "This is the whole publication — counted, un-rounded, nothing hand-set: minor's
variable 6̂/7̂ (Dorian color, subtonic-vs-leading-tone), major's lowered 7̂ (Mixolydian color) or
raised 4̂ (Lydian color), and every borrowing appear as their actual counts." —
`cowork_notation_output_contract.md:141-144`.
*In plain words:* for each scale degree the analysis reports how long and how often each
chromatic version of it was heard, verbatim from the notes; the display may later phrase this as
"Dorian-leaning", but the published fact is the raw counts, not an interpretation.

**Key agreement is gauged against two references at once — the piece's home key and the local
key of the moment.**
*Verbatim:* the ratified convention — "Grade the key-agreement column against BOTH the DCML global
(home) and local key, both carried everywhere the key column appears." — `OPEN_ITEMS.md:241`
(OI-143 row).
*In plain words:* when checking whether the analyzer got the key right, it is compared both to the
overall tonal home of the piece and to whatever key is momentarily in force, and both values are
always reported side by side rather than collapsed into one. (Here "DCML" is the reference
annotation source described in subject 8.)

**The exotic dominant-family modes are graded as the minor key of their parent scale, by the
user's ruling.**
*Verbatim:* "the five dominant-family exotic modes … now reduce to the MINOR key of their PARENT
COLLECTION — an emitted 'C♯PhrygDom' grades as F♯ minor, the key it is the dominant of". —
`CLAUDE.md` gate block (A), ~line 314.
*In plain words:* when the analyzer names something like "C♯ Phrygian-dominant", the scoring
treats it as F♯ minor — the key that chord is the dominant of — because the human annotators read
those passages that way about two-thirds of the time and the tonic-triad reading zero percent.

---

## 4. What may count as a chord, and how one is chosen

The chord decisions concentrate in one document, `docs/scoring_model.md` §8, which explicitly
frames itself: "*These are load-bearing design decisions. Future changes must respect them or
risk regressions*" (`docs/scoring_model.md:907-910`). The load-bearing ones:

**A dead end, recorded so nobody re-walks it: making one continuity bonus conditional on a thin
predecessor.**
*Verbatim:* "`rootContinuityBonus` sparse-predecessor gate is a dead end (Iter 98). Both
density-based and inversion-aware variants tried; both regress mozart_k280-1 IV→V65 Alberti
bass." — `docs/scoring_model.md:915-917`.
*In plain words:* an attempt to withhold a "same underlying-note-as-before" bonus when the
previous chord was thinly voiced was tried twice and abandoned both times, because it broke a
specific Mozart passage; the failure is recorded so the idea is not retried blind.

**A rule about what suppresses which bonuses when the analyzer is still finding boundaries.**
*Verbatim:* "**`ScoringPhase::Segmentation` must suppress all context-dependent bonuses.** …
Adding a new context bonus without gating it … will cause segmentation regressions." —
`docs/scoring_model.md:924-928`.
*In plain words:* while the analyzer is still deciding where chords begin and end, any scoring
help that depends on neighbouring chords must be switched off, or the boundary-finding gets
corrupted; a new context-sensitive bonus that ignores this rule will cause regressions.

**One particular bonus is the mechanism that picks which spelling of a diminished-seventh chord
wins — do not remove it blindly.**
*Verbatim:* "**`dim7CharacteristicBonus` is the dim7 rotation selector.** Do not suppress without
replacing the non-diatonic-♭♭7 mechanism (B3 lesson)." — `docs/scoring_model.md:912-913`.
*In plain words:* a fully-diminished-seventh chord has four equally-valid roots by pitch alone;
this bonus is what breaks that tie toward the correct spelling, so removing it without a
replacement leaves the chord unrootable.

**The chord-template list is size-locked by the compiler, so adding one is a deliberate,
all-at-once act.**
*Verbatim:* "**Template arrays update atomically under `analysis::kTemplateCount`.** … Adding a
template = bump the constant + add the template/mask entries in the same edit". —
`docs/scoring_model.md:930-935`.
*In plain words:* the set of recognized chord shapes and all the tables sized to it are tied to a
single count, so the build refuses if you add a shape without adding its matching entries —
closing an old class of silent corruption. (A *template* here = one recognized chord shape the
analyzer matches against.)

**Chord-selection thresholds are tuned to Baroque music on purpose and are not to be loosened for
other styles.**
*Verbatim:* "**Gate thresholds are Baroque-calibrated.** Do not widen Baroque-tuned thresholds to
accommodate Jazz or other styles … Use a tighter structural guard or a preset-specific override
instead." — `docs/scoring_model.md:950-953`.
*In plain words:* the numeric cut-offs that admit or reject chord readings are set for Bach-era
music; if another style needs different behavior, the fix is a stricter rule that names the
troublesome chord type or a separate per-style setting — never a loosening of the Baroque value.

**Several more narrow constraints in the same section** — the four load-bearing gates on the
step-voice-leading bonus (`:919-922`), the "both a major third and an augmented fifth" condition
on the augmented-seventh guard (`:947-948`), the sparse-bass inversion rule (`:955-956`), and the
post-bonus quality guard for the diminished bonus (`:958-960`) — each records a specific past
regression the rule prevents. They are cataloged verbatim in the machine list under
`docs/scoring_model.md`.

> **A live conformance question sits under this subject** (rowed as **OI-226**, not decided
> here): the combined method's rule for which chord candidates are even *allowed to compete* was
> found to have **no stated basis** in the ratified decode plan — it arrived through a code port
> with only inline comments. That absence-of-a-recorded-decision is precisely OI-207's subject
> matter; it is flagged in the open-items register.

---

## 5. How non-chord tones are treated

**A pedal point is defined by its musical role, independent of which voice holds it — replacing
an older bass-only definition.**
*Verbatim:* "The pedal-point concept — the STRUCTURAL pedal of harmony theory (a tone held against
changing harmony), not the piano sustain-pedal marking — becomes an ornament-label class …
defined VOICE-INDEPENDENTLY (bass / internal / inverted sub-labels) … This supersedes the legacy
bass-only `isPedalPoint`/`pedalBassPc` fact … the voice-independent class publishes strictly more
information (#12) from the same facts." — `cowork_notation_adoption_increment.md:504-512`.
*In plain words:* a sustained tone held under (or over, or inside) changing harmony is recognized
as a pedal point wherever it sits, not only in the bass; this replaces the old code that only
noticed bass pedals, and it loses nothing because it says strictly more from the same evidence.
(An *ornament-label class* = a category of non-chord tone the analysis can tag after it has
decided the chords.)

**Three alternative ways of handling the pedal were examined and explicitly ruled out, each with
its reason.**
*Verbatim:* "P2 (keep the legacy detector alive: #6/#7/#19 failures), P3 (drop: #12 regression),
P4 (a pedal factor in A's model: forbidden now by #8/#17/#18/#22; lawful only via a measured
residual and a ledgered factor proposal) — excluded, recorded per the constrained-optimum
ledger." — `cowork_notation_adoption_increment.md:512-514`.
*In plain words:* keeping the old detector was rejected (it duplicates and is unestablished),
dropping pedal detection entirely was rejected (it loses information), and building pedal
awareness directly into the model was rejected for now (it is not yet permitted to add a model
ingredient without first measuring the need). Only the post-analysis labeling approach survives.

**Non-chord-tone labels in general are a post-analysis publication, delivered on their own later
step, and marked with how well established they are.**
*Verbatim:* "The record reserves the per-note ornament-label fields (category per the fitted
emission's classes; the voice-independent pedal-point class … per the §10 ruling). They are
delivered by OI-194's own increment, status-marked; until then the fields are absent". —
`cowork_notation_output_contract.md:149-155`.
*In plain words:* after the chords are settled, each note can be tagged as a chord tone or a
particular kind of non-chord tone; this is a separate future deliverable, and until it ships the
fields are simply left empty rather than filled with guesses.

---

## 6. What the analysis publishes, and who may read it

**Every derived fact is published once, at its source, and everyone else reads it — nobody
recomputes it.**
*Verbatim:* "every derived analytical fact is **published exactly once, on the producing layer's
output surface; consumers read, never re-derive.** A fact consumed by no one is either **declared
dormancy** (its future consumer named) or **waste** (removed)." — `CLAUDE.md:91-95`.
*In plain words:* a computed fact has exactly one home; other places in the program look it up
there instead of working it out again, and a fact nobody uses must either name its intended
future user or be deleted.

**Facts that could serve as evidence for a future reading are published broadly even before
anyone asks for them.**
*Verbatim:* "for EVIDENCE-class facts … **publish broadly even without a named consumer** — …
a visible smörgåsbord of evidence lets a future design RECOGNIZE useful facts it would never have
thought to request." — `CLAUDE.md:96-100`.
*In plain words:* clues the analysis happens to notice are laid out openly so a later design can
spot uses for them it would never have known to ask for — with each such clue carrying a mark of
whether it is trustworthy enough to lean on.

**The in-app analysis reads from exactly one published data structure, and the per-note question
is a lookup into it, not a second computation.**
*Verbatim:* "the answer is a VIEW query over the same record … No second computation exists
(#6): the note seam is a lookup into the span seam's record." —
`cowork_notation_output_contract.md:40-44`.
*In plain words:* asking "what chord is under this note?" does not run the analysis again — it
looks the answer up in the same single record the whole-span analysis produced, so there is only
ever one analysis path.

**The publication carries the full ranked list of candidate readings, not just the winner or a
top-few — no cut-off number exists anywhere.**
*Verbatim:* "both axes publish the FULL scoreable candidate lists — the original 'runner-up' /
'top-N' wording is superseded. No truncation constant exists anywhere in the publication (a
breadth 'N' or a gap-window width would be a hand-set value with no basis) … nothing computed is
discarded at the boundary". — `cowork_notation_output_contract.md:108-113`.
*In plain words:* the analysis hands on every reading it scored, in ranked order, rather than
keeping only the best one or the best few; there is no magic number that trims the list, because
any such number would be an unjustified invention and would throw away evidence a later
refinement needs. (This is the project rule "verify at the whole output surface, winner *and*
carry" made concrete.)

**Two different uncertainty numbers are published as separate, clearly-named fields and never
silently swapped for each other.**
*Verbatim:* "the gap is a log-score difference, the mass is a probability; neither ever silently
replaces the other (#19: two different instruments, each trusted only under its own
establishment). Both carry establishment status on the surface". —
`cowork_notation_output_contract.md:128-132`.
*In plain words:* the analysis reports two kinds of "how sure is it" — "the gap" (how far the
winning reading's fit-number exceeds the alternative's) and "the mass" (the winning reading's
share of the total probability) — and because they mean different things, they are kept as
distinct labeled fields, each marked with how well trusted it is. Neither is yet a calibrated
real-world probability; both are the model's own internal numbers.

**Every published analysis states which fitted values produced it — a provenance-less analysis is
not allowed to exist.**
*Verbatim:* "Every published record carries its instrument provenance … A consumer — and any
future measurement — can always answer 'which fitted values produced this analysis' from the
record itself; a provenance-less analysis cannot exist." —
`cowork_notation_output_contract.md:52-57`.
*In plain words:* each result carries a stamp of the exact tables and weights that made it, so
anyone can always trace a reading back to the settings behind it and reproduce it.

---

## 7. How the result is displayed

**A permanent, enforced boundary separates the analysis (what is true) from the presentation
(how it is shown).**
*Verbatim:* "the record stays preset-independent; renderings are presentation, facts are
published … A permanent dependency-direction guard enforces the boundary both ways (user
directive at the D2 ruling)." — `cowork_notation_output_contract.md:104-106`.
*In plain words:* the analysis produces style-neutral facts, and the choice of how to show them —
which style preset, which symbol — is a separate downstream concern; a built-in guard makes it
impossible for display choices to leak back into the analysis or vice versa. (A *preset* here =
a display style such as "Baroque" or "Jazz".)

**Display may phrase a mode from the raw scale-color counts, but the phrasing is a presentation
act, not a published fact.**
*Verbatim:* "The presentation layer may FORMAT a reading from it ('Dorian-leaning'); the published
fact is the counts, with establishment status." — `cowork_notation_output_contract.md:144-145`.
*In plain words:* turning "raised sixth heard mostly" into the words "Dorian-leaning" happens only
at display time; the analysis itself only ever publishes the counts, so the interpretation can be
changed without touching the facts.

**Two display gaps are recorded as faithful-to-the-facts, not as bugs, and deferred.** The
augmented-sixth family currently shows as a plain major-triad symbol because the fitted chord
vocabulary collapses it to major pitch content (`OPEN_ITEMS.md:153`, OI-201 row — "*Faithful to
the published facts, not an inference bug*"); and a non-diatonic root currently renders as "?" in
Nashville-number display (`OPEN_ITEMS.md:83`, OI-113 row).
*In plain words:* both are known display incompletenesses that honestly reflect what the analysis
knows, are recorded in the open-items register, and are to be finished at the display layer rather
than patched by distorting the analysis.

---

## 8. How we gauge ourselves, and what counts as a regression

**The official regression stop: the amount of music where the root is genuinely decidable but we
get it wrong must never grow.**
*Verbatim:* "the **class-(b) (pitch-class-decidable-root) root-disagree DURATION must be
NON-INCREASING** vs the committed reference — the *meaningful* functional errors never grow. Any
preset increasing ⟹ FAIL." — `CLAUDE.md` gate block (A), ~line 334.
*In plain words:* the single hard gate on every change is measured in *how much playing time* we
get a decidable root wrong, and that quantity is not allowed to rise; a change that increases it
anywhere fails, full stop.

**Errors are split into two categories, and only the meaningful category is a hard stop.**
*Verbatim:* the two-tier policy — "**Class (b) — functional/key regression: UNCHANGED HARD STOP**"
(a chord whose root *is* decidable by pitch, gotten wrong) versus "**Class (a) —
symmetric-rotation churn: TRACKED, CONDITIONAL**" (a chord whose root is undecidable by pitch
alone, such as a symmetric diminished-seventh). — `CLAUDE.md` gate block (B), ~lines 403-409.
*In plain words:* when a chord genuinely has a right root and we miss it, that is the serious
error and can never increase; when a chord is inherently ambiguous by pitch (so no reading is more
correct), a change in which ambiguous spelling we pick is tolerated within limits and watched, not
treated as failure. (*Symmetric* = a chord that looks the same from several roots, so pitch alone
cannot choose.)

**A change may not be graded on the data used to tune it; the headline number is the held-out
one.**
*Verbatim:* "No value is graded on data that helped fit it. Every fit event declares its held-out
data (split or k-fold) and its capacity budget … BEFORE fitting; the headline claim is the
held-out figure." — `CLAUDE.md`, Guiding principle 20.
*In plain words:* any number learned from examples must be scored on *different* examples set
aside in advance, and how many free numbers you are allowed to tune is fixed before you start, so
that a value cannot be graded against the very cases that shaped it. (*Held-out* = examples
deliberately reserved for grading; *capacity* = how many free numbers a method is permitted.)

**Ground truth is itself measured, not assumed perfect — you cannot claim a residual is
irreducible below the level annotators disagree.**
*Verbatim:* "The accuracy of ground truth is itself a measured quantity — per-axis annotator
agreement, not an assumed binary … Every precision target and every 'irreducible residual'
verdict is interpreted against that measured ceiling." — `CLAUDE.md`, Guiding principle 21;
tracked open at `OPEN_ITEMS.md:187` (OI-179).
*In plain words:* the reference annotations are treated as an imperfect gauge whose own error is
to be measured; without knowing how often expert annotators disagree, you cannot tell a real
analysis error apart from a place the experts themselves would argue about.

**The reference annotations are the DCML "When in Rome" corpus; music21 only corroborates, it is
not ground truth.**
*Verbatim:* the recurring standing note — "music21 is NOT ground truth" — carried through the gate
policy. — `CLAUDE.md` gate block (A).
*In plain words:* correctness is judged against the human-expert DCML analyses; the music21
library's readings are used only as a cross-check, never as the arbiter.

**Every reported number carries its uncertainty; a difference inside the noise is not a finding.**
*Verbatim:* "Sampling noise on the measurement corpus is quantified; a difference within the
uncertainty is not a finding, and no decision rests on one." — `CLAUDE.md`, Guiding principle 24.
*In plain words:* because the test set is finite, every number has a margin of error attached, and
a change smaller than that margin does not count as evidence of anything.

**Every gauged number is stamped to the exact corpus and tool version that produced it.**
*Verbatim:* "Every measurement is stamped to corpus-hash + instrument-commit; snapshot the
outgoing reference before any re-baseline." — `CLAUDE.md`, Guiding principle 16.
*In plain words:* every result records which snapshot of the music and which version of the gauge
made it, and before any baseline is replaced the old one is saved — so a number can always be
reproduced and a change can always be traced.

---

## 9. How work is sequenced and ratified

This subject holds the project's meta-decisions — the rules about *how decisions are made and
carried out*. They are numerous; the load-bearing ones follow, and the remainder (the full 24
guiding principles and their amendment trail) are quoted verbatim in the machine list under
`CLAUDE.md`.

**Build only on established fact and theory.**
*Verbatim:* "Build only on established fact and theory — published research, public algorithms,
public software. Fact-finding (investigative) coding is allowed." — `CLAUDE.md`, Guiding
principle 1.
*In plain words:* every design rests on something already known and citable; exploratory
investigation to gather facts is fine, but building inference on a hunch is not.

**One path per concern — no duplicated code anywhere.**
*Verbatim:* "Total unification — no duplication of any code. One path per concern." — `CLAUDE.md`,
Guiding principle 6.
*In plain words:* each job in the system is done in exactly one place; two copies of the same
logic is a defect to be unified, not a convenience.

**No accuracy-chasing changes until every method sits in its correct layer.**
*Verbatim:* "No inference-problem-driven coding until all methods and algorithms are implemented
in their correct layer." — `CLAUDE.md`, Guiding principle 8.
*In plain words:* the structure is built first; you may not tweak the code to fix a particular
wrong analysis until the machinery it belongs to is in place — otherwise fixes accrete as
patches. (This is why this very audit is scaffolding work, and why inference improvements wait.)

**A surprise is a stop, not a curiosity to build around.**
*Verbatim:* "Surface a surprise as a STOP before building around it (the operational form of #3)"
(Guiding principle 13); "An unexpected finding means we have failed #1 … treat it as a failure to
diagnose, not a curiosity" (Guiding principle 3). — `CLAUDE.md`.
*In plain words:* if the system does something unexpected, that means an assumption was wrong, so
work halts to diagnose it rather than coding a workaround on top of the mystery.

**Every behavior change is one revertible, provenance-stamped, user-approved commit.**
*Verbatim:* "Every behavior change is user-ratified as one revertible, provenance-stamped commit."
— `CLAUDE.md`, Guiding principle 14.
*In plain words:* nothing that changes what the analyzer does ships without the user's approval,
and it ships as a single commit that can be cleanly undone and traces its own justification.

**Before any inference-affecting design is built, its assumptions are laid out, predicted, and
hand-traced — the Premise Gate.**
*Verbatim:* Guiding principle 17 requires a "premise ledger — every load-bearing causal claim
explicitly labeled **FACT** … **THEORY** … or **ASSUMPTION**", a "**written quantitative
prediction per assumption** … recorded *before* measuring — no prediction, no build", and a "**desk
simulation** — trace the mechanism by hand through the intended architecture on 3–5 real corpus
cases". — `CLAUDE.md`, Guiding principle 17.
*In plain words:* every design first writes down what it is assuming and whether each assumption
is a proven fact, an established theory, or a guess; commits to a numeric prediction in advance so
it cannot rationalise the result afterward; and walks the mechanism through real examples by hand
before any code is written.

**An unchecked causal claim, and an unestablished gauge, are both forbidden to carry load.**
*Verbatim:* "Unverified causal premises are FORBIDDEN (Class A). No design may carry load on a
causal claim about our own system or data that is checkable but unchecked" (principle 18);
"Unestablished instruments are FORBIDDEN (Class B) … trusted only after being *positively
established* … never because it is merely unfalsified" (principle 19). — `CLAUDE.md`.
*In plain words:* you may not build on a claim about our own system that could be checked but was
not, and you may not trust a measurement tool, corpus, or gate until it has been actively proven
correct — "no evidence against it" is not the same as "shown to be right".

**Designs are chosen for the best possible inference alone; the value of reusing existing code
does not get a vote.**
*Verbatim:* "the value of reusing existing code, and the cost of making existing code obsolete,
are SECONDARY … **(b)** downstream implementation impact … carries NO weight; **(c)**
end-user-visible behavior change carries NO weight (the 2026-07-26 unshipped-scoping ruling)". —
`CLAUDE.md:106-113` (decision-neutrality corollary).
*In plain words:* the best design for accurate analysis is picked first; "but we already have code
that does it another way", "but this would make other parts change", and "but users would see it
differently" are explicitly disallowed as reasons — reuse counts only as work already proven
correct, never as sunk cost. (Every behavior change still needs approval; this only says it
doesn't need *permission-by-inertia*.)

**Every discovered-but-unresolved issue has exactly one home: the open-items register.**
*Verbatim:* the register is "the ONE home for every discovered-but-unresolved issue and the
**authoritative status surface** … a stage may not open while a register item gating it is open".
— `CLAUDE.md`, open-items-register section.
*In plain words:* nothing gets tracked in scattered prose; each open issue gets one indexed row
whose status is the single source of truth, and a phase of work cannot begin while an issue that
blocks it is still open.

**A temporary rewrite runs beside the old code under a declared, pre-approved sanction, with a
retirement map — and that retirement happens before the big reviews.**
*Verbatim:* the sanctioned dual path — "A built beside the certified stack temporarily violates #6;
declare the parallel decode + side-by-side grading + the retirement map so the transition is
pre-ratified." (`OPEN_ITEMS.md:114`, OI-180); the ordering — the architecture restructure runs
"AFTER the OI-180 retirement map's deletions settle, BEFORE the OI-198/199/200 reviews"
(`OPEN_ITEMS.md:176`, OI-205).
*In plain words:* when a replacement must run alongside the code it replaces, that duplication is
allowed only as a declared, pre-approved, time-boxed state with a written plan for removing the old
path; and the old path is removed before the whole-system reviews run, so the reviews read a clean
structure. (A *retirement map* = the written plan naming what gets deleted and when.)

**One local fix must never be contributed back to the upstream MuseScore project.**
*Verbatim:* the distribution constraint — "**FORK-LOCAL ONLY — NEVER merge upstream / to the
MuseScore community.** … Any future push/PR/merge that would carry `cfc7eb5e39` … toward
`musescore/MuseScore` is a HARD STOP". — `CLAUDE.md:679` region.
*In plain words:* a MusicXML import fix made for this fork may live in the user's own repository
but must never be pushed or merged into the public MuseScore project; any action that would carry
it there is a hard stop.

**The whole-piece interactive analysis was shelved on measured evidence — a bounded window won.**
*Verbatim:* "The *whole-score* decode variant (originally ratified as Q1) was **shelved** after
this A/B; the cache shipped as a **bounded-window** memoization". — `docs/p3_granularity_ab_3_1b.md:3-6`;
mirrored in code — "the originally-ratified whole-score decode was SHELVED because its premise …
was falsified by the 3.1b A/B" (`src/notation/internal/notationcomposingbridge.cpp:333-334`).
*In plain words:* an earlier decision to analyze the whole piece for each interactive query was
reversed once measurement showed a bounded window around the query was as accurate and cheaper;
this reversal lived in an archived evidence document, and a later build re-introduced whole-piece
analysis unaware of it — which is the exact contradiction that motivated this entire audit, now
tracked openly as OI-210.

---

## Self-test and recall notes (dispatch rules 8 and 3)

**Readability self-test.** Every entry above was checked against the question *"would a reader who
knows music theory and software architecture, but nothing about this project, understand what was
decided and why it matters?"* First drafts that leaned on an undefined internal term or a
statistics word were rewritten: **11** entries were rewritten on that test — the two-mode-key
entry, the semi-Markov-segmentation entry, the two-uncertainty entry, the held-out-evaluation
entry, the ground-truth-ceiling entry, the Premise-Gate entry, the class-(a)/(b) entry, the
slice-identity entry, the pedal voice-independence entry, the full-candidate-list entry, and the
decision-neutrality entry — each of which first used a term or number the target reader could not
be expected to know, and was given a defining clause or a plain-words consequence.

**One decision resisted plain restatement and is flagged as a finding:** the published
*content-score gap* versus *marginal mass* distinction (subject 6, the two-uncertainty entry) can
be *described* in plain words — one is how far a reading's fit-number exceeds the alternative, the
other is the reading's share of the probability — but *why the project keeps them as two
instruments rather than one* rests on a statistical claim (that a re-scoring difference and a
forward-backward probability are established by different evidence and neither is a calibrated
confidence) that cannot be made fully lawful to a non-statistician without the mathematics. The
consequence is stated plainly (they are never swapped, each is trusted only under its own proof),
which is the part a reader needs; the underlying equivalence question is genuinely mathematical.
Per the dispatch, a decision nobody can restate plainly is itself worth recording — this one
restates *far enough to check*, but its full justification does not reduce to plain words.

**Recall note — decisions the signature net does NOT catch (important for the conformance audit).**
A signature harvest can only find statements phrased with decision-vocabulary. Three of the
load-bearing decisions quoted above carry no such vocabulary and are therefore **absent from the
machine candidate list** — they are quoted here from the source directly:

- the priority-of-evidence table (`ARCHITECTURE.md:3134-3141`) — a plain ranked table, no ruling
  words;
- the slicer's boundary definition (`ARCHITECTURE.md:1045`) — a specification sentence in a
  responsibility table;
- the piece-start declared-key shortcut (`ARCHITECTURE.md:3128-3130`) — worded as a "deliberate
  pragmatic choice", which the net does not recognize.

This is the general lesson, and it matches the dispatch's own instruction: **`ARCHITECTURE.md`'s
per-layer specifications are the primary home of how-a-layer-should-work decisions, and they must
be read in full by the conformance audit — the harvest is a supplement to that reading, not a
replacement for it.** (The neighbouring paragraph at `ARCHITECTURE.md:1047-1053` *is* caught,
because it contains the phrase "never re-decided", which pulled the slice-identity decision into
the harvest; the bare table row one line above it was not.)
