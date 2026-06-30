import os, sys, random
import numpy as np
from scipy import sparse
sys.path.insert(0,'/sessions/nice-busy-fermat/mnt/MS/idiom_discovery')
from parsers.dcml import load_dcml_repo
from parsers.jht import load_jht
from parsers.mcgill import load_mcgill
from parsers.choco import load_choco_harte, load_choco_m21
from parsers.bach_chordify import load_bach
C="/sessions/nice-busy-fermat/mnt/MS/corpora"; P=C+"/ship/choco/partitions"; T="/sessions/nice-busy-fermat/mnt/MS/tools"
# chord-tone offsets in FIFTHS relative to root (spelling-aware, Moss-style)
CT={"maj":[0,4,1],"min":[0,-3,1],"dim":[0,-3,-6],"aug":[0,4,8],
    "dom7":[0,4,1,-2],"min7":[0,-3,1,-2],"maj7":[0,4,1,5],"halfdim7":[0,-3,-6,-2],
    "dim7":[0,-3,-6,-9],"minmaj7":[0,-3,1,5],"aug7":[0,4,8,-2],"sus":[0,-1,1]}
LO,HI=-12,12; W=HI-LO+1
def profile(p):
    v=np.zeros(W)
    for c in p.chords:
        if c.root_fifths is None: continue
        for off in CT.get(c.quality,[0]):
            f=c.root_fifths+off
            if LO<=f<=HI: v[f-LO]+=1
    s=v.sum()
    return v/s if s>0 else v
random.seed(0)
classical=[]
specs=[C+"/expl/dcml_scarlatti",C+"/expl/dcml_mozart",C+"/expl/dcml_beethoven",T+"/dcml/corelli"]
rom=C+"/expl/dcml_romantic"
specs+=[os.path.join(rom,s) for s in os.listdir(rom) if os.path.isdir(os.path.join(rom,s,"harmonies"))]
for d in specs:
    ps=load_dcml_repo(d,source="dcml",composer=os.path.basename(d))
    for p in ps: p.meta["tradition"]="classical"
    classical+=ps
classical+=load_bach(limit=40)
jazz=load_jht(C+"/expl/jazz_harmony_treebank/treebank.json")+load_choco_harte(P+"/real-book","real-book","jazz",limit=500)
pop=load_mcgill(C+"/ship/McGill-Billboard")+load_choco_harte(P+"/isophonics","isophonics","pop")
folk=load_choco_m21(P+"/nottingham","nottingham","folk",limit=500)
samp=lambda l,n: random.sample(l,n) if len(l)>n else l
N=400
pieces=samp(classical,N)+samp(jazz,N)+samp(pop,N)+samp(folk,N)
random.shuffle(pieces)
Xp=np.array([profile(p) for p in pieces])
np.save("/tmp/Xp.npy",Xp)
print("saved Xp",Xp.shape,"(should align with X2 rows=",1600,")")
