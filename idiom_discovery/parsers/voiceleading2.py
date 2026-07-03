"""Voice-leading idiom discovery — fuller loaders + the second feature view (axis-2 study).

NEW code for the axis-2 follow-on (CC, 2026-07-03).  The pilot's View-A extractor
(`voiceleading.vl_profile`) is imported UNCHANGED and reused verbatim, so the pilot is a
strict subset (the pilot baseline reproduces byte-for-byte at the feature level).

What is new here:
  * fuller note-level loaders (all DCML notes/ corpora, full music21 4-part chorale set,
    curated .mxl at note level per notated (staff, voice) via music21 — NOT chordify);
  * View B: voice-pair MOTION-TYPE rates (parallel / similar / contrary / oblique),
    pure interval-arithmetic, no theory labels;
  * the source/era/texture lens maps (interpretation covariates only — never clustering input).

Method contract: `cowork_idiom_discovery_design.md` (discover -> then name; confound gate first-class;
no theory features in the encoding).  Coverage note (declared limitation, not solved here): we read
NOTATED voices only — implied polyphony / compound melody in a single notated voice reads as leapy;
that is a property of the representation, recorded, not corrected by any inference.
"""
from __future__ import annotations
import os, sys, glob, collections, bisect
from fractions import Fraction
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parsers.voiceleading import vl_profile          # View A — UNCHANGED (pilot-identical)

REPO_DEFAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------------------------------------------------------------------------
# View B — voice-pair motion-type rates.
# ---------------------------------------------------------------------------
def _motion(pu0, pu1, pv0, pv1):
    """Classify the simultaneous motion of two voices from (pu0,pv0) to (pu1,pv1).
    Pure interval arithmetic; no theory labels.  Returns one of
    'parallel' | 'similar' | 'contrary' | 'oblique', or None if neither voice moved.
      * oblique  — exactly one voice moves;
      * contrary — both move, opposite directions;
      * parallel — both move, same direction, and the harmonic interval is preserved;
      * similar  — both move, same direction, harmonic interval changes."""
    du = (pu1 > pu0) - (pu1 < pu0)
    dv = (pv1 > pv0) - (pv1 < pv0)
    if du == 0 and dv == 0:
        return None
    if du == 0 or dv == 0:
        return 'oblique'
    if du == -dv:
        return 'contrary'
    return 'parallel' if (pu1 - pv1) == (pu0 - pv0) else 'similar'


def vl_profile_B(voices_onset, min_events=8):
    """View B feature vector [P(parallel), P(similar), P(contrary), P(oblique)].

    `voices_onset`: list of voices, each a list of (onset, midi) with ONE pitch per
    onset (chords already reduced to a single sounding pitch by the loader).

    Simultaneity rule (stated for the report): for each concurrent voice pair (u, v) we
    sample at the merged sorted set of the two voices' note onsets; a voice's pitch at a
    sample is the pitch of its most recent onset <= t (piecewise-constant hold); motion is
    classified between consecutive samples, dropping samples where neither voice moves.
    Rates are aggregated over ALL voice pairs in the piece.  None if < min_events motions."""
    cnt = collections.Counter()
    n = len(voices_onset)
    for i in range(n):
        u = voices_onset[i]
        ou = [o for o, _ in u]; pu = [p for _, p in u]
        for j in range(i + 1, n):
            v = voices_onset[j]
            ov = [o for o, _ in v]; pv = [p for _, p in v]
            times = sorted(set(ou) | set(ov))
            prev = None
            for t in times:
                iu = bisect.bisect_right(ou, t) - 1
                iv = bisect.bisect_right(ov, t) - 1
                if iu < 0 or iv < 0:
                    continue                       # before one voice has started
                cur = (pu[iu], pv[iv])
                if prev is not None:
                    m = _motion(prev[0], cur[0], prev[1], cur[1])
                    if m:
                        cnt[m] += 1
                prev = cur
    tot = sum(cnt.values())
    if tot < min_events:
        return None
    return np.array([cnt['parallel'] / tot, cnt['similar'] / tot,
                     cnt['contrary'] / tot, cnt['oblique'] / tot])


# ---------------------------------------------------------------------------
# Loaders — each returns a list of unified per-piece records:
#   {id, source, texture, era, nvoices, nnotes, A (16-d or None), B (4-d or None)}
# A is computed by the pilot's vl_profile (unchanged); B by vl_profile_B.
# ---------------------------------------------------------------------------
def _topmidi(n):
    """Single sounding pitch for a music21 note/chord = the top (highest) pitch.
    None for unpitched/empty objects (guards against empty-chord / percussion notes)."""
    try:
        if n.isNote:
            return n.pitch.midi
        if n.isChord and len(n.pitches):
            return max(p.midi for p in n.pitches)
    except Exception:
        return None
    return None


def _dcml_voices(df):
    """(voices_A, voices_onset) from a DCML notes df.
    voices_A replicates the pilot's load_dcml_notes_vl EXACTLY (every midi row per
    (staff,voice), onset-sorted, chord tones exploded) so View A stays byte-compatible.
    voices_onset reduces each onset to a single top pitch for View B."""
    voices_A = []
    voices_on = []
    for (_st, _vo), g in df.groupby(["staff", "voice"]):
        g = g.copy()
        try:
            g["_o"] = g["quarterbeats"].map(
                lambda x: float(Fraction(str(x))) if str(x) not in ("", "nan") else 0.0)
        except Exception:
            continue
        g = g.sort_values("_o")
        seqA = [int(float(m)) for m in g["midi"] if str(m) not in ("", "nan")]   # pilot-identical
        if len(seqA) > 1:
            voices_A.append(seqA)
        on = collections.OrderedDict()                                            # onset -> top midi
        for o, m in zip(g["_o"], g["midi"]):
            if str(m) in ("", "nan"):
                continue
            mv = int(float(m))
            if o not in on or mv > on[o]:
                on[o] = mv
        seqB = list(on.items())
        if len(seqB) > 1:
            voices_on.append(seqB)
    return voices_A, voices_on


def load_dcml_notes(notes_dir, source, texture, era, limit=None):
    files = sorted(glob.glob(os.path.join(notes_dir, "*.notes.tsv")))
    if not files:
        files = sorted(glob.glob(os.path.join(notes_dir, "*.tsv")))
    if limit:
        files = files[:limit]
    out = []
    for f in files:
        try:
            df = pd.read_csv(f, sep="\t", dtype=str)
        except Exception:
            continue
        if not {"midi", "staff", "voice", "quarterbeats"} <= set(df.columns):
            continue
        vA, vOn = _dcml_voices(df)
        pid = os.path.basename(f)
        for suf in (".notes.tsv", ".tsv"):
            if pid.endswith(suf):
                pid = pid[:-len(suf)]; break
        out.append(dict(id=pid, source=source, texture=texture, era=era,
                        nvoices=len(vA), nnotes=sum(len(s) for s in vA),
                        A=vl_profile(vA), B=vl_profile_B(vOn)))
    return out


def load_m21_chorales(limit=None, texture="chorale", era="baroque"):
    """Full music21 4-part Bach chorale set (drop the pilot's limit=60).
    View A input replicates the pilot's load_chorales_vl exactly."""
    from music21 import corpus
    out = []
    for path in corpus.getComposer('bach'):
        if limit and len(out) >= limit:
            break
        try:
            s = corpus.parse(path)
        except Exception:
            continue
        if len(s.parts) != 4:
            continue
        vA = []
        vOn = []
        for part in s.parts:
            flat = part.flatten().notes
            seqA = [n.pitch.midi for n in flat if n.isNote]          # pilot-identical
            vA.append(seqA)
            on = collections.OrderedDict()
            for n in flat:
                if not n.isNote:
                    continue
                o = float(n.offset)
                mv = n.pitch.midi
                if o not in on or mv > on[o]:
                    on[o] = mv
            seqB = list(on.items())
            if len(seqB) > 1:
                vOn.append(seqB)
        out.append(dict(id=os.path.basename(str(path)), source="m21_chorale",
                        texture=texture, era=era,
                        nvoices=sum(1 for s in vA if len(s) > 1),
                        nnotes=sum(len(s) for s in vA),
                        A=vl_profile(vA), B=vl_profile_B(vOn)))
    return out


def load_curated_notes(folder, source, texture, era, limit=None,
                       exts=(".xml", ".mxl", ".musicxml")):
    """Curated full-arrangement scores at NOTE level, per notated (staff, voice) via
    music21 — NOT chordify (chordify destroys voices).  Chords within a notated voice are
    reduced to their top (melody) note (declared: this differs from the DCML branch, which
    explodes chord tones per the pilot; it is the cleaner reading for dense arrangements)."""
    from music21 import converter, stream
    files = []
    for e in exts:
        files += glob.glob(os.path.join(folder, "*" + e))
    files = sorted(files)
    if limit:
        files = files[:limit]
    out = []
    for f in files:
        try:
            s = converter.parse(f)
        except Exception:
            continue
        vA = []
        vOn = []
        for pi, part in enumerate(s.parts):
            vdict = collections.defaultdict(list)                    # (staff,voice) -> [(onset, topmidi)]
            measures = list(part.getElementsByClass(stream.Measure))
            if measures:
                for m in measures:
                    mo = float(m.offset)
                    vs = list(m.voices)
                    if vs:
                        for v in vs:
                            for n in v.notes:
                                mv = _topmidi(n)
                                if mv is not None:
                                    vdict[(pi, str(v.id))].append((mo + float(n.offset), mv))
                    else:
                        for n in m.notes:
                            mv = _topmidi(n)
                            if mv is not None:
                                vdict[(pi, "1")].append((mo + float(n.offset), mv))
            else:
                for n in part.flatten().notes:
                    mv = _topmidi(n)
                    if mv is not None:
                        vdict[(pi, "1")].append((float(n.offset), mv))
            for _k, seq in vdict.items():
                seq = sorted(seq)
                seqA = [mv for _o, mv in seq]
                if len(seqA) > 1:
                    vA.append(seqA)
                on = collections.OrderedDict()
                for o, mv in seq:
                    if o not in on or mv > on[o]:
                        on[o] = mv
                seqB = list(on.items())
                if len(seqB) > 1:
                    vOn.append(seqB)
        out.append(dict(id=os.path.basename(f), source=source, texture=texture, era=era,
                        nvoices=len(vA), nnotes=sum(len(s) for s in vA),
                        A=vl_profile(vA), B=vl_profile_B(vOn)))
    return out


# ---------------------------------------------------------------------------
# Interpretation-lens maps (post-hoc naming only — NEVER clustering input, spec §6).
# era: musicological consensus; texture: coarse scoring type.  Declared, not measured.
# ---------------------------------------------------------------------------
DCML_ERA = {
    # renaissance / early
    "monteverdi_madrigals": "renaissance", "sweelinck_keyboard": "renaissance",
    "frescobaldi_fiori_musicali": "renaissance", "peri_euridice": "renaissance",
    "kleine_geistliche_konzerte": "renaissance",
    # baroque
    "corelli": "baroque", "bach_chorales": "baroque", "bach_en_fr_suites": "baroque",
    "bach_solo": "baroque", "handel_keyboard": "baroque", "couperin_clavecin": "baroque",
    "couperin_concerts": "baroque", "pergolesi_stabat_mater": "baroque",
    "wf_bach_sonatas": "baroque",
    # classical / galant
    "scarlatti_sonatas": "classical", "cpe_bach_keyboard": "classical",
    "jc_bach_sonatas": "classical", "kozeluh_sonatas": "classical",
    "mozart_piano_sonatas": "classical", "beethoven_piano_sonatas": "classical",
    "ABC": "classical", "pleyel_quartets": "classical",
    # romantic
    "chopin_mazurkas": "romantic", "schumann_kinderszenen": "romantic",
    "schumann_liederkreis": "romantic", "c_schumann_lieder": "romantic",
    "liszt_pelerinage": "romantic", "mendelssohn_quartets": "romantic",
    "grieg_lyric_pieces": "romantic", "dvorak_silhouettes": "romantic",
    "tchaikovsky_seasons": "romantic", "schubert_winterreise": "romantic",
    "wagner_overtures": "romantic", "medtner_tales": "romantic",
    "rachmaninoff_piano": "romantic", "mahler_kindertotenlieder": "romantic",
    # modern
    "debussy_suite_bergamasque": "modern", "ravel_piano": "modern",
    "bartok_bagatelles": "modern", "poulenc_mouvements_perpetuels": "modern",
    "schulhoff_suite_dansante_en_jazz": "modern",
}
DCML_TEXTURE = {
    "bach_chorales": "chorale",
    "corelli": "chamber", "couperin_concerts": "chamber", "ABC": "chamber",
    "mendelssohn_quartets": "chamber", "pleyel_quartets": "chamber",
    "monteverdi_madrigals": "vocal", "kleine_geistliche_konzerte": "vocal",
    "pergolesi_stabat_mater": "vocal", "peri_euridice": "vocal",
    "schubert_winterreise": "vocal", "c_schumann_lieder": "vocal",
    "schumann_liederkreis": "vocal", "mahler_kindertotenlieder": "vocal",
    "wagner_overtures": "orchestral",
    # everything else = keyboard (default in loader)
}


def dcml_corpora(root=None):
    """Enumerate the DCML/DLC corpora that carry notes/*.tsv (canonical set = tools/dcml/;
    corpora/expl/dcml_* are dedup-verified clones and are excluded)."""
    root = root or REPO_DEFAULT
    base = os.path.join(root, "tools", "dcml")
    out = []
    for d in sorted(glob.glob(os.path.join(base, "*"))):
        nd = os.path.join(d, "notes")
        if os.path.isdir(nd) and glob.glob(os.path.join(nd, "*.tsv")):
            name = os.path.basename(d)
            out.append((name, nd, DCML_TEXTURE.get(name, "keyboard"),
                        DCML_ERA.get(name, "unknown")))
    return out
