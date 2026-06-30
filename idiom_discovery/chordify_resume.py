import sys, os, glob, time, pickle
sys.path.insert(0,'/sessions/nice-busy-fermat/mnt/MS/idiom_discovery')
from model import Piece, ChordEvent, name_to_fifths
from parsers.bach_chordify import q_m21
from music21 import converter, chord
PF="/tmp/curated.pkl"; MAX=5
CUR="/sessions/nice-busy-fermat/mnt/MS/corpora/expl/curated_mxl"
SETS=[("hiromi","jazz"),("steely_dan","pop"),("piazzolla","classical")]
data=pickle.load(open(PF,"rb")) if os.path.exists(PF) else []
done={d[0] for d in data}
queue=[(f,s,t) for s,t in SETS for f in sorted(glob.glob(os.path.join(CUR,s,"*.mxl"))) if os.path.basename(f) not in done]
print("remaining before:", len(queue)); t0=time.time(); did=0
for f,s,trad in queue:
    if did>=MAX: break
    pid=os.path.basename(f)
    try:
        sc=converter.parse(f); k=sc.analyze("key"); tf=name_to_fifths(k.tonic.name.replace("-","b"))
        chords=[]
        if tf is not None:
            for c in sc.chordify().recurse().getElementsByClass(chord.Chord):
                if len(c.pitches)<2: continue
                rf=name_to_fifths(c.root().name.replace("-","b"))
                if rf is not None: chords.append(ChordEvent(root_fifths=rf-tf,quality=q_m21(c)))
        p=Piece(source=s,pid=pid,chords=chords,mode=k.mode); toks=p.transition_tokens()
        data.append((pid,s,trad,toks,len(chords)))
    except Exception as e:
        data.append((pid,s,trad,[],0)); print("  ! skip",pid,str(e)[:40])
    pickle.dump(data,open(PF,"wb")); did+=1   # save after EACH
print("did %d in %.0fs; total %d; remaining %d"%(did,time.time()-t0,len(data),len(queue)-did))
