import json, glob, os, re

NOTE_TO_PC = {'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,
              'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}

def parse_root(sym):
    m = re.match(r'^([A-G][b#]?)', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else -1

def parse_bass(sym):
    m = re.search(r'/([A-G][b#]?)$', sym)
    if m: return NOTE_TO_PC.get(m.group(1), -1)
    return parse_root(sym)

for f in sorted(glob.glob('tools/corpus/*.ours.json')):
    bwv = os.path.basename(f).replace('.ours.json','')
    data = json.load(open(f))
    for r in data.get('regions', []):
        if not r.get('bassIsRoot'): continue
        wq = r.get('quality','')
        if wq != 'Augmented': continue
        wb = r.get('bassPitchClass', -1)
        ws = r.get('chordScore', 0)
        for i, alt in enumerate(r.get('alternatives', [])):
            asym = alt.get('chordSymbol','')
            if 'mMaj7' not in asym: continue
            ab = parse_bass(asym)
            ar = parse_root(asym)
            if ab != wb: continue          # same bass
            if ar != (wb+5)%12: continue   # I7 interval
            margin = ws - alt.get('score', 0)
            print(f"{bwv:15s} m={r['measureNumber']:3} b={r['beat']}  "
                  f"{r['chordSymbol']:10s} -> {asym:15s}  alt_idx={i}  margin={margin:+.3f}")
            break
