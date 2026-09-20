# CC — Decomposition of the per-event charged set: KEY-driven vs CHORD/SEGMENTATION-driven

> **READ-ONLY. HEAD `dd418ecfed`. No build, no committed tool, no production/gate/scoring/threshold change.**
> Every number is computed from on-disk corpora only, reusing `compare_analyses`
> (`three_way_classify`, `_dcml_time_spans`), `dcml_parser` (`local_key`, `_key_to_tonic_pc`), and
> `characterise_bir_false.validate_corpus_dir` verbatim — same machinery as Round 3. The repro script is
> **throwaway / uncommitted**: `tools/cc_decomp_measure.py` (raw blob `tools/cc_decomp_out.json`). It is a
> diagnostic helper, **not** the standing `--oracle-root` tool (still unbuilt, pending ratification).

---

## Headline (the one cut that matters)

The Round-3 finding — *true per-event root-error rate ≈21% (≈10× the batch ~2%)* — decomposes cleanly. Under the
**authoritative DCML-local-key oracle** (project ground-truth rule: DCML authoritative, music21 only
corroborates — `feedback_ground_truth`), the plurality is **KEY-DRIVEN**:

| preset | charged (recs) | **KEY-DRIVEN** | **OVER-GRAB** (seg) | **CHORD-ID** | **AMBIGUOUS** |
|---|---:|---:|---:|---:|---:|
| **Baroque HEAD** | 3882 | **2131 — 54.9 %** | 1228 — 31.6 % | 86 — 2.2 % | 437 — 11.3 % |
| **Jazz** | 4083 | **2159 — 52.9 %** | 1548 — 37.9 % | 83 — 2.0 % | 293 — 7.2 % |
| **Default** | 3914 | **1818 — 46.4 %** | 1767 — 45.1 % | 129 — 3.3 % | 200 — 5.1 % |

**Verdict: the KEY axis owns the plurality of the ~21 % per-event error (Baroque/Jazz ~53–55 %; Default a
near dead-heat, 46.4 % vs 45.1 %).** This **confirms the re-assessment's K1-first hypothesis** and identifies the
10× multiplier as **key-span propagation** — a wrong key over a long span charges *every* event in it — **not**
(as Round 3 hypothesized) region over-grab. **But segmentation over-grab is a strong, co-dominant #2 (32–45 %,
plurality-tying in Default)** — large enough to warrant a *parallel* lever, not deferral behind K1. **CHORD-ID is
negligible (2–3 %)** — independent confirmation that the chord/vertical axis is near-ceiling.

**Critical caveat (the sensitivity below):** ~55–79 % of the KEY band is the **tonicization / local-vs-global
grain** — events where music21 (the corroborator) sides with the *global* key while DCML asserts a *local* key,
even though both oracles agree on the **root**. Treating those strictly as AMBIGUOUS (oracle-key disputed, §2)
shrinks the **hard, m21-corroborated key-detection** error to **24.5 % / 18.4 % / 9.8 %** and lets OVER-GRAB take
the plurality. So K1's real target splits into (a) hard key-detection and (b) local-key *commitment labeling* —
the K3 "when to assert a tonicization" problem. This reproduces `precision_headroom`'s 63 %-tonicization /
37 %-key-detection split, now per-event.

---

## §1 — Method (read-only, pc-typed, reuses Round-3 machinery)

For **each charged event** (`music21_dcml_agree`: `m21_pc == dcml_pc ≠ our_pc` at the event onset tick,
per Round 3 §1), classified into exactly one bucket, in priority order:

1. **KEY-DRIVEN** — our **key** ≠ the oracle key at the event. Our key = the `.ours.json` region's `key` string
   covering the tick, parsed to **(tonic-pc, mode-class∈{major,minor})**. Oracle key = the DCML annotation's
   `local_key` (`dcml_parser`), parsed to (tonic-pc, mode). Key mismatch = tonic-pc differs **or** mode-class
   differs (mode compared only when both sides resolve to maj/minor; our exotic modes — Dorian/Mixolydian/etc. —
   are mapped to their third's maj/minor class).
2. **CHORD/SEGMENTATION-DRIVEN** — our key **matches** the oracle key, root still wrong. Sub-split:
   - **OVER-GRAB** — our single region covering the event spans **≥2 distinct oracle roots** (Round-3 over-grab
     test: count distinct `dcml.root_pc` over DCML events whose onset ∈ `[our_region.start, our_region.end)`).
   - **CHORD-ID** — our region aligns ~1:1 with the oracle event (exactly 1 oracle root in its span); a genuine
     vertical/competition miss.
3. **AMBIGUOUS** — the oracle key cannot be cleanly established: **music21 (corroborator) disagrees with DCML on
   the key** at this event (`m21_tonic ≠ dcml_tonic`), or a key string is unparseable (0 such events — all keys
   parsed). In the PRIMARY table this fires only when our key *matches* DCML but m21 disputes it; the SENSITIVITY
   below extends it to *all* m21-disputed-key events.

**Robustness checks performed.** All charged events have parseable our-key and m21-key (0 unparseable per preset).
Per-record charged totals (3882/4083/3914) reconcile to Round 3's set-deduped charged (3862/4065/3894) exactly:
the **+20/+18/+20** are co-tick oracle annotations (two DCML events whose reconstructed onsets coincide — e.g.
mid-beat key changes); each is classified independently, which is correct at event granularity. music21's key
format (`g minor`, `B- major`, `f# minor`) needed a dedicated parser (case = mode, `-` = flat); a first pass that
mis-read flat/minor m21 keys was found and fixed (it had mis-stated Jazz AMBIGUOUS by ±38).

---

## §2 — Per-preset results

### PRIMARY — DCML-local key as the authoritative oracle

(table repeated from Headline, with the mode-only vs tonic split of the KEY band)

| preset | KEY-DRIVEN | …tonic-differ | …mode-only | OVER-GRAB | CHORD-ID | AMBIGUOUS |
|---|---:|---:|---:|---:|---:|---:|
| Baroque HEAD | 2131 (54.9 %) | 2117 | 14 | 1228 (31.6 %) | 86 (2.2 %) | 437 (11.3 %) |
| Jazz | 2159 (52.9 %) | 2133 | 26 | 1548 (37.9 %) | 83 (2.0 %) | 293 (7.2 %) |
| Default | 1818 (46.4 %) | 1806 | 12 | 1767 (45.1 %) | 129 (3.3 %) | 200 (5.1 %) |

**KEY errors are overwhelmingly *tonic* transpositions, not parallel maj/minor** (mode-only is 0.3–0.6 %). The
dominant `(dcml_tonic − our_tonic)` intervals are **+9 (= −3 semitones, the relative-key third)** and the
dominant/subdominant fifths — i.e. our key is typically the **relative major/minor or a neighbouring diatonic
key** of the oracle's local key, exactly the global-vs-local-tonicization confusion.

### SENSITIVITY — strict AMBIGUOUS (every m21-disputed-key event → AMBIGUOUS)

When the oracle key is required to be **m21-corroborated** (else AMBIGUOUS, per §1.3 applied to the KEY band too):

| preset | KEY-DRIVEN (hard, m21-corroborated) | OVER-GRAB | CHORD-ID | AMBIGUOUS |
|---|---:|---:|---:|---:|
| Baroque HEAD | 951 (24.5 %) | 1228 (31.6 %) | 86 (2.2 %) | 1617 (41.7 %) |
| Jazz | 752 (18.4 %) | 1548 (37.9 %) | 83 (2.0 %) | 1700 (41.6 %) |
| Default | 384 (9.8 %) | 1767 (45.1 %) | 129 (3.3 %) | 1634 (41.7 %) |

Under the strict reading OVER-GRAB takes the plurality (or ties AMBIGUOUS), and the **hard** key-detection band
is 10–25 %. The truth sits between the two tables: **the KEY band is real (it is the largest single cause under
the authoritative oracle), but roughly half-to-most of it is the local-key *labeling* grain, not raw mis-keying.**

---

## §3 — Worked examples (Baroque HEAD; stem@tick, our key+root vs oracle key+root)

**KEY-DRIVEN, m21 corroborates DCML (hard key error — both oracles agree on local key, we are elsewhere):**
- `bwv10.7@36000` m19.4 — OUR **Bbmaj**→Bb · DCML **g** `V4/3`→G · m21 **g minor**→G. We hold the relative
  major (Bb) across a g-minor span; every event in the span is charged. *(span propagation, textbook.)*
- `bwv101.7@10080` m6.1 — OUR **Fmaj**→F · DCML **d** `VI`→Bb · m21 **d minor**→Bb.
- `bwv102.7@6720` m4.2 — OUR **Gmin**→Ab · DCML **c** `iv6`→F · m21 **c minor**→F.

**KEY-DRIVEN, m21 disputes DCML (tonicization / local-vs-global band → AMBIGUOUS under sensitivity):**
- `bwv101.7@12480` m7.2 — OUR **Fmaj**→C · DCML **a** `IV`→D · m21 **d minor**→D. DCML tonicizes A-minor; m21
  stays in d-minor; we read F-major. Same root D agreed by both oracles, three different keys.
- `bwv102.7@17760` m10.1 — OUR **Gmin**→Eb · DCML **Eb** `IVmaj7`→Ab · m21 **c minor**→Ab. *(This is the
  Round-3 showcase "straddle." At the charged event our **key** is wrong — see §4.)*

**OVER-GRAB (key matches oracle, our region covers ≥2 oracle roots):**
- `bwv101.7@1440` m1.3 — OUR **Dmin**→Bb · DCML **d** `iv6`→G. Our single d-minor region covers `iv6`(G),
  `i6`(D), `iv7`(G) — three oracle roots; charged on the beats it over-covers.

**CHORD-ID (key matches, region 1:1, genuine vertical miss — mostly symmetric-dim7 / bass-as-root):**
- `bwv153.1@3840` m2.4 — OUR **Amel**→B (`Bdim7`) · DCML **a** `viio6/5`→Ab. Symmetric dim7, root pc-undefined
  by construction (the CLAUDE.md two-tier seed).
- `bwv117.4@17280` m9.4 — OUR **Gmaj**→C · DCML **G** `ii6`→A. We picked the bass (C) of an A-rooted `ii6`.

**AMBIGUOUS (our key matches DCML, but m21 disputes the oracle key):**
- `bwv11.6@20160` m15.1 — OUR **Bmin**→B · DCML **b** `ii%6/5`→C# · m21 **D major**→C#. Roots agree (C#), DCML
  and m21 split b-minor vs its relative D-major — oracle key not cleanly established.

---

## §4 — Reconciliation with Round 3 (the showcase straddles are KEY-driven, not over-grab)

Round 3 attributed the 10× to "region over-grab" and named four straddles (bwv102.7, bwv358, bwv227.7, bwv432).
At the **charged DCML event**, three of them classify as **KEY-DRIVEN** here, because **our key is wrong at that
event**, upstream of the segmentation:

| case | charged event | OUR key→root | DCML key→root | bucket here |
|---|---|---|---|---|
| bwv102.7 | @17760 `IVmaj7` | **Gmin**→Eb | Eb→Ab | KEY-DRIVEN (m21-disputed) |
| bwv358 | @5760 `I6` | **Fmaj**→A | d→D | KEY-DRIVEN (tonic) |
| bwv227.7 | @18000 `iv6/5` | **Gmaj**→G | b→E | KEY-DRIVEN (tonic) |

Round 3 observed the **segmentation symptom** (one region straddling two DCML chords); the decomposition shows
the **key cause sits above it** — fix the key and the region's frame, then the straddle's root, follows. This is
not a contradiction of Round 3 (its per-event grid and floor/charge separation stand); it refines *which layer
owns* the cases Round 3 used to motivate the over-grab hypothesis. The over-grab bucket is still real and large
(§2) — it is just populated by *different* events (regions that over-cover **within a correct key**, like
`bwv101.7@1440`), not by the named showcase straddles.

---

## §5 — Verdict (which layer owns the plurality of the ~21 %)

1. **KEY owns the plurality under the authoritative DCML-local oracle** (54.9 % / 52.9 % / 46.4 %). The 10×
   per-event multiplier is **dominated by key-span propagation**. **K1 is confirmed as the #1 lever**, and its
   true impact is ~10× the batch number it was scoped against — the re-assessment's plan **stands, sharpened**.
2. **Segmentation (OVER-GRAB) is co-dominant #2 (31.6 % / 37.9 % / 45.1 %), tying KEY in Default.** This is a
   **partial re-prioritization flag**: segmentation is a larger lever than "defer behind K1" implies; it deserves
   a **parallel** track, especially for the Default config the user runs (near dead-heat).
3. **CHORD-ID is negligible (2.2 % / 2.0 % / 3.3 %).** The chord/vertical axis **is** near-ceiling, as concluded
   — and the residue is dominated by structurally-unresolvable symmetric-dim7 (the known two-tier seed), not
   addressable vertical competition. No re-prioritization toward the chord axis.
4. **The KEY band is half-to-most *tonicization labeling*, not hard mis-keying** (sensitivity: hard,
   m21-corroborated key errors = 24.5 % / 18.4 % / 9.8 %; the rest is local-vs-global grain). **K1 therefore
   splits**: (a) a hard key-detection sub-lever (~10–25 %) and (b) a local-key *commitment* sub-lever (~30 %,
   the "when to assert a tonicization" problem — closer to K3). The user/Cowork should decide whether the first
   K1 step targets hard mis-keying (where the oracles concur we are wrong) or the labeling grain (larger but
   softer, and entangled with the tonicization-vs-modulation backlog).

**Plurality owner: the KEY layer** — with the explicit qualification that segmentation is a co-dominant second
and that roughly half of the key mass is the tonicization-labeling sub-problem rather than raw key detection.

---

## §6 — Stop-condition compliance

- **READ-ONLY** — HEAD `dd418ecfed`; no build, no committed tool, no production/gate/scoring/threshold change. ✅
- **No build needed** — every signal (our key, oracle local key, over-grab span) read from existing
  `.ours.json` regions + `dcml_parser`; no data required that isn't already on disk. **No STOP.** ✅
- **AMBIGUOUS reported honestly, not forced** — 5–11 % primary; the m21-disputed key band is surfaced as an
  explicit sensitivity (up to ~42 %) rather than silently absorbed into KEY or CHORD. **No forced verdict.** ✅
- **Nothing committed / no threshold touched** — `tools/cc_decomp_measure.py` + `cc_decomp_out.json` are
  throwaway, uncommitted (mirroring Round 3's `cc_round3_measure.py`). ✅

**For Cowork/user to ratify before the standing `--oracle-root` tool and before K1 work begins:**
1. The **plurality verdict**: KEY-driven owns the per-event error under the authoritative DCML-local oracle, with
   segmentation a co-dominant second and chord-ID near-zero.
2. The **K1 split decision**: target hard key-detection (m21-corroborated, ~10–25 %) first, or the larger
   local-key-labeling grain (~30 %, entangled with the tonicization/modulation backlog) — these are different
   work items.
3. Whether **segmentation (OVER-GRAB)** gets a parallel lever given its 32–45 % share (Default near-tie).
