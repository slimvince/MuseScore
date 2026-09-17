# CC — Layer 3 wiring: Jazz net +1 churn INVESTIGATION (read-only)

**Status: READ-ONLY investigation, HELD / gitignored (`/cc_*.md`). No commit, no push, no golden refresh, no gate
edit, no decoder-knob / scorer change.** Step 2 reverted (per the prior decision); the working tree is the **faithful
Step-1-only (b)-rule wiring**, uncommitted. Built at HEAD `2203ad9fda`; all corpora stamped `git 2203ad9fda`.

**Question (Decision A, conservative gate kept strict):** guardrail (3) = *net BIR=false non-increasing on EVERY
preset*. Step-1 passes Baroque (53, −4) and Default (53, −4) but **Jazz nets +1 (24 vs gate 23)**. Is the Jazz +1
**avoidable within the proper L3 layers without weakening the gate** — specifically via the one in-scope lever, the
slice→region **reduction rule (a)/(b)** — or is it **irreducible class-(a) churn at Layer 3**?

**ANSWER: irreducible class-(a) churn at Layer 3.** The reduction rule (a) start-slice yields a BIR case-identity set
**byte-identical to (b) duration-majority on all three presets** — it does not touch the churn. Both new Jazz cases are
verified class-(a) at the score, each on a **single-key region** (so reduction-rule-invariant by construction), each
needing a **higher layer** (function/cadence) to resolve. No class-(b) regression exists.

---

## §0 — Step-2 reverted; baseline confirmed
- Shared scorer at baseline: `scaleScoreInKeySigOnly = -0.20`, `scaleScoreInNeither = -0.05`
  (`keymodeanalyzer.h:193-194`); **0** decode-only reweight residue in `regionanalyzer.cpp`; `decode()` called with the
  un-modified caller `keyPrefs`. Working tree = **Step-1-only (b)-rule wiring**.
- (b)-rule corpora regenerated with the reverted binary: **Baroque 53 / Jazz 24 / Default 53** — byte-matching the
  original Step-1-only run ⇒ the Step-2 revert is clean (byte-identical to the pre-Step-2 wiring).

## §1 — Jazz churn cases re-verified at the score (independent, post-revert)
Jazz (b) = 24. Delta vs the ratified gate baseline (23):
- **2 NEW** (vs gate-23): `bwv272@4320`, `bwv291@17760`
- **1 FIXED** (in gate-23, gone): `bwv244.15@10080`
- net **+1** (2 new − 1 fixed).

Each NEW case re-verified by an **independent music21 parse of the raw score** (`tools/corpus/{stem}.xml`) — the
sounding pitch classes over the GT region span, NOT the prior classification:

| case | GT (music21/DCML) | OUR | sounding pcs (independent) | structure | both roots ∈ set? | class |
|---|---|---|---|---|---|---|
| `bwv272@4320` | G#°7 = #iv° (root pc 8), d minor, span [4320,4800) | B°7/D (root pc 11) | `{D,F,Ab,B}` | interval cycle **[3,3,3,3] = symmetric fully-dim7** (4-way root coin-flip) | yes (Ab ✓, B ✓) | **(a)** symmetric dim7 rotation |
| `bwv291@17760` | Eø7 = viiø (root pc 4), F major, span [17760,**18000**) | Gm6/Db (root pc 7), span [17760,**19200**) | `{D,E,G,Bb}` over the GT span | **Eø7 ≡ Gm6** half-dim/m6 share-tone tetrad | yes (E ✓, G ✓) | **(a)** share-tone rotation |

**Both NEW Jazz cases are provably class-(a). No class-(b) (genuine functional key/root) regression → no §1 STOP.**
(`bwv272@4320` has the *same* span as GT — a pure rotation. `bwv291@17760` has a *wider* span than GT — a collapse
candidate examined in §2.)

## §2 — Avoidability: reduction rule (a) start-slice vs (b) duration-majority (all 3 presets)
Built a variant changing ONLY the per-region reduction (decode unchanged): rule **(a)** = the decoder key of the slice
covering `regionStart` (vs ratified **(b)** = duration-majority over the region's slice run). Rebuilt; regenerated all
three corpora; measured BIR case-identity.

| preset | (b) total / new-vs-gate | (a) total / new-vs-gate | (a) Δ vs (b) |
|---|---|---|---|
| Baroque | 53 / {bwv272@4320, bwv289@20160} | 53 / (same) | **0 cases differ** |
| Jazz | 24 / {bwv272@4320, bwv291@17760} | 24 / (same) | **0 cases differ** |
| Default | 53 / {bwv272@4320, bwv289@20160, bwv387@10560} | 53 / (same) | **0 cases differ** |

**Rule (a) ≡ rule (b) on BIR case-identity, byte-for-byte, on every preset** (`comm` of the sorted case sets: empty in
both directions). The slice→region reduction rule is **inert** on the churn — it neither helps Jazz nor harms
Baroque/Default. The Jazz +1 is therefore **not** a duration-majority collapse artifact.

### Why (a) ≡ (b): the churn regions are single-key (decoder probe, `--decode-keymode --preset Jazz`)
- `bwv272@4320`: **one** decoder slice `[4320,4800)` key **A min** → start-slice == duration-majority trivially. The
  `{D,F,Ab,B}` symmetric dim7 is a 4-way root coin-flip; with one slice the reduction rule cannot change the key, and
  the rotation is determined by (key + the symmetric chord) — emission/function-level, not mapping-level.
- `bwv291@17760`: **six** decoder slices `[17760,19200)`, **all G Dorian** → single-key run ⇒ (a)==(b). Crucially
  **G Dorian ≡ F major are the SAME collection, different center**; so `{E,G,Bb,D}` roots as **Gm6 (Dorian i6)** under
  the decoder's G-Dorian center vs **Eø7 (viiø)** under GT's F-major center. The root disagreement flows from a
  **same-collection modal-CENTER** disagreement — exactly the sweep's **L5 modal-rotation residual**
  (`cc_layer3_sweep_report.md` §3 Finding 4), which needs cadence/function, not a key-signature or scale-weight change.

### Diagnosis: collapse-artifact vs emission/center rotation
Neither new Jazz case is a reduction-rule-fixable collapse. `bwv272@4320` is a pure **symmetric-dim7 rotation** on a
single slice. `bwv291@17760`'s wider span is a **segmentation** (Pass-2/2b) effect, but the region key is single-valued
(G Dorian) regardless of (a)/(b), so the reduction rule cannot reach it; the root churn is a **same-collection center**
pick (L5). Both are mapping-invariant.

## §3 — VERDICT (decision input)
**The Jazz net +1 is NOT avoidable within the proper L3 layers without weakening the gate.** The single in-scope lever
— the slice→region reduction rule — is byte-identical (a)-vs-(b) on all three presets, so it cannot remove the Jazz
churn (nor does it cost Baroque/Default anything). The churn is **irreducible class-(a) rotation at Layer 3**:
1. `bwv272@4320` — a **symmetric fully-diminished-7th** root coin-flip (root pitch-class undefined by construction; the
   CLAUDE.md "structurally unresolvable" class). Resolvable only by **function** (which rotation is vii°/#iv°) — Layer 4
   — or a **spelling-aware / guardrail-(B) gate** refinement.
2. `bwv291@17760` — a **same-collection modal-center** rotation (G Dorian ≡ F major), the sweep's L5 residual.
   Resolvable only by **cadence/function** to pin the tonal center — Layer 4/L5 — not by L3 key/scale machinery.

The other in-scope-but-ruled-out levers confirm this: decoder-private knobs are ratified-exhausted (sweep §2 plateau);
Step 2 (scale-contrast) is key-orthogonal to both a symmetric dim7 and a same-collection center (and was BIR-flat);
preset-conditioning the decoder is new architecture; weakening the gate is the path Decision A rejected.

**Bottom line for "then we will see":** the Jazz +1 cannot be cleared at Layer 3 without weakening the gate or leaving
the proper layers. It is irreducible class-(a) churn whose true fix lives at **Layer 4 (function/cadence)** or in the
**deferred guardrail-(B) / spelling-aware gate refinement**. The decision (accept the +1 as documented class-(a) under a
guardrail-(B) refinement, or hold Step-1 wiring until L4 can pin these rotations) is Cowork's + the user's — this report
supplies the evidence, not the choice.

## §4 — State / compliance
- Working tree restored to ratified **(b) duration-majority** (the §2 (a)-variant reverted; rebuilt). Step-1-only
  wiring, **uncommitted**. Goldens git-clean; nothing staged.
- No gate edit, no decoder-knob/scorer/Step-2 change adopted; the (a)-variant was a transient measurement, reverted.
- `upstream` untouched; nothing pushed.
- Deliverable: this file (`cc_layer3_jazz_churn_investigation.md`, held/gitignored).
