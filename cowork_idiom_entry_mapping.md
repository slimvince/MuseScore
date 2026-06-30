# Idiom mapping — encyclopedia catalog entries → the five idioms (for the StyleTag swap)

> **For the StyleTag implementation.** Each §5 entry of `cowork_progression_schema_dictionary.md` is tagged with its
> idiom(s) from the ratified set. **Multi-valued** — an entry can legitimately belong to several idioms (e.g. a plain
> ii–V–I is Diatonic-functional; with sevenths it is Seventh-functional). Provisional, easy to revise.
>
> Idioms: **1 Diatonic-functional · 2 Chromatic-functional · 3 Seventh-functional · 4 Triadic-modal ·
> 5 Chromatic-coloristic**. Cross-attributes (tagged separately per entry): **mode** (major/minor), **chromaticism**
> (diatonic↔chromatic).

## §5.1 — the function map (generative spine)
| Entry | Idiom(s) | Note |
|---|---|---|
| Diatonic functions (T / SD / D; descending-fifth/third, ascending-second motions) | **1** | the functional backbone |
| Secondary dominant `V7/x`, secondary leading-tone `viio7/x` | **2** | applied chromaticism |
| Applied ii–V (`IIm7/x → V7/x → x`) | **3** (+ **2**) | sevenths + applied |
| Substitute dominant `subV7/x` (tritone sub) | **5** | (its enharmonic German-6th reading → **2**) |
| Modal interchange (`iv, iiø, ♭VI, ♭III, ♭II`-Neapolitan, Picardy, minor `v`) | **2** | mixture; the **♭VII/♭VI triadic** borrowings also → **4** |

## §5.2 — named progressions & schemas
| Entry | Idiom(s) | Note |
|---|---|---|
| Cadential — authentic `V(7)→I`, half, plagal `IV→I` | **1** | basic cadences |
| Cadential — deceptive `V→vi/♭VI`, Phrygian half `iv6→V` | **1** (+ **2**) | the chromatic/Phrygian colour |
| **ii–V family** — `IIm7–V7–Imaj7`, minor `iiø7–V7–i`, incomplete ii–V | **3** | the jazz seventh-functional core |
| Turnarounds — `I–vi–ii–V`, `I–VI7–ii–V`, rhythm-changes A | **3** | the `VI7` secondary → also **2** |
| Sequences — circle-of-fifths | **1** / **3** | triadic → 1, sevenths → 3 |
| Sequences — descending-thirds (`I–vi–IV–ii`) | **1** | |
| Sequences — galant **Monte / Fonte** | **2** | ★ voice-leading-defined — *primary home is axis-2* |
| Bass/pop loops — **doo-wop** `I–vi–IV–V`, **Axis** `I–V–vi–IV` | **4** | triadic-modal pop |
| Bass/pop loops — **Pachelbel** | **4** (+ **1**) | |
| Bass/pop loops — **Andalusian** `i–♭VII–♭VI–V` (Phrygian) | **4** (+ **5**) | modal + chromatic-flavoured |
| Bass/pop loops — **lament bass** (chromatic descending tetrachord) | **2** / **5** | chromatic |
| **Galant schemata** — Prinner, Romanesca, Ponte, Do-Re-Mi, Quiescenza | **2** (provisional) | ★ **voice-leading-defined** — harmonic tag provisional; *primary identity is the voice-leading layer (axis 2)* |
| Advanced jazz — **Coltrane changes**, **backdoor** `♭VII7→I` | **5** | |

## §5.3 — substitution operations
| Entry | Idiom(s) | Note |
|---|---|---|
| Secondary dominant / tonicization | **2** | |
| Related ii–V | **3** | |
| **Tritone substitution (subV)** | **5** | |
| Diatonic (functional) substitution (`I↔iii↔vi`, `IV↔ii`, `V↔viio`) | **1** | |
| Modal interchange | **2** (+ **4** triadic borrowings) | |
| Diminished approach (passing/auxiliary dim7) | **2** | |
| Deceptive resolution (`V→vi/♭VI`) | **2** | |
| Line cliché (chromatic inner line) | **5** | voice-leading-adjacent |
| Upper-structure / voicing substitution | **— (out)** | a *voicing*, not a function-idiom (already out of scope, dictionary §5.3) |

## Notes for the re-tag
- **Multi-tag is correct, not a defect** — the functional family (1/2/3) overlaps by design (same progression, richer
  vocabulary), so many entries carry two idiom tags.
- **The galant schemata and line cliché are voice-leading-defined** (Prinner, Romanesca, … ; the cliché's chromatic
  line). Their harmonic-idiom tag here is a placeholder; their **primary identity belongs to the voice-leading axis**
  (the spec's future voice-leading layer) — flag them so the future layer claims them.
- Each entry also gets the two cross-attributes: **mode** (major / minor / either) and **chromaticism**
  (diatonic / chromatic), tagged independently of the idiom.
