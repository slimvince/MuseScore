# Decisions group O — Intonation

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-244 — Choosing an interval family for an ambiguous sonority is deferred; fixed tables are used

> Another deferred design question is **which interval family to prefer for
> ambiguous sonorities**.  The current shipped tuning systems use fixed lookup
> tables (for example, 5-limit just intonation uses 9/5 for a minor seventh and
> 15/8 for a major seventh) rather than a style-aware policy that can choose
> between alternatives such as 5-limit dominant sevenths versus septimal
> "harmonic sevenths" (7/4), or other competing targets for altered/extended
> sonorities.  This is not specific to seventh chords — similar ambiguity also
> appears in tritones, minor sonorities, diminished/augmented chords, and larger
> extensions.  This choice architecture should be explored later, but it is not a
> current implementation target.

**In plain words.** When more than one pure interval could be targeted - a 5-limit minor seventh against a septimal one, and the same choice for tritones, minor and altered sonorities - the tuning systems keep their fixed lookup tables. A style-aware choice is left for later.

**Why.** Derivation not recorded. The record states the design space and that it is deferred, but not the measurement or constraint behind the deferral.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:6354-6363`

**Provenance.** ARCHITECTURE.md:5088-5089 states it is not a current implementation target; the same deferral is recorded in the retired-session record at STATUS_ARCHIVE.md:2335 ★ RATIFIED-FOR-NOW (user, 2026-08-02): to be REVIEWED when the intonation feature's implementation is revisited (the OI-62 held feature).

### D-245 — Voice role comes from staff position or explicit assignment; automatic melody detection is deferred

> Automatic melody detection is deferred. For now, voice role is determined by staff position
> or explicit user assignment — not automatic detection. Per-staff override of voice role is
> a future extension.

**In plain words.** Which voice counts as the melody is taken from where it sits in the score or from what the user says. Working it out automatically is left for later, as is a per-staff override.

**Why.** Derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:6477-6479`

**Provenance.** ARCHITECTURE.md:5203-5205 states the deferral ★ RATIFIED-FOR-NOW (user, 2026-08-02): to be REVIEWED when the intonation feature's implementation is revisited (the OI-62 held feature).

### D-246 — Fixed-pitch instruments are deferred, and will never receive tuning offsets

> Fixed-pitch instruments (piano, organ, fretted guitar) are deferred — their handling is not
> yet implemented. When implemented, they will serve as absolute anchors that other
> instruments tune to, and will never receive tuning offsets themselves.

**In plain words.** Piano, organ and fretted guitar are not handled yet. When they are, they will be the fixed reference other instruments tune to, and will not be retuned themselves.

**Why.** The constraint is the instruments themselves: their pitch is fixed by construction, so a tuning offset cannot be applied to them (ARCHITECTURE.md:5304-5306).

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:6578-6580`

**Provenance.** ARCHITECTURE.md:5304-5306 states both the deferral and the eventual behaviour ★ RATIFIED-FOR-NOW (user, 2026-08-02): to be REVIEWED when the intonation feature's implementation is revisited (the OI-62 held feature).

### D-366 — Recorded-performance intonation material is OUT of corpus scope — the intonation features are validated by theory and by listening

> | N15 | performed-intonation reference material | T-21/T-24 | **★ SCOPE RULING RATIFIED (user, 2026-07-04):** audio-domain, out of corpus scope; T-21/T-24 validate by theory/listening |

**In plain words.** Reference material for how performers actually tune is audio, not notation, and is ruled outside what the corpus collection covers. The two intonation features that would have consumed it are validated instead against tuning theory and by ear.

**Why.** derivation not recorded — the record states the ruling and its consequence but gives no reason beyond the material being audio-domain.

**Status.** LIVE · decided 2026-07-04 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:273`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 224). A delegation at ARCHITECTURE.md:370 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The cell records `★ SCOPE RULING RATIFIED (user, 2026-07-04)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

