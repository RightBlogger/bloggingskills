---
name: house-style
description: "When the user wants to define, apply, or enforce a consistent writing style across their blog, or check whether a draft follows it. Also use when the user says 'house style', 'style guide', 'make it consistent', 'does this follow our style', 'audit this draft', 'set our writing rules', 'tone of voice', or asks why their content keeps reading like AI across posts. This is the shared quality layer every other blogging skill reads. For rewriting one AI-sounding draft, see humanize. For the blog's niche, audience, voice, and CMS setup, see blog-context. For writing a post from scratch, see article."
metadata:
  version: 0.2.0
---

# House style

You own the writing standard for this blog: the rules that keep every post
readable, human, and consistent no matter which skill or which day produced it.
Every writing skill in this collection reads this rulebook before it drafts or
edits.

## The rulebook

The full standard lives in [references/ai-tells.md](references/ai-tells.md). Read it
before anything else. It has two tiers: hard rules that apply to every line written
(no em dashes, no fabricated claims, no chatbot residue), and frequency tells that
only count when they repeat or stack.

Precedence, highest first: the user's explicit request, then a captured voice in
`.agents/blog-context.md` or a brand-voice profile, then the rulebook. If following
the rulebook would break something the user asked for, do what the user asked and
mention the conflict in one line.

## What this skill does

1. Apply. Other skills load the rulebook themselves; it's the contract, so nothing
   needs restating.
2. Audit. Handed a draft, report against the rulebook without rewriting it. List
   every hard-rule hit, then the frequency tells that repeat, each with the offending
   quote and a fix. Lead with whatever does the most damage.
3. Customize. When the user wants their own variations (British spelling, an Oxford
   comma policy, jargon allowed for an expert audience, brand-banned words), record
   them under "House-style deltas" in the Voice section of `.agents/blog-context.md`
   so every skill inherits them. Don't edit the rulebook itself for one blog's
   preferences.

## Output (audit mode)

- A one-line verdict: does this read human, and the top three reasons.
- A table of violations: tier, pattern, offending quote, fix. Hard-rule hits first.
- A count of the worst repeat offenders (em dashes: 14, "it's not X": 6).
- A pointer to humanize for the rewrite. The audit itself doesn't rewrite.

## Related skills

humanize · brand-voice · article · blog-context · seo-optimize
