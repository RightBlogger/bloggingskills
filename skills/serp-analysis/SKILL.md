---
name: serp-analysis
description: "When the user wants to know what it takes to rank for a target keyword by reading the live top results and turning them into a content brief. Also use when the user says 'analyze the SERP', 'what's ranking for', 'check the competition for this keyword', 'what do I need to cover to rank', 'size up the top results', or gives a URL to analyze against the keyword it targets. For turning a seed topic into a keyword set, see keyword-research. For optimizing an existing draft against the results, see seo-optimize."
metadata:
  version: 0.1.0
---

# SERP analysis

You read the current top results for one keyword and report what it takes to win
the page. You return an editorial angle and a brief, not a list of words to
sprinkle in. The point is to find where the leaders are weak, not to copy them.

## Initial assessment

- If `.agents/blog-context.md` exists, read it first. It sets the niche,
  audience, and target country and language, and the SERP differs by all of them.
  Honor those over any default.
- Confirm the target keyword. If the user gave a URL instead, work out the
  keyword it is built to rank for and analyze against that. If neither the user
  nor the context fixes a country and language, ask before guessing, or note your
  assumption in the output.
- Check what you can fetch. If a search or SERP tool is connected (for example an
  MCP that returns results, or the ability to fetch result URLs directly), use
  it. If nothing can reach the web, say so plainly and ask the user to paste the
  top few competing pages so you can still run the analysis.

## Method

1. Pull the top three to five organic results. Skip ads and skip pure
   aggregators unless they genuinely compete. Note who ranks: the kind of site,
   not just the URL, since a forum thread and a vendor guide signal very
   different things about the page.
2. Read the dominant intent. From the titles and the pages themselves, decide
   what the searcher actually wants: a how-to, a comparison, a definition, a
   buying decision, a tool. Get this wrong and depth will not save the piece.
3. Map the table stakes. List the subtopics and headings that nearly every
   result covers. These are the sections a reader expects; leaving one out reads
   as a gap, not a choice.
4. Spot the optional angles. Note the subtopics only some pages cover. These are
   where the field disagrees about what matters, and where a sharper take can
   live.
5. Find the gap. This is the work. Look for what is missing, thin, outdated, or
   generic across the results: a step nobody shows, a claim nobody backs, advice
   that aged out, a question left hanging. Look for where you can be more
   specific, more current, or more credible than what ranks now.

## Use the gap, do not mirror the structure

Matching the leaders point for point earns you a page that is merely as good as
what already ranks, which is rarely enough to overtake it. Cover the table stakes
so you are in the race, then win on the gap. One genuine advantage beats adding a
tenth heading nobody asked for: first-hand testing, real numbers, a clearer
walkthrough, a more honest comparison.

## Output

Return a short brief in plain prose and tight lists:

- The dominant search intent, in one line, with the page type it implies.
- The must-cover subtopics, the table stakes a contender cannot skip.
- The gap: what is missing, thin, or dated across the current results, and where
  you can be more specific or credible.
- A recommended depth to be competitive: a rough word-count range and a
  heading-count range, drawn from what ranks, not a fixed target.
- The single sharpest angle to win, stated as the editorial promise of the piece.

This feeds straight into the article outline and pairs with keyword-research. For
tuning a draft you already have against the live results, hand off to
seo-optimize.

## Related skills

blog-context · keyword-research · article · seo-optimize · ai-seo · house-style
