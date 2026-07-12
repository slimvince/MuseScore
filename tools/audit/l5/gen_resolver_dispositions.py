#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
#
# EG-7 Layer-5 (function) certification — PASS 1, partition 1 (L5-DORMANT resolver
# pipeline). The disposition generator (protocol P1/P2, #17(f) generated-artifact rule):
# it enumerates EVERY deep inventory row tagged to the dormant-resolver population and
# assigns each a verdict from the closed rubric, with a stated reason. "No issue" is
# itself a recorded claim with a reason (P2). Findings are encoded as explicit per-row
# overrides (keyed by file+line / file+name), never hand-typed into the output.
#
# Reads the committed inventory CSVs under tools/audit/l5/ (scope, not verdicts) and
# writes pass1_dispositions_resolver.csv + pass1_dispositions_resolver.json. Read-only
# over the corpus and production code (an audit instrument, not inference code).
#
# Run:  python tools/audit/l5/gen_resolver_dispositions.py

import csv
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# ── Scope: the 20 L5-DORMANT files (function/ + progression/progressionrecognizer) ──
DORMANT_RE = re.compile(
    r'^(src/composing/analysis/function/|src/composing/analysis/progression/progressionrecognizer)')

# Per-file module role (for the reason text of a plain SURVIVES row).
MODULE_ROLE = {
    'forwardoverride':        'the §8 reusable confidence-weighted forward-override mechanism',
    'functioncadence':        'the §5.2 key-agnostic event-pair cadence detector',
    'functionmodulation':     'the §5.3/§5.4 tonicization-vs-modulation arbiter + recompute',
    'functionoutput':         'the §7 output assembly (the L5→L6 contract)',
    'functionprogression':    'the §5.0 licensed-progression grammar (the D5 grammar owner)',
    'functionrelationallabel':'the §5.6 relational-label classifier + unified applied emitter',
    'functionresolver':       'the §5.5 resolver + §8 fine-grain override + bounded-context loop',
    'functionromannumeral':   'the §5.1 base Roman-numeral derivation (a faithful wrap)',
    'tonicizationlabeler':    'the reused §13 dormant applied-chord labeler',
    'progressionrecognizer':  'the §4 progression-recognition consumer of the Harmonic Vocabulary',
}

def module_of(path):
    base = os.path.basename(path)
    return re.sub(r'\.(cpp|h)$', '', base)

# ── Firewall-seed literal detection: a named precision-phase weight/threshold default ──
# These are the parameter-struct field defaults + the inline §7 function-confidence
# magnitudes. All carry load (they are the mechanism's thresholds/weights) and are
# hand-set "NOT tuned" seeds → UNFIT (declared firewall). Whether each is registered in
# tools/param_manifest.json is recorded per-row (only the forwardoverride θ pair is).
FIREWALL_PARAM_NAMES = [
    'baseBar', 'confidenceScale',
    'wBase', 'wBassFiveToOne', 'wLeadingTone', 'wSeventh', 'wMetric',
    'wPhraseBoundary', 'wFinalBar', 'discountHalf', 'discountPlagal', 'discountEvaded',
    'baseChangeCost', 'wDuration', 'wCadentialWeight', 'wSpelling',
    'wCadenceVote', 'wLicensedFit', 'wNextBestMargin', 'kBoundary',
    'wLicensedOut', 'wLicensedIn', 'wCadentialFit', 'decidingMargin',
    'blendRate', 'admissionThreshold', 'modeCueFactor', 'chordsOnlyFactor',
]
# The forwardoverride θ pair is the ONLY L5-DORMANT literal in tools/param_manifest.json
# (group G8, family θ, status "fit", consuming_path "dormant").
IN_PARAM_MANIFEST = {('src/composing/analysis/function/forwardoverride.h', '81'),
                     ('src/composing/analysis/function/forwardoverride.h', '82')}

# The inline §7 function-confidence magnitudes in functionresolver.cpp (the pick(...,conf)
# calls) — hand-set ordinal seeds, NOT registered in param_manifest (a finding).
INLINE_CONF_LINES = {'210', '225', '232', '246', '322', '338'}

def is_double(value):
    return '.' in value

# ── Findings: explicit per-row overrides (file, line) → (finding slug, verdict, note) ──
# Plain-language slugs (no invented numbering scheme). Spelled out in the report. Each
# finding is resolved to a concrete inventory row: the exact (file,line) branch/literal/
# field row when one exists there, else the ENCLOSING FUNCTION row (so every finding is
# attached to a real deep row and appears flagged in the CSV — P1/P2 completeness).
FINDINGS = {}
def add_finding(file, line, slug, verdict, rubric, note):
    FINDINGS[(file, str(line))] = dict(slug=slug, verdict=verdict, rubric=rubric, note=note)

F = 'src/composing/analysis/function/'
# 1. Modulation confirmation admits ALL cadence types (spec + own header say authentic/half only).
for ln in (52, 53, 54, 60):
    add_finding(F+'functionmodulation.cpp', ln,
        'modulation-confirmation-admits-all-cadence-types', 'ASSUMPTION', 'branch',
        'The §5.3/§5.4 cadence-confirmation gate counts ANY FunctionalCadence type with a '
        'matching tonic; the design and this file own header restrict confirmation to an '
        'authentic OR half cadence. A deceptive/plagal/evaded cadence would wrongly confirm '
        'a modulation (a deceptive cadence by definition denies the tonic).')
# 2. Half cadence does not down-weight a seventh / inverted dominant (§5.2 says it should).
add_finding(F+'functioncadence.cpp', 387,
    'half-cadence-no-seventh-downweight', 'ASSUMPTION', 'branch',
    'tryHalf sets genuineDominant=false unconditionally, so a seventh (or inverted) half '
    'cadence gets the same vote as a plain-triad half; §5.2 fixes the direction that a '
    'seventh weakens a half ("down-weighted, not excluded") — the direction is absent, not '
    'merely un-tuned.')
# 3. isAppliedResolution deliberately excludes the augmented same-root (delta 0) edge — in-code flagged.
add_finding(F+'functionprogression.cpp', 122,
    'applied-resolution-augmented-delta0-excluded', 'ASSUMPTION', 'code',
    'The resolutionEdgeBonus augmented->major/minor same-root (delta 0) edge is deliberately '
    'excluded (§5.0 licenses root MOTION); a design decision the code itself flags to Cowork.')
# 4. Grammar §15-12 motions are IN the code — the signed design §5.0/§15-12 still says "pending".
for ln in (62, 71, 80):
    add_finding(F+'functionprogression.cpp', ln,
        'grammar-amendment-landed-design-doc-stale', 'FACT', 'code',
        'isAscendingFifth / isDescendingSecond / isDiatonicDiminishedFifth (the three §15-12 '
        'motions) are implemented; the signed design §5.0/§15-12 still describes the code as '
        'the pre-amendment set "pending dispatch" — the design doc is stale relative to code.')
# 5. Inline §7 function-confidence magnitudes are hand-set and NOT in param_manifest.
for ln in INLINE_CONF_LINES:
    add_finding(F+'functionresolver.cpp', ln,
        'inline-function-confidence-magnitudes-unregistered', 'UNFIT', 'constant',
        'The emitted §7 functionConfidence magnitude (0.25 bass-prior / 0.5 neighbour / 1.0 '
        'progression|cadence) is a hand-set inline ordinal seed NOT registered in '
        'tools/param_manifest.json (unlike the forwardoverride θ pair which is).')
# 6. Augmented-sixth trigger assumes L4 roots the aug6 chord on b6-hat.
add_finding(F+'functionrelationallabel.cpp', 118,
    'augmented-sixth-trigger-assumes-flat6-root', 'ASSUMPTION', 'branch',
    'tryAugmentedSixth fires only when identity.rootPc == tonic+8 (b6-hat); it assumes Layer 4 '
    'roots an augmented-sixth sonority on the lowered submediant. If L4 commits a different '
    'root for the (root-ambiguous) aug6, the trigger does not fire — an engage-time input '
    'contract assumption.')
# 7. Modal-mixture ROLE not tagged for a quality-altered diatonic-root borrowing in a minor key.
add_finding(F+'functionrelationallabel.cpp', 196,
    'modal-mixture-role-minor-key-incomplete', 'ASSUMPTION', 'branch',
    'tryModalMixture tags the ModalMixture role only for a chromatic root or (in Ionian) a '
    'quality-altered diatonic degree; a quality-altered diatonic-root borrowing in a MINOR key '
    'gets no role (label string still correct) — a documented scope limit, declared to Cowork.')
# 8. Punctuation-boundary stop (ii) subsumed into (i) in the dormant bounded-context loop.
add_finding(F+'functionresolver.cpp', 573,
    'decision-context-stop-punctuation-boundary-subsumed', 'ASSUMPTION', 'code',
    'isCutDecision implements decision-context stop conditions (i) cadence-anchor and (iii) K/B '
    'bound but folds (ii) the standalone punctuation boundary into (i) for the dormant resolver '
    '(an engage-time input) — a documented spec-ahead-of-code deferral of stop (ii).')
# 9. combinedBoundary has no guard against kBoundary<=0 (default 1.0 safe; dormant).
add_finding(F+'functionoutput.cpp', 132,
    'combined-boundary-no-kboundary-positivity-guard', 'ASSUMPTION', 'code',
    'combinedBoundary = combined/(combined+kBoundary) has no guard for kBoundary<=0; with '
    'kBoundary=0 and combined=0 it is 0/0 (NaN). The default kBoundary=1.0 is safe and the path '
    'is dormant — a latent edge only if a future caller zeroes the seed.')

# ── Row builders ──────────────────────────────────────────────────────────────────
rows = []  # each: dict(file, dimension, locator, line, verdict, rubric_class, reason, flagged, finding)

def emit(file, dimension, locator, line, verdict, rubric_class, reason):
    rows.append(dict(file=file, dimension=dimension, locator=locator, line=int(line),
                     verdict=verdict, rubric_class=rubric_class, reason=reason,
                     flagged='no', finding=''))

def read_csv(name):
    path = os.path.join(HERE, name)
    with open(path, newline='', encoding='utf-8') as fh:
        return [r for r in csv.DictReader(fh) if DORMANT_RE.match(r['file'])]

# Function ranges (for the enclosing-function fallback of a finding).
FUNC_RANGES = {}  # file -> list of (start, end, name)
for r in read_csv('l5_functions.csv'):
    FUNC_RANGES.setdefault(r['file'], []).append(
        (int(r['start_line']), int(r['end_line']), r['name']))

# functions (87) — every function re-affirmed L5-DORMANT / SURVIVES.
for r in read_csv('l5_functions.csv'):
    mod = module_of(r['file'])
    emit(r['file'], 'function', f"{r['name']}@{r['start_line']}", r['start_line'], 'SURVIVES', 'code',
         f"L5-DORMANT function in {MODULE_ROLE.get(mod, mod)}; no production consumer "
         f"(only {mod}_tests + the batch_analyze diagnostic); byte-identical on production.")

# decls (28) — type/struct/enum declarations on the dormant contract surface.
for r in read_csv('l5_decls.csv'):
    emit(r['file'], 'decl', f"{r.get('name','')}@{r['line']}", r['line'], 'SURVIVES', 'code',
         "L5-DORMANT type declaration on the dormant value/contract surface; no production use.")

# crosslayer (37) — includes. All forward/lateral; no backward (higher-layer) include.
for r in read_csv('l5_crosslayer.csv'):
    tgt = r.get('target_area', '')
    if tgt == 'external':
        reason = "external/std-library include; no layer coupling."
    elif tgt == 'function':
        reason = "sibling L5 function/ include (the §6 single-owner reuse, not duplication)."
    else:
        reason = (f"forward/lateral include of the {tgt} substrate (L5 consumes L1-L4 + "
                  f"vocabulary/spelling); consistent with the §2 forward-only constraint.")
    emit(r['file'], 'crosslayer', f"{r.get('include','')}@{r['line']}", r['line'], 'SURVIVES', 'crosslayer', reason)

# fields (225) — data members on the dormant value/contract structs.
for r in read_csv('l5_fields.csv'):
    emit(r['file'], 'field', f"{r.get('name','')}@{r['line']}", r['line'], 'PUBLISHED', 'field',
         "Field on an L5-DORMANT value/contract struct; part of the dormant output surface "
         "(read by the module tests and, at engage, the L5->L6 consumer). No siloed/trapped "
         "datum found at the struct surface; a per-field consumer trace is an engage-step item.")

# literals (183) — constants.
for r in read_csv('l5_literals.csv'):
    val = r['value']
    ctx = r.get('context', '')
    loc = f"[{val}]@{r['line']}"
    # A firewall SEED is the INITIALIZER of a named param field ("<name> = <value>"),
    # not a comment mention of the name nor a use of the param variable on the line.
    seed_hit = is_double(val) and any(
        re.search(rf'\b{nm}\s*=\s*{re.escape(val)}\b', ctx) for nm in FIREWALL_PARAM_NAMES)
    if seed_hit:
        manifest = 'IN param_manifest.json (G8/theta)' if (r['file'], r['line']) in IN_PARAM_MANIFEST \
                   else 'NOT in param_manifest.json'
        emit(r['file'], 'literal', loc, r['line'], 'UNFIT', 'constant',
             f"Named precision-phase weight/threshold default (hand-set 'NOT tuned' firewall "
             f"seed); {manifest}. Dormant: changes no production output. Only the direction is "
             f"fixed by the design; the value is a Stage-5 fit candidate.")
        continue
    if val == '1920.0':
        reason = "FACT: MuseScore whole-note tick unit (480 ticks/quarter) — a stable time unit, not a threshold."
    elif val == '0.2':
        reason = "Uniform idiom prior (1/5 over the five ratified idioms) — established, sums to 1."
    elif is_double(val):
        reason = ("Structural double (a zero/one identity default, a [0,1] clamp bound, a "
                  "boolean-as-double 1/0 indicator, or a >0 guard) — not a tuned parameter.")
    else:
        reason = ("Music-theory interval or structural integer (a mod-12 root-motion/scale-degree "
                  "constant, the octave modulus 12, an array size 5/7, or a -1/0 sentinel/index) "
                  "— established by theory or by construction, not tuned.")
    emit(r['file'], 'literal', loc, r['line'], 'ESTABLISHED', 'constant', reason)

# branches (255) — control-flow decisions; premise labeled per branch.
GUARD_RE = re.compile(r'(<\s*0|>=?\s*(size|n\b|.*\.size)|rootPc\s*<|== -1|!=\s*nullptr|'
                      r'\bempty\(\)|\.size\(\)|>=\s*0|Index\s*<|Index\s*>=|i\s*[<>]=?\s*|< 0\.0|<= 0\.0)')
for r in read_csv('l5_branches.csv'):
    ctx = r.get('context', '')
    loc = f"{r.get('kind','')}@{r['line']}"
    if GUARD_RE.search(ctx):
        emit(r['file'], 'branch', loc, r['line'], 'SURVIVES', 'branch',
             "FACT (defensive): a structural range/null/empty guard — a construction invariant, "
             "not a musical judgment. Dormant.")
    else:
        emit(r['file'], 'branch', loc, r['line'], 'SURVIVES', 'branch',
             "THEORY (music-theory / design decision): a functional-harmony test whose premise is "
             "cited to the signed design §5.x (root-motion, cadence-form, precedence, or the "
             "firewall threshold direction). Dormant.")

# ── Resolve every finding to a concrete row, and flag it ────────────────────────────
def enclosing_function_line(file, line):
    for (start, end, name) in FUNC_RANGES.get(file, []):
        if start <= line <= end:
            return start
    return None

resolved_findings = set()
for (ffile, fline), fdata in FINDINGS.items():
    fline_i = int(fline)
    # 1) exact (file,line) row of the finding's rubric dimension.
    dim = {'branch': 'branch', 'constant': 'literal', 'field': 'field'}.get(fdata['rubric'])
    target = None
    if dim:
        for row in rows:
            if row['file'] == ffile and row['line'] == fline_i and row['dimension'] == dim:
                target = row
                break
    # 2) else the enclosing FUNCTION row (code-level or non-matching findings attach here).
    if target is None:
        encl = enclosing_function_line(ffile, fline_i)
        if encl is not None:
            for row in rows:
                if row['file'] == ffile and row['line'] == encl and row['dimension'] == 'function':
                    target = row
                    break
    if target is None:
        raise SystemExit(f"UNRESOLVED FINDING {fdata['slug']} at {ffile}:{fline} — fix the anchor")
    target['verdict'] = fdata['verdict']
    target['reason'] = fdata['note'] + f" [finding anchor {ffile}:{fline}]"
    target['flagged'] = 'yes'
    target['finding'] = fdata['slug']
    resolved_findings.add(fdata['slug'])

# ── Write the artifacts ─────────────────────────────────────────────────────────────
rows.sort(key=lambda r: (r['file'], r['dimension'], r['locator']))

csv_path = os.path.join(HERE, 'pass1_dispositions_resolver.csv')
with open(csv_path, 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=['file', 'dimension', 'locator', 'line', 'verdict',
                                       'rubric_class', 'reason', 'flagged', 'finding'])
    w.writeheader()
    for r in rows:
        w.writerow(r)

# Summary: counts per dimension and per verdict; the flagged rows; the findings roster.
by_dim = {}
by_verdict = {}
for r in rows:
    by_dim[r['dimension']] = by_dim.get(r['dimension'], 0) + 1
    by_verdict[r['verdict']] = by_verdict.get(r['verdict'], 0) + 1
flagged = [r for r in rows if r['flagged'] == 'yes']
finding_slugs = sorted({r['finding'] for r in flagged if r['finding']})

summary = {
    'audit': 'EG-7 Layer-5 (function) certification, PASS 1, partition 1 (L5-DORMANT resolver pipeline)',
    'instruction': 'cc_instruction_l5_audit_pass1_resolver (Cowork, 2026-07-12)',
    'scope': {'tag': 'L5-DORMANT', 'files': 20, 'deep_rows': len(rows)},
    'freeze_head_commit_of_inventory': 'c081f79f63fa0daff934e32236651141cb2858b6',
    'corpus_hash': 'c50002fee1',
    'rows_total': len(rows),
    'by_dimension': by_dim,
    'by_verdict': by_verdict,
    'flagged_row_count': len(flagged),
    'findings': finding_slugs,
    'note': ('READ-ONLY fact-finding; no production behaviour changed. Verdicts are the '
             'auditor blind-pass judgment (P1/P2). "No issue" rows carry a stated reason. '
             'Findings are per-row overrides spelled out in cc_l5_audit_pass1_resolver_report.md.'),
}
json_path = os.path.join(HERE, 'pass1_dispositions_resolver.json')
with open(json_path, 'w', encoding='utf-8') as fh:
    json.dump(summary, fh, indent=1)

all_finding_slugs = sorted({v['slug'] for v in FINDINGS.values()})
unresolved = [s for s in all_finding_slugs if s not in resolved_findings]
print(f"rows: {len(rows)}")
print(f"by_dimension: {by_dim}")
print(f"by_verdict: {by_verdict}")
print(f"flagged rows: {len(flagged)} across {len(finding_slugs)} findings")
for s in finding_slugs:
    print(f"  - {s}")
if unresolved:
    raise SystemExit(f"UNRESOLVED FINDINGS: {unresolved}")
print("all findings resolved to a real deep row.")
