# Where can the true key be lost? — the layer-3 key-decode mechanism, pinned at the code (OI-141)

> **Status: READ-ONLY MECHANISM MAP (CC, 2026-07-12).** Executes
> `cc_instruction_l3_key_decode_mechanism.md` against the grounding
> `cowork_key_drift_research_grounding.md`. No `src/` change, no constant tuned, no
> golden refresh; `tools/robust_stop/` and `tools/corpus/` written by NOTHING (only
> read-only diagnostics into a session scratch dir). Explorational, open-book: findings
> are pinned at file-and-line, verified fresh at the code and the data — including
> against the audit reports' own assertions (#15/#19). The mechanism is MAPPED; no fix
> and no design are proposed (guiding principles 7 and 8).
>
> **Provenance / reproducibility (#16).** HEAD `cfcb5cceea` (the Task-0 register commit).
> Corpus `c50002fee1` (pinned, 352 XMLs). Diagnostics: the committed default-OFF
> `batch_analyze --decode-keymode` (+ the read-only `--seq-max-alts` bounded-sweep
> override, decode-keymode path only, production byte-identical) and `--dump-key-candidates`,
> run from the HEAD binary (built 2026-07-12); both RETURN before `analyzeScore`, so
> production output is untouched. All numbers below come from those dumps; nothing was
> hand-transcribed from another document.

---

## §0 — The answer in one paragraph

The literature's decoders (Temperley) run a full 24-key lattice, so a key can only be
outranked, never dropped from search. **Our live layer-3 decoder does NOT do that.** Its
per-slice EMISSION scores all 252 (tonic × mode) states, but the whole-sequence Viterbi
runs over a **pruned lattice — the global union of each slice's emission top-8** (`topK = 8`).
A (tonic, mode) state that is never in any slice's top-8 emission is **not a lattice state
at all** and can never be decoded, carried, or recovered. So there **is** a search-level
prune — at the emission→lattice boundary, not inside the Viterbi (which is exhaustive and
global over its state set). Downstream of the decode there is **no** greedy or
hysteresis-gated key commit (the greedy step is segmentation, not key; the only post-decode
key override is env-gated OFF); the region key is a deterministic duration-majority reduction
of the global Viterbi, and the carry (`keyAlternatives`) is a truncation of it. Re-tracing
three failures at the decoder's own numbers, the true key is lost at **two earlier points,
not at the carry**: (1) the **emission scoring + its narrow ±4-beat window** — the true key
is ranked below the local winner (`bwv369`: true key emission #7, wrong key #1) or buried
so deep it never enters the lattice at all (`bwv226.2`: true key emission #116, absent from
the 27-state lattice); and (2) the **single hand-set change cost** — over a non-discriminating
emission the Viterbi commits to a wrong coherent run (`bwv110.7`: a cadential dominant span
read as its own key, "a fifth off"). The lattice top-8 prune and the carry cap are real but
**secondary** — they only remove keys the emission has already failed to rank. **This
corrects the diagnosis report's "drops off the beam" phrasing: none of the three is a
carried-list beam drop.**

---

## §1 — The mechanism map (Task 1)

The live key path is one whole-score decode wired at `region/regionanalyzer.cpp:632-636`:
`changePointSlices(noteModel)` → `KeyModeSequenceDecoder::decode(slices, noteModel,
keySigCtx.correctedFifths, keySigCtx.declaredMode, keyPrefs, kDefaultKeyModeSequencePreferences,
excludeStaves)`. The stages below are that call's internals.

### 1.1 Emission — all 252 states scored, no pruning (where the candidate set is formed)

Per slice, `KeyModeAnalyzer::analyzeKeyMode` scores **every** (tonic × mode) candidate:
- The candidate set is `12 tonics × ACTIVE_MODE_INDICES` where `ACTIVE_MODE_INDICES` is
  **all 21 modes** (`key/keymodeanalyzer.cpp:71-75`), so **252 states**
  (`keymodeanalyzer.h:122` — "252 total"). The evaluation vector is sized `12 * numModeSlots`
  (`keymodeanalyzer.cpp:571`) and the double loop scores **every** (tonicPc, modeSlot) with no
  early exit (`:573-605`). No pruned subset.
- The six scoring terms are summed per candidate (`:591-592`): scale membership, triad
  evidence, key-signature proximity, characteristic pitch, true leading tone, mode prior;
  the declared-mode penalty is subtracted (`:598-603`).
- `analyzeKeyMode` itself RETURNS only the **top-3** (`keymodeanalyzer.h:167`;
  `keymodeanalyzer.cpp:727-754`), with the winner chosen by a family-selection tonal-centre
  formula among the modes that share the notated signature (`:645-693`) — but the sequence
  decoder does **not** consume that top-3; it reads the **full 252-candidate dump** via the
  `dumpOut` instrument (`keymodeanalyzer.cpp:788-831`; the decoder calls
  `analyzeKeyMode(ctx, keySigFifths, keyPrefs, declaredMode, &dump)` at
  `key/keymodesequence.cpp:147`).

Plain sentence: *for every slice we compute a fitness score for all 252 possible keys; nothing
is pruned at this stage.*

### 1.2 Sequence decode — a pruned lattice, then a full global Viterbi over it

This is the load-bearing stage. Two distinct steps:

**(a) The lattice state set is the global union of each slice's emission TOP-8 — a prune**
(`keymodesequence.cpp` `buildLattice`, `:127-175`). Per slice it stores all 252 emission
scores in `byCand[t]` (`:152-154`) but inserts only the **top-`k` (k = `seqPrefs.topK` = 8**,
`keymodesequence.h:116`) candidates into `globalCand` (`:140,156-159`). The lattice state set
is that union (`:162-167`); the emission is then projected onto it using the FULL per-slice
scores (`:168-173`), so a state that made top-8 at *some* slice is scored at *every* slice —
but **a state never in any slice's top-8 is absent from the lattice entirely.** The header
names this "State pruning" and argues the incumbent is protected because it is top-8 where it
prevails (`keymodesequence.h:55-63`). **Measured lattice sizes on the traced pieces: 31
(`bwv369`), 26 (`bwv110.7`), 27 (`bwv226.2`) states — ≈ 10–12 % of the 252**, not the full grid.

**(b) The Viterbi over that state set is exhaustive and GLOBAL, no beam inside it**
(`decodeLattice`, `:242-398`). Forward max-sum pass considers every state against every
predecessor at every slice (`:266-295`), takes the best end state + traceback for the connected
optimal whole-span path (`:297-321`), and a backward pass (`:323-348`) gives each slice a
sequence-margin confidence. There is **no** beam pruning inside the Viterbi — the optimum is
over the whole span, not windowed or greedy.

**Transition / change costs** (`changeCost`, `:231-240`): stay = 0; switch =
`changeBaseCost + changePerFifthStep × cofDistance + relativePairExtraCost` (the last only for a
same-signature relative-major/minor flip). The three constants are the resolver's live margins,
all `[empirical]` / hand-set: `changeBaseCost = hysteresisMargin = 2.0`
(`types/analysistypes.h:782`), `changePerFifthStep = keySignatureDistancePenalty = 0.60`
(`:704`), `relativePairExtraCost = relativeKeyHysteresisMargin = 2.0` (`:788`). The emission
window is `windowBeats = 4.0` (`keymodesequence.h:137`, deliberately small — the header says the
transition penalty "carries the long-range coherence the old 16-beat look-back faked"). **None of
these is in `tools/param_manifest.json`** (grep-empty for the L3 sequence constants; this is
OI-91, re-confirmed; `relativeKeyHysteresisMargin` also value-duplicates `hysteresisMargin`, OI-97).

Plain sentence: *the search is not full-lattice — it first throws away every key that was not
among the 8 best-scoring at some slice, then finds the single best whole-piece key line over
what remains, preferring to stay put by a fixed hand-set penalty.*

### 1.3 Region commit — deterministic reduction, no greedy/hysteresis key commit

The whole-score decode runs ONCE (`regionanalyzer.cpp:632-636`); the reach-back re-decode loop
(`:658-720`) is `opts.reachBack.enabled` default OFF and cannot fire on a whole-score model.
Each coarse Pass-1 region takes `localKeyForRegion(rs, re)` (`:737-843`): it walks the region's
slices, `votes` accumulates the CHOSEN key's duration (`:788`), and the region key `best` is the
**duration-majority** chosen key (`:798-805`) — a pure reduction of the global Viterbi output, no
hysteresis, no re-inference. The result is assigned to `region.keyModeResult` /`keyAlternatives`
/`keyConfidence` at `:1030-1032` (pre-merge) and `:1049-1051` (region); Pass-2 sub-regions
inherit it verbatim (`inheritRegionKeyContext`, `:274-279`).

**Where the audit's "greedy expansion step" actually sits:** `greedyExpandSegmentation`
(`:870-873`) decides **segmentation boundaries** (Layer 2), consuming the resolver seed
`keyFifths/keyMode`, **not** the key. It changes WHERE regions split, not WHICH key they get.

**The only post-decode key revision** is `applyJointKeyWiring` (`:396`, called at `:1472`), gated
on `jointKeyWiringEnabled()` = the `MUSE_JOINT_KEY_WIRING` env var, **default OFF**
(`section/jointkeydecision.cpp:138-140,145`) — it never runs in production.

Irrevocable points on the KEY path, in order: **(1) the top-8 emission→lattice prune** (a state
never top-8 anywhere cannot be recovered by any later stage); (2) the global Viterbi optimum
(not premature — it IS the global optimum, but it is final); (3) the Pass-1 duration-majority
reduction, inherited unchanged by sub-regions. There is **no greedy or hysteresis-gated key
commit** anywhere downstream of the decode.

### 1.4 The carry — `keyAlternatives`, capped, per-alternative margin discarded

Two truncations, both downstream of the decode:
- **Per slice:** `SliceKeyMode.alternatives` is ranked by the sequence-margin total
  (`alpha+beta`) and capped at `maxAlternatives = 4` (`keymodesequence.h:151`;
  `keymodesequence.cpp:384-394`). Each carried alternative is built by `stateToResult`, which sets
  `.score` = the state's **emission** score and drops the ranking total (`:393` → `:94-103`), and
  `normalizedConfidence` = 0. So the per-alternative closeness that ranked it **is computed then
  discarded** (OI-75 / OI-81, re-verified at the current code).
- **Per region:** `localKeyForRegion` builds a `menu` bucketed over each slice's chosen key AND
  its ranked alternatives, weighted by overlap duration (`regionanalyzer.cpp:766-792`), and
  `keyAlternatives` = that menu minus the chosen key, ranked by accumulated weight
  (`:837-841`) — the menu **weight is used for ordering then dropped** (the returned
  `regionAlts` is a plain `vector<KeyModeAnalysisResult>`). `keyConfidence` = `rep.confidence`,
  the chosen key's single sequence margin (`:842`), not a per-alternative quantity.

`keyAlternatives` / `keyConfidence` have **zero production consumers** — declared dormancy for
L5 (OI-75; `cc_l3_audit_pass1_report.md` §2). So the carry is where the ranking information is
lost to consumers, but it is **not** where the true key is lost from the analysis.

### 1.5 Anchoring — one signature read at start, applied to the whole decode

`resolveKeySignatureContext` (`key/keyresolver.cpp:206-252`) reads the `KeySigEvent` at **one
tick** (`:218`, `tick` = the analysis `startTick`), maps the declared mode from `KeyMode`
(`:225-236`, dropped under `ignoreDeclaredMode`, `:242-244`), and applies the Baroque
partial-signature correction gated on the declared mode (`:247-250`; `partialSignatureCorrection`
`:107-190`, `kPervasiveFraction = 0.03`, `kDominanceRatio = 2.0`, `:182-183`). The decode receives
these as **scalar** `correctedFifths` / `declaredMode` applied to **every** slice's emission
(`regionanalyzer.cpp:634-636` → `keymodesequence.cpp:147`). Inside the emission the signature is
one weak per-candidate bias (`scoreKeySignatureProximity`, `keymodeanalyzer.cpp:586`) and the
declared mode another (`declaredModePenalty = 1.0`, subtracted, `:598-603`,
`analysistypes.h:733`).

Consequences at code:
- **A mid-piece notated key-signature change is never re-anchored** — one signature for the whole
  decode; a notated change is tracked only via the note-driven change cost
  (`regionanalyzer.cpp:626-628`; OI-94(a), re-confirmed).
- **The declared mode DOES enter the key decode** (as the penalty). OI-78's silo is about a
  *different* consumer (the chord diatonic bonus), out of L3-decode scope.
- **No dominant-implication / cadence key-evidence channel enters the decode** — named but not
  built (OI-94(b) = OI-68 A-3).

---

## §2 — Cowork's three predictions, answered

| # | Prediction (recorded before I looked) | Verdict | Evidence |
|---|---|---|---|
| 1 | The per-slice EMISSION evaluates ALL candidate states, not a pruned subset | **MET** | `keymodeanalyzer.cpp:571-605` scores all 12×21 = 252; `keymodesequence.cpp:147` reads the full 252-dump per slice. (Nuance: `analyzeKeyMode` *returns* only top-3, but the decoder consumes the full dump.) |
| 2 | The SEQUENCE decode is ALSO full-lattice over its states, no search pruning inside it | **FAILED (the load-bearing correction)** | The lattice state set is the **union of each slice's emission top-8** (`topK=8`, `keymodesequence.cpp:140,156-159`), measured at **26–31 states** (~12 % of 252), not the full grid. A key never top-8 anywhere is absent (`bwv226.2` G major, §3). The Viterbi *within* that set IS full and global with transition costs (`:266-321,231-240`) — so the "full + transition-cost" half is right, the "no search pruning" half is wrong: the top-8 union is a search-level prune upstream of the Viterbi. |
| 3 | The loss happens DOWNSTREAM of the search — at a greedy/hysteresis region-commit and/or the carry truncation | **FAILED / refined** | (a) There is **no** greedy or hysteresis key commit: the greedy step is *segmentation* (`:870-873`), the region key is a deterministic reduction (`:737-843`), the only post-decode override is env-gated OFF (`:1472`). (b) The carry IS a truncation that discards the per-alternative margin (§1.4) but is **not** where the true key is lost — in all three traces the key was already lost upstream. (c) The loss lives at the **emission model + its ±4-beat window** and at the **single change-cost constant** (§3). |

Two of three predictions failed — the mechanism differs from the pre-look picture in a way that
changes the design conversation (per the instruction: a failed prediction that finds a real
search-level prune is the more useful outcome).

---

## §3 — The three failures re-traced against the found mechanism (Task 2)

All numbers are the **decoder's own** per-slice emission (via `--decode-keymode --seq-max-alts
260`, which widens the *serialized* alternatives without changing `topK`, so the lattice and the
decode are unchanged). The `--dump-key-candidates` figures are the **resolver's** per-region
emission (a wider fixed-lookback window, a different instrument) shown only as corroboration.
`bwv369`, `bwv226.2`, `bwv110.7` are none of the 12 transposed pieces (OI-142), so these are
genuine inference errors.

### Case A — `bwv369@10080`: LOCAL EMISSION failure (the narrow window), not a beam drop
Score in 1 sharp (G/e-minor); DCML global = e minor. The decoder reads D major at m5 (correct
local area), then at m6 (tick 10080) chooses **G major** and stays.
- Decoder local emission at 10080: **G major #1 = 35.56**; the true **e minor = 29.11, rank #7**
  of 31 surviving lattice states (gap 6.45). The decoder's *chosen* key IS the local emission
  argmax — the Viterbi is not overriding here; **the emission itself ranks the wrong key first.**
- e minor **is** a lattice state (a carried alternative at m5, emission ~32–35) — so it is **not**
  lost from the search; it is out-scored locally and then falls below the top-4 carry.
- Corroboration: the resolver's WIDER window ranks **e minor #1 (63.96)** at this region — i.e.
  the tight ±4-beat window is implicated: more context finds e minor, the narrow window does not.
- **Correction to the diagnosis:** this was described as "the global key drops off the beam
  mid-run." Mechanically the global key is a lattice state throughout; it is **out-ranked by the
  local emission** (relative-major over-pull), then truncated from the 4-slot carry. Not a beam
  drop — an emission-window failure.

### Case B — `bwv226.2@36960`: EMISSION-MODEL failure (deep), a true search-level absence
Score in 2 flats; DCML global = G major (local G). The decoder is locked on **B♭ major** across
m21–25.
- **G major is absent from the 27-state lattice at every slice** in the region (never top-8
  emission → never a lattice state). Verified 36000–37920: chosen B♭ major throughout, G major
  ABSENT from the surviving states.
- Corroboration: even in the resolver's WIDER window, G major ranks **#116 (25.09)** vs B♭ major
  54.47 — a 29.39 gap. The emission scoring model simply does not favor the true key here.
- This is the one genuine **search-level absence**, and its cause is the **emission model**, not
  the beam width or the carry: no lattice/carry mechanism can recover a key the emission ranks
  116th. (This region is in the diagnosis's `absent_from_menu` set — confirmed here as
  absent-from-*lattice*, a stronger statement.)

### Case C — `bwv110.7@14400`: VITERBI / CHANGE-COST over-smoothing (a fifth off)
Score in 2 sharps (D/b-minor); DCML global = b minor. The decoder reads **B (harmonic minor)**
correctly at m7 b1–2.5, flips to **F♯ minor** (the dominant of b) at m7 b3, and stays in F♯ minor
through m8–m9.
- Decoder local emission at 14400: **B minor #1 = 27.96**, D major 27.94, F♯ minor 27.87 — a
  near three-way tie (spread **0.09**). The decoder **chose F♯ minor (local rank #3)** — here the
  whole-sequence Viterbi **overrides** the razor-thin local winner. Sequence margin `keyConf = 5.1`
  (the F♯ minor path is robust over the run).
- Mechanism: F♯ is the dominant of b minor; the F♯-span emission is competitive, and over a
  non-discriminating emission (0.09 spread) the fixed change cost (2.0 + 0.6·steps) makes a single
  coherent F♯-minor run cheaper than flipping B→F♯→B. The decoder has **no cadence /
  dominant-to-tonic channel** to read F♯ as V-of-b, so the dominant span becomes its own key —
  the "a fifth off" wrong-key-area drift the diagnosis found dominant among genuine errors.

**Summary of the three:** three genuine errors, three distinct mechanisms — narrow-window emission
(A), deep emission-model failure (B), change-cost over-smoothing of a flat emission (C). In none
is the loss at the carry; in none is it a greedy/hysteresis region-commit.

---

## §4 — Where drift and stickiness mechanically live (mechanism only)

- **The emission scoring model + its ±4-beat window is the first and largest loss point.** It
  decides the top-8 that forms the lattice and the per-slice ranking the Viterbi follows. When it
  ranks the true key below the local winner (A) or buries it out of the top-8 (B), the true key is
  lost before the Viterbi, the carry, or any downstream stage can act. Two of three traced losses
  are here.
- **The single hand-set change cost is the second loss point (stickiness / over-smoothing).** Over
  a non-discriminating emission it commits the global optimum to a wrong coherent run — a cadential
  dominant read as its own key (C). This is Temperley's "inertia" constant, and ours is unfit
  (`hysteresisMargin` 2.0 / `keySignatureDistancePenalty` 0.60 / `relativeKeyHysteresisMargin`
  2.0, none in `param_manifest.json` — OI-91/OI-97).
- **The top-8 emission→lattice prune is a real search-level prune** (contradicting the "search is
  full-lattice" premise), but it bites only where the emission has already failed to rank the true
  key top-8 (B). It is a *symptom* of the emission model, not an independent cause.
- **The carry (`keyAlternatives`, 4-slot cap, discarded per-alternative margin) is downstream and
  secondary.** It loses ranking information to L5 consumers (OI-75/OI-81), but it never loses a key
  the decode actually chose; it reflects an already-failed emission/decode.
- **There is no greedy or hysteresis-gated key commit, and no beam inside the Viterbi.** The greedy
  step is segmentation; the region key is a deterministic reduction of a global optimum; the
  Viterbi is exhaustive over its (pruned) state set.
- **Anchoring is one-shot:** a single signature + declared mode read at start, applied to the whole
  decode; a mid-piece notated key change is never re-anchored (OI-94), and no cadence/dominant
  channel enters the decode (OI-68).

Plain statement for the design conversation: **the literature's "a key can only be outranked,
never dropped" does NOT hold for our decoder — a key can be dropped, at the top-8 emission→lattice
boundary. But on the traced failures the true key was dropped *because the emission scored it
poorly*, not because the beam was too narrow around a well-scored key. The drift and stickiness
live in the emission scoring model (+ its narrow window) and in the one unfit change-cost
constant; the lattice prune and the carry truncation are downstream consequences, not the primary
causes.** Mechanism only — no fix, no design.

---

## §5 — Self-check + boundary honored

- **Read-only w.r.t. production.** No `src/` file changed, no constant tuned, no golden refreshed.
  Only the committed default-OFF diagnostics were run (`--decode-keymode`, `--dump-key-candidates`,
  and the read-only `--seq-max-alts` override which changes only the *serialized* alternative count
  on the diagnostic path, not `topK` and not the decode). `tools/robust_stop/` and `tools/corpus/`
  written by NOTHING; all dumps went to a session scratch dir outside the repo.
- **Verified at the code and data, never at assertion (#15/#19).** Every mechanism claim is a fresh
  file-and-line citation; every failure number is from a dump, not another document. The one place
  I lean on a prior report (the diagnosis's case list) I re-measured (Case B is confirmed
  absent-from-*lattice*, stronger than absent-from-menu) and corrected its "drops off the beam"
  phrasing where the code contradicts it.
- **Resolver-vs-decoder caveat stated:** the `--dump-key-candidates` figures are the retired
  resolver's wider-window emission (a different instrument); every conclusion rests on the
  **decoder's own** emission (`--seq-max-alts`). The resolver figures are corroboration only.
- **No self-invented labels/jargon:** the names used (emission, lattice, top-8 union, change cost,
  Viterbi, carry, `keyAlternatives`, `keyConfidence`, region reduction) are the code's and the
  register's own. New register content is one row (OI-141 update) + cross-references to existing
  OI-75/OI-81/OI-91/OI-94/OI-97/OI-68.
- **Findings are register rows and report sections, nothing built or fixed** (principles 7/8).

*CC, 2026-07-12. The mechanism is pinned: our decoder is not full-lattice — it prunes to a top-8
emission union, then runs a global Viterbi with one unfit change cost. On the traced failures the
true key is lost at the emission model (+ narrow window) and at the change cost, not at the carry
and not at a greedy commit. The "beam drop" framing is corrected. The design conversation is the
user's to open on this mechanism; this report decides and builds nothing. Fork-only; `upstream`
untouched.*
