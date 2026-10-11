---
name: seo-optimize
description: "When the user wants to optimize an existing draft or published post for a target keyword, improve on-page relevance, or rework a piece around what readers actually search. Also use when the user says 'optimize this for SEO', 'rank for [keyword]', 'make this post more findable', 'make this rank better', 'help me with SEO', 'add my keyword to this', or pastes a draft or URL with a keyword in mind. This is an optimization pass on content that already exists. For writing a new post from scratch, see article. For meta titles and descriptions, see meta. For internal linking, see internal-links. For AI-answer citability, see ai-seo."
metadata:
  version: 0.2.0
---

# SEO optimize

You take a draft or published post that already exists and tune it around one target
keyword, so it reads naturally and answers what searchers came for. You are not
writing from scratch, and you never stuff keywords. Readability wins every time.

You're done when the title and opening match what the searcher typed, the headings
cover the intent, the related questions are answered, no sentence exists only to hold
a keyword, and the author's argument and voice are intact.

## Initial assessment

- If `.agents/blog-context.md` exists, read it. The captured author voice and any
  product or audience notes override the defaults below. Preserve the author's
  meaning and voice; you are sharpening their piece, not replacing it.
- Read [house-style/references/ai-tells.md](../house-style/references/ai-tells.md)
  before you touch the draft. Every edit you make has to survive that rulebook.
- Get two inputs: the content (pasted text or a URL) and the primary keyword. If
  the keyword is missing, infer it from the title and opening, say which one you
  used, and proceed. If SERP context was provided, keep it handy for step 1.
- If the post is old and losing traffic, refresh is the better fit: it diagnoses the
  decline before editing.

## Method

1. Pin the target. Settle on the primary keyword, then gather the related terms and
   the top reader questions around it. If keyword-research or serp-analysis output
   is available, pull from it; otherwise infer the obvious related terms and the
   questions a searcher would type.
2. Build a short optimization brief: the intent the page must satisfy, the related
   terms worth working in, the top questions the piece should answer, and any
   section the ranking pages treat as table stakes that this one lacks. Keep it to a
   few lines. Leave word count out of it; length follows the question, and Google
   has no preferred word count.
3. Edit the draft against the brief:
   - Place the primary keyword, as a concept inflected naturally, in the title, in
     at least one H2, and early in the intro. Keep the title close to the words a
     searcher would type; search engines rewrite titles that drift from the page
     and the query, and AI search cites closely matching titles more often. Never
     force the exact string where a natural phrasing reads better.
   - Answer the main question in the first few sentences, and open each section
     with its point. That opening is what skimmers and answer engines take.
   - Weave in only the related terms that are genuinely missing, and only where they
     read as something a person would write.
   - Make every heading descriptive so the set covers the search intent. Replace
     generic headings that earn nothing.
   - Tighten structure per house-style: paragraph length, sentence variance, and
     skimmability. Cut padding rather than add it.
4. Re-read for stuffing. If any sentence exists to hold a keyword, rewrite or delete
   it. If the piece now repeats an idea, collapse it. Run the rulebook's self-check
   on every sentence you wrote or changed.

## Hard rules

- Readability and natural language come first, always. A keyword that hurts the
  sentence loses.
- Do not keyword-stuff. Do not repeat the target to hit a count.
- Do not mention SEO, keywords, search intent, or strategy anywhere in the post.
  The reader sees an article, not the machinery behind it. The notes below the post
  are for the author, so plain talk about keywords is fine there.
- Preserve the author's argument, facts, and voice. You change how findable it is,
  not what it says.
- Optimize this one page. Never propose near-duplicate pages for keyword variations;
  that's scaled content abuse and it splits the page's strength.
- Don't change the URL of a published post unless the user asks; if they do, they
  need a redirect.

## Output

Return the optimized draft first. Then, below a `---` separator, give the brief in a
few lines and a short change list in plain terms: what you added, moved, or rewrote,
and why it helps the reader find or follow the piece. No jargon, no keyword-density
talk. If the post is published, note whether the change is substantial enough to
update its "last updated" date.

## Related skills

article · refresh · humanize · meta · internal-links · ai-seo · keyword-research · serp-analysis · house-style
