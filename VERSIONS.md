# Skill versions

The canonical version table. Each skill carries its own `metadata.version`. The repo
version tracks the collection as a whole.

Repo version: 0.3.0

| Skill | Version |
|-------|---------|
| blog-context | 0.2.0 |
| brand-voice | 0.2.0 |
| house-style | 0.2.0 |
| content-plan | 0.1.0 |
| keyword-research | 0.2.0 |
| serp-analysis | 0.2.0 |
| article | 0.3.0 |
| humanize | 0.2.0 |
| seo-optimize | 0.2.0 |
| refresh | 0.2.0 |
| internal-links | 0.2.0 |
| meta | 0.3.0 |
| ai-seo | 0.3.0 |
| youtube-to-blog | 0.2.0 |

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
