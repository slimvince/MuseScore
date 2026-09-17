# CC Instruction — J-key-i: scoped-joint KEY decision, DIAGNOSTIC + measure (HELD)

> **Ratification-gated, DIAGNOSTIC-ONLY, production byte-identical.** First build of
> `docs/scoped_joint_design.md` §8 (user ratified the scoped constrained-joint design 2026-06-15).
> Implements the §6 **key-axis-first** step as a measurement, not a wiring. **No production resolve-path
> edit. No commit.** Output is a dossier; Cowork verifies at source; user ratifies before anything wires.

---

## §1 — What this is (and is NOT)

Build the **scoped-joint KEY decision** as a **diagnostic producer that runs PARALLEL to production** and
measure it against DCML. It does **not** replace, feed, or alter the production key resolver. The point is
to learn — before wiring — whether the constrained-joint key decision (hard-prune + soft-rank + a scoped
joint on the coupled core) beats the current local resolver on the key axis, and by how much, attributably.

**NOT in scope:** wiring into production (`keyresolver`/`basisIndep`/rendered RNs); the chord axis; the
function axis; the learned dim7 emission (reserved seam, §7 of the design); the gate-layer dissolution;
the file-split. Any of these → STOP and surface.

## §2 — Scope (autonomous zone only)

All work in `src/composing/` (CLAUDE.md autonomous zone) + `tools/` (measurement). **Zero** `src/notation`/
`src/engraving` production edits. The diagnostic producer is a **new module** (e.g.
`src/composing/analysis/section/jointkeydecision.{h,cpp}`) invoked **only** from a diagnostic/tools path —
never from the production resolve path. If implementing it cleanly requires touching a production file,
STOP and surface (do not edit).

## §3 — Build: the diagnostic scoped-joint key-decision producer

Per analysis region, produce a **key/mode decision** by the constrained-joint procedure, emitting it to a
diagnostic dump (no production mutation):

1. **Candidate key/mode hypotheses** per region — the existing local key candidates + the cadence-derived
   local-tonic hypotheses (key-agnostic; the committed `cadencekeyanchor`).
2. **Hard-constraint prune** (design §3 set, key-relevant only): the notated signature **fifths** (reliable;
   mode is NOT hard), and diatonic-membership facts implied by any **complete-clear-vertical-chord** already
   pinned. Disqualify key hypotheses that violate a raw fact; PIN where a unique survivor remains. **A hard
   constraint must never pin a key that disagrees with DCML — measure this rate (§4.3); a nonzero rate is a
   finding to surface, and that constraint is demoted to soft.**
3. **Soft scores** rank the survivors — scale/collection prior, the **cadence anchor (SOFT)**, the
   **local-modulation hypotheses (SOFT)**, **bass-is-root (SOFT)**, and the **global key-path transition
   cost** (modulation penalty across regions), plus the shipped declared-mode **hint (1.0)**. These are
   scores, never vetoes. Assert in code/structure that none of these is treated as hard.
4. **Scoped joint on the coupled core only.** Using the residual probe (`tools/cc_joint_residual_probe.py`),
   identify the regions where, after the hard prune, **both** chord and key remain ambiguous **and** coupled
   (the measured ~13.5%). On *those* regions only, make one joint decision over the surviving (chord, key)
   pairs, scored by the broad soft evidence + key-path, subject to the hard constraints. Everywhere else use
   the forward soft-rank (no joint search).

**Attribution toggle (mandatory, mirrors 4b-i's dual-condition measurement):** a flag that runs the producer
in **two configurations** — (a) **soft-only** (steps 1–3, no joint; scoped joint disabled) and (b)
**soft+scoped-joint** (steps 1–4). Measuring both isolates the joint core's incremental value from the
soft-rank baseline.

## §4 — Measure (all three presets: Default, Baroque, Jazz)

Use the committed DCML **L1 `--key-breakdown`** instrument (`a96f179f40`). Measure BOTH configurations
(soft-only, soft+joint) against the current production resolver as the reference. Report:

1. **Key axis — S1/S2** for production vs soft-only vs soft+joint; the **delta** each config gives, and the
   **soft-only → soft+joint increment** (the joint core's attributable value). Relative-pair recovery
   specifically (the measured floor): how many relative-major/minor regions each config gets right.
2. **Modulation correctness (de-masking).** Score the modulation-bearing regions against DCML directly (not
   gameable global-key agreement) — i.e. does each config place the modulation where DCML does. If a
   dedicated breakdown flag is needed, build it in `tools/` (in-zone); do not invent a metric — state
   exactly what is counted.
3. **Hard-constraint safety.** The rate at which any hard key-prune pins a key that **disagrees with DCML**
   (must be ~0; any case is enumerated + adjudicated). This is the design §3/§10 safety gate.
4. **Per-case adjudication** of every region where soft+joint **changes** the key vs production — against
   DCML, bucketed (genuine win / genuine loss / convention-boundary / DCML-parse-noise, esp. Jazz key
   S2 unreliability).

## §5 — Byte-identity + suite gates (the diagnostic must not perturb production)

Prove the diagnostic addition changes **nothing** in production output:
- **Capture production output BEFORE adding the producer and AFTER**; assert identical on the chord axis
  (`.ours.json`) and key axis. The diagnostic runs parallel — production must be byte-identical to the
  current working-tree baseline.
- **BIR gate 57/23/57** unchanged on all three presets (the diagnostic touches no production path).
- **Snapshots 11/11** pass, goldens **unchanged** (no `--update-goldens` — there is no intended production
  change). Confirm the current count from STATUS.md rather than assuming.
- **Suites green:** composing (505) / notation (57) / snapshots (11/11) — confirm current counts at source.
Any production-output change, gate move, or golden move = **STOP** (it means the producer leaked into
production; it must not).

## §6 — Deliver: HELD + dossier, no commit

Write `cc_j_key_i_report.md` (gitignored) with: the two-config key-axis numbers + the attributable joint
increment, the relative-pair + modulation-correctness breakdowns, the hard-constraint safety rate (+ any
violating case), the full per-case adjudication, and the byte-identity/suite confirmations. **HELD —
uncommitted.** Note any sandbox-bash noise per CLAUDE.md (host-side Read/Grep authoritative). Do not commit;
Cowork verifies at source, user ratifies J-key-ii (the wiring) separately.

## §7 — Stop conditions
- Any production resolve-path / `src/notation` / `src/engraving` edit needed → STOP, surface.
- A hard constraint pins a key that disagrees with DCML → STOP, report the case, demote it to soft.
- Any soft producer (cadence / modulation / bass-is-root) being treated as hard → STOP.
- Production output, the BIR gate, or a snapshot golden moves → STOP (diagnostic leaked into production).
- The coupled-core scope balloons toward a full lattice (it is the measured ~13.5%, scoped) → STOP, surface.
- Uncertain whether a key decision is correct → adjudicate against DCML; if still unclear, bucket as
  convention-boundary and surface — never guess.
