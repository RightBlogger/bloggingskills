---
name: ai-seo
description: "When the user wants a post to be cited by AI search and answer engines — ChatGPT search, Perplexity, Google AI Overviews and AI Mode, Gemini, Claude. Also use when the user says 'AI SEO', 'AEO', 'GEO', 'LLM SEO', 'answer engine optimization', 'generative engine optimization', 'optimize for ChatGPT', 'optimize for Perplexity', 'AI Overviews', 'AI Mode', 'get cited by AI', 'AI citations', or 'should I add llms.txt'. Audits and edits a post so its answers are easy to lift and safe to cite, and separates what helps from what's myth. For on-page keyword optimization, see seo-optimize. For human-voice editing, see humanize. For SERP and competitor context, see serp-analysis. For an old post losing clicks to AI answers, see refresh."
metadata:
  version: 0.3.0
---

# AI SEO

You make a blog post the source AI answer engines quote: ChatGPT search, Perplexity,
Google AI Overviews and AI Mode, Gemini, and Claude. These engines retrieve pages
from a search index first and then quote passages that answer the question cleanly,
so a page has to be findable, and then easy to lift and safe to cite. You work on the
second part and check the first.

You're done when the post answers its core question in its opening, each section
leads with a self-contained answer, every important claim is specific and sourced,
the trust signals are visible, and the user knows which off-page steps matter.

## What helps and what doesn't

Give the user this distinction plainly, because the AEO and GEO space is full of
paid advice that isn't backed by the engines themselves.

What helps, and why:
- Ranking. AI features retrieve from the same index and ranking systems as regular
  search, often for several related sub-queries at once. A page that can't rank for
  any of them rarely gets cited.
- Front-loaded answers. Engines quote the opening of a page far more than the end.
- Self-contained, specific sentences with numbers, names, and dates. Engines quote
  sentences, not pages.
- Focused pages. A page that answers one question well beats an "ultimate guide"
  that answers twenty thinly.
- First-hand experience, original data, and a named author with real credentials.
  These make a quote safe to cite.
- Freshness that's real. ChatGPT and Perplexity lean toward recently updated pages,
  and a substantive update is worth showing with a visible date.
- Mentions elsewhere. Engines weigh what other sites, forums, and videos say about a
  brand, not only what the brand says about itself.

What doesn't, per Google's own guidance on AI search:
- An `llms.txt` file. Google Search ignores it, and there's no evidence it earns
  citations elsewhere.
- Chopping a page into tiny chunks or rewriting it in a special "AI style."
- Special schema for AI features. Structured data still helps regular rich results
  (Article, Product, VideoObject), but FAQ markup no longer produces rich results for
  most sites.
- A separate page for every phrasing of a question. That's scaled content abuse, and
  it can get a site demoted.
- Self-ranked "best X" lists that put the publisher first. Engines tend to cite those
  pages while leaving the publisher out of the answer.

[references/evidence.md](references/evidence.md) has the sources and numbers behind
these, dated. Cite them when the user asks why.

## Initial assessment

- If `.agents/blog-context.md` exists, read it for the author, credentials, and the
  "Experience and proof" section. A captured voice still wins over any rule here.
- Read the house-style rulebook at `../house-style/references/ai-tells.md` before you
  write any new sentence.
- Take the post as text or a URL. State the one question it answers in a sentence. If
  you can't, the page has no answer for an engine to lift; fix that first.
- If you can search the web, look at how AI answers currently handle the question and
  which pages they cite. That's the bar.
- If the post is stale (old prices, versions, or a past year in the title), say so
  first and point to refresh. Engines favor current pages, and no amount of
  restructuring makes an outdated answer safe to cite.

## Method

Audit against these checks, then apply or propose each edit.

1. Answer first. The core question gets a direct, self-contained answer in the first
   100 words, about 40 to 60 words long, quotable with no surrounding context. When
   this collides with another rule, a clear, quotable answer beats an exact word
   count.
2. Opening third. The key facts, numbers, and the main recommendation appear in the
   first third of the post, not saved for the end.
3. Section leads. Each H2 opens with one or two sentences that answer that section's
   question on their own. Rewrite headings toward how people actually ask only where
   that is how they search.
4. Sub-questions. List the follow-up questions a person (or an engine's fan-out)
   would ask next. Cover the missing ones inside this page, briefly. Don't propose new
   pages for each.
5. Specifics. Replace vague claims with numbers, names, dates, and sources. Flag any
   claim with no source rather than invent one.
6. Trust signals. A named author with relevant credentials, a visible publish or
   updated date, first-hand evidence (a test, a photo, original data), and links to
   primary sources.
7. A summary block. One short "Key takeaways" list near the top helps skimmers and
   gets quoted. Check the post doesn't already have one under another name (TL;DR,
   Summary, At a glance) before adding it.
8. FAQ. Add 3 to 5 questions only if readers still have real questions the body
   didn't answer. It's for readers and answer engines, not for rich results.
9. Access. If you can read the site's `robots.txt`, confirm it doesn't block the
   search crawlers the user cares about: Googlebot, Bingbot (Copilot draws on Bing),
   OAI-SearchBot for ChatGPT search, Claude-SearchBot, and PerplexityBot.
   Blocking a training crawler like GPTBot doesn't remove a site from those search
   results. For Google, two more switches decide eligibility: the site must be
   opted in to generative AI features in Search Console (an opted-out site gets no
   AI Overview or AI Mode citations), and the page must allow a snippet, so check
   for `nosnippet`, a tiny `max-snippet`, or `data-nosnippet` on the answer. If you
   can't see these settings, ask the user to confirm them.

One answer-first block and one takeaways list is the point. Don't stack summary boxes.

## Output

1. If the user asked a direct question (llms.txt, schema, a specific engine), answer
   it first in a few lines.
2. A short audit: which of the nine checks the post fails, worst first.
3. The edits, ready to paste, in this order: the answer-first opening, the takeaways
   list, the rewritten section leads, the added sub-question coverage, and the FAQ if
   it earned one.
4. Off-page steps, in two or three lines: where the brand should be mentioned or
   reviewed, a YouTube video if the topic suits one, and how to watch results. AI
   referrers (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com,
   claude.ai) belong in their own analytics channel. Search Console's generative AI
   report and Bing's AI Performance report show citations and impressions but not
   clicks, so read them as visibility, not traffic.

Don't restate the post back to the user.

## Related skills

seo-optimize · serp-analysis · refresh · article · humanize · house-style
