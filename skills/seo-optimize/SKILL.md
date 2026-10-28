---
name: seo-optimize
description: "Tunes an existing draft or published post around one target keyword so its title, opening, and headings match what searchers want, without stuffing. Use when the user says 'optimize this for SEO', 'rank for [keyword]', 'make this more findable', 'make this rank better', or 'help me with SEO' about content that exists. For a new post, see article. For a post losing traffic, see refresh. For meta fields, see meta. For AI citations, see ai-seo."
metadata:
  version: 0.3.0
---

# SEO optimize

You take a draft or published post that already exists and tune it around one target
keyword, so it reads naturally and answers what searchers came for. You are not
writing from scratch, and you never stuff keywords. Readability wins every time.

You're done when the title and opening match what the searcher typed, the headings
cover the intent, the related questions are answered, no sentence exists only to hold
a keyword, and the author's facts, argument, and voice are intact.

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

- A keyword that hurts the sentence loses. Never repeat the target to hit a count.
- Keep SEO, keywords, search intent, and strategy out of the post itself. The reader
  sees an article, not the machinery behind it. The notes below the post are for the
  author, so plain talk about keywords is fine there.
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
