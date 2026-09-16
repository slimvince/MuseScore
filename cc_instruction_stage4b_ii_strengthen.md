# CC Instruction: Stage 4b-ii — strengthen note-based relative-pair inference (structural-sufficiency test)

## Authorization + framing

Implements `docs/stage4b_design.md` §5 (4b-ii), data-driven from the 4b-i floor. Base: the committed
4b-i. **All work is in the composing autonomous zone** (`src/composing/analysis/key/keymodeanalyzer.{h,cpp}`)
+ `tools/` (measurement). **No `src/notation`/`src/engraving` PRODUCTION edit** — only test re-pins /
snapshot-golden refreshes, DCML-verified, if a winner genuinely moves. HELD — no commit.

**The load-bearing question this run answers** (not just "make the number better"): **can the EXISTING
note-based structure, with better weights, carry the relative-major/minor decision — or is a new
mechanism needed?** 4b-i proved the declared mode was a near-total relative-pair crutch (mode-absent
floor ~3× worse). 4b-ii tests whether the hand-built terms can close that gap. The answer feeds **both**
the OQ6 pass-bar AND the A-vs-B question (if the existing structure can't close it even well-weighted,
that is evidence the key-axis emission needs a richer/learned model — a Stage-5/6 finding, reported, not
acted on here).

**Overfitting guard (mandatory):** the final weights are **Stage 5's fit**. Do **NOT** hand-tune weights
to minimize the corpus number. Use **principled, provisional** bumps and report the *direction and
magnitude* of floor movement + which cases recover, so we learn structural sufficiency. A weight set that
only works by fitting the 326-chorale gate is a Stage-5 artifact, not a 4b-ii result — flag it if you see it.

## The terms to strengthen (the relative-pair discriminators) [code]

From the 4b-i report §7 + scoping dossier §2 — the terms that actually separate relative pairs (C major
vs A minor share the diatonic set, so scale membership and the mode prior are near-symmetric and are NOT
the lever):

1. **`applyPairwiseDisambiguation`** (`keymodeanalyzer.cpp:581-607`; weights `disambiguationTriadBonus
   4.50` / `Cost 1.50` / `TonicBonus 1.00`, `keymodeanalyzer.h:305-307`) — the **strongest existing
   relative-pair discriminator** and the most promising lever. It already targets the top-2 same-signature
   modes (the exact decision boundary).
2. **Tonic / triad salience** (`scoreTriadEvidence`: `tonicWeight 1.60`, `completeTriadBonus 2.50`,
   `missingTonicPenalty −2.50`) — what distinguishes which of the relative pair is tonic.
3. **True leading tone** (`trueLeadingToneBoost 1.20`) — directional tonic indicator (harmonic-minor i vs
   its relative); relevant to the bwv371/437/276 tonic-correct/flavor-wrong cases.

Read each at source before changing; quote file:line in the report. Cadence→key wiring (OQ4) stays
**deferred** — only flag it if 1–3 demonstrably cannot close the gap.

## Method

1. Strengthen the discriminators with principled provisional bumps (explore which term(s) move the
   floor; document the rationale for each — e.g. "pairwise tonic-bonus raised because the relative
   decision hinges on tonic salience, not magnitude-fitted").
2. Measure **mode-present AND mode-absent**, all three presets, on the corrected DCML-only
   granularity-robust **L1 `--key-breakdown`** (the `a96f179f40` instrument). Report:
   - **Mode-absent floor movement** (the headline): Default/Baroque S2 vs the 4b-i floor (2070 / 2099).
     How much of the ~1383-region gap closes? (Jazz key S2 is unreliable — 39–46% label-parse failures;
     treat Baroque/Default as load-bearing, as in 4b-i.)
   - **Mode-present** must NOT regress: the BIR gate (chord axis) stays ~57/23/57 — **an un-adjudicated
     BIR=false increase on any preset is a hard stop**; DCML-adjudicate every moved gate case. Report
     mode-present S2 too (it should stay ≈ the 4b-i +2 / 0, not worsen).
   - **Case-level:** bwv365/bwv33.6 (should recover — the relative IS note-distinguishable per 4b-i);
     bwv371/bwv437/bwv276 (tonic-correct, flavor — does the church-mode flavor improve?); **bwv64.2 /
     bwv83.5** (the hard class — note inference reads a *different* key; if these stay wrong, say so —
     they are NOT relative-pair ties and likely need Stage-5/6 / richer emission).
3. **Snapshots:** refresh only DCML-verified-correct diffs (report each).
4. Suites green (composing/notation/snapshots).

## Deliverable — `cc_stage4b_ii_report.md`

- The provisional weight changes (with per-term rationale, every weight `[empirical — Stage-5 fits]`).
- The both-conditions measurement (floor movement + mode-present non-regression + per-case).
- **The structural-sufficiency verdict** (the point of the run): does the existing structure close the
  gap, and by how much? What residual is genuinely unreachable by these terms (→ Stage-5/6 / A-vs-B
  evidence)? This is the input to the OQ6 mode-absent pass-bar (which the user sets against these numbers).
- A first-pass read of whether Stage 5 fitting could plausibly take it further (structure sufficient,
  weights just need fitting) vs. a structural ceiling (a new term/mechanism or learned emission needed).

Every number `[probe]`, every root `[oracle]`. HELD — no commit; propose the commit shape in the report.

## Stop conditions
- Strengthening that closes the mode-absent floor but **wrecks mode-present** (the gate or mode-present S2
  regresses materially) — that is a **trade-off finding** (the structure can't separate relatives without
  collateral damage = insufficient); report it, do not push through it.
- An un-adjudicated BIR=false increase on any preset, mode-present (ratification hard stop).
- Any `src/notation`/`src/engraving` PRODUCTION edit appearing necessary (surface for authorization).
- Catching yourself corpus-fitting the weights to the 326-chorale gate (overfitting guard) — stop and
  report the provisional set + the sufficiency finding instead.
- The hard-class cases (bwv64.2/bwv83.5) needing a wholly new mechanism — report as an A-vs-B / Stage-5/6
  finding; do NOT build a new term in this run.
