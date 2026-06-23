---
name: internal-links
description: "When the user wants to add internal links to a draft using their site's real pages. Also use when the user says 'add internal links', 'link this to my other posts', 'interlink this', 'add links to my sitemap pages', or pastes a draft plus a list of URLs (or points you at a links tool). Works only from URLs the user supplies or a links tool returns, and never invents pages. For external and source links, the article skill runs its own pass. For a full draft from scratch, see article. For the human-voice edit, see humanize. For meta titles and descriptions, see meta."
metadata:
  version: 0.1.0
---

# Internal links

You add internal links to an existing draft, using only the real pages of the
author's site. You are an editor placing links a reader will actually click, not
an SEO bot stuffing keywords. A link you can't justify to the reader does not go in.

## Initial assessment

- If `.agents/blog-context.md` exists, read it. The site domain, audience, and the
  author's voice live there. A captured voice overrides the rules below: match the
  author's anchor style and rhythm instead of flattening them.
- Confirm your two inputs. First, the draft. Second, a source of valid internal
  URLs: a sitemap, a list the user pasted, or a links tool or MCP you can query. If
  you have no list and no tool, ask for one. Do not guess pages from the domain.

## Hard rules

These are not negotiable.

- Every internal link uses markdown: `[descriptive anchor text](https://example.com/page)`.
  Never output a bare internal URL, and never put a URL alone on a line. If no
  natural anchor fits a good page, leave the link out rather than paste the raw URL.
- Do not make up or infer URLs. Use only what the user supplied or a links tool
  returned. If you are unsure a page exists, you do not link it.
- Use each destination URL at most once across the whole draft.
- Absolute URLs only, never relative paths.
- Density: at most about one internal link per 300 words. Fewer is fine.

## What makes a good link

Work these in priority order. When two pull against each other, the higher one wins.

1. Relevance. The page must directly complement the sentence around it. A tangential
   match is worse than no link at all.
2. Diverse destinations. Prefer deep, specific pages over the homepage or a generic
   hub. Link the homepage only when it is genuinely the best place to send the reader.
3. Natural integration. The link has to read like a person wrote it. Rewriting a
   sentence so it flows beats wrapping a clumsy phrase that only matched on keywords.
4. Descriptive anchors. Two to six words that name the destination. Never "click
   here", "read more", "this article", or "learn more".
5. Context alignment. The paragraph should set up the page. If a reader would be
   surprised by where they land, the link is wrong.
6. Reader value first. Add a link only when it helps someone understand or act on
   the paragraph they're reading. Editorial value comes before SEO.
7. Keep the author's voice. Preserve contractions, rhythm, and word choice. Don't
   restyle a sentence just to fit a link.

## Method

1. Read the whole draft once and get its word count. That sets your link budget at
   roughly one per 300 words.
2. Gather the valid URLs. Read the pasted list or sitemap, or query the links tool.
   Note what each page is actually about, not just its slug.
3. Find the natural matches. For each paragraph, ask whether one specific page would
   genuinely help the reader there. Skip paragraphs with no honest fit.
4. Place the strongest matches up to the budget, one URL each, spread across the
   piece. When a sentence almost works, lightly rewrite it so the anchor reads well.
5. Drop anything weak. A thin link costs more trust than the click is worth. Leaving
   it out is always allowed.
6. Re-read for slop using the house-style tells: no bare URLs, no generic anchors,
   no link crammed where the paragraph doesn't earn it.

## Output

Return the full draft with the links inserted in markdown. Then, below a `---`
separator, give a short list of the links you added as `anchor text -> URL`, and
note any sentences you lightly rewrote to fit a link. If you skipped likely-looking
pages, say so in a line so the author knows the gaps were deliberate.

## Related skills

article · humanize · seo-optimize · meta · house-style · blog-context
