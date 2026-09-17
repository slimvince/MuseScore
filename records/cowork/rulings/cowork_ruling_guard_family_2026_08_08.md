# The guard family ruling of 2026-08-08 — ONE design over OI-300's and OI-348's whole family

> **STATUS: RATIFIED RULING RECORD, written 2026-08-08 (Cowork), awaiting application.** Ruled by
> the user on Cowork's decision surface of 2026-08-08 ("ratified", after the full surface — the
> family enumerated, the design with its stated ceiling, and the rejected alternatives — was
> delivered as user-visible text). Interim carrier until the applying dispatch records it
> (D-230). The mechanism change is licensed by this ruling (D-436). It applies the standing
> one-fix-per-family rule (user, 2026-07-28): the remedy is designed once over the enumerated
> family — OI-300's shapes (1)–(5) and OI-348's two — never per symptom.
>
> **The ruling authorizes no fix to the analysis, no design of inference, and no inference
> change. It is a change to the audit's own guard apparatus only.**

## The design, as ratified

1. **Wrapper recursion where a dialect model exists.** The code string of `bash -c`, `sh -c`,
   `powershell(.exe) -Command`, `pwsh -Command` is re-run through the guard's own decision with
   the matching dialect branch — composition of the established POSIX and PowerShell branches
   (#6), no new modeling. Closes OI-348 shape 1.
2. **Interpreter code without a model is decided by POLICY, with a positive bound.** A
   `python -c` / `perl -e` (and kin) code string containing a LITERAL repository path is
   DENIED; anything else is admitted, and the computed-path residual goes into the corpus so
   the published rate REPORTS the ceiling rather than being silent about it (#19; the guard
   cannot parse interpreter code, and pretending otherwise is the unvalidated proxy #17(d)
   forbids). Both measured instances carried literal paths. Closes OI-348 shape 2 to the
   stated bound.
3. **The false-deny shapes are fixed in the same act:** redirection operators and their targets
   classified as non-path tokens (OI-300 shape 5); heredoc body lines excluded from command
   classification (shape 4); and a hashless `git diff` aimed at a working-tree path moved to
   the DENIED side (shape 3 — D-253's own text names it).
4. **OI-300 shape (2) — the unexpanded variable — is closed BY RULING, not by code:**
   deny-on-indeterminate is adopted as standing policy and recorded as such. The asymmetry
   decides it: a false deny costs a retry through the file tools; a false admit costs an
   unverified read through the very mount whose measured stale-content failure created D-253.
5. **Order and establishment — corpus first**, as the OI-343 and OI-345 rulings fixed it: every
   shape enters the establishment corpus BEFORE one line of the mechanism moves; the blindness
   is measured at the unwidened guard; both rates are published on the same extended corpus;
   the revert condition — a material rise in false denials — governs. On success OI-348 closes
   and OI-300's owed list retires with every residual named; a residual that survives is
   recorded in the artifact, never silently.

## The rejected alternatives, recorded with the ruling

A wrapper-only patch (per-symptom — the exact act the family rule forbids). A full shell parser
via an external library (heavier establishment burden, no additional coverage of the ENUMERATED
family; an instance outside the family is a new row on its own evidence). A blanket denial of
all `-c`/`-Command` invocations (fires on legitimate `/tmp` and generator work — the
guard-gets-disarmed failure, recorded as worse than a known gap).

## Application

Its own bounded wave, dispatched AFTER `cc_instruction_document_routes_and_d472.md` returns —
a mechanism change wants a clean tree around it. The dispatch reads this record whole (D-643).
