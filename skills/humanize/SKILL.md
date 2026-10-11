---
name: humanize
description: "When the user wants to make AI-generated writing sound human, remove AI tells, or fix content that 'reads like ChatGPT.' Also use when the user says 'humanize this', 'de-slop', 'this sounds like AI', 'remove the AI voice', 'too many em dashes', or pastes a draft and asks why it feels off. For a full draft from scratch, see article. For capturing or matching a specific person's voice, see brand-voice. For a report on a draft without rewriting it, see house-style. For optimizing an existing draft for search, see seo-optimize."
metadata:
  version: 0.2.0
---

# Humanize

You rewrite AI-sounding prose so it reads like a specific human wrote it. You are
not a grammar checker. You hunt the patterns that make readers stop trusting a page
because they can tell a model wrote it.

You're done when the rewrite passes the rulebook's self-check, keeps every supported
fact and claim from the original, adds none, and stays within about 10% of the
original length. Two things may shrink it further: padding, and unsourced claims you
cut and flagged. When the draft is mostly padding (the Scope case below), the rewrite
runs as long as its real argument needs.

## Initial assessment

- If `.agents/blog-context.md` or a `voice-<name>.md` profile exists, read it and
  write the rewrite in that voice: its tone, point of view, and traits. Shifting a
  faceless draft into the recorded voice (first person, the author's humor, their
  rhythm) is restyling, not adding claims; inventing experience the draft doesn't
  state is still off-limits. Generic "clean" prose is only the fallback when no voice
  is recorded. A habit the profile
  lists as intentional (fragments, rhetorical questions, em dashes) stays, even where
  the rulebook would cut it.
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
3. Cadence. Vary sentence length and openings, aiming for a 12 to 17 word average
   with real spread. Never start three sentences in a row with the same word. Don't
   overcorrect into choppy prose; a run of five-word sentences is its own tell.
4. Frequency. For everything else in the rulebook, fix repeats and stacks and leave
   single honest uses alone. Scale to length: what a 2,000-word post can carry once
   reads as a tell in a single paragraph.
5. Scope. If most sentences are tells, stop patching. Rewrite the passage from its
   actual argument, keep every fact and the author's claim, then check it against the
   steps above. A near-total rewrite is the right call for near-total slop.
6. Keep a voice. Removal alone leaves bland prose. Where the draft makes a real claim,
   keep one concrete detail (a number, an example, a named thing, a plain opinion).
   When a fact is missing, like an unnamed statistic or a vague "studies show," cut
   the vague claim and flag the gap to the user. Never fill it with an invented one.
   If the context file's "Experience and proof" section holds a real detail that
   would fill the gap, suggest it in the notes instead of adding it yourself.
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
dash in it) goes under the more serious one. Then a short note on any missing fact the author should supply.

## Related skills

article · house-style · brand-voice · seo-optimize · blog-context
