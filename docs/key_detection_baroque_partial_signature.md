# Key/Mode Detection — Baroque Partial-Signature Weakness

> **RESOLVED ON THE ANCHOR CASE 2026-06-03 by commit `81978321e3` (`fix(keyresolver):
> Option B Baroque partial-signature correction`), in HEAD — and the scope of that word
> is stated here rather than left to be assumed (see the second banner below).** Option B
> from §4 below was
> implemented: the resolver now detects the partial-signature convention (♭6
> pervasive ≥3% of sounding weight AND dominating ♮6 by ≥2×) and reinterprets the
> signature one step toward the missing accidental (minor −1 flat / major +1 sharp)
> for the whole of `resolveKeyAndModeRanked`. Corelli `op01n08d` is now detected as
> **C minor at rank 0 for every region** (verified live 2026-06-08,
> `cc_step3_key_investigation_report.md` Part C); G minor no longer appears at any
> rank. The body below documents the **pre-fix** state and is retained for history.
> The residual `op01n08d` test symptoms (§"three remaining symptoms") are
> quality / inversion / segmentation issues, **not** key detection — see the commit
> message of `81978321e3` for the post-fix status of each.

> **★ WHAT *RESOLVED* ABOVE COVERS, AND WHAT IT DOES NOT (added 2026-08-09 on the user's
> Ruling 35(a) of `cowork_rulings_2026_08_09_fifth_stop.md`; the correction is scoped and
> nothing above it is withdrawn).** What the banner above verifies is the **anchor case**,
> `op01n08d`, and it verifies it correctly. It is **not** a statement about the population
> of pieces that share the notation practice this document describes. Measured over the
> population **derived by this document's own §3 method** — the notated key signature
> against the published annotated key, read from the corpus metadata and applied
> mechanically to every piece named here rather than to §3's table alone — the correction
> reads **fewer than half** of that population with the annotated tonic, the large majority
> of the disagreements landing on a home of the **notated** signature, which is §3's own
> diagnostic for the signature lock this correction exists to escape. Every value is at
> `tools/audit/oi357_partial_signature_establishment.json` and none is restated here
> (**D-431**). **A disagreement total is not a defect total** — each one is a genuine defect,
> a defensible modal reading the major/minor ground truth cannot represent, or an artifact of
> comparing a global reading against a global annotation on a piece that modulates, and that
> reading has not been made per case. **The tracking row is `OPEN_ITEMS.md` OI-363**, which
> also carries what bounds it: the subject here is the **legacy** key resolver, which the
> production arm does not run (the production question is `OPEN_ITEMS.md` OI-357), and this
> repertoire is not the gate corpus, so no published measurement moves.

*Investigation, 2026-05-23 (read-only; no code changed). Anchor case: Corelli
`op01n08d` (the `CorelliOp01n08dUserReportedChordTrackAudit` notation failure).*

## TL;DR

The key/mode resolver is **structurally locked to the notated key signature**. For
any in-range signature it picks the best `(tonic, mode)` pair *whose natural
signature equals the notated one*, and it never overrides the signature itself.
This is correct for modern notation but **systematically wrong for Baroque
"partial" signatures** (a.k.a. Dorian/Mixolydian signatures), which notate a key
with **one fewer accidental** than the modern convention. For such pieces the true
key sits **one circle-of-fifths step sharper** than *any* candidate the analyzer
can produce, so it is unreachable.

`op01n08d` is C minor notated with **2 flats** (modern C minor = 3 flats, with A♭
supplied as an accidental). The analyzer detects **G minor** — the Aeolian home of
the 2-flat signature. The same mechanism mis-keys most short-signature Corelli
pieces (verified below).

## 1. How key/mode detection works

Entry point: `keyresolver::resolveKeyAndModeRanked` ([keyresolver.cpp](../src/composing/analysis/key/keyresolver.cpp)),
which wraps `KeyModeAnalyzer::analyzeKeyMode` ([keymodeanalyzer.cpp:519](../src/composing/analysis/key/keymodeanalyzer.cpp#L519)).

**Inputs/evidence:**
- The score's **key-signature event** at the tick → `keyFifths` and (if present) a
  **declared mode** from `KeySig.mode()` (MAJOR→Ionian, MINOR→Aeolian, or a
  specific church mode). `op01n08d` declares `<mode>minor</mode>` → Aeolian.
- A **windowed pitch context** (fixed lookback + dynamic lookahead) of
  `(pitch, durationWeight, beatWeight, isBass)` tuples.
- Per-candidate score = scale-membership + triad evidence (tonic/third/fifth/
  leading-tone, complete-triad bonus, missing-tonic penalty) + **key-signature
  proximity penalty** + characteristic-pitch + true-leading-tone + **mode prior**,
  then a **declared-mode penalty** (−7.0) for modes outside the declared class.
- Confidence = sigmoid of the top-1/top-2 score gap.

**Two facts that drive the bug:**

1. **Mode priors** ([keymodeanalyzer.h:211](../src/composing/analysis/key/keymodeanalyzer.h#L211)):
   Ionian **+1.20**, Aeolian **+1.00** dominate; Dorian/Mixolydian/MelodicMinor
   −0.50, HarmonicMinor −0.30, everything else more negative. So among the modes of
   a signature, the **major (Ionian) and natural-minor (Aeolian) homes are the
   default winners** unless pitch evidence overrides.

2. **Signature lock.** For an in-range signature the winner is chosen from the
   *family that shares that signature*: the selection loop
   ([keymodeanalyzer.cpp:633-663](../src/composing/analysis/key/keymodeanalyzer.cpp#L633))
   only iterates `tonicPc = (keySigIonianTonicPc + keyModeTonicOffset(mode)) % 12`,
   and `resolveToFifths` ([:189](../src/composing/analysis/key/keymodeanalyzer.cpp#L189))
   reports each candidate's *natural* signature. A candidate whose natural signature
   differs from the notated one **cannot win** (the global-best fallback only runs
   for out-of-range signatures). The `keySignatureDistancePenalty` (0.60/step,
   [:411](../src/composing/analysis/key/keymodeanalyzer.cpp#L411)) further penalizes
   anything off the notated signature even where it could compete.

The resolver then applies a **piece-start shortcut**
([keyresolver.cpp:122](../src/composing/analysis/key/keyresolver.cpp#L122)): with no
previous region + a declared mode, it returns the declared anchor directly —
tonic = `ionianTonicPcFromFifths(keyFifths) + keyModeTonicOffset(declaredMode)`. For
`(-2, Aeolian)` that is **G** (Bb + 9 semitones). So region 1 is hard-anchored to
**G minor**, and hysteresis + the declared-minor prior pull subsequent regions back
toward G minor.

## 2. Why `op01n08d`'s 2-flat signature → G minor

- Notated signature = −2, declared mode = minor (Aeolian).
- Piece-start anchor → **G Aeolian (G minor)**, confidence 0.5.
- In later windows, the declared-minor penalty removes all major modes; among the
  **minor modes that share −2**, the tonic options are: **G Aeolian** (prior +1.00),
  C Dorian (−0.50), **C melodic minor** (−0.50), G harmonic minor (−0.30), D
  Phrygian (−1.50)… G Aeolian's prior advantage (~+1.3 to +1.5 over any C option)
  makes G minor the default; only strongly C-cadential windows (mm. 26–39, repeated
  V–i in C) overcome it and flip to **`Cmel`** (C *melodic* minor — see next point).
- **C natural/harmonic minor is unreachable.** Real C minor (with A♭) has natural
  signature −3, one step off the notated −2, so it is never a candidate. The only
  C-tonic options within −2 are C Dorian and C melodic minor — **both have A♮, not
  A♭.** That is why, even when the analyzer *does* find tonic C, it reports
  `Cmel`, whose iv-degree triad on F is **F major** (F–A–C), not F minor.

Per-region detection on `op01n08d` (from `batch_analyze --dump-regions notation`):
ambiguous/transition regions read `Gmin`/`Gharm`; only the clear C-cadential tail
(m26+) reads `Cmel`. DCML ground truth: **global key C minor throughout**, with a
tonicization of v (g minor, mm. 9–13) and III (E♭, mm. 14–23).

## 3. Scope — systematic, not a special case

Corelli notates in the late-17th-century convention of **one accidental short**.
From `tools/dcml/corelli/metadata.tsv` (notated `KeySig` vs DCML `annotated_key`):

| Piece | Notated | True key | Modern sig | Detected (notation path) |
|---|---|---|---|---|
| op01n01 | −1 | F major | −1 | (matches) |
| op01n03 | +2 | A major | +3 | **D major** |
| op01n05 | −1 | B♭ major | −2 | — |
| op01n08 | −2 | C minor | −3 | **G minor** |
| op01n09 |  0 | G major | +1 | **G Mixolydian / C major (scattered)** |
| op01n10 | −1 | G minor | −2 | **D minor** |

Unifying rule: **the true key is one step sharper (one more sharp / one fewer
flat) than notated**, so the analyzer lands on the notated signature's Ionian
(major case) or Aeolian (minor case) home — always a fifth/fourth off the true
tonic. Verified empirically: op01n03a→`Dmaj`, op01n09a→`GMixolyd`, op01n10a→`Dmin`,
op01n08d→`Gmin`. This affects **most of the Corelli corpus** and, in principle, any
Baroque score using partial signatures.

**Why the Baroque BIR baseline (27/23) doesn't expose it:** BIR measures
root-pc / bass-is-root agreement, which is largely **key-independent** — a chord's
root/bass can be right while the key label is wrong. The wrong key corrupts
**quality** (F vs Fm), **Roman numerals**, and some **inversions** — exactly what
the Corelli *notation* tests assert (chord symbols + romans), which is why they
catch it while BIR does not. So the corpus metric understates the real-world
quality impact for Baroque material.

## 4. Better approaches and tradeoffs

The fix must let the resolver conclude the true key is one step sharper than
notated. Options, roughly increasing in scope/risk:

- **A. Signature-flexible candidates.** Allow the winner to come from the notated
  family *or* the family one step sharper (one more sharp / one fewer flat), letting
  pitch + cadence evidence decide. Directly removes the lock. *Risk:* adds a
  competitor family to **every** piece, including correctly-notated modern scores
  (Bach chorales, Mozart, Chopin) — could destabilize them. Best gated (e.g. only
  the +1-sharp neighbor, only when the "missing" accidental is pervasively present).
- **B. Partial-signature detector.** Detect that the characteristic accidental of
  the sharper key is pervasive (e.g. A♭ saturating a notated "G minor", or F♯
  saturating a notated "C major") and reinterpret the signature. *Risk:* heuristic
  thresholds; the leading tone is always an accidental in minor, so the
  discriminator must key on the **b6 / specific degrees**, not just any accidental.
- **C. Cadence/bass tonic-finding decoupled from signature.** Define the tonic by
  cadential function (V–I root motion, phrase-final chords, first/last bass) and fit
  the mode afterward. Most robust musicologically; the codebase already has cadence
  detection. *Risk:* largest change — a different key-finding architecture, broad
  behavioral shift.
- **D. Annotation / per-score override.** Read the DCML/annotated key where present
  (or a user override). Fixes the test corpus but does not generalize to user scores.

**Cross-cutting tradeoff:** key detection is foundational — it feeds chord quality,
Roman numerals, inversions, and (indirectly) segmentation and BIR. The current
approach is deliberately conservative (trust the notation), which is *safe for the
modern-notated majority* and *wrong for Baroque partial signatures*. Any change here
**must** be validated against both BIR presets (Baroque ≤25 false / Jazz ≤13 false),
all notation tests, and the pipeline snapshots, because it can move output on every
score. **No variant is "low-risk."**

## Relationship to the three remaining `op01n08d` test symptoms

The task hypothesis was "fixing the key fixes all three at once." That is **partly
optimistic**:

- **m24 F→Fm** — *the genuine key symptom, but needs two things.* The analyzer must
  (i) escape the signature lock to reach **C natural/harmonic minor** (with A♭ so
  F = iv), and (ii) assign minor quality to the **thirdless** F. C melodic minor
  (the best reachable C option within −2) still yields F **major**. So even perfect
  in-family tonic-finding does not fix m24 — it requires the signature escape *plus*
  thirdless-quality logic (the previously-rejected δ "diatonic quality prior", which
  was rejected precisely because it ran on the wrong key).
- **m2 b3 G/B→G** — **not a key symptom.** That region is *already* detected as C
  (`Cmel`); the chord is G + B (no D) with bass B → first inversion `G/B`. This is
  an **inversion / root-position-preference** issue, independent of the key.
- **m18 b1 missing C minor** — primarily **segmentation.** The m17 region (`Gm` =
  iii/III, correct even under the true key) absorbs m18 b1's C minor (a short region
  swallowed). Key context may nudge it but the proximate cause is region absorption.

So the key fix is necessary for broad Baroque correctness and for m24, but it will
**not** by itself clear m2 b3 (inversion) or m18 (segmentation).

## Recommendation

This is a foundational, corpus-wide change with no low-risk variant. Recommend the
next session **prototype Option A or B behind full validation** (both BIR presets +
notation + snapshots) rather than a blind edit, and treat m2 b3 / m18 as separate
inversion / segmentation work. Do **not** revive the δ quality prior until the key
is corrected first.
