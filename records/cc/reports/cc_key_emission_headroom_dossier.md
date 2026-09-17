# CC Dossier — Key-Emission Headroom (Stage-4 emission-fix scoping)

*CC, 2026-06-13. Base `f8c6b3932a`. Investigation scopes the Stage-4 **emission**
fix: how much of the ~85% Class-B (the emission consistently prefers the wrong key)
is recoverable, by which mechanism. Method A–H. Read-only except the one authorized
diagnostic instrument (§2). Every number tagged `[probe]` (Python over committed
`.ours.json` + DCML) or `[dump]` (the new key-candidate instrument) or `[code]`.*

> **Headline.** The Class-B bulk is **not** one phenomenon. It splits at a single
> structural fault line — **how the resolver handles the declared (notated) mode** —
> which is mis-set at *both* extremes: **dropped entirely for empty (0-fifths)
> signatures** (73 stems → 625 of the 1032 S2 regions are pure emission, 349
> relative-pair ones reachable by *restoring* it), and **trusted absolutely via a
> −7.0 penalty for non-empty signatures** (127 relative-pair S2 entrenched on a
> notation-vs-DCML convention disagreement — mostly ceiling). The term-level dump
> proves it: in every anchored case the correct key loses by **exactly the −7.0
> declared penalty**; in every zero-sig case the relative pair is a **near-tie**
> (gap 0.0–0.34) decided by the ±0.20 Ionian-vs-Aeolian prior. **Recoverable by a
> structural emission fix: ≈ 349 + a partial-signature subset (≈ 34–44 % of S2);
> fitted (Stage-5): small; genuine ceiling: ≈ 127 + the dominant-reading tail.**

---

## §1 — Tier-1 structural decomposition (no build; committed `.ours.json` + DCML)

**Corpus:** `tools/corpus/default` (the live config), 326 WiR-covered Bach chorales,
10 108 matched regions. **S2 = 1032 (10.2 %)** — reproduces the design report exactly
[probe `/c/tmp/task1_decomp.py`, which reuses `compare_analyses` + `compare_rn.classify_pair`
+ `dcml_parser` verbatim, like the §3 derivation probe].

### 1.1 Cause split (Method A)

```
S2 = 1032
  relative major/minor of DCML global :  509  (49.3%)
  parallel (same tonic, diff mode)    :    0  ( 0.0%)
  fifth-related (our tonic ±4th/5th)  :  333  (32.3%)
  other                               :  190  (18.4%)
  ----
  single-key stem (our key NEVER changes): 153 (14.8%) over 16 stems  [rel 128 / nonrel 25]
  DCML global present as our runner-up   : 499 (48.4%)
  our key == DCML LOCAL key              :   0 ( 0.0%)   <-- not tonicization-tracking
  deviation (mostly-right stem)          : 106 (10.3%)   path-fixable ceiling (design report)
  mostly-wrong stem                      : 926 (89.7%)   the emission bulk this report scopes
```

The **0/1032 "our == DCML local"** result [probe, local_key parses 974/974] is load-bearing:
our wrong keys match **neither** the DCML global **nor** the local key, so the Class-B
bulk is **genuine wrong-key emission**, not a region we read as a local tonicization that
DCML scored against the global (that escape hatch is empirically empty here).

### 1.2 The fault line — declared-mode handling, read via the piece-start anchor (Method B)

The resolver's declared mode is `KeySigEvent::mode()` [code `keyresolver.cpp:225`], **not**
the xml `<mode>`. The reliable detector of what the resolver *actually saw* is the
**piece-start anchor**: region 0 with `keyConfidence == 0.5` AND `keyModeRunnerUp == null`
fires iff `declaredMode.has_value()` [code `keyresolver.cpp:263`]. Cross-tabulating it
against signature emptiness [probe `/c/tmp/task1_anchor.py`]:

```
                       fifths==0   fifths!=0
  anchored (decl set)      0          252
  NOT anchored (decl none)  73           1     <-- bwv62.6 the lone anomaly
```

**Near-perfect correlation: the declared mode is present iff the signature is non-empty.**
All 73 zero-fifths stems lose their declared mode — confirmed directly by the instrument:
`declaredModeOrdinal = -1` on every zero-sig region dumped [dump]. The xml *carries* the
mode (e.g. bwv153.9 `<mode>major</mode>`, bwv254 `<mode>minor</mode>`), so this is a
**MuseScore key-signature import behavior**: an empty signature yields `KeyMode::UNKNOWN`
and the `<mode>` is not propagated. Consequence cascade — for a 0-sig stem the resolver
loses **(i)** the piece-start anchor, **(ii)** the −7 declared-mode penalty, **(iii)**
`partialSignatureCorrection` (all three are gated on `declaredMode.has_value()`).

### 1.3 The two populations of Class-B (Method C)

Crossing cause × anchor [probe `/c/tmp/task1_anchor.py`]:

```
                 anchored(decl set)   emission(zero-sig)   total
  relative              127                  382            509
  fifth-related         183                  150            333
  other                  97                   93            190
  ----                  407                  625           1032
  single-key-stem S2:   139                   14            153
```

- **ANCHORED-relative = 127.** ALL 127 have the notated mode-class **disagreeing** with the
  DCML global mode-class [probe] — i.e. the notation calls the piece (say) D-minor while
  WiR's global key is its relative F-major. The −7 penalty then makes the DCML key
  unreachable. 12 stems: `bwv166.6, bwv24.6, bwv244.40, bwv244.54, bwv245.14, bwv245.3,
  bwv261, bwv274, bwv314, bwv384, bwv393, bwv96.6`. 139 of the 153 single-key floor are
  these (a wrong anchored declaration is wrong on every region → consistent error).
- **EMISSION zero-sig = 625** (382 relative + 150 fifth + 93 other): pure pitch analysis
  (no anchor, no penalty, no partial-sig). Of the **382 relative**, the notated `<mode>`
  **agrees** with DCML global on **349** (and disagrees on 33, absent on 0) [probe
  `/c/tmp/task1_final.py`] — so *restoring* the dropped mode would entrench **349**
  correctly. The zero-sig fifth/other bulk includes Baroque partial-signature cases
  (bwv254 = d-minor notated 0-fifths) that the dropped mode prevents correcting.

---

## §2 — The diagnostic instrument (AUTHORIZED build; byte-identity-gated)

**What it is.** A read-only `--dump-key-candidates TICK[,TICK]` flag on `batch_analyze`.
For each region whose `[startTick,endTick)` contains a requested tick, it re-runs the
per-region key resolution (threading `prevKey` over the produced regions, mirroring
`regionanalyzer`'s loop) with a diagnostic dump enabled, and emits, **per candidate
(252 = 12 tonics × 21 modes)**, the six `KeyModeAnalyzer` scoring terms already computed
internally — `scaleMembership`, `triadEvidence`, `characteristicPitch`, `trueLeadingTone`,
`keySignatureProximity`, `modePrior` — plus the declared-mode penalty, the post-hoc
disambiguation delta, the tonal-centre family-selection score, and the resolver context
(notated/corrected fifths, declared-mode ordinal, path taken, lookahead beats, hysteresis /
strong-prior promotion flags, production key, resolved winner).

**Design (the snapshot/gateCtxOut precedent).** Optional trailing `dumpOut` pointers,
defaulting to `nullptr`, on `KeyModeAnalyzer::analyzeKeyMode` and
`keyresolver::resolveKeyAndModeRanked`; a `KeyCandidateScore` / `KeyResolveDump` struct.
When null (every production path) the functions are byte-identical — the dump only
*serializes scores already computed* (the six terms are recovered from the stored
`CandidateEvaluation` plus a deterministic recompute of the three tonic/mode-local terms;
the disambiguation delta is `finalScore − Σterms + declaredPenalty`). The emission scores
are **prevResult-independent**, so the term breakdown is exact regardless of the prev chain.

**Byte-identity holds** (the proof gate — all green):
- composing_tests **505/505**, notation_tests **57/57** [proof].
- pipeline_snapshot_tests **11/11 zero-diff**, no golden refresh [proof].
- Baroque corpus sha256: **0 differ / 25** spot (the 13 floaters + every §3 sample stem +
  corelli) [probe `byte_identity_spot.sh`]; **full 0 differ / 353** [probe
  `byte_identity_full.sh`] — the dump does not touch the winner, as designed.

**Commit:** `a4ae4a9203` `feat: read-only key-candidate diagnostic dump (Stage-4 emission instrument)`.
Files: `keymodeanalyzer.{h,cpp}`, `keyresolver.{h,cpp}`, `tools/batch_analyze.cpp`.

One honest caveat surfaced by the instrument (no byte-identity failure): `candidates[0]`
is the raw-score argmax, but the **actual** emission winner is the *family/tonal-centre
selection* [`keymodeanalyzer.cpp:615–663`], which can differ (it did on bwv254/bwv245.15 —
§3.4). For the relative and anchored cases they coincide (verified: `candidates[0]` ==
`resolvedWinner` == `productionKey`), so the §3 term attribution is exact there; for the
fifth/other cases the mechanism is the family selection itself, reported as such.

---

## §3 — Tier-2 causal attribution (term-level, real numbers per window) [dump]

19 windows across all populations (`/c/tmp/task3_run.sh` + bwv254/bwv245.15). Each row:
the gap `winner − correct`, then the term(s) that account for it. Full traces in
`/c/tmp/task3_out.txt`.

### 3.1 ANCHORED-relative → the term is `declaredPenalty` (−7.00), unambiguously

| window | winner / correct | gap | `declaredPenalty` | next term | correct-key rank |
|---|---|---|---|---|---|
| bwv244.54 @960  | Dmin / **F** | +7.79 | **−7.00** | triad +0.99 | 10/252 |
| bwv244.54 @2880 | Dmin / **F** | +7.39 | **−7.00** | triad +0.59 | 8/252 |
| bwv244.54 @10080| Dmin / **F** | +7.14 | **−7.00** | triad +0.34 | 6/252 |
| bwv244.40 @1440 | F#min / **A**| +6.85 | **−7.00** | lt −1.20 / triad +1.25 | 6/252 |
| bwv244.40 @6240 | F#min / **A**| +5.73 | **−7.00** | lt −1.20 | 6/252 |
| bwv166.6 @960   | Bbmaj / **g**| +6.79 | **−7.00** | triad −0.41 | 10/252 (strongPrior fired) |
| bwv166.6 @1920  | Bbmaj / **g**| +6.89 | **−7.00** | triad −0.31 | 11/252 (hyst fired) |
| bwv261 @4320    | Bmin / **D** | +6.43 | **−7.00** | triad −0.37 | 7/252 |
| bwv261 @5760    | Bmin / **D** | +6.80 | **−7.00** | prior −0.20 | 7/252 |

Read it directly: the correct key is rank 6–11 **only** because its mode class eats the
−7.00 declared penalty; strip the penalty and it sits within ~0.3–0.8 of the winner (≈ rank 2).
The other five emission terms are noise here. **This is a declared-mode-trust (structural)
issue, not a fitted-weight balance.** The notated mode genuinely *is* the relative of DCML's
analytical call (bwv244.54 notates D-minor, WiR globals F-major), so the resolver is
faithfully following the score; DCML disagrees.

### 3.2 EMISSION zero-sig relative → near-tie decided by `modePrior` (±0.20) + `triad` (±0.5)

| window | winner / correct | gap | dominant term(s) | note |
|---|---|---|---|---|
| bwv153.9 @2880 | Amin / **C** | +0.15 | triad +0.35, prior −0.20 | correct rank 2 |
| bwv25.6 @10560 | Amin / **C** | +0.34 | triad +0.54, prior −0.20 | hyst → prod Cmaj (fixed) |
| bwv153.5 @10560| Amin / **a** | +0.00 | emission **prefers correct**; prod Cmaj via prev-chain | path error, not emission |
| bwv16.6 @1920  | Cmaj / **a** | +0.08 | **prior +0.20**, triad −0.12 | Class-A spurious flip |
| bwv420 @12960  | Cmaj / **a** | +0.06 | **prior +0.20**, triad −0.14 | Class-A spurious flip |

The relative pair shares every diatonic note, so the emission is a **dead heat** (gaps
0.0–0.34). The decisive quantities are the **+0.20 Ionian-over-Aeolian prior**
(`modePriorIonian 1.20 − modePriorAeolian 1.00`) and **sub-0.5 triad-evidence** differences.
The prior is doing exactly its designed job (break ties toward the commoner mode) — and
breaks them the wrong way on these windows. Note bwv153.5 @10560: the **emission is correct**
(Amin 60.46 > Cmaj 60.43); the S2 error is the *prev-chain/hysteresis* holding Cmaj — a
path error, not emission (path-fixable, Class-C-like).

### 3.3 ANCHORED fifth / Class-C → `modePrior` (+1.50 Aeolian-vs-Dorian), tail is a hysteresis trap

| window | winner / correct | gap | dominant term(s) |
|---|---|---|---|
| bwv343 @480   | Dmin / **g** (GDor) | +2.27 | **prior +1.50**, triad +0.77 |
| bwv343 @1920  | Dmin / **g** (GDor) | +2.48 | **prior +1.50**, triad +0.98 |
| bwv343 @19200 | Dmin / **g** (Gmin) | **+0.01** | lt −1.20, scale +0.61, ksp +0.60 (near-tie tail) |

bwv343 declares minor but reads **D-minor for g-minor** (the dominant, *non*-relative). No
declared penalty fires (both minor-class). The driver early is `modePrior` (Aeolian +1.00 vs
Dorian −0.50 = **+1.50**) plus the dominant's tonic-triad support; by the tail the emission is
a **+0.01 tie** that hysteresis traps on the wrong key (the design report's Class-C late tail —
path-fixable by a global decode).

### 3.4 EMISSION zero-sig fifth / "other" → family-selection + the dropped-mode disabling partial-sig

| window | production / correct | mechanism |
|---|---|---|
| bwv254 @960  | **Amin** / d | raw-argmax=Fmaj, **family-selected=Amin**; d-minor notated 0-fifths → `partialSignatureCorrection` never runs (declMode dropped) → signature-locked to the 0-sig Aeolian home |
| bwv254 @4800 | **Amin** / d | same; emission argmax is *Dmin* (correct) but the 0-sig family lock + prev-chain holds Amin |
| bwv245.15 @1440 | **EPhrygDom** / a | **raw-argmax = Amin (correct!)**; the tonal-centre family selection prefers the locally-complete E-dominant (V-of-a) triad |
| bwv245.15 @1920 | **BLoc#6** / a | same dominant/exotic-mode family pick |

These are **not** a single emission term. bwv254 is a Baroque **partial-signature** case
(d-minor written without the B♭) — the dropped mode disables `partialSignatureCorrection`,
which *would* detect pervasive B♭ and correct 0 → −1 (anchoring D-minor); bwv254 notates
`<mode>minor</mode>`, DCML global = d [probe], so restoring the mode fixes it structurally.
bwv245.15's wrong key is the **family/tonal-centre selection** preferring the sounding
dominant — a tonicization-reading the path/Stage-6 should resolve.

---

## §4 — Fix scoping + Stage-4 shape

### 4.1 The structural / fitted / ceiling split

| bucket | size (of S2=1032) | mechanism (§3) | fix class |
|---|---|---|---|
| **A. Zero-sig relative, notation agrees w/ DCML** | **349** | mode dropped → near-tie flips | **STRUCTURAL** — restore declared mode for 0-sig → −7 entrenchment dwarfs the 0.2–0.5 noise |
| **B. Zero-sig fifth/other, partial-signature** | subset of 243 (e.g. bwv254) | mode dropped → no partial-sig | **STRUCTURAL** — restoring mode re-enables `partialSignatureCorrection` |
| **C. Zero-sig dominant-reading / family pick** | subset of 243 (e.g. bwv245.15) | tonal-centre prefers sounding V | **STAGE-6 / path** (tonicization label, not a key change) |
| **D. Residual zero-sig near-ties** | part of 382 | ±0.20 prior / triad swing after entrenchment | **FITTED (Stage-5)** — small; mostly subsumed by A |
| **E. Anchored fifth (Class-C)** | 183 | modePrior +1.5; tail hysteresis-trapped | **FITTED (prior) + PATH (tail)** |
| **F. Anchored relative, notation ≠ DCML** | **127** | declaredPenalty −7.0 on a convention disagreement | **CEILING** (resolver follows the notation; a small structural lever exists, risky) |

**STRUCTURAL — the highest lever (bucket A, ~349, + a partial-sig slice of B).** One fix:
**import the notated `<mode>` for empty key signatures** (read the MusicXML `<mode>` directly,
or fix the engraving import to retain `KeyMode` at 0 fifths), so `declaredMode` is set for the
73 zero-sig stems. This single change re-enables anchor + the (graded) declared prior + the
partial-sig correction for all of them. Reach: **349 relative (high confidence — the dump
shows the −7 advantage swamps the sub-0.5 emission noise) + the partial-sig fifth subset**.
≈ **34–44 % of S2** — *exceeding* the path-only Class-A/C estimate, exactly as the
meta-principle predicts (precision is emission, not search). **Risks, quantified:** the **33**
zero-sig relative stems whose notation disagrees with DCML would entrench wrong (they are
already wrong — no net loss, they merely join bucket F); and a hard −7 lock would over-constrain
genuinely-modulating 0-sig pieces — which is **why the lock must become a graded prior**, not
a −7 wall (next paragraph).

**FITTED (Stage-5) — small (buckets D, part of E).** The ±0.20 Ionian-vs-Aeolian prior and the
+1.5 Aeolian-vs-Dorian prior are mis-balanced for these windows, but reweighting them is a
global tie-breaker that just moves errors between pieces — consistent with the design report's
"Stage-5 = the fitter, ~1.3 %." Leave the numbers to the Stage-5 DCML-objective fit; do **not**
hand-tune them in Stage 4.

**CEILING (bucket F, ~127, + the dominant-reading tail of C).** The 127 anchored-relative are a
**notation-vs-analyst convention disagreement** — the resolver faithfully reports the notated
key; WiR's global-key choice differs (which relative is "the" tonic). The metric penalizes us
for trusting the score. A structural lever exists (let overwhelming relative-triad/cadence
evidence override the declared penalty) but it is high-risk: the −7 penalty is what keeps
**correctly-notated** anchored scores (the other ~240 anchored stems, mostly correct) from
flipping to their relative. Recommend routing the 127 to **accepted ambiguity** for Stage 4,
revisiting only under the Stage-6 label contract (a `KeyArea` that can carry "notated key X,
analytical key its relative" is the honest representation).

### 4.2 Recommended Stage-4 shape

The data **confirms** the design report's reframe and **sharpens** it: the Class-B bulk is an
**emission** problem rooted in declared-mode handling, not a search problem. Stage 4 should be:

1. **Fix the declared-mode import for empty signatures** (structural, do now). Highest single
   lever (~349 + partial-sig). Gate it exactly as a 3.2-class behavior change: Baroque BIR
   (13/7 identity sets) + pipeline snapshots + DCML-adjudicate every movement. This is an
   emission fix that the byte-identity era ends on (the resolved key feeds `analyzeChord`).
2. **Make the declared mode a graded HMM prior / initial-state, not a −7 wall.** The path's
   modulation penalty (λ) then supplies *graded* stickiness toward the declared/global mode —
   resisting the bucket-A/D near-tie flips and the bucket-E/Class-C tail (the bwv153.5 @10560
   and bwv343 @19200 path errors) **without** the −7's inability to ever modulate. This is the
   KeyArea scaffold; λ is co-ratified with the Stage-6 label contract (design OQ-1).
3. **Leave the prior weights to Stage-5** (bucket D), and **route bucket F (127) + the
   dominant-reading tail (C) to accepted ambiguity / Stage-6** — the KeyArea must be able to
   represent "notated key ≠ analytical key" and "this region tonicizes V" rather than forcing a
   single wrong global label.
4. **KeyArea spans + hysteresis supersession** remain as the design report has them (independent
   of the S2 shrink).

Net: Stage 4 = **(emission) declared-mode import fix + graded declared prior** (the ~349+
recoverable) **+ KeyArea spans + hysteresis→path supersession**; **Stage 5** fits the residual
prior balance; **Stage 6** owns the 127 convention cases and the dominant-reading tail; the
**HMM/search** path remains deferred — it cannot move an error the emission consistently
prefers (re-confirmed: 0/1032 track DCML-local; the bulk is genuine emission).

---

## §5 — Unknowns / what I did not (or could not) pin

1. **The exact root of the mode-drop.** Proven at the resolver boundary (`declaredModeOrdinal
   = -1` for all 0-sig [dump]; xml carries `<mode>` [probe]); I did **not** read the MuseScore
   MusicXML/keysig import to confirm *where* `KeyMode::UNKNOWN` is assigned at 0 fifths. The
   fix in §4 is robust to this (read the xml mode, or fix the import) but the precise import
   site is unverified. `bwv62.6` (the lone non-zero-sig non-anchored anomaly) is also unexplained.
2. **The realized reach of the restore fix.** I measured *reachability* (349 relative agree;
   bwv254-class partial-sig) but did **not** build the fix and re-measure S2 — that is the
   Stage-4 build's decision A/B (and it ends byte-identity, so it is out of scope here). The
   349 is high-confidence (the −7 advantage swamps the sub-0.5 noise per §3.2) but the
   partial-sig subset of bucket B is bounded only by the 3 %/2× thresholds firing, not counted.
3. **bucket B/C sizing inside the 243 zero-sig fifth+other.** I sampled bwv254 (partial-sig)
   and bwv245.15 (dominant-reading) but did not classify all 243 — needs a per-region
   partial-sig-vs-dominant discriminator. Reported as "subset," not an integer.
4. **The family-selection / tonal-centre mechanism** (bwv254, bwv245.15) interacts with
   hysteresis and the prev-chain; my dump threads `prevKey` over post-merge regions, which can
   diverge from production for a minority of regions (the `resolvedWinner` ≠ `productionKey`
   cases). The **emission term breakdown is exact** (prevResult-independent); the *winner
   identity* for those few is the caveat in §2. Quantifying how much of bucket C is family-pick
   vs hysteresis needs a prev-chain-faithful re-run (Stage-4 build).
5. **Non-Bach S2 structure.** Measured on Bach (the only WiR-covered homophonic gate set).
   Whether cross-corpus zero-sig drops mode identically — and whether its declared-mode handling
   is the same fault line — is unmeasured (a Stage-4-measure task).

---

*Stop-condition disclosures.* (a) The byte-identity gate held — the instrument committed on
green per its explicit authorization (§2). (b) No dump-perturbs-winner finding (the opposite —
0/353). (c) The discovery that the Class-B bulk is **mostly an emission/declared-mode fault**,
with a concrete ~34–44 % structural lever, *reshapes* Stage 4 toward the emission import fix +
graded prior (§4.2) and routes the 127 convention cases to accepted ambiguity — reported as the
primary scoping finding, not implemented (this run scopes only). (d) No scope creep into the fix.
