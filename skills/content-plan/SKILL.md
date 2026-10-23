---
name: content-plan
description: "When the user wants to decide what to write next, plan a batch of posts, or organize a blog into topic clusters without the posts competing with each other. Also use when the user says 'what should I write about', 'content plan', 'content calendar', 'blog topic ideas', 'topic clusters', 'plan my next 10 posts', 'content strategy for my blog', 'am I cannibalizing my own posts', or 'which old posts should I update'. Returns a prioritized list of posts, each with one keyword, one intent, and the angle only this blog can bring. For the keyword set behind a single post, see keyword-research. For writing a planned post, see article. For updating one decaying post, see refresh."
metadata:
  version: 0.2.0
---

# Content plan

You decide what this blog should publish next. The output is a short, ranked list of
posts where each one targets a distinct search intent, ladders up to a pillar, and has
an angle the blog can actually back with experience or data.

You're done when every planned post has a distinct intent no existing page already
serves, a pillar, a page type, and a reason it should exist, the list is ordered
by what to write first, and the candidates you cut are listed with their reasons.

## Initial assessment

- Read `.agents/blog-context.md`. The pillars, audience, goal, and "Experience and
  proof" sections drive this plan. If it doesn't exist, run blog-context first or
  infer the pillars from the site and label them as inferred.
- Get the inventory of what's already published: a sitemap, a CMS export, or a
  pasted list of URLs and titles. Without one, plan anyway but say you couldn't check
  for duplicates.
- Use data when it's connected. Search Console shows queries the site already gets
  impressions for, which is the strongest source of ideas. A keyword or SERP tool adds
  demand and difficulty. With neither, estimate and label estimates as such.
- Default to 10 to 15 new posts unless the user asks for a number.

## Method

1. Map the inventory. Sort existing posts under the pillars and note which pillars
   are thin. Pages that target the same intent as each other are cannibalization;
   list them for a merge.
2. Gather candidates for each pillar from:
   - Search Console queries with impressions but no page built for them. Look first
     at striking distance (an average position of about 5 to 20), where the site is
     already close. Check the page earning those impressions: if it's built for the
     query, it goes on the refresh list instead; if it only ranks in passing, plan
     the new post and have that page link to it.
   - The real problems and questions in the audience section (keyword-research can
     expand any one of them).
   - Comparisons, alternatives, and "how to choose" decisions readers face.
   - The Experience and proof section. Posts built on the author's own tests, data,
     or stories are the ones competitors can't copy, and they're what readers,
     search engines, and AI answers reward.
3. One page per intent. Merge candidates that a single page would satisfy. A quick
   test: if the same results rank for both searches, it's one post. Drop any
   candidate an existing page already serves, and add that page to the refresh list
   if it serves it badly.
4. Score each survivor on four things: fit with the blog's goal, reader demand,
   winnability (forums, thin pages, or outdated posts in the top results mean an
   opening), and the unique angle this blog can bring. Cut anything that scores low
   on the last one; a post with no angle is filler. Spread the proof: if three
   candidates all lean on the same test or story, keep the strongest one and fold the
   rest in, or the posts will repeat each other. Note each candidate you cut and
   why. A plan that shows its rejects can be checked, and writing them down stops
   the ranking from sliding toward raw search volume.
5. Shape clusters. For each pillar, name the hub page (existing or planned) and make
   sure supporting posts link up to it and across to siblings.

## Output

Open with two or three lines on what the plan is based on (the inventory, which data
sources, what's estimated). Then a table of planned posts in priority order with these
columns: working title, primary keyword, intent, page type (how-to, comparison, review,
list, explainer, opinion), pillar, demand (from data, or marked "est."), the unique
angle or proof, and the hub it links to.

Then four short lists:

- Refresh instead: existing posts to update rather than duplicate, with a one-line
  reason each (hand these to refresh).
- Merge: pages competing for the same intent, with the URL that should survive.
- Gaps in proof: planned posts that need a test, data, or story the author doesn't
  have yet.
- Considered and cut: candidates that didn't make the plan and aren't already on
  the refresh or merge lists, one line each with the reason ("a planned post
  already covers it", "no angle we can back", "ranked below the cutoff on
  demand"). Group near-duplicates on one line. "Maybe later" isn't a reason.

Save the plan to `.agents/content-plan.md` unless the user said not to, so article
and keyword-research can pick topics from it and skip what's already planned.

## Related skills

blog-context · keyword-research · serp-analysis · article · refresh · internal-links
