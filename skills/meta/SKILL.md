---
name: meta
description: "Writes the SERP-facing metadata for a post: the meta title, meta description, and URL permalink, plus the lead image tags and a minimal Article JSON-LD that decide the thumbnail in Discover and AI answers, from the post (or topic) plus the primary keyword. Use when the user says 'write the meta', 'meta title and description', 'SEO title', 'permalink', 'URL slug', 'snippet for Google', 'og:image', 'Discover', 'article schema', or asks what shows up in search results before the click. For the full post, see article. For the human-voice pass, see humanize. For on-page keyword work, see seo-optimize."
metadata:
  version: 0.3.0
---

# Meta

You write the three fields Google shows before anyone clicks: the meta title, the
meta description, and the URL permalink. These are public the moment the page is
indexed, so they are the worst place for AI-ese to leak. One stray em dash or one
"comprehensive guide" here is seen by every searcher, including the ones who never
scroll. AI assistants also quote titles and descriptions verbatim, which raises the
stakes on what they say.

You're done when each field fits its cap, leads with the searcher's words, states
something the post actually delivers, and passes the rulebook's hard rules.

## Initial assessment

- If `.agents/blog-context.md` exists, read it. A captured author voice and the
  site's URL conventions override the defaults below.
- Read the hard rules in the house-style rulebook at
  `../house-style/references/ai-tells.md`. Every field has to pass them.
- Get the primary keyword. If the user did not give one, read it off the post's H1
  and first paragraph and say which one you used. If Search Console data is
  available, use it to pick the exact phrase people search rather than guessing.
- Skim the post (or topic) so the description matches what the page delivers. A
  promise the post does not keep is a click that bounces.

## Rules

Lead with the proven keyword the reader actually types, near the front of the
title where it survives truncation. Keep the title close to the post's H1 and to
the query. Search engines rewrite titles that drift from the page, and they rewrite
most meta descriptions anyway, so a description that matches the page is the one
most likely to survive.

Carry a fact from the post instead of teasing it. "Disabling emoji scripts removes
three HTTP requests" outlives "Find out how to speed up your site," because people
and AI assistants can use it as is. The fact has to come from the post body: never
invent a result, ranking, or number, and never write "our tests" or "we found"
unless the post says so. If the post makes no specific claim, describe concretely
what it covers.

When a field holds alternatives (two prices, several options, a range), put the
value the site most wants quoted first. Skimmers and AI answers take the first
number or name they see. Write plain language a 12-year-old would follow.

No dashes. Never use an em dash or an en dash in any field. Models reach for them
to cram two ideas into a short line. Use a comma, a colon, or two short phrases
instead. A plain hyphen inside a compound word is fine.

No filler molds. Metadata attracts its own: "comprehensive guide," "ultimate guide,"
"everything you need to know," "the only X you'll ever need," "discover," "learn
how." Say what the page gives the reader.

## Field caps

- Meta title: 60 characters maximum, aim for 50 to 58 so it has headroom. Keyword
  near the front. Over 60 gets truncated in the SERP.
- Meta description: 155 characters maximum, aim for 135 to 150. Active voice, lead
  with the fact or benefit, work the keyword in naturally.
- Permalink: 2 to 5 natural-language words, lowercase, hyphen-separated, readable as
  a phrase. No stop-word padding and no IDs. Strip years and numbers unless they are
  genuinely part of the topic. Never change the slug of a published post unless the
  user asks; that needs a redirect.

Show the character count beside the title and the description so the user can see
the caps hold. Models miscount characters, so if you can run code, count with it
(for example `len("...")`); otherwise count carefully and leave a few characters of
headroom.

## Image and structured data

Google Discover and AI answers show a thumbnail, and Google picks it from `og:image`
and the page's image markup. Discover's 2026 core update also demotes clickbait and
favors original, in-depth posts, so the title rules above apply to `og:title` too.

- `og:image`: the post's lead image, at least 1200px wide. The author's own photo or
  screenshot beats stock, since Discover rewards original work. Use only a real image
  path from the user or the post; with none, say the post needs a lead image instead
  of inventing a URL.
- `max-image-preview:large` in the robots meta tag, so Discover can show the large
  card. Many sites set it site-wide already; check before adding it.
- Article JSON-LD with `headline`, `image`, `datePublished`, `dateModified`, and
  `author` as a Person with `name` and `url` pointing to a real author page. Take
  every value from the post or `.agents/blog-context.md` and leave out any field you
  can't fill truthfully. Change `dateModified` only when the content changed in
  substance (see refresh).

This markup earns thumbnails and ties the post to its author. It doesn't earn AI
citations on its own (see ai-seo), so keep it to these fields. If the CMS or an SEO
plugin already outputs them, give the values to fill in rather than raw markup.

## Output

Return the three fields, labeled:

- Meta title, with its character count.
- Meta description, with its character count.
- Permalink.
- The lead image recommendation and the Article JSON-LD block, unless the user only
  asked for the title and description.

Offer a couple of title or description variants when a different angle on the
keyword could win more clicks. Keep every variant inside the caps.

If the post itself gets in the way (an outdated year in the H1, a claim it
contradicts elsewhere), write the fields from what's true and add one line telling
the author what to fix in the post.

## Related skills

article · humanize · seo-optimize · blog-context · house-style · ai-seo
