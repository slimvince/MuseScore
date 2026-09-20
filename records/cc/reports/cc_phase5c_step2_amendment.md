# Phase 5c — Step 2 AMENDMENT (Layer 5 / FUNCTION): relax the authentic-cadence gate

> **Instruction:** the Step-2 amendment — drop the genuine-dominant (seventh/tritone) **gate** so a *plain* triad
> V→I is admitted as authentic; keep the seventh/tritone as a vote **strengthener**. Confirm a plain I→IV is still
> **not** a cadence. Gate: dormant + byte-identical. Spec corrected by Cowork at
> `cowork_layer5_function_design.md` §5.2 (2026-06-26, working-tree edit, not mine). This dossier is gitignored.
>
> **HEAD `20b1185057`** (unchanged — NOT committed; see §5). Working tree carries the relaxation + tests, uncommitted.

## 0. Result — ⛔ **§5 STOP**: the discriminator does NOT hold

> **★ SUPERSEDED by §7 (2026-06-29).** Cowork ratified that this STOP does NOT block: the limit is **by design** (a
> key-agnostic event-pair test cannot separate V→I from I→IV; resolved downstream). The relaxation was **committed**
> (HEAD `254e8c3b0e`), the STOP test reframed as a documented limit, and the phrase gate confirmed + tested. The §0/§3/§5
> "STOP / not committed / HEAD unchanged" text below records the original finding; see **§7** for the resolution.

The relaxation's **positive** half works exactly as intended — a plain triad V→I is now a PAC, and a V7→I outvotes
it. But §5's stop condition is **empirically confirmed**: after dropping the seventh gate, the
leading-tone-resolution event **does not by itself reject I→IV**. Per the amendment's §5 I have **STOPPED**, **not
committed**, and **not re-added the seventh gate** — reporting so Cowork re-evaluates the discriminator.

---

## §1 — The change applied (faithful to the instruction)

`src/composing/analysis/function/functioncadence.cpp`, `tryAuthentic()`:

- **Dropped** the `if (!isGenuineDominant(dom, arr, tonicPc)) return makeNone();` admission gate.
- **Kept** `isGenuineDominant(...)` computed as `genuineDom` and stored on the cadence
  (`c.genuineDominant = genuineDom`), so it still feeds the `+wSeventh` vote term — the **strengthener**, not a gate.
- Perfect/imperfect split unchanged (`bassFiveToOne = formV && root(dom) && root(arr)`).
- The leading-tone-resolution event (`ltResolves`) and the pre-dominant→dominant **sequence** requirement are
  unchanged and remain the admission gates.

Header (`functioncadence.h`) comment updated to describe the seventh as a strengthener and to carry the ★★
discriminator-concern note. **No threshold/weight tuned** (firewall). **No production code touched** — the unit has
**no production consumer** (grep of `src/` + `tools/` finds the identifiers only in the module, its test, and the two
CMakeLists), so the change is **byte-identical on production by construction**.

---

## §2 — The positive half WORKS (the amendment's intent)

Two new tests, both green:

- **`PlainTriadVToIIsPerfectAuthentic`** — `ii → V(plain G triad, no seventh) → I`, all root position, B→C resolving
  in voice 3 → **PerfectAuthentic**, tonic C, `bassFiveToOne`, `leadingToneResolves`, `genuineDominant == false`. This
  case was **excluded** before the amendment; it is admitted now. (The common Bach-chorale phrase-end.)
- **`SeventhStrengthensTheVoteOverAPlainTriadV`** — the same `ii→V→I` with a plain triad vs. with G7, same salience:
  both **PerfectAuthentic**; `genuineDominant` false vs. true; **`seventh.tonicVote > plain.tonicVote`** (the
  `+wSeventh` strengthener). Ordering confirmed.

So dropping the gate correctly **stops missing** the plain chorale cadence, and the seventh still raises the vote.

---

## §3 — ⛔ The STOP: a plain I→IV is now ALSO admitted (the discriminator cannot separate them)

**Root cause (music theory, not a fixture artifact).** A plain triad **V→I** and a plain triad **I→IV** are **exact
transpositions** of each other: a Major triad → triad, root up a perfect fourth, with the **third of the approach
chord resolving up a semitone to the root of the arrival chord**. The detector is **key-agnostic** — it hypothesizes
the **arrival** is the tonic. So for the I→IV pair (C→F) it hypothesizes **F** is the tonic, which makes **E (the
third of the I chord) the "leading tone" of F**, and the ordinary smooth common-tone voice leading **E→F** *is* a
7̂→1̂ same-voice motion → `leadingToneResolves` **fires**. There is **no event-pair signal** that distinguishes the
two: the seventh was the only separator, and it separated them by **rejecting both** (that is exactly why the plain
chorale V→I was being missed — the bug this amendment set out to fix).

**The spec's premise is key-aware, the detector is key-agnostic.** The corrected spec
(`cowork_layer5_function_design.md` §5.2, Cowork's edit) states *"this leading-tone-resolution event is itself the
discriminator against tonic-to-subdominant."* That holds for a **key-aware** reading — in C major the leading tone is
uniquely B, and I→IV has no B→C, so only V→I flags. But the key-agnostic detector tests **F** as the tonic for the
I→IV pair, where **E→F** is the leading-tone resolution. The discriminator therefore does **not** survive the
key-agnostic framing.

**Empirical confirmation — `PlainAuthenticAndItsTranspositionAreIndistinguishable_STOP` (green).** The test feeds the
relaxed detector a genuine plain V→I in C *and its exact +5 transposition* (= a plain I→IV in C, pitch-classes C→F),
and asserts the **current** behavior:

| Progression (pitch classes) | Fed as | Detector verdict |
|---|---|---|
| `Dm → G(triad) → C(triad)`, B→C in v3, C ends phrase | genuine plain V→I | **PerfectAuthentic, tonic C** ✓ correct |
| `Gm → C(triad) → F(triad)`, E→F in v3, F ends phrase (exact +5 transposition) | **a plain I→IV in C** | **PerfectAuthentic, tonic F** ✗ **false positive** |

`leadingToneResolves` is **true** on the I→IV pair (the test asserts it) — confirming the regression flows through
the discriminator itself, not some other path. The two transposed progressions receive the **identical** verdict;
the detector cannot tell them apart from the event pair alone.

(For completeness: the FULL detector still rejects a *bare* I→IV via the **phrase gate** (the mid-phrase IV does not
end a phrase — `PassingIToIVIsNotACadence`, still green) and via the **sequence gate** when no pre-dominant of the
spurious tonic precedes it. But a realistic **V→I→IV** phrase that ends on IV (e.g. `G→C→F`, G satisfying the
degree-2 pre-dominant test of F) slips through all gates as a false PAC on F. The discriminator §5 names is genuinely
absent.)

---

## §4 — Gate (dormant + byte-identical — measured)

| Gate | Result |
|---|---|
| Build | clean (`/tmp/build_amend.log`; 9/9 link steps, 0 `error C####`/`FAILED`) |
| `composing_tests` | **911/911** (908 + 3 new; 2 disabled, baseline) |
| `notation_tests` | passed (4 skipped, baseline) |
| `pipeline_snapshot_tests` | **11/11**, **NO golden refresh** (1 skipped, 3 disabled — baseline) |
| Corpus **53/24/53** | **unchanged by construction** — no production consumer; not re-measured (Step-1/2 precedent) |
| Production reach | **none** — `detectFunctionalCadences` unused outside the module + its test |

Byte-identical on production holds (the change is dormant; snapshots refreshed zero goldens).

---

## §5 — Decision & what I did NOT do (per the amendment's §5)

- **STOPPED.** Did **not** proceed to §4's "commit locally." **HEAD is unchanged at `20b1185057`.**
- **Did NOT re-add the seventh gate** (the amendment forbids it). The relaxation is left **applied** in the working
  tree (uncommitted) so Cowork can inspect/re-evaluate the discriminator on the actual code.
- **Did NOT touch** `cowork_layer5_function_design.md` (its working-tree modification is **Cowork's** §5.2 spec
  correction, pre-existing), `detectCadences()` (production), `upstream`, or any threshold/weight.
- The `_STOP` test asserts the **current (buggy) behavior** so the suite stays green; the assertion **is** the
  regression record and is reproducible. If a discriminator fix later rejects that I→IV, the test must be revised in
  lock-step (noted in the test comment).

## §6 — Declared to Cowork (the inference problem, per the standing rule — not prescribing a fix)

The leading-tone-resolution event is a sound **key-aware** discriminator but is **insufficient in the key-agnostic
event-pair frame**, because plain V→I and plain I→IV are transpositionally identical at the pitch-class + voice-motion
level. Re-evaluation options (for Cowork — I am not choosing one without direction):

1. **Keep the seventh/tritone as a soft requirement for the *plain*-triad case only** — admit a plain V→I only when
   an additional non-transpositional cue is present (e.g. the arrival is metrically/structurally stronger than the
   approach, or the phrase/section actually ends there), letting the seventh remain a strengthener for the V7 case.
   This keeps "plain V→I is authentic" while denying the symmetric I→IV the same structural support.
2. **Resolve I↔IV at a higher layer** — accept that the event-pair detector casts a *tonic vote* (not a verdict) and
   let the key/voice-leading aggregation (Step 3 resolver / Step 4 modulation arbiter) discount the transposed
   competitor, since a real I→IV almost never has the arrival as the metric/phrase goal.
3. **Re-instate the seventh gate** and accept that a *plain*-triad chorale V→I is detected only when a seventh or a
   leading-tone-chord substitution is present (the pre-amendment behavior) — i.e. decline the amendment.

These are surfaced as the declared inference problem; no production movement, no tuning, and no gate re-addition was
performed. Awaiting Cowork's re-evaluation of the discriminator.

## Files touched (working tree, uncommitted)
- `src/composing/analysis/function/functioncadence.cpp` — dropped the genuine-dominant admission gate; kept it as the
  `genuineDom` strengthener flag.
- `src/composing/analysis/function/functioncadence.h` — comment: seventh = strengthener; ★★ discriminator-concern note.
- `src/composing/tests/functioncadence_tests.cpp` — +3 tests (plain-V→I PAC; seventh strengthener ordering; the
  `_STOP` transposition-symmetry regression record); two stale comments corrected.

---

## §7 — RESOLUTION (Cowork-ratified, 2026-06-29): the §5 STOP does NOT block — commit the relaxation; the limit is by-design

Cowork re-evaluated the discriminator and **ratified the relaxation**. The §3 finding stands and is **correct and
important**, but it is **not a blocker**: a key-agnostic event-pair test *cannot* separate a plain V→I from a plain
I→IV (they are exact transpositions), and that is **by design** — the cadence detector casts **soft evidence**, it is
not a key-aware classifier. The spec premise (LT-resolution = the discriminator) was wrong and is **corrected** at
`cowork_layer5_function_design.md` §5.2 ("the key-agnostic limit"). The disambiguation is **resolved downstream**: the
seventh/tritone strengthener (when present), the **phrase gate** (the common mid-phrase I→IV), and the **key-layer
aggregation** (the rare at-boundary residual's soft vote).

**Done this session (per the resolution instruction §1–§5):**

1. **Relaxation committed** (§1) — the genuine-dominant ADMISSION gate stays dropped; the seventh/tritone remains the
   `+wSeventh` vote strengthener. The two positive tests stay green (`PlainTriadVToIIsPerfectAuthentic`,
   `SeventhStrengthensTheVoteOverAPlainTriadV`). No threshold/weight tuned (firewall).
2. **STOP test reframed as a documented limit** (§2) — `PlainAuthenticAndItsTranspositionAreIndistinguishable_STOP`
   → **`PlainAuthenticAndItsTranspositionAreIndistinguishable_KeyAgnosticLimit_ResolvedDownstream`**. Same assertions
   (the event-pair test alone returns the same verdict for V→I and its +5 transposition — **by design**); the comment
   block + the `functioncadence.h` ★★ note rewritten from "STOP / pending Cowork re-evaluation" to **"the key-agnostic
   limit — resolved downstream"**, pointing to §5.2.
3. **Phrase gate confirmed at source + tested** (§3) — verified that **every** cadence type (`tryAuthentic`,
   `tryDeceptive`, `tryHalf`, `tryPlagal`, `tryEvaded`) gates candidate admission on `arr.endsPhrase` *first*
   (functioncadence.cpp:220/295/352/400/444), so a mid-phrase I→IV is **never admitted as a candidate**. The §6 STOP
   ("phrase gate not applied at candidate admission") does **NOT** trigger. New test
   **`PlainIToIVRejectedMidPhraseAdmittedAtBoundary_PhraseGate`**: the I→IV pair NOT at a phrase boundary → **no
   cadence**; the SAME pair AT a boundary → admitted, casting a soft vote (`tonicVote > 0`) for the key layer to weigh.
   Added the candidate-admission anchor comment at the `tryAuthentic` phrase gate. (The rare at-boundary I→IV is left as
   the documented soft-evidence residual — no key-aware test added inside this key-agnostic unit, per the instruction.)

**Gate (§4) — dormant + byte-identical:**

| Gate | Result |
|---|---|
| Build | clean (9/9 link steps; `functioncadence_tests.cpp` compiled, 0 errors) |
| `composing_tests` | **912/912** (911 + 1 new phrase-gate test; 2 disabled, baseline) |
| `notation_tests` | **53/53** (4 skipped, baseline) |
| `pipeline_snapshot_tests` | **11/11**, **NO golden refresh** (1 skipped, 3 disabled — baseline) |
| Corpus **53/24/53** | **unchanged by construction** — no production consumer; not re-measured (Step-1/2/amendment precedent) |
| Production reach | **none** — `detectFunctionalCadences` used only by the module + its test (+ 2 CMakeLists) |

**Commits (§5) — local, unpushed:**
- **`7845328d05`** `docs(cowork): L5 §5.2 "the key-agnostic limit" correction (Phase 5c Step 2)` — Cowork's §5.2 spec
  correction (the relaxation + the documented limit).
- **`254e8c3b0e`** `feat(function): relax L5 authentic-cadence gate to admit plain triad V->I (Phase 5c Step 2
  amendment, dormant)` — the relaxation + the reframed/added tests. **HEAD = `254e8c3b0e`.**

**Step 2 is COMPLETE.** Awaiting the Step-3 (resolver) instruction. (`upstream` untouched; `scratch_artifacts/` left
untracked, not committed; this dossier remains gitignored.)
