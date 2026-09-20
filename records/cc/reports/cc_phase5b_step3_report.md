# CC — Phase 5b Step 3: G6 — confidence model + open-question label (the L4→L5 abstain contract)

**Commit (local, unpushed, decoder + tests only — verifiable by sha):** `c74fe98ff5`
`feat(composing): L4 G6 — confidence model + open-question label (L4→L5 abstain contract) (Phase-5b Step 3, dormant)`

`git show --stat` lists exactly three files — `chordslicedecoder.cpp`, `chordslicedecoder.h`, `decode_chord_tests.cpp`.
No production wiring; `tools/batch_analyze.cpp` is **untouched** (0 diff). (The working-tree
`cowork_phase5b_l4_build_plan.md` change is the Step-0 grounded-order doc edit — *not mine*, left uncommitted;
`scratch_artifacts/` is gitignored.)

**Method (the instruction's spine):** §1 INVESTIGATE-confirm → §2 BUILD G6 (dormant) → §3 RE-MEASURE → §4 GATE →
§5 ASSESS. Build-it-right per the signed spec (`cowork_layer4_chordsymbol_design.md` §7/§8/§12/§15-O1); **no
threshold/inference tuning** (the firewall — Phase B owns calibration). `upstream` untouched.

---

## TL;DR — G6 is REPRESENTATIONAL (the decision is unchanged); built, accuracy-neutral, contract populated → proceed to Step 4

1. **§1 — the confidence model is a richer VALUE, NOT a decision change.** The spec's commit/abstain boundary
   ("uncertain when low margin **OR** low sufficiency") is **already** the as-built G1 decision: `applyCommitDecision`
   commits only when `sufficient && marginOk` — two **independent** gates (sufficiency = `templateTonePresenceCount ≥
   sufficiencyChordTones`; margin = `!uncertain`). So the spec's **composite confidence** (margin × sufficiency ×
   membership cleanliness) is carried **alongside** the same decision; building it does **not** move the commit/abstain
   boundary. The open-question representation (competing readings + ambiguity kind) is fully derivable from the
   decoder's existing ranked candidates + margins. The L4→L5 contract is **forward/additive** — L4 *declares* the open
   question, L5 *resolves* it. **No L5 / no structural change beyond the decoder → no §1 STOP.**
2. **§2 — built dormant in `chordslicedecoder`.** `SliceConfidence{margin, sufficiency, membershipCleanliness,
   composite=min(…)}` (the "low for EITHER reason" MIN — a wide margin does NOT rescue an insufficient slice) +
   `OpenQuestionLabel{question(Root/Quality/None), ambiguity(ShareTone/RelativePair/SymmetricRotation/Transition/
   Insufficient/Close), readingA, readingB}`. Populated by `applyCommitDecision` AFTER the decision is settled. **One
   `analyzeChord` cube; no new scorer; no new accuracy parameter** (marginCertainty reuses the existing
   `uncertaintyMargin` scale).
3. **§3 — accuracy-neutral, confirmed by byte-identical decode output.** G6 reads/writes only NEW fields; the decode
   JSON (which `batch_analyze --decode-chords` emits from the *unchanged* fields) is content-identical to Step-2-final,
   so the grader metrics are **unchanged**: coverage-matched **68.0 % Baroque / 67.7 % Default**, abstain **58.2 %**,
   among-committed **77.8 %**. Open-question label populated on abstained slices — the **share-tone (Am6↔F♯ø7)**
   spot-check is an oracle-asserted unit test that **names both competing readings + the ShareTone ambiguity**.
4. **§4 — GATE PASSED.** Production **byte-identical** (decoder production-dead; `batch_analyze.cpp` 0-diff; snapshots
   **11/11** zero-diff, no goldens refreshed → corpus **53/24/53** holds by construction). Both suites green: composing
   **854** (+10 G6 tests), notation **53**. New G6 unit tests (+10) all green.
5. **§5 — ASSESS: proceed to Step 4 (spelling-pin, G4).** The confidence/open-question representation is built, the
   committed accuracy holds (representational), and the L4→L5 contract is populated on abstains. No regression, no
   threshold tuning, no L5 dependency. → Step 4.

---

## §1 — INVESTIGATE-confirm (read-only): the spec's G6 against the as-built decoder

Read the spec's G6 surface — §4 step 3 (commit/inherit/**abstain**), §5 step 4 (the two certainty conditions), §7
(data design: the composite confidence + the open-question label), §8 (certainty is part of the output), §12 (glossary:
Confidence, Uncertain), §15-O1 (the residual classes) — against `chordslicedecoder.{h,cpp}` as built at HEAD
(`4aa88452cd`, Step-2-final).

### (a) The confidence model — does it change the DECISION, or is it a richer VALUE? → **richer VALUE (representational)**

- **As built**: `decideSlice` sets `confidence = chosen − best-different (margin)` and `uncertain = confidence <
  uncertaintyMargin` (**margin-only**). The G1 decision (`applyCommitDecision`) commits only when `sufficient &&
  marginOk`, where `sufficient = templateTonePresenceCount(chosen, focal) ≥ sufficiencyChordTones` and `marginOk =
  !uncertain`. These are **two independent gates**.
- **Spec §7**: "the confidence … combining the **margin**, the **sufficiency**, and the **membership cleanliness**. A
  slice is 'uncertain' when confidence is low for **either** reason — low margin **or** low sufficiency; these are
  independent, and a wide margin does not rescue an insufficient slice."
- **The finding**: the spec's confidence-driven uncertainty boundary (**low margin OR low sufficiency**) is **already
  the as-built G1 decision** — commit ⟺ (sufficiency-clear AND margin-clear); else inherit (a certain answer) or
  abstain (uncertain). So the spec's **composite confidence is a richer VALUE carried alongside the SAME decision** —
  *representational*. Building it does **not** change the commit/abstain boundary (which is the G1 sufficiency + margin
  gates, already built and firewall-frozen). Membership cleanliness is a **third** confidence input the spec folds into
  the *value*; G1 does not gate on it, so it too is representational. **Verdict: representational — build it as a richer
  value; keep the decision exactly where G1 put it.**

### (b) The open-question representation — does the decoder already have what L5 needs? → **yes**

- Spec (§4 step 3 / §6 / §7 / §12): on an abstain, carry the **competing readings**, **name the open question** (root /
  quality / a note's membership), and the **kind of ambiguity** (the §15-O1 residual classes: share-tone pc-identical
  chords like Am6↔F♯ø7; symmetric rotations; relative pairs; the function-dependent residual).
- **As built the decoder already has**: the ranked candidate list (`chosen` + `alternatives`, ∪ the prevailing chord),
  the margin to the best different reading, the per-note membership split, and the abstain *reason* (insufficient vs
  sufficient-low-margin, and — from the two-reading inherit — continuation vs transition). Every input the open-question
  label needs is local. The competing readings are already carried; only the **named question + ambiguity kind** are
  unbuilt. **Confirmed populatable from the decoder alone.**

### (c) The L4→L5 contract shape — forward/additive, L4 declares, L5 resolves → **confirmed, no STOP**

- The label is a **forward, additive** interface: L4 *declares* uncertainty and *names* what is open; L5 (function)
  *resolves* it by selecting among the carried readings (spec §8 forward-only resolution; §15-O1 the resolver IS Layer
  5). G6 must **not** itself resolve the open question — and it does not (no progression grammar, no chord-to-chord
  transition cost; the ambiguity kind is derived from the two readings' pitch-class structure + the abstain reason
  only). **No L5, no structural change beyond the decoder → no §1 STOP.**

## §2 — BUILD G6 (in `chordslicedecoder`, dormant)

**`SliceConfidence` (the composite confidence MODEL, §7):**
- `margin` = the raw margin (== `SliceChord.confidence`).
- `sufficiency` = `present / required` template tones of the chosen chord, clamped [0,1] (a full seventh → 1.0; a dyad
  of a triad → 0.67; a lone tone → 0.33). `required` is read off the one source `kTemplateIntervals` (no new table).
- `membershipCleanliness` = the chord-tone fraction of the focal pitch classes (few contested notes vs many), [0,1].
- `composite = min(marginCertainty, sufficiency, membershipCleanliness)` — the **MIN** is the spec's "low for EITHER
  reason" property: a wide margin cannot rescue an insufficient slice, nor a clean membership a low margin.
  `marginCertainty = clamp(margin / (2·uncertaintyMargin), 0, 1)` — reuses the **existing** `uncertaintyMargin` (at the
  decision boundary → 0.5; at 2× → 1.0; the no-competitor sentinel → 1.0). **No new accuracy parameter.**

**`OpenQuestionLabel` (the named open question, §7/§12/§15-O1):**
- `question ∈ {None, Root, Quality, NoteMembership}` — `None` on commit/inherit; on abstain, `Quality` when the two
  readings share a root and differ in quality (C vs C7; passing-dim vs applied), else `Root`. `NoteMembership` is a
  reserved forward value (not populated this increment).
- `ambiguity ∈ {None, InsufficientEvidence, TransitionVsContinuation, SymmetricRotation, ShareTone, RelativePair,
  CloseReading}` — derived locally from the chosen vs the best-different reading + the abstain reason: thin-slice
  transition (next provisional ≠ prevailing) → Transition; thin-slice no-continuation → Insufficient; augmented
  rotations → SymmetricRotation; same focal pitch-class collection (Am6↔F♯ø7) → ShareTone; roots a minor third apart
  major↔minor (C↔Am) → RelativePair; else → CloseReading.
- `readingA` = the chosen/top reading, `readingB` = the best DIFFERENT carried reading (`hasReadingB`) — the two
  readings in tension are **named**, not merely listed (the full ranked list stays on `alternatives`).

**Wiring:** `applyCommitDecision` calls a new `populateForwardContract` AFTER the decision is settled (every exit path),
reading the FINAL chosen chord. The trichotomy (commit/inherit/abstain) and every existing field are **unchanged**;
only the new `confidenceModel` + `openQuestion` are written. **One `analyzeChord` cube; representation/decision wiring,
not a new scorer.**

## §3 — RE-MEASURE (the assess checkpoint, per the CORRECTED gate)

G6 reads only the FINAL chosen chord and writes only NEW fields; the decode JSON `batch_analyze --decode-chords` emits
is built from the *unchanged* `SliceChord` fields (`chosen`, `confidence`, `uncertain`, `hasChord`, `alternatives`,
`chordTonePcs`, `nonChordTonePcs`) — and `batch_analyze.cpp` is **untouched**. So the decoder's chord output is
**content-identical** to Step-2-final, and the held-out chord-root grader reads identical input → **identical metrics**.

**Decode-output byte-identity (content), fresh G6 binary vs the committed Step-2-final decode artifacts:**

| | stems compared | content mismatches |
|---|---|---|
| Baroque | 353 | 0 |
| Default | 353 | 0 |

(Compared as parsed JSON objects — the raw `batch_analyze` stdout is compact, the Step-2-final artifacts are
`json.dumps(indent=2)` pretty-printed, so a literal `cmp` differs on whitespace only; the **content** is identical.)

**Coverage-matched accuracy + abstain, before(Step-2-final) → after(G6) — UNCHANGED (representational):**

| variant | among-committed | abstain | coverage-matched |
|---|---|---|---|
| Step-2-final two-reading (Baroque) | 77.8 % | 58.2 % | 68.0 % |
| **G6 (Baroque)** | **77.8 %** | **58.2 %** | **68.0 %** |
| Step-2-final two-reading (Default) | 77.8 % | 58.2 % | 67.7 % |
| **G6 (Default)** | **77.8 %** | **58.2 %** | **67.7 %** |

G6 is **accuracy-neutral by construction** — the open-question label is representational; the confidence model is a
richer value that does not change the committed accuracy. (As expected by the plan: "G6 to be accuracy-neutral-or-better
… the confidence model should not regress committed accuracy.")

**Open-question label populated on abstained slices — the §4 spot-check.** The share-tone abstain spot-check is an
oracle-asserted unit test (`G6_ShareToneAbstain_NamesBothReadingsAndAmbiguity`): an **Am6 ↔ F♯ø7** (same four pitch
classes) low-margin abstain carries **both** competing readings (`readingA` = F♯ø7, `readingB` = Am) **and** the
**ShareTone** ambiguity kind, `question = Root`. A relative-pair (C↔Am) abstain names **RelativePair** (distinct from a
same-collection share-tone); a thin transition slice names **TransitionVsContinuation**; a phantom-root thin slice names
**InsufficientEvidence**.

## §4 — Gate (all PASSED)

- **Production byte-identical.** The decoder is production-dead (referenced only by `batch_analyze --decode-chords`,
  which returns before `analyzeScore`); `batch_analyze.cpp` is 0-diff; only NEW `SliceChord` fields are added.
  **Snapshots 11/11 zero-diff** (no goldens refreshed) → P1–P4 production output unchanged → **corpus 53/24/53 holds by
  construction** (the decoder never reaches the production analyzer; the same production-dead, preset-agnostic argument
  the prior increments used).
- **Both suites green.** Composing **854** (+10 G6 tests over Step-2-final's 844), notation **53**.
- **New unit tests (+10, oracle-asserted).** Confidence model: clear slice → composite ≈ 1; low margin → low composite;
  **wide margin does NOT rescue insufficiency** (the spec invariant — composite tracks the MIN); contested membership
  lowers composite. Open-question: commit → None/None; **share-tone Am6↔F♯ø7 → both readings + ShareTone**; relative
  pair C↔Am → RelativePair; transition → Transition; insufficient → InsufficientEvidence; determinism.
- **Build green** (no new warnings beyond the pre-existing two).

## §5 — ASSESS (proceed to Step 4)

- **Expected (instruction §5):** the confidence/open-question representation is built, coverage-matched accuracy
  holds-or-improves, the L4→L5 contract is populated on abstains → proceed to **Step 4 (spelling-pin, G4)**.
- **Measured:** all three hold. The representation is built dormant; committed accuracy is **unchanged** (68.0 % / 67.7
  % coverage-matched, byte-identical decode output); the open-question label is populated on every abstained slice and
  names both readings + the ambiguity kind (oracle-tested on the share-tone residual). **No committed-accuracy
  regression; no threshold tuning needed; no L5 dependency** → none of the §5/§7 STOP conditions tripped.
- **→ Proceed to Step 4 (spelling-pin, G4).**

## §6 — Deliver

- **Commit** `c74fe98ff5` — local, unpushed, **decoder + tests only** (`git show --stat`: exactly `chordslicedecoder.cpp`,
  `chordslicedecoder.h`, `decode_chord_tests.cpp`).
- This report (`cc_phase5b_step3_report.md`, gitignored).

## §7 — Stops honored

- The confidence/open-question needed **no** L5 to populate and **no** structure beyond the decoder → no §1 STOP.
- **No production movement** (decoder dead; `batch_analyze.cpp` 0-diff; snapshots 11/11; corpus 53/24/53 by
  construction; decode output content-identical to Step-2-final) → no leak STOP.
- **No threshold/inference tuning** — the confidence model reuses the existing `uncertaintyMargin`; the decision is
  unchanged (the firewall held).
- No `upstream` push; the commit is local, unpushed, decoder + tests only.

## Artifacts (gitignored / untracked, under `scratch_artifacts/`)

- G6 decode: `corpus_decode_chord_g6/{baroque,default}` (fresh G6 binary); content-compared vs
  `corpus_decode_chord_step2final_B/{baroque,default}` (Step-2-final committed artifacts).
- Build/tests: `/c/tmp/g6_build.log`, `g6_composing.log` (854), `g6_notation.log` (53), `g6_snap.log` (11/11),
  `g6_decode.log` (the 49 DecodeChord tests incl. the 10 new G6 tests).
