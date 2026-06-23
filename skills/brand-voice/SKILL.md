---
name: brand-voice
description: "When the user wants their content to sound like a specific person or brand, or wants to capture and reuse a writing voice from samples. Also use when the user says 'make it sound like me', 'match my voice', 'capture my writing style', 'analyze how I write', 'write in our brand voice', 'here are samples of my writing', or 'it doesn't sound like us'. Builds a reusable voice profile the other skills write in. For one-off de-slopping with no captured voice, see humanize. For the blog's niche and audience setup, see blog-context."
metadata:
  version: 0.1.0
---

# Brand voice

You capture a real person's or brand's writing voice from samples and turn it into a
reusable profile the other skills write in. A captured voice is the most valuable
context this collection holds. It overrides the generic "sound human" rules, because
the goal stops being "avoid AI tells" and becomes "sound like this specific writer."

## Initial assessment

- Read `.agents/blog-context.md` if it exists. The Voice section is where the profile
  belongs; update it rather than starting a parallel file. For more than one author,
  use `.agents/voice-<name>.md` and note which posts use which.
- Get samples. Ask for three to five pieces the author actually wrote: posts, emails,
  threads, or a URL to their writing. More and longer is better. Without samples you
  can't capture a voice, so don't invent one. If the user has none, capture stated
  preferences by interview and label the profile aspirational until real samples exist.
- Check you have enough. Count the words you actually have. Under about 400, capture only
  the traits the samples clearly support, label the profile "low-confidence (thin
  samples)" in the Voice section, and tell the user which dimensions you couldn't observe
  (usually transitions and how they sustain a long middle). Never fabricate a trait to
  reach a count.

## Method

1. Read for what repeats, not what it's about. Ignore the topics; study the moves.
   Read at least a few hundred words before you generalize, so you catch habits rather
   than one-off choices. Separate voice from belief: a trait must be a portable mechanic
   (sentence shape, person, punctuation, an opening move), not a claim only this author
   can make ("I've done this at four companies") or a topic-bound opinion. Capture the
   shape ("earns authority by citing specific reps"), never the specific claim, so the
   skills that write later never fabricate experience.
2. Profile the voice across concrete, imitable dimensions:
   - Rhythm: typical sentence length and how much it varies (short and punchy, long
     and winding, or a deliberate mix).
   - Formality and person: first or second person, contractions, slang, how close the
     writer stands to the reader.
   - Signature moves: rhetorical questions, fragments, asides, humor, analogies, direct
     address, strong openings. This is the fingerprint.
   - Vocabulary: plain or technical, the words they reach for, the words they avoid.
   - Stance: how much opinion, hedging, or certainty they show.
   - Structure: how they open, how they transition, how they land an ending.
   - Punctuation habits: dashes, parentheses, lists, emphasis. Note what they actually
     do, even when it breaks a generic rule.
3. Pull two or three short verbatim lines that are unmistakably theirs, to anchor the
   profile in real examples.

## Output

If `.agents/blog-context.md` exists, replace its Voice section. If it doesn't, create it
from blog-context's [template](../blog-context/references/template.md) and fill in only
the Voice section, leaving the other sections as bracketed prompts for blog-context to
complete later. For more than one author, write `.agents/voice-<name>.md`. The Voice
section holds:

- As many copyable traits as the samples genuinely support (up to ten; fewer is fine for
  thin samples), each with a one-line do and a tiny example. For instance: "Opens with a
  blunt claim, not a windup. Do: 'Most cold brew advice is wrong.' Not: 'Cold brew has
  become increasingly popular.'"
- A short "keep these, they're intentional" list: quirks a generic pass would flag as
  tells but that belong to this voice (a habit of fragments, a signature dash, a
  rule-of-three). Name each one in the same words ai-tells.md uses to ban it ("standalone
  fragments", "blunt cold open"), and add the line "These win over ai-tells.md wherever
  they conflict." That wording is what makes humanize and article skip them instead of
  sanding them off.
- The two or three verbatim anchor lines.

Confirm the path, then tell the user that article, humanize, and the rest now write in
this voice and that it overrides the generic anti-AI rules wherever they conflict.

## Related skills

blog-context · humanize · house-style · article
