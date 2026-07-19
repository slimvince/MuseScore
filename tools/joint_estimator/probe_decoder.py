#!/usr/bin/env python3
"""probe_decoder.py — the joint-estimator PROBE DECODER (the #17 funnel's read-only-probe stage).

READ-ONLY MEASUREMENT INSTRUMENT. No src/ file is touched; no build, no test-suite run, no golden,
no corpus regen, no re-baseline. This decodes the ratified factorization
(`cowork_joint_estimator_factorization.md`, user-ratified 2026-07-19) at IDENTITY WEIGHTS (every
factor weight = 1 — the mandated generative baseline) over the committed fit-layer inputs, to
measure whether the ratified STRUCTURE delivers BEFORE any C++ exists. Dispatch: Cowork 2026-07-19.

★ THE FIREWALL (grep-proven, as in every fit dispatch): no value is adjusted anywhere in response to
any measured number. The decoder IMPORTS the committed tables and note events; the GRADING import
(compare_rn / a8_rebaseline_measure / compare_analyses) is confined to the Task-3 measurement step
and cannot feed back into any value. This is an EXPLORATIONAL run (the ratified scope-of-surprise
rule): a result outside the written prediction bands is ALLOWED and is the point — it is reported,
never tuned away.

TOTAL UNIFICATION (#6): this module writes NO second Roman-numeral parser, NO second table-keying
scheme, NO second chord-template. It REUSES the fit-layer generators' own primitives:
  - normalize.normalize_label / LabelClass          (the OI-186a class)
  - gen_note_tables (member_pcs, chord_factor_pcs, note_category, spelling_bin, tonic_lof,
                     _emit_context_chain/_emit_display, _split_degree, _chord_root, constants)
  - gen_label_tables (the table cell-keying: _t1_ctx_chain, _t1_outcome_parent, _relation_cell,
                      _applied_rel_parent, _t4_ctx_chain, _collection_fifths, _fold_fifths_diff,
                      _cof_distance, _key_change_kind, read_xml_header, _PC_TO_FIFTHS, pool sigils)
  - compare_rn / compare_analyses / a8_rebaseline_measure  (GRADING ONLY — Task 3, read-only)

The ratified score form (§2, with the 2026-07-19 factor-granularity amendment) at identity weights:

  Score(S,h) =  logP_prior(k1 | signature, declared mode)              [once, initial state only]
             +  Σ_seg  logP_entry(c | key change)   at a key change (and the INITIAL segment)
             +  Σ_seg  logP_chord(c_j | c_{j-1}, mode)  at a same-key boundary
             +  Σ_seg  logP_key(k_j | k_{j-1})           at every boundary (=stay-cell if no change)
             +  Σ_tone logP_emit(category(tone; k,c) | covariates)     [per tone]
             +  Σ_tone logP_spell(spelled-degree(tone) | k)            [per tone]
             +  Σ_event logP_bass(event bass factor-role | c)          [per event  — Ni's form]
             +  Σ_role  n_events · logP_absent(role | family)  for each TEMPLATE tone absent from the
                                                               whole segment [per event of length]
             +  Σ_event logP_bound(boundary? | beat class)             [per event]
  DECLARED OMISSIONS (reported on every artifact): the CADENCE factor (feature weights deliberately
  unfit until the weight-fitting stage) and the FERMATA term (fermatas are not in the note-event
  extraction — an extraction addendum owed). No substitute for either. (The injected-table PARITY
  mode DOES score cadence, because the desk-simulation hand arithmetic used the provisional cadence
  values — see probe_desksim.py.)

Decode: exact block-factorized semi-Markov Viterbi with the full per-segment posterior retained (the
runner-up key reading + score gap per segment span). No abstention: the probe commits its best path
everywhere (the OI-33 flag must read 0 — MAP, per OI-178).
"""
from __future__ import annotations

import json
import math
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_HERE))

import normalize as norm            # noqa: E402  the OI-186a class (reused)
import gen_note_tables as gnt       # noqa: E402  note-side primitives (reused)
import gen_label_tables as glt      # noqa: E402  label-side table keying (reused)
# FIREWALL: the decoder imports ONLY the fit-layer generators above — never the grading chain
# (compare_rn / compare_analyses / a8_rebaseline_measure). The grade is downstream, in probe_run.py,
# and feeds no value back here (§ the ratified fit-firewall).

NEG_INF = float("-inf")
LOG0_FLOOR = math.log(1e-9)         # a defensive floor for a would-be zero probability (never emit 0)

# ── input artifact locations (committed) ──────────────────────────────────────
TABLES_ALL = _HERE / "tables_all.json"
NOTE_TABLES_ALL = _HERE / "note_tables_all.json"
FACTOR_PRESENCE_ALL = _HERE / "factor_presence_all.json"
NOTE_EVENTS = _HERE / "note_events" / "note_events.json"
FOLD_ARTIFACT = _HERE / "fold_assignment.json"
WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")

# ── note-event record field indices (note_events provenance: event_fields / note_fields) ──
# event = [start, end, measure, beat, metric_class_code]
EV_START, EV_END, EV_MEAS, EV_BEAT, EV_MC = 0, 1, 2, 3, 4
# note = [onset, dur, pc, midi, lof, part, measure, beat, metric_class_code, approach, departure, tied]
N_ONSET, N_DUR, N_PC, N_MIDI, N_LOF, N_PART, N_MEAS, N_BEAT, N_MC, N_AP, N_DP, N_TIED = range(12)

# canonical fewest-accidental spelling of a pc, for rendering a decode key string + the spelling
# factor's tonic line-of-fifths (matches gen_label_tables._PC_TO_FIFTHS; letter+acc only).
_PC_KEYNAME = {0: "C", 1: "Db", 2: "D", 3: "Eb", 4: "E", 5: "F",
               6: "F#", 7: "G", 8: "Ab", 9: "A", 10: "Bb", 11: "B"}

# WiR inversion figure(s) that place a given chord factor-role in the bass, per family. Used to map
# an event's actual bass note (its factor-role against the segment's chord) to the table-4 figure the
# bass/inversion factor scores. Several spellings can denote one role (e.g. '2' and '4/2' both = the
# seventh in the bass); the query sums whichever the row stored.
_ROLE_TO_FIGURES = {
    "triad":   {"root": [""], "third": ["6"], "fifth": ["6/4"]},
    "seventh": {"root": ["7"], "third": ["6/5"], "fifth": ["4/3"], "seventh": ["2", "4/2"]},
}

# ══════════════════════════════════════════════════════════════════════════════
# class-key <-> LabelClass helpers (the vocabulary is class KEY strings — §1)
# ══════════════════════════════════════════════════════════════════════════════

def class_from_key(key: str) -> norm.LabelClass:
    """Parse a stored class KEY 'deg | qual | inv | target' back to a LabelClass (#6 inverse of
    LabelClass.key()). The four fields are ' | '-joined verbatim by LabelClass.key()."""
    parts = key.split(" | ")
    while len(parts) < 4:
        parts.append("")
    return norm.LabelClass(parts[0], parts[1], parts[2], parts[3])


def mode_name(is_major: bool) -> str:
    return "major" if is_major else "minor"


# ══════════════════════════════════════════════════════════════════════════════
# Katz-table query with the ratified below-threshold (leftover) rule (§5, option 2a)
# ══════════════════════════════════════════════════════════════════════════════
# A stored Katz distribution over `counts`' pooled vocabulary holds EXACT MLE for reliable cells and
# NAMESPACED reserved-mass buckets («invfree»/«family»/BASE, «rel»…, mode:/mp:) for the sparse mass.
# To score ONE specific rare continuation, the ratified rule (cowork_sensitive_cell_probe.md
# finding 2 option 2a; factorization §5): follow the outcome's parent chain to the first stored
# bucket, then apportion the bucket's mass in proportion to that outcome class's OVERALL FREQUENCY IN
# THE MODE (the standard back-off construction) — never even division, never zero.
#   leftover_mode="freq"  -> option 2a (ratified): apportion by the mode's class marginal.
#   leftover_mode="even"  -> option 2b (the probe's second declared variant): even split.
# The denominator is the marginal mass over the vocabulary classes that back off into that bucket.


def _first_bucket(dist: dict, outcome, parent_fn) -> Optional[str]:
    """Walk parent_fn from `outcome` until a key is present in `dist`; return it (or None)."""
    cur = outcome
    seen = set()
    while cur is not None:
        ck = cur.key() if isinstance(cur, norm.LabelClass) else str(cur)
        if ck in dist:
            return ck
        if ck in seen:
            return None
        seen.add(ck)
        cur = parent_fn(cur)
    return None


# ══════════════════════════════════════════════════════════════════════════════
# The adapter interface (fitted tables OR injected provisional tables share this)
# ══════════════════════════════════════════════════════════════════════════════

class Adapter:
    """Log-probability provider for every factor. The engine (segment scorer + Viterbi) calls these
    and never looks inside a table, so the fitted and the injected-provisional adapters are
    interchangeable (Task-2 establishment). `cadence_on` gates the DECLARED-OMITTED cadence factor:
    False for the fitted corpus decode (no fitted cadence table exists), True for the parity mode."""

    cadence_on = False
    name = "abstract"

    # each returns a log-probability (a nat); NEG_INF marks an impossible/unmappable candidate.
    def prior_logp(self, tonic, is_major, sig_fifths, declared_mode): raise NotImplementedError
    def entry_logp(self, cls, is_major): raise NotImplementedError
    def key_trans_logp(self, k_prev, k): raise NotImplementedError
    def chord_trans_logp(self, prev_cls, cls, is_major): raise NotImplementedError
    def emission_logp(self, category, combo): raise NotImplementedError
    def spelling_logp(self, sbin, is_major): raise NotImplementedError
    def bass_logp(self, role, family, degree_base, quality, is_major): raise NotImplementedError
    def factor_absent_logp(self, role, family): raise NotImplementedError
    def boundary_logp(self, beat_class, is_boundary): raise NotImplementedError
    def cadence_logp(self, approach_pcs, approach_bass, arrival_pcs, arrival_bass, tonic, is_major):
        return 0.0


# ══════════════════════════════════════════════════════════════════════════════
# The FITTED adapter — the committed tables_all / note_tables_all / factor_presence_all
# ══════════════════════════════════════════════════════════════════════════════

class FittedAdapter(Adapter):
    name = "fitted"
    cadence_on = False        # DECLARED OMISSION: no fitted cadence table; the corpus decode omits it

    def __init__(self, leftover_mode="freq"):
        self.leftover_mode = leftover_mode
        self.tables = json.loads(TABLES_ALL.read_text(encoding="utf-8"))
        self.ntab = json.loads(NOTE_TABLES_ALL.read_text(encoding="utf-8"))
        self.fpres = json.loads(FACTOR_PRESENCE_ALL.read_text(encoding="utf-8"))
        self.corpus_git_hash = self.tables["provenance"]["corpus_git_hash"]

        # table 1: per mode, a display-key -> row map + a level-key -> dist back-off map.
        self.t1 = {}
        self.t1_levels = {}
        for mode in ("major", "minor"):
            rows = self.tables["table1_chord_transition"][mode]
            self.t1[mode] = rows
            lvl = {}
            for _dk, row in rows.items():
                lvl.setdefault(row["context_used"], row["dist"])
            self.t1_levels[mode] = lvl
        self.t2 = self.tables["table2_key_transition"]
        self.t3 = self.tables["table3_entry_chord"]
        # table 4: display-key -> row + level-key -> dist back-off map.
        self.t4 = self.tables["table4_bass_inversion"]
        self.t4_levels = {}
        for _dk, row in self.t4.items():
            self.t4_levels.setdefault(row["context_used"], row["dist"])
        self.t5 = self.tables["table5_signature_prior"]

        # note tables
        self.emis = self.ntab["emission_category_by_covariate"]
        self.emis_levels = {}
        for _dk, row in self.emis.items():
            self.emis_levels.setdefault(row["context_used"], row["dist"])
        self.spell = self.ntab["spelling_position_by_mode"]
        self.boundary = self.ntab["event_boundary_by_beat_class"]

        # factor-presence (PRIMARY mode 'overlap'): P(absent | role,family) — the missing-tone basis.
        self.fp = self.fpres["factor_presence_table"][self.fpres["primary_mode"]]

        # the per-mode class marginal (option 2a apportionment) — a table quantity, counted once over
        # the SAME GT substrate the tables used (glt.extract_stem). Firewall-clean: independent of any
        # decode/grade measurement, like every other counted table.
        self._mode_marginal = None
        self._apportion_cache = {}       # (id(dist), bucket, mode) -> (denom_mass, member_count)
        # factor memoization (pure functions of class/key args — the decode calls each many times)
        self._ct_cache, self._entry_cache, self._kt_cache = {}, {}, {}

    # ---- the mode class marginal (lazy; used only by the leftover rule) ----
    def mode_marginal(self, mode):
        if self._mode_marginal is None:
            self._mode_marginal = self._count_mode_marginal()
        return self._mode_marginal[mode]

    def _count_mode_marginal(self):
        fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
        covered = sorted(fa["stem_index"].keys())
        marg = {"major": Counter(), "minor": Counter()}
        for stem in covered:
            d = glt.extract_stem(stem)
            for r in d["seq"]:
                if r["is_major"] is None or r["cls"].raw_unnormalized:
                    continue
                marg["major" if r["is_major"] else "minor"][r["cls"].key()] += 1
        return {m: dict(c) for m, c in marg.items()}

    # ---- the ratified leftover apportionment over a stored Katz dist ----
    def _katz_query(self, dist, outcome_cls, parent_fn, mode, is_class=True):
        """P(outcome_cls | ...) from a stored Katz dist with the ratified below-threshold rule (§5).
        is_class=True: the outcome space is chord CLASSES (table1 normal rows, table3) — option 2a
        apportions the first-bucket mass by the outcome's class marginal in the mode. is_class=False:
        a non-class categorical outcome space (the applied-relation resolve/elsewhere cells) — the
        first-bucket mass is the reserved mass for that terminal semantic cell and is returned
        directly (the standard assign-reserved-mass back-off)."""
        ck = outcome_cls.key() if isinstance(outcome_cls, norm.LabelClass) else str(outcome_cls)
        if ck in dist:
            return dist[ck]
        bucket = _first_bucket(dist, outcome_cls, parent_fn)
        if bucket is None:
            return None
        mass = dist[bucket]
        if mass <= 0.0:
            return None
        if not is_class:
            return mass
        denom, count = self._apportion(dist, bucket, parent_fn, mode)
        if self.leftover_mode == "even":
            return mass / max(1, count)
        marg = self.mode_marginal(mode)          # option 2a (ratified): class-marginal apportionment
        return mass * (marg.get(ck, 0) + glt.ALPHA) / denom if denom > 0 else mass

    def _apportion(self, dist, bucket, parent_fn, mode):
        """(marginal-mass, member-count) of the vocabulary classes that back off into `bucket`,
        cached per (dist, bucket, mode) — the class-marginal iteration is otherwise O(vocab) per
        leftover query and would dominate the decode."""
        key = (id(dist), bucket, mode)
        v = self._apportion_cache.get(key)
        if v is None:
            marg = self.mode_marginal(mode)
            tot, cnt = 0.0, 0
            for c in marg:
                if _first_bucket(dist, class_from_key(c), parent_fn) == bucket:
                    tot += marg[c] + glt.ALPHA
                    cnt += 1
            v = (tot if tot > 0 else glt.ALPHA, cnt)
            self._apportion_cache[key] = v
        return v

    # ---- factor 10: signature/declared-mode prior (INITIAL STATE ONLY) ----
    def prior_logp(self, tonic, is_major, sig_fifths, declared_mode):
        dmode = declared_mode if declared_mode in ("major", "minor") else "none"
        dist = self.t5.get(dmode, self.t5.get("none", {"BASE": 1.0}))
        if sig_fifths is None:
            return _safe_log(dist.get("BASE", 1.0 / 24.0))
        coll = glt._collection_fifths(tonic, is_major)
        diff = glt._fold_fifths_diff(coll - sig_fifths)
        band = str(diff) if abs(diff) <= 1 else "far"
        lm = "M" if is_major else "m"
        cell = f"{band}|{lm}"
        if cell in dist:
            return _safe_log(dist[cell])
        # back-off: mode marginal cell, then BASE apportioned over the residual (unlisted) keys.
        mcell = f"mode:{lm}"
        if mcell in dist:
            return _safe_log(dist[mcell])
        base = dist.get("BASE", 0.0)
        residual_keys = max(1, 24 - sum(1 for k in dist if "|" in k and not k.startswith(("mode:", "mp:"))))
        return _safe_log(base / residual_keys if base > 0 else 1e-6)

    # ---- factor 6: entry chord (initial segment + at a key change) ----
    def entry_logp(self, cls, is_major):
        ck = (cls.key(), is_major)
        v = self._entry_cache.get(ck)
        if v is None:
            p = self._katz_query(self.t3, cls, glt._t3_entry_parent, mode_name(is_major))
            v = _safe_log(p) if p is not None else LOG0_FLOOR
            self._entry_cache[ck] = v
        return v

    # ---- factor 5: key transition (every boundary; stay-cell if no change) ----
    def key_trans_logp(self, k_prev, k):
        kk = (k_prev, k)
        v = self._kt_cache.get(kk)
        if v is None:
            v = self._compute_key_trans(k_prev, k)
            self._kt_cache[kk] = v
        return v

    def _compute_key_trans(self, k_prev, k):
        tpa, tpm = k_prev
        tb, mb = k
        if tpa == tb and tpm == mb:
            return _safe_log(self.t2.get("stay", 1e-6))
        kind = glt._key_change_kind(tpa, tpm, tb, mb)
        if kind in ("parallel", "relative"):
            cell = kind
        else:
            dist = glt._cof_distance(tpa, tb)
            mp = f"{'M' if tpm else 'm'}{'M' if mb else 'm'}"
            band = f"cof{dist}" if dist <= 2 else "cofFar"
            cell = f"{band}|{mp}"
        if cell in self.t2:
            return _safe_log(self.t2[cell])
        mp_cell = "mp:" + cell.split("|", 1)[1] if "|" in cell else None
        if mp_cell and mp_cell in self.t2:
            return _safe_log(self.t2[mp_cell])
        return _safe_log(self.t2.get("BASE", 1e-6))

    # ---- factor 4: same-key chord transition (with the applied-relation override) ----
    def chord_trans_logp(self, prev_cls, cls, is_major):
        ck = (prev_cls.key(), cls.key(), is_major)
        v = self._ct_cache.get(ck)
        if v is None:
            v = self._compute_chord_trans(prev_cls, cls, is_major)
            self._ct_cache[ck] = v
        return v

    def _compute_chord_trans(self, prev_cls, cls, is_major):
        mode = mode_name(is_major)
        rows = self.t1[mode]
        levels = self.t1_levels[mode]
        pk = prev_cls.key()
        if pk in rows:
            row = rows[pk]
        else:
            chosen = _first_present(glt._t1_ctx_chain(prev_cls), levels)
            row = {"context_used": chosen, "dist": levels.get(chosen, {})}
        # applied-relation row (option 1a): score the outcome by its RELATION to the target.
        if str(row.get("context_used", "")).startswith(glt._REL):
            rel_cell = glt._relation_cell(prev_cls, cls)
            p = self._katz_query(row["dist"], rel_cell, glt._applied_rel_parent, mode, is_class=False)
            return _safe_log(p) if p is not None else LOG0_FLOOR
        p = self._katz_query(row["dist"], cls, glt._t1_outcome_parent, mode)
        return _safe_log(p) if p is not None else LOG0_FLOOR

    # ---- factor 1: pitch emission P(category | covariate combo) ----
    def emission_logp(self, category, combo):
        dk = gnt._emit_display(combo)
        if dk in self.emis:
            dist = self.emis[dk]["dist"]
        else:
            chosen = _first_present(gnt._emit_context_chain(combo), self.emis_levels)
            dist = self.emis_levels.get(chosen, {})
        p = dist.get(category)
        if p is None or p <= 0.0:
            # an unobserved category in this covariate row: a small additive floor (never zero).
            return _safe_log(1.0 / (sum(dist.values()) + 3.0) if dist else 1e-4)
        return _safe_log(p)

    # ---- factor 2: spelling emission P(spelled-degree bin | mode) ----
    def spelling_logp(self, sbin, is_major):
        dist = self.spell[mode_name(is_major)]["dist"]
        if sbin in dist:
            return _safe_log(dist[sbin])
        # back-off through the spelling parent chain to the first stored class/base bucket.
        cur = sbin
        seen = set()
        while cur is not None and cur not in seen:
            if cur in dist:
                return _safe_log(dist[cur])
            seen.add(cur)
            cur = gnt._spelling_parent(cur)
        return _safe_log(dist.get("BASE", 1e-4))

    # ---- factor 3: bass/inversion P(bass factor-role | chord) ----
    def bass_logp(self, role, family, degree_base, quality, is_major):
        if role is None:
            return _safe_log(0.02)          # a non-chord-factor bass — a floor (rare; declared)
        mode = "M" if is_major else "m"
        dk = f"{degree_base}|{quality}|{mode}"
        if dk in self.t4:
            dist = self.t4[dk]["dist"]
        else:
            chosen = _first_present(glt._t4_ctx_chain((degree_base, quality, mode)), self.t4_levels)
            dist = self.t4_levels.get(chosen, {})
        figs = _ROLE_TO_FIGURES.get(family, {}).get(role, [])
        p = sum(dist.get(f, 0.0) for f in figs)
        if p <= 0.0:
            return _safe_log(0.01)          # this inversion never occurred for this chord — a floor
        return _safe_log(p)

    # ---- the missing-template-tone penalty basis (per role, per family) ----
    def factor_absent_logp(self, role, family):
        cell = f"{role}|{family}"
        rec = self.fp.get(cell)
        if rec is None:
            return _safe_log(0.05)
        return _safe_log(rec["p_absent_smoothed"])

    # ---- factor 7: boundary P(boundary? | beat class) ----
    def boundary_logp(self, beat_class, is_boundary):
        rec = self.boundary.get(beat_class)
        if rec is None:
            return 0.0
        p = rec["prob"]
        p = min(max(p, 1e-6), 1 - 1e-6)
        return math.log(p if is_boundary else (1.0 - p))


def _safe_log(p):
    return math.log(p) if p and p > 0 else LOG0_FLOOR


def _first_present(chain, level_map):
    for k in chain:
        if k in level_map:
            return k
    return chain[-1]


# ══════════════════════════════════════════════════════════════════════════════
# The shared factor engine — categorize notes/events for (k, c); reuse gnt primitives
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class Piece:
    stem: str
    events: list          # [start,end,measure,beat,mc]
    notes: list           # the 12-field note records
    n_quarter: int
    meter: tuple
    notes_by_event: list = field(default_factory=list)   # per event: list of note records (onset in ev)
    ev_bass: list = field(default_factory=list)           # per event: bass pc (lowest midi) or None
    ev_onset_pcs: list = field(default_factory=list)       # per event: set of onset pcs
    _live_notes: list = field(default_factory=list)        # (onset, offset, pc) for non-anacrusis notes

    def prepare(self):
        # assign each (non-anacrusis) note to the event whose [start,end) contains its ONSET (the
        # gen_note_tables onset-in-segment convention). Events partition by onset/offset, so each
        # onset lands in exactly one event; anacrusis (measure 0) notes are excluded (OI-184(a)).
        self.notes_by_event = [[] for _ in self.events]
        starts = [e[EV_START] for e in self.events]
        import bisect
        for n in self.notes:
            if n[N_MEAS] == 0:
                continue
            i = bisect.bisect_right(starts, n[N_ONSET]) - 1
            if 0 <= i < len(self.events) and self.events[i][EV_START] <= n[N_ONSET] < self.events[i][EV_END]:
                self.notes_by_event[i].append(n)
        self.ev_bass = [event_bass_pc(ns) for ns in self.notes_by_event]
        self.ev_onset_pcs = [frozenset(n[N_PC] for n in ns) for ns in self.notes_by_event]
        self._live_notes = sorted(((n[N_ONSET], n[N_ONSET] + n[N_DUR], n[N_PC])
                                   for n in self.notes if n[N_MEAS] != 0), key=lambda t: t[0])

    def overlap_pcs(self, i, j):
        """Pitch classes sounding anywhere in [start_i, end_{j-1}) (overlap membership — gnt)."""
        start = self.events[i][EV_START]
        end = self.events[j - 1][EV_END]
        pcs = set()
        for onset, offset, pc in self._live_notes:
            if onset >= end:
                break
            if offset > start:
                pcs.add(pc)
        return pcs


_MC_NAME = gnt._MC_INV       # {0:downbeat,...}
_MV_NAME = gnt._MV_INV       # {0:none,1:step,2:leap}


class ChordCache:
    """Per-(tonic,is_major,class-key) cache of member_pcs / chord_factor_pcs / root_pc (reuse gnt)."""
    def __init__(self):
        self._m = {}

    def get(self, cls, tonic, is_major):
        key = (tonic, is_major, cls.key())
        v = self._m.get(key)
        if v is None:
            mem = gnt.member_pcs(cls, tonic, is_major)
            fac = gnt.chord_factor_pcs(cls, tonic, is_major)
            root = fac[0][1] if fac else None
            v = (mem, fac, root)
            self._m[key] = v
        return v


def event_bass_pc(notes):
    """Lowest sounding midi -> its pc, over an event's notes; None if the event has no notes."""
    if not notes:
        return None
    lo = min(notes, key=lambda n: n[N_MIDI])
    return lo[N_PC]


def segment_notes(piece: Piece, i, j):
    out = []
    for e in range(i, j):
        out.extend(piece.notes_by_event[e])
    return out


def segment_overlap_pcs(piece: Piece, i, j):
    """Pitch classes sounding anywhere in [start_i, end_{j-1}) (overlap membership — gnt)."""
    return piece.overlap_pcs(i, j)


def score_segment_content(piece: Piece, i, j, tonic, is_major, cls, adapter: Adapter,
                          cache: ChordCache, seg_pcs=None):
    """The WITHIN-segment factor sum for a candidate (segment [i,j), key (tonic,is_major), chord cls):
    emission (per tone) + spelling (per tone) + bass (per event) + missing-tone (per event of length)
    + boundary (per event). Returns NEG_INF for an unmappable class in this key. `seg_pcs` (overlap
    pcs of the span) may be passed precomputed."""
    mem, fac, _root = cache.get(cls, tonic, is_major)
    if mem is None:
        return NEG_INF
    n_events = j - i
    total = 0.0
    key_lof = glt._PC_TO_FIFTHS[tonic % 12]      # tonic line-of-fifths for the spelling factor

    # emission + spelling, per tone (onset-in-segment)
    for e in range(i, j):
        for n in piece.notes_by_event[e]:
            cat = gnt.note_category(n[N_PC], mem, tonic, is_major)
            combo = (_MC_NAME[n[N_MC]], _MV_NAME[n[N_AP]], _MV_NAME[n[N_DP]], bool(n[N_TIED]))
            total += adapter.emission_logp(cat, combo)
            total += adapter.spelling_logp(gnt.spelling_bin(n[N_LOF] - key_lof, is_major), is_major)

    # bass, per event (Ni's per-frame form)
    family = "seventh" if (fac and len(fac) == 4) else "triad"
    fac_pc = {pc: role for role, pc in (fac or [])}
    for e in range(i, j):
        bpc = piece.ev_bass[e]
        if bpc is None:
            continue
        total += adapter.bass_logp(fac_pc.get(bpc), family, cls.degree_base, cls.quality, is_major)

    # missing-template-tone penalty, per event of segment length (fully-absent factor only)
    if fac:
        if seg_pcs is None:
            seg_pcs = piece.overlap_pcs(i, j)
        for role, pc in fac:
            if pc not in seg_pcs:
                total += n_events * adapter.factor_absent_logp(role, family)

    # boundary, per event: the first event is a boundary; interior events are non-boundaries
    for idx, e in enumerate(range(i, j)):
        total += adapter.boundary_logp(_MC_NAME[piece.events[e][EV_MC]], idx == 0)

    return total


def score_segment_content_breakdown(piece: Piece, i, j, tonic, is_major, cls, adapter: Adapter,
                                    cache: ChordCache):
    """The per-FACTOR breakdown of the within-segment sum (the establishment / parity view — the
    SAME factor calls score_segment_content makes, itemized). Returns a dict of nats per factor."""
    mem, fac, _root = cache.get(cls, tonic, is_major)
    if mem is None:
        return None
    n_events = j - i
    key_lof = glt._PC_TO_FIFTHS[tonic % 12]
    b = {"emission": 0.0, "spelling": 0.0, "bass": 0.0, "missing_tone": 0.0, "boundary": 0.0}
    for e in range(i, j):
        for n in piece.notes_by_event[e]:
            cat = gnt.note_category(n[N_PC], mem, tonic, is_major)
            combo = (_MC_NAME[n[N_MC]], _MV_NAME[n[N_AP]], _MV_NAME[n[N_DP]], bool(n[N_TIED]))
            b["emission"] += adapter.emission_logp(cat, combo)
            b["spelling"] += adapter.spelling_logp(gnt.spelling_bin(n[N_LOF] - key_lof, is_major), is_major)
    family = "seventh" if (fac and len(fac) == 4) else "triad"
    fac_pc = {pc: role for role, pc in (fac or [])}
    for e in range(i, j):
        bpc = event_bass_pc(piece.notes_by_event[e])
        if bpc is None:
            continue
        b["bass"] += adapter.bass_logp(fac_pc.get(bpc), family, cls.degree_base, cls.quality, is_major)
    if fac:
        seg_pcs = segment_overlap_pcs(piece, i, j)
        for role, pc in fac:
            if pc not in seg_pcs:
                b["missing_tone"] += n_events * adapter.factor_absent_logp(role, family)
    for idx, e in enumerate(range(i, j)):
        bc = _MC_NAME[piece.events[e][EV_MC]]
        b["boundary"] += adapter.boundary_logp(bc, idx == 0)
    return b


def score_hypothesis(piece: Piece, hyp, adapter: Adapter, cache: ChordCache,
                     sig_fifths, declared_mode):
    """Score an EXPLICIT hypothesis = ordered list of segments, each a dict
    {'i','j','tonic','is_major','cls': LabelClass}. Returns a per-segment per-factor breakdown, using
    the SAME factor calls the Viterbi uses (so a parity pass on hand cases establishes the engine).
    prior at the initial segment; entry at the initial segment AND at a key change; chord_trans at a
    same-key boundary; key_trans at EVERY boundary; cadence at every boundary (toward the arrival
    segment's key). No shared-term dropping here — the caller selects which factors to sum."""
    out = []
    for si, seg in enumerate(hyp):
        i, j = seg["i"], seg["j"]
        tonic, is_major, cls = seg["tonic"], seg["is_major"], seg["cls"]
        b = score_segment_content_breakdown(piece, i, j, tonic, is_major, cls, adapter, cache)
        if b is None:
            b = {"emission": NEG_INF}
        b["prior"] = 0.0
        b["entry"] = 0.0
        b["chord_trans"] = 0.0
        b["key_trans"] = 0.0
        b["cadence"] = 0.0
        if si == 0:
            b["prior"] = adapter.prior_logp(tonic, is_major, sig_fifths, declared_mode)
            b["entry"] = adapter.entry_logp(cls, is_major)
        else:
            prev = hyp[si - 1]
            b["key_trans"] = adapter.key_trans_logp((prev["tonic"], prev["is_major"]), (tonic, is_major))
            same = (prev["tonic"] == tonic and prev["is_major"] == is_major)
            if same:
                b["chord_trans"] = adapter.chord_trans_logp(prev["cls"], cls, is_major)
            else:
                b["entry"] = adapter.entry_logp(cls, is_major)
            b["cadence"] = cadence_at(piece, i, tonic, is_major, adapter)
        out.append(b)
    return out


def cadence_at(piece: Piece, i, tonic, is_major, adapter: Adapter):
    """The DECLARED-OMITTED cadence factor at the boundary that STARTS a segment at event i (toward
    that segment's key). Zero for the fitted adapter (omitted). The approach is event i-1 (the last
    event of the previous segment); the arrival is event i. Position-and-key dependent only."""
    if not adapter.cadence_on or i <= 0:
        return 0.0
    ap_notes = piece.notes_by_event[i - 1]
    ar_notes = piece.notes_by_event[i]
    ap_pcs = {n[N_PC] for n in ap_notes}
    ar_pcs = {n[N_PC] for n in ar_notes}
    ap_bass = event_bass_pc(ap_notes)
    ar_bass = event_bass_pc(ar_notes)
    return adapter.cadence_logp(ap_pcs, ap_bass, ar_pcs, ar_bass, tonic, is_major)


# ══════════════════════════════════════════════════════════════════════════════
# Candidate generation (the vocabulary + the declared root-present prune)
# ══════════════════════════════════════════════════════════════════════════════

class Vocabulary:
    """The chord-class vocabulary observed in the fitted tables (§1), collapsed to INVERSION-FREE
    classes (degree, quality, target). The chord STATE carries no inversion field: the inversion is a
    derived published fact read off the segment's actual bass (chord_factor_pcs), and no factor score
    except a largely-pooled table-1 cell depends on it — a DECLARED simplification that keeps the
    state space tractable (collapses I|Maj||, I|Maj|6|, I|Maj|64| to one state; the transition uses
    the inversion-free class, which the table-1 «invfree» back-off already models). Pooled buckets
    («…», BASE) are not chord states."""
    def __init__(self, tables):
        keys = set()
        for mode in ("major", "minor"):
            for fromk, row in tables["table1_chord_transition"][mode].items():
                keys.add(fromk)
                for o in row["dist"]:
                    if not (o.startswith("«") or o == "BASE"):
                        keys.add(o)
        for k in tables["table3_entry_chord"]:
            if k != "BASE" and not k.startswith("«"):
                keys.add(k)
        self.classes = {}
        for k in sorted(keys):
            lc = class_from_key(k).inversion_free()      # collapse inversion
            if lc.raw_unnormalized or lc.quality in ("triad", "seventh"):
                continue                                  # pooled-quality placeholders are not states
            self.classes[lc.key()] = lc
        self.keylist = sorted(self.classes)


# ══════════════════════════════════════════════════════════════════════════════
# The exact block-factorized semi-Markov Viterbi
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class Segment:
    i: int
    j: int
    tonic: int
    is_major: bool
    cls_key: str
    start_tick: int
    end_tick: int


@dataclass
class DecodeResult:
    stem: str
    segments: list           # list of dict (span, key, chord, score contributions summary)
    total_score: float
    n_events: int
    decode_seconds: float
    posterior: list          # per segment: {best, best_score, runner_key, runner_score, gap}
    notes: str = ""


# candidate-state generation (two DECLARED prunes, each loss-measurable by widening it):
#  (1) ROOT-PRESENT: only (key,class) whose chord ROOT is a sounding pc of the segment. Justified by
#      the fitted factor-presence table (root|triad=0.96 / root|seventh=0.92): a rootless-root reading
#      is already disfavored by the missing-tone penalty, so pruning it changes almost nothing.
#  (2) KEY-FIT: only the KEY_PRUNE_TOPK keys whose diatonic collection best covers the segment's onset
#      pcs, PLUS the notated-signature key, PLUS every key active in the neighborhood (kept by the DP).
#      A key whose collection excludes most sounding pcs pays large emission penalties and cannot win.
#  This is the ratified §5 "documented pruning" reserve, applied because exact 24-key decode is
#  intractable in pure Python at chorale scale; its loss is measured by re-running a sample at higher K.
KEYS_24 = [(t, m) for t in range(12) for m in (True, False)]
KEY_PRUNE_TOPK = 6


def _key_collection(tonic, is_major):
    coll = gnt._MAJ_COLLECTION if is_major else gnt._MIN_COLLECTION
    return frozenset((tonic + s) % 12 for s in coll)


_KEY_COLL = {(t, m): _key_collection(t, m) for t in range(12) for m in (True, False)}


def _candidate_keys_for_segment(onset_pcs, key_set, sig_key):
    """The KEY-FIT prune: keys ranked by |onset_pcs ∩ collection|, keep the top-K, always include the
    signature key. Ties broken deterministically by (−fit, tonic, mode)."""
    scored = sorted(key_set, key=lambda k: (-len(onset_pcs & _KEY_COLL[k]), k[0], not k[1]))
    keep = scored[:KEY_PRUNE_TOPK]
    if sig_key is not None and sig_key in _KEY_COLL and sig_key not in keep:
        keep.append(sig_key)
    return keep


def _candidate_states_for_segment(piece, i, j, vocab: Vocabulary, cache: ChordCache, key_set,
                                  sig_key=None):
    onset_pcs = set()
    for e in range(i, j):
        onset_pcs |= piece.ev_onset_pcs[e]
    seg_pcs = piece.overlap_pcs(i, j)
    keys = _candidate_keys_for_segment(onset_pcs, key_set, sig_key)
    n_onset = len(onset_pcs)
    max_ncts = max(1, j - i)          # allow ~1 non-chord tone per event of segment length
    cand = []
    for (tonic, is_major) in keys:
        for ckey, lc in vocab.classes.items():
            mem, _fac, root = cache.get(lc, tonic, is_major)
            if root is None or root not in onset_pcs:
                continue                                   # (1) ROOT-PRESENT prune
            if mem is None:
                continue
            present = len(mem & onset_pcs)
            if present < min(2, len(mem)):
                continue                                   # (2) MEMBER-OVERLAP (root + >=1 more)
            if (n_onset - present) > max_ncts:
                continue                                   # (3) FIT prune: few non-chord tones
            cand.append((tonic, is_major, ckey))
    return cand


def decode_piece(piece: Piece, adapter: Adapter, vocab: Vocabulary, cache: ChordCache,
                 seg_cap=8, key_set=None, sig_fifths=None, declared_mode="",
                 prune_keys=None):
    """Exact semi-Markov Viterbi. State = (tonic, is_major, class-key). Segment length capped at
    `seg_cap` events (the established semi-Markov default; stated in the artifact). Returns a
    DecodeResult with the best path + the per-segment runner-up key posterior."""
    t0 = time.perf_counter()
    N = len(piece.events)
    key_set = key_set or KEYS_24
    if prune_keys is not None:
        key_set = [k for k in key_set if k in prune_keys]
    sig_key = None
    if sig_fifths is not None:
        # the notated-signature MAJOR key (collection_fifths == sig_fifths, major) is always kept
        for (t, m) in key_set:
            if m and glt._collection_fifths(t, m) == sig_fifths:
                sig_key = (t, m)
                break

    # V[e] : dict state -> (best_score, back_i, back_state)   best segmentation of events[0:e] whose
    # LAST segment ends exactly at event e (exclusive). V[0] is the empty prefix (score 0, no state).
    # We store per-boundary e the best-ending states; transitions consult V[i].
    V = [dict() for _ in range(N + 1)]
    # sentinel: an "initial" pseudo-state so the first segment pays prior + entry.
    START = ("START",)
    V[0][START] = (0.0, None, None)

    # precompute candidate states per (i,j) lazily
    cand_cache = {}

    def candidates(i, j):
        key = (i, j)
        c = cand_cache.get(key)
        if c is None:
            c = _candidate_states_for_segment(piece, i, j, vocab, cache, key_set, sig_key)
            cand_cache[key] = c
        return c

    # segment content score cache (i,j,state) -> content logp; overlap-pcs cached per (i,j)
    content_cache = {}
    overlap_cache = {}

    def content(i, j, tonic, is_major, ckey):
        k = (i, j, tonic, is_major, ckey)
        v = content_cache.get(k)
        if v is None:
            sp = overlap_cache.get((i, j))
            if sp is None:
                sp = piece.overlap_pcs(i, j)
                overlap_cache[(i, j)] = sp
            v = score_segment_content(piece, i, j, tonic, is_major, vocab.classes[ckey],
                                      adapter, cache, seg_pcs=sp)
            content_cache[k] = v
        return v

    # per-boundary summaries of V[i] (computed once, reused across the seg_cap window)
    summ = [None] * (N + 1)

    def summarize(i):
        s = summ[i]
        if s is not None:
            return s
        key_best, key_arg = {}, {}
        per_class = defaultdict(dict)
        start_score = None
        for st, (sc, _bi, _bs) in V[i].items():
            if st == START:
                start_score = sc
                continue
            (tt, tm, ck) = st
            per_class[(tt, tm)][ck] = sc
            if (tt, tm) not in key_best or sc > key_best[(tt, tm)]:
                key_best[(tt, tm)] = sc
                key_arg[(tt, tm)] = ck
        s = (start_score, key_best, key_arg, per_class)
        summ[i] = s
        return s

    for j in range(1, N + 1):
        best_here = {}
        for i in range(max(0, j - seg_cap), j):
            if not V[i]:
                continue
            start_score, key_best, key_arg, per_class = summarize(i)
            cand_states = candidates(i, j)
            # target keys present among the candidates
            tgt_keys = {(t, m) for (t, m, _c) in cand_states}
            # (c) precompute the best key-CHANGE into each target key (independent of the target class)
            kchg = {}
            for (tt, tm) in tgt_keys:
                best_k, arg_k = NEG_INF, None
                for (pt, pm), kb in key_best.items():
                    if pt == tt and pm == tm:
                        continue
                    val = kb + adapter.key_trans_logp((pt, pm), (tt, tm))
                    if val > best_k:
                        best_k, arg_k = val, (pt, pm)
                kchg[(tt, tm)] = (best_k, arg_k)
            for (tonic, is_major, ckey) in cand_states:
                cscore = content(i, j, tonic, is_major, ckey)
                if cscore == NEG_INF:
                    continue
                cls = vocab.classes[ckey]
                cad = cadence_at(piece, i, tonic, is_major, adapter)
                entry_lp = adapter.entry_logp(cls, is_major)
                best_in = NEG_INF
                back = None
                # (a) initial segment
                if start_score is not None:
                    tin = start_score + adapter.prior_logp(tonic, is_major, sig_fifths, declared_mode) + entry_lp
                    if tin > best_in:
                        best_in, back = tin, (i, START)
                # (b) same-key chord transition (+ the stay key-cell)
                same = per_class.get((tonic, is_major))
                if same:
                    stay = adapter.key_trans_logp((tonic, is_major), (tonic, is_major))
                    for pck, psc in same.items():
                        tin = psc + adapter.chord_trans_logp(vocab.classes[pck], cls, is_major) + stay
                        if tin > best_in:
                            best_in, back = tin, (i, (tonic, is_major, pck))
                # (c) key-change transition (precomputed best prev key) + entry
                bk, ak = kchg.get((tonic, is_major), (NEG_INF, None))
                if ak is not None:
                    tin = bk + entry_lp
                    if tin > best_in:
                        best_in, back = tin, (i, (ak[0], ak[1], key_arg[ak]))
                if best_in == NEG_INF:
                    continue
                score = best_in + cscore + cad
                st = (tonic, is_major, ckey)
                cur = best_here.get(st)
                if cur is None or score > cur[0]:
                    best_here[st] = (score, back[0], back[1])
        V[j] = best_here

    # terminate: best full-coverage state at V[N]
    if not V[N]:
        return DecodeResult(piece.stem, [], NEG_INF, N, time.perf_counter() - t0, [],
                            notes="no complete path")
    end_state, (end_score, _bi, _bs) = max(V[N].items(), key=lambda kv: kv[1][0])
    # backtrack
    segs = []
    st, j = end_state, N
    while st is not None and st != START:
        sc, bi, bs = V[j][st]
        (tonic, is_major, ckey) = st
        segs.append(Segment(bi, j, tonic, is_major, ckey,
                            piece.events[bi][EV_START], piece.events[j - 1][EV_END]))
        st, j = bs, bi
    segs.reverse()

    posterior = _segment_posterior(piece, segs, adapter, vocab, cache, sig_fifths, declared_mode, key_set)
    dt = time.perf_counter() - t0
    seg_dicts = [_seg_summary(piece, s, vocab, cache) for s in segs]
    return DecodeResult(piece.stem, seg_dicts, end_score, N, dt, posterior)


def _seg_summary(piece, s: Segment, vocab, cache):
    cls = vocab.classes[s.cls_key]
    _mem, fac, root = cache.get(cls, s.tonic, s.is_major)
    return {
        "i": s.i, "j": s.j, "start_tick": s.start_tick, "end_tick": s.end_tick,
        "tonic_pc": s.tonic, "is_major": s.is_major,
        "key": _key_string(s.tonic, s.is_major),
        "class_key": s.cls_key, "root_pc": root,
        "degree": cls.degree_base, "quality": cls.quality,
        "inversion": cls.inversion, "target": cls.target,
    }


def _segment_posterior(piece, segs, adapter, vocab, cache, sig_fifths, declared_mode, key_set):
    """For each committed segment SPAN, the runner-up KEY reading and its score gap (§5): hold the
    span + its committed chord class fixed and re-score the segment's content under each candidate
    key, reporting the best alternate key and the content-score gap. A cheap, honest local posterior
    (the full lattice marginal is retained implicitly by the exact DP; this is the published slice)."""
    out = []
    for s in segs:
        cls = vocab.classes[s.cls_key]
        scores = {}
        for (tonic, is_major) in key_set:
            _mem, _fac, root = cache.get(cls, tonic, is_major)
            if root is None:
                continue
            sc = score_segment_content(piece, s.i, s.j, tonic, is_major, cls, adapter, cache)
            if sc != NEG_INF:
                scores[(tonic, is_major)] = sc
        best = (s.tonic, s.is_major)
        best_sc = scores.get(best, NEG_INF)
        alt = None
        alt_sc = NEG_INF
        for k, sc in scores.items():
            if k == best:
                continue
            if sc > alt_sc:
                alt, alt_sc = k, sc
        out.append({
            "span": [s.start_tick, s.end_tick],
            "committed_key": _key_string(s.tonic, s.is_major),
            "committed_key_content_score": round(best_sc, 4) if best_sc != NEG_INF else None,
            "runner_key": _key_string(*alt) if alt else None,
            "runner_key_content_score": round(alt_sc, 4) if alt_sc != NEG_INF else None,
            "gap": round(best_sc - alt_sc, 4) if (alt and best_sc != NEG_INF) else None,
        })
    return out


def _key_string(tonic, is_major):
    return _PC_KEYNAME[tonic % 12] + ("maj" if is_major else "min")


# ══════════════════════════════════════════════════════════════════════════════
# Loading pieces
# ══════════════════════════════════════════════════════════════════════════════

def sub_piece(piece: Piece, event_indices, bass_override=None):
    """A Piece containing only the given events (re-indexed 0..n-1), for a focused factor check on a
    real span. `bass_override` (a pc) forces that pc to be the event minimum (lowest midi) wherever it
    sounds — used to trace a reading under a specified bass (the OI-185 bwv352 bass question). Notes
    keep their real covariates/lof; ticks are preserved so overlap membership is unchanged."""
    events = [list(piece.events[i]) for i in event_indices]
    notes = []
    for i in event_indices:
        for n in piece.notes_by_event[i]:
            m = list(n)
            if bass_override is not None:
                m[N_MIDI] = (m[N_PC] + 24) if m[N_PC] == bass_override else (m[N_PC] + 72)
            notes.append(m)
    sp = Piece(stem=piece.stem, events=events, notes=notes,
               n_quarter=piece.n_quarter, meter=piece.meter)
    sp.prepare()          # populate notes_by_event, ev_bass, ev_onset_pcs, _live_notes (absolute ticks)
    return sp


def load_pieces():
    d = json.loads(NOTE_EVENTS.read_text(encoding="utf-8"))
    prov = d["provenance"]
    pieces = {}
    for stem, p in d["pieces"].items():
        pc = Piece(stem=stem, events=p["events"], notes=p["notes"],
                   n_quarter=p["n_quarter"], meter=tuple(p["meter"]) if p["meter"] else None)
        pc.prepare()
        pieces[stem] = pc
    return pieces, prov


def piece_header(stem):
    """Signature fifths + declared mode for a stem (reuse gen_label_tables.read_xml_header)."""
    xml = glt.read_xml_header(stem)
    if xml is None:
        return None, ""
    return xml["init_fifths"], (xml["declared_mode"] or "")


if __name__ == "__main__":
    import probe_run
    probe_run.main(sys.argv[1:])
