# Task A, row 3 — Hentschel, Moss, McLeod, Neuwirth & Rohrmeier 2021, the unified chord model — AT THE OBJECT

> **STATUS: TARGETED RE-READ, AT THE OBJECT, 2026-08-31.** Executing §2 of
> `cowork_reading_pass_remedial_commission_2026_08_31.md`. **All six pages (printed pp. 143–148,
> Music Encoding Conference Proceedings 2021) read as page images with the file tools**, from the PDF
> the user supplied at `docs/research_papers/reading_pass_2026_08/mec-chord-model.pdf`, staged
> through the bridge. **No web-fetch read of any kind was used on this row.** A targeted re-read, not
> a third extraction. **Nothing of the findings surface is edited here.**
>
> **This paper prints its own page numbers**; every location below is the printed page.
>
> **★ THREE NOT-ESTABLISHABLE VERDICTS, and they share one cause: the article is six pages, and three
> things our records attribute to it are not in it.** Their substance is confirmed from the article's
> own prose; **their cited evidence is not at the place cited.** None touches a SUPPORTS or a
> rival-defusal, so **none is a STOP** by §2's test.

## The CONFIRMED claims

### C1 — Three pitch-class types with one-directional conversion — **CONFIRMED verbatim**

Carries **DP-L's SUPPORTS** entry and a §5 routed extract.

**p. 145:** *"we model different types of pitch classes: Generic Pitch Classes (GPCs; A–G), Spelled
Pitch Classes (SPCs; GPC plus accidentals), and Enharmonic Pitch Classes (EPCs; MIDI note number mod
12). **An SPC can be converted into an EPC or a GPC, but not vice versa.**"* **Exact.**

### C2 — The unabstracted level is kept in the same object — **CONFIRMED, from the article's own prose**

Carries **§9.0's ENRICHES** entry — the surface's *"with the unabstracted level retained in the same
object"* — and DP-L's *"rather than normalising destructively."*

**p. 146, *Score Level*:** *"This least abstract representation of a chord consists of the set of
pitches that are taken from all the notes within the segment referred to by the chord symbol. On this
level, pitches are typically represented as SPCs, although we can also model annotated MIDI files at
this level with pitches viewable only as EPCs. Each PC is also associated with one or multiple
octaves."* Figure 3a (p. 145) shows exactly that: the Corelli chord's pitches as red circles with
octave numbers attached, **beside** the derived properties.

**And the abstraction's lossiness is equally the paper's own** — **p. 146, *Pitch Equivalences*:*
enharmonic equivalence *"is represented as a flag that may be associated either with individual PCs
or the entire chord, converting the corresponding PCs to EPCs."* **The cross-check's §2 resolution —
that the conversion is lossy and the graph is not — holds at the article**, on this evidence rather
than the evidence it cites (see K3).

### C3 — The level ladder, in the model's own order — **CONFIRMED**

Carries §9.0's *"levels from score-surface pitches through pitch functions (root, bass, chord-tone
status) to chord properties."*

**p. 146** names them in section order: *Score Level* → *Pitch Equivalences* → *Pitch Functions* →
*Relative Pitch Classes* → *Chord Functions and Properties*. **The surface's description of the ladder
is the paper's own organisation.**

### C4 — Chord-tone status is a pitch function at the same level as root and bass — **CONFIRMED, and the fence holds**

Carries **DP-D's fenced note** — the one the surface records *"so it is not enlisted later."*

**p. 146, *Pitch Functions*:** *"Pitches and PCs can be assigned functions within the chord.
Importantly, each can be classified as either a chord tone or a non-chord tone. The possibility of
ignoring non-chord tones, such as suspensions or ornaments, is common to many annotation standards.
**Other common pitch functions are, for example, root, bass note, and leading tone**, but this set of
categorical pitch functions can easily be extended."*

**The fence is right at the object.** This is a statement about what a representation may carry. **The
paper contains no inference procedure and no measurement of any kind** (C7), so it says nothing about
*when* a chord-tone assignment is decided, in either direction.

### C5 — Mode as an ordered interval collection admitting arbitrary sets — **CONFIRMED**

Carries a §5 routing to the mode question.

**p. 146:** *"we refer to any ordered collection of SIVs as a 'Mode', and the combination of a mode
and a tonic pitch as a 'Key'"*, with *"other modes (e.g., octatonic, hexatonic, and pentatonic
scales)"* named where the one-to-one GPC→SIV mapping fails. **Not a closed list of diatonic modes.**

### C6 — The row decides nothing and demands existing annotations — **CONFIRMED**

Carries the §3.1 coupling table's *"Data design — decide nothing."*

**p. 144:** *"The objective of this paper is to propose a unified representation of chords for the
comparative purpose outlined above, making it possible to characterize, query, and translate
different features across standards."* **p. 147**, Conclusion: *"Our contribution should be understood
as a first step towards this goal."* **No analysis is performed on any score; the inputs are
annotation systems.**

### C7 — No measurement of any kind — **CONFIRMED at the whole read**

**There is not a single number reported as a result anywhere in the six pages.** No corpus, no
metric, no evaluation, no comparison. **The cross-check's governing agreement — *"no figure can be
quoted from it, because it has none"* — holds exactly.**

### C8 — The cadential six-four is not discussed — **CONFIRMED at the whole read**

Carries **DP-N's** *"Row 3 does NOT discuss it — established by a direct question, not by absence of
notice."* **Now established by absence of notice over the whole document as well:** the term, the
figure and the object do not appear on any of the six pages. **The surface's entry is right, and its
grade improves from a prompted answer to a whole read.**

---

## ★ The NOT ESTABLISHABLE verdicts — three attributions that are not at the place cited

**Their common cause is at p. 145, footnote 1.** The article states: *"A formal definition of our
model, a comparison of several harmonic annotation standards, as well as more example graphical chord
diagrams, can be found in our **supplementary online material**"*, footnoted to
`https://github.com/DCMLab/chord-model`. **The article is a six-page summary; the formal apparatus
lives elsewhere.** The row-3 cross-check states in its own §3 that **neither pass opened the
repository** — and then attributes three things to "the paper" that are only in it.

### ★ K1 — The BNF specification of KEY and MODE is not in the article

**What the cross-check says** (§3): the key's hierarchy type is *"**CONFIRMED**, at the formal
specification: `KEY := <tonic: PITCH, mode: MODE, [type: KEYTYPE], [KEY]>` with `KEYTYPE := Global |
Local | Secondary`"*, and modes are *"**CONFIRMED**, at the specification `MODE := Maj | Min | Dor |
… | INTERVAL*`"*. The findings surface carries the first into **§5's routed extracts**: *"its Key
carrying an optional **Global / Local / Secondary** type."*

**Neither string is anywhere in the article.** There is no BNF, no grammar and no formal definition in
the six pages.

**What the article does support, in prose. p. 146:** *"The tonic of a key, if present, may be
represented as an absolute PC or again relative to another tonic or key, e.g., **for secondary
dominants and other chord borrowings, or for indicating a local key**. **Various levels of a tonal
hierarchy may be disambiguated by a "Type" feature on the key.**"*

**So the substance is CONFIRMED — a key carries an optional type feature, and the hierarchy levels the
prose names are the local key and the secondary-dominant/borrowing case.** **What is NOT ESTABLISHABLE
at the article is the quoted syntax and the closed three-value enumeration.** They may well be in the
supplementary material; **this pass has not opened it, and a claim may not be sourced to a document
nobody read.**

### ★ K2 — The "Figure 2 caption" quoted in the cross-check's decisive step is not the Figure 2 caption

**What the cross-check says** (§2, resolving its one apparent conflict, marked *decisively*): *"The
Figure 2 caption states that the graph 'displays the pitches on the score surface as Specific Pitch
Classes (SPC) with octave information' beside the derived properties."*

**At the object, Figure 2's caption reads in full: *"Sofia Gubaidulina, String Trio (1988), mvt. 1,
hexachord in mm. 27–37."*** Figure 3's caption is about the model's representation of the Corelli
chord and the pitch-type relations, and contains no such sentence either. **The quoted sentence is
not a caption in this article.**

**The claim it was cited for is nonetheless true**, and C2 above establishes it from the *Score Level*
paragraph and Figure 3a. **So the resolution stands and its evidence does not.** Recorded because a
later reader following the citation would find a Gubaidulina caption and conclude the resolution was
invented.

### ★ K3 — Two of the four "case studies" are not in the article

**What the cross-check carries** (§3): *"The four case studies and what each demonstrates — Corelli
(one Dorian chord in four notations), Dvořák (Riemannian and Tonfeld at once), a jazz chord whose
implicit pitches exceed its label, and a Gubaidulina hexachord with no traditional root, handled by a
'central tone'."*

**The article contains two: Corelli (Figure 1, and its graph at Figure 3a) and Gubaidulina (Figure 2,
and its graph at Figure 4).** The Dvořák and jazz cases appear only as a claim in the Conclusion —
**p. 147:** *"capable of expressing a variety of challenging analytical cases in a wide range of
styles including Western classical, late-Romantic,¹ Jazz,¹ and contemporary post-tonal music"* —
**where the superscript 1 on "late-Romantic" and "Jazz" is footnote 1, the supplementary material.**
**The two cases are named and located outside the article, not shown in it.**

**The Corelli and Gubaidulina descriptions are CONFIRMED** — the Corelli chord is annotated in four
systems at Figure 1 and the passage is in C Dorian; the Gubaidulina hexachord *"defies analytical
categories linked to triadic music, such as the root of a stack of thirds. The central note of the
chord is D4"* (pp. 144–145), and Figure 4 attaches *"the 'Central Tone' function to D as provided by
an analyst"*.

---

## What this row does NOT establish

- **No tabulated value was verified**; the paper has none (C7).
- **Nothing about DP-D's verdict**, recorded because the user's ruling holds that question open across
  the seven. **Row 3's bearing on DP-D is exactly the fence the surface already records: none in
  either direction** (C4). That is now established at the object rather than by a prompted question.
- **Nothing from the supplementary material or the repository.** Opening it as design input is outside
  this commission's licence, and K1 and K3 are recorded as unestablished rather than chased.

## Verdict for the row

**Eight load-bearing structural claims CONFIRMED, two of them at a better grade than before (DP-N's
absence and DP-D's fence, both now from a whole read rather than a prompted question). Three NOT
ESTABLISHABLE — a BNF quotation, a figure caption and two case studies, none of them at the place
cited, all with their substance confirmed from the article's own prose or recorded as living in
material nobody read. No falsifier candidate. No STOP.**

**★ The pattern is worth naming.** All three are the same error: **material from the supplementary
repository, or invented in its shape, cited as the paper's** — in a cross-check that itself records
that neither pass opened that repository. It is the fourth row of five in which the doubled reading's
resolution is less reliable than the resolution's own confidence, and the first in which the defect is
**a source that does not exist at the citation** rather than a misreading of one that does.

*Provenance: read 2026-08-31 at `docs/research_papers/reading_pass_2026_08/mec-chord-model.pdf`, all
six pages as page images, staged through the bridge and read with the file tools. The first-pass
extract and the cross-check were read at the file first, to enumerate. No shell was run on the
repository or on any staged copy of it. The supplementary material and the code repository were NOT
opened. No specification derived, no document amended, no code opened, no register row or entry
written.*
