# CC — Layer 3 / Increment B: the held-out ground-truth key/mode harness (READ-ONLY)

**Status:** COMPLETE. **READ-ONLY — no production code, no behavior change, no corpus regen.**
The only change is the `tools/` measurement harness (`tools/cc_layer3_keymode_baseline.py`, Python; reads
existing `*.ours.json` + WiR rntxt + runs `music21` over the WiR annotations in-memory). Production analysis
output (`composing`/`notation`/snapshots/BIR/oracle) is **byte-identical by construction** — no `.cpp`/`.h`
touched, no build run, no corpus regenerated (§5 confirmation below). Cowork verifies read-only + the
split/metric methodology (esp. that the headline numbers are held-out, not in-sample); user ratifies; then
push; then Increment C.

**Spec:** `cowork_layer3_keymode_impl_design.md` §2 (Increment B); done-criterion `cowork_layer3_keymode_design.md`
§6. **No-assume:** every claim below is confirmed at source this session (file reads + data dumps), not assumed.

---

## §0 — Headline (the decision-relevant numbers)

All headline numbers are the **HELD-OUT TEST split** (out-of-sample; `md5(stem)%100 < 20`), with the
**fixed extractor** and the **two-source unambiguous** definition (parser-concurrence ∧ no-modulation).

| | Baroque (test) | Jazz (test) |
|---|---|---|
| scorable regions | 2311 | 2222 |
| our-keyfail (**FIXED** extractor) | **0** | **0** |
| our-keyfail (legacy extractor, the caveat) | 18 | **960** |
| UNAMBIGUOUS (stable ∧ parser-concur) | 1301 (56.3%) | 1245 (56.0%) |
| **→ full (tonic+mode) match** | **87.3%** (1136/1301) | **61.5%** (766/1245) |
| AMBIGUOUS | 1010 | 977 |
| → top-1 / in-top-2 / neither | 9.9% / 37.5% / 52.6% | 18.9% / 21.0% / 60.1% |

**The two findings that matter:**

1. **Held-out ≈ in-sample → no memorization.** Baroque test full-match 87.3% vs train 84.8% (test even
   *higher*); Jazz test 61.5% vs train 67.3%. The small, non-systematic train/test gap confirms the §3.4
   audit mitigation: the resolver is tuned to the **BIR root gate, not to WiR key labels**, so there is no
   meaningful out-of-sample penalty. The done-criterion's out-of-sample requirement is now satisfiable.

2. **★ The Jazz "91.5%" was an artifact of dropping 39% of regions.** The legacy extractor silently rejected
   every modal label Jazz emits (3839 / 5948 regions = 39%); the surviving 61% were the plain maj/min readings
   that happen to coincide with functional GT — a **biased subset**. With the fix exposing the modal readings,
   the **true Jazz unambiguous full-match is 61.5% (test), not 91.5%.** The drop is dominated by **tonal-center
   displacement by a perfect fifth** (the modal "read the dominant/subdominant region as its own key"): of the
   479 Jazz test-split unambiguous misses, **224 (47%) read the GT key's dominant (V)** and **108 (23%) its
   subdominant (IV)** — together **69%** are P5-related rotations the major/minor functional GT cannot credit.
   This is the relative/rotation residual the L3 path is designed to attack (design §4.1), now measured at full
   coverage instead of hidden behind a parse drop.

---

## §1 — Ground-truth key/mode extraction (confirmed at source)

- **GT (local) key/mode per location** comes from the **When-in-Rome (DCML-lineage) Bach rntxt** local key,
  parsed by `dcml_parser.parse_rntxt_file` → `DcmlRegion.local_key` / `.global_key` (a `"d:"` token sets the
  prevailing local key; `find_wir_file` resolves the stem → `analysis.txt`). Parsed to `(tonic_pc, is_major)`
  by `compare_rn._dcml_key_tonic`. Coverage = **326/353** stems each preset; the 27 uncovered stems are never
  scored and never folded into a `/353` (reported explicitly).
- **Our side**: the per-region `key` string in `tools/corpus/<preset>/*.ours.json`, aligned to the WiR stream
  by the **same validated time-overlap aligner** `compare_analyses.align_dcml_regions`
  (`DEFAULT_DCML_MATCH_MODE`) that `compare_rn` uses.
- **On-disk `*.music21.json` is global-only — RE-VERIFIED this session.** Across all 353 stems / **29047
  regions**, the per-region `key` equals `keyGlobal` in **0** cases. It therefore cannot ground a *local*
  key/mode metric directly (confirms the audit). It is, however, the basis of the **second source** below
  (via the `music21` library re-parsing the WiR rntxt, not the static json).

## §2 — The unambiguous / ambiguous split (genuine two-source, with its limitation stated)

The audit used a **single-source proxy** (unambiguous ≈ WiR `local==global`). Per §2 of the instruction it is
**replaced with a genuine two-source concurrence where the data allows**:

- **Source 1** = our hand-rolled `dcml_parser` local key (above).
- **Source 2** = **`music21` 9.9.1's independent romanText parser** of the **same** WiR `analysis.txt`
  (`converter.parse(path, format='romanText')` → per-`RomanNumeral` `.key`), aligned by **exact (measureNumber,
  beat)**. Alignment is exact: across the corpus **m21-missing = 0** (every WiR location has a music21 reading),
  and music21 tracks local modulations (e.g. bwv245.15: A-minor → D-minor at m3).
- **`concur`** = the two parsers agree on the local key/mode at that location. **`stable`** = WiR `local==global`
  (no modulation). **UNAMBIGUOUS = `stable ∧ concur`.** **AMBIGUOUS = complement.**

The two axes are kept **separate on purpose** because each captures a different ambiguity:
the **parser-concurrence** axis catches encoding / applied-chord / modulation-boundary ambiguity (the two
implementations genuinely disagree on ~3–10% of regions — relative pairs and off-by-one-chord modulation
boundaries, e.g. `Bbmaj`↔`Gmin`, `Ebmaj`↔`Cmin`, boundary `Dmaj`↔`Emin`), and the **stable** axis catches the
modulation/tonicization ambiguity the same-annotation parser-concurrence cannot.

> **★ LIMITATION — stated, not hidden (instruction §2 / stop-condition §7).** Both sources parse the **one** WiR
> **human annotation**, so this is a two-**implementation** concurrence, **not** a two-**annotator** concurrence.
> The design's "DCML ∧ music21 agree" intended two *independent analyses*. For the **Bach chorale gate set that
> is impossible read-only**: `*.music21.json` is global-only (above) and there is **no Bach `harmonies.tsv` with
> a `localkey` column** — the chorales are WiR-rntxt-only (the on-disk `bach_en_fr_suites` TSVs are a separate
> keyboard corpus, not the 353-stem gate set). So the strongest honest split available read-only is
> "two parsers concur on the one annotation **AND** that annotation reports no local modulation." This is a
> **strict refinement** of the audit's stable-only proxy (it additionally removes the stable-but-parser-disagree
> regions), and it is reported alongside the stable count so the refinement is transparent. A true two-annotator
> split would require a second independent local annotation of the chorales (not on disk) — a corpus-acquisition
> step, not a read-only one (surfaced, not faked).

## §3 — The held-out split (out-of-sample)

No canonical WiR/DCML chorale train/test split is published, so the harness **defines a fixed, documented,
deterministic one**: `split_of(stem) = 'test' if md5(stem)%100 < 20 else 'train'` (md5, not Python's salted
hash → stable across runs/machines). **All headline numbers are the TEST split.** Train and `all` are reported
for context (and to expose any overfitting gap — there is none, §0.1). This addresses the audit's open item
("no held-out split yet") and the §6.3 done-criterion's out-of-sample requirement.

## §4 — The metric + the Jazz fix

**The metric** (design §4/§6), per scorable region, per preset, per split:
- **UNAMBIGUOUS** → full `(tonic, mode)` match (target ~100%; the real defect bar).
- **AMBIGUOUS** → **top-1 / in-top-2 / neither**. The resolver emits a ranked top-2 (`key` +
  `keyModeRunnerUp.key`); `in-top-2` = GT is the runner-up. The flagged-residual machinery is **Increment C**,
  so pre-C the ambiguous bar is reported as this measurable breakdown, **plus** a supplementary count of the
  `neither` regions the resolver already flags via low confidence (`keyConfidence < 0.20`) — Baroque 288/531,
  Jazz 532/587 of test `neither` are low-confidence, i.e. the resolver itself is already uncertain on the bulk
  of its ambiguous misses (a positive signal for the Increment-C confidence-bearing path).

**The Jazz parse fix.** Root cause (enumerated this session): `compare_rn._our_key_tonic`'s regex
`^([A-G])([#b]?)([a-z]+)$` has a **lowercase-only mode group**, so it rejects every CamelCase modal label the
analyzer emits. The full reject set (counts across baroque+jazz+default): `Mixolyd` (6710), `Dor` (5167),
`Lyd` (2874), `Mix♭6` (134), `PhrygDom` (103), `alt` (69), `Dor#4` (28), `Loc#6` (27), `Phryg` (17),
`Lyd#2` (16), `Dor♭2` (12), `Lyd♭7` (6), `Lyd+` (6), `Ion+` (1), `Loc#2` (1) — Jazz emits these on **39%** of
regions (the 3839 our-keyfail). The fix (`our_key_tonic_fixed`, **local to the harness — `compare_rn.py` is
untouched, so the BIR pipeline that depends on it stays byte-identical**) accepts any mode token
(case-insensitive, with accidental/figure suffixes) and colours it by the **tonic-triad third**: major if the
mode begins `maj/ion/lyd/mix/alt` or contains `dom` (phrygian dominant); minor otherwise (dorian, phrygian,
aeolian, locrian, harmonic/melodic minor). After the fix, **our-keyfail = 0** on both presets (it also recovers
the 83 Baroque + 3839 Jazz legacy keyfails). **Jazz numbers re-reported on the now-parseable full set**:
the honest unambiguous full-match is **61.5% (test)** — see §0.2 for why this is *lower* than the legacy 91.5%
(the 91.5% measured only the unrepresentative parseable subset).

## §5 — Gate (READ-ONLY) — confirmation

- **No production change.** Only `tools/cc_layer3_keymode_baseline.py` changed (a Python diagnostic). No
  `.cpp`/`.h` touched, **no build run**, **no corpus regenerated**. Therefore `composing`/`notation`/snapshot/
  BIR/oracle output is **byte-identical by construction** — there is nothing for it to differ from (the gate's
  "if any production metric moves → STOP" cannot trigger; no production metric was computed or could move).
- **Reproduces the audit baseline as a sanity anchor.** The harness recomputes the audit-config (OLD extractor,
  stable-only proxy, FULL corpus) inline and prints it: **Baroque 85.5% (5146/6021)**, **Jazz 91.5%
  (3492/3817)** — byte-for-byte the audit §3.3 numbers. The `--legacy-audit` flag also reruns the original
  report verbatim. The **delta** to the new headline is fully explained: (a) held-out test split instead of full
  corpus (small, non-systematic), (b) the parser-concurrence refinement of the unambiguous set
  (Baroque stable 1347 → unamb 1301; raises the match rate by removing parser-disagree regions), and (c) the
  Jazz parse fix (the large, deliberate Jazz drop, §0.2).
- **No corpus regen.** Reads existing `tools/corpus/<preset>/*.ours.json` + WiR annotations only.

## §6 — Re-running

```
# Increment-B harness (default): held-out, two-source, Jazz-fixed
python tools/cc_layer3_keymode_baseline.py
python tools/cc_layer3_keymode_baseline.py --json out.json    # machine-readable dump
python tools/cc_layer3_keymode_baseline.py --test-pct 25      # vary the held-out fraction
python tools/cc_layer3_keymode_baseline.py --legacy-audit     # the original audit baseline verbatim
```
(Requires `music21` for the second source — present, 9.9.1; ~0.25s/file, cached across presets.)

## §7 — Deliverables + what is NOT done (for Increment C)

**Delivered:** the extended `tools/cc_layer3_keymode_baseline.py` (committed locally, unpushed) + this report.

**Explicitly NOT done (Increment C, the rebuild):** the flagged-residual *machinery* (this harness only reports
the confidence-flag as a supplementary count); the modal-palette GT (Dorian/Mixolydian have no RN ground truth —
the design §6 scope caveat stands, and it is exactly the Jazz drop's cause); the two-**annotator** unambiguous
split (needs a second independent local annotation not on disk — §2 limitation). The Increment-C key-path
decoder is graded against **this harness's held-out unambiguous full-match** (must improve, esp. the
P5-rotation Jazz residual and the Baroque relative-pair misses) + the oracle KEY tier + dual-preset BIR.

---
*Sources read this session: `cowork_layer3_keymode_design.md`, `cowork_layer3_keymode_impl_design.md`,
`cc_layer3_keymode_audit_dossier.md`, `tools/compare_rn.py`, `tools/dcml_parser.py`,
`tools/compare_analyses.py`, `tools/cc_layer3_keymode_baseline.py`; data dumps over `tools/corpus/{baroque,jazz}`
and `tools/dcml/when_in_rome`. music21 9.9.1.*
