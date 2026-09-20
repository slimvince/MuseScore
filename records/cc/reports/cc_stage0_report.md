# CC Report — Stage 0: Hygiene and Honest Ground Truth

*Implements `docs/implementation_roadmap.md` Stage 0 (items 0.1–0.6). Base: `e7d4ba2b1a`.
Hard constraint: zero behavior change — met (416/416 · 52/52 · 11/11, zero snapshot diffs,
no goldens refreshed; BIR Baroque 13 / Jazz 7 unchanged, both presets regenerated, corpus
restored to Baroque).*

---

## 1. Doc pass (roadmap 0.1)

Fixed every site that presented `explorationMode` as a *live* mechanism (it was replaced by
`fn::ScoringPhase` in `e7d4ba2b1a`). Genuinely-historical mentions ("the former
`explorationMode` flag", "Iter 94 as the `explorationMode` flag") were left intact.

**ARCHITECTURE.md** (4 sites):

| Site | Before | After |
|---|---|---|
| §2.14 (L368) | "…already acknowledges this with `explorationMode`." | "…already acknowledges this by running its exploratory passes in `ScoringPhase::Segmentation` (progression signals withheld)." |
| §4.1d common gates (~L1001) | "`!prefs.explorationMode` (false during `greedyExpandSegmentation`'s internal boundary-exploration calls …)" | "`prefs.scoringPhase == ScoringPhase::Final` (the progression signals are withheld during …, which run in `ScoringPhase::Segmentation` …)" |
| Flag header block (~L1042) | "**`explorationMode` flag (Iter 94):** `ChordAnalyzerPreferences::explorationMode` (default `false`) is set to `true` …" | "**`ScoringPhase` (Iter 94 as `explorationMode`; reworked to the enum in `e7d4ba2b1a`):** `ChordAnalyzerPreferences::scoringPhase` (default `ScoringPhase::Final`) is set to `ScoringPhase::Segmentation` …" |
| Defer list (~L1334) | "**`explorationMode` coupling** — `greedyExpandSegmentation` sets `explorationMode = true` … Major refactor — defer." | "**Segmentation ↔ scorer phase coupling** — … sets `scoringPhase = ScoringPhase::Segmentation` … (introduced Iter 94 as the `explorationMode` flag; reworked into the `ScoringPhase` enum in `e7d4ba2b1a`, which removed the per-function dual-path …). The residual coupling … remains … Major refactor — defer." |

**docs/layer_architecture_audit.md** (3 sites, L265/267/349):

| Site | Before | After |
|---|---|---|
| L265 | "`explorationMode = true`: Gate R must never fire regardless of bassPc." | "`ScoringPhase::Segmentation`: Gate R must never fire regardless of bassPc." |
| L267 | "…the `!explorationMode` guard that CC found necessary." | "…the segmentation-phase guard (`phase == ScoringPhase::Final`) that CC found necessary." |
| L349 | "(`basisDep ≤ 0 && !explorationMode && bass ∉ template`)" | "(`basisDep ≤ 0 && phase == ScoringPhase::Final && bass ∉ template`)" |

**Deliberately NOT rewritten:**
- `docs/redesign_plan.md` — its `explorationMode` text (the "Resolve the dual-path"
  recommendation at ~L494–502 and the Gate R history at ~L531–542) is *freshly-added
  planning-session content*. The instruction protects these ("do not rewrite them"); they
  are out of the roadmap 0.1 scope (which names only ARCHITECTURE.md + the audit doc); the
  Gate R block is historically accurate (it describes `638ced1c12`, which **did** use
  `!explorationMode`); and turning the open "resolve the dual-path" recommendation into
  "resolved" would change the doc's *meaning*, not its tense — a stop-and-ask condition.
  `COWORK_HANDOFF.md` already records the dual-path as "✅ RESOLVED — committed
  `e7d4ba2b1a`", so the planning-doc set is internally coherent.
- `docs/scoring_model.md` §"ScoringPhase", §10, §11 (L670) — already correctly historical
  (e.g. "This replaced the former per-function `explorationMode` flag"; "Historical: in
  E1/E2 this was three explicit `!prefs.explorationMode`-gated calls"). No edit needed for
  the doc pass. (§10's struct-field line was updated separately under Task 3.)

**Uncommitted planning-doc review:** `CLAUDE.md` (+1 convention line), `STATUS.md`,
`COWORK_HANDOFF.md`, `docs/redesign_plan.md`, `ARCHITECTURE.md` §2.14 — all coherent
session-log / architecture-review updates; sanity-checked, not rewritten. STATUS.md even
records the exact pending follow-up that is this Task 1.

**Commit 1:** `7bc1609159` — doc set committed (message per instruction). Staged set was
exactly: ARCHITECTURE.md, CLAUDE.md, COWORK_HANDOFF.md, STATUS.md, docs/redesign_plan.md,
plus the two previously-untracked docs (docs/layer_architecture_audit.md,
docs/implementation_roadmap.md). `muse`, `ai-assistant/`, `cowork_*.md`,
`tools/dump_bir_cases.py` excluded.

---

## 2. Junk deletion (roadmap 0.4) — ⚠ DEVIATION

Both files identified and removed from disk:
- `s -ExecutionPolicy RemoteSigned) ; (& c:sMS.venvScriptsActivate.ps1)` (13966 bytes —
  a mangled PowerShell command captured as a filename)
- `C:tmpbuild_out.txt` (23 bytes — content was stray build output: `ninja: no work to do.`)

**Deviation:** the instruction stated these were *untracked* ("No commit needed (they were
untracked)"). `git status --porcelain` after `rm` shows them as **tracked deletions**
(` D "C\357\200\272tmpbuild_out.txt"` etc. — the `\357\200\272` is the Cygwin private-use
encoding of `:`). They were committed to the repo at some earlier point. The `rm` removed
them from the working tree, but because they are tracked, the deletion must be **committed**
to actually leave the repo.

Because the files are unambiguous junk, I removed them and **folded the deletion into the
proposed Commit 2** ("chore: Stage 0 hygiene") rather than creating a surprise commit.
Commit 2 awaits your confirmation, so nothing is finalized without review. `ai-assistant/`
left untouched. (Native git treats the `C:` prefix as a drive letter — `git ls-files
"C:tmpbuild_out.txt"` errors "outside repository" — so `rm` with a `./` prefix was used;
the staged deletion is reachable via `git add -A -- .` or `git rm`.)

---

## 3. Dead fnCtx fields (roadmap 0.2)

Removed `HarmonicFunctionContext::keyFifths` and `::keyMode` (`harmonicfunctionlayer.h`) and
their two writes + the "DEAD (write-only)" NOTE comment (`chordanalyzer.cpp`).

**No-other-consumer verification.** Searched all `*.cpp/*.h` for `HarmonicFunctionContext`:
only 5 usages — the struct def, the `applyHarmonicFunction` params (`ctx`, harmonicfunctionlayer.{h,cpp}),
the `fnCtx` write site (chordanalyzer.cpp:2934), and `gater_tests.cpp:205` (which sets only
`previousRootPc`/`nextRootPc`). A targeted scan of `harmonicfunctionlayer.cpp` for
`.keyFifths`/`.keyMode` finds only `snapshot.keyMode` and `gateCtx->keyMode` — **never**
`ctx.keyFifths`/`ctx.keyMode`. Confirmed write-only; safe removal. The struct comment was
rewritten to a guard ("no key fields here by design …") so they are not re-introduced; the
chordanalyzer.cpp rationale comment was preserved (key influence flows via
`ScoringCell::basisIndep` + `ScoringSnapshot::{scale,keyTonicPc,keyMode}`). `keySignatureFifths`
and `keyMode` locals remain used elsewhere — no unused-variable warnings.

Doc sync: `docs/scoring_model.md` §10 updated to list only `previousRootPc`/`nextRootPc`
and to state the deliberate absence of key fields.

---

## 4. `kTemplateCount` shared constant (roadmap 0.3)

**Placement:** `inline constexpr std::size_t kTemplateCount = 17;` in
`mu::composing::analysis` (chordanalyzer.h, at the top of the namespace block).

**Rationale:** the template set is owned by the chord scorer (the `templates` /
`kDiagTemplates` arrays and the three score matrices all live in the `analysis` namespace),
so the constant belongs there. The function layer's `kMasks` is a *mirror* / dependent and
references `analysis::kTemplateCount` — which matches, rather than fights, the include
direction (`harmonicfunctionlayer.h → chordanalyzer.h`). No include-direction change was
forced. `std::size_t` is available via the header's existing `<array>`/`<cstdlib>` includes.

**Sites converted (the 5 from scoring_model §9, plus one bonus):**
1. `analyzeChord` `std::array<TemplateDef, kTemplateCount> templates`
2. `kDiagTemplates` in `diagnoseChord`
3. the three score matrices `std::array<std::array<double, kTemplateCount>, 12>`
   (`basisIndepMatrix` / `complexityFactorMatrix` / `augFactorMatrix`)
4. `kMasks` `std::array<uint16_t, analysis::kTemplateCount>` in `harmonicfunctionlayer.cpp`
5. **(bonus, not in the instruction's list)** the `tiePriority >= 17` bounds check in
   `bassIsTemplateChordTone` — converted to
   `static_cast<std::size_t>(tiePriority) >= analysis::kTemplateCount` (the cast avoids a
   signed/unsigned `-Wsign-compare`; the preceding `tiePriority < 0` short-circuit makes it
   safe). This was a sixth literal-17 that also tracks the template count; see §7.

**static_asserts added (3):**
- `static_assert(templates.size() == kTemplateCount, …)` after the `templates` array;
- `static_assert(kDiagTemplates.size() == kTemplateCount, …)` after `kDiagTemplates`;
- `static_assert(kMasks.size() == analysis::kTemplateCount, …)` after `kMasks`.

These are `.size()`-based (implicit via the type, per the instruction) — they catch a future
hand-edit that re-hardcodes a size literal different from `kTemplateCount`. The deeper
guarantee is structural: adding a TemplateDef entry **without** bumping the constant is now a
hard compile error ("too many initializers"); the matrices/kMasks resize automatically. This
closes the silent stack-overrun class from B1.

**Doc sync:** `docs/scoring_model.md` §2 (count tied to `kTemplateCount`), §3 (Atomic update
requirement rewritten around the constant + compiler enforcement), §9 step 5 (rewritten:
bump the constant + add entries; failure modes documented).

---

## 5. Tie policy + divergence docs (roadmap 0.5, 0.6)

**FP tie policy (0.5):** new "### Floating-point tie policy" subsection in
`docs/scoring_model.md` (end of §3). Documents the exact comparator in `applyHarmonicFunction`
(`harmonicfunctionlayer.cpp`): `a.score != b.score` → higher score; tie → lower `tiePriority`;
tie → lower `rootPc`. States explicitly that **no epsilon** is used (intentional), and the
fragility caveat (Δ=+7b ~0.02-margin class, bwv320 ≈1.92 vs 1.90 could flip under FP
re-association — flags/platform/reordered arithmetic — so any such change requires a full
corpus A/B on both presets). Doc-only.

**Divergences (0.6):**
- `onsetBoundaryThreshold`: comment added at the `tools/batch_analyze.cpp` hard-coded `0.25`
  site, noting the bridge reads it from `IComposingAnalysisConfiguration`
  (`notationharmonicrhythmbridge.cpp:85`), that 0.25 is *also* the registered config default
  (`composingconfiguration.cpp:148`) so they coincide today, and that all batch corpus
  numbers assume 0.25. No behavior change (Stage 2 territory).
- Region-collapse duplication: cross-referencing comments added at **both**
  `regionanalyzer.cpp` same-root merge sites (main loop ~L497 and Pass 2 ~L694).
  **Helper NOT extracted** — the merge predicate + body are identical, but the two
  `else`-branches build different `HarmonicRegion` shapes (Pass 2 also sets `keyModeResult`,
  etc.), so a shared helper is not the *trivial, provably byte-identical* extraction the
  instruction gates on. Comments suffice; both point to `implementation_roadmap.md 0.6`.

---

## 6. Test / BIR results

| Check | Result | Required | Status |
|---|---|---|---|
| Build | exit 0, all targets linked | clean | ✓ |
| `composing_tests.exe` | 416 / 416 | 416 | ✓ |
| `notation_tests.exe` | 52 / 52 | 52 | ✓ |
| `pipeline_snapshot_tests.exe` | 11 / 11 (1 skip = divergence-observation generator) | 11 | ✓ |
| Goldens refreshed | none | none | ✓ |
| BIR=false Baroque (`characterise_bir_false.py`) | 13 | 13 | ✓ |
| BIR=false Jazz | 7 | 7 | ✓ |
| `tools/corpus/` restored | Baroque | Baroque | ✓ |

Build emitted only one warning — `notationcontextmenumodel.cpp(49): C4100 'element'
unreferenced formal parameter` — which is pre-existing and in `notationscene` code untouched
by this work. The three new `static_assert`s passed (the build would have failed otherwise);
no new warnings from any touched file.

Corpus runs: Baroque regenerate → characterise (13) → Jazz regenerate → characterise (7) →
Baroque restore. All `run_bach_preset.py` runs processed 353 scores (326 with WiR coverage),
exit 0.

---

## 7. Deviations

1. **Tracked junk files (Task 2).** The two junk files were *tracked*, not untracked as the
   instruction stated. Their removal therefore needs a commit. Folded into the proposed
   Commit 2 (clearly flagged); not finalized without your confirmation. See §2.
2. **Sixth literal-17 site (Task 4).** The instruction listed five sites. A sixth literal
   `17` — the `tiePriority >= 17` bounds check in `bassIsTemplateChordTone` — also tracks the
   template count and would silently mis-bound if the count changed. I converted it to
   `analysis::kTemplateCount` (with a `std::size_t` cast). This is strictly within the
   spirit of 0.3 ("all template-sized arrays derive from one constant") and is byte-identical
   at the current value 17.
3. **CLAUDE.md "4-site atomic update" section.** That section (project root) still describes
   the old "exactly four sites … silent stack-buffer overrun" workflow, now superseded by the
   compiler-enforced `kTemplateCount` approach. I did **not** edit CLAUDE.md — it is outside
   this instruction's doc-sync scope (which named only `scoring_model.md` §3/§9). Recommend a
   follow-up to reconcile CLAUDE.md's "4-site atomic update" / "Staleness check" wording with
   the new single-constant model.
4. **Build warning.** The single C4100 warning is pre-existing and unrelated (untouched
   `notationscene` code) — reported for completeness, not introduced here.

No test failed, no BIR moved, no snapshot diffed, no doc-meaning rewrite was required, and
`kTemplateCount` placement did not force an include-direction change — so none of the
stop-and-ask conditions were triggered.

---

## 8. Commit status

- **Commit 1 (Task 1, docs):** `7bc1609159` — committed.
- **Commit 2 (Tasks 3–6 code + the Task-2 tracked-junk removal):** **proposed, NOT committed**
  — awaiting Cowork confirmation.

**Proposed Commit 2 staged set** (explicit per-file; never `muse`):
- `src/composing/analysis/chord/chordanalyzer.h`
- `src/composing/analysis/chord/chordanalyzer.cpp`
- `src/composing/analysis/function/harmonicfunctionlayer.h`
- `src/composing/analysis/function/harmonicfunctionlayer.cpp`
- `src/composing/analysis/region/regionanalyzer.cpp`
- `tools/batch_analyze.cpp`
- `docs/scoring_model.md`
- the two tracked junk-file deletions (`C:tmpbuild_out.txt`, the mangled `s -ExecutionPolicy…`)

**Excluded:** `tools/dump_bir_cases.py` (separate concern), `cowork_*.md`, `ai-assistant/`,
`tools/iter90_*.txt`, `tools/iter97_*.txt`, `tools/corpus/` (gitignored), `muse`.

**Proposed Commit 2 message** (extended from the instruction's draft to cover the
tracked-junk removal — please confirm or adjust):

```
chore: Stage 0 hygiene — kTemplateCount, dead fnCtx fields, tie-policy docs

Derive all template-sized array extents (both TemplateDef arrays, the three score
matrices, kMasks, and the bassIsTemplateChordTone bounds check) from a single
analysis::kTemplateCount constant (closes the silent stack-overrun class from B1;
scoring_model.md §2/§3/§9 updated per sync rule). Remove the write-only
HarmonicFunctionContext keyFifths/keyMode fields (documented dead since the Step-3
investigation). Document the FP tie policy and the batch onsetBoundaryThreshold
divergence; cross-reference the duplicated region-collapse sites. Remove two tracked
repo-junk files (a mangled PowerShell-command filename and C:tmpbuild_out.txt) — these
were tracked, not untracked as the Stage-0 instruction assumed.

Byte-identical: 416/416, 52/52, 11/11, zero snapshot diffs, no goldens refreshed;
BIR Baroque 13 / Jazz 7 unchanged (both presets regenerated, corpus restored to Baroque).
```

(If you prefer the junk removal as a *separate* `chore: remove tracked repo junk` commit, or
to leave it out of Commit 2 entirely, say so and I'll restage accordingly.)
