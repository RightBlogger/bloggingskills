---
name: blog-context
description: "When the user wants to set up or update the foundational context for their blog — niche, audience, topic pillars, authors and their real experience, CMS, and writing voice — so every other skill stops re-asking. Also use when the user says 'set up my blog', 'blog context', 'who is my audience', 'connect my site', 'my writing voice', or is starting with this collection for the first time. Creates .agents/blog-context.md, which every other blogging skill reads first. For deciding what to write next, see content-plan. For a one-off keyword list, see keyword-research. For capturing a voice from writing samples, see brand-voice."
metadata:
  version: 0.2.0
---

# Blog context

You create and maintain the foundation file every other skill depends on:
`.agents/blog-context.md`. It records what this blog is, who it's for, how it
sounds, and what real experience it can draw on, so no skill re-interviews the user
and no skill has to invent proof.

You're done when the file exists, every section holds either a real answer or a
clearly marked gap, and the user has seen a three-line summary.

## Before anything

Check whether `.agents/blog-context.md` already exists. If it does, read it and ask
only about what's missing or stale. Don't start over on top of existing context.

## How to gather it

Infer first, then ask. If the user gives a URL and you can read the web, read the
homepage, the about page, and a few recent posts, draft every section you can, and
ask only about the gaps. Without web access, interview the user, grouping questions
so it takes one or two rounds, not ten.

## What to capture

1. Blog. Name, URL, primary niche, the goal (rank for X, drive signups, build
   authority), and other channels the posts can point to (a YouTube channel, a
   newsletter).
2. Audience. Who reads this, their level, the problems they arrive with, the words
   they actually use for them, and where they look for answers (Google, AI
   assistants, YouTube, Reddit, newsletters).
3. Pillars. The three to six topic clusters this blog owns. New posts ladder up to
   one of these.
4. Authors. Who writes or reviews posts, and the credentials or hands-on background
   that make them worth reading. A real name and bio is a trust signal for readers
   and search engines alike.
5. Experience and proof. The real material the writing skills may cite: products the
   author has used, tests they ran, results with numbers, customer stories, original
   data, photos or screenshots on hand. Writing skills cite only what's listed here
   or supplied in the request, so this section is what lets a post carry first-hand
   detail without fabricating it.
6. Voice. Tone, reading level, point of view, and any house-style deltas (spelling,
   allowed jargon, banned words). From writing samples, summarize four to six
   concrete traits; for a deeper capture, run brand-voice.
7. CMS and tools. The CMS, plus which data sources the agent can reach (Search
   Console, analytics, a keyword tool, a SERP or scraping tool, a sitemap).
8. Constraints. Anything off-limits, required disclaimers, the blog's stance on
   disclosing AI assistance, and competitor domains to avoid linking.

## Output

Write `.agents/blog-context.md` with those sections, short and scannable, using
[references/template.md](references/template.md) as the starting point. Mark unknowns
as `[unknown]` instead of guessing. Then confirm the path, summarize what you captured
in three lines, name the biggest gap (usually Experience and proof), and tell the user
which skills now read the file automatically.

## Related skills

brand-voice · content-plan · keyword-research · serp-analysis · house-style · article
