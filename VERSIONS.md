# Skill versions

The canonical version table. Each skill carries its own `metadata.version`. The repo
version tracks the collection as a whole.

Repo version: 0.6.0

| Skill | Version |
|-------|---------|
| blog-context | 0.2.1 |
| brand-voice | 0.3.0 |
| house-style | 0.4.0 |
| content-plan | 0.2.1 |
| keyword-research | 0.4.0 |
| serp-analysis | 0.4.1 |
| article | 0.6.0 |
| humanize | 0.4.0 |
| seo-optimize | 0.3.1 |
| refresh | 0.3.2 |
| internal-links | 0.3.1 |
| meta | 0.4.1 |
| ai-seo | 0.4.0 |
| youtube-to-blog | 0.4.1 |

## 0.6.0

Built from a November 2026 research pass: Anthropic's Fable 5.1, 5.2, and Opus 5.5
prompting guides, OpenAI's GPT-6 skills guidance, the SlopShape study of AI blog
structure, and what writers on Reddit and X report actually works.

- Rulebook: a new "tidy, self-announcing post" section. In a 2026 study, a
  classifier reading structure alone told AI blog posts from human ones with a
  detection score of 97 out of 100, and rewording barely moved it. The rulebook now
  names the shape and splits it in two: a roadmap paragraph, a duplicate summary
  block, a recap close, and old-way-versus-new framing get fixed wherever they
  appear; nothing for the reader to do and a voice with no person in it are
  judgment calls. A direct answer in the intro is explicitly kept. Conclusions no
  longer "tie back to the opening"; they end on something new.
- Rulebook: new tells for current models: mannered prose (Anthropic's term, "a dial
  worth turning"), compressed shorthand, no position, and "genuinely" and
  "honestly" as inflating adverbs. The self-check now starts by reading the first and
  last paragraphs together, and says to run once, since a second tells-only pass
  tends to make text worse.
- Rulebook: sentence, paragraph, and intro rules lead with the target (a phone
  reader, varied rhythm) and keep the numbers as rough guides for the whole piece,
  not caps on each sentence, because current models follow style rules literally
  and caps make prose choppy. Drafting writes toward positive defaults and uses the
  lists as a checklist.
- `humanize`: a new "Shape" step cuts the roadmap paragraph and duplicate summaries,
  rewrites a recap close while keeping the conclusion, and flags what needs the
  author's material. Facts the author wrote stay and get flagged for checking (only
  vague authority and unclaimed experience are cut), a self-contradicting draft keeps
  the body's number and flags the conflict, and it stops after one pass.
- `ai-seo`: the answer-first opening is the summary. A separate "Key takeaways" list
  is now only for long reference posts (roughly 2,000 words or more), never alongside
  a recap close, and an existing one on a short post gets folded into the opening. Evidence adds
  the SlopShape numbers, Gemini 4 Hydrogen in AI Mode, a reported November Search
  Console logging gap (secondary source), and Google's planned AI-training robots
  token.
- `brand-voice`: asks for varied samples, since models copy whatever samples share,
  takes anchor lines from different samples, skips anchors that only work because
  of a fact about the author, and notes per trait which mode (post, email, social)
  it belongs to. The rulebook says to imitate anchor lines, never reuse them.
- `article`: rereads the voice's anchor lines right before drafting, and runs the
  self-check once or humanize's method, not both.
- `house-style`: audits whole-piece shape, not only lines. The audit table gains
  shape tiers, orders by damage, and lists facts that contradict each other.
- `refresh`: Google update list adds the November 2026 core update, the Hydrogen
  switch, and the October AI-content guidance change.
- Skills follow their own rulebook: intensifiers like "genuinely" and "truly" removed
  (patch bumps for internal-links, meta, seo-optimize, and serp-analysis;
  youtube-to-blog picks up article's drafting changes).
- Tests: six near-miss routing cases where no skill should fire (`"expect": null`).
- AGENTS.md adds three authoring rules: targets over numeric limits, samples over
  adjectives, shape before words.

## 0.5.0

- Descriptions rewritten to current skill-authoring guidance: third person, the use
  case first, one trigger phrase per distinct request, scope boundaries kept. The
  always-loaded description text drops by about a third (8,262 to 5,650 characters).
- Pruned rules that were stated twice. `article/references/sections.md` is gone:
  its intro, conclusion, and FAQ rules moved into the rulebook, and its section
  rule now sits in article's drafting step. `youtube-to-blog` points to article's
  length tiers instead of copying them. `meta`, `humanize`, and `internal-links`
  point to the rulebook instead of restating it, and `seo-optimize` trims its hard
  rules to the ones stated nowhere else.
- The rulebook's Links section adds "learn more" to the banned anchors, and the
  conclusion is specified as an H2.
- Cut lines that don't change behavior (intent definitions, "keep it scannable",
  hand-off notes the descriptions already carry) and dated facts in `meta`.
- `house-style` gains a "done when" line. The rulebook opens with a contents line.
- AGENTS.md: description rules, a no-op test, a contents line for long references,
  and a corrected note on how models handle conflicting rules.

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
