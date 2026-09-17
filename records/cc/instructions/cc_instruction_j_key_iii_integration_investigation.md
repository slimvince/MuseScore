# CC Instruction — J-key-iii (Step 1): the WIRING integration investigation (READ-ONLY)

> **Ratification-gated, READ-ONLY, no code change.** The user ratified **wiring J-key-i's soft
> constrained-joint key decision into production** (2026-06-15, "max correct inferring first"). The decision
> has been **diagnostic-only** throughout (`decideJointKey` is called only from the `--dump-joint-key` tools
> path) — the production integration point has never been exercised. Per never-guess / measure-before-wire,
> Step 1 **characterizes the integration at source and produces the concrete wiring design**, ahead of the
> wiring (Step 2). **No code is written in this step.**

---

## §1 — What this is

J-key-i proved the soft decision beats production (+3.80/+3.50/+12.24 pp; S2 −140/−96/−1706) and stands.
J-key-iii **wires it**: the production resolved key adopts the joint decision, which then feeds `basisIndep`
(chord emission) and the rendered Roman numerals — so byte-identity ends on **both** axes and this is the
**first intentional production behavior change on the key axis**. Before writing that wiring, this step
answers, **at source, read-only**, exactly *where* and *how* the joint decision plugs into production, what
it must produce, what consumes it, and whether the substitution is clean feed-forward. Output: a dossier
that **is** the Step-2 wiring spec.

## §2 — Scope

**Read-only.** Source characterization across `src/composing/` (the resolver, KeyArea, basisIndep) and
`src/notation` (the harmonic-rhythm bridge / RN rendering) — **reading only**. **No edits, no wiring, no
build needed** (a build only if a claim genuinely requires compiling a probe — prefer source reading). The
producer (`jointkeydecision.{h,cpp}`) and all production paths stay untouched; HEAD unchanged.

## §3 — The questions to answer at source

1. **The production key-resolution pipeline + call order.** Map the feed-forward path: where the
   `analyzeKeyMode` local candidates are produced → where the key is *resolved* (`keyresolver.cpp`) → where
   `KeyArea` is built → where `basisIndep` consumes the resolved key for chord emission → where the notation
   bridge renders the RN. Establish the exact order and the data each stage hands the next.
2. **The plug-in point.** Where does `decideJointKey`'s per-region `(tonicPc, isMajor)` decision *substitute*
   the production resolved key? Identify the single cleanest substitution point (replace the resolver's
   output vs override it post-hoc). State which.
3. **The representation gap.** The joint decision emits per-region `(tonicPc, isMajor)` (+ anchor, span
   count, structural flags). The production consumers expect a richer structure (`KeyModeAnalysisResult` /
   `KeyArea` spans / a **confidence**, the hysteresis state, etc.). Enumerate **exactly what each consumer
   reads** and **what the joint decision does NOT currently supply** (e.g. per-region confidence for
   `basisIndep` gating, KeyArea span boundaries). This gap list is the core of the Step-2 design.
4. **Circularity / feed-forward proof.** Confirm the joint decision's inputs — `analyzeKeyMode` candidates,
   the key-agnostic cadence/modulation instruments, the notated signature — are **all computed BEFORE**
   resolution, and that **no consumer of the resolved key feeds back** into those inputs. The substitution
   must be a clean feed-forward replacement (the J-key-i §10 echo-only property must survive wiring). If any
   feedback path exists → STOP and surface (the wiring is not safe as-is).
5. **Hysteresis disposition.** J-key-i's decision is a **global key-path Viterbi** that *replaces* the
   production note-based hysteresis (`keyresolver.cpp:323-345` — the documented "must NOT touch" trap) and
   the `relativeKeyHysteresisMargin` anchor. Characterize what wiring the Viterbi means for the hysteresis:
   clean replacement, or must they coexist? What breaks if the hysteresis is removed?
6. **The behavior-change surface (sizing).** Predict which production outputs move: key-axis S2 (↓ expected,
   the win), chord-axis `.ours.json` where the resolved key shifts (feeds `basisIndep`), the **BIR gate**
   (may move on all 3 presets — the CLAUDE.md hard-stop axis), and the snapshot goldens. Estimate the
   magnitude (roughly how many `.ours.json` change) from the J-key-i diagnostic delta.
7. **The tail residual.** Confirm the 56 partial-signature stems remain at the signature reading under the
   wired decision (the documented, ratified residual — not a regression vs production).

## §4 — Output: the concrete wiring design (dossier, no code)

Write `cc_j_key_iii_integration_dossier.md` (gitignored, HELD): the plug-in point, the consumer/
representation-gap list, the circularity proof, the hysteresis disposition, the predicted behavior-change
surface + sizing, and the tail confirmation. Frame it as the **Step-2 wiring spec** — concrete enough that
the wiring instruction can be written from it. Recommend the cleanest staging for Step 2 (wire → measure the
production delta on both axes → DCML-adjudicate every moved BIR/snapshot case → HELD for ratification →
commit only on a clean adjudication; un-adjudicated BIR=false increase on any preset = hard stop).

## §5 — Stop conditions
- **Any code change / wiring in this step** (it is read-only) → STOP.
- **A circularity / feedback path** is found (the substitution is not clean feed-forward) → STOP, surface
  (the wiring needs a redesign before proceeding).
- **A consumer needs information the joint decision cannot supply** and no clean mapping exists → surface it
  as a design gap (do not invent a value).
- Uncertain about a pipeline edge (order, what a consumer reads) → read the source and cite file:line; if
  still unresolved, surface it — never guess the integration.
