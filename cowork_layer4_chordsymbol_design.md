# Architectural Layer 4 — CHORD SYMBOL (with NON-CHORD TONES) — Architecture & Design

> **Status: SIGNED (user, 2026-06-24)** — the revision of the 2026-06-22 sign-off, approved after the spec review
> (`cowork_layer4_spec_review.md`) and the language sweeps (`cowork_spec_language_sweep.md`,
> `cowork_layer3_spec_language_sweep.md`). It corrects three faults: the thin-evidence path was specified only by
> preference, not by rule (the hole the phantom-root defect fell through); the prose reached into the source; and it
> carried invented vocabulary. The build state and the mapping onto existing source live in the delivery plan, not
> here — this document reads the same whether or not anything has been built.
> **★ AS-BUILT (2026-06-26): this spec is now realised** — `chord/chordslicedecoder.{h,cpp}` implements G1
> (commit/inherit/abstain + ≥3-template-tone sufficiency), G2/G3 three-tier membership + plausibility, the §4 two-reading
> both-sides inherit, G6 (confidence + the open-question L4→L5 contract), and the G4/C1 symmetric-root spelling-pin
> (consuming `engravingbridge::spellingview`). It is **built but DORMANT** — production still runs legacy
> `analyzeChord`/`ChordPathDecoder`; the **engage-with-L5** strategy defers the production switch + legacy retirement to
> the joint L4+L5 step (measured: better where it commits; ~85% of its abstention genuinely function-dependent → L5).
> §15-O2 (bounded-window joint) + C2 (new four-note types) are deferred to the engage step. Build state:
> `cowork_phase5b_l4_build_plan.md`.
>
> **Open item O1 is resolved (user-ratified 2026-06-24, see §15):** the step that resolves a slice marked "uncertain"
> is **Architectural Layer 5 (function) itself** — there is no distinct box between the note-layers and Layer 5. Layer
> 5 resolves the carried readings at its gated entry, as part of assigning function. This document names it
> "Architectural Layer 5" throughout, identically with the Layer-3 spec. (Evidence: `cowork_uncertain_resolver_investigation.md`
> + the part-3 measurement, Cowork-verified at the score.)
>
> *(Two template sections do not apply: "Deployment view" and "Human-interface design" — backend analysis code, no
> separate deployment, no user interface.)*

## 1. Introduction & purpose

**What Architectural Layer 4 is.** For each slice produced by Architectural Layer 2 it names the **chord symbol** (for
example `Bm7`, `Gdim`, `C`) **and** decides, for every note sounding in that slice, whether the note belongs to that
chord (a **chord tone**) or not (a **non-chord tone**). It treats these as **one** decision, because the symbol cannot
be named without deciding which notes belong to it: the slice `{C, E, G, D}` is `C major` with `D` a passing
non-chord tone **or** `Cadd9` with `D` a chord tone, and which reading is right *is* the membership decision.

**What music it operates on.** The slices from Architectural Layer 2, over the notes from Architectural Layer 1, with
the key/mode from Architectural Layer 3 available as a preference, for the user-selected part of the score.

**Why it commits where it can and abstains where it cannot.** A slice's sounding pitches are rarely all chord tones —
a passing note, a neighbour, a suspension all sound *inside* a slice without belonging to its chord. Where the notes
(helped by the key preference and the neighbouring chords) determine a chord, the layer names it. Where they do not —
too few notes to fix a chord, or two readings that only function or spelling can separate — the layer **does not
guess**: it marks the slice "uncertain," records which question is open and the competing readings, and hands that
forward. Knowing *where the note evidence runs out* is part of this layer's job; the "uncertain" mark is the explicit
hand-off.

**The responsibility boundary.** Architectural Layer 4 owns the contribution of the **note evidence** — the slice's
pitches, their notated spelling, their metric weight, and the immediately neighbouring chords — to the
chord-and-membership question, with the key/mode used as a **preference** (a lean toward the diatonic reading, never a
determinant). It resolves everything the notes and that preference can resolve. It does **not** own the final
arbitration of the cases the notes and key alone cannot decide: the **symmetric sonorities** whose root is undefined
by pitch class and unfixed by spelling (a MIDI-imported diminished-seventh), and the chords whose reading turns on
**function** (a passing diminished versus a real applied chord). That residual is handed forward — as the competing
readings plus the "uncertain" mark naming what is open — to Architectural Layer 5, which resolves it by **selecting
among the readings this layer carried**, never by inventing a chord or re-deriving one from the raw notes.

**Scope — what it does:** assign each slice a chord symbol (root, quality, and bass/inversion), a chord-tone set, a
non-chord-tone set, the ranked competing readings, a confidence, and an "uncertain" mark (naming the open question)
where the evidence does not decide.

**What it explicitly does NOT do:**

- It does **not** name **function** or Roman/Nashville numerals — that is the chord symbol read *in* the key, decided
  by Architectural Layer 5.
- It does **not** decide the **key/mode** (Architectural Layer 3); it consumes the key as a preference and never feeds
  a chord decision back into key, except through Architectural Layer 5.
- It does **not** detect **cadences** (a function-level event, Architectural Layer 5), and does **not** group equal
  slices for display (Architectural Layer 6), and does **not** read or change the notes or slices (Architectural
  Layers 1 and 2).
- It does **not** classify the **type** of a non-chord tone (passing, neighbour, suspension, anticipation): naming the
  chord needs only the chord-tone-versus-non-chord-tone call; the type label is a separable later annotation.
- It does **not** analyse **voice-leading across the progression** (a separable, later concern). It *does* use the
  **local** stepwise treatment of a note within its window — a note approached and left by step is embellishment-like —
  as one membership cue; that is a property of the single note in its window, not an analysis of the progression.
- It does **not** re-derive a chord from a **pooled bag of several slices' notes**. This prohibition is stated once,
  authoritatively, in §8 ("Never a pooled recompute") and referenced thereafter.

**Which chords it recognizes.** Any chord built by stacking thirds. A chord is named in three pieces:

- **the root** — the note the chord is built on (each of the twelve pitch classes is tried);
- **the basic quality** — the pattern of thirds on that root: one of the four **triads** (major, minor, diminished,
  augmented) or the six **seventh chords** (dominant, major, minor, half-diminished, diminished-seventh, minor-major);
- **the added notes** — any sixth, ninth, eleventh, thirteenth, or altered tone above the basic quality, read off the
  membership decision (§5), not matched as a separate thing.

So the recognized vocabulary is *(every quality) × (every root) × (whatever added notes membership finds)* — large by
construction (`C6`, `Am7`, `Cmaj9`, `G7♭9`, …). `C6` is a major-quality chord on C whose chord tones happen to include
the sixth; it is not stored anywhere as "`C6`."

**The stored list is a catalogue of chord *types*, not of finished chords.** It holds one entry per **quality** — an
interval pattern such as *root, major third, perfect fifth* — matched at every root and scored. **Inversion and
note-order are factored out by construction:** a pattern is a *set* of intervals (order-independent), tried at the
twelve roots, with the bass tracked separately, so neither multiplies the entries. What is deliberately **not** in the
catalogue is the added notes (sixths, ninths, suspensions): established practice finds that folding these into the
chord vocabulary degrades recognition, so the standard recipe is **a small catalogue of basic types plus recovering
the added notes afterward** (§14) — which is exactly this layer's membership decision. The catalogue stays small and
clean; the recognized vocabulary is far larger.

**Which chords it does NOT recognize.** Non-tertian sonorities — quartal/quintal chords, secundal clusters, anything
not expressible as stacked thirds. A passage genuinely in one of these is reported as the **closest** recognized
tertian chord, or marked "uncertain," never as the unrecognized construction.

## 2. Constraints

- **Minimality (the governing principle, stated once).** Architectural Layer 4 settles only what the notes and the key
  preference decide, and **defers every separable sub-problem**: the unfixable symmetric-sonority root (→ the later
  function step), the non-chord-tone *type* (→ a later annotation), and voice-leading across the progression (→ a
  relational later concern). Whatever can stand alone with its own evidence is not done here.
- **Maximal information — use the notated spelling, not bare pitch class.** Within its question the layer uses **all**
  the note information Architectural Layer 1 carries, most importantly the **notated spelling** (the tonal pitch class,
  `G♯` versus `A♭`), which names a chord's root where pitch class cannot — decisively for the symmetric sonorities. It
  is a strong-but-fallible signal (engraving can be expedient; a MIDI import may carry arbitrary spelling), so it is
  weighed, not trusted blindly, by the precedence ladder in §5.
- **Chord symbol and chord-tone membership only.** The evidence it may use is the **notes** (which pitches sound, their
  notated spelling, their metric weight), the **key/mode** (a preference), and the **immediately neighbouring chords**
  (its own decisions, so an embellishment slice does not spawn a new symbol). It may **not** use function, cadence, or
  any already-decided downstream result.
- **The key is a preference, not a determinant.** The notes are primary; the key preference tips a reading only when
  the notes leave it close (the precedence ladder, §5), and is itself weakened when Architectural Layer 3 marked the
  key "uncertain."
- **Its output states its own certainty, and what is uncertain.** Where the evidence decides, it commits; where it
  does not, it records the competing readings, marks the slice "uncertain," and **names which question is open** — the
  root, the quality, or a specific note's membership.
- **It reads each slice with a window that extends only as far as the slice's own chord.** The window starts at the
  slice and its immediate neighbours and extends across contiguous neighbouring slices **while they continue to
  support one consistent chord reading**, stopping at the first slice whose notes are inconsistent with that reading.
  That first inconsistent boundary is the operational meaning of "the slice's chord is now fully in view"; the window
  never reaches past it, because the *next* chord is progression reasoning and belongs to Architectural Layer 5. The
  stop condition is stated here once and referenced in §4–§5.
- **Bounded context at the selection edge (`cowork_bounded_context_design.md`).** The window must **not assume a
  neighbour slice exists.** When it would reach beyond the currently-loaded span — at the edge of the user's
  selection — Architectural Layer 4 either **requests an extension** (one harmony's worth, the same bound as the stop
  condition above) or, if Architectural Layer 1 reports the **score boundary**, proceeds with the truncated window. A
  slice at the very start or end of the piece simply has one fewer neighbour; a slice at the edge of a *selection* (not
  of the score) reaches for the missing context rather than guessing without it. This contract is fixed now so the
  layer is built to bounded context, never to "the whole score is always loaded."
- **It changes analysis output** (unlike Architectural Layers 1 and 2), so it is judged by accuracy measurement, not by
  identical output; the pinned analysis snapshots are refreshed only after a change is confirmed correct.
- **Works on the user's selected music, at any size and in any style** (its *structure* assumes no style). The style
  preset enters as a **weak preference on the likely chord vocabulary** — Baroque expects triads and sevenths; Jazz
  raises the extended and altered chords; "Standard" sits between — overridden by clear note evidence.
- **It does not notice score edits** — deciding the analysis is stale is the caller's job.

## 3. Context & scope (external view)

**What it reads (inputs):** the slices from Architectural Layer 2; the notes from Architectural Layer 1 (each slice's
pitches, their notated spelling, their metric weight, and the immediately neighbouring slices); the key/mode from
Architectural Layer 3 (the chosen key plus its competing keys and "uncertain" mark) as a preference; its own
neighbouring chord decisions (for embellishment context); the style preset; and its own tunable settings.

**What it offers (operations other code calls):**

- *Name the chord-and-membership for each slice* — given the slices, the notes, and the key, return one result per
  slice: the chosen symbol, its chord-tone set, its non-chord-tone set, the competing readings, a confidence, and the
  "uncertain" mark with its open-question label.
- *Re-name a sub-range* — re-run the naming over part of the sequence after a small edit, consistent with the
  incremental contract of the layers below.

**Who uses it (consumers):** Architectural Layer 5 (function — reads each slice's chord symbol *in* the key);
Architectural Layer 6 (grouping — merges adjacent slices carrying the same chord-and-membership); and the later
function step that resolves the slices marked "uncertain."

**What it deliberately does not read:** function, cadences, or any already-decided downstream result fed back to it.

**Implementation locator** *(current location, under revision against this spec — the layer is mid-rebuild).* The
chord scorer and the per-slice chord decoder live under `src/composing/analysis/chord/`
(`chordanalyzer.{h,cpp}`, `chordslicedecoder.{h,cpp}`).

## 4. Solution strategy

Read the slices left to right, each within its window (§2). For each slice, in two readings:

1. **List the possible chords.** From the slice's pitches, generate **every** tertian chord the pitches could spell —
   each basic type at each root — and score each by how well the pitches fit it. **Completeness is the priority:** a
   chord never listed can never be chosen, and the measured dominant error is "the right chord was never on the list,"
   not "the wrong one was picked among good options." The fit measure is the one stated in §5 (present chord tones
   credited; absent ones a mild shortfall; extra notes carried to the membership decision, not penalised as wrong
   pitches).
2. **Decide membership together with the symbol.** A candidate chord implies which notes are chord tones and which are
   left over; each left-over note is judged chord-tone versus non-chord-tone by the rule in §5. The symbol and the
   membership are chosen together — the reading that best explains the slice as *a chord plus its embellishments* — and
   the membership feeds back into the score (a reading that needs implausible chord tones, defined in §5, is
   penalised). The added notes fall out of this: a chord tone above the basic triad or seventh *is* the sixth/ninth.
3. **Commit, inherit, or abstain.** Pick the highest-scoring chord-and-membership and test it against the two
   certainty conditions in §5: if the slice has enough independent chord tones and a clear-enough winner, **commit**
   it; if it does not have enough notes to fix a chord but its notes are consistent with the prevailing chord,
   **inherit** the prevailing chord; otherwise **abstain** — mark "uncertain," name the open question, and carry the
   competing readings. **A new symbol is never committed from too few notes** (this is the rule the phantom-root defect
   violated).

**The first and second readings.** Membership and the inherit/abstain test both need the neighbouring chords, which
are this layer's own output — a chicken-and-egg, resolved in two readings. The **first reading** names each slice from
its own pitches and the key preference **alone** (there are no decided neighbours yet, so neither the prevailing-chord
preference nor the inheritance fallback applies). The **second reading** re-decides each slice using the now-available
provisional neighbours on **both** sides — which is what passing-tone detection and the inheritance fallback need (a
passing tone is defined by the chord it leaves *and* the chord it resolves to). The prevailing-chord preference and the
"inherit on insufficiency" fallback therefore act **only on the second reading**; a phantom named on a thin slice in
the first reading is corrected to the prevailing chord (or to "uncertain") in the second. One refinement reading is the
baseline; a more precise bounded-window alternative is a flagged later refinement (§15).

This stays inside the layer: it uses the neighbour chords *as context*, never a chord-to-chord transition cost or
progression grammar (that is Architectural Layer 5).

## 5. Building-block view (the internal rules)

The naming has four parts; the third and fourth carry the decision rules the review found missing.

1. **Listing the possible chords.** Match the sounding notes against each basic chord type at each root, producing the
   candidates the notes could express, each with a **fit score**: present chord tones credited, a chord tone absent
   from the slice counted as a *mild* shortfall (smaller than a wrong note, so an incomplete chord still matches its
   plausible completions rather than failing), and a sounding note not in the candidate carried to the membership
   decision rather than scored as a wrong pitch. Added notes (sixths, ninths) are not candidate types — they come out
   of membership.
2. **The key and prevailing-chord preferences.** Adjust each candidate's score by the key (a lean toward diatonic
   chords *only* when the notes leave readings close; weaker when the key is itself "uncertain") and, on the second
   reading, by the prevailing chord (a lean toward continuing the current chord across a metrically weak slice).

3. **The membership decision — stepwise structure decides; metric weight is the tie-breaker, not a co-equal cue.**
   The question for each sounding note is whether it behaves as a **chord tone** or as an **embellishment** (a
   non-chord tone), read from its melodic motion within the window. The decisive signal is **stepwise structure**, in
   three tiers — and metric weight enters **only** at the third:
   - **Stepwise-embellishing → non-chord tone, *regardless of metric weight*.** A note approached **and** left by step
     between chord tones (a passing or neighbour tone), or held over from the previous chord and resolving down by step
     into a chord tone (a suspension), is a non-chord tone — *even on a strong beat*. This is the **accented passing
     tone**, which metric weight alone would misclassify as a chord tone; stepwise structure overrides the weight.
   - **No stepwise connection → chord-tone extension, *regardless of metric weight*.** A note reached **and** left by
     leap is a structural member — an arpeggiated chord tone — *even when metrically weak*. This is the **weak leap**,
     which metric weight alone would wrongly call an embellishment.
   - **Stepwise on one side only → the boundary case, decided by metric weight and the prevailing chord.** An
     appoggiatura (leapt to, resolved by step), an escape tone (approached by step, left by leap), or an incomplete
     neighbour: a note foreign to a **clear prevailing chord** that is **metrically weak**, or that resolves by step
     into a chord tone, is a non-chord tone; a **metrically asserted** (strong or sustained) note consonant with the
     candidate is a chord-tone extension.

   So both-sides-stepwise and no-side-stepwise are settled by structure alone; metric weight adjudicates **only** the
   one-sided case. (What counts as "a step," "weak," and "a clear prevailing chord" are tunable thresholds; the
   three-tier rule itself is fixed.) The added notes (6th/9th/…) fall out of this — an extra note classified a chord
   tone simply *is* the extension.

   **The same test applied to a *required* (template) tone is the plausibility check.** A candidate's own chord tones
   are run through the identical classification: a template tone that behaves as an embellishment (tier 1,
   stepwise-embellishing) makes the candidate **implausible** — it is forcing a passing tone to be a chord member (the
   reading that hears the passing `D` of `C–E–G–D` as a chord tone of `Cadd9`, or the passing seventh of a triad as a
   real seventh). A candidate needing many such implausible chord tones is penalised; this is the "**implausible chord
   tones**" penalty named in §4 step 2, and it is exactly what discriminates `C` from `Cadd9` and a triad from a
   spurious seventh. (Template tones are therefore **not** exempt from the behaviour test — testing them *is* the
   plausibility penalty.)

4. **Commit / inherit / abstain, and result assembly.** Apply the two certainty conditions:
   - **Sufficiency** — does the slice contain enough independent chord tones to fix a chord, namely at least a complete
     triad's worth (three distinct chord tones) after the window has gathered and membership has removed the non-chord
     tones?
   - **Margin** — does the chosen reading beat the best *different* (root, quality) reading by more than the certainty
     margin?
   A slice that passes **both** is **committed**. A slice that fails **sufficiency** but whose notes are all consistent
   with the prevailing chord (each sounding note is one of its chord tones or a stepwise embellishment of it)
   **inherits** the prevailing chord. Any other slice — failing sufficiency with no consistent prevailing chord, or
   passing sufficiency but failing margin — is marked **"uncertain,"** with the open question named (root, quality, or a
   specific note's membership) and the competing readings carried. Then assemble the per-slice result.

**Symmetric sonorities — pin the root from the notated spelling; defer only the unfixable remainder.** A symmetric
diminished-seventh or augmented chord has no pitch-class-defined root — every rotation is equally spaced — but the
**notated spelling** usually names it: spelled `G♯–B–D–F` it is `G♯` diminished-seventh, spelled `A♯–C♯–E–G` it is
`A♯`. So the layer reads the spelling and **pins the root from it** where the spelling is present and internally
consistent (the common case, and deterministic — the spelling does not move with the key, so no rotation churn
arises). Only where the spelling is **absent or contradicts the other evidence** does it defer: name the quality and
bass, carry the rotations, mark "uncertain" (open question: the root), and leave the re-spelling judgment to the later
function step.

**Incomplete chords (too few notes to fix a chord).** A slice may sound only two notes — an open fifth, or a third
with no fifth. The layer names it from the evidence it owns, in this order: (1) **matching even when notes are
missing** lists the chords the dyad could complete to (step 1's mild-shortfall scoring); (2) the **key preference**
picks the likely quality from the root's scale degree when the sounding notes fit it; (3) on the second reading, the
**inheritance fallback** (step 4) keeps a dyad that is really an embellishment of the prevailing chord from spawning a
new symbol; (4) the **bass** anchors the inversion and the **metric weight** informs membership. Where these decide,
the chord is named or inherited; where they do not — a lone scale-degree pitch, or a bass-sharing pair whose reading
turns on function (`iii`↔`I6`, `V6`↔`vii°`) — the slice is marked "uncertain" with the open question named. The layer
does **not** reach for chord-progression grammar or voice-leading to complete the chord (minimality, §2).

**Arpeggios (a chord spelled one note at a time).** When a chord is arpeggiated, each note is its own thin slice whose
window (§2) gathers the figure's notes, so the chord emerges and each slice is named it or inherits it; Architectural
Layer 6 later groups the consecutive same-chord slices. The window's gathering is **governed by the membership rule**,
never a pooled recompute (§8): a run of notes forms a chord only when they are genuinely its chord tones — a melodic
line with passing tones must not inflate into a richer chord (`C–E–G–B` is a `Cmaj7` arpeggio *or* a `C` triad with a
passing `B`, decided by metric weight and the prevailing chord, and marked "uncertain" if neither decides). Only short
figuration within the window is named here; a phrase-length prolongation of one harmony is a reduction judgment beyond
this layer.

## 6. Runtime view (scenarios)

- **A clear triad slice:** the pitches fit one triad, all notes are chord tones → that symbol, committed, no
  non-chord tones.
- **A passing-tone slice:** `{C, E, G, D}` on a weak beat, `D` stepwise between `C` and `E`, the prevailing chord `C`
  → `C major` with `D` a non-chord tone (not `Cadd9`); the slice carries the neighbours' chord and groups away later.
- **A genuine seventh chord:** `{G, B, D, F}` sustained, `F` on a strong beat → `G7`, committed.
- **A thin slice (the phantom-root case):** a single sounding `C♯` over a passage whose prevailing chord is `A major`
  → the slice **inherits** `A major` (the `C♯` is its third), **not** a new `F♯` chord named from the lone note.
- **A thin slice with no consistent prevailing chord:** a lone pitch at a true harmonic boundary, neighbours
  themselves thin → marked **"uncertain"** (open question: the root), competing completions carried — never a guess.
- **A symmetric diminished seventh:** root pinned from the notated spelling where present (`G♯–B–D–F` → `G♯`
  diminished-seventh); where the spelling is absent or contradicted, marked "uncertain" (open question: the root) with
  the rotations carried.
- **A function-dependent reading** (passing diminished versus real applied chord): marked "uncertain" (open question:
  the quality/function reading), competing readings carried for Architectural Layer 5.

## 7. Data design

Each slice's result holds: the chosen **chord symbol** (root + quality + bass/inversion — the bass-versus-root
distinction is part of the symbol and is what the home metric scores); the **chord-tone set**; the **non-chord-tone
set** (chord-tone-versus-not only; the type is a later annotation); the **competing readings**; a **confidence**; and
the **"uncertain" mark with its open-question label** (root / quality / a named note's membership — so a downstream
selector knows *what* to resolve, not merely that something is open).

The **confidence** is composite, combining: the **margin** to the best different reading; the **sufficiency** (how
complete the committed chord is — a full seventh present versus a dyad completed by preference); and the **membership
cleanliness** (few contested notes versus many). A slice is "uncertain" when confidence is low for **either** reason —
low margin (ambiguity) **or** low sufficiency (insufficient evidence); these are independent, and a wide margin does
not rescue an insufficient slice.

Internally the decision uses, per slice, the listed candidates with their fit-plus-preference scores and the per-note
membership calls. The layer's settings — the recognized vocabulary (preset-dependent), the metric-weight and
stepwise thresholds, the window's extent, the strength of the key and prevailing-chord preferences, the sufficiency
count, and the certainty margin below which a slice is "uncertain" — are tunable values.

## 8. Crosscutting concepts

- **Certainty, and what is uncertain, are part of the output** — every slice carries the competing readings, a
  composite confidence, and (when uncertain) the named open question; ambiguity is recorded, never hidden, and it is
  what Architectural Layer 5 uses when it resolves the carried readings at its gated entry.
- **It annotates, it does not transform** — the slices and notes are unchanged; the chord and membership are added as
  annotations; the competing readings are kept so the decision can be revisited.
- **Never a pooled recompute** (the authoritative statement of this prohibition). Membership is judged per slice
  against the prevailing chord; the layer never pools several slices' pitches into one bag and re-derives a chord from
  the bag — that over-reads, treating every passing note as a chord tone, and was the failure that motivated the
  rebuild (§13). The note model stays the lossless source so membership is decided from the real notes, not a lossy
  aggregate.
- **Narrow context, forward from key** — the window is small and bounded by the slice's own chord (§2); the wide
  phrase-length context lives in key (Architectural Layer 3) and feeds forward as a preference. The only path by which
  a chord influences a key is Architectural Layer 5 — never a direct back-edge from this layer.
- **Forward-only resolution** — the genuinely undecidable slices are carried as competing readings plus "uncertain,"
  not forced; Architectural Layer 5 *selects* among them, it does not re-enter this layer.
- **Speed and incremental editing** — naming a slice is cheap (a small pitch set against the catalogue); each slice's
  reading is cached; re-naming only a sub-range keeps editing responsive.

## 9. Architecture decisions (with the alternatives weighed)

- **Chord symbol and chord-tone membership are ONE decision.** Alternative: name the symbol first, classify membership
  second. Chosen: one decision — the symbol and the membership co-determine each other (you cannot separate `C` from
  `Cadd9` without deciding the ninth's membership), and splitting them forces each half to guess the other.
- **Match only the basic chord type; the added notes come from membership.** Alternative (what the replaced code did):
  keep triads/sevenths as matched types and detect sixths/ninths as after-the-fact flags on the winner. Chosen: match
  only the basic types (with the diminished-seventh and minor-major as their own four-note types) and read the added
  notes off membership — a chord tone above the basic type simply *is* the added note. This avoids a blow-up of "type
  × every combination of extras," and gives the diminished-seventh its own type (the replaced code mishandled it as a
  diminished triad plus a flag, with no place to pin its spelled root).
- **List completely, then select — completeness is the lever.** Alternative: a strong re-scorer over a cheap, partial
  list. Chosen: complete listing, because the measured residual is overwhelmingly "the right chord was never listed,"
  not "the wrong one was picked." A learned re-scorer over the *complete* list is a later, secondary refinement (§11),
  never a substitute for listing completely.
- **Don't guess on thin evidence — gather, inherit, or abstain.** Alternative (what the implementation did): name the
  best-scoring chord on every slice regardless of how few notes support it. Chosen: a slice that cannot fix a chord
  from its own gathered notes either inherits the prevailing chord (when consistent) or is marked "uncertain" — a new
  symbol is committed only from enough notes (§5 step 4). This is the rule whose absence produced the phantom-root
  defect.
- **The key is a preference, fed forward — not a joint decision.** Alternative: decide key and chord together. Chosen:
  feed-forward (key → chord); the residual key↔chord coupling (relative major/minor, a passing-versus-real modulation)
  is handled by Architectural Layer 5, never folded in here.
- **Symmetric-sonority roots: read the spelling; defer only the unfixable remainder.** Alternatives: pin the rotation
  by voice-leading/key cleverness (rejected — reaches for relational evidence this layer should not own); or treat the
  analysis as spelling-blind and defer *every* symmetric root (rejected — discards information the score provides).
  Chosen: pin from the notated spelling where present and consistent, defer only the unspelled-or-contradicted
  remainder.
- **Only the chord-tone/non-chord-tone call here; the non-chord-tone TYPE is deferred.** Alternative: classify
  passing/neighbour/suspension here. Chosen: naming the chord needs only chord-tone-versus-not; the type is a
  separable later annotation.

## 10. Quality & testing

- **Compared against human analyses (the main judge).** The chord root and quality are compared against published
  analyses on a **held-out set** the layer was not tuned on. The bar: full agreement where the analyses are
  unambiguous; on the genuinely ambiguous cases, either the answer is among the defensible readings or the slice was
  marked "uncertain" with the right open question named.
- **The standing safety test, in plain terms.** The project's standing test requires that **no chord's functional
  root becomes wrong** (the meaningful errors never grow, on either tuning preset), while **tolerating churn among the
  symmetric sonorities** whose root pitch class cannot fix (a diminished-seventh's rotation is a coin-flip, not a
  quality measure). This split falls out of the design: the layer commits a root only where the notes-plus-spelling
  decide it and defers the unfixable symmetric root, so the metric naturally divides into the decidable roots (held to
  no regression) and the deferred symmetric ones (resolved only once Architectural Layer 5 settles them).
- **The standing root-error set is not the layer's residual — it overstates it several-fold (measured 2026-06-24).**
  The project's standing root-error set (the BIR=false cases) is mostly **Layer-1–4 work**, not what reaches
  Architectural Layer 5: a large majority is settled by the notated spelling (≈60% Baroque / ≈42% Jazz), and most of
  the rest by bass/inversion, local voice-leading, or is plain segmentation over-grab the change-point slicing removes
  by construction. The genuinely function-only remainder is **small** — pitch-class-identical share-tone chords on the
  chord side (for example Am6↔F♯ø7), and the whole note-identical key-disagreement class on the key side. So this set
  is read as a *budget of work across Layers 1–5*, not as a measure of this layer's accuracy; the layer's own number
  is the decidable-root agreement above, with membership and uncertainty scored separately.
- **Membership is measured in its own right.** Because the chord-tone/non-chord-tone call is the real lever (§11), its
  precision and recall against the human analyses' chord tones are scored separately, not folded into the chord-root
  number — chord-root alone would not reveal a membership regression.
- **Calibration of uncertainty is measured.** Whether the "uncertain" mark and the confidence land on the genuinely
  ambiguous and the genuinely insufficient slices, whether the named open question is correct, and whether the true
  chord is among the carried readings. This backs the claim that the layer is honest about what it does not know.
- **Behaviour tests** (independent of the corpus): a clean triad names one chord with no non-chord tones; a weak-beat
  passing note stays the neighbours' chord with the note flagged; a sustained strong-beat note above the triad is a
  chord tone (a sixth/ninth chord); a suspension is a non-chord tone; a thin slice over a clear prevailing chord
  **inherits** it; a thin slice with no consistent prevailing chord is **"uncertain"** (never a new symbol); a
  symmetric diminished seventh names quality+bass and is "uncertain" (root deferred) when the spelling is absent; a
  function-dependent reading is "uncertain."
- **Safety net (a hard stop):** the standing safety test above holds on both tuning presets; both automated test
  suites pass; pinned snapshots are refreshed only after a change is confirmed correct.
- **Test locator** *(current location, fixed once the rebuild against this spec lands).* The behaviour and decode
  tests live in the composing test suite; the held-out chord-root and membership grading runs through the read-only
  chord-decode diagnostic (`--decode-chords`).

## 11. Risks & technical debt

- **The chord axis is near its ceiling; the chord-tone/non-chord-tone call is the real lever.** Given good slices and
  a good key the chord-root residual is a few percent, so most remaining quality is in the membership call, whose cue
  combination (§5 step 3) and window (§2) are the main open tunables.
- **Complete listing is the priority risk.** A chord never listed can never be chosen; the listing (and its
  preset-dependent vocabulary) must be complete before any re-scoring is worth adding.
- **The unfixable symmetric root is deferred by design, not an open risk here.** The layer names quality+bass and
  carries the rotations as "uncertain"; the spelled root is resolved later. So the symmetric-rotation churn is
  *dissolved* here (no arbitrary root committed) and *resolved* at Architectural Layer 5.
- **A learned re-scorer is deferred** — a small re-scorer over the complete list is a later, separately-gated
  refinement (§14), gated on the per-event metric with out-of-sample discipline.
- **The accuracy numbers, and their definition, are provisional** until the full pipeline (through function and
  grouping) is rebuilt; the layer is judged by whether the genuine errors drop versus the replaced per-region path on
  the held-out set, not by a fixed target.

## 12. Glossary

*(Only terms used in a specific way — standard musical terms are assumed known.)*

**Chord symbol** — a chord named by its root, quality, and bass/inversion (`Bm7`, `Gdim`, `C`), independent of
key/function. **Chord tone** — a note of the slice that belongs to its chord. **Non-chord tone** — a note sounding in
the slice that is not part of its chord (passing, neighbour, suspension, anticipation). **Membership** — the per-note
chord-tone-versus-non-chord-tone call. **Listing the possible chords** — producing the complete set of chord symbols a
slice's pitches could express, before selection. **Re-scoring** — re-ranking an already-listed set (a later, secondary
step). **Rotation** — for a symmetric sonority, one of the equally-spaced choices of which note is the root.
**Prevailing chord** — the chord of the nearest preceding already-decided slice within the window. **Inherit** — to
take the prevailing chord as a thin slice's own answer when the slice's notes are all consistent with it. **Key
preference** — the lean toward chords belonging to the Architectural Layer 3 key, applied only when the notes leave
readings close. **Confidence** — the composite certainty number, combining the margin to the best different reading,
the evidence sufficiency, and the membership cleanliness. **Uncertain** — a slice the layer does not commit; it carries
the competing readings **and names which question is open** (the root, the quality, or a specific note's membership) so
Architectural Layer 5 knows what to resolve.

## 13. Background: what this layer replaces, and corrections on record (not needed to understand the layer)

- **What it replaces:** the per-region chord path — the template-based chord scorer run over coarse regions, followed
  by chord-dependent merge passes. It named a chord per coarse region rather than per constant-sonority slice, from a
  region-level aggregate of the tones.
- **Correction — the pooled over-reading.** An earlier approach re-derived a chord from a pooled bag of a region's
  tones; passing and neighbour notes entered the bag and inflated the chord. The correction is this layer's per-slice,
  prevailing-chord-aware membership decision — never a pooled recompute (§8).
- **Correction — listing, not re-scoring, is the lever.** An earlier lean toward a strong re-scorer was corrected by
  the measurement that the residual is mostly un-listed candidates, not mis-ranked ones.
- **On the key↔chord order:** chord is helped by key, not the reverse; naming the notes as a chord adds nothing the
  pitch content does not already carry for key-finding. So key is decided first and fed forward; the residual coupling
  lives in Architectural Layer 5.

## 14. Related work & external sources (what we borrowed, discarded, and why)

- **Chord and non-chord tones decided together** — Temperley/Melisma root-finding with ornamental-dissonance handling,
  and the joint chord-plus-per-note-membership formulation (JNMR 2024): naming the chord and classifying each note as
  one decision, the shape this layer takes.
- **Key-free chord identification** — Pardo & Birmingham: identifying chords from pitch content without committing to a
  key, supporting a symbol named from the notes with key only as a preference.
- **Label every event with context** — the Contrapunctus benchmark labels every beat (not coarse segments) with
  neighbour context and finds that, given the right key, the chord task is largely solved — which is why this layer is
  per-slice and neighbour-aware and treats the chord axis as near-ceiling with the membership call as the lever.
- **The catalogue holds types; the added notes are recovered, not stored** — template-based chord recognition
  (Erlangen FMP; Oudre, Févotte & Grenier, 2011) uses a small dictionary of chord *types* matched at every (root,
  type), inversion and order factored out. The explicit lesson (JNMR 2024, via Contrapunctus): added notes cannot be
  folded into the chord vocabulary without recognition degrading — so a small catalogue plus recovering the added
  notes afterward, which is this layer's membership decision.
- **Incomplete-chord handling** — Pardo & Birmingham's partial matching that credits present evidence and tolerates
  missing notes and, where a segment is ambiguous, carries *multiple labels* (the same carry-and-defer stance as our
  "uncertain"); and the key/scale preference for a sparse chord's quality (Temperley/Sleator), which also separates
  root-finding from key-finding, mirroring our layer split. We deliberately do **not** adopt Temperley's chord-level
  root-proximity smoothing here — that chord-sequence preference is a function-blind stand-in for progression, so by
  minimality it is deferred to Architectural Layer 5 (function). The genuinely function-dependent residual (bass-sharing `iii`↔`I6`,
  `V6`↔`vii°`) is an engine-independent floor (~7%, Contrapunctus), deferred here, not forced.
- **Deferred refinement — a small learned re-scorer** over the complete list (Contrapunctus reports a few points'
  gain), gated on the per-event metric with out-of-sample discipline — secondary, never a substitute for complete
  listing.
- **Considered and discarded:** a pooled-region recompute (over-reads, §13); a chord-first or joint key+chord base
  order (chord is helped-by but not needed-for key; the coupling is Architectural Layer 5); joint neural key+chord
  prediction (deferred to Architectural Layer 5, not used in this decomposed layer).
- **Corpora:** the Roman-numeral analysis corpora (When-in-Rome, DCML) for the chord-root and quality metric, read at
  the human analysis's event grain; a fixed held-out split; the project's Bach and Jazz tuning presets.

## 15. Open items & deferred refinements

- **O1 — the destination of "uncertain" (RESOLVED, user-ratified 2026-06-24).** The step that resolves a slice marked
  "uncertain" — selecting among the carried readings on functional/cadential evidence — **is Architectural Layer 5
  (function) itself**, performed at its gated entry; there is no distinct box between the note-layers and Layer 5. The
  reason is structural: the only single-slice note cues that exist (spelling, bass/inversion, metric weight, local
  voice-leading) are all already owned by Layers 1–4, so a case separable by a note cue is Layer-4 work and a case not
  so separable is function — leaving no third `(evidence × question)` for a separate box. The measured residual confirms
  it: function-only on the chord side (pc-identical share-tone chords such as Am6↔F♯ø7) and structural on the key side
  (the relative-major/minor and tonicization-vs-modulation classes are note-identical, so only the surrounding
  progression separates them). Full evidence: `cowork_uncertain_resolver_investigation.md`.
- **O1b — a *confident* commit is also overturnable (the confidence-weighted override; user-ratified 2026-06-26).** O1
  covers the slices this layer *abstained* on. The ratified architecture-wide principle goes further: a slice this layer
  **confidently committed** can still be overturned by Layer 5 when its functional/cadential evidence is decisive (the
  fine-grain chord override — the class-(b) transients). So a commit is the best reading on the notes-and-key evidence
  this layer had, **not a final word**. Two facts make this safe and already-supported (VERIFIED at source): the layer
  carries its ranked `alternatives` (∪ the prevailing chord) and its `confidenceModel` on **every** decision — Commit and
  Inherit included, filled before the trichotomy and never pruned — so Layer 5 overrides **by selecting among the readings
  this layer carried** (never by re-deriving), and the carried confidence is the quantity its override threshold scales
  against. Where the correct reading was never carried at all, that is a *coverage* miss fixed inside this layer, not by
  Layer 5. A lock-in test pins the carry. Note: this layer's confidence is **vertical-fit only** by construction (no
  progression signal folded in — that is Layer 5's to supply), and `alternatives` is capped (`topK`) and excludes
  spelling-pinned symmetric siblings — calibration facts the Layer-5 override design accounts for, not defects here. Full
  mechanism: `cowork_layer5_function_design.md` §8/§9-D7; `cowork_target_architecture.md` control-flow contract.
- **O2 — a bounded-window joint resolution for the neighbour dependency (deferred).** The baseline resolves the
  membership↔neighbour chicken-and-egg with the two-reading scheme (§4). A bounded joint choice — picking the chords
  and membership that best explain a few-slice window *together* — is potentially more precise but is deferred, because
  its window bound is delicate (too wide and it becomes the progression decode that belongs to Architectural Layer 5)
  and its evidence must stay note + membership, never progression grammar. Once the two-reading baseline is built and
  measured, test whether its per-slice precision falls short of the joint optimum; adopt the joint version only with a
  strictly note-bounded window.
