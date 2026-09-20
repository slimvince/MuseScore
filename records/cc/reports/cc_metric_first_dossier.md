# CC — METRIC-FIRST dossier: the oracle-root (+ tiered) gate design

> **READ-ONLY design deliverable. HEAD `dd418ecfed`. No code, behavior, inference, gate-threshold, or
> scoring-term change was made.** Per `cowork_architecture_reassessment.md` §3.1 / §5(b): build the metric
> before any inference work, because CC's anchor dossier (`cc_anchor_redesign_dossier.md` §2C) proved **BIR is a
> misleading proxy** — it scored 5 oracle-root *regressions* as "fixes." This dossier (a) traces what
> measurement signal already exists, (b) designs the oracle-root gate + its acceptance test, (c) recommends on
> the tier ladder, (d) lists normalizer gaps, (e) specifies the integration/protocol changes. Cowork reconciles;
> user ratifies before any metric is built.

---

## §1 — What already exists (the reusable stack)

**The headline finding: the oracle-root comparison is already implemented.** It lives in
`compare_analyses.three_way_classify()`. The "gap" is not a missing comparison — it is a **filter applied on
top of it** in `characterise_bir_false.py` that makes the *standing gate* (the CLAUDE.md 57/23 case set) a
bass-coupled subset of the true oracle-root error set. Removing that one filter yields the oracle-root gate.

### 1.1 The data is present, pitch-class-typed, and 1:1 aligned (read-only, no build)

Per `tools/corpus/<preset>/*.{ours,music21}.json` and `tools/dcml_parser.py`:

| Oracle / source | Field | Type | Notes |
|---|---|---|---|
| **Ours** | `rootPitchClass` | int 0–11 | + `bassPitchClass`, `bassIsRoot` (bool) |
| **music21** (`.music21.json`) | `rootPitchClass` | int 0–11 | music21's own `RomanNumeral` root |
| **DCML** (GT, via `dcml_parser`) | `DcmlRegion.root_pc` | int 0–11 or None | `_compute_root_pc(numeral, effective_key)`; the applied-`/X` + minor-key `vi/vii` rooting bugs are **fixed** (CLAUDE.md; verified 100% vs music21 `RomanNumeral` on gate cases) |

- **Root is a pitch class everywhere.** This is decisive: the gate compares `rootPitchClass` **ints**, so it is
  **immune to enharmonic spelling and to all Roman-numeral string-normalization edge cases** (Ger6 collapse,
  `#vii` strip, etc.). Those rules only bite the *label/tier* accounting (§4), never the root gate. (Concrete:
  the acceptance case bwv416 has oracle root *Ab* and our reading *G#dim7* — both pc 8; a pc comparison scores
  it a match, a string comparison would not.)
- **Alignment is solved.** `compare_analyses.align_regions` (ours↔music21) and `align_dcml_regions`
  (ours↔DCML) both use **time-overlap with a 50%-of-either-region lenient-OR threshold**. For music21 the
  segmentation is **1:1 by `startTick`/`endTick`** in practice (same 480-tick grid). DCML ticks come from the
  TSV `abs_tick` column when present, else reconstructed from `measure`+`beat` against analyzer measure anchors.
- **Corpus integrity is enforced.** `characterise_bir_false.validate_corpus_dir()` requires
  `corpus_manifest.json`, `complete==True`, exact count, and per-stem SHA256 match — the anti-contamination
  guard CLAUDE.md describes. Any oracle-root tool reuses this verbatim.

### 1.2 `compare_analyses.three_way_classify()` — the oracle comparison, already written

```
ours_dcml   = (ours_root_pc   == dcml_root_pc)
theirs_dcml = (theirs_root_pc == dcml_root_pc)   # theirs = music21
all_agree           : ours==dcml  and music21==dcml
dcml_ours_agree     : ours==dcml  and music21!=dcml
music21_dcml_agree  : music21==dcml and ours!=dcml   ← OUR ROOT IS WRONG, both oracles concur
all_differ          : (else)
```

`music21_dcml_agree` **is the genuine oracle-root-error predicate**: our root differs from a root that DCML
(authoritative) and music21 (corroborating) **both** assert. It is bass-blind by construction — it never reads
`bass_pc`. This is exactly the decoupling §2 asks for, and it is the conservative choice: where the two oracles
*disagree* (chiefly the symmetric-dim7 pc-undefined floor) the case falls into `all_differ` and is **not**
charged against us — the floor is excluded for free.

### 1.3 `characterise_bir_false.py` — why the *gate* diverges from oracle-root-wrong

The script computes the right thing and then **discards half of it**:

```
line 162:  if our_r.bass_is_root:            # ← THE TRAP: skip every BIR=true case
               continue
line 169:  if three_way_classify(...) == "music21_dcml_agree":   # then keep oracle-wrong
```

So the **standing gate** (the CLAUDE.md 57/23/57 case-identity set) is

> `{ our_root ≠ oracle_root (music21 & DCML agree) } ∩ { bass ≠ root }`

— the oracle-root-error set **intersected with BIR=false**. The intersection is the bug. When an analyzer
change makes a *wrong* root coincide with the bass (e.g. a recompute selects a root-position chord on the
wrong root), `bass_is_root` flips **true**, the case is `continue`'d out of the set, the gate integer **drops**,
and that reads as a **"fix"** — while `three_way_classify` would still say `music21_dcml_agree` (root still
wrong). That is the precise mechanism behind the anchor's 5 false-positive "fixes." **The oracle-root gate is
this same script with line 162 deleted** (root error counted regardless of bass position).

### 1.4 `analyze_inversion_errors.py` — the same oracle comparison, as a diagnostic (not a gate)

Already calls `three_way_classify` and splits the `music21_dcml_agree` set by `bassIsRoot` true/false →
the **47/57 (Baroque) / 81/23 (Jazz)** figures in CLAUDE.md; the `bassIsRoot=false` halves (**57/23**)
independently reproduce the BIR gate. So it **already measures the full oracle-root error set** — it just
reports it as margin/alt/noteCount diagnostics rather than emitting a stable per-preset **case-identity set**.
It is ~80% of the gate; what's missing is the stem@tick identity-set emission + the manifest validation gate
(which `characterise_bir_false` already has).

### 1.5 `compare_rn.py` — label-tier comparison (the tier-ladder substrate)

Buckets each aligned pair into `exact / partial / key_disagree / quality_disagree / root_err` via
`classify_pair` (root-pc match × case-encoded quality match × exact-string match). This is our existing,
coarser cousin of the Contrapunctus 6-tier ladder (§3). `root_agree` here is the same root-pc comparison as
`three_way_classify`, but against DCML only (no music21 corroboration step).

**Reuse summary:** root comparison (`three_way_classify`), alignment (`align_regions`/`align_dcml_regions`),
corpus validation (`validate_corpus_dir`), DCML rooting (`dcml_parser.root_pc`), and label tiering
(`compare_rn.classify_pair`) **all already exist**. The oracle-root gate is an assembly of parts we own, not a
new measurement.

---

## §2 — The oracle-root gate (the core deliverable)

### 2.1 Definition

> **Oracle-root error set (per preset)** =
> `{ case (stem@tick) : three_way_classify(our_root_pc, music21_root_pc, dcml_root_pc) == "music21_dcml_agree" }`
>
> aggregated as a **case-identity set** (stem@tick), exactly like BIR, for **Baroque / Jazz / Default**.
> A region whose root merely equals the **bass** earns nothing — it is scored against the **oracle** root, not
> the bass. (Formally: drop `characterise_bir_false.py:162`; keep the `music21_dcml_agree` predicate.)

Properties that satisfy the §2 mandate:
- **Bass-decoupled.** `three_way_classify` never reads `bass_pc`; a wrong-root-equals-bass move cannot reduce
  the count.
- **Pitch-class typed.** Enharmonic-/spelling-immune (no normalizer dependency for the root verdict).
- **Floor-honest.** Symmetric-dim7 and other oracle-disputed roots land in `all_differ`, not charged.
- **Conservative oracle.** Requires DCML **and** music21 to concur our root is wrong → no penalty where the
  oracles themselves disagree. (DCML is authoritative; music21 corroborates — exactly the CLAUDE.md policy.)

**Baseline note (honest):** this set is a **superset** of today's BIR gate (it re-includes the BIR=true
oracle-wrong cases line 162 drops), so its per-preset integers will be **higher than 57/23/57** and must be
**re-baselined**. The baseline is computable **read-only from the existing on-disk corpus** (no analyzer
build) — see §5.3.

### 2.2 Acceptance test — reproduce the anchor's 5/2 split

The gate is correct **iff**, run on the anchor's 25 moved cases (HEAD = `tools/corpus/baroque_kma_abs`,
ANCHOR = `tools/corpus/baroque`; both carry `.music21.json`, both on disk — read-only), it scores each case by
`our_root_pc == oracle_root_pc` and yields **exactly**:

- **5 regressions** (HEAD root correct → ANCHOR root wrong): `bwv102.7, bwv227.7, bwv261, bwv358, bwv432`
- **2 genuine fixes** (HEAD root wrong → ANCHOR root correct): `bwv14.5, bwv416`

Worked from `cc_anchor_redesign_dossier.md` §2C (oracle root in pc; ✓=root matches oracle):

| case | oracle root | HEAD reading → root | ANCHOR reading → root | HEAD vs oracle | ANCH vs oracle | verdict |
|---|---|---|---|---|---|---|
| bwv102.7@17520 | Eb (3) | EbMaj7/Ab → Eb | AbMaj9 → Ab | ✓ | ✗ | **regress** |
| bwv227.7@18120 | G (7) | GMaj7/E → G | Em13 → E | ✓ | ✗ | **regress** |
| bwv261@33840 | C# (1) | C#m/E → C# | F#7/E → F# | ✓ | ✗ | **regress** |
| bwv358@6000 | E (4) | E11/G# → E | G#dim7 → G# | ✓ | ✗ | **regress** |
| bwv432@5520 | A (9) | Am/E → A | EMaj7#5 → E | ✓ | ✗ | **regress** |
| bwv14.5@8160 | Bb (10) | Gm/Bb → G | Bbadd9 → Bb | ✗ | ✓ | **FIX** |
| bwv416@10080 | Ab (8) | E7b9/G# → E | G#dim7 → G#(=8) | ✗ | ✓ | **FIX** |

**Why BIR fails here and the oracle gate succeeds:** in all 5 regressions the ANCHOR reading is **root-position**
(`AbMaj9, Em13, F#7, G#dim7, EMaj7#5` — no slash → `bass_is_root=true`), so BIR drops them as "fixed." Critically
bwv416's genuine fix is **also** root-position `G#dim7` (`bass_is_root=true`) — BIR cannot tell bwv416 (root pc
8 = oracle Ab) from bwv358 (root pc 8 ≠ oracle E). **Only the pitch-class root-vs-oracle comparison separates
them.** This is the exact discrimination the gate must have, and the table shows the design delivers it.
*(The remaining 18 of 25 cases are `neither`/`both-match`/`already-correct` and are correctly scored as no-change
by the gate — they do not enter the 5/2 ledger.)*

**One caveat to verify at build time:** the §2C table's "oracle root" column was computed from `.music21.json`
**only** (the read-only proxy the dossier used). The gate's `music21_dcml_agree` predicate additionally requires
**DCML** coverage + agreement at each tick. The acceptance check must confirm all 7 cases have aligned DCML rows
that concur; if any lacks DCML coverage, document the fallback policy (music21-corroborated-DCML, else
music21-alone) rather than silently dropping the case. This is the only place the acceptance test could fail to
reproduce for a non-root reason, and it is checkable read-only.

---

## §3 — Tier-ladder accounting: recommendation = **PARTIAL adopt**

Contrapunctus's cumulative ladder (`contrapunctus_findings.md` §10, §10c, §10e):
`exact ⊂ +sameChord ⊂ +inversion ⊂ +convention ⊂ +sharedBass ⊂ +secondaryDiatonic`. Their per-engine jumps:
exact 59.63 → … → +sharedBass **72.73** → +secondaryDiatonic 73.16; **the biggest jump is `+sharedBass`
(+6.77pp)** — i.e. most non-exact misses are bass-sharing/incomplete-chord ambiguities (`iii↔I6`, `V6↔vii°`),
which is **our own bass-anchoring floor** (audit-#6 216/345) and the §5(e) "accept the floor."

**Value:** a tier ladder cleanly separates *genuine error* from *defensible convention floor* — better than
BIR + ad-hoc buckets, and our convention buckets (Cad⁶₄↔I⁶₄, vii°↔V, V/V↔II, shared-bass) map onto it
**verbatim** (§10 confirms "the convention examples are *our* ambiguity buckets"). It tells us *which* residual
is worth chasing (genuine root error) vs which is the honest ceiling (sharedBass / secondaryDiatonic).

**Cost:** the full 6-tier port needs label-string tier logic + a parity-tested normalizer (their `rn_normalize.py`
= 986 fixtures, Scala-parity). Our `compare_rn` is a coarse 5-bucket cousin and would need the normalizer gaps
in §4 closed before its tiering is trustworthy. That is **medium** cost and **normalizer-sensitive** — exactly
the surface that bit them (the 2026-06-09 fairness audit) and us (the GT-parser re-baseline).

**Recommendation — PARTIAL, sequenced:**
1. **Now (cheap, normalizer-immune):** ship the **oracle-root pc gate** (§2) as the standing primary. It needs
   none of the tier machinery and reproduces the anchor split today.
2. **Next (low cost):** add a **3-tier collapse** on top, computed from data we already have:
   **`exact-root` (gate pass) / `convention-floor` (root differs but falls in a known defensible bucket —
   shared-bass `iii↔I6`/`V6↔vii°`, Cad⁶₄↔I⁶₄, vii°↔V, V/V↔II) / `genuine-root-error` (the rest)**. The
   convention-floor membership is a pc-relationship test (bass-sharing, cad-6/4 pattern) that does **not** need
   the full RN normalizer — it keeps the cheap normalizer-immune property while giving the genuine-vs-floor cut.
3. **Defer (medium, evaluate at Stage 5):** the full 6-tier Scala-parity ladder + normalizer unification.
   Justify it only if/when the learned chord-label re-ranker (§3.4 of the re-assessment) needs the finer
   `+inversion`/`+secondaryDiatonic` granularity to measure its +7pp claim out-of-sample. Until then the 3-tier
   collapse captures the genuine-vs-floor signal that matters for K1.

---

## §4 — Normalizer parity gaps (read-only; list + proposed fixes, nothing changed)

`compare_rn.normalise_rn` currently does: strip `[key]` prefix, strip `→/>` mod prefix, `% → ø`, drop
figured-bass parens `(…)`, and route the Italian-`It6` token to the root-only fallback. Diffed against the
Contrapunctus `rn_normalize.py` rule set (§10c), the following rules are **NOT handled** and could bias
**label/tier** agreement (they do **not** affect the §2 pc root gate):

| Gap | Contrapunctus rule | Our state | Bias risk | Proposed fix |
|---|---|---|---|---|
| **Aug6 collapse** | `Ger65/Ger7→Ger6`, `Fr6→Fr43` | absent | Ger/Fr land in root-only fallback (split_rn returns None) → tier under-credit | add aug6 canonicalization in `normalise_rn`; or, since DCML root_pc already roots aug6, keep root-gate-only (no tier credit) and document |
| **`/o7 → ø7`** half-dim shorthand | mapped | only `% → ø` | half-dim written `/o7` mis-tiers | add `/o7 → ø7` replace |
| **Tonicization slash keep-set** | slash-before-roman-letter = tonicization (KEEP, keep-set `{I,V,i,v,N,n,F,G,C}`); other slash = figured-bass (DROP) | `extract_quality` discards everything after first `/` | lowercase `/v,/vi,/vii` tonicizations conflated; this is the **exact bug** that inflated their rivals' numbers | implement the keep-set split in `normalise_rn` (kept tonicizations preserved, figured-bass slashes dropped) |
| **`#vii → vii` exact-tier-only** | strip only at exact tier, no-slash/local forms | not done | `#vii°↔vii°` typography mis-tiered | add at exact-tier comparison only (secondary `#viio65/ii` keeps the chromatic marker) |
| **Inversion shorthand** | `V2→V42`, `*63→*6` | not normalized | inversion-figure mismatches | add shorthand expansion |
| **Decorative `+` / `Δ` / unicode sub/superscript** | stripped/ASCII-folded | partial (`It6` only) | minor | fold unicode + strip decorative `+`, elide `Δ` |
| **N6 ≡ bII6 at exact** | notation identity, matches at exact tier | not handled | Neapolitan mis-tiered | treat as exact-tier identity |

**Crucial framing:** every gap above is a **label/tier** concern. The **oracle-root pc gate (§2) is unaffected**
— it compares `rootPitchClass` ints, and the DCML root_pc is derived by `dcml_parser`'s degree→pc logic
(already bug-fixed), not by these string rules. So: **the gaps are a precondition for §3 (tier ladder), not for
§2 (root gate).** Recommend closing them **only if the tier ladder is adopted**, and unifying via a single
parity-tested normalizer (their lesson, our GT-parser-re-baseline twin) rather than patching ad hoc.

---

## §5 — Integration shape & protocol changes

### 5.1 Dual gate (oracle-root primary, BIR secondary — not a replacement)
- **Oracle-root pc gate** (§2) becomes the **primary** standing gate; **BIR stays** as a secondary diagnostic
  (it still cheaply flags inversion/bass-position behavior). The re-assessment's §4 "dual metric standing"
  requirement is satisfied by reporting both per-preset case-identity sets.
- Hard-stop rule (mirrors the existing BIR rule): **any increase in the oracle-root case set in any preset
  (Baroque / Jazz / Default) is a hard stop**, evaluated as the case-identity set (not a bare integer), with the
  same anti-contamination manifest validation.

### 5.2 Minimal build (for after ratification — NOT built here)
- Smallest change: a sibling tool (or a `--oracle-root` flag on `characterise_bir_false.py`) that runs the
  **identical** load/validate/align pipeline **with line 162 removed** and emits the `music21_dcml_agree`
  case-identity set per preset. ~30 lines; reuses `validate_corpus_dir`, `align_*`, `three_way_classify`
  unchanged. Optionally fold in the §3.2 3-tier collapse.
- `analyze_inversion_errors.py` already computes the underlying set — the new tool is mostly its
  `music21_dcml_agree` collection re-emitted in `characterise_bir_false`'s stem@tick identity-set format.

### 5.3 Read-only baseline + acceptance, before any code lands
Because all inputs are on disk, **both** the new-baseline measurement **and** the §2.2 acceptance test are
**computable read-only from the existing corpora** (`baroque`, `jazz`, `baroque_kma_abs`) with **no analyzer
build**. Recommended ratification sequence: (1) compute the oracle-root baseline per preset read-only;
(2) run the acceptance check on the 25 anchor cases and confirm the **5/2** split (with the §2.2 DCML-coverage
caveat resolved); (3) only then wire the tool into the standing protocol.

### 5.4 Standing-protocol + CLAUDE.md changes
- `run_bach_preset.py`: **unchanged** (still regenerates the per-preset manifest-stamped corpus).
- `characterise_bir_false.py` step: **add** the oracle-root gate emission alongside the BIR emission (same dir,
  same validation).
- **CLAUDE.md "Gate threshold and preset policy":** add the oracle-root case-identity set (per preset) as the
  **primary** pre-commit gate, with BIR retained as secondary; re-baseline the three sets (will be supersets of
  57/23/57); state the hard-stop rule on oracle-root case-set growth. Note the pc-typed (normalizer-immune)
  property and the symmetric-dim7 floor exclusion.

---

## §6 — Stop-condition compliance & open question for reconciliation

- **No code/behavior/gate/scoring change made** — design only, HEAD `dd418ecfed`. ✓
- **Oracle-root data IS cleanly available read-only** (pc ints, 1:1/50%-overlap aligned, manifest-validated);
  no fabrication needed. The only flagged ambiguity is the §2.2 DCML-coverage check on the 7 acceptance cases,
  resolvable read-only. ✓
- **No threshold/scoring-term change** (that is post-ratify). ✓

**Open question for Cowork/user:** the gate oracle = `music21_dcml_agree` (both oracles must concur). This is
conservative and floor-honest, but it is **stricter** than the music21-only proxy the anchor dossier used to
derive the 5/2 split. Confirm the policy: **(A)** require DCML+music21 concurrence (recommended — excludes
oracle-disputed floor automatically), with a documented music21-only fallback where DCML coverage is absent; or
**(B)** DCML-authoritative with music21 as a tie-break only. Recommendation: **(A)**, pending the read-only
acceptance run confirming all 7 anchor cases retain DCML coverage.
