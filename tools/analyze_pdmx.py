import pandas as pd


df = pd.read_csv(r"C:\s\MS\tools\pdmx\PDMX.csv", low_memory=False)
print(f"Total scores: {len(df)}")
print(f"Columns: {list(df.columns)}")

# Genre distribution
print("\n--- Top 20 genres ---")
genres = df["genres"].dropna().str.split("-").explode().str.strip()
print(genres.value_counts().head(20))

# Annotation coverage
print(f"\nHas annotations: {df['has_annotations'].sum()}")
print(f"Has annotations %: {df['has_annotations'].mean():.1%}")

# Jazz-tagged scores
jazz = df[df["genres"].str.contains("jazz", case=False, na=False)]
print(f"\nJazz-tagged scores: {len(jazz)}")

# Jazz + annotations
jazz_ann = jazz[jazz["has_annotations"] == True]
print(f"Jazz + has_annotations: {len(jazz_ann)}")

# Jazz + annotations + polyphonic
jazz_poly = jazz_ann[jazz_ann["n_tracks"] > 1]
print(f"Jazz + has_annotations + n_tracks > 1: {len(jazz_poly)}")

# Jazz + annotations + polyphonic + quality filters
jazz_rated = jazz_poly[jazz_poly["rating"] > 3.5]
print(f"Jazz + has_annotations + n_tracks > 1 + rating > 3.5: {len(jazz_rated)}")

jazz_rated4 = jazz_poly[jazz_poly["rating"] > 4.0]
print(f"Jazz + has_annotations + n_tracks > 1 + rating > 4.0: {len(jazz_rated4)}")

if "is_official" in df.columns:
    jazz_official = jazz_poly[
        (jazz_poly["is_official"] == True)
        | (jazz_poly["is_user_publisher"] == True)
    ]
    print(f"Jazz + has_annotations + n_tracks > 1 + official/publisher: {len(jazz_official)}")

# Track count distribution for jazz+annotated
print("\n--- n_tracks distribution for jazz+annotated ---")
print(jazz_ann["n_tracks"].value_counts().head(10))

# Rating distribution for jazz+annotated+polyphonic
print("\n--- rating distribution for jazz+annotated+polyphonic ---")
print(jazz_poly["rating"].describe())

# Sample titles from best candidates
best = jazz_poly[jazz_poly["rating"] > 4.0]
if len(best) > 0:
    print("\n--- Sample titles (jazz+annotated+polyphonic+rating>4) ---")
    cols = [
        "title",
        "artist_name",
        "n_tracks",
        "rating",
        "n_annotations",
        "is_official",
        "is_user_publisher",
    ]
    available = [c for c in cols if c in df.columns]
    print(best[available].head(20).to_string())

# Also check: what annotation types exist?
# n_annotations counts all annotations including chord symbols,
# dynamics, tempo markings etc. Check if we can filter for
# chord-symbol-specific annotations
print("\n--- n_annotations distribution for jazz+polyphonic ---")
print(jazz_poly["n_annotations"].describe())
print(jazz_poly["n_annotations"].value_counts().head(10))

# How many jazz+polyphonic have substantial annotations
# (more than just dynamics — chord symbols would push this higher)
jazz_rich = jazz_poly[jazz_poly["n_annotations"] > 10]
print(f"\nJazz + polyphonic + n_annotations > 10: {len(jazz_rich)}")
jazz_rich_rated = jazz_rich[jazz_rich["rating"] > 3.5]
print(f"Jazz + polyphonic + n_annotations > 10 + rating > 3.5: {len(jazz_rich_rated)}")