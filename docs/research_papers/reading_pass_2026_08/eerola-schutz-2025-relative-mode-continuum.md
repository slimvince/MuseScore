# FETCHED CONTENT RECORD — Eerola & Schutz 2025, "Major-minorness in tonal music: Evaluation of relative mode estimation using expert ratings and audio-based key-finding principles" (Psychology of Music)

> **Retrieval record.** Population row 10 ("relative mode as a continuum", R113). Candidate
> identified last slice; CONFIRMED at the paper 2026-08-30: the abstract's own words build "on
> a continuum, an approach we refer to as 'relative mode'". Fetched from the publisher's page
> `https://journals.sagepub.com/doi/10.1177/03057356251326065`, read whole via two prompted
> extraction calls (standing bound in `reading_pass/additions.md`). Not central.

## Method

Relative mode estimation: Δ = max(similarity over 12 major keys) − max(similarity over 12
minor keys), from pitch-class distributions of SYMBOLIC (MIDI) or AUDIO input against key
profiles; positive = major-leaning, negative = minor-leaning. Best configuration: the "Simple"
profile (Sapp 2011), cosine similarity, 3-second non-overlapping windows; audio chroma via
constant-Q transform.

## Experiments and numbers

Ground truth: five expert theorists rating 72 preludes (Bach WTC I, Chopin Op. 28, Shostakovich
Op. 34; first 8 bars) on a 1–7 entirely-minor…entirely-major scale; inter-rater r = .90
(Bach .89, Chopin .95, Shostakovich .84).

- Experiment 1 (MIDI, n=72): model-vs-expert r = .835 overall (Bach .832, Chopin .868,
  Shostakovich .791); best single profiles ~.84–.85.
- Experiment 2 (audio, n=72 recordings, 1934–2020): r = .859 (Bach .839, Chopin .915,
  Shostakovich .799); symbolic-vs-audio mean correlation difference only ≈ −.01 to −.02.
- Experiment 3 (audio, n=1,008 recordings): r = .820 [95% CI .628–.919]; 70–74% of expert
  variance; the MIR-toolbox categorical mode function manages r = .474 on the same task.

## Positions (as quoted)

For the continuum: "some minor key passages end on major chords; some major passages 'borrow'
harmonies from parallel minor keys"; Schoenberg cited treating Lydian/Mixolydian as major-like
and Dorian/Phrygian as minor-like; conclusion: "a more granular approach to classification
beyond the traditional binary of major/minor could prove useful", mode as a "super cue" for
emotion.

## Limits (as stated)

Three composers of Western classical repertoire; very short excerpts degrade it; 4% of
recordings fall outside the confidence intervals; no audio descriptor adds beyond the estimate.
