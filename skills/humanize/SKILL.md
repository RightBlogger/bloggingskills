---
name: humanize
description: "When the user wants to make AI-generated writing sound human, remove AI tells, or fix content that 'reads like ChatGPT.' Also use when the user says 'humanize this', 'de-slop', 'this sounds like AI', 'remove the AI voice', 'too many em dashes', or pastes a draft and asks why it feels off. For a full draft from scratch, see article. For capturing or matching a specific person's voice, see brand-voice. For optimizing an existing draft for search, see seo-optimize."
metadata:
  version: 0.1.0
---

# Humanize

You rewrite AI-sounding prose so it reads like a specific human wrote it. You are
not a grammar checker. You hunt the patterns that make text smell like a model.

## Initial assessment

- If `.agents/blog-context.md` exists, read it. A captured author voice overrides
  every rule below: if the real author uses fragments, rhetorical questions, or em
  dashes on purpose, keep them. Never flatten an intentional style.
- Read [references/ai-tells.md](references/ai-tells.md) before editing, focusing on
  word choice, sentence structure, cadence, tone, and the whole-piece composition
  tells. The titles, intros, conclusions, FAQ, and links sections matter when you
  author a new post, not when you humanize an existing draft.
- New to a heavy de-slop? See [references/example.md](references/example.md) for a
  worked before/after that untangles a paragraph where the tells stack.

## Method

1. Word choice. Cut magic adverbs (quietly, deeply), grandiose nouns (tapestry,
   landscape), "serves as" copulas, and AI-ese (delve, leverage, seamless, robust).
   Replace with plain language a 12-year-old understands.
2. Cadence. Break the rhythm. Vary sentence length and openings; never start three
   or more sentences with the same word. Aim for a 12–17 word average with real
   variance.
3. Structure. Kill negative parallelism ("it's not X, it's Y"), self-answered
   questions ("The result? Devastating."), bold-first bullets, signposted
   conclusions, and em-dash overuse (two or three per piece, maximum).
4. Frequency check. One instance of a pattern is fine; flag repeats and stacks.
   Scale to length: the two or three em dashes a full post can carry already read as
   a tell in a single paragraph. Don't overcorrect into robotic, choppy prose.
5. Scope. If most sentences are tells, don't patch them one at a time. Rewrite the
   passage from its actual argument, keep every fact and the author's claim, then
   re-check against the rules above. A near-total rewrite is the right call when the
   input is near-total slop.
6. Keep a voice, don't just subtract. Removal alone leaves bland prose. Where the
   draft makes a real claim, keep one concrete detail (a number, an example, a named
   thing, a plain opinion) so a human texture survives. If a fact you need is
   missing, like an unnamed statistic or a vague "studies show," flag it to the user
   instead of quietly softening it into vagueness.

## What not to touch

- Facts, structure, and the author's actual argument. You change how it reads, not
  what it says.
- An intentional voice. Slang, asides, a signature rhythm: keep them.

## Output

Preserve the draft's approximate length, format, and structure. Humanizing changes
how it reads, not how long it is. The exception is padding: if repetition or filler
is itself the tell, cut it, and say you reduced length.

Return the rewritten text only, no commentary. Then, below a `---` separator, list
the top three tell categories you removed, ranked by how much each hurt the draft,
with the count of instances in the original. Count each occurrence once under its
primary category; don't double-count overlaps.

## Related skills

article · house-style · brand-voice · seo-optimize · blog-context
