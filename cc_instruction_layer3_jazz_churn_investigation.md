# CC Instruction — Layer 3 wiring: REVERT Step 2 + investigate the Jazz net +1 (read-only; HOLD the commit)

> The two-tier BIR gate is ratified (CLAUDE.md, "Gate threshold and preset policy"). **Decision A (conservative):**
> guardrail (3) — *net BIR=false count non-increasing on EVERY preset* — stays **strict**. The Step-1 wiring passes
> Baroque (53, net −4) and Default (53, net −4) with all-class-(a) new cases, but **Jazz nets +1 (24 vs gate 23)** and
> therefore fails guardrail (3), even though both new Jazz cases are verified class-(a). **Investigate whether the
> Jazz +1 is avoidable WITHOUT weakening the gate or leaving the proper layers, before any commit.**
>
> **★ HOLD: no commit, no push, no golden refresh, no gate edit, no decoder-knob or scorer change.** This is the
> Step-2 revert + a read-only investigation. Production stays uncommitted/held.

## §0 — Revert Step 2 (clean, regardless of the outcome)
Remove the decode-only `scaleMembership` reweight block; confirm the shared scorer is at baseline
(`scaleScoreInKeySigOnly = -0.20`, `scaleScoreInNeither = -0.05`). Step 2 is **BIR-flat and KEY-only** — it left Jazz
at 24 with *and* without it — so it does not bear on the Jazz churn; it is deferred to a separate KEY-metric-gated
increment. The working tree is then **Step-1-only wiring**.

## §1 — Re-verify the Jazz churn cases at the score (independent, post-revert)
On the Step-1-only wiring, list the Jazz BIR delta vs the gate baseline (23): the **2 new** cases (expected
`bwv272@4320`, `bwv291@17760`) and the case(s) **fixed** (net +1 ⇒ 2 new − 1 fixed; name the fixed case). Re-confirm
**each new case at the score** (the music21 GT region) is genuinely class-(a) symmetric / share-tone — do **not**
rely on the prior classification; the case set may shift slightly after the Step-2 revert. **Any new Jazz case that
is not *provably* class-(a) is class-(b) = a real regression = STOP and surface** (that changes everything).

## §2 — Characterize AVOIDABILITY (read-only; measure on the corpus, all three presets)
Can Jazz be brought net-non-increasing **without** (i) weakening the gate, (ii) tuning decoder-private knobs
(ratified exhausted), (iii) preset-conditioning the decoder (new architecture), or (iv) Step 2? The **one** in-scope
proper-layer lever is the slice→region **reduction rule** — the L3 wiring's own mapping choice, which we explicitly
left `(a)/(b)/(c)` as alternatives in the wiring dossier:
- Build a variant with intra-region rule **(a) start-slice** (decode unchanged; only the per-region reduction
  differs) and measure the **BIR case-identity on Jazz AND Baroque AND Default** vs the ratified **(b)
  duration-majority**.
  - If **(a)** brings Jazz net-non-increasing, introduces **no** new class-(b) on any preset, and does **not**
    net-increase Baroque/Default → a *legitimate* finding (a principled mapping rule, not a gate hack). Surface it
    for re-ratification of the intra-region rule (we ratified (b); this revisits it with data).
  - If **(a)** harms Baroque/Default or introduces any class-(b) → reject; **(b)** stays.
- Diagnose whether the two new Jazz cases are a **duration-majority collapse artifact** (a within-region modulation
  averaged out by (b)) or an **emission-level rotation** the mapping cannot touch.
- Do **NOT** explore decoder-knob / preset-conditioning / scorer / gate changes — out of scope (exhausted / new
  architecture / the gate-weakening path you ruled out).

## §3 — Verdict (the decision input for "then we will see")
State plainly, with the measurements: is the Jazz +1 **avoidable** within the proper layers without weakening the
gate — and if so by which mapping rule and at what cost to Baroque/Default — **or irreducible class-(a) churn at
Layer 3** (the rotation coin-flip the pitch-class pipeline cannot stabilize; resolvable only at Layer 4 / the
spelling-aware gate, or by the guardrail-(B) refinement we deferred)? Do not pick the path — report the evidence;
Cowork + user decide.

## §4 — Deliverable + stop conditions
- Deliver `cc_layer3_jazz_churn_investigation.md` (held/gitignored): §1 per-case re-verification, §2 (a)-vs-(b)
  measurement on all three presets, §3 verdict.
- **STOP and surface** if: any new Jazz (or other-preset) case is not provably class-(a); rule (a) would help Jazz
  but hurt Baroque/Default (report, don't adopt); or you find yourself reaching for a decoder/scorer/gate change.
- No commit, no push, `upstream` untouched. Working tree stays held (Step-2 reverted, Step-1 wiring uncommitted).
