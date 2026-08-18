# The governing-surface split — what each part of the five mandatory reads is, and where it should live

> **STATUS: RULED, 2026-08-17. NOTHING IS EXECUTED BY IT.**
> This surface was a ruling surface awaiting the user; **the user ruled it at the governing-surface
> split sitting of 2026-08-17, whose record is `cowork_rulings_2026_08_17_governing_surface_split.md`**
> — the authority for what was ruled and what was not, none of which is restated here (#6).
> **The banner it replaces read "STATUS: RULING SURFACE, awaiting the user. NOTHING HERE IS RULED
> AND NOTHING IS EXECUTED." — true when it was written, and made untrue by the sitting; the former
> rendering stands in git at the commits that carried it (#12).**
> No governing file is edited by the measurement this surface reports, no span is moved, and no
> fate below is decided BY THIS SURFACE. Every fate below is the PROPOSAL the user ruled on; ONE later
> dispatch executed what was ruled, and this surface executes nothing.
>
> **GENERATED, not hand-written.** Every count, every span and every reader below comes from two
> committed artifacts — `tools/audit/governing_surface_spans.json` and
> `tools/audit/governing_surface_readers.json` — and nothing is typed by hand.

## 0. What is being decided, explained from scratch

**The five files.** Every session — the writing side and the coding side alike — is ordered to read
five files before it does anything else: `CLAUDE.md` (the standing rules), `OPEN_ITEMS.md` (the
open-issues index), `DECISIONS.md` (the index of what was decided), `STATUS.md` (what state the
work is in) and `BUILD_AND_TEST.md` (how to build, test and measure). They are the mandatory reads.

**The problem, in the user's own words:** *"we need to prune (at least) claude.md and open_items.md
because the mandatory reads at session start for you and CC are too large (we are already hitting
quality problems - and there are also other issues like real monetary cost and response times)."*

**What is NOT being proposed.** Nothing is deleted. A span that moves is moved WHOLE to a place
that keeps it — an archive file, or the document that properly owns it — with a dated pointer left
at the site it came from. Nothing is lost, which is the standing no-information-loss rule.

## 1. The test every fate below is proposed under, as the user ruled it

The line is **not** current-versus-old. It is **READERSHIP: who needs this span, and when.**

- **STAYS AT SITE** — a span that changes what a working session does or how it reads a rule today:
  the rule itself, the purpose that bounds its application, live caveats, STOP conditions.
- **ARCHIVES, with a dated pointer at the site** — a span whose only reader is someone re-opening
  the decision or auditing its history: preserved former wordings, declined alternatives, accepted
  costs, founding narratives, superseded baselines. That reader needs it at the moment of
  re-opening, not at session start, and the pointer takes them there.
- **MOVES TO ITS PROPER HOME** — a span that is not archive material but mis-homed.
- **THE DOUBT DEFAULT: a span the test cannot place STAYS AT SITE.** A wrongly archived operative
  span fails silently; wrongly kept noise fails visibly and cheaply. Staying is the recoverable
  direction.

**Every span this measurement could not place positively is marked as doubt-defaulted below, and
its proposed fate is STAYS AT SITE.** That is the ruled default applied mechanically, never a
judgment stretched to reach a verdict.

## 2. How big the problem is — the measurement, per file

| file | characters | lines | spans | anchored namings into it | register entries homed here |
|---|---:|---:|---:|---:|---:|
| `CLAUDE.md` | 156,068 | 1,853 | 156 | 1,354 | 87 |
| `OPEN_ITEMS.md` | 610,413 | 470 | 408 | 129 | 1 |
| `DECISIONS.md` | 132,664 | 901 | 658 | 0 | 0 |
| `STATUS.md` | 505,057 | 780 | 150 | 79 | 0 |
| `BUILD_AND_TEST.md` | 28,010 | 563 | 130 | 34 | 1 |
| **total** | **1,432,212** | | **1,502** | **1,596** | **89** |

## 3. What each file is made of, by class

The classes are the ruling's own. Each span is placed by a recognizer over its own text, and the
marker that placed it is published in the artifact beside the verdict.

### `CLAUDE.md`

| class | spans | characters | share of the file |
|---|---:|---:|---:|
| resolved-row | 0 | 0 | 0.0% |
| self-declared-historical-or-superseded | 6 | 7,862 | 5.0% |
| preserved-former-wording | 5 | 22,656 | 14.5% |
| defense-and-declined-alternatives | 5 | 5,254 | 3.4% |
| pointer-entry-of-a-completed-batch | 0 | 0 | 0.0% |
| operative-rule-text | 140 | 120,169 | 77.0% |
| — of which no recognizer placed (**doubt-defaulted**) | | 120,169 | 77.0% |

### `OPEN_ITEMS.md`

| class | spans | characters | share of the file |
|---|---:|---:|---:|
| resolved-row | 133 | 326,334 | 53.5% |
| self-declared-historical-or-superseded | 1 | 5,709 | 0.9% |
| preserved-former-wording | 6 | 33,374 | 5.5% |
| defense-and-declined-alternatives | 0 | 0 | 0.0% |
| pointer-entry-of-a-completed-batch | 0 | 0 | 0.0% |
| operative-rule-text | 268 | 244,972 | 40.1% |
| — of which no recognizer placed (**doubt-defaulted**) | | 244,972 | 40.1% |

### `DECISIONS.md`

| class | spans | characters | share of the file |
|---|---:|---:|---:|
| resolved-row | 0 | 0 | 0.0% |
| self-declared-historical-or-superseded | 0 | 0 | 0.0% |
| preserved-former-wording | 2 | 4,385 | 3.3% |
| defense-and-declined-alternatives | 1 | 5,094 | 3.8% |
| pointer-entry-of-a-completed-batch | 0 | 0 | 0.0% |
| operative-rule-text | 655 | 123,112 | 92.8% |
| — of which no recognizer placed (**doubt-defaulted**) | | 123,112 | 92.8% |

### `STATUS.md`

| class | spans | characters | share of the file |
|---|---:|---:|---:|
| resolved-row | 0 | 0 | 0.0% |
| self-declared-historical-or-superseded | 0 | 0 | 0.0% |
| preserved-former-wording | 2 | 4,168 | 0.8% |
| defense-and-declined-alternatives | 0 | 0 | 0.0% |
| pointer-entry-of-a-completed-batch | 129 | 453,664 | 89.8% |
| operative-rule-text | 19 | 47,076 | 9.3% |
| — of which no recognizer placed (**doubt-defaulted**) | | 47,076 | 9.3% |

### `BUILD_AND_TEST.md`

| class | spans | characters | share of the file |
|---|---:|---:|---:|
| resolved-row | 0 | 0 | 0.0% |
| self-declared-historical-or-superseded | 6 | 1,476 | 5.3% |
| preserved-former-wording | 2 | 767 | 2.7% |
| defense-and-declined-alternatives | 0 | 0 | 0.0% |
| pointer-entry-of-a-completed-batch | 0 | 0 | 0.0% |
| operative-rule-text | 122 | 25,647 | 91.6% |
| — of which no recognizer placed (**doubt-defaulted**) | | 25,647 | 91.6% |

## 4. The proposed fates, per class

Each fate below applies to every span of that class, in every file. The per-span list is in the
artifact; nothing is decided per span by hand, which is what keeps this a measurement rather than
a sweep of judgments.

| class | proposed fate | why, under the ruled test |
|---|---|---|
| operative-rule-text | **STAYS AT SITE** | It is the rule itself, or a span no recognizer placed elsewhere. The ruled doubt default is that a span the test cannot place stays at site. |
| resolved-row | **ARCHIVES, with a dated pointer at the site** | A resolved row's only reader is someone auditing the history of an issue that is closed. The interim reading scope already skips these rows at session start, so archiving them makes physical a boundary the user has already ruled. |
| self-declared-historical-or-superseded | **ARCHIVES, with a dated pointer at the site** | The span says of ITSELF that it is historical or superseded. Its reader is someone re-opening the decision; the pointer takes them there. |
| preserved-former-wording | **ARCHIVES, with a dated pointer at the site** | The ruling names preserved former wordings as archive material by name. Information loss is not at stake: preservation elsewhere-with-record is what the register split already did. |
| defense-and-declined-alternatives | **ARCHIVES, with a dated pointer at the site** | The ruling names declined alternatives and accepted costs by name. NOTE THE NARROWNESS: only a span carrying an explicit declined-alternative or accepted-cost marker is in this class — a rule's PURPOSE stays at site, because the ruled test says the purpose that bounds a rule's application is operative. |
| pointer-entry-of-a-completed-batch | **NOT DECIDED BY THIS TEST — governed by `STATUS.md`'s own archive rule** | A dated entry recording a completed batch. The readership test does not settle it and this surface does not stretch to a verdict: `STATUS.md` carries its OWN rule — *a superseded entry moves to `STATUS_ARCHIVE.md` instead of accumulating here* — and ruling (C) already brings that rule into the executing act. What the measurement contributes is the size: this class is the largest single block of the five files, so which entries are superseded is a question worth answering rather than a formality. Until it is answered the ruled default holds and every character of it stays at site. |

## 5. What a split would have to reconcile — the readers, measured before any act

This is the half the third batch's STOP made mandatory: a mutation's reach is MEASURED before the
act, never assumed. An **anchor** is a citation into a file AT A LINE; moving a span above it
silently re-points it at something else.

| file | files naming it | namings | anchored namings | files carrying an anchor | tools that read or parse it |
|---|---:|---:|---:|---:|---:|
| `CLAUDE.md` | 781 | 8,928 | 1,354 | 63 | 4 |
| `OPEN_ITEMS.md` | 715 | 5,824 | 129 | 21 | 9 |
| `DECISIONS.md` | 149 | 367 | 0 | 0 | 2 |
| `STATUS.md` | 468 | 3,119 | 79 | 24 | 1 |
| `BUILD_AND_TEST.md` | 194 | 887 | 34 | 17 | 0 |

**The tools that read or parse each file**, which are what a change of SHAPE breaks rather than a
change of line numbers:

- `CLAUDE.md` — `tools/audit/decisions/gen_item1_rehome_blocker.py`, `tools/audit/gen_phase1_completion_inventory.py`, `tools/audit/gen_phase1_finish_line.py`, `tools/audit/shell_read_guard.py`
- `OPEN_ITEMS.md` — `tools/audit/decisions/gen_cluster_dispositions.py`, `tools/audit/gen_discard_records.py`, `tools/audit/gen_index_status_normalization.py`, `tools/audit/gen_nongating_apparatus_rows.py`, `tools/audit/gen_oi367_opening_correction.py`, `tools/audit/hardening_battery.py`, `tools/audit/register_lint.py`, `tools/audit/shell_read_guard.py`, `tools/open_items_split_check.py`
- `DECISIONS.md` — `tools/audit/decisions/gen_decisions_register.py`, `tools/audit/gen_phase1_completion_inventory.py`
- `STATUS.md` — `tools/audit/shell_read_guard.py`
- `BUILD_AND_TEST.md` — *none found*

**What this does NOT establish:** That a naming is a DEPENDENCY, or that a file naming none of these depends on none of them. The scan sees TRACKED files only, and a path composed at run time carries no literal to find — the same bound the retirement caller-check publishes of itself.

## 6. What this surface asks the user to rule

1. **The per-class fates in §4** — each one, as proposed or amended.
2. **Whether the doubt-defaulted share in §3 is acceptable as it stands**, or whether a further
   measured pass should try to place more of it before anything moves. It is the largest share
   of every file, and under the ruled default every character of it stays at site.
3. **Where each archive destination is**, for the classes proposed to archive — an existing
   archive file, or a new one created by the executing act on the established pattern.
4. **Which `STATUS.md` entries are SUPERSEDED**, which is the one class this test deliberately
   does not decide. That file's own rule already says a superseded entry moves to `STATUS_ARCHIVE.md`
   instead of accumulating, and ruling (C) brings that rule into the executing act; what the
   measurement adds is that this is the largest single block of the five files.

**★ ONE LIMITATION OF THE MEASUREMENT, STATED RATHER THAN LEFT TO BE FOUND.** A span is classed
from its own text by a recognizer, and a span that is MIXED — live rule text with an archive
marker inside it — is classed by the marker. The span rule cuts a block again at every ★ marker,
which is the record's own way of opening an amendment, and that correction was made because
without it three spans carried 26.8% of `CLAUDE.md` into an archive class. The residual risk is
the same shape at a finer grain, and it runs in the ARCHIVE direction — the one the doubt default
exists to prevent — so the executing dispatch reads every span it archives rather than trusting
its class.

**Nothing here is ruled.** No file is edited, no span is moved, no anchor is re-aimed and no
reader is touched. This surface proposes; the user rules; ONE later dispatch performs — in that
order and no other.

*Generated by `tools/audit/gen_governing_surface_readers.py` from `tools/audit/governing_surface_spans.json` and `tools/audit/governing_surface_readers.json`, 2026-08-16, dispatch `cc_instruction_preparation_fifth.md` Task 2.*
