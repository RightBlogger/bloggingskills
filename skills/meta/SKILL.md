---
name: meta
description: "Writes the SERP-facing metadata for a post: the meta title, meta description, and URL permalink, from the post (or topic) plus the primary keyword. Use when the user says 'write the meta', 'meta title and description', 'SEO title', 'permalink', 'URL slug', 'snippet for Google', or asks what shows up in search results before the click. For the full post, see article. For the human-voice pass, see humanize. For on-page keyword work, see seo-optimize."
metadata:
  version: 0.1.0
---

# Meta

You write the three fields Google shows before anyone clicks: the meta title, the
meta description, and the URL permalink. These are public the moment the page is
indexed, so they are the worst place for AI-ese to leak. One stray em dash or one
"comprehensive guide" here is seen by every searcher, not just the readers who
scroll.

## Initial assessment

- If `.agents/blog-context.md` exists, read it. A captured author voice and the
  site's URL conventions override the defaults below.
- Get the primary keyword. If the user did not give one, ask, or read it off the
  post's H1 and first paragraph. If Search Console data is available, use it to
  pick the exact phrase people search rather than guessing.
- Skim the post (or topic) so the description matches what the page delivers. A
  promise the post does not keep is a click that bounces.

## Rules

Lead with the proven keyword the reader actually types, near the front of the
title where it survives truncation. Promise one specific benefit, not a vague
one: "Compare 2026 prices and uptime" beats "everything about hosting". Write
plain language a 12-year-old would follow.

No dashes. Never use an em dash or an en dash in any field. Models reach for them
to cram two ideas into a short line. Use a comma, a colon, or two short phrases
instead.

No AI-ese. Cut "dive into", "delve into", "leverage", "unlock", "game-changer",
"seamless", "comprehensive guide", "ultimate guide", "in conclusion", "the only X
you'll ever need", and "everything you need to know". Say the plain thing.

## Field caps

- Meta title: 60 characters maximum, aim for 50 to 58 so it has headroom. Keyword
  near the front. Over 60 gets truncated in the SERP.
- Meta description: 155 characters maximum, aim for 135 to 150. Active voice, spark
  curiosity, work the keyword in naturally.
- Permalink: 2 to 5 words, lowercase, hyphen-separated. No stop-word padding. Strip
  years and numbers unless they are genuinely part of the topic.

Count the characters yourself and show the count beside the title and the
description so the user can see the caps are respected.

## Output

Return the three fields, labeled:

- Meta title, with its character count.
- Meta description, with its character count.
- Permalink.

Offer a couple of title or description variants when a different angle on the
keyword could win more clicks. Keep every variant inside the caps.

## Related skills

article · humanize · seo-optimize · blog-context · house-style · ai-seo
