#!/usr/bin/env python3
"""
cc_layer3_keymode_baseline.py  —  READ-ONLY Layer-3 (key/mode) baseline + the
Increment-B held-out direct key/mode ground-truth harness.

The DIRECT key/mode-vs-ground-truth metric for the L3 audit (cowork_layer3_keymode
_design.md §6). NOTHING here touches production or rebuilds any corpus: it reads the
already-committed per-region key strings from tools/corpus/<preset>/*.ours.json and
the When-in-Rome (DCML-lineage) Bach rntxt local-key ground truth, aligns them with
the SAME validated time-overlap aligner compare_rn uses, and reports a DIRECT
(tonic,mode)==GT comparison — independent of chord root (unlike the indirect
`key_disagree` RN proxy).

Why WiR and not the on-disk *.music21.json: the committed music21.json carries only
a per-piece GLOBAL key (key==keyGlobal for all 29047 regions / 353 stems — re-verified
2026-06-22, this session), so it cannot ground a LOCAL key/mode metric. WiR rntxt
carries a true LOCAL key per measure/beat (coverage ~326/353; the uncovered stems are
reported, never folded into /353).

────────────────────────────────────────────────────────────────────────────────────
INCREMENT B (this session, 2026-06-22) — the held-out ground-truth harness
────────────────────────────────────────────────────────────────────────────────────
The audit baseline (the legacy code below) used a single-source proxy for the
unambiguous/ambiguous split (WiR local==global) and the OLD `compare_rn._our_key_tonic`
extractor (which rejects ~39% of Jazz key strings — all modal CamelCase labels). This
increment, per `cowork_layer3_keymode_impl_design.md` §2, adds:

  1. A FIXED key extractor (`our_key_tonic_fixed`) — the legacy regex's mode group is
     `[a-z]+`, so it silently rejects every CamelCase modal label our analyzer emits
     (`DDor`, `GMixolyd`, `Mix♭6`, `PhrygDom`, `Lyd♭7`, …).  Those are the Jazz 39%
     parse-fail.  The fix accepts the mode token regardless of case / accidental-suffix
     and colours it major/minor by the tonic-triad third.  READ-ONLY: it is a local
     extractor in THIS harness; `compare_rn.py` is untouched (the BIR pipeline that
     depends on it stays byte-identical).

  2. A GENUINE two-source unambiguous split (replaces the local==global proxy where the
     data allows).  Source 1 = our hand-rolled `dcml_parser.parse_rntxt_file` local key.
     Source 2 = `music21`'s independent romanText parser of the SAME WiR analysis.txt
     (per-RN `RomanNumeral.key`, aligned by exact (measure, beat)).  unambiguous =
     the two parsers CONCUR on the local key/mode AND WiR local==global (no modulation).
     ★ LIMITATION (stated, not hidden): both sources parse the ONE WiR human annotation,
     so this is a two-IMPLEMENTATION concurrence (catches encoding / applied-chord /
     modulation-boundary ambiguity), NOT a two-ANNOTATOR concurrence.  The design's
     "DCML ∧ music21 agree" intended two independent ANALYSES; for the Bach chorale gate
     set that is impossible read-only — music21.json is global-only and there is no Bach
     harmonies.tsv with a localkey column (the chorales are WiR-rntxt-only).  The
     local==global axis is retained precisely because it captures the modulation
     ambiguity the same-annotation parser-concurrence cannot.

  3. A fixed, documented HELD-OUT train/test split by stem (deterministic md5(stem)%100
     < TEST_PCT).  No canonical WiR/DCML chorale split is published, so we define one.
     All HEADLINE numbers are the TEST split (out-of-sample, the §6.3 done-criterion).

  4. The metric (design §4/§6): on UNAMBIGUOUS regions, full (tonic+mode) match (target
     ~100%); on AMBIGUOUS regions, top-1 / in-top-2 / neither (the resolver emits a
     top-2 via `keyModeRunnerUp`; the flagged-residual machinery is Increment C, so the
     ambiguous bar is reported as the measurable top-1/in-top-k breakdown pre-C).

Run:  python tools/cc_layer3_keymode_baseline.py            # Increment-B report (default)
      python tools/cc_layer3_keymode_baseline.py --legacy-audit   # the old audit baseline
      python tools/cc_layer3_keymode_baseline.py --json out.json  # machine-readable dump
"""
import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import compare_rn as C            # _our_key_tonic, _dcml_key_tonic, WIR_BASE_DEFAULT
import compare_analyses as cmp    # load_analysis, align_dcml_regions, DEFAULT_DCML_MATCH_MODE
import dcml_parser as dcml        # find_wir_file, parse_rntxt_file

# Force UTF-8 stdout so the music-flat sigil '♭' in modal key labels prints on Windows.
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass


def _key_pair(region_attr_getter):
    """Helper unused placeholder kept for clarity; inlined below."""
    raise NotImplementedError


class Tally:
    def __init__(self):
        self.pieces = 0
        self.covered = 0
        self.total = 0
        # region-count tallies
        self.aligned = 0          # ours region had an aligned WiR region
        self.scorable = 0         # both keys parsed
        self.our_keyfail = 0
        self.gt_keyfail = 0
        # direct comparison (against WiR LOCAL key)
        self.match_full = 0       # (tonic,mode) == local
        self.match_tonic = 0      # tonic == local tonic (mode may differ)
        self.match_mode = 0       # mode == local mode (tonic may differ)
        # stable vs modulation split (local==global vs local!=global)
        self.stable = 0
        self.stable_full = 0
        self.modul = 0
        self.modul_match_local = 0   # matched the modulated local key (correct switch)
        self.modul_match_global = 0  # matched home/global (stayed put — the masked error)
        self.modul_neither = 0
        # duration-weighted (granularity-robust) — ticks
        self.dur_scorable = 0
        self.dur_full = 0
        self.dur_stable = 0
        self.dur_stable_full = 0
        self.dur_modul = 0
        self.dur_modul_local = 0
        self.dur_modul_global = 0
        # error patterns
        self.patterns = Counter()

    def add(self, o):
        for k, v in self.__dict__.items():
            if isinstance(v, Counter):
                v.update(o.__dict__[k])
            else:
                self.__dict__[k] += o.__dict__[k]


def score_piece(ours_regions, wir_regions) -> Tally:
    t = Tally()
    t.pieces = 1
    matches = cmp.align_dcml_regions(ours_regions, wir_regions,
                                     mode=cmp.DEFAULT_DCML_MATCH_MODE)
    for ours_r, dr in zip(ours_regions, matches):
        if dr is None:
            continue
        t.aligned += 1
        dur = max(0, int(getattr(ours_r, 'end_tick', 0)) - int(getattr(ours_r, 'start_tick', 0)))
        otc, omaj = C._our_key_tonic(getattr(ours_r, 'key', None))
        ltc, lmaj = C._dcml_key_tonic(getattr(dr, 'local_key', None))
        gtc, gmaj = C._dcml_key_tonic(getattr(dr, 'global_key', None))
        if otc is None:
            t.our_keyfail += 1
            continue
        if ltc is None:
            t.gt_keyfail += 1
            continue
        t.scorable += 1
        t.dur_scorable += dur
        our = (otc, omaj)
        loc = (ltc, lmaj)
        glob = (gtc, gmaj)
        full = (our == loc)
        if full:
            t.match_full += 1
            t.dur_full += dur
        if otc == ltc:
            t.match_tonic += 1
        if omaj == lmaj:
            t.match_mode += 1
        if not full:
            t.patterns[(_kname(our), _kname(loc))] += 1

        is_modulation = (gtc is not None and loc != glob)
        if not is_modulation:
            t.stable += 1
            t.dur_stable += dur
            if full:
                t.stable_full += 1
                t.dur_stable_full += dur
        else:
            t.modul += 1
            t.dur_modul += dur
            if our == loc:
                t.modul_match_local += 1
                t.dur_modul_local += dur
            elif our == glob:
                t.modul_match_global += 1
                t.dur_modul_global += dur
            else:
                t.modul_neither += 1
    return t


_PCNAME = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']


def _kname(tm):
    pc, maj = tm
    return f"{_PCNAME[pc % 12]}{'maj' if maj else 'min'}"


def score_corpus(ours_dir: Path, wir_base: Path) -> Tally:
    agg = Tally()
    ours_files = sorted(ours_dir.glob("*.ours.json"))
    agg.total = len(ours_files)
    uncovered = []
    for p in ours_files:
        stem = p.name.replace(".ours.json", "")
        wir_path = dcml.find_wir_file(str(wir_base), stem)
        if not wir_path:
            uncovered.append(stem)
            continue
        try:
            _, ours_regions = cmp.load_analysis(p)
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            uncovered.append(stem)
            continue
        if not ours_regions or not wir_regions:
            uncovered.append(stem)
            continue
        t = score_piece(ours_regions, wir_regions)
        t.covered = 1
        t.total = 0  # avoid double counting in add()
        agg.add(t)
    agg._uncovered = uncovered
    return agg


def _pct(n, d):
    return (100.0 * n / d) if d else 0.0


def report(label: str, t: Tally) -> str:
    L = []
    L.append(f"=== {label} — DIRECT key/mode vs WiR local-key GT ===")
    L.append(f"  corpus stems:        {t.total}")
    L.append(f"  WiR-covered stems:   {t.covered}  (uncovered: {t.total - t.covered} — never scored)")
    L.append(f"  aligned regions:     {t.aligned}")
    L.append(f"  scorable regions:    {t.scorable}  (our-keyfail {t.our_keyfail}, gt-keyfail {t.gt_keyfail})")
    L.append("")
    L.append(f"  DIRECT (tonic+mode)==local : {_pct(t.match_full, t.scorable):5.1f}%  ({t.match_full}/{t.scorable})")
    L.append(f"    tonic-only match         : {_pct(t.match_tonic, t.scorable):5.1f}%  ({t.match_tonic}/{t.scorable})")
    L.append(f"    mode-only  match         : {_pct(t.match_mode, t.scorable):5.1f}%  ({t.match_mode}/{t.scorable})")
    L.append(f"  duration-weighted full     : {_pct(t.dur_full, t.dur_scorable):5.1f}%  ({t.dur_full}/{t.dur_scorable} ticks)")
    L.append("")
    L.append("  -- UNAMBIGUOUS proxy: regions where WiR local==global (no local modulation) --")
    L.append(f"     stable regions          : {t.stable}  ({_pct(t.stable, t.scorable):.1f}% of scorable)")
    L.append(f"     full match on stable     : {_pct(t.stable_full, t.stable):5.1f}%  ({t.stable_full}/{t.stable})")
    L.append(f"     dur-weighted full stable : {_pct(t.dur_stable_full, t.dur_stable):5.1f}%")
    L.append("")
    L.append("  -- AMBIGUOUS proxy: regions where WiR local!=global (modulation/tonicization) --")
    L.append(f"     modulation regions       : {t.modul}  ({_pct(t.modul, t.scorable):.1f}% of scorable)")
    L.append(f"       matched local (switched): {_pct(t.modul_match_local, t.modul):5.1f}%  ({t.modul_match_local}/{t.modul})")
    L.append(f"       matched global (stayed) : {_pct(t.modul_match_global, t.modul):5.1f}%  ({t.modul_match_global}/{t.modul})")
    L.append(f"       matched neither         : {_pct(t.modul_neither, t.modul):5.1f}%  ({t.modul_neither}/{t.modul})")
    L.append("")
    L.append("  Top direct-mismatch patterns (ours -> WiR-local):")
    for (o, d), n in t.patterns.most_common(12):
        L.append(f"    {o:<8} -> {d:<8} {n}")
    return "\n".join(L)


def legacy_main(args):
    """The original audit baseline (single-source local==global proxy, OLD extractor,
    full corpus).  Reachable via --legacy-audit; reproduces the §3.3 audit numbers
    (Baroque 85.5% / Jazz 91.5% stable full-match) verbatim as a sanity anchor."""
    root = Path(args.corpus_root)
    wir = Path(args.wir_base)
    out = {}
    for preset in args.presets:
        d = root / preset
        if not d.is_dir():
            print(f"[skip] {d} not found")
            continue
        t = score_corpus(d, wir)
        print(report(preset, t))
        print()
        out[preset] = {k: (dict(v) if isinstance(v, Counter) else v)
                       for k, v in t.__dict__.items()
                       if not k.startswith("_") and not isinstance(v, Counter)}
    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=2))
        print(f"[wrote] {args.json}")


# ════════════════════════════════════════════════════════════════════════════
# INCREMENT B — the held-out, two-source, Jazz-fixed direct key/mode harness
# ════════════════════════════════════════════════════════════════════════════

# ── (1) The FIXED our-key extractor (the Jazz parse fix) ────────────────────
# compare_rn._our_key_tonic uses `^([A-G])([#b]?)([a-z]+)$` — the mode group is
# lowercase-only, so every CamelCase modal label our analyzer emits is rejected:
# enumerated this session, the rejects are exactly the modes
#   {Dor, Mixolyd, Lyd, harm*, mel*, Mix♭6, PhrygDom, alt, Dor#4, Loc#6, Phryg,
#    Lyd#2, Dor♭2, Lyd♭7, Lyd+, Ion+, Loc#2}  (*harm/mel are lowercase and DO parse;
# they are listed for completeness).  Jazz emits modal readings on 39% of regions →
# the 3839 our-keyfail caveat.  The fix accepts ANY mode token (case-insensitive,
# with accidental/figure suffixes) and colours it by the tonic-triad third.
_OURS_KEY_RE_FIXED = re.compile(r'^([A-G])([#b]?)(.+)$')
_NOTE_OURS = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
# Mode-name prefixes whose tonic triad has a MAJOR third (everything else = minor):
#   maj/ion(ian)/lyd(ian)/mix(olydian)/alt(ered dominant) by prefix; PhrygDom
#   (phrygian dominant) by the 'dom' substring (its prefix 'phr' is otherwise minor).
_MAJOR_MODE_STARTS = ('maj', 'ion', 'lyd', 'mix', 'alt')


def our_key_tonic_fixed(k):
    """Our key string -> (tonic_pc, is_major).  Handles the full modal palette the
    legacy extractor rejects.  (None, None) only if there is no leading note letter."""
    if not k:
        return (None, None)
    m = _OURS_KEY_RE_FIXED.match(k.strip())
    if not m:
        return (None, None)
    letter, acc, mode = m.group(1), m.group(2), m.group(3)
    pc = (_NOTE_OURS[letter] + (1 if acc == '#' else -1 if acc == 'b' else 0)) % 12
    ml = mode.lower()
    is_major = ml.startswith(_MAJOR_MODE_STARTS) or ('dom' in ml)
    return (pc, is_major)


# ── (2) The second source: music21's independent romanText local-key parse ──
_M21_CACHE: dict = {}


def m21_local_index(wir_path: str):
    """Parse a WiR analysis.txt with music21 (independent of dcml_parser) and return
    ('ok', {(measureNumber, round(beat,3)): (tonic_pc, is_major)}) or ('fail', msg).
    Cached per path (both presets reuse the same 326 files)."""
    if wir_path in _M21_CACHE:
        return _M21_CACHE[wir_path]
    try:
        from music21 import converter, roman
        score = converter.parse(wir_path, format='romanText')
        idx: dict = {}
        for rn in score.recurse().getElementsByClass(roman.RomanNumeral):
            try:
                k = rn.key
                nm = k.tonic.name              # 'A', 'B-', 'F#'
                pc = (_NOTE_OURS[nm[0]] + nm.count('#') - nm.count('-')) % 12
                idx[(rn.measureNumber, round(float(rn.beat), 3))] = (pc, k.mode == 'major')
            except Exception:
                continue
        res = ('ok', idx)
    except Exception as exc:
        res = ('fail', f"{type(exc).__name__}: {exc}")
    _M21_CACHE[wir_path] = res
    return res


# ── (3) The held-out split (deterministic, documented) ──────────────────────
TEST_PCT_DEFAULT = 20


def split_of(stem: str, test_pct: int) -> str:
    """Deterministic, reproducible train/test partition by stem.  No canonical WiR/DCML
    chorale split is published, so we define one: md5(stem) % 100 < test_pct -> 'test'.
    Stable across runs/machines (md5, not Python's salted hash)."""
    h = int(hashlib.md5(stem.encode('utf-8')).hexdigest(), 16)
    return 'test' if (h % 100) < test_pct else 'train'


_PCN = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']


def _km_name(tm):
    if tm is None or tm[0] is None:
        return None
    return f"{_PCN[tm[0] % 12]}{'maj' if tm[1] else 'min'}"


# ── (4) The Increment-B tally + scoring ─────────────────────────────────────
class BTally:
    def __init__(self):
        self.pieces = 0
        self.aligned = 0           # our region had an aligned WiR region
        self.scorable = 0          # both our (fixed) key and WiR local parsed
        self.our_keyfail = 0       # our key did not parse (FIXED extractor)
        self.our_keyfail_legacy = 0  # our key did not parse (LEGACY extractor) — the Jazz caveat
        self.gt_keyfail = 0
        self.m21_missing = 0       # scorable region with no music21 reading at (m,beat)
        # axes
        self.stable = 0            # WiR local==global
        self.concur_known = 0      # m21 present at location
        self.concur = 0            # m21 local == dcml local (two-parser agree)
        # the metric
        self.unamb = 0             # stable AND concur
        self.unamb_full = 0        # full (tonic+mode) match on unambiguous
        self.amb = 0              # complement
        self.amb_top1 = 0         # our == GT on ambiguous
        self.amb_in_top2 = 0      # GT in {our, runnerUp} (but not top1) on ambiguous
        self.amb_neither = 0
        # duration-weighted unambiguous
        self.dur_unamb = 0
        self.dur_unamb_full = 0
        # supplementary: confidence-flagged defensible on ambiguous (design §6 bonus)
        self.amb_flagged = 0       # ambiguous + neither-top2 + low conf (we flagged it)
        # mismatch patterns on unambiguous (the real defects)
        self.unamb_miss = Counter()

    def add(self, o):
        for k, v in self.__dict__.items():
            if isinstance(v, Counter):
                v.update(o.__dict__[k])
            else:
                self.__dict__[k] += o.__dict__[k]


FLAG_CONF_THRESHOLD = 0.20   # keyConfidence below this = "flagged residual" (supplementary)


def b_score_piece(ours_regions, wir_regions, m21_idx) -> BTally:
    t = BTally()
    t.pieces = 1
    matches = cmp.align_dcml_regions(ours_regions, wir_regions,
                                     mode=cmp.DEFAULT_DCML_MATCH_MODE)
    for ours_r, dr in zip(ours_regions, matches):
        if dr is None:
            continue
        t.aligned += 1
        dur = max(0, int(getattr(ours_r, 'end_tick', 0)) - int(getattr(ours_r, 'start_tick', 0)))

        otc, omaj = our_key_tonic_fixed(getattr(ours_r, 'key', None))
        leg_tc, _ = C._our_key_tonic(getattr(ours_r, 'key', None))
        ltc, lmaj = C._dcml_key_tonic(getattr(dr, 'local_key', None))
        gtc, gmaj = C._dcml_key_tonic(getattr(dr, 'global_key', None))

        if leg_tc is None:
            t.our_keyfail_legacy += 1
        if otc is None:
            t.our_keyfail += 1
            continue
        if ltc is None:
            t.gt_keyfail += 1
            continue
        t.scorable += 1

        our = (otc, omaj)
        loc = (ltc, lmaj)
        full = (our == loc)

        # runner-up (our #2 key candidate) for the in-top-2 ambiguous metric
        ru = getattr(ours_r, 'key_runner_up', None)
        ru_pair = our_key_tonic_fixed(ru.get('key')) if isinstance(ru, dict) else (None, None)
        in_top2 = (loc == our) or (loc == ru_pair)

        # axis 1: stable (no modulation per WiR)
        stable = (gtc is not None and loc == (gtc, gmaj))
        if stable:
            t.stable += 1

        # axis 2: two-parser concurrence (music21 romanText vs dcml_parser)
        m21_here = None
        if m21_idx is not None:
            m21_here = m21_idx.get((int(getattr(dr, 'measure_number', -1)),
                                    round(float(getattr(dr, 'beat', -1.0)), 3)))
        concur_known = m21_here is not None
        if concur_known:
            t.concur_known += 1
        concur = concur_known and (m21_here == loc)
        if concur:
            t.concur += 1
        if not concur_known:
            t.m21_missing += 1

        # the metric: unambiguous = stable AND concur
        unamb = stable and concur
        if unamb:
            t.unamb += 1
            t.dur_unamb += dur
            if full:
                t.unamb_full += 1
                t.dur_unamb_full += dur
            else:
                t.unamb_miss[(_km_name(our), _km_name(loc))] += 1
        else:
            t.amb += 1
            conf = float(getattr(ours_r, 'key_confidence', 0.0) or 0.0)
            if full:
                t.amb_top1 += 1
            elif in_top2:
                t.amb_in_top2 += 1
            else:
                t.amb_neither += 1
                if conf < FLAG_CONF_THRESHOLD:
                    t.amb_flagged += 1
    return t


def b_legacy_stable_full(ours_regions, wir_regions):
    """Compute the AUDIT-config (OLD extractor + stable-proxy, full corpus) stable and
    stable-full counts for one piece — the exact §3.3 sanity reproduction."""
    matches = cmp.align_dcml_regions(ours_regions, wir_regions,
                                     mode=cmp.DEFAULT_DCML_MATCH_MODE)
    stable = 0
    stable_full = 0
    for ours_r, dr in zip(ours_regions, matches):
        if dr is None:
            continue
        otc, omaj = C._our_key_tonic(getattr(ours_r, 'key', None))
        ltc, lmaj = C._dcml_key_tonic(getattr(dr, 'local_key', None))
        gtc, gmaj = C._dcml_key_tonic(getattr(dr, 'global_key', None))
        if otc is None or ltc is None:
            continue
        if gtc is not None and (ltc, lmaj) == (gtc, gmaj):   # stable
            stable += 1
            if (otc, omaj) == (ltc, lmaj):
                stable_full += 1
    return stable, stable_full


def b_score_corpus(ours_dir: Path, wir_base: Path, test_pct: int):
    """Returns dict: split -> BTally ('train','test','all'); plus coverage + m21 status."""
    splits = {'train': BTally(), 'test': BTally(), 'all': BTally()}
    legacy = {'stable': 0, 'stable_full': 0}      # audit-config sanity (full corpus)
    total = 0
    covered = 0
    m21_ok = 0
    m21_fail = []
    for p in sorted(ours_dir.glob("*.ours.json")):
        total += 1
        stem = p.name.replace(".ours.json", "")
        wir_path = dcml.find_wir_file(str(wir_base), stem)
        if not wir_path:
            continue
        try:
            _, ours_regions = cmp.load_analysis(p)
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not ours_regions or not wir_regions:
            continue
        covered += 1
        status, m21_idx = m21_local_index(wir_path)
        if status == 'ok':
            m21_ok += 1
        else:
            m21_idx = None
            m21_fail.append((stem, m21_idx))
        t = b_score_piece(ours_regions, wir_regions, m21_idx)
        sp = split_of(stem, test_pct)
        splits[sp].add(t)
        splits['all'].add(t)
        ls, lsf = b_legacy_stable_full(ours_regions, wir_regions)
        legacy['stable'] += ls
        legacy['stable_full'] += lsf
    meta = {'total': total, 'covered': covered, 'm21_ok': m21_ok,
            'm21_fail': len(m21_fail), 'legacy': legacy}
    return splits, meta


def _bpct(n, d):
    return (100.0 * n / d) if d else 0.0


def b_report(preset: str, splits, meta, test_pct: int) -> str:
    L = []
    L.append("=" * 84)
    L.append(f"INCREMENT B — {preset} — held-out direct key/mode vs WiR local GT")
    L.append("=" * 84)
    L.append(f"  corpus stems:      {meta['total']}   WiR-covered: {meta['covered']}  "
             f"(uncovered {meta['total'] - meta['covered']} — never scored)")
    L.append(f"  music21 2nd source: {meta['m21_ok']}/{meta['covered']} files parsed "
             f"({meta['m21_fail']} failed)")
    L.append(f"  held-out split:    md5(stem)%100 < {test_pct} = test  (deterministic)")
    L.append("")
    for sp in ('test', 'train', 'all'):
        t = splits[sp]
        tag = "◀ HEADLINE (out-of-sample)" if sp == 'test' else ""
        L.append(f"  ── split: {sp.upper()}  {tag}")
        L.append(f"     scorable regions: {t.scorable}   "
                 f"(our-keyfail FIXED {t.our_keyfail}, "
                 f"LEGACY {t.our_keyfail_legacy}, gt-keyfail {t.gt_keyfail})")
        L.append(f"     stable (local==global): {t.stable}  | "
                 f"parser-concur (m21==dcml): {t.concur}/{t.concur_known}  | "
                 f"m21-missing: {t.m21_missing}")
        L.append(f"     UNAMBIGUOUS (stable ∧ concur): {t.unamb}  "
                 f"({_bpct(t.unamb, t.scorable):.1f}% of scorable)")
        L.append(f"        → full (tonic+mode) match : "
                 f"{_bpct(t.unamb_full, t.unamb):5.1f}%  ({t.unamb_full}/{t.unamb})"
                 f"   [dur-wt {_bpct(t.dur_unamb_full, t.dur_unamb):.1f}%]")
        L.append(f"     AMBIGUOUS (complement): {t.amb}  "
                 f"({_bpct(t.amb, t.scorable):.1f}% of scorable)")
        L.append(f"        → top-1 match    : {_bpct(t.amb_top1, t.amb):5.1f}%  ({t.amb_top1}/{t.amb})")
        L.append(f"        → in-top-2 (not 1): {_bpct(t.amb_in_top2, t.amb):5.1f}%  ({t.amb_in_top2}/{t.amb})")
        L.append(f"        → neither        : {_bpct(t.amb_neither, t.amb):5.1f}%  ({t.amb_neither}/{t.amb})"
                 f"   (of which conf<{FLAG_CONF_THRESHOLD} flagged: {t.amb_flagged})")
        L.append("")
    # sanity reproduction of the audit baseline (full corpus, OLD extractor, stable proxy)
    lg = meta['legacy']
    L.append(f"  ── SANITY: audit-config reproduction (OLD extractor, stable==local==global "
             f"proxy, FULL corpus)")
    L.append(f"     stable full-match: {_bpct(lg['stable_full'], lg['stable']):.1f}%  "
             f"({lg['stable_full']}/{lg['stable']})   "
             f"[audit §3.3: Baroque 85.5%, Jazz 91.5%]")
    L.append("")
    tt = splits['test']
    L.append("  ── top UNAMBIGUOUS-bucket misses (test split; ours -> WiR-local, the real defects):")
    for (o, d), n in tt.unamb_miss.most_common(10):
        L.append(f"       {str(o):<8} -> {str(d):<8} {n}")
    return "\n".join(L)


def increment_b_main(args):
    root = Path(args.corpus_root)
    wir = Path(args.wir_base)
    test_pct = args.test_pct
    out = {}
    for preset in args.presets:
        d = root / preset
        if not d.is_dir():
            print(f"[skip] {d} not found")
            continue
        splits, meta = b_score_corpus(d, wir, test_pct)
        print(b_report(preset, splits, meta, test_pct))
        print()
        def _jsonable(v):
            if isinstance(v, Counter):
                # tuple keys (ours,gt) -> "ours->gt" so json can serialize
                return {(f"{a}->{b}" if isinstance(k, tuple) else str(k)): n
                        for k, n in v.items()
                        for a, b in [(k if isinstance(k, tuple) else (k, ""))]}
            return v
        out[preset] = {
            'meta': {k: v for k, v in meta.items() if k != 'legacy'},
            'legacy_sanity': meta['legacy'],
            'splits': {sp: {k: _jsonable(v) for k, v in t.__dict__.items()}
                       for sp, t in splits.items()},
        }
    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=2))
        print(f"[wrote] {args.json}")


def main():
    ap = argparse.ArgumentParser(description="Layer-3 key/mode ground-truth harness "
                                             "(Increment B held-out, default).")
    ap.add_argument("--corpus-root", default=str(REPO_ROOT / "tools" / "corpus"))
    ap.add_argument("--wir-base", default=str(C.WIR_BASE_DEFAULT))
    ap.add_argument("--presets", nargs="+", default=["baroque", "jazz"])
    ap.add_argument("--test-pct", type=int, default=TEST_PCT_DEFAULT,
                    help="held-out test fraction (md5(stem)%%100 < this); default 20")
    ap.add_argument("--legacy-audit", action="store_true",
                    help="run the original audit baseline (single-source proxy, OLD "
                         "extractor) instead of the Increment-B harness")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()
    if args.legacy_audit:
        legacy_main(args)
    else:
        increment_b_main(args)


if __name__ == "__main__":
    main()
