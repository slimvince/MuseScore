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


def b_score_corpus(ours_dir: Path, wir_base: Path, test_pct: int, suffix: str = ".ours.json"):
    """Returns dict: split -> BTally ('train','test','all'); plus coverage + m21 status.

    `suffix` selects the source files: ".ours.json" (the per-region resolver
    baseline, default) or ".decode.json" (the Layer-3 decoder, via
    decode_keymode_corpus.py). Both are loaded by the SAME cmp.load_analysis +
    aligned by the SAME align_dcml_regions, so the only difference is whose
    key/mode is graded — the direct metric is identical."""
    splits = {'train': BTally(), 'test': BTally(), 'all': BTally()}
    legacy = {'stable': 0, 'stable_full': 0}      # audit-config sanity (full corpus)
    total = 0
    covered = 0
    m21_ok = 0
    m21_fail = []
    for p in sorted(ours_dir.glob("*" + suffix)):
        total += 1
        stem = p.name[:-len(suffix)]
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


def _directional(preset, base_splits, dec_splits):
    """Print the held-out DIRECTIONAL comparison (decoder vs per-region baseline),
    on the TEST split — the §4 grading signal. Granularity differs (the decoder is
    per-slice, the baseline per-region), so the duration-weighted full-match is the
    most comparable line."""
    bt, dt = base_splits['test'], dec_splits['test']
    L = []
    L.append("=" * 84)
    L.append(f"DIRECTIONAL — {preset} — decoder vs per-region baseline (TEST split, out-of-sample)")
    L.append("=" * 84)
    L.append(f"  unambiguous full (tonic+mode) match:")
    L.append(f"     per-region baseline : {_bpct(bt.unamb_full, bt.unamb):5.1f}%  "
             f"({bt.unamb_full}/{bt.unamb})   [dur-wt {_bpct(bt.dur_unamb_full, bt.dur_unamb):.1f}%]")
    L.append(f"     decoder (Layer 3)   : {_bpct(dt.unamb_full, dt.unamb):5.1f}%  "
             f"({dt.unamb_full}/{dt.unamb})   [dur-wt {_bpct(dt.dur_unamb_full, dt.dur_unamb):.1f}%]")
    L.append(f"  Δ full-match (decoder − baseline) : "
             f"{_bpct(dt.unamb_full, dt.unamb) - _bpct(bt.unamb_full, bt.unamb):+.1f} pts  "
             f"(dur-wt {_bpct(dt.dur_unamb_full, dt.dur_unamb) - _bpct(bt.dur_unamb_full, bt.dur_unamb):+.1f})")
    L.append(f"  tonic-only / mode-only on unambiguous misses (the rotation/relative defects):")
    L.append(f"     baseline top misses : "
             + ", ".join(f"{o}->{d}:{n}" for (o, d), n in bt.unamb_miss.most_common(5)))
    L.append(f"     decoder  top misses : "
             + ", ".join(f"{o}->{d}:{n}" for (o, d), n in dt.unamb_miss.most_common(5)))
    return "\n".join(L)


def increment_b_main(args):
    root = Path(args.corpus_root)
    wir = Path(args.wir_base)
    test_pct = args.test_pct
    decode_root = Path(args.decode_dir) if args.decode_dir else None
    out = {}
    for preset in args.presets:
        d = root / preset
        if not d.is_dir():
            print(f"[skip] {d} not found")
            continue
        splits, meta = b_score_corpus(d, wir, test_pct)
        print(b_report(preset, splits, meta, test_pct))
        print()
        if decode_root is not None:
            dd = decode_root / preset
            if dd.is_dir():
                dsplits, dmeta = b_score_corpus(dd, wir, test_pct, suffix=".decode.json")
                print(b_report(preset + " [DECODER]", dsplits, dmeta, test_pct))
                print()
                print(_directional(preset, splits, dsplits))
                print()
            else:
                print(f"[skip decoder] {dd} not found (run decode_keymode_corpus.py first)")
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


# ════════════════════════════════════════════════════════════════════════════
# CHARACTERIZATION SCAFFOLD (§1a–d) — read-only measurement of the EXISTING
# decoder output vs the held-out WiR local-key GT.  Reuses the Increment-B
# extractors / aligner / split (ONE grading path; no second metric forked).
#
#   §1a  Calibration   — reliability curve + uncertainty precision/recall +
#                        alternative-recall (does confidence track correctness?)
#   §1b  Residual buckets — relative-pair / tonicization-boundary / modal-GT /
#                        structurally-undecidable / genuinely-wrong / other
#   §1c  Modal-bucket audit — confirmed-defensible vs actually-wrong, by the
#                        slice's actual pitch content (from the corpus xml)
#   §1d  Per-beat granularity — re-grade at the quarter-note grid, not per-slice
#
# NOTHING here changes a decoder setting (no uncertainThreshold/topK/window
# move — that is the later, separately-ratified sweep).  It only measures.
# ════════════════════════════════════════════════════════════════════════════

# A genuine church-mode label (not plain major/minor/ionian/aeolian).  These are
# the readings a major/minor GT cannot represent — the "modal-GT-representational"
# excuse §1c guards against.
_CHURCH_MODE_PREFIXES = ('dor', 'phryg', 'phr', 'lyd', 'mixolyd', 'mix', 'locr',
                         'loc', 'aeol')  # aeol kept here only to EXCLUDE below


def _mode_token(keystr):
    """The mode-label portion of one of our key strings ('DDor' -> 'Dor')."""
    if not keystr:
        return ""
    m = _OURS_KEY_RE_FIXED.match(keystr.strip())
    return m.group(3) if m else ""


def _is_church_modal(keystr):
    """True iff the label names a church mode other than ionian/aeolian (= the
    plain major/minor the GT can encode).  'DDor','GMixolyd','Cphryg' -> True;
    'Gmaj','Amin','CIon','Aaeol' -> False."""
    tok = _mode_token(keystr).lower()
    if not tok:
        return False
    if tok.startswith(('maj', 'min', 'ion', 'aeol', 'harm', 'mel')):
        return False
    return tok.startswith(('dor', 'phryg', 'phr', 'lyd', 'mix', 'locr', 'loc'))


def _is_relative_pair(our, gt):
    """our,gt = (tonic_pc, is_major).  True iff they are the relative major/minor
    of each other (same key signature, opposite mode): major tonic = minor tonic
    + 3 semitones."""
    if not our or not gt or our[0] is None or gt[0] is None:
        return False
    if our[1] == gt[1]:
        return False
    maj, mino = (our, gt) if our[1] else (gt, our)
    return maj[0] == (mino[0] + 3) % 12


# Characteristic vs contradicting scale degrees (semitones above the modal tonic)
# for the modal-defensibility check (§1c).  char present + contra absent ⇒ the
# notes genuinely support the mode; contra present + char absent ⇒ the mode is an
# excuse for a plain major/minor reading.
_MODE_DEGREES = {
    'dor':     (9, 8),    # raised 6th vs natural-minor b6
    'mix':     (10, 11),  # b7 vs major 7th
    'mixolyd': (10, 11),
    'lyd':     (6, 5),    # #4 vs perfect 4th
    'phryg':   (1, 2),    # b2 vs major 2nd
    'phr':     (1, 2),
    'locr':    (1, 2),    # b2 (the b5 is shared with several modes)
    'loc':     (1, 2),
}


def _mode_degree_pair(keystr):
    """(char_semitone, contra_semitone) for the modal label, or None."""
    tok = _mode_token(keystr).lower()
    for pref, pair in _MODE_DEGREES.items():
        if tok.startswith(pref):
            return pair
    return None


def _region_records(decode_dir: Path, wir_base: Path, preset: str, test_pct: int):
    """Yield per-region characterization records for a preset's decoder corpus,
    on the held-out TEST split.  Each record carries everything §1a/b/c/d need:
    our (tonic,major)+raw key string, GT local+global, confidence, uncertain flag,
    the carried alternatives, whether stable/modulation, and the stem + slice tick
    span (for the §1c pitch lookup).  Reuses cmp.align_dcml_regions + the fixed
    extractors verbatim (one grading path)."""
    d = decode_dir / preset
    recs = []
    if not d.is_dir():
        return recs
    for p in sorted(d.glob("*.decode.json")):
        stem = p.name[:-len(".decode.json")]
        if split_of(stem, test_pct) != 'test':
            continue
        wir_path = dcml.find_wir_file(str(wir_base), stem)
        if not wir_path:
            continue
        try:
            data, ours_regions = cmp.load_analysis(p)
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not ours_regions or not wir_regions:
            continue
        raw = data.get("regions", [])
        matches = cmp.align_dcml_regions(ours_regions, wir_regions,
                                         mode=cmp.DEFAULT_DCML_MATCH_MODE)
        for idx, (ours_r, dr) in enumerate(zip(ours_regions, matches)):
            if dr is None:
                continue
            otc, omaj = our_key_tonic_fixed(getattr(ours_r, 'key', None))
            ltc, lmaj = C._dcml_key_tonic(getattr(dr, 'local_key', None))
            gtc, gmaj = C._dcml_key_tonic(getattr(dr, 'global_key', None))
            if otc is None or ltc is None:
                continue
            rawreg = raw[idx] if idx < len(raw) else {}
            alts = []
            for a in (getattr(ours_r, 'alternatives', []) or []):
                if isinstance(a, dict):
                    at, am = our_key_tonic_fixed(a.get('key'))
                    if at is not None:
                        alts.append((at, am))
            recs.append({
                'stem': stem,
                'our': (otc, omaj),
                'our_key': getattr(ours_r, 'key', ''),
                'loc': (ltc, lmaj),
                'glob': (gtc, gmaj) if gtc is not None else None,
                'conf': float(getattr(ours_r, 'key_confidence', 0.0) or 0.0),
                'uncertain': bool(rawreg.get('uncertain', False)),
                'alts': alts,
                'start_tick': int(getattr(ours_r, 'start_tick', 0)),
                'end_tick': int(getattr(ours_r, 'end_tick', 0)),
                'dur': max(0, int(getattr(ours_r, 'end_tick', 0)) - int(getattr(ours_r, 'start_tick', 0))),
                'correct': (otc, omaj) == (ltc, lmaj),
                'modulation': (gtc is not None and (ltc, lmaj) != (gtc, gmaj)),
            })
    return recs


# ── §1a  Calibration ─────────────────────────────────────────────────────────
_CONF_BINS = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, float('inf')]


def calibration(recs):
    bins = []
    for lo, hi in zip(_CONF_BINS[:-1], _CONF_BINS[1:]):
        sub = [r for r in recs if lo <= r['conf'] < hi]
        n = len(sub)
        acc = (sum(1 for r in sub if r['correct']) / n) if n else 0.0
        bins.append({'lo': lo, 'hi': hi, 'n': n, 'acc': acc})
    wrong = [r for r in recs if not r['correct']]
    uncert = [r for r in recs if r['uncertain']]
    # recall: of wrong, fraction flagged uncertain
    u_recall = (sum(1 for r in wrong if r['uncertain']) / len(wrong)) if wrong else 0.0
    # precision (strict): of uncertain, fraction wrong
    u_prec_strict = (sum(1 for r in uncert if not r['correct']) / len(uncert)) if uncert else 0.0
    # precision (inclusive): of uncertain, fraction wrong OR structurally ambiguous
    #   structural ambiguity = a modulation/tonicization region (GT local != global)
    #   OR our reading is the relative major/minor of GT (same notes, undecidable
    #   from one region) — both computable from the KEY GT alone (no chord evidence).
    def _amb(r):
        return (not r['correct']) or r['modulation'] or _is_relative_pair(r['our'], r['loc'])
    u_prec_incl = (sum(1 for r in uncert if _amb(r)) / len(uncert)) if uncert else 0.0
    # alternative-recall: of wrong, fraction where GT local is in carried alternatives
    alt_recall = (sum(1 for r in wrong if r['loc'] in r['alts']) / len(wrong)) if wrong else 0.0
    return {
        'n': len(recs), 'wrong': len(wrong), 'uncertain': len(uncert),
        'bins': bins,
        'uncert_recall': u_recall, 'uncert_prec_strict': u_prec_strict,
        'uncert_prec_incl': u_prec_incl, 'alt_recall': alt_recall,
    }


# ── §1b  Residual buckets ────────────────────────────────────────────────────
def bucket_misses(recs):
    """Bucket every scorable miss (our != GT local).  structurally-undecidable
    (symmetric dim7 / whole-tone / augmented) is NOT separable from KEY GT alone —
    it needs the slice pitch/chord content (out of L3-key scope, §5 stop) — so it
    is reported as a residual sub-count (uncertain-flagged share of 'other') and
    NOT fabricated as a hard bucket."""
    misses = [r for r in recs if not r['correct']]
    b = Counter()
    examples = {}
    for r in misses:
        if _is_relative_pair(r['our'], r['loc']):
            k = 'relative-pair'
        elif r['modulation']:
            k = 'tonicization-boundary'
        elif _is_church_modal(r['our_key']) and r['our'][0] == r['loc'][0]:
            k = 'modal-GT-representational'
        elif (not r['modulation']) and (not _is_church_modal(r['our_key'])):
            k = 'genuinely-wrong-resolvable'
        else:
            k = 'other'
        b[k] += 1
        examples.setdefault(k, []).append(r)
    # structurally-undecidable proxy: of the genuinely-wrong+other set, how many
    # are uncertain-flagged (a hint they may be the symmetric/ambiguous floor).
    resolvable_set = examples.get('genuinely-wrong-resolvable', []) + examples.get('other', [])
    undecidable_hint = sum(1 for r in resolvable_set if r['uncertain'])
    return {'n_miss': len(misses), 'buckets': dict(b),
            'undecidable_uncertain_hint': undecidable_hint,
            'examples': examples}


# ── §1c  Modal-bucket audit (pitch-content defensibility) ────────────────────
_M21_SCORE_CACHE = {}


def _pcs_in_window(xml_path, start_tick, end_tick, division=480):
    """Pitch-class set sounding in [start_tick, end_tick) of the corpus score,
    via music21 (offset in quarter notes = tick/division).  Cached per file."""
    try:
        from music21 import converter
    except Exception:
        return None
    key = str(xml_path)
    sc = _M21_SCORE_CACHE.get(key)
    if sc is None:
        try:
            sc = converter.parse(str(xml_path)).flatten().notes.stream()
        except Exception:
            _M21_SCORE_CACHE[key] = False
            return None
        _M21_SCORE_CACHE[key] = sc
    if sc is False:
        return None
    o_lo = start_tick / division
    o_hi = end_tick / division
    pcs = set()
    for n in sc:
        try:
            off = float(n.offset)
        except Exception:
            continue
        dur = float(getattr(n, 'quarterLength', 0.0) or 0.0)
        # a note sounds in the window if its span overlaps it
        if off < o_hi and (off + dur) > o_lo:
            for pp in (n.pitches if hasattr(n, 'pitches') else [n.pitch]):
                pcs.add(pp.pitchClass)
    return pcs


def modal_audit(modal_misses, corpus_xml_dir: Path, sample_cap=40):
    """For each modal-GT-representational miss, classify confirmed-defensible vs
    actually-wrong by the slice's actual pitch content."""
    defensible = wrong = inconclusive = no_pitch = 0
    details = []
    for r in modal_misses[:sample_cap]:
        pair = _mode_degree_pair(r['our_key'])
        if pair is None:
            inconclusive += 1
            continue
        char_deg, contra_deg = pair
        xmlp = corpus_xml_dir / f"{r['stem']}.xml"
        pcs = _pcs_in_window(xmlp, r['start_tick'], r['end_tick']) if xmlp.exists() else None
        if pcs is None:
            no_pitch += 1
            continue
        tonic = r['our'][0]
        char_present = ((tonic + char_deg) % 12) in pcs
        contra_present = ((tonic + contra_deg) % 12) in pcs
        if char_present and not contra_present:
            verdict = 'defensible'; defensible += 1
        elif contra_present and not char_present:
            verdict = 'actually-wrong'; wrong += 1
        else:
            verdict = 'inconclusive'; inconclusive += 1
        details.append((r['stem'], r['our_key'], _km_name(r['loc']), verdict))
    return {'defensible': defensible, 'actually_wrong': wrong,
            'inconclusive': inconclusive, 'no_pitch': no_pitch,
            'sampled': min(len(modal_misses), sample_cap),
            'total': len(modal_misses), 'details': details}


# ── §1d  Per-beat granularity ────────────────────────────────────────────────
def per_beat_grade(decode_dir: Path, wir_base: Path, preset: str, test_pct: int):
    """Re-grade the decoder at the quarter-note grid (per-beat) rather than per
    slice, alongside the region-level full-match, on the TEST split.  Reuses
    cmp._dcml_time_spans / cmp._infer_ticks_per_beat for the GT spans."""
    d = decode_dir / preset
    beats = scor = full = 0
    reg_scor = reg_full = 0
    if not d.is_dir():
        return None
    for p in sorted(d.glob("*.decode.json")):
        stem = p.name[:-len(".decode.json")]
        if split_of(stem, test_pct) != 'test':
            continue
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
        # region-level (equal-weight per slice) full-match
        matches = cmp.align_dcml_regions(ours_regions, wir_regions,
                                         mode=cmp.DEFAULT_DCML_MATCH_MODE)
        for ours_r, dr in zip(ours_regions, matches):
            if dr is None:
                continue
            otc, omaj = our_key_tonic_fixed(getattr(ours_r, 'key', None))
            ltc, lmaj = C._dcml_key_tonic(getattr(dr, 'local_key', None))
            if otc is None or ltc is None:
                continue
            reg_scor += 1
            if (otc, omaj) == (ltc, lmaj):
                reg_full += 1
        # per-beat
        spans = cmp._dcml_time_spans(ours_regions, wir_regions)
        tpb = cmp._infer_ticks_per_beat(ours_regions)
        step = int(round(tpb)) or 480
        gt = [(s, e, dr) for (s, e), dr in zip(spans, wir_regions) if s >= 0 and e > s]
        slices = sorted(ours_regions, key=lambda r: r.start_tick)
        if not slices:
            continue
        piece_start = min(r.start_tick for r in slices)
        piece_end = max(r.end_tick for r in slices)
        tick = piece_start
        while tick < piece_end:
            ourk = next((r.key for r in slices if r.start_tick <= tick < r.end_tick), None)
            gk = next((dr.local_key for (s, e, dr) in gt if s <= tick < e), None)
            if ourk is not None and gk is not None:
                otc, omaj = our_key_tonic_fixed(ourk)
                ltc, lmaj = C._dcml_key_tonic(gk)
                if otc is not None and ltc is not None:
                    scor += 1
                    if (otc, omaj) == (ltc, lmaj):
                        full += 1
            beats += 1
            tick += step
    return {
        'region_scorable': reg_scor, 'region_full': reg_full,
        'region_pct': _bpct(reg_full, reg_scor),
        'beat_scorable': scor, 'beat_full': full,
        'beat_pct': _bpct(full, scor),
        'delta': _bpct(full, scor) - _bpct(reg_full, reg_scor),
    }


def characterize_main(args):
    decode_dir = Path(args.decode_dir) if args.decode_dir else None
    if decode_dir is None:
        print("ERROR: --characterize requires --decode-dir "
              "(run decode_keymode_corpus.py first).")
        return
    wir = Path(args.wir_base)
    corpus_xml = Path(args.corpus_xml_dir)
    test_pct = args.test_pct
    out = {}
    for preset in args.presets:
        recs = _region_records(decode_dir, wir, preset, test_pct)
        cal = calibration(recs)
        buc = bucket_misses(recs)
        # §1c audits EVERY miss where the decoder emitted a genuine church-mode
        # label (Dor/Mix/Lyd/Phryg/Loc...), not only the narrow §1b
        # modal-GT-representational bucket (tonic-match ∧ stable ∧ non-relative):
        # most modal misses are same-collection rotations that land in the
        # relative-pair / tonicization buckets, yet the "is this a defensible modal
        # reading or an excuse?" question applies to ALL of them.  The narrow §1b
        # bucket count is reported separately above.
        modal_misses = [r for r in recs
                        if not r['correct'] and _is_church_modal(r['our_key'])]
        audit = modal_audit(modal_misses, corpus_xml, sample_cap=80)
        pb = per_beat_grade(decode_dir, wir, preset, test_pct)

        print("=" * 84)
        print(f"CHARACTERIZATION — {preset.upper()} — held-out TEST split "
              f"(md5(stem)%100<{test_pct})")
        print("=" * 84)
        print(f"  scorable regions (test): {cal['n']}   wrong: {cal['wrong']}   "
              f"uncertain-flagged: {cal['uncertain']}")
        print()
        print("  §1a CALIBRATION — reliability curve (confidence bin -> agreement):")
        for bn in cal['bins']:
            hi = "inf" if bn['hi'] == float('inf') else f"{bn['hi']:.1f}"
            bar = "#" * int(round(bn['acc'] * 30))
            print(f"     conf [{bn['lo']:.1f},{hi:>4}): n={bn['n']:4d}  "
                  f"acc={bn['acc']*100:5.1f}%  {bar}")
        print(f"     uncertainty RECALL  (wrong that were flagged) : {cal['uncert_recall']*100:5.1f}%")
        print(f"     uncertainty PRECISION (flagged that were wrong, strict) : "
              f"{cal['uncert_prec_strict']*100:5.1f}%")
        print(f"     uncertainty PRECISION (wrong OR struct-ambiguous, inclusive) : "
              f"{cal['uncert_prec_incl']*100:5.1f}%")
        print(f"     ALTERNATIVE-RECALL (true key in carried alternatives | wrong) : "
              f"{cal['alt_recall']*100:5.1f}%")
        print()
        print(f"  §1b RESIDUAL BUCKETS — {buc['n_miss']} scorable misses:")
        for k in ('relative-pair', 'tonicization-boundary', 'modal-GT-representational',
                  'genuinely-wrong-resolvable', 'other'):
            n = buc['buckets'].get(k, 0)
            print(f"     {k:<28} {n:4d}  ({_bpct(n, buc['n_miss']):4.1f}%)")
        print(f"     [structurally-undecidable (symmetric dim7/whole-tone/aug) is NOT")
        print(f"      separable from key GT alone — needs pitch/chord evidence (§5 stop);")
        print(f"      uncertain-flagged share of genuinely-wrong+other = "
              f"{buc['undecidable_uncertain_hint']} (ambiguity hint)]")
        print()
        print(f"  §1c MODAL-BUCKET AUDIT — {audit['total']} church-modal misses "
              f"(all modal readings; sampled {audit['sampled']}, pitch from corpus xml):")
        print(f"     confirmed-defensible : {audit['defensible']}")
        print(f"     actually-wrong       : {audit['actually_wrong']}")
        print(f"     inconclusive         : {audit['inconclusive']}   "
              f"(no-pitch {audit['no_pitch']})")
        for stem, ok, gt_, verdict in audit['details'][:12]:
            print(f"        {stem:<12} ours={ok:<10} gt={gt_:<8} -> {verdict}")
        print()
        if pb:
            print(f"  §1d GRANULARITY — region-level vs per-beat full (tonic+mode) match:")
            print(f"     region-level : {pb['region_pct']:5.1f}%  "
                  f"({pb['region_full']}/{pb['region_scorable']})")
            print(f"     per-beat     : {pb['beat_pct']:5.1f}%  "
                  f"({pb['beat_full']}/{pb['beat_scorable']})")
            print(f"     delta (beat - region) : {pb['delta']:+.1f} pts")
        print()
        out[preset] = {'calibration': {k: v for k, v in cal.items() if k != 'bins'},
                       'reliability_bins': cal['bins'],
                       'buckets': buc['buckets'],
                       'undecidable_uncertain_hint': buc['undecidable_uncertain_hint'],
                       'modal_audit': {k: v for k, v in audit.items() if k != 'details'},
                       'per_beat': pb}
    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=2))
        print(f"[wrote] {args.json}")


# ════════════════════════════════════════════════════════════════════════════
# CAUSAL DECOMPOSITION (the error-decomposition increment) — read-only.
#
# The characterization (cc_layer3_characterization_report.md §1a) found ~72–77%
# of WRONG slices CARRY the true key/mode in the alternatives but don't pick it
# (selection, not coverage). This mode answers WHY each carried-but-not-picked
# error is not picked, partitioning the carried error mass into:
#   A — L3 emission-recoverable   (Q3: distinguishing pc present, underweighted)
#   B — L3 cost-recoverable       (Q2: sustained modulation over-smoothed)
#   C — L5 cadence-required       (Q2 brief tonicization ∪ Q3 absent relative-pair)
#   D — L5 chord/spelling-required(Q3 absent ∧ symmetric sonority in window)
#   F — L5 cause-indeterminate-from-notes (Q3 absent, non-relative, non-symmetric;
#                                     a modal rotation / collection-share — §7 honest
#                                     "needs chord/function evidence" residual)
# plus the COVERAGE pile:
#   E — not-carried (true key never in the emitted alternatives), sub-split:
#         E-pruning  : loc appears elsewhere in the piece's decode (a viable state,
#                      locally outranked / pruned from this slice's top-alts) → L3
#         E-emission : loc never appears anywhere for the piece (emission never
#                      surfaces it) → structural / emission limit
#
# The decision tree (per CC instruction §1):
#   Q1  emission[correct] vs emission[picked]  (per-slice local-fit, NOT the margin)
#        correct > picked → TRANSITION (the sequence/cost overrode a locally-right
#                           emission) → Q2
#        correct ≤ picked → EMISSION (the emission itself preferred wrong) → Q3
#   Q2  GT-correct local key contiguous persistence around the slice (beats)
#        ≥ cutoff → B (sustained, over-smoothed real modulation)
#        < cutoff → C (brief tonicization the cost should suppress — L5 call)
#   Q3  distinguishing pc(s) present in the emission window (corpus xml)?
#        present (weight ≥ cutoff) → A (emission underweighted)
#        absent → relative-pair → C ; symmetric sonority → D ; else → F
#
# ONE grading path: reuses our_key_tonic_fixed / C._dcml_key_tonic /
# cmp.align_dcml_regions / split_of / _pcs_in_window / _is_relative_pair —
# the same extractors/aligner/split as Increment B and the characterization.
# NO decoder setting is read or changed; NOTHING is wired; read-only.
# ════════════════════════════════════════════════════════════════════════════

# Mode-tonic offset above the parent Ionian tonic (for the pitch-class COLLECTION
# of any key/mode label).  A church mode's collection IS a parent major scale; a
# plain minor's collection is its relative major.  This lets the "distinguishing
# diatonic pc" be computed as a true collection difference (so a modal ROTATION /
# relative pair correctly yields an EMPTY diatonic distinguisher — note-undecidable).
_MODE_TONIC_OFFSET = {
    'maj': 0, 'ion': 0, 'lyd': 5, 'mix': 7, 'dor': 2, 'phryg': 4, 'phr': 4,
    'aeol': 9, 'min': 9, 'loc': 11, 'locr': 11, 'harm': 9, 'mel': 9,
}
_IONIAN_DEGREES = (0, 2, 4, 5, 7, 9, 11)


def _mode_offset(mode_token):
    ml = (mode_token or '').lower()
    for pref, off in _MODE_TONIC_OFFSET.items():
        if ml.startswith(pref):
            return off
    return 0  # unknown -> treat as ionian


def _collection_of_keystr(keystr):
    """Pitch-class collection (parent major scale) of one of our key strings."""
    m = _OURS_KEY_RE_FIXED.match((keystr or '').strip())
    if not m:
        return None
    pc = (_NOTE_OURS[m.group(1)] + (1 if m.group(2) == '#' else -1 if m.group(2) == 'b' else 0)) % 12
    parent = (pc - _mode_offset(m.group(3))) % 12
    return frozenset((parent + d) % 12 for d in _IONIAN_DEGREES)


def _collection_of_pair(pair):
    """Collection of a plain (tonic_pc, is_major) GT key (minor -> relative major)."""
    if pair is None or pair[0] is None:
        return None
    parent = pair[0] % 12 if pair[1] else (pair[0] - 9) % 12
    return frozenset((parent + d) % 12 for d in _IONIAN_DEGREES)


def _distinguishing(correct, picked, picked_keystr):
    """(set_of_distinguishing_pcs, kind) separating CORRECT (plain maj/min GT) from
    PICKED (our reading, possibly church-modal).  Empty set = note-undecidable
    (relative pair without a sounded raised LT, or a same-collection modal rotation)."""
    coll_c = _collection_of_pair(correct)
    coll_p = _collection_of_keystr(picked_keystr) or _collection_of_pair(picked)
    if coll_c is None or coll_p is None:
        return (set(), 'unknown')
    if coll_c != coll_p:
        diff = set(coll_c) - set(coll_p)
        kind = 'parallel-third' if correct[0] == picked[0] else 'diatonic-diff'
        return (diff, kind)
    # same collection: relative pair (chromatic raised LT distinguishes) or rotation
    if _is_relative_pair(correct, picked):
        minor = correct if not correct[1] else picked
        return ({(minor[0] + 11) % 12}, 'relative-lt')
    return (set(), 'rotation')


def _symmetric_sonority(pcs):
    """'dim7' / 'aug' / 'whole-tone' / None for a pitch-class set (window content)."""
    s = set(pcs)
    if not s:
        return None
    for p in s:
        if {p, (p + 3) % 12, (p + 6) % 12, (p + 9) % 12} <= s:
            return 'dim7'
    for p in s:
        if {p, (p + 4) % 12, (p + 8) % 12} <= s:
            return 'aug'
    for wt in (frozenset({0, 2, 4, 6, 8, 10}), frozenset({1, 3, 5, 7, 9, 11})):
        if len(s & wt) >= 5 and s <= wt:
            return 'whole-tone'
    return None


def _pc_weights_in_window(xml_path, start_tick, end_tick, division=480):
    """{pitch_class: total quarter-length sounding} over [start,end) of the score.
    Reuses the _M21_SCORE_CACHE the §1c modal audit populates."""
    try:
        from music21 import converter  # noqa: F401
    except Exception:
        return None
    key = str(xml_path)
    sc = _M21_SCORE_CACHE.get(key)
    if sc is None:
        try:
            from music21 import converter
            sc = converter.parse(str(xml_path)).flatten().notes.stream()
        except Exception:
            _M21_SCORE_CACHE[key] = False
            return None
        _M21_SCORE_CACHE[key] = sc
    if sc is False:
        return None
    o_lo = start_tick / division
    o_hi = end_tick / division
    w = {}
    for n in sc:
        try:
            off = float(n.offset)
        except Exception:
            continue
        dur = float(getattr(n, 'quarterLength', 0.0) or 0.0)
        if off < o_hi and (off + dur) > o_lo:
            ov = min(off + dur, o_hi) - max(off, o_lo)
            if ov <= 0:
                continue
            for pp in (n.pitches if hasattr(n, 'pitches') else [n.pitch]):
                w[pp.pitchClass] = w.get(pp.pitchClass, 0.0) + ov
    return w


def _gt_timeline(ours_regions, wir_regions):
    """Merged contiguous (start_tick, end_tick, (tonic,major)) GT-local-key runs,
    and the inferred ticks-per-beat — for Q2 persistence."""
    spans = cmp._dcml_time_spans(ours_regions, wir_regions)
    tpb = cmp._infer_ticks_per_beat(ours_regions) or 480.0
    raw = []
    for (s, e), wr in zip(spans, wir_regions):
        if s < 0 or e <= s:
            continue
        k = C._dcml_key_tonic(getattr(wr, 'local_key', None))
        if k[0] is None:
            continue
        raw.append((s, e, (k[0], k[1])))
    raw.sort()
    merged = []
    for s, e, k in raw:
        if merged and merged[-1][2] == k and s <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e), k)
        else:
            merged.append([s, e, k])
    return merged, tpb


def _persistence_beats(merged, tpb, tick, loc):
    """Contiguous beat-length of the GT-correct (loc) key run covering `tick`."""
    for s, e, k in merged:
        if k == loc and s <= tick < e:
            return (e - s) / tpb
    # fall back: nearest loc run by midpoint (alignment slack)
    best = 0.0
    for s, e, k in merged:
        if k == loc:
            best = max(best, (e - s) / tpb)
    return best


def _decompose_signals(decode_dir, wir_base, corpus_xml_dir, preset, test_pct,
                       window_beats=4.0):
    """Single read-only pass: for every scorable MISS on the TEST split, compute the
    fixed (cutoff-independent) signals the Q1/Q2/Q3 tree needs.  Returns the list of
    per-miss signal dicts (cheap to re-bin under different cutoffs)."""
    d = Path(decode_dir) / preset
    sigs = []
    if not d.is_dir():
        return sigs
    corpus_xml = Path(corpus_xml_dir)
    for p in sorted(d.glob("*.decode.json")):
        stem = p.name[:-len(".decode.json")]
        if split_of(stem, test_pct) != 'test':
            continue
        wir_path = dcml.find_wir_file(str(wir_base), stem)
        if not wir_path:
            continue
        try:
            data, ours_regions = cmp.load_analysis(p)
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            continue
        if not ours_regions or not wir_regions:
            continue
        raw = data.get("regions", [])
        # piece-wide set of every (tonic,major) the decoder ever names (chosen ∪ alts)
        # over ALL slices — for the E coverage sub-split.
        piece_states = set()
        for rr in raw:
            pk = our_key_tonic_fixed(rr.get('key'))
            if pk[0] is not None:
                piece_states.add(pk)
            for a in rr.get('alternatives', []) or []:
                ak = our_key_tonic_fixed(a.get('key'))
                if ak[0] is not None:
                    piece_states.add(ak)
        merged, tpb = _gt_timeline(ours_regions, wir_regions)
        win = window_beats * tpb
        matches = cmp.align_dcml_regions(ours_regions, wir_regions,
                                         mode=cmp.DEFAULT_DCML_MATCH_MODE)
        for idx, (ours_r, dr) in enumerate(zip(ours_regions, matches)):
            if dr is None:
                continue
            otc, omaj = our_key_tonic_fixed(getattr(ours_r, 'key', None))
            ltc, lmaj = C._dcml_key_tonic(getattr(dr, 'local_key', None))
            gtc, gmaj = C._dcml_key_tonic(getattr(dr, 'global_key', None))
            if otc is None or ltc is None:
                continue
            our = (otc, omaj)
            loc = (ltc, lmaj)
            if our == loc:
                continue  # correct — not a miss
            # modulation = GT local key differs from the piece's global key (the
            # tonicization-boundary axis §1b uses).  Lets the report cross-tab the
            # L3 piles by stable-vs-modulation, so the A pile's tonicization overlap
            # (a present distinguishing pc that is really an applied tone, not key
            # evidence) is surfaced rather than silently counted as clean L3.
            modulation = (gtc is not None and loc != (gtc, gmaj))
            rawreg = raw[idx] if idx < len(raw) else {}
            our_key = getattr(ours_r, 'key', '') or ''
            start_t = int(getattr(ours_r, 'start_tick', 0))
            end_t = int(getattr(ours_r, 'end_tick', 0))
            # carried alternatives, each with its EMISSION (alt 'confidence' = .score)
            alts_emis = []
            for a in (getattr(ours_r, 'alternatives', []) or []):
                if isinstance(a, dict):
                    at, am = our_key_tonic_fixed(a.get('key'))
                    if at is not None:
                        alts_emis.append(((at, am), float(a.get('confidence', 0.0) or 0.0)))
            carried = any(k == loc for k, _ in alts_emis)
            emission_picked = rawreg.get('keyEmission', None)
            emission_picked = float(emission_picked) if emission_picked is not None else None
            emission_correct = max((e for k, e in alts_emis if k == loc), default=None)

            sig = {
                'stem': stem, 'start_tick': start_t, 'end_tick': end_t,
                'measure': int(getattr(ours_r, 'measure_number', 0) or 0),
                'our': our, 'loc': loc, 'our_key': our_key,
                'carried': carried,
                'modulation': modulation,
                'emission_picked': emission_picked,
                'emission_correct': emission_correct,
                'uncertain': bool(rawreg.get('uncertain', False)),
                'relative_pair': _is_relative_pair(our, loc),
                'loc_in_piece': loc in piece_states,
                'persistence_beats': _persistence_beats(merged, tpb, start_t, loc),
                'distinguish_pcs': None, 'distinguish_kind': None,
                'distinguish_weight': None, 'symmetric': None,
                'branch': None,
            }
            # branch (cutoff-independent) — needs both emissions
            if carried and emission_picked is not None and emission_correct is not None:
                sig['branch'] = 'TRANSITION' if emission_correct > emission_picked else 'EMISSION'
            # Q3 pitch evidence — only the EMISSION branch needs it (compute once)
            if sig['branch'] == 'EMISSION':
                dpcs, kind = _distinguishing(loc, our, our_key)
                sig['distinguish_pcs'] = sorted(dpcs)
                sig['distinguish_kind'] = kind
                xmlp = corpus_xml / f"{stem}.xml"
                wmap = _pc_weights_in_window(xmlp, int(start_t - win), int(end_t + win)) \
                    if xmlp.exists() else None
                if wmap is None:
                    sig['distinguish_weight'] = -1.0  # no-pitch sentinel
                else:
                    sig['distinguish_weight'] = max((wmap.get(pc, 0.0) for pc in dpcs),
                                                    default=0.0)
                    # Symmetry is a VERTICAL property of the chord AT the slice, not
                    # of the ±window (a wide window accumulates enough pcs to make a
                    # dim7/aug subset appear by chance).  Detect on the slice span only.
                    slice_pcs = _pcs_in_window(xmlp, start_t, end_t)
                    sig['symmetric'] = _symmetric_sonority(slice_pcs) if slice_pcs else None
            sigs.append(sig)
    return sigs


def _classify(sig, q2_cut, q3_cut):
    """Assign one miss to a pile under the given Q2 (sustained beats) and Q3
    (present-weight) cutoffs.  Cutoff-dependent only at the B/C and A/absent splits."""
    if not sig['carried']:
        return 'E-pruning' if sig['loc_in_piece'] else 'E-emission'
    if sig['branch'] is None:
        return 'UNSCORED'           # missing emission (should be ~0)
    if sig['branch'] == 'TRANSITION':
        return 'B' if sig['persistence_beats'] >= q2_cut else 'C'
    # EMISSION
    dw = sig['distinguish_weight']
    if dw is None:
        return 'F'
    if dw < 0:                       # no-pitch (xml unreadable) — cannot place in A
        return 'F-nopitch'
    present = (dw > 0.0) and (dw >= q3_cut)
    if present:
        return 'A'
    if sig['relative_pair'] or sig['distinguish_kind'] in ('relative-lt', 'rotation'):
        # note-undecidable relative / collection-share → cadence/function (L5)
        return 'C' if sig['relative_pair'] or sig['distinguish_kind'] == 'relative-lt' else 'F'
    if sig['symmetric']:
        return 'D'
    return 'F'


_PILES = ['A', 'B', 'C', 'D', 'F', 'F-nopitch', 'E-pruning', 'E-emission', 'UNSCORED']
_PILE_DESC = {
    'A': 'L3 emission-recoverable (Q3 present-underweighted)',
    'B': 'L3 cost-recoverable    (Q2 sustained over-smoothed modulation)',
    'C': 'L5 cadence-required    (Q2 brief tonicization ∪ Q3 absent relative-pair)',
    'D': 'L5 chord/spelling-req.  (Q3 absent ∧ symmetric dim7/aug/whole-tone)',
    'F': 'L5 cause-indeterminate  (Q3 absent, non-relative, non-symmetric / rotation)',
    'F-nopitch': '   (Q3 absent — xml pitch unreadable; cannot confirm A)',
    'E-pruning': 'COVERAGE: not-carried, loc IS a piece state (locally outranked) → L3',
    'E-emission': 'COVERAGE: not-carried, loc never named for piece (emission limit)',
    'UNSCORED': '(carried but an emission was missing — should be ~0)',
}


def _partition(sigs, q2_cut, q3_cut):
    c = Counter()
    for s in sigs:
        c[_classify(s, q2_cut, q3_cut)] += 1
    return c


def decompose_main(args):
    decode_dir = Path(args.decode_dir) if args.decode_dir else None
    if decode_dir is None:
        print("ERROR: --decompose requires --decode-dir.")
        return
    wir = Path(args.wir_base)
    corpus_xml = Path(args.corpus_xml_dir)
    test_pct = args.test_pct
    # central cutoffs + the §3 sensitivity grids
    q2_central, q3_central = 4.0, 0.0
    q2_grid = [2.0, 4.0, 8.0]      # sustained-persistence cutoff (beats)
    q3_grid = [0.0, 0.5, 1.0]      # distinguishing-pc present weight (quarter-lengths)
    out = {}
    for preset in args.presets:
        sigs = _decompose_signals(decode_dir, wir, corpus_xml, preset, test_pct)
        n_miss = len(sigs)
        n_carried = sum(1 for s in sigs if s['carried'])
        n_trans = sum(1 for s in sigs if s['branch'] == 'TRANSITION')
        n_emis = sum(1 for s in sigs if s['branch'] == 'EMISSION')
        part = _partition(sigs, q2_central, q3_central)

        print("=" * 88)
        print(f"DECOMPOSITION — {preset.upper()} — held-out TEST split "
              f"(md5(stem)%100<{test_pct})")
        print("=" * 88)
        print(f"  scorable misses (test): {n_miss}")
        print(f"    carried (true key in emitted alts): {n_carried}  "
              f"({_bpct(n_carried, n_miss):.1f}%)   "
              f"not-carried: {n_miss - n_carried}  ({_bpct(n_miss - n_carried, n_miss):.1f}%)")
        print(f"    Q1 branch of carried: TRANSITION (emission was right) {n_trans}  | "
              f"EMISSION (emission wrong) {n_emis}")
        print()
        print(f"  PARTITION at central cutoffs (Q2 sustained ≥ {q2_central:.0f} beats, "
              f"Q3 present weight > {q3_central:.1f}):")
        for k in _PILES:
            if part.get(k, 0) == 0 and k in ('UNSCORED', 'F-nopitch'):
                continue
            print(f"     {k:<11} {part.get(k,0):4d}  ({_bpct(part.get(k,0), n_miss):4.1f}% of miss)  "
                  f"{_PILE_DESC[k]}")
        l3_head = part.get('A', 0) + part.get('B', 0)
        l5_spec = part.get('C', 0) + part.get('D', 0) + part.get('F', 0) + part.get('F-nopitch', 0)
        print(f"     ── A+B (L3 headroom, UPPER BOUND): {l3_head}  ({_bpct(l3_head, n_miss):.1f}% of miss)")
        print(f"     ── C+D+F (L5 spec)       : {l5_spec}  ({_bpct(l5_spec, n_miss):.1f}% of miss)")
        print(f"     ── E (coverage)          : {part.get('E-pruning',0)+part.get('E-emission',0)}"
              f"  (pruning {part.get('E-pruning',0)} / emission {part.get('E-emission',0)})")
        print()
        # ── Reconciliation cross-tab: the L3 piles split by stable vs modulation.
        # A present distinguishing-pc in a MODULATION (tonicization) region cannot
        # be told from an applied tone by the notes alone — so A∩modulation overlaps
        # the §1b tonicization-boundary L5 mass and is NOT safely clean L3.  Only
        # A∩stable is unambiguously emission-reweighting headroom.  Same logic for B.
        def _xt(pile_keys):
            st = sum(1 for s in sigs if _classify(s, q2_central, q3_central) in pile_keys
                     and not s['modulation'])
            mo = sum(1 for s in sigs if _classify(s, q2_central, q3_central) in pile_keys
                     and s['modulation'])
            return st, mo
        a_st, a_mo = _xt({'A'})
        b_st, b_mo = _xt({'B'})
        print(f"  RECONCILIATION — L3 piles by stable / modulation (the §1b tonicization axis):")
        print(f"     A  stable {a_st:4d}  | modulation {a_mo:4d}  "
              f"(A∩stable = clean L3; A∩modulation overlaps L5 tonicization)")
        print(f"     B  stable {b_st:4d}  | modulation {b_mo:4d}")
        clean_l3 = a_st + b_st
        print(f"     ── CLEAN L3 (A∩stable + B∩stable): {clean_l3}  ({_bpct(clean_l3, n_miss):.1f}% of miss)")
        print()
        print(f"  §3 THRESHOLD SENSITIVITY:")
        print(f"    Q2 sustained cutoff (beats) → B (L3) / C (L5) split of the {n_trans} TRANSITION:")
        for q2 in q2_grid:
            pc = _partition(sigs, q2, q3_central)
            print(f"       ≥{q2:>4.0f} beats : B={pc.get('B',0):4d}  C(from-trans)={n_trans-pc.get('B',0):4d}")
        print(f"    Q3 present-weight cutoff → A (L3) / absent (L5) split of the {n_emis} EMISSION:")
        for q3 in q3_grid:
            pc = _partition(sigs, q2_central, q3)
            absent = n_emis - pc.get('A', 0)
            print(f"       >{q3:>4.1f} qL    : A={pc.get('A',0):4d}  absent(→C/D/F)={absent:4d}")
        print()
        # spot-check sample (the §3 manual verification dump)
        print(f"  §3 SPOT-CHECK SAMPLE (≤4 per pile; verify cause vs the score):")
        bypile = {}
        for s in sigs:
            bypile.setdefault(_classify(s, q2_central, q3_central), []).append(s)
        for k in ('A', 'B', 'C', 'D', 'F', 'E-pruning', 'E-emission'):
            for s in bypile.get(k, [])[:4]:
                ep = s['emission_picked']; ec = s['emission_correct']
                ep_s = f"{ep:.2f}" if ep is not None else "—"
                ec_s = f"{ec:.2f}" if ec is not None else "—"
                dw = s['distinguish_weight']
                dw_s = (f"{dw:.2f}" if (dw is not None and dw >= 0) else
                        ("nopitch" if dw == -1.0 else "—"))
                mflag = 'mod' if s['modulation'] else 'stab'
                print(f"     [{k:<10}] {s['stem']:<11} m{s['measure']:<3} {mflag} "
                      f"{s['our_key']:<9}->{_km_name(s['loc']):<8} "
                      f"emis pick={ep_s} corr={ec_s} | persist={s['persistence_beats']:.1f}b "
                      f"| dpc={s['distinguish_pcs']} kind={s['distinguish_kind']} w={dw_s} "
                      f"sym={s['symmetric']}")
        print()
        out[preset] = {
            'n_miss': n_miss, 'n_carried': n_carried,
            'n_transition': n_trans, 'n_emission': n_emis,
            'partition_central': dict(part),
            'A_plus_B_upperbound': l3_head, 'C_plus_D_plus_F': l5_spec,
            'A_stable': a_st, 'A_modulation': a_mo, 'B_stable': b_st, 'B_modulation': b_mo,
            'clean_L3_Astable_Bstable': clean_l3,
            'E_pruning': part.get('E-pruning', 0), 'E_emission': part.get('E-emission', 0),
            'sensitivity_q2': {f"{q2}": dict(_partition(sigs, q2, q3_central)) for q2 in q2_grid},
            'sensitivity_q3': {f"{q3}": dict(_partition(sigs, q2_central, q3)) for q3 in q3_grid},
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
    ap.add_argument("--decode-dir", default=None,
                    help="root of the Layer-3 DECODER corpus (<dir>/<preset>/*.decode.json, "
                         "produced by decode_keymode_corpus.py); when given, also grades the "
                         "decoder and prints the directional decoder-vs-baseline comparison")
    ap.add_argument("--legacy-audit", action="store_true",
                    help="run the original audit baseline (single-source proxy, OLD "
                         "extractor) instead of the Increment-B harness")
    ap.add_argument("--characterize", action="store_true",
                    help="run the §1a–d characterization scaffold (calibration / "
                         "residual buckets / modal-bucket audit / per-beat granularity) "
                         "on the decoder corpus; requires --decode-dir")
    ap.add_argument("--corpus-xml-dir", default=str(REPO_ROOT / "tools" / "corpus"),
                    help="dir of the corpus *.xml scores (for the §1c pitch-content "
                         "modal-defensibility check); default tools/corpus")
    ap.add_argument("--decompose", action="store_true",
                    help="run the CAUSAL DECOMPOSITION of the carried-but-not-picked "
                         "errors (Q1 emission / Q2 transition / Q3 emission tree → the "
                         "A/B/C/D/F + E coverage partition, with §3 sensitivity + "
                         "spot-check); requires --decode-dir (regenerated with keyEmission)")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()
    if args.decompose:
        decompose_main(args)
    elif args.characterize:
        characterize_main(args)
    elif args.legacy_audit:
        legacy_main(args)
    else:
        increment_b_main(args)


if __name__ == "__main__":
    main()
