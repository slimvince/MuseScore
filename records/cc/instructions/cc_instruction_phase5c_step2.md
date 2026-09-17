# CC Instruction — Phase 5c Step 2: the cadence detector (L5 §5.2, dormant)

> **Plan: `cowork_phase5c_l5_build_plan.md` Step 2. Spec: `cowork_layer5_function_design.md` §5.2 + the §5.0 shared defs
> (the contract — implement its mechanism, do not re-spec).** Step 1 ratified. Build the **key-agnostic, event-pair,
> feature-scored cadence detector** as its **own dormant unit** (consumed later by Step 3 resolver + Step 4 modulation),
> **byte-identical on production**. **Default constants (firewall) — no tuning. Reuse the frame, build the corrected
> logic. Proportionality: build it right and stop; the half cadence is the weakest link in the literature — hold it at low
> confidence, do not chase it.** *(Reminder: the never-bash rule is Cowork's.)*

## §0 — Preamble (sweep)
Commit local-only the unstaged Cowork docs (the Step-1 §5.0 syncs): `docs(cowork): Phase-5c Step-1 ratification + §5.0 syncs`.
Report the sha.

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read-only, confirm and report:
- **The event-pair inputs:** the committed chords of an approach→arrival pair + their **inversion/bass** (from L4 /
  `bassPc`), the **leading-tone resolution** as a detected voice-motion event (L1 note voices across the boundary), the
  **genuine-dominant** test (a seventh / tritone resolving), and the **bass scale-degree** pair — all reachable.
- **The phrase gate:** the dormant **phrase-boundary primitive** (`phraseBoundaryTicks`) is consumable for the
  chorale phrase-gate (§5.2 admits a candidate only at a phrase boundary).
- **Reuse vs build — be precise:** **reuse** the dormant `cadencekeyanchor`'s **key-agnostic frame** + its primitives
  (`endsPhrase`, `chromaticLeadingTone`, the salience inputs); but its **leading-tone-PRESENCE** test is the broken one
  (the major-third-as-LT false positive on I→IV/I→V) — **do NOT reuse that logic; BUILD the corrected event-pair +
  leading-tone-RESOLUTION detection** that replaces it (dormant). The circular **production** `detectCadences()` is **not**
  touched here (its retirement is Phase 5d).
If an input is unreachable, or the corrected detector needs a structural change beyond a new dormant unit → **STOP and
report.**

## §2 — BUILD the cadence detector (§5.2), dormant
Implement §5.2 exactly, on the event pair (approach → arrival), as its own unit:
- **Cadential-six-four collapse FIRST** — a 2nd-inversion tonic-spelled sonority (from L4's chord) over a held bass
  scale-degree five proceeding to a root-position dominant → collapse to one dominant approach so the cadential bass reads
  five-to-one.
- **Authentic test:** the **sequence** (pre-dominant → dominant → tonic) **and** at the pair: bass **5→1**, **leading-tone
  resolution** (the 7→1 voice-motion event across the boundary — *resolution*, never mere presence), and a **genuine
  dominant** (seventh or tritone resolving).
- **Typology** (§5.2): **perfect/imperfect by the BASS-DERIVED INVERSION** criterion (both chords root position →
  perfect; an inverted chord → imperfect; the **top-voice arrival is only a soft optional nudge, never the hard test** —
  the §5.2 amendment; do **not** build a top-voice requirement, do **not** identify the melody); **half** (terminal
  root-position dominant; **Phrygian** = pre-dominant-6 → V, bass semitone 6→5); **deceptive** (cadential V → submediant);
  **plagal / evaded** at **lower confidence** by rule.
- **Chorale phrase-gate:** admit a candidate only at a phrase boundary (consume `phraseBoundaryTicks`).
- **Weighted tonic-vote:** each admitted cadence casts the §5.2 vote (a weighted sum of evidence-strength + salience cues,
  minus the per-type lower-confidence discount). **Key-agnostic** — the detector reads no resolved key; the vote *informs*
  the key.

## §3 — Constants
- The **tonic-vote weights** and the **per-type lower-confidence discounts** stay at the spec's stated **defaults** —
  **no tuning** (firewall; that is Phase B). The half cadence is held at the modest default confidence the literature
  warrants; do not chase it.

## §4 — Tests (oracle-asserted)
- A root-position V7→I with both chords root position is a **PAC**; the same with an inverted tonic is an **IAC** (by
  inversion, not top voice); a `iv6→V` minor-mode pair with the semitone bass is a **Phrygian half**; a cadential V→vi is
  **deceptive**; the **cadential-6/4 collapse** reads the bass as 5→1; a passing **I→IV is NOT a cadence** (the
  false-positive the old presence-test hit — the corrected resolution test rejects it).

## §5 — Gate
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, no golden refresh (the new unit has **no production consumer**; the live
  `detectCadences()` is untouched). Movement → STOP.

## §6 — Deliver
Commit **locally (unpushed)**: the new dormant cadence-detector unit + the §4 tests. Write `cc_phase5c_step2_report.md`
(gitignored): the §1 confirm (incl. the reuse-frame / build-corrected-logic split), the §2 build, the §4 tests, the §5
gate result, and the commit sha — so Cowork verifies the unit is dormant, reuses the key-agnostic frame (not the broken
presence test), and honours the §5.2 inversion-anchored amendment.

## §7 — Stops
- An input unreachable; the corrected detector needs structure beyond a dormant unit; or you find yourself reusing the
  broken leading-tone-presence logic → STOP, report.
- Touching the live `detectCadences()` (that retirement is Phase 5d) → STOP. Any threshold/weight **tuning** → STOP
  (firewall). Any production movement → STOP. `upstream` → STOP.
