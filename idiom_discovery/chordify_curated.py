import sys, os, time, pickle
sys.path.insert(0,'/sessions/nice-busy-fermat/mnt/MS/idiom_discovery')
from parsers.bach_chordify import load_xml_scores
setname, trad = sys.argv[1], sys.argv[2]
folder="/sessions/nice-busy-fermat/mnt/MS/corpora/expl/curated_mxl/"+setname
t=time.time(); ps=load_xml_scores(folder, setname, trad); dt=time.time()-t
print("%s: %d scores in %.0fs (%.1fs each)"%(setname,len(ps),dt,dt/max(len(ps),1)))
pf="/tmp/curated.pkl"
data=pickle.load(open(pf,"rb")) if os.path.exists(pf) else []
for p in ps:
    data.append((p.pid, setname, trad, p.transition_tokens(), len(p.chords)))
pickle.dump(data, open(pf,"wb"))
print("  saved; total curated pieces now:", len(data))
for p in ps:
    print("   %-45s chords=%d"%(p.pid[:45], len(p.chords)))
