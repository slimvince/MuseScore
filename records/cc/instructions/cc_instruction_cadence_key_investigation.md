# CC Instruction: Cadence→Key investigation — does a global/cadential signal close the relative-pair floor?

## Authorization + framing

Stage 4b-ii proved (rigorously, `cc_stage4b_ii_report.md`) that **reweighting local note terms cannot
carry the relative-major/minor decision** — the floor regions are the sub-1.0-hint near-ties, and any
local term strong enough to win them mode-absent overrides the correct hint mode-present (the §4
structural coupling). The finding pinpoints a **missing signal**: the *global/cadential identity of the
key* (which relative the piece resolves to, integrated over the whole piece, not the lookahead window) —
the thing the declared mode was a proxy for.

This run **investigates whether a cadence→key signal actually supplies that missing signal — DERIVED on
real floor cases, BEFORE any build.** It is modeled on the beam-widening and key-path investigations,
which *falsified* their fixes by deriving against real margins. **A negative result here is a valid,
valuable outcome** (it would push the key axis toward Stage 6 / a learned emission). Do NOT build the
cadence→key wiring; derive its feasibility.

**Constraints:** READ-ONLY analysis + measurement. No production behavior change. A read-only,
byte-identity-gated diagnostic dump is permitted *if needed* to inspect cadence evidence on floor cases
(the `--dump-key-candidates` precedent: optional out-param, 0/353×3 sha256, default off). HELD — no
commit. Never-guess: read the cadence detector at source; sample REAL cases; tag every claim `[probe]`
(measured) / `[code]` (read at source) / `[oracle]` (DCML/music21) / `[unknown]` (stated, not guessed).

## The load-bearing question (the make-or-break — §4 coupling escape)

4b-ii's coupling is the thing to beat. The other levers failed *because they are local-window-salience
terms deciding the same sub-1.0 near-ties as the hint.* **Cadence is a candidate precisely because it is
global/phrase-level, not window-local — so it CAN point differently from local salience.** But that must
be **derived, not assumed:**

> **Q-CENTRAL:** On the floor population (the ~1383 Default sub-1.0 relative-pair near-ties), does the
> cadential/global evidence point to the **correct** relative (oracle/DCML), AND is it **decoupled** from
> the local near-tie salience — i.e. can it win these cases mode-absent **without** overriding the correct
> 1.0 hint mode-present? If cadence is just another local term that re-enters the same coupling, it fails
> like the others — report that as the finding.

## Tasks

1. **Locate + characterize the cadence machinery [code].** Find the Stage-2.1-relocated cadence/pivot
   detector (composing section analyzer per the 2.1 move — locate and quote file:line). What does it
   actually produce (cadence type? location? confidence? does it identify the resolution *key*/*degree*,
   or only that a cadence occurred)? Is it per-region, per-section, or whole-piece? Does anything
   currently feed it into `analyzeKeyMode` / `keyresolver`? (4b-ii §2 said no cadence term feeds key
   scoring — confirm.) This establishes what raw signal is available without new detection work.

2. **Characterize the floor population [probe] [oracle].** From the 4b-i mode-absent floor, isolate the
   relative-pair near-tie regions (the sub-1.0-gap cases — reuse the `--ignore-declared-mode` +
   `--key-breakdown` machinery and the dump). How many are there; what are their DCML resolutions; how
   many sit in pieces with a clear final/structural cadence vs none. This bounds the *addressable* set.

3. **Derive Q-CENTRAL on a real sample [probe] [oracle].** Take a representative sample of floor cases
   (incl. bwv365/33.6/64.2/83.5 and a spread of others). For each: does the cadential/global evidence
   (final cadence, V→i vs V→I, leading-tone-of-the-relative resolution, dominant-of-the-true-tonic
   recurrence) actually *discriminate the correct relative*, where the local window salience is balanced?
   Quantify: of the sampled floor cases, what fraction would a cadence signal resolve **correctly**, and
   critically — does it do so on cases the local hint got **right** mode-present **without flipping them**
   (the coupling-escape test)? If cadence and the hint agree on the mode-present winners but cadence ALSO
   resolves the mode-absent floor, the signal is decoupled (the fix is viable). If cadence can't separate
   them, or only wins the floor by also flipping correct mode-present cases, it re-enters the coupling
   (the fix is not viable — a finding).

4. **Size the recoverable fraction + the residual [probe].** Of the +1383 Default floor: how much does a
   cadence signal plausibly close (the Task-3 fraction), and what residual remains genuinely unreachable
   by cadence (→ the hard class bwv64.2/83.5; pieces with no clear cadence; ambiguous repertoire)? The
   residual is the A-vs-B input: large residual ⇒ the key axis needs a learned/richer emission (B);
   small residual ⇒ hand-built cadence→key (A) suffices for the key axis.

5. **Calibrate + recommend [code/probe].** Against the literature (cadence-based key finding; the
   Temperley/HarmAn line) note whether cadence-anchored relative resolution is a known-sound approach.
   Recommend the Stage-4 shape: (a) build cadence→key as the next hand-built composing step (with the
   concrete wiring sketch — how the cadence output would feed `analyzeKeyMode`/`keyresolver`, and whether
   it escapes the coupling by being applied at section/piece scope not window scope); or (b) fold it into
   Stage 6 (co-developed with the functional layer); or (c) the cadence signal is insufficient → the key
   axis is a Stage-6/learned-emission (B) problem. Re-scope OQ6's pass-bar onto whichever lever this names.

## Deliverable — `cc_cadence_key_investigation_dossier.md`

The Q-CENTRAL derivation (decoupled or not — with the real-case evidence), the floor characterization,
the recoverable-fraction + residual sizing, and the Stage-4-shape recommendation with the A-vs-B read.
Every number `[probe]`, every root `[oracle]`. HELD — no production change, no commit. If a byte-identity
diagnostic was added, report its 0/353×3 proof.

## Stop conditions
- Catching yourself **building** the cadence→key term/wiring (this run derives feasibility; building is a
  later, separately-ratified step) — stop and report the derivation instead.
- The cadence signal failing to discriminate the floor, or failing the coupling-escape test — that is the
  **finding** (key axis → Stage 6 / learned emission); report it plainly, do not force a fix.
- Any production behavior change, or a diagnostic that isn't byte-identical (0/353×3) — surface it.
- The cadence detector not actually producing a usable key/degree resolution (only a cadence flag) —
  report what *would* be needed (new detection work) as a sizing finding, don't build it.
