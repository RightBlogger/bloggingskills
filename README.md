# Blogging Skills

Agent skills that write blog content which ranks and doesn't read like AI.

A collection of [Agent Skills](https://agentskills.io) for the full blogging
pipeline: research, outline, draft, humanize, optimize, publish. Built for people
who use a coding agent (Claude Code, Codex, Cursor, Windsurf, and anything that
supports the Agent Skills spec) to run a real content operation.

Most "write a blog post" prompts produce slop, and everyone can smell it now. This
collection's whole point is the opposite: content that ranks *and* reads like a
person wrote it. The quality bar lives in one shared rulebook,
[`ai-tells.md`](skills/house-style/references/ai-tells.md), that every writing skill
reads before it touches a draft.

## What are skills?

Skills are markdown files that give an AI agent specialized knowledge and a workflow
for a specific task. Drop them in your project and the agent recognizes when you're
doing that task and applies the right method. You can also call one directly, like
`/article` or `/humanize`.

## The point of view

- Generating a post is a commodity. Content that ranks and reads human is the scarce
  thing. The anti-slop rulebook is the product.
- Blogging is a pipeline, not a prompt. Research, outline, draft, humanize, optimize,
  publish. The skills compose; `article` conducts them.
- Write for humans first, rank second.
- These run in your repo and touch your real stuff: your CMS, your Search Console,
  your knowledge base.

## How the skills work together

Two foundation skills are read first by everything else. Then the pipeline runs.

```
foundation   blog-context   +   house-style        (read by every skill)
                 |                    |
                 |   captures niche,  |   the anti-slop rulebook every
                 |   audience, voice  |   writing skill loads before drafting
                 v                    v

pipeline
  research    keyword-research, serp-analysis
    -> outline    article  (references/outline.md)
    -> draft      article  (section by section, no redundancy)
    -> humanize   humanize          <-- the differentiator
    -> optimize   seo-optimize, internal-links, meta, ai-seo
    -> publish    your CMS

repurpose   youtube-to-blog  (the article pipeline applied to a video)
```

See each skill's "Related skills" line for the full map.

## Available skills (v0.1)

| Skill | What it does |
|-------|--------------|
| [blog-context](skills/blog-context/) | Foundation. Captures niche, audience, pillars, CMS, and voice into `.agents/blog-context.md`, read first by every other skill. |
| [house-style](skills/house-style/) | Foundation. The shared writing rulebook ([`ai-tells.md`](skills/house-style/references/ai-tells.md)). Applies to every writing skill, and audits a draft on request. |
| [brand-voice](skills/brand-voice/) | Captures a real writing voice from samples into a reusable profile the other skills write in. The captured voice overrides the generic anti-AI rules. |
| [keyword-research](skills/keyword-research/) | Turns a seed topic into one primary keyword plus related terms grouped by search intent. |
| [serp-analysis](skills/serp-analysis/) | Reads the live top results for a keyword and returns a content brief: intent, must-cover topics, the gap, and the winning angle. |
| [article](skills/article/) | The flagship. Runs the whole pipeline to produce a publish-ready post from a topic. |
| [humanize](skills/humanize/) | The hero. Strips AI tells and restores a human voice without flattening intentional style. |
| [seo-optimize](skills/seo-optimize/) | Optimizes a draft that already exists against a target keyword, readability-first, no stuffing. |
| [internal-links](skills/internal-links/) | Inserts relevant internal links using your real pages, with descriptive anchors and no invented URLs. |
| [meta](skills/meta/) | Writes the SERP-facing meta title, description, and permalink inside the hard character limits. |
| [ai-seo](skills/ai-seo/) | Makes a post citable by AI answer engines (AEO/GEO): answer-first blocks, key takeaways, FAQ, E-E-A-T. |
| [youtube-to-blog](skills/youtube-to-blog/) | Turns a video or transcript into a real post, not a transcript dump, with the video embedded. |

## Installation

### Option 1: CLI (recommended)

Use [`npx skills`](https://github.com/vercel-labs/skills) to install. Replace
`OWNER/bloggingskills` with this repo's path once it's published.

```bash
# Install all skills
npx skills add OWNER/bloggingskills

# Install specific skills
npx skills add OWNER/bloggingskills --skill article humanize

# List available skills
npx skills add OWNER/bloggingskills --list
```

This installs to `.agents/skills/` (and symlinks into `.claude/skills/` for Claude
Code).

### Option 2: Claude Code plugin

```bash
/plugin marketplace add OWNER/bloggingskills
/plugin install blogging-skills
```

### Option 3: Clone and copy

```bash
git clone https://github.com/OWNER/bloggingskills.git
cp -r bloggingskills/skills/* .agents/skills/
```

## Quickstart

The first session, start to finish:

1. Set up context once. "Set up the context for my blog" runs `blog-context` and writes
   `.agents/blog-context.md` (niche, audience, pillars, voice). Every skill reads it, so
   you explain your blog once.
2. Capture your voice (recommended). "Capture my writing voice, here are three posts I
   wrote" runs `brand-voice`. The profile makes every draft sound like you, and it
   overrides the generic anti-AI rules.
3. Write. "Write a 1,500-word post on [topic]" runs `article`: research, outline, draft,
   humanize, and a light optimize pass, in one go.
4. Polish. "This reads like AI, fix it" runs `humanize`. "Write the meta title and
   description" runs `meta`. "Add internal links from my sitemap" runs `internal-links`.
5. Connect your data (optional). With Search Console, a SERP or scraping tool, or your
   CMS wired in as an MCP or CLI, the research and optimization skills use your real
   numbers instead of estimates. See [docs/data-sources.md](docs/data-sources.md). With
   nothing connected, every skill still works by reasoning from what it knows.

## Usage

Once installed, just ask:

```
"Set up the context for my blog"        -> blog-context
"Write a 2000-word post on cold brew"   -> article
"This draft reads like ChatGPT, fix it" -> humanize
"Turn this YouTube video into a post"   -> youtube-to-blog
"Write the meta title and description"  -> meta
```

Or call a skill directly: `/article`, `/humanize`, `/seo-optimize`.

The first thing to run is `blog-context`. Every other skill reads it, so you only
explain your blog once.

## Roadmap

Shipping next, in roughly this order: `content-plan` (pillars and clusters,
anti-cannibalization), `copy-edit`, `faq`, content-type playbooks (`listicle`,
`how-to`, `comparison`, `roundup`), `podcast-to-blog`, `repurpose` (post to social,
newsletter, email), `schema`, `refresh` (update decaying posts), and `gsc-report`.

## Credits

The anti-slop rulebook is distilled from editing a high volume of model-generated
drafts in a production blog-generation system — the patterns readers reliably flag
as machine-written, and the fixes that hold up at scale.

## License

[MIT](LICENSE). Use these however you want.
