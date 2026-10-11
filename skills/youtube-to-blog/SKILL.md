---
name: youtube-to-blog
description: "When the user wants to turn a YouTube video or its transcript into a publish-ready blog post that ranks and reads like a person wrote it, not a raw transcript dump. Also use when the user says 'turn this video into a blog post', 'write a post from this YouTube link', 'repurpose this video', 'blog version of my video', or pastes a transcript and a URL. Inputs are a video URL or transcript, a length, and whether to embed the video. For a topic or keyword instead of a video, see article. For only the human pass on existing text, see humanize."
metadata:
  version: 0.2.0
---

# YouTube to blog

You turn a video into a blog post that earns its own search traffic. The transcript
is raw material, not the draft. You reorganize its ideas around what a reader came
to find, add the context the camera skipped, and run the article skill's pipeline:
outline, section-by-section drafting, then a humanize pass.

The post is done when it stands on its own for someone who never watches the video,
follows the reader's question instead of the speaker's order, passes the rulebook's
self-check, and contains nothing the video or the user didn't support.

## Initial assessment

1. Read `.agents/blog-context.md` for niche, audience, pillars, and voice. If it
   doesn't exist, assume a general reader and a plain conversational voice, say so in
   your notes, and keep going.
2. Read the house-style rulebook at `../house-style/references/ai-tells.md` (also at
   `../article/references/ai-tells.md`; this skill builds on article and expects it
   installed alongside). It is the full writing contract.
3. Get the inputs: the video URL or transcript, the length, and whether to embed the
   video. Length tiers match the article skill: micro ~500, short ~1,000, medium
   ~1,500, long ~2,500, very-long ~3,500, and an explicit word count wins. Land
   within 90 to 105% of the target. Default to medium and embedding on when the user
   doesn't say.

## Method

### 1. Get the transcript

If a YouTube or transcript tool is available, pull the transcript, title, and channel
name with it. Otherwise ask the user to paste the transcript. Don't write the post
from the title and description alone; that produces a summary of a video you haven't
seen.

### 2. Outline around the reader, not the timeline

Mine the transcript for its substance, then reorganize it around the question a
searcher would type. A video meanders; a post answers. Use the article skill's
[outline guidance](../article/references/outline.md). The speaker's
own demonstrations, results, and opinions are this post's information gain, so give
them a section, not a passing mention. Offer a checkpoint here only if the user asked
for one.

### 3. Draft section by section

Follow the article skill's [section rules](../article/references/sections.md). Hold
the running draft in mind so no point repeats. Add the context, definitions, and
examples that went unsaid on camera, and never paraphrase the transcript line by line.
A post that restates the video in order reads like a caption file and ranks like one.

Attribute first-hand claims to the speaker ("In the video, Sam tests...") unless the
user is the speaker and wants first person.

### 4. Embed and attribute

If embedding is on, put the YouTube URL on its own line, as plain text, right after
the introduction. Most CMSs auto-embed a bare video URL; markdown link syntax or an
iframe breaks that. Credit the video and channel in the intro or the first section.

### 5. Humanize

Run the rulebook's "Quick self-check before shipping" on the full draft and fix what it
finds. Transcripts carry spoken filler ("so basically," "you know," "right?") that
reads badly on the page; cut it.

## Output

The post in markdown, starting with `# Title`, with the video URL after the intro if
embedding is on. If you are writing to a file, the file holds only the post.

Then, below a `---` line (or in your reply when you wrote a file), short notes: the
meta title, description, and slug if you wrote them, up to three timestamps worth a
screenshot, a reminder to add VideoObject structured data if the CMS doesn't, and any
assumption you made. Under 100 words.

## Related skills

blog-context · house-style · article · humanize · internal-links · meta
