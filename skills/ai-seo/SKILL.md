---
name: ai-seo
description: "When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user says 'AI SEO', 'AEO', 'GEO', 'answer engine optimization', 'generative engine optimization', 'optimize for ChatGPT', 'optimize for Perplexity', 'AI Overviews', 'get cited by AI', 'AI citations', or 'optimize for Gemini'. This is about extractability and trust signals, not ranking. For on-page keyword optimization, see seo-optimize. For human-voice editing, see humanize. For SERP and competitor context, see serp-analysis."
metadata:
  version: 0.1.0
---

# AI SEO

You make a blog post citable by AI answer engines: ChatGPT, Perplexity, Google AI
Overviews, Gemini, and Claude. The goal is getting the page quoted in an answer,
not ranked in a list of ten blue links. Engines pull self-contained sentences and
short blocks out of context, so you edit for extractability and trust. This is
answer-engine and generative-engine optimization at the post level (AEO, GEO).

This is not the same job as on-page search SEO (that's seo-optimize) or making the
voice sound human (that's humanize). Those tune keywords and tone. You tune whether
a machine can lift a clean, trustworthy chunk from the page.

## Initial assessment

- If `.agents/blog-context.md` exists, read it. Use the post's core question, the
  named author and their credentials, any proprietary data, and the publish or
  last-updated date. A captured author voice still wins over any rule here.
- Take the input as text or a URL. Identify the one question this page answers. If
  you cannot state it in a sentence, the page has no answer for an engine to lift,
  and that is the first thing to fix.

## Method

Audit the post against the checklist below, then apply or propose each edit.

1. Answer-first block (BLUF). Put a direct, self-contained answer to the core
   question near the top, around 40 to 50 words, phrased so an engine can quote it
   verbatim with no surrounding context.
2. Key takeaways. Add a short, scannable summary of the main points near the top.
   Engines lift these blocks often, so make each line stand on its own.
3. Question-style headings. Reword section headings to match how people actually
   ask, so each section maps to a real prompt a reader would type into an AI tool.
4. FAQ. Add 4 to 6 questions readers ask AI tools, each answered first and direct
   in 2 to 4 sentences. The article skill covers this writing pattern; reuse it.
5. Self-contained claims. Rewrite important sentences so each holds up alone, out
   of context. Replace vague phrasing with specific numbers, named things, and
   dates. Engines quote sentences, not whole pages.
6. Experience and trust signals (E-E-A-T). Surface first-hand observation,
   proprietary data, and concrete examples. Show a named author with credentials
   and a visible publication or last-updated date. These are what make a quote safe
   to cite.
7. Structured data. Recommend the schema that fits, usually Article plus FAQ as
   JSON-LD, so the content is machine-readable. Do not write the markup here; name the
   types that fit so the JSON-LD can be generated as a separate step.

Respect frequency over prohibition. One answer-first block and one takeaways list
is the point; do not turn the whole post into stacked summary boxes.

## Output

Lead with a short AEO audit: what is missing against the seven checks above. Then
give the concrete edits, applied or proposed, in this order:

- the answer-first block (the 40 to 50 word version, ready to paste)
- the key takeaways list
- the reworked question-style headings
- the FAQ questions and answer-first responses
- a one-line schema recommendation naming the types that fit

Keep the audit tight and the edits ready to drop in. Do not restate the post back
to the user.

## Related skills

seo-optimize · serp-analysis · article · humanize · house-style
