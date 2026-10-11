---
name: article
description: "When the user wants to write a complete, publish-ready blog post or article from a topic or keyword. Also use when the user says 'write a blog post', 'write an article about X', 'draft a post on', 'I need a 2000-word article', 'turn this keyword into a post', or gives a topic and a target length. This is the flagship that runs the full pipeline: research, outline, draft, humanize, optimize. For a video transcript instead of a topic, see youtube-to-blog. For optimizing a draft that already exists, see seo-optimize. For updating an old post, see refresh. For only humanizing existing text, see humanize."
metadata:
  version: 0.2.0
---

# Article

You write a full blog post that ranks, gets quoted by AI answer engines, and reads
like a person wrote it. You conduct the pipeline in order: research, outline,
section-by-section drafting, a humanize pass, and a light optimize pass. One-shot
drafts repeat themselves and drift off the reader's question, which is why the
order matters.

The post is done when it answers the reader's question better than what already
ranks, lands within the length target, passes the rulebook's self-check, and makes
no claim you can't trace to a source, the user, or `.agents/blog-context.md`.

## Initial assessment

1. Read `.agents/blog-context.md` for niche, audience, pillars, voice, and the
   "Experience and proof" section (real data, cases, and credentials you may cite).
   If it doesn't exist, don't stop to interview the user. Assume a general reader,
   an informative goal, and a plain conversational voice, say so in your notes, and
   suggest blog-context for next time.
2. Read the house-style rulebook at `../house-style/references/ai-tells.md`. If that
   path doesn't resolve because the skill was installed alone, read the bundled copy
   at `references/ai-tells.md`. It is the full writing contract; this file doesn't
   repeat it.
3. Settle the target: primary keyword, length, and angle. Infer what the user didn't
   state and keep going. Ask first only when two readings would produce different
   posts (for example, "Python" the language or the snake).

## Length

Tiers: micro ~500 · short ~1,000 · medium ~1,500 · long ~2,500 · very-long ~3,500.

An explicit word count wins over a tier label ("a short 700-word post" means 700).
With no length given, pick the tier serp-analysis recommends, or medium. Land within
90 to 105% of the target, counting the post with its headings and without the notes. Models overwrite by default, so trim before returning,
cutting repetition and filler first and specifics last.

## The pipeline

### 1. Research

Skip this if the user gave an outline. Otherwise get the primary keyword, five to
fifteen related terms, and the three to five questions real readers ask
(keyword-research). If you can read the live results, find what the top pages cover
and where they're weak (serp-analysis). This feeds the outline; it doesn't get
pasted into the post.

With no keyword or web tools connected, infer the terms and questions from what you
know, treat the gap as best effort, and never present invented volumes or rankings
as data.

### 2. Outline

Follow [references/outline.md](references/outline.md): an intro, H2 sections with H3s
where a section is dense, an optional FAQ, and a conclusion. Headings say what the
reader learns. Plan where the post's information gain comes from: the original
example, number, comparison, or opinion that the ranking pages lack. If the user
asked for a checkpoint, stop here and show the outline.

### 3. Draft section by section

Follow [references/sections.md](references/sections.md). Write sections in order and
hold the running draft in mind so no point repeats. Open each section with its
answer, then support it. Treat the keyword as a concept: inflect and reorder it so
every mention reads as natural prose.

Use first-hand experience, data, and examples only from the user, the context file,
or a source you can name. Where a real detail would make a section stronger and you
don't have one, write the section without it and list the spot in your notes. A
plausible invented anecdote is worse than none.

### 4. Humanize

Run the rulebook's "Quick self-check before shipping" on the full draft and fix what
it finds. Pay extra attention to the question-then-fragment pattern ("Want X? Do
Y."), which long drafts accumulate; keep it to one per post. For a heavy rewrite,
apply the humanize skill's method.

### 5. Optimize (light)

If the user has a site and a list of real URLs or a links tool, add internal links
(internal-links). Write the meta title, description, and slug (meta). Never mention
SEO, keywords, or strategy in the post itself.

## Format rules this skill adds

The rulebook covers style. These are specific to a finished post:

- The first line is the H1: `# Title`.
- Every line of the post is reader-facing copy: no notes to the user, no word counts,
  no "[insert X]" placeholders.
- Images only where they help a section, never a default hero. Use markdown image
  syntax with descriptive alt text, and only real image sources (user paths, an asset
  library, a stock provider). With no source, leave images out. For stock photos, add
  a credit line.
- Embed a widget, iframe, or script only when the user asks, inside a fenced
  `html-embed` block so it survives publishing.
- In a "best X" or comparison post where the blog sells one of the options, say so
  in the post and judge it by the same criteria as the rest. Readers discount
  self-ranked lists, and AI answers tend to cite them while leaving the publisher
  out.

## Output

The post in markdown, starting with `# Title`, ready to paste into a CMS. If you are
writing to a file, the file holds only the post.

Then, below a `---` line (or in your reply when you wrote a file), short notes for the
author:

- The meta title, description, and slug.
- Spots where first-hand experience or a real number would strengthen the post.
- Two or three places a screenshot, chart, or photo would help, if the post has no
  images.
- Any claim the author should verify before publishing.
- Assumptions you made (audience, length, angle), if any.

Keep everything after the meta fields under about 80 words. Skip a bullet that has
nothing in it.

## Related skills

blog-context · brand-voice · content-plan · keyword-research · serp-analysis · humanize · internal-links · meta · seo-optimize · ai-seo · refresh · youtube-to-blog
