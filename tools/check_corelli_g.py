import sys, json

data = json.load(open('C:/s/MS/tools/check_corelli_raw.json'))
for r in data.get('regions', []):
    if r.get('startTick', 0) >= 27000 and r.get('startTick', 0) <= 28500:
        print(f"t={r['startTick']:5} m={r['measureNumber']:2} b={r['beat']:4.1f} {r['quality']:12} {r['chordSymbol']:8} BIR={r.get('bassIsRoot','?')} key={r.get('key','?')}")
        for alt in r.get('alternatives', [])[:4]:
            print(f"  alt: {alt.get('chordSymbol','?'):8} score={alt.get('score',0):.3f} q={alt.get('quality','?')}")
