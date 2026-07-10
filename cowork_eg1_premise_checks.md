# EG-1 Premise Checks — the Pre-Build Ledger Inputs (read-only, at code)

> **Cowork, 2026-07-10 (session 36, post-probe).** User-directed follow-up to
> `cc_eg2_probe_report.md`: before the EG-1 build (the arc-#9 selection re-ordering + arc-#11
> F-B demotion + the distinct-root carry) is opened, the two mechanisms whose failure dominated
> the EG-2 probe are traced AT CODE (#18: checkable premises get checked). Read-only; no design
> decided here — design decisions are enumerated and assigned to their owning layer (#7).

## PC-1 — WHY the dim7 spelling-pin never fires: ROOT CAUSE ESTABLISHED

**The gate chain** (`chordslicedecoder.cpp`): `decideSlice:712` builds the symmetric set from
**the scorer's CHOSEN candidate** — `symmetricRotationSet(sc.chosen, focal):566` returns valid
ONLY if `chosen.quality == Diminished` (with all of r, r+3, r+6, r+9 sounding, `:592-596`) or
`chosen.quality == Augmented` (`:588-591`). Only then is the spelling consulted:
`spellingRootOf:627` requires every collection tone spelled, uncontradicted (`:604-618`), and
an exact line-of-fifths stack (step 3, `:640-643`); root = max-LOF end (`:646`).

**Gate 2 is sound when reached** — desk-verified here on bwv272's G♯–B–D–F: LOF F=−1, D=2,
B=5, G♯=8, an exact step-3 stack, root G♯ = the DCML rotation.

**Gate 1 is the blocker.** The design premise — *"on a symmetric dim7 sonority the scorer's
chosen quality is Diminished"* — was an unlabeled ASSUMPTION, and the probe measured it FALSE:
of 324 dim7 sonorities (Baroque), 278 abstain and the 214 that end committed choose
**Major 121 / Minor 49 / HalfDim 29 / Sus 10 / Aug 1 / Diminished 4** (`cc_eg2_probe_report.md`
§2.6). Contributing FACT: the four-note dim7 TYPE is deferred (C2/G5,
`chordslicedecoder.h:97-103`), so the Diminished reading competes as a triad-plus-bonus against
complete Major/Minor triads with bass support — and usually loses the argmax.

**Coupled effect (for the next probe's predictions):** when the pin DOES fire, resolved
sibling rotations are excluded from `bestOther` (`:727-741`) — the pin also RECOVERS THE
MARGIN. Opening gate 1 would therefore reduce dim7 abstention, not just fix rotation naming.

**E4 design question — enumerated, NOT decided (Layer-4 owner, #7/#8):**
(a) detect the symmetric collection from the SOUNDING PC SET (`present[12]`) independently of
the chosen quality, pin the root, then re-rank; or (b) land the C2/G5 four-note dim7 type
first (already gated at engage Step-0 F-4), making Diminished win the argmax where it should;
or **(c) — user-raised 2026-07-10 — generalize SPELLING to a first-class evidence primitive**
(the tpc facts are already L1-carried per note; O1 measured ~60 % of the Baroque residual
spelling-resolvable; arc-#9 ranks spelling as load-bearing selection channel #2), of which the
symmetric pin becomes just one consumer — see register row OI-15. Each option owes its own #17
ledger + desk sim (control flow AND arithmetic) at the E4 design step.

## PC-2 — the abstention control flow: ESTABLISHED

`decideSlice`/`applyDecision` (`chordslicedecoder.cpp:1004-1063`): **Commit** requires
`sufficient` (≥ `sufficiencyChordTones`=3 of the chosen's OWN template tones present,
`:1007-1008`) AND `marginOk` (`confidence ≥ uncertaintyMargin`, `:1009-1013`);
**Inherit** only for insufficient continuations of the prevailing chord (`:1038-1055`);
everything else **Abstains** (`:1058-1063`) — including "sufficient but low margin".
Confidence = chosen score − best DIFFERENT-symbol candidate (`:732-744`).

Consequences, now measured (probe §2.2): dense candidate cubes put many readings within the
margin → 18 % of scored duration abstains (86 % of dim7s). Three ledger facts follow:

1. The abstain rate rides on **`uncertaintyMargin` = 0.5 — an arbitrary, never-fit Tier-3 seed**
   (`chordslicedecoder.h:174`). The metric-moving behavior of the whole EG-2 probe sits
   downstream of an unestablished constant.
2. On the E0 chain every Abstain is decided by `resolveAbstained` — progression-first at
   confidence 1.0, the T1-1 trap — so **the EG-1 selection re-ordering directly governs ~18 %
   of scored duration**, and the probe showed the winning root is often already carried
   (bwv10.7: G in the carry, Cm selected; 47 % of abstained duration had a legacy-correct root
   available).
3. The robust-stop metric is abstention-reducible (probe §4.5) — a ratified abstain-aware stop
   convention is owed BEFORE any abstaining path can ever be adoption-gated (instrument-layer
   concern; the probe grader is the prototype; the pinned a8 reference stays untouched until
   then).

## PC-3 — the Xsus fifth mis-rooting: OPEN, checkable, assigned (NOT checked here)

The probe's dominant new-error class (43 % of new-broken: `Xsus` rooted on the 5th of the true
triad — {D,F,A}→Asus, {E,G,B}→Bsus, {D,G,B}→Dsus; §2.3-2.4). **Hypothesis (UNCHECKED — labeled
per #17(a), carries no load):** bass-on-the-fifth voicings let the sus template plus
`bassNoteRootBonus` (0.70) outscore the complete triad read as a second-inversion. CHECKABLE
at the cube dump for `bwv87.7@9600`. Owner: the Layer-4 scorer (a Tier-2 hand-set-constants
family). Timing: the E4/Stage-5 path per #8 — recorded now so the next probe does not
misattribute these committed-cell errors to the L5 selection.

## What this hands the EG-1 build instruction

The build's ledger can now cite PC-1/PC-2 as FACT (established at code + probe-measured), must
carry PC-3 as a labeled open hypothesis, and its desk sim must trace **control flow before
arithmetic** — the EG-2 desk sim's failure mode (predicting term arithmetic for mechanisms
that never fired) is the #17(c) lesson this session adds. Proposed #17(c) sharpening for user
ratification: *"the desk simulation must first establish that the mechanism FIRES on the traced
case (control flow), then how much it moves (arithmetic)."*

*Cowork, session 36. Code cites verified at `chordslicedecoder.{h,cpp}` via direct read;
measured figures from `cc_eg2_probe_report.md` (established instrument). No file besides this
one changed.*
