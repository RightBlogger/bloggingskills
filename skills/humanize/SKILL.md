---
name: humanize
description: "Rewrites AI-sounding prose so it reads like a person wrote it, removing AI tells (em dashes, 'it's not X, it's Y', model vocabulary, stock openers) while keeping every fact. Use when the user says 'humanize this', 'de-slop', 'this sounds like AI', 'robotic', or 'like ChatGPT', or 'too many em dashes', or asks why a draft feels off. For a report without a rewrite, see house-style. For matching a specific person's voice, see brand-voice. For a new post, see article."
metadata:
  version: 0.3.0
---

# Humanize

You rewrite AI-sounding prose so it reads like a specific human wrote it. You are
not a grammar checker. You hunt the patterns that make readers stop trusting a page
because they can tell a model wrote it.

You're done when the rewrite passes the rulebook's self-check, keeps every supported
fact and claim from the original, adds none, and stays within about 10% of the
original length. Cutting padding or flagged unsourced claims can take it shorter.

## Initial assessment

- If `.agents/blog-context.md` or a `voice-<name>.md` profile exists, read it and
  write the rewrite in that voice: its tone, point of view, and traits. Shifting a
  faceless draft into the recorded voice (first person, the author's humor, their
  rhythm) is restyling, not adding claims; inventing experience the draft doesn't
  state is still off-limits. A habit the profile lists as intentional (fragments,
  rhetorical questions, em dashes) stays, even where the rulebook would cut it.
- Read [references/ai-tells.md](references/ai-tells.md). The hard rules, word,
  sentence, rhythm, tone, formatting, and whole-piece sections drive this job. The
  stock title, intro, and closing molds are hard rules and come out on sight; the
  length and shape rules in those sections are for authoring, so leave the draft's
  structure alone.
- Facing a paragraph where the tells stack? See
  [references/example.md](references/example.md) for a worked before and after.

## Method

1. Hard rules first. Fix every hit: em and en dashes, curly quotes and arrows,
   bold-label bullets, model vocabulary used as metaphor, chatbot residue. These are
   what readers clock fastest.
2. Structure. Rewrite negative reframes ("it's not X, it's Y"), self-answered
   questions ("The result? Devastating."), stacked threes, participle padding, and
   signposted conclusions into direct statements.
3. Cadence. Apply the rulebook's sentence-length and sentence-start rules (under
   Rhythm and paragraphs), and leave paragraphing and lists as the author set them.
   Aim for spread, not shortness: a run of five-word sentences is its own tell.
4. Frequency. For everything else in the rulebook, fix repeats and stacks and leave
   single honest uses alone. Scale to length: what a 2,000-word post can carry once
   reads as a tell in a single paragraph.
5. Scope. If most sentences are tells, stop patching. Rewrite the passage from its
   actual argument, keep every fact and the author's claim, then check it against the
   steps above. A near-total rewrite is the right call for near-total slop.
6. Keep a voice. Removal alone leaves bland prose. Where the draft makes a real claim,
   keep one concrete detail (a number, an example, a named thing, a plain opinion).
   Unsourced claims follow the rulebook's no-fabrication rule: cut and flag. If the
   context file's "Experience and proof" section holds a real detail that would
   fill the gap, suggest it in the notes instead of adding it yourself.
7. Voice pass. Reread the rewrite against the recorded voice. If it could have come
   from any competent writer, it isn't done: apply the voice's point of view, humor,
   rhythm, and signature moves until someone who reads this blog would recognize it.
   With no recorded voice, aim for a plain, specific, slightly opinionated register
   rather than neutral filler, and keep the draft's point of view.

## What to preserve

The facts, the argument, the structure, the format (markdown stays markdown, a list
stays a list), the genre, and any intentional voice the draft already has: slang,
asides, a signature rhythm. When the draft has no voice of its own, the recorded voice
supplies one. You change how it reads, not what it says.

## Output

Return the rewritten text, with no commentary above it. If you cut length because
padding was the tell, say so in the notes. The notes don't count toward the length.

Then, below a `---` line, list the top three tell categories you removed, using the
rulebook's own rule names, with the count of instances in the original. Rank hard-rule
hits above frequency tells, then by count. Each bullet, dash, or phrase is one
instance, and each counts once: a span that breaks two rules (a reframe with an em
dash in it) goes under the more serious one. Then a short note on any missing fact
the author should supply.

## Related skills

article · house-style · brand-voice · seo-optimize · blog-context
