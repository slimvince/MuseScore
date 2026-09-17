# CC Instruction — BUILD the standing oracle-root metric (TIERED) + regen the stale Baroque corpus

> Metric-first is validated and decomposed (`cc_metric_dossier`, `round2/3`, `decomposition` reports;
> Cowork-reconciled). The decomposition proved the per-event charged error is a **three-way co-dominant split**
> (hard-key ~10–25%, tonicization ~30%, segmentation over-grab ~32–45%) with chord-ID negligible (~2–3%), and
> that the verdict is **definition-sensitive** — so the standing gate must **report the decomposition tiers
> SEPARATELY** (no premature collapse) or it will steer effort onto convention boundaries. **This is the BUILD
> step** (first committed tooling in the metric arc). **It is MEASUREMENT only — no production/analyzer/scoring/
> threshold change.** Commit locally; Cowork verifies at the committed object; user ratifies the standing
> baseline. North star: best = CORRECT vs the DCML/music21 oracle.

## §0 — Scope (measurement tool + corpus hygiene; NOT a behavior change)
- **IN:** a standing oracle-root metric tool (per-event, policy A, tiered) + regenerating the stale
  `tools/corpus/baroque/` from HEAD. No production code, no scoring term, no gate threshold, no `chordanalyzer`
  touch. The tool only *reads* corpora and *emits* case-identity sets — like `characterise_bir_false`.
- **OUT (deferred, separate steps):** the CLAUDE.md gate-policy rewrite (oracle-root primary / BIR secondary),
  the off-chorale genre-balanced builds, and any K1/K3/segmentation inference work. Do NOT start them here.

## §1 — The tool (fine-grained, tiered)
Build it as a sibling tool or a `--oracle-root` mode (your call — reuse `characterise_bir_false`'s
`validate_corpus_dir` + `compare_analyses` + `dcml_parser` verbatim; do not fork them). Per preset
(Baroque/Jazz/Default), over the per-event oracle grid (round-3 semantics: one event per DCML annotation at its
own tick; our per-region roots expanded onto it), emit **case-identity sets (stem@tick)** for each tier:

1. **CHARGED total** = `three_way_classify == music21_dcml_agree` (bass-decoupled, pc-typed). Then decompose
   each charged event into exactly one of:
   - **KEY-HARD** — our key ≠ **both** oracles (DCML-local AND music21) → genuine key-detection error.
   - **KEY-TONICIZATION** — our key ≠ DCML-local but **= music21-global** (the local-vs-global grain) → the K3
     labeling band; report it **separately** (it is partly convention — never silently folded into KEY-HARD).
   - **OVER-GRAB** — key matches the oracle, but our single region spans **≥2 distinct oracle roots** →
     segmentation under-grab.
   - **CHORD-ID** — key matches, region aligns 1:1, our root still wrong → vertical/competition miss.
   - **AMBIGUOUS** — cannot be cleanly bucketed; report its size, do not force.
2. **FLOOR** = `all_differ` where DCML ≠ music21 (the genuine same-event oracle dispute / symmetric-dim7). Report
   separately; **never summed** into charged.

Report per preset: the CHARGED total, the 5 charged sub-tier counts + %, and the FLOOR count. Manifest-validate
every corpus dir (the anti-contamination guard) exactly as `characterise_bir_false` does.

## §2 — Acceptance: TWO distinct checks (tool-validation vs standing baseline)
**Separate "is the tool correct" from "what is the standing number."** The tool reproduced the read-only
reports on the corpora *those reports used* — that validates the TOOL and is done. But the standing baseline is
measured on the **canonical plain corpora** (§3), where Baroque RE-STATES.

1. **Tool-validation (done — confirm only):** on the report corpora, reproduce Round-3 charged/floor
   (Baroque-as-measured 3862/4287; Jazz 4065/4276; Default 3894/4285) and the decomposition split. This proves
   the tool's logic; it is NOT the standing baseline.
2. **★ Standing baseline (the real deliverable):** measured on the **plain/canonical** `tools/corpus/{baroque,
   jazz,default}` (§3). **Baroque RE-STATES off the non-canonical `baroque_kma_abs`** (which carried a
   non-default key-modulation / joint-key key reading — Gmin↔Bbmaj oscillation — while matching HEAD on the
   chord, so it passed the BIR/chord litmus but was NOT plain HEAD). On plain HEAD: Baroque **KEY ≈ 46.8%**, not
   54.9%; **re-run the full decomposition (all tiers) on plain Baroque** — the charged *set* shifts with the
   key, so OVER-GRAB / CHORD-ID / AMB also re-state, not just KEY. Jazz/Default already used the plain dirs →
   unchanged. **Report the standing baseline as the plain-corpora numbers; carry NO `kma_abs` Baroque figure
   forward.**
- Invariant that must hold on plain: **chord-ID stays near-ceiling (~2–3%)** and the 2 robust fixes (bwv14.5,
  bwv416) hold. If chord-ID moves materially on plain, STOP — something else is wrong.
If the tool's logic diverges from the read-only reports on the *same* corpus, STOP (tool bug). A Baroque
*number* change between `kma_abs` and plain is EXPECTED, not a bug — it is the corpus correction.

## §3 — Corpus hygiene + the standing-anchor decision (USER-RATIFIED: Option 1, plain-for-all)
**Ratified:** the standing oracle-root baseline is anchored on the **canonical, flag-OFF, `run_bach_preset`-
reproducible, manifest-stamped** `tools/corpus/{baroque,jazz,default}` — the same corpora the BIR gate uses.
**Not** `baroque_kma_abs` (a non-default key-modulation variant) and **not** kma-for-all. Reason: the standing
metric must measure **production**; anchoring on a non-production corpus to preserve a report number is papering
over. (`baroque/` was also stale anchor output, BIR 54 — the regen fixes both at once.)

- **Regenerate `tools/corpus/baroque/`** from HEAD via the standing `run_bach_preset.py` (manifest-stamped).
- **★ Identity check must verify KEY, not just chord/BIR.** Confirm the regen is plain HEAD on **both** axes:
  `characterise_bir_false` → **57** AND `bwv40.8 = Gm7` (chord), **AND the key reads stable Gmin (NOT the
  Gmin↔Bbmaj oscillation of `kma_abs`)**. The whole `kma_abs` trap was that it matched HEAD on chord/BIR while
  differing on KEY — so chord-only identity is insufficient. A standing corpus is the manifest-validated
  `run_bach_preset` output, never a legacy/hand-made dir.
- Jazz/Default already match CLAUDE.md (plain) — leave them.
- Then compute the §2(2) standing baseline (incl. the **re-run Baroque decomposition on plain**) on these dirs.

## §4 — Workflow + deliver
- **Commit LOCALLY (unpushed).** The tool + any helper, plus the regenerated `baroque/` manifest (if corpora
  are tracked; if gitignored, just report the regen). Write `cc_metric_build_report.md`: the tool's design, the
  acceptance results (all tiers vs the read-only numbers), the corpus-regen confirmation, and the per-preset
  standing tiered baseline.
- Cowork verifies at the committed object (the tool reuses the validated comparisons unchanged; the tiers
  reproduce the reports; no production/scoring file touched). User ratifies the standing baseline.
- **No push, no CLAUDE.md policy rewrite, no inference work** until the baseline is ratified (separate steps).

## §5 — Stop conditions
- The tool's tiers do NOT reproduce the read-only decomposition **on the same corpus** → STOP + report (tool
  bug). *(A Baroque number change between `kma_abs` and plain is EXPECTED — the corpus correction, not a bug.)*
- Building it would require touching `chordanalyzer`/scoring/a gate threshold → STOP (it must be read-and-emit
  only).
- The Baroque regen does not return to **57 AND `bwv40.8=Gm7` (chord) AND stable-Gmin (key)** → STOP (corpus or
  build problem; do not paper over). Chord-only match is INSUFFICIENT — the key axis must verify too.
- **chord-ID tier moves materially off near-ceiling (~2–3%) on the plain corpus** → STOP (the corpus correction
  should only move KEY/over-grab shares, not the chord ceiling).
- Any temptation to fold KEY-TONICIZATION into KEY-HARD, charged into floor, or to carry a `kma_abs` Baroque
  number forward as the standing baseline → STOP (the separation + the canonical-corpus rule are the whole point).
