# Cross-check — row 3: Hentschel, Moss, McLeod, Neuwirth & Rohrmeier 2021, the unified chord model

> **The two extracts compared, 2026-08-31**, under `cowork_reading_pass_commission_2026_08_30.md`
> §4 and the independence protocol of `reading_pass/continuation.md` §2.
> First pass: `reading_pass/extracts/hentschel-moss-mcleod-neuwirth-rohrmeier-2021-unified-chord-model.md`
> (session 1, 2026-08-30). Second pass: `reading_pass/extracts_second_pass/` same file name
> (session 2, 2026-08-31), **written and landed before the first extract was opened.**
> **Neither extract has been edited to match the other.**
>
> **The read-tool bound of §0 of the row-1 cross-check applies here unchanged.**

## 1. Agreements

Both passes agree, and both quote or paraphrase the same governing sentences, on: the three
pitch-class types held **distinct** with **one-directional** conversion (spelled → enharmonic or
generic, never back); **mode as a first-class interval collection**, admitting named diatonic modes
and arbitrary collections alike; the chord as a **graph** over explicit properties, in which a
theory specifying less is still representable and missing properties are induced only where
derivable; **suspensions and ornaments as per-note functions**, with non-chord tones ignorable
rather than removed; and — reached independently by both — that **the paper reports no measurement
of any kind**, being a representation paper whose evidence is qualitative case studies.

**That last agreement is the one that governs how this row may be used:** no figure can be quoted
from it, because it has none.

## 2. The one apparent conflict — **BOTH PASSES RIGHT, AT DIFFERENT SCOPES**

The first extract states that the model treats octave and enharmonic equivalence *"as explicit flags
— never destructive normalization."* The second extract states that SPC → EPC or GPC *"is lossy and
non-reversible."* Read side by side these look opposed.

**Resolved at the paper: they are describing different things and both hold.**

- The **conversion between types is genuinely lossy** — the second pass's reading — because an EPC
  cannot recover the spelling it came from.
- The **graph is not**, which is the first pass's reading: enharmonic equivalence is *"represented as
  a flag that may be associated either with individual PCs or the entire chord, converting the
  corresponding PCs to EPCs"*, octave equivalence by simply ignoring the octave, and — decisively —
  **the graph retains the score-level pitches alongside the abstracted ones.** The Figure 2 caption
  states that the graph *"displays the pitches on the score surface as Specific Pitch Classes (SPC)
  with octave information"* beside the derived properties.

**So: the abstraction is lossy, and the model's answer is not to make it lossless but to KEEP THE
UNABSTRACTED LEVEL IN THE SAME OBJECT.** Neither extract is wrong; each carries half. The half the
second pass had is the warning a consumer needs when it holds only a converted value; the half the
first pass had is the design property. **Recorded here as one fact in two parts; neither extract
edited.**

*This is the clearest case so far of the double pass earning its cost by producing two true
sentences that a single reader would probably have collapsed into one imprecise one.*

## 3. Items one pass held and the other missed — all confirmed at the paper

| Held by | Item | Status |
|---|---|---|
| First pass | A key carries an optional **hierarchy type** beside tonic and mode | **CONFIRMED**, at the formal specification: `KEY := <tonic: PITCH, mode: MODE, [type: KEYTYPE], [KEY]>` with `KEYTYPE := Global \| Local \| Secondary`. **The second pass had key as tonic-plus-mode only, which is incomplete** — and the missing part is exactly the global/local distinction this project's own grading conventions turn on |
| First pass | Modes include arbitrary interval collections, not only the named diatonic ones | **CONFIRMED**, at the specification `MODE := Maj \| Min \| Dor \| … \| INTERVAL*`, with octatonic, hexatonic and pentatonic scales named in the text |
| First pass | The paper does **not** discuss the cadential six-four as a standards flashpoint — that evidence lives elsewhere | **CONFIRMED**: not stated anywhere |
| Second pass | **Root and bass are PITCH FUNCTIONS** carried by individual pitches — *"Other common pitch functions are, for example, root, bass note, and leading tone"* — while **inversion is a separate chord-level property**, `INV := {0..N}` | **CARRIED**. Neither is derived from the other in this model |
| Second pass | The abstraction levels in the model's own order: score level → pitch equivalences → pitch classes → pitch functions → relative pitch classes → chord functions and properties | **CARRIED** |
| Second pass | The four case studies and what each demonstrates — Corelli (one Dorian chord in four notations), Dvořák (Riemannian and Tonfeld at once), a jazz chord whose implicit pitches exceed its label, and a Gubaidulina hexachord with **no traditional root**, handled by a *"central tone"* | **CARRIED**. The post-tonal case is the one that shows what the model's minimal requirement actually buys |
| Second pass | A BNF-like **formal specification**, supplementary online material, and a code repository cited as `https://github.com/DCMLab/chord-model` | **CARRIED**. **Neither pass opened the repository**, and this pass is not licensed to open it as design input |
| Second pass | **Fact of absence:** the paper does not state what an annotation must carry to be losslessly convertible | **CARRIED** — compatible with, and sharper than, the first pass's *"induced only where derivable"* |

## 4. One reading flagged, because it is the kind that gets borrowed later

The second extract records an observation and immediately fences it: this model puts **chord-tone
status at the same level as root and bass — a function a pitch carries** — rather than as a
downstream annotation on a finished chord. **That is a representation choice and says nothing about
WHEN the assignment is decided**, so it is not evidence for or against DP-D in either direction.

**The fence is repeated here deliberately.** A paper by four of the same authors as row 2 (whose
method decides chord tones post hoc) modelling chord-tone status as a pitch-level function is
exactly the sort of adjacency a later reader turns into an argument. **It is not one. This paper
measures nothing and infers nothing.**

## 5. Verdict

**Nothing disagrees between the two extracts.** The one apparent conflict is two halves of one fact
(§2). Three items the first pass held and the second missed are confirmed — one of them, the key's
global/local/secondary type, materially completing the second extract. Five items the second pass
held and the first missed are carried.

**The cross-check for row 3 is COMPLETE, at the relayed grade declared above.**

*Provenance: session 2 of the reading pass, 2026-08-31. All resolution reads at the paper's source
URL, `https://apmcleod.github.io/pdf/mec-chord-model.pdf`. No specification derived, no document
amended, no code opened, no register row or entry written. Neither extract was edited.*
