# Gate Re-Baseline Verification — 57/23 through the CANONICAL tool + hand-traced soft bucket

*CC, 2026-06-13. READ-ONLY analysis + corpus regen at HEAD `bcd4319aa7`. The metric-batch
fixes (`cc_metric_rebaseline_report.md`) stay **STAGED/HELD** — no new commit; CLAUDE.md /
STATUS.md NOT edited (the gate-identity rewrite is Cowork's, post-verify). Verifies the
13→57 / 7→23 move before ratification. P3 out of scope (key axis, rides with Stage 4).*

Evidence tags: **[probe]** ran a script · **[oracle]** music21 9.9.1 `roman.RomanNumeral` ·
**[code]** quoted source.

---

## §0 — TL;DR (verdict: 57/23 is the right pin to enshrine)

1. **The canonical tool reproduces 57/23 at HEAD — no driver-vs-canonical discrepancy.**
   `characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz}` over freshly
   regenerated 353/353 corpora stamped at HEAD returns **Baroque 57, Jazz 23** — identical
   to the throwaway `gate_ids.py`. [probe]
2. **Strict superset confirmed THROUGH the canonical tool (0 lost), both presets.** I ran the
   same canonical tool against the OLD (HEAD-committed) parser → exactly **13 / 7**, captured
   its identity set, and set-diffed: **OLD ⊆ NEW, 0 lost** for Baroque (13⊆57) and Jazz
   (7⊆23). All 13 documented Baroque `stem@tick` + all 7 Jazz stems are present. [probe]
3. **Every contested GT root is oracle-correct.** All 57 + 23 WiR roots that the gate uses
   match the music21 `RomanNumeral` root computed on the actual figure + local key —
   **80/80 = 100 % [oracle]**. The re-baseline rests on correct ground truth.
4. **Hand-trace firms the actionable count — it does NOT materially move.** Refined split of
   the +44/+16 (each contested root oracle-tagged): **Baroque +44 = 42 ambiguity (95 %) / 2
   genuine (5 %)**; **Jazz +16 = 15 ambiguity (94 %) / 1 genuine (6 %)**. Net actionable
   after re-baseline ≈ **9–10 Baroque / 4 Jazz** — confirms the report's ~10 / ~4. The gate
   *count* quadruples; the actionable signal barely changes. **No stop-condition triggered.**
5. **New structural finding (refines the report):** ~18 of the report's "soft viio↔V7"
   cases are actually over a **symmetric fully-diminished-7th sonority** (we hear all four
   dim tones, our root is a rotation labelled as a rootless dominant) → **pitch-class
   unresolvable**, not soft. The report's "dim7-rot 12" undercounts the unresolvable
   sub-class because it keyed on *our* quality label; the sonority-based count is **30/57
   Baroque (53 %)**. This is the seed of a possible two-tier / spelling-aware gate (noted,
   not built).

**Recommendation: ratify 57/23.** It is a real undercount-correction (oracle-grounded,
strict superset), 95 %+ legitimate ambiguity, and the genuinely-new actionable additions
are 1–2 cases. Additionally flag the symmetric-dim7 set as a structurally-unresolvable
sub-class for a future two-tier gate.

---

## §1 — Canonical-tool reproduction at HEAD (Step 1)

### Setup
- **Build at HEAD:** `setup_and_build.bat` → `ninja: no work to do` — the existing
  `batch_analyze.exe` is already the HEAD build (the intervening `a4ae4a9203` key-diagnostic
  touched `keymodeanalyzer`/`keyresolver`/`batch_analyze.cpp` but is proven byte-identical
  output, STATUS 0/353). [probe]
- **Regen both corpora at HEAD:** `run_bach_preset.py --preset Baroque/Jazz` →
  both **353/353 complete**, `corpus_manifest.json` stamped **`bcd4319aa7` = HEAD** (was
  `a652dc1ba7`, 3 commits behind). Manifest guard satisfied. [probe]
- music21 **9.9.1** (matches the audit oracle). [probe]

### Result — 57/23 confirmed via the canonical tool
```
characterise_bir_false.py --corpus-dir tools/corpus/baroque  → 57 genuine BIR=false (git bcd4319aa7)
characterise_bir_false.py --corpus-dir tools/corpus/jazz     → 23 genuine BIR=false (git bcd4319aa7)
```
**No discrepancy** between the throwaway `gate_ids.py` (57/23) and the canonical
`characterise_bir_false.py` (57/23). [probe]

### Strict-superset / 0-lost — proven through the SAME canonical tool
To avoid trusting the throwaway driver's set-diff, I temporarily reverted `dcml_parser.py`
+ `compare_analyses.py` to their HEAD-committed (pre-fix) blobs, ran the canonical tool
(→ **13 / 7**, the historical baseline), captured the identity sets, then restored the
staged fixes (worktree+index blob hashes verified byte-identical to the pre-revert
snapshot). Set-diff OLD vs NEW [probe]:

| preset | OLD (canonical, HEAD parser) | NEW (canonical, staged parser) | lost | added |
|---|---|---|---|---|
| Baroque | 13 | 57 | **0** | 44 |
| Jazz | 7 | 23 | **0** | 16 |

- **OLD Baroque-13** = the exact CLAUDE.md set (`bwv102.7@17520, bwv14.5@8160, bwv17.7@46080,
  bwv174.5@6240, bwv245.17@4800, bwv245.40@51360, bwv261@33840, bwv269@20640, bwv301@960,
  bwv381@4800, bwv422@23040, bwv432@5520, bwv45.7@20160`) — all 13 present in NEW. ✓
- **OLD Jazz-7** = `{bwv244.15@10080, bwv245.17@4800, bwv245.40@51360, bwv422@23040,
  bwv432@5520, bwv45.7@20160, bwv74.8@13440}` — all 7 present in NEW. ✓
- `comm -23 OLD NEW` is **empty** for both presets → strict superset, **0 lost**. ✓

The canonical tool and the throwaway driver agree exactly; the throwaway 57/23 is validated.

---

## §2 — Hand-traced soft bucket (Step 2)

Method = the audit's §3.A: for each gate case open the actual pitch-class set our analyzer
saw (`pitch_class_set`), the WiR figure + local key, and the music21 `RomanNumeral` oracle
(root pc + chord pcs). Helper `C:\tmp\handtrace.py` / `classify.py` replicate the canonical
gate filter verbatim (it does **not** produce the gate count) and add the oracle + a
share-tone analysis. [probe]

### §2.0 — Every contested GT root oracle-verified
For all **57 Baroque + 23 Jazz** cases, `RomanNumeral(wir_figure, local_key).root().pitchClass`
**== the gate's `dcml_root`** — **80/80, 100 % agreement [oracle]**. The ground truth the
re-baseline pins is correct on every case (consistent with the parser's 99.97 % corpus-wide
oracle check). The half-dim sigil (`vii/o7`, `vi/o7`), compound applied figures
(`viio7/V`, `viio6/4/iv`, `V2/IV`) and minor-key cased degrees all resolve cleanly.

### §2.1 — Refined classification of the +44 / +16

Buckets (by **sonority structure**, not our label):

| bucket | meaning | adjudicable? |
|---|---|---|
| **dim7-symmetric** | we hear a full {r,r+3,r+6,r+9}; our root is a rotation (labelled dim *or* rootless V7♭9) | **NO** — pitch-class unresolvable |
| **viio-share-tone** | WiR leading-tone dim *triad/incomplete-7th*, we read an inverted dominant/major sharing ≥3 tones, GT root present | NO — defensible alternate |
| **relative-sus-incomplete** | G6≡Em7, sus-over-tonic, vi-vs-I, Δ=+7a chord-tone reading | NO — defensible alternate |
| **GENUINE** | GT root absent from the sonority, or our nominal root absent over a non-dim chord (applied-dom under-read), or ≤1-tone overlap | **YES — actionable** |

**Baroque +44** [probe, each root [oracle]]:

| bucket | count | % |
|---|---|---|
| dim7-symmetric (unresolvable) | 30 | 68 % |
| viio-share-tone | 11 | 25 % |
| relative-sus-incomplete | 1 | 2 % |
| **GENUINE (actionable)** | **2** | **5 %** |

→ **42 ambiguity (95 %) / 2 genuine (5 %)**.

**Jazz +16** [probe]:

| bucket | count | % |
|---|---|---|
| dim7-symmetric (unresolvable) | 6 | 38 % |
| viio-share-tone | 9 | 56 % |
| **GENUINE (actionable)** | **1** | **6 %** |

→ **15 ambiguity (94 %) / 1 genuine (6 %)** (matches the report exactly).

### §2.2 — The genuinely-actionable NEW cases (firmed-up count)

| case | preset(s) | WiR (oracle root) | our reading | why genuine |
|---|---|---|---|---|
| **bwv429@24240** | Baroque + Jazz | `V2/IV` /A → **A** [oracle] | E/G# (E major) | **GT root A absent** from our pcs `{D,E,G#,B}`; we read a clean E7; share 1/4. The one unambiguous new genuine. (Likely a beat-alignment/segmentation slice, not a vertical-scoring miss.) |
| **bwv10.7@36000** | Baroque | `V4/3/iv` /g → **G** [oracle] | Bb/C | our nominal root **Bb is absent** from the sonority `{C,D,Eb,F,G}`; GT root G *is* present but the applied dominant's defining 3rd (B) is absent (E♭ present), so it is a weakly-supported applied dom we under-read. |

**bwv227.7@18120** (report's 3rd Baroque-genuine) — I **reclassify as ambiguity/segmentation,
not a vertical miss**: our root G **is** sounding, and the region holds **7 distinct pcs**
(`{C#,D,E,F,F#,G,B}`) — a merged/over-grabbed segment, not a clean chord either side. GT
root C# (`V6/5/V`) [oracle] is present; share 3/4. The defect is segmentation (Stage-3
decoder territory), not a vertical root miss. Counting it as "actionable" is defensible, so
the Baroque-new actionable count is **2 (strict vertical) to 3 (incl. segmentation)**.

**Confirm/correct vs the report's first pass:** the report said ~3 Baroque / ~1 Jazz new.
I **confirm Jazz = 1** exactly, and **refine Baroque to 2 clear + 1 segmentation-borderline**
(= 3 if segmentation counts). The first pass holds; the only movement is bwv227.7 sliding
from "genuine" to "segmentation-ambiguity" — i.e. the actionable count is, if anything,
slightly *lower* than the first pass, not higher.

### §2.3 — Refinement of the report's bucketing (the substantive finding)

The report split the +44 as "dim7-rot **12** + viio↔V7 **29** + genuine 3", keying
"dim7-rot" on **our quality label** (Diminished/HalfDim). The hand-trace shows that is an
undercount of the unresolvable set: **~18 of the cases the report filed under "soft
viio↔V7" sit over an identical symmetric fully-diminished-7th sonority** — we just labelled
them as a *rootless V7♭9* (e.g. `bwv245.3@12480` we say `C7b9`, sounding pcs `{C#,E,G,Bb}` =
a symmetric dim7; WiR `viio7/V` root C# [oracle]). All 30 Baroque dim7-symmetric cases are
**share = 4/4** over a `{r,r+3,r+6,r+9}` set [probe]. By pitch class the root is undefined,
exactly as the prompt stipulates for the dim7-rotation class — so these need no per-case
tracing and are accepted as ambiguity. **Net: 68 % of the +44 (not the report's 27 %) is
the *hard*-unresolvable symmetric-dim7 class; only the 11 viio-share-tone (incomplete-LT)
cases were genuinely "soft", and every one of them traced to legitimate ambiguity** (GT root
present, ≥3 shared tones, defensible inverted-dominant/major reading — e.g. `bwv269@20640`
D/F# over the F#-dim triad; `bwv320@31680` D7/A over `viio6`).

---

## §3 — Net actionable, ratification recommendation, two-tier seed

### Net actionable error after re-baseline
| | original (audit §3.A) | new (this trace) | net |
|---|---|---|---|
| Baroque | ~7 | 2 (clear) – 3 (incl. seg) | **~9–10** |
| Jazz | ~3 | 1 | **~4** |

This **confirms the report's ~10 Baroque / ~4 Jazz**. (Note: a pure-vertical lens applied
uniformly would call even some *original* "genuine" cases ambiguity — e.g. the Δ=+7a
`bwv102.7`/`bwv261` are vertically 4/4-ambiguous and are actionable only as the known
Phase-E/Stage-5 reweighting target, not as vertical misses — so the *vertical* net floor is
lower still, ~4/2. Either accounting leaves the headline unchanged: **the quadrupling of the
gate count is 95 %+ legitimate ambiguity; new real errors number 1–3.**)

### Is 57/23 the right pin to enshrine? — YES
- It is a **strict superset** (0 lost) of the trusted 13/7 → no regression hidden by the move. [probe]
- Every added GT root is **oracle-correct** (100 %) → the additions are real gate cases the
  old parser bug was hiding in `all_differ`, not parser noise. [oracle]
- The added mass is **overwhelmingly unresolvable/defensible** (95 %+), so 57/23 as a
  *regression pin* is honest: a future change that drops one of these would still be caught,
  and the count won't drift from spurious causes.
- Reproduced through the **canonical** tool at HEAD on a manifest-validated 353/353 corpus —
  the staleness and driver-provenance concerns are both closed.

### Two-tier / spelling-aware sub-class (note only — do NOT build)
The **symmetric fully-diminished-7th** cases (**30/57 Baroque ≈ 53 %**, **6/23 Jazz ≈ 26 %**;
all share = 4/4 over `{r,r+3,r+6,r+9}`) are **root-ambiguous by pitch class by construction**
and can only be adjudicated by **spelling** (which note is the notated leading tone). They
are the natural seed of a two-tier gate: a *hard* pin (the ~9–10 / ~4 actionable + the
defensible-incomplete cases) versus an accepted *structurally-unresolvable* sub-class
(symmetric dim7). A spelling-aware root comparator would be the follow-on that could
adjudicate them — recorded as a Stage-5/6 input, not built here.

---

## §4 — Constraints honored / process

- **READ-ONLY + corpus regen only.** Metric-batch fixes remain **STAGED/HELD** — no new
  commit. Staged blob hashes of `dcml_parser.py` / `compare_analyses.py` /
  `rerun_dcml_comparison.py` are **byte-identical** before and after the temporary
  OLD-parser A/B (verified via `git rev-parse :path` + `git hash-object`). [probe]
- **CLAUDE.md / STATUS.md NOT edited** (the 13/7→57/23 rewrite is Cowork's). [probe]
- **No production/engraving change** (P3 out). Corpora regenerated at HEAD `bcd4319aa7`
  (353/353, manifest-stamped) — the only intended side effect, permitted by the mandate.
- **No stop-condition triggered:** canonical reproduces 57/23 (no driver disagreement); both
  regens 353/353 (manifest guard passed); the hand-trace does **not** materially flip the
  actionable count (≈9–10 / 4, confirming the report).
- Throwaway helpers (`C:\tmp\handtrace.py`, `C:\tmp\classify.py`) reuse the canonical
  `characterise_bir_false`/`compare_analyses`/`dcml_parser` machinery verbatim; music21
  9.9.1 `roman.RomanNumeral` is the root oracle. Every number [probe], every root [oracle].

---

## §5 — Default (user-run config): 14 → 57 through the CANONICAL tool

*CC, 2026-06-13, same READ-ONLY+regen regime at HEAD `bcd4319aa7`. Closes the third gate
identity (CLAUDE.md line 108: **Default = 14 = Baroque-13 ∪ {bwv187.7}**) so Cowork can rewrite
the whole gate section as one coherent change. The corrected parser moves Default the same way
it moved Baroque/Jazz; the new number is **measured, not guessed.***

### §5.0 — TL;DR
**Default: 14 → 57, strict superset (0 lost), and the move is the *same* correction already
ratified for Baroque.** The NEW Default-57 set is **55-of-57 identical to the oracle-vetted
Baroque-57**; the only Default-specific delta is a single segmentation-tick shift of the
already-characterized `bwv227.7` over-grab case. No new error class, no new actionable error.
**Recommendation: pin Default = 57** alongside Baroque 57 / Jazz 23.

### §5.1 — OLD Default = 14 reproduced (HEAD/pre-fix parser, canonical tool)
- `Default` is a real `--preset` (`run_bach_preset.PRESET_CHOICES`, line 48): it reproduces the
  live product out-of-box config (registered mode-prior defaults + untouched
  `ChordAnalyzerPreferences`), distinct from the `Standard` tuning preset. [code]
- Regenerated `tools/corpus/default` at HEAD: **353/353 complete**, `corpus_manifest.json`
  stamped **`bcd4319aa7` = HEAD** (was `a652dc1ba7`, 3 behind). Manifest guard satisfied. [probe]
- A/B as in §1: reverted **only the worktree** (`git restore --source=HEAD --worktree`) of
  `dcml_parser.py`+`compare_analyses.py` to their HEAD blobs (index/staged corrected blobs
  untouched), ran the **canonical** `characterise_bir_false.py --corpus-dir tools/corpus/default`
  → **exactly 14**, then `git restore` from index. Worktree blobs of all three staged tools
  verified **byte-identical** to the staged blobs afterward (`2db84ba9…` / `c27c7ddb…` /
  `16d46831…`); `git status` = `M ` (staged-only, no unstaged residue). [probe]
- **OLD Default-14 identity set** (stem@tick) =
  `{bwv102.7@17520, bwv14.5@8160, bwv17.7@46080, bwv174.5@6240, bwv187.7@19200,
  bwv245.17@4800, bwv245.40@51360, bwv261@33840, bwv269@20640, bwv301@960, bwv381@4800,
  bwv422@23040, bwv432@5520, bwv45.7@20160}`. This is **Baroque-13 ∪ {bwv187.7@19200}** — the
  exact CLAUDE.md identity. The `bwv187.7` tick is **19200** (CLAUDE.md's prose "m14.b2";
  recorded actual = `bwv187.7@19200`). ✓ [probe]

### §5.2 — NEW Default = 57 (staged corrected parser, canonical tool)
`characterise_bir_false.py --corpus-dir tools/corpus/default` (corrected parser in worktree)
→ **57 genuine BIR=false**, identity set (stem@tick): [probe]
```
bwv10.7@36000  bwv102.7@17520 bwv122.6@6720  bwv14.5@8160   bwv144.6@15360 bwv144.6@16320
bwv151.5@13440 bwv153.1@18240 bwv16.6@16800  bwv169.7@24960 bwv17.7@46080  bwv174.5@6240
bwv187.7@19200 bwv20.11@13440 bwv227.7@18000 bwv244.32@5760 bwv244.46@960  bwv245.15@13920
bwv245.17@4800 bwv245.37@13920 bwv245.3@12480 bwv245.40@51360 bwv258@10560  bwv261@33840
bwv269@20640   bwv272@4800    bwv272@8160    bwv282@9120    bwv289@21600   bwv300@13440
bwv301@960     bwv309@8640    bwv320@31680   bwv334@5280    bwv334@6720    bwv336@8640
bwv342@25440   bwv352@1440    bwv358@6000    bwv364@2880    bwv381@4800    bwv392@14400
bwv40.3@2400   bwv402@22080   bwv416@10080   bwv421@2880    bwv422@23040   bwv423@28320
bwv429@24240   bwv432@5520    bwv45.7@20160  bwv48.3@2880   bwv57.8@15360  bwv64.8@5280
bwv77.6@22080  bwv94.8@24960  bwv96.6@13440
```

### §5.3 — Strict superset / 0-lost (through the same canonical tool)
| config | OLD (HEAD parser) | NEW (staged parser) | lost | added |
|---|---|---|---|---|
| **Default** | 14 | 57 | **0** | 43 |

`comm -23 OLD_default NEW_default` is **empty** → OLD-14 ⊆ NEW-57, **0 lost**. ✓ [probe]
No stop-condition: OLD reproduces 14, regen is 353/353, nothing lost.

### §5.4 — The 43 additions are the Baroque correction, not a new Default story
Cross-diff **NEW Default-57 vs the oracle-vetted NEW Baroque-57** (§1–§3): [probe]
- **55 cases shared** (identical stem@tick).
- **Default-only** = `{bwv187.7@19200, bwv227.7@18000}`.
- **Baroque-only** = `{bwv227.7@18120, bwv60.5@30960}`.

Of the **43 Default additions** (NEW-57 minus OLD-14), **42 are byte-identical (stem@tick) to
cases already in the oracle-vetted Baroque-57** — i.e. 100 % oracle-correct GT root and already
bucketed at 95 % ambiguity (symmetric-dim7 / viio-share-tone) in §2. Only **one** addition is
not already in the vetted Baroque set: **`bwv227.7@18000`**. `bwv187.7@19200` is Default-specific
but it was already in OLD-14 (not an addition). So the entire Default re-baseline reduces to
**"the ratified Baroque +44 correction, minus `bwv60.5`, plus one segmentation-tick variant of
`bwv227.7`."**

### §5.5 — Spot-check of the single Default-specific addition `bwv227.7@18000`
- **GT root oracle-correct.** WiR region: `global_key=e`, `local_key=b`, label `V6/5/V`,
  parser `root_pc=1 (C#)`. Under the verify report's method (full applied figure + local key),
  `roman.RomanNumeral('V6/5/V', Key('b')).root().pitchClass == 1 (C#)` — **matches** the gate's
  `dcml_root` and music21's *independent* vertical label (`.music21.json` = "C# half-diminished
  seventh chord", root C#). ✓ [oracle] *(Caveat, honestly noted: the **bare** `RN('V6/5', Key('b'))`
  and the global-key `RN('V6/5/V', Key('e'))` both resolve to F# — the documented WiR applied-figure
  parser subtlety [[project_functional_residual_oq1]]. Under the consistent chord_symbol+local_key
  method the report uses, the root is C# and the case is oracle-correct.)*
- **Not a new class — it is the segmentation/over-grab borderline already flagged in §2.2.**
  Our reading `G6/E` (G major, root G) over a **7-pc over-grabbed segment**
  `{C#,D,E,F,F#,G,B}`; the GT `C#ø7 = {C#,E,G,B}` is **fully present** (share 4/4 on the GT
  tones), GT root C# present. This is the *same chorale region* as the Baroque
  `bwv227.7@18120` that §2.2 reclassified as "segmentation-ambiguity, not a vertical miss" —
  reproduced under the Default preset's segmentation at tick 18000 vs Baroque's 18120. It carries
  a viio-share-tone flavor (our G-major shares ≥2 tones with the C#ø7) but the dominant defect is
  the merged-segment over-grab. **No new error class; not a clean new actionable error.** [probe]

### §5.6 — Recommendation
**Pin Default = 57.** It is a strict superset of the trusted 14 (0 lost), 42/43 additions are
the *already-ratified, oracle-correct, 95 %-ambiguity* Baroque correction, and the lone
Default-specific addition is the previously-characterized `bwv227.7` segmentation borderline
(oracle-correct GT root C#). The three-identity gate becomes **Baroque 57 / Jazz 23 / Default
57** (full Default identity set above for Cowork's CLAUDE.md/STATUS.md rewrite). All numbers
[probe], all roots [oracle]; no commit, no production change, parser fixes remain STAGED/HELD.
