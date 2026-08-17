# The finer `CLAUDE.md` split — what each part of the standing-rules file is, and where it should live

> **STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED AND NOTHING IS EXECUTED.**
> `CLAUDE.md` is **byte-unchanged** by the measurement this surface reports. No span is moved, no
> anchor is re-aimed, and every fate below is a **PROPOSAL**. The user rules this surface; ONE
> later dispatch then executes what is ruled, and nothing before that.
>
> **GENERATED, not hand-written.** Every count, every span and every reader below comes from two
> committed artifacts — `tools/audit/claude_md_finer_spans.json` and
> `tools/audit/claude_md_finer_readers.json` — and nothing is typed by hand.

## 0. What is being decided, explained from scratch

**The file.** `CLAUDE.md` carries this project's standing rules: the guiding principles, the
open-items and decisions register conventions, the gate and threshold policy, the writing and
working conventions. Every session reads it before doing anything else.

**Why it is being looked at again.** The user's pruning direction named this file FIRST. A
coarse measurement predicted about 23% of it was archive material; the executed split moved
**3.2%**, because the read-before-move safeguard established that the placement was largely
wrong. Ruling 4 of `cowork_rulings_2026_08_17_sixth_return.md` therefore commissioned THIS pass:
a finer span unit and stricter recognizers, delivering a new surface with per-span fates.

**What is NOT being proposed.** Nothing is deleted. A span that moves is moved WHOLE to `CLAUDE_ARCHIVE.md`
with a dated pointer left at the site it came from. Nothing is lost, which is the standing
no-information-loss rule.

## 1. The test every fate below is proposed under, as the user ruled it

§5(E) of `cowork_rulings_2026_08_16_preparation_return.md`. The line is **not** current-versus-old.
It is **READERSHIP: who needs this span, and when.**

- **STAYS AT SITE** — a span that changes what a working session does or how it reads a rule today:
  the rule itself, the purpose that bounds its application, live caveats, STOP conditions.
- **ARCHIVES, with a dated pointer at the site** — a span whose only reader is someone re-opening
  the decision or auditing its history: preserved former wordings, declined alternatives, accepted
  costs, founding narratives, superseded baselines.
- **THE DOUBT DEFAULT: a span the test cannot place STAYS AT SITE.** A wrongly archived operative
  span fails silently; wrongly kept noise fails visibly and cheaply.

**Every span this measurement could not place positively is marked doubt-defaulted below, and its
proposed fate is STAYS AT SITE.** That is the ruled default applied mechanically, never a judgment
stretched to reach a verdict.

## 2. What this pass changed, and the measured evidence for each change

| what changed | the measured ground |
|---|---|
| **A cut at every numbered-principle opener** (`^\d{1,2}\.\s`) | finding F33's second case, measured: an amendment record's span OVERRAN into principles 22, 23 and 24, which carry no blank line above them, so the coarse pass placed three standing principles in an archive class. |
| **A former-wording marker no longer places a span on its own** — a quotation must accompany it, beginning within 300 characters | finding F33's largest mis-class, measured: 15,395 characters of live governing rule text — the decisions register's rules (a) through (n) — were classed `preserved-former-wording` on two sentences that POINT AT former wordings preserved in the register's own provenance, the span containing none. |

**What the stricter recognizer costs, stated so it is chosen rather than discovered:** a genuinely preserved wording shorter than the floor, or beginning further from every one of its markers than the window, is NOT placed and falls to the doubt default — it stays at site, which is the recoverable direction. A preservation marked by italics alone, with no quotation marks, is likewise not placed.

**★ AND TWO KINDS OF SPAN ARE NEVER CLASSED BY THE WORDS THEY CONTAIN**, this pass's own self-check, reading the surface it had just generated. Both were proposed for archiving on the first run.

- **An archive pointer** (`^\s*\*★ ARCHIVED \d{4}-\d{2}-\d{2}`) — the executed split leaves a compact dated pointer at every site it archives, and that pointer QUOTES its target's class and opening, so a recognizer reading its words places it in the class of the thing it points at. Archiving a pointer removes the one breadcrumb back to the moved span.
- **A bare section heading** (`^#{1,6}\s`) — a heading is a span of its own and its section body is another, so classing the heading by its own words would move it while everything under it stayed — a headless section, and a heading filed alone in the companion.

Both are placed at site POSITIVELY rather than by the doubt default: the doubt default records an absence of evidence; these two are decisions with a reason, and publishing the reason is what lets the user overrule either in one edit rather than rediscover it.

## 3. The measurement

| | characters | lines | spans | placed by the doubt default |
|---|---:|---:|---:|---:|
| the coarse pass (before the split) | 156,068 | | 156 | 120,169 (77.0%) |
| **this pass** (after the split) | 151,045 | 1,792 | 185 | 135,341 (89.6%) |

**The two are measured at DIFFERENT TREES, so the character counts are not comparable and the
shares are what to read.** the coarse decomposition was taken BEFORE the executed split, so its character counts include the 6,540 characters that act archived. What is comparable is the SHAPE: how much of the file each pass places by evidence rather than by the doubt default.

### By class, with the proposed fate

| class | spans | characters | share of the file | proposed fate |
|---|---:|---:|---:|---|
| self-declared-historical-or-superseded | 2 | 5,873 | 3.9% | **ARCHIVES, with a dated pointer at the site** |
| preserved-former-wording | 2 | 3,894 | 2.6% | **ARCHIVES, with a dated pointer at the site** |
| defense-and-declined-alternatives | 2 | 3,775 | 2.5% | **ARCHIVES, with a dated pointer at the site** |
| operative-rule-text | 179 | 137,376 | 91.0% | **STAYS AT SITE** |
| **proposed to ARCHIVE, in total** | | **13,542** | **9.0%** | |

### ★ Where this pass proposes archiving a span the read-before-move safeguard already READ and KEPT

The executed split's own read-before-move safeguard left 17 spans at site because they do not read as their class says (finding F33). Where this pass proposes archiving one of them, the user is being asked to overturn a reading already performed AT THE FILE — so the conflict is named here, with the safeguard's own reason quoted, rather than left to be noticed.

**How to read a conflict:** the safeguard's reason either IS or IS NOT answered by this pass's finer cut, and that is the question. Where the reason was that a span OVERRAN into live rule text, the finer cut answers it. Where the reason was that the span ITSELF states a rule, no cut answers it and the proposal should be refused.

- **lines 194–213**, proposed `preserved-former-wording` — opening *"**★ THAT PARAGRAPH REPLACED A NARROWER ONE, AND THE FORMER WORDING STANDS IN PLACE (#12; user-ruled 2026-08-11 on a surf…"*
  - **The safeguard's own reason for keeping it:** ★ FAILS TEST (1). The span OVERRUNS the amendment record it is classed for: principle #21's preserved former wording runs from line 228 to 247, and lines 248-260 are PRINCIPLES 22, 23 AND 24 — three live standing principles carrying no blank line above them, so the span rule carried them into the archive class. Archiving this span would remove three principles from the standing list. This is finding F29's residual risk realised.
- **lines 344–374**, proposed `defense-and-declined-alternatives` — opening *"**★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH A PER-ROW LAPSE RECORD (user-ruled 2026-08-11; the ruling re…"*
  - **The safeguard's own reason for keeping it:** ★ FAILS TEST (2). Classed by an accepted-costs marker inside it, but the span STATES THE RULE: an apparatus row stays open, stops gating any stage and stops being owed, with the per-row lapse record and the #19 bound. That rule is stated nowhere else, so a session reading CLAUDE.md would stop meeting it.
- **lines 796–816**, proposed `self-declared-historical-or-superseded` — opening *"*★ [SUPERSEDED by the OI-178 adoption 2026-07-26 — historical] THE OI-168 RE-BASELINE (2026-07-14; report `cc_oi168_fix_…"*
  - **The safeguard's own reason for keeping it:** ★ FAILS TEST (2). It self-declares as superseded and historical, and it closes with a LIVE caveat and a live prohibition — the OI-170 carry-forward, and "L4 is NOT tonic-independent; no design may assume it is". A design session must meet that prohibition at the site.
- **lines 1008–1044**, proposed `self-declared-historical-or-superseded` — opening *"**★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; `cc_a8_rebaseline_measure_report.md`).** The **primary report…"*
  - **The safeguard's own reason for keeping it:** ★ FAILS TEST (2). Classed historical on a `retained for provenance` marker that governs only the recitation in its second half. Its first half STATES the A-8 dual-track's ratified baselines and the hard stop that governs when it governs — live figures a measurement session reads.
- **lines 1750–1772**, proposed `preserved-former-wording` — opening *"**★ THE RULE COVERS EVERY READ MECHANISM AND EVERY DIALECT (recorded 2026-08-08 on the user's direction, at the third me…"*
  - **The safeguard's own reason for keeping it:** ★ FAILS TEST (2). Classed on a former wording preserved inside it, but the span STATES THE RULE'S REACH — that the shell-read restriction covers every read mechanism and every dialect, what the guard watches, and that its silence on an unwatched surface is not compliance (#19). A working session acts on all three.

## 4. What a further split would have to reconcile — the reach, refreshed at this tree

An **anchor** is a citation into the file AT A LINE; moving a span above it silently re-points it
at something else. This is the half the third batch's STOP made mandatory: a mutation's reach is
MEASURED before the act, never assumed.

| files naming it | namings | anchored namings | files carrying an anchor | tools that read or parse it | register entries homed here |
|---:|---:|---:|---:|---:|---:|
| 797 | 11,362 | 2,723 | 65 | 4 | 87 |

**The tools that read or parse it**, which are what a change of SHAPE breaks rather than a change
of line numbers:

- `tools/audit/decisions/gen_item1_rehome_blocker.py`
- `tools/audit/gen_phase1_completion_inventory.py`
- `tools/audit/gen_phase1_finish_line.py`
- `tools/audit/shell_read_guard.py`

**What this does NOT establish:** That a naming is a DEPENDENCY, or that a file naming none of these depends on none of them. The scan sees TRACKED files only, and a path composed at run time carries no literal to find — the same bound the retirement caller-check publishes of itself. The parser list is narrower still: a tool reaches it only when the line that names the file ALSO carries a read signal, so a tool that derives its inputs from `CLAUDE.md` across two lines is invisible to it.

**Why nothing is excluded from this scan, unlike the coarse pass's:** The coarse pass excludes its own three outputs because each names all five governing files, so writing them would change the population its next run counts. That hazard does not arise here: this reading is taken at a PINNED COMMIT at which this pass's own outputs do not exist. Every tracked naming is therefore counted — the coarse pass's own artifacts among them — which makes this a WIDER figure than that pass's and not a comparable one.

## 5. The proposed fate, per span

Every span of the file, in order. **`doubt`** marks a span no recognizer placed — its fate is the
ruled default. The evidence that placed each other span is in the artifact beside it.

| lines | kind | characters | class | doubt | proposed fate | opening |
|---:|---|---:|---|:-:|---|---|
| 1–1 | block | 58 | operative-rule-text |  | STAYS AT SITE | # Claude Code — Standing Instructions for This Repository… |
| 3–3 | block | 22 | operative-rule-text |  | STAYS AT SITE | ## Guiding principles… |
| 5–7 | block | 197 | operative-rule-text | ● | STAYS AT SITE | The standing decision guides for all work in this repository. Every design, build, and measurement choice is c… |
| 9–11 | numbered-principle sub-block | 197 | operative-rule-text | ● | STAYS AT SITE | 1. **Fact- and theory-based coding only.** Build only on established fact and theory — published research, pub… |
| 12–13 | numbered-principle sub-block | 145 | operative-rule-text | ● | STAYS AT SITE | 2. **Specific research over general.** Most research so far has been general or on already-handled topics; tar… |
| 14–16 | numbered-principle sub-block | 199 | operative-rule-text | ● | STAYS AT SITE | 3. **An unexpected finding means we have failed #1** (and possibly #2, #4, #6). Surprise signals that the fact… |
| 17–17 | numbered-principle sub-block | 52 | operative-rule-text | ● | STAYS AT SITE | 4. **Long-term goal: maximum-precision inference.**… |
| 18–19 | numbered-principle sub-block | 110 | operative-rule-text | ● | STAYS AT SITE | 5. **Investigate when facts may be scarce.** If we are unsure whether facts are scarce, gather more facts.… |
| 20–20 | numbered-principle sub-block | 77 | operative-rule-text | ● | STAYS AT SITE | 6. **Total unification — no duplication of any code.** One path per concern.… |
| 21–22 | numbered-principle sub-block | 180 | operative-rule-text | ● | STAYS AT SITE | 7. **Adhere to layers.** Enhance a layer only with algorithms/methods that belong to it, nothing else. Worst c… |
| 23–27 | numbered-principle sub-block | 525 | operative-rule-text | ● | STAYS AT SITE | 8. **No inference-problem-driven coding until the refactoring, the architectural design and the algorithmic co… |
| 28–34 | star-marked sub-block | 657 | operative-rule-text | ● | STAYS AT SITE | **★ THIS PRINCIPLE POINTS AT ITS OPERATIONAL HALF — D-592 AND D-593 (written 2026-08-04 on the user's ruling; … |
| 35–39 | star-marked sub-block | 491 | operative-rule-text | ● | STAYS AT SITE | **★ AND THE ENTRY IS D-172, ONCE (user's ruling, 2026-08-04, `OPEN_ITEMS.md` OI-329).** The widening above bri… |
| 40–40 | numbered-principle sub-block | 76 | operative-rule-text | ● | STAYS AT SITE | 9. **Test and measure only on corpora known to be non-stale and accurate.**… |
| 41–52 | numbered-principle sub-block | 1,159 | operative-rule-text | ● | STAYS AT SITE | 10. Documentation is kept in sync with code **so that code can always be compared against its specification, a… |
| 53–60 | star-marked sub-block | 845 | defense-and-declined-alternatives |  | ARCHIVES, with a dated pointer at the site | **★ WHAT IT SUPERSEDES — A POINTER, NEVER A COPY (#6).** R3's clause that an apparatus finding's row is **mand… |
| 61–65 | star-marked sub-block | 420 | operative-rule-text | ● | STAYS AT SITE | **★ WHAT IT DOES NOT DO.** It authorizes no fix, no design and no inference change. It moves neither **D-231**… |
| 66–66 | numbered-principle sub-block | 92 | operative-rule-text | ● | STAYS AT SITE | 11. **Regression test cases always in sync with code; regression-test between iterations.**… |
| 67–69 | numbered-principle sub-block | 236 | operative-rule-text | ● | STAYS AT SITE | 12. **No information loss.** Negative/exclusion evidence is information ("finding by exclusion") — carry a rul… |
| 70–79 | star-marked sub-block | 942 | operative-rule-text | ● | STAYS AT SITE | **★ THE RECOMPUTABLE CLAUSE ABOVE REACHES EVERY COLLAPSE, NOT ONLY AN EXCLUSION (2026-07-06; the record states… |
| 80–80 | numbered-principle sub-block | 93 | operative-rule-text | ● | STAYS AT SITE | 13. **Surface a surprise as a STOP before building around it** (the operational form of #3).… |
| 81–81 | numbered-principle sub-block | 93 | operative-rule-text | ● | STAYS AT SITE | 14. **Every behavior change is user-ratified as one revertible, provenance-stamped commit.**… |
| 82–83 | numbered-principle sub-block | 126 | operative-rule-text | ● | STAYS AT SITE | 15. **Verify at objects/data on the full output surface, never at assertion** (winner *and* carry, not the win… |
| 84–85 | numbered-principle sub-block | 150 | operative-rule-text | ● | STAYS AT SITE | 16. **Reproducibility.** Every measurement is stamped to corpus-hash + instrument-commit; snapshot the outgoin… |
| 86–99 | numbered-principle sub-block | 1,216 | operative-rule-text | ● | STAYS AT SITE | 17. **The Premise Gate.** Before any inference-affecting design is built or probed: (a) a **premise ledger** —… |
| 100–109 | star-marked sub-block | 961 | operative-rule-text | ● | STAYS AT SITE | **★ WHAT A DESK SIMULATION'S TABLE VALUES ARE, AND WHAT THEY MAY NEVER BECOME (user-ratified 2026-07-19).** Ev… |
| 110–115 | star-marked sub-block | 517 | operative-rule-text | ● | STAYS AT SITE | **★ EVERY DESK-SIMULATION TRACE RUNS AT IDENTITY WEIGHTS (user-ratified 2026-07-19).** A trace under (c) runs … |
| 116–117 | numbered-principle sub-block | 169 | operative-rule-text | ● | STAYS AT SITE | 18. **Unverified causal premises are FORBIDDEN (Class A).** No design may carry load on a causal claim about o… |
| 118–121 | numbered-principle sub-block | 311 | operative-rule-text | ● | STAYS AT SITE | 19. **Unestablished instruments are FORBIDDEN (Class B).** An instrument, corpus, gate, or recorded figure is … |
| 122–125 | numbered-principle sub-block | 363 | operative-rule-text | ● | STAYS AT SITE | 20. **Fit/evaluation separation.** No value is graded on data that helped fit it. Every fit event declares its… |
| 126–130 | numbered-principle sub-block | 405 | operative-rule-text | ● | STAYS AT SITE | 21. **Ground truth is an instrument too.** The accuracy of ground truth is itself a measured quantity — per-ax… |
| 131–148 | star-marked sub-block | 1,666 | operative-rule-text | ● | STAYS AT SITE | **★ THE CEILING CANNOT BE CITED FROM THE LITERATURE; MEASURING IT HERE IS THE ONLY ROUTE (recorded 2026-08-04 … |
| 149–169 | star-marked sub-block | 2,009 | operative-rule-text | ● | STAYS AT SITE | **★ AND THE MEASUREMENT IS NOW COMMISSIONED, IN TWO HALVES, WITH THE RULE THAT ENDS THE CONTACT ROUTE (user-ru… |
| 170–193 | star-marked sub-block | 2,324 | operative-rule-text | ● | STAYS AT SITE | **★ AND THE CONTACT ROUTE CLOSED BY ANSWER, NOT BY SILENCE — WITH THE ANSWER THAT THE ONE LOCALLY HELD CANDIDA… |
| 194–213 | star-marked sub-block | 1,905 | preserved-former-wording |  | ARCHIVES, with a dated pointer at the site | **★ THAT PARAGRAPH REPLACED A NARROWER ONE, AND THE FORMER WORDING STANDS IN PLACE (#12; user-ruled 2026-08-11… |
| 214–218 | numbered-principle sub-block | 399 | operative-rule-text | ● | STAYS AT SITE | 22. **Every hard gate carries a pre-declared protocol for the largest change it will face.** A gate written on… |
| 219–222 | numbered-principle sub-block | 336 | operative-rule-text | ● | STAYS AT SITE | 23. **End-state principles need lawful transitions.** When a planned change must temporarily violate an end-st… |
| 223–226 | numbered-principle sub-block | 300 | operative-rule-text | ● | STAYS AT SITE | 24. **Every reported figure carries its uncertainty.** Sampling noise on the measurement corpus is quantified;… |
| 228–231 | block | 344 | operative-rule-text | ● | STAYS AT SITE | *Ledger corollary to #17 (ratified with #20–#24):* when a decision selects a **constrained optimum** (a design… |
| 233–237 | block | 451 | operative-rule-text | ● | STAYS AT SITE | *Scope of surprise (ratified with #17–19):* surprises are **allowed in explorational runs** whose purpose is t… |
| 239–252 | block | 1,226 | operative-rule-text | ● | STAYS AT SITE | *Fact-publication corollary to #6/#7/#12 (ratified by the user, 2026-07-10):* every derived analytical fact is… |
| 254–266 | block | 1,132 | operative-rule-text | ● | STAYS AT SITE | *Decision-neutrality of the existing implementation (corollary to #4/#6/#19; user-ratified 2026-07-26):* Desig… |
| 268–278 | block | 1,001 | operative-rule-text | ● | STAYS AT SITE | *Theory-grounding corollary to #1/#2 (2026-07-19; the record states no ratifier):* where published research is… |
| 280–291 | block | 1,061 | operative-rule-text | ● | STAYS AT SITE | *Provenance: principles 1–11 are the user's standing list; #12 (no information loss) and #13–16 were ratified … |
| 293–299 | block | 659 | operative-rule-text | ● | STAYS AT SITE | **Delegation pointer (the fifth home case; written 2026-08-03 on the user's direction, the OI-293 write list).… |
| 301–301 | block | 114 | operative-rule-text |  | STAYS AT SITE | ## The open-items register (user-directed, 2026-07-10; split into index + detail files, user-ratified 2026-07-… |
| 303–318 | block | 1,527 | operative-rule-text | ● | STAYS AT SITE | **The register is `OPEN_ITEMS.md` (the lean INDEX) + `open_items/OI-<n>.md` (one detail file per item).** The … |
| 320–342 | star-marked sub-block | 2,137 | operative-rule-text | ● | STAYS AT SITE | **★ QUALIFICATION OF RULE (b) — THE APPARATUS ROWS ARE DECLARED NON-GATING (user-ruled 2026-08-03).** Rule (b)… |
| 344–374 | star-marked sub-block | 2,930 | defense-and-declined-alternatives |  | ARCHIVES, with a dated pointer at the site | **★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH A PER-ROW LAPSE RECORD (user-ruled 2026-08-11; the… |
| 376–384 | star-marked sub-block | 824 | operative-rule-text | ● | STAYS AT SITE | **★ RULE (f) — EVERY INDEX STATUS CELL BEGINS WITH ONE CANONICAL TOKEN (user-ruled 2026-08-09; the ruling reco… |
| 386–391 | block | 556 | operative-rule-text | ● | STAYS AT SITE | **The two STOPs that make it a mechanism rather than a convention.** A **lint** reports every non-canonical op… |
| 393–402 | block | 941 | operative-rule-text | ● | STAYS AT SITE | *Why the rule is worth a lettered place beside the others.* It is one cause with three faces, and each face wa… |
| 404–412 | star-marked sub-block | 776 | operative-rule-text | ● | STAYS AT SITE | **★ AND WHAT A DISCARD VERDICT DOES TO A ROW ALREADY ON THE BOOKS — IT IS AN INPUT TO THE DERIVATION THAT DECI… |
| 414–419 | block | 541 | operative-rule-text | ● | STAYS AT SITE | **THE RULING. A DISCARD verdict on an already-rowed item is an INPUT to the derivation that decides gating — n… |
| 421–426 | star-marked sub-block | 511 | operative-rule-text | ● | STAYS AT SITE | **★ THE GUARD, WHICH IS NOT AN ADDITION BUT #10's OWN REQUIREMENT.** A discard verdict is **AUTHORED**, not de… |
| 428–431 | block | 324 | operative-rule-text | ● | STAYS AT SITE | *Why an input rather than a hand-made correction:* **D-436** reserves to the user the question of what a deriv… |
| 433–433 | block | 167 | operative-rule-text |  | STAYS AT SITE | *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 8 line(s), `defense-and-declined-alternatives`, opening "**THE T… |
| 435–435 | block | 167 | operative-rule-text |  | STAYS AT SITE | *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 4 line(s), `defense-and-declined-alternatives`, opening "**THE C… |
| 437–442 | star-marked sub-block | 515 | operative-rule-text | ● | STAYS AT SITE | **★ WHAT IT DOES NOT DO.** It authorizes **NO SWEEP** — it states how a discard verdict is consumed, not that … |
| 444–444 | block | 96 | operative-rule-text |  | STAYS AT SITE | ## The decisions register (shape user-ratified 2026-07-28; content + living surface 2026-08-02)… |
| 446–605 | block | 15,395 | operative-rule-text | ● | STAYS AT SITE | **The register is `DECISIONS.md` (the lean INDEX) + `decisions/group_<X>.md` (full entries: the verbatim decis… |
| 607–621 | star-marked sub-block | 1,479 | operative-rule-text | ● | STAYS AT SITE | **★ HOW RULE (c) IS DISCHARGED ONCE IT HAS ALREADY BEEN MISSED (user-ruled 2026-08-09; the ruling record is `c… |
| 623–623 | block | 19 | operative-rule-text |  | STAYS AT SITE | ## Project context… |
| 625–628 | block | 241 | operative-rule-text | ● | STAYS AT SITE | This is MuseScore Studio. The active development area is the `composing` module (`src/composing/`), which impl… |
| 630–630 | block | 43 | operative-rule-text |  | STAYS AT SITE | ## Autonomous operation — composing module… |
| 632–632 | block | 75 | operative-rule-text | ● | STAYS AT SITE | When working on the `src/composing/` module you are **pre-authorized** to:… |
| 634–639 | block | 446 | operative-rule-text | ● | STAYS AT SITE | - Edit any file under `src/composing/` without asking for confirmation - Edit `src/notation/internal/notationa… |
| 641–642 | block | 107 | operative-rule-text | ● | STAYS AT SITE | **Standard loop for mismatch reduction work** — do all of the following without stopping for confirmation:… |
| 643–643 | numbered-principle sub-block | 28 | operative-rule-text | ● | STAYS AT SITE | 1. Analyse the mismatch(es)… |
| 644–644 | numbered-principle sub-block | 44 | operative-rule-text | ● | STAYS AT SITE | 2. Implement the fix in `chordanalyzer.cpp`… |
| 645–645 | numbered-principle sub-block | 9 | operative-rule-text | ● | STAYS AT SITE | 3. Build… |
| 646–646 | numbered-principle sub-block | 42 | operative-rule-text | ● | STAYS AT SITE | 4. Run tests and read the mismatch report… |
| 647–647 | numbered-principle sub-block | 63 | operative-rule-text | ● | STAYS AT SITE | 5. Report results (mismatches before → after, any regressions)… |
| 649–656 | block | 401 | operative-rule-text | ● | STAYS AT SITE | Only stop and ask if: - A regression is introduced (mismatch count goes up or a previously passing test fails)… |
| 658–658 | block | 27 | operative-rule-text |  | STAYS AT SITE | ## Build and test commands… |
| 660–665 | block | 512 | operative-rule-text | ● | STAYS AT SITE | **Always read these three files at the start of every session:** - `C:\s\MS\BUILD_AND_TEST.md` — authoritative… |
| 667–669 | block | 305 | operative-rule-text | ● | STAYS AT SITE | Do not rely on memory of previous sessions for baseline numbers or iteration state — read STATUS.md. `STATUS_A… |
| 671–686 | fenced-block | 614 | operative-rule-text | ● | STAYS AT SITE | ``` # Build — use PowerShell Start-Process (cmd.exe //c fails in MSYS2/Git Bash) powershell.exe -Command "Star… |
| 688–692 | block | 410 | operative-rule-text | ● | STAYS AT SITE | **Both test suites must pass after every code change.** The notation tests include `pipeline_snapshot_tests` w… |
| 693–695 | fenced-block | 85 | operative-rule-text | ● | STAYS AT SITE | ``` cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens ```… |
| 696–697 | block | 137 | operative-rule-text | ● | STAYS AT SITE | Then re-run `./pipeline_snapshot_tests.exe` to confirm all pass. Only run `--update-goldens` when the output c… |
| 699–699 | block | 36 | operative-rule-text |  | STAYS AT SITE | ## Gate threshold and preset policy… |
| 701–704 | block | 270 | operative-rule-text | ● | STAYS AT SITE | Gate thresholds (e.g. Gate I: 0.45, Gate L: 0.35; Gate K is retired — removed from this list by user ruling 20… |
| 706–706 | block | 69 | operative-rule-text |  | STAYS AT SITE | ### (A) THE ROBUST-UNIT REGRESSION STOP (ratified R10-b, 2026-07-06)… |
| 708–713 | star-marked sub-block | 560 | operative-rule-text | ● | STAYS AT SITE | **★ The governing hard regression stop** is the **granularity-robust union-of-boundaries unit, variant (b) DCM… |
| 715–725 | block | 1,091 | operative-rule-text | ● | STAYS AT SITE | **Committed reference (the diff base): `tools/robust_stop/`** — per-preset `stem@runStartTick` variant-(b) roo… |
| 727–743 | star-marked sub-block | 1,683 | operative-rule-text | ● | STAYS AT SITE | **★ THE PINNED INSTRUMENT NOW DECLARES WHICH INFERENCE ARM ITS BASELINES WERE MEASURED ON, AND REFUSES A CORPU… |
| 745–759 | star-marked sub-block | 1,536 | operative-rule-text | ● | STAYS AT SITE | **★ Ratified baselines — RE-BASELINED AT THE OI-178 JOINT-ESTIMATOR ADOPTION, 2026-07-26 (user-ratified, optio… |
| 761–775 | star-marked sub-block | 1,466 | operative-rule-text | ● | STAYS AT SITE | **★ HOW THE ROOT COLUMN MUST BE READ — IT UNDERSTATES WHAT A WRONG KEY COSTS (D-576; recorded here 2026-08-04 … |
| 777–792 | block | 1,647 | operative-rule-text | ● | STAYS AT SITE | **STAGED SCOPE — CLOSED AT THE NOTATION SWITCH (user-ratified 2026-07-27).** The OI-178 adoption put the joint… |
| 794–794 | block | 172 | operative-rule-text |  | STAYS AT SITE | *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 5 line(s), `self-declared-historical-or-superseded`, opening "**… |
| 796–816 | block | 2,231 | self-declared-historical-or-superseded |  | ARCHIVES, with a dated pointer at the site | *★ [SUPERSEDED by the OI-178 adoption 2026-07-26 — historical] THE OI-168 RE-BASELINE (2026-07-14; report `cc_… |
| 818–828 | block | 1,167 | operative-rule-text | ● | STAYS AT SITE | *The KEY columns above supersede the OI-142/OI-143 column (key home 71.29/67.49/70.52, key local 65.72/62.49/6… |
| 830–836 | block | 700 | operative-rule-text | ● | STAYS AT SITE | *Earlier columns, for the record: the OI-142/OI-143 re-baseline (user-ratified 2026-07-12) applied the 12 tran… |
| 838–840 | block | 255 | operative-rule-text | ● | STAYS AT SITE | - **The hard stop (per preset):** the **class-(b) (pitch-class-decidable-root) root-disagree DURATION must be … |
| 841–844 | fenced-block | 255 | operative-rule-text | ● | STAYS AT SITE | ``` python tools/a8_rebaseline_measure.py --out-dir <cand> [--corpus-root <scratch>] # self-validates grid==or… |
| 845–866 | block | 2,107 | operative-rule-text | ● | STAYS AT SITE | - **The mandatory explained diff:** every run lists the **run-level set-diff** vs the reference (added/removed… |
| 868–871 | star-marked sub-block | 373 | operative-rule-text | ● | STAYS AT SITE | **★ THE FOUR GRADING CONVENTIONS THE ROBUST UNIT IS MEASURED UNDER (each ruled earlier; written into this bloc… |
| 873–911 | block | 3,905 | operative-rule-text | ● | STAYS AT SITE | - **THE ONLY GROUND TRUTH IS THE HUMAN ANNOTATION. The algorithmic analysis is a noise filter, never a standar… |
| 913–916 | star-marked sub-block | 345 | operative-rule-text | ● | STAYS AT SITE | **★ THREE FURTHER MEASUREMENT CONVENTIONS, HOMED HERE 2026-08-07 ON THE USER'S HOMING RULING.** They sit BESID… |
| 918–945 | block | 2,670 | operative-rule-text | ● | STAYS AT SITE | - **A measurement publishes its COVERAGE DENOMINATOR and its PER-CORPUS breakdown; a single aggregate number t… |
| 947–949 | star-marked sub-block | 252 | operative-rule-text | ● | STAYS AT SITE | **★ TWO MORE GRADING CONVENTIONS, HOMED HERE 2026-08-07 ON THE USER'S HOMING RULING.** They sit beside the sev… |
| 951–974 | block | 2,269 | operative-rule-text | ● | STAYS AT SITE | - **A DEFENSIBLE MODAL READING THE MAJOR/MINOR GROUND TRUTH CANNOT REPRESENT IS A GROUND-TRUTH LIMITATION, NOT… |
| 975–978 | star-marked sub-block | 371 | operative-rule-text | ● | STAYS AT SITE | **★ READ IT BESIDE THE CREDITING-RULE PROHIBITION IMMEDIATELY BELOW, WHICH IS A DIFFERENT BINDING STATEMENT OF… |
| 980–1006 | star-marked sub-block | 2,506 | operative-rule-text | ● | STAYS AT SITE | **★ THE CREDITING RULE IS NOT AMENDED TO COUNT A TONICIZATION LABEL AS AGREEING WITH THE ANNOTATOR'S MODULATED… |
| 1008–1044 | star-marked sub-block | 3,642 | self-declared-historical-or-superseded |  | ARCHIVES, with a dated pointer at the site | **★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; `cc_a8_rebaseline_measure_report.md`).** The **prim… |
| 1046–1046 | block | 64 | operative-rule-text |  | STAYS AT SITE | ### (B) The two-tier per-cell class policy — CARRIED OVER, LIVE… |
| 1048–1053 | block | 523 | operative-rule-text | ● | STAYS AT SITE | **This policy is UNCHANGED at R10-b and now governs the robust unit's per-cell classification** (the class-(a)… |
| 1055–1087 | block | 3,200 | operative-rule-text | ● | STAYS AT SITE | **Two-tier refinement (user-ratified 2026-06-22) — class-(b) functional regression vs class-(a) symmetric-rota… |
| 1089–1089 | block | 105 | operative-rule-text |  | STAYS AT SITE | ### (C) RETROSPECTIVE — the batch 52/24/52 stop (superseded at R10-b, 2026-07-06 — historical reference)… |
| 1091–1091 | block | 172 | operative-rule-text |  | STAYS AT SITE | *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 8 line(s), `self-declared-historical-or-superseded`, opening "> … |
| 1093–1102 | block | 1,023 | operative-rule-text | ● | STAYS AT SITE | **The batch stop's diagnostic form — KEPT (no longer the stop).** `characterise_bir_false.py` remains a runnab… |
| 1104–1109 | fenced-block | 367 | operative-rule-text | ● | STAYS AT SITE | ``` cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque cd C:\s\M… |
| 1111–1124 | block | 1,179 | operative-rule-text | ● | STAYS AT SITE | **Re-baselined 2026-06-13 (corrected GT parser).** The prior **13/7/14** gate was an **undercount**: GT-parser… |
| 1126–1126 | block | 172 | operative-rule-text |  | STAYS AT SITE | *★ ARCHIVED 2026-08-17 → `CLAUDE_ARCHIVE.md`: 7 line(s), `self-declared-historical-or-superseded`, opening "**… |
| 1128–1136 | star-marked sub-block | 921 | operative-rule-text | ● | STAYS AT SITE | **★ (History) Corrected to the ratified post-L3-wiring state `53 / 24 / 53` (Stage-0 measurement, commit `b57d… |
| 1138–1159 | block | 2,301 | operative-rule-text | ● | STAYS AT SITE | - **Baroque = 52** with identities (stem@tick): `{bwv10.7@36000, bwv14.5@8160, bwv144.6@15360, bwv144.6@16320,… |
| 1161–1161 | block | 16 | operative-rule-text |  | STAYS AT SITE | ### (D) Caveats… |
| 1163–1174 | block | 1,319 | operative-rule-text | ● | STAYS AT SITE | **Cross-layer-budget caveat (2026-06-24, O1 measurement) — LIVE (an interpretation caveat, not a granularity o… |
| 1176–1187 | star-marked sub-block | 1,140 | operative-rule-text | ● | STAYS AT SITE | **★ CORRECTION OF RECORD TO THE CAVEAT ABOVE — THE FUNCTION-ONLY SHARE IS OVERSTATED, BECAUSE OVER-GRABBED SEG… |
| 1189–1197 | block | 868 | operative-rule-text | ● | STAYS AT SITE | **Granularity caveat (Stage 2.2-i) — ✅ RESOLVED at R10-b (2026-07-06).** The mandate this caveat raised — "a g… |
| 1199–1206 | block | 639 | operative-rule-text | ● | STAYS AT SITE | (`tools/analyze_inversion_errors.py` is a *separate* secondary metric: its three-way `music21_dcml_agree` genu… |
| 1208–1208 | block | 84 | operative-rule-text | ● | STAYS AT SITE | If a gate causes BIR=false regressions in a non-Baroque preset, the correct fix is:… |
| 1209–1211 | numbered-principle sub-block | 200 | operative-rule-text | ● | STAYS AT SITE | 1. A tighter **structural entry condition** that excludes the problematic chord type regardless of preset (pre… |
| 1212–1212 | numbered-principle sub-block | 91 | operative-rule-text | ● | STAYS AT SITE | 2. A **preset-specific threshold override** that leaves the Baroque-tuned value unchanged.… |
| 1214–1214 | block | 72 | operative-rule-text | ● | STAYS AT SITE | Never widen a Baroque-tuned threshold to cover a non-Baroque edge case.… |
| 1216–1222 | block | 577 | operative-rule-text | ● | STAYS AT SITE | **Preset scoring caps — corrected 2026-06-10:** `maxTotalInversionContextBonus` is **never set on any code pat… |
| 1224–1224 | block | 76 | operative-rule-text |  | STAYS AT SITE | ## Scoring model — `docs/scoring_model.md` (MANDATORY for scoring sessions)… |
| 1226–1228 | block | 222 | operative-rule-text | ● | STAYS AT SITE | **Read `docs/scoring_model.md` at the start of any session that touches scoring logic in `chordanalyzer.cpp`**… |
| 1230–1241 | star-marked sub-block | 1,108 | operative-rule-text | ● | STAYS AT SITE | **★ THE SAME FORM, FOR THE PRODUCTION INFERENCE LAYER (user-ruled 2026-08-11; the ruling record is `cowork_rul… |
| 1243–1246 | block | 300 | operative-rule-text | ● | STAYS AT SITE | The document is the authoritative reference for how the scoring pipeline works, why each term exists, and what… |
| 1248–1251 | block | 270 | operative-rule-text | ● | STAYS AT SITE | **Sync rule — mandatory:** Any commit that adds or modifies a template, bonus, guard, gate, or other scoring t… |
| 1253–1256 | block | 276 | operative-rule-text | ● | STAYS AT SITE | - Adding a template: update the Templates section (§2), increment the template count in the array-size comment… |
| 1258–1260 | block | 216 | operative-rule-text | ● | STAYS AT SITE | **Staleness check:** The template count in `docs/scoring_model.md` §2 must always match the `array<TemplateDef… |
| 1262–1270 | block | 641 | operative-rule-text | ● | STAYS AT SITE | **Template additions — the `kTemplateCount` model (since `a236a0ff21`):** All template-related array extents (… |
| 1271–1271 | numbered-principle sub-block | 82 | operative-rule-text | ● | STAYS AT SITE | 1. Bump `analysis::kTemplateCount` N→N+1 (auto-resizes the matrices and `kMasks`)… |
| 1272–1272 | numbered-principle sub-block | 53 | operative-rule-text | ● | STAYS AT SITE | 2. Add the new `TemplateDef` entry in `analyzeChord`… |
| 1273–1273 | numbered-principle sub-block | 79 | operative-rule-text | ● | STAYS AT SITE | 3. Add the interval bitmask to `kMasks` (a zero mask silently disables Gate R)… |
| 1275–1277 | block | 230 | operative-rule-text | ● | STAYS AT SITE | Remaining trap: bumping the constant **without** adding the `TemplateDef` entry value-initializes a trailing a… |
| 1279–1279 | block | 17 | operative-rule-text |  | STAYS AT SITE | ## Score corpora… |
| 1281–1286 | block | 391 | operative-rule-text | ● | STAYS AT SITE | For any task involving scores (validation, snapshot tests, manual QA, LLM-triage, qualitative review), read `d… |
| 1288–1288 | block | 33 | operative-rule-text |  | STAYS AT SITE | ## Local patches — do not revert… |
| 1290–1292 | block | 215 | operative-rule-text | ● | STAYS AT SITE | The following changes have been made intentionally to fix bugs unrelated to the composing module. Do **not** r… |
| 1294–1304 | star-marked sub-block | 996 | operative-rule-text | ● | STAYS AT SITE | **★ THIS SECTION IS A CHECK'S INPUT (2026-08-03).** `tools/audit/local_patches_check.py` derives its patch lis… |
| 1306–1306 | block | 61 | operative-rule-text |  | STAYS AT SITE | ### Windows Snap fix — `muse` submodule (applied 2026-05-14)… |
| 1308–1309 | block | 121 | operative-rule-text | ● | STAYS AT SITE | **File:** `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp` **Function:** `calculateWindo… |
| 1311–1315 | block | 358 | operative-rule-text | ● | STAYS AT SITE | Two lines were removed that set `ptMinTrackSize` equal to the full monitor work area inside the `WM_GETMINMAXI… |
| 1317–1318 | block | 147 | operative-rule-text | ● | STAYS AT SITE | The fix: `ptMaxSize` and `ptMaxPosition` are kept (they correctly constrain the maximised position); `ptMinTra… |
| 1320–1322 | block | 184 | operative-rule-text | ● | STAYS AT SITE | Upstream issue: musescore/MuseScore#25823 (related cousins: #21344, #16794). Introduced by upstream commit `4a… |
| 1324–1324 | block | 69 | operative-rule-text |  | STAYS AT SITE | ### MusicXML declared-mode import fix (Stage 4a, applied 2026-06-14)… |
| 1326–1327 | block | 144 | operative-rule-text | ● | STAYS AT SITE | **File:** `src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp` **Function:** `addKey()` (the `K… |
| 1329–1339 | block | 845 | operative-rule-text | ● | STAYS AT SITE | The dedup guarded the `KeySig` creation on **fifths only**: `if (oldkey != key.key() \|\| key.custom() \|\| ke… |
| 1341–1348 | block | 668 | operative-rule-text | ● | STAYS AT SITE | The fix: fetch the prevailing `KeySigEvent` (not just the `Key` fifths) and add an `oldKeySig.mode() != key.mo… |
| 1350–1354 | block | 399 | operative-rule-text | ● | STAYS AT SITE | Upstream issue: musescore/MuseScore#9444. The buggy fifths-only dedup is upstream-unchanged code (the `// TODO… |
| 1356–1362 | star-marked sub-block | 698 | operative-rule-text | ● | STAYS AT SITE | **★ DISTRIBUTION CONSTRAINT (user, 2026-06-15): FORK-LOCAL ONLY — NEVER merge upstream / to the MuseScore comm… |
| 1364–1364 | block | 102 | operative-rule-text |  | STAYS AT SITE | ### Chord-symbol parser "sussus" fix — `ParsedChord::parse` (applied 2026-04-15; recorded 2026-08-02)… |
| 1366–1368 | block | 116 | operative-rule-text | ● | STAYS AT SITE | **File:** `src/engraving/dom/chordlist.cpp` **Function:** `ParsedChord::parse()` (~line 990) **Commit:** `b1ba… |
| 1370–1375 | block | 488 | operative-rule-text | ● | STAYS AT SITE | One line removed: the redundant case-sensitive `tok1 = u"sus"` assignment beside the correct lowercase `tok1L … |
| 1377–1387 | star-marked sub-block | 978 | operative-rule-text | ● | STAYS AT SITE | **★ DISTRIBUTION DISPOSITION (user-ratified 2026-08-02): UPSTREAMABLE** — a general parser defect fix with no … |
| 1389–1389 | block | 69 | operative-rule-text |  | STAYS AT SITE | ## VS Code extension — bash command rules (MANDATORY, every session)… |
| 1391–1394 | block | 339 | operative-rule-text | ● | STAYS AT SITE | The Claude Code VS Code extension (v2.1.141+) has a 15-second stall detector. If the API stream is silent for … |
| 1396–1396 | block | 63 | operative-rule-text | ● | STAYS AT SITE | **Two rules that apply to every bash command, no exceptions:**… |
| 1398–1403 | block | 413 | operative-rule-text | ● | STAYS AT SITE | **Rule 1 — Always append `; echo "exit:$?"` to any command that may return non-zero.** A non-zero exit code al… |
| 1405–1413 | block | 584 | operative-rule-text | ● | STAYS AT SITE | **Rule 2 — Never let a single bash call produce large output.** Large output (thousands of lines) takes >15 se… |
| 1415–1415 | block | 90 | operative-rule-text | ● | STAYS AT SITE | Build commands via `Start-Process` are isolated from these rules (exit code not exposed).… |
| 1417–1417 | block | 15 | operative-rule-text |  | STAYS AT SITE | ## Conventions… |
| 1419–1496 | block | 7,103 | operative-rule-text | ● | STAYS AT SITE | - American English throughout — "analyzer" not "analyser" - No confirmation prompts between analyse → implemen… |
| 1497–1520 | star-marked sub-block | 2,245 | operative-rule-text | ● | STAYS AT SITE | **★ WHAT HAPPENS TO A NAME BORROWED FROM THE PUBLISHED RESEARCH, AND IN WHAT ORDER THE CLEANUP RUNS (user-rule… |
| 1522–1534 | block | 1,247 | operative-rule-text | ● | STAYS AT SITE | - **EVERY DESIGN DECISION CARRIES ITS DEFENSE AT ITS HOME (user-directed, 2026-08-01, at the decisions-registe… |
| 1536–1538 | block | 238 | operative-rule-text | ● | STAYS AT SITE | - **ISSUE-EXHAUSTION AND SPECIFICATION COMPLETION BEFORE ANY FIX DESIGN (user-directed, 2026-08-02; sharpens #… |
| 1539–1567 | star-marked sub-block | 2,685 | operative-rule-text | ● | STAYS AT SITE | **★ THE THREE-PHASE STRUCTURE BELOW IS SUPERSEDED AND ITS TRUTH HALF IS REPLACED (user-ruled 2026-08-15; the r… |
| 1568–1587 | star-marked sub-block | 1,960 | operative-rule-text | ● | STAYS AT SITE | **★ HOW FAR THE DOC-SYNC HALF REACHES INTO A DOCUMENT'S ACCOUNT OF ITSELF (user-ruled 2026-08-04; D-639).** Th… |
| 1588–1594 | star-marked sub-block | 663 | operative-rule-text | ● | STAYS AT SITE | **★ AND IT BEARS ON A GATE VERDICT — A POINTER, NOT A RULING (the question is open at `OPEN_ITEMS.md` OI-336).… |
| 1595–1633 | star-marked sub-block | 3,701 | operative-rule-text | ● | STAYS AT SITE | **★ WHEN PHASE 1 IS COMPLETE — THE FINISH LINE IS CUT BY D-438'S TEST, AND THE APPARATUS RESIDUE DOES NOT GATE… |
| 1634–1655 | star-marked sub-block | 2,087 | operative-rule-text | ● | STAYS AT SITE | **★ QUALIFICATION — PHASE 3 WAITS ON THE PHASE-2 ITEMS THAT COULD FIND ANOTHER MEMBER OF THE FAMILY BEING DESI… |
| 1656–1685 | star-marked sub-block | 2,597 | operative-rule-text | ● | STAYS AT SITE | **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT IS RATIFIED (user, 2026-08-03; D-439).** `cowork_o… |
| 1687–1695 | block | 802 | operative-rule-text | ● | STAYS AT SITE | - **MAKE IT WORK FIRST; COMPROMISE ON PERFORMANCE ONLY IF PERFORMANCE PROVES TO BE A PROBLEM (user-directed, 2… |
| 1697–1706 | block | 937 | operative-rule-text | ● | STAYS AT SITE | - **CANDIDATE ADMISSION IS COMPLETION, NOT REFINEMENT — so #8 permits fixing it now (user-ruled 2026-07-28, at… |
| 1708–1715 | block | 775 | operative-rule-text | ● | STAYS AT SITE | - **ONE FIX IS DESIGNED ONCE OVER THE WHOLE ENUMERATED FAMILY, NEVER PER SYMPTOM (user-ruled 2026-07-28, at th… |
| 1717–1729 | block | 1,227 | operative-rule-text | ● | STAYS AT SITE | - **THE WHOLE DECISION SURFACE IS DELIVERED AS USER-VISIBLE TEXT BEFORE ANY CHOICE QUESTION (user mandate 2026… |
| 1731–1749 | block | 1,844 | operative-rule-text | ● | STAYS AT SITE | - **WORKING-TREE FILES ARE READ WITH THE FILE TOOLS; SHELL ACCESS IS LIMITED TO GIT OBJECT QUERIES BY EXPLICIT… |
| 1750–1772 | star-marked sub-block | 1,989 | preserved-former-wording |  | ARCHIVES, with a dated pointer at the site | **★ THE RULE COVERS EVERY READ MECHANISM AND EVERY DIALECT (recorded 2026-08-08 on the user's direction, at th… |
| 1774–1781 | block | 787 | operative-rule-text | ● | STAYS AT SITE | - **INVESTIGATE BY DEFAULT; NEVER ASK THE USER WHETHER TO INVESTIGATE OR PROCEED (user mandate 2026-06-14; hom… |
| 1783–1783 | block | 74 | operative-rule-text |  | STAYS AT SITE | ## The self-check after every coding exercise (user-directed, 2026-07-11)… |
| 1785–1792 | block | 685 | operative-rule-text | ● | STAYS AT SITE | After EVERY coding exercise — code, scripts, instruments, and document edits alike — and BEFORE reporting the … |

## 6. What this surface asks the user to rule

1. **The per-span fates in §5** — as proposed, or amended span by span.
2. **Whether the two recognizer changes in §2 are the right ones**, given what each costs.
3. **Whether the 89.6% left at site by the doubt default is acceptable as it stands**, or whether
   a further pass should try to place more of it. Under the ruled default every character of it
   stays.

**★ THE ANSWER THIS PASS ACTUALLY GIVES, stated plainly because it is the point of commissioning it.**
At this grain and under these recognizers, **9.0% of `CLAUDE.md` — 13,542 characters in
6 spans — is placeable as archive material by evidence.** That is more than the 3.2% the split
moved and far less than the coarse pass's 23% prediction.

**And the number that actually decides the question is smaller still: 5 of those spans were
ALREADY READ AT THE FILE by the split's own safeguard and deliberately KEPT** (§3 above). Only
**1 span, 845 characters**, is proposed on ground no reading has yet refused. Of the
contested ones, exactly one — the principle-#21 overrun — is answered by this pass's finer cut;
the rest were kept because the span ITSELF states a rule, and no cut answers that.

**So: if the goal is a materially smaller `CLAUDE.md`, this measurement says the recognizers are
not the route.** What remains is rule text and amendment records that no pattern over prose
separates from the rules they amend. That is a finding about the file, not a failure of the pass,
and it is stated here rather than left for the user to infer from a small number.

**★ ONE LIMITATION, STATED RATHER THAN LEFT TO BE FOUND.** A cut inside a block yields a span whose
sentence may continue in the next one, so a span is not guaranteed to be readable on its own. That
is why the fates here are PROPOSALS, and why the read-before-move safeguard binds any later
executing act exactly as it bound the last one.

**Nothing here is ruled.** `CLAUDE.md` is not edited, no span is moved, no anchor is re-aimed and no
reader is touched. This surface proposes; the user rules; ONE later dispatch performs — in that
order and no other.

*Generated by `tools/audit/gen_claude_md_finer_surface.py` from `tools/audit/claude_md_finer_spans.json` and `tools/audit/claude_md_finer_readers.json`, 2026-08-17, dispatch `cc_instruction_preparation_seventh.md` Task 3.*
