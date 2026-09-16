# CC Instruction — ANCHOR redesign: READ-ONLY proper-layer investigation

> The naive "recompute on raw tone union" hard-stopped correctly (`cc_anchor_recompute_report.md`): it
> over-reads non-chord tones (sus/add). The architecture diagnosis stands (a merged region's chord should be a
> function of its final tones), but the FIX's proper layer is undecided. **User-ratified: investigate the proper
> layer BEFORE any implementation — architecture/region-layer angle first, do NOT assume it's a scoring task.**
> **READ-ONLY: findings only, NO code/behavior/inference change.** North star: move root/chord output toward the
> DCML/music21 oracle. **★ Reminder: any eventual amendment must live in the PROPER architectural layer — this
> investigation decides which.**

## §0 — First: revert the experiment to a clean tree (then investigate read-only)
1. **Revert ONLY the anchor experiment:** `git checkout HEAD -- src/composing/analysis/region/regionanalyzer.cpp`
   (the report §1 confirms all anchor edits were confined to that one file). HEAD stays `dd418ecfed`.
2. **Confirm the held work is untouched:** `git status --short` must still show the **3 held B2 files**
   (`section/localmodulationdetector.cpp` + `.h` + `tools/batch_analyze.cpp`) and the pre-existing HELD docs —
   unstaged, unchanged. The revert touches `regionanalyzer.cpp` ONLY. If the revert would affect anything else,
   STOP.
3. The guard + bounded-settle machinery from the experiment is sound and fully documented in
   `cc_anchor_recompute_report.md` — it is recoverable; we are clearing the wrong-INPUT recompute, not the
   mechanism.

## §1 — The question: which LAYER owns the embellishment discrimination?
Production currently reads each short slice's chord embellishment-free. The merge flattens slices into one
region whose raw tone union includes suspensions/passing/neighbor tones; `analyzeChord` on that union (CC passed
`context=nullptr`) promotes them to chord members. **Determine, at source, which of the candidate fixes below is
the PROPER-LAYER fix — try the region-layer / architecture candidates (A,B,C) before conceding the scoring-layer
one (D).** This is the whole deliverable.

## §2 — Candidates to evaluate (read-only, at the committed object + the report's own data)

**A — Temporal context (architecture / region-layer; CC flagged this as "implicated").**
- Trace exactly **how `analyzeChord` uses `ChordTemporalContext`** to avoid over-reading embellishments: what
  signals (prev/next root, root-continuity, anything) and HOW. **The decisive sub-question:** does production
  discriminate embellishments *within a vertical via the temporal context*, or does it rely on the
  **segmentation** putting embellishments in *separate short slices* (so a single slice never contains the
  embellishment + the chord together)? If the latter, a flattened merged region **cannot** be rescued by
  temporal context alone — name that.
- What does a `ChordTemporalContext` contain, and **can a valid one be constructed for a merged region** from
  its neighbor regions? Would passing it (instead of `nullptr`) plausibly change the over-read? (Reason from the
  mechanism; you may not run code.)

**B — Duration / metric weighting (data-representation; possibly in-layer).**
- Does `ChordAnalysisTone` carry **duration / metric weight**, and does `analyzeChord` **weight tones by it**
  (so a short passing tone scores below a held chord tone)?
- Does `mergeChordAnalysisTones` **preserve per-tone durations** in the union, or collapse to presence? CC's
  recompute built a `pcPresenceMask` (presence only) — **did the recompute lose duration information the oracle
  needs?** If the oracle duration-weights and the union preserved durations, why did the held chord tones not
  dominate? Locate where the weighting would have applied. If preserving/using duration is the fix, that is an
  in-layer data-representation fix, NOT a new scoring term.

**C — Adopt-only-if-stronger (region-layer policy on the recompute output).**
- **Empirically test, from the report's own data (no build needed):** the 14 REMOVED (genuine fixes) vs the 11
  NEW (regressions). For each, classify the identity change: is the fix/regression a **ROOT or core-QUALITY
  change**, or a **same-root added-extension (sus/add/add9/add11)**? Hypothesis: the 14 fixes are root/quality
  corrections; the 11 regressions are same-root sus/add over-specs. **If that split is clean**, a region-layer
  policy — *adopt a recomputed identity only when it changes the root or core triad quality; reject a mere
  suspension/extension of the same root* — recovers the 14 and rejects the 11, with **no scoring-layer change**.
  Report the actual classification of all 25 cases.

**D — New scoring-layer discriminator (LAST resort, only if A+B+C are all insufficient).**
- If embellishment discrimination genuinely requires new oracle logic (duration-weighted tone filtering before
  analysis, etc.) that cannot be expressed as A/B/C, then it is a scoring task under the CLAUDE.md scoring-doc
  rules (template/bonus/guard ⇒ `docs/scoring_model.md` sync) — scope it, but do NOT treat it as the default.

## §3 — Deliver
`cc_anchor_redesign_dossier.md`: for A, B, C, D — the source evidence, whether it is the proper-layer fix, and
its layer. The **decisive verdict**: which candidate (or combination) is the recommended redesign, in which
layer, and why; the §2C 25-case classification table; the §2A within-vertical-vs-segmentation finding (it may
rule A in or out); and whether any in-layer fix (A/B/C) suffices or D is genuinely required. **READ-ONLY — HEAD
`dd418ecfed`, no code change.** Cowork reconciles at source; the user ratifies the layer + direction before any
implementation.

## §4 — Stop conditions
- Any code/behavior change beyond the §0 revert → STOP (investigation is read-only).
- The §0 revert would touch anything other than `regionanalyzer.cpp` → STOP.
- A candidate can't be cleanly resolved from source/data → say so; give what you found; do not force a verdict.
- Do NOT begin implementing any candidate — this produces the direction, the user ratifies it first.
