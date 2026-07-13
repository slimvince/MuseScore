# Engage arc #12 — Stage-3 owed MEASUREMENTS: does the joint key↔chord step actually pay?

> **Status: MEASUREMENT (CC, 2026-07-07). READ-ONLY — no production behavior change, no build of the joint
> step, no fit, no constant tuned.** Executes `cc_instruction_engage_stage3_joint_measure.md` (engage arc #12).
> Principle-driven throughout (`CLAUDE.md ## Guiding principles`, 1–16). This settles the facts the joint-step
> design (`cowork_joint_key_chord_design.md`) deliberately left unmeasured — above all the decisive one: **does
> re-deciding the chord under alternative carried keys measurably improve root-correctness, or not?**
>
> **Grounding tags.** `[code]` = read at the named source symbol on live disk at HEAD `fa0a881aa4`; `[data]` =
> measured on the pinned corpus `c50002fee1` by the instrument `689840d2ef`; `[design]` = the joint-step /
> pedal design docs. No claim rests on an unverified assumption (#1/#5).
>
> **Provenance / reproducibility (#16).** Corpus `c50002fee1` (the pinned frozen gate corpus, 352 source
> XMLs, 326/326 WiR-covered per preset). Instrument commit **`689840d2ef`** (`feat(composing): --dump-joint-probe`).
> HEAD **`fa0a881aa4`**, branch `master`, fork-only. Measurement report artifact:
> `tools/reports/joint_probe_measure.json` — **re-measured at OI-160 (2026-07-13) under the OI-142-corrected
> ground truth, and now the ONE canonical artifact of this instrument** (it carries both axes: the chord-axis
> blocks this report reads and the key-axis block the OI-43/OI-44 shelve record reads; the separately-named
> duplicate `mode_key_chord_probe.json` is retired, #6). The corrected §2.1 figures are marked in place, the
> superseded ones kept beside them (#12). Both regression stops untouched/green (production byte-identical —
> §5). The benefit is measured the SAME way the robust stop is (#1): root-agreement vs the DCML (When-in-Rome)
> ground truth, aligned to our region ticks by the SHARED `compare_analyses._dcml_time_spans` /
> `compare_rn._active_index_at` / `dcml_parser` substrate the a8 driver reuses — no proxy, no new tick matcher.

---

## §0 — Headline (the go/no-go)

**The joint step's chord re-decode barely pays, and on the population it is scoped to it does not pay at all.**
Measured over the pinned corpus ×3 presets:

- **★ The benefit (the go/no-go).** On the regions where the chord root FLIPS under a carried alternative key,
  the flipped reading agrees with the DCML root only marginally more often than the current key-then-chord
  reading: net **corr − harm = +9 / +3 / +10** (Baroque/Jazz/Default) out of **~6200 DCML-scored regions per
  preset** — i.e. **+0.05 to +0.16 percentage points** of root accuracy. Harm is **~75–90 % of correction**
  everywhere (28 harms vs 37 corr Baroque; 33 vs 36 Jazz; 25 vs 35 Default). Even the **oracle upper bound** (a
  perfect key-selector that captures every available correction and avoids every harm) is only **+35–37 regions
  = +0.6 pp**. `[data]`
- **★ On the coupled minority the step is actually scoped to** (key-uncertain: D-L3a sequence margin below its
  bar 1.0), the net is **0 / +5 / −2** on **n = 16 / 15 / 11** flipped regions — **zero-to-noise, one preset
  negative.** `[data]`
- **The fire-rate is tiny.** The chord winner flips under some carried key in only **1.4–1.5 %** of committed
  regions (99 / 95 / 89 regions), and **0.9–1.4 %** of the key-uncertain coupled regions — **~10× smaller than
  the ~13.5 % "coupled" structural proxy** `decideJointKey` carries (`jointkeydecision.h:59-61` `[code]`). The
  chord axis is **almost always key-stable.** `[data]`

**Verdict handed up (the build decision is Cowork's/the user's, #8):** the measured evidence does **not** support
building the joint key↔chord step as a precision lever. The design's §0 framing of it as "the biggest precision
lever (#4)" is **not borne out on this corpus** — the chord axis moves rarely, and when it moves, corrections and
harms nearly cancel. This is consistent with (and sharper than) the design's own owed-2 expectation
("qualitative win on hard cases, low single-digit points overall" `[design]` §5) — the measured reality is
**sub-single-digit points overall and ~zero on the hard cases.** Per #3/#5 this is surfaced as a
STOP-and-report, not built around.

---

## §1 — The probe (Task 1): the pure decoder re-decoded under carried keys

The instrument is a default-OFF `batch_analyze` diagnostic `--dump-joint-probe` (`689840d2ef`), the read-only
pattern of `--dump-fanout` / `--dump-fullspine`. It is **not** the production joint step — no beam driver, no
wiring, no behavior change; it exercises the existing decoder as the pure re-decode the design names.

**The pure-fn signature it exercises `[code]`.** `ChordSliceDecoder::decode(slices, noteModel,
keySignatureFifths, keyMode, chordPrefs, decoderPrefs, excludeStaves)`
(`chordslicedecoder.h:524-531`) — "this increment takes one key" (`:133`), the key a diatonic PRIOR (`:130`). So
re-decoding under a different key is well-defined and reproducible (the "faithful mechanism" J-key-iii deferred;
design §2.2). The per-slice ranking is **context-free** (`chordslicedecoder.h:533-542` `redecodeRange` note), so
one full decode under key `k` gives each slice's winner-under-`k`.

**The carried keys it re-decodes under (faithful to L3's carry).** Per production `HarmonicRegion` the probe reads
the L3 **argmax key** (`keyModeResult`) and the **carried candidate-key menu** (`keyAlternatives`, the region-level
ranked keys built by `resolveKeyAndModeRanked`, `regionanalyzer.cpp:1049-1051` `[code]`) + the **D-L3a
sequence-margin confidence** (`keyConfidence`, `harmonicrhythm.h:119` `[code]`). It decodes ALL slices once per
distinct carried key (argmax ∪ alternatives, the whole score's union), then records, per region, the
**duration-majority committed decoder root** under each key. Production regions are obtained with **opts identical
to `analyzeScore`** (Smoothed granularity, 0.25 onset threshold, sparse Pass-1 admission) so the carry matches how
the frozen corpus is produced. Emits the standard `.ours.json` region schema (for DCML alignment) + an additive
`probe` object. Returns before the standard `writeJson` ⇒ production byte-identical (§5).

**The A/B held fixed the way the design intends.** The baseline is the decoder-under-**argmax**-key root; the
flip is the decoder-under-**alternative**-key root — **the same decoder, varying only the key.** That is exactly
"re-deciding the chord under alternative keys" (the joint step's chord axis), isolated from any decoder change.
The production `analyzeChord` root is emitted only as a cross-reference (`prodRoot`), never as the A/B baseline.

**Route caveat (honest, #12).** The decoder is run globally under each key and a region's root is the
duration-majority of its committed (Commit/Inherit) slices; a G1 Inherit's prevailing chain can span the score
under that key. This is faithful to "what the decoder outputs for the whole score under key `k`"; the majority
over Commit-dominant regions minimizes inherit-chain sensitivity. A production joint step would decode per-region
under the settled key — the same decoder, so the flip counts are representative, not the exact per-region beam
output.

---

## §2 — The decisive facts (Task 2), measured vs the DCML ground truth (#16)

All figures: pinned corpus `c50002fee1`, ×3 presets, DCML-root agreement via the shared a8 substrate.
`n` denotes region counts. Full table: `tools/reports/joint_probe_measure.json`.

### §2.1 ★ The benefit — corr / harm / neutral on the root flips (the go/no-go)

A **flip** = a carried alternative key under which the decoder commits a **different** region root than the
argmax key (both roots defined). Per flip, vs the DCML root: **corr** = the flip agrees where argmax did not;
**harm** = argmax agreed and the flip does not; **neutral** = neither agrees (a root move that changes nothing).
This is the same net-(corr−harm) framing that exposed the F-B override (`cc_engage_c3_measurement_report.md`).

> **★ RE-MEASURED AT OI-160 (2026-07-13) — the figures below are the corrected ones; the ruling is
> unchanged.** The original run pre-dated the **OI-142** ground-truth correction (the 12 transposed
> editions' offsets, applied at `dcml_parser.load_wir_regions`), so the DCML-graded corr/harm split
> below was sorted against a partly-wrong ground truth. The artifact was refreshed from a run at HEAD
> and the superseded figures are kept beside the corrected ones (#12). **What moved and what did not
> is the whole story:** the **fire-rate is byte-identical** (99 / 95 / 89 flip regions — which chords
> flip is a property of *our analyzer*, and our analyzer did not change), and so are beam width, the
> pedal counts, and the region counts; **only the ground-truth-graded corr/harm sort moved.** The
> **coupled minority (§2.2) — the population this decision actually turns on — is byte-identical.**
> See `cc_oi160_report.md`; superseded artifact at `tools/reports/snapshot_2026-07-13_pre_oi160/`.

| preset | **top-alt flip** (per region, the highest-conf carried alt that flips) | **per-flip pairs** (all region×alt flips) | **any-alt oracle bound** (DCML-scored regions) |
|---|---|---|---|
| Baroque | corr **38** / harm **29** / neut 30 → **net +9** (n=97) | 59 / 53 / 61 → net +6 (n=173) | corr-available **38**, harm-exposed **29**, over **6249** |
| Jazz | corr **39** / harm **33** / neut 22 → **net +6** (n=94) | 75 / 55 / 43 → net +20 (n=173) | corr-available **39**, harm-exposed **33**, over **6149** |
| Default | corr **36** / harm **26** / neut 27 → **net +10** (n=89) | 67 / 50 / 52 → net +17 (n=169) | corr-available **36**, harm-exposed **26**, over **6253** |

*Superseded (the pre-OI-142 grading, kept for the record — #12): top-alt corr/harm/neut **37/28/32 → net +9**
(Baroque), **36/33/25 → net +3** (Jazz), **35/25/29 → net +10** (Default); per-flip pairs 56/52/65 → +4,
70/55/48 → +15, 64/49/56 → +15; oracle bound 37/28, 36/33, 35/25. The net (corr−harm) moved
**+9 / +3 / +10 → +9 / +6 / +10** — Jazz by three regions, Baroque and Default not at all.*

Reading it:
- **Every framing tells the same story: the flip is nearly a coin-flip.** Corrections exceed harms only
  slightly; the net is a handful of regions out of ~6200. Absolute root-accuracy gain: **+0.10 to +0.32 pp**
  (top-alt / per-flip); the **oracle ceiling is +0.6 pp** (a perfect key-selector capturing all corr, no harm).
- **The oracle bound EQUALS the top-alt result** (corr-available == top-alt corr; harm-exposed == top-alt harm,
  to the unit on all presets). That is an owed-4 finding in itself: when a carried key CAN flip to the DCML root,
  the **top-ranked** carried key is the one that does — a beam of width >2 over the carried keys adds nothing on
  this corpus (§2.3).

### §2.2 ★ The coupled minority — where the joint step is actually scoped (the honest population)

The trigger the design defines (C3 §3.1) fires only where the L3 key is **uncertain** — D-L3a sequence margin
`keyConfidence` below its bar (the `uncertainThreshold` default **1.0**, `keymodesequence.h:141` `[code]`;
CLAUDE.md-verified, **not** the demoted emission sigmoid). Restricting the benefit to those regions:

| preset | coupled flipped regions (n) | corr / harm / neutral | **net** |
|---|---|---|---|
| Baroque | 16 | 4 / 4 / 8 | **0** |
| Jazz | 15 | 8 / 3 / 4 | **+5** |
| Default | 11 | 2 / 4 / 5 | **−2** |

**On the population the joint step is theory-scoped to, the net is zero-to-noise (0, +5, −2) on n = 11–16.** The
sign is not even stable across presets. This is the sharpest form of the go/no-go: the coupled minority — the
*only* population for which the contract theory-justifies a key-coupled chord re-decode — does not yield a
reliable correction surface.

> **★ OI-160: this table is BYTE-IDENTICAL under the corrected ground truth** (4/4/8, 8/3/4, 2/4/5 — every
> cell unmoved). The OI-142 correction re-sorted three graded flips corpus-wide (§2.1), and **none of them
> fell in the coupled minority.** The sharpest evidence the no-go rests on is therefore untouched by the
> correction, not merely unthreatened by it.

### §2.3 The fire-rate (owed-1 / owed-3) and beam width (owed-4)

- **Fire-rate [owed-1/3].** The chord winner flips under some carried key in **99 / 95 / 89** committed regions =
  **1.5 % / 1.5 % / 1.4 %** of committed regions; on the coupled minority **16 / 15 / 11** = **1.4 % / 1.0 % /
  0.9 %**. `[data]` This is the true C3 fire-rate the C3 report found un-computable read-only
  (`cc_engage_c3_measurement_report.md` §2.3) — now measured via the pure re-decode. It is **~10× below** the
  `decideJointKey` structural proxy (`coupled` ~13.5 %, `jointkeydecision.h:59-61` `[code]`), and far below the
  ~25 % ≥3rd-root fan-out. **The chord axis is almost always key-stable** — grounded, not surprising (§4):
  the top carried alternatives are chiefly **relative / closely-related keys sharing the diatonic collection**, so
  the decoder's diatonic-prior term barely shifts and the winner root does not move.
- **Beam width [owed-4].** The carried-key count per region (argmax + `keyAlternatives`) is **exactly 5 in ~98 %**
  of regions (Baroque 10030 of 10255 at width 5; 178 at 6; 47 at >6) — the `maxAlternatives = 4` cap
  (`KeyModeSequencePreferences`, `[code]`) ⟹ ≤5 keys, confirmed as **almost always exactly 5**. But §2.1 shows a
  **width-2 beam (argmax + top alt) already captures every available correction** — the extra carried keys do not
  add corrections. So the design's beam-width floor is over-provisioned relative to the measured need.

### §2.4 Which of the six owed measurements this settles read-only, and which stay build-gated

| owed | settled here (read-only)? | result / why |
|---|---|---|
| **[owed-1]** true C3 fire-rate | ✅ **settled** | 1.4–1.5 % committed; 0.9–1.4 % coupled (§2.3) |
| **[owed-3]** per-key winner flip-rate | ✅ **settled** | same measurement — the flip IS the winner-root disagreement across carried keys (§2.3) |
| **[owed-2]** coupling benefit magnitude | ✅ **settled at the go/no-go granularity** | net +9/+3/+10 overall, 0/+5/−2 coupled (§2.1/§2.2). A *production* robust-stop-restricted-to-coupled before/after (design's owed-2 instrument) needs the **built** joint settle — **build-gated**; but the go/no-go the build decision turns on is settled here. |
| **[owed-4]** beam width / fixpoint depth | ◑ **partly settled** | width: ~5 carried, but width-2 captures all corrections (§2.3). Whether a bounded fixpoint over the joint scorer adds anything is **build-gated** (needs the joint scorer). |
| **[owed-5]** coupling-term form under re-decode | ⛔ **build-gated** | an A/B of `couplingScore` forms requires the built joint scorer; not read-only. |
| **[owed-6]** precision-phase constants | ⛔ **build-gated (R5)** | Stage-5 fits; out of scope for a measurement pass (#8). |

---

## §3 — The pedal owed-P1 (Task 3, secondary): reader-over-carry vs in-place detection

**[owed-P1]** (`cowork_layer5_engagement_design.md` §6.2 / §8.3): does the pedal reading read from the **carried
distinct-root alternative** (bass-as-non-chord-tone) **agree** with today's in-place `applyIter8691Pedal` pass2
upper-voice detection? Measured: over regions where production stamps `isPedalPoint`
(`chordanalyzer.h:280` `[code]`), does the decoder carry under the argmax key already hold the production pedal
(upper-voice) root (a root ≠ bass in the representative committed slice's `chosen ∪ alternatives`)?

| preset | production pedal regions | carry already holds the pedal root | agreement |
|---|---|---|---|
| Baroque | 5 | 1 | 0.20 |
| Jazz | 2 | 1 | 0.50 |
| Default | 5 | 1 | 0.20 |

**Finding — but UNDERPOWERED, flagged (#5).** Agreement is **low (1 of 2–5)**, which leans toward the §6.3
`[flag]` conclusion: the carried distinct-root alternative does **not** reliably reproduce the in-place
upper-voice re-decode, so a pure carry-reader would need the **upper-voice-conditioned Layer-4 carry attribute**
form, not the bare reader. This is consistent with the audit's named gap — **the decoder has NO pedal detection**
(`chordslicedecoder.cpp` grep → 0 matches; `[design]` §6.1) — so its carry commits the bass-rooted / full-voice
reading rather than the upper-voice chord. **However n = 2–5 per preset is far too small to settle owed-P1.** The
production pedal population on the Bach chorale corpus is tiny; the agreement figure is a directional signal, not
a decision. **Declared to Cowork:** owed-P1 is *measured but underpowered*; a decisive read needs a pedal-dense
corpus (the DCML `pedal` GT column exists — `dcml_parser.DcmlRegion.pedal` `[code]` — a future pedal-scoped
measurement could use it).

---

## §4 — Does this close a surprise? (#3 discharge)

**No new #3 surprise — but a decisive sizing that sharpens the design's own owed expectation.** The design flagged
owed-2 honestly: the coupling benefit magnitude was **unmeasured**, expected "qualitative, low single-digit
points" (`[design]` §5). The measurement lands **below** that: sub-single-digit overall, ~zero on the coupled
minority. The reason is **fact-grounded, not surprising** (#1): the carried key alternatives are overwhelmingly
**diatonic-collection siblings** (relative major/minor, enharmonic-signature pairs — see the smoke region
`bwv10.7@0`: argmax G-minor plus four alternatives all re-decoding to the **same** root 7). The chord scorer's
key-dependence enters only through the **diatonic-prior term** (`chordslicedecoder.h:130` `[code]`) and the
**symmetric-rotation spelling-pin** (G4/C1) — both of which barely move when the alternative key shares the
collection. So the key→chord coupling is **structurally weak** on tonal common-practice music, exactly because
the hard key decisions are between collection-siblings that name the same chords.

Where this **does** matter (the genuinely-coupled cases — a modulation seam, a relative-pair boundary where the
alternative key is a *different* collection) is precisely the coupled minority — and there the n is 11–16 and the
net is ~0. So the honest reading: **the joint step's chord axis is not where the precision headroom is.** The
precision-headroom re-grounding already said as much (root-err is 95 % functional/"neither", 5 % vertical;
`project_precision_headroom_regrounding.md`) — the chord *root* rarely turns on the key.

Per #8/#13: this is a **measurement handed up**, not an inference fix built. The build decision is Cowork's/the
user's, now on measured fact rather than the unmeasured "biggest lever" assumption.

---

## §5 — Boundary honored + both stops green (byte-identity proof)

- **No production behavior change.** `--dump-joint-probe` is default-OFF and returns before the standard
  `writeJson`. The change is purely additive (a new diagnostic function + flag + help text in
  `tools/batch_analyze.cpp`; a new harness `tools/measure_joint_probe.py`) — **no existing code path modified**,
  **no `src/` touched**.
- **Byte-identity proof.** With the new binary, standard `--preset Baroque` analysis of **12 corpus stems**
  reproduces the committed `tools/corpus/baroque/*.ours.json` **byte-for-byte** (12/12; spot check + additive-gated
  structural argument). ⟹ the **robust-stop** (class-(b) root-disagree DURATION) and the **batch 52/24/52 stop**
  are **identity-PASS by construction** (no analysis output moved; no golden refresh). Corpus frozen `c50002fee1`.
- **No fit, no tune, no build of the joint step** (#8; the dispatch moratorium): no beam driver, no wiring, no
  constant fitted. Measurement only.
- **Pushed fork-only** (`cfc7eb5e39` upstream HARD STOP honored; `upstream` untouched).

---

## §6 — Acceptance checklist (this pass)

- ✅ **The probe exercises the existing `ChordSliceDecoder` as a pure re-decode under carried keys** — production
  byte-identical (12/12 spot check + structural).
- ✅ **★ The benefit measured as corr/harm/neutral vs DCML — the joint-step go/no-go — reported ×3 presets:**
  net **+9 / +3 / +10** overall; **0 / +5 / −2** on the coupled minority; oracle ceiling **+0.6 pp**. **The
  measured evidence does not support building the joint step as a precision lever.**
- ✅ **Fire-rate** (1.4–1.5 % committed, 0.9–1.4 % coupled — ~10× below the 13.5 % proxy) + **beam width**
  (~5 carried; width-2 captures all corrections) reported; the read-only-now owed measurements (owed-1/2/3,
  partial owed-4) settled, the build-gated ones (owed-4 fixpoint, owed-5, owed-6) flagged (§2.4).
- ✅ **Pedal owed-P1 agreement measured** — low (0.20 / 0.50 / 0.20) but **underpowered (n = 2–5)**; flagged, not
  decided.
- ✅ **Report + fold, stamped (#16), with SHAs** — corpus `c50002fee1`, instrument `689840d2ef`, HEAD `fa0a881aa4`.
- ✅ **No production change / no build of the joint step / no fit; both stops green; pushed fork-only.**

*CC, 2026-07-07. Engage arc #12 — Stage 3 opens measurement-first (#1/#3/#5): measure whether the joint step
pays before building it. Measured answer: it barely pays overall and not at all on the coupled minority the chord
axis is scoped to. On this report: Cowork verifies at objects → brings the go/no-go + sizing to the user; the
build decision is theirs, on measured fact.*
