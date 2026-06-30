"""ChoCo JAMS reader (v1: the standard Harte `chord` namespace only — real-book/
isophonics/billboard).  key_mode gives the tonic; root key-normalized to the tune's
home key (first key obs).  Roman/Weimar/m21 namespaces are a follow-up."""
import os, sys, glob, json, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import Piece, ChordEvent, name_to_fifths, canon_quality_harte
_CH = re.compile(r"^([A-G][#b]*)(?::([^/]+))?(?:/.+)?$")
def _key_tonic(kv):
    if not kv: return None, None
    s = kv.strip()
    if ':' in s: ton, mode = s.split(':', 1)
    elif ' ' in s: ton, mode = s.split(' ', 1)
    else: ton, mode = s, 'major'
    return name_to_fifths(ton.strip()), ('minor' if 'min' in mode.lower() else 'major')
def _chord(v, tf):
    if not v or v in ('N', 'X'): return None
    m = _CH.match(v.strip())
    if not m or tf is None: return None
    rf = name_to_fifths(m.group(1))
    if rf is None: return None
    return ChordEvent(root_fifths=rf - tf, quality=canon_quality_harte(m.group(2) or 'maj'), raw=v)
def load_choco_harte(part_dir, source, tradition, limit=None):
    pieces = []
    files=sorted(glob.glob(os.path.join(part_dir,'choco','jams','*.jams')))
    if limit and len(files)>limit:
        import random as _r; _r.seed(0); files=_r.sample(files,limit)
    for jp in files:
        try: d = json.load(open(jp))
        except Exception: continue
        anns = d.get('annotations', [])
        ch = [a for a in anns if a.get('namespace') == 'chord']
        ky = [a for a in anns if a.get('namespace') == 'key_mode']
        if not ch: continue
        kv = ky[0]['data'][0]['value'] if ky and ky[0]['data'] else None
        tf, mode = _key_tonic(kv)
        chords = [c for c in (_chord(o.get('value'), tf) for o in ch[0]['data']) if c]
        if chords:
            pid = os.path.splitext(os.path.basename(jp))[0]
            pieces.append(Piece(source=source, pid=pid, chords=chords, mode=mode, meta={'tradition': tradition}))
    return pieces

import re as _re2
_M21=_re2.compile(r"^([A-G][#b\-]*)(.*)$")
def canon_quality_m21(q):
    q=q.strip()
    if q in ("","M","maj","major","6","M6"): return "maj"
    if q in ("m","min","-","m6","min6"): return "min"
    if q in ("7","dom7"): return "dom7"
    if q in ("m7","min7","-7"): return "min7"
    if q in ("M7","maj7","ma7","^7"): return "maj7"
    if q in ("dim","o","dim7","o7"): return "dim7" if "7" in q else "dim"
    if q in ("+","aug"): return "aug"
    if q in ("m7b5","%7","%","o/","ø","ø7"): return "halfdim7"
    if q in ("mM7","m(maj7)","minmaj7"): return "minmaj7"
    if q.startswith("sus"): return "sus"
    if q.startswith("M") or q.startswith("maj") or q.startswith("^"): return "maj7" if "7" in q else "maj"
    if q.startswith("m") or q.startswith("-"): return "min7" if "7" in q else "min"
    if "7" in q: return "dom7"
    return "other"
def _chord_m21(v, tf):
    if not v or v in ("N","X"): return None
    m=_M21.match(v.strip())
    if not m or tf is None: return None
    rf=name_to_fifths(m.group(1).replace("-","b"))
    if rf is None: return None
    return ChordEvent(root_fifths=rf-tf, quality=canon_quality_m21(m.group(2)), raw=v)
def load_choco_m21(part_dir, source, tradition, limit=None, nss=("chord_m21_abc","chord_m21_leadsheet")):
    import glob as _g, json as _j, os as _o, random as _r
    files=sorted(_g.glob(_o.path.join(part_dir,"choco","jams","*.jams")))
    if limit and len(files)>limit: _r.seed(0); files=_r.sample(files,limit)
    pieces=[]
    for jp in files:
        try: d=_j.load(open(jp))
        except Exception: continue
        anns=d.get("annotations",[])
        ch=[a for a in anns if a.get("namespace") in nss]
        ky=[a for a in anns if a.get("namespace")=="key_mode"]
        if not ch: continue
        kv=ky[0]["data"][0]["value"] if ky and ky[0]["data"] else None
        tf,mode=_key_tonic(kv)
        chords=[c for c in (_chord_m21(o.get("value"),tf) for o in ch[0]["data"]) if c]
        if chords:
            pieces.append(Piece(source=source,pid=_o.path.splitext(_o.path.basename(jp))[0],chords=chords,mode=mode,meta={"tradition":tradition}))
    return pieces

# --- weimar (chord_weimar: root + optional "-" for minor + digits) ---
import re as _re3
_WC=_re3.compile(r"^([A-G][#b]?)(-?)(.*)$")
def _wkey(kv):
    if not kv: return None,None
    if kv.endswith("-maj"): return name_to_fifths(kv[:-4]),"major"
    if kv.endswith("-min"): return name_to_fifths(kv[:-4]),"minor"
    return _key_tonic(kv)
def _q_weimar(minor, rest):
    if minor:
        if "maj7" in rest or "^" in rest: return "minmaj7"
        if "7" in rest: return "min7"
        return "min"
    if "maj7" in rest or "^" in rest: return "maj7"
    if "%" in rest: return "halfdim7"
    if "o" in rest or "dim" in rest: return "dim7" if "7" in rest else "dim"
    if "+" in rest or "aug" in rest: return "aug"
    if "7" in rest: return "dom7"
    return "maj"
def _chord_weimar(v, tf):
    if not v or v in ("N","X","NC"): return None
    m=_WC.match(v.strip())
    if not m or tf is None: return None
    rf=name_to_fifths(m.group(1))
    if rf is None: return None
    return ChordEvent(root_fifths=rf-tf, quality=_q_weimar(m.group(2)=="-", m.group(3)), raw=v)
# --- jazz-corpus (chord_jparser_harte: case-sensitive M/m) ---
_JP=_re3.compile(r"^([A-G][#b]?)(.*)$")
def _q_jparser(q):
    q=q.strip()
    if q in ("","M","6","M6"): return "maj"
    if q in ("m","m6","-"): return "min"
    if q=="7": return "dom7"
    if q in ("m7","-7"): return "min7"
    if q in ("M7","maj7","^7"): return "maj7"
    if q.startswith("sus"): return "sus"
    if q in ("o","dim"): return "dim"
    if q in ("o7","dim7"): return "dim7"
    if q in ("+","aug"): return "aug"
    if q in ("m7b5","%","%7","h7","mb5"): return "halfdim7"
    if q in ("mM7","m^7"): return "minmaj7"
    if q.startswith("M") or q.startswith("maj") or q.startswith("^"): return "maj7" if "7" in q else "maj"
    if q.startswith("m") or q.startswith("-"): return "min7" if "7" in q else "min"
    if "7" in q: return "dom7"
    return "other"
def _chord_jparser(v, tf):
    if not v or v in ("N","X","NC"): return None
    m=_JP.match(v.strip().split("/")[0])
    if not m or tf is None: return None
    rf=name_to_fifths(m.group(1))
    if rf is None: return None
    return ChordEvent(root_fifths=rf-tf, quality=_q_jparser(m.group(2)), raw=v)
def _load_choco_generic(part_dir, source, tradition, ns, keyfn, chordfn, limit=None):
    import glob as _g, json as _j, os as _o, random as _r
    files=sorted(_g.glob(_o.path.join(part_dir,"choco","jams","*.jams")))
    if limit and len(files)>limit: _r.seed(0); files=_r.sample(files,limit)
    out=[]
    for jp in files:
        try: d=_j.load(open(jp))
        except Exception: continue
        anns=d.get("annotations",[]); ch=[a for a in anns if a.get("namespace")==ns]
        ky=[a for a in anns if a.get("namespace")=="key_mode"]
        if not ch: continue
        kv=ky[0]["data"][0]["value"] if ky and ky[0]["data"] else None
        tf,mode=keyfn(kv)
        chords=[c for c in (chordfn(o.get("value"),tf) for o in ch[0]["data"]) if c]
        if chords: out.append(Piece(source=source,pid=_o.path.splitext(_o.path.basename(jp))[0],chords=chords,mode=mode,meta={"tradition":tradition}))
    return out
def load_choco_weimar(part_dir,source,tradition,limit=None):
    return _load_choco_generic(part_dir,source,tradition,"chord_weimar",_wkey,_chord_weimar,limit)
def load_choco_jparser(part_dir,source,tradition,limit=None):
    return _load_choco_generic(part_dir,source,tradition,"chord_jparser_harte",_key_tonic,_chord_jparser,limit)
