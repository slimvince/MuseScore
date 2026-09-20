# J-key-i — Scoped Constrained-Joint KEY Decision: diagnostic build + measurement

> **HELD — uncommitted, diagnostic-only, production byte-identical.** First build of
> `docs/scoped_joint_design.md` §6 (the key-axis-first step) as a measurement that runs
> PARALLEL to production. No production resolve-path edit; no commit. Cowork verifies at
> source; user ratifies J-key-ii (the wiring) separately.
>
> **Date:** 2026-06-15. **HEAD:** `2245aedf82` (unchanged). **Scope of numbers:** WiR-Bach
> covered stems only (326/353 aligned); non-Bach unmeasured (stated). Every key is `[oracle]`
> via the committed `dcml_parser`/`compare_rn` machinery; every number is `[probe]` from the
> read-only instruments below. Weights are provisional `[empirical — Stage-5 fits]`.

---

## 0. Headline

1. **The SOFT constrained-joint key decision beats the production resolver on the key axis,
   robustly across all three presets** — key-accuracy (vs DCML) **+3.80 pp Default / +3.50 pp
   Baroque / +12.24 pp Jazz**; genuine key error (S2) **−140 / −96 / −1706**. The soft decision
   lands at **58.5–58.8 % on every preset** where production ranges 46.4 %→55.0 % — it is
   *preset-stable* because it leans on the notated signature + key-agnostic evidence, not the
   preset-tuned resolver (this is the whole Jazz gap).
2. **The SCOPED JOINT adds ~nothing on the key axis** — the soft→joint increment is
   **−0.04 / −0.14 / −0.06 pp** (inert, marginally negative). On the key axis the chord×key
   coupling, as formulated, does not move the decision: **the gains are entirely from the SOFT
   broad-evidence re-rank, not the joint search.** (Consistent with the meta-principle and with
   the measured sparse coupled core; it argues J-key-ii should wire the *soft* decision and
   leave joint-coupling to the chord axis.)
3. **⛔ A §7 STOP fired — the home-fifths HARD constraint is UNSAFE.** At DCML *key-stable*
   regions the notated signature fifths disagree with DCML's global key **~17 % of the time
   (17.0 / 17.0 / 17.2 %; 56 stems)** — spot-verified as partial/**Dorian signatures**
   (e.g. `bwv254`, `bwv265`: D minor notated with 0 flats) plus analyst global-key conventions.
   Per design §3/§10 and J-key-i §7, **the notated-fifths-as-hard pin must be DEMOTED to soft
   (or refined with note-based signature inference) before J-key-ii wiring.** This is the one
   load-bearing finding; it is the documented systematic Baroque partial-signature mis-keying,
   now quantified on the key-decision safety gate (the residual probe's "safety PASSES" was the
   *chord*-pin; the *key* home-fifths pin had never been safety-measured — this is the first).
4. **Production is byte-identical** — 353/353 `.ours.json` per preset reproduce the committed
   baseline once the additive `jointKey` block is stripped (0 production-field diffs); BIR gate
   **57 / 23 / 57**; suites green (composing **545**, notation **57**, snapshots **11/11**).

**Recommendation:** ratify the SOFT key decision as the J-key-ii lever (it is the measured win,
preset-robust). **Do NOT wire the home-fifths as a hard constraint** — demote/refine it first
(partial-signature handling). **Do NOT wire the scoped joint-coupling for the key axis** (it is
inert here; its value, if any, is the chord axis — J-chord). Keep cadence/modulation/
bass-is-root/declared-mode SOFT (they are, structurally).

---

## 1. What was built (J-key-i §2, §3)

A new **diagnostic producer** + read-only instruments. **Zero** `src/notation` / `src/engraving`
production edits; all work in the CLAUDE.md autonomous zone (`src/composing/`) + `tools/`.

- **`src/composing/analysis/section/jointkeydecision.{h,cpp}`** — `decideJointKey(regions,
  fifths, weights)`. Per region it produces **two** key/mode decisions (the attribution toggle,
  mirroring 4b-i's dual-condition measurement):
  - **config A (soft-only):** hard-fifths home-pair prune → soft re-rank (scale/collection prior,
    cadence anchor `[SOFT]`, modulation hypotheses `[SOFT]`, bass-is-root `[SOFT]`, declared-mode
    hint 1.0 `[SOFT]`) decoded as a **global key-path Viterbi** with a modulation transition
    penalty. No joint.
  - **config B (soft + scoped-joint):** identical, except on the **coupled core** (chord-ambiguous
    AND key-modulation-ambiguous) the key emission is augmented by the best chord candidate's
    key-fit, so chord and key are decided jointly (§5 of the design).
  - It consumes the committed key-agnostic instruments verbatim (`detectAuthenticCadences`,
    `detectLocalModulations`) + the existing `analyzeKeyMode` local candidates (a SOFT prior).
- **`tools/batch_analyze.cpp` `--dump-joint-key`** — appends a top-level `"jointKey"` object
  (per-region two-config decisions + structural flags + anchor/scope tallies). Default OFF.
- **`tools/run_bach_preset.py --dump-joint-key`** — passes the flag through for corpus regen.
- **`tools/cc_j_key_i_measure.py`** — the DCML measurement (reuses `compare_analyses` /
  `dcml_parser` / `compare_rn` verbatim; nothing re-defined).
- **`tools/cc_j_key_i_byteid.py`** — the byte-identity proof (strips the additive `jointKey`
  block, diffs the rest vs the committed baseline corpus).
- **`src/composing/tests/jointkeydecision_tests.cpp`** — 7 unit tests pinning the invariants.

### No-circularity / no-production-leak (design §10; J-key-i §2, §5) — VERIFIED
- The decision reads **only** key-agnostic + local-candidate evidence. The production resolved key
  is carried as `prodTonicPc/prodIsMajor` and **only echoed** in the dump — `decideJointKey` never
  reads it (unit test `ProductionKeyEchoedNotRead`: a deliberately-wrong prod key does not perturb
  the result). The cadence/modulation inputs are `CadenceRegionInput`-shaped (ticks/rootPc/quality/
  pcMask) — physically incapable of carrying a key.
- The producer appears **only** on the `--dump-joint-key` tools path. The production resolver /
  winner / rendered RN never call it.
- Every soft term is an **additive re-rank** of the hard survivors — no early-out / disqualify on a
  soft term, so no soft score can veto a hard fact (the −7-wall-in-reverse safety property is
  structural). The cadence anchor / modulation / bass-is-root / declared-mode are all SOFT
  (J-key-i §7 stop "a soft producer treated as hard" did NOT fire).

---

## 2. §5 — Byte-identity + suite gates (the diagnostic must not perturb production) — ALL PASS

| Gate | Result |
|---|---|
| `.ours.json` byte-identity (flag-ON stripped vs committed baseline) | **353/353 each preset, 0 production-field diffs** (Default/Baroque/Jazz) |
| Local flag-OFF vs flag-ON-stripped (bwv10.7) | **identical, 79077 = 79077 bytes** |
| BIR gate (case-identity → byte-identity preserves it) | **Default 57 / Baroque 57 / Jazz 23** (== gate) |
| composing_tests | **545 / 545 PASS** (538 baseline + 7 new `JointKeyDecision`) |
| notation_tests | **57 / 57 PASS** |
| pipeline_snapshot_tests | **11 / 11 PASS** (1 expected skip), **goldens unchanged** (no `--update-goldens`) |

The `jointKey` block is purely additive (appended after the `regions` array); the production
writer is untouched ⇒ byte-identity is structural and empirically confirmed. (The instruction's
"composing 505" was a stale estimate; the at-source baseline is 538, confirmed.)

---

## 3. §4.1 — KEY AXIS (config vs DCML; scored = correct + S1 + S2)

`correct` = config (tonic,mode) == DCML **local** key. `S1` (=global ≠local) = config == DCML
global but DCML modulated (stayed home / masked modulation). `S2` = genuine error (≠ both).

### Default
| config | scored | correct | S1 | S2 | key-acc |
|---|---|---|---|---|---|
| production | 10109 | 5556 | 3021 | 1532 | 55.0 % |
| **soft** | 10109 | 5940 | 2777 | 1392 | **58.8 %  (+3.80 pp)** |
| joint | 10109 | 5936 | 2775 | 1398 | 58.7 %  (+3.76 pp) |

### Baroque
| config | scored | correct | S1 | S2 | key-acc |
|---|---|---|---|---|---|
| production | 10119 | 5566 | 3035 | 1518 | 55.0 % |
| **soft** | 10119 | 5920 | 2777 | 1422 | **58.5 %  (+3.50 pp)** |
| joint | 10119 | 5906 | 2772 | 1441 | 58.4 %  (+3.36 pp) |

### Jazz
| config | scored | correct | S1 | S2 | key-acc |
|---|---|---|---|---|---|
| production | 9788 | 4544 | 2104 | 3140 | 46.4 % |
| **soft** | 9788 | 5742 | 2612 | 1434 | **58.7 %  (+12.24 pp)** |
| joint | 9788 | 5736 | 2612 | 1440 | 58.6 %  (+12.18 pp) |

**Scoped-joint increment (joint − soft): −0.04 / −0.14 / −0.06 pp** — inert, marginally negative.
**S2 (genuine key error) reduction soft−prod: −140 / −96 / −1706.**

**Reading:** the SOFT constrained re-rank is the entire lever; the scoped joint is dead weight on
the key axis. The soft decision is preset-stable (~58.5–58.8 % everywhere); production's Jazz
collapse (46.4 %, S2=3140) is bypassed because the soft decision does not depend on the
Jazz-tuned resolver.

---

## 4. §4.1 — Relative-pair recovery (mode-correct among same-signature regions)

The measured floor (relative-major/minor disambiguation): among regions whose key shares DCML's
local signature, how often is the **mode** right.

| config | Default | Baroque | Jazz |
|---|---|---|---|
| production | 78.2 % | 78.6 % | 80.2 % |
| **soft** | **81.7 %** | **81.9 %** | **81.5 %** |
| joint | 81.7 % | 81.8 % | 81.5 % |

+3.3–3.5 pp Default/Baroque; +1.3 pp Jazz. Joint == soft. The residual ~18 % relative-pair error
is dominated by the **cadence anchor's piece-global mode call** being too coarse (worked example
§7) — a soft-weight/sectionality calibration target for Stage 5, not a joint-search gap.

---

## 5. §4.2 — Modulation correctness / de-masking (among DCML local ≠ global)

Scored against DCML **directly** (config local == DCML local), NOT the gameable `rn_agree`.

| config | Default | Baroque | Jazz |
|---|---|---|---|
| production | 10.2 % (410/4036) | 9.8 % (397/4046) | 17.2 % (672/3915) |
| **soft** | **16.9 % (684/4036)** | **17.2 % (697/4046)** | **18.8 % (736/3915)** |
| joint | 16.9 % (684) | 17.2 % (694) | 18.9 % (739) |

The soft decision places **~1.7× more** modulations correctly than production on Baroque/Default
(the modulation detector is now an active SOFT lever, where in production it is unwired). The
absolute level (~17–19 %) is bounded by the modulation detector's known precision/recall ceiling
(`cc_stage4d_i_report.md`: recall 33 %, precision ~47 %) — this is the upstream lever to lift, not
the joint search.

---

## 6. §4.3 — HARD-CONSTRAINT SAFETY (the design §3/§10 gate) — ⛔ ONE FAILURE

### (a) Home-fifths pin — IMPLEMENTED — **FAILS at ~17 % (the §7 STOP)**
At DCML key-stable regions (local == global), the notated signature fifths **disagree with DCML's
global key**: **Default 1032/6073 = 17.0 %, Baroque 1034/6073 = 17.0 %, Jazz 1012/5873 = 17.2 %**
(**56 stems**). Spot-verified at source:
- `bwv254`, `bwv265`: DCML global **D minor**, notated **0 flats** → **D Dorian** partial signature
  (the documented systematic Baroque mis-keying — `project_key_detection_baroque_partial_signature`).
- the remainder is a mix of further partial/Dorian signatures and DCML analyst global-key
  conventions (precise split deferred to J-key-ii).

**Consequence:** because the home pair is the only non-modulation key the producer can emit, a
partial-signature chorale's *true* home key is structurally excluded — the hard-fifths prune pins
a DCML-disagreeing key. **This is exactly the §7 stop condition ("a hard constraint pins a key
that disagrees with DCML → STOP, report, demote to soft").** It fired. Production shares the same
notated-signature ceiling (it is "locked to the notated signature"), so the ceiling is not unique
to the producer — but as a *hard* constraint it is unsafe and **must be demoted to soft / refined
with note-based signature inference before J-key-ii.**

### (b) Candidate "pinned-chord ⊆ key collection" — measured UNSAFE → correctly left SOFT
At chord-pinned regions, requiring the DCML local key's collection to contain the pinned chord
would prune it **14.0 / 14.0 / 13.9 %** of the time (a pinned chord carries a note outside the
local collection — secondary dominants, applied chords, raised LTs). A nonzero rate ⇒ the
candidate constraint is unsafe ⇒ **it is correctly NOT a hard constraint** (the §3 "demote to
soft" rule, applied a priori and now quantified). The producer never used it; this measures *why*.

---

## 7. §4.4 — Per-case adjudication (joint changes key vs production)

Because joint ≈ soft, these are effectively **soft-vs-production** moves.

| bucket | Default | Baroque | Jazz |
|---|---|---|---|
| genuine_win (config correct, prod not) | 768 | 739 | 2079 |
| genuine_loss (prod correct, config not) | 388 | 399 | 887 |
| convention_boundary (same non-correct bucket) | 137 | 126 | 430 |
| dcml_noise (DCML unparseable) | 0 | 0 | 0 |
| other_move (lateral non-correct) | 328 | 342 | 822 |
| **net (win − loss)** | **+380** | **+340** | **+1192** |

**Worked example — `bwv10.7` (home pair Bb major / G minor, notated −2):** ticks 0–3360 DCML
local = **G minor** = global; production correctly stays G minor; soft/joint globalize to
**Bb major** → `genuine_loss` (the cadence anchor's piece-global relative-major bias). Ticks
3840+ DCML modulates to local **Bb major** ≠ global G minor; production stays G minor (wrong);
soft/joint say Bb major → `genuine_win`. One chorale shows **both** sides: the cadence anchor's
*global* mode call is right for the middle section and wrong for the opening — the relative-pair
loss is a **sectionality/soft-weight** problem (Stage-5 calibration), not a joint-search problem.

---

## 8. Scope cross-checks + caveats

- **Coupled-core fraction: 23.7 / 23.8 / 21.1 %** (vs the dossier's oracle ~13.5 %). The
  diagnostic's *structural proxy* for "key-ambiguous" (covered by, or adjacent to, a committed
  modulation span) is **broader** than the oracle 2×2 (chord-AMBIG & key-MODULATION) — it
  over-counts ~1.6–1.75×. It is still **scoped, not a full lattice** (the §7 "balloons toward a
  full lattice" stop did NOT fire; the per-region joint is over a ≤(2 + #spans) state set). The
  joint being inert despite the *larger* proxy core only strengthens conclusion #2.
- chord-PINNED 67.6 / 67.7 / 70.2 %; key hard-pinned (no span covers) 38–41 %.
- **WiR-Bach only** (326/353 aligned). Non-Bach unmeasured. Jazz key S2 carries DCML-parse
  unreliability (stated in the design); the Jazz numbers track the same shape as Baroque/Default,
  so the conclusions are corpus-robust.
- Weights `[empirical — Stage-5 fits]`, not corpus-fit to any gate. The relative-pair and
  modulation residuals are calibration-sensitive (the soft win could grow with Stage-5 fitting).

---

## 9. §7 — Stop conditions: status

| Stop condition | Fired? |
|---|---|
| Production resolve-path / `src/notation` / `src/engraving` edit needed | **No** |
| **A hard constraint pins a key that disagrees with DCML** | **YES — home-fifths, ~17 % (§6a). Reported; recommend demote/refine before J-key-ii.** |
| A soft producer treated as hard | No (additive structure; asserted) |
| Production output / BIR gate / snapshot golden moves | No (byte-identical; 57/23/57; 11/11 unchanged) |
| Coupled core balloons to a full lattice | No (21–24 %, scoped) |
| Uncertain key decision | Adjudicated vs DCML; bucketed (§7) |

The diagnostic build itself is complete and clean. The fired stop is a **HOLD on J-key-ii**, not
a defect in J-key-i.

---

## 10. Recommendation for the user (J-key-ii ratification input)

1. **Ratify the SOFT constrained-joint key decision** as the wiring lever — it is the measured,
   preset-robust win (+3.5 / +3.8 / +12.2 pp; S2 −96/−140/−1706; relative-pair +3 pp; modulation
   ~1.7×).
2. **Demote the home-fifths from HARD to SOFT, or add note-based signature inference**, before
   wiring (the §6a/§9 safety failure — ~17 %/56 stems of partial-Dorian + convention). Without
   this the producer cannot represent the true key of a partial-signature chorale.
3. **Do NOT wire the scoped joint-coupling for the key axis** — it is inert-to-harmful here
   (−0.04…−0.14 pp). Reserve the joint for the CHORD axis (J-chord).
4. Continue to keep cadence / modulation / bass-is-root / declared-mode **SOFT**.
5. Lift the modulation detector's upstream precision/recall (the bounded ~17–19 % de-masking
   ceiling) — the cadence #4 dominant/subdominant guard + relative-pair anchor already on the
   branch — to raise both the modulation and relative-pair soft wins.

---

## 11. Notes

- **Sandbox-bash noise:** one path quirk — the Bash tool's `/tmp` (MSYS) and Windows-`python`'s
  `/tmp` (= `C:\tmp`) differ; smoke artifacts were written to `C:/tmp/` to bridge it. Corpus +
  measurement ran clean. Host-side Read/Grep are authoritative for any spot-check.
- **Working tree:** carries the pre-existing HELD diagnostics (4b-i ` M` sandbox-noise on
  committed files, per STATUS) plus the new J-key-i files below — all **uncommitted**.
- **Gitignored:** this report (`/cc_*.md`) and the `tools/corpus/*_jki/` measurement corpora
  (`/tools/corpus/`) are gitignored — HELD by construction.

### Files (HELD, uncommitted)
- `src/composing/analysis/section/jointkeydecision.h` `.cpp` (new)
- `src/composing/tests/jointkeydecision_tests.cpp` (new) + `CMakeLists.txt` registrations
- `src/composing/analysis/CMakeLists.txt` (module registration)
- `tools/batch_analyze.cpp` (`--dump-joint-key` diagnostic, flag-gated)
- `tools/run_bach_preset.py` (`--dump-joint-key` pass-through)
- `tools/cc_j_key_i_measure.py`, `tools/cc_j_key_i_byteid.py` (new instruments)

**HELD — uncommitted. Cowork verifies at source; user ratifies J-key-ii separately.**
