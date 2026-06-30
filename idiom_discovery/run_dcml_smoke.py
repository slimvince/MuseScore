"""First discovery smoke: DCML classical corpora across ~250 years.
Validates the pipeline end-to-end and asks whether emergent topics/clusters track ERA."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parsers.dcml import load_dcml_repo
from extract import build_corpus
from discover import fit_lda, summarise

C = "/sessions/nice-busy-fermat/mnt/MS/corpora/expl"
ERA = {
    "beethoven_piano_sonatas": "classical", "chopin_mazurkas": "romantic",
    "schumann_kinderszenen": "romantic", "grieg_lyric_pieces": "late_romantic",
    "dvorak_silhouettes": "late_romantic", "tchaikovsky_seasons": "romantic",
    "liszt_pelerinage": "romantic", "medtner_tales": "late_romantic",
    "debussy_suite_bergamasque": "impressionist",
}
specs = [(f"{C}/dcml_scarlatti", "scarlatti", "baroque"),
         (f"{C}/dcml_mozart", "mozart", "classical"),
         (f"{C}/dcml_beethoven", "beethoven_qt", "classical")]
rom = f"{C}/dcml_romantic"
for sub in sorted(os.listdir(rom)):
    d = os.path.join(rom, sub)
    if os.path.isdir(os.path.join(d, "harmonies")):
        specs.append((d, sub, ERA.get(sub, "romantic")))

pieces = []
for d, comp, era in specs:
    ps = load_dcml_repo(d, source=comp, composer=comp)
    for p in ps:
        p.meta["era"] = era
    pieces += ps
    print(f"  {comp:26s} {era:14s} {len(ps):3d} pieces")

print(f"TOTAL pieces: {len(pieces)}")
X, vocab, meta = build_corpus(pieces, view="transition", min_df=5, max_df=0.95)
print(f"piece × transition-token matrix: {X.shape}  (vocab {len(vocab)})")
lda, dt = fit_lda(X, n_topics=10, seed=0)
summarise(lda, dt, vocab, meta, n_clusters=6, seed=0)
