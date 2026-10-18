---
name: refresh
description: "When the user wants to update an existing, already-published blog post that has gone stale or lost traffic. Also use when the user says 'refresh this post', 'update this old article', 'this post lost traffic', 'my rankings dropped on this page', 'content decay', 'make this post current', 'update it for this year', or pastes an old post or URL and asks what to fix. Diagnoses why the post declined before changing anything, then updates facts, coverage, and freshness honestly. For tuning a draft around a keyword with no decline involved, see seo-optimize. For writing a new post, see article. For deciding which posts to refresh across the whole blog, see content-plan."
metadata:
  version: 0.2.0
---

# Refresh

You bring a published post back up to date so it earns its traffic and its
citations again. Most decaying posts don't need a rewrite. They need the right fix
for the reason they slipped, which is why you diagnose before you edit.

You're done when you've named the cause of the decline, every fact, number, link,
and version in the post is current or flagged, the post covers what readers now
expect, and nothing the post still ranks for was removed.

## Initial assessment

- Read `.agents/blog-context.md` for audience, voice, and the "Experience and proof"
  section, which is where new first-hand detail can come from.
- Read the house-style rulebook at `../house-style/references/ai-tells.md` before you
  write anything new.
- Get the post: a URL to fetch or the pasted text, plus the publish date if known.
- Gather what data you can reach. With Search Console connected, pull this page's
  clicks, impressions, average position, and top queries for the last three months
  against the same period a year earlier. With a SERP or web tool, read the current
  top results for the post's main query. With neither, work from the post itself and
  say the diagnosis is inferred.

## Method

### 1. Diagnose the decline

Match the evidence to a cause. Each one calls for a different fix.

| Cause | What you see | Fix |
|-------|--------------|-----|
| Outdated | Old prices, versions, screenshots, years, dead links | Update facts in place |
| Intent shift | The top results are now a different format (a tool, a list, a video) | Restructure to the format that wins |
| Outpaced | Competitors added depth, original data, or better examples | Add the missing coverage and real information gain |
| Cannibalized | Another page on the same site ranks for the same queries | Merge into one page and redirect the other |
| Absorbed by AI answers | Impressions steady or rising, clicks falling, position stable | Make it the cited source (ai-seo) and give readers a reason to click |
| Discover-only drop | Search clicks steady, Discover traffic gone | Check the headline for clickbait and the post for depth and timeliness; check the lead image is large and original |
| Not a content problem | Deindexed, a title rewritten in the SERP, a site-wide drop, the site opted out of AI features in Search Console | Report it; editing the post won't help |

If the drop lines up with a Google update window, say which one; the dated list is
in [references/google-updates.md](references/google-updates.md). Causes often stack
(outdated and outpaced is common); name the main one first. Write
the diagnosis before touching the text. If the evidence points to "not a content
problem," stop there and say so.

### 2. Pick the scope

- Surgical update for outdated facts and light gaps. Keep the structure and the voice.
- Section rewrites for an outpaced post. Replace weak sections, keep strong ones.
- Restructure for an intent shift. Same URL, new shape.
- Merge for cannibalization. Recommend which URL survives and the redirect.

Protect what still works. If Search Console shows the post earning clicks for a query,
keep the section and heading that answer it.

### 3. Update

1. Check every claim with a date on it: prices, versions, stats, product names, UI
   steps, screenshots, and anything phrased as "currently" or "this year." Facts the
   user gives you count as verified. Replace what you can verify; leave the rest as
   written and list it in the change log. Never guess a new number or leave a
   placeholder in the post.
2. Check the old claims of experience. If the post says "we tested" or "in my
   experience" and the context file doesn't back it, rewrite the claim to what's
   true and flag the change. An old post is not exempt from the no-fabrication rule.
3. Fix or remove broken and redirected links. Add links to newer posts on the site
   when a list of real URLs or a links tool is available (internal-links).
4. Add what readers now expect, from the current top results, and one piece of
   information gain the others lack, drawn from the context file or the user.
5. Write new and changed text to the rulebook, matching the voice of the parts you
   kept. Run the rulebook's self-check on everything you wrote.
6. Revisit the title and meta description only if the angle or the year changed
   (meta), and put the suggested fields in the change log. Keep the URL.

### 4. Date it honestly

Update the "last updated" date only when the content changed in substance. Bumping
the date on an unchanged post misleads readers and search engines. Keep a year in the
title only if the content is truly year-specific, and then set it to the year of
this update.

## Output

1. The diagnosis: cause, evidence, and chosen scope, in a few lines.
2. The updated post in markdown, or for a merge, the merged post plus the redirect.
3. Below a `---` line, a change log: what you changed and why, facts the author must
   verify, any section you deliberately kept, and whether to update the published
   date.

## Related skills

seo-optimize · ai-seo · internal-links · meta · humanize · content-plan · serp-analysis · blog-context
