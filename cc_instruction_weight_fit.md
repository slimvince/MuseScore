# CC instruction — algorithm completion, step 2 of 2: the weight fit (the ratified staged fitting's second stage; OI-176/OI-177 BIND)

> **Both user rulings are IN (2026-07-19): ★R1 = W1 (the four-beat window), ★R2 = C1 (the cap
> amended to ≤ 14). This file is DISPATCHED.**
>
> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, **`cowork_prefit_gates.md` (the held-out and capacity
> protocols — they BIND this dispatch: this IS the fit event's weight stage)**,
> `cowork_joint_estimator_factorization.md` §2/§3 (the score form; the cadence-feature forms),
> the §5a staged-fitting decision in `cowork_joint_estimator_architecture.md`, and your step-1
> record (`c6ae08bd45`).
>
> **Current state:** branch `master`, HEAD `c6ae08bd45` (verify). One Cowork-authored uncommitted
> doc edit rides YOUR commit: `cowork_handoff.md`. **PYTHON-ONLY; instrument layer only; no
> `src/`, no build, no golden, no re-baseline. THE FIREWALL, precisely stated for a fit event:
> the training objective (the conditional likelihood below) is lawfully consulted by the
> optimizer on TRAINING folds; the GRADING metric is computed exactly once per held-out fold at
> the end and feeds NOTHING back; any other peek at any accuracy figure during fitting is
> forbidden and grep-proven absent.** Pinned instruments import-only. No adoption is proposed
> here (the OI-178 protocol is not in play); results return for user review.

**Dispatch author:** Cowork, 2026-07-19, at the user's direction — the last algorithmic stage
before the production build (the user's option-2 ruling).

## ★R1 — the tritone-pair approach window (user ruling required)

The cadence tritone-pair feature currently tests a single event; the published form it derives
from tests the LAST FOUR BEATS before the candidate cadence arrival. Options presented to the
user: W1 = the four-beat window (the established published form); W2 = keep single-event (our
undeclared simplification, measured under-firing); W3 = a fitted decay window (also published,
more parameters). **RULING: W1 (user, 2026-07-19)** — the window is the four beats strictly
before the boundary event, within the piece, voice-agnostic, and the feature definition (both
degrees sounding anywhere in the window) is stated on the artifact. Report the new fire count
beside the old 589.

## ★R2 — the weight-vector size against the ratified cap (user ruling required)

Enumerating the ratified score form's weights: 8 factor weights (prior, pitch emission incl. the
presence penalty, spelling, bass, chord transition, key transition + entry as one factor's
weight, boundary incl. the fermata cells, and the declared-mode strength) plus the FOUR cadence
feature weights (leading-tone resolution, tritone pair, dominant-tonic bass, fermata location —
the ratified factorization gives each feature its own fitted weight) = **12 or 13 depending on
the entry-table treatment — potentially exceeding the ratified "≤ 12" cap** in the capacity
protocol. Options presented to the user: C1 = amend the cap to ≤ 14 (a one-line protocol
amendment; capacity impact nil — tokens per parameter stays in the thousands); C2 = tie the four
cadence features to one shared cadence weight (stays under cap; loses per-feature calibration —
the features' relative strengths would be fixed at 1:1:1:1 with no basis). **RULING: C1 (user,
2026-07-19; the capacity-protocol cap is hereby amended ≤ 12 → ≤ 14 by ratification — Cowork
records the amendment on the gates document, riding this commit)** — state the final
weight-vector enumeration on the artifact.

## Task 1 — the training signal (ground-truth paths on the lattice)

Per piece: construct the ground-truth path — the GT segments mapped to event spans through the
established alignment, each with its (key, chord-class) state — under the SAME exclusions as the
counting (the interim misaligned-span leave-out; the flagged pieces excluded entirely from
training; anacrusis-measure labels dropped). A GT label absent from the decoder vocabulary maps
per the fitted normalization; report any unmappable remainder. **Establishment:** the GT path's
score is computable for every training piece (no minus-infinity terms — the below-threshold rule
guarantees this; verify and report the count of GT transitions that route through leftover mass);
show 3 pieces' path construction in the report.

## Task 2 — the objective and the fit

The ratified convex fit: maximize the sum over training pieces of
log P(GT path | piece; w) — the semi-Markov conditional-likelihood objective where each factor's
log-probability (from the FROZEN tables) and each cadence feature is a feature function and w is
the weight vector — with an L2 penalty, its strength chosen by inner cross-validation WITHIN
training folds only. Per the ratified held-out protocol: fit on each of the 5 training-fold
complements; evaluate each held-out fold exactly once; pool. Also fit the all-326 publishable
variant, reported beside the CV headline, never in its place. **The identity-weight decode runs
through the same grading as the mandated ablation arm.** Convexity means the optimizer's
convergence is checkable — report the convergence evidence (objective monotonicity, gradient
norm at stop).

## Task 3 — measurement, against these written predictions (Cowork, #17b)

Grade the fitted-weight decode per held-out fold on the robust unit; pooled CV figures with
piece-level bootstrap 95 % confidence intervals; beside them: the identity-weight arm and the
committed current-system baselines. **Predictions (fitted weights versus the identity-weight
probe's 74.43 / 53.67 / 72.97 / 59.50):** key-local 77–85 (UP); key-home 62–75 (UP
substantially — the cadence factor targets exactly the relative-major/minor confusion the probe
diagnosed); root 72–78 (stable to up); Roman numeral 60–68 (UP). A result outside a band is a
prominently-reported finding with named-piece diagnosis — this is a fit event, not an
explorational run: nothing proceeds on top of an unexplained band miss until the user reviews.
Also report: the fitted weight values themselves with plain-language interpretation (which
evidence types the fit strengthened or discounted, and the cadence features' fitted strengths);
the three sensitive cases (the bwv352 pair, the bwv10.7 merge-versus-split, the deceptive
cadence) re-decoded under fitted weights; the prune-cost re-measured on the 12-piece sample
(weights may change what pruning loses); decode timings.

## Commit

**One commit:** `tools: the weight fit — semi-CRF conditional likelihood under the ratified gates; cadence features weighted; CV headline + identity ablation` —
the fit code, the fitted-weight artifacts (per fold + all-326, provenance-stamped, the final
weight enumeration and the ★R1/★R2 rulings recorded on them), the re-decode and grading
artifacts, this file (force-add), the riding Cowork doc edit. Push **origin only**.

## Self-check before reporting (standing rule)

Diff scope proven; pinned instruments untouched; the firewall as stated above grep-proven; the
held-out discipline auditable from the artifacts (fold provenance on every figure); all figures
generated. **Report:** the CV headline table with confidence intervals (fitted vs identity vs
current baselines); the weight values and their reading; the establishment items; the sensitive
cases; the prediction verdicts; reuse-versus-new; anomalies — a surprise at a fit event is a
STOP-for-review, reported, never built around.
