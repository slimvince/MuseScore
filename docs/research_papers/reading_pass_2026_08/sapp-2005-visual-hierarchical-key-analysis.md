# FETCHED CONTENT RECORD — Sapp 2005, "Visual Hierarchical Key Analysis" (keyscapes; Computers in Entertainment 3(4))

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the author's open copy
> `https://ccrma.stanford.edu/~craig/papers/05/p3d-sapp.pdf`. STRUCTURED CONTENT RECORD from one
> prompted extraction call over the whole text — a bounded, declared read. Population row 17
> (R-7 alternative: a tonality estimated at every window size at once); CENTRAL — second
> independent pass owed.

## The keyscape

A two-dimensional picture of thousands of simultaneous key analyses: horizontal axis time,
vertical axis ANALYSIS WINDOW SIZE from one beat to the whole piece; per window size a sliding
window's key result is plotted at the window's centre — a triangular domain. Key-finding inside
each window: Krumhansl-Schmuckler correlation with Krumhansl probe-tone weights, or Aarden's
score-derived profiles, or root-finding; correlation r-values normalized. Colours: circle of
fifths → rainbow; major bright, minor dark. Linear or logarithmic window-size scaling (the
logarithmic called the "more perceptually accurate view").

Hierarchy reading, as quoted: "The bottom of the plots represent small-scale key features…
similar to the foreground in a landscape painting. The top… represents large-scale key… similar
to the background." Stable single-colour regions read as more certain; colour-shifting regions
as less certain / modulation boundaries.

## The multi-resolution claim (as quoted)

The single-window "Goldilocks problem": "If too much music is analyzed at once, fewer important
keys are suppressed; if too little music is analyzed at once, the chordal structure of the music
is really being analyzed instead of the key structure." Worked failure: a Schubert variation
analyzed whole gives A major r = 0.86 over F♯ minor r = 0.78, hiding a two-key structure a split
analysis reveals. Keyscapes claimed to display harmonic structure hierarchically, likened to
Lerdahl & Jackendoff tree reductions.

## Evaluation

**No systematic accuracy measurement** — qualitative validation against theory expectations:
Mozart Divertimento key sequence C[15 bars]–G[13]–d[4]–F[7]–C[24] rendered correctly; Barber
Adagio tonic chord only 19/564 quarter-note units (3.3%) with subdominant and dominant each
about three times more frequent (a tonic-scarcity case in the C36 direction); profile
comparison — Krumhansl weights over-emphasize the dominant key at the subdominant's expense,
Aarden's the reverse; Bach BWV 1007: Krumhansl-profile whole-piece key WRONG (D major), Aarden
right (G major). No error rates, no corpus statistics, no runtime analysis.

## Scope and limits (as stated)

Western art music examples only; the histogram-correlation key finder is order-insensitive ("as
if all the notes were played at once in a single large chord") with order-sensitive methods
(Temperley 2002) named as future work; colour mapping arbitrary; atonal works produce
deliberately fragmentary keyscapes.
