# Task A, row 1 — McLeod & Rohrmeier 2021, the modular harmonic analyzer — AT THE OBJECT

> **STATUS: TARGETED RE-READ, AT THE OBJECT, 2026-08-31.** Executing §2 of
> `cowork_reading_pass_remedial_commission_2026_08_31.md`. **All eight pages read as page images
> with the file tools**, from the PDF the user supplied at
> `docs/research_papers/reading_pass_2026_08/ismir-harmony.pdf`, staged through the bridge. **No
> web-fetch read of any kind was used on this row.** This is a targeted re-read of the existing
> extracts' load-bearing structural claims, **not a third extraction**; tabulated values are outside
> its scope by the commission's own words. **Nothing of the findings surface is edited here.**
>
> **Locations are PDF page numbers of that file. The pages carry no printed page number** — that is
> stated rather than left implicit, because a citation to "p. 3" of this paper means the third page
> of the file and nothing the paper prints.

## What was enumerated, and from where

The claims below are every claim of `reading_pass/extracts/…`, `…/extracts_second_pass/…` and
`…/cross_checks/…` for this row that is **structural** — how the method decides, what it decides
jointly or in stages, what it assumes and hands on — **and** carries load in
`cowork_reading_pass_findings_2026_08_31.md`: in a design point's verdict (§2), in the §3.1 coupling
table, in the §3.2 chain, or in the §5 routed extracts. Tabulated values (Table 1's CSR figures, the
per-inversion accuracies, the mode split) are excluded by the commission. They were nonetheless
seen at the pages in passing and **none diverged**; that is recorded and not counted as a
verification.

## The verdicts

### C1 — The chord label is decided over whole absolute symbols, not per-field, and the paper states the reason — **CONFIRMED**

Carries **DP-A's SUPPORTS verdict**, where the findings surface calls it *"a primary-source
statement of DP-A's ground by authors who chose the holistic form on it."*

At **PDF p. 3**, right column, in full: *"It would be possible to treat each aspect of a chord symbol
(root, type, and inversion) as a separate feature of each chord, and have the CCM output one
distribution over each, as has been done in previous work (e.g., [24,26]). However, while this
approach makes sense in terms of reducing the size of a model, it doesn't make sense conceptually:
there may be a situation in which the model sees a C in the bass, and thinks the chord is either a C
major triad in root position or an A minor 7th chord in 1st inversion. In cases such as this, it is
important that every feature of a chord is considered holistically as a unit, rather than
potentially classifying the chord as a C minor 7th chord in 1st inversion."*

**The surface's quotation is exact and its worked case is the paper's own.** The distribution is over
all 1540 absolute chord symbols (PDF p. 2, §2.2; p. 3).

**One addition the surface does not carry, recorded because it strengthens the same point:** the
paper names the per-field form as what *previous work* does and cites it — references [24] and [26],
which its reference list gives as Micchi, Gotham & Giraud 2020 and Chen & Su's Harmony Transformer
(PDF pp. 7–8). The lineage DP-A reads as its rival is the lineage this paper names as the rival.

### C2 — A standalone boundary model over-segmented, and a merge rule was added — **CONFIRMED, with a nuance that sharpens DP-C rather than weakening it**

Carries **DP-C's SUPPORTS verdict** — the findings surface calls it *"direct primary evidence about
boundary-first designs"* — and appears again in §5's routed extracts to the L2 detail specification.

At **PDF p. 4**, right column, verbatim: *"we noticed that the CTM was over-segmenting the input, and
the thresholds were difficult to tune. However, the CCM's outputs were relatively accurate."* The
merge rule is defined immediately above it: it is *"legal for two consecutive chord windows c_m and
c_{m+1} to be merged if: (1) the resulting chord window's duration … is still less than C_dur_max;
and (2) Ch(c_m) = Ch(c_{m+1})"*, and it *"can be repeated as many times as possible as long as the
two constraints are still met."* **The surface's statement of the merge condition is exact.**

**★ The nuance, and it is a finding of this re-read.** The surface reads the merge rule as *"a repair
bolted after it."* The paper's own next sentence says what the repair is FOR: *"Thus, we created the
merge rule, which allows us to tune the CTM thresholds to over-transition, letting the more accurate
CCM merge windows later."* So the over-segmentation is not merely a fault that had to be patched —
once the merge rule exists the authors **deliberately tune the boundary model to over-produce
boundaries** and let the chord-classifying stage settle which survive. **That is a stronger form of
DP-C's own position than the surface states**: the working system's answer to an untunable standalone
boundary model is to stop asking it to decide and to let the later, better-informed step decide.
The paper frames the rule as *"another example of the interpretability of our system helping in its
development"* (PDF p. 4). **No verdict moves; the ground under DP-C's SUPPORTS is firmer than it was
recorded as.**

### C3 — The system does not commit the boundary model's segmentation; windows, chords and keys are decoded together — **CONFIRMED**

**This is the single question the read tool answered backwards in one prompted read of three**
(`population.md` §3b; the cross-check's §2.7), and it is the question DP-C turns on. It is now read
at the object.

At **PDF p. 4**, §2.4 Inference: the CTM's outputs define which windows are *valid* — six stated
conditions, of which (1)–(3) are thresholds on the CTM's own values and (4)–(6) are duration and
well-formedness constraints — and then: *"Having found all possible chord windows, the search process
involves finding the most probable complete and labeled path through the score."* A labeled path
assigns **both** a chord and a key to every window, and the path probability (Eqn. 1) multiplies the
CTM, CCM, KTM and sequence probabilities together over the whole path, normalised by window count.
*"We explore the search space iteratively using beam search decoding."*

**The surface's sentence and its quotation are exact.** The CTM constrains legality; it does not
decide the segmentation.

### C4 — Applied chords are represented as brief, potentially recursively embedded key changes — **CONFIRMED**

Carries **DP-E's SUPPORTS verdict** and part of **DP-L's**.

At **PDF p. 2**, §2.1, verbatim: *"Our model does not output applied chords (e.g., secondary
dominants like V/V) directly. Rather, we treat them as brief, potentially recursively embedded, key
changes as in [25]."* Reference [25] is Rohrmeier's jazz-harmony syntax paper (PDF p. 8) — the
device is adopted from a named source, which the surface does not say and which is recorded here.

The worked example at **PDF p. 6**, Figure 2, shows the behaviour: the applied dominant V2/IV in
Grieg's Notturno is found *"as a key change to F"*.

### C5 — The input is spelled, and requires the metrical level of each note's onset and offset — **CONFIRMED**

Carries **DP-F/DP-G/DP-H's SUPPORTS verdict** and the upstream half of the §3.1 coupling table.

At **PDF p. 1**, §1: *"We also use spelled pitches (where an A♯ is a different pitch from a B♭),
which is still uncommon in existing work."* **Both quoted fragments are exact.** The abstract states
the same choice as *"not treating enharmonically equivalent pitches as identical"*.

At **PDF p. 3**, §2.3, the CTM's note encoding includes *"the metrical levels of the note's onset and
offset positions (downbeat, beat, sub-beat, or other; two one-hots of length 4)"* — **the surface's
"metrical level of each note's onset and offset" is exact.**

**One addition to the coupling table's upstream cell, which is a summary rather than an error.** The
same encoding also requires the note's octave, its normalised MIDI pitch height, its duration, and
the durations from its onset to the previous and following note's onsets (PDF p. 3). Every one of
those is derivable from what L0 gives, so nothing crosses the boundary that the framework's L0 does
not publish — **the cell is incomplete, not wrong**, and this file records the fuller list so a
detail specification does not have to re-read the paper for it.

### C6 — No key is required as input — **CONFIRMED**

At **PDF p. 2**, §2.2: *"The system's input is a sequence of notes N ordered temporally by onset
position, where notes with equal onset position are ordered by increasing pitch."* Nothing further.
The first key is produced by the ICM in combination with the first absolute chord symbol (PDF p. 3),
so the key axis is inferred and not given. **The coupling table's "no key" is right.**

### C7 — What it hands downstream: segmentation, chord symbol and local key per span; no chord-tone assignment; no rivals — **CONFIRMED**

Carries the downstream half of the §3.1 coupling table, the *"L2, minus two of its four published
facts"* placement, **DP-K's** *"Rows 1, 12, 17, 18 and 19 publish no rivals at all"*, and §3.2's
*"Row 1 commits its best path."*

At the object: a labeled path assigns one chord and one key per window (PDF p. 4); Figure 2 (PDF p.
6) shows exactly one key row and one chord row under the score, with inversions written as figured
bass. **No alternative reading, mass, confidence or rival is published anywhere in the paper.** The
beam holds paths during search only.

**★ One addition, and it is the nearest thing in this paper to publishing an alternative — it is not
one.** At **PDF p. 6**, §4: *"We also intend to design a human-in-the-loop annotation tool using this
system, where expert annotators can first get the system's output, change some labels as they see
fit, and then re-run the search process, constraining the system to a path that includes the
manually corrected labels."* That is a **constrained re-decode**, not a rival stream: the correction
comes from outside the system and the system still publishes one path. **DP-K's reading of this row
is unchanged and now rests on the pages.**

### C8 — Suspensions, altered chordal tones and pedal tones are absent and are named future work — **CONFIRMED**

Carries §3.2's chain claim that *"row 1 names suspensions and altered tones as future work and row 2
delivers them."*

At **PDF p. 1**, §1: *"our system's output is nearly equivalent to a full RNA, lacking only altered
chordal tones such as suspensions, and pedal tones, which we intend to include in future work."*
**Exact.**

### C9 — The line-of-fifths encoding of relative root and bass, −14–14, two one-hots of length 29 — **CONFIRMED**

Carries a §5 routed extract to the L2 detail specification.

At **PDF p. 3**, right column: *"the root pitch class and bass note pitch class, each represented as
the interval above the key tonic on the line of fifths (-14–14; two one-hots of length 29)"*.
**The surface's quotation is exact.**

### C10 — The initial-chord prior is count-based with additive smoothing — **CONFIRMED**

Carries a §5 routed extract.

At **PDF p. 4**, left column: *"The ICM is a much simpler model than the rest, and we simply count the
proportion of each chord—grouped by chord type, inversion, and relative root—as the first chord of a
piece in our training data. We then apply additive smoothing to this estimate, adding 1/1540 (where
1540 is the number of chords in our vocabulary) to each count."* **Exact**, and it confirms the
second pass's addition that the ICM is not a network.

### C11 — The authors' own diagnosis of key-error inheritance as a cost of modularity — **CONFIRMED**

Carries the first extract's DP-A and DP-B bearing.

At **PDF p. 5**, §3.2, verbatim: *"Interestingly, the baseline performs relatively well on key
detection (even on our internal corpus), which points to one downside of our modular approach: the
key depends on outputs from the other components, adding noise to the process, which isn't a factor
for the end-to-end baseline."* **Exact.**

---

## ★ C12 — The cross-check's one explicitly UNRESOLVED item is now RESOLVED, and its resolution CORRECTS the cross-check

**This is the row's one CORRECTED verdict. It is NOT a falsifier candidate** — it moves no design
point's verdict and touches no SUPPORTS or rival-defusal — but it is exactly the class of thing this
commission exists to find, and it corrects a judgment rather than a fact.

**What the cross-check says** (§2.3): the first extract's phrase *"the ±14-fifths bounded key
transitions"* is *"confirmed in its object but mis-attached in its phrasing"*, because the quotation
found was the encoding of a relative chord's root and bass; and it records **"UNRESOLVED as to
whether key transitions carry a fifths bound of their own"**, sending a later reader to the paper's
key-model section.

**What the pages say.** The key-model section carries a ±14 line-of-fifths bound of its own, twice,
both at **PDF p. 3**, right column:

- the key-change vector appended at a key change encodes *"the tonic of the new key, represented as
  the interval above the previous key's tonic on the line of fifths (-14–14; one-hot of length 29);
  the mode (major or minor; one-hot of length 2); and a flag indicating that this is a key change"*;
- and the KSM's **output** is *"a distribution over key symbols consisting of a tonic (-14–14 on the
  line of fifths from the previous key tonic) and a mode (58 keys in total)"* — 58 being the 29
  reachable tonics in both modes. Key changes outside that range are *"invalid"* or *"uncovered"* and
  are *"treated in the same way"* as the out-of-range chords described beside them, whose prior *"is
  0"*.

**So key transitions ARE bounded to ±14 fifths from the previous key's tonic, and the first pass's
phrase was right about the object as well as the number.** The cross-check's "mis-attached" reading
is **CORRECTED**, and its UNRESOLVED item is **CLOSED at the pages**.

**Why it is worth the space.** The ±14 bound is a routed input to the L2 detail specification. Left
as the cross-check left it, a later reader would have carried the encoding bound and **not** the
transition bound, and would have had to re-open the paper to find that the key axis is reachability-
bounded at all — which is a claim about what the search can reach, and therefore R-5's territory.

---

## What this row does NOT establish

- **No tabulated value was verified**, by the commission's own exclusion. The values seen in passing
  agreed with the extracts; that is an observation, not a verification.
- **The confusion matrix (Figure 3), Figure 4's per-mode split and the training details of §3.1**
  were read but carry no load anywhere in the findings surface and are not enumerated here.
- **Nothing about the implementation repository** — the disposition surface's relayed claim about
  MuseScore3 files remains unestablished, as the first-pass content record already says; the paper
  gives only the code URL (PDF p. 6, footnote 3).

## Verdict for the row

**Eleven load-bearing structural claims CONFIRMED at the pages, with two additions that sharpen the
ground under DP-C and DP-A. One CORRECTED verdict, against the cross-check's own resolution and not
against any design point. No falsifier candidate. No STOP.**

*Provenance: read 2026-08-31 at `docs/research_papers/reading_pass_2026_08/ismir-harmony.pdf`, all
eight pages as page images, staged through the bridge and read with the file tools. Both extracts and
the cross-check for this row were read at the file first, to enumerate. No shell was run on the
repository or on any staged copy of it. No specification derived, no document amended, no code
opened, no register row or entry written.*
