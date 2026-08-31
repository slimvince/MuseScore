# FETCHED CONTENT RECORD — Hu & Arthur 2021, "A Statistical Model for Melody Reduction" (Future Directions of Music Cognition, 2021; arXiv:2105.05385)

> **Retrieval record.** Population row 14 ("Hu & Arthur 2021"), identity settled 2026-08-30 at
> the author's laboratory page (exactly one Hu & Arthur 2021 publication: Tianxue Hu & Claire
> Arthur), fetched from `https://arxiv.org/pdf/2105.05385`. STRUCTURED CONTENT RECORD from one
> prompted extraction call over the whole text — a bounded, declared read (the standing
> environment bound in `reading_pass/additions.md`). Not central.

## Task and model

Melody reduction = identifying and removing NON-CHORD TONES from a monophonic melody (the
uppermost voice only), leaving a chord-tone skeleton. Framing: NCTs are "a commonly-cited
reason for the poor performance of automatic chord estimation (ACE) systems"; reduction as a
PREPROCESSING step for harmonic analysis.

Model: logistic regression, CT vs NCT per note. Features: duration, on/off-beat, arriving
interval (step/leap), departure interval (step/leap), and their interactions; forward stepwise
selection by AIC. Inputs at inference: surface features only (duration, metric position,
intervals) — NO harmony; the key and the Roman-numeral analysis are used only to DERIVE the
ground-truth CT/NCT labels ("labeled via a NCT identification algorithm given its scale degree,
associated RN, and the key").

## Data and results

Corpus: TAVERN (27 Mozart/Beethoven theme-and-variation sets, 281 movements): themes subset
2,039 notes (81% CT / 19% NCT); full 45,299 notes (~72/28). Validation: 6 Haydn "Sun" quartets,
12,616 notes.

Results: Model 1 (trained full TAVERN) accuracy 75.34%, AUC 0.79, vs all-CT baseline 70.30%.
Model 2 (themes-trained) 75.39%, AUC 0.78. Ten-fold on themes: accuracy 84.87%, precision
0.8756, recall 0.9508, F1 0.9116, AUC 0.8747. Generalization: TAVERN full 76.4% (baseline
71.2%), Haydn 70.6% (baseline 66.0%, AUC 0.6852) — margins over the trivial all-chord-tone
baseline of ~4–5 points.

## Scope, limits, positions (as stated)

Class imbalance biases toward CT; the ground truth "is far from an objective process"; melody
operationalization oversimplified, context beyond n=2 unused. Style dependence stated: chorale
styles are mostly chord tones and prior NCT work does well there, while "on non-homorhythmic
and especially virtuosic styles… model performances worsen"; variations carry far more NCTs
(passing, neighbouring, appoggiaturas). Future work: use as an ACE preprocessing stage —
"preliminary results indicate a modest improvement" (deep-learning polyphonic version in
progress at writing).
