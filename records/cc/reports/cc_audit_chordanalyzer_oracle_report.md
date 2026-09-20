# CC Layer Audit #5 — `chordanalyzer.cpp` (the vertical oracle) — READ-ONLY findings

*CC primary auditor, 2026-06-17. HEAD `a03c2493bb`. Per `docs/layer_audit_plan.md` §3.
Read-only: no code / behavior / inference change. North star = CORRECT inference vs the
DCML/music21 oracle, not a proxy gate. Reconciles with `cowork_audit_chordanalyzer_oracle.md`.*

**Evidence tags:** **[src]** read at HEAD source · **[probe]** ran a read-only script over the
committed corpus · **[oracle]** music21 9.9.1 cross-check (inherited from
`cc_functional_residual_dossier.md`). Drivers are throwaway `C:\tmp\cc_audit_oracle_*.py` /
`cc_audit_gate_symmetric.py`, reusing the committed metric machinery (`compare_analyses`,
`dcml_parser`) verbatim. No repo write but this file.

**Base / corpus state [probe].** `tools/corpus/default` manifest `git_hash = 41f7c65f63`,
`complete=True`, `ours_count=353`, music21 9.9.1. HEAD `a03c2493bb` is 4 commits later, all
**byte-identical** verbatim splits (`ed4b462021`/`2024f2951e`/`a03c2493bb` + the parent
`41f7c65f63`), each gate-verified 0-diff `.ours.json` ×3 presets (STATUS.md). So the corpus
chord output IS HEAD's chord output. The corrected GT parser is **committed at HEAD**
(`a96f179f40`; blobs `dcml_parser.py 2db84ba9`, `compare_analyses.py c27c7ddb` — identical to the
"staged/HELD corrected parser" the functional-residual dossier measured on). The re-measurement
below is therefore a true at-HEAD reproduction, not a stale read.

---

## §1 — Responsibility (the contract)

`RuleBasedChordAnalyzer::analyzeChord` — the **vertical chord oracle**: from sounding pitch content
(+ bass, + key context) score every `root × template` cell against the **17-template vocabulary**,
build the bass-independent score matrix, hand a `fn::ScoringSnapshot` (the vertical candidate cube,
**no progression signal**) to the competition/function layer; emit up to 3 `ChordAnalysisResult`
candidates. Foundational vertical identification. **[src** chordanalyzer.h:74,822-829; .cpp:1198-1299**]**

**One responsibility — with a caveat (phase-2).** The oracle is "vertical" by design (Stage 3.3
migrated all five progression signals OUT to the competition pipeline; the snapshot adds no temporal
term **[src** .cpp:787-800**]**). But it **reads the key in two of its six score terms** (§2.4) —
so it is *mostly* vertical, not *purely* vertical. That key-leak is the chord↔key coupling and is a
phase-2 dependency note, not a within-layer defect.

---

## §2 — Correctness (vs the true chord — the VERDICT-CRITICAL measurement)

### §2.1 — ★ The functional/vertical split, RE-MEASURED at HEAD [probe]

Three-way root classification (`three_way_classify`) over the **326 WiR-rntxt-covered Bach stems**
in `tools/corpus/default`, per-ours regions aligned to music21 (`align_regions`) and to DCML
(`align_dcml_regions`, time-overlap). My driver reproduces the dossier's instrument:

| figure | this audit @ HEAD | dossier (2026-06-14, corrected parser) |
|---|---:|---:|
| stems scored | 326 | 326 |
| three-way scored regions | 10,109 | 10,108 |
| `all_agree` | 7,608 | — |
| `dcml_ours_agree` | 136 | — |
| **`music21_dcml_agree`** (vertical-fixable) | **212** | **212** |
| **`all_differ`** (neither / functional) | **2,153** | **2,153** |
| **root_err** (= m21_dcml + all_differ) | **2,365** | **2,365** |
| per-ours root_err rate | 23.4 % | 23.4 % |
| **FUNCTIONAL %** (all_differ / root_err) | **91.0 %** | **91.0 %** |
| **VERTICAL %** (m21_dcml / root_err) | **9.0 %** | **9.0 %** |

Exact reproduction (the lone +1 region in 10,109 vs 10,108 is an alignment-id edge; it moves no
headline). **The split at HEAD is 91.0 % functional / 9.0 % vertical.**

**★ I CORRECT the Cowork note's `[prov ≈ 95.2 % functional / 4.8 % vertical]`.** That is the OLD
**buggy-parser** figure (the WiR parser mis-rooted applied + minor-key LT/submediant chords, burying
365 already-correct cases + 75 vertical-fixable cases inside `all_differ`). On the **corrected
parser that is now committed at HEAD**, the functional share is **91.0 %** and the vertical share
**9.0 %** — the vertical share is ≈double the old number, but still a clear minority.

**The verdict HOLDS.** The oracle correctly roots the sonority for the large majority of cases; of
its root errors, ~91 % are not vertical-scoring failures (a second *independent* vertical analyzer —
music21 — reaches the *same* root and DCML still differs → a functional-LAYER reading, or a
defensible ambiguity, not a pitch-content failure). The "chord axis is healthy; obligations are
DOWNSTREAM (the competition/function layer)" conclusion stands on the corrected number — it is just
**less lopsided** than `95.2/4.8` implied. The "true vertical headroom" is even smaller than 9 %
once the inherent symmetric floor (§2.3) is removed from it.

### §2.2 — The second vertical analyzer agrees with us in the residual [oracle, inherited]

Inside `all_differ` (2,153), music21 == ours in **94.1 %** (dossier §0.4) — in 94 % of the functional
residual the two independent vertical analyzers produce the **same** root and DCML differs. This is
the corpus-scale signature that the residual is non-vertical (functional) or defensible-ambiguity,
not an oracle-scoring bug.

### §2.3 — The symmetric floor (C3), measured [probe]

A region is **pc-root-ambiguous** when its weight-significant pitch classes contain a full
diminished-7th `{x,x+3,x+6,x+9}` (4 equal minor-thirds — 4 equally-valid roots) or a full augmented
triad `{x,x+4,x+8}` (3 roots). Measured from each region's `pitchClassSet` bitmask:

| scope | symmetric (dim7 ∪ aug) | dim7 | aug |
|---|---:|---:|---:|
| **corpus-wide** (11,255 default regions) | **2.5 %** (277) | 1.4 % (163) | 1.0 % (118) |
| within `music21_dcml_agree` (vertical-fixable, 212) | **28.8 %** (61) | — | — |
| within `all_differ` (functional, 2,153) | 3.2 % (69) | — | — |
| **Baroque-57 BIR=false gate cases** | **54 %** (31) | **53 %** (30) | 2 % (1) |

**Two corrections / confirmations of Cowork's `[prov ≈ 53 % Baroque]`:**
- **CONFIRMED, precisely, as a GATE-case statistic:** 30/57 = **53 %** of the Baroque BIR=false gate
  cases contain a full dim7 (and 31/57 = 54 % are symmetric) — exact match to the `[prov]`.
- **It is NOT a corpus-wide statistic.** Symmetric sonorities are only **2.5 %** of all regions. The
  53 % is a property of the *curated root-error gate*, where ambiguous sonorities concentrate by
  construction — not of Bach harmony at large.

**The symmetric set IS the inherent vertical floor, and it is concentrated in the vertical-fixable
bucket** (28.8 % of the 212), not the functional one (3.2 %). Root is undefined by pitch class
alone; the oracle resolves it **only** via the key-coupled `dim7CharacteristicBonus` rotation-selector
(§2.4) — i.e. the symmetric-dim7 root is reached, when it is reached, by reading the key, not by the
vertical score. These cases are the structurally-unresolvable seed of a reserved learned slice
(CLAUDE.md / `back_half_design`); not hand-buildable away by a better template scorer.

### §2.4 — The key coupling (X2), confirmed at source — and it is broader than Cowork noted [src]

The bass-independent vertical score `basisIndepMatrix[root][tpl]` is the sum of six terms
**[src** .cpp:1293-1299**]**. **Two of them read the key:**
1. **`diatonicRootContribution`** (.cpp:801-812): a **flat +0.30** (`diatonicRootBonus`) to *every*
   root that is in the key scale. Not limited to ambiguous sonorities — it is uniform — but it only
   *changes the winner* on near-ties, so it behaves as a diatonic tiebreaker. **[src]**
2. **`dim7CharacteristicBonus`** (.cpp:452-485): a **key-dependent rotation selector** for symmetric
   dim7 — it rewards the enharmonic root whose `bb7` is *non-diatonic* in the current key. This is the
   mechanism that picks one of the four pc-equal dim7 roots (§2.3). **[src]**

So the "vertical" oracle leaks a key dependency in **two** terms (Cowork's note cited only
`diatonicRootContribution`). The dim7 leak is the more consequential one: the symmetric-floor root is
**defined by the key**, not the pitches. Phase-2 chord↔key circularity finding (consistent with the
re-emission-bug coupling, STATUS.md).

### §2.5 — viio7 ↔ V7 share-tone (C3 cont.)

Confirmed structurally: a `{0,3,6,10}` (HalfDim) / dim-triad+b7 vs `{0,4,7,10}` (dom7) share three
tones; the oracle's choice is a near-tie resolved partly downstream. Three of the Baroque-57 gate
cases are HalfDiminished winners where DCML reads otherwise (bwv245.15/245.37 etc.) **[probe** §
gate detail**]**. Sub-case of the ambiguity floor.

---

## §3 — Completeness (vs the chord vocabulary)

### §3.1 — The 17-template vocabulary [src .cpp:1198-1216]

Maj triad · maj7 · dom7 · dom7b5 · min triad · min7 · dim triad · sus4b5 · half-dim7 · aug triad ·
aug7 · sus2 · sus4(b7) · sus4+maj7 · sus4#5 · sus#4 · power. All tertian/sus/power; **none extended
beyond a 7th core.** `static_assert(templates.size() == kTemplateCount)` (=17).

### §3.2 — fully-dim7 `{0,3,6,9}` is DERIVED, not an explicit template [src — CONFIRMS Cowork Q3]

There is **no** `{0,3,6,9}` template. Template #7 is the dim **triad** `{0,3,6}`; the fourth tone
(`root+9`) is rewarded by `dim7CharacteristicBonus` only when the complete dim triad is present and
`root+9` is non-diatonic (§2.4). So `vii°7` is the dim-triad template + a key-gated rotation bonus —
a rotation-SELECTION mechanism over the four pc-equal roots, not a vocabulary entry. **Confirmed.**

### §3.3 — The jazz-vocabulary gap (C4) [src + probe-limitation]

**Structural fact [src]:** the 17 scoring templates have no extended/altered entries (9/11/13, alt).
Extensions ARE detected — `detectExtensions` (.cpp:198-327) is rich: natural/♭/♯ 9th, 11th/♯11,
13th/♭13/♯13, 6/9 — but as **label decorations layered on a triad/7th template CORE in
`buildChordResult`** (.cpp:871), *after* scoring. Consequence: an extended chord (e.g. C13) is
*scored* as its 7th core (dom7 template) and the 9/11/13 are appended to the symbol. For **stacked**
extensions the **root is unaffected** (root of C13 = root of C7), so this is largely correct on the
root axis. The genuine gap is **altered dominants** (a ♯5 reads as Augmented, a ♭5 as dom7b5; rootless
voicings) where the alteration changes the best-fit template and can shift the root.

**Empirical measurement NOT available read-only (flagged, not guessed).** The "Jazz corpus" with
ground truth (`tools/corpus/jazz`) is the **353 Bach chorales under the Jazz preset** — Bach harmony
does not exercise 9/11/13/alt, so it cannot quantify this gap. The **real** jazz scores
(`tools/extra scores/*.mscz`) have **no DCML/music21 ground truth**, and the standalone
`batch_analyze.exe` **fails to load `.mscz`** ("failed to load score" on all of
all-the-things / giant-steps / autumn-leaves / so-what) — it lacks the compressed-container reader
**[probe]**. So a corpus-scale jazz-vocab error rate is an **unknown** here; C4 stands as a
structural completeness gap, not a measured number.

---

## §4 — Gaps → obligations (tagged)

| # | obligation | tag |
|---|---|---|
| **O1** | **The functional residual (≈91 % of root errors, ~2,153 regions) is a DOWNSTREAM problem.** The oracle roots correctly; the winner-selection/function layer must reach the functional root. | `[correctness]` `[priority: chord-axis]` `[fix: downstream — the competition/function layer, audited next; NOT the oracle]` |
| **O2** | **Symmetric-dim7/aug floor** (~2.5 % of regions corpus-wide; 53 % of the Baroque gate; 28.8 % of the vertical-fixable bucket). Root pc-undefined; resolvable only via the key-coupled rotation-selector. The irreducible vertical floor → reserved learned slice. | `[correctness — inherent floor]` `[priority: chord-axis]` `[fix: NOT hand-buildable — reserved]` |
| **O3** | **The "9 % vertical" is an over-estimate of fixable vertical headroom.** ≈29 % of it is the symmetric floor (O2). The genuinely-better-vertical-scorer-fixable slice is the small remainder. | `[correctness]` `[priority: chord-axis — LOW]` `[fix: Stage-5 emission, small]` |
| **O4** | **Chord↔key coupling: the oracle reads the key in 2 score terms** (`diatonicRootContribution` flat +0.30 on all in-key roots; `dim7CharacteristicBonus` key-gated dim7 rotation). "Mostly vertical," not pure. | `[structural — dependency]` `[priority: phase-2 / chord↔key circularity]` `[fix: structural, phase-2]` |
| **O5** | **Jazz-vocabulary completeness gap.** No extended/altered scoring templates; extensions are post-scoring label decorations. Root usually correct for stacked extensions; altered-dominant/rootless voicings can mis-root. Corpus-scale size UNMEASURED (no jazz GT; `.mscz` won't load in batch_analyze). | `[completeness]` `[priority: chord-axis / jazz]` `[fix: behavior-changing — deferred; needs a jazz GT corpus to size]` |

---

## §5 — Reconciliation with Cowork's note

| Cowork claim | verdict |
|---|---|
| ~95 % vertically correct / **95.2 % functional, 4.8 % vertical** | **CORRECTED → 91.0 % / 9.0 %** at HEAD on the committed corrected parser. The *direction* (oracle solid, errors mostly functional) holds; the *magnitude* was the buggy-parser figure. |
| Symmetric chords are the pc-root-undefined floor; **≈53 % of Baroque** | **CONFIRMED as a gate-case stat** (30/57 = 53 % dim7). **Corrected scope:** corpus-wide it is 2.5 %, not 53 %. |
| viio7↔V7 share-tone, partly resolved downstream | confirmed (sub-case of the ambiguity floor). |
| Diatonic-root tiebreak reads the key | confirmed, **and broadened**: the key enters in **two** terms, the dim7 rotation-selector being the load-bearing one. |
| Vocabulary = 17 tertian/sus/power; no extended jazz harmony | confirmed at source. |
| fully-dim7 explicit template or derived? | **DERIVED** (dim triad + key-gated `dim7CharacteristicBonus`). |
| Obligations are DOWNSTREAM, not the oracle | confirmed — holds on the corrected 91 %. |

**Net:** the chord-axis-healthy verdict and the two-track split **HOLD**. The one substantive
correction is the headline number (`95.2/4.8` → `91.0/9.0`); it does not flip the verdict, but the
honest vertical share is ≈double and should be quoted as **9 %** going forward.

---

## §6 — Method / unknowns

- **Method:** byte-identical-corpus reasoning (HEAD = corpus output, gate-proven 0-diff) + a faithful
  three-way reproduction reusing the committed `compare_analyses`/`dcml_parser` (driver reproduces
  the dossier counts exactly). Symmetric share decoded from `pitchClassSet`. Source claims read at HEAD.
- **Unknowns (surfaced, not guessed):** (1) the jazz-vocab gap size (O5) — no jazz GT, `.mscz` won't
  load in standalone batch_analyze; (2) the B1↔B3 (rule-reachable vs ambiguity) split *inside* the
  functional residual is the dossier's soft number (both route away from "needs-a-learned-model") —
  out of scope for the oracle audit, it is the next layer's (competition/function) obligation;
  (3) alignment-noise vs genuine-disagreement inside `all_differ` is unseparated (inflates the
  ambiguity share — a lenient audit would only *strengthen* the oracle-is-healthy verdict).
- **Stop conditions:** none hit. No production/inference/behavior change; all probes read-only and
  byte-identical to production.

*Cowork verifies methodology + reconciles; user ratifies. Drivers: `C:\tmp\cc_audit_oracle_split.py`,
`cc_audit_oracle_symmetric.py`, `cc_audit_gate_symmetric.py` (throwaway, untracked).*
