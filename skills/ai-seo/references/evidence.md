# Evidence behind the ai-seo checks

Collected October 2026, updated November 2026. AI search changes fast, so treat every number here as a
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
- Gemini 4 Hydrogen became the default model in AI Mode on 2026-11-12 and answers
  the hardest AI Overview questions. Google says its improved query fan-out links to
  "a broader range of helpful links than before," with no figures. Citation data
  from November spans this switch and the core update that began 2026-11-10.
  Source: blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade.

## Summaries and the AI shape

- Semrush found clear summaries among the traits most associated with citation
  (above). A separate 2026 study found the same habit marks a post as generated:
  across 2,250 human and 11,250 AI company blog posts, 88% of AI posts had a summary
  or synthesis stage against 27% of human ones, 77% closed by restating the opening
  (12% human), and 93% announced the thesis before the first section (51% human).
  Structure alone separated AI from human posts at 97.0 macro-F1, and 96.1 after
  each model reworded its own posts. These are a classifier's results, not a reader
  study, and the study counts any thesis stated before the first section, so a
  direct answer in the intro is part of the pattern too. The practical reading: keep
  the one answer-first opening that citation needs, and drop the roadmap paragraph,
  the takeaways box, and the recap close that pile on top of it.
  Sources: arxiv.org/abs/2609.15369 (SlopShape, September 2026);
  sitefire.ai/blog/how-to-tell-ai-slop-from-human-writing (2026-09-04).

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
- Google plans to honor a shared robots.txt policy token for AI training
  preferences, based on an IETF draft, starting in 2027. Nothing to deploy yet.
  Source: developers.google.com/search/updates (2026-10-30), as summarized at
  younusfardeen.in (secondary).

## Measuring it

- Search Console's generative AI performance reports (Search and Discover) show
  impressions, pages, countries, and devices, but no clicks. Global since
  2026-08-31. Source: developers.google.com/search/blog/2026/06/gen-ai-performance-reports.
  A logging error reportedly under-counted these impressions on 2026-11-09 to 11
  (and on 2026-08-13 to 17, later restored), so don't read a dip on those days as a
  loss. Source: mojodojo.io/blog/gemini-4-hydrogen-default-ai-mode (secondary;
  confirm against Search Console's own annotations).
- Bing Webmaster Tools has an AI Performance report with Copilot citations and
  grounding queries, also without clicks (public preview, 2026-02).
  Source: searchinfluence.com/blog/bing-ai-performance-report-copilot-citations
  (secondary).
