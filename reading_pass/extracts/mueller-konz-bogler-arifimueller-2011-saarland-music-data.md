# EXTRACT — Müller, Konz, Bogler & Arifi-Müller 2011, "Saarland Music Data (SMD)" (ISMIR 2011 late-breaking) — population row 15, first pass

> **Establishment bound: NONE OF THE FETCH BOUNDS APPLY TO THIS ROW.** The user resolved the
> row's STOP by supplying the paper himself (2026-08-30); it is two pages and was **read whole
> at the object** (page images through the file tools). The PDF binary itself is landed beside
> the other fetched records at
> `docs/research_papers/reading_pass_2026_08/mueller-konz-bogler-arifimueller-2011-saarland-music-data.pdf`
> — the one population row whose primary sits on disk as a PDF. Identification basis: the user's
> own act answering the population file's §5 STOP; "the Saarland project" = Saarland Music Data,
> a collaboration of Saarland University / MPI Informatik (Müller, Konz) with the Hochschule
> für Musik Saar (Bogler, Arifi-Müller).

## What the paper is

A two-page DATASET description, not an algorithm or analysis paper. Saarland Music Data (SMD):
royalty-free music data at `www.mpi-inf.mpg.de/resources/SMD/`, licensed **CC BY-NC-SA 3.0
Unported** ("freely available for research purposes"), in two collections:

- **SMD MIDI-Audio Piano Music:** 50 pieces/movements of Western piano literature (Bach,
  Bartók, Beethoven, Brahms, Chopin, Haydn, Liszt, Mozart, Rachmaninoff, Ravel, Skryabin),
  performed by Hochschule students on a Yamaha Disklavier DCFIIISM4PRO — audio recordings with
  **perfectly synchronized MIDI files** capturing key and pedal movements (synchronization
  accuracy ~10 ms at the note-onset level; 44.1 kHz audio, MP3 192 kbit/s; no post-processing
  beyond trimming).
- **SMD Western Music:** audio recordings of 200 pieces/movements (piano, chamber music,
  Klavierlieder, some orchestral; Bach through Tchaikovsky), performed 2004–2010 under varying
  recording conditions.

Named intended uses, in the paper's words: "music transcription, performance analysis, music
synchronization, audio alignment, or source separation." File naming:
Composer_Work_Performer_Version.{mp3,mid}.

## Claims, labeled

- **[FACT — §2]** SMD is an AUDIO and performance-MIDI dataset with the properties above.
  That is the paper's whole content; it carries **no harmonic analysis, no key/mode/chord
  annotation, no analysis algorithm, and no measurement of any analysis**.
- Nothing rises to THEORY or CONJECTURE — there are no analytical claims to label.

## Coupling facts (mandatory)

- **Assumes upstream:** nothing — it is source data.
- **Hands downstream:** synchronized audio+performance-MIDI pairs and audio recordings; no
  annotations of the kind this project grades against.
- **Stated scope:** research use under a NonCommercial-ShareAlike licence.

## Bearing on the framework — NO BEARING

- **No design point of `FRAMEWORK.md` §9 is touched**: the dataset contains no symbolic scores
  with harmonic ground truth, no analysis method, and no evaluation methodology. The verdict in
  the disposition surface's vocabulary is **NO BEARING** for every design point and interface.
- **Corpus intake routing, for completeness:** were it ever brought in, the ruled intake
  discipline already disposes of it twice over — a newly acquired corpus enters as research
  material, never the gate (D-308), and recorded-performance material is OUT of corpus scope
  (D-366, the intonation ruling's corpus side). Its CC **BY-NC**-SA licence additionally sits
  outside the shipping-parameter licence pool's terms (D-292 territory) — noted, not ruled.
- The "German research branch" class of the disposition surface therefore adds context, not
  framework input: the Saarland collaboration's contribution is performance-aligned DATA for
  audio-side tasks, orthogonal to this project's notated-score analysis.

## Verification targets touched

- None of V1–V13 originates here.
