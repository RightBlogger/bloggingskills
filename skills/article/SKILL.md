---
name: article
description: "When the user wants to write a complete, publish-ready blog post or article from a topic or keyword. Also use when the user says 'write a blog post', 'write an article about X', 'draft a post on', 'I need a 2000-word article', 'turn this keyword into a post', or gives a topic and a target length. This is the flagship that runs the full pipeline: research, outline, draft, humanize, optimize. For a video transcript instead of a topic, see youtube-to-blog. For optimizing a draft that already exists, see seo-optimize. For only humanizing existing text, see humanize."
metadata:
  version: 0.1.0
---

# Article

You write a full blog post that ranks and reads like a human wrote it. You are the
conductor of the pipeline. You don't dump a draft in one pass. You move through
research, outline, section-by-section drafting, a humanize pass, and a light
optimize pass, in that order.

## Initial assessment

1. Read `.agents/blog-context.md` for niche, audience, pillars, and voice. If it
   doesn't exist, ask the three essentials inline (audience, goal, voice) or suggest
   running blog-context first.
2. Read the house-style rulebook at `../house-style/references/ai-tells.md`. If that
   path doesn't resolve because the skill was installed alone, read the bundled copy
   at `references/ai-tells.md`. The non-negotiables are summarized below; that file
   is the full contract.
3. Confirm the target: primary keyword, length tier, and angle.

## Length tiers (target word counts)

micro ~500 · short ~1,000 · medium ~1,500 · long ~2,500 · very-long ~3,500.

Pick the target from the user's explicit word count if they gave one; otherwise map
their adjective (short, medium, long) to the tier above. If a stated number conflicts
with a tier label, for example "a short 700-word post," the explicit number wins and
becomes the target. Hold the final draft within roughly 90 to 105% of that target,
and trim before returning. Models overwrite by default.

## The pipeline

### 1. Research (skip if the user gave an outline)

Get the primary keyword and five to fifteen related terms (use keyword-research). If
you can read the SERP, note what the top results cover and where the gap is (use
serp-analysis). Pull the three to five questions real readers ask. This feeds the
outline. Don't dump it into the post. If keyword-research, serp-analysis, or web
tools aren't connected, don't skip this step and don't fabricate a SERP or invent
volumes: infer the related terms and reader questions from your own knowledge of the
topic, treat the content-gap as best-effort, and state nothing in the post you
couldn't support.

### 2. Outline (see [references/outline.md](references/outline.md))

Build an intent-driven outline: intro, H2 sections (with H3s where a section is
dense), an optional FAQ, and a conclusion. The number of H2s scales with length
(short 2 to 3, medium 4, long 5, very-long 6+). Put the primary keyword or a natural
variant in at least one heading; spread related terms across other headings.
Headings describe what the reader learns, never generic, never keyword-stuffed.
Offer the user a checkpoint here if they want one.

### 3. Draft, section by section (see [references/sections.md](references/sections.md))

Write each section in order, holding the running draft in mind so you never repeat a
point already made. Aim for 200 to 350 words under each H2, and run shorter on micro
and short posts so the whole piece stays in range. The total word budget beats the
per-section floor; never pad a section to hit a number.
Treat the keyword as a concept, not a fixed string: inflect and reorder it so every
mention reads as natural prose. Intro and conclusion follow their own rules in
sections.md. Add a FAQ only if it fits the topic.

### 4. Humanize

Before finishing, run ai-tells.md's "Quick self-check before shipping" against the
draft. Search literally for em dashes, "serves as," "it's not," "here's the,"
bold-colon bullets, and the question-then-fragment-answer pattern ("Want X? Do Y.");
cap that last one at one per post. Read every three consecutive sentences for
repeated openings. For a deeper rewrite, hand off to the humanize skill. This pass is
not optional; it's what separates this from generic AI output.

### 5. Optimize (light)

Add internal links if the user has a site (internal-links). Generate the meta title
and description (meta). Don't keyword-stuff, and never mention SEO in the output.

## Non-negotiable rules (full set in house-style)

- No em dashes in prose. No horizontal rules. No bold-colon bullets.
- Short paragraphs (1–3 sentences, under 150 words). Prose over lists.
- Vary sentence openings; never start three or more in a row with the same word.
- Use contractions. Reading level around 8th grade.
- No banned title, intro, or conclusion patterns (see ai-tells.md).
- The first line of the article is the H1: `# Title`. No meta-commentary anywhere;
  every line is reader-facing copy. Never print word counts.

## Images and embeds

Add images only where they help a section, never a hero by default. Use real
markdown image syntax with descriptive alt text; for stock photos, add a credit
line. Only embed a widget, iframe, or script if the user explicitly asks, and wrap
it in a fenced `html-embed` block so it survives publishing. Never invent embeds. If
you have no real image source (no asset library, no stock provider, no user-supplied
paths), omit images rather than invent file paths or URLs.

## Output

The finished post in markdown, starting with `# Title`, ready to paste into the CMS.
Nothing else: no preamble, no notes.

## Related skills

blog-context · brand-voice · keyword-research · serp-analysis · humanize · internal-links · meta · seo-optimize · youtube-to-blog
