# Claude Code — Standing Instructions for This Repository

## Project context

This is MuseScore Studio. The active development area is the `composing` module
(`src/composing/`), which implements harmonic analysis. See
`C:\Users\vince\.claude\projects\c--s-MS\memory\project_chord_analyzer.md` for
full project context.

## Autonomous operation — composing module

When working on the `src/composing/` module you are **pre-authorized** to:

- Edit any file under `src/composing/` without asking for confirmation
- Edit `src/notation/internal/notationaccessibility.cpp` without asking
- Edit `ARCHITECTURE.md` (project root) without asking
- Run the build: `powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`
- Run the tests: `./composing_tests.exe` from `ninja_build_rel/`
- Read `src/composing/tests/chord_mismatch_report.txt` after each test run

**Standard loop for mismatch reduction work** — do all of the following without
stopping for confirmation:
1. Analyse the mismatch(es)
2. Implement the fix in `chordanalyzer.cpp`
3. Build
4. Run tests and read the mismatch report
5. Report results (mismatches before → after, any regressions)

Only stop and ask if:
- A regression is introduced (mismatch count goes up or a previously passing
  test fails)
- A change would touch files **outside** `src/composing/` and
  `notationaccessibility.cpp`
- The catalog XML (`chordanalyzer_catalog.musicxml`) needs to be modified
  (ground-truth changes require explicit approval)
- You are uncertain whether a fix is correct and want a second opinion

## Build and test commands

**Always read these two files at the start of every session:**
- `C:\s\MS\BUILD_AND_TEST.md` — authoritative commands for all build variants, both test suites, and all Python tools
- `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration, and known regressions

Do not rely on memory of previous sessions for BIR numbers or iteration state — read STATUS.md.

```
# Build — use PowerShell Start-Process (cmd.exe //c fails in MSYS2/Git Bash)
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Run composing tests (must be in ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe

# Run notation tests — includes P1/P2/P3/P4 pipeline regression test
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check (always --preset Baroque unless iteration says otherwise)
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report written to:
src/composing/tests/chord_mismatch_report.txt
```

**Both test suites must pass after every code change.** The notation tests include
`pipeline_snapshot_tests` which pins P1/P2/P3/P4 output against golden JSON files.
If a change intentionally alters chord output (e.g. a new inversion gate fires),
the pipeline snapshot goldens need refreshing. Note: `pipeline_snapshot_tests.exe`
is a SEPARATE binary from `notation_tests.exe` — pass `--update-goldens` to it:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
```
Then re-run `./pipeline_snapshot_tests.exe` to confirm all pass.
Only run `--update-goldens` when the output change is verified correct.

## Gate threshold and preset policy

Gate thresholds (e.g. Gate I: 0.45, Gate K: 0.20, Gate L: 0.35) are **calibrated
against the Baroque corpus** and are intentionally Baroque-specific. Do NOT adjust
them to accommodate other musical styles.

**Before committing any gate addition or modification**, corpus analysis must be run
for BOTH Baroque and Jazz presets. Any BIR=false increase in either preset is a
hard stop:

```
# Baroque (per-preset dir — clean-slated and manifest-stamped each regen)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque

# Jazz (independent dir — no contamination; order no longer matters)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz
cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz
```

Since Stage 2.2a (M3 fix) each preset writes to its **own** dir under `tools/corpus/`
and stamps a `corpus_manifest.json`. `run_bach_preset.py` clean-slates the dir at the
start of a regen and **exits nonzero** unless the corpus is complete (**352/352** at current HEAD — the
expected count is derived from the source `.xml` files, not hard-coded);
`characterise_bir_false.py` **refuses** to measure a dir whose manifest is missing,
incomplete, or whose `.ours.json` fingerprints do not match (preset contamination —
the old shared-`tools/corpus` failure mode). The gate is the **case-identity** set,
not a bare integer.

**Two-tier refinement (user-ratified 2026-06-22) — class-(b) functional regression vs class-(a)
symmetric-rotation churn.** A *new* BIR=false case is one of two classes:
- **Class (b) — functional/key regression: UNCHANGED HARD STOP.** A new BIR=false case at a sonority
  whose root is *pitch-class-decidable* (any non-symmetric chord — triads, dominant sevenths, etc.)
  where the analysis now gets the root or key wrong. **Zero** new class-(b) cases on any preset, ever.
  This is the gate's real intent and does not move.
- **Class (a) — symmetric-rotation churn: TRACKED, CONDITIONAL (not an automatic hard stop).** A new
  BIR=false case at a sonority whose root is *pitch-class-undecidable by construction* — symmetric
  diminished-seventh, augmented, whole-tone, or a share-tone tetrad (half-dim↔m6; dim7-subset-of-V7♭9;
  Maj7↔relative-minor triad). The pitch-class analyzer is spelling-blind and cannot pick the
  spelling-correct rotation; no rotation is more correct by pitch class. Acceptable **only when ALL** of:
  (1) **verified at the score per case** against the actual notes (e.g. the music21 GT region) —
  assertion is not enough; (2) **default to class (b) on any doubt** — if not *proven* class-(a), it
  IS class-(b); (3) **the class-(b) (pitch-class-decidable-root) BIR=false count is non-increasing** on every preset —
  the *meaningful* errors never grow; the class-(a) total may wobble by a **small, every-case-verified**
  amount (the rotation count is a coin-flip, not a quality measure), but a **large class-(a) net
  increase trips mandatory investigation** (a change destabilizing many symmetric sonorities is a
  signal even when each case is individually class-(a)); (4) **case identities recorded** (stem@tick +
  sonority); (5) **interim only** — a
  bridge pending the Stage-5/6 spelling-aware (two-tier) gate, which retires this exception. Applies
  **only** to the symmetric/share-tone structural class; no other source of a new BIR=false case
  qualifies. Root cause: the rotation churn is a **chord-layer (Layer-4) root ambiguity** *surfaced,
  not caused,* by a key change; the proper fix is spelling/voice-leading-aware chord-root selection
  (Layer 4 / Stage 5–6). Founding evidence (Cowork-verified at the score, music21 GT, 2026-06-22):
  `bwv272@4320` (G♯dim7), `bwv289@20160` (A♯dim7), `bwv291@17760` (Eø7↔Gm6), `bwv387@10560`
  (G♯dim7/E7♭9) — all symmetric/share-tone, zero functional regressions; the Layer-3 decoder-wiring
  increment. Full provenance: `cowork_gate_policy_amendment.md`.
- **First accepted class-(a) interim case (Layer-3 wiring, 2026-06-22):** Baroque/Default net **−4** (all new
  cases class-(a)); **Jazz net +1** — accepted under guardrail (3): new `bwv272@4320` (G♯dim7 coin-flip) +
  `bwv291@17760` (Eø7↔Gm6 same-collection center), `bwv244.15@10080` fixed; both new verified class-(a) at the
  score, zero new class-(b), and the L3 reduction-rule lever measured byte-identically inert (a≡b on all presets) —
  so the +1 is irreducible at Layer 3. **Retires when Layer 4 (function/cadence) pins the rotation/center** —
  rotation-pinning is a named early Layer-4 job. Investigation: `cc_layer3_jazz_churn_investigation.md`.

**★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; `cc_a8_rebaseline_measure_report.md`).** The
**primary reported metric AND the Stage-5 fitting-objective basis** is now the **granularity-robust
union-of-boundaries unit, variant (b) DCML-only** (music21 is not GT): **root governs, with RN + key always
tracked beside it**. Ratified baselines (variant b, root-agree at 326/352 coverage; **★ re-baselined at the
2.2e kWStepIn adoption, 2026-07-05**): **Baroque 63.36 % / Jazz 62.37 % / Default 63.25 %** (RN-agree
44.58/42.40/44.41 %, key-agree 68.19/64.52/67.77 %). *(Jazz is byte-identical to the pre-adoption corpus —
proven by an explicit-override reconstruction — so its root/RN reproduce the prior 62.37/42.40 exactly; its
key figure reflects the a8 re-measure, not a 2.2e change. Prior baselines: 63.32/62.37/63.22, RN
44.56/42.40/44.40, key 68.11/64.43/67.50.)* When it
governs, the **hard stop is the class-(b) (pitch-class-decidable-root) root-disagree DURATION non-increase per
preset** + a **mandatory explained per-run set-diff** (zero-new-case cannot scale to ~7,000 cells; class-(b)
dominates ~95 %+ at this unit). **UNTIL the Stage-5 fitter lands, the batch 52/24/52 case-identity gate above
REMAINS THE hard regression stop (R10 unchanged)** — the robust unit is the reported/fit-objective metric, the
batch gate is the tripwire. C1 reliability curves on this unit: `cc_c1_reliability_report.md`.

**Re-baselined 2026-06-13 (corrected GT parser).** The prior **13/7/14** gate was an
**undercount**: GT-parser bugs (applied-chord `/X` rooting + minor-key
leading-tone/submediant rooting, fixed in `tools/dcml_parser.py`) corrupted the WiR roots
of applied and `viio`/`vio` chords, pushing genuine candidate cases into the discarded
`all_differ` bucket. With the roots now oracle-correct (music21 `RomanNumeral`, **100% on
all gate cases**), those cases surface. The new gate is a **strict superset** of the old
(every old case preserved, **0 lost** — verified through the canonical tool with an A/B
parser revert). **~95% of the added mass is legitimate ambiguity** — chiefly **symmetric
fully-diminished-7th** sonorities (root pitch-class-undefined by construction; ≈53% of
Baroque) and **viio↔V7 share-tone** readings; the genuinely-new *actionable* error count
is only ~1–3 per preset (net ≈9–10 Baroque / ~4 Jazz). The symmetric-dim7 members are
structurally unresolvable by pitch class and are the seed of a future **two-tier /
spelling-aware** gate (Stage 5/6 — noted, not built). Full provenance:
`cc_metric_rebaseline_report.md` + `cc_gate_rebaseline_verify_report.md`.

**★ CURRENT STATE `52 / 24 / 52` (re-baselined at the ratified 2.2e kWStepIn adoption, 2026-07-05, commit
`c50002fee1` + the corpus chore below).** The 2.2e delta vs the prior `53 / 24 / 53`: **removal-only
`{bwv244.32@5760}`** on Baroque + Default (the class-(b) case the kWStepIn 0.10→0.125 adoption fixed); Jazz
unchanged (byte-identical). The identity sets below are the 52/24/52 form; the history that produced the
prior 53/24/53 is preserved in the following paragraph.

**★ (History) Corrected to the ratified post-L3-wiring state `53 / 24 / 53` (Stage-0 measurement, commit `b57dbfa7a8`,
2026-06-25).** The `57/23/57` sets previously listed here predated the **already-ratified L3-wiring delta**
(`−4 / +1 / −4`) — the two-tier-gate prose above describes that delta, but these integer tables were never updated.
They are now. The delta, verified by diffing the measured sets against the prior `57/23/57` sets: **Baroque**
`− {bwv102.7@17520, bwv122.6@6720, bwv227.7@18120, bwv301@960, bwv336@8640, bwv381@4800}` (six fixed)
`+ {bwv272@4320, bwv289@20160}` (two class-(a) symmetric dim7) = net **−4**; **Jazz** `− {bwv244.15@10080}`
`+ {bwv272@4320, bwv291@17760}` = net **+1**. (Baroque and Jazz deltas Cowork-verified against the prior sets;
Default measured at `53`.) The **case-identity set, not the integer, is the gate** — re-measure with
`characterise_bir_false.py` after any change.

- **Baroque = 52** with identities (stem@tick):
  `{bwv10.7@36000, bwv14.5@8160, bwv144.6@15360, bwv144.6@16320, bwv151.5@13440, bwv153.1@18240, bwv16.6@16800,
  bwv169.7@24960, bwv17.7@46080, bwv174.5@6240, bwv20.11@13440, bwv244.46@960, bwv245.15@13920,
  bwv245.17@4800, bwv245.37@13920, bwv245.3@12480, bwv245.40@51360, bwv258@10560, bwv261@33840, bwv269@20640,
  bwv272@4320, bwv272@4800, bwv272@8160, bwv282@9120, bwv289@20160, bwv289@21600, bwv300@13440, bwv309@8640,
  bwv320@31680, bwv334@5280, bwv334@6720, bwv342@25440, bwv352@1440, bwv358@6000, bwv364@2880, bwv392@14400,
  bwv40.3@2400, bwv402@22080, bwv416@10080, bwv421@2880, bwv422@23040, bwv423@28320, bwv429@24240, bwv432@5520,
  bwv45.7@20160, bwv48.3@2880, bwv57.8@15360, bwv60.5@30960, bwv64.8@5280, bwv77.6@22080, bwv94.8@24960,
  bwv96.6@13440}` (= prior Baroque-53 − `{bwv244.32@5760}`, the class-(b) case the 2.2e kWStepIn adoption fixed;
  `characterise_bir_false.py --corpus-dir tools/corpus/baroque`, re-baselined at the ratified 2.2e adoption, removal-only).
- **Jazz = 24** with identities (stem@tick):
  `{bwv144.6@15360, bwv144.6@16320, bwv245.15@13920, bwv245.17@4800, bwv245.37@13920, bwv245.40@51360, bwv272@4320,
  bwv272@8160, bwv280@17280, bwv282@9120, bwv291@17760, bwv301@1440, bwv313@14880, bwv334@5280, bwv342@25440,
  bwv392@14400, bwv422@23040, bwv429@24240, bwv432@5520, bwv45.7@20160, bwv48.3@2880, bwv64.8@5280, bwv74.8@13440,
  bwv74.8@13920}` (= prior Jazz-23 − {bwv244.15@10080} + {bwv272@4320, bwv291@17760}).
- **Default (the user-run config) = 52.** Per the `characterise_bir_false.py --corpus-dir tools/corpus/default`
  measurement, Default = Baroque-52 with `{bwv352@1440, bwv60.5@30960}` replaced by `{bwv227.7@18000, bwv387@10560}`
  (the rest identical to Baroque-52). Re-baselined at the ratified 2.2e adoption: removal-only `{bwv244.32@5760}`
  vs the prior Default-53 (the same class-(b) case the kWStepIn adoption fixed on Baroque). *(✅ RE-CONFIRMED by measurement at the 2026-07-03 grammar-completion regen
  (`cc_grammar_completion_report.md`, commit `ce509b0961`): all three presets' case-identity sets matched this
  document exactly, set-diff empty both directions — the earlier Stage-0 prose-inconsistency caveat is discharged and
  the Default identities above may be relied on.)*

**Cross-layer-budget caveat (2026-06-24, O1 measurement):** the BIR=false set is **not** the Layer-5 resolver
residual — it is a **work budget distributed across Layers 1–5**, and it overstates the function-only remainder
several-fold. Measured during the O1 investigation (`cowork_uncertain_resolver_investigation.md` +
`cc_uncertain_resolver_measurement_report.md`): ≈60% Baroque / ≈42% Jazz are **spelling-resolvable** (the Layer-4
notated-spelling root pin), and most of the rest is **bass/inversion**, **local voice-leading**, or plain
**segmentation over-grab** the change-point slicer (Layer 2) removes by construction (e.g. `bwv10.7@36000` — a 5-note
scale `C-D-E♭-F-G` over-grabbed across two GT chords `i43`/`iv532`, Cowork-verified at the score). The genuinely
**function-only** remainder reaching Architectural Layer 5 is small: pitch-class-identical share-tone chords
(`bwv352` Am6↔F♯ø7; Jazz `bwv291` Eø7↔Gm6) on the chord side, and the **note-identical** key-disagreement class
(relative major/minor, tonicization-vs-modulation) on the key side. So a BIR=false count is read as cross-layer work,
not as any one layer's accuracy. (O1 resolved: the resolver of "uncertain" is Layer 5 itself, no separate box.)

**Granularity caveat (Stage 2.2-i):** the 53/24 gate is measured at **batch
(cross-barline) region** granularity; the user-visible **per-beat** root-error rate
is ~7× higher when the same scores are scored at measure-aligned (section)
granularity. Inspect that view with `batch_analyze --section-level` (diagnostic flag,
default OFF — it does not change the gate). See `cc_stage2_2_ab_dossier.md` for the
A/B that quantified this; a granularity-robust metric is mandatory at Stage 5.

(`tools/analyze_inversion_errors.py` is a *separate* secondary metric: its three-way
`music21_dcml_agree` genuine split is `bassIsRoot` true/false. **Re-measured under the
corrected parser** (`cc_functional_residual_dossier.md`, 2026-06-14): **Baroque 24/13→47/57,
Jazz 35/7→81/23** — the `bassIsRoot`=false halves (**57 / 23**) independently match the
re-baselined gate. `characterise_bir_false.py` reproduces that BIR=false half (57/23, Default 57).
Since Stage 2.2-ii (Rider 1) it takes `--corpus-dir` and reads BOTH `.ours.json` and
`.music21.json` from the validated per-preset dir — `--ours-dir` is a deprecated,
unvalidated alias.)

If a gate causes BIR=false regressions in a non-Baroque preset, the correct fix is:
1. A tighter **structural entry condition** that excludes the problematic chord type
   regardless of preset (preferred — e.g. an extension guard blocks augmented+seventh
   chords in all styles), OR
2. A **preset-specific threshold override** that leaves the Baroque-tuned value unchanged.

Never widen a Baroque-tuned threshold to cover a non-Baroque edge case.

**Preset scoring caps — corrected 2026-06-10:** `maxTotalInversionContextBonus` is
**never set on any code path** — both presets inherit the 2.0 default, and the cap is
currently non-binding (the four inversion bonuses sum to 1.85 Baroque/default, 0.75
Jazz). The formerly documented "Baroque=2.5 / Jazz=0.6" values were aspirational and
never implemented. Jazz's inversion behavior comes from its **reduced individual
inversion bonuses** (0.20/0.20/0.15/0.20 in `batch_analyze.cpp`), not the cap. Full
story in `docs/scoring_model.md` §4 (note below the "Other terms" table).

## Scoring model — `docs/scoring_model.md` (MANDATORY for scoring sessions)

**Read `docs/scoring_model.md` at the start of any session that touches scoring
logic in `chordanalyzer.cpp`** — this includes adding or modifying templates,
bonuses, guards, gates, score matrices, or post-scoring passes.

The document is the authoritative reference for how the scoring pipeline works,
why each term exists, and what invariants must not be broken. Violating these
invariants without reading the doc first has caused multiple failed attempts
(B1 leading-tone ambiguity, B2 ×4, B3 rotation-selector bypass).

**Sync rule — mandatory:** Any commit that adds or modifies a template, bonus,
guard, gate, or other scoring term in `chordanalyzer.cpp` **must** include a
corresponding update to `docs/scoring_model.md` in the same commit. The two
must never drift apart. Specifically:

- Adding a template: update the Templates section (§2), increment the template
  count in the array-size comment, add the guard description if applicable
- Adding or changing a bonus/gate: update the relevant §4 or §6 entry
- Adding a new constraint or dead end: add it to §8

**Staleness check:** The template count in `docs/scoring_model.md` §2 must
always match the `array<TemplateDef, N>` declaration in `chordanalyzer.cpp`.
If they differ, the doc is stale — update it before proceeding.

**Template additions — the `kTemplateCount` model (since `a236a0ff21`):** All
template-related array extents (the `analyzeChord` template array, the three score
matrices, `kMasks` in `harmonicfunctionlayer.cpp`) are derived from
`analysis::kTemplateCount` in `chordanalyzer.h`, so the compiler enforces size
consistency — the old silent stack-buffer-overrun failure mode (a missed matrix
resize, caught in the B1 attempt 2026-06-04) is closed. (Since Stage 2.3
`18dc9e1829` the duplicate `kDiagTemplates` array is gone — `diagnoseChord` replays
the production pipeline, so there is **one** template array, not two.) Adding a
template means:
1. Bump `analysis::kTemplateCount` N→N+1 (auto-resizes the matrices and `kMasks`)
2. Add the new `TemplateDef` entry in `analyzeChord`
3. Add the interval bitmask to `kMasks` (a zero mask silently disables Gate R)

Remaining trap: bumping the constant **without** adding the `TemplateDef` entry
value-initializes a trailing all-zero template (silent) — always do both in the
same edit. The authoritative checklist is `docs/scoring_model.md` §9.

## Score corpora

For any task involving scores (validation, snapshot tests, manual QA,
LLM-triage, qualitative review), read `docs/score_inventory.md` first. It
maps every score location to its intended use and lists the do-not-touch
files. Companion references: `tools/REPRODUCIBILITY.md` (how to recreate
corpora) and the JSON registries (`tools/corpus_registry.json`,
`tools/extra_scores_registry.json`).

## Local patches — do not revert

The following changes have been made intentionally to fix bugs unrelated to the
composing module. Do **not** revert them, and do not let build scripts or
dependency updates overwrite them without explicit approval.

### Windows Snap fix — `muse` submodule (applied 2026-05-14)

**File:** `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`  
**Function:** `calculateWindowSize()`

Two lines were removed that set `ptMinTrackSize` equal to the full monitor work
area inside the `WM_GETMINMAXINFO` handler. This told Windows the minimum
allowed window size was the entire screen, which prevented Windows Snap from
resizing a maximised MuseScore window into a chosen snap zone (the window
stayed full-screen and lost its title-bar controls).

The fix: `ptMaxSize` and `ptMaxPosition` are kept (they correctly constrain the
maximised position); `ptMinTrackSize` is intentionally left unset.

Upstream issue: musescore/MuseScore#25823 (related cousins: #21344, #16794).  
Introduced by upstream commit `4ad218709` (5 Aug 2025).  
**Do not restore the `ptMinTrackSize` lines.**

### MusicXML declared-mode import fix (Stage 4a, applied 2026-06-14)

**File:** `src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp`  
**Function:** `addKey()` (the `KeySig`-dedup guard, ~line 5976)

The dedup guarded the `KeySig` creation on **fifths only**:
`if (oldkey != key.key() || key.custom() || key.isAtonal())`. At score start the
prevailing key defaults to `{C, KeyMode::UNKNOWN}` (`KeyList::key()` →
`setConcertKey(Key::C)`), so a **0-fifths** key signature carrying an explicit
`<mode>` (e.g. `<fifths>0</fifths><mode>minor</mode>`) matched the prevailing fifths,
the whole `KeySig` was dropped, and the declared `<mode>` went with it →
`KeyMode::UNKNOWN` downstream. Export *does* write `<mode>`
(`exportmusicxml.cpp:2473`), so this broke export/import round-trip of `<mode>` and,
in our pipeline, dropped the declared-mode anchor on ~79 zero-signature Bach stems
(`cc_key_emission_headroom_dossier.md` — `declaredModeOrdinal=-1`). The maintainers'
own `// TODO only if different custom key ?` flags the dedup as known-incomplete.

The fix: fetch the prevailing `KeySigEvent` (not just the `Key` fifths) and add an
`oldKeySig.mode() != key.mode()` term to the guard, so a mode-bearing key at matching
fifths is retained. A key matching the prevailing one in **both** fifths and mode (and
not custom/atonal) still produces **no** `KeySig`, so plain mode-less C-major scores are
unaffected. Verified isolated to empty-signature scores (exactly 79 zero-sig `.ours.json`
changed, 0 non-empty-signature stems); BIR gate byte-identical on all three presets
(Baroque 57 / Jazz 23 / Default 57); key-inference S2 −378 (Default). Round-trip of
`bwv254` (0-fifths `<mode>minor</mode>`) now preserves `<mode>`.

Upstream issue: musescore/MuseScore#9444. The buggy fifths-only dedup is upstream-unchanged
code (the `// TODO only if different custom key ?` line). Stage-4a discrete step; the
graded-prior / KeyArea work that softens the resolver's −7 declared-mode wall is a later
Stage-4 step (see `cc_stage4a_mode_import_report.md`).
**Do not revert; do not let dependency updates overwrite without approval.**

**★ DISTRIBUTION CONSTRAINT (user, 2026-06-15): FORK-LOCAL ONLY — NEVER merge upstream / to the
MuseScore community.** This patch (`cfc7eb5e39`) is fine to have in the **central repo = the user's
fork** (`origin` = `slimvince/MuseScore`) and may be pushed there, but it must **NEVER** be pushed or
merged to `upstream` (`musescore/MuseScore`) or otherwise contributed to the MuseScore community.
`upstream` push is disabled in this repo; keep it so. Any future push/PR/merge that would carry
`cfc7eb5e39` (or its content) toward `musescore/MuseScore` is a HARD STOP — surface, do not proceed.
(The #9444 reference above is the upstream *bug report*; it does NOT authorize contributing THIS patch.)

## VS Code extension — bash command rules (MANDATORY, every session)

The Claude Code VS Code extension (v2.1.141+) has a 15-second stall detector. If the
API stream is silent for >15 seconds — which happens any time a bash command is running
— the extension marks the session `idle` and hands control back to the user, even though
CC is still running. This causes silent disconnects that are hard to detect.

**Two rules that apply to every bash command, no exceptions:**

**Rule 1 — Always append `; echo "exit:$?"` to any command that may return non-zero.**
A non-zero exit code also triggers an immediate idle transition. The echo always returns 0.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Rule 2 — Never let a single bash call produce large output.**
Large output (thousands of lines) takes >15 seconds to process and triggers the stall
detector. Redirect to a file and read separately.
- BAD:  `./pipeline_snapshot_tests.exe`  (many failing tests = large output)
- GOOD: `./pipeline_snapshot_tests.exe > /tmp/snap_out.txt 2>&1; echo "exit:$?"`
         then `head -50 /tmp/snap_out.txt`
- BAD:  `batch_analyze <score> --dump-regions notation`
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

Build commands via `Start-Process` are isolated from these rules (exit code not exposed).

## Conventions

- American English throughout — "analyzer" not "analyser"
- No confirmation prompts between analyse → implement → build → test steps
- Commit only when explicitly asked
- never hallucinate or guess, verified facts only - better ask first if unsure.
