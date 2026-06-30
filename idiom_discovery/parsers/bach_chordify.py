"""Note-level Bach chorale extraction via music21 chordify (the neutral, mechanical
path — NOT our Baroque-tuned analyzer; spec D6).  key via music21's analysis,
root via music21's normal-form root (both neutral heuristics, not our L3+)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import Piece, ChordEvent, name_to_fifths
from music21 import corpus, chord
def q_m21(c):
    try:
        if c.isDominantSeventh(): return 'dom7'
        if c.isDiminishedSeventh(): return 'dim7'
        if c.isHalfDiminishedSeventh(): return 'halfdim7'
    except Exception: pass
    qmap={'major':'maj','minor':'min','diminished':'dim','augmented':'aug'}
    if c.isTriad(): return qmap.get(c.quality,'other')
    if c.seventh is not None: return {'major':'maj7','minor':'min7'}.get(c.quality,'other')
    return qmap.get(c.quality,'other')
def load_bach(limit=60):
    pieces=[]
    for path in corpus.getComposer('bach'):
        if len(pieces)>=limit: break
        try: s=corpus.parse(path)
        except Exception: continue
        if len(s.parts)!=4: continue
        try: k=s.analyze('key')
        except Exception: continue
        tf=name_to_fifths(k.tonic.name.replace('-','b'))
        if tf is None: continue
        chords=[]
        for c in s.chordify().recurse().getElementsByClass(chord.Chord):
            if len(c.pitches)<2: continue
            rf=name_to_fifths(c.root().name.replace('-','b'))
            if rf is None: continue
            chords.append(ChordEvent(root_fifths=rf-tf, quality=q_m21(c)))
        if chords:
            pieces.append(Piece(source='bach_chordify', pid=os.path.basename(str(path)),
                                chords=chords, mode=k.mode, meta={'tradition':'classical'}))
    return pieces
if __name__=="__main__":
    import time,collections
    t=time.time(); ps=load_bach(limit=5); dt=time.time()-t
    print("parsed %d chorales in %.1fs (%.2fs each)"%(len(ps),dt,dt/max(len(ps),1)))
    tot=sum(len(p.chords) for p in ps)
    print("chords=%d top=%s"%(tot,dict(collections.Counter(c.quality for p in ps for c in p.chords).most_common(6))))
    print("ex tokens[:12]:", ps[0].tokens()[:12])

def load_xml_scores(folder, source, tradition, limit=None,
                    exts=(".xml",".mxl",".musicxml")):
    import glob as _g, os as _o
    from music21 import converter
    files=[]
    for e in exts: files+= _g.glob(_o.path.join(folder,"*"+e))
    files=sorted(files)
    if limit: files=files[:limit]
    pieces=[]
    for f in files:
        try: s=converter.parse(f)
        except Exception: continue
        try: k=s.analyze("key")
        except Exception: continue
        tf=name_to_fifths(k.tonic.name.replace("-","b"))
        if tf is None: continue
        chords=[]
        for c in s.chordify().recurse().getElementsByClass(chord.Chord):
            if len(c.pitches)<2: continue
            rf=name_to_fifths(c.root().name.replace("-","b"))
            if rf is None: continue
            chords.append(ChordEvent(root_fifths=rf-tf, quality=q_m21(c)))
        if chords:
            pieces.append(Piece(source=source, pid=_o.path.basename(f),
                                chords=chords, mode=k.mode, meta={"tradition":tradition}))
    return pieces
