# Language-mechanical sweep — the L3 (key/mode) architecture spec

> **Method** (as in `cowork_spec_language_sweep.md`): take each two-place word, force it to be followed by the thing
> it points at, and flag where that forces a phrase the spec does not supply. This pass goes **deeper** than the
> combined L1–L4 sweep, chasing every L3-specific pointer word, not only the ones L3 shares with L4.
>
> **Headline.** L3 is markedly *more* complete than L4. It already names the arguments L4 leaves bare: "confidence"
> is defined (sequence margin, §9 + glossary), "the residual" is enumerated concretely (§11), the candidate space is
> fixed (252), and "emphasised" is unpacked (bass / strong beat / frequency, §2). So the sweep returns **four**
> genuine L3-specific holes plus the two it shares with L4 — a short list, fixable in place without reopening the
> architecture.

---

## L3-specific holes (new — not in the combined pass)

**H1 — "how far apart the two keys are" → apart *measured on what?*** (§4, §5 step 2, §9). The change cost "grows
with how far apart the two keys are," and a "near modulation" is made cheaper than a "remote" one. Forced: *apart =
__distance along the line of fifths__*, or *__semitone distance between tonics__*, or *__number of differing notes in
the two scales__*? These rank key-pairs differently (B and F♯ are one step apart on the line of fifths but six
semitones apart), so the choice changes which modulations the layer treats as "near." The spec names the *shape* (cost
rises with distance) but never the **distance measure** — and that measure decides the layer's whole modulation
behaviour. This is the most consequential L3 hole. (Numeric weights stay tunable; the *metric* must be named.)

**H2 — "change cost" / "expensive" / "cheap" → costed *in what units, against what?*** (§4, §5 step 2). "Keeping the
current key/mode cheap and changing it expensive." Forced: a change cost is only meaningful **relative to the local-fit
score** it is subtracted from — a penalty of "5" is cheap or dear only against the fit numbers. The spec adds
local-fit and subtracts change cost (§4) but never says the two are **on one common scale**, nor what that scale is.
Two readers could put fit and cost on incomparable scales and get opposite sequences. State once: *change cost is
expressed in the same units as the local-fit score, so that one sum is meaningful.*

**H3 — "brief" / "sustained" / "so few slices" / "persists" → brief/sustained *for how long, by what test?*** (§4,
§6). "A brief excursion is not worth the change cost"; "a sustained modulation is worth it." Forced: *brief = __the
excursion spans too few slices for the accumulated better fit to repay the two change costs (in and back out)__*. The
spec actually *does* supply this completion implicitly ("not worth the change cost over so few slices") — so the rule
is **present but not named as the definition**. The fix is small: state plainly that "brief vs sustained" is **not a
slice-count threshold at all** but the outcome of the fit-versus-cost arithmetic, so no "how many slices" number is
ever set. (Worth making explicit precisely because a reader expects a duration threshold and there isn't one.)

**H4 — "a set limit" (reach-back) → limited *to what, measured how?*** (§5, §6). When the opening has no settled key,
L3 widens earlier "until the prevailing earlier key is in view **or a set limit is reached**." Forced: *a set limit =
__a maximum reach-back distance, measured in __[bars? beats? slices? notes?]__. The unit is unnamed (§7 lists
"reach-back-window size" as a tunable but not its unit), and it shares the untested "in view" condition (below). Name
the unit and the stop test.

---

## Shared holes (same as L4 — reached again here)

**S1 — "uncertain" → uncertain *about what?*** (§1, §2, §4, §6, §7). As in L4, the bare mark never names its
proposition, and §7's data design carries it as a **yes/no with no about-what field**. For L3 the proposition is one
of a small, *nameable* set: *uncertain — the notes do not decide __(a) relative major vs relative minor__ / __(b)
which side of a modulation seam this slice is on__ / __(c) which modal rotation of a shared collection__*. Because L3's
ambiguity classes are already enumerated (§11), the payload is cheap to add and high-value: the later step is told not
just *that* the slice is uncertain but *which* of the three questions to arbitrate.

**S2 — the destination: "the later, gated key-and-chord step" vs "Architectural Layer 5 (function)."** (§1, §2, §3,
§9, §11, §13). L3 hands its residual forward, but — exactly as in L4 — fills the "settled by ___" blank with both
names, sometimes in the same section (§11 uses "the function layer (Architectural Layer 5)" and elsewhere "the later,
gated key-and-chord step"). Forced to one canonical name, the spec cannot give it. **This is the one hole the sweep
cannot fix in place**, because it is a genuine undecided architecture question shared with L4 — *is the resolver of
"uncertain" Layer 5 itself, or a distinct gated step sitting between the note-layers and Layer 5?* It must be decided
once and named identically in both specs.

---

## Swept and confirmed complete (the contrast that proves the method)

These L3 two-place words **are** completed, and are the standard the rest should meet:

- "confidence" → *how much better the winning sequence is than the best sequence forced to a different key/mode at
  this slice* (§5 step 4, §9, glossary) — fully named, including its unit (a sequence-score margin).
- "the residual" → the three enumerated classes (§11: tonicization-vs-modulation; same-collection centre; symmetric
  spelling) — fully named.
- "emphasised" → *in the bass, on a strong beat, or sounding often* (§2) — named.
- "local-fit … how well it fits" → *the reused per-window scorer's score* (§3, §4) — named (routed to a defined
  component), the completion L4's general "fit" still lacks.
- "candidate" → *one of the 252 (12 tonal centres × 21 modes)* (§1) — fixed and enumerated.
- "weak prior / weak hint" → *overridden whenever the note evidence conflicts* (§2) — named.

The pattern matches the L1/L2 finding: where L3 specifies a **defined quantity** (confidence, the candidate set, the
residual classes) the pointer words resolve; the four open holes (H1–H4) are all places where L3 names a **shape**
("grows with distance," "cheap vs expensive," "brief vs sustained," "a set limit") without naming the **quantity** the
shape is over. Naming those four quantities — a distance metric, a common scale, the fit-vs-cost arithmetic, a
reach-back unit — closes L3 to the standard, with S1 (add the about-what payload) and S2 (decide the destination)
remaining.

## Recommendation

H1–H4 and S1 are safe in-place precision fixes to the L3 architecture spec — they make explicit what the built layer
already does (or must do), change no behaviour, and do not reopen the SIGNED architecture. **S2 is the exception**:
do not fix it unilaterally in either spec — it is the user's architectural call (one box or two), and once decided it
is named identically in L3 and L4. I have left S2 flagged, not resolved, in the L4 rewrite for the same reason.
