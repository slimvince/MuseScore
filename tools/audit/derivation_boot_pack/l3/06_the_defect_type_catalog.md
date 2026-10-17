# The defect types — the named shapes of reasoning error

This file is GENERATED. It carries the catalog's TYPE and DEFINITION columns and nothing else: the founding-instance and detection-signature columns are descriptions of this project's implementation and are excluded from this pack by the ruling that admits the catalog.

These are the shapes a derivation must not walk into. They are named here so that a session can check its own work against them by name.

| ID | type (plain) |
|---|---|
| DT-1 | Unverified causal premise carrying load (Class A, #18) |
| DT-2 | Unestablished instrument / constant (Class B, #19), incl. tuned-against-a-broken-instrument |
| DT-3 | Value-copied constants — one decision stored as two named literals that agree by history, not by reference |
| DT-4 | Silent overwrite of a committed field — revision without carrying the original (#12) |
| DT-5 | Siloed / trapped derived fact — computed, then unavailable to other consumers |
| DT-6 | Duplicated derivation — the same verdict recomputed per consumer |
| DT-7 | Never-fires / always-fires mechanism — code whose designed population is empty or total |
| DT-8 | Scale-incommensurable comparison — quantities on different scales compared as if same |
| DT-9 | Unvalidated proxy→target substitution — a structural proxy read as a behavioral quantity |
| DT-10 | One-sided insulation claim — "X cannot affect Y" without the false-negative path enumerated |
| DT-11 | Hand-transcribed measurement number — a figure in a doc with no generated-artifact provenance |
| DT-12 | Stale anchor / dangling reference — file:line anchors or doc references that no longer resolve |
| DT-13 | Interim exception without a wired retirement condition — a "bridge" nothing forces closed |
| DT-14 | Gate/precondition mismatch — a mechanism guarded by a precondition its real population almost never satisfies (the generalized PC-1 shape) |
| DT-15 | Abstention/coverage-movable metric — a quality metric reducible by opting out rather than by being right |
| DT-16 | Raw-source interpretation outside the fact layer — a consumer re-reading the raw score/DOM with private eligibility rules (#7) |
| DT-17 | Silently-truncating capability — a specified trigger/handler that was never coded, failing quiet instead of loud |
| DT-18 | Plumbing commit without working-tree/index sync — a scratch-index commit whose reconstructions were staged to the object DB and the ref moved, but never materialized to disk, so the object DB/ref run AHEAD of the working tree + main index |
| DT-19 | Layer-boundary violation (#7/#6) — a fact/segmentation-layer file depends on a HIGHER analysis layer (upward `#include` back-edge) and/or one module co-locates multiple layers' concerns (grab-bag owner-drift); includes a header comment asserting a back-edge removed while the `.cpp` still has it |
| DT-20 | Self-defeating instruction composition — an instruction (or protocol application) whose mandatory preconditions defeat one of its own requirements, e.g. a required session-start read that leaks exactly what a blinding requirement withholds |
| DT-21 | Layer mis-attribution in the inventory / tag table — a file assigned the WRONG layer (or wrong concern) in the machine file-table, so a later layer audit that INHERITS the tag would deep-audit the wrong file / miss a file. The coarse "deferred to layer X" tags are best-guesses, never established at the code |
| DT-22 | Signed-design rule not honored by a coded mechanism — a BUILT mechanism omits or contradicts an explicit fixed-direction RULE of the signed design (an admission restriction, a weighting direction, a precedence), so it behaves more permissively or less discriminately than the ratified spec. Distinct from DT-17 (a whole capability never coded, failing quiet): here the mechanism IS built and runs — it just diverges from a sub-rule the design fixes. Distinct from DT-2 (a numeric constant off-manifest): the divergence is a structural rule, not a value to fit |
| DT-23 | Silent-failure / silent-drop path in an instrument — a broad or bare `except` (or an error→default fold into the wrong bucket) that discards or mis-attributes data with NO skip-counter and NO surfacing (print/raise), so a SYSTEMATIC failure silently shrinks or mis-buckets the measured population instead of failing loud. Distinct from DT-17 (a specified capability never CODED, failing quiet): here the error handling IS coded — it just swallows the failure. Distinct from DT-4 (silent overwrite of a committed field): the loss is on the error/exception path, not a struct mutation |
| DT-24 | Destructive default output path — an instrument's DEFAULT output/destination argument resolves to a COMMITTED reference (a corpus, a golden, a manifest/registry, a committed map), so a no-arg invocation silently overwrites / re-baselines committed ground truth with no confirmation and no scratch redirect. Distinct from DT-4 (in-memory struct-field overwrite) and DT-23 (an error-path drop): here the loss is a normal-path filesystem write of a committed artifact via a convenience default. Compounds DT-2 when the same tool's output is also unfingerprinted at consume time (the producing-side complement) |
| DT-25 | Undocumented capability / mode on a shared instrument — a flag, mode, or output path the code EXPOSES and parses that NO contract document (the tool's own help text, `BUILD_AND_TEST.md`, `REPRODUCIBILITY.md`) lists, so a runnable measurement path exists that was never surfaced in the instrument's contract (an unratified/unlisted measurement mode on a shared tool). The REVERSE of DT-17 (a specified capability never coded, failing quiet): here the capability IS coded and runnable — it is merely absent from the contract, so a run could produce numbers no document accounts for. Distinct from DT-12 (a doc reference that no longer resolves): here the doc omission is total, not stale |
