# CC Instruction — B: #4 dominant/subdominant guard — SCOPING investigation (READ-ONLY)

> **Ratified (user, 2026-06-15): option B.** The J-key-iii global flip-ON regressed 3/8 non-chorale snapshot
> scores by over-committing to the **subdominant/dominant** (mozart_k279 C→F, bwv806 A→D, corelli i→v) — the
> known **I→IV / I→V tonicization-read-as-modulation** failure = the deferred 4c **"#4 dominant/subdominant
> guard"** (4d-i: ~43% of modulation-detector FPs). This step **characterizes the over-detection at source
> and sizes the guard's discriminator** — read-only, measure-first — BEFORE any guard is built. It unblocks
> the global flip-ON and is convergent with in-scope Bach modulation precision. **No code change.**

---

## §1 — What this is

The non-chorale regressions are a key decision over-committing to IV/V because the cadence/modulation soft
evidence reads a brief **I→IV or I→V tonicization** as a sustained **modulation to IV/V**, committing a span
that becomes a lattice state the Viterbi picks. The fix is the deferred **#4 guard**: a discriminator that
distinguishes a *tonicization* (stay home) from a genuine *modulation to the subdominant/dominant*. Before
building it, **measure whether that discriminator is separable** (the same measure-first gate that the
partial-sig redux applied) — does a signal cleanly separate the 3 regressing over-commitments from the
genuine modulations, WITHOUT breaking the Bach modulation-detector precision the win relies on.

## §2 — Scope

**Read-only.** Source characterization in `src/composing/analysis/section/` (the cadence anchor +
`localmodulationdetector`) + measurement in `tools/`. **No edits to the instruments; no guard built; no
wiring change.** HEAD unchanged. (A build only if a probe genuinely needs it; prefer source reading + the
existing `--dump-modulation` / `--dump-joint-key` diagnostics.)

## §3 — The questions to answer at source + by measurement

1. **Locate the over-detection.** At source, find where `detectLocalModulations` (and/or the cadence anchor)
   commits a span to IV/V on the 3 regression scores — is it the cadence anchor naming IV/V as the local
   tonic (the V→IV/subdominant over-detection, J-key-i §10.5), or the modulation detector's span-commitment
   threshold, or both? Cite the mechanism at `file:line`. Confirm it via the `--dump-modulation` /
   `--dump-joint-key` dumps on mozart_k279_1 / bwv806_gigue / corelli_op01n08a (the IV/V span that flips the
   key).
2. **Characterize the discriminator.** A genuine modulation to IV/V has **sustained establishment in the new
   key + a cadence IN it**; a tonicization is **brief / passing**. Identify the key-agnostic signals already
   available (span length, cadence-in-target, return-to-home, the relative-strength of the home cadence vs
   the IV/V cadence) that could separate the two.
3. **Measure separability (the load-bearing gate).** On a labeled set — the 3 non-chorale over-commits (must
   be SUPPRESSED) vs the genuine modulations in the Bach corpus the win relies on (must be KEPT) — sweep the
   candidate discriminator and report recall (genuine modulations kept) vs false-suppression (does the guard
   wrongly kill real Bach modulations). **If no threshold separates them, STOP and surface** (the guard
   can't be made safe — same stop as the partial-sig redux).
4. **Convergence check.** Confirm the guard helps the **in-scope** work too: does suppressing the I→IV/I→V
   misreads raise the 4d-i modulation-detector precision (~47%) without lowering its recall on genuine Bach
   modulations? (Convergent ⇒ B is architecture-quality precision work, not a non-chorale-only patch.)

## §4 — Output: the guard design (dossier, no code)

Write `cc_b_guard_scoping_dossier.md` (gitignored, HELD): the over-detection mechanism (cited at source),
the discriminator characterization, the **separability measurement** (does a safe threshold exist?), the
convergence result, and — if separable — the concrete **#4 guard design** (where it sits, the signal, the
provisional threshold `[empirical — Stage-5 fits]`) framed as the next build instruction's spec. If NOT
separable, surface that the subdominant/dominant generalization is itself a calibration/learned-evidence
problem (the recurring precision wall) for a Cowork/user direction call.

## §5 — Stop conditions
- Any code change / guard built / wiring change in this step (read-only) → STOP.
- No threshold separates the over-commits from genuine modulations → STOP, surface (guard not safely
  buildable on current signals).
- The guard would suppress genuine Bach modulations (breaks the in-scope win) → STOP, surface the trade-off.
- Uncertain about a mechanism → read the source and cite `file:line`; if unresolved, surface — never guess.
