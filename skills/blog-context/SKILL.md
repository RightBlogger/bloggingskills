---
name: blog-context
description: "When the user wants to set up or update the foundational context for their blog — niche, audience, topic pillars, CMS, and writing voice — so every other skill stops re-asking. Also use when the user says 'set up my blog', 'blog context', 'who is my audience', 'connect my site', 'my writing voice', or is starting with this collection for the first time. Creates .agents/blog-context.md, which every other blogging skill reads first. For a one-off keyword list, see keyword-research. For capturing a voice from writing samples, see brand-voice."
metadata:
  version: 0.1.0
---

# Blog context

You create and maintain the foundation file every other skill depends on:
`.agents/blog-context.md`. It records what this blog is, who it's for, and how it
sounds, so no skill ever has to re-interview the user.

## Before anything

Check whether `.agents/blog-context.md` already exists. If it does, read it and ask
only what's missing or stale. Don't start over on top of existing context.

## What to capture

Interview the user, or infer from their site if they give a URL, and write these
sections:

1. Blog. Name, URL, primary niche, and the goal (rank for X, drive signups, build
   authority).
2. Audience. Who reads this, their level (beginner vs practitioner), the problems
   they arrive with, and the words they actually use for them.
3. Pillars. The three to six core topic clusters this blog owns. New posts should
   ladder up to one of these.
4. Voice. Tone (conversational, editorial, technical), reading level, point of view
   (first / second / third person), and any house-style deltas (spelling, allowed
   jargon, banned words). If the user has writing samples, summarize the voice in
   four to six concrete traits, and record them in the Voice section so every
   skill writes in them. For a deeper capture from real writing samples, run
   brand-voice.
5. CMS and tools. WordPress, Ghost, or Webflow, plus which data sources exist
   (Search Console, analytics, a knowledge base).
6. Constraints. Anything off-limits, required disclaimers, or competitor domains to
   avoid linking.

## Output

Write `.agents/blog-context.md` with those sections, short and scannable.
[references/template.md](references/template.md) is a fillable starting point. Confirm
the path, summarize what you captured in three lines, and tell the user which skills
will now read it automatically.

## Related skills

brand-voice · keyword-research · serp-analysis · house-style · article
