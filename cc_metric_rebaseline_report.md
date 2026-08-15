# Coordinated Metric Re-Baseline — P0/P1/P2/P4/P5 (tools-only)

*CC, 2026-06-13. Base `a4ae4a9203`+ (HEAD `bcd4319aa7`; the intervening commit is a
read-only docs erratum). Fixes the TOOLS-side measurement corruption found by
`cc_measurement_pipeline_audit.md` (P0/P1/P2/P4/P5). **P3 (engraving mode-drop, key axis)
is OUT of scope — it rides with the held Stage-4 work.** No production/engraving file
touched. **Status: HELD — `git add` ok, NOT committed.** Per the user's 2026-06-13
decision (Option 2: "report only"), this run does **not** re-pin metric tests, does **not**
edit the CLAUDE.md/STATUS.md gate identities, and does **not** propose the commit.*

Evidence tags: **[probe]** ran a script; **[oracle]** verified against music21 9.9.1
`roman.RomanNumeral`; **[code]** quoted source.

---

## §0 — TL;DR

All four tools-side defects are fixed and **oracle-verified**. The cross-corpus precision
numbers moved as a coherent re-baseline (GT volume ×2.40, per-ours root_agree +14.9pp). **P4
was resolved as a real fix, not a quarantine** (`quarterbeats_all_endings`). **The one
result that contradicts the audit's prediction — and the reason this stays HELD — is that
the BIR 13/7 gate MOVED: Baroque 13→57, Jazz 7→23.** The move is a *strict superset* (0
lost), and the +44/+16 added cases are **93–94 % the same legitimate-ambiguity families
the audit already flagged** (diminished-7th root rotation, viio↔V7 share-tones) — so the
genuinely-actionable error count barely changed (~10 Baroque / ~4 Jazz). The old 13/7 was
an *undercount* caused by the very parser bugs this run fixes.

| # | Fix | Where | Verified |
|---|---|---|---|
| P0 | Fractional-onset drop → `Fraction` parse, keep all rows, align by `qb·480` | `dcml_parser.parse_abc_harmonies_file`, `compare_analyses._dcml_time_spans` | GT ×2.40 [probe] |
| P1 | rntxt applied `/X` rooted in local key → resolve tonicized target first | `dcml_parser.parse_rntxt_file` (+ overloaded-slash fix) | applied 88.6→99.9 % [oracle] |
| P2 | minor-key `viio`/`vio` rooted a semitone flat → case-based LT/submediant raise | `_compute_root_pc` **and** `_resolve_dcml_key` (both paths) | TSV 99.47 %, rntxt 99.97 % [oracle] |
| P4 | ABC/Beethoven repeat offset → align on `quarterbeats_all_endings` | `parse_abc_harmonies_file` default column | beethoven 48.2→60.3 %, every repeat-movement up [probe] |
| P5 | stale-default trap + downbeat-only denominator hidden | `rerun_dcml_comparison.py` defaults + freshness guard + coverage note | guard fires [probe] |

---

## §1 — The fixes (approach + the root-source choice justified)

### P0 — fractional-onset drop (the dominant lever)
`parse_abc_harmonies_file` parsed `mn_onset` with `float()`; the TSV stores whole-note
fractions (`"1/4"`, `"9/2"`, `"23/4"`), so `float("1/4")` raised `ValueError`, caught by a
bare `except: continue` that silently discarded **58.9 %** of all annotations (every
off-downbeat row). Fix: a `_parse_fraction` helper parses with `fractions.Fraction`; **all
rows are kept**; each region carries `abs_tick = round(Fraction(quarterbeats)·480)` and the
comparator (`_dcml_time_spans`) aligns by that exact tick instead of the measure-anchor
reconstruction (which only ever saw the surviving downbeats and ballooned each span to a
whole measure). The bare except is **narrowed** to `(ValueError, KeyError, ZeroDivisionError)`
and every still-skipped row is recorded to an optional `skipped` list / printed to stderr —
no silent drops. Deliberate rests (`.`, `~`, `@none`, empty numeral) are not counted as
skips. *Result:* GT volume **37,886 → 90,851 (×2.40)** — exactly the audit's prediction
[probe].

### P1 — rntxt applied `/X` (root correctness)
`parse_rntxt_file` rooted the primary numeral of an applied chord in the **local** key
(`primary = numeral.split('/')[0]`), so `V/vi` in B♭ was rooted F instead of the true D
(audit: 877/880 applied rntxt rows mis-rooted, 0.3 % oracle agreement). Fix: resolve the
tonicized target's absolute key **before** rooting, exactly as the TSV path does via
`relativeroot`. **Additional bug found in tracing:** the WiR rntxt slash is *overloaded* —
it marks tonicization (`V/vi`) but also figured-bass inversions (`V6/5`, `4/3`) and the
half-diminished sigil (`vii/o7`). A naive `partition('/')` mis-split `V6/5/iv` into
(`V6`, `5/iv`). New helper `_split_rntxt_applied` treats the trailing slash-segment as a
tonicization target **only when it is a bare Roman-numeral degree** (`_RNTXT_TARGET_RE`),
otherwise the slash belongs to a figure. *Result:* rntxt applied-chord oracle agreement
**88.6 % → 99.9 %** [oracle].

### P2 — minor-key leading-tone / submediant (root correctness)
`_DEGREE_SEMITONES_MINOR = [0,2,3,5,7,8,10]` rooted `viio` at tonic+10 (subtonic) not +11
(leading tone), and `vio` at +8 not +9. Fix grounded in the music21 oracle [probe]: in a
minor key, **case disambiguates** degrees 6 and 7 — lowercase `vi`/`vii` are the raised
forms (+9 / +11, harmonic-minor leading-tone), uppercase `VI`/`VII` the natural forms
(+8 / +10); the explicit `#`/`b` prefix is applied on top of the cased value (so `#vio`→+10,
`#viio`→+0, matching music21). Applied to **both** code paths the audit named: `_compute_root_pc`
(direct rooting) **and** `_resolve_dcml_key` (so an applied chord like `V7/vi` or `V/vii` in
a minor key tonicizes the correct, non-flat key).

**Root-source choice (the audit's explicit call): the deterministic port, not a music21
runtime dependency.** I kept the parser self-contained (Fraction + relativeroot + raised-7
case rule) and **verified it against the music21 `roman.RomanNumeral` oracle** rather than
calling music21 at runtime. Justification: (1) the metric stays dependency-free and fast
(no per-row RomanNumeral construction over ~100k rows); (2) the oracle check below shows the
deterministic rule reproduces music21 to 99.5–100 % on well-formed figures, so the runtime
dependency would buy nothing; (3) it keeps the parser's existing structure (the TSV
`relativeroot` path the audit said is correct and must not be touched stays intact).

**Oracle agreement (the correctness check):**
- **TSV path** (corelli, mozart, chopin, grieg, schumann, tchaikovsky, dvorak): **99.47 %
  (42,680 / 42,908)**. The 228 residual disagreements are *entirely* out-of-scope
  representational gaps: 112 augmented-sixths (`It6`/`Fr6`/`Ger6` — audit L3.4, a known
  small music21-vs-DCML gap), 115 two-level applied (`V/V/V`, single-level resolution like
  the TSV path), and **1** double-sharp chromatic edge (`##vio`). [oracle]
- **rntxt path** (Bach gate, 326 chorales): **99.97 % (18,322 / 18,327)**; applied
  88.6→99.9 %, minor-key 99.9 %. The 5 residual are 2 `It6` + 3 multi-level applied. [oracle]

### P4 — ABC/Beethoven structural offset (**resolved, not quarantined**)
On repeat-bearing ABC movements the plain `quarterbeats` runs bars ahead of our ticks (it
elides first-ending material); a naive `quarterbeats` correction made Beethoven ~12pp worse.
**Root cause + fix:** our reading is repeat-*unexpanded* (no `expandRepeats` anywhere), so it
contains every written ending once — which is exactly what the **`quarterbeats_all_endings`**
column counts. Adopting it as the default `abs_onset_col`:
- recovers **every one of the 29 repeat-bearing Beethoven movements** (e.g. n13op130_06
  25.6→64.7 %, n05op18-5_01 42.9→73.5 %); Beethoven overall **48.2 → 60.3 %** [probe];
- is **byte-identical** on movements without repeats (the two columns are equal there), so
  the dvorak/corelli/tchaikovsky numbers are unchanged (+0.0) and chopin/mozart/schumann/
  grieg/bach_suites repeat-movements also improve;
- **no corpus regresses.**

This is strictly better than the audit's sanctioned quarantine fallback: zero movements are
excluded; the offset is repaired at the source coordinate. (A per-row fallback to the other
quarterbeats column guards against a sparsely-populated cell.)

### P5 — reporting hygiene (`rerun_dcml_comparison.py`)
- **Defaults repointed** from the stale `live_20260515` / `live_20260515_bach` (pre-Stage
  1/2/3, ~5pp low — the audit L1.2 accidental-measurement trap) to the HEAD-stamped
  `live_head_verify`.
- **Stale-hash guard** `_check_corpus_freshness`: reads each corpus report's recorded
  `git_hash`, compares to `git rev-parse HEAD`, prints a prominent multi-line warning on any
  mismatch (and `--strict-hash` hard-fails for CI; `--allow-stale-hash` suppresses). Verified:
  warns on the current 1-commit-behind corpus, `--strict-hash` exits nonzero [probe].
- **Coverage honesty** (audit L6.1): a header line states the DCML-anchored denominator is
  now the FULL annotation set (~2.4× the old downbeat-only count), so a reader cannot mistake
  the post-fix denominator for the old one.

*(The stale 53.8 %/54.4 % STATUS/MEMORY headline is corrected to the post-fix number in §2
below; per the "report only" decision I did not edit STATUS.md/MEMORY in this run.)*

---

## §2 — The re-baseline table (before → after)

**Cross-corpus weighted aggregate** (`rerun_dcml_comparison.py`, `live_head_verify`, 520
movements over the 9 scoreable corpora; cpe_bach excluded both sides as before) [probe]:

| Figure | BEFORE (HEAD parser) | AFTER (corrected) | Δ |
|---|---|---|---|
| DCML annotations (denominator) | 37,886 | 90,851 | **×2.40** |
| Coverage (resolved / total) | 37,640 (99.4 %) | 90,730 (99.9 %) | full set |
| **per-DCML root_agree** | **54.4 %** (20480/37640) | **50.3 %** (45633/90730) | **−4.1 pp** |
| **per-ours root_agree** (time-overlap) | **49.3 %** (30620/62110) | **64.2 %** (39877/62129) | **+14.9 pp** |
| per-ours rn_agree | 33.2 % (20599/62110) | 40.4 % (25081/62129) | +7.2 pp |
| per-DCML rn_agree | 36.6 % (13764/37640) | 34.2 % (30994/90731) | −2.4 pp |

Reading: the **per-ours** view (does each region we emit match GT?) jumps **+14.9pp** — the
old downbeat-only GT was ballooning spans and mis-scoring our correct within-measure regions.
The **per-DCML** view (does each GT annotation get matched correctly?) dips **−4.1pp** because
we now score 2.4× more annotations, including dense sub-beat ones our coarser regions don't
all hit. Both directions are honest; the de-inflation is the point.

**Note on the audit's −7.7pp prediction:** the audit estimated per-DCML 54.4→46.7 % using a
*naive* `quarterbeats` correction that regressed Beethoven. My P4 fix (`all_endings`)
recovers Beethoven instead, so the corrected per-DCML lands at **50.3 %**, above the audit's
beethoven-penalized lower bound — i.e. the real number is better than the audit's worst case.

**Per-corpus root_agree** (`compare_rn.py --cross-corpus`, per-ours) [probe]:

| corpus | BEFORE | AFTER | Δ | note |
|---|---|---|---|---|
| dvorak | 59.3 % | 72.2 % | +12.9 | no repeats |
| chopin | 58.5 % | 72.4 % | +13.9 | |
| corelli | 45.1 % | 74.6 % | +29.5 | float-drop dominated |
| mozart | 48.1 % | 58.8 % | +10.7 | |
| schumann | 52.0 % | 74.9 % | +22.9 | |
| tchaikovsky | 46.2 % | 62.5 % | +16.3 | no repeats |
| grieg | 50.9 % | 60.9 % | +10.0 | |
| **beethoven** | **48.2 %** | **60.3 %** | **+12.1** | **P4 corrected (all_endings), not quarantined** |
| bach_suites | 46.8 % | 62.6 % | +15.8 | |

Every corpus improves on the per-ours metric. **Beethoven's P4 disposition: corrected, not
quarantined** (0 movements excluded).

---

## §3 — Corrected headroom direction (full re-derivation deferred)

The audit (§4) said the headroom dossier's **"95.2 % functional / 4.8 % vertical"** split is
materially inflated by P0+P1+P2 and must be re-derived on the corrected metric. The cheap
directional read from this run:

- Cross-corpus **per-ours root_err fell from 50.7 % → 35.8 %** (= 100 − root_agree) — i.e. a
  large share of what was counted as "vertical" root error was a *parser/alignment artifact*,
  not an analyzer error.
- On the **Bach gate** specifically (the dossier's evidence base), the vertical residual that
  survives correct GT is the 57/23 set — of which **§5 shows 93–94 % is legitimate
  diminished-7th/viio ambiguity**, not actionable vertical error. So the "4.8 % vertical"
  figure was both *inflated by the artifacts* (corelli −29.5pp etc.) and *over-attributed to
  error* (most of the surviving residual is ambiguity).

The full functional-vs-vertical RE-decomposition and the OQ-1 re-derivation are, per the
mandate, a **separate follow-on on the corrected metric** (the corrected parser was the
prerequisite, now in place). Not produced here.

---

## §4 — Re-pin ledger (NO re-pin performed; status documented)

Per the user's decision, **no metric test was re-pinned and no test was added.** The
empirical status, for the eventual accept-path:

- **`tools/tests/test_metric_scripts.py` (70 tests) + `test_metric_primitives_l0l1.py` (21
  tests) + `test_dcml_parser.py`: all green, unchanged** [probe: `python -m unittest
  discover` → `Ran 91 tests OK`; parser test `OK`]. The existing tests pin *comparator*
  behavior with synthetic `D()`/`R()` builders that supply `root_pc` directly, so they are
  structurally insulated from the parser-internal root changes — the anticipated breakage did
  not occur.
- **Recommended NEW tests for the accept-path** (additions, not re-pins): (a) a fractional
  `mn_onset="1/2"` row is KEPT not dropped; (b) rntxt-vs-TSV applied-root equivalence
  (`V/vi` ⇒ same pc both paths); (c) minor-LT root (`viio` in minor ⇒ +11; `vio` ⇒ +9;
  `#viio`⇒+0); (d) `abs_tick == round(Fraction(quarterbeats)·480)` exactness; (e) the
  overloaded-slash split (`V6/5/iv` ⇒ ('V6/5','iv'), `vii/o7` ⇒ ('vii/o7','')). Each would
  carry the marker `# re-pinned 2026-06-13: metric re-baseline (audit P0/P1/P2/P4)`.

---

## §5 — THE GATE FINDING (insulation hypothesis falsified)

The audit predicted "the 13/7 gate does NOT move (already clean)." **It moves.** Re-running
`characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz}` against the corrected
parser:

| preset | BEFORE | AFTER | lost | added |
|---|---|---|---|---|
| Baroque | **13** | **57** | **0** | **44** |
| Jazz | **7** | **23** | **0** | **16** |

Both are **strict supersets** — every original case is preserved (0 lost), confirmed by
set-diff of the gate identity (`stem@tick`) computed with the old vs new parser [probe].

**Mechanism.** The gate is `three_way_classify == 'music21_dcml_agree'` (music21's
note-analysis root == WiR root) ∧ winner `bassIsRoot==False` ∧ `classify==chord_disagree`.
The audit's insulation argument was that the filter *requires* `music21_root == wir_pc`, so a
parser-corrupted `wir_pc` is admitted only if music21 coincides with it. That is true for the
13 cases that were *present* — but it missed the **false negatives**: the P1/P2 bugs corrupted
the WiR root of every applied / minor-LT chord, pushing them into `all_differ` (parser ≠
music21), which the gate *discards*. With the WiR root now oracle-correct (99.97 %), music21's
independent note-analysis agrees with it and our analyzer differs → these surface as gate
cases. So the old 13/7 was an **undercount**: the parser bug was hiding ~44 + 16 genuine
*candidate* errors from the project's primary regression pin.

**This is why the run is HELD.** Re-baselining the project's central gate (CLAUDE.md/STATUS.md
hard-code the 13/7 identity sets and the "BIR=false increase = hard stop" workflow) is a
project-level decision for Cowork sign-off.

### §5.1 — First-pass triage of the +44 / +16 (the audit's §3.A lens)

The audit found ~46 % of the original 13 was legitimate ambiguity (V7↔viio, G6≡Em7,
sus-over-tonic). Applying the same lens to the added cases — keyed on chord structure, not
sampling [probe] — the added cases are **even more ambiguity-dominated**, because the bug
specifically corrupted `viio`/applied roots, and those are exactly the chords with inherent
root ambiguity:

| preset | added | AMBIGUITY | genuine / lean-genuine |
|---|---|---|---|
| Baroque | 44 | **41 (93 %)** | 3 (7 %) |
| Jazz | 16 | **15 (94 %)** | 1 (6 %) |

Ambiguity breakdown (Baroque): **dim7-rotation 12** (our root is a minor-3rd rotation of the
WiR root within the *same symmetric fully-diminished-7th* — all four notes are equally valid
roots by pitch alone; e.g. bwv144.6@16320 WiR `viio4/3` root B♭, we root the same {B♭,D♭,E,G}
on D♭, Δ=+3); **viio↔V7 share-tones 29** (WiR is a leading-tone diminished, we read a
major/dominant/sus sharing 3 of 4 tones — the audit's V7↔viio family; e.g. bwv245.3@12480 WiR
`viio7/V`, we read C-major sharing E,G). **Only 3 Baroque cases are genuinely actionable**,
all *applied-dominant* mis-roots where the GT root is weakly or not supported in our reading:
`bwv429@24240` (WiR `V2/IV`, GT root A **absent from our pc-set** — the one clear genuine),
`bwv10.7@36000` (`V4/3/iv`), `bwv227.7@18120` (`V6/5/V`). Jazz: 1 genuine (`bwv429@24240`).

**Net actionable error after re-baseline:** original ~7 Baroque / ~3 Jazz (audit) + new ~3 / ~1
= **~10 Baroque / ~4 Jazz**. The gate *count* quadruples, but the genuinely-actionable signal
barely moves — the +44/+16 are overwhelmingly the diminished-7th-rotation and viio↔V7
ambiguities that pitch-class-root agreement can never resolve.

### §5.2 — Full enumeration of the added cases

**Baroque +44** (`stem@tick  WiR  our_root/quality → dcml_root  Δ  triage`):

```
bwv10.7@36000    V4/3/iv     10/Major        ->  7  +3   genuine(applied-V)
bwv122.6@6720    viio7        7/Diminished   ->  1  +6   amb:dim7-rot
bwv144.6@15360   viio2        4/Minor        -> 10  +6   amb:viio-vs-V7
bwv144.6@16320   viio4/3      1/Diminished   -> 10  +3   amb:dim7-rot
bwv151.5@13440   viio7        2/Major        ->  3  +11  amb:viio-vs-V7
bwv153.1@18240   viio7/V      2/Major        ->  3  +11  amb:viio-vs-V7
bwv16.6@16800    viio7/iv     9/Major        ->  1  +8   amb:viio-vs-V7
bwv169.7@24960   viio7/vi     8/Diminished   ->  5  +3   amb:dim7-rot
bwv20.11@13440   viio7/V     10/Minor        ->  1  +9   amb:dim7-rot
bwv227.7@18120   V6/5/V       7/Major        ->  1  +6   genuine(applied-V)
bwv244.32@5760   viio        10/Major        -> 11  +11  amb:viio-vs-V7
bwv244.46@960    viio7/V      4/Major        ->  5  +11  amb:viio-vs-V7
bwv245.15@13920  viio7/V      2/HalfDim      ->  8  +6   amb:dim7-rot
bwv245.37@13920  viio7/V      3/HalfDim      ->  9  +6   amb:dim7-rot
bwv245.3@12480   viio7/V      0/Major        ->  1  +11  amb:viio-vs-V7
bwv258@10560     viio7/V     11/Diminished   ->  5  +6   amb:dim7-rot
bwv272@4800      viio7/V      2/Major        ->  3  +11  amb:viio-vs-V7
bwv272@8160      viio         2/Suspended4   ->  8  +6   amb:viio-vs-V7
bwv282@9120      viio7/ii     4/Major        ->  8  +8   amb:viio-vs-V7
bwv289@21600     vi/o7        4/Major        ->  8  +8   amb:viio-vs-V7
bwv300@13440     viio7/V      9/Major        -> 10  +11  amb:viio-vs-V7
bwv309@8640      viio7/V      9/Major        ->  1  +8   amb:viio-vs-V7
bwv320@31680     viio6        2/Major        ->  6  +8   amb:viio-vs-V7
bwv334@5280      viio6/4/iv   2/Minor        -> 11  +3   amb:viio-vs-V7
bwv334@6720      viio7/V      7/Diminished   ->  1  +6   amb:dim7-rot
bwv336@8640      viio4/3      6/Major        -> 10  +8   amb:viio-vs-V7
bwv342@25440     viio4/3     11/Diminished   ->  8  +3   amb:dim7-rot
bwv352@1440      vi/o7        9/Minor        ->  6  +3   amb:ranked-2nd
bwv358@6000      viio7/V      4/Major        ->  8  +8   amb:viio-vs-V7
bwv364@2880      viio7/V      7/Major        ->  8  +11  amb:viio-vs-V7
bwv392@14400     viio6/5      9/Diminished   ->  6  +3   amb:dim7-rot
bwv40.3@2400     viio7/V      0/Major        ->  1  +11  amb:viio-vs-V7
bwv402@22080     viio7        2/Diminished   -> 11  +3   amb:dim7-rot
bwv416@10080     viio7/V      4/Major        ->  8  +8   amb:viio-vs-V7
bwv421@2880      viio7/V      2/Major        ->  3  +11  amb:viio-vs-V7
bwv423@28320     viio7/V      0/Major        ->  1  +11  amb:viio-vs-V7
bwv429@24240     V2/IV        4/Major        ->  9  +7   GENUINE (GT root absent from our pcs)
bwv48.3@2880     viio4/3      9/Diminished   ->  6  +3   amb:dim7-rot
bwv57.8@15360    viio7/vi     0/Minor        ->  6  +6   amb:viio-vs-V7
bwv60.5@30960    vii/o7/V     6/Minor        ->  3  +3   amb:viio-vs-V7
bwv64.8@5280     viio4/3      6/Diminished   ->  3  +3   amb:dim7-rot
bwv77.6@22080    viio7/V      9/Major        ->  1  +8   amb:viio-vs-V7
bwv94.8@24960    viio7        4/Minor        -> 10  +6   amb:viio-vs-V7
bwv96.6@13440    viio7/V      7/Major        ->  8  +11  amb:viio-vs-V7
```

**Jazz +16:**

```
bwv144.6@15360   viio2        1/Diminished   -> 10  +3   amb:dim7-rot
bwv144.6@16320   viio4/3      1/Diminished   -> 10  +3   amb:dim7-rot
bwv245.15@13920  viio7/V      2/Minor        ->  8  +6   amb:dim7-rot
bwv245.37@13920  viio7/V      3/Minor        ->  9  +6   amb:dim7-rot
bwv272@8160      viio         2/Suspended4   ->  8  +6   amb:viio-vs-V7
bwv280@17280     viio6        4/Minor        ->  1  +3   amb:ranked-2nd
bwv282@9120      viio7/ii     2/Diminished   ->  8  +6   amb:dim7-rot
bwv301@1440      viio6       11/Minor        ->  8  +3   amb:viio-vs-V7
bwv313@14880     viio6        9/Minor        ->  6  +3   amb:ranked-2nd
bwv334@5280      viio6/4/iv   2/Minor        -> 11  +3   amb:viio-vs-V7
bwv342@25440     viio4/3     11/Diminished   ->  8  +3   amb:dim7-rot
bwv392@14400     viio6/5      9/Diminished   ->  6  +3   amb:dim7-rot
bwv429@24240     V2/IV        4/Major        ->  9  +7   GENUINE (GT root absent from our pcs)
bwv48.3@2880     viio4/3      9/Diminished   ->  6  +3   amb:dim7-rot
bwv64.8@5280     viio4/3      6/Diminished   ->  3  +3   amb:dim7-rot
bwv74.8@13920    viio6        4/Major        ->  8  +8   amb:ranked-2nd
```

(Triage is a structural first pass; a hand-traced confirmation per case — the audit's §3.A
method — is the natural follow-on before any 57/23 baseline is ratified.)

---

## §6 — Deviations, unknowns, stop-condition status

1. **STOP CONDITION TRIGGERED — BIR gate moved (§5).** Reported, not committed. Per the
   user's Option-2 decision the fixes stay staged/HELD; the gate re-baseline (13/7 → 57/23)
   awaits Cowork sign-off. The move is oracle-grounded (the WiR roots are 99.97 % correct) and
   a strict superset, so it is a *real* undercount-correction, not a regression — but it is
   the project's central pin, so it is the user's call.
2. **P4 resolved, not quarantined** (deviation from the audit's quarantine fallback, in the
   better direction): `quarterbeats_all_endings` fixes all 29 repeat-bearing Beethoven
   movements with zero exclusions and zero non-repeat regressions.
3. **P3 untouched** (out of scope by mandate — key axis, rides with Stage-4).
4. **Oracle residuals out of scope** (audit-acknowledged): aug6 `It6/Fr6/Ger6` (representational
   gap), multi-level applied (`V/V/V`, single-level resolution), 1 double-sharp `##vio`. Total
   <0.6 % of scoreable rows.
5. **No new tests added / no re-pin** (per decision); §4 lists the recommended additions.
6. **Headroom HEADLINE re-derivation deferred** (mandate: separate follow-on); §3 gives the
   direction only.
7. **`git diff --stat` is tools-only**: `tools/dcml_parser.py`, `tools/compare_analyses.py`,
   `tools/rerun_dcml_comparison.py`. (The COWORK_HANDOFF.md / STATUS.md / docs changes in
   the tree pre-date this session.) No production/engraving file touched [probe].

---

*Drivers (throwaway, `/tmp` and `C:\tmp`): `oracle_verify.py` / `oracle_bucket.py` /
`oracle_rntxt.py` (music21 oracle), `p4_probe.py` / `allcorp_probe.py` (qb vs all_endings),
`gate_ids.py` (gate identity set-diff), `triage.py` / `do_triage2.py` (case triage). The
metric machinery (`dcml_parser`, `compare_analyses`, `compare_rn`, `rerun_dcml_comparison`,
`characterise_bir_false`) was reused verbatim; music21 9.9.1 `roman.RomanNumeral` is the
true-root oracle.*
