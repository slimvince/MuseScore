# LLM-Assisted Triage for Chord Inference Validation — Design Discussion

**Status:** Discussion only. No implementation committed. This document captures
a design conversation between Vincent Wong and Claude on 2026-04-23, preserved
so future planning sessions can pick up the shared context rather than restart
it.

## Problem

We have an inferrer (the chord analysis pipeline in `src/composing/` plus the
notation bridge) that produces chord symbols, Roman numerals, and Nashville
numbers for a score. For authoritative corpora — Bach chorales with music21
ground truth, Beethoven quartets with DCML annotations — we can compute
mismatch percentages mechanically against the external labels (see
`tools/corpus_registry.json`).

For the ~125 scores in `tools/extra_scores_registry.json` (`ground_truth: false`
across jazz/piazzolla/steelydan groups), we have no mechanical comparator. The
scores often have printed chord symbols, but those symbols are frequently
*prescriptive* — instructions to a rhythm section about what voicing to play,
not descriptions of the notes actually written. Comparing our inferrer's output
against printed symbols therefore produces noise: the inferrer is reading
notes, the symbols are sometimes describing intent.

We want a way to direct the inspector's (Vincent's) scarce time at the
regions most likely to contain real errors, without hand-reviewing every
region of every score.

## Core principle

> When our inferrer, one or more LLMs, and any printed chord symbol differ
> within reason, flag that region for human inspection.

"Within reason" is a tunable threshold that adjusts based on how much evidence
is available and how reliable each source has historically been.

## Key design decisions

### The tool is a triage filter, not a comparison evaluator

The primary output is a ranked work queue — scores and regions the inspector
should look at next — not an agreement percentage. Aggregate metrics
("% agreement with LLM ensemble") are secondary and, if misused as an
optimization target, actively harmful because they encourage tuning the
inferrer toward whatever systematic biases the ensemble shares.

Recall matters more than precision. A false positive costs the inspector a
few minutes; a false negative is a missed error that ships. Threshold
calibration should lean toward flagging more rather than fewer, tuned by
observed inspector fatigue rather than by optimizing for a single number.

### Multi-LLM, parallel-as-async

"Parallel" here means *an accumulating body of opinions per score*, not
simultaneous API calls. Multiple LLMs (frontier cloud models plus local
open-source models) analyze scores independently, on different days, possibly
with different prompt versions. The registry retains all opinions; the triage
computation reads whatever opinions are available at the moment it runs.

A score with one LLM's opinion on file produces weaker triage than a score
with four. That asymmetry is fine and visible — it surfaces as a confidence
field on the triage output.

Local LLMs earn their place specifically as an always-available backstop:
when quota is exhausted or cloud models are down, a weak opinion from a
low-track-record local model, honestly disclosed, still contributes epsilon
of signal and keeps the tool usable.

### Music-specialized classifiers are a distinct participant category

Symbolic-music BERT variants (MusicBERT, RNBERT, MMT-BERT, etc.) are worth
discussing as ensemble participants, but they are not drop-in peers of the
generative LLMs and should not be treated as such.

They are discriminative token-level classifiers, not open-ended generators.
Output shape is a label per position over a closed tag vocabulary (Roman
numeral, chord quality, key). There is no free-form reasoning pass, no
"explain yourself" channel, and the input path is MusicXML → MIDI →
OctupleMIDI/REMI (or the variant the specific model expects). That conversion
chain is its own drift surface: our bridge writes the MusicXML, a third-party
step reads it into MIDI, another step tokenizes to the model's training
representation. Any one of those steps can discard information we care about
(voice leading nuance, enharmonic spelling, pedal metadata) before the model
sees the score.

The bigger trap is the training-data-independence problem. RNBERT and
comparable Roman-numeral classifiers are fine-tuned on DCML-derived corpora —
which is the same ground-truth source we use for the Beethoven quartets in
`tools/corpus_registry.json`. On those scores the classifier is not adding
an independent opinion; it is approximately reproducing the comparator we
already have. Counting its agreement as a fourth ensemble vote would
double-book our existing authoritative label.

On jazz / pop / non-common-practice material, these classifiers are
out-of-distribution and are probably weaker than a general frontier LLM at
the same task, but we will not know until we check. The per-style
track-record segmentation in the design handles this asymmetry naturally:
a specialized classifier can carry a high (model, version, DCML-style)
track record and a low (model, version, jazz-style) track record
simultaneously, and the triage weighting respects that.

Net role if one of these ships in the tool: specialized local-model
participant. Strong candidate on common-practice classical where its
training domain matches; honest low weight on styles where we have no
evidence; explicit flag that its opinion on DCML scores is *not* independent
from the DCML ground truth and must not be mixed into the agreement
calculation for those scores without accounting for that correlation.

### Per-LLM track-record weighting

Each LLM accumulates a per-model track record keyed by (model_id, version,
effort_tier), ideally sub-segmented by style tag when sample sizes permit.
The score updates from human verdicts on previously-triaged regions: when the
inspector resolves a flag, each LLM that had an opinion on that region gets
credit (full, partial, or zero) based on how close its prediction was.

Updates should be *soft-scored*, not binary right/wrong. Ambiguous regions
where multiple analyses are defensible are the regions that matter most for
calibration, and binary scoring throws away information exactly there.

Bootstrapping: day one, scores are uniform priors with zero observations.
Early triage weights all models equally (or uses pre-registered guesses).
As human verdicts accumulate, weighting becomes meaningful. A Bayesian
(beta-prior) shape handles uncertainty honestly — 80% over 3 observations
is a very different signal than 80% over 200, and the downstream threshold
logic should see that distinction.

### Availability resilience

The pipeline does not block waiting for complete data. Each run of the tool
collects whatever opinions are available at the time: LLMs with quota remaining
respond, LLMs that fail (quota, outage, timeout, budget cap) are logged and
queued for next cycle. The registry is the durable state; the tool is what
advances it when cycles permit.

Emergent property from combining track-record weighting with availability
resilience: the triage threshold *auto-adjusts* to input quality. High-
track-record ensemble available → tight threshold, confident flags. Only a
weak local model available → widened threshold, fewer flags at lower
confidence, honest disclosure rather than drowning the inspector.

### Input format: structured plain text, deliberately boring

Named formats (ABC, Lilypond, Humdrum/kern) each carry model-specific
training-data priors. ABC excels on monophonic folk tunes; Lilypond buries
content under engraving syntax; Humdrum is rare enough in training data
that model behavior is unpredictable. None were designed as LLM input.

Use a custom structured plain text instead — unambiguous English-readable,
no format prior needed, evolvable as we learn what LLMs trip over. Sketch
(not committed):

```
Key: Bb major
Time: 4/4
Tempo: 120 bpm (quarter)

m1 b1 (quarter): RH [F4 Ab4 C5 Eb5]  LH [Bb2 F3]   printed: "Bbm7"
m1 b2 (quarter): RH [F4 Ab4 C5 D5]   LH [Bb2 F3]
...
```

### Do not over-reduce before the LLM sees it

Tempting to pre-reduce to "sounding pitches at beat X" with sustained notes
included by our windowing logic. Don't. Deciding what counts as sounding at
a given beat *is* analytical work — it's what `collectRegionTones`, pedal
windows, and decay weights do in the production path. If the tool pre-applies
our methodology before the LLM sees anything, the LLM is evaluating a
reduced view that reflects some of our choices, which weakens the
independence the ensemble needs.

Pass onsets with durations; let the LLM window. More tokens, more independence
— and independence is the whole point.

### Chord symbol handling: two passes, different purposes

For the independent-opinion pass, strip printed chord symbols from the input.
Anchoring is real; show the LLM "the printed symbol is Cm7(b5)" and its
analysis will drift toward that answer whether or not the notes support it.
The three-way comparison (inferrer × LLM × printed) requires the LLM's pass
to be note-only.

Separately, a second pass *can* show the LLM both the notes and the printed
symbol, asking explicitly: "Does the symbol describe the sounding notes
(description), partially describe a superset (partial instruction), or
contradict them (full instruction)?" That classification is itself valuable
— it's how a region or score gets automatically tagged as "printed symbols
are prescriptive, do not use as ground truth." Two prompts, two registry
fields, two analytical purposes.

### Output format mirrors input

LLMs should return structured output (structured-output / tool-use modes for
cloud models; JSON-schema prompts with retry for weaker models). The
comparator parses without fuzzy matching. Chord labels should normalize to
the same canonical form produced by the production `ChordSymbolFormatter`
rather than whatever dialect each model happens to emit (`Cmaj7` vs `CM7`
vs `C major 7`) — otherwise the normalization layer becomes its own drift
surface. Reuse the production formatter if possible.

### Human verdicts as accumulating ground truth

When the inspector resolves a flagged region, the verdict is captured as
structured data: "inferrer was right," "inferrer was wrong, the answer is
X," "genuinely ambiguous between X and Y." These verdicts accumulate in
the registry over many cycles, yielding a hand-annotated corpus
*concentrated on the difficult regions* — which is more valuable
per-annotation than a uniform sample of easy cadences.

The byproduct loop: verdicts update per-LLM track records → next cycle
triage improves → fewer false flags → inspector time used more
productively. The loop is the point. A verdict-capturing UI (even very
minimal — CSV or registry-edit workflow) is a prerequisite for the tool
to improve over time.

### Triage output surfaces model reliability to the inspector

When a flag is presented, the inspector should see which LLMs contributed,
their track records on the relevant style, and the specific disagreement.
Example: "flagged by Claude Sonnet 4.6 (0.87 jazz accuracy over 156 obs)
and GPT-4 (0.79 over 98 obs), not flagged by local Llama (0.52 over 43
obs)." Hiding this context leads the inspector to second-guess the tool
rather than use it. Visible reliability is also an incentive for the track
records to remain accurate — they're user-facing.

### Registry extends the existing pattern

The existing `tools/extra_scores_registry.json` schema grows optional
fields per score entry: one per (model, version, effort) analysis result,
plus a `human_verdicts` field for resolved regions, plus per-score
metadata tracking which LLMs have been attempted and which succeeded.
No new storage system; same JSON pattern already in use.

## Relationship to the production path

This tool would rely on `batch_analyze` (or equivalent) to produce our
inferrer's output. `batch_analyze` today duplicates several pieces of
bridge logic (see `ARCHITECTURE.md` §2.10 / §4.1c "Rule 10" violations:
harmonic boundary detection, windowed pitch collection, bass-movement
sub-boundaries). Any triage tool using its output inherits those drift
risks. The companion refactor — moving the duplicated helpers *down* into
`src/composing/` so both bridge and batch_analyze link one implementation —
is a prerequisite for the triage measurements to be meaningful at the
per-region level.

## Non-goals explicitly discussed

- **Not a replacement for the authoritative corpora.** Bach chorales,
  Beethoven quartets, and similar corpora with external ground truth
  remain the primary correctness signal. LLM-assisted triage extends
  coverage to scores where that signal is absent.
- **Not "LLM as ground truth."** Any single LLM is one imperfect evaluator;
  the tool treats LLM output as opinions to be weighted, not facts to be
  matched. A single-LLM "% agreement" metric as the primary evaluation
  target would encode that vendor's biases into our inferrer's evolution.
- **Not a blocker for iterations 1-10 of the current refactor.** The
  triage tool is a downstream quality-of-life addition; the refactor
  iterations have standalone value and should not wait on this.

## Open questions for when planning starts

- Input format: custom structured text, a minimal MusicXML subset, or
  a hybrid? A practical test (hand-prepare one score in each candidate
  format, paste to three LLMs, compare reliability and consistency)
  should precede committing to a format.
- Inspection UI: CSV-based workflow, lightweight web page, or integrated
  into a notebook? The verdict-capture step is the critical UX — if it
  takes more than a few seconds per verdict, the loop breaks down.
- Cost policy: per-run budget caps, per-model priority ordering, cadence
  of re-runs when the inferrer changes. Needs a concrete design once the
  tool takes shape.
- Track-record segmentation granularity: (model, version, effort) is
  certain; adding style tags depends on whether sample sizes will support
  per-genre cells within a reasonable time horizon.
- Pass policy for score sizes that exceed any single context window
  (e.g. Sun Bear Concerts at 1323 regions). Chunking with overlap has
  alignment overhead; pre-segmenting by region couples the LLM's view
  to our segmentation. Worth empirical investigation before committing.
