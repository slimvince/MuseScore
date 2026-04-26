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
