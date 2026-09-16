# CC Instruction: Coordinated metric re-baseline — fix P0/P1/P2/P4/P5 (tools-only)

## Context + decision

The pipeline audit (`cc_measurement_pipeline_audit.md`) found five measurement defects.
**Decision (user 2026-06-13): fix the TOOLS-side measurement corruption now as ONE
coordinated re-baseline; P3 (engraving mode-drop, key-axis) rides separately with the
held Stage-4 work.** This run fixes **P0, P1, P2, P4, P5 — all in `tools/`** (parser,
alignment, reporting). **NO production/engraving change. P3 is OUT of scope.**

This is a **deliberate metric re-baseline** (like the Stage-1d F-1/F-2 corrections, larger):
it changes ground-truth parsing + alignment, the metric tests re-pin, and the cross-corpus
precision numbers WILL move — that is the point. Base `a4ae4a9203`+. Method A–H;
**HELD = `git add` ok, commit NOT until approval** (the re-baseline commit needs Cowork
sign-off because it moves every headline number). Never-guess; the music21 `RomanNumeral`
oracle and the TSV-vs-rntxt equivalence are the correctness checks.

## The fixes (audit §4 order)

**Step 1 — P0 fractional-onset (the dominant lever).** In `dcml_parser.parse_abc_harmonies_file`
(and anywhere `mn_onset`/`quarterbeats` is parsed): parse with `fractions.Fraction`, NEVER
`float` — keep ALL annotations (the 58.9% currently dropped). **Align by absolute tick =
`round(Fraction(quarterbeats) * 480)`** (audit L4.1 verified this exact + pickup-aware on
18 pieces), not the measure-anchor reconstruction. Narrow the bare `except (ValueError,
KeyError): continue` so it can't silently swallow a legitimate-but-unhandled row again
(log/count anything it still skips — no silent drops).

**Step 2 — P1 rntxt applied + P2 minor-LT/vio (root correctness).**
- P1: in `parse_rntxt_file`, resolve the `/X` applied target BEFORE rooting (port the TSV
  `_resolve_effective_dcml_key` path — do NOT touch the TSV applied path, it's correct).
- P2: fix the natural-minor degree table so raised `viio`/`vio` root at +11/+9 (leading
  tone / raised submediant), on BOTH paths and inside tonicized `#viio/X`.
- **Root-source choice (your call, justify):** port the deterministic resolution
  (Fraction + relativeroot + raised-7) — PREFERRED, keeps the metric self-contained, no
  music21 runtime dep — vs rooting via music21 `RomanNumeral`. Whichever you pick,
  **verify the corrected roots against the music21 `RomanNumeral` oracle** on a sample
  (it's the audit's true-root oracle); report the agreement rate (target ~100% on
  well-formed figures).

**Step 3 — P4 ABC/Beethoven structural offset (must be handled IN this batch, per the
user's choice).** The naive `quarterbeats` correction makes beethoven +3.6pp worse
(audit L4.3) because GT qb runs ~4 bars ahead of our ticks on repeat-bearing ABC. Anchor
GT to OURS by matched downbeats (not raw qb) on the affected movements. **If you cannot
cleanly resolve P4 for a given ABC movement, QUARANTINE that movement's number** (exclude
+ report "P4-affected, not corrected") rather than ship a wrong correction — do NOT let
beethoven regress. First pin P4's scope (audit §6.1: per-movement qb-span-end vs our
`max(endTick)` bisection) so you know which movements need anchoring vs quarantine.

**Step 4 — P5 reporting hygiene.** Surface the coverage denominator honestly (post-fix =
full annotation set, ~×2.4 the old downbeat-only count); refresh the stale 53.8%/54.4%
headline to the post-fix number; repoint `rerun_dcml_comparison.py` defaults to a
HEAD-aware path and **fail loudly if the corpus `git_hash ≠ HEAD`** (close the
accidental-stale-measurement trap L1.2).

## Re-pin (deliberate metric re-baseline)

Update `tools/tests/test_metric_scripts.py` + `test_metric_primitives_l0l1.py` to the
CORRECTED behavior, each marked `# re-pinned 2026-06-13: metric re-baseline (audit
P0/P1/P2/P4 — was downbeat-drop/applied/minor-LT-corrupt)`. Add: a fractional-onset test
(a `"1/2"` row is KEPT, not dropped), the rntxt-vs-TSV applied-root equivalence test, a
minor-LT root test (`viio` in minor → +11), the quarterbeats-alignment exactness test.
Non-affected tests stay green unchanged.

## Verification — the re-baseline is documented, not just green

1. Python suite green (re-pins listed). The music21-oracle agreement rate (Step 2).
2. **The re-baseline table** — before/after for every cross-corpus figure (per-DCML
   root_agree, per-ours, rn_agree, GT volume / coverage ×2.4), per-corpus, with P4's
   beethoven either corrected or quarantined (state which).
3. **The corrected headroom HEADLINE** (cheap once the parser's fixed — re-run the
   headroom probe): the real `root_err` vs the parser-artifact share (the dossier's "366
   phantom" + the minor-LT mass), i.e. **how inflated "95% functional / 4.8% vertical"
   actually was**. (The full functional-residual RE-decomposition + OQ-1 re-derivation is
   a SEPARATE follow-on on the corrected metric — not this run.)
4. **BIR 13/7 gate UNCHANGED** — re-run `characterise_bir_false --corpus-dir
   tools/corpus/{baroque,jazz}` → expect 13/7 exact (the insulation regression check). If
   it MOVES, the insulation hypothesis was wrong — STOP and report (a major finding).
5. No production/engraving file touched (`git diff --stat` = tools/ only).

## Commit — HELD for Cowork (the re-baseline needs sign-off)

ONE commit, tools/ only. Message documents the number movement (the re-baseline table) +
the four defects fixed + "BIR 13/7 unchanged; P3 deferred to Stage 4." Propose; do not
commit until approved.

## Report — `cc_metric_rebaseline_report.md`

§1 each fix (approach + the root-source choice justified); §2 the re-baseline table
(before/after, per-corpus, P4 disposition); §3 the corrected headroom headline (real vs
artifact root_err); §4 the re-pin ledger; §5 BIR-unchanged confirmation; §6
deviations/unknowns. Every number [probe]; the corrected roots [oracle-verified].

Stop conditions: the BIR 13/7 gate MOVING (insulation wrong — report); P4 unresolvable
on an ABC movement (quarantine + report, don't ship a worse number); the corrected roots
NOT matching the music21 oracle (the fix is wrong — report); any need to touch
production/engraving (that's P3/Stage-4, out of scope — stop). Do not re-derive OQ-1 in
this run — the corrected metric is the prerequisite; the OQ-1 re-decomposition follows.
