# Evidence behind the ai-seo checks

Collected October 2026. AI search changes fast, so treat every number here as a
snapshot and re-check the source before quoting it to a client. Studies show
correlation, not cause.

## What Google says about AI search

- AI Overviews and AI Mode are "rooted in our core Search ranking and quality
  systems" and retrieve from the Search index. No llms.txt, no special markup, and no
  need to break content into chunks or write in an AI style. Making pages for query
  fan-out variations falls under the scaled content abuse policy.
  Source: developers.google.com/search/docs/fundamentals/ai-optimization-guide
  (updated 2026-07-10).
- The helpful content guidance lists changing page dates to seem fresh and
  fabricated creator profiles (AI headshots, made-up names, false credentials) as
  warning signs, and says Google has no preferred word count.
  Source: developers.google.com/search/docs/fundamentals/creating-helpful-content
  (updated 2026-10-05).
- Generative AI content needs manual fact-checking, including titles, meta
  descriptions, structured data, and alt text.
  Source: developers.google.com/search/docs/fundamentals/using-gen-ai-content
  (updated 2026-10-01).
- FAQ rich results ended in May 2026; HowTo rich results ended in 2023.
  Source: developers.google.com/search/updates.
- To appear in AI Overviews and AI Mode, a page must be indexed and snippet-eligible,
  and the site must be opted in to generative AI features. Search Console has had an
  opt-out toggle (covering AI Overviews, AI Mode, and AI in Discover) since June,
  global from 2026-08-31; Google says it doesn't affect regular rankings.
  Sources: developers.google.com/search/docs/appearance/ai-features and
  blog.google/products-and-platforms/products/search/new-controls-website-owners
  (2026-06-03).
- Google says llms.txt is not used by Search and is neutral for rankings
  (2026-06-15). Ahrefs server logs found 97% of llms.txt files got zero requests in
  May 2026.

## Who gets cited

- Only 37.9% of AI Overview citations come from the top 10 organic results for the
  original query, down from 76% in mid-2025. Ahrefs attributes the drop to query
  fan-out: the engine searches related sub-queries and cites pages ranking for those.
  Source: ahrefs.com/blog/ai-overview-citations-top-10 (2026-03-02).
- In ChatGPT, pages whose titles closely match the prompt and whose URL slugs are
  natural language were cited more often.
  Source: ahrefs.com/blog/why-chatgpt-cites-pages (2026-04-15).
- About 44% of ChatGPT citations come from the first 30% of a page's text, and
  focused pages beat long all-in-one guides.
  Source: Kevin Indig, growth-memo.com (February and April 2026; partly paywalled).
- Across 304,000 cited URLs, clear summaries, visible E-E-A-T, Q&A formatting, and
  clean section structure were the content traits most associated with citation.
  Source: semrush.com/blog/content-optimization-ai-search-study (2026-01-14).
- ChatGPT and Perplexity cite fresher pages than Google's organic results do; AI
  Overviews showed no such preference.
  Source: ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content (2025-07).

- Adding JSON-LD schema showed no meaningful citation lift in AI Overviews, AI Mode,
  or ChatGPT. Source: ahrefs.com/blog/schema-ai-citations (2026-05-11).
- Word count barely correlates with AI Overview citation (0.04), and 53% of cited
  pages are under 1,000 words.
  Source: ahrefs.com/blog/short-vs-long-content-in-ai-overviews (2025-12).
- The most-cited domains in AI Overviews are YouTube (22.9%), Reddit (18.5%),
  Facebook (10.1%), Quora (4.7%), and Wikipedia (4.0%). Off-page presence on these
  platforms is part of AI visibility.
  Source: ahrefs.com/blog/most-cited-domains-ai-overviews (2026-09-02).

## What it does to clicks

- An AI Overview correlates with a 58% lower click-through rate for the top result.
  Source: ahrefs.com/blog/ai-overviews-reduce-clicks-update (2026-02-04).
- Organic CTR on queries with an AI Overview fell to 1.3% in December 2025 and was
  2.4% in February 2026, still below pre-AI Overview levels. Brands cited inside the
  AI Overview got about 120% more clicks per impression than those not cited.
  Source: seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
  (2026-04-24).
- Searchers clicked a result on 8% of visits with an AI summary, against 15% without.
  Source: pewresearch.org (2025-07-22).
- AI assistants still send a small share of total site traffic, so measure them, but
  don't trade search rankings for them.
  Source: seranking.com/blog/ai-traffic-research-study (2026).

## Crawlers

- OAI-SearchBot controls whether a site appears in ChatGPT search; GPTBot is the
  training crawler. Source: developers.openai.com/docs/bots.
- Claude-SearchBot and Claude-User are separate from the ClaudeBot training crawler.
  Source: support.claude.com/en/articles/8896518.

## Measuring it

- Search Console's generative AI performance reports (Search and Discover) show
  impressions, pages, countries, and devices, but no clicks. Global since
  2026-08-31. Source: developers.google.com/search/blog/2026/06/gen-ai-performance-reports.
- Bing Webmaster Tools has an AI Performance report with Copilot citations and
  grounding queries, also without clicks (public preview, 2026-02).
  Source: searchinfluence.com/blog/bing-ai-performance-report-copilot-citations
  (secondary).
