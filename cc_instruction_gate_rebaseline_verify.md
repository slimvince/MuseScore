# CC Instruction: Verify the 57/23 gate re-baseline before ratification (read-only)

## Context + decision

Your metric re-baseline batch (`cc_metric_rebaseline_report.md`) is sound — the P0/P1/P2/P4
fixes are oracle-verified and Cowork confirmed the P2 source fix independently. The gate
moved 13→57 / 7→23 (strict superset). **User decision 2026-06-13: "Verify, then ratify."**
Before Cowork rewrites the CLAUDE.md/STATUS.md gate identities to 57/23, two things must be
nailed down. This run is **READ-ONLY analysis + a corpus regen at HEAD** — the metric-batch
fixes stay STAGED/HELD, no new commit, and **do NOT edit CLAUDE.md/STATUS.md** (Cowork does
that after this verifies). Never-guess; the music21 `RomanNumeral` oracle is the root check.

Two reasons this verification is needed: (1) your 57/23 came from a throwaway `/tmp` driver
(`gate_ids.py`), not the canonical `characterise_bir_false.py`, and against a corpus stamped
`a652dc1ba7` (3 commits behind HEAD); (2) your triage's "~10 actionable" rests on a
first-pass structural classification of the soft viio↔V7 bucket that you yourself flagged as
needing a hand-trace.

## Step 1 — Reproduce 57/23 through the CANONICAL tool at HEAD

- Regenerate BOTH per-preset corpora at HEAD (clean tree; the analyzer source is unchanged
  since the stamp — only docs + the byte-identical key-diagnostic `a4ea` + tools-metric
  `f8c6` — so the `.ours.json` should be identical, but regenerate to close the staleness):
  `run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque` and `--preset Jazz
  --output-dir tools/corpus/jazz` (both must come back 353/353, manifest stamped = HEAD).
- Run the **canonical `characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz}`**
  (NOT a throwaway driver) with the staged parser fixes active. Confirm: **Baroque 57,
  Jazz 23, strict superset** — explicitly verify all original 13 Baroque + 7 Jazz identities
  (the `stem@tick` sets in CLAUDE.md) are still present (0 lost). Report any deviation from
  57/23 as a finding (it would mean the throwaway driver and the canonical tool disagree).
- Redirect large output to a file and `head` it (CLAUDE.md bash rules); `; echo "exit:$?"`.

## Step 2 — Hand-trace the soft viio↔V7 bucket (firm up the actionable count)

The dim7-rotation cases (Δ ∈ {3,6,9}, diminished/half-dim quality) are structurally
unresolvable — a symmetric fully-diminished 7th is genuinely root-ambiguous by pitch class;
accept those as ambiguity without per-case tracing. **The viio↔V7 share-tone bucket (~29
Baroque + the Jazz ones) is the soft one — hand-trace each** with the audit's §3.A method:
open the actual pitch/tick content our analyzer saw + the WiR annotation, and classify each:
- **LEGITIMATE AMBIGUITY** — our reading is a defensible alternate root over the same/near
  pitch set (e.g. a dominant/incomplete reading sharing 3 of 4 tones with the leading-tone
  diminished), where pitch-class root agreement can't adjudicate; OR
- **GENUINE VERTICAL MISS** — the diminished chord is clearly present and we failed to
  identify it (the actionable target).
Verify each contested GT root against the music21 `RomanNumeral` oracle. Output the refined
genuine-vs-ambiguity split for the +44/+16 and the **firmed-up actionable count** (your
first pass said ~3 Baroque / ~1 Jazz new; confirm or correct it).

## Verification + report — `cc_gate_rebaseline_verify_report.md`

§1 the canonical-tool reproduction (57/23 confirmed at HEAD? strict-superset confirmed? any
driver-vs-canonical discrepancy?). §2 the hand-traced viio↔V7 split + the firmed actionable
count, each contested root oracle-tagged. §3 the net actionable error after re-baseline
(original + new), and an explicit recommendation: is 57/23 the right pin to enshrine, and
should the dim7-rotation cases be flagged as a structurally-unresolvable sub-class (the
seed of a possible two-tier gate / spelling-aware follow-on — note only, don't build it).
Every number [probe], every root [oracle].

## Constraints

READ-ONLY + corpus regen only. Metric-batch fixes stay STAGED/HELD — **no new commit**.
**Do NOT touch CLAUDE.md / STATUS.md** (the gate-identity rewrite is Cowork's, post-verify).
No production/engraving change (P3 still out). Stop conditions: the canonical tool does NOT
reproduce 57/23 (driver disagreement — report, do not paper over); the regen is not 353/353
(manifest guard); the hand-trace flips the actionable count materially (report — it changes
the ratification calculus). If a case can't be cleanly classified, mark it UNKNOWN, don't
guess.
