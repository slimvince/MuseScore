import pandas as pd


df = pd.read_csv(r"C:\s\MS\tools\pdmx\PDMX.csv", low_memory=False)

jazz = df[df["genres"].str.contains("jazz", case=False, na=False)]
candidates = jazz[
    (jazz["n_tracks"] > 1)
    & (jazz["rating"] > 4.0)
    & (jazz["n_annotations"] > 100)
].sort_values("n_annotations", ascending=False)

print(f"Candidates: {len(candidates)}")
print("\n--- Top 20 by annotation count ---")
cols = ["title", "artist_name", "n_tracks", "rating", "n_annotations", "mxl"]
print(candidates[cols].head(20).to_string())

# Save full list for downloading
candidates[cols].to_csv(
    r"C:\s\MS\tools\pdmx\jazz_candidates.csv",
    index=False,
)
print(f"\nSaved {len(candidates)} candidates to jazz_candidates.csv")