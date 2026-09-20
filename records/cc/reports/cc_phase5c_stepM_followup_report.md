# CC Report — Phase 5c Step-M follow-up: STOP / DECLARED FINDING (the V/iv over-trigger is NOT guard-fixable)

**Verdict: HARD STOP — the instructed Part A cannot achieve its stated goal, and the over-trigger
is an inference problem, not a guard-placement defect. No code changed, nothing committed,
production untouched (byte-identical). Declaring to Cowork per the standing rule
("if you discover inference problems — only declare them to Cowork"; "no
inference-problem-driven coding").**

The task asked me to (A) hoist the §5.6 **foreign-tone test** to be `emitAppliedLabel`'s first
precondition (no content change — placement only) so that "a fully-diatonic `I` before `iv`"
stops emitting `V/iv`, and (B) re-measure to confirm the 12/6/13 false labels are gone (→ 0/0/0).

**On inspection of the actual cases, the premise is false: the over-trigger chords are NOT
fully diatonic.** Every one is the **major tonic in a minor/modal key** — it carries the **raised
third**, which is foreign to the natural-minor signature. The foreign-tone test (hoisted or not)
therefore **cannot reject them**. The instructed change is **provably inert** for the exact cases
it targets — and inert everywhere else.

---

## §1 — What the over-trigger actually is (the per-case evidence)

Pulled from the existing Step-M dumps (`tools/corpus/{baroque,jazz,default}_l5m/*.ours.json`),
every `inline=I → l5=V/iv` unit. The report's "12/6/13" were the subset where the *legacy region
RN was already exact*; the full population is **62 / 29 / 56**. The structure is uniform:

| example | local key | chord (root + pcs) | the foreign tone |
|---|---|---|---|
| `bwv26.6@11040` | D minor | **D major** = D, **F#**, A | **F#** = raised 3̂ (∉ D-nat-minor) |
| `bwv301@3840` | A minor | **A major** = **C#**, E, A | **C#** = raised 3̂ |
| `bwv40.8@25920` | C minor | **C major** = C, **E**, G | **E** = raised 3̂ |
| `bwv120.6@22560` | B minor | **B major** = **D#/E♭**, F#, B | **D#** = raised 3̂ |
| `bwv176.6@30720` | F minor | **F major** = C, F, **A** | **A** = raised 3̂ |
| `bwv47.5@6720` | G minor | **G major** = D, G, **B** | **B** = raised 3̂ |
| `bwv119.9@10560` | E PhrygDom | **E major** = E, **G#/A♭**, B | **G#** = raised 3̂ |

In **every** case the chord is a major (or dominant-functioned) triad **rooted on the home tonic
pitch class**, containing the **major third** — which in a minor key is a *raised* third, foreign
to the signature, and is *simultaneously* the **leading tone of the `iv`-degree root** (a fifth
below). DCML reads it as the major tonic `I`; the labeler reads it as `V/iv`.

This is **not** a "plain diatonic `I`". The natural-minor tonic is `i` (minor). A *major* tonic in a
minor key is the Picardy/chromatic raised-3rd color — a chord that genuinely carries an accidental.

### Why the structure is unavoidable — `V/iv` is *always* tonic-rooted
`iv` is the 4th degree = tonic + 5 semitones. The applied **dominant of `iv`** sits a perfect
fifth above `iv`'s root: `(tonic+5) + 7 = tonic + 12 = tonic`. So **`V/iv` is rooted on the home
tonic pitch class, by construction.** A chord rooted on the tonic, with a major third, moving to
the 4th degree, is therefore **pitch-class-identical to `V/iv`**. In a minor key the major tonic
*is* exactly this chord. Pitch classes alone cannot separate "the major tonic `I`" from "the
applied dominant `V/iv`"; only **function / cadence context** can (does the music tonicize `iv`?).

---

## §2 — Proof that the instructed hoist is inert (no build needed; it follows from the code)

`emitAppliedLabel` (`src/composing/analysis/function/functionrelationallabel.cpp`) emits an
applied label by exactly two routes, and **both already require a foreign tone to be present**:

1. **Subsumed `tonicizationlabeler`, dominant path** (`tonicizationlabeler.cpp:108-126`): its own
   false-positive guard first proves the target's leading tone `lt = d+11` is **chromatic**
   (`if (pcInMask(collMask, lt)) continue;` — it only proceeds when `lt ∉ collMask`), and then
   *requires `lt` to be present in the chord* (`pcInMask(a.pitchClassMask, lt)`). ⇒ the chord
   necessarily contains a tone ∉ collMask → **foreign tone present**.
2. **Subsumed labeler, leading-tone path** (`tonicizationlabeler.cpp:127-134`): requires the chord
   **root** to equal the chromatic `lt` (`a.rootPc == lt`) → **foreign tone present** (the root).
3. **Broadened path** (`functionrelationallabel.cpp:286-298`): already gated by the *same*
   foreign-tone test `(pcMask & ~collMask) != 0`.

Therefore **every** applied label the emitter produces is on a chord that *already* contains a
foreign tone. The hoisted foreign-tone precondition `(pcMask & ~collMask) != 0` passes for all of
them and **rejects none**. The only chords it *could* newly reject — fully-diatonic ones — are
precisely the chords the emitter **never** labels applied in the first place. The change is a
**no-op by construction.**

For the over-trigger specifically: `collMask = diatonicMaskFromFifths(keyFifths)` is the
natural-minor signature collection; the raised third is never in *any* minor signature (nor in
harmonic/melodic minor, which raise 7̂/6̂, not 3̂). So `hasForeignTone = true` for all 147 cases →
the guard cannot touch them. (Worked example, `bwv26.6@11040`: `pcMask = 580 = {D,F#,A}`,
collMask(D-nat-minor) `= {D,E,F,G,A,B♭,C}`; `580 & ~collMask` has bit 6 (F#) set → foreign-tone =
true → not rejected.)

### Empirical corroboration over the existing dumps
- **AppliedSecondary labels sitting on a fully-diatonic chord: 0 / 0 of 768 Baroque, 755 Default.**
  (The hoisted guard would reject these — there are none.) The 7 apparent Jazz hits in a throwaway
  scan were a *Dorian-collection modeling error in my Python*, not the code: the code's collMask
  comes from the **key-signature fifths**, under which those `V7/III` chords carry a chromatic ♭7̂
  and are **not** fully diatonic. So the true count is **0 on every preset** — consistent with the
  inertness proof.
- All **62 / 29 / 56** `I→V/iv` over-trigger units carry the raised-3rd foreign tone (§1).

**Consequence for Part A's test:** the requested assertion — "the `I→iv` cases now emit `I`, not
`V/iv`" — **cannot be made to pass** with the foreign-tone guard. A test written to that spec would
fail. I therefore did not write it (writing a knowingly-failing or knowingly-vacuous test would be
dishonest).

---

## §3 — Why this is an inference problem (and what would actually discriminate)

The over-trigger is the **tonicization-vs-tonic-function** ambiguity — the *same* continuum the
report's §3.1 / §8.2 "tonicization-vs-modulation residual" lives on, and the same one the
instruction itself **defers to the §5.4 companion** (the modulation recompute, not engaged here).
A major tonic that points at `iv` is pitch-class-identical to `V/iv`; the only discriminator is
whether the surrounding function/cadence treats `iv` as tonicized. That is **Layer-5 §5.4/§5.5
function context**, not a pitch-class guard.

**The one structural handle — and why it is not a clean guard.** Because `V/iv` is always
tonic-rooted (§1), the over-trigger could be narrowed to "an applied label whose chord root is the
home tonic." But suppressing *all* tonic-rooted applied labels would also drop **genuine `V/IV`
tonicizations**, which DCML *does* label (a real secondary dominant of the subdominant is
tonic-rooted too). Deciding "major-tonic color" vs "real `V/IV`" for a tonic-rooted major chord
is exactly the function/context judgment — **inference**, not a structural precondition. So even
the tonic-root angle resolves at §5.4/§5.5, not in `emitAppliedLabel`.

The instruction's constraint ("**do not change the guard's content** — only its placement";
"reuse `diatonicMaskFromFifths` — no second test") forbids the only thing that *might* narrow this
(a new root-vs-tonic test), and the allowed thing (placement of the foreign-tone test) is inert.
The two are mutually exclusive: the instructed mechanism cannot reach the instructed outcome.

---

## §4 — The pending spec amendment rests on the same false premise

`cowork_layer5_function_design.md` carries an **unstaged** edit (the §5.6 "universal precondition"
bullet, meant to ride with the Part-A commit). Its text — *"a plain diatonic `I→iv`"*, *"returned
an applied label for a diatonic `I` before `iv`"* — characterizes the over-trigger chord as
**fully diatonic**, which §1 shows is factually wrong (it is the raised-3rd major tonic, carrying
an accidental). I have **left that edit untouched on disk** (it is a Cowork document; I did not
author it and will not revert another author's pending work). **It should be revised** before any
commit: the over-trigger is a raised-3rd major tonic (a tonicization-vs-tonic ambiguity), and the
foreign-tone precondition — while correct and worth stating as universal *coverage* — does **not**
resolve it (it resolves the separate fully-diatonic `bVII7→III` / `ii°→III` divergence, §4 of the
Step-M report, which is already handled by the broadened path and the labeler's own LT guard).

Note: stating the foreign-tone guard as a universal precondition is harmless and arguably tidy
(it makes the *coverage* explicit), but it must not be sold as the fix for the `V/iv` over-trigger,
and the Part-A test expecting 0/0/0 must not be written, because neither is true.

---

## §5 — What I did and did not do

- **Did:** read the spec §5.6, `functionrelationallabel.cpp`, `tonicizationlabeler.cpp`,
  `writeL5Json` (the `--dump-l5` substrate), the unit tests, the Step-M report; enumerated all 147
  over-trigger cases from the existing dumps; proved the hoist inert from the code; verified the
  emitter is dormant (only consumers: `--dump-l5` default-OFF diagnostic + unit tests — no
  production region/section consumer).
- **Did NOT:** edit `functionrelationallabel.cpp`, add the Part-A test, commit the §5.6 amendment,
  build, or regenerate corpora. There is no point measuring an inert change, and committing a
  no-op fix advertised as closing the over-trigger would be misleading. **Production is
  byte-identical (untouched).** `upstream` untouched.

## §6 — Asks for Cowork (you hold the architecture; this is the local code/data truth)

1. **Re-rule the over-trigger's class.** The evidence says it is an **inference** case
   (tonicization-vs-tonic-function), the §5.4/§5.5 family — *not* algorithmic completion of the
   foreign-tone guard. If you concur, the over-trigger is resolved at the L5-relational **engage**
   by function/cadence context (the deferred §5.4 companion), not by a pre-engage guard.
2. **Revise the unstaged §5.6 amendment** (or tell me to): drop the "fully-diatonic `I→iv`"
   characterization; if the universal-precondition bullet stays, frame it as *coverage of the
   genuinely-diatonic `bVII7→III`/`ii°→III` divergence* (which the guard does handle), and
   explicitly **exclude** the raised-3rd `V/iv` over-trigger (which it cannot).
3. **If you still want a pre-engage suppression of the `V/iv`-on-tonic label**, the only available
   handle is structural-but-inference-laden (root == home tonic), and it conflicts with genuine
   `V/IV`. I will not build it without an explicit ruling — it is an inference fix by the standing
   rule. Tell me which way to go.

**Bottom line:** the instructed Part A is a verified no-op against its target; the over-trigger is
the raised-3rd major-tonic / `V/iv` ambiguity, structurally a tonicization-vs-tonic-function
inference resolved by §5.4/§5.5 at engage. Declared, not coded.
