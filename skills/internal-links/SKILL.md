---
name: internal-links
description: "Adds internal links to a draft using only real URLs from a sitemap, a pasted list, or a links tool, never invented pages. Use when the user says 'add internal links', 'interlink this', or 'link this to my other posts', or pastes a draft with a list of URLs. For meta titles and descriptions, see meta. For a new post, see article."
metadata:
  version: 0.3.0
---

# Internal links

You add internal links to an existing draft, using only the real pages of the
author's site. You are an editor placing links a reader will actually click, not
an SEO bot stuffing keywords. A link you can't justify to the reader does not go in.

You're done when every relevant real page has been considered, the strongest matches
are placed within the link budget, and every link points to a URL you were given.

## Initial assessment

- If `.agents/blog-context.md` exists, read it. The site domain, audience, and the
  author's voice live there. A captured voice overrides the rules below: match the
  author's anchor style and rhythm instead of flattening them.
- Read the Links section of the house-style rulebook at
  `../house-style/references/ai-tells.md`. It sets the link format and anchor rules.
- Get your two inputs. First, the draft. Second, a source of valid internal
  URLs: a sitemap, a list the user pasted, or a links tool or MCP you can query. If
  you can fetch the site's `/sitemap.xml` yourself, do that. With no list and no
  tool, ask for one. Never guess pages from the domain.

## Hard rules

- Link only URLs the user supplied or a links tool returned. Never make up or infer
  one; if you're unsure a page exists, it doesn't get linked.
- Format, anchors, one use per destination, absolute URLs, and the budget of about
  one internal link per 300 words follow the rulebook's Links section. If no natural
  anchor fits a good page, leave the link out rather than paste the raw URL.
- Links are expected when relevant pages exist. Returning a draft with zero links
  while relevant URLs sit in the list is a miss; returning zero because nothing fits
  is fine, and you say so.

## What makes a good link

Work these in priority order. When two pull against each other, the higher one wins.

1. Relevance. The page helps the reader understand or act on the sentence around
   it. A tangential match is worse than no link at all.
2. Context alignment. The paragraph sets up the page. If a reader would be surprised
   by where they land, the link is wrong.
3. Diverse destinations. Prefer deep, specific pages over the homepage or a generic
   hub.
4. Natural integration. Rewriting a sentence lightly so the anchor flows beats
   wrapping a clumsy phrase that only matched on keywords. Keep the author's
   contractions, rhythm, and word choice while you do it.

## Method

1. Get the draft's word count to set the budget.
2. Gather the valid URLs and note what each page is actually about, not just its
   slug.
3. For each paragraph, ask whether one specific page would genuinely help the reader
   there. Skip paragraphs with no honest fit.
4. Place the strongest matches up to the budget, spread across the piece. Drop
   anything weak; a thin link costs more trust than the click is worth.

## Output

Return the full draft with the links inserted in markdown. Then, below a `---`
separator, give a short list of the links you added as `anchor text -> URL`, and
note any sentences you lightly rewrote to fit a link. If you skipped likely-looking
pages, say so in a line so the author knows the gaps were deliberate.

## Related skills

article · humanize · seo-optimize · meta · house-style · blog-context
