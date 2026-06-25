# Language-mechanical sweep — the L1–L4 architecture specs

> **Method.** Many words are *two-place*: they point at something but are written with only one place filled.
> "Uncertain" means *uncertain about X*; the spec writes the bare "uncertain" and the missing X is the imprecision.
> The sweep is mechanical: take each two-place word, **force it to be followed by the thing it points at** — a
> complete sentence — and wherever that forces a phrase the spec does not actually supply, a hole is found. This is
> deliberately blind to meaning; it catches gaps the semantic review (`cowork_layer4_spec_review.md`) did not, and
> reinforces several it did.
>
> Findings are grouped by the kind of missing argument. L1 and L2 (mature, AS-BUILT) come out almost clean and are
> confirmed at the end; the work is in L3 and L4.

---

## Group I — words missing their *proposition* ("about what?")

**"uncertain" → uncertain *about what, exactly?*** The single most-used word in both L3 and L4, and nowhere does it
name the proposition it doubts. Forced to complete it, the specs split into readings they never choose between:

- L3 §1, §2, §4, §6, §7: "marks the slice 'uncertain'." Forced: *uncertain — the notes do not decide __which of the
  carried key/modes is the tonal centre__* — **or** *uncertain — the notes do not decide __whether any single key
  fits this slice at all__*. These are different claims (a choice between named alternatives vs an absence of any
  fit), and the later gated step must act on them differently. The spec commits to neither.
- L4 §1, §4, §5, §6: "marks them 'uncertain'." Worse here, because L4 names two things at once (the chord symbol
  *and* each note's membership). Forced: *uncertain about __the root__* / *__the quality__* / *__which sounding note
  is a chord tone__* / *__all of it__*? A thin slice and a relative-major/minor share-tone pair are both "uncertain,"
  but about completely different things. Unspecified.
- **Sharper than the glossary gap.** The earlier review noted "uncertain" is undefined (A8). The mechanical pass
  shows the deeper fault: even the **data design** (L3 §7, L4 §7) carries "uncertain" as a bare **yes/no**, with no
  field for *what* is uncertain. A downstream selector is told *that* the layer is unsure but not *what to choose
  among* — it cannot act precisely on a one-bit flag. The output needs an **uncertain-about-what payload**, not just
  a mark.

**"ambiguous" / "genuinely ambiguous" → ambiguous *between what and what?*** Sometimes the pair is named, often not.

- L3 §1/§2 "where the evidence is genuinely ambiguous" — forced: *ambiguous between __the relative major and its
  relative minor__*, or *between __a tonicization and a real modulation__*. Where §2 later names those two cases it is
  complete; the many bare "genuinely ambiguous cases" elsewhere are not.
- L4 §1 "the genuinely ambiguous cases" — forced: *ambiguous between __which two chord readings__?* Named in a few
  places (`C` vs `Cadd9`; `iii` vs `I6`; `V6` vs `vii°`) and bare in the rest. The rule should be: a "genuinely
  ambiguous" claim always names the competing readings, because the carried alternatives *are* that pair.

---

## Group II — words missing their *test* ("by what condition do we know?")

These are the holes the phantom-root defect fell through. Each names a stopping or fallback condition in principle but
never gives the condition that fires it — and forcing the completion exposes a **circular** definition.

**"in view" → in view *by what test?*** When does the layer *know* the thing is in view and stop?

- L3 §5: "widen … until the prevailing earlier key **is in view** or a set limit is reached." Forced: *in view = __a
  single key/mode is committed (not 'uncertain') for the opening slice__*? The test is never stated.
- L4 §2/§4: "lazy-extends … until the prevailing harmony **is in view**, and no further." Same hole — and this is the
  measured under-gathering (review A3).

**"as far as needed" / "enough" → needed *for what?*** L4 §2: the window "extends only **as far as needed**." Forced:
*needed __to bring the prevailing harmony into view__* — which routes straight back to "in view," whose own test is
missing. So "extend as far as needed" reduces to "extend until in view" reduces to "extend until enough" — **a circle
with no ground**. The implementer, handed a circle, picked a fixed reach and under-gathered. The spec must break the
circle with a concrete condition (e.g. *extend across contiguous slices that share one consistent chord reading; stop
at the first slice that does not*).

**"prevailing chord" / "prevailing harmony" → prevailing *as of when, measured how?*** Used ~ten times in L4 as
though it were a defined object; it is not. Forced: *the chord of __the nearest preceding slice already decided__* —
**or** *the chord that __covers the most time across the window__* — **or** *the chord on __the last strong beat__*?
Three different objects, three different answers on the exact thin slices that matter. (Compounded by review A7: in
the first reading there are no decided neighbours yet, so "prevailing chord" has *no* referent there at all.)

**"decisive" / "clear" → decisive/clear *past what bar?*** L3 §1 "where the note evidence is **decisive**"; L4 §2
"never overrides **clear** chromatic evidence." Forced: *decisive = __the winning margin exceeds the uncertain
threshold__*; *clear = __the chromatic reading beats the diatonic one by more than the prior's weight__*. The
mechanical pass shows "decisive" and "uncertain" are **the two sides of one threshold** and should be defined once as
a single quantity, not as two independent adjectives.

---

## Group III — words missing their *destination* ("which later thing?")

**"later" / "the later gated step" / "the gated key-and-chord step" / "Architectural Layer 5" → settled *by which one
thing?*** Forcing "the residual is settled by ___" exposes that the specs fill that blank with **three different
names**, used interchangeably, and never say whether they are one destination or several:

- L4 §1 hands the residual to "the later, gated key-and-chord step **and** Architectural Layer 5 (function)" — reads
  as two destinations.
- L3 §1/§11 hands its residual to "the later, gated key-and-chord step" in some sentences and to "the function layer
  (Architectural Layer 5)" in others — reads as one, named twice.
- L4 §9/§3 calls it "the later, separately-gated key-and-chord step," distinct from Layer 5.

Forced to complete every "deferred to ___" with a single canonical name, the specs cannot — because the architecture
has not fixed **whether the thing that resolves 'uncertain' is Layer 5 itself, or a separate gated step that sits
between Layer 4 and Layer 5.** This is a genuine architectural ambiguity the prose has been papering over with
synonyms. It must be named once and defined: one box, one name, one place in the dependency order.

**"defers / leaves for / hands forward" → defers *what* to *that* destination.** The *what* is usually well-named in
L4 (the re-spelling judgment; the symmetric rotations) and L3 §11 (tonicization-vs-modulation; same-collection
centre; symmetric spelling) — this half is good. It is only the *destination* (Group III above) that is unstable.

---

## Group IV — words missing their *criterion* ("by what rule is it so?")

**"plausible" / "implausible chord tones" → implausible *by what criterion?*** L4 §5.3/§4.2: "a reading needing many
**implausible** chord tones is penalised." Forced: *implausible = __a chord tone the membership cues say should be a
non-chord tone__*, or *__an extension rare for the style preset__*, or *__a pitch outside the key__*? Three different
penalties; the spec names none. This drives the symbol↔membership feedback and is unspecified.

**"spurious" → spurious *by what test?*** L4 §1/§4/§5: keep an embellishment slice "from spawning a **spurious** new
symbol." Forced: *spurious = __a symbol different from the prevailing chord on a metrically weak slice whose odd notes
are all stepwise non-chord tones__*. That completion *is* the missing fallback rule (review A2) — "spurious" is
standing in for a decision procedure that was never written.

**"too few notes to fix the chord" → too few *than how many*, to fix *what*?** L4 §5. Forced: *fewer than __a complete
triad (three distinct pitch classes)__*, too few to *__determine root and quality uniquely__*. The threshold is
implied by the prose ("only two notes") but never stated as the rule; "fix the chord" = pin root+quality should be
said.

**"fit" / "fits" → fits *by what measure?*** L3 §4 routes "how well it fits the notes" to the named reused scorer —
**complete.** L4 §4.1 "how well the pitches **fit** each candidate" names no measure in the general case; only the
incomplete-chord path (§5) gives one (present tones credited, absent ones a mild miss). The general chord-fit measure
should be stated once, as L3's is.

---

## Group V — L1 and L2: swept and confirmed near-clean

The same sweep over the two AS-BUILT specs finds their two-place words almost all completed — which is the standard
the upper specs should meet:

- L1 "lossless" is immediately completed ("keeps every note **and** every fact … **and never** discards or
  summarises"), "widen the span" always names the direction ("earlier and/or later in time"), "backward search" always
  names "no limit." The one residue: "the per-note facts that **later layers need**" (§1) — *needed by which layer,
  for what?* — but §7 then enumerates all eleven facts, so the blank is filled downstream.
- L2 "a fact, never a guess" is completed by the explicit rule ("a boundary at every note start **and** stop"); "the
  set of notes **changes**" is completed by the exact-set definition (§7, including same-pitch doublings). "Over-grab"
  is defined. No open two-place words of consequence.

Their cleanliness has a cause worth copying: L1/L2 specify *facts with definitions*, so every pointer word resolves to
a stated rule. L3/L4 specify *judgements under uncertainty*, and that is exactly where the bare pointer words cluster —
which is the warning that the judgement rules are the part still unwritten.

---

## What the mechanical pass adds beyond the semantic review

Reinforces (same holes, reached blindly): the window stop-condition (II ≈ review A3), the prevailing-chord fallback
(II/IV "spurious" ≈ A2), "decisive"/"uncertain" as one threshold (II ≈ A4), "uncertain" undefined (I ≈ A1/A8).

**New** (the method's own catches):

1. **"uncertain" needs an *about-what payload* in the output**, not merely a glossary definition — a one-bit mark is
   unactionable downstream (Group I).
2. **The "later gated step" vs "Layer 5" destination is architecturally unfixed** — three synonyms hide an undecided
   box in the dependency order (Group III).
3. **"implausible chord tones" has no criterion** — the symbol↔membership feedback rests on an undefined word
   (Group IV).
4. **"as far as needed → in view → enough" is a closed circle** — not just vague but self-referential, with no ground
   condition (Group II).
5. **"genuinely ambiguous" should always name its competing pair** — the carried alternatives *are* that pair, so the
   bare phrase is a missed chance to be exact (Group I).

## Recommendation

Fold these into the L4 rewrite as a **completion rule the prose must obey**: every "uncertain" names what it doubts
and carries that as output; every "ambiguous" names the competing pair; every "in view / enough / needed" gives a
ground test, not another pointer; every "prevailing chord / plausible / spurious / decisive / clear" resolves to a
stated rule (value still deferrable to tuning); and "the later gated step" is replaced everywhere by one fixed,
defined name. Then apply the same rule pass to the L3 architecture spec, and the light residue to L1.
