---
name: youtube-to-blog
description: "When the user wants to turn a YouTube video or its transcript into a publish-ready blog post that ranks and reads like a person wrote it, not a raw transcript dump. Also use when the user says 'turn this video into a blog post', 'write a post from this YouTube link', 'repurpose this video', 'blog version of my video', or pastes a transcript and a URL. Inputs are a video URL or transcript, a length tier, and whether to embed the video. For a topic or keyword instead of a video, see article. For only the human pass on existing text, see humanize."
metadata:
  version: 0.1.0
---

# YouTube to blog

You turn a video into a blog post that earns its own search traffic. The transcript
is raw material, not the draft. You reorganize its ideas around what a reader came
to find, add context the camera skipped, and run the same pipeline the article skill
uses: outline, section-by-section drafting, then a humanize pass.

## Initial assessment

1. Read `.agents/blog-context.md` for niche, audience, pillars, and voice. If it
   doesn't exist, ask the three essentials inline (audience, goal, voice) or suggest
   running blog-context first.
2. Read the house-style rulebook at `../house-style/references/ai-tells.md` (it also
   sits at `../article/references/ai-tells.md`, since this skill builds on the article
   pipeline and expects both installed alongside). That file is the full contract; do
   not write in slop.
3. Confirm the inputs: the video URL or pasted transcript, the length tier, and
   whether the user wants the video embedded in the post.

## Length tiers (target word counts and heading count)

short ~1,000 (about 10 headings) · medium ~1,500 (about 15) · long ~2,500 (about 25)
· very-long ~3,500 (about 40). Hold the final draft within roughly 90 to 105% of
target and trim before returning.

## Method

### 1. Get the transcript

If the user gave a URL and a YouTube tool or MCP is available, pull the transcript
that way. Otherwise ask the user to paste it. Either way, capture the video title and
channel name so you can attribute the source later.

### 2. Build an outline from the transcript's ideas

Mine the transcript for its substance, then reorganize it around reader search intent
rather than the order the speaker happened to cover things. A video meanders; a post
answers the question the reader typed. Reuse the article skill's outline approach in
[../article/references/outline.md](../article/references/outline.md): intent-driven
headings that describe what the reader learns, the primary keyword or a variant in at
least one heading, related terms spread across the rest. Scale the heading count to
the length tier above. Offer the user a checkpoint here if they want one.

### 3. Draft section by section

Write each section in order, the same way the article skill does in
[../article/references/sections.md](../article/references/sections.md). Hold the
running draft in mind so you never repeat a point you already made. Aim for 250 to
350 words under each H2. Treat the topic as a concept, not a fixed phrase, so every
keyword mention reads as natural prose. Follow house-style throughout.

The job here is to add value, not to transcribe. Bring in context, examples, and
detail that went unsaid on camera. Never paraphrase the transcript line by line; a
post that just restates the video in order reads like a caption file and ranks like
one.

### 4. Embed the video if requested

If the user wants the video in the post, place the YouTube URL on its own line as
plain text, near the start, right after the introduction. A bare URL alone on a line
auto-embeds in most CMSs. Do not wrap it in markdown link syntax and do not add an
iframe; the plain URL is what triggers the embed.

### 5. Attribute the source

Credit the original video and the channel somewhere natural, so the post stands as
its own work while pointing readers back to the source.

### 6. Humanize before finishing

Run ai-tells.md's "Quick self-check before shipping" against the draft: search for em
dashes, "serves as," "it's not," "here's the," bold-colon bullets, and the
question-then-fragment-answer pattern ("Want X? Do Y."), and read every three
consecutive sentences for repeated openings. For a deeper rewrite, hand off to the
humanize skill. This is not optional; it is what separates the post from a cleaned-up
transcript. If the user wants visuals, you can also suggest screenshots at key moments
in the video, each with a short caption, but only when they help a section.

## Output

The finished post in markdown, starting with `# Title`, ready to paste into the CMS,
with the video embedded near the top if the user asked for it. Nothing else: no
preamble, no notes, no word counts.

## Related skills

blog-context · house-style · article · humanize · internal-links · meta
