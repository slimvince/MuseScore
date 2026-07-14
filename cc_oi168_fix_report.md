# OI-168 — the signature-mask fix: adoption + correctness re-baseline

**Session:** CC, 2026-07-14. **Dispatch:** `cc_instruction_oi168_fix.md` (Cowork, 2026-07-13; user-ratified).
**Type:** inference-affecting **correctness re-baseline** on the governing hard stop (block (A)).
**Predecessor measurement:** `cc_oi168_magnitude_report.md` (the default-OFF A/B this fix promotes).

**Headline.** The fix is adopted and the re-baseline is clean: **Baroque and Default are byte-identical**,
**Jazz gains exactly one corrected chord**, the run-level set-diff is **removal-only**, and the hard stop
**strictly decreases** (`OVERALL: PASS`). Every prediction was met exactly.

**And a STOP.** The dispatch's closure statement — *"L4 is structurally tonic-independent"* — is **refuted**.
The fix makes the two key-consuming **scoring terms** tonic-independent, which is all it ever touched.
**Three further L4 sites answer the same collection question through the tonic** and carry the identical
defect on the identical population. **The collection/tonic split still does not hold** (§5, `OPEN_ITEMS.md`
OI-170). Separately, the Task-3 re-home was **stopped**: its stated premise is false at the code (§6, OI-171).

---

## 1. Premise Gate — predictions, recorded BEFORE the fix was built (#17b)

*(Written to this file before the source edit and before any regeneration. This is a **reproduce-check** and
is declared as such: the predecessor A/B ran the same predicate through the same binary, so anything other
than an exact reproduction would mean the promoted code is not the variant that was measured.)*

| quantity | prediction | actual | verdict |
|---|---|---|---|
| Baroque `.ours.json` changed | 0 / 352 | **0 / 352** | met |
| Default `.ours.json` changed | 0 / 352 | **0 / 352** | met |
| Jazz `.ours.json` changed | exactly 9, the named stems | **exactly 9, the named stems** | met |
| committed-chord flips, all presets | exactly 1 (`bwv145.5@12960`) | **exactly 1, that one** | met |
| flips outside the Altered regions | **0** (the load-bearing structural claim) | **0** | met |
| class-(b) root-disagree duration | Baroque +0, Jazz −480, Default +0 | **+0 / −480 / +0** | met |
| run-level set-diff | removal-only, one run, zero additions | **removal-only, one run, zero additions** | met |
| `robust_stop_diff.py` verdict | OVERALL PASS | **OVERALL PASS** | met |
| `pipeline_snapshot_tests` goldens to refresh | 0 | **0** (suite passes unrefreshed) | met |
| `composing_tests` / `notation_tests` | green, no test edit | **1103 / 53, green** | met |

The 9 Jazz stems, predicted and observed identical: `bwv135.6`, `bwv145.5`, `bwv187.7`, `bwv245.37`,
`bwv314`, `bwv353`, `bwv404`, `bwv60.5`, `bwv64.8`.

---

## 2. The change

Both key-consuming scoring terms now ask the key's **collection**, never its tonic:

```cpp
// dim7CharacteristicBonus  (chordanalyzer.cpp)
if (pcInMask(signatureMask, dim7Pc)) { return 0.0; }   // diatonic — no bonus

// diatonicRootContribution (chordanalyzer.cpp)
if (pcInMask(signatureMask, rootPc)) { return prefs.diatonicRootBonus; }
```

where `signatureMask = diatonicMaskFromFifths(keySignatureFifths)` — the repo's existing primitive whose
contract is *"Key-agnostic: depends ONLY on the notated signature, never a resolved mode"* (`analysisutils.h`).

**The dead parameters are gone.** Neither term takes `keyTonicPc` or `scale` any more. That is the point of
the change, not a tidy-up: the tonic-independence is now **structural** — there is no tonic in scope to get
it wrong — rather than an algebraic cancellation that a future mode-table edit could silently break, which
is exactly how OI-168 was born. `keyTonicPc`/`scale` remain in `analyzeChord` because a scale **degree** is
tonic-relative by definition; they are still consumed by the degree block and published on the snapshot.

**Also removed:** the `pcInKeyCollection` A/B predicate, the `MU_KEY_COLLECTION_SIGMASK_VARIANT` switch, and
the `…MembershipTests` / `…MembershipDiffers` counters. With the mode-transposed set deleted there is nothing
to switch against, and a "differs" counter would compare a set against itself and report a structural zero —
a false instrument (#19), not a measurement. The probe's population and Aeolian-guard counters are kept
(they still measure something real, and OI-167/OI-102 still want them).

**Doc sync (mandatory, same commit):** `docs/scoring_model.md` §4 — both term entries rewritten to state the
signature-collection contract, the defect they replaced, and a warning against reintroducing
`keyTonicPc + scale` for a membership test.

---

## 3. Verification at the objects (#15)

Corpus regenerated for all three presets (352/352 each) into a scratch tree and compared per-file by sha256
against the committed `tools/corpus/<preset>`:

| arm | Baroque | Jazz | Default |
|---|---|---|---|
| `.ours.json` byte-identical | **352 / 352** | 343 / 352 | **352 / 352** |
| differing | **0** | **9** | **0** |
| committed-chord flips inside the 24 Altered regions | 0 | **1** | 0 |
| committed-chord flips anywhere else | **0** | **0** | **0** |

Baroque and Default byte-identical is the **δ = 0 derivation verified at runtime on 704 scores**, not argued
on paper. Zero flips outside the Altered population is the load-bearing structural claim; a single one would
have refuted the derivation and been a STOP.

**The one flip, `bwv145.5@12960` (m10 b1), local key `D#alt`.** Sounding notes, with their notated spelling:
D♯3 (bass) · F♯3 · B4 — a **B-major triad in first inversion**.

| | committed chord | root | score |
|---|---|---|---|
| before | `Ebm` (roman `i`) | pc 3 | 1.830 |
| after | `B/Eb` (roman `bVI6`) | **pc 11** | 1.900 |

The old reading was not a rival rotation — **it named a chord the notes do not contain** (E♭ minor needs a
B♭; the sounding B is not one of its chord tones). Under `D#alt` the corrupted collection was the D♯-major
set (contains D♯, excludes B) while the signature's actual collection is D major (contains B, excludes D♯),
so the +0.30 diatonic-root bonus went to the wrong root by exactly the semitone transposition OI-168 derives.
**Both oracles back the new reading:** music21 gives root 11, and the DCML ground truth already listed this
region as a class-(b) root **failure** (`bwv145.5@12960 our_root=3 -> dcml_root=11 dur=480 cls=b`). The flip
also merges the following region (`@13440`, a B dominant seventh over the same bass) — same-root
run-coalescing behaving correctly once the root is right.

### The governing hard stop

```
=== baroque ===  runs 6506 -> 6506 (+0/-0)   class-(b) dur 2714000 -> 2714000  delta=+0   PASS
=== jazz    ===  runs 6689 -> 6688 (+0/-1)   class-(b) dur 2784160 -> 2783680  delta=-480 PASS
                 REMOVED: bwv145.5@12960  our_root=3 -> dcml_root=11  dur=480 cls=b
=== default ===  runs 6522 -> 6522 (+0/-0)   class-(b) dur 2718080 -> 2718080  delta=+0   PASS
OVERALL: PASS
```

**Removal-only, one run, zero additions on any preset.** Class-(a) unmoved everywhere; the key columns
unmoved (the key layer is upstream of the corrected terms); WiR coverage unchanged (326/326).

### An honest note on the published columns

At the **two decimals CLAUDE.md reports, no percentage column moves.** Jazz root-agree goes 64.9772 →
64.9830 % (+0.0058 pp) — below the reported precision. What actually moves is the **hard stop itself**
(Jazz class-(b) duration −480 ticks) and the **Jazz run count** (6689 → 6688). Saying "root-agree improved"
without that qualification would overstate a 480-tick correction; the gate block is stamped accordingly.

**Tests:** `composing_tests` 1103/1103, `notation_tests` 53/53, `pipeline_snapshot_tests` 11/11 — all green,
**no golden refreshed**. The snapshot suite runs the Default configuration, which is byte-identical, and none
of its 12 stems is among the 9 that change.

### Re-baseline ritual (block (A) discipline)

- **O-12:** outgoing reference snapshotted to `tools/robust_stop/snapshot_2026-07-13_pre_oi168/` with a
  `SNAPSHOT_NOTE.md`, **before any edit**.
- **Reference re-stamped** from the candidate measurement, with the explained removal-only run-diff.
- **#17f (no hand-transcribed figures):** the manifest's recorded numbers were previously hand-assembled.
  They are now **derived** by a new instrument, `tools/robust_stop_restamp.py`, which regenerates every
  figure from the candidate `summary.json`. It is **established** (#19) by reproducing the *outgoing*
  manifest's preset blocks **exactly** before being used to write the new one. Incidental finding it forced:
  the key-agreement denominator is `scored_dur` (so the abstain duration sits **in** the denominator) — an
  ad-hoc "agree/(agree+disagree)" reading gives a different, wrong number.

---

## 4. Self-check against the guiding principles

- **#1/#2:** every figure is measured, none transcribed; the derivation was verified at runtime.
- **#3/#13:** two surprises surfaced as STOPs rather than being built around — §5 and §6.
- **#6/#7:** one membership predicate, one path; the term now lives at its correct layer (it takes a
  signature, which L4 legitimately has, not a tonic, which is L3's).
- **#8:** no inference-problem-driven coding — OI-170's three sites are declared, not fixed.
- **#14/#16:** one revertible provenance-stamped commit; O-12 snapshot first; reference re-stamped.
- **#19:** the new re-stamp instrument is positively established before use, not merely unfalsified.
- **Deviation to declare:** the dispatch asked for the `sparsechordrefinement` re-home in this session.
  It was **not done** — see §6. That is the dispatch's own escape clause, exercised.

---

## 5. ★ STOP — the fix does NOT make L4 tonic-independent (OI-170)

The dispatch's closing claim is that after this change *"L4 is structurally tonic-independent, the
collection/tonic premise holds (OI-167 + OI-168 closed)"*. **It does not, and it is not.** I checked the
whole layer rather than the two named terms, and found **three more sites that answer a pure
collection-membership question through the tonic** — the same `(keyTonicPc + scale[i]) % 12` construction,
the same δ ≠ 0 corruption, the same live region path:

| # | site | what it decides | reachable |
|---|---|---|---|
| 1 | `buildChordResult`'s **`diatonicToKey`** flag (`chordanalyzer.cpp`, the *"every sounding pc must be in the scale"* loop) | a **published fact** (`r.function.diatonicToKey`), read by `notationimplodebridge.cpp:1205` | region path |
| 2 | **Gate I**'s `invRootIsDiatonic` (`postscoringgates.cpp:475-479`) | **swaps the committed winner** | region path |
| 3 | **Gate L**'s `invRootIsDiatonic` (`postscoringgates.cpp:520-524`) | **swaps the committed winner** | region path |

Sites 2 and 3 are **decision-bearing**: when they fire they change the committed chord. The decoder runs
none of the three (it passes `gateCtxOut = nullptr`), so this is invisible from the decoder — but the
decoder is not on the production path today (measured: `decoderWindowCalls = 0`), and the region path is.

Two consequences the design pass must absorb:

1. **The `cowork_evidence_inventory.md` §8 circle-3 collection/tonic split still does not hold** for the
   live L4. OI-167's row and OI-168's closure both need this qualification before anything rests on them
   (#18 — a design may not carry load on a checkable-but-unchecked causal claim).
2. **L4 is now internally inconsistent under a δ ≠ 0 mode.** `diatonicRootContribution` says a root *is* in
   the key (signature collection) while Gate L can simultaneously say it is *not* (mode-transposed set) —
   two answers to one question inside one analysis (#6/#12).

**This does not invalidate the adoption.** The A/B held all three sites constant, so the measured result is
exactly what the adopted fix delivers: a strict improvement, just a partial one. Fixing the remaining three
is a further correctness re-baseline with its own robust-stop diff — **declared, not fixed** (#8, and outside
this dispatch's scope). The population is the same 24 Jazz `Altered` regions, and Baroque/Default should
again be byte-identical (δ = 0), so the measurement is cheap.

---

## 6. ★ STOP — Task 3 (the OI-167 re-home) is NOT clean; its premise is false at the code (OI-171)

The dispatch asks me to execute the disposition my own OI-167 report proposed: re-home
`refineSparseChordQualityFromKeyContext` out of L4 to the presentation surface, *"proven byte-identical
(0 fires means 0 behavior change)"*. **The report's premise for that — "it already runs post-commit" — is
wrong, and I am correcting my own claim.**

The function has **four** call sites in `composing`. **Three are inside the region analyzer's commit path,
before the commit:**

```cpp
// regionanalyzer.cpp
refineSparseChordQualityFromKeyContext(chosenResult, tones, localKeyFifths, localKeyMode);  // :1015
applyTonicPriorToSparseChord(chosenResult, tones, localKeyFifths, localKeyMode);            // :1017
...
decoder.commit(chosenResult.identity, gateCtx);                                             // :1026
```

Its quality overwrite therefore reaches the **committed chord identity** and the emitted `.ours.json`. The
same shape repeats at `:1233` (pass 2) and `:1423` (pass 2b). Only the fourth site
(`sectionanalyzer.cpp:158`) and the notation bridge are presentation-side.

**So moving the file to a presentation home does not re-home it — it removes it from the analysis commit
path.** That is a structural behavior change. It is *empirically* inert on this corpus only because the body
never executes (OI-167 measured 0 entries: `analyzeChord` never hands the region path an `Unknown`-quality
chord), and "no score in this corpus triggers it" is a corpus fact, not a structural guarantee.

**I stopped rather than force the cross-layer move**, per the dispatch's own instruction. The disposition
goes to the design pass, which must choose between: (a) delete the three `regionanalyzer` call sites — needs
a robust-stop diff and an argument that an `Unknown`-quality region cannot arise — then re-home the
remainder; (b) re-home only the presentation call sites; (c) retire the function outright (OI-102's carried
question). **`cc_oi167_collection_tonic_report.md` §4.2's "RE-HOME (preferred) … zero behavior change"
recommendation must be corrected before it is acted on.**

---

## 7. Incidental — a second instance of OI-169

`formatNashvilleNumber(const ChordAnalysisResult&, int keySignatureFifths)` (`chordsymbolformatter.cpp`)
**never reads `keySignatureFifths`** — the same `C4100 unreferenced formal parameter` defect as OI-169's
`structuralPenalties(… extThreshold)`, in a file this session did not touch (pre-existing at HEAD; it
surfaced when the unity build recompiled the TU). Folded into OI-169's disposition. Not fixed.

---

## 8. Register

- **OI-168 → ✅ FIXED + RE-BASELINED**, with the caveat pointer to OI-170.
- **OI-167 → conclusion REFUTED, not merely conditional** — cannot close until OI-170 and OI-171 resolve.
- **OI-169 → extended** with the second instance (§7).
- **OI-170 → NEW (★★, Class-A #18)** — the three surviving tonic-anchored collection tests (§5). A STOP.
- **OI-171 → NEW** — the re-home premise is false at the code (§6).

## 9. Reproduce

```
python tools/run_bach_preset.py --preset <P> --output-dir <dir>          # 352/352 per preset
python tools/cc_oi168_probe_report.py byteid <dir> tools/corpus/<p>      # 352/352 Baroque+Default; 9 Jazz
python tools/cc_oi168_probe_report.py flips  tools/corpus/jazz <dir>     # 1 flip, 0 outside the Altered regions
python tools/a8_rebaseline_measure.py --out-dir <cand> --corpus-root <root>
python tools/robust_stop_diff.py --candidate <cand>                      # OVERALL PASS, removal-only
python tools/robust_stop_restamp.py --candidate <cand> ...               # derives the manifest (#17f)
```
