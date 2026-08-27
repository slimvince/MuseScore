# Decision surface — the defect in the take rule, and the redraw it forces

> **STATUS: DECISION SURFACE.** Cowork, 2026-08-27, the fifty-second session. One decision, the
> alternatives, what each costs towards the objective and the ruled principles, and a recommendation.
> **There is no question in the turn that delivers it.** The choice question is put in a later turn.
>
> **Taken at branch tip `aa3077709117962ab05b27d79466bfacc77a2382`**, read at `.git/refs/heads/master`
> with the file tool. No shell command was run against the repository by this side.
>
> **This is the THIRD and last of the three decisions.** The first two are ruled and recorded at
> `cowork_rulings_2026_08_27_stopped_strata_sitting.md`.
>
> **★ THE HAZARD THAT ATTACHES TO THIS WHOLE SURFACE, DECLARED AT THE TOP.** Your ruling of
> 2026-08-27 protects the sample by having the writing side fix the selection **before any count is
> visible**. The counts are now visible — 33, 59, 730 — and this surface proposes changing the rule
> knowing them. **That property is spent for this decision and cannot be recovered.** What partly
> answers it is set out at §6 and does not answer it completely.

---

## 1. What this decision is about, explained from scratch

The sample is drawn from eight populations, called **strata**. For each, a rule you declared on
2026-08-27 decides which items are taken. The rule, in full, as written into the dispatch before any
count was known:

> Let `N` be a stratum's enumerated count and `T = 25`.
> **If `N ≤ T`: the stratum goes in WHOLE.**
> **If `N > T`: the stratum contributes exactly `T = 25` items**, taken systematically: let
> `k = floor(N / T)`; take the items at 1-indexed ordered positions `1, 1+k, 1+2k, …, 1+24k`.

`T = 25` is **declared, not derived** — no measurement in this project supports it, and nothing below
changes that or moves it.

The ordering within a stratum is fixed and mechanical: **file path in byte order, then line number**
(then, for deleted headings, the hash of the deleting commit).

**The rule has a defect. It was authored by the writing side — by this side's predecessor, not by
Claude Code — and Claude Code applied it exactly as written and adjusted nothing, which was
correct.**

---

## 2. The defect, derived from the rule's own text

**The last position the rule can ever reach is `1 + 24k`.** Everything after that in the ordering is
unreachable — not "rarely drawn", but **impossible to draw**.

**And because the ordering is path-then-line, the unreachable region is always the same thing: the
end of the last-sorted files.** So the exclusion is **correlated with content**, not neutral. It is
not a sampling error that averages out; it is a fixed hole in a fixed place.

**Worked at the three affected strata, from the rule's text and the reported counts:**

| Stratum | `N` | `k` | last reachable position | unreachable |
|---|---|---|---|---|
| 5 — evidence inventory | 33 | 1 | 25 | **26–33 (8 items)** |
| 8 — deleted headings | 59 | 2 | 49 | **50–59 (10 items)** |
| 7 — current headings | 730 | 29 | 697 | **698–730 (33 items)** |

**A second, sharper face of the same defect.** When `T < N < 2T` — that is, `26 ≤ N ≤ 49` — `k` is 1
and the take degenerates to positions `1, 2, 3, … 25`: **the first twenty-five items of the ordering,
contiguously.** It is not a spread at all. Stratum 5 is in that band, so the evidence inventory was
sampled by taking its first 25 list items in file order. Claude Code reports the consequence: **its
Layer-5 section contributes nothing to the sample, and most of its Layer-4 section contributes
nothing.**

### 2.1 One correction to the report's arithmetic, derived here and small

Claude Code's report gives stratum 8's unreachable region as **positions 51–59**. By the rule's own
text `k = floor(59/25) = 2`, so the last drawn position is `1 + 24×2 = 49`, and **position 50 is also
beyond the take's reach: the region is 50–59, ten items, not nine.** Strata 5 and 7 in the same table
are correct as reported. **Nothing turns on it** — the defect and the redraw are identical either way
— but it is one more item than the record says, and this side derived it rather than repeating the
report.

---

## 3. What this decision is judged towards

**(a) The sample must not be shaped by a side that can see what its choices admit.** Your ruling of
2026-08-27. Already partly spent here; §6.

**(b) A declared number is cited as declared.** `T = 25` stays declared and stays at 25 under every
alternative below.

**(c) The finding must be reportable per stratum with an honest uncertainty range** — your ruling of
2026-08-26, which is why the sample was stratified at all. A range computed over a population with a
fixed hole in it is not honest, whatever the arithmetic says.

**(d) The standing bar against work pitched at too high a meta level.** All four alternatives below
are one line of arithmetic in one dispatch; none is a governance project. The bar does not separate
them.

---

## 4. The alternatives

### Alternative D — keep the rule, declare the exclusion

Change nothing. Record on the face of the placement report that each sampled stratum's last stretch
was unreachable, and name it.

**Towards the objective.** Cheapest possible: nothing is redrawn, the sample stands, the frame's gate
opens today.

**Why this side does not recommend it.** The exclusion is not a rounding artefact. **A whole layer of
the evidence inventory is absent from the sample** and the last thirty-three headings of the
last-sorted document-set files can never be tested. A per-stratum proportion computed on that
population, however carefully caveated, will be read as *the frame holds* by any successor who skims
it — and the caveat cannot be quantified, because nobody knows whether the excluded tail is like the
rest.

*(It is listed first because it is the only alternative that costs nothing, and the case for it should
be seen before the cost of the others.)*

### Alternative A — the cure named in the handoff: `floor(i·N/T) + 1`

Take positions `floor(i·N/T) + 1` for `i = 0 … T−1`, with `T` unchanged at 25.

**What it fixes.** The degenerate contiguous case is gone: at `N = 33` it spreads across positions 1
to 32 instead of taking 1 to 25.

**★ What it does NOT fix, derived here and not previously reported.** The last position it reaches is
`floor(24N/25) + 1`, which is **not the end of the ordering**:

| Stratum | `N` | last reachable under A | still unreachable |
|---|---|---|---|
| 5 | 33 | 32 | 33 (1 item) |
| 8 | 59 | 57 | 58–59 (2 items) |
| 7 | 730 | 701 | **702–730 (29 items)** |

**So for the largest stratum, Alternative A removes four items from the hole and leaves twenty-nine.**
The one-sided, content-correlated exclusion the defect is *about* survives it almost intact. **This
side proposed A in the handoff without deriving that, and is correcting its own proposal here.**

### Alternative B — midpoint sampling: `floor((2i+1)·N / 2T) + 1`

Take the midpoint of each of 25 equal blocks. **What it fixes:** the residual is no longer one-sided
— it is split evenly between the two ends. At `N = 730` positions 1–14 and 717–730 are unreachable,
fourteen at each end; at `N = 33` nothing is unreachable at all.

**Its cost.** A hole at both ends is still a hole correlated with content — it excludes the *beginning
of the first-sorted file* as well as the end of the last. It trades a directional bias for a
symmetric one. It is the textbook cure for the bias and it is not the cure for the property this
project actually named.

### Alternative C — endpoint-inclusive spread

Take, for `i = 0 … T−1`, the position

> `p_i = 1 + ( i×(N−1) + 12 ) // 24`   *(integer division; `12` is `(T−1)/2` and `24` is `T−1`)*

**Written in integer arithmetic deliberately**, so that no rounding convention has to be trusted:
a rule that says *round* has an undefined answer at exactly one half, and a selection rule with an
implementation-dependent answer is not deterministic, which is the property your ruling of 2026-08-27
requires of it.

**What it fixes.** `p_0 = 1` and `p_24 = N`, for every `N`. **There is no unreachable region at
either end, for any stratum, at any count.** Checked at all three: `N = 33` → 1 … 33; `N = 59` →
1 … 59; `N = 730` → 1 … 730. Positions are strictly increasing and distinct whenever `N > T`, which
is the only case the take applies to.

**Its cost, stated plainly.** **Item 1 and item `N` are always drawn.** Two of the twenty-five slots
are spent deterministically on the first and last item of the ordering — which, since the ordering is
path-then-line, means the first heading of the byte-first file and the last item of the last file.
**Half of that cost is already being paid:** the rule as it stands, and Alternative A, also draw
position 1 every time. What C adds is that position `N` is always drawn too.

---

## 5. Recommendation

**Alternative C.**

The ground is that C is the only one of the four that removes the property the defect is about. D
keeps the hole and declares it. A — this side's own earlier proposal — shrinks the hole and leaves
twenty-nine items of it in the largest stratum, which is why it is corrected here rather than
recommended. B makes the hole symmetric, which is an improvement in bias and not a removal.

**C's cost is a fixed, declarable inclusion of two boundary items**, and half of that cost is already
being paid under the current rule. **A fixed inclusion that everyone can see is a smaller defect than
a fixed exclusion that nobody can size**, and that is the whole of the argument.

**`T` stays at 25 and stays declared, not derived.** Nothing here supplies a measurement for it and
no successor may cite it as measured.

---

## 6. What partly answers the counts-visible hazard, and what does not

**What answers it.** The take stays at 25 and the threshold stays at 25 — the two numbers that decide
how much of a stratum is drawn do not move, so the change cannot be shaping *how much* of anything is
taken. The replacement is a **general formula**, stated for every `N`, and it is chosen on a property
— that it reaches both ends of every ordering — which can be stated and checked without reference to
any count.

**What does not answer it, and is not smoothed over.** The counts were used. They were used to size
the defect, and they were used to compare the four candidates: the tables at §2 and §4 are computed
at `N = 33`, `59` and `730`. A successor must read the change as **made with the counts visible**,
because it was.

---

## 7. What follows if C is ruled — and it is very nearly a whole new sample

Say plainly what the next dispatch does, because between this decision and Ruling 1 of this sitting
almost nothing of the sealed file survives:

- **Strata 5, 7 and 8 are REDRAWN** under the corrected formula, on the units confirmed by Ruling 2.
- **Stratum 4 is untouched** — `N = 21` is at or below the threshold, so it is a census, and no take
  rule applies to it.
- **Strata 1, 2 and 3 are drawn for the FIRST time**, on the memberships and units declared by
  Ruling 1.
- **Stratum 6 is not drawn at all** and is recorded as NOT ENUMERABLE, per Ruling 1.
- **A new sealed file is written and committed at a new tip.** It supersedes
  `cowork_placement_sample_sealed_2026_08_27.md`, which is **not deleted** — it stays as the record of
  what was drawn under the defective rule. **Both are withheld from the frame's author.**

**One item of the old sample's content is knowable without opening it and is stated so the successor
does not have to check:** stratum 4's census of 21 deferred register entries is unaffected by every
ruling in this sitting, so it carries across unchanged.

**And the gate.** With Ruling 1 settling every stopped stratum and this ruling settling the draw,
**the frame is no longer gated on a decision** — it is gated only on the new sealed file existing.
The frame's author remains a fresh Cowork session that has read neither sealed file. **This session
is barred from being that author.**

---

## 8. Method

**Read whole for this surface:** `cc_instruction_placement_sample.md` (the rule's own text, at its
§2.2), `cc_report_placement_sample.md`, `cowork_rulings_2026_08_27_placement_sample_sitting.md`, and
the top entry of `cowork_handoff.md`.

**Derived by this side, not relayed:** every figure in the tables at §2 and §4 — the last reachable
position under the current rule and under each candidate, and the unreachable region at each of the
three counts — computed from the rule's quoted text and from the reported `N`. **That is how the
correction at §2.1 and the finding about Alternative A at §4 were reached.** The counts `33`, `59`
and `730` themselves are **relayed** from Claude Code's report and are not verified here.

**★ THE VERIFICATION LIMIT, UNCHANGED FOR A NINTH SESSION.** This side has no shell, cannot resolve a
commit or a blob, and relays every git-object figure.

**Not opened by this side:** any part of `cowork_placement_sample_sealed_2026_08_27.md`,
`cowork_evidence_inventory.md`, `ARCHITECTURE.md`, `CLAUDE.md`, `DECISIONS.md`, any source file, any
measurement output, any dossier, any boot pack.
