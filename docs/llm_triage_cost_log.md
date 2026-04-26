# LLM-Triage Cost Log

Running record of LLM API costs incurred by the triage pipeline, plus
per-provider cost-per-call data useful for forecasting full-corpus
runs. Update this file after each significant spend round so it stays
a working budget tool rather than a historical artifact.

## Recorded spend (as of 2026-04-26)

All work to date covers a single score:
`pachelbel-canon-in-d-arr-hiromi-uehara.mscz` (~85 measures, ~150 LLM
judgments per provider per call).

| Provider                | Total spend         | Paid calls | Per-call average      |
|-------------------------|---------------------|------------|-----------------------|
| Claude Sonnet 4.6       | $2.40 USD           | 4          | ~$0.60                |
| Gemini 3.1 Pro Preview  | 7.40 SEK (~$0.69)   | 3          | ~2.50 SEK (~$0.23)    |
| OpenAI GPT-5.5          | $2.34 USD           | 2          | ~$1.17                |
| **Total**               | **~$5.43 USD**      | **9**      |                       |

The Claude calls span v1.0 (first wired API), v1.1 (post-refactor
verification), and v1.2 Runs 1 + 3 (cache-test fresh and
force-refresh). The Gemini calls were v1.1 (post-billing-enable) and
v1.2 Runs 1 + 3. OpenAI's calls are v1.2 Runs 1 + 3 only — v1.2 was
its first integration. Free-tier Gemini attempts before billing
enablement returned 429 quota errors and incurred no charge.

## Per-call cost shape

OpenAI is the most expensive of the three at this tier because
reasoning tokens (the model's internal thinking before the visible
response) bill at output-token rates. GPT-5.5 with reasoning enabled
ran ~2300 reasoning tokens per call on Pachelbel. Without reasoning
mode, OpenAI would likely sit closer to Claude's per-call cost.

Claude is mid-tier; Gemini is cheapest, by roughly 5× over OpenAI.

## Pachelbel-equivalent forecasting unit

A "Pachelbel-equivalent" is one ~85-measure score producing ~150 LLM
judgments per provider. Cost across all three providers per
Pachelbel-equivalent is approximately **$2.00 USD** when running
fresh (no cache hits).

## Hiromi-corpus forecast

Conservative sizing of the 20 Hiromi scores, using Pachelbel as the
unit: most originals look 1-3 Pachelbel-equivalents; the largest
("Spiral", "Wake Up and Dream", similar) may run 4-5×. Working
estimate: 2 Pachelbel-equivalents per score on average.

20 × 2 × $2.00 ≈ **$80 worst-case** for a fresh full-corpus run
across all three providers. Realistic figure with the mix of small
and large scores averaging out is probably **$30-50**.

## Caching impact

`run_triage.py` (v1.2) caches per-provider responses keyed on
`(score_content_hash, model, prompt_version, system_prompt_hash,
tool_definition_hash)`. Once a (score, model, prompt-version) tuple
has been called, subsequent runs against the same key cost zero —
the script reads the existing JSON file instead of hitting the API.

Practical implication: the *first* full-corpus run is the expensive
operation. Iterating the comparator (v1.3) or other downstream tools
against the same cached responses is free. Cost re-enters when (a) a
new provider is added, (b) `prompt_version` is bumped, (c) new scores
enter the corpus, or (d) `--force-refresh` is passed deliberately.

## Free / paid tier notes

Gemini's AI Studio provides a free tier for older models
(`gemini-2.5-flash`, `gemini-2.0-flash`) but **not** for the
analytical/Pro/preview tier. v1.1 was initially blocked at `quota: 0`
on `gemini-2.5-pro` until billing was enabled. To use
`gemini-3.1-pro-preview` (the v1.2+ default), billing must be on.

Claude has no free tier. Anthropic Console requires loaded credits
before keys validate against the API.

OpenAI has no free tier. Platform requires a payment method on file
plus loaded credits before keys work.

## Practical budget framing

A starting balance of $20-30 on each of Anthropic and OpenAI, with
Gemini's pay-as-you-go billing already enabled, comfortably covers
the first full-corpus seeding plus generous iteration room. Sustained
operation thereafter is essentially free thanks to caching, provided
the prompt schema and model identifiers stay stable.

## How to update

After each significant round (a v1.x verification cycle, a batch
corpus run, a re-run after a prompt-version bump, etc.), append a new
dated section under "Recorded spend" with the new provider totals,
calls made since the last entry, and anything notable (reasoning-token
usage, surprise cost spikes, provider outages, model deprecations).
Don't overwrite the previous entry — keeping the running history
makes drift visible.

## Update — 2026-04-26 (v1.3-prep round)

Added one Bach chorale to the cache: `bwv10.7` (~46-68 judgments per
source depending on granularity). All three LLMs called fresh
(no cache hits — first run on this score).

| Provider | Calls (since prior log) | Tokens (in+out) | Actual spend |
|----------|-------------------------|-----------------|--------------|
| Claude   | 1   | 4099 + 7462         | $0.12        |
| Gemini   | 1   | 3205 + 3730         | 2.36 SEK     |
| OpenAI   | 1   | 3108 + 10637        | $0.34        |

Total round: $0.12 + 2.36 SEK (~$0.22) + $0.34 ≈ **$0.68 USD**
across all three providers on this single Bach chorale (much
shorter than Pachelbel).

**Forecasting recalibration.** Pre-bwv10.7 forecasts (per the
"Per-call cost shape" section earlier in this doc) underestimated
Gemini and OpenAI costs:

- **Gemini was the surprise.** Visible tokens (3205 in + 3730 out)
  suggest a small bill, but `gemini-3.1-pro-preview` either bills
  reasoning/thinking tokens beyond the visible output, or its rates
  are higher than the modest tier most older Gemini models used.
  Per-call reality is ~$0.20-0.25 on a small score, **not 5× cheaper
  than OpenAI as I'd modeled — closer to par.**
- **OpenAI** continues to be expensive due to reasoning-mode billing
  (10,637 output tokens for 65 judgments — much of that is internal
  reasoning).
- **Claude** matches the $3-in/$15-out Sonnet rate model accurately.

## Updated cumulative totals (Pachelbel + bwv10.7)

| Provider | Total spend         | Paid calls | Per-call average      |
|----------|---------------------|------------|-----------------------|
| Claude   | $2.52 USD           | 5          | ~$0.50                |
| Gemini   | 9.76 SEK (~$0.91)   | 4          | ~2.44 SEK (~$0.23)    |
| OpenAI   | ~$2.68 USD          | 3          | ~$0.89                |
| **Total**| **~$6.11 USD**      | **12**     |                       |

## Recalibrated Hiromi corpus forecast

With actuals showing Gemini and OpenAI both at roughly $0.20-0.30
per Bach-chorale-sized call, the per-Pachelbel-equivalent cost is
roughly:

- Claude: ~$0.50 per Pachelbel-eq
- Gemini: ~$0.40 per Pachelbel-eq (recalibrated up from initial estimate)
- OpenAI: ~$1.00 per Pachelbel-eq (largely from reasoning tokens)
- **All three together: ~$1.90 per Pachelbel-eq**

Hiromi corpus average ~2 Pachelbel-eq per score × 20 scores × $1.90
≈ **$76 worst-case fresh full-corpus run**. Realistic figure
**$40-60** with the small-score / large-score mix averaging out.

Slightly higher than the original $30-50 forecast, but still
hobby-budget territory. The correction is mostly Gemini —
free-tier-pricing intuitions don't transfer to the Pro/preview
tier we're actually using.

