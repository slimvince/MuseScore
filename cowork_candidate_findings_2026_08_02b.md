# Candidate findings — the second unattended probe pass (Cowork, 2026-08-02, while phase 1g runs)

> **STATUS: CANDIDATE FINDINGS — NOT YET ROWS.** Two read-only probe agents ran while the phase-1g
> triage held the register surface; nothing here touched the register, any specification, or any
> file CC owns. Rowing and register corrections happen AFTER the triage lands and is verified, in
> one deliberate pass. Establishment status: agent-run apparatus, each probe self-established
> against the committed parity reference (12/12) with predictions registered before measuring;
> artifacts committed-side under `tools/joint_estimator/invariance_probes_2026_08_02/` and
> `tools/joint_estimator/applied_chord_stake_2026_08_02/` (untracked until the rowing commit).

## A. The invariance probes (perspective-inventory channel 3, second wave)

**A-1. The emission is NOTE-COUNT-weighted, and octave doubling therefore moves committed
readings — a model property by trained design, now measured.** Determined at the source before
running: the emission adds one term per note record, and the fitted table was counted the same
way (`probe_decoder.py:747-753`; `gen_note_tables.py:385-410`) — fit and decode are CONSISTENT,
so this is not the OI-228 class (no fit/decode mismatch). Measured: doubling ONE upper voice an
octave up (pitch classes, bass, and event lattice all unchanged) moved the committed reading on
13.2 % of segments (354/408 survived), re-cut boundary structure on 9 of 12 pieces (the
registered surprise — the prediction said ≥9 would be stable), and lowered every total score.
Violation classes diagnosed with measured factor deltas: quality inflation (a doubled seventh
turns V into V7 — margin +0.48→+0.96 at bwv2.6@5760), a key relabel driven purely by the
SPELLING factor (bwv153.1@18000: E major→A minor with emission deltas identical), and wholesale
re-segmentation. **Why it matters:** a pure octave doubling is the same harmony by construction;
13 % committed-reading movement from it is a robustness/consistency fact that bears on the
family design (WHAT the emission counts — notes, pitch classes, or sounding tones — is exactly
the input-representation question OI-228/OI-243/OI-246 circle) and on orchestral repertoire,
where doubling is the norm (OI-209). A pc-level or sounding-level emission would be a
refit-requiring model change — a phase-3 design input, never a knob-turn. **Disposition: NEW ROW
(family-design input; the third face of the what-does-the-emission-read family).**

**A-2. Note-order permutation: the committed surface is order-independent — 36/36 identical.**
An establishment POSITIVE worth recording (the §5 tie-break never fell through to input order).
Residual caveat: total scores wobble at ~1e-14 (floating-point summation order); any future gate
comparing scores at exact equality would flake; the existing 1e-6 tolerance is safe.
**Disposition: INVENTORY (a one-line establishment note where the parity checks are documented;
the ulp caveat recorded beside the tolerance).**

## B. The applied-chord stake (the OI-267 measurement) — with a premise correction

**B-1. ★ The premise of D-248/OI-267 is PARTLY FALSE at HEAD: the production joint renderer DOES
emit applied-chord labels.** `jointrender.h:62-63` renders the "/target" suffix; the committed
corpus carries applied labels on 8.62 % of scored duration (`V/IV` 101,160 ticks, `V/V` 24,240…),
including 50,280 ticks of EXACT matches against applied ground truth (`viio7/V`→`viio7/V`).
D-248's verbatim concerns the LEGACY ChordFunction structure (no relative-root field) — a
different surface from the production decode. This also substantially answers OI-267's "OI-53
tension" question: the joint surface emits applied labels; the legacy structure does not carry
them. **Disposition: a REGISTER RECONCILIATION (post-triage): D-248's plain restatement and
provenance corrected to name its true (legacy) scope; dated notes on OI-267; no new row needed
beyond the correction.**

**B-2. The measured stake is SMALL — the scheduling input OI-267 asked for.** Applied-GT cells
carry 4.11 % of scored duration and 4.52 % of total Roman-numeral-disagreement duration; the hard
upper bound if every applied-GT disagreement vanished is **+1.62 points** on RN agreement
(64.12 → at most 65.74), and the pure right-chord-wrong-name slice is **+0.38 points**. The
OI-192 fifth-substitution overlap is weak both ways (applied-GT explains 4.12 % of the fifth
family; the fifth shape explains under a third of applied-GT root errors — the suspected
neighbour relation is refuted). All four registered prediction bands came in HIGH — the
measured reality is smaller than predicted. Establishment: driven through the committed
`a8_rebaseline_measure` substrate verbatim, reproducing the ratified baselines to the digit;
the applied-label test is the GT parser's own normalization. **Disposition: OI-267's answer —
the row's measurement half is DONE; the revisit enters the phase-3 plan at LOW priority with
these numbers, after the B-1 scope reconciliation.**

## What waits for the user's return

Rowing A-1, the A-2 inventory note, the B-1 register reconciliation and OI-267's dated note —
all after the phase-1g triage is verified (the register surface is CC's until then); then the
user's acceptance of the triage's exclusion list; then phase 1h continues the full reads.
