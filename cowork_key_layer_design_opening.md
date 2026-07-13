# The key-layer design conversation — opening document

> **Cowork, 2026-07-12.** The design conversation the user scoped at the start of the
> arc — mode/key + chord inference, where and how — now opens on complete inputs: the
> honest measurement columns (OI-142/OI-143), the failure taxonomy (the OI-141
> diagnosis), the research grounding (`cowork_key_drift_research_grounding.md`), and
> the decode mechanism pinned at the code (`cc_l3_key_decode_mechanism_report.md`).
> This document lays out the design decisions with their grounded options and
> Cowork's written expectations. It decides nothing; every decision is the user's,
> every build waits for its proper stage, every constant-fit waits for the fitting
> stage.
>
> **The user's standing frame for all of it (stated 2026-07-12, restating guiding
> principle 4):** the long-term objective is MAXIMUM-PRECISION inference. Complexity,
> large amounts of code, architecture redesign where needed, and long analysis times
> are all acceptable costs. The sanctioned latency valve already exists in the
> ratified architecture: the **effort preset** (quick / normal / ambitious,
> `ARCHITECTURE.md` §2.14 — defined, deliberately not yet implemented, added after
> profiling), with its two standing rules: every cost-driving choice is an explicit
> setting, never a hardcoded constant; every optional expensive refinement is a
> cleanly separable on/off stage. Precision-bearing design below is therefore never
> rejected for cost; cost only decides which effort tier a refinement defaults into.
>
> **The ratified structural frame any design must fit** (`ARCHITECTURE.md` §2.14,
> user-ratified): layers are forward-only; each emits ranked candidates plus a
> confidence, never a forced point estimate; "revise on later evidence" is the
> confidence-weighted forward-override with a localized, region-scoped forward
> recompute — and the architecture ALREADY names the **cadence-confirmed key
> override** as one such forward recompute. A design needing more than that does not
> get a hidden back-edge; it proposes a layer redesign openly (guiding principle 7,
> worst case) and gets ratified or rejected as such.

## 1. The established inputs (pointers, not restatements)

- **Mechanism (pinned at code):** all 252 key/mode states are scored per slice; the
  sequence search runs only over the union of per-slice top-8 states; region commit
  is a faithful reduction of the global decode; the carry truncates at 4 and drops
  the margins. Traced failure weights: the emission model and its ±4-beat window
  (2 of 3 traces, including one true key ranked 116th), the single unfit change cost
  (1 of 3 — over-smoothing through a real modulation), the top-8 prune (secondary),
  the carry cap (downstream only).
- **Honest columns:** key-agree HOME 71.29/67.49/70.52, LOCAL 65.72/62.49/65.39
  (Baroque/Jazz/Default) — the local column is the fitting objective for everything
  below; the home-minus-local gap is the measured stickiness.
- **Taxonomy:** wrong-key-area drift leads the genuine errors; relative-key
  confusion second (with the true key's leading tone present-but-unused in ~57 % of
  that class); tonicization-versus-modulation is a convention boundary now visible
  via the dual columns.
- **The June cadence→key dossier** (`cc_cadence_key_investigation_dossier.md`,
  2026-06-14, pre-dating the robust unit — its sizing needs re-validation on the
  current columns). Plainly: a cadence is the dominant-resolving-to-tonic arrival
  formula at a phrase end — the single most key-revealing fragment of a chord
  progression, since it names the tonic. The dossier's finding: a cadence→key signal structurally supplies the missing
  relative-pair evidence and addressed ≈91 % of that era's mode-absent floor; the
  then-existing cadence detector was unusable (circular — it presupposes the key);
  the recommendation was a NEW key-agnostic cadence pre-scan voting tonic+mode from
  root motion and the raised leading tone. **Claim to verify, not assume:** the
  dormant, certified layer-5 cadence machinery (`functioncadence.cpp`) appears to BE
  that pre-scan's built form — it derives a tonic vote from root motion and chord
  quality, key-independently. If verified, the "new detection work" the dossier
  priced is already built and audited.
- **Dormant/unused assets, all audited:** the phrase-boundary view (gated off), the
  cadence/modulation machinery (dormant, two signed-rule divergences to reconcile),
  the declared mode (siloed), the notated mid-piece key change (never re-anchored),
  the runner-up margins (computed, discarded), spelling facts (carried at the note
  layer, consumed only by one pin).

## 2. The design decisions, each with grounded options and a written expectation

**Decision 1 — search completeness: retire the top-8 union prune.** The literature
decodes the full lattice; 252 states is computationally trivial; the prune made one
traced true key unsearchable. Expectation, written: going full-lattice alone changes
few winners (under 1 point — the absent keys are absent because the emission ranks
them low, and search membership does not fix rank) but removes a structural
impossibility and is the enabling precondition for every evidence improvement below.
Essentially free; no effort-tier needed.

**Decision 2 — the emission model (the largest measured lever).** Options, all
compatible and separately measurable:
(a) **spelling-aware profiles** — Temperley's tonal-pitch-class variant, verified
in-paper at +3.6 points; our spelled-pitch facts already exist at the note layer
(the register's spelling channel). Expectation: the single best-grounded emission
improvement; most of its value lands on the relative and parallel-mode classes.
(b) **leading-tone/accidental evidence** — measured present-but-unused in ~57 % of
the failing relative class. Partly subsumed by (a); worth its own term only if (a)
under-delivers.
(c) **window treatment** — one traced failure flips correct purely by window width.
Options: a fitted width; or multi-scale emission (score at several widths, the
sequence decode arbitrates) — more code, cleanly separable, a natural "ambitious"
effort-tier resident. Expectation: multi-scale beats any single fitted width on the
wrong-area class; magnitude unknown, measurable read-only offline.
(d) **input weighting check** — Temperley's flat-input finding (presence beats
duration weighting; repeated notes over-weight). Cheap offline A/B against our
current weighting; direction unknown for our corpus — that is why it is measured.
(e) **profile fitting** — the mode priors and emission weights are hand-set; they
become fitting-stage targets against the local column regardless of (a)–(d).

**Decision 3 — the transition model (the stickiness lever).** Options:
(a) **phrase-boundary-modulated change costs** — cheaper transitions at phrase ends;
the comparable product's single biggest published win; our phrase-boundary view is
built and gated off. The phrase-end facts themselves come from TWO score signals
jointly (the evidence inventory, user-enriched 2026-07-12): fermatas (the chorale
convention, currently unread) and sufficiently long rests (the dormant view's
existing mechanism, its threshold hand-set and unfit). Expectation: the
best-grounded structural transition change; directly attacks the home-versus-local
gap.
(b) **the cadence→key channel** — the June dossier's green light + the ratified
cadence-confirmed forward override + the (to-be-verified) already-built tonic-voting
machinery. The one genuine ARCHITECTURE question in this conversation: where the
key-agnostic cadence primitive LIVES so that layer rules hold — published as an
early analysis fact consumable by the key decode, versus consumed later as the
forward-override trigger. Both fit the forward-only frame; the first informs the
decode itself, the second corrects it after. Expectation: this channel is what holds
the true key through a real modulation (the traced over-smoothing case) and what the
relative floor has been waiting for; it is the largest single precision opportunity
in this document.
(c) **key-proximity-structured costs** — standard in the HMM tradition, but our
measured caution stands: our drift lands exactly on proximate keys; proximity priors
alone could worsen it. Only with (b) as the counterweight.
(d) **tonicization modeling** — short excursion spans distinguished from committed
modulations, aligning our output with the local-key convention the new column grades
against; the public modulation/tonicization dataset can calibrate the boundary.
Expectation: this converts a large share of the remaining label-gap class into
agreement without touching the hard cases.
(e) **progression-grammar evidence** (added at the user's question, 2026-07-12):
progressions are key-relative — the same chord roots that are grammatical I–IV–V–I
under one key are nonsense under its relative — so HOW WELL the observed sequence
matches known progressions UNDER EACH CANDIDATE KEY discriminates between keys even
where the chords themselves cannot. The assets exist dormant and audited (the
harmonic vocabulary catalog; the licensed-progression grammar). The cadence channel
(b) is this channel's sharpest special case — a dominant-to-tonic arrival names the
tonic directly — which is why (b) leads. MEASURED CAUTION attached: the one deployed
use of the licensed-progression signal (as a CHORD-selection override) measured
net-harmful and uncorrelated with correctness; that condemns assuming, not this use —
so (e) enters only through a written prediction and a read-only probe: grammaticality-
under-candidate-key scored on the measured failing classes, discrimination reported
before any design commits to it.

**Decision 4 — anchoring.** Re-anchor at notated mid-piece key-signature changes
(a known, bounded gap); integrate the declared mode as a graded prior rather than a
silo. Small, grounded, low-risk; mostly bookkeeping-level design.

**Decision 5 — the output surface (the fact-publication decision).** Publish the
ranked alternatives WITH their margins (ending the computed-then-discarded waste);
populate the per-alternative confidence; state the consumers: the chord layer's
diatonic prior, the function layer, the tonicization arbitration, and any future
revisit of the shelved joint step. Per the fact-publication corollary, each published
fact names its consumer or its declared dormancy.

**Decision 6 — the state space itself.** 252 = 12 tonics × 21 mode rows. The mode
inventory is a design input never revisited since it was hand-set: which modes earn
states per preset, how harmonic/melodic minor variants are represented, whether any
rows are dead. An enumeration-and-justification pass belongs to this design before
any fitting bakes the current inventory in.
*Enriched 2026-07-12 from the mode-grading adjudication and the published record:*
the key-detection tradition for common-practice music runs 24 states (12 major + 12
minor) — no published tracker emits jazz-scale keys; the Baroque-relevant modal
residue in the scholarship is the four church modes (Phrygian, Mixolydian, Dorian,
Aeolian — Burns, "Bach's Modal Chorales"), NOT the dominant-family jazz scales; our
hand-set Baroque priors are near-backwards against that record (church modes
suppressed, Phrygian dominant boosted +0.50 — the value the adjudication probe
caught mislabeling); and the annotators grade everything as major/minor regardless.
**The user's direction (2026-07-12), recorded for this decision:** in the Baroque
inventory only ordinary major and minor carry high priority; the dominant-family
exotics are candidates for retirement from that inventory (dominant-heaviness
re-expressed as evidence — the cadence/dominant channels), with the church modes the
one scholarly-supported question to settle; the Jazz inventory legitimately keeps
the chord-scale modes (unestablishable until jazz ground truth exists, OI-7); the
Default inventory is DEFERRED pending the corpus-expansion evidence (OI-38/OI-39).
Sequencing per the readiness gate: the inventory decision comes FIRST, then the
surviving priors are FIT against the local column at the fitting stage — never
hand-set again; no ad-hoc prior adjustment now.
*Refinement (user, 2026-07-13): the chord-scale mode names are an established,
published naming convention, and the detections are USEFUL — the probe showed the
flagged spans are real (dominant-saturated music); only the ROLE was wrong. So the
direction is: KEEP the vocabulary and the detection, CHANGE THE JOB — the mode fit
becomes a published EVIDENCE fact (feeding the dominant-shape/cadence channels, the
smörgåsbord, and the declared intonation consumer), while the KEY state space per
preset is curated separately. Nothing detected is discarded; a fact miscast as a
conclusion becomes an input.*
**★ THE GOVERNING FRAMING (user-ratified 2026-07-13, superseding retire-vs-keep):
infer the mode as precisely as the evidence allows, always; carry the rich answer
(#12); bind interpretations LATE — at three depths.** (1) NEVER bound: the rich
per-state fit is always computed and always PUBLISHED (the emission already scores
all 252 states; publishing is free; discarding at inference time is where
information dies today). (2) Bound at INFERENCE, per preset: which states may WIN
the committed key — not deferrable to display (mid-pipeline consumers read the
committed key), softened by the collection insight (an exotic mode shares its
parent's collection, and the chord layer mostly consumes the collection), governed
by the preset mode-priors, FITTED not hand-set — "Baroque ≈ major/minor" lives here
as fitted weights, not deleted vocabulary. (3) Bound at each CONSUMER: grading
reduces by the annotators' convention (landed); DISPLAY reduces by the preset's
presentation choice, very late, possibly a user setting (a Baroque user sees
major/minor — or "G minor, dominant-colored" on request; a Jazz user sees "G alt");
the chord layer binds to the collection; intonation binds to the full scale
identity. Nothing lost anywhere; everything interpreted exactly as late as its
consumer permits.

**Decision 7 — the structural fit.** Everything above lives inside the ratified
forward-only frame — including the cadence channel, which the architecture already
sanctions in override form. If measurement later shows an option genuinely requires
more (a true joint re-decode, a back-edge), that finding comes back here as an open
layer-redesign proposal under principle 7 — named, costed, ratified — never as a
quiet patch. The shelved joint key↔chord step stays shelved on its measured record;
nothing in this document reopens it.

## 3. The order of work (the funnel, per item)

Design ratification here → desk simulation on the traced cases → read-only offline
probes (the emission and lattice options are all measurable from dumped emissions
without touching production) → ratified builds at the key layer's proper stage under
the certified-layer discipline → constants fit at the fitting stage against the
LOCAL column, under the hard stop and both key columns. Every item gets its register
row and its written predictions at dispatch time; the numbers above marked
"expectation" become those predictions.

## 4. The cheapest deciders, recommended first (all read-only)

1. **The offline re-decode probe:** re-run the sequence decode offline from the
   existing 252-state emission dumps — full-lattice versus top-8, and window variants
   — grading both key columns. One instrument answers Decisions 1 and 2(c)/(d)
   before any design is built.
2. **The cadence-vote coverage probe:** run the dormant tonic-voting cadence
   machinery offline over the failing classes — does its vote point at the true key
   in the over-smoothing and relative-confusion cases? This verifies the dossier's
   ≈91 % claim on the honest columns and settles whether the built machinery is the
   called-for pre-scan.
3. **The spelling-profile desk simulation:** hand-trace the Temperley spelling
   variant through the traced failures before any profile work is designed.
4. **The progression-grammar discrimination probe** (the user's channel, decision
   2 option (e) of the transition section): score the observed chord sequence's
   grammaticality under each candidate key on the measured failing classes, read-only
   from existing outputs and the dormant grammar; report whether it discriminates,
   with the prediction written at dispatch time. Runs naturally together with the
   cadence-vote probe (same inputs, same population).

## 5. Uncertainty flags (honest)

- The "the dormant cadence machinery IS the called-for pre-scan" identification is
  argued from its shape, not yet verified at code against the dossier's requirements
  — first item of the cadence-vote probe.
- The ≈91 % dossier figure is from a pre-robust-unit metric era and a floor
  population that no longer exists in that form; treat as directional until re-run.
- The effort preset is defined, not implemented; nothing below depends on it
  existing yet — it only names where expensive refinements default when they land.
- All magnitude expectations in §2 are Cowork's grounded estimates, written to be
  checked by the §4 probes, not to be right.

*Cross-references: OI-141 (the line of work), OI-75/OI-81/OI-94/OI-78/OI-15 (the
unused assets), OI-91/OI-97 (the unfit constants), OI-118/OI-119 (cadence machinery
divergences to reconcile before it engages anywhere), OI-44 (the joint step's
declared status, untouched), `ARCHITECTURE.md` §2.14 (the ratified frame + the
effort preset), and the four assembled inputs named in the preamble.*
