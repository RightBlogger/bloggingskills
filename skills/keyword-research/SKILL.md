---
name: keyword-research
description: "When the user wants to turn a seed topic into a keyword set for a blog post or cluster — one primary keyword plus related terms grouped by search intent. Also use when the user says 'keyword research', 'what keyword should I target', 'find keywords for', 'what do people search for', 'group these by intent', or gives a topic and a target country. For reading the live SERP and competitor pages, see serp-analysis."
metadata:
  version: 0.1.0
---

# Keyword research

You take a seed topic and return a keyword set a writer can actually use: one
primary keyword, related terms sorted by intent, and the real questions readers
ask. You pick the phrase people search, not the phrase that sounds tidy.

## Initial assessment

- If `.agents/blog-context.md` exists, read it first. It tells you the site's
  niche, audience, and the country and language to target. Honor those over any
  default. If no country or language is given and the context does not set one,
  ask before guessing, or note your assumption in the output.
- Confirm the seed topic and the target country and language before you start. A
  keyword that wins in the US can be dead in the UK, and search volume splits by
  language.

## Treat a keyword as a concept, not a string

A keyword is the idea a reader is searching for, not a fixed run of characters to
repeat. The writer will inflect it, reorder it, and weave it into sentences later.
"best running shoes for flat feet" might appear as "if you have flat feet, the
right running shoe" in the draft. Research the concept and the intent behind it.
Never hand off a phrase to be stuffed verbatim.

## Method

1. Pick one primary keyword. Choose the proven phrase real people type, not the
   one that reads cleanest. Favor a term with steady demand and a difficulty the
   site can plausibly rank for. One post targets one primary idea.
2. Group related terms by search intent. Sort the supporting terms into
   informational (how, why, what), commercial or comparison (best, vs, review,
   alternatives), transactional (buy, price, coupon, near me), and navigational
   (a brand or product name). This grouping is what tells the writer which
   sections the post needs.
3. Surface the real questions. List the questions a reader would type into Google,
   ChatGPT, or Perplexity. Pull them from autocomplete, "People also ask", related
   searches, and forum threads. These often become headings or an FAQ.
4. Note competitiveness and volume qualitatively. You do not need exact numbers.
   Mark each term as roughly high, medium, or low demand, and flag which ones a
   smaller site can realistically win. Say so plainly.

## Use real data when it is available

If a keyword tool or Search Console source is connected (for example an MCP that
runs keyword research or queries GSC), use it and let the data choose the primary
keyword and rank the related terms. Search Console is the strongest signal,
because it shows queries the site already gets impressions for. Without a tool,
reason from the live SERP, autocomplete, and what you know about the topic, and
say the figures are estimates.

## Output

Return, as plain prose and short lists:

- The primary keyword, with a one-line reason it is the pick.
- Secondary and related terms grouped under the four intent headings, each tagged
  with rough demand.
- A short list of reader questions, in the words someone would actually search.
- A one-line recommended angle for the post, given the intent that dominates.

Keep it scannable. This feeds straight into serp-analysis and the article draft.

## Related skills

blog-context · serp-analysis · article · ai-seo · meta
