# CC Investigation — Cadence→Key: does a global/cadential signal close the relative-pair floor?

**Date:** 2026-06-14 · **Status:** HELD — **READ-ONLY derivation, NO production change, NO commit, NO
build.** Base = committed 4b-i (`ef30cc70f3`) + local 4a (`cfc7eb5e39`, HEAD). Reuses the on-disk 4b-i
floor corpora (`tools/corpus/default_4bi{,_abs}`) and the `compare_rn` L1 instrument. Every number tagged
`[probe]` (measured), `[code]` (read at source), `[oracle]` (DCML/music21 via When-in-Rome), `[theory]`
(music-theoretic/literature), `[unknown]` (stated, not guessed).

**Verdict (one line):** A cadence→key signal **does** supply the missing relative-pair signal and **does**
escape the §4 coupling — **structurally, by being a piece/section-scoped global anchor, not a window-local
term** — and it addresses **≈91 % of the Default mode-absent floor (1259 of +1383 regions)**. **But the
existing cadence detector cannot be wired in: it is downstream of and circular with key resolution.** The
recommendation is **(A) build a new, key-agnostic cadence→key anchor as the next hand-built Stage-4 step**,
with a small genuinely-different residual (the mode-invariant "other"/different-key class, ≈22 % of the
floor S2, incl. bwv83.5) reserved for Stage 6. This is **not** a falsification — it is a green light for A,
with a sizing caveat (new detection work required) and a reliability contingency.

---

## 1. The cadence machinery at source — what it produces, and why it is unusable as-is `[code]`

Located: `src/composing/analysis/section/sectionanalyzer.{h,cpp}` (the Stage-2.1 / Phase-4c relocation,
header lines 82–142; impl `detectCadences` 156–239, `detectPivotChords` 241–354). Findings, all read at
source:

1. **It is DOWNSTREAM of key resolution and CIRCULAR with it.** `detectCadences` decides PAC/PC/DC/HC from
   `chordResult.function.degree` — and `function.degree` is computed *from* the already-resolved
   `keyModeResult` (`sectionanalyzer.cpp:114`, `diatonicDegreeForRootPc(rootPc, keySignatureFifths, mode)`;
   the PAC test is literally `b.function.degree==0 && a.function.degree==4` at `:198–200`). It cannot
   inform the key decision because it presupposes the key decision.

2. **It is gated on assertive confidence — silent EXACTLY on the floor.** Both regions of every cadence
   pair must pass `hasAssertiveKeyConfidence` = `normalizedConfidence ≥ 0.8` (`:153, 175–176, 227`). The
   floor population is *by construction* the sub-1.0-hint near-ties (4b-ii §4); those regions do not carry
   assertive confidence, so the detector emits nothing for them. It fires only where the key is already
   decided confidently — the opposite of where the signal is needed.

3. **It requires a single stable key across the cadence pair** (`:184–188`: a key/mode change between the
   two regions → "not a cadence" → skipped). So it can never *select between* two candidate keys; it only
   labels motion *inside* one settled key.

4. **It emits a TYPE LABEL at a tick, never a key/degree resolution.** Output is `CadenceMarker{int tick,
   std::string label}` with `label ∈ {PAC, PC, DC, HC}` (`:93–96`). There is no "this cadence implies
   tonic X / mode Y" output anywhere.

5. **Nothing wires it to key scoring.** Grep of `src/composing/analysis/key/` for `cadence` → **0 hits**;
   every consumer of `detectCadences`/`detectPivotChords` is notation-side annotation/display
   (`notationcomposingbridge.cpp`, `notationimplodebridge.cpp`, the implode/annotate/snapshot tests). This
   **confirms 4b-ii §2** at source: no cadence term feeds `analyzeKeyMode`/`keyresolver`.

**Sizing finding (stop-condition triggered):** *The detector does not produce a usable key/degree
resolution — only a key-presupposing cadence flag.* Per the run's stop-condition, I report what would be
needed rather than build it. A cadence→key signal requires a **new, key-agnostic cadence pre-scan** that
runs **before** resolution: detect structural dominant→tonic resolutions by *root motion* (descending
fifth / leading-tone resolution) and *the presence of the minor's raised leading tone*, key-independently,
and **vote for a tonic+mode**. The existing `detectCadences` is the wrong tool (downstream); the *score
walk* it does is reusable as a template, but the gating and degree-from-key logic must be replaced.

---

## 2. The floor population, measured and decomposed `[probe]` `[oracle]`

Reusing the on-disk 4b-i corpora and a read-only classifier (`tools/cc_floor_classify.py`, written this
run — opens `.ours.json` + WiR rntxt, reuses `compare_rn`'s alignment, `classify_pair`,
`key_disagree_subtag`, and the `_our_key_tonic`/`_dcml_key_tonic` parsers; redefines **no** metric; writes
nothing). It sub-classifies every **S2** region (genuine key error, our key ≠ DCML global) by the
*relationship* between our key and the DCML global key:

| Default S2 (genuine key error) | mode-present (ceiling) | mode-absent (FLOOR) | floor−ceiling Δ |
|---|---:|---:|---:|
| **S2 total** | **687** | **2070** | **+1383** |
| relative_pair (our = relative maj/min of DCML global) | 193 (28 %) | **1452 (70 %)** | **+1259 (91 % of Δ)** |
| parallel (same tonic, opposite mode) | 0 | 0 | 0 |
| other (different key — dominant/subdominant/unrelated) | 411 (60 %) | 454 (22 %) | **+43 (3 %)** |
| keyfail (our key string unparseable) | 83 (12 %) | 164 (8 %) | +81 (6 %) |

**Reading.** The +1383 floor is **91 % relative-major/minor confusion** (1259 regions). The declared mode
was almost entirely a *relative-pair* tiebreaker: drop it and relative-pair S2 explodes 193→1452, while the
"other"/different-key class is **nearly mode-invariant** (411→454, +43) — declared mode never fixed those
either. `parallel` (C-major-vs-C-minor) is empty: the mode confusion is **relative**, not parallel. This is
exactly the population a cadence→key signal targets, and it is cleanly separable from the residual.

Example relative-pair floor regions `[probe][oracle]`: `bwv10.7 ours=B♭maj / DCML g` (B♭ is the relative
major of g), `bwv33.6 ours=C / DCML a`, `bwv328`, `bwv187.7`, `bwv289`, `bwv342` … (the 25 heaviest stems
listed by the classifier). Example "other" residual regions: `bwv102.7 ours=Gmin / DCML c` (the Δ=+7a
dominant-minor case), `bwv10.7 ours=Cmel / DCML g`, `bwv83.5 ours=a / DCML d`.

---

## 3. Q-CENTRAL — derived on real floor cases: the signal IS decoupled `[probe]` `[oracle]` `[theory]`

**Q-CENTRAL restated:** on the floor near-ties, does the cadential/global evidence point to the *correct*
relative, AND is it decoupled from local salience — can it win these mode-absent **without** overriding the
correct 1.0 hint mode-present?

### 3.1 — Does cadence point to the correct relative? — YES, by the strongest cue in tonal music `[theory]`
The relative pair C-major ↔ A-minor shares a key signature; the *only* reliable disambiguator is **where
the structural cadences land and with what dominant**: a major piece cadences `G(7)→C` (diatonic dominant,
no accidental); the relative minor cadences `E(7)→Am` carrying **G♯, the raised leading tone — a note
foreign to the shared 0-sharp signature**. The presence of a structural `V–i` with the minor's raised LT at
a phrase end is the textbook, near-decisive marker of the minor relative (Temperley's key-finding line
explicitly notes that key-finding error concentrates on the relative major/minor pair and that
cadential / leading-tone cues resolve it; HarmAn, Pardo & Birmingham, anchors labeling on the same
dominant→tonic motion). This is precisely the signal the declared mode was proxying.

### 3.2 — Why this is NOT 4b-ii's failed B1 lever — the decoupling is the *scope* `[code]` `[theory]`
4b-ii's B1 ("raise `tonalCenterLeadingTone`") **failed** because it weighted the minor's LT (G♯)
**uniformly across every region** — so every vi-tonicization *inside a major piece* fired it, drifting the
corpus toward minor (4b-ii §2.3, net +85/+67 present, +241/+206 absent). A cadence→key signal counts that
same G♯ **only when it is part of a structural dominant resolving to a candidate tonic at a phrase
boundary** — integrated over the piece, not summed per window. The difference between B1 and cadence is not
*what* is measured (both look at the LT) but *at what scope*: window-local salience (B1) vs
piece/section-level cadential structure (cadence). **Scope is the decoupling.**

### 3.3 — The coupling-escape test, derived against the present↔absent data `[probe]`
4b-ii §4's coupling: any **local-window** term strong enough to win the floor near-ties mode-absent also
overrides the correct 1.0 hint mode-present, because both decide the *same* sub-1.0 population. A cadence
anchor escapes this for two compounding reasons, both verifiable in the §2 table:

- **It is not a window term.** A cadence→key signal sets the **global** (tonic, mode) once, from cadences
  integrated over the piece, then anchors per-region resolution to it — *mechanically identical to how the
  declared mode worked* (a global anchor applied per region, `keyresolver`/`keymodeanalyzer`). It therefore
  does not compete with local salience region-by-region; it overrides it globally. The §4 coupling is a
  property of *window-local* terms and does not apply.
- **A correct cadence signal AGREES with the hint.** Mode-present, the 1259 relative-pair regions the hint
  recovers (1452−193) are *already correct*; a cadence signal pointing to the same resolution relative
  **reinforces** them (no flip) while supplying the same answer mode-absent. The measured proof of
  agreement: mode-present relative_pair S2 is only **193** — i.e. on 1259 relative-pair regions the
  notated-mode anchor and a correct cadence anchor would return the identical (correct) key. There is no
  population on which a *correct* cadence signal must fight a *correct* hint. The only residual risk is
  **detection error**, which is bounded by detector quality — a reliability question, not the structural
  coupling that killed reweighting.

**Q-CENTRAL answer: DECOUPLED — the fix is viable** for the relative-pair class (≈91 % of the floor),
contingent on (a) building new key-agnostic cadence detection (§1), and (b) cadence reliability
approaching notated-mode reliability on this population (§4 caveat).

### 3.4 — Named cases `[probe]` `[oracle]`
| stem | DCML global `[oracle WiR]` | S2-class (absent) | reading |
|---|---|---|---|
| bwv33.6 | a minor | relative_pair (14) | relative-pair; cadence-addressable; already mostly recovered mode-absent (4b-i) |
| bwv365 | a minor | relative_pair (4) | relative-pair; recovered mode-absent (4b-i); cadence would secure it |
| bwv64.2 | **C major** | relative_pair (1 absent / 20 present) | **see correction below** |
| bwv83.5 | d minor | **other (10 absent / 14 present)** | different-key residual (reads a-minor = dominant of d); **mode-invariant** → Stage 6, NOT cadence-relative |

**Honest discrepancy flagged (never-guess):** 4b-ii §3 characterized **bwv64.2** as "G major, read A-minor,
hard different-key class." Measured against the WiR rntxt here, bwv64.2's **global key is C major**, and it
classes as a **relative-pair** (A-minor is the relative minor of C). Mode-absent it has only **1** S2
region (nearly clean); mode-**present** it has **20** (the declared-mode over-lock — the same +19 outlier
4a flagged). So under this metric bwv64.2 is *not* a different-key hard case and is *not* helped by the
declared mode — it is mildly *hurt* by it. I report the measurement and flag the conflict with 4b-ii's
table rather than reconcile by guess; the likely cause is that 4b-ii read the *piece-start resolved key*
(one region) while this aggregates all S2 regions, but I have not verified that and do not assert it.
**bwv83.5 is the clean residual exemplar:** `other`, different-key, and mode-invariant (present ≈ absent) —
declared mode never fixed it, so cadence-relative logic won't either; it is a genuine Stage-6 case.

---

## 4. Recoverable fraction + residual `[probe]`

Sizing against the **Default +1383 floor gap** (mode-absent 2070 − mode-present 687):

- **Cadence-addressable (relative-pair) — upper bound ≈ 1259 regions ≈ 91 % of the gap.** This is the
  **hint-parity ceiling**: the number of relative-pair regions the notated-mode anchor recovers
  (1452−193). A cadence→key anchor that replicates the notated mode's accuracy on the relative axis
  recovers this set. **It is a ceiling, not a measured recovery** — the realized fraction equals
  (cadence-detection accuracy on the relative pair) × 1259, and is < 1259 wherever a piece has no clear
  structural cadence, has conflicting cadences (modulating chorales), or the pre-scan misreads the dominant.
  Tagged `[probe ceiling]`; the realized number requires building the detector (out of scope).
- **Residual genuinely unreachable by relative-pair cadence logic ≈ the rest:**
  - **"other"/different-key ≈ 454 (22 % of floor S2), mode-INVARIANT** (present 411 ≈ absent 454). This is
    the bwv83.5 / bwv102.7 (Δ=+7a) class — our per-region key is a *different* key (dominant/subdominant),
    not the relative. Declared mode never fixed it; cadence-relative logic won't either. **→ Stage 6 /
    richer emission.** (A *general* cadence-anchored global key — not just relative disambiguation — might
    recover the subset of these that have a clear final cadence on the true tonic, but the dominant-read
    cases, where a V chord is mistaken for a tonic, are exactly where cadence detection is hardest; treat as
    residual.)
  - **keyfail ≈ 164 (8 %)** — our key string unparseable; an emission/formatting issue orthogonal to
    cadence.
  - **The ~193 relative-pair regions the notated mode itself cannot fix** — interior tonicizations / genuine
    local ambiguity; the irreducible relative-pair tail.

**A-vs-B read:** the recoverable fraction by a **hand-built global cadence anchor is large (≈91 % of the
floor gap)** and the genuinely-different residual is **small and mode-invariant (≈22 % of floor S2)**. Per
the run's framing (large residual ⇒ B; small residual ⇒ A suffices), this points firmly to **A
(hand-built) for the key axis**, with **B reserved only for the mode-invariant "other" residual at Stage 6.**

---

## 5. Calibration + recommendation `[theory]` `[code]`

**Literature.** Cadence-anchored relative resolution is a **known-sound** approach. The
Krumhansl-Schmuckler / Temperley key-finding line documents that (i) the dominant error mode of pitch-based
key finders is the **relative major/minor** swap, and (ii) the corrective cue is **cadential / leading-tone
voice-leading** (the raised LT at `V–i`). HarmAn (Pardo & Birmingham 2002) segments and labels off the same
dominant→tonic motion. So a phrase-/cadence-anchored relative resolver sits squarely on published, sound
method — it is *adding a missing modality* (cadential structure), not reweighting the present one, which is
exactly what 4b-ii's structural-insufficiency verdict prescribed.

**Recommendation — (A) build cadence→key as the next hand-built Stage-4 step, with the wiring sketch below.**

Concrete wiring (composing-zone; hand-built; no learned model):
1. **New key-agnostic cadence pre-scan** (new code, runs *before* `analyzeKeyMode`, does **not** read the
   resolved key — this is the part the existing `detectCadences` cannot supply, §1). For each phrase
   boundary (chorale fermatas are natural markers), detect a structural dominant→tonic resolution by
   *root motion* (descending-fifth bass) and *leading-tone resolution*; for each candidate tonic accumulate
   a cadential weight, with the **raised LT of the minor** (E→Am with G♯) vs the **diatonic dominant of the
   major** (G→C) as the relative discriminator. Integrate over the piece/section → a global
   `(tonicPc, mode)` cadential prior with a confidence.
2. **Feed it as a GLOBAL prior into `keymodeanalyzer`/`keyresolver`**, anchoring per-region resolution the
   way the dropped declared-mode anchor did — i.e. the cadential prior *replaces the proxy the declared
   mode was standing in for*. Apply at **section/piece scope, not window scope** — this is what makes it
   escape the §4 coupling (§3.2–3.3): it is a global tiebreaker on the relative axis, not a local salience
   term.
3. **Confidence-gate it** so it only breaks relative-pair near-ties (where the note evidence is balanced)
   and never overrides a region with strong unambiguous local key evidence — keeping mode-present
   byte-stable on the chord (BIR) gate and on the non-relative key decisions.

Why not (b) fold into Stage 6: the relative axis is a *small, well-understood, literature-backed*
hand-buildable signal addressing 91 % of the floor — exactly the kind of discrete composing-zone step
Stage 4 is for. Co-developing it inside a learned functional layer would defer a high-value, low-risk fix
behind a much larger effort. (c) cadence-insufficient → B is **falsified for the relative axis** by §2–§4:
the signal exists, is decoupled, and is large.

**OQ6 / pass-bar re-scope.** 4b-ii showed reweighting recovers ≈0 of the floor. This run shows a
**hand-built global cadence anchor has a ≈91 %-of-floor ceiling on the relative-pair class.** The OQ6
mode-absent pass-bar should therefore be set against the **cadence→key lever**, not reweighting: a
reasonable target is "recover a substantial majority of the 1259 relative-pair floor regions
(hint-parity ceiling) at mode-present-neutral cost and BIR-gate-byte-identical," with the mode-invariant
"other" residual (≈454) and keyfail (≈164) explicitly out of scope → Stage 6.

---

## 6. Stop-conditions — disposition
- ✅ **Caught myself before building** the cadence→key term/wiring — derived feasibility only; the wiring is
  a sketch (§5), not code.
- ✅ **Signal failing to discriminate / coupling re-entry** — did **not** occur; the signal discriminates
  (§3.1, 91 % relative-pair floor) and escapes the coupling structurally (§3.2–3.3). Reported as a viable
  fix, not forced.
- ✅ **Detector produces only a flag, not a key/degree** — **this condition fired** (§1): reported as a
  sizing finding (new key-agnostic detection required), not built around.
- ✅ **No production change; no diagnostic added to the binary** — none. The only working-tree artifacts are
  this dossier and `tools/cc_floor_classify.py` (a standalone read-only Python classifier that opens
  existing `.ours.json`; it touches no C++ binary, no corpus, no golden — so the **0/353×3 byte-identity
  gate is not applicable** and no such proof is needed). HELD — no commit.

## 7. Working-tree artifacts (HELD)
- `cc_cadence_key_investigation_dossier.md` (this file).
- `tools/cc_floor_classify.py` (read-only S2-composition classifier — keep or drop at Cowork's discretion;
  it documents the relative-pair vs other sizing protocol, the b2_measure.sh precedent).
- No source edit, no snapshot/golden refresh, no `docs/` sync (no scoring term changed). Source tree
  unchanged from HEAD `cfc7eb5e39`.
