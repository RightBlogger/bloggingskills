---
name: house-style
description: "Audits a draft against the collection's writing rulebook of AI tells without rewriting it, and records a blog's own style variations. The rulebook is the shared standard every writing skill reads. Use when the user says 'house style', 'style guide', 'does this follow our style', 'audit this draft', or 'set our writing rules'. For rewriting an AI-sounding draft, see humanize. For niche, audience, and voice setup, see blog-context."
metadata:
  version: 0.4.0
---

# House style

You own the writing standard for this blog: the rules that keep every post
readable, human, and consistent no matter which skill or which day produced it.
Every writing skill in this collection reads this rulebook before it drafts or
edits.

You're done when an audit lists every hard-rule hit, every repeating tell, and any
habits of the tidy, self-announcing post, each with a fix, or when the user's own
variations are recorded where every skill reads them.

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

1. Audit. Handed a draft, report against the rulebook without rewriting it. List
   every hard-rule hit, then the frequency tells that repeat, each with the offending
   quote and a fix. Check the whole-piece shape too (the rulebook's "tidy,
   self-announcing post" section), since structure gives a draft away faster than
   any word.
2. Customize. When the user wants their own variations (British spelling, an Oxford
   comma policy, jargon allowed for an expert audience, brand-banned words), record
   them under "House-style deltas" in the Voice section of `.agents/blog-context.md`
   so every skill inherits them. Don't edit the rulebook itself for one blog's
   preferences.

## Output (audit mode)

- A one-line verdict: does this read human, and the top three reasons.
- A table of violations: tier (hard rule, shape fix, shape judgment call, or
  frequency tell), pattern, offending quote, fix. Order it by damage: hard-rule hits
  and shape fixes first, then judgment calls, then frequency tells. A hit that fits
  two rules goes under the more serious one.
- A count of the worst repeat offenders (em dashes: 14, "it's not X": 6), when any
  pattern repeats.
- Facts that contradict each other inside the draft, if any, so the author can pick
  one.
- A pointer to humanize for the rewrite. The audit itself doesn't rewrite.

## Related skills

humanize · brand-voice · article · blog-context · seo-optimize
