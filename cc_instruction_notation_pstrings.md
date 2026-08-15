# CC instruction — the presentation string formatters + the inference↔presentation boundary guard (seams-2 partition unit "P-strings")

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (now the lean INDEX — open
> `open_items/OI-<n>.md` detail files as needed), and the ratified
> `C:\s\MS\cowork_notation_output_contract.md` (note its NEW top amendment — "display
> renderings are PRESENTATION derivations" — which is one of this dispatch's riding Cowork
> edits and exactly what you are building).
>
> **What this is:** one unit of the notation-layer migration (the seams-2 partition; P0–P3a
> and the register split are DONE — see the handoff's 2026-07-26 blocks). This dispatch is
> that partition's "P-strings" unit AS ITS OWN INSTRUCTION — the older accumulated
> `cc_instruction_notation_seams_2.md` is now a REFERENCE document (its amendments 1–6 are the
> ratified rulings this instruction restates); do not execute from it.
>
> **Current state:** branch `master`; expected HEAD `1e32b5e92e` (the register-split commit,
> pushed) — verify via `git show --stat 1e32b5e92e` and that HEAD matches; mismatch = STOP.
> Riding Cowork edits (verify they are the only non-yours tracked diffs):
> `cowork_notation_output_contract.md` (the presentation-derivations amendment) and
> `cowork_handoff.md`. Commit them WITH your first commit. This dispatch file stays untracked.
>
> **Hard stops, always:** push origin only; ANY behavior change with the migration flag
> (`useJointNotationRecord`) OFF — byte-identity proven per commit (all three suites green, NO
> golden refresh); no legacy-analysis call on the record path; no inference edit anywhere (a
> musically-wrong-looking record output is diagnosed later at the dual-arm comparison, never
> patched); files outside the touchable set; a surprise is a STOP (#13). VS Code bash rules on
> every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-26. **The ruled context (user, 2026-07-26, both P3a
findings):** display strings are PRESENTATION derivations from published record facts — the
record publishes FACTS (degrees, classes, spellings as line-of-fifths/tpc, bass roles, keys)
and stays preset-independent; presentation renders idiom. Concretely: (1) NASHVILLE is a
presentation concern (every constituent verified derivable from published facts — degree +
accidental via the published root spelling, class quality incl. seventh-ness, bass
role/inversion, key; no exception class); (2) the display CHORD SYMBOL is ruling **D2** — the
record's grading-form string (`"GMaj"`/`"GDom7"`) stays (batch/a8 continuity), and the
idiomatic, spelling-aware display symbol ("G", "G7", "A♭m7") is a presentation derivation.

**Touchable set:** `src/notation/internal/**` (the record-path emitter sites),
`src/composing/analysis/section/**` (ONLY if the adapter's fact CARRIAGE needs completing —
see Task 1's hazard), the presentation formatter component (`chordsymbolformatter.*` and/or
one new shared presentation formatter unit beside it), the relevant test dirs + CMake lists,
`ARCHITECTURE.md`, `STATUS.md`, index+detail register files (row notes only), the two riding
Cowork files. **NOT touchable:** the joint module's inference/decode files (`jointdecoder`,
`jointtables`, `jointadapter`, `jointfactadapter`, `jointprimitives` — the boundary this very
dispatch guards), `tools/robust_stop/`, corpus, goldens.

---

## Task 1 — the display chord-symbol path (record arm), with the carriage-faithfulness establishment

1. ONE shared presentation-side path renders the display symbol from the record-derived
   `AnalyzedRegion`/`ChordAnalysisResult` facts — REUSE the existing `ChordSymbolFormatter`
   component where it is faithful (carried establishment, #19); do not write a second
   symbol formatter if the existing one serves (#6).
2. **The named hazard — prove the CARRIAGE, not the formatter:** the record→section adapter
   (`sectionrecordadapter.cpp`) maps the class quality through the coarse grading map
   (`Dom7`→Major-class etc.), which can drop seventh-ness/extensions on the way to display.
   Verify what the formatter needs (quality enum + extensions + bass/inversion + rootTpc) and
   complete the ADAPTER's carriage from the record's published facts (the class carries
   seventh-ness; the record carries member factor roles and spellings). Fix the carriage —
   never compensate inside the formatter, and never touch the grading-form string.
3. **Establishment (#19):** unit tests with independently-stated expectations across the
   vocabulary families — major/minor/dominant-seventh/half-diminished/diminished-seventh/
   augmented + applied classes + the chromatic classes; FLAT-KEY spelling cases proving the
   root comes from the record's published tpc (A♭ vs G♯ under the appropriate keys); an
   inversion/bass-slash case. The record-arm emitters (the P3a annotation emitter now; the
   later units' emitters when they land) write the DISPLAY form.

## Task 2 — the shared Nashville formatter (record arm)

1. ONE shared presentation-side Nashville formatter consuming record facts (degree +
   accidental from the published root spelling relative to key, quality suffix incl.
   seventh-ness, bass-degree slash from the bass factor role). Document the derivation and the
   convention chosen for applied/chromatic classes (a presentation convention — pick the one
   the LEGACY Nashville formatter uses, cite its code, so continuity is testable).
2. **Establishment:** derivation documented; unit tests with hand-derived expectations;
   continuity vs the legacy Nashville formatter on readings where both arms agree (same root,
   quality, key — assert identical output there; differences elsewhere are the known
   inference-driven class, not formatter divergence).
3. Wire the record-arm emitter site(s) that previously wrote nothing for Nashville (the P3a
   emitter's declared gap closes; update its golden-less snapshot test accordingly).

## Task 3 — the permanent inference↔presentation boundary guard (user directive)

A mechanical dependency-direction TEST (the include-closure pattern the joint module build
established), failing on violation, both directions: (a) the joint module's inference files
include/reference NO presentation formatter, styling, preset-symbol, or display-string code;
(b) the presentation formatters (`chordsymbolformatter` + the new Nashville unit) include NO
inference internals — they consume only the published record/adapter output surface. Document
in the test what "inference files" and "presentation files" enumerate (a maintained list is
acceptable; a glob is better). This is a permanent suite member, not a one-off check.

## Task 4 — doc sync + closing

`ARCHITECTURE.md` (the presentation-derivation boundary as-built: what renders where, the
guard); `STATUS.md` closing entry (figures from your artifacts); a dated note on the OI-182
detail file if any presentation-constant site moved (row untouched otherwise). Commits per
change-class (suggested: Task 1, Task 2, Task 3+4 — each with the three suites green and NO
golden refresh); the riding Cowork files on the first commit; push origin.

## Report

Hashes; the carriage-faithfulness result (what was missing, what now carries it, the tests);
the flat-key spelling evidence; the Nashville continuity result (count of coinciding readings
asserted identical); the boundary guard's file enumeration + a demonstrated failure (perturb a
scratch include to prove the guard fires — the negative-control discipline); suite totals per
commit; reuse-vs-new / what-retires (expected: `ChordSymbolFormatter` reused; nothing retires
here); anomalies (a surprise is a STOP). Standing self-check before reporting: re-read every
commit's actual diff against the principles and `DEFECT_TYPES.md`.

**After this unit (each as its own fresh instruction, Cowork-written):** P4 implode+tuning
(the exposure-bucket unification + the OI-182 execution), the merged note-seam unit, P6 (the
dual-arm classified comparison — the switch-ratification evidence), P7 (doc sync/close).
