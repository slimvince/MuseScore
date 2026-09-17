# CC Instruction — J-key-iii (Step 2): WIRE the joint key decision into production + measure both axes (HELD)

> **Ratification-gated. INTENTIONAL behavior change — the FIRST production change on the key axis, and the
> first landing of the constrained-joint architecture in production.** Built from the Cowork-verified
> integration spec (`cc_j_key_iii_integration_dossier.md`). Wire the **J-key-i strong-signature-backbone**
> soft decision as a frozen single-forward 2-pass; measure the production delta on BOTH axes; DCML-adjudicate
> every moved case. **HELD for ratification; NO commit until a clean adjudication. Not byte-identical (this
> is the change) — but the KEY axis must transfer exactly (§5).**

---

## §0 — PRECONDITION: restore the J-key-i formulation (ratified)

The on-disk producer is the superseded **J-key-ii** global-soften (`signaturePrior=0.30` + note-inferred
candidate lattice). The user ratified wiring **J-key-i** (the +3.80/+3.50/+12.24 pp profile, 56-stems-at-
signature residual). **First action — restore `jointkeydecision.{h,cpp}` to the J-key-i strong-signature-
backbone:** revert the three J-key-ii demotion changes (drop the note-inferred candidate lattice + the
top-K aggregation, drop `signaturePrior`, restore the **forced signature home pair** as the only non-span
home states — J-key-i `jointkeydecision.cpp:187-205`). The J-key-i state is **uncommitted** (J-key-ii edited
it in place), so this is a **re-derivation from the J-key-i report spec, not a git checkout**.

**Gate (before any wiring):** regen the `--dump-joint-key` diagnostic on all 3 presets and confirm it
**reproduces the ratified J-key-i profile** — key-acc +3.80/+3.50/+12.24 pp vs prod, S2 −140/−96/−1706,
56 partial-sig stems at the signature reading (bwv254/265 → A minor). If it does not reproduce, STOP — the
restore is incomplete; do not wire an unverified formulation.

## §1 — Scope

All wiring in `src/composing/` (the CLAUDE.md autonomous zone) + `tools/` regen. **Zero** `src/notation`/
`src/engraving` edits (the bridge consumes `AnalyzedSection` agnostically). The 2-pass lives at the
`analyzeRegions` boundary; both the notation bridge and `batch_analyze` traverse it, so they share one path.

## §2 — The representation mapping (dossier §3)

The joint decision emits per-region `(tonicPc, isMajor)`. Map to the production `KeyModeAnalysisResult`:
- **`normalizedConfidence`** — **carry the matching pre-joint local candidate's `normalizedConfidence`**
  (the `localCandidates[k]` whose `(tonic,isMajor)` == the joint pick), with a **documented constant
  fallback** when the joint pick is a modulation-span state not among the local candidates. (Reuses a real
  calibrated number; no invented value, no producer-math change.)
- **`keySignatureFifths`** — derive from `(tonicPc,isMajor)`: major → tonic's circle position; minor →
  relative-major fifths. **Partial-signature rule (J-key-i): pin to the NOTATED fifths** (the home pair is
  the signature pair, so this is automatic — confirm it).
- **`KeySigMode`** — major → Ionian, minor → Aeolian. ⚠ **This COLLAPSES the 21-mode space to binary on
  every re-keyed region** (dossier §3). It is inherent to the `(tonicPc,isMajor)` decision. **Do NOT invent
  a mode** — but this collapse is a measured-and-adjudicated item, see §6/§7.

## §3 — The wiring: a frozen single-forward 2-pass (dossier §2, §4)

At / wrapping `region::analyzeRegions`:
1. **Pass-1** — the existing forward loop → regions with production key `K0` + chord `R0` (unchanged).
2. Build `JointKeyRegionInput[]` from those regions (identical to the `batch_analyze.cpp:1069-1110`
   diagnostic construction) and call `decideJointKey` **once** over all regions → per-region
   `(jointTonicPc, jointIsMajor)`.
3. For each region: map (§2) → write `region.keyModeResult`, and **re-run `analyzeChord` under the joint
   key** to refresh `chordResult` (so `basisIndep` reflects it). This pass-2 re-emission is the new behavior.
4. Hand the re-keyed, re-chorded regions to `analyzeSection` unchanged.

**Circularity constraints (MANDATORY — dossier §4, the freeze):**
- Decide `K_joint` **once** from the **pass-1** chords/cadence/modulation, and **freeze it**. The cadence/
  modulation/bass inputs stay on the **pass-1** roots — do NOT recompute them from the re-emitted `R_joint`.
- **Do NOT iterate to a fixpoint** (`re-key → re-chord → re-key → …`) — single forward pass only (an
  iterated loop is an unmeasured feedback system; the §9 balloon stop).

**Hysteresis (dossier §5):** keep **Layer A** (resolver hysteresis) running — it shapes the
`localCandidates` the win was measured on; removing it changes the inputs → the measured numbers stop
transferring. Apply the joint override **AFTER Layer B** (island-stabilization in `analyzeSection`) so the
Viterbi path is authoritative and Layer B doesn't double-smooth a correct one-region joint modulation.
Confirm the exact ordering at source before wiring.

## §4 — Scope-of-change cross-check (no scope creep)

The only production-logic change is the 2-pass + the override mapping, all in `src/composing/`. Do not
touch the resolver internals (Layer A), the gate layer, or the chord templates. If the wiring appears to
require an edit outside `src/composing/`, STOP and surface.

## §5 — The KEY-AXIS INVARIANT gate (the win transfers exactly)

Because `K_joint` is frozen from pass-1 (= the diagnostic's inputs), the **wired per-region resolved key
MUST be byte-identical to the measured `jointKey` decisions** (the diagnostic `softTonicPc/softIsMajor`).
Regen and **assert per-region equality** across all 3 presets. If the wired key axis differs from the
diagnostic decisions, the freeze leaked or an input changed — **STOP and diagnose** (the +3.8/+3.5/+12.24 pp
win only transfers if this holds). This is the cheapest, strongest correctness check of the wiring.

## §6 — Measure the production delta on BOTH axes

Regen all 3 presets (`run_bach_preset.py` Default/Baroque/Jazz) + `characterise_bir_false.py`; run
`composing_tests`, `notation_tests`, `pipeline_snapshot_tests`. Report:
- **Key axis:** confirm §5 (transfers exactly) + the realized S2 reduction vs production.
- **Chord axis (`.ours.json` winner flips):** the new behavior — re-emission under the joint key flips
  ambiguous winners via `diatonicRootContribution`. Size it (how many regions' chord winner moved).
- **BIR gate (the hard-stop axis):** the new 57/23/57 numbers, all 3 presets, with the moved case identities.
- **Snapshots + mode-collapse:** the moved snapshot goldens. ⚠ **The root-based BIR/`rn_agree` metric does
  NOT see a mode collapse** (it scores root+quality, not mode); only the snapshot goldens do. So **separately
  enumerate every region where the wired `KeySigMode` is Aeolian/Ionian but production emitted a non-
  Ionian/Aeolian mode** (Dorian/Mixolydian/…), and whether any such region is a snapshot diff — this is the
  mode-collapse surface, measured, not assumed.

## §7 — DCML-adjudicate every moved case (the ratification gate)

- **Every moved BIR case** adjudicated vs DCML (root_pc + quality). **An un-adjudicated BIR=false increase
  on ANY preset is a HARD STOP** (CLAUDE.md gate policy) — surface it, do not push past.
- **Every moved snapshot golden** adjudicated vs DCML before refresh; refresh **only** DCML-verified-correct
  diffs (`--update-goldens` on `pipeline_snapshot_tests`, then re-run to confirm).
- **Mode-collapse cases (§6):** for each, adjudicate whether collapsing the region's mode to Ionian/Aeolian
  is DCML-correct or a regression vs production's richer mode. Bucket genuine-collapse-regressions separately
  — they are a real consequence of the representation, a finding to surface (accept-as-architecture vs
  address-later is a Cowork/user call, not a CC decision).

## §8 — Deliver: HELD + dossier, commit only on clean adjudication

Write `cc_j_key_iii_step2_report.md` (gitignored, HELD): the §0 restore-and-reproduce confirmation, the §5
invariant result, the both-axes delta, the full BIR + snapshot + mode-collapse adjudication, and a clear
**commit recommendation**: commit only if the key win is realized (§5 holds), there is **no un-adjudicated
BIR=false increase** on any preset, and every snapshot/mode-collapse move is DCML-justified. Sync
`docs/scoring_model.md` if any scoring term/weight moved (the CLAUDE.md sync rule). The commit message must
state this is the **first intentional production behavior change on the key axis** (the constrained-joint
architecture landing). **HELD — Cowork verifies at source; the user ratifies the commit.**

## §9 — Stop conditions
- §0 restore does NOT reproduce the ratified J-key-i profile → STOP (do not wire an unverified formulation).
- §5 wired key axis ≠ the measured `jointKey` decisions → STOP (the freeze leaked; the win won't transfer).
- An **un-adjudicated BIR=false increase** on any preset → HARD STOP.
- The wiring requires an edit outside `src/composing/` → STOP, surface.
- Any iteration-to-fixpoint / recomputing the joint key from re-emitted chords → STOP (single forward pass).
- A snapshot or mode-collapse move cannot be DCML-adjudicated as correct → surface it (do not refresh the
  golden, do not commit past it) — never guess.
