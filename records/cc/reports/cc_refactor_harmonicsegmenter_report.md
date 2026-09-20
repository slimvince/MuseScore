# Refactor report — split `harmony/harmonicsegmenter.cpp` (boundary primitives)

**Result: STOP — surfaced, not forced. No code changed, no commit made.**

HEAD at investigation: `2024f2951e` (refactor: split sectionanalyzer.cpp …).

## §1 What was requested

Peel the boundary-detection primitives (`collectNoteChangeTicks` and siblings)
off the `greedyExpandSegmentation` policy function into a new sibling TU
(`harmony/segmentationprimitives.cpp`), **strictly byte-identical / pure code
movement**. The binding purity rule (task §1, §5) requires: move a function only
if it is **already external/header-declared OR an anon-namespace helper that can
move WITH all its callers** (so no linkage promotion is needed). A piece needing a
linkage promotion / new declaration to separate is the *sectionanalyzer Pass-4
case* → **STOP, surface, do not force.**

## §2 Source of truth — linkage and call graph (fresh reads, this HEAD)

Header `harmonicsegmenter.h` declares **only two** symbols with external linkage:
`greedyExpandSegmentation` (L96) and `placedRegionsToTicks` (L110). Everything
else in `harmonicsegmenter.cpp` lives in the file's anonymous namespace (L59–563)
— internal linkage, invisible to any other TU.

Anonymous-namespace contents and their call sites (verified by repo-wide grep;
the other `fillGap` hits in `engraving/` and `importexport/` are unrelated
functions in different namespaces):

| Helper (anon ns, internal linkage) | Defined | Called by | Sole caller = residual? |
|---|---|---|---|
| `qualityToString` | L63  | `fillGap` (476, 559) **and** `greedyExpandSegmentation` (745, 822, 862, 871, 914) | caller set includes residual |
| `isOnBeat` | L81  | `greedyExpandSegmentation` only (712) | **yes** |
| `countParticipatingStaves` | L93  | `greedyExpandSegmentation` only (611, 718) | **yes** |
| `collectNoteChangeTicks` | L152 | `greedyExpandSegmentation` only (577) | **yes** |
| `fillGap` | L323 | `greedyExpandSegmentation` only (769, 776, 783) | **yes** |

The entire anonymous namespace is a single internal-linkage dependency cluster
that funnels into `greedyExpandSegmentation`. `fillGap` additionally calls
`qualityToString`.

## §3 Why no byte-identical split exists

The named targets — `collectNoteChangeTicks`, `countParticipatingStaves`,
`isOnBeat` — are exactly the *anon-namespace-helper-whose-sole-caller-is-the-
residual* shape. Moving any of them to a new TU while leaving
`greedyExpandSegmentation` behind requires **promoting them from internal linkage
to external linkage and adding a new declaration** so the residual TU can still
call them across the TU boundary. That is, by the task's own definition, **not a
verbatim move** — it is the explicit STOP condition (§1, §5 "the sectionanalyzer
Pass-4 case").

The alternatives were each checked and rejected:

- **Move the primitives, keep `greedyExpandSegmentation`** → residual calls
  internal-linkage symbols now in another TU → link failure unless promoted →
  linkage promotion + new declaration → STOP.
- **Move the policy (`greedyExpandSegmentation` + `fillGap` + `qualityToString`),
  keep the primitives** → the moved `greedyExpandSegmentation` calls
  `collectNoteChangeTicks`/`countParticipatingStaves`/`isOnBeat`, still internal
  to the old TU → same linkage promotion → STOP. (Also inverts the requested
  direction.)
- **Move the whole cluster together** (greedyExpandSegmentation + all five anon
  helpers) → that does not *separate* the primitives from the policy at all; it
  just renames the file and leaves only the trivial `placedRegionsToTicks`
  behind. Not the requested split, and not a meaningful layer separation.
- **Move only `placedRegionsToTicks`** (the one freely-movable symbol — external,
  no in-TU callers, no helper deps) → byte-identical and trivial, but it is **not
  a boundary-detection primitive**; it is a result→ticks converter. Does not
  satisfy the assessment's intent of peeling primitives off the god-function.

There is no cut of this TU that (a) separates the boundary-detection primitives
from `greedyExpandSegmentation` and (b) keeps every moved helper together with all
its callers. The coupling is structural: the primitives have no consumer other
than the policy function.

## §4 Acceptance gate

Not reached — no build/test run, because no byte-identical move is available to
gate. Per task §5 the correct action at a linkage-promotion boundary is to stop
before changing code.

## §5 Recommendation

The clean separation the assessment wants (primitives in their own TU) is
achievable, but **only via a linkage promotion** — e.g. declare the three
primitives in a small internal header (`segmentationprimitives.h`) under
`mu::composing` (or a `detail` namespace) and give them external linkage, then
move their definitions to `segmentationprimitives.cpp`. That is a deliberate
interface-introducing refactor, **not** the byte-identical pure-move this task is
scoped to, and it requires explicit approval (it adds a declaration / changes
linkage, and would warrant its own behavior-identity verification even though the
logic is unchanged).

**No change committed. Awaiting direction:** (a) approve the linkage-promotion
variant as a separate, non-"byte-identical-pure-move" step, or (b) skip this
candidate and move to the next pure-split candidate in the assessment.
