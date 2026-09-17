# CC Instruction — J-key-ii-redux: SCOPED confidence-gated partial-signature override, MEASURE-FIRST + DIAGNOSTIC (HELD)

> **Ratification-gated, DIAGNOSTIC-ONLY, production byte-identical.** Replaces the J-key-ii **global**
> signature-demotion (a clean negative: safety only 17%→4.3%, win shrank −1 pp / +118–195 S2 — the §7 stop
> fired) with the user-ratified **scoped** lever (2026-06-15): keep J-key-i's strong signature backbone for
> the correctly-signed bulk; override the home pair to the note-inferred key **only** when note evidence
> *confidently* contradicts the notated signature (the deferred OQ3 detector, now scoped). **No production
> resolve-path edit. No commit. Wiring is J-key-iii, a separate later gate.**

---

## §1 — What this is, and the measure-first order

The J-key-ii finding is structural: a single **global** signature prior is on the wrong side of both cases
(strong to defend a correct signature; weak to override a Dorian lie). The fix is a **per-piece binary
decision** — trust the signature unless note evidence *confidently* says otherwise. The precision-critical
part is the **confidence gate**: a false fire on a correctly-signed piece would override a correct signature
with a wrong note-key and **regress the bulk** (the same precision trap the 4c/4d cadence work hit — the
anchor is ~44% pin-wrong and over-detects subdominants). So this is built in **two ordered steps, the gate
measured BEFORE it is wired into the decision:**

- **Step 1 (measure the gate's separability) — do FIRST, read-only.** Does a precise contradiction
  threshold even exist?
- **Step 2 (build the scoped override) — ONLY if Step 1 finds a usable threshold.**

**NOT in scope:** wiring into production (J-key-iii); the chord axis; the joint-coupling (inert on the key
axis); the learned emission. Any of these → STOP and surface.

## §2 — Scope (autonomous zone only)

All work in `src/composing/` + `tools/`. **Zero** `src/notation`/`src/engraving` edits. The producer stays
diagnostic, parallel to production (`--dump-joint-key` only); production byte-identical. Start from a
**restored J-key-i strong-signature backbone** (the J-key-ii global demotion is reverted in the producer —
the home pair is again the forced home lattice — then the Step-2 override is added on top).

## §3 — Step 1: MEASURE the gate separability (read-only, NO override yet)

Define a per-piece **signature-contradiction confidence** from the **key-agnostic** note evidence already
available (collection-fit margin + the cadence anchor), e.g.: the margin by which the top note-inferred home
key (whole-piece collection-fit, and/or the cadence anchor's tonic) beats the signature relative pair,
**restricted to cases where that note-key's signature fifths ≠ the notated fifths** (the Dorian-lie shape).
Do NOT wire it into the decision — only emit it (additively) and measure.

Measure its **distribution on the two populations**: the **56 partial-signature stems** (true
contradictions — note evidence *should* win) vs the **correctly-signed bulk** (the gate must NOT fire). Report:
- Whether a threshold **separates** them — the precision/recall of "fire the override" at a sweep of
  thresholds (how many of the 56 it catches vs how many correctly-signed pieces it wrongly flags).
- The honest read: is there a threshold with **high precision** (≈no bulk false-fires) at usable recall?
**This is the load-bearing gate.** If no precise threshold separates the populations, **STOP and surface** —
the override cannot be made safe, and a different signal (or accepting J-key-i's ceiling) is the decision.

## §4 — Step 2: build the scoped override (ONLY if Step 1 found a usable threshold)

Keep J-key-i's **strong signature backbone** (the home pair is the forced home for the correctly-signed
bulk — this protects the measured +3.5/+12 pp win). Add: **when the Step-1 contradiction confidence exceeds
the measured threshold for a piece, override the home pair to the note-inferred key for that whole piece**
(partial signatures are a piece-global property → a per-piece swap, not a per-region one). Everything else
unchanged (cadence/modulation/bass-is-root/declared-mode SOFT; the anchor stays a soft term, NOT a candidate
state — its V→IV over-detection, J-key-ii §3). Re-anchor the declared-mode hint onto the overridden tonic
when the override fires (J-key-ii §6 note — otherwise it pulls back to the wrong relative).

## §5 — Measure (all three presets) + byte-identity gates

Re-run the J-key-i / J-key-ii instruments and report:
- **Safety:** the lattice-exclusion / structural-recovery rate on the 56 stems → target **~0** (bwv254 AND
  bwv265 the stress cases — bwv265 must escape A minor this time).
- **Bulk win preserved:** key-acc / S2 / relative-pair / modulation **vs J-key-i soft** — the bulk must be
  **back to J-key-i's win** (the override fires only on the 56, so the correctly-signed bulk should be
  byte-identical to J-key-i's soft decision; verify it).
- **Override precision:** how many pieces the override fired on, and whether any correctly-signed piece
  regressed (must be ~none).
- **Byte-identity** (still diagnostic): production `.ours.json` byte-identical; BIR 57/23/57; snapshots pass
  + goldens unchanged (confirm current counts from STATUS.md); suites green. Any production move = STOP.

## §6 — Deliver: HELD + dossier, and the J-key-iii gate

Write `cc_j_key_ii_redux_report.md` (gitignored, HELD, no commit): the Step-1 separability result
(threshold + precision/recall), the Step-2 safety + bulk-preservation + override-precision numbers, and a
clear **J-key-iii verdict**: *proceed to wire* only if **safety ~0 AND bulk win = J-key-i's win AND override
precision high (no bulk regression)**. Otherwise surface the trade-off. Cowork verifies at source; user
ratifies J-key-iii separately. Note any sandbox-bash noise (host-side Read/Grep authoritative).

## §7 — Stop conditions
- **Step 1 finds no precise threshold** separating the 56 from the bulk (gate not separable) → STOP, surface
  (the override can't be made safe; decision reverts to Cowork/user).
- The override **fires on correctly-signed pieces** (precision too low) / regresses the bulk → STOP.
- The bulk win is **not restored** to J-key-i's level → STOP (the backbone wasn't properly kept).
- Production resolve-path / `src/notation` / `src/engraving` edit needed, or any production-output / BIR /
  snapshot move (diagnostic leaked) → STOP.
- Any attempt to wire into production (that is J-key-iii) → STOP.
- Uncertain key decision → adjudicate vs DCML; bucket + surface — never guess.
