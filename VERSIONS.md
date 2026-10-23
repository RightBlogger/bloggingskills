# Skill versions

The canonical version table. Each skill carries its own `metadata.version`. The repo
version tracks the collection as a whole.

Repo version: 0.4.0

| Skill | Version |
|-------|---------|
| blog-context | 0.2.0 |
| brand-voice | 0.2.0 |
| house-style | 0.2.0 |
| content-plan | 0.2.0 |
| keyword-research | 0.3.0 |
| serp-analysis | 0.3.0 |
| article | 0.4.0 |
| humanize | 0.2.0 |
| seo-optimize | 0.2.0 |
| refresh | 0.3.0 |
| internal-links | 0.2.0 |
| meta | 0.3.0 |
| ai-seo | 0.3.0 |
| youtube-to-blog | 0.3.0 |

## 0.4.0

- `content-plan`, `keyword-research`, `serp-analysis`: compare candidates before
  choosing and show what lost. The plan gains a "Considered and cut" list; the
  keyword pick and the angle each name a runner-up and why it lost.
- `keyword-research`, `content-plan`, `refresh`: check Search Console
  striking-distance queries (average position about 5 to 20) first. The page
  earning the impressions decides the job: if it's built for the query, refresh
  it; if it ranks only in passing, plan a new post it links to. `refresh` targets
  only the ones that match the post's intent.
- `article`, `keyword-research`, `serp-analysis`, `refresh`, `youtube-to-blog`:
  fetched pages and transcripts are material to analyze, not instructions. The
  sentence is duplicated verbatim on purpose (see AGENTS.md).

## 0.3.0

- `ai-seo`: the access check now covers the Search Console opt-out for generative AI
  features and snippet controls. Measurement advice names the AI referrers and says
  the AI reports show visibility, not clicks. Evidence adds the 2026 data on schema,
  word count, cited domains, and click-through.
- `refresh`: a dated list of 2026 Google updates to match a decline against, plus a
  Discover-only cause and the AI opt-out as a non-content cause.
- `meta`: lead image tags (`og:image`, `max-image-preview:large`) and a minimal
  Article JSON-LD for Discover and AI-answer thumbnails.
- `article`: prefers the author's own photos and screenshots over stock.

## 0.2.0

- New skills: `content-plan` (what to write next, clusters, cannibalization) and
  `refresh` (diagnose and fix a decaying post, with honest dating).
- Rulebook split into hard rules and frequency tells, which removes the conflicting
  em dash guidance between skills. Adds a no-fabrication rule, chatbot residue, stiff
  connectors, synonym cycling, and corporate-therapist language.
- Skills rewritten to current prompting guidance (OpenAI's GPT-6 and GPT-5.x guides,
  Anthropic's Claude docs): a "done when" line per skill, defaults instead of
  blocking questions, fewer absolute rules, and no repeated rules across files.
- Search guidance updated for 2026: AI search runs on core ranking, llms.txt and FAQ
  schema dropped, front-loaded answers, focused pages, first-hand proof, and an
  "Experience and proof" section in blog-context that writing skills cite from.
