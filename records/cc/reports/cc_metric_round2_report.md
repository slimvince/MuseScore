# CC — METRIC-FIRST Round 2 report: read-only baseline + acceptance + genre-balanced audit

> **READ-ONLY. HEAD `dd418ecfed`. No analyzer build, no committed gate tool, no production/gate/scoring/
> threshold change.** All numbers below are computed from on-disk corpora only, reusing
> `compare_analyses` + `dcml_parser` + `characterise_bir_false.validate_corpus_dir` verbatim. Repro scripts are
> throwaway and **uncommitted**: `tools/cc_round2_measure.py` (§A.1/§A.2), `tools/cc_round2_onset.py` (§A.3
> decomposition), `tools/cc_round2_genre_cov.py` (§B). They are diagnostic helpers, **not** the standing gate
> tool (the `--oracle-root` flag remains unbuilt, pending ratification).

## Headline

- **§A.1 — the oracle-root baseline is computable read-only and is a clean superset of 57/23/57** (operational
  "drop line 162" definition): **Baroque 106 / Jazz 104 / Default 110**, each = the BIR gate ∪ the BIR=true
  (wrong-root-equals-bass) cases line 162 discards. Confirmed.
- **§A.2/§A.3 — STOP CONDITION HIT. The 5/2 acceptance does NOT reproduce under the ratified policy-A oracle.**
  The dossier's 5/2 split reproduces **exactly and only** under a `(music21-only, onset-anchored)` oracle — the
  read-only proxy the anchor dossier admitted using. Under **policy A** (DCML *and* music21 must concur), **4 of
  the 5 named "regressions" (bwv102.7, bwv227.7, bwv358, bwv432) are not scoreable** — at the chord onset DCML
  *conflicts* with music21 (they fall in the `all_differ` floor). Under the **production max-overlap alignment
  the gate tool actually uses**, those same 4 score as **fixes** — the gate would have reproduced BIR's blind
  spot, not corrected it. Only the 2 genuine fixes (bwv14.5, bwv416) survive policy A robustly. **This is a
  design/alignment issue that must be reconciled before the standing gate tool is built.**
- **§B — a genre-balanced policy-A metric is NOT runnable off the Bach chorales today.** The 10 non-chorale DCML
  corpora + the When-in-Rome anthology have **no `.music21.json` sidecars** (only the 353 chorales do), so the
  music21 corroboration half of policy A is absent. DCML-only two-way coverage is rich and parseable
  (≈101.8k TSV annotations across 586 scores, all root-resolvable; ≈171.9k rntxt annotations), but consuming it
  needs a build (`batch_analyze` over each corpus) and a **DCML-only** oracle, which is a weaker/different
  oracle than the chorale gate's policy A.

---

## §A.1 — Oracle-root baseline, per preset (read-only)

**Corpus identity first (a required clarification).** The on-disk `tools/corpus/baroque` dir is **not** the HEAD
Baroque gate corpus — it holds the **ANCHOR** binary's output (litmus: `bwv40.8@20160 = Bbsus/G`,
`bwv431@480 = Fsus/D`; `characterise_bir_false` → **54**, git-stamped `dd418ecfed` but anchor-binary content).
The **HEAD** Baroque reading is `tools/corpus/baroque_kma_abs` (`bwv40.8 = Gm7`, `bwv431 = Dm7`;
`characterise_bir_false` → **57** = the CLAUDE.md baseline, git `a03c2493bb` ≡ HEAD via byte-identical refactors).
Jazz (`jazz`, 23) and Default (`default`, 57) match CLAUDE.md exactly. **So the Baroque baseline below is taken
from `baroque_kma_abs` (HEAD = 57); `baroque` (ANCHOR = 54) is reported only as the acceptance-test ANCHOR.**

Three nested sets per corpus (all on the **`music21_dcml_agree`** predicate, WiR-covered chorales only,
denominator 326):

| set | definition | meaning |
|---|---|---|
| **A** | `three_way_classify == music21_dcml_agree` | pure §2.1 formal def (primary root vs both oracles; **no** chord_disagree, **no** bass filter) |
| **B** | A ∩ `classify == chord_disagree` | **the dossier's operational gate** = `characterise_bir_false.py` **minus line 162** |
| **C** | B ∩ `bass_is_root == False` | the standing **BIR gate** (= 57/23/57) |

| preset (dir) | A (pure §2.1) | **B (gate = "minus line 162")** | C (BIR gate) | Δ B vs 57/23/57 |
|---|---:|---:|---:|---|
| **Baroque** HEAD (`baroque_kma_abs`) | 203 | **106** | 57 | **+49** (all `bass_is_root=True`) |
| **Jazz** (`jazz`) | 200 | **104** | 23 | **+81** (all `bass_is_root=True`) |
| **Default** (`default`) | 212 | **110** | 57 | **+53** (all `bass_is_root=True`) |
| Baroque ANCHOR (`baroque`) — *context only* | 538 | 116 | 54 | — |

**Delta verification (the §A.1 ask).** `B \ C` is, by construction, `B ∩ {bass_is_root=True}` — i.e. exactly the
oracle-wrong cases line 162 drops because our wrong root happens to equal the bass. All 49 / 81 / 53 newly
included cases are **wrong-root-equals-bass** (confirmed: every member has `bass_is_root=True` and is
`music21_dcml_agree`). `C ⊂ B ⊂` superset of 57/23/57 — **confirmed, exactly as the dossier predicted.** Full
case-identity sets are in `tools/cc_round2_measure.py` output (`B_minus_C` lists; representative additions:
Baroque `bwv2.6@5280, bwv272@4320, bwv64.8@17280, bwv187.7@3840, …`).

**⚠ A new design fork the dossier did not flag — A ≫ B, and A is unstable.** The pure §2.1 definition (A) is
**~2× B** and is **segmentation/alternatives-sensitive**: the same Baroque scores give A=203 at HEAD but A=538
at ANCHOR (B moves only 106→116). The gap `A \ B` is the **near_agree** set — cases where our *primary* root is
wrong but one of our *alternatives* carries the oracle root. Whether the oracle-root gate should **count** these
(A = strict primary-root error) or **exclude** them (B = "we at least surfaced it as a candidate") is a real
policy choice. **Recommendation: adopt B as the standing baseline** — it is BIR-continuous, far more stable, and
is the dossier's stated "drop line 162" definition — but record A as the stricter primary-root-only reading and
flag that the §2.1 prose ("just the `music21_dcml_agree` predicate") and the operational "drop line 162" are
**not the same set** and must be disambiguated in the gate spec.

---

## §A.2 / §A.3 — Empirical acceptance: **the 5/2 split does NOT reproduce under policy A** (STOP)

The acceptance was run four ways over the 25 anchor-moved cases (HEAD = `baroque_kma_abs`,
ANCHOR = `baroque`), scoring each case `our_root_pc == oracle_root_pc` in each corpus and deriving
fix / regress. The two axes are **oracle** (music21-only vs policy-A m21∧dcml) and **alignment** (onset-anchored
vs production max-overlap). Result, restricted to the dossier's named cases:

| oracle × alignment | named-5 regress reproduced? | named-2 fix reproduced? | notes |
|---|:--:|:--:|---|
| **music21-only, onset** | ✅ **yes** | ✅ yes | the dossier's exact proxy — 5/2 reproduces cleanly |
| **policy-A, onset** | ❌ no (only **bwv261**) | ✅ yes | 4 of 5 become **unscoreable** (DCML conflicts m21 at onset) |
| **policy-A, max-overlap** *(= the production gate)* | ❌ **no — 4 of 5 flip to FIX** | ✅ yes | the gate agrees with BIR on the 5 |

**Per-case ledger (the 7 acceptance cases):**

| case | HEAD root | ANCH root | m21@onset | dcml@onset | concur? | verdict (m21-only,onset) | verdict (policy-A) |
|---|---|---|---|---|:--:|---|---|
| bwv14.5@8160 | G | **Bb** | Bb | Bb | ✅ | **FIX** | **FIX** (robust) |
| bwv416@10080 | E | **Ab** | Ab | Ab | ✅ | **FIX** | **FIX** (robust) |
| bwv261@33840 | C# | F# | C# | C# | ✅ | regress | regress (onset) / **fix** (overlap) |
| bwv102.7@17520 | Eb | Ab | Eb | **C (vi)** | ❌ | regress | **unscoreable** → **fix** (overlap) |
| bwv227.7@18120 | G | E | G | **E** | ❌ | regress | **unscoreable** → neither |
| bwv358@6000 | E | Ab | E | **D (I6)** | ❌ | regress | **unscoreable** → **fix** (overlap) |
| bwv432@5520 | A | E | A | **Eb (viio7)** | ❌ | regress | **unscoreable** → **fix** (overlap) |

**§A.3 resolution (the DCML-coverage check on the 7).** *None* of the 7 lacks DCML coverage — so the documented
music21-only **fallback (for absent coverage) applies to none**. Instead, a different condition appears: **4 of
the 7 have a DCML/music21 *conflict* at the onset** (coverage present, roots disagree). Under policy A a conflict
is the `all_differ` **floor**, not a chargeable oracle-root error and not a fallback case. Only **3 of the 7
concur** at the onset (bwv14.5, bwv416, bwv261). The 4 conflicts are exactly the passing-sonority / symmetric
ambiguities the gate's floor-honesty is designed to exclude — but they are *also* the cases the anchor work was
trying to catch.

**Root-cause, verified by direct region inspection (e.g. bwv102.7 m9–10):** the analyzer creates one region
`[17520,18240)` that straddles the end of `vi` (DCML root **C**, to tick 17760) and the start of `IVmaj7` (DCML
root **Ab**). music21 reads a fleeting `EbMaj7` at the onset `[17520,17760)`. So:
- **onset, m21-only** → oracle = Eb → HEAD (Eb) right, ANCHOR (Ab) wrong → **regress** (the dossier).
- **max-overlap, policy-A** → the region overlaps the later Ab portion more → oracle = Ab (m21 ∧ dcml concur
  there) → ANCHOR (Ab) right, HEAD (Eb) wrong → **fix** (the production gate).

Both are internally consistent; they measure different things (onset harmony vs region-dominant harmony). **They
give opposite verdicts on the 5 critical cases.** The dossier's 5/2 lives on the music21-only-onset reading; the
ratified policy-A gate — whether onset- or overlap-aligned — does not reproduce it.

**Per the §D stop condition this is a STOP + report.** The implication: the gate's correctness proof (reproduce
the anchor's 5/2) **fails** as specified. One of three things must be reconciled by Cowork/user before the
standing tool is built:
1. **Oracle policy** — policy A is *too conservative* for the anchor's target cases: the 4 over-grab regressions
   the anchor cared about are precisely where DCML≠music21 at the onset, so policy A drops them into the floor.
2. **Alignment** — max-overlap *rewards* the ANCHOR's region-spanning over-grab (the over-grabbed region
   overlaps the destination chord more). Catching onset over-reads needs **onset-anchored** alignment, which is
   a different (and segmentation-fragile, cf. bwv227.7 below) machinery than `characterise_bir_false` uses.
3. **The acceptance target itself** — the anchor dossier's 5/2 was computed on a music21-only proxy and may not
   be the right policy-A acceptance target at all.

**Segmentation-tick caveat (bwv227.7).** This case is additionally muddied by onset drift: HEAD segments the
region at tick **18120**, ANCHOR at **18000** (`bwv227.7@18000` is in ANCHOR's set; `@18120` is not). Exact-tick
set membership therefore reads it as a "fix"; the overlap oracle reads it as "neither"; the onset-m21 oracle as
"regress". Three methods, three answers — an independent symptom that the acceptance is alignment-fragile.

**What IS robust:** bwv14.5 (G→Bb, oracle Bb) and bwv416 (E→Ab, oracle Ab) are genuine fixes under **all** four
methods (m21 ∧ dcml concur, onset and overlap agree). The 2 genuine fixes are solid; the 5 regressions are not.

---

## §B — Genre-balanced coverage audit (read-only)

### B.1 Per-corpus GT coverage (measurable from disk today)

GT parsed with `dcml_parser` (`parse_abc_harmonies_file` for TSV, `parse_rntxt_file` for rntxt). "rootPC" = the
oracle-root denominator (annotations with a resolvable root pitch class). **music21 sidecar present** governs
whether **policy A** (m21 ∧ dcml) can run at all.

| corpus | genre | GT files | annotations | root-resolvable | music21 sidecar? | existing script → metric |
|---|---|---:|---:|---:|:--:|---|
| **bach_chorales** (BIR gate) | Baroque (SATB) | 326 WiR-covered / 353 | — | — | ✅ **353** | `characterise_bir_false` → **policy-A** `music21_dcml_agree` |
| corelli | Baroque (trio) | 149 | 14,043 | 14,043 | ❌ | `run_corelli_validation` → **DCML-only** root agree % |
| bach_en_fr_suites | Baroque (kbd) | 89 | 11,207 | 11,207 | ❌ | `run_bach_suites_validation` → DCML-only |
| ABC | Classical (Beethoven SQ) | 70 | 27,990 | 27,990 | ❌ | `run_beethoven_validation` → DCML-only |
| mozart_piano_sonatas | Classical | 54 | 15,030 | 15,030 | ❌ | `run_mozart_validation` → DCML-only |
| cpe_bach_keyboard | Galant | 66 | 10,902 | 10,902 | ❌ | `run_cpe_bach_validation` → DCML-only |
| chopin_mazurkas | Romantic | 55 | 8,993 | 8,992 | ❌ | `run_chopin_validation` → DCML-only |
| schumann_kinderszenen | Romantic | 13 | 919 | 919 | ❌ | `run_schumann_validation` → DCML-only |
| tchaikovsky_seasons | Romantic | 12 | 2,992 | 2,992 | ❌ | `run_tchaikovsky_validation` → DCML-only |
| dvorak_silhouettes | Late-Romantic | 12 | 1,526 | 1,526 | ❌ | `run_dvorak_validation` → DCML-only |
| grieg_lyric_pieces | Late-Romantic | 66 | 8,151 | 8,151 | ❌ | `run_grieg_validation` → DCML-only |
| when_in_rome (anthology) | Mixed | 921 rntxt / 1,294 analysis.txt | 171,882 | 171,882 | ❌ (chorale slice only) | `compare_when_in_rome` → DCML-only |

TSV GT is **100% root-resolvable** (one Chopin row excepted) — the `dcml_parser` TSV+rntxt paths already span
every cloned corpus. The denominators above are GT-side and need **no build**; producing the *numerator*
(our root per region) needs `batch_analyze` over each corpus (a build — out of scope here).

### B.2 Genre-balanced macro design

Aggregate **one observation per genre** (macro-average), so the 326 chorales cannot dominate, while keeping the
chorale-only policy-A number for continuity:

```
genres = {Baroque-chorale, Baroque-instrumental(corelli+suites), Classical(beethoven+mozart),
          Galant(cpe), Romantic(chopin+schumann+tchaikovsky+dvorak), Late-Rom(grieg), Mixed(WiR-anthology)}
oracle_root_macro = mean_over_genres( agree_rate(genre) )   # each genre weighted equally
report alongside: chorale_policyA (the current gate, for continuity)
```

**The hard constraint:** only the **Baroque-chorale** genre can use **policy A** today (it is the only genre
with music21 sidecars). Every other genre can offer only a **DCML-only** two-way root agreement
(`compare_ours_vs_dcml_direct`). A macro that mixes a policy-A chorale number with DCML-only numbers elsewhere is
**not apples-to-apples**. Two clean options for reconciliation:
- **(a) Two-tier macro** — report a **policy-A** number for chorales and a separate **DCML-only** macro across
  all genres (including a DCML-only chorale number for parity inside that macro). Honest, runnable after a build,
  no music21 generation needed.
- **(b) Generate music21 sidecars** for all ~1,700 non-chorale scores so policy A runs everywhere. Larger,
  music21-version-pinning, and a deliberate new ground-truth asset — a Stage-5 decision, not read-only.

Recommendation: **(a)** as the near-term genre-balanced view; **(b)** only if/when a uniform policy-A macro is
judged worth the music21-generation cost.

### B.3 GT-format / identity gap list (flag, don't fix)

1. **No music21 sidecars off-chorale** — policy A is chorale-only today. (Biggest gap; governs B.2.)
2. **`.ours.json` for the 10 non-chorale corpora + WiR anthology must be built** — the validation scripts run
   `batch_analyze` live; nothing end-to-end is read-only today except the chorale gate (cached outputs exist).
3. **Alignment substrate differs by format:** TSV carries `quarterbeats` → exact `abs_tick` (pickup-aware);
   rntxt (WiR) has **no** absolute column → measure-anchor reconstruction that needs our region anchors (so even
   alignment needs `.ours.json`). The §A onset-vs-overlap ambiguity recurs at every genre.
4. **Chorale identity hazard (unchanged, inventory C3):** music21-BWV (353) vs DCML-Riemenschneider (361)
   chorale selections are **not** super/subset and have no in-repo concordance; do not silently treat one as a
   subset of the other.
5. **WiR anthology basename quirk:** every score is `score.mxl` under
   `Corpus/<style>/<composer>/<piece>/<number>/`; any oracle-root tool keying by basename must use per-score
   subdirectories (1,294 `analysis.txt` vs 921 `.rntxt` — some pieces share an analysis).

### B.4 Diagnostic, not auto-recalibration

A genre-balanced number reports **where we stand**, nothing more. It must **not** trigger widening any
Baroque-tuned threshold (CLAUDE.md hard rule). If a non-Baroque genre scores poorly, the response space is the
existing one (tighter structural entry condition, or preset-specific override) — never a Baroque-threshold
widening. **Measurement only.**

---

## §C/§D — Compliance & stop conditions

- **READ-ONLY** — HEAD `dd418ecfed`; no build, no committed tool, no production/gate/scoring/threshold change. ✅
- **§A.1 delivered** — per-preset oracle-root baseline (B = 106/104/110), case-identity sets emitted, delta vs
  57/23/57 confirmed as the BIR=true (wrong-root-equals-bass) additions. ✅ Plus a flagged A≫B design fork.
- **§D STOP — the empirical acceptance does NOT reproduce the 5/2 split under policy A.** Reported, not
  worked around. The 5/2 is a `(music21-only, onset)` artifact; policy A drops 4 of 5 to the floor (onset) or to
  **fixes** (production overlap). This must be reconciled before the standing gate tool is built. ✅ (reported)
- **§D — no case silently dropped:** the 4 conflict cases are recorded (DCML≠music21 at onset), distinct from
  the absent-coverage fallback (which applies to none of the 7). ✅
- **§D — genre GT readability:** all 11 cloned corpora + WiR parse cleanly; the gap is **music21 sidecars**
  (policy-A corroboration) and **`.ours.json`** (a build), both listed — no denominator fabricated. ✅
- **No threshold/scoring change, no gate tool committed.** ✅

**For Cowork/user:** ratify (1) **baseline B = 106/104/110** as the oracle-root baseline (vs the stricter pure-A
203/200/212); (2) how to resolve the **acceptance failure** — adjust the oracle policy, the alignment, or retire
the 5/2 target; (3) the **genre-balanced design (a) two-tier macro** vs **(b) generate music21 sidecars**.
Until (2) is resolved the `--oracle-root` standing tool should **not** be built, because its specified
correctness proof does not hold.
