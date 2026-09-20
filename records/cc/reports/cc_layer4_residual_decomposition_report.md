# Layer 4 / Increment B — chord-root residual decomposition (read-only) — **gates Increment C**

**Date:** 2026-06-24 · **Scope:** read-only / decode-only measurement (no production change, no wiring,
no Increment-C code) · **Status of artifacts:** held / gitignored
(`/cc_*.md`, `tools/cc_*`) · `upstream` untouched.

## TL;DR — VERDICT: **STOP and surface. Do NOT proceed to Increment C yet.**

The −15.4 dur-weighted chord-root residual (per-slice 58.4 vs per-region 73.8) is **not** a
fine-grain measurement effect, and it is **not** mostly spelling-fixable. Reducing the per-slice
decoder to the *same region grain* as the per-region baseline recovers only **+2.3 pts (Baroque) /
+1.5 pts (Jazz)** of the ≈15.4-pt gap — a **−13.1 / −13.8 pt real deficit remains at equal grain**.
Of the per-slice misses, **only 3.1 % are spelling-fixable** (the Increment-C pin target); **96.9 %
are genuinely-wrong**, dominated by **wrong-root (60 %)** where the decoder's root is not even a GT
chord tone. The fragment diagnostics localize the cause: **42 % of misses are thin slices (≤2 named
chord-tones)** and **36 % saw a strict subset of the GT chord** — i.e. **the per-slice window is not
gathering the prevailing harmony's notes.** The Increment-C notated-spelling pin would touch ~3 % of
the residual and would **not** fix the ~13-pt window/fragment deficit. That deficit must be
investigated and fixed before C.

Both §2 STOP triggers fire **independently**: (i) per-slice-reduced-to-region is still well below
per-region; (ii) the genuinely-wrong bucket is large.

---

## Method (one grading path, reused; nothing new measured)

- Decoder output: the existing `--decode-chords` per-slice JSON in `tools/corpus_decode_chord/{baroque,jazz}`
  (Increment-B scalar path). **Verified this JSON reproduces the published Increment-B numbers exactly**
  (Baroque per-slice 58.4 / baseline 73.8 / Δ −15.5; Jazz 58.3 / 73.7 / −15.3) via the committed
  `tools/cc_layer4_chord_baseline.py` before decomposing — so it *is* the Increment-B output, not assumed.
  (The uncommitted decoder edits in the tree only add the separate `--decode-chords-l3key` fair-key
  diagnostic; the scalar `--decode-chords` path is byte-identical to Increment B — confirmed in the diff,
  "a constant key vector reproduces the single-key path byte-for-byte".)
- Grader: the same substrate the baseline uses — `compare_analyses.load_analysis` /
  `align_dcml_regions`, GT root + chord-tone set from music21's `RomanNumeral` parse of the WiR
  annotation (`tools/cc_layer4_residual_decompose.py`, held/local; reuses
  `cc_layer4_chord_baseline`). Held-out **TEST** split (md5(stem)%100 < 20), 72 stems, both presets.
- The decoder's named chord = `noteClassifications.chordTones` (carries 7ths even where `quality`
  is the base triad — e.g. root G "Gm" with chordTones {G,B♭,D,F} = Gm7); GT chord = music21
  `pitchClasses`.

---

## §1(a) GRANULARITY — the decisive sub-test

Reduce per-slice decoder roots to region grain (the **duration-majority** decoder root over each
per-region-baseline span — the same reduction the L3 wiring used for key), re-graded **identically**
(same spans ⇒ identical DCML alignment as the baseline; the only thing that differs from the baseline
line is the root source). Denominators match the baseline exactly (Baroque 1,929,840 ticks), so this
is apples-to-apples.

| line (dur-weighted chord-root) | Baroque | Jazz |
|---|---|---|
| per-slice (slice grain) | 58.4 % | 58.3 % |
| **per-slice REDUCED-to-region** | **60.7 %** | **59.8 %** |
| per-region baseline | 73.8 % | 73.7 % |
| grain reduction recovers | **+2.3** of +15.5 | **+1.5** of +15.3 |
| **residual at equal grain** | **−13.1 pts** | **−13.8 pts** |

**Reading:** coarsening the decoder to the baseline's own region grain barely moves it. The decoder's
errors are **not** short isolated wrong slices inside otherwise-correct regions (those would wash out
under a duration-majority vote); the decoder is wrong across **substantial spans**, or its slices
within a region are fragmented/split — both meaning the window is not converging on the prevailing
harmony. **Per-slice genuinely sees ~13 pts less than per-region at the same grain.** → §2 STOP
trigger (i).

---

## §1(b) SPELLING-FIXABLE — small (3.1 %), and score-verified genuine

Per-slice misses where the decoder chord and the GT chord are the **same note collection read with a
different root** — exactly what the Increment-C notated-spelling pin fixes. Defined **strictly**:
symmetric dim7 rotation, symmetric augmented rotation, or a true 4-note enharmonic tetrad (ø7↔m6,
same PC-set, both roots legitimately spellable).

| (b) sub-bucket | Baroque (count / % misses / % dur) | Jazz |
|---|---|---|
| dim7 symmetric rotation | 49 / 1.7 % / 1.6 % | 49 / 1.7 % / 1.6 % |
| aug symmetric rotation | 6 / 0.2 % / 0.2 % | 6 / 0.2 % / 0.2 % |
| true 4-note enharmonic tetrad | 32 / 1.1 % / 1.4 % | 32 / 1.1 % / 1.4 % |
| **(b) TOTAL spelling-fixable** | **87 / 3.1 % / 3.2 %** | **87 / 3.1 % / 3.2 %** |

> **Correction recorded during the analysis (why (b) is this small):** a first-cut "set-identical"
> filter wrongly counted **3-note triad inversion / phantom-root** errors as spelling-fixable
> (e.g. `bwv11.6 m9`: notes {C#,E,A}=A major, GT root A, but decoder assigned **D — a root not even in
> the notes**; `bwv11.6 m19 b3`: {D,F#,A}=D major, decoder took F# as root — a plain inversion error).
> Neither is an enharmonic-spelling ambiguity; the spelling of those notes is unambiguous. Tightening
> (b) to genuine same-collection rotations dropped it from a misleading 17 % to the real **3.1 %**.

**Score verification (the notated spelling pins the GT root):**

- **bwv16.6 m9 b4** — WiR `viio6/5/iv` (a minor), spelled root **C#**, chord E–G–B♭–C# (dim7).
  Decoder picked E. The B♭/C# spelling pins C# (leading tone of iv). ✓
- **bwv179.6 m8 b2** — WiR `viio7/V` (a minor), spelled root **D#**. The **score itself** notates
  {A3, C5, **D#3**, F#4} — D# notated as D# (not E♭), so D#–F#–A–C pins **D#** as the root.
  Decoder picked F#. ✓ (confirmed against the actual notated accidentals)
- **bwv177.5 m4 b2.5** — WiR `viio4/3` (e minor), spelled root **D#**, chord A–C–D#–F#. Decoder
  picked A. The D# spelling pins the root. ✓

So the spelling-pin lever is **real but tiny** — it cannot close a 13-pt deficit.

---

## §1(c) GENUINELY-WRONG — 96.9 %, dominated by the window/fragment problem

| (c) sub-bucket | Baroque (count / % misses / % dur) | Jazz |
|---|---|---|
| inversion (same notes, wrong root) | 108 / 3.8 % / 4.3 % | 112 / 4.0 % / 4.4 % |
| share-tone / function (root ∈ GT) | 503 / 17.9 % / 16.4 % | 504 / 17.9 % / 16.4 % |
| **wrong root (root ∉ GT chord-tones)** | **1698 / 60.3 % / 61.5 %** | 1698 / 60.2 % / 61.4 % |
| other | 419 / 14.9 % / 14.7 % | 419 / 14.9 % / 14.7 % |
| **(c) TOTAL genuinely-wrong** | **2728 / 96.9 % / 96.8 %** | 2733 / 96.9 % / 96.8 % |

**Orthogonal fragment diagnostics over ALL misses — the "window not gathering" signal:**

| diagnostic | Baroque (% misses / % dur) | Jazz |
|---|---|---|
| thin slice (≤2 named chord-tones) | **42.1 % / 37.1 %** | 42.2 % / 37.1 % |
| decoder notes ⊊ GT notes (saw a fragment) | **35.9 % / 33.0 %** | 36.0 % / 33.0 % |
| phantom root (root ∉ its own notes) | **40.9 % / 41.6 %** | 40.7 % / 41.4 % |
| foreign notes (decoder note ∉ GT chord) | 47.1 % / 46.9 % | 47.0 % / 46.8 % |

Named chord-tone-count histogram among misses (Baroque): `0:20, 1:207, 2:959, 3:1339, 4:290` —
**1186 / 2815 misses (42 %) have ≤2 named tones.**

**Top genuinely-wrong type — thin-slice fragment misread (the dominant cause).** Representative
`wrong root` cases (decoder root not even a GT chord tone):

- `bwv11.6 m15 b2`: decoder named root **F#** from a **single sounding note {C#}**; GT root C# (the
  prevailing C#–E–G–B chord). The window saw one note and committed a chord.
- `bwv11.6 m2 b3`: decoder root **D** from the **dyad {F#,A}**; GT root F# (F# m, {C#,F#,A}). Phantom
  absent root over a 2-note fragment.
- `bwv11.6 m7 b3.5`: decoder root **D** from the dyad {C#,A}; GT root A ({C#,E,G,A}). Fragment of the
  prevailing harmony read as a different chord.

**Second type — share-tone / function (17.9 %).** Root-offset signature `3:232, 4:139, 7:102` =
minor-third / major-third / fifth offsets: classic **inversion / relative / vii°↔V7** confusions.
Per the Layer-4 design these turn on **function** (deferred to Layer 5), **not** spelling — the
notes' spelling is unambiguous, so the Increment-C pin does not touch them.

Neither the dominant (fragment) type nor the second (function) type is addressed by the spelling pin.

---

## §2 VERDICT (gates Increment C)

Per preset, the chord-root story:

| | per-slice (slice grain) | reduced-to-region | per-region | spelling-fixable | genuinely-wrong |
|---|---|---|---|---|---|
| **Baroque** | 58.4 | **60.7** | 73.8 | **3.1 %** | **96.9 %** (wrong-root 60 %) |
| **Jazz** | 58.3 | **59.8** | 73.7 | **3.1 %** | **96.9 %** (wrong-root 60 %) |

**→ STOP and surface.** Both STOP conditions of the instruction fire independently:

1. **Per-slice-reduced-to-region is still well below per-region** (60.7 vs 73.8 / 59.8 vs 73.7 — a
   ~13-pt real deficit at equal grain). The −15.4 is **not** a granularity artifact; grain accounts
   for only ~1.5–2.3 pts of it.
2. **The genuinely-wrong bucket is large** (96.9 %), dominated by wrong-root (60 %), and the fragment
   diagnostics (42 % thin slices, 36 % strict-subset reads, 41 % phantom roots) point to **the
   per-slice adaptive window not gathering the chord's notes** — precisely the deeper gap §2 names.

The per-slice thesis does **not** hold at Increment B as-is, and the spelling-pin is **not** the
remaining lever: it would fix ≈3 % of the residual while ≈13 pts of window/fragment deficit remain.

**Recommended next step (for Cowork to scope — not built here):** investigate and fix the
**window/membership gathering** before Increment C — the adaptive lazy-extend window (and/or the
two-pass neighbour aggregation) is leaving ~40 % of misses as ≤2-note fragments that commit a wrong
(often phantom-rooted) chord instead of converging on the prevailing harmony. Increment C's
spelling-pin remains a valid but small lever to apply **after** the window deficit is closed.

## §5 stop-condition attestations
- No production output moved (read-only / `--decode-chords` only). ✓
- No Increment-C spelling-pin logic written. ✓
- No push; `upstream` untouched. ✓
- Tooling (`tools/cc_layer4_residual_decompose.py`) and this report are held / gitignored. ✓
