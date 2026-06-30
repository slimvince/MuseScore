"""Voice-leading feature extractor (note-level only). Per voice -> consecutive melodic
intervals; per-piece profile = |interval| histogram (0..12) + repeat/step/leap rates.
Sources: music21 Bach chorales (4 parts) and DCML notes/ TSV (per staff+voice)."""
import os, sys, glob, collections
from fractions import Fraction
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def vl_profile(voices):
    ivs=[abs(s[i]-s[i-1]) for s in voices for i in range(1,len(s)) if s[i] is not None and s[i-1] is not None]
    if len(ivs)<8: return None
    a=np.array(ivs)
    hist=np.array([float(np.mean(a==k)) for k in range(12)]+[float(np.mean(a>=12))])  # P(|iv|=k)
    extra=np.array([float(np.mean(a==0)), float(np.mean((a>=1)&(a<=2))), float(np.mean(a>2))])  # repeat,step,leap
    return np.concatenate([hist, extra])

def load_chorales_vl(limit=60):
    from music21 import corpus
    out=[]
    for p in corpus.getComposer('bach'):
        if len(out)>=limit: break
        try: s=corpus.parse(p)
        except Exception: continue
        if len(s.parts)!=4: continue
        voices=[]
        for part in s.parts:
            seq=[n.pitch.midi for n in part.flatten().notes if n.isNote]
            voices.append(seq)
        pr=vl_profile(voices)
        if pr is not None: out.append((os.path.basename(str(p)),"chorale",pr))
    return out

def load_dcml_notes_vl(notes_dir, label, limit=None):
    files=sorted(glob.glob(os.path.join(notes_dir,"*.tsv")))
    if limit: files=files[:limit]
    out=[]
    for f in files:
        try: df=pd.read_csv(f,sep="\t",dtype=str)
        except Exception: continue
        if not {"midi","staff","voice","quarterbeats"}<=set(df.columns): continue
        voices=[]
        for (st,vo),g in df.groupby(["staff","voice"]):
            g=g.copy()
            try: g["_o"]=g["quarterbeats"].map(lambda x: float(Fraction(str(x))) if str(x) not in ("","nan") else 0.0)
            except Exception: continue
            g=g.sort_values("_o")
            seq=[int(float(m)) for m in g["midi"] if str(m) not in ("","nan")]
            if len(seq)>1: voices.append(seq)
        pr=vl_profile(voices)
        if pr is not None: out.append((os.path.basename(f),label,pr))
    return out

if __name__=="__main__":
    from sklearn.cluster import KMeans
    from sklearn.metrics import adjusted_rand_score as ARI
    C="/sessions/nice-busy-fermat/mnt/MS"
    data=load_chorales_vl(60)
    for d,lab in [("corpora/expl/dcml_mozart","piano"),("corpora/expl/dcml_beethoven","piano"),("corpora/expl/dcml_scarlatti","piano")]:
        data+=load_dcml_notes_vl(os.path.join(C,d,"notes"),lab)
    labels=np.array([d[1] for d in data]); X=np.array([d[2] for d in data])
    print("pieces: %d  (chorale %d, piano %d)"%(len(data),(labels=='chorale').sum(),(labels=='piano').sum()))
    km=KMeans(2,random_state=0,n_init=10).fit_predict(X)
    print("VL-clusters vs source(chorale/piano)  ARI=%.3f"%ARI(labels,km))
    for lab in ["chorale","piano"]:
        m=labels==lab; mp=X[m].mean(0)
        print("  %-8s mean: repeat=%.0f%% step(1-2)=%.0f%% leap(>2)=%.0f%%  |iv| P(3)=%.0f%% P(4)=%.0f%% P(7+)=%.0f%%"%(
            lab,100*mp[13],100*mp[14],100*mp[15],100*mp[3],100*mp[4],100*mp[7:13].sum()))
