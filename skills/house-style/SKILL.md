---
name: house-style
description: "When the user wants to define, apply, or enforce a consistent writing style across their blog, or check whether a draft follows it. Also use when the user says 'house style', 'style guide', 'make it consistent', 'does this follow our style', 'set our writing rules', 'tone of voice', or asks why their content keeps reading like AI across posts. This is the shared quality layer every other blogging skill reads. For rewriting one AI-sounding draft, see humanize. For the blog's niche, audience, voice, and CMS setup, see blog-context. For writing a post from scratch, see article."
metadata:
  version: 0.1.0
---

# House style

You own the writing standard for this blog: the rules that keep every post
readable, human, and consistent no matter which skill or which day produced it.
Every writing skill in this collection reads this rulebook before it drafts or
edits.

## The rulebook

The full standard lives in [references/ai-tells.md](references/ai-tells.md): word
choice, sentence cadence, paragraph structure, formatting, titles, intros,
conclusions, FAQ, and links. Read it before anything else. It merges a community
AI-tell catalog with rules distilled from a production blog engine.

Two principles override the details:

- Frequency, not prohibition. One of any pattern is fine; repeats and stacks are
  the tell.
- A captured human voice wins. If `.agents/blog-context.md` records the author's
  real voice, it overrides any "sound human" rule here. Never flatten an
  intentional style.

## What this skill does

1. Apply. When another skill writes, it pulls these rules in. The rulebook is the
   contract; you don't need to restate it.
2. Audit. Handed a draft, score it against the rulebook. Walk the sections of
   ai-tells.md and flag concrete violations, each with the offending quote and a
   fix. Lead with the highest-frequency offenders.
3. Customize. When the user wants their own variations (British spelling, an Oxford
   comma policy, jargon allowed for an expert audience, brand-banned words), record
   those deltas at the top of `.agents/blog-context.md` so every skill inherits
   them.

## Output (audit mode)

- A one-line verdict: does this read human, and the top three reasons.
- A table of violations: pattern, offending quote, fix.
- A count of the worst repeat offenders (em dashes: 14, "it's not X": 6).
- Don't rewrite the whole piece here. Report and point the user to humanize.

## Related skills

humanize · brand-voice · article · blog-context · seo-optimize
