# CC Instruction: Stage 2.3 addendum — two approved items that missed the commit

## Context

D1 `18dc9e1829` + D2 `001b15df2d` are verified and accepted. Cowork's approval carried
two REQUIRED additions that did not reach you (relay gap — chat-relayed adjustments have
now been lost twice; henceforth all Cowork adjustments arrive as instruction files like
this one). Implement both in ONE small commit. Base: `001b15df2d`.

## Task 1 — Stale doc-comment (chordanalyzer.h:62)

The header comment block still says "the `templates` and `kDiagTemplates` TemplateDef
arrays in chordanalyzer.cpp" — `kDiagTemplates` was removed in D1. Fix the comment to
reflect the post-2.3 reality (one template array; diagnose replays production). Sweep
the WHOLE repo for other survivor references to `kDiagTemplates` and `contextualBonuses`
(comments and docs included — `grep -rn`, report hits; scoring_model.md was already
synced in D1, verify it has none).

## Task 2 — Context banner in the diagnose dump

`batch_analyze --diagnose-measures` replays the production pipeline with NULL temporal
context (region-in-isolation — correct, per the 2.3 scoping decision; threading the
real context is roadmap 2.3b). REQUIREMENT: every such dump must state this explicitly
so an rcb-class investigation can never mistake an isolated dump for an in-context
verdict (the historical trap 2.3 exists to close). Add a banner line at the top of each
diagnosed region's output, e.g.:

```
CONTEXT: NONE (isolated region — progression signals computed with null temporal
context; inter-region effects such as rootContinuityBonus feed are NOT represented.
For in-context diagnosis see roadmap 2.3b.)
```

If the diagnose path CAN receive a context in some invocation (survey — the unit-test
path passes one), make the banner conditional: print the actual context summary
(previousRootPc etc.) when present, the NONE banner when absent. Never print nothing.

## Verify + commit

Build; composing 501/501; batch_analyze regression script; one `--diagnose-measures`
smoke run showing the banner (paste 5 lines in your reply). Production byte-identity
unaffected (comment + diagnostic-output-only). ONE commit:
`fix: stage 2.3 addendum — stale kDiagTemplates comment + diagnose context banner`.
Commit directly (both items pre-approved); report hash + the grep sweep results inline.
