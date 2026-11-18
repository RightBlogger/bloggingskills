---
name: humanize
description: "Rewrites AI-sounding prose so it reads like a person wrote it, removing AI tells (em dashes, 'it's not X, it's Y', model vocabulary, stock openers) while keeping every fact. Use when the user says 'humanize this', 'de-slop', 'this sounds like AI', 'robotic', 'like ChatGPT', or 'too many em dashes', or asks why a draft feels off. For a report without a rewrite, see house-style. For matching a specific person's voice, see brand-voice. For a new post, see article."
metadata:
  version: 0.4.0
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
  "tidy, self-announcing post" habits follow that section's own split. The length
  and section rules
  in the title, intro, and conclusion sections are for authoring, so otherwise leave
  the draft's structure alone.
- Facing a paragraph where the tells stack? See
  [references/example.md](references/example.md) for a worked before and after.

## Method

1. Hard rules first. Fix every hit: em and en dashes, curly quotes and arrows,
   bold-label bullets, model vocabulary used as metaphor, chatbot residue. These are
   what readers clock fastest.
2. Shape. Structure gives a draft away before its words do, and rewording doesn't
   change it. Cut a roadmap paragraph ("In this post, we'll cover..."), and keep a
   direct answer in the intro. If the cuts leave the intro empty, open with the
   post's bottom line, built from facts already in the body. Cut a takeaways box or recap section that repeats the
   body, unless the post is a long reference piece and the close doesn't also recap;
   move any fact found only in the box into the body. If the conclusion recaps the
   opening or the body, rewrite it to end on the next step, a caveat, or the last
   real point, and keep the conclusion itself. Rewrite old-way-versus-new-way framing
   nobody defends. A post with nothing for the reader to use, or a voice with no
   person in it, needs material you don't have: name it in the notes. These are
   deletions and one rewritten close, not a reorganized draft.
3. Sentences. Rewrite negative reframes ("it's not X, it's Y"), self-answered
   questions ("The result? Devastating."), stacked threes, participle padding,
   mannered metaphors, and signposted conclusions into direct statements.
4. Cadence. Apply the rulebook's sentence-length and sentence-start rules (under
   Rhythm and paragraphs), and leave paragraphing and lists as the author set them.
   Aim for spread, not shortness: a run of five-word sentences is its own tell.
5. Frequency. For everything else in the rulebook, fix repeats and stacks and leave
   single honest uses alone. Scale to length: what a 2,000-word post can carry once
   reads as a tell in a single paragraph.
6. Scope. If most sentences are tells, stop patching. Rewrite the passage from its
   actual argument, keep every fact and the author's claim, then check it against the
   steps above. A near-total rewrite is the right call for near-total slop.
7. Keep a voice. Removal alone leaves bland prose. Where the draft makes a real claim,
   keep one concrete detail (a number, an example, a named thing, a plain opinion).
   Specific facts the author wrote (a number, a date, a product detail) are the
   author's to stand behind: keep them, and list any that look worth checking in the
   notes. Cut vague authority ("studies show," "experts say") and any claim of
   experience the draft doesn't make, per the no-fabrication rule. If the draft
   contradicts itself (two different numbers for one thing), keep the body's
   version and flag the conflict. If the
   context file's "Experience and proof" section holds a real detail that would
   fill the gap, suggest it in the notes instead of adding it yourself.
8. Voice pass. Reread the rewrite against the recorded voice. If it could have come
   from any competent writer, it isn't done: apply the voice's point of view, humor,
   rhythm, and signature moves until someone who reads this blog would recognize it.
   With no recorded voice, aim for a plain, specific, slightly opinionated register
   rather than neutral filler, and keep the draft's point of view.

Make one pass through these steps, then stop. A second pass that hunts only for
tells tends to make text worse: it removes the author's voice and replaces one
pattern with another.

## What to preserve

The facts, the argument, the structure (minus the shape habits step 2 cuts), the
format (markdown stays markdown, a list stays a list), the genre, and any
intentional voice the draft already has: slang, asides, a signature rhythm. When the
draft has no voice of its own, the recorded voice supplies one. You change how it
reads, not what it says.

## Output

Return the rewritten text, with no commentary above it. If you cut length because
padding was the tell, say so in the notes. The notes don't count toward the length.

Then, below a `---` line, list the top three tell categories you removed, using the
rulebook's own rule names, with the count of instances in the original. Rank
hard-rule hits and the shape habits fixed in step 2 above frequency tells, then by
count. Each bullet, dash, or phrase is one instance (a box or list that is one tell
counts once), and each counts once: a span that breaks two rules (a reframe with an
em dash in it) goes under the more serious one. Then a short note on any missing
fact the author should supply.

## Related skills

article · house-style · brand-voice · seo-optimize · blog-context
