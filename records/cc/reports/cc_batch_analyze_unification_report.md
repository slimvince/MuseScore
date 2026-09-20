# `batch_analyze` test-path unification audit (Step 2 / ledger F17)

**Read-only code audit. No source edits.** Scope: confirm that `batch_analyze`'s
**corpus-characterisation path** (the `.ours.json` that feeds the two-tier BIR gate via
`characterise_bir_false.py`) **is the production analysis path**, not a duplicate/parallel
analyzer.

- **Audited at:** HEAD = `ba7ed3d857b575968bf8fcb9f6a423446d09e5ad` (the §0 doc commit, below).
- **Files traced:** `tools/batch_analyze.cpp`, `tools/run_bach_preset.py`,
  `src/composing/analysis/region/regionanalyzer.{h,cpp}`,
  `src/notation/internal/notationharmonicrhythmbridge.cpp`,
  `src/notation/internal/notationcomposingbridge.cpp`,
  `src/notation/internal/notationcomposingbridgehelpers.cpp`,
  `src/notation/internal/notationimplodebridge.cpp`.

---

## §0 — Cowork doc commit (local-only)

Committed `cowork_l1l4_completion_ledger.md` (new, 93 insertions — includes the standing
inference firewall) on `master`, local only:

- **sha = `ba7ed3d857b575968bf8fcb9f6a423446d09e5ad`**
- `git show --stat` lists exactly one file: `cowork_l1l4_completion_ledger.md | 93 ++++` — docs only.
- `scratch_artifacts/` was **not** committed: it is gitignored (`git check-ignore` → match), so
  `git add <ledger>` could not pull it in. No other modified/new `cowork_*` / `COWORK_*` existed
  (`git status --porcelain` showed only the ledger + the ignored `scratch_artifacts/`).
- This report (`cc_batch_analyze_unification_report.md`) is gitignored (`git check-ignore` → match)
  — not committed, per instruction.

---

## §1 — The corpus-characterisation call chain

`run_bach_preset.py` builds the corpus by invoking, per score, **no diagnostic flag**:

```
batch_analyze "<score.xml>" "<stem>.ours.json" --preset <Baroque|Jazz|Default|…>
```

(`tools/run_bach_preset.py:161-162` / `:174` — native and bash launch forms; the only ever-appended
`extra_args` are the additive read-only `--dump-*` flags, all documented byte-identical.)

In `main()` the dump mode defaults to **Batch** (`tools/batch_analyze.cpp:2406`,
`RegionDumpMode dumpMode = RegionDumpMode::Batch;`). With `--dump-regions` absent and
`--section-level` absent (`sectionLevel=false`, `:2409`), the corpus `.ours.json` is produced by:

```
main()  (batch_analyze.cpp:2801-2802)
  └─ regions = analyzeScore(score, excludeStaves, keyPrefs, chordPrefs, /*sectionLevel=*/false)
       └─ analyzeScore  (batch_analyze.cpp:553-711)
            └─ cra::analyzeRegions(score, startTick, endTick, excludeStaves,
                                   chordPrefs, keyPrefs, opts)        ← batch_analyze.cpp:595-596
            └─ (sectionLevel==false  ⇒  analyzeSection is NOT called; :615)
            └─ per merged region: keyresolver::resolveKeyAndModeRanked(...)  ← :677  (runner-up field only)
  └─ writeJson(regions, …)   (batch_analyze.cpp:2855 / :2874)
```

`cra::analyzeRegions` is **`mu::composing::analysis::region::analyzeRegions`** — the shared
orchestrator in `src/composing/analysis/region/regionanalyzer.cpp`. Its own header states the
sharing explicitly:

> *"Both `notation::analyzeHarmonicRhythm` (regional path) and `batch_analyze::analyzeScore` call
> this directly."* — `regionanalyzer.h:183-185`

The serialized `.ours.json` chord/key fields come straight from the orchestrator's per-region
result: `ar.chord = hr.chordResult`, `ar.key = hr.keyModeResult` (`batch_analyze.cpp:689,692`). The
key **winner** the gate measures is `analyzeRegions`' per-region winner; batch only *re-runs*
`resolveKeyAndModeRanked` to fill the runner-up JSON field (the orchestrator stores only the
winner — comment `:665-668`).

**→ The corpus path calls the production analysis entry. There is no parallel/own corpus analyzer.**

---

## §2 — Production-path vs diagnostic-only (kept separate)

The known diagnostic-only duplicate analyzers are reached by **early-return flag branches that never
reach `analyzeScore`/`analyzeRegions`**, exactly as the audit note says. Confirmed each returns
before the corpus path and is gated behind its own flag:

| Flag | Diagnostic analyzer | Bypasses corpus path |
|---|---|---|
| `--decode-chords` | `ChordSliceDecoder` (`runChordDecode`, :2248/:2783) | yes — returns before `analyzeScore` |
| `--diagnose-measures` | `diagnoseChord` replay (`writeDiagnosticJson`, :1479/:2853) | decorates the **same** regions; see note |
| `--dump-tonicization` | `tonicizationlabeler` | "labeler NEVER feeds the resolver" (:1179) |
| `--dump-key-candidates` | resolver dump replay (`writeKeyCandidateDump`, :835) | read-only, separate stream |
| `--validate-slices` / `--decode-keymode` / `--dump-cadence-anchor` / `--dump-modulation` / `--dump-joint-key` | various | "never reaches analyzeScore/analyzeRegions" / "standard `.ours.json` byte-identical" (:927,:990,:1054,:2698,:2726,:2765) |

Note on `--diagnose-measures`: since Stage 2.3 (`18dc9e1829`) `diagnoseChord` is a **view** that
replays the production pipeline (`analyzeChord` + `applyIter8691Pedal` + `applyPostScoringGates`) —
it is not a second scorer. Regardless, it is a separate flag and the corpus run does not pass it.

**→ The corpus `.ours.json` / BIR-root path does NOT route through any diagnostic analyzer.** It is
`analyzeScore → analyzeRegions` only.

---

## §3 — Unification verdict: **REUSE of the analyzer core + PARTIAL on configuration/wrapping**

**Reuse (no duplicate analyzer):** The corpus path runs the *same* `analyzeRegions` orchestrator the
notation product runs. The live bridge `analyzeHarmonicRhythm` is itself a thin wrapper around
`cra::analyzeRegions` (`notationharmonicrhythmbridge.cpp:131-133`). So the BIR gate exercises
**shipped analysis code** — there is **no second/parallel chord or region analyzer** behind the gate.
This is the load-bearing finding: F17's worst case ("the gate tests a path that isn't what ships,
duplicate analyzer") is **NOT** present.

**Partial (three configuration/wrapping divergences that weaken representativeness):** the corpus
path and the live product reach `analyzeRegions` with **different options and a different
post-pipeline**, so the corpus output is the live *region layer* under a *batch configuration*, not
the live final result. The three divergences:

1. **No `analyzeSection` (largest).** The live product always runs `analyzeSection(...)` ON TOP of
   `analyzeHarmonicRhythm`:
   - annotation action: `notationcomposingbridge.cpp:1372-1376`
   - bounded-window unit (status bar / P3): `notationcomposingbridge.cpp:320-324`
   - implode → chord track: `notationimplodebridge.cpp:1374-1377`

   `analyzeSection` adds measure layout, gap-tone insertion, **key/mode stabilization**, sparse-quality
   refinement, cadence/pivot detection, and confidence-gated key-area grouping
   (`composing/analysis/section/sectionanalyzer.*`; bridge note
   `notationcomposingbridgehelpers.cpp:29-32`). The corpus default path **omits all of it**
   (`sectionLevel=false`); it is only reachable via the diagnostic `--section-level` flag, which by
   design does **not** change the committed BIR gate (CLAUDE.md / STATUS Stage 2.2-i). So the gate's
   key field is the **pre-stabilization** region winner, and the chord field is the pre-section-refinement
   region winner.

2. **`excludeLookAheadOnDenseStart` differs at the region layer itself.** Batch sets it **`true`**
   (`batch_analyze.cpp:585`, "batch-specific tone-collection behaviour", :572-574); the live bridge
   sets it **`false`** (`notationharmonicrhythmbridge.cpp:119`). This is a tone-collection option on
   the *same* orchestrator that can change dense-start regions' tones (hence chord results) between the
   gate and the live path.

3. **Preset chord/key prefs.** The **primary** gate runs `--preset Baroque`
   (`preferMinorOverMajorAdd6=true`, inversion bonuses at struct defaults — `batch_analyze.cpp:2668-2669`).
   The live product uses **`kDefaultChordAnalyzerPreferences`** unconditionally at every live
   chord-scoring site (`notationharmonicrhythmbridge.cpp:133`; D-PASS0 Half A) — i.e. the Baroque
   chord-scoring preset **never reaches the live product**. Only **`--preset Default`** reproduces the
   live chord prefs (struct defaults, `preferMinorOverMajorAdd6=false` — `:2671-2678`). Mode priors:
   batch presets use fixed per-preset values; the live path reads them from
   `IComposingAnalysisConfiguration` (user settings); `--preset Default` reproduces the app's bespoke
   out-of-box priors (Stage 2.4 V4), but diverges if the user customizes mode priors.

This "partial" is already known and bounded in-repo: the Stage-2 roadmap calls it the metric blind
spot ("batch/BIR measures `analyzeRegions` while users get `analyzeSection`"); CLAUDE.md's Stage-2.2-i
granularity caveat (per-beat error ~7× the batch-region rate) and the 0.25 onset-threshold divergence
note (`batch_analyze.cpp:577-583`, roadmap 0.6) are the same fact set. The V4 measurement found the
Baroque gate's identity set = Baroque-13 ∪ {bwv187.7} — a near-exact, slightly conservative proxy for
the user-experienced (Default) region errors.

---

## §4 — Does the corpus output represent the shipped result?

**For the region-analysis ENGINE: yes — same code.** The chord/key the gate scores is produced by the
exact `analyzeRegions` the notation product runs; no duplicate analyzer sits behind the gate.

**For the full shipped RESULT: not exactly — it is the live *region layer under a batch config*, not
the live *final* output.** For a given score, `batch_analyze`'s corpus output equals what the notation
product shows only where all three §3 divergences are inert on that region:

- the score is measured under **`--preset Default`** (matches live chord prefs; `Baroque`/`Jazz` do not),
- the user has **not** customized mode priors (else live `keyPrefs` differ),
- the region has **no dense-start look-ahead difference** (`excludeLookAheadOnDenseStart` true vs false),
- the **onset threshold** is the default 0.25 on both (true today; batch hard-codes it, bridge reads
  config — `batch_analyze.cpp:577-584` vs `notationharmonicrhythmbridge.cpp:85`), **and**
- **`analyzeSection` is a no-op for that region** (key/mode stabilization, sparse refinement, and
  key-area grouping don't move the winner).

The last condition is the material one: the live user-visible answer is post-`analyzeSection`, and the
corpus default `.ours.json` is pre-`analyzeSection`. So the gate is a faithful test of the **shipped
region analyzer**, and (under `--preset Default`) a close proxy for the live result — but it is **not**
a measurement of the complete live pipeline. The gate's validity for catching analyzer regressions is
sound (it runs the real engine); its representativeness of the *end-user output* is **partial**, by the
documented design choice to gate at batch-region granularity.

---

## Summary

| Question | Finding |
|---|---|
| Corpus `.ours.json` path | `main → analyzeScore → cra::analyzeRegions` (no diagnostic flag) |
| Duplicate/parallel analyzer behind the gate? | **No** — shared `regionanalyzer::analyzeRegions`, same as `notation::analyzeHarmonicRhythm` |
| Diagnostic analyzers (`--decode-chords`, `--diagnose-measures`, `--dump-*`)? | Separate flags; early-return; do not touch the corpus path |
| Verdict | **REUSE of the analyzer core (gate is valid — tests shipped code) + PARTIAL on representativeness** |
| Partial divergences | (1) corpus omits `analyzeSection` (live always runs it); (2) `excludeLookAheadOnDenseStart` true vs false; (3) primary gate = `--preset Baroque`, never shipped — only `--preset Default` matches live chord prefs; mode priors fixed vs user-config |
| Shipped-result equality (§4) | Region-engine: identical code. Full output: holds only under `--preset Default`, default config, and where `analyzeSection` is winner-neutral; otherwise the corpus is pre-`analyzeSection` |

**Recommendation for Cowork (not implemented — read-only audit):** the F17 "one path per concern"
goal is met at the analyzer-core level. To close the representativeness gap, the section layer
(`analyzeSection`) and the `excludeLookAheadOnDenseStart` / onset-threshold options would need to be
brought onto the gate path (the Stage-2 unification already names this), and the user-facing gate read
from **`--preset Default`** rather than Baroque. These are behaviour-affecting changes (BA-gated) — out
of scope here.

**Stops honored:** no source edits; only the §0 doc commit (`ba7ed3d857…`, docs-only). No `upstream`
push.
